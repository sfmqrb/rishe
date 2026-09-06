# Verification process log — verify-page-245


## [2026-09-06T15:52:09.471Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 245 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-245.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-245.json. Write /home/sfmqrb/git/rishe/data/verification/page-245.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 245` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T15:52:11.145Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T15:52:11.729Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T15:52:11.744Z] TOOL RESULT

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


## [2026-09-06T15:52:12.011Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-245.txt"
}
```


### [2026-09-06T15:52:12.029Z] TOOL RESULT

```
1	=== PDF page 245 (book page 215) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Kau, Qau 1 : to strike, beat  (refs POK:535; WLD:331)
4	#1 (parent #0) [Avestan] refs=SYN:290; WLD:331; SNS:150 | kôš : strike ; fra-košaiti : kills ; kau-kušati : tries, fights ; thwaxša : try
5	  #2 (parent #1) [Persian] refs=BQT:1648, 1731 | koštan «کشتن» : to kill ; kŭšîdan «کوشیدن» : to try, to fight | extra: کوشش
6	#3 (parent #0) [Germanic] refs=AHD | haujam : cut grass
7	  #4 (parent #3) [English] refs=None | hay ; hoe
8	--- entry 1 ---
9	ROOT [Indo-European] Kau 2, Qau 2, Kâukos : to howl, a raucous bird  (refs IEC:483; POK:434)
10	#1 (parent #0) [Persian] refs=IEC:1521; MON:2888 | kabk «کبک» : partridge
11	#2 (parent #0) [Sanskrit] refs=AHD:1521 | cakôra : partridge
12	--- entry 2 ---
13	ROOT Kâukos -> redirect to Kau 2
14	--- entry 3 ---
15	ROOT [Indo-Schythian] Kavŭta : gray, dark blue  (refs ISS:43)
16	#1 (parent #0) [Old Persian] refs=ISS:43 | kapautaka : gray, dove
17	  #2 (parent #1) [Pahlavi] refs=HRN:187; KNT:178 | kapôt, kapôtar
18	    #3 (parent #2) [Persian] refs=BQT:1589; MON:2890 | kabŭd «کبود» : gray, dark blue, purple ; kabŭtar «کبوتر» : dove | extra: کفتر | NOTE: CEL6:46 derives "kabŭtar" from Indo-European "Kepro: a kind of bird"
19	  #4 (parent #1) [Sogdian] refs=ISS:43; SOD:191 | kp`wtk : blue ; kp`wt`yčh : dove
20	#5 (parent #0) [Latin] refs=ISS:43 | capotes : dove (a Latin-Armenian word)
21	#6 (parent #0) [Greek] refs=ISS:43 | kapauta : dove (a Greek-Armenian word)
22	#7 (parent #0) [Sanskrit] refs=ISS:43 | kapôta : dark blue, dove
23	
```


## [2026-09-06T15:52:15.033Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-245.json",
 "description": "Read source JSON for page 245"
}
```


### [2026-09-06T15:52:15.104Z] TOOL RESULT

