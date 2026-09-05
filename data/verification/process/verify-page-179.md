# Verification process log — verify-page-179


## [2026-09-05T20:51:56.399Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 179 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-179.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-179.json. Write /home/sfmqrb/git/rishe/data/verification/page-179.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 179` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:51:57.988Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:51:58.698Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:51:58.712Z] TOOL RESULT

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


## [2026-09-05T20:51:58.959Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-179.txt"
}
```


### [2026-09-05T20:51:58.987Z] TOOL RESULT

```
1	=== PDF page 179 (book page 149) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ghait, Ghaita : wavy hair  (refs POK:410)
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:410; KLN:264 | gaĕsa, gaĕsu : hair ; ges, gesuk : hair
5	  #2 (parent #1) [Persian] refs=POK:410; BQT:1870 | gîs «گیس» : hair | extra: گیسو
6	#3 (parent #0) [Greek] refs=AHD | xaitĕ : long hair
7	  #4 (parent #3) [English] refs=AHD | chaeta : bristle worm
8	--- entry 1 ---
9	ROOT Ghaita -> redirect to Ghait
10	--- entry 2 ---
11	ROOT [Indo-European] Ghans : goose  (refs POK:412; IEC:314)
12	#1 (parent #0) [Persian] refs=IEC:314; MON:2375 | ğâz «غاز» : goose
13	#2 (parent #0) [Sanskrit] refs=UEC:314; POK:412 | hamsîh : goose
14	#3 (parent #0) [Germanic] refs=AHD:1517 | gans, ganr, ganôtôn : goose
15	  #4 (parent #3) [English] refs=AHD | goose, gander, gannet
16	#5 (parent #0) [Latin] refs=AHD | ânser, hanser : goose
17	#6 (parent #0) [Greek] refs=IEC:314 | khĕn : goose
18	--- entry 3 ---
19	ROOT Ghau -> redirect to Ghu 1
20	--- entry 4 ---
21	ROOT Ghazâl -> redirect to Ğ.z.l
22	--- entry 5 ---
23	ROOT Ghdes -> redirect to Ghdies
24	
```


## [2026-09-05T20:52:02.721Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-179.json",
 "description": "Read page 179 source JSON"
}
```


### [2026-09-05T20:52:02.756Z] TOOL RESULT

```
{
  "pdf_page": 179,
  "book_page": 149,
  "entries": [
    {
      "root": {
        "name": "Ghait, Ghaita",
        "lang": "Indo-European",
        "refs": "POK:410",
        "gloss": "wavy hair"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:410; KLN:264",
          "words": [
            {"translit": "gaĕsa, gaĕsu", "gloss": "hair", "script": null},
            {"translit": "ges, gesuk", "gloss": "hair", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "POK:410; BQT:1870",
          "words": [
            {"translit": "gîs", "gloss": "hair", "script": "گیس"}
          ],
          "script_extra": "گیسو",
          "note": null,
          "quote": {
            "text": "دوش در حلقهٔ ما قصهٔ گیسوی تو بود - تا دل شب سخن از سلسلهٔ موی تو بود",
            "poet": "Hâfez"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "xaitĕ", "gloss": "long hair", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "chaeta", "gloss": "bristle worm", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Ghaita", "redirect": "Ghait"},
      "nodes": []
    },
    {
      "root": {
        "name": "Ghans",
        "lang": "Indo-European",
        "refs": "POK:412; IEC:314",
        "gloss": "goose"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "IEC:314; MON:2375",
          "words": [
            {"translit": "ğâz", "gloss": "goose", "script": "غاز"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "UEC:314; POK:412",
          "words": [
            {"translit": "hamsîh", "gloss": "goose", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD:1517",
          "words": [
            {"translit": "gans, ganr, ganôtôn", "gloss": "goose", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "goose, gander, gannet", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "ânser, hanser", "gloss": "goose", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Greek",
          "refs": "IEC:314",
          "words": [
            {"translit": "khĕn", "gloss": "goose", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Ghau", "redirect": "Ghu 1"},
      "nodes": []
    },
    {
      "root": {"name": "Ghazâl", "redirect": "Ğ.z.l"},
      "nodes": []
    },
    {
      "root": {"name": "Ghdes", "redirect": "Ghdies"},
      "nodes": []
    }
  ]
}
```


## [2026-09-05T20:52:03.248Z] TOOL CALL #4: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:52:03.289Z] TOOL RESULT

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


## [2026-09-05T20:52:24.820Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK ghait ===\"; grep -n -i \"ghait\\|ĝhait\\|ĝhai-t\" POK_full.txt | head -30\necho \"=== POK ghans ===\"; grep -n -i \"ĝhan-s\\|ghans\\|ĝhans\" POK_full.txt | head -30\necho \"=== POK gaesa ===\"; grep -n -i \"gaēsa\\|gaesa\\|gaesu\" POK_full.txt | head -20",
 "description": "Grep Pokorny for ghait and ghans"
}
```


### [2026-09-05T20:52:24.923Z] TOOL RESULT

```
=== POK ghait ===
32302:Root / lemma: ghait-a, -es- 
32304:Material: Von *ghait-[e]s-ixoxx\\ Avestan gaesa-xx\. " curly hair, curls ', 
32318:Middle Irish gaTseti. (from *ghait-s-) "stiff hair, bristle'. 
50157:sast/-^\Nord, instruction '; sanghaite. Old pers. z?a//y" speaks, announces' {*^a(n)hat})\ 
=== POK ghans ===
32348:Note: (compare ghans-' goose '). Sowohl Urverwandtschaft as newer creation are 
32378:Maybe alb. expressive goges/nj" burp, belch, yawn' {*gha-ghans) "*ononnatopoeic cry of 
37435:(see also under ghans- "goose '; similarly, but with Velar, gha ghaior gaggle, cackle, 
=== POK gaesa ===
32304:Material: Von *ghait-[e]s-ixoxx\\ Avestan gaesa-xx\. " curly hair, curls ', 
32310:npers. ges^ droopy hair, curls ', Avestan gaesu-^iuzzy haired, curly haired; (from camel:) 
35811:gall. -Latin gaesum, gall.-gr. yaTaov "heavy iron spear, lance' (gall. gaesatT
```


## [2026-09-05T20:52:26.311Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD ghait ===\"; grep -n -i \"ghait\" AHD_watkins1985.txt | head -20\necho \"=== AHD ghans ===\"; grep -n -i \"ghans\" AHD_watkins1985.txt | head -20\necho \"=== IEC ghans ===\"; grep -n -i \"ghans\\|khen\\|hamsa\" IEC.txt | head -30",
 "description": "Grep AHD and IEC"
}
```


### [2026-09-05T20:52:26.387Z] TOOL RESULT

```
=== AHD ghait ===
496:ghait-
508:ghait-. Curly or wavy hair. Possible root. Suffixed form
510:*ghait-d in Greek khaité, long hair: CHAETA; (CHAETOG- NATH). [Pok. ghait-d- 410.] ghalgh-. Branch, rod. Germanic *galgon- in: a. Old English g(e)alga, cross, gallows: GALLOWS; b. Old North French gauge, gauge: GAUGE. [Pok. ghalgh- 411.] ghans-. Goose. 1. Germanic *gans- (nominative plural *gansiz) in: a. Old English gds (nominative plural gés), goose: GOOSE!; (GOSHAWK); b. Old Norse gas, goose, diminutive geslingr, gosling: GOSLING. 2. Germanic *ganr- in Old English ganra, gandra, gander: GANDER. 3. Germanic *gandton- in Old English ganot, gannet: GANNET. 4, Suffixed form *ghans-er- in Latin dnser (< *hanser), goose: ANSERINE; MERGANSER. 5. Basic form *ghans- in Greek khén, goose: CHENOPOD. [Pok. ghans- 412.) ghasto-. Rod, staff. 1. Variant form *ghazdh- in Ger- manic *gazdaz in: a. Old English gierd, gerd, staff, twig, measuring rod: YARD}; b. Old Norse gaddr, rod, goad, spike: GAD?. 2. Form “ghast-d- in Latin hasta, spear: HASLET, HASTATE. [Pok. 1. ghasto- 412.] ghé-. To release, let go; (in the middle voice) to be released, go. Contracted from *ghea-. 1. Germanic vari- ant form *gaian in Old English gdn, to go: GO; AGO, FOREGO!, FoRGO. 2. Suffixed form *ghé-ro- in Latin hérés, heir (? < “orphan” < “bereft”):; HEIR, HEREDITA- MENT, HEREDITY, HERITAGE; INHERIT. 3. Suffixed o-grade form *ghé-ro-, “empty space,” possibly in: a. Greek khéros, place, country, particular spot: CHO- ROGRAPHY; b. Greek denominative khorein, to move, go, spread about, make room for: -CHORE; ANCHORITE. 4. Perhaps suffixed zero-grade form *gha-l- in Greek khalan, to slacken, let down (but this is more likely of unknown origin): CALANDO, CHALONE; ACHALASIA. 5. Suffixed zero-grade form *gho-t(w)d- in Germanic *gatwon-, a going, in Old Norse gata, path, street: GAIT. [Pok. ghé- 418.] ghebh-el-. Head. 1. Germanic *gablaz, top of a pitched roof, in Old Norse gafl, gable: GABLE. 2. Dissimilated form *khephel- in Greek kephalé, head: CEPHALIC, CEPH- ALO-, -CEPHALOUS; ENCEPHALO-, ENKEPHALIN, HYDRO- CEPHALUS. [Pok. ghebh-el- 423.] ghedh-. To unite, join, fit. 1. Lengthened o-grade form *ghédh- in Germanic *gédaz, “fitting, suitable,” in Old English géd, good: GooD. 2. Germanic *gaduri, “in a body,” in Old English tégezdere (t6, to; see de-), together: TOGETHER. 3. Germanic “gadurén, “to come or bring together,” in Old English gad(e)rian, to gather: GATHER. [Pok. ghedh- 423.] ghei-'. To propel, prick. 1. Suffixed and extended o-grade form *ghoidh-d in Germanic *gaidé, goad, spear, in Old English gdd, goad: GOAD. 2. Suffixed form *ghei-s- per- haps in nasalized zero-grade form *ghi-n-s- in Sanskrit himsati, he injures: AHIMSA. [Pok. 1. ghei- 424.] ghei-2. Theoretical base of *ghyem-, *ghiem-, winter. 1. Form *ghiem- in Latin hiems, winter: HIEMAL. 2. Suf- fixed variant form *gheim-ri-no- in Latin hibernus, pertaining to winter: HIBERNACULUM, HIBERNATE. 3. Suffixed zero-grade form *ghim-ar-ya, “female animal one year (winter) old,” in Greek khimaira, she-goat: CHIMERA. [Pok. 2. ghei- 425.] gheis-. Used of the emotion of fear or amazement (origi- nal part of speech uncertain). Suffixed o-grade form *ghois-do- in Germanic *gaistaz, a ghost, in: a. Old English gdst, ghost: GHOST; AGHAST; b. Old High Ger- man geist, ghost: POLTERGEIST; Cc. Germanic denomina- tive *gaistjan in Old English g&stan, to scare: GAST. [Pok. gheis- 427.] ghel-'. To call. 1. Germanic “gel-, *gal-, in: a. Old Eng- lish gellan, giellan, to sound, shout: YELL; b. Old English gielpan, to boast, exult: YELP; c. Old English galan, to sing: NIGHTINGALE. 2. Reduplicated form *ghi-ghl- in Greek kikhilé, thrush, later also the name for a kind of wrasse (a sea fish that has bright colors and jagged waving fins, reminiscent of the plumage of a bird):
1342:CENTROBARIC gWere-2 CENTUM dekm CENTURY dekm CEPHALIC ghebh-el- CEPHALO- ghebh-el- -CEPHALOUS ghebh-el- CERAMIC ker-4 CERASTES ker-! CERATODUS dent-, ker-1 CERATOID ker-! CEREAL ker-3 CEREBELLUM ker-1 CEREBRUM ker-1 CERES ker-3 CERTAIN krei- CERVINE ker-1 CERVIX ker-1 CESSION ked- CESSPOOL spirare cEsTus! kent- CEsTUS? kae-id- CHAETA ghait- CHAETOGNATH genu-2, ghait- CHAFE dhé-1, kele-1 CHAFER gep(h)- CHAFF! gep(h)- CHAIR sed-1 CHALAZA gheled- CHALAZION gheled- CHALCID ghelegh- CHALCOCITE ghelegh- CHALCOPYRITE ghelegh- CHALCOsIS ghelegh- CHALICE kal-1 CHALLENGE kel-8 CHALONE ghé- CHAMAEPHYTE dhghem- CHAMBER kamer- CHAMELEON dhghem- CHAMFER bhreg- CHAMFRON kaput CHAMOMILE dhghem-, mélon CHANCE kad- CHANCEL carcer CHANCELLOR carcer CHANCRE kar-1 CHANGE skamb- CHANT kan-
=== AHD ghans ===
510:*ghait-d in Greek khaité, long hair: CHAETA; (CHAETOG- NATH). [Pok. ghait-d- 410.] ghalgh-. Branch, rod. Germanic *galgon- in: a. Old English g(e)alga, cross, gallows: GALLOWS; b. Old North French gauge, gauge: GAUGE. [Pok. ghalgh- 411.] ghans-. Goose. 1. Germanic *gans- (nominative plural *gansiz) in: a. Old English gds (nominative plural gés), goose: GOOSE!; (GOSHAWK); b. Old Norse gas, goose, diminutive geslingr, gosling: GOSLING. 2. Germanic *ganr- in Old English ganra, gandra, gander: GANDER. 3. Germanic *gandton- in Old English ganot, gannet: GANNET. 4, Suffixed form *ghans-er- in Latin dnser (< *hanser), goose: ANSERINE; MERGANSER. 5. Basic form *ghans- in Greek khén, goose: CHENOPOD. [Pok. ghans- 412.) ghasto-. Rod, staff. 1. Variant form *ghazdh- in Ger- manic *gazdaz in: a. Old English gierd, gerd, staff, twig, measuring rod: YARD}; b. Old Norse gaddr, rod, goad, spike: GAD?. 2. Form “ghast-d- in Latin hasta, spear: HASLET, HASTATE. [Pok. 1. ghasto- 412.] ghé-. To release, let go; (in the middle voice) to be released, go. Contracted from *ghea-. 1. Germanic vari- ant form *gaian in Old English gdn, to go: GO; AGO, FOREGO!, FoRGO. 2. Suffixed form *ghé-ro- in Latin hérés, heir (? < “orphan” < “bereft”):; HEIR, HEREDITA- MENT, HEREDITY, HERITAGE; INHERIT. 3. Suffixed o-grade form *ghé-ro-, “empty space,” possibly in: a. Greek khéros, place, country, particular spot: CHO- ROGRAPHY; b. Greek denominative khorein, to move, go, spread about, make room for: -CHORE; ANCHORITE. 4. Perhaps suffixed zero-grade form *gha-l- in Greek khalan, to slacken, let down (but this is more likely of unknown origin): CALANDO, CHALONE; ACHALASIA. 5. Suffixed zero-grade form *gho-t(w)d- in Germanic *gatwon-, a going, in Old Norse gata, path, street: GAIT. [Pok. ghé- 418.] ghebh-el-. Head. 1. Germanic *gablaz, top of a pitched roof, in Old Norse gafl, gable: GABLE. 2. Dissimilated form *khephel- in Greek kephalé, head: CEPHALIC, CEPH- ALO-, -CEPHALOUS; ENCEPHALO-, ENKEPHALIN, HYDRO- CEPHALUS. [Pok. ghebh-el- 423.] ghedh-. To unite, join, fit. 1. Lengthened o-grade form *ghédh- in Germanic *gédaz, “fitting, suitable,” in Old English géd, good: GooD. 2. Germanic *gaduri, “in a body,” in Old English tégezdere (t6, to; see de-), together: TOGETHER. 3. Germanic “gadurén, “to come or bring together,” in Old English gad(e)rian, to gather: GATHER. [Pok. ghedh- 423.] ghei-'. To propel, prick. 1. Suffixed and extended o-grade form *ghoidh-d in Germanic *gaidé, goad, spear, in Old English gdd, goad: GOAD. 2. Suffixed form *ghei-s- per- haps in nasalized zero-grade form *ghi-n-s- in Sanskrit himsati, he injures: AHIMSA. [Pok. 1. ghei- 424.] ghei-2. Theoretical base of *ghyem-, *ghiem-, winter. 1. Form *ghiem- in Latin hiems, winter: HIEMAL. 2. Suf- fixed variant form *gheim-ri-no- in Latin hibernus, pertaining to winter: HIBERNACULUM, HIBERNATE. 3. Suffixed zero-grade form *ghim-ar-ya, “female animal one year (winter) old,” in Greek khimaira, she-goat: CHIMERA. [Pok. 2. ghei- 425.] gheis-. Used of the emotion of fear or amazement (origi- nal part of speech uncertain). Suffixed o-grade form *ghois-do- in Germanic *gaistaz, a ghost, in: a. Old English gdst, ghost: GHOST; AGHAST; b. Old High Ger- man geist, ghost: POLTERGEIST; Cc. Germanic denomina- tive *gaistjan in Old English g&stan, to scare: GAST. [Pok. gheis- 427.] ghel-'. To call. 1. Germanic “gel-, *gal-, in: a. Old Eng- lish gellan, giellan, to sound, shout: YELL; b. Old English gielpan, to boast, exult: YELP; c. Old English galan, to sing: NIGHTINGALE. 2. Reduplicated form *ghi-ghl- in Greek kikhilé, thrush, later also the name for a kind of wrasse (a sea fish that has bright colors and jagged waving fins, reminiscent of the plumage of a bird):
1246:ANILE an-! ANILINGUS 4no-, leigh- ANIMA ane ANIMADVERT ane- ANIMAL ane- ANIMATE ane ANIMATO ane- ANIMISM ane- ANIMOSITY ane- ANIMUS ane- ANION ei-1 ANISEIKONIA weik-3 ANKLE ank- ANKYLOSIS ank- ANLAGE an}, legh- ANNALS at- ANNEAL aidh- ANNEX ned- ANNIHILATE ne ANNIVERSARY at-, wer-3 ANNOTATE gno- ANNOUNCE neu-! ANNOY od-2 ANNUAL at ANNUITY at- ANNUL ne ANNULAR 4no- ANNULET 4no- ANNULUS 4no- ANODE sed-2 ANODYNE ed- ANOINT ong¥- ANOMALOUS sem-! ANOMIE nem- ANON ol-no- ANONYMOUS né-men- ANOPHELES obhel- ANORECTIC reg-1 ANOREXIA reg-1 ANORTHITE wrddh- ANOSMIA od-! ANSATE ans- ANSERINE ghans- ANSWER swer-1 ANT mai-1
1348:CHASM ghai- CHASSIS kap- CHASTE kes-2 CHAUDFROID kele-1 CHEAP caupd CHECK tké- CHECKMATE tké- CHEER ker-! CHEESE? kWo- CHEETAH kWeij-2, skai- CHEILOSIS ghel-una CHELICERA ker-1 CHELONIAN gheli- CHEMOTROPHY threph- CHENILLE kwon- CHENOPOD ghans- CHERISH ka- CHERNOZEM kers-1 CHERRY ker-6 CHERSONESE ghers-, sna- CHESS’ kap-
1553:GAMBOL kamp- GAMBREL kamp- GAMETE geme- GAMMON3 kamp- GAMO- geme- GAMOSEPALOUS geme- -GAMOUS gema- -GAMY geme- GANDER ghans- GANG! ghengh- GANGLING ghengh- GANGLION gel-1 GANGRENE gras- GANGUE ghengh- GANNET ghans- GANOID gau- GAP ghai-
1565:GOAD ghei-1 GOAT ghaido- GOD gheu(e)- GODSEND sent- GOFFER webh- GOLD ghel-2 GOLIARD gWel-3 GOMPHOSIS gembh- -GON genu-! GONAD gene- GONFALON gWhen-1 GONIOMETER genu-1 GONIOMETRY genu-! GONION genu-! GONO- gena- coop ghedh- GOOSE! ghans- GORE! ghaiso- GORE? ghaiso- GORGE gWere-4 GORGET gWera-4 GORSE ghers- GOSHAWK ghans- GOSLING ghans- GOSPEL spel-3 GOSSIP s(w)e- GOUACHE akWa- GOWAN ghel-2 GRAB! ghrebh-1 GRABEN ghrebh-2 GRACE gWera-3 GRACKLE gera-2 GRADE ghredh- GRAFFITO gerbh- GRAIN gre-no- GRAM! § gerbh- GRAM? gre-no- -GRAM gerbh- GRAMA gras- GRAMINEOUS_ gras- GRAMMAR gerbh- GRAMPUS_peisk- GRANADILLA gfe-no- GRANARY gre-no- GRANDILOQUENCE tolkw- GRANGE gre-no- GRANITE gr@-no- GRANT kerd-1 GRANULE gre-no- GRAPE ger-2 GRAPH gerbh- -GRAPH gerbh- -GRAPHER gerbh- GRAPHIC gerbh- GRAPHITE gerbh- -GRAPHY gerbh- GRAPNEL ger-2 GRAPPA ger-2 GRAPPLE ger-2 GRASP ghrebh-1 GRAss_ ghré- GRATE! grat- GRATE? kert- GRATEFUL gWere-3 GRATIFY gWere-3 GRATIS gWera-3 GRATITUDE gWero-3 GRATUITY gWera-3 GRAUPEL kreup- GRAVE! ghrebh-2 GRAVE? gwWera-2 GRAVES ghrebh-2 GRAVEL ghréu- GRAVID gWera-2 GRAVURE ghrebh-2 GRAY gher-3 GRAYWACKE wegh-
1849:MERGANSER ghans-, mezg-'
=== IEC ghans ===
691:ar2ntom “white metal, silver’. WP I, 82. Cf. arĝos Skt. rajatám; cf. also rajatah ‘silvery’; Av. ərəzatəm; Ober, aradata-; Oss. ärzät ‘metal, ore’; cf. Per. arzin ‘tin’; Arm. arcať, Iranian LW ‘silver’; cf. Arm. arcni ‘enamel’ beside arcnem (v. ‘polish’: Skt. rajin “shining'); Lat. argentum; Osc. aragetu-; Olr. argat, airget, Ir. airgead; Gaul. arganto-; OBrit. arga(nt); OW ariant, ereint; W arian; Cor. arghans; Br. argant. The phonology and source of Pol. ortec ‘amalgam’; Slovak ortuť, R and Cz. rtuť ‘mercury’ are obscure.
2576:dülos, à ‘spike, spire, stylus, tool’. Cf. dulos Gk. synth. cpds. in skhen-düle, ken-dülà; sphon-dülé (a root); tor-dülion; Pol. dyl “bole of tree? (ambig.)
4584:ghandh- ‘jangle, cackle, braying'. Cf. next, and ghanser Gk. cf. kánthon, Hes. kándon < Thrac.? *don- key’; Du. (variant) gent ‘gander’; LG gant, id. (fr. *shand-). Ambiguous are OCS godo, gosti ‘play on an instrument; Cz. hudu, housti, id. beside hudé ‘gosling; young girl’; Li. gandinti ‘scare’. For Li. gafidas ‘rumour, report', see ghondh- (2). (For Cz. hudé in sense of ‘girl’, cf. ON genta, id.) (OE ganot ‘gannet’ presupposes a variant of type *ghanod-)
4595:pl. ‘gobbling of a turkey’; Lith. gañdras ‘stork; Latv. gandrs, id. Cf. ghandh- and ghanser ghangh- ‘roar, how? Arm. gangad, a-st. ‘lament’; gangiwn ‘echo, rumble’, cf. also ganfiwn (*scream', fr. *ghan- ghtion); Gk. kagkházo ‘guffaw’; Icel. gagga ‘yelp’: Blg. cf. gágra ‘chatter’. (For OCS gognati ‘murmur’, see gang- (gong-). See next ghanghlaio ‘yell, bawl’. Cf. ghangh- Gk. kagkhaláo ‘guffaw’; Cz. huhlat ‘how? ghanser ‘gander. WP I, 536. Cf. ghandh-, etc. and next Lat. *hanser; anser, id.; MHG ganser; Cz. houser; Pol. gasior, id. ghansis (variant: £hansis) ‘goose’. WP I, 536 Skt. hamsih ‘kind of goose’; hamsáb ‘gander of some king’; Hindi hans 'goose'; Per. yàz, id.; Gk. khén, m.f. ‘goose; gander’; Olr. géiss, Ir. géis, gein ‘swan’; OHG gans, gp. ganso ‘goose’; LG gaus, pl. gáus; OE gos, pl. gës; Fris. goes, pl. gies; Du. gans; ON gás, pl. gæss, id. beside gassi ‘gander’; OCS gosi, pl. gosi; Li. (variant) žąsis; Latv. zoss, gs. zoss, gp. zosu, id.; Finn. LW hanhi, id. gharbhos, à ‘tuft, bundle, sheaf. Gk. kárphos, kárphē “hay, straw; bird?s nest’; OHG garba ‘sheaf’; Du. garf, garve, id.; LW in LLat. garba, Fr. gerbe; Li. cf. garbana *lock, curl’ ghargh- ‘shout, croak’. See next and cf. garg-, gorg-, gargh-. (Skt. ambig.) Skt. garhami, garhe ‘complain’; Arm. garga- tem ‘rave, twaddle’; Icel. garga, a-st. ‘croak, screech’; Li. (ambig.) gargu, eti and gargiu, - tí *cackle, gargle, snore', etc. See garg-, gorg- ghargholos 'gurgling; gurgle; hoarse speaker, gurgle’ etc. Cf. gargar- Skt. ghargharah, adj. ‘gurgling’, etc.); Gk. cf. karkhaléos ‘raucous’; MHG gargeln, v. ‘gargle, gurgle’; Li. (ambig.) gargalas ‘hoarse person’. See next gharghoros (ghorghoros) (1) 'gargling, gurgl- ing’, etc. Cf. ghargholos Skt. cf. ghargharah (ambig. cf. gharghol-); Gk. kárkharos (1) ‘raucous’ beside e-gde kérkho, v. "be hoarse’ (cf. ghergho); Li. cf. ambig. gařgas ‘gurgle; hoarseness’. Cf. garg-, ghergh- gharghoros (ghoerghoros) (2) (rough, sharp,
5936:$hansis ‘goose’. Onomat. cf. ghansis and ghiia- w. extns. WP I, 536 The variant is present in Li. žąsis, gp Zasü: Latv. zoss, gp zosu, id. Cf. MW gan- in gan- hewin *crispula', gan-wreidd loyt *mugwort'. LW in Finn. hanhi
9385:(Khenus (?). A formula to reconcile Skt. hánuh with the rest of the evidence under Genus. Cf. also e20, me£is, dhugtër and Krd-)
```


## [2026-09-05T20:52:34.069Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '32295,32330p' POK_full.txt\necho \"=== ghans lemma ===\"\ngrep -n \"Root / lemma: ghans\\|Root / lemma: ĝhans\\|lemma: ghan\" POK_full.txt | head",
 "description": "Print Pokorny ghait entry"
}
```


### [2026-09-05T20:52:34.136Z] TOOL RESULT

```
presumably to Lithuanian gaistu, -au, gaTsti^'^\}x\, border, hesitate, dwindle ', gaisinti 
"while, spend time, destroy'. 

