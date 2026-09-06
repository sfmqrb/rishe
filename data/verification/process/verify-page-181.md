# Verification process log — verify-page-181


## [2026-09-05T20:52:43.201Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 181 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-181.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-181.json. Write /home/sfmqrb/git/rishe/data/verification/page-181.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 181` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:52:45.225Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:52:45.713Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:52:45.726Z] TOOL RESULT

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


## [2026-09-05T20:52:46.145Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-181.txt"
}
```


### [2026-09-05T20:52:46.158Z] TOOL RESULT

```
1	=== PDF page 181 (book page 151) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ghdies, Ghdes, Ghies, Ghes : yester  (refs POK:416)
4	#1 (parent #0) [Avestan] refs=POK:416; KLN:1762 | zyô : yester
5	  #2 (parent #1) [Pahlavi] refs=None | dîk
6	    #3 (parent #2) [Persian] refs=MON:1588 | dî «دی ۳ ( دیروز ، دیشب )» : yester
7	#4 (parent #0) [Sogdian] refs=SOD:94 | `zyy-myd : yesterday
8	#5 (parent #0) [Germanic] refs=AHD | ges-ter : yester
9	  #6 (parent #5) [English] refs=None | yester, yesterday
10	--- entry 1 ---
11	ROOT [Indo-European] Ghě 1, Ghěi 3, Ghi-ghe-me : to go, to let go, also to go without (lack); I reach, meet with  (refs POK:418; KLN:666)
12	#1 (parent #0) [Avestan] refs=POK:418; KLN:666 | zâ 1 : to go ; â-zâ : go to, go near ☞Apo ; uz-zâ, uzayantô : to spring up, burst open ☞Ud 1 ; zazâmi : I dismiss ; avâ-zazâmi : I let off (remove) ☞Au 2 ; frâ-zazâmi, upa-zazâmi : to let to, forward ☞Upo,Per 1
13	#2 (parent #0) [Germanic] refs=AHD | gee-n : to go
14	  #3 (parent #2) [English] refs=None | go, ago, forego
15	#4 (parent #0) [Latin] refs=AHD | hěrěs : one who goes without parents, orphan
16	  #5 (parent #4) [English] refs=None | heir, heredity, heritage, inherit
17	--- entry 2 ---
18	ROOT Ghe 2 -> redirect to Ki 2
19	
```


## [2026-09-05T20:52:49.212Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-181.json",
 "description": "Read source JSON page 181"
}
```


### [2026-09-05T20:52:49.248Z] TOOL RESULT

```
{
  "pdf_page": 181,
  "book_page": 151,
  "entries": [
    {
      "root": {
        "name": "Ghdies, Ghdes, Ghies, Ghes",
        "lang": "Indo-European",
        "refs": "POK:416",
        "gloss": "yester"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:416; KLN:1762",
          "words": [
            {"translit": "zyô", "gloss": "yester", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": null,
          "words": [
            {"translit": "dîk", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:1588",
          "words": [
            {"translit": "dî", "gloss": "yester", "script": "دی ۳ ( دیروز ، دیشب )"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:94",
          "words": [
            {"translit": "`zyy-myd", "gloss": "yesterday", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "ges-ter", "gloss": "yester", "script": null}
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
            {"translit": "yester, yesterday", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Ghě 1, Ghěi 3, Ghi-ghe-me",
        "lang": "Indo-European",
        "refs": "POK:418; KLN:666",
        "gloss": "to go, to let go, also to go without (lack); I reach, meet with"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:418; KLN:666",
          "words": [
            {"translit": "zâ 1", "gloss": "to go", "script": null},
            {"translit": "â-zâ", "gloss": "go to, go near", "script": null, "see": ["Apo"]},
            {"translit": "uz-zâ, uzayantô", "gloss": "to spring up, burst open", "script": null, "see": ["Ud 1"]},
            {"translit": "zazâmi", "gloss": "I dismiss", "script": null},
            {"translit": "avâ-zazâmi", "gloss": "I let off (remove)", "script": null, "see": ["Au 2"]},
            {"translit": "frâ-zazâmi, upa-zazâmi", "gloss": "to let to, forward", "script": null, "see": ["Upo", "Per 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "gee-n", "gloss": "to go", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "go, ago, forego", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "hěrěs", "gloss": "one who goes without parents, orphan", "script": null}
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
            {"translit": "heir, heredity, heritage, inherit", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Ghe 2",
        "redirect": "Ki 2"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-05T20:52:50.203Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -50 && cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "List verification dir and read source matrix"
}
```


### [2026-09-05T20:52:50.247Z] TOOL RESULT

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


## [2026-09-05T20:52:55.911Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n 1,80p tools/verify_check.py && echo ---- && python3 -c \"\nimport json\nd=json.load(open('data/verification/page-127.json'))\nprint(json.dumps(d['entries'][0],ensure_ascii=False)[:3000])\n\"",
 "description": "Inspect verify_check and example output"
}
```


### [2026-09-05T20:52:57.897Z] TOOL RESULT

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
----
{"entry": 0, "root": "Dhem", "verdict": "confirmed", "modern_form": "PIE *dʰemH- (LIV² *dʰmeh₁-) 'to blow, breathe; to smoke, raise dust'", "note": "Pokorny IEW 247-248 heads the entry 'dhem-, dhemə- \"stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben = düster, dunkel), wehen, blasen (hauchen = riechen)\"', so Nourai's language label (Indo-European) and his gloss 'to make vapor, raise dust' are an accurate short rendering of the German. Cheung (Etym. Dict. of the Iranian Verb, *damH³) writes the same root «PIE *dʰmeH- 'to blow' = LIV: 153 | Pok.: 247 f.»; Wiktionary reconstructs *dʰemH-. Watkins/AHD carries no dhem- root (its list goes dhembh- → dhen-¹), simply because no English word reaches it through Latin or Greek, so its silence is not a disagreement. Two weak spots in the chart: the Avestan node's gloss (node 1) and the name Damāvand (node 2), which Nourai's own source BQT:878 derives from a different root.", "note_fa": "ریشهٔ نمودار همان ریشهٔ هندواروپاییِ آغازینِ *dʰemH- «دمیدن، فوت کردن؛ دود و بخار برخاستن» است. پوکورنی در صفحهٔ ۲۴۷ کتاب خود آن را با معنای آلمانیِ «stieben, rauchen … wehen, blasen» آورده و برگردانِ کوتاهِ نورایی («بخار ساختن، گرد برانگیختن») با آن می‌خواند؛ چونگ نیز همین ریشه را *dʰmeH- «دمیدن» (LIV ۱۵۳) می‌نویسد. پس جعبهٔ ریشه، برچسبِ زبان و معنای آن درست است و ادعای نورایی در این حد پذیرفتنی است. تنها دو نقطهٔ سست در نمودار هست: معنایی که برای صورتِ اوستایی داده شده (گرهٔ ۱) و نامِ «دماوند» (گرهٔ ۲) که خودِ مأخذِ نورایی، یعنی حاشیهٔ معین بر برهان قاطع ص ۸۷۸، آن را از ریشهٔ دیگری می‌گیرد.", "sources": ["https://en.wiktionary.org/wiki/%D8%AF%D9%85%DB%8C%D8%AF%D9%86", "https://en.wiktionary.org/wiki/%D8%AF%D9%85"], "ref_check": [{"ref": "POK:247", "status": "supports", "note": "POK_01.txt (grep -n 'dbem-' → line 3513), IEW p.247: 'dbem-, dhemo- ,stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben == düster, dunkel), wehen, blasen (hauchen = riechen)'; the page continues 'Ai. dhámati ,bläst', av. daδmainya- …, npers. damīdan ,blasen, wehen', dam ,Atem, Atemzug''. Exactly the root box as drawn."}], "consulted": [{"src": "WLD", "where": "Bd. I 851 f. (WLD_Bd1 djvu line 53642)", "stance": "supports", "note": "'dhem-, dhemə- „stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben = düster, dunkel), wehen, blasen (hauchen = riechen)“. Bedeutungsumfang wie bei Wz. *dheu- „stieben“.' — the source Pokorny 247 abridges."}, {"src": "CHEUNG", "where": "s.v. *damH³ (CHEUNG.txt line 4670 ff.)", "stance": "supports", "note": "'*damH³ \"to blow, breathe; to swell\" … «PIE *dʰmeH- \"to blow\" > LIV: 153 | Pok.: 247 f.»'"}, {"src": "AHD", "where": "Watkins 1985, d-list (AHD_watkins1985.txt line 377)", "stance": "silent", "note": "the appendix runs 'dhembh-. To bury. … [Pok. (dhembh-), dhmbh- 248.] dhen-¹. To run, flow.' — no dhem- entry at all, since no English word descends from it via Latin/Greek."}, {"src": "IEC", "where": "Mann, d-section (grep 'dhem' in IEC.txt)", "stance": "silent", "note": "Mann has dhen
```


## [2026-09-05T20:52:58.163Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','MON','SOD','AHD','BRT','PHD','HRN','HUB','IEC','SYN','WLD','SKT','LEW','LAT','NYB','CHEUNG','ARY']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600])\n\"",
 "description": "Read refs_online entries"
}
```


### [2026-09-05T20:52:59.793Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b
LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf
CHEUNG null
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it
```


## [2026-09-05T20:53:08.324Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==424' POK_01.txt | head -70",
 "description": "Print Pokorny p.416"
}
```


## [2026-09-05T20:53:08.878Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==426' POK_01.txt | head -80",
 "description": "Print Pokorny p.418"
}
```


### [2026-09-05T20:53:10.241Z] TOOL RESULT

```
(Bash completed with no output)
```


### [2026-09-05T20:53:11.820Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:53:14.638Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in POK_01.txt POK_02.txt POK_03.txt POK_full.txt; do echo \"$f: $(awk 'BEGIN{RS=\"\\f\"} END{print NR}' $f) pages, $(wc -c <$f) bytes\"; done",
 "description": "Count POK pages"
}
```


### [2026-09-05T20:53:16.645Z] TOOL RESULT

```
POK_01.txt: 363 pages, 981836 bytes
POK_02.txt: 433 pages, 1137861 bytes
POK_03.txt: 429 pages, 1170809 bytes
POK_full.txt: 1 pages, 3971883 bytes
```


## [2026-09-05T20:53:20.201Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=71 && NR<=73 {print \"=== leaf\",NR,\"===\"; print}' POK_02.txt | head -120",
 "description": "Print POK_02 leaves 71-73"
}
```


### [2026-09-05T20:53:21.941Z] TOOL RESULT

```
=== leaf 71 ===
n';    ahd.  *goto,    gota,    mhd.    g'öt{t)e,   got[t)^ .Pate,  Patina
WP.  I  529  f.,  Trautmann  367;    ausführl.  Lit.  bei  Feist  227  f.
ghauo-  ,falscb.  erlogen'??
Lat.  haud  Begriffsnegation  .nicht',  vielleicht  aus  ^hauidom  >  *Jmudom (>  haud  wie  nihilum  >  nihil),  neutr.  Adjektiv  .falsch  (wäre  es)' ;
air.  gäu,  gäo,  gö  f.  .Unrichtiges.  Lüge',  gü-forcell  .falsches  Zeugnis* mcymr.  geu,  ncymr.  gau  .falsch'.  Subst.  .Lüge',  corn.  gow  m.  ds..  bret gaou  ds. ;  abgeleitet  mcymr.  geuawc,  ncymr.  euog  .schuldig'.  z^;
Ganz  zweifelhafte  Gleichung.  Wenn  die  kelt.  Formen  mit  äu  anzusetzen sind,  könnten  sie  auf  idg.  *göu-  (zu  geu-  .biegen'.  S.  393)  zurückgehen. Vgl.  zum  Vokalismus  Pokorny  ZceltPh.  11.  19.  zur  Bedeutung  Frisk  Göte-' borgs  Högsk.  Ärsskr.  41  (1935),  3.  Abt..  S.  11.  ^
WP.  I  530.  WH.  I  636  f..  869.  '
gMem-,  ghdom-,  Gen.-Ablativ  gh{d)m-es  ,Erde,  Erdboden';  aus  der Schwundstufe  entwickelte  sich  ghm-,  von  wo  der  einfachere  Anlaut gh-  auch  auf  hochstufige  Formen  übergriff  (über  die  ai.  Anlaute  jm-, gm-  neben   ksm-  vgl.  Johansson  Xenia  Lideniana  1912,  S.  116 — 126).
Vgl.  zum  Anlaut  noch  Wackernagel  Ai.  Gr.  I  129,  241,  §§  109,  209  by, III  241  ff.,  Schwyzer  Gr.  Gr.  I  326,  631,  10,  Benveniste  BSL.  38,  139  ff., Specht  Dekl.  241.
Ai.  St.  ksam-,  Nom.  Sg.  ksdh  (=  av.  zä)  f.  ,Erde,  Erdboden'  (Akk. k§äm  =  av.  zqm ;  Lok.  ksdmi  und  *ksäm,  wenn  ksdman  aus  dieser  Form mit  Postposition  *en  ,in'  zu  erklären  ist,  vgl.  ai.  pdri-jman  , rings  auf  der Erde' ;  Instr.  jmä ;  Gen.  jmdh,  sekundär  gmdh,  ksmdh) ;  ksdmya-h  ,auf  der Erde  befindlich,  irdisch';
av.  zä,  Akk.  zam,  Lok.  zdme,  Gen.  zdmö  ,Erde,  Erdboden';
gr.  x&tbv  f.  ,Erdboden'  (*x^a>u ;  danach  mit  v  auch  Gen.  xd-ovog,  xd^öviog ,unterirdisch'  usw.),  xaixal  ursprüngl.  ,zur  Erde  hin',  dann  auch  ,auf  der Erde'  (bis  auf  die  andere  Vokalstufe  =  apr.  semmai  ,nieder'  und  vermut- lich auch  =  lat.  huml  ,zu  Boden'),  xai.iaC,s  ,zur  Erde  nieder',  xf^l-^V^og , niedrig',  %d-aixal6g  ,niedrig'  ( :  lat.  humilis),  vielleicht  veo-xi-^os  .neu,  uner- hört  (auf   der   Erde?)';
phryg.  ^s^sXcü  (thrak.  IsfxiXrj)  ,Mutter  Erde'(?),  auch  phryg.  l^sfisXsv ßccQßagov  divögdTtoöov  Hes.  (vgl.  russ.  celovek  ,Mensch'  und  ,Diener') ;  Fdav  Ma ,Xd^(bv  Mä'  kann  echt  phryg.  sein  (idg.  e  >  phryg.  «),  gd-  :  z-  wie  ai. ksäh  :  av.  zä]
alb.  dhe  ,Erde'  (==  x^cjv) ',  vgl.  gr.  Jrj^rjTrjg,  dor.  Jä^&XTiQ,  thess.  Ja^^d- irjQ,  äol.  Ja)fxdTr]Q',  illyr.  Jw-,  Ja^-  (Pisani  IF.  53,  30,  38)  aus  idg.  *gd;hö, bzw.  Vokat.  *gdhom;  über  Ja^ila,  Beiwort  der  Demeter,  s.  WH.  I  321;
415
lat.  humus  (aus  *homos)  ,Erde,  Erdboden',  wahrscheinlich  Umformung' eines  alten  Kons. -St.  *§hom-]  daher  auch  f.  wie  xdthv]
=== leaf 72 ===
  humilis  , niedrig' ( -vd-af^ccXög)  ]  im  Osk.-Umbr.  * homi-teros,  -temos  als  Kompar.  Superl.  vom Lok.  *homi  ,unten'  (:  ai.  ksdmi)  :  osk.  hu[n]truis  ,inferis',  huntrus  ,inferös'; umbr.  hutra,  kontra  ,lnfrä^  Abi.  hondomu  ,infimö';  umbr.  hondu  ,pessum- datö'  aus  *hon(d)-töd]  über  lat.  hümänus  s.  unten;
air.  du,  Gen.  don  ,Ort,  Stelle'  (Pedersen  KG.  I  89,  s.  auch  unten  zu duine]  die  Entw.  von  ghd  zu  d-  stimmte  zu  t  aus  -kp-  in  art  ,Bär'  aus /kpos]  n  statt  m  wie  in  '^d^övoq  aus  der  Vorstufe  *dön  —  aus  *  dörrt  —  von da  verschleppt);
lit.  itemej  lett.  zeme,  apr.  same,  semme  ,ErdeS  semmai  ^nieder'  (:  xaiialy s.  oben),  lett.  zem  ,unter*  (wohl  Verkürzung  des  Lok.  zeme);  lit.  zemas, lett.  z^ms  ^niedrig';
aksl.  zemlja  ,Erde';  dazu  auch  aksl.  zmhja  , Schlange'  (,auf  der  Erde kriechend,  x-^^H-^^og'),  zmbjb  , Drache'.
Dazu  Worte  für  ,Mensch'  als  , Irdischer': -  lat.  homö,  -inis  ,Mensch',  alat.  hemö  (auch  in  nemo  , niemand'  aus  *ne- Äemö),  Akk.  hemönem]  zu  humus  wohl  hümänus  , menschlich',  mit  unklarem Vokalismus  (*hoim-  würde  zum  oi  des  air.  PI.  doini  , Menschen'  stimmen, falls  hier  alter  Diphthong  vorläge,  aber  für  ein  idg.  *gdhoim-  fehlt  jede Wahrscheinlichkeit;  s.  auch  unten);  osk. -umbr.  *homön-  (Ablautstufe  *ghom- wie  humus,  gegenüber  lat.  hemön-  oder  einzeldialektischer  Umlaut  aus *hemün-),  osk.   kumuns  ,homines',  umbr.   homonus  ,hominibus';
got.  guma,  aisl.  gumi,  ags.  guma,  ahd.  gomo  , Mensch,  Mann',  nhd.  in Bräuti-gam.  (idg.  *ghjnon-  oder  *gh^mon-)',
'  lit.  (alt)  zmud  (Dauksa  m.  Akk.  zmünj)  , Mensch',  heute  zmogüs,  zmogus (^-Formans  wie  in  aksl.  mg-zb)  , Mensch',  apr.  smoy  (leg.  smoa?),  weiter- gebildet apr.  smunents  m.  , Mensch',  smonenawins  ds.,  und  smüni  f.  , Person', lit.  zmonä  f.  ,Frau',  zmönes  PI.  m.  , Menschen'  (Akk.  PL  zmönis  dial.  aus idg.  ghmön^ns).
Pedersen  (KG.  I  69,  89,  116,  173)  stellt  hierher  auch  air.  duine,  cymr. dyn,  corn.  bret.  den  ,Mensch',  urk.  *donio-  aus  *ghdomio-  =  x^^^i-og,  ai. ksamya-h]  das  wäre  allerdings  der  einzige  Beleg  für  kelt.  ni  aus  mi;  es könnte  Übertragung  des  n  aus  dem  Paradigma  *dön  ,Ort,  Stelle'  (s.  oben) erwogen  werden.  Doch  wäre  dann  der  PI.  air.  doini,  nir.  daoine  ,Menschen, Leute'  (echter  Diphthong)  von  duine  zu  trennen ;  weit  wahrscheinlicher wird  doini  als  *dheuenio-  oder  *dhouenio-  und  duine  usw.  als  tiefstufiges *dhuniO'  mit  got.  diwans  , sterblich'  verbunden  (s.  *dhuen-  unter  dkeu- ,sterben') ;  unwahrscheinlich  Borgström  NTS.  12,  83  f. ;
toch.  A  ^om  ^Bursche,  Jüngling^,  B  saumo,  PI.  ^ämna  ^Mensch^  (:  lat. hemönem) ;  s.  Pedersen  Tochar.  107  f. ;
416  •
hitt.  te-e-kan  (tegan),  Gen.  tagnäs  ,Er
=== leaf 73 ===
de^  und  toch.  A  tkam,  Gen.  tkanU B  kern  ds.  werden  durch  Metathese  aus  *g{e)dhom-,  *gh{e)dhom  (Pede.sen Group.  41  f.),  dieses  aus  idg.  *dh(e)ghom  (Kretschmer  Gl.  20,  66  f.)  erklärt- dagegen  mit  beachtlichen  Gründen  Benveniste  Mel.  Van  Ginneken  193 ff/.: eine  Wurzel  *dhegh-  setzt  auch  Specht  Dekl.  241  an ;  ich  würde  die  hitt! und  toch.  Formen  mit  Benveniste  lieber  fernhalten.  :^.
WP.  I  662  ff.,  WH.  I  654  f.,  663  ff.,  869,  Trautmann  369.  #;
ghäies  (schwundst.  ghdis?),  vereinfacht  (?)  zu  ghSes,  ghißs,  ghes  ,gestemV ~Ai.  liydh  ,gestern'  (ghies),  hyastana-h  ,gestrig',  av.  zyö,  apers.  diya{ka\ pers.  di{g)]
gT.  eleisch  asg-ög'  x^k  Hes.  (aus  *xt£S,  idg.  ghies?);  gr.  x^k  {*9hdes), h^k  (nach  iytsLvog  :  y,eTvog,  selbständige  Partikel  oder  Vorschlagsvokal, s.  oben  S.  283  und  Schwyzer  Gr.  Gr.  I  413,  Lejeune  Traite  182);  x^i-^dg, adverb.  x^t^a  , gestrig',  nach  Schwyzer  Gr.  Gr.  I  351  aus  X-^k-{-*dtd zu  ai.  a-dyä  ,heute'  (Instrum.  von  idg.  *dios  ,Tag';  fehlt  oben  S.  183),  mit vortoniger  Schwächung  des  e  zu  i,  nach  Specht  KZ.  68,  205  aus  *ghdis >  ghis  mit  Adverbialsuffix  (wie  in  gr.  xQvß-da) ;  Xi9-£0't)'0g  , gestrig' ;
alb.  dje  ,gestern',  dial. , morgen'  (*ghes),  djetliine  ds.,  para-dje  ,vorgestern';
lat.  her%,  her^  , gestern',  hesternus  ,gestrig'  (aus  *hestrinos  mit  -tro-  wie in  germ.  *gestra-)]
air.  in-de  (*gdies),  cymr.  doe,  acorn.  doy,  ncorn.  de,  mbret.  deck,  nbret. deac'h  , gestern'  (die  brit.  Formen  aus  *gdiies)\  cymr.  neithhür  usw.  ,gesteni^ abend'  vielmehr  aus  *nokti  -\-  cymr.  hwyr  ,spät'  (Lw.  aus  lat.  serus) ;
got.  gistra-dagis  ,morgen',  ags.  geostra,  wsächs.  giestran-dxg,  nordhumbr/ gioster-dxg  , gestern',  ahd.  kestre,  gesteron,  gesteren  ^gestern';  dehnstufig anord.  i  gaer  {*gez-),  i  gjar  (Noreen  Aisl.  Gr.*  §  72,  263  a  1);  s.  darüber Specht  KZ.  68,  202  f.
WP.  I  664,  WH.  I  642  f.,  869,  Schwyzer  Gr.  Gr.  I  326,  631,  10,  Specht KZ.  68,  201  ff.
ghdü-  (oder  ghiü-?)  ,Fisch'.
Arm.  jukn  , Fisch'  (Erweiterung  wie  in  mu-kn  ,Maus');
gr.  ix^vg,  -vog  (*ghdüs)  ,Fisch'  {l-  ist  Vokalentwicklung  wie  in  hzlvog , Gabelweihe' :  arm.  ein  , Falke',  idg.  kplno-)]
ghduu-:  lit.  zitvis  (Gen.  PL  zuviD  f.,  lett.  zuvs,  zivs  m.  ds.;  dazu  die  Verba ostlit.  züsta,  zuvOj  züti  , fischen';
Gutturalsuffix:  apr.  suckis  m.  (Akk.  PI.  suckans)  ,Fisch'  (lit.  zuk-  in zük-mistras  ,Fischmeister',  zuk-sparnis  ,Fischaar',  zuklys  ,Fischer') ;  dazu ferner  lett.  zutis  m.  , Aal' ;  lit.  zvejys  m.  ,Fischer',  lit.  zvejöti,  lett.  zvejv,
```


## [2026-09-05T20:53:44.282Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=74 && NR<=75 {print \"=== leaf\",NR,\"===\"; print}' POK_02.txt | head -90",
 "description": "Print POK_02 leaves 74-75"
}
```


## [2026-09-05T20:53:45.805Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"ghdhyes\\|ghes-\\b\\|yesterday\" AHD_watkins1985.txt | head -20; echo ====; grep -n -i \"^ghē-\\|ghē-\\.\\|ghē- *To release\\|To release, let go\" AHD_watkins1985.txt | head -20",
 "description": "Grep AHD Watkins for ghdhyes and ghe"
}
```


### [2026-09-05T20:53:46.168Z] TOOL RESULT

```
=== leaf 74 ===
M ,fischen',  itvynas  m.  , Fischschuppe',  \Qtt.  zvini  m.  PL  ,Fischschuppen';  apr. sucka-ns  neben  Ix^g,  wie  lat.  sucu-la  neben  süs,  anord.  askr  neben  lit.  uosis.
417
Zur  Anlautfrage  {ghd  oder  (jhi'>)  vgl.  Schwyzer  Gr.  Gr.  I  325;  gleich- artig' ist  besonders  x^(^^'  '•  ^^^^^^>  und  eine  Parallele  mit  k-  bietet  hAxlvog:  ein. Kein  ganz  sicherer  Hinweis  auf  *gh,i'  ist,  da  in  seiner  Zugehörigkeit etwas  zweifelhaft,  der  Fischname  alt.  schwed.  gius,  nschwed.  gas  ,Perca Lucioperca^  nhd.  dial.  giesen  ,Cyprinus  cephalus^  und  alt.  schwed.  fiska- qiusen  ,ein  Raubvogel,  Falco  haliaetus',  worin  ein  *gji(se  , Fischer'  stecke.
WP.  I  664,  Trautmann  373,  Schwyzer  Gr.  Gr.  I  325,  413;  zum  idg.  d ycr\,  zuletzt  Lejeune  Traite  de  Phonetique  grecque  S.  31  f.
p-üze-,  g'^o-  u^d  ähnliche  enklitische  Partikeln  zur  Verstärkung  des  vorher- gehenden Wortes.  Es  scheinen  zwei  Gruppen  geschieden  werden  zu müssen,  einzelsprachlich  aber  z.  T.  die  eine  an  Stelle  der  andern getreten  zu  sein:  1.  gJie,  gho,  2.  mit  palatalem  Gutt.,  der  in  den  europ. Sprachen  als  g,  im  Ar.  als  gh  erscheint  (wie  in  den  Fällen  wie  gr.  yiwg: ai.  hdnuh),  also  eine  von  der  normalen  sog.  Media  aspirata  verschie- dene Artikulationsart  aufwies,  und  dem  Vokal  i  oder  e.
1.  -ghe,  'gho:
ai.  gha  {*gho),  ha  {*ghe)  hinter  Negation  (nd  glia),  Personalpron.  (z.  B. vaydm  gha),  dem  5o/^o-Pron.  (sd  gha^  sd  ha)^  dem  Fragepron.  (z.  ß.  kdrii ha),  dem  Relativpron.  (yö  gha^  yö  ha),  auch  hinter  andern  Wortarten;  ai. hdnta  ^wohlan,  auf,  da  nimm,  sieh  da^;
umbr.  -hont  (z.  B.  era-hunt  ,eädem^),  vgl.  auch  lat.  hic  , dieser^  aus *gho  oder  *ghe  -f-  */t-e;
cymr.  a{g)  ,mW  aus  *ad-ghe-j    s.  oben  S.  3;
aksl.  -gOf  -ze  hinter  Negation  (ni-ze  ,neque^,  nejedim  ze  ,ne  unus  quidem, ovösig']  vgl.  auch  aksl.  7ieze,  serb.  nego  ,als'  beim  Komparativ  und  serb. nego  ^sondern,  aber^,  cech.  nez(e)  ,doch^,  wo  ne-  eher  der  Negation  als  der positiv  weisenden  Bed.  des  Pron.-St.  ne-  entsprungen  ist),  hinter  dem Relativpron.  (ize),  dehnstufig  {*gho)  osorb.  kdy-ha  ,wann  denn'  (u.  dgl.; Berneker  316);
lit.  -gu  {*ghö),  -gi  (dies  mit  dem  Vokal  i  der  2.  Gruppe)  in  negl,  neigt, negü  , nicht',  hinter  Pers.-Pron.  (z.  B.  tu-gu,  tu-gi  ,ovye'),  alit.  auch  -ga,  -ge, dem  so/^o-Pron.  (z.  B.  tie-gi),  dem  Fragepron.  (kaip-gi  ,wie'),  -gu  auch Fragepartikel  (vgl.  auch  alit.  an-gu  ,ob',  apr.  an-ga  ,ob'),  apr.  beggi  ,denn', käigi  ,wie',  neggi  ,auch  nicht,  noch',  niqueigi  ,nimmermehr';  gr.  ovx^ s.  unte
=== leaf 75 ===
n.
2.  -i(b)^:
in  ai.  hi,  av.  zl  hervorhebende  Partikel  (nd  hi,  nahi,  av.  nöit  zl]  ai.  kdr-hi jwann?',  tdr-hi  , damals'  u.  dgl.),  hinter  dem  ersten  Wort  des  Satzes  ,denn  ja';
27
418
gr.  oi-xh  l^T%i  ,nicht',  Jj-xi  ,wo',  vai-xi  ,jawolil,  allerdings'  {--^ -y-,  vgl.  unten  /£,  vermutlich  durch  Kreuzung  mit  einer  Partikel 1.  Gruppe);
lat.  *ne-gi  (nach  Holthausen  KZ.  47,  309  =  as.  nee  ,und  nicht*),  vq] o-esetzt  durch  negotium^  ursprgl.  Satzkompositum  negotium  est  (vgl.  ~ ötium  est  bei  Terenz)  und  negäre  (vgl.  nhd.  verneinen,  bejahen)'^
klr.  bulg.  serb.  -2i  hinter  Personalpron.
in  o-r.  i^€-y6  =  got.  m^-^,  ahd.  mi-h  =  arm.  25  ,me'  (zunächst  aus  *in-^\ iyo)  ys,  eyw-ys,  av  ys,  got.  pu-k,  si-k,  ahd.  di-h,  si-h;  nach  dem  so//o-prQj. 6'  /£,  nach  dem  Relativpron.  oaaa  ys,  ovTiva  ys,  ferner  yh,  dor.  böot^^ yä  auch  hinter  andern  Wortarten.  Im  Balt.  sowie  auch  (außer  in  der  mit X  vokalisierten  Form)  im  Slav.  ist  der  Guttural  der  1.  Gruppe  herrschend geworden,  wie  auch  in  gr.  -^t;
ven.  me-xo  ,mich'  hat  das  o  von  e^o  ,ich'  bezogen;
toch.  Verstärkungspartikel  A  —  k^  B  —  /c(e)  aus  *-^Äe  oder  -ghe  (vgh Pedersen  Toch.  136);
hitt.  am-mu-uk  {ammuk)  ,mich',  tu-uk  (tuk)  ,dich':  got.  puk  (*tu-ge) usw.,  s.  Pedersen  Hitt.  73  f.,  166  f.
WP.  I  541  f.,  WH.  I  644,    Schwyzer  Gr.  Gr.  I  606,  624.  :^
I.  ghe-,  ghei-  A.  ,leer  sein,  fehlen';  B.  ,verlassen,  fortgehen',  dann  , gehen'; vielleicht  zu  ghe-,  ghei-  ,gähnen,  klaffen'  (vgl.  ,gähnende  Leere');  aus  < ,klaffend  abstehen'  kann  sich  auch  ,fortgehen'  entwickeln.  ^Wt
Mit  der  Bed. -Färbung  B:  -^
Ai.  jdhäti  ,verläßt,  gibt  auf  {jahimah,  Imper.  jahlM,  Aor.  ahät,  ahäyij Partiz.  lilnd-K)jjihlte  ,geht,  fährt  auf,  hlyate  ,wird  verlassen,  bleibt  zurück'; häni-h  f.  ,Mangel;  das  Fahrenlassen'  (yihäyas-  ,leerer  Raum'  wegen  des Präfixes,  das  aach  in  vi-kä-  ,auseinanderklaffen') ;  vgl.  S.  427  ;
av.  zazämi  ,ich  entlasse  aus',  mit  avu-  ,entfernen,  verscheuchen',  mit «pa-  und  frä-  ,herzulassen,  herzuführen';  ä-zä-  ,herangehen',  uz-zä-  ,auf- springen,  sich  aufrichten'  {uzayantö  Partiz.  Nom.  PL);
gr.  hom.  yf.Lx&v(x}  (*xtxav/w),  att.  ^tyxcivu)  {*gh9-n-u-),  Inf.  Präs.  hom.  xi^ij- ^evai,  Partiz.  Präs.  xtx«/s, erreichen,  einholen,  treffen,  erlangen,  einnehmen'; mit  formantischem  -d- :  gr.  x^^o^iai,  Fut.  ep.  /«ö-ö-o^a/,  i^or.  ep.  ^adat^/ti^v ,weiche,  fliehe,  lasse  ab',  d:vaxaQ(o  tr.  ,dränge  zurüc
```


### [2026-09-05T20:53:46.261Z] TOOL RESULT

```
Exit code 1
382:blind: TYPHUS; TYPHLOSOLE. 11. Extended form *dheubh., “beclouded in the senses,” in suffixed o-grade form *dhoubh-o- in: a. Germanic *daubaz in Old English déaf, deaf: DEAF; b. nasalized form *dhu-m-bho- in Germanic *dumbaz in Old English dumb, dumb: pumps; c. Germanic *diibén- in Old English *dife, dove (< “dark-colored bird”): DOVE!. 12. Extended zero-grade form *dhwel- in: a. Germanic *dwelan, to go or lead astray, in Old English dwellan, to deceive (but influenced in sense by cognate Old Norse dvelja, to tarry): DWELL; b. Germanic *dulaz in (i) Old English dol, dull: DoL- DRUMS (ii) Middle Low German dul, dull: (DOLT), DULL. 13. Extended zero-grade form *dhwes- in Greek suffixed form *th(wjes-es-, smoke, whence Greek *th(w)es-es-yon, becoming theion, brimstone, sulfur: THIO-, THION-. 14. Perhaps Old English docce, dock (< “dark-colored plant”): Dock‘. 15. Perhaps Irish did, pipe: DUDEEN. [Pok. 4. dheu- 261.] dheu-2. To flow. Germanic *dauwaz, dew, in: a. Old English déaw, dew: DEW; b. compound *melith-dauwaz, “honeydew” (see melit-). [Pok. 1. dheu- 259.] dheu-’. To become exhausted, die. 1. Suffixed o-grade form *dhou-to- in Germanic *daudaz in Old English déad, dead: DEAD. 2. Suffixed o-grade form *dhou-tu- in Germanic *dauthuz in Old English déath, death: DEATH. 3. Suffixed o-grade form *dhow-yo- in Old Norse deyja, to die: DIE}. 4. Suffixed extended zero-grade form *dhwi-no- in Germanic *dwinan in Old English dwinan, to diminish, languish: DWINDLE. [Pok. 2. dheu- 260.] dheub-. Deep, hollow. 1. Germanic *deupaz in Old Eng- lish déop, deep: DEEP, DEPTH. 2. Germanic expressive denominative *duppjan in Old English dyppan, to im- merse, dip: pip. 3. Parallel root form *dheubh- in Ger- manic *deub-, *dub- in verb *diibjan in Old English dyfan, to dip, and difan, to sink, dive: pivE. [Pok. dheu-b- 267.] dheubh-. Wedge, peg, plug. Germanic *dub- in: a. Old English dubbian, to tap, strike (with a sword): DUB); b. Low German dubben, to hit: puB?; c. Germanic di- minutive *dub-ila- in Middle Low German dével, peg: DOWEL. [Pok. dheubh- 268.] dheugh-. To produce something of utility. 1. Germanic extended form *duht- in Old English dyhtig, dohtig, strong (< “useful”): DOUGHTY. 2. Suffixed form *dheugh- os- in Greek teukhos (< *theukhos), gear, anything produced, tool: HEPTATEUCH, HEXATEUCH, PENTA- TEUCH. [Pok. dheugh- 271.] dhghem-. Earth. 1. Suffixed zero-grade form *(dh)ghm-on-, “earthling,” in Germanic *gumén- in Old English guma, man: BRIDEGROOM. 2. O-grade form *dhghom- in Greek khthon, earth: CHTHONIC; AUTOCH- THON. 3. Zero-grade form *dhghm- in Greek khamai, on the ground: CHAMAEPHYTE, CHAMELEON, CHAMOMILE, GERMANDER. 4. Suffixed o-grade form *(dh)ghom-o- in Latin humus, earth: HUMBLE, (HUMILIATE), (HUMILITY), HUMUS; EXHUME, INHUME, TRANSHUMANCE. 5. Suffixed o-grade form *(dh)ghom-on-, “earthling,” in: a. Latin homé, human being, man: HOMAGE, HOMBRE!, HOMINID, HOMO!, HOMUNCULUS, OMBRE; BONHOMIE, HOMICIDE; b. (in part) Latin himdnus, human, kind, humane: HUMAN, (HUMANE). 6. Suffixed form *(dh)ghem-ya in Russian zemlya, land, earth: SIEROZEM, ZEMSTVO. 7. Full-grade form *(dh)ghem- in Persian zamin, earth, land: ZAMINDAR. [Pok. ghdhem- 414.] dhghut-. Fish. Greek ikhthus, fish: 1cHTHYO-. [Pok. ghdha- 416,] dhgh(y)es-. Yesterday. Suffixed (comparative) form (dh)ghes-ter- in Germanic “ges-ter- in Old English geo- stran, giestran, “yester-”: YESTER-, (YESTERDAY). [Pok. ghdhies 416.] dhgvhei-. To perish, die away. Zero-grade form *dhgvhi- in Greek phthinein, to die away: PHTHISIS. [Pok. gthdhei(a)- 487.)
(eval):1: === not found
```


## [2026-09-05T20:53:52.795Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o \"gh[eéè]-[^ ]* *To release[^]]*\\]\" AHD_watkins1985.txt | head; echo ====; grep -n -o \".\\{80\\}heres.\\{200\\}\" AHD_watkins1985.txt | head -5; echo ==== ; grep -n -o \".\\{300\\}HEREDITY.\\{200\\}\" AHD_watkins1985.txt | head -5",
 "description": "Grep AHD for ghe- release and heres"
}
```


### [2026-09-05T20:53:52.998Z] TOOL RESULT

```
Exit code 1
510:ghé-. To release, let go; (in the middle voice) to be released, go. Contracted from *ghea-. 1. Germanic vari- ant form *gaian in Old English gdn, to go: GO; AGO, FOREGO!, FoRGO. 2. Suffixed form *ghé-ro- in Latin hérés, heir (? < “orphan” < “bereft”):; HEIR, HEREDITA- MENT, HEREDITY, HERITAGE; INHERIT. 3. Suffixed o-grade form *ghé-ro-, “empty space,” possibly in: a. Greek khéros, place, country, particular spot: CHO- ROGRAPHY; b. Greek denominative khorein, to move, go, spread about, make room for: -CHORE; ANCHORITE. 4. Perhaps suffixed zero-grade form *gha-l- in Greek khalan, to slacken, let down (but this is more likely of unknown origin): CALANDO, CHALONE; ACHALASIA. 5. Suffixed zero-grade form *gho-t(w)d- in Germanic *gatwon-, a going, in Old Norse gata, path, street: GAIT. [Pok. ghé- 418.]
(eval):1: === not found
```


## [2026-09-05T20:54:04.421Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport json;d=json.load(open('../refs_online.json'));print(d['KLN']['page_offset']);print(d['KLN'].get('lookup_hint'));print(d['MON'].get('page_offset'));print(d['MON'].get('lookup_hint'))\n\"",
 "description": "KLN and MON offsets"
}
```


## [2026-09-05T20:54:05.303Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"yester\" KLN_1966.txt | head -20",
 "description": "Grep Klein for yester"
}
```


### [2026-09-05T20:54:06.368Z] TOOL RESULT

```
KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
None
Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).
```


### [2026-09-05T20:54:06.413Z] TOOL RESULT

```
17682:hestemal,  adj.,  of  yesterday.  —  Formed  with  adj. suff.  -al  fr.  L.  hesternus,  ‘of  yesterday’,  which stands  for  *hestrinos  and  is  cogn.  with  OI. hyaslanah,  Gk.  -/fttavjoq,  ‘of  yesterday’.  L. hesternus  derives  fr.  heri,  ‘yesterday’,  as  OI. hyastanah  derives  fr.  OI.  hyah,  ‘yesterday’,  Gk. X&eotvo?  fr.  of  s-m-  See  yester-.
24128:moderate,  tr.  v.  —  ME.  moderaten,  fr.  L.  modera¬ tus,  pp.  of  moderari.  See  moderate,  adj . moderation,  n.  —  ME.  moderacion,  fr.  MF.  ( =  F.) moderation,  fr.  L.  moderationem,  acc.  of  mode- ratio,  ‘moderating’,  fr.  moderatus,  pp.  of  mode¬ rari.  See  moderate,  v.,  and  -ion. moderator,  n.  —  ME.  moderatour,  fr.  L.  mode¬ rator,  gen.  -oris,  ‘manager,  ruler,  director’,  lit. ‘he  who  moderates’,  fr.  moderatus,  pp.  of  mode¬ rari.  See  moderate  and  agential  suff.  -or. modern,  adj.  —  F.  moderne,  fr.  Late  L.  modernus, ‘modem’,  formed  with  suff.  -e-rnus  fr.  L.  modd, ‘just  now’,  which  is  prop.  abl.  of  modus,  ‘meas¬ ure’,  and  lit.  means  ‘by  measure' ;  see  mode.  For the  formation  of  Late  L.  modernus  fr.  L.  modd cp.  L.  hesternus,  ‘of  yesterday’,  fr.  heri,  ‘yester¬ day’,  hodiernus,  ‘of  today’,  fr.  hodie,  ‘today’. Cp.  hesternal,  hodiernal;  cp.  also  diurnal,  noc¬ turnal.
```


## [2026-09-05T20:54:10.697Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^yester\" KLN_1966.txt | head; echo ====; grep -n -o \"yester-,.\\{900\\}\" KLN_1966.txt | head -3",
 "description": "Grep Klein yester- entry"
}
```


## [2026-09-05T20:54:11.845Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=890 && NR<=896 {print \"=== leaf\",NR}' KLN_1966.txt; echo; grep -n \"1762\" KLN_1966.txt | head",
 "description": "Locate KLN page 1762"
}
```