```
{
  "pdf_page": 245,
  "book_page": 215,
  "entries": [
    {
      "root": {
        "name": "Kau, Qau 1",
        "lang": "Indo-European",
        "refs": "POK:535; WLD:331",
        "gloss": "to strike, beat"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "SYN:290; WLD:331; SNS:150",
          "words": [
            {"translit": "kôš", "gloss": "strike", "script": null},
            {"translit": "fra-košaiti", "gloss": "kills", "script": null},
            {"translit": "kau-kušati", "gloss": "tries, fights", "script": null},
            {"translit": "thwaxša", "gloss": "try", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1648, 1731",
          "words": [
            {"translit": "koštan", "gloss": "to kill", "script": "کشتن"},
            {"translit": "kŭšîdan", "gloss": "to try, to fight", "script": "کوشیدن"}
          ],
          "script_extra": "کوشش",
          "note": null,
          "quote": {
            "text": "زبهر تن شـاه غـمخـواره ایم - نه از کوشش و جنگ بیچاره‌ایم",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "haujam", "gloss": "cut grass", "script": null}
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
            {"translit": "hay", "gloss": null, "script": null},
            {"translit": "hoe", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Kau 2, Qau 2, Kâukos",
        "lang": "Indo-European",
        "refs": "IEC:483; POK:434",
        "gloss": "to howl, a raucous bird"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "IEC:1521; MON:2888",
          "words": [
            {"translit": "kabk", "gloss": "partridge", "script": "کبک"}
          ],
          "note": null,
          "quote": {
            "text": "بهوای کبک رفتم که چو باز حمله آرم - زهلاک خویش غافل که ز پی بود عقابم",
            "poet": "Qâânî"
          }
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "AHD:1521",
          "words": [
            {"translit": "cakôra", "gloss": "partridge", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Kâukos",
        "redirect": "Kau 2"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Kavŭta",
        "lang": "Indo-Schythian",
        "refs": "ISS:43",
        "gloss": "gray, dark blue"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "ISS:43",
          "words": [
            {"translit": "kapautaka", "gloss": "gray, dove", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "HRN:187; KNT:178",
          "words": [
            {"translit": "kapôt, kapôtar", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:1589; MON:2890",
          "words": [
            {"translit": "kabŭd", "gloss": "gray, dark blue, purple", "script": "کبود"},
            {"translit": "kabŭtar", "gloss": "dove", "script": "کبوتر"}
          ],
          "script_extra": "کفتر",
          "note": "CEL6:46 derives \"kabŭtar\" from Indo-European \"Kepro: a kind of bird\"",
          "quote": {
            "text": "غلام همّت آنم که زیر چرخ کبود - زهرچه رنگ تعلق پذیرد آزاداست",
            "poet": "Hâfez"
          }
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "ISS:43; SOD:191",
          "words": [
            {"translit": "kp`wtk", "gloss": "blue", "script": null},
            {"translit": "kp`wt`yčh", "gloss": "dove", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Latin",
          "refs": "ISS:43",
          "words": [
            {"translit": "capotes", "gloss": "dove (a Latin-Armenian word)", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Greek",
          "refs": "ISS:43",
          "words": [
            {"translit": "kapauta", "gloss": "dove (a Greek-Armenian word)", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "ISS:43",
          "words": [
            {"translit": "kapôta", "gloss": "dark blue, dove", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-06T15:52:17.389Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo \"---\" && python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','WLD','SYN','SNS','BQT','AHD','IEC','MON','ISS','HRN','KNT','SOD','CEL','ARY','SKT','KLN','PHD','NYB','BRT','HUB']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:400])\n\""
}
```


### [2026-09-06T15:52:19.160Z] TOOL RESULT

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
---
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
ISS {"title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967", "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute", "kind": "google_books_preview+archive_restricted", "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
CEL {"title": "S. K. Gupta, A Comparative Etymologic Lexicon of Common Indo-European Words, 6 vols., Milton MA 1997", "edition_found": null, "kind": "catalog", "url": "HathiTrust mdp.39015021572337 etc. (8-vol 1986- ed., search-only) ; Open Library records", "identifier": null, "local_file": null, "page_offset": null, "lookup_hint": null, "notes": "RE-SEARCH 2026-09: catalogue only; the 1997 Sverge Ha
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
```


## [2026-09-06T15:52:22.383Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-202.json'))\nprint(json.dumps(d['entries'][0], ensure_ascii=False, indent=1)[:3500])\n\""
}
```


## [2026-09-06T15:52:23.019Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n 1,120p data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-06T15:52:24.207Z] TOOL RESULT

```
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
   "where": "Bd. I 675-677 (WLD_Bd1 djvu line 42665 ff., running head 'gʷem-, gʷā-')",
   "stance": "supports",
   "note": "'gʷem-, gʷā-' … 'ai. gātram „Glied, Körper“; ai. gātu- „Gang, Weg, Raum, Ort“, av. gātu-s „Ort, Platz; Liegerstatt, Sessel, Thron“, ap. gāθu … ai. vi-gāman- n. „Schritt“ … av. gāman- n. „Schritt“'. This is the source Pokorny 463 abridges (Buck cites it as 'Walde-P. 1.675 ff.')."
  },
  {
   "src": "AHD",
   "where": "Watkins 1985, g-list (AHD_watkins1985.txt line ~539)",
   "stance": "supports",
   "note": "'gʷā-. Also gʷem-. To go, come. 1. Germanic *kum
```


### [2026-09-06T15:52:24.245Z] TOOL RESULT

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


## [2026-09-06T15:52:55.390Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"hauen, schlagen\" POK_0*.txt | head -20; echo \"=== 434 area\"; grep -n \"heulen\" POK_0*.txt | head -30"
}
```


### [2026-09-06T15:52:55.459Z] TOOL RESULT

```
=== 434 area
POK_03.txt:23:Gr.  (b,  ä  Ausruf  bes.  des  Erstaunens,  Vokativpartikel  (davon  öjI^slv  ,oh; rufen*,  d)'^  ,heda!S  vgl.  auch  wörtj  ort  ,ermunternder  Zuruf  der  RudererM nach  Kretschmer  KZ.  38,  135  auch  in  gr.  d)-Qvoiiai  ,heulen,  brüllen*).
POK_03.txt:4842:Ai.  thuthukrt-  m.  ,ein  bestimmter  Vogel,  Ringeltaube^;  gr.  rvTcb'  fj  ylav^ Hes.,  rovrig'  6  -AÖoavcpog  Hes.;  lat.  tutubäre  ,schreien'  (von  der  Eule),  vgl. Plaut.  Men.  653 f.  ^vln  adferri  noctuam,  quae  „tu,  tü^  usque  dicat  tihiV -^ lit.  tütüoti  ,tuten^,  tutlys,  tutütis  , Wiedehopf';  im  Germ,  neugeschaffen (oder  mit  stockender  Lautverschiebung  im  Schallwort)  mnd.  (nhd.)  tüten tuten\  aisl.  tauta,  tutla  , murren*;  als  älterer  Typus  {^tü  mit  cZ-Präsens) i^s.  dütan  , einen  Ton  ausstoßen',  aisl.  Pjöta  ,heulen,  einen  starken  Ton geben',  ags.  deotan  ,heulen,  widerhallen,  lärmen',  ahd.  diozan  ,laut  tönen*, »isl  pytr  , starker  Ton,  GeheuP,  mhd.  duz,  diez,  döz  , Schall,  Geräusch*, got.  puthaürn  ,Tuthorn,  Trompete*,  aisl.  pyss  ,Lärm',  ags.  dyssa  m.  ,Toser*.
POK_03.txt:4938:j^  Schallwz.  , heulen',  vielfach  redupl.  ulul-,
POK_03.txt:4940:ai.  uhli-j  ulülu-  ,ululabilis,  ululatus',  gr.  ^Aaw,  vla-Ktso)  ,belle',  lat.  uln- are ,heulenS  ulula  f.  ,Kauz*,  lit.  ulula  bangos  ,es  heulen  die  Wellen', ulülötij  ulöti  , hallo  rufen',  ulhüoti,  iilhauti  ,rufen,  singen,  schreien';
POK_03.txt:5008:für  isl.  sukka  ,lärmen',  daneben  svakke,  ist  jedoch  Vergleich  mit  BOfWt dial.  seykia  ,bellen'  und  lit.  saugti  , eigenartig  singen',  alit.  sugti  ,betikly winseln',  lett.  sudzet  ,klagen',  sükstities  , seufzen'  (daneben  ^-Formen  wit  Bti saukill  durch  Einfluß  von  kaukti  ,heulen',  §aükti  , schreien')  untar  M|^» *s(e)ug-  möglich;  got.  sioegnjan  ,frohlocken'  könnte  auf  Grund  von  yif»» swög-j  swag-  als  Schall  wort  ins  Leben  gerufen  worden  sein;  das  -Wf-  » aisl.  sukka  ist  intensivierend.
POK_01.txt:1325:Mit  auslautenden  Gutturalen:  ai.  bük-kära-h  ,Gebrüll  des  Löwen^, bukkati  ,bellt^  (av.  bucahin-  ,der  das  Geheule,  Gefauche  an  sich  hat', buxti'  ,Heulen,  Fauchen'^?),  gr.  ßvKTVjQ  ,heulend^
POK_01.txt:1376:WP.  II  120  f.,  W^H.  I  95.   Vgl.  auch  bhU-  ,heulen'  usw.
POK_01.txt:1726:mit  germ.  II  (Konsonantenschärfung  in  der  Schallwurzel),  ahd.  bellan ,bellen',  ags.  bellau  ,brüllen,  bellen,  grunzen';  ahd.  bullön  ,heulen  (vom Wind),  bellen,  brüllen',  isl.-norw.  bulla  , babbeln,  schwatzen';  aisl.  bjalla, ags.  belle,  engl,  bell,  mnd.  belle  , Schelle,  Glocke',  nhd.  (eigentl.  ndd.)  Bell- hammel , Leithammel  (mijt  Schelle)';
POK_01.txt:2195:bblB'  ,heulen,  laut  weinen,  blökend
POK_02.txt:546:alb.  ngurönj  ,heulen'  (vom  Wind) ;
POK_02.txt:563:mhd.  krischen  ,kreischen',  mnd.  krlten  , schreien,  heulen',  mhd.  krlen , scharf  schreien',  nhd.  kreißen,  mhd.  kristen,  nhd.  kreisten.
POK_02.txt:918:russ.  gogotdth  _,gackern,  schnattern;  laut  lachen^  mdartl.  ,wiehern^,  öech. alt  Jiohtati  ,heulen^,  poln.  gogotac  ,glucken^,  osorb.  gagotac,  gigotac  (wegen g  statt  h  jüngere  Lautnachahmung)  ,schnattern^ ;  russ.  gdgatb  ,schnattern, von  Gänsen^,  9dgci  ^Eidergans^,  gagdra  ,Taucher^  usw.
POK_02.txt:1246:ags.  gleljpan  (st.  V.)  ,prahlen',  mhd.  gelpfen,  gelfen  , schreien,  singen, prahlen',  aisl.  gjalp  n.  , Prahlerei',  ags.  gielp  ds.,  as.  gelp  , Trotzrede,  Hohn', ahd.  gelph  , Trotzrede,  Prahlerei',  adj.  ,lustig,  übermütig',  ahd.  gelb^ ,jemd.  täuschen',  as.  galpön  (schw.  V.)  ,laut  schreien,  prahlen',  dän.  gylpe, gulpe  , schluchzen,  wie  ein  Rabe  schreien'  (mit  germ.  S  aisl.  gjalfr  ,Wellen' getöse',  gylfi  ,König,  Fürst^,  gylfin  n.  , Unhold',  gylfra  f.  ,Hexe',  gylfr^'^^gfi m.  , Schwert',  mnd.  gelve  ,Woge',  ndl.  golf  , Welle',  dial.  galveren,  golveren] .schallen,  heulen') ;
POK_02.txt:1596:dazu  wohl  aisl.  geyja  ,bellen,  schelten,  spotten',  ags.  giegan  , schreien'; aisl.  god-gä  , Gotteslästerung',  hund-gä  ,Bellen'  und  die  Weiterbildungen aisl.  gauta  , schwatzen,  prahlen',  ndld.  guiten  ,ausschelten,  spotten',  nhd. dial.  ganzen^  ganzen  ,bellen,  schreien',  got.  gaunön  ,klagen,  trauern',  aisl. gaula  , heulen';  über  lit.  gausti  s.  unter  gou-  , rufen,  schreien'.  Trotz des  nichtpalatalen  Wurzelanlauts  (s.  oben  über  lit.  gomurys)  könnte  es •hierher  gehören,  da  viele  ursprüngl.  palatale  Gutturale  litauisch  als  ^,  k erscheinen.
POK_02.txt:2432:Das  mit  gr.  ^fxegog  gleichgesetzte  ahd.  asächs.  jämar,  ags.  geomor ,traurig',  Subst.  ahd.  jämar  yjammer^  (ursprüngl.  angeblich  ,bedrückt^) dürfte  jedoch  wegen  anord.  amra  ,jammern',  das  zu  emja,  ymja  ,heulen' gehört,  eher  einer  Interjektion  entsprungen  sein.  Cymr.  afar  ,Leid,  Klage' (mir.  amar  ds.)  kann  kein  j-  verloren  haben  und  muß  schon  deswegen fernbleiben.
POK_02.txt:2591:mhd.  jü,  jüch  ,Ausruf  der  Freude'  (ähnlich  jö  beim  Aus-  und  Zuruf)^ davon  mhd.  jüwen,  jüwezen  ,ju  rufen,  jubeln',  jüchezen,  nhd.  jauchzen^ juchzen,  mhd.  jölen,  jodeln,  nhd.  johlen,  jodeln,  auch  anord.  yla,  engl,  yowl ,heulen'  aus  *jüljan'^
POK_02.txt:2956:käu-,  keu-,  kü-  ,heulen^;  kauä  ,schreinder  Vogel;  Schallwurzel,  teils  mit anlaut.  kj  teils  mit  k.
POK_02.txt:2957:Ai.  käuti  , schreit^.  Intens,  köküyate  ,schreit,  tönt,  seufzt*  (Gramm.), köka-  m.  ,Eule,  Hund^?  (,schreiend;  heulend^);  kohila-  , Kuckuck^;
POK_02.txt:2963:ahd.  hüiüo  ,Eule^,  hüwila,  hiuwula  ^Nachteule^,  ahd.  hiuwilön  ,jubeln< mhd.  Muweln,  hiulen  ,heulen,  schreien^,  mnd.  hülen,  mengl.  hülen,  engl. howl ;
POK_02.txt:2964:lit.  (s.  oben)  kaukiü,  kaükti,  lett.  käukt  ,heulen,  von  Hunden  oder  Wölfen', lit.  sukükti  jds.j  aufheulen^,  kaukaU  ^eine  Art  WasservogeP,  lett.  kaüka ;,Sturmwind^ ;
POK_02.txt:3193:Erweiterung  *k(e)len2-  (vgl.  lat.  clä-m-äre) :  ai.  Ä:raw<^aii , schreit,  brüllt, wiehert'  (*klem-d-?)]  ags.  hlimman,  hlymman  ,klingen,  tönen,  rauschen, brüllen',  hlimme  ,reißender  Strom',  hlemm  {^hlammi)  ,Schall',  ahd.  (h)limmen ,brummen,  heulen',  anord.  hlymja  ,klingen,  krachen,  lärmen',  ahd.  hlamön ,rauschen,  tosen';
POK_02.txt:5376:Vielleicht  auf  ders.  Schallvorstellung,  aber  mit  a-Vokalismus,  beruht gr.  la7tiC,ü)  ^benehme  mich  übermütig',  XaTTLaTrjg  ^Aufschneider,  Prahler' und  hxXXaxp  ,Sturmwind'  (als  ,heulend').
```


## [2026-09-06T15:52:56.688Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== BRT kaoš\"; grep -n -i \"kao\\?š\\|kaoša\\|frakaoš\" BRT.txt | head -30; echo \"== CHEUNG kauš\"; grep -n \"kauš\\|kaus\" CHEUNG.txt | head -40"
}
```


### [2026-09-06T15:52:56.757Z] TOOL RESULT

```
== BRT kaoš
== CHEUNG kauš
16656:*kausl 251 
16680:*kauš! ‘to fight, struggle; to kill’ 
16713:*IE COGNATES: Toch. A kos-, B kaus- (pres.) ‘to kill, strike down, destroy’ 
16716:252 *kaus2 
16737:0 The Iranian evidence for a root *kauš is confined to Sogd. and possibly Khot. / 
54825:kaus- (B), 251 
55616:(s.v.), *kaup!, *kaus! (s.v.), 
56593:*Hiaud, *Hrab/f, *kaus , 
56946:*jan, *kaus’ 
57081:*daiH! , *haiz, *kas! , *kaus? 
57769:*kaus’, *uai(H)n 
58081:*Hiaud, *kaus' , *par’, *part,
```


## [2026-09-06T15:53:02.246Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '16650,16760p' CHEUNG.txt"
}
```


### [2026-09-06T15:53:02.293Z] TOOL RESULT

```
BSogd. wk’wr ‘(blood)relative, kinsfolk, family’ 

*NWIR: Kurd. kur (m.), Bakht. kur(r), Gz. kur, Gur. kur ‘son, boy’, Tal. kara foal’, ? 
NP kir (*kuria- ?), Khuns. kur ‘penis’ ( *kura- ?) 


*kausl 251 


*NEIR: (+ *ui-) Oss. I. g;yryn/g,yrd, D. igurun/igurd ‘to be born; exist’ 

*SANSKRIT: ? küla- ‘household, whose members include slaves, servants, etc., 
(blood)relatives and guests’ (RVh, AVh, Вг+) = EWAia I: 372 f. 

9 The root *kur- is probably nominal in origin. The Oss. verbal formation appears to 
be denominative: the absence of an ablaut alternation in the pres./partic. is an 
indication. Note also Oss. I. ag,yryn/ag,yrd, D. agurun/agurd ‘to seek, demand’ (< 
Caucasian ?), I. kuryn/k,yrd, D. korun/kurd ‘to ask’. Similar forms for a small 
animal, young are also found in geographically close languages: Hitt. /kurka-/ (c.) 
‘foal, colt’, Gr. к®©руос ‘bastard son’ (Hes.), Arm. k‘urak ‘foal’ (< Hitt., Ir. ?).The 
Skt. form does not fit in this category very well: different origin ? The Lith. cognate 
kurtas ‘greyhound’ quoted by Mayrhofer, EWAia I: l.c. appears to be an old Slavic 
borrowing *x»rt» ‘id.’, which can hardly be traced back to IE. 


*PIE— > LIV: —| Pok.: 
*REFERENCES: KPF II: 262 f.; Abaev, Slovar’ I: 532, 36, 602; WIM I: 366; Szemerényi 1977: 12 ff.; WIM 
П/2: 693; Vahman — Asatrian 1991: 112 f.; Cabolov 2001: 525; Cheung 2002: 192, 198 


*kauš! ‘to fight, struggle; to kill’ 

*AVESTAN: Y Av. kuš- ‘to fight, struggle’ = Liste: 16 

Pres. them.: IND. 3sg. YAv. fra(-ca) kusaiti (V 5.34) 

*MIDDLE PERSIAN: MMP kws-, qws- ‘to struggle; kill’, BMP kwhs- /koxS-/ ‘to strive, 
struggle, endeavour’, BMP kws- (NKSWN-) /kus-/ ‘to kill’, BMP kwhssn /köxsisn/ 
‘strife, combat? > DMMPP: 215a f. 

Well attested: Pres.: IND. 1sg. MMP qwsym, 3sg. ВМР kwhsyt /koxSéd/, ВМР kwsyt /kuséd/, BMP 
kwsynd /kösend/, etc. 

*PARTHIAN: ? kwš- ‘to struggle’ = Ghilain: 66 | DMMPP: 215a 

Partic.: perf. pass. II ? kws’d (not found in DMMP} 

*CHORESMIAN: mjkš- ‘to butt (with the horns)’ = Samadi: 105 

*NWIR: Widely attested: NP kustan/kus- ‘to kill, slay; to beat, bruise’, Bal. kust/kus-, 
Kurd. kustin/kuz-, Zaz. kistis/kiSen-, Anar. -ikust/ (impv.) Ikiš (or ikus ?), Awrom. 
kuštáy/k”š-, Abyan., Abz. kösta/kös-, Gz. kes-/kust, Gil. (Rsht.) kustoen/kus-, Gur. 
(Kand.) kust-/-kus-, Ham. kostän/koS-, Isfah. kosdän/k(e)S-, Khuns. kus-/kust, Mah. 
kus-, Qohr. küsta/küs-, Semn. kustä/ (impv.) -kus, Sang. -kóst-/kosSaen-, Siv. kusten 
/kus-, Shamerz. -küst-/kosam-, Soi küst-/-küs, Sorkh. -kust-/kus-, Lasg. -košt ‘to 
kill’, NP kusti ‘fighting, wrestling’ 

© This well attested Ir. root goes back to has an ingress. so-formation of IE *keHju-, 
cf. OCS kovati ‘to forge’, Lith. käuti ‘to murder, beat, hew’, OHG houwan, OE 
héawan, Engl. to hew, etc. This formation has an exact correspondence in Toch. 

“PIE ingress. *keHzu-s°/,- > LIV: 345 f. | Pok.: 535 

*IE COGNATES: Toch. A kos-, B kaus- (pres.) ‘to kill, strike down, destroy’ 


252 *kaus2 


*REFERENCES: КРЕТ. 83a, 208b, 248a f.; Ivanow 1926: 421; КРЕП: 216 f.; Christensen, Contributions I: 
71; Christensen, Contributions II: 61, 117, 161; Abrahamian 1936: 117, 130; Abaev, Slovar’ I: 603; 
MacKenzie 1966: 100; EVS: 40a; WIM I: 70; WIM II/1: 78; WIM III: 112; Adams 1999: 208, 210; Paul 
1998: 303b; Steblin-Kamenskij 40a; Cabolov 2001: 525 f.; Lecoq 2002: 121, 123, 126 (passim); Korn 
2005: 318, 392 


*kaug ‘to look, see’ 
*KHOTANESE: (+ *us-) ? OKh. uskus- ‘to act frivolously’ = SGS: 17 
*SOGDIAN: (+ *ati-) SSogd. tkws ‘to look after, nurse’, BSogd. tk’ws ‘to examine, 


look’, CSogd. tkws, MSogd. tkws ‘to look, observe’ 
Widely attested: Pres.: IND. 2sg. BSogd. tk’ws, 3sg. BSogd. tk’wst, BSogd. tk’wyst, CSogd. tkwst, 
MSogd. tkwst (BBB: 35), etc. 


*NEIR: ? Yi. kös-/kist ‘to search for’ (rather *kas! ?) 
0 The Iranian evidence for a root *kauš is confined to Sogd. and possibly Khot. / 
Yidgha. This "root" may be a so-formation of a root cognate with Skt. Кау 0 


intend to’ (EWAia I: 328). 
*REFERENCES: IIFL II: 219b; DKS: 63 


*kauz! *to search, seek" 

*KHOTANESE: kus- ‘to search, seek’ = SGS: 23 

*SOGDIAN: BSogd. ywyz- (yw(y)z-), MSogd. xwj- ‘to wish, demand’ (initial 
fricative < ?) 

Pres.: IND. 3sg. BSogd. ywyzt, 3pl. BSogd. ywyz’nt, SUBJ. 3sg. BSogd. ywyz’t, OPT. 3sg. BSogd. 
ywyz’y, BSogd. ywz’y; Inf.: BSogd. ywyz’y, BSogd. ywz’y, POT.-SUBJ. 3sg. BSogd. ’ywst’ wn’’t, 
BSogd. ’ywstw wn” t; Inf.: pret. BSogd. ’ywst’, BSogd. ’ywstw 

*CHORESMIAN: kwzy- ‘to ask for, plea, beg’; ? kwcy- ‘to seek, search; ask for’ (with 
unexplained -c-) = Samadi: 106 f. 

*NEIR: (+ *us-) ? M. wuskuj-/wuskujoy- ‘to seek’ (Zarubin)
```


## [2026-09-06T15:53:02.536Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=2900 && NR<=2975' POK_02.txt | grep -n \"\" | tail -60"
}
```


### [2026-09-06T15:53:04.310Z] TOOL RESULT

```
17:WP.  I  358,  WH.  I  179.
18:534  •
19:1.  kat-  , flechtend   zusammendrehen,   zu   Ketten,    Stricken,    Hürdengeflecht'.
20:Lat.  catena  , Kette'  (*cates-nä),  cassis,  -is  ,Jägergarn,  Netz'  (wegen  caUna eher  =  *kat-s-is  als  *kat-ti-s-  vielleicht  auch  casa  ,primitive  Hütte'  (xlt- ^prünglich  aus  leichtem  Geflecht;  wohl  dial.  aus  *catiä,  wie  osk.  Bansae aus  Bantiae))
21:vielleicht  hierher  caterva  f.  ,Hau£e,  Schar,  Truppe'  (*kates-ouä),  umbr. kateramu,  caterahamo  ,catervamini,  congregamini',  doch  s.  unten  unter  1.  A;e^.
22:cymr.  cader  ,Festung'  (nur  in  ON),  air.  cathh^  , Stadt';
23:vielleicht  aisl.  hadda  f.  ,Ring,  Henkel,  Bügel' _(*Äa;>i/)ün  :  catena;  recht unsicher),  wohl  ags.  heador  n.  ,Einschließung,  Gefängnis';
24:ksl.  kotbCh  ,cella,  Nest',  russ.  koty  PL  ,Fischwehr,  Fischzaun',  skr.  kdt, (dial.)  kbtac  ,kleiner  Stall';  dial.  ,Art  Fischfang'  usw.  und  bulg.  kötara, kötora,  kötor  ,Hürde',  skr.  kotar  ,Zaun',  kotär  , Gebiet,  Grenze'  (,*aus Zäunen'),  sloven.  kotdr  ,Bezirk'  (s.  Berneker  386,  588) ;
25:WF.  I  338,  WH.  I  175 ff.,  181  f.
26:2.  kat-  ,Junge  werfen;  Tierjunges'.
27:Lat.  catulus  ,Tierjunges,  bes.  junger  Hund  oder  Katze',  umbr.  katel^ Gen.  katles  , catulus';
28:aisl.  hadna  f.  , junge   Ziege',   mhd.    hatele,   nhd. -Schweiz,    haue   , Ziege';
29:slav.  kotiti  s^  (russ.  kotitbsja  usw.)  , Junge  werfen',  dial.  köthka  ,Lamm', skr.  kot  jBrut',  poln.  wy-kot  , Zicklein'  usw.  (s.  Berneker  589  f.).
30:WP.  I  338  f.,  WH.  I  183.
31:kat-  ,kämpfen',  katu-  :  5af (e)ro-  ,Kampf'.
32:Ai.  sätdyati  ,haut  zusammen,  wirft  nieder';  sdtru-  m.  ,Besieger,  Feind';
33:gall.  catu-  , Kampf  in  GN  Catu-rlx  , Schlachtenkönig',  air.  cath  , Kampf; Truppe,  Schar',  qymr.  cad  ds.,  corn.  cas  m.  ,Kampf';  cymr.  cadr(*kat-ro-) , stark',  abret.  cadr,  mbret.  kazr^  nbret.  kaer  ,schön';  cymr.  cadarn  , stark', bret.  kadarn  ,tapfer';  dazu  auch  nach  Loth  RC  42,  84  f.  cymr.  cadw  m, , Truppe,  Schar'  (^katuo-),  als  Verb  »bewahren,  schützen';  abrit.  Mars Belatu-cadros  enthält  hingegen  die  Wurzel  kad-  , glänzen' ; ■  aisl.  Jiod  f.  ,Streit'  (=  gall.  catu-),  GN  Hgdr,  got.  MN  Theuda-hatha-8, ags.  headu-,  ahd-  hadu-  , Kampf  in  Namen  wie  Hadu-mär,  Hedwig]  mhd. Jiader  ,Zank,  Streit';
34:falls  man  hier  slav.  k-  für  k-  annehmen  darf  (vgl.  oben  S.  18^),  abg. kotora,  russ. -ksl.  kotera  , Streit,  Kampf;
35:möglich   wäre   Heranziehung   des   thrak.  VN   der   IccrgaL,  ^arQO-^evtai]
36:daß  in  gr.  aarlvrj  , Luxuswagen',  adriXla'  nleiäg  tö  äargov,  die  als  phryg. Worte  mit  arm:  sayl  , Wagen'  (arm.-phryg.  *satilia)  zusammenhängen,  die Bed.  des  , Streitwagens'  die  ursprüngliche  sei,  ist  unerweisbar.
37:WP.  I  339,  340,  Vendryes  RC.  43,  246,  M.  Leumann  Hermes  68,  359,
38:1
39:535
40:}caU'  ^erniedrigen^  demütigen;  kau-no-s  Schande,  Schämt
41:Gr.  T^avvöq'  xazög  (ay,Xr]QÖg,  in   letzterer  Bed.  zu  v-alo),  Schulze  KZ.  29
42:270  Anm.  1)  Hes.  und  'Aavoög  (oder  xavgog)'  v.av.6g,  auch   '/.avaqdv'   yiaKÖv
43:Hes.;
44:got.  Jiauns   ^niedrig,  demütigt   (haunjan   ^erniedrigen^),    ahd.    höni    ,ver-
45:achtet,  elend,  niedrig^  (honen  ,schmähen,  höhnen^),  ags.  hean  ^niedrig,  elend,
46:erbärmlich^  (hynan  ,schmähenQ,  ahd.  hönida,  as.  hönda  ,Schande^,  afries.
47:hänetJie  ,Anklage^,  ahd.  höna  ,Hohn^;
48:anord.  häd  {*hawipa-)  n.  ,Spott^,  mhd.  hüren  ,kauern%-
49:lett.    käuns   m.   ,Schmach,   Schande,   Scham^,    käuneties   ,sich   schämen,
50:blöde  sein^,  käuntgs  ,schamhaft,  verschämt,  blöde^; lit.  küviüos,  küvetis  ,sich  schämen'. WP.  I  330,  Feist  249  f.,  Trautmann  122.
51:käu-,  k9U-  ,hauen,  schlagend
52:Lat.  (mit  präsensbildendem  d)  cüdö,  -ere  ,schlagen,  klopfen,  stampfen, prägen^  (wohl  für  *caudö  nach  den  viel  häufigeren  Kompos. ;  vgl.)  caudex, codex  ,Baumstamm,  Klotz;  zu  Schreibtafeln  gespaltenes  Holz,  Notizbuch*^, cödicillus  ,Scheitholz^,  caudica  ,aus  einem  Baumstamm  gemachter  Kahn^, incüs,  -üdis  f.  ,Amboß^;  toch.  A  kot-y  B  kaut-  ,spalten';
53:ahd.  houioan  (Äto),  ags.  heawan  (heow),  aisl.  hqggua  (Jiiö)  ,hauen  (hieb)^ (dazu  als  ,zu  Hauendes^  got.  usw.  hawi  ,Heu'^) ;
54:lit.  kduju,  köviau,  kduti  (*käu{ö)  ,schlagen,  schmieden;  kämpfen^,  kovä ,Kampf',  lett.  nüo-kaut  ,erschlagen,  töten*^,  kava  ,Schlag,  Schicht^  (*Ä:aw-), lit.  küjis  ,Hammer^  =  apr.  cugis  ds.  (abg.  kyjh  ds. ;  lit.  kilgis  ist  aus  küjis nach  kügis  ,Heuhaufen^  umgebildet);
55:abg.  kovQ  (später  ksl.  kujg)  kovati  ,schmieden^  (=  ahd.  homuu),  serb. küjem  (dial.  kbvem)  kbvati  ,schmieden,  prägen;  (ein  Pferd)  beschlagen^, ksl.  kyjb  ,Hammer^  (*kü-io-),  russ.  kuzm , Schmiedearbeit^,  schwundstufig  abg. k^znh  ,List^  (,Ränke  schmieden'^)  usw. ;  toch.  A  ko-^  B  kau-  ,töteii^
56:WP.  I  330  f.,  WH.  I  186,  300  f.,    Trautmann  123.
57:käu-,  keu-,  kü-  ,heulen^;  kauä  ,schreinder  Vogel;  Schallwurzel,  teils  mit anlaut.  kj  teils  mit  k.
58:Ai.  käuti  , schreit^.  Intens,  köküyate  ,schreit,  tönt,  seufzt*  (Gramm.), köka-  m.  ,Eule,  Hund^?  (,schreiend;  heulend^);  kohila-  , Kuckuck^;
59:arm.  kuk  jOTsvay^ög'  (:  lit.  kaukti,  Meillet  Msl.  12,  214;  die  Nichtver- wandlung  des  2.  ä:  zu  5  nach  u  ist  im  Schallworte  kein  Einwand);
60:gr.  xw-xi5-co  ,schreie,  wehklage^  (dissim.  aus  *xi;-xt;-w),  xcüxv^a  ,Wehklage^; xavä^,  -äxog,  ion.  -i^?,  hom.  X7;^,  -Y.6g  f.,  Y/qv^,  -cxog  ,eine  Möwenart^; mit  gebrochener  Reduplikation  (wie  ai.  köka-,  lit.  kaukti,  saukti,  slav. kukati  usw.)  Y.avv.aViag,  Y,avy.iaXogj  y.avy.LdXr,g  Vogelnamen  (Hes.) ;
61:536  f
62:aber  mcymr.  cuan,  cjmv.  cwan,  abret.  couann,  nbret.  kaouan,  dial.  cavan kotian,  kouhen  ds.  (Ernault  RC  36,  206  3)  sind  wohl  onomatopoetiscLe Neubildungen ;
63:lat.  (gall.)  cavannus  ^Nachteule'  (Anthol.  lat.);
64:ahd.  hüiüo  ,Eule^,  hüwila,  hiuwula  ^Nachteule^,  ahd.  hiuwilön  ,jubeln< mhd.  Muweln,  hiulen  ,heulen,  schreien^,  mnd.  hülen,  mengl.  hülen,  engl. howl ;
65:lit.  (s.  oben)  kaukiü,  kaükti,  lett.  käukt  ,heulen,  von  Hunden  oder  Wölfen', lit.  sukükti  jds.j  aufheulen^,  kaukaU  ^eine  Art  WasservogeP,  lett.  kaüka ;,Sturmwind^ ;
66:lit.  kövas  m.  _,Dohle^,  köva  f.  ^Saatkrähe'  (*käuä  =  poln.  kawa)-^
67:russ.  kdvka  ,Froscli^,  dial.  ^Dohle^,  kdvath  ^stark  husten',  klr.  (usw.) kdvka  ,Dohle^,  kavcdty  ^kreischen' ;  ablaut.  (*Ä:ew-)  bulg.  <^dvka,  serb.  ^ävha, öech.  cavka  , Dohle';  aksl.  kuja-jg,  -ti  ,murren';  russ.  kükath  ,murren, mucksen',  serb.  kükati  ,wehklagen'  usw.
68:Mit  -h~f  -h(h)o-:  ai.  kükkubha-  m.  , wilder  Hahn,  Fasan',  gr.  xovxovgpag ,Vogelart'  (spät,  kaum  echt  gr.);  schallnachahmend  sind:  y.i%vßog  wohl ,Nachteule'  (daneben  'Ai%y.aßrjy  yiUv^og  (daraus  lat.  cicuma),  xtxufi/g  ds., KL%7,aßav  ,deren  Schrei'),  lat.  cucuhiö,  -Ire  vom  Schrei  der  Nachteule (Thomas  Stud.  39  nimmt  Hiat  füllendes  h  an);  auch  die  i(Ä)-,Suffixe' der  vorgenannten  könnten  so  aufgekommen  sein.
69:Mit  -g-:  ai.  küjati  ,knurrt,  brummt,  murmelt';  norw.  Tiauke  ,johlen, rufen'.
70:Mit  -p-:  got.  liiufan  , wehklagen*,  anord.  hjüfra  ds.,  ags.  heofan  ds., as.  hiovan,  ahd.  hiofan^  Mob  an  ds.
71:Mit  -r-:  ai.  cdköra-  m.  ,eine  Art  Rebhuhn';  lat.  caurire  ,schreien,  vom brünstigen  Panther';  aksl.  kurz  ,Hahn',  ksl.  kurica  ,Henne';
72:Mit  anlaut.  Palatal:
73:Ai.  süka-  m.  ,Papagei';  arm.  sag  ,Gans'  (*kaua)  =  aksl.  sova  ,Eule' (:  kelt.  cavannus)]  lit.  saukiüj  §aükti  ,schreien,  laut  rufen,  nennen'; russ.  sycb  ,Zwergeule,  Sperlingseule',  cech.  syc  ,Eule'  (^kük-ti-)-,  unsicher aksl.  Surm  ,Geräusch'  (^IcEu-mo-s?  Brugmann  II ^  1,  247).
74:Vgl.  Suolahti  Dt.  Vogelnamen  185  (hier  über  die  Neuschöpfung  ahd. kaha  ,Dohle'  usw. ;  vgl.  lit.  kövas  usw.  ds.).
75:WP.  I  331  f.,  WH.  I  184,  190,  298,  Trautmann  122.
76:kau{9)lä  :  külä  ,Geschwulst;  bes.  Leibschaden,  Leistenbruch'.
```


## [2026-09-06T15:53:15.779Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^434\\|  434  \\|^433\\|^435\" POK_02.txt | head; echo \"---\"; awk 'NR>=1200 && NR<=1400' POK_02.txt | grep -n \"43[0-9]\" | head -20"
}
```


## [2026-09-06T15:53:17.665Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"cakora\\|cakôra\\|cakora-\\|kapiñjala\\|kabk\" IEC.txt | head -20; echo \"== IEC kau\"; grep -n \"^kau-\\|^kāu\\|kauka\\|kaukos\" IEC.txt | head -20"
}
```


### [2026-09-06T15:53:17.724Z] TOOL RESULT

```
1311:433
1332:434  »
1352:435
---
48:lit.  gulbinti  , rühmen,  preisen';  über  gulbas  , Schwan'  s.  S.  431;
67:430
72:'^ghlö-  (wie  in  gr.  xkwQÖg)  tritt  auf  in  ags.  glöm  , Zwielicht,  Dämmerun»* (doch  ist  ö  vor  m  mehrdeutig),  as.  glöian,  ahd.  gluoen  , brennen,  glühen glänzen',  aisl.  glöd  ,Glut,  glühende  Kohle',  ags.  gläd  f.  ,Glut,  Flamme, glühende  Kohle,  Kohle',  afries.  gled  ,Glut,  Brand',  ahd.  gluot  ,Glut, glühende  Kohlen';  aisl.  -glör  n.  , Glanz'  (:  %Io}q6<;),  aisl.  glöra  , funkeln'; s.  auch  unten  S.  433  ghlöu-]  ;;
82:431
99:432
112:433
127:ghlöu-  in  aisl.  glöa  ,glühen,  glänzen,  leuchten',  ags.  glöioan  ,fulminare', aisl.  himinglijbva  , Tochter  Agirs  und  der  Rän'  (Verkörperung  der  Woge); -glö-  f.  , Sonne',  -glöa  f.  ,Mond' ;  s.  auch  oben  S.  430  unter  ghlö-,
133:434  »
153:435
172:436  ^  '^fi
191:437
```


### [2026-09-06T15:53:17.781Z] TOOL RESULT

```
== IEC kau
6868:kauk- (1) ‘skull’, (2) ‘height, pile’, etc. see following entries and cf. kaukos
6869:kaukol-os (1) ‘skull, basin, trough'. WP I, 331. Cf. kaüKos Per. cf, kafce (-ladle" LW in R kovš, id.); Gk. kaukálion ‘vesseľ, kaükalon ('skull'. Ambig. cf. kauK-); Li. káukolis, io, m. and káukole, es, f. ‘skull’; Finn. LW kaukalo “trough?
6870:kaukol- (kauk-) (2) an umbelliferous plant (same as (1)?) Skt. cf. kokam (‘red lotus’ or sim.); Li. kaŭ- kis, io, m. *hedge-parsley'; Gk. cf. kaukalís “an umbel. plant?
6871:kaukol- (3) "a bird’. Cf. kauko, ið, kaukos (1) Skt. kokilah (“Indian cuckoo'; also “mouse, snake, insect'!); Hes. cf. kaukalías (a bird); Li. kauklys ‘siren, hooter’
6872:kaukoros ‘height, hill. Cf. kaukos (2) Li. kaükaras, -à, m. f., id.; cf. (Medic?) Cau- casus, and (Celtic?) placename Cauca (in Spain) and Cauco-liberum (in France).
6876:kaukos (1) ‘shriek, howl, clamour, call", Variant: kāuk- as separate entry, cf. also kauko above. Cf. WP I, 331, 371 & 466. Extn. mng. ‘howler’, etc. Skt. kókah "wolt" beside (variant) kau$ikah ‘owl’; Ir. cuach ‘cuckoo’; Blg. kuk, id. beside kuče ‘dog’; OCS cf. kuctka ‘bitch’; Li. kaükas (‘goblin, mandrake, thunderbolt’ in folklore); kaukýs ʻa raucous bird'; kiáuke ‘jackdaw’; Latv. kaukis (‘bawler; blackcap’ ornith.); cf. (variant) Slovene čuk ‘owl’. (Isophonic: LLat. caucus ‘concubine’ and Alb. kakë- in kakë- zozë ‘salamander’: Latv kaukis, kaukis (2), m. ‘toad’. The Alb. form suggests a prototype *kauko-dieudio)
6877:kaukos (2) ‘high; height, hill hump’. (Variant: kauK-) Skt. (variant) koS$yau, dual no. ‘two glands near horse's heart; Tokh. A koc, B kauc, kaus (&high'; adv. "op: Go. hauhs, OHG hoh, OE heah, ON hár ‘high’ beside OHG houg, MHG houc, ses, G Haug, ON haugr fhill- ock, mound’; Sw. hög ‘high; hill; R küca ‘pile’; Li. kaükas ‘boil, neck-gland of pig’; extn. in kaukaras, kaukure (f hilltop', etc.). A variant arises in Li. káuge 'pile'; Latv. kaudze, id.
6880:kaukos — kaustos, kautos
6902:kaukos, is, à (kauk-) “a raucous bird’. WP I, 33] Skt. kókah (2) ‘red goose, cuckoo’; Hind. koki ‘crow’; Sind. kok, m. ‘cuckoo; frog’; Per. kabg ‘partridge’; Tokh. A cf. kokafi “an un- identified bird”; Gk. kéux, gs kéukos “a gull’ beside kábéx, kaúēx, id.; Sard. coca ‘goose’ beside Sard. (Campid.) coga (^witch', cf. mngs. of Lat. strix); Ir. cuach ‘cuckoo’; W cawci (jackdaw': Hind. koki); Cz. kavka, Pol. kawka “daw”; Srb. cf. (variant) Cavka, id.; Li. kaukys, m. “a shrill bird’; kiauke ‘daw’; Latv. kaukis *blackcap gull'. (A similar onomat. element is present in Hind. kauwa ‘crow, daw? and in Fr. cahouette, id.)
8393:kunkos, à, io “lump, hump, bulge’. Cf. kung-, elc. Alb. (ambig.) kungë, f. id.; (R (ambig.) küca ‘heap, mass, crowd" preferably to kaukos (1), q.v); Li. cf. kunksoti, inf. ‘bulge; huddle together; Latv. cf. kunce, f. (*tadpole', fr.
```


## [2026-09-06T15:53:25.820Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '1325,1355p' POK_02.txt"
}
```


### [2026-09-06T15:53:25.859Z] TOOL RESULT

```
(Zur  Zusammenstellung  dieser  Worte  mit  lit.  zvelgiü,  zvelgti  , blicken' vergleiche  Trautmann  374.)
ghlöu-  in  aisl.  glöa  ,glühen,  glänzen,  leuchten',  ags.  glöioan  ,fulminare', aisl.  himinglijbva  , Tochter  Agirs  und  der  Rän'  (Verkörperung  der  Woge); -glö-  f.  , Sonne',  -glöa  f.  ,Mond' ;  s.  auch  oben  S.  430  unter  ghlö-,
ghiü- :  norw.  dial.  glyma  , finster,  drohend  oder  lauernd  blicken',  aschwed. glüna  ,scheel  blicken',  ostfries.  glümen  ,verdeckt  und  heimlich  nach  etwas sehen  und  lauern';  aisl.  glümr  m.  ^Bär'i
Dazu  s-(s^-)Erweiterungen:
Ir.  gluss  (*ghlustu-)  , Licht,  Helligkeit' ;
aisl.  glys  , Glanz,  Putz',  nisl.  glosa  , strahlen',  mhd.  glosen^  glosten  , glühen, glänzen',  gloste  ,Glut',  mnd.  glüren  , lauern',  engl,  to  glower  , finster  blicken', steir.  gloren  , starren',  norw.  dial.  glyra  , seitwärts  blicken,  schielen,  blinzeln*, aisl.  glyrna  f.  ,Auge',  norw.  glör  ds.
28
434  »
ghlad-  :  meng-l.  glouten,  engl,  to  glout  , starren,  betrübt  oder  miirri aussehen*,  to  gloat  (<; '^^^o^ian)  , hämisch  blicken,  anstarren',  aisl.  ^^ ,grinsen',  mhd.  nhd.  glotzen.
WP.  I  623 f,   624ff.,  WH.  I  473f.,   514,   578  f.,   600,    607  f.,   639, 868,  Trautmann  83f,  88,  364f.,  368,  372,  Persson  Beitr.  170f.,  790ff.,  STßl
2.  ghel-  , schneiden' ?  ?
Ai.    hald-    m.    n.   , Pflug'    (ursprüngl.    ,Ast,    Zweig'?);    hudu-,    hu^a- _  ,Widder'  (*ghldu-) ;
a.vm.  joi  , Pfahl,  Stock'  usw.,  j lern  ,£urche,  pflüge'; gr.    ydlXog    , Priester    der    Kybele,    Verschnittener'    (aus    dem    Phry3 woher  auch  hitt.  iskalla-  ,zerfetzen,  zerreißen',  Iskallis  Name  des  Attis?) daraus  lat.  gallus  ds. ;
acymr.  gylyfn',  mcymr.  geleu,  gelyf  ,Messer,  Dolch'   (Vendrjes  Et!  c( ■    4,  60)  aus  *ghel-mo-  =  ags.  glelm-^
got.  gilpa  L  , Sichel' ;  ags.  gielm  m.  , Garbe' ;  aisl.  ggltr,  galti  ,Ebei gylr,  gylta  ,Sau;  Axt',  ags.  gleite  , junge  Sau',  mnd.  gelte  ,verschnittenj Mutterschwein',  ahd.  galza,  gelza  f.  , verschnittenes  Schwein' ;  ahd.  mh( galt,  a.gs.  gielde,  anord.  geldr,  aschwed.  galder  , keine  Milch  gebend,  ui fruchtbar',  aisl.  gelda  , kastrieren' ;  Schweiz,  galt  auch  ,noch  keine  MiU gebend',  galdvee  =  , Jungvieh'.
lit.  zuolis  , Stück  Holz,  Baumstamm'  [ghöli-). Obige  Gleichungen  durchwegs  unsicher. '      WP.  I  628  f.,  Petersson  Heterokl.  155  f.,  WH.  I  581.
gbelä  ,Wein'??
Ai.  halä  , Branntwein' ; gr.  x^^^Si  "to?  , ungemischter  Wein',    xall-xQrjrog   ds. ;    maked.  '/.dXL&ogi oivog.  ^u^^sglag  Hes. ;
thrak.^/Aßi*  6  olvog  Hes.  (*ghel-). WP.  I  631.    Sehr  zweifelhaft.
gheldh-  , begehren';  nur  ar.  und  slav.
Ai.  gfd^yati  , ist  gierig,  verlangt  heftig'  (=  serb.-ksl.  zhzdg),  grdhnu-1^ .gierig',  gfdhra-h  ,gierig;  Geier',  gardha-h  (=  aksl.  glad^)  m.  ,Begierde*, av.  gdrdda-  ds. ;
slav.  *zlldiö  , verlange'  in:  «
serb.-ksl.  zhzdg,  zhdeti  ,desiderare',  skr.  züdim,  züdjeti  ,verlangen,  sich| sehnen  nach' ;
s\2iY.  *galda-  m.  ,Hunger'  in:
aksl.  glad^,  skr.  gläd  (Gen.  gläda);  cech.  hlad\  russ.  göiod  (Gen.  göloda).
WP.  I  633,  Trautmann  87  f.
I
435
crhel{ß)S^'  Metallbezeichnung  (»Bi'onze»  Kupfer,  Eisen')?
Aksl.  *ieZezo  in  zeUz{h)m  ^eisern*,  skr.  £eljezo,  russ.  ^eUzo  , Eisen* ;
lit.  gelezis  und  zem.  gelBs  (davon  gelezlnis,  gelzinis  , eisern'),  lett.  dzelzs, ostlett.  dzelezs,  apr.  gelso  f.  , Eisen' ;
```


## [2026-09-06T15:53:27.221Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=6820 && NR<=6910' IEC.txt | grep -nE \"^[0-9]{2,4}$|^ *[0-9]{2,4} *$\" ; echo \"--- context markers\"; sed -n '6860,6905p' IEC.txt | cut -c1-160"
}
```


### [2026-09-06T15:53:28.955Z] TOOL RESULT

```
13:20
14:25
15:30
16:35
17:40
18:45
19:478
30:479
38:20
39:25
40:30
41:33
42:40
43:45
44:480
55:481
62:15
63:20
64:25
65:30
66:35
67:40
68:45
69:482
79:483
87:20
88:25
89:30
90:33
91:40
--- context markers
33
40
45
480
rys, id.
kaud- (form of kauo, küd-, q.v.) ‘strike’ Tokh. A kot-, B kaut- “split, eut: Lat. cauda “tail beside cüdo, Gre ((forge', fr. the cpd. forms?); cf. als
kaudst- (extn. of kaud-, q. v.) ‘cutting down, cut, section’ Skt. cf. kosthah ‘bowels’; ON haust, Sw. höst ‘harvest’; Li. kaustyti, v. ‘forge’.
kaug- “shout”, etc.; kauk- ‘raucous bird’, see kāuk-
kauk- (1) ‘skull’, (2) ‘height, pile’, etc. see following entries and cf. kaukos
kaukol-os (1) ‘skull, basin, trough'. WP I, 331. Cf. kaüKos Per. cf, kafce (-ladle" LW in R kovš, id.); Gk. kaukálion ‘vesseľ, kaükalon ('skull'. Ambig
kaukol- (kauk-) (2) an umbelliferous plant (same as (1)?) Skt. cf. kokam (‘red lotus’ or sim.); Li. kaŭ- kis, io, m. *hedge-parsley'; Gk. cf. kaukalís “
kaukol- (3) "a bird’. Cf. kauko, ið, kaukos (1) Skt. kokilah (“Indian cuckoo'; also “mouse, snake, insect'!); Hes. cf. kaukalías (a bird); Li. kauklys �
kaukoros ‘height, hill. Cf. kaukos (2) Li. kaükaras, -à, m. f., id.; cf. (Medic?) Cau- casus, and (Celtic?) placename Cauca (in Spain) and Cauco-liberum (in
kauko, ið ‘shriek’. Cf. Kauk- and next. Cf. WP I, 331, 371 & 466 Skt. koCami, id.; Arm. kawSem, id.; Tokh. B cf. sauk- ‘call, name”; Gk. kaukízomai �
481
kaukiù, ^ti ‘hoot, how" beside (variant) šau- Ku, “ti ‘shout’; Latv. kaucu, kaukt, as Li. beside saukt ‘shout’; Cz. cf. s-kucet ‘howl. Variants
kaukos (1) ‘shriek, howl, clamour, call", Variant: kāuk- as separate entry, cf. also kauko above. Cf. WP I, 331, 371 & 466. Extn. mng. ‘howler’, etc. Skt
kaukos (2) ‘high; height, hill hump’. (Variant: kauK-) Skt. (variant) koS$yau, dual no. ‘two glands near horse's heart; Tokh. A koc, B kauc, kaus (&high';
kauks-, see kauko, ið
kauKos, à, io “shell, skull, bowl, cup’. Cf. kaukolos, etc. WP II, 548-551 Skt. kosah “shell, cup, pail, box, cask’; kośam, id.; cf. koSika, kausika �
kaukos — kaustos, kautos
15
20
25
30
35
40
45
482
Latv. kauss ‘skull, bow; Finn. LW kauha ‘ladle’; Est. LW kauss ‘bowl’. (Note: the mak- ing of cups and bowls from human skulls is mentioned by Herodot
kaulos, à, is “stem, stalk, stick, penis’. WP I, 332 Skt. korah ‘joint’; kaulah, adj. “of the family’; Hitt. cf. külas “an undefined costly obje
(kaunā, iə, see kounā)
kaunos, ios (1) ‘base, vile; baseness, shame’. WP I, 330 Tokh. A safíi, B sono ‘shame; hatred’; Ir. cuan ‘deceit’; Go. hauns, adj. ‘humble’; OH
kaunos, à (2) (?) “reedy place, marsh’. (Same as (1)?) Gk. cf. Kaunos (a town in Caria); W cawn ‘reeds’; Br. kaon 'mill-race'; Li. Kaunas
kaurio ‘howl Lat. caurio, ire, id.; Slovene, cf. kurjak "wolt
kauros ‘cock’ Alb. kar ‘penis’; OCS kurü ‘cockerel’; Cz. kur, id., kura "hen"
kaust- ‘bush’ (koupst-?) Ger. Hauste, wm. “pile; dolly-sheaf; OCS kustü, R kust ‘shrub’
kaustos, kautos ‘struck, forged’. Cf. kauuo. (For Gk. kaustós, see Kausto-) Pol. kuty ‘shod, of horses’; OCS kuštọ, ku-
483
titi, Cz. kutit “fashion, contrive’; Cz. cf. po- kuta (‘penalty’: Ukr. = 'penance"); Srb. cf. kucam ‘hit’; Li. cf. káustyti ‘forge, shoe a horse�
kăutos (2), pp. type to kăueið, q.v. (vowel ambig. *koutos also possible) Lat. cautum; ON háiór (pp. of heyja “hold, Observe, manage"); Latv. cf. kautrs 
káueio, kăuið "watch, observe, manage’. Cf. kouos. (The diphthong is either *-au- or *-ou-, represented for convenience as *-áu-). WP I, 369 Skt. cf. kavi
kaukos, is, à (kauk-) “a raucous bird’. WP I, 33] Skt. kókah (2) ‘red goose, cuckoo’; Hind. koki ‘crow’; Sind. kok, m. ‘cuckoo; frog’; Per. ka
káulos, à (koul-, kül-) ‘scrotal hernia’. WP I, 333 Gk. këlë (Doric: -à-) ‘hernia’; Lat. cf. coleus, culeus ‘scrotum’; OHG hola; OE heala 'scr
käng, ið (kou-, kāu-, kü-) (1) “strike, hew’. WP I, 330. Gk. etc. ambig. Cf. Káu- Av. cf. fra-kava ‘fight’; apa-kavo ‘warrior’; Per. kavam, inf
káutos — kek- (keks-)
```


## [2026-09-06T15:53:43.069Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"hay\\b\" AHD_watkins1985.txt | head -20; echo \"== kau\"; grep -n \"^kau\\|^kāu\\|kau-\\.\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-06T15:53:43.124Z] TOOL RESULT

```
377:dapper, heavy, strong; later quick, nimble: DAPPER. [Pok. dheb- 239.] dhegvh-. To burn, warm. Suffixed o-grade form *dhogvh- eye- in Latin fovére, to warm, cherish, foment (> fomen- tare, to foment, and fomes, tinder): FOMENT, FOMITE. [Pok. dhegth- 240.] dh@(i)-. To suck. Contracted from *dheoa(i)-. 1. Suffixed reduced form *dhé-mnd- in Latin fémina, woman (< “she who suckles”): FEMALE, FEMININE; EFFEMINATE. 2. Suf- fixed reduced form *dhé-to- in Latin fétus, pregnancy, childbearing, offspring: FAWN, (FETAL), FETUS; EFFETE, (FETICIDE), SUPERFETATE. 3. Suffixed reduced form *dhé-kundo- in Latin fécundus, fruitful: FECUND. 4. Suf- fixed reduced form *dhé-no- in Latin fénum, faenum, hay ( < “produce”): FENNEL, FINOCHIO; (FENUGREEK), SAIN- FOIN. 5. Perhaps suffixed zero-grade form *dhi-lyo- (< *dhia-lyo-) in Latin filius, son, and filia, daughter (but these are equally possibly from the root bheue-): FILIAL, FILIATE; AFFILIATE, HIDALGO. 6. Suffixed reduced form *dhé-lo- in Latin fél(are, to suck: FELLATIO. 7. Suffixed reduced form *dhé-l-ik- in Latin félix, fruitful, fertile, lucky, happy: FELICITATE, FELICITY; FELICIFIC, INFELIC- Ty. 8. Suffixed reduced form *dhé-ld- in Greek thélé, nipple: ENDOTHELIUM, EPITHELIUM, (MESOTHELIUM). 9. Suffixed reduced form *dhé-l-u- in Greek thélus, female: THEELIN. [Pok. dhéi)- 241.] dheia-. To see, look. Variant form *dhyd- (< *dhyag-) in: a. suffixed form *dhyd-mn in Greek sémeion and séma (stem sémat-), sign: SEMANTIC, SEMATIC; SEMAPHORE, SEMASIOLOGY, SEMEME, SEMIOLOGY, SEMIOTIC; b, San- skrit dhydti, he meditates (< “he observes mentally”): ZEN BUDDHISM. [Pok. dheis- 243.] dheigh-. To form, build. 1. Germanic *daigjén in Old English d%ge, bread kneader: DAIRY. 2. Germanic *-dig- in Old English compound Aléfdige, mistress of a house- hold (< “bread kneader”; Al#f, bread, loaf): LADY. 3. Ex- tended o-grade form *dhoigho- in Germanic *daigaz in: a. Old English dag, dough: pouGH; b. Old High German teic, dough: TEIGLACH. 4. Suffixed zero-grade form *dhigh-ird, in Latin figira, form, shape (< “result of kneading”): FIGURE; CONFIGURATION, DISFIGURE, PRE- FIGURE, TRANSFIGURE. 5. Nasalized zero-grade form *dhi-n-gh- in Latin fingere, to shape: (FAINT), FEIGN, (FEINT), FICTILE, FICTION, FIGMENT; EFFIGY. 6. Nasal- ized zero-grade form *dhi-n-g(h)- in Greek thinganein, to touch: THIGMOTAXIS, THIXOTROPY. 7. Suffixed o-grade form *dhoigh-o- in Avestan daéza-, wall (originally made of clay or mud bricks): PARADISE. [Pok. dheigh- 244.] dhel-. A hollow. 1. Germanic *daljé in Old English dell, valley: DELL. 2. Germanic *dalam in Old English del, valley: DALE. 3. Germanic *del- in Old Norse dzla, wooden gutter on a ship: DALLES. [Pok. 1. dhel- 245.] dhelbh-. To dig, excavate. Germanic *de/ban in Old English de/fan, to dig: DELVE. [Pok. dhelbh- 246.] dhembh-. To bury. Suffixed zero-grade form *dhmbh-o- in Greek taphos (< *thaphos), tomb: CENOTAPH, EPI- TAPH. [Pok. (dhembh-), dhmbh- 248.] dhen-'. To run, flow. Suffixed o-grade form *dhon-ti- in Latin fons (stem font-), spring, fountain: FONT!, FOUN- TaIN. [Pok. 1. dhen- 249.] dhen-2. Palm of the hand. Suffixed form *dhen-r in Greek thenar, palm of the hand: THENAR. [Pok. 2. dhen- 249.] dher-1. To make muddy; darkness. 1. Suffixed form *dher-g- in Germanic *derk- in Old English deorc, dark: DARK. 2. Suffixed zero-grade form *dhr-egh- in: a. Ger- manic ‘suffixed form *drah-sta- in Old English drés, dregs: pross; b. Germanic *dragj6 in Old Norse dregg, dregs: DREGS. 3. Suffixed extended zero-grade form *dhro-bh- in Germanic *drab- in: a. Old English dreflian, to drivel: DRIVEL; b. probably Low German drabbelen, to paddle in water or mire, draggle, akin to the Low German source of Middle English drabelen, to draggle: DRABBLE; C. Middle Irish drab, dregs, probably akin to the Celtic source of DRAB2. 4. Suffixed extended
591:kau-2, To hew, strike. 1. Germanic *hawwan in: a. Old English héawan, to hew: HEW; b. Old Norse héggva, to cut: HAGGLE; c. Old ‘French hove, a hoe: HOE. 2. Ger- manic *hawwé6 in Old Norse hégg, a gap, a cutting blow, akin to the source of HAG?. 3. Germanic *haujam in Old English hieg, hay, cut grass: HAY. 4. Suffixed form *kau-do- in Latin ciidere (< *caudere), to strike, beat: incus. [Pok. kdu-, 535.]
1579:HAG2 kau-2 HAGGARD kagh- HAGGLE kau-2 HAGIO- yag- HAIL! kaghlo- HAIL? kailo- HAKE keg- HALBERD bhardha, kelp- HALE! kailo- HALE? kele-2 HALF skel-1 HALIBUT bhau- HALL kel-2 HALLOW kailo- HALO-  Sal-1 HALT! kel-3 HALT? kel-1 HALTER! kelp- HALTER? § sel-4 HAM konemo- HAMADRYAD deru, sem-! HAME_ tkei- HAMLET tkei- HAMMER ak- HANDIWORK kom HANDSEL sel-3 HANG konk- HANKER konk- HANUMAN genu-2 HAP kob- HAPLESS kob- HAPLOID pel-3, sem-1 HAPPEN kob- HAPPY kob- HARANGUE koro- HARBINGER koro- HARBOR koro- HARD kar-1 HARDS_ kes-! HARDY! = kar-1 HARE kas- HARM kormo- HARMONY ar- HARNESS _nes-1 HARPOON  serp-1 HARPSICHORD ghere- HARQUEBUS keg- HARRY koro- HART ker-1 HARTEBEEST ker-1 HARUSPEX ghere- HARVEST kerp- HASH! =skep- HASLET ghasto- HASTATE ghasto- HAT kadh- HATCHET skep- HATE kad- HATRED ar-, kad- HAUBERK kWel-1 HAUGH kel-2 HAUGHTY al-3 HAUL kele-2 HAULM kolem- HAUNT tkei- HAUSTELLUM aus-2 HAUSTORIUM aus-2 HAUTBOY al-3, busk- HAVE kap- HAVEN kap- HAW2 kagh- HAWK! kap- HAWKER keu-2 HAWSE kWel-1 HAWSER al-3 HAY kau-2 HAZEL koselo- HE! ko-
== kau
590:kau-'. To howl (imitative). 1. Reduplicated suffixed form *ka-kau-ro- in Sanskrit cakorah, partridge: CHUKAR. 2. Reduplicated form *k6-kii-o- in Greek kdkuein, to wail, lament: Cocytus. [Pok. kau- 535.]
591:kau-2, To hew, strike. 1. Germanic *hawwan in: a. Old English héawan, to hew: HEW; b. Old Norse héggva, to cut: HAGGLE; c. Old ‘French hove, a hoe: HOE. 2. Ger- manic *hawwé6 in Old Norse hégg, a gap, a cutting blow, akin to the source of HAG?. 3. Germanic *haujam in Old English hieg, hay, cut grass: HAY. 4. Suffixed form *kau-do- in Latin ciidere (< *caudere), to strike, beat: incus. [Pok. kdu-, 535.]
592:kaul-. Stalk, stem. Latin caulis, stalk, stem, cab- bage-stalk, cabbage: CAULICLE, CAULINE, COLE, KALE; AMPLEXICAUL, CAULESCENT, CAULIFLOWER, COLCAN- NON, COLESLAW, KAILYARD SCHOOL, KOHLRABI. [Pok. kau-l- 537.)
```


## [2026-09-06T15:53:43.951Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '6902p' IEC.txt; echo \"=== SYN 290\"; grep -n \"kill\\|slay\" SYN.txt | sed -n '1,5p'"
}
```


### [2026-09-06T15:53:44.010Z] TOOL RESULT

```
kaukos, is, à (kauk-) “a raucous bird’. WP I, 33] Skt. kókah (2) ‘red goose, cuckoo’; Hind. koki ‘crow’; Sind. kok, m. ‘cuckoo; frog’; Per. kabg ‘partridge’; Tokh. A cf. kokafi “an un- identified bird”; Gk. kéux, gs kéukos “a gull’ beside kábéx, kaúēx, id.; Sard. coca ‘goose’ beside Sard. (Campid.) coga (^witch', cf. mngs. of Lat. strix); Ir. cuach ‘cuckoo’; W cawci (jackdaw': Hind. koki); Cz. kavka, Pol. kawka “daw”; Srb. cf. (variant) Cavka, id.; Li. kaukys, m. “a shrill bird’; kiauke ‘daw’; Latv. kaukis *blackcap gull'. (A similar onomat. element is present in Hind. kauwa ‘crow, daw? and in Fr. cahouette, id.)
=== SYN 290
3906:7. Skt. vadhri- ‘castrated’ (cf. Grk. pis * roulas xpis and pis * orddwv, Toputas, evvodxos, Hesych.) fr. vadh- ‘strike, slay’ : Grk. &féw ‘thrust’, etc., IE *wedh-. Walde-P. 1.254 f.
6059:Grk. cgay or pl. cdayat (both in Aristot.) ‘throat’, this prob. the earliest meaning of the word, whence o¢étw ‘cut the throat, slay’ (cf. Lat. iugulare ‘slay’ fr. cugulum ‘throat’) and the re- sulting common use of c¢ay as ‘slaugh- ter’. No accepted etym., but prob. con- nected, by a series of parallel root-forms, with o¢yt, Dor. opat (gen. -xés) ‘wasp’, o¢yv, Dor. cpav ‘wedge’, odiyyw ‘bind tight, constrict’, all with common notion of ‘narrow’. Cf. Dan. strube, etc., below, 4. (Different combinations in Walde-P, 2.651-53, 658.)
7384:6. Lett. ndve ‘death’: navet ‘kill’, ChSI. navi, Goth. naus, ON nar ‘corpse’ (4.77), Lith. novytt ‘torture, kill’, ChSL., Boh. naviti ‘tire’, ete. Walde-P. 2.316. Mithl-Endz. 2.703 f.
7390:1480 f. Barth. 1146. 4.76 KILL Grk. (ao) xrelvw (éxredvov) Goth. usgiman, -daupjan, Lith. uzmusti, Zudyli NG ss akordvw afslahan Lett. nuokaut, nuon aver Lat. _interficere, occidere, ON deyda, drepa, sla, vega ChSl.  ubiti, umoritz necare Dan. draebe SCr.  ubiti, usmrtjt; It. uccidere, ammazzare Sw. déda (drapa) Boh. —zabiti, usmrlitt Fy. tuer OE cwellan, sléan, (a)dj- Pol. —zabié, uSmiercig Sp. matar dan Russ. ubit’ Rum. omort, ucide ME  sley, culle, quelle Skt. han-, vadh- Ir. marbaim, gonim, or- NE kill (slay) Av. jan-, fra-kus-, maraé., gim Du. dooden etc. NIr. — marbhaim OHG  totan, (ir)slahan W. lladd MHG iaten, (er)slan Br. laza, NHG téten, erschlagen, um-
7392:Words for ‘kill’ are often originally the same as, or derived from, words for ‘strike’ (9.21). Frequently, as in Balto- Slavic, the perfective form of ‘strike’ is ‘kill’. Some are derivatives of words for ‘dead, death’, or causatives of those for ‘die’. Some are originally euphemistic expressions from such diverse sources as ‘put in darkness’, ‘deprive of (life)’, ‘ex- tinguish’, etc.
```


## [2026-09-06T15:53:55.795Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"fra-kus\\|frakus\\|fra-kuš\" SYN.txt | head; echo \"== page markers near 7384\"; awk 'NR>=7350 && NR<=7420' SYN.txt | grep -nE \"^ *(28[0-9]|29[0-9]) *$|29[0-9] \" | head"
}
```


## [2026-09-06T15:53:56.704Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"SNS\" ../refs_online.json >/dev/null; grep -n -i \"kus\\|kôš\\|kws\" SNS_pages.txt | head -20"
}
```


### [2026-09-06T15:53:57.416Z] TOOL RESULT

```
7390:1480 f. Barth. 1146. 4.76 KILL Grk. (ao) xrelvw (éxredvov) Goth. usgiman, -daupjan, Lith. uzmusti, Zudyli NG ss akordvw afslahan Lett. nuokaut, nuon aver Lat. _interficere, occidere, ON deyda, drepa, sla, vega ChSl.  ubiti, umoritz necare Dan. draebe SCr.  ubiti, usmrtjt; It. uccidere, ammazzare Sw. déda (drapa) Boh. —zabiti, usmrlitt Fy. tuer OE cwellan, sléan, (a)dj- Pol. —zabié, uSmiercig Sp. matar dan Russ. ubit’ Rum. omort, ucide ME  sley, culle, quelle Skt. han-, vadh- Ir. marbaim, gonim, or- NE kill (slay) Av. jan-, fra-kus-, maraé., gim Du. dooden etc. NIr. — marbhaim OHG  totan, (ir)slahan W. lladd MHG iaten, (er)slan Br. laza, NHG téten, erschlagen, um-
7450:Av. fra-kus- (only once, janaii; frat kugaitz, but cf. NPers. kustan ‘kill’) prob. : Skt. kus- ‘tear, etc,’, further connections dub. Walde-P. 1.331. Barth 431. ;
== page markers near 7384
39:288
```


### [2026-09-06T15:53:59.030Z] TOOL RESULT

```
2293:          akustan
2302:                                                          -»A>'>j t <        o*/ :a+kustan                            :j'.o=*o T
5125:       OkUSti^ j-u^c^il^ <Ai>»»^:pahrSzend:
7274:                     ^t^^^U^^fc^^^from kusks.                                                 •   T/ir-^ .JLijjii^            rpanzdah salag:                       i5^-o» -*oCef«J                           lo
8674:                                                                                                                                •V^^CWir.Wan. II,          57)    kws
8738:     Y-f-^-Y/f^ -aa-YT—Tr/T^-'jjt «w-l> <**>b *o-S :kust: W*
8739:        *&/f<S .jl+t^yl+t :kust ud kust:     »«»»3    v*»»3                       i
8742:             -?-Y/M -afc-Yf/Y^ .^b-.^**- :kust-5: jW^'J                                                            »V«^16-lWT^/T^Ui^,             472) kataka-           lfci
8746:                •YY-fa/Y^ .^i> .wol> .4i-S .c*-f :kustag:
8753:                                                                           *>».$                    J >j*   l   /-^<o L^^oU^ j45 j-ji. a*, yS .ji^S :kustlg:
8763:                                                                                                                      1Y/TT^    (^j-j'j :<i) Alif.jliS;              :kusad:          **JU\S
8769:                                                                                                                                                               .*i^S.cuiS:kust:           Kju»J
8771:         **oM9^ho \&) .UjK.U^tkunisnan: ««M»3                                                  kusnati,              ^kOs  L kusaiti, /kaos-
8774:                                                                                                     i^j'3>»J£i v^i^^l^^lkwst, kws :^i (GtfP£                                        191)
8777:                                                                                                                                       A/\o>S              .jLiS:kustar:             i*K«jij
11037:                                  .cA :kust: NKSWN,            t:    y»:                                    O^'^r!^: asnavisn:                    C SMHN, In: >>   :
11042:     L^^JaUiOtotlW*. 3n$. p- 154>kwst, kwl                                    :       ^
14969:                                Spas/apas 12/9-10    kusnati 218/6                     ch3ya 174/21
15281:                                                              kusaiti 218/6            x v a5tvada0a 78/12
15451:kws/kwst 218/7-277/15            f
```


## [2026-09-06T15:54:14.661Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=7386 && NR<=7460' SYN.txt | grep -nE \"^ *(28[5-9]|29[0-5]) *$\"; echo \"--- SNS pdf page tags\"; awk 'NR<=8790' SNS_pages.txt | grep -n \"\\[pdf page\" | tail -5; echo \"--- around 8771\"; sed -n '8765,8780p' SNS_pages.txt | cut -c1-200"
}
```


## [2026-09-06T15:54:15.774Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"kāu-\\|kau-\\|kus-\\|keu-s\" incoming/WLD/WLD_Bd1_pages.txt | sed -n '1,40p' | cut -c1-200"
}
```


### [2026-09-06T15:54:16.167Z] TOOL RESULT

```
3:288
59:290
--- SNS pdf page tags
--- around 8771




                                                                                                                                                               .*i^S.cuiS:kust:           Kju»J
     (
         **oM9^ho \&) .UjK.U^tkunisnan: ««M»3                                                  kusnati,              ^kOs  L kusaiti, /kaos-
                                                                                                                                  :                                              :;i >t-
                                                                                                :
                                                                                                     i^j'3>»J£i v^i^^l^^lkwst, kws :^i (GtfP£                                        191)
                                                                                                T/U^ .^=— lAiijjB-^^^bMiiyjj (Junker. 2)                                     WWPJ1
X^/lo^.(     -*j«0"3   «K» '.^) ><?>£                   :kunisnIh:-*WJM 3
                                                                                                                                       A/\o>S              .jLiS:kustar:             i*K«jij
                                                   .^:kunSh:                  <# *tt
                                                                  ,   **- |B
          .T/U*   -^ifM*** :be kuneh: W*                                                                                                                                •j£:kfir:            >y
```


### [2026-09-06T15:54:16.211Z] TOOL RESULT

```
5475:Haken, Biegung zwischen Brust und Hufte“, dnkus- n. „Biegung, Ivriim-
31225:                                                                         kau-, keu-,                  ku                                                        331
31241:Hochst unsicher bes. wegen der abweichenden Bed. von ai. kahiti kus-                                                                                        ,
31247:kau-, keu-, ku-                         = Schalhvz., teils mit                                   q.    teils mit k.
35135:376                                       qeu-   — ken-,   (:   kau-, ku-)
35203:keu-        (:   kau-, ku-) ,,anziinden, verbrennen'               1
35675:   Av. cakus- n. „Wurfhammer, Wurfaxt", np. cakus „IIammer“ (s. Bar-
37660:kernel ,,Giirtel“ (aber wohl niclit katakanl „Schmuck mit Glockchen“, kau-
50564:                               s. u. kau- Schallwort).
52577:„Kase im ersten Zustand ‘, kur *kura -) ,,ds., gcronnene Milch k0yr (* kau-              (
```


## [2026-09-06T15:54:20.684Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '31200,31270p' incoming/WLD/WLD_Bd1_pages.txt | cut -c1-230"
}
```


### [2026-09-06T15:54:20.747Z] TOOL RESULT

```
 lett. niio-kaut „erschlagen,                toten“, kava ,,Schicht“, lit. kiijis „Hammer“                                  = apr.
cugis ds. (abg. kyjb ds.             aus kujis nach kiigis ..Heuhaufen"
                                       ;
                                            lit.   laigis       ist

umgebildet, Trautmann Apr. 364; Ficks KZ. 42, 288 Yergleich mit gr. xvfirj-
hg       fxdyaiQa, ajuEivovde              neXexog,            eg    xdgjiovg        xaxaftakkovai Hes.                scheitert
fibrigens auch daran, das                    -?<</“-      gr. -vy-       ergeben hatte);
      abg.kora (spater ksl. kujq) kovati ., schmieden ', serb. kujem ( kbvUm )             1




kovati „schmieden,    pragen; (ein Pferd; beschlagen, ksl. kyjb ..Hammer 1 ,
r.    kuzm „Sehmiedearbeit a , abg. kbzm ..List (..Ranke schmieden") usw.       -1




(s.    Berneker 592 f.j.
                      :                                                                                                                                               ;




                                                                         kau-, keu-,                  ku                                                        331


   Z. B. Zupitza Gutt. 122 m. Lit. (zu weitgehenden Yerkniipfungen bei
Johansson IF. 19, 125f.).
   Zum Wzansatz quit- s. Brugmann IF. 6, 99 anders Hirt Abl. 102 (qoucZ-).                                   :



  1st av. fra-kusaiti „erschlagt, tcitet", np. kuitun „toten eine s-Erw.?
                                                                                                                                        -
                                                                                                                                            ‘




Hochst unsicher bes. wegen der abweichenden Bed. von ai. kahiti kus-                                                                                        ,


nati „reifit, zerrt, zwickt, knetetb


kau-, keu-, ku-                         = Schalhvz., teils mit                                   q.    teils mit k.

   Ai. kduti „schreit“, Intens. kokilyate ,,schreit, tont, seufzt“, koka- ,,Gans;
Wolf    -1                                                        --
                                                            s. qtiqu-); arm.
                 (,,schreiend; heulend '; Zsfall mit koka- ..Kuckuek",
kuk     ..GTtivay u6g‘'                     12,214; die Nichtverwandlung
                                            (: lit.      kaiikii, Meillet Msl.
des 2. k zu s nach it. beanstandet von Pedersen KZ. 39, 3S4, ist im Schall-
worte kein Einwand eine Gdf. qoq - wil'd dureh y.wxvcn nicht gestiitzt)
                                                    ;



                          wehklage‘‘ (diss. aus *y.v-y.v-to), xurxvtia „Weh-
   gr. xco-xv-cn ,,schreie,
klage '; xava£, -axog, jon. ->;f, hom. xyg, -yog f., xiji'i, -vy.og „ein Meer-
        --



vogel, wahrscheinlich Sula bassana L. ‘, mit gebroehener Bed. oder for-                      -
```


## [2026-09-06T15:54:44.933Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"kuš\\|kaoš\\|kuša\" BRT.txt | head -30"
}
```


### [2026-09-06T15:54:44.981Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T15:54:46.159Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"θβaxš\\|thwaxsh\\|Ppaxs\\|0paxs\" BRT.txt | head -10; echo \"== CHEUNG thwaxsh\"; grep -n \"θβaxš\\|\\*θβaxš\" CHEUNG.txt | head -10"
}
```


### [2026-09-06T15:54:46.228Z] TOOL RESULT

```
== CHEUNG thwaxsh
```


## [2026-09-06T15:54:49.383Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; wc -l BRT.txt; grep -n \"kus\" BRT.txt | head -20"
}
```


### [2026-09-06T15:54:49.440Z] TOOL RESULT

```
30724 BRT.txt
2075:Göttingen  1S93. (A)BucAiGKE  ReLV£d.:  I.a  Religion  vjdique  d.'a:piii  les  hymnes  du  Rig-Veda.     Paris  1878  ff. Bgm.;  KBkusiuiin. Grdi.:  Grundriis  der  vergleichenden  Grammatik  der  indogermanischen  Sprachen.    Strassbu^
2190:A.  {in  AS..  AD.,  AP.):  Akkusati t(us).  |  air.:  altirisch.
2191:A-  (in  3SPfA.  usw.):  Aktivfum).  |Akk.:  Akkusativ(us).
3053:KompA.;  Ableit.  —  ai.  aghä-  Adj.:  n.  — iEl  vgl.  SÖITERI.IN  IF.  4-  92-  —  Pu-i  '■«/, vaiak,  (meiEl)  vattat.  —  D  Vgl.  iSt,  Lxndner Festgrass  Roth  214-  Pü-:  "pi"-  ä  oj:"  . .  äii  i vallar  lamaitän  rast/,  erl. ;  i  taarkusän  gmi'il\ S.  zu  mahrküSa-.  —  2)  Hds,  ayjwi.
3507:Sa. :  apafivatvam,  apajaiah.  —  »)  Pü.  verwendet das  Wort,  als  wäre  es  mp.  Y.  46.  4q  wird fröt  muri  bavel  mit  kus  i^gaytht  bavet,  Y.  41 flön  Aar  ti  amii  Ioh  m  yän  bavät  mit  ku  man apagayihi  mä  bavät  erläutert;  s.  noch  jUay- No.  1,
4022:•  j.  afnah'vant-   Adj.   'reich   an   Habe,  j  •  j.  a-fra'tatkvah-"  Adj.  (fem,  •■iat.kusi-)
4024:—  "ha/sne  {sA.)  *afnat»ukh  F.  2C  \aAmät  kisipnla..'kusisi^Vi.)  hamaya gätvif
4219:—  ä^a  asSmcll .  .  damals  sannt  vTmruyi yä^ä  "näil  vySmrvUä..  sardkustrS^^ .  .'v\r
5464:Vgl.  ari^a-.  —  Pü. :  hal  kusl  i  ddsin.
6090:rMtlsbTs!  dansaia  urväzä  Y.30,  i;  —  jyS  tr' päl  darfsat  (sd.)  'sa^a  Y.  J2.  13;  —  at m  mit  äais  (sd.)  -Am  Y.  4y.  i  o  ;  —  Hyalins möi  tnraos  's?m  JasB  fräxihml  (sA)  Y. 43.^2;  —  alilye  mos  -sä  (als  Subj.)^ syazäuj (sd.)  Y,_y4.9j  a)  neben  AAtira- Mazdäh:  frS  va  fratsyS  ptazää  'Ifmcä mrsiu (sd.)  Y.4i}.6;  —  iä  uxoa  *mamySus mahyä  niasds  'Säicä  yüstnaibyä  gfntl  Y. ^2.9 ;  —  at  tBi  myatdim  ahurä  .  .  'säila dämä  (sd.)  Y.J^.3;  —  %wa/i»tT  vS  masdä xsa^rSi  °iäicä  sSnghS  viäqnt  (sd.)  Y.  ja. 6;  —  at  räiam  (sd.)  zarakustrB..  daäaitf .  .matdsi.  .°/3i\.J J.  14;  —  ahurS..°sä hazaosS  tnasda  Y.sg.j;  —  .  yim  'üt  vahiitS hasaoltm    ahur^m  yäsä   (sd.)  .  .  Y..  28.  8 ;
6219:taM    tva    itsit    .  ,    tt/rqm    'yqm    n3it    .  . fästryqm    HSit  pu%reistlm     "keiner    von denen,   die  nicht  essen,  ist  tüchtig  die  .  . Werke  des  Aia  zu  verrichten  noch  . .  Land- b2u  zu  treiben  .  .  noch  in  den  Besitz  von Söhnen  zu  gelangen"  V._j, 33').        a)  mit einer    (akkus.)     Massbestimmung:     tatui.- masd  (sd.)  xl  *altqmat  'yam  *pafre  yö  . . P.  18.         3)  'Erwerb  des  (höchsten)  An- rechts, Anspruch  auf  das  Paradies':  imqm aifkvyqmca  (sd.)  *°j'fl«('a*' Y._J.4; — yqm aiai'a    vaauhlm    °yqm    vaioa    tarn    drvA K'i'jvä  "welchen  guten  Anspruch  der  A^a- gläubige    kennt   (sva.  besitzt),   damit  ist der  2?n^läubige  unbekannt"  Vr.  22.3. Zum  Praes.  3 1  asaya-,  —  Pü. :  ahräiih  (Sü. :  puri- jralä],  erl.  (zu  Y.  3):    iär  u  karpai  .  .  hamäi kvaim.    —    ')  Vgl.  Vyt.  //    unler    asaya-.  — '\  NA.  aiyqtn ;  s.  aber  Nir.
7223:—  V3r>-ir(^imn  . .  ya  . .  aca  paraca  pirs- saite  Yt.  j^.47.  2)  anschliessead  'dazu, dazu  auch,  und  auch';  aStS  sl  vSxs  .  . */ramrvqriö  ä  vacS  aAuriS  vairyö  fraoxtS .  ,  spanvaitti  H,7,4;  —  hil  hama  pairi- süite  fräpaya  (sd.)  datikus  ä  upaosatih- väsca  Yt  /p.  1 ;  —  yi  ä  axti/  ahinäi  ySm axfSyöi  (sd.)  dSn/ig  Y.jÖ.i;  —  >wsi  as *ärmaitis  "^wS  ä  gPui  tasäi^i.)  as  Y.^i. 9,  a)  wiederholt  'et  .  ,  et',  nach- gestellt: ahunm  masdqm  ämruyi  (sd.) nmänahe  mitandpatSis  ratum  ä  vXsS  vTspa- töil  ratßm  ä'  .  .  daitihupatöis  ratüm  a Y.  13. 1.  a)  in  Verbindung  mit  (vor- ausgehendem) cä:  ahmClkSng  ,  .  urunö pasukanqincä  ,  .  yaHbyascä  tsi  ä  yascii aHbyö  ä  arfh)n  ".  .  für  welche  diese  und welche  für  diese  da  sind"  Y.  J5.  i.  a)  zu- gleich gegenüberstellend  'atque  tarnen': yS  .  .  paiti.hincaiti  ä  dim  (sd,)  mit  api- vatäite  daSnaya  ..  V.p.52.  II)  Praen.** i)  mitAkk.;  a)  räumlich,  o)  'hin  zu  ~,  hin gegen  — ':  ka'i:il  drupm  nls  ahmat  ä  nts näiiimä  (sd.)  fff^  ii  avä  yöi  . .  Y.44.13; 11;  —  iaoa  nö  ioa  . .  agats  iäiycjatjhatat haca  anhaot  aikyajaiiksin  ahüm  3  V.  iq.
7809:•  j.  f^naoha-  m.  EN.  eines  Gläubigen: vokustrahe  'nauhahe  aiaonö  "des  F.,  Sohns des  4 .."  Yl;j.i23.
8267:Komp.:  upa-\-*iUm,  —  Zum  V.  'ly-.  — Pü. :  kakar  ast  kus  apar  rajt  csift ,    erl. :    Susr.
8419:')  Der  iöf  i  apärscn  heisst  Bd.  13.  9  das grössie  Gebirg  nach  dem  Albiirz  [jut  hal  Aar- iuri  afärstn  köf  i  mas  ast);  auf  ihm  entspringen nach  Bd.  20.  16,  17,  21,  32  die  Flüsse  Harirüd, Ililmand,  Miit-fäb  und  Balx.  Danach  wäre  der westliche  Teil  des  Ilindükus  gemeint,  nördlich und  ästlich  von  Kabul,  das  küh  i  bäbä;  vgl. Ggb.  OK.  58,  GlrPh.  2.  393,  Dst.  ZA.  i.  loz. S.  noch  Ma«QUabt  Eransalir  286.
8491:'seioya-m.,  lum  V.'ilar-;  statt  •i/fj'd- geschr., S  26S.  iL  — Pü.;  valäH  unar  darr7ka^\  iarl. Andere  loVvi.;  s.Dst.  ZA.  2.  654 >).  S.  noch lu  s(k'iaya-  No.  l.  —  •»  Geschr,  b  b  a  (Ideo- gramm von  diir  Türe'j+MA;  daher  die  Etl. : kusäa  dar  apr  hast.  —  »  Wo  aber  in  der Obersetiung  vtiäl  mit   iSij/  verwechtelt  wird.
8921:AMeit.  —   Zum  V.  kay-.  —  np.  kln,  p-.  fronij —  I'ü. :  iiti,  erl. :  kusäii  pTiliJui!  kuii/iid.
8954:'töten,  totschlagen':  anyS  ahmHl  yö janaiti  Jraca  kusaiü  "ausser  dem,  der (ihn)  schlägt  und  lötet"  V.5.  34.
9620:•  j.  kuxsnüsa"  — ?  — :  N.4Ä Jedenfalls  lu  ^xinmi-;  s.  No.  1.    —    O  FrW. /.  2  hat  dafür  kujusnvlia   (ob  JSOM.?);    aber 71  a   der  Bombayer  N.-Ausg.  steht  nochmals (als  Zitat)  kuslniila.
9678:475                        kusra-                          —  gae9ä-  i                     476
```


## [2026-09-06T15:54:50.683Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"θβaxš\\|θβaxša\\|thβaxš\\|Ovaxs\\|9(3axs\" CHEUNG.txt | head; echo \"---\"; grep -n \"to be active\\|zealous\" CHEUNG.txt | head -20"
}
```


### [2026-09-06T15:54:50.744Z] TOOL RESULT

```
---
25899:foremost zealous, pushy one’ (Y 13.2). © For the meaning of YAv. Oßaz- and
```


## [2026-09-06T15:54:58.719Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '8940,8960p' BRT.txt | cut -c1-250; echo \"=== col markers\"; awk 'NR>=8900 && NR<=8970' BRT.txt | grep -nE \"4[0-9][0-9] \" | head"
}
```


## [2026-09-06T15:55:00.610Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Oßax\\|θβax\\|0ßax\\|Ößax\" CHEUNG.txt | head; echo \"== BRT thwaxsh\"; grep -n \"9paxs\\|Owaxs\\|paxsa-\\|Baxs\" BRT.txt | head"
}
```


### [2026-09-06T15:55:00.967Z] TOOL RESULT

```
•  j.  kaofa-,  p.  kaufa-  m.  r)  'Bergrücken, Höhenzug':  II  arkadris  näma"  °/a''  Bh.  /. » I ;  J-  7 ;  —  cd^wärü  vi'üwana  (sd.)  'fö YL  ig.z'i  —  vtgiihö  (sd.)  . .  'famm  Yt.  i4- 21.       2)'Höcker' desKamels  (nu
KompE.  —  np.  köh  'Berg',  toha  'Höcker'.
•  j.  kaoya-"'  Adj.  'den  Kavay,  der  Kavny- dyuastie  eigen,  it/j/isch':  uyrpm  kavaim^'' :^arptt5  (sd.)  mazda'jätain  Yt.  79.  9;  13", 68",  69,  /.  21,  (?.  2,  10.  66,  r37,  J2.  4,  Y. 2.14,  Vyt.40; —  küvayeheca^'^  3^armat
Ableit.  ans  ^kavay..  —  PS. :  kayän  farrak,  Sü. :
ka'Wtaiy
432
58.  13  und
rajnäm  Srih.    —    ')  zSchr.  •.
Cld.  kz.  32.  593.
j.  kanynm :  s.  ^kavay-.
•  j.  kaoirisa-  m.  Name  eines  Bergs  oder Gebirgs;  ahmat  haca  garay3  fraoxlyan  .. sasca  Yl  ig.  6*\
•)  Bd./?.  ässagt:  kndradd  (Tiansskr.  des Aw.  Worts)  kef  pa  cräii  vei.
Aus  it.  *iaiifisa..  —  Vgl.  ai.  äti-tulva-,  lat. calvuit     Also  'karav-  Adj.+'/jJ-?
•  j.  kaos-  V.,  nur  mit^rö  'töten'.  Praes.  3
'töten,  totschlagen':  anyS  ahmHl  yö janaiti  Jraca  kusaiü  "ausser  dem,  der (ihn)  schlägt  und  lötet"  V.5.  34.
np.  kullan  'töten'.  —  Pü. :  undeutlich.
•  j.  kaoia-  m.  EN.  eines  Gläubigen :  ^ac- raosahe  'iaAe  asaonS  "des  Fr.,  Sohns  des
K..."    Yt,  7^.12  2.
ai.  k.'sä-   m.  EN.  eines  Priestergeschlechls;?).
•  j.  "anaornS  (sd.)  tnanatjhe  kya  visäi kaia  kva  parg"  FrD.  6.
•  j.  kakahyav-  ra,  Name  eines  Bergs oder  Gebirgs:  ahmal  ha^a  gaiayö  frao- xsyan  .  .  °yus7a  Yt.  ig.  4.
=== col markers
```


### [2026-09-06T15:55:01.022Z] TOOL RESULT

```
== BRT thwaxsh
14381:SuperL  zu  %TBaxsa:  —  ai.  »gl.  tväkfiyas-  Adj., Kompar.  —  Pü.;  /uxsättum.
```


## [2026-09-06T15:55:13.693Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; pdftoppm -f 245 -l 245 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg245 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


## [2026-09-06T15:55:14.141Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '14370,14390p' BRT.txt | cut -c1-250"
}
```


### [2026-09-06T15:55:15.961Z] TOOL RESULT

```
total 7632
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 11:55 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     968 Sep  6 11:53 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   92182 Sep  6 10:55 bqt1854.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66580 Sep  6 10:57 bqt2023.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69965 Sep  6 11:25 bqt2242crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   28189 Sep  6 11:25 bqt2417crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  431133 Sep  6 11:16 bqt2420_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9548 Sep  6 11:25 bqt2meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb   81018 Sep  6 11:16 build213.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67391 Sep  6 11:49 build225.py
-rw-rw-r-- 1 sfmqrb sfmqrb   71757 Sep  6 11:47 build232.py
-rw-rw-r-- 1 sfmqrb sfmqrb   32265 Sep  6 11:51 build234.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb   84366 Sep  6 11:54 c246_n2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   51690 Sep  6 11:54 c246_n6.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb    6971 Sep  6 11:03 crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    8619 Sep  6 11:03 crop2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5240 Sep  6 11:03 crop3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12820 Sep  6 11:05 crop_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3408 Sep  6 11:05 crop_guthjo.png
-rw-rw-r-- 1 sfmqrb sfmqrb  111118 Sep  6 11:19 crop_habl.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9001 Sep  6 11:05 crop_node12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5564 Sep  6 11:05 crop_node1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5286 Sep  6 11:05 crop_varathra.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11652 Sep  6 11:13 c_xzn.png
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
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:44 p216
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:52 p233
-rw-rw-r-- 1 sfmqrb sfmqrb   33321 Sep  6 11:51 part1.json
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
-rw-rw-r-- 1 sfmqrb sfmqrb   78380 Sep  6 11:51 pg239.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81131 Sep  6 11:51 pg240.png
-rw-rw-r-- 1 sfmqrb sfmqrb   97613 Sep  6 11:49 pg242.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80632 Sep  6 11:55 pg245.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79253 Sep  6 11:54 pg246.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1209522 Sep  6 11:39 sin_goog.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  147680 Sep  6 11:20 sns167.jpg
```


### [2026-09-06T15:55:15.999Z] TOOL RESULT

```
Vgl.  ai.  pratiiakfSifäk ;  mp.  tuxiäk.  —  S.  auch
'tajt-,  —  Pü.:  fa  *'tuxiäJah.
•  j.  (hvaxäa-  Adj.  'rührig,  emsig,  eifrig'; patri  ti  haoma  .  .  äa6ami  imqm  tanüm  .  . 'Jili  Aaomili  Y.li.  10.
Znm  V.  itaaxJ-,  —  Pü.;  täi  man  iavil,  was nicht  zum  Aw.  Wortlaut  stimmt.
•  g.  d'waxäah-  n.  'Rührigkeit,  Eifer": ärmatBil  galhä  fräds  'satahä  "durch  die Rührigkeit  der  A.,  die  Haus  und  Hof fördert"  Y. 4Ö".  12;  - —  vidas  vä  -sauhs gavsi  "oder  wer  mit  Eifer  für  das  Rind sorgt"  Y.
Zum  V.  %viaxi:  —  ai.  tväifv  tu  —  Pfi.: iMiäkih,  (lu  Y.  ig):  tuxiäi;  Sü.  (dRn.):  vya- vasäyaiä,  'täyai,  'läyi.  —  •)  Eig.  'fiir  das  Rind sorgenden  Eifer'.
•  j.  d-waxsamna-  Adj,,  PPM,:  s.  %waxs:
•  j.  d-waxäiti  Inf  'sich  zu  rühren, emsig   tätig   zu  sein",   als  Diener:  ysistö
^w"  hvsUiB  (sd.)  ^paitis^mi  F.^e.
Zum  V.  %v:axs-  (S  aöb.  i  d).  —  P6.:  tuxiäi, tx\.\  framän  buriät  bavet.  —  i)  Im  Sinn  des Konj.  —  I  aus  idg.  >  oder  aus  idg.  i;  dann lu  einem  Praes.  24  oder  30  (Iler.)  *%iitaxiaya-.
•  j.  Onwaxäista-  Adj.  'der  rührigste, eifrigste':  yS  (nämL  Bura^ustrlf)  'tö  abavat mainivA  däman  Y.ff.  15;  —  mihra  .  .  yö 'ts  yatatanam  Yt  10.  98;  —  sraoSim  .  . yünqm  't>m  Y.  57. 13.
SuperL  zu  %TBaxsa:  —  ai.  »gl.  tväkfiyas-  Adj., Kompar.  —  Pü.;  /uxsättum.
•  g.  ÖTwat  Adv,;  s.  ^wa:
g.  %wat  AbL:  s.  unter  "Wa-,
•  j.  ^Tvay-  V,  'Furcht  erwecken;  —  hegen'. Praes.  a  %waya-,  3  %wya-.
"Furcht  erwecken' :  %wyatit-  (nur  Ableit).
mit  upa  'sich  fürchten,  sich  ängstigen': pdhqm  %rvB.datanqm  ups.%wayäti  yasca . . "er  ängstigt  sich  vor  dem  Pfad,  der  . ." Vyt.27(?)').
Vgl  %aiayaiiha-.  —  gr.  vgl.  an«  (?,  Bgm.  GrGr.i 277).  —  1)  An  der  Parallelst  eile  V.  ig.  ag steht  jajai/i  statt  ufiä.%W.
•  j.  {hwayaoha-  n.  'gefährlicher  Zustand, Gefahr":  'fg/um  va  *d^wayanh»m  (sd.) va  N,  /o;  —  *dkwayankim  (sd.) . .  *'afam N./o.
KompE.     —     Ableit.  aus  "^viayah-.     —     Pü.:
•  j.  ^wayah-  n.  'Schrecknis;  Gefahr'. Ableit  —  Zum  V.  äwoy..
```


## [2026-09-06T15:55:27.699Z] TOOL CALL #30: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg245.png"
}
```


### [2026-09-06T15:55:28.199Z] TOOL RESULT

```

```


## [2026-09-06T15:55:28.194Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T15:55:41.809Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KNT kapautaka\"; grep -n -i \"kapautaka\\|kapauta\" KNT.txt | head; echo \"=== HRN\"; grep -n -i \"kabud\\|kabūd\\|kabūtar\\|kabutar\\|kapōt\\|kapot\" HRN.txt | head -20; echo \"=== PHD\"; grep -n -i \"kabōd\\|kapōt\\|kabod\\|kabotar\\|kabōtar\" PHD.txt PHD_mackenzie.txt | head -20"
}
```


### [2026-09-06T15:55:41.889Z] TOOL RESULT

```
=== KNT kapautaka
1801:IL. Secondary: *Akaufa-ka- in Akaufaciya-; Andma-ka-; ar-ika-, to pAr. *asra-, LAv. аюга; Атќа-Ка-, hypocoristic to a compound name; äršti- ka-, probably with vriddhi; kapauta-ka-; kdsa-ka-; ba^da-ka-; vazra-ka-; Vahau-ka-, hypocoristic to a compound name.
4262:37 : idä : akariya : kàsaka : һуа : kapautaka : uta : sikab
5242:kapautaka- adj. ‘blue’, in kdsaka hya kapau- |
=== HRN
7326:ai. kapota- 'Taube; grau, bleigrau (taubenfarbig,
=== PHD
PHD.txt:4989:kabod
PHD_mackenzie.txt:3120: kabOd [kpwt I N --] grey-blue; pigeon.
PHD_mackenzie.txt:3122:kabotar [kpwtll M kbwtr, N --] pigeon.
PHD_mackenzie.txt:6712:goblet jam(ag), payga!.                       grey-blue kabod.
PHD_mackenzie.txt:7283:pigeon kabod, kabotar.                     pollution ahidih, nasrust(ih).
PHD_mackenzie.txt:9458:kadag                     \5t-S    kabotar
PHD_mackenzie.txt:9548:kabOd                  \~\4J~         kardarih
```


## [2026-09-06T15:55:43.177Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== ISS/DKS kapauta\"; grep -n -i \"kapauta\\|kavuta\\|kavūta\" ISS_alt_DKS.txt | head -20; echo \"=== SOD\"; grep -n \"kp.wt\" SOD.txt | head -20"
}
```


### [2026-09-06T15:55:43.247Z] TOOL RESULT

```
=== ISS/DKS kapauta
1396:kavüta- ' blue, gray’, Z 22-154 ne atá haryasa ne atd ssáttana ne atä stauru Катта ‘(of the emperor's wife) not very black, not very white, not severely grey'. From kapauta- ' blue, grey’, O.Pers. kapautaka-, Greek-Pers. karravra, Zor.P. hapót, kapótar, ‘pigeon’, N.Pers. Рабба, kabótar,
=== SOD
39443:4793  kp'wt   B  >yf 
39449:4794  kp'wt'ych   B  j^S 
39457:4795  kp'wtk   B  Ajf 
40965:ku/apote/ic  (qwpwdyc)  ^kp'wt'ych,  qpwtyc
```


## [2026-09-06T15:55:53.411Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '1390,1404p' ISS_alt_DKS.txt"
}
```


### [2026-09-06T15:55:53.454Z] TOOL RESULT

```
kalyálkyim 'auspicious', K 156-62 vañi уе kalyakyim bada ‘now this auspicious time’, either Iranian from Aalya- ог BS kalyána-kya- (-im = -ai, -e). See kala- ; and s.v. sükyi.
kalyāsta 'excellent', K 29:192 vara prra(ma)na sabaja kalyasta 'there the brahman prospers (BS sampady-), excellent (in morals or skill)”; =K 38:131 prrammand sami-iund kalyāscya 'the brahman of noble origin, excellent". From katya- with suffix -dsta-. See kala-, and akalüíca; sami-fund from  Prakrit *same-yona-, BS samyag-yoni-.
kalsta- 'a particular ornament’, Z 13:137 cu hā aysárüna harastándd svarpa-süttára kalsta. куйе ратјиа parremá hüdai pharu nvāsa yidündi ‘what adornments they dis- played brocade (BS suvarga-sütra-), kalsta-ornaments, cita-ornaments, finger-rings, parrema-ornaments, they made for him very great noise’; K 63, 78v3 hara kaiyūra kaista maula paraima ' necklace (BS hara-), bracelet (BS keyüra-), kalsia-ornament, headdress (BS такщіа-), paraima-ornament'; JS 33v3-4 Reste keyure hāre graune galamna (grauna- ‘garland’ ; galamna- ' ornament"). From base kalt- with -£a- suffix, connected with O.Ind. kajaka- ' necklace from Ralt-a-, see T. Burrow, BSOAS 35, 1972, 538-9. See Aala-.
kava 'fsh', K 144, 1v3 mahdsamdmdrra kavä māñamdä tsīya ' would go like a fish in the great sea’; Z 24'504 kho ји за kava baltte ce duru псе jsa kaste 'as a fish quivers which falls far from the water’ ; Sid. дут kava гот pt jsa hamtsa ' together with fat of fish', BS matsya-tailena, Tib. ñahi Зар dan; plural Z 4:49 kave, JS зог2 kave (JS 28v2 keve for *kava). Adjective, Sid. 15105 kavamñe '(bone) of fish’, Tib. ña-rus; Sid. 17v2 kaviñe кийа, ibid. gv2 kavīñe gūsta 'fesh of fish’, Tib. а-а; Sid. r4ir5 kavindm aha khenda 'like fish eggs', Tib. ñahi sgo-ma hdra-ba, From карӣ-, Sogd. Кру, Yidya kap, Waxi kūp, Pašto kab, plur. kaban, kabünah, kabó; Oss. DI. käf, plur. káftd; I. jdu-gáf = käfy djcytd ' fish. eggs, caviar’, Connexion with Lakk хаба gen. xrablul (with xf = voiceless pharyngal 4) 'fish' uncertain. Possibly Oss. D. käsalgä, І. käsag ' fish" from older *kaffa-, with Wanetsī kaša, plur. ko3e ‘fish’. Caucasian Darga dialects savs, kavs, yaoš (R. von Erckert, p. 64, ‘from Ossetic"). Possibly from kap- 'grey' in O.Ind. kapila-, see kavüta-.
kara-baira uncertain word, see s.v. baira-, 11 51:97; ibid. ttugarü-barra.
kavürma 'safe place( ?)', 11 18, 8b tt và kavārma tsvümdi ‘they went to the keep’, after a list of names, as elsewhere spasaña tsue "he went on guard duty’, following names. Possibly from base kap- ‘то hold, imprison’, and var- ‘to surround, enclose', hence "Aapa-varma- *kavvürma-, dyadic compound. For kap- see khapa, kava; Armen. Iw kaparan ��bond, detention, prison’ from Iranian *hapadüna-.
kavüta- ' blue, gray’, Z 22-154 ne atá haryasa ne atd ssáttana ne atä stauru Катта ‘(of the emperor's wife) not very black, not very white, not severely grey'. From kapauta- ' blue, grey’, O.Pers. kapautaka-, Greek-Pers. karravra, Zor.P. hapót, kapótar, ‘pigeon’, N.Pers. Рабба, kabótar,
Armen. lw Rapoyt, kapoutak, Armen.-Lat. capotes, Sogd. kp'wthk ‘blue’, kp'wi'yčh, Man. ушрилуё ‘pigeon’, Yayn. kapüca' dove', Balöčī kapót, Мопјапі Rówiya, Yidya Абшїо, Waxi kibit, Ѕапаеёї kóvi8, Sarīkolī гађана, Kurd käwūk, Khowar lw Аоодг. O.Ind. kapdta- ‘dove’, kapotaka- ‘теу’. Base kap- 'grey' also in O.Ind. kapila-, kapisa- ‘reddish’, kapi- ' monkey’, Zor.P. Rapik 'monkey'. See also Апта ' fish'.
kašš-, has-, kas-, karš- ' fall, come into, fail’, Z 23:99 tra ttádeta kaśśīru ' may you fall into this darkness’; Z 10:11 varata kasfüre bodhi-sambüra hamalà ‘there the bodhi- sambhàra- ' means for bodhi-knowledge' come together"; Sid. r21v3 dyamkyai kasüre 'his sight fails', Tib. mig ldons-śin ' eye becomes blind’; 3 sing. Sid. 14r5 nastá ga kaste "faces go downwards’, Tib. lto sbo-bo dan; K 65, 82ут akşanvā hagtyà па kasaune ' may I not come into the eight calamities (BS айапа-)'; noun Sid. 2r2 biysma Rasane hivi pishalà ' chapter of the failing of urine’, Tib. géin sri-bahi lehu; Sid. 8v3 Бухта katama, Tib. дёп hgag-pa (hgag-ba 'stop") With intrusive -r- only JS 38v3-4 karse bhadrre-kalpya ' migrates into the bhadra- kalpika- world’, parallel BS cyavate. Participle kasfa-, K 64, 81v3 küladva hasta ' fallen into the kilada- ( ?)'; JS asvi ttädeta kastye ysama-famdat vaska “ог the world (= BS loka-) fallen into darkness’; 1 sing. ш 2, 7r4 taña bärmaña kaşfūm ' I have come into this prison’; Ш 5, 11v5 hamtharkaña hasta ‘соте into distress’; Y 32, gas kastin; K 46:47 та tcaimefia kasfe 'I failed in my eye’. From base kas- with -ya-. Elsewhere Iranian kap- “to fall’, Zor.P. kaf-, M.Parth. T. kf-, gf-:hft, gft 'to fall, Аит, М.Регѕ.Т. ghwn *kafvan, *hahuan, N.Pers. kuhan, kuhnah 'old'; Zor.P. Арі, kptn 'to fall’, Balo&t kapag, k'afay, kapta 'fall, happen, bring forth’. Possibly kass-, from kas-y- with =s= < -tr- (as basaka- ' calf") to base kas-, kah- (sce khah-), if *Ras-s- gave kats- > kas- (as O.Ind. vivatsati 'wishes to dwell’, fut. vatsyati to base was- ' dwell").
ka&cai 'sorrow', П 7:117 уяга kaścai hethiye ' the heart has been troubled in sorrow" where Ааќса loc. sing. is possibly from Rasca but with shortened -а- (hethīye < hamthrīye).
*Jasa- ' belt(?), 111 41:26—7 Rhua daittá hasta Каха haritya а panīśdä ' when the lord sees you, he loosens or ties up his belt’, Uncertain: possibly -dy- from -as- as in käş- ‘to look’, and Asdya ‘віх’ from хаў, Then to Iranian kafa-, Av. kala-, 'armpit', Zor.P, kaš, dast-kaf ‘hands under arms’, N.Pers. kaš, M.Pers.T. dst-Rf" respectfully ', Sogd. р-у 'side', Buyni bi-fuf ‘armpit’ from *api-kafa-, Wax kal- (-1 < -#-), N.Pers. kalk ‘side under armpit’. IE Pok. 611 kokso-, -à ' part of body’, O.Ind. Ra&sa, kaksa-, Lat. coxa ‘hip’; O.Ind. kaksa-, haksya- ' girdle, girth’,
kasta- ‘attached’, see Лаз-, Мап). 170-1 аката asakhesta sa khu ja veysa ' unaffected, unsmeared like the lotus’,
kagtü 'sunken', ш 79:9 aid stä brraihd: Каза ті pattiye ' the horse fatigued, the belly fallen in, the muscles stiffened', see also päta- 'fallen in, sunken’.
kas- 'fall, come to, arise, migrate’, V 125, 6b3 (second of the five dangers) Avi abádd niroskasate kasindá ' when for him untimely water rises, they fall. ..'; atas-, Z 24:168 kye và ра-зішпава dtasare tta gre ‘who fall headlong, so they stay’. For kaste 3 sing., see kasi-. Participle kasfa-
to both Aas- and Rasi-, see kaíi-. Conjunct niroskasate from nira uskasate, Possibly kas- from kas-s-, see khah-.
```


## [2026-09-06T15:55:54.947Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== SOD page\"; grep -n \"4793  kp'wt\\|4793\" SOD_pages.txt | head -3; awk 'NR<=39460' SOD.txt | grep -c \"\"; grep -n \"kp'wtk\" SOD_pages.txt | head -3"
}
```


### [2026-09-06T15:55:56.837Z] TOOL RESULT

```
== SOD page
17360:      GMS 1014; STii 5.42                                 4793 kp'wt B                                          >yf
37752:Go)be proper     8693                     biped    3732                          blue 4793,4795
38445: grey blue 4793, 4795                           hangman      6538                         having   2696, 2806
39460
17372:                                                          4795 kp'wtk     B                                     Ajf
```


## [2026-09-06T15:56:21.366Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR<=17372' SOD_pages.txt | grep -n \"pdf page\" | tail -3; echo \"=== KNT page for 5242\"; awk 'NR<=5242' KNT.txt | grep -nE \"^ *17[0-9] *$|^ *17[0-9] \" | tail -5; sed -n '5238,5246p' KNT.txt"
}
```