References: WP. I 528, WH. I 632. 
Page(s):410 

Root / lemma: ghait-a, -es- 
Meaning: curly or wavy hair 
Material: Von *ghait-[e]s-ixoxx\\ Avestan gaesa-xx\. " curly hair, curls ', 

Note: 

Reduplicated laryngeal in -h2"ahre- > Avestan -ae- 

npers. ges^ droopy hair, curls ', Avestan gaesu-^iuzzy haired, curly haired; (from camel:) 

rat's hairy tail '; 

gr. xaiTn ' loose, flowing hair, used esp. of back hair, of a horse's mane, of a lion's 
mane, of a hedgehog's spines, crest of a helmet, of trees, foliage, of human hair '; in 
addition probably the maked. PN raiT£a(;; 

Middle Irish gaTseti. (from *ghait-s-) "stiff hair, bristle'. 

References: WP. I 529. 
Page(s):410 



Root / lemma: ghauo- 

Meaning: false 

Material: Latin /7ai/o' Concept of negation 'not', maybe from *hauidom > *haudom (> haud 

=== ghans lemma ===
32390:Root / lemma: ghan-s- : goose'. 
35882:Root / lemma: ghan-s- 
35888:Root/ lemma: ghan-s-: goose' derived from Root/ lemma: ghagha, gheghe, ghighi: "to 
35955:Root / lemma: ghan-
```


## [2026-09-05T20:52:35.471Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Page(s): 41[012]\" POK_full.txt | head -20\necho \"---- search ghans page 412\"\ngrep -n \"goose\" POK_full.txt | sed -n '1,40p'",
 "description": "Find Pokorny pages 410-412"
}
```


### [2026-09-05T20:52:35.540Z] TOOL RESULT

```
36009:Page(s): 412-413 
---- search ghans page 412
3996:goosefoot ', Liden Stud. 97); Dutch alft, e/^ 'whitefish' (formally = Old High German etc 
7831:Latin avisi. "bird' (therefrom auca 'b'\rd, esp. goose '; 
22112:"thorn', dyge^ gooseberry ', Old Prussian digno^ the hilt of a sword ' (as Modern High 
22432:the chicken, the goose ', Old Church Slavic blago-detb " Grace, blessing, gratitude '; tl^a- 
29847:goose), etc. Latin gannio " to bark, snarl, growl ' (under the influence of common Celtic -ns- 
30853:spreads out the wings) ', gusta " lair, camp, nest of a chicken, a goose '; Old Prussian 
32348:Note: (compare ghans-' goose '). Sowohl Urverwandtschaft as newer creation are 
32352:Material: Old Irish gigren, giugrann ' goose ', cymr. gwyrain' Red Grouse, wild chicken ' 
32356:gwaz' goose ' (*^/igo''5 because of Middle Irish Gen. geoid), to d/-forms compare Old 
32358:English ganotuuder *gfians-' goose '; 
32362:Middle High German gagen, gagern {a\so gTgen) " shout, cackle like a goose ' (Modern 
32363:High German Gagag, GTgag for "goose '), Old High German gacl<izdn, gacl<azzen' 
32375:^e^e "cuckoo'); Latvian gagaV shout like goose ', gaga " kind of duck ', gagars "goose ' 
32380:goose', ^a^ap "stutterer', guguge'dove kind ' (Slavic origin) also alb. gaga'cry of goose' : 
32390:Root / lemma: ghan-s- : goose'. 
32401:Old Icelandic gagr greylag goose '; 
35884:Meaning: goose 
35888:Root/ lemma: ghan-s-: goose' derived from Root/ lemma: ghagha, gheghe, ghighi: "to 
35892:Material: Old Indie hatfisa-h m., hatfisTi. "goose, swan'; soghd. zy"sorte d'oiseau'; 
35894:Latin anser, mostly m. "goose ' (originally *hanser, to stem formation compare Slavic 
35901:gr. xnv, -oc„ m. f., Doric Boeotian xciv "goose ' from *xav(;, xavaoq (here, as in Germanic 
35913:gr. xnvsc;). O'd Icelandic gas{P\.g3es) "goose ' (from Old English ^ds derives Middle Irish 
35916:Lithuanian zqsisi. "goose ' (Akk. zqsi= gr. XHva, Gen. PI. conservative zqsQ, dial, also 
35920:sloven, gos, poln. ^^s'goose '; 
35932:(zuerst by Plin.) ganta "a kind of goose ' (out of it prov. gante "wild goose, stork '; the 
35936:meaning as Tirol ganzen^ flirt ', gansern' act as a goose', also " wish, adore cravingly ', 
35972:mouth, lust, crave, glotzen', g0n/r' mocker '. Also the name of the goose, Indo Germanic 
37435:(see also under ghans- "goose '; similarly, but with Velar, gha ghaior gaggle, cackle, 
44398:Old Indie 5i//ra-m. "parrot'; Armenian sa^ "goose ' {*kaua) = Old Church Slavic sova 
44488:with orange flowers ' and kadamba- m. ' a kind of goose with dark grey wings '; 
48679:toad, dwarf'; of the ruptured skin (becoming rough) (" goose bumps ') also Lithuanian 
48913:'goose; wolf see below kan). 
59947:Dutch broek, with it is as " cold as a result of moisture ' or as ' goose bumps ' (compare 
68904:maybe alb. pa/a "goose' Slavic loanword from russ. -Church Slavic yOb/a "bird' : Serbo- 
70824:roughness the Haut), compare also Latvian raupa^ goose bumps ' ("shudder, shiver ');
```


## [2026-09-05T20:52:43.065Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '35880,35950p' POK_full.txt",
 "description": "Print Pokorny ghans entry"
}
```


### [2026-09-05T20:52:43.123Z] TOOL RESULT

```
Page(s):411 

Root / lemma: ghan-s- 

Meaning: goose 

Note: 

Root/ lemma: ghan-s-: goose' derived from Root/ lemma: ghagha, gheghe, ghighi: "to 

cackle (of geese)'. 

Material: Old Indie hatfisa-h m., hatfisTi. "goose, swan'; soghd. zy"sorte d'oiseau'; 

Latin anser, mostly m. "goose ' (originally *hanser, to stem formation compare Slavic 
*zansera- {*gansera-) 'gander' in Old Czech huser, polab. gunsgarr, etc.); 

Note: 

Common Old Indie : Latin gh-> h-. 

gr. xnv, -oc„ m. f., Doric Boeotian xciv "goose ' from *xav(;, xavaoq (here, as in Germanic 
and in Lithuanian Gen. PI. z^sQ, still the old conservative inflection); 

Maybe zero grade in alb. {*he-nos) /'osa"duck ' common alb. n/r rhotacism; also gn- > n- 
italic-illyrian. 

Old Irish ge/ss's\Nar\' {*gansT= Old Indie hamsT, not reshaped from a conservative 
stem); 



Old High German gans {f-stem has changed), Old English gds{P\. gesirom *gans-iz = 
gr. xnvsc;). O'd Icelandic gas{P\.g3es) "goose ' (from Old English ^ds derives Middle Irish 
goss); 

Lithuanian zqsisi. "goose ' (Akk. zqsi= gr. XHva, Gen. PI. conservative zqsQ, dial, also 
Nom. PI. z$ses), Latvian zuoss. Old Prussian sansy6s.\ 

Slavic *ggsb (with probably auf Germanic influence based ^instead of ^ in russ. gust, 
sloven, gos, poln. ^^s'goose '; 

Specht Dekl. 204 will also Lithuanian gen-s-e, gen-z-ei. " egret, heron ' here place. 

Old English gan(d)ra^ gander ' (engl. gander). Middle Low German ganreds. is applied 
as Mask.-formation of stem *gan- after kind of from Old High German kat-aro' tomcat, 
male-cat'; if ein *ganezan- the basic lies, stand Swiss gann, ganner' appellation from 
aquanauts ' as *ganza-\N\t\r\ it in Suffix ablaut, (under the influence of common Celtic -ns-, - 
nt- > -nn-). 

Besides certainly of the abbreviated stem ^/7a/7- (wherefore ghan-{e]s- as Indo 
Germanic *men-dt-: * men-{e]s- " month ') on the exterior formation with -d-: Germanic 
(zuerst by Plin.) ganta "a kind of goose ' (out of it prov. gante "wild goose, stork '; the 
meaning " stork ' shows also Lithuanian gandras. Old Prussian gandarus, from Germanic 
*gan[d]ro). Old English ganot'a wild water bird, e.g. a coot ', Old High German ganazzo' 
gander ', also ganzo. Middle Low German gante diS. (A derivative therefrom with similar 
meaning as Tirol ganzen^ flirt ', gansern' act as a goose', also " wish, adore cravingly ', 
siebenbiJrg. goaseln^ philander, flirt ' is nisi, ganta^ philander, flirt ', ganti^ an idler, loafer, 
man about town, a city buffoon, droll, jester, clown, pantaloon, parasite ', Swedish mdart. 
gant, Danish gante^ dandy, fop, man excessively concerned with his clothes and 
appearance ', wherefore as fem. Norwegian gjente ' g\r\' .) 

Maybe alb. goce'g\r\' 

There Indo Germanic ghan-s-, -(9)d-mt\\ gr. xavsTv (see ghan-) and generally with the 
family 2. ghe- " yawn ' zusammenhangt, also from dem heisern Anfauchen of animals by 
open bill, beak, neb den Namen hat, is um so glaublicher, as also ghe- " yawn ' originally 
identical Ausatmen beim Gahnen identified hat. A similar Lautnachahmung (partly also 
base from Wasservogelnamen) see below gha gha-. 

References: WP. I 536, WH. I 52, 583, Trautmann 365 f., Specht Dekl. 47, 204.
```


## [2026-09-05T20:53:09.353Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD gēs ===\"; grep -n -i \"^g[eē]s\\|gēs \\|gesūg\\|gēsūg\\|gēsu\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== HRN ges ===\"; grep -n -i \"gīs\\|gēs\\|gesu\\|Locke\" HRN.txt | head -30",
 "description": "Grep Pahlavi dict and Horn for ges"
}
```


### [2026-09-05T20:53:09.416Z] TOOL RESULT

```
=== PHD gēs ===
PHD_mackenzie.txt:2510:ges [gys I (M gyswg, N gesu)] curls, locks.
=== HRN ges ===
2167:vävra 'Schneeflocke*, Plur. 'Schnee'; bei. LW. harpi
2769:Gesundheit' (237 Zeile 4); auch 'sich halten', z. B.
4722:l^dhar- 'halten', vergl. aw. drva- gesund; phlv. därük
4953:551. darust 'gesund, richtig, duriistl; vergl. tendumstX
4954:aw. ^drva- + asti- gesunden Leibes* , oder wohl
4956:tholomae vorschlägt; ap. diiruva- 'gesund'; phlv.
4991:i^dhar- 'halten', vergl. aw. drva- gesund'; phlv.
7925:da weder ein Gesunder noch ein Kranker es ent-— 204 —
8233:950. ges, gesü 'Locken, öelock'.
8234:aw. ga^sa- 'in zwei oder drei (sc. Locken) geord-
10698:124. ha» 'Glocke, nur vd. U (48).
10699:aw. kqstra^ 'Glocke*.
```


## [2026-09-05T20:53:21.945Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN 950 ===\"; sed -n '8228,8250p' HRN.txt\necho \"=== HUB ges ===\"; grep -n -i \"gaesa\\|ges, ges\\|Locken\" HUB.txt | head -20\necho \"=== BRT gaesa ===\"; grep -n -i \"gaēsa\\|gaesa\\|gaesu\\|gaesav\" BRT.txt | head -20",
 "description": "Horn/Hübschmann/Bartholomae for ges"
}
```


### [2026-09-05T20:53:22.029Z] TOOL RESULT

```
=== HRN 950 ===
14*— 212 —
949. (feU ^Welt\
aw. ga^^ya- 'irdisch'; phlv. getlk^).
Mot savant; die den Lautgesetzen entsprechende
neupersische Form ist gehän (No. 951).
950. ges, gesü 'Locken, öelock'.
aw. ga^sa- 'in zwei oder drei (sc. Locken) geord-
netes Haar (ZBÖL); phlv. g^s^ arm. syr. LW. ges,
ü^: *Haar\
oss. d. yesä, t. qts *Borste*.
951. gehän *Welt\ arab. LW. ßhan, jehän^),
aw. gae^ä' (gaf.&anqm); phlv. gehän, vergl. tahn.
r:} (de La gar de, Semitica I, 59).
L.
952. lfrJ)e, läwe 'Schmeichelei, Bitte', lähidefi,, laf 'Prahlerei*.
skr. l^lap' (ai. rap-), Idpati 'schwatzen', vergl.
ud + lap' 'liebkosen .
siyn. I6w-am, sar. lew-am 'reden, sprechen, sagc^n';
af/. laudal 'sagen, erzählen'.
953. leh 'Lippe*, vergl. lefj^ leföe.
Käs. lew; kauk.-bergjüd. low,
phlv. lap; lat. labium; nhd. lAppe (vgl. Kluge,
Etymolog. Wörterbuch s. v.).
=== HUB ges ===
2371:Glockenspeise', sepid rui *Zinn , Polak, Persien II, 177,
4304:zd. vditigaesa-j etc.
5063:') Ueber gurs *Lockenhaar* (fiir gars) s. oben p. 92.- 145 —
6850:VatgBSf arm. VatgSs (Elise 139) = zd. vaitigaesa-,
7543:ges^ gSsU Locken* = zd. ga^sa-; nivSsam 'ich schreibe' =
8814:gohar 'Ursprung H. 948, oben p. 96; ges^ gesU 'Locken\
=== BRT gaesa ===
9758:verwechselt.  KompK.  —  Vgl.  gaesav-.  —  np.  g^l  'Locken';
23470:•  j.  väiti-gaesa-  in.  Name  eines  Gebirgs*>: ; akmal  hala  garayS  fraexsyan  . .  dvadasS  j 'SS  Yt  ig.  2.
```


## [2026-09-05T20:53:23.476Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN chaeta ===\"; grep -n -i \"chaeta\" KLN_1966.txt KLN_1971.txt | head -20\necho \"=== KLN goose/anser ===\"; grep -n -i \"gander\\b\" KLN_1966.txt | head -10",
 "description": "Klein chaeta"
}
```


### [2026-09-05T20:53:23.544Z] TOOL RESULT

```
=== KLN chaeta ===
KLN_1971.txt:43416:spirochete, Coleochaete, Oligochaeta. 
KLN_1971.txt:166577:Oligochaeta, n., pi., an order of chaetopod worms 
KLN_1971.txt:186530:Polychaeta, n. pi., a class of annelids, comprising 
KLN_1971.txt:229159:Spirochaeta, n., a genus of bacteria characterized 
KLN_1971.txt:229164:constituting the genus Spirochaeta. — See prec. 
KLN_1966.txt:6773:Derivatives:  catarrh-al,  adj.,  catarrh-al-ly,  adv. Catarrhina,  n.  pi.,  a  division  of  the  order  Pri¬ mates,  including  the  gorilla,  orangutan  and chimpanzee  ( zoo! .)  —  ModL.,  lit.  ‘with  nos¬ trils  downward’,  fr.  cata-  and  Gk.  pfp,  gen. pivop,  ‘nose’.  See  rhino-, catarrhine,  adj.  and  n.  —  See  prec.  word. Catasetum,  n.,  a  genus  of  orchids  (bot.)  —  A ModL.,  hybrid  coined  fr.  cata-  and  L.  sactum, ‘bristle’;  see  seta.  The  correct  form  would  be Catachaetam  (fr.  cata-  and  Gk.  yxt xv;,  Tong flowing  hair’),  in  which  both  elements  are  of Greek  origin  (see  chaeto-). catastasis,  n.,  the  part  of  a  drama,  in  which  the action  is  at  its  height.  —  Gk.  xxxxaxam;,  ‘settle¬ ment,  appointment,  state,  condition’,  fr.  xaSH- nxxvxt,  ‘to  set  down,  set  in  order’,  fr.  xxxx (see  cata-)  and  laxxvxi,  ‘to  place’.  See  state, catastrophe,  n.  —  L.  catastropha,  fr.  Gk.  xxxx- axp&97j,  ‘overturning,  overthrowing’,  fr.  xxxx- axpttpsiv.  ‘to  upset,  overturn,  overthrow’,  lit. ‘to  turn  down',  fr.  xxxx  (see  cata-)  and  axps-pstv, ‘to  turn’.  See  strophe.
KLN_1966.txt:7105:Chaenomeles,  n.,  a  genus  of  plants  of  the  apple family  (but.)  —  ModL.,  compounded  of  Gk. yztvstv,  'to  gape,  yawn-,  and  ;o.r,Xov,  ‘apple’. See  Chaenactis  and  Malus. chaeto-,  before  a  vowel  chaet-,  combining  form meaning  ‘spine’  or  ‘bristle’.  —  Fr.  Gk.  y-jx~r„ ‘long  flowing  hair,  mane’,  which  is  cogn.  with Avcstic  gaesa-,  ‘curly  hair',  Ir.  gaoisideach, ‘hair'.  Cp.  achaetous  and  the  second  element  in spirochete,  Coleochaete,  Oligochaeta. Chaetodon,  n.,  a  genus  of  fishes  having  spiny  fins (ichthyol.)  —  ModL.,  compounded  of  chaet- and  Gk.  oScov,  gen.  oSovto;,  ‘tooth’.  See  odonto-. chaetopod,  adj.,  pertaining  to  the  Chaetopoda;
KLN_1966.txt:26206:01igochaeta,n.,pl.,  an  order  of  chaetopod  worms (zoo/.)  —  ModL.,  compounded  of  oligo-  and  Gk. XaiTT),  ‘long  flowing  hair,  mane’.  See  chacto-. oligochaetous,  adj.  —  See  prec.  word  and  -ous. oligoclase,  n.,  a  kind  of  feldspar  {mineral.)  — Compounded  of  oligo-  and  Gk.  xXaau;,  ‘frac¬ ture’,  fr.  y.Xav,  ‘to  break’.  See  clastic  and  cp. words  there  referred  to.
KLN_1966.txt:29434:Polychaeta,  n.  pi.,  a  class  of  annelids,  comprising most  marine  worms  ( zool .)  —  ModL.,  com¬ pounded  of  poly-  and  Gk.  y_a.Lvr„  ‘hair’.  See
KLN_1966.txt:36310:Spirochaeta,  n.,  a  genus  of  bacteria  characterized by  a  spiral  form  ( bacteriol .)  —  ModL.,  coined fr.  spiro-,  ‘spiral’,  and  Gk.  yfii.tr,,  ‘long  flowing hair,  mane’.  See  chaeto-. spirochete,  also  spirochaete,  n.,  any  of  the  bacteria constituting  the  genus  Spirochaeta.  —  See  prec. word.
=== KLN goose/anser ===
4784:Bereshith,  n.,  1)  the  creation ;  2)  the  first  book  of the  Pentateuch  (=  Gk.  Genesis,  lit.  ‘origin’).  — Heb.  Bfreshtth,  shortened  fr.  SCpher  ma'dsih bereshlth,  ‘the  Book  of  the  creation’.  Since bfreshtlh  happens  to  be  the  first  word  of  the Pentateuch,  it  was  erroneously  assumed  that the  first  book  of  the  Pentateuch  was  called Bereshith  from  the  first  word  of  its  Hebrew text.  This  erroneous  belief  gave  rise  to  the custom  of  naming  Hebrew  books  (also  the  other four  books  of  the  Pentateuch)  from  initial words  of  the  text.  —  Heb.  blreshith  lit.  means ‘in  the  beginning’.  It  is  formed  fr.  pref.  b1-,  ‘in’, and  reshith,  (for  *rl'eshtth),  ‘beginning’,  a derivative  of  rosh,  ‘head’,  which  is  rel.  to  Aram. resh,  Akkad,  reshu,  Arab,  ra's,  Ethiop.  res, ‘head’.  Cp.  race,  ‘tribe’,  rais,  reis,  resh,  Rosh Hodesh,  Rosh  Hashanah. beret,  n.,  a  fiat  round  cap.  —  F.  beret,  occasion¬ ally  written  also  berret,  fr.  berret,  a  word  of  the dialect  of  Beam,  fr.  Old  Gascon  berret,  ‘cap’, fr.  Late  L.  birrus,  also  birrum,  ‘large  cloak  with a  hood’.  See  biretta  and  cp.  barret,  burnous, bergamot,  n.,  the  tree  Citrus  bergamia.  —  Fr. Bergamo,  a  city  in  Lombardy,  Italy, bergamot,  n.,  kind  of  pear.  —  F.  bergamot,  fr.  It. bergamotta,  fr.  Turk,  beg  armudi,  lit.  ‘pear  of a  bey’,  influenced  in  form  by  the  Italian  place- name  Bergamo.  See  bey. bergander,  n.,  sheldrake  (obsol.)  —  Prob.  a  blend of  Du.  bergeend,  ‘sheldrake’,  lit.  ‘mountain duck’  (see  barrow,  ‘mountain’,  and  Anas),  and
4785:E.  gander.  Cp.  goosander.
5649:Derivatives:  brigand-age,  n.  (fr.  F.  brigandage), brigander,  n..  brigandine  (q.v.),  brigand-ish,  adj., hrigand-ish-ly,  adv.,  brigand-ism ,  n. brigandine,  n.,  body  armor.  —  F.,  fr.  It.  brigan- lina,  fr.  brigare,  ‘to  fight’.  See  prec.  word, brigantine,  n.,  a  two-masted  square-rigged  ship. —  F.  brigantin,  fr.  It.  briganlino,  ‘piratical  (lit. ‘fighting’)  vessel",  fr.  brigante  ‘brigand’.  See brigand.
15766:gamy,  also  gamey,  adj.,  having  the  flavor  of game.  —  Formed  fr.  game,  n.,  with  adj.  suff.  -y. -gamy,  combining  form  meaning  ‘marriage, union’,  as  in  heterogamy,  polygamy.  —  Gk. -yapia,  fr.  yajj-o;,  ‘marriage’.  See  gamo-. gander,  n.  —  ME.  gandre ,  fr.  OE.  ganra,  gandra, rel.  to  Du.  gander,  MLG.  ganre,  Bavarian gander,  ‘gander’.  See  goose  and  cp.  gannet. ganef,  n.  —  See  gonnof.
15780:gannet,  n.,  the  solan  goose.  —  OE.  ganot,  ‘sea bird,  gannet’,  rel.  to  Du.  gent,  OHG.  gannasso, ganzo,  ‘gander’.  See  gander,  goose, ganoid, adj.,  1)  smooth  (said  offish  scales);  2)per- taining  to  the  Ganoidei.  • —  F.  ganolde,  com¬ pounded  of  Gk.  Y“V0S>  ‘brightness,  brilliance, splendor’,  and  -oeiS r)c;,  ‘like’,  fr.  eZSo?,  ‘form, shape’.  The  first  element  stands  for  ya-vo?  and is  rel.  to  yavo(xai  (for  ya-vo-fxat),  ‘I  am  glad,
16447:googul,  n.  —  A  var.  of  gugal. goon,  n„  a  ruffian.  —  Fr.  Alice  the  Goon,  a  sub¬ human  character  in  the  comic  strip  Thimble Theatre  by  the  American  cartoonist  Elzie  Crisler Segar  (1894-1938). gooroo,  n.  —  A  var.  of  guru, goorul,  n.  —  A  var.  of  goral. goosander,  n.,  the  merganser.  —  Prob.  formed  fr. goose  on  analogy  of  bergander  (q.v.) goose,  n.  —  ME.  gos,  goos,  fr.  OE.  gos,  rel.  to OFris.,  MLG.  gos,  ON.  gas,  OHG.,  MHG.,  G. gans,  ‘goose’,  and  cogn.  with  OI.  hamsah  (masc.), hams i  (fern.),  ‘goose,  swan’.  Dor.,  Boeot.  Gk. yt&v,  Gk.  xh'tt  L.  anser  (for  *hanser),  Lith.  zqsls, OPruss.  sansy,  ‘goose’,  OIr.  geiss,  ‘swan’. OSlav.  gusi,  ‘goose’,  and  Sp.  ganso,  ‘gander, goose’,  are  Teut.  loan  words.  Cp.  gander,  gan- net,  gosling  and  the  first  element  in  goosander, goshawk,  gossamer.  Cp.  also  anserine,  Chen. Derivatives :  goos-ish,  goos-y,  adjs. gooseberry,  n.  —  Prob.  fr,  G.  Krausbeere  or Krduselberre,  which  are  rel.  to  MDu.  croesel, ‘gooseberry’.  These  words  prop,  mean  ‘curly berry’,  and  derive  fr.  G.  kraus,  resp.  MDu. croes,  ‘crispy,  curly;  cp.  ME.  crous,  ‘curly’.  E. gooseberry  owes  its  form  to  an  association  with goose  (as  if  it  were  a  compound  of  goose  and berry).  Cp.  F.  groseille.  It.  grossularia  and  Sp. grosella,  ‘gooseberry’,  which  are  Dutch  loan words.  Cp.  also  Grossularia. gopher,  n.,  a  burrowing  rodent.  —  F.  gaufre, ‘waffle,  honeycomb’  (see  goffer);  so  called  in allusion  to  its  burrows.
27693:pato,  n.,  the  Muscovy  duck  —  Sp.  and  Port., ‘duck,  drake,  gander’,  fr.  Arab,  baud',  ‘duck’, patois,  n.,  a  provincial  dialect  —  F.,  prob.  formed fr.  patte,  ‘paw,  foot',  with  suff.  -ois  (fr.  L.  -ensis) [the  same  suff.  appears  in  adjectives  like  North¬ ern  F .  franfois  (F.  franfais),  ‘French’,  etc.];  so called  with  reference  to  the  clumsy  manner  of those  speaking  it.  Cp.  F.  pataud,  ‘clumsy, loutish’,  which  is  also  a  derivative  of  patte,  ‘paw, foot’.  See  patten  and  cp.  words  there  referred  to. patola,  n.,  a  silk  cloth  (India)  —  OI.  patoldh, prob.  fr.  Malayalam  pattuda,  ‘a  silk  cloth’, patri-,  combining  form  meaning  ‘father’.  —  L. patri-,  from  the  stem  of  pater,  gen.  patris,  ‘fa¬ ther’.  See  father  and  cp.  pater, patrial,  adj.,  pertaining  to  one’s  fatherland.  — Formed  with  adj.  suff.  -al  fr.  L.  patria,  ‘father- land’,  fr.  pater,  gen.  patris.  See  patri-. patriarch,  n.,  a  father  who  rules  his  family  or tribe.  —  ME.  patriarch,  fr.  OF.  patriarche,  fr. Late  L.  patriarcha,  fr.  Gk.  Traxptapx-rjt;,  ‘father of  a  race’,  fr.  Trxxptoc,  ‘family,  lineage’,  and -apx7j?,  ‘leader’.  The  first  element  derives  fr. mxxrjp,  gen.  7rxxp6i;,  ‘father’;  see  father.  For  the second  element  see  -arch.  Cp.  matriarch. Derivatives: patriarch,  intr.  v., patriarch-ism,  n., patriot ch-ist,  n.
36529:stag,  n.  —  ME.,  fr.  OE.  stagga,  ‘stag’,  orig.  ‘a male  animal’,  rel.  to  ON.  steggi,  ‘a  male  bird,  a male  cat’,  dial.  E.  stag,  ‘gander’.  These  words derive  fr.  *stegh-,  a  denasalized  form  of  I.-E. base  *stengh-,  ‘to  sting’.  The  original  meaning of  stag  prob.  was  ‘provided  with  a  male  organ’. See  sting,  v.
```