### [2026-09-05T20:54:12.297Z] TOOL RESULT

```
Exit code 1
(eval):1: === not found
```


### [2026-09-05T20:54:14.002Z] TOOL RESULT

```
=== leaf 890
=== leaf 891
=== leaf 892
=== leaf 893
=== leaf 894
=== leaf 895
=== leaf 896

16179:Derivative:  girth,  tr.  v.,  to  gird, gisarme,  n„  battle-ax  with  a  long  shaft  carried by  foot  soldiers  in  the  Middle  Ages.  —  ME., fr.  OF.,  fr.  OHG.  getisarn,  lit.  ‘weeding  iron’, fr.  getan,  ‘to  weed’,  and  isarn,  ‘iron’  (see  iron). OF.  gisarme  was  influenced  in  form  by  OF. arme,  ‘weapon’  (see  arm,  ‘weapon’), gismondite,  n.,  a  hydrous  calcium  aluminum  sili¬ cate  (mineral.)  —  Named  after  the  Italian  min¬ eralogist  Carlo  Giuseppe  Gismondi  (1762-1824), who  first  analyzed  it.  For  the  ending  see  subst. suff.  -ite.
36859:Derivative:  stoic-al-ly,  adv. stoichiometry,  also  stoechiometry,  stoicheiometry, n.,  the  art  of  determining  the  atomic  and  molec¬ ular  weights  of  the  elements  (chem.)  —  G.  Std- chiometrie,  lit.  ‘measurement  of  elements’,  coin¬ ed  by  the  German  chemist  Jeremias  Benjamin Richter  (1762-1807)  in  his  “Anfangsgriinde  der Stochiometrie  oder  Meflkunst  chemischer  Ele- mente”  (1792)  fr.  Gk.  axotyeiov,  ‘element’,  and -pexpla,  ‘a  measuring  of’.  The  first  element  is  a derivative  of  axotyoq,  ‘row,  line,  rank’,  which is  rel.  to  oxt/os,  ‘row,  line,  rank;  verse’,  oxe(- yetv,  ‘to  go;  to  march  in  order’ ;  see  stichic.  For the  second  element  see  -metry.
38420:Derivative:  telegrammat-ic,  adj. telegraph,  n.  —  F.  telegraphe,  lit.  ‘that  which writes  at  a  distance’,  coined  by  the  French  di¬ plomatist  Comte  Andrd-Fran?ois  Miot  de  M  dlito (1762-1841)  fr.  x7]Xe,  ‘far  off,  at  a  distance’,  and -Ypoupo?,  fr.  YP*9£tv,  ‘to  write’,  to  denote  the signaling  device  invented  by  the  Chappe  broth¬ ers  in  1792;  see  tele-  and  -graph.  (The  original name  given  to  this  device  by  its  inventors  was tachygraphe,  lit.  ‘that  which  writes  fast’.) Derivatives :  telegraph,  intr.  and  tr.  v.,  telegraph¬ er,  n.,  telegraphese  (q.v.),  telegraph-ic,  telegraph- ic-al,  adjs.,  telegraph-ic-al-ly,  adv.,  telegraph-ist, n.,  telegraph-y,  n.
```


## [2026-09-05T20:54:18.531Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} END{print \"leaves:\",NR}' KLN_1966.txt; grep -n \"yester\" KLN_1966.txt | head -20; echo ====1971====; grep -n \"yester\" KLN_1971.txt | head -20",
 "description": "Find yester in Klein files"
}
```


### [2026-09-05T20:54:20.225Z] TOOL RESULT

```
Exit code 1
leaves: 903
17682:hestemal,  adj.,  of  yesterday.  —  Formed  with  adj. suff.  -al  fr.  L.  hesternus,  ‘of  yesterday’,  which stands  for  *hestrinos  and  is  cogn.  with  OI. hyaslanah,  Gk.  -/fttavjoq,  ‘of  yesterday’.  L. hesternus  derives  fr.  heri,  ‘yesterday’,  as  OI. hyastanah  derives  fr.  OI.  hyah,  ‘yesterday’,  Gk. X&eotvo?  fr.  of  s-m-  See  yester-.
24128:moderate,  tr.  v.  —  ME.  moderaten,  fr.  L.  modera¬ tus,  pp.  of  moderari.  See  moderate,  adj . moderation,  n.  —  ME.  moderacion,  fr.  MF.  ( =  F.) moderation,  fr.  L.  moderationem,  acc.  of  mode- ratio,  ‘moderating’,  fr.  moderatus,  pp.  of  mode¬ rari.  See  moderate,  v.,  and  -ion. moderator,  n.  —  ME.  moderatour,  fr.  L.  mode¬ rator,  gen.  -oris,  ‘manager,  ruler,  director’,  lit. ‘he  who  moderates’,  fr.  moderatus,  pp.  of  mode¬ rari.  See  moderate  and  agential  suff.  -or. modern,  adj.  —  F.  moderne,  fr.  Late  L.  modernus, ‘modem’,  formed  with  suff.  -e-rnus  fr.  L.  modd, ‘just  now’,  which  is  prop.  abl.  of  modus,  ‘meas¬ ure’,  and  lit.  means  ‘by  measure' ;  see  mode.  For the  formation  of  Late  L.  modernus  fr.  L.  modd cp.  L.  hesternus,  ‘of  yesterday’,  fr.  heri,  ‘yester¬ day’,  hodiernus,  ‘of  today’,  fr.  hodie,  ‘today’. Cp.  hesternal,  hodiernal;  cp.  also  diurnal,  noc¬ turnal.
(eval):1: ===1971==== not found
```


## [2026-09-05T20:54:26.554Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=892 && NR<=894 {print \"--- leaf\",NR,\"---\"; print}' KLN_1966.txt | head -60",
 "description": "Print KLN leaf 892-894"
}
```


### [2026-09-05T20:54:28.638Z] TOOL RESULT

```
--- leaf 892 ---
  the  past  participle.
urea,  n.,  crystalline  compound  found  in  the  urine of  animals  (biochem.)  —  ModL.,  fr.  F.  uree,  a word  coined  by  the  French  chemist  Antoine- Franqois  de  Fourcroy  (1755-1 809)  frond, the  base of  the  word  urine  (q.v.)  )
Derivative:  ure-al,  adj.
urease,  n.,  an  enzyme  occurring  in  soybeans (bio¬ chem.)  —  Coined  fr.  urea  and  suff.  -ase. uredo,  n.,  a  kind  of  rust  (bot.)  —  L.  uredo,  ‘a blast,  blight;  a  burning  itch",  fr.  urere,  ‘to  burn’. See  combust.
uremia,  uraemia,  n.,  a  morbid  condition  of  the blood  (med.)  —  Medical  L.,  compounded  of oupov,  ‘urine’,  and  octpia,  ‘blood".  See  urine, hemal  and  1st  -ia.
Derivative:  urem-ic,  uraem-ic,  adj. ureter,  n.,  the  duct  conveying  urine  from  the  kid¬ neys  to  the  bladder  (anat.)  —  Medical  L.,  fr.  Gk. oup^-r^p,  usually  in  the  pi.  ouprj-vjpEi;,  fr. oupciv,  ‘to  pass  urine’,  fr.  oupov.  See  urine. Derivatives:  ureter-al,  ureter-ie,  adjs. ureteritis,  n.,  inflammation  of  the  ureter  (med.)  — Medical  L.,  formed  from  prec.  word  with  suff. -itis.
uretero-,  before  a  vowel  ureter-,  combining  form denoting  the  ureter.  —  Fr.  Gk.  oup7;-rr]p.  See
ureter.
urethan,  urethane,  n.,  ethyl  carbamate  (chem.)  — F.  urethane,  coined  by  the  French  chemist  Jean- Baptiste-Andrd  Dumas  (1800-84)  from  the  ab¬ breviation  of  the  words  urea  and  ether  and  suff. -an,  -ane.
urethra,  n.,  the  canal  through  which  the  urine  is discharged  from  the  bladder  (anat.)  —  Medical L.  urethra,  fr.  Gk.  ouprjflpa,  a  word  coined  by Hippocrates  fr.  oiipetv,  ‘to  pass  urine",  fr.  oSpov. See  urine  and  cp.  ureter.
Derivatives:  urethr-al,  adj.,  urethr-ism,  n. urethritis,  n.,  inflammation  ‘of  the  urethra"  (med.) —  Medical  L.,  formed  fr.  Gk.  o'jprjffpa  (see prec.  word)  with  suff.  -itis. urethro-,  before  a  vowel  urethr-,  combining  form denoting  the  urethra.  —  Gk.  oup'^Epo-.  'joprjflp-, fr.  ouprjffpa.  See  urethra, urethroscope,  n.,  an  instrument  for  the  examina¬ tion  of  the  interior  of  the  urethra  (med.)  —  Com¬ pounded  of  urethro-  and  Gk.  -crxo-'.ov,  fr. ay. oTrstv,  ‘to  look  at,  examine".  See  -scope, uretic,  adj.,  pertaining  to  urine;  urinary.  —  Late L.  ureticus,  fr.  Gk.  o’iprjTixis,  ‘of,  or  relating to,  urine",  fr.  oupciv,  ‘to  pass  urine".  See  urine and  adj.  suff.  -ic.
urge,  tr.  v.  —  L.  urgere,  ‘to  press,  drive,  urge", cogn.  with  Goth,  wrikan,  ‘to  persecute’,  OE.
urgence
UbUIIUU
wrecan ,  "to  drive,  expel;  to  avenge'.  See  wreak. Derivatives:  urge,  n.,  urgent  (q.v.),  urg-er,  n. urgence,  n.  —  MF.  (=  F.),  fr.  Late  L.  urgentia.
See  next  word  and  -ce.
urgency,  n.  —  Late  L.  urgentia,  fr.  L.  urgens,  gen. -entis.  See  next  w'ord  and  -cy. urgent,  adj.  —  ME.,  fr.  MF.  (=  F.)  urgent,  fr.  L. urgentem,  acc.  of  urgens,  pres.  part,  of  urgere. See  urge  and  -ent.
Derivatives:  urgent-ly,  adv.,  urgent-ness,  n.
-uria,  combining  form  meaning  ‘relating  to  urine (med.)  —  Medical  L.,  fr.  Gk.  -oupla,  fr.  odpov. See  urine  and  1st  -ia.
Uriah,  1)  masc.  PN.;  2)  in  the  Bible,  a  Hittite, husband  of  Bathsheba.  —  Prob.  of  foreign,  pos¬ sibly  Horite,  origin,  but  folk-etymol.  identified with  the  Heb.  name  Uriyyah,  which  lit.  means ‘flame  of  the  Lord’,  or  ‘my  light  is  the  Lord’. For  the  first  element  of  this  name  see  Urim  and cp.  Uriel,  for  the  second  see  Eljiah  and  cp.  words there  referred  to.
uric,  adj.,  pertaining  to  urine.  —  Formed  with adj.  suff.  -ic  fr.  Gk.  ohpov.  See  urine.
Uriel,  masc.  PN.  —  Heb.  Uri’el,  lit.  ‘flame  of God’  or  ‘my  light  is  God’.  See  next  word  and El.
Urim,  n.  pi.,  one  of  the  two  objects  attached  to the  breastplate  of  the  high  priest  (Bible).  —  Heb. urim,  of  uncertain  origin.  It  is  perh.  identical with  the  pi.  of  Sr,  ‘fire,  flame’,  fr.  dr,  v.,  ‘it  be¬ came  light’  (whence  also  or,  n.,  ‘light’),  which  is rel.  to  Aram.  Sr,  ‘to  give  light,  shine’,  Akkad. urru,  ‘light,  day’,  Arab,  awwara,  ‘he  kindled’, uwar,  ’heat,  glow’.  Cp.  Uriah,  prec.  word  and the  second  element  in  Melchior.  Cp.  also  the Septuagint  which  renders  urim  by  SrjXcoon;, ‘manifestation’  (fr.  StjXoGv,  ‘to  make  visible’), and  Symmachus,  who  translates  it  with  the word  ooTioiioi,  pi.  of  cpomapLo?,  ‘illumina¬ tion’  (fr.  90k.  gen.  cpUTo?,  ‘light’).  Cp.  Thum- mim.
urin-,  form  of  urino-  before  a  vowel, urinal,  n.  —  ME.  urynale,  fr.  OF.  (=  F.)  urinal, fr.  Late  L.  urinal,  fr.  L.  adj.  urinalis,  ‘relating  to urine’,  fr.  urina.  See  urine  and  adj.  suff.  -al. urinary,  adj.  —  Medical  L.  urindrius,  correspond¬ ing  in  sense  to  L.  urinalis,  ‘relating  to  urine’,  fr. urina.  See  urine  and  adj.  suff.  -ary. urinate,  intr.  v.  —  ML.  urinatus,  pp.  of  urinare, ‘to  pass  urine’,  fr.  L.  urina,  ‘urine’.  (L.  urindri means  ‘to  plunge  into  water’.)  See  urine  and verbal  suff.  -ate.
Derivatives:  urinat-ion,  n.,  urinat-ive,  adj. urine,  n.  —  ME.,  fr.  MF.  (=  F.),  fr.  OF.,  fr.  L. urina,  which  is  cogn.  with  OI.  var ,  vari,  water  , Avesiic  var,  ‘rain’,  Toch.  A  war,  water ,  Lith. hires,  Lett,  jura,  ‘sea’,  esp.  ‘the  Baltic’,  OPruss. wars,  ‘pond’,  OE.  wter,  ON.  ver,  ‘sea  ,  ON.  ur, ‘drizzling  rain’.  All  these  words  derive  fr.  I.-E. base  *wer-,  ‘water,  rain,  wet’ ;  cp.  urea,  ureter, urethra,  uretic,  and  the  first  element  in  aurochs. Fr.  I.-E.  *  wer-s-,  an  -^-enlargement  of  base  *wer-.
16BZ
derive  Gk.  oup£o>  (for  *  worse  yo  ),  oupelv,  ‘to pass  urine’  (whence,  with  back  formation, oJpov,  ‘urine’).  For  further  derivatives  of  base *  wer-s-  see  varsha.
urino-,  before  a  vowel  urin-,  combining  form meaning  ‘urine’.  —  Fr.  L.  urina.  See  prec.  word, urn,  n.  —  ME.  urne,  fr.  L.  urrta ,  ‘water  pot,  urn  , which  stands  for  *urcna  and  is  rel.  to  urceus, ‘pitcher’.  See  urceolate.
Derivatives:  urn,  tr.  v.,  urn-ful,  adj. uro-,  before  a  vowel  ur-,  combining  form  mean¬ ing  ‘urine’,  as  in  urology  (med.)  —  Gk.  oupo-, oup-,  fr.  oijpov,  ‘urine’.  See  urine, uro-,  before  a  vowel  ur-,  ‘tail-,  tail-like’,  as  in  uro- pod  (zool.)  —  Gk.  oGpo-,  oGp-,  fr.  oupa,  ‘tail’, which  stands  for  ‘operfa  and  is  rel.  to  oppop (for  I.-E.  •orsos),  ‘tail,  rump,  base  of  the  spine’, and  cogn.  with  OS.,  ON.,  OHG.,  MHG.  ars, ‘buttock’.  See  arse  and  cp.  the  second  element in  coenurus,  colure,  cynosure,  dasyure,  squirrel. Urocoptis,  n.,  a  genus  of  landsnail  (zool.) ModL.,  compounded  of  uro-,  ‘tail’,  and  Gk. xGttteiv,  ‘to  cut,  strike’,  which  is  rel.  to  xomc,
‘a  knife’,  xopipia,  ‘something  cut’.  See  comma  , and  cp.  Coptis.
Uropeltidae,  n.  pi.,  a  family  of  burrowing  snakes (zool.)  —  ModL.,  formed  with  suff.  -idae  fr. uro-,  ‘tail-’,  and  Gk.  tieXtt),  ‘a  small  shield’  (see pelta) ;  so  called  in  allusion  to  the  tail  which  ends in  a  shield.
uropod,  n.,  any  of  the  abdominal  appendages  of an  arthropod  (zool.)  —  Componded  of  uro-, ‘tail-’,  and  Gk.  7toup,  gen.  ttoSo?,  ‘foot’.  See
-pod.
-urous,  combining  form  meaning  ‘-tailed’.  — Formed  with  suff.  -ous  fr.  Gk.  oupS,  ‘tail’.  See uro-,  ‘tail-’.
Ursa,  n.,  name  of  either  of  two  constellations  (al¬ so  called  the  Great  Bear,  resp.  the  Little  Bear). —  L.  ursa,  ‘she  bear’,  fern,  of  ursus,  ‘bear’.  See Ursus  and  cp.  words  there  referred  to.
Ursidae,  n.  pi.,  a  family  of  large  carnivores  (zool.) —  ModL.,  formed  with  suff.  -idae  fr.  L.  ursus, ‘bear’.  See  Ursus.
ursine,  adj.,  pertaining  to  a  bear.  —  L.  ursinus,  fr. ursus,  ‘bear’.  See  Ursus  and  -inc  (representing  L. -inus).
arson,  n.,  the  Canada  porcupine.  —  F.  ourson, dimin.  of  ours,  ‘bear’,  fr.  L.  ursus.  See  Ursus. Ursula,  fern.  PN.  —  Fr.  L.  Ursula,  dimin.  of  ursa, ‘she-bear’.  See  Ursa  and  -ule.
Ursus,  n.,  a  genus  of  large  carnivores,  the  Euro¬ pean  brown  bear  and  its  allies  (zool.)  —  L.  ursus, ‘bear’,  which  stands  for  *urcsos  and  is  cogn. with  Gk.  apKTop  (also  ti.px.oq),  ‘bear’.  See  arc¬ tic  and  cp.  Ursa,  ursine,  urson,  Ursula,  Orson. Urtica,  n.,  a  genus  of  plants,  the  nettle  (hot.)
L.  urtica,  ‘nettle’,  lit.  ‘the  plant  that  causes  burn¬ ing’,  fr.  urere,  ‘to  bum’.  See  cumbust. Urticaceae,  n.  pi.,  the  nettle  family  (bot.)
ModL.,  formed  fr.  Urtica  with  suff.  -aceae. urticaceous,  adj.  —  See  prec.  word  and  -aceous.
urticaria,  n.,  nettle  rash  (med.)  —  Medical  L., formed  fr.  L.  urtica,  ‘nettle’.  See  Urtica. urticate,  tr.  v.,  to  sting  like  a  nettle.  —  ML.  urti¬ catus,  pp.  stem  of  urticare,  fr.  L.  urtica,  ‘nettle’. See  Urtica  and  verbal  suff.  -ate. urtication,  n.  —  ML.  urticatio,  gen.  -onis,  fr. urticatus,  pp.  of  urticare.  See  prec.  word  and -ion.
urubu,  n.,  the  black  vulture.  —  Port,  and  Sp. urubu,  a  Tupi  loan  word.
urus,  n.,  the  aurochs.  —  L.  urus,  a  Teut.  loan word.  Cp.  OE.,  OHG.  ur,  ‘bison’,  and  see aurochs.
us,  objective  case  of  we.  —  ME.  ous,  us,  fr.  OE. us,  rel.  to  OS.,  OFris.  us,  ON.,  Swed.  oss,  Dan. os,  MDu.,  Du.  ons,  OHG.,  MHG.,  G.  uns,  Goth. uns,  fr.  I.-E.  base  *ns-,  for  *nes,  *nds,  ‘we’; cogn.  with  OI.  nas,  ‘us’,  Avestic  na,  ‘us’,  Toch. A  nas,  Hitt,  nash,  ‘us’,  Hitt,  anzash,  ‘we’.  Alb. na,  ‘us’,  Gk.  dual  vci,  vffii,  ‘we  two’,  Lesbian ap.p.£,  Dor.aui  (for  *aapiE;  whence  Ion.  and  Att. ■qpEu;),  Avestic  ahma  (for  I.-E.  *nsme),‘ we’,  L. nos,  ‘we,  us‘,  OSlav.  ny,  ‘us’,  nasu,  ‘our’,  OPruss. nouson,  ‘our’.  Alb.  ne,  ‘we’,  Olr.  ni,  W.,  Co., Bret,  ni,  ny,  ‘we,  us’.  The  rough  spirit  in  Att. 7)!Z£i:<;  is  due  to  the  influence  of  ujisTg,  ‘ye, you’.  Cp.  our,  nostrum.
usable,  adj.  —  ME.,  fr.  MF.  (=  F.),  fr.  OF.  (= F.)  user.  See  use,  v.,  and  -able.
Derivative:  itsable-ness,  n. usage,  n.,  the  time  allowed  for  the  payment  of  a bill,  as  established  by  custom.  —  ME.,  fr.  OF. (=  F.)  usage,  fr.  us,  ‘usage’,  fr.  L.  us
--- leaf 893 ---
us.  See  use, n.,  and  -age.
usance,  n.  —  ME.  usaunce,  fr.  OF.  ( —  F.)  usance, fr.  user,  ‘to  use’.  See  use,  v.,  and  -ance. use,  n.  —  ME.  us,  use,  fr.  OF.  (=  F.)  us,  fr.  L. usus,  ‘usage,  custom,  use’,  fr.  usus,  pp.  of  uti,  ‘to use’,  fr.  OL.  oilier,  which  is  rel.  to  Oscan  uittiuf, ‘use’;  of  uncertain  origin.  Cp.  usage,  usance, usual,  usufruct,  usurp,  usury,  utensil,  utility, utilize,  abuse,  misuse,  peruse.
Derivatives:  use-ful,  adj.,  use-ful-ly,  adv.,  use¬ fulness,  n.,  use-less,  adj.,  use-less-ly,  adv.,  use¬ less- ness,  n.
use,  tr.  v.  —  ME.  usen,  fr.  OF.  (=  F.)  user,  fr. VL.  *usdre  (whence  also  It.  usare.  Proven?., Cat.,  Sp.,  Port,  usar),  freq.  of  L.  uti  (pp.  its  us), ‘to  use’.  See  use,  n.
Derivatives:  us-ed,  adj.,  us-ed-ly,  adv.,  us-ed- ness.  n.,  user  (q.v.)
user,  n.,  one  who  uses.  —  ME.  See  use,  v.,  and agential  suff.  -er.
user,  n.,  right  of  use  (law.)  —  OF.  (=  F.)  infin. user,  ‘to  use’.  See  use,  v.  For  the  subst.  use  of the  infinitive  in  law  terms  cp.  attainder  and  words there  referred  to.
ushabti,  n.,  a  small  figure  representing  a  servant, deposited  in  an  ancient  Egyptian  tomb.  — Egypt,  ushebti,  ‘lit.  answerer’, usher,  n.  —  ME.  ussher,  fr.  MF.  ussier,  uissier  (F. huissier),  fr.  OF.,  fr.  VL.  ustiarius,  ‘doorkeeper’.
fr.  L.  ostiarius,  of  s.m.,  fr.  ostium,  ‘door,  en¬ trance’.  See  ostiary.
Derivatives:  usher,  tr.  v.,  usher-er,  n. usine,  n.,  works,  factory.  —  F.,  fr.  North  Eastern F.  wisine,  altered  fr.  Picard  ouchine,  ult.  fr.  L. officina,  ‘workshop,  manufactury’.  See  officinal. Usnea,  n.,  a  genus  of  lichens  (hot.)  —  ModL.,  fr.
Arab.  ushnah,  ‘moss’,  which  is  of  Persian  origin. Usneaceae,  n.  pi.,  a  family  of  lichens  (bot.)  — ModL.,  formed  from  prec.  word  with  suff. -aceae.
```


## [2026-09-05T20:54:37.239Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=896 && NR<=903 {print \"--- leaf\",NR,\"---\"; print substr($0,1,600)}' KLN_1966.txt",
 "description": "Print last KLN leaves"
}
```


### [2026-09-05T20:54:39.270Z] TOOL RESULT

```
--- leaf 896 ---
,  bodies  of  those  who were  slain  in  battle’,  wol,  ‘pestilence’,  OHG., MHG.  wal,  ‘battlefield;  slaughter’,  OHG.  wuol, ‘slaughter’,  and  cogn.  with  OIr .fuil,  ‘blood  ,  W. gweli,  ‘wound’,  Toch.  A  wal,  ‘to  die’,  Lith. velis,  ‘ghosts  of  the  dead’.  The  second  element is  rel.  to  OE.  heall,  ‘hall’ ;  see  hall.  Cp.  the  first element  in  Valkyrie.
1
vali,  n.,  the  governor  of  a  Turkish  vilayet.  — Turk,  vali,  fr.  Arab.  wait.  See  vilayet, valiance,  valiancy,  n.  —  ME.  valiaunce,  fr.  MF. (=  F.)  vaillance, 
--- leaf 897 ---
��,  nr^  (Hesychius), ‘web’,  L.  pannus,  piece  of  cloth’.  See  pane. Derivative:  van-ed,  adj.
Vanessa,  n.,  a  genus  of  butterflies  ( entomol .)
ModL.,  of  uncertain  origin, vang,  n.,  either  of  two  ropes  extending  from  the end  of  a  gaff  to  the  deck  ( naut .)  —  Du.  vang,  ‘a catch',  fr.  vangen,  ‘to  seize,  catch,  capture , which  is  rel.  to  G.  fangen,  of  s.m.  See  fang,  n. and  v.
vanguard,  n.  —  ME.  avaunt  garde,  vantgard,  fr. MF.  (=  F.)  avant-garde,  fr.  avant,  ‘before’  and garde,  ‘guard’.  See  avaunt  and  g
--- leaf 898 ---
  —  A  hybrid  coined  fr.  vari¬ ola  and  suff.  -ite  (representing  Gk.  -Tty)?  ) ;  so called  from  its  smallpoxlike  appearance, varioloid,  adj.,  resembling  smallpox.  —  A  hybrid coined  fr.  variola  and  Gk.  -oei8 ‘like’,  fr. elSoq,  ‘form,  shape’.  See  -oid. variolous,  adj.,  pertaining  to,  or  having,  small¬ pox.  —  Medical  L.  varioldsus,  fr.  variola.  See variola  and  adj.  suff.  -ose. variometer,  n.,  an  instrument  for  the  comparison of  magnetic  forces  ( electr .)  —  A  hybrid  coined fr.  L.  varius,  ‘changing,  various’,  an
--- leaf 899 ---
agential  suff.  -or.
vau,  also  waw,  n.,  the  sixth  letter  of  the  Hebrew alphabet.  —  Heb.  waw,  ‘hook,  pin,  peg’;  so called  in  allusion  to  the  ancient  form  of  this letter.
vaucberia,  n.,  a  genus  of  algae  (bot.)  —  ModL., named  after  the  Swiss  botanist  Jean-Pierre
vaudeville
velites
fitienne  Vaucher  (1763-1841).  For  the  ending see  1st  suff.  -ia.
vaudeville,  n.,  a  theatrical  entertainment  consist¬ ing  of  several  acts.  —  F.,  alteration  of  vaidevire, fr.  Van  de  Vire ,  ‘Valley  of  the  Vire’  (in  Norman¬ dy)  ;  the  songs
--- leaf 900 ---
  F.)  veine,  fr.  L. vena,  ‘blood  vessel,  watercourse,  vein;  natural inclination',  which  is  of  uncertain  origin.  Cp. venation,  vennel,  venose,  venule  and  the  first  ele¬ ment  in  venesection.