## [2026-09-06T15:56:21.549Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '7315,7340p' HRN.txt | cut -c1-300"
}
```


### [2026-09-06T15:56:23.197Z] TOOL RESULT

```
=== KNT page for 5242
5125:174
5165:175
5173:176
5210:177
5220:178
vi- + kan- ‘dig apart, destroy’: viyakanam 1st sg. imf. XPh 38. viyaka" imf. ($208, §228.11) DB 1.64. vikanàhy 2d sg. subj. (327) DB 4.71, 78; vikandh"-di& (S27, 454.11, $136) DB 4.77.
*kan- vb. of uncertain connections, probably ‘throw, place’: cf. NPers. dwgdnddn ‘heap up’ from ava-kan- (Dv. Gr. $184; Morgenstierne, Acta Or. 1.249; Hz. ApI 225).
ava- + kan- ‘put down on, place on’: avakanam Ist sg. imf. (8213, 5226.1) DB 1.86.
Ka™pa"da- (8111) sb. ‘Kampanda’, a district in Media (cf. Kónig, RuID 71): Elam. qa-um-pan- taš, Akk. ha-am-ba-mu. Kapada пет. DB 2.27.
kapautaka- adj. ‘blue’, in kdsaka hya kapau- |
taka ‘lapis lazuli’: deriv. ($146.11) of stem in РЫ. — | kapót, NPers. kabod ‘gray-blue’, Skt. kapóta- ‘pigeon, pigeon-color, gray’ (Scheil 21.29; Bv. BSLP 30.1.61; Konig, Burgbau 62; Bleichsteiner, WZKM 37.94-101; Wb. AfOF 7.42, cf. PW 10.1887 s.v. Караша; Hz. AMI 3.64-5). kapau- taka nsm. DSf 37.
Käpišakāni- sb. ‘Kapishakani’, a fortress in Arachosia ($117, $126): Elam. qa-ap-pi-i3-fa-qa- nui, Каракат ns. DB 3.608.
Ka"büjiya- sb. ‘Cambyses’, (1) father of Cyrus the Great; (2) son of. Cyrus the Great, king of Persia before-Dartus: Elam. kan-bu-si-ia, АКК.
LEXICON
```


### [2026-09-06T15:56:23.238Z] TOOL RESULT

```
LW. kurd. keü^ qewy, vergl. Kas. köik, kcnrk; af/.
kabk; bei. kabg, n. kaivg (120).
'Eine starke Verstümmelung* der sansk.-bel. Formen
(Geiger) kann das neupersische Wort nicht sein;
in der Stammsilbe {kebk aus *kapak) sind sie aber
gewiss identisch (etwa auch mit kebiiter?). Ihr Ver-
bal tniss zu gr. nuy.Tcdfirj^ arm. knffav, syr. qaqqewä, alle
'Rebhuhn (Hübschmann, ZDMG. 46, 241 No. 60),
ist unklar.
842. kebüter 'Taube, nni5D (Jer. 48, 28), kebüd 'blau',
keffer (inbD, Ps. 56, 1, Litbl. f. or. Ph. 11, 19:^, kebük.
ai. kapota- 'Taube; grau, bleigrau (taubenfarbig,
vergl. kapöta-)\ vergl. jain. käö {*kapötu-) 'Nuance
der Hautfarbe zwischen blau und rot* (Leumann bei
Feist, Got. Etym., S. 144); phlv. kapötar 'Taube'
(Papyrus, Hörn, ZDMG. 43, 50), kcqM 'blau (Men.
27, 50 'der blaue Wolf, vergl. palang IJD kapötar
"ij:n'»*lp 'der Panther, den man kapötar^ d. i. tauben-
farbig, nennt* im sog. Iran. Bund,, briefliche Mitteilung
von Dr. E. W. West vom 23. 11. 1891); arm. LW.
kapoit 'blau (vergl. Bartholomae, BB. XVII, 101).
kurd. kewük, kavök^ kötir; af/. kavntar , kautar;
bei. kapöt (191), köntar (210); wa;^. kibit, sar. cabnnd,— 188 -
Im Neupersischen muss auch einmal ein Majhül-
vokal vorhanden gewesen sein ; doch reimt schon bei
FirdüsT kebüd auf düd (I, S. 5 Vers 77), numüd (I,
```


## [2026-09-06T15:56:38.049Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; head -3 SOD_pages.txt | cut -c1-120; echo \"...\"; grep -c \"pdf page\" SOD_pages.txt; echo \"=== BQT v3\"; ls -la incoming/BQT/; head -5 incoming/BQT/BQT_v3_pages.txt | cut -c1-150; grep -c \"pdf page\" incoming/BQT/BQT_v3_pages.txt"
}
```


### [2026-09-06T15:56:38.150Z] TOOL RESULT

```
 SOGDIAN
DICTIONARY
Sogdian - Persian - English
...
0
=== BQT v3
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
[pdf page 1]
[NOT OCRED - use tools/ref_page.py]
[pdf page 2]
7
Ub
721
```


## [2026-09-06T15:56:42.200Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; head -40 data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json; echo \"=== tool help\"; python3 tools/ref_page.py --help 2>&1 | head -30"
}
```


### [2026-09-06T15:56:44.034Z] TOOL RESULT

```
{
"pdf": "data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf",
"pdf_pages": 721,
"offset_mode": 1203,
"anchors": 34,
"map": {
"1210": 1,
"1211": 2,
"1212": 3,
"1213": 4,
"1214": 5,
"1215": 6,
"1216": 7,
"1217": 8,
"1218": 9,
"1219": 10,
"1220": 11,
"1221": 12,
"1222": 13,
"1223": 14,
"1224": 15,
"1225": 16,
"1226": 17,
"1227": 18,
"1228": 19,
"1229": 20,
"1230": 21,
"1231": 22,
"1232": 23,
"1233": 24,
"1234": 25,
"1235": 26,
"1236": 27,
"1237": 28,
"1238": 29,
"1239": 30,
"1240": 31,
"1241": 32,
"1242": 33,
"1243": 34,
=== tool help
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


## [2026-09-06T15:56:46.219Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb; ls data/verification/sources/refs/ocr/BQT/ 2>/dev/null | head -40"
}
```


## [2026-09-06T15:56:47.623Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls data/verification/sources/refs/ocr/ 2>/dev/null; ls data/verification/sources/refs/ocr/BQT 2>/dev/null | wc -l; ls data/verification/sources/refs/ocr/BQT 2>/dev/null | grep -E \"158|164|173\" "
}
```


### [2026-09-06T15:56:47.681Z] TOOL RESULT

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
203
```


### [2026-09-06T15:56:47.949Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T15:56:50.146Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 300 python3 tools/ref_page.py BQT:1589 --image 2>&1 | tail -40"
}
```


### [2026-09-06T15:56:57.692Z] TOOL RESULT

```
قرشت» پرنده‌ایست کهآنرا بعریی‌در اج‌میگو, ندم. | پاباب است» وآن جایی باشد ازرودخانه که پیاده
کبکنجهر - بفتح اول وثالك وسکون توا ن گذشت .

نانی ونون و جیم بتختانی رسیده و برای قرشت کبود - بر وزن حود » رنگی است

زده, فلاخن راگویند۴ - و بمعنی مرخ نیز پر | معروف وآسمان بدان رنگه است۷ - ونام کوهی

و بلند پرواز هم آمده است ؛ و بعضی گوبند هم هست ۸ وغربان کوه را جبل کوبند.

کبکنجیر دراج اس و آن پرنده‌ای باشد (۳) کبودان * سم اول وئانی بواومجهول

(۱) چش : قبیح ! (۷) چش : چموش . (۳) چش : است.

۱- (ص) «كبكبة ( بفتح ) کروه » كبكبة ( بم اول و سوم )کروه درهم پیوسته از
اسبان وجز آن » «منتهی‌الارب» « اقرب‌الموارد ».۴ - ر4 : ح ۷ صفحهٌ قبل .۰ ۴ مسحف
«کشکنجیر» (هم.) ۴ - صرالین عبدالحمید « کبکنجیر » را در کلیله ودمنه ( چاپ
اول قرب ص۱۸۰ ) درترجمهٌ « صفرد > عرییءمذ کور درکلیله ودمنهٌ آبن مقفع (مصحح‌محمدحن
نائل المرصفی سس ۲۰۱ > بکار برده و صفرد پرنده ایست كوچك مانند كنجشك » و بدان در جین.
(تری ) مثل زنند و گویند : اجین من‌سفرد « تاصقی اضاً ص ۲۰۱ ح ۲ در فرهشگهای فارسی
کبکنجیر را دراج کفته اند . 2 < کول , پوستین گوسپندکلان سال ۶ رشیدی ».

‎٩‏ - دربزم وصال دوش دل‌محرم بود خاطر چو نهال آرزو خرم بود

‏کنجشکه نهاده سینه برسینة‌باز تا صبح مدار بر کیوتردم بود.
ظپوری « بهار عجم ».

‏۷ -کردی ۴6۷ (آبی ) » مازندرانی ۳21 , 88۷ , 881 « ژابا س ۳۵4 :۰۷
کیلکی ۴8۳۵4 . اشکاشمی 1۴8۳۵۸ (آیی ) «گربرسن ۸۱ > ورك : کبوتر .

‏۸ - «کبون بذال معجمه. قربه‌است. بین آن‌وسمرقند چهارفرسنگه‌است>«ممجم البلدان».

‏7 کبوآر - بفتح ( وئی زکسر) اول وفتح چپارم » ازه کبود» (آبی) رك :کفتر » کبوك.
هندی‌باستان -۴80۵18 (کبونر ؛ خاکستری )» پهلوی ۳2۳۵127 ( کبوتر ), 680۵1( کبود)»
آرمنی ع ۴۵0011 ( کبود ) . کردی ۷۵۷۵۷ ۰ ۴۵۷۵ . ۳فا۴۵ . اشانی 8۷012۳ ۰
7 بلوچی 18۳۵1 , ۴۵۵1۵۳۲ , وخی انتانا. سربکلی2208141. رك : اسشق_هوبشمان
7 پرنده‌ایست از راستةٌ کبوتران » داراي بالهای دراز و پاهای كوچك و نازك و منقار ضمیف؛

‏و آن‌نزادهای متعدد دارد .
```


## [2026-09-06T15:57:08.308Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 300 python3 tools/ref_page.py BQT:1648 2>&1 | tail -35"
}
```


### [2026-09-06T15:57:15.290Z] TOOL RESULT

```
جفاوو زو تم | ۱ کشت ۷ - بنم اول بر وزن جفنك ن
و 2 ول و واو پروزن جمل را گوبند و آن جانورست که سر کین را
فرامرز » بمعتی دهقان وبرزیگر و زراعت کننده ۳ ام
5 0 : میغلطاند و میبرد .
باشد - و زمین زراعت و کشت‌زار .انیز گوبند. وا
کشتاد ‎٩‏ - با ای قرشت بر وزن کشتگان رنده - کنابه از شهیدان
هشیار . چانور سمل کرده را کوبند که پیربی | است » و شهیدکسیراکویند که در خدمت امام
مذبوح خوانند . زمان باکفار جنگه کند وکشته شود.
کشتاو ۰۱- بفتح اول و سکون ثالی کشتمند ۸ - بکس اول و فتح میم
وفوقانی بالف کشیده و بواو زده , بمعنی‌رقت‌است | بروزن خشت بند » زمین زرامت کرده شده را
که آن مغموم بنم مردم بودن‌ویر حال درخیر | گودند #۰
۹ -کمعان بنم است3۷81382 , نام سلله‌ای از شاهان که از نراد ۷16601 یا ازاسل
«سکه‌اء بودند واند کی پی‌ازم رکه 5غ71484001<27)برفندهار وپنجاب مستولی شدند . رل :
کریتنن . ساسان ۲۹ ببعد و رك : فهرست اعلام همان کتاب . ولف 251۵8 خوانده است .
منسوب‌بدان* کشانی»است: کشانی هم اسر زمان جان ,داد تو گوبی که هر کز ز مادر نزاد.
فردوسی طوسی « فرهنگه نظام > .
۴ - دامن کعان , کما نکشان . ۴ - تنها متعمل نیت بلکه اسم‌فاعلهای‌مرخم
مختوم به «کش » به - آن جمم بسته شوند . ۴ - از :که (< کمت) +۱ (واسطه) +
ورز ( ورزیدن ) :
کشاورز با مرد دهقان نژاد کی شد بر ما بهنگام داد .
فردوسی طوسی « فرهنگه نظام > .
8 - پهلوی 7 ۴۵5۲ بمعنی کشته بکار رفته . رك : دین مخمنه . دستور پهاوی ص
۵۶ » ور : نیب رکه مس ۱۳۰ : داایقاظ ۵3
بدبتن خویش چو خودکرده‌ای باید خوردنت ز کفتار ,خوش .
ناصر خنرو بلخی ص ۰.۲۱۲
- نیز پمعنی حاصل مصدر منی قتل بکار میرود . رك : اسم مصدر بقلم نگلرندهی ۱۱۰
و۹ ۹ -ظ . برساختهٌ فرقهٌ آذرکیوان . ۷ -رك : کستل . ورك: رشدی.
۸ - از :کشت (کاشتن) ۳ مند ( پسوند اصساف ):
دو منزل زمین تا بر هیرمند پر از آب و خوث میوه وکشتمند .
اآندی طوسی « رشیدی > .
۰ کشتن - بنم اول و افتح سوم ء اوستا - ۳2۵0۶۵ , ۴۷۶۳2141 ( قتل , کشت ) :
پپلوی 9122 «اسشق ۸۵۵ ۰ نیزپهلوی ۳۵2۳801188 ( نزاع کردن ) ازربشة - 6۵910,
قی : #طفاطای۵ا (* کخش نم اول در فارسی ) و 1۵8101185110 ( کشتار در فارسی ) :
بقیه درحاشية صفحهٌ ۱۹۶۹
```


## [2026-09-06T15:57:27.913Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 300 python3 tools/ref_page.py BQT:1731 2>&1 | tail -30; echo \"=== paths\"; ls data/verification/sources/refs/ocr/BQT/ | grep -E \"1589|1648|1731\""
}
```