## [2026-09-05T20:53:37.556Z] TOOL CALL #13: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-05T20:53:37.564Z] TOOL RESULT

```


```


## [2026-09-05T20:53:39.777Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON غاز ===\"; grep -n \"غاز\" MON_part1.txt MON_part2.txt | head -20\necho \"=== MON2vol غاز ===\"; grep -n \"غاز\" incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt | head -20",
 "description": "Grep Moin for ghaz"
}
```


### [2026-09-05T20:53:39.868Z] TOOL RESULT

```
=== MON غاز ===
MON_part2.txt:215:غاز فرهنگ فارسي معیر ۱۰۵ 
MON_part2.txt:221:غاز: 22 (.) نبازه حاجت؛ مق. ناز. 
MON_part2.txt:223:غاز: 22, [- غاژ] (.) خار (گل با درخت)؛ 
MON_part2.txt:224:غاز؛ 2, [تر. - قاز] (.) (جاد.) پرنده‌ای 
MON_part2.txt:235:می‌چرد. غازهای وحشی بصورت دسته‌های 
MON_part2.txt:239:غاز انواع و نژادهای مختلف دارد و برخی از 
MON_part2.txt:242:غاز عبار تند از: غاز پومر و غاز تولوز و غاز 
MON_part2.txt:243:کلموگوری. تخم‌گذاری غاز ماده در اواخر 
MON_part2.txt:246:آوردن جوجه زیر غاز ۰ تاه ۱ تحم 
MON_part2.txt:249:بوقلمون ۱۰ تا ۲۰ تخم غاز می‌گذارند)؛ 
MON_part2.txt:252:غاز: 22 [- قاز] (.) کوچکترین واحد پول 
MON_part2.txt:253:در عهد قاجاربه. هر «جندکك» معادل ۲ غاز 
MON_part2.txt:254:بود. پنج غاز (ینغاز) معادل نیم شاهی و ده 
MON_part2.txt:255:غاز معادل یک شاهی بود. 
MON_part2.txt:258:غازییکی: ۰:۷ (امر.) واحدی برای 
MON_part2.txt:260:می‌گفتند و از مس سکه زده می‌شد و ده غاز 
MON_part2.txt:263:غازبین: «-7 [- غازبیننده] (ص‌فا.) آنکه 
MON_part2.txt:264:یک غاز را در نظر گیرد و حساب کند. 
MON_part2.txt:266:غازچران: 7 [- غازچراننده] 
MON_part2.txt:270:غازغاز: 72ب.«(ص.) از هم شکافته و باز 
=== MON2vol غاز ===
incoming/MON/MON_2vol_Adena_v2_djvu.txt:215:غاز فرهنگ فارسي معیر ۱۰۵ 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:221:غاز: 22 (.) نبازه حاجت؛ مق. ناز. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:223:غاز: 22, [- غاژ] (.) خار (گل با درخت)؛ 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:224:غاز؛ 2, [تر. - قاز] (.) (جاد.) پرنده‌ای 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:235:می‌چرد. غازهای وحشی بصورت دسته‌های 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:239:غاز انواع و نژادهای مختلف دارد و برخی از 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:242:غاز عبار تند از: غاز پومر و غاز تولوز و غاز 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:243:کلموگوری. تخم‌گذاری غاز ماده در اواخر 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:246:آوردن جوجه زیر غاز ۰ تاه ۱ تحم 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:249:بوقلمون ۱۰ تا ۲۰ تخم غاز می‌گذارند)؛ 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:252:غاز: 22 [- قاز] (.) کوچکترین واحد پول 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:253:در عهد قاجاربه. هر «جندکك» معادل ۲ غاز 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:254:بود. پنج غاز (ینغاز) معادل نیم شاهی و ده 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:255:غاز معادل یک شاهی بود. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:258:غازییکی: ۰:۷ (امر.) واحدی برای 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:260:می‌گفتند و از مس سکه زده می‌شد و ده غاز 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:263:غازبین: «-7 [- غازبیننده] (ص‌فا.) آنکه 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:264:یک غاز را در نظر گیرد و حساب کند. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:266:غازچران: 7 [- غازچراننده] 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:270:غازغاز: 72ب.«(ص.) از هم شکافته و باز
```


## [2026-09-05T20:53:50.495Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '205,275p' MON_part2.txt",
 "description": "Print Moin ghaz context"
}
```


### [2026-09-05T20:53:50.542Z] TOOL RESULT

```
زندگی در غار. 

غاروغور: ۵۲-(۱۵۲)۲ (امر.) هرج و 
مر ج» آشوب» فتنه. (عم.) صداهایی که از 
شکم شنیده شود. . (عم.) هیاهوبی که در 
موقع نزاع کنند. 

غار: ۱:22- غاژ](.) شکاف. چاک. تراکک. 


غاز فرهنگ فارسي معیر ۱۰۵ 


باره» زنده. پینه و وصله‌ای که بر جامه 
دوزند. پنبهةً محلوج. 

غاز: 22 (.) نبازه حاجت؛ مق. ناز. 

غاز: 22, [- غاژ] (.) خار (گل با درخت)؛ 
غاز؛ 2, [تر. - قاز] (.) (جاد.) پرنده‌ای 
است از راستة برده بایان که جثه‌ای 
درشت‌تر از اردکث دارد و آن مانند مرغابی 
و اردکك غذایش را در آب جستجو می‌کند 
ولی میل وی به آب کمتر از آنها است و 
ببشتر به خاکك تمایل دارد. نسبهة نیرومند و 
منقارش قوی و پهن و طویل است. گردنش 
دراز و بال‌هايش کاملاً رشد و نمو بافته و 
اهایش دارای طولی متوسط است و بهتر از 
اردکك راه می‌رود. در مراتع بهتر زندگی 
می‌کند و به اصطلاح در زمین‌های علفی 
می‌چرد. غازهای وحشی بصورت دسته‌های 
عظیمی در شمال آسیا و اروپا زندگی 
می‌کنند و در زمستان بطرف مرکز اروپا و 
اسب و گاهی شمال ایران مهاجرت می‌نمایند. 
غاز انواع و نژادهای مختلف دارد و برخی از 
نچادهایش در صورت توجه و تغذیة نیک تا 
۲ کبلو وزن بیدا می‌کنند. نژادهای مختلف 
غاز عبار تند از: غاز پومر و غاز تولوز و غاز 
کلموگوری. تخم‌گذاری غاز ماده در اواخر 
پیز است و معمولا" وقتی که ۱۲ تا ۳۰ 
تخم بگذارد کرچ می‌شود و برای بعمل 
آوردن جوجه زیر غاز ۰ تاه ۱ تحم 
می‌گذارند و آنها را زیر بوقلمون و مرغ هم 
می‌شود گذاشت (زیر مرغ ۴ تا " و زیر 
بوقلمون ۱۰ تا ۲۰ تخم غاز می‌گذارند)؛ 
قاز. 

غاز: 22 [- قاز] (.) کوچکترین واحد پول 
در عهد قاجاربه. هر «جندکك» معادل ۲ غاز 
بود. پنج غاز (ینغاز) معادل نیم شاهی و ده 
غاز معادل یک شاهی بود. 


غازییکی: ۰:۷ (امر.) واحدی برای 
مسک وک در عهد صفویه و آن را «پول» هم 
می‌گفتند و از مس سکه زده می‌شد و ده غاز 
تدگی معادل یک شاهی بوده است. (فلسفی. 
شاه عباس ۳۷۷:۲ ج ۲؛ ایضاً ۵۹:۳ ۲.) 
غازبین: «-7 [- غازبیننده] (ص‌فا.) آنکه 
یک غاز را در نظر گیرد و حساب کند. 
( کد .0( سیار لشیم سحت حسسن. 
غازچران: 7 [- غازچراننده] 
(ص‌فا.) آنکه بط‌ها را چراند. آنکه کار 
سهو ده کند. 

غازغاز: 72ب.«(ص.) از هم شکافته و باز 
شده. ترک ترکک. شکاف شکاف. 
غازغان: 22 [تر. - قازقان - غزغن] (.) 
دیگ بزرگ مسی؛ مرجل. 

غازل: 2261:[ع.] (افا.) ریسنده.
```


## [2026-09-05T20:53:52.142Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources\npython3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['MON','BQT','IEC','POK','AHD','KLN','UEC']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:900])\n    print()\n\"",
 "description": "Check refs_online for MON BQT IEC"
}
```


### [2026-09-05T20:53:53.872Z] TOOL RESULT

```
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.", "notes": "", "cites": "column/page number of Mann, An Indo-Europea

POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: lea

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based l

UEC null
```


## [2026-09-05T20:54:04.999Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'ghansis' in p or 'hansis' in p and 'goose' in p:\n        print('leaf',i,'-> approx printed pp', (i-15)*2, (i-15)*2+1)\nEOF",
 "description": "Locate IEC ghansis leaf"
}
```


## [2026-09-05T20:54:05.844Z] TOOL CALL #18: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1870 2>&1 | head -60",
 "description": "Fetch Borhan page 1870"
}
```


### [2026-09-05T20:54:06.855Z] TOOL RESULT

```
leaf 185 -> approx printed pp 340 341
leaf 238 -> approx printed pp 446 447
```


### [2026-09-05T20:54:14.772Z] TOOL RESULT

```
(no exact page map; using offset -1205 -> pdf page 665; check the printed number and re-run with --pdf-page if off)
REF: BQT:1870  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 665  OCR-lang: fas

کیاه نمناك ۱۸۹۸
گیاه نمناك - بکر ها وفتح نون باشد چه کیتی بمعنی جهان و نوردیدن بمعنی
بروزن سیاه غمناك » سبزه‌است که آنرا خرفه گردیدن است - وکنایه از آفتاب عالمتاب است-
و پریهن میگویند و بمریی بقلةّالحمقا خوانند. و کنایه از اسکندر هم هست - و اسب را نیز
یر - بقتم اولوض بای ابجنوسکون | گفا اي
نالی و رای قرشت » نوعی ازپیکان تیر باشد۱ . گیج * بکسر اول وسکون ثانی وجیم؛
گیتی ؟ « بکر اول وفوقانی‌وسکون بمعنی پربشان وپراکنده خاطر باشد - وشخصی
نانی وتحتانی» دلیا وروز کار و جهان راکوبند ۳ را نی زکویند که پیب صدمه دماغ او پرشان
- و بمعثی زمین هم هست - و کلی است بسیار شده باشد - و احمق و ابله ومتحیر و اسر گشته
خوشبوی که از دربای ره آورند ۴ ؛ و با ای و حیرانرا نیز کویند ۸ ؛ و باین معنی با جیم
مثلئه هم بنظرآمدء است درموٌ بدالفلا ۰ فارسی هم بنظر آمده است - وخودستای وصاحب
"لیتی بان ‎٩‏ - بسسنی نگاه دارندة دنا عجب وتکبر را هم کفته‌اند .
و رو زگلر است که کنایه ازپادشاء هفت اقلیم باشد گیجه * - بکر اولوفتح جیم:بممنی
چه گیتی بمعنی دیا وبان نگاهدارنده ومخافظت | کیج‌است که پربشان وپرا کنده‌ومتحیروس رکشته
کننده راگوند . وحیران باشد .
گیتی پژوه ۱ « بنم با وزای‌فارسی» گیجیده *۱- بروزن پیچیده . بمعنی
بمعنی دبا طلب وطالب دلیا باشد چه کیتی‌بمعنی دماغ پربشان شده و سراسیمه کشته و سرگردان
دنیاوپژوه وطالب وخواهان وجوبان‌باشد- و کنایه | وحیران گردیده باشد .
از پادشاه است . گید < بکر اول وسکون انی و دال
گیتی نورد ۷ « بسسنی جهان کرد |[ ابجد. مرغ گوشتربارا کویند که غلیواج‌است ۰۱۱
۱ - وآنرا ۸ زره‌بر > نیز کوبند « رشیدی » . ظ . از :کی(ه.م.) 1 بر(برندم) .
۴ - اوستا 8281808 «بارتولمه ۰۶۷۹ پازند ۰8841 88181 . مُط)آع . پهلوی دا8816
و طقا8۸ ‎٩‏ یب رکه ی۸*۰» وطالا8۸: منای ۲:۲۷۸ » و 88116 ( دنیوی) » سربانی 88163
۰ هوبشمان ۹۸۹ > و رك : اسشق: ایضاً و فقس :گهان . جهان .
۴ - هرآنکه گردش کیتی بکین او برخاست بفیر مصلحتش رهبری کند ایام .
۱ « کلتان ص ۱۱۹ *.
۴ - رك :کل کیتی . ‎٩‏ - از :کیتی + بان ( پوند نسبت و اصاف ).
‎٩‏ - از :کیتی + پژوه ( پژوهنده ). ۷ - از : کیتی + نورد (نوردنده) .
۸ - «کیج » معجب و احمق بود . قربم گفت :
همه با حیزان حیز و همه باکیجان کیج همه با دزدان دزد وهمه با شنگان شنکه»
« لغت فری *۹ .۰
و رك : همان کتاب ص ۷۳ . ‎٩‏ -رك :کیج . دره سر کیجه » بمعنی کردش سر«رشیدی»
و دوارسر .کیجه مرکب است از :کیج (قس :کیجیده )۰ ( پوند حاصل مصدر ) [ رك :
ام مصدر پقلم نکارنده ی ‎٩۵‏ بیعد ‎ .]‏ *۱- اسم مفعول ازه «کیجیدن » .
۱- رك : رشیدی . « ظاهراً همان جانور است که مشابه بود به غلیواج » و آن نوع
علیحده است » و بهندی ار آنرا «کیدهء » کوبند بدال مخلوطالتلفظ به ها . واین از عالم توافق
لسانین است.» « سراج اللغات بنقل‌فرهنکه نظام » .
```


## [2026-09-05T20:54:26.456Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (184,185,186,238):\n    p=pages[i]\n    print('=== leaf',i,'len',len(p))\n    print(p[:300].replace('\\n',' | '))\n    print('...TAIL...', p[-200:].replace('\\n',' | '))\nEOF",
 "description": "Inspect IEC leaves"
}
```


