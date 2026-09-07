# Verification process log — verify-page-366


## [2026-09-07T19:29:17.895Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 366 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-366.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-366.json. Write /home/sfmqrb/git/rishe/data/verification/page-366.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 366` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T19:29:19.935Z] AGENT

I'll start by reading the instructions and the relevant files.


## [2026-09-07T19:29:20.702Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T19:29:20.717Z] TOOL RESULT

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


## [2026-09-07T19:29:21.249Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-366.txt"
}
```


### [2026-09-07T19:29:21.269Z] TOOL RESULT

```
1	=== PDF page 366 (book page 336) ===
2	--- entry 0 ---
3	ROOT [Sanskrit / Malaysian] Nîmbǔ, Limǔ : lemon, lime  (refs SKT:295; HJB:514)
4	#1 (parent #0) [Persian] refs=BQT:1922; MON:3671 | lîmǔ «لیمو» : lemon, lime
5	  #2 (parent #1) [Turkish] refs=None | limon
6	  #3 (parent #1) [Arabic] refs=None | lîmah
7	    #4 (parent #2) [French] refs=VOP:319 | limon, limonâd
8	      #5 (parent #4) [Persian] refs=VOP:319 | lîmonâd «لیموناد» : lemonade
9	      #6 (parent #4) [English] refs=KLN:878; AHD:748 | lemon, lemonade
10	    #7 (parent #3) [Spanish] refs=None | lima
11	      #8 (parent #7) [French] refs=None | 
12	        #9 (parent #8) [English] refs=KLN:890; AHD:758 | lime : a citrus fruit
13	          #10 (parent #9) [Persian] refs=VOP:314 | lâym «لایم» : a drink
14	--- entry 1 ---
15	ROOT [Indo-European] Nis : None  (refs KLN:1049)
16	#1 (parent #0) [Avestan / Old Persian] refs=KNT:193; KLN:1049; DZA:57 | niš, nij : away, off, out ; niš-bar : to carry out ☞Bher
17	#2 (parent #0) [Sanskrit] refs=AHD:889; KLN:1049 | nir-vanah : blowing out, extinction ☞Wě 1
18	  #3 (parent #2) [Persian] refs=MON:4882 | nîrvânâ «نیروانا» : extinction of soul by absorption into the Supreme Being
19	  #4 (parent #2) [English] refs=AHD:889 | Nirvana : extinction of soul by absorption into the Supreme Being
20	
```


## [2026-09-07T19:29:24.755Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-366.json",
 "description": "Read source JSON page 366"
}
```


### [2026-09-07T19:29:24.809Z] TOOL RESULT

```
{
  "pdf_page": 366,
  "book_page": 336,
  "entries": [
    {
      "root": {
        "name": "Nîmbǔ, Limǔ",
        "lang": "Sanskrit / Malaysian",
        "refs": "SKT:295; HJB:514",
        "gloss": "lemon, lime"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "BQT:1922; MON:3671",
          "words": [
            {"translit": "lîmǔ", "gloss": "lemon, lime", "script": "لیمو"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Turkish",
          "refs": null,
          "words": [
            {"translit": "limon", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Arabic",
          "refs": null,
          "words": [
            {"translit": "lîmah", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "French",
          "refs": "VOP:319",
          "words": [
            {"translit": "limon, limonâd", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "VOP:319",
          "words": [
            {"translit": "lîmonâd", "gloss": "lemonade", "script": "لیموناد"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 4,
          "lang": "English",
          "refs": "KLN:878; AHD:748",
          "words": [
            {"translit": "lemon, lemonade", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 3,
          "lang": "Spanish",
          "refs": null,
          "words": [
            {"translit": "lima", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "French",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": "KLN:890; AHD:758",
          "words": [
            {"translit": "lime", "gloss": "a citrus fruit", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Persian",
          "refs": "VOP:314",
          "words": [
            {"translit": "lâym", "gloss": "a drink", "script": "لایم"}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Nis",
        "lang": "Indo-European",
        "refs": "KLN:1049",
        "gloss": null
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "KNT:193; KLN:1049; DZA:57",
          "words": [
            {"translit": "niš, nij", "gloss": "away, off, out", "script": null},
            {"translit": "niš-bar", "gloss": "to carry out", "script": null, "see": ["Bher"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "AHD:889; KLN:1049",
          "words": [
            {"translit": "nir-vanah", "gloss": "blowing out, extinction", "script": null, "see": ["Wě 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:4882",
          "words": [
            {"translit": "nîrvânâ", "gloss": "extinction of soul by absorption into the Supreme Being", "script": "نیروانا"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "English",
          "refs": "AHD:889",
          "words": [
            {"translit": "Nirvana", "gloss": "extinction of soul by absorption into the Supreme Being", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-07T19:29:27.214Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['SKT','HJB','BQT','MON','VOP','KLN','AHD','KNT','DZA','POK','WLD','HRN','HUB','ARY','PHD','NYB','LKT','TTS','FSD','WEB','IEC','SYN','PLA','AFM','FVQ','DOZ','DEV','PHN']:\n    if k in d: print(k, json.dumps(d[k], ensure_ascii=False)[:600]); print()\n    else: print(k, 'MISSING'); print()\n\""
}
```


### [2026-09-07T19:29:28.486Z] TOOL RESULT

```
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt", "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.4

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook. Decoys: ketabnak 132354 (Zomorrodian), Google Books RwdkAAAAMAAJ (Nahid Shahidi 1997, no view). Purchase second-hand only."}

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\

DZA {"title": "M.T. Rashed Mohassel, Daramadi bar Dastur-e Zaban-e Avestai, Khajeh 1364/1985", "kind": "purchase", "url": "taaghche.com (revised edition ebook)", "lookup_hint": "Not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "RE-SEARCH 2026-09: the 1364 Khajeh edition is not digitised; a revised edition is sold as an ebook on Taaghche."}

POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 

TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt"], "page_offset": 

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou

DOZ {"title": "R. Dozy, Oosterlingen: Verklarende lijst der Nederlandsche woorden die uit het Arabisch, Hebreeuwsch, Chaldeeuwsch, Perzisch en Turksch afkomstig zijn, Leiden 1867", "edition_found": "1867", "kind": "archive_djvu", "url": "https://archive.org/details/oosterlingenver00dozygoog", "identifier": "oosterlingenver00dozygoog (also ...01dozygoog, ...02dozygoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DOZ.txt", "page_offset": "leaf = printed + 11..13 (e.g. leaf 15 = p.2, leaf 43 = p.32). local file has \\f between leaves (0-based leaf index i == i-th form-feed 

DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.

PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://ar
```


## [2026-09-07T19:29:36.803Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n '1,120p' data/verification/sources/SOURCE_MATRIX.md"
}
```


## [2026-09-07T19:29:36.815Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -40 && echo --- && sed -n '1,60p' tools/verify_check.py"
}
```


### [2026-09-07T19:29:36.867Z] TOOL RESULT

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


### [2026-09-07T19:29:36.884Z] TOOL RESULT

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
---
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
```


## [2026-09-07T19:29:48.664Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==315||NR==316' SKT.txt | grep -n -i -A6 -B2 'lemon\\|Limon' | head -60\necho \"=== SKT grep lemon ===\"\ngrep -n -i 'LEMON' SKT.txt | head -20"
}
```


## [2026-09-07T19:29:49.682Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i 'nimbu\\|LIME, ' HJB.txt | head -30\necho \"=== leaf search ===\"\ngrep -c $'\\f' HJB.txt"
}
```


### [2026-09-07T19:29:49.928Z] TOOL RESULT

```
=== SKT grep lemon ===
21824:Zest.    I F.  -  L.  -  Gk.)      Fonoerly  a  «Wp of  orange  or  lemon-peel,  used  for  fla' drinks ;  hence,  something  that  gives or  simply  a  reli»h.  — F.  ust,  'tneih whereby  the  kenicll  of  a  walnut  is Cot.;   hence,  a  slice  of  lemoupecL  ^ schisttu,   schistos,  Itt.   cleft,  divide'
```


### [2026-09-07T19:29:51.057Z] TOOL RESULT

```
4069:BBINJABBY,  s.  Also  BINJAB- BEE,  BUNJABBEE,  and  so  on.  But the  first  form  has  become  classical  from its  constant  occurrence  in  the  Indian Despatches  of  Sir  A.  Wellesley.  The word  is  properly  H.  bawdrdy  and Wilson  derives  it  from  Skt.  hamj, trade,'  kdra^  '  doer.'  It  is  possible  that the  form  bnnjdrd  may  have  been  sug- gested by  a  supposed  connection  witn the  Pers.  hiring,  *rice.'  (It  is  alleged in  the  Did,  of  Words  used  in  the  E, Indies^  2nd  ed.,  1806,  to  be  derived  from brinjy  *rice,'  and  aro,  'bring'!)  The Brinjanries  of  the  Deccan  are  dealers  in grain  and  salt,  who  move  about,  in numerous  parties  with  cattle,  carrying their  goods  to  different  markets,  and  who in  the  days  of  the  Deccan  wars  were  the great  resource  of  the  commissariat,  as they  followed  the  armies  with  supplies for  sale.  They  talk  a  kind  of  Manratta or  Hindi  patois.  Most  classes  of  Banjaras in  the  west  appear  to  have  a  tradition <)f  having  first  come  to  the  Deccan  with Moghul  camps  as  commissariat  carriers. In  a  pamphlet  called  Some  Account  of the  Bunjarrah  Class^  by  N.  R.  Cumber- lege,  District  Sup.  of  Police^  Bcueinj Berar  (Bombay,  1882  ;  [N(yrih  Indian N,  <fc  Q,  iv.  "163  Mqq.ji  the  author attempts  to  distin^ish  between  brinj- arees  as  *  grain-carriers,'  and  bunjarrahs, from  bunjdr,  *  waste  land'  ^meaning banjar  or  bdnjar).  But  this  seems fanciful.  In  the  N.-W.  Provinces  the name  is  also  in  use,  and  is  applied  to a  numerous  tribe  spread  along  the skirt  of  the  Himalaya  from  Hardwar to  Qorakhpur,  some  of  whom  are settled,  whilst  the  rest  move  about with  their  cattle,  sometimes  transport- ing goods  for  hire,  and  sometimes carrying  grain,  salt,  lime,  forest  pro- duce, or  other  merchandise  for  sale. rSee  Orooke,  Tribes  and  Castes,  i.  149  seqq.] vax^&r&S,  as  they  are  called  about Bombay,  used  to  come  down  from Bajputana  and    Central    India,    with
8155:with  lime,  and  generally with  a  terraced  plaster  root.
8921:1882.—"  I  learn  that  in  Bladraa  dallies  are restricted  to  a  single  gilded  orange  or  lime, or  a  tiny  sugar  pagoda,  and  Madras  offioers who  have  seen  the  bushels  of  fruit,  nuts, almonds,  sugar-candy^  .  .  .  ko,,  received  by single  officials  in  a  single  day  in  the  N.  W. Provinces,  and  in  addition  the  number  of bottles  of  brandy,  champagne,  liquors,  kc., received  along  with  all  the  preceding  in  the
12496:KHOA,  8.  Hind,  and  Beng.  hKod^ a  kind  of  concrete,  of  broken  brick^ lime,  &c.,  used  for  floors  and  terrace- roofs.
13188:not  an  AncAo- Indian  word.  But  it  has come  into  European  languages  through the  Ar.  Uvm&n^  and  is,  according  to Hehn,  of  Indian  origin.  In  Hind,  we have  both  llmH  and  nvnibU,  which  last, at  least,  seems  to  be  an  indigenous  form. The  Skt.  dictionaries  give  nimMha. In  England  we  get  the  word  through the  Romance  languages,  Fr.  Umon^  It. limone,  Sp.  limony  &c.,  perhaps  both from  the  Crusades  and  from  the  Moors of  Spain.  [Mr.  Skeat  writes:  "The Malay  form  is  limau,  *a  lime,  lemon, or  orange.'  The  Port,  limao  may possibly  come  from  this  Malay  form. I  feel  sure  that  limaUf  which  in  some dialects  is  limar^  is  an  indigenoiLS  word which  was  transferred  to  Europe.**] (See  LIME.)
13233:LIME,  8.  The  fruit  of  the  small Citrus  Tnedica,  var.  acida,  Hooker,  is that  generally  called  lime  in  India^ approachinfi;  as  it  does  very  nearly  to- tne  fruit  of  the  West  India  Lime.  It is  often  not  much  bigger  than  a pif;eon's  e£w;,  and  one  well-known mmiature  ume  of  this  kind  is  called by  the  natives  from  its  thm  skin Jcdghoun  nimbUy  or  *  paper  lime.'  This seems  to  bear  much  the  same  relation to  the  lemon  that  the  miniature  thin- skinned  orange,  which  in  London shops  is  called  Tangerine,  bears  to  the "China  orange."  But  lime  is  also used  with  the  characterising  adjective for  the  Citrtis  medico^  var.  LtmettOy Hooker,  or  Sweet  Lime,  an  insipid fruit.
13234:The  word  no  doubt  comes  from  the Sp.  and  Port,  lima,  which  is  from  the Ar.  liTna;  Fr.  lime,  Pers.  lim&,  limun (see  LEHON).  But  probably  it  came into  English  from  the  Portuguese  in India.  It  is  not  in  Minsheu  (2nd  ed. 1727).
16957:It  is  a  North  Indian  term,  and  is generally  used  for  the  combination  of betel,  areca-nut,  lime,  &c.,  which  is politely  offered  (along  ^vith  otto  of roses)  to  visitors,  and  which  intimates the  termination  of  the  visit.  This  is more    fully    termed    pawn-sooparie
17729:&c.,  s.  Citrus  decumanaj  L.,  the  largest of  the  orange-tribe.  It  is  the  same fruit  as  the  shaddock  of  the  West Indies ;  but  to  the  larger  varieties some  form  of  the  name  Poramelo seems  also  to  be  applied  in  the  West. A  small  variety,  with  a  fine  slcin,  is sold  in  London  shops  as  "the  For- bidden fruit."  The  fruit,  though frown  in  gardens  over  a  great  part  of ndia,  really  comes  to  perfection  only near  the  Equator,  and  especially  in Java,  whence  it  was  probably  brought to  the  continent.  For  it  is  called  in Bengal  Batdvi  nimbu  (i.e.  Citrus  Batn- viana).  It  probably  did  not  come  to India  till  the  17th  jjentury  ;  it  is  not mentioned  in  the  Am.  According  to Bretschneider  the  Pommelo  is  men- tioned in  the  ancient  Chinese  Book  of the  Shu-King.  Its  Chinese  name  is Yu.
18028:1727.— **  Fort  William  was  built  on  an irregular  Tetragon  of  Brick  and  Mortar, called  Puckah,  which  is  a  Composition  of Brick-dust,  lime,  Molasses,  and  cut  Hemp, and  when  it  comes  to  be  dry,  it  is  as  hard and  tougher  than  firm  Stone  or  Brick." — A,  Hamilton,  ii.  19 ;  [ed.  1744,  ii.  7].
20454:c.  1676.— "There  is  the  Serpent's  stone not  to  be  forgot,  about  the  oigness  of  a double  (doubloon  ?) ;  and  some  are  almost oval,  thick  in  the  middle  and  thin  about the  sides.  The  Indians  report  that  it  is bred  in  the  head  of  certain  Serpents.  But I  rather  take  it  to  be  a  story  of  the  Idoloter's Priests,  and  that  the  Stone  is  rather  a  com- position of  certain  Drugs.  ...  If  the  Person oit  be  not  much  wounded,  the  place  must be  incis'd ;  and  the  Stone  being  appli'd thereto,  will  not  fall  off  till  it  has  orawn all  the  poison  to  it :  To  cleanse  it  you  must steep  it  in  Womans-milk,  or  for  want  of that,  in  Cows-milk.  .  .  .  There  are  two ways  to  try  whether  the  Serpent-stone  be true  or  false.  The  first  is,  by  putting  the Stone  in  your  mouth,  for  there  it  will  give a  leap,  and  fix  to  the  Palate.  The  other  is by  putting  it  in  a  glass  full  of  water ;  for  if the  Stone  be  true,  the  water  will  fall  a boy  ling,  and  rise  in  little  bubbles.  .  .  ." — Tai>emter,  E.T.,  Pt.  ii.  155;  [ed.  Ball,  ii. 1521.  Tavernier  also  speaks  of  another snake-stone  alleged  to  be  found  behind the  hood  of  the  Cobra:  "This  Stone  being rubb'd  against  another  Stone,  yields  a  slime, which  being  drank  in  water,"  oc.  kc. — Ibid.
21533:As  re^rds  what  appears  to  be the  Indian  word,  Shakespear  gives : "  TdnJf^h  (in  QuzeratX  an  undercnround reservoir  for  water."  [And  so  Flatts.] Wilson  gives:  "Tdnken  or  tdibm, Mahr.  .  .  .  Tdnkh  (said  to  be  Ckuer- dthi).  A  reservoir  of  water,  an  arti* ficial  pond,  commonly  known  to Europeans  in  India  as  a  Tank. TdrHciy  Guz.  A  reservoir  of  water ; a  small  welL''  R  Drummond,  in  his lUustraJtions  of  GuzeraUee,  &C.,  gives: "TanJba  (Mah.)  and  Tankoo  (Gnz.) Reservoirs,  constructed  of  stone  or brick  or  lime,  of  larger  and  leaser size,  generally  inside  houses. .  .  .  They are  almost  entirely  covered  at  top, having  but  a  small  aperture  to  let a  pot  or  bucket  down.*  ..."  In  the towns  of  Bikaner,"  says  Tod,  *^mo6( families  have  large  cisterns  or  reser- voirs called  Tankasy  filled  by  the  rains^ (RajptUana^  ii.  202).  Again,  speakinig of  towns  in  the  desert  of  M^wir,  he says ;  "  they  collect  the  rain  water  in
25819:Lime,  5166 Limon,  514a Limpo,  limpoa,  5156 ling,  linga,  5176 Ling^adhari,   lingait,
=== leaf search ===
1054
```


## [2026-09-07T19:30:00.562Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('HJB.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\n# find leaf containing LEMON entry\nfor i,l in enumerate(leaves):\n    if 'come  into  European  languages  through' in l:\n        print('leaf',i)\n        print(l[:200].replace('\\n',' | '))\n        print('...')\n        idx=l.find('LEMON')\n        print(l[max(0,idx-400):idx+1500])\n        break\nEOF"
}
```


### [2026-09-07T19:30:01.821Z] TOOL RESULT

```
leaf 563
arch.  [Arch- deacon Gray  (China,  ii.  101)  gives  10 ft  as  the  equivalent  of  3i  English miles;  Gen.  Cunningham  (^rc^.  Rep. i.  305)  asserts  that  Hwen  Thsanff  con- verts the  Indian 
...
Letcfai,
Aux  fruits  moins  pourpres  que  ta  bouche." LeeonU  de  Lisle.
1878.—".  .  .  and  the  Uchi  hiding  under a  shell  of  ruddy  brown  its  globes  of  trans- lucent and  delicatelv  fragrant  flesh." — PA. Rolnnson,  In  My  Inaian  Oarden,  49.
1879.—".  .  .  Here  are  a  hundred  and sixty  lichi  fruits  for  you.  .  .  ."—if.  Stokes, Indian  Fairy  Tales  (Oalc.  ed.)  51.
LEMON,  s.  Ciirus  medico,  var. Limonum,  Hooker.    This  is  of  course
LEM0N-QRAS8.
514         LEWCHEW,  LIU  KIU.
not  an  AncAo- Indian  word.  But  it  has come  into  European  languages  through the  Ar.  Uvm&n^  and  is,  according  to Hehn,  of  Indian  origin.  In  Hind,  we have  both  llmH  and  nvnibU,  which  last, at  least,  seems  to  be  an  indigenous  form. The  Skt.  dictionaries  give  nimMha. In  England  we  get  the  word  through the  Romance  languages,  Fr.  Umon^  It. limone,  Sp.  limony  &c.,  perhaps  both from  the  Crusades  and  from  the  Moors of  Spain.  [Mr.  Skeat  writes:  "The Malay  form  is  limau,  *a  lime,  lemon, or  orange.'  The  Port,  limao  may possibly  come  from  this  Malay  form. I  feel  sure  that  limaUf  which  in  some dialects  is  limar^  is  an  indigenoiLS  word which  was  transferred  to  Europe.**] (See  LIME.)
c.  1200. — **Sunt  praeterea  aliae  arbores fructus  acidos,  pontic!  videlicet  saporis,  ex se  procreantes,  quos  appellant  limones." — Jacobi  de  Vitriaco,  aist,  Ih
```


## [2026-09-07T19:30:01.996Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i 'lemon' SKT.txt | head; echo \"=== try Limon/lime ===\"; grep -n -i '^Lime\\|Lime (\\|Limon' SKT.txt | head -20"
}
```


### [2026-09-07T19:30:02.065Z] TOOL RESULT

```
21824:Zest.    I F.  -  L.  -  Gk.)      Fonoerly  a  «Wp of  orange  or  lemon-peel,  used  for  fla' drinks ;  hence,  something  that  gives or  simply  a  reli»h.  — F.  ust,  'tneih whereby  the  kenicll  of  a  walnut  is Cot.;   hence,  a  slice  of  lemoupecL  ^ schisttu,   schistos,  Itt.   cleft,  divide'
=== try Limon/lime ===
10466:lime  (]].  the  linden  tree.  i.E.)  Limt\% a  corruption  of  lint,  as  in  Shak.  Temp.  v. 10:  and  tint  is  a  corraption  of  Und V  above) ;  tbe  lengthening  of  1  being  due  10 loss  of  d.
23772:Alimony,  mone>  allowed  for  a  \rlfc*fl support  upon  her  sepAratioo  from  hfli hustiand.     ^I,)     L.  aiimonia,  nnori»hment.
```


## [2026-09-07T19:30:07.297Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(len(leaves))\nfor i in (313,314,315,316,317):\n    print('--- leaf',i,'---')\n    print(leaves[i][:1400])\nEOF"
}
```


### [2026-09-07T19:30:08.598Z] TOOL RESULT

```
657
--- leaf 313 ---
ii)|  . glr>vc  without  fingers.
Mix.  to  mingle.  (E  ")     Pot  foi AT  for  asi.     A.  S.  mi^ttutt  to
MOHAIR.
ri;
Lsture
fT.  >
r  allied  to  it).  +
tcl.  measff,  Ktus.
i.-j.i.  l^miutri,  Gk.
t  Ski.   iwitrti.  mixed.
VMIK,  uiDGk.^V
D*r.  iwdjA,  q.  V.
I*  mtjc/w/is.»inixtare. •tinfrt,  to  rau  (above).
sec  H  ediuiD. t.
ttmonica,  the  science  of  aiiling  the |n^(>k-)  Gk.>t»T}^oKiKa,  mnemonics ; Ht  ot  fu^fi^ffiffui,  belonging  to  me- PIDlt-  ^an^^om't  crude  form  of /ivi^/Jtur. ^  «■  Gk.  >i>*ao/4cu,  I  remember.     (V
>%a.«b.  (E.)  M.  £.  mffw,  correspond- (kA.S.  OTi^i*,  Wickedness,  of  wbicii  ibe teike  seems  to  have  been  a  hurt  or Hcoce  was  formed  A.S.  mJtnan,  to X.  tment,  M.  E.  mcmn,  to  lament, obwlete.  its  place  being  supplied  by (tern  of  the  sb..  used  as  a  vb.  A.S. '  it  oe0Ctate  with  Icel.  mtm,  a  hart. D>a.  Mcrn,  defect,  blemish,  haan. It)  Der.  btmoan,  vb.,  substituted  for '  kmtnen,  A.  S,  ii  minnn.  to  bemoan. «t  (F,  -  Tent.)  M.  E.  moft  - O.  F. tDcnbankmCQt^dike.  [As  in  the  case ik.  th«  um«'  word  means  either  the hci!  '  c^  embankment  thrown
\\m  '     The  same  word  a*
«ff#,  \*v.Lr..  iump,  sodd,  turfe.  little iBit  lo  iboot  at ;'  Cotgrave.  Cf.  also mtUrn^  a  heap  of  earth,  aUo  a  hoUow, I  lUbc  E.  «Mtf/1.  Span  mota,  a  muuNd  ; hMcb  muff
--- leaf 314 ---
moi/ui.  a  measure. Model.  Moderate :  see  Mode. Modem,    Modeat,    Modicum ;    tec Mode. Modify,  Modulate ;  see  Moda, Mogul,  a  Mou^oli.m.  (Mongolia.)  Pers. Ah^hdl,  a  Mogul ;  another  form  of  Mtngot. Mohair,  cloth  of  tine  hatr.    ,F  »Aratx) A  sophisticated  spelling  (by  confusion  wi\K hair)  of  0.  F.  mcuhain,  meitdirc,  m*Klv% 1«
\
I
I
290
MOHAMMEDAN.
(F.  main).  •-  Arab,  mu^/tay/ar,  •  kind  of OOVK  camlet  or  hair-cloth.
moire,  watctnt  silk.  <F.  -  Arab)  Aa altered  form  of  mohair,  as«d  in  a  cbianged dense.
Mohammedan.  (Arab.)  A  follower oi  AfohaMmeii.^Krvih.  mnhammad,  praiirc- woithy. ^Aiub.  MamaJa,  he  piai&ed.
Mohur,  a  cold  coin.  (Pera.^  Pers.  mtiAr, mu/iur,agola  coin  worth  16  rupees  (^VlUon).
Moldore :  see  Monition.
Moiety ;  sec  Medium.
Moil,  10  toil,  drudge ;  see  HoUif^.
Moire ;  see  Mohair.
Moist :  see  Must  (3).
Molar,  used  for  grinding.  (L.)  L.  mih iaris,  adj..  from  mola,  a  mill.  Cf.  iMoUn, to  grind.     (VMAR,)
mill.  (L.)  M.  E.  miln,  myin,  multu; whence  miV/r,  muIU,  by  loss  of  n.  A.  S. tnyin,  my/^n.^L.  ma/itia,  a  miU^  extended from  me!a,  a  mill.
mullet(2),  afive-pointedstar.  (F.-L.) O.  F.  mctettt,  a  rowell.  whence  it  came  to mean  the  •  mullet '  of  heraldry ;  also  O.  F. moltttu,  '  a  mullet,  rowell  of  a  spur  ;  *  Cot. Dimio.  fr
--- leaf 315 ---
3 F.  monitiott.  —  L.  ace  maninfimem  - moui/us,  pp.  of  moHgre,  lo  adtiie,  Ul moke  to  think.     (VMAN.I
admoniah.  (F.-D  M.E.a«Mi so  that  adrjifinuk  is  a  corrupliflV  ' older  form  amortcst.  *  I  ■■wwlr  er  • Wyclif,  J  Cor.  iv.  I4.  ^  O.F.  •« (later  ii(/iMMJ/rr),  to  advise -Lo« mQHitvrit  arUrwanlB  ai^wnfmsaif.  Id
MONK.
advue.  *  L.  ai/.  to  ;  mtmtrt, admottu-ory  (from  pp.  ad'
bate.  (L.)  F(om  pp.  or  L. to  fthcw  fully, —L.  de,  down, B»T,  to  fthcw,  from  wnmsfruwi, te  raooAtor  ^bclow). ■  pUcDirhcTe  money  is  coined. mint,  mynt.  A.  S.  myntt, B  L.  m»n<ta^  (n  a  mint,  la) lf/«  WAS  a  sunume  of  Juno, pple  at  Kome  money  was \i.  aeue  ii  *  waniuig  one.'  — L. un.
, a  Portugese  gold  coin.  (Port. Bailey's  Diet.  —  Port  ttiocda Wore,  ^1  jj. ;  lit  '  mooey  of ftttta,  mooey:  de.  of;  aurum, y  ',l)elow). rtUting    to    money.    (L.)
lit.  belonging  to  a  mint.—
a  mint,  (j)  money.
■•  L.)    M .  E.  meneit. «-  O.  F.
maUy.^L. moneM*  (i)  mint, bc«  mint  (above).
a  pKKligy.  (K.  -  L)  F. I.  mfiHifrum,  a  divine  omen. bi£.  (Put  for  moH-^strum  ■}. I  to  wam.
Bt.  a  memonal.  (F.  -L.)  F. I..  maMumtntum,  a  memorial. |i6f  mcni-,  seen  in  mcni-t-us, hr.  to  advise,   remind ;    with
\Y.  —  L.)  M.  E.  mousfrt.  a n,  lit.  diiplay.  — O.  F.  mos/rf, of  motfitre,  '  a 
--- leaf 316 ---
,  G.  momif O.  H.  G.  m4Mfi,  LithuoQ.  m^nU^  Ck.  m^i^. Allied  to  Skt.  xwiird,  &  month.  Lit.  the 'measurer'  of  time.     (^MA.)
mond&y.  (£.)  M.  E.  moHtMday,  later moneday,  nionday.  A.  S.  niSnan  dag,  day of  the  moon ;  where  minan  is  the  gen.  of m6na^  moon.
month.  (E.)  M.E.mw«v/A,  later  ffw»/A. A.  S.  m6na^,  a  lunation ;  from  m^Ma,  monn. •f  Dn.  maand,  Icel.  rndnuSr,  Don.  maarud, Swed-  mdnad,  O,  mtmaf,  G.  menoths^  a month.  Allied  to  Lithuan.  mintxis^  Kqbs. miesiat^,  L.  mensisy  Irish  and  W.  mfV,  Gael. miW.    Gk.    /i^c,    Skt.    Maxa,     a    month.
cyMA.)
Moor  (i),  a  heath.  (E.)  M.  E.  mert. AS.  ffiJr.+IccL  f/K^r,  moor,  peat ;  O.  Du. moei\  moor,  mud ;  m^rlandt,  peaty  land ; Dan.  mor,  G.  0»wr.  Prob.  allied  to  Slira and  Blosa.
morass,  a  bog.  (Dn.)  Da.  macros, marsh,  fen ;  O.  Du.  motrasch^  adj.,  belong- ing to  a  moor,  from  the  sb.  motr,  moor, mud.  Cf,  G.  morast  \iox  mcrask  *),  Swed. moras,  Dan.  morads,  a  morass.  %  Distinct from  marsh.
Moor  (3),  to  fasten  up  a  ship;  sec  Har.
ICoor  (3),  a  native  of  N.  Africa.  (F.- L.-Gk.)  O.  F.  Afort,  'a  Moor;*  Cot.- L.  Maurus.  —  Gk,  yiavpat,  a  Moor.  Cf. Gk.  /jaC/wf,  d/uifpuf,  dark.  Der.  Mack-^- mocr,  corruption  of  blackmoor  (Minaheu), i.  e.  blcuk  Moor.
moroooo,  a  fine  kind  of  lea
--- leaf 317 ---
Morbid :  see  UorUl.
Mordacity,  sarcasm.  (F.  *  L)  ) used.  —  F.  mordasiti,  —  L.  sec.  OTfrilM from  mi^rdacHat^  ^wea  lo  bitt.*!*  •
0.»r
AlUei
rm  of  mfifi/ax,  biting.  ^L.
noathful.  small  piece.  (F. m*rsii.  —  O.  F.  morsel  (F. lUl.  m0ritiio.  Dimin.  from bite.  —  L.  mcrsHSt  pp.  of
f.  —  U)    O.  F.  rtmorsx  Cot. 9rtus,  rcraorse.  —  L.   rimor- •m^rdert,  to  bite  again,   to Kiue  (I). t«jr(i). I ;  see  Mom.
open  belmet.  (F.  —  Span.) Span,  morriffn  ;  cf.  Fan. \pn'M9t,  a  morion.  The  word ma f  accept  the  prob.  deri va- k  m»rra,  the  crown  of  the in.  morrf,  anything  roand; ck.  Perhaps  from  Basque heap  (Diex). (E.)  The  Marmonites  arr Joseph  Smiih,  who  in  1837 und  Uie  book  of  AUtintm. we  may  call  the  word  £., lish-spealttng  people,
M,E.  moru,  a  Northern or  M.  E.  mtfrnvn,  Ancrcn (■  S.  mvfTtm,  whence  monom ■fig*  of  r  to  w.<f  Da.  Dan.
urkti,  to  blink,  Gk.  /lap- W.  Orig.  Knse  prob.  'down.' B.  (Low  L.  —  G.)  Coined V  here  abort  for  m^rgengobe, t.  orig.  a  present  made  to  a ming  after  marriage,  esp.  if r  inferior  rank.  Hence  used K  marriage.
E.)    ^ort  for  mprtvtnins, ;  formed  from  M.  E,  m»f^ adding  the  substantival  (not s  -6^  (  -  A.  S.  -ung), £.)     M.  E.  tHoruH^  from  the
(above)t  by  lo&s  of M.  SL  mprvten  gave  rise  (1) looa  of  n :
```


## [2026-09-07T19:30:22.478Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\nfor i,l in enumerate(leaves):\n    if re.search(r'\\bLEM|\\bLIM|Lemon|limon|limun|Um[uo]n', l):\n        # print running heads\n        heads=re.findall(r'\\n([A-Z][A-Z\\-\\.\\, ]{3,30})\\.?\\n', l)\n        print(i, heads[:4])\nEOF"
}
```


### [2026-09-07T19:30:24.051Z] TOOL RESULT

```
267 ['LEGERDEMAIN.']
275 ['UMB.', 'LIMBECK.', 'LINE.']
642 ['SUPPLEMENT.']
```


## [2026-09-07T19:30:27.500Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (266,267,268,274,275,276):\n    print('=== leaf',i,'===')\n    print(leaves[i][:2200])\nEOF"
}
```


### [2026-09-07T19:30:28.830Z] TOOL RESULT

```
=== leaf 266 ===
r  or  e4 of  a  sail  at  the  sides.  ( Scand. \  led.  Hk leech-line  ;  Swcd.  //>.  Dan  icg.%  buU-ra] +0.  Du.  iyktn,  a  bolt-rope  \Sewd). Leek.  (E.)  ME.  tetk.  AS.  U^ Du.  iook,  Icel.  iaukr,  Dan.  /o^.  Swcd.  l G-  iauck.  Der.  gnr-Iu,  ihar-lock^  JUj lock  (latter  s>-llablc).  1
Leer,  a  sly  look.  (E.)    The  wb  il development  from  the  sb..  which  is  aa  \ word.     M.  E.  Ure,  the  cheek,  face,  cd plcxioo,  mien ;  usually  in  a  good  scnae.  \ Sltcltoa  has  it  in  a  bad  sense.     A.S.  A^ the  check  ;  hence,  the  face,  look,  mioL Iccl.  hlyr,    the  cheek.    ^Allied  to  ] loertn.   to  peqs,  peer,  which  is  ouite  i tinct    from    Da.    loertn,    to    lurL      \ Lower  (3). Leea,  dregs  of  wine.    (F  )     PI.  of  a form  Ue.  not  used.— F.  lu»  'the  l«ea» Low    U  lia,   pL   lim,   lees    (loi Origin  unknown. Left,  (he  weaker  hand.  (E") /;//.  Infi.     A.S.  lift.  Mr  Succt that    inanis,  /r/?,'  occurs  in  a  g1 Quelleu,  i.  445).  and  that  the has  senne  for  synni  ^sin'i;  so  that  M for  lyft^  with  the    sense   *  v •weak;'    cf.  A.S.  ly/i-dJl,    [ Fries.  Ueft,  ittfUr  hond,  lefi  hj:.'i ;   u lujt,  tuth.  left    ^.  The  fonn  of  llie  I is   LUB  ;   prob.  allied  to  ZiOp.      % allied  to  L.  lauus,  Gk-  \aiin, -Log,    (Scand.)     hX.  E.  Ay  fpL Icel.  l^r,  a  leg  r  Dan.  ta;^,  iive  ca' leg ;  Swcd.  la,^  (the  same). Legacy ;  see  LegaL. Legal,  pertaining  to  the  law. F.W.-L./;^.':-  '--'      »     '- lex.  Taw,  cognate st-nse  is  'that  w fixed ;  c/  Gk.  Kfrrai  fu^ot.  the  i from  «i>ai,  I  lie.     (V  I  AGH.>
allege    (F.-L.^    N^ -F.  cUU^uer,  'to  air lq;an,  to  send,  dispaiuu  ,    jt.i>o
:?f^
.sti Tbi
I
^L       LEGEND.
^Hwlon.  »  t»  ai^  (for  ad)t  to  ; "mtoid,  •ppoint,  from  iiqp^,  stem  of w.
\y,  s  doe  prevpottion  in  mixing  metoU. •  )  ?'ormcfiy  tiUity .  M  fc..  ajay.^ |4^,  d.'rj-.  .Ji'.ti^.  — U.  h-  auur,  Kiiiyir^ ^pc.  *  L.  a.V/tszrr,  to  biml  together ; (C  p.  349.  col  J.  1.  iS.  The  O.  K. t> .  became  aUi,  and  was  misuDder- ts  tictng  d  &i'*  L.  cu/  ttgtm,  accordi
=== leaf 267 ===
  sb.  (L.)  Low  L.  ccUetta.  a colU-ctioQ  in  money,  an  assemhly  for prayer,  heiioe  a  khurt  prayer;  see  the word  above.
oull.  to  collect,  select.  (F.-L.)  M.E. €ullem.^O.  F.  toillir,  ckillirt  to  collect; see  coil  ( I  ^  above.
diligent,  induhtriooa.  (F.— U)  O.  F. Ji/tgrnt.^L..  JiJiemf-,  stem  of  dUtgins, careful,  diligent,  lit.  loving  (fond) ;  pres. pt.  of  diligtre^  to  love,  select,  lit.  choose between.  —  L.  di-  ( >=  du-)^  apart :  Ugtrt.  to choose.
elect,  chosen.  (L.)  L.  elntuj,  pp.  of etigert,  to  choose  oot  —  L.  r,  out;  itgtrt, to  choose.
aleffant,  choice,  neaL  (F.-L.)  O.F. eleganl.'^l^  elegtutt-,  intern  o( i/^gans,  taste- ful, neac  — L.  r,  out;  Ug;  base  of  Ugtrt^ to  choose.
eUgible.  (F.-L.)  F.  tligibU.^how L.  eligibiJis,  fit  to  be  choiien.  — L.  tligtrt, to  choose  ;  !iee  elect  above.
Intolloot  (F-L.1  O.  F.  iff///&f/.- L.  infeiUctus,  perception,  discernment.  — L.  inUlUctus,  pp.  of  inUliigire^  to  dis- cern—L  intei-,  lor  inUr,  between  ;  U^re^ to  choose.
intelligence.  (F.-L.)    F.mfe//igenct,
—  L.  mtiiligtutia,  perception.  ■•  L.  ittUi' li^t-t  stem  of  pres.  pt.  of  inUUigtrt,  to discern,  onder>tand  \  above).
InteUlgiblo.   (F.-L.)     ^.tnumgiblt,
—  L.  inttliigihilu,  perceptible  to  the  sca*cs.
—  L,  intelUgtrty  to  discern  (above). lection,  a  reading,  portion  to  be  read.
(L.)  From  L.  Itftic^  a  rcadinj^.  — L.  Uttus, pp.  of  legtrt,  to  read.
lecture,  a  discourse.  (F-  -  L.)  F.  Uc- tvrt,  ft  reading. —  Low  L.  Uitura,  a  com- I  mcntary.  — L.  w/m/,  pp.  of  Ugf.rt.^  vo  n»d.
I I
I
I
I
LEGERDEMAIN.
legible,  readable.  (F.  -  L.)  O.  F.  k- gihU.  *  L,  itgi&Uis,  legible.  -  L.  kgtrt,  to read.
legion,  a  large  bodv  of  soldiers.  (F.  — h.)  M.  E.  IfgiouH.'^b.  F.  Up'tm.~h.  ie- gionem^  ace  of  k^a,  a  Roman  legion,  body of  from  4?oo  to  6aoo  men.  —  L.  iegert,  to gather,  select  a  band.
legume,  a  pod.  (F.  -  L.)  F.  U^^me, pulse,  a  pod.  vL.  U^men  {item  /e^f^nn^, pulse,  bean -plant;  applied  to  a  crop  that can  be  picked  (not  cut).  —  L.  /c/r/r,  to 
=== leaf 268 ===
 see  Lama.  But  the  word  may  be  Lapp; the  Lapp  name  is  hnmek.
IfOmoa.  ^F.  —  Pers.l  Formerly  itpum, «  F.  limoH. «  Pcrs.  limtJa,  limtimd,  a  Icinoi^ citron.
Lemur,  a  noctonial  animaL  (L.)  I* lemur,  n  ghost :  so  nicknamed  by  oaSorai-- isls  from  Its  nocturnal  habits.
Lend ;  see  Loan.
Length  ;  sec  Lone
Lenient,  mild.  (L.)  Frnra  pro.  pait<< of  L.  lenire,  to  soothe.  •»  L.  Umu,  softd mild.
lopity.  (L.)  Englished  from  LJbiiHq mildness.  — L.  lenis  (abovel.
relent.  (F.  -  L.)  Altered  from  F,  f» lentir,  to  slacken,  to  relent  (cf.  L.  rr/» tescert^  to  slacken).  — F.  «-,  pol  far  rr* (U  n-tuf) ;  L.  lentus^  sUck.  slow.  alM to  lenis,  gentle  labove).
XiOns,  a  uiccc  of  glass  tiMil  in (L.)     So  called  from  the  rciccnblani double-convex  lens  to  the  shape  of  thfri of  a  lentil. -•L.  lens^  a  lentU.
lentU.  a  plajit.  (F.-L.)  M.  E.  iMflK -O.  F.  lentiiU.  -  L.  lenticmlii^  a  little  Ic» til ;  double  dimin.  of  Itnti'^  crude  lomi irnt,  a  lentil.
Lent,  a  fast  of  40  days,  beginning Ash-Wedncsday.     (E.)      The    fast sprinij-ume ;  the  old  sense  is  simply y>\.K.ient,lenttn.    A.  S.  >Mr/^«, tKe  s; supposed  to  be  derived  from  iSsMf, because  in  sprii^  the  dajrs  lengthen  i is  possible.  4*  ^^-  It'^*,  sprisg;  C. O.  H.  G.  Itnsin,  Ungiun,      Der. adj.,  from  A.&  leueten,  sb.
Lentil :  see  Lena.
Lentiak,  the  masiiC'lTee.  (P.  ••  L.) lentisqui.  ~  L.  lentiscum^  Uniitemt^  osmill from  the  clamminess  of  ll^  resin. —  L. us,  sticky,  plianL    See  LenienV
Leo.  a  lion.  (L.  —  Ck.')     L.  U9.  « A^o/r,  a  lion.     We  also  tiiul  Du.  AvMit, Iffua^   Russ.  lev,  IJthaaa.  U9AS,  ivM lion.     Cf.  Heb.  Libi\  a  liort
loopard.  (K.-I.-Gk.^  O.F. ••L.  //^/on//fjr.  —  Gk.  Aioiri^>*«»,  a        _ supposed  to  be  a  moogrrl  brlwctn  a  fl (panther^   and  a  lioncsa.  —  Gk.  Jm»n  I \i«v,  a  lion;  m^i^lmt  a  pard
LEPER.
LEVITY.
(F.-L  -Ok  )    F.  /w«.  -  L.  &»-
of  *V» :  see  Leo  (above),
r,  (F,  -  U  -  Gk.)     The  sense  has
i;    Ufn   formerly   meaiil    ihe  di&-
tLf:  and  what  we  now
=== leaf 274 ===
.  lUgt, i.
I  aoubaaMdor;    fee Zrf»<iV ilcaaieDl. I«liant ;  tee  lioeua
LIGHT
«49
Iilflslong:  see  Iiiro.
Xiift  ( I ),  to  raise ;  see  I«oft..
Lift  (a),  to  steal.  (E.)  We  mak  of a  shop-ti/ttr,  a  thief;  see  Shak,  Troil.  i. i.  109.  Properly,  the  verb  should  be  liff. An  E^  word,  but  only  preserved  in  Gothic. Cf  Goth,  hiifan,  to  -itcal ;  hliftus,  a  thief. Cognate  with  L.  cUpen,  to  steal.     Golh.
Ji/tf/ujs=GV.  tcXiirnft,  a  thicf.
Ijigaznent.  a  band,  the  membrane  con- necting the  moveable  bones.  (F.  -•  L.) f.  ii^amtnt.'^X^  iigamcntum.  a  tie,   band.
—  L.  iiga-rt,  to  tie;  with  sufBx  'tntntum. Alligation,  a  rule  in  arithmetic.    (.L.)
From  L.  aJ/i^fio.  a  binding,  barid.«>L. a/7ripfj/us,  pp.  oi  a/ligurt.  to  bind;  tee  ally (below).
ally,  to  bind  together  (F.-L.)  M.E. aZ/Vrt.  — O.  F,  aiitr,  to  bind  up.  — L.  a/« (■a(b/i,  to;  iigart,  to  bind.  Der.  aiii- anc£,  M.  E.  ^iaaattt.
league  (i>,  a  bond,  alliance.  (F.-L.) F.  ligtu,  'a  league;*  Cot.  — Low  L.  lij^,  a league.  —  L.  ligare,  to  bind.
Uable,  rc^p-onsiMe.  (F.  —  L.)  Formeil, with  suffix  -0^//,  friim  F.  H-er^  lo  tie.  — L. hgart,  to  lie.
liotor,  an  officer  in  Rome.  (L.)  U tutor,  i.e.  'binder:*  either  from  the  fasces or  •bound'  rods  which  he  bore,  or  from binding  culprits.     Allied  to  Iigmn,ta  bind.
lien,  a  legal  claim,  charge  on  property. (F.  — L.>  F.  lien,  a  band,  or  tie.  anjtbirg that  fastens  or  fetters.  —  L.  Ugamtn,  1  tie.  •« L.  iij^arr,  to  tie.
ligattire,  a  bandage.  (F.  — L)  F.fi^- turg,  a  tic,  bandage.  ~  L.  Hgatura,  a  binding.
—  L.  li^us,  pp.  of  iigart,  to  tic. oblige,    to     constrain.     (F.  —  L.)        F.
oSiierr.  —  L.  o^-iifftrtt  to  bind  together, oblige.
rally  1 1),  to  re-assemble.  (F.-L.)  F. raiUtr.  —  F.  «-,  again :  idtitr,  to  ally ;  see ally  (alx>ve).
Idght  vO.  illnmination.  (E.)  M.  E. light,  -  A.  S.  U6ht,  light.  +  Du.  and  G. lifht,  Goth.  Uukath,  light.  The  /  is a  suffii ;  cf.  L.  tux  (stem  /!»-•)•  light. Gk.  X<v«-4^.   white,   Skt.   mch^   to  slu
=== leaf 275 ===
 Ktyvfuov,  a  sort  of  gem (aml>cr  or  jaciotbl ;  £xod.  xxviiL  ig.
liik*  (I),  simiUr.  (E)  M.  K.  lyJb.  /i>. A-  S.  //r,  commonly  ^-/ic.  +  Du.  gt'/ijk, ItmL  Wkr,  g^Ar,  Dan.  Ug,  Swcd.  liJt,  Goth,
UMB.
CD  iorai*'  aad  dcrivad ■K  acM^  ■■  form,  «^{x,'  ««. fora.  body,  IobL  ^  GMk.  AO. DiL  UJi^  «  oornae.  Dan.  Hf,  $w«d.  £1 corpse;  G.:^         "  V  G- tfi.
A.  S.  «»£&;  L.^  .   u%  like,  with  p><
#w  »««,  orcfk.
Uehgaia.  aduardiyanl called  becavee  a  onnw.  lia pcrtcd  uder  it.    The  U U.  E.  &i,  a  ooraee.  bat body ;  from  A.  S.  2£r,a  body ;
luw  {t\  to  be  pleued  with.  <£.> cawtroctioo  has  alteted;  M.  E. pleaaes.  is  impersonaL  as  w  mod.  E likt  =  if  it  may  please  yoa.  -  A.  S. to  please,  lit  to  be  like  or  svi^able  fofl A.  S.  /^.  ee-:ii,  like ;  sec  XJko  (tV  4*  I /Tyien,  to  init ;  Icel.  iiha,  to  Ukei  Go ^lioM.  to  please  (similaily  derived).       I
liken,  to  compare.  (Scaod.)  U. Hkntm,  to  liken  ;  bat  Uie  tnic transitive,  viz.  to  be  like.  — Swed. to  re>emble.  (1)  to  liken,  from Din.  it^Ht,  the  same,  from  Ug. Iiilac,  a  shrub.  (Span.  — Ti Span.  /t7d^.«-TuTk.  iftla^,  a  Ula£.2 Ul^\  liianj,  liiang,  of  which  the  pfO| sen-e  is  indigo*planL  Tne  tittiisl  /cUfl for  ff,  and  the  abore  form&  arc  frqin  a blue,  whence  nilak,  blnct»h.  The  pl| is  named  from  the  blucish  Cil^  «• Aowere  in  some  Tarietics. LUy.  a  planL  Cl-'Ok 't  A.&ldtf. L.  ///iWfli.—Ck.  h€ipiOr,  1  lily. Xiimb  (i).  a  member,  braitcb (E.)  M  K.lim.  A.S.  A'M.*f  t Dan.  Sued.  Um,
limber  u),  part  of  a consisting  of  two  wheels  and (Scand,>  Krom  prov.  E.  UmAoTt thilii  or  shalts,  the  b  being Further,  Umm-fr-t  \%  a  lionhU  plural ;. appears  by  the  dcrivaiJua.»loeL  Am| boughs,  branches  (hcoce.  shafts'!,  pL lim,  foliage,  closely  related  toAjNr.  alui Xilmb  (3),  the  edge  or  bonlei scKlJnl,  &c  (L.)  L.  Umlm4^ edging.  e<Igc.
Umbo,  limbus,  the  bonlen (L.)    The  orig.  phrase  is  i«  U Umbo  is  the  abl.  oi-e  *A  iimi>mt, the  limlnu  pcfri,  <■  -.y
on  the  border  of  !• .  (he
abode  tiU  Chnat
=== leaf 276 ===
an  rhell-l'ish.  (.F.-L) ^^/M/  ',Philhi»,  1706).  A.  S. «K^    %    Lkfflptey,   which  aUo
sticks  to  rodcs.^Low  L  hmprxda^  for L.  tampcdra,  a  lamprey.  See  Lamprey, a,  V.  Lambent.  Cf.  *  Lrmpt itia^  lem- pedu  ; '   Wright's  Vocab.  4^8.  17.
liimpld,  pure,  bright.  <F.  — L)  ^.Um- pide.  —  L.  Hmpidus.  clear.  Allied  to Lymph;  alsa  to  Gk.  Aa/iw/i^,  bright* Xii/nrfiK,  to  shine. Llnch  pin,  a  pin  to  fasten  a  wheel  00 an  axle.  (E. )  Formerly  iins-pin,  lit. 'axle-pin.*— A. S.  ^m/.?,  an  axle-trce.+Du. Itins,  a  linch-pin,  Low  G,  intui^  G.  iun^t^ a  linch-pin.
land.  Linden,  the  lime  tree.  (E.)  The true  form  of  ihc  fib.  ts  //W,  and  Itmi-en  is the  adj.  from  it.  Hence  Hndcn  irtt  *» /ind ;  the  same  thing.  M.  E.  //W.  A.  S. /;>it/,  the  tree  >  also  a  shield,  commonly  of thi«  wood.  The  wood  13  white,  smooth, and  easily  carved ;  we  may  therefore  con- nect it  with  G.  gtiind,  ^^t/indt,  smooth, Icel.  /inr,  smooth,  soft.  L.  Utttus.  pUant, A.  S.  //«/  ^for  iiMne*),  pUant.  +  Du.  i$Hdt, led.  Dan.  Swed.  Und.  it.  linde.
lime  (]].  the  linden  tree.  i.E.)  Limt\% a  corruption  of  lint,  as  in  Shak.  Temp.  v. 10:  and  tint  is  a  corraption  of  Und V  above) ;  tbe  lengthening  of  1  being  due  10 loss  of  d.
Line,  a  thread,  thin  cord ;  alao  a  itroke. row,  rank,  verse  (L. ;  or  F.  — L).  In  the bciise  '  cord.'  we  lind  A.  S.  Une^  directly from  L.  iinea.  In  the  other  senses,  it  is froDi  F.  ligtu,  also  from  L.  linta.  p.  The L.  lima  meant  orig.  a  string  made  of  Aax, being  fern,  of  adj.  liruuj,  made  of  tlax.* L.  limtm,  flax.  Cf.  Gk.  Kivw,  Aax.  Der. out  dine.
delineate.  (L.)  From  pp.  of  L. dtlineare,  to  sketch  in  outline.  —  L.  (/<, down  ;  Itmart,  to  mark  out,  from /iVwd^a  line.
lineago,  ^F.  — L.)  F.ii^^pr,  a  lineage. —  F.  ii^ntf  a  line,  rank,  —  L.  /md,  a  Ime tabove).
lineal.  (L)  L.  linealis,  belongirtg  to a  line.—  L.  Unea,  a  line.
lineament,  a  feature.  (F. -L.)  F, lintament.  Cot— L.  ItH^amtnium,  a  draw- ing, delineation.  — L.  /irteare,  to
```


## [2026-09-07T19:30:48.475Z] TOOL CALL #14: Bash

```json
{
 "command": "ls data/ && grep -rn \"SKT\" --include=*.md --include=*.json data/verification/sources/*.md 2>/dev/null | head; echo ---; grep -rln \"Skeat\" data/extracted/ | head"
}
```


### [2026-09-07T19:30:48.557Z] TOOL RESULT

```
ANOMALIES.md
extracted
EXTRACTION_SPEC.md
research
translations
verification
(eval):1: no matches found: --include=*.md
---
```


## [2026-09-07T19:30:49.907Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\nfor i in range(264,280):\n    nums=re.findall(r'\\b([23]\\d\\d)\\b', leaves[i])\n    print(i, nums[:6])\nEOF"
}
```


### [2026-09-07T19:30:51.360Z] TOOL RESULT

```
264 []
265 ['242']
266 ['349']
267 []
268 []
269 []
270 []
271 []
272 []
273 []
274 []
275 []
276 []
277 ['254']
278 ['255']
279 []
```


## [2026-09-07T19:31:00.650Z] TOOL CALL #16: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(len(d));print(sorted(d.keys()))\""
}
```


### [2026-09-07T19:31:01.953Z] TOOL RESULT

```
111
['AEF', 'AFA', 'AFM', 'AHD', 'AHM', 'AID', 'AIN', 'AKD', 'AKM', 'AMD', 'ARB', 'ARK', 'ARM', 'ARP', 'ARY', 'AVG', 'AWH', 'BLY', 'BQT', 'BRT', 'BST', 'CEL', 'DEV', 'DMO', 'DOZ', 'DRM', 'DVS', 'DZA', 'EAV', 'ETM', 'FAF', 'FFD', 'FIB', 'FNI', 'FRS', 'FSD', 'FSF', 'FVA', 'FVF', 'FVQ', 'FVS', 'FWE', 'GPL', 'HID', 'HJB', 'HRN', 'HUB', 'IEC', 'IRN', 'IRT', 'ISS', 'KAS', 'KFL', 'KGW', 'KLN', 'KNT', 'LAM', 'LAT', 'LEW', 'LKT', 'LST', 'MAG', 'MFL', 'MMF', 'MON', 'MPP', 'MZF', 'NAT', 'NFI', 'NYB', 'OEW', 'OXF', 'PEI', 'PHD', 'PHN', 'PLA', 'POK', 'PRT', 'RCH', 'ROE', 'SAP', 'SBK', 'SDQ', 'SHP', 'SIN', 'SKT', 'SLW', 'SNB', 'SNS', 'SOD', 'SOG', 'SOR', 'SPG', 'SYN', 'TAD', 'TLM', 'TTS', 'TYL', 'TZF', 'UNV', 'VDQ', 'VGH', 'VIE', 'VOP', 'VSF', 'WEB', 'WLD', 'ZAP', 'ZAW', 'ZFS', 'ZMA']
```


## [2026-09-07T19:31:12.943Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"lemonade\" KLN_1966.txt | head -5\necho \"=== lime ===\"\ngrep -n -i \"lime, n\\.\\|lime (fruit\\|lima, from Arabic\" KLN_1966.txt | head -5"
}
```


### [2026-09-07T19:31:13.008Z] TOOL RESULT

```
21453:Derivatives:  lemon,  adj.  and  tr.  v.,  lemonade (q.v.),  lemon-y,  adj.
21454:lemonade,  n.  —  F.  limonade,  fr.  limon,  ‘lemon’.
26462:orangeade,  n.,  a  drink  made  of  orange  juice, water  and  sugar.  —  F.,  formed  fr.  orange  on  the analogy  of  lemonade.  See  prec.  word  and  -ade. orangery,  n.,  a  place  where  orange  trees  are  cul¬ tivated.  —  F.  orangerie,  fr.  orange.  See  orange and  -ery.
=== lime ===
7925:clime, n.,  i)  a  region;  2)  climate.  —  L.  clima.  See climate.
```


## [2026-09-07T19:31:13.656Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"nirvana\\|nirvāṇa\\|nirvana,\" KLN_1966.txt | head -10; echo \"=== KLN 1971 ===\"; grep -n -i \"nirvana\" KLN_1971.txt | head -10"
}
```


### [2026-09-07T19:31:13.715Z] TOOL RESULT

```
25465:nippy,  adj.,  1)  nipping,  pinching;  2)  sharp;  3) quick,  active  (British  colloq.)  —  Formed  with adj.  suff.  -y  fr.  nip,  ‘to  pinch’, nirvana,  n.,  extinction  of  the  individual  soul  by absorption  into  the  supreme  spirit  (Hinduism) —  OI.  nirvanah,  lit.  ‘a  blowing  out  (of  a  light), extinction,  disappearance’,  which  is  formed  fr. nis-,  nir-,  ‘out,  forth,  away’  (which  is  rel.  to Avestic  nish-,  of  s.m.,  and  prob.  cogn.  with OSlav.  nisti,  ‘poor’),  and  vati,  ‘it  blows’,  for whose  etymology  see  wind,  n.
=== KLN 1971 ===
161825:nirvana, n., extinction of the individual soul by 
267393:bedeguar, nirvana, Vayu, vent, ‘outlet’, ventail,
```


## [2026-09-07T19:31:19.565Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ndef ctx(n):\n    for i in range(n-1, max(0,n-400), -1):\n        m=re.search(r'^\\s*(\\d{3,4})\\s*$', lines[i])\n        if m: return i+1, m.group(1)\n    return None\nfor n in (21453, 21454, 25465):\n    print(n, ctx(n))\n# also find page markers near\nEOF"
}
```


### [2026-09-07T19:31:20.865Z] TOOL RESULT

```
21453 (21444, '878')
21454 (21444, '878')
25465 (25394, '1046')
```


## [2026-09-07T19:31:26.160Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '21440,21460p' KLN_1966.txt\necho \"==== nirvana region ====\"\nsed -n '25390,25400p' KLN_1966.txt\necho \"...\"\ngrep -n '^\\s*10[45][0-9]\\s*$' KLN_1966.txt | sed -n '1,20p'"
}
```


### [2026-09-07T19:31:27.403Z] TOOL RESULT

```
leitneriaceous,  adj.  —  See  prec.  word  and  -aceous. lekane,  n.,  a  large  dish  or  bowl  ( Greek  antiq.)  — Gk.  XocotvT),  ‘dish,  pot,  pan’,  fr.  Xsxoc,  of  s.m. prob.  meaning  lit.  ‘something  bent’,  and  cogn. with  L.  lanx,  gen.  lands,  ‘plate,  dish;  scale  of weighing  machine’.  See  balance  and  cp.  words there  referred  to.
Lelia,  fern.  PN.  —  L.  Laelia,  fern,  of Laelius,  name of  a  Roman  gens.
leman,  n.,  sweetheart;  usually  in  the  sense  of  par¬ amour.  —  ME.  leofman,  lefman,  lemman,  fr. OE.  leof,  ‘dear’,  and  man,  ‘man’.  See  lief  and man.
lemma,  n.,  an  assumption  taken  for  granted.  — L.,  fr.  Gk.  Xr)jjL|ia,  ‘something  received;  some¬ thing  taken  for  granted,  assumption,  premise’, rel.  to  e{-Xv][J.^at,  perf.  pass,  of  XajxSavoj,  ‘I take,  grasp,  seize;  I  receive’,  which  derives  partly fr.  I.-E.  base  *(s)lagK-,  'to  take,  seize',  whence also  Xi^oizai  (for  *Xay-io;iii  or  *Xav-|-ionat), ‘I  take,  grasp,  (see  latch),  and  partly  fr.  base *labh-,  ‘to  take,  seize’,  whence  Gk.  X&pupov, ‘spoil,  prey’,  ap.<pi-Xa<pif]<;,  ‘wide-spreading  (lit. ‘taking  in  on  both  sides’),  OI.  Idbhate,  lambhate, rdbhate,  ‘seizes’,  Lith.  Idbis,  ‘possession,  riches’, labas,  ‘good’.  Cp.  analemma, dilemma,  trilemma, afitmlahe.  cataleusv.  enllepsy,  narcolepsy,  nym-
878
pholepsy,  prolepsis,  syllable.  For  base  *rabh-,  as a  probable  secondary  form  of  base  *labh~,  see rabid.  For  the  ending  of  lemma  see  suff.  -ma. lemming,  n.,  a  small,  ratlike  animal.  —  Norw.,  fr. Lapp,  luomek.
Lemna,  n.,  a  genus  of  plants,  the  duckweed  (bot.)
_  ModL.,  fr.  Gk.  X£|xva,  ‘a  kind  of  marsh
plant’.
Lemnaceae,  n.  pi.,  the  duckweed  family  (bot.)  — Formed  fr.  Lemna  with  suff.  -aceae. lemnaceous,  adj.  —  See  prec.  word  and  -aceous. lemniscate,  n.  (geom.)  —  Late  L.  lemniscatus, ‘adorned  with  ribbons’,  fr.  lemniscus,  ‘ribbon’, fr.  Gk.  Xr^vtaxo?,  of  s.m.  See  next  word  and adj.  suff.  -ate.
Derivative:  lemniscat-ic,  adj. lemniscus,  n.,  1)  the  form  -  used  in  annotations;
2)  a  band  of  fibers  (anal.)  —  Late  L.  lemniscus, fr.  Gk.  Xrjixvioxo?,  ‘ribbon’,  which  is  prob.  rel. to  Ayjpvo?,  ‘Lemnos’  (name  of  an  island  in  the Aegean  Sea),  hence  orig.  meant  ‘of  Lemnos’. Cp.  lemniscate.
lemon,  n.  —  ME.  lymon,  fr.  MF.  (=  F.)  limon,  fr. Turk,  limon,  fr.  Pers.  limun,  ‘limon,  citron’.  Cp. lime,  ‘a  fruit’,  limonene.
Derivatives:  lemon,  adj.  and  tr.  v.,  lemonade (q.v.),  lemon-y,  adj.
lemonade,  n.  —  F.  limonade,  fr.  limon,  ‘lemon’.
See  prec.  word  and  -ade. lemur,  n.,  any  of  a  group  of  nocturnal  mammals related  to  the  monkeys.  —  ModL.,  fr.  L.  lemu¬ res,  ‘spirits  of  the  dead,  ghosts,  specters’,  cogn. with  Gk.  Xocfiupo?,  ‘voracious,  gluttonous’,  Aa- [xia,  ‘spirits  of  the  dead,  ghosts,  specters’.  Sec lamia  and  cp.  words  there  referred  to.  The  ani¬ mal  was  called  lemur  in  allusion  to  its  nocturnal habits.
lemures,  n.  pi.,  the  spirits  of  the  dead  ( Roman  re¬ ligion).  —  L.  lemures.  See  prec.  word, lemuroid,  adj.,  resembling,  or  pertaining  to,  the lemurs  or  the  Lemuroidea.  —  A  hybrid  coined fr.  lemur  and  Gk.  -oetSrjc,  ‘like ,  fr.  elSo^, ‘form,  shape’.  See  -oid.
Lemuroidea,  n.  pi.,  a  suborder  of  Primates,  the lemur  (zool.)  —  ModL.  See  prec.  word.
Lena,  fem.  PN.  —  Shortened  fr.  Helena  or  Mag¬ dalena.
lend,  tr.  and  intr.  v.  —  ME.  lenen,  fr.  OE.  Henan, ‘to  lend,  grant’,  fr.  lien,  ‘loan’,  rel.  to  Du. lenen,  OHG.  lehanon,  MHG.  lehenen,  G.  lehnen, ‘to  lend’.  See  loan.
Derivative :  lend-er,  n.
==== nirvana region ====
Derivatives:  nicotin-ean,  nicotin-ed,  nicotin-ian, nicotin-ic,  adjs.,  nicotin-ism,  n.,  nicotin-ize,  tr.  v. nictate,  to  nictitate.  —  L.  nictatus,  pp.  of  L.
nictare,  ‘to  wink,  blink’.  See  next  word, nictitate,  intr.  v.,  to  wink.  —  ML.  nictitatus,  pp. of  nictitare,  freq.  of  L.  nictare,  ‘to  wink,  blink’, fr.  nicere,  ‘to  beckon’,  fr.  I.-E.  base  *kneig"h-, ‘to  bend’,  whence  also  L.  *nivere  in  conivere,  ‘to close  the  eyes,  blink,  wink  at,  overlook  (errors), connive  at’.  See  connive  and  verbal  suff.  -ate  and cp.  words  there  referred  to.
Derivative:  nictitat-ion,  n. nidal,  adj.,  pertaining  to  a  nidus.  —  See  nidus  and adj.  suff.  -al.
nidamental
1046
nidamental,  adj.,  pertaining  to  a  covering  for  an egg  or  eggs  ( zool .)  —  Formed  with  adj.  su ft',  -al fr.  L.  nidamentum,  ‘materials  for  a  nest,  nest’,  fr. nidus,  ‘nest’.  See  nidus.
niddering,  adj.,  base,  cowardly;  n.,  a  coward.  — An  erroneous  form  standing  for  ME.  nithing, ‘infamous  person,  coward’ ;  used  by  the  Scottish novelist  and  poet  Sir  Walter  Scott  (1771-1832).
See  nithing.
nide,  n.,  a  nest;  specif.,  a  brood  of  pheasants.  — L.  nidus  (whence  also  F.  nid),  ‘nest’.  See  nidus, nidificate,  intr.  v.,  to  build  a  nest,  to  nidify.  —  L. nidified  I  (-urn),  pp.  stem  of  nidificare,  ‘to  build  a nest’,  compounded  of  nidus ,  ‘nest’,  and  -fiedre, fr.  facere,  ‘to  make,  do’.  See  nidus,  and  -ficate. nidification,  n.  —  ML.  nidificatio,  gen.  -dnis,  fr. L.  nidificatus,  pp.  of  nidificare.  See  prec.  word and  -ion.
nidify,  intr.  v.,  to  make  a  nest,  to  nidificate.  —  F.
nidifier ,  fr.  L.  nidificare.  See  nidificate, nid-nod,  intr.  v.,  to  nod  repeatedly.  —  Antiphonic reduplication  of  nod.
...
25234:1040
25394:1046
25568:1054
25634:1056
25635:1057
25668:1058
25669:1059
32788:1044
39957:1043
40007:1040
```


## [2026-09-07T19:31:36.276Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"limon,  citron\\|Sp\\.  lima\\|lima,  ‘lime\" KLN_1966.txt | head\necho \"=== search lime entries ===\"\ngrep -n \"^lime\\|  lime,\" KLN_1966.txt | sed -n '1,15p'"
}
```


### [2026-09-07T19:31:36.377Z] TOOL RESULT

```
21452:lemon,  n.  —  ME.  lymon,  fr.  MF.  (=  F.)  limon,  fr. Turk,  limon,  fr.  Pers.  limun,  ‘limon,  citron’.  Cp. lime,  ‘a  fruit’,  limonene.
21760:Derivative:  lime ,  tr.  v.,  1)  to  smear  with  bird¬ lime  ;  2)  to  mix  with  lime, lime,  n.,  a  fruit  allied  to  lemon.  —  F.,  fr.  Proven?. limo,  fr.  Arab,  lima1'  (whence  also  Sp.  lima), noun  of  unity,  formed  from  the  collective  noun lim,  which  derives  fr.  Pers.  limun.  See  lemon  and cp.  limonene.
=== search lime entries ===
6139:calcareous,  adj.,  pertaining  to,  or  containing, lime  or  calcium.  —  L.  ealedrius,  ‘pertaining  to lime’,  fr.  calx,  gen.  calcis,  ‘limestone,  lime, pebble’,  a  loan  word  fr.  Gk.  yi/.'A,  ‘small  stone, pebble’,  which  prob.  derives  fr.  I.-E.  *(s)q(h)e- liq-,  enlargement  of  base  *(s)qel-,  ‘to  cut,  cleave, split’.  See  colter  and  cp.  silica.  Cp.  also  calcine, calculate,  calculus,  calx,  cauk,  causeway,  causey, chalk,  chaussee. —  The  right  spelling  of  the  word would  be  catcarious  (a  form  now  obsolete),  the English  correspondence  of  L.  -arius  being -arious  (or  -ary).
20090:lime’,  which  is  compounded  of  Vqbq,  ‘mistletoe; birdlime’,  and  -o')Sr,-,  ‘like’.  See  Ixia,  -ode,  ‘like’, and  -idae.
21696:‘pale’,OPruss.  /ou.w«(pl.)‘stars’,W.  Hug,  ‘gleam, glimmer’,  OIr.  luach,  ‘white’,  loche,  ‘lightning’, luchair ,  ‘brightness,  luster’,  Mir.  luan.  Ion, ‘moon’,  Toch.  A  luk-,  ‘to  shine’,  A  lok,  B  lauke ‘far  away’,  Hitt,  lukezi,  lukzi,  ‘is  bright’.  Base *leuq-,  ‘to  be  light,  to  shine’,  is  identical  with base  *leuq-,  ‘to  see,  behold’,  whence  OI.  Ideate, lokate,  ‘sees,  perceives’,  locayati,  lokayati,  ‘re¬ gards,  looks  at’,  Toch.  A  Idk-,  B  lyk-,  to  see , Gk.  Xeiloceiv  (for  *Xsu>u£iv),  ‘to  look  at,  see’, W.  am-lwg,  ‘conspicuous’,  Lith.  laukti,  ‘to  wait’. Cp.  lea,  ‘a  track  of  open  country’,  leuco-,  levin, link,  ‘torch’,  loka, low, ‘blaze’,  luce,  lucent, lucid, Lucifer,  Lucius,  lucubrate,  luculent,  lucule,  lucus a  non  lucendo,  lucem,  Lucy,  luminous,  lunar, lunation,  lime,  luster,  ‘gloss’,  lustrum,  lux,  Luzu- la,  Lychnis,  lynx.
21750:Limax,  n.,  the  genus  containing  the  slugs  (zool.) —  L.  Umax,  gen.  -acis,  ‘slug,  snail’,  fr.  Gk.  Xsi- ptot5,  which  is  cogn.  with  Russ,  slimak,  ‘snail’,  lit. ‘the  slimy  animal’,  OPruss.  slayx,  Lith.  sliekas, Lett,  slieka,  ‘earthworm’,  OE.  slaw-wyrm,  ‘slow- worm’  (see  slowworm).  All  these  words  are  deriv¬ atives  of  I.-E.  base  *(s)lei-,  ‘slimy’,  whence also  OE.  sliw,  ‘tench’,  slim,  ‘mud’.  See  slime and  cp.  lime,  ‘birdlime’.
21760:Derivative:  lime ,  tr.  v.,  1)  to  smear  with  bird¬ lime  ;  2)  to  mix  with  lime, lime,  n.,  a  fruit  allied  to  lemon.  —  F.,  fr.  Proven?. limo,  fr.  Arab,  lima1'  (whence  also  Sp.  lima), noun  of  unity,  formed  from  the  collective  noun lim,  which  derives  fr.  Pers.  limun.  See  lemon  and cp.  limonene.
21761:lime,  n.,  the  linden  tree.  —  Fr.  earlier  line,  fr.  lind\ see  linden.  The  change  of  line  to  lime  prob.  oc¬ curred  first  in  compounds  whose  second  element began  with  a  labial  (as  in  line-bark,  line-bast, etc.)
21762:limehouse,  n.,  defamation  of  one  s  political  op¬ ponents.  —  Named  after  the  borough  Lime- house,  near  London,  where  David  Lloyd  George (1863-1944)  delivered  a  speech  July  30,  1909. limejuicer,  n.  (slang),  1)  a  British  ship;  2)  an  Eng¬ lish  sailor;  3)  an  Englishman.  —  Formed  fr. lime,  the  fruit,  juice,  and  suff.  -er ;  so  called  from the  limejuice  served  on  British  ships  to  prevent scurvy.
21766:Limerick,  n.,  a  nonsense  verse  of  five  lines,  usu¬ ally  rhyming  aabba.  —  So  called  after  the  Irish place  name  Limerick,  which  is  mentioned  in  the refrain  of  a  similar  verse.  (The  refrain  runs: “  Will  you  come  up  to  LimerickT’) limes,  n.,  boundary.  —  L.  limes.  See  limit, lime  tree,  the  linden  tree.  —  See  lime,  ‘the  linden tree’.
21767:limey,  n.  (slang),  1)  an  English  sailor;  2)  an Englishman.  —  Shortened  fr.  limejuicer.  For  the ending  see  adj.  suff.  -y.
21782:limno-,  before  a  vowel  limn-,  combining  form meaning  ‘marsh,  marshy  lake’.  —  Gk.  Xtjrvo-, Xifrv-,  fr.  Xtu.v7],  ‘marsh,  pool,  lake’,  which  is rel.  to  Xi[xr)V,  ‘harbor,  haven’,  Xetjacov,  ‘a  moist, grassy  meadow’,  and  prob.  cogn.  with  L.  limus, ‘slime,  mud,  mire’.  See  slime  and  words  there  re¬ ferred  to  and  cp.  esp.  lime,  ‘birdlime’.  Cp.  also limnetic,  limonite,  Limonium,  Lymnaea,  and  the first  element  in  Limicolae  and  in  Limosella.
21786:limonene,  n.,  a  terpene  of  lemonlike  odor  (chem.) —  Formed  with  suff.  -ene  fr.  ModL.  limonum, ‘lemon’,  fr.  F.  limon.  See  lemon  and  cp.  lime,  ‘a fruit’.
21800:limy,  adj.  —  Formed  with  adj.  suff.  -y  fr.  lime, ‘birdlime’.
21805:linchpin,  n.,  a  pin  passing  through  the  end  of  an axletree.  —  Fr.  earlier  linspin,  lit.  ‘axle  pin'.  The first  element  of  this  compound  derives  fr.  OE. lynis,  ‘axletree’,  which  is  rel.  to  OS.  lunisa,  MLG. lunse  (whence  G.  Liinse),  MDu.  lunse.  Ions (whence  Du.  luns ),  ‘axletree’,  and  cogn.  with OI.  anil}  (for  *olni),  ‘part  of  the  leg  above  the knee’ ;  see  ell.  For  the  second  element  see  pin. linctus,  n.,  asirupy  medicine.  —  L.  linctus,  ‘a  lick¬ ing’,  fr.  linctus,  pp.  of  lingere,  ‘to  lick’.  See  lick, lindackerite,  n.,  a  complex  nickel  copper  arsenate (mineral.)  —  G.  Lindackerit,  named  after  the 19th-cent.  Austrian  chemist  Joseph  Lindacker, who  analyzed  it.  The  ending  -it  goes  back  to Gk.  -itijc;  see  subst.  suff.  -ite. linden,  n.,  the  lime  tree.  —  Prop,  subst.  use  of  the obsol.  adjective  linden,  ‘of  linden  wood’,  fr.  ob- sol.  lind,  ‘linden  tree’,  fr.  OE.  lind,  which  is  rel. to  OS.  Undo,  lindia,  ON.  lind,  OHG.  linta, MHG.,  G.  linde,  ‘the  lime  tree’.  These  words prob.  mean  lit.  ‘the  tree  with  pliant  bast’,  and derive  fr.  I.-E.  base  *lent-,  ‘flexible’,  whence  also dial.  Russ,  lut,  ‘lindenbast’,  Russ  lutijo,  ‘a  forest of  lime  trees’,  Pol.  Jet,  ‘switch,  twig  ,  Lith.  lento, ‘board,  plank’,  L.  lentus,  ‘flexible’,  OE.  tide, ‘soft,  mild,  gentle’.  See  lentitude  and  cp.  the second  element  in  Ethelinda.  Cp.  also  lime, ‘linden’.
21838:linguo-,  combining  form  meaning  lingual,  lin- guatiy.  —  Fr.  L.  lingua,  ‘tongue’.  See  lingual, liniment,  n.,  an  oily  liquid  for  applying  to  the skin.  —  ME.  lynyment,  fr.  Late  L.  linimentum,  fr. L.  linire,  a  secondary  form  of  lincre,  ‘to  daub, besmear,  anoint’,  which  stands  for  *ti-nere  and is  cogn.  with  OI.  linati,  layate,  llyate,  tiyati, ‘adheres  to;  slips  into;  disappears’,  Gk.  aXi- velv,  ‘to  anoint,  besmear’,  OIr.  as-leinamm, ‘I  soil’,  leinam,  ‘I  follow’  (lit.  ‘I  stick  to’);  fr. I.-E.  base  *(s)lei-,  ‘slime,  slimy,  sticky’,  whence also  OE.  slim,  ‘sUme’.  See  slime  and  -ment  and cp.  lime,  ‘birdlime’.  Cp.  also  delete.  The  change
21998:lemo,  Du.  leem,  OHG.  leimo ,  MHG.  leime, leim,  G.  Lehm,  ‘loam’,  and  to  OE.  Urn,  ‘lime’. See  lime,  ‘birdlime’,  and  cp.  words  there  referred to.
```


## [2026-09-07T19:31:47.469Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor n in (21760, 25465):\n    for i in range(n-1, max(0,n-300), -1):\n        m=re.search(r'^\\s*(\\d{3,4})\\s*$', lines[i])\n        if m:\n            print(n, 'prev marker', m.group(1), 'at line', i+1); break\n    for i in range(n, min(len(lines), n+300)):\n        m=re.search(r'^\\s*(\\d{3,4})\\s*$', lines[i])\n        if m:\n            print(n, 'next marker', m.group(1), 'at line', i+1); break\nEOF"
}
```


### [2026-09-07T19:31:48.748Z] TOOL RESULT

```
21760 prev marker 890 at line 21753
21760 next marker 891 at line 21764
25465 prev marker 1046 at line 25394
25465 next marker 1054 at line 25568
```


## [2026-09-07T19:31:56.079Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^nis-\\|nis-,  pref\\|nir-,  pref\\|Avestic  nish\\|Avestic  nis\" KLN_1966.txt | head\necho \"=== between markers listing headwords ===\"\nsed -n '25455,25475p' KLN_1966.txt | cut -c1-120"
}
```


### [2026-09-07T19:31:56.149Z] TOOL RESULT

```
25465:nippy,  adj.,  1)  nipping,  pinching;  2)  sharp;  3) quick,  active  (British  colloq.)  —  Formed  with adj.  suff.  -y  fr.  nip,  ‘to  pinch’, nirvana,  n.,  extinction  of  the  individual  soul  by absorption  into  the  supreme  spirit  (Hinduism) —  OI.  nirvanah,  lit.  ‘a  blowing  out  (of  a  light), extinction,  disappearance’,  which  is  formed  fr. nis-,  nir-,  ‘out,  forth,  away’  (which  is  rel.  to Avestic  nish-,  of  s.m.,  and  prob.  cogn.  with OSlav.  nisti,  ‘poor’),  and  vati,  ‘it  blows’,  for whose  etymology  see  wind,  n.
=== between markers listing headwords ===
Niobe,  n.,  the  daughter  of  Tantalus  and  wife  of Amphion  whose  seven  sons  and  seven  daugh¬ ters  were  sla
I U4V
ebhah,  ‘enmity’,  Akkad,  ayabu,  ‘enemy’,  and  the Hebrew  PN.  lyyobh.  Cp.  Job  and  niobium.  For other  
Derivative:  Niobe-an,  adj. niobic,  adj.,  columbic  ( chem )  —  Formed  fr.  nio¬ bium  with  adj.  suff.  -ic.
niobite,  n.,  columbite  (mineral)  —  Formed  fr. niobium  with  subst.  suff.  -ite. niobium,  n.,  a  metallic  el
nip,  tr.  and  intr.  v.,  to  pinch  sharply;  to  bite  — ME.  nippen,  prob.  fr.  MLG.  nippen,  ‘to  pinch’ 
Derivative:  nip,  n.,  a  pinch,  bite, nip,  n.,  a  sip.  —  Cp.  LG.  and  Du.  nippen,  ‘to  sip’, and  E.  n
nipa,  n.,  an  East  Indian  palm.  —  Sp.  and  Port., fr.  Malay  nipah.
nipper,  n.,  1)  one  who,  or  that  which,  nips  or pinches;  2)  a  small  boy  (British  colloq.);  3)  pi., small
nipping,  adj.,  that  which  nips;  sharp.  —  Formed with  part.  suff.  -mg  fr.  nip,  ‘to  pinch’. Derivative
nippy,  adj.,  1)  nipping,  pinching;  2)  sharp;  3) quick,  active  (British  colloq.)  —  Formed  with adj.  suff.
Derivative:  nirvan-ic,  adj.
Nisan,  n.,  name  of  the  first  Jewish  month  —  Heb.
Nisan,  fr.  Akkad,  nisannu. nisi,  conj.,  unless,  if  not  (a  term  used  in  law,  as decree  nisi,  order  nisi, 
nisus,  n.,  effort,  endeavour.  —  L.  nisus,  ‘a  striving, exertion,  effort’,  fr.  nisus,  pp.  of  nit  or,
nitro
re,  ‘to  close  the  eyes,  blink,  wink  at,  overlook (errors),  connive  at’.  See  connive  and  cp.  nicti¬ t
nit,  n.,  the  egg  of  a  louse.  —  ME.  nite,  fr.  OE. hnitu,  rel.  to  Norw.  nit.  MDu.  nete,  Du.  neet, OHG
Derivatives:  nit-t-er ,  n.,  nit-t-y,  adj. niter,  nitre,  n.,  nitrate  of  potassium  (chem.)  —  F. nitre,  fr. 
Derivative:  nitrate,  tr.  v.,  to  treat  with  nitric acid.
nitric,  adj.,  1)  pertaining  to  niter;  2)  pertaining to  nitrogen;  3)  containing  nitrogen.  —  F.  nitri- que
```


## [2026-09-07T19:32:01.486Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(len(leaves))\nfor i in (206,207,208,209):\n    print('=== leaf',i,'===')\n    print(leaves[i][:2500])\nEOF"
}
```


### [2026-09-07T19:32:02.764Z] TOOL RESULT

```
232
=== leaf 206 ===
n, fall down’: [avagmat]a nsf. past pte. ($244) DSe 46f (conj. of Kent, cf. JAOS 54.46).
рата + gam- ‘go forth’: paragmata nsf. past pte. ($101, $103.IV, §122, 8132.2, §244) DNa 44f.
ham- + gam- ‘come together, assemble’: ha"- gmaté npm. past pte. ($101, $1081У, $1322, $140.V, $244) DB 2.32, 38, 43, 52, 58; 3.65. See also Надтаійла-.
gay- vb., see Jiv-. gara- ‘devouring’, see bdtugara-.
garta- sb., either ‘cave’ or ‘wagon’, see Asa- garla-.
Garmapada- adj. ‘Garmapada’, the fourth month, June-July: Elam. kormabadas, АКК. du-
183
'"üzu. From garma- ‘heat’, Av. garama-, Skt. gharmá-, Lt. formus ‘hot’, NEng. warm, pIE *gthormo-, cf. Gk. bepuos (with analogical -e-), + pada- ‘step, station’ ($29, §31, $149.1, $161.Ib, $165): ‘Heat-Station Month’. — Garmapadahya gsm, DB 1.42; 3.71, 46.
gav- sb. ‘cow, cattle’ ($101): Av. gau£, Skt. gaus, Gk. fois, NEng. cow, pIE nom. *g*dus: in Gaubaruva-, Gaumäla-, perhaps in Gatagu-.
gasta- adj. ‘repugnant, evil’; пі, as sb., ‘evil, harm’: past pte. ($85, $242.I) of vb. *gant- *gandh- ‘smell’, Av. ganti- ‘evil odor’ (AIW 493), duZ-gantt- ‘evil-smelling’ (AiW 757), Skt. gandhá- ‘odor’ (Bv. Gr. $179); for meaning, ef. Lt. odor ‘smell’, бй ‘(I have smelled), I hate’, odium ‘dislike, hatred’. Not abstract to same root, *gant-tdi-, nom. gasta', abl. shortened by haplology, as taken by Hz. AMI 8.68, ApL 173-7. gastá nsf. DNa 57f. дазій absn. DNa 52; XPh 57; ASa 5°; A’Sde 4 (gasta da, db; $53); A?Ha 6°.
gud- vb., see gaud-.
gub- vb., see gaub-.
grab- vb. ‘seize (аз possession), seize (as prisoner)’, pres. garbaya- (§30, $217): Av. grab-, pres. gaurvdya-, Skt. grabh-, pres. grbhdyah, NEng. grab, pIE *ghrebh-. See also Patigraband-. agar- . bayam Ist sg. imf. DB 24 bis; 4.7, 32; 5.25f; DNa 17; DSe 16; DZe 8. agarbáya imf. DB 2.88; 3.74, 90°; 5.12. agarbaya* 3d pl. imf. 04232.) DB 2.18; 3.48, 49; 5.27f. agarbayalà imf. mid. (§235.11) DB 1.42, 43, 81; 3.82f. When meaning ‘seize as prisoner’ (DB 2.4 second occurrence, 13, 88; 3.48, 49, 74, 90; 4.7, 32; 5.12, 25f, 27f) per- haps not agarb- but ágarb-, from à + grab- (see below).
à + grab- ‘seize (as prisoner)’: dgarbita пзш. past pte. pass. ($80, §217, $232.11) DB 2.73. For uncertain examples, see under grab- (uncom- pounded).
-cé (i.e. -cd) enel. conj. ‘and’: GAv. -@, LAv. -€a, Skt. ca, Gk. тє, Lt. -que, pIE уш, ~... -cé ‘both ... and’ DB 1.65, DNb 32; cà .. . -cã ula ‘both ... and... and’ DB 1.66-7. -cé DB 1.65 ter, 66, 66f; DPd 9f; DNb 32 bis; XPh 41, 51, 54. -ca-maiy DNb 28, 51, 52 (§51
=== leaf 207 ===
3f, 57; XPa 20; XPc 14; XPf 48, alva}m-c* ($521) DB 5.9. Ка&-сїу nsm. DB 149, 53; DSe 37. @& ciy asn. DB 1.58. paruvam-ciy DB 1.63, 67, 69. yaciy (q.v.) DNb 35, 36, 57. haw-cty DPe 23f. hakaram-ciy DNb 34f. [haca-cily DSf 23: vakna-|cily XPg 7f, less likely than vaknalptly, see under apiy. |
Citcizri- sb. ‘Cincikhri’, father of Martiya (§163.V): Elam. st-in-sa-ak-ri-1§, Akk. #-in-Sa- ah-ri-i& Cicizrais gsm. (§179.1V) DB 2.9.
сій adv. ‘so long’, correlative with уйій ‘un- til’: from ci- + suffix seen in Gk. ёте-та ‘then’ (8191.11; wrongly König, RuID 72, and Sen 40). DB 248, 63.
cica- sb. ‘seed, lineage’: Av. &6ra-, NPers. &hr ‘origin’ ($78, $148.IIT). In Ariyaciqa-, Ciça- іахта-.
Ciga"lazma- sb. ‘Cicantakhma’, а Sagartian
OLD PERSIAN
rebel: Elam. şi-iš-ša-an-tak-ma, Akk. -it-ra-an. — | lah-ma, Gk. Tpravraixuns. From ciga-(§9.n1) + | lazma- ‘brave’ ($9.11): ‘Brave-by-Lineage’ (§160,- Ie); the -zm- is Median ($163.II; Jacobsohn, KZ 54.261; Bv. BSLP 31.2.79). For the nasal end-
ing the prior element, see $159.n1. Cicatazma
пет. DB 2.79; 4.20; DBg 1f. Ciçatarmam asm, DB 2.871. Cicalaxmà ism. DB 2.86.
сіла] emphasizing adv. after neg., ‘at all’: , :
Av. cină ‘also, likewise’; perhaps isn. of ci-, cf.. 4 JAOS 58.116-7, 324, and Harl, KZ 63.2 (not ! eità], with Sen 134). DSe 36.
ciyăkara- (§53) adj. ‘how great’; nt. аз sb., ‘how great a thing’: *ciya(n)t-, cf. Skt. kiyat nsn. ‘how much, how many’, + kara- to root kar- ‘make’ ($160.19; Bthl. AiW 597; hardly to kara- ‘time’, cf. hakaram, as taken by MB Gr $293, Hz. ApI 101-3). ciyakaram nsn. (§259) DNa 39; ciyükaram DNb 50; ciyakaram-ca-maiy (written — : -"m*m*eur; $41, $51, $132, $138.I; Lg. 15.178, — | against Hz. ApI 240) DNb 51, 51f. 1
CiSpi- (so Schaeder, SbPAW 1931.641.n4; i Catišpi- acc. to Justi, INB 152, on the evidence of certain spellings in Greek) sb. "Teispes', King of Elam about 610 в.с., ancestor of Cyrus and Darius: Elam. $1-13-рї-1$, АКК. $-4f-pi-i$, Gk. Téergs (S117, 8124.3, §164.V). Стр nsm. (824, §179.IV) DB 1.5°; DBa 8. Cišpãiš gsm. (824, 8179.IV) DB 1.5f; Cišpaiš ($24, S170.IV) AmH 3; DBa 8.
ja*tar- sb. ‘smiter, slayer’: Av. Jantar-, Skt. hantdr-; pIE *g*hen-tor-, agent noun to OP root jan- ($154.11). Jat пзш. ($186.1) DB 4.58, 78.
jad- vb. ‘pray, ask’, with acc. of person and асс. of thing: Av. Jad- (gad-, Bthl. AIW 487), pres. faiya- (§214), Gk. aor. inf. mid. Өёосасдо:, pIE *g*hedh-. — jadiyümiy lst sg. ($226.1) DPd 21; DNa 54; XPh 59; XSc 4.
jan- vb. ‘strike; smite, defeat (enemy ш. battle
=== leaf 208 ===
 Skt. jū- ‘press for- ward, impel quickly, excite, promote’, pres. jdvate ‘hastens’, caus. javayati. Cf. Ву. BSLP 332.152; Hz. AMI 4.127, 8.37-8, 65-6, ApI 366-7; Wb. МА 41.8320; Bailey, BSOS 7.292-4; Schaeder SbPAW 1935.502; Kent, Lg. 9.43, 231.
abi- + jav- caus. ‘promote, increase, add to’: abiyajüvayam 1st sg. imf. ($215) XPg 9; abijáva- yam (§23.1, $140.IIT) XPf 40.
jtyamna- pte. as adj. ‘growing old’, nt. as sb. ‘end’ ($109, $241): Av. Jyamna-, pte. to root }уй- ‘grow weak’, Skt. jinåti ‘grows old’. jiyamnam asn. DB 2.62.
ji- vb. ‘live’: Av. fait: (gay-, Bthl. AiW 502), Skt. Джай, Lt. vivit, pIE *g*īųeti (§216); see also gaiéd-, jiva-. ajivatam 3d du. imf. ($229) DSf 14; XPf 21. jwà 2d sg. imv. ($2371) DB 4.56, 75.
jiva- ad). ‘living’: Av. fva-, Skt. jivd-, Lt. vivos, pIE *g*iuo-, cf. *g*iuo- in Gk. Blos "life", *g*ig*o- in OEng. cwicu "living, NEng. quick (8101, $114, $150). See also 7й-. Jiva nsm. XPh 48, 54. jva-diy Аза 3 (dubious $22, 555.1; ef. JAOS 51.229, Scheil 21.93, Wb. AfOF 7.45). jivahya gsm. DB 5.19f, 35.
jü- vb., see jav-.
-{а- encl, demonst. pron. ‘this, it’: Av. Skt. ta-, ef. OP tya-. Only -tā apm., referring to patikarā,
185
in avabasa-a DB 4.72 (8133, $196; JAOS 62.272- 3).
{аита- sb. ‘family’ (8149.1): Av. taoxman-, NPers. tuzm, Skt. tokd-m ‘offspring’, tókman- tokma-s ‘young blade of barley’; -zm- became OP -hm- (5103.1, 5118.1), but remained in Med. (Ву. BSLP 31.2.76-9, Gr. $188; wrongly Mt. Gr. §75, Kent JAOS 35.329-31). taumd nsf. DB 1.8; 4.56, 58f, 64, 75, 79; DBa 13. іаитат asf. DB 488. іаитӣуӣ gsf. ($119) DB 1.9, 28f, 45, 49; 2.16, 81; 4.19f, 22; DBa 15; DBe 8; DBg 11f. taumaya absf. DB 1.61f.
tauman- sb. ‘power, strength’: deriv. of root tav- ‘be strong’, with suffix -man- as in Skt. nama ‘name’, Lt. nomen (§122, $155.11). For separa- tion from taumd- ‘family’, see Tm. Lex. 91, and Kent, JAOS 35.329-31. See also tawiyah-. taumā nsn. ($187) DB 4.74, 78; 5.19°, 35. tau- тату (= taumanis-Saiy; §41, §130, $138, $187) ipn. DNb 25f (Lg. 15.171-2, 176; not gen. sg. with Hz. Api 327; hardly loc. sg. with Sen 247; possibly aee. du., ‘two powers lof mind and of body|’, with Pisani, Riv. Stud. Or. 19.88-9).
lauviyah- adj. ‘stronger’: comp. to *tauma-, adj. to tauman- ‘power’; for formation ($48, $122, $156.IIT, $190.1-1), ef. Skt. sthürd- ‘strong’ and comp. sthdviyas-, Av. stūra- and comp. staoyah-, tarma- ‘brave’ and comp. tqsyah-: JAOS 58.324. іашлуй nsm. (§185.1V) DSe 39 (not to pres. pte. tavya-nt-, as taken by Hz. ApI 328).
takaba
=== leaf 209 ===
it (§76.V, 5148.1). Cf. Gray, AJP 58.67; Hz. Klio 8.51, AMI 2.77; Hinz, ZDMG 95.227. lacaram asm. DPa 6; АР]. dacaram ($494) рва 3.
tanii- sb. ‘body, self’ (8$153.IT) Ау. tand-, Skt. tani-; cf. Debrunner, IF 52.136. Decl., 51831. lanüs nsf. DNb 33. lanüm asf. XPf 31.
| tar- vb. ‘cross over’: Av. tar-, Skt. tdratz, caus. türáyalt, Lt. trans pte. as prep. ‘across’, cf. NEng. through. See also fara. vi- + tar- ‘go across’, caus. ‘put across’: viya- larayam Ist sg. imf. (§215) DB 5.24f. viyatarayd- mā lst pl. imf. (5230.1) DB 1.88.
fara prep. with aec. ‘through’: Av. tarō, NPers. tär, Skt. ards; formed on root tar- (q.v.) similarly to para (q.v.). іста] DZe 12.
Táravà- sb. ‘Tarava’, a town in Persia; Elam. -F-ra-ü-ma, АКК. ta-ar-ma-. Тато nsf. DB 3.22.
larsa- pres. stem. of vb. ‘fear’, with Ласа + abl.: Av. tarasaiti, NPers. térsé5, pIE "is-ske-ti (831, $97, $212), ef. pIE *tres- in Skt. trdsati, Gk. тре, also *trem- *trep- in Lt. tremit ‘trembles (with fear)’, trepidus ‘agitated (with fear). Jarsatiy ($228.1) DPd 11f. iarsa"tiy 3d pl. (§232.1) DSe 38f. alarsa imf. DB 1.50f. atarsa” 3d pl. imf. (5232.0) DB 2.12°; DPe 9. tarsam 1st sg. inj. (8224, 5237) DPe 21.
tav- vb. ‘be strong’: Av. tav-, Skt. tu-, ef. Gk. ravpos ‘bull’, Lt. taurus. See also ulava-, tauman-, lawiyah-, lunuvat- (but cf. Hz. ApI 328-33). {йгауай ($122, 8123.2, $215) DNb 33f. atávayam Ist sg. imf. (5215) DNb 47.
taš- vb., see under tazš-; in ustafanà-.
Tigra- sb. ‘Tigra’, a fortress іп Armenia: Elam. ti-ig-ra ($108.1У). Tigra nsm. DB 2.39.
*hgra- adj. ‘pointed’ (S103.IV, 5148.1): Av.
OLD PERSIAN
tiyri- ‘arrow’, Skt. tigmd- ‘pointed’, cf. with strong grade Av. bitaéya- ‘two-edged’, Skt. téjate ‘ig sharp’. See also татай. figram asf. DB 5.22.
Tigra- sb. ‘Tigris’ (§76.V, $103.1V, $107, $166): Elam. £-ig-ra, Akk. di-iq-lat, Gk. Tiypas. Tigram ast. DB 1.85, 88.
igrazauda- adj. ‘wearing the pointed cap’ + i ($161.ITa), asisshown in the sculpture of Skunkha 4 the Scythian at Behistan (cf. also НФ. 7.64): ’hgra- ‘pointed’ + хашіа- ‘cap’ ($159). tigra- тамай npm. DNa 26, DSe 25°, XPh 27; for пега, ($56.11) DN xv, A?P 15.
tunwa"l- adj. ‘powerful’: pte. (8240) to *tu- | nautiy, pres. to lav- (8122; JAOS 15.170; otherwise — : Hz. ApI 329-32). Decl., $190.1, $210. tunwa | папа. (§210.1) DNb 10. tunuva"lam. (589) DB 4.65. tunuva*tahya gsm. DNb 9.
{шат pron. ‘thou’: GÀv. эт, LAv. tim, Skt. tuvám, pIE *tuyom; ef. Skt. dm, Gk. Dor. r$, Lt. tà, Gt. pit (576.1, $187). Decl., $194. turam nsm. DB 4.37, 41, 67, 70,
```


## [2026-09-07T19:32:09.934Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (215,216,217):\n    print('=== leaf',i,'===')\n    print(leaves[i][:3000])\nEOF"
}
```


### [2026-09-07T19:32:11.092Z] TOOL RESULT

```
=== leaf 215 ===
rada&a, duvaista-. dürau lsn. as adv. ‘afar, far away, far and wide’ (GAv. düiré, LAv. duire, Skt. d'ré; $65, 6191.111) DNa 44. duraty apiy DSe 11, DZe 6, DE 18, XPa 9, XPb 18, XPe 8, XPd 13, XPf 13, XPh 10, XE 18, XV 14, A'Pa 14f°, A’He 17. düraiapiyy DNa 12, dürayapiy DNa 46 ($18, $136).
duradasa adv. ‘from afar’, with preceding hacá: dūra- + adv. -dä asin отада + abl. -ša asin avada&a (§135, 5191.1; ЈАО 54.37).  DSf 23.
duruj- vb. ‘lie, deceive’: Av. druj- ‘le’ (draog-, Bthl. AYW 767), pres. druZasti, sb. druzé ‘principle of evil, devil’, Skt. drúhyatí ‘deceives’, Gm. trügen, pIE *dhrugh- (876.111). See alsodrauga-. adu- rujiya imf. (§101, $103.IV, $113, 5128, 4132.1, 2, 3, $214, 5228.11) DB 1.39, 78; 3.80; 4.8, 10f, 13, 16, 18, 21, 24, 261, 29; DBb 2; DBc 2; DBd 2; DBe 3f; DBf 1; DBg 2; DBh 2f; ОВ! 2f; DB} 2f. adurujiyasa" 3d pl. imf. ($214, §218.1, $232.III) DB 4.34f. duruxiam nsn. past pte. pass. ($103.IV, $122, $128, 8132.1, 3, $242.I) DNb 52, 5f; asn. DB 4.44f, 49f.
duruva- adj. ‘firm, secure’: Av. drva-, Skt. dhruvd-; deriv. to root in OP ‘dar- ($122, $128, $150). durwä nsf. DB 4.39.
duvatsta- adj. ‘very long, very far’: superl. to dūra- ($156.IIL, §190.11 $191.0; МВ Gr. $275), ef. Skt. davisthd- with slightly different formation.
192 OLD PERSIAN
duvais[ta]m asn. as adv. ‘for a long time’ DPe 23 (cf. remarks s.v. hyà).
duvara- sb. ‘door’: Av. dvar-, Skt. dhvar-, Gk. дора, Lt. forés, NEng. door, Lith. dvéras ‘court- yard’, pIE *dhuor- dhur- and its extended forms *dhyoro- etc.; see also duvarfi-. duvarayd-maiy lsn. ($186) DB 2.75; 89f.
duvari- sb. ‘portico, colonnade’: duvar- ‘door’ + varði- ‘cover, protection’, to root var- ‘cover’, with haplology ($34, $129, $152.IV, §160.Ia; ВЫ. AIW 766). duvarfim asm. XPa 12.
duvitdparanam adv. ‘one after the other, in succession’, a meaning agreeing with Elam. Samak- mar ‘ex ordine’: duvità ($191.11, $204.IT), MPers. dit ‘one or other of two’ (Bthl., quoted by Tm. Lex. 102), ef. OP duviliyam ‘a second time’, Skt. 0015 ‘twice’, Lt. bis, + paranam ‘before, previ- ously’ (Tm. 1.е., and Vdt. Stud. 1.8). This is better than Tm.’s "long aforetime', adv. duvità ong’, GAv. дайа, Skt. dvità (cf. OP duvaistam), + paranam (as above); also than KT's duvità- parnam ‘in two lines’, contaming the cognate of Skt. parnd- ‘wing’ (supported by Wb. ZDMG 61.724-5, KIA 10-1, and by Hz. AMI 1.112n). DB1.10; DBa 17.
duvitiya- adj. ‘second’: GAv. daibitya-, LAv. bitya-, Skt. dvitiya-, pLE *dyitiio- (676.11, 51441, 5204.1). See also duwilàáparanam. дилат, asn, as adv. ‘a second time’, DB 2.87f, 57, 3.77; as inner obj., ‘a second (uprising), DB 3.24 (not duvitiya-ma udapalalà ‘was second to rise up from me’, as Bthl. AiW 964 takes it, since udapatatà nowhere else takes an expression of the person against whom uprising is made).
duš- insep. prefix ʻi: Av. dui-, Skt. dus-, Gk. dve- ($76.Ш); in dušiyāra-, duskarta-.
dusiyara- sb. ‘evil year, bad harvest, famine’: duš- + yar- ‘year’ made thematic, Av. ydr-, Gk. ёра ‘season’, NGm. 
=== leaf 216 ===
e 15; DZe 10. drayahya lsn. ($136, §251A; wrongly taken as gen., Hz. АрІ 141-3) DB 1.15, DPe 14, DSe 28°; drayahiyà ($27) XPh 23.
naiy adv. ‘not’: Av. 207, РЫ. në, Skt. ned; :
from pIE *ne, Skt. na, Lt. ne-scio ‘I don't know’, -+ Эа, asn. of pron. i-, Lt. id, OP id-am, ete. (869, 884, $191.1, $291.11, §292a). DB 1.32, 48, 49 ter, 52, 53, 71, 91°; 221, 24, 31, 51, 84; 3.15, 86; 4.44, 47 bis, 51, 55, 58, 63 bis, 63f, 64°, 65 bis; 5.16°, 31; DPd 11; DNb 7f, 12, 13, 21, 23, 36, 40; DSe 36, 40 bis, 43°; DS} 3; XV 22. nai-maiy (836) DB 4.64. nai-ma DNb 8, 10, 19. nai- pati-mà (8133) ОМ 20. nai-&im DB 4.49. naty- diš ($136) DB 4.73, 78.
naiba- adj. ‘beautiful, (religiously) good’, re- .
placing GAv. vahu- ‘good’, and opposite of duš- karta- (Hz. AMI 8.68, ApI 266-7): NPers. nē ‘brave, good’ ($11, §75.V, $148.11). пафа nsf. DPd 8. naibam nsn. XPa 13, 16; XPg 4; XV 20. naibam asn. DSe 32°; DSi 4^; DSp 2f°; XPh 43.
naucaina- adj. ‘of cedar’: NPers. nóZ, пдѓап ‘pine cone’; therefore naucaina- ‘pine-cone-shaped’ ($147.11), appropriate to the cedar (König, Burg- bau 53-4; Hz. AMI 3.58). naucaina nsm. DSf 30f. |
nab- vb. ‘perish’, causative (8123.2, $215) "in- jure; destroy’: Aw. )nas-) ӨЮ. naé-, Gk. vexus
7 ыйсы аЙ eet NUI ШЕЛ, АМАА а аз an ШО. Дені. Zr é
DD де 5... anes
LEXICON
‘corpse’, Lt. acc. nec-em ‘destruction’, nocet ‘harms’, pIE *nek- (887).
vi- + nab- caus. ‘injure, harm’: vindPayatiy (8215) DNb 17f. viyanatlaya imf. (§122, $1232, $215) DB 4.66. vinátayá"tiy За pl. subj. (8222.1I, §232.1) A’Sa 5°, A?Ha 7° (conj. Kent). vinátayais opt. ($215, $223.II, $228.11) DNb 20, 21. vi- nastahyd gsn. past pte. pass. as sb. ($03, $122, $242.11) DNb 18.
Nadi"labaira- sb. ‘Nidintu-Bel, a Baby- lonian rebel: Elam. nu-ti-ut-be-ul, Akk. ni-din-ti- йе] (§75.V, §76.V, $107). Naditabaira пзш. DB 1.77, 92f; 2.1; 4.12; DBd 1. Naditabairam asm. DB 1.80, 84; 24, 5. Naditabairahyà gsm. DB 1.85, 89, 95.
napüt- sb. ‘grandson’: Av. Skt. napat-, Lt.’
nepos, pIE *nepot- (875.1, §110, $142). napa nsm. (§124.5, §188.1) AmH 4; DB 1.3; DBa 4; А:Ра 16°.
Nabukudracara- sb. ‘Nebuchadrezzar’, son of Nabonidus; name assumed by the rebels Nidintu- Bel and Arkha: Elam. nab-ku-tur-ra-sir, Akk. nabu-kudurri-ugur (82, 833, §75.V, $128, §163.- VD. Nabukudracara nsm. DB 3.80f, 89; 4.14, 29f; DBd 3f; written Nabukuracara ($52.V) DBi 5f. Nabuk*dracara (822) DB 1.78f, 84, 93.
Nabunaita- sb. ‘Nabonidus’, last king of the New Babylonian Empire, 556-39. в.с: Elam. na- bu-ni-da, Akk. nabü-na'id; Gk. Aaßivnros (Hat. 1.74, ete.). Nabunailahyà gsm. DB 1.79. Na- bunaitahya (§36.1Vb) DB 3.81; 4.14, 30; DBd 5f; DBi 7f.
niman- sb. ‘name’: Ау. náman-, NPers. пат, Skt. náman-, Lt. nomen, pIE *nómen-, cf. Gk. буора, NEng. name ($109, $110, 5155.11). See also Andmaka-. náma^, suffixless lsn. used with mase. and nt. generic nouns to denote specification ($112, $187, §251C, §312): DB 1.28, 30, 36, 37, 74, 77, 92; 2.8f, 9, 14°, 19, 22, 29, 38, 49, 65, 79, 82, 95; 3.5, 12, 13, 22 bis, 31, 34, 44, 51, 56, 78, 84; 4.8,
=== leaf 217 ===
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
paié- vb. ‘cut, engrave, adorn’: Av. paésa- ‘adornment’, Skt. pisdtz ‘cuts, adorns’, Gk. токіћоѕ ‘variegated’, OCS pisati ‘to write’, pIE *peik-, cf. Lt. pingit ‘embroiders, paints’ (Wb. AfOF 7.42). Cf. also nipišti-, parsiyd-, P
```


## [2026-09-07T19:32:24.214Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT niš ===\"\ngrep -n \"niš\\.bar\\|niš-bar\\|nižbar\\|niš\\.\\|nis\\.bar\" BRT.txt | head -20"
}
```


### [2026-09-07T19:32:24.261Z] TOOL RESULT

```
=== BRT niš ===
```


## [2026-09-07T19:32:25.421Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK nis ===\"\ngrep -n \"ni-s-\\|nis- \\|*nis-\\|niž\\|nis-, nis\" POK_full.txt | head -20\necho \"=== POK ni- page ===\"\ngrep -n \"^ni-, nei-\\|ni-, nei\" POK_full.txt | head"
}
```


### [2026-09-07T19:32:25.486Z] TOOL RESULT

```
=== POK nis ===
ugrep: error: error at position 18
(?m)ni-s-\|nis- \|*nis-\|niž\|nis-, nis
                  \___empty (sub)expression


=== POK ni- page ===
```


## [2026-09-07T19:32:28.297Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls POK*; echo ---\ngrep -n \"nis-\" POK_full.txt | head -20"
}
```


### [2026-09-07T19:32:28.401Z] TOOL RESULT

```
POK_01.txt
POK_02.txt
POK_03.txt
POK_full.txt
---
13685:bbuja' twist, arm', bboga-b' coil of a snake; ring' (: Old High German boug); nis-bhuj- 
72890:Avestan haxay- {hasi-) ds., ap. Haxamanis-^ 'Axai|j£vr|^';
```


## [2026-09-07T19:32:35.626Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- BRT nis/niz variants ---\"\ngrep -n -o \"ni[sšzž]\\.[a-zA-Zāī]*\" BRT.txt | sort | uniq -c | sort -rn | head -30"
}
```


### [2026-09-07T19:32:35.683Z] TOOL RESULT

```
--- BRT nis/niz variants ---
      1 7647:nis.
      1 4978:nis.
      1 26783:nis.
      1 2433:nis.
      1 23451:nis.
      1 2199:nis.
      1 17139:nis.
```


## [2026-09-07T19:32:36.435Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"ni-, nei-\\|nieder, unter\\|'nieder'\" POK_01.txt POK_02.txt POK_03.txt | head -20"
}
```


### [2026-09-07T19:32:36.481Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T19:32:41.094Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"hinaus\" BRT.txt | head -30"
}
```


### [2026-09-07T19:32:41.141Z] TOOL RESULT

```
3138:•  p,  a-xäata-  Adj.  (fem.  °/3-)  'unverletzt, ungestört':  Ayi^  duvaislam  ÜyätW  'tl hauvciy  . .  nirasitliy  (sd.)  , .  "Wohlbehagen, auf  sehr  lange  Zeit  hinaus  ungestört,  es wird  sich  . .  einstellen  . ."  D,  5. 3.
4807:mit  US  i)  'heraus-,  hinausgehen':  isar» pasca  paradristim  .  .  US  haia  baooS  (sd.) \ayap'^  \,y.2;  — ,  usayeiii  parayeni  V.  22.
6725:mit  US  'hinaus-,  hinaufschicken':  pairikä .  .  ya  uzStihat  aurS  matnyus  Yt-Ä  39.
7171:/'  /■Rh       r  ■  1"      /   /"  I  Feuer  hinaus,  jenseits  des  Feuers  gelegene"
8349:—  ,  .  maiüatam  frä%W3r?sat  . .  aAurS  . . 'ri  AarqmYtio.$o;  —  W-riy  däraya*va*um xlaya'hiyam  D.7(?);  —  I'  °riy  *abistam{^.) upariyayam  Bh.  4.i3(?).  [J)  auf  die Frage  wohin?:  yS  vaslnm  upanhanzaiti 'ri  aitim  irislim  V.Ä23;  5,61;  —  avqm vanqm  .  .  yqm  °ri  urvaranqm  .  .  taoxma niäayaj  Yt  /2. 17.  b)  'Über  —  hin',  mit Akk.  oder  Instr.:  mana  raya  . .  pasvasca staoraü  °ri  zqm  7'ÜarpnlaYt.$.8^;  ig.^4; — yais  °rf  äya  stma  gaobTs  *fyeintiY.i2. 3.  c)  "über  —  hinaus',  mit  Akk.  oder Instr.:  *uzdatum  (sd.)  hl  .  .  ksrmaot  'ri spamm  'ri  raohm  "ri  vihrk^m  "einen  Auf- bau . .  über  den  Hund  hinaus  *'  , ."  V.
8420:Ableit  aus  *Hpairi,iaena-  Adj.  'was  über  die (Flughöhe  der)  Adler  hinausgeht',  mit  V^Jdhih in  der  2.Silbe,  S  'twa.  1  aE.0  —  inp,  (Pü!) apärien.  —  0  Anders  KZ.  38.  292.
8496:•  j.,  g.  'U3,  US',  UZ",  p.  us°,  ud"  i)  Adv. (nur  Komp.  und  Ableit);  —  2)  Praev, (mit  'ai'-,  '^■warps-,  pat-,  'bar-,  'stä-,  'zan- usw.);  Iiinauf;  hinaus'.         IYLÄ32:   hes
11244:•  j.  Öamtu-tära- "  .\dj,  'über  die  Ent- fernung eines  C.  hinausgehend,  weiter  als ein  €.  gehend,  reichend';  °r5  F.  ig.
12045:•  p  *tara''-draya*'  Adv.  'übet  das  Meer hinaus,  jenseits  des  Meers',  mit  dem  Relativ Bezeichnung  einer  Abteilung  der  Sak^ix: saka  (sd.)  tyaiy  f  D.  6.  3.
12079:Bildung  wie  iari.zaairä.;  vgl,  /iaeli./ara-.  — ai.  vgl.  iar6ddzi}as-  Adj.  —  ")  Nach  der fl-Dekl, t^d  (wieder)  verschafft,  heimlichWasserj.j,  tarö.piS-wa- i)  Adj. 'der  ungenügende aad  Kraut"  V.  75. 10;  9',  s)  Praen.  mit  |  Nahrung  hat,  bekommt,  Mangel  anNahrung Akt;  a)  'durch  -  hin,  über  -  hin,  über  l^xditV:  yff  spätum^'^wim^dasH yim  pasus.- -  hinw^,  hinaus';  o)  räumlich:  husi^m  \  ^aurum  "wenn  einer  den  Hund  ,/*.  an f^sm  ra^aya  TS  . .  vilanuhaitm  Yt  5,  [  Nahrungsmangel  leiden  lässlf'  V.  13.  20, '•r,  ?8;  —  hrTs'^J  'rff  pir>tamcit  h!  urva- 1  24;  20.  2)  n.  'ungenügende  Nahrung, »■  ..frqparaymi  Y./5.6;  7J.  i6,  Vyt.|  Nahrungsmangel' (?):  paiH  'w>m  daidyat •fc>  Nik.2;  —  mtknm  .  .  yS  paeiryö  'r3\yai:a  . .  Vytß  (?);  —  *Vf^  N.  13  (?)". **■«   asnaffUi     Yt  10.  13;  V.ltj.jo;   — |      I'ü,  (lu  Vyt.h  lar  i'ariin,(ra'S.):  *tar  fihn'\
12099:Ableit  lU  lafä+yär-;  ei  mag  ein  *tarS yän (AP.)  'über  die  Jahre  hinaus'  zu  Grunde  liegen,
15409:•  j.  para.daxäta-  Adj.,  nur  fem.  'tu-  'die Über    die  Regel    hinaus   is^   nicht  mehr  |
16303:•  j.  pouru.spaxStay-  f.  'weithin  reichen- des Erspähen':  daya  .  .  °tim  tbi^antqm paiti./aitTm  dusmainyunqm  ha'i:rä.itiväitlm harmriianqm  "gib  . .,  dass  wir  die  Feinde auf  weit  hinaus  erspähen,  die  Gegner  ab- wehren, die  Widersacher  auf  einen  Schlag besiegen"  Y.57.  26;  —  Hi  rfflr^..  Ytp.  i.
16825:mit  US  \)  'hinaustragen':  ydi  pa%a  utba- nnte  spanasca  irista  ,  .  "wenn  des  Weges hinausgetragen  werden  tote  Hunde  und  . ." V.  S.  14.  a)  'etwas  heraustragen,  heraus- schaffen aus  — ';  a)  mit  Gen.:  iritt^m  uzba- röit  apB  "man  schaffe  den  Toten  aus  dem Akk.  des  wohin?:  3  aisma  yasavuha  afi  Wasser"V. 6. 37.  P)  mit^a^b  undAbl.: mqm  bara  V.  7Ä  19;  —  avi  dsi  a!m  *ha-   us    haca    alibyö    nmanaHbyS    bart^m  .  .
17654:•  j.  fra-pad-  :fra-bd-  m.  'Vorderteil  des menschlichen  Fusses,  Vorderfiiss',  vom Knöchel  bis  zu  den  Zehenspitzen:  dasiram {hdyum)  'hdtm  V.  8.  67,  68',  69,  <J.  24*;  — yat  nä  paurva  °bda  (AD.)  /rabdöjirajB frama&aiü  "wenn  Jemand  über  die  Spitzen der  Vorderfüsse  um  eines  Vorderfiisses Länge  hinauspisst"  V.  /<?.  40*';  —   °bda
17657:hat :  ia  marl  fa  vinäsiärVi  pes  i  /rapiA /rapai  drahnäi  fräc  mnel  "wenn  man  sündiget Weise  Tor  den  Vorderfuss  einen  Vorderfuss  weit hinauspisst".  Die  Sonde  heisst  Av.35.6  hai pä% mkiihik  "Stehendpissen'.  Das  Pissen  soll  in hockender  Stellung  und  so  geschehen,  dass  der Urin  mischen  den  Fiissen  zu  Boden  geht.  Vgl. die  PüGlosse  in  V.  iS.  44  (bei  Haug  Essajrs  »  374). KompA.  —  n.  präpäd- -OL.  —Yü,-.  frapai,frabd.
17774:mit  US  1)  'aufziehen,  aufsteigen',  von Wolken :  äat  magya  usfravante  . .  yahva  . . "alsdann  steigen  die  Wolken  auf  . ."  Yt, 8. 40.  2)    Kaus.  'hinaus-,   fortschwem-
19251:•  j-,  g.  niä'*,  niS°'^,  p.  «i/*^*  i)  Adv. 'hinaus'  (nur  Ableit).  2)  Fraev.  'hinaus, weg'  (mit  qy',  'dar-,  'bar-,  näi^).
19450:mit  Abi.  '(emittere  ex  — ,  hinauslreiben  aus —  sva.)  berauben':  yastSm  x/ahräl  mazäa mSikat  jyalSus  v3  "wer  ihn,  o,  M.,  der Herrschail  beraubt  oder  des  Lebens"  Y. 46.  A.
19894:•)  Sie  werden  «Is  Zwillinge  gedacht  {%.yima- mit  Litt),  die  in  ewigem  Kampf  mit  einander liegend  alles  Seiende  gcschafTen  haben.  Nicht ganz  klar  erscheint  das  Verhältnis  des  guten (heiligen)  Geists  zu  AkuraMoidäh.  Es  kommt das  dahei,  dass  Zca-i^üiirai  Lehre  eben  doch nicht  rein  dualistisch  ausgedacht  ist ,  sondern das*  sie  über  die  beiden  uranfan glichen  und g;Ie ichmächtigen  Geister  des  streng  dualistischen Gedankens  die  Gottheit  dt^AkuroMaidSh  hinaus- hebL  Auf  diese  Weise  «iid  der  heilige  Geist, wo  er  in  Beziehung  zu  AhM.  gesetzt  ist,  lu einem  dienenden  und  yennitielnden  Gci«(  de» AML,  nicht  anders  als  Aia,  VohuManak  usw., und  als  nener  Gegensatz  ergibt  sich  nanmebr AhuraMaidäh  und  AnraMainyav.  Litt  bei  In. GIrPh,  3.  630  f.
20883:razunm  (sd.)  yS  mqm  mairyö  .  .  paiti pantata  "laqueum  (insidiatoris)  qui  me insidiator  ,,  oppugnavit"  Yt5.  so^J*;  — yö  ktnnavät  (Sp.  447  o.)  yim  yataite MÜrfm  .  .  albists  hyat  Yt.  10.  iio;  — fra paurvö vätqm  vazailt yqm<,^-ai.) pa>ö siti  haomö  ". .  (ad  vias)  quas  vias  .  ." Yt.  Ä33;  —  üvistayaica  ..  huframirtta- ya?ca  ysi  htnti  haoma  sura  "..(vinorum) quae  sunt  vina  .  ."  Vr.  (?.  3;  —  udiyasca rasvas^a  gatris  yailqmta  .  .  masyika  . gairinqm  nilmqm  ddhar>  "et  U.  et  R.  mons et  (alii  monte.s)  quorura  .  .  montium  . ." Yt.  IQ.  6.  c)  yS  NSm.  und  ySi  NPm. stehen,  ohne  Beziehung  zu  einem  Wort  des Übergeordneten  Satzes,  d)  im  Vorder- satz im  Sinn  von  'wenn  wer,  wenn  einer, wenn  man':  yp  kainTti?m  upäiti  .  .pührqm- {sd.)i^  hl  daoäili  mä  .  .  agsa  ya  kaine . . tarO  daxslsm  paraylt  (Sp.  152  u.)  V, /5. 9;  —  y5  ffiirikam  U^ravaittm  . .  xsudrä avi  fraiiharisaiti  hat  aiiihe  asti  paititis (sd.)  V.jtV.67f.;  —  y5  hl  *3p?r»ti3mnai (Sp.  869  o.)  nsil  visäiti  *främrUite  kö  .  . ai>!rapaitinqm\ea^  ..  astryäti  N.  j_j;  — yö  aiuä  bansma^a  */ra stürmte.. aoäi  anye . .  *framravainti  . .  vispaZiqmcd  arwi.snm- vaiti  (sd.)  vispe  ratufryB  N.  6b;  —  y5i pa'^a  utbartnte  spanaüa  irista  naraiM  . . hat  tä  päka  (sd.)  frayqn  .  .  "wenn  man desWegs  hinausträgt  tote  Hunde,.,  sollen  .. V.Ä14;  —  *ySi  dim  */rahincin  *antari ätar>m:a  bar>smaca  anairyanqm  tat  dahyu- nqm  v»r>hrili  uzjasaiti  N.  6(Vj  —  mit  der 1.  Plur.  im  Sinn  von  'wenn  wir,  unsereins': ySi  timäni  hqmiarämahi  (sd.)  . .  alrsmca .  .  aaf  pascaäa  . .  sps  vä  tiä  vä  iri^yat huha  ts  v»i-)^qn  aSe  ySi  mazdayasna  V. 5.39.  b)  im  Nachsatz  im  Sinn  von  'dass einer':  aya  daoia  disyJ/(sA.)ylf..  aiwy'ir?- hqm  (sd.)  nSii  aiwyästi  V.  18. 9.  ß)  adjek- tivisch: yaEca  ß«  narS  . .  Jason  brä^ra vä  haxaya  vH  .  .  yezi  laäS-cinanhö  jasqn .  hqm  ioa  iaSitm  hqm.bäray>n  "quique  . .  vin venerint,  (iis)  ,  ."  V.  4. 44.  Anhang
23814:•  g.  vouru-£a£änay-  Adj.  'weit  hinaus (in   die  Zukunft)   blickend':    raßorai   'nl
25557:iarü  und  Akk.  'sich  hinaussetzen  über  — , sich  verfehlen  gegen  — ':  nöii  a&äiti  */ra- raiisyanqm  (sd.)  ^urvhyHH^  *tarS  .  . data  .  .  sardhustraAt  P.  5Ö.
26701:mit  ß-^  'procedere';  1)  'hervortreten, auftreten',  Med.:  amava  mi^rB  fraxltaite Yt,  jo.  107.  a)  mit  /laca  und  AbL:  yai astvataritS  fraxltäite  (Konj.)  haca  apai kqsaoyäi  Yt.  ig.  92.  b)  mit  paiti  und \nSa.:  ß-axstaite"'>  paiti  äya  ztma  mihrB., YtJO.gS;  —  saätahe  . .  yö  . .  satB.alhry3 fraxstata"^  paiti  äya  S3m3  Yt/_J,  97;  — yänfm  .  .ya'^a  v»rihra}ä .  .fraxstane . .  simä paiti  Y.p.  ao;  ao,  2)  'hinaus,  ins  Freie gehen':  vasB  pascaita  fraxitaite  aiwi.- gäme  iha  hama  "nach  Belieben  soll  (kann) er  (der  Hund)  dann  hinausgehen  . ."  V. 1$.  4S"'.  3)  'sich  aufetellen,  Aufstellung nehmen',  vom  Priester:  säänm  ahmai  . . yahmäi  zaota  anasava  ,  .  pasca  bar»sma frahista  (3SPfA.)  Yt  10. 138.  4)  'voran- kommen, Fortschritte  machen':  tactntB nBit  apayeintHSp.  148  f.)  ianntB  nBit /ra- stanvanti  Yt  10.  20.
```


## [2026-09-07T19:32:50.273Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(json.dumps(d['BRT'],ensure_ascii=False,indent=1))\"\necho \"=== context around 19251 ===\"\nsed -n '19240,19270p' BRT.txt | cut -c1-300"
}
```


### [2026-09-07T19:32:51.720Z] TOOL RESULT

```
{
 "title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)",
 "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/altiranischeswr00bartgoog",
 "identifier": "altiranischeswr00bartgoog",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt",
 "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.",
 "notes": "Nourai's Table IV says 1979; that is the unchanged reprint.",
 "cites": "column number (the Altiranisches Wörterbuch is numbered by column, two per page)"
}
=== context around 19251 ===
•  j.   ni-zanga-   Adj,   'vom   Fnssknöcbel
hinab  gehend':  andvT  . .  'ga  (IS.)  aokra *paitijinuxta  ".  .  vom  Knöchel  abwärts mit  Schuhwerk  bekleidet"  Yt.3. 64.
•  j.  ni-zanta-  Adj.  'ein(d.  i.  im  Haus)''ge- boren,  ingenuus';  'um  F.  26.
mp.  (Pü.)  niiami;  ai.  vgl.  iti/'a-  Adj.  'eigen'; Bthl.  IFAni.  72.  27.  —  Pü.:  nieand,  erl.: /  pa  xmiak  säyll.  —  i>  S.  PüErl.
•  j,  *m-zbaya-  m.  'Anrufung':  mal  °yeke
dby  Google
io87
niä-
sraois  asyS  (soll  heissen)  "unter  Anrufung des  . .  Srr  Vd.  /2.
Zum  V.  *av-  (Piaei.  t#ii>'a-).   Wertlos.  —  Fü.:
ayät  iartan.
•  j-,  g.  niä'*,  niS°'^,  p.  «i/*^*  i)  Adv. 'hinaus'  (nur  Ableit).  2)  Fraev.  'hinaus, weg'  (mit  qy',  'dar-,  'bar-,  näi^).
KompA.;  Ableit.  —  iL  ai/',  w-' (luw.)  Adv., Praev.  —  Pii.:  afie.  —  ')  Wenn  yoio  Verbum getrennt,  sowie  vor  tonlosen  Leuten.  —  ')  Vor tönenden  I^naten.  —  3)  In  nijiyam,  Sp.  I53ni.
•  j.  iiiiaofaar^tayae-::!!  Inf.  '(und)  Acht zu  haben  auf  — ,  zu  wachen  über  — ':  frada- hai  nmanahaa . .  hani^räila  aiwyaxitraica nipsiayaüa  'ya^a  Yt.j.6;  Y. 77.11;  — mit  Akk.:  gaihiscä  tanvaiüä  nipätayaica 'yaica  Y.5Ä  a.
Zorn  V.  har-  mit  tu;   iSchr.  «.  S  ^S.  48,  — Y\\.:  pa  afe  sardärlh. j.  näaohanUü:  i.  unter  hat-.
•  j.  nisanharvd'ri-  f.:  s.  unter  tUlhantar-.
j.  miavhaiä:  s.  ^had-.
•  j.  ni-sastay-  f.  '(das  Sichsetzen,  Sich- niederlassen  auf  das  Weib  sva.)  Begatten'  *' : paoiryäi  upaHa  (sd.)  paoiryai  °la  (LS.) hrisatfm  ufiSzananatn  upazöit  V.  16.  15.
Zum  V.  'Aad-i  vgl.  aJaiisasla  Inf.  —  ai.  nisatlay- {.  'Untätigkeit'.  —  Pü, i/o  a/ar  miiniiiüli. — ')  iBed.  s.  ai.  nifeäüiah  RV.  lO.  S6.  lö,  bei Gdn.  VSt.  3.  37  'sobald  er  anfsitil'.
g.  nili{iyd  Y.  50.  2 :  s.  kartd-.
g,  nutal  Yt.  ig.    13:  d,  i.  »ii  tal.
•  j.  niä'tara-  Adj. 'der  äussere':  Satiüm.. avaJiiäsil  ava  'r»m  (ASn.)  kariayä  "dann sollst  du  aussen  an"  den  abgegrenzten Kaum  herantreten"  W.g.  13.
KompA.  —  Kompar.  aus  ms.  —  aL  vgl.  täffya- Adj.  —  Pä. :  kac  iuslaklar  apar  Mi.  —  ')  WdrtL 'an  das  Äussere  des  .  .*.
•  j.  niitara-naema-  m.  'Aussenseite',  nur Abis,  'von  der  Aussenseite  her  sva.  aussen, ausserhalb';  'mäj  nmänahe  V,  f^.  7;  — , nmarum  :^sraoxs?um  (sd.)  *antar>jiaimä^ st?hrpals>m  'mal  "V.^y.zi,
PiL :  hac  halailar  nemai.  ,
•  j.  niitarvtö.spaya-  Adj.  'mit  hinge- breiteten  Kissen,  worin  Kissen  ausgebreitet sind'i  'yi  (APn.)  . .  nmänä  Yt  10. 30;  —  1 *'spaem''>  ..  nmän^m  Yt. /O.  30.
'tfaya-  m.  sva.  /ra'ifäl-,  sd.  —  •)  Die  Hds. ' bieten  hier  asp',  \
•  '].  ni-stätay-  f.  'Anordnung,  Befehl':  yU\ niäayeiti  (sd.)  k^nße  sraoiyqm  (sd.)  isar^  \ ha  'ta  (LS.)  kiryeiti  Yt  10. 109.
j.  itiiläMm'  V.  i^.  50;  lies  naitäjt'
nu  1088
•  j.  ni-stQtay-  f.  'Preisung,  Ehrung*:  kva . .  vfrshraynoAe  ttqma,a*l>aitil .  ,  kva  .  , 'äaüil  Yt.  14.  i^z.
```


## [2026-09-07T19:32:58.248Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '16800,16840p' BRT.txt | cut -c1-400"
}
```


### [2026-09-07T19:32:58.317Z] TOOL RESULT

```
dby  Google
935  'bar-  J  —  'bar-  mit  apa  936
aHe  richtet  Ä.  die  Weisung"  Y.  6^2. 7 ;  — '  Y,  ^J- 1 3 ;  —  näirikaca  . .  Jamm  iaraäi tiatnniUa  räzanca  (sA)  barmlu  dahuls  väcim  V._j,ii;  YL/0,85,  J7.61,  ¥.70.4 ahuräi  mazdäi  anu/tmqmia  Yt  13.  157;  C^rTttii);  —  mihnm  .  .  ys . .  avaroit'^^ —  parlf  x^nsca{sA.)..barafu  cifarihanqm  (3SPTA.,  Augm.)  vaSm  Ytio.73; — vom iünalu  ".  .  man  soll 
1.  7  (wo  abari'tä);  —  inanä  t^ure^maxda  113.  8)  'reiten',  Akt  und  Med.'*>; upasiatn  baratuv  D.^j;  —  i^ure^masda-  a.)  absolut:  taünef  .  .  bartntö  (NP.)  «ä"? maiy  ufastam(Stvaz.)  aiara^Sh.i.9usv.;i  ^asiamianti  vasMtd  .  ,  Yt.  10.  20;  — — yaha  ml  barm  upasiam  Yt  13.  t;  5. 63; —  barimnö  vä  vazfituUS  vä  N.  ^',  — hä  mihara  aamala..iA
2.  18;  36.  a)  zugleich  mit  Angabe  des  vä pairi  (vä)  iarvati  N.55;  Vd.7;  — ^r^- wohin?,  a)  durch  Lok.:  ais'qm  ;^ma/em  fy  Bh. 5. 4.  [Zu  bm^araYt.  10.81,  Kon. .  .  *ni6»r/ise   ab?nta  (sd.)    baraiti    Yt  77.  der  NA,,  s.  Sp.  940  u.  und  No.  a8.]
14.  ß)  durch  Praen.:  yesi  sl  zao^r^  mit  aiti  'etwas  (wieder)  hinübertragen, baraiti  avi  ii  mai%an3m  "wenn  er  sich  -bringen  zu  — '  (ava  mit  Akk.):  us  kata die  Z.  zu  seiner  Wohnung  bringt"  Yt  aiibyä  nmanaäbyS  baraym  .  .  Str^m^a  . . 10. 136.  3)  "hervorbringen;  gebären':  iu^a  (sd.)  . .  aä^m  airtm  aiti  barqn  ava barat  daiiihts  V.  2.  ioPüZ.(?
tarn  arstim  barai/iYt.  10.21.  5) '(davon- 1  nanbyB  .  .  V.  77.  4;  —  ydka  ..  am?r7xtim tragen  sva.)  gewinnen;  empfangen':  yänä  avaiaräni  ..  Uta  az?m  apaiaräni  ..  sk- (sd.)  baraiti  astavB  va  .  .  m^nyahe  Yt.  o^m'a  tars/amca  haca  maata  dämaiyS  Yt 14.3^.  a)  mit  refl.  Dat:  paourva  ?ü  g.^i-;  10*; — ya  haca  daevayasnai^yü . . fumS  baraiti  "zuerst
stimme, den  Ruf  erheben,  ertönen  lassen*:  tragen,  abreissen,  zerstören':  apa  aetam yS  mq'^rä  {sd.)  . .  *väcim  baraitT  Y,  50,  6;  \distqm  {sd.)  baraym    apa    a!t>m   taddtum
■  a^ra   väHm   baraiti  .  .  ir.'hiaci  (sd.)  ,  baraym  V.  S.  74,
dby  Google
937
IT-  mit  antan
'bar-  mit  tts
938
mit  antan  'dazwischen  —,  iänem- ^  ft/^nm  vä  gaw^tn  (sd.)  vs  avi  ava^araiti bringen'(?):  xhal  vayüMi  antar?.barilit\V.3.2^.  3)  'etwas  Jemandem  (Gen.) N. 67.  .verursachen':  tßm    ..    mtäsrö-dru/qm    avi
mit  antar?  nnd, paiti  — ?  — :  VJspgm  anAifa^ihyäs»  tamiS%wyqm{sA.)  ava^arahi tan  paiHMaröti  N.  65  "'>.  j  Yt  10. 23.
mit  ava  1)  'hinab-,  hineinbringen':  y5\      mit    a»/    und    a    'etwas   herzubringen »otJ  ft'jW  kar^ä  frakarayäti  ava  iha  ba- '  zu  — '  (Akk.):  yat  .  .   avi  ätr?m  äbannti rtnü  *yavahe  vä  "wenn  man  in  der  Erde  \  affayä  urvarayä  .  .  Yt  i4-  SS- drei  Furchen  rieht  (und)  sie  bringen  (sva,  1     mit  avi  und/rJ:  pas^aiti  avi  Al  iritta- s�
a)  '(Kleider)  herabziehen  sva,  von oben  her,  über  den  Kopf  her  anlegen'; yS  vastra  vastnm  *aiwyaithaysrii  *itzba- rmti  (sd.)  . .  uparat  ftaOnai  ava-bannti  . . N.pJ.  a)  'hinzu-,  herzubringen,  ver- schafien':  *yaoxHayS  ava-bantam  (statt Hur.)  F.  4  g;  —  cvat  gaonahe  (sd.)  ava.- barat  N.  65.  a)  mit  Angabe  des  wohin? oder  wem?,  a)  durch  avi  mit  Abi.:  
hinzubringen  zu  — ,  an  —  hin'  (Akk,)i haoma  .  ,  ya  nasäum  ava.b?r»ta  Y.6. 42 '"'.  5)  'wegtragen,  wegbringen':  ava aS?m  iristfm  baraym  V.8.2;  3.  Un- deutlich P.jA';  s.  unter  hunara-.
mit  *ava"1  und  aw  'Jemandem  (Akk,) etwas  (Akk.)  zubringen,  verschaffen' ;  ^azia"' dim  aviJiarami  aojO  YtÄas;  —  *ava"'> mqm  aviiawryqm  .  .  aojS  .  .  "so  würde ich  mir  verschaffen  . .  die  Kraft  . ,"  Yt.
S.,^.
mit  avi  i)  'herzu-,  heranbringen':  tma^ .  iavana  avi.b»rf/aYi.ll.a\         a)
Aj  paoirfm  yasna  , .  Jrabarsit  Vd. g;  —  avi  . .  har3%r?m  frabarajl  Vd.  2. Wertlos.
mit  a  1)  'an  sich  tragen,  besitzen': ustrahe  .  .  yS  arinqm  .  .  vtasisttm  aojS äbaraiti  Yt  i4- 12;  —  asatam  . .  abar?  (?)  *J' *ahurspu%rs{%d.)  YL/4.59.  3)  'etwas herzubringen,  herbeiholen':  ap3m  ab>r»s (sd.)  S.barat  N.  77,  3)  'Jemanden  hin- zubringen zu  —'  \ä  mit  Akk.) :  visptm  aia- vatutn  vakistpm  ä  ahStn  aiaraiH  P.  24.
mit  upa  i)  'etwas  herzu-,  hinzubringen': barssmqn  upa.baraiti  N.  joj;  VytJ^;  — "hrayqm  *kva  *taHi  (sd.)  upa.barS  ratu- fris  N.  70^;  —  hc^ra  taoxma  upa.bara pasvqmla  ..  V.  2.  25;  271*,  30,  33,  35  f.*, 38.  a)  mit  Dat.  der  Person:  jahikayai ya.  aom  pu%r?m  baraiti  anyahmai  arsanai varitftn  paike  upa.baraiti  ",  .  die  da  das Kind  gebiert,  das  von  
mit  US  \)  'hinaustragen':  ydi  pa%a  utba- nnte  spanasca  irista  ,  .  "wenn  des  Weges hinausgetragen  werden  tote  Hunde  und  . ." V.  S.  14.  a)  'etwas  heraustragen,  heraus- schaffen aus  — ';  a)  mit  Gen.:  iritt^m  uzba- röit  apB  "man  schaffe  den  Toten  aus  dem Akk.  des  wohin?:  3  aisma  yasavuha  afi  Wasser"V. 6. 37.  P)  mit^a^b  undAbl.: mqm  bara  V.  7Ä  19;
raiti"^  %wyqm^a  "er  bringt  Verderben Über  sie  und  Angst"  Yt  70,37.  a) 'ver- teilen an  -'  (Akk.):  avi  dll  alm  .  .  ha- md^a  (sd,)  baraiti  isavS  Yt/o.  101.
mit  avi  und  ava  \)  'etwas  hinzubringen zu  — '  (Akk.):  yB  atr?m  nasupakim  dai- tlm  gatüm    avi    ava.baraiti
ätr?mca  V.  5. 40;  40.  a)  'etwas  weg- bringen, -schaffen' :  us  ..  iarahi  .  .  palma häiriHnqm  Vyt  ^o  (?).  a)  'von  —  weg' (haca  mit  Abt.);  yimtm  .  .y5  uxbarai haca daevaÄbys  iUis^a  saokala  Yt.  ig.  32;  5. 26.  3)  'etwas  hervorbringen,  schaffen',
von  AhM.:  d(>a  aam..  urvarä . ,  uzbanm
85.         2)   'etwas  Jemandem  (Dat)   ver-.V.so.  4; — yqm  (näml.  andvTm)  as?m schalen':  ya%a  na  JryS fiyai  vaniaoe  .  .•uxbaire  (iSPrM.)  Yt  5.  6.         4)    'etwas
dby  Google
939  'bar-  mit  la  und  ni/  —  'bar-  mitjrä  940
Jemandem    (Dat)    darbringen,    weihen':'     mit /aiA' und  «f  Vieder hraausbriogeD,
zae^rä  ta  uzbärayrn '^t.  f.  $B;  —  bansttia  zurückversetzen    in    — '  (Lok.):  yasca    ml
ig uxdäraya/X.ip.  ig,  Vjt.  2 J.        s)'!^'^''  '^^t^m  nanm  qxS {sA.)  ava^pnpttm  ravöAu
der)  herauiziehen  sva.  über  die  Füsse  her  paiti  usbärayai  V.  18. 10.
anlegen':  ys   vastra    z-aitr?m  *aiivyänha-        mit    parä      i)     'wegtragen,     -bringen,
yänli  *iaiannti  aratufryS  uparat  tialmat  -nehmen;  entwenden':  II   adam  tyu*  parä-
ava^annti    aia    aiwySakayanti  ratufryö  bartam  patiyäbaram  (sd)  Bh.i.  14;    14;
"wenn    sie  Kleid   um  Kleid    anlegen    — :  —  tntinm  ..yspara  ratiää  (sd.)  baraiti
```


## [2026-09-07T19:33:04.811Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '16840,16870p' BRT.txt | cut -c1-400 | grep -n -i \"ni.  1)\\|mit  ni\\|nis\\|niä\\|niS\" "
}
```


### [2026-09-07T19:33:04.864Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T19:33:07.439Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '16840,16866p' BRT.txt"
}
```


### [2026-09-07T19:33:07.488Z] TOOL RESULT

```
"wenn    sie  Kleid   um  Kleid    anlegen    — :  —  tntinm  ..yspara  ratiää  (sd.)  baraiti
ziehen  sie  sie  heraufwärts  an,  so  sind  sie  Ytio.  27;  —  yas'a  ..  a^tankam  yai  myat-
ar.,    ziehen  sie  sie  von  oben  her  herab-  danqm  paraiaraiti  N.Öj;  63;  — para..
wäits  an,  legen  sie  sie  so  an,  so  sind  sie  baraAe  Yyt  50  Q).        a) 'von  —  weg' {liatj
r."  a.gj'*'.  Undeutlich:    us.bTbarJmi  mit   AbL):    yassJat  paiti    .  .    kaca    gai-
N.48;  —  uzbarayat  N.  2S.  >äiys  paraiaratH   dasa  (sd.)    V.  13.  10;
mit  »f   und   ms   'etwas    heraustragen,   4o(?).         2)  |  'fortreissen'  vom  Wasser:
-holen  aus  — '    {haca  mit  AbL):    m  kaca  äpisim    (Sp,  329  m.)    paräbar^    Bb.    i.
tutssvö  aitavat  apat  kaca  mibsray?n  "man    19.  3)  'heimtragen,  einheimsen':  vlips
soll  so  viel  (ab  möglich)  vondemLeich-  :^ ar)iitis{^A^ paraiaranV .g.t"} .       4)  'be-
nam   aus   dem  Wasser   herausholen"    V.  seitigen':  ya^ä  gaumät^  ..  vÜam  tyäm
&31.  amäxam  naiy paritiari^'B\i.i.i$.        a)ab-
nüt  paiti  i)  'zurückbringen,  wieder  er-  solut 'eine  Schuld  beseitigen  sva.  sie  wieder
statten',  mit  Dat  der  Person:  yS  naire..  gut    machen':    S/yV  satail  AaiaJvii anain
nöitn^mSisA.) paiti. baraiti y. 4.1.     z)'dar-   (sA)  nar am  para. baraiti  V.4.5.
bringen,  offerre,  opfern':    taoa  yai  paiti.-        wxpairi —  7~:ya^aca pasus.Aaurvänhs
barjttti  yä  ar^dulat  *apaititat  *ajayaurva   aSat    sraaäm    .  .  pairi.barämaiäe  Yt  //.
(Sp.  737  m.)  "so  auch,    wenn   man   dar-  7,        [N.JOj:  lies /airf.*".]
bringt,  was  . ."  N.54;  54  {paiti.baranti);       mit  frä  i)  '(gradum)  proferre,  vonrärts
—  poica  vä  *pairi {Sp.  857  u.;  vä)  *paiH.-  tun':  paoirim  gäma  (sd-J  frabarat  Ä  2.
barS'^  ratu/ris  a.ioj;  —  yai  bar>sma    15;  153,  33,  a) 'hintragen,  hmbringen
a£ö.dräjs  .  .  kvacit  aglahe  paiti.barSit  N.   zu  — '  (il  mit  Akk.):   ta  nara .  .ya  nasäum
yo;  70';  —  *kva  aSam  als mfm  paiti. barät  3pim    ä    vä  atrym   ä  vä  /raiarynti  V.  7.
N. /o_j;  loj  (paiti.barB,  Sp.sasf.),  106,    35; — yö  vTsat ..  sao>rqm*ätrfm  a/raia-
108;—  aal  [mqm\  ^kqmal  (Sp.47of.)  .  .   rü/f' V.^.  i4(?)PüZ.        ä) 'Jemandem  (Dat,
alimanqm  paitiMratti  V. 18.22;    —  >>?  Gen.)  etwas  zutragen,  bringen;  übertragen,
barysmaca  *frast»r»nte  g>usca  paitOaraiti  zu  eigen  geben':  yö  näirikaya  ..  3?ary%»m
```


## [2026-09-07T19:33:19.471Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"nirvana\" AHD_watkins1985.txt | head\necho \"=== we- to blow ===\"\ngrep -n -i \"To blow\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-07T19:33:19.525Z] TOOL RESULT

```
1125:wé-. To blow. Contracted from “*wea-; oldest basic form *gwé- (< *owea-). 1. Suffixed irregular shortened form *we-dhro- in Germanic *wedram, wind, weather, in Old English weder, weather, storm, wind: WEATHER. 2. Suf- fixed (participial) form *wé-nt-o-, blowing, in: a. Ger- manic *windaz in (i) Old English wind, wind: wIND! (ii) Old Norse vindr, wind: wInpow; b. Latin ventus, wind: VENT, VENTAIL, VENTILATE. 3. Suffixed Germanic form *wé-ingjaz in Old Norse vengr, wing, akin to the Scandi- navian source of Middle English wenge, wing: WING. 4. Basic form *wé- in Sanskrit vdti (stem *vd-), he blows: NIRVANA. [Pok. 10. aw/é)- 81.]
1923:NIPPLE nabja- NIRVANA we-
=== we- to blow ===
53:result of descent from a common original. Certain similarities may be accidental: the Greek verb “to breathe, blow,” has a root pneu-, and in the language of the Klamath Indians of Oregon the verb “to blow” is pniw-. Other similarities may reflect univer- sal or near-universal features of human lan- guage: in the languages of most countries where the bird is known, the cuckoo has a name derived from the noise it makes. A vast number of languages around the globe have “baby-talk” words like mama and papa. Fi- nally, languages commonly borrow words and other features from each other, in a whole gamut of ways ranging from casual or chance contact to learned coinages of the kind that English systematically makes from Latin and Greek. But where all of these pos- sibilities must be excluded, the comparatist assumes genetic filiation: descent from a common ancestor, which, in the case of Indo- European, as Sir William Jones surmised almost two centuries ago, no longer exists. In the early part of the 19th century, scholars set about exploring systematically the similarities observable among the princi- pal languages spoken now or formerly in the regions from Iceland and Ireland in the west to India in the east, and from Scandinavia in the north to Italy and Greece in the south. They were able to group these languages into a family which they called Indo-European (the term first occurs in English in 1813, though in a sense slightly different from today’s). The similarities among the different Indo-European languages require us to as- sume that they are the continuation of a single prehistoric language, called Indo- European or Proto-Indo-European. In the words of the greatest Indo-Europeanist, the
321:yawn, gape: BAY2, BEVEL; ABASH, ABEYANCE. 2. Possibly Vulgar Latin *abbaidre (> Old French (a)baiier), to bay: BAY‘*.] [battuere. To beat. Latin verb of unknown origin. (BATE?), BATTER!, (BATTER’), (BATTERY), BATTLE; ABATE, COMBAT, DEBATE, (RABBET), (REBATE?), (RE- BATO).] bel-. Strong. 1. Suffixed o-grade form *bol-iyo- in Russian bol’shoi, large: BOLSHEVIK. 2. Prefixed form *dé-bel-i- (dé-, privative prefix; see de-), “without strength,” in Latin débilis, weak: DEBILITATE, DEBILITY. [Pok. 2. bel- 96.] bend-. Protruding point. 1. Germanic *pannja-, “struc- ture of stakes,” in Old English penn, pen for cattle: PEN2. 2. Germanic *pund- possibly in Old English pund- (> Middle English pound), pundfald, enclosure for stray animals: POND, POUND3; IMPOUND, PINFOLD. 3. Germanic *pin- in Old English pintel, penis: PINTLE. [Pok. bend- 96.) beu-'. Also bheu-. Appears in words loosely associated with the notion “to swell.” I. Root form *beu-. 1. Ger- manic *puk- in: a. Old English pocc, pustule: POCK; b. Old French po(u)che and Old North French poke, bag: POACH!, POCKET, POKE3, POUCH, (PUCKER). 2. Old Eng- lish pyffan, to blow out: puFF. 3. Old English -piite, “fish with large head” (in aele-piite, eelpout): pouT?. II. Root form *bheu- with various Germanic derivatives. 1. Old English bdsm, bosom: Bosom. 2. Old English biic, belly, pitcher: BUCKBOARD. 3. Frankish *biak (> Old French buc), trunk of the body: TREBUCHET. 4. Old English bye), pustule: BorL?. 5. German dialectal baustern, to swell, akin to the source of Middle English bost, a bragging: BoasT!. III. Root form *beu-. 1. Latin bulla, bubble, round object, amulet (> Old French boule and Spanish bola, ball): BILL!, BILLET!, BOLA, BOULE?, BOWL’, (BULL?2), BULLA, BULLATE, BULLET, (BULLETIN); BOULE- VERSEMENT. 2. Latin bullire (> French bouiller), to bubble, boil: BOIL!, BOUILLON, BUDGE!, (BULLION), BULLY?; BOUILLABAISSE, EBULLIENCE, GARBOIL, PAR- BOIL. 3. Possibly Latin bucca (> Old French boucle, buckle, curl, and Spanish boca, mouth), (inflated) cheek: BOCACCIO, BOUCLE, BUCCAL, BUCKLE!, BUCKLE?; DE- BOUCH, DISEMBOGUE, EMBOUCHURE. 4. Greek boubén, groin, swollen gland: BUBO. [Pok. 2. beu- 98.] beu-2. Root imitative of muffled sounds. 1. Latin bitié (perhaps > Old French butor), bittern: BITTERN!. 2. Latin bited, a kind of hawk: BUZZARD. [Pok. 1. b(e)u- 97.] bha-'. To shine. Contracted from *bhas-. 1. Germanic *baukna-, beacon, signal, in: a. Old English béac(e)n, beacon: BEACON; b. Old English denominative bécnan, biecnan, to make a sign, beckon: BECKON. 2. Perhaps Germanic *bazja-, berry (< “bright-colored fruit”), in Old English berie, berige, berry: BERRY. 3. Germanic *bandwa-, “identifying sign,” banner, standard, sash, also “company united under a (particular) banner,” in: a. Spanish banda, sash: BANDOLEER; b. Late Latin ban- dum, banner, standard: BANNER, (BANNERET). 4. Suf- fixed form *bhaw-es- in Greek phds (stem phét-), light: PHOS-, PHOT, PHOTO-; PHOSPHORUS. 5. Extended and suffixed form *bhan-yo- in Greek phainein, “to bring to light,” cause to appear, show, and phainesthai (passive), “to be brought to light,” appear: FANTASY, (PANT), PHANTASM, (PHANTOM), PHASE, PHENO-, PHENOMENON; DIAPHANOUS, EMPHASIS, EPIPHANY, HIEROPHANT, PHAN- EROGAM, (PHANTASMAGORIA), PHOSPHENE, SYCOPHANT, THEOPHANY, (TIFFANY). [Pok. 1 bha@- 104.] bha-2. To speak. Contracted from *bhaa-. 1. Latin fari, to speak: FATE; AFFABLE, (FANTOCCINI), INEFFABLE, IN- FANT, (INFANTRY), PREFACE. 2. Greek phanai, to speak: -PHASIA; PROPHET. 3. Suffixed form in Germanic *ban- wan, *bannan, to speak publicly (used of particular kinds of proclamation in feudal or prefeudal custom; “to proclaim under penalty, summon to the levy, declare
328:bheidh-. To persuade, compel, confide. 1. Probably Ger- manic *bidan, to await (< “to await trustingly, expect, trust”), in Old English bidan, to wait, stay: BIDE; ABIDE, (ABODE). 2. Latin fidere, to trust, confide, and fidus, faithful: FIANCE, FIDUCIAL, (FIDUCIARY); AFFIANCE, (AFFIANT), (AFFIDAVIT), (CONFIDANT), CONFIDE, (CONFI- DENT), (DEFIANCE), DEFY, DIFFIDENT. 3. Suffixed o-grade form *bhoidh-es- in Latin foedus (stem foeder-), treaty, league: FEDERAL, FEDERATE; CONFEDERATE. 4. Zero-grade form *bhidh- in Latin fidés, faith, trust: FAITH, FEALTY, FIDELITY; INFIDEL, PERFIDY. [Pok. bheidh- 117.] bheig-. To shine. An uncertain but plausible root. Greek phoibos, shining: PHOEBE, PHOEBUS. [Pok. bheigz- 118.] bhel-'. To shine, flash, burn; shining white and various bright colors. I. 1. Russian byelii, white: BELUGA. 2. Greek phalaros, having a white spot (> phalaris, coot): PHALAROPE. II. 1. Suffixed variant form *bhié-wo- in Germanic *bléwaz, blue, in Old French bleu: BLUE. 2. Suffixed zero-grade form *bhb-wo- in Latin flavus, golden or reddish yellow: FLAVESCENT, FLAVO-; (FLAVIN), (FLAVONE), (FLAVOPROTEIN). III. Various ex- tended Germanic forms. 1. *blaikjan, to make white, in Old English blécan, to bleach: BLEACH. 2. *blaikaz, shining, white, in: a. Old Norse bleikr, shining, white: BLEAK}; b. Old English biéc, bright: BLEAK?. 3. Ger- manic *blikkatjan in Old High German blécchazzen, to flash, lighten (> German Blitz, lightning): BLITZKRIEG. 4. *blas-, shining, white, in: a. Old English blxse, torch, bright fire: BLAZE!; b. Middle Dutch bles, white spot: BLESBOK; C. Old French ble(s)mir, to make pale: BLEM- Ish. 5. *blend-, *bland-, to shine, dazzle, blind, confuse, in: a. Old English blind, blind: BLIND; (BLINDFOLD), (PURBLIND); b. Old High German blentan, to blind, deceive: BLENDE; Gc. Old English blandan, to mingle: BLEND; d. Old French blond; blond: BLOND. 6. *blenk-, *blank-, to shine, dazzle, blind, in: a. Old English blen- can, to deceive: BLENCH!; b. Old French blanc, white: BLANCH, BLANK, BLANKET; BLANCMANGE. 7. *blisk-, to shine, burn, in Old English blyscan, to glow red: BLUSH. IV. Extended form *bhleg-, to shine, flash, burn. 1. Ger- manic *blakaz, burned, in Old English blxc, black: BLACK. 2. Zero-grade form *bhig- in: a. Latin fulgére, to flash, shine: FULGENT, FULGURATE; EFFULGENT, FOU- DROYANT, REFULGENT; b. Latin fulmen (< “fulg-men), lightning, thunderbolt: FULMINATE. 3. a. Latin flagrdre, to blaze: FLAGRANT; CONFLAGRANT, CONFLAGRATION, DEFLAGRATE; b. Latin flamma (< *flag-ma), a flame: FLAMBE, FLAMBEAU, FLAMBOYANT, FLAME, FLAMINGO, FLAMMABLE; INFLAME. 4. Greek phiegein, to burn: PHLEGM, PHLEGMATIC, PHLEGETHON. 5. Greek phlox, a flame, also a wallflower: PHLOGISTON, PHLOX; PHLOGO- PITE. [Pok. 1. bhel- 118, bheleg- 124, bhleu-(k)- 159.] bhel-2. To blow, swell; with derivatives referring to various round objects and to the notion of tumescent masculinity. 1. Zero-grade form *bhl- in Germanic *bul- in: a. Old English bolla (> Middle English boll), pot, bowl: BOLL, BOWL!; b. Old Norse bolr, tree trunk: BOLE}; c. Old Norse bulki, cargo (< “rolled-up load”): BULK}; d. Old High German bolla, ball: ROCAMBOLE; e. Middle High German bole, beam, plank: (BOULEVARD), BUL- WARK; f. Middle Dutch bolle, round object: BOLL; g. Middle Dutch bille, buttock: BILTONG; h. Swedish *buller-, “round object,” in bullersten, “rounded stone,” boulder, akin to the Scandinavian source of English BOULDER; i. possibly obsolete Swedish bulde, a swelling (see wer-1). 2. Suffixed zero-grade form *bhl-n- in: a. Germanic *bulJ6n-, bull, in Old Norse boli, bull: BULL); b. Greek phallos, phallus: PHALLUS; ITHYPHALLIC.
342:flagitdre, to demand importunately: FLacitious. [Pok. bhlag- 154.] bhlagh-men-. Form, ritual form. Sanskrit brahmd, brah- man-, priest, and brahma, bréhman-, prayer: BRAHMA!, BRAHMAN, (BRAHMIN). [Pok. bhlagh-men- 154.] bhlé-1. To howl. Probably imitative. 1. Germanic suffixed form *blé-t- in Old English b/gtan, to bleat: BLEAT. 2. Germanic suffixed form *b/é-r- in Middle English bleren, to roar: BLARE. 3. Latin flére, to weep: FEEBLE. [Pok. bAlé- 154.] bhié-2, Also bhla-. To blow. 1. Germanic suffixed form *blé-w- in Old English blawan, to blow: BLow!. 2. Ger- manic suffixed form *blé-dram, “something blown up,” in: a. Old English blZdre, blister, bladder: BLADDER; b. Old Norse bladhra (noun), bladder, and bladhra (verb), to prattle: BLATHER. 3. Germanic extended form *blés- in: a. Old English b/ést, a blowing, blast: BLAST; b. Middle Dutch blas(e), a bladder: stncLass. 4. Variant form *bhid- in Latin flare, to blow (> flabellum, fan): FLABELLUM, FLATUS, FLAVOR; AFFLATUS, CONFLATE, (DEFLATE), INFLATE, SOUFFLE. [In Pok. 3. bhel- 120.] bhlei-. To blow, swell. Extension of bhel-2. 1. Germanic *blajjinén-, a swelling, in Old English blegen, a boil, blister: BLAIN. 2. Perhaps in the Germanic source of Old French blestre, a blister: BLISTER. [Pok. 2. bhiei- 156.] bhleu-. To swell, well up, overflow. Extension of bhel-?. 1. Possibly Germanic *b/aut- in Old Norse blautr, soft, wet: BLOAT. 2. Extended form bhleug~- in Latin fluere, to flow, and -fluus, flowing: FLUCTUATE, FLUENT, FLUERIC, FLUID, FLUME, FLUOR, (FLUORO-), (FLUSH2), FLUVIAL, FLUX; AFFLUENT, CONFLUENT, EFFLUENT, (EFFLUVIUM), (EFFLUX), (FLUORIDE), FLUVIOMARINE, INFLUENCE, (IN- FLUENZA), MELLIFLUOUS, REFLUX, SUPERFLUOUS. 3. Zero-grade form *bhlu- in Greek phluein, phluzein, to boil over: PHLYCTENA. 4. Possibly Greek phloos, phioios, tree bark (< “swelling with growth”): PHLOEM. [Pok. bhileu- 158.] bhlig-. To strike. Latin fligere, to strike: AFFLICT, CON- FLICT, INFLICT, PROFLIGATE. [Pok. bhlig- 160.] bhoso-. Naked. Germanic *bazaz in: a. Old English bzr, bare: BARE!; b. Old Swedish and Old Danish bar, bare: BALLAST. [Pok. bhoso-s 163.] bhrag-. To smell. 1. Germanic *brak- in Old High Ger- man bracc(h)o, dog that hunts game by scent: BRACH. 2. Suffixed form *bhrag-ro- in Latin fragrdre, to smell: FLAIR, FRAGRANT. [Pok. bhrag- 163.] bhrater-. Brother, male agnate. 1. Germanic *brdthar- in Old English bréthor, brother: BROTHER. 2. Latin frdter, brother: FRA, FRATERNAL, FRIAR; CONFRERE, FRATRI- CIDE. 3. Greek phratér, fellow member of a clan: PHRATRY. 4, Sanskrit bhratd, bhrdatar-, brother: PAL. [Pok. bhrdater- 163.] bhreg-. To break. 1. Germanic *brekan in: a. Old English brecan, to break: BREAK; b. Old English bréc, a break- ing: BREACH; c. Old High German brehhan, to break, akin to the Germanic source of Italian breccia, breccia: BRECCIA; d. Old French breier, to break: BRAY?; e. Old French brier (dialectal) and broyer, to knead: BRIOCHE. 2. Germanic *brak-, bushes (< “that which impedes motion”), in Old Norse *brakni, undergrowth, akin to the probable Scandinavian source of Middle English brake(n), bracken: BRACKEN, BRAKE’, BRAKE‘, 3. Nasal- ized zero-grade form *bhr-n-g- in Latin frangere, to break: (FRACTED), FRACTION, (FRACTIOUS), FRACTURE, FRAGILE, FRAGMENT, FRAIL!, FRANGIBLE; ANFRACTU- OUS, CHAMFER, DIFFRACTION, (INFRACT), INFRANGIBLE, INFRINGE, OSSIFRAGE, REFRACT, (REFRAIN?), (REFRIN- GENT), SAXIFRAGE, SEPTIFRAGAL. 4, Latin suffrdgdri, to vote for (? < “to use a broken piece of tile as a ballot”), hence suffrdgium, the right to vote: SUFFRAGAN, SUF- FRAGE. [Pok. 1. bhreg- 165.] bhréi-. Also bhri-. To cut, break. 1. Possibly Latin fricdre (> French frotier), to rub: FRAY?, FRICATIVE, FRICTION, FROTTAGE; AFFRICATE, DENTIFRICE. 2. Possi-
760:merk-'. To decay. Latin marcére, to decay, wither: MARCESCENT. [Pok. 1. merk- 739.] [merk-2. Italic root, possibly from Etruscan, referring to aspects of commerce. 1. Latin merx (stem merc-), mer- chandise (> mercdri, to trade): MARKET, (MART), MER- CER, MERCHANT; COMMERCE. 2. Latin merces, pay, reward, price: MERCENARY, MERCY. 3. Probably Latin Mercurius, the god of (inter alia) commerce: MERCURY. [In Pok. merk- 739.]] [merph-. Form. Greek root of unknown origin. 1. Suf- fixed o-grade form *morph-G- in Greek morphé, form, beauty, outward appearance: -MORPH, MORPHEME, MOR- PHO-, MORPHOSIS. 2. Possibly borrowed from Greek morphé, via Etruscan, is Latin forma, form, shape, contour, appearance, beauty: FORM, FORMAL, FORMULA; CONFORM, CORACIIFORM, DEFORM. [In Pok. 2. mer- 733.]] mers-. To trouble. Suffixed o-grade form mors-eyo- in Germanic *marzjan in Old English merran, mierran, to impede: MAR. [Pok. 6. mer- 737.] meu-. Damp; with derivatives referring to swampy ground and vegetation and to figurative qualities of wetness. 1. Extended form *meus- in Germanic *meus-, *mus- in: a. Old English mos, bog: Moss; b. Old Norse mosi, bog, moss, akin to the Scandinavian source of LITMUS. 2. Germanic suffixed form *meuz-i- in Old Norse myrr, bog: MIRE; (QUAGMIRE). 3. Suffixed zero-grade form *mus-to- in Latin mustus, new, newborn (< “wet”): MUST’, MUSTARD. 4. Possibly suffixed extended zero-grade form *mii-ro- in Greek murios, countless (< “flowing, endless”): MYRIAD. 5. Possibly suffixed ex- tended zero-grade form *mud-so- in Greek musos, un- cleanness: MYSOPHILIA, MYSOPHOBIA. [Pok. 1. meu- 741.] meue-. To push away. Latin movére, to move (> mobilis, neuter mobile, fickle, changeable): MOB, MOBILE, MO- MENT, (MOMENTOUS), MOMENTUM, MOSSO, (MOTIF), MO- TION, MOTIVE, MOTOR, MOVE, MOVEMENT; COMMOTION, EMOTION, PROMOTE, (REMOTE), (REMOVE). [Pok. 2. meu- 743.) meug-'. To act surreptitiously. Germanic *muk- or Celtic *mug- in Old French muchier, to skulk: MOOCH. [Pok. 1. meug- 743.] meug-2. Slimy, slippery; with derivatives referring to various wet or slimy substances and conditions. Enlarged form of meu-. 1. Nasalized form *mu-n-g- in Latin mungere, to blow the nose: EMUNCTORY. 2. Possibly Germanic *(s)mug-, referring to wetness and also to figurative slipperiness: a. Old English smoc, shirt: smock; b. Middle High German smuck, “clothing,” adornment, jewel: scHmMuCK; c. Old Norse mugga, driz- zle, akin to the source of Middle English muggen, to drizzle: MuGGY; d. Low German smukkelen, smuggeln, to smuggle (< “to slip contraband through”): SMUGGLE; e. Middle Low German smucken, to adorn (< “to make sleek”): SMUG; f. Old Norse mygla, mold, mildew, akin to the source of Middle English molde, mold: MOLD®. 3. Ger- manic *meuk- in Old Norse mjikr, soft: MEEK. 4. Variant form *meuk- in Latin miicus, mucus: MOIST, MUCILAGE, MUCO-, MUCUS, (MUSTY). 5. Zero-grade variant form *muk- in: a. Greek mukés, fungus, mushroom: -MYCETE, MYCO-; STREPTOMYCES, (STREPTOMYCIN); b. suffixed form *muk-so- in Greek muxa, mucus, lamp wick (< “nozzle of a lamp” < “nostril”): MATCH2, Myxo-. [Pok. 2. meug- 744.] mezg-'. To dip, plunge. 1. Latin mergere, to dip, dive: MERGE; EMERGE, IMMERSE, SUBMERGE. 2. Latin mergus, diver (water bird): MERGANSER. [Pok. 1. mezg- 745.] mezg-*. To knit. Germanic “mésk- in Middle Dutch a maesche, knitted fabric: MESH. [Pok. 2. mezg- 746. [mimos. A mime. Greek noun of unknown origin. MIME, MIMESIS, MIMIC.] [miser. Wretched, unfortunate. Latin adjective of un- known origin. MISER, MISERABLE, MISERY; COMMISER- ATE.]
828:fixed o-grade form *pozk-itd in Germanic *faihithé in Old French faida, hostility, feud: FEUD!. [Pok. 2. peig-795.] peis-'. To crush. 1. Suffixed zero-grade form *pis-to- in Latin pistillum, pestle: PESTLE, PISTIL. 2. Nasalized zero-grade form *pi-n-s- in Latin pinsdre, to pound: PISTON. 3. Possibly suffixed form *pis-lo- in Latin pilum, javelin, pestle: PILE?. 4. Perhaps Greek ptissein (pt- for p-), to crush, peel: PTISAN, (TISANE). [Pok. 1. (peis-2), pis- 796. peis-2. To blow. Germanic “fis- in Old Norse fisa, to fart, akin to the Scandinavian source of Middle English fise, fart: F1zGIG. [Pok. 2. peis- 796.] peisk-. Fish. Zero-grade form *pisk-. 1. Suffixed Ger- manic form “fisk-a- in: a. Old English fisc, fish: FISH; b. Middle Dutch vische, vis, fish: WEAKFISH. 2. Suffixed form “pisk-i- in Latin piscis, fish: PISCARY, PISCATORIAL, PISCES, PISCI-, PISCINA, PISCINE; GRAMPUS, PORPOISE. [Pok. peisk- 796.] pek-'. To make pretty. 1. Possibly Germanic “fagra- in Old English feger, beautiful: FAIR}. 2. Possibly Germanic *fagin-, *fagan-, to enjoy, in Old English fegen, joyful, glad (> fagnian, to rejoice): FAIN, FAWN}. [Pok. 1. pek- 796.] pek-?. To pluck the hair, fleece, comb. 1. Extended form *pekt- in Germanic *fehtan, to fight, in Old English feohtan, to fight: FIGHT. 2. Suffixed extended form *pekt-en- in: a. Latin pecten, a comb: PECTEN; b. zero-grade. form *pkt-en- in Greek kteis (genitive ktenos < *pktenos), a comb: CTENIDIUM; CTENOID, CTENOPHORE. [Pok. 2. pek- 797.] peku-. Wealth, movable property. 1. Germanic *fehu- in: a. Old Norse fé, property, cattle: FELLOW; b. Old French fie, fief: FEE; c. Medieval Latin feudum, feudal estate: FEUD?; INFEUDATION. 2. Suffixed form “peku-n- in Latin peciinia, property, wealth: PECUNIARY; IMPECUNIOUS. 3. Suffixed form *peku-l- in Latin peciilium, riches in cattle, private property: PECULATE, PECULIAR. [In Pok. 2. pek- 797.] pekv-. To cook, ripen. 1. Assimilated form (in Italic and Celtic) *kvekw- in Latin coquere, to cook: COOK, CUISINE, (CULINARY), KILN, KITCHEN, QUITTOR; APRICOT, BISCUIT, CONCOCT, DECOCT, PRECOCIOUS, RICOTTA. 2. Greek pe- pon, ripe: PEPO. 3. Greek peptein, to cook, ripen, digest (> peptos, cooked): PEPTIC; DRUPE, EUPEPTIC, PEPSIN, PEPTONE, PUMPKIN. 4. Greek -pepsia, digestion: DYSPEP- sia. 5. Sanskrit pakva-, ripe: PUKKA. [Pok. peky- 798.] pel-1. Dust, flour. 1. Latin pollen, fine flour, dust: PoL- LEN. 2. Latin pulvis, dust: POWDER, PULVERIZE. 3. Latin palea, chaff: PAILLASSE, PALEA. 4. Greek palunein, to sprinkle flour: PALYNOLOGY. 5. Greek poltos, porridge (made from flour), probably borrowed via Etruscan into Latin as puls, pottage: POULTICE, PULSE?. [Pok. 2 b. pel- 802.] pel-2. Pale. 1. Suffixed variant form *pal-wo- in: a. Ger- manic *falwaz in Old English fealu, fealo, reddish yellow: FALLOW DEER; b. Latin pallére, to be pale: PALE, PAL- LID, PALLOR; APPALL; C. Latin palumbés (influenced in form by Latin columbus, dove), ringdove, “gray bird”: PALOMINO. 2. Suffixed form “pel-ko- probably in Ger- manic *falkén-, falcon (< “gray bird”), in: a. Old French girfaut, gyrfalcon: GYRFALCON; b. Late Latin falcé, falcon (but Germanic *falkén- is also possibly from the Late Latin): FALCON. 3. Suffixed extended form *peli- wo- in: a. Greek pelios, dark: PELOPS; b. o-grade form *poli-wo- in Greek polios, gray: POLIOMYELITIS. 4. Per- haps Greek pelargos (< *pelawo-argos), stork (< “black- white bird”; argos, white; see arg-); PELARGONIUM. [Pok. 6. pel- 804.] pel-3. To fold. 1. Extended o-grade form *polt- in Ger- manic *falthan, *faldan in: a. Old English fealdan, faldan, to fold: FoLD!; b. Old High German faldan, to fold: FALTBOAT; Cc. Germanic compound “*faldistélaz, “folding stool” (*stdlaz, stool; see sta-), in Medieval Latin compound faldistolium, folding chair: FALDSTOOL;
872:+ esse, to be; see es-): POSSIBLE, POTENT; (IMPOTENT), PREPOTENT. 3. Form *pot- in: a. compound *ghos-pot-, “suest-master,” host (see ghos-ti-); b. compound *dems-pot-, “house-master,” ruler (see deme-'). 4. Old Persian pati-, master: PADISHAH. [Pok. poti-s 842.] [prak-. To make, do. Greek root. Greek prassein (Attic prattein), to effect, do: PRACTICAL, (PRACTICE), PRAG- MATIC, PRAXIS. [In Pok. 1. per 811.]] prek-. To ask, entreat. 1. Basic form *prek- in Latin *prex, prayer (attested only in the plural precés), with denominative precdri, to entreat, pray: PRAY, PRAYER?, PRECARIOUS; DEPRECATE, IMPRECATE. 2. Suffixed zero-grade form *prk-sk- becoming *pork-sk-, contracted into *posk- in suffixed form *posk-to-, contracted into *posto-, which appears in Latin postuldre, to ask, re- quest: POSTULATE; EXPOSTULATE. [Pok. 4. perk- 821.] prep-. To appear. Suffixed zero-grade form *prp-yo- in Germanic *furbjan, to cause to have a (good) appearance, polish, in Old French fo(u)rbir, to polish, burnish: FuR- BISH. [Pok. prep- 845.] preu-. To hop. 1. Zero-grade form *pru- in Germanic *fru- in Old English frogga (with obscure expressive suffix -gga), frog: FROG. 2. Extended o-grade form *prowo- in Germanic *frawaz in: a. Middle Dutch uro, “leaping with joy,” happy: FROLIC; b. Old High German fré, happy, in frewida, joy (> German Freude): scHa- DENFREUDE. [Pok. preu- 845.] preus-. To freeze, burn. 1. Germanic *freusan, to freeze, in Old English fréosan, to freeze: FREEZE. 2. Suffixed zero-grade form *prus-to- in Germanic *frustaz, frost, in Old English forst, frost, frost: FROST. 3. Suffixed form *preus-i- in Latin *preusis, *preuris, act of burning, whence denominative pririre, to burn, itch, yearn for: PRURIENT, PRURIGO, PRURITUS. 4. Suffixed zero-grade form *prus-ina in Latin pruina, hoarfrost: PRUINOSE. [Pok. preus- 846.] pri-. To love. Contracted from *pria-. 1. Suffixed form *priy-o- in Germanic “frijaz, beloved, belonging to the loved ones, not in bondage, free, in: a. Old English fréo, free; FREE; b. Dutch vrij, free: FILIBUSTER. 2. Suffixed (participial) form “priy-ont-, loving, in Germanic ‘“fri- Jjand-, lover, friend, in Old English friond, fréond, friend: FRIEND. 3. Suffixed shortened form *pri-tu- in Germanic *frithuz, peace, in: a. Old High German fridu, peace: SIEGFRIED; b. Old French esfreer, to disturb: AFFRAY; c. Germanic *frij-, peace, safety, in compound *berg-frij-, “high place of safety” (see bhergh-?). 4. Suffixed femi- nine form *priy-G, beloved, in Germanic *frijj6, beloved, wife, in: a. Old Norse Frigg, goddess of the heavens, wife of Odin: Fricc; b. Germanic compound “*frije-dagaz, “day of Frigg” (translation of Latin Veneris diés, “Ve- nus’s day”), in Old English frigedeg, Friday: FRIDAY. [Pok. prdi- 844.] prokto-. Anus. Greek prokios, anus: PROCTITIS, PROCTOL- OGY, PROCTOSCOPE. [Pok. prdkto- 846.] pster-. Also ster-. To sneeze. Imitative root. 1. Suffixed form *ster-nu- in Latin sternuere, to sneeze: STERNUTATION. 2. Suffixed form *ster-t- in Latin ster- tere, to snore: STERTOR. [Pok. pster- 846.] pu-'. Also phu-. To blow, swell. Imitative root. 1. Ex- tended form *pus- in Latin pustula, a bubble, blister: PUSTULE. 2. Perhaps extended form “pit-, penis, in Latin praepiitium, foreskin (prae-, before, in front; see per’): PREPUCE. 3. Variant form *phi- in Greek phusa (> phusan, to blow), bellows, bladder: EMPHYSEMA, PHYSO- STIGMINE, PHYSOSTOMOUS. [Pok. 1. pu- 847.] pu-2, To rot, decay. 1. Suffixed form *pi-lo- in Germanic *filaz, rotten, filthy, in: a. Old English fi, unclean, rotten: FOUL; b. Old Norse fill, foul, akin to the Scandi- Navian source of FULMAR; ¢. Germanic abstract noun *filithd in Old English fylth, foulness: FILTH; d. Ger- manic denominative *filjan, to soil, dirty, in Old English fylan, to sully: FILE’; DEFILE!. 2. Extended form *pug- in Germanic *fuk- in Icelandic fiki, rotten sea grass, and
1125:wé-. To blow. Contracted from “*wea-; oldest basic form *gwé- (< *owea-). 1. Suffixed irregular shortened form *we-dhro- in Germanic *wedram, wind, weather, in Old English weder, weather, storm, wind: WEATHER. 2. Suf- fixed (participial) form *wé-nt-o-, blowing, in: a. Ger- manic *windaz in (i) Old English wind, wind: wIND! (ii) Old Norse vindr, wind: wInpow; b. Latin ventus, wind: VENT, VENTAIL, VENTILATE. 3. Suffixed Germanic form *wé-ingjaz in Old Norse vengr, wing, akin to the Scandi- navian source of Middle English wenge, wing: WING. 4. Basic form *wé- in Sanskrit vdti (stem *vd-), he blows: NIRVANA. [Pok. 10. aw/é)- 81.]
1165:wet-'. To blow, inspire, spiritually arouse. Related to wé-. 1. Lengthened-grade form *w6t- in Germanic suffixed form *wéd-eno-, *wéd-ono-, “raging,” “mad,” “inspired,” hence “spirit,” name of the chief Teutonic god, in: a. Old English Woéden, Woden: WoDEn; b. Old English Wod- nesdxg, ““Woden’s day”: WEDNESDAY; Cc. Old Norse Odhinn, Odin: Opin; d. Old High German Wuotan (> German Wotan), Wotan: WoTAN. 2. Lengthened variant form *wdt- in Latin vdtés, prophet, poet: vaTic. 3. Suf- fixed variant form *wat-no- in Latin vannus, a winnow- ing fan: FAN!, vAN3. 4, Oldest basic form *awet- becoming *awet- in suffixed form *awet-mo- in Greek atmos (< *aetmos), breath, vapor: ATMOSPHERE. [Pok. udé- 1113.]
```


## [2026-09-07T19:33:31.480Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('POK_01.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint('leaves',len(leaves))\nfor i in (318,319,320,321):\n    print('=== leaf',i,'===')\n    print(leaves[i][:2500])\nEOF"
}
```


### [2026-09-07T19:33:32.678Z] TOOL RESULT

```
leaves 364
=== leaf 318 ===
.  elteur)  »feuchte Niederung'.  Dazu  altnord.  Uldna  ,schimmeln',  ahd.  oltar  »Schmutzkrume*, wohl  auch  anord.  ylda  »Moderduft*.
zn-Formantien  finden  sich  in:
norw.  dial.  ulma  .schimmeln'»  ndd.  ostfries.  olm,  ulm  »Fäulnis,  bes.  im Holz*,  mnd.  ulmich  ,von  Fäulnis  angefressen',  mhd.  ulmic  ds.;  lit.  elmes, almens  »die  aus  der  Leiche  fließende  Flüssigkeit*.
^^-Erweiterung  liegt  in  arm.  alb  »Dreck'  vor.
WP.  I  152  f.,  WH.  I  28  f.»  Petersson  Heterokl.  165  f.
20
306  s
f     .  ■     i
4.  el-,  ol'  Schallwurzel.  •
Arm.  almuk  ,Lärm,  Aufruhr  usw.*  (*lmo-),  alavC-lh  ,Flehen*,  olb  »Klao-^t  I ololh  , inständige  Bitte';  *  .    f
gr.  ololvg  , Heuler,  weibischer  Mensch',  öXolvyr}  , Klagegeschrei*,  ölom^^      \ v6g  »jammernd',  dlocpvQo^ai  ,jammere';  vielleicht  auch  k'lsyog  n.  , Klagelied« elsog  m.,  später  n.  , Mitleid';
asl.  jahnr^  ,Lärm',  jalma    ,strepere,    Stridore,    crepare',   norw.    mdartl jalm^  jelm  , Schall',  schwed.  mdartl.  jalm  , Schrei,  Mißlaut*;  norw.  mdartl alka  , Händel  anfangen*,  ostfries.  ulken  »Unwesen  treiben,  schreien,  spottea    •''•• höhnen'  (nhd.  ulken),  schwed.  dial.  alken  ,zu  knurren  anfangen';  /•■^r
lit.  nualdeti  »erschallen',  algöti  , zusammenrufen,  nennen';
vielleicht  gehören  auch  die  Namen  für  Wasservögel  von  einer  Wz.  el hierher  (doch  s.  S.  304);  etwas  verschieden  ist  der  Gefühlswert  von  uU,
WP.  I  153  f.,  Pisani  Armen.  8  f.
5.  el-,  Ol-  , vernichten»  verderben'??
Arm.  eiern,  Gen.  eiefan  »Unglück*;  olorm  , unglücklich*;
gr.  b'llvuL  , verderbe'  (*ol-vv-(i.L),  Fut.  dXeao),  Perf.  dX(bXsY.a  (älter  intrans] ^lü)Xa)  usw.,  nach  Schwjzer  Gr.  Gr.  I  747  dl-  statt  *il~  nach  dem  Kausat*^ *dX6w',  öle/.iü  , vernichte*,  iJXs&gog  m.  , Verderben*;
nach  Loth  (RC  40,  371)  hierher  mbret.  el-hoet , Hunger'  (zu  hoet  ,Nahrung').  "^j bret.  (Vannes)  ol-huid  , Nahrungsmaugel',  ol-argant  , Geldmangel'  usw.^'^ vielleicht  auch  air.  el-tes  ,lauwarm'  {tes  , Hitze');
über  lat.  aboleö  s.  WH.  I  4 f.;  ob  el-  den  Wurzeln  elg-,  elk-  zugrunde' liegt?
eventuell  hitt.  hu-ul-la-a-i  »er  besiegt,  vernichtet*,  Couvreur  g  134 L/ anders  Hendriksen,  Laryngaltheorie  27»  47.  :\
WP.I159f.»  Schwyzer  Gr.  Gr.  1361,  363,696,  747,  Petersson  Heterokl.  159.
6.  el-,  elQ-ilä-]  el-eu-(dh')  , treiben,  in  B
=== leaf 319 ===
ewegung  setzen;    sich  bewegen,
gehen'.
Arm.  eianim  ,ich  werde',  Aor.  1.  Sg.  eU  (*ehi),  2.  Sg.  ehr,  3.  Sg.  eieu-, elanem  ,ich  steige  hinauf,  komme  heraus',  3.  Sg.  Aor.  el;  dazu  eluzi  ,j'ai fait  monter'  (*el-ou-ghe-),  danach  eluzanem  ,je  fais  sortir';
gr.  ila-  im  Imper.  koisch  iXdrw,  Fut.  iXävTc  {*£XaovTt)y  Aor.  iXdaavrsg und  poet.  iXdco  , treibe';  suppletiv  zu  &/o)  (s.  unten  kelt.  el-),  Fut.  att.  iXßf Aor.  IrjXaaa;  meist  äXavvio  ,treibe,  fahre'  (von  einem  Nomen  *^Xa-vv-ogy Brugmann  Grundriß  H,  1,  321);
mit  dh-Erweiterung  , kommen' :  Aor.  '^Xdov  (aus  ^Xvd'Ov)^  daraus  dor.  ustv. 'ijv&ov]  Perf.  hom.  elXrjXov&a,  att.  iXrjXv&cc]  Fut.  ion.  iXsucrof^ai]  über  Perf. iXrjXvf.isv  (*elu-),  Adjekt.  Ttgoa-i^XvTog  »einer,  der  kommt',  e'ftrjXvg,  -vöog  ds.^ s.  Schwyzer  Gr.  Gr.  I  704 2,  769^;
307
man  stellt  noch  hierher  iallu)  ,schicke,  werfe'  (*i-J-iö),  Aor.  hom.  ^Xa, dor.  t'ß^«  (Schwyzer  Gr.  Gr.  I  648,  717);  aber  ai.  lyarti  ,er  erregt'  gehört eher  zu  1.  er--^
air.  lu^d  ,ging'  (*hidh-e),  3.  PI.  lotar  {Hudh-ont-r)]  wie  im  Gr.  wird i,n  Kelt.  ag-  , treiben'  durch  el-  suppliert,  womit  aber  zum  Teil  auch  die ^Vurzel  'pel-  ,pellö'  (s.  dort)  zusammengefallen  ist,  so  gewiß  im  air.  Fut. thlaid  ,wird  treiben'  (aus  *pi-plä-s.e-ti),  Fut.  sek.  di-eblad  , würde  entreißen'; gl-  erscheint  im  Brit.  nur  im  Konjunktiv:  Fräs.  l.  Sg.  mcymr.  el{h)wyf, 3.  Sg.  el,  Corn.  1.  Sg.  yllyf,  3.  Sg.  ello,  mbr.  3.  Sg.  me  a  y-el  ,ich  werde crehen*  (das  y  ist  hiatustilgend ;  Ih  und  II  gehen  auf  ^4-intervok.  s  zurück); vielleicht  hierher  die  gall.  FIN  Elaver  >  Elaris  >  frz.  Allier  {*eb-uer-  : *eld-iten-,  s.  oben  ilavvw)  und  Elantia  >  nhd.  Elz]
vielleicht  dazu  als  no-Partizip  (??)  ags.  lane,  -u  f.  , Gasse,  Weg',  anord. l^n  , Häuserreihe',  usw.  Über  anord.  elta  , drücken,  verfolgen,  forttreiben' i*alatjan?)  s.  Falk-Torp  m.  Nachtr.
\VP.  I  155  f.,  Meillet  BSL.  26,  6  f.,  Schwyzer  Gr.  Gr.  I  213,  507,  521  ^ G81f.
p  eh  elQ-,  mit  -ic-Er Weiterung  elk-,  elak-  , hungrig,  schlecht'  (?).
Air.  elc  ,böse'  (aber  olc  ds.,  Gen.  uilc  setzt  *ulko-  voraus!);  über lat.  ulciscor  s.  unter  elkos-]
vielleicht  anord.  illr  ,böse'  (*elhila-)-
lit.  dlkti,  lett.  alkt  (daneben  s-alkt)  , hungern'  (*ohk-),  apr.  alklns,  lit. dlkanas  ,nü
=== leaf 320 ===
st  Bezeichnungen  für  , Ellenbogen'  und ,Elle':
Gr.  wXsvT]  , Ellenbogen',  wA-^v,  -svog  ds.;  (hXeyigavov  (aus  d)Xevo-y.Qavov durch  Ferndissimilation,  vgl.  Brugmann  Ber.  d.  sächs.  Ges.  d.  W.  1901, 31  ff.)  , Ellenbogenkopf';  (hllov  tt^v  tov  ßgccxlovog  xa/fTn^v  Hes.;
lat.  ulna  (aus  *olina)  , Ellenbogenknochen,  der  ganze  Arm*;
air.  uilenn  , Winkel',  mir.  uillind  , Ellenbogen,  Winkel*  {-II-  aus  -In-  der synkopierten  Kasus,  vgl.  Pedersen  KG.  II  59),  cymr.  eliiij  acorn.  elin, Hret.  Hin  , Ellenbogen'  {*olina)]
den  gleichen  langen  Mittelvokal  zeigt  das  Got.:  aleina  ,Elle',  doch liaben  die  übrigen  germ.  Formen  kurzen  Mittelvokal:  ags.  ein  (engl,  eil),
20*
308  •
ahd.  elina,  mhd.  elline,  eine,  nhd.  Elle;  das  Altnord,  zeigt  FormenbuntheiK    • aisL  selten  alen  (anorw.  auch  alun)  mit  erhaltenem  Mittelvokalt,  sonst  n}^ ein  {(fln,  äln)\
einfache  Wurzel  *üU-  in  ai.  aratni-Tj.  m.  ^Ellenbogen',  av.  arddna-  ds.  yVg rä^ni-  ,Elle',  apers.  arasnis  ds. ;
in  alb.  ZeVe  geg.  laus  ,Arm  vom  Ellenbogen  bis  zur  Hand'  {*len^. doch  vgl.  Pedersen  KZ.  33,  544)  fehlt  der  anlaut.  Vokal.  *
B.  Die  gleiche  Wz.  steckt  weiterhin  in:  ai.  äni-h  m.  , Achsennagel,  Beinteü über  dem  Knie*  (*ärni-,  idg.  *elni-  oder   *ölni-),    aräla-h    .gebogen*,  ärtm'- jBogenende',    wohl    auch    in    alaka-   , Haarlocke',   vielleicht   in    äla-valati^. jVertiefung   um    die  Wurzel   eines   Baumes,    um   das   für   den   Baum  b^'^ stimmte  Wasser  einzufangen';
arm.  oin  (Gen.  oiin)  ,Rückenwirbel,  Rückgrat,  Schulter*,  ulu  ,RückgraL Schulter'  (aus  idg.  *olen,  bzw.  *ölen)',  weiter  arm.  aiein  (Gen.  aieian) , Bogen,  Regenbogen',  il  (Gen.  iloy)  ,&'r^axTos,  Spindel,  Spille'  (*ß^o-),  iZi^da.'
cymr.  olwyn  (*oleina)  ,Rad';
germ.  ablaut.  Huni-  in  ahd.  as.  mhd.  Zitn  , Achsennagel,  Lünse',  nbcL Lonnagel,  vgl.  ahd.  luning  , Lünse',  ags.  lyni-hor  , Bohrer*,  woneben  eine s-Ableitung  ags.  lynis,  asächs.  lunisa,  mnd.  liins(e),  nhd.  Lünse]
lit.  lufis  , Achsennagel'  (Specht  Dekl.  100,  125,  163);
abg.  lanita  ,Wange'  {*olnita).
C.  Weiterbildung  ^1-eq-:
1.  In   Bezeichnungen    für   Ellenbogen,  Arm,   gelegentlich   auch   andere^ Körperteile:
Arm.  ololt  ^Schienbein,  Bein^  (*eloq-  oder  *oloq-);
gr.  [äl^  xat]  ^Xa^'  nrjxvgj  l^&aixdvcov  Hes.;
lit.  üolektis  t,  lett.  uolekts  ,Elle^  (ursp
=== leaf 321 ===
)  ,talus^
2.  Gr.  Xo^ög  ,verbogen,  verrenkt,  schräg'  (mir.  lose  ,lahm'),  XixQ^^i ,schief,  quer'  (*A€Xö'-^tog),  XixQi^g  ^quer',  XiY.QLq)ig  ,quer'  (diss.  aus  *Xi%Qi(pk} Saussure  MSL.  7,  91,  Hirt  IF.  12,  226 ;  das  i  der  1.  Silbe  wohl  eher  aus e  assimiliert  als  mit  i  =  «,  wie  allerdings  : )  Xlxqol  Hes.  neben  XeytQol  ,die Zinken  des  Hirschgeweihs',  Xl^,  Xly^  *  nXdyiog  Hes.,  als  ,Einbiegung,  Mulde Xiytog  n.,  Afxtg,  Xsyiccvr}  , Mulde,  Schüssel';
cymr.  llechwedd , Abhang,  Neige',  gall.  Lexoviij  Lixovii  VN;  mir.  lose  ,lahm'; lat.    licinus   ,krummgehörnt   (aus    Hecinos),    lanx,    -eis   ,Schüssel'    (wohl auch  laeus  usw.,  s.  *laqu-)]
ganz   fragwürdig   ist   die   Deutung   von   abg.  lono  ,Busen,  Schoß'  usw.
309
aus  Hoq-s-no-  _,Einbieguiig^,   ebenso    die   von   bulg.  lönec   usw.   ,TopP   aus loq-s-no-  (s.  Berneker  732).
p.  Zu  l^i-  ^biegen^  gehören  auch:
Vielleicht  got.  undarleija  ^unterster,  geringster^;
lett.  leja  ,l!sX,  Niederung^^  lejs  ^niedrig  gelegen'.
1.  Mit  122-Suf fixen:
vermutlich  gr.  leLy,d)v  ^Wiese^  (;*Niederung,  Einbuchtung'),  At^Tyv  , Hafen', thess.  ,Markt'  (,*Bucht'),  li^vri  ,See,  Teich'  G*Vertiefung,  eingebogene Niederung');
cymr.  ZZu??// , Ulme'  (*lei-mä),  nir.  ON  Liamhain  (zu  Hlamh  ds.),  vielleicht schwundstufig  mir.  Um  ds.  [Himo-),  nir.  ON  Leamhain  (falls  nicht  aus Hemo-,  s.  unter  1.  eZ-);
lat.  llmus  ^schief,  llmiis  ,der  schräg  mit  Purpur  besetzte  Schurz  der Opferdiener',  hmes  -iüs  ,Querweg,  Rain,  Grenzlinie  zwischen  Äckern',  osk. liimitum  ,limitum',  llmen  , Türschwelle'  (,*Querbalken');
anord.  limr  (w-St.)  f.  , Glied,  dünner  Zweig'  (,*biegsam'),  lim  f.  ds.,  lim n,  ,die  feinen  Zweige,  die  das  Laub  tragen',  ags.  lim  n.  ,Glied,  Zweig', hochstufig  anord.  llmi  m.  ,Reisbund,  Besen'  (lit.  liemuo  m.  ,Baumstamm, Körperstatur',  ursprüngl.  ,Rundholz,  Rundung'?).
2.  Mit  r-Suffix:  vielleicht  alb.  klir-te  ,Tal'  aus  Präf.  ke-\-li-r,
3.  Mit  f-Suffixen:
lat,  lituus  ,Krummstab  der  Auguren;  krummes  Signalhorn  im  Kriege, Zinke'  (auf  einem  *li-tu-s  ,Krümmung'  beruhend);
got.  lipus  , Glied',  anord.  lidr  (w-St.)  , Gelenk,  Glied,  Krümmung,  Bucht^,
ags.  lidj  liodu-  m.,  as.  Utk  ,Gelenk,  Glied',  ahd.  lidj  mhd.  lit,  lides  m.  n.
.    ,ds.,  Teil,  Stück'  (s-St.),  wozu  anord.  lida  ,beugen',  ags.  älidian  ,zerglied
```


## [2026-09-07T19:33:48.175Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"ni-, nei-\\|nei-, ni-\\|ni\\.  ,nieder\\|,nieder'\" POK_01.txt POK_02.txt POK_03.txt | head -20\necho \"=== POK_full ni ===\"\ngrep -n \"^ni-\\|nizu\\|niz-\" POK_full.txt | head -20"
}
```


### [2026-09-07T19:33:48.244Z] TOOL RESULT

```
POK_03.txt:80:Lok.  PL),  Gen.  Sg.  aks-n-dh  usw.,  Nom.  Du.  aksi  =  av.  ah  ,die  (beiden)  "^^ Augen'  (vgl.  *ofö-  ds.  in  lit.  aH,  abg.  o<fz  und  als  Grundlage  von  arm.  ac-i^  _ und  gi\  liaas),  Bildung  vom  kons.  St.  *aks-]  dieser  St.  ahs-  auch  in  ved.  an-"(ijb  r ,blind';   av.  rtsi   für  *axn  nach  wsi  ,Ohren',   vgl.  av.  aiwy-äxsayeinti  ,sie beaufsichtigen',  aiwyäxstar-  , Aufseher' ;  redupl.  ai.  iJcsate  ,sieht'  (idg.  *iiu, aus  *i-oÄ;^);  aksd-   m.  , Würfel',   d.  i.   ,mit  Augen  versehen';  ksana-  m.  n. , Augenblick'   (scheint  aus  einem   Lok.   *[a]ksdn  erwachsen);    nicht   über- gewuchert ist  der  /)-St.  in  die  verdunkelten  Komposita  ai.  prdtika-  ,zuge- wandt,   entgegengesetzt',  n.  , Antlitz'  (:  nQoa-tjnov),   dnlka-   n.  ,das  Zuge- kehrte, Vorderseite',  av.  ainlka-  m.  ,Antlitz'  (*proti,  '^eni  +  ^fc"- ;  vgl.  slav. nich  unter  *m-  ,nieder'),  ghrtäcl  f.  ,fettig  (aussehend) ;    Opferlöffel',  svitid f.  ,glänzend';
POK_01.txt:4594:ni-,  nei'  ,nieder',  Komparativ  nitero-  ,nieder'  (im  Gegensatz  zu  ,oberer'):
POK_01.txt:4597:arm.  ni-,  n-  ,nieder';  ;!fj
POK_02.txt:1038:gr.  x&tbv  f.  ,Erdboden'  (*x^a>u ;  danach  mit  v  auch  Gen.  xd-ovog,  xd^öviog ,unterirdisch'  usw.),  xaixal  ursprüngl.  ,zur  Erde  hin',  dann  auch  ,auf  der Erde'  (bis  auf  die  andere  Vokalstufe  =  apr.  semmai  ,nieder'  und  vermut- lich auch  =  lat.  huml  ,zu  Boden'),  xai.iaC,s  ,zur  Erde  nieder',  xf^l-^V^og , niedrig',  %d-aixal6g  ,niedrig'  ( :  lat.  humilis),  vielleicht  veo-xi-^os  .neu,  uner- hört  (auf   der   Erde?)';
=== POK_full ni ===
10821:ni-s, or with o-gradation as gr. cpajvn?); Old English M/5/7'brag, boast' (as Latin forirovn 
14115:ni-bar possibly not yet?', Konj. "if not',ya-i6'5/"if'. Old High German ibu, oba. Middle High 
63049:Root / lemma: niz-do- {*he- niz-do-) 
72522:ni-zd-os, -o/77'nest' (prefix /?/■ "low, base', or 'ein-' as "place zum Nieder- or Einsitzen'):
```


## [2026-09-07T19:33:52.806Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '4590,4625p' POK_01.txt\necho \"=== find printed page ===\"\npython3 - <<'EOF'\nt=open('POK_01.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# find leaf index of line 4594\nimport itertools\ncnt=0\nfor i,l in enumerate(lines):\n    cnt+=l.count('\\f')\n    if i==4593:\n        print('form feeds before line 4594:',cnt)\n        break\nEOF"
}
```


### [2026-09-07T19:33:54.030Z] TOOL RESULT

```
aksl.  on-  {on-uUa  ,Schuhwerk^,  q-doh  ,Tal^),  schwundstuf,  v^n',  v^  in< adnom.  m.  Lok.  und  Akk. ;
toch.  AB  y-,  yn-j  B  in-  (nur  Präfix).
n-dhi:  ai.  ddhi  ,über,  auP,  apers.  adiy  ,in';  gall.  Intensivpräfix  Andi> (PN  Ände-roudus  ,der  sehr  rote^),  cymr.  an{ne)-  in  anne-l  ,Vorrichtunc^ =  air.  2«cZe-Z  {*ndhi-l-om),  cymr.  an-daw  ,lauschen^  (zu  taw  ,schweigend')* air.  ind-  (teils  aus  *indi-j  teils  aus  sekundärem  *indo-)  in  ind-reth  ,Eia- fall'  (*indi-reto-),  indnaide  (s.  weiter  unten),  usw.  Pedersen  (KG.  I  45)' will  auch  got.  und  ,bis  zu'  hierher  stellen;  s.  über  andere  Möglichkeiten  ' oben  S.  50  und  S.  181.  >^
(e)nero-  ,innerlich':  arm.  *nero-  ,das  Innere',  vorausgesetzt  von  ner- ,intra,  hinein',  nerJts  ,innen',  nerkoy  , drinnen';  vielleicht  gr.  bvsqol  als  ,die drinnen',  nämlich  in  der  Erde;  oder  besser  Hypostase  aus  o\  iy  egc^?
ni-,  nei'  ,nieder',  Komparativ  nitero-  ,nieder'  (im  Gegensatz  zu  ,oberer'):
ai.  ni,  av.  nl  ,nieder(wärts)',  ai.  nitardm  ,unterwärts',  av.  nitdma-  ,der
unterste';
arm.  ni-,  n-  ,nieder';  ;!fj
kelt.  *ne  aus  *nei  in  air.  ar-neut-saj  in-neut-sa  ,ich  erwarte',  (urir. *-ne-sedu)j  Yerbaln.  indn{a)ide  (*indo-ne-sodion)  und  in  ar-neigdet  ,sie beten'  (*ari-ne-gedont)]  vgl.  anders  Bergin  Eriu  10,  111;
ahd.  nidar,  as.  nithar,  ags.  nipei',  aisl.  nidr  ,niederwärts',  ahd.  nidana^ as.  nithana  ,unten',  ags.  neodan,  nipan  ,herunter,  unter',  aisl.  nedana  ,von unten  her',  Präp.  mit  Akk.  ,unterhalb',  as.  nithe  Adv.  ,unten',  ahd.  nida Präp.  mit  Dat.  und  Akk.  ,unterhalb,  unter';
abg.  niz^  ,hinab,  hinunter'  (Bildung  wie  prä-zi,  usw.);
im  Kompositum:  *
ai.  mpa-  ,tiefliegend'  (ni-\-ap-  ,Wasser');
*ni'oJcu-  als  ,die  Augen  niederhaltend'  in:
ai.  nlcä  ,abwärts'  (vgl.  nyanc-  ,nach  unten  gerichtet');
^^«
313
abg.  nicb  .pronus',  poniknqti,  nicati  ,pronum  esse,;  Wackernao-el-De- brunuer  Ai.  Gr.  III  230  f.,  Trautmann  198  f.  "^
mit  Formans  -uo-:
^v.  veLÖg  f.  ;Feld,  Flur^  (,*NiederungO.  veiaTog,  veacoq  ,der  unterste', vBLodxv  ,von  unten',  veiod-L  ,unterhalb',  vEiaiqa  yaarriQ  ,der  untere  Teil  des Bauches',  vr^iaxa'  ecxara,  xcrwrara  Hes.,  theb.  NrjLTzai  Ttvlai  (rj  scheint für  e  aus  ei  vor  pal.  Vokal  zu  stehen);
abg.  niva  , Acker'  (,*Niederung'),  skr.  7ijwa  (woher  das  J?),  öech.  russ. niva   ds.  {*neiuä  f.);
schwundstufig  ags.  neowol,  neol,  nlhol  ,pronus'  aus  *niwol,  mnd.  nigel ,niedrig';
hierher  wohl  auch  mit  Vollstufe  lit.  neivoti  ,quälen',  lett.  nievdt  ,ver- ächtlich  behandeln,  schmähen,  niederdrücken'  (auch  got.  *naüü  ivsTysv^ Marc.  VI  19?).
Vgl.  idg.  ni-zdos  ,Nest'  unter  sed-  ,sitzen'.  Als  ,heruntermachen'  (wie lett.  nievdt)  beruhen  wohl  auch  neid-  ,ovEidog',  neit-  ,befeinden'  neiq-  (s.  dort), auf  unserem  nei-,  ni-.
enter,  nter  ,zwischen — hinein',  en-tero-  ,innerlicli' :
ai.  antdvj  av.  antard,  apers.  antar  ,zwischen',  adnom.  mit  Lok.,  Instr., Akk.,  Gen.;  ai.  dntara-  ,innerlich',  av.  antara-  ,innerer',  Superl.  ai.  dntama- ,der  nächste'  (nicht  zu  dnti,  dnta-),  av.  antdma-  ,der  innerste,  vertrauteste, Intimus';  ai.  antrd-,  auch  mit  Vrddhi  äntrd-  n.  ,Einge weide';
arm.  dnder-Ic  Fl.  ,Einge weide'  (gr.  Lw.?  s.  Hübschmann  Arm.  Gr.  1447 f.);
gr.  evTEQOVj  meist  PI.  ,Eingeweide' ;
alb.  nder  ,zwischen,  in',  ferner  ndjej^,  '^QJ^i'  usw.  ,bis'  (^entero-) ;
lat.  e?i^er,  inter  ,zwischen',  adnom.  m.  Akk.  (erstarrt  m.  Gen.  intervias, interdius),  intrö,  inträ,  intrin-secus,  interus  ,innerlich',  interior,  intimus^ intestlnus  (s.  unten),  osk.  Entrai  ,*Interae',  tiefstufig,  osk.  anter  ,inter', umbr.  anter j  ander  ,während',  adnom.  m.  Lok.  und  Akk. ;
air.  eterj  etir,  etar  , zwischen',  adnom.  m.  Akk.,  corn.  ynter,  yntre,  bret. entre  (der  Endvokal  nach  tre-j  dre  =  cymr.  trvjy),  acymr.  ithr  ,inter';  gall. inter  ambes  ,inter  rlvös';
ahd.  untar  usw.  ,unter  =  zwischen'  ==  osk.  anter  (verschieden  von germ.  *under,  ahd.  usw.  untar  ,unterhalb'  aus  *7j,dher^  lat.  infrä)]  vgl. got.  undaürni-mats  ,Zwischen-mahl'  =  ,Frühstück',  anord.  nndorn  n. ^Vormittag  (um  9  Uhr)',  as.  undorn,  ags.  undern  ,Mittag',  ahd.  untorn ^Mittag,  Mittagessen'  (n-Suffix  wie  in  lat.  internus)]  hochstufig  wie  ^v. evrsQa  usw.  anord.  idrar  Fl.  , Eingeweide'  (aus  ^innrar,  *inperöz),  innre, idre  ,der  innere'  (wenn  diese  nicht  spez.  nord.  -?'o-Ableitungen  von  inn  = got.  inn  ,hinein',  s.  oben,  sind);
314
slav.  *^tro  in  aksl.  jqtro  ^Leber^,  ablaut.  gtroba  ,v.oilLa'j  gtrb  ^eiaw^ über  hitt.  antüinias  ,interior' ,  andurza  ^drinnen'  s.  Lohmann  I.  F.  51^  32Qf entös  /von)  innen^  (vgl.  ai.  i-tdh  ^von  hier^^  lat.  caelitus  usw.): gT.  h'zög  ^innen^;  wovon  evxoa-^ev^  -d-L  und  weiter  ivröad^ia,  ivroad^l^. , Eingeweide^  (oder  letztere  mit  aus  evroad-s  verschlepptem  -d"  für  *ivToancf vgl.  ai.  antastya-  n.  ^Eingeweide^,  Fick  I*  363^  Vendryes  Rev.  et.  gr.  23* 1910,  74);  '      '
lat.  intus  ,von  drinnen;  innen ^,  davon  mit  analoger  Umgestaltung  intestina' mnd.  nhd.  dial.  inser  ^eßbare  innere  Teile  von  Tieren',  anord.  istr  n tstra  Lj  ,das  die  Eingeweide  umgebende  Fett^  (*en-s-tro-);
apr.  instran  ,Fett^,  lett.  tstri  PL  _,Nieren^  (*en-s-<ro-) ;  lett.  leksa  ^Inneres'  pl  . ,Eingeweide^  (*'en-t-{a),  alit.  inscios  ,Herz^,  lit.  {scios  , Eingeweide^  {*en-s-t{o\ Über  die  Zusammenrückung  lat.  endo,  indu,  wozu  gr.  t«  evdiva,  air. inne  ^Eingeweide^,  s.  oben  S.  182  —  Über  gr.  bv-öov  ,*im  Haus^  (wozu evdo-d-av,  -i9-t,  lesb.  dor.  evdoL  nach  OL-KO-d-sv,  -&Ly  ö'iy.ol)  s.  dem-  ,bauen' WF.  I  125  ff.,  II  335  f.,  WH.  I  687  f.,  694,  708  f.,  711  f.,  870,  Traut^ mann  69  f.,  198  f.   W.  Schulze  Kl.  Sehr.  70  ff.  t^.^
=== find printed page ===
form feeds before line 4594: 324
```


## [2026-09-07T19:34:17.177Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- MON limu ---\"\ngrep -c \"لیمو\" MON_part1.txt MON_part2.txt 2>/dev/null\ngrep -n \"لیموناد\" MON_part1.txt MON_part2.txt 2>/dev/null | head -5\necho \"--- MON nirvana ---\"\ngrep -n \"نیروانا\" MON_part1.txt MON_part2.txt 2>/dev/null | head -5"
}
```


### [2026-09-07T19:34:17.276Z] TOOL RESULT

```
--- MON limu ---
MON_part1.txt:13
MON_part2.txt:37
MON_part2.txt:41546:لیمونادها مصرف می‌گردد؛ لیمون حلوء 
--- MON nirvana ---
```


## [2026-09-07T19:34:20.056Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"لیمو\" MON_part2.txt | head -40 | cut -c1-250"
}
```


### [2026-09-07T19:34:20.116Z] TOOL RESULT

```
6676:لیمو و ِ مایعی زرد رنگ روشن 
15613:اوردن اب غوره یا لیمو خشکک را به عنوان 
16647:لیمو عمانی -< خشکک را سوراخ کرده در قیمه 
17496:لیموترش را هم بدان علاوه کنند و هموزن 
19937:کرده با لیموی عمانی در شکمش ربخته و 
29516:نواد گارن» نژاد گاسکون,» ن#اد لیموزن ناد 
36820:است جامد و به رنگ زرد لیمویی؛ نی مره و 
41499:(گی.) لیمو شیرین. 
41505:لیمو : 17 (- لیمون (معر.)» هند. نسو؛ 
41513:لیمو ترش: ۱-5 ( مر.) گونه‌ای لیمو که 
41532:مایل به قرمز یا بنفش‌اند. میوژ لیموترش پس 
41536:بافت بشرة پوست لیموترش کیسه‌های 
41538:از فشردن میوة اين گیاه آب لیمو میگیر ند؛ 
41539:لیموی ترش, لیمون بلدی؛ لیموی بلدی» 
41540:لیمون مالح؛ لیمون س_ _ آب. 
41541:لیمو شیرین: ۱-1 گنا.) گونه‌ای 
41542:لیمو که میوه‌اش شیرین و درشت‌تر از لیمو 
41546:لیمونادها مصرف می‌گردد؛ لیمون حلوء 
41547:لیموی شیرین؛ لیم» حلیب. 
41549:لیمون: ۱۱/۹۵ ( یا ۰ لیمون اضالما 
41550:برنطی: یکی از گونه‌های لیموترش است. 
41551:لیمون اضالیا مالح: (گیاء) گونه‌ای لیموترش 
41552:که به لیموی ایتالیایی نیز موسوم است. لیمون 
41553:بلدی: (گیا.) یموترشلیمون حلو: (گیا.) 
41554:لیمو شیرین. لیمون ماله: ( کیا.) لیمو شیرین. 
41561:لیموشیر ین 
41565:فرانسوی به معنی شربت آب لیمو است. 
53513:تژاد بلیموت را کك» براهماء جاوه. و باندوت. 
53598:خروسی که به بی‌وقت خواند. مرغ پلیموت 
54212:نار نج بر تقال» بالنگ. نارنگی؛ لیمو ترض» 
54213:لیمو شیرین» توسرخ و غیره. مر کبات‌بیشتر در 
59536:روی آن آب لیموی تازه ریزند (کتاب 
59785:گوشت مرغابی را با آب لیمو یا آب نارنج 
69350:جشن موبدان موبد خوانچه‌ای که در آن لیمو 
87878:تارنج و لیموترش و لیمو شبرین) و گوجه 
94409:و چهار مرتبه زیادتر از آب لیموی ترش 
94454:دارای گل‌های زرد لیمویی است. محصول و
```


## [2026-09-07T19:34:22.775Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '41495,41570p' MON_part2.txt"
}
```


### [2026-09-07T19:34:22.822Z] TOOL RESULT

```
زبانیان که مخصوص نواحی گرم کرة زمین 
است و در نواحی جنوبی ايران (از جمله در 
چا‌بهار) نیز کاشته می‌شود. این گیاه در 
حقیقت یکی از گونه‌های سپستان است. 
(گی.) لیمو شیرین. 


لیم: ((ص.) شوخ و ظریف و بذله گو. 


لیمو : 17 (- لیمون (معر.)» هند. نسو؛ 
سنتت. ] (.) (گیا.) نام دو نوع گیاه از گروه 
مرکبات و از تیرهٌ سدابیان که میوه‌های آنها 
ما کول است و از نظر طعم ی 
0 ویر می‌شوند. (گیا.) میوهٌ گیاه 


مذ کور. ( کذ با 
لیمو ترش: ۱-5 ( مر.) گونه‌ای لیمو که 
بصورت درحتی و مره ویر و 


۴ تا ۵ متر که ريشة قوی و منشعب دارد. 
ساقه‌اش راست و سایل به سر و دارای 
شاخه‌های خاردار است. ب رگک‌هایش شفاف و 
متناوب به رنگک سب مابل به زرد و دندانه‌دار 
و با کامل می‌باشد. از مشخصات برگک آن 
این است که دمب رگ بال‌دار آن کم عرض تر 
از ب رگ نارنج و پرتقال است. گل‌های آن 


۱5 


متعدد و دارای سوی ضصعف و شامل 
گلب رگ‌هایی است که سطح داخلی آنها به 
رنگ سفید ولی در سطح خارجی کمی 
مایل به قرمز یا بنفش‌اند. میوژ لیموترش پس 
از رسیدن به رنگ زرد روشن و مزه آن 
ترش و مطبوع است. دانه‌هایش بدون بو 
ولی دارای طعم بسیار تلخ می‌باشند. در زیر 
بافت بشرة پوست لیموترش کیسه‌های 
بزرگک و فراوان محتوی اسانس وجود دارد. 
از فشردن میوة اين گیاه آب لیمو میگیر ند؛ 
لیموی ترش, لیمون بلدی؛ لیموی بلدی» 
لیمون مالح؛ لیمون س_ _ آب. 
لیمو شیرین: ۱-1 گنا.) گونه‌ای 
لیمو که میوه‌اش شیرین و درشت‌تر از لیمو 
ترش است و ابش به عنوان مدر به بیماران 
تب‌های عفونی داده می‌شود. اسانس 1 
جهت معطر کردن شربت‌های دارویی و 
لیمونادها مصرف می‌گردد؛ لیمون حلوء 
لیموی شیرین؛ لیم» حلیب. 

لیمون: ۱۱/۹۵ ( یا ۰ لیمون اضالما 
برنطی: یکی از گونه‌های لیموترش است. 
لیمون اضالیا مالح: (گیاء) گونه‌ای لیموترش 
که به لیموی ایتالیایی نیز موسوم است. لیمون 
بلدی: (گیا.) یموترشلیمون حلو: (گیا.) 
لیمو شیرین. لیمون ماله: ( کیا.) لیمو شیرین. 
لی‌موناد: 0 ]۱ , لسمونات| (۱.) در 


فرهنک فارسی معین 


لیموشیر ین 
تداول عامه و در زبان فارسی به معنی شربت 
گازداری است که با جوش شیرین و کمی 
مادةٌ ترش‌مزه درست کنند ولی در زبان 
فرانسوی به معنی شربت آب لیمو است. 
لیمه: (ه-)نآ1 (۱.) جرک و سح: لسمه 
گوش. کفش چرکین از چرم دباغت نا کرده. 
لین 11۱۳۳۵0 [ع.] نرم؛ مق. زبر» حشن. رام» 
. روان. (سد.) مننور؛ مق. قوی. 
لین: «۱ (ع.| (امسص.) نرمی؛ لینت؛ متد.
```


## [2026-09-07T19:34:35.092Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('MON_part2.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# look for standalone numbers near 41500\nfor i in range(41300,41620):\n    m=re.match(r'^\\s*([\\d۰-۹]{3,4})\\s*$', lines[i])\n    if m: print(i+1, m.group(1))\nEOF"
}
```


### [2026-09-07T19:34:36.343Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T19:34:40.389Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('MON_part2.txt',encoding='utf-8',errors='replace').read()\nprint('formfeeds', t.count('\\f'))\nleaves=t.split('\\f')\n# find leaf containing لیمو entry\nfor i,l in enumerate(leaves):\n    if 'لیمو : 17' in l or 'لی‌موناد' in l:\n        print('leaf',i)\n        print(repr(l[:300]))\n        print(repr(l[-300:]))\n        break\nEOF"
}
```


### [2026-09-07T19:34:41.798Z] TOOL RESULT

```
formfeeds 0
leaf 0
'معین» محمد» ۱۲۹۱ ۱۳۵۰. \n\n\n۰ \n۳ \n\n\nفرهنگ معین / محمد معین. -- تهران: آدنا: کتاب راه نو ۰۱۲۸۱ \n\n\n۲ج \n(دوره) :964-7252-51-2 :158 \n(ج.۲) 964-7252-53-6 :158۷ (ج.۱) 964-7252-52-8 :5۳81] \nفهر ستنویسی بر اساس اطلاعات فیپا. \n۱. فارسی -- واژه\u200cنامه\u200cها. الف. عنوان. \n۴۵ف ۲۹۵۴/۸۷ ۳112 ۳ فا ۴ \n۱۳۸۱ \nکتابخانه ملی ا'
' کسی که در بهودیه \nمتو لد شده باشد. کسی که از اعقاب سا کنان \n1 ناحیت بود. \n\nیهودی: 01 منسوب به بهو د. متدین به \nدین بهود. (عم.) گاهی به آدم جبان و ترسو \nو مردنی و کم دل و جرأت گفته می\u200cشود \n(فرعا.جما.) \n\nیبلاق: ۱۰۰(۷ [تر.] جای\u200cباش تاستان» \nمنطقهٌ خوش آب و هوا که هنگام تابستان \nبدانجا روند» مصطاف. \n\n\n'
```


## [2026-09-07T19:34:52.205Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification\npython3 - <<'EOF'\nimport json,glob,re\nn=0\nfor f in sorted(glob.glob('page-3*.json')):\n    d=json.load(open(f))\n    for e in d.get('entries',[]):\n        for rc in e.get('ref_check',[]) or []:\n            if rc.get('ref','').startswith('MON'):\n                print(f, rc['ref'], rc['status'], rc['note'][:300]); n+=1\n        for nd in e.get('nodes',[]):\n            for rc in nd.get('ref_check',[]) or []:\n                if rc.get('ref','').startswith('MON'):\n                    print(f, rc['ref'], rc['status'], rc['note'][:300]); n+=1\n    if n>12: break\nEOF"
}
```


### [2026-09-07T19:34:53.429Z] TOOL RESULT

```
page-300.json MON:3549 partial Mo'in's entry exists and reads 'لاییدن: [= لاب (= لابه) + یدن؛ قس. مصدری مانوی پارتی: نامیدن، دعا کردن، درخواست کردن] تضرع کردن' (MON_part2.txt line 37656) — it confirms the word and the meaning but derives it from لابه, not from the IE echoic root. The page number could not be checked: the archive.
page-300.json MON:3523 supports Mo'in's Farhang has the entry: 'لادن ... (اِ) نام صمغی است خوشبوی که از گیاه عشقه حاصل می‌شود و قاعده‌آور است ... لاذنه، لاذن' with the same Manuchehri verse (MON_part2.txt line 37796 ff.). Page number not verifiable (the archive scan of Mo'in has no page markers), but the alphabetical spacing to MO
page-301.json MON6:1773 not_checked Mo'in vols 5–6 (a'lam / proper names) are neither on disk nor online (refs_online.json: only the lexicon vols are readable through vajehyab/abadis, and the archive.org copy is a 2-vol abridgement), so p.1773 could not be opened. The gloss is however corroborated independently: abadis.ir s.v. لاجین g
page-301.json MON6:1773 not_checked Mo'in vol. 6 (a'lam) is not available on disk or online; only the lexicon volumes are readable (vajehyab/abadis), and they carry لاجورد without any Turkic-tribe etymology.
page-302.json MON:3536 supports Mo'in's Farhang s.v. لاله: «لاله [= آلاله - قس. لال، سرخ]» (MON_part2.txt l.38122) — the Adena condensation preserves the cross-reference to لال 'red'; the 6-vol page number itself cannot be checked (no scan of the 6-vol edition exists).
page-302.json MON:3536 partial Mo'in's لالک entry in the Adena condensation (MON_part2.txt l.38220) gives «لالکا، لاله گوش» (earlobe) and the geranium, i.e. a different sense-group; the footwear sense is not carried there, so the page could not be confirmed.
page-302.json MON:1676 partial Mo'in's Farhang has the expected entries (رنج، رنجش، رنجیدن، رنجاندن: e.g. MON_part1.txt l.2857 «رنجیدگی، رنجش، شکراب، اندوه، غم», l.2906 «رنجانیدن، رنجه کردن، گزند رسانیدن»), and Mo'in's own etymological footnote on the word is the BQT one quoted above; the 6-vol page 1676 itself cannot be verified
page-302.json MON:3616 supports Mo'in s.v. لقلقه (MON_part2.txt l.39947): «لقلقه: [ع. لقلقة] (مصدر) سخت آواز کردن؛ آواز لکلک ... آوازی همراه با جنبش و اضطراب؛ فصاحت عاری از بلاغت» — the Arabic origin tag [ع.] and both senses Nourai gives. The 6-vol page number itself is unverifiable (no scan of the six-volume Farhang exists).
page-303.json MON supports MON_part1.txt: 'جبرئیل: [= جبرائیل ـ جبریل] (اخ.) یکی از فرشتگان مقرب'; MON_part2.txt s.v. ملک: 'عدد این گونه فرشتگان در اسلام چهار است: جبرائیل، اسرافیل، میکائیل، عزرائیل'. (Moʿin's aʿlām volumes 5–6 are not on disk, so page numbers could not be given.)
page-303.json MON not_checked گابریل would stand in Moʿin's aʿlām volumes (5–6); the local MON_part1/part2 files cover only the lexicon volumes and return 0 hits for گابریل. vajehyab/abadis also carry only the lexicon.
page-303.json MON partial Moʿin's aʿlām volumes (5–6), where دانیال and الیاس would stand, are not on disk; MON_part1/2 (lexicon) return 0 hits for either name.
page-303.json MON not_checked These are European personal names and a Paris place name; they would stand (if at all) in Moʿin's aʿlām volumes 5–6, which are not on disk — MON_part1/part2 give 0 hits for الیزه, شانزه, آمانوئل, رافائل, الیزابت, ساموئل, دانیل.
page-304.json MON:3551 not_checked The 6-volume Amir Kabir Farhang-e Fārsi is not online with its pagination (refs_online.json: 'Page numbers cannot be mapped online'; the local MON_part1/part2 are OCR of the 2-vol Adena abridgement without page breaks), so p.3551 itself could not be opened. The content was verified instead in Mo'in'
page-304.json MON:3551 not_checked Pagination of the 6-vol Mo'in is not reproducible online (see node #2); the entry's content — '[په.] کنارهٔ هر چیزی. بخش بیرونی دهان' — was read on abadis.ir and matches Nourai's gloss 'lip, also side or edge of anything'.
```


## [2026-09-07T19:35:03.706Z] TOOL CALL #46: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1922 --image 2>&1 | tail -40"
}
```


## [2026-09-07T19:35:04.641Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT limon/lima ===\"\ngrep -n -i \"limon\\|Zitrone\\|Limone\" LKT.txt | head -20"
}
```


### [2026-09-07T19:35:10.089Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1922.png
REF: BQT:1922  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 719  OCR-lang: fas

لیلیا ۱ -۱۹۲۲-
ایلیا ۱ - بالام بروزن انیا بلفت زد | لول‌فر ۴ - بروزن وستی بلوفرات
وپلزند(۱) بمعتی‌شب است که عربان لیل کویند. | وآن کلی باشد کبود که بیشتر درمیانآب روید.
لیمو ۲ * با اول بثانی رسیده ومیم‌بواو ورمهای گرم را نافع است وخوردن‌آن‌منع‌احتلام
کشیده * معروف است . کوبند آب لیمودفع‌سم کند .
مار و عقرب میکند؛ وبعضی کوبند نام درختیست لیق - بکر اول و سکون ثانی مجعول
که هبو آن لیمو است . و واو . بکی ازنامهای خورشید است که‌تیراعظم
لیمو دارد9-» با دال ابجد بالف کنیده | باشد ۴ .
و برای قرشت پواو رسیده , نباتیست کوهی که یود - بروزن زبرك » پرامرد ضخم
در بهار از میان درزهای سنک بر هيآید و بوی لك ويك را گونند .
لیمو میکند وآترا ری وقیج کویند . لیولنگ - بای مجمود و قح لام
لیمو نیون - بکرنون وتحتانی بواو بت
- ۱ : بروزن دبورنگه . برف ر۱ 9 کوبند وآن‌چیزی
شیده و بنون زده , بلفت سربانی دوائی است | باشد سفید که درزمتان مانند پنبه حلاجی کرده
که بیخ‌آلرا بشیرازی حلیم خوانند. ضمادکردن از آسمان فرو بارد و بعربی ثلج خوانند ؛ و باین
آن درد مفاصل و نقری را نافع است . معنی بفتح اول بر وزن تنومند هم گفته اند -
لینج با نون بروزن ابرج » نوعی از | و بمعنی ترف که قراقروت باشد هم‌آمده است.
افلیمیا(۲) است کهآنرا درجز یره قبری درممندن ظاهرا که درهعنی لغت تصحیف خوانی شده‌باشد.
مس یایند . ااعلم .
(۱) چك : ژند و پاژد . (۷) چش : افلیما . ۱
۱- هز 2راژها , 2رداانها1 , 2را1۸ . بهلوی 5820 ( شب ) ۸« پونکر ۰.۱۰۷
۴ - اصل این نبات ازهند است ونام آن هم هندست «تفس» . درسانسکربت
تچ : ۰
77 « ژابا س ۰۳۸۶ . لیمو < لیمون ( عر ) ۳ 11308 ( فر )011۳5
0 . نزد قدها لیموقمی|زمر کبات که ترش و معطر است و خود وآب آنرا در چای
وخورشها کنند و درولابات ساحلی‌بخر خزر وفاری‌پعمل می‌آید «لفت نامه» وامروز آنرا لیموترش
کوبند - لیمو در زمان ما غالباً به لیمو شیرین اطلاق شود که آنهم از مرکبات و دارای پوست
نازك زرد رنگی است وطعم وی شیرین است .
۴ <* بیلوفر(ه.م.) < تیلوپل * نیلوپر < لیلوپل < لیلوپر .
۴ - ای ساقی مه روی درانداز ومرا ده زان می که رزش مادر ولیوش پدرآمد.
انوری آبیوردی «* جهانگیری >.
ه - صحیح «ترف؟ است و «برف» مصحف آدست و برهان خود این حدس را زده است.
لیولنگه و هلباکك و پنیرتن وهبولنگك جمله ترف را خوانند . غمناك راست :
وان زر از توباز خواهدآن که تا اکنون ازو ‏ جوغری خوردی همی و طایفی و لیولنکه .>
« لغت فری ص ۶۳۰۰ ۰
(برهان قاطع ۲۳۴۳)
```


### [2026-09-07T19:35:10.130Z] TOOL RESULT

```
=== LKT limon/lima ===
2210:Antimonium  reichte,  um  sie  zu  vergiften : anti  <  gr.  üivti  'gegen',  frz.  moine 'Mönch'],  sp.  pg.  it.  anlimonio;  engl. antimony^  dtsch.  Antimon.  —  Möglicher- weise geht  auch  sp.  bismuto,  frz.  bistnuth, it.  bisniutia;  dtsch.  Wismuth,  engl,  bis- muth  auf  das  ar.  Grundwort  zurück. [RomForsch  III,  493.  Eguilaz  346.  Devic DEt  34.   Lammens  Rem  52/53  u.  260.
3072:1320.  Ar.  Ilm: Einheitsnonien  l'inia  'kleine  Zitrone  von sehr  süßem  Geschmack' ;  hieraus  sp.  pg. lima,  frz.  Urne,  Urne  hergamote  'Citrus bergamia  vulgaris  Risso'.  [DE  297/298. Eguilaz  439.    Devic  DEt  152.
3076:'Zitrone,  Citrus  limonum',  ebenso  ar. laimün  und  tk.  limon  'Zitrone'  und 'Zitronenbaum';  hieraus  it.  limone,  siz. limuni,  prov.  limon,  frz.  limon,  limoniev, kat.  llimö,  sp.  limdn,  pg.  limäo,  Umoeiro, rum.  lämte  'Zitrone',  lamuH  'Zitronen- baum'; engl,  lemon,  ndl.  lemoen,  lamoen, dtsch.  Limone  (selten),  liieraus  Limonade 'süßes  Getränk';  russ.  limon,  klruss.  ly- mon,   bulg.  öech.  limon,  serb.  limun.
3077:poln.  limona.  [DE  298.  Eguilaz  439 ML  5057.  Kluge  287.  MWiD  81.  83 Mikl  SlEtWb  170  a.  Bern  SlEtWb  72 1/722 .
3101:'Nachlese,  Abfälle,  Wertloses',  mit  Imäla [ä  >  e]  Itilcet ;  hieraus  sp.  luquete  'Stück Zitronen-  oder  Apfelsinenschale,  das  man in  den  Wein  tut,  um  ihm  diesen  Ge- schmack zu  geben'  [Dicc  Gast  1286  a; DE  298].
3704:'Fünf  [Horn  NpEt  S.  73,  Nr.  328;  vgl. päng-äb  'Pandschab',  engl.  Schreibung Punjaub  'FOnfstromland'] ;  hieraus  engl. punch,  dtsch.  Punsch,  ein  Getränk,  das aus  fünf  Zutaten  hergestellt  wird:  Arrak, Zucker,  Zitronensaft,  Wasser  (oder  Tee) und  Gewürz  (Zimt)  [SCHILLER  läßt  in seinem  Punschlied  das  letzte  aus  und singt:  ,Vier  Elemente  /  Innig  gesellt  / Bilden  das  Leben  /  Bauen  die  Welt."]; sp.  ponche,  rum.  punciü,  russ.  punS. [Ho'oson-Jobson  737/739.    Kluge  353.
4167:'Trank'  [Vb.  sariba  'trinken'],  hieraus mlat.  siröpus,  sirüpus,  it.  sciroppo,  si- roppo,  frz.  sirop,  syrop,  prov.  isarop, kat.  aixarop,  sp.  jnrope,  pg.  xarope, enxarope,  rum.  sirop,  sirup;  ndl.  siroop, stroop  [in  Südhmburg  dial.  sroep,  vgL GRM  V,  171],  dtsch.  Sirup,  engl,  syrop, syrup;  russ.  sirop,  serb.  sirup,  äech. syrup,  poln.  syrop.  —  Aus  der  gleich- bedeutenden ar.  Form  surba,  sarba wurde  zur  Bezeichnung  eines  kühlenden Trankes  über  tk.  serbet  'Kühltrank'  it. sorbetto  'süßes  Fruchteis'  [mit  Einwir- kung von  it.  sorbire  'schlürfen'],  frz. Sorbet,  sp.  sorbete,  pg,  sorvete,  rum.  ger- bet 'dicker  Obstsaft';  ndl.  sorbet,  engl. sherbet,  shrub,  dtsch.  Sorbet,  Scherbet 'ein  aus  Wasser,  zerstoßenen  Rosinen, Zucker,  Zitronensaft,  Ambra  und  ähn- lichen Zutaten  gemischter  Kühltrank'. [DE  218  und  417.  Eguilaz  495  und  513. ML  7675  und  7711.
4741:2117  Ar.  turungr: 'Apfelsine',  Einheitsnomen  turunga; hieraus  sp.  pg.  toronja,  kat.  taronja 'Mittelding  zwischen  Zitrone  und  Apfel- sine, dickschaliger  und  fleischiger  als  die letztere'.  —  Aus  ar.  turungän  'Melisse' wurde  sp.  torongil,  kat.  tarongina  'dass.' [mit  Imäla  ä  ^  e  >  i].  [DE  351. Eguilaz  507.
5806:Limonade  1322
7097:labarda  823 /rtc-c«  1295 /accÄe  2130 /a/ia  siz.  24 lambiccare  79 lambiccio  79 lanibicco  79 /an/"«  1535 laparderi  siz.  823 laparduni  siz.  823 /a^is  lazzuli  1311 larice  114 lazzaretto  1310 lazzarone  1310 lazzeruola  2ii06 lazzuli(lapis)  1311 Ze/ffli  siz.  1313 libeccio  1313 i?7ac  1319 Hmbiccio  79 limone  1322 limuni  siz.  1322 Usciardo  1581 K«rfo  2127 «M<o  2127 1329
7739:limona  1322
8540:limon  loiiii
```


## [2026-09-07T19:35:28.450Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '3066,3080p' LKT.txt"
}
```


### [2026-09-07T19:35:28.503Z] TOOL RESULT

```
1317.  Tk.  libade:
'Kurze  wattierte  Weste,  Wollmanter [Kel6kiun  Kämüs  1074  b];  hieraus  rum. libadea  'Rock'.
1318.  Ar.  llf:
Einheitsnomen  Ufa  'Palmenbast'  und 'Seil  daraus';  hieraus  siz.  leff'a  'foglia delicata  del  ciafaglione',  sp.  hfe  'Art Fangseil'  [Dicc  Gast  1280  a].  [GrSVociSic 239.  Eguilaz  437  [mit  anderer  Erklärung].
1319.  Ar.  lilak:
Auch  lailak  [aus  pers.  llläg,  niläg,  s.  hier Nr.  1568]  'Syringa  vulgaris,  spanischer Flieder',  dessen  lilafarbene  Blütensträuße zwar  keinen  Farbstoff  liefern,  aber  einem bestimmten  Blau  seinen  Namen  gegeben haben ;  daher  hieraus  rum.  liliac  'P'lieder', Uliachiü  'lila',  lulachiu  'Indigo',  it.  sp. lilac,  frz.  lilas;  hu\g.  Iii' ak,lulak'^Fl\edev\ Cech.  poln.  lilak  'dass.';  dtsch.  lila  'bläu- lich', engl,  lilac  'Flieder'.  [Ngr.  XouXctKi 'bläuliche  Farbe  oder  Tinte'.]  [DE  297. Eguilaz  439.    Mikl  SlEtWb  169  b.
1320.  Ar.  Ilm: Einheitsnonien  l'inia  'kleine  Zitrone  von sehr  süßem  Geschmack' ;  hieraus  sp.  pg. lima,  frz.  Urne,  Urne  hergamote  'Citrus bergamia  vulgaris  Risso'.  [DE  297/298. Eguilaz  439.    Devic  DEt  152.
1321.  Tk.  limaii:
'Hafen'  [aus  gr.  Xi|ar)v;  ngr.  \i|Lidvi]; hieraus  rum.  liman  'Hafen,  Zufluchtsort' ; russ.  liman  'Meerbusen',  klruss.  Igman, lymen,  poln.  bulg.  liman  'Hafen'.
1322.  Pers.  liiuüu:
'Zitrone,  Citrus  limonum',  ebenso  ar. laimün  und  tk.  limon  'Zitrone'  und 'Zitronenbaum';  hieraus  it.  limone,  siz. limuni,  prov.  limon,  frz.  limon,  limoniev, kat.  llimö,  sp.  limdn,  pg.  limäo,  Umoeiro, rum.  lämte  'Zitrone',  lamuH  'Zitronen- baum'; engl,  lemon,  ndl.  lemoen,  lamoen, dtsch.  Limone  (selten),  liieraus  Limonade 'süßes  Getränk';  russ.  limon,  klruss.  ly- mon,   bulg.  öech.  limon,  serb.  limun.
poln.  limona.  [DE  298.  Eguilaz  439 ML  5057.  Kluge  287.  MWiD  81.  83 Mikl  SlEtWb  170  a.  Bern  SlEtWb  72 1/722 .
1323.  Sskr.  liiiga:
Ebenso  tamul.  Ungarn  'membrum  virile', das  buddhistische  Emblem  des  Mahä, Deva  (Siva),  das  sich  als  Kegel  aus schwarzem  Stein  in  den  Pagoden  dieser Gottheit  findet.  In  den  Reisebeschrei- bungen über  Indien  häufig  als  Lingam, engl,  lingam  erwähnt.
1324.  Tk.  lipkaii:
```


## [2026-09-07T19:35:41.040Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"===== PHN limon =====\"; grep -n -i \"limon\\|lime,\" PHN.txt | head -10\necho \"===== DEV limon =====\"; grep -n -i \"LIMON\\|^Lime\\|lime\\.\" DEV.txt | head -10\necho \"===== TTS limon =====\"; grep -n -i \"limon\" incoming/TTS/TTS_pages.txt 2>/dev/null | head -5"
}
```


### [2026-09-07T19:35:41.119Z] TOOL RESULT

```
===== PHN limon =====
6755:LIMON (fruit), s. m. (a.-p.-t.)
6757:turc, limon y fruit du limonier, donnant beaucoup de jus, et
6759:chissanle, appelée limonade. Ses qualités sont les mêmes que
6761:liens écrivent limone, les Espagnols limon, les Portugais limâo,
9203:de jus de fruits, tels que limons, mûres, groseilles, etc., et
9208:agréable, très-connu des limonadiers, et dont on fait un fré-
9527:boisson aussi agréable que la limonade. Les Orientaux en font
10684:Limon (firuit), s. m. (a.-p.-t.) sSg
===== DEV limon =====
1638:LiMo.'s.  Fruit.  Esp.  limon,  portug.  limào ,  ital.  limone. De  l'arabe-persan  ^^^  lëimoûn,  même  sens.
3787:Lima,  hisp.  voy.  Limon.
3788:Limâo,  pg.  voy.  Limon.
3789:Lime,  voy.  Limon.
3790:Limon.
3791:Limone,  ital.  voy.  Limon.
5113:JiLJ  voy.  Liias. A^  jaers.  voy.  Lilas. tiLLJ  voy.  Lilas. .âXJ  pei's.  voy.  Liias. JulLJ  pers.  voy.  Lilas. iCçJ  voy.  Limon. y^.çJ  voy.  Limon.
===== TTS limon =====
527:üimon (Citrone), statt limav, limon. Als Auslaut wechselt l mit
```


## [2026-09-07T19:35:42.577Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"===== AFM limun =====\"; grep -n \"ليمون\\|لیمون\\|لیمو\" AFM_pages.txt 2>/dev/null | head -10; ls AFM* 2>/dev/null; ls incoming/AFM 2>/dev/null\necho \"===== PLA =====\"; grep -n -i \"limun\\|līmūn\\|laimun\" incoming/PLA/PLA_pages.txt 2>/dev/null | head -10"
}
```


### [2026-09-07T19:35:42.647Z] TOOL RESULT

```
===== AFM limun =====
AFM_alt.txt
AFM_pages.txt
AFM.pdf
AFM.txt
===== PLA =====
13623:laimun                                                                       243                                                               mä&5Un
```


## [2026-09-07T19:35:46.350Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHN 6750-6770 ===\"; sed -n '6750,6775p' PHN.txt\necho \"=== DEV 1630-1650 ===\"; sed -n '1630,1645p' DEV.txt\necho \"=== TTS 520-535 ===\"; sed -n '520,535p' incoming/TTS/TTS_pages.txt"
}
```


### [2026-09-07T19:35:46.448Z] TOOL RESULT

```
=== PHN 6750-6770 ===
citerne, d'un vase ou d'un liquide; sédiment, lie. — Comparez l'an-
glais lee. — On dit figurément, en français, la lie du peuple,
en parlant de la plus vile et de la plus basse populace. —
Quand on emploie absolument le mot lie, c'est qu'il s'agit de la
lie de vin.LOU 239
LIMON (fruit), s. m. (a.-p.-t.)
|4vi [Ihn] en arabe, ^^jJ [/tmoti] en persan, et {j^^ [Itmom] en
turc, limon y fruit du limonier, donnant beaucoup de jus, et
surtout employé dans la composition d'une boisson très^rafraf-
chissanle, appelée limonade. Ses qualités sont les mêmes que
celles du citron, avec lequel on le confond souvent. — Les Ita-
liens écrivent limone, les Espagnols limon, les Portugais limâo,
et les Anglais Umon,
LIPPE, s. f. (p.)
tçJ [fcA] Ihre, — Lippe ne se dit que de la lèvre inférieure quand
elle est naturellement trop grosse, ou lorsqu'on l'avance, par
moquerie ou par humeur. — Faire la lippe, dans le style fa-
milier, s'emploie pour bouder, — Voyez Livas.
L00KetL0K,8. m. (a.)
^jj^ [/a^otijf] ce quon lèche, ou ce que le médecin donne à lécher au
w
malade; dérivé de (^jiI [la^aq] lécher. Electuaire employé contre
les rhumes, les douleurs de poitrine, et qui se prend ordinai-
rement par cuillerées. Le look blanc, dont la préparation est
fort simple, est d'un usage plus fréquent que le look jaune ou
rert. — On trouve encore dans les dictionnaires français les
=== DEV 1630-1650 ===
LvzuLi  (Lapis-).  —  Voy.  Azur.
Lascar.  Matelot  indien  de  la  classe  des  parias.  Du  persan JCmJ  lechkcv,  armée ,  troupe.
Lebbeck.  Espèce  d'acacia  asiatique  et  africain  (connu à  la  Réunion  sous  le  nom  de  bois  noir).  De  l'arabe  ^ Jebli/i.  Le  nom  du  genre  lébeckie  (^Lebeckia),  (jui  comprend des  arbustes  du  cap  de  Bonne-Espérance,  a  sans  doute  la ])ieme  origine  étymologique.
Léviathan.  Transcription,  dans  saint  Jérôme,  de  l'hé- breu jD^lb  imjathan^  qui  désigne  un  monstre  aquatique  ou terrestre  mal  défini.  On  peut  voir  ce  qu'en  dit  Gesenius dans  son  Dictionnaire  hébraïque.  Le  mot  paraît  se  ratta- cher à  la  racine  m*?  lavah,  replier,  tordre,  en  arabe,  <^^ lawa;  le  léviathan  serait  un  animal  capable  de  se  recourber en  replis  tortueux,  un  serpent,  un  dragon.
LiLAS.  Esp.  hlaCj  portug.  Iilazaro.  Les  Arabes  disent jUJ,  ^"^i  Mac,  Mac.  (Meninski,  Onomast.  sm  mot  Synnifa Persica.)  Ces  mots,  qui  ne  sont  point  d'origine  arabe,  se rattachent  au  persan  Juj  iM,  indigo  (voy.  Anil);  on  trouve les  diverses  formes  persanes:  ^djj,  ^^>,  ^^■>  é^'  '^^'^'> nilah,  ndadj ,  Madj ,  Mandj,  Mang,  se  rapportant  toutes  à l'indigo;  ce  qui  montre  le  changement  de  n  initial  en  /. L'arabe   hlah  peut   être  pris   de  l'un  quelcon(|ue  de  ces
'   D'HerbeloI,  Biblioth.  nrientak ,  an  mot  Inuk.
15-2  DICTIONJNAIRE  ÉTYMOLOGIQUE
mots,  ou  mieux  encore,  je  [)ense,  du  diminulif  JXJ  hlak, bleuâtre,  comme  les  doigts  bleuis  par  le  froide  nuance qui  caractérise  parfaitement  les  fleurs  du  lilas  de  Perse, lesquelles  sont  d'un  pourpre  pâle  ^.
LiMo.'s.  Fruit.  Esp.  limon,  portug.  limào ,  ital.  limone. De  l'arabe-persan  ^^^  lëimoûn,  même  sens.
Plusieurs  espèces  de  citronniers  portent  aussi  le  nom de  lime,  esp.  et  portug.  lima;  en  arabe  iUJ  lima.  (Voy. Dozy,  Gloss.  p.  2(^-7.)
LisME.  Droit  qu'on  payait  aux  régences  barbaresques pour  la  pèche  du  corail.  De  l'arabe  ^^,  i^'y^  hlzim,  lâ- zima,  chose  obligatoire,  dette,  impôt.  (Defrémery.)M.  Gher- bonneau  donne  la  forme  i^\l  lezma  qui  convient  encore mieux  pour  l'étymologie.  i^Dichonn.  franc -arah.  au  mot tribut.  )
LoG.  Mesure  des  liquides  chez  les  Hébreux.  Transcrip- tion de  l'hébreu  t}  log.
Loocii.  Portug.  looch.  Terme  de  pharmacie ,  pris  de l'arabe  ^yO  laôq,  potion  qu'on  lèche,  c'est-à-dire  qu'on prend  à  petites  gorgées;  du  verbe  (^jtl  la  aq ,\échei\  lampcr.
FjOiu.  Nom  d'une  espèce  de  ])erroquet.  C'est  le  malais (^^^  loûrl  ou  t^^yj  noïiri,  qui  désigne  un  perroquet  des Moluques.  ^vLe  lori,  dont  les  teintes  rouges  si  variées  sur- passent en  splendeur  celles  de  la  plus  belle  tulipe.  '^ (Rienzi,  Océanie ,  ï,  p.  Ac).)
'   'sLilah,  a  lilllo  Mue,  Miii&li;  Miio  as  llie  fingors  \\\\h  roM  piiiclnii|;.'' (IVicliardson.)
^   Dicl.  iVhisl.  uni.  do  Ooloivillo,  I.  XVIII,  p.  .'>:>.
=== TTS 520-535 ===
türkischen Sprachen gehören und in den meisten Fällen auf s,
s und         t    zurückzuführen sind.
        13)        L und      it     sind     als   Anlaute den eigentlich             türkischen
Sprachen fremd und kommen als solche mit Ausnahme der
Fremdwörter und einiger Affixe nur einigemal vor. Der Ost-
türke spricht das anlautende l noch leicht aus, der Osmane nur,
indem er demselben einen Selbstlaut vorsetzt. So: iliman (Bucht),
üimon (Citrone), statt limav, limon. Als Auslaut wechselt l mit
j     (vgl.       Ul-i'ij   [Theil],        sil-sij    [reiben,      wischen]), mit          n (vgl.
kü-ltin [stechen, schneiden],                       col-con     [stumpf]     und mit r          (vgl.

tal-tur [gross, geräumig], tHl-tiir [gegenüber)].
     14) Das von l Gesagte gilt noch mehr von r, welches
als Anlaut im Westtürkischen nur mit Hülfe eines vorgesetzten
Vocals ausgesprochen werden kann.      So hat der Osmane
aus      den         Fremdwörtern Russ                  (Russe),     Rum         (Grieche),     rali
```


## [2026-09-07T19:35:57.491Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nfor fn,ln in (('PHN.txt',6755),('DEV.txt',1638)):\n    t=open(fn,encoding='utf-8',errors='replace').read()\n    lines=t.split('\\n')\n    ff=sum(l.count('\\f') for l in lines[:ln-1])\n    print(fn,'line',ln,'leaf',ff)\nEOF\necho \"=== TTS page tag ===\"\nawk 'NR<=530 && /\\[pdf page/ {p=$0} END{print p}' incoming/TTS/TTS_pages.txt\ngrep -n \"\\[pdf page\" incoming/TTS/TTS_pages.txt | awk -F: '$1<530' | tail -3"
}
```


### [2026-09-07T19:35:58.748Z] TOOL RESULT

```
PHN.txt line 6755 leaf 270
DEV.txt line 1638 leaf 185
=== TTS page tag ===
```


## [2026-09-07T19:36:02.751Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"page\" incoming/TTS/TTS_pages.txt | head -5\necho ---\npython3 - <<'EOF'\nt=open('incoming/TTS/TTS_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nimport re\nfor i in range(0,530):\n    if re.search(r'pdf page|\\f', lines[i]): print(i+1, lines[i][:60])\nEOF"
}
```


### [2026-09-07T19:36:04.124Z] TOOL RESULT

```
---
1     ETYMOLOGISCHES WÖRTERBUCH
12      ETYMOLOGISCHES WÖRTERBUCH
39           PL
48               MEINEM GEEHRTEN FREUNDE
69                            VORWORT.
101                                         VIII
146                                           IX
189                                            X
249                                        XI
293                                         XII
345                                         XIII
396                                             XIV
440                                          XV
489                                                       XVI
```


## [2026-09-07T19:36:16.737Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN limu ===\"; grep -n -i \"limu\\|Citrone\\|Zitrone\" HRN.txt | head -10\necho \"=== HUB limu ===\"; grep -n -i \"limu\\|Citrone\" HUB.txt | head -10\necho \"=== ARY limu ===\"; grep -n \"لیمو\" incoming/ARY/ARY_pages.txt | head -5\necho \"=== ARY latin ===\"; grep -n -i \"LIMU\\|LIMOU\" incoming/ARY/ARY_latin_index_pages.txt | head -5"
}
```


### [2026-09-07T19:36:16.823Z] TOOL RESULT

```
=== HRN limu ===
1735:153. hädreng 'Citrone*.
5699:Bedeutung 'sclimutzig, unrein* dem Worte nach der Überlieferung nicht
=== HUB limu ===
686:'Citrone' (Citronat-Citrone) sondem auch 'species cucu-
688:Im Altarmenischen klingt varung *Gurke, Citrone,
5426:212, zd. vdta-; bddrang 'Citrone =^ phi. vatrang\ badam
5613:Velum*; variing *Gurke, Citrone', np. badrang, balang, va-
=== ARY limu ===
=== ARY latin ===
```


## [2026-09-07T19:36:18.591Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN lemon ===\"; grep -n -i \"lemon\" SYN.txt | head -5\necho \"=== IEC nis ===\"; grep -n -i \"^nis-\\|nis- \" IEC.txt | head -5\necho \"=== FSD lime/lemon ===\"; ls FSD*; grep -n -i \"lemon,  n\\|LEMON\" FSD_vol3.txt 2>/dev/null | head -5\necho \"=== WEB ===\"; ls WEB*"
}
```


### [2026-09-07T19:36:18.690Z] TOOL RESULT

```
=== SYN lemon ===
=== IEC nis ===
4194:gnis- ‘filth’ G Knies (1) ‘filth’; Cz. Slovak hnis ‘pus’; (*-- in) OCS gníst, f. ‘filth’; gnïšọ, gnísiti ‘defile’. Radical in OCS gnijð, gniti, v. “turn bad’. (Isophonic Du. kniezen ‘sulk, whim- per’; G Knies (2) “quarrel')
7457:knis- ‘fret at, wear down, bore, dig’. WP I, 396 Ir. cf. cnis, f. ‘gap in warp’; W cf. cnyw *bad- ger”, fr. *knisius?; Gk. cf. knissós ‘glutton’; ON hnísa ‘porpoise’; Li. knisius ‘digger, go- getter’; knysys, io, m. ��snout’; knisti, v. ‘root up’; Latv. cf. knislis ‘midge’
9011:Knid- above, and knid- Gk. kníssa, knisa, f. id.; Lat. cf. nidor, Oris, m. id. (fr. *Knisd- with loss as in nidus); Br. krien, kriénen, m. “burnt crust’; Icel. cf. hnis- su-, cpds “of unpleasant taste”
=== FSD lime/lemon ===
FSD_vol1.txt
FSD_vol2.txt
FSD_vol3.txt
FSD_vol4.txt
2894:(Canfua 6uz(/oJtii) of the phlox family iPolemoniaee»), for-
14136:Bhoals 19. A county in £ Kentucky, 224 sq m.. county- Bot A famUy of herbs of the order Polemonialee with op-
15065:elemontsused having been eonsecratcd at a previous celebra-
45722:Rwtrr JJaueta and Philemon 1 08.
47089:of oranges lemons, olives, and other evergreen subtropi-
=== WEB ===
WEB_vol1.txt
```


## [2026-09-07T19:36:25.937Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FSD lemon vol2 ===\"; grep -n -i \"lem'on\\|lemon, n\\|Pers. limun\\|limun\" FSD_vol2.txt | head -8\necho \"=== FSD lime ===\"; grep -n -i \"Sp. lima\\|Ar. limah\\|limah\" FSD_vol2.txt FSD_vol3.txt | head -8\necho \"=== FSD nirvana ===\"; grep -n -i \"nirvana\" FSD_vol3.txt | head -5\necho \"=== IEC ni ===\"; grep -n \"ni- ‘down\\|ni ‘down\\|nis ‘out\" IEC.txt | head -5"
}
```


### [2026-09-07T19:36:26.125Z] TOOL RESULT

```
=== FSD lemon vol2 ===
74577:Le-moinne',  1   la-mwon':  2   le-mwiin',  JeanSilmlle  (lo/wlSlB- iVi4lS92).  A   French  journalist  and  author, lem'on,  i   lem'an;  2   Ifim'on,  vt.  To  impart  the  flavor  of  a   lemon to;  as,  to  lemon  an  Ice.
74579:lem'on,  n.  1.  The  fruit  of  the  tropical  or  subtropical tree  Citrus  medica  limonum,  of  the  family  Rutaceie.  It is  usually  ellipsoidal  tvith  a   protruding  point  at  each  end. The  rind  contains  the  oil  of  lemon.  Citric  add  is  ob- tained from  the  juice.  The  principal  varieties  cultivated in  the  United  States  are  the  Bclalr,  the  Eureka,  the Genoa,  the  Lisbon,  the  Sicily,  and  the  'Villafranca.
74583:1.  walnut,  the  white  walnut  or  butternut,—  lem'on- weed",  n.  A   flustrold  polyzoan.— lera'on-wood",  n. A   New  Zealand  tree  (Pittosporum  eugenipides)^  the  hedge- laurel  or  tarata.—  sweet  1.,  a   European  species  (Ciirtw  lumta) whose  oblong  yellow*rinded  fruit  with  a   curved  point  has a   very  sweet  pulp.—  water*!.,  n.  The  product  of  either  of two  tropical  American  trees  of  the  genus  Passiflora;  as (1)  Passiflora  lanrifoUa,  a   lemon»shaped  yellow  fruit  having a   watery  pulp  of  agreeable  flavor;  (2)  Passiflora  maliformis, a   smaller  fruit  of  similar  qualities  —   the  sweet  calaba.sh  of  the West  Indies.  The  wild  water-lemon  i.s  yielded  by  Passiflora fatida  and  Is  about  the  size  of  a   cherry.  It  has  a   very  deli- cately flavored  pulp.— wild  1.  1.  (U.  S.]  The  may-apple.
74585:Lem'on,  Mark  (1809-1ST0).  A   noted  English  novelist, humorist,  and  first  editor  of  Punch.
=== FSD lime ===
=== FSD nirvana ===
26565:perfsottoas of tho Buddha and the hops of obtaialas Nirvana.
58279:philosophy It was sometimes called Nirvana, a name
58283:JMu4(i. Moksha, or Nirvana
=== IEC ni ===
11581:nei- "down Cf. ni-, neiu- Gk. neí-atos ‘lowest’; neíara, adv. "lower; nei-óthen ‘from below’; nei-óthi “down below’; formant in OCS niže (‘below’, and com. Sl.); nici ‘face downward’; and in Slo- vene ni-Cati, inf. ‘crouch’; ni-hati, inf. ‘dangle’; z-gde in Skt. Av. ni- ‘down’; Oss. ní, ni, id.
```


## [2026-09-07T19:36:33.580Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '74579,74582p' FSD_vol2.txt | cut -c1-1200\necho \"=== IEC page ===\"\npython3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nff=sum(l.count('\\f') for l in lines[:11580])\nprint('leaf',ff, 'approx printed page', (ff-15)*2)\nprint(lines[11580][:400])\nEOF\necho \"=== IEC nis? ===\"\ngrep -n \"nis- ‘\\|niz- ‘\\|nis, adv\" IEC.txt | head"
}
```


### [2026-09-07T19:36:35.028Z] TOOL RESULT

```
lem'on,  n.  1.  The  fruit  of  the  tropical  or  subtropical tree  Citrus  medica  limonum,  of  the  family  Rutaceie.  It is  usually  ellipsoidal  tvith  a   protruding  point  at  each  end. The  rind  contains  the  oil  of  lemon.  Citric  add  is  ob- tained from  the  juice.  The  principal  varieties  cultivated in  the  United  States  are  the  Bclalr,  the  Eureka,  the Genoa,  the  Lisbon,  the  Sicily,  and  the  'Villafranca.
2.  The  tree  that  produces  this  fruit.  3.  The  color  of  a lemon.  4.  [Slang,  IT.  S.]  A   wmrthless  disappointing person  or  thing;  as,  he  Isa  imoK,- he  handed  me  a   lemon.  [< E.limon,  <   lAj.lirnoin-),  <   Per.  innan,  lemon.]
—   desert  lemon  [Austral.],  a   tree  (Aialantia  glatiea)  ofthe family  Rutaeex,  with  a   globular  fruit  about  half  an  Inch  In diameter,  from  who.se  acid  juice  Is  prepared  a   pleasant beverage.— essential  salt  of  1.,  acid,  potassium  oxalate,  or salt  of  sorrel.— Icm'on  ibalm",  n.  Same  as  balm,  n.,  3.— l.ddrd,  n.  [fjoeal,  Eng.)  Thcllnnet.— l.scadmlum,  «.  A pale»yellow  pigment  consisting  essentially  of  cadmium  sulfld: used  as  a   paint  both  with  oil  and  with  water.— l.scolor,  n. The  color  of  a   ripe  lemon;  yellow  with  a   greenish  tinge.—  l.i colored,  a.— l.=cuttlng,  n.  The  cleaving  of  a   suspended lemon  with  a   sword  by  one  riding  at  full  speed.— I.*dab,  n. [Local,  Ir.]  The  smear^dab.—l.  4drop,  M.  A   semi«trauslu- cont  drop  of  candy  flavored  with  lemon.;—  l.eflsh,  «.  An amber»flBh  {Seriola  siearnsi) .—  I.  *grass,  n.  Any  of  several Ea.st»Indtan  perennial  tutted  grasses,  especially  Andwpogon sehananth-m,  A.  citratus,  sua&  A.  nardus,  with  long  leaves, yielding  an  essential  odoriferous  oil  used  in  perfumery. See  ciTEONELLA  OIL  
a.  Scented  with  or  like  lemon.— I. fscented  gum,  an ornamental  tree  {Eucalyptus  macnlata  cliridora),  cul- tivated in  southern  California,  and  distinguished  by a   long  slender  trimk,  smooth,  white  hark,  and  drooping branches  bearing  narrow  lemon-scented  leaves  and  white flowers.  It  yields  a   volatile  oil  used  in  perfumery  and  a strong  durable  wood  employed  for  girders  and  wharf'piling. —   I.  scurvy sgrass,  same  as  scuevysgbass,  l.~I.=sole,  ii. Any  of  various  flatfishes,  edible,  but  ot  Inferior  quaUty,  as, specif.,  the  British  smear»dab  {Glyptoccphalttsmicrocephalus) . — l.^qnash,  n.  [Eng.]  Lemonade  made  with  soda»water.— I.csqucezer,  n.  An  Instrument  for  expressing  the  juice  of lemons.—  1.  thyme,  a   lemon'seented  variety  of  the  common creeping  thyme  {Thyrrms  serpyllum).—  l.stree,  n.  1-  Same as  lemon,  2.  2.  The  lemon-plant.—  1.  verbena,  a   South* American  shrub  {Lippia  ckrfodora),  cultivated  in  gardens for  the  fragrance  exhaled  by  Its  flowers  and  bruised  leaves. —
=== IEC page ===
leaf 465 approx printed page 900
nei- "down Cf. ni-, neiu- Gk. neí-atos ‘lowest’; neíara, adv. "lower; nei-óthen ‘from below’; nei-óthi “down below’; formant in OCS niže (‘below’, and com. Sl.); nici ‘face downward’; and in Slo- vene ni-Cati, inf. ‘crouch’; ni-hati, inf. ‘dangle’; z-gde in Skt. Av. ni- ‘down’; Oss. ní, ni, id.
=== IEC nis? ===
4194:gnis- ‘filth’ G Knies (1) ‘filth’; Cz. Slovak hnis ‘pus’; (*-- in) OCS gníst, f. ‘filth’; gnïšọ, gnísiti ‘defile’. Radical in OCS gnijð, gniti, v. “turn bad’. (Isophonic Du. kniezen ‘sulk, whim- per’; G Knies (2) “quarrel')
7457:knis- ‘fret at, wear down, bore, dig’. WP I, 396 Ir. cf. cnis, f. ‘gap in warp’; W cf. cnyw *bad- ger”, fr. *knisius?; Gk. cf. knissós ‘glutton’; ON hnísa ‘porpoise’; Li. knisius ‘digger, go- getter’; knysys, io, m. ��snout’; knisti, v. ‘root up’; Latv. cf. knislis ‘midge’
```


## [2026-09-07T19:36:45.452Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd2 ni ===\"; grep -n \"ni-, nei-\\|nitero\\|,nieder'\" incoming/WLD/WLD_Bd2_pages.txt | head -10\necho \"=== WLD band3 register ===\"; grep -n \"^ni \\|nitero\" WLD_band3.txt | head -10"
}
```


## [2026-09-07T19:36:45.478Z] TOOL CALL #59: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-07T19:36:45.484Z] TOOL RESULT

```


```


### [2026-09-07T19:36:45.535Z] TOOL RESULT

```
=== WLD Bd2 ni ===
=== WLD band3 register ===
```


## [2026-09-07T19:36:50.508Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%84%DB%8C%D9%85%D9%88",
 "prompt": "Give the full Persian etymology section for لیمو (limu) — what it derives from (Sanskrit? Malay? Arabic?), any Middle Persian form, and descendants/borrowings into Arabic, Turkish, European languages. Quote verbatim."
}
```


## [2026-09-07T19:36:51.915Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/lemon",
 "prompt": "Quote the full etymology entry for \"lemon\" and also for \"lemonade\" if present: the chain through Old French/Middle English, Arabic laimun, Persian limun, and any mention of Sanskrit nimbu or Malay."
}
```


### [2026-09-07T19:36:58.170Z] TOOL RESULT

```
# Persian Etymology of لیمو (limu)

## Etymology Source
The word derives from Sanskrit. According to the etymology section: "Borrowed from Sanskrit निम्बू (nimbū), borrowed from an Austroasiatic language."

The Sanskrit term itself came from Austroasiatic origins, making this a chain of borrowing across language families.

## Key Descendants and Borrowings

The term spread extensively into other languages through Arabic and other intermediate languages:

**Major Romance Language Borrowings:**
- English: "lemon"
- Spanish: "limón"
- Italian: "limone"
- Portuguese: "limão"
- Catalan: "llimona"

**Turkic Languages:**
- Turkish: "limon"
- Turkmen: "leýmun"

**Semitic and African Languages:**
The word entered Arabic as "لَيْمُون (laymūn)" and subsequently spread to Amharic, Tigrinya, Somali, and other East African languages.

**South Asian Languages:**
Hindi and Urdu also adopted forms like "लीमू (līmū)" and "لیموں (līmū̃)" respectively.

The page does not list a Middle Persian form explicitly, but shows the Persian term as a direct borrowing from Sanskrit rather than an inherited Persian word.
```


### [2026-09-07T19:36:58.739Z] TOOL RESULT

```
# Etymology of Lemon

**Lemon (n.1)** traces back through multiple linguistic layers:

"ovate, pale yellow citrus fruit," c. 1400, _lymon_, from Old French _limon_ "citrus fruit" (12c.), which comes via Provençal or Italian from Arabic _laimun_, Persian _limun_. The term likely originated "from an Austronesian word of the Malay archipelago, such as Balinese _limo_ 'lemon,' Malay _limaw_ 'citrus fruit, lime'."

The fruit itself was "brought from India to the Levant by the Arabs 9c. or 10c."

**Secondary meanings** developed later:
- "person with a tart disposition" (1863)
- "worthless thing" (1909)
- Slang for a Quaalude (1960s)

## Lemonade

The page lists "lemonade" as a related word linking to lemon, but does not provide a separate detailed etymology entry for lemonade itself in the content above.

**Note:** The etymology does not mention Sanskrit _nimbu_ in connection with lemon specifically—that reference appears only in the separate entry for lime (n.2).
```


## [2026-09-07T19:37:15.323Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/lime",
 "prompt": "Quote the etymology of lime (n.2), the citrus fruit: the chain through French lime, Provençal/Spanish lima, Arabic lima, Persian limun, and any mention of Sanskrit nimbu."
}
```


## [2026-09-07T19:37:16.785Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://www.cnrtl.fr/etymologie/limon",
 "prompt": "Quote the etymology given for the French word limon (the citrus fruit) and limonade: what language it was borrowed from (Arabic? Italian? Turkish? Persian?), with dates."
}
```


### [2026-09-07T19:37:19.687Z] TOOL RESULT

```
# Etymology of Lime (n.2) - The Citrus Fruit

According to the Online Etymology Dictionary, lime (the citrus fruit) entered English around the 1630s. The etymological chain traces as follows:

The word came "probably via Spanish _lima_ or Portuguese _limão_," which derived from Arabic _lima_ meaning "citrus fruit," ultimately from Persian _limun_.

The entry notes: "The word is perhaps from or related to Sanskrit _nimbu_ 'lime.'" The source suggests multiple possible origins for the ultimate root, including potential connections through Malay _limaw_ ("lime" or generically "citrus fruit"), with scholars proposing that English may have acquired the term from Portuguese traders in India.

This etymological path reflects the historical spread of the Persian lime through Arab trade networks into the Mediterranean and eventually to European languages.
```


### [2026-09-07T19:37:21.032Z] TOOL RESULT

```
I appreciate your question, but the provided web page content only shows "Portail lexical" (Lexical Portal), which appears to be a title or header with no actual etymological information included.

To answer your question about the etymology of French "limon" and "limonade," I would need access to the actual content of that lexical portal page, which hasn't been provided. The snippet shared doesn't contain any etymological data, source language information, or dates.

Could you provide the full page content or text that contains the etymology details you're asking about?
```


## [2026-09-07T19:37:26.997Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/limon",
 "prompt": "Quote the French section etymology for limon (citrus fruit) and the Turkish section etymology for limon: source languages named (Arabic, Persian, Italian, Greek?)."
}
```


## [2026-09-07T19:37:28.347Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://www.nisanyansozluk.com/kelime/limon",
 "prompt": "Quote the etymology given for Turkish limon: source language and forms (Persian limun? Arabic? Greek?), first attestation date."
}
```


### [2026-09-07T19:37:31.085Z] TOOL RESULT

```
# Etymology Sources for "Limon"

**French (citrus fruit):**
The entry states: "Borrowed from Italian limóne." Italian is the named source language for the French word meaning lemon.

**Turkish:**
According to the etymology tree provided, Turkish limon derives from Ottoman Turkish, which borrowed from Classical Persian līmū, which borrowed from Sanskrit nimbū, which was borrowed from an Austroasiatic language. The named source languages are Persian, Sanskrit, and Austroasiatic—not Arabic, Italian, or Greek.
```


### [2026-09-07T19:37:32.433Z] TOOL RESULT

```
I cannot provide the etymology information you're requesting. The web page content shown is only the header and footer of the Nişanyan Sözlük (Nişanyan Dictionary) website—it contains navigation elements, copyright information, and policy links, but does not include the actual dictionary entry for "limon" or any etymological details about the word's source language, historical forms, or first attestation date.

To find this information, you would need to access the full dictionary entry on the website itself.
```


## [2026-09-07T19:37:39.232Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/nirvana",
 "prompt": "Quote the English etymology of nirvana, and the Sanskrit निर्वाण (nirvāṇa) analysis: prefix nis-/nir- and the root vā 'to blow'. Any mention of Proto-Indo-Iranian *niš or PIE *ni-."
}
```


## [2026-09-07T19:37:40.383Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/ni%C5%A1",
 "prompt": "Quote the reconstruction page: Proto-Iranian *niš — its meaning, its Proto-Indo-Iranian and PIE ancestry, and its descendants (Avestan niš, Old Persian, Middle Persian)."
}
```


### [2026-09-07T19:37:41.711Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T19:37:43.599Z] TOOL RESULT

```
# Nirvana Etymology

**English Etymology Quote:**
"Borrowed from Sanskrit निर्वाण (nirvāṇa, "blown or put out, extinguished"), from निस् (nis, "out") +‎ वा (vā, "to blow")"

**Analysis:**
The word breaks down into two Sanskrit components: a prefix meaning "out" (nis-/nir-) combined with a verbal root meaning "to blow" (vā). This composition creates the literal sense of something being "blown out" or extinguished, which became the philosophical concept of cessation in Buddhist thought.

The source document does not mention Proto-Indo-Iranian or Proto-Indo-European etymologies for these Sanskrit elements.
```


## [2026-09-07T19:37:49.678Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%A8%E0%A4%BF%E0%A4%B8%E0%A5%8D",
 "prompt": "Quote the Sanskrit entry for निस् (nis): meaning, etymology (Proto-Indo-Iranian *niš, PIE *ni-s?), cognates in Avestan and Old Persian."
}
```


## [2026-09-07T19:37:52.115Z] TOOL CALL #69: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%86%DB%8C%D8%B1%D9%88%D8%A7%D9%86%D8%A7/",
 "prompt": "Quote what the Persian dictionaries (فرهنگ معین، فرهنگ عمید، دهخدا) say for نیروانا: definition and any origin tag (Sanskrit سنسکریت?)."
}
```


### [2026-09-07T19:37:55.646Z] TOOL RESULT

```
# Sanskrit Entry for निस् (nis)

Based on the Wiktionary content provided, here's what is documented:

## Meaning
The word निस् functions as an adverb meaning **"out, forth, away"** and related concepts. The entry notes it is **"rarely used independently"** but typically appears as a prefix to verbs and their derivatives.

## Etymology
The page references निस्- (nís-) but does not provide the Proto-Indo-Iranian or Proto-Indo-European etymologies you requested. The content states **"See निस्- (nís-)"** without offering detailed etymological reconstruction.

## Cognates
The provided text contains no information about Avestan or Old Persian cognates.

## Note
The entry appears incomplete regarding comparative Indo-European linguistics. The Wiktionary article focuses on the Sanskrit form itself, pronunciation (Vedic /nís/, Classical /n̪is̪/), and derived terms like निरय (niraya) and निर्वाण (nirvāṇa), but lacks the etymological depth you've requested.
```


### [2026-09-07T19:37:58.917Z] TOOL RESULT

```
# نیروانا - Persian Dictionary Definitions

## فرهنگ معین (Farhang-e Moein)
The page does not include a separate entry from Farhang-e Moein specifically.

## فرهنگ عمید (Farhang-e Amid)
The page does not include a separate entry from Farhang-e Amid specifically.

## دهخدا (Dehkhoda)
The page does not include a separate entry from Dehkhoda specifically.

## Available Persian Dictionary Entry (دانشنامه آزاد فارسی)

The most detailed Persian definition provided is from the Free Persian Encyclopedia:

"درحوزۀ پژوهش های غربی، مجادله های فراوانی در خصوص ماهیت آن جریان داشته است" - discussing Western scholarly debates about its nature

**Origin Tag:** Sanskrit (سانسکریت) - derived from a verb meaning "to cool down" or "to extinguish," like extinguishing a candle. The term's essential meaning reflects the extinguishing of flames of desire, hatred, greed, and ignorance.
```


## [2026-09-07T19:38:05.460Z] TOOL CALL #70: WebFetch

```json
{
 "url": "https://vajehyab.com/?q=%D9%86%DB%8C%D8%B1%D9%88%D8%A7%D9%86%D8%A7&d=moein",
 "prompt": "Does Mo'in's Farhang have an entry for نیروانا? Quote it with any origin tag in brackets (e.g. [سنسکریت])."
}
```


### [2026-09-07T19:38:08.650Z] TOOL RESULT

```
Based on the web page content provided, **no, Mo'in's Farhang does not have an entry for نیروانا (Nirvana)**. 

The page displays: "«نیروانا» پیدا نشد!" ("نیروانا was not found!"), and suggests users either check the word spelling or propose a new entry for this term.
```


## [2026-09-07T19:38:11.681Z] TOOL CALL #71: Bash

```json
{
 "command": "timeout 300 python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%84%DB%8C%D9%85%D9%88' --note 'page 366, root Nimbu/Limu, Persian limu < Sanskrit nimbu < Austroasiatic; descendants' 2>&1 | tail -3\ntimeout 300 python3 tools/fetch_source.py 'https://www.etymonline.com/word/lemon' --note 'page 366, node 6 English lemon: OFr limon via Provencal/Italian < Ar laimun < Pers limun; Malay/Austronesian limaw' 2>&1 | tail -3\ntimeout 300 python3 tools/fetch_source.py 'https://www.etymonline.com/word/lime' --note 'page 366, node 9 English lime: via Spanish lima/Portuguese limao < Ar lima < Pers limun; rel. Skt nimbu' 2>&1 | tail -3\ntimeout 300 python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/limon' --note 'page 366, node 4 French limon < Italian limone; Turkish limon < Ottoman < Classical Persian limu < Skt nimbu' 2>&1 | tail -3\ntimeout 300 python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/nirvana' --note 'page 366 entry 1, nodes 2/4: Skt nirvana = nis- out + va- to blow' 2>&1 | tail -3"
}
```


### [2026-09-07T19:38:15.304Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/623f769081c78bc2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e1855d14f1e6936a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3a608fb5a8d1ab04.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f190b4a96e1b7c12.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5da585b195df37a2.txt
```


## [2026-09-07T19:38:25.206Z] TOOL CALL #72: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1922.png"
}
```


### [2026-09-07T19:38:25.818Z] TOOL RESULT

```

```


## [2026-09-07T19:38:25.816Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-09-07T19:38:58.939Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\ncat > data/verification/sources/refs/ocr/BQT/1922.vision.txt <<'EOF'\n[Borhan-e Qate', ed. Mo'in, printed page 1922 (BQT_v3_picofile.pdf pdf page 719) — read from the\nrendered PNG (1922.png) by claude-opus-5, 2026-09-07. Headwords in the right-hand column:\nلیلیا / لیمو / لیمو دارو / لیمونیون / لینج ; left column: لیلوفر / لیو / لیوک / لیولنگ.]\n\nColumn head (right): لیلیا ۱ ـ با لام بروزن اثیا، بلغت زند وپازند(۱) بمعنی شب است که عربان لیل گویند.\n\nلیمو ۲ ـ با اول بثانی رسیده و میم بواو کشیده . معروف است . گویند آب لیمو دفع سم\nمار و عقرب میکند؛ و بعضی گویند نام درختیست که میوهٔ آن لیمو است .\n\nلیمو دارو ـ با دال ابجد بالف کشیده و برای قرشت بواو رسیده ، نباتیست کوهی که در بهار\nاز میان درزهای سنگ بر می‌آید و بوی لیمو میکند و آنرا بعربی وشیج گویند .\n\nلیمونیون ـ بکسر نون و تحتانی بواو کشیده و بنون زده ، بلغت سریانی دوائی است که\nبیخ آنرا بشیرازی حلیم خوانند. ضماد کردن آن درد مفاصل و نقرس را نافع است .\n\n[Mo'in's numbered footnotes at the foot of the page:]\n\n۱ ـ هز lailyâ ، llaillnyâ ، lêlyâ ، پهلوی shap ( شب ) ، «یونکر ۱۰۷» .\n\n۲ ـ اصل این نبات از هند است و نام آن هم هندیست «نمبو» ، در سانسکریت\n    [Devanagari: निम्बूकः  = nimbūka-]  ، «زابا ص ۳۸۴» .  لیمو = لیمون ( ع ) = limon ( فر )\n    = citrus limonium .  نزد قدما لیمو قسمی از مرکبات که ترش و معطر است و خود و آب آنرا\n    در چای و خورشها کنند و در ولایات ساحلی بحر خزر و فارس بعمل می‌آید «لغت‌نامه» و امروز\n    آنرا لیموترش گویند ـ لیمو در زمان ما غالباً به لیمو شیرین اطلاق شود که آنهم از مرکبات و\n    دارای پوست نازک زرد رنگی است و طعم وی شیرین است .\n\n۳ ـ = نیلوفر (ه.م.) = نیلوپل = نیلوپر = لیلوپل = لیلوپر .\nEOF\nwc -l data/verification/sources/refs/ocr/BQT/1922.vision.txt; ls -la data/verification/sources/refs/ocr/BQT/1922.png"
}
```


### [2026-09-07T19:38:59.013Z] TOOL RESULT

```
27 data/verification/sources/refs/ocr/BQT/1922.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 385933 Sep  7 15:35 data/verification/sources/refs/ocr/BQT/1922.png
```


## [2026-09-07T19:39:05.979Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PLA context ===\"; sed -n '13600,13640p' incoming/PLA/PLA_pages.txt | cut -c1-200\necho \"=== PLA limu entry ===\"; grep -n \"līmū\\|limü\\|limu \" incoming/PLA/PLA_pages.txt | head -10"
}
```


### [2026-09-07T19:39:06.052Z] TOOL RESULT

```
=== PLA context ===
&=-            lilaß = nilag a. v. <                                       pers. Sus 1ilak                  "Flieder"     — engl.         lilac,
          afrz.             lilac,                nfrz.           lilas     8,

     _                 -            _

sl) - lilaki:                                "blaßviolett,                  fliederfarben",                  dtsch.     lila
                                                                                                                          skr. >pers>>
           ar.             > sp.                2,


©,         - laimün,                         limün:            "Zitrone"          pers.          10,


1. BQ.             s. v.,                 Muhlt          s. v.
2.    Ellenbogen                          Ss.     v.
3.    Macuch                S.          v.
4. Muhlt                   s.       v.,         al-MuCarrab               s.     v.
5, TaCälivi figh al-luga s. v., Kamäl                                                            s. v.
6.    Fraenkel                      Ss.      v.
7.    Mackenzie                         s.      v.
8.    Genaust                   S.        v.
9.    Fremdwörterbuch                                   S.    v.
10. Muhit s. v.,                                  al-Munfid             s. v.,         Littmann            s. v.,     Genaust    s.v.
laimun                                                                       243                                                               mä&5Un


                                                                                                 1
          limone       — pers.                       limu,           mand.            nimuia
                                                                                        2
          limone           it.          limone >> pers.                    Limu
                                                                             3
          limone       —T pers.               >er. >                 it.         ”.
                                                                                                                                           4
          limetta:          "dünnschalige                      Zitronenart"_                     pers.        —> ar. >             it.
          limah:       (Citrus,               saure        Limette),                  frz.     lime,     sp.       lima      s.    limon
          limünäd:          "Limcenade;               Erfrischungsgetränk"                             aus     Fruchtsaft,               Zucker    u.
          Wasser;          auch         künstlich              mit    Kohlensäurezusatz                       pers.               _>ar.        >> frz.


Ol,»       -    1iwän:          "liwan;            Vorhalle           mit        Säulen,         Vorzimmer"              (für      pers.        al-Iwän)
          pers.       7,
=== PLA limu entry ===
13610:©,         - laimün,                         limün:            "Zitrone"          pers.          10,
13635:          limünäd:          "Limcenade;               Erfrischungsgetränk"                             aus     Fruchtsaft,               Zucker    u.
14900:see - nimü = limu q. v. 10,
```


## [2026-09-07T19:39:17.537Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"ليمون\\|الليمون\\|ليمو\" AFM_pages.txt AFM.txt AFM_alt.txt 2>/dev/null | head -10\necho \"=== nimu ===\"\nsed -n '14895,14905p' incoming/PLA/PLA_pages.txt | cut -c1-200"
}
```


### [2026-09-07T19:39:17.611Z] TOOL RESULT

```
=== nimu ===


ug           - nimbri$t:                  "weichgekochte                 Eier"         pers.        ıc     mp.    -#' nem "halb"          u.
        „ub, briät aus briftan                             "rösten".

see - nimü = limu q. v. 10,

>?    >= - nainufar                   = nilüfar            q.    v.          .


                                                                         [bi
```


## [2026-09-07T19:39:33.689Z] TOOL CALL #76: Bash

```json
{
 "command": "ls site/pages/366.jpg 2>/dev/null || pdftoppm -f 366 -l 366 -r 150 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg366 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/"
}
```


### [2026-09-07T19:39:34.954Z] TOOL RESULT

```
site/pages/366.jpg
total 32088
drwx------ 2 sfmqrb sfmqrb     4096 Sep  7 15:38 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  7 11:48 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     8635 Sep  7 12:07 318-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   101267 Sep  7 12:07 318-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61586 Sep  7 12:18 320-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115970 Sep  7 12:18 320hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86272 Sep  7 12:18 320-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13284 Sep  7 12:18 320-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   107524 Sep  7 12:27 328-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    43713 Sep  7 12:35 331-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   135301 Sep  7 12:35 331-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    52382 Sep  7 12:41 333-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    88345 Sep  7 12:41 333-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68568 Sep  7 12:43 335-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   105946 Sep  7 12:43 335-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   111897 Sep  7 13:57 340hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24993 Sep  7 13:57 340-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92337 Sep  7 13:59 342-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92697 Sep  7 13:56 343hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30778 Sep  7 13:56 343-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61503 Sep  7 13:52 346-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81599 Sep  7 14:37 350-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    99691 Sep  7 14:40 351-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115624 Sep  7 14:43 355-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    85914 Sep  7 14:35 358hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    19549 Sep  7 14:35 358-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    74812 Sep  7 14:35 358-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1579505 Sep  7 14:24 afm76.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1055262 Sep  7 14:23 afm77.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1297 Sep  7 15:29 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    14937 Sep  7 11:56 arrows.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1413 Sep  7 12:27 box1b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1385 Sep  7 12:27 box1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1132 Sep  7 12:27 box2b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1988 Sep  7 12:27 box2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    85949 Sep  7 11:57 bqt2002_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72256 Sep  7 11:58 bqt2002_f1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   161214 Sep  7 11:57 bqt2002_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   153966 Sep  7 13:44 bqt2014_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   299343 Sep  7 15:34 bqt2173_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79304 Sep  7 15:38 bqt2195_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59998 Sep  7 15:38 bqt2210_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63319 Sep  7 12:40 build333.py
-rw-rw-r-- 1 sfmqrb sfmqrb    83643 Sep  7 12:12 build.py
-rw-rw-r-- 1 sfmqrb sfmqrb     7075 Sep  7 12:13 c331_av1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10759 Sep  7 12:13 c331_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11800 Sep  7 14:19 c355_arab2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7474 Sep  7 14:19 c355_conn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10501 Sep  7 14:19 c355_runik2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7270 Sep  7 14:19 c355_runik.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3537 Sep  7 11:53 c_migare2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1829 Sep  7 11:53 c_migare3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2261 Sep  7 11:53 c_migare4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3958 Sep  7 11:53 c_migare.png
-rw-rw-r-- 1 sfmqrb sfmqrb    46690 Sep  7 13:44 crop_av3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40759 Sep  7 13:44 crop_heb.png
-rw-rw-r-- 1 sfmqrb sfmqrb    94819 Sep  7 13:44 crop_pers0.png
-rw-rw-r-- 1 sfmqrb sfmqrb    19652 Sep  7 11:53 c_semita2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2639 Sep  7 11:53 c_semita.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40259 Sep  7 11:50 ferdowsi2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30950 Sep  7 11:51 ferdowsi3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    28946 Sep  7 11:51 ferdowsi4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4298 Sep  7 11:50 ferdowsi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78732 Sep  7 13:40 ffd32.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30152 Sep  7 15:34 ffd77_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61328 Sep  7 15:34 ffd77.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61328 Sep  7 13:44 ffd82.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9383 Sep  7 11:55 masjid.wiki
-rw-rw-r-- 1 sfmqrb sfmqrb    33701 Sep  7 12:04 mk319a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    46151 Sep  7 12:09 mk319b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    51516 Sep  7 12:09 mk322.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61981 Sep  7 12:06 mk323.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63978 Sep  7 12:35 mk330.py
-rw-rw-r-- 1 sfmqrb sfmqrb    64100 Sep  7 12:34 mk331.py
-rw-rw-r-- 1 sfmqrb sfmqrb    90456 Sep  7 12:42 mk332.py
-rw-rw-r-- 1 sfmqrb sfmqrb    99976 Sep  7 12:34 mk334.py
-rw-rw-r-- 1 sfmqrb sfmqrb    57252 Sep  7 12:38 mk337.py
-rw-rw-r-- 1 sfmqrb sfmqrb    83271 Sep  7 13:58 mk338.py
-rw-rw-r-- 1 sfmqrb sfmqrb    74349 Sep  7 13:57 mk340.py
-rw-rw-r-- 1 sfmqrb sfmqrb    59512 Sep  7 13:57 mk341.py
-rw-rw-r-- 1 sfmqrb sfmqrb    82502 Sep  7 13:57 mk342.py
-rw-rw-r-- 1 sfmqrb sfmqrb    66284 Sep  7 13:55 mk343.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58811 Sep  7 13:57 mk344.py
-rw-rw-r-- 1 sfmqrb sfmqrb    36436 Sep  7 13:51 mk348b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    20510 Sep  7 13:47 mk348.py
-rw-rw-r-- 1 sfmqrb sfmqrb    67410 Sep  7 14:53 mk353.py
-rw-rw-r-- 1 sfmqrb sfmqrb    87481 Sep  7 14:40 mk354.py
-rw-rw-r-- 1 sfmqrb sfmqrb    38634 Sep  7 14:34 mk358.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61503 Sep  7 13:42 navak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3021 Sep  7 13:42 navak.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1525 Sep  7 13:41 p342_box2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1759 Sep  7 13:41 p342_box3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1703 Sep  7 13:41 p342_box.png
-rw-rw-r-- 1 sfmqrb sfmqrb   108903 Sep  7 13:41 p342hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10531 Sep  7 13:39 p343_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30408 Sep  7 13:39 p343_mus.png
-rw-rw-r-- 1 sfmqrb sfmqrb   103027 Sep  7 14:19 p355hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86505 Sep  7 14:27 p358_av.png
-rw-rw-r-- 1 sfmqrb sfmqrb   114524 Sep  7 14:19 p358hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    37883 Sep  7 14:20 p358_q2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    36134 Sep  7 14:20 p358_q3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4274 Sep  7 14:19 p358_quote.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4789 Sep  7 15:38 p361_empty2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4152 Sep  7 15:38 p362_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3458 Sep  7 15:35 p362_germ1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2606 Sep  7 15:35 p362_germ2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   135659 Sep  7 15:34 p363_mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb   223838 Sep  7 15:34 p363_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    21223 Sep  7 13:47 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb    37635 Sep  7 12:04 part_a.json
-rw-rw-r-- 1 sfmqrb sfmqrb    58545 Sep  7 12:09 part_b.json
-rw-rw-r-- 1 sfmqrb sfmqrb     5736 Sep  7 14:43 patch354.py
-rw-rw-r-- 1 sfmqrb sfmqrb    97817 Sep  7 11:50 pg318hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    62558 Sep  7 11:50 pg318.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67293 Sep  7 11:54 pg319.png
-rw-rw-r-- 1 sfmqrb sfmqrb   146848 Sep  7 12:01 pg320hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80891 Sep  7 12:00 pg320.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71522 Sep  7 12:00 pg321.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72193 Sep  7 11:57 pg323.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65279 Sep  7 11:49 pg324.png
-rw-rw-r-- 1 sfmqrb sfmqrb    55902 Sep  7 11:58 pg326.png
-rw-rw-r-- 1 sfmqrb sfmqrb   163982 Sep  7 11:53 pg327hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    73619 Sep  7 11:52 pg327.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69765 Sep  7 12:12 pg329.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72757 Sep  7 12:13 pg330.png
-rw-rw-r-- 1 sfmqrb sfmqrb   128240 Sep  7 12:13 pg331hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    94945 Sep  7 12:12 pg331.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75312 Sep  7 12:17 pg332.png
-rw-rw-r-- 1 sfmqrb sfmqrb   104609 Sep  7 12:27 pg333hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70886 Sep  7 12:26 pg333.png
-rw-rw-r-- 1 sfmqrb sfmqrb    41782 Sep  7 12:18 pg334_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    97297 Sep  7 12:18 pg334.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58407 Sep  7 12:18 pg334_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    88659 Sep  7 12:22 pg335.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57846 Sep  7 12:31 pg336.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60414 Sep  7 12:19 pg337.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65267 Sep  7 13:37 pg338.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63922 Sep  7 13:44 pg339.png
-rw-rw-r-- 1 sfmqrb sfmqrb   111897 Sep  7 13:44 pg340hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64116 Sep  7 13:39 pg341.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75149 Sep  7 13:40 pg342.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64151 Sep  7 13:39 pg343.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60735 Sep  7 13:42 pg344.png
-rw-rw-r-- 1 sfmqrb sfmqrb   168870 Sep  7 13:42 pg346hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76794 Sep  7 13:39 pg346.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59757 Sep  7 14:29 pg349.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70743 Sep  7 14:25 pg350.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86553 Sep  7 14:25 pg351.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69045 Sep  7 14:18 pg355.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78195 Sep  7 14:27 pg357.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49496 Sep  7 14:19 pg358.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82867 Sep  7 15:38 pg359.png
-rw-rw-r-- 1 sfmqrb sfmqrb    45536 Sep  7 15:36 pg360.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57895 Sep  7 15:38 pg361.png
-rw-rw-r-- 1 sfmqrb sfmqrb   111691 Sep  7 15:34 pg362hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76202 Sep  7 15:29 pg362.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66511 Sep  7 15:33 pg363.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49805 Sep  7 15:37 pg364.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59224 Sep  7 15:34 pg367.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49419 Sep  7 15:35 pg368.png
-rw-rw-r-- 1 sfmqrb sfmqrb        0 Sep  7 13:36 queue.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  3120575 Sep  7 14:24 skeat1882.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  2985742 Sep  7 14:25 skeatdli.txt
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 14:29 sns_0022.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 14:29 sns_0158.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 12:17 sns53.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4676 Sep  7 14:29 sns_meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb   135853 Sep  7 14:30 sns_n157.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   129673 Sep  7 14:30 sns_n159.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   113320 Sep  7 14:30 sns_n21.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n53.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n54.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  1021826 Sep  7 12:18 sns_p54.png
-rw-rw-r-- 1 sfmqrb sfmqrb 12288786 Sep  7 12:18 sns_text.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb      341 Sep  7 13:46 s.py
-rw-rw-r-- 1 sfmqrb sfmqrb   116699 Sep  7 14:30 t1.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb     1308 Sep  7 11:54 v2001.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    27253 Sep  7 12:02 z_maqd2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63140 Sep  7 12:02 z_maqd3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4293 Sep  7 12:01 z_maqd.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2895 Sep  7 12:01 z_meh.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25378 Sep  7 12:01 z_mezna2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    33685 Sep  7 12:01 z_mezna.png
```


## [2026-09-07T19:39:41.113Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\nfor f in skeat1882.txt skeatdli.txt; do echo \"==== $f ====\"; grep -n -i \"LEMON\" $f | head -5; done"
}
```


### [2026-09-07T19:39:42.349Z] TOOL RESULT

```
==== skeat1882.txt ====
39971:Lemon.  (F.  —  Pers.)   Formerly  limon. 
39973:-  F.  limon.  -  Ters.  limiin,  limtind,  a  lemon, 
40984:F.  lime.  —  Pers.  limit,  a  lemon,  citron.  See 
40985:Lemon. 
60562:spirit,  water,  lemon-juice,  sugar,  spice  ;  in- 
==== skeatdli.txt ====
43219:lemon, citron. Of Malay origin. 
43967:F. lime. — Pers limu, (also llmun), a lemon, 
61473:spirit, water, lemon-juice, sugar, spice ; in- 
89750:of orange or lemon-peel, used for flavour- 
89754:is divided,’ Cot. ; hence, a slice of lemon-
```


## [2026-09-07T19:39:47.949Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\necho \"=== skeatdli lemon ===\"; sed -n '43210,43225p' skeatdli.txt\necho \"=== skeatdli lime(3) ===\"; sed -n '43960,43975p' skeatdli.txt\necho \"=== page markers near ===\"; python3 - <<'EOF'\nimport re\nt=open('skeatdli.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor n in (43219,43967):\n    for i in range(n-1,max(0,n-120),-1):\n        m=re.search(r'^\\s*(\\d{2,3})\\s*$', lines[i])\n        if m: print(n,'prev page marker',m.group(1),'line',i+1); break\n    for i in range(n,min(len(lines),n+120)):\n        m=re.search(r'^\\s*(\\d{2,3})\\s*$', lines[i])\n        if m: print(n,'next page marker',m.group(1),'line',i+1); break\nEOF"
}
```


### [2026-09-07T19:39:49.251Z] TOOL RESULT

```
=== skeatdli lemon ===
Iiemniscate, a curve like the figure 8. 
(L. — Gk. ) From 1 lemmsedt-us, adorned 
with a ribbon. — L. lemniscus, a pendent 
libbon. — Gk. k-q^xviatco^, a fillet. Said to 
be from Gk. krjvos, wool ; which is allied 
to Wool. 

l^exnon. (F. — Pers.) Formerly 
— k. limon. — Pers. limim, limund, a 
lemon, citron. Of Malay origin. 

Xiemur, a nocturnal animal. (L.) L. 
lemur, a ghost ; so nicknamed by natural- 
ists from its nocturnal habits. 

Xieud. (E.) The final d is excrescent. 
=== skeatdli lime(3) ===
a cormption of line, as in Shak. Temp. v. 
10; and line is a corruption of Itnd, 
the lengthening of 1 having occasioned 
the loss of d, (Sweet, E. Gr. § 1607.) 
See Lind. 

Iiime {?,), a kind of citron. (F. — Pers.) 
F. lime. — Pers limu, (also llmun), a lemon, 
citron. — Malay liman, a lime, a citron. 
Idmehound, a dogin aleash. (Hybrid ; 
F. — L„ and E.) Shoit for ham-hound, 
used by Turberville. The M. E. Ham or 
lyam means *a leash.’ — O.F, Hem, now 
spelt Hen, a band ; Guernsey Ham, Han. 
— L. Hgdmen, a tie. See Lien, Liane. 
I^imit. (F.~L.) F. hmite, a limit - 
=== page markers near ===
43219 next page marker 290 line 43241
43967 next page marker 295 line 43988
```


## [2026-09-07T19:40:04.758Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\npython3 - <<'EOF'\nimport re\nt=open('skeatdli.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor i,l in enumerate(lines[43100:44100], start=43101):\n    m=re.search(r'^\\s*(\\d{2,3})\\s*$', l)\n    if m: print(i, m.group(1))\nEOF\necho \"=== headers around 295 ===\"\nsed -n '43980,43995p' skeatdli.txt"
}
```


### [2026-09-07T19:40:06.142Z] TOOL RESULT

```
43241 290
43697 293
43988 295
=== headers around 295 ===

Idmn, to illuminate, paint. (F.-L.) 

M. E. hmnen, contracted form of luminen, 
to illuminate (Prompt. Parv.). Again, 
luminen is for enlununen.^O,Y^ enlu- 


295 



LIMP 


LINNET
```


## [2026-09-07T19:40:17.177Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\nsed -n '43690,43712p' skeatdli.txt; echo \"-----\"; sed -n '43235,43252p' skeatdli.txt"
}
```


### [2026-09-07T19:40:17.252Z] TOOL RESULT

```
Russ Igaie, luigate, to lie; loje, a lie, 
(VEEUGH.) 

Lief, dear. (E.) Id.Y.leef, A.S. leaf. 
E-Du. lief, Icel l;ufr, Swed. Ijuf Goth. 
Hubs, G. lieb. Teut. type *leuboz. Cf, 

293 



LIEGE 


LIGHTS 


Russ, iioboif agreeable, liobite^ to love; 

L. iiibet^ libet, it pleases; Skt. lubh, to 
desire. (-^LEUBH.) Allied to Love. 

faithful, subject. (F. — O. H. G.) 
-----
S( e Long. Der. length-en. 

ienient, mild. (L.) Fiom pres. part, 
of L. lenh'e, to soothe. — L. lenis, soft, mild. 


290 



LENITY 


LETHE 


lenity. (F. — L.) O. F. /eniu, mild- 
ness (obsolete). — L. lenitatem^ acc. of
```


## [2026-09-07T19:40:41.541Z] TOOL CALL #81: Bash

```json
{
 "command": "cat .gitignore 2>/dev/null | head -30; echo ---; git check-ignore -v data/verification/sources/refs/SKT.txt; echo \"rc=$?\""
}
```


### [2026-09-07T19:40:42.694Z] TOOL RESULT

```
# regenerable from the PDF via pdftoppm (see tools/)
data/pages/

# built site (regenerate with tools/build_site.py)
site/risheh.html
__pycache__/

# Verification: OCR texts of copyrighted reference works (local audit copies only)
data/verification/sources/refs/
---
.gitignore:9:data/verification/sources/refs/	data/verification/sources/refs/SKT.txt
rc=0
```


## [2026-09-07T19:40:48.942Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/skeatdli.txt data/verification/sources/refs/SKT_dli_revised.txt\nls -la data/verification/sources/refs/SKT_dli_revised.txt\ngrep -n \"Lime {?,), a kind of citron\\|a kind of citron\" data/verification/sources/refs/SKT_dli_revised.txt | head"
}
```


### [2026-09-07T19:40:50.323Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 2985742 Sep  7 15:40 data/verification/sources/refs/SKT_dli_revised.txt
43966:Iiime {?,), a kind of citron. (F. — Pers.)
```


## [2026-09-07T19:40:58.293Z] TOOL CALL #83: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=lemon",
 "prompt": "Quote the etymology bracket of the AHD entry for \"lemon\" (and lime if shown): the chain of languages named."
}
```


## [2026-09-07T19:40:59.147Z] TOOL CALL #84: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=nirvana",
 "prompt": "Quote the etymology bracket of the AHD entry for \"nirvana\": the Sanskrit analysis (nis- + va-) and the IE root cross-reference."
}
```


### [2026-09-07T19:41:02.842Z] TOOL RESULT

```
# Etymology of "Lemon"

According to the dictionary entry, the etymology traces through these languages:

"Middle English _limon_, from Old French, from Old Italian _limone_, from Arabic _laymūn_, ultimately from alteration of Persian _līmū_"

The chain of linguistic descent flows from Persian through Arabic, Old Italian, and Old French before arriving in Middle English. The entry notes this involved "an alteration (probably influenced by an Andalusian Romance augmentative suffix akin to Spanish _\-ón_) of Persian _līmū_."

The entry also references a "LIME" entry for related etymological information, though that specific chain is not detailed in this excerpt.
```


### [2026-09-07T19:41:04.819Z] TOOL RESULT

```
# Nirvana Etymology

According to the American Heritage Dictionary entry, the Sanskrit analysis is:

"Sanskrit _nirvāṇam_, a blowing out, extinction, nirvana : _nis-, nir-_, out, away + _vāti_, it blows"

The entry references the Indo-European root connection with:

"see **wē\-** [in the Appendix of Indo-European roots]"

This indicates the Sanskrit _vāti_ (it blows) traces back to the reconstructed IE root *wē-.
```


## [2026-09-07T19:41:13.189Z] TOOL CALL #85: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=lime",
 "prompt": "Quote the etymology bracket of the AHD entry for \"lime\" the citrus fruit (lime2 or lime3): the chain of languages named (French, Spanish, Arabic, Persian)."
}
```


### [2026-09-07T19:41:15.931Z] TOOL RESULT

```
# Etymology of Lime (Citrus Fruit)

The etymological chain for the citrus fruit "lime" traces through these languages:

"French, from Spanish _lima_, from Arabic _līma_, from Persian _līmū_"

This progression shows how the word entered European languages through Romance language intermediaries before reaching English, ultimately deriving from Persian origins.
```


## [2026-09-07T19:41:16.511Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in 'https://www.ahdictionary.com/word/search.html?q=lemon' 'https://www.ahdictionary.com/word/search.html?q=nirvana' 'https://www.ahdictionary.com/word/search.html?q=lime' 'https://en.wiktionary.org/wiki/%E0%A4%A8%E0%A4%BF%E0%A4%B8%E0%A5%8D' 'https://abadis.ir/fatofa/%D9%86%DB%8C%D8%B1%D9%88%D8%A7%D9%86%D8%A7/'; do timeout 300 python3 tools/fetch_source.py \"$u\" --note 'page 366: AHD/Wiktionary/abadis lookups for lemon, lime, nirvana, Skt nis-' 2>&1 | tail -1; done"
}
```


### [2026-09-07T19:41:21.055Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/2fa51328ec271028.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/214dc3adcada1e85.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/75c5e726d4dfa802.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/93e0d7fb6a684c84.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bb017621448cefe2.txt
```


## [2026-09-07T19:41:29.543Z] TOOL CALL #87: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%84%D8%A7%DB%8C%D9%85/",
 "prompt": "Is there a Persian entry for لایم? Quote any definition and origin tag (English? لیمو? a drink?)."
}
```


### [2026-09-07T19:41:34.381Z] TOOL RESULT

```
# Persian Entry for لایم

Yes, there is a Persian entry. According to the dictionary source provided:

**Definition**: "ملامت کننده، نکوهش کننده، سرزنش کننده" (one who reproaches, blames, or censures)

**Origin**: The entry notes it derives from "لائم" and is classified as a noun (اسم) with plural forms "لائمین" or "لوائم."

**English equivalent**: "reprover"

This is not related to a drink or لیمو (lemon). It's an Arabic-origin Persian word meaning someone who criticizes or finds fault.
```


## [2026-09-07T19:42:04.972Z] TOOL CALL #88: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/366.jpg"
}
```


### [2026-09-07T19:42:04.991Z] TOOL RESULT

```

```


## [2026-09-07T19:42:27.085Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\npython3 -c \"\nfrom PIL import Image\nim=Image.open('/home/sfmqrb/git/rishe/site/pages/366.jpg')\nprint(im.size)\nw,h=im.size\n# crop region of the empty box: in displayed 1100x1400 approx coords x 640-870, y 565-650\nsx=w/1100.0; sy=h/1400.0\nim.crop((int(600*sx),int(555*sy),int(880*sx),int(660*sy))).resize((int(280*sx*3),int(105*sy*3))).save('p366_empty.png')\n\"\nls -la p366_empty.png"
}
```


### [2026-09-07T19:42:28.657Z] TOOL RESULT

```
(1100, 1423)
-rw-rw-r-- 1 sfmqrb sfmqrb 13022 Sep  7 15:42 p366_empty.png
```


## [2026-09-07T19:42:31.669Z] TOOL CALL #90: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/p366_empty.png"
}
```


### [2026-09-07T19:42:31.685Z] TOOL RESULT

```

```


## [2026-09-07T19:42:38.557Z] TOOL CALL #91: Bash

```json
{
 "command": "sed -n '60,140p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-07T19:42:38.603Z] TOOL RESULT

```
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


## [2026-09-07T19:42:58.328Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\ntimeout 300 python3 tools/fetch_source.py 'https://vajehyab.com/?q=%D9%86%DB%8C%D8%B1%D9%88%D8%A7%D9%86%D8%A7&d=moein' --note 'page 366 entry 1 node 3: Moin lexicon (vajehyab) has NO entry for نیروانا — negative result for MON:4882' 2>&1 | tail -1\ntimeout 300 python3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D9%84%D8%A7%DB%8C%D9%85/' --note 'page 366 entry 0 node 10: abadis لایم = Arabic لائم (blamer), no drink sense — negative result for VOP:314' 2>&1 | tail -1"
}
```


### [2026-09-07T19:43:01.238Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/fe8307c44a406962.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/413e4b8b817d236c.txt
```


## [2026-09-07T19:49:22.805Z] TOOL CALL #93: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk366.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_LIMU  = \"https://en.wiktionary.org/wiki/%D9%84%DB%8C%D9%85%D9%88\"\nW_LIMON = \"https://en.wiktionary.org/wiki/limon\"\nW_NIRV  = \"https://en.wiktionary.org/wiki/nirvana\"\nW_NIS   = \"https://en.wiktionary.org/wiki/%E0%A4%A8%E0%A4%BF%E0%A4%B8%E0%A5%8D\"\nE_LEMON = \"https://www.etymonline.com/word/lemon\"\nE_LIME  = \"https://www.etymonline.com/word/lime\"\nA_LEMON = \"https://www.ahdictionary.com/word/search.html?q=lemon\"\nA_LIME  = \"https://www.ahdictionary.com/word/search.html?q=lime\"\nA_NIRV  = \"https://www.ahdictionary.com/word/search.html?q=nirvana\"\nAB_NIRV = \"https://abadis.ir/fatofa/%D9%86%DB%8C%D8%B1%D9%88%D8%A7%D9%86%D8%A7/\"\nAB_LAYM = \"https://abadis.ir/fatofa/%D9%84%D8%A7%DB%8C%D9%85/\"\nVJ_NIRV = \"https://vajehyab.com/?q=%D9%86%DB%8C%D8%B1%D9%88%D8%A7%D9%86%D8%A7&d=moein\"\n\nSKT_QUOTE = (\"SKT_dli_revised.txt l.43966 (archive.org in.ernet.dli.2015.158267, the revised Concise; \"\n             \"page header '295' at l.43988, so the entry stands at the foot of p.294/top of p.295): \"\n             \"'Lime (3), a kind of citron. (F. - Pers.) F. lime. - Pers. limu, (also limun), a lemon, \"\n             \"citron. - Malay limau, a lime, a citron.'  Two entries earlier (l.43219, p.289): \"\n             \"'Lemon. (F. - Pers.) Formerly limon. - F. limon. - Pers. limun, limuna, a lemon, citron. \"\n             \"Of Malay origin.'\")\n\ndata = {\n \"pdf_page\": 366,\n \"book_page\": 336,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-07\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Nîmbǔ, Limǔ\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"Sanskrit निम्बू nimbū- / निम्बूक nimbūka- 'lime, lemon' (itself a loan from an Austroasiatic language) beside Malay limau 'citrus fruit, lime'\",\n   \"note\": (\"Both halves of Nourai's double label are real and are exactly what his two cited references say. \"\n            \"Skeat's revised Concise (s.v. 'Lime (3)') gives 'Pers. līmū (also līmūn) ... - Malay līmau, a lime, a citron', \"\n            \"and Hobson-Jobson p.514 s.v. LEMON quotes Skeat himself: 'The Malay form is limau, \\\"a lime, lemon, or orange\\\" ... \"\n            \"I feel sure that limau ... is an indigenous word which was transferred to Europe', while in the same paragraph noting \"\n            \"'In Hind. we have both līmū and nimbū, which last, at least, seems to be an indigenous form. The Skt. dictionaries give \"\n            \"nimbūka.' Modern scholarship keeps both strands but disagrees on which is ultimate: Wiktionary (s.v. لیمو) derives Persian \"\n            \"līmū from Sanskrit nimbū, itself 'borrowed from an Austroasiatic language', whereas Etymonline (s.v. lemon) prefers \"\n            \"'an Austronesian word of the Malay archipelago, such as Balinese limo \\\"lemon\\\", Malay limaw \\\"citrus fruit, lime\\\"'. \"\n            \"The gloss 'lemon, lime' is right (the two fruits are not distinguished in the Indian forms). \"\n            \"EXTRACTION NOTE for the owner: the printed page also carries, to the right of the Avestan/Old Persian node of entry 1, \"\n            \"a completely blank box (no language label, no refs, no word) joined by a plain line; it is empty in the book itself and \"\n            \"is absent from the JSON, so nothing was verified for it.\"),\n   \"note_fa\": (\"ریشهٔ این خانواده در سنسکریت «نیمبو» (निम्बू / निम्बूक nimbūka-) به معنی لیمو است و در زبان‌های \"\n               \"مالایی صورت limau «میوهٔ مرکبات، لیمو» دیده می‌شود؛ پس برچسب دوگانهٔ «سنسکریت / مالایی» نورایی درست است و \"\n               \"درست همان چیزی است که دو مرجع خودِ او (اسکیت، حبسن‌جبسن ص ۵۱۴) می‌گویند. معین نیز در حاشیهٔ برهان قاطع \"\n               \"ص ۱۹۲۲ می‌نویسد: «اصل این نبات از هند است و نام آن هم هندی است ›نمبو‹، در سانسکریت निम्बूकः». \"\n               \"پژوهش امروزی هر دو رشته را می‌پذیرد ولی در سرچشمهٔ نهایی اختلاف دارد: ویکی‌واژه نیمبوی سنسکریت را وام‌واژه‌ای \"\n               \"از زبان‌های آسیای جنوب‌شرقی (آسترو‑آسیایی) می‌داند و اتیمانلاین سرچشمه را آسترونزیایی (مالایی/بالیایی) می‌شمارد. \"\n               \"ادعای نورایی درست است.\"),\n   \"sources\": [SKT_QUOTE.split(\" \")[0] and W_LIMU, E_LEMON, E_LIME, A_LEMON, A_LIME],\n   \"ref_check\": [\n     {\"ref\": \"SKT:295\", \"status\": \"supports\",\n      \"note\": SKT_QUOTE + \" NB: the repo's refs/SKT.txt (Google scan aconciseetymolo01skeagoog) is an EARLIER impression \"\n              \"with different pagination (Lemon on p.245, and no 'Lime (3)' entry at all), which is why the page number only \"\n              \"matches in the revised text; I copied the revised OCR to refs/SKT_dli_revised.txt for audit.\"},\n     {\"ref\": \"HJB:514\", \"status\": \"supports\",\n      \"note\": \"HJB.txt leaf 563 (running head '514 LEWCHEW, LIU KIU'), s.v. LEMON: 'it has come into European languages through \"\n              \"the Ar. laimūn, and is, according to Hehn, of Indian origin. In Hind. we have both līmū and nimbū, which last, at \"\n              \"least, seems to be an indigenous form. The Skt. dictionaries give nimbūka. ... [Mr. Skeat writes: \\\"The Malay form is \"\n              \"limau, a lime, lemon, or orange ... I feel sure that limau ... is an indigenous word which was transferred to Europe.\\\"]' \"\n              \"— i.e. Nourai's root box (Sanskrit nimbū + Malay limau, gloss 'lemon, lime') is lifted straight from this page.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"BQT\", \"where\": \"p.1922, Mo'in's footnote 2 to لیمو (refs/ocr/BQT/1922.png + 1922.vision.txt)\", \"stance\": \"supports\",\n      \"note\": \"«اصل این نبات از هند است و نام آن هم هندیست ›نمبو‹، در سانسکریت निम्बूकः، ›زابا ص ۳۸۴‹. لیمو = لیمون (ع) = limon (فر) = citrus limonium»\"},\n     {\"src\": \"LKT\", \"where\": \"no. 1322 (p.106) and no. 1320\", \"stance\": \"supports\",\n      \"note\": \"1322 'Pers. līmūn: \\\"Zitrone, Citrus limonum\\\", ebenso ar. laimūn und tk. limon ...; hieraus it. limone, ... frz. limon, \"\n              \"... engl. lemon ... hieraus Limonade'; 1320 'Ar. līm: Einheitsnomen līma \\\"kleine Zitrone von sehr süßem Geschmack\\\"; \"\n              \"hieraus sp. pg. lima, frz. lime' (LKT.txt ll.3072-3077)\"},\n     {\"src\": \"KLN\", \"where\": \"p.878 s.v. lemon and p.890 s.v. lime 'a fruit'\", \"stance\": \"partial\",\n      \"note\": \"Klein knows the same Persian līmūn source but routes lemon through Turkish and lime through Provençal, and says nothing \"\n              \"about Sanskrit or Malay — so he supports the Persian layer, not the Indian/Malay root box.\"},\n     {\"src\": \"MON\", \"where\": \"s.v. لیمو (MON_part2.txt l.41505)\", \"stance\": \"supports\",\n      \"note\": \"«لیمو: [= لیمون (معر.)، هند. نیمبو؛ سنسکریت …] (اِ) (گیا.) نام دو نوع گیاه از گروه مرکبات» — Hindi nimbū and Sanskrit \"\n              \"given as the origin, exactly Nourai's root.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Persian\", \"words\": \"lîmǔ\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"New Persian لیمو līmū is a loanword, not an inherited Iranian word: Sanskrit/Middle Indic nimbū- (Prakrit \"\n        \"*limbū, Hindi both nimbū and līmū) reached Persia with the fruit itself in the early Islamic centuries (Hobson-Jobson: \"\n        \"'brought from India to the Levant by the Arabs 9c. or 10c.'), the initial n- being dissimilated/replaced by l- in the \"\n        \"Indo-Aryan forms Persian actually met (Hindi līmū beside nimbū). Persian has both a shorter līmū and an extended līmūn \"\n        \"(the -ūn form is the one the Arabs took over as laymūn and which Europe knows). Mo'in's footnote in Borhan-e Qate' \"\n        \"p.1922 spells this out: 'the plant comes from India and its name too is Indian, nambū/nimbū; in Sanskrit nimbūka-; \"\n        \"līmū = līmūn (Arabic) = limon (French)'. No Middle Persian form is recorded, which fits a post-Sasanian loan.\"),\n     \"derivation_fa\": (\"«لیمو» واژه‌ای وام‌گرفته است، نه میراث ایرانی: از هندی/سنسکریت نیمبو (nimbū) که در گویش‌های هندی \"\n        \"به صورت līmū نیز آمده و با خودِ میوه در سده‌های نخست اسلامی به ایران رسیده است. تبدیل «ن» آغازی به «ل» در همان \"\n        \"صورت‌های هندی رخ داده و فارسی هر دو صورت لیمو و لیمون را دارد. هیچ صورت فارسی میانه‌ای برای آن ثبت نشده و این \"\n        \"خود نشانهٔ وام‌گیری پس از دورهٔ ساسانی است. معین در حاشیهٔ برهان قاطع (ص ۱۹۲۲) همین را می‌گوید: «اصل این نبات از \"\n        \"هند است ... در سانسکریت निम्बूकः ... لیمو = لیمون (ع) = limon (فر)». ادعای نورایی درست است.\"),\n     \"sources\": [W_LIMU, E_LEMON],\n     \"ref_check\": [\n       {\"ref\": \"BQT:1922\", \"status\": \"supports\",\n        \"note\": \"Rendered and read as refs/ocr/BQT/1922.png (BQT_v3_picofile.pdf pdf page 719; printed page number ۱۹۲۲ visible at the \"\n                \"top of the leaf); headword «لیمو» with Mo'in's footnote 2 quoted in full in refs/ocr/BQT/1922.vision.txt — the footnote \"\n                \"gives exactly Nourai's arrow (Indian/Sanskrit nimbū > Persian līmū > Arabic līmūn > French limon).\"},\n       {\"ref\": \"MON:3671\", \"status\": \"partial\",\n        \"note\": \"Content confirmed: MON_part2.txt l.41505 «لیمو: [= لیمون (معر.)، هند. نیمبو؛ سنسکریت …]». The page number itself is \"\n                \"not checkable: the only scan on disk/online is the 2-vol Adena condensation of Mo'in without the 6-vol pagination \"\n                \"(refs_online.json: MON page numbers cannot be mapped online).\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"HRN\", \"where\": \"grep 'limu', 'Citrone' in HRN.txt\", \"stance\": \"silent\",\n        \"note\": \"Horn's Grundriss has no article on līmū (only no. 153 hādreng 'Citrone'); an Indian loanword of Islamic date falls \"\n                \"outside his etymological corpus.\"},\n       {\"src\": \"HUB\", \"where\": \"grep 'limu', 'Citrone' in HUB.txt\", \"stance\": \"silent\",\n        \"note\": \"Hübschmann's Persische Studien likewise has no līmū (his Citrone material is badrang/vārung).\"},\n       {\"src\": \"PHD\", \"where\": \"grep 'limu', 'lym' in PHD.txt\", \"stance\": \"silent\",\n        \"note\": \"MacKenzie's Concise Pahlavi Dictionary has no līmū — consistent with a post-Sasanian borrowing.\"},\n       {\"src\": \"ARY\", \"where\": \"grep لیمو in ARY_pages.txt\", \"stance\": \"silent\",\n        \"note\": \"Aryanpur's IE-roots dictionary does not treat لیمو (it is not an Indo-European inheritance).\"}\n     ],\n     \"derivation_note\": None\n    },\n    {\n     \"id\": 2, \"lang\": \"Turkish\", \"words\": \"limon\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"Ottoman/Modern Turkish limon 'lemon' is a loan from Persian līmūn, taken over with the fruit; l- is not a \"\n        \"native Turkic initial, so older Anatolian Turkish pronounced it with a prothetic vowel (ilimon), which Vámbéry cites as \"\n        \"the standard proof that the word is a Fremdwort. Wiktionary gives the chain Turkish limon < Ottoman Turkish < Classical \"\n        \"Persian līmū < Sanskrit nimbū. Nourai's arrow Persian > Turkish is therefore right; whether Turkish took it directly \"\n        \"from Persian or through Arabic laymūn cannot be decided on the form alone.\"),\n     \"derivation_fa\": (\"«limon» ترکی وام‌واژه‌ای از فارسی «لیمون» است. «ل» در آغاز واژه در ترکی اصیل نمی‌آید، و همین سبب شده \"\n        \"که در ترکی عثمانی آن را با واکهٔ پیشین (ilimon) تلفظ کنند؛ وامبری همین را دلیل بیگانه‌بودن واژه می‌شمارد. ویکی‌واژه \"\n        \"زنجیرهٔ ترکی limon < ترکی عثمانی < فارسی کلاسیک līmū < سنسکریت nimbū را می‌دهد. پس پیکان نورایی (فارسی › ترکی) \"\n        \"درست است، هرچند نمی‌توان از خودِ صورت واژه دانست که مستقیم از فارسی گرفته شده یا با میانجی «لیمون» عربی.\"),\n     \"sources\": [W_LIMON],\n     \"ref_check\": [\n       {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"TTS\", \"where\": \"Vámbéry 1878, Vorwort §13 (TTS_pages.txt l.527, printed pp. XVI-XVII)\", \"stance\": \"supports\",\n        \"note\": \"'L und [r] sind als Anlaute den eigentlich türkischen Sprachen fremd und kommen als solche mit Ausnahme der \"\n                \"Fremdwörter ... nur einigemal vor ... So: ilimán (Bucht), ilimon (Citrone), statt liman, limon' — Vámbéry has no \"\n                \"dictionary article on limon at all, i.e. he treats it as a loanword.\"},\n       {\"src\": \"LKT\", \"where\": \"no. 1322\", \"stance\": \"supports\",\n        \"note\": \"'Pers. līmūn ... ebenso ar. laimūn und tk. limon \\\"Zitrone\\\" und \\\"Zitronenbaum\\\"' — Lokotsch derives the Turkish \"\n                \"word from the Persian one, as Nourai's arrow does.\"},\n       {\"src\": \"KLN\", \"where\": \"p.878 s.v. lemon\", \"stance\": \"supports\",\n        \"note\": \"'fr. Turk. limon, fr. Pers. līmūn' — Klein has exactly this Persian > Turkish step.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Arabic\", \"words\": \"lîmah\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"Arabic took the Persian word twice over. The collective لِيم līm 'limes' yielded the noun of unity لِيمة \"\n        \"līma(t) 'a single (sweet, thin-skinned) lime', while the extended Persian līmūn gave لَيْمُون laymūn 'lemon'. Both are \"\n        \"recognised Persian loans in Arabic: Asbaghi, Persische Lehnwörter im Arabischen p.243, lists 'laimūn, limūn: \\\"Zitrone\\\" \"\n        \"pers.' and, in the index of European outcomes, 'limah: (Citrus, saure Limette), frz. lime, sp. lima' and even an Arabic \"\n        \"doublet 'nīmū = līmū'. Klein p.890 says the same: 'Arab. līma(t), noun of unity, formed from the collective noun līm, \"\n        \"which derives fr. Pers. līmūn'. Nourai's form lîmah is the pausal spelling of that unity noun.\"),\n     \"derivation_fa\": (\"عربی این واژه را دو بار از فارسی گرفت: «لیم» (اسم جمع) که «لیمة» (اسم وحدت) از آن ساخته شد، و «لیمون» \"\n        \"که از صورت گستردهٔ فارسی لیمون آمد. اصباغی در «وام‌واژه‌های فارسی در عربی» (ص ۲۴۳) هر دو را معرَّبِ فارسی می‌داند و \"\n        \"حتی صورت «نیمو = لیمو» را نیز در عربی ثبت کرده است؛ کلاین (ص ۸۹۰) هم می‌نویسد «līma(t) عربی، اسم وحدت از اسم \"\n        \"جمع līm که از فارسی līmūn است». صورت «لیمه»ٔ نورایی همان اسم وحدت است. ادعای او درست است.\"),\n     \"sources\": [E_LIME, A_LIME],\n     \"ref_check\": [\n       {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"PLA\", \"where\": \"Asbaghi 1988 p.243 (PLA_pages.txt ll.13610, 13627-13635) and p.~? s.v. nīmū (l.14900)\", \"stance\": \"supports\",\n        \"note\": \"'laimūn, limūn: \\\"Zitrone\\\" pers.'; 'limetta: \\\"dünnschalige Zitronenart\\\" pers. -> ar. -> it.'; 'limah: (Citrus, \"\n                \"saure Limette), frz. lime, sp. lima s. limon'; 'nīmū = līmū q.v.'\"},\n       {\"src\": \"KLN\", \"where\": \"p.890 s.v. lime, n., a fruit\", \"stance\": \"supports\",\n        \"note\": \"'F., fr. Provenç. limo, fr. Arab. līma(t) (whence also Sp. lima), noun of unity, formed from the collective noun \"\n                \"līm, which derives fr. Pers. līmūn.'\"},\n       {\"src\": \"AFM\", \"where\": \"grep ليمون / ليمو in AFM_pages.txt and AFM.txt\", \"stance\": \"silent\",\n        \"note\": \"Addi Shir's Kitab al-Alfaz al-Farisiyya al-Mu'arraba returns no hit for the word (0 matches on either Arabic \"\n                \"spelling), so he does not list līm/laymūn among his Arabicised Persian words.\"},\n       {\"src\": \"LKT\", \"where\": \"no. 1320\", \"stance\": \"supports\",\n        \"note\": \"'Ar. līm: Einheitsnomen līma \\\"kleine Zitrone von sehr süßem Geschmack\\\"; hieraus sp. pg. lima, frz. lime' — the \"\n                \"unity-noun analysis and the Romance outcome.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"French\", \"words\": \"limon, limonâd\", \"verdict\": \"disputed\",\n     \"derivation\": (\"The French words themselves are secure — Old French limon 'citrus fruit' is attested from the 12th c. and \"\n        \"limonade (a lemon-and-sugar drink) from the 17th c., limonade being limon + the Romance suffix -ade. What is disputed is \"\n        \"Nourai's PARENT: he makes French limon a borrowing from Turkish limon (this is Klein p.878's account, and Klein is the \"\n        \"reference he cites two nodes down). Modern authorities route it through Arabic and Italy instead: Etymonline, 'from Old \"\n        \"French limon \\\"citrus fruit\\\" (12c.), via Provençal or Italian from Arabic laimun, Persian limun'; AHD, 'Middle English \"\n        \"limon, from Old French, from Old Italian limone, from Arabic laymūn, ultimately from an alteration ... of Persian līmū'; \"\n        \"Wiktionary s.v. limon (French), 'Borrowed from Italian limone'; Asbaghi p.243 likewise routes limūnād 'pers. -> ar. -> \"\n        \"frz.' A Turkish intermediary is chronologically awkward: the word is in French two to three centuries before Ottoman \"\n        \"contact with France mattered, and it is the Crusades and Moorish Spain/Sicily that Hobson-Jobson p.514 names as the \"\n        \"route ('perhaps both from the Crusades and from the Moors of Spain'). So: word real, parent wrong.\"),\n     \"derivation_fa\": (\"خودِ واژه‌های فرانسوی درست‌اند: limon «میوهٔ مرکبات» از سدهٔ دوازدهم میلادی در فرانسویِ کهن گواه دارد و \"\n        \"limonade (لیموناد) در سدهٔ هفدهم از limon + پسوند ‑ade ساخته شده است. آنچه پژوهش امروزی رد می‌کند، «پدرِ» این گره در \"\n        \"نمودار نورایی است: او فرانسوی را از ترکی گرفته (این نظر کلاین ص ۸۷۸ است)، اما اتیمانلاین، فرهنگ American Heritage و \"\n        \"ویکی‌واژه همگی راه را از عربی «لیمون» و سپس ایتالیایی limone / پروانسی limon می‌دانند، و اصباغی نیز limūnād را \"\n        \"«فارسی › عربی › فرانسوی» می‌گیرد. میانجیِ ترکی از نظر تاریخی هم ناسازگار است، زیرا واژه دو‑سه سده پیش از \"\n        \"اهمیت‌یافتن پیوند عثمانی–فرانسه در فرانسوی به کار می‌رفته و حبسن‌جبسن (ص ۵۱۴) راهِ ورود را جنگ‌های صلیبی و مورهای \"\n        \"اسپانیا می‌شمارد. پس واژه درست است ولی پیکانِ ترکی › فرانسوی نادرست است.\"),\n     \"sources\": [E_LEMON, A_LEMON, W_LIMON],\n     \"ref_check\": [\n       {\"ref\": \"VOP:319\", \"status\": \"not_checked\",\n        \"note\": \"Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi (1371/1992) is not digitised anywhere — refs_online.json VOP: \"\n                \"'RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook. Purchase second-hand only.'\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"p.878 s.v. lemon\", \"stance\": \"supports\",\n        \"note\": \"'lemon, n. — ME. lymon, fr. MF. (= F.) limon, fr. Turk. limon, fr. Pers. līmūn, \\\"limon, citron\\\"' — Klein is the \"\n                \"one authority that agrees with Nourai's Turkish step.\"},\n       {\"src\": \"PHN\", \"where\": \"Pihan 1866 p.239 s.v. LIMON (fruit) (PHN.txt leaf 270)\", \"stance\": \"partial\",\n        \"note\": \"'LIMON (fruit), s. m. (a.-p.-t.) [līm] en arabe, [līmūn] en persan, et [līmūn] en turc, limon, fruit du limonier \"\n                \"... employé dans la composition d'une boisson très rafraîchissante, appelée limonade' — Pihan lists Arabic, Persian \"\n                \"AND Turkish side by side without choosing between them, and confirms limonade as the French derivative.\"},\n       {\"src\": \"DEV\", \"where\": \"Devic 1876 p.152 s.v. Limon (DEV.txt leaf 185)\", \"stance\": \"contradicts\",\n        \"note\": \"'LIMON. Fruit. Esp. limon, portug. limão, ital. limone. De l'arabe-persan laimoûn, même sens.' — Devic derives the \"\n                \"French from Arabic/Persian directly, with Italian and Spanish as parallels, and never mentions Turkish.\"},\n       {\"src\": \"PLA\", \"where\": \"Asbaghi p.243\", \"stance\": \"contradicts\",\n        \"note\": \"'limūnād: \\\"Limonade; Erfrischungsgetränk aus Fruchtsaft, Zucker u. Wasser\\\" ... pers. -> ar. -> frz.' — Persian to \"\n                \"Arabic to French, no Turkish link.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Persian\", \"words\": \"lîmonâd\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"Persian لیموناد līmonād is a 19th/20th-century re-borrowing from French limonade — a round trip, since the \"\n        \"French word rests ultimately on Persian līmūn itself. Mo'in records it with the French tag and even notes the semantic \"\n        \"drift that came with the naturalisation: s.v. لی‌موناد, 'in common Persian usage it means a carbonated drink made with \"\n        \"baking soda and a little sour ingredient, whereas in French it means a lemon-juice sherbet' (MON_part2.txt l.41560 ff.). \"\n        \"Phonetically the French nasal -on- is rendered by Persian -on- and the final -ade by -âd, the normal treatment of French \"\n        \"loans of the Qajar/Pahlavi period (cf. مارمالاد, پماد).\"),\n     \"derivation_fa\": (\"«لیموناد» وام‌واژه‌ای است از فرانسوی limonade که در سدهٔ سیزدهم/چهاردهم هجری به فارسی آمده؛ یعنی سفری \"\n        \"دوسویه، زیرا خودِ واژهٔ فرانسوی بر «لیمون» فارسی استوار است. معین آن را با نشان [فر.] آورده و حتی تحول معنایی آن را \"\n        \"یادآور شده است: «در تداول عامه و در زبان فارسی به معنی شربت گازداری است که با جوش شیرین و کمی مادهٔ ترش‌مزه درست \"\n        \"کنند ولی در زبان فرانسوی به معنی شربت آب لیمو است». از نظر آوایی ‑ade فرانسوی به ‑اد بدل شده، همان‌گونه که در \"\n        \"مارمالاد و پماد. ادعای نورایی درست است.\"),\n     \"sources\": [W_LIMU],\n     \"ref_check\": [\n       {\"ref\": \"VOP:319\", \"status\": \"not_checked\",\n        \"note\": \"VOP (Moshiri 1992) has no scan anywhere; see refs_online.json VOP.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"MON\", \"where\": \"s.v. لی‌موناد (MON_part2.txt ll.41556-41565)\", \"stance\": \"supports\",\n        \"note\": \"«لی‌موناد: [فر. limonade] ... در تداول عامه و در زبان فارسی به معنی شربت گازداری است ... ولی در زبان فرانسوی به معنی \"\n                \"شربت آب لیمو است» — the French origin and the Persian sense-shift.\"},\n       {\"src\": \"BQT\", \"where\": \"p.1922, Mo'in's footnote to لیمو\", \"stance\": \"partial\",\n        \"note\": \"The footnote equates «لیمو = لیمون (ع) = limon (فر)», establishing the French member of the family that لیموناد is \"\n                \"built on, but does not treat لیموناد itself.\"},\n       {\"src\": \"PHN\", \"where\": \"Pihan p.239\", \"stance\": \"supports\",\n        \"note\": \"'... une boisson très rafraîchissante, appelée limonade' — the French word and drink Persian borrowed.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"English\", \"words\": \"lemon, lemonade\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"English lemon is first recorded c.1400 as lymon, straight from Old/Middle French limon 'citrus fruit'; \"\n        \"lemonade (1660s) is French limonade taken over wholesale. Klein p.878 — the page Nourai cites — has 'lemon, n. — ME. \"\n        \"lymon, fr. MF. (= F.) limon' and 'lemonade, n. — F. limonade, fr. limon, \\\"lemon\\\"'; AHD gives 'Middle English limon, \"\n        \"from Old French'. The French > English step is uncontroversial; the only reservation belongs to node #4 (Klein and \"\n        \"Nourai put Turkish behind the French form, while OED/AHD/Etymonline put Arabic laymūn and Italian limone there). \"\n        \"The Middle English -y- of lymon simply spells the French [i], and the modern spelling with e- follows the reduced \"\n        \"unstressed vowel.\"),\n     \"derivation_fa\": (\"انگلیسی lemon نخست‌بار حدود ۱۴۰۰ م. به صورت lymon گواه دارد و یکسر از limon فرانسوی گرفته شده است؛ \"\n        \"lemonade نیز (سدهٔ هفدهم) همان limonade فرانسوی است. کلاین در همان ص ۸۷۸ که نورایی یاد می‌کند می‌نویسد «lemon — ME. \"\n        \"lymon, fr. MF. (= F.) limon» و «lemonade — F. limonade». این حلقهٔ فرانسوی › انگلیسی هیچ اختلافی ندارد؛ تنها ایراد به \"\n        \"گرهٔ پیشین (#۴) بازمی‌گردد که در آن ترکی میانجی گرفته شده است. «y» در املای میانه همان [i] فرانسوی را می‌نمایاند و \"\n        \"«e» امروزی بازتاب کاهش واکهٔ بی‌تکیه است. ادعای نورایی درست است.\"),\n     \"sources\": [E_LEMON, A_LEMON],\n     \"ref_check\": [\n       {\"ref\": \"KLN:878\", \"status\": \"supports\",\n        \"note\": \"KLN_1966.txt l.21452-21454, under the page marker '878' (l.21444): 'lemon, n. — ME. lymon, fr. MF. (= F.) limon, \"\n                \"fr. Turk. limon, fr. Pers. līmūn, \\\"limon, citron\\\". Cp. lime, \\\"a fruit\\\", limonene.' / 'lemonade, n. — F. limonade, \"\n                \"fr. limon, \\\"lemon\\\". See prec. word and -ade.' Exactly Nourai's two English words on exactly the cited page.\"},\n       {\"ref\": \"AHD:748\", \"status\": \"not_checked\",\n        \"note\": \"AHD:748 is a page of the 1975 New College Edition main dictionary, which is not on disk (only the Watkins IE-roots \"\n                \"appendix is). The content was checked in the current online AHD instead: 'Middle English limon, from Old French, \"\n                \"from Old Italian limone, from Arabic laymūn, ultimately from ... Persian līmū' — which supports the English entry \"\n                \"but not the Turkish link. 748/1505 also fits 'lemon' alphabetically in that edition.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"SKT\", \"where\": \"revised Concise p.289 s.v. Lemon (SKT_dli_revised.txt l.43219)\", \"stance\": \"supports\",\n        \"note\": \"'Lemon. (F. - Pers.) Formerly limon. - F. limon. - Pers. līmūn, līmūnā, a lemon, citron. Of Malay origin.'\"},\n       {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls s.v. lemon (FSD_vol2.txt l.74579-74580)\", \"stance\": \"partial\",\n        \"note\": \"'lemon, n. ... [< F. limon, < LL. limon(-), < Per. līmūn, lemon.]' — French from a Latinised limon from Persian; no \"\n                \"Turkish step.\"},\n       {\"src\": \"LKT\", \"where\": \"no. 1322\", \"stance\": \"supports\",\n        \"note\": \"'... engl. lemon, ndl. lemoen, lamoen, dtsch. Limone (selten), hieraus Limonade \\\"süßes Getränk\\\"'.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"Spanish\", \"words\": \"lima\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"Spanish (and Portuguese) lima 'lime' is a direct Andalusi-Arabic borrowing of līma(t), the unity noun of \"\n        \"līm, learned in al-Andalus where the Arabs had planted the fruit; the Arabic feminine ending -a(t) coincided with the \"\n        \"Spanish feminine -a, so the word needed no adaptation. Klein p.890 notes 'Arab. līma(t) ... (whence also Sp. lima)', \"\n        \"AHD s.v. lime gives 'from Spanish lima, from Arabic līma', and Lokotsch no. 1320 'Ar. līm ... hieraus sp. pg. lima'. \"\n        \"Hobson-Jobson p.516 s.v. LIME adds the trade history: 'The word no doubt comes from the Sp. and Port. lima, which is \"\n        \"from the Ar. līma ... But probably it came into English from the Portuguese in India.'\"),\n     \"derivation_fa\": (\"«lima»ی اسپانیایی (و پرتغالی) وام‌واژه‌ای است یکسر از «لیمة» عربی اندلس، آنجا که عرب‌ها این میوه را \"\n        \"کاشته بودند؛ پایانهٔ مؤنثِ ‑ة عربی با ‑a مؤنثِ اسپانیایی هم‌سان بود و واژه به هیچ سازگاری نیاز نداشت. کلاین (ص ۸۹۰) \"\n        \"«līma(t) عربی ... (که lima اسپانیایی نیز از آن است)»، فرهنگ American Heritage «از اسپانیایی lima، از عربی līma» و \"\n        \"لوکوچ (شمارهٔ ۱۳۲۰) «Ar. līm ... hieraus sp. pg. lima» را می‌آورند. ادعای نورایی درست است.\"),\n     \"sources\": [A_LIME, E_LIME],\n     \"ref_check\": [\n       {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"p.890 s.v. lime, n., a fruit\", \"stance\": \"supports\",\n        \"note\": \"'fr. Arab. līma(t) (whence also Sp. lima), noun of unity, formed from the collective noun līm, which derives fr. \"\n                \"Pers. līmūn.'\"},\n       {\"src\": \"LKT\", \"where\": \"no. 1320 (LKT.txt l.3072)\", \"stance\": \"supports\",\n        \"note\": \"'Ar. līm: Einheitsnomen līma \\\"kleine Zitrone von sehr süßem Geschmack\\\"; hieraus sp. pg. lima, frz. lime, lime \"\n                \"bergamote.'\"},\n       {\"src\": \"HJB\", \"where\": \"p.516 s.v. LIME (HJB.txt l.13234)\", \"stance\": \"supports\",\n        \"note\": \"'The word no doubt comes from the Sp. and Port. lima, which is from the Ar. līma; Fr. lime, Pers. līmū, līmūn.'\"},\n       {\"src\": \"DEV\", \"where\": \"Devic p.152\", \"stance\": \"supports\",\n        \"note\": \"'Plusieurs espèces de citronniers portent aussi le nom de lime, esp. et portug. lima; en arabe līma.'\"}\n     ]\n    },\n    {\n     \"id\": 8, \"lang\": \"French\", \"words\": \"\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"A pass-through node: the word Nourai leaves blank is French lime f. 'lime (fruit)', borrowed from Spanish \"\n        \"lima in the 16th-17th c. as the fruit reached France through Iberian trade. AHD s.v. lime states the chain flatly — \"\n        \"'French, from Spanish lima, from Arabic līma, from Persian līmū' — which is Nourai's arrow exactly; Etymonline agrees \"\n        \"('probably via Spanish lima or Portuguese limão'). The one dissenting voice is Klein p.890, who makes French lime a \"\n        \"borrowing from Provençal limo rather than from Castilian, with Spanish lima a parallel outcome of the same Arabic word; \"\n        \"either way the immediate donor is Ibero-Romance/Occitan and the ultimate one Arabic līma(t).\"),\n     \"derivation_fa\": (\"این گره واژه‌ای ندارد و تنها حلقهٔ میانی است: مقصود «lime» فرانسوی است که در سده‌های شانزدهم–هفدهم از \"\n        \"«lima» اسپانیایی وام گرفته شد، همراه با رسیدن خودِ میوه به فرانسه از راه بازرگانی ایبری. فرهنگ American Heritage \"\n        \"همین زنجیره را می‌دهد: «فرانسوی، از اسپانیایی lima، از عربی līma، از فارسی līmū». تنها کلاین (ص ۸۹۰) واسطه را \"\n        \"پروانسی limo می‌داند نه اسپانیایی. در هر دو صورت دهندهٔ نزدیک، رومانسِ ایبری/اوکسیتان و سرچشمهٔ دور، «لیمة» عربی \"\n        \"است. ادعای نورایی پذیرفتنی است.\"),\n     \"sources\": [A_LIME, E_LIME],\n     \"ref_check\": [\n       {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this empty pass-through node.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"p.890 s.v. lime, n., a fruit\", \"stance\": \"partial\",\n        \"note\": \"'lime, n., a fruit allied to lemon. — F., fr. Provenç. limo, fr. Arab. līma(t) (whence also Sp. lima)' — French, but \"\n                \"via Provençal rather than Spanish.\"},\n       {\"src\": \"LKT\", \"where\": \"no. 1320\", \"stance\": \"supports\",\n        \"note\": \"'hieraus sp. pg. lima, frz. lime' — Lokotsch lists French lime with the Iberian forms as outcomes of Arabic līma.\"},\n       {\"src\": \"DEV\", \"where\": \"Devic p.152 s.v. Limon (end)\", \"stance\": \"supports\",\n        \"note\": \"'Plusieurs espèces de citronniers portent aussi le nom de lime, esp. et portug. lima; en arabe līma. (Voy. Dozy, \"\n                \"Gloss. p. 267.)'\"}\n     ]\n    },\n    {\n     \"id\": 9, \"lang\": \"English\", \"words\": \"lime\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"English lime 'a citrus fruit' appears in the 1630s, i.e. with the Caribbean and East-Indian trade, from \"\n        \"French lime (Nourai's node #8) reinforced by Spanish lima and Portuguese lima/limão — Hobson-Jobson p.516 says 'probably \"\n        \"it came into English from the Portuguese in India. It is not in Minsheu (2nd ed.)'. Klein p.890, the page Nourai cites, \"\n        \"gives 'lime, n., a fruit allied to lemon. — F., fr. Provenç. limo, fr. Arab. līma(t) ... which derives fr. Pers. līmūn'. \"\n        \"The gloss 'a citrus fruit' is correct and the word is kept apart from the two homonyms lime 'birdlime/calx' (OE līm) and \"\n        \"lime 'linden' (< lind), which are unrelated.\"),\n     \"derivation_fa\": (\"«lime» انگلیسی به معنی نوعی مرکبات از دههٔ ۱۶۳۰ م. گواه دارد، یعنی همزمان با بازرگانی کارائیب و هند \"\n        \"شرقی، و از «lime» فرانسوی (همان گرهٔ ۸) گرفته شده و صورت‌های اسپانیایی lima و پرتغالی lima/limão آن را تقویت کرده‌اند؛ \"\n        \"حبسن‌جبسن (ص ۵۱۶) می‌نویسد «احتمالاً از پرتغالی‌ها در هند به انگلیسی رسیده است». کلاین در همان ص ۸۹۰ که نورایی \"\n        \"یاد کرده می‌گوید «lime ... — F., fr. Provenç. limo, fr. Arab. līma(t) ... که از فارسی līmūn است». این واژه را نباید با \"\n        \"دو هم‌آوای بی‌ربطش (lime «آهک/سریشِ پرنده‌گیری» از انگلیسی کهن līm و lime «درخت زیزفون» از lind) اشتباه گرفت. \"\n        \"ادعای نورایی درست است.\"),\n     \"sources\": [E_LIME, A_LIME],\n     \"ref_check\": [\n       {\"ref\": \"KLN:890\", \"status\": \"supports\",\n        \"note\": \"KLN_1966.txt l.21760, between the page markers '890' (l.21753) and '891' (l.21764): 'lime, n., a fruit allied to \"\n                \"lemon. — F., fr. Provenç. limo, fr. Arab. līma(t) (whence also Sp. lima), noun of unity, formed from the collective \"\n                \"noun līm, which derives fr. Pers. līmūn. See lemon and cp. limonene.' Exactly the word and gloss on exactly the \"\n                \"cited page.\"},\n       {\"ref\": \"AHD:758\", \"status\": \"not_checked\",\n        \"note\": \"The 1975 New College Edition main dictionary is not on disk; the current online AHD entry was read instead and says \"\n                \"'French, from Spanish lima, from Arabic līma, from Persian līmū', i.e. it supports Nourai's whole Arabic > Spanish > \"\n                \"French > English chain. p.758 is ten pages after the 'lemon' page 748, which fits alphabetically.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"SKT\", \"where\": \"revised Concise p.294/295 s.v. Lime (3) (SKT_dli_revised.txt l.43966)\", \"stance\": \"supports\",\n        \"note\": \"'Lime (3), a kind of citron. (F. - Pers.) F. lime. - Pers. līmū, (also līmūn), a lemon, citron. - Malay līmau, a \"\n                \"lime, a citron.'\"},\n       {\"src\": \"HJB\", \"where\": \"p.516 s.v. LIME (HJB.txt ll.13233-13234)\", \"stance\": \"supports\",\n        \"note\": \"'The fruit of the small Citrus medica, var. acida ... The word no doubt comes from the Sp. and Port. lima, which is \"\n                \"from the Ar. līma; Fr. lime, Pers. līmū, līmūn (see LEMON). But probably it came into English from the Portuguese \"\n                \"in India.'\"},\n       {\"src\": \"FSD\", \"where\": \"grep 'Sp. lima', 'Ar. limah' in FSD_vol2/vol3\", \"stance\": \"silent\",\n        \"note\": \"The lime-fruit article did not come out of the Funk & Wagnalls OCR (the volume break falls in L); no result either way.\"}\n     ]\n    },\n    {\n     \"id\": 10, \"lang\": \"Persian\", \"words\": \"lâym\", \"verdict\": \"unverified\",\n     \"derivation\": (\"Nourai's last link is a modern colloquialism: Persian لایم lâym, i.e. English 'lime' transcribed with \"\n        \"Persian ای for the English diphthong /aɪ/, used in Iran of lime-flavoured soft drinks and cordials — hence his gloss \"\n        \"'a drink' rather than 'a fruit'. Formally the borrowing is transparent (a 20th-c. English loan, not the older Persian \"\n        \"لیمو), and it completes a full circle Persian līmū > Arabic > Spanish > French > English > Persian. But I could find no \"\n        \"independent attestation: Nourai's own reference (VOP:319/314, Moshiri's dictionary of European words in Persian) has no \"\n        \"scan anywhere; Mo'in's lexicon has لیمو/لیموناد but no لایم (MON_part2.txt, 0 hits); abadis.ir s.v. لایم returns only the \"\n        \"Arabic لائم 'reprover, blamer' (plural لائمین/لوائم), not a drink; and Borhan-e Qate' predates the word. Marked \"\n        \"unverified rather than plausible because no source either way could be produced.\"),\n     \"derivation_fa\": (\"آخرین حلقهٔ نمودار یک وام‌واژهٔ گفتاری نو است: «لایم» یعنی همان lime انگلیسی که «ای» فارسی، دوواکهٔ \"\n        \"/aɪ/ انگلیسی را می‌نمایاند و در ایران برای نوشابه و شربتِ طعم‌لیمو به کار می‌رود؛ از همین رو نورایی آن را «نوعی \"\n        \"نوشیدنی» معنی کرده است. صورت واژه شفاف است (وام‌گیری سدهٔ چهاردهم/بیستم از انگلیسی، نه همان «لیمو»ی کهن) و \"\n        \"دایره را کامل می‌کند: لیموی فارسی › عربی › اسپانیایی › فرانسوی › انگلیسی › فارسی. اما هیچ گواه مستقلی نیافتم: \"\n        \"مرجع خودِ نورایی (مشیری، فرهنگ واژه‌های اروپایی در فارسی) هیچ نسخهٔ دیجیتالی ندارد؛ در فرهنگ معین «لیمو» و \"\n        \"«لیموناد» هست ولی «لایم» نیست؛ و آبادیس زیر «لایم» تنها «لائم» عربی (سرزنش‌کننده) را می‌آورد. پس داوری: \"\n        \"بی‌گواه (نه رد، نه تأیید).\"),\n     \"sources\": [AB_LAYM],\n     \"ref_check\": [\n       {\"ref\": \"VOP:314\", \"status\": \"not_checked\",\n        \"note\": \"Moshiri's Farhang-e Vazheha-ye Orupayi dar Farsi is not digitised (refs_online.json VOP: 'no catalogue record with \"\n                \"a scan, no ebook'), so p.314 could not be opened.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"MON\", \"where\": \"grep لایم in MON_part1.txt / MON_part2.txt\", \"stance\": \"silent\",\n        \"note\": \"Mo'in's lexicon has لیمو, لیموترش, لیمو شیرین, لیمون, لی‌موناد, لیمه (l.41499-41566) but no لایم in the 'lime drink' sense.\"},\n       {\"src\": \"BQT\", \"where\": \"p.1922 (the لیمو page) and grep لایم in BQT_v1/v2/v3 page files\", \"stance\": \"silent\",\n        \"note\": \"Borhan-e Qate' (1062/1652) is three centuries older than any English loan of this kind; the لیمو page carries \"\n                \"لیمو، لیمو دارو، لیمونیون only.\"},\n       {\"src\": \"ARY\", \"where\": \"grep لایم in ARY_pages.txt\", \"stance\": \"silent\",\n        \"note\": \"Aryanpur's IE-roots dictionary does not list it.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"Nis\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"Proto-Indo-Iranian *niš 'out, forth, away' — an s-extension of PIE *ni- 'down' (Pokorny 312 ni-, nei-)\",\n   \"note\": (\"The element is real and Nourai's two authorities do reconstruct it at PIE level: Kent, Old Persian p.193, 'nij- verbal \"\n            \"prefix \\\"away\\\": sandhi form of pIE *nis- before voiced stops, generalized, cf. Av. niš-, Skt. niṣ-', and Klein p.1049 \"\n            \"s.v. nirvana, 'nis-, nir-, \\\"out, forth, away\\\" (which is rel. to Avestic nish-, of s.m., and prob. cogn. with OSlav. \"\n            \"nisti, \\\"poor\\\")'. What earns a 'plausible' rather than 'confirmed' is (a) the missing gloss — the root box carries no \"\n            \"meaning at all, where 'out, forth, away' was needed — and (b) the fact that *nis is securely reconstructible only for \"\n            \"Indo-Iranian plus Slavic niz-: Pokorny p.312 and Mann col. ~900 file the material under *ni-, *nei- 'nieder' (down), \"\n            \"with the -s an ablative-type extension and the sense 'out' an Indo-Iranian development from 'down(wards)'. Nourai's \"\n            \"label 'Indo-European' is thus defensible but broader than the evidence.\"),\n   \"note_fa\": (\"این عنصر واقعی است و هر دو مرجعِ خودِ نورایی آن را در سطح هندواروپایی بازسازی می‌کنند: کنت (پارسی باستان، ص ۱۹۳) \"\n               \"«nij- پیشوند فعلی ›دور، بیرون‹: صورت سندهیِ *nis- هندواروپایی پیش از انسدادی‌های واک‌دار، قس. اوستایی niš-، \"\n               \"سنسکریت niṣ-» و کلاین (ص ۱۰۴۹) «nis-، nir- ›بیرون، دور‹ که با nish- اوستایی خویشاوند است». دو نکته اما \"\n               \"داوری را به «با احتیاط پذیرفتنی» می‌کشاند: نخست آنکه خانهٔ ریشه هیچ معنایی ندارد و می‌بایست «بیرون، دور» \"\n               \"نوشته می‌شد؛ دوم آنکه *nis تنها برای هندوایرانی و اسلاوی (niz-) استوار است، و پوکورنی (ص ۳۱۲) و مان این \"\n               \"مواد را زیر ریشهٔ *ni-, *nei- «پایین، فرود» می‌آورند و ‑s را پسوندی می‌شمارند؛ معنای «بیرون» تحولی \"\n               \"هندوایرانی از «فرود» است. پس برچسب «هندواروپایی» پذیرفتنی ولی فراخ‌تر از گواه‌هاست.\"),\n   \"sources\": [W_NIS, W_NIRV, A_NIRV],\n   \"ref_check\": [\n     {\"ref\": \"KLN:1049\", \"status\": \"supports\",\n      \"note\": \"KLN_1966.txt l.25465, just after the page marker for 1049 (l.25457, OCR'd as 'I U4V', between the clean markers 1046 \"\n              \"and 1054): 'nirvana, n. ... — OI. nirvanah, lit. \\\"a blowing out (of a light), extinction, disappearance\\\", which is \"\n              \"formed fr. nis-, nir-, \\\"out, forth, away\\\" (which is rel. to Avestic nish-, of s.m., and prob. cogn. with OSlav. \"\n              \"nisti, \\\"poor\\\"), and vati, \\\"it blows\\\", for whose etymology see wind, n.' Klein is the source of Nourai's whole \"\n              \"entry, root and both nodes.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"POK\", \"where\": \"Pokorny IEW p.312 (POK_01.txt l.4594, leaf 324 = p.312)\", \"stance\": \"partial\",\n      \"note\": \"'ni-, nei- \\\"nieder\\\", Komparativ nitero- ... ai. ní, av. nī \\\"nieder(wärts)\\\" ... abg. nizъ \\\"hinab, hinunter\\\"' — \"\n              \"Pokorny has the root but glosses it 'down', and gives no separate *nis- lemma; Skt. niṣ / Av. niš belong here as the \"\n              \"-s extension.\"},\n     {\"src\": \"IEC\", \"where\": \"Mann, IEC.txt l.11581 (leaf 465, col. ~900)\", \"stance\": \"partial\",\n      \"note\": \"'nei- \\\"down\\\" Cf. ni-, neiu- Gk. neí-atos \\\"lowest\\\" ... formant in OCS niže ... z-gde in Skt. Av. ni- \\\"down\\\"; Oss. \"\n              \"ní, ni, id.' — again *ni-/*nei- 'down', no *nis-.\"},\n     {\"src\": \"AHD\", \"where\": \"Watkins 1985 (AHD_watkins1985.txt ll.1125, 1923)\", \"stance\": \"silent\",\n      \"note\": \"The Watkins appendix has no entry for *ni-/*nis- at all; it treats nirvana only under 'wē-. To blow ... 4. Basic form \"\n              \"*wē- in Sanskrit vāti (stem *vā-), he blows: NIRVANA. [Pok. 10. aw(ē)- 81.]' and indexes it 'NIRVANA wē-'.\"},\n     {\"src\": \"WLD\", \"where\": \"grep 'ni-, nei-', 'nitero' in WLD_Bd1/Bd2/band3\", \"stance\": \"silent\",\n      \"note\": \"No hit for the lemma in the available Walde-Pokorny OCR (Bd. II covers this stretch but the entry did not survive the \"\n              \"DLI OCR); WP I 125 ff./II 335 f. is the reference Pokorny himself gives for it.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan / Old Persian\", \"words\": \"niš, nij : away, off, out ; niš-bar : to carry out\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Both forms and both glosses are right, and even the compound is attested. Bartholomae, Altiranisches \"\n        \"Wörterbuch col. 1087: 'j., g. niš°, niž°, p. niš° 1) Adv. \\\"hinaus\\\" (nur Ableit.). 2) Praev. \\\"hinaus, weg\\\" (mit ay-, \"\n        \"°dar-, °bar-, nāi°)' — i.e. Avestan niš is an adverb/preverb 'out, away' that compounds with bar- exactly as Nourai says. \"\n        \"The niš-/niž- pair is purely positional (niš before voiceless sounds, niž before voiced), and Old Persian generalised the \"\n        \"voiced sandhi form: Kent p.193, 'nij- verbal prefix \\\"away\\\": sandhi form of pIE *nis- before voiced stops, generalized, \"\n        \"cf. Av. niš-, Skt. niṣ-; with verb ay- \\\"go\\\"' (OP nijāyam 'I went out'). For niš-bar- see AiW col. 939 s.v. bar- 'mit uz \"\n        \"und niš \\\"etwas heraustragen, -holen aus —\\\": ... niš.barayən, \\\"one should carry the corpse out of the water\\\", Vd. 6.31' \"\n        \"— and bar- is indeed PIE *bher- 'to carry', so the cross-reference to Bher is right.\"),\n     \"derivation_fa\": (\"هر دو صورت و هر دو معنا درست‌اند و حتی ترکیب یادشده گواه دارد. بارتولومه در «فرهنگ ایرانی باستان» \"\n        \"(ستون ۱۰۸۷) می‌نویسد: «niš/niž اوستایی و niš پارسی باستان: ۱) قید ›بیرون‹، ۲) پیشوند فعلی ›بیرون، دور‹ (با \"\n        \"ay-، dar-، bar-)». دوگانگی niš/niž تنها آوایی است (niš پیش از واک‌های بی‌واک و niž پیش از واک‌دارها) و پارسی \"\n        \"باستان همان صورت واک‌دار را تعمیم داده است؛ کنت (ص ۱۹۳): «nij- پیشوند فعلی ›دور‹: صورت سندهیِ *nis- \"\n        \"هندواروپایی پیش از انسدادی‌های واک‌دار که تعمیم یافته، قس. اوستایی niš-، سنسکریت niṣ-؛ با فعل ay- ›رفتن‹». \"\n        \"برای niš-bar- نگاه کنید به همان فرهنگ، ستون ۹۳۹ زیر bar-: «با uz و niš ›چیزی را بیرون بردن/بیرون آوردن از‹ ... \"\n        \"niš.barayən ›مرده را از آب بیرون آورند‹ وندیداد ۶.۳۱». و bar- همان ریشهٔ *bher- «بردن» است، پس ارجاع نورایی \"\n        \"به Bher نیز درست است. ادعای او درست است.\"),\n     \"sources\": [W_NIS],\n     \"ref_check\": [\n       {\"ref\": \"KNT:193\", \"status\": \"supports\",\n        \"note\": \"KNT.txt leaf 217 (the running head '194 OLD PERSIAN' falls further down the leaf, so this entry is on p.193): \"\n                \"'nij- verbal prefix \\\"away\\\": sandhi form of pIE *nis- before voiced stops, generalized, cf. Av. niš-, Skt. niṣ- \"\n                \"(§120); with verb ay- \\\"go\\\".' Nourai's page is exact.\"},\n       {\"ref\": \"KLN:1049\", \"status\": \"supports\",\n        \"note\": \"KLN_1966.txt l.25465 (p.1049): 'nis-, nir-, \\\"out, forth, away\\\" (which is rel. to Avestic nish-, of s.m.)' — the \"\n                \"Avestan form and the gloss Nourai gives.\"},\n       {\"ref\": \"DZA:57\", \"status\": \"not_checked\",\n        \"note\": \"Rashed Mohassel, Daramadi bar Dastur-e Zaban-e Avestai (Khajeh 1364/1985) is not digitised — refs_online.json DZA: \"\n                \"'RE-SEARCH 2026-09: the 1364 Khajeh edition is not digitised; a revised edition is sold as an ebook on Taaghche.'\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch col. 1087 s.v. niš° and col. 939 s.v. bar- (BRT.txt ll.19251, 16846)\", \"stance\": \"supports\",\n        \"note\": \"col. 1087: 'j., g. niš°, niž°, p. niš° 1) Adv. \\\"hinaus\\\" (nur Ableit.). 2) Praev. \\\"hinaus, weg\\\" (mit ay-, dar-, \"\n                \"bar-, nāi-)'; col. 939 s.v. bar-: 'mit uz und niš \\\"etwas heraustragen, -holen aus —\\\" (haca mit Abl.) ... \"\n                \"niš.barayən ... \\\"man soll so viel (als möglich) von dem Leichnam aus dem Wasser herausholen\\\" V. 6.31.'\"},\n       {\"src\": \"KNT\", \"where\": \"Kent p.193 s.v. nij- and p.193 s.v. ni-\", \"stance\": \"supports\",\n        \"note\": \"Besides nij-, the same page has 'ni- prep. and verbal prefix \\\"down\\\": Av. ni, Skt. ni-, pIE *ni', which shows the \"\n                \"*ni- / *ni-s relationship inside Kent's own lexicon.\"},\n       {\"src\": \"POK\", \"where\": \"IEW p.312\", \"stance\": \"partial\",\n        \"note\": \"'ai. ní, av. nī \\\"nieder(wärts)\\\" ... abg. nizъ' — the base root, glossed 'down' not 'out'.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Sanskrit\", \"words\": \"nir-vanah : blowing out, extinction\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Sanskrit निर्वाण nirvāṇa- is the past participle of nir-vā- 'to blow out, be extinguished': the prefix nis- \"\n        \"(sandhi nir- before a voiced sound, exactly the alternation of node #1) plus the root vā- 'to blow' (present vāti 'it \"\n        \"blows'), so literally 'blown out'. Wiktionary s.v. nirvana: 'Sanskrit निर्वाण (nirvāṇa, \\\"blown or put out, \"\n        \"extinguished\\\"), from निस् (nis, \\\"out\\\") + वा (vā, \\\"to blow\\\")'; AHD, 'Sanskrit nirvāṇam, a blowing out, extinction, \"\n        \"nirvana : nis-, nir-, out, away + vāti, it blows. See wē-'. The metaphor is of a lamp going out, transferred in Buddhist \"\n        \"and Jain usage to the extinction of desire and of individual existence. Nourai's transliteration 'nir-vanah' is the \"\n        \"nominative singular nirvāṇaḥ (masculine) / nirvāṇam (neuter) with the long ā left unmarked, and his cross-reference to \"\n        \"'Wě 1' is precisely Watkins' root wē- 'to blow', whose only Sanskrit-based English derivative is NIRVANA.\"),\n     \"derivation_fa\": (\"«نیروانا» (निर्वाण nirvāṇa-) در سنسکریت اسم‌مفعولِ nir-vā- «بیرون دمیدن، خاموش شدن» است: پیشوند \"\n        \"nis- (که پیش از واکِ واک‌دار به nir- بدل می‌شود — همان ابدالِ گرهٔ پیشین) به‌علاوهٔ ریشهٔ vā- «دمیدن» (فعل vāti \"\n        \"«می‌دمد»)، یعنی لفظاً «دمیده‌شده/خاموش‌شده». ویکی‌واژه و فرهنگ American Heritage همین تجزیه را می‌دهند. \"\n        \"استعارهٔ آن، خاموش‌شدن چراغ است که در آیین بودا و جین به خاموشی آرزو و نیستیِ فردیت تعبیر شده است. صورت \"\n        \"«nir-vanah»ی نورایی همان nirvāṇaḥ فاعلیِ مفرد است با «آ»ی کشیدهٔ بی‌نشان، و ارجاع او به «Wē 1» دقیقاً ریشهٔ \"\n        \"*wē- «دمیدن» واتکینز است. ادعای نورایی درست است.\"),\n     \"sources\": [W_NIRV, A_NIRV],\n     \"ref_check\": [\n       {\"ref\": \"AHD:889\", \"status\": \"supports\",\n        \"note\": \"The page number belongs to the 1975 New College Edition main dictionary (not on disk), but the appendix that Nourai \"\n                \"cross-refers to is: AHD_watkins1985.txt l.1125, 'wē-. To blow ... 4. Basic form *wē- in Sanskrit vāti (stem *vā-), \"\n                \"he blows: NIRVANA. [Pok. 10. aw(ē)- 81.]', and the index l.1923 'NIRVANA wē-'. The current online AHD entry reads \"\n                \"'Sanskrit nirvāṇam, a blowing out, extinction, nirvana : nis-, nir-, out, away + vāti, it blows. See wē-' — Nourai's \"\n                \"gloss and cross-reference verbatim. 889/1505 also fits 'nirvana' alphabetically.\"},\n       {\"ref\": \"KLN:1049\", \"status\": \"supports\",\n        \"note\": \"KLN_1966.txt l.25465 (p.1049): 'nirvana ... — OI. nirvanah, lit. \\\"a blowing out (of a light), extinction, \"\n                \"disappearance\\\", which is formed fr. nis-, nir-, \\\"out, forth, away\\\" ... and vati, \\\"it blows\\\"' — including \"\n                \"Klein's own transliteration 'nirvanah', which is where Nourai's spelling comes from.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. wē- and the index (AHD_watkins1985.txt ll.1125, 1923)\", \"stance\": \"supports\",\n        \"note\": \"'Basic form *wē- in Sanskrit vāti (stem *vā-), he blows: NIRVANA' — the second element of the compound.\"},\n       {\"src\": \"POK\", \"where\": \"IEW p.81 (Pok. 10. au̯(e)-) as cited by Watkins, and p.312 for nis-\", \"stance\": \"supports\",\n        \"note\": \"Watkins refers the root to 'Pok. 10. aw(ē)- 81', Pokorny's au̯(e)-, au̯ē(o)-, u̯ē- 'blasen' — the standard \"\n                \"reference for Sanskrit vāti.\"},\n       {\"src\": \"KLN\", \"where\": \"p.1049\", \"stance\": \"supports\",\n        \"note\": \"See ref_check; Klein also links vāti to English wind.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"nîrvânâ\", \"verdict\": \"plausible\",\n     \"derivation\": (\"The Persian word نیروانا exists with exactly Nourai's meaning, but the arrow drawn straight from Sanskrit is \"\n        \"too short. نیروانا is a learned twentieth-century loan that entered Persian through European writing on Buddhism — the \"\n        \"final -â of نیروانا reflects the European spelling nirvana (English/French), not the Sanskrit nominative nirvāṇam/\"\n        \"nirvāṇaḥ that a direct borrowing would have given (compare the older Indo-Persian treatment of Sanskrit nouns, which \"\n        \"keeps the stem: e.g. برهمن, ودا). Its date and its usage confine it to modern philosophical prose and translations; \"\n        \"abadis.ir carries it only in an encyclopaedia entry (دانشنامهٔ آزاد فارسی), glossed from Sanskrit as 'to cool down, be \"\n        \"extinguished, as a candle is extinguished', with no lexicographical tradition behind it. So: word and gloss right, \"\n        \"route incomplete (Sanskrit > English/French > Persian).\"),\n     \"derivation_fa\": (\"واژهٔ «نیروانا» در فارسی هست و معنایش هم همان است که نورایی می‌گوید، اما پیکانی که یکسر از سنسکریت \"\n        \"به فارسی کشیده شده کوتاه است. «نیروانا» وام‌واژه‌ای است دانشورانه از سدهٔ چهاردهم هجری که از راه نوشته‌های \"\n        \"اروپایی دربارهٔ آیین بودا به فارسی رسیده: «آ»ی پایانی بازتاب املای اروپایی nirvana است، نه صورت فاعلیِ سنسکریت \"\n        \"nirvāṇam/nirvāṇaḥ که وام‌گیریِ مستقیم می‌بایست می‌داد (قس. رفتار دیرینِ فارسیِ هند با نام‌های سنسکریت، مانند \"\n        \"«برهمن» و «ودا» که ستاک را نگه می‌دارند). کاربردش نیز به نثر فلسفی و ترجمه‌های نو محدود است؛ آبادیس آن را تنها \"\n        \"در «دانشنامهٔ آزاد فارسی» با تعبیر سنسکریتِ «سرد شدن، خاموش شدن مانند خاموشی شمع» آورده و در فرهنگ معین نیست. \"\n        \"پس: واژه و معنا درست، ولی راهِ وام‌گیری ناقص است (سنسکریت › انگلیسی/فرانسوی › فارسی).\"),\n     \"sources\": [AB_NIRV, VJ_NIRV],\n     \"ref_check\": [\n       {\"ref\": \"MON:4882\", \"status\": \"not_found\",\n        \"note\": \"p.4882 of the 6-vol Amir Kabir Farhang falls in Mo'in's vol. 4 (foreign words and compounds), which is neither on \"\n                \"disk nor online: vajehyab.com/?q=نیروانا&d=moein answers «نیروانا» پیدا نشد! and MON_part1/part2 (the 2-vol Adena \"\n                \"condensation of the lexicon volumes) give 0 hits for نیروانا. The placement is plausible — a foreign word belongs \"\n                \"in that volume — but the entry itself could not be read.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"MON\", \"where\": \"grep نیروانا in MON_part1.txt / MON_part2.txt; vajehyab (Mo'in)\", \"stance\": \"silent\",\n        \"note\": \"0 hits in either file; vajehyab's Mo'in module: «نیروانا» پیدا نشد!\"},\n       {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' (1062/1652)\", \"stance\": \"silent\",\n        \"note\": \"Three centuries older than the word; no entry, and Mo'in added no footnote for it.\"},\n       {\"src\": \"ARY\", \"where\": \"grep نیروانا in ARY_pages.txt\", \"stance\": \"silent\",\n        \"note\": \"Aryanpur's IE-roots dictionary does not carry it.\"},\n       {\"src\": \"AHD\", \"where\": \"abadis.ir s.v. نیروانا (دانشنامهٔ آزاد فارسی)\", \"stance\": \"partial\",\n        \"note\": \"The only Persian reference work that could be read on the word gives the Sanskrit origin and the 'extinguishing of \"\n                \"a candle' image, but says nothing about how the word reached Persian.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"English\", \"words\": \"Nirvana\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"English nirvana is a direct scholarly borrowing of Sanskrit nirvāṇa-, first used in English in 1836 (Turnour's \"\n        \"and later Max Müller's and Rhys Davids' writings on Buddhism), taken over in the stem form without the case ending and \"\n        \"with the Sanskrit retroflex ṇ simply written n. AHD gives 'Sanskrit nirvāṇam, a blowing out, extinction, nirvana : nis-, \"\n        \"nir-, out, away + vāti, it blows. See wē-' and Klein p.1049 the same, with the gloss Nourai copies word for word: \"\n        \"'extinction of the individual soul by absorption into the supreme spirit (Hinduism)'. The weakened sense 'blissful \"\n        \"oblivion' is a 20th-century extension and does not affect the etymology.\"),\n     \"derivation_fa\": (\"«Nirvana» انگلیسی وام‌واژه‌ای است مستقیم و دانشورانه از سنسکریت nirvāṇa- که نخست‌بار در ۱۸۳۶ م. در \"\n        \"نوشته‌های بوداشناسان انگلیسی‌زبان به کار رفت؛ ستاک واژه بدون پایانهٔ اعرابی گرفته شده و «ن»ی خیشومیِ کامی \"\n        \"(ṇ) ساده نوشته شده است. فرهنگ American Heritage و کلاین (ص ۱۰۴۹) هر دو همان تجزیه و همان تعریفی را می‌دهند که \"\n        \"نورایی واژه‌به‌واژه نقل کرده است: «خاموشی روح فردی با فرورفتن در روح برتر». معنای سبک‌شدهٔ «سرخوشیِ بی‌خبری» \"\n        \"افزودهٔ سدهٔ بیستم است و به ریشه‌شناسی آسیبی نمی‌زند. ادعای نورایی درست است.\"),\n     \"sources\": [W_NIRV, A_NIRV],\n     \"ref_check\": [\n       {\"ref\": \"AHD:889\", \"status\": \"supports\",\n        \"note\": \"The 1975 page is not on disk, but the appendix Nourai cross-refers to is (AHD_watkins1985.txt l.1125: '... he blows: \"\n                \"NIRVANA'), and the current online AHD entry gives 'Sanskrit nirvāṇam, a blowing out, extinction, nirvana : nis-, \"\n                \"nir-, out, away + vāti, it blows. See wē-' — matching both the gloss and the ☞Wē cross-reference on the chart.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"p.1049 s.v. nirvana (KLN_1966.txt l.25465)\", \"stance\": \"supports\",\n        \"note\": \"'nirvana, n., extinction of the individual soul by absorption into the supreme spirit (Hinduism) — OI. nirvanah ...' \"\n                \"— Nourai's English gloss is Klein's, verbatim.\"},\n       {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls (FSD_vol3.txt ll.58279-58283)\", \"stance\": \"supports\",\n        \"note\": \"'... philosophy it was sometimes called Nirvana, a name ...' / 'Mukti, Moksha, or Nirvana' — the word is current in \"\n                \"English with this sense, though the L-volume article itself did not survive the OCR.\"},\n       {\"src\": \"AHD\", \"where\": \"Watkins 1985 index (AHD_watkins1985.txt l.1923)\", \"stance\": \"supports\",\n        \"note\": \"'NIPPLE nabja- NIRVANA wē-' — the appendix's own index assigns English NIRVANA to the root wē-.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\n# strip helper keys that are not part of the schema\nfor e in data[\"entries\"]:\n    for n in e[\"nodes\"]:\n        n.pop(\"derivation_note\", None)\n\nout = \"/home/sfmqrb/git/rishe/data/verification/page-366.json\"\nwith open(out, \"w\", encoding=\"utf-8\") as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\", out)\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk366.py"
}
```


### [2026-09-07T19:49:24.285Z] TOOL RESULT

```
written /home/sfmqrb/git/rishe/data/verification/page-366.json
```


## [2026-09-07T19:49:29.698Z] TOOL CALL #94: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -m json.tool data/verification/page-366.json > /dev/null && echo \"JSON OK\"\npython3 -c \"\nimport json;d=json.load(open('data/verification/page-366.json'))\nprint(json.dumps(d['entries'][0]['sources'],ensure_ascii=False))\n\"\npython3 tools/verify_check.py 366"
}
```


### [2026-09-07T19:49:31.060Z] TOOL RESULT

```
JSON OK
["https://en.wiktionary.org/wiki/%D9%84%DB%8C%D9%85%D9%88", "https://www.etymonline.com/word/lemon", "https://www.etymonline.com/word/lime", "https://www.ahdictionary.com/word/search.html?q=lemon", "https://www.ahdictionary.com/word/search.html?q=lime"]
nodes verified: 14/14
node verdicts: {'confirmed': 11, 'disputed': 1, 'unverified': 1, 'plausible': 1}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'supports': 8, 'partial': 1, 'not_checked': 10, 'not_found': 1}
books consulted: {'silent': 12, 'supports': 27, 'partial': 6, 'contradicts': 2} | by book: {'KLN': 7, 'LKT': 5, 'ARY': 3, 'DEV': 3, 'MON': 3, 'BQT': 3, 'FSD': 3, 'AHD': 3, 'PLA': 2, 'PHN': 2, 'SKT': 2, 'HJB': 2, 'POK': 2, 'HRN': 1, 'HUB': 1, 'PHD': 1, 'TTS': 1, 'AFM': 1, 'BRT': 1, 'KNT': 1}
```


## [2026-09-07T19:49:44.975Z] TOOL CALL #95: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'EOF'\nimport json,glob,os,re\nidx=None\nfor p in ('data/verification/sources/web/index.json','data/verification/sources/web/index.jsonl'):\n    if os.path.exists(p): idx=p\nprint('index:',idx)\ntxt=open(idx,encoding='utf-8').read() if idx else ''\nurls=[\"https://en.wiktionary.org/wiki/%D9%84%DB%8C%D9%85%D9%88\",\"https://www.etymonline.com/word/lemon\",\"https://www.etymonline.com/word/lime\",\"https://en.wiktionary.org/wiki/limon\",\"https://en.wiktionary.org/wiki/nirvana\",\"https://www.ahdictionary.com/word/search.html?q=lemon\",\"https://www.ahdictionary.com/word/search.html?q=lime\",\"https://www.ahdictionary.com/word/search.html?q=nirvana\",\"https://en.wiktionary.org/wiki/%E0%A4%A8%E0%A4%BF%E0%A4%B8%E0%A5%8D\",\"https://abadis.ir/fatofa/%D9%86%DB%8C%D8%B1%D9%88%D8%A7%D9%86%D8%A7/\",\"https://abadis.ir/fatofa/%D9%84%D8%A7%DB%8C%D9%85/\",\"https://vajehyab.com/?q=%D9%86%DB%8C%D8%B1%D9%88%D8%A7%D9%86%D8%A7&d=moein\"]\nfor u in urls:\n    print(('OK  ' if u in txt else 'MISS'), u)\nEOF"
}
```


### [2026-09-07T19:49:46.229Z] TOOL RESULT

```
index: data/verification/sources/web/index.jsonl
OK   https://en.wiktionary.org/wiki/%D9%84%DB%8C%D9%85%D9%88
OK   https://www.etymonline.com/word/lemon
OK   https://www.etymonline.com/word/lime
OK   https://en.wiktionary.org/wiki/limon
OK   https://en.wiktionary.org/wiki/nirvana
OK   https://www.ahdictionary.com/word/search.html?q=lemon
OK   https://www.ahdictionary.com/word/search.html?q=lime
OK   https://www.ahdictionary.com/word/search.html?q=nirvana
OK   https://en.wiktionary.org/wiki/%E0%A4%A8%E0%A4%BF%E0%A4%B8%E0%A5%8D
OK   https://abadis.ir/fatofa/%D9%86%DB%8C%D8%B1%D9%88%D8%A7%D9%86%D8%A7/
OK   https://abadis.ir/fatofa/%D9%84%D8%A7%DB%8C%D9%85/
OK   https://vajehyab.com/?q=%D9%86%DB%8C%D8%B1%D9%88%D8%A7%D9%86%D8%A7&d=moein
```


## [2026-09-07T19:50:04.812Z] AGENT

Done — `/home/sfmqrb/git/rishe/data/verification/page-366.json` written, `verify_check.py 366` reports 14/14 nodes and **0 PROBLEM lines**.

**Page 366 (book 336) — 2 entries, 14 nodes**
- Roots: 1 confirmed (Nîmbǔ/Limǔ), 1 plausible (Nis)
- Nodes: 11 confirmed, 1 disputed, 1 plausible, 1 unverified
- Ref checks: 8 supports, 1 partial, 1 not_found, 10 not_checked (VOP ×3 and DZA have no scan anywhere; AHD main-dictionary pages 748/758/889 are not on disk — content checked in the online AHD instead)

**Disputed**
- Nis, node #4 French *limon, limonâd*: word real, **parent wrong**. Nourai (following Klein p.878, which he cites) makes Fr. limon a loan from Turkish; AHD, Etymonline, Wiktionary and Asbaghi all route it Persian → Arabic *laymūn* → Italian *limone*/Prov. *limon* → French, and Hobson-Jobson names the Crusades/Moorish Spain. Devic p.152 and Asbaghi p.243 explicitly contradict the Turkish step.

**Unverified**
- Nîmbǔ, node #10 Persian *lâym* "a drink": no source either way — VOP:314 undigitised, Mo'in has 0 hits, abadis s.v. لایم gives only Arabic لائم "blamer".

**Plausible**
- Root *Nis*: real (Kent p.193 "pIE *nis-", Klein p.1049), but the root box has **no gloss**, and Pokorny p.312 / Mann col. 900 file it under *ni-, *nei- "down" with no separate *nis- lemma (Indo-Iranian + Slavic only).
- Node #3 Persian نیروانا: word and gloss right, but it is a 20th-c. loan via English/French (final -â), not straight from Sanskrit as drawn.

**For the owner (extraction)**
- The printed page has a **completely blank box** (no language, no refs, no word) joined by a plain line to the right of entry 1's Avestan/Old Persian node; it is empty in the book itself and absent from the JSON — nothing to fix, but noted in the entry's `note`.
- `refs/SKT.txt` (Google scan) is an **earlier impression** of Skeat's Concise: Lemon on p.245 and **no "Lime (3)" entry at all**, so Nourai's SKT page numbers don't map. The revised text (archive.org `in.ernet.dli.2015.158267`) has "Lime (3), a kind of citron … Malay līmau" at p.294/295 — matching SKT:295. I copied that OCR to `data/verification/sources/refs/SKT_dli_revised.txt` (gitignored) for audit.
- New audit artefacts: `refs/ocr/BQT/1922.png` + `1922.vision.txt` (Mo'in's footnote on لیمو, read from the image); 12 web pages archived via `fetch_source.py`.
- Not committed — left for the coordinator.