### [2026-09-06T15:57:35.786Z] TOOL RESULT

```
وبسکون ثالت, بنای بلند راکویند و بمربی‌ضر کوف » بر وزن سوف . پرنده ایست
خوانند ‎٩‏ بنحوست مشهو رکه آنرا بوم و چشد لیز کوبند

۱ - از : کوش ( کوشیدن )+ ان ( پوند صفت فاعلی ) .

۴ - نیزه کوشان » نام قومی‌است . رك :کشان . ۴ - از :کوش (کوشیدن) +
ش ( پنوند اسم مصدر ) . راك : کوشیدن .

۴ - پراکنده شد ترك سیصد هزار بجایی نید کوشش و کارزار .
فردوسی طوسی . شاهنامةٌ بخ اج ۸ ۲۶۶۱ و راك : اسم مصدر بقلم نگارنده ص ۸

8 - رك : كوچك . ۹ کوفه « تاریخ سیستان ص ۰۳۲۹ ۳۳۸ > پهلوی
۳۶۴ ۰« بونکرصس ۱۰۶ دردی 0512 (کلاه فرنگی بالای بناء اطاق تابستانی) « ژابا ص
۰ معرب آن ۸ جوسق ؟ « این درید >. ۷ -رك : کشکنجی .

۸ - رشیدی «کوشه > را مترادف «کوشا » و «کوشان » بمعنی کوشنده آورده بدون
شاهد . جهانگیری «کوشه »> را بمعنی کوشیده کفته بدون شاهد , انجمن‌آرا و فرهنکه تظام این
کلمه‌را نیاورده اند . اگراستعمال شده باشد ظ۰ آسم مصدر است از: کوش (کوشیدن) ۰-۳(پوند
انم مصدر ) رك : آسم مصدر بقلم نگارنده ص ‎٩۹‏ بیعد ؛ در تاجیکی 1۳08136 بمعنی نشخواراست
سخن ۲ :۸ص ۹۲۱ > » و در تاررخ سیستان « کوشه > بممنی كوشغك آمده . ر4 : ح ‎٩‏ .۰

‎٩‏ - اصح «کوغیار» (هم.) است . ۴ بمعنی اخر ظ . با ۸« بهمتیار» که
شاگرد ابوعلی بوده » لفظاً و معناً خلط کرده‌اند . ‎۹٩‏ ر3 : رشدی .

‏5 کوهشیدن - بنم اول وافتح پنجم ( درقدیم 6۵5101127 ) » پهلوی ۳۵5۳01180
از ره - 1۵35 ۰ - 3۳۵88 ( قی : پهلوی 1۵981550 و 8۵91181110 ) ۰ شاد از
۶۸ - 2620 , 0(8581) 3۵6 5 . باختمانی از - 1۲5 » ساسکریت 519108811
(کشیدن ) فارس ی کنونی «کشتن > ( جنم ) « نیب رکه ص۱۳۰ ؛ جد وجهد کردن»سعی کردن:
« دولت نه بکوشیدن است » چاره کم جوشیدن است . » «گلتان س ۱۱۳ .

=== paths
1589.png
1589.txt
1648.png
1648.txt
1731.png
1731.txt
```