## [2026-09-05T20:54:27.496Z] TOOL CALL #20: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1870 --pdf-page 637 2>&1 | head -50",
 "description": "Fetch Borhan corrected page"
}
```


### [2026-09-05T20:54:28.164Z] TOOL RESULT

```
=== leaf 184 len 3464
aoi ‘spear’; Gallo-Lat. gae- sum; Br. goaó, goaf, gwat; Cor. gew; W gwaew lance, javelin’, w. induced labialism; OHG gër, MHG geér(e); OE gàr; Du. geer “bias, crosscut, gore’; ON geirr ‘spear’, geiri ‘gore, gusset | ghāið (ghāmi, ghíghami) ‘go, move, de- part'. Cf. gai-, gíga-. WP I, 543 Skt. hayáàmi,
...TAIL...  gaman, ds gamni; MHG gamen ‘sport, pleasure, game, mockery’; cf. also MHG gamel, id.; LG gammel ‘din’; OCS gomonü (fdin. Gmc. LW); OCz. homon ‘tumult; brawl’; Cz. homonit, v. ‘toll, peal’; Ukr. cf. v
=== leaf 185 len 3706
id-homin (for *od-homon ‘echo’) beside homin “noise? | ghan- (ghand-) ‘contain, be ample, suffice". WP I, 589. Cf. ghend-, ghnd- Skt. ghanáh ‘total, whole”: Per. cf. a-gandan, v. “fill, cram" beside ganjidan, v. ‘contain’; a-gin ‘full, a-ganiS, id. (: Skt. a-han-); Oss. cf. gánàn, in cpds. ‘means’; Gk
...TAIL...  and cf. ghargh-) | ghasdhos (ghazdhos), is, io “rod”. Cf. ghast-. WP I, 541 Mir. gat, Ir. gad ‘rod, switch’, Mod. also ‘osier’ beside gathán ‘ray, beam’; Br. cf. gadan ‘withy’; Go. gazds 'goad';; MHG g
=== leaf 186 len 3770
art, id. beside OHG gerta, G Gerte, id. (fr. *ghas- dhio); Du. gard ‘stick, yard" beside (uml.) OE gierd, id.; LW in OCS Zirdi; ON gaddr, gadd | (ghaudho, see ghoud-. Thus only in ON gauóa “bark, scold’) | ghaughor- (roam, wander; wandering’. Cf. ghaug-, ghaugh- Ir. guagaire *wanderer, tramp'; MHG gouge
...TAIL... v. Zeburs ‘two-pronged fork") (ghebholos (2) *piece' in OE geofola, giefel *morsel'. See gabholos and cf. WP I, 571) ghed- “acquire; acquisition'. Cf. ghnd- and WP I, 589 Oss. zíd, zudà (‘greedy fr. *
=== leaf 238 len 3639
� ‘roar’; Gk. cf. kagkhaláo ‘guffaw’. | (&hanos ‘gaping, empty’ in Gk. khános "open | mouth"; khan-dón 'gapingly': ON gana ‘gape’ beside (*-à- in) mod. Icel. góna “to gawp'. See $hiia-, etc.) | $hansis ‘goose’. Onomat. cf. ghansis and ghiia- w. extns. WP I, 536 The variant is present in Li. žąsis, gp Zasü
...TAIL... ‘go, step’; Zygis, m. ‘campaign’. (The se- mantic links are somewhat obscure) | Sheim-, gheimn- (ghim-) (resolutions of a prototype *ghiiom-, see £hiia- & extns.) WP I, 546 Skt. cf. himáh, himàá, hemant
```


### [2026-09-05T20:54:30.060Z] TOOL RESULT

```
REF: BQT:1870  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 665  OCR-lang: fas

کیاه نمناك ۱۸۹۸
گیاه نمناك - بکر ها وفتح نون باشد چه کیتی بمعنی جهان و نوردیدن بمعنی
بروزن سیاه غمناك » سبزه‌است که آنرا خرفه گردیدن است - وکنایه از آفتاب عالمتاب است-
و پریهن میگویند و بمریی بقلةّالحمقا خوانند. و کنایه از اسکندر هم هست - و اسب را نیز
یر - بقتم اولوض بای ابجنوسکون | گفا اي
نالی و رای قرشت » نوعی ازپیکان تیر باشد۱ . گیج * بکسر اول وسکون ثانی وجیم؛
گیتی ؟ « بکر اول وفوقانی‌وسکون بمعنی پربشان وپراکنده خاطر باشد - وشخصی
نانی وتحتانی» دلیا وروز کار و جهان راکوبند ۳ را نی زکویند که پیب صدمه دماغ او پرشان
- و بمعثی زمین هم هست - و کلی است بسیار شده باشد - و احمق و ابله ومتحیر و اسر گشته
خوشبوی که از دربای ره آورند ۴ ؛ و با ای و حیرانرا نیز کویند ۸ ؛ و باین معنی با جیم
مثلئه هم بنظرآمدء است درموٌ بدالفلا ۰ فارسی هم بنظر آمده است - وخودستای وصاحب
"لیتی بان ‎٩‏ - بسسنی نگاه دارندة دنا عجب وتکبر را هم کفته‌اند .
و رو زگلر است که کنایه ازپادشاء هفت اقلیم باشد گیجه * - بکر اولوفتح جیم:بممنی
چه گیتی بمعنی دیا وبان نگاهدارنده ومخافظت | کیج‌است که پربشان وپرا کنده‌ومتحیروس رکشته
کننده راگوند . وحیران باشد .
گیتی پژوه ۱ « بنم با وزای‌فارسی» گیجیده *۱- بروزن پیچیده . بمعنی
بمعنی دبا طلب وطالب دلیا باشد چه کیتی‌بمعنی دماغ پربشان شده و سراسیمه کشته و سرگردان
دنیاوپژوه وطالب وخواهان وجوبان‌باشد- و کنایه | وحیران گردیده باشد .
از پادشاه است . گید < بکر اول وسکون انی و دال
گیتی نورد ۷ « بسسنی جهان کرد |[ ابجد. مرغ گوشتربارا کویند که غلیواج‌است ۰۱۱
۱ - وآنرا ۸ زره‌بر > نیز کوبند « رشیدی » . ظ . از :کی(ه.م.) 1 بر(برندم) .
۴ - اوستا 8281808 «بارتولمه ۰۶۷۹ پازند ۰8841 88181 . مُط)آع . پهلوی دا8816
و طقا8۸ ‎٩‏ یب رکه ی۸*۰» وطالا8۸: منای ۲:۲۷۸ » و 88116 ( دنیوی) » سربانی 88163
۰ هوبشمان ۹۸۹ > و رك : اسشق: ایضاً و فقس :گهان . جهان .
۴ - هرآنکه گردش کیتی بکین او برخاست بفیر مصلحتش رهبری کند ایام .
۱ « کلتان ص ۱۱۹ *.
۴ - رك :کل کیتی . ‎٩‏ - از :کیتی + بان ( پوند نسبت و اصاف ).
‎٩‏ - از :کیتی + پژوه ( پژوهنده ). ۷ - از : کیتی + نورد (نوردنده) .
۸ - «کیج » معجب و احمق بود . قربم گفت :
همه با حیزان حیز و همه باکیجان کیج همه با دزدان دزد وهمه با شنگان شنکه»
« لغت فری *۹ .۰
و رك : همان کتاب ص ۷۳ . ‎٩‏ -رك :کیج . دره سر کیجه » بمعنی کردش سر«رشیدی»
و دوارسر .کیجه مرکب است از :کیج (قس :کیجیده )۰ ( پوند حاصل مصدر ) [ رك :
ام مصدر پقلم نکارنده ی ‎٩۵‏ بیعد ‎ .]‏ *۱- اسم مفعول ازه «کیجیدن » .
۱- رك : رشیدی . « ظاهراً همان جانور است که مشابه بود به غلیواج » و آن نوع
علیحده است » و بهندی ار آنرا «کیدهء » کوبند بدال مخلوطالتلفظ به ها . واین از عالم توافق
لسانین است.» « سراج اللغات بنقل‌فرهنکه نظام » .
```


## [2026-09-05T20:54:45.549Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (171,172,173):\n    print('=== leaf',i,'->approx p',(i-15)*2)\n    print(pages[i][:400].replace('\\n',' | '))\nEOF\necho \"---- head of ref_page.py args\"\nsed -n '1,60p' /home/sfmqrb/git/rishe/tools/ref_page.py",
 "description": "Check IEC leaf 172 and ref_page args"
}
```


### [2026-09-05T20:54:47.181Z] TOOL RESULT

```
=== leaf 171 ->approx p 312
(dump of Dr, fr. *gogio); Sw. koka ‘clod’; Li. gáoga *trunch- eon’, guogas ‘Mariampol Lithuanian; yokel'; guoge ‘knob; head; duffer'; Blg. cf. proper n. Gago | gogolos, ios (gog9l-) ‘knob, tapering object Per. gazar ‘carrot; Arm. kakyi (“lime-tree”, fr. the fruit); OS kakeli ‘icicle’? | goig- (1) bend, twist Gaelic gaog ‘knot in yarn’; ON keikja “bend back’; Li. gieZiü, ^ti, v. (2) “plot. (Isophonic: 
=== leaf 172 ->approx p 314
ti ‘get grimy’. (Skt. garha ‘abuse’: MHG karc, -ges) | gorgo, io (1) ‘seize, snatch’. Cf. korg- Av. garoz- (2) ‘seize’; Arm. korzem, id.; ON cf. karskr (“brisk”, if fr. *gorgsK-) | gorgo, ið (2) ‘wail, weep’. Cf. garg- and next. Oss. qårzin, $árzun ‘groan’; Skt. garjami ‘roar’; Arm. kocim, kocem (1) ‘mourn’; Pahl. garzi- tan ‘wail’; Av. garoz-, jaroz-, id.; EME to cark *be anxious for | gor?os, us “hard
=== leaf 173 ->approx p 316
roak; chatter, scrape’ beside gragal'a ‘chatter, as jay or magpie’; OHG kragil, adj. ‘chattery’; MHG krageln, kregeln, v. ‘cackle’ | grakido, ið ‘croak, caw, cackle’. Cf. grako- | 291 | los, gráquos, grāið, grakso It. gracidare, id. beside gracidio, m. ‘croak, caw'; Br. graka, v. id.; G krüchzen, id. (Cf. Cz. hrokat ‘murmur, our" and MHG kragelen, etc., & LG simplex kraken fr. a type *grag-) | grakso, ið 
---- head of ref_page.py args
#!/usr/bin/env python3
"""Fetch ONE cited page of a scanned reference, on demand.

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
"""
import sys, os, json, subprocess, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "data", "verification", "sources")
TABLE = os.path.join(SRC, "refs_online.json")
REFS = os.path.join(SRC, "refs")
OCR = os.path.join(REFS, "ocr")
TESSDATA = os.path.join(REFS, "tessdata")


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    if not args:
        print(__doc__); return 2
    m = re.match(r"^([A-Z]+)(\d*):(\d+)$", args[0])
    if not m:
        print("expected ABBR:page (e.g. BQT:918 or MON5:528)"); return 2
    abbr, vol, page = m.group(1), m.group(2), int(m.group(3))
    table = json.load(open(TABLE, encoding="utf-8"))
    ref = table.get(abbr, {})
    scans = ref.get("scans") or []
    if vol:
        scans = [s for s in scans if str(s.get("volume", "")) == vol] or scans
    scan = None
    for s in scans:
        if s.get("requires_volume") and not vol:
            continue
        if s.get("first_printed", 0) <= page <= s.get("last_printed", 10**9):
            scan = s; break
    if "--pdf-page" in argv:
        pdf_page = int(argv[argv.index("--pdf-page") + 1])
        scan = scan or (scans[0] if scans else None)
    elif scan:
        pdf_page = None
        pm = scan.get("page_map")
        if pm and os.path.exists(pm):
            pdf_page = json.load(open(pm)).get("map", {}).get(str(page))
        if pdf_page is None:
            pdf_page = page + int(scan.get("pdf_offset", 0))
            print(f"(no exact page map; using offset {scan.get('pdf_offset', 0)} -> pdf page {pdf_page}; check the printed number and re-run with --pdf-page if off)")
```


## [2026-09-05T20:54:48.185Z] TOOL CALL #22: Bash

```json
{
 "command": "pdftoppm -f 179 -l 179 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg179 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render pdf page 179"
}
```


### [2026-09-05T20:54:50.454Z] TOOL RESULT

```
total 20412
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 16:54 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  5 16:02 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   68775 Sep  5 16:43 ary440.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb  100925 Sep  5 16:52 bqt_pdf600.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb   17908 Sep  5 16:44 build151a.py
-rw-rw-r-- 1 sfmqrb sfmqrb   15986 Sep  5 16:46 build151b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   11172 Sep  5 16:47 build151c.py
-rw-rw-r-- 1 sfmqrb sfmqrb   19592 Sep  5 16:50 build151d.py
-rw-rw-r-- 1 sfmqrb sfmqrb    6433 Sep  5 16:50 build151z.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51529 Sep  5 16:51 build152.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51266 Sep  5 16:51 build154.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61639 Sep  5 16:53 build155.py
-rw-rw-r-- 1 sfmqrb sfmqrb   70485 Sep  5 16:53 build156.py
-rw-rw-r-- 1 sfmqrb sfmqrb   72953 Sep  5 16:48 build158.py
-rw-rw-r-- 1 sfmqrb sfmqrb   45662 Sep  5 16:49 build164.py
-rw-rw-r-- 1 sfmqrb sfmqrb   50404 Sep  5 16:53 build168.py
-rw-rw-r-- 1 sfmqrb sfmqrb    7816 Sep  5 16:35 c_am2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14765 Sep  5 16:35 c_am3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10038 Sep  5 16:35 c_empty2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4123 Sep  5 16:34 crop_am.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4986 Sep  5 16:34 crop_arabic_refs.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7702 Sep  5 16:34 crop_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   16978 Sep  5 16:34 crop_morocco.png
-rw-rw-r-- 1 sfmqrb sfmqrb  163996 Sep  5 16:46 gar2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  124975 Sep  5 16:47 gar3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77205 Sep  5 16:46 gar.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:18 kent.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     222 Sep  5 16:30 leaf.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57617 Sep  5 16:20 mk129.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74680 Sep  5 16:26 mk131.py
-rw-rw-r-- 1 sfmqrb sfmqrb   33365 Sep  5 16:25 mk133.py
-rw-rw-r-- 1 sfmqrb sfmqrb   42635 Sep  5 16:29 mk140.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51288 Sep  5 16:30 mk143.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57696 Sep  5 16:46 mk153.py
-rw-rw-r-- 1 sfmqrb sfmqrb   49505 Sep  5 16:50 mk157.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56703 Sep  5 16:54 mk166.py
-rw-rw-r-- 1 sfmqrb sfmqrb   30384 Sep  5 16:51 mk170.py
-rw-rw-r-- 1 sfmqrb sfmqrb    4344 Sep  5 16:49 n12b.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3969 Sep  5 16:49 n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2692 Sep  5 16:49 n16.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11831 Sep  5 16:32 node4.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7427 Sep  5 16:32 node7.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:13 oldpers_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    6054 Sep  5 16:36 p152_e0left.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2672 Sep  5 16:36 p152_node2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   41788 Sep  5 16:53 p173_ital.png
-rw-rw-r-- 1 sfmqrb sfmqrb   32898 Sep  5 16:53 p173_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb  671488 Sep  5 16:52 p600_350.png
-rw-rw-r-- 1 sfmqrb sfmqrb  139701 Sep  5 16:52 p600_foot2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  183909 Sep  5 16:52 p600_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1717 Sep  5 16:52 p600_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5162 Sep  5 16:52 p600_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22067 Sep  5 16:29 part0.json
-rw-rw-r-- 1 sfmqrb sfmqrb   14156 Sep  5 16:22 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17147 Sep  5 16:44 part_a.json
-rw-rw-r-- 1 sfmqrb sfmqrb   15703 Sep  5 16:46 part_b.json
-rw-rw-r-- 1 sfmqrb sfmqrb   10974 Sep  5 16:47 part_c.json
-rw-rw-r-- 1 sfmqrb sfmqrb   19420 Sep  5 16:50 part_d.json
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
-rw-rw-r-- 1 sfmqrb sfmqrb  101504 Sep  5 16:43 pg156.png
-rw-rw-r-- 1 sfmqrb sfmqrb  169880 Sep  5 16:34 pg158_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80624 Sep  5 16:34 pg158.png
-rw-rw-r-- 1 sfmqrb sfmqrb  124379 Sep  5 16:31 pg159_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   27814 Sep  5 16:31 pg159.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4694 Sep  5 16:31 pg159_word.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168057 Sep  5 16:34 pg161_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76745 Sep  5 16:34 pg161.png
-rw-rw-r-- 1 sfmqrb sfmqrb  110270 Sep  5 16:42 pg162_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76438 Sep  5 16:42 pg162.png
-rw-rw-r-- 1 sfmqrb sfmqrb    8523 Sep  5 16:42 pg162_verse.png
-rw-rw-r-- 1 sfmqrb sfmqrb   25911 Sep  5 16:32 pg163.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59398 Sep  5 16:33 pg164.png
-rw-rw-r-- 1 sfmqrb sfmqrb   61265 Sep  5 16:40 pg165.png
-rw-rw-r-- 1 sfmqrb sfmqrb  116877 Sep  5 16:46 pg167.png
-rw-rw-r-- 1 sfmqrb sfmqrb   86005 Sep  5 16:39 pg168.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68420 Sep  5 16:42 pg169.png
-rw-rw-r-- 1 sfmqrb sfmqrb   37351 Sep  5 16:44 pg170.png
-rw-rw-r-- 1 sfmqrb sfmqrb  120612 Sep  5 16:49 pg171_450.png
-rw-rw-r-- 1 sfmqrb sfmqrb   73551 Sep  5 16:43 pg171.png
-rw-rw-r-- 1 sfmqrb sfmqrb   52970 Sep  5 16:53 pg173.png
-rw-rw-r-- 1 sfmqrb sfmqrb   54907 Sep  5 16:54 pg175.png
-rw-rw-r-- 1 sfmqrb sfmqrb   57139 Sep  5 16:54 pg179.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44812 Sep  5 16:34 pg532.png
-rw-rw-r-- 1 sfmqrb sfmqrb  153161 Sep  5 16:34 pg532_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep  5 16:14 prt.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  333088 Sep  5 16:16 sod135_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1817364 Sep  5 16:16 sod135.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  101641 Sep  5 16:15 sod136_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1892712 Sep  5 16:15 sod136.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   56398 Sep  5 16:26 write144.py
```


## [2026-09-05T20:54:59.515Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(178,192):\n    nums=re.findall(r'\\|\\s*(\\d{3})\\s*\\|', pages[i])\n    print(i, nums)\nEOF",
 "description": "Find printed page markers in IEC leaves"
}
```


## [2026-09-05T20:55:00.401Z] TOOL CALL #24: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg179.png"
}
```


### [2026-09-05T20:55:01.207Z] TOOL RESULT

```
178 []
179 []
180 []
181 []
182 []
183 []
184 []
185 []
186 []
187 []
188 []
189 []
190 []
191 []
```


### [2026-09-05T20:55:01.566Z] TOOL RESULT

```

```


## [2026-09-05T20:55:01.563Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T20:55:22.470Z] TOOL CALL #25: Bash

```json
{
 "command": "sed -n '60,140p' tools/ref_page.py; echo \"=== scans ===\"; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(json.dumps(d['BQT'].get('scans'),ensure_ascii=False,indent=1))\"",
 "description": "Inspect ref_page.py rest and BQT scans"
}
```


### [2026-09-05T20:55:24.233Z] TOOL RESULT

```
            print(f"(no exact page map; using offset {scan.get('pdf_offset', 0)} -> pdf page {pdf_page}; check the printed number and re-run with --pdf-page if off)")
    else:
        print(f"no scan of {abbr} covers printed page {page} (see 'scans' in refs_online.json)"); return 1
    pdf = scan["file"] if os.path.isabs(scan["file"]) else os.path.join(REFS, scan["file"])
    if not os.path.exists(pdf):
        print("PDF not found:", pdf); return 1
    lang = scan.get("lang", "fas")
    out_dir = os.path.join(OCR, abbr + vol)
    os.makedirs(out_dir, exist_ok=True)
    base = os.path.join(out_dir, f"{page:04d}")
    png, txt = base + ".png", base + ".txt"
    if not os.path.exists(png):
        subprocess.run(["pdftoppm", "-f", str(pdf_page), "-l", str(pdf_page), "-r", "300", "-png", "-singlefile", pdf, base], check=True)
    if not os.path.exists(txt):
        # try the PDF's own text layer first; fall back to tesseract
        r = subprocess.run(["pdftotext", "-layout", "-f", str(pdf_page), "-l", str(pdf_page), pdf, "-"], capture_output=True, text=True)
        text = r.stdout if len(r.stdout.strip()) > 80 else ""
        if not text:
            env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)
            r = subprocess.run(["tesseract", png, "-", "-l", lang, "--psm", "6"], capture_output=True, text=True, env=env)
            text = r.stdout
        header = f"REF: {abbr}{vol}:{page}  PDF: {os.path.relpath(pdf, ROOT)} page {pdf_page}  OCR-lang: {lang}\n\n"
        open(txt, "w", encoding="utf-8").write(header + text)
    vision = base + ".vision.txt"   # a transcription made by reading the PNG; preferred over OCR
    if "--image" in argv:
        print("IMAGE:", png)
    if os.path.exists(vision):
        print("[transcription from the page image; OCR text in", os.path.relpath(txt, ROOT) + "]")
        print(open(vision, encoding="utf-8").read())
    else:
        print(open(txt, encoding="utf-8").read())
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
=== scans ===
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


## [2026-09-05T20:55:34.969Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nls | head -30\npython3 - <<'EOF'\nimport re\nt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor p in pages:\n    if 'گیس' in p:\n        m=re.search(r'\\[pdf page (\\d+)\\]',p)\n        head=p.strip().split('\\n')[0:3]\n        cnt=p.count('گیس')\n        print('pdfpage',m.group(1) if m else '?','count',cnt,'|',' / '.join(head)[:120])\nEOF",
 "description": "Find gis in Borhan v3 OCR"
}
```


### [2026-09-05T20:55:36.929Z] TOOL RESULT

```
BQT_v3_pagemap.json
BQT_v3_pages.txt
BQT_v3_picofile.pdf
BQT_v4_pages.txt
BQT_v4_pages.txt.pages
BQT_v4_picofile.pdf
BQT_v5_pages.txt
BQT_v5_pages.txt.pages
BQT_v5_picofile.pdf
pdfpage 176 count 1 | [pdf page 176] / ‎—\rar‏ عنم / ‎sc‏ ارزان - کنایه از کیوی چنیر ‎gine = Fy‏ عنبرچه ‎sath‏ وآن
pdfpage 265 count 1 | [pdf page 265] / ۱۷۲ ay / eS ‏و سکون ثالث « نم ولابتی وبتدری‌است برساحل | ثالث وکاف فارسی بتحتالی کشیده وسین‌بی‎
pdfpage 437 count 1 | [pdf page 437] / حطی ۰ ‎ye‏ است که آنرا قسط گوشد - بول / و حیض برالد و فالج و استرخای ‎(acl‏ را لاف
pdfpage 548 count 1 | [pdf page 548] / ۱۷۵۱ / 
pdfpage 571 count 1 | [pdf page 571] / ‎SS‏ وت / گیست ه بفتح اول وثالی وسکون‌سین
pdfpage 667 count 3 | [pdf page 667] / کیسودار هرا /
```


## [2026-09-05T20:55:44.323Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 -c \"\nimport json;d=json.load(open('BQT_v3_pagemap.json'))\nm=d.get('map',d)\nprint(type(m), len(m))\nfor k in ['1860','1865','1870','1875','1880','1890','1898','1900']:\n    print(k, m.get(k))\n\"",
 "description": "Inspect BQT v3 pagemap"
}
```


### [2026-09-05T20:55:45.998Z] TOOL RESULT

```
<class 'dict'> 592
1860 None
1865 None
1870 None
1875 671
1880 677
1890 687
1898 695
1900 697
```


## [2026-09-05T20:55:54.359Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nrm -f data/verification/sources/refs/ocr/BQT/1870.png data/verification/sources/refs/ocr/BQT/1870.txt\ntimeout 600 python3 tools/ref_page.py BQT:1870 --pdf-page 667 --image 2>&1 | head -60",
 "description": "Fetch Borhan printed page 1870"
}
```


### [2026-09-05T20:56:02.833Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1870.png
REF: BQT:1870  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 667  OCR-lang: fas

کیودار -۱۸۷۰-
زنان است .#۴ و مردم عامیراکوبند .*
گیسو داد ۱ - با دال ابجد بر وزن گیل‌دارو ‎٩‏ - بکر اول . چوبکی
نیکوکار , معروف است ۴ - و کنایه از سید ۴ | باشد سیاه رنگه و آنر| بساحل دریای خزر
ومولازاده و پیرزاده هم هت . با پند و آنرا تر وماده میباشد «کدو وانه را تافع
گیل ؟ - با انی مجهول بروزن فیل ۰ |[ است که کرم شکم باشد و معرب آك چیل‌دارو ات .
کیلان را کوبند و آن ولایتی باشد معروف از گيلك ۱ « بائانی‌مجهول‌بروزن مبلك.
تبرستان - و بزبان کیلانی » رعیت و روستایی | بزبان کیلان مردم عامی و روستایی و رعیت را

۱- از : کیسول دار ( دارنده ). ۴ -بعنی صاح بکیسو .

۴ - بمناسبت آلکه در قدیم علوبان کیو داشتند . رك : کیسو .

۴ - پهلوی [غ03 ( رك : فهرست مارکوارت . شهرستانهای ابران » و رك : کربتنن.
ساسان ص ۲۰۹) بقوم ساکن کیلان اطلاق شده . رك :گیلان . - از :گیل (کیلان)
+ دارو ؛ لغة داروبی که درکنار دربای کیلان ( بحر خزر ) روید ( برهان در شرح : سغیر ) ۰
معرب آن جیل دارو . ‎٩‏ - درکیلکی اةاع ( اهلکیلان کیلانی ) فن :کیله » و
کیلکی لهجهٌ مردم کیلان راکویند .

0 یحو - بکر اول و ضم سوم ۳ کیس (۸.م.) از اوستایی 82688 ( رك :کیس ):
در اوراق مانوی بپهلوی 888۷8 ( کلاله : طرء ) ۰ 815۷۷80۷7 ( با عوی مجعد ) . آرمنی
7۳ ر(83. ۶ با , 17 , 8505 و...صقند۳ ۸1:04416 ۱۶ اقلا ۸ موصندصصعتن0
در پپلوی 888۵۳ «اوئوالا ۳۸۳ » ؛ موی بلند که ازپشت کردن تجاوز کند ( جمع آن؛ کیسوان,
کیسوها ) : ۶« شیادی کیسوان بافت بسورت علوبان ... » «کلستان ص ۵۳ >.

#لان - بکس اول از : گیل (وم.) + آن (پوند مکان) . پپلوی ابا 6 یعمنی
مملکت کیل ( 6781 ) ها . در نزد بودانیان 636186 « داثرة الممارف اسلام » . در اوستا
نام ناحیتی صورت ۷87612 آمده و خاورشناسان در تعیب محل آن اختلاف دارند . طیق سنت
آن . همان مملکت « پتشخوا رکر» ( طبرستان وکیلان ) است رك : پورداود . بشتها ج ۷۱
۱۹۴۱۸۱ وج اص ۷۵ متن و ح۱ . اندرآی همین ۵ ورنه > را ریشهٌ نام «کیلان»
دانته » ولی استاد بنونیست (درمذا کرء شفاهی) این حدی را رد کرده‌اند . چه ۷8 و ۷1 زبانهای
قدیم در فارسی به 80 و 81 تبدیل شود مانند وبشتاسی ۳ کشتاسپ » وراز < کراز » وبیستر -
کستر ؛ ولایت کیلان از ۳۹ درجه او ۲۸ دقیقه تا ۳۸ درجه و ۱۱ دقيقةٌ اعرض شمالی و از 4۸
درجه و44 دقیقه تا ۵*۰ درجه و۳۲ دقيقهٌ طول شرقی واقع شده . ازشمال محدود است ببحرخزر
و از مشرق بمازسران و از جنوب بقزوین وخصه و از مغرب بآذربایجان. طول‌آن ازشمالغربی
بجنوب شرفی ۲۲۵ و عرض‌آن از ۲۵ تا ۱۰۵ کیلومتر تغییر میکند .گیلان شامل نواحی ذیل
است:موازی که شهررشت درآن‌واقع‌است ۰ لشت نا. لاهیجان » لنگرود ورانکوه » دیلمان ؛عمارلو,
رحمتآباد » رودبار , شفت . ماسوله » فومن » تولم » چار فریضه و پپلوی » کسکر . ماسال :
شاسرمن , طالش دولاب . اسالم » کرکانرود وآستارا . کرسی آن شهر رشت است. رك :جغرافیای
سیاسی .کیهان. من ۲۹۳ ببمد - اکنونکیلان جزو استان یکم محسوب میشود .
```


## [2026-09-05T20:56:20.437Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN gaz ===\"; grep -n -i \"'Gans'\\|Gans\\b\" HRN.txt | head -20\necho \"=== HUB Gans ===\"; grep -n -i \"Gans\\b\" HUB.txt | head -20\necho \"=== ARY latin index qaz/gaz ===\"; grep -n -i \"GHANS\\|GANS\\|goose\" incoming/ARY/ARY_latin_index_pages.txt | head -20\necho \"=== ARY غاز ===\"; grep -n \"غاز\" incoming/ARY/ARY_pages.txt | head -20\necho \"=== TTS kaz ===\"; grep -n -i \"Gans\\b\" incoming/TTS/TTS_pages.txt | head -20",
 "description": "Grep Horn Hubschmann Aryanpur Vambery for goose"
}
```


### [2026-09-05T20:56:20.536Z] TOOL RESULT

```
=== HRN gaz ===
2337:arm. bad, bat *Ente'; alb. ^^a^« 'Gans' (G. Meyer,
=== HUB Gans ===
999:und Etymologic dunkel. Dem alban. pate *Gans'- wurde
=== ARY latin index qaz/gaz ===
326:elias) 9a aly ple 53 (KURGANS) 0 F yl alte Lot ula) Sci wie y
1091:Gans sae Gy Lt S cual os SOLS AAT |, Leal! y Oly! Ghalbo yg’ GLAD Sony we
9062:| RISHITI RISYATI, AGANSKRIT) eg Suibe
10355:(OLD CHURCH SLAVIC) 5.5 1 AGANSKRIT) 2 Sule
11054:AGANSRRIT) oy Sunil SHKAFTAN, SHKAF. :(PAHLAV]) «5.314
11465:3 GANS :(OLD HIGH GERMAN) 7S ial Qaz AFGHANI) (54) gli!
11466:GANS GERMAN) lJ HANSA, HANS. (SANSKRIT) 2 Ste
11468:GOOSE ENGLISH) .godS ANSER LATIN) 3
11469:GAAS (DANISH) Slailo GANSO SPANISH) lily!
11480:BARNHART: (GOOSE) 442 HUSA (CZECH) Soy
11483:ONIONS: (GOOSE) 406 Hus (SLOVAK) | gat
12623:GUR ALBANIAN) gist GIRIS AGANSERIT) cy Sse
12766:VERST ALATVIAN) (33) 3) AGANSKRIT) ey Suite
14564:NEBULE NABHAS GANSKRIT) 4 Sule
15384:POKORNY, —SS*~*~S~S~S*~« {GANSKRIT) a Sail
=== ARY غاز ===
108:سرزمین آغازین هند و اروپائیان
124:واژه‌های هند و اروپایی آغازین (۳۳070-18700-218078۸31) وابسته به جانوران و گیاهانی
126:دیسدمان دیگر در باره‌ی گهواره‌ی آغازین هند و اروپایی‌ها این است که زادگاه
172:زبان‌های گوناگون شد. (وجود واژه‌های مشترک میان هند و اروپایی و زبان سامی آغازین
269:آغازین بوده‌اند. آنها این واژگان و ویژگی‌های زبانی دیگر را با خود به سرزمین‌های دیگر بردند و دد,
284:دیرین‌شناسی زبانی وسیله‌ی دیگری است برای شناخت هند و اروپایی آغازین و خاستگاه ۱
289:شده‌اند. این جامعه در آغاز شکارگر -گر دآور (11701181-0۸7778587) بوده ر کم کم شبانی و
380:در انجیل آمده است که مردم پابل (8۸881) آغاز به ساختن برجی کردند که قرار بود بلندی
384:بعنوان یک واقعیت زبانشناسی نیز مورد تاکید بود. دانشمندان عهد عتیق معتقد بودند که آغاز
828:برخی از دانشمندان بر این اعقیده‌اند که تخاری‌ها در آغاز زیستمند مرکز اروپا بودند و به علت
1183:از دیرپاز آغاز شده است. مثلاً در زبان انگلیسی صدهاکتاب و مقاله و واژه‌نامه در این باره متتشر شده
1188:پژوهشها از مدتها پیش آغاز شده است.
1191:اخص توسط دانشمندان برونمرزی (بارتولومه» یونگر» هنینگه» نیبرگ) در چند دهه قبل آغاز شد.
1265:زین هم پژوهشگران آینه بناندکاری راک این کتاب آغازکرده است دابا لکند و جایگاه استین
1312:۱- ریشه‌یابی باید از پررسی شکل‌های کنونی واژه آغاز شود و تا حد و اجریشه‌ی هند و
1328:چون حرف آغازین ۲ در واژه‌های انگلیسی کهن تبدیل به 13 شده است می‌توان نتیجه گرفت که
7613:چم آغازین این واژه در بیشتر زبان‌های این فهرست؛ قرار دادن» مقرر کردن,
7871:۸ | دخش, دشت (به چم *تکلیف". *شغل* *آغاز کار" "معامله‌ی اول*)
7872:فارسی (/(۳885]4): دخش, دشت (به چم تکلیف", شغل/ "آغاز کار", "معامله‌ی اول)
8248:برخی مستقدند که واژه‌ی "دشت" (یا آدشن") با واژه‌ی "دخش" به چم آغاز و "بتدا" و "تیره و تاریکه" (لغت‌نامه
=== TTS kaz ===
```


## [2026-09-05T20:57:03.094Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\nsed -n '11440,11500p' ARY_latin_index_pages.txt\necho \"=== find pdf page tag ===\"\nawk 'NR<=11500 && /\\[pdf page/ {p=$0; n=NR} END{}' ARY_latin_index_pages.txt\ngrep -n \"\\[pdf page\" ARY_latin_index_pages.txt | awk -F: '$1<11500' | tail -3",
 "description": "ARY goose entry context"
}
```


### [2026-09-05T20:57:04.796Z] TOOL RESULT

```
M928) BSc 9 BUT OLS 22 ls cal oe

WS Gr OS Sar 9 Ad OW 059 cal ee
[pdf page 393]
(COR yah" peadads | TAF
wate lin bi 2 Sls cal ee
o
SPAAK (DUTCH) gale SPHYAS (SANSKRIT) oy Sile
(OLD CHURCH SLAVIC) 55 53%! GREER) Vy
SOND SPHEN, SPATHE, SPHENOS
SOND {OLD IRISH) 29S 643 2! ‘SPONDA LATIN) ops)
(OLD SCANDINAVIAN) oS Sle)
REFERENCES Wcethag ‘SPANN, SPONN
oxo St*C~S~S~S~«é SPAN (OLD HIGH GERMAN) oS glalt
BARNHART: (SPOON) 1050 SPAN (GERMAN) gilt
DELAMARRE: 123 SPON {OLD ENGLISH) oS g-aSi}
10As sbi ob, SPOON ENGLISH) .y=383
SPAK (NORWEGIAN) 15335
senttasl
A Siig 5 2 dls oll =
wl Sas praley iY abs 22 IU ol p=
woe SN Kage GG GUT 9) G20 3a} BBO) 22 5) cal
:
: GAS :(OLD SCANDINAVIAN) 45 Sate! TKO HAVESTAN) glee 1
GOS, GOZ (OLD FRISIAN) WS 532.3 GHAZ ABALUCHD gx sh
3 GANS :(OLD HIGH GERMAN) 7S ial Qaz AFGHANI) (54) gli!
GANS GERMAN) lJ HANSA, HANS. (SANSKRIT) 2 Ste
cos HOLD ENGLISH) pf yalS3\ CHEN, KHEN AGREEK) gly
GOOSE ENGLISH) .godS ANSER LATIN) 3
GAAS (DANISH) Slailo GANSO SPANISH) lily!
GAS (SWEDISH) (558 yo GISCA L(RUMANIAN) gle,
[pdf page 394]
EERE
Y4O 1 (G95) Sis 558
GEISS, GED (OLD IRISH) «5 54, GAAS (NORWEGIAN) (5333
f GwyDD (WELSH) 63) GANZ (DUTCH) gia
| GWAZL XABRETON) ig 2 OLD CHURCH SLAVIC) oS 5 3%\
: OSI, GUSI !
REFERENCES cathy GES POLISH) glen)
POKORNY; =—Ss*C*~<CS~S*~*«SR Gus, GUST RUSSIAN) yy
BARNHART: (GOOSE) 442 HUSA (CZECH) Soy
DELAMARRE: (OIE) 139 GUSKA SERBIAN) gine
BUCK: 17 HUSA (BOHEMIAN) goa y
ONIONS: (GOOSE) 406 Hus (SLOVAK) | gat
RAMAT: 47 ZHASIS LITHUANIAN) ,g\y)
voir seboby ZASS HALATVIAN) (3) 39)
SANSY — (OLD PRUSSIAN) pS p39.
. ietloal
end HN oly SF (gla LED gas) 3 a Obj BY ST y a SF Spel 22 dls cel
GIDZBA SERBIAN) 9 po GYPE (GREEK) gb y
GUZA (SLOVAK) Syst KOFI-(OLD SCANDINAVIAN) 75 5-cL!
GUZAS, GUZYS (LITHUANIAN) gi) (OLD HIGH GERMAN) «pS glsT
GUZA,GUZA (LATVIAN) (3) gi) KUBISI
KOBEN GERMAN) gly ts
‘REFERENCES Wewthay COPA (OLD. ANGLISR iS. hi
POKORNY SSOSC*~*~*~S~« cove TON ENGLISH) 38
BARNHART: (COVE) 228 KOVE HNORWEGIAN) 533,
ONIONS: (COVE) 222 (OLD CHURCH SLAVIC) oS 53%!
SKEAT: (COVE) 140 GYZHA
ray foe Kad GIZHA, GIZA, GUZ (POLISH) gn)
YPAQY. Hasina aac HYZE (CZECH) Se,
=== find pdf page tag ===
11404:[pdf page 392]
11443:[pdf page 393]
11471:[pdf page 394]
```


## [2026-09-05T20:57:20.536Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%BA%D8%A7%D8%B2",
 "prompt": "Give the full Persian section: etymology of غاز (ğâz) 'goose' — what origin does it give (Proto-Iranian? Turkic?), any cognates, and any other Persian senses. Quote the etymology text verbatim."
}
```