Derivatives:  vein,  tr.  v.,  vein-ed,  adj.,  vein-er,  n., vein-ing,  n.,  vein-y,  adj.,  vein-i-ness,  n. velamen,  n.,  a  membrane  (anat.)  —  L.  velamen, ‘a  covering',  fr.  velare,  ‘to  veil,  cover’.  See  veil, v.  and  n.,  and  -men.
velar,  adj.,  pertaining  to,  or  connected  with,  the velum.  —  L.  velaris,  fr.  velum.  See  velum  and  -ar. velari
--- leaf 901 ---
r’, vojina,  ‘war’,  Gk.  iep.ai  (for  ‘I  as¬
pire  to,  tend  to,  make  haste,  long  for’,  OE.  wap, ‘hunting’,  ON/  veidr,  ‘chase,  hunting,  fishing’, OHG.  weida,  MHG.,  G.  weidc,  ‘pasture,  graz¬ ing,  food;  pasture  land’,  are  prob.  derivatives of  a  denasalized  var.  of  the  above  base.  Cp.  the first  element  in  voivode.
venery,  n.,  sexual  love,  (archaic).  —  From  the stem  of  L.  venus,  gen.  veneris,  ‘love,  sexual desire’.  See  venerate  and  cp.  Venus.  Cp.  also prec.  word.
venesect,  tr.  v.,  to  phlebotomize  (med.)
--- leaf 902 ---
, ventricle,  n.,  cavity  in  an  organ  of  the  body.  — Fr.  F.  ventricule,  or  directly  fr.  L.  ventrieulus, ‘stomach,  ventricle’,  dimin.  of  venter,  ‘belly’. See  venter,  ‘abdominal  cavity’,  and  -cle  and  cp. ventrieulus.
ventricose,  adj.,  bellied.  —  ModL.  ventriedsus,  fr. L.  venter,  ‘belly’.  See  venter,  ‘abdominal  cavity’, and  adj.  suff.  -ose.
Derivative:  ventricos-ity,  n. ventricular,  adj.  —  Formed  with  suff.  -ar  fr.  L.
ventrieulus.  See  ventricle.
Ventriculites,  n.,  a  genus  of  fossil  (paleontol.)  — A  ModL.  hyb
--- leaf 903 ---
��true’,  and  Gk. ruov,  fr.  mtoraiv,  ‘to  look  at,  examine’.  See very  and  -scope.  The  correct  form  would  be alethoscope  (fr.  Gk.  dcXvjffrji;,  ‘true’  and  -rsy.6- mov ) .
veratral,  n.,  the  radical  C9H10O4  (chem.)  —  Form¬ ed  with  adj.  suff.  -al  fr.  L.  verdtrum,  'hellebore’. See  veratrine.
veratric,  adj.,  pertaining  to  a  white  crystalline acid. —  Formed  with  adj.  suff.  -ic  fr.  L.  verdtrum, ‘hellebore’  (see  veratrine) ;  so  called  because  it  is easily  obtained  by  the  decomposition  of  vera¬ trine.  \
veratridine,
```


## [2026-09-05T20:54:43.176Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la KLN_1971.txt && grep -n \"yester\" KLN_1971.txt | head -10",
 "description": "Grep KLN_1971 for yester"
}
```


### [2026-09-05T20:54:43.242Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 10278576 Sep  4 14:06 KLN_1971.txt
113099:hestemal, adj., of yesterday. — Formed with adj. 
113100:suff. -al fr. L. hestemus, ‘of yesterday’, which 
113102:hyastanah, Gk. x&eaiv6$, ‘of yesterday’. L. 
113103:hestemus derives fr. heri, ‘yesterday’, as OI. 
113116:hyastanah derives fr. OI. hydh, ‘yesterday’, Gk. 
113117:x!>e<Tw6<; fr. of s.m. See yester-. 
153217:cp. L. hesternus , ‘of yesterday’, fr. heri , ‘yester- 
269780:yester-, pref. — ME. yestren, fr. OE. geostran -, 
269783:gester, gestern, G. gestern , ‘yesterday’, ON. i 
269784:gser, ‘tomorrow, yesterday’, Goth, gistradagis ,
```


## [2026-09-05T20:54:46.271Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '269775,269830p' KLN_1971.txt",
 "description": "Print Klein yester- entry"
}
```


### [2026-09-05T20:54:46.335Z] TOOL RESULT

```
wathaba , ‘he leapt, jumped’, in South Arab., ‘he 
sat, dwelled’, Ethiop. ausaba , ‘he married’, lit. 
‘he caused to dwell’. Cp. moshav, moshava. Cp. 
also marchpane. 

yester-, pref. — ME. yestren, fr. OE. geostran -, 
also giestran -, gystran, rel. to- MLG. ghisteren, 
Du. gister(en ), OHG. gestaron, gesteren , MHG. 
gester, gestern, G. gestern , ‘yesterday’, ON. i 
gser, ‘tomorrow, yesterday’, Goth, gistradagis , 
‘tomorrow’. The orig. meaning of these words 
was ‘the other day’ (reckoned from today, either 
backward or forward). They are cogn. with OI. 
hyah, ‘yesterday’, Avestic zyo, Pers. di, ‘yester- 
day’, Toch. ksdr, ‘tomorrow’, Gk. X^^ ‘yester- 
day’, Alb. dje, L. heri, ‘yesterday’, L. hesternus , 
‘of yesterday’, OIr. indhe, W. doe, OCo. doy , 
‘yesterday’. Cp. hesternal. 
yesterday, adv. and n. — ME. yisterdai , yesterdai, 
fr. OE. geostran dseg, also giestran dxg, gystran 
dxg, ti. and adv., ‘yesterday’. See yester- and 
day. 

yesternight (archaic), adv., last night ; n., the night 
last past. — ME. yisternight , yesternight , fr. OE. 
gystran niht. See yester- and night, 
yestreen, adv. and n. (Scot.) — Contraction of 
yester-even. See yester and even, n. 

yet, adv. — ME. yet, yete , yit, fr. OE. giet, gieta, 
gyt, ‘still, yet’, rel. to OFris. ieta, eta, MHG. 
ieuzo, ieze, ‘yet’. 

Derivative: yet, conj. 

yew, n., any tree of the genus Taxus. — ME. eu, 
fr. OE. eow, iw, rel. to MLG., MDu. iwe, iewe, 
Du. ijf, OHG. iwa, MHG. iwe, G. Eibe, ON. yr , 
‘yew’, and cogn. with Gaul, ivos (whence F. if, 
Sp., Port, iva), OIr. eo, W. ywen, Bret, ivin , 
‘yew’; prob. fr. I.-E. base *oiwa-, * s iwa-, *iwa-, 
‘berry, grape’, whence also Gk. ofy; 673, oa, 
‘service, tree’, L. iiva, ‘grape’. Arm. aigi (for 
oiwiya ), ‘vine’, and possibly also Lith. jieva, 
ievd, ‘black alder’, Lett, ieva, of s.m., OSlav. iva, 
‘willow’. Cp. Iva, uva. 

Yggdrasill, n., the great tree of the universe (Norse 
mythol .) — ON. yg(g)drasill , fr. Yggr, name of 
Odin, and drasill, ‘horse’. 

Yiddish, adj. and n. — G. judisch, ‘Jewish’, fr. 
Jude, ‘Jew’, fr. OHG. judo, of s.m., fr. L. Ju- 
daeus, fr. Gk. ’IouSaio?. See Jew and adj. suff. 
-ish.
```


## [2026-09-05T20:54:47.237Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^go, intr\" KLN_1971.txt | head; grep -n \"heir, n\" KLN_1971.txt | head",
 "description": "Find Klein go and heir entries"
}
```


### [2026-09-05T20:54:47.314Z] TOOL RESULT

```
104081:go, intr. v. — ME. gon , fr. OE. gdn, rel. to OS., 
50395:coheir, n., a joint heir. — Formed fr. co- and heir, 
111474:heir, n. — ME., fr. OF. heir, eir (F. hoir), fr.
```


## [2026-09-05T20:54:53.550Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '104081,104110p' KLN_1971.txt; echo \"-----heir-----\"; sed -n '111474,111500p' KLN_1971.txt",
 "description": "Print Klein go and heir"
}
```


### [2026-09-05T20:54:53.667Z] TOOL RESULT

```
go, intr. v. — ME. gon , fr. OE. gdn, rel. to OS., 
OFris., MLG. gdn , Dan. gaa, Swed. gd, MDu. 
gaen, Du. gaan , OHG., MHG. gdn , gen, G. 
gehen , Crimean Goth. geen y ‘to go’, fr. I.-E. 
base *ghe-, *ghei-. The same base appears re- 
duplicated in OI. jihite (for *ghi-ghe-te ), ‘goes 
aw ay’, ja-ha-ti (for *ghe-ghe-ti), ‘leaves, aban- 
dons’, Gk. xL^ivo (for * ghi-ghe-no), x(xtQ[AI 
(for *ghi-ghe-mi), ‘I reach, meet with’, Avestic 
zazami , ‘1 dismiss’. Base *ghe-> *ghei-, ‘to go’, 
is identical with base *ghe-, *ghei-, ‘to lack, be 
in want of’ (prop, ‘to go without’), whence Gk. 
XT)xo<;, ‘want, need’, x aTe ^ v » ‘ to want, be in 
need of, long for, desire’, x^ 9 °^ ‘bereaved of’, 
L. heres, ‘heir’; see heredity and cp. chori-. Cp. 
ago. 

Derivatives: go, n., that which goes, go-er, n., 
go-ing, n. 

goad, n. — ME. gode, fr. OE. gad, ‘point, sting, 
goad, arrow’, rel. to Lombard gaida, ‘spear’, 
and cogn. with OI. hetih, ‘missile, projectile*, 
hayati, hinSti, ‘pushes on, hurls’, Avestic zaena 
‘weapon’, Gk. ^aux;, ‘shepherd’s staff’, Gaul.- 
L. gaesum , ‘a long heavy javelin’, Olr. gae , 
‘spear’, OE. gar, ‘spear’, Du. gesel, OHG. 
geisila, MHG. geisel , G. GeijSsl, ‘whip, lash*. 
All these words are traceable to I.-E. base *ghei - 9 
‘to drive on, push on*. Cp. gore, ‘a triangular 
-----heir-----
heir, n. — ME., fr. OF. heir, eir (F. hoir), fr. 
VL. *herem (whence also OProveng. er, ‘heir’), 
for L. heredem, acc. of heres, ‘heir’, prob. a 
compound meaning ‘he who obtains that which 




HEIRDOM 



340 



is left’. The first element of this compound 
derives fr. I.-E. base *ghe(i)-, ‘to lack, be empty; 
to yawn’, whence also OI. jahdti, ‘leaves, aban- 
dons, gives up’, jihite, ‘goes away’, Gk. x 9 jpo<;, 
‘bereaved of’, xatvew, ‘to gape, yawn’, 

‘lack, want’. See go and cp. chori-. The second 
element is *ed-. It is prob. formed from the 
preposition *e , ‘beside; close by’ (which stands 
in gradational relationship to prep. * 6 , ‘close, 
by’, appearing in OI., Avestic a ‘toward’; see
```


## [2026-09-05T20:55:08.338Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gestern\" BRT.txt | head -30",
 "description": "Grep Bartholomae for gestern"
}
```


### [2026-09-05T20:55:08.383Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:55:08.855Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"yesterday\" PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt | head -20",
 "description": "Grep Pahlavi dicts for yesterday"
}
```


### [2026-09-05T20:55:08.944Z] TOOL RESULT

```
PHD.txt:125:did ... add other. add dig |YTMAL < А *?{т?1 | N di] yesterday. delete *drém ... (read balgam) drubušt ... add protective. drust [drw(d)st' ... duš-čihr ... add ill-natured. duš-nām [-n^m | (M dwjn'm), N ~] add ill-famed. dušwār [dwáw?l | (M dwjw'r), ... ékanag ... for obedient read loyal, faithful. ~th : for obedience read loyalty, faithfulness. for Farrēbāg... read KFarrēbāy [pinb(^)g] ... frayad |pl(y)d^t' | N faryad] ... delete M pry'd. frazand |prz/znd | ... frusag ... add M prwšg. garódman ... read | P grdm'n. gazdum |gcd(w)m, gzd(w)m |... guftàr ..., ~th : add eloquence. hambar |hm-, hnb] |... add  hamest |hmyst'] whose good and bad deeds weigh equal. ~(ag)an |-(k)^n'] limbo, the neutral station between heaven and hell. delete hammist ..., ~(ag)an ... handarz ... add M °’ndrz. hammoxtan, hammoz-, ~i8n : add learning. hast |TWMNYA < A tmny ; ... add hūg [HZWLYA < A hzyr’; hwk' | M hwg, N xiig] pig. add hūkar(ag) |hwkl(k') | N xükara] porcupine. (not hedgehog) add *huzārag [hwc’lk | N хијага) little, small, few. !jadag ... add fortune. jüdan ... | M jwwdn, jwy- ... add karawuš [kl wš| N ^] wine-press. delete karbunag ... read karbūg |klpwk', klbwk'| lizard. kardagān ... add service (ofthe gods). delete karxēš vds
PHD_mackenzie.txt:533:add dig [YTMAL < A Ptm'll N d~ yesterday.
```


## [2026-09-05T20:55:16.050Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"zyö\\|zyo\\b\\|zy6\\|zyö\" BRT.txt | head -20; echo \"--- hyah/di ---\"; grep -n \"np\\. di\\b\\|hyás\\|hyáh\" BRT.txt | head -20",
 "description": "Grep Bartholomae for zyo"
}
```


### [2026-09-05T20:55:16.111Z] TOOL RESULT

```
2472:dalvil  . .  atibyö  kam  Y.44.20;  46.12;  — li  narS..aeiqm  nmäna  Yt.i~.yC;  g— 14.^, J0.39f.s,  33,Y./j.3,j7.37,Vr.//.i9,V.2, 43-J.i4,Ä4i,  12.1, 13.50,  i5.22,FrV/. 10. 40,  N.<S'5; — g3ui..ya  dar>nlhu  mi^rS.- drujqm  ..frazarsta  (sd.)  aglqm  rai'iya  .. hiit»nte  Yt. /o.  38;  —  vTspanqmca  , .  asae- nqm  aiaoninqmca  .,  vUpanqmca  allqm  za- ra'iuStnm  ..  *susruma ikatsim  Yt.Jj.148; —  a^qm  anyS  N.  61,  62;  —  aifam  aOiai»- kam  .  .  adqmcH  S  ahmt  .  .  vicC^ei  (sd.) aipT\.32.i;  30.1,  8,55.9;  —  haxays .. astvat.gr3take  .  .  assu  paro  fräntmlite aismü  Ytiff.g$;  — gä^a  . .  yezi  argAqm *Syutnpe  väUm  framaraiti  N.  42;  —  xi paiti  apqm  .  .  a^ra  atthqm  V.  y.  5 1 ,  Y. 6Ä7;  Yl/j.68;  —  duzvarmanhS  .  .  rä- mqmcä  J//'"'  dadätu  V.  ^3.  8 ;  —  yaia  ta r  ,  ,  minghäeä  .  .  yH  vohü  .  ,  a'iä  %WJ Si/'"'  yazamaide  Y.  j(?.4;  —  karapsAsaJ (sd.)  kfvitäsca  . .  töi  abyH  (AbL)  bairyänts (sd.)  .,  Y.52. 15; — spuda..kuir3  ayä.. Y.44-I5;  30.6,  3t.io;  —  /J  mainyn  .  . ascä  (GD.)  .  .  Y.30.3;  —  Gen.  in  Ver- bindung mit  hava-i  zasta  hl . .  frasniöa- v paityesii  V.22.7  — 13;  /.z;- — \y"t  aSahe  yat  apirmäyükahe  ahe  hava- aiwySr3hafi?m,.äat  aiijhi  ahi  aiwyästö  Y.  _v(7«  tütroö  "die  Hände  ..  des  Kindes  an ij.zb;  — ahur>m  ..  ahyä  x!a~i:räc3  ..  *hva- 1  dessen  Leib"  V.itf,  7  (?)  "';  —  dgL,  zugleich paphsiica  (sd.)  lim  .  .  yasämaidi  Y.  J7.  vorausweisend:  astvatjr3iö  ..  kB  ..  aiike if.;  —  sraosim  ..yazamaide  ahe  raya  . .  j  haxayB  /räyente  astvat.iritahe  Yt.  ip.  95: aiÄke  ama  ,.  ahe  yasna  ..  t?m  yai3i  "den '  - —  dalnqm  .  .  yao:dai%xSa  ai:a  sT  aiAka Sr.  .  .;  ob  seiner  Pracht  .  ."  Y.  57.3;  Yt.  yaoidaitii  ..  havaya  .  .  dainayä  Y.io. J-i^i  5i  9  (statt  fem.!);  —  noii  kl  anyö\i9.  a)  spez.  auf  das  Subjekt  des  gleichen urva  kaum  urvämm  paiti  irista  (sd.)  ^a-|Satzes,  Reflexivum:  ka%S  .  .  gqm  Ha- zaiti  xraosyü(a{%t^voyaca*a>»he^^.*at3hr^^  sSil  y}  kirn  ahmai  ..  stsi  usyaj  (sd.) Y.  13.9;  —  fravasayS  . .  ankam  raya  . .  Yt  ".  .  qui  eam  sibj  .  .  esse  cupiat"  Y.  ^o.  2 ; 13.2, 14—18"';  — gunäayäi  ..  za/an  ta/-  ^  —  nsit  sp>ntqm  d3r?st  (sd).  akmai  stöi San  (sd)  aya^'*  masJY.3.32;  —  vac?  ..\armaitlm  Y.4^.2;  —  hvJ  tat  n3  ..  ak- yii  . ,  akmai  straohm  dqn  Y.  45. 5 ;  —  |  mai  "'  dazdl  (sd.)  Y.  5/.  1 9 ;  —  aada  (sd.) ustä  ahmst  yahmai  .  .  kakmaicTt  . .  atca  \  vinzyötüca  It  akmai  fracä  vatöyBtü  (sd) <ihmai  Y.  43. 1  f ;  —  gavöi  . .  ha  %X  to\lt  alibyB  yöi  .  .  "..  sibi  (ipse)  . ."  Y.  J5.  6; huisii»m3  .  .  dal  .  .  at  ahyäi  .  .  masda  \- —  at  hT . .  /ravanll  (sd.)  vasirim  ahyai orvara  vaxsat  Y.4S-6;  31-9;  —  raya  ..\fntyant3m  Y.jj.  10;  —  nSit  ta  Im  x^3ui koya  aiiiAä  raiavö  Y.iff.iS;  *YyX.  50; — {vaipyö  .,  zara'iuhrtm  ..  Ayat  akml'^ paoiryö  gairis  . .  akmat  haca  garayO  tu- 1  urüraost  astö  hyat  , .  v3z3  (sd,)  Y.  31. uxiyqHYt.ig.\i.;  34,80;  —  hö  nBit..*/r3-\  12.  aa)  Der  Gen,  vertritt  dann  die  ent- nJmaite  ,.  /rä  ahmst  parö  ..  «jÄion/i;  j  sprechendeFormdeslat  suus:  airj  *i'jiri»i Y. 57-18,  ungeschickt  benutzt  Ytp.4;  lo.  baraiti  mi>akvac3  vä  irvivaca  (sd.)  vä.. 117;- —  *haltuma  . .  kacaiti  dim  . .  astica  akyl  zaridaca  manat»kac3  ", .  ex  suo  (uter- ahmi  avavat;^arin6  yäi:a  yat..Yx.ig.(>Z;\c^^)  corde  et  animo"  Y.ji.ti; —  akya —  :^aitu/  . .  vtrizifum  mat  airyamnä  . .  \xrata  frö  ma  sastB  (sd.)  vakistä  Y.  45. 6  ;
2801:Irrlehrer,  der  . ."  \.g,$i{.;  —  yavat  °fa *gaintii  upankacaili  (sd.)  V.  7.  56;  — yavat  'sa  ilß  bySrixfi  (sd.)  .  ,  frabavai \.i4.\y,  — yavat  -lö  spä  anya{sA.) )asö V./5.48,  a)mitrelativischemAnschIuss: "jS  zT  asti  baslazyö.t3mö  .  .yal  *mahnm.- sppni»m.baei'azyd  (sd.)  V.  7.44;  —  '/a  bi~ paitisiana  (sd.)  y3  kaine  V.  75. 19;  19;  — vXsp»m  ä  ahmst.,  yat  -ia  yö  apsntinyBkB uxjasnf  (sd.)  "bis  es,  das  Kind  . ,"  V.  75. 15;  —  'sa  yS  *ar?mBiidd'a.W3.  2)  auf ein  Relativum  als  dessen  Korrelat,  sub- stantivisch: ci'at  dra)ö  avaMUlüt  '^a  yö näirikaya  . .  !^ar>^3tn  frabamt  V.  /J.  4 1 ; —  °sö  .  .  aitayä  vihrkayh  (sd.)  Jq'^-wS.' tarö  *at3kat  . .  ya^a  spä  vtkrkake  k»r?- naoiti  V.  y .  4 1 ;  — "/?  ratufris  *yö  jayara N.if};  24,  60;  —  'sa  yetjhe  apirinSyükö ^•9i  7;  —  °^'''  zaoiranqm  tnaziltaca  . . yiJ  *naire  asaone  *daste  N.^4.  III)  In
5256:mit  US  'sich  erheben':  s.  *uzirfidyai Inf.  a)  insbes,  von  Gestirnen,  'aufgehen': fistrUn  .  .  yim  .  .  uzyö.rfnt^m'^  *AispS.- Sinti  Yt.  <V,  36;  —  hi'anxsaltim  vzyS.- rai/i'>^'V.ifi.2S^^;  —  uzayiira3^^>  uzlra^*^* Ava>vx/ag/a\.  21.  5,  17'*;  —  hmat  uzTra^* V.2/.s«>.
6599:Kopula  hat  keinen  festen  Platz,  bevor- zugt aber  entschieden  die  Stelle  hinter dem  ersten  Hochton  ihres  Satzes,  und zwar  auch  im  Nebensatz.)'^':  ks  nar?  ahl yim  ..i  ..  az3m  ahmi..haomB  asava  \.g. I  f.;  12.  7  (wo  ahmt),  Yt.  7.  7  V,  11-15»', Ä15,  70.54',  74.3^  75.43-48S',  77.17, Az.  7,  Vyt  /;  —  azim  bä  is  ahmt  .  .  yä I  hava  dama  H.  2.  1 1 ;  —  srTrö  ahi  sara- .  'bus/ra  Auksntö  ahi  YL  77.  22;  10.  29', i  76',  79,  80,  72. 1,  Y.p.  25,  70.9',  6"2, 1,  V. '  iq.  6,  70,  VyL  22;  —  asU  (als  Vok.)  bfr?- zaiti  hmäta  ahi  huci^ra  YL;7. 15;  — hai^imifa  asahe  xä  ahi  Y.  70.4;  —  Hica (sd.)  caräiti}  ahi  yqm . .  H,2. 10;  —  yäha vasi  (sd.)  asäum  *ala  anhB  (sS.)  asava Y.77. 16;  —  avdha  izara>uslra)  *a»kä (iS.)'^'  spanya  V./Ä7;  —  a>a..AumäyH.- taraca  ..  atjhäma  Vr.  72.4;  —  mä  hyä>a (2p.)''>  duizaotärB  Vyt.  72;  —  aheca anhlus  yö  astvatS  yasia  asti  manahyä  Y. 57.25;  —  yatea  aAmäl  asti  mazyö  ..  tat tiB   däyala  Y.  (»5. 14;  14^;    —  yayä    asti
7609:•  j,  »-var«zyant-  Adj.  i)  mit  Akk,  'nicht wirkend,  begehend':  'zinbyd^"^  pascaila araiwya  syaoina  V.J.  40.  2)  ohne Obj.  'sich  nicht  übend  (tn  den  Werken der  Religion)';  yö  saite  haurvqm  tarasca xsapamm  ayazsmns  . .  'zyö  ".  ,  ohne  zu beten  . .  ohne  sich  (im  Guten)  zu  üben" V./&S-
8098:mahalUh •Sa.:  vrdähik;  {vi  Vr.):  mvJmlHjh). •  j,   izyö.tara-  Adj.  'der  erfolgreichere';
8674:•  j.  "uzyö  F.5.
10778:•  j-  G  gO  xäaSrya-  Adj.  'imperiosus,  Ge- bieter, Machthaber',  von  Göttern;  1)  von Haoma :  haomS{sfL)  fräsmis  baisazyö  srtrS ys  tairidsiisrö  Y.57. 1 9,  ß)  von  Apqm- Napät:  hmanhm  ahur»m  "rim  xsaUfm apqm    napäifm{sd.)   aurvai.asp^m  Y.  2.  5;
14116:Wortlaut  dSt);  a)  int  gAw.:  katlltSm\bStidvahyä  (sd.)  .  .  tka^B  -gva  .  .  aiäi asava  vä  'gvä  vä  virtnvaitl  (sd.)  mazyö  ränsB  \.4ff.3;  —  t/u/.sasti/ (sd.)  .  .  akä Y.ji.iy;  44-a,  46.6  (zit  7/.13.  P-50,  varanS  -gvä  *ftizvä  av^r»tS  (sd.)  Y.  45. wo   drvs),  4j.  5;    —    'gvani^tit  Y,  46.  5,;  r-  «)    i^'^t'  ^£.    von    bestimmten  dem
16530:•  j.  baeSazyö.tara-  Adj.  (fem.  'rä-)  'der heiltätigere':  fravasayS  .  .  yä  "ri  (NPC) ahmät..yaha  vaca  framraväire  [sd.)  Yt 13.  64.
16532:•  j.  baeäazyö.tuma-  Adj.  'der  heilkräftigste,
19399:\pfr?satca  ma  ä/  akl  . .  Y.43.  J;  —  at ahya  ma  bTndvahyä  (sd.)  manayätc  lialis Y.4g.2;  —  nüij  ahya  ma  a%rii  {^.)  . . frSsyatY.46-^-  B 11)  imjAw.;  zu  a  1): "  mam  stavät?  Yt5.  8;  Ä  15,  10.108; ana  mam  yasna  yazaiSa  Yt.5.  91;  — yat  mam  iura  pazdayanta  Ytjj.  55;  — ^.82; —yai  ma  hau  na  ..aot  avi  ashaväj P.  27;  —  yezi  mam  p^nsa^Ae  Y.iS.j; Vt,  /f.  56,  ig.  44;  '—  aoi  mam  .  .  ttütci yd^a  ma  aparacit  saoiyan^  siavqn  Y. g.z; — yS  mam  alvS  JäraayätiYt,iy.3o; 5.  so,  Y.  //.  I,'  a,  3,  5;  —  As  ahi  yS  mam zbayehiY\,ij.  17;  V.J.  a6;  —  aat  ma  riBit masyaka  .  .yazmie  Yt.  10.  54;  —  aat  mam tarn  ^baisazyöis  Y .22.2,  9;  2  i.St.,  R2,i4, Yt/7. 19,  SS;  —  yezi  ahi  paurva.nalmat aat  mam  avi  nmSnaya  YtJÖ.  a;  2,  Y.j/.i;
20457:mäsdayasneis  . .  staotanam  yesnyanqm  Vr. 5.  7  j  —  gSuI  .  .  gayehe  .  .  'rahe  spmtake asaonS  vgntyarfuAaAe  Yt.21.3;  —  xara- 'hustnm  .  .  'nm  spnlwt  .  .  g^l  urvätam yazamaide  G.  4-  6  i  —  fravaiayS .  .  yqm^a ahrS  .  .  sraosahe  . ,  mi%raAe  . .  °rtiÄe  spenr tahe  YL/_y,86;  /J.  17;  —  äal  mqm  tum bi/azyöi^  'rö  (alsVok.)  iptnts  ys  aij^arma V.  22.  2 ;  —  ^aiti  ahmSi  avafata  °rö  spmts yH  asjfarmä  V.  22. 6.  a)  *rahe  spfTitahe (näml,  ayars)  heisst  der  39,  Monatstag: 'rahe  spmtahe  alaotüS  v^r»tyar?uhahe  S. /.  29;  vgl.  2.39,  ¥./().  7.  Undeutlich:
27334:•  j.  srayah-  Adj.  'der  schönere':  cä  aUi masyS  vanhs  'yS  aSstn  dätim  yim  vjdsyüm .  .  iipairi  anyäis  sraväÜ  "um  wie  viel ; grösser,  besser,  schöner  ist  dies  Gesetz  . .  1 als  die  andern  Lehren"  V.5.  22;  —  imat\ vaahs  imat  'yS  yj^a  tum  .  .  valaahe  V.  | 5.  a  I ;  —  yalca  ahmst  asti  mazyö  .  . '. vatfhS  . .  'yd  . .  parS.ar?jaslar3m    tat  .  .
--- hyah/di ---
```


## [2026-09-05T20:55:23.574Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"g[eo]st[e3]rn\\|zy5\\|zyö-\\|hyás\\|hyáh\\|ai\\. hyáh\" BRT.txt | head -20; echo \"== search zya ==\"; grep -n \"^• *j, *zy\\|• j, zy\\|zyö \" BRT.txt | head",
 "description": "Search Bartholomae variants"
}
```


### [2026-09-05T20:55:23.661Z] TOOL RESULT

```
22251:v»r>%rajqsttmS  artuxts  växf  yäAi  v)r>- 'hraJqstymS  Yt. //,  3;  Y.  7.  26;  —  ahu- nahe  vairyehe  arsuxhahe  "i'äj: /(statt GS.)" Y.  Ä  i;  —  *imqm  vacS  (AP.)  dnmjaySil ySi  ankin  vär)hrarjnyB.t»m>mca  baiiazy5J>- mptttla:  yd^ä  ahU  vairyS  V.  p.  z  7 ;'  2  8,  «y.  1 9 ;
== search zya ==
6599:Kopula  hat  keinen  festen  Platz,  bevor- zugt aber  entschieden  die  Stelle  hinter dem  ersten  Hochton  ihres  Satzes,  und zwar  auch  im  Nebensatz.)'^':  ks  nar?  ahl yim  ..i  ..  az3m  ahmi..haomB  asava  \.g. I  f.;  12.  7  (wo  ahmt),  Yt.  7.  7  V,  11-15»', Ä15,  70.54',  74.3^  75.43-48S',  77.17, Az.  7,  Vyt  /;  —  azim  bä  is  ahmt  .  .  yä I  hava  dama  H.  2.  1 1 ;  —  srTrö  ahi  sara- .  'bus/ra  Auksntö  ahi  YL  77.  22;  10.  29', i  76',  79,  80,  72. 1,  Y.p.  25,  70.9',  6"2, 1,  V. '  iq.  6,  70,  VyL  22;  —  asU  (als  Vok.)  bfr?- zaiti  hmäta  ahi  huci^ra  YL;7. 15;  — hai^imifa  asahe  xä  ahi  Y.  70.4;  —  Hica (sd.)  caräiti}  ahi  yqm . .  H,2. 10;  —  yäha vasi  (sd.)  asäum  *ala  anhB  (sS.)  asava Y.77. 16;  —  avdha  izara>uslra)  *a»kä (iS.)'^'  spanya  V./Ä7;  —  a>a..AumäyH.- taraca  ..  atjhäma  Vr.  72.4;  —  mä  hyä>a (2p.)''>  duizaotärB  Vyt.  72;  —  aheca anhlus  yö  astvatS  yasia  asti  manahyä  Y. 57.25;  —  yatea  aAmäl  asti  mazyö  ..  tat tiB   däyala  Y.  (»5. 14;  14^;    —  yayä    asti
7609:•  j,  »-var«zyant-  Adj.  i)  mit  Akk,  'nicht wirkend,  begehend':  'zinbyd^"^  pascaila araiwya  syaoina  V.J.  40.  2)  ohne Obj.  'sich  nicht  übend  (tn  den  Werken der  Religion)';  yö  saite  haurvqm  tarasca xsapamm  ayazsmns  . .  'zyö  ".  ,  ohne  zu beten  . .  ohne  sich  (im  Guten)  zu  üben" V./&S-
8674:•  j.  "uzyö  F.5.
10778:•  j-  G  gO  xäaSrya-  Adj.  'imperiosus,  Ge- bieter, Machthaber',  von  Göttern;  1)  von Haoma :  haomS{sfL)  fräsmis  baisazyö  srtrS ys  tairidsiisrö  Y.57. 1 9,  ß)  von  Apqm- Napät:  hmanhm  ahur»m  "rim  xsaUfm apqm    napäifm{sd.)   aurvai.asp^m  Y.  2.  5;
14116:Wortlaut  dSt);  a)  int  gAw.:  katlltSm\bStidvahyä  (sd.)  .  .  tka^B  -gva  .  .  aiäi asava  vä  'gvä  vä  virtnvaitl  (sd.)  mazyö  ränsB  \.4ff.3;  —  t/u/.sasti/ (sd.)  .  .  akä Y.ji.iy;  44-a,  46.6  (zit  7/.13.  P-50,  varanS  -gvä  *ftizvä  av^r»tS  (sd.)  Y.  45. wo   drvs),  4j.  5;    —    'gvani^tit  Y,  46.  5,;  r-  «)    i^'^t'  ^£.    von    bestimmten  dem
27334:•  j.  srayah-  Adj.  'der  schönere':  cä  aUi masyS  vanhs  'yS  aSstn  dätim  yim  vjdsyüm .  .  iipairi  anyäis  sraväÜ  "um  wie  viel ; grösser,  besser,  schöner  ist  dies  Gesetz  . .  1 als  die  andern  Lehren"  V.5.  22;  —  imat\ vaahs  imat  'yS  yj^a  tum  .  .  valaahe  V.  | 5.  a  I ;  —  yalca  ahmst  asti  mazyö  .  . '. vatfhS  . .  'yd  . .  parS.ar?jaslar3m    tat  .  .
```