## [2026-09-06T15:57:49.732Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT; python3 -c \"\nfrom PIL import Image\nfor p,box in [('1648.png',(0.05,0.86,0.98,1.0)),('1731.png',(0.05,0.80,0.98,0.95))]:\n    im=Image.open(p); w,h=im.size\n    c=im.crop((int(box[0]*w),int(box[1]*h),int(box[2]*w),int(box[3]*h)))\n    c=c.resize((c.width*2,c.height*2))\n    c.save('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_'+p)\n    print(p, im.size, c.size)\n\""
}
```


### [2026-09-06T15:57:52.602Z] TOOL RESULT

```
1648.png (1650, 2546) (3070, 714)
1731.png (1650, 2546) (3070, 764)
```


## [2026-09-06T15:57:54.894Z] TOOL CALL #45: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_1648.png"
}
```


### [2026-09-06T15:57:55.069Z] TOOL RESULT

```

```


## [2026-09-06T15:57:55.067Z] INPUT

[Image: original 3070x714, displayed at 2000x465. Multiply coordinates by 1.53 to map to original image.]


## [2026-09-06T15:58:01.218Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT; python3 -c \"\nfrom PIL import Image\nim=Image.open('1648.png'); w,h=im.size\nc=im.crop((int(0.05*w),int(0.815*h),int(0.98*w),int(0.885*h)))\nc=c.resize((int(c.width*2.2),int(c.height*2.2)))\nc.save('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_1648b.png')\nprint(c.size)\""
}
```


### [2026-09-06T15:58:03.257Z] TOOL RESULT

```
(3377, 393)
```


## [2026-09-06T15:58:05.572Z] TOOL CALL #47: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_1648b.png"
}
```


### [2026-09-06T15:58:05.670Z] TOOL RESULT

```

```


## [2026-09-06T15:58:05.667Z] INPUT

[Image: original 3377x393, displayed at 2000x233. Multiply coordinates by 1.69 to map to original image.]


## [2026-09-06T15:58:22.559Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} END{print NR}' SNS_pages.txt; echo \"---\"; awk 'BEGIN{RS=\"\\f\"} NR==150' SNS_pages.txt | grep -n \"kus\\|kos\\|kox\" | head -10; echo \"=== search kwhs\"; grep -n \"kwhs\\|koxs\\|kOxs\" SNS_pages.txt | head"
}
```


### [2026-09-06T15:58:24.253Z] TOOL RESULT

```
242
---
=== search kwhs
16063:ka-san 50/10             kOxsisn 216/3                       -m   236/1             mar 239/4
```


## [2026-09-06T15:58:28.930Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR<=8775' SNS_pages.txt | grep -c $'\\f'; echo \"---\"; awk 'BEGIN{RS=\"\\f\"} NR==150{print substr($0,1,600)}' SNS_pages.txt"
}
```


### [2026-09-06T15:58:30.614Z] TOOL RESULT

```
126
---
                                    o^U;c-,l:».t»;lj                                                                                  Lu c—»Lr a*b ail*
                                                                                                                                                                                          Tf
9-X



                             .v.^Uy-o^V'^ vuhuman: >6*M                                                                                           •d/n^f -A/A^                    m/T<^
lotwal 5n5.             181)            .^ W*i   ^W
```


## [2026-09-06T15:58:40.130Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(json.dumps(d['SNS'],ensure_ascii=False,indent=1))\"; echo \"=== page 150-ish blocks\"; cd data/verification/sources/refs; for n in 148 149 150 151; do echo \"--- blk $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n{print substr($0,1,300)}' SNS_pages.txt | tr -s ' '; done"
}
```


### [2026-09-06T15:58:41.831Z] TOOL RESULT

```
{
 "title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/VajnameShayest",
 "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt"
 ],
 "page_offset": "242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image",
 "covers_etymology": true,
 "notes": "OCR quality is POOR: Persian text mostly garbage, Latin transliterations partially readable. Verification will usually need the page image."
}
=== page 150-ish blocks
--- blk 148
 M




 Lj c—^L: ft-U illj 
--- blk 149
 )




 li; ^^U 4.1*3!}
 (Ujo-^U^L*^
 
--- blk 150
 o^U;c-,l:».t»;lj Lu c—»Lr a*b ail*
 
--- blk 151
 bfc.U.;!, T^r
 c-jAic— fc**fc*3'3.
```


## [2026-09-06T15:58:55.430Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for f in MON_part1.txt MON_part2.txt; do echo \"== $f\"; grep -n \"کبک\\|کبود\\|کبوتر\" $f | head -5 | cut -c1-200; done"
}
```


## [2026-09-06T15:58:56.327Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 300 python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/کبک' --note 'page 245, root Kau 2, Persian kabk partridge etymology' 2>&1 | tail -20"
}
```


### [2026-09-06T15:58:57.145Z] TOOL RESULT

```
== MON_part1.txt
3778:گل کبود» گل ارزق» عروس النیل. آبگون. 
3971:کبیر» یاس کبود. پلم. آقطی صغیر: (گیا.) 
6609:کبوتر. نوعی پرستو. 
6635:کبود» ازرق» آسمان‌گون. 
8620:نیلگون؛ 1 آسمان کبود؛ آستفان نیلگون. 
== MON_part2.txt
3417:کوکو. (جاذ.) کبوتر. 
11140:فبج: لجادر ,91 [معر. کبک ] (.) (جان.) 
11141:کبک 
12277:کبوتر» کبوتر بغدادی. 
12318:(مص‌ل.) بانگ کردن (کبوتر» شتر» شکم).
```


### [2026-09-06T15:58:59.740Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/f21d22b60349a8c1.txt
```