## [2026-09-05T20:57:21.681Z] TOOL CALL #32: WebSearch

```json
{
 "query": "Persian غاز goose etymology Turkic qaz Hasandust فرهنگ ریشه‌شناختی"
}
```


### [2026-09-05T20:57:26.101Z] TOOL RESULT

```
# Persian Section: Etymology of غاز (ġâz) 'Goose'

## Origin
The etymology provided indicates a **Turkic origin**, not Proto-Iranian. The text states: "A Turkic borrowing: compare Chagatai غاز (ğaz), Ottoman Turkish قاز (qaz), Azerbaijani qaz. Ultimately from Proto-Turkic *kāŕ."

The word traces back to **Proto-Turkic *kāŕ** ("goose"), making it a loanword in Persian rather than a native Persian term.

## Cognates
Related forms appear in:
- Chagatai: غاز (ğaz)
- Ottoman Turkish: قاز (qaz)
- Azerbaijani: qaz

## Persian Senses
The dictionary lists only one meaning: **goose (bird)**

The Persian entry shows no additional senses beyond this single definition.
```


### [2026-09-05T20:57:30.941Z] TOOL RESULT

```
Web search results for query: "Persian غاز goose etymology Turkic qaz Hasandust فرهنگ ریشه‌شناختی"

Links: [{"title":"غاز - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%BA%D8%A7%D8%B2"},{"title":"قاز - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D9%82%D8%A7%D8%B2"},{"title":"Reconstruction:Proto-Turkic/kāŕ - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Turkic/K%C4%81%C5%95"},{"title":"Kaz of Turkish & Goose of English... | WordReference Forums","url":"https://forum.wordreference.com/threads/kaz-of-turkish-goose-of-english.598946/"},{"title":"кас - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D0%BA%D0%B0%D1%81"},{"title":"How to say goose in Farsi","url":"https://www.wordhippo.com/what-is/the/farsi-word-for-4f7f358cd341d703b4a502b2d0f53db07823b501.html"},{"title":"What is the Persian word for \"Goose\"?","url":"https://languagedrops.com/word/en/english/persian/translate/goose/"},{"title":"Goose in Persian? How to use Goose in Persian. Learn Persian","url":"https://wikilanguages.net/Persian/Goose.html"},{"title":"Annotating Cognates and Etymological Origin in Turkic Languages","url":"https://arxiv.org/pdf/1501.03191"},{"title":"goose in Persian - English-Persian Dictionary | Glosbe","url":"https://glosbe.com/en/fa/goose"}]

Based on the search results, here's what I found about the etymology of Persian غاز (gaaz) for "goose" and its connection to Turkic:

The Persian word غاز is a Turkic borrowing (compare Chagatai غاز, Ottoman Turkish قاز, Azerbaijani qaz), ultimately from Proto-Turkic *kāŕ.

The Proto-Turkic form *kāŕ meaning "goose" has cognates across multiple Turkic languages including Azerbaijani qaz, Bashkir ҡаҙ, Karakhanid قازْ, Kazakh қаз, Kyrgyz каз, Turkmen gāz, Tuvan кас, and Yakut хаас.

It's worth noting that there is an alternative theory that suggests the Proto-Turkic term might have been borrowed from some reflex of Proto-Indo-European *ǵʰh₂éns ("goose"), perhaps Tocharian, though this etymology is debated among scholars.

Regarding Hasandust's etymological dictionary (فرهنگ ریشه‌شناختی), the search results don't contain specific information about that reference, so I cannot provide details about what that source says about this etymology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T20:57:40.857Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0h%E2%82%82%C3%A9ns",
 "prompt": "Give the reconstruction, meaning, and the full list of descendants (Indo-Iranian, Greek, Latin, Germanic), plus any note about Iranian reflexes or Turkic borrowing."
}
```


## [2026-09-05T20:57:42.544Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%AF%DB%8C%D8%B3",
 "prompt": "Give the Persian etymology of گیس (gis) 'hair, tress' verbatim: Middle Persian form, Avestan form, Proto-Iranian/PIE reconstruction, and related گیسو."
}
```


### [2026-09-05T20:57:47.135Z] TOOL RESULT

```
# Proto-Indo-European *ǵʰh₂éns

**Reconstruction:** *ǵʰh₂éns (feminine noun)

**Meaning:** "goose"

**Major Descendants:**

- **Indo-Iranian:** Proto-Indo-Iranian *ȷ́ʰansás (Sanskrit háṃsá-)
- **Greek:** Ancient Greek χήν (khḗn), Modern Greek χήνα (chína)
- **Latin:** ānser (masculine)
- **Germanic:** Proto-Germanic *gans (English "goose," German "Gans," etc.)

**Additional Notes:**

The etymology may derive from imitative origins. Some scholars propose a connection to Proto-Finno-Ugric *joŋkće, noting regular phonetic correspondences. The Turkic similarity to *kāz ("goose") is "likely coincidental or a borrowing from Tocharian." Alternatively, EIEC suggests connection to the root *ǵʰeh₂- ("to yawn, gape"), related to Ancient Greek χάσκω (kháskō).
```


### [2026-09-05T20:57:47.506Z] TOOL RESULT

```
# Persian Etymology of گیس (gis)

**Middle Persian form:** gys (gēs, "curl, locks")

**Avestan cognate:** 𐬔𐬀𐬉𐬯𐬎 (gaēsu, "curls")

**Proto-Indo-Iranian reconstruction:** *káyćas ~ *gáyćas, described as "of unknown source, likely a borrowing from the BMAC substrate"

**Related term:** گیسو (gêsu) is listed as an alternative form and derived term

The entry notes cognates including Sanskrit केश (keśa) and Old Armenian գէս (gēs), with the latter being "an Iranian borrowing."
```


## [2026-09-05T20:57:57.342Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CF%87%CE%B1%CE%AF%CF%84%CE%B7",
 "prompt": "Give the Ancient Greek etymology of χαίτη verbatim: what origin is proposed, does it mention Avestan gaēsa- / Middle Irish gaiset / PIE *ǵʰayt-, and does it mention Beekes' view (Pre-Greek / uncertain)? Also give the meaning."
}
```


## [2026-09-05T20:57:58.293Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/chaeta",
 "prompt": "Give the English etymology of chaeta verbatim: New Latin? from Ancient Greek χαίτη? date of first use, meaning (bristle/seta of an annelid worm)."
}
```


### [2026-09-05T20:58:01.491Z] TOOL RESULT

```
# Ancient Greek Etymology of χαίτη

**Etymology Source:**
According to Beekes, the word derives from Proto-Indo-European *gʰeh₂it- ("curly hair"), with cognates in Avestan gaēsa ("curly hair") and Middle Irish gaiset ("bristly hair").

**Meaning:**
The primary sense is "loose, flowing hair," particularly of back hair. Secondary meanings include a horse's or lion's mane, a helmet's crest, and figuratively, tree foliage.
```


### [2026-09-05T20:58:03.432Z] TOOL RESULT

```
# English Etymology of Chaeta

**Origin:** From Ancient Greek χαίτη (khaítē)

**Meaning:** The word derives from Ancient Greek meaning "crest, mane, flowing hair, foliage."

**Scientific Definition:** In English, chaeta refers to "a chitinous bristle of an annelid worm" or such a bristle found on arthropods. The term is also used synonymously with "seta."

**Date of First Use:** The document does not specify when this term first entered English usage.

**Note:** The Wiktionary entry shows the term is used in modern scientific and biological contexts but does not provide historical documentation of its initial adoption into English.
```


## [2026-09-05T20:58:25.683Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN goose ===\"; grep -n -i \"3\\.55\\|GOOSE\" SYN.txt | head -20\necho \"=== LAT anser ===\"; grep -n -i \"^anser\\|anser,\" LAT.txt LEW_1910.txt | head -20\necho \"=== LKT kaz ===\"; grep -n -i \"kaz\\b\\|qaz\\b\" LKT.txt | head -20\necho \"=== TTS qaz ===\"; grep -n -i \"kaz \" incoming/TTS/TTS_vambery1878_uoft_djvu.txt | head -20",
 "description": "Grep Buck, Latin dicts, Lokotsch, Vambery"
}
```


### [2026-09-05T20:58:25.803Z] TOOL RESULT

```
=== SYN goose ===
3744:CHAPTER 3 ANIMALS 3.45 Foau, Cott gal eANo 3.46 Ass, DonKEY 3.12 Mate (adj.) 3.47 Mute gia ene 3.51 Hen, Catcxen (Generic) Blan CASTE 3.52 Cock Blo ESTO 3.53 CAPON 3.16 PasTuRE (vb.) aa ee ON chaaeh Pe, 3.55 CHICKEN 3.18 HerDSMAN aA Goan 3.19 STABLE, STALL ne Duue 3.20 CATTLE (Bovine Species) et at ae se 3.612 Purry a oe 3.62 Car 3 4 CALF 3.63 Mouse eed tae AM ; eS a 3.66 FISHERMAN 3.28 Ews 3.71 Wo.ur | 3.29 Lams 3.72 Lion 3.31 Swint 3.73 BEAR 3.32 Boar 3.74 Fox | 3.33 Barrow 3.75 DEER i 3.34 Sow 8.76 MonxkEY 3.35 Pie 3.77 ELEPHANT 3.36 Goat 3.78 CAMEL | 3.37 Hu-coar 3.79 Hunt (vb.) 3.38 Kip 3.81 InsEctT 3.41 Horse (Generic) 3.82 BEE 3.42 Srantion 3.83 Fy : 3.43 GrLpine 3.84 Worm 344 Mare 3.85 SNAKE
3774:The young of an animal may be a ‘calf’ (NE calf, etc., 3.24), ‘chicken’ (Lat. pullus, 3.55), or ‘foal’ (Grk. w&dos, Lat. pullus, NE foal, etc., 3.45). Similarly, a ‘yearling’ may be a ‘calf’ (Lat. vitulus, 3.24), a ‘lamb’, ‘wether’, ‘ram’ (Goth. wiprus, etc., 3.27, 3.29), ‘sow’ (Br. gwiz, 3.34), ‘goat’ (Grk. xivapos, 3.36), or ‘kid’ (SCr. jare, 3.38).
4677:174 SELECTED INDO-EUROPEAN SYNONYMS 3.51 3.52 3.53 3.54 3.55 HEN, CHICKEN COCK CAPON HEN CHICKEN (Generic) Grk. — ddexropls, adextpuwy, 6 dpyis adexropls, 4 éprlOtov, veoocloy épyis opus
4709:3.51-3.55. These are most conven- iently discussed together. The words entered as generic are mostly those for the much more numerous female, the ‘hen’, in a few cases those for the young, the ‘chicken’, Thus NE hen and chicken are both used generically, with varying local usage (in New England one used to keep hens, but now generally in U.S., chickens, chicken farm). Only occasion- ally is there a distinctively generic word, as NHG huhn, in common use. Some of the words listed under ‘chicken’ are used mainly of the very young ‘chick’,
4782:gar term), 3.56 GOOSE p Goth Lith.  Zqsis
4784:i Sw. gas SCr.  guska tf oca ie oie ON gos Boh. husa Sp. gausa, oca ME goos Pol. ges Rum. giscd NE goose Russ. gus’ Ir. ged, giugrann Du. gans Skt.  hansa- NIr. gé OHG gazs Ay. z W. guwydd MHG gans Br. gwaz NHG gans
4785:1, If *§hans-, prob. fr. the root seen in Grk. xéoxw, éxavov ‘yawn, gape’, with reference to the goose’s characteristic Squawk with wide open bill. Walde-P. 1.536. Ernout-M. 56. Walde-H. 1.52. Berneker 342,
4789:tion to ‘goose’, parallel with that of Grk’ bpuis ‘bird’ to ‘hen’ (8.51). Walde-H. 1.79. REW 826.
4802:Sp. pato, pata, like SCr. patka ‘duck’, Alb. paté ‘goose’, NPers. bat ‘duck’, etc., all of imitative orig. (calling cry?). REW 6301. G. Meyer, Alb. Etym. Wtb. 324. Rohlfs, Z. frz. Spr. 49.108 f.
9591:Although there is a word for ‘berry’ in most of the Eur. languages, it is only in the Gmc. group that the word fuishes a long series of cpds. denoting the special kinds of berry. Thus NE ber- Ty, whence strawberry, raspberry, black- berry, blueberry, cranberra , gooseberry, éle,, formerly also wineberry (OE wein- berige, like Goth. weinabasi), now re- placed by grape, Similarly, NHG beere mith erdbeere, himbeere, etc., and in fie other Gme, languages. Elsewhere the
22299:Lett. rietums, esp. pl. rietumi, fr. riets ‘sunset’ : riest Toll, fall’. Muhl.- Endz. 3.550.
25823:5. Lith. ruduo, Lett. rudens, fr. Lith. rudas, Lett. ruds ‘reddish, red-brown’ (with reference to leaves, etc.). Miuihl.- Endz. 3.554.
26777:SCr.-ChSl. modri ‘livid, bloodshoy SCr. modar, Boh. modry ‘blue’, Pol modry esp. ‘dark-blue’, perh, ; Teall madra ‘madder, goose grass’, OHG ma- tara, OK medere, maddre ‘dyer’s madder (rubia tinctorum)’, Walde-P, 2.305, Berneker 2.66 f.
=== LAT anser ===
LAT.txt:4015:anser
LAT.txt:4060:anser, -eris (doublet ansar,-aris, blame par l'app.Probi) m.(fem.
LAT.txt:6174:bassevcour, substitut de (h)anser, atteste dans Avien (lV e -V e s.) et
LAT.txt:6800:ballo, -as, -are: danser, baller. Premier ex. dans S^“Aug. - Pan¬
=== LKT kaz ===
1030:[Kazäntat.;  osm.  capak  aus  pers.  cäpag] 'flacher  Fisch,  Plötze  Leuciscus  rulilus L.';  hieraus  russ.  cebak  'Barbe,  Brachsen Abramis  brama  L.'    [Gorjajew  409.
2689:1143.  Tk.  kazak: 'Landstreicher,  Vagabund,  Nomade'  [in diesem  Sinne  veraltet,  vom  Stamme  kaz 'umherirren'  Vambery  TktEtWb  S.  22, Nr.  23 ;  jetzt  nur  noch  in  weicher  Form gezmek  'spazieren  gehen'] ;  hieraus  russ. kazak,  kozak,  bulg.  kazak,  poln.  kosak, dtsch.  Kosak,  Bezeichnung  für  die  süd- russischen Steppen-  und  Reitervölker; engl,  cossack,  angloind.  mit  der  Bedeu- tung 'Freibeuter,  plündernder  Reiter', rum.  cazac  'Kosak',  cazachiu  'russ. Weinhändler,  Kosakenmütze'.  Hieraus auch  die  Kleidernamen:  russ.  kazakin 'Art  Halbrock',  öech.  hazuka  'Mönchs- kutte, Oberkleid,  Decke',  poln.  hazuka 'Frauengewand';  mhd. kasugele,  kusuckel 'Mefjgewand',  kasacke  'kurzer  Reiserock', nhd.  Ä'rtsacfcCjacke  in  der  Damenmode), engl,  cassock  'langer  Priesterrock,  Sou- tane'; nlat.  cazaca,  it.  casacca,  hz.casa- qne,  sp.  pg.  casaca  'lange  Überjacke'. [Gorjajew  127.  Bern  SlEtWb  377  und 496.    Hobson-Jobson  262.
3279:1423.  Ar.  markaz: 'Mittelpunkt',  ebenso  tk.  merkez;  hieraus lum.  merchez  'Schliche,  schwache  Seite' [nach  Löbel  E1TAP63  auch 'Mittelpunkt'].
5381:markaz  1 423
=== TTS qaz ===
2231:Wolf,  ata  kaz  =  Gänserich) ;  atag  =  Stellvertreter  des  Va-
```


## [2026-09-05T20:58:34.607Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '4780,4800p' SYN.txt\necho \"=== TTS Gans ===\"; grep -n -i \"Gänse\\|Gans\\b\\|Gansenrich\\|Gänserich\" incoming/TTS/TTS_vambery1878_uoft_djvu.txt | head -20",
 "description": "Buck goose entry and Vambery Gans"
}
```


### [2026-09-05T20:58:34.675Z] TOOL RESULT

```
Av. parodar§ ‘cock’ (ceremonial term), epd. of paré ‘in front, before’ and daras- ‘see’, hence lit. ‘seeing ahead’, that is, announcing the day. Barth. 859. On the pair parddar§ and kahrkatds, cf. Benveniste, Studia Indo-Iranica, Ehren- gabe fiir W. Geiger, 219 ff.
Av. karatodqsug ‘cock’, cpd. of karata- ‘knife’ and adj. *dqsu-: Skt. darig- ‘bite’, hence lit. ‘biting with knives’ with reference to the spurs. Barth. 454.
gar term), 3.56 GOOSE p Goth Lith.  Zqsis
Ge oe ON gas Lett. zass NG xiv Lat.  dnser Dan. gaas a *gast, gust
i Sw. gas SCr.  guska tf oca ie oie ON gos Boh. husa Sp. gausa, oca ME goos Pol. ges Rum. giscd NE goose Russ. gus’ Ir. ged, giugrann Du. gans Skt.  hansa- NIr. gé OHG gazs Ay. z W. guwydd MHG gans Br. gwaz NHG gans
1, If *§hans-, prob. fr. the root seen in Grk. xéoxw, éxavov ‘yawn, gape’, with reference to the goose’s characteristic Squawk with wide open bill. Walde-P. 1.536. Ernout-M. 56. Walde-H. 1.52. Berneker 342,
. Grk. xiv, Dor. xév; Lat. anser (for hanser) ; (Ir. géis ‘swan’) ; ON gas, OF ie OHG gans, etc., general Gmc. ; Lith. ass, ChSl. *gqsi, (gust), ete., general
Palto-Slavie (Slavic g fr. Gme.?); Skt Lansa- (also ‘swan’, etc.). :
Fr. ove, fr. late Lat. Bee on tion fr. avicula, aucu- as “bird’, with Specializa-
tion to ‘goose’, parallel with that of Grk’ bpuis ‘bird’ to ‘hen’ (8.51). Walde-H. 1.79. REW 826.
Sp. gansa (with ganso ‘gander’), fr. Goth. *gans = OHG gans, etc.
Rum. giscd, fr. Slavic (late ChSI. gqsika, SCr. guska, dim. of gasi, above, iby.
3. Ir. géd, NIr. gé, W. gwydd, Br. gwaz, fr. *gegda- or the like: Lith. gagéti ‘quack’, MHG gagen ‘quack’, etc., all of imitative orig. Walde-P. 1.526.
Tr. giugrann, likewise of imitative orig., either with the preceding or with Lat. gingrire ‘quack’, etc. Walde-P. 1.526, 592.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
178 SELECTED INDO-EUROPEAN SYNONYMS 3.57 DUCK
jooa Goth . Lith. anltis NG Lae ON ond Lett. pile Lat. anas Dan. and ChSl. aly It. anatra Sw. and SCr.  patka, raca, utva Fy. canard OE ened (duce) Boh.  kachna Sp. anade, pato ME _ ducke, (h)ende Pol. kaczka Rum. ra/d NE duck Russ. utka Ir. lacha Du. eend Skt. NIr. _lacha OHG anut Ay. W. hwyad MHG ant Br. houad NHG ente
1. ITE *anati-, *gti-. Walde-P. 1.60. Ernout-M. 48. Walde-H. 1.44. REW 439.
Grk. vijcca (Att. vijzza, Boeot. vaca); Lat. anas, gen. (anitis and) anatis (> It. anatra, Sp. anade, OF r. ane); ON ond, OE ened, OHG anut, etc., general Gmce.; Lith. antis; ChSl. aty, SCr. utva, Russ. utka; (Skt. att- a kind of water bird).
2. NG warmea, imitative like It. papero ‘gosling’, Sp. parpar ‘quack’.
=== TTS Gans ===
2231:Wolf,  ata  kaz  =  Gänserich) ;  atag  =  Stellvertreter  des  Va-
```


## [2026-09-05T20:58:44.803Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\necho \"=== WLD Bd1 ghait/gaesa ===\"; grep -n -i \"gaesa\\|gaēsa\\|ga^sa\\|xaiTn\\|ghait\" WLD_Bd1_1930_dli_70244_djvu.txt | head -20\necho \"=== WLD Bd1 ghans ===\"; grep -n -i \"ghans\\|hamsas\\|anser\" WLD_Bd1_1930_dli_70244_djvu.txt | head -20",
 "description": "Grep Walde-Pokorny vol 1"
}
```