## [2026-09-05T20:55:30.301Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"zaz[aä]\" BRT.txt | head -20; echo \"== leaves ==\"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' BRT.txt",
 "description": "Grep Bartholomae zaza"
}
```


### [2026-09-05T20:55:31.907Z] TOOL RESULT

```
6592:—  its/i"'  i?  Ad^m  jräid  aiaurune  .  . Yti'ia  ra^aistaraAe  ..\'.ij.44.  4)  mit Instr.  'zusimmea  sein  mit  — ',  sva.  'etwas zu  eigen  haben.  Jemand  zu  eigen  sein'; B)  im  Aw.:  ratUa  ..  ysi  (NDf.)  ,4?« (statt  Du.)  k}krpa  sraista  (ISf.)  *zazäite (Sil.)  Vt.5.34;  —  ujÄ"*  zl  ana  avc u.\'Mi/a  tsdO/a^a^u/..  V./ij.iO.  S)  mit a)  dem  LS,  eines  Nom.  act.'",  b)  einem Absolutiv,  c)  einem  Infinitiv  im  Sinn  von a)  ilal.  'stare  lavorando',  engl,  'to  be labouring',  ß)  (nur  bei  a)  ital.  'esser  in , lavoro'.  a)  LS.  A)  ||  im  Ap.:  «)  ^adakiy aJam  asnaiy  (sd.)  äham  abiy  ''uvajam ".,  1  wastaarching.."Bh.2. 3; — lyaxnahyä mühyS  14  raocabis  'kakatä  (sd.,  auch fdSt.)  <7-4i»*  ". .  stavano  passando"  Bh.  i. \\;  usw.  B)  im  Awr.:  ß)  aisamcTi  ä ahml  >ii>akml  .  .  vTiiiiBi  (sd.)  ai^T  Y.J2. 8.  b)  Absol.  B)  im  Aw.:  yesi  ahi g-if?  ii?r^3m  (sd.)  V.  sr.  5;  — yesi  anhat Hfiirtjin  vn  . .  aiitii.vantim  (sd.)  vä  V.  7. la;  —  ya^a  na  sat>mea  .,  *parsanqm (sd.)  *nijat3m  hyat  YtTj.yi;  —  yezicä ttasui  nar)m  *3stärayantJm  (sd.)  S»h3t'°* V.  1.4;  — yezi  *hisku  hiskväi  sralsyäntTm  i (sä)  ./«Ä<i/">  V.A'.34.  c)  Inf.  B)^im Aw.:  yims  asti  l>pri%e  (sd.)  xi'airayS  V. 1', 7;  —  iJtar/  vSi  (sd.)  masda  ahurahyS^ aAl\.^O.y,  3;  —  iäis  ä  mazda  vlävalsam  \ ^ti'i'i  (sd.)  ahlX. 34.11;  —  kasluscu'n''i\ a.\'iiu/ig  iJi^?(sd.)  auhai  isväcil  fias  paraos\ aks  är?gi'äitlY.47-A>  — y'^a  nS  ankam  1 (3PKPfA.)">    *Jafd  (sd)    manh  Y.&o.iir
6862:■rahe  mazdä  Vr.  14.2;  — yeAh! hltqm  äat yesng  (sd)  paitl  vai)hd  mazdä  'rS  vag'iä Y.  27. 1 5 ;  —  äppm  zazahi  tarn  ys  °rS  mazdä zrayaahal ha'a  z'ouru.kas-lt ha'^ra  Täi?mca dunmqnca  V.5.  15;  isf.'.  60;  —  a'iä  Ml (sd.)  °rB  ma-id\  zard^ustr^m  aoaxsayaUa Y.  /2.  S ;  —  ar>dvlm  . .  yahmya  °rS  mazda ivaiiayal  Yt.  5.85;  —  imat  t!  saahat
7422:•  j.,  g.  ärmatay-j-ffiü///- f. 'Denken,  wie ;  !i;>/v«c^/flM  Y.  4(^.5;  —  ks  b»r»xiqm  iäi't es  sich  gehört,  rechtes,  dem  göldichen ,  (sd.)  x/dirä  mal  'tim  Y.44'l\  —  «i Gebot  und  Willen  sich  fugendes  Denken,  \  )isi  dugfda  /tu^ao%anä  (sd.)  'lis  Y.  45. Frommergebenheit';  i)  im  Gegensatz  zu  4,  a)  Du.  in  Verbindung  mit  aÜTt^  Du. tarö.malay-  (sd,):  vainJt  ahmt  nmäiie  °tis\*A.  und  Arm';  yadä  ahm  za-im  (sd.)  .  . tarH.maitlm  Y.60.%.  z)  sonst:  °leis  .mazdascü  ühuräi^hs  asicn  "maifi  Y.  j/. kasctt  asa  AuzSntus{?.d.)  Y.  4^.  5 ;  —  Aahil  \  4.  a)  sonst  mit  spttUa-  Adj. :  ySi  sp?ntqm tJng  3  vTjSmySl  (sd.)  °tis  Y.  44. 11;  —  °Wfff  %'wahya  mazdä  Tldusö  6^rßjnqm{sd.) ntanB  voAB  urutiaslä  aSaunam  namasca ya .  dus.^ao%anä  avazazat  Y.34-9;  10;  — 'til  T^cä  "den  guten  Sinn  und  die  Seelen  ,  kukm  . .  assm  ka  sp?tita  "tu  Y.  57.  4;  — der  .(i/flgläubigen  und  deren  Gebet,  ihit  kJ  vä  asa  afrastä  (sd)  kä  spmia  °til Frommergebenheit   und   ihren  Glaubens-  ". .  mit  wem  ist  die  heilige  Arm."
12403:—  ahys  *mainyJus  IvSm  ahl  tä  (sd) sp»ntlf\.4-p.^; — yat  Ai  tarn  us.sayar»Aa tarn  imvS  sara%ustra  Y.*?.  13J  —  tum paoiryS  sarä^u/tra  ahumm  vairlm  /n sravays  \.g.  14;  15;  —  tum  nS  äiraom *xaota  *sU{sd.)  Vr.j.  7.  2)  vor  einem attnbutiven  Relativ(satz) :  apjm  zazaAi tum  ys  aAars  mazäi  V.  j.  15;  15'
17140:•  ].,  g,  baraxla-  Adj.  (fem.  '\a-')  'will- kommen (geheissen),  sva.  geschätzt,  schätz- bar, teuer';  a)  von  Personen:  kS  '%qm lait  (sd.)  ..ärmaillm  Y.44.'j; —  'öam  möi firaiaosirs  .  .  daBlsUt  (sd.)  k>hrp!m  V. 5J.  17;  —  äat  mqm  ..'^qm  hattitn  hir^xoB- tarqm  (sd.)  .  ,  H.  2.  14.  a)  mit  Gen. ('von  — ,  für  — "):  ySi  sptntqm  ärmaiHm "hwakyä  mazdä  •'harn  vidusS  .  .  avazazat "die  die  heilige  Arm.,  die  von  deinem Wissenden,o^T  geschätzte,. .verscheuchen" "^•34-9;  —  ha  (näml.  ärmaiii/)  ..vatihius manatihd  °8;(NSf)'*  "sie,  die  vom  guten Sinn  geschätzte"  Y.  48. 6.  b)  von  Sachen : anyhsca  *o«  (NPf.)  avarith  "und  andre schätzbare  Besitztümer"  Yt.  17.  7;  —  hitUi anyasHi  asas^a  /äi^rasca  .  .  'iSsca  (NPn.) V.  /.  20;  —  aps  mä  Isiim  apayantä  (sd.) 'Garn  Aaittm   vaithSus    manatths  Y.^ja.  9,
18783:Sü.:  nirgaminyak  (NP,).  —  0  Das  ä  »om  NS, •«i/j  E.  dageg.  lat.  «ö-.  —  >)  Gdn.  KZ.  sÄ  si  i. •  j.  nasav-  f.,  m.  'Leiche,  Leichnam'  (von Menschen  und  Tieren);  'Leichenteil':  nSii spsMrjtS  nsit  . .  °su/  nanm  nötl  *astara- yäti  yaica  alte  °jai^  ('Leichenteile')  ^5  sps.- birslaca . .  'tus  nanm  *3stärayantfm  äahäi Uar^Jtäitya  .  .  visps  anhul . .  p^/SJanu/ frSria  ankam  °sunqm  ('Leichen')  ys  paiti äya  zima  irfnhar^V.j.if.; — jaica  aste 'sävS  fri^yeilica  puyäica  Y.6.28;  —  iat iä  nara  yaoidayqn  anhm  .  .  yä  'säum ava.h>Tvta  ssnS  vä  paraAristahe  tnasyeke vä  V.iV.3S;  33,  97,  5.42;  — >aÄ<i  narim alavarum  .  .  'sui  (AP.)  aoi  ava  *%ravTt (Sp.8o2U.)P.2y;  — yai  aesa  'sus  anaiwi.- ynixta  sanS  vS  ..  V.J. 2^;  30; — yt . . matdayasna  ,  .  taci.apaya  (sd.)  's3um^^ frajasqn  .  .  aS^a  S/s  ayaoidya  .  .  yavat azsa  'sus  niibpnla;  us  haca  'savö  (GS.) altavat  apat  Aaca  niiläraym  (Sp.  939  o.) ,  .  pasia  'savs  (GS,)  niüjn^i  .  .  a/i yaoidya  bavaiti  V.  6.  26—32;  —  pasi'a  ., 'Säum  avaJian^mtiisA.)  sps/um  vä  raoitm vä  vfhrkim  wa  V.  5.  J;  —  nara  .  .  yä 'Säum  matgu^qtn  äp»m  ä  vä  älnm  ä  vä ,  .  frabarmti  V.  7.  25;  —  yat  .  .  mazda- yasna  . .  ätnm  nasu.paktm  /ra/asan  'sBm hqmpa^qn  'sUm  /i<lvayqn{sA.)  V.ff.j^;  — «äV  vatihs  ..  iyaöimm  v^myeiti  ydOBii^ puhrake  .  .  frä  nast>m  (sd.)  'sam  pacät  \ V.  76. 1 7 ;  —  nara  . .  yä  'säum  fraauharät  I sünS  vä  .  .  masyefu  vä  V.  7.23;  —  visp^m  j ä  ahmäi  'sunqmca  aiwi.varsianqm  (sd.)  j V.  5, 14;  —  apim  zazämi  aztm  yS  akurS\ mazdä  . .  avi  "ssm  (in  koll.  Sinn)  vazämi  1 . .  tä  ha%ra  frafrävayämi  avi  zrayn  päi- 1 Hifm  (sd.)  V.  5. 1 7  f. ;  1 5  f.  A)  Name  der  \ Leichenhexe*':  ial  .  .  'sus  upa.dvqsaitii ..  i^ari  pasca  para.iristlm  ..  us  haca  6ao%S ayät  .  .  'SUS  upa.dvqsaiti  apäx^raiibyS naHnaeibyB  *maxsi.hhrpa  arrjaitya  V.  7. I  £;  —  yat  aSe  yä  sps.jataca  .  .  coatit>m pascaüa  srvätum  .  .  'sus'  upa.dvqsaitii  .  . asnyehe  (sd.)  pascaita  anyehe  ra^ws  .  . 'SUS  upa.dvqsaiti  V,  7. 3  f. ;  —  kuha  a!tat •sus  (statt  Aide.)  '>  pirTttäne  yä  haca  irista upa  jvanifm  upa-rag^waiti  (sd.)  V.  jo.  i, *9-A1^^;  —  "/"  vä  'sui  ra/hwät  (sd.) nänAanat  Aaia  V._J.  14;  p.  40;  —  /rä  el dvqsaiti  . ,  'sui  yai  dastmim  /räihaoiÜ naum»m  paiti.rathwayHH  (sd.)  V.5.  28; 27-32",  8.  41",  70,  71,  g.  15-24  (oft);
27620:•  j.  'zan-  V,  'zeugen,  gebären',  von  ahuri- sehen  Wesen  ■'.  Praes.  5  *zazafi-'\  zizan-, II  ziin-i\    17  (FuL)  zqAya'*\  27  (Pass.)
27777:•  j.,  g.  zar-  V.  'erzürnen',  Praea.  10  b sarariu-^\  11  b  zaran-",  13  zaranya-^'', 30  (Iter.)  zäraya-;  Perf.  i  zazar-'K  — PPfP.  tar^ia-,
27781:erzürnen,  zornig,  ergrimmt  werden':  drvi zantS  zaranumanö*'*  zazarSnB'''  Yt II.  5;  —  mihrym  yim  ..  zaranimmm p3r3%ujafai3hs  vazmti  avi  kamayh  "M., den,  wenn  er  zUmt,  die  breithufigen  (Rosse) fahren  gegen  .  ."  Yt.  10. 47.
28045:•  j.  zazant-  Adj.,  PPA.:  s.  Aai-  mit No.  3.
28046:•  j.  zazaran-  Adj.  'zornig,  zornmütig'; gvtaÄe  .  .   'rattS  (GS.)  Y.p.  3o'>.
28048:•  j.  zazaräna-  Adj.,  PPM.:  s.  zar-  mit No.  a.
28049:•  j.  *zazäite"  Inf.  '(Kinder)  zu  erzeugen, zu  gebären"*;  vanta  . .  ySi  h»n  kikrpa srazsla  zaz'  "die  beiden  Frauen  . .,  die den  schönsten  Körper  haben  zur  Zeugung von  Kindern"  Yt.5. 34.
29683:i)  'sich  bemächtigen,  in  seinen  Besitz bringen,  gewinnen';  a)  mit  Akk.;  tri- %mttm  xia'hnm  zazaiti  (3SKPA.)''  Yt. 5.  i3o(?).  b)    mit    Lok.:    hanaema(3
== leaves ==
1041
```


## [2026-09-05T20:55:50.339Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"•  *j[.,].\\{0,40\\}z[äa]-  *V\\.\\|•  *j[.,].\\{0,60\\}uzy\\|uzayant\" BRT.txt | head -20",
 "description": "Grep Bartholomae za- verb and uzayanto"
}
```


### [2026-09-05T20:55:51.894Z] TOOL RESULT

```
3453:•  j.,  g.  aj-cit  ParL,  an  der  Spitze  des  Satzes und  Versglieds;  1)  im  Nachsatz  hinter ^fl/- ät:  a)  yatcil  tnqm  Iura  pazäayatita  ..  at- cit asim  tanöm  aguse  .  .  ajat  mqm  fra- guzayanta  "als  .  .,  da  .  .  da  . ."  Yt.  f^. 56.        h)  yatcit  Ävasf;fm {sd.)  *aaAyeiti..
7038:satz'so,  dann;  da.' -.yezi ('wenn') aAipaurva.- naem3l  3'  mqm  avi.rimilnaya  (sd.)  Yt.16. 2;  a.  3-3,  Y.2.43,  ^'.36,  103,  /ö'.ii,Nik. 3,  Vd.  13';  —  yat  ('wenn')  yave  dayat ä'  datva  y^ism  (sd.)  V.J. 32;  321,  H.  2". 13,  N.  IJ2;  —  3at  (s.  8)  yat  apö  uzbargnte .  .  a°  fraiasinti  . .  fravasayö  Yt.  13.65; V.  Ä40,  i7.4;  —  yat  ("als')  mqm  tura pazdayatita  .  .  3'  az3m  tanüm  aguze  .  . \3at  (s.  3)  mqm  fraguzayanta  ..Yt  i7.  55^'; — yas}  tat  nmäfum  äk^rstmn  .  .  «7°  mqm tnairyö  akasat  dai  (s.  2)  .  .  fräksrmaot V.  22.  i£;  —  3at  (s.  8)  yat  miirtm  .  . /radaöqm   .  .   a°  dim  danqm  ,  .  Yt.  10.  i ;
7265:13,  N.  Ö2;  —  äat  (s.  8)  yat  äpd  udiannte .  .  ä'  fralasinH  .  .  fravalayS  Yt  JJ.  65; V,  ^,40,  ^7.4;  —  yat  ('als')  mqm  Iura pazdayaiita  . .  ä°  azsm  tanüm  aguze  . . äat  (s.  3)  mamfraguzayanta  ..  Yt  i;.  553'; — yas)  Uli  mnärom  äktrirum  .  .  ü°  mam mairyd  äkasat  äat  (s.  2)  .  .  fräkirmaot V.  22.  if;    —    äat  (s.  8)  yat  mi>r)m   .  .
8584:•  j.  *uzayant-  Adj.,  PPA,:  s.  sä-.
8667:•  j.  uzya-  m.  EN.  eines  Gläubigen:  "ythe vankm3tayana?u  alaonS  "des  U.,  Sohns des  Vauhwiäta  . ."  Yt.  ij.  119.
8669:•  j.  uzyazcUüia-  m.  ein  Teil  der  Nase: 'na  F._jd.
8671:•  j.  ". ,  manayät  (sd.) , .  uzylflramayi"' DkB.  131.  '
8673:•  j,  'uzyeiti  xt  zavavat  (sd.)  hyatica.J" VyLjo.
8674:•  j.  "uzyö  F.5.
9875:mit^a  'aus  dem  Versteck  hervorholen': äai  mam  fraguzayanta  . .  "da  holten  mich aus  dem  Versteck  . ."  Yt. /".  55.
17388:•  j.  buzya-  Adj.  'von  Ziegen  herrührend, caprinus':  paya^ham ..'zyanamca  V.j.sa.
19402:—  y^tlH  vtqm  iura  pazäayatita  .  .  atai mqm  fi-aguzayanta  ..  YLJ7.56;  56;  — *daSaJ  zTmqm  avavata  daxsa (%^)yd^a  . . P.  22.  2)  Abi.;  a)  im  Ap.;  zu  a  a): tyJ'lam  hahma''  d^aAya"  .  .  ave^  .  .  Eh. /.  7;  8,0.6.3; — pasäv<r  kacama^  atars<i' Bh.2.4;  D.j.a;  —  imä  dahyäv^  tyä Aacäma"  Aami%''iy3  abava'  Eh.  2.  2;  5, ,?■  S.  13'  zti  33):  vahyatdat^ ..hauv *duvitty(^{sA.)ma^  udapatata  Eh.  5.5;  — mana  als  Abi.:  hauv  ''uvajam  hami^^iyam akunauS mana  Bh.4>3.  bi)  im  gAw.; zu  a  3):  yezT  ahya  \asa  psi  mai  xsayeht Y.44.1^,  n)  im  jAw.;  mäveya  als AbL;  zu  a  i);  ima  .  .  ya  mavSya  pasia vazstiti  Yt^.  95.  3)  Dat;  b)  nurn)  im jAw.;  zu  a  i):  uzvar^zai  (sd.)  mavöya mihB.matanqm^a  . .  Vr.  20.  2.         4)  Gen.;
20912:Nominativ  oder  dem  ihm  gleichen  Akku-' 12; —  Hat  mqm  fraguzayanta  ysi  i
27698:(als  LS.)*>  nidaihyqn  V.  6.43;  7.39,  S. 10;  —  ufträvhs  .  .  *uzayantB  (sd.)  tfmat Yx.ij.iy,  —  yB  . .  var>s3m  t^mäta^^ sayarum  (sd.)  vafnaiti  .  .  Yt  14.  3 1 ;  — vans?m  ztmäp'^  avaoirihffttfm  Yt.  16. 10;
```


## [2026-09-05T20:56:00.105Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"•  *j[.,][^\\n]\\{0,25\\}\\bz[äa][-']\" BRT.txt | head -30",
 "description": "Grep Bartholomae za headwords"
}
```


### [2026-09-05T20:56:01.892Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:56:04.332Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=27900 && NR<=28060' BRT.txt | grep -n \"•\" | head -60",
 "description": "List BRT headwords in z-range"
}
```


### [2026-09-05T20:56:06.142Z] TOOL RESULT

```
3:•  j.  zairi.gaona-  Adj.  (fem.  'na-')  'gelb-, vgl.  iirvizS.miuiya-,  wegen  *Jn  goldfarbig':  haemS .  .°nS  Y.p.  16,  10. 12";
5:•  j.   zaranyö.saepa-  Adj.  wo{rin,  -mit)  2,  ifi.  a)    sva.    'grünlich,    gelbgrün':
10:•  j.  zaranyo.pis-,  **pi9--  Adj.  (auch  fem.) 'goldgeschmückt':  yS  paoiryS  °pTsS  srirä barssnava  ginwnaiti  "der  als  erster  die goldgeschmückten  .  .  Höhen  erklimmt" Yt.  JO.  1 3 ;  —  fr3  gaosavara  sisptmna  .  . minu{%A.)ca  -/m  (ADf.)'>  YtJj.io;  — ya^a  vil  *>r?tats.pai'hi  (sd.)  yaia  vä *-pafki  {K'Pa.)''^  ydha  v<t  *kilat  gaonaiiam Aog.  ly.
11:•  j.  zaraoyö.pusä-  Adj.  (mask.  'sa-)  'mit
13:•  j.  *zaranyö.tninav-  Adj.  'der  goldenen Halsschmuck  trägt":  vaim  saranyB.pusim  . . ^'minum'^  ..  zaranyS.v^iim  Yt/j.  57-
15:•  ).  zaranyö.vastra'  Adj.  mit  goldenem Gewand  bekleidef :  vaim  zaranys^alm  .  . °nm  ..  taranyl!.aoknm  YLi5.  57.
16:•  j.  zaranyö.viir«9inan-  Adj.  'des  Brust- wehr von  Gold  ist':  mi^nm,.*man3m  Yt,
17:•  j.  zaranyö.vääa-"  Adj.  'des  Wagen  aus Gold  ist':  valm  *i»m  '*  . .  zaranyS.caxr9m Yt.  15.  57.
19:•  j.  zaranyö.tuvix&na- Adj. 'mit  goldener Verschnüning':  andvl . .  ao%ra  *päili. smuxta  'na  ". .  mit  Schuhwerk  angetan, das  mit  goldenen  SchnUrbändem  befestigt ist"  Yt.5.  64.
22:•  j.  zairi.gaosa-  Adj.  "mit  gelben,  gold- farbigen Ohren':  spanim  .  .  spaStim  'sim V.if.  16'  17,  18;  —  aspahe  ..  aurus'afie .  .  'sähe  Yt.Äi8.
24:•  j.  zairi£i-  f.  EN.  einer  gläubigen  Frau: 'cyi  asaonyä  ¥17^,139.
26:•  j.  "zairita-  Adj.  'gelb,  fahlgelb':  span>in 'hm  ca%ru.(asm3in  V.J.  16',  17,  18;  — ffiftM  .  .  yim  .  .  "iim  Y.  p.  1 1 ;  —  aisis 'iahe  Y.p.30; — yim  upairi  ^vis'^rao&at .  .  'hm  Y.g.ii.
28:•  j.  zairita-  in.  EN.  eines  Gläubigen: datahahe  'Iahe  Yt  13.  98.
30:•  j.  zairi.döiSra-"  Adj.  'mit  gelben,  gold- farbenen Augen':    haomü  frasmü'  .  .  'rS
33:•  j.  zairi-päSna-  Adj.  'mit  gelber,  gold- farbener Ferse  (?):  gattdarswan  (sd.)  yim 'n>m  YL5.  38,  75.41-
34:•  j.  zairina-  Adj,  (fem.  '«ä-)  'aufreibend, erschlaffend',  von  der  BsHyastä  (sd.): bU^yasia  yä  'na  V.U.  9;  —  ÖBsyashm 'mm  Yt  18.  2.^
36:•  j.  tairimya-  n.  'festes  Haus,  Gehäus'. KompA.;  Ableit  —  ai.  vgl.  harmyi-  n.;  s. daiu  IF.  /.  70.
37:•  j.  zairimyafsinan-  Adj.  -  ?  -'':  'ma {NSm.,  näml.  ist  der  Hund)  %ryafsma yaka  vals3 . .  °ma  %rya/sma  ya%a  jahika V.  13.  46  und  48.
39:•  j.  zairimyaDUra-  m.  Name  eines fAiftischen  Tiers,    'Schildkröte"':    da^m
42:•  j.  zairimyäka-  m.  anderer  Name  des zairimyamtra-:  daiumyim  tairimyatiunm (sd.)  nqma  yim  maiySka  avi  duivaiaaAS 'hm  nqma  aojaite  V.  13.  6.
44:•  j.  zairimyä'vant-  Adj.  'der  ein  festes Haus  besitzt',  vom  Mond:  mätthim  . . •vanfym  Yt  7.  5.
46:•  j.  zairi.varay-  m.  EN.  eines  Helden der  iranischen  Sage;  Sohn  des  Aurvat.- aspa  und  Bruder  des  Vlitäspa:  tarn  yasata aspsyaols  'vairii  *falne  apS  daityayS  Yt. J.  112;  117');  —  •»■^»7  asaonS  Yt  13.  101.
48:•  j.  zaurura-  Adj.  'altersschwach,  gebrech- lich':   han^  vä  'rö  vä  pairiitä.xludrS  vcl
51:•  j.  'zar«ta-  Adj.  (fem.  'tu-),  PPfP.: s.  zar:
53:•  j.  'zar«ta-  Adj.  'altersschwach':  ya'^a narpm  a/avanam  "duscä  'tarn  uparät  rtal- mät  nasul  aoi  ava  *^ravTt  (sd.)  P.  23; V.  J.I3PÜZ.
55:•  j.  zaronaena-  Adj.  (fem.  'nagHi-):  s. I  unter  taranaMa-.
59:•  j.  zartnav-,  taranav-  m.  'Gold'. KompA.;  AbleiL  —  VgL  laranya-.
60:•  j.  zarannmaiti-  L  Naioe  etnes  Flusses**: trayS ya(  kasaim  . .  avi  tjm  arihaiUacatti .  .  'maHla  Ytiff.66L
61:•>  Eid  Nebenfliui  des  Hilmand.  Bd.  2a  34 pilt  Zarrhtmand  all  andrer  Name  des  Hilmand. VgL  We»t  SBE.  5. 81  No.  9.  S-relw  lA.  ig.  23.
63:•  j.  zar90U>manay-  Adj.  'mit  goldenem Halsschmuclc':  kahrkäsd  •mainii'^  yt.  14.
64:'tnattay-  m.;  «L  manäy-  m,,  laL  TgL  "«i^i IF.  J.  17».  —  Vgl  minav-.  —  Spü-:  w«. mand;  t.  dagegen  Bd.  /p.  35:  karkai  i  lar- man  mämsH  (bei  Westi  'dwelling  in  decay"). —  *)  Es  könnte  der  Bartgäcr  damit  gemeint »ein.  —  »)  NA.  •mainyui,  f.  aber  J  lO.  Um- kehning  der  ^368.  14  beiprochenen  Scbrelb-
65:•  j.  zarsnu'mant-,  zaranu'mant-"  Adj. 'Gold  enthaltend,  goldhaltig":  •manism bavähi  ya%a  yat  asti  'matö  tnaSytinake Vyt4''-  A)  mit  *süra-  m.  fsd.)  'aurata lacuna',  Name  eines  Sees  oder  Teichs*': 'manttm  saT7m  Ny.i.  8;  —  •manlB  surake FrW.5. 1.
66:•)  Kd.  32.  6  kennt  einen  See  (mw-)  Zarrn- mand  in  llamatän.  NpöErl.  verlegt  satrin  älat 'das  goldene  Gerät'  -  so  Tür  z*  s'  -  anf  den ^tx^Saugand  {^.  siu>k>Hla-)\  danach  dachte  man sich  :*  s'  als  eine  bis  zum  Fuss  des  Bergs hinabreichende  Irichterartige  ÖHhung,  durch  die das  Wasser  auf  dem  Erdboden  zum  Himmel sieigl  {pa  an  türäx  ab  t  iah  i  arniln  bat  äsrnän iälä  lavaJ).
70:•  j.  *zaranya-'>  Adj.  'golden':  arfdvf  . . 'nya  ao'hra  (sd.)  *f>3iti.smaxta  Yt.5. 78; —  vatnm  .  .  zarSt/  (sd.)  ayan?td  fra- hixfym  .  .  *'n}-ehe  Yt.  10.  13z;  96,  I
72:•  j.  *zannaya-'',  zarjmaya-  m.  'Früh-' ling':  misti  urvaranam  xatri^aonanam °malm  paiti  ztm^a  *uzuxsyänti  Yt.7.4.
74:•  j.  ■'"zaramaya-''  Adj.  'venius':  :far3~ %anam  hi  bantam  'yehe  raofnahe  (sd.) H.2'i8.
77:•  j.  *zairyank-''  m.  SN.  eines  GBobigcn: aiatan'jahe  *yqs  (Nom.  statt  Gen.)"  Yt /J.  114.
78:Eig.  'gelblich',  vlt.  Knrmame.  —  Ableit.  aoi (Komp.  mit)  uiray-i  vgl.  zairit-,  zairiii-  and aL  k-ityäni-  Adj.  'weis^ch'.  —  •)  So  J  10, Mf  3;  NA,  jaity:  —  i>  s.  BTHL.  Stod.  /,  80, Cm.  GGA.  iS^.  374.
79:•  j.  zaurvan-  m.  'Greisenalter,  Alteis- schwäche':  tail  'va  . .  »i»Y  vanhyus  Y. 9.5;  —  ■»«  °vqm{,h&^a  mpffkyümca  Yt g.  10;  ■ —  'va  *duidq  (sd.)  f^rS  Jonttaoiti V.  ig.  43;  F.  20;  —  amm  ..  Osistsm •vJfum  upäiti  yat  spStts  ySi  . .  "das  . , kommt  am  raschesten  zur  Gebrechlichkeit des  Alters,  (was)  die  Himde  (sind),  die  . ." V.  13.  a8.
81:•  j.  zar9&-  V,  'zerren';  nur  mit  Praev. Praes.  3  sanSa-^\  —  PPfP.  •larsta-.
90:•  j.  zarSayamna-')  Adj.  'die  Federn  auf- stikubend':  tmnyahe  . .  väryynaAe  . .  yS vazaite  °nB  ayrqm  usaitim  usaahtnt  "des Vogels  K,  der  ums  erste  Morgenrot  fliegt, seine  Federn  aufsträubend"  Yt  i4-  ao.
102:•  j.  zarätvaena-  i)  Adj.  (fem.  *nr-)  'aus Stein':  yezi  anhat  zar/naiai/ (sd.)  . .  'ms
106:Ableit.  ans  larjtva-.  —  Pia.:  lanjäi, •  i-,  g.  zasta-,  p,  dasta-  m.  'Hand',  uzw, uÄKnscher  Wesen"';  i)  in  eigentlicher  Be- deutung, von  Menschen  und  Göttern:  in yazaiU  .  .  gaomata  °ta  (IS.)  Yt.y.  50;  — tara%ustrS . .  asünS  'la  draiimnB  V.  ip.  4; 19;  —  mtknm  ..yS ..vazr?m  °taya[lS.) ^draiimnB    Yt. /O.  96;  Y,57.  31,  V.  /p.  ig;
114:•  g.,  j,  zasta'vant-  Adj.  'tatkräftig'":  _yJ hsi  dadat  'vai  avS  "der  ihm  (dem  Rind) tatkräftige  Hilfe  gewährt"  Y,  2p.  9;  —  'vat
117:•  g,  zastä-iSta-  n.  "Wunsch,  Weisung  der Hand,  Handwink'*':  itrsi  (Sp.  i84f.)  zi xlms  . .  'ta  ya  nä  ^ä^rl  däyät  ". .  die Handwinke,  die  uns  ins  Paradies  versetzen" Y.  jo.  s;  —  stdi  rapanli!  ciirä.avaa^m (sd.)  at  masdä  daibisyant!  'tais  d>r>sta.- amataksm  ". .  aber,  o  M.,  dem  Feind  sicht- bare Qual  schaffe,  gemäss  deinen  Hand- winken" Y.j4. 4.
130:•  j.  zastä.maräta-  Adj.  'durch  Hand- schlag geschlossen',  von  mihra-  m.  'Ver- trag'": bityS  (näml.  mt^rJ)  'ts  "die  zweite (Art  des  Vertrags  wird)  durch  Handschlag geschlossen"  V,  4.3;  —  aisS  mihrB  ..yS 'IS  V.  4.6;  —  ys  mlhnm  aiwi.druiaiti yim  'tftn  V.4I.  12.
132:•  j.  zastö.franö.-masah-  Adj.  'des  Grösse die  Hand  fiillt,  so  gross,  umfangreich,  wie man  es  in  der  "Hand  trägt":  aSsmanamtit . . 'sibls  {tiAtoL  stäis)  A.J.  5,
136:•  j.  ■•'zastö.niaza-"  Adj.  'durch  Ver- pländung  der  Hand,  durch  Handschlag  ge- schlossen'*': °«J  (^3t  framanzaiii  'zö  ähäl antan  urvaifya  (sd.)  frada'^aiti  V,  4.3.
137:•)  Eig.  'wobei  Verpfandung  der  Hand,  des  Hand- gelübdes stattfindet';  auch  uufÄmurZ/a- genannt.
144:•  j.  *2ast5.niitay-"  Adj.  (auch  fem.)  'das Mass  der  Hand  habend',  von  Flüssig- keiten sva.  'soviel  in  die  hohle  Hand geht,  eine  Hand  voll';  ala  alia  näirika *'fim'^  ap;m  franuharai  "und  es  soll  die Frau  eine  Hand  voll  Wasser  trinken"  V. 7.71.
145:Zum  V.  mä[y'y;  ai.  milay-  t  —  Pü.:  luväaT- m.  —  »  So,  •rni/Tm  Kl;  L  1,  Pt  2  haben •maJlfm  (s.  S  36S.  9\  NA.  'maüi.
146:•  j.  zazant-  Adj.,  PPA.:  s.  Aai-  mit No.  3.
147:•  j.  zazaran-  Adj.  'zornig,  zornmütig'; gvtaÄe  .  .   'rattS  (GS.)  Y.p.  3o'>.
149:•  j.  zazaräna-  Adj.,  PPM.:  s.  zar-  mit No.  a.
150:•  j.  *zazäite"  Inf.  '(Kinder)  zu  erzeugen, zu  gebären"*;  vanta  . .  ySi  h»n  kikrpa srazsla  zaz'  "die  beiden  Frauen  . .,  die den  schönsten  Körper  haben  zur  Zeugung von  Kindern"  Yt.5. 34.
152:•  j.  zazuätlima-  Adj.  'der  im  Kampf am  meisten  gewonnen  hat,  der  siegreichste' ; yö  nä  Ms  hubsrsta  iaräj . .  sasta  dairiAtus . .  hu  aahaiti  °mS  xiayS  kasHt  masyünqm "wen . ,,  der  wird  der  siegreichste  Herrscher werden  .  ."  Yt.  13, 1 8.
154:•  j.  zazvah- :  zazuS-  Adj.,  PPfA, :  s.  hat-. Ableit.
155:•  j.,  g.  zah-  V.  'verlassen,  im  Stich  lassen'. Praes.  ^^  za/iT-'K  —  PFP.  zaßyH'.
159:•  g,  zaKya-''  Adj.  'der  im  Stich  gelassen, dem  Verderben  preisgegeben  werden  wird, soll';  'XyäSs'^  (NP.)  vTspSnhS  xraospntqm upa  Y.5?.  8.
161:•  ].,  g.  zä-  V.  'gehen',   nur  mit  Praev.
```


## [2026-09-05T20:56:12.114Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '28055,28085p' BRT.txt",
 "description": "Print BRT za- entry"
}
```


### [2026-09-05T20:56:12.167Z] TOOL RESULT

```
mit  fi-ä  'im  Stich  lassen,  verschwinden aus  — '  (Akk,):  ma  yave  imat  ttmSmm  . . ^armS  frazahlt  Y.  60.  7.
».jasalt  'deficit'  (intr.).   —   PiL   (lu  Y.  &>):
zä(y)-
•  g,  zaKya-''  Adj.  'der  im  Stich  gelassen, dem  Verderben  preisgegeben  werden  wird, soll';  'XyäSs'^  (NP.)  vTspSnhS  xraospntqm upa  Y.5?.  8.
PFP.  mm  V.  sak:  —  Pü.:  ianiSn^manJ.  — ■)  X  statt  h  vli.  nor  wegen  des  folgenden  S, vgl.  aiahyä  —  aiaXyäcä,  %  2S6  No.  3.
•  ].,  g.  zä-  V.  'gehen',   nur  mit  Praev.
Praes.  i  sa-,  37  naya-,  —  Inf.  •«?.
mit  a  1)  lierangehen,  herankommen', ohne  Zielangabe;  at  vsyaoja  t^j/ty!nff(sd.) aurvats.  .yäis  azä%a  {2PKA.)  ", .  Kenner . ., mit  denen  ihr  herankommen  sollt"  Y. 50.  7.  a)  '(feindlich)  gehen  gegen  — ' (Akk.):  s.  Inf.  *az3.
mit  ut  'aufspringen,  sich  au&ichten': ultränhs  . .  *usayan/ö'^  zfmai  ptntamna (sd.)  v<&airyav5  "die  Kamele  . .,  die  vom Boden  sich  (auf  den  Hinterbeinen)  auf- richtend . ."  Ytr7. 13.
ai.  /iii/tt\  ahd.  ^J«(?)3).  —  Pü.  (tu  Y.  so): gtiflär  iaväne,  Sü.:  aiya  gj-hTlä[rii\  iiaz-imi; vgl.  in  au  mit  No.  3.  —  >)  NA.  acjayerii,  ]  10 uzayanH.  iSchr.  s.  S  304  ü.  36.  —  »)  Wie ta  einer  ö(j')-Wuriel ;  s.  ZDMG.  43.  663.  — 1)  Vgl.  die  Litt,  bei  Osthoff  Suppletivw.  5;.
•  j.,  g.  zä(y)-'l  V,  'mittere'.  Praes.  i  «/-, 3  21JJJ- :  tatay-,  zaz-,  4  eaya-,  24  sayaya-.
'entlassen  aus  — '  (Aaca  mit  AbL):  aprm zatäAi  tum  . .  zrayanhai  haca  vourukasät ^'  5-  '  S  >  ' —  äp9m  saznmi  az»m  .  .  tra- yanhat  haca  V,  5. 17.
mit  avä  'entfernen,  verscheuchen';  _yÄ'.. ärmaÜTm  .  .  b?r?xhqm  (sd.)  .  .  aiasazat (3PPrA.)'>  Y.34.  9; '—  aat  tl  aivö  ahunS vairyü  .  .  *samanguza  avasai  (jSPtA.)^ vtspe  dafva  Yt. /p.  81.
mit  upa  und  frä  'herzulassen,  -filhren': äpim  .  .  upa  astsm  frazayayähi  V.5. 16; —  3p}m  .  .  upa  astim  frazayaylmi  V. J.18.
mit  fru  'herzulassen,  herholen' :  fra  mi gt&wa  sazayqn^''  niibinta  {%A)  V,  &  37.
mit  vJ  'ßihren  lassen,  sich  scheiden von  — '  (Akk.):  ivJtaya'ka''''  magjm  tfoi ai . .  "scheidet  ihr  euch  (aber)  vom  Bund, so  .."  Y.5^.7.
tC\.jäkäÜ  'er  lässt  im  Stich'.  —  Pü.  (lu  V.5.
15.  >7.  Ä  V.  53)--  gri/t<,ni\  (zu  Y.  34,  V.  5.
16,  18):  Aillan.  —  ')  $  313.  la  —  »>  S  'W. 16;  vgl.  ai.  JahaH,  3PPA.  Falsch  MiLU  G. 50+.  —  a  Thera.  —  4)  Statt  vh:   AnflaUige
dby  Google
Sehte  Lbung.
i)   S.  in  saanß  a
•  j.  zita-  Adj.  (fem,  •«-)   i)  'geboren';
uita  nB  'IS  äirava  yS  .  .  zaraku^trS  Yt. A?-94i  ^■I9-4Ö;  —  hiliqmca  atshusamca 'lammca   aziitanqm'a    ahotiam   Y.G^.ö;
—  yazatanqm  .  .  'tanqmca  asätanqinca fi-ai5.car)'irqni   sao^yantqmca    Yt  ig.  22;
—  narqmca  'tanqmca  sqhyamnanqnt^a (sd.)  Y,  4-  S'i  —  ^^annatiuhaslimS  °tanqm Y.g.  4.  2)  'jetzt  vorhanden,  jetzig';  ya/ asti  airyanqm  dahyunqm  'tanqm  (GPf.) aziitanamca  (sd.)  Yt  ig.  56.
KompA.  —  ri'fP.  iura  V.  -.an-.  —  ai./i/a- Atlj.,    nip.  Siit;    rp.    vgl.  :.i</a.    —     Pü.;    :ä/,
•  j.  nsil  hväzaiö  nöii  "zäniti  FrD.  7.
•  j.  zänu.dräl|ah-  Adj.  (auch  fem.)  'im Vorstrecken  des  Kinns  bestehend':  aEvahe zl  .  .  anasaonS  v'l  (NSf.)  .  .  ü/riti^  (ßAy V.  16.  II.
*:iinav-  f.  'Kinn'');  vgl.  %\.  hänav-  f.,  np. zaiiiix.  —  Pii.;  züiiak  drahnäk.  —  ')  Vor- strecken des  Kinns  bei  gleichzeitigem  Streifen des  llandiückens  vom  Ilats  her  nach  dem Kinn  tu  drückt  in  Italien  Geringschätzung aus.  —  >)  Das  ä  ist  aufrälÜg;  man  hat  das Wort  dirtim  mit  'Knie'  übersetit  —  lulelil Gdn.  SPreussAW,  ig.  414:  'Kniestoss' -  und zu  ai.  j'iinit  n.,  np.  zitiii  gestellt  Aber  Pü. spricht  nicht  dafür  j  'Knie'  wäre  zänüi.
•  j.  *zämaoya-"  m.  'Bruder  des  Schwieger- sohns': 'yö  F.  20.
```


## [2026-09-05T20:56:34.529Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"•  *j\\.  *zy\" BRT.txt | head -20",
 "description": "Grep BRT zy headwords"
}
```