## [2026-09-06T15:59:02.355Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; grep -n -A15 -i \"^Persian\\|Etymology\" data/verification/sources/web/f21d22b60349a8c1.txt | sed -n '1,60p'"
}
```


### [2026-09-06T15:59:02.403Z] TOOL RESULT

```
65: Etymology 1 
66-
67- 1.2.1 
68- Noun 
69-
70- 1.2.1.1 
71- Alternative forms 
72-
73- 1.2.2 
74- References 
75-
76- 1.3 
77: Etymology 2 
78-
79- 1.3.1 
80- Proper noun 
81-
82- Toggle the table of contents 
83-
84- کبک 
85-
86- 7 languages 
87-
88- فارسی 
89- Français 
90- हिन्दी 
91- Kurdî 
92- Malagasy 
--
194: Etymology 1
195- [ edit ] 
196-
197- From Middle Persian [Book Pahlavi needed] ( kpk' /⁠kabk⁠/ , “ partridge ” ) , Northern Luri کڢگ ( kwg ) . Compare Ancient Greek κᾰκκᾰ́βη ( kăkkắbē ) .
198-
199- Noun
200- [ edit ] 
201-
202- کبک • ( kabk ) ( plural کبک‌ها ) 
203-
204- partridge ( bird ) 
205- c. 1030 , Manuchehri , (Please provide the book title or journal name) : گویی بط سفید جامه به صابون زده است
206- کبک دری ساق پای در قدح خون زده است gōyē batt-i safēd jāma ba sābūn zada-ast
207- kabk -i darī sāq-i pāy dar qadah-i xūn zada-ast You would say the white duck has washed its robes with soap,
208-That the valley partridge has dipped its feet in a cup of blood. 
209-
--
222: Etymology 2
223- [ edit ] 
224-
225: Etymology tree
226-
227- Algonquin kepék bor. 
228- French Québec bor. 
229- Persian کبک 
230-
231- Borrowed from French Québec .
232-
233- Proper noun
234- [ edit ] 
235-
```


## [2026-09-06T15:59:09.703Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in 'https://en.wiktionary.org/wiki/کبوتر' 'https://en.wiktionary.org/wiki/کبود' 'https://en.wiktionary.org/wiki/کشتن' 'https://en.wiktionary.org/wiki/کوشیدن'; do echo \"### $u\"; timeout 300 python3 tools/fetch_source.py \"$u\" --note 'page 245 verification (roots Kau 1 / Kavuta)' 2>&1 | tail -2; done"
}
```


### [2026-09-06T15:59:14.406Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/کبوتر
/home/sfmqrb/git/rishe/data/verification/sources/web/e7e1c4b52350950b.txt
### https://en.wiktionary.org/wiki/کبود
/home/sfmqrb/git/rishe/data/verification/sources/web/ec3a3e86b59b3923.txt
### https://en.wiktionary.org/wiki/کشتن
/home/sfmqrb/git/rishe/data/verification/sources/web/e532defa01506fed.txt
### https://en.wiktionary.org/wiki/کوشیدن
/home/sfmqrb/git/rishe/data/verification/sources/web/245b4eedaf0e20aa.txt
```


## [2026-09-06T15:59:17.501Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in e7e1c4b52350950b ec3a3e86b59b3923 e532defa01506fed 245b4eedaf0e20aa; do echo \"##### $f\"; grep -n -i -A6 \"^ *From \\|Inherited from\\|Etymology tree\" $f.txt | sed -n '1,45p'; done"
}
```


### [2026-09-06T15:59:19.160Z] TOOL RESULT

```
##### e7e1c4b52350950b
181: From Wiktionary, the free dictionary
182-
183- See also: كبوتر 
184-
185- Persian
186- [ edit ] 
187-
--
203: From Middle Persian [Book Pahlavi needed] ( kpwtl ) , 𐫐𐫁𐫇𐫤𐫡 ( kbwtr /⁠kabōtar⁠/ , “ pigeon ” ) , from Old Persian *kapautah , from Proto-Indo-Iranian *kapáwtas ( “ pigeon ” ) . Cognate with Baluchi کپوت ( kapōt ) , Sanskrit कपोत ( kapota ) . 
204-
205- Pronunciation
206- [ edit ] 
207-
208- ( Classical Persian ) IPA ( key ) : /ka.boː.ˈtar/ , /ka.buː.ˈtar/ 
209-
--
394: Categories : Persian terms inherited from Middle Persian 
395- Persian terms derived from Middle Persian 
396: Persian terms inherited from Old Persian 
397- Persian terms derived from Old Persian 
398: Persian terms inherited from Proto-Indo-Iranian 
399- Persian terms derived from Proto-Indo-Iranian 
400- Persian terms with IPA pronunciation 
401- Rhymes:Persian/ar 
402- Rhymes:Persian/ar/3 syllables 
403- Persian lemmas 
404- Persian nouns 
##### ec3a3e86b59b3923
144: From Wiktionary, the free dictionary
145-
146- Persian
147- [ edit ] 
148-
149- رنگِ کبود 
150- Etymology
--
153: From Middle Persian kpwt' ( kabōd , “ blue-gray; pigeon ” ) , from Old Persian 𐎣𐎱𐎢𐎫𐎣 ( k-p-u-t-k /⁠kapautaka⁠/ ) , from Proto-Iranian *kapawtakáh , from Proto-Indo-Iranian *kapawtakás , from *kapáwtas ( “ grey - blue ” ) . Cognate with Sanskrit कपोतक ( kapotaka , “ pigeon-coloured ” ) , Old Armenian կապուտակ ( kaputak ) (an Iranian borrowing).
154-
155- Pronunciation
156- [ edit ] 
157-
158- ( Classical Persian ) IPA ( key ) : /ka.ˈboːd/ , /ka.ˈbuːd/ 
159-
--
242: Categories : Persian terms inherited from Middle Persian 
243- Persian terms derived from Middle Persian 
244: Persian terms inherited from Old Persian 
245- Persian terms derived from Old Persian 
246: Persian terms inherited from Proto-Iranian 
247- Persian terms derived from Proto-Iranian 
248: Persian terms inherited from Proto-Indo-Iranian 
249- Persian terms derived from Proto-Indo-Iranian 
250- Persian terms with IPA pronunciation 
251- Rhymes:Persian/oːd 
252- Rhymes:Persian/oːd/2 syllables 
253- Rhymes:Persian/uːd 
254- Rhymes:Persian/uːd/2 syllables 
##### e532defa01506fed
166: From Wiktionary, the free dictionary
167-
168- See also: گشتن and كسبن 
169-
170- Persian
171- [ edit ] 
172-
--
176: From Middle Persian [Term?] ( /⁠kuštan⁠/ ) , from Proto-Iranian *kawš- ( “ to fight, kill ” ) , from Proto-Indo-Iranian *kawš- , from Proto-Indo-European *kewh₂- ( “ to hit, strike ” ) with s-extension.
177-
178- Pronunciation
179- [ edit ] 
180-
181- ( Classical Persian ) IPA ( key ) : /kuʃ.ˈtan/ 
182-
--
1064: From Proto-Iranian *karH- ( “ to spread out, sow, make furrows ” ) , from a conflation of two roots:
1065-
1066- Proto-Indo-European *kʷerH- ( “ to spread, scatter (seed), sow ” ) , whence also Old Irish fo·ceird ( “ to put, throw ” ) , and
1067-
1068- Proto-Indo-European *kʷolh₁-eye- ( “ to make furrows, plough ” ) , a causative formation of Proto-Indo-European *kʷel- ( “ to turn end-over-end, to revolve ” ) , whence also Latin colō ( “ to till, cultivate ” ) and English cultivate .
1069-
1070- Pronunciation
--
1954: Categories : Persian terms inherited from Middle Persian 
1955- Persian terms derived from Middle Persian 
1956- Persian terms derived from Proto-Iranian 
1957- Persian terms derived from Proto-Indo-Iranian 
1958- Persian terms derived from Proto-Indo-European 
1959- Persian terms with IPA pronunciation 
1960- Rhymes:Persian/an 
--
1965: Persian terms inherited from Proto-Iranian 
1966: Persian terms inherited from Proto-Indo-European 
1967- fa:Death 
1968-
1969- Hidden categories: Middle Persian term requests 
1970- Persian terms in nonstandard scripts 
1971- Persian links with redundant wikilinks 
1972- Persian links with redundant alt parameters 
##### 245b4eedaf0e20aa
142: From Wiktionary, the free dictionary
143-
144- Persian
145- [ edit ] 
146-
147- Etymology
148- [ edit ] 
--
150: Etymology tree
151-
152- Proto-Indo-European *kewh₂- der. 
153- Proto-Indo-Iranian *kawš- 
154- Proto-Iranian *kawš- der. 
155- Middle Persian [script needed] ( kwhš-ytn' /⁠kōxšīdan⁠/ ) 
156- Persian کوشیدن 
--
158: From Middle Persian [script needed] ( kwhš-ytn' /⁠kōxšīdan⁠/ , “ to strive; to struggle; to endeavor ” ) , from Proto-Iranian *kawš- ( “ to fight, kill ” ) (whence also کشتن ( koštan , “ to kill ” ) ), from Proto-Indo-Iranian *kawš- , from Proto-Indo-European *kewh₂- ( “ to hit, strike ” ) with s-extension. [ 1 ] Cognate with Central Kurdish تێ کۆشان ( tê koşan , “ to try; to strive for ” ) , Northern Kurdish tê koşîn ( “ to try; to strive for ” ) and Gurani جە کۊشیای ( ce küşiyay , “ to try; to strive for ” ) .
159-
160- Pronunciation
161- [ edit ] 
162-
163- ( Classical Persian ) IPA ( key ) : /koː.ʃiː.ˈdan/ 
164-
--
637: Categories : Persian terms inherited from Middle Persian 
638- Persian terms derived from Middle Persian 
639- Persian terms derived from Proto-Indo-Iranian 
640- Persian terms derived from the Proto-Indo-European root *kewh₂- 
641- Persian terms derived from Proto-Iranian 
642- Persian terms derived from Proto-Indo-European 
643- Persian terms with IPA pronunciation 
--
655: Pages with etymology trees 
656: Persian entries with etymology trees 
657- Persian terms in nonstandard scripts 
658- Persian links with redundant wikilinks 
659- Persian links with redundant alt parameters 
660- Persian links with manual fragments 
661- Pages with entries 
662- Pages with 1 entry
```


## [2026-09-06T15:59:38.977Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== KLN hay\"; grep -n \"^hay,\\|hay, n\\.\\|hoe, n\\.\" KLN_1966.txt | head -5; grep -n -i \"haujam\\|hawwan\" KLN_1966.txt SKT.txt | head -10; echo \"== SKT\"; grep -n \"HAY\\.\\|HOE\\.\\|^Hay\\|^Hoe\" SKT.txt | head -10"
}
```


### [2026-09-06T15:59:39.070Z] TOOL RESULT

```
== KLN hay
17325:hay,  n.,  grass  mown.  —  ME.  have,  hey,  fr.  OE. hieg,  hig,  heg,  rel.  to  OS.  hoi,  ON.  hey,  Dan.  ho, Swed.  ho,  Norw.  hoy,  OFris.  ha,  he,  MDu.  hoy, hooy,  Du.  hooi,  OHG.  houwi,  hewi,  MHG. hbuwe,  hou,  G.  Heu,  Goth,  hawi,  ‘hay’,  lit.  ‘that which  is  to  be  cut’,  or  ‘that  which  is  cut'.  Cp. OE.  heawan,  ‘to  cut’,  and  see  hew.
17327:hay,  n.,  a  hedge  (archaic).  —  ME.  hai,  hei,  a blend  of  OE.  hege,  ‘hedge’,  and  F.  haie,  of  s.m. F.  haie  is  a  loan  word  fr.  Frankish  *hagja,  which is  rel.  to  OHG.  hegga,  OE.  hege,  ‘hedge’,  OE. hecg,  of  s.m.  See  hedge  and  cp.  the  first  element in  haybote,  hayward.
== SKT
8478:Hay.  (E.)  M.  E  A^y.  A.SA^^.+Diu hooi,  Icel.  hiy,  Don.  Swed.  ho,  Gulh.  Aav^ grass:  G.  hem.  Properly  'cut  gnus;' from  the  verb  to  Hew ;  !>ee  Hew.
8745:Hoe:  M:e  Hew.
11284:Hay  (a),  the  fifth  month.  (K.-L)  K Mai.  *  L.  Afaiuj^  M  ay  ;  the  moec| •growth.'     (VMAGII)
15676:Hay  (r>;  sec  Badina.
```


## [2026-09-06T15:59:40.414Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 300 python3 tools/fetch_source.py 'https://www.etymonline.com/word/hay' --note 'page 245, root Kau 1, English hay from Germanic *haujam' 2>&1|tail -2; timeout 300 python3 tools/fetch_source.py 'https://www.etymonline.com/word/hoe' --note 'page 245, root Kau 1, English hoe via Old French houe from Frankish *hauwa' 2>&1|tail -2"
}
```


### [2026-09-06T15:59:43.003Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/4f8c0bb2ccf70604.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2d99be528b74aa77.txt
```


## [2026-09-06T15:59:45.673Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; grep -n -i -m2 -A6 \"hay (n\" 4f8c0bb2ccf70604.txt | head -20; echo \"=== hoe\"; grep -n -i -m2 -A6 \"hoe (n\" 2d99be528b74aa77.txt | head -20"
}
```


### [2026-09-06T15:59:45.738Z] TOOL RESULT

```
23: hay (n.) 
24-
25- "grass mown," Old English heg (Anglian), hieg , hig (West Saxon) "grass cut or mown for fodder," from Proto-Germanic *haujam , literally "that which is cut," or "that which can be mowed" (from PIE *kau- "to hew, strike;" source also of Old English heawan "to cut;" see hew ).
26-
27- Germanic cognates include Old Norse hey , Old Frisian ha , Middle Dutch hoy , German Heu , Gothic hawi "hay."
28-
29: Slang phrase hit the hay (pre-1880) was originally "to sleep in a barn;" hay in the general figurative sense of "bedding" is from 1903; roll in the hay (n.) is from 1941.
30-
31- Entries linking to hay 
32-
33- hew (v.) 
34-
35- Old English heawan "to chop, hack, gash, strike with a cutting weapon or tool" (class VII strong verb; past tense heow , past participle heawen ), earlier geheawan , from Proto-Germanic *hawwanan (source also of Old Norse hoggva , Old Frisian hawa , Old Saxon hauwan , Middle Dutch hauwen , Dutch houwen , Old High German houwan , German hauen "to cut, strike, hew"), from PIE *kau- "to hew, strike," a root more widely developed in Slavic (source also of Old Church Slavonic kovo , Lithuanian kauti "to strike, beat, fight;" Polish ku ć "to forge," Russian kovat' "to strike, hammer, forge;" Latin cudere "to strike, beat;" Middle Irish cuad "beat, fight").
=== hoe
23: hoe (n.) 
24-
25- "implement for digging, scraping, or loosening earth," mid-14c., from Old French houe (12c.), from Frankish *hauwa , from Proto-Germanic *hawwan (source also of Old High German houwa "hoe, mattock, pick-axe," German Haue ), from PIE *kau- "to hew, strike" (see hew ).
26- also from mid-14c. 
27-
28- hoe (v.) 
29-
30: early 15c., "to clear weeds with a hoe," from hoe (n.). Tedious and toilsome work, hence a hard (or long) row to hoe "a difficult task;" hoe (one's) own row "tend to one's affairs." Related: Hoed ; hoeing .
31- also from early 15c. 
32-
33- Entries linking to hoe 
34-
35- hew (v.) 
36-
```


## [2026-09-06T15:59:52.820Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '11130,11150p' MON_part2.txt; echo \"=== kabud/kabutar in MON_part2\"; grep -n \"کبود\\|کبوتر\" MON_part2.txt | sed -n '1,10p'"
}
```


### [2026-09-06T15:59:52.896Z] TOOL RESULT

```
قسباله‌نویس: ۰-۷5 [ع. ف. - 
قباله نویسنده | (ص‌فا.) آنکه قباله نویسد؛ 
چک‌نوس» صکاککك. 

قسبان: 7:۰2 [سعر. کپان - قهان] (ا.) 
ترازویی که دارای یکت بله باشد؛ قیان. 
قانمد: 1 [ع. ف.| (امسر.) 
بالا یوش نمدی» بارانی نمدین. 

فبج: لجادر ,91 [معر. کبک ] (.) (جان.) 
کبک 

قبچور: ۰۵۵5۲ [مف. - قیچور - قوبجور] 
(.) مالیات» باج. مالیات متعلق به مواشی و 
حبوانات (ابلخانان). 


۱۳۳ فر هنگ فارسی معیر قیح 


=== kabud/kabutar in MON_part2
3417:کوکو. (جاذ.) کبوتر. 
12277:کبوتر» کبوتر بغدادی. 
12318:(مص‌ل.) بانگ کردن (کبوتر» شتر» شکم). 
14806:کبوتر متوسط است. طول پرهای دمش نیز 
15685:آن بسه تسرتیب: نیلی» کبود» سبزء زرد؛ 
16854:زنیل مانندی که در خانه آویزند تا کبوتران 
18146:ازرق» کنود. کبود چشم. ضح. در گیلان 
19705:زنبیلی که کبوتر در آن تخم گذارد. 
20010:کبود (غم.) 
20161:کبوتر: (ند. -)»هاتاطت [دکفتر - کیتری از
```


## [2026-09-06T15:59:56.796Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '20150,20185p' MON_part2.txt; echo \"=== kabk entry\"; grep -n \"کبک\" MON_part2.txt | sed -n '1,20p'"
}
```


### [2026-09-06T15:59:56.899Z] TOOL RESULT

```
ستوران و آدمیان به طریق اجتماع. (ف.) 


جاه و جلال»؛ شکوه) شوکت. 
کبک خرام: صجمجطام1 .. [- 
کبک خرامنده] (ص‌فا.) آنکه روش اس مانند 
کبک زیبا باشد. 


کبل: اقا (- کول | (.) پوستینی که از 
پوست کوسزندان بزرگ دوزند؛ پوستین 
کبوتر: (ند. -)»هاتاطت [دکفتر - کیتری از 
رشه «کود»» آبی] (.) (جاذ.) برنده‌ای . 
اس توا کال وا انتفاعت که ارفخار 
بزرگتر ولی از کبک کوچکتر است و خود 


راسته مشخصی را در بسن پرندگان نوجود 


کیو ترباز فررهنگ فارسی معیر ۱۳۳۵ 


می‌آورد که بنام راسته کسوتران نامیده 
می‌شود و شامل تمام گونه‌های مختلف 
کبوترها می‌گردد. منقار کبوتران ضعیف و 
در قاعده برآمده است. در حدود ۲ گونه 
کبوتر در سراسر کر زمین تشخیص داده 
شده است و چون گونه‌های این جانور به 
وسیلةٌ انسان اهلی و تربیت و پرورش داده 
شده‌اند از این لحاظ نژادهای بسیاری از آن 
تا به حال بوجود آمده‌اند بطوری که در هر 
کبوترخانه می‌توان نژاد مخصوصی را 
برحسب انتخاب مربی تولید کرد. اين پرنده 
بصورت زوج (نر و ماده) زندگی می‌کند. 
کیوتر ماده ۸ تا ۰ روز پس از جفتگیری 
=== kabk entry
11140:فبج: لجادر ,91 [معر. کبک ] (.) (جان.) 
11141:کبک 
19181:کلیک اوتیء کبک گیاه| (ا.) (گیا.) گیاهی 
20110:کبک نر و ماده به یکك اندازه‌اند» لیکن 
20112:قهوه‌یی دیده می‌شود. پای کبک جوان زرد 
20114:کبک بر خاکستری و کله‌اش زرد است. 
20115:کبک نر و ماده در بهار جفتگیری می‌نمایند 
20117:کبک ماده در اردیبهشت ماه در زمین چاله‌ای 
20129:آن باید در منازل چمن تهیه کرد تا کبکث در 
20132:جوجهٌ کبک بیرون آید. جوجهً کبک 
20134:حجل» قبج» کبک کبک معمولی؛ ج 
20135:کبکان. کبگان بزم: (کد.) ساقیان و مطربان و 
20136:شاهدان. کبک دری: (جاد.) گونه‌ای کبک 
20141:می‌ز ید. جثه‌اش تا سه برابر کبکت معمولی 
20142:ممکن است برسد و همه خصابص کبکث 
20144:موسیقی قدیم. کبک رقاص: ( کن.) اسب 
20145:شوخ و بازیگر. کبک کر: (جان.) دراج. 
20146:کبک معمولی: (جان.) کیکك. 
20148:کبکبه: (م)عاهاها (ع. کبکبهة | (ا) گروه : 
20154:کبک خرام: صجمجطام1 .. [-
```


## [2026-09-06T16:00:06.652Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '20098,20112p' MON_part2.txt"
}
```


### [2026-09-06T16:00:06.706Z] TOOL RESULT

```
کوتاه و ضخیم و استخوان تارس (با مقايسة 
استخوان آدمی می‌توان گفت استخوان کف 
ا) در این حیوان نسبتهٌبلند و بدون پر است. 
در حدود هشت گونه از این برنده شناخته 
شده که همه در نقاط کوهستانی آسیا و ارو با 
یه ان خی دی اما کت لو 
درخت و به اصطلاح روباز زندگی می‌کند و 
روی شاخه‌ها نمی‌رود و اکثر یکك زوج نر و 
ی ات 
جفتگیری و بعد از آن نر و ماده با هم بسر 
می‌برند و از دانه‌های گیاهی و حشرات و 
سزی‌ها و بر درختان تغذیه می‌کنند. 
کبک نر و ماده به یکك اندازه‌اند» لیکن 
رنگ نر زیباتر و روی سینه‌اش لکه‌ای 
قهوه‌یی دیده می‌شود. پای کبک جوان زرد
```


## [2026-09-06T16:00:11.832Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=20060 && NR<=20098' MON_part2.txt | grep -n \"کبک\\|\\[\" "
}
```


### [2026-09-06T16:00:13.555Z] TOOL RESULT

```
16:کبریت: :۲۰۳ [معر.] (.) گوگرد. (ف.) 
21:کیس: ۲۵5۰ [ع.] (مصم.) به خاک انباشتن 
29:کبش: ۲۵05 [غ.] (ا.) گوسفند نر شاخدار؛ 
35:کیک: اد! [دراج - معر. قیج | () (جان.)
```


## [2026-09-06T16:00:22.877Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '39435,39465p' SOD.txt | cut -c1-140"
}
```


### [2026-09-06T16:00:23.059Z] TOOL RESULT

```
4792  kp'wr   B,  M  jylT 
kapur   (kpwr) 

camphor 

TSP  3.171,  270,  7.109;  Benv.  Notesi  53;  GMS  807 

4793  kp'wt   B  >yf 
kapot 

blue,  grey  blue 
TSP  3.32,47,  101 

4794  kp'wt'ych   B  j^S 

kapote/ic   ©Yaghn.  kapuci  =^qpwtyc, 

qwpwtyc 
dove,  pigeon 
EGSii  85;  GMS  1186n  1;  SCE  163,  175,  351 

4795  kp'wtk   B  Ajf 
kapote   ©<OP  kapautaka 

blue,  grey  blue 
TSP  3.114,  128,  146 

4796  kp'ystCh)  B  uUU 
kapist  (kpyst)  ©pi.  of  kap
```


## [2026-09-06T16:00:31.648Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 300 python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/kewh₂-' --note 'page 245, root Kau 1, PIE *kewh2- to hit/strike' 2>&1|tail -2; sed -n '1,80p' tools/verify_check.py"
}
```


### [2026-09-06T16:00:34.091Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/40c28ff6f53d0391.txt
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
```


## [2026-09-06T16:00:36.681Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '80,140p' tools/verify_check.py"
}
```


### [2026-09-06T16:00:36.730Z] TOOL RESULT

```
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


## [2026-09-06T16:00:50.114Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; grep -ho \"Indo-Sc[a-z]*\\|Indo-Sch[a-z]*\" data/extracted/batch/*.json | sort | uniq -c"
}
```


### [2026-09-06T16:00:50.173Z] TOOL RESULT

```
     13 Indo-Schythian
```


## [2026-09-06T16:00:51.920Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"tuek̑-\\|tvaksati\\|tvakš\\|tväks\" POK_0*.txt | head; echo \"== watkins twerk\"; grep -n \"twerk-\\|tuek\" AHD_watkins1985.txt | head -5"
}
```


### [2026-09-06T16:00:52.004Z] TOOL RESULT

```
== watkins twerk
1100:twerk-. To cut. Zero-grade form *twrk- in Greek sarx, flesh (< “piece of meat”): SARCASM, SARCO-, (SARCOID), (SARCOMA), (SARCOUS); ANASARCA, ECTOSARC, PERISARC, (SARCOCARP), SARCOPHAGUS, (SARCOPTIC MANGE), SYS- SARCOSIS. [Pok. tuerk- 1102.]
1242:ANA- an! ANABAENA gWa- ANABAPTIST g¥ébh-1 ANABIOSIS gWei- ANACOLUTHON sem-! ANACRUSIS kreue-2 ANADEM dé- ANADIPLOSIS dwo- ANADROMOUS der-1 ANAGLYPH gleubh- ANAGOGE ag- ANALCIME = alek- ANALECTS leg-1 ANALEPTIC (s)lag¥- ANALOGOUS leg-! ANALYSIS leu-1 ANAMNESIS men-1 ANAPEST peu- ANAPHORA bher-? ANARTHROUS ar- ANASARCA twerk- ANASTOMOSIS ste-men- ANASTROPHE  streb(h)- ANATHEMA dhé-1 ANATOMY tem- ANCESTOR ked- ANCHOR ank- ANCHORITE ghé- ANCIENT! ant- ANCILLARY kWel-1 ANCON ank-
1441:EsLis gWela-1 EBULLIENCE beu-! ECBOLIC gWele-1 ECCENTRIC kent- ECCHYMOSIS gheu- ECCLESIA kela-2 ECCRINE krei- ECEsIsS weik-1 ECHARD segh- ECHELON skand- ECHIDNA ang¥hi- ECHINO- ang¥hi- ECHINUS angVhi- ECHO (s)wagh- ECHOLALIA 1a- ECLAIR kelo-2 ECLAIRISSEMENT kelo-2 ECLAMPSIA [ap- ECLECTIC leg-! ECLIPSE leikw- ECLOSION kleu-3 ECOLOGY weik-1 ECONOMY weik-1 ECRU kreue-1 ECSTASY sta- ECTO- eghs ECTOSARC twerk- ECU skei- ECUMENICAL welk-1 ECZEMA yes- EDACIOUS ed- EDAPHIC sed-! EDDY eti EDELWEISS _athal-, kweit- EDEMA oid- EDENTATE dent- EDGE ak-
2079:PER- pert PERCEIVE kap- PERCENT dekm PERCH? perk-1 PERCOLATE kagh- PERCURRENT kers-2 PERCUSS kwét- PERDITION d6- PERDURABLE deue- PEREGRINE agro- PEREMPTORY em- PERENNIAL at- PERFECT dhé-1 PERFIDY bheidh- PERFORATE bher-2 PERFUME dheu-1 PERFUNCTORY bheug-2 PERFUSE gheu- PERGOLA perg- PERI- per! PERICARDIUM kerd-1 PERICLINE Klei- PERIGEE gé PERIHELION sawel- PERIL per-4 PERIMYSIUM mis- PERINEPHRIUM negWh-ro- PERIOD sed-2 PERIONYCHIUM nogh- PERIOSTEM ost- PERIPATETIC pent- PERIPETEIA pet- PERIPHERY bher-1 PERIPHRASIS gWhren- PERIPHYTON bheue- PERIPTERAL pet- PERISARC  twerk- PERISH ei-1 PERISSODACTYL per! PERISTALSIS | stel- PERISTYLE sta- PERITHECIUM dhé-1 PERITONEUM ten- PERITRICH _ thrix PERIWINKLE! weng- PERJURE yewes- PERMANENT men-3 PERMEATE mei-1 PERMIT (s)meit(a)- PERMUTE mei-1 PERNICIOUS nek-1 PERONEAL per-2 PERORAL 6s- PERORATE 6r- PERPEND (S)pen- PERPENDICULAR (S)pen- PERPETRATE peter- PERPETUAL pet- PERPLEX plek-
2212:SAPID sep-1 SAPIENT sep-1 SAPONACEOUS _ seib- SAPONATE seib- SAPONIFY seib- SAPONIN seib- SAPONITE seib- SAPOR sep-! SAPROBE gWei- SAPSAGO skep- SARCASM twerk- SARCO-  twerk- SARCOCARP twerk- SARCOID twerk- SARCOLEMMA lep-1 SARCOMA twerk- SARCOPHAGUS twerk- SARCOPTIC MANGE skep-, twerk- SARCOUS twerk- SARDONIC sward- SARDONYX nogh- SARMENTOSE serp-1 SARTORIUS serk- SASTRUGA ghd, ster-2 SATE! sa-
```


## [2026-09-06T16:01:52.017Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== HRN kuschten\"; grep -n -i \"kuschten\\|kuštan\\|kušten\\|köschiden\\|koschiden\" HRN.txt | head -5; echo \"== HRN 841 kebk\"; sed -n '7305,7318p' HRN.txt | cut -c1-200; echo \"== IEC p1521\"; awk 'NR>=1 && NR<=100000' IEC.txt | grep -n \"^1521$\\|^ *1521 *$\" | head"
}
```


### [2026-09-06T16:01:53.961Z] TOOL RESULT

```
== HRN kuschten
== HRN 841 kebk
840*"" kehest, kehestü, kel)este^ kewest, DDDD (Jer. 8, 14)
'Koloquinthe ; Gift, Aristolochia (?)\
aw. kapasti- (Spiegel, zuletzt Ar. Periode 46);
phlv. kapast (Bund.).
Die Bedeutung des aw. Wortes ist ganz unsicher
(vergl. Geldner, »5 Yasht, 77) ; lit. kopustas 'Kohlkopf,
das Spiegel vergleicht, gehört bestimmt nicht hierher.
841. kelfk *Kebhuhn*, arab. LW. (jabj^ qahjat.
vergl. skr. kajnnjala^ 'Haselhuhn*; bei. kainnjar^
n. I^awinjar 'Rebhuhn' (li)0).
LW. kurd. keü^ qewy, vergl. Kas. köik, kcnrk; af/.
kabk; bei. kabg, n. kaivg (120).
'Eine starke Verstümmelung* der sansk.-bel. Formen
(Geiger) kann das neupersische Wort nicht sein;
== IEC p1521
20085:1521
```


## [2026-09-06T16:01:56.252Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '20085,20095p' IEC.txt | cut -c1-300"
}
```


### [2026-09-06T16:01:56.300Z] TOOL RESULT

```
1521
(uerpó, see Supt: U and cf. urpo (2), urpol-; uerpos, à, see uorp- (2))
uers- (1) ‘droplet, sprinkling, shower, dew, rain’. WP I, 269. Cf. uersó (1) Skt. varsáh, -Á, Am. mfn. “rain, shower’; Av. cf. varo&-, v. ‘sprinkle’; Per. baris “rain”; Hitt. warsas (queried), id.; Gk. hérse, hérsé, f. (1) ‘dew’; Olr. cf. feraim, v. ‘pour, rain? beside Mi
uers- (2) ‘young of animal’. Cf. uerks- and uersën-. WP I, 269. (Skt. urs-) Skt. cf. (z-gde) vrsah, m. ‘young male, esp. bullock’; Gk. hérse, hérse, f. (2) “young ani- mal, lamb”; cf. also (?) Hes. errás, usu. érraos, m. (cram, wild boar’. A synthetic cpd.?); Lat. verres, gs: verr
uers- (3) 'growth, hard skin' Lat. cf. verr-üca, f. ‘wart; hillock’; OE wearr, m. *callouse'; OFris. cf. (?) wersene ‘wrinkle’
uersen- ‘male animal". Cf. uers- (2), uerks-. WP I, 269 Av. varo$no, adj. ‘male’; Ionic Gk. érsen, gs: -enos, adj. id.; Latv. vérséns, m. “ox; steer’
uersi- (?). Cf. WP I, 267 Skt. cf. vargi-sthah ‘highest’; Per. bi$, adj. “much, more’; Olr. ferr, Ir. fearr, adj. “better”. (ISophonic: Go. waírsiza, OHG wirsiro, ON verri ‘worse’; G wirs, wirsch “bad, raging’; Du. cf. wars 'averse") (!)
uersð (-ið, -aio) (1) ‘shed, sprinkle, pour, gush, rain’. Cf. uers- (1). WP I, 269 Skt. várgati, 3s. ‘shower, bedew’; pp: vrstah; cf. vrstíh, f. ran: Av. varo&-, v. ‘sprinkle; in- seminate'; Gk. eráo, v. (pour, spew forth’; cf. hérse, f. ‘dew’; herseeis, adj. ((bedewed'. Cf. al
uersó, ið (2) “drag, trail’. WP I, 292 Hitt. cf. warsiya(mi), v. (queried: “plough); Gk. Gro Locr. wérro, v. ‘drag’; Lat. verro, ére, OLat. vorro ('drag, trail; sweep, brush”,
uerpo — uertos
15
```


## [2026-09-06T16:02:04.337Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls data/verification/sources/refs/ocr/BOOK | tail -5; cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg245.png data/verification/sources/refs/ocr/BOOK/245.png; ls -la data/verification/sources/refs/ocr/BOOK/245.png"
}
```


### [2026-09-06T16:02:06.282Z] TOOL RESULT

```
92.png
94.png
95.png
96.png
99.png
-rw-rw-r-- 1 sfmqrb sfmqrb 80632 Sep  6 12:02 data/verification/sources/refs/ocr/BOOK/245.png
```


## [2026-09-06T16:02:15.639Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT; cat > 1648.vision.txt <<'EOF'\n[Borhan-e Qate', ed. Mo'in, printed p. 1648 — footnote 5, transcribed from the page image\n(the tesseract OCR mangles the Latin transliterations; this is what the print actually shows):]\n\n۵ کشتن ـ بضم اول و فتح سوم ، اوستا ـ kaosh ، kushaiti ( قتل ، کشتن ) ،\nپهلوی kushtan «اشتق ۸۰۰» ، نیز پهلوی kôxshîtan ( نزاع کردن ) از ریشهٔ ـ kôsh ،\nقس : kôshishn ( = کشش بضم اول در فارسی ) ، و kôshîtârîh ( کشتار در فارسی ) ،\nبقیه در حاشیهٔ صفحهٔ ۱۶۴۹\nEOF\necho saved; ls"
}
```


### [2026-09-06T16:02:17.578Z] TOOL RESULT

```
saved
0001.png
0001.txt
0049.png
0049.txt
103.vision.txt
1219.png
1219.txt
1219.vision.txt
1223.png
1223.txt
1225.png
1225.txt
1225.vision.txt
1226.png
1226.txt
1275.png
1275.txt
1280.png
1280.txt
1280.vision.txt
1294.png
1294.txt
1294.vision.txt
1299.png
1299.vision.txt
1300.png
1300.txt
1300.vision.txt
1302.png
1302.txt
1302.vision.txt
1339.png
1339.txt
1357.png
1357.txt
1382.png
1382.txt
1385.png
1385.txt
1385.vision.txt
1439.png
1439.txt
1445.png
1445.txt
1445.vision.txt
1452.png
1452.txt
1453.png
1453.txt
1455.png
1455.txt
1462.png
1462.txt
1465.png
1465.txt
1471.png
1471.txt
1472.png
1472.txt
1488.png
1488.txt
1492.png
1492.txt
1544.png
1544.txt
1564.png
1564.txt
1564.vision.txt
1571.png
1571.txt
1572.png
1572.txt
1572.vision.txt
1578.png
1578.txt
1578.vision.txt
1589.png
1589.txt
1624.png
1624.txt
1637.png
1637.txt
1637.vision.txt
1648.png
1648.txt
1648.vision.txt
1689.png
1689.txt
1689.vision.txt
1694.png
1694.txt
1707.png
1707.txt
172.vision.txt
1731.png
1731.txt
1754.png
1754.txt
1759.png
1759.txt
1774.png
1774.txt
1774.vision.txt
1776.png
1776.txt
1781.png
1781.txt
1783.png
1783.txt
1786.png
1786.txt
1786.vision.txt
1800.png
1800.txt
1802.png
1802.txt
1803.png
1803.txt
1803.vision.txt
1806.png
1806.txt
1807.png
1807.txt
180.png
180.vision.txt
1819.png
1819.txt
181.png
181.vision.txt
1832.png
1832.txt
1838.png
1838.txt
1841.png
1841.txt
1848.png
1848.txt
1854.png
1854.txt
1854.vision.txt
1861.png
1861.txt
1862.png
1862.txt
1864.png
1864.txt
1865.png
1865.txt
1870.png
1870.txt
1878.png
1878.txt
1900.png
1900.txt
1908.png
1908.txt
2023.png
2023.txt
2023.vision.txt
2080.png
2080.txt
2083.png
2083.txt
2099.png
2099.txt
2133.png
2133.txt
2143.png
2143.txt
220.vision.txt
2222.png
2222.txt
2224.png
2224.txt
2242.png
2242.txt
2242.vision.txt
2246.png
2246.txt
2246.vision.txt
2293.png
2293.txt
2331.png
2331.txt
2395.png
2395.txt
2396.png
2396.txt
2406.png
2406.txt
2407.png
2407.txt
2417.png
2417.txt
2417.vision.txt
2420.png
2420.txt
2420.vision.txt
2427.png
2427.txt
2427.vision.txt
31.vision.txt
333.png
333.vision.txt
58.vision.txt
70.vision.txt
72.vision.txt
733.png
733.vision.txt
902.png
902.vision.txt
```


## [2026-09-06T16:02:19.649Z] AGENT

Now writing the verification file.


## [2026-09-06T16:08:45.230Z] TOOL CALL #72: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p245 && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p245/build.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndoc = {\n \"pdf_page\": 245,\n \"book_page\": 215,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": []\n}\n\n# ------------------------------------------------------------------ entry 0\ne0 = {\n \"entry\": 0,\n \"root\": \"Kau, Qau 1\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *keh₂u- / *keh₂w- (older notation *kāu-, *kəu-) 'to hew, strike, beat'; Pokorny IEW 535, Watkins/AHD kau-², Wiktionary *kewh₂-\",\n \"note\": \"Pokorny p.535 carries the entry 'kāu-, kəu- „hauen, schlagen“' with Lat. cūdō, OHG houwan / OE hēawan 'hauen', Lith. káuti 'schlagen, schmieden; kämpfen', OCS kovati 'schmieden', Toch. A ko-, B kau- 'töten' — exactly Nourai's root box, and his page number is right. Walde-Pokorny I 330 f. is the source Pokorny abridges, and p.331 (which Nourai cites) is the very page that ends that entry. The modern laryngealist notation is *keh₂u- / *kewh₂- (Wiktionary, LIV 345 f.); Cheung 2007 derives the Iranian branch from an ingressive s-formation *keh₂u-s-. Language label ('Indo-European') and gloss ('to strike, beat') are both correct. The one real problem on this chart is inside the Avestan box: 'θβaxša' belongs to a different root, and 'kau-kušati' is not an attested form.\",\n \"note_fa\": \"جعبهٔ ریشه درست است: پوکورنی در صفحهٔ ۵۳۵ مدخل «kāu-, kəu-» را با معنای «زدن، بریدن» آورده و لاتین cūdō، آلمانی باستان houwan، لیتوانیایی káuti و اسلاوی کهن kovati را زیر آن نشانده است؛ پس شمارهٔ صفحهای که نورایی می‌دهد درست است. در نگارش امروزی، ریشه را *keh₂u- / *kewh₂- می‌نویسند و چونگ (۲۰۰۷) شاخهٔ ایرانی را از ستاک sدار *keh₂u-s- می‌گیرد. برچسب «هندواروپایی» و معنای «زدن، کوبیدن» هر دو درست‌اند. تنها لغزش این نمودار در جعبهٔ اوستایی است: «θβaxša» از ریشهٔ دیگری است و «kau-kušati» صورتی است که در هیچ فرهنگی نیامده است.\",\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/kewh₂-\", \"https://www.etymonline.com/word/hay\"],\n \"ref_check\": [\n   {\"ref\": \"POK:535\", \"status\": \"supports\",\n    \"note\": \"POK_02.txt (the leaf whose running numbers are 535-536): 'kāu-, kəu- „hauen, schlagen“. Lat. (mit präsensbildendem d) cūdō, -ere „schlagen, klopfen, stampfen, prägen“ ... ahd. houwan, ags. hēawan, aisl. hȩggua „hauen“ (dazu als „zu Hauendes“ got. usw. hawi „Heu“); lit. káuju, káuti „schlagen, schmieden; kämpfen“ ... toch. A ko-, B kau- „töten“. WP. I 330 f.' Page marker '535' stands two lines above the entry.\"},\n   {\"ref\": \"WLD:331\", \"status\": \"supports\",\n    \"note\": \"WLD_Bd1_pages.txt, running head 'kau-, keu-, ku 331': p.331 carries the closing paragraphs of *kāu- 'hauen, schlagen' (abg. kovati, lit. kūjis 'Hammer') and, on the same page, the note 'Ist av. fra-kušaiti „erschlägt, tötet“, np. kuštan „töten“ eine s-Erw.?' — i.e. exactly the material of Nourai's root box and Avestan node.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, k-list (AHD_watkins1985.txt line 591)\", \"stance\": \"supports\",\n    \"note\": \"'kau-². To hew, strike. 1. Germanic *hawwan in: a. Old English hēawan, to hew: HEW; ... 3. Germanic *haujam in Old English hieg, hay, cut grass: HAY. 4. Suffixed form *kau-do- in Latin cūdere (< *caudere), to strike, beat: INCUS. [Pok. kāu-, 535.]'\"},\n   {\"src\": \"IEC\", \"where\": \"Mann col./p. 483\", \"stance\": \"supports\",\n    \"note\": \"'kāuēiō, ið (kou-, kāu-, kū-) (1) “strike, hew”. WP I, 330 ... Av. cf. fra-kava “fight”; apa-kavo “warrior”; Per. kavam ...' — Mann puts the same root and the Iranian material on the same page as the 'raucous bird' root of Nourai's next chart.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *kauš¹, p. 251 f.\", \"stance\": \"supports\",\n    \"note\": \"'This well attested Ir. root goes back to an ingress. so-formation of IE *keh₂u-, cf. OCS kovati “to forge”, Lith. káuti “to murder, beat, hew”, OHG houwan, OE hēawan, Engl. to hew ... *PIE ingress. *keh₂u-s°/ₑ- > LIV: 345 f. | Pok.: 535.'\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n \"id\": 1,\n \"lang\": \"Avestan\",\n \"words\": \"kôš; fra-košaiti; kau-kušati; thwaxša\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Two of the four words are right and two are not. (a) 'kôš' is Bartholomae's Avestan headword kaoš- (AiW col. 431 f.), a verb attested only with the preverb frā; Bartholomae glosses it 'töten', not 'strike', so Nourai's gloss is one step too early. (b) 'fra-košaiti' is the single attested finite form, Vend. 5.34 anyō ahmāt yō janaiti frāca kušaiti 'except him who strikes and kills (him)'; the real form is frā ... kušaiti with short u (Nourai's ô is his own transcription of Iranian u/ū). Iranian *kauš- is an s-extension of PIE *keh₂u- 'to hew, strike' (Cheung 2007: 251 f., LIV 345 f., Wiktionary), so the arrow from the root box is right; Walde-Pokorny I 331 and Buck 4.76 both flag the s-extension as uncertain, but the modern handbooks (Cheung, LIV, Wiktionary) accept it. (c) 'kau-kušati „tries, fights“' is not an Avestan word: it appears in neither Bartholomae, Cheung, Buck nor Walde-Pokorny; it looks like Nourai's own display of the root *kau- plus the Sanskrit present kuṣṇáti 'tears, pinches' that Walde-Pokorny mentions in the same paragraph. (d) 'θβaxša „try“' is a real Avestan word — Bartholomae's θβaxša- Adj. 'rührig, emsig, eifrig', θβaxšah- n. 'Rührigkeit, Eifer', to the verb θβaxš- — but Bartholomae equates it with Sanskrit tvakṣ- 'to fashion, be active', i.e. PIE *tweḱs-/*twerḱ- (Watkins twerk-, Pok. 1102), and it has nothing to do with *keh₂u-. Nourai evidently put it here because its meaning matches kūšīdan 'to try' in the daughter box, but as a drawn arrow it is wrong.\",\n \"derivation_fa\": \"از چهار واژهٔ این جعبه دو تا درست است و دو تا نادرست. «kôš» همان مدخل kaoš- در فرهنگ ایرانی باستان بارتولومه (ستون ۴۳۱–۴۳۲) است که تنها با پیشوند frā به کار رفته و معنای آن «کشتن» است نه «زدن»؛ تنها صورت گواه‌دار آن frā ... kušaiti در وندیداد ۵؍۳۴ است. ایرانی باستان *kauš- ستاکی sدار از ریشهٔ هندواروپایی *keh₂u- «زدن، بریدن» است (چونگ ۲۰۰۷، LIV، ویکی‌واژه)، پس پیکان نورایی درست است؛ والده–پوکورنی و باک این پیوند را «بسیار نامطمئن» خوانده بودند ولی پژوهش امروزی آن را پذیرفته است. در برابر، «kau-kušati» صورتی اوستایی نیست و در بارتولومه، چونگ، باک و والده–پوکورنی دیده نمی‌شود (ظاهراً آمیزه‌ای است از kau- و سنسکریت kuṣṇáti). «θβaxša» نیز واژهٔ اوستایی راستینی است به معنای \\u00a bچالاک، کوشا»، امّا بارتولومه آن را هم‌ریشهٔ سنسکریت tvakṣ- می‌داند (ریشهٔ *tweḱs-)، نه *keh₂u-؛ پس گذاشتن آن در این جعبه خطای نورایی است که فقط به دلیل همانندی معنایی با «کوشیدن» صورت گرفته است.\",\n \"sources\": [W + \"%DA%A9%D8%B4%D8%AA%D9%86\", W + \"Reconstruction:Proto-Indo-European/kewh₂-\"],\n \"ref_check\": [\n   {\"ref\": \"SYN:290\", \"status\": \"supports\",\n    \"note\": \"Buck, Selected Synonyms, §4.76 KILL, p.290 (SYN.txt line 7450, between the page markers '288' and '290'): 'Av. fra-kuš- (only once, janaiti frā kušaiti, but cf. NPers. kuštan “kill”) prob. : Skt. kuś- “tear, etc.”, further connections dub. Walde-P. 1.331. Barth. 431.' Buck's table itself lists 'Av. jan-, fra-kuš-' for KILL. He supports the Avestan form and the link to NP kuštan, but calls the wider IE connection doubtful.\"},\n   {\"ref\": \"WLD:331\", \"status\": \"partial\",\n    \"note\": \"WLD_Bd1_pages.txt p.331: 'Ist av. fra-kušaiti „erschlägt, tötet“, np. kuštan „töten“ eine s-Erw.? Höchst unsicher bes. wegen der abweichenden Bed. von ai. kṣṇāuti, kuṣṇāti „reißt, zerrt, zwickt, knetet“.' Walde-Pokorny have the forms and the derivation Nourai draws, but mark it 'höchst unsicher' — hence 'partial'. Nothing on the same page connects θβaxša- with this root.\"},\n   {\"ref\": \"SNS:150\", \"status\": \"partial\",\n    \"note\": \"Tavoosi, Glossary of Shayast ne Shayast: the OCR (SNS_pages.txt, form-feed block 127) does carry the relevant glossary entry, readable as 'kušnāti, kōš / kusaiti, /kaoš-' and 'kwst, kws', and the index has 'kōxšišn 216/3'. So the book really does treat the k(a)oš-/kuš- material Nourai cites, but the printed page numbers are illegible in this scan (refs_online records 'page offset not determined — OCR too poor'), so p.150 itself could not be confirmed. Nothing found there for θβaxša- or kau-kušati.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch col. 431-432, s.v. kaoš- and (col. ~796) θβaxša-\", \"stance\": \"partial\",\n    \"note\": \"BRT.txt line 8954: 'j. kaoš- V., nur mit frā „töten“. Praes. 3 ... anyō ahmāt yō janaiti frāca kušaiti “ausser dem, der (ihn) schlägt und tötet“ V.5.34. np. kuštan „töten“.' Supports kôš and fra-košaiti; no 'kau-kušati' anywhere in AiW. For the fourth word, BRT.txt line ~14372: 'j. θβaxša- Adj. „rührig, emsig, eifrig“ ... Zum V. θβaxš-. — ai. tvakṣ- ...' — i.e. a different root.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Etym. Dict. of the Iranian Verb, *kauš¹ 'to fight, struggle; to kill', pp. 251 f.\", \"stance\": \"supports\",\n    \"note\": \"'*AVESTAN: Y Av. kuš- “to fight, struggle” ... Pres. them.: IND. 3sg. YAv. fra(-ca) kusaiti (V 5.34) ... *MIDDLE PERSIAN: MMP kws-, qws- “to struggle; kill”, BMP kwhs- /kōxš-/ “to strive, struggle, endeavour”, BMP kws- (NKSWN-) /kuš-/ “to kill” ... *PIE ingress. *keh₂u-s°/ₑ- > LIV: 345 f. | Pok.: 535.' Cheung has no entry attaching θβaxš- to this root.\"},\n   {\"src\": \"POK\", \"where\": \"IEW 535, kāu-, kəu- 'hauen, schlagen'\", \"stance\": \"silent\",\n    \"note\": \"Pokorny's article on p.535 lists Latin, Germanic, Baltic, Slavic and Tocharian reflexes but no Iranian form at all; the Avestan evidence enters only through Walde-Pokorny's footnote on I 331.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 2,\n \"lang\": \"Persian\",\n \"words\": \"koštan «کشتن»; kūšīdan «کوشیدن» (extra کوشش)\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Both verbs go back to Old Iranian *kauš- (Av. kaoš-/kuš-), the s-extension of PIE *keh₂u- 'to hew, strike'. (1) کشتن koštan/kuštan 'to kill' < Middle Persian kwštn' /kuštan/, present kuš- (Book Pahlavi NKSWN- as the Aramaic ideogram), regularly from the participial stem *kuš-ta-; the New Persian infinitive keeps the -tan of the MP infinitive unchanged and the u of the zero grade. (2) کوشیدن kūšīdan 'to strive, struggle' < Middle Persian kwhš-ytn' /kōxšīdan/, from the same root with the -xš- present suffix (*kauš-sk-); MP -ō- gives the New Persian majhūl ō that later merged with ū, and the -x- was lost between consonants, kōxšīdan > kōšīdan > modern kūšīdan (Mo'in expressly notes 'در قدیم kōšīdan'). The chart's 'extra' کوشش kūšeš is the regular verbal noun kūš (present stem) + -eš, and it is the word in the Ferdowsī line quoted in the box; MP kōxšišn is its exact ancestor. So the whole box, and the arrow to it, is standard and correct — with the one convention-caveat that Persian does not descend from Avestan but from the same Old Iranian stock, Avestan standing here as Nourai's proxy for Old Iranian.\",\n \"derivation_fa\": \"هر دو فعل از ریشهٔ ایرانی باستان *kauš- (اوستایی kaoš-/kuš-) اند. «کشتن» از فارسی میانهٔ kuštan (ستاک حال kuš-، به هزوارش NKSWN-) است که از صفت مفعولی *kuš-ta- ساخته شده؛ «کوشیدن» از فارسی میانهٔ kōxšīdan است که پسوند ستاک حال -xš- دارد؛ خـ میان دو همخوان افتاده و واو مجهول فارسی میانه (ō) در فارسی نو با ū یکی شده است: kōxšīdan > kōšīdan > کوشیدن. خود معین در حاشیهٔ برهان قاطع می‌نویسد «در قدیم kōšīdan». «کوشش» نیز از ستاک حال «کوش» + پسوند اسم مصدر «ـش» است و برابر فارسی میانهٔ kōxšišn. ادعای نورایی درست است؛ تنها یادآوری آنکه فارسی نو از اوستایی نیامده، بلکه هر دو از ایرانی باستان‌اند و در نمودارهای نورایی اوستایی جایگزین ایرانی باستان است.\",\n \"sources\": [W + \"%DA%A9%D8%B4%D8%AA%D9%86\", W + \"%DA%A9%D9%88%D8%B4%DB%8C%D8%AF%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:1648\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qate' ed. Mo'in, printed p.1648, footnote 5 to کشتن (read from the page image, saved as refs/ocr/BQT/1648.vision.txt): 'کشتن ـ بضم اول و فتح سوم، اوستا ـ kaosh، kushaiti (قتل، کشتن)، پهلوی kushtan «اشتق ۸۰۰»، نیز پهلوی kôxshîtan (نزاع کردن) از ریشهٔ ـ kôsh، قس: kôshishn (= کشش بضم اول در فارسی) و kôshîtârîh (کشتار در فارسی)'. This is precisely Nourai's chain Av. kaoš-/kušaiti → Pers. koštan, and it ties kūšīdan/kūšeš to the same root.\"},\n   {\"ref\": \"BQT:1731\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qate' printed p.1731, footnote to کوشیدن (refs/ocr/BQT/1731.txt): 'کوشیدن ـ بضم اول و فتح پنجم (در قدیم kōšīdan)، پهلوی kōxšītan از ریشهٔ -kauš ... فارسی کنونی «کشتن» ... «نیبرگ ص ۱۳۰»؛ جد و جهد کردن، سعی کردن'. The same page's note on کوشش reads 'از: کوش (کوشیدن) + ش (پسوند اسم مصدر)' and quotes the Ferdowsī line Nourai prints in the box.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary, s.v. kuš-/kušt and kōxš-\", \"stance\": \"supports\",\n    \"note\": \"Checked via CHEUNG's citation of the same forms and PHD_mackenzie.txt: Book Pahlavi kws- (NKSWN-) /kuš-/ 'to kill', kwhs- /kōxš-/ 'to strive, struggle', kwhssn /kōxšišn/ 'strife, combat' — the exact Middle Persian stage between the Avestan and the New Persian boxes.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"*kauš¹, NWIR section\", \"stance\": \"supports\",\n    \"note\": \"'Widely attested: NP kustan/kus- “to kill, slay; to beat, bruise”, Bal. kušt/kuš-, Kurd. kuštin/kuz-, Zaz. kištis ... NP kušti “fighting, wrestling”' — both Persian senses (killing and struggling) from the one root, as the chart has it.\"},\n   {\"src\": \"HRN\", \"where\": \"Grundriss der neupersischen Etymologie — grepped for kuštan/kōšīdan\", \"stance\": \"silent\",\n    \"note\": \"No entry found in HRN.txt for either verb (Horn's Grundriss omits them); a silent result, not a contradiction.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 3,\n \"lang\": \"Germanic\",\n \"words\": \"haujam\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Proto-Germanic *haujam n. 'hay', literally 'that which is (to be) mown', a *-jo- derivative of the verbal root *hawwan- 'to hew' (< PIE *keh₂u-, with the regular Grimm shift k > h and PIE *-u- surfacing as Germanic -aww-/-au-). The word is directly attested as Gothic hawi, Old Norse hey, Old Saxon hōi, Old High German houwi/hewi (> German Heu), Old English hīg/hēg. Watkins's AHD appendix gives the form in exactly Nourai's shape and with exactly his gloss ('Germanic *haujam in Old English hieg, hay, cut grass'), so the box is a straight quotation of his cited source.\",\n \"derivation_fa\": \"ژرمنی آغازین *haujam «علف درویده، کاه» از ستاک فعلی *hawwan- «بریدن، تراشیدن» با پسوند *-jo- ساخته شده و معنای تحت‌اللفظی آن «آنچه دروده می‌شود» است. در گذار همخوان‌های ژرمنی (قانون گریم) کـ هندواروپایی به h بدل شده است. گوتی hawi، نروژی باستان hey، آلمانی باستان houwi (> Heu) و انگلیسی کهن hēg بازماندهٔ آن‌اند. واتکینز در پیوست AHD دقیقاً همین صورت و همین معنا را آورده؛ ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/hay\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 (AHD_watkins1985.txt line 591), s.v. kau-²: '3. Germanic *haujam in Old English hieg, hay, cut grass: HAY.' Word, language label and gloss are Watkins's own.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 535\", \"stance\": \"supports\",\n    \"note\": \"'ahd. houwan, ags. hēawan, aisl. hȩggua „hauen“ (dazu als „zu Hauendes“ got. usw. hawi „Heu“)' — Pokorny derives the 'hay' noun from the 'hew' verb of this root, as the chart does.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein, Comprehensive Etym. Dict. of English, s.v. hay, n., grass mown (KLN_1966.txt line 17325)\", \"stance\": \"supports\",\n    \"note\": \"'hay, n., grass mown. — ME. haye, hey, fr. OE. hieg, hig, heg, rel. to OS. hoi, ON. hey ... OHG. houwi, hewi ... Goth. hawi, “hay”, lit. “that which is to be cut”, or “that which is cut”. Cp. OE. hēawan, “to cut”, and see hew.'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict., s.v. Hay (SKT.txt line 8478)\", \"stance\": \"supports\",\n    \"note\": \"'Hay. (E.) M.E. hey, A.S. hīg. + Du. hooi, Icel. hey, Dan., Swed. hö, Goth. hawi “grass”; G. heu. Properly “cut grass”; from the verb to Hew; see Hew.'\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 4,\n \"lang\": \"English\",\n \"words\": \"hay; hoe\",\n \"verdict\": \"plausible\",\n \"derivation\": \"'hay' is exactly right: Old English hīg / hēg / hieg 'grass cut for fodder' < PGmc *haujam, Middle English hey > modern hay; the arrow from the Germanic box is correct. 'hoe' is a different route within the same root and does NOT come from *haujam: Middle English (mid-14c.) howe, from Old French houe (12c.), borrowed from Frankish *hauwa 'mattock', a noun to Proto-Germanic *hawwan- 'to hew' (compare Old High German houwa 'hoe, mattock, pick-axe', German Haue). So hoe reaches English through Romance from a West Germanic sibling of *haujam, not from *haujam itself; Watkins keeps the two apart under kau-² ('1.c. Old French houe, a hoe: HOE' vs '3. Germanic *haujam ... HAY'). The node is therefore right about the ultimate root but draws one of its two words under the wrong parent.\",\n \"derivation_fa\": \"واژهٔ hay درست در جای خود است: انگلیسی کهن hēg/hieg از ژرمنی آغازین *haujam و از راه انگلیسی میانه hey به صورت کنونی رسیده است. امّا hoe «کج‌بیل» از *haujam نیست؛ این واژه در سدهٔ چهاردهم میلادی از فرانسوی کهن houe وام گرفته شده و آن خود وام‌واژه‌ای است از فرانکی *hauwa، از ستاک ژرمنی *hawwan- «بریدن» (قس: آلمانی باستان houwa، آلمانی Haue). پس ریشهٔ پایانی یکی است ولی مسیر جداست و در نمودار زیر پدرِ نادرست نشسته است؛ ادعا با احتیاط پذیرفتنی است.\",\n \"sources\": [\"https://www.etymonline.com/word/hay\", \"https://www.etymonline.com/word/hoe\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"The node carries no reference of its own in the book; it inherits the AHD citation of its Germanic parent, which was checked there (Watkins kau-² covers both HAY and HOE, but assigns them to different Germanic bases).\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Etymonline/Klein, s.v. hay and hoe\", \"stance\": \"partial\",\n    \"note\": \"Etymonline s.v. hay: 'Old English heg (Anglian), hieg, hig (West Saxon) “grass cut or mown for fodder”, from Proto-Germanic *haujam, literally “that which is cut” ... (from PIE *kau- “to hew, strike”)'. s.v. hoe: '“implement for digging...”, mid-14c., from Old French houe (12c.), from Frankish *hauwa, from Proto-Germanic *hawwan ... from PIE *kau- “to hew, strike”.' Same root, different Germanic base and a Romance transit for hoe.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, s.v. Hoe (SKT.txt line 8745)\", \"stance\": \"supports\",\n    \"note\": \"'Hoe: see Hew.' Skeat likewise refers hoe to the 'hew' verb, not to the 'hay' noun.\"}\n ]\n})\n\ndoc[\"entries\"].append(e0)\n\n# ------------------------------------------------------------------ entry 1\ne1 = {\n \"entry\": 1,\n \"root\": \"Kau 2, Qau 2, Kâukos\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *kāu-, *kēu-, *kū- 'to howl, cry out' (onomatopoeic), with the bird-name derivative *kauā / *kāukos 'a raucous bird'; Pokorny IEW 535 f., Walde-Pokorny I 331 f., Watkins/AHD kau-¹, Mann IEC 483\",\n \"note\": \"The root itself is real and the gloss is a fair translation of the standard entries: Pokorny heads it 'kāu-, kēu-, kū- „heulen“; kauā „schreiender Vogel“; Schallwurzel, teils mit anlaut. ḱ, teils mit k', and Mann's IEC p.483 has both 'kāukos, is, ā (kauk-) “a raucous bird”' and (p.481) 'kaukos (1) “shriek, howl, clamour, call”' — which is where Nourai's third root-name Kâukos comes from, and why the gloss combines 'to howl' with 'a raucous bird'. His IEC:483 citation is exact. His second citation, POK:434, is WRONG: Pokorny p.434 is in the middle of the *ghel- articles ('2. ghel- „schneiden”?', 'ghelā „Wein”??', 'gheldh- „begehren”'); the howl root stands on pp.535-536, i.e. on the same page as the 'strike' root of the previous chart — the very coincidence that presumably made Nourai reach for a different number here. Watkins confirms the page: '[Pok. kau- 535.]'.\",\n \"note_fa\": \"ریشه واقعی است و معنا درست: پوکورنی مدخل را «kāu-, kēu-, kū- «زوزه کشیدن»؛ kauā «پرندهٔ پر‌صدا»، ریشهٔ آوایی» می‌نویسد و من (IEC) در صفحهٔ ۴۸۳ مدخل «kāukos ‹a raucous bird›» را دارد — همین است خاستگاه نام سوم جعبه (Kâukos). پس ارجاع IEC:483 دقیق است، امّا POK:434 نادرست است: صفحهٔ ۴۳۴ پوکورنی در میانهٔ مدخل‌های *ghel- است و این ریشه در صفحهٔ ۵۳۵–۵۳۶ قرار دارد؛ واتکینز نیز می‌نویسد [Pok. kau- 535]. این خطای چاپی/ارجاعی کتاب است و به درستی خود ریشه آسیب نمی‌زند.\",\n \"sources\": [W + \"%DA%A9%D8%A8%DA%A9\"],\n \"ref_check\": [\n   {\"ref\": \"IEC:483\", \"status\": \"supports\",\n    \"note\": \"Mann, An Indo-European Comparative Dictionary, p.483 (IEC.txt line 6902): 'kāukos, is, ā (kauk-) “a raucous bird”. WP I, 331. Skt. kókaḥ (2) “red goose, cuckoo”; Hind. koki “crow”; Sind. kok “cuckoo; frog”; Per. kabg “partridge”; ... Gk. kēux, gs kēukos “a gull” ... Cz. kavka, Pol. kawka “daw” ...' — the root name, the gloss and the Persian word of the next node all stand on this one page.\"},\n   {\"ref\": \"POK:434\", \"status\": \"not_found\",\n    \"note\": \"POK_02.txt: the page marked '434' carries 'ghlād- ... 2. ghel- „schneiden“??, ghelā „Wein“??, gheldh- „begehren“' — nothing about howling or birds. The article Nourai means, 'kāu-, kēu-, kū- „heulen“; kauā „schreinder Vogel“; Schallwurzel', is on pp.535-536, immediately after the 'hauen, schlagen' root of his previous chart. Watkins cites it as '[Pok. kau- 535.]'. The page reference in the book is simply wrong.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 535-536\", \"stance\": \"supports\",\n    \"note\": \"'kāu-, kēu-, kū- „heulen“; kauā „schreinder Vogel“; Schallwurzel ... Ai. kāuti „schreit“ ... gr. κω-κῖ-ω „schreie, wehklage“ ... lit. kaukiù, kaũkti, lett. kāukt „heulen, von Hunden oder Wölfen“ ... Mit -r-: ai. cakóra- m. „eine Art Rebhuhn“ ... WP. I 331 f.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. kau-¹ (AHD_watkins1985.txt line 590)\", \"stance\": \"supports\",\n    \"note\": \"'kau-¹. To howl (imitative). 1. Reduplicated suffixed form *ka-kau-ro- in Sanskrit cakoraḥ, partridge: CHUKAR. 2. Reduplicated form *kō-kū-o- in Greek kōkuein, to wail, lament: COCYTUS. [Pok. kau- 535.]'\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 331 f.\", \"stance\": \"supports\",\n    \"note\": \"WLD_Bd1_pages.txt p.331: 'kau-, keu-, ku- = Schallwz., teils mit ḱ teils mit k. Ai. kāuti „schreit“, Intens. kokilyate ... arm. kuk ... gr. κω-κύ-ω „schreie, wehklage“ ...' — the same article Pokorny abridges on p.535.\"}\n ],\n \"nodes\": []\n}\n\ne1[\"nodes\"].append({\n \"id\": 1,\n \"lang\": \"Persian\",\n \"words\": \"kabk «کبک»\",\n \"verdict\": \"plausible\",\n \"derivation\": \"کبک kabk 'partridge' is inherited, not borrowed: Middle Persian kpk' /kabk/ 'partridge' > New Persian kabk (Arabic borrowed it back as قبج qabj, which Mo'in duly marks 'معرّب کبک'). The disputed step is the one Nourai draws, from the onomatopoeic IE root. Mann does assign it there — IEC 483 lists 'Per. kabg “partridge”' among the reflexes of *kāukos 'a raucous bird' — and the phonetics work (*kau-k- > Ir. *kap-ka-/*kabka- with the usual -u- > -p/b- before a stop is however NOT regular, which is why others hesitate). Horn (no. 841) sets the Persian word beside Skt. kapiñjala- 'francolin' and Bal. kabg but says its relation to Greek κακκάβη, Armenian kaẵaw and Syriac qaqqewā 'partridge' 'ist unklar'; Wiktionary traces it only to Middle Persian kabk and merely says 'Compare Ancient Greek κᾰκκᾰ́βη'. All of these are transparently imitations of the bird's call, so grouping them under an onomatopoeic *kau- is reasonable but not demonstrable by sound law — hence 'plausible' rather than 'confirmed'.\",\n \"derivation_fa\": \"«کبک» واژه‌ای ارثی است نه وام‌واژه: فارسی میانهٔ kabk > فارسی نو کبک؛ عربی آن را به صورت معرّب «قبج» وام گرفته است (معین هم می‌نویسد «معرّب کبک»). امّا پیوند آن با ریشهٔ آوایی *kāu- قطعی نیست: من در صفحهٔ ۴۸۳ آن را ذیل *kāukos آورده، ولی هرن (شمارهٔ ۸۴۱) نسبت آن را با یونانی κακκάβη، ارمنی kaẵaw و سریانی qaqqewā «ناروشن» می‌داند و ویکی‌واژه تنها تا فارسی میانه عقب می‌رود. چون همهٔ این صورت‌ها آشکارا تقلید آوای پرنده‌اند، نهادنِ آن‌ها زیر یک ریشهٔ آوایی پذیرفتنی است ولی با قانون آوایی اثبات‌پذیر نیست؛ پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [W + \"%DA%A9%D8%A8%DA%A9\"],\n \"ref_check\": [\n   {\"ref\": \"IEC:1521\", \"status\": \"not_found\",\n    \"note\": \"IEC.txt p.1521 (line 20085 ff.) is deep in the u- section — 'uers- (1) “droplet, sprinkling, shower” ... uersō (2) “drag, trail”' — with nothing about partridges. Mann's Persian kabg is on p.483, s.v. kāukos, the same page Nourai cites for the root box. '1521' has evidently been copied across from the sister node's AHD:1521.\"},\n   {\"ref\": \"MON:2888\", \"status\": \"partial\",\n    \"note\": \"Mo'in, Farhang-e Farsi, s.v. کبک (MON_part2.txt line 20094 of the 2-vol reprint): 'کبک: kabk [= دراج — معرّب قبج] (ا.) (جان.)' followed by a long natural-history description ('حجل، قبج، کبک معمولی؛ ج کبکان ... کبک دری'). Mo'in has the word with exactly Nourai's gloss but offers no Indo-European derivation, so he supports the word and not the arrow. (The 6-volume pagination Nourai cites could not be checked directly; only the 2-volume reprint is on disk.)\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 841, p.187\", \"stance\": \"partial\",\n    \"note\": \"'841. kebk „Rebhuhn“, arab. LW. qabj, qabjat. vergl. skr. kapiñjala- „Haselhuhn“; bel. kawinjar ... LW. kurd. keū, qew; ... afḡ. kabk; bel. kabg, n. kawg. ‚Eine starke Verstümmelung‘ der sansk.-bel. Formen (Geiger) kann das neupersische Wort nicht sein; in der Stammsilbe (kebk aus *kapak) sind sie aber gewiss identisch (etwa auch mit kebūter?). Ihr Verhältniss zu gr. κακκάβη, arm. kaẵaw, syr. qaqqewā, alle ‚Rebhuhn‘ (Hübschmann, ZDMG. 46, 241 No. 60), ist unklar.' Horn reconstructs *kapak, does not reach an IE root, and warns the wider comparison is unclear.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann p.483, s.v. kāukos\", \"stance\": \"supports\",\n    \"note\": \"'... Per. kabg “partridge” ...' listed among the reflexes of the 'raucous bird' root — the only book on the shelf that actually makes Nourai's connection.\"},\n   {\"src\": \"POK\", \"where\": \"IEW 535 f.\", \"stance\": \"silent\",\n    \"note\": \"Pokorny's article on the 'heulen' root lists Indic, Greek, Baltic, Slavic, Celtic and Germanic bird-names but no Iranian or Persian form.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 2,\n \"lang\": \"Sanskrit\",\n \"words\": \"cakôra\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Sanskrit चकोर cakóra- m. 'the Greek partridge / chukar (Alectoris chukar)' is a reduplicated r-derivative of the onomatopoeic root: PIE *ka-kau-ro- > Indo-Aryan *ca-kāu-ra- > cakóra-, with the regular Indic palatalisation of the reduplicating k- before the front vowel of the reduplication (satem *k > ċ) and the -r- suffix that Pokorny lists for this root. The word travelled onward: Sanskrit cakóra- > Hindi/Urdu cakor > English chukar (19th c., an Anglo-Indian bird-name). Pokorny puts the form exactly here — 'Mit -r-: ai. cakóra- m. „eine Art Rebhuhn“' — alongside Latin caurīre 'to cry (of a panther in heat)' and OCS kurŭ 'cock', so the arrow is standard doctrine.\",\n \"derivation_fa\": \"سنسکریت cakóra- «گونه‌ای کبک» صورتی مضاعف (با تکرار هجا) و دارای پسوند -r- از همان ریشهٔ آوایی است: *ka-kau-ro- > *ca-kāu-ra- > cakóra-، که در آن کـ نخست طبق قاعدهٔ زبان‌های ستم پیش از واکهٔ پیشین به چ بدل شده است. پوکورنی در صفحهٔ ۵۳۵ همین صورت را ذیل «Mit -r-» آورده و واتکینز نیز آن را *ka-kau-ro- بازسازی کرده است؛ پس ادعای نورایی درست است. همین واژه از راه هندی cakor به انگلیسی chukar راه یافته است.\",\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/kewh₂-\"],\n \"ref_check\": [\n   {\"ref\": \"AHD:1521\", \"status\": \"supports\",\n    \"note\": \"The 1975 AHD 'Indo-European Roots' appendix occupies pp.1505-1550, so p.1521 falls squarely in the k- roots; the entry itself (identical in Watkins's 1985 stand-alone edition, AHD_watkins1985.txt line 590) reads: 'kau-¹. To howl (imitative). 1. Reduplicated suffixed form *ka-kau-ro- in Sanskrit cakoraḥ, partridge: CHUKAR.' Word, language, gloss and derivation are Watkins's.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 535 f.\", \"stance\": \"supports\",\n    \"note\": \"'Mit -r-: ai. cakóra- m. „eine Art Rebhuhn“; lat. caurīre „schreien, vom brünstigen Panther“; aksl. kurŭ „Hahn“, ksl. kurica „Henne“.'\"},\n   {\"src\": \"IEC\", \"where\": \"Mann p.483 (kāukos) and p.481 (kaukos 1)\", \"stance\": \"partial\",\n    \"note\": \"Mann lists the bird-names of this root (Skt. kókaḥ, Gk. kēux, Lith. kaukýs 'a shrill bird', Latv. kaukis) but does not himself cite cakóra-; a compatible picture without the specific form.\"}\n ]\n})\n\ndoc[\"entries\"].append(e1)\njson.dump(doc, open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p245/part1.json','w'), ensure_ascii=False, indent=1)\nprint(\"ok\", len(doc[\"entries\"]))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p245/build.py"
}
```


### [2026-09-06T16:08:47.712Z] TOOL RESULT

```
Exit code 1
  File "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p245/build.py", line 46
    کورنی دیده نمی‌شود (ظاهراً آمیزه‌ای است از kau- و سنسکریت kuṣṇáti). «θβaxša» نیز واژهٔ اوستایی راستینی است به معنای \u00a bچالاک، کوشا»، امّا بارتولومه آن را هم‌ریشهٔ سنسکریت tvakṣ- می‌داند (ریشهٔ *tweḱs-)، نه *keh₂u-؛ پس گذاشتن آن در این جعبه خطای نورایی است که فقط به دلیل همانندی معنایی با «کوشیدن» صورت گرفته است.",
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 5133-5137: truncated \uXXXX escape
```


## [2026-09-06T16:08:52.415Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p245; python3 - <<'EOF'\nimport io\np='build.py'\ns=io.open(p,encoding='utf-8').read()\ns=s.replace('\\\\u00a bچالاک، کوشا»','«چالاک، کوشا»')\nio.open(p,'w',encoding='utf-8').write(s)\nEOF\npython3 build.py"
}
```


### [2026-09-06T16:08:54.467Z] TOOL RESULT

```
ok 2
```


## [2026-09-06T16:12:18.068Z] TOOL CALL #74: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p245/build2.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\nW = \"https://en.wiktionary.org/wiki/\"\ndoc = json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p245/part1.json'))\n\nBAILEY = (\"Bailey, Dictionary of Khotan Saka (1979) s.v. kavūta- (ISS_alt_DKS.txt line 1396): \"\n \"'kavūta- “blue, gray”, Z 22:154 ne atä haryāsa ne atä śśāttana ne atä stauru kavūta \"\n \"“(of the emperor's wife) not very black, not very white, not severely grey”. From kapauta- \"\n \"“blue, grey”, O.Pers. kapautaka-, Greek-Pers. καπαυτα, Zor.P. kapōt, kapōtar “pigeon”, \"\n \"N.Pers. kabūd, kabōtar, Armen. lw kapoyt, kapowtak, Armen.-Lat. capotes, Sogd. kp'wtk “blue”, \"\n \"kp'wt'yčh, Man. kypwtyč “pigeon”, Yaγn. kapūta “dove”, Balōčī kapōt, ... O.Ind. kapōta- “dove”, \"\n \"kapotaka- “grey”. Base kap- “grey” also in O.Ind. kapila-, kapiśa- “reddish”, kapi- “monkey”, \"\n \"Zor.P. kapik “monkey”.'\")\n\ne3 = {\n \"entry\": 3,\n \"root\": \"Kavŭta\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"Old Iranian *kapauta- 'blue-grey' (adj.), extended *kapautaka-; Proto-Indo-Iranian *kapáwtas; the Khotan Saka reflex is kavūta-\",\n \"note\": \"The material of this chart is entirely real and it is copied from a first-class source — H. W. Bailey. What Nourai has done is put a DAUGHTER form in the root box. Bailey's own entry (in his Dictionary of Khotan Saka, the published successor of the Indo-Scythian Studies volume Nourai cites) reads 'kavūta- “blue, gray” ... From kapauta- “blue, grey”, O.Pers. kapautaka-, ...': kavūta- is the Khotanese outcome (Iranian intervocalic -p- > Khotanese -v-, and the diphthong -au- monophthongised to -ū-), and the common ancestor of everything else in the chart is *kapauta-, not kavūta-. Wiktionary reconstructs Proto-Iranian *kapawtakáh / Proto-Indo-Iranian *kapáwtas 'grey-blue'. The language label 'Indo-Schythian' (so spelt, 13 times in the book, and so printed on p.215) is Nourai's shorthand taken from the title of Bailey's series 'Indo-Scythian Studies'; the language actually meant is Khotan Saka, an Eastern Iranian (Saka/Scythian) language, so the label is loose but not simply false. The gloss 'gray, dark blue' is Bailey's own 'blue, gray'. Verdict: the etymon is confirmed, the direction of the top arrow is not, hence 'plausible'. The chart's NOTE reporting that CEL6:46 derives kabŭtar from an Indo-European 'Kepro: a kind of bird' has no support anywhere: Bailey, Horn (no.842), Kent (p.178), MacKenzie, Mo'in and Wiktionary all derive kabūtar from *kapauta- 'blue-grey' (the bird named from its colour), and Gupta's Comparative Etymologic Lexicon is not a standard reference and is not available even in catalogue form for checking.\",\n \"note_fa\": \"مادهٔ این نمودار یکسره درست و برگرفته از منبعی درجه‌یک (هَرُلد بیلی) است، امّا نورایی صورتی فرزند را در جعبهٔ ریشه نشانده است. بیلی خود می‌نویسد: «kavūta- «آبی، خاکستری» ... از kapauta-، پارسی باستان kapautaka-، ...»؛ یعنی kavūta- بازتاب ختنی است (پ ایرانی در میان دو واکه در ختنی به و بدل شده و دوواکهٔ au به ū تک‌واکه گشته) و نیای مشترکِ همهٔ صورت‌های این نمودار *kapauta- است نه kavūta-. ویکی‌واژه ایرانی آغازین *kapawtakáh و هندوایرانی آغازین *kapáwtas «کبود، خاکستری‌آبی» را بازسازی می‌کند. برچسب «Indo-Schythian» (که سیزده بار در کتاب و در همین صفحهٔ ۲۱۵ چاپ شده) کوته‌نوشتِ خود نورایی از عنوان مجموعهٔ بیلی «Indo-Scythian Studies» است و زبان موردنظر ختنی‌سکایی است، پس برچسب سست است نه نادرست. دربارهٔ یادداشت نمودار (که CEL6:46 «کبوتر» را از «Kepro» می‌گیرد): هیچ منبعی آن را تأیید نمی‌کند؛ بیلی، هرن (۸۴۲)، کنت (ص ۱۷۸)، مکنزی، معین و ویکی‌واژه همگی کبوتر را از *kapauta- «کبود» می‌دانند، یعنی پرنده به نام رنگش خوانده شده است.\",\n \"sources\": [W + \"%DA%A9%D8%A8%D9%88%D8%AF\", W + \"%DA%A9%D8%A8%D9%88%D8%AA%D8%B1\"],\n \"ref_check\": [\n   {\"ref\": \"ISS:43\", \"status\": \"partial\",\n    \"note\": \"Bailey's Indo-Scythian Studies VI (1967) itself is not obtainable; the substitute on disk is the same author's Dictionary of Khotan Saka (1979), which is the mature form of the same lexicon. \" + BAILEY + \" Every single node of Nourai's chart — Old Persian, Pahlavi, Persian, Sogdian, the Armeno-Latin capotes, the Greek καπαυτα and Sanskrit kapota- — comes from this one entry, so the citation is substantively right; but Bailey derives kavūta- FROM kapauta-, whereas Nourai makes kavūta- the source. Page 43 of ISS could not be verified as such.\"}\n ],\n \"consulted\": [\n   {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, DKS p.55 s.v. kavūta-\", \"stance\": \"partial\",\n    \"note\": BAILEY},\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon p.178\", \"stance\": \"supports\",\n    \"note\": \"'kapautaka- adj. “blue”, in kāsaka hya kapautaka “lapis lazuli”: deriv. (§146.II) of stem in Phl. kapōt, NPers. kabōd “gray-blue”, Skt. kapóta- “pigeon, pigeon-color, gray”. kapautaka nsm. DSf 37.' (KNT.txt line 5242, after the page marker '178'.)\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 842, p.187\", \"stance\": \"supports\",\n    \"note\": \"'842. kebūter „Taube“ ..., kebūd „blau“ ... ai. kapota- „Taube; grau, bleigrau (taubenfarbig)“ ...; phlv. kapōtar „Taube“ ..., kapōt „blau“ ...; arm. LW. kapoit „blau“ ...; kurd. kewūk, kavōk, kōtir; afḡ. kavutar, kautar; bel. kapōt, kōntar; waḵ. kibit ...' — Horn's page is exactly the HRN:187 Nourai cites for the Pahlavi node.\"}\n ],\n \"nodes\": []\n}\n\ne3[\"nodes\"].append({\n \"id\": 1,\n \"lang\": \"Old Persian\",\n \"words\": \"kapautaka\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Old Persian 𐎣𐎱𐎢𐎫𐎣 k-p-u-t-k = kapautaka- is genuine and well placed, but it is an ADJECTIVE 'blue', not a word for 'dove'. It occurs once, in Darius's Susa foundation charter DSf 37: kāsaka hya kapautaka 'the blue semi-precious stone', i.e. lapis lazuli, brought from Sogdiana. Formally it is *kapauta- 'blue-grey' plus the very common Old Persian secondary suffix -ka- (Kent §146.II lists kapauta-ka- among his examples). The 'dove' half of Nourai's gloss belongs to the sister formation *kapauta- used as a bird-name (Skt. kapóta-, MP kapōtar), not to the attested Old Persian word. Directionally the node is also the one that should be in the root box (see the entry note), so it is right about the form and only loose about the meaning and its position.\",\n \"derivation_fa\": \"پارسی باستان kapautaka- واقعی است و جای آن در نمودار تقریباً درست، امّا صفت است به معنای «کبود/آبی» و نه نام پرنده. تنها یک بار در سنگ‌نبشتهٔ داریوش در شوش (DSf ۳۷) آمده است: kāsaka hya kapautaka «سنگ نیمه‌گرانبهای کبود»، یعنی لاجورد که از سغد می‌آوردند. ساخت آن *kapauta- «کبود» + پسوند ثانوی پرکاربرد -ka- است (کنت، بند ۱۴۶؍۲). معنای «کبوتر» در گلوسِ نورایی از آنِ ساخت خواهرِ آن (سنسکریت kapóta-، پهلوی kapōtar) است نه از آنِ واژهٔ گواه‌دار پارسی باستان؛ افزون بر این، همین صورت است که باید در جعبهٔ ریشه می‌نشست.\",\n \"sources\": [W + \"%DA%A9%D8%A8%D9%88%D8%AF\"],\n \"ref_check\": [\n   {\"ref\": \"ISS:43\", \"status\": \"partial\",\n    \"note\": \"Bailey (DKS s.v. kavūta-) lists 'O.Pers. kapautaka-' immediately after the base kapauta-, exactly as Nourai's node has it; but Bailey makes it a descendant of *kapauta-, not of Khotanese kavūta-. ISS p.43 itself not obtainable.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon p.178 (KNT.txt line 5242) and §146.II (line 1801)\", \"stance\": \"supports\",\n    \"note\": \"'kapautaka- adj. “blue”, in kāsaka hya kapautaka “lapis lazuli” ... kapautaka nsm. DSf 37.' §146.II lists 'kapauta-ka-' among the secondary -ka- formations. Kent gives no 'dove' sense for the Old Persian word.\"},\n   {\"src\": \"BRT\", \"where\": \"Bartholomae, Altiranisches Wörterbuch (grepped for kapauta-/kapaota-)\", \"stance\": \"silent\",\n    \"note\": \"No Avestan cognate found in AiW; the adjective is an Old Persian (and later Middle/New Persian) word, not attested in Avestan — which is why Nourai's chart, unusually, has no Avestan box here.\"},\n   {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, DKS s.v. kavūta-\", \"stance\": \"supports\",\n    \"note\": \"'From kapauta- “blue, grey”, O.Pers. kapautaka- ...'\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 2,\n \"lang\": \"Pahlavi\",\n \"words\": \"kapôt, kapôtar\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Both Middle Persian forms are attested and MacKenzie transcribes them kabōd and kabōtar: Book Pahlavi kpwt' /kabōd/ 'grey-blue; pigeon' and kpwtl (Manichaean kbwtr) /kabōtar/ 'pigeon'. kabōd continues Old Persian kapautaka- with the regular Middle Persian losses — post-tonic *-ka- dropped and intervocalic *-p- lenited to -b- (*kapautaka- > *kapōtak > kabōd, the final -d being the MP outcome of *-t- after a long vowel); kabōtar continues *kapauta- with the animal-name suffix *-tara-/-ar (or *kapautara-), likewise with p > b. Nourai's spellings kapôt / kapôtar are the older transliteration style (Horn's phlv. kapōt, kapōtar), so the node reproduces its cited source exactly rather than MacKenzie's normalisation.\",\n \"derivation_fa\": \"هر دو صورت فارسی میانه گواه‌دارند: مکنزی kabōd (نوشتهٔ kpwt') «کبود؛ کبوتر» و kabōtar (نوشتهٔ kpwtl، مانوی kbwtr) «کبوتر» می‌خواند. kabōd دنبالهٔ پارسی باستان kapautaka- است با دو دگرگونی قاعده‌مند: افتادن پسوند بی‌تکیهٔ -ka و نرم‌شدن پـ میان دو واکه به ب؛ kabōtar نیز از *kapauta- با پسوند نام‌جانوری -tar است. صورت‌نویسی «kapôt، kapôtar» در نمودار همان شیوهٔ کهن‌تر هرن است، پس گره دقیقاً منبع خود را بازتاب می‌دهد. ادعای نورایی درست است.\",\n \"sources\": [W + \"%DA%A9%D8%A8%D9%88%D8%AF\", W + \"%DA%A9%D8%A8%D9%88%D8%AA%D8%B1\"],\n \"ref_check\": [\n   {\"ref\": \"HRN:187\", \"status\": \"supports\",\n    \"note\": \"Horn, Grundriss der neupersischen Etymologie no. 842, p.187 (HRN.txt line 7326 ff., the marker '— 188 —' follows a few lines later): 'phlv. kapōtar „Taube“ (Papyrus, Horn, ZDMG. 43, 50), kapōt „blau“ (Men. 27, 50 “der blaue Wolf” ...)'. Nourai's two Pahlavi words, in Horn's own transliteration, on Horn's page 187.\"},\n   {\"ref\": \"KNT:178\", \"status\": \"supports\",\n    \"note\": \"Kent p.178 s.v. kapautaka-: 'deriv. of stem in Phl. kapōt, NPers. kabōd “gray-blue”' — Kent gives the Pahlavi form Nourai puts in this box and derives it from the Old Persian node above, which is exactly the arrow drawn.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary (PHD_mackenzie.txt lines 3120, 3122)\", \"stance\": \"supports\",\n    \"note\": \"'kabōd [kpwt' | N --] grey-blue; pigeon.' and 'kabōtar [kpwtl | M kbwtr, N --] pigeon.' The English-Pahlavi half of the same book has 'grey-blue kabōd' and 'pigeon kabōd, kabōtar'.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (Glossary) — grepped kapōt/kabōd\", \"stance\": \"silent\",\n    \"note\": \"No entry located in NYB_vol2_glossary.txt; the word does not occur in Nyberg's selection of texts.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn no. 842, p.187\", \"stance\": \"supports\",\n    \"note\": \"See ref_check: 'phlv. kapōtar „Taube“ ..., kapōt „blau“ ...; arm. LW. kapoit „blau“ (vergl. Bartholomae, BB. XVII, 101).'\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 3,\n \"lang\": \"Persian\",\n \"words\": \"kabŭd «کبود»; kabŭtar «کبوتر» (extra کفتر)\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"کبود kabūd 'blue, dark blue' < Middle Persian kabōd (kpwt') < Old Persian kapautaka- < Proto-Iranian *kapawtakáh; کبوتر kabūtar 'dove, pigeon' < Middle Persian kabōtar (kpwtl) < Old Persian *kapautah < Proto-Indo-Iranian *kapáwtas 'pigeon'. In both, the Middle Persian majhūl ō (from Old Iranian *au) is written with و and was still pronounced ō in classical Persian — Horn notes that Firdausī still rhymes kabūd with dūd — and only later merged with ū, which is why the modern pronunciation is kabūd/kabūtar. The chart's 'extra' form کفتر kaftar is the colloquial doublet with the regular sound-substitution b > f before t (kabtar > kaftar); Borhan-e Qate' cross-refers 'رک: کفتر' on the very page cited. The bird is named from the colour, not the colour from the bird: Mo'in states it outright.\",\n \"derivation_fa\": \"«کبود» از فارسی میانهٔ kabōd (نوشتهٔ kpwt')، از پارسی باستان kapautaka-، از ایرانی آغازین *kapawtakáh؛ و «کبوتر» از فارسی میانهٔ kabōtar، از پارسی باستان *kapautah، از هندوایرانی آغازین *kapáwtas «کبوتر». در هر دو، واو مجهول فارسی میانه (ō برخاسته از au ایرانی باستان) در فارسی دری هنوز ō تلفظ می‌شده — هرن یادآور می‌شود که فردوسی هنوز «کبود» را با «دود» قافیه می‌کند — و سپس با ū یکی شده است. صورت «کفتر» گونهٔ گفتاری با ابدال ب به ف پیش از ت است (kabtar > kaftar) و برهان قاطع در همان صفحه به آن ارجاع می‌دهد. معین نیز روشن می‌گوید که نام پرنده از رنگ آن گرفته شده است، نه برعکس؛ پس ادعای نورایی درست است و ادعای CEL6:46 (که «کبوتر» را از «Kepro» می‌گیرد) پذیرفتنی نیست.\",\n \"sources\": [W + \"%DA%A9%D8%A8%D9%88%D8%AF\", W + \"%DA%A9%D8%A8%D9%88%D8%AA%D8%B1\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:1589\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qate' ed. Mo'in, printed p.1589 (refs/ocr/BQT/1589.txt) carries the headwords کبود and کبوتر with Mo'in's etymological footnotes. For کبود, footnote 7: 'کردی kaw (آبی)، مازندرانی ...، گیلکی ...، اشکاشمی kavod (آبی) ... رک: کبوتر.' For کبوتر: 'هندی باستان kapōta- (کبوتر؛ خاکستری)، پهلوی kapōtar (کبوتر)، kapōt (کبود)، ارمنی kapoit (کبود)، کردی kavo/kawaw ...، بلوچی kapōt, kabōtar، وخی ...، سریکلی ... رک: اشتق‌هوبشمان'. The page also carries the cross-reference 'رک: کفتر' that matches the chart's extra form.\"},\n   {\"ref\": \"MON:2890\", \"status\": \"supports\",\n    \"note\": \"Mo'in, Farhang-e Farsi, s.v. کبوتر (MON_part2.txt line 20161 of the 2-vol reprint): 'کبوتر: [= کفتر؛ کبتری از ریشهٔ «کبود»، آبی] (ا.) (جان.) پرنده‌ای ...' — Mo'in derives kabūtar from the root کبود 'blue' and gives کفتر as its variant, i.e. exactly Nourai's box including the 'extra' form. (Only the 2-volume reprint is on disk, so the 6-volume page number 2890 could not be checked directly.)\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"Horn no. 842, pp.187-188\", \"stance\": \"supports\",\n    \"note\": \"'842. kebūter „Taube“ ..., kebūd „blau“ ... Im Neupersischen muss auch einmal ein Majhūl-vokal vorhanden gewesen sein; doch reimt schon bei Firdūsī kebūd auf dūd (I, S. 5 Vers 77), numūd ...' — Horn both derives the pair from Pahlavi kapōt/kapōtar and dates the ō > ū merger.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, s.v. kabōd, kabōtar\", \"stance\": \"supports\",\n    \"note\": \"'kabōd [kpwt'] grey-blue; pigeon', 'kabōtar [kpwtl | M kbwtr] pigeon' — the immediate Middle Persian ancestors.\"},\n   {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, DKS s.v. kavūta-\", \"stance\": \"supports\",\n    \"note\": \"'... Zor.P. kapōt, kapōtar “pigeon”, N.Pers. kabūd, kabōtar ...' — Bailey's own chain is Nourai's chain.\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 4,\n \"lang\": \"Sogdian\",\n \"words\": \"kp`wtk; kp`wt`yčh\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Both Sogdian words are in Gharib's dictionary with Nourai's glosses, and Gharib herself marks the first as an Old Persian loan. Buddhist Sogdian kp'wtk = kapōte 'blue, grey-blue' is entry 4795 with the express note '< OP kapautaka' — i.e. precisely the arrow Nourai draws from the Old Persian box; kp'wt'yčh = kapōte/ič 'dove, pigeon' (entry 4794, with Yaghnobi kapuči and Manichaean kypwtyč) is the same stem with the Sogdian diminutive/feminine suffix -č(ī). Sogdian also keeps the bare adjective kp'wt = kapōt 'blue, grey blue' (entry 4793). Note that in a strictly genealogical tree Sogdian would not descend from Old Persian at all — Gharib's '<OP' marks a loan from the Achaemenid chancery language into Eastern Iranian, and it is that borrowing, not inheritance, that the arrow really represents.\",\n \"derivation_fa\": \"هر دو واژهٔ سغدی در فرهنگ سغدی بدرالزمان قریب آمده و خود او kp'wtk (شمارهٔ ۴۷۹۵) را با نشانهٔ «< پارسی باستان kapautaka» آورده است، یعنی همان پیکانی که نورایی از جعبهٔ پارسی باستان کشیده. kp'wt'yčh «کبوتر» (شمارهٔ ۴۷۹۴، با یغنابی kapuči و مانوی kypwtyč) همان ستاک است با پسوند تصغیر/مؤنث سغدی -č(ī). سغدی صفت ساده kp'wt «کبود» را نیز دارد (شمارهٔ ۴۷۹۳). تنها نکته آنکه سغدی از پارسی باستان نیامده است؛ نشانهٔ «<OP» در فرهنگ قریب وام‌گیری از زبان دیوانی هخامنشی به ایرانی خاوری را نشان می‌دهد نه توارث.\",\n \"sources\": [W + \"%DA%A9%D8%A8%D9%88%D8%AF\"],\n \"ref_check\": [\n   {\"ref\": \"SOD:191\", \"status\": \"supports\",\n    \"note\": \"Gharib, Sogdian Dictionary, entries 4793-4795 (SOD.txt lines 39443-39458): '4793 kp'wt B — kapōt — blue, grey blue — TSP 3.32,47,101'; '4794 kp'wt'ych B — kapōte/ič ©Yaghn. kapuči — dove, pigeon — EGSii 85; GMS 1186n1; SCE 163,175,351'; '4795 kp'wtk B — kapōte ©<OP kapautaka — blue, grey blue — TSP 3.114,128,146'. Entry numbers 4793-4795 out of c.10,800 fall roughly 44% into the lexicon, which on a c.450-page dictionary lands at about p.190 — consistent with Nourai's SOD:191.\"},\n   {\"ref\": \"ISS:43\", \"status\": \"partial\",\n    \"note\": \"Bailey (DKS s.v. kavūta-) likewise lists 'Sogd. kp'wtk “blue”, kp'wt'yčh, Man. kypwtyč “pigeon”' — the very two forms of this node, in the same spelling. ISS p.43 itself not obtainable.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SOD\", \"where\": \"Gharib nos. 4793-4795\", \"stance\": \"supports\",\n    \"note\": \"'4795 kp'wtk ... kapōte ©<OP kapautaka ... blue, grey blue' — Gharib states the Old Persian source explicitly.\"},\n   {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, DKS s.v. kavūta-\", \"stance\": \"supports\",\n    \"note\": \"'... Sogd. kp'wtk “blue”, kp'wt'yčh, Man. kypwtyč “pigeon”, Yaγn. kapūta “dove” ...'\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 5,\n \"lang\": \"Latin\",\n \"words\": \"capotes\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The form is copied faithfully from Bailey, who lists 'Armen. lw kapoyt, kapowtak, Armen.-Lat. capotes' — and Nourai's parenthesis '(a Latin-Armenian word)' renders Bailey's 'Armen.-Lat.' exactly. But it is not a Latin word in any ordinary sense: capotes is the Latin-letter rendering of Armenian կապոյտ kapoyt 'blue' as it appears in the mediaeval Armenian-Latin glossaries, and Armenian kapoyt / kapowtak is itself an old borrowing from Iranian (Hübschmann; Wiktionary calls Old Armenian կապուտակ kaputak 'an Iranian borrowing'; Bartholomae, BB XVII 101, cited by Horn, says the same). So the word does go back to Iranian *kapauta-, as the arrow says, but the label 'Latin' overstates it, and it reaches Latin through Armenian rather than descending from the root independently. Accepted with that correction.\",\n \"derivation_fa\": \"این صورت درست از بیلی رونویسی شده است: بیلی می‌نویسد «ارمنی وام‌گرفته kapoyt، kapowtak؛ ارمنی‌ـ لاتین capotes» و پرانتز نورایی «واژه‌ای لاتین‌ـ ارمنی» ترجمهٔ همان است. با این‌همه، capotes به معنای متعارف واژه‌ای لاتین نیست؛ صورت لاتین‌نویسیِ ارمنی «կապոյտ kapoyt» (کبود) در واژه‌نامه‌های ارمنی‌ـ لاتین سده‌های میانه است، و خود kapoyt/kapowtak وام‌واژه‌ای کهن از ایرانی است (هوبشمان؛ بارتولومه BB XVII، ص ۱۰۱؛ ویکی‌واژه نیز կապուտակ را «وام‌واژه‌ای ایرانی» می‌خواند). پس بازگشت واژه به *kapauta- ایرانی درست است ولی برچسب «لاتین» بیش از اندازه است و راه رسیدنش وام‌گیری از ارمنی است نه توارث؛ با این اصلاح پذیرفتنی است.\",\n \"sources\": [W + \"%DA%A9%D8%A8%D9%88%D8%AF\"],\n \"ref_check\": [\n   {\"ref\": \"ISS:43\", \"status\": \"partial\",\n    \"note\": \"Bailey, DKS s.v. kavūta- (ISS_alt_DKS.txt line 1397): 'Armen. lw kapoyt, kapowtak, Armen.-Lat. capotes'. The form and Nourai's parenthetical label both come straight from here; Bailey classes it as Armeno-Latin, and the immediately preceding words show that Armenian itself has the word as a loanword ('lw'). ISS p.43 itself not obtainable.\"}\n ],\n \"consulted\": [\n   {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, DKS s.v. kavūta-\", \"stance\": \"supports\",\n    \"note\": \"'Armen. lw kapoyt, kapowtak, Armen.-Lat. capotes' — the only source for this form.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn no. 842, p.187\", \"stance\": \"partial\",\n    \"note\": \"'arm. LW. kapoit „blau“ (vergl. Bartholomae, BB. XVII, 101)' — Horn confirms that the Armenian word is a loanword from Iranian, which is what makes the 'Latin' node an Armenian-mediated form rather than an independent Latin reflex.\"},\n   {\"src\": \"LEW\", \"where\": \"Walde, Lateinisches etymologisches Wörterbuch (grepped 'capotes')\", \"stance\": \"silent\",\n    \"note\": \"No such headword in LEW_1910.txt — as expected: capotes is not part of the Latin lexicon proper.\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 6,\n \"lang\": \"Greek\",\n \"words\": \"kapauta\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The form is real and the arrow is right, but the parenthesis in the book is wrong. Bailey's entry reads 'Greek-Pers. καπαυτα' — a Graeco-Persian form, i.e. Old Persian kapauta- as transcribed in Greek letters (the kind of Iranian word preserved in Greek glossaries and in Greek-script Iranian material), not 'a Greek-Armenian word' as Nourai's box says; the '(Armeno-)' label belongs to the Latin node just above it, and has evidently slipped one line. Substantively the form is simply Old Persian *kapauta- 'blue-grey' in Greek dress, so it supports the same Iranian etymon; the gloss 'dove' is again transferred from the bird-name of the family rather than from this attestation, which is the colour word.\",\n \"derivation_fa\": \"صورت واقعی است و پیکان درست، امّا توضیح داخل پرانتزِ کتاب نادرست است. بیلی می‌نویسد «Greek-Pers. καπαυτα»، یعنی صورتی «یونانی‌ـ پارسی»: همان پارسی باستان kapauta- که به خط یونانی نوشته شده است؛ نه «واژه‌ای یونانی‌ـ ارمنی» که در جعبه آمده. برچسب «ارمنی» از گرهٔ لاتینِ بالای آن یک سطر لغزیده است. از نظر ماده، این صورت همان *kapauta- «کبود» ایرانی است و همان ریشه را تأیید می‌کند؛ معنای «کبوتر» نیز مانند گرهٔ پارسی باستان از نام پرندهٔ این خانواده به این‌جا کشیده شده، حال آنکه صورتِ گواه‌دار واژهٔ رنگ است. خطای برچسب از خود کتاب است.\",\n \"sources\": [W + \"%DA%A9%D8%A8%D9%88%D8%AF\"],\n \"ref_check\": [\n   {\"ref\": \"ISS:43\", \"status\": \"partial\",\n    \"note\": \"Bailey, DKS s.v. kavūta- (ISS_alt_DKS.txt line 1396): 'From kapauta- “blue, grey”, O.Pers. kapautaka-, Greek-Pers. καπαυτα, Zor.P. kapōt, kapōtar “pigeon” ...'. Bailey's label is 'Greek-Pers.', i.e. Graeco-Persian; the book's '(a Greek-Armenian word)' does not correspond to anything in the source. ISS p.43 itself not obtainable.\"}\n ],\n \"consulted\": [\n   {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, DKS s.v. kavūta-\", \"stance\": \"partial\",\n    \"note\": \"Supports the form καπαυτα and its Iranian origin, contradicts the 'Greek-Armenian' description: Bailey writes 'Greek-Pers. καπαυτα'.\"},\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian p.178\", \"stance\": \"supports\",\n    \"note\": \"Kent's entry for kapautaka- shows the Old Persian stem *kapauta- that the Greek transcription renders; he cites the Greek/Elamite/Akkadian evidence for the Susa charter in which the word occurs.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, IEC (grepped kapauta/kapotos)\", \"stance\": \"silent\",\n    \"note\": \"No Greek headword of this shape in Mann; καπαυτα is not part of the inherited Greek lexicon but a transcription of an Iranian word, consistent with Bailey's 'Greek-Pers.' label.\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 7,\n \"lang\": \"Sanskrit\",\n \"words\": \"kapôta\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Sanskrit कपोत kapóta- m. 'dove, pigeon' (already Rigvedic, RV 10.165, the 'dove' hymn) and the derived kapotaka- 'pigeon-coloured, grey' are the exact Indo-Aryan match of Iranian *kapauta-: Proto-Indo-Iranian *kapáwtas gives Indic kapóta- by the regular monophthongisation of *au > o, while Iranian keeps the diphthong (OP kapauta-ka-). Bailey and Kent both cite it in this function, and Bailey adds the wider base kap- 'grey' seen in Sanskrit kapila- 'tawny', kapiśa- 'reddish-brown' and kapi- 'monkey'. Strictly the word is a cognate of the Iranian forms, not a descendant of Khotanese kavūta-, but as a sister branch under the common etymon the node is correct.\",\n \"derivation_fa\": \"سنسکریت कपोत kapóta- «کبوتر» (که در ریگ‌ودا ۱۰؍۱۶۵ هم آمده) و صورت مشتق kapotaka- «به رنگ کبوتر، خاکستری» برابر دقیق ایرانی *kapauta- اند: هندوایرانی آغازین *kapáwtas در هندی باستان به kapóta- بدل شده، زیرا au در آن‌جا به o تک‌واکه می‌شود، حال آنکه ایرانی دوواکه را نگاه می‌دارد (پارسی باستان kapauta-ka-). بیلی و کنت هر دو همین برابری را می‌آورند و بیلی ستاک گسترده‌تر kap- «خاکستری» را در kapila-، kapiśa- و kapi- نیز نشان می‌دهد. به‌دقت، این واژه هم‌ریشهٔ صورت‌های ایرانی است نه بازماندهٔ ختنیِ kavūta-، ولی به عنوان شاخهٔ خواهر زیر ریشهٔ مشترک، گره درست است.\",\n \"sources\": [W + \"%DA%A9%D8%A8%D9%88%D8%AA%D8%B1\"],\n \"ref_check\": [\n   {\"ref\": \"ISS:43\", \"status\": \"partial\",\n    \"note\": \"Bailey, DKS s.v. kavūta-: 'O.Ind. kapōta- “dove”, kapotaka- “grey”. Base kap- “grey” also in O.Ind. kapila-, kapiśa- “reddish”, kapi- “monkey”, Zor.P. kapik “monkey”.' Exactly Nourai's word with exactly his double gloss 'dark blue, dove'. ISS p.43 itself not obtainable.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian p.178\", \"stance\": \"supports\",\n    \"note\": \"'... Skt. kapóta- “pigeon, pigeon-color, gray”' cited as the Indo-Aryan match of OP kapautaka-.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn no. 842, p.187\", \"stance\": \"supports\",\n    \"note\": \"'ai. kapota- „Taube; grau, bleigrau (taubenfarbig)“' heads Horn's article on kebūter/kebūd — the same equation.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' p.1589, Mo'in's footnote to کبوتر\", \"stance\": \"supports\",\n    \"note\": \"'هندی باستان kapōta- (کبوتر؛ خاکستری)' — Mo'in opens the etymology of کبوتر with the Sanskrit form.\"}\n ]\n})\n\ndoc[\"entries\"].append(e3)\njson.dump(doc, open('/home/sfmqrb/git/rishe/data/verification/page-245.json','w'), ensure_ascii=False, indent=1)\nprint(\"written\", sum(len(e[\"nodes\"]) for e in doc[\"entries\"]))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p245/build2.py"
}
```


### [2026-09-06T16:12:20.238Z] TOOL RESULT

```
written 13
```


## [2026-09-06T16:12:22.812Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -m json.tool data/verification/page-245.json > /dev/null && echo \"valid JSON\"; python3 tools/verify_check.py 245"
}
```