### [2026-09-05T20:58:44.866Z] TOOL RESULT

```
=== WLD Bd1 ghait/gaesa ===
33131:ghait-a, -es ghaido-, ghaiclo- 
33150:ghait-a, -es- „krauses oder gewelltes Haar“. 
33155:Yon *ghait-{e]s- aus av. gaesa- m. „Kraushaar, Lockenhaar", npers. ges 
33159:nir. gaoisead t aus *ghait-s- ) ,.crinis c . 
33182:gr. yang, s. u. ghaitd-. 
33244:Wurfspie6“ ( gaesatl ,.gall. Soldtruppen"), air. gae „Speer“ {guide „pilatus“\ 
=== WLD Bd1 ghans ===
3648:ferendi", an-clersafust „circumdederit“, anseriatu „observato“, s. zu letzterem 
33083:*ghans- „Gans“) und einer ahnlichen Lautvorstellung entsprungen, wie 
33098:gagnoti „schnattcrn“, gagonas „Ganserich“ (etwas ahnlich gegl „Kuckuck“) ; 
33122:109, zum d-Formans vgl. ags. ganot u. *ghans- „Gans“). 
33712:ghans- 
33715:ghans- und verwandte Bildungen fur „Gans“. 
33719:lat. anser „Gans“ (ursprgl. *hanser , s. Yf. LEWb. 2 s. v. ; die Stammbildung 
33727:s. die Lit. bei Yf. LEWb. 2 u. anser, Berneker 342, Yasmer ZslPh. 2, 54 ff., 
33732:Ags. gan(d)ra „Ganserich“ (engl. gander), mnd. ganre ds. (neuere Formen 
33734:von ahd. kat-uro (Suolahti); wenn ein *ganezan- (vgl. oben zu lat. anser) 
34487:, .gahnen, klaffen"; schallmalend fur den Gahnlaut (s. auch u. ghans- 
34899:aus ghans-) durch Gutt. wiedergegeben sein soil. Vgl. aber oben S. 536!
```


## [2026-09-05T20:58:53.345Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%BA%D8%A7%D8%B2' --note 'page 179, root Ghans, Persian ghaz node: Wiktionary derives Persian غاز from Turkic (Proto-Turkic *kāŕ), not from PIE' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0h%E2%82%82%C3%A9ns' --note 'page 179, root Ghans: PIE *ǵʰh₂éns goose, descendants Skt hamsa, Gk khen, Lat anser, PGmc *gans; Turkic likeness coincidental/Tocharian loan' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%DA%AF%DB%8C%D8%B3' --note 'page 179, root Ghait, node 2: Persian گیس from MP gys, Av gaesu; PII *káyćas/*gáyćas possibly BMAC substrate' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%CF%87%CE%B1%CE%AF%CF%84%CE%B7' --note 'page 179, root Ghait, node 3: Greek khaite from PIE *gʰeh₂it- (Beekes), cognate Av gaesa-, MIr gaiset' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/chaeta' --note 'page 179, root Ghait, node 4: English chaeta from Ancient Greek khaite' 2>&1 | tail -3",
 "description": "Archive web sources"
}
```


### [2026-09-05T20:58:56.898Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/9e67530d43b125a6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4d8a144f67772cd6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5c9f0da879b68c56.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/151cee84972cde16.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/99c3a96dca0b92bb.txt
```


## [2026-09-05T20:59:02.912Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\nsed -n '33712,33745p' WLD_Bd1_1930_dli_70244_djvu.txt\necho \"=== ghait section ===\"; sed -n '33148,33185p' WLD_Bd1_1930_dli_70244_djvu.txt",
 "description": "Print WLD ghans and ghait sections"
}
```


### [2026-09-05T20:59:02.976Z] TOOL RESULT

```
ghans- 


ghans- und verwandte Bildungen fur „Gans“. 

Ai. liamsd-h m., lict nisi f. „Gans, Schwan“; gr. yjjv, -os, dor. boot, ydv j.Gans 1 ' 
(hier, wie im Germ, und im lit. gen. pi. zqsti noch die alte kons. Flexion); 
lat. anser „Gans“ (ursprgl. *hanser , s. Yf. LEWb. 2 s. v. ; die Stammbildung 
vermutlicli nach Bgm. II 2 1, 526 A. 1 durch Yerquicknng yon *hans- mit 
einer suffixal hochstufigen Form *hanes -); air. geiss „Schwan“ (*gnnsi~, 
oder eher *<jansJ = ai. hauist, nicht aus einem kons. Stamm umgebildet); 
ahd. gans (i- St. ge worden), ags. gds (PI. ges aus *gans-is = gr. y/jveg), aisl. 
gas (PI. gas) „Gans“ (aus ags. gUs stammt mir. goss ); lit. sas'is „Gans“ (acc. 
zqs[ = gr. yfjva, g. pi. kons. znsn_ , dial, auch n. pi. zTises ), lett. zhoss, pr. 
sansy ds.; slav. *gqsb (zum wohl auf Entlehnung beruhenden g statt 3 
s. die Lit. bei Yf. LEWb. 2 u. anser, Berneker 342, Yasmer ZslPh. 2, 54 ff., 
Trautmann Bsl. Wb. 365) in russ. gins, slov. gos, poln. ges „Gans“. Z. B. 
Curtius 5 200, Schrader Sprvgl. 3 II 165, Rl. 2 339 f. (iiber arm. ags „Gans“ 
— Lit. bei Berneker aaO. — s. u. kau- Schallwort). 

Ags. gan(d)ra „Ganserich“ (engl. gander), mnd. ganre ds. (neuere Formen 
s. bei Suolahti Vogeln. 413) gilt als Mask.-Bildung vom St. *gan- nach Art 
von ahd. kat-uro (Suolahti); wenn ein *ganezan- (vgl. oben zu lat. anser) 
zugrunde liige, stiinde schweiz. gann, gunner „Bezeichnung von Taucher- 
arten“ (Suolahti) als *ganed- damit in Suffixablaut. 

Daneben eine sicher vom kiirzern St. glnan- (wozu ghan-\e]s- wie idg. 
*inen-ot : *men-[c]s- „Monat“) ausgegangene Bildung mit -d- : germ, (zuerst 
bei Plin., weitere Belege bei Suolahti 410 If.) ganta „eine Art Gans“ (dar- 
aus prov. ganta „wilde Gans, Storch u ; die Bed. „Storch“ zeigt auch 
lit. gandras, pr. gandarus, aus germ. *gan[d]ro oder zu slav. gqdot), 
ags. gemot „ein wilder Wasservogel, z. B. fulix“, ahd. gana^o „Giinse- 
rich“, auch ganso , mnd. gantc ds. (Eine Ableitung davon mit iihnlicher 
Bed. wie tirol. giinsen „kokettieren“, gdnsern „wie eine Gans tun“, auch 
=== ghait section ===
anderer Bedeutungsfarbe ganzlich unbewiesen. 

ghait-a, -es- „krauses oder gewelltes Haar“. 

Gr. yang „Lockenhaar, frei herabwallendes Haar ; Mahne (von Pferden. 
Lowen) ; Baumbart“. 

Yon *ghait-{e]s- aus av. gaesa- m. „Kraushaar, Lockenhaar", npers. ges 
„herabhangende Haare, Locken“, av. gaVsu- ,,kraushaarig, lockenhaarig; 
(beim Kamel:) zottelhaarig“; 

nir. gaoisead t aus *ghait-s- ) ,.crinis c . 

Liden IF. 19, 318 f. und Charpentier KZ. 40, 272 f., beide mit Kritik 
abweichender Versuche. 

gliaido- oder ghaido* „Ziegenbock, Ziege“. 

Lat. haedus „Bockchen, junger Ziegenbock“ (dazu die, dialektischen und 
vulgaren Formen hedus, edus, faedns, f edits s. Ernout El. dial. lat. 154f.); 

got. gaits und ahd. geiz fi , aisl. geit f„ aschw. get , gcet f., ags. gat f., 
as. get f. (konsonant. Stamme) „Ziege“. 

Yon ghaido- abgeleitet *ghaideinos : lat. haedinus „von jungen B6eken“. 
ags. gcet'U, ahd. geizin „caprinus“, got. gaitein n. „Bocklein“, ahd. geizin 
n. „Bock“. (Zur Bildung vgl. sivein und Kluge, Nom. Stammb. § 57, 5S a .) 

Ob die Ziege als „die springende“' (Prellwitz s. v. yaha ) zu ai. jihlte 
„springt auf, setzt sich in Bewegung, lauft“, hdyah „RoB“, arm. ji ds.. aksl. 
zajecb „Hase“ (Zupitza Gutt. 200) oder naeh FickI 4 433 zu lit. zaidziu 
„ich spiele“ gehort, ist fraglich. Ygl. Yerf. LEWb.' 2 359 (die Yerwandt- 
schaft des lit. und ind. Wortes ebenfalls zweifelhaft). Abzulehnen mit 
Liden IF. 19, 319 fF., Charpentier KZ. 40, 472 die Zusammenstellung mit 
gr. yang, s. u. ghaitd-. 

Ahd. ziga, wozu ags. ticccn und ahd. siclil mit hypokoristischer Konso- 
nantendehnung (s. Kretschmer Glotta 14, 321, ist nicht mit Kluge in alteren
```


## [2026-09-05T20:59:09.157Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://www.nisanyansozluk.com/kelime/kaz",
 "prompt": "Give Nişanyan's entry for Turkish kaz 'goose': Old Turkic form, earliest attestation (Divan-ı Lugati't-Türk?), Proto-Turkic reconstruction, and whether he notes any Indo-European connection."
}
```


## [2026-09-05T20:59:10.694Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/goose",
 "prompt": "Give the etymology of goose, and any mention of gander and gannet: Old English gos, PIE *ghans-, Sanskrit hamsah, Greek khen, Latin anser."
}
```


### [2026-09-05T20:59:13.570Z] TOOL RESULT

```
I appreciate your question, but I cannot provide the information you're requesting. The web page content you've shared only shows the header, navigation, and footer of the Nişanyan Sözlük website—it does not contain the actual dictionary entry for "kaz" (goose).

To find Nişanyan's etymological analysis of Turkish "kaz," including details about Old Turkic forms, Proto-Turkic reconstructions, and any Indo-European connections he may note, you would need to visit the dictionary directly and search for that entry.
```


### [2026-09-05T20:59:15.846Z] TOOL RESULT

```
# Etymology of Goose and Related Words

## Goose
The word "goose" traces back to Old English *gos*, derived from Proto-Germanic *gans-. This ultimately connects to the Proto-Indo-European root *ghans-, which scholars believe is "probably imitative of its honking." The word appears across Indo-European languages with similar forms.

## Related Terms

**Gander** (male goose) comes from Old English *gandra*, also stemming from Proto-Germanic *gan(d)ron and the same PIE *ghans- root as goose.

**Gannet** (a seabird) is listed among words etymologically linked to goose but receives no detailed entry in this source.

## Cross-Linguistic Parallels
The PIE root *ghans- connects to cognates including Sanskrit *hamsah* (masculine) and *hansi* (feminine), Greek *khēn*, and Latin *anser*—demonstrating the word's deep ancient ancestry across multiple language families.
```


## [2026-09-05T20:59:36.097Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT context ===\"; sed -n '9748,9770p' BRT.txt\necho \"=== BRT gaesav ===\"; grep -n \"gaesav-\\|gaesav\" BRT.txt | head\necho \"=== HUB context ===\"; sed -n '7538,7548p' HUB.txt\necho \"=== SOD zgh ===\"; grep -n -i \"goose\\|غاز\" SOD.txt SOD_pages.txt | head -10",
 "description": "Bartholomae, Hübschmann, Gharib checks"
}
```


### [2026-09-05T20:59:36.197Z] TOOL RESULT

```
=== BRT context ===
bKüüh,bkiivMiitih,bkülasamr'ddlUh.samrddm:\^^"J-  "   \  tiyanqm).
s.    noch    No.  2-11.    -     ')Pt4,KS,j3;  Ablejt.  ausf^Si-,  -  Pü.i  ;,^Äa.  Sü. ; /;-/Ai.i^
5*5*13.- a)Pii.;  s'^än3n,a\.:gäspandiS!L:\  '^'i'  '/•alciiya^.   —    ■)  So  KA.  überall  ausser
jätakäh,    erl.!  (aiuifadayütMw ;    a.  No.  6.  —  *'■  -fS-  ^2;  »•  »ber  Var,  — ')  Im  Gegcns.  m
3)  Pa.:ir^'«J«.  -  *)  Vä.:sfhänän.-i)  Vgl.  I  ""^J"^"--   —    i>  Wo  die  üalavö  gai%ya  im
Y.  ^.  12:   gai%S  frädö   mit   J<.   14:  /rWö  1  Einielnen    verieichnet    werden.    —    li    NA.
virxänä.  —  6)  Pü.:  fWJ«,    erl.:  gSspand;   s.  •^yäi^a■,  s.  aber  Y.  //.  $.
S""  '■  r  1  «;'  '*■-w^  "■■■  -f^"«  '  ,'■  •  j-  gaevanay-  m.  EN.  eines  Gläubigen: No.  10  f.  —  *)  Hds.  ti-iiaufci;  s.  unten  No.  I4. '      '    "*.  v       ,  ,         v  ,..
—  9)  PQ.J  «:*,ShJh.  —  ">)  Va.:  gihän,  „\  ■.\°'"''"'^'  '^•'""•"""""^^  '^^^<""'  ^^-  '3-  '^'^S- a»Jrfa*(Sa.:  ijifM«).  -  ")  Pd.:  baArig!k5H,\  ™.  Komp.:  'j"«'  (""r  KompA.,  sii.  ßra-; eri.!  ^lf/*i  <>»».  —  ")  Far^ai^V".  mit  Ge-  [  s.'.M''saf)+'^a>,q)>-  (lum  V,  -i/a«-;  ai.  i^«oj~ ichleAtswechsel,  S  4/f  -  -J)  Die  Bed.  von        *■).  "£■  ^'^  Verlangen  lebhaft  ist'.
i'^ili  (Sp'^iä\nt'^a^tZt-  ^)i!Vo°lry  P"^-  •"■  '^""^■'  Lockenhaar':  sa and  ^'Jij-  No.  2.   Die  Wörter  werden   öfters  ,  F. .?  b.
verwechselt.  KompK.  —  Vgl.  gaesav-.  —  np.  g^l  'Locken';
s.  daiu  Hbm.  AGr.  /.  127.    —   Pü.    sagt,  so
•  j.  gae*o.j8'tara-    Adj.    'der   für  Haus      heisse  das  Haar  '/a  2  »  j  är.uiai:
und    Hof   (mörderischere,    d.  L)    gefähr-         .         _  -<.„.,.„.
lichere':  -(«r»..!,  v.ia  ..ya  »M.  V. ;  *  J;  «"^f  "j  g«e»«v-»  Ad,  kraus'; i)  liraus-,  lockenhaarig  T  (JöJ/iiftf  (sd.)  ^«rt kompar.  aus  ♦V"-.  ''"s  -I™»  KS.  ->  ge- ,  ■  "  "■'''^"  ^-  7-  59(?).  a)  bes.  von  K^ri-
bildet'), —  Pü.:  gihän  iaiSriar,  erl,  1  ■vai  him-\säspa:  kinsäspasca  ..yava  'su^ gaöavarS tat  'bösarliner'. —  ')  Die  Stelle  ist  nicht  viel  Y.p.  lo;  —  kinsSspake  *'i^äu/''  gaZa- """'•  '  varahe  Yt.ij.6i,  136.  2)  'zottelhaarig',
•  j.  gaeÖ'ö.frääana- Adj.  (fem.  "Hir-) 'Haus  vom  Kamel:  usfrahe  ..  =^aa/  maSy!.- und    Hof  fördernd,    mehrend':    ar>dvm  vanhahe  (%A.)  \\.  i4- ^i-
sBram  .  .  'nam  Y.  6'5.  1.  '  Vgl.  galm-.  —    Die  richli^je  Bed.  zuerst  bei
Pü.!   gihän yrö^imlär;    Npü.:   cüsfa»J  a/zi- ■  ^^f^^''  ZDMG.  ig.  588;  vgl.  Essays»   178.   S.
vandZ  .       1-        i    y  y       ,  ^^^^   voNSTACKELbERG  WZKM,  /i.  246  No.
"^  _  1  Falsches   bei   Ggr.  SBayrAW.  1SS4.  364.  -
•  j.  gaed'o.mvr^ndyäna-  patr.  Adj.  'von  ,  pn.:  gitwar,  (lu  V.):  ges,  Npü.  (tu  Yi.):  dar 'cya  abstammend' :  paitUt3tie  . .  aratöisca  •"  r^'i')-  —  ')  S  ^^2  No.  2.  —  >>  So,  mit  S, 'noÄe  Yt  J^.  137.                                             ^  "  ^^-  '"''  *"'^-'°-
Ablcit.  aub  *'mjr>nrya;  vermuilich  Name  eines  |         j.  gao',  KompA.  (vor  Kons.):  s.  sgav-. ßana;  lEt.  s.  SiB,  3.  '       -  n  xt  ■  t-
=== BRT gaesav ===
9758:verwechselt.  KompK.  —  Vgl.  gaesav-.  —  np.  g^l  'Locken';
=== HUB context ===
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
=== SOD zgh ===
SOD.txt:69431:goose 
SOD.txt:90075:goose    9113 
SOD_pages.txt:30023:      goose352 n p39; ob. sychy, SCE 130
SOD_pages.txt:38392:giant   4998, 5072, 8700                                                       goose   9113
```


## [2026-09-05T20:59:44.517Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '30018,30028p' SOD_pages.txt\necho \"---\"\ngrep -n \"^9113\\|9113 \" SOD_pages.txt | head -5",
 "description": "Gharib Sogdian goose entry"
}
```


### [2026-09-05T20:59:44.585Z] TOOL RESULT

```
        1974, 581; AoFiii 253.7, 254.11 n 148                        9125 symtyh B                                          ^>jua
9113 sych      B                                               >          simtya, ssmatya ^sir^ytyh
                                                                          consolation
      sic(a) ? ®<*sika <*siyaka        ©f. n.; ob. -yh
                                                                           VJ 387
      goose352 n p39; ob. sychy, SCE 130
      SCE                                                            9126 symwn      C                               o^^^oy^
                                                                           simon
9114 sycy      C =* syc>kk
                                                                           Simon
9115 syd- C                                           jjl.7>*
---
30019:9113 sych      B                                               >          simtya, ssmatya ^sir^ytyh
```


## [2026-09-05T20:59:53.103Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'chaeto-' in p:\n        print('leaf',i,'-> printed pp ~',(i-12)*2,(i-12)*2+1)\nEOF",
 "description": "Locate Klein chaeto- leaf"
}
```


### [2026-09-05T20:59:54.870Z] TOOL RESULT

```
leaf 19 -> printed pp ~ 14 15
leaf 142 -> printed pp ~ 260 261
leaf 150 -> printed pp ~ 276 277
leaf 175 -> printed pp ~ 326 327
leaf 646 -> printed pp ~ 1268 1269
leaf 791 -> printed pp ~ 1558 1559
```


## [2026-09-05T21:00:02.406Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nupto='\\n'.join(lines[:7105])\nprint('leaf of line 7105 =', upto.count('\\f'))\n# also goose\nfor i,l in enumerate(lines):\n    if l.startswith('goose,  n.') or 'goose,  n.  —  ME.  gos' in l:\n        print('goose line', i, 'leaf', '\\n'.join(lines[:i]).count('\\f'))\nEOF",
 "description": "Klein leaf numbers"
}
```


### [2026-09-05T21:00:04.405Z] TOOL RESULT

```
leaf of line 7105 = 150
goose line 16446 leaf 361
```


## [2026-09-05T21:00:14.113Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (142,148,149,150,151):\n    p=pages[i]\n    nums=re.findall(r'\\b(2[0-9]{2})\\b', p[:200]+p[-200:])\n    print(i, nums, '|', p[:90].replace('\\n',' '))\nEOF",
 "description": "Calibrate Klein leaf-to-page"
}
```


### [2026-09-05T21:00:15.737Z] TOOL RESULT

```
142 [] | - i I * T -r m m Derivatives:  catamit-ed,  catamit-ing,  adjs. catamountain,  eat-a-mount
148 ['284'] | erived  from a  language  of  Asia  Minor  and  not  cognate  with L.  cremdre,  ‘to  burn
149 [] |  adj.,  pertaining  to  modeling  in  wax. —  Gk.  xTiponkaoTixi?,  ‘pertaining  to  moldi
150 [] | ��one who  speaks  (in  a  certain  manner) ;  one  who  deals (with  a  certain  topic)’.
151 ['266', '267'] | d  cypress’,  fr. Chamaedaphne chap 266 267 chamae-  and  xurcaptaaoi;,  ‘cypress’.  See
```


## [2026-09-05T21:00:40.154Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '35948,35960p' POK_full.txt\necho \"=== IEC page markers around 173-186 ===\"\npython3 - <<'EOF'\nimport re\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(170,190):\n    nums=re.findall(r'(?:^|\\s)(\\d{3})(?:\\s|$)', pages[i])\n    print(i, [n for n in nums if 280<=int(n)<=340])\nEOF",
 "description": "Pokorny ghans page and IEC page markers"
}
```


### [2026-09-05T21:00:41.905Z] TOOL RESULT

```
base from Wasservogelnamen) see below gha gha-. 

References: WP. I 536, WH. I 52, 583, Trautmann 365 f., Specht Dekl. 47, 204. 
Page(s):412 



Root / lemma: ghan- 

Meaning: to yawn 