### [2026-09-05T20:56:34.581Z] TOOL RESULT

```
28278:•  j.  zyä.;  p.diyä- V.  'schädigen'.  Praes.  1 1 \sina-,älf^ä•■.äln''^,3^  (Pass.) ya-";  Perti \*üy.  —  PPfP.  äOa-'^i  Int  syänai.         S.
28291:!  •  j.  zyänay-  t  'Schädigung':  aSif  akmai \ä  *'nlm'^  nsit  vtesptm  xsta  mätdayatmti
28299:•  j.  zyänä-  f.  'Schädigung,  Schaden':  mä duibirgt^  (sd.)  'nam  . .  yasBü  aom  nanm YL  /.  24.
28301:•  j.  zyänäi  Inf.  'zu  schädigen';  */raiain- tlmca  .  .  ytAkä  .  .  naicisia  aidhä  yäsäiti zy"  ", .  und  die  keiner  suchen  soll  zu schädigen"  V.Ö5.  ii.
```


## [2026-09-05T20:56:36.837Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '28300,28345p' BRT.txt",
 "description": "Print BRT after zyanai"
}
```


### [2026-09-05T20:56:36.890Z] TOOL RESULT

```
Zum  V.  «►■"•■  —  S.  noch  *syanay-  No.  2.  — Pü. :  jw/o  ^ähÜH  tari  öi  marl  rat,  etL :  kti tyän  tu  häiit.
•  j.  zyänäi  Inf.  'zu  schädigen';  */raiain- tlmca  .  .  ytAkä  .  .  naicisia  aidhä  yäsäiti zy"  ", .  und  die  keiner  suchen  soll  zu schädigen"  V.Ö5.  ii.
Zum  V.  zyä-.  —  Pü. :  mä  iat  Siän  rä\  ;fäAäl zyän,  eil. :   iusän    mä  taväit    baiiät  kort  i^äsl.
•  j-  zyeit  F.  25  b ''.
Pu.:  ünilär.  —  ')  Nach  Pü.  «om  V.  syä-.  \\L kUE  "zyeUe  |PasS.)  verderbt,
j.  cyi:  s.  unter  iyam-.
y  lyu-asraifmUm  N.  6S:  lies  si  ai'asr:
•  p.  *zra"ka-'*  m,  Name  eines  1-andes'', Drangiana:  imä  dahyäv<^  tya  inauä  fati- yäis'a"  , ,  farkava''  'k<^  haraivc^  £h.  7. 6;
•0.5.2,6.,.
Bei  den  Griechen  Zäpäyyti,  Zapafpi.  —  >>  NA. :af'.  —  ')  Eig.  Volksname;  ».  in  jaio-.  Nach Ggr.  GlrPh.  s.  393  lOlL  z-  freilich  'Seeland- Schaft'  bedeuten;  mir  ist  nicht  deutlich, wie  das  Wort  mit  irayaA-  zusammengebracht werden  soll.
•  j.  zarammna-  Adj.,  PPM,;  s.  xar-.
•  j.  zaranumana-  Adj,,  PPM.r  s.  xar-.
•  j.  zrayaoha-  m.  EN.  eines  Gläubigen, Bruders  (?)  des  SfifntSjera  (av-  '* :  'yanka (GD.)  sp?nts.xratva  aiaonä  Yty.  115,
Ableit.  aus  zrayaA;  also  etwa  'marüuis'.  ~ ')  Vgl.  Dk,  7-  7-  8
•  j.  zrayana-  Adj.  (fem,  °«J-)  'marinus': äp^m  xayanqtn  .  .  itffm  'nqm  ".  .  das Meerwasser"  Yt.  6.  2,
Ableit.  au$  stayaA-,  etwa  lu  NS.  a-ayö  oder IM  KasusFormcn  nach  der  a-Dekl,  (vgL  p. ärayani)  nach  Mustern  wie  v/üanana-.  —  PQ, : äp  i  zray.
•  j,  zrayah-'>,  p.  ''drayah-'*  n.  '(ausge- dehnte  Wasserfläche    sva.)    See,    Meer";
il  i)  im  Ap.T  intäm  yuviySm  (sd.)  .  .  abiy •ya^  /ya*  hals  parsa''  aifiy  \i.i-j.y,  — abiy  'yam^hS,^^  Bh.5.  4; — ^  im  Gegensatz zum  Festland;  yauna  (sd )  tyaiy  *uikaAyä Uta  tyaiy  *yakya  (LS.)"  D.  5,  a.  a)  tyaiy 'yaiy/f  'qui  in  mar!  (habttant)  sva.  Insel- bewohner' steht  unter  den  Provinzennamen des  Reichs  Darius  I.:  imä  dahyavJ'  . . arabnyt^  mudrsy<^  tyaiy  'yakyä  .  .  Bh. 1. 6.  2)  im  jAw.,  nur  von  bestimmten
Wasserbecken;  a)  mit  vQuru.kala-  (sd., auch  fdSt)  Name  des  Weltozeans:  'yö °s>m  Y.  Ö5. 3  usw.;  —  'yaiahs  *safa  V. 42.4  usw.;  —  'yatahat  kaca  'sätYtS.2^ usw.;  —  'yanhaha  hala  'Ist  Yt  Ä  47 ;  — •^«  (LS.)"  'saya  YL5.38,  ÄS;  —  'yä (LS.)«  •iaya  Y.(5'5.4;  —  ^^  'yH  (näml. °üm)  äyactayati  ¥1.^31;  31^;  —  6u»pm °yanks  (näml.  'sähe)  Yt/5. 51.  b)  mit poitiia-  (sd.)  Name  eines  mythischen  Sees: 'yB  'k)M  V,5. 18;  —  'yarihat  haca  'kät ^■5-  '9J  —  *antar3.ar}'i3m  'jaw/i^  (näml. 'kahe)  V.5. 19.  c)  mit  kasaoya-  (sd.) Name  des  /fJmffm-Sees:  'yS  yat  kasalm Yt  19. 66.
KompE. ;  Ableit.  —  ä.  j'räyai'  n.  'Fläche', mp.  (Pü.)  iray,  np.  daryä  (woiu  Hbm.  PSt 62).  —  ')  So  auch  y.  42. 4  au  lesen,  wo  NA. sarayö  neben  zrayaohö  bietet.  —  ')  NA.  da- ray'.  —  J)  Nach  der  o-Dekl  ;  aber  die  Form ist  nicht  sicher.  —  *)  FrMOllbr  WZKM.  //. 3S6  hat  ZDMG.  46-  298  jedenfalls  nicht  nach- geschlagen. —  i)  Wegen  der  LS.  traya,  srayä (so  Pt4  lu  Y.  55.  4,  F  I  ru  Yt.  J.  4.  *■  3"  J NA.  hat  auch  trayäi),  beides  verderbte  For- men, s.  Bthl.  ZDMG.  43.  668,  4S-  [49-  Anders FoY  IFAni.  3.  18.
•  j.  'zraz-dä-  kompV.  'vertrauen,  glauben'. Praes.  i  zrazda-.  —  Inf.  *sraiäatai-ia.
yä  ml  äamam  .  .  tras'a  dsi'*  apita aotäi  "dass  sie  an  meine  Reli^on  glaube und  sie  begreife"  Yt^.  26.
Aus  ar.  *iri^dhä~  durch  votkietj'mologischen Anschluis  an  sind-  'Heri';  s.  Cld,  KZ.  J/. 272,  woEU  JusTI  NB.  381.  Zur  trad.  Fassung (,  Bthl.  IF,  g,  277.  —  >i,  h-addhä-  'eredere'. —  >)  iTrenn.  s.  RV.  a.  12.  J  (u.  ö.),  ferner □nter  manä-,  mqtdä-,  yaoiää-.
•  g.  *^zraz-dä-''  Adj.  'gläubig,  gläubig ergeben':  ysi  'da  (NT.)  atffiTn  inatdäi "die  dem  M.  gläubig  ergeben  sind"  Y. 31.1.
KompE.;  Ableit  —  Zum  V.  trasda-,  —  au vgl.  iraddha-  Adj.  'credulus'.  —  Pü. ;  ranioi da^H,  SB.:  fravftHdäh.  —  ')  iSchr.  t.  BTHL.
ZDMG.  4S.  149,  Cld.  KZ.  sj-  461.
dby  Google
1703
'daeta-
1704
•  j-,  g.  'zrazdätay-''  i)  f.  'Vertrauen auf  -,  Glaube  an  -';  a)  mit  Akk.  oder Gen.  (obj.):  °ääittm  ma^nm  spjntjm  "den Glauben  an  das  heilige  Wort"  Y.  25.  6;  — 'dälSÜ  ma^rafte  spmtake  V.  22.25.  ^)  ™'^ Inf.:  sadra  mffi  sas  (sd.)  . .  •däUi!  tat vfmyddyai  hyal  .  .  Y.  43.  11.  LS, *'dätal-ca  als  Inf  sbes.  a)  Adj.  (auch fem.)  'vertrauend,  gläubig':  'datüit  aahuyat (sd.)  haca  Yt  10.  9.
Zum  V.  triada:  —  Vgl.  Urasdälay.  EN.  — Pü. :  rmaii  dahünlh.  —  i)  NA.  hat  bald  mrazd', bald  zratd'  (Vt.  14.  2,  Yt.  IQ.  51,  13. 91);  ■-  lu
•  j.  'zrazdätay-  m.  EN.  eines  Gläubigen: 'dätsi^  falsatavAs  asaonH  "des  Zr.,  Sohns des  P.  . ."  Yt  13. 1 1  s.
Vgl.  'ttaxda/ay.
•  j.  *zrazdätae-i-a "  Inf.  'zu  vertrauen auf—,  zu  glauben  an  — ':  yamaheca  hapia-
nhätöis  .  .  gr*  Vr.  1$.  3.
Zum  V.  iroßdä-;  vgl.  xriudälay:  —  Pü. ;  rmaäi  \ dahiinih.  —  <)  So  K;  a;  NA.  taraidälayaHa.  '
•  j.  zrazdä'tama-  Adj.  'der  gläubigste  \ an  — '  (Akk.):  yaäsra  narS  .  .  aiam  h3nti\ 'tgma  ". .  am  gläubigsten  an  das  heilige Recht"  Yt  13.25.  !
Superl.  aus  »'■»mWä-;  s.  äätama: — Vgl.  «»■(«- ;
•  g.  *zrazdiSta-''  Adj.  'der  gläubigste': 3i»/(sd.)  'dtüö  Y.5^.  7.
SuperL  zu  '*zr(adä-%  vgl.  iratdäiima-.  —  Pü.! rawel.  Sä.:  fira^arel  "loU  Torwarts  gehen".  —
")  NA.  larazd:
•  j.  zarahyah-"  Adj.  (fem.  *°he.hT-)'^  'der mindere,  schwächere':  aivayacil  *aisms.- b»rHü  ..  bar?zy!}  ^ahm*^  •Ar.:Är/ (NSf.) " drufim  (statt  NS.)  "durch  eine  einzige  Dar- bringimg  von  Brennholz  und  . .  wird  das Ma  erhöht,  die  Dr.  geschwächt"  P.  24-
Vgl.  ai.  hrisiyo!-  Adj.,  Koropar.  zu  hranrd- Adj.;  Bthl.  IF.  5.  368.  —  Pu.:  *täAismAa i  drui,  erl. :  kui  apt  kähentt.  —  1)  D.  i.  irak', troti  Bgm.  Grdr.»  /.  745 ;  vgl.  lu  '^trati/ä-.  — >)  Hds.  'Ar  Aö.  —  J)  DsT.  (und  Blocket): tisishaaÜh  i  drüj  . .  .
•  j.  zräda-  m.  'Panzerkoller,  Panzer": yaisqm  xayanam  rahsi^ti . .  haptakiS  'is  V. i4-9l  —  *°aahe''>  ..paiti.dSnake  Vd./2.
arm.  LW.  zrahk';  vgl.  mp.  (Pü.)  trik,  np.  zriA (vom  Hbu.  IFAni.  10.  31).  —  ■)  Das  itt  mit tarahithe  gemeint.
```


## [2026-09-05T20:56:49.818Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gestern\" HRN.txt HUB.txt | head -20",
 "description": "Grep Horn/Hübschmann for gestern"
}
```


### [2026-09-05T20:56:49.869Z] TOOL RESULT

```
HUB.txt:1327:303. Slvend. para Vorgestern' (Journ. asiat. 1893, 294)
HUB.txt:4023:gestern, zUmad 'Brautigam' (Jezd, ZDMG. 35, 341, 361;
HUB.txt:4024:36, 58, 59, 65, 78), zunun *ich weiss', ezi gestern', zUmo
HUB.txt:4027:dt gestern*, damad 'Brautigam, Schwiegersohn' u. s. w.
HUB.txt:5912:parBr Vorgestern - ap. paruva- friiher + ^ayar-^ zd.
HUB.txt:7843:6) dahan 'Mund* = zd. zafan-^ 7) d^, df^ gestern = skr.
HUB.txt:8589:(nom.); dig gestern' (neben di), bal. zlk; xug 'Schwein
HRN.txt:2923:303. peren 'gestern', perendös 'gestern Nacht'.
HRN.txt:2974:811. perer Vorgestern, perejröz, pere\seb.
HRN.txt:5243:kurd. duc; afy. LW. dös; oss. disson 'gestern Abend'
HRN.txt:5284:590. dT, dtg 'gestern', :m (Is. 30, 33), dme, diröz^ dlseh.
HRN.txt:5286:ai. hyds gestern; phlv. dik (PP61.) ^).
HRN.txt:5287:kurd. LW. 8cSve]dl gestern Abend'; oss. d. azine,
HRN.txt:5288:äzinä, t. znofi, zinon gestern' (11); bei. zlk^ zi (427);
HRN.txt:5297:'gestern' ohne Stern und — leider auch ohne Belog.
```


## [2026-09-05T20:56:50.123Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"yesterday\" SOD_pages.txt SOD.txt | head -20",
 "description": "Grep Gharib Sogdian for yesterday"
}
```


### [2026-09-05T20:56:50.177Z] TOOL RESULT

```
SOD.txt:16967:the  day  before  yesterday  ? 
SOD.txt:23405:yesterday 
SOD.txt:63794:yesterday 
SOD.txt:88642:day  before  yesterday     1416 
SOD.txt:95608:yesterday    2376,  8298 
SOD_pages.txt:7846:      the day before yesterday ?                                      ar5yf, ar5ef   0r8yf-)     ©<*drafaya
SOD_pages.txt:10616:                                                                      yesterday
SOD_pages.txt:27656:     yesterday                                                              100c5
SOD_pages.txt:37966:crore    5068                            cut     1043, 6863                      day before yesterday      1416
SOD_pages.txt:39969:                                        yesterday 2376, 8298
```


## [2026-09-05T20:56:54.232Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5280,5300p' HRN.txt; echo \"---HUB 7840---\"; sed -n '7838,7850p' HUB.txt; echo \"---HUB 8585---\"; sed -n '8583,8595p' HUB.txt",
 "description": "Print Horn 590 and Hübschmann contexts"
}
```


### [2026-09-05T20:56:54.297Z] TOOL RESULT

```
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
*) Bei Fi*k findet man im Wörterbuch* mehrmals ein aw. zyö
'gestern' ohne Stern und — leider auch ohne Belog.
9*- 132 —
591. debä, debah *Brokat', arab. dliäj; debäce * Vorrede*.
ai. l/'dlp-, drpyate ^flammen, strahlen, glänzen*;
---HUB 7840---
tar"; 2) danad er weiss', ap. adana er wusste', gd. zanata
2. pi. ; skr. jfanati; 3) rfws^ 'Hand' = ap. dasta-, zd. zasta-^
skr. hasta-, arm. dast-ak, dasf-a-kert; 4) di? *Herz' = zd.
zered'^ zaredaya- (vd. 1,3), skr. Ard-, hrdaya-] 5) d(Js^
Treund' — dostar = ap. daustar-, vgl. zd. zaosa-, skr. y^/s ;
6) dahan 'Mund* = zd. zafan-^ 7) d^, df^ gestern = skr.
%as; darj/a *Meer' = ap. dray a- (oder drayah- ZDM6. 46,
298), zd. zrayah-, aber dial, zarah^); 9) ap. adam *ich' —
zd. a^g;M, skr. aham; 10) ap. adm^ *er nahm' = zd. zinat,
skr. jinati- 11) ap. ayadana- 'Tempel', zd. ya^ Verehren',
arm. yazem opfere , phi. paz. yazisn Terehrung; 12) ap.
gud Verbergen = zd. guz\ 13) ap. dida- Testung', vgl.
np. dizy diz^ dBz *Burg' aus "^diza-y ^daiza-, oben p. 62.
---HUB 8585---
§ 135. Das im Phi. auslautende suffixale k ist verschie-
den behandelt worden, und zwar 1. nach den obigen Regeln,
wenn es a) nicht mehr als Suffix empfunden wurde oder
b) nach Konsonanten stand; 2. unregelmassig, wenn es als
Suffix empfunden wurde und nach Vokalen stand.
1. Regelmassig: a) sag *Hund' = med. andxa, zd. spa
(nom.); dig gestern' (neben di), bal. zlk; xug 'Schwein
(= xuk) H. 510; b) nach tonlosen Konsonanten: xusk
*trocken = ap. uska--^ bizisk 'Arzt*, arm. hmk (vgl. bal.
rdpask *Fuchs', makask Tliege', musk 'Ratte', Geiger,
Lautl. 26); c) nach tonenden^): buzurg 'gross' = sl^, vazrka-;
marg 'Tod' = zd. mahrka-; suturg 'stark', vgl. skr. sthilra-;
bang *Ruf, Stimme* = phi. vang^ arm. vang^ vanh, bal.
```


## [2026-09-05T20:57:15.463Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} {n=NR} /gestern.*ohne Stern|590\\. dT, dtg/ {print \"HRN leaf\",NR}' HRN.txt; awk 'BEGIN{RS=\"\\f\"} /dig gestern. \\(neben di\\)/ {print \"HUB leaf 135:\",NR} /d\\^, df\\^ gestern = skr/ {print \"HUB leaf dlist:\",NR}' HUB.txt",
 "description": "Find leaf numbers in HRN/HUB"
}
```


## [2026-09-05T20:57:16.351Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"zyy\" SOD_pages.txt | head -20; echo \"-----\"; sed -n '27650,27660p' SOD_pages.txt; echo \"-----10610\"; sed -n '10605,10625p' SOD_pages.txt",
 "description": "Grep Sogdian dict for zyy"
}
```


### [2026-09-05T20:57:17.300Z] TOOL RESULT

```
HRN leaf 153
HUB leaf dlist: 231
HUB leaf 135: 251
```


### [2026-09-05T20:57:17.367Z] TOOL RESULT

```
4700:320 Hwrt- =» sw>rt-                                            333 "wzyy    M =» 'wz'k
4750:    owaze, awaze (*wzyy, Wnh) =^*w}zh
7231:     anxez ©caus. st. ^'ny'yz-, 'nx^z-, }nzyynt-                          AVS 74
7279:      anya-zangawe                                              1230 *nyy my5      S =» }zyy myS
7351:1246 'nzyynt-           S, C                     j^yi
7845:      (3)poze-me0 ? =^zyy my5                                   1428 >r8\p-       B                              u-u^^
9766:     ozyan ©<*ava-zayana-, fzan-\ MP }wzyyn;
10445:                                                                                (3)zyer Ozyyr-) =*JYyr-, zy'yr-
10453:     ozPar ? <DAv. uzban Parth. 'wzbry                                            ^'nzyynt-, 'nzyst-
10487:2316 'zyyr- ~» ^y'yr-                                                     469; STi 86.12; f. adj. >zprth, KG 554
10614:      0<?)make return                                            2376 *zyy my8 S                                      jJjl(,
11777:                                                                                                                 przyy
11833:       TSP 2.166, 400 n pl71; VJ 1131; Texts. p734                Prze (brzy, Przyy) =»Prz*k
11843:                                                             2828 przyy    M =» Przy
16783:                                                                       zyer   Ojyyr-) ©impf. jyYyr =^zy>yr-, zyyr-,
16889:          BSOAS 11,71                                             ziyer (zyyyr-) ©impf. =>JYyr-
19150:     mandzpart =>mnt}zprt, mndzprt                                     5408 mnzyynt- S
19151:     unclean, impure                                                        manzyent ? ©impf. =»}nzyynt-
19969:      (/<?)let go                                                mazen ©Av. *hama-zaena-; MP zen =*mzyyn
20032:     5695 mzyy    M => mzyx                                     >J>         encletic particIeG?/ indefinable meaning)
-----
      Gersh. apud. Sund. MSP b!68 p52
                                                                         pyaste (py*sty) ^py'stk, pysty(y)
8298 pyVkh S                                 J3jL ± lAZi^JS    \
                                                              JJJ
                                                                         adorned
     piyamak ? ©Yaghn. p/yon                                              BSTBL, Dhu. 36, 223, Dhy. 180, 363; Frag. Len.
     yesterday                                                              100c5
                                         o*.
     MDii 1.1,3 pill n pi 12, 113
                                                                    8310 py>sty -* py>stk
8299 py»t-      B                        jij'c^j       i            8311 py't- B,M,S                           o>S^y^\J
-----10610

       (s)zwast (zwst-) ©pt. st. ^zw'rt-                                                                            94
                                                                 2375 >zyt- S                                ' S^j,^/
       (to)return                                                     azit ? ©pt. st, >zytwd}r-\ perf. st. ^zyt-1
       KG pl8l.354                                                    (fo)take, (^)beat ?
 2360 'zw'yrt- B, S                                                   MDii pi 17.14; Gersh. Advice. 85; S W, C2 p74
                                                  oxkfj.
                                                                        n21
      (o)zwert ©<*uz-wartdya-         ^'zw^t, zw>yrt-
      0<?)make return                                            2376 *zyy my8 S                                      jJjl(,
      TSP 12.18; GMS 627                                              (a)ze-me9 ? ©Av. zv<? ^'pzymyS
                                                                      yesterday
 2361 »zwh    B =4 'nyw
                                                                      Anc. Lett. 2.16, >nyy myS\ Hen. Date. 604 n4;
 2362 'zwn    C                                    -^j^'v-              Benv. El Oss. 109
      az5n
       child, son
       STi 84.20; pi. -/, STi 7-2, 43.15; C2, 52R15t                                                        (j*)sSJ
         87R10; ob. pi. -tyf C2, 102V24; BSTii 878.10;
         Sund. AoFviii 1981, 191V4                               2377 (fR,fL)
                                                                      <D S ©Idg.
```


## [2026-09-05T20:57:34.649Z] TOOL CALL #41: Bash

```json
{
 "command": "sed -n '1,50p' tools/fetch_source.py",
 "description": "Inspect fetch_source.py"
}
```


### [2026-09-05T20:57:34.688Z] TOOL RESULT

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
    fetch_url = urllib.parse.urlunsplit((parts.scheme, parts.netloc.encode("idna").decode(),
                                         urllib.parse.quote(parts.path, safe="/%:@!$&'()*+,;="),
                                         urllib.parse.quote(parts.query, safe="=&%:/?+"), parts.fragment))
    os.makedirs(WEB, exist_ok=True)
    path = os.path.join(WEB, h + ".txt")
    if os.path.exists(path) and time.time() - os.path.getmtime(path) < 86400:
        print(path); return 0
    status, title, text = 0, "", ""
    try:
        req = urllib.request.Request(fetch_url, headers={"User-Agent": UA, "Accept-Language": "en"})
```


## [2026-09-05T20:57:36.146Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"دی\" MON_part1.txt | grep -n \"دیروز\\|روز گذشته\" | head -10; echo \"---BQT---\"; grep -n \"دی\" BQT_v2_pages.txt | grep \"دیروز\" | head -10",
 "description": "Grep Mo'in and Borhan for دی"
}
```


### [2026-09-05T20:57:36.220Z] TOOL RESULT

```
888:16799:آمس: 2۳5 [ع.] (ق.) دیروز. 
1686:30973:پرد: ۳:20 [پیشین» سابقی] (ق.) دیروز» 
1729:31605:سه روز پیش از دیروز. 
1731:31632:پیش از دیروز. 
3656:64577:دیگ: عآه (- دی] (ق.) دی» روز گذشته. 
---BQT---
21246:              ‫افغانی ع ‪ . 01501‬استی ‪( ۳0551‬عصر دیروز) “ بلوچی ‪« 1564‬اسشق ایضا» ‪.‬‬
21808:  ‫]‪id‬‏ ‪evécs‬‬      ‫ع‬         ‫‪ ,‬کردی‬       ‫‪kîd‬‏‬   ‫یهلوی‬   ‫( دیروز ‪۹5‬‬     ‫هندی ‏ باستان ‪séyh‬‏‬             ‫‪۱‬‬
21809:  ‫د(یروز عصر ) ‪ ۰‬استی ‪ 2002 , 8012 , 6022‬و ‪ ( 00012‬دیروز ) " بلوچی ‪۵2 , 612‬‬
```


## [2026-09-05T20:57:42.499Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '21795,21820p' BQT_v2_pages.txt; echo \"=== page tag ===\"; awk 'NR<=21810 && /\\[pdf page/ {p=$0} END{}' BQT_v2_pages.txt; grep -n \"\\[pdf page\" BQT_v2_pages.txt | awk -F: '$1<21810' | tail -2",
 "description": "Print Borhan footnote context and page"
}
```


### [2026-09-05T20:57:44.069Z] TOOL RESULT

```
‫وزن شرم کین » نام فرشته است ‪ -‬و مکی از‬                      ‫دیا وش س با نون بر وزن قبایوش »‬
‫نامهای‌الهی هم هت ‪ -‬ونام روز بیست وسیم(‪)۱‬‬
‫از دیماه مغان‬    ‫روز‬       ‫در ین‬   ‫‪۰‬‬   ‫باشد ازهر ماه شمسی‬    ‫خشکی ودربا دزدی وراهزنی میکردند ‪ ۰‬وبصنی‬
‫روز‬     ‫بتن‬
          ‫دكراس‬
              ‫جشن سازند و عید کنند و لي‬                         ‫کگوبند دام شخصی است که عذرا را بفروخت ‪.‬‬
‫دعا کردن بجهت دفم شر شیاطین واز حق تمالی‬                     ‫دیب = پکسراول بروزن‪ :‬سیب » بندری‬
                                       ‫فرزند درخواستن ‪.‬‬
                       ‫‪۱‬‬                    ‫‪۰‬‬                      ‫باشد ازبنادر هند ‪ -‬ودر ترکی‌بیخ وین ه‬
                                                                ‫چریز‬
‫دیباذر ‪ = ۲‬بفتح اول دوال قطه دار‬                                                                     ‫رگاونند ‪. ۴‬‬

                                                                          ‫(‪ )۱‬چك‪ :‬ببست وسوم ‪.‬‬
  ‫]‪id‬‏ ‪evécs‬‬      ‫ع‬         ‫‪ ,‬کردی‬       ‫‪kîd‬‏‬   ‫یهلوی‬   ‫( دیروز ‪۹5‬‬     ‫هندی ‏ باستان ‪séyh‬‏‬             ‫‪۱‬‬
  ‫د(یروز عصر ) ‪ ۰‬استی ‪ 2002 , 8012 , 6022‬و ‪ ( 00012‬دیروز ) " بلوچی ‪۵2 , 612‬‬
       ‫‪4:۲۰ ۶۸‬‬   ‫‪ .‬ورك‪ :‬دزی حاص‬             ‫‪۱۸۱‬‬    ‫(فر) «لك‪۲‬ص‬    ‫‪60062‬‬       ‫‪Ff‬‏ —‬              ‫‪.‬‬    ‫داسشق ‪۰۹۵۰‬‬
   ‫‪ - ۴‬سانسکریت ‪« 301۷‬فهرست ماللهند بیرونی ص ‪« :»۲4۳‬الدیبات » وحی‌الجزاثره‬
  ‫‪ - ۴‬درترکی ‪ :‬شایستگی‪ ,‬خوشبختی؛ ته " پ »ا پابه «جفتابی‬                               ‫م«اللهند ص ‪ ۰۸‬ی ‪٩‬‏ > ‪.‬‬
      ‫* ‪ -‬بهلوی ‪ « 081‬تاوادیا ‪ ۰ ۰۹۱‬از هندی باستان ‪802۷010 . 01 -‬‬                                          ‫‪.‬‬         ‫‪۳‬‬
   ‫‪ .‬رجه اشتقاق آن قطعی ليست‬                        ‫( زبانه کشیدن » پرتو افکندن » درخشیدن) ‪٠‬‏ ارمنی ع‬
   ‫د اسشق ‪۱٩٥۰‬‏ در فارسی = دبباه د‪۳‬یبه؛ و دیباچه و دیوان نیز ازهمین ریشه است معرب آن‬
  ‫‪ 06.‬است «اسفا ‪ ۲: ۱‬ص ‪ > ۵۷۱ ۰ ۱۷۱‬وآلرا از ربشة‬                            ‫‪06‬‬
                                                                             ‫‪.‬زو اول آن‬
                                                                                      ‫دیباح است ج‬
      ‫‪ ۷001۱ ,‬اکدی گرفته‌اند < فاب ‪۱‬ص ‪> ۲۱۱‬رك‪:‬‬                     ‫تالا سومری (لوحه ‪ .‬خط ) و ا‪00‬‬
                  ‫دستان» دییر ‪ * ۰۰ ۰‬از ‪ :‬دیباج ( معرب دبا = ديپاکه ) ی (سبت)‪.‬‬
=== page tag ===
```


## [2026-09-05T20:57:56.388Z] TOOL CALL #44: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0%C7%B5%CA%B0y%C3%A9s' \\\n 'https://en.wiktionary.org/wiki/%D8%AF%DB%8C' \\\n 'https://www.etymonline.com/word/yester-' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0eh%E2%82%81-' \\\n 'https://en.wiktionary.org/wiki/heres' ; do\n python3 tools/fetch_source.py \"$u\" --note 'page 181: roots Ghdies (yester) and Ghe 1 (to go); checking PIE reconstruction, Persian di, English yester/heir' ; done",
 "description": "Archive web sources"
}
```


### [2026-09-05T20:58:00.623Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/fc56187460042fea.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/828f0d6ec27b0a28.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ec39522c85b7c609.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a15eeb8595907f07.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9e2c24cf83667ad8.txt
```


## [2026-09-05T20:58:03.753Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in fc56187460042fea a15eeb8595907f07; do echo \"##### $f\"; head -c 300 $f.txt; echo; grep -n -i \"Iranian\\|Avestan\\|Persian\\|Descendants\\|Etymology\" $f.txt | head -30; done",
 "description": "Inspect fetched PIE pages"
}
```


### [2026-09-05T20:58:05.367Z] TOOL RESULT

```
##### fc56187460042fea
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0%C7%B5%CA%B0y%C3%A9s
FETCHED: 2026-09-05T20:57:58Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/dʰǵʰyés - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/dʰǵʰyés - Wiktionary, the free 
62: Etymology 
74: Descendants 
140: Etymology
143: Possibly from *dʰeǵʰ- ( “ day ” ) , whence perhaps Proto-Germanic *dagaz . [ 1 ] The suffix is uncertain but perhaps a form of (what would become) the comparative *-is- , as if literally “day-er”, effectively contrasting it with the current day. ( Can this ( + ) etymology be sourced ?) However, as de Vaan notes, it is unclear whether *-y- is originally part of the cluster, being found only in Indo-Iranian. [ 2 ] If not, it may be analogical in that branch, and the original *dʰǵʰés would simply be the genitive singular to a root noun *dʰéǵʰs .
145: Alternatively, some suggest that the cluster *dʰǵʰ- may have come from earlier *ǵʰd- (compare *dʰéǵʰōm for a theoretically similar case) such that the original PIE form might have contained *dey- ( “ day ” ) and the demonstrative pronoun stem *ǵʰe- (or even earlier *gʰe- ), thus *ǵʰe-dyés ( “ on that day ” , gen.sg. ) . In that case, it would be a fitting counterpart to pre-Indo-Iranian *h₁e-dyé(s) and *sm̥-dyés , whence Sanskrit अद्य ( adyá , “ today ” ) and सद्यः ( sadyáḥ , “ immediately ” , literally “ on the same day ” ) respectively. However, the existence and function of *ǵʰ- along with the phonetic development of the cluster remain unclear.
171: Proto-Celtic: *gdesi ( see there for further descendants )
176: Descendants
179: Proto-Albanian: *de ( see there for further descendants )
182: Ancient Greek: χθές ( khthés ) , ἐχθές ( ekhthés ) ( see there for further descendants )
184: Proto-Indo-Iranian: *ȷ́ʰyás ( see there for further descendants )
186: Proto-Germanic: *gēz ( see there for further descendants )
##### a15eeb8595907f07
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0eh%E2%82%81-
FETCHED: 2026-09-05T20:57:59Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/ǵʰeh₁- - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/ǵʰeh₁- - Wiktionary, the free dicti
62: Etymology 
140: Etymology
166: Proto-Indo-Iranian: *ȷ́ʰáȷ́ʰaHti 
170: Proto-Iranian: *jájaHti 
171: Avestan: 𐬰𐬀𐬰𐬁𐬌𐬙𐬌 ( zazā i ti ) 
174: Proto-Indo-Iranian: *Háȷ́ʰāHst 
180: Proto-Germanic: *gāną ( see there for further descendants )
183: Proto-Indo-Iranian: *ȷ́ʰHnás 
185: Sanskrit: हीन ( hīná ) ( see there for further descendants )
```


## [2026-09-05T20:58:09.182Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '135,200p' a15eeb8595907f07.txt; echo \"#### dhghyes descendants\"; sed -n '160,200p' fc56187460042fea.txt",
 "description": "Read PIE pages detail"
}
```


### [2026-09-05T20:58:09.235Z] TOOL RESULT

```
 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Etymology
 [ edit ] 

 Dunkel suggests this root came from an adverb *ǵʰoh₁ ( “ behind ” ) (whence Proto-Slavic *za ) as "to leave behind". [ 1 ] 

 Root
 [ edit ] 

 *ǵʰeh₁- [ 2 ] [ 3 ] [ 4 ] 

 to leave , abandon 

 Alternative reconstructions
 [ edit ] 

 *gʰeh₁- [ 5 ] ( for Germanic and Greek ) 

 Derived terms
 [ edit ] 

 Terms derived from the Proto-Indo-European root *ǵʰeh₁- (42 c, 0 e) 

 *ǵʰé-ǵʰeh₁-ti ( reduplicated present ) 
 Proto-Hellenic: 
 Ancient Greek: κιχάνω ( kikhánō ) 

 Proto-Indo-Iranian: *ȷ́ʰáȷ́ʰaHti 
 Proto-Indo-Aryan: *ȷ́áźʰaHti 
 Sanskrit: जहाति ( jáhāti ) 

 Proto-Iranian: *jájaHti 
 Avestan: 𐬰𐬀𐬰𐬁𐬌𐬙𐬌 ( zazā i ti ) 

 *ǵʰḗh₁-s-t ~ *ǵʰéh₁-s-n̥t ( s-aorist ) 
 Proto-Indo-Iranian: *Háȷ́ʰāHst 
 Proto-Indo-Aryan: *HáźʰāHst 
 Sanskrit: अहास् ( áhās ) ( later: अहासीत् ( áhāsīt ) ) 
 ⇒ Sanskrit: अहात् ( áhāt ) ( clarification of 3sg. ) 

 *ǵʰh₁-yé-ti ( ye-present ) 
 Proto-Germanic: *gāną ( see there for further descendants )

 *ǵʰh₁-nó-s 
 Proto-Indo-Iranian: *ȷ́ʰHnás 
 Proto-Indo-Aryan: *źʰHnás 
 Sanskrit: हीन ( hīná ) ( see there for further descendants )

 *ǵʰeh₁ro- 

 Unsorted formations 

 Albanian: ngah 

 Proto-Celtic: *gat- ( < *ǵʰh₁-t- ) 
 Proto-Brythonic: *gad- 
 Middle Cornish: gasa , gase 
 Cornish: gasa 

 Middle Welsh: gadu , gadael , gadel 
 Welsh: gadael 