### [2026-09-06T16:12:24.486Z] TOOL RESULT

```
valid JSON
nodes verified: 13/13
node verdicts: {'disputed': 1, 'confirmed': 7, 'plausible': 5}
root verdicts: {'confirmed': 2, 'plausible': 1}
ref checks: {'supports': 10, 'partial': 8, 'not_checked': 1, 'not_found': 1}
books consulted: {'partial': 6, 'supports': 23, 'silent': 7} | by book: {'HRN': 6, 'ISS_alt_DKS': 5, 'POK': 4, 'PHD': 3, 'IEC': 3, 'KNT': 3, 'BRT': 2, 'CHEUNG': 2, 'KLN': 2, 'SKT': 2, 'NYB': 1, 'SOD': 1, 'LEW': 1, 'BQT': 1}
```


## [2026-09-06T16:12:31.095Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; head -c 20 data/verification/page-245.json | xxd | head -2; python3 -c \"\nimport json;d=json.load(open('data/verification/page-245.json'));print([e['entry'] for e in d['entries']]);print([ (e['entry'],[n['id'] for n in e['nodes']]) for e in d['entries']])\""
}
```


### [2026-09-06T16:12:33.062Z] TOOL RESULT

```
00000000: 7b0a 2022 7064 665f 7061 6765 223a 2032  {. "pdf_page": 2
00000010: 3435 2c0a                                45,.
[0, 1, 3]
[(0, [1, 2, 3, 4]), (1, [1, 2]), (3, [1, 2, 3, 4, 5, 6, 7])]
```


## [2026-09-06T16:12:52.265Z] AGENT

Page 245 (book p. 215) verified. `verify_check.py 245`: **0 PROBLEM lines**, 13/13 nodes.

**Counts** — nodes: 7 confirmed, 5 plausible, 1 disputed. Roots: 2 confirmed, 1 plausible. Ref checks: 10 supports, 8 partial, 1 not_found, 1 not_checked; 31 `consulted` entries across 14 books.

**Disputed / flagged**
- **Kau, Qau 1 — node #1 Avestan (`disputed`)**: `θβaxša "try"` belongs to a different root — Bartholomae glosses it "rührig, emsig, eifrig" to the verb θβaxš-, cognate with Skt. tvakṣ- (*tweḱs-/twerḱ-), not *keh₂u-. And `kau-kušati "tries, fights"` is unattested — absent from Bartholomae, Cheung, Buck and Walde-Pokorny. The other two words (kaoš-, frā kušaiti, Vend. 5.34) are correct.
- **Kau 2 — root ref `POK:434` is wrong** (`not_found`): Pokorny 434 is the *ghel- articles; the "heulen / raucous bird" root is on pp. 535-536 — the same page as Kau 1. Watkins cites "[Pok. kau- 535.]". `IEC:483` is exact ("kāukos … 'a raucous bird' … Per. kabg 'partridge'").
- **Kau 2 — node #1 `IEC:1521` is wrong** (`not_found`): IEC p. 1521 is the u- section (uers-…); Mann's Persian kabg is on p. 483. The number was evidently copied from the sister node's AHD:1521.
- **Kavŭta root (`plausible`)**: Bailey (DKS s.v. kavūta-) derives kavūta- **from** *kapauta-; Nourai has put the Khotan Saka daughter form in the root box. Proper etymon: OIr. *kapauta-, PIIr. *kapáwtas.
- **Kavŭta node #6 Greek (`plausible`)**: Bailey writes "**Greek-Pers.** καπαυτα" (a Graeco-Persian transcription of OP kapauta-); the book prints "(a Greek-Armenian word)" — the "Armenian" label has slipped one line from the Latin node above.
- **Kavŭta node #5 Latin (`plausible`)**: `capotes` is Bailey's "Armen.-Lat.", an Armenian word in Latin dress, not a Latin lexeme; Armenian kapoyt is itself an Iranian loan.
- **Kavŭta node #1 (`plausible`)**: OP kapautaka- is an adjective 'blue' (DSf 37, kāsaka hya kapautaka 'lapis lazuli'); the 'dove' half of the gloss belongs to the sister bird-name.
- The chart NOTE (CEL6:46 deriving kabŭtar from IE "Kepro") is unsupported: Bailey, Horn 842, Kent 178, MacKenzie, Mo'in and Wiktionary all give *kapauta- 'blue-grey'.

**Extraction errors: none.** The JSON is faithful to the printed page, including "Indo-Schythian" (Nourai's own spelling, 13× in the book) and "kau-kušati".

Side artefacts: `refs/ocr/BOOK/245.png`, `refs/ocr/BQT/{1589,1648,1731}.{png,txt}` plus a new `1648.vision.txt` (footnote 5 transcribed from the image, since tesseract mangled the Latin transliterations); 8 web pages archived via `fetch_source.py`.