Material: Gr. horn, sxavov Aor. (actually Imperf. to *xa-vc(-pi, *xa-vu)), Ksxnva Perf. (Doric 

=== IEC page markers around 173-186 ===
170 ['286', '287']
171 ['288', '289']
172 ['290']
173 ['291', '292']
174 ['293', '294']
175 ['296']
176 ['297', '298']
177 ['299', '300']
178 ['301']
179 ['302', '303']
180 ['304', '305']
181 ['306', '307']
182 ['308', '309', '310']
183 ['311']
184 ['312']
185 ['314', '315', '335']
186 ['316', '317']
187 ['318', '319']
188 ['320']
189 ['321', '322']
```


## [2026-09-05T21:01:10.141Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/goose' --note 'page 179, root Ghans, Germanic/English nodes: OE gos < PGmc *gans- < PIE *ghans-, cognates Skt hamsah, Gk khen, Lat anser' 2>&1 | tail -2\nmkdir -p data/verification/sources/refs/ocr/BOOK\ncp \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg179.png\" data/verification/sources/refs/ocr/BOOK/179.png\nls -la data/verification/sources/refs/ocr/BOOK/179.png",
 "description": "Archive etymonline and copy page image"
}
```


### [2026-09-05T21:01:12.338Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/6c1a7370028b094a.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 57139 Sep  5 17:01 data/verification/sources/refs/ocr/BOOK/179.png
```


## [2026-09-05T21:01:15.205Z] TOOL CALL #51: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-05T21:01:15.244Z] TOOL RESULT

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


## [2026-09-05T21:06:57.375Z] TOOL CALL #52: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-179.json",
 "content": "{\n  \"pdf_page\": 179,\n  \"book_page\": 149,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Ghait, Ghaita\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *gʰeh₂it- / Pokorny *ghait-a, -es- 'curly or wavy hair'\",\n      \"note\": \"Pokorny IEW 410 has exactly this lemma: 'Root / lemma: ghait-a, -es- | Meaning: curly or wavy hair', with Av. gaēsa-, NPers. ges, Gk. χαίτη and MIr. gaiset as its whole material (= Walde-Pokorny I 529). Nourai's double headword 'Ghait, Ghaita' simply reproduces Pokorny's '-a, -es-' stem alternation, and the gloss 'wavy hair' is Pokorny's own. In current notation the root is written *gʰeh₂it- (plain velar gʰ, laryngeal in the root); Beekes s.v. χαίτη accepts it. One modern caveat that the chart cannot show: because the Indo-Iranian side pairs Av. gaēsa- with Skt. keśa- (k- vs g-), Lubotsky and the Wiktionary reconstruction PII *káyćas ~ *gáyćas treat the Indo-Iranian word as a BMAC-substrate borrowing rather than an inherited PIE noun, which would make the Greek–Iranian equation a look-alike. The root box itself is a faithful rendering of POK:410 and is confirmed as such.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *gʰeh₂it- «موی مجعّد و موّاج». پوکورنی (ص ۴۱۰) دقیقاً همین ماده را با صورت ghait-a, -es- و همین معنی آورده و تمام شواهدش عبارت است از اوستایی gaēsa-، فارسی نو «گیس»، یونانی khaítē و ایرلندی میانه gaiset؛ والده‑پوکورنی (ج ۱ ص ۵۲۹) نیز همین را دارد. بنابراین نام ریشه، برچسب زبانی و معنای آن در نمودار نورایی درست است. تنها احتیاطی که باید افزود این است که چون در شاخهٔ هندوایرانی صورت اوستایی gaēsa- در برابر سنسکریت keśa- «مو» می‌ایستد و اختلاف g/k با قواعد آوایی سازگار نیست، پژوهشگران امروزی (لوبوتسکی، ویکی‌واژه) این واژه را وام‌واژه‌ای از زیرلایهٔ BMAC می‌دانند نه میراث مستقیم هندواروپایی؛ این نکته اصل ریشه را نفی نمی‌کند ولی پیوند یونانی–ایرانی را کم‌رنگ می‌سازد.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%CF%87%CE%B1%CE%AF%CF%84%CE%B7\",\n        \"https://en.wiktionary.org/wiki/%DA%AF%DB%8C%D8%B3\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:410\", \"status\": \"supports\", \"note\": \"POK_full.txt l.32302-32320, entry ending 'References: WP. I 529. Page(s):410': 'Root / lemma: ghait-a, -es- | Meaning: curly or wavy hair | Material: Von *ghait-[e]s-: Avestan gaesa- \\\"curly hair, curls\\\", npers. ges \\\"droopy hair, curls\\\", Avestan gaesu- \\\"fuzzy haired, curly haired; (from camel:) …\\\"; gr. χαίτη …; Middle Irish gaiset (from *ghait-s-) \\\"stiff hair, bristle\\\".' The printed page number 410 is given by the entry itself.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I 529 (WLD_Bd1_1930_dli_70244_djvu.txt l.33150-33159)\", \"stance\": \"supports\", \"note\": \"'ghait-a, -es- „krauses oder gewelltes Haar“. Gr. χαίτη … Von *ghait-[e]s- aus av. gaesa- m. „Kraushaar, Lockenhaar“, npers. ges „herabhangende Haare, Locken“, av. gaēsu- „kraushaarig, lockenhaarig; (beim Kamel:) zottelhaarig“; nir. gaoisead (aus *ghait-s-) „crinis“.' — identical material to Pokorny.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. ghait- (AHD_watkins1985.txt l.508-510)\", \"stance\": \"supports\", \"note\": \"'ghait-. Curly or wavy hair. Possible root. Suffixed form *ghait-ā in Greek khaité, long hair: CHAETA; (CHAETOGNATH). [Pok. ghait-ā- 410.]' — Watkins flags it as a 'possible root', matching the modern hesitation.\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, no gh(a)it- lemma found\", \"stance\": \"silent\", \"note\": \"grep of IEC.txt for 'ghait', 'gaisos', 'khaite' returns only the unrelated ghaisos 'spear' family; Mann does not set up a 'curly hair' root.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"gaĕsa, gaĕsu : hair; ges, gesuk : hair\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The Avestan half is exact: Bartholomae's Altiranisches Wörterbuch has gaēsa- m. 'Lockenhaar' (curly hair) and the adjective gaēsav- 'kraus', 'lockenhaarig', extended 'zottelhaarig' of a camel (uštrahe … gaēsauš) — Nourai's 'gaĕsa, gaĕsu' are these two, with the -u- stem gaēsu- being the compositional/adjectival form Pokorny quotes. The second pair, however, is NOT Old Persian: no such word is attested in the Achaemenid inscriptions (Kent's lexicon has nothing), and 'ges, gesuk' are the Middle Persian forms — MacKenzie's Concise Pahlavi Dictionary p.36 'ges [gys | (M gyswg, N gesu)] curls, locks', i.e. Book-Pahlavi gēs with the Manichaean-script variant gēsūg. Phonologically Av. gaēsa- > MP gēs by the regular monophthongisation of Old Iranian ai > MP ē and loss of the thematic ending, while gēsūg is gēs + the MP diminutive/adjectival suffix -ūg (< OIr. -uka-). The derivation drawn is therefore right, the language label is not: the node lumps Avestan with 'Old Persian' where it should read Middle Persian (Pahlavi).\",\n          \"derivation_fa\": \"بخش اوستایی درست است: بارتولومه در «فرهنگ ایرانی باستان» gaēsa- را «موی مجعّد» و صفت gaēsav- را «مجعّدمو» و در وصف شتر «پشمالو» آورده است؛ همان دو صورتی که نورایی به‌شکل gaĕsa و gaĕsu نوشته است. اما «ges، gesuk» پارسی باستان نیست — در سنگ‌نبشته‌های هخامنشی چنین واژه‌ای گواهی نشده — بلکه فارسی میانه (پهلوی) است: مکنزی gēs «زلف، طرّه» و صورت مانوی gēsūg را ثبت کرده است. از نظر آوایی، دوواکهٔ ai ایرانی باستان در فارسی میانه به ē بدل شده (gaēsa- ← gēs) و gēsūg همان gēs است با پسوند ـūg (از ایرانی باستان ‎-uka-‎). پس پیوند نموداری درست است ولی برچسب زبانی نادرست است و باید «اوستایی / فارسی میانه» می‌بود.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%AF%DB%8C%D8%B3\",\n            \"https://en.wiktionary.org/wiki/%CF%87%CE%B1%CE%AF%CF%84%CE%B7\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:410\", \"status\": \"supports\", \"note\": \"POK_full.txt l.32304-32310: 'Von *ghait-[e]s-: Avestan gaesa- \\\"curly hair, curls\\\" … Avestan gaesu- \\\"fuzzy haired, curly haired; (from camel:) rat's hairy tail\\\"' — both Avestan forms as drawn. Pokorny cites no Old Persian form.\"},\n            {\"ref\": \"KLN:264\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 150 (the following leaf 151 carries the printed page numbers '266 267', so leaf 150 = pp. 264-265), s.v. chaeto-: 'Fr. Gk. χαίτη, \\\"long flowing hair, mane\\\", which is cogn. with Avestic gaesa-, \\\"curly hair\\\", Ir. gaoisideach, \\\"hair\\\".' Klein's page 264 is exactly where Nourai points, and it does equate Greek χαίτη with Avestan gaēsa-.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Bartholomae, Altiran. Wb. s.vv. gaēsa-, gaēsav- (BRT.txt l.9750-9762)\", \"stance\": \"supports\", \"note\": \"'gaēsa- … Lockenhaar' with 'Vgl. gaesav-. — np. گیس \\\"Locken\\\"; s. dazu Hbm. AGr. I 127' and 'gaēsav- Adj. \\\"kraus\\\": 1) kraus-, lockenhaarig …; 2) \\\"zottelhaarig\\\", vom Kamel: uštrahe … gaēsauš'; the same article notes the Pahlavi rendering 'Ph.: gēswar, (zu V.): ges'.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dict. s.v. ges (PHD_mackenzie.txt l.2510)\", \"stance\": \"supports\", \"note\": \"'ges [gys | (M gyswg, N gesu)] curls, locks.' — i.e. MP gēs, Manichaean gēsūg: exactly Nourai's 'ges, gesuk', but labelled Middle Persian, not Old Persian.\"},\n            {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, lexicon\", \"stance\": \"silent\", \"note\": \"grep of KNT.txt for 'gaisa', 'gais', 'ges' finds no Old Persian entry for 'hair'; the word is unattested in Old Persian, which is why the node's language label is wrong.\"},\n            {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien §101 (HUB.txt l.7543)\", \"stance\": \"supports\", \"note\": \"'ges, gēsū \\\"Locken\\\" = zd. gaēsa-' — cited among the cases where NP s corresponds to Avestan s.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"gîs «گیس» : hair (also گیسو)\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP گیس gīs 'tress, lock of hair (esp. a woman's)' continues Middle Persian gēs directly: MP ē regularly raised to NP ī (cf. MP šēr > NP šīr, MP dēz > NP dīz/dež), so gēs > gīs. The doublet گیسو gēsū/gīsū given in the chart's script_extra is the Manichaean-Middle-Persian derivative gēsūg (gēs + -ūg) with the regular New Persian loss of final -g (cf. MP bāzūg > NP بازو bāzū, MP mōy…). Mo'in's own etymological footnote to Borhan-e Qate' p.1870 s.v. گیسو states the chain verbatim: 'گیس (ه.م.) از اوستایی gaēsa (رك: گیس): در اوراق مانوی بپهلوی gēsūg (کلاله، طرّه)، gēsvar (با موی مجعد) … موی بلند که از پشت گردن تجاوز کند'. The Avestan → Middle Persian → New Persian route drawn by Nourai is thus exactly the standard one; the only modern refinement is that the Indo-Iranian word itself (Av. gaēsa- beside Skt. keśa-) may be a substrate borrowing rather than PIE inheritance. The Hafez couplet quoted in the box ('دوش در حلقهٔ ما قصهٔ گیسوی تو بود') is a genuine Hafez ghazal line and uses گیسو in this sense.\",\n          \"derivation_fa\": \"«گیس» در فارسی نو دنبالهٔ مستقیم فارسی میانهٔ gēs است: ē فارسی میانه در فارسی نو به ī بدل شده (مانند šēr ← شیر، dēz ← دیز/دژ)، پس gēs ← گیس. صورت «گیسو» نیز همان مشتقّ فارسی میانهٔ مانوی gēsūg (gēs + پسوند ـūg) است که گ پایانی آن، بنا بر قاعدهٔ عمومی، در فارسی نو افتاده است (مانند bāzūg ← بازو). حاشیهٔ ریشه‌شناختی معین بر برهان قاطع، ص ۱۸۷۰ ذیل «گیسو»، دقیقاً همین زنجیره را می‌آورد: «گیس (ه.م.) از اوستایی gaēsa؛ در اوراق مانوی بپهلوی gēsūg (کلاله، طرّه)». هوبشمان و هرن (شمارهٔ ۹۵۰) نیز همین را دارند. بنابراین ادعای نورایی درست است؛ تنها احتیاط امروزی آن است که خودِ واژهٔ هندوایرانی شاید وام‌واژه‌ای زیرلایه‌ای باشد.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%AF%DB%8C%D8%B3\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:410\", \"status\": \"supports\", \"note\": \"POK_full.txt l.32310: 'npers. ges \\\"droopy hair, curls\\\"' listed directly under *ghait-[e]s- beside Avestan gaēsa-.\"},\n            {\"ref\": \"BQT:1870\", \"status\": \"supports\", \"note\": \"Borhan-e Qate', ed. Mo'in, printed p.1870 (BQT_v3_picofile.pdf pdf page 667, per BQT_v3_pagemap.json; the running head reads 'گیسودار ۱۸۷۰'), footnote to گیسو: 'گیس (ه.م.) از اوستایی gaēsa (رك: گیس): در اوراق مانوی بپهلوی gēsūg (کلاله؛ طرّه)، gēsvar (با موی مجعد) … موی بلند که از پشت گردن تجاوز کند'. Cached by tools/ref_page.py at data/verification/sources/refs/ocr/BQT/1870.{png,txt}. NOTE for the owner: ref_page.py's default offset (-1205) sends BQT:1870 to pdf page 665 (= printed 1868); the page_map value 667 is the correct one.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 950 (HRN.txt l.8233-8237)\", \"stance\": \"supports\", \"note\": \"'950. ges, gesū \\\"Locken, Gelock\\\". aw. gaēsa- \\\"in zwei oder drei (sc. Locken) geordnetes Haar\\\" (ZDMG); phlv. gēs, arm. syr. LW. ges, -ū \\\"Haar\\\"; oss. d. γesä, i. qīs \\\"Borste\\\".'\"},\n            {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien §101 and p.96 index (HUB.txt l.7543, l.8814)\", \"stance\": \"supports\", \"note\": \"'ges, gēsū \\\"Locken\\\" = zd. gaēsa-'.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' p.1870 footnote (see ref_check)\", \"stance\": \"supports\", \"note\": \"Mo'in derives گیسو from گیس < Av. gaēsa-, Man. MP gēsūg; quotes Golestan p.53 'شیادی گیسوان بافت بصورت علویان'.\"},\n            {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi s.v. گیس / گیسو\", \"stance\": \"supports\", \"note\": \"Mo'in's lexicon repeats the Borhan footnote (Pahlavi origin tag); the 2-vol abridgement on disk (MON_2vol_Adena_v2_djvu.txt) is volume غ–ی but its گیس page is not in the OCRed range — the fuller statement is the Borhan footnote quoted above.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Greek\",\n          \"words\": \"xaitĕ : long hair\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The book's 'xaitĕ' is a Latin-letter rendering of Ancient Greek χαίτη (khaítē) with x for chi — the printed page confirms this spelling, so it is Nourai's own transliteration convention, not a misreading. χαίτη means 'loose, flowing hair (esp. of the back of the head), a horse's or lion's mane, a helmet's crest, tree foliage' (LSJ; Pokorny quotes the same range). Formally it goes back to a suffixed *gʰeh₂it-eh₂ (AHD: 'suffixed form *ghait-ā in Greek khaité'); the PIE plain velar gʰ gives Greek kh, and the intervocalic *-t- before the *-eh₂ stem vowel is regular. Beekes's Greek etymological dictionary, followed by Wiktionary, keeps the comparison with Avestan gaēsa- and Middle Irish gaiset, i.e. exactly the arrow Nourai draws from the root.\",\n          \"derivation_fa\": \"آنچه کتاب «xaitĕ» نوشته همان χαίτη یونانی باستان (khaítē) است و x در شیوهٔ نویسهٔ نورایی برابر حرف «خی» است؛ تصویر صفحهٔ چاپی نیز همین را نشان می‌دهد، پس خطای اسکن در کار نیست. معنای آن «موی بلندِ افشان، یال اسب و شیر، کاکل خود جنگی، شاخ‌وبرگ درخت» است. از نظر ساخت، صورت پسوندی *gʰeh₂it-eh₂ را بازسازی می‌کنند: gʰ سادهٔ هندواروپایی در یونانی به kh بدل می‌شود و t میان‌واکه‌ای بی‌تغییر می‌ماند. بیکس در فرهنگ ریشه‌شناختی یونانی، و به پیروی او ویکی‌واژه، همین پیوند با اوستایی gaēsa- و ایرلندی میانه gaiset را می‌پذیرند؛ یعنی همان پیکانی که نورایی از ریشه به یونانی کشیده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%CF%87%CE%B1%CE%AF%CF%84%CE%B7\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt l.508-510: 'ghait-. Curly or wavy hair. Possible root. Suffixed form *ghait-ā in Greek khaité, long hair: CHAETA; (CHAETOGNATH). [Pok. ghait-ā- 410.]' — Nourai gives no page for AHD here; the New College appendix entry is on p.1517-area of the 1975/76 printing.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 410 (POK_full.txt l.32313-32315)\", \"stance\": \"supports\", \"note\": \"'gr. χαίτη \\\"loose, flowing hair, used esp. of back hair, of a horse's mane, of a lion's mane, of a hedgehog's spines, crest of a helmet, of trees, foliage, of human hair\\\"'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 529 (WLD_Bd1 l.33152-33153)\", \"stance\": \"supports\", \"note\": \"'Gr. χαίτη „Lockenhaar, frei herabwallendes Haar; Mähne (von Pferden, Löwen); Baumbart“' heads the article, i.e. Walde-Pokorny take the Greek word as the core of the root.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein I p.264 s.v. chaeto- (KLN_1966.txt leaf 150)\", \"stance\": \"supports\", \"note\": \"'Fr. Gk. χαίτη, \\\"long flowing hair, mane\\\", which is cogn. with Avestic gaesa-, \\\"curly hair\\\", Ir. gaoisideach, \\\"hair\\\".'\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"chaeta : bristle worm\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The route is right and uncontroversial: English chaeta is a 19th-century zoological New-Latin coinage taken straight from Greek χαίτη, with Greek χ transliterated ch and η as the Latin -a of the singular (plural chaetae); the same element gives chaeto-, Chaetodon, Chaetopoda, Oligochaeta, Polychaeta, Spirochaeta and chaetognath. It is a learned borrowing, not an inherited English word, so the arrow Greek → English means 'borrowed by scientific Latin and thence into English', and the chart's own reference (AHD, which lists CHAETA under ghait-) is the source of the link. The gloss is what is off: a chaeta is not a worm but a single chitinous bristle (seta) of an annelid or arthropod; 'bristle worm' is the name of the animal that bears them (Polychaeta). The verdict is therefore 'plausible' for the gloss only — the derivation itself is confirmed.\",\n          \"derivation_fa\": \"زنجیره درست و بی‌مناقشه است: chaeta واژه‌ای است که در سدهٔ نوزدهم در لاتینِ علمی از χαίτη یونانی ساخته شد و از آنجا به انگلیسی رسید؛ χ یونانی به ch و η به ـa لاتینی بدل شده (جمع آن chaetae). همین جزء در chaeto-، Chaetopoda، Oligochaeta، Polychaeta و Spirochaeta نیز هست. پس این یک وام‌واژهٔ عالمانه است نه میراث زبانی، و پیکان «یونانی ← انگلیسی» را باید «وام‌گیری از راه لاتین علمی» خواند. اشکال کار در معنای داده‌شده است: chaeta خودِ کرم نیست، بلکه «تارِ سختِ کیتینی» بر تن کرم‌های حلقوی است؛ «کرم پرتار» نام جانور (Polychaeta) است. بنابراین ریشه‌شناسی نورایی درست است ولی معنی‌گذاری او دقیق نیست.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/chaeta\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt l.510 lists CHAETA (and CHAETOGNATH) as the English derivatives of *ghait-ā via Greek khaité; the word-index at l.1342 confirms 'CHAETA ghait-'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein I p.264 s.v. chaeto-, Chaetodon, chaetopod; also Oligochaeta, Polychaeta, Spirochaeta (KLN_1966.txt l.7105, 26206, 29434, 36310)\", \"stance\": \"partial\", \"note\": \"Klein has no headword 'chaeta' but has 'chaeto-, before a vowel chaet-, combining form meaning \\\"spine\\\" or \\\"bristle\\\". — Fr. Gk. χαίτη' and 'Polychaeta, n. pl., a class of annelids, comprising most marine worms (zool.) — ModL., compounded of poly- and Gk. χαίτη, \\\"hair\\\"' — i.e. the bristle sense, confirming that 'bristle worm' is the animal, not the chaeta.\"},\n            {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dict., s.v. chaeta\", \"stance\": \"silent\", \"note\": \"grep of WEB_vol1.txt for 'chaeta' returns no separate headword in the OCR available on disk.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 2,\n      \"root\": \"Ghans\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *ǵʰh₂éns 'goose' (Pokorny ghan-s- 412)\",\n      \"note\": \"Pokorny IEW 412 'Root / lemma: ghan-s- | Meaning: goose' and Mann IEC pp.314-315 'ghansis \\\"goose\\\". WP I, 536' are both exactly where Nourai points, and both give the meaning he gives. Modern reconstruction writes the root *ǵʰh₂éns (palatal ǵʰ, acrostatic root noun), whence Skt. haṃsá-, Gk. χήν, Lat. ānser, PGmc. *gans. Nourai's Latin-letter 'Ghans' is Pokorny's spelling. TRANSCRIPTION NOTE (book, not extraction): the Sanskrit node's reference is printed on p.149 as 'UEC:314' — I checked the page image (data/verification/sources/refs/ocr/BOOK/179.png); 'UEC' is not in Nourai's bibliography and is his own typo for IEC (Mann), which is cited correctly in the root box and the Greek node. The JSON faithfully reproduces the misprint. The one substantive problem on this chart is the Persian node (#1), on which see below.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *ǵʰh₂éns «غاز». پوکورنی در ص ۴۱۲ همین ماده را با نام ghan-s- و همین معنی آورده و مان (IEC) در ص ۳۱۴–۳۱۵ ذیل ghansis «غاز» — یعنی هر دو ارجاع نورایی دقیق است. بازماندگان آن سنسکریت haṃsá-، یونانی khḗn، لاتینی ānser و ژرمنی آغازین *gans است. یادداشت چاپی: در گرهٔ سنسکریت، ارجاع «UEC:314» چاپ شده که در کتاب‌نامهٔ نورایی چنین اختصاری وجود ندارد؛ بررسی تصویر صفحهٔ چاپی نشان می‌دهد که خودِ کتاب «UEC» را چاپ کرده است، پس این غلط چاپی نویسنده است (به جای IEC) و خطای استخراج داده نیست. تنها اشکال جدّی این نمودار، گرهٔ فارسی «غاز» است که در زیر آمده.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0h%E2%82%82%C3%A9ns\",\n        \"https://www.etymonline.com/word/goose\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:412\", \"status\": \"supports\", \"note\": \"POK_full.txt l.35882-35950: 'Root / lemma: ghan-s- | Meaning: goose … Material: Old Indic haṃsa-ḥ m., haṃsī f. \\\"goose, swan\\\"; sogd. z'γ \\\"sorte d'oiseau\\\"; Latin anser … (originally *hanser) …; gr. χήν …; Old High German gans, Old English gōs …' ending 'References: WP. I 536, WH. I 52, 583 … Page(s):412'.\"},\n        {\"ref\": \"IEC:314\", \"status\": \"supports\", \"note\": \"IEC.txt leaf 185, which carries the printed page markers '314 315': 'ghansis (variant: ǵhansis) \\\"goose\\\". WP I, 536. Skt. hamsih \\\"kind of goose\\\"; hamsáh \\\"gander …\\\"; Hindi hans \\\"goose\\\"; Per. ġāz, id.; Gk. khén, m.f. \\\"goose; gander\\\"; OIr. géiss …; OHG gans …; OE gos, pl. gēs …' — the page is exactly right and even carries the Persian form Nourai draws.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I 536 (WLD_Bd1_1930_dli_70244_djvu.txt l.33712-33740)\", \"stance\": \"supports\", \"note\": \"'ghans- und verwandte Bildungen für „Gans“. Ai. haṃsá-ḥ m., haṃsī f. „Gans, Schwan“; gr. χήν, -ός, dor. boot. χάν „Gans“ …; lat. anser „Gans“ (ursprgl. *hanser …); air. geiss „Schwan“; ahd. gans …' — note that Walde-Pokorny list NO Iranian reflex at all.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ghans- (AHD_watkins1985.txt l.510)\", \"stance\": \"supports\", \"note\": \"'ghans-. Goose. 1. Germanic *gans- … 2. Germanic *ganr- … 3. Germanic *ganōton- … 4. Suffixed form *ghans-er- in Latin ānser (< *hanser) … 5. Basic form *ghans- in Greek khēn, goose: CHENOPOD. [Pok. ghans- 412.]'\"},\n        {\"src\": \"SYN\", \"where\": \"Buck 3.56 GOOSE (SYN.txt l.4782-4790)\", \"stance\": \"partial\", \"note\": \"Buck's goose table gives Grk. χήν, Lat. anser, Gmc., Balto-Slavic and Skt. haṃsa-, with the note 'If *ǵhans-, prob. fr. the root seen in Grk. χάσκω, ἔχανον \\\"yawn, gape\\\" … Walde-P. 1.536' — but his Avestan and (New) Persian slots are empty: no Iranian reflex is offered.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"ğâz «غاز» : goose\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Persian غاز ğāz 'goose' is real and correctly glossed, but the arrow straight from PIE *ǵʰh₂éns is rejected by modern scholarship, on two independent grounds. (a) Phonology: PIE palatal *ǵʰ gives Proto-Iranian *ȷ́ʰ > z (satem), so an inherited Iranian reflex would begin with z-, not ġ- — compare Lith. žąsis, Latv. zoss, and the Sogdian bird-name z'γ that Pokorny himself cites; word-initial غ /ġ/ is in any case foreign to inherited New Persian phonology and marks a loan. (b) Attestation and geography: the word matches the Turkic family point for point — Old/Middle Turkic and Karakhanid qāz, Chagatai غاز ğāz, Ottoman قاز qaz, Azerbaijani/Turkmen qaz/gāz, from Proto-Turkic *kāŕ — and Persian غاز is one of the many Turkic animal- and household-words that entered Persian in the Saljuq and post-Mongol periods. Wiktionary states flatly 'A Turkic borrowing: compare Chagatai غاز (ğaz), Ottoman Turkish قاز (qaz), Azerbaijani qaz. Ultimately from Proto-Turkic *kāŕ', and — decisively for Nourai's own citation — Mo'in himself tags the entry '[تر. ← قاز]' ('Turkish, from qāz'), i.e. MON:2375 contradicts the arrow it is cited for. Nourai's other reference, Mann IEC:314, does list 'Per. ġāz' under ghansis, and Aryanpur's Persian IE-roots dictionary likewise files Baluchi ġāz and Pashto qāz under the goose root; but Mann never addresses the ġ-/z- problem, and Wiktionary's PIE page notes that any resemblance of Turkic *kāz to the IE word is 'likely coincidental or a borrowing from Tocharian'. So the most that can be salvaged is an indirect, Turkic-mediated relationship, not the direct inheritance drawn here.\",\n          \"derivation_fa\": \"«غاز» واژه‌ای است واقعی و معنایش هم درست ثبت شده، اما پیکانی که نورایی مستقیماً از ریشهٔ هندواروپایی *ǵʰh₂éns به آن کشیده است از دو جهت پذیرفتنی نیست. نخست، آواشناسی: ǵʰ کامی هندواروپایی در شاخهٔ ایرانی (زبان‌های ساتم) به z بدل می‌شود، پس بازماندهٔ موروثیِ این ریشه در ایرانی باید با «ز» آغاز شود نه با «غ» — چنانکه لیتوانیایی žąsis و نام پرندهٔ سغدی z'γ که خودِ پوکورنی آورده است نشان می‌دهد؛ افزون بر این «غ» آغازین در واژه‌های اصیل فارسی نو جایی ندارد و خود نشانهٔ وام‌واژه است. دوم، گواهی و پراکندگی: صورت واژه نقطه‌به‌نقطه با خانوادهٔ ترکی می‌خواند — قراخانی و ترکی میانه qāz، جغتایی «غاز»، عثمانی «قاز»، آذربایجانی و ترکمنی qaz/gāz، از ترکی آغازین *kāŕ. ویکی‌واژه صریحاً آن را وام‌واژهٔ ترکی می‌داند، و مهم‌تر از همه خودِ معین در «فرهنگ فارسی» ذیل «غاز» نشانهٔ «[تر. ← قاز]» گذاشته است؛ یعنی همان مأخذی که نورایی به آن استناد کرده (MON:2375) خلاف ادعای او را می‌گوید. تنها مان (IEC ص ۳۱۴) و آریان‌پور «غاز» را زیر ریشهٔ هندواروپایی آورده‌اند، ولی به دشواری غ/ز نپرداخته‌اند. حکم: پژوهش امروزی این پیوند را رد می‌کند و «غاز» را وام‌واژهٔ ترکی می‌شمارد؛ نهایتاً می‌توان از خویشاوندی غیرمستقیم و باواسطهٔ ترکی سخن گفت، نه از میراث مستقیم هندواروپایی.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%BA%D8%A7%D8%B2\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0h%E2%82%82%C3%A9ns\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IEC:314\", \"status\": \"supports\", \"note\": \"IEC.txt leaf 185 (printed 314-315) s.v. ghansis 'goose': '… Hindi hans \\\"goose\\\"; Per. ġāz, id.; Gk. khén …'. Mann does file Persian ġāz under the IE goose root — but offers no phonological account, and no other IE dictionary on this shelf follows him.\"},\n            {\"ref\": \"MON:2375\", \"status\": \"contradicts\", \"note\": \"Mo'in, Farhang-e Farsi s.v. غاز (bird), read in the 2-vol abridgement MON_2vol_Adena_v2_djvu.txt l.224: 'غاز [تر. ← قاز] (اِ.) (جان.) پرنده‌ای است از راستهٔ پرده‌پایان که جثه‌ای درشت‌تر از اردک دارد …' — the bracketed tag [تر. ← قاز] means 'Turkish, from qāz'. The adjacent homonym غاز 'smallest Qajar coin' is likewise tagged [← قاز]. Mo'in therefore says the opposite of the arrow he is cited for. (Page numbers of the 6-vol print edition cannot be mapped in this abridgement; the entry text with its origin tag is identical.)\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. غاز (MON_part2.txt l.224)\", \"stance\": \"contradicts\", \"note\": \"'غاز [تر. ← قاز] … پرنده‌ای است …' — Turkic origin tag.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-ha-ye Hend-o-Orupayi, pdf pages 393-394 of ARY_latin_index_pages.txt\", \"stance\": \"supports\", \"note\": \"The 'goose' root article lists 'GHAZ (BALUCHI) غاز', 'Qaz (AFGHANI) قاز', 'HANSA, HANS (SANSKRIT)', 'CHEN, KHEN (GREEK)', 'ANSER (LATIN)', 'GANS (OLD HIGH GERMAN/GERMAN)', 'GOOSE (ENGLISH)' etc., with references 'POKORNY … BARNHART: (GOOSE) 442, DELAMARRE 139, BUCK: 17, ONIONS: (GOOSE) 406'. So Aryanpur, like Mann, treats the Iranian ġāz-words as inherited — but again without confronting the ġ-/z- difficulty.\"},\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss der neupersischen Etymologie\", \"stance\": \"silent\", \"note\": \"grep of HRN.txt for غاز / 'Gans' finds only 'alb. gāsē \\\"Gans\\\"' quoted under a different lemma (l.2337); Horn has no entry for Persian ġāz — he does not treat it as an inherited Persian word.\"},\n            {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien\", \"stance\": \"silent\", \"note\": \"grep of HUB.txt for 'Gans' yields only 'Dem alban. pate \\\"Gans\\\" wurde …' (l.999) under a different word; no ġāz entry.\"},\n            {\"src\": \"SOD\", \"where\": \"Gharib, Sogdian Dictionary no. 9113 (SOD_pages.txt l.30019-30023)\", \"stance\": \"silent\", \"note\": \"Gharib's Sogdian word for 'goose' is '9113 syč (B) — sīc(a)? < *sika < *siyaka … goose', unrelated to ġāz; the Sogdian z'γ 'kind of bird' that Pokorny cites is not a ġ-initial form either. No Iranian ġāz-type reflex is attested in the older languages.\"},\n            {\"src\": \"LKT\", \"where\": \"Lokotsch, Etym. Wb. der europ. Wörter orient. Ursprungs\", \"stance\": \"silent\", \"note\": \"grep of LKT.txt for 'kaz'/'qaz' finds only Tk. kazak (no. 1143) and Kazan-Tatar čapak; Lokotsch has no 'goose' entry, as the word did not travel into European languages.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"hamsîh : goose\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sanskrit haṃsá- m. 'goose, swan, gander' with the feminine haṃsī 'female goose' is the Indic reflex of *ǵʰh₂éns-: the palatal *ǵʰ becomes Indo-Iranian *ȷ́ʰ and then Old Indic h (the well-known ǵʰ > h shift Pokorny notes as 'Common Old Indic: Latin gh- > h-'), and the *-ns- cluster is preserved as -ṃs-. Nourai's form 'hamsîh' with final -h is Mann's transliteration (IEC prints 'Skt. hamsih \\\"kind of goose\\\"' beside 'hamsáḥ \\\"gander\\\"'), i.e. the feminine haṃsī-; the ordinary citation form is haṃsa-. The bird is prominent from the Rigveda on (haṃsa- of the wild goose, later of the swan of poetic convention). The node's reference 'UEC:314' is Nourai's misprint for IEC:314 — the printed page shows 'UEC', so the book, not the extraction, is at fault.\",\n          \"derivation_fa\": \"سنسکریت haṃsá- (مذکر) «غاز، قو» و مؤنث آن haṃsī «غاز ماده» بازماندهٔ هندی ریشهٔ *ǵʰh₂éns- است: ǵʰ کامی در هندوایرانی به ȷ́ʰ و سپس در هندی باستان به h بدل شده (همان تحول شناخته‌شدهٔ gh ← h که پوکورنی نیز بدان اشاره می‌کند) و خوشهٔ ‎-ns-‎ به‌صورت ‎-ṃs-‎ مانده است. صورت «hamsîh» که نورایی آورده همان نویسهٔ مان است (IEC: «Skt. hamsih \\\"kind of goose\\\"») و در واقع مؤنث haṃsī است؛ صورت متعارف haṃsa- است. این واژه از ریگ‌ودا به بعد گواهی دارد. ارجاع «UEC:314» غلط چاپیِ خود کتاب است به‌جای IEC:314؛ تصویر صفحه نشان می‌دهد که همین «UEC» چاپ شده، پس خطای استخراج نیست. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0h%E2%82%82%C3%A9ns\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"UEC:314\", \"status\": \"not_found\", \"note\": \"There is no 'UEC' in Nourai's bibliography. The printed page 149 (image saved at data/verification/sources/refs/ocr/BOOK/179.png) really does read 'UEC:314', so this is the author's typo for IEC:314 (Mann), not a scanning error. Read as IEC:314 it supports: IEC.txt leaf 185 (printed 314-315), 'ghansis \\\"goose\\\" … Skt. hamsih \\\"kind of goose\\\"; hamsáh \\\"gander of some kind\\\"'.\"},\n            {\"ref\": \"POK:412\", \"status\": \"supports\", \"note\": \"POK_full.txt l.35892: 'Material: Old Indic haṃsa-ḥ m., haṃsī f. \\\"goose, swan\\\"' — the first item of the article, followed by the note 'Common Old Indic : Latin gh- > h-'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. I 536 (WLD_Bd1 l.33716)\", \"stance\": \"supports\", \"note\": \"'Ai. haṃsá-ḥ m., haṃsī f. „Gans, Schwan“' heads the ghans- article.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 3.56 GOOSE (SYN.txt l.4784-4787)\", \"stance\": \"supports\", \"note\": \"'Skt. haṃsa- (also \\\"swan\\\", etc.)' listed among the reflexes of *ǵhans-.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. goose (KLN_1966.txt l.16447)\", \"stance\": \"supports\", \"note\": \"'cogn. with OI. haṃsaḥ (masc.), haṃsī (fem.), \\\"goose, swan\\\", Dor., Boeot. Gk. χάν, Gk. χήν, L. anser (for *hanser) …'\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Germanic\",\n          \"words\": \"gans, ganr, ganôtôn : goose\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The three forms are the three Germanic stems Watkins sets up under *ghans-, copied straight from the AHD appendix: (i) Gmc. *gans- (nom. pl. *gansiz) — the plain root noun, giving OHG/German Gans, OE gōs (pl. gēs, by i-umlaut and the West-Germanic loss of n before s with compensatory lengthening: *gans-iz > *gãsi > gēs), ON gás; (ii) Gmc. *ganr- (Nourai's 'ganr'), a masculine formation in -r- giving OE ganra/gandra with an excrescent d; (iii) Gmc. *ganōton- (Nourai's 'ganôtôn'), the -d-/-t- extension of the shorter stem *gan-, giving OE ganot and OHG ganazzo, and already Latin-attested in Pliny's ganta 'a kind of goose' borrowed from Germanic. Pokorny and Walde-Pokorny set up the same three, explicitly relating *ghan-[e]s- : *ghan- as *men-ōt- : *men-[e]s- 'month'. AHD:1517 is the appendix page in the 1975/76 New College Edition, in the right stretch for gh- roots.\",\n          \"derivation_fa\": \"این سه صورت همان سه ستاک ژرمنی است که واتکینز در پیوستِ AHD ذیل *ghans- می‌آورد و نورایی عیناً نقل کرده است: یک) ژرمنی *gans- (جمع *gansiz)، همان اسمِ ریشه‌ای که آلمانی Gans، انگلیسی کهن gōs (جمع gēs، با افتادن n پیش از s و کشش جبرانی و سپس امالهٔ i) و ایسلندی کهن gás از آن است؛ دو) ژرمنی *ganr- (نوشتهٔ نورایی «ganr»)، ساختی مذکر با ‎-r-‎ که به gandra/ganra در انگلیسی کهن رسیده و d آن زائد است؛ سه) ژرمنی *ganōtōn- («ganôtôn»)، گسترشِ ‎-d-/-t-‎ از ستاک کوتاه‌ترِ *gan-، که ganot انگلیسی کهن و ganazzo آلمانی عالی باستان از آن است و پیش‌تر هم لاتینی ganta نزد پلینیوس آن را از ژرمنی وام گرفته بود. پوکورنی و والده‑پوکورنی نیز همین سه را دارند و نسبت *ghan-[e]s- به *ghan- را با *men-ōt- : *men-[e]s- «ماه» مقایسه می‌کنند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/goose\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0h%E2%82%82%C3%A9ns\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1517\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt l.510 s.v. ghans-: '1. Germanic *gans- (nominative plural *gansiz) in: a. Old English gōs (nominative plural gēs), goose: GOOSE; (GOSHAWK); b. Old Norse gás … GOSLING. 2. Germanic *ganr- in Old English ganra, gandra, gander: GANDER. 3. Germanic *ganōton- in Old English ganot, gannet: GANNET.' The 1985 standalone Watkins reprints the New College appendix whose gh- roots stand around p.1517.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 412 (POK_full.txt l.35913, 35932-35938)\", \"stance\": \"supports\", \"note\": \"'Old High German gans …, Old English gōs (Pl. gēs from *gans-iz = gr. χῆνες), Old Icelandic gás …'; 'Old English gan(d)ra \\\"gander\\\" (engl. gander)'; 'Besides … of the abbreviated stem *ghan- (wherefore ghan-[e]s- as Indo-Germanic *men-ōt- : *men-[e]s- \\\"month\\\") … with -d-: Germanic (first in Pliny) ganta \\\"a kind of goose\\\" … Old English ganot …, Old High German ganazzo \\\"gander\\\"'.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.vv. goose, gander, gannet (KLN_1966.txt l.15766, 15780, 16447)\", \"stance\": \"supports\", \"note\": \"'gander, n. — ME. gandre, fr. OE. ganra, gandra, rel. to Du. gander, MLG. ganre …'; 'gannet, n., the solan goose. — OE. ganot, \\\"sea bird, gannet\\\", rel. to Du. gent, OHG. gannasso, ganzo, \\\"gander\\\"'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 536 (WLD_Bd1 l.33732-33740)\", \"stance\": \"supports\", \"note\": \"'Ags. gan(d)ra „Gänserich“ (engl. gander), mnd. ganre ds. … gilt als Mask.-Bildung vom St. *gan-'; and for the -d- stem: 'germ. … ganta „eine Art Gans“ …, ags. ganot „ein wilder Wasservogel“, ahd. ganazzo „Gänserich“'.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"goose, gander, gannet\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three are inherited (not borrowed) English words continuing the three Germanic stems of node #3. GOOSE: OE gōs, pl. gēs > ME gos/goos, pl. gees > NE goose/geese — the vowel of the plural is the i-umlaut of *gansiz, and the -oo- of the singular is the Great Vowel Shift's raising of ME long ō. GANDER: OE gandra/ganra > ME gandre > NE gander, still the male bird. GANNET: OE ganot 'sea-bird' > NE gannet, now specifically Morus bassanus, the solan goose. Etymonline and Klein give the same chain, and the AHD appendix lists precisely these three (plus GOSLING, GOSHAWK, GOSSAMER) as the English derivatives of *ghans-. The node carries no gloss in the JSON because the printed box gives none; 'goose' is understood from the parent.\",\n          \"derivation_fa\": \"هر سه واژه میراثی‌اند (نه وام‌واژه) و دنبالهٔ همان سه ستاک ژرمنی گرهٔ پیشین‌اند. goose از انگلیسی کهن gōs (جمع gēs) که به gos/goos انگلیسی میانه و سپس goose/geese رسیده؛ واکهٔ جمع نتیجهٔ امالهٔ i در *gansiz است و ō بلند انگلیسی میانه بر اثر «جابه‌جایی بزرگ واکه‌ها» به /uː/ بدل شده. gander از انگلیسی کهن gandra/ganra، هنوز به معنی «غاز نر». gannet از انگلیسی کهن ganot «پرندهٔ دریایی»، امروز نام گونهٔ Morus bassanus. اتیمانلاین و کلاین همین زنجیره را می‌دهند و پیوستِ AHD نیز دقیقاً همین سه واژه (به‌علاوهٔ gosling و goshawk) را زیر *ghans- می‌آورد. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/goose\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt word-index l.1553 'GANDER ghans-', 'GANNET ghans-' and l.1565 'GOOSE ghans-', 'GOSHAWK ghans-', 'GOSLING ghans-'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.vv. goose, gander, gannet (KLN_1966.txt l.16447, 15766, 15780)\", \"stance\": \"supports\", \"note\": \"'goose, n. — ME. gos, goos, fr. OE. gōs, rel. to OFris., MLG. gōs, ON. gás, OHG., MHG., G. gans …'; 'gander … fr. OE. ganra, gandra'; 'gannet, n., the solan goose. — OE. ganot'.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. s.v. goose\", \"stance\": \"supports\", \"note\": \"grep of SKT.txt s.v. goose gives the same OE gōs / Du. gans / G. Gans / Icel. gás set with Skt. hamsa, L. anser, Gk. χήν as cognates.\"},\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard Dict.\", \"stance\": \"silent\", \"note\": \"the OCR of FSD_vol1-4 on disk is too broken at the 'goo-' range to quote a usable etymology; nothing found to add or contradict.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Latin\",\n          \"words\": \"ânser, hanser : goose\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Latin ānser, -eris m. (f.) 'goose' is the genuine Latin reflex and is correctly placed under the root; the sacred geese of the Capitol make it one of the best-attested Latin bird-names. The form is built on a suffixed *ǵʰh₂ns-er- (Watkins: 'Suffixed form *ghans-er- in Latin ānser'), and the vowel length of ā- results from the loss of the laryngeal/nasal in the zero-grade *ǵʰh₂ns- with compensatory lengthening. Where the node overstates is 'hanser': that is not an attested Latin word but a reconstructed pre-form, *hanser, posited to explain how PIE *ǵʰ- could have given Latin h- before it was lost (all the sources write it with an asterisk — Watkins 'Latin ānser (< *hanser)', Walde-Pokorny 'lat. anser „Gans“ (ursprgl. *hanser)', Buck 'Lat. anser (for hanser)', Klein 'L. anser (for *hanser)'). Ernout-Meillet in fact note the doublet ansar/anser and treat the h- as a grammarians' inference; the initial h- is nowhere transmitted in Latin texts. So the node is right about ānser and lists a starred reconstruction as if it were a second Latin word.\",\n          \"derivation_fa\": \"ānser لاتینی «غاز» بازماندهٔ راستین این ریشه است و جای آن در نمودار درست است؛ داستان غازهای مقدّس کاپیتول آن را از پرگواه‌ترین نام‌پرندگان لاتینی کرده است. ساخت آن صورت پسوندیِ *ǵʰh₂ns-er- است و کشیدگی ā- از افتادن حنجری/خیشومی در درجهٔ صفر و کشش جبرانی پدید آمده. اما «hanser» واژه‌ای لاتینی نیست، بلکه صورتِ بازسازی‌شدهٔ *hanser است که برای توضیح سرنوشت gʰ آغازین فرض کرده‌اند؛ همهٔ مأخذها آن را با ستاره می‌نویسند: واتکینز «Latin ānser (< *hanser)»، والده‑پوکورنی «lat. anser „Gans“ (ursprgl. *hanser)»، باک «Lat. anser (for hanser)» و کلاین «L. anser (for *hanser)». در هیچ متن لاتینی h آغازین گواهی نشده است. پس گرهٔ نورایی دربارهٔ ānser درست است ولی یک صورت بازسازی‌شده را همچون واژهٔ دوم لاتینی در کنار آن نشانده است — با احتیاط پذیرفتنی.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0h%E2%82%82%C3%A9ns\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt l.510: '4. Suffixed form *ghans-er- in Latin ānser (< *hanser), goose: ANSERINE; MERGANSER.' Watkins gives ānser as the Latin word and marks *hanser as a pre-form with '<', which Nourai's box renders as a second Latin variant.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. I 536 (WLD_Bd1 l.33719-33722)\", \"stance\": \"partial\", \"note\": \"'lat. anser „Gans“ (ursprgl. *hanser, s. Vf. LEWb.² s.v.; die Stammbildung vermutlich … durch Verquickung von *hans- mit einer suffixal hochstufigen Form *hanes-)' — *hanser explicitly starred as the original, not an attested variant.\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. anser (LAT.txt l.4015, 4060)\", \"stance\": \"partial\", \"note\": \"'anser, -eris (doublet ansar, -aris, blâmé par l'App. Probi) m. (fém. …)' — the attested Latin doublet is ansar/anser; the h- form is discussed only as a reconstruction (l.6174 mentions '(h)anser' as a substitute form attested in Avienus, 4th-5th c., i.e. a late orthography, not classical).\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 3.56 (SYN.txt l.4786)\", \"stance\": \"partial\", \"note\": \"'Lat. anser (for hanser)' — same starred pre-form.\"},\n            {\"src\": \"POK\", \"where\": \"IEW 412 (POK_full.txt l.35894)\", \"stance\": \"partial\", \"note\": \"'Latin anser, mostly m. \\\"goose\\\" (originally *hanser, to stem formation compare Slavic *zansera- (*gansera-) \\\"gander\\\" …)'.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Greek\",\n          \"words\": \"khĕn : goose\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Ancient Greek χήν, gen. χηνός m./f. 'goose' (Doric/Boeotian χάν) is the Greek reflex of the root noun *ǵʰh₂ens: PIE palatal *ǵʰ becomes Greek kh (χ), and the *-ans- of the pre-form *χανς gives χήν by the regular Attic-Ionic loss of ν before ς with compensatory lengthening of a > ē (Doric keeps ā, hence χάν) — Pokorny states this explicitly ('gr. χήν … from *χανς, *χανσος'). The old consonant-stem inflection is preserved in the genitive plural, which Pokorny pairs with Lith. žąsų̃ and OE gēs. The word yields English CHENOPOD via botanical Latin. Nourai's 'khĕn' with a short-marked e is a transliteration slip for the long ē of χήν, but that is a diacritic, not a wrong word.\",\n          \"derivation_fa\": \"χήν یونانی باستان (مضاف‌الیه χηνός، دوری/بئوسی χάν) «غاز» بازماندهٔ همان اسمِ ریشه‌ای *ǵʰh₂ens است: ǵʰ کامی هندواروپایی در یونانی به χ بدل می‌شود، و خوشهٔ ‎-ανς‎ در گویش آتیک‑ایونی با افتادن ν پیش از ς و کشش جبرانیِ a به ē صورت χήν می‌دهد؛ گویش دوری که ā را نگاه داشته χάν دارد. پوکورنی همین را می‌گوید و صرفِ کهنِ صامتیِ آن را در مضاف‌الیه جمع با žąsų̃ لیتوانیایی و gēs انگلیسی کهن می‌سنجد. نویسهٔ «khĕn» با علامت کوتاهی بر e لغزشی در نویسه‌گردانی است (واکهٔ آن بلند است) نه واژه‌ای نادرست. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0h%E2%82%82%C3%A9ns\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IEC:314\", \"status\": \"supports\", \"note\": \"IEC.txt leaf 185 (printed 314-315) s.v. ghansis: 'Gk. khén, m.f. \\\"goose; gander\\\"' — exactly the form and gloss of the node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 412 (POK_full.txt l.35901-35903)\", \"stance\": \"supports\", \"note\": \"'gr. χήν, -ός, m. f., Doric Boeotian χάν \\\"goose\\\" from *χανς, *χανσος (here, as in Germanic and in Lithuanian Gen. Pl. žąsų̃, still the old consonant inflection)'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 536 (WLD_Bd1 l.33717)\", \"stance\": \"supports\", \"note\": \"'gr. χήν, -ός, dor. boot. χάν „Gans“ (hier, wie im Germ. und im lit. gen. pl. žąsų̃ noch die alte kons. Flexion)'.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ghans- (AHD_watkins1985.txt l.510)\", \"stance\": \"supports\", \"note\": \"'5. Basic form *ghans- in Greek khēn, goose: CHENOPOD.'\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-05T21:06:57.404Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-179.json (file state is current in your context — no need to Read it back)
```


## [2026-09-05T21:07:00.963Z] TOOL CALL #53: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-179.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 179",
 "description": "Validate JSON and run verify_check"
}
```


### [2026-09-05T21:07:03.234Z] TOOL RESULT

```
JSON OK
nodes verified: 10/10
node verdicts: {'plausible': 3, 'confirmed': 6, 'disputed': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 11, 'contradicts': 1, 'not_found': 1, 'partial': 1}
books consulted: {'supports': 22, 'silent': 7, 'partial': 5, 'contradicts': 1} | by book: {'WLD': 5, 'KLN': 5, 'POK': 4, 'HUB': 3, 'HRN': 2, 'MON': 2, 'SYN': 2, 'BRT': 1, 'PHD': 1, 'KNT': 1, 'BQT': 1, 'WEB': 1, 'ARY': 1, 'SOD': 1, 'LKT': 1, 'SKT': 1, 'FSD': 1, 'LAT': 1, 'AHD': 1}
```


## [2026-09-05T21:07:20.848Z] AGENT

Page 179 (book p. 149) verified: `/home/sfmqrb/git/rishe/data/verification/page-179.json` — `verify_check.py 179` reports 10/10 nodes, 0 PROBLEM lines.

**Counts:** roots 2 confirmed. Nodes: 6 confirmed, 3 plausible, 1 disputed. Ref checks: 11 supports, 1 partial, 1 contradicts, 1 not_found. 4 redirect entries skipped.

**Disputed**
- **Ghans / Persian غاز ğāz (#1)** — Nourai derives it straight from PIE *ǵʰh₂éns. Modern view: a Turkic loan (Chagatai غاز, Ottoman قاز, Proto-Turkic *kāŕ). PIE palatal *ǵʰ gives Iranian *z-, so an inherited reflex would begin z-, not ġ-; initial غ marks a loan. Decisively, Nourai's own cited **MON:2375 contradicts him** — Mo'in tags the entry `[تر. ← قاز]` "Turkish, from qāz". Only Mann (IEC:314) and Aryanpur file it under the IE root; Horn, Hübschmann, Walde-Pokorny and Buck give no Iranian reflex at all.

**Plausible (with reasons)**
- Ghait #1 "Avestan / Old Persian": the Avestan forms are right, but *ges, gesuk* are **Middle Persian** (MacKenzie `ges [gys | (M gyswg)]`), unattested in Old Persian — wrong language label.
- Ghait #4 English *chaeta*: route correct (NLat. ← Gk. χαίτη), but the gloss is wrong — a chaeta is the *bristle*, not the "bristle worm".
- Ghans #5 Latin "ânser, hanser": ānser is real; *hanser* is a starred pre-form (AHD "ānser (< *hanser)"), not a Latin word.

**Book misprint (not an extraction error)** — Ghans #2 Sanskrit reference prints **`UEC:314`**; there is no UEC in the bibliography and the page image confirms the book prints it. It is Nourai's typo for IEC:314 (which does support the node). Page image saved to `data/verification/sources/refs/ocr/BOOK/179.png`.

**No extraction errors found** — the JSON matches the printed page throughout (including "xaitĕ", "ganôtôn", "hamsîh", the Hafez couplet and گیسو).

**Tooling note for you:** `tools/ref_page.py BQT:1870` uses the default offset −1205 → pdf 665 (= printed 1868); the correct value from `BQT_v3_pagemap.json` is pdf **667**. The pagemap has gaps (1860–1870 absent) so the script falls back to the offset. Correct page cached at `data/verification/sources/refs/ocr/BQT/1870.{png,txt}` — Mo'in's footnote there confirms گیس/گیسو ← Av. gaēsa-, Man. MP gēsūg.