#### dhghyes descendants

 *ǵʰdyés [ 2 ] 

 *ǵʰés [ 3 ] 

 Derived terms
 [ edit ] 

 *dʰǵʰyés-tero-s 

 *dʰǵʰyés-i ( innovative locative singular ) 
 Proto-Celtic: *gdesi ( see there for further descendants )

 Proto-Italic: *hezi [ 2 ] 
 Latin: here , herī̆ 

 Descendants
 [ edit ] 

 Proto-Albanian: *de ( see there for further descendants )

 Proto-Hellenic: *kʰtʰés 
 Ancient Greek: χθές ( khthés ) , ἐχθές ( ekhthés ) ( see there for further descendants )

 Proto-Indo-Iranian: *ȷ́ʰyás ( see there for further descendants )

 Proto-Germanic: *gēz ( see there for further descendants )

 References
 [ edit ] 

 ^ Beekes, Robert S. P. ( 2010 ), “ χθές ”, in Etymological Dictionary of Greek (Leiden Indo-European Etymological Dictionary Series; 10 ), with the assistance of Lucien van Beek, Leiden, Boston: Brill, →ISBN , page 1632 

 ↑ 2.0 2.1 2.2 De Vaan, Michiel ( 2008 ), “ heri ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN , page 283 : “ PIt. * χes-i . PIE *ǵʰ-di-es 'yesterday' ” 

 ↑ 3.0 3.1 Dunkel, George E. ( 2014 ), Lexikon der indogermanischen Partikeln und Pronominalstämme [ Lexicon of Indo-European Particles and Pronominal Stems ]‎ [1] (in German), volume 2: Lexikon, Heidelberg: Universitätsverlag Winter, →ISBN , pages 266-270 

 ^ Kloekhorst, Alwin ( 2014 ), “Proto-Indo-European “thorn”-clusters”, in Historische Sprachforschung / Historical Linguistics ‎ [2] , volume 127 , Vandenhoeck & Ruprecht, →JSTOR 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/dʰǵʰyés&oldid=92151279 "
```


## [2026-09-05T20:58:13.665Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i \"etymology\\|yesterday\\|Middle Persian\\|Old Persian\\|Avestan\" 828f0d6ec27b0a28.txt | head -40",
 "description": "Read Persian دی wiktionary"
}
```


### [2026-09-05T20:58:13.712Z] TOOL RESULT

```
70: Etymology 
87: Etymology 1 
96: Etymology 2 
111: Etymology 3 
223: Etymology
252: Etymology 1
255: From Middle Persian [Term?] ( /⁠dīk⁠/ ) , from Proto-Indo-Iranian *ȷ́ʰyás , from Proto-Indo-European *dʰǵʰyés .
279: Etymology 2
282: Middle Persian ddw’ ( Day , “ Creator ” ) .
353: Etymology 3
407: Persian terms inherited from Middle Persian 
408: Persian terms derived from Middle Persian 
436: Middle Persian term requests 
444: Persian entries with etymology texts
```


## [2026-09-05T20:58:17.706Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '248,282p' 828f0d6ec27b0a28.txt",
 "description": "Read دی etymology 1"
}
```


### [2026-09-05T20:58:17.749Z] TOOL RESULT

```
 Persian Wikipedia has an article on: دی 

 Wikipedia fa 

 Etymology 1
 [ edit ] 

 From Middle Persian [Term?] ( /⁠dīk⁠/ ) , from Proto-Indo-Iranian *ȷ́ʰyás , from Proto-Indo-European *dʰǵʰyés .

 Adverb
 [ edit ] 

 Dari

 دی 

 Iranian Persian

 Tajik

 ди 

 دی • ( di ) 

 ( archaic ) yester 

 Derived terms
 [ edit ] 

 دیـ ( “ yester- ” ) 

 Etymology 2
 [ edit ] 

 Middle Persian ddw’ ( Day , “ Creator ” ) .
```


## [2026-09-05T20:58:24.838Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"zazāiti\\|zaz\\b\\|\\*zaH\\|\\*jaH\" CHEUNG.txt | head -20; echo \"=== za entry ===\"; grep -n \"^\\*za\" CHEUNG.txt | head -30",
 "description": "Grep Cheung for za"
}
```


### [2026-09-05T20:58:24.916Z] TOOL RESULT

```
14210:*jaH ‘to demand, request’ 
29759:*zaH ‘to leave (behind)’ 
29765:auuazazat (Y 34.9), SUBJ. 2sg. ҮАУ. zazähi (V 5.15), 3р1. OAv. zazonti (Y 30.10), ОРТ. 3р1. ҮАУ. ба... 
29769:1984: 214 derived it from *zaH. A further emendation was made by De Vaan 2003: 213: “us.zizanonti 
29822:Bart. zoz-/zoXt, Orosh. zoz-/zoxt, Sariq. zoz-/zuxt, Yzgh. zaz-/zext ‘to take, obtain, 
30252:interpreted differently: for YAv. frazahit (Y 60.7) see *zaH, and OAv. zaxiia- (Y 
30302:*NWIR: Bal. zar ‘anger’ (but Bal. zar ‘lament’ < NP хаг, *zaHr) || (+ *а-) NP 
50301:zaz-/zext, 461 
55099:*zaH (s.v.) 
56301:*jaH, *jad 
57053:*(h)rah, *raic, *raz, *zaH 
57054:*raic, *xa(m)p/b, *zaH 
=== za entry ===
29732:*zag ? ‘to sound (utter, say, etc.) 
29756:*zail 461 
29759:*zaH ‘to leave (behind)’ 
29799:*zai! ‘to set in motion, impel’ 
29892:*zamb2 463 
29921:*zamb! ‘to open the mouth, yawn’ 
29952:*zamb? ‘to crush’ 
30019:*zanH! ‘to give birth; (pass.) to be born’ 
30026:*zanHl 465 
30113:*zanHË ‘to know’ 
30145:*zanH2 467 
30240:*zap/f ? ‘to become quiet, still’ 
30260:*zarH2 469 
30263:*zarH! ‘to hurt, wound, anger’ 
30316:*zarH? ‘to age, grow old’ 
30350:*zarHË ‘to bewail the deceased, 5: JS ex ull” 
30392:*zau 471 
30395:*zarš! ‘to be excited, delighted, rejoice’ 
30494:*zauH ‘to call’ 
30541:*zauš ‘to take pleasure, rejoice in’ 
55099:*zaH (s.v.) 
55130:*zarH^ 
55196:*zarH' (s.v.) 
55613:*zanH! (s.v.) 
55738:*zap/f 
56132:*zamH 
56179:*zamb? 
56303:*zaiH 
56478:*zai? 
56769:*zarH*
```


## [2026-09-05T20:58:25.647Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"heres\\|hērēs\\|hěrēs\" LAT.txt | head -10; echo \"--- LEW ---\"; grep -n \"heres\" LEW_1910.txt | head -10",
 "description": "Grep Latin dicts for heres"
}
```


### [2026-09-05T20:58:25.743Z] TOOL RESULT

```
4927:Mais Brdor a perdu le sens de "sAcheresse" qui est rAservA A BriditBs
5395:heres ex asse "h^ritier unique" (de la totalite) par opposition aux
11304:constitui: itaque heres cum constituit se heredem esse, dicitur cernere,
15790:heres meus damnas esto, legatum per damnationem, et la glose de Non.
26411:renoa de s^cheresse"); specialise dans le sens de "bonne renoaa£e,
27750:puis de genre coaaun k l' 4 poque imperiale, secundus, secunda heres:
27752:Malgr 4 Festus qui enseigne que heres apud antiquos pro domino
27766:(tardif); exheres "d£sh£rit 4 , d 4 possbdb" (Pl.), exheredo,-ds (class.,
27772:Terne de droit, ancien, usuel. Les langues romanes ont conserve heres ,
28468:herest "nolet", ombr. heri "uult", heriest "nolet", etc., avec participe
--- LEW ---
238:Futtr I 557, 558 Fuutret I 557, 867 Gaaviis I 577 yéhav I 586 Genetai I 591 haf<tar>, hafiest I 630 Hetrennis I 658 Hereklui I 640 Herentateis I 658 herest I 658 heriam I 643, 658 herviad I 243. 658 herrins I 243 hipid I 159, 630 hipust I 630 hurz, hurtum I 242 hurtin I 687 humuns I 654 huxn>truis, huntrus I 664 tak I 720 4dtk I 192, 386, 720 Jetis I 673 div I 395, 862 imaden I 685, 686, 687, 692 inim, nim, in. 1404 wk, toc I 720 wklet I 349, 716 tone I 720
```


## [2026-09-05T20:58:29.188Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '29759,29800p' CHEUNG.txt",
 "description": "Print Cheung zaH entry"
}
```


### [2026-09-05T20:58:29.231Z] TOOL RESULT

```
*zaH ‘to leave (behind)’ 

*AVESTAN: YAv. za- (za-) ‘to leave (behind)’ || (+ *aua-) ‘to leave behind, abandon’ 
|| (+ *fra-) ‘to abandon’ = Liste: 68 

Pres. athem. red.: IND. Isg. YAv. zazami (V 5.17), 3sg. YAv. zazaiti (Yt 5.130), INJ. 3pl. OAv. 
auuazazat (Y 34.9), SUBJ. 2sg. ҮАУ. zazähi (V 5.15), 3р1. OAv. zazonti (Y 30.10), ОРТ. 3р1. ҮАУ. ба... 
"zaziian (V 8.37 f.); Aor. {1} athem.: OPT. 1р1. OAv. zaéma (Y 41.4); Aor. {2} s-: OPT. 35р. YAv. 
frazahit (Y 60.7); Partic.: perf. YAv. zazus- (Yt 13.18, P 26). 9 YAv. us.zizenti (V 3.5) was corrected to 
*us.zazonti by Bartholomae, AIW: 1658 and interpreted as 3р1. SUBJ. ‘they breed’ (*zanH!), but Kellens 
1984: 214 derived it from *zaH. A further emendation was made by De Vaan 2003: 213: “us.zizanonti 
3pl. IND. (*zanH’). 

*PARTHIAN: (+ *ш-) wzyh- ‘to depart, abandon’ = Ghilain: 89 | DMMPP: 362b 
Pres.: wzyh[; Partic.: perf. pass. wz’d, wyz'd 

*KHOTANESE: (+ *аџа-) OKh. vas- ‘to shun, avoid’ = SGS: 120 

*SOGDIAN: (+ *aua- or *ш-) CSogd. pys-wz’y ‘heirloom’ 

*CHORESMIAN: (+ *aua-) (?) wzy- ‘to leave behind, remain’ > Samadi: 229 f. 

*NEIR: (+ *aua-) Yi. wuza- ‘to be tired’, M. uzay-/uzayi- ‘to be left behind’ || (+ *ui-) 
Oss. I. zajyn/zad, D. izajun/izad ‘to remain’ 

*MISC: (+ *aua- or *ui-) Orm. ozuk ‘left, remaining’, Par. üzeh-/uzä ‘to remain, be 
left behind’ 

*SANSKRIT: hà ‘to leave (behind), abandon’ (RV+) = EWAia П: 813 

© This root has a good IE etymology. 

«PIE *g'eH,- ‘to leave (behind) > LIV: 173 | Pok.: 418 f. 

*IE COGNATES: ? Gr. vim ‘I overtake, reach, arrive, meet’ (kim, Kıynlevog), 
Gr. xñpoç ‘empty, bereft’, Lat. heres ‘heritage’ 

*REFERENCES: JIFL I: 238a f., 388b; IIFL II: 264b; DKS: 379a; Abaev, Slovar’ IV: 285; Werba 1997: 331 


*zai! ‘to set in motion, impel’ 
*AVESTAN: zaii- ‘to set in motion’ || (+ *fra-) ‘to permeate, penetrate’ || (+ *ui-) ‘to
```


## [2026-09-05T20:58:29.579Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '27745,27790p' LAT.txt",
 "description": "Print Ernout-Meillet heres"
}
```


### [2026-09-05T20:58:29.624Z] TOOL RESULT

```
d'un vocatif d'un theae en o-, Herclo-, n'est pas suffisaaaent ap-
puy^e par le vestinien Eerclo, CIL I a 3 S> 4 *
h 5 r 5 s, - 5 dls (acc. Aerem dans Naevius cite par Non.86,33; cf. Aeben;
la forae se retrouve en roaan, et fr . hoir repose sur Aerea) d'abord
seuleaent aasculin (1'enfant male seul pouvant h^riter A 1'origine),
puis de genre coaaun k l' 4 poque imperiale, secundus, secunda heres:
heritier lbgal.
Malgr 4 Festus qui enseigne que heres apud antiquos pro domino
ponebatur , P.F.88,38, le sens anci en du aot est bien "heritier":
c’est par plaisanterie que Plaute 1'eaploie pour "propri^taire",
Men.477 et 493. De a£me, c’est par extension de sens que hSrSdium
a signifi^ "petit doaaine rural": c'est d'abord la part minima ina-
li^nable qui doit revenir k l'h 4 ritier, cf. Varr., R.R. 1,10,3, bina
iugera quod a Romulo primum diuisa dicebantur uiritim, quae heredem
sequerentur, heredium appellarunt', de la le sens de praedium paruultm
que lui donne P.F.89,1, cf.Plin.10,50, in III Tabulis legum nostrarum
nusquam nominatur uilla, semper in significatione ea hortus, in horti
uero heredium.
Autres derives et conposes: hereditas: h^ritage (sens abstrait
et concret); hergditarius: h 4 r 4 ditaire; hSrediolum: petit h^ritage
(Colun.); hgrgdipeta (Petron.)j cohSrSs,-edis (Cic.), cohereditds
(tardif); exheres "d£sh£rit 4 , d 4 possbdb" (Pl.), exheredo,-ds (class.,
derives d'epoque iapbriale), exheredito (Rhet.Her.?); pro-, sub-hgres,
termes de droit, rares et tardifs.
II n'y a pas de verbe "hbriter" en latin classique; heredito,-ds
n'apparait que dans la 1 . de 1 'Rglise (hgredifico dans Ir£n 4 e); et
pour "dish 4 riter" Plaute dit exheredem facere) aais Ciceron a exheredo.
Terne de droit, ancien, usuel. Les langues romanes ont conserve heres ,
M.L.4115, hereditare 4113, hereditarius 4114 ; exheredare , 30130.
Le britt. aer, her est un mot savant.
Rtant donne que 1'irlandais a orbe et le gotique arbi "h^ritage"
en face de lat. orbus, il est naturel de rapprocher lat.AerSs de gr.
XHpOC "d 4 pouill 4 "; plus precis^aent, on a meae rapproch^ gr. x>lph>OTr|£
"collatdral qui h 4 rite k defaut d'un proche parent". Les hypotheses
qui ont ete propos£es sur la foraation de hgres et de sont
incertaines.
heri (t dans T 4 r., Sun.169, Aeri sinos uiginti pro ambobus dedi
( sen. iaab, ). L'i final, an ci en aais secondaire ( cf. plus bas), s'est
abreg^ par 1'effet de la loi des mots iaabiques; heri a abouti pho-
n^tiquenent k here, cf. Quint.1,4,7; 1,7,33, P.F.88,33) adv.: hier.
- Ancien, usuel. Panroaaa, M.L.41150. *- 531 - hetta
Derivds: hesternus, forni comae aeternus, sempiternus, et hodiernus,
nocturnus, diurnus, et, tardif, modernus.
L'indo-europeen qui n'a pas d'adverbe coamun pour "demain" (v.
cr 3 s), en avait un pour "hier". L'initiale comporte dea alternancea
de fonte du groupe initial: gr.yJdeC, eyQez, iri. in-dhi, gall.doe, des
```


## [2026-09-05T20:58:53.409Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== SKT yester ==\"; grep -n \"^Yester\\|Yester-\\|yester\" SKT.txt | head -5; echo \"== SKT heir ==\"; grep -n \"^Heir\\|Heir,\" SKT.txt | head -5; echo \"== SKT go ==\"; grep -n \"^Go, to move\\|^Go,\" SKT.txt | head -5",
 "description": "Grep Skeat"
}
```


### [2026-09-05T20:58:53.485Z] TOOL RESULT

```
== SKT yester ==
21785:vt,   adj  ,   belonging   to   yesterday;   where
21788:W».  Ski.  Acar,  yesterday.     The  iuRiK  -ftfr
== SKT heir ==
== SKT go ==
```


## [2026-09-05T20:58:54.932Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== NYB ==\"; grep -n \"\\bdyk\\b\\|dīk\\|d'ik\" NYB_vol2_glossary.txt | head -10; echo \"== KNT diy ==\"; grep -n \"diya\\|diyaka\" KNT.txt | head -10",
 "description": "Grep Nyberg and Kent"
}
```


### [2026-09-05T20:58:55.006Z] TOOL RESULT

```
== NYB ==
1252:dek [dyk] pot, vessel 423. — NP deg.
2029:Hróm [hlwm] Rome, in the Phl literature designating the Byzantine empire: 17*. 1090, — Cf Schaeder, IB II, 24 sqq. hrömäyik [hiwm’yk, hlwm'dyk] Romaic, Byzantine 1?. 1075-12. 1145; pl. cas. obl.
2625:muzrayik [mwel’dyk] Egyptian, of Alex- ander the Great 1075-12, - OP mudräya-, SW form presupposing a NW form muz-.
== KNT diy ==
419:ХРе ASayarsa : xsdyadiya : vazraka :
556:arlavd, ArtaxSaga, Artavardiya, by the Elamite
563:! Greek єр is not conclusive evidence for 7, despite xépoa = karía- and Zytphs = Bardiya, both with у ($80); ef. "Гутафёриує = Vitdafarnd, with -ar-, and 'Apseáum = Aršāma and 'Apratiptys = ArtaxSacd, both with r by the Elam. testimony, despite Gr. ар-. Several Greek transliterations of place-names have ap for Persian ar: Tapa = Paréava, Xayapría = Asagaria, etc.
573:Bardiya = Brd-, Elam. bir-ti-ga.
584:By the Elam. writings: Атта (or Araza), Arbairé-, Armina, Asagaria, Paréava, Fravartis (also РЫ. fravartikdn), Margu&, Marduniya, -vard- in Ar- tavardiya, Vidafarna (also Av. хатто), Vidarna, Sparda, haumavargd: many of these confirmed also by Greek forms, ete.
666:Two compound words are sometimes cut by the divider; these are Ariya : cd and Ariyacica, paruo : zanànüm and paruzandndm paruzendnam. There is also variation between the phrasal ad- verb paradraya and the prepositional phrase para : draya. But in Fragment Theta of DSf, the. . .]?- -k-[.. supposed to belong to dérantyakara 49 should be read ...h/--5-|... as part of avaiy : Spardiya 51-2.
806:yadiyarsa.
1039:bond, from pIE bh-.. pIE *bhergh- ‘be high’, in Bardiya-, barSan-,
1056:OP maub-, Adiyabausna-, gaibà-, frabara-, mitah-,
1091:Av. dtar- d6r- ‘fire’, seen in the OP month-name Aciyddiya- and probably in the personal name Аспа (despite the fact that Аста was an Elamite).
```


## [2026-09-05T20:59:04.765Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '21780,21795p' SKT.txt; echo \"== heir ==\"; grep -n -i \"^heir\\|Heir\\.\" SKT.txt | head -5; echo \"== go ==\"; grep -n -i \"^Go\\b\" SKT.txt | head -5",
 "description": "Skeat yester + heir + go"
}
```


### [2026-09-05T20:59:04.857Z] TOOL RESULT

```
Testerday.    (E.)       M.  E.    yiiterdai\
orn  A.  S.  ^eosfra,  giatra,  gystra  ^yesicr-).
id    iA^.  a  d»y.+Du.  ^Jteren,  dag  van
Mttr^  G.  fisfcrn.  Goth,  gt'sfrtn/ngir.      p.
tjfrr-  answers  lo  I-al.  Acsfer    in  Aes  ter^
vt,   adj  ,   belonging   to   yesterday;   where
%in  the  syllabltf  hes-  is  cognate  with  IceL
T,  Don.  gaar,  Swcd.  ^r,  LaL  ker-i,  Gk,
W».  Ski.  Acar,  yesterday.     The  iuRiK  -ftfr
I  uvcAsiain-fer  ier,rx-fer-ifir, &c.
If  wjfcr-  answcre  to  an  Ar)-an  type
Lr.i  1  .V  '  iKA,  of  which  the  prob,  sense
ra»  '  the  morning  beyood  ;'  where  GHVAS
uniiAcs  *  morning.'
Y»t.  (E.)  M.  E,  jrA  yif.  A.  S  ^V. ft,  jrttf,  moreover.  4*  O-  Fries,  if/a.  ita, 1  tl-  G.  WMO.  ieu,  yet;  cf.  G.  Jetzt, low.  B.  The  M.  II.  t-i.  ie-iuo  is  com- Qandeu  of  f>-»  and  »«i>  =  A.  S.  t6,  too; icuce  A.  S  f^et  is  pro!),  short  for  ^e  hi. i&   'and  aho/  moreover;  aee  Yea  and
T«w.  a  tree.  (K.)  M.  E  rtr.  A.  S.  /». fDu.  »>y;  Iccl.  yr,  G.  r///.  O.  il.  G.  iica, lew.  Perhaps  of  Celtic  mtein ;  we  also ivi  Iriih  iubhar,  Gael,  iuohar,  iu^har. W.  jrttf,  jrxffft,  Com  Mivin,  Bret.  I'vm,  a frw.  ^  Alw  allied  to  ipy. Y«x.  to  hiccough.  (K.)  M.  E.  yexem, mkm.  A.  S.giscian.  to  sob,  sigh.  Prob. dlicd  to  L  htjcert,  to  yawn,  Aidrr,  to piwn;  see  YftWTi.  (V"GHL) YiOli  tE.)  M.  E^/./w.7//dSr«,  pt.  t w/^,  pp.  yo/iien,  to  pny ;  hence,  lo  yield in  \  S.  gifi'tian,  giidan^  pL  t.  gcaid, to  pay.  give  up.  +  Du.  geidtn, i  J,  Don.  gieUe,  to  poy;  Swed.
== heir ==
8538:*L.   kmdifan,  to  mheriL  —  L,  ktrtJit erode  form  of  htrts^  an  heir. horita^.    (F.  -  L.)     O.  F.  htritagt.
8620:HeriUee :  see  Heir.
19158:Tanist,  a  presumptive  heir  to  a  , (Irish.)    Irish  fanaiste.  nppxrent  heir.—  I tauiiiie,  accond  in  rank  (Rh^'s).
== go ==
```


## [2026-09-05T20:59:07.583Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== WLD ghdies ==\"; grep -n \"ghdies\\|ĝhđies\\|g'hdies\\|hyás.*gestern\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10; echo \"== WLD ghe- ==\"; grep -n \"ĝhē-, ĝhēi-\\|ghe-, ghei-\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10",
 "description": "Grep Walde-Pokorny"
}
```


### [2026-09-05T20:59:07.655Z] TOOL RESULT

```
== WLD ghdies ==
== WLD ghe- ==
```


## [2026-09-05T20:59:16.914Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"\\[pdf page\" incoming/WLD/WLD_Bd1_pages.txt | head -3; echo \"...\"; grep -n \"hyás\\|hyas .gestern\\|gestern\" incoming/WLD/WLD_Bd1_pages.txt | head -20",
 "description": "Grep WLD Bd1 pages for gestern"
}
```


### [2026-09-05T20:59:16.977Z] TOOL RESULT

```
...
9045: „gestern‘    i fjord
29617:veecr ds., wozu Adv. aksl. fb'era ..gestern" (nach Yasmer IF. 42, 179ff., ein
62934:gh[dijes oder ghjes ,.gestern .
62938:   Ai. liyas ,,gestern“, hyastana „gestrig“,                                   np. di, dig          .   din       gr. /deg,     eydeg
62943:1919, 122),                y&ernvog         „gestrig“;       alb.       dje   „gestern“, djcdine                   ds.,   djetiems,
62944:djeitn „gestrig“, paradje „vorgestern“ (G. Meyer        BB. 8, 187, Alb. Wb. 69).
62945:   Lat. h.eri, here,, gestern“, hesternus „ gestrig"; air .indite, cymr .doe, acorn.
62946:dry.     ncorn. de,                  mbret. deck, nbret. deac'h „gestern“                               (vgl. Meillet Msl. 11,
62950:neysor nbret. neiscr „gestern Abend ( <C*noktigestro Fick II 4 195).
62957:(einmal             belegt,           sonst)    giestrandeeg ,            giestranniht,             gyrstancefen          „gestern
62959:,.gestern“,bgestre „vorgestern“, gesterig „gestrig'‘; ablautend in aisl. 7 (jeer
62961:gjaar und jjeer. schw. i gar, dan. igaar „gestern", yacirsdagen „das Gestern".
```


## [2026-09-05T20:59:20.243Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '62930,62975p' incoming/WLD/WLD_Bd1_pages.txt; echo \"=== page tag ===\"; awk 'NR<=62935' incoming/WLD/WLD_Bd1_pages.txt | grep -n \"\\[pdf page\" | tail -2",
 "description": "Print WLD ghdies"
}
```


### [2026-09-05T20:59:22.339Z] TOOL RESULT

```
giesen „Cyprinus   cephalus" und a. schwed. fiska-giustn „ein Raubvogel,
                                 4
Falco haliaetus ', worin ein *gjuse ,,Fischer“ stecke.
                                                       <-
gh[dijes oder ghjes ,.gestern .
   Zum Anlaut vgl. Wackernagel Ai. Gr. I 240 mit der alteren Lit., Meillet
Msl. 9, 373 A.                  1,    11, 317, Schrijnen KZ. 44, 20, Brugmann Grdr. I 2 794,
Brugmann-Thumb                         Gr. Gr. 151 f., Ber. d. sachs. Ges. d. Wiss. 1917,6 u. 1.                                 A
   Ai. liyas ,,gestern“, hyastana „gestrig“,                                   np. di, dig          .   din       gr. /deg,     eydeg
(nach          fy.sivog G. Meyer Gr. Gr. 3 166, anders Brugmann Grdr. I 2
                            :   y.sivog
b25, Ber. d. sachs. Ges. 1917, 3', yjh£6g, adv. ydi^u (analogisch nach txqcoi’Qal
Brugmann a. zul. a. 0. 3ff. mit Lit.; zustimmend Hermann Berl. phil. Wschr.
1919, 122),                y&ernvog         „gestrig“;       alb.       dje   „gestern“, djcdine                   ds.,   djetiems,
djeitn „gestrig“, paradje „vorgestern“ (G. Meyer        BB. 8, 187, Alb. Wb. 69).
   Lat. h.eri, here,, gestern“, hesternus „ gestrig"; air .indite, cymr .doe, acorn.
dry.     ncorn. de,                  mbret. deck, nbret. deac'h „gestern“                               (vgl. Meillet Msl. 11,
317, Pedersen KGr. I 67, 89), cymr. neithiwyr corn, neihur, nchur mbret.          ,                                       ,


neysor nbret. neiscr „gestern Abend ( <C*noktigestro Fick II 4 195).
           ,
                                                                    '



   Got. gistradngis „avgiov“                           (zur Bed.         s.   Brugmann aaO. 15),                     ags. gkstron
(einmal             belegt,           sonst)    giestrandeeg ,            giestranniht,             gyrstancefen          „gestern
(tags,         nacht,           abend)",       gystrrnlic „gestrig“,             ahd.           gestre ,    gesteron,         gesteren
,.gestern“,bgestre „vorgestern“, gesterig „gestrig'‘; ablautend in aisl. 7 (jeer
(<%er-). / giar (s. Koreen aisl. Gr. 4 § 72, 263a 1), aschw. i gar, norw. dial.
gjaar und jjeer. schw. i gar, dan. igaar „gestern", yacirsdagen „das Gestern".
   Curtius 201, Yanirek 98, Fick I 4 55, 220, 437. Ill 4 133, Falk-Torp 392,
Brugmann Ber. d. slicks. Ges. d. Wiss. 1917, H. 1.
  Die weitere Ankniipfung an die Pronominalstamme gho-, ghi- „dieser“
(Brugmann Demonstrativpronomina 72) iiberzeugt nicht.
                                           gSa       guei-                                          665

g“a-     ,
             gehen,   kommen“ s. u. g^em-.

g!!liai-, g!hai-d- „hell, leuchtend" (eig. g"hsi- :g!thi-; die langdiphthongische
      Hochstufe ist nicht belegt).
   Gr. (patdgog „klar, hellglanzend, leuchtend heiter, vergnfigt" (= lit. giedras),
                                                          ;

=== page tag ===
```


## [2026-09-05T20:59:42.166Z] TOOL CALL #59: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/%C8%B7%CA%B0y%C3%A1s' \\\n 'https://www.etymonline.com/word/heir' \\\n 'https://www.etymonline.com/word/go' ; do python3 tools/fetch_source.py \"$u\" --note 'page 181: Ghdies/Ghe 1 verification'; done",
 "description": "Fetch PII and etymonline pages"
}
```


### [2026-09-05T20:59:45.526Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/e5c01c7aed833904.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ff5dfd0afcdc6a63.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3cca67aa58fd7cc6.txt
```


## [2026-09-05T20:59:48.894Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"#### PII\"; sed -n '130,200p' e5c01c7aed833904.txt; echo \"#### heir\"; grep -n -i \"heres\\|Proto-Indo-European\\|orphan\\|bereft\" ff5dfd0afcdc6a63.txt | head -10",
 "description": "Read PII and etymonline heir"
}
```


### [2026-09-05T20:59:48.967Z] TOOL RESULT

```
#### PII
#### heir
25: "one who inherits, or has right of inheritance in, the property of another," c. 1300, from Anglo-French heir , Old French oir "heir, successor; heritage, inheritance," from Latin heredem (nominative heres ) "heir, heiress" (see heredity ). Heir apparent (late 14c.) has the French order of noun-adjective, though it was not originally so written in English. It is the heir of one still alive whose right is clear. After death the heir apparent becomes the heir-at-law . Related: Heir-apparency .
32: 1530s, "inheritance, succession," from French hérédité , from Old French eredite "inheritance, legacy" (12c.), from Latin hereditatem (nominative hereditas ) "heirship, inheritance, an inheritance, condition of being an heir," from heres (genitive heredis ) "heir, heiress" (from PIE root *ghe- "to be empty, left behind," source also of Greek khēra "widow"). Legal sense of "inheritable quality or character" first recorded 1784; the modern biological sense "transmission of qualities from parents to offspring" seems to be found first in 1863, introduced by Herbert Spencer.
53: c. 1300, "to make (someone) an heir" (a sense now obsolete), from Old French enheriter "make heir, attribute the right of...inheretance to, appoint as heir," from Late Latin inhereditare "to appoint as heir," from in- "in" (from PIE root *en "in...") + Latin hereditare "to inherit," from heres (genitive heredis) "heir" (see heredity)....
71: orphan 
73: harb- "change allegiance," Latin orbus "bereft," Sanskrit arbhah "weak, child," Armenian orb "orphan," Old Irish orbe "heir...," Old Church Slavonic rabu "slave," rabota "servitude" (see robot), Gothic arbja, German erbe, Old English ierfa "heir,"...
```


## [2026-09-05T20:59:52.695Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && wc -l e5c01c7aed833904.txt && sed -n '1,10p;55,120p' e5c01c7aed833904.txt",
 "description": "Check PII page content"
}
```


### [2026-09-05T20:59:52.745Z] TOOL RESULT

```
5 e5c01c7aed833904.txt
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/%C8%B7%CA%B0y%C3%A1s
FETCHED: 2026-09-05T20:59:44Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-09-05T21:00:06.418Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== SYN yesterday ==\"; grep -n -i \"yesterday\" SYN.txt | head -5; echo \"== SYN go ==\"; grep -n \"14\\.11 GO\\|GO$\" SYN.txt | head -5; echo \"== IEC ghe ==\"; grep -n \"ghē-\\|ghe- 'go'\\|ghēros\\|ghēro-\" IEC.txt | head -10",
 "description": "Grep Buck and Mann"
}
```


### [2026-09-05T21:00:08.150Z] TOOL RESULT

```
== SYN yesterday ==
24315:TopayYy TomMoRROW YESTERDAY Hour
25463:prep. in modern Scand. due to 7 dag ‘to- day’, 7 g@r ‘yesterday’?), OE t6 morgen (also on morgen), ME to morwen, to morwe, NE tomorrow, OHG in morgan, phrases with prepositions ‘to, in, on’ and ‘morning’, beside adv. dat. in OHG mor- gane, MHG morgen(e), NHG, Du. mor- gen. Weigand-H. 2.219. Franck-v. W. 422f. NED s.v. tomorrow.
25464:Goth. gistradagis (adv. gen.) : OE geostra-deg, etc. ‘yesterday’ (14.49), renders atpuv Mt. 6.30, with puzzling shift of meaning if not merely a blunder in translating. Cf. Brugmann, op. cit. p. 15.
25472:14.49 YESTERDAY
25473:Grk. —_xés, Ex0és Goth. . Lith. vakar NG xrés, éxrés, Wes ON i g@r Lett. vakar Lat. —heri Dan. 7 gaar ChSl.  v%%era It. teri Sw. t gdr SCr.  juéer Fr. hier Or geostran dag Boh.  véera Sp. ayer ME __yister(n)day Pol. wezoraj Rum. tert NE yesterday Russ. véera Ir. indhé Du. gisteren Skt. hyas Nir. indé, iné OHG - gesteron Av. te W. doe MHG gester(n)
== SYN go ==
== IEC ghe ==
```


## [2026-09-05T21:00:08.765Z] TOOL CALL #63: Bash

```json
{
 "command": "pdftoppm -f 181 -l 181 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg181 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 181"
}
```


### [2026-09-05T21:00:11.160Z] TOOL RESULT

```
total 23596
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 17:00 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb   74140 Sep  5 16:56 build160.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53286 Sep  5 16:55 build161.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67253 Sep  5 16:56 build162.py
-rw-rw-r-- 1 sfmqrb sfmqrb   45662 Sep  5 16:49 build164.py
-rw-rw-r-- 1 sfmqrb sfmqrb   82221 Sep  5 16:56 build168.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53542 Sep  5 16:57 build169.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb   61790 Sep  5 16:57 mk167.py
-rw-rw-r-- 1 sfmqrb sfmqrb   30384 Sep  5 16:51 mk170.py
-rw-rw-r-- 1 sfmqrb sfmqrb    4344 Sep  5 16:49 n12b.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3969 Sep  5 16:49 n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2692 Sep  5 16:49 n16.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11831 Sep  5 16:32 node4.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7427 Sep  5 16:32 node7.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:13 oldpers_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    6054 Sep  5 16:36 p152_e0left.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2672 Sep  5 16:36 p152_node2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   35268 Sep  5 16:59 p162a.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14337 Sep  5 16:59 p162b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76438 Sep  5 16:59 p162.png
-rw-rw-r-- 1 sfmqrb sfmqrb   41788 Sep  5 16:53 p173_ital.png
-rw-rw-r-- 1 sfmqrb sfmqrb   32898 Sep  5 16:53 p173_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb  671488 Sep  5 16:52 p600_350.png
-rw-rw-r-- 1 sfmqrb sfmqrb  139701 Sep  5 16:52 p600_foot2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  183909 Sep  5 16:52 p600_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1717 Sep  5 16:52 p600_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5162 Sep  5 16:52 p600_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1189 Sep  5 16:57 p600_top.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb   73400 Sep  5 16:56 pg172.png
-rw-rw-r-- 1 sfmqrb sfmqrb   52970 Sep  5 16:53 pg173.png
-rw-rw-r-- 1 sfmqrb sfmqrb   54907 Sep  5 16:54 pg175.png
-rw-rw-r-- 1 sfmqrb sfmqrb   57139 Sep  5 16:54 pg179.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81598 Sep  5 16:58 pg180.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56794 Sep  5 17:00 pg181.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77310 Sep  5 16:58 pg184.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44812 Sep  5 16:34 pg532.png
-rw-rw-r-- 1 sfmqrb sfmqrb  153161 Sep  5 16:34 pg532_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep  5 16:14 prt.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  333088 Sep  5 16:16 sod135_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1817364 Sep  5 16:16 sod135.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  101641 Sep  5 16:15 sod136_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1892712 Sep  5 16:15 sod136.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  561602 Sep  5 16:57 t598.png
-rw-rw-r-- 1 sfmqrb sfmqrb  632359 Sep  5 16:57 t599.png
-rw-rw-r-- 1 sfmqrb sfmqrb  671488 Sep  5 16:57 t600.png
-rw-rw-r-- 1 sfmqrb sfmqrb  545905 Sep  5 16:57 t601.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top598.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top599.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top601.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24918 Sep  5 16:58 tops2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4812 Sep  5 16:57 tops.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56398 Sep  5 16:26 write144.py
```


## [2026-09-05T21:00:16.064Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '25472,25492p' SYN.txt",
 "description": "Print Buck 14.49"
}
```


### [2026-09-05T21:00:16.109Z] TOOL RESULT

```
14.49 YESTERDAY
Grk. —_xés, Ex0és Goth. . Lith. vakar NG xrés, éxrés, Wes ON i g@r Lett. vakar Lat. —heri Dan. 7 gaar ChSl.  v%%era It. teri Sw. t gdr SCr.  juéer Fr. hier Or geostran dag Boh.  véera Sp. ayer ME __yister(n)day Pol. wezoraj Rum. tert NE yesterday Russ. véera Ir. indhé Du. gisteren Skt. hyas Nir. indé, iné OHG - gesteron Av. te W. doe MHG gester(n)
Br. dec’h NHG gestern
Most of the words for ‘yesterday’ be- long to an inherited group, pointing clearly to an IE adv. of this meaning. The others (the Balto-Slavic, and pop. NG) meant orig. ‘in the evening’ or ‘ate’, whence ‘in the past evening’, and with extension to the entire day ‘yester- day’. Cf. the parallel but forward shift in the history of words for ‘tomorrow’ (14.48).
1. IE *hes, etc. (variant init. com- binations). Walde-P. 1.664. Ernout- M. 449. Walde-H. 1.642f. Falk-Torp 292.
Grk. x6és, and éxéés, adj. xOtés, xGeowds; Lat. herz, later hert (> Ro- mance words), adj. hesternus; Ir. in- dhe, NIr. indé, ine, W. doe, Br. dec’h (cf. Pedersen 1.67, 89, 2.25); (Goth. gistra- dagis, 11.48), OE giestron, usually geo- stran, giostran deg (with geostra adj.), ME yister(n)day, NE yesterday, OHG
gesteron, gesteren, gestre, MHG gester(n), NHG gestern, Du. gisteren; without deriv. suffix and in ablaut ON 7 g@r, 7 gjar, Dan. % gaar, Sw. i gar; Skt. hyas and adj. hyastana-, NPers. di, dig, dine; Alb. dje. On the supposed meaning ‘tomorrow’ of ON 7 g@r, and ‘day after tomorrow’ of OHG é-gestern, é-gestra, often quoted in connection with Goth. gistra-dagis, cf. Brugmann, op. cit. pp. 11 ff.
2. NG pop. yés (not fr. x6és, but) fr. 6yé ‘late’ (14.17), first specialized to ‘late yesterday, yesterday evening’ (as still in some dial.), then extended to ‘yesterday’. Hatzidakis, Mec. 1.122.
3. Lith., Lett. vakar (orig. loc. sg.), Ch8SI. viéera, viiéera, SCr. jucer, etc., gen- eral Slavic (prob. old instr. sg.) fr. the Balto-Slavie word for ‘evening’ (14.46). Walde-P. 1.311. Vasmer, IF 42.179 ff. Miihl.-Endz. 4.446.
14.51 HOUR Grk apa Goth. hweila Lith. valanda (adyna) NG pa ON #0, stund Lett. stunda Lat. hora Dan. time ChSI. godina (éasit) It. ora Sw. — timme SCr. sat, ura Er. heure OE lid Boh.  hodina Sp. hora ME (h)oure, tide Pol. — godzina Rum. ceas NE hour Russ. as Ir or, war Du uur Nir. uair OHG zit W. awr MHG zit, ar(e) Br. eur NHG | stunde
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
a eek EO ee ee Sc a
aon ee ee
1 ST aN ens
1 porrowed the division of ghe Gree hours from the Babylonians the day Hy 109). However, the hour of cf. e roniats was actually a double the Ba y the entire day, whereas the hours ee ded only the period of light Greeks night) into twelve parts. This (da i adopted likewise by the Ro- system Much later the night was divided ail fashion. Consequently, the ariod of time covered by an hour was yariable according to the length of the day, depending upon the seasons. This state of affairs lasted well up into the Middle Ages. Cf. Schrader, Reallex. sy, stunde; Kubitschek, Grd. d. antik. Jeitrechnung 178.
The ‘hour’ was designated by words yhich were originally, and often con- tinued to be, used as more general terms for ‘time’ or for various periods of time. But Grk. dpa, through Lat. hora, in its specialized sense, eventually spread We ae ane either as ‘hour’ or as ‘cloc 58).
1, Grk. dpa, ‘period of time, season’, ete. (14.11), specialized to ‘hour’. Hence lat, hora, whence It. ora, Sp. hora, (Rum. oara only dial. ‘hour’, or pl. ort in phrases for ‘what time’ or ‘so many a Fr. heure, OF r. (h)ure, (h)ore > i Og (h)oure, NE hour; also Ir. 6r,
Nir. uair, W. awr, Br. eur, Du. uur, i oe tre > MHG ar(e), NHG
- REW 4176, Loth, Mots lat. 135.
2 Rum. ceas vi v " fr. iS) basi, bel j r. Slavic, cf. Chsl.
3, : (4 aaa hweila ‘period of time’ oN me most commonly ‘hour’. i, onere OF fad, ME tide, OG, MHG a words for ‘time’ also (14.11). Stunde ae Sometimes ‘hour’), NHG Period of ti a Since 15th cent.), orig.
```


## [2026-09-05T21:00:17.585Z] TOOL CALL #65: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg181.png"
}
```


### [2026-09-05T21:00:17.968Z] TOOL RESULT

```

```


## [2026-09-05T21:00:17.958Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T21:00:45.457Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### yester-\"; sed -n '20,40p' ec39522c85b7c609.txt; echo \"### heres\"; grep -n -i \"Etymology\\|Proto-Italic\\|orphan\\|heir\" 9e2c24cf83667ad8.txt | head -12; echo \"### go\"; sed -n '20,32p' 3cca67aa58fd7cc6.txt",
 "description": "Read etymonline/wiktionary snippets"
}
```


### [2026-09-05T21:00:45.528Z] TOOL RESULT

```
### yester-

 Origin and history of yester- 

 yester- 

 "next before the present," from Old English geostran "yesterday," from Proto-Germanic *gester- (source also of Old High German gestaron , German gestern "yesterday," Old Norse gær "tomorrow, yesterday," Gothic gistradagis "tomorrow"). Compare yesterday .

 Originally "the other day" (reckoned from "today," either backward or forward), according to Watkins from PIE root *dhgh(y)es- "yesterday" (source also of Sanskrit hyah , Avestan zyo , Persian di , Greek khthes , Latin heri , Old Irish indhe , Welsh doe "yesterday;" Latin hesternus "of yesterday").

 As also in yestereven "on the evening of the day before the present," also yestere'en ; yestereve ; yestermorn , yestermorning ; yesternight ; yesteryear .

 Entries linking to yester- 

 yesterday (n., adv.) 

 Middle English yesterdai , "the day last past; during the day preceding the present," from Old English geostran dæg ; see yester- + day .

 Other Germanic languages tend to use their version of yester- alone for this (German  gestern , etc.). The only known parallel is in Gothic ( gistradagis ). The transferred sense of "a short time ago" is by late 14c. To want or need (something) yesterday "right away" is by 1974.

 yesternight (n., adv.) 

### heres
76: Etymology 
102: Etymology 1 
123: Etymology 2 
129: Etymology 3 
135: Etymology 4 
144: Etymology 5 
153: Etymology 6 
268: Etymology
285: heir , heiress 
290:dēbentur.” [...] “If the glories of such deeds do not inspire you – [and moreover, neither are you yourself endeavoring an effort with merit] – consider Ascanius, [now] coming of age, and the hope of [your] heir Iulus, to whom is due the rule of Italy and the land of Rome.” 
293: : "Hoc Monumentum Hērēdem Nōn Sequitur" "This tombstone does not follow the heir ." (An inscription sometimes found on Ancient Roman tombstones, seemingly to stop a tombstone’s being sold off for money by the dead Roman’s heirs.) 
370: Old French: eir Anglo-Norman: heir , aire → Middle English: heir English: heir 
### go

 Origin and history of go 

 go (v.) 

 Old English gan "to advance, walk; depart, go away; happen, take place; conquer; observe, practice, exercise," from West Germanic *gaian (source also of Old Saxon, Old Frisian gan , Middle Dutch gaen , Dutch gaan , Old High German gan , German gehen ), from PIE root *ghē- "to release, let go; be released" (source also of Sanskrit jihite "goes away," Greek kikhano "I reach, meet with"), but there does not seem to be general agreement on a list of cognates.

 A defective verb throughout its recorded history; the Old English past tense was eode , a word of uncertain origin but evidently once a different verb (perhaps connected to Gothic iddja ); it was replaced 1400s by went , past tense of wenden "to direct one's way" (see wend ). In northern England and Scotland, however, eode tended to be replaced by gaed , a construction based on go . In modern English, only be and go take their past tenses from entirely different verbs.

 The word in its various forms and combinations takes up 45 columns of close print in the OED. Meaning "cease to exist" is from c. 1200; that of "to appear" (with reference to dress, appearance, etc.) is from late 14c.; that of "to be sold" is from early 15c. Meaning "to be known" (with by ) is from 1590s; that of "pass into another condition or state" is from 1580s. From c. 1600 as "to wager," hence also "to stand treat," and to go (someone) better in wagering (1864). Meaning "say" emerged 1960s in teen slang. Colloquial meaning "urinate or defecate" attested by 1926, euphemistic (compare Old English gong "a privy," literally "a going").

 To go back on "prove faithless to" is from 1859; to go under in the figurative sense "to fail" is from 1849. To go places "be successful" is by 1934.
```


## [2026-09-05T21:01:09.370Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^دی\\b\\|^دی:\" MON_part1.txt | head -10; echo \"---\"; sed -n '64570,64580p' MON_part1.txt",
 "description": "Find Mo'in دی entry"
}
```


### [2026-09-05T21:01:09.436Z] TOOL RESULT

```
1263:دیدکان به علت کسالت با سماری. آب دادن 
1372:دیگر که در آب افتاده و زیان دیده باشد. 
1855:دیگر است. 
1923:دیگر از آنها ترکیب می‌شود. (گیا.) به؛ 
2244:دیگری» یکی از دو چیز یا دو کس» غیر؛ ج. 
2259:دیگر سرای دیگی عقمی. 
3354:دیوزده» سابه‌دار. 
3836:دینام و باتری موقعی وصل می‌کند که ولت 
3837:دینام بالاتر از ولت باتری گردد یعنی فقط 
4403:دیواری که برای حفظ سیاه کشند؛ بش کر 
---


۷۲ فرهنگ فارسی معین دیگ 


بکار رود. دیک بار گذاشتن تن: (عم.) گذاشتن 
درگ محتوی مواد غدذایی بر روی اجاق. 
دیگ: عآه (- دی] (ق.) دی» روز گذشته. 
دیگ‌افسزار: تقادص [- دیگک‌اوزار ۰ 
دیگ‌ابزار ] (امر.) داروهای خوشبویی که در 
دیگ خوراک‌پزی ریزند مانند فلفل»
```


## [2026-09-05T21:01:14.122Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"دیروز\\|دوش\\|روز گذشته\" MON_part1.txt | sed -n '1,12p'; echo \"=== search دی (ق.) ===\"; grep -n \"دی: \\|دی ‪\" MON_part1.txt | head -5",
 "description": "Search Mo'in for dī entry"
}
```


### [2026-09-05T21:01:14.199Z] TOOL RESULT

```
3173:را بو شد از بن دوش تا بند وا قدر 
4726:آمدوشد؛: 2020-0-0 (مص خم. مر.) آمد 
7915:بند کنند و دیگری را بر دوش پوشند. 
16799:آمس: 2۳5 [ع.] (ق.) دیروز. 
18397:عسل» سیره» دوشاب. (امر.) عهد» شرط» 
20054:بار: ۲ آنچه که بر دوش و بشت انسان با 
20119:پشت و دوش خود حمل کند: باربرنده» 
20806:بکارت او نرفته باشد» دوشيزه. 
21922:همدوش» همسان» همردیف. مطایق» معادل» 
23938:دوشاب و با از نان تنکك و روغن و خرما 
24490:دوشبزه بودن. (امص.) دختری» دوشی زگی. 
24491:تا زگی. ازاله بکارت کردن: دوشیزگی دختر 
=== search دی (ق.) ===
65:قیمت دوره دو جلدی: ۱۲۰/۰۰۰ ریال 
1002:ابادی: 2020 (حامص.) عمارت؛ 
2847:آزادی: ]27:4 ۳ .) حریت» آزادگی؛ 
4341:انسان؛ آلت زنانگی. آالت مردی: (جاد.) 
4954:فرزندی: اردشیر بابکان (اردشیر پسر
```


## [2026-09-05T21:02:26.565Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KLN1966 go ==\"; grep -n \"^go,  intr\\|go,  intr\" KLN_1966.txt | head -3; echo \"== WLD ghe- leer sein ==\"; grep -n \"leer sein, fehlen\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt incoming/WLD/WLD_Bd1_pages.txt | head -5",
 "description": "Locate KLN go leaf and WLD ghe-"
}
```


### [2026-09-05T21:02:26.628Z] TOOL RESULT

```
== KLN1966 go ==
16366:Derivative :  Gnostic-ism,  n. gnu,  n.,  a  large  S.  African  antelope.  —  Fr.  gnoo, the  word  by  which  the  German  traveler  Georg Forster  (1754-1794)  rendered  Kaffir  ngu  (in  his book  ‘A  Voyage  Around  the  World’,  I,  p.83). go,  intr.  v.  —  ME.  gon,  fr.  OE.  gan,  rel.  to  OS., OFris.,  MLG.  gan,  Dan.  gaa,  Swcd.  gi,  MDu. gaen,  Du.  gaan,  OHG.,  MHG.  gan,  gen,  G. gehen,  Crimean  Goth,  geen,  ‘to  go’,  fr.  I.-E. base  *ghe-,  *ghei-.  The  same  base  appears  re¬ duplicated  in  OI.  jihite  (for  *ghi-ghe-te ),  ‘goes away’,  jd-hd-ti  (for  *ghe-ghe-ti),  ‘leaves,  aban¬ dons’,  Gk.  xty&vro  (for  *ghi-ghe-nd),  xiy_T]^u (for  *ghi-ghe-mi),  ‘I  reach,  meet  with’,  Avestic zazami,  ‘I  dismiss’.  Base  *ghe-,  *ghei-,  ‘to  go’, is  identical  with  base  *ghe~,  *ghei-,  ‘to  lack,  be in  want  of’  (prop,  ‘to  go  without’),  whence  Gk. XijToi;,  ‘want,  need’,  ya-reiv,  ‘to  want,  be  in need  of,  long  for,  desire’,  yff'K,  ‘bereaved  of’, L.  heres,  ‘heir’ ;  see  heredity  and  cp.  chori-.  Cp. ago.
== WLD ghe- leer sein ==
```


## [2026-09-05T21:02:38.594Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} /go,  intr\\.  v\\.  —  ME\\.  gon/ {print \"leaf\",NR}' KLN_1966.txt; echo \"-- HENNING sogdian --\"; grep -n \"zyy myδ\\|ʾnyy\\|nyy my\" HENNING_selected_papers.txt | head -5",
 "description": "KLN go leaf; Henning grep"
}
```


### [2026-09-05T21:02:40.596Z] TOOL RESULT

```
leaf 360
-- HENNING sogdian --
```


## [2026-09-05T21:02:49.520Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==345 {print substr($0,1,700)}' KLN_1966.txt; echo \"....\"; awk 'BEGIN{RS=\"\\f\"} NR==345 {print substr($0,length($0)-400)}' KLN_1966.txt",
 "description": "Print KLN leaf 345"
}
```


### [2026-09-05T21:02:51.319Z] TOOL RESULT

```
 Glossarium  mediae  et  in- fimae  latinitatis,  s.v.  balare. galingale,  n.,  an  aromatic  root  of  the  ginger family.  —  OF.  galingal,  formed— through  the medium  of  MGk.  yaXxyyoc  and  ML.  galanga fr.  Arab,  khalanjdn,  fr.  Pers.,  ult.  fr.  Chin.  Ko- leung-keung,  lit.  ‘mild  ginger  from  the  region of  Kao’.
Galinsoga,  n.,  a  genus  of  plants  (bot.)  —  ModL.,
galiot
gambade
named  after  the  Spanish  botanist  Mariano Martinez  de  Galinsoga  (died  in  1 797). galiot,  galliot,  n.,  a  small  swift  galley.  —  F. galiote,  fr.  OF.  galie.  See  galley, galipot,  gallipot,  n.,  resinous  substance  of  certain pines.  —  F.  galipot,  of  unkno
....
e  rel.  to  Heb.  gamal.  For  the  second  element in  the  name  Gamaliel  see  El. gamashes,  n.  pi.,  a  kind  of  legging  (archaic).  — F.  gamaches,  fr.  ModProven?.  gamacho,  fr. OProvent;.  galamacha,  fr.  Sp.  guadamaci,  fr. Arab,  ghadamast,  lit.  ‘(leather)  from  Ghadames (a  town  in  Tripolis)’.
gamb,  gambe,  n.,  an  animal’s  leg  or  shank;  used esp.  in  heraldry
```


## [2026-09-05T21:03:06.007Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=358 && NR<=362 {print \"== leaf\",NR; print}' KLN_1966.txt | grep -o \"\\b6[0-9][0-9]\\b\\|\\b7[0-9][0-9]\\b\\|== leaf [0-9]*\" | head -20",
 "description": "Find printed page numbers near KLN go"
}
```


### [2026-09-05T21:03:07.759Z] TOOL RESULT

```
== leaf 358
661
== leaf 359
== leaf 360
664
665
== leaf 361
666
667
== leaf 362
668
669
670
```


## [2026-09-05T21:03:13.251Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==361 {print substr($0,1,900)}' KLN_1966.txt",
 "description": "Print KLN leaf 361 start"
}
```


### [2026-09-05T21:03:14.821Z] TOOL RESULT

```
 without’),  whence  Gk. XijToi;,  ‘want,  need’,  ya-reiv,  ‘to  want,  be  in need  of,  long  for,  desire’,  yff'K,  ‘bereaved  of’, L.  heres,  ‘heir’ ;  see  heredity  and  cp.  chori-.  Cp. ago.
Derivatives:  go,  n.,  that  which  goes,  go-er,  n., go-ing,  n.
goad,  n.  —  ME.  gode,  fr.  OE.  gad,  ‘point,  sting, goad,  arrow’,  rel.  to  Lombard  gaida,  ‘spear’, and  cogn.  with  OI.  hetih,  ‘missile,  projectile’, hdyati,  hinSti,  ‘pushes  on,  hurls’,  Avestic  zaina-, ‘weapon’,  Gk.  x«ioc,  ‘shepherd’s  staff’,  Gaul.- L.  gaesum,  ‘a  long  heavy  javelin’,  OIr.  gae, ‘spear’,  OE.  gar,  ‘spear’,  Du.  gesel,  OHG. geisila,  MHG.  geisel,  G.  Geiffsl,  ‘whip,  lash’.
666
All  these  words  are  traceable  to  I.-E.  base  *ghei-, ‘to  drive  on,  push  on’.  Cp.  gore,  ‘a  triangular piece  of
```


## [2026-09-05T21:03:23.214Z] TOOL CALL #74: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg181.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/181.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -3",
 "description": "Copy page image for audit"
}
```


### [2026-09-05T21:03:23.279Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-05T21:11:31.688Z] TOOL CALL #75: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build181.py",
 "content": "# -*- coding: utf-8 -*-\nimport json, io\n\nW_DHGHYES = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰǵʰyés\"\nW_DI = \"https://en.wiktionary.org/wiki/%D8%AF%DB%8C\"\nE_YESTER = \"https://www.etymonline.com/word/yester-\"\nW_GHEH1 = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0eh%E2%82%81-\"\nW_HERES = \"https://en.wiktionary.org/wiki/heres\"\nE_HEIR = \"https://www.etymonline.com/word/heir\"\nE_GO = \"https://www.etymonline.com/word/go\"\n\ndoc = {\n  \"pdf_page\": 181,\n  \"book_page\": 151,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": []\n}\n\n# ---------------------------------------------------------------- entry 0\ne0 = {\n  \"entry\": 0,\n  \"root\": \"Ghdies, Ghdes, Ghies, Ghes\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *dʰǵʰyés (Pokorny's notation ǵhdies / ǵhdes / ǵhies / ǵhes) 'yesterday'\",\n  \"note\": \"The root box is copied verbatim from Pokorny IEW 416, whose entry opens 'ghdies (schwundst. ghdis?), vereinfacht (?) zu ghdes, ghies, ghes „gestern“' — Nourai's four variant shapes, the label Indo-European and the gloss 'yester' (= German 'gestern') are all exact. Watkins/AHD writes the same root dhgh(y)es- 'yesterday' [Pok. ghdhies 416]; de Vaan (s.v. heri) and Wiktionary reconstruct *dʰǵʰyés, i.e. only the notation of the difficult initial 'thorn' cluster differs, not the root. The one real weakness of the chart is the Avestan node: the form zyō that the whole handbook tradition prints has no attestation in the Avestan corpus (see node 1), and the Persian branch does not in fact pass through Avestan (node 2).\",\n  \"note_fa\": \"جعبهٔ ریشه دقیقاً از پوکورنی صفحهٔ ۴۱۶ گرفته شده است؛ وی ریشه را چنین می‌آورد: ghdies و صورت‌های ساده‌شدهٔ ghdes، ghies، ghes «دیروز». پس برچسب زبان (هندواروپایی آغازین)، صورت‌ها و معنا درست است؛ ریشه‌شناسی امروزی (دووان، ویکی‌واژه) همان ریشه را *dʰǵʰyés می‌نویسد و تفاوت تنها در شیوهٔ نوشتن خوشهٔ آغازین است. دو نقطهٔ سست نمودار این است که یکم صورت اوستایی zyō در متن اوستا شاهدی ندارد (گره ۱) و دوم آنکه «دی» فارسی از راه اوستایی نیامده بلکه دنبالهٔ صورت جنوب‌غربی (پارسی باستان) است (گره ۲).\",\n  \"sources\": [W_DHGHYES, E_YESTER],\n  \"ref_check\": [\n    {\"ref\": \"POK:416\", \"status\": \"supports\",\n     \"note\": \"POK_02.txt leaf 73 (= IEW p.416; POK_02: leaf = p − 344): 'ghdies (schwundst. ghdis?), vereinfacht (?) zu ghdes, ghies, ghes „gestern“. — Ai. hyáḥ „gestern“ (ghies), hyastana-ḥ „gestrig“, av. zyō, apers. diya(ka), pers. di(g)' — the root box, its four shapes and the gloss are Nourai's source word for word.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I p. 664 (WLD_Bd1_pages.txt line 62934 ff.)\", \"stance\": \"supports\",\n     \"note\": \"'gh[di]es oder ghjes „gestern“ ... Ai. hyas „gestern“, hyastana „gestrig“, np. di, dig ... gr. χθές, ἐχθές ... Lat. heri, here „gestern“ ... Got. gistradagis' — Walde-Pokorny is Pokorny's own source; note it lists NO Avestan form.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, dh-list (AHD_watkins1985.txt line 382)\", \"stance\": \"supports\",\n     \"note\": \"'dhgh(y)es-. Yesterday. Suffixed (comparative) form (dh)ghes-ter- in Germanic *ges-ter- in Old English geostran, giestran, “yester-”: YESTER-, (YESTERDAY). [Pok. ghdhies 416.]'\"},\n    {\"src\": \"SYN\", \"where\": \"Buck §14.49 'yesterday' (SYN.txt line 25472 ff.)\", \"stance\": \"supports\",\n     \"note\": \"'1. IE *hes, etc. (variant init. combinations). Walde-P. 1.664. ... Skt. hyas and adj. hyastana-, NPers. di, dig, dine; Alb. dje.' Buck's word-table carries an Avestan column whose form the OCR renders unreadably ('Av. te'), and his discussion cites only Sanskrit and New Persian on the Indo-Iranian side.\"}\n  ],\n  \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n  \"id\": 1, \"lang\": \"Avestan\", \"words\": \"zyô\", \"verdict\": \"disputed\",\n  \"derivation\": \"PIE *dʰǵʰyés > Proto-Indo-Iranian *ǳʰyás > Sanskrit hyáḥ 'yesterday'; the Iranian counterpart of hyáḥ is quoted throughout the handbooks as Avestan zyō, and Pokorny 416 prints 'av. zyō' immediately after 'ai. hyáḥ', which is where Nourai took it from (with Klein s.v. yester-, 'cogn. with OI. hyah, Avestic zyo, Pers. di'). Phonologically the form is unobjectionable (PIE *ǵʰ > Iranian *ǳʰ > Avestan z, as in Av. zasta- 'hand', zaraδ- 'heart'), but it is a ghost-word: Bartholomae's Altiranisches Wörterbuch (1904) — compiled precisely to replace Fick's uncited citation-forms — has no entry zyō at all (the z-section runs zyā- 'schädigen', zyānay-, zyānā-, zyānāi, zyeiṯ, zyu-, then zra̱ka-), and Horn, Grundriss der neupersischen Etymologie no. 590, states in a footnote that 'in Fick's dictionary one repeatedly finds an aw. zyō “gestern” without an asterisk and — unfortunately — also without a citation'. Walde-Pokorny I 664 likewise gives Sanskrit hyas and NPers. dī, dīg but no Avestan word. The chain Fick > Pokorny > Klein > Watkins/AHD > Etymonline > Gharib has simply repeated the form; it is not attested in the Avesta.\",\n  \"derivation_fa\": \"صورت هندواروپایی *dʰǵʰyés در هندوایرانی آغازین *ǳʰyás و در سنسکریت hyáḥ «دیروز» شده است؛ برابر ایرانی آن را فرهنگ‌نویسان اوستایی zyō می‌نویسند و نورایی نیز همین را از پوکورنی (ص ۴۱۶) و کلاین گرفته است. از نظر آوایی ایرادی بر این صورت نیست (در اوستایی *ǵʰ همیشه z می‌دهد، مانند zasta- «دست»)، اما این واژه در متن اوستا شاهدی ندارد: در فرهنگ ایرانی باستان بارتولومه (۱۹۰۴) مدخلی به نام zyō نیست، و هرن در شمارهٔ ۵۹۰ در پاورقی صریحاً می‌گوید که فیک این صورت را بی‌ستاره و متأسفانه بی‌هیچ شاهدی آورده است؛ والده‑پوکورنی (ج۱ ص ۶۶۴) هم هیچ صورت اوستایی نمی‌آورد. پس این واژه یک «واژهٔ شبح» است که از فیک به پوکورنی و از آنجا به دیگران رسیده است؛ ادعای نورایی در این گره با احتیاط باید خوانده شود.\",\n  \"sources\": [W_DHGHYES, E_YESTER],\n  \"ref_check\": [\n    {\"ref\": \"POK:416\", \"status\": \"supports\",\n     \"note\": \"IEW p.416 (POK_02.txt leaf 73) does print 'av. zyō' among the reflexes — so Nourai's citation is accurate; the reference itself, however, is repeating Fick.\"},\n    {\"ref\": \"KLN:1762\", \"status\": \"supports\",\n     \"note\": \"Klein s.v. yester- (KLN_1971.txt line 269780; = 1966 two-vol. p.1762, the y-section near the end of vol. II): 'They are cogn. with OI. hyah, “yesterday”, Avestic zyo, Pers. di, “yesterday”, Toch. ksar ... Gk. χθές ... L. heri'. Note Klein calls them cognates, not a chain.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"z-section, between zyānāi and zra̱ka- (BRT.txt lines 28301-28310)\", \"stance\": \"contradicts\",\n     \"note\": \"Bartholomae's Altiranisches Wörterbuch has no headword zyō: the sequence is 'j. zyānāi Inf. „zu schädigen“ ... j. zyeiṯ F.25b ... j. zyu- ... p. *zra̱ka- m. Name eines Landes, Drangiana'. The standard Avestan lexicon does not know the word.\"},\n    {\"src\": \"HRN\", \"where\": \"no. 590, p.131 f., footnote 4 (HRN.txt line 5297, leaf 153 = printed p.132)\", \"stance\": \"contradicts\",\n     \"note\": \"'Bei Fick findet man im Wörterbuch mehrmals ein aw. zyō „gestern“ ohne Stern und — leider auch ohne Beleg.' Horn names the source of the ghost-form and denies it any attestation.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. I p. 664\", \"stance\": \"silent\",\n     \"note\": \"the entry 'gh[di]es oder ghjes „gestern“' lists Ai. hyas, np. di/dig, Greek, Latin, Albanian, Celtic and Germanic — and no Avestan form at all.\"}\n  ]\n})\n\ne0[\"nodes\"].append({\n  \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"dîk\", \"verdict\": \"plausible\",\n  \"derivation\": \"The Middle Persian word is genuine: MacKenzie's Addenda to the Concise Pahlavi Dictionary adds 'dīg [YTMAL < A ʾTMʾL | N dī] yesterday' — written with the Aramaic ideogram YTMAL (Aram. ʾetmāl 'yesterday'), read dīg; and Horn no. 590 already had 'phlv. dīk (PPGl.)', which is exactly Nourai's spelling (book-Pahlavi <dyk> in the older -k transliteration = MacKenzie's dīg). What is wrong is the arrow. Avestan z- can never give Persian d-: the two are the regular dialectal reflexes of Old Iranian *ǳʰ (< PIE *ǵʰ), north-eastern/Avestan z versus south-western/Old Persian d — the same split as Av. zasta- : OP dasta- 'hand', Av. zrayah- : OP drayah- 'sea', Av. zaraδ- : NP del 'heart', Av. daēza- : NP dez 'fort'. Hübschmann, Persische Studien p.221, lists 'dī, dīg “gestern” = skr. hyas' in precisely that list of south-western d-words. MP dīg therefore continues an Old Persian *diya-ka- (Pokorny 416 quotes 'apers. diya(ka)', though no such form is attested in the Achaemenid inscriptions — Kent's lexicon has none), a sister of the Avestan word, not its descendant; Wiktionary accordingly takes دی straight from MP /dīk/ < Proto-Indo-Iranian *ǳʰyás.\",\n  \"derivation_fa\": \"صورت فارسی میانه درست است: مکنزی در افزوده‌های فرهنگ کوچک پهلوی خود «dīg [YTMAL] ، فارسی نو: دی، دیروز» را می‌افزاید و هرن نیز در شمارهٔ ۵۹۰ همین «dīk» را می‌آورد؛ نوشتار dyk در خط پهلوی کتابی همان dīg خوانده می‌شود. اما جهت پیکان نادرست است: z اوستایی هرگز در فارسی به d بدل نمی‌شود؛ این دو بازتاب‌های گویشی از یک صورت ایرانی باستان‌اند — شمال‌شرقی/اوستایی z در برابر جنوب‌غربی/پارسی باستان d — همان دوگانگی که در zasta-/dasta- (دست)، zrayah-/drayah- (دریا) و zaraδ-/دل دیده می‌شود؛ هوبشمان در مطالعات ایرانی ص ۲۲۱ دقیقاً «dī، dīg» را در همین فهرست می‌آورد. پس dīg پهلوی دنبالهٔ *diya-ka- پارسی باستان است، نه فرزند صورت اوستایی؛ نمودار در اینجا باید اصلاح شود.\",\n  \"sources\": [W_DI],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node; the form was checked against MacKenzie, Horn and Hübschmann under 'consulted'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary, Addenda & Corrigenda s.v. dīg (PHD_mackenzie.txt line 533; also PHD.txt line 125)\", \"stance\": \"supports\",\n     \"note\": \"'add dīg [YTMAL < A ʾTMʾL | N dī] yesterday.' — the Middle Persian word exists and gives NP dī, exactly as the chart's Pahlavi→Persian arrow says.\"},\n    {\"src\": \"HRN\", \"where\": \"no. 590, p.131 f. (HRN.txt line 5286)\", \"stance\": \"supports\",\n     \"note\": \"'ai. hyás „gestern“; phlv. dīk (PPGl.)' — Horn spells the Pahlavi word exactly as Nourai does.\"},\n    {\"src\": \"HUB\", \"where\": \"Persische Studien p.221 (HUB.txt line 7843, leaf 231 = printed p.221)\", \"stance\": \"contradicts\",\n     \"note\": \"'6) dahan „Mund“ = zd. zafan-; 7) dī, dīg „gestern“ = skr. hyas; 8) daryā „Meer“ = ap. draya-, zd. zrayah-' — Hübschmann files dī/dīg among the words whose d- is the Old Persian (south-western) reflex facing Avestan z-, i.e. Persian cannot descend from the Avestan form.\"},\n    {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon (grep 'diya' in KNT.txt)\", \"stance\": \"silent\",\n     \"note\": \"no Old Persian word for 'yesterday' is attested in the inscriptions; Pokorny's 'apers. diya(ka)' is an inference from Middle Persian, not a text form.\"},\n    {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary (grep 'dyk' in NYB_vol2_glossary.txt)\", \"stance\": \"silent\",\n     \"note\": \"the glossary has only 'dēk [dyk] pot, vessel 423. — NP dēg'; the adverb dīg does not occur in Nyberg's text selection.\"}\n  ]\n})\n\ne0[\"nodes\"].append({\n  \"id\": 3, \"lang\": \"Persian\", \"words\": \"dî\", \"verdict\": \"confirmed\",\n  \"derivation\": \"NP دی dī 'yesterday, yester-' < MP dīg/dīk, with the ordinary New Persian loss of the old suffixal -g in the free-standing adverb (Persian keeps both: dī and dīg, cf. Hübschmann §135 on Pahlavi final -k > NP -g in sag, dīg, xūg). The word is archaic as a simplex but productive as a first element, which is why Nourai's box glosses it with دیروز dī-rōz 'yesterday' and دیشب dī-šab 'last night'; Horn no. 590 lists 'dī, dīg „gestern“, dīm, dīrōz, dīšeb' as one family, and Mo'in's Farhang has 'دیگ [= دی] (ق.) دی، روز گذشته'. Wiktionary glosses دی (dī) '(archaic) yester' — Nourai's gloss 'yester' is exactly right, and his Persian script and the numbered homonym (دی ۳, distinguishing it from دی the month-name and دی 'creator') follow Mo'in's own numbering. The one nuance is that this دی has nothing to do with the month دی (Day, MP dadū/dady, 'creator'), which is a different word entirely.\",\n  \"derivation_fa\": \"«دی» فارسی نو از فارسی میانهٔ dīg / dīk است و پسوند پایانی در کاربرد قیدی افتاده است؛ فارسی هر دو صورت «دی» و «دیگ» را دارد (هوبشمان، بند ۱۳۵). امروز این واژه به تنهایی کهنه است ولی در ترکیب‌های «دیروز» و «دیشب» زنده است — همان‌ها که نورایی در جعبه آورده است. هرن (ش ۵۹۰) همان خانواده را می‌شمارد و معین می‌نویسد «دیگ [= دی] (ق.) دی، روز گذشته»؛ حاشیهٔ معین بر برهان قاطع نیز همین ریشه را با سنسکریت hyás و پهلوی dīk می‌سنجد. باید توجه داشت که این «دی» با «دی» نام ماه (از فارسی میانهٔ dadū «دادار») یکی نیست؛ ادعای نورایی در این گره درست است.\",\n  \"sources\": [W_DI],\n  \"ref_check\": [\n    {\"ref\": \"MON:1588\", \"status\": \"partial\",\n     \"note\": \"The six-volume Farhang-e Farsi cannot be paged online, so the exact page could not be verified; the entry itself is there in the two-volume abridgement (MON_part1.txt line 64577): 'دیگ: [= دی] (ق.) دی، روز گذشته' ('dīg = dī, adv., yesterday, the day gone by'), i.e. Mo'in supports both the form and the gloss; only the page number is unchecked.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"HRN\", \"where\": \"no. 590, p.131 (HRN.txt line 5284)\", \"stance\": \"supports\",\n     \"note\": \"'590. dī, dīg „gestern“, dīm (Is. 30, 33), dīme, dīrōz, dīšeh.' — the family Nourai prints in the box, with the same compounds.\"},\n    {\"src\": \"HUB\", \"where\": \"Persische Studien §135, p.241 (HUB.txt line 8589)\", \"stance\": \"supports\",\n     \"note\": \"'1. Regelmässig: a) sag „Hund“ = ... zd. spā; dīg „gestern“ (neben dī), bal. zīk; xūg „Schwein“' — the dī ~ dīg doublet explained as the regular treatment of Pahlavi final -k.\"},\n    {\"src\": \"MON\", \"where\": \"Farhang-e Farsi (2-vol. abridgement), s.v. دیگ (MON_part1.txt line 64577)\", \"stance\": \"supports\",\n     \"note\": \"'دیگ: [= دی] (ق.) دی، روز گذشته.'\"},\n    {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' ed. Mo'in, footnote to دی (BQT_v2_pages.txt lines 21808-21809)\", \"stance\": \"supports\",\n     \"note\": \"the etymological footnote, though badly OCR'd, is legibly 'هندی باستان hīyas ... ( دیروز ) ... پهلوی [d]īk ... کردی ... بلوچی ... ( دیروز )' — Mo'in derives دی from the same Indo-Iranian word via Pahlavi dīk, with Kurdish, Ossetic and Baluchi cognates, i.e. Horn's picture.\"}\n  ]\n})\n\ne0[\"nodes\"].append({\n  \"id\": 4, \"lang\": \"Sogdian\", \"words\": \"`zyy-myd\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Gharib, Sogdian Dictionary p.94, entry 2376, reads: 'ʾZYY MYδ  S  (a)ze-meθ ?  ©Av. zyō  ⇒ ʾpzymyδ — yesterday — Anc. Lett. 2.16, ʾnyy myδ; Hen. Date. 604 n4; Benv. Ét. Oss. 109'. So Nourai's SOD:94 is a page number (not an entry number) and is exactly right, and his '`zyy-myd' renders ʾzyy myδ (the backtick = aleph, yy = /ē/, d = δ). The word is a compound of the inherited 'yesterday' adverb — Sogdian z- being the regular eastern-Iranian reflex of Old Iranian *ǳʰ, the exact counterpart of the form the handbooks call Avestan zyō — with myδ 'day' (< Old Iranian *maiθa-), literally 'yester-day', the same compound type as Old English geostran dæg. It is attested in the Sogdian Ancient Letters found at Dunhuang (early 4th c. CE), Letter 2 line 16, in the spelling ʾnyy myδ, discussed by Henning, 'The Date of the Sogdian Ancient Letters' (BSOAS 12, 1948, p.604 n.4) and by Benveniste, Études sur la langue ossète p.109. The chart's arrow, root → Sogdian, is correct as drawn (Gharib's own '©Av. zyō' is a comparison, not a claim of descent from Avestan).\",\n  \"derivation_fa\": \"غریب در فرهنگ سغدی، صفحهٔ ۹۴، مدخل ۲۳۷۶، می‌آورد: ʾzyy myδ «دیروز»، با ارجاع به نامه‌های باستانی سغدی ۲ؚ۱۶. پس ارجاع نورایی (SOD:94) شمارهٔ صفحه است و درست است. این واژه ترکیبی است از قید ارثی «دی» (با z که بازتاب معمول *ǳʰ در ایرانی شرقی است) با myδ «روز»، یعنی تحت‌اللفظ «دی‌روز» — دقیقاً همان الگوی ساختاری که در انگلیسی کهن geostran dæg و در فارسی «دیروز» دیده می‌شود. پیکان نمودار (ریشه ← سغدی) درست است.\",\n  \"sources\": [],\n  \"ref_check\": [\n    {\"ref\": \"SOD:94\", \"status\": \"supports\",\n     \"note\": \"SOD_pages.txt lines 10611-10618, printed page 94: '2376  ʾzyy myδ   S ... (a)ze-meθ ? ©Av. zyō ⇒ ʾpzymyδ / yesterday / Anc. Lett. 2.16, ʾnyy myδ; Hen. Date. 604 n4; Benv. Ét. Oss. 109'. Page number, transliteration and gloss all match the chart.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"SOD\", \"where\": \"Gharib, Sogdian Dictionary, p.94 no.2376 and p.~ no.1230 (SOD_pages.txt lines 7279, 10616)\", \"stance\": \"supports\",\n     \"note\": \"no. 1230 'ʾnyy myδ  S ⇒ ʾzyy myδ' cross-refers the Ancient-Letters spelling to the same lemma — the word is real and attested.\"},\n    {\"src\": \"HENNING\", \"where\": \"Selected Papers (grep 'ʾnyy', 'zyy my' in HENNING_selected_papers.txt)\", \"stance\": \"silent\",\n     \"note\": \"the OCR of the Selected Papers does not carry the Sogdian transliterations of 'The Date of the Sogdian Ancient Letters' in a searchable form; Gharib's citation 'Hen. Date. 604 n4' could not be read directly.\"}\n  ]\n})\n\ne0[\"nodes\"].append({\n  \"id\": 5, \"lang\": \"Germanic\", \"words\": \"ges-ter\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Nourai's 'ges-ter' is Watkins's reconstruction copied letter for letter, and his refs=AHD is therefore exact: 'dhgh(y)es-. Yesterday. Suffixed (comparative) form (dh)ghes-ter- in Germanic *ges-ter- in Old English geostran, giestran, “yester-”: YESTER-, (YESTERDAY). [Pok. ghdhies 416.]'. The -ter- is the old contrastive suffix that also makes Latin hes-ternus and Sanskrit hyas-tana- 'of yesterday'; in Germanic it yields *gestra- > Gothic gistra-dagis (which means 'tomorrow', the original sense being simply 'the other day', reckoned either way), Old English geostran/giestran/gystran, Old High German gestre, gesteron, gesteren, German gestern, Dutch gisteren, with a lengthened-grade by-form *gēz- in Old Norse í gær. Klein and Skeat give the same Germanic set.\",\n  \"derivation_fa\": \"صورت «ges-ter» دقیقاً بازساخت واتکینز در پیوست ریشه‌های هندواروپایی فرهنگ میراث آمریکایی است: ژرمنی آغازین *ges-ter- که در انگلیسی کهن geostran / giestran شده است. پسوند -ter- همان پسوند تقابلی کهن است که در لاتین hes-ternus و سنسکریت hyas-tana- نیز دیده می‌شود. از *gestra- ژرمنی، گوتی gistra-dagis (به معنای «فردا»، زیرا معنای نخستین «روز دیگر» بوده است)، آلمانی gestern و هلندی gisteren برآمده‌اند. ادعای نورایی درست است.\",\n  \"sources\": [E_YESTER],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"AHD_watkins1985.txt line 382: 'dhgh(y)es-. Yesterday. Suffixed (comparative) form (dh)ghes-ter- in Germanic *ges-ter- in Old English geostran, giestran, “yester-”: YESTER-, (YESTERDAY). [Pok. ghdhies 416.]' — the node is a verbatim copy.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I p. 664 (WLD_Bd1_pages.txt lines 62956-62961)\", \"stance\": \"supports\",\n     \"note\": \"'Got. gistradagis „αὔριον“ ..., ags. giestron ..., ahd. gestre, gesteron, gesteren „gestern“ ...; ablautend in aisl. í gær (<*gēz-)'.\"},\n    {\"src\": \"KLN\", \"where\": \"s.v. yester- (KLN_1971.txt line 269780; 1966 ed. p.1762)\", \"stance\": \"supports\",\n     \"note\": \"'ME. yestren, fr. OE. geostran-, also giestran-, gystran, rel. to MLG. ghisteren, Du. gister(en), OHG. gestaron, gesteren, MHG. gester, gestern, G. gestern “yesterday”, ON. í gær ..., Goth. gistradagis “tomorrow”. The orig. meaning of these words was “the other day”.'\"},\n    {\"src\": \"SKT\", \"where\": \"Skeat s.v. Yesterday (SKT.txt lines 21780-21790)\", \"stance\": \"supports\",\n     \"note\": \"'M.E. yisterdai, from A.S. geostra, giestra, gystra (yester-) and dæg, a day. + Du. gisteren, ... G. gestern, Goth. gistra-dagis. β. yester- answers to Lat. hester- in hesternus.'\"}\n  ]\n})\n\ne0[\"nodes\"].append({\n  \"id\": 6, \"lang\": \"English\", \"words\": \"yester, yesterday\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Old English geostran dæg > Middle English yisterdai / yesterdai > Modern English yesterday; the bare first element survives only as the bound prefix yester- (whence yesternight, yestereve, yesteryear), so Nourai's 'yester' is a prefix rather than a free word — Klein files it as 'yester-, pref.'. Etymonline (following Watkins) makes the same chain and notes that the original force was 'the other day', reckoned backward or forward, which is why Gothic gistradagis means 'tomorrow'.\",\n  \"derivation_fa\": \"انگلیسی کهن geostran dæg > انگلیسی میانه yisterdai > انگلیسی نو yesterday. جزء نخست تنها همچون پیشوند مقید yester- برجا مانده است (yesternight، yesteryear)؛ پس «yester» در جعبهٔ نورایی واژهٔ مستقل نیست بلکه پیشوند است. کلاین و اسکیت همین زنجیره را می‌دهند و معنای آغازین را «آن روز دیگر» دانسته‌اند. ادعای نورایی درست است.\",\n  \"sources\": [E_YESTER],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for the English box; checked against Klein, Skeat and Etymonline below.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"s.v. yester-, yesterday (KLN_1971.txt lines 269780-269790)\", \"stance\": \"supports\",\n     \"note\": \"'yesterday, adv. and n. — ME. yisterdai, yesterdai, fr. OE. geostran dæg, also giestran dæg, gystran dæg, n. and adv., “yesterday”. See yester- and day.'\"},\n    {\"src\": \"SKT\", \"where\": \"Skeat s.v. Yesterday (SKT.txt line 21780 ff.)\", \"stance\": \"supports\",\n     \"note\": \"'Yesterday. (E.) M.E. yisterdai, from A.S. geostra ... and dæg, a day.'\"}\n  ]\n})\n\ndoc[\"entries\"].append(e0)\n\n# ---------------------------------------------------------------- entry 1\ne1 = {\n  \"entry\": 1,\n  \"root\": \"Ghě 1, Ghěi 3, Ghi-ghe-me\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *ǵʰeh₁- 'to leave, abandon; (middle) to go away' (LIV² 173; Pokorny ǵhē-, ǵhēi- 418; AHD ghē-)\",\n  \"note\": \"Both of Nourai's references are precise. Pokorny IEW 418 heads the entry 'I. ǵhē-, ǵhēi- A. „leer sein, fehlen“; B. „verlassen, fortgehen“, dann „gehen“', which is exactly Nourai's 'to go, to let go, also to go without (lack)'. The third name in the box, 'Ghi-ghe-me : I reach, meet with', is not a separate root but the reduplicated present *ǵʰi-ǵʰeh₁-mi, and it comes straight from Klein s.v. go (the last part of the entry stands on p.666 of the 1966 two-volume edition, which is what Nourai cites): 'The same base appears reduplicated in OI. jihite (for *ghi-ghe-te), “goes away”, ja-ha-ti (for *ghe-ghe-ti), “leaves, abandons”, Gk. κιχάνω (for *ghi-ghe-no), κίχημι (for *ghi-ghe-mi), “I reach, meet with”, Avestic zazami, “I dismiss”'. Modern handbooks (LIV² 173, Cheung s.v. *zaH, Wiktionary) reconstruct *ǵʰeh₁- 'to leave, abandon' and derive the 'go' sense from it exactly as Pokorny did, so the root box stands; only Nourai's Avestan citation forms and the gloss of Latin hērēs need qualification.\",\n  \"note_fa\": \"هر دو ارجاع نورایی دقیق است. پوکورنی در صفحهٔ ۴۱۸ ریشه را چنین می‌آورد: ǵhē-، ǵhēi- الف) «تهی بودن، کم داشتن»؛ ب) «رها کردن، رفتن» — همان که نورایی ترجمه کرده است. نام سوم جعبه (Ghi-ghe-me) ریشهٔ جداگانه نیست، بلکه ماضیٔ مضاعف (ستاک دوباره‌سازی‌شده) *ǵʰi-ǵʰeh₁-mi است که کلاین ذیل go (ص ۶۶۶ چاپ دوجلدی) با یونانی κίχημι و اوستایی zazami می‌سنجد. پژوهش امروزی (LIV² ۱۷۳ و چونگ ذیل *zaH) همین ریشهٔ *ǵʰeh₁- «رها کردن، واگذاشتن» را می‌پذیرد؛ پس جعبهٔ ریشه درست است و تنها صورت‌های اوستایی و معنای لاتین hērēs نیاز به قید دارند.\",\n  \"sources\": [W_GHEH1, E_GO],\n  \"ref_check\": [\n    {\"ref\": \"POK:418\", \"status\": \"supports\",\n     \"note\": \"POK_02.txt leaf 75 (= IEW p.418): 'I. ǵhē-, ǵhēi- A. „leer sein, fehlen“; B. „verlassen, fortgehen“, dann „gehen“; vielleicht zu ǵhē-, ǵhēi- „gähnen, klaffen“ ... Ai. jáhāti „verläßt, gibt auf“ ... av. zazāmi „ich entlasse aus“ ... gr. κιχάνω ... „erreichen, einholen, treffen“'.\"},\n    {\"ref\": \"KLN:666\", \"status\": \"supports\",\n     \"note\": \"Klein s.v. go: the entry runs over the foot of p.665 onto p.666 of the 1966 two-volume edition (KLN_1966.txt leaves 360-361, printed page numbers 664-665 and 666 visible in the OCR): 'fr. I.-E. base *ghe-, *ghei-. The same base appears reduplicated in ... κίχημι (for *ghi-ghe-mi), “I reach, meet with”, Avestic zazami, “I dismiss”. Base *ghe-, *ghei-, “to go”, is identical with base *ghe-, *ghei-, “to lack, be in want of” (prop. “to go without”), whence Gk. χῆρος “bereaved of”, L. heres, “heir”' — the whole root box, including the odd gloss 'to go without (lack)', comes from this page.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, gh-list (AHD_watkins1985.txt line 510)\", \"stance\": \"supports\",\n     \"note\": \"'ghē-. To release, let go; (in the middle voice) to be released, go. Contracted from *gheə-. 1. Germanic variant form *gaian in Old English gān, to go: GO; AGO, FOREGO¹, FORGO. 2. Suffixed form *ghē-ro- in Latin hērēs, heir (? < “orphan” < “bereft”) ... [Pok. ghē- 418.]' — this single AHD entry is the source of the Germanic and Latin branches of the chart.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"Etym. Dict. of the Iranian Verb, s.v. *zaH (CHEUNG.txt line 29759 ff.)\", \"stance\": \"supports\",\n     \"note\": \"'*zaH “to leave (behind)” ... ©This root has a good IE etymology. «PIE *ǵʰeH₁- “to leave (behind)” > LIV: 173 | Pok.: 418 f.» ... *IE COGNATES: ? Gr. κιχάνω “I overtake, reach, arrive, meet”, Gr. χῆρος “empty, bereft”, Lat. heres.' Cheung endorses Pokorny's page and even his set of cognates.\"},\n    {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. hērēs, p.530 (LAT.txt line 27750 ff.)\", \"stance\": \"partial\",\n     \"note\": \"'il est naturel de rapprocher lat. hērēs de gr. χῆρος “dépouillé” ... Les hypothèses qui ont été proposées sur la formation de hērēs ... sont incertaines.' The root connection is accepted, the internal analysis is not settled.\"}\n  ],\n  \"nodes\": []\n}\n\ne1[\"nodes\"].append({\n  \"id\": 1, \"lang\": \"Avestan\",\n  \"words\": \"zâ 1; â-zâ; uz-zâ, uzayantô; zazâmi; avâ-zazâmi; frâ-zazâmi, upa-zazâmi\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"Every gloss in this box is Pokorny 418 translated: 'av. zazāmi „ich entlasse aus“, mit avə- „entfernen, verscheuchen“, mit upa- und frā- „herzulassen, herzuführen“; ā-zā- „herangehen“, uz-zā- „aufspringen, sich aufrichten“ (uzayantō Partiz. Nom. Pl.)'. Bartholomae's dictionary confirms the material but splits it into two lemmata: (a) 'zā- V. „gehen“, nur mit Praev.', with ā- 'herangehen, herankommen' (Y 50.7 āzāθā) and uz- 'aufspringen, sich aufrichten' (Yt 17.13 uštrāŋhō ... *uzayantō zəmaㆇ 'the camels, rising up from the ground'), compared with Skt. jíhīte and OHG gān; and (b) 'zā(y)- V. „mittere“', 'entlassen aus —' (V 5.17 āpəm zazāmi azəm 'I let the water out'), with avā- 'entfernen, verscheuchen' (Y 34.9 avazazaㆇ), with upa- and frā- 'herzulassen, -führen' (V 5.16, 5.18 upa astəm frazayayāhi), Skt. jáhāti. Two caveats: (i) Nourai's preverbal forms 'avā-zazāmi, frā-zazāmi, upa-zazāmi' are normalised 1sg. citation forms he built himself — the texts have avazazaㆇ (3pl. inj.), (upa ...) frazayayāhi (2sg. subj.), frā ... zazayən; only zazāmi is attested as such (V 5.17); (ii) his gloss 'burst open' for uz-zā is too strong for 'sich aufrichten', 'rise up'. Cheung s.v. *zaH lists the same forms under one Iranian root 'to leave (behind)' with the 'go' senses derived from it, so the merger Nourai inherits from Pokorny is defensible.\",\n  \"derivation_fa\": \"تمام معانی این جعبه برگردان پوکورنی ص ۴۱۸ است. بارتولومه همین مواد را دارد اما در دو مدخل: یکی zā- «رفتن» که تنها با پیشوند می‌آید (با ā- «نزدیک آمدن»، با uz- «برخاستن، راست ایستادن» در یشت ۱۷ؚ۱۳ دربارهٔ شتران) و دیگری zā(y)- «رها کردن، فروگذاشتن» (وندیداد ۵ؚ۱۷: āpəm zazāmi «آب را رها می‌کنم»). دو نکته: نخست آنکه صورت‌های avā-zazāmi و frā-/upa-zazāmi ساختهٔ خود نورایی است و در متن اوستا صورت‌های دیگر (avazazaㆇ، frazayayāhi) آمده است؛ دوم آنکه معنای «burst open» برای uz-zā اغراق‌آمیز است. چونگ ذیل *zaH همهٔ این صورت‌ها را زیر یک ریشه می‌آورد؛ پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n  \"sources\": [W_GHEH1],\n  \"ref_check\": [\n    {\"ref\": \"POK:418\", \"status\": \"supports\",\n     \"note\": \"IEW p.418 (POK_02.txt leaf 75): 'av. zazāmi „ich entlasse aus“, mit avə- „entfernen, verscheuchen“, mit upa- und frā- „herzulassen, herzuführen“; ā-zā- „herangehen“, uz-zā- „aufspringen, sich aufrichten“ (uzayantō Partiz. Nom. Pl.)' — the box is a line-by-line translation of this.\"},\n    {\"ref\": \"KLN:666\", \"status\": \"partial\",\n     \"note\": \"Klein s.v. go cites only 'Avestic zazami, “I dismiss”' of the six forms in the box; the preverbal compounds are not in Klein.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch s.v. zā- and zā(y)- (BRT.txt lines 28060-28090; cf. line 8584)\", \"stance\": \"partial\",\n     \"note\": \"'j., g. zā- V. „gehen“, nur mit Praev. ... mit ā 1) „herangehen, herankommen“ ... mit uz „aufspringen, sich aufrichten“: uštrāŋhō .. *uzayantō zəmaㆇ ... Yt.17.13' and, as a separate lemma, 'j., g. zā(y)- V. „mittere“ ... „entlassen aus —“: āpəm zazāmi azəm .. V.5.17; mit avā „entfernen, verscheuchen“ ... avazazaㆇ (3PPrA.) Y.34.9; mit upa und frā „herzulassen, -führen“: āpəm .. upa astəm frazayayāhi V.5.16'. Also 'j. *uzayant- Adj., PPA.: s. zā-'. Bartholomae confirms the forms but keeps two roots apart and has none of Nourai's 1sg. compound forms.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"s.v. *zaH (CHEUNG.txt lines 29759-29775)\", \"stance\": \"supports\",\n     \"note\": \"'Pres. athem. red.: IND. 1sg. YAv. zazāmi (V 5.17), 3sg. YAv. zazaiti (Yt 5.130), INJ. 3pl. OAv. auuazazaㆇ (Y 34.9), SUBJ. 2sg. YAv. zazāhi (V 5.15) ... OPT. 3pl. YAv. frā ... *zaziian (V 8.37 f.)' — the attested paradigm, which shows that Nourai's avā-/frā-/upa-zazāmi are normalisations.\"},\n    {\"src\": \"POK\", \"where\": \"IEW p.418\", \"stance\": \"supports\", \"note\": \"see ref_check; Pokorny is also the immediate model for the merger of Bartholomae's two roots.\"}\n  ]\n})\n\ne1[\"nodes\"].append({\n  \"id\": 2, \"lang\": \"Germanic\", \"words\": \"gee-n\", \"verdict\": \"confirmed\",\n  \"derivation\": \"'gee-n' is Nourai's rendering of Germanic *gē-n / *gā-n 'to go', the n-stem by-form that gives Old High German and Middle High German gān, gēn, German gehen, and beside it Old English gān, Old Saxon/Old Frisian gān, Dutch gaan. The spelling with -ee- is Klein's: his 'go' entry (KLN:666, the page Nourai cites for the root) ends the Germanic list with 'Crimean Goth. geen, “to go”'. Watkins/AHD, whom Nourai names for this node, writes the same thing as 'Germanic variant form *gaian in Old English gān, to go: GO; AGO, FOREGO¹, FORGO'. Formally the verb is the ye-present *ǵʰh₁-yé-ti > Proto-Germanic *gāną (Wiktionary), a defective verb throughout its history (Old English suppletive past eode, replaced by went in the 15th c.).\",\n  \"derivation_fa\": \"«gee-n» صورت ژرمنی *gē-n / *gā-n «رفتن» است که در آلمانی علیای کهن gān / gēn و در آلمانی امروز gehen شده است؛ املای دو-e از کلاین آمده که در مدخل go می‌نویسد «Crimean Goth. geen». واتکینز (مأخذ مورد استناد نورایی) همین را *gaian می‌نویسد که در انگلیسی کهن gān شده است. از دید ساختاری، این فعل همان ستاک *ǵʰh₁-yé-ti است. ادعای نورایی درست است.\",\n  \"sources\": [W_GHEH1, E_GO],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"AHD_watkins1985.txt line 510: 'ghē-. To release, let go ... 1. Germanic variant form *gaian in Old English gān, to go: GO; AGO, FOREGO¹, FORGO.' Watkins's spelling of the Germanic form differs from Nourai's, but the claim (Germanic verb 'to go' from this root) is the same.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"s.v. go (KLN_1966.txt leaf 360 = p.665; KLN_1971.txt line 104081)\", \"stance\": \"supports\",\n     \"note\": \"'ME. gon, fr. OE. gan, rel. to OS., OFris., MLG. gan, Dan. gaa, Swed. gå, MDu. gaen, Du. gaan, OHG., MHG. gan, gen, G. gehen, Crimean Goth. geen, “to go”, fr. I.-E. base *ghe-, *ghei-.' — the source of the shape 'gee-n'.\"},\n    {\"src\": \"POK\", \"where\": \"IEW p.418-419\", \"stance\": \"supports\",\n     \"note\": \"Pokorny lists the Germanic 'go' verb (ahd. gān, gēn) under ǵhē- alongside Skt. jáhāti and Gk. κιχάνω; Bartholomae likewise adduces 'ahd. gān(?)' at the end of his zā- 'gehen' article.\"}\n  ]\n})\n\ne1[\"nodes\"].append({\n  \"id\": 3, \"lang\": \"English\", \"words\": \"go, ago, forego\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Old English gān 'to advance, walk; depart' > Middle English gon > go. 'Ago' is Middle English agon, the past participle of Old English āgān 'to pass away, go by' (ā- intensive prefix + gān), so 'three days ago' is literally 'three days gone by'; 'forego' is Old English foragān 'to go before' (fore- + gān) — to be kept apart from 'forgo' (Old English forgān 'to go without, abstain'), though the two have been confused since the 16th c. and Watkins lists both, FOREGO¹ and FORGO, under this root. All three items in the box are therefore correct.\",\n  \"derivation_fa\": \"انگلیسی کهن gān «رفتن» > انگلیسی میانه gon > go. واژهٔ ago از اسم مفعول agon (از انگلیسی کهن āgān «گذشتن») است، پس «three days ago» یعنی «سه روز گذشته»؛ forego از انگلیسی کهن foragān «پیشاپیش رفتن» است، که از سدهٔ شانزدهم با forgo «چشم پوشیدن» درآمیخته است. هر سه واژهٔ جعبه درست‌اند.\",\n  \"sources\": [E_GO],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference given for the English box; checked against Klein and Watkins below.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"s.v. go, ago (KLN_1971.txt line 104081 ff.)\", \"stance\": \"supports\",\n     \"note\": \"the 'go' entry ends 'Cp. ago' and gives the Germanic and IE background; Klein's separate 'ago' entry derives it from OE āgān.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ghē- (AHD_watkins1985.txt line 510)\", \"stance\": \"supports\",\n     \"note\": \"'in Old English gān, to go: GO; AGO, FOREGO¹, FORGO' — the same three English words as the chart.\"}\n  ]\n})\n\ne1[\"nodes\"].append({\n  \"id\": 4, \"lang\": \"Latin\", \"words\": \"hěrěs\", \"verdict\": \"plausible\",\n  \"derivation\": \"Latin hērēs, gen. hērēdis, means simply 'heir' (m., later also f.); the accusative herem in Naevius and French hoir presuppose *herem. The connection with this root is standard: hērēs is built on the zero/e-grade *ǵʰeh₁-ro- seen in Greek χῆρος 'bereft', χήρα 'widow', i.e. 'the bereaved one, the one left behind', with the second element usually taken as *-ed-. What is not standard is Nourai's gloss 'one who goes without parents, orphan': that is Watkins's cautious parenthesis — AHD 'Suffixed form *ghē-ro- in Latin hērēs, heir (? < “orphan” < “bereft”)' — turned into a definition. Ernout-Meillet stress that hērēs never meant 'orphan' in Latin ('le sens ancien du mot est bien “héritier”') and call the formation uncertain; Klein glosses it 'prob. a compound meaning “he who obtains that which is left”'. The arrow root → Latin is right; the gloss in the box is a hypothesis presented as a meaning.\",\n  \"derivation_fa\": \"لاتین hērēs (مضاف‌الیه hērēdis) تنها به معنای «وارث» است. پیوند آن با این ریشه پذیرفته است: ساخت *ǵʰeh₁-ro- که در یونانی χῆρος «محروم، بی‌کس» و χήρα «بیوه» دیده می‌شود، یعنی «برجامانده، واگذاشته‌شده». اما معنایی که نورایی در جعبه آورده («کسی که بی‌پدرومادر می‌شود، یتیم») در واقع حدس احتیاط‌آمیز واتکینز است که در پرانتز و با علامت پرسش آمده بود؛ ارنو‑مییه تأکید می‌کند که معنای کهن این واژه همان «وارث» بوده و ساخت آن قطعی نیست. پس پیکان درست است ولی معنای جعبه باید فرضیه خوانده شود.\",\n  \"sources\": [W_HERES, E_HEIR],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"partial\",\n     \"note\": \"AHD_watkins1985.txt line 510: '2. Suffixed form *ghē-ro- in Latin hērēs, heir (? < “orphan” < “bereft”): HEIR, HEREDITAMENT, HEREDITY, HERITAGE; INHERIT.' Watkins gives 'heir' as the meaning and marks 'orphan' with a question mark as a guess about the prehistory; Nourai has promoted the guess to the gloss.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. hērēs, p.530 (LAT.txt lines 27747-27780)\", \"stance\": \"partial\",\n     \"note\": \"'Malgré Festus qui enseigne que heres apud antiquos pro domino ponebatur ..., le sens ancien du mot est bien “héritier” ... il est naturel de rapprocher lat. hērēs de gr. χῆρος “dépouillé” ... Les hypothèses qui ont été proposées sur la formation de hērēs ... sont incertaines.'\"},\n    {\"src\": \"KLN\", \"where\": \"s.v. heir (KLN_1971.txt line 111474 ff.)\", \"stance\": \"partial\",\n     \"note\": \"'for L. heredem, acc. of heres, “heir”, prob. a compound meaning “he who obtains that which is left”. The first element of this compound derives fr. I.-E. base *ghe(i)-, “to lack, be empty; to yawn” ... The second element is *ed-.' Klein's paraphrase is not 'orphan' either.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"s.v. *zaH, IE cognates (CHEUNG.txt line 29789)\", \"stance\": \"supports\",\n     \"note\": \"'*IE COGNATES: ? Gr. κιχάνω ..., Gr. χῆρος “empty, bereft”, Lat. heres' — the Latin word is still reckoned to this root today.\"}\n  ]\n})\n\ne1[\"nodes\"].append({\n  \"id\": 5, \"lang\": \"English\", \"words\": \"heir, heredity, heritage, inherit\", \"verdict\": \"confirmed\",\n  \"derivation\": \"All four are Latin hērēs taken into English through French. 'Heir' is Middle English heir, from Anglo-French heir / Old French oir, from Vulgar Latin *herem for Latin hērēdem (acc. of hērēs), c. 1300. 'Heritage' is Old French heritage, from Late Latin hērēditāre 'to inherit'. 'Inherit' is Middle English enheriten, from Old French enheriter, from Late Latin inhereditare 'to appoint as heir'. 'Heredity' is a 1530s learned borrowing of French hérédité < Latin hērēditātem, and only acquired its biological sense in 1863 (Herbert Spencer). Watkins lists exactly this set (HEIR, HEREDITAMENT, HEREDITY, HERITAGE; INHERIT) under ghē-.\",\n  \"derivation_fa\": \"هر چهار واژه از لاتین hērēs و از راه فرانسه به انگلیسی راه یافته‌اند: heir از فرانسهٔ کهن oir / آنگلو‑فرانسه heir (سدهٔ ۱۴)؛ heritage از فرانسهٔ کهن heritage؛ inherit از فرانسهٔ کهن enheriter و لاتین متأخر inhereditare؛ heredity وام‌واژهٔ عالمانهٔ سدهٔ ۱۶ از فرانسه hérédité که معنای زیست‌شناختی آن از ۱۸۶۳ رواج یافت. واتکینز دقیقاً همین چهار واژه را ذیل ghē- می‌آورد؛ ادعای نورایی درست است.\",\n  \"sources\": [E_HEIR],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference on the English box; checked against Klein, Skeat, Watkins and Etymonline.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"s.v. heir (KLN_1971.txt line 111474)\", \"stance\": \"supports\",\n     \"note\": \"'heir, n. — ME., fr. OF. heir, eir (F. hoir), fr. VL. *herem (whence also OProvenç. er, “heir”), for L. heredem, acc. of heres, “heir”.'\"},\n    {\"src\": \"SKT\", \"where\": \"Skeat s.v. Heir / Heritage (SKT.txt lines 8538, 8620)\", \"stance\": \"supports\",\n     \"note\": \"'L. hereditare, to inherit. — L. hered-, crude form of heres, an heir. heritage. (F. – L.) O.F. heritage.' and 'Heritage: see Heir.'\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ghē- (AHD_watkins1985.txt line 510)\", \"stance\": \"supports\",\n     \"note\": \"'HEIR, HEREDITAMENT, HEREDITY, HERITAGE; INHERIT.'\"}\n  ]\n})\n\ndoc[\"entries\"].append(e1)\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-181.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\n"
}
```


### [2026-09-05T21:11:31.718Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build181.py (file state is current in your context — no need to Read it back)
```


## [2026-09-05T21:11:40.841Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 - <<'EOF'\nimport io\np='build181.py'\ns=io.open(p,encoding='utf-8').read()\ns=s.replace('ㆇ','ṯ')\nio.open(p,'w',encoding='utf-8').write(s)\nprint(s.count('ṯ'))\nEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build181.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-181.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 181",
 "description": "Build and validate page-181.json"
}
```


### [2026-09-05T21:11:43.657Z] TOOL RESULT

```
9
written
JSON OK
nodes verified: 11/11
node verdicts: {'disputed': 1, 'plausible': 3, 'confirmed': 7}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 6, 'not_checked': 4, 'partial': 3}
books consulted: {'contradicts': 3, 'silent': 4, 'supports': 22, 'partial': 3} | by book: {'KLN': 6, 'HRN': 3, 'SKT': 3, 'BRT': 2, 'WLD': 2, 'HUB': 2, 'CHEUNG': 2, 'POK': 2, 'AHD': 2, 'PHD': 1, 'KNT': 1, 'NYB': 1, 'MON': 1, 'BQT': 1, 'SOD': 1, 'HENNING': 1, 'LAT': 1}
```


## [2026-09-05T21:11:44.507Z] AGENT

You've hit your session limit · resets 7:40pm (America/Toronto)
