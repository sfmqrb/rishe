# Verification process log — verify-page-408


## [2026-09-14T00:53:15.434Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 408 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-408.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-408.json. Write /home/sfmqrb/git/rishe/data/verification/page-408.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 408` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T00:53:16.534Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T00:53:17.425Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T00:53:17.439Z] TOOL RESULT

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


## [2026-09-14T00:53:17.936Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-408.txt"
}
```


### [2026-09-14T00:53:17.958Z] TOOL RESULT

```
1	=== PDF page 408 (book page 378) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Pu 2 : to blow, swell  (refs POK:847)
4	#1 (parent #0) [Persian] refs=POK:847; HRN:75 | puk «پوک» : empty
5	#2 (parent #0) [Latin] refs=AHD | pustula : blister
6	  #3 (parent #2) [English] refs=None | pus ; pustule
7	--- entry 1 ---
8	ROOT Pu 3 -> redirect to Apo
9	--- entry 2 ---
10	ROOT [Indo-European] Pŭ 4, Peua : to decay, rot  (refs POK:848)
11	#1 (parent #0) [Avestan] refs=POK:849; SNS:137 | pu 2, pav, puyeiti : to decay ; pŭtay, pŭiti : rotten
12	  #2 (parent #1) [Pahlavi] refs=POK:849; SNS:137 | pŭsîtan : to rot ; pŭdag, pŭtak : rotten
13	    #3 (parent #2) [Persian] refs=BQT:425,429; FFD:44; BLY:73 | pŭsîdan «پوسیدن» : to rot ; pŭdeh «پوده» : rotten | extra: پوس | NOTE: This poem is about the wooden cross of Jesus.
14	#4 (parent #0) [Germanic] refs=AHD | fŭ-faz : rotten ; fŭlithô : foulness ; fausa : spongy, rotten
15	  #5 (parent #4) [English] refs=AHD | foul ; filth ; fuzzy
16	--- entry 3 ---
17	ROOT Pug -> redirect to Peuk
18	--- entry 4 ---
19	ROOT [Indo-European] Puk : bundled together  (refs POK:849)
20	#1 (parent #0) [Avestan] refs=POK:849; SOD:298 | pusâ : crown made of bundled twigs and flowers ; pusâ-ka : garland, crown
21	  #2 (parent #1) [Pahlavi] refs=MON:779 | pusag : crown
22	    #3 (parent #2) [Persian] refs=MON:779; FRS:146 | pasâk «پساک» : crown of flowers | extra: بساک
23	  #4 (parent #1) [Sogdian] refs=SOD:298 | ps`k : crown
24	#5 (parent #0) [Greek] refs=AHD | puknos : strong, thick, dense
25	  #6 (parent #5) [English] refs=AHD | pycnometer : a device for measuring density
26	#7 (parent #0) [Greek] refs=POK:849 | am-pus : headband
27	
```


## [2026-09-14T00:53:19.439Z] AGENT

I'll read the source JSON and reference index.


## [2026-09-14T00:53:20.671Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-408.json",
 "description": "Read source JSON page 408"
}
```


### [2026-09-14T00:53:20.718Z] TOOL RESULT

```
{
  "pdf_page": 408,
  "book_page": 378,
  "entries": [
    {
      "root": {
        "name": "Pu 2",
        "lang": "Indo-European",
        "refs": "POK:847",
        "gloss": "to blow, swell"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "POK:847; HRN:75",
          "words": [
            {"translit": "puk", "gloss": "empty", "script": "پوک"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "pustula", "gloss": "blister", "script": null}
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
            {"translit": "pus", "gloss": null, "script": null},
            {"translit": "pustule", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Pu 3", "redirect": "Apo"},
      "nodes": []
    },
    {
      "root": {
        "name": "Pŭ 4, Peua",
        "lang": "Indo-European",
        "refs": "POK:848",
        "gloss": "to decay, rot"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:849; SNS:137",
          "words": [
            {"translit": "pu 2, pav, puyeiti", "gloss": "to decay", "script": null},
            {"translit": "pŭtay, pŭiti", "gloss": "rotten", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "POK:849; SNS:137",
          "words": [
            {"translit": "pŭsîtan", "gloss": "to rot", "script": null},
            {"translit": "pŭdag, pŭtak", "gloss": "rotten", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:425,429; FFD:44; BLY:73",
          "words": [
            {"translit": "pŭsîdan", "gloss": "to rot", "script": "پوسیدن"},
            {"translit": "pŭdeh", "gloss": "rotten", "script": "پوده"}
          ],
          "script_extra": "پوس",
          "note": "This poem is about the wooden cross of Jesus.",
          "quote": {
            "text": "چو پور پدر رفت سوی پدر - تو اندوه این چوب پوده مخور",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "fŭ-faz", "gloss": "rotten", "script": null},
            {"translit": "fŭlithô", "gloss": "foulness", "script": null},
            {"translit": "fausa", "gloss": "spongy, rotten", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "foul", "gloss": null, "script": null},
            {"translit": "filth", "gloss": null, "script": null},
            {"translit": "fuzzy", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Pug", "redirect": "Peuk"},
      "nodes": []
    },
    {
      "root": {
        "name": "Puk",
        "lang": "Indo-European",
        "refs": "POK:849",
        "gloss": "bundled together"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:849; SOD:298",
          "words": [
            {"translit": "pusâ", "gloss": "crown made of bundled twigs and flowers", "script": null},
            {"translit": "pusâ-ka", "gloss": "garland, crown", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "MON:779",
          "words": [
            {"translit": "pusag", "gloss": "crown", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:779; FRS:146",
          "words": [
            {"translit": "pasâk", "gloss": "crown of flowers", "script": "پساک"}
          ],
          "script_extra": "بساک",
          "note": null,
          "quote": {
            "text": "چونکه یکی تاج و بساک ملوک - باز یکی کوفته آسیاست",
            "poet": "Kasâî"
          }
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "SOD:298",
          "words": [
            {"translit": "ps`k", "gloss": "crown", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "puknos", "gloss": "strong, thick, dense", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "pycnometer", "gloss": "a device for measuring density", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:849",
          "words": [
            {"translit": "am-pus", "gloss": "headband", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-14T00:53:22.675Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','HRN','AHD','SNS','BQT','FFD','BLY','SOD','MON','FRS','WLD','PHD','NYB','BRT','HUB','CHEUNG','KLN','SKT','IEC','SYN','ARY']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


### [2026-09-14T00:53:23.762Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/downloa
BLY {"title": "H. W. Bailey, 'Hvatanica II' (glossary of Khotanese words), BSOAS 9.1 (1937) pp. 69-78", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/bailey-studies-1930-1993 (Robert Bedrosian's open compilation \"Selected Writings of H. W. Bailey\"; Hvatanica II = PDF pp. 313-322)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sourc
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
FRS {"title": "Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/LughatEFurs-AbuMansurAliBinAhmadAsadiTusiFarsi (Abbas Eqbal's 1319/1940 Tehran edition); also dli.ernet.439493 / dli.ernet.437743 (Horn's 1897 Göttingen edition, 'Lughat Faras')", "lookup_hint": "Look up the headword (entries grouped by final letter); FRS_p
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
CHEUNG MISSING
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root,
```


## [2026-09-14T00:54:04.636Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -80",
 "description": "List local reference files"
}
```


### [2026-09-14T00:54:04.680Z] TOOL RESULT

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


## [2026-09-14T00:54:05.406Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '1,120p' data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T00:54:05.444Z] TOOL RESULT

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


## [2026-09-14T00:54:08.844Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"puk̑\\|pū̆-\\|ἄμπυξ\\|πυκνός\\|ampyx\" POK_full.txt | head -40",
 "description": "Grep Pokorny for puk entries"
}
```


### [2026-09-14T00:54:08.889Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T00:54:10.161Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"847\\|848\\|849\" POK_full.txt | head -20; echo ---; wc -l POK_full.txt POK_01.txt POK_02.txt POK_03.txt",
 "description": "Check Pokorny file structure"
}
```


### [2026-09-14T00:54:10.213Z] TOOL RESULT

```
3897:References: WP. I 34 f., WH. I 60, 848, Feist 18 f., Pedersen Hittitisch 128, Tocharisch 
6001:References: WP. I 45 f., WH. I 57 f., 60, 847, Pedersen Hittite 128, Couvreur H 93. 
6413:References: WP. I 82 f., II 362 f., WH. I 66, 848, Feist 25, Schwyzer Gr. Gr. I 260, 447, 
6503:References: WP. I 80 f., WH. 62 f., 848. 
7270:References: WP. I 42 f., WH. I 51, 847. 
8839:References: WP. I 849 f., WH. I 467, Feist 113 f., Sievers-Brunner 121, 243, Wackernagel- 
9347:References: WH. I 61, 65, 848, Feist 72, Trautmann 22, Pedersen Hittitisch 27, 164. 
9387:References: WP. I 42, WH. I 75 f., 849 f. 
20028:References: WP. I 849 f., WH. I 466 f., 469, 471 f., 864, Trautmann 49, Pedersen 
21240:References: WP. I 848. 
21350:References: WP. I 847 f., WH. I 565, 867, Trautmann 45 f. 
21387:References: WP. I 847, Benveniste BSL. 30, 73 f., Pisani REtlE. 1, 238 ff. 
25085:/?/- > -nn-), gr. 6vo(; etc. s. WH. I 72 f., 647, 849. 
29439:References: WP. I 162, WH. I 72, 849, Meillet Esquisse2 39. 
67517:See also: see below pu-1, S. 847. 
69174:Page(s): 846-847 
69195:Page(s): 847 
69217:Page(s): 849 
69260:Page(s): 849 
69338:Page(s): 847-848 
---
  93771 POK_full.txt
   5151 POK_01.txt
   6715 POK_02.txt
   5974 POK_03.txt
 111611 total
```


## [2026-09-14T00:54:13.015Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '69140,69360p' POK_full.txt",
 "description": "Read Pokorny entries pp.846-849"
}
```


### [2026-09-14T00:54:13.090Z] TOOL RESULT

```
Root / lemma: pfso- (?) 

Meaning: onion 

Note: is mediterranes loanword 

Material: Gr. Trpaaov ' leek ': Latin porrum, porrus ' leek '. 

In e-grade: 

Maybe alb. presh, pras ' leek ' : Rom. praz^ leek ' . 

References: WP. II 84, WH. II 343, Szemerenyi Gl. 33, 261 f. 

Page(s): 846 

Root / lemma: pster-, pstereu- 

Meaning: to sneeze 

Material: Armenian p'rngam, p'mcem^r\'\ese'; gr. nrapvuijai, nraipu) 'niese', nTapp6(; m., 

nT6po(; m. 'das Niesen' (with Inlautbehandlung the Aniautgruppe pst- : anocpGapa^aoGai 

'schnarchen' Hes.); Latin sternuo, -ere 'sneeze'; Old Irish sreod^6as Niesen', cymr. 

ystrew, trew6s., ystrewi, trem'6s., Middle Breton streuyaff, nbret. stref/a' sneeze' {*striw-). 

Maybe alb. (*psheterij) psheret/j" sIgW, tesht/j" sneeze'. 



References: WP. 11101, WH. II 591. 
Page(s): 846-847 



Root / lemma: ptel(e)ia 

Meaning: a kind of tree 

Material: Gr. nrsAsa, epidaur. nsAsa 'elm, RiJster' (latter with probably older 

Aniautsvereinfachung; unclear are TiAiai ' black poplar' Hes. and because of Aniauts 

ansAAov aiY£ipo(; Hes.); Latin ////a'Linde' (Middle Irish /e/fe derives from dem Engl.); 

Venetic FIN Tiliaventus? 

Armenian /'eZ/'elm' is loanword from nTsAsa; 

perhaps *ptel-eia^6\e Breitblattrige' or at most 'weit die Aste Breitende'. 

References: WP. II 84 f., WH. II 681 f., Pokorny KZ. 54, 307 f. 
Page(s): 847 

Root / lemma: puR-2 

Meaning: to enclose, put together 

Note: 

Root/ lemma: puR-2\ "to enclose, put together' derived from Root/ lemma: ku-, kus- 

{*k'^uk'^h-) : "to kiss' common Celtic - Greek - lllyrian k"'->p-. 

Material: Avestan pusa-i. " headband '; gr. a|j-nu^ m. " headband ', Adverb. nuKa "tight, 

firm, dense, sensible, wise, painstaking ', in compound nuKi- (nuKi-[jri5r|<; "sensible, wise'), 

out of it nuKi-voc; newer nuKvoc; "dense, tight, firm, proficient', nuKO^u) "make tight, firm, 

wrap dense'; alb. puth^kusse', actually "umarme'. 

References: WP. II 82, J. B. Hofmann, Gr. etym. Wb. 290. 

Page(s): 849 

Root / lemma: pu-lo- 

Meaning: hair 

Note: 

Root / lemma: pi-lo- : hair' : Root / lemma: pu-lo- : hair' derived from Root / lemma: pleuk- 

: "flake, feather, hair' common consonant + cosnonant > consonant + vowel recorded in 

centum languages first, mainly Latin. 

Material: Old Indie pu/a-, pulaka- m. "das Strauben the Harchen am body', pulastf- m. 

"schlichtes hair of the head bearing, carrying'; Substantiv " hair of the head ', Patronymikon 



Paulastya-; gr. Plur. ttuAiyY£<^ "hair am Hintern, curls ' Hes.; Middle Irish i//"beard' {*pulu-), 
u/ach' bearded', ulchai. "beard', U/a/c/'d'\e Leute from Ulster' {*U/ut/}. 
References: WP. II 84, G. Liebert Nominalsuffix -f/- 191. 
Page(s): 850 

Root / lemma: puk-1, peuk- 
Meaning: thick-haired, *fox 

Material: Old \x\d\c puccha-, -/77"tail, member, rod' (kann *pufkJ-sko- se'in); after dem 
buschigen Schwanz named, seems Gothic fauho. Old Icelandic foa. Old High German 
foha^ vixen ' (Germanic -on), besides with masc. -s-: Old English fox. Old High German 
fuhslox' etc.; Lithuanian paustis " animal hair '; russ.-poln. puch ( *peukso-, poukso-) 
"Flaumfedern, Daunen, fine woolen Haar an animals' (out of it Lithuanian pukas 
Tlaumfeder'), russ. pus/styj l\eecY, dense, buschig', pusnoj tovar'Pe\z\Nerk', Czech- 
Lower Serbian o-pus{*puchb), opys'iaW, russ. opuska, opus/na'edge (of Waldes), hem, 
Verbramung'. 
Note: 

Alb. suggests that Root/ lemma: puk-1, peuk-: (thick-haired, *fox) is a reduced root of 
older Latin volpes 'fox', gr. alopex a fox. Root / lemma: alp-, lup- : [a kind of carnivore (fox, 
wolf)]. 

References: WP. II 82f. 
Page(s): 849 

Root / lemma: pu-1, peu- pou- a\so phu- 
Meaning: to blow, blow up 

Material: Old Indie /0/7^p'/0/7i//ra/'a/ra-"keuchend' (Lex.), pupphula-^E\a\\uuq' (Lex.), 
phuphusa-, -/77' lung ', pupphusa-^ lung, Samenkapsel the Wasserrose' (Lex.), phut-karoti 
"blows, pustet, shouts, howls from vollem neck'; Armenian (/7)c»^/" breath, breeze, breath, 
soul' {*pouio-), hevarshoxi or heavy breathe' {*peua-), /7oy//r"congregation, meeting, 
troop'; Middle Irish uan^scuxw, froth, foam' = cymr. ewyn, bret. eon ds. {*pou-ino-), PI. eien 
"Ouellen' (compare Lithuanian pi/Za'Schaumblase'); abret. e^o/70c"schaumend'; Latvian 
pu/Zs^heap, herd, nest, Strichregen', pCi/udt' fester ', pJ/'/'Regenwolken', russ. pu/Ja, kir. 
pu/'a'baW; 

Lithuanian pure' tassel ', Latvian paurs, yOa^Ae'Hinterhaupt, cranium; acme, apex ' 
("bulge '), Lithuanian puras ' measure of capacity ', Latvian purs ' measure of capacity for 
corn, grain, Aussteuerkasten', puns, pune, punis' hunch, outgrowth am tree, hunch ', 



pauns, pauna 'cran'\um, Stirnknochen', also probably Old Prussian poun/an 'buWocW, 
Lithuanian pune, Latvian pauna'Ranze\, bundle'. 

pu-g-. gr. TTUYn "the Hintere'; Old Icelandic ^i/^'Schneesturm', ^'uka ' qu\ck, fast through 
die air drive, whisk ', /b/r'snow flurry', Middle High German fochen 'b\o\N'; Latvian puga 
"gust of wind', pauga' cushion, head'. 

p(h)u-k-. Armenian yo'^/r' "breath, breeze, wind, breaking wind, fart', PI. "bellows', p'cem 
"hauche', yO'/r '5/77 "blase myself auf; npers. /OJ/r"das blast (um fire anzufachen), bellows', 
afgh. pu, puk^a puff, a blast, the act of blowing'; 

Lithuanian yOi//r/7e "blister, bubble', yOiz/rs/e "swelling, blister', puksciu, pukst/^pant, gasp, 
wheeze', pukys, pukis "chub' (*"Dickkopf'); Latvian pukuls " tassel ' (actually " thick tassel 

yo:/-/?- (probably broken Redupl.): alb. pupe'curd, grape, hill', pupeze'bud, poppy', 
pupu/e^ back'; Latin pupus 'smaW kid, child, knave, boy, BiJbchen', *yC>J/?5" small girl' and 
(late) " pupil of the eye ' (the small reflection of Beschauers in Auge of Angesprochenen')" ' 

Maybe Italian pupilla : Spanish pupila : French pupille : Romagnolo bamben : Venetian 
balota dei oci Albanian bebe " pupil of the eye '. 

Vulgar Latin *puppa {Frencb poupe, Italian poppa) " nipple '; Old Irish ^c/?/" breast' {*puptu- 
); Latvian p^ps "Weiberbrusf, paupVio swell', pupuol'i pupuolT^e\6euka\z.cbeu' (with 
voiced-nonaspirated yO^it'^/zs "bubble auf beer, knot in thread, string'), Lithuanian pupele, 
pupela, pupuole^bu6\ probably also Lithuanian pupa, Latvian pupa'bean'. 

p(h)u-s- Old Indie pusyati, pusnati, yOOS5//"gedeiht, makes thrive, wachst to, ernahrt', 
yC»^s/^-"wohlgenahrt, rich', pusti-, pustf-i. " prospering; flourishing, growth, fullness, 
wealth', p6sa-(is., puspa-ml\o\Ner, blossom, bloom, blossom', puskala-^ncb, prachtig, in 
full vitality '; gr. cpOaa "blast, bellows, bubble' (*(puaaa or *phut-ia), cpuaaw "blow, blase 
auf, cpOoiau) "snort', cpuoiy^f. " garlic, onion, bulb', (puaaA(A)i(; f. "bubble', cpuoKa f. "bubble, 
weal, callus', cpuoKn f. " intestine, sausage ', cpuaKOJv "Dickbauch', noi-cpuaaoj "blow, snort'; 
Latin pussula, pustu/a 'bubb\e, vesicle, blister, bubble'; Mor\Neg\ar\f0ysa {*faus/an) "swell 
up, aufgahren', f(j)usa^ buzz, whirr, with Gewalt ausstromen'; Lithuanian yOJs/e "bubble', 
Latvian pus//s6s., Lithuanian pusnis, yC>^s/7y/75S "zusammengewehter Schneehaufe', puse 
(puse) "blister, bubble', p^'s/ras "Hitzblaschen auf the Haut', Latvian pusk/'s' bouquet, 
Banderstrauft, tussock ' ; Old Church Slavic *puchat/^b\o\N\ *opuchngti^\.o bloat, bulge, 
swell', puchl-b "cavus (turgid, swollen)', xuss. pychatb "pant, gasp, Gluthitze from sich give'. 



pychatb "aufgeblasen, haughty sein', pysnyj^ luscious, aufgeblasen, haughty ' etc., Old 
Church Slavic napystiti sq "sich aufblasen', russ. pyscitb ds. ( *pyskitr, probably also Czech- 
poln. etc. yoys/r "snout, muzzle with thick Lippen'); compare above S. 790 pauson-1 

pu-t-. Old \nd'\c pupputa-^ intumescence of the palate and gums'; gr. nuvvo(; 'rump' 
Hes. ( *put-snos)\ Latin praeputium 'Vorhaut' (from a *putos "penis', compare wruss. potka 
ds.); perhaps Irish i///7 'udder' {*putus)\ Baltic *putid^b\oW in Lithuanian puciu, pusti^b\oW, 
reflex, 'to swell', puntu, pust/^io swell, sich aufblasen', pOslei. 'bubble, bladder', putlus 
'sich blahend, aufgeblasen, stout, proud', p^/a'Schaumblase', putmenosi. PI. 'swelling, 
lump, growth', yC>a/7-yC>J/e//s'aufgeblasener person', papautas'\Nea\, callus', also pautas 
'egg, testicle', pusu, yOi/s/'blow, breathe, breathe', pusma^ breath ', pute bubble, blister, 
bubble', probably also Lithuanian putra^ cereal, grain ', Latvian putra^ cereal, grain, 
porridge, mash'; auf voiced-nonaspirated: Latvian pudurs, puduris^ tussock, heap', pudra 
'heap'; wruss. potka {*p'btbka) 'male limb, member'. 

References: WP. II 79 ff., WH. II 389 f., 392, Trautmann 233 f.; 
See also: compare above b(e)u-2. 
Page(s): 847-848 

Root / lemma: pu-2 : peua- 
Meaning: to rot, stink 
Note: presumably from a pu^ixeV evolved 

Material: Old Indie puyat/'mrd faul, stinkt' = Avestan puye/t/^\N\r6 faul'. Old Indie puya-, -m 
"pus', puti- 'faul, stinkend; Jauche, pus' = Avestan pJ/ay-'Fauligwerden, Verwesung'; 
pashto yOJ/'TriJbung of Auges', westosset amt>udlau\'; Old \r\d'\c putau {: Old Icelandic 
fud) 'buttocks'; with -s/co- Middle Persian pusinTtan^ decayed ', Old Icelandic fauskr^ 
rotten, decayed, decomposed; brittle wood'; Armenian /7i/'eitriges blood'; gr. ttuGco 
"manche decayed ', nu9o|jai "faule', nuov {*pu'^om), nuoq, -£0c; n. "pus'; perhaps also 
nu6(; m., nuap, nuaTO(;, nusria " beestings '; Latin pus, pun's ^ pus' ( *puuos), puted, -ere " 
decayed ', put/dus'iau\' (from a participle *pu-to-s), puter, -tris, -//"©"faul, rotten, decayed, 
decomposed; brittle ' with u-, as Middle Irish othrach^ dunghill ', probably also ofhar'e\n 
sicker' {*putro-), othar-//ge ^Krankenbett, Begrabnisplatz'; Old Icelandic fu/nn^ decayed, 
rott', /&/" decay ', funa^ decayed ', feyja' decay let, verrotten let', Gothic fu/s, Old Icelandic 
fu//, Old English Old High German fu/lauV; 

Old Icelandic fudt "pudenda'. Middle High German i/i//" pudenda', Alemannian vi/de// 
Kinderwort "Popo', geminated Middle High Germanvotze; Lithuanian pi^vu, puti^ decayed 
', causative pudau, -yt/" decayed make', Latvian put^ decayed ', causative pudeV
```


## [2026-09-14T00:54:27.676Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '69360,69400p' POK_full.txt",
 "description": "Read remainder of Pokorny pu-2"
}
```


### [2026-09-14T00:54:27.759Z] TOOL RESULT

```
decayed make', Lithuanian piaulas {*peu-lo-s) m. 'verfau Iter tree', Latvian prauls 
"verfaultes wood' {*plauls), Lithuanian puliaim. PI. "pus', puves(i)aim. PI. 'verfaulte 
Sachen', Latvian puves/m. PI. "pus', puzn/m. PI. ds., papuvet ' fallow '. 

with ^;Old Icelandic fuk/^ Stank', nisi, fuk/ a\so 'verfaultes seaweed, kelp ', as Latvian 
punis^ decaying, pustulating', yOJ/7es PI. 'Modererde'; 

with s; Norwegian f0yr{*fauza-) " rotten, decayed, decomposed; brittle ', Dutch voos 
"schwammig', Swiss ^efdse/7"morschgeworden'; about Old Icelandic fauskrsee above; 

References: WP. II 82, WH. II 391 f., Trautmann 234; G. Liebert Nominalsuff. -//- 151. 
Page(s): 848-849 

Root / lemma: pu-3 

See also: see below peu- and pou-. 

Page(s): 849 

Root / lemma: pu-ro- 

Meaning: corn 

Material: Gr. nOpoc;, Doric airOpoq "Weizenkorn, wheat', nOpnv " seed from allerlei Obst 

and other Fruchten', 5i6(;-nupo(;, -ov 'eine the Weichselkirsche similar fruit'; Lithuanian 

yOi7/'5/"Winterweizen', Latvian pup wheat'. Old Prussian puret Trespe, Bromus 

secalinus'. Old Church Slavic pyro' spelt ', Czech pyr'Quecke', slov. pfrrn., pfrai. " spelt ' 

etc.; Old English /j/rs 'Ouecke, Ackerunkraut', engl. furze. 

References: WP. II 83, Trautmann 232; compare georg. yOi//?" bread'. 

Page(s): 850 

Root / lemma: /ab^-or rdo^- : Aebh-
```


## [2026-09-14T00:54:30.068Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pustula\\|pussula\\|puk\\b\" AHD_watkins1985.txt | head -30; echo \"=== pu- entries ===\"; grep -n \"^pū\\|^pu-\\|pū-\\. To rot\\|To rot\" AHD_watkins1985.txt | head -30",
 "description": "Grep Watkins AHD"
}
```


### [2026-09-14T00:54:30.142Z] TOOL RESULT

```
321:yawn, gape: BAY2, BEVEL; ABASH, ABEYANCE. 2. Possibly Vulgar Latin *abbaidre (> Old French (a)baiier), to bay: BAY‘*.] [battuere. To beat. Latin verb of unknown origin. (BATE?), BATTER!, (BATTER’), (BATTERY), BATTLE; ABATE, COMBAT, DEBATE, (RABBET), (REBATE?), (RE- BATO).] bel-. Strong. 1. Suffixed o-grade form *bol-iyo- in Russian bol’shoi, large: BOLSHEVIK. 2. Prefixed form *dé-bel-i- (dé-, privative prefix; see de-), “without strength,” in Latin débilis, weak: DEBILITATE, DEBILITY. [Pok. 2. bel- 96.] bend-. Protruding point. 1. Germanic *pannja-, “struc- ture of stakes,” in Old English penn, pen for cattle: PEN2. 2. Germanic *pund- possibly in Old English pund- (> Middle English pound), pundfald, enclosure for stray animals: POND, POUND3; IMPOUND, PINFOLD. 3. Germanic *pin- in Old English pintel, penis: PINTLE. [Pok. bend- 96.) beu-'. Also bheu-. Appears in words loosely associated with the notion “to swell.” I. Root form *beu-. 1. Ger- manic *puk- in: a. Old English pocc, pustule: POCK; b. Old French po(u)che and Old North French poke, bag: POACH!, POCKET, POKE3, POUCH, (PUCKER). 2. Old Eng- lish pyffan, to blow out: puFF. 3. Old English -piite, “fish with large head” (in aele-piite, eelpout): pouT?. II. Root form *bheu- with various Germanic derivatives. 1. Old English bdsm, bosom: Bosom. 2. Old English biic, belly, pitcher: BUCKBOARD. 3. Frankish *biak (> Old French buc), trunk of the body: TREBUCHET. 4. Old English bye), pustule: BorL?. 5. German dialectal baustern, to swell, akin to the source of Middle English bost, a bragging: BoasT!. III. Root form *beu-. 1. Latin bulla, bubble, round object, amulet (> Old French boule and Spanish bola, ball): BILL!, BILLET!, BOLA, BOULE?, BOWL’, (BULL?2), BULLA, BULLATE, BULLET, (BULLETIN); BOULE- VERSEMENT. 2. Latin bullire (> French bouiller), to bubble, boil: BOIL!, BOUILLON, BUDGE!, (BULLION), BULLY?; BOUILLABAISSE, EBULLIENCE, GARBOIL, PAR- BOIL. 3. Possibly Latin bucca (> Old French boucle, buckle, curl, and Spanish boca, mouth), (inflated) cheek: BOCACCIO, BOUCLE, BUCCAL, BUCKLE!, BUCKLE?; DE- BOUCH, DISEMBOGUE, EMBOUCHURE. 4. Greek boubén, groin, swollen gland: BUBO. [Pok. 2. beu- 98.] beu-2. Root imitative of muffled sounds. 1. Latin bitié (perhaps > Old French butor), bittern: BITTERN!. 2. Latin bited, a kind of hawk: BUZZARD. [Pok. 1. b(e)u- 97.] bha-'. To shine. Contracted from *bhas-. 1. Germanic *baukna-, beacon, signal, in: a. Old English béac(e)n, beacon: BEACON; b. Old English denominative bécnan, biecnan, to make a sign, beckon: BECKON. 2. Perhaps Germanic *bazja-, berry (< “bright-colored fruit”), in Old English berie, berige, berry: BERRY. 3. Germanic *bandwa-, “identifying sign,” banner, standard, sash, also “company united under a (particular) banner,” in: a. Spanish banda, sash: BANDOLEER; b. Late Latin ban- dum, banner, standard: BANNER, (BANNERET). 4. Suf- fixed form *bhaw-es- in Greek phds (stem phét-), light: PHOS-, PHOT, PHOTO-; PHOSPHORUS. 5. Extended and suffixed form *bhan-yo- in Greek phainein, “to bring to light,” cause to appear, show, and phainesthai (passive), “to be brought to light,” appear: FANTASY, (PANT), PHANTASM, (PHANTOM), PHASE, PHENO-, PHENOMENON; DIAPHANOUS, EMPHASIS, EPIPHANY, HIEROPHANT, PHAN- EROGAM, (PHANTASMAGORIA), PHOSPHENE, SYCOPHANT, THEOPHANY, (TIFFANY). [Pok. 1 bha@- 104.] bha-2. To speak. Contracted from *bhaa-. 1. Latin fari, to speak: FATE; AFFABLE, (FANTOCCINI), INEFFABLE, IN- FANT, (INFANTRY), PREFACE. 2. Greek phanai, to speak: -PHASIA; PROPHET. 3. Suffixed form in Germanic *ban- wan, *bannan, to speak publicly (used of particular kinds of proclamation in feudal or prefeudal custom; “to proclaim under penalty, summon to the levy, declare
872:+ esse, to be; see es-): POSSIBLE, POTENT; (IMPOTENT), PREPOTENT. 3. Form *pot- in: a. compound *ghos-pot-, “suest-master,” host (see ghos-ti-); b. compound *dems-pot-, “house-master,” ruler (see deme-'). 4. Old Persian pati-, master: PADISHAH. [Pok. poti-s 842.] [prak-. To make, do. Greek root. Greek prassein (Attic prattein), to effect, do: PRACTICAL, (PRACTICE), PRAG- MATIC, PRAXIS. [In Pok. 1. per 811.]] prek-. To ask, entreat. 1. Basic form *prek- in Latin *prex, prayer (attested only in the plural precés), with denominative precdri, to entreat, pray: PRAY, PRAYER?, PRECARIOUS; DEPRECATE, IMPRECATE. 2. Suffixed zero-grade form *prk-sk- becoming *pork-sk-, contracted into *posk- in suffixed form *posk-to-, contracted into *posto-, which appears in Latin postuldre, to ask, re- quest: POSTULATE; EXPOSTULATE. [Pok. 4. perk- 821.] prep-. To appear. Suffixed zero-grade form *prp-yo- in Germanic *furbjan, to cause to have a (good) appearance, polish, in Old French fo(u)rbir, to polish, burnish: FuR- BISH. [Pok. prep- 845.] preu-. To hop. 1. Zero-grade form *pru- in Germanic *fru- in Old English frogga (with obscure expressive suffix -gga), frog: FROG. 2. Extended o-grade form *prowo- in Germanic *frawaz in: a. Middle Dutch uro, “leaping with joy,” happy: FROLIC; b. Old High German fré, happy, in frewida, joy (> German Freude): scHa- DENFREUDE. [Pok. preu- 845.] preus-. To freeze, burn. 1. Germanic *freusan, to freeze, in Old English fréosan, to freeze: FREEZE. 2. Suffixed zero-grade form *prus-to- in Germanic *frustaz, frost, in Old English forst, frost, frost: FROST. 3. Suffixed form *preus-i- in Latin *preusis, *preuris, act of burning, whence denominative pririre, to burn, itch, yearn for: PRURIENT, PRURIGO, PRURITUS. 4. Suffixed zero-grade form *prus-ina in Latin pruina, hoarfrost: PRUINOSE. [Pok. preus- 846.] pri-. To love. Contracted from *pria-. 1. Suffixed form *priy-o- in Germanic “frijaz, beloved, belonging to the loved ones, not in bondage, free, in: a. Old English fréo, free; FREE; b. Dutch vrij, free: FILIBUSTER. 2. Suffixed (participial) form “priy-ont-, loving, in Germanic ‘“fri- Jjand-, lover, friend, in Old English friond, fréond, friend: FRIEND. 3. Suffixed shortened form *pri-tu- in Germanic *frithuz, peace, in: a. Old High German fridu, peace: SIEGFRIED; b. Old French esfreer, to disturb: AFFRAY; c. Germanic *frij-, peace, safety, in compound *berg-frij-, “high place of safety” (see bhergh-?). 4. Suffixed femi- nine form *priy-G, beloved, in Germanic *frijj6, beloved, wife, in: a. Old Norse Frigg, goddess of the heavens, wife of Odin: Fricc; b. Germanic compound “*frije-dagaz, “day of Frigg” (translation of Latin Veneris diés, “Ve- nus’s day”), in Old English frigedeg, Friday: FRIDAY. [Pok. prdi- 844.] prokto-. Anus. Greek prokios, anus: PROCTITIS, PROCTOL- OGY, PROCTOSCOPE. [Pok. prdkto- 846.] pster-. Also ster-. To sneeze. Imitative root. 1. Suffixed form *ster-nu- in Latin sternuere, to sneeze: STERNUTATION. 2. Suffixed form *ster-t- in Latin ster- tere, to snore: STERTOR. [Pok. pster- 846.] pu-'. Also phu-. To blow, swell. Imitative root. 1. Ex- tended form *pus- in Latin pustula, a bubble, blister: PUSTULE. 2. Perhaps extended form “pit-, penis, in Latin praepiitium, foreskin (prae-, before, in front; see per’): PREPUCE. 3. Variant form *phi- in Greek phusa (> phusan, to blow), bellows, bladder: EMPHYSEMA, PHYSO- STIGMINE, PHYSOSTOMOUS. [Pok. 1. pu- 847.] pu-2, To rot, decay. 1. Suffixed form *pi-lo- in Germanic *filaz, rotten, filthy, in: a. Old English fi, unclean, rotten: FOUL; b. Old Norse fill, foul, akin to the Scandi- Navian source of FULMAR; ¢. Germanic abstract noun *filithd in Old English fylth, foulness: FILTH; d. Ger- manic denominative *filjan, to soil, dirty, in Old English fylan, to sully: FILE’; DEFILE!. 2. Extended form *pug- in Germanic *fuk- in Icelandic fiki, rotten sea grass, and
876:puk-1. To make fast. Suffixed form *puk-ino- in Greek pukinos, later puknos, strong, fast, thick: PYKNIC; PYC- NIDIUM, PYCNOMTER. [Pok. 2. puk- 849.]
877:puk-2, Bushy-haired. Suffixed form *puk-so- in: a. Ger- manic *fuhsaz, fox, in Old English fox, fox: Fox; b. Ger- manic feminine *fuhsdn- in Old English fyxe (> Middle English fixen), she-fox: VIXEN. This root is in part a taboo deformation of wikwo- and wip-é-. [Pok. pik- 849.]
1535:FOX puk-2
2144:PUSH pel-6 PUSILLANIMOUS an@-, pau- PUSTULE pu-1 PUTAMEN peu- PUTATIVE peu- _ PUTREFY dhé-1, pu-2 PUTRESCENT pu-@ PUTRID pu-2 PYCNIDIUM puk-! PYCNOMTER puk-! PYELITIS pleu- PYGMAEAN peuk- PYGMY peuk- PYKNIC puk-! PYLON pulé PYLORUS pulé PYO- pu-2 PYRACANTHA = ak- PYRARGYRITE arg- PYRE pir- PYRENE piiro- PYRETIC  pir- PYRITES pir- PYRO- pur- PYROPE okw- PYROSIS pir- PYROXENE xenos PYRRHOTITE pir- PYRUVIC ACID 6g-
2456:VISA weid- VISAGE weid- VISCID weis- VISCOUNT ei-1 vIscous weis- VISE wel-1 VISIGOTH weSs-pero- VISION weid- VISTA weid- VITAL gWei- VITAMIN gWei- VITELLUS wet-2 VITIATE wei-4 VITICULTURE wei-1 VITILIGO wel-4 VITTA wei-1 VITUPERATE wei-4 VIVA gWei- VIVACIOUS gWei- VIVERRINE wer-® VIVID g¥ei- VIVIFY dhé-1, gwel- VIVIPAROUS gWei- VIXEN puk-2 VOCABLE wekw- VOCAL wekw- VOCATION wekw- VOCIFERATE bher-1 VODKA wed-1 VOGUE wegh- VOICE wekw- VOID eu-2
=== pu- entries ===
872:+ esse, to be; see es-): POSSIBLE, POTENT; (IMPOTENT), PREPOTENT. 3. Form *pot- in: a. compound *ghos-pot-, “suest-master,” host (see ghos-ti-); b. compound *dems-pot-, “house-master,” ruler (see deme-'). 4. Old Persian pati-, master: PADISHAH. [Pok. poti-s 842.] [prak-. To make, do. Greek root. Greek prassein (Attic prattein), to effect, do: PRACTICAL, (PRACTICE), PRAG- MATIC, PRAXIS. [In Pok. 1. per 811.]] prek-. To ask, entreat. 1. Basic form *prek- in Latin *prex, prayer (attested only in the plural precés), with denominative precdri, to entreat, pray: PRAY, PRAYER?, PRECARIOUS; DEPRECATE, IMPRECATE. 2. Suffixed zero-grade form *prk-sk- becoming *pork-sk-, contracted into *posk- in suffixed form *posk-to-, contracted into *posto-, which appears in Latin postuldre, to ask, re- quest: POSTULATE; EXPOSTULATE. [Pok. 4. perk- 821.] prep-. To appear. Suffixed zero-grade form *prp-yo- in Germanic *furbjan, to cause to have a (good) appearance, polish, in Old French fo(u)rbir, to polish, burnish: FuR- BISH. [Pok. prep- 845.] preu-. To hop. 1. Zero-grade form *pru- in Germanic *fru- in Old English frogga (with obscure expressive suffix -gga), frog: FROG. 2. Extended o-grade form *prowo- in Germanic *frawaz in: a. Middle Dutch uro, “leaping with joy,” happy: FROLIC; b. Old High German fré, happy, in frewida, joy (> German Freude): scHa- DENFREUDE. [Pok. preu- 845.] preus-. To freeze, burn. 1. Germanic *freusan, to freeze, in Old English fréosan, to freeze: FREEZE. 2. Suffixed zero-grade form *prus-to- in Germanic *frustaz, frost, in Old English forst, frost, frost: FROST. 3. Suffixed form *preus-i- in Latin *preusis, *preuris, act of burning, whence denominative pririre, to burn, itch, yearn for: PRURIENT, PRURIGO, PRURITUS. 4. Suffixed zero-grade form *prus-ina in Latin pruina, hoarfrost: PRUINOSE. [Pok. preus- 846.] pri-. To love. Contracted from *pria-. 1. Suffixed form *priy-o- in Germanic “frijaz, beloved, belonging to the loved ones, not in bondage, free, in: a. Old English fréo, free; FREE; b. Dutch vrij, free: FILIBUSTER. 2. Suffixed (participial) form “priy-ont-, loving, in Germanic ‘“fri- Jjand-, lover, friend, in Old English friond, fréond, friend: FRIEND. 3. Suffixed shortened form *pri-tu- in Germanic *frithuz, peace, in: a. Old High German fridu, peace: SIEGFRIED; b. Old French esfreer, to disturb: AFFRAY; c. Germanic *frij-, peace, safety, in compound *berg-frij-, “high place of safety” (see bhergh-?). 4. Suffixed femi- nine form *priy-G, beloved, in Germanic *frijj6, beloved, wife, in: a. Old Norse Frigg, goddess of the heavens, wife of Odin: Fricc; b. Germanic compound “*frije-dagaz, “day of Frigg” (translation of Latin Veneris diés, “Ve- nus’s day”), in Old English frigedeg, Friday: FRIDAY. [Pok. prdi- 844.] prokto-. Anus. Greek prokios, anus: PROCTITIS, PROCTOL- OGY, PROCTOSCOPE. [Pok. prdkto- 846.] pster-. Also ster-. To sneeze. Imitative root. 1. Suffixed form *ster-nu- in Latin sternuere, to sneeze: STERNUTATION. 2. Suffixed form *ster-t- in Latin ster- tere, to snore: STERTOR. [Pok. pster- 846.] pu-'. Also phu-. To blow, swell. Imitative root. 1. Ex- tended form *pus- in Latin pustula, a bubble, blister: PUSTULE. 2. Perhaps extended form “pit-, penis, in Latin praepiitium, foreskin (prae-, before, in front; see per’): PREPUCE. 3. Variant form *phi- in Greek phusa (> phusan, to blow), bellows, bladder: EMPHYSEMA, PHYSO- STIGMINE, PHYSOSTOMOUS. [Pok. 1. pu- 847.] pu-2, To rot, decay. 1. Suffixed form *pi-lo- in Germanic *filaz, rotten, filthy, in: a. Old English fi, unclean, rotten: FOUL; b. Old Norse fill, foul, akin to the Scandi- Navian source of FULMAR; ¢. Germanic abstract noun *filithd in Old English fylth, foulness: FILTH; d. Ger- manic denominative *filjan, to soil, dirty, in Old English fylan, to sully: FILE’; DEFILE!. 2. Extended form *pug- in Germanic *fuk- in Icelandic fiki, rotten sea grass, and
```


## [2026-09-14T00:54:41.099Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '872,874p' AHD_watkins1985.txt | grep -o \"pu-2, To rot, decay.\\{0,1400\\}\"",
 "description": "Read full Watkins pu-2 entry"
}
```


### [2026-09-14T00:54:42.162Z] TOOL RESULT

```
pu-2, To rot, decay. 1. Suffixed form *pi-lo- in Germanic *filaz, rotten, filthy, in: a. Old English fi, unclean, rotten: FOUL; b. Old Norse fill, foul, akin to the Scandi- Navian source of FULMAR; ¢. Germanic abstract noun *filithd in Old English fylth, foulness: FILTH; d. Ger- manic denominative *filjan, to soil, dirty, in Old English fylan, to sully: FILE’; DEFILE!. 2. Extended form *pug- in Germanic *fuk- in Icelandic fiki, rotten sea grass, and
```


## [2026-09-14T00:54:42.234Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"FUZZY\\|fuzzy\\|FULMAR\" AHD_watkins1985.txt | head -10",
 "description": "Grep fuzzy in Watkins"
}
```


### [2026-09-14T00:54:42.286Z] TOOL RESULT

```
872:+ esse, to be; see es-): POSSIBLE, POTENT; (IMPOTENT), PREPOTENT. 3. Form *pot- in: a. compound *ghos-pot-, “suest-master,” host (see ghos-ti-); b. compound *dems-pot-, “house-master,” ruler (see deme-'). 4. Old Persian pati-, master: PADISHAH. [Pok. poti-s 842.] [prak-. To make, do. Greek root. Greek prassein (Attic prattein), to effect, do: PRACTICAL, (PRACTICE), PRAG- MATIC, PRAXIS. [In Pok. 1. per 811.]] prek-. To ask, entreat. 1. Basic form *prek- in Latin *prex, prayer (attested only in the plural precés), with denominative precdri, to entreat, pray: PRAY, PRAYER?, PRECARIOUS; DEPRECATE, IMPRECATE. 2. Suffixed zero-grade form *prk-sk- becoming *pork-sk-, contracted into *posk- in suffixed form *posk-to-, contracted into *posto-, which appears in Latin postuldre, to ask, re- quest: POSTULATE; EXPOSTULATE. [Pok. 4. perk- 821.] prep-. To appear. Suffixed zero-grade form *prp-yo- in Germanic *furbjan, to cause to have a (good) appearance, polish, in Old French fo(u)rbir, to polish, burnish: FuR- BISH. [Pok. prep- 845.] preu-. To hop. 1. Zero-grade form *pru- in Germanic *fru- in Old English frogga (with obscure expressive suffix -gga), frog: FROG. 2. Extended o-grade form *prowo- in Germanic *frawaz in: a. Middle Dutch uro, “leaping with joy,” happy: FROLIC; b. Old High German fré, happy, in frewida, joy (> German Freude): scHa- DENFREUDE. [Pok. preu- 845.] preus-. To freeze, burn. 1. Germanic *freusan, to freeze, in Old English fréosan, to freeze: FREEZE. 2. Suffixed zero-grade form *prus-to- in Germanic *frustaz, frost, in Old English forst, frost, frost: FROST. 3. Suffixed form *preus-i- in Latin *preusis, *preuris, act of burning, whence denominative pririre, to burn, itch, yearn for: PRURIENT, PRURIGO, PRURITUS. 4. Suffixed zero-grade form *prus-ina in Latin pruina, hoarfrost: PRUINOSE. [Pok. preus- 846.] pri-. To love. Contracted from *pria-. 1. Suffixed form *priy-o- in Germanic “frijaz, beloved, belonging to the loved ones, not in bondage, free, in: a. Old English fréo, free; FREE; b. Dutch vrij, free: FILIBUSTER. 2. Suffixed (participial) form “priy-ont-, loving, in Germanic ‘“fri- Jjand-, lover, friend, in Old English friond, fréond, friend: FRIEND. 3. Suffixed shortened form *pri-tu- in Germanic *frithuz, peace, in: a. Old High German fridu, peace: SIEGFRIED; b. Old French esfreer, to disturb: AFFRAY; c. Germanic *frij-, peace, safety, in compound *berg-frij-, “high place of safety” (see bhergh-?). 4. Suffixed femi- nine form *priy-G, beloved, in Germanic *frijj6, beloved, wife, in: a. Old Norse Frigg, goddess of the heavens, wife of Odin: Fricc; b. Germanic compound “*frije-dagaz, “day of Frigg” (translation of Latin Veneris diés, “Ve- nus’s day”), in Old English frigedeg, Friday: FRIDAY. [Pok. prdi- 844.] prokto-. Anus. Greek prokios, anus: PROCTITIS, PROCTOL- OGY, PROCTOSCOPE. [Pok. prdkto- 846.] pster-. Also ster-. To sneeze. Imitative root. 1. Suffixed form *ster-nu- in Latin sternuere, to sneeze: STERNUTATION. 2. Suffixed form *ster-t- in Latin ster- tere, to snore: STERTOR. [Pok. pster- 846.] pu-'. Also phu-. To blow, swell. Imitative root. 1. Ex- tended form *pus- in Latin pustula, a bubble, blister: PUSTULE. 2. Perhaps extended form “pit-, penis, in Latin praepiitium, foreskin (prae-, before, in front; see per’): PREPUCE. 3. Variant form *phi- in Greek phusa (> phusan, to blow), bellows, bladder: EMPHYSEMA, PHYSO- STIGMINE, PHYSOSTOMOUS. [Pok. 1. pu- 847.] pu-2, To rot, decay. 1. Suffixed form *pi-lo- in Germanic *filaz, rotten, filthy, in: a. Old English fi, unclean, rotten: FOUL; b. Old Norse fill, foul, akin to the Scandi- Navian source of FULMAR; ¢. Germanic abstract noun *filithd in Old English fylth, foulness: FILTH; d. Ger- manic denominative *filjan, to soil, dirty, in Old English fylan, to sully: FILE’; DEFILE!. 2. Extended form *pug- in Germanic *fuk- in Icelandic fiki, rotten sea grass, and
874:Norwegian fogg, rank grass, probably akin to the Scandi- navian source of Middle English fog, fogge, aftermath grass: FoG?. 3. Extended variant form *pous- in Ger- manic *fausa- in Low German fussig, spongy: FUZZY. 4. Suffixed form *pu-tri- in Latin puter (stem putri-), rotten: PUTRESCENT, PUTRID; OLLA PODRIDA, (POT- POURRI), PUTREFY. 5. Suffixed form *puw-os- in: a. Lat- in pus, pus: PURULENT, PUS; SUPPURATE; b. Greek puon, puos, pus: PYO-. 6. Greek compound empuein, to suppu- rate (en-, in; see en): EMPYEMA. [Pok. 2. pii- 848.]
1544:FROLIC fik-, preu- FROM per? FRONTISPIECE spek- FROST preus- FROTTAGE bhréi- FROWARD per! FRUCTIFY bhrig- FRUGAL bhriig- FRUGIVOROUS bhrig- FRUIT bhriig- FRUITION bhriig- FRUMENTACEOUS _ bhrig- FRUMENTY bhriig- FRUSTULE bhreus-2 FRUSTUM bhreus-2 FRY! bher-4 FUGACIOUS bheug-1 -FUGE bheug-! FUGITIVE bheug-1 FUGLEMAN man-1, pleu- FUGUE bheug-! FUHRER per-2 FULCRUM bhelg- FULGENT bhel-1 FULGURATE bhel-1 FULIGINOUS dheu-1 FULL! pele-1 FULMAR pu-2 FULMINATE bhel-1 FUMARIC ACID dheu-1 FUMAROLE dheu-1 FUMATORIUM dheu-! FUMATORY dheu-1 FUME dheu-! FUMIGATE ag-, dheu-! FUMITORY dheu-1, ters- FUNAMBULIST al-2 FUNCTION bheug-2 FUND bhudh- FUNDAMENT bhudh- FUNDUS_ bhudh- FUNGIBLE bheug-2 FUNNEL gheu-
1547:FUSE? gheu- FUSILE gheu- FUSION gheu- FUTILE gheu- FUTURE bheue- FUZZY pu-2
```


## [2026-09-14T00:54:51.364Z] TOOL CALL #14: Bash

```json
{
 "command": "pdftoppm -f 408 -l 408 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg408 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg408.png",
 "description": "Render PDF page 408 to PNG"
}
```


### [2026-09-14T00:54:53.349Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 78365 Sep 13 20:54 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg408.png
```


## [2026-09-14T00:54:55.076Z] TOOL CALL #15: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg408.png"
}
```


### [2026-09-14T00:54:55.686Z] TOOL RESULT

```

```


## [2026-09-14T00:54:55.679Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-14T00:55:04.508Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg408.png')\nprint(im.size)\n# Germanic box approx y 1400-1580 x 590-940 in original coords (displayed*1.65)\nim.crop((580,1400,960,1570)).resize((380*3,170*3)).save('pg408-germ.png')\nim.crop((560,2350,950,2470)).resize((390*3,120*3)).save('pg408-ampus.png')\n\"",
 "description": "Crop Germanic and am-pus boxes"
}
```


### [2026-09-14T00:55:05.853Z] TOOL RESULT

```
(2550, 3300)
```


## [2026-09-14T00:55:07.982Z] TOOL CALL #17: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg408-germ.png"
}
```


### [2026-09-14T00:55:08.001Z] TOOL RESULT

```

```


## [2026-09-14T00:55:12.650Z] TOOL CALL #18: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg408-ampus.png"
}
```


### [2026-09-14T00:55:12.688Z] TOOL RESULT

```

```


## [2026-09-14T00:55:27.298Z] TOOL CALL #19: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg408.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/408.png && echo ok",
 "description": "Copy page PNG for audit"
}
```


### [2026-09-14T00:55:27.364Z] TOOL RESULT

```
ok
```


## [2026-09-14T00:55:29.716Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\n# leaf = printed + 21\nfor p in (75,):\n    for leaf in (p+21,p+22,p+20):\n        if leaf<len(pages):\n            print('==== leaf',leaf,'printed',p,'====')\n            print(pages[leaf][:2500])\nEOF",
 "description": "Print Horn page 75"
}
```


### [2026-09-14T00:55:30.589Z] TOOL RESULT

```
412
==== leaf 96 printed 75 ====
skr. (Sütr.) püjäyati 'Ehrfurcht bezeigen'; phlv.
pöfinak 'bereuend' ').
337. pü^e Pfote .
phlv. päcakf püzak 'Pfote'.
Zu pai, vergl. Hörn, BB. XVII, 258.
338. po8t 'Fell, Haut', pöstln,
aw. pq8tö.[fra&ah' ; phlv. pöst, pöstln.
LW. kurd. pöst ^ pTst 'Fell, Haut'; bei. pöst, pöst
(213) ; afy. pöst ; wa/. p^i?^, sar. past,
339. j>iifc, pwA: das Blasen (um Feuer anzufachen), Blase-
balg 2).
gr. (pvöa 'Blasen, Blasebalg, (pvonta *Blase'; arm.
puK 'Hauch', puUI^ Blasebalg , pKam 'sich aufblasen,
pcem 'hauchen' (nicht entlehnt nach Hübschmann
No. 285).
Die richtige neupersische Form muss buk sein.
Arm. p und gr. rp weisen auf indog. ph (vergl.
Bartholomae, BB. 10, 290), np. h auf indog. bh\
also indogermanische Doppelformen wie bei [/^veph-,
vebltr- u. ö.^).
340. puläd 'Stahl'.
phlv. pülafat oder püläft, vd. 8 (254) (arm. LW.
poXopat, poXpaty po'kovat)^ pülaftTn (AV.), pülät (West
Säy. näääy. 2, 114).
LW. kurd. püla, ptla etc.; af>'. pöläd; oss. biilaf^
bolaf; bei. puläJ , pülat (209) ; arab. fülad, syr. "TPC.
*) Peshotun's *Grammar of the Pahlvi Language', 8. 359
Zcrile 2 (nach Darme steter, Et. ir. I, 280).
*) Die Verhältnisse liegen bei diesem Worte nicht klar. Darf
man nach arm. p*uft etc. annehmen, dass die Bedeutung *Brennholz\
welche die Wörterbücher dem np. pük geben, nur geraten ist? SF's
Vers :
meil-i ütes buved hemtse bepüfc
z. B. verträgt die Bedeutung *Hauch, Blasen' für ^>^i^• sehr gut.
') Bartholomae (briefl. Mitteilung) meint, dass die Verdächtigung
von np. püh nicht notwendig sei, da ein Wechsel von Tenuis und Tenuis
aspirata im Anlaut oft genug vorkomme, während ein solcher von ph,
bh u. dgl. sich auf den Auslaut beschränke.
==== leaf 97 printed 75 ====
7« -
Vergl. Seil rader, Sprachvergl. und Urgesch.^ 287,
Miklosich, Fremdwort. 8, Hübschmann, Etymol.
u. Lautl. d. osset. Spr. 121. Fr. Müller hält (WZKM.
5, 186) np. püläd für ein griechisches Lehnwort (etwa
no'Kvnava^) ; ganz unsicher.
341. pehre *Wache\
aw. i)ädra' 'Schutz'; ai. pätra- (unsicher; ein Mal),
arm. LW. paliak (cpQovgu)^ vergl. paA, pahapan etc.,
fara\parhaJc (de Lagarde, No. 2203).
LW. af/. pahra, pahar; bei. pahar, pahrä (193).
342. 2>ehlü 'Seite'; Stadt' (Sahn. 1, 104 Vers 793, 105
Vers 804), arab. LW. fahla 'Stadt*.
mäz. päll; gel. pälü.
aw. pere&ii' 'breit'; phlv. pahlük hezw, pffhrük 'Seite';
ai. vergl. pfthm- 'Erde'.
LW. bei. pahll 'Rippe (279); kurd. pal (H.-Sch.).
Mit aw. peresH' 'Kippe, Seite\ ai. pärgcd-, kurd.
pärsü, wa/. pürs, kurm. parsü, oss. fars 'Seite, Strich,
Gegend' (278) lässt sich np. pehlü lautlich nicht direkt
zusammenstellen.
343. peJilev, pehletan 'Held'^).
ap. Parfhava-; phlv. pahlav (gehört etwa auch
pahlum hierher?).
344. peh/Ti' 'weit, breit', pehnä.
Käs. pen, pahdn, pan,
aw. pa^ana^ 'weit, breit; phlv. pahan, pahnäi^
pahnäk.
kurd. pän ; af;\ plan ; oss. d. fafan t. fäfdn 'Breite,
breit' (281); bei. patan (289).
345. {i)pei-, Praefix.
ap. patli/ 'zu, gegen etc.'; aw. paiti; phlv. pat-^ pät-
etc.; ai. präti.
Im Neupersischen erscheint das Praelix pati- als
pät\ pa\ pid% peö\ pei" {pe^),
*) Gehört hierher t. LW. balabän (statt *palabän) *gro88* (s. auch
Miklosich, Denksohr. WAW. Band 35, 255; 37, 10)? Für bala-
(*pala-) vergl. mäz. päli^ gel. pälü, kurd. päl (No. 342).
==== leaf 95 printed 75 ====
74 -
haben (die Wörterbücher erklären allierdings das
erstere durch das letztere).
333. inipü, püpe, püpek 'Wiedehopf; auch hühü etc.
Lat. upüpa 'Wiedehopf; gr. snoifj.
kurd. papü (H.-Sch.), päpü (JJ.).
Der Name ist onomatopoetisch gebildet (vergl.
B r e h m , Vögel II : *Wenn zwei Wiedehopfe streiten,
rufen sie unablässig hup^ auch wohl hup-puli) ^).
Die neupersischen Formen mit p sind denen mit b
vorzuziehen (vergl. auch das Gazophylacium, das beide
hat).
334. püde *faul, verfault', päsiden (Inchoat.) *faulen .
aw. päiti' Täulniss, apuyant- *nicht faulend'; phlv.
pütaky püslnitan, püs(i)sn^ arm. LW. put (aaß^pog, v6&og) ;
skr. püyati (Brahm., Sütr.), ai. piiti- *faul, stinkend'.
oss. d. am-bud, t. ämbid ^faul* (18).
335. poz 'Partie um die Nase* 2).
g. püz,
kurd. püZj pöz; bei. pöz, pönz, n. pönz 'Nase (310);
aiy, pöza^ paza ; sangl. fuzik, minj. foska,
oss. d. finje, t. fing 'Nase' (286), arm. pinj (pinS)
'Nasenloch* will Hübschmann hiervon trennen ;
aber vielleicht mit Unrecht. Urverwandtschaft ist
doch gewiss vorhanden (nachträgliche Nasalirung).
336. pöziS 'Reue, Entschuldigung', pöztden (Vis und Kämm, ^
S. 92 Vers 3).
^) Nach griechiöcher Anschauung ruft der Wiedehopf nov nov,
d. i. 7IOV uoa flai (nämlich Procne und Philomela), vergl. Preller,
Griech. Mythologie', II, 142. Mein Freund und College Thraemer
macht mich auch auf Tzetzes, Chil. YII, 479 aufmerksam: uov noZ ds
2) FR hat folgenden Vers Mölevi M a* n e v I ' s (Metr. Remelj :
röl pinhän mehimed z'esän heröz
tä siiyi bäyes ne bu(ßäyend^ pöz
vergl. deutsch *seine Nase in etwas hineinstecken'. F J citirt noch Verse
aus Sa' dl und Gsedl.
```


## [2026-09-14T00:55:43.476Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pusa\\|puiti\\|puyeiti\\|pūiti\\|pūtay\\|apuyant\" BRT.txt | head -40",
 "description": "Grep Bartholomae"
}
```


### [2026-09-14T00:55:43.529Z] TOOL RESULT

```
4499:•  j.  anupöiö'want-  Adj.  (fem.  'waiii-) 'mit  einem  hervortretenden  Reif,  Kranz versehen';  pusain  ('Diadem')  .  .  'waüTm Yt.  5.128.
9928:•  j.  ga8ä-  f.  "Wiuflteule"*:  he  . .  °oqtn nijairtti  aspalca  puiti  vlral^a  "er  schmet- tert die  Keule  nieder  auf  Ross  und  Mami" Yt.  jo.  101;  —  hazannm  °oanqm  Ytio,
12833:•  j.  "startvs  vä  puiti  psSti  davaisne  »a" V,  7. 43  PüZ.
14066:•  j,  drafäaka'vant-  Adj.  (fem.  •vaiti-) 'mit  Bändern  geschmückt' :  pusam . .  'vaitim Yt.5.i»8.
15918:Die  Lesung  ist  nnsicher;  nach  Jp  I,  Mr2 u.  a.  wäre  pusavaiä  zu  schreiben,  d.  i. 'mit  einem  Biadem  (fusä-)  versehen';  so las  wohl  auch  PB.  —  Fü.:  puiänSmand,  erL: vis  bacak  apäi\  Scheint  fusavaiä  gelesen  und puia  gleich  np.  pus  "Sohn'  gesellt  lu  haben. DST.  ZA.  2.  270  häh  dai  für  richtig!  — ')  ai.  pai-  f.  —  ')  Dann  (ur  *pasu^v'  geschr., S  i6S.  12.
25092:•  j.  raO^kara-  Adj.  (fem.  •kairJ-)  '(einen Wagen,  Wagenkasten  bildend,  d.  L)  wie ein  Wagenkasten  gestaltet"':  ufairi pusam bandayata  artdvT  .  .  asta^aoiäqm  'iair- yam*^  YL5.  n8.
25913:—  panea  'ta  upäsananqm  V.J.  36;  36,  ä 83,  *F.  10;  —  xsvas  'taif  Aala.H'kanqm  V. 4-(>;  13';  —  hapita  'ta  us'tranqm  Ytg. 30; V.4.7,  13';  —  aita  'ta  upusananqm  V. 4. 14;  14,  8;  —  ye^ke  avavat  hatnanqtn (sd.)  «(wa  **W(/  (als  Nom.)  hasatirimea Yt.5. 120;  V.4.9,  15'.  b)  adjekL  ge- braucht: Äfl^ra.._yiisfl/'aÄ^jiT.,^anfaj(i/to"o Hailca  hazanraisca  Vr.  Ä  i.  a)  mit attiib.  Einerzahlen:  hazatanm  narqtn  .  . iaoxma  . .  xlvas  'ta  . .  tisrS  'ta  (als  Gen.) "den  Samen  von  1000  Männern  . .  von 600  . .  von  300"  V.  2. 30.
25949:•  j.  sato.straDha-  Adj.  (fem.  'ishä-)  "mit hundert   Juwelen  (?)    besetzt':    pusau. •aham  saranalfilm  Yt.  5.128.
```


## [2026-09-14T00:55:49.690Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"Diadem\" BRT.txt | head -20; echo \"=== pu- verb ===\"; grep -n -i \"faulen\\|Fäulnis\\|Faulnis\\|fanlen\" BRT.txt | head -20",
 "description": "Grep Bartholomae for Diadem and faulen"
}
```


### [2026-09-14T00:55:49.755Z] TOOL RESULT

```
4499:•  j.  anupöiö'want-  Adj.  (fem.  'waiii-) 'mit  einem  hervortretenden  Reif,  Kranz versehen';  pusain  ('Diadem')  .  .  'waüTm Yt.  5.128.
6457:•  j.  asta.kaoida-  Adj.  (fem.  "da-)  'acht- teilig, achtfach  geteilt':  ufairi  fusqm bandayata  arjdvt  süra  anähtla  .  .  'dam ". .  ein  Diadem  . .,  ein  achtteiliges"  Yt. 5.128.
27911:goldenem  Diadem  geschmückt*:  vann zaranyS.xaoüim  .  .  'sim  Yt.  /J.  57;  — 'sjm  hitäsf^m  Yt.  /p.  41.
=== pu- verb ===
4073:•  j.  a-friÖyant-  Adj.  'nicht  verfaulend, verwesend':  yat  kirmavqn  frahm  ahüm azar}Smi3m  amarihntim  -yantim  apu- yantsm  Yt  79.  11;  —  *°yS  Vyt  45'', F.jh".
15302:•  j.  *pavitajr-  f.  'Fäulnis,  Venvesung": cvat  antar>  *n)r3ui  aSsa  druxl  y3  nasus axtica  'ti^a  ahitica  fräsnaoiti  "wie  viel . , trifft  die  Drug  . .  mit  Krankheit,  Fäulnis und  Befleckung?"  V.5. 27,
17476:aürvaniä  'iaz'H    ".  ^    die  Berggipfel  "'die !  ^J"    frae*-    V.    'verfaulen,    verwesen', acht  Renner'"  ¥1.75,3.
17492:yai^a  aete  nasävö  frikyeiHca  (statt  Plur.) puyäila  "und  wenn  die  Leichname  ver- faulen und  verwesen"  V.ö'.  28; —  'ß-iHyani-.
24663:galwqm  pairiyaoidai'hUa  .  .  'rasibyasia vJspaHbyasia  patri  aSltaäliyB  V.  14.  17. Eig.  'mit  unförmlichen  Gliedmaßen';  vgLai vyäiiga.  Adj.  'an  den  Gliedern  entstellt';  in 'anura-  s.  Ntr.  —  Pa.  ■.  tiiankava  in  Aw.- Buchsl.,  erl.:  rpkn  oderrpnk;  Gü.: 'Fäulnis',
```


## [2026-09-14T00:55:57.464Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '17470,17500p' BRT.txt; echo \"===== 15295-15310\"; sed -n '15295,15310p' BRT.txt",
 "description": "Read Bartholomae pu- root context"
}
```


### [2026-09-14T00:55:57.542Z] TOOL RESULT

```
Vgl.
2^;  air,  brüad.  -
•  j.  "bsut  N.ö^.
(S  36S.  7,  S}»;    sonst    erscheint   im  Awesta beliebig  >a-  (.  /^a-)  und  /rä'.  -  ')  S.  daiu Bthl.  IF.  12.  99.  —  3)  Aog.  //:  lies/rÄ. •  j.  "yoy^la  fraeazaite"  F.  tfe.
Pii. :   ä_f  JiwH /räf  I  a  dt    (d.  i.  (fl>'n'  'nascitur' oder  fj^/  'precatar').
j./raeta:  s,  ■ii)'-,  Sp.   153  m.
aürvaniä  'iaz'H    ".  ^    die  Berggipfel  "'die !  ^J"    frae*-    V.    'verfaulen,    verwesen', acht  Renner'"  ¥1.75,3.
El.  ?    Aus  ar.  *pkäni>i' ;  S  9,  sgS.  7  b.
•    j.    finkav-    m.    'Gipfel,    Spitze    (od.  1 dgL)':  ahmat  haea  garayB  fraoxfyqn  a/ia
•  j.  "faSri  'Vater'«:  F.y.
Pii.:  paar.  —  ')  Ist  Itein  selbständiges  Wort, sondern  vom  Kompositumende  abgetdst,  vgl. iridal.ßirJ-  u.a.,  Bthl.  IF.  II.    133,
•  j./jorf-,  Fem.  zu  ptar-:  s.  yoi&a pitar-. KompE.  —  Vgl.  */'*"'■
j,  *f;^tS,  g,  fitröi :  i.  unter  fiUar-.
•  j.  fyaohav-  m.  'Hagel':  artdvim  .  .yniht cahwärö  ariana  hqmMSal  aAurö  mazäa v3t?mca  vänmca  magy^mca  -tihumca  Yt. j.  i2o;Ä33.
vAbleit  —  Ob  lU  ai.  findfli,  pipha  'lerstam- pfen'  (mit  idg,  s)f\  s.  Bthl.  AirV.  109,  Ost- HOFF  PBrB.  18.  a.    Vgl.  piiatU-.
•  j.  fyaohv'a-  den,  Praes.  3»  'hageln', 'hageln,  Hagel  fallen  lassen',  i)  von  der
^ac\A'^:ta^ryascit  fiaca  xlafhs  vänntya  . . fyanhvaityä'*  "auch  in  dunkler  Nacht, (welche  sva.)  wenn  es  .  .  hagelt"  Yt  16. 10,  2)  von  den  Hengsten  der  Arsdvl:
cahwärS  arhina  .  .  misti  .  .  värttUaica sntaiiniaica  srasStaa^a  *fyanhuniaica  3' (3PPM.)  "vier  Hengste  . .  durcheinander lassen  sie  es  regnen  und  schneien  und triefen  und  hageln"  Ylj.  120.
S  '53-  3-  —  ''  Vgl  snarg-  No.  1.—  =»  Lesung  un- sicher; besser  vU.  mit  J  10  fyanhuntyi, S  iSl  d  o,  —  3)  NA.  \»,\/ryai>k'  ohne  Be- merkung;  ebenso  Wo.  Doch  wohl Dmckfe hier.
•  j.  fyanhvattt-  Adj.  (fem.  'vaitl-y'', PPA.:  s.JyarfAva-.
')  Unsicher,  s. /yasflma-  No.  2.
Praes.  27  fii^ya-.
yai^a  aete  nasävö  frikyeiHca  (statt  Plur.) puyäila  "und  wenn  die  Leichname  ver- faulen und  verwesen"  V.ö'.  28; —  'ß-iHyani-.
Et.?").  —    Pa.  naslai'),  —  ">  ai.  mrityaä  'er lerßllt*  reimt  wohl  as\i  fr&y',  ist  aber  nicht identisch  damit,  wie  Gdn.  GIrPh.  *.  52  wilL — ")  Zu  'nas-;  vgl.  dagegen  lU  aftAyant-. •  j.  'fraeöta-  Adj.  'der  meiste'  an  Zahl: *^dus.dätayä  (Sp.7S3m.)  'tai^Yva..)  drvanfö Aog.  $6;  F.  y.  a)  ASn.  'Um  als  Adv.
'am  meisten'",  nach  Zahl,  Menge,  Um- fang usw.:  mq%raväkahe  .  .  yS  'Um  . . a/irmairyanqm  (Gen.  part  als  Obj.) . .  ava.- jaynat  Yt  1^.105;  —  yat  ba  paiti  'hm kärayeiti  .  .  yavanqnüa  västranqtnca  (sd,; Gen.  part  als  Obj.)  V.  3.  4;  ~  yat  bä paiti  't»m  viksnte  .  .  girihqm  (Gen.  part als  Obj.)  V.J.  22;  —  ya^  b3  paiti  'tim bavainü  .  .  g^rjiqm  (Gen.  Flur,  als  Subj.) V.J.  10;  —  yat  bä  paiti  't)m  malsmti pasvasca  , .  V._j.  6;  —  yat  bä  paiti  °t»m us.zlZ3nti  (sd.)  pasvasla  V,_j,  5;  — yat  bä paiti  'tim  daxma  usdaüa  (sd.)  kiryänte V.J.9;  13;  —  yat  bä  paiti  Uim  lairi nikantt  V.  j.  8;  —  yat  ba  paiti  "tsm uskfnti\.3.i2;  —  yS  't>m  apivataiU  dag- nayh  V.  g,  3.  a)  zur  Verstärkung  des Superlativs  '* :  yai  ahmi  nmäne  . .  'ttm yaozdätU.B3mö.t»n3mca  hu^ö.z3mS.t3m3mca kambistitnla  .  .  V,  5.  46^',
Kompar.  laparau-.  —  Aul  ar.  *pr<4J)iitha;  mit a  aus  uridg.  >.  —  Wgl /räyoA-.  —  Pü.;/«- Uli,  —  0  In  V.  3.  10  könnte  'lfm  syntaktisch
dby  Google
97  S  'fraeäta-  -
dl  NSn.(Subj.),  in  V.  3.  5,  6,  12,  aa,  Yt.  13. 105  aU  ASn.  (Obj.)  genommen  werden,  S. aber  die  übrigen  Stellen  und  den  Gebrauch unstes  'am  meisten'.  S.  auch  fräyö  Adv,  — ")  Wie  gr.  ffJjiorov;  s.  KÜHNER  Ausf.Gr.d. Griech.Spr.>  2.  26.  —  31  Vgl.  V.  3.  15,  wo •hm   fehlt.
•  g.  'fraeSta-  m.  'Gesandter,  Bote':  yavsi vTspsi  'tänhs  hr^hämä  "fiir  alle  Zeit  wollen wir  (deine)  Gesandten  sein"  V-^j?.  8".
Komp.:  *fra-^*aia-,  Pl'fP.  «im  V.  'ais-.  — np.  firiila,  ßriha  'Bote',  arm.  LW.  hriHak.  — Pü.:  hamäk  täk  i  z-isp  framänpat  ktiid,  erl.! fraiöstr  u  hä-uiitän  i  fraiöstr  läk  tan  1  pasin hamäk  fäüxiähih  dah.  —  0  Vgl.  zSl.  Y.  33. 1  c
===== 15295-15310
•  j.  'payah-  Adj.  '(milchend,  Milch  sva.) Saft  gebend,  schaffend"':  maiaydizarf- ma^tt  {sd.)  'yanhim  Vr.  2.  2;  —  mailySi- zanmayehe  'yatths  Vr.  /.  2.
Vgl  'fayak-.  —  Pü.;  flmenU.  —  ')  Bed.  nach Roth  ZDMG.  34.  703.
•  j.  pav-  V.  'faulig  werden,  verwesen' Praes.  27  puya-.
yezica  alle  nasävO  friäsyatila  (sd.)  fi^e tica  Y.6.28;  —  'puyant;
a\.  puyaü,  wose.  ämiiiyun,  mp.  kaniiüiltan'i^ np.  fiüsü/an');  t.  noch  Pü.  zu  afiuyan/'  und GltPh.  1  b,  321.  —  Fä.-.fiälai.  —  D  Inkob.; vgl.  GIrPh.  /.  320,  /  b.  129.
•  j.  pavant-  Adj.  'hütend,  schirmend, schützend':  avä  °va  (NS.)  pasca  'vii  pars •vä  spa/  vT^aSa  ,  .  frä  *aähe  vJsaiti nivirS  .  .  yakmäi  .  .  Yt  10. 46.
Ableit  (mit  vanl^  aus  '"^pS^y)-  n.  Das  auf- fällige a  setzt  die  Existens  von  Fonnen  wie *kupi,  *kup3Bi  usw.,  nach  der  i-Dekt.,  voraus.
•  j.  *pavitajr-  f.  'Fäulnis,  Venvesung": cvat  antar>  *n)r3ui  aSsa  druxl  y3  nasus axtica  'ti^a  ahitica  fräsnaoiti  "wie  viel . , trifft  die  Drug  . .  mit  Krankheit,  Fäulnis und  Befleckung?"  V.5. 27,
Zum  V.  pav:  —  Vgl.  pülay;  zu  dem  sich *paviüiy'  verhalt  wie  im  Aind.  sämlay-  I.  zu sätäy-  i,  —  Pü.!  paiinjisn  'Bespiengung',  erl. : remanih.  —  i)  So  L  4,  K  1 ;  NA.  pivaf.
•  j.  'par-  V.  'gleich  machen'.  Praes.  4 psra-,  3$  (Pass.)  pairya-.
'vergleichen':  kva  iä  (föä/'j(sd.)  *pair- yeU'^  V.  ig.aj.
mit  aipi  'begleichen  (eine  Schtild)',  ohne Obj.  'Busse  tun':  Aa  hi  asti  B'ha  hä  hl asH  aptnHl  aipi.pänmnäi  ida  alaone nSil  anaipi.panmnäi  drujO  nmaw..  "..das ist  daiiir  die  Sühne  für  den  Gläubigen, der  hier  Busse  tut;  für  den  (aber),  der nicht  Busse  tut  (,  gilt  der  Spruch):  draß\ d^mämmw.  (Y.^i).  iidj"  V.  Ä  107.^
VgL  Sp>T}lay-,  anäp>ri%a-.  —  lat  vgl.^ar  Adj.  I
'gleich'.  —  Pü.  (in  V.  yp);  ku  Hält  däir  api raruiend,  erl. :  \kii)  iSn  äyiin  u  iavHit  tu  yäi, s,  No.;  (tu  V.  S):  ka  apar  pukrik  att,  erl.! ka  apta-  vicärel.  —  >)  So  nach  Jp  I,  Mr2. NA.  hat  pärayänii  (».  auch  Pü.);  doch  beachte man,  dass  kurz  lavOT  zweimal  nipätayania steht,  das  leicht /äi-iij''  vnanlasst  haben  kann. pairy'  ist  jedenfalls  die  lectio  diS".
•  j.,  g.  'par-  V.  'füllen'.  Praes.  3  'fra-^'', 1  pa/r-,  II  p)rm-;  Perf.  *pa/r-.  —  PPfP.
p?r3na'  (sbes.).
```


## [2026-09-14T00:56:11.279Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pus[aä]\" BRT.txt | head -30",
 "description": "Grep Bartholomae pusa"
}
```


### [2026-09-14T00:56:11.333Z] TOOL RESULT

```
4499:•  j.  anupöiö'want-  Adj.  (fem.  'waiii-) 'mit  einem  hervortretenden  Reif,  Kranz versehen';  pusain  ('Diadem')  .  .  'waüTm Yt.  5.128.
14066:•  j,  drafäaka'vant-  Adj.  (fem.  •vaiti-) 'mit  Bändern  geschmückt' :  pusam . .  'vaitim Yt.5.i»8.
15918:Die  Lesung  ist  nnsicher;  nach  Jp  I,  Mr2 u.  a.  wäre  pusavaiä  zu  schreiben,  d.  i. 'mit  einem  Biadem  (fusä-)  versehen';  so las  wohl  auch  PB.  —  Fü.:  puiänSmand,  erL: vis  bacak  apäi\  Scheint  fusavaiä  gelesen  und puia  gleich  np.  pus  "Sohn'  gesellt  lu  haben. DST.  ZA.  2.  270  häh  dai  für  richtig!  — ')  ai.  pai-  f.  —  ')  Dann  (ur  *pasu^v'  geschr., S  i6S.  12.
25092:•  j.  raO^kara-  Adj.  (fem.  •kairJ-)  '(einen Wagen,  Wagenkasten  bildend,  d.  L)  wie ein  Wagenkasten  gestaltet"':  ufairi pusam bandayata  artdvT  .  .  asta^aoiäqm  'iair- yam*^  YL5.  n8.
25913:—  panea  'ta  upäsananqm  V.J.  36;  36,  ä 83,  *F.  10;  —  xsvas  'taif  Aala.H'kanqm  V. 4-(>;  13';  —  hapita  'ta  us'tranqm  Ytg. 30; V.4.7,  13';  —  aita  'ta  upusananqm  V. 4. 14;  14,  8;  —  ye^ke  avavat  hatnanqtn (sd.)  «(wa  **W(/  (als  Nom.)  hasatirimea Yt.5. 120;  V.4.9,  15'.  b)  adjekL  ge- braucht: Äfl^ra.._yiisfl/'aÄ^jiT.,^anfaj(i/to"o Hailca  hazanraisca  Vr.  Ä  i.  a)  mit attiib.  Einerzahlen:  hazatanm  narqtn  .  . iaoxma  . .  xlvas  'ta  . .  tisrS  'ta  (als  Gen.) "den  Samen  von  1000  Männern  . .  von 600  . .  von  300"  V.  2. 30.
25949:•  j.  sato.straDha-  Adj.  (fem.  'ishä-)  "mit hundert   Juwelen  (?)    besetzt':    pusau. •aham  saranalfilm  Yt.  5.128.
27910:•  j.  zaraoyö.pusä-  Adj.  (mask.  'sa-)  'mit
29551:PiiZ.;  —  /laväi  rahmeiJ.105; — x^aAmt*^ dam  Yi.i4-2',  2*;  —  kväahs  puäirSnhS pusättÄS  davainti    'V.ig.42^^;   —    Äava unaNyt  42;    —    ferner;    AavS   FrW. 8.1;    —   havä   N.55;   —   Avam    F.  24, P.  26';   —   hvais    FD.  7;   —  '  ^3(7  V. 4. 1  PüZ.'"'.         S.  noch  zu  "hasaoiyä. KompA.  (-feä-,  xH-,  *7tvä- ;  j"«?").  E, ;  AbleiL {Avä-,  x'a').    —    Ableit,  aus  dem  Pron.  refl.; s.  nutet '^fl-.  —  ai.  ivä-  Adj.,  alat.  joiwj  usw. (Bgm.  KurieVglGr.  409);  np.  vgl,  jr^w'eißen' (woia  GIrPh.  I.  37,  391,  l  b.  119).    —   Pü.: jr^ij;  s.  noch  No.  3,  8f.  —  O  Nur  Ton  dieser Stammfoim  finden  sich  Kasus  rein  pronomi- naler Bildung:  x^aArni,  J^aiyäi  aoä  j^aXjii. — »>  iF.  s.  Aain^ä,  GIrPh.  /.  I31i  iSchr.  S  36S. 13b.  — 3) Pü.:  «ÜB  iuiiiSti  an  i  yS  'veslruni facina«  proprinm'.    —    4)  NA.  x'äuiaitia.    — S)  MlLLS  Auseinandersetzung   über  die  Form, G.  SS7,  ist  völlig  verkehrt.  —  *)  Die  Stellung ganz  wie  im  Lat. :    'suae  quaeque  genti'.    — 7)  Hds.  AavaAt.  —  »)  Pü.:  an  i  ei.  —  9)  Fu.: fehlt.  —  10)  V.  4- 1  steht  daftr  :fäi
```


## [2026-09-14T00:56:20.955Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Stirnband\\|Kopfbinde\\|puiä-\\|pusä-\\|puSä\" BRT.txt | head -20; echo \"=== around 15930-15990\"; sed -n '15920,15960p' BRT.txt",
 "description": "Find Bartholomae pusā headword"
}
```


### [2026-09-14T00:56:21.487Z] TOOL RESULT

```
27910:•  j.  zaraoyö.pusä-  Adj.  (mask.  'sa-)  'mit
=== around 15930-15990
Ganz  unsicher.  —  Pä.:  fehlt
•  j.  *pasv-äzah-'>  m.  Titel  eines  Gehilfen beim  Opfer:  'zat»h?m  ästaya  "ich  stelle den  P,  an"  N.  6^5.
Eig.  'der  dasOpfertier  zu  treiben  hat';  •Jsa*- n,  'Trieb',  zum  V.  a^.  —  ')  Hds.  paa'ä  i*.  — ä)  Es  heisst:  pa  paip'  äsf  ziän  gSipand  afe a-.i-ganäii  kal  kust  i  daiin  ^spand  atvganisn. j.  pasvira  Vt.  13.   12;  lies  pasu  vaa.
•  j.  pazdaya-  Praes.  30  (Kaus.)  'scheu- chen',
1)  'aufscheuchen':  yä galwqm  yam  apu- %rqm  janaiti  va  vayHti  va  xraosyeüi  va paldayäli  va  "wer  eine  HUndin,  die  kurz zuvor  geworfen  hat,  schlägt  oder  verfolgt oder   anschreit   oder  aufscheucht"  V.  i^.
dby  Google
885
pazdav-
paka-
886
5.  3)  'verscheuchen':  yai  mqm  iura (sd.)  pasdayanta  .  .  naotaraca  Yt  J".  55;
Za  einem  Praes.  3  n.  ^pa-zda-ti ;  %.  "thaii- und  BtHL.  ZDMG.  JO.  686.  —  Pfi.:  transsltr. (paid^nil),  mit  der  Erl.;  kus  dost  Aae pas  Skä/rl (s.  noch  syazg;  No.  3).
•  j.  pazdav-  m,  Name  schädlicher  Klein- tiere, etwa  'Käfer,  Made' :  baevan  'dunam gäks.varttanqm  (sd.)  ava.JanySl  V.  14.  6,
np.  vgl.  paidak  'Kommilbe',  Ob  daiu  ai. /fifoi-m.  EN.  —  PB.:  pind,  ob  ♦/"ä"''''*?
•  j.  "^"paSna-  m.  "Hinsehen  auf  — ';  nur LS.  'in  conspectu,  angesichts',  mit  a)  Gen. und  b)  Akk.:  a)  'ne  varsis  pisinankB  YL 5-37)  49;  —  ""'  <^P^  däityayh  Yt. 5.112, 17.29,17.61.  b)  °tte  äpsm  frazdänaom Yt.  j.  108.
KompE.  (s.  mpcaHaia-\  —  Zum  V.  sfas-, S  83.  a.  —  O  NA.  hat  pasne;  aber  F  i,  E 1 haben  durchaus,  J  [o,  PI  1  fast  überall  /.
•  j.  'paSna-  n,  'Augenlid':  'nsm  F.^d. Vgl.  ai.  päkfman-  n.  'Augenwimpern';  np. pdim  'Wolle';  e.  dazu  Zufitza  Gült.  1S9, Hbm.  PSt.43.  —  Ya.%pS!  i  fah»  (woiu  liurd. pac  i  cam  'Augenlid',  ZDMG.  3S.  55  lU  ver- gleichen).
•  j.,  g.,  p.  'pä(y)- V.  'hüten'.  Praes.  ipa-: pa-'^,  a  pHya-,  T  päpay,  fj  paya-,  °fya-'>; j-A  0  r.  1  päA-.  —  PPfP.  fiata-;  Inf.  psi,  pü  e, *patayal-ca,  pä%räi,  'fyethyai.
i)  'hüten,  schützen,  schirmen':  arh  . . xlü%rTl  hupStS  timS  ya  uitrS  p3iH*v^airiS Yt  14. 12;  — pairi^wd  bavaiti  panth  yim .  .  paiti  Aog.  ~S;  —  avatsqmca  pahü phntS  yim  isMti  ..Yt  10.  4$; —  ahwum vairim  tattütn  paiti  V.r/.3;  Yt._j.3;  — ttr^m  afur<^mazdä  patuv  utamaiy  xsa- ^•^am  X.1.4;  4,  2.3,^.3',  4.3,  7.3,  Am.4, Ao.  1. 4.  a)  'behüten,  beschützen  vor  — '
{pairi  oder  iaca  mit  Abi,):  päta  (»P.) tiB  tbisyantat  pairi  SrB.j;  F. /o;  —  ^imaiii dahyäum  c^urt^mazdä  patuv  haca  hainäya D.^3;  6.^.  2)  'abhalten,  abwehren von  — ,  es  verwehren,  dass  . .',  mit  Abi. oder  abL  Inf,:  ta  .  .  yä  Tm  Aujyatui/ (sd.) payat  {3SKA.)  fiHt  duzjyatnis  Y.  46.%;  — at  tSng  är)gvä  . .  pat  gh  frörftöis'isA.)  Y. 46.  \;  —  %waAya  mqhranS  dstim yi  Js  pat dar^säf(sd.)  alahyä  Y.js.  13,  3)  'wahr- nehmen, sich  angelegen  sein  lassen,  sorgen für  -'  (Akk.):  piahake  (aSKj-AorM.) aahuhwftnca  ratuhwim&t  Yt  Ä  1;  — !'  imam  parsam  käram  padty  yadiy  kar<^ parst^  pata*  ahatiy  "(so)  sorge  fiir  das
persische  Heer;  wenn  fUr  das  persische Heer  gesorgt  ist,  . ."  D.5. 3. mit  a:  s.  afya^yai  Inf. mit  patiy,  paiti  i)  I  Med,  'sich  hüten, .ich  in  Acht  nehmen  vor  — '  {haca  mit Abi,):  ha?a  draug^  darSam  poHpayt^uvä Bh.4-5-  a)  Med.  'sich  vorsehen  gegen  — , sich  zu  decken  suchen  gegen  -'  (Akk.): ya'^a  na  snaihi/  asne  niymal^m  paiti.- ■ainöii . .  aval paiti.papayamnB  *vlovä  . . '.  21.  3)  Med.  'sich  (einer  Sache)  ver- sehen, (es)  ahnen',  absolut:  na^a  mainyu paitipaite  "und  nicht  versieht  er  sich  des im  Geist"  Ytro.  19.
mit  \/r3  und]^  nX  'schützen,  Schutz gewähren  vor  — '  (pairi  mit  Abi.):  \frä\^ \a  uvaiibya  ahubya  uvaiibya  nS  akubya ipayi  (Opt.)  '*  .  .  pairi  .  .   mahrkat  Y.
mit  an) 'hüten,  schlitzen':  sraosim  ..yB nipaiti  mazdä  damqn  .  .  ys  vUp»m  aküm ..  pnhua  maiki/a  nipaiti  Y.57. 16;  — azftn  bsii..nipayani  vispa  voha  Ytj.Sg; — lam  ta  daiühavB  mpahi  Yt.ro.78.  a)  'be- hUten,  beschützen  vor  — '  (pairi  oder  parB mit  AbL):  nipaysis  mallm  urva%»m  .  . aurva%at  parB  Yli,  24;  —  uvaiibya  nS ahubya  nipaya  (Opt)'^  ..  pairi .,  moAr/tat YL  10. 93^*;  —  faf  iij  /i}tr0  nipätü  pairJ . . Ibaisauhat  Y.5Ä  2.  2)  'in  Obhut,  Ver-
wahr geben':  tatca  .  .  %wahmT  3  *dqm (sd)  nipauhl  (iSKjAorM.)  manS  vohB  .. Y.45>io**i — y^  ais  asim  ttipäahl manasca vokB  yavaitaiti  "der  ich  darum  das  rechte Tun  in  Verwahr  geben  will  und  das  gute Denken  flir  immer"  Y.  18. 1 1  *'.
ai.  pAli,  pähi,  fäsati,  pAntak;   ap.  päyad,  'bäd.
—  S.  noch  päA-  (piiy\  —  Pü. :  päyüan,  päaa- kih  karlan,  Npö.  (lU  Y.  ja.  13,  46.  A):  dir kardan,  —  ')  pa.  vor  dem  y  des  Opt. :  payä.
—  ')  Nur  im  Inf.  äfyniyäi.  fya-  ist  die  regel- rechte Kompositions  form  lu  paya-  (mit  a  aus urldg.  A;    IF-  7.  70.    —    J>  Vgl.  Yl,  to.  93.
frä  ist  Wiederholung  aus  dem  Vorhergehen- den, wie  auch  die  Stellung  von  aSa  (sd.,  No.  5) ausweist.  —  «  Vgl,  V.57.  2S  und  No.  3.  — 5)  S.  iSt.  unter  dam-,  daidar-  and  pairigae'i.a:
•  j,  'pa{y)-  i)  Adj.  "hütend,  schützend, schirmend'.  2)  n.  'Schutz,  Schirm'.  DS. pdf  als  Inf.  sbes.
KompE. ;  Ableit.  {s.  fiavaa/.).  —  Zum  'V.pä(yy.
—  ai.  -pa-  Adj.
•  j.  paka-  Adj.  'kochend'.
KompE.  —  Zum  V.  pak-.  —  ai.  'päki'  Adj., mp,  'päk,  np.  'bä,  'vi.
db,Google
887
päta-
•  P-  (.  i-)  päta-  Adj.,  PPfP.:  s.  'päiy)-. KompE.
•  j.  %wqm  tat  upaxbaya  y3i  pStayas£a nipätayJi  mhtshtmla  Miarfca  (soll  heissen) "darum  ruf  ich  dich  an,  dass  du  schützest und  beschützest  Sonne  und  Mond"  VyL  43.
Verbindung  von  fä°  und  ni-fä'  wie  Yl  /aSo.
•  j.  patar-  m.  'Hüter,  Schützer,  Schinner', von  Göttern :  'ta  nqma  ahmt  (näml.  AhM.) Yt/.i3;  —  /fiw'näml.  Mi^ra)  maskanahe °/a  nipata  ahi  adruzqm  Yt.  10. 80;  — haom^m  . .  'tsrftn  tanuye  baire  Yt  14. 57.
KompE.  —  Zam  V.  p^yY-  —  ai.  pätir-  m., rp.  ^fl'(?);  llBM.  PSl.  35.  —  Va.:  päspän.
```


## [2026-09-14T00:56:35.482Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"pusag\\|pūsīdan\\|pusidan\\|pūdag\\|pudag\\|pūtag\\|pōsīdan\" PHD.txt PHD_mackenzie.txt | head -20",
 "description": "Grep MacKenzie"
}
```


### [2026-09-14T00:56:35.531Z] TOOL RESULT

```
PHD_mackenzie.txt:6657:foul gandag, ganniig, pudag.                 gaining one's ends kiimag-hanjiim.
PHD_mackenzie.txt:7488:rotten pudag; v. corrupt.                  save boxtan.
PHD_mackenzie.txt:7489:rottenness pudagih.                        saved boxtag.
```


## [2026-09-14T00:56:36.915Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"pusak\\|pusag\\|pūsīt\\|pusit\\|pūtak\\|putak\" NYB_vol2_glossary.txt | head -20",
 "description": "Grep Nyberg glossary"
}
```


### [2026-09-14T00:56:36.968Z] TOOL RESULT

```
3192:pūtakēh [pwtkyh] decomposition, decay 112°.
```


## [2026-09-14T00:56:41.865Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pwtk\\|pwsk\\|pws\\b\\|pwsyt\" PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt | head -20; echo \"=== crown ===\"; grep -n -i \"diadem\\|crown\" PHD_mackenzie.txt | head -20",
 "description": "Grep Pahlavi spellings"
}
```


### [2026-09-14T00:56:41.935Z] TOOL RESULT

```
PHD.txt:170:abilag 5/4! | N ~a] blister. a-bim [bym] fearless. āb-kāmag [5A mk! | N ~a] a thick, sour soup. abnüs Pžēnws | (N ābnūs)] ebony. a-biy Pbwd] senseless. ~ih: senselessness. à abr РЫ, Séi | N ~] cloud. M bel abrang [ing | N aurang] glory, splendour. abrastan, abraz- [AP stn',SPc- | М ?br?st, N (afráttan), afrdz-] lift, raise. abraz [Pe | N afrāz] acclivity. abrēšom Pflyš(u)m | M? bryfwm, N ~} silk. ~én [-yn!] silken. abróxtan, abróz- ['piwhtn', ?phoc- | M brwxt, ?)brwc-, N afróxtan, afróz-] light, kindle, illuminate, polish. ~i$n(ih): illumination. āb-tazan Pftcn!] watercourse. a-bun [*dwx!] baseless, bottomless. a-burd-framān ['bwltplm^n'] disobedient. ~th: disobedience. aburnāy f(w)lnd, v. purnāy | N burnā] under age, child. ^h : childhood. aburnáyag [?A(w)/n’(d)yk'] child. abus [pws] (woman) having just given birth. “АҺ: childbirth. арив, -tan Pws, -tn! | M ’bwws, v. ábestan] pregnant. „il: pregnancy. abydxtan, abyóz- Phywhtn', ?bywc-] join, mix. āb-zan zn! | N ~] bath. labzar [el pel] M *6c*7, N afzār] instrument, means; spice. *abzar [6271 | M bail skill, power; powerful. „ūmand [-wmnd] skilled, able. abzāy-, —išn, у. abztidan, abzón [?pzwn! | M, J ”*bzwn, N afzün] increase, growth. ~ig [-yk!] increasing, expansive, bountiful. ~igih: bountifulness. abzüdan, abzáy- ['pzwtn!,^?pzd- | M ?bz'y-, N afzüdan, afzāy-] in- crease, grow. ~i$n: increase, growth. a-čār [cI] inevitable, Jee ~ag [-k'] compelled.
PHD.txt:551:pillagan [plk’n' | M pylg, N ~] steps, ladder. pim [pym] pain, pang, sorrow. ~gén [-kyn'] sorrowful. pir [руі | N ~] old, aged, ancient. ~ih: age. piring [pling | M pryng, (N pirind)] monochrome damask, pist [pst! | N ~] browned flour. pistag [pstk! | IN pista] pistachio nut. pišīz [pšyc | N ~] small copper coin, ‘farthing’. pēhišn [pwhsn'] corruption, decay. pēlāwad [pwPft! | М pwl'wd, N pēlād] steel. ~ën [-yn!] (made of) steel. pondik [pndk' | Ar. b/fundug] hazel-nut. por [pwl | N —] francolin. pēryētkēš [pwlyw(k)kyf = Av. paoiryē.tkaēša-| (one of) the first teachers of the Mazdean religion. ~ЛЬ : the primal doctrine of the Mazdean religion. pēst [pwst! | = M, N ~] skin, hide; bark, shell. mēn [-yn! | N ~in] (made of) skin. pēšīdan, pēš- [pws-yin' | N <] cover, put on, wear. ~išn: covering. potk [pwtk' | N ~] sledge-hammer. poxtan, paz- [APPWN-tn' < А V?ph; pwhtn', pc- | M pwxtn, N ~] cook, bake. рӧу- [pwd- | (P pwd-), N ~] run. ~iSnig : running. p6z(ag) [pwc(k!) | N pēz(a)] snout, muzzle. püdag [pwtk! | N pūda) foul, rotten. —ih: rottenness. 1puhl [pwhl | N pul] bridge. *puhl [pwhl] expiation, atonement; punishment. puhlénidan [ pwhlynytn'] cause to atone. purnāy [pwln’d] adult. purr (MALE < A mlh; pul | M pur, N ~} full. =-ģāh [-g’s] at the fullness of time, about to die. ~-тюаһ [-mh] full moon. —-rawišnih [-lwbsnyh] fullness. ~-sardag [-sltk'] of all kinds. --xwarrah [-G DE] full of glory. pursidan, purs- [pwrs-ytn' | M pwrs-ydn, N ~] ask. Vu re: Е ~iSn: question. — ~i$nig : responsible. pus [BRE < A br-h; pws | = M, N =] son. ~ar [BREI, pwsl | M pwsr, N ~] son. —yàn [pwsd?n! | M pwsy’n] womb. pušt [52001 | = M, N ~] back; support, protection.
NYB_vol2_glossary.txt:1491:Filippos [pylpws] Dilurroc', Philip 117°.
NYB_vol2_glossary.txt:3182:pus [BRH; pws 2218. 2615, 277] son, cas. rect. and cas. obl., passim; secondary cas. obl. pusar [BRH-1] 5115.21.24, 523.9; pl. cas. obl. pusän (BRH-'n'] 188, sec- ondary form pusarän [pwsPn'] in the enumeration apāk pusarān brätarän (ete.) 185, 21°. 241-5. — < OP puca-, SW form of pudra- (v. ‘puhr); MPrs pws (cas. rect.), pwsr (cas. obl.). — pusar is modelled on the pattern of pttar, brätar, mātar, duxtar; NP pus (old), pusar; modern pisar influenced by pidar.
NYB_vol2_glossary.txt:3187:pušt [pwšt'; Ps. pwšty] the back 1112. 2521. 29%. 6513. 1287; pat ~ tacitan to run after, to pursue 311%; pat ~ bütan to protect, to be the protector 31°; ~ kartan 6 to protect 872%; — pl. eas. obl. ~-dn: pat puštān i Vištāspān for the (acts of) protection of the Vistasp dynasty 9514. — MPrs pws, NP pušt < *pršti-; Av. (878) paršta-, parsti-, v. s. v. puštēpān.
NYB_vol2_glossary.txt:3192:pūtakēh [pwtkyh] decomposition, decay 112°.
NYB_vol2_glossary.txt:6106:pwlwd: polavatčn pwr: purr pwrsydn: pursitan pws: pus pwst: post pwšt: pušt py'dg: padatak pyd, pydr: pit pyd’g: paitak pyg: padak pygm: paitäm pym’n: patmän pymwen: patmöcan pymwxtn, pymwe-: patmöxtan pyr’yg: pairayak pyrwz: péroz pyšwb'y: p&söpäi pyšyn: pēšēnīk Pyš, pyšyy, pyšyh: pēš pyw’c-: patvac- pywn: patvand pywst: patvastan
PHD_mackenzie.txt:831:abu8 [lpws] (woman) having just given birth.
PHD_mackenzie.txt:833:Abus, -tan ['pws, -tnl I M 'bwws, v. Abestan] pregnant.
PHD_mackenzie.txt:4258:posidan, pos- [pws-ytn' IN.....,] cover, put on, wear.
PHD_mackenzie.txt:4260:potk [pwtk IN.....,] sledge-hammer.
PHD_mackenzie.txt:4267:piidag [pwtk I N piida] foul, rotten.
PHD_mackenzie.txt:4283:pus [BRE < A br-h; pws I = M, N ......] son.
=== crown ===
772:abcsar ['f>ysli M 'bysr, N alsar] crown.
6316:crown abesar.                              date-palm muy.
```


## [2026-09-14T00:56:54.223Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ps'k\\|pws'k\\|ps\\`k\\|psʼk\" SOD.txt | head -20; echo \"=== crown in SOD ===\"; grep -n -i \"crown\" SOD.txt | head -30",
 "description": "Grep Gharib Sogdian for crown"
}
```


### [2026-09-14T00:56:55.162Z] TOOL RESULT

```
26393:2845  ps'k   B  Jl^c^i 
39801:4854  krps'k   B  (<JLJ^)aJ^  i^^X^^ja^  i^JUf 
57722:7435  ps'k   M  (^TLJ.-J^^jf  ^-uU^t«jf  £l- 
57732:7436  ps'kyc   M  (*-ft~>:Ls>j^>)J-*(J#?*\* 
79232:10516  wysps'k    B  =»  wyspsy 
=== crown in SOD ===
57727:garland,  crown 
79240:prince,  crown  prince 
88511:crown    7435 
88512:crown  prince     10517
```


## [2026-09-14T00:56:57.641Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '57715,57740p' SOD.txt; echo \"=== 2845 ===\"; sed -n '26388,26400p' SOD.txt",
 "description": "Read SOD entries 7435 and 2845"
}
```


### [2026-09-14T00:56:57.726Z] TOOL RESULT

```
then,  afterwards,  on  the  other  hand 
STii;  BSTi  14a,  C2  glossy  BBB  656 

7433  ps>h    M  -*  ps> 

7434  ps'q    C  =*  ps>k 

7435  ps'k   M  (^TLJ.-J^^jf  ^-uU^t«jf  £l- 
p(s)sak   (ps>q)  ©<Av.  pusa-ka-;  MP  pwsg 

©pi.  _/   =»>ps>k(h) 

garland,  crown 

Hen.  BSOAS  11,  74.14,  15;  LW  48;  C2,  48V25; 
GMS  171 

7436  ps'kyc   M  (*-ft~>:Ls>j^>)J-*(J#?*\* 
pasakic   ©Uigh.  pPkyc 

fourth  month  of  the  year 


299 


=== 2845 ===
bound,  prisoner 
STi  3801;  C2  gloss. 

2844  psty   M  =»  pst'k 

2845  ps'k   B  Jl^c^i 
f(o)sak?  ^'ps'y- 

bearing,  subjection 

TSP  16.39,  40  n  p230;  fi?t,  TSP  2.205  n  pl71 

2846  ps>m-  =>  ,ps>m-
```


## [2026-09-14T00:57:06.304Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"7435\\|\\[pdf page\" SOD_pages.txt | grep -n -B2 -A2 \"7435\" | head; echo \"---\"; awk '/7435  ps.k/{found=1} found&&/\\[pdf page/{print; exit}' SOD_pages.txt; echo \"--- find page tag before\"; grep -n \"\\[pdf page\" SOD_pages.txt | awk -F: '{print $1, $0}' | head -3",
 "description": "Locate SOD page for entry 7435"
}
```


### [2026-09-14T00:57:07.370Z] TOOL RESULT

```
1:25090:     parezamande                                             7435 ps'k M            (^TLJ.-J^^jf ^-uU^t«jf £l-
2:37977:crown    7435                            cutting through the waist      5607     dears 7392
3:38357: garland   1303, 7435                  giving birth    11336                   going and returning          321
---
--- find page tag before
```


## [2026-09-14T00:57:10.421Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=25090 && /\\[pdf page/{p=$0; n=NR} END{}' SOD_pages.txt; grep -n \"pdf page\" SOD_pages.txt | awk -F: '$1<25090' | tail -2",
 "description": "Find pdf page tag for SOD entry 7435"
}
```


### [2026-09-14T00:57:11.750Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T00:57:19.279Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c \"\" MON_part1.txt MON_part2.txt; grep -n \"پساک\\|بساک\" MON_part1.txt MON_part2.txt | head -20",
 "description": "Grep Mo'in for pasak/basak"
}
```


### [2026-09-14T00:57:19.357Z] TOOL RESULT

```
MON_part2.txt:94500
MON_part1.txt:99339
MON_part1.txt:23305:بساک: 0 تاجی که از گل‌ها و 
MON_part1.txt:31588:پساک: »۲:۰2 (.) تاجی که از گل‌ها و 
MON_part1.txt:46094:پرچم است که بساکی درشت و چسنده 
MON_part1.txt:82066:بهم متصل شده و یک لول ۵ بساکی را
```


## [2026-09-14T00:57:21.854Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '23298,23315p' MON_part1.txt; echo \"==========\"; sed -n '31580,31600p' MON_part1.txt",
 "description": "Read Mo'in basak/pasak entries"
}
```


### [2026-09-14T00:57:21.935Z] TOOL RESULT

```
زیسانی» لطسیفه گسویی. بسی آمیختگی. 
گشاده‌رویی در صحبت و نوازش مهمان. 
سادگیء بسیرنگی» بی‌نیرنگی. (شیم.) 


چگونگی جسم مفرد (بسیط). 

بساک: 0 تاجی که از گل‌ها و 
ریاحین و اسپرغم‌ها و برگ مورد می‌ساختند 
و پادشاهان و بزر کان و دلیران روزهای عید 
و جشن و مردمان در روز دامادی بر سر 
می‌گذاشتند. ( گیا.) برجستگی دکمه مانند 
انتهای مبلة پرچم گل که مسحتوی دانه‌های 
گرده می‌باشد. 

بسالت: ۱022 [ع. سالة ] (امص.) دلبری» 
دلاوری» یلی؛ شجاعت. 

==========
دخره» اندوخته. س افکندن» س‌انداز» 
پس‌اوگند. آنجه از اقساط بدهی و قرضی در 
موعد خود پرداخت نشده باشد. 
پس‌افتادن: (مصل.) عقب 
افتادن» تاخیر. عود مرض در حال نقاهت» 
نکس. افتادن به پشت و مردن» غش کردن با 
مر دن. 

پساک: »۲:۰2 (.) تاجی که از گل‌ها و 
ریاحین با اسپر عم‌ها ساختندی و بادشاهان و 


۳۵1 


فر هنک فارسی معین 


سان بر بر وز
```


## [2026-09-14T00:57:34.122Z] TOOL CALL #35: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(json.dumps(d['MON'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['FRS'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['SNS'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['BLY'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['FFD'],ensure_ascii=False,indent=1))\n\"",
 "description": "Read ref details for MON FRS SNS BLY FFD"
}
```


### [2026-09-14T00:57:35.211Z] TOOL RESULT

```
{
 "title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)",
 "kind": "website+archive_djvu",
 "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)",
 "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt"
 ],
 "page_offset": null,
 "covers_etymology": true,
 "notes": "covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم‌ها' instead, which do give Avestan forms (e.g. Frangrasyan) and can serve as a cross-check. noorlib has no Mo'in 6-vol entry found. The 6-vol edition itself was not found on archive.org, Google Books or HathiTrust full view. || RE-SEARCH 2026-09: still no scan of the 6-vol Amir Kabir edition (incl. vols 5-6 اعلام) on archive.org, Google Books (API quota-limited; WebSearch found no record with preview), HathiTrust (no record surfaced), noorlib, ketabnak (author page persons/6040 lists 34 Mo'in titles, none the 6-vol فرهنگ), tarikhema, picofile, scribd, Commons/Wikisource. Only the 2-vol Adena condensation exists (archive.org, mirrored on ketabnak 65980/65981, picofile, persianpdf, scribd); its image PDFs were downloaded to incoming/MON/ (the _text.pdf variants with OCR layer are at the same archive.org identifiers). The 6-vol set is purchase-only (in print: iketab.com, bookroom.ir/book/97022, 30book.com/Book/32100).",
 "cites": "page number of Mo'in's six-volume Farhang-e Farsi; MON5:… / MON6:… = volume 5 / 6 (proper names)"
}
{
 "title": "Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/LughatEFurs-AbuMansurAliBinAhmadAsadiTusiFarsi (Abbas Eqbal's 1319/1940 Tehran edition); also dli.ernet.439493 / dli.ernet.437743 (Horn's 1897 Göttingen edition, 'Lughat Faras')",
 "lookup_hint": "Look up the headword (entries grouped by final letter); FRS_pages.txt has \\f page breaks (567 leaves). Pagination differs from the 1365 Kharazmi edition Nourai cites — verify the entry, not the page.",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS.txt"
 ],
 "page_offset": "different edition — no mapping",
 "covers_etymology": false,
 "notes": "Persian OCR fair. Ganjoor does not host Loghat-e Fors."
}
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
{
 "title": "H. W. Bailey, 'Hvatanica II' (glossary of Khotanese words), BSOAS 9.1 (1937) pp. 69-78",
 "edition_found": null,
 "kind": "archive_djvu",
 "url": "https://archive.org/details/bailey-studies-1930-1993 (Robert Bedrosian's open compilation \"Selected Writings of H. W. Bailey\"; Hvatanica II = PDF pp. 313-322)",
 "identifier": null,
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BLY/BLY_Hvatanica_II_BSOS9_1937_pp69-78.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BLY/BLY_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BLY/Bailey_Studies_1930-1993_bedrosian.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BLY/BLY_bailey_studies_pages.txt"
 ],
 "page_offset": "BLY_pages.txt: 11 leaves; printed = leaf(1-based) + 67 (leaf 2 = p.69 ... leaf 11 = p.78).",
 "lookup_hint": "JSTOR only (BSOAS 9, 1937-39). Not on IA. Bailey's Dictionary of Khotan Saka (ISS_alt_DKS.txt, open) supersedes Hvatanica for the same words.",
 "notes": "Open full text obtained (article extracted from the compilation; the whole 114 MB compilation with 80 Bailey articles is kept alongside and also covers Hvatanica I, III, IV and other Bailey papers)."
}
{
 "title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995",
 "kind": "local_scan_ocr",
 "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)",
 "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages_faseng.txt"
 ],
 "page_offset": "115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X).",
 "covers_etymology": true,
 "notes": "Actual title is «ماده‌های فعل‌های فارسی دری» (Qoqnus). Open scan downloaded (image-only) and OCRed. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Entries: headword, then 'فارسی میانه ... < ایرانی باستان *...' with Latin transliterations (best read in *_pages_faseng.txt or on the page image). | OCR text, printed = pdf-5"
}
```


## [2026-09-14T00:57:41.050Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FFD pdf page 49 (printed 44) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==49' incoming/FFD/FFD_pages_faseng.txt | head -60",
 "description": "Read FFD printed page 44"
}
```


### [2026-09-14T00:57:42.132Z] TOOL RESULT

```
=== FFD pdf page 49 (printed 44) ===
awk: cannot open "incoming/FFD/FFD_pages_faseng.txt" (No such file or directory)
```


## [2026-09-14T00:57:45.049Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && ls; echo \"---\"; grep -n \"پوسیدن\\|پوس\" FFD_pages.txt | head -20",
 "description": "List FFD dir and grep pusidan"
}
```


### [2026-09-14T00:57:45.131Z] TOOL RESULT

```
FFD_asmaneketab.pdf
FFD_pages.txt
FFD_pages.txt.pages
---
1232:پوسیدن
1233:(پوسید» مادهٌ ماضی جعلی است» از مادهٌ مضارع ساخته شده است.
1234:پوس < ایرانی باستان 0۷8۵*. برای 2 > آرای. 8 برای ساختن ماد آغازی از ريشه
1235:به‌کار می‌رفته است. 0۷ صورت ضعیف ريشةٌ 080 است. ريشهٌ 020 «پوسیدن» معنی
1236:می‌دهد. «پوده» به معنی «پوسیده» از ريشهٌ 020 گرفته شده است. به شرح زیر:
2493:40 : (ريشه < پوسیدن) ۴۴
```


## [2026-09-14T00:57:49.282Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && sed -n '1225,1260p' FFD_pages.txt; echo \"=== which pdf page ===\"; awk 'NR<=1232 && /\\f/{c++} END{print \"formfeeds before:\",c}' FFD_pages.txt; python3 -c \"\nt=open('FFD_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nidx=sum(len(l)+1 for l in lines[:1231])\nprint('pdfpage', t[:idx].count('\\f')+1)\n\"",
 "description": "Read FFD pusidan entry and locate page"
}
```


### [2026-09-14T00:57:50.417Z] TOOL RESULT

```
[pdf page 49]
با فعلهای فارسی دری
است» از ایرانی باستان ۳۳-۱۵*. برای 1۵ -> آراست. 8 که صورت ضیف 34108
است» صورت اصلی 007 است» 8 پیش از ۲ به # بدل شده است. 3208 و 002 به معتی
: «نجات دادن» هستند. پوزش فارسی دری بازماندهٌ 88215 فارسی میانه است که هم
«نجات‌دادن) و هم «عذرخواهی‌کردن» معنی می‌دهد. «پوزیدن» به معنی «عذرآوردن و
معذرت خواستن» است.
پوسیدن
(پوسید» مادهٌ ماضی جعلی است» از مادهٌ مضارع ساخته شده است.
پوس < ایرانی باستان 0۷8۵*. برای 2 > آرای. 8 برای ساختن ماد آغازی از ريشه
به‌کار می‌رفته است. 0۷ صورت ضعیف ريشةٌ 080 است. ريشهٌ 020 «پوسیدن» معنی
می‌دهد. «پوده» به معنی «پوسیده» از ريشهٌ 020 گرفته شده است. به شرح زیر:
< فارسی میانه 08028 < ایرانی باستان 0-12-12*. برای 1۵ > آراست. 12 پسوند و
صورتی دیگر از 00 است.
بوشیدن ۱
پوشید < فارسی میانه 006810.
پوش ج فارسی میانه 005.
پوییدن
پویید مادةٌ ماضی جعلی است. از مادهٌ مضارع ساخته شده است.
پوی + فارسی میانه 00 < ایرانی باستان 0200-2*. برای 2 > آرای. ريشهٌ 0200
به‌معنی «دوبدن) است. (5 هم در فارسی میانه (دویدن)» معنی می‌دهد.
پیراستن
پیراست < فارسی میانه 0217351 و ۷۲391 0817381 د. ایرانی باستان -21-739م*
است و ۷۱391 ۷۷1-139-18*. برای 18 + آراست. 1 و 2211 هر دو پیشوتد فعلی هستند.
[pdf page 50]
ماده‌های ماضی و مضارع فارسی دزی سس ها ۴۵
58 به جای 134 آمده» 4 پیش از 1 بدل به 8 شده است. ريشهٌ 4 به معنی «(منظم کردن»
است. «آراستن» هم از ریشةٌ 134و پیشوند فعلی 2 آمده است.
پیرای + فارسی میانه 08773 و ۷13 به ترتیب از 021-730-8* و ۷:1-734-2*. برای 2
> آرای.
78 (۷۲3 را به صورتهای «ویراستن)» «ویرای» به فارسی دری آورده‌اند.
پیمودن
پیمود < فارسی میانه 0277030 < ایرانی باستان 2021-3-12 *. برای 12 -> آراست.
1 پیشوند فعلی است. ريشهٌ ()133به معنی «اندازه گرفتن» است. 021-۳3-1۵* ایرانی
باستان باید در فارسی میانه به صورت 2271730 می‌آمد. به قیاس با ۶737 و 8700
به‌جای آن 027884 آمده است > آزمودن.
=== which pdf page ===
formfeeds before: 48
pdfpage 49
```


## [2026-09-14T00:57:59.187Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BLY && awk 'BEGIN{RS=\"\\f\"} NR==6' BLY_pages.txt | head -80",
 "description": "Read Bailey Hvatanica II p.73"
}
```


### [2026-09-14T00:58:00.310Z] TOOL RESULT

```
                                     HVATANICA                         II    73


 parajs- 'hold firm', so also p
 phara 676 may be phara, Skt
 pharsa'vata a title, see kaysa
 pharra-, Sogd. farn, BSOS v
 batha- 'armour', confirmed
  cit., p. 401).
beittd 618 : samu kho hambievu beittd harbidd 5ichai 3jye; with 616 tramu

     mdrarmdu
     nitcana       kho ttamdu
             inddi samv  hvamnda     hambiita
                                 hamargya.      hambada.
                                            Confusion  of ysiiysuna
                                                               'pus' cvt ye iliva
     with ysuyanii 'taste' obscured both these passages. Beside ysei,

     ha.mblta-, hambiiva- must be connected with Oss. dmbuyun 'to
     rot ', Mid. Pers. hambisistan, pfitak, NPers. anbiissdan, pfisidan
     'to rot', Av. Skt. payv-. In medical texts passim jeh- is used for
     'heal', hence beitta rather from band- 'bind'. So render:
     618 'just as when he binds up the fester, all his disease is removed';
     616 'as when for a man, the fester full of pus, if he has ointments
     outside it, is no more than a hamdrgya (-?-)'.
biysman- ' urine '.
byiirru 687 ' 10,000', Av. baevar-, here treated as a verbal form under
     byiis-. Besides the phrases in BSOS viii 121, note also: tcause
     kfila pjrma hastiisa laksa byiri hauda ysari hastase. The corre-
     sponding episode of the Mahavastu iii 114 mentions the
     &Skiyamandala.
bremn-' weep '. The story of Asita 25234 ff. is well known: at sight of the
     child Asita wept. It is the asitamy tv a'ru-pariplutiksam of
     Buddhacarita i 62 (ed. Johnston). Mid. Pers. bram- 'weep'.
     In the Samghata-siitra brem- corresponds to Tibetan nu
     ' weep '.
brorcu, brokye, braukyi, brocd. No parallel version has yet been noted,
     but it is probably to be connected with brord, Skt. bhakta-, Tib.
     yi-ran-ba (' glad '), and with puror- 'to remove'. The -r- of
     brorcu is then original.
murdsa- 'peacock '.
mraha- 'pearl': mirdhe, Skt. muktd, Tib. mu-tig, has nothing to do
     with marakata- (Gr. ordppay0os, NPers. zumurrud, Tib. mar-
     gad, etc.) 'emerald ', but may represent a form of tkapyapl?'r7s,
     Mid. Parth. mrgryd, Mid. Pers. mwrw-ryt, NPers. murvdrfd.
ysariiihe 215. itce pastdte ysariie tcalce jahe. With yseruna, yserina
     <*zari-gauna-, yseruna tturngara 'fresh (= green) ginger'.
     Mid. Pers. zargon, NPers. zaryiin.




                            This content downloaded from
          71.172.217.118 on Thu, 11 Feb 2021 00:49:26 UTC
                    All use subject to https://about.jstor.org/terms
```


## [2026-09-14T00:58:07.223Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"\\[pdf page\" BQT_v1_pages.txt | head -3; echo \"---\"; grep -n \"پوسیدن\\|پوده\" BQT_v1_pages.txt | head -20",
 "description": "Grep Borhan vol1 for pusidan/pude"
}
```


### [2026-09-14T00:58:07.287Z] TOOL RESULT

```
---
1470:قیاس‌باید کرد» ودرائنای سخن کلم «دانستی»را بیپوده بسیار آورند. زبان
16226:های ییپوده و عث را هم کفته اند - و مردم
21538:رامر بپوسیدن هم‌هست- و بائانی ممروف سخنی
22828:۴ رك : بیپوده ۲
29543:و بپوده ۷ - ودروغ - و تروبر و عکر وحیله
29567:بمعنی هرزه ویبپوده - و دروغ و محال- ومکن
```


## [2026-09-14T00:58:14.167Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nprint('formfeeds',t.count('\\f'))\nprint(repr(t[:300]))\n\"; echo \"---\"; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));import sys\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1)[:3000])\n\"",
 "description": "Inspect BQT v1 structure"
}
```


### [2026-09-14T00:58:15.458Z] TOOL RESULT

```
formfeeds 776
'\x0c۱ ۵ ۱! ۱\n7 موم ۳ لام\nم ۱ 0 و طق صفرررنیاعدریرماروی\n۰ ۱ "۳\n۳\nم و اس مر هر وه او\n7 رین خلت ریز یتایب بره ات\nلف\u200cبال ۶۲ .یرک\nا اند کل داي رشب , رمع\nفان تا تا\nرن 9 3\nکرحم تن\nاد شش مرا\nمو رم | مر\nوک رهب اه نات مج\nلش\nوان روکد ور\n۱ و\nطراول ؛ | ع اس\nچاپ دوم فروردین ۱۳۴۳\nبا تجدید نظر کامل\nبسرمایه کنابفروشی ا'
---
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


## [2026-09-14T00:58:19.120Z] TOOL CALL #42: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:425 --image 2>&1 | head -60",
 "description": "Fetch Borhan page 425"
}
```


### [2026-09-14T00:58:20.244Z] TOOL RESULT

```
no scan of BQT covers printed page 425 (see 'scans' in refs_online.json)
```


## [2026-09-14T00:58:26.219Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfor i,p in enumerate(pages):\n    if 'پوسیدن' in p or 'پوده' in p or 'پوسید' in p:\n        print('--- leaf',i)\nEOF",
 "description": "Find leaves with pusidan in Borhan v1"
}
```


### [2026-09-14T00:58:27.368Z] TOOL RESULT

```
--- leaf 52
--- leaf 385
--- leaf 429
--- leaf 537
--- leaf 563
--- leaf 596
--- leaf 597
--- leaf 712
```


## [2026-09-14T00:58:30.265Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (429,430,428,425,426):\n    print('=========== leaf',i)\n    print(pages[i][:1800])\nEOF",
 "description": "Print Borhan v1 leaves around 425-430"
}
```


### [2026-09-14T00:58:31.461Z] TOOL RESULT

```
=========== leaf 429
نت و ۵ ٩‏ حه
باددر هشت ه بسنی باد در کف است
که بی‌ماحصل و نهی‌دست و مفلس باشد .
باددر فام ۱- بک دابع و سکون‌زای
فارسی و نون بالف کشیده و بمیم زده . غلبه
و بساری خونراگومند در اعضا .که سب آن
ریشها و دملها تولد کند . ۱
باددست » مردم تهی‌دست - ومسرف
و هرزه خرح و تلف کننده را گویند .
ددم - بح رایع وسکون میم که
از کی است که خود را بر از باد نخوت وغرور
کند .و عتکیر و متجبر نشیند .
بادد ان - با رای قرشت بروزنآسمان,
نام فرشته‌است که باد را حرکت دهد و ازجایی
بجایی برد ۴ - و مردم مثکبر و صاحب نخوت
و طالب سری و سروری باشد - و بادژن‌ومروحه
رانیز گویند - و فاعل وامر باین هعنی‌هم‌هست .
پاذدس ‏ بر وزن دادری . خانه‌ای را
کون که از چهارطرف آن بادآ ید .
باددم م بن‌رای قرشت وسکون میم؛
بهوده وتباه و ازکار بازمانده را گوبند ؟ - وکار
های ییپوده و عث را هم کفته اند - و مردم
رعیت را یز کوبند ۴ ؛ و بفتح رای فرشت هه
بنظر آمده است . ۶
بادر نگ ‌ بفتح رایع و سکون تون
و کاف فارسی ؛ نوعی از خبار باشد که خورند -
و ترفج را یز کوند و آن میوه‌اس تکه پوست
آنرا مربا سازند 9۵ - و بمعنی اسب جلد و تند
و تیز همآمده است - و نوعی از کهواره باشد که
ترا بیاویز ند و طفل رادرآن خواباتند وحرکت
دهند - وییماربی باشد که‌بسبب غم و نمهخوردن
عارض شدهباشد» وآن چنان بود که در رودمدردی
و افخی و قرااری بهم رسد و اف‌پیچش کند .
بادر نگ بو یه - بررزن و معنی ید
رنجیویه است » و آن‌گیاهی است که عقرب را
هلاك کند و اءراض سوداوی ویلغمیرا نافع‌باشد.
و بادرنجبوبه معرب. آنمت و درعربی مقلهاتوجیه
کوننه ۱ .
بادر نگین - کنابه از ترو بت‌است
که قصیده و غزل و قطعه و رماعی ماشف -
بادرو - بر وزن تازیو . ربسانی است
که آ نرا بادرنجبوبه کویند - ونوعی از خاواست
۳ تص *باد» خود فرشته ایتخاد وه مارا
۴ - چون‌بایشان بازخوردآسیب‌تاء‌شهربار جنکه‌ایشانعجز کشت وسحرامشان‌بادرم .عنصری‌بخی.
۴ - جلد بشکول دان و خوش پدرام بادرم شد رعیتان را نام . « ازفرهنگستظوم *.
۵ - پهلوی ۷2۲208 « ناوادبا۱۹ : ۲» «اونوالا 46 ب و ۰۲۷۳ , طبری ۷۵۲88
۱ « واژه نامه ۷۷۶ *. در فارسی بادا
=========== leaf 430
باد وح
که جربی بادروج گویند ؛ د بسی کوبند بادرو
تره‌ایست که بر کش بسپرغم میماند و بوی ترنج
میدهد
پاددوج - بسکون جیم .کل بتان
افروز باشد و بویدن آن عطه آورد وکز دن
عقرب را نافع باشد , و آثرا پعربی ضومردهفرح
القبالمحزون (۱) خوانئد » وبعن ی کوندریحان
کوهی است ٩‏
بادرو ده ت بفتح‌زای نقطه‌دار ۰ بمعتی
هرروزه باشد - و خوراك و فوت هرروزه را نیز
کوبند - وجامةٌ کپنه و لباس ی که هرروزیوشند-
پادر و 4 « بنتم نون , باد رنجبوبه را
کویند وآن ریحانیاست ممیوف ۴ .
بادره بسکون ثالث بر وزن بادشه »
سخن گفتن بی الدیشه بود - و تشدی و تیزی‌در
کارهارا نیز گوبند -. وبمعنی یاچ شلوار و تنبان
هم هت » و باین هعنی بفتح ثالث هم | مدهاست.
بادر یس » بکر رابم‌وسکون تحتانی
و سین بی‌نقطه » چرم با چوبی باشد مدور که در
کلوی‌دوك کنند بجهت آنکه رسمان یکه‌میر سند
یکجا جمع شود و بعربی فلکه خوانند » وبسنی
تابی را گوبند که زنان بدوك دهند - و نزتَختة
کرد میان سوراخی باشد که بر سر چوب خیمه
کذار ند - وممصنی بادزن هم‌آمده امت. .
بادر یسه - بنتج سین بی‌نقطه . بسنی
بادریی است که آن چوبی ,با چرمی باشد که در
کلوی دوك صب کنند - و کماج خیمه را نیزبه
مشابیت بدان بادره گوبند .
پاذر پسه چشم - کنایه از مردم يك
(۱) چك : مفرح قلالسهزون .
دس وا
چشم باش د که بعربی اعور خواتند - و کنابه از
شطان و دجال هم هت .
ناد ه یک ثاك وسکون زای‌فارسی,
سرخی‌ءفرطی‌باشدمامل به‌بنفشیو کمودتو کدورت
که برروی حردع عارشض شود ۵ و مب آن خون
سوخته بود که بر رویآدمی دود؛ و بعضی گویشد
صفرای سوخته است. وروی خداوند بادژ ؛ شبیه
بود برو یکی کهابندای‌علت جذامش باشدوبسنی
این علت رامقدمةٌ جذام میدانئد ؛ و بسن ی کویند
بادژ سرخ‌باداست وورم خونی راتیزبادژمب‌گوشدب
و پیمئی شراب لملی هم آمده است .
بادر ام ه با فای بالف کشیده و بمیم
زده , بمعنی اول بادژ است و سرخی و بنفشی
و کدورت و کمودت روی باشد.
بادر کام ه باکاف » بروزنوه‌منیبادژفام
است که سرخی وبنفشی و کمودت روی باشدو عضی
آنرا سرخ‌باد گویند 5
باثد ۵ « بنتح زای هوز و سکون عیم.
کارهای عبث و بی‌نفم را گویشد :
بادر فا - بان
=========== leaf 428
 هریداب‎
باك بره » بنتح بای ابجد و رای‌فرخت.
نام روز یست و دوم )۱( همن حاه باشف. کو بند
عفت سال درابران باد نیامد» درین‌روز شبانی‌پیش
کسری آعد هکفت دوشآ نمقدار باد آمد کهعوی
بروشت کوسفندان بچنبید » پی حد آندوزشاطی
کردند و خوشحالی لمودند. و باین تام شهرت
۳
بایر ۵ - بنتح بای‌فارسی و رای‌قرشت.
ترا چوب را کون د که دروفت تراشیدن چوب
بیبزد - ۱
باثیریی » بکس شاك ‏ باد سبا را
کوبند و آن از ما بين مشرق و شمال وزد ؛
و بعشی باد دبوررا بادبرین گویشد چنانکه شمس
فخری گفته است. بیث :
بزعر چرخ‌مرین بی‌مثال فرمانت
زسوی‌غرب‌نبارد وزید مادبرن .
بادیج بروزن مارییج » ریسمالی‌باشد
که در ایام عید و جشن از جامی آویزند و زنان
و کودکان برآن فشنند و در حوا آنند ورو نك ,
و باين معنی بجای حرق ثالث زای نقطمدار حم
عقت لس 9ب
باد پیز ن بادزن را گونند, و بعریی
مروحه خوانند .
باد پیما س با بای فارسی بروزن کارفرماه
مردم مفلس لابالی بی فابده گوی و بی ماحصل
و درو غ گوی را گومند - و کنابه از اسب واستر
و شترئیزرفتار - و مودم‌سیاح و بیابان گردباشد .
بادپیم‌ودن کنابه ازکارهای بی نفع
و بهوده و ی فایده کردن و حخن غیر نحقیق
گفتن باشد - و بمعنی شراب خوردن عم بنظر
9
لاد تم - بروزن چهار تخم . رآزبانه
و بادبان را گویند .
بادخان - باخای نقطه‌دار بروزن[ سمان,
۱( چك : دوم .
حه هم 4 ه
بادگیر و گذرگاه باد باشد مطلفاً خواه دربلندی
پادخافی - بر وزن شادسالی » نام
چشمه‌ایت در قرية هوا که‌یکی از فرای دامفان
است گو مشد | کرانداد اندكك چیزی مردار درآن
چشمه افتد باد و طوفان بمرتبه‌ای شودکه آدم
باث حن بروزن بادزن » رهگتر باد را
کوند - وباد گیر وخانةٌ باد گیر رانیز گفته‌اند.
باد حوان با اومعدو له برروزن‌شادمان»
کتابه ازمردم هرز کوی و خوشآعد کوی‌باشد
و معرف را نیز گویند .
با خوود لک کی است‌سیاء و کو پيك
واو پیوسته درپرواز میباتد. گویند غذای او باد
وگن درجایی شیند . دیگر شواندبرخاست؛
بادخون بضم رآبم‌وسکون واوونون»
راه کذر باد - و خانة باد کی دار باشد .
باددار را دثل ید بروزت حا کار 4
مردم بی‌تعلق و هج‌انگ": باشد - و مردم‌متکبر
و صاحب 
=========== leaf 425
ی ۷۰ ‌-
پاخر و بنتحالت وسکون رای‌بی‌هطه
و زای نقطه‌دار , نام فصبهابست در خراسان ونم
کوشه‌نی باشد از چهل و حشت کوش موسیقی .
باخسه - با سین بی‌هطه‌بروزن باغچه.
راهی باشد بفیر از راء ثعارف خانهای که از آن
راه نز آهد و رفت نوان‌کرد - و نثتر حجام را
نیز گوشد .
باخود - بروزن کافور , نلبجد ایراهیم
کگویند سکه درم در ژمان او بهمرسید .
ممدوله و نحتانی و شین فرشت » سر یب فرو
بردن و خوطه خوردن باشد - و بمعنی تنهابی
هم هست . ۱
باحه - بفح اك » کاسه یشت‌ولاگیشت
را کوشد .
پاك ۴ « بر وزن شاد , معروف است که
كي از چهار عنص باشد - و نلم فرشته است
مو کل بررتروج ونکاح- ونام روز بیست‌ودوم(۱)
از هرماه شمسی باشد و ندییر و مصالح آن روز
پدو تعلق دارد . نك است درین‌روز نوبر‌مدن‌ونو
پوشیدن و براسب نو سوار شدن ۴ - و کنابه‌از
حدف و سخن هم حست - و بمعنی ابود و هیچ
باشد - و کنابه از تندو تیز هم هست - و منح
و ثنا را نیز کوبند - و بمعثی آه وناله هم آحده
(۱) چك : دوم .
است - و نام کنج دویم (۱) است از جملةٌ هشت
خسرویرویز و کنج بادآوردهمین است ؟ -
و بمعتی‌لخوت رغرور وخودیینی هم هست سوأسب
را نیز گونندکه بعربی فری خوانند - و بمعنی
شراب هم بنظ آمده است - و مخفف یاده
باه] بله س بل حلاك کننده را گویتد
باذاد نگ * - بننعرای‌فرشت‌وسکون
نون وکاف فارسی » ترنج‌را کویند و آن‌میوه‌ایست
معرو ف که‌پوست آنرا مرباسازند وآنرابادابنگه
حم میگوه مد . ۶
باداش « بروژنآ دای » مکافات وجزای
نیکی را گربند» وبابای فارسی هم آمدماست ۷ -
باد] فر اه ۲ - بافا و رای قرشت بوزن
آرامگاه ؛ بمعشی عقوبت و جزای کناه و مکافات
بدی باشد و بادفر را نیز کوین که بازییلاانال
است؛ ون پوست پاره‌ای باشد مهو رکه رسمالی
درآن گذرانند ودر کشا کشآ ور ند تابکردش‌در] مد
و صدابی از آن ظاهر شود ۸ .
پادافر اه ۲ » بروزن ماءدر عاه ,بمعنی
بادآ فراء است که جزا ومعافات بدی‌باشدد ویاژمسةً
بادافره ۲ - بحنف الف سیم ()
اطفال باشد ۸ . ۷
ضه درصفحً ۲۰٩‏
=========== leaf 426
نکن مم ینظر آعده است ٩‏
ادا فنجیر - نومی از درخت انجیراست
که یش از هم درختان موه دهد و انجیر آن
کاواك و پرباد میباشد .
بادان‌فیروذ - نم خهرآردیل است
و چون فیروز آن شهر را بنا کرد باین نام‌موسوم
ساخت چه بادان بممنی آبادان است.؟ .
باد) نگیز » نام کلی است که هر گاه
مزارعان خواهن که غله را از کاه جدا کنندو باد
نباشد آ نگل را بدست مالند و بر ک آنرا بر
هوا یاشند باد بهم‌رسد .
بادآ وود » نام کنم دوبم (۱) است
هشت کنج‌خسرءپرویز سد ی 5 زر
و گوهر بیکی از جزایر حصنه میفرسناد انفافاً
باد کشتی را بحوالی اردوی خسرو پرویز آورد
بادام شکوفه فشان - کنابه از
بادامه - بفتح میم ۰ یله ابریشم را
8 شتر هم آمده
است - و چشم مانندی باشد که از طلا و نقره
سازند و بر کلاه طفلان دوزند - و خال گوشتی
را هم گفته‌اند ۰ و آن اژخ مانندی است که‌بیدتی "
از بشر؟ میدم برمیآبد - وهردانه و حلفلزنجیر
را نیز کوبند - و رقعه و پینه را نیز گوین که
درویشان برخرقه دوزند - و خرفةٌ مرفعه را هم
میگوند » بعنی خرقه ای که ازیاره های رنگین
فراهم دوخنه‌شده باشد - وجنسی از ابر شمباشدب
و هرجنس مطبوع را یز کفته‌اند .
بادان - بر وزن نادان . مخفف آبادان
است که‌شیض‌خراب باشد - وبمعنی پاداش‌وجزای
۱ - باین ممنی ظاهرا مصحف «پاداش ‏ پاداش» است . راك : باداش . ۴ - ور
ممجم‌البلدان «باذان‌فیروز» ونیزدرمتن‌برهان وسروری *فیروز گرد» ودرثاهنامه «پیروزرام*» وقولی
بادان‌پیروز با آبادان پیروز نام قدیم اردبیل است که فیروز ساسانی در فرن پن<م میلادی آثرا بنا
کرده است «دائرتا لمعارف اسلام : اردیل».
بقیه ازصفحهٌ ۷۰۵
این روزرا «باد» خوانشد . «روزشماری ۵4-۵۳ . ركك : روزشماری ص ۸۲
۴ - رك : بادآور . ٩‏ طبری ۷2۲208 « واژه نامه ۶۷۷۶ گیلکی و
رك : بادرنگ . ۱ رد : پاداش. ۷ - بهلوی 02111725 (یادانی) م رکب از
۳۵۷-2 . جزو دوم مشتق از ۳85] همربشه و بمعنی پرسیدن « پیب رگ ۱۷۹ جمماً بسنی
بیرسیدن ۰ بازخواست . ۸ رگ : بادفر .
٩‏ که از يك کناه ار برفنم زراه
فتادم بباد افرءٌ تک اد اسدی .
#ادای _ آی(آسیا) که با بادکردد. (مر کب از:
باد ۳- آی راك : این‌دو کلمه ] )
» #دام ‏ پپ
```


## [2026-09-14T00:58:44.136Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\nfor i in (537,563,596,597):\n    print('=========== leaf',i)\n    print(pages[i][:1200])\nEOF",
 "description": "Print candidate Borhan leaves"
}
```


### [2026-09-14T00:58:45.294Z] TOOL RESULT

```
777
=========== leaf 537
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
تلبلی آورد . د
=========== leaf 563
۳۳
خوانند .
لیو ث » بر وزن ربوند » بمعنی غدر:
است که بیوفابی کردن باشد .
ی ۵ » بروزن هیوه» بمعنی غرمب وتنها
باشد - وزنی را نیز کویند که‌شوهرش مرده‌باشد
با او را طلاق داده باشد - ومحردیرا یز گویند
که زش حرده باشد - و نام داروبی است که
بر که آن سر که کیرماند اما خار تدارو و ی
آن بخیار شباهت دارد(۱) لیکنکوچکترازآن
باشد وآنرا بمربی قثاء البری‌خوانشد وقتاءالحمار
همان‌است .
بیهله ۴ - بکسر ارل و ضم ها بروزن
دل شده , مخفف بهوده است و معنی نا حق
و باطل باشد» چههده بممنی حق است.- ویمعنی
بی نفم هم‌آمده است و جح اول جامه‌ای را
(۱) خم ۰۳ چك : بخبار دراز .
۹ را اقرب الموارد : بین.
بیهوده
کویند که از حرارت آتش زرد شده باشد .
دیق بنتح اول و اكث وسکون ثالی
و قاف » دام شهریست غیر معلوم۴ .
یهن بکراول بروژن‌سجن, خاریشت
بز رکه تیرانداز را کویند یعنی خارهدای خود را
ماشد تیراندازد .
لیهو ۵ - بقثح او بر وزن فرسود »
چیزبرا کون د که نزدبك بسوختن رسیده وآتش
آلرا زرد کرده باشد - و بکسر اول هم آمده
2 ۱
یو ذه - بکس اولبر وزن فیروزه:
بمعنی بیپده است که نا حق و باطل باشد -
و بممنی پی نفع هم آمده است - و بفتح اول
جامه ای را کویند که نزديك بسوختن رسیده
باشده .
۴ - مرب بیهگه
۴ رك : بیپوده ۲
بیپنه ویهوده..
۴ رله ؛
=========== leaf 596
بحطیجه
بتطیح - با لامبروزن زنگیجه:بمعنی
یخلوچه است که زیر بل کسی را خاربدن باشد
بعنوان خوش طبمی .
پدر پاشد؟ - و ختح اول درختی را گوبند که
ح کر بار ندهد۴ - و بضم اول چوب پوسیده
باشد کهآ کر کنند؟ .۱
, بل بو بطم اول و بای فارسی بروزن
ودایم و پاینده .هم‌هست.
ید د خق4 - بسکون‌خای قطه داربروزن
عر جسته 0 غمکین واندوهتاله را گوبند" ۰
فد ۵ س بروزن تبرزه ؛ طمامی‌باشد
که‌آترا در رومال ولنگی بندند واز جایی‌بجایی
برند وا را زله گویشد - و بمعی حصه و بپره
۱ هم‌آعده است م و بسص یگوبندهرچی ز که دررومال
ولنگی بسته شده باشد . چه آن رومال بته را
مجموع پدرزه خوانند .
بدر ام ‌ با رای_ قرشت بروزن‌اسلام»
بمعنی آراسته و نیکو وخوش وخرم باشد- وجای
(۱) خم ۳: خشنود . (۷) چش : خسف .
۱ - رك: بخلوچه. ۴ چنانکه: بدندر(ه .م) ورك: بدر.
عرب.*«لفت نامه *. ۴ - آنرا بود نیز گویند دلقت نامه» . رك : پده .
* - ازاوستا 0۵۱۸1.۲2۳020 ۵ (فی: رام) «اسشق ٩۲۸۷‏ :
ای تلزه بهار سخت. پدرأمی پيراية دهر وزیور عصری . «منوچهری‌دامتانی ۹٩۱‏ .
۱ - ززادن چومادری (عادر زال) پردخته شد ز داش ازآن دیو پدرخته شد .فردوسی‌طوسی.
بنقل فرهتگها . لکن این کلمه بنظر درست نمي آد » و در لفت نامه ولف نیز نیامده است.
« لت نامه ».
۵ پدر - در لهج مر کزی بکر اول وفتح دوم و در لپجه های شمالی بفتح حردو ۰
هلوی ۳۶٩‏ و ۳۲ دیب رک ۰۱۸۰ ؛ بارسی باستان و اوسنا ۳112۶: ه
=========== leaf 597
مت ۳۱۲
فد ۱۵ - بروزن‌فرسود؛ بمععنی‌سلامت
باشد - و بمعنی وداع فیزآمده است -
لف‌4۵ ت بر وژن صدمه » بمعنی حصه
وبهره وزله باشد - و هرچیز رانیز گوبند که در
لنگی ورومالی(۱) بسته باشتد ,
ید ند ر ۴ بر وزن سکندر, پدرسبییر۱
کویند که شوهر مادر است » و بر وزن نضنفر
و حق نظر عم آمده است .
بدو ار بروزن پرواز ۰ دوچوب بلند
باشد که هردو را از عم باندگ فاصله برزمین فرو
بر نده و چوب دیگر بمرض بربالای‌آنها بندند تا
کبوتران و گاهی جانوران شکاری برآن نشیتند
وآنرا بعربی میقعه خوانند۴ - و در موبدالفنلا
کردا کرد کلاء ودهان انسان و حبواتات دنگر
ببان
باشد از جالب بیرون - ومنقار مرغان: . .
پل « بفتح اول و ثانی, دام درختی‌است
که هرکز بار ومیوه ندهد و آنرا بعریی غرب
خوانند ۴ و منم اول چوپ پوسیده بائد که
آراآتشگره سازند. و بمر بی‌حراقه گوید ۹
و باینیمنی فتح اول هم آمده‌است. *
بمعثی ظهور باشد که از ظاهر شدن و نمابان
کردبدن امت- وبمعنی موجود هم هست‌چنانکه
کوبند + پدیدار آمد» یعنی موجود شد.
پد سار باسینبی‌نقطه بروزن پدیدار,
برسرکاری دفئن باشدکه پیش ازین شروع درآن
کرده باشند و
پر قت « یکر اول و سکون شانی
و رای بیطةٌ مضموم بفا و فوفالی زده » ماضی
(۱) چش : رومال .
پذرفئن باشد بعنی قبول کرد و معترف شد » چه
۱ - پهلوی 04ت +08 «نولدکه . کارنامه »٩۵‏ (قس : درود) «اسشق ۲۸۸ : «( علی
فریب) بامن (بوصر مشکان) خالی کرد و گفت : ب
```


## [2026-09-14T00:59:01.108Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (710,711,712,713):\n    print('=========== leaf',i)\n    print(pages[i][:2200])\nEOF",
 "description": "Print Borhan leaves 710-713"
}
```


### [2026-09-14T00:59:02.256Z] TOOL RESULT

```
=========== leaf 710
هعئی با زای نقطه دار نیز بنظرآهده ات
ترر بان » بروزن همزبان؛ بمه‌:ی زبان
آور وشخصی که کرم کفنکو شود و خن هی
ثر وتازه بگوید - و بمعنی ترجمان هم هست
یمنی شخصی که لفتی را اززبانی بزبان دیگر
قرب کند ۷ .
فر ۵۵ بسکون ثالی بر وزن سرزده »
بیعنی اول ترده ۱ ست که قبالة خانه وباغ باشد »
- وقنح انی بروزن تبرزه هم‌آهدء ۲ ست.
تر فان بروزن ومعتی ترجمان است
یمنی شخصی که لفتی راز زبانی بز بان دیگرسیان
کند ؟- وترزبان را نیز گوبند ۴ و آن شخصی
باشد که سخنهای تروتازه نقل کند.
نرس- بخم اول و سکون انی و سین
بی‌نقطه» بمعنی سخت و محکم باشد- ودر عربی
سیر را کوبند که ترکان قلقان خوانند - و نم
اول ونانی زمین سخت باشد ؛ و باین معنی بفتح
9
اول دضم نانی هم گفته‌اند - وبفئح اول وسکون
انی ممروف است که خوف وبیم باشد ۴ .
قر سا ه بر وزن تنها » ثرسنده و یم
بر نده وء امه کننده‌را گو ند و نصرانی ٩‏ وآش-
مرست را نیز گفتهاند ۷
ترس استودان*- بنتح اود
وسکون ثانی و ثاكث و همز؛ مفتوح وسین دبگر
موقوف و فوفانی بواو زسبده و دال بالف کشده
بنون زده دعا وزند ویازند (۱) خواندن فارسیان
ات یه ووو من اه تمه منک :له که
گونند چونروح از فالب مفارقت نماید سه‌شانه
و او را دز این
سه شبانروز ترس دم بسیار است ٩‏ لهذا دراین
سه روز برسردخمة اونكك خوانند تا روح‌اواز آن
ایمن گردد . ومعنی ترکیبی اين لفت خوف فبی
است چه ترس بمعتی خوف ویم‌باشد, واستودان
دخمه ومقبره را کوند . ۶
0
)۱( چيك: زند وبا ند.
. رك : ترزفان‎ ٩
«اسشق ۰۰۷۸۶ اتکاه
رك : ترسیدن .
راهب‌نیز درعر می بهه ین معنی است
۴ بارسی اسثان و اوستابی ۳25 ‌
۱ - بهلری 2۲521
۳۸ چنانکه
ای کریمی که از خزانة غیب
٩‏ - در ندش فصل۲۸ بند۱۸] مده:
۰ کلستان ۲ *.
۵ رل : اسنودان .
. دیو وبزرش بردر دوزخ
ث رسندفه» خالف.
=========== leaf 711
یو اس
آلرسه- بفتح اول, قوت واهمهرا گویند ‏
رصم اول فوس تزح را )۱( 3
تر شدن ه کنابه از اعراضی شدن
و آزرده گردیدن باشد ببب ظرافت کردن
تر شاك ضم اول بر وزن اردك »
نام پرندمایست سبزرنگه - و بر که کياهی است
اه
ترش یا - کیاهی است‌ترش خموساء
وه رگیاه ترش‌را نوان کفت عموماً .
فر شه- بن اول و تانی و فتح الت" نام
میوهء‌ایست -٩‏ ورستنیی باشد که تضم آندا بعرمی
بزر الحماض و حب آلرشاد خوانند . اکر قدری
از آن‌نخم درخرعه بندند» وزن بربازوی چپ‌ندد
مادام که باخود دارد آیستن نشود. ۶
تر شیناث. بروزن گل چنك. رستنیی
باشد بوستانی که بعربی حماض کویند ؛ و نخم
آنرا بزه الحماش خوانند ؟ .
فرع » بنم اول و ثالی و سکون ین
تقطه دار , اسبی باشد سرخ رنگه که آن را
کهر خوانند ۴ .
قرغاذه - بروزن ادزه. غالبوساحب
حکم وسر کش وک ی که حکمها ازروی غالبیت
ور کی کند - وسر کشی کردتیرا نیز کویند.
قر تغاق - بنتح اول بر وزن چخماق »
بای داشتن شبها د خبر دار بودن را کویند -
ویضم اول عم باینمعنی آمدیاست.
قر هه با دال ابجد بر وزن طبقچه .
گرفته شده وترنجده» وهرعنوی وبندیومفصلی
که سب درد مندی و آزار آن حرکت شوان
کرد . گونند « ترغده شده است » ۰ و بروژن
غمکده هم آمده است که بفتح نالث باشد -
ترش مه بکسر الت بر وزن ورزش ۰
نوعی از زرد آلو و فیسی باشد .
فرغو ‏ بر وزن بد کوء نوعی ازباقتة
ابررشمی سرخ رنگه باشد.
(0) چش: قوی وقرح‌را:
اد ۲۳
از آن کز تو ترسد شری ای حکیم
و گر با چنو صد بر آیی بجنگه .
« کلتان ۲۸ .
باشد. ضد شیرین.
مقابل: شیرسی .
=========== leaf 712
آر قنج» بر وزن شطرنج , راه باريك
ودشوار را گویند ۵ .
آر نك ۱ » بروزن‌فزند » بممنی‌مسال
و بپوده ۷ - ودروغ - و تروبر و عکر وحیله
باشد۸
آر هه بر وزن برف , کشكه سیاه را
کویشد و آنرا بعربی مصل وبترکی قرافروت
خوانشد - و کمكك سفید و پر خشك را نیز
گوینه ۱ .
ان صم بضم اول وسکون ثانی و
بالف کشیده بسین بی‌لفطة زده, ی
است و آرا هکل نیز گویشد .و آن رمتئیی باشد
که از زیر خمها وجاهای نمناك روبد ۴
تر فان » فر ورن دریان» «عفقف ترزفان
است که ترجمان و شخص زبان آور باشد * .
و بای ابجد بالف کشیده . آشی را گونند که
قاتق آن‌از قراقروت‌باشد ۹
وبا بمعن ی آش باشد:
ترفرروش- کنایه از کسی‌است
بظاهر خود را 0
قفر قذا ٩۵‏ «بروزن‌شرمنده: پمعنی‌ترفند
است که‌دروغ- وییهودس وت وبرومکروحیله باشده
+ باین هعنی‌بجای حرف الث قاف هم بنظر آمده
است - ویمعنی قرس ودیم هم‌هست.
تر فینه* اس ون کشکینه , آخررا
کونند که فاتق آنرا فرافروت 0 باشند .
تر قنفه ۷۱- با قاف پروزن شرعنده .
بمعنی هرزه ویبپوده - و دروغ و محال- ومکن
وحیله‌باشد ,۵
فرقیین « بروزن تقین, بلفت نبعی‌خعطی
است که محرران دربنی‌محل‌میان دوحرف‌بی‌مد
(۱) چك: ۷۹
9 9 کرمان ]21 :
بشمر توفند ار ترف بودم و رخبی پند و حکمت اکذون چو شکر وقندم .
سوزنی سمرفندی. «لغت نامه حرف‌پ ص2۲۵
۴ رك : لك ] : ۳۱۰ . ۴ - رك : ترزفان و توزبان . ۳ ۱
( ۳9 -- با (‌ .۴
۵ راهی کو راست است بگزین ای دوست دورشو از راه بیکرانه ونوفنج.
رود کی سمرقندی. «لغت فرس ۹5.
۱ - از اوستابی 1۳۵0 ت , 666/1۷24 ( دزدیدن » با نقلب سرقت کردن ) ؛ بهله
۳ (بحیله ربودن) "هندی باستان - ۰00۲28 ۳۵8816) (انتقال بافتن. تغییر دادن)
قی بونانی 1۳6۵ ,در فارسی: ترب (حبله ومکر) «استق۳۸۹*.
۲ - باهتر او همه هثرها بافه باسخن او همه مخنا ترفند .
فرخی میستانی «لفت فری۸۸*.
۸ - چون خود نکنی چنانکه گوبی پند نو بود دروغ وتسرفند .
«ناصر خسرو بلخی*۹*.
٩‏ -ركٌ : ترفند. - از: ثرف (ه .۸ ۲- یله (پسوند اسبت) -
ی : ترفنده .
» تر قه - بفتح اول ودوم وسوم مشدد ومخفف. از: ترق (اسم صوت ت رکیدن چیز) ,
(پسوند پدید آورنده آساز صوت)؛ باروت و مواد منفجره .
=========== leaf 713
وامالآنرا نی زکفته‌اند - و گذاشتن و گذشتن
ونرك دادن وخلاصی از تملفات‌جسمانی وخواهش
نضالی و گشتن ازماسوی‌افه بجذیات حفانی,ونراد
باینمعنی عربی هم هست6 - ونام قصبه ایست از
مضافات آذربایجان ‏ و بنم اول و سکون انی
ممروف‌است که‌نفیض نازمك باشدء ‏ و کویندترکان
از ارلاد بافث بن نوح‌اند و ولابت ثرکتان‌رانیز
بطریق مجاز تراد میگویشا - و کنابه‌ازمطلوب
ومعشوق وفلام باشد۷ .
ثر کان‌چر خج- کنابه از سبعاٌ ساره
است که زحل و مشثری و مریخ وآفتاب و زهره
لت ومای أت
تر کافی س بر وزن قریانی» بالایوشی‌را
٩‏ - ترقین؛ سیاه کردن موضعی را بفرد حساب بخط زائده تااکمان نشو دکه‌ابنجارا برای
نوششن سفید کذاشته‌ند «غیا» :
هسند نست بحق بارز مجموع وجود وآن د گرها همه ترفین عدم‌را تفصیل .
انوری آبیوردی بنقل *المعجم شمس فیس چاپ مدری۲ ۲۷
۳ - ظاهراً اصل اترك است ولی دود مزبور در شمال خراسان جاری‌است. رأه:جفرافیای‌طبيمي.
کیهان۲ 4۷ .رردیدیگربنام«بر ک» است. رکه:پ رکه ۴ از: تر 4 (پسوندیدید آورندشاسم
ازصفت) تر حلوابی‌در آ ذر بابجان «ارمغان‌سال۱۲ شمارث۷«کاف» بقلم 7-3 وی*ودر کیلان‌هممُمو لاست:
۴ اسم صوت از: تر کیدن . 8 از عربی وارد فارسی شده. بت 3
جنم‌اون درتر کی بممنی شجاع و دلیر وسخت «جفتابی ۲۱۳ ۴ ۰ درچینی 6لاع_لا1 » در ونانی
[101۲*0 ,نام ترلك بعنوان قومی بدوی نخستین بار درفرن ششم میلادی دیده میشود. در همان
فرن تر کان دولتی بدوی تاسیس کردند که از معولستان و سرحد شمالی چین نا بحر اسود امتداد
داشته است . موسس حکومت مزبو رکه چینان اورا ۲760 - 11[ نامند ( در کنیبه‌یای ثرکی
0 درسال ۵6۲ در گذشت وبرادرش 15181 (درطیری [ , ۸٩۵‏ و ۸: منجبوخاقان)
که در مقرب فتوحانی کرده . ظاهراً تاسال ۵۷٩‏ زیسته است . این دو برادر کویا ازآغاز منتفل
ازیکدیگر حکومت میکردند .
چینیان ازدولت مزبور بنام امپرانوری تی‌کان شمال وامپراتوری ترکان «شرق یاد کرده‌اند.
7 در سال ۵۸۱ تحت نفوز -لسلهٌ چینی أفاگ اين دو امپرانوری بطور فطع از بکدیگی جدا شدند
وبه‌دها هردونايم‌سلملةً چینی 208" (۱۱۸ -۹۹۷) گردیدند . درحدود سال ۱۸۲ .ترکان شمال
موفق شدند استقلال خودرا بدست آورند . دربار؛ روابط این ترکان قدیم و اخلاف آنان حث‌های
بیار شده است که درین مختصر جایآنها نیست. برای‌اطلاع بیخثررجوع بداثرة المعارف‌اسلامذٍیل
5 نود . ملله های ترك که در ابران دورة اسلامی سلطنت کردماند : غزنوبان ( ۳۵۱ -
0 +) ۰ سلجوفیان ( 4۲4 - اواخر قرن شم )» خوارزهشاهیان(* 6۷ .)٩۲۸-‏
*_غلامان و کنیزان تر که نژاد زا بودند. بدین‌مناسبت تركیمعنی معشوق زباروی‌بکار رفته‌است.
کشند و باطل کردن عبارنی
```


## [2026-09-14T00:59:10.672Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'پوست' in p or 'پوشید' in p or 'پولاد' in p:\n        print(i, p[:60].replace('\\n',' '))\nEOF",
 "description": "Locate p-u section in Borhan v1"
}
```


### [2026-09-14T00:59:11.886Z] TOOL RESULT

```
11 سه ژبا نبای‌ایرانی نعستین بابتخت هخامنشیان بوده و بو نانیان 
95 هشتاد وهفت مزایای برهان قاطع د - سخنی چند دربارة برهان قاطع 
99 نود ويك عایس برهان چنانکه خوداودرهقدمه میبگوید که فصدداشته ا
103 نود وپنحع نقایس برهان مثالع-< کر یمان. بروزن نریمان؛ نام جد 
104 "مقدنمه ۰ نود شش آن‌شر اب خورد مست نگردد... ۹6‏ این‌بود نمو 
137 صد و بیست و نه کتاب حاضر ۴ برخی اعلام تاریخی‌و جفرافیایی درم
156 مقدمه صد و چپل و هت مع۷[ وفع :۳6۱6۷ ال 2۵۵61 ,(مق .6) عماعمت
170 تالیف کتاب دیباجة موف ۱ ۳ فرجام‌رسانیدموخا تمصحیفة انبیا وفا
217 "آب سیه « یکی اك , مخخف آب سیاء انت که شراب انگوری - و علت ک
227 عمل کردن ویبروی تىودن ناحکام شرمعت باشد . ] چالك - با جیم فا
238 آرا آداه بروزن خارا . آرایش. وآرایش کننده و آراینده را کویند
244 در دل کسی‌جای کند ؛ وباین معلی بازای نفطه‌دار هم آمده است . 
249 ۳ آسا آن را « حب الآس » خوانند ۴. کونند عمای موسی علیه السلا
255 ی آشنا کر خابة سک آنی است ۷ . خالهرا نیز گویند چنانکه گوبند 
278 آویزه وروت آوفزه « بر وزن پاکیزه , کوشوارء راگوند . ٩و‏ لژ ۵
279 اه ۲ هنیا به (۱) - با بای ابجد و نون و بای حطی وبای بيكك قطة
282 آهو پای عب را نیز گفته اند "۱ خواه با مردم باشد و خواء با چی
292 مگ بر آن قبر میهد ٩‏ - د الم خخضصی که کاتای شا تلاح هو : آ ی
297 ی سس اعشی وسکون ثانی و جیم . میواست که آنرا خاوسی «تریج» اگو
304 اخی» بر وزن مفی ؛ کاری و چیزی‌را کوبندکه قابل تین باشد - وصا
305 و تشنگی را فرو نشاند - و بفتح اول ‏ و کسرثالث در غربی اهر بد
309 خوانندش, وبعض ی کویند منسوب‌باردیل‌ین ارمنین است وتا کردة او
312 بخشایش » بمعنی خیر و خیرات و چیزی در راه خدا بمردم دادن باشد
321 سب ۱۰۵ تت ضحاك می فرمود بکشند و مغز سرایشالرا بجهت مارالی که
325 << ۶+ )راد - یک اول بر وزن خبار » بن و تك آب را خوانند - و د
327 ما ارم » جح اول و سکون.تانی و میم » بنتی فد باشد ‏ ارمل س بر
335 اسیندار هف ۱ - بش میم وسکون ذال نقطه دار. بروزن ومعنی اسفندا
342 استینه ۱ وورم وآمای کرده باشده وی سرعابی‌را گویشد که برجراحت
351 - و۱۳ اسمنك بفتح اول وثالث وسکون نانی اسمند‌ر » بنتح او » پم
354 اشتر گیا - بکر کاف فارسی و تحتانی بالف کشیده , بممتی اشتر خا
357 _ٍِِ اشکو خیدن . مصدر اشکوخ است که لفزیدن دبسردرآمدن وافتادن
367 افگنده(۱)سم کنابه ازعجز وزاری بسیارباشد . ومعرب افلاطون‌است 
371 حم اي ٩‏ سه معلوم » نام کتابی از بپودان است: - بلفت بونانی و
384 انج - بفتح اول وسکون ثانی و جیم» اطراف 2 روی و رخار ( ۱ ) با
385 - بو - ) فحل س بفتم اول وکسر ثالث و سکون نانی ولام» رسثنی با
388 اندر خور ا ندز خو در - بنمخای نفطه‌داروسکون واو ممدو له و را
401 ای ۸ اه نیز خواشد ره ۳ اورمز ۱ نم اول و میم و سکون وین ثالث 
423 بت ۷۲۰۳ ح- قلعهٌ آن شهر بوده چاهی است عمیق . گویندحاروث و ما
425 ی ۷۰ ‌- پاخر و بنتحالت وسکون رای‌بی‌هطه و زای نقطه‌دار , نام
429 نت و ۵ ٩‏ حه باددر هشت ه بسنی باد در کف است که بی‌ماحصل و نه
445 2 بالاده ع بروزن آماده. اسب جنیبت‌را کون که اسب کوتل باشد ٩‏
451 الو خوداست چنانکه‌شاسته حشتیو اجب‌الو حجو د(۱) را گونند . و 
452 سموده رستم اندر کوههای ۰ و پوست آبرا جیبه جامه ساخت . خاصیتش
454 وتیردانی را کوبندک» پر از نبر باشد » ومعنی تر کیبی آن‌بت مان
470 بر جوسیوی ۳ بر توسوسن سین اول مک ور وتحتانی بواو دسیده و بسی
477 ده نسکهای عشهور زند )۱( آست سی و پنج برسم بدست گیرید ؛ و بجه
478 می شیر آن" زین نهادن سرخ‌مرد گوبند و بعربی عصا الراعی خوانند
481 ۳ بر گ ید - معروفست - و نوعی از پیکان تیر هم هست که آنرا بهی
487 سای هس و بفتح او وسکون ائی‌نام ماه - و ستارمشتری باشد ۱ - و 
490 و کار بهوده و بیفایده کردن باشد . # پر ود قلكك - کنابه ازماه
492 راد ب‌آمده پز اد بر آهفه - زیی را گویند که بسیار پیر شده باش
494 کنفه . کوبند که‌درخت‌پسته مکال میوه‌فزدار بارآورد و یکسال بی
497 ایوان و مفه را گویند , و تک اول حم آهده است . بسك - بنتم اول
498 بستان تم اول بروزن برهان » کلزار و کلسان‌را کوشد , ومشفف بوس
505 7 و۷ حه بشلشگه - بکس اول و ثالی و سکون نالث و فتح شین نقطه د
510 ٩‏ . و چرن واضم او ساخته فراخانی حفگفعد ور اکتون خنایی۱ اندا
528 مصفر بن است ۳ که حبة الخترا و چنلافوج . باشد , و آن بیثثر در
531 هه بولرد بنیاد بر بخ نهادن- کنبب. از | جممی را کوندکه بر اصن
538 لهراسب ؛ بممتی خواب دیدن باشد و جربی رژبا خوانند . بوشیاس - 
545 ی ۳۹ ده بهر ام تل - هی مر فج توح کتک هر اهج -_بنتح میم و سکو
548 غشب را فرو نشاند ۰ و او موکل است ب رگلوان و گومقندان , اکثر 
555 - ۳۳ 7 یر دک بنتم رابع بر وزن نك بی » بمعئی برژه انته ات صمف
605 پرنح پردختن- بر وزن برجن ۰ مخفف پوداختن است که بمعنی فارغ گش
606 پرده دار فلك پرده داد قلاك - کنابه ازماء است که قمر باشد . ۱
608 ستو! بکر اول و #الی وسکون الك و ضم فوقانی و واو ساکن . بمعنی
614 پرعدوار و ثل وار ۱ نتمولنانی‌وسکون مه بش فب ریز کته که ریخب 
615 و قری وییم وباگك٩‏ -و سروب رکه را نی زکوین و بمعنی داشتن (۱)
623 ۵ بفتح اول وسکون‌ثانی ودالابجد, بمعنی خون باشد که بعرچی دم گ
632 پشت پاخارمدن شدن و خوش آمدن و خوشحال کردبدن جاشد ۱ ۰ فست با 
644 بیان هیجد هم (۱) در بای فارسی با نون مشتمل بر شصت ودو لت و ک
652 . بودان تروش فوفانی ورای بی‌نقطه وسکون واو وشن‌نقطه دار" نام
653 4 ۷۲۷- ود یان - بکرثاك بر وزن‌حوربان» ۱ رای شهر کنوح۱ هم هست
660 یاب وبکر او عخفف یه بات دکه درچراغ سوزند - وشمم تیز سلزند ۷ 
664 پیراهن فبا کردن پیراستن وزینت دادن راگویند مطلقا- و دبافت کر
665 پیر فلا کنابه از کوکب زحل پیر كاخ - بکسر اول و سکون ثالی و ف
675 بح «یینکی» برروزن زیر کی غذودنی باشد ین ۱ با نون بروزن لموء 
685 - هی ع < باشد چه اززبان نازی زبان عربی وازاسب تلزی اسب عر هی
718 ترلك دوال و فتراك باشد ,ربت رکی‌قنجفه٩‏ گوند؟ . تر لاث . بکر
747 و کنابه . از دهان خویان هم هست - و بمعنی فروبردن و نایدید کر
753 ححه اي سس زوسن خاموش‌بودن - و فریب دادن‌هم 0 تنیده ۴ بر ون د
755 صوا داد نت تو بال . و توپال۱ , لفت اول با بای ابجد ودیگری با
760 تورنگه تور نگ س با انی مجپول بر وزن هوشنگه , خروس صحرابی‌را 
761 اي حه قوژ ه بازای فارسی » بمعنی آخرتوز است» و آن پوست درختی 
762 و سشگه هنم اول با سین بی اقطه بر وزن هوشنگه ۰ ی تفت است که ر
```


## [2026-09-14T00:59:41.477Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(666,684):\n    head=pages[i][:120].replace('\\n',' | ')\n    print(i, head)\nEOF",
 "description": "Scan Borhan leaves 666-683"
}
```


### [2026-09-14T00:59:42.473Z] TOOL RESULT

```
666 علت برص وجذام داشته باشده ۴. | ودنه باثانی مجهول و دال بررزن | بی سوزن » عبل نمودن و اراده کردن بطرفی | باشد . | لیسه ۴ » با ثان
667 تن پش باز | و مواجه ویرابر و مقابل را یز کویند وکنابه | ازدو لت م هست. | لیشا نی ۵اد - بارال ابجد بالف کشیده | و برای قرشت زده ۰
668 پیشواز است که بعربی استفبال گوبند و نوعی | ازجامة پرشیدنی هم هست . | پیش خاه - بسنی رواق است که | بیشگاه خانه باشد - و ایوانی 
669 ۳و | فیشگاه « باکاف فارسی بروزن ثیرماه» | بیتی صدر- و صدر مجلس هردو آهده است - | وفرشی‌را نیز گوبند که‌درپیش افکنند. وفرش یکه | 
670 شطالی باشد .3 | ی اد بایای حطی» بروزن وععنی | بیشکار است ت که خادم و خدستکار اک رد | ومزدور وش دست‌باشد ویمصی بیشاب و شاش | هم ه
671 وشرط را گونند ۳ | لیتا- بکسر اول بر وزن جیفه » چوبی | باشد بوسده در ولابت خوزسنان و آن را دای | ی ۲ بکاربرند بمنی باستگه و چشم
672 بان. مقراضه | دو شاخ باشد | فیکانی » با کاف بر وزن شبطانی . | نوعی از لعل و فیرءزه باشد ۷ - و جنشی از | توشادر ح‌ هست که برشکل و
673 - ۷ - | پیالاد ۵ - بارای‌قرشت بروزن مینافام, | نام حصاری است ت عظیم‌و بز رگث. | بیل‌افکندن کنابه از عاجز کردن | باشد . | یل آهرو ۵
674 پیل معلق در عوا | یل معلق درد هو کناب اژابیباهد | یی سه بر وزن زیلو ؛چویی .که بدان | مسواگ کنند وعریان اراك خوانند - و بار درخ
675 بح | «یینکی» برروزن زیر کی غذودنی باشد | ین ۱ با نون بروزن لموء کشك‌باشد | که دوغ نرش خشك‌شده‌است‌ویعربی اقطوبتر کی | چکده رانیز
676 پیوسته گری | شو سته گری فوند کرد | و موافقت نمودن را گویند. | وکاف فارسی » بمعنی عروس باشد ؛ و بنمثانی‌هم | درست است۷ ۰ | بو گانی 
677 گفتار چهارم | از کناب برهان قاطع درحرف تای فرشت با عروف تبجی | مبتنی‌بر بیست وچهار بیان ومحتوی بر هشذصد وسی وشش لفت | و گنایت 
678 است - و بیمنی که باکاف مکوراء تممال‌میشود . | همجو*وافف باش‌تا نیفتی» و#برخیز تابرویم *عنی | واقف باش که نیفتی و برخیز که بر
679 وجام و شیلةٌ آلوان کنند وگاهی خالی گذارند . | و کاهی هردرطرف آنرا پنجرء کنند - و گلخن | حمام وکور سکری و آهنگری و امتال آرا | 
680 تايه زر - یواح | ناتلی » بکسر ثالث بر ءزن غافلی » | سفره ودستار خوان‌را گویشد. | تاتوره بر وزن ماشوره ؛ چدار؟ | و نجاوي باشد ازآ
681 ی او | تاجداد - کنابه از پادشاه است - | رن و محافظت کنند ناج را یز | گویتد.- | تاچر ان - بنم جیم ورای قرشت بالف | یده و بئون زده »
682 هم‌آمده است که مشثق از ریختن باشده . | تاخیره - بر وزنتاجیره» خت‌ولالع | و سرتوشت را گوبند - و بمعتی اصیب و قسمت | وآنجه برآن 
683 تادون ه بر وزن قارون » بممنی_ تیوه | وتاريك باشد؟ . | تار هیخ- با ین نقطه دار بروزن‌چهار | میخ » بخاری باشد که در ابام ژمستان
```


## [2026-09-14T00:59:48.743Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(654,665):\n    print('======',i)\n    print(pages[i][:900])\nEOF",
 "description": "Print Borhan leaves 654-664"
}
```


### [2026-09-14T00:59:49.942Z] TOOL RESULT

```
====== 654
یوستین بگازر ۱
وعیب جوننده باشد ۰
(وستیی در بدن » کنابه از افثای
راز کردن باشد .
کردن. وعیب نمودن باشدا .
که بر وقت رشتن مردوك محند.
زره وجوشن را گویند - وامربردورشدن‌ویکناری
رفتن هم عست یمتی از راء دورشو - ونام کیاهی
است کهآ نرا میکویشد وشافپا میسازند واز جانب
ارمن می‌آورند و آنرا پوش دربندی میخوانند .
نقری را نافم است » و شیاف خوزی همان‌است.
و‌شا؟ - با ات بالفکشیده. پوشنده
وپوشند کی را گونند؟ .*
بو شث با ثانی‌مجهول بررزن‌حوشك»
بزبان ماوراء النه رگربه را گویند و بعربی سنود
خوانند؟ .
بو شگان - با انی مجهول ر فتح الث
وک‌اف فارسی بر وزن م وکشان. نام نوایست‌از
موسیقی - و بمعنی مغیبات‌هم‌هست بعنی‌چیهابی
که درعالم غیبت‌اند- وبسکون ثالث بروزن‌دوستان
نام جایی و مقامی است نردبك‌به نیشابورومقامی
۱ "۳ رژ۵: دوست کردن.
5 ود: بوشنج ۰ 3 له: بوشث.
۵ - کلکی 0۲ .
اسشق ۳۳۹
8۷ سم
است از مقامات سالك که آنرا بعربی غیب‌الفیب
مفدس تجلی لماید وفانی درحق ومافی در وگردد.
بو شنگ سب با ثانی مجپول بر وزن
هوشنگه , نا
====== 655
و
پولاب بر وزن دولاب » بم‌نی
حس باشد و پولاپی‌حسی, بعنی‌|نچه بحس ونظر
درآ مد ۱ ۰
که از آن‌کارد و شمشیر واعثال‌آن سازند -وتیغ
و شمشیر را نیز گویند - و نام پهلواتی است
ای ال اج و نام دو ست ماز ندرانی و اورا بولاد
غندی میگفته‌اند عم غین نقطه دار - و ب‌عنی
و3 هم هست.
ولاد خسای « کنابه ازاس‌سرزور
ماشفد .
و لادد که م کنابه‌از اسب‌پرزورباشد.
بو لادسنحان کنانه از دلاوران
وسارزان واساحه داران باشد ۰
بو لاد هندی ۰ کنابه‌ازشیترهندی
باشد 5 3 ۰
4و لافی ع با ثانی حجهول بی وژن
طولافی » نوعی از اش‌ارد باشد .
و [4 س با ثانی محپول بر وزن لوله .
خریره مضمحل شده را کویند - وهندوانه‌ومیوه
های دمگر را نز گفته‌اند که درون آنها نرم
. فوبه
و ضایع شده باشد .
زسن را گونند که تکلتو باشد .
وک - بر وزن جوی. بمعنی پوبه‌باشد
که رفتار متوط است یعنی نه نند و نه آهسته,
و بعضی رفتار تند را گوشدب واعر بدیشمه‌نی «م
ست ععنی راه رو وقدم‌بردار .
پو با ۶ بروزن کویا» رونده‌را گویشد
- و بعضی دونده را نز گفته‌اند .
بویان ۴ زان جو ب
====== 656
4 بفتح اول وسکون ثانی » کلمه‌است
که هنگام تصین با حیرتآمیخته برزبان رانن
وتکرار نیز کننه؟ ۰
یاه » بر وزن بهانه . چوبکی باشد
که درود گران درشکاف چوبی که باره‌مشکافند
فرو برند و کفشگران مابین کفثر و فاب نهند
و گاهی در زیر در گذارند تا سته و کشوده
کی
4 4 بفتح هردو بای فارسی وسکون
تین با حيرتآمخت هگوشد .
بر * بم اول بر وزن ظهر ؛ مدرسةٌ
جهودان را گویند - و بقتح اول دك حصه از چپار
حصه روز و چهار حصهثش باشد چه شبانروزیرا
بهشت حصه کرده حربك را پهر گویند. واین در
هندومتان یشتر مصطلح است .
۱ - رك؛ په‌به » امروز به‌به گوبند .
۳
۵۵
ومحافنت باشد .
هر ه داد - با دال ابجد بر وزن
هرزه کار ۰ باس دار ومحافظت کنشدمرا گوند.
پهلو- بفتح اول و سکون ثانی وضم لام
بواو کشیده, معروف‌است وبعربی‌جنب خوانند ۴
- و بفتح لام شهر را کویند مطلفاً چه پهلوی
بمعنی شهري باشد - و تواحی اصفپان را تیز
کنته‌اند و مردم شجاع و دلاور باشد - ومردم
بزر که وصاحب حال راهم میگویند چه مراد از
راه پهلوی‌راه بزرگان بزدانی‌است *ونام ولاشی
هم
====== 657
4۳ اس ۱ بهلو صاییدن
بهلو دادن کنابه از حثفت
رسانیدن - و تردیکی نمودن باشد - و دوری
کردن و کناره کزدن - و روکردانیدن را لیز
پهلو داد - کی رااکوین که منفت
رسان باشد- و سغنی را نیز کوبند که کزند کی
ودشنامی درضمن داشته باشد 5
بهلو در دن» کتابه از برابری کردن دد
ال وقدر ومرنبه باشد .
پهلو ساییدن - بمنی پهلو زدن
بهلو آن - بروزن نبروان: مردم سخت
وتواناودلاور- وقوی‌جثهوبز رکه وضابط _ودرشت
آندام - و درعت گوي را گوشد ۳
بهلوانی « بروزن لن ترانی » شهری
وزبان شهری را کوبند - و منسوب به‌پپلوان هم
هست - و زبان فارسی باسنانی را نیز گوبند که
فارسی قدي‌باشد ۴ .
پهلو تهی کردن - بسنی کناره
کردن و دوری گزیدن باشد - ویرهیز واجتناب
نمودن از چیزی و از کی و تنپبا شدن هم
هت -
۱ - بپلوان منسوب به‌بهلو ( پارت) است. الف ونون در ابنجا علامت نسبت است نه
نعانه صغهٌ جمع؛ و نظایر آزیدر فارسی سیار است : بامدادان» موب بنامداد (هنگام بامدادا ۲
کیلان منسوب بگیل (مکان کیل) ۰ توران منسوب بتور (مکان تور) « ابران باستان ص۲۹۶۱ >»
====== 658
است که کنابه از برابری کردن در عال و فدر
وهر تب باشد.
هلو از دن» کنابه از گربختن ودو
برنافتن- وترلك دادن و اجتناب نمودن و احتراژ
کردن باشد .
بهلو کند ‌ بعنی بهلز نهی کندو کناره
گر ند «دوری نماد ویگریزد ِ
پهلو نهادن م کنایه از خواییدن
پهلوانی- وشهری- وزبان شهری باشد» ومنسوب
به‌پهلوان وزبان فارسی هم 2
بهله بفتح اول وثاك وسکون ثانی ؛
ولات اصقهان وری ودینور باشد ۴ .
پهمز له بازای هوز بروزن احمدك »
خار یشت بز رکب تبر انداز را کویند کد سخول
باشد ,
هن « شح اول و انی بر وزن دهن »
شریکه پسب مهرباتی‌دریستان مادر طفیا نکند.
و بسکون ثانی ممروف است که پشت و پخش
وعریض باشد ۴ . #
باشد .
بهلوی ۲ » بر وزن منئوی ؛ بمعنی
: مر.کب از: پپاو (ء .م) 4 نی ( مسوند قبت ) ؛ معنی تسین آن بارتی است‎ - ٩
سپس بعهنی زبان معمول درعود پارتیان و مدها زبان‌عهد ساساتیان | رف : حقدمهٌ آفای پور داود‎
بو ۲ ۶۳ بر کاب حاشر یمعنی . خروی و سلطنتی 4 امروزه بهلوی‎
بزبانی ابرانی که اصطلاحاً پارسی مباندمینامند اطلاق‌مبشود و آن‌را بردوق
====== 659
ی
بهنا 4 بروزن مستانه , نوعی‌از میمون
باشد- وکلیچةٌ روغنی را لبز گود .
هنال بروزن کمند. دامی باشدکه‌بدان
آهو گیر ند.
(م ی و - بروزن فدفور » چیزیست مانند
دستنبوی که بزبان عرب آن را حنظل خوانند
وقنامالنمام(۱) همان‌است- ویمعنی بهی‌نیز هست
که خرزحره باشد .
44 س ختح ارل وثانی و تالث . بمعتی
بهن‌است» و آن شیری باشد که سیب مهربانی
بیار دریستان مادر طفیان کند - وبسکون ثانی
چوکان بازی و کوی بازی باشد - و نوعی از
سازند و گوی را در آن نهاده بر خوا اندازند
وچون تزديك بزمین رسد باز بهمان پهنه‌میز نند
[۴ نگذارد که برزهن آید ی تمفصل رسانند ۰
وآن‌را جربی طبطا بکوبند- و پهنی ران آذمی
و حیوانات دیگر باشد از جاب درون و آن را
بربی قطن خوانند - و بمعنی میدان هم آمده
خوانند وچوبی باشد مخروطی تراشیده که‌اطفال
رسمانی برآن پیچند و نوعی برزمین اندازند که
تادیرباز بگردد ۱ .
ی « بنتح اول بر وزن سهی ۰ حنظل
باشد و آنراخریز؛ تلخ‌هم هت و خرزهرمرا
چوکان را نیز گوشد که سر آنرا مانشدکفه یز پهی خوانند ؟ .
بیان بیست ویکم
ی 
====== 660
یاب
وبکر او عخفف یه بات دکه درچراغ سوزند
- وشمم تیز سلزند ۷ -
یمیت بروزن سراب. بمعنی پاباباست
که ین‌حوض وته جربا باشد وبعربی قمع رکوبند -
وتهات عرچیز را تز کفتهاعد - و بمعنی تاب
لبادم بر وزن زباده . هعروف است
که قض سواره باشد ۴ - ونام مکی‌از مپرهای
شطرنح عم حست - و نم کلی است ممروف -
از عردم یی سواد باشد یمنی علم و فنلی کسب
تکروه بلشد .
یباده نهادن-کنابه از زبون داتن
وعلجز اتکلشتن باشد . 9۶
ار دشتی- بکسر .اول و زای هوز ۰
دوآنی است که *ن را جربی صل‌الفار خوانند .
کوبنه اکر حوش بخورد میمیرد , و از خواص
او اتت که اک رک رکه بای بربر که آن ,گذارد
حمین که مزدارد لنگه شده باشد وگن سای
توقف کند الیته بفتد وبمیرد .
هیا لش یا کاف . تسیر پیاز است -
مه
وکیاهی را لیز کون دکه ازآن بوربا بافند -
و نوعی از کرز باشدکه سر. آن را با زنجیر
چو کن خوانند ۴ - ونام قربه‌ایت دردامن کوه
معدن لمل ۵ .
یا کیی- املیباشد قیمتی۷ ومنسوب
بقربه مازك را نیز گویند.
فاد یز « بکس لام و سکون تحتالی
و زای نقطه دار . نوعی از از 
====== 661
و۳ ««
پیاهو - با های هوز بر وزن ترازو .
هم عده است کهخالة شش بهلو 7
اری ماشد ٩‏ ۰
فیتا۵؟ - بانای قرشت؛ زد زن و معنی
ت بلغت زند و بازند (۱).
لیترسب؟ - بدر اول و سکون ثانی
و .فوفانی و رای می نقعله مفتوح بسن مي نقمله
وبای فارسی زده , نام بدر پورشسپ اسث که جد
یفام است
برست ات .
شقات- با تای قرشت بر وزن مخك »
کرمیست که جامهای ایرشمی را خورد وضایع
و ۵
له بروزن هیج . بمعتی تاب و حلقه
و خم باشف ب و کنابه از رشك و حند هم
هست .
پیچبا * - با بای فارسی بسر وزن
پیشوا . خرچنکه را کویند که بمربی سرطان
خوانند .
پیچاگ - بای مجهول بروزن قیجك ۰
(۱) چك: ژد و پاژند :
۱ ‌- ره 5 آهویای.
۶ اسشق+ ۳4عرك : بیام.
و مربی آن دا عشقه و لبلاب خوانند ۷ -
و کرو ابرشم و رسمانب و سربند زن را
دا
لین » بروزن ربوند . عصانه ویتانی
بند زنان را گومند .
لیچه » با نانی مجهول بوزن رشه .
و عذقه کویندشی  .۷‏ و زلف عملی دا نیز
گویند- و طر؛ زلف و کا کل را حم کقتماند که
پیچند و برمکدیگر گرء زتند - وموی بلف وا
نیز گفنه‌اند و بعربی عفاص خ
====== 662
تشن
ولای‌هرچیز وضله حرشیتی را کوشد ازحیوانات
پیتتن" -بروزن ربختن,بممنی پیچیدن
باشف . ۱
یتخس" بروزن ک رکس . بممنی کمان
بردن واز روی گمان فهمیدن وراه بچیزی بردن
باشد .
سای ارل و تاك پر مك
- و چیزی که 9 فرم شده باشد -
و درمانده و عاجز شده را نیز کویند - و بمعئی
هی بست 4 دبوار ی که بیخ
ومحبری ومتحصن و کرفتاروبندی رانیز گفته‌اند
و بد بو و متعفن و گندیده شده را ه مگویند »
وبضم الث یز آمده است .
پیخسته ح بر وزن برجنه » بمعنی
زیر بای نرم شدم و عاجز ودرمانده - و محبوی
و گرفتار - و بد بو و متعفن - وکمان بردن را
- و در
زر کوسد ری ی رس اسر میتی
ره
بزور باشد ۰
بمعنی ترت ومرت وتار وعار و بفایده - وهرچه
از تف آش زرد وضایع شده باشد ِ#
ید اد بر وزن شداد ؛ بمعني بیدا
وظاهر باشد .
فيك او سی» بنتح واو و سین بی نفطه
بتحنانی کشیده . درمی که در زمان کیان رایج
بوده و هردرمی به‌ینج دینار خرج میشد, وبکسر
واو هم بنظر آمده ات :۷
پیر ؟ بروزن وه‌متی پدر |
اب گوند ۵ ۰
یر ا ۲ - با انی مجهول بروزن گیرا »
و سر تراش که مو
====== 663
خافهای زیادن را عرد نی قلاف. ماهه 2
وبمعنی‌ساخدن ویرداختن ومنقح کردن- وچیزی‌را
از عیب خالی نمودن هم هست .
ثیر استو۱ « کم کردن چیزی باشد
بواسطه زبابی و خوش آیند کی همچو بربدن
ذاخهای زبادئی آزدرخت وموی زبادنی از بدن.
کوبند شبی اباز بامر سلطان محمود در حالت
مستی زلف خویش را بربد. روز دیگر سلطان
از آن حالت پریتان خاطر گفت. عنصری باین
رباعی سلطان را از کدورت بسرون آورد :
ر باعی
هنن زلف بت‌از کاسنن است
چه جای بفم نشتن و خاستن است
جای طرب ونثاط ومی خواستن است
کاراستن سرو ز پیراستن است.
سو دیاغت دادن چرم را نیز گویشد.
۳
بر استه؟ بروزن بی‌خواسته » به‌عتی
مرتب گردانیده و ساخته و پرداخته باشد -
و باغی که شاخهای زبادنی درختان آن را بریده
وعلفهای زبادنی آن‌را چده و صفا داده باشند -
و درخت ی که آن را پر کاوش کرده باشند » بعنی
شاخهای زیادتی آن را بریده باشند - ودهی را
معتی بابای ابجدهم بنظر آمده است.
نون و دال ابجد , ماضی متفرق ساختن
وافشاندن باشد بعنی متفرق ساخت ویریشان کرد
و افشانید ۰
یر آهن» با انی 
====== 664
پیراهن فبا کردن
پیراستن وزینت دادن راگویند مطلقا- و دبافت
کردن پوست را ه مکفته‌اند ‌#
پیر آهی قبا کردن - کنابه از چا
زدن و پاره کردن پیراهن باشد.
پر اهی کاغدی- کنابه از داد -
خواهی‌باشد٩‏ . وروشنابی صبح وشعاع آقتاب را
نیز کویند .
لیر ای ؟ه بروزن سیمای» زشت دهنده
باشد "که سرتراش و بافبان است . چه کی که
شاخهای زبادتی درخت دا سرد او را بشان
پیراکوبند - و پرداختن و مستعد کردن را لیز
کفته‌اند .
یر آیش- بابای حطی» بروزن و ععنی
بیراهش است که پبراستن وزشت دادن ودباخت
کردن بوست باشد. وساختن و پرداختن. وهستمد
کردن ومهیا نمودنرا نیز گویند.
ثبر اینده » مر وزن ژیباینده » زیت
دهنده را گویند که چیزی را از چیزی بجپت
خوش آبند کی کم کند همچو سرتراش و باغبان,
برخلاف مشاطه .
پیر ایه۴ ه بر وزن بی خابه . آرایش
و زیور باشد ازطرف تقصان همچو سر ترائشیدن
واصلاح کردن وشاخهای زبادتی درخت دابربدن.
و کنایه ازساختن رپرداختن هم هست؛ ودرجمیع
بفتح اول‌هم پنظی آمده است ۴ .
هیر بر فا آن» بکسراول وتح بایابجده
۱ ره کاغذی حجا
```


## [2026-09-14T00:59:58.810Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (650,651,652,653):\n    print('======',i)\n    print(pages[i][:2600])\nEOF",
 "description": "Print Borhan leaves 650-653"
}
```


### [2026-09-14T00:59:59.929Z] TOOL RESULT

```
====== 650
لذیو ۵» بر وزن خمیره » بمعنی پنیرگ
است که آن را خبازی و مل و کیه و .نان کلاغ
خوانند و شاب گردله را تنز گویند که
است » و پنبر از آن جهت کویندش که میوو
آن فه‌ینین مسمانده و[ فتاب ون
کردله مرک نش میت
آنکه بهرطرف که آفتاب 0 تیلوفر - و جالوری باشد که بسربانی حربا
میکند ٩‏ . و بضی کویند 3 0 ثیلی - با ام و ور و حرکت مجبولء
بثیر له نیلوفراست- وخربارا جایی را گویند در شه رکه در آن اسباب و غله
3 گفته‌اند, وان‌حانورست وامثال آن فروشند.
از جنس چلیامه . 1
۱ وهسوه وداناآن
بیان نو دهم
در بای فارسی با واو مشتمل برهفتاد ودو لغت و کنایت
بر پش» : ‌ نوی بروزندو کش
۳
لو لسمین» بکس ثالث و میم بر وژن
رو چرکن » بل زند و بازند (۱) خودی را
کوند از آهن که در روز های جنگه بر سر
بو با ع با بای فارسی و نازی هرده
کوچك . بمعنی
هدهد و شانه سر
باشد ‏ - و دخش
مکر و دوشیزه را
لیز گویند .
بو ۰ نم اول و سکون وین
0 نز حمی
۰ معثی دارد.
لو‌ادی ه بنتح اول بر وزن نمازی ۰
بممنی درد و سوزش باشد و آن «ا بعربی جوی
خوانشد ‏
ی بر وزن خوب »
مس اک رها رب
بشتر میباشد. وبابای فارسی شانه سر را گویشد..
و 13 مرغ سلیمان هم خواناد چنانچه شپرم‌را
مرغ عیسی ۴
- بنیرد 6۵۱۷۵ از تبر: پثی ر کیان 1۷1۵1۷80605 جنسهای ببار دارد: بعضی
تکاله 2 دائمی و کلهای آن‌بننش وگل‌آن علین است . « کل کلاب ۷ ب>.
ِ - رك: پويك . ۴ - پوبو » پوبه. پويك و بوبو وصور دیگرء لاتننی۵0۳2(]
بونالی 2 ,کردی 020, 0200 «اسشق ۳۳۳ » و رك: پرندگان در لهجه‌های کردی ص
6 ۳ ۱
۱ (بر هان فاطعخد)
====== 651
حه ی پا حس ۱
بو پل" با بای فارسی , بروزن و معنی
ودر هندونتان با بر کک بان خور ند» ومعرب آن
فوفل است.
و وه با بای فلرسی بر وزن کوکو »
شانه سر وهدحدرا کویند که‌مرغ سلیمان‌است ِ
ک و کو خوانند .
لو له - بنم اول وفتح بای فارسی,بمعنی
لو تاه منم اول وسکون تانی وفوقاتی ؛
جگر کوسقند را کویند و لهذا غلیه‌ای که از
جگر کوسفند سازند قلبه پونی خوانند -
و بمعنی لوت هم آمده است که اقسام خوردنی‌ها
و انواع اطعمه و اثربه باشد - ونوعی از خربزه
هم هست ۰
و 4 - بانای فرشت
و مخزن را کوند . #۶
و خت" بر وزن سوخت : بمعنی پشت
باشد که از يختن است ۲
و ۵ نم اول بروزن سود » نقض ار
است وآن 7 باشد که دریهنامی جامه افته
میشود و تار بدرازی جامه ۴ - و آتشگیره را
نز کویند وآن چیزی بای دکه باچخماق آش
بروزن غوطه.خزانه
۱ -ر: پوپك:
۵ « واژه نامه۱۸۳* .
بزران
برآن زنند ۴ - وبمعت یکهنه هم آمده است که
در مقابل نو باشد ۵ .
لو ذات « با تای قرشت بروزن پوچات,
بمعنی محسوی باشد و پوداتان بمعنی مصوسات
بعنی آنچه بنطر وحس درآید۱ .
لو ده بر وزن روده » معتی جود است
که نقیش نار باشده چه آن درطول جامه و این
عم رفته را هم کفته‌اند ۷ - و رکوی سوخته -
وچوبی بوسیده کهآترا بجپت آتشگیره‌مهیا کرده
باشند ۴ ومعربی‌حراقه خوانند- وسوده وربختهرا
لیز کویند - و کندیده و ضایم شده را حم
کفته‌اند ۷
وه س بضم اول بروزن حور؛ بمعنی‌پسر
است که برادر دختر باشد ۸ و نام رای شهر
کنوج ٩‏ همست واو یکی‌از بادشاهان و رابان
حندوستان بوده. ومعرب آن فور است- وکسی‌را
یز گونند که خود را نادان و هیحمدان
وانماید ٩۴‏ - ودراجرا نز کفته‌اند و آن پرنده -
است ممروف .
پی دنه بروزن توران » نام شه رکنوج
است ومعرب آن قنوج باشد۱۱- و بمعنی خلیفه
وجانشن .- وباد گار حم‌آمده | ست- وجمع پور
حم مت که یسران باشد .
۴ طبری 6 ( بوه )۰ مازندرانی
۰۲۲۳۹ ازدسانیر «فر هگ دساتیر‎ ۳۹ ٩
-٩‏ مرب آن قنوح.
۱- رگ:پوره
کف شکردنه وراز..
====== 652
. بودان تروش
فوفانی ورای بی‌نقطه وسکون واو وشن‌نقطه دار"
نام ساحخری بوده که درزمان خود عثل و مائند
نداشته ۷ . ۱
فوران دخت س من داد بی نقطه
وسکون خای نقطه دار و تای فرشت بمعنی پسر
است نه دختر » نه يك پسر بلکه چندین پسر
است ؛ چه پوران جمع سر باشد» وان نام دختی
خسرویرویز است که پیش ازآزرمیدخت پادشاهی
کرده راورا بدین نام ازجهت آن خوانده‌اند که
ازوکارهای مردانه بظهور آهده است وأورا نوران
سل ملوله تر کسنان‌وده؟
مجهول و را و دال بی نقطه و کاف فارسی بالف
کشفه و بنون زده » مناید دائست که فارسیان
خمسه مسترف4۶ه را بر پنج روزآخرآ بان ماه می-
افزایندکه مجموعه ده روژ شود وآن ده روز را
پورد گان مبگویند» ودراین روزها جشن سازند
وشادی‌تمایند و آنراجشن بورد کان‌خوانند,ومعرب
آن فوردجان است؟ .
9
پوددیان - با بای حطی » بر وزن
و ممنی پورد گان است که ایام جشن پارسیان
باشد .
و د شسب * «پورمعلوم» پفتح‌شن قمله
دار وسکون سین بي نقطه و بای ابجد » نام پدر
پو دعنقا - لفب زال پدر رستم است»
چه کویند او را سیمرغ بز رکه کرد وسیمر غ‌را
عنقا ثبز خوانند .
بور ك بر وژن خوبك , نام دخش
رای قنوج است و او در حبالةٌ بهرام گور بود .
پور کند با کاف بر وزن زورمند ,
طاق وایوان ومتزل را کوند» وباین‌معتی با زای
نقطه دار هم بنظر آمده است .
لبود هنك ه با میم بر وزن حوشمند ؛
صاحب فرزند و عبالمنه را کوند - و با ثالی
مجهول نام کیاهی است خوشیو .
و ده « بر وزن شوره ۰ بمعنی پور
باشد که بر است . و تنهٌ درخت را ای گوشدب
ویز بان هندی یمعتی تمام پاشد۷ . .
.
4۶ تور (سرح) ان (نست) بعئی
بعمنی(از نژاد)سفیداست وسرخاب وسهراب هردو بمعنیآب سرخ‌است. ازافادات امثادپور داود*.
۳ یگ سحیح و رورد کان است. بیرولی گوید 2 پرورد گان چخست 1 نج روز سن اندرآبان ماهء
وسبب نام کردن آن چنانت که کب رکان اندرین پنجروز خورشی وشراب‌نهتد روانهای «رد گان را
و همی کون دکه جان مرده بیابد وزآن غذاگیرد » و چون از بس آبانماه پنجروز افزوئی بوده
افتاد واندر کیش اذان میم ری بود. بي طردو ینجرا بکارهردند از جهت احشاطرا. وسست وششم
روز آبان‌ماه فروردکان کردند وآخرشان آخر دزدبده» وجملةٌ فرورد گان دمروز گشت. * «التفهیم
ص ۲۵۹ رله: فرورد گان . اهر تلا آن: فروردجان «النفهیم ص ۲۵۹ ح » .
۶ پپلوی 3۵۲0511250 مرکب از : پوروش بمعنی دو رنه : صیاه وسپید وییر +
اسب» دعنی دار ندهٌ اسب دورشگف بااسب شبر» درمر و حالذهب «بورشسف؟ ودر طبری پوستف ( بور-
شیف) آهده «مزدیبنا ص۷۶ وجدول برایر ص۹4۹» و ركك : پیثرسپ . ۱ - ازرشة 011۲
درسان‌کریت بمعنی پر کردن , مملو کردن و اسم مفمول آن در سانسکریت ۳00108 است یعنی
درشده» تمام, کامل. «د کتر کونهن راجا».
====== 653
4 ۷۲۷-
ود یان - بکرثاك بر وزن‌حوربان»
۱ رای شهر کنوح۱ هم هست -
و زای هوز » پبرامونو کردا کرد دهان حیوانات
باشد - ومایین لب و بیتی را نیز گویندسوبم‌عنی
ساق درخت هم امده است.و نقار مرغاثرا نیز
کفته‌اند» و با زای فارسی م ۲۳
۰ ۳۹
پورش ۴ - با ابی مجهول بر وزن
سوزش » بمعتی عذر ومعذرت‌وعذرآوردن‌ومعذرت
خواستن باشد .
لودن » بر وزن سوزن » زمینی را
گویند. که بجهت زرات کردن پاك کرده
بشند .
ور ه ۳ بر وزن دوزه » بیرامون
و کردا کرد دهانرا گونند - و بمعتی ننةٌ درخت
هم‌آمده اس 8۵
ود ین ه بر وزن کوزیدن . عذر
آوردن وحعذرت خواستن باشدل" 3
وس » بر وزن طوس ۰ چرب زبانی
و قرب و فروتتی را گویند۷ .
دو یا نه بر وزن روزانه » قرب دادن
وفرونتی و بزبان خوش مردم را فربفئن .
لو ست هه ی وزن دوست » معروف
۱
است ۸ - و بمعنیغیبت هم آ مده‌استکهبد گوبی
ومذمت باشد .
پوست باد کر دن -کنابه از طبار
نه دلی نمودن وراز گفتن باشد .
پوست یرای - با بای فارسی
حطی زده » چرم کر و دیاغ را کویند .
بوست دادن » کنابه از اظهار ته
دلی نمودن ومافی‌النمیر گفتن باشد .
بوست سگ‌بر و کشدن- کناب
از بی حیامی و بی شرمی‌نمودن باشد .
بوستگال ه باکاف فارسی بالف کشیده
وبلام زده ؛ پوست بی‌مویرا گوسد که درزبردنبة
کوسفتد مي باشد وآرا باندك دلبه جدا کرده
در سبراب بر ند» و دوست در کوسفند را ف ‏
کلته‌ادد که سر ککن از حودیای آنآ و بشتهات .
۱ بوستگا له بالام بر وزن بوست پاره,
بهعنی پوستگال است که پوست زبردنبةٌ گوسفند
ودوست مقعد کوسفندباشد ۰
فوست کردن - کنابه از الیس
و محرم ساختن باشد - و غیبت نمودن و خبث
کردنرا گویند .
و ستین » لباسیاست‌مسرونه۹ .و کنابه
از غیبت ومذعت وعیب هم‌هست .
۴ کردی002, ۳6۵2, افغانی 0672 .
دروس ورامین) «اسشق ۳۳۹*.
۵ رك : بوز .
نت اسم مصدراز پوزیدن ( مسعمل
۷ - ره : پلوی .
و
```


## [2026-09-14T01:00:20.956Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[653][2500:5000])\nprint('===== 654 head')\nprint(pages[654][:1200])\nprint('===== leaf 216/217 head')\nprint(pages[216][:400]); print('---'); print(pages[217][:400])\nEOF",
 "description": "Print rest of Borhan leaf 653 and 654"
}
```


### [2026-09-14T01:00:22.048Z] TOOL RESULT

```
===== 654 head
یوستین بگازر ۱
وعیب جوننده باشد ۰
(وستیی در بدن » کنابه از افثای
راز کردن باشد .
کردن. وعیب نمودن باشدا .
که بر وقت رشتن مردوك محند.
زره وجوشن را گویند - وامربردورشدن‌ویکناری
رفتن هم عست یمتی از راء دورشو - ونام کیاهی
است کهآ نرا میکویشد وشافپا میسازند واز جانب
ارمن می‌آورند و آنرا پوش دربندی میخوانند .
نقری را نافم است » و شیاف خوزی همان‌است.
و‌شا؟ - با ات بالفکشیده. پوشنده
وپوشند کی را گونند؟ .*
بو شث با ثانی‌مجهول بررزن‌حوشك»
بزبان ماوراء النه رگربه را گویند و بعربی سنود
خوانند؟ .
بو شگان - با انی مجهول ر فتح الث
وک‌اف فارسی بر وزن م وکشان. نام نوایست‌از
موسیقی - و بمعنی مغیبات‌هم‌هست بعنی‌چیهابی
که درعالم غیبت‌اند- وبسکون ثالث بروزن‌دوستان
نام جایی و مقامی است نردبك‌به نیشابورومقامی
۱ "۳ رژ۵: دوست کردن.
5 ود: بوشنج ۰ 3 له: بوشث.
۵ - کلکی 0۲ .
اسشق ۳۳۹
8۷ سم
است از مقامات سالك که آنرا بعربی غیب‌الفیب
مفدس تجلی لماید وفانی درحق ومافی در وگردد.
بو شنگ سب با ثانی مجپول بر وزن
هوشنگه , نام قربه‌ایست مابین فثدهار و مولتان
وه‌مرب‌آن فوشنج بود6 - و بسکون ثالت وفتح
نون بمعنی پوشك است که گربه باشد ٩‏ .
لو شنه» بنن اول و سکون نانی و فتح
الث و نون ۰ بمعنی سرپوش باشد - وهرچیزی
پو شه ۲ - بر وزن خوشه ؛ بمعنیمطلق
آویزند .
لكش - بنم اول وسکون ثانی و کاف 4
نز گونند که درجابی بنهان کنند وخاله برب
===== leaf 216/217 head
" ]یست - بنتح ثاك و سکون رابم
و فوقالی . کرشت ترنج را گویند , و آن را
میه بالشکه نیز خواشد . ممده را ژبان دارد -
و یکر تاك مخفف آبستن باشد ۱ . #
۲ فستان ه بی وزن تاستان » بسنی
آبتن بود یمنی هر حیوالی که بچه در شکم
داشته‌باشد ۱ - و بمعنی پنهان‌داشتن هم گفته اند.
] بسقی - بر وزن داستن نهفته و پنهان
را کوبند و هر حیوال ی که بچه در شکم‌داشته
باشد ؟ .
آ بستن قریاك » بکی نون » کنابه
از پربط است ۰ و آن س
---
"آب سیه « یکی اك , مخخف آب
سیاء انت که شراب انگوری - و علت کوری
و غیره باشد . ۸ ۱
[ بشت - بنتح تالك و سکون شین و ای
قرشت » هفته و پنهان را گوبند ٩‏ .
۲ بشتگاه ه خلونشانه - و جای هفتن
و محل پنهان شدن باشد » چه گاه بمعنی جا
و مقامبهم آهده است - و ادیخانه و مستراح را
یی زگویند .
] اشتگه - مخفف آبشتگاه است که
محل نهفتن و ستالخلا باشك  .‏ .
۲ بشتن - بفتح ثاك » بر وزن‌وارستن .
بمعنی نهفته وپوشیده داشتن
```


## [2026-09-14T01:00:35.964Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"pus\\|put\\|pūs\\|pūt\" SNS.txt | grep -i \"rot\\|decay\\|foul\\|faul\" | head -20; echo \"=== direct ===\"; grep -n \"pusit\\|pūsīt\\|pütak\\|putak\\|pūtak\" SNS.txt SNS_pages.txt | head -20",
 "description": "Grep SNS for pusitan"
}
```


### [2026-09-14T01:00:36.039Z] TOOL RESULT

```
=== direct ===
```


## [2026-09-14T01:00:39.632Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nimport re\nfor i,p in enumerate(pages):\n    if re.search(r'p[uūöo][sš]', p) and re.search(r'rot|decay|putrid|faul', p, re.I):\n        print('leaf',i)\nEOF",
 "description": "Search SNS for pus- entries"
}
```


### [2026-09-14T01:00:41.334Z] TOOL RESULT

```
leaves 243
leaf 220
```


## [2026-09-14T01:00:43.867Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[220][:2500])\n\"",
 "description": "Print SNS leaf 220"
}
```


### [2026-09-14T01:00:45.048Z] TOOL RESULT

```
                                              Is *.U*;lj   tf   At i$b*& *=-,**
43

                                  166/10-290/17-325/4       zgnafzar 170/11
yazed 312/16             zaraan
                                                            zlndaglh 171/3
yazem 312/2-12           zaraanlg 166/14-325/8
                                                            zlv3d 170/17
yazend 312/14            zamlg 167/1-326/3
                                                            zlvandag 171/2-4
yazisn 311/11-312/10     zamlgSn 167/8
                                                            zlvSh 171/1
yazisn I arday fravard   zamistSn 325/9
                                                            zlvisnlh 170/21
  311/15                 zan 167/10-288/4
                                                            ziyan 170/7
yazisn I sr&s 311/17     zan3n 167/14-288/18
                                                            ziy3nag 170/10
yazis 1 yazdan 311/20    zand 169/8-10
                                                            zChr 167/15
yazisn kardan 311/14     zandbad 169/12
                                                            z5r 169/4
yOzdahr 334/8            zandbadan 169/14
                                                            zOrmandtar 169/7
y5zdahran 334/12         zandlg 169/15
                                                            z3t 168/13
y&zdahrgar 212/14-334/13 zanSd 241/6-10
                                                            zStlh 168/22
yBzdahrgarlh 334/15      zan x apustan 288/13
                                                            zQzag 168/10
ySzdahrlh 334/17         zan I dastan 288/16
                                                            zufr 168/2
                         zanlh 167/24-288/20
                                                             zufray 168/9
                         zan I zadag 288/15
zad 164/19                zanisn 169/1
zadag 163/2               zan Xv 5stan 111/12-288/11
zadan 164/14              zarcr3 162/11
zad hSnd 164/20           zartust 165/10
 zara-yazad 166/17        zartustan 165/17
 zayfid 165/6             zartustOgtura 166/6
 zayEnd 165/5             zartustrOturo 165/19
 z3yisn 165/1             zartuItrOtuman 166/2
 zayisnlh 165/3           zartuItrOtumlh 166/4
 zad 241/7-9              zaspan 163/7
 zadSrlh 163/4            zSfanC?) 163/8
 zahag 162/1-4-10         zfih 155/8-169/18
```


## [2026-09-14T01:00:50.389Z] TOOL CALL #55: Bash

```json
{
 "command": "timeout 300 python3 tools/ref_page.py SNS:137 --image 2>&1 | head -30",
 "description": "Try ref_page for SNS 137"
}
```


### [2026-09-14T01:00:51.478Z] TOOL RESULT

```
no scan of SNS covers printed page 137 (see 'scans' in refs_online.json)
```


## [2026-09-14T01:00:56.383Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    for m in re.finditer(r'\\bp[uūöo0][sšt]\\w*', p):\n        s=m.group(0)\n        if len(s)>3:\n            print(i, s, '|', p[max(0,m.start()-60):m.start()+80].replace('\\n',' '))\nEOF",
 "description": "Find pus/put forms in SNS"
}
```


### [2026-09-14T01:00:57.570Z] TOOL RESULT

```
70 putrS |           wvu puclo        :   ^7 p U?a-         :       *« putrS-: i- puflra-                     :£-                                      
70 pusaran |  :   ^~»«>i**S>                            •o!r<        :   pusaran: BRHr'n: >*                       ^tftj                                 
70 pusarIh | *                                 wwp            :frazand!h/pusarIh:BRHyh :>» -o^u    •i$j»i'isx>b*                                         
70 puslh |  ^: bhar : L /bar *- * 1_                 :    ^il*J>N :pad puslh padlrSft: y»»>^-»u*I>wo                                                   
84 putay |          909)patay: ^j^/pu/pav                   -     j>   putay-: /-                           •o^o^.o^jl^ :fraz bariin;                  
103 postpone |                                           vw<iito»»   .JUL: postpone, neglect. (<JW) spSzed:                                                
206 putra |                           ma 39/17  dosa- 332/14            putra- 109/12-138/16                                              rofiksika- 238
226 pusarlh | t.L a yy   i$A* $***& c-^j  _ >* pestar 232/22              pusarlh 109/17                    rad 226/2              reraanth 235/13 pes ud 
226 pusih | 6/2              reraanth 235/13 pes ud pas 143/2           pusih 138/19                      radSn 226/4            r€s 234/12 petrSt 142/1
226 pust | adSn 226/4            r€s 234/12 petrSt 142/14              pust 139/5-10                     radlh 226/5            rSsag 234/18 pexak 143/
226 pusarSn | 225/1                  rSdag 233/19           rOzgar 230/13 pusarSn 109/15             r3z 222/4                         reman 235/10       
235 post |          dil 225/6                  drust 339/9 dandSn fris post 339/19     deh/dih 242/10               dist 313/11                drustih
```


## [2026-09-14T01:01:01.849Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[84][:3000])\n\"",
 "description": "Print SNS leaf 84"
}
```


### [2026-09-14T01:01:03.061Z] TOOL RESULT

```
try                                  UjtiMtfUtaUti'j                                                                                        Uc^UtebMU                           »tj




                                                         ^m«S           p.        119

                                                                                                                                               *
                                                                                                                                                                         -t/ts
                                                        .*-*-    :   puxtag :»»*>'*         •




                                TA/T^      (GJVPE.      64) /pac         :   L / 1-          j
                                                                                                                                                       •o-^'J^.jIji :fraz:0"
                                                                                                                             (Aim. 974)fra->^ fra-/fra-:t-
                                                                                       Xwtu
                                 iAiWb.    897)p3sav/paratu                   :        L.             ^^'j.,^^,,,, nQn fraz:                                        ^^
             WIT** -T\/1T^                (J? J >** -^jr** '^'^ J»)          <J<   (0


                                                                                                                  •t/H«*         IWVtfrf.tWWf/lri l., wwr
                                                                                                 I             •••XK'JttjIji          :f r3z raved     .
                                                                                                                                                                ,«iitOo» er«y

                                                                                                                                                   >V'v J       h/i»J -r/f J
                                                                                                     TV,t,f
                                                                                                              '*"*-"*'-Wl«* bur d:                               '„,>« J,l
  MiVfc.          909)patay: ^j^/pu/pav                   -     j>   putay-: /-                           •o^o^.o^jl^ :fraz bariin;
                                                                                                                                                                 ^^^
                                                                                                                                                            ij/irJ .rr/r«s

                                                                     ^:pani:            «»»
```


## [2026-09-14T01:01:09.985Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (101,102,103):\n    print('==== leaf',i); print(pages[i][:2200])\n\"",
 "description": "Print SNS leaves 101-103"
}
```


### [2026-09-14T01:01:11.114Z] TOOL RESULT

```
==== leaf 101
                                                                 .....   L- c__L a,L ^,l                                      Y°
uj tSmJ\A teb *h


                   ^



                                           'TA/VT^          -0-0T 'O* JU:ira h)                   :ZY, m:           .£-&



                                                                             •   ^a ,^o : im      den :       w^ _z»->


                                                                                               •oVi :ziyan:             tt?0«
                         tjzli                      ^jj-- zyanay- fc-
                                   (AiWb. 1701)ojyanay-                           :                                 :




                        l/H^-Tf-r/U^-AT-A1-Ao-V»/T^ Uo twal 187) zy'n:                                .




                                                    V»/1T^                            ^-aAiaj     :   ziyanag: WWJ**               W

                                               .
                                                   J I>1^.. c iL--jljil l>!j               :zen af zar:            *-^«^*£
                                                                                      .*ii» c ^L. 0rfj      :zin:v-J
                       {Arm Gram 151) zen                    :           ^jl AiWb 1650) zaena:
                                                                                           .                            fc-

                       infzar          +(jJ».y^e4j zln: ^.                  (tfir. Man. Ill,              65)zyn:^6
                        Noldeke ZDMG.                32,         408.             ;i&      Aar-^jiB .^lyl                          16

                                           .f/1T*S          -f -*>->W
                                                                                 awa«ar :^                (OVP£.    23_

                                                                              abS^Jij.jl^i :zlvad: *>***>
                          gay      :   >;, (A {fife.         609)           jlva-: ^jois ^Iva-: ^1 fc-
                         )yw:^V         (iter. Man.          II
==== leaf 102
                                          »


                        L^   ^U -b    ')')_




                j"I ;iJ           —           gsh5n:   ^
 c akta
          L,   .o^-^V         *
                                              lMpf# 160 )
                                                            bl?

                        .^./L-sB«t tar: >*~»                                                                                             .f a:           40   :   -O
                .
                                                                      (Jackson. 106) catvarisSt                :   L caflwar^sat-                    sbm


                    ,        M    3
                                      ^o>^=saxtag:J^
                                                                                                                             >*iJC       .*-:            si :A3


                        ^v^-w"-
                             :E av S nd:
                                         SGVTWN, nd =   ^:^                                      1/1Y*£   .*-!?*- :sig3nag:              S3K3**

                                            i37)
                                                       c^i                                                            .*l*-:siy3(h)                  :   -U*->*

                                                                                        U:.syawarsan   s©i-CAiffl>.   1631)syava-                    jfc-
                                                                      .
                                                                          6/ Y^.   iJ




                                                                                                                       .Crf-L   :s3xt: \*>U<J>
                                                                                                          .{GNPE.     152)/sac-                  :       t-
                                                                  I




                                                                  I
                                                                               -TA/T^ .o-ltf*L :saxt 5st5d:       
==== leaf 103
                                                         '       :


                                       tu^tn-L.jlj                                                                                 c-^Lul-^L^U^Ij                                                       \Vt
YA


                                                      .(Kotwai.       P- 169)                                                                  (Jlb.jfi^-,       :sast5r:        1a*»«*xx_w
                   .Y-p-6-T-l/" ** -6/T^
                                             *                                              !.P$           •(/Kk'fc.       1573)sastar-                   :   i^tf-**    sastar-:*5"
                                                                                                                      U/1fl^           (Mir. Man.             Ill, 61)-;s*st*r                      :




                                                         .j-V-       :spas:o"e>JJ            "-JjIj^a^-jVJU^jI^^j.i^^i^Ujj^"                                             .jL   :sar:\<o»
                  (AiJ/fc.    1614) spas i&SiS**             /spas-          :&-


                                                                                                                                                              .JL.aJL :salag: l9J-*<_v

^^.T^V^^^                 ***<* :x v ast ? :                            ,*mvW
 T4j^ffj.A.T
                               v
             w«*m*>o nsjlwO * x astanam :         1                          ^W           (Mir. s'rtjsU (AiWb.                   1567)         saracfa-: L.              [4V0"* •'*&)
                   V splitcorn -
                                  falhhanast                                         \>
                                                                                                                      »Y—) /A <5 .*/?<* -A/Y«£                    #sn.        III.
Corn separated                                                                   :                                                                                                           61).

=x
     v ast:l
             j0T
                     ^t^
```


## [2026-09-14T01:01:18.830Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"بساک\\|پساک\\|بساك\\|پساك\" FRS.txt FRS_pages.txt | head -20",
 "description": "Grep Loghat-e Fors for basak"
}
```


### [2026-09-14T01:01:18.884Z] TOOL RESULT

```
FRS.txt:10322:۱ - ۵ : بسا چون تاجی بود که از ک لکنند » ات پساك تاجی باشد که ازاسیر غم 
FRS.txt:10325:بندند ۰ س ؛ بساك تاجی بود ازاسیرغم که از گلها کنند ۲ - این لفت در هیچ 
FRS.txt:11843:من بساك از ستالك بید کنم... بی تو ام‌وزجفت سبزه منم 
FRS.txt:16508:بساکسا که بره است و فرخشه بر خوانش 
FRS_pages.txt:11184: ‫پساك تاجی باشد که ازاسیرغم‬   ‫‪ : ۵ - ۱‬بسا چون تاجی بود که از کلکنند »ات‬
FRS_pages.txt:11185: ‫‪ - ۲‬این لفت در هیچ‬     ‫بندند ‪ ۰‬س ؛ بساك تاجی بود ازاسیرغم که از گلهاکنند‬
FRS_pages.txt:13009:    ‫بی تو ام‌وزجفت سبزه منم‬               ‫من بساك از ستالك بید کنم‪...‬‬
FRS_pages.txt:18387:                                   ‫بساکسا که بره است و فرخشه بر خوانش‬
FRS_pages.txt:18389:‫و کبساکه جوین نان همی نیابد سیر]‬
```


## [2026-09-14T01:01:22.788Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10310,10335p' FRS.txt; echo \"=== page of FRS_pages line 11184 ===\"; python3 -c \"\nt=open('FRS_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nidx=sum(len(l)+1 for l in lines[:11183])\nprint('leaf', t[:idx].count('\\f')+1)\npages=t.split('\\f')\nn=t[:idx].count('\\f')\nprint(pages[n][:1500])\n\"",
 "description": "Read Loghat-e Fors basak entry"
}
```


### [2026-09-14T01:01:23.807Z] TOOL RESULT

```
یراك" 
نام غلامیست از غلامان [ عنصوی گوید : 
پمستحقان ندهی‌هر آ نچه‌داری و باز دهی (مع‌جرودستارسيزك و سیمالك ] 
ال" 
ابله بود و حرامزاده را نیز گویند [ محیاث گوید : 
آن‌ کت کلو خ روی لقب کرد جرب کرد 
زیرا لقب گران نبود بر دل فغالك ] 
* 
چفز بود » نسخه | دیگر ] خبوك خوانند [ دقیقی * گوید : 
عمجت پلیدو چنودیده‌ها روی ری ی که مر اورا کنی‌خبلت 


۱ - ۵ : بسا چون تاجی بود که از ک لکنند » ات پساك تاجی باشد که ازاسیر غم 


بندند ۰ س ؛ بساك تاجی بود ازاسیرغم که از گلها کنند ۲ - این لفت در هیچ 


فرهنگ وهيچيك ازنسخ دیگر جزدرحاشية بدست یامد وازهء‌ال‌هم که فقط درحاشةً 


هست درست مفه‌وم این کلمه معلوم نشد . احتمال دارد که سيزك نامی بوده اس تکه 
بر کنیز کان مي‌نهاده و سیماك نام دیگری که بفلا‌ان می‌داده‌اند و غرض شاعر این است 
که‌سپزك راباممجروسیماك رابا دستارمی‌بخشی .۰ ۳ - ن . ففاكامق بودوحر امز اده 
رانیز کویند ۰ چ ؛ فناك بنیض [ کذا ] وحر امزده و قلتبان وایله بود ۰ س مثل متن 
4 - ن »۰ يك‌چنز بود بعنی وزغ » چ ۰ بك وزغ باشد » س بك چنز بودوغوك‌نیز 
=== page of FRS_pages line 11184 ===
leaf 274
                                            ‫‪۹۳‬‬

‫و س کسست که‪-‬بری‌نیابدازملکی ]‬                 ‫کهندیم حر دره وبره است‬     ‫یاک‬

                                        ‫‪(۳‬‬
                 ‫‪:‬‬   ‫سیر "غمهاکنند [ کسائی گود‬
                                             ‫چون تاجی بود که از اس‬


      ‫چکوه‌نیکی‌تاج و بساله ملوك باز یکی کوفتة آسیاست ]‬

                                    ‫یراك"‬
                                 ‫نامغلامیست ازغلامان [عنصوی گوید ‪:‬‬
‫پمستحقان ندهی‌هر آ نچه‌داری و باز دهی (مع‌جرودستارسيزك و سیمالك ]‬

                                        ‫ال"‬
                      ‫ابله بود و حرامزاده را نیزگویند [ محیاث گوید ‪:‬‬
                                   ‫کرد‬       ‫لقب کرد جرب‬     ‫کتکلو خ روی‬‫آن‌‬

‫زیرا لقب گران نبود بر دل فغالك ]‬

                                        ‫*‬
             ‫چفز بود » نسخه | دیگر ] خبوك خوانند [ دقیقی * گوید ‪:‬‬

‫اورا کنی‌خبلت‬
            ‫ی که مر‬            ‫ری‬            ‫پلیدوچنودیده‌ها روی‬    ‫عمجت‬


 ‫پساك تاجی باشد که ازاسیرغم‬   ‫‪ : ۵ - ۱‬بسا چون تاجی بود که از کلکنند »ات‬
 ‫‪ - ۲‬این لفت در هیچ‬     ‫بندند ‪ ۰‬س ؛ بساك تاجی بود ازاسیرغم که از گلهاکنند‬
 ‫بدست یامد وازهء‌ال‌هم که فقط درحاشةً‬        ‫فرهنگ وهيچيك ازنسخ دیگر جزدرحاشية‬
  ‫که‬
   ‫اس‬‫هست درست مفه‌وم اینکلمهمعلوم نشد ‪ .‬احتمال دارد که سيزك نامی بوده ت‬
  ‫انست‬
     ‫برکنیز کان مي‌نهاده و سیماك نام دیگری کهبفلا‌ان می‌داده‌اند و غرض شاعر ای‬
‫که‌سپزك راباممجروسیماك رابا دستارمی‌بخشی ‪ - ۳ ۰.‬ن ‪ .‬ففاكامق بودوحر امزا
```


## [2026-09-14T01:01:36.253Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -m3 \"^pustule\\|pustule, n\\|pus, n\\|^pus \" KLN_1966.txt | head; echo \"---grep context---\"; grep -n \"pustula\" KLN_1966.txt | head -5; echo \"--- foul/filth ---\"; grep -n \"OE\\. ful\\|fūl,\\|filth, n\\|foul, adj\" KLN_1966.txt | head -5",
 "description": "Grep Klein for pus, pustule, foul"
}
```


### [2026-09-14T01:01:36.346Z] TOOL RESULT

```
29564:pustule’,  is  of  imitative  origin.  The  second  ele¬ ment  in  7ro|ztp6Xu^  is  possibly  rel.  to  the  second element  in  oivocpXu|,  ‘given  to  drinking,  drunk¬ en’,  and  to  (pXtkiv,  ‘to  boil  over,  bubble’,  (pXctv, ‘to  abound’,  and  cogn.  with  L.  fluere,  ‘to  flow’. See  fluent  and  cp.  flimflam.
---grep context---
13001:in’,  fr.  ev  (see  2nd  en-),  and  ipoaav,  ‘to  blow’, fr.  9 -3 '■to.,  ‘wind,  blast,  bladder’,  from  the.  I.-E. imitative  base  *pu-,  *phu-,  ‘to  blow,  swell’ whence  also  L.  pustula,  ‘blister,  pimple,  pustule’. See  pustule  and  cp.  Physalia,  Physeter.  For  the ending  see  suff.  -ma.
18889:impetigo,  n.,  a  pustular  disease  of  the  skin  ( med .) —  L.  impetigo,  ‘eruption  of  the  skin’,  from  im-
28684:wind,  bubble’,  from  the  imitative  base  *pu-, *phu-,  ‘to  blow,  swell’,  whence  also  L.  pustula, ‘blister,  pimple,  pustule’.  See  pustule  and  -ia  and cp.  the  next  two  words.  Cp.  also  emphysema. Physalis,  n.,  a  genus  of  plants,  the  ground-cherry (bot.)  —  ModL.,  fr.  Gk.  9U3aX (X)i;,  ‘bladder; a  plant  with  a  bladderlike  calyx’.  See  prec. word.
30122:Derivative:  prepotent-ly,  adv. prepuce,  n.,  the  foreskin.  —  ME.,  fr.  OF.  (=  F.) prepuce,  fr.  L.  praeputium,  ‘foreskin,  prepuce’, fr.  prae  (see  pre-)  and  *putos,  ‘penis’,  which  is perh.  cogn.  with  White  Russian  potka,  Czech pyj,  ‘penis’,  and  with  Lith.  puciit,  pusti,  ‘to  blow, swell',  Lett,  piislis,  ‘bladder’,  L .  pustula,  ‘blister, pimple,  pustule’.  See  pustule.
31111:pustulant,  adj.,  producing  pustules.  —  Late  L. pustulous,  gen.  -antis,  pres.  part,  of  pustulare. See  next  word  and  -ant.
--- foul/filth ---
15273:foulness,  n.  —  ME.  foulnesse,  fr.  OE.  fulness ,  fr. fid,  ‘foul’.  See  foul,  adj.,  and  -ness, foumart,  n.,  polecat.  —  ME.  fulmart,  fulmard. fr.  OE.  ful,  ‘foul’,  and  meard,  ‘marten’.  See  foul, adj.,  and  marten.  E.  foumart  was  influenced  in form  by  F.  marte,  ‘marten’, found,  tr.  and  intr.  v.,  to  establish.  —  ME.  foun¬ der!,  fr.  OF.  funder,  fonder  (F.  fonder),  ‘to  found’, fr.  L.  fundare,  ‘to  found’,  lit.  ‘to  lay  the  bottom of’,  fr.  fundus,  ‘bottom’.  See  fund  and  cp.  fond, ‘foundation’.
```


## [2026-09-14T01:01:41.248Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '31111,31125p' KLN_1966.txt; echo \"=== pus ===\"; grep -n \"pus,  n\" KLN_1966.txt | head -3; echo \"=== foul adj ===\"; grep -n \"foul,  adj\" KLN_1966.txt | head -3; echo \"=== fuzzy ===\"; grep -n \"fuzzy\" KLN_1966.txt | head -3",
 "description": "Read Klein pustule and find pus/foul/fuzzy"
}
```


### [2026-09-14T01:01:41.350Z] TOOL RESULT

```
pustulant,  adj.,  producing  pustules.  —  Late  L. pustulous,  gen.  -antis,  pres.  part,  of  pustulare. See  next  word  and  -ant.
pustulate,  tr.  v.,  to  form  into  pustules;  intr.  v., to  form  pustules.  —  Late  L.  pustulatus,  pp.  of pustulare,  ‘to  blister,  cause  blisters’,  fr.  L.  pus- tula.  See  pustule  and  verbal  suff.  -ate. pustulate,  adj.,  covered  with  pustules.  —  Late  L. pustulatus.  See  pustulate,  v.
pustulation,  n.  —  Late  L.  pustuldtid,  gen.  -onis,  ‘a breaking  out  into  pustules’,  fr.  pustulatus,  pp.  of pustulare.  See  pustulate,  v.,  and  -ion. pustule,  n.  —  ME.,  fr.  L pustula,  ‘blister,  pimple, pustule",  from  the  I.-E.  imitative  base  *pu-, *phu-,  ‘to  blow,  swell’,  whence  also  OI.  pupphu- sah,  ‘lung’,  phut-karod,  ‘blows,  shouts’,  Gk. tpuaa,  'pair  of  bellows;  breath,  blast,  wind, bubble',  (pucrav,  ‘to  blow’,  Lith.  puciit,  piisti,  ‘to blow,  swell’,  Lith.  piisle,  Lett,  piislis,  ‘bladder’, Lett,  pusma,  ‘breath’,  OSlav.  puchati,  ‘to  blow’, ON .fjuk,  ‘snowstorm’.  Cp,  Physalia,  Physeter, emphysema.  Cp.  also  prepuce.  For  the  ending see  suff.  -ule.
Derivative  :  pustul-ar,  adj.
put,  tr.  and  intr.  v.  — -  ME.  puten,  putten,  fr.  OE. putian,  a  collateral  form  of  potion,  ‘to  push, throw’,  rel.  to  MDu.  pote,  ‘scion,  plant’,  Du. poten,  ‘to  plant’,  Dan  putte,  ‘to  put’,  Icel.  pota, ‘to  poke’.  The  original  sense  of  all  these  words was  ‘to  push,  thrust’.  Cp.  potter,  ‘to  dawdle’. Cp.  also  putt.
Derivatives:  put,  n.,  putt-er,  n.,  putt-ing,  verbal n.
putamen,  n.,  the  hard  stone  of  certain  soft-fleshed fruits,  such  as  peach,  plum,  cherry  (bot.)  —  L. putamen,  gen.  -inis,  ‘that  which  falls  off  in  trim¬ ming  or  pruning,  clippings,  waste;  shell,  peel’, fr.  putare,  ‘to  trim,  prune,  lop,  clean,  cleanse’. See  putative.  For  the  ending  see  suff.  -men. putaminous,  adj.  —  Formed  with  suff.  -ous  fr.  L. putamen,  gen.  -inis.  See  prec.  word, putanism,  n.,  harlotry,  prostitution.  —  F.  puta- nisme,  fr.  putairt,  ‘harlot’,  fr.  OF.  pule,  prop, fern,  of  the  adj.  put,  ‘dirty,  bad’,  orig.  Totten, foul’,  fr.  L.  putidus,  fr.  putere,  ‘to  stink’.  Cp. OProven?.  put,  ‘bad’,  and  puta,  putan,  ‘harlot’, and  see  pus  and  -ism.  Cp.  also  putois.
putative,  adj.,  presumed;  reputed.  —  ME.,  fr. Late  L.  putativus,  fr.  L.  putatus,  pp.  of  putare, ‘to  trim,  prune,  lop,  clean,  cleanse;  to  think over,  consider,  reckon,  count’,  which  is  prob. rel.  to  puteus,  ‘well,  pit’  (lit.  ‘a  hole  cut'),  and  to pavire,  ‘to  beat,  ram,  tread  down’.  Cp.  compute, count,  ‘to  reckon’,  deputy,  dispute,  impute,  re¬ pute.  Cp.  also  pit,  putamen,  puteal,  amputate. Cp.  also  pave.  Cp.  also  pure.  For  the  ending  of putative  see  suff.  -ive.  For  the  sense  develop¬ ment  of  L.  putare  cp.  L.  caedere,  ‘to  cut,  lop, cut  down’,  whence  decidere,  ‘to  cut  off;  to decide’.
Derivative:  putative-ly,  adv. puteal,  n.,  a  curb  round  the  mouth  of  a  well (archil.)  —  L.,  fr.  puteus,  ‘a  well’.  See  prec.  word and  adj.  suff.  -al  and  cp.  pit.  Cp.  also  pozzolana. putid,  adj.,  rotten.  —  L.  putidus,  fr.  putere,  ‘to stink,  be  rotten’.  See  pus.
Derivatives:  putoid-ly,  adv.,  putid-ness,  n. putlog,  n.,  a  horizontal  piece  of  timber  in scaffolding.  —  Prob.  compounded  of  the  verb put  and  log,  ‘a  heavy  piece  of  wood’.
Derivative:  putlog,  tr.  v.
putois,  n.,  a  brush  used  in  decorating  pottery.  — F,  putois,  ‘polecat’,  fr.  OF.  put,  ‘stinking,  rot¬ ten’,  fr.  L.  putere  (see  putanism);  so  called because  orig.  made  of  polecat’s  hair.
Putorius,  n.,  a  subgenus  of  mammals  of  the  mus¬ teline  family  including  the  polecats  (zool.)  — ModL.,  fr.  L.  piitor,  ‘a  foul  smell,  stench’,  from the  stem  of  putere,  ‘to  stink’.  See  pus  and  cp. putois,  putanism.
putrefacient,  adj.,  putrefactive.  —  L.  putrefaciens, gen.  -ends,  pres.  part,  of  putrefacere.  See  putre¬ factive  and  -ent.
putrefaction,  n.  —  ME.  putrefaccion,  fr.  L.  putre- factid,  gen.  -onis,  fr.  putrefactus,  pp.  of  putre¬ facere.  See  next  word  and  -ion. putrefactive,  adj.,  putrefying.  —  MF.  (=  ,F.) putrefactif  (fern,  putrefactive),  fr.  L.  putrefactus, pp.  of  putrefacere,  ‘to  make  rotten’,  which  is compounded  of  putrere,  'to  be  rotten’,  and facere,  ‘to  make,  do’.  See  putrid,  fact  and  -ive. putrefy,  tr.  v.,  to  make  rotten;  intr.  v.,  to  become rotten.  —  ME.  putrefien,  fr.  MF.  (=  F.)  putre- fier,  fr.  L.  putrefacere.  See  prec.  word  and  -fy. Derivative:  putrefi-er,  n.
=== pus ===
3101:Aplopappus,  n.,  a  genus  of  plants  (bot.)  —  ModL., fr.  Gk.  <xttX6o<;,  aTrXou?,  ‘simple’,  and  mimros, ‘pappus’.  See  haplo-  and  pappus.
4173:Axonopus,  n.,  a  genus  of  plants  of  the  family Poaceae  ( bot .)  —  ModL.,  compounded  of  Gk.
6309:campus,  n.,  college  grounds.  - —  L.,  ‘field’.  See camp,  n.
=== foul adj ===
15268:foughten,  old  pp.  of  fight.  —  ME.  foughten,  fr. OE.  fohten,  pp.  of  feohtan,  ‘to  fight’.  See  fight,  v. foujdar,  n.,  an  officer;  a  criminal  judge  (India).  — Hind,  fawjddr,  fr.  Pers.  fawjddr,  a  hybrid  lit. meaning  ‘a  holder  of  military  force’,  coined  fr. Arab,  fauj,  ‘band,  troop,  military  force’,  and  the Pers.  suff.  -dar,  ‘holder,  possessor’.  See  aumildar and  cp.  words  there  referred  to. foujdary,  also  foujdarry,  n.,  a  criminal  court.  — Hind,  fawjddri,  fr.  fawjddr.  See  prec.  word, foul,  adj.  —  ME.  foul,  fr.  OE.  fid,  rel.  to  OS., OFris.,  MLG.,  OHG.,  MHG.  fid,  ON.  full, Dan.,  Swed.,  Norw.  ful,  MDu.  vuul,  Du.  vuil, G.  faul,  Goth,  fids',  formed  with  suff.  -la  fr. Teut.  base  *fi-  (whence  also  ON.  fuinn,  ‘foul, rotten’),  corresponding  to  I.-E.  base  *pu-, whence  OI.  pByati,  ‘rots,  stinks’,  pBtih,  ‘foul, rotten’,  Arm.  hu,  ‘purulent  blood’,  Gk.  rcu6<;, ‘first  milk  after  the  birth’,  ttjov  or  ttuov,  ‘dis¬ charge  from  a  sore;  matter’,  ttuOciv,  ‘to  cause to  rot’,  L.  pus,  ‘matter’,  putere,  ‘to  stink’,  puter, putridus,  ‘foul,  rotten’,  Lith.  pdviu,  pBti,  ‘to  rot’, pBliai,  ‘matter’,  Mir.  othrach,  ‘dung’.  Cp.  filth, defile,  ‘to  pollute’,  foumart.  Cp.  also  empyema, purulent,  pus,  pustule,  putanism,  putois,  Pu- torius,  putrid,  pyaemia,  pyo-,  Pythium,  sup¬ purate.
15269:Derivatives:  foul,  adv.  and  n„  foul,  v.  (q.v.), foully  (q.v.),  foulness  (q.v.). foul,  intr.  and  tr.  v.  —  OE.  fulian,  ‘to  become foul,  to  rot’,  fr.  ful.  See  foul,  adj. foulard,  n.,  1)  a  thin  textile  of  silk;  2)  a  hand¬ kerchief  made  of  this  material.  —  F.,  prob. formed,  with  change  of  suff.,  fr.  OProven?. foulat,  ‘fulled’,  fr.  VL.  *fuilare,  ‘to  full’.  See  full, ‘to  thicken  (cloth)’.
15272:foully,  adv.  —  ME.,  fr.  OE.  fiilllce,  ‘in  a  foul manner’.  See  foul,  adj,,  and  adv.  suff.  -ly. foulmouthed,  adj.,  speaking  foully  or  obscenely.  — Formed  fr.  foul,  ‘filthy’,  and  pp.  of  mouth,  v. (see  mouth);  first  used  by  Shakespeare. Derivatives:  foulmouthed-ly,  adv.,  foulmouthed- ness,  n.
=== fuzzy ===
15620:fuzz,  n.,  light  particles  or  fibers.  —  Prob.  back formation  fr.  fuzzy.
15621:fuzzy,  adj.,  covered  with  fuzz;  fluffy.  —  LG.  i
```


## [2026-09-14T01:01:50.928Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15620,15624p' KLN_1966.txt; echo \"=== filth ===\"; grep -n \"filth,  n\" KLN_1966.txt | head -2; echo; grep -n \"pus,  n\\.\\|pus, n\\.\" KLN_1966.txt | head; grep -n \"purulent\" KLN_1966.txt | head -3",
 "description": "Klein fuzzy, filth, pus"
}
```


### [2026-09-14T01:01:51.082Z] TOOL RESULT

```
fuzz,  n.,  light  particles  or  fibers.  —  Prob.  back formation  fr.  fuzzy.
fuzzy,  adj.,  covered  with  fuzz;  fluffy.  —  LG.  i
fussig,  ‘weak,  loose,  spongy’;  rel,  to  Du.  vooj,
‘spongy’.
Derivatives:  fuzzi-ly,  adv.,fuzzi-ness,  n.
=== filth ===
14736:Derivatives:  filler-able,  adj.,  filter-abil-ity,  n., filter-able-ness,  n.,  filter-er,  n.,  filter-ing,  n. filth,  n.  —  ME.  filthe,  fulthe,  fr.  OE.  fyld,  rel.  to OHG.  fulida.  ‘filth’.  See  foul  and  subst.  suff.  -th. Derivatives:  filth-y,  adj.,  filth-i-ly,  adv.,  filth-i- ness,  n.

3101:Aplopappus,  n.,  a  genus  of  plants  (bot.)  —  ModL., fr.  Gk.  <xttX6o<;,  aTrXou?,  ‘simple’,  and  mimros, ‘pappus’.  See  haplo-  and  pappus.
4173:Axonopus,  n.,  a  genus  of  plants  of  the  family Poaceae  ( bot .)  —  ModL.,  compounded  of  Gk.
6309:campus,  n.,  college  grounds.  - —  L.,  ‘field’.  See camp,  n.
6609:carpus,  n.,  the  wrist  (anat.)  —  L.,  fr.  Gk.  xotp-oc, ‘wrist’,  which  stands  for  *xrxp7to;  and  lit. means  ‘that  which  turns',  from  I.-E.  base *k'Lerp-,  ‘to  turn,  revolve’,  whence  also  OE. hweorfan,  ‘to  turn  about,  go,  move’,  hwerf,  ‘dam, bank’,  prop,  ‘a  place  for  turning  about’.  See wharf  and  cp.  the  second  element  in  metacarpus.
7699:Cinq  Ports,  a  group  of  towns  (orig.  five)  on  the southeast  coast  of  England.  —  F.,  ‘five  (sea) ports’.  See  cinq(ue)  and  port,  ‘harbor’, cinter,  cintre,  n.,  the  centering  of  an  arch  or bridge.  —  F.  cintre,  ‘curve,  bend’,  fr.  cintrer,  ‘to curve,  bend’,  fr.  VL.  *cincturare,  fr.  L.  cinctura, ‘cincture,  girdle’,  fr.  cinctus,  pp.  of  cingere,  ‘to gird’.  See  cincture  andcp.  words  there  referred  to. cion,  n.,  the  uvula.  —  Gk.  xtcov,  ‘pillar;  uvula’, cogn.  with  Arm.  siun,  ‘pillar’, cipher,  n.  —  ME.  cyphre,  fr.  OF.  cifre,  ‘zero’,  fr. Sp.  cifra,  fr.  Arab,  sifr,  ‘empty;  zero’  (fr.  safara, ‘was  empty’),  which  is  a  loan  translation  of  OI. sunyah,  ‘empty;  cipher  with  no  real  value;  zero’ (F.  chiffre,  ‘cipher’,  derives  fr.  It.  cifra,  of  s.m., fr.  ML.  cifra,  which  is  also  borrowed  fr.  Arab. sifr).  Cp.  MHG.  cifre,  ‘zero’  (whence  G.  Ziffer, ‘cipher’),  which  derives  fr.  OF.  cifre.  Cp.  deci¬ pher.  Cp.  also  zero,  which  is  a  doublet  of  cipher. Derivatives:  cipher,  tr.  and  intr.  v.,  cipher-er,  n. cipolin,  n.,  a  green  Italian  marble.  —  F.,  fr.  It. cipollino,  ‘a  little  onion’,  dimin.  formed  fr.  ci- polla,  ‘onion’,  fr.  L.  caepulla,  dimin.  of  caepa, cepa,  ‘onion’;  so  called  because  the  foliated form  of  this  marble  resembles  the  coats  of  an onion.  See  cibol  and  cp.  chive, cippus,  n.,  post,  inscribed  column  used  as  a  land¬ mark  (Roman  antiq.)  —  L.,  ‘post,  stake,  pillar, gravestone,  boundary  stone,  landmark’,  of  un¬ certain  origin.  It  is  possibly  rel.  to  L.  scipid, ‘staff,  and  cogn.  with  Gk.  crxEmov,  ‘staff, stick’,  ON.  skifa ,  OS.  skiDa,  etc.,  ‘disk,  slice’. See  sheave,  n.
9244:Coronopus,  n.,  a  genus  of  plants  of  the  mustard family  (bot.)  —  ModL.,  fr.  Gk.  xoporvoTtoup,  ‘the hartshorn’,  which  is  compounded  of  xoprovn), ‘crow’,  and  ttoup,  gen.  710861;,  ‘foot’.  The  first element  is  rel.  to  Gk.  xopaf;,  ‘raven’,  and  cogn. with  L.  corvus,  ‘raven’,  cornix,  ‘crow’;  see  cora¬ coid.  For  the  second  element  see  -pod. corozo,n.,  the  name  of  several  S.  American  palms. —  Sp.  (now  spelled  corojo),  from  a  S.  American native  word.
10371:Dasypus,  n.,  a  genus  of  armadillos  (zool.)  — ModL.,  fr.  Gk.  Sacju7rou?,  ‘a  hare’,  lit.  ‘the hairy-footed  animal’,  fr.  dasy-  and  rot)?,  gen. no8o?,  ‘foot’.  See  dasy-  and  -pod. Dasystephana,  n.,  a  genus  of  plants  of  the  gentian family  (bot.)  —  ModL.,  compounded  of  dasy- and  Gk.  axccpavoi;,  ‘crown’.  See  Stephanos, dasyure,  n.,  any  of  small  marsupial  mammals  of Australia.  —  Compounded  of  dasy-  and  Gk. oup£,  ‘tail’.  See  uro-,  ‘tail-’, data,  n.  —  PI.  of  datum  (q.v.) date,  n.,  a  given  point  of  time.  —  ME.,  fr.  OF. (=  F.)  date,  fr.  ML.  data  (scil.  littera)  (whence also  It.,  Proven?.,  Sp.  data),  lit.  ‘(letter)  given’, prop.  fem.  pp.  of  L.  dare,  ‘to  give’.  This  term derived  fr.  L.  datum  (neut.  pp.  of  dare),  the  first word  used  in  letters  to  indicate  the  place  and time  of  writing  as  e.g.  datum  Romae  pridie Kalendas  Maids,  ‘given  (i.e.  written)  at  Rome on  the  last  day  of  April’.  L.  dare  is  rel.  to  dos, ‘marriage  portion,  dowry’,  do-num,  ‘gift’,  dond, donare,  ‘to  give  as  a  present’,  fr.  I.-E.  base  *dd-, *d1-,  ‘to  give’,  whence  also  OI.  da-da-ti,  ‘gives’, Avestic  dadaiti,  of  s.m.,  OI.  da-tar-,  da-tar-, ‘giver’,  da-tram,  ‘gift’,  Gk.  8i-Bco-pi,  ‘I  give’, Sd)-T(0p,  Sco-xrjp,  So-xrjp,  ‘giver’,  8£>-pov,  Sto- t(vt),  8<o;,  ‘gift’,  S6-m;,  ‘a  giving;  gift’,  Bo-xo; (verbal  adj.  of  Si-Sto-ptt),  ‘given’,  OSlav.  dati,  ‘to give’,  da-ru,  ‘gift’,  da-ni,  ‘tax’,  da  mi,  ‘I  shall  give’, Lith.  duomi,  ‘I  give’,  OPruss.  dost,  ‘gives’,  Arm. ta-m,  ‘I  give’,  tu-r,  ‘gift’,  Alb.  Sa-sc,  ‘I  gave’. Cp.  add,  addendum,  anecdote,  antedate,  anti¬ dote,  apodosis,  condone,  dado,  dation,  dative, die,  ‘cube’,  donation  and  words  there  referred to,  dose,  dosimeter,  dosology,  dot,  ‘marriage portion’,  dower,  dowry,  edit,  irredenta,  post¬ date,  reddendum,  reddition,  render,  rendition, sacerdotal,  subdititious,  surrender,  tradition, traitor,  treason.  Cp.  also  mandate,  command, commend,  countermand,  demand.  Cp.  also  the second  element  in  vend.
12812:Elephantopus,  n.,  a  genus  of  plants  (hot.)  — Modi-.,  lit.  ‘the  elephant’s  foot’,  compounded of  Gk,  &i<pac,  gen,  -avro?,  ‘elephant’,  and  roue, ‘foot’.  See  elephant  and  -pod.
13051:Derivative:  encash-ment ,  n. encarpus,  n.,  an  ornament  consisting  of  a  festoon of  fruits,  leaves,  flowers,  etc.  —  ModL.,  fr.  Gk. eyxapTTOi;,  ‘containing  fruit’,  fr.  4v  (see  2nd en-)  and  xapir 6q,  ‘fruit’.  See  carpel, encaustic,  adj.,  burnt  in;  prepared  by  heat.  — Lit.,  ‘burnt  in’;  fr.  Gk.  eyxauaTix6<;,  fr.  sy- xau otoq,  verbal  adj.  of  kyv.ot.Uiw,  ‘to  bum  in’,  fr. ev  (see  2nd  en-)  and  xotUiv,  ‘to  bum’.  See  caustic, encaustic,  n.  —  L.  encaustica,  fr.  Gk.  cyxccuaTixf] (scil.  t iyyt]),  ‘encaustic  art’,  fern,  of  iyx'X'JaTixiii;. See  caustic,  adj.
13314:Eoanthropus,  n.,  a  prehistoric  type  of  man,  the Piltdown  man  ( anthropol .)  —  ModL.,  lit.  ‘man of  the  dawn’,  compounded  of  eo-  and  Gk. 5v9-p<d7t05,  ‘man’.  See  anthropo-.
15268:foughten,  old  pp.  of  fight.  —  ME.  foughten,  fr. OE.  fohten,  pp.  of  feohtan,  ‘to  fight’.  See  fight,  v. foujdar,  n.,  an  officer;  a  criminal  judge  (India).  — Hind,  fawjddr,  fr.  Pers.  fawjddr,  a  hybrid  lit. meaning  ‘a  holder  of  military  force’,  coined  fr. Arab,  fauj,  ‘band,  troop,  military  force’,  and  the Pers.  suff.  -dar,  ‘holder,  possessor’.  See  aumildar and  cp.  words  there  referred  to. foujdary,  also  foujdarry,  n.,  a  criminal  court.  — Hind,  fawjddri,  fr.  fawjddr.  See  prec.  word, foul,  adj.  —  ME.  foul,  fr.  OE.  fid,  rel.  to  OS., OFris.,  MLG.,  OHG.,  MHG.  fid,  ON.  full, Dan.,  Swed.,  Norw.  ful,  MDu.  vuul,  Du.  vuil, G.  faul,  Goth,  fids',  formed  with  suff.  -la  fr. Teut.  base  *fi-  (whence  also  ON.  fuinn,  ‘foul, rotten’),  corresponding  to  I.-E.  base  *pu-, whence  OI.  pByati,  ‘rots,  stinks’,  pBtih,  ‘foul, rotten’,  Arm.  hu,  ‘purulent  blood’,  Gk.  rcu6<;, ‘first  milk  after  the  birth’,  ttjov  or  ttuov,  ‘dis¬ charge  from  a  sore;  matter’,  ttuOciv,  ‘to  cause to  rot’,  L.  pus,  ‘matter’,  putere,  ‘to  stink’,  puter, putridus,  ‘foul,  rotten’,  Lith.  pdviu,  pBti,  ‘to  rot’, pBliai,  ‘matter’,  Mir.  othrach,  ‘dung’.  Cp.  filth, defile,  ‘to  pollute’,  foumart.  Cp.  also  empyema, purulent,  pus,  pustule,  putanism,  putois,  Pu- torius,  putrid,  pyaemia,  pyo-,  Pythium,  sup¬ purate.
31091:purulent,  adj.,  consisting  of,  or  resembling,  pus.
31092:—  L.  purulentus,  ‘festering,  mattery’,  fr.  pus, gen.  puris,  ‘matter,  pus’.  See  pus  and  -ulent. Derivative;  purulent-ly,  adv.
```


## [2026-09-14T01:01:57.789Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=31090 && NR<=31110' KLN_1966.txt | grep -o \"pus,  n[^|]\\{0,600\\}\" | head -2; echo \"---\"; sed -n '31093,31099p' KLN_1966.txt",
 "description": "Klein pus entry"
}
```


### [2026-09-14T01:01:58.864Z] TOOL RESULT

```
pus,  n.,  yellowish  matter  produced  by  an  infec¬ tion.  —  L.  pus,  ‘viscous  matter,  pus’,  rel.  to putere,  ‘to  stink,  be  rotten’,  puter,  putridus, ‘foul,  rotten’,  fr.  I.-E.  base  *pu-,  ‘to  rot,  stink’, whence  also  OI.  puyati,  ‘rots,  stinks’,  putih, ‘stinking,  foul’,  Gk.  miov,  miov,  ‘discharge  from a  sore;  matter’,  Tcuffeiv,  ‘to  cause  to  rot’,  Goth. fills,  OE ./«/,  ‘foul’.  See  foul,  adj.,  and  cp.  words there  referred  to.
---
purusha,  n.,  the  original  man,  the  soul  of  universe (Hinduism)  —  OI.  purusab,  ‘man’,  of  uncertain origin.
purvey,  tr.  v.,  to  supply  (food  or  provisions); intr.  v.,  to  make  provision,  prepare.  —  ME. porveien,  purveien,  fr.  AF.  porveire,  purveire,  fr. OF.  porveeir,  porveoir  (F.  pourvoir),  ‘to  provide’, fr.  L.  providere.  See  provide.  For  the  pref.  see pur-.
purveyance,  n.  —  ME .  porveance,  purveiaunce,  fr. OF.  porveance,  purveance,  fr.  porveeir,  porveoir. See  prec.  word  and  -ance. purveyor,  n.  —  ME.  purveour,  fr.  OF.  porveor, purveor.  See  purvey  and  agential  suff.  -or. purview,  n.,  1)  the  body  of  an  act  or  bill;  2)  scope, range.  —  AF .purveii,  fr.  OF .porveii  (F .pourvu), ‘provided-,  pp.  of  OF.  porveier  (F.  pourvoir),  ‘to provide’  (see  purvey,  provide).  AF.  purveu  oc¬ curred  esp.  in  the  legal  phrases  purveu  est,  ‘it  is provided’,  and  purveu  que,  ‘provided  that’, whence  the  substantial  use  of  E.  purview  in  the sense  of  ‘proviso,  provision’, purwannah,  n.,  an  order;  a  royal  letter  or  grant (Anglo-Indian).  —  Hind,  parwdnah,  fr.  Pers. parwanah,  ‘order’.
pus,  n.,  yellowish  matter  produced  by  an  infec¬ tion.  —  L.  pus,  ‘viscous  matter,  pus’,  rel.  to putere,  ‘to  stink,  be  rotten’,  puter,  putridus, ‘foul,  rotten’,  fr.  I.-E.  base  *pu-,  ‘to  rot,  stink’, whence  also  OI.  puyati,  ‘rots,  stinks’,  putih, ‘stinking,  foul’,  Gk.  miov,  miov,  ‘discharge  from a  sore;  matter’,  Tcuffeiv,  ‘to  cause  to  rot’,  Goth. fills,  OE ./«/,  ‘foul’.  See  foul,  adj.,  and  cp.  words there  referred  to.
Puseyism,  n.,  another  name  for  Oxford  Tractar- ianism,  mostly  used  contemptuously.  —  Named after  one  of  the  leaders,  E.  Bouverie  Pusey (1800-82).  For  the  ending  see  suff.  -ism. Puseyite,  n.,  a  Tractarian.  —  See  prec.  word  and subst.  suff.  -ite.
push,  tr.  and  intr.  v.  —  ME.  posshen,  pusshen,  fr. OF.  polser,  poulser  (F.  pousser),  earlier  poulser, fr.  L.  pulsare,  ‘to  push,  beat,  strike’,  freq.  of pellere  (pp.  pulsus),  ‘to  beat,  strike,  knock, push,  drive’.  See  pulse,  ‘throb’  and  cp.  words there  referred  to.  Cp.  also  pousse-cafe,  poussette, repousse.
Derivatives:  push,  a., push-able,  adj., push-er,  n., push-ful,  adj.,  push-ful-ly,  ad \.,  push-ful-ness,  n., push-ing,  adj.  and  n.,  push-ing-ly,  adv.,  push- ing-ness,  n.
```


## [2026-09-14T01:02:06.751Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB pusidan/puk ===\"; grep -n \"pūsīden\\|pusiden\\|pûsîden\\|pūk\\|pûk\\|puk \" HUB.txt | head -10; echo \"=== CHEUNG pau ===\"; grep -n \"pauH\\|\\*pau\\b\\|pūs-\\|to rot\" CHEUNG.txt | head -20",
 "description": "Grep Hübschmann and Cheung"
}
```


### [2026-09-14T01:02:06.831Z] TOOL RESULT

```
=== HUB pusidan/puk ===
1469:339. Der Etymologie wegen ist np. puk nicht zu verdach-
1470:tigen. Vgl. afgh. pu, puk a puflf, a blast, the act of
6261:Zar. 65 (afgh. spuk light*).
8761:phi. sapuk Phi. Min. 63, Z. 15, Yatk. i. Zar. 65; tanuk
=== CHEUNG pau ===
6694:then be the result of contamination with the semantically close root *pauH, cf. Av. 
7628:*NWIR: Kurd. ganin/gan- ‘to rot’, NP gand ‘stench’, NP gandah ‘fetid, stinking, 
18071:*pari-) prm’w- ‘to terrify’. © On ‘sp’w- (caus.-iter. ?) ‘to terrify, affright’ see *pau. 
19806:*pau 301 
19841:*pau ‘to be afraid ?’ 
19901:*pauH ‘to stink, smell, rot’ 
19914:*SOGDIAN: MSogd. pws (inch.) ‘to rot’ {hapax} 
19918:*CHORESMIAN: pwn- ‘to rot, stink’ = Samadi: 164 
19921:(inch.) ‘to rot’, Kurd. (Kurm.) püc ‘rotten; useless’ || (+ *ham-) NP anbusidan/ 
19922:anbus- ‘to rot’ 
19925:Yghn. pus- ‘to rot’, Ishk. puduk, Pash. puda, Wa. pitk ‘rotten, foul’, Sh. pow, Rosh. 
19932:azmbujun/zembud ‘to rot’ 
19936:«PIE *p(e)uH- ‘to rot, decay, stink’ — LIV: 480 f. | Pok.: 848 f. 
19939:feyja ‘to let it rot’, (ppp.) füinn ‘rotten’, Lith. püti ‘to rot, decay, decompose’ 
29301:dein Haus verfallen !’) || (+ *a-) ? Bal. ašešt/ašeš- ‘to rot’ ("Et. unknown.", 
55622:*baiH, *pau, *ram (s.v.), 
56587:*baiH, *pau, *ram (s.v.), 
57584:to rot 
57653:*frait/9, *pauH 
57931:*baud’, *eant, *eraH, *pauH
```


## [2026-09-14T01:02:10.346Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '19901,19945p' CHEUNG.txt; echo \"=== HUB 339 context ===\"; sed -n '1460,1480p' HUB.txt",
 "description": "Read Cheung *pauH and Hübschmann 339"
}
```


### [2026-09-14T01:02:10.418Z] TOOL RESULT

```
*pauH ‘to stink, smell, rot’ 

*AVESTAN: Y Av. pu- ‘to stink, smell, rot’ = Liste: 35 

Pres. /а-: IND. 3sg. YAv. puiieti® (V 6.28); Partic.: pres. YAv. apuiiant- ‘not stinking, rotting’ (Yt 19.11, 
Yt 19.19, Yt 19.23, Yt 19.89) 

*MIDDLE PERSIAN: BMP pwtk /pudag/ ‘foul, rotten’ 

*PARTHIAN: pwd ‘decay’ > DMMPP: 286a 

*KHOTANESE: (+ *ham-) OKh. hambuta-, hambuva- ‘rotted, festering’ 

*SOGDIAN: MSogd. pws (inch.) ‘to rot’ {hapax} 

Pres.: IND. 3sg. MSogd. pwst 

*CHORESMIAN: pwn- ‘to rot, stink’ = Samadi: 164 

*NWIR: NP püsidan/püs-, Abyan. püsoya/püs-, Gz. püs-/püsa, Khuns. pis-/pisà 
(inch.) ‘to rot’, Kurd. (Kurm.) püc ‘rotten; useless’ || (+ *ham-) NP anbusidan/ 
anbus- ‘to rot’ 

*NEIR: Sh. pi(y)-/pud, Rosh. pay-, Sariq. pey-/püd, Yzgh. piw-/pod, Yi. piy-/pio, 
Yghn. pus- ‘to rot’, Ishk. puduk, Pash. puda, Wa. pitk ‘rotten, foul’, Sh. pow, Rosh. 


*paxš 303 


puw, Bart. paw ‘rotten core of a tree’ || (+ *ham-) Oss. I. ambyjyn/embyd, D. 
azmbujun/zembud ‘to rot’ 

*SANSKRIT: pu ‘to become foul, putrid, to stink’ (YV, Вг+) = EWAia II: 155 

«PIE *p(e)uH- ‘to rot, decay, stink’ — LIV: 480 f. | Pok.: 848 f. 

*IE COGNATES: Gr. т%Өоңно ‘I rot, decay’, Gr. лос (n.), Lat. pus (Ё) ‘pus’, ON 
feyja ‘to let it rot’, (ppp.) füinn ‘rotten’, Lith. püti ‘to rot, decay, decompose’ 
*REFERENCES: IIFL П: 235b, 535b; Abaev, Slovar’ I: 141; EVS: 65a, 116a, 64a; WIM I: 71; WIM П/1: 
81; DKS: 463a; Werba 1997: 444; Steblin-Kamenskij 1999: 263; Lecoq 2002: 127 


*paus ‘to dress, clothe, cover’ 

=== HUB 339 context ===
persisch ?
336. 1st wegen der Bedeutung nicht sicher.
337. Np. puSa *crus sive hominis sive animalis (unbelegt)
kann, wenn aus podak entstanden, zu np. poyidan
laufen' gehoren. Vgl. nhd. Lauf , Lauft in waid-
mannischem Sinne. Zusammenhang niit pai iindet
nicht statt, vgl. Horn's Bemerkungen zu Nr. 282.
338. Zd. pqstO' in pqstdfra&ah- ist noch ganz unklar, aber
die Pehleviiibersetzung giebt es durch post wieder.
339. Der Etymologie wegen ist np. puk nicht zu verdach-
tigen. Vgl. afgh. pu, puk a puflf, a blast, the act of
blowing', pukai a puflf, inflating', pug 'the act of blowing,
a puflf*, pukql *to blow, to inflate, to breathe upon'. -
Lies (fvaaa.
340. Die beste Lesart im Armenischen ist polovat. Dies
sowie np. ptildd setzen ein phi. *pdlavat oder *pOlavat
(anstatt polofat oder polapat) voraus.
*) Vgl. auoh die Name n PanahmOy, Jazdpanah bei Hoffmann^
Ausziige p. 70 und 87. Aus dem von Fr. Muller mit Unrecht heran-
gezogenen phi. panak (= arm. -panak^ pStz. pana Shk. 262) konnte im
Neup. nur ^pana werden.— 44 —
```


## [2026-09-14T01:02:22.739Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"پوک\\|پوسیدن\\|پساک\\|بساک\" ARY_pages.txt | head -20",
 "description": "Grep Aryanpur"
}
```


### [2026-09-14T01:02:22.790Z] TOOL RESULT

```
1236:واژه‌ها در زبانهای مختلف. مثلاً دو واژه‌ی «بْزه فارسی و 81721۳ انگلیسی و یا دو واژه‌ی «پوسیدن»
5268:۸۲ | پوسیدن پوده (به چم
```


## [2026-09-14T01:02:24.743Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"puknos\\|pukinos\\|πυκνός\\|pyknos\" IEC.txt SYN.txt SKT.txt | head -10; echo \"=== pycnometer ===\"; grep -n -i \"pycnometer\\|pyknic\" KLN_1966.txt | head -5",
 "description": "Grep Mann/Buck/Skeat/Klein for pyknos"
}
```


### [2026-09-14T01:02:24.815Z] TOOL RESULT

```
=== pycnometer ===
31141:pycnidium,  n.,  a  spore-bearing  receptacle  occur¬ ring  in  certain  fungi  (bot.)  —  ModL.,  formed  fr. Gk.  ttoxvo q  (see  pycno-)  and  suff.  -idiiun. Derivative:  pycnidi-al,  adj. pycno-,  before  a  vowel  pycn-,  combining  form meaning  ‘close,  thick,  dense’,  as  in  pycnometer.
31142:—  Gk.  7IOXVO-,  Ttoxv-,  fr.  Ttuxvop,  ‘close,  solid, thick,  dense’,  fr.  mixa,  ‘thickly,  solidly’  (whence TtuxdtCsiv,  ‘to  crowd  together,  condense’),  which is  cogn.  with  Avestic  pusa-,  ‘headband’,  Alb. pud,  ‘I  kiss’,  prop.  ‘I  embrace’ ;  not  rel.  to  7:6?, ‘with  the  clenched  fist’.  Cp.  pyknic.
31143:pycnometer,  n.,  an  instrument  for  measuring  the density  of  liquids  or  solids.  —  Compounded  of pycno-  and  Gk.  [zerpov,  ‘measure’.  See  meter, ‘poetical  rhythm’.
31153:pyknic
31155:pyknic,  adj.,  fat,  plump.  —  Formed  with  suff.
```


## [2026-09-14T01:02:29.923Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && sed -n '5255,5285p' ARY_pages.txt; echo \"=== pdf page tag ===\"; awk 'NR<=5268 && /\\[pdf page/{p=$0} END{print p}' ARY_pages.txt",
 "description": "Read Aryanpur pusidan entry"
}
```


### [2026-09-14T01:02:31.051Z] TOOL RESULT

```
ایسلندی کهن (/142/ 5070/04 ضا0): پسگشت‌ها اه بر ادا
۲8 بف71 ی
نورس کهن (۸۵۳82 صا0): 7۸3 2 (11۸1 5 ,375 (لت )۴8‏ اههد
ساکسرنی کهن (542:0۸۷ 010): 58 9 (ناه۴5) هام05
فریزی کهن ((۲۶/514 0ا0): 3 «#0ق) 5
8 ,51121825 6 (۲1126) ,349 لته ۰ علمانوه
لد آلمانی کهن (400وع 810 صل۵): ,7813 4 (8۸1) ,210 ما5 :37
آلمانی سا ۰ بآنآظ8 برهان قاطع + ۴۳۷
انگلیسی کهن (بلولا8۸0 0ا0):
بادداشت,
چم اين واژه در زبان‌های اسلاوی: دستمال» کهنه‌ی بچه.
چم این واژه در زبان‌های ژرمنی: پوست جانور؛ پرستین.
[pdf page 179]
۸۲ | پوسیدن پوده (به چم
اوستایی (47:874۷): ادد ریا آلمانی کهن (/0579/۵ 0 بالاان,
پهلوی (/ا/ل۳۸): ,۶11817۸۷ ,۶107۸86 آلمانی (0880/4۷): ت7۸
6 ,81781۳17۸ انگلیسی کهن (54ا8(/0 صا0): ۴1
اوستی (0558716): 110 انگلیسی (810اا8(/0): 8017
کردی (7ل08215): 78 دانمارکی ([0۸/15): ب707
سانسکریت (54/5877): 8118 ,۴17۸71 سرئدی (81780/5[7): بالا70
ارمنی (۸48(۷1۸0): 3 نروژی (700۳5014(۷): 0
بونانی 07280): هلدی (ل07): ۷
,۳۷۵۸ ,8120۸ ,8108 ,817170 لیترانی (/(1۸هت777/.).
لاتین (۸710ا): 1 ۶۷0 ,زا800۸
58 ,8 ,۶1885 ,۴11780 لتونی (لتی) (701۸(۷ما): ۳15
فرانسه (ع/۳88۸): ۳17۲31۳187۳ ,8107810
اسپانیایی ([5۳4۸//3): ۳1701813 ,8107100 پسگشت‌ها انم ۲
ایتالیابی (17۸۵(۷): ۳0 149 میتی نا
پرتغالی (۳0870010235): 3 (اتام۴) اف را
,8178100 5 (۴88) دق متام
گرتیکد (0077416): 718 9 ,گ11 انا :۱/25
=== pdf page tag ===
[pdf page 179]
```


## [2026-09-14T01:02:39.382Z] TOOL CALL #70: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-14T01:02:39.390Z] TOOL RESULT

```


```


## [2026-09-14T01:02:41.854Z] TOOL CALL #71: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/pus",
 "prompt": "Give the full etymology of \"pus\", and any related entries shown (pustule, purulent), including the PIE root cited."
}
```


## [2026-09-14T01:02:43.197Z] TOOL CALL #72: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D9%88%DA%A9",
 "prompt": "What does the Persian entry پوک say — meaning and etymology? Quote it."
}
```


### [2026-09-14T01:02:46.730Z] TOOL RESULT

```
# پوک (Puk) — Persian Dictionary Entry

Based on the Wiktionary page, the Persian word **پوک** (puk) is defined as follows:

**Meaning:** "hollow"

**Etymology:** The page does not provide an etymology section. The only reference cited is:

> "Steingass, Francis Joseph (1892), A Comprehensive Persian–English dictionary, London: Routledge & K. Paul"

The entry includes pronunciation information across multiple Persian dialects (Classical, Dari, Iranian, Tajik, and Hazaragi) but does not explain the word's origin or historical development.
```


### [2026-09-14T01:02:47.586Z] TOOL RESULT

```
# Etymology of "Pus"

**Main Entry (Pus):**
The word "pus" arrived in English during the late 14th century from Latin *pus*, meaning "pus, matter from a sore." The Latin term also carried figurative meanings of "bitterness, malice" and was related to *puter* ("rotten") and *putere* ("to stink").

**Proto-Indo-European Root:**
The ultimate origin traces to PIE *\*pu-* (2), meaning "to rot, decay." This root may have originated as an echoic representation of disgust reactions.

**Related Language Evidence:**
The root appears across multiple languages, including Sanskrit *puyati* ("rots, stinks"), Greek *pythein* ("to cause to rot"), Lithuanian *pūvu, pūti* ("to rot"), and Gothic *fuls*.

**Medical Definition:**
According to the source, "yellowish-white inflammatory exudation, consisting of white blood cells, etc., produced by suppuration."

**Related Entries Shown:**

- **Purulent:** From Latin *purulentus* ("full of pus"), first documented in the early 15th century as describing pus-colored material.
- **Foul:** Derived from Old English *ful*, connected through the same PIE root *\*pu-*, originally relating to decay and unpleasantness.
```


## [2026-09-14T01:02:51.150Z] TOOL CALL #73: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/pustule",
 "prompt": "Give the full etymology of \"pustule\", including the PIE root cited and cognates."
}
```


## [2026-09-14T01:02:52.580Z] TOOL CALL #74: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pewH-",
 "prompt": "Does this reconstruction page exist? What is the root's meaning and what descendants (Indo-Iranian, Latin, Germanic) are listed?"
}
```


### [2026-09-14T01:02:56.183Z] TOOL RESULT

```
# Etymology of Pustule

**Definition & Timeline:** The word "pustule" meaning "small, inflammatory sore or tumor containing pus" entered English in the late 14c.

**Etymology Path:** It derives from Old French *pustule* (13c.) and directly from Latin *pustula* "blister, pimple."

**PIE Root:** The Latin term traces back to an imitative Proto-Indo-European root *\*pu-* (1), which conveys the sense of "blow, swell," particularly referencing an "inflated area."

**Related Cognates:** The same PIE root produced:
- Sanskrit *pupphusah* "lung"
- Greek *physa* "breath, blast, wind, bubble"
- Lithuanian *pučiu, pūsti* "to blow, swell"
- Old Church Slavonic *puchati* "to blow"

**Related English Words:** The entry notes connections to *emphysema* and mentions related terms including *pustulant*, *pustulate*, and *pustulation*.
```


### [2026-09-14T01:02:57.745Z] TOOL RESULT

```
# Proto-Indo-European Root *pewH-

**Existence:** Yes, this reconstruction page exists on Wiktionary.

**Root Meaning:** The root means "to be clean, pure," as indicated in the definition provided.

**Key Descendants Listed:**

*Indo-Iranian:*
- Sanskrit pávate (thematic present), punā́ti (nasal-infix present), and paváyati (causative)
- Persian pâk ("pure; clean")
- Kurdish pak ("pure")

*Latin:*
- pūrus ("pure"), putus, and putō
- The Latin forms show the semantic connection to purification

*Germanic:*
- Proto-Germanic *fawjaną (from the causative formation *powH-éye-ti), with further descendants in Germanic languages

The page also documents extensive reflexes across Proto-Celtic, Proto-Italic, and various Iranian languages, demonstrating the root's wide distribution across Indo-European language families.
```


## [2026-09-14T01:03:03.482Z] TOOL CALL #75: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D9%88%D8%B3%DB%8C%D8%AF%D9%86",
 "prompt": "Give the Persian entry پوسیدن: meaning and full etymology (Middle Persian, Proto-Iranian, PIE forms and cognates). Quote the etymology."
}
```


## [2026-09-14T01:03:04.538Z] TOOL CALL #76: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D9%88%D8%AF%D9%87",
 "prompt": "Is there a Persian entry پوده? What does it mean and what etymology is given?"
}
```


### [2026-09-14T01:03:08.108Z] TOOL RESULT

```
# Persian Entry: پوده

Yes, there is a Persian entry for **پوده** (pude). 

## Meanings

The adjective has three primary definitions:
1. Rubbed or worn; fallen to pieces
2. Foul or rotten
3. Empty or hollow

## Etymology

The word derives from Middle Persian *pūdag*, meaning "foul, rotten." It shares linguistic kinship with Old Armenian *փուտ* (pʻut), which linguists identify as "an Iranian borrowing."

The entry cites Francis Joseph Steingass's 1892 *Comprehensive Persian–English Dictionary* as a reference source.
```


### [2026-09-14T01:03:08.872Z] TOOL RESULT

```
# Persian Entry: پوسیدن (Pusidan)

## Meaning
The verb پوسیدن has three primary definitions:
1. To rot, decay, or decompose
2. To moulder or putrefy
3. To corrode or rust

## Etymology

The word traces back through ancient language families. According to the source: "From Proto-Iranian *puH- ('to rot'), from Proto-Indo-Iranian *puH-, from Proto-Indo-European *puH- ('rotten, foul')."

**Cognates include:**
- Sanskrit पूयति (pūyati) — "to stink, to become putrid"
- Latin pūs — "pus, foul matter"
- Ancient Greek πῡ́θω (pū́thō) — "to rot, to decay"

The etymological trail demonstrates a consistent semantic field centered on decay and decomposition across Indo-European languages, with the root *puH- appearing as the ancestral form in Proto-Indo-European.
```


## [2026-09-14T01:03:12.817Z] TOOL CALL #77: WebSearch

```json
{
 "query": "Avestan pusā- \"diadem\" Middle Persian pusag crown Sogdian psʾk garland etymology"
}
```


## [2026-09-14T01:03:14.002Z] TOOL CALL #78: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%B3%D8%A7%DA%A9",
 "prompt": "Is there a Persian entry بساک? Meaning and etymology?"
}
```


### [2026-09-14T01:03:18.286Z] TOOL RESULT

```
# بساک (Basāk) - Persian Entry

Yes, there is a Persian entry for **بساک** on Wiktionary.

## Meanings
The word has two primary definitions:
1. A wreath or garland
2. An anther (the part of a flower that produces pollen)

## Etymology
The term derives from Middle Persian *pwsg* (pronounced "pusag" or "pūsag"), meaning "garland." It shares cognates across several ancient languages, including Parthian, Sogdian, Avestan, Sanskrit, Old Armenian, and Tocharian languages—suggesting an Indo-European origin related to braids, plaits, and head ornaments.

## Pronunciation
Depending on dialect, it's pronounced approximately "ba-SAAK," with variations in Dari, Iranian Persian, and Tajik Persian.
```


### [2026-09-14T01:03:21.727Z] TOOL RESULT

```
Web search results for query: "Avestan pusā- "diadem" Middle Persian pusag crown Sogdian psʾk garland etymology"

Links: [{"title":"DIADEM Definition & Meaning - Merriam-Webster","url":"https://www.merriam-webster.com/dictionary/diadem"},{"title":"Diadem - Etymology, Origin & Meaning","url":"https://www.etymonline.com/word/diadem"},{"title":"Hvare-khshaeta","url":"https://en.wikipedia.org/wiki/Hvare-khshaeta"},{"title":"CROWN i. In the Median and Achaemenid periods - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/crown-i/"},{"title":"Aban","url":"https://en.wikipedia.org/wiki/Aban"},{"title":"CROWN ii. From the Seleucids to the Islamic conquest - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/crown-ii/"},{"title":"Diadem - Livius","url":"https://www.livius.org/articles/objects/diadem/"},{"title":"Category:Middle Persian terms derived from Avestan - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Category:Middle_Persian_terms_derived_from_Avestan"},{"title":"graphsearch.epfl.ch","url":"https://graphsearch.epfl.ch/en/concept/63118/concepts"}]

The search results provide general information about diadems and crowns in Persian contexts, but they don't contain the specific etymological information about the Avestan, Middle Persian, and Sogdian terms you're asking about (pusā-, pusag, and psʾk). Let me search more specifically for these linguistic forms.

Links: [{"title":"SOGDIAN LANGUAGE i. Description - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/sogdian-language-01/"},{"title":"SOGDIANA i. The Name - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/sogdiana-name/"},{"title":"Sogdian language - Encyclopedia of Buddhism","url":"https://www.encyclopediaofbuddhism.org/wiki/Sogdian_language"},{"title":"SOGDIAN LANGUAGE ii. Loanwords in Persian - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/sodgian-language-i-loanwords/"},{"title":"Sogdian","url":"http://www.languagesgulper.com/eng/Sogdian.html"},{"title":"Sogdia","url":"https://en.wikipedia.org/wiki/Sogdia"},{"title":"Sogdian language","url":"https://en.wikipedia.org/wiki/Sogdian_language"}]

Links: [{"title":"CROWN i. In the Median and Achaemenid periods - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/crown-i/"},{"title":"Kiani Crown - Wikipedia","url":"https://en.wikipedia.org/wiki/Kiani_Crown"},{"title":"Category:Middle Persian terms by etymology - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Category:Middle_Persian_terms_by_etymology"},{"title":"Middle Persian literature","url":"https://en.wikipedia.org/wiki/Middle_Persian_literature"},{"title":"Sasanian crowns","url":"https://en.wikipedia.org/wiki/Sasanian_crowns"},{"title":"تاج - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%AA%D8%A7%D8%AC"},{"title":"Middle Persian","url":"https://en.wikipedia.org/wiki/Middle_Persian"},{"title":"Persian Online – Grammar & Resources » Middle Persian","url":"https://sites.la.utexas.edu/persian_online_resources/history-of-the-language/middle-persian/"}]

Based on my search results, I found limited information about the specific etymological connection you're asking about. However, I did find one relevant piece of information:

In New Persian, the word "pasāk" (meaning "garland") derives from the Sogdian form "(ʾ)psʾk". This shows that the Sogdian term for garland was borrowed into Persian.

Unfortunately, the search results do not contain specific information about the Avestan form "pusā-" meaning "diadem," the Middle Persian form "pusag" meaning "crown," or the detailed etymological relationship connecting these three forms across Avestan, Middle Persian, and Sogdian. To fully answer your query about this etymology, I would need sources that specifically discuss these linguistic cognates and their historical development, which were not returned in these searches.

If you're researching this topic for academic purposes, you might want to consult specialized etymological dictionaries focused on Iranian languages or linguistic studies specifically addressing Old Iranian word families.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T01:03:27.890Z] TOOL CALL #79: WebFetch

```json
{
 "url": "https://en.wiktionary.org/w/index.php?title=%D8%A8%D8%B3%D8%A7%DA%A9&action=raw",
 "prompt": "Reproduce the full etymology section verbatim, including all cognate forms and any note about Sogdian mediation."
}
```


## [2026-09-14T01:03:28.911Z] TOOL CALL #80: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/sodgian-language-i-loanwords/",
 "prompt": "Does this article list Persian pasāk / basāk \"garland\" as a Sogdian loanword? Quote the relevant passage."
}
```


### [2026-09-14T01:03:30.301Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-14T01:03:32.500Z] TOOL RESULT

```
# Etymology Section

The etymology traces the Persian word to Pahlavi origins: "From {{inh|fa|pal|𐫛𐫇𐫘𐫃|t=garland|ts=pusag, pūsag|sc=Mani}}."

The section lists several cognate forms across related languages:
- Parthian: "{{cog|xpr|𐫛𐫇𐫘𐫃|ts=pusag, pūsag}}"
- Sogdian: "{{cog|sog|tr=ʾpsʾk}}"
- Avestan: "{{cog|ae|𐬞𐬏𐬯𐬀|t=plait, head dress}}"
- Sanskrit: "{{cog|sa|पुट|t=plait}}"
- Old Armenian: "{{cog|xcl|պսակ}}"
- Old Uyghur: "{{cog|xto|tr=psuk}}"
- Tocharian B: "{{cog|txb|tr=pässakw}}"

The documentation demonstrates a widespread Indo-European root shared across Persian, Parthian, Sogdian, Avestan, Sanskrit, Armenian, and Tocharian languages, all connected to concepts of garland, plait, or head dress.
```


## [2026-09-14T01:03:41.632Z] TOOL CALL #81: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E1%BC%84%CE%BC%CF%80%CF%85%CE%BE",
 "prompt": "Give the Ancient Greek entry ἄμπυξ: meaning, declension (genitive), and etymology, including any connection to πυκνός or Avestan pusā."
}
```


## [2026-09-14T01:03:43.281Z] TOOL CALL #82: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CF%80%CF%85%CE%BA%CE%BD%CF%8C%CF%82",
 "prompt": "Give the Ancient Greek entry πυκνός: meaning and etymology (earlier form πυκινός, PIE root, cognates such as Avestan pusā or ἄμπυξ)."
}
```


### [2026-09-14T01:03:48.407Z] TOOL RESULT

```
# ἄμπυξ (ámpux)

## Meaning
The Ancient Greek noun ἄμπυξ refers to three related objects: "a woman's diadem; frontlet," "a horse's headband," or "the rim of a wheel."

## Declension
This is a third-declension noun with genitive form **ἄμπυκος** (ámpukos). It can function as either masculine or feminine gender.

## Etymology
The etymology involves two competing theories. Traditionally, scholars viewed it as "a root noun prefixed with ᾰ̓μ- (ăm-), belonging to πῠ́κᾰ (pŭ́kă, 'solidly') and πῠκνός (pŭknós, 'compact')," with a connection to Avestan **pusā** meaning "headband, diadem."

However, the page notes a significant problem: "the notion 'thick, solid' does not seem to fit the objects in question." Instead, scholars like Beekes propose the word was borrowed and "contains a typical Pre-Greek suffix," suggesting a non-Indo-European origin rather than a connection to the Greek words for density or compactness.
```


### [2026-09-14T01:03:49.360Z] TOOL RESULT

```
# Ancient Greek πυκνός

## Meaning
The adjective πυκνός (pŭknós) has three primary senses:
1. **Thick** (synonym: παχύς)
2. **Dense**
3. **Sagacious; crafty; cunning**

## Etymology
The word possibly derives from Proto-Indo-European *puḱ- meaning "press together." Related cognates include:
- **Avestan** pusā ("headband, diadem")
- **Albanian** putë

An alternative poetic form exists: πῠκῐνός (pŭkĭnós)
```


## [2026-09-14T01:04:06.201Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '31586,31596p' MON_part1.txt; echo \"=== basak full ===\"; sed -n '23303,23312p' MON_part1.txt; echo \"=== NYB pusak ===\"; grep -n -i \"pusak\\|psak\\|crown\\|diadem\\|garland\" NYB_vol2_glossary.txt | head -10",
 "description": "Mo'in pasak entries and Nyberg crown"
}
```


### [2026-09-14T01:04:06.303Z] TOOL RESULT

```
مر دن. 

پساک: »۲:۰2 (.) تاجی که از گل‌ها و 
ریاحین با اسپر عم‌ها ساختندی و بادشاهان و 


۳۵1 


فر هنک فارسی معین 

=== basak full ===
چگونگی جسم مفرد (بسیط). 

بساک: 0 تاجی که از گل‌ها و 
ریاحین و اسپرغم‌ها و برگ مورد می‌ساختند 
و پادشاهان و بزر کان و دلیران روزهای عید 
و جشن و مردمان در روز دامادی بر سر 
می‌گذاشتند. ( گیا.) برجستگی دکمه مانند 
انتهای مبلة پرچم گل که مسحتوی دانه‌های 
گرده می‌باشد. 

=== NYB pusak ===
590:api-sar [pysl] crown 6%. — MPrs ’bysr (S); NP afsar. Probably < Olr *upa-sarah- ‘that which is on the head’ (v. sar) > *apa-sara- and then remodelled to "api- sara- with variable accent: *api-sara- > apisar, *ápi-sara- > *apsar > afsar.
900:bälen [b'lyn'] the crown of the head 728. — Paz. bälin, Skr. v. erroneously utsirsaka ‘pillow’ after NP bälin. < OP
1544:Frašāvart [pls’wlt’] the son of Vištaspa, the crown prince and the co-regent of his father 2216, 2314, 2419, - Av. (1010) Fraš.ham.varota-.
3691:tag [t’k'] crown 5619; han i zrös ~ a cockscomb 56°. — Syr. lw. čaja; Arab. lw. taj and hence again NP ta; cf Arm t‘aga-vor ‘king’.
4011:vaspuhr [w’spwhl] belonging to the class of vispuhr (g.v.), i.e. the lawful heirs within the clan or family: [1. adj.: pus ~~ + šāhān farrax"tom (the son entitled to share the patrimony, foremost among the princes =) the crown prince, the heir to the throne SS 10.] — 2. subst. (royal) heir: ~ % Vistäspän the (foremost) heir of the Vistasp family 26”. 2719, of Frašāvart, the crown prince and co-regent (2217). — < *väispudri-, vrddhi derivative from *eispuÜra- (v. vispuhr), v. Bthl, WZKM 25, 1911, 251-254; in Babylonian cunei- form script 4-ma-su- (var. -as-) pe-it-ru-u = *wäspidri- < *wäspudri-, v. Eilers in Taqizadeh Vol., 1962, 55-63. The mean- ing and juridical purport of this term and its derivatives, as also of the basic w. vispuhr and its derivatives, have been
```


## [2026-09-14T01:04:13.282Z] TOOL CALL #84: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%BE%D8%B3%D8%A7%DA%A9/",
 "prompt": "What does the فرهنگ معین (Mo'in) section say for پساک? Quote the entry including any bracketed origin tag such as [په.] or [پهلوی]. Also quote Dehkhoda if present."
}
```


### [2026-09-14T01:04:18.792Z] TOOL RESULT

```
# پساک - Lexicographic Entries

**Farhang-e Mo'in (فرهنگ معین):**
"(پَ ) (اِ. ) = بساک : تاجی که از انواع گل ها درست می کردند و پادشاهان"

This entry indicates پساک is a variant of بساک, referring to a floral crown worn by royalty and dignitaries during celebrations.

**Dehkhoda (لغت نامه دهخدا):**
"تاجی که از گلها و اسپرغمها و ریاحین ساختندی و پادشاهان و بزرگان بروزهای عید"

The Dehkhoda lexicon similarly defines it as a garland or crown made from flowers and aromatic plants, worn during festive occasions.
```


## [2026-09-14T01:04:27.378Z] TOOL CALL #85: Bash

```json
{
 "command": "for u in \\\n \"https://www.etymonline.com/word/pus\" \\\n \"https://www.etymonline.com/word/pustule\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D9%88%DA%A9\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D9%88%D8%B3%DB%8C%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D9%88%D8%AF%D9%87\" \\\n \"https://en.wiktionary.org/wiki/%D8%A8%D8%B3%D8%A7%DA%A9\" \\\n \"https://en.wiktionary.org/wiki/%E1%BC%84%CE%BC%CF%80%CF%85%CE%BE\" \\\n \"https://en.wiktionary.org/wiki/%CF%80%CF%85%CE%BA%CE%BD%CF%8C%CF%82\" \\\n \"https://abadis.ir/fatofa/%D9%BE%D8%B3%D8%A7%DA%A9/\" ; do\n timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 408 (book 378), roots Pu 2 / Pu 4 Peua / Puk\" 2>&1 | tail -2\ndone",
 "description": "Archive web sources used"
}
```


### [2026-09-14T01:04:32.680Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/2c4608deb7c6d002.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b55c339aa58e3ee3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7d83825993ba89ef.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f81ec56f0692dd66.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c1703d3c3b36f9ed.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9870531e5f235da6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/84c02c2d7c0169c2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cd09a423f082ceb5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/89955fb6ebb17a76.txt
```


## [2026-09-14T01:04:38.751Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd2 pustula/pusa ===\"; grep -n \"pustula\\|pusa-\\|puiti\\|pūtay\" incoming/WLD/WLD_Bd2_pages.txt | head -10; echo \"=== WLD Bd3 index ===\"; grep -n \"pustula\\|pusa\" WLD_band3.txt | head -10",
 "description": "Grep Walde-Pokorny"
}
```


### [2026-09-14T01:04:38.824Z] TOOL RESULT

```
=== WLD Bd2 pustula/pusa ===
5403:vgl.    auch    (fcotdeg      unter 5w-, 5Aw);     lat.   pusstda, pustula    ,,   Blase, Blaschen,
7268:   Red.-stufig oder mit Ass. an den A ok. der 2. Silbe arm. polar ..pustula,
=== WLD Bd3 index ===
```


## [2026-09-14T01:04:41.048Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC ===\"; grep -n \"pustula\\|pūtos\\|puknos\\|pukno\" IEC.txt | head -10; echo \"=== LEW ===\"; grep -n \"pustula\\|pussula\" LEW_1910.txt | head -5; echo \"=== LAT ===\"; grep -n \"pustula\\|pus, puris\\|pūs\" LAT.txt | head -5",
 "description": "Grep Mann, Walde LEW, Ernout-Meillet"
}
```


### [2026-09-14T01:04:41.165Z] TOOL RESULT

```
=== IEC ===
13805:püstos (phüstos), is, à ‘swollen, inflated; puff, swelling, inflation’. Cf. pūt- & extns. Skt. cf. pustakab, am. mn. ‘boss, hump’; Arm. Gut. gs: put'o, o-st. (haste, zeal’, fr. a type *phustio-); Oss. cf. futt kànín, v. ‘to in- flate’; Gk. phustós, adj. "inflated, spongy’; phusté, f. *puff-pastry'; Lat. cf. pustula, f. ‘blister, pustule’; Ir. pus, m. ‘lip’; pl: puis & pusa ‘mouth’ (fr. *phust-); W ws, m. ‘effort’; wst, m. (push; gust’, fr. *pustó-); Li. püstas, adj. ‘blown, puffed’; püst!; pustà, f. *snow- storm’; Latv. püsts, adj. blown — of glass?
=== LEW ===
=== LAT ===
44604:palagra: pustula rupta in cute CG 1 III 604,33. D 4 formation de
51174:pustula, -ae ( pussula; pusula; cf.P.F.88,35) f.: 1° bouton; 3 0 bulle.
51176:D 4 riv 4 s: pustulB,-as; pustulatus et pusulatus; pustulBsus et pusu-
51177:IBsus; pustulesco,-is; pustulatio. Le diminutif pustella, qui est
51179:D'une racine expressive *p(hju- 41 argie par -s- dans pustula et
```


## [2026-09-14T01:04:50.938Z] TOOL CALL #88: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Stirnband\" incoming/WLD/WLD_Bd2_pages.txt | head -5; echo \"=== pu faulen ===\"; grep -n \"faulen, stinken\\|faul, stinkend\" incoming/WLD/WLD_Bd2_pages.txt | head -5",
 "description": "Grep WLD Bd2 for Stirnband and faulen"
}
```


### [2026-09-14T01:04:51.011Z] TOOL RESULT

```
22981:rach „Halfter‘^   (= cymr. pen-rlie „Stirnband''), sciatJi-rach „Schildriemen“;
=== pu faulen ===
5351:wahrscheinlicheres u. apo, pu- und u. pU- „faulen, stinken"); lat. praeputium
5434:„Eiter‘‘, puti-Ji „faul, stinkend; Jauche, Eiter''           =
```


## [2026-09-14T01:04:54.669Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5425,5460p' incoming/WLD/WLD_Bd2_pages.txt; echo \"=== find WLD page tag ===\"; awk 'NR<=5434 && /\\[pdf page/{p=$0} END{print p}' incoming/WLD/WLD_Bd2_pages.txt; awk 'NR<=5403 && /\\[pdf page/{p=$0} END{print p}' incoming/WLD/WLD_Bd2_pages.txt",
 "description": "Read Walde-Pokorny pu- faulen entry"
}
```


### [2026-09-14T01:04:55.879Z] TOOL RESULT

```
      Walde, Etymologisclies Worterbttch.   II.                                           6
 82                                  pu        puq-, peuq-


pu-, pu-, vereinzelt und zweifelhaften Alters       (poii oder pau) „fauleii;
     stinken^; vermutlich aus einem pu 5 ,pfui entwickelt (Falk-Torp u. fuT).
      Ai. puyati „wird faul,  8tinkt‘‘     =
                                       av. puyeiti 5 ,wird fauk^, ai. puya-h^ -m
„Eiter‘‘, puti-Ji „faul, stinkend; Jauche, Eiter''           =
                                                      av. pUtay- „Fauligwerden,
Verwesiiiig“; arm. (Hubschmann Arm.-Gr, I 468) Jiu „eitriges Blut“; gr.
Tivd'ca „inache faulen“, jtv'&opai „faule^‘, nvov (*pu‘^~om)j nvog^ -eog n. ,jEiter*‘;
vielleichtauch (von der eiterahnlichen Dicklichkeit) nvog m., nva^, nvarog^
Ttveila „Biestmilch^‘(wenn nicht nach Persson Beitr. 259a 3 zu *pu-, pus--
„schwellen“, ai. pusyati usw., wie ahd. hiost „Bl®stmilcli“ zur gleichbed.
Wz. b{h)u-^ b^h^u-S”); lat. pUs^ puris „Eiter“, piltea^ -ere j,fanlen“, putidus
„fauk‘, (voneinem Ptc. "^pU-to-s)^ piiter^ ~tris, -tre „faul, morsch“ mit w-,
wie mir. othrach „Mi8thaufen“, wohl auch othar „ein Kranker“, othar-lige
„Krankenbett, Begrabnisplatz'' aisl. fuinn ,,verfault, rott‘‘, ffii „Faulnis'*,
                                       ;


funa „faulen“,              „verfaulen lassen, verrotten lassen“, got. /'w/s,   aisl.

ags.    ahd.   fill      mit g aisl. fitki „Stank‘', nisi, fiiki auch „verfaultes
                      „faul“;
Seegras^ Seetang“, wie lett. pufnis ..faulendes, eiterndes‘', pUfnes pi.
„Modererde“ (Persson Beitr. 465); mit s- aisl. fausJcr ^faules, morsches
Holz“, norw. mdartl. foyr (^fauza-) „morsch“, ndl. voos „schwammig“,
schweiz. gefosen „morschgeworden“ (s. Holthausen Afneuere Spr. 121, 2943
Falk-Torp u, fos II; ersterer stellt hieher auch mhd. ffmi und nd. fdm
aus ^faunta- „Schaum“; vgl. auch u. pen- „Schaum“); vermutlich aisl.
fud „cunnus“, mhd. vut „cunnus'‘, alem. vildeli Kinderwort ,.Popo“ gemi-
niert aisl. fiitta „cunnus“, mhd. votze, und ai, pUiati „IIinterbacken“ (van
Helten ZfdtWtf, 10, 195f., Ficklll^ 242, Falk-Torp u. ful*, nicht wahr-
=== find WLD page tag ===
```


## [2026-09-14T01:05:06.559Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Diadem\\|nvxvog\\|puk-\\|puq-\" incoming/WLD/WLD_Bd2_pages.txt | head -15",
 "description": "Grep WLD for puk root"
}
```


### [2026-09-14T01:05:06.626Z] TOOL RESULT

```
5427: 82                                  pu        puq-, peuq-
5471:puk- „zusammendrangen, eng umschlieBen".
5483:puq-, punq- etwa „dicht behaart, buschig (buschiger Schwanz), dichtwollig‘\
5485:zu vermutlich av. pusa f. „Diadem“ (Zubat}’^ KZ. 31, 13, Bthl. Wb. 91 If.
```


## [2026-09-14T01:05:08.955Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5471,5495p' incoming/WLD/WLD_Bd2_pages.txt",
 "description": "Read WLD puk- entry"
}
```


### [2026-09-14T01:05:09.004Z] TOOL RESULT

```
puk- „zusammendrangen, eng umschlieBen".
   Gr. Tivxvog „fest, dicht, derb, tiichtig, solid‘‘, Zsform stvxi- in jivy.i-
pi^drjg „verstandig“ (Wackernagel Yerm.-Beitr. 10), von wo aus jtvxtvog
„7Tvxv6g^^ (Bechtel Lex. 287); jivxa Adv. „fe8t, dicht^, 7ivy,a cpQoveiv „klug,
verstandig denken‘‘, nvyAI^oa „mache fest oder dicht, drange zs., bedecke
oder umhiille dicht“; alb. pud^ „kusse“ (aus „*umarme, j’embrasse“), ped-
toil „fiige zwei Dinge fest zs.^‘, puMohem „kleide mich eng, schniire mich,

umarme“.        G. Meyer Alb. Wb. 356, Pedersen KZ. 36, 332,          s.   auch Persson
Beitr. 245.


puq-, punq- etwa „dicht behaart, buschig (buschiger Schwanz), dichtwollig‘\
   Ai. piiccha-h, -m. „Schwanz, Schweif, Rute“ (kann                sein), wo-
zu vermutlich av. pusa f. „Diadem“ (Zubat}’^ KZ. 31, 13, Bthl. Wb. 91 If.
zw.; ursprgl. ein pelzbesetzter Turban, ahnlich der Kopfbedeckung eines
Fuchsmajors?); nach dem buschigen Schwanz benannt, scheint auch got.
fauho „Fuchs'‘, aisl. foa,     folia ,,Fuchsin“, ags. fox, ahd. fuhs „Fuchs^'
(vgl. zur Yerteilung nach dem Geschlecht ags.^?oa;, ahd. hihs aus ^luysu-
                                              pumes-    — puro-                                    83

jjLuchs'^:    aschwed. lox         f.   aus   ^lolioyi)   nach Uhlenbeck PBrB. 22, 538 f., Ai.
Wb. 168      f.,   Got. Wb.^ 42, Falk-Torp m, fiihs (vgl.
                                                     lit. Mega „Schwanz'*:
ndegis „Fuchs‘'; eine Gdbed. „Faucher‘^ scheint mir sachlich verfehit, trotz
```


## [2026-09-14T01:05:21.693Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC puk ===\"; grep -n \"^puk\\|puknós\\|puknos\\|pūsā\\|pusā\" IEC.txt | head -10; echo \"=== IEC pūtos/pauyo ===\"; grep -n \"pūtos\\|pauyō\\|'to rot'\\|‘to rot’\" IEC.txt | head -8; echo \"=== SKT foul ===\"; grep -n -m2 \"Foul\\b\" SKT.txt | head -4",
 "description": "Grep Mann and Skeat"
}
```


### [2026-09-14T01:05:21.795Z] TOOL RESULT

```
=== IEC puk ===
13733:pük- (phük-) ‘swell, puff; swelling, puff". Cf. phuk- as a separate entry Skt. pukah, m. (unidentified s.); Alb. cf. pucé, f. (blister, pustule’, fr. *puktio or *pukstio); Ir. cf. úcaim, v “full — wool’ beside (*ph-) puchán, pochán, m. ‘swelling, pustule’; W pwg, m. id.; Li. pūkas, m. ('down', if not a LW fr. R pux, id.); püka, f. ‘blizzard’; pükys, gs: -io, m. ‘bullhead fish, bass’; Latv. püka, f. “flock of wool'; pl: pükas, f. & püki, m. “down, fluff; puke, f. flower’; pūķis, m. dra. gon’; cf. also pukàties and pukoties, v. "be angry’; pücigs, adj. inflated; angry’. (Extn. in Gk. puknós, adj. Compact" preferably to type
13745:puksos, ios “bush, brush'. Cf. pukstios Alb. push, m. ‘down, pile; OHG fuhs, m. (and com. Gmc.) ‘fox’; OE fox, m. id.; fyxe, f. ‘vixen’; Li. pusai, mpl. ‘fur’; pušis, gs: -io, m. 'Scotchfir'; (uncertainly) Gk. püxos, f. (box, bot. LW in Lat. buxus, id. whence Alb. bush, id.)
13747:pukstios, is “bush, brush, sheaf. Cf. puksos. WP II, 82 Skt. púččhah, m. “tail”; Per. cf. pūst ‘skin, fur’; Gk. puktis, f. “an unidentified small furry animal; Li. pukštys, gs: pukščio, m. "wad beside pūkštē, f. ‘bundle’; Latv. pušķis, s. id.
13748:puk- “fit, enclose, hug, embrace, encircle’. WP II, 82 Av. pusa, f. ‘diadem’; Per. puse, id.; Gk. cf. púka, adv. ‘close-fitting’; puknós, pukinós, adj. ‘compact’; cf. ám-pux, gs: -pukos, m & f ‘chap- let, fr. ámbh-^); (late Gk. also ‘tyre’); Alb. puth, v. ‘kiss’; pér-puth, v. “fit close’; MIr. (*phuk-) poc, s. *kiss'; Br. poki, inf. id.
=== IEC pūtos/pauyo ===
=== SKT foul ===
```


## [2026-09-14T01:06:42.575Z] TOOL CALL #93: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSF pude ===\"; grep -n \"پوده\\|چوب پوده\" FSF.txt | head -5; echo \"=== BQT v1 basak ===\"; python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'بساک' in p or 'بساك' in p or 'پساك' in p or 'پساک' in p:\n        print('leaf',i, p[:80].replace('\\n',' '))\nEOF",
 "description": "Check FSF and Borhan for pude/basak"
}
```


### [2026-09-14T01:06:43.842Z] TOOL RESULT

```
=== FSF pude ===
10214:پوده (بر وزن روده) 
10229:تو اندوه این چوب پوده مخور 
=== BQT v1 basak ===
```


## [2026-09-14T01:06:47.197Z] TOOL CALL #94: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10208,10245p' FSF.txt; echo \"=== page tag ===\"; python3 -c \"\nt=open('FSF_pages.txt',encoding='utf-8',errors='replace').read()\ni=t.find('چوب پوده مخور')\nprint(t[max(0,i-1800):i+300])\n\" | head -60",
 "description": "Read Farhang-e Shahnameh pude entry"
}
```


### [2026-09-14T01:06:48.215Z] TOOL RESULT

```
( پرویز ۳۳۳۸) 
پندمند 
پندآمیز (به «مند» نگاه کنید): 
بدو گفت کاین نامه پندمند 
ببر سوی آن دیو جسته ز بند 
(۶۵۱-۱۱۱-۲) 
پوده (بر وزن روده) 


پوسیده کهنه: 


۱۵۱ 


قیصر از خسرو پرویز خواسته است که 
صلیبی را که عیسی را به آن بستند و در گنج 
ایرانست برایش بفرستد. خسروپرویز 
خواهش او را می‌پذیرد و به شوخی پاسخ 
می‌دهد: 
چو پور پدر رفت سوی پدر 
تو اندوه این چوب پوده مخور 
( پرویز (TY.‏ 
همان دار عیسی نیرزد به رنج 
که شاهان نهادند آن را به گنج 
از ایران چو چوبی فرستم به‌روم 
بخندد به ما بر همه مرز و بوم. 
پوزش 
امرزش, خواهش بخشایش گناه و رفتار و 
کردار بد: 
به یزدان کنون سوی پوزش گرای 
که اویست بر نیکوی رهنمای 
(۱۰۳-۱۴۲-۱) 


ز کردار بد پوزش آورد پیش 
بپیچید زان خام کردار خویش 
(۱۱۱۳۰۵) 
=== page tag ===
داوسی‬                       ‫خحنک سیم معنبر شمامة دلخواه‬

 ‫که پندواسی خواندش پارسی‬                         ‫که درهوای تو برخاست بامداد پگاه‬
 ‫(رویز ‪)۸۳۳۳‬‬
           ‫پ‬
                                        ‫پندمند‬              ‫نزگ ‪+‬ین [نسبت] ‪+‬ها‬
                                                                             ‫پکبل ا‬
                                                                                  ‫مر‬
               ‫پندآمیز (به «مند» نگاه کنید)‪:‬‬
               ‫نامه پندمند‬     ‫ین‬
                                ‫افت‬
                                  ‫کو گ‬
                                     ‫بد‬
                                                 ‫[علامت تخصیص ] جپوشونشیااکی که‬
 ‫ببر سوی آن دیو جسته ز بند‬
                                                                  ‫یکایک بیامد خجسته سروش‬
 ‫(‪)۲-۱۱۱-۱۵۶‬‬
                             ‫پوده (بروزن روده)‬     ‫بسان پری پلنگینهپوش‬
                              ‫پوسیده کهنه‪:‬‬         ‫‪۱-۰۲۲‬‬
 ‫پوشیدن‬                                          ‫‪۱۵۱‬‬


           ‫سیاوش بدانست کانمهرچیست‬                     ‫قیصر از خسرو پرویز خواسته است که‬

 ‫چنان دوستی نزه ره ایزدیست‬                         ‫صلیبی را کهعیسی را بهآن بستند و در گنج‬
‫بار دوم سودابه پس از آنکه زمانی زیبایی‬                  ‫ایرانست برایش بفرستد‪ .‬خسروپرویز‬
     ‫می‌گوید‪:‬‬       ‫وش‬
                     ‫ییدابه‬
                          ‫سستا‬
                             ‫خود را می‌‬                ‫خواهش او را می‌پذیرد و به شوخی پاسخ‬
               ‫من اینک بهپیش تواستاده‌ام‬                                               ‫می‌دهد‪:‬‬

‫تن و جان شیرین تو را داده‌ام‬                                     ‫چو پور پدر رفت سوی پدر‬
              ‫زمن هرچ خواهی همهکامتو‬                    ‫تو اندوه این چوب پوده مخور‬

‫برارم نپیچم سر از دام تو‬                                ‫( پرویز (‪.YT‬‏‬


    ‫سرش تنگ بگرفت و یک پوشه چاک‬                                ‫همان دار عیسی نیرزد به رنج‬
‫بداد و نبود آگه از شرم وباک‬                            ‫که شاهان نهادند آن را بهگنج‬
‫‏)‪(TAF-TY-T‬‬
```


## [2026-09-14T01:06:53.097Z] AGENT

Now I have everything. Writing the verification file.


## [2026-09-14T01:15:05.478Z] TOOL CALL #95: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-408.json <<'JSONEOF'\n{\n  \"pdf_page\": 408,\n  \"book_page\": 378,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Pu 2\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *pu- / *p(h)u- 'to blow, blow up, swell' (imitative)\",\n      \"note\": \"Pokorny IEW 847-848 'pū̆-1, peu-, pou- also phu-' meaning 'to blow, blow up'; Watkins/AHD 'pū-1. Also phū-. To blow, swell. Imitative root. [Pok. 1. pu- 847]'. Nourai's English gloss 'to blow, swell' is Watkins' wording verbatim, and POK:847 is the right page. The root is imitative/onomatopoeic, so Pokorny and Watkins both warn it has no fixed IE shape; the numbering 'Pu 2' is Nourai's own (Pokorny numbers it pū̆-1). Language label (Indo-European) and gloss are correct.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *pu-/*p(h)u- «دمیدن، باد کردن، آماسیدن» است؛ پوکورنی آن را در صفحهٔ ۸۴۷ فرهنگ خود (IEW) زیر pū̆-1 آورده و واتکینز در پیوست ریشه‌های هندواروپایی فرهنگ AHD همان معنی «to blow, swell» را می‌دهد که نورایی واژه‌به‌واژه برگرفته است. این ریشه از گونهٔ ریشه‌های آوانمود (onomatopoeic) است و از همین رو صورت واحدی ندارد. برچسب زبانی و معنی ریشه در نمودار درست است؛ تنها شمارهٔ «۲» شماره‌گذاری خود نورایی است نه پوکورنی.\",\n      \"sources\": [\n        \"https://www.etymonline.com/word/pustule\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:847\", \"status\": \"supports\", \"note\": \"POK_full.txt, entry 'Root / lemma: pu-1, peu- pou- also phu-', 'Meaning: to blow, blow up', 'Page(s): 847-848'. The sub-section 'p(h)u-s-' on the same page gives 'Latin pussula, pustula \\\"bubble, vesicle, blister\\\"' and the sub-section 'p(h)u-k-' gives 'npers. pūk \\\"das Blasen (um Feuer anzufachen), Blasebalg\\\"' — i.e. exactly the two children Nourai draws.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. pū-1\", \"stance\": \"supports\", \"note\": \"'pu-1. Also phu-. To blow, swell. Imitative root. 1. Extended form *pus- in Latin pustula, a bubble, blister: PUSTULE. ... [Pok. 1. pu- 847.]' (AHD_watkins1985.txt line 872).\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. II p. 79 ff. (WLD_Bd2_pages.txt line 5351, 5403)\", \"stance\": \"supports\", \"note\": \"Walde-Pokorny Bd. II treats 'pū-, pu- \\\"blasen\\\"' with 'lat. pussula, pustula \\\"Blase, Bläschen\\\"' and cross-refers to 'u. pū- \\\"faulen, stinken\\\"' as a separate root — the same two-root split Nourai keeps (Pu 2 vs Pŭ 4).\"},\n        {\"src\": \"IEC\", \"where\": \"Mann col./p. entry 'pūk- (phūk-)'\", \"stance\": \"supports\", \"note\": \"'pūk- (phūk-) \\\"swell, puff; swelling, puff\\\" ... Alb. cf. pucë, f. \\\"blister, pustule\\\" ... (Extn. in Gk. puknós ...)' (IEC.txt line 13733).\"},\n        {\"src\": \"KLN\", \"where\": \"s.v. pustule\", \"stance\": \"supports\", \"note\": \"'from the I.-E. imitative base *pu-, *phu-, \\\"to blow, swell\\\", whence also OI. pupphusah, \\\"lung\\\" ... Gk. phusa, \\\"pair of bellows; breath, blast, wind, bubble\\\"' (KLN_1966.txt line 31142 area).\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"puk «پوک»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Pokorny does list New Persian pūk under this root, in the sub-section p(h)u-k-: 'npers. pūk \\\"das Blasen (um Feuer anzufachen), Blasebalg\\\", afgh. pūk \\\"a puff, a blast, the act of blowing\\\"' (IEW 847), taking it over from Horn, Grundriss no. 339 (p. 75). The phonology is the sticking point: Horn observes that Armenian pʿukʿ and Greek phūsa point to IE *ph-, while a New Persian p- initial would normally continue IE *p- and NP b- would continue IE *bh-, so 'die richtige neupersische Form muss būk sein'; Bartholomae (letter quoted by Horn) answered that tenuis/tenuis aspirata vary freely in the anlaut, and Hübschmann, Persische Studien no. 339 (p. 44), concludes 'Der Etymologie wegen ist np. pūk nicht zu verdächtigen'. The problem with Nourai's node is the GLOSS: every source that puts pūk under *pu- glosses it 'blowing (to fan a fire), bellows, puff', not 'empty'. NP پوک 'hollow, empty, porous' (Steingass; Wiktionary) is either a semantic extension of the same word ('blown up' > 'puffed up' > 'hollow, with nothing inside') — a step none of the cited authorities actually takes — or a separate expressive formation. Root family right, gloss unsupported: plausible.\",\n          \"derivation_fa\": \"«پوک» در فرهنگ‌های امروزی به معنی «تهی، میان‌خالی، بی‌مغز» است، اما آنچه پوکورنی (ص ۸۴۷) و هرن (بند ۳۳۹، ص ۷۵) زیر این ریشه آورده‌اند «پوک» به معنی «دمیدن (برای برافروختن آتش)، دَم آهنگری» است، با همریشهٔ ارمنی pʿukʿ «دَم» و پشتوی pūk. هرن هشدار می‌دهد که از نظر آوایی صورت درست فارسی باید «بوک» باشد، چون «پ» فارسی نو دنبالهٔ *p هندواروپایی و «ب» دنبالهٔ *bh است؛ ولی بارتولومه و هوبشمان (مطالعات فارسی، بند ۳۳۹، ص ۴۴) این تردید را نپذیرفته‌اند و هوبشمان می‌نویسد ریشه‌شناسی np. pūk جای گمان ندارد. پس پیوند واژه با ریشهٔ «دمیدن» پذیرفتنی است، اما معنی «تهی» که نورایی می‌دهد در هیچ‌یک از منابع یادشده نیامده و تحول معنایی «باد کرده ← میان‌تهی» فرضی است؛ ادعا با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%BE%D9%88%DA%A9\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:847\", \"status\": \"partial\", \"note\": \"POK_full.txt, 'pu-1 ... Page(s): 847-848', sub-section 'p(h)u-k-': 'npers. pūk \\\"das blast (um fire anzufachen), bellows\\\", afgh. pu, puk \\\"a puff, a blast, the act of blowing\\\"' (OCR). Pokorny has the word under this root but glosses it 'blowing, bellows', not 'empty'.\"},\n            {\"ref\": \"HRN:75\", \"status\": \"partial\", \"note\": \"HRN.txt leaf 96 = printed p. 75, no. 339: 'pūk, pŭk: das Blasen (um Feuer anzufachen), Blasebalg. gr. φῦσα ... arm. pʿuk ... Die richtige neupersische Form muss būk sein.' Horn's page is exactly the one cited, but his gloss is 'blowing/bellows' and he flags a phonological difficulty; footnote 2 even asks whether the dictionaries' meaning 'Brennholz' for np. pūk is merely guessed.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"Persische Studien no. 339, p. 44 (HUB.txt line 1469)\", \"stance\": \"supports\", \"note\": \"'339. Der Etymologie wegen ist np. puk nicht zu verdächtigen. Vgl. afgh. pu, puk \\\"a puff, a blast, the act of blowing\\\", pukai \\\"a puff, inflating\\\" ... Lies φῦσα.' — Hübschmann defends the etymology but again only for the sense 'puff, blowing'.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann, s.v. pūk- (phūk-) (IEC.txt line 13733)\", \"stance\": \"partial\", \"note\": \"'pūk- (phūk-) \\\"swell, puff; swelling, puff\\\"' — the root-form is there (with Lith. pūkas, Alb. pucë 'blister'), but Mann lists no Persian reflex.\"},\n            {\"src\": \"ARY\", \"where\": \"ARY_pages.txt, searched پوک\", \"stance\": \"silent\", \"note\": \"Aryanpur's Persian IE-roots dictionary has no entry پوک (grep of ARY_pages.txt for 'پوک' returns only the پوسیدن material).\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/پوک\", \"stance\": \"partial\", \"note\": \"Persian پوک (puk) is glossed simply 'hollow', citing Steingass 1892; no etymology is offered, so the 'empty' sense is attested but unetymologised.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Latin\",\n          \"words\": \"pustula\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin pustula (also pussula, pusula) 'blister, pimple, pustule' is the standard s-extension of the imitative root: *pu-s- + the diminutive-ish -tula/-sula suffix. Watkins states it flatly — 'Extended form *pus- in Latin pustula, a bubble, blister: PUSTULE' — and Pokorny prints 'Latin pussula, pustula \\\"bubble, vesicle, blister\\\"' in the p(h)u-s- paragraph of IEW 847-848 beside Gk. φῦσα 'bellows, bubble', Skt. pusyati, Lith. pūslė 'bladder'. Ernout-Meillet agree: 'D'une racine expressive *p(h)u- élargie par -s- dans pustula'. The semantics are transparent: 'blown up, swollen' > 'bubble' > 'blister on the skin'.\",\n          \"derivation_fa\": \"واژهٔ لاتینی pustula (گونه‌های pussula و pusula) به معنی «تاول، آبله، جوش چرکی» از گسترش *pu-s- همین ریشهٔ آوانمود ساخته شده است. واتکینز می‌نویسد «صورت گسترش‌یافتهٔ *pus- در لاتینی pustula» و پوکورنی (ص ۸۴۷–۸۴۸) در بند p(h)u-s- آن را کنار φῦσα یونانی «دَم، حباب» و pūslė لیتوانیایی «مثانه» می‌آورد. ارنو–مِیه نیز می‌نویسند «از ریشه‌ای تعبیری *p(h)u- که در pustula با -s- گسترش یافته است». تحول معنایی روشن است: «باد کرده، آماسیده» ← «حباب» ← «تاول». ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/pustule\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. pū-1: '1. Extended form *pus- in Latin pustula, a bubble, blister: PUSTULE.' (AHD_watkins1985.txt line 872).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 847-848, section p(h)u-s-\", \"stance\": \"supports\", \"note\": \"'Latin pussula, pustula \\\"bubble, vesicle, blister, bubble\\\"' listed with gr. φῦσα, Lith. pūslė (POK_full.txt, 'pu-1 ... Page(s): 847-848').\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. ~79 (WLD_Bd2_pages.txt line 5403)\", \"stance\": \"supports\", \"note\": \"'lat. pussula, pustula \\\"Blase, Bläschen\\\"' under the 'blasen' root.\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. pustula (LAT.txt lines 51174-51179)\", \"stance\": \"supports\", \"note\": \"'pustula, -ae (pussula; pusula ...) f.: 1° bouton; 2° bulle. ... D'une racine expressive *p(h)u- élargie par -s- dans pustula'.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann s.v. pūstos (IEC.txt line 13805)\", \"stance\": \"supports\", \"note\": \"'pūstos (phūstos) \\\"swollen, inflated; puff, swelling\\\" ... Lat. cf. pustula, f. \\\"blister, pustule\\\"'.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"English\",\n          \"words\": \"pus; pustule\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"PUSTULE is right: Middle English pustule, from Old French pustule (13th c.) and directly from Latin pustula — a learned/medical borrowing, so the chain Latin > Old French > Middle English is exactly Nourai's arrow (Klein s.v. pustule; Etymonline). PUS is wrong as drawn. English pus (late 14th c., medical) is Latin pūs, pūris 'viscous matter, pus', and pūs does NOT come from pustula: it is the s-stem *puw-os- of the OTHER root, PIE *puH- 'to rot, decay' — i.e. Nourai's own next root Pŭ 4, Peua, where it belongs beside puter, putidus, Gk. πύον and Gothic fūls. Watkins puts PUS under pū-2 §5a ('Suffixed form *puw-os- in: a. Latin pus, pus: PURULENT, PUS'), Klein s.v. pus derives it 'fr. I.-E. base *pu-, \\\"to rot, stink\\\"' and cross-refers to foul, and Etymonline gives 'PIE root *pu- (2) \\\"to rot, decay\\\"'. So this node mixes two different roots; the node verdict takes the worse of the two words.\",\n          \"derivation_fa\": \"واژهٔ pustule انگلیسی درست همان‌گونه است که نمودار نشان می‌دهد: از فرانسهٔ کهن pustule (سدهٔ سیزدهم) و در نهایت از pustula لاتینی، وام‌واژه‌ای پزشکی-دانشورانه. اما pus نادرست جای گرفته است: pus انگلیسی (سدهٔ چهاردهم) از pūs, pūris لاتینی است و pūs خود از pustula نمی‌آید، بلکه ستاک -s داری از ریشهٔ دیگری است، یعنی *puH- هندواروپایی «پوسیدن، گندیدن» — همان ریشه‌ای که خود نورایی در ورودی بعدی (Pŭ 4, Peua) آورده است. واتکینز pus را زیر pū-2 «to rot, decay» می‌آورد، کلاین می‌نویسد «از ریشهٔ هندواروپایی *pu- \\\"گندیدن، بو گرفتن\\\"» و etymonline نیز همین را می‌گوید. بنابراین پژوهش امروزی این پیکان (pustula ← pus) را رد می‌کند و pus را به ریشهٔ «پوسیدن» می‌سپارد؛ داوری گره بر پایهٔ بدترین واژه «مردود» است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/pus\",\n            \"https://www.etymonline.com/word/pustule\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"The node carries refs=None in the book; the parent Latin box cites AHD, and Watkins/AHD in fact contradicts the pus arrow (see consulted).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. pus and s.v. pustule (KLN_1966.txt lines 31093, 31142)\", \"stance\": \"contradicts\", \"note\": \"'pus, n. ... — L. pus, \\\"viscous matter, pus\\\", rel. to putere, \\\"to stink, be rotten\\\", puter, putridus, \\\"foul, rotten\\\", fr. I.-E. base *pu-, \\\"to rot, stink\\\" ... See foul, adj.' vs. 'pustule, n. — ME., fr. L. pustula ... from the I.-E. imitative base *pu-, *phu-, \\\"to blow, swell\\\"'. Klein keeps the two words under two different roots.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. pū-2 §5a; index 'PUSTULE pu-1 ... PUS' \", \"stance\": \"contradicts\", \"note\": \"'5. Suffixed form *puw-os- in: a. Latin pus, pus: PURULENT, PUS; SUPPURATE; b. Greek puon, puos, pus: PYO-. [Pok. 2. pū- 848.]' — AHD, the reference the parent node cites, assigns PUS to the rot-root, not to pustula.\"},\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/pus and /word/pustule\", \"stance\": \"contradicts\", \"note\": \"pus: 'from PIE *pu- (2) \\\"to rot, decay\\\"'; pustule: 'from PIE root *pu- (1) \\\"blow, swell\\\"'. Two roots, two words.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 2,\n      \"root\": \"Pŭ 4, Peua\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *puH- / *p(e)uH- 'to rot, decay, stink' (Pokorny pū̆-2 : peuə-)\",\n      \"note\": \"Pokorny IEW 848-849 'pū̆-2 : peuə-', 'Meaning: to rot, stink' — so Nourai's 'Peua' is Pokorny's peuə- with the schwa written 'a', and POK:848 is the correct first page. Watkins has the same root as 'pū-2. To rot, decay. [Pok. 2. pū- 848.]'; Cheung's Etymological Dictionary of the Iranian Verb sets up *pauH 'to stink, smell, rot' and refers it to 'PIE *p(e)uH- \\\"to rot, decay, stink\\\" — LIV: 480 f. | Pok.: 848 f.'. Root, language label and gloss are all correct. The chart's NOTE on the Persian box ('This poem is about the wooden cross of Jesus') is itself correct: Noushin's Farhang-e Shahnameh p. 151 s.v. پوده explains that Caesar asked Khosrow Parviz for the cross Jesus was bound to, kept in the Iranian treasury, and Khosrow answered jokingly with this very bayt.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *puH-/*p(e)uH- «پوسیدن، گندیدن، بوی بد دادن» است؛ پوکورنی آن را زیر pū̆-2 : peuə- در صفحه‌های ۸۴۸–۸۴۹ آورده و «Peua»ی نورایی همان peuə- با شوا است. واتکینز نیز pū-2 «to rot, decay» دارد و چونگ در فرهنگ ریشه‌شناختی فعل ایرانی ستاک *pauH «گندیدن، پوسیدن» را برمی‌سازد و آن را به *p(e)uH- هندواروپایی (LIV ۴۸۰) بازمی‌گرداند. ریشه، برچسب زبانی و معنی هر سه درست‌اند. یادداشت نمودار دربارهٔ بیت فردوسی نیز درست است: عبدالحسین نوشین در «واژه‌نامک» (ص ۱۵۱، ذیل پوده) می‌نویسد قیصر از خسروپرویز صلیب عیسی را که در گنج ایران بود خواست و خسرو به شوخی چنین پاسخ داد.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D9%BE%D9%88%D8%B3%DB%8C%D8%AF%D9%86\",\n        \"https://www.etymonline.com/word/pus\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:848\", \"status\": \"supports\", \"note\": \"POK_full.txt: 'Root / lemma: pu-2 : peuə-', 'Meaning: to rot, stink', 'Page(s): 848-849'. Material includes 'Old Indic pūyati \\\"wird faul, stinkt\\\" = Avestan puyeiti', 'Avestan pūitay- \\\"Fauligwerden, Verwesung\\\"', 'with -sk̑o- Middle Persian pūsīnītan', 'Gothic fūls, Old Icelandic fūll, Old English/Old High German fūl'.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. pū-2\", \"stance\": \"supports\", \"note\": \"'pu-2. To rot, decay. ... [Pok. 2. pū- 848.]' (AHD_watkins1985.txt lines 872-874).\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. II p. 82 (WLD_Bd2_pages.txt lines 5427 ff.)\", \"stance\": \"supports\", \"note\": \"'pū-, pu-, vereinzelt und zweifelhaften Alters (pou oder pau) \\\"faulen; stinken\\\"; vermutlich aus einem pu \\\"pfui\\\" entwickelt.'\"},\n        {\"src\": \"CHEUNG\", \"where\": \"s.v. *pauH (CHEUNG.txt lines 19901 ff.)\", \"stance\": \"supports\", \"note\": \"'*pauH \\\"to stink, smell, rot\\\" ... «PIE *p(e)uH- \\\"to rot, decay, stink\\\" — LIV: 480 f. | Pok.: 848 f.'\"},\n        {\"src\": \"FSF\", \"where\": \"Noushin, Farhang-e Shahnameh p. 151 s.v. پوده\", \"stance\": \"supports\", \"note\": \"'پوده (بر وزن روده): پوسیده، کهنه ... قیصر از خسرو پرویز خواسته است که صلیبی را که عیسی را به آن بستند و در گنج ایرانست برایش بفرستد ... چو پور پدر رفت سوی پدر / تو اندوه این چوب پوده مخور' — confirms both the verse and Nourai's note about the cross.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"pu 2, pav, puyeiti; pŭtay, pŭiti\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Bartholomae's Altiranisches Wörterbuch has the verb as '√pav- \\\"faulig werden, verwesen\\\", Praes. 27 puya-', quoting Vd. 5.28 'yeziča aēte nasāvō frisyeinti puyeinti' — 'und wenn die Leichname verfaulen und verwesen' — so both Nourai's citation forms pav- (root grade) and puyeiti (3sg. present of the ya-present *puya-) are correct Avestan. Bartholomae adds the descent chain himself: 'ai. pūyati, oss. æmbiyun, mp. pūsītan, np. pūsīdan'. Cheung s.v. *pauH gives 'Y Av. pu- \\\"to stink, smell, rot\\\"; Pres. /a-: IND. 3sg. YAv. puiieti (V 6.28); Partic. YAv. apuiiant- \\\"not stinking, rotting\\\"'. The nominal forms are equally real: pūitay- f. and its by-form *pavitay- f. 'Fäulnis, Verwesung' (Vd. 5.27), matching Nourai's 'pŭtay, pŭiti' — but note that these are feminine abstract NOUNS ('putrefaction, decay'), not the adjective 'rotten' that Nourai glosses them with; the adjective is pūta-. The derivation from the root is the regular ti-abstract *puH-ti-.\",\n          \"derivation_fa\": \"بارتولومه در «فرهنگ ایرانی باستان» ریشهٔ اوستایی را چنین می‌آورد: «√pav- \\\"گندیدن، پوسیدن\\\"، ستاک حال puya-» با شاهد وندیداد ۵٫۲۸ «puyeinti» یعنی «و چون پیکرها بگندند و بپوسند»؛ پس هر دو صورت pav- و puyeiti در نمودار درست‌اند. خودِ بارتولومه زنجیرهٔ تحول را هم می‌دهد: سنسکریت pūyati، آسی æmbiyun، فارسی میانه pūsītan، فارسی نو پوسیدن. چونگ نیز zیر *pauH صورت puiieti و صفت فاعلی apuiiant- «نگندنده» را می‌آورد. صورت‌های اسمی pūitay- و *pavitay- «گندیدگی، پوسیدگی» (وندیداد ۵٫۲۷) نیز راست‌اند و همان «pŭtay, pŭiti»ی نمودارند؛ تنها نکته آنکه این‌ها اسم مؤنث انتزاعی‌اند نه صفت «پوسیده»، و صفت مربوط pūta- است. پس ادعای نورایی درست است، با اصلاحی خُرد در معنی.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%BE%D9%88%D8%B3%DB%8C%D8%AF%D9%86\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:849\", \"status\": \"supports\", \"note\": \"The entry 'pu-2 : peuə-' runs over 848-849; its material opens 'Old Indic pūyati \\\"wird faul, stinkt\\\" = Avestan puyeiti \\\"wird faul\\\" ... pūti- \\\"faul, stinkend\\\" = Avestan pūitay- \\\"Fauligwerden, Verwesung\\\"' (POK_full.txt).\"},\n            {\"ref\": \"SNS:137\", \"status\": \"partial\", \"note\": \"Tavoosi's Shayast ne Shayast glossary does carry an entry built on this root — SNS_pages.txt leaf 84 (the leaf is headed 'p. 119' in the scan) reads '(AiW. 909) patay: pu/pav — pūtay-', i.e. exactly Nourai's Avestan citation forms with Bartholomae's column number. The scan's printed page 137 could not be reached (page images are not in the ref_page.py scan list and the Persian OCR of the page headers is garbage), so the page number itself is unverified while the content is confirmed.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch s.v. pav- and *pavitay- (BRT.txt lines 15302, 17492)\", \"stance\": \"supports\", \"note\": \"'• j. pav- V. \\\"faulig werden, verwesen\\\" Praes. 27 puya-. ... ai. pūyati, oss. æmbiyun, mp. pūsītan, np. pūsīdan'; and '• j. *pavitay- f. \\\"Fäulnis, Verwesung\\\" ... Zum V. pav-: — Vgl. pūitay-'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"s.v. *pauH, AVESTAN section (CHEUNG.txt line 19903)\", \"stance\": \"supports\", \"note\": \"'*AVESTAN: Y Av. pu- \\\"to stink, smell, rot\\\" = Liste: 35. Pres. /a-: IND. 3sg. YAv. puiieti (V 6.28); Partic.: pres. YAv. apuiiant- \\\"not stinking, rotting\\\" (Yt 19.11 ...)'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. 82 (WLD_Bd2_pages.txt line 5434)\", \"stance\": \"supports\", \"note\": \"'Ai. pūyati \\\"wird faul, stinkt\\\" = av. puyeiti \\\"wird faul\\\", ai. pūya-ḥ \\\"Eiter\\\", pūti-ḥ \\\"faul, stinkend\\\" = av. pūtay- \\\"Fauligwerden, Verwesung\\\"'.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"pŭsîtan; pŭdag, pŭtak\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both Pahlavi words are attested and both descend regularly from the Avestan/Old Iranian material of the parent node. pūdag, written pwtk' (hence Nourai's doublet 'pŭdag, pŭtak' — the same word in MacKenzie's normalisation and in the older transliteration of the Pahlavi spelling), continues Old Iranian *pū-ta-ka-, the verbal adjective *puH-to- 'rotted' plus the productive -ka- suffix, with the regular Middle Persian lenition of intervocalic -t- to -d-; MacKenzie prints 'pūdag [pwtk' | N pūda] foul, rotten. ~īh: rottenness' and Nyberg glosses pūtakēh [pwtkyh] 'decomposition, decay'. The verb pūsītan is the inchoative in *-s- (IE *-sk̑e/o-): Pokorny explicitly notes 'mit -sk̑o- mp. pūsīnītan', Horn no. 334 lists 'phlv. pūtak, pūsīnītan, pūs(i)šn', and Bailey (BSOS 9, 1937, 73) writes 'Mid. Pers. hambūsīstan, pūtak, NPers. anbūsīdan, pūsīdan \\\"to rot\\\"'. Nourai's spelling pūsītan is the bare stem without the causative -īn-, exactly the form Bartholomae cites ('mp. pūsītan').\",\n          \"derivation_fa\": \"هر دو واژهٔ فارسی میانه راست‌اند و هر دو از مادهٔ اوستایی گرهِ بالادست می‌آیند. pūdag (نوشتهٔ pwtk'، و از همین رو دو صورت «pŭdag / pŭtak» در نمودار: یکی آوانگاری امروزی و دیگری حرف‌نویسی املای پهلوی) دنبالهٔ ایرانی باستان *pū-ta-ka- است، یعنی صفت مفعولی *puH-to- «پوسیده» به‌علاوهٔ پسوند -ka-، با نرم‌شدن قانونمند «ت» میان‌واکه‌ای به «د» در فارسی میانه؛ مکنزی می‌نویسد «pūdag [pwtk'] گندیده، پوسیده» و نیبرگ pūtakēh «پوسیدگی» را می‌آورد. فعل pūsītan ستاک آغازی (inchoative) با -s- (از *-sk̑e/o- هندواروپایی) است: پوکورنی می‌نویسد «با -sk̑o-: فارسی میانه pūsīnītan»، هرن (بند ۳۳۴) «phlv. pūtak, pūsīnītan, pūs(i)šn» دارد و بیلی (۱۹۳۷، ص ۷۳) «فارسی میانه hambūsīstan, pūtak» می‌نویسد. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%BE%D9%88%D8%AF%D9%87\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:849\", \"status\": \"supports\", \"note\": \"POK_full.txt, entry 'pu-2 : peuə-' (Page(s): 848-849): 'with -sk̑o- Middle Persian pūsīnītan \\\"decayed\\\", Old Icelandic fauskr \\\"rotten, decayed ... wood\\\"' (OCR 'pusinTtan'). Pokorny's Middle Persian form is the -īn- extended pūsīnītan; Nourai's pūsītan is the shorter variant Bartholomae cites.\"},\n            {\"ref\": \"SNS:137\", \"status\": \"partial\", \"note\": \"Same as node 1: the Shayast ne Shayast glossary entry that cites AiW 909 pu/pav, pūtay- was located (SNS_pages.txt leaf 84, scan header 'p. 119'), but the printed page 137 could not be confirmed — the volume's OCR page numbers are unreadable and it is not in the ref_page.py scan set.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary, s.v. pūdag (PHD.txt line 551)\", \"stance\": \"supports\", \"note\": \"'pūdag [pwtk' | N pūda] foul, rotten. ~ih: rottenness.' — MacKenzie confirms pūdag/pwtk' and its New Persian continuation, but has no verb pūsīdan/pūsītan.\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary (NYB_vol2_glossary.txt line 3192)\", \"stance\": \"supports\", \"note\": \"'pūtakēh [pwtkyh] decomposition, decay 112°.' — the abstract of pūtak.\"},\n            {\"src\": \"BLY\", \"where\": \"Bailey, 'Hvatanica II', BSOS 9 (1937) p. 73 (BLY_pages.txt leaf 6)\", \"stance\": \"supports\", \"note\": \"'hambīta-, hambūva- must be connected with Oss. æmbuyun \\\"to rot\\\", Mid. Pers. hambūsīstan, pūtak, NPers. anbūsīdan, pūsīdan \\\"to rot\\\", Av. ... Skt. pūy-.'\"},\n            {\"src\": \"CHEUNG\", \"where\": \"s.v. *pauH, MIDDLE PERSIAN / PARTHIAN (CHEUNG.txt lines 19907-19909)\", \"stance\": \"supports\", \"note\": \"'*MIDDLE PERSIAN: BMP pwtk /pudag/ \\\"foul, rotten\\\"; *PARTHIAN: pwd \\\"decay\\\" > DMMPP: 286a'.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"pŭsîdan «پوسیدن»; pŭdeh «پوده» (extra: پوس)\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP پوسیدن pūsīdan 'to rot' is the direct continuation of the Middle Persian inchoative pūsī(nī)tan, with the regular Middle Persian -tan > New Persian -dan of the infinitive after a vowel/sibilant, giving the present stem پوس pūs- (the chart's 'extra' script form) beside the past stem پوسید. Abolghasemi, Fe'l-hā-ye Fārsi-ye Dari p. 44, sets it out exactly so: «پوسیدن ... پوس < ایرانی باستان *puš-. ... *pu صورت ضعیف ریشهٔ *pau است. ریشهٔ *pau «پوسیدن» معنی می‌دهد. «پوده» به معنی «پوسیده» از ریشهٔ *pau گرفته شده است ... < فارسی میانه pūdag < ایرانی باستان *pu-ta-ka-». پوده pūde 'rotten, decayed (esp. of wood)' is MP pūdag with the regular New Persian loss of final -g after the vowel (MP -ag > NP -a/-e). Cheung lists 'NP pūsīdan/pūs-' and 'NP anbūsīdan' under *pauH, and Bartholomae gives the whole chain 'av. pav- ... mp. pūsītan, np. pūsīdan'. The Ferdowsi bayt quoted in the chart ('چو پور پدر رفت سوی پدر ــ تو اندوه این چوب پوده مخور') is genuine Shahnameh (Khosrow Parviz section) and Nourai's note is right: Noushin's Farhang-e Shahnameh p. 151 s.v. پوده explains that Caesar asked for the cross on which Jesus was bound, kept in the Iranian treasury, and Khosrow replied with this couplet.\",\n          \"derivation_fa\": \"«پوسیدن» دنبالهٔ مستقیم فعل آغازی فارسی میانهٔ pūsī(nī)tan است؛ مصدرِ -tan فارسی میانه پس از واکه و سایشی به -dan فارسی نو بدل شده و ستاک حال «پوس» (همان صورت افزودهٔ نمودار) و ستاک گذشتهٔ «پوسید» به دست آمده است. ابوالقاسمی در «ماده‌های فعل‌های فارسی دری» (ص ۴۴) دقیقاً همین را می‌نویسد: «پوس < ایرانی باستان *puš- ... *pu صورت ضعیف ریشهٔ *pau است ... «پوده» به معنی «پوسیده» از ریشهٔ *pau گرفته شده ... < فارسی میانه pūdag < ایرانی باستان *pu-ta-ka-». «پوده» نیز همان pūdag پهلوی است با افتادن قانونمند «گ» پایانی (پهلوی -ag ← فارسی نو -ه). چونگ صورت «NP pūsīdan/pūs-» و «انبوسیدن» را زیر *pauH می‌آورد. بیت فردوسی نیز از بخش خسروپرویز شاهنامه است و یادداشت نورایی دربارهٔ چوب صلیب عیسی، به گواهی «واژه‌نامک» نوشین (ص ۱۵۱)، درست است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%BE%D9%88%D8%B3%DB%8C%D8%AF%D9%86\",\n            \"https://en.wiktionary.org/wiki/%D9%BE%D9%88%D8%AF%D9%87\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:425,429\", \"status\": \"partial\", \"note\": \"Borhan-e Qate' does carry پوده: in the archive.org scan of vol. 1 the chapter divider «بیان نوزدهم — در بای فارسی با واو» stands on leaf 650 and the entry is on leaf 651: «پوده - بر وزن روده ... و چوبی پوسیده که آن را بجهت آتشگیره مهیا کرده باشند ... و گندیده و ضایع شده را هم گفته‌اند». The printed pages 425/429 could not be confirmed: BQT_v1_pages.txt has no page tags, the OCR'd page numbers in the headers are unreliable, and ref_page.py reports 'no scan of BQT covers printed page 425'. No headword پوسیدن was found in the OCR of leaves 651-654; Mo'in's etymological footnotes on those leaves are illegible in this OCR.\"},\n            {\"ref\": \"FFD:44\", \"status\": \"supports\", \"note\": \"Abolghasemi, Fe'l-hā-ye Fārsi-ye Dari, printed p. 44 = pdf page 49 (FFD_pages.txt, leaf 49): «پوسیدن / (پوسید» مادهٔ ماضی جعلی است ... پوس < ایرانی باستان *puš- ... *pu صورت ضعیف ریشهٔ *pau است. ریشهٔ *pau «پوسیدن» معنی می‌دهد. «پوده» به معنی «پوسیده» از ریشهٔ *pau گرفته شده است ... < فارسی میانه pūdag < ایرانی باستان *pu-ta-ka-». Exactly Nourai's chain, on exactly the cited page.\"},\n            {\"ref\": \"BLY:73\", \"status\": \"supports\", \"note\": \"Bailey, 'Hvatanica II', BSOS 9 (1937), p. 73 (BLY_pages.txt leaf 6 = printed 73): 'must be connected with Oss. æmbuyun \\\"to rot\\\", Mid. Pers. hambūsīstan, pūtak, NPers. anbūsīdan, pūsīdan \\\"to rot\\\"'. The cited page is correct.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"Grundriss no. 334, p. 74 (HRN.txt leaf 95)\", \"stance\": \"supports\", \"note\": \"'334. pūde \\\"faul, verfault\\\", pūsīden (Inchoat.) \\\"faulen\\\". aw. pūiti- \\\"Fäulniss\\\", apuyant- \\\"nicht faulend\\\"; phlv. pūtak, pūsīnītan, pūs(i)šn, arm. LW. put; skr. pūyati, ai. pūti- \\\"faul, stinkend\\\". oss. d. am-bud, t. ämbid \\\"faul\\\".' — Horn gives the whole chart in one entry.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"s.v. *pauH, NWIR section (CHEUNG.txt line 19921)\", \"stance\": \"supports\", \"note\": \"'*NWIR: NP pūsidan/pūs- ... (inch.) \\\"to rot\\\", Kurd. (Kurm.) pūč \\\"rotten; useless\\\" || (+ *ham-) NP anbūsidan/anbūs- \\\"to rot\\\".'\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-hā, pdf p. 179 s.v. «پوسیدن، پوده»\", \"stance\": \"supports\", \"note\": \"Independent modern Persian cross-check: the entry lists Avestan, Pahlavi pūtāk, Ossetic, Kurdish, Sanskrit pūti/pūyati, Armenian, Greek, Latin pūs/pūteō/pūtridus, Old English fūl, English FOUL, Gothic fūls, Lithuanian — i.e. the same family, and it too puts Latin PUS and English FOUL here rather than under the 'blow' root.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. pūdag\", \"stance\": \"supports\", \"note\": \"'pūdag [pwtk' | N pūda] foul, rotten' — MacKenzie himself gives the New Persian outcome پوده.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Germanic\",\n          \"words\": \"fŭ-faz; fŭlithô; fausa\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"The second and third forms are right: Germanic *fūlithō 'foulness' (OE fylð > FILTH, OHG fūlida) and *fausa- 'spongy' (Low German fussig, Du. voos, Norw. føyr < *fauza-) are both Watkins' forms under pū-2. The first, printed 'fŭ-faz', is impossible: there is no Germanic *fū-faz. It is a misprint for *fū-laz, the suffixed form *pū-lo- that gives Gothic fūls, ON fúll, OE fūl 'foul'. Watkins pū-2 §1: 'Suffixed form *pū-lo- in Germanic *fūlaz, rotten, filthy, in: a. Old English fūl, unclean, rotten: FOUL; ... c. Germanic abstract noun *fūlithō in Old English fylth, foulness: FILTH'; Klein s.v. foul: 'Goth. fūls; formed with suff. -la fr. Teut. base *fū-'; Walde-Pokorny II 82: 'got. fūls, aisl. fūll, ags., ahd. fūl \\\"faul\\\"'. The l/f confusion is the book's own: the 300 dpi render of PDF p. 408 plainly shows 'fŭ-faz : rotten' in the Germanic box, so the JSON extraction is faithful and Nourai (or his typesetter) misread his AHD source. Note also that Watkins' *fausa- is glossed simply 'spongy' (Low German fussig); Nourai's added 'rotten' comes from the wider root meaning.\",\n          \"derivation_fa\": \"دو صورت دوم و سوم درست‌اند: ژرمنی *fūlithō «پلیدی» (انگلیسی کهن fylð ← filth، آلمانی علیای کهن fūlida) و *fausa- «اسفنجی» (آلمانی سفلای fussig، هلندی voos، نروژی føyr از *fauza-)، هر دو در واتکینز زیر pū-2 آمده‌اند. اما صورت نخست که کتاب «fŭ-faz» چاپ کرده ناممکن است: در ژرمنی چنین صورتی نیست و این خطای چاپی به‌جای *fū-laz است، یعنی همان *pū-lo- پسوندداری که گوتیک fūls، ایسلندی کهن fúll و انگلیسی کهن fūl «گندیده» از آن آمده‌اند. واتکینز می‌نویسد «صورت پسونددار *pū-lo- در ژرمنی *fūlaz»، کلاین ذیل foul می‌نویسد «گوتیک fūls؛ با پسوند -la از ستاک ژرمنی *fū-» و والده–پوکورنی (جلد ۲، ص ۸۲) «got. fūls, aisl. fūll, ags., ahd. fūl». تصویر ۳۰۰ نقطه‌ای صفحهٔ ۴۰۸ نشان می‌دهد که خودِ کتاب «fŭ-faz» چاپ کرده است؛ پس خطای چاپی کتاب است، نه خطای خوانش اسکن.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"fŭ-faz\",\n          \"correct_form\": \"fū-laz (Gmc. *fūlaz, from PIE *pū-lo-)\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/pus\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins 1985 s.v. pū-2 has all three forms but the first as *fūlaz, not *fūfaz: '1. Suffixed form *pū-lo- in Germanic *fūlaz, rotten, filthy, in: a. Old English fūl ...: FOUL ... c. Germanic abstract noun *fūlithō in Old English fylth, foulness: FILTH ... 3. Extended variant form *pous- in Germanic *fausa- in Low German fussig, spongy: FUZZY.' (AHD_watkins1985.txt lines 872-874). So the reference supports the node except for the misprinted first form.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. foul, adj. (KLN_1966.txt line 15268)\", \"stance\": \"partial\", \"note\": \"'foul, adj. — ME. foul, fr. OE. fūl, rel. to OS., OFris., MLG., OHG., MHG. fūl, ON. fúll ... Goth. fūls; formed with suff. -la fr. Teut. base *fū- ..., corresponding to I.-E. base *pū-' — confirms *fū- + -la-, i.e. *fūlaz, never *fūfaz.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. 82 (WLD_Bd2_pages.txt lines 5434 ff.)\", \"stance\": \"partial\", \"note\": \"'got. fūls, aisl. fūll, ags., ahd. fūl \\\"faul\\\" ... mit s-: aisl. fauskr \\\"faules, morsches Holz\\\", norw. mdartl. føyr (*fauza-) \\\"morsch\\\", ndl. voos \\\"schwammig\\\"' — supports *fūlaz and *fausa-/*fauza-, no *fūfaz.\"},\n            {\"src\": \"BOOK\", \"where\": \"PDF p. 408, Germanic box (data/verification/sources/refs/ocr/BOOK/408.png)\", \"stance\": \"supports\", \"note\": \"The 300 dpi render shows 'fŭ-faz : rotten / fŭlithô : foulness / fausa : spongy, rotten' — the extraction into page-408.json is faithful; the error is the printed book's.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"foul; filth; fuzzy\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three are Watkins' English outcomes of the Germanic forms in the parent box. FOUL: OE fūl 'unclean, rotten' (< Gmc. *fūlaz) > ME foul > foul, with the regular OE ū > ME /uː/ > Great Vowel Shift /aʊ/. FILTH: OE fylð (i-umlaut of ū before the -ithō abstract suffix, hence y) > ME filthe > filth; Klein 'filth, n. — ME. filthe, fulthe, fr. OE. fylð, rel. to OHG. fūlida \\\"filth\\\". See foul and subst. suff. -th'. FUZZY is not native: it is a 17th-c. borrowing from Low German fussig 'weak, loose, spongy' (Klein s.v. fuzzy: 'LG. fussig, \\\"weak, loose, spongy\\\"; rel. to Du. voos, \\\"spongy\\\"'), which is Watkins' Gmc. *fausa-; fuzz is a back-formation from fuzzy. So the arrow Germanic > English holds for each word, with fuzzy borrowed rather than inherited.\",\n          \"derivation_fa\": \"هر سه واژه همان بازمانده‌های انگلیسی صورت‌های ژرمنی گرهِ بالادست‌اند. foul از انگلیسی کهن fūl «ناپاک، گندیده» (از ژرمنی *fūlaz) با تحول آوایی قانونمند ū کهن ← /aʊ/ امروزی؛ filth از انگلیسی کهن fylð که y آن نتیجهٔ امالهٔ (i-umlaut) ū پیش از پسوند اسم‌ساز -ithō است، و کلاین آن را به OHG fūlida «پلیدی» می‌پیوندد؛ اما fuzzy واژه‌ای بومی نیست بلکه وام‌واژه‌ای از آلمانی سفلای fussig «سست، اسفنجی» (کلاین: «LG. fussig، هم‌ریشه با هلندی voos») است که همان *fausa- ژرمنی واتکینز است، و fuzz خود ساختی پس‌گشتی از fuzzy است. بنابراین پیکان «ژرمنی ← انگلیسی» برای هر سه درست است، با این تفاوت که fuzzy وام‌گیری است نه میراث.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/pus\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. pū-2: FOUL (§1a), FILTH (§1c) and FUZZY (§3) are all listed as English outcomes; the index confirms 'FUZZY pu-2' and 'FULMAR pu-2' (AHD_watkins1985.txt lines 872-874, 1547).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. foul, filth, fuzzy (KLN_1966.txt lines 15268, 14736, 15621)\", \"stance\": \"supports\", \"note\": \"'foul, adj. — ME. foul, fr. OE. fūl ... corresponding to I.-E. base *pū-'; 'filth, n. — ME. filthe, fulthe, fr. OE. fylð, rel. to OHG. fūlida, \\\"filth\\\". See foul'; 'fuzzy, adj., covered with fuzz; fluffy. — LG. fussig, \\\"weak, loose, spongy\\\"; rel. to Du. voos, \\\"spongy\\\".'\"},\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/pus, related entry 'foul'\", \"stance\": \"supports\", \"note\": \"'Foul: Derived from Old English ful, connected through the same PIE root *pu-, originally relating to decay and unpleasantness.'\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur pdf p. 179, s.v. «پوسیدن، پوده»\", \"stance\": \"supports\", \"note\": \"The entry's English column gives 'FOUL' and its Old English fūl, listing them with Latin pūs and Avestan/Pahlavi forms of this root.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 4,\n      \"root\": \"Puk\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *puk̑- 'to press/bundle together, enclose tightly'\",\n      \"note\": \"Pokorny IEW 849 has 'puk̑-2', 'Meaning: to enclose, put together', with exactly the three members Nourai draws: 'Avestan pusa- f. \\\"headband\\\"; gr. ἄμπυξ m. \\\"headband\\\", Adverb πύκα \\\"tight, firm, dense\\\", ... πυκινός, newer πυκνός \\\"dense, tight, firm\\\"; alb. puth \\\"kusse\\\", actually \\\"umarme\\\"'. Watkins calls it 'puk-1. To make fast. ... Greek pukinos, later puknos ... [Pok. 2. puk- 849]'. Mann, IE Comparative Dictionary, s.v. puk̑-, glosses it 'fit, enclose, hug, embrace, encircle' and lists 'Av. pusā, f. \\\"diadem\\\"; Per. pūse, id.; Gk. púka ...; puknós, pukinós ...; cf. ám-pux, gs: -pukos'. So root, page and gloss ('bundled together') are all sound. One nuance worth recording: Walde-Pokorny (1927) II 82-83 had NOT yet joined Av. pusā- to this root — there it appears under the neighbouring root 'puq-, punq- \\\"dicht behaart, buschig\\\"' (with Skt. puccha- 'tail', Gmc. *fuhsaz 'fox'), 'zu vermutlich av. pusā f. \\\"Diadem\\\" (Zubatý KZ 31, 13, Bthl. Wb. 911 f. zw.; ursprünglich ein pelzbesetzter Turban?)'. Pokorny 1959 moved it; Nourai follows the 1959 arrangement, which is also Klein's and Mann's.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *puk̑- «به‌هم فشردن، دسته کردن، تنگ در بر گرفتن» است. پوکورنی (IEW ص ۸۴۹) زیر puk̑-2 با معنی «to enclose, put together» دقیقاً همین سه عضو را می‌آورد: اوستایی pusa- «سربند»، یونانی ἄμπυξ «سربند» و πύκα/πυκνός «انبوه، فشرده»، و آلبانیایی puth «می‌بوسم» (در اصل «در آغوش می‌گیرم»). واتکینز آن را puk-1 «to make fast» می‌نامد و مان در فرهنگ تطبیقی هندواروپایی معنی «fit, enclose, hug, embrace, encircle» می‌دهد و صورت‌های Av. pusā، Gk. púka/puknós و ám-pux (اضافی -pukos) را فهرست می‌کند. پس ریشه، شمارهٔ صفحه و معنی «bundled together» درست‌اند. تنها نکتهٔ تاریخی آنکه والده–پوکورنی (۱۹۲۷، جلد ۲، ص ۸۲–۸۳) هنوز pusā- اوستایی را نه به این ریشه بلکه به ریشهٔ همسایهٔ *puk̑- «پرمو، پُرپشم (دُم انبوه)» می‌بست؛ پوکورنی در ۱۹۵۹ آن را جابه‌جا کرد و نورایی از چیدمان ۱۹۵۹ پیروی می‌کند.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%CF%80%CF%85%CE%BA%CE%BD%CF%8C%CF%82\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:849\", \"status\": \"supports\", \"note\": \"POK_full.txt: 'Root / lemma: puk̑-2', 'Meaning: to enclose, put together', 'Page(s): 849'; material: 'Avestan pusa- f. \\\"headband\\\"; gr. ἄμπυξ m. \\\"headband\\\", Adverb. πύκα \\\"tight, firm, dense\\\" ... πυκινός newer πυκνός \\\"dense, tight, firm\\\"; alb. puth \\\"kusse\\\", actually \\\"umarme\\\". References: WP. II 82.'\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. puk-1 (AHD_watkins1985.txt line 876)\", \"stance\": \"supports\", \"note\": \"'puk-1. To make fast. Suffixed form *puk-ino- in Greek pukinos, later puknos, strong, fast, thick: PYKNIC; PYCNIDIUM, PYCNOMETER. [Pok. 2. puk- 849.]'\"},\n        {\"src\": \"IEC\", \"where\": \"Mann s.v. puk̑- (IEC.txt line 13748)\", \"stance\": \"supports\", \"note\": \"'puk- \\\"fit, enclose, hug, embrace, encircle\\\". WP II, 82. Av. pusa, f. \\\"diadem\\\"; Per. puse, id.; Gk. cf. púka, adv. \\\"close-fitting\\\"; puknós, pukinós, adj. \\\"compact\\\"; cf. ám-pux, gs: -pukos, m & f \\\"chaplet\\\" ... Alb. puth, v. \\\"kiss\\\".'\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. II pp. 82-83 (WLD_Bd2_pages.txt lines 5471, 5483-5485)\", \"stance\": \"partial\", \"note\": \"'puk̑- \\\"zusammendrängen, eng umschließen\\\". Gr. πυκνός \\\"fest, dicht ...\\\", πύκα Adv. ...; alb. puth \\\"küsse\\\"' — but Av. pusā- is placed in the NEXT entry, 'puq-, punq- etwa \\\"dicht behaart, buschig\\\" ... wozu vermutlich av. pusā f. \\\"Diadem\\\"'. WLD 1927 keeps pusā- apart from πυκνός; IEW 1959 unites them.\"},\n        {\"src\": \"KLN\", \"where\": \"s.v. pycno- (KLN_1966.txt line 31142)\", \"stance\": \"supports\", \"note\": \"'Gk. πυκνός, \\\"close, solid, thick, dense\\\", fr. πύκα, \\\"thickly, solidly\\\" ... which is cogn. with Avestic pusa-, \\\"headband\\\", Alb. puth, \\\"I kiss\\\", prop. \\\"I embrace\\\"' — Klein independently joins Av. pusā- to πυκνός, as Nourai does.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"pusâ; pusâ-ka\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Avestan pusā- f. is real and well attested, but its dictionary gloss is 'Diadem, Stirnband, head-band', not Nourai's expansive 'crown made of bundled twigs and flowers' — that wording is Mo'in's definition of the New Persian descendant بساک, read back onto the Avestan word. Bartholomae's AiW glosses it 'Diadem' throughout the compounds where it occurs (Yt 5.128, the description of Arədvī Sūrā Anāhitā: raθō.karō- 'chariot-box-shaped' pusā-, asta.kaoiδa- 'eight-rayed', zaranyō.pusā- 'wearing a golden diadem', drafšaka.vant- 'adorned with ribbons', anupōiδwant-); Walde-Pokorny II 83 and Mann likewise give 'Diadem'; Wiktionary glosses Avestan 𐬞𐬏𐬯𐬀 'plait, head dress'. The form pusā-ka- is the weaker link: it is NOT attested in Avestan. Gharib sets it up as a reconstruction to explain the Sogdian word — her entry 7435 reads '< Av. pusa-ka-' — i.e. an Old Iranian *pusa-ka-, pusā- plus the common -ka- suffix. So: parent word confirmed, second form reconstructed not attested, gloss embellished.\",\n          \"derivation_fa\": \"واژهٔ اوستایی pusā- (مؤنث) راست و پُرشاهد است، اما معنی فرهنگ‌نویسانهٔ آن «دیهیم، سربند، تاج سر» است نه آنچه نورایی می‌نویسد («تاجی از شاخه‌ها و گل‌های دسته‌شده»)؛ این تعریف در اصل تعریف معین برای واژهٔ فارسی «بساک» است که به واژهٔ اوستایی بازبرده شده. بارتولومه در سراسر ترکیب‌های آن (یشت ۵٫۱۲۸ در وصف اردویسور اناهیتا: zaranyō.pusā- «دارندهٔ دیهیم زرین»، asta.kaoiδa- «هشت‌پَر»، raθō.kara- و …) آن را «Diadem» معنی می‌کند؛ والده–پوکورنی و مان نیز همین را می‌آورند و ویکی‌واژه «plait, head dress». صورت دوم، pusā-ka-، در اوستا شاهد ندارد و برساختی است: قریب در فرهنگ سغدی (شمارهٔ ۷۴۵۳۵ ← ۷۴۳۵) می‌نویسد «< Av. pusa-ka-»، یعنی ایرانی باستان *pusa-ka- با پسوند پرکاربرد -ka-. بنابراین واژهٔ مادر تأیید می‌شود، صورت دوم برساخته است و معنی آراسته‌تر از منابع است؛ ادعا با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%CF%80%CF%85%CE%BA%CE%BD%CF%8C%CF%82\",\n            \"https://en.wiktionary.org/wiki/%D8%A8%D8%B3%D8%A7%DA%A9\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:849\", \"status\": \"partial\", \"note\": \"IEW 849 (puk̑-2) has 'Avestan pusa- f. \\\"headband\\\"' — the simplex only, glossed 'headband'. Pokorny gives no pusā-ka- and no 'bundled twigs and flowers'.\"},\n            {\"ref\": \"SOD:298\", \"status\": \"supports\", \"note\": \"Gharib, Sogdian Dictionary, entry 7435 (the printed page marker '299' follows entry 7436 in SOD.txt, so the entry sits on the p. 298/299 opening Nourai cites): 'ps'k M p(s)sāk (ps'q) © < Av. pusa-ka-; MP pwsg ... garland, crown. Hen. BSOAS 11, 74.14, 15; LW 48; C2, 48V25; GMS 171.' Gharib is the source of the form pusā-ka- and of the whole Avestan > MP > Sogdian line.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch, the pusā- compounds (BRT.txt lines 4499, 6457, 25092, 25949, 27910)\", \"stance\": \"partial\", \"note\": \"'anupōiδwant- ... pusam (\\\"Diadem\\\") .. Yt. 5.128'; 'asta.kaoiδa- \\\"achtteilig\\\": ... pusąm bandayata arədvī sūra anāhita ... \\\"ein Diadem .., ein achtteiliges\\\" Yt. 5.128'; 'zaranyō.pusā- Adj. \\\"mit goldenem Diadem geschmückt\\\"'. Bartholomae's gloss is 'Diadem' only; he has no pusā-ka-.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. 83 (WLD_Bd2_pages.txt line 5485)\", \"stance\": \"partial\", \"note\": \"'wozu vermutlich av. pusā f. \\\"Diadem\\\" (Zubatý KZ. 31, 13, Bthl. Wb. 911 f. zw.; ursprünglich ein pelzbesetzter Turban ...?)' — the word is real, the gloss is 'Diadem', and WLD hangs it on a different root.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann s.v. puk̑- (IEC.txt line 13748)\", \"stance\": \"supports\", \"note\": \"'Av. pusa, f. \\\"diadem\\\"; Per. puse, id.' — Mann puts the Avestan word in this root family, as the chart does.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/بساک, etymology section\", \"stance\": \"supports\", \"note\": \"Cognate list for the family: 'Avestan 𐬞𐬏𐬯𐬀 (pūsa) \\\"plait, head dress\\\"', beside Parthian and Sogdian forms.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"pusag\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Middle Persian pusag 'crown, garland', spelled pwsg (Manichaean 𐫛𐫇𐫘𐫃), is the regular continuation of Old Iranian *pusa-ka-: the -ka- suffix gives MP -ag with the usual voicing of intervocalic -k-, and the Avestan long ā of pusā- is shortened in the unstressed first syllable of the derivative. Gharib cites it inside her Sogdian entry ('MP pwsg'), Wiktionary's Persian entry بساک derives the word 'From Middle Persian 𐫛𐫇𐫘𐫃 (pusag, pūsag, \\\"garland\\\")' with Parthian pusag alongside, and the Old Armenian loan պսակ (psak) 'crown, wreath' — a well-known Parthian/Middle Iranian borrowing — independently guarantees a Middle Iranian *pusāg/pusag with this meaning. MacKenzie's Concise Pahlavi Dictionary happens not to list it (his word for 'crown' is abesar), and Nyberg's glossary has no pusag either, so the Pahlavi form rests on the Manichaean/Parthian attestations and the Armenian and Sogdian evidence.\",\n          \"derivation_fa\": \"فارسی میانهٔ pusag «تاج، تاج گل» با املای pwsg (مانوی 𐫛𐫇𐫘𐫃) دنبالهٔ قانونمند ایرانی باستان *pusa-ka- است: پسوند -ka- در فارسی میانه به -ag بدل می‌شود (واک‌دار شدن k میان‌واکه‌ای) و «ā» کشیدهٔ pusā- اوستایی در هجای بی‌تکیهٔ مشتق کوتاه می‌شود. قریب در مدخل سغدی خود «MP pwsg» را می‌آورد، ویکی‌واژه مدخل «بساک» را از «فارسی میانه pusag/pūsag \\\"تاج گل\\\"» می‌گیرد و در کنار آن pusag پارتی را می‌نهد، و وام‌واژهٔ ارمنی کهن پسک/պսակ «تاج» — که وام‌گیری شناخته‌شده‌ای از ایرانی میانه است — خود گواه مستقلی بر وجود *pusāg/pusag ایرانی میانه با همین معنی است. مکنزی در «فرهنگ کوچک پهلوی» این واژه را نیاورده (واژهٔ او برای «تاج» abesar است) و نیبرگ نیز آن را ندارد؛ پس صورت پهلوی بر پایهٔ شواهد مانوی/پارتی و گواهی ارمنی و سغدی استوار است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A8%D8%B3%D8%A7%DA%A9\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON:779\", \"status\": \"partial\", \"note\": \"Mo'in's six-volume Farhang-e Farsi is not online and the page cannot be mapped (refs_online.json: 'Page numbers cannot be mapped online'; only the 2-vol Adena condensation exists as MON_part1/2.txt, which has no page breaks). In that condensation the relevant headwords بساک (MON_part1.txt line 23305) and پساک (line 31588) are present with the flower-crown definition, but the bracketed etymological tag is illegible in the OCR and abadis.ir's Mo'in text for پساک carries no origin tag at all — so Mo'in's Pahlavi etymon could not be read.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary (grep 'pusag', 'crown')\", \"stance\": \"silent\", \"note\": \"MacKenzie has no pusag; his entry for 'crown' is 'abesar [ʾbysl | M ʾbysr, N afsar]' (PHD_mackenzie.txt lines 772, 6316).\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (grep 'pusak', 'crown')\", \"stance\": \"silent\", \"note\": \"The glossary has pus 'son', pušt 'back', api-sar 'crown', tāg 'crown' (Syriac loan) — no pusag.\"},\n            {\"src\": \"SOD\", \"where\": \"Gharib no. 7435 (SOD.txt line 57722)\", \"stance\": \"supports\", \"note\": \"'p(s)sāk ... © < Av. pusa-ka-; MP pwsg' — Gharib cites the Middle Persian form directly.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/بساک (raw etymology)\", \"stance\": \"supports\", \"note\": \"'From Middle Persian 𐫛𐫇𐫘𐫃 (pusag, pūsag, \\\"garland\\\")', with cognates Parthian 𐫛𐫇𐫘𐫃 (pusag), Sogdian ʾpsʾk, Avestan 𐬞𐬏𐬯𐬀, Old Armenian պսակ, Tocharian B pässakw.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"pasâk «پساک» (extra: بساک)\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The word and its meaning are exactly as the chart gives them. Mo'in: «بساک: تاجی که از گل‌ها و ریاحین و اسپرغم‌ها و برگ مورد می‌ساختند و پادشاهان و بزرگان و دلیران روزهای عید و جشن و مردمان در روز دامادی بر سر می‌گذاشتند», with پساک cross-referenced to it; Dehkhoda the same; Asadi Tusi's Loghat-e Fors has the headword glossed «چون تاجی بود که از اسپرغم‌ها کنند» and quotes precisely the Kasā'i verse Nourai prints. The p-/b- doublet (پساک ~ بساک) is the ordinary Persian orthographic hesitation in old words of this shape. What is less certain is the immediate parent. A direct New Persian descendant of Middle Persian pusag would be expected to show *pusa/pōsa — MP -ag regularly yields NP -a/-e and MP u is not raised to a — whereas پساک/بساک keeps a final -k and has long ā, the shape of the north-eastern forms (Sogdian ʾpsʾk/psāk, Parthian pusāg; compare Old Armenian psak, borrowed from Parthian). Encyclopaedia Iranica's survey of Sogdian loanwords in Persian in fact lists NP pasāk 'garland' as a borrowing from Sogdian (ʾ)psʾk. Wiktionary nonetheless derives بساک from Middle Persian pusag. So the family and the root are certain; the particular arrow 'Pahlavi pusag > Persian pasāk' that Nourai draws is one of two competing accounts, the other making it a Sogdian (or Parthian) loan.\",\n          \"derivation_fa\": \"واژه و معنای آن درست همان است که نمودار می‌آورد. معین: «بساک: تاجی که از گل‌ها و ریاحین و اسپرغم‌ها و برگ مورد می‌ساختند و پادشاهان و بزرگان و دلیران روزهای عید و جشن و مردمان در روز دامادی بر سر می‌گذاشتند»، و «پساک» را به همان ارجاع می‌دهد؛ دهخدا نیز همین. «لغت فرس» اسدی طوسی سرواژه را «چون تاجی بود که از اسپرغم‌ها کنند» معنی می‌کند و همان بیت کسایی را می‌آورد که نورایی نقل کرده است. دوگانگی «پ/ب» در نوشتار واژه‌های کهن فارسی چیز عادی است. اما دربارهٔ پدرِ بی‌واسطهٔ این واژه جای گفت‌وگو هست: اگر «پساک» بازماندهٔ مستقیم pusag فارسی میانه بود، انتظار داشتیم به صورت *پوسه/پوسا درآید، چون -ag پهلوی در فارسی نو به -ه بدل می‌شود و «و» به «a» نمی‌گراید؛ حال آنکه این واژه «ک» پایانی و «آ» کشیده دارد، یعنی درست شکل صورت‌های شمال‌شرقی (سغدی ʾpsʾk/psāk، پارتی pusāg؛ قس ارمنی کهن psak که وام از پارتی است). دانشنامهٔ ایرانیکا در بررسی وام‌واژه‌های سغدی در فارسی، pasāk «تاج گل» را وام‌واژه‌ای سغدی می‌شمارد؛ ویکی‌واژه اما آن را از pusag فارسی میانه می‌گیرد. پس خانواده و ریشه قطعی است ولی پیکانِ «پهلوی ← فارسی» یکی از دو تبیین رقیب است؛ با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A8%D8%B3%D8%A7%DA%A9\",\n            \"https://abadis.ir/fatofa/%D9%BE%D8%B3%D8%A7%DA%A9/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON:779\", \"status\": \"supports\", \"note\": \"Content confirmed, page not mappable (see node 2). MON_part1.txt line 23305: «بساک: تاجی که از گل‌ها و ریاحین و اسپرغم‌ها و برگ مورد می‌ساختند و پادشاهان و بزرگان و دلیران روزهای عید و جشن و مردمان در روز دامادی بر سر می‌گذاشتند»; line 31588: «پساک: ... تاجی که از گل‌ها و ریاحین با اسپرغم‌ها ساختندی و پادشاهان و ...». abadis.ir's Mo'in text: «(پَ) (اِ.) = بساک: تاجی که از انواع گل ها درست می کردند و پادشاهان».\"},\n            {\"ref\": \"FRS:146\", \"status\": \"supports\", \"note\": \"Asadi Tusi, Loghat-e Fors — in the Eqbal 1319 edition on disk the entry stands on printed p. 93 (FRS_pages.txt leaf 274): the headword is glossed «چون تاجی بود که از اسپرغم‌ها کنند» and quoted with Kasā'i's line «چگونه نیکی تاج و بساک ملوک — باز یکی کوفتهٔ آسیاست», i.e. exactly the verse and poet Nourai prints. The footnote records the manuscript variants «بسا / بساک / پساک تاجی باشد که از اسپرغم بندند». The page number differs because Nourai cites the Kharazmi 1365 edition (refs_online.json: 'Pagination differs ... verify the entry, not the page').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt lines 23305 (بساک) and 31588 (پساک)\", \"stance\": \"supports\", \"note\": \"Both spellings present with the flower-crown definition; no Pahlavi etymon legible in this OCR or in the online Mo'in text.\"},\n            {\"src\": \"FRS\", \"where\": \"Loghat-e Fors, printed p. 93 (FRS_pages.txt leaf 274)\", \"stance\": \"supports\", \"note\": \"Kasā'i's verse with بساک 'flower crown' — the oldest lexicographic attestation, and Nourai's own quotation.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' vol. 1 (grep بساک/پساک over BQT_v1_pages.txt)\", \"stance\": \"silent\", \"note\": \"Neither بساک nor پساک appears anywhere in the OCR of Borhan vol. 1.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/بساک\", \"stance\": \"supports\", \"note\": \"'From Middle Persian pusag \\\"garland\\\"'; senses 'wreath, garland' and (botanical) 'anther' — the latter is Mo'in's second sense «برجستگی دکمه‌مانند انتهای میلهٔ پرچم گل».\"},\n            {\"src\": \"Encyclopaedia Iranica\", \"where\": \"'SOGDIAN LANGUAGE ii. Loanwords in Persian' (fetch blocked, 403; seen only in search summary)\", \"stance\": \"partial\", \"note\": \"The article is reported to list NP pasāk 'garland' as a loan from Sogdian (ʾ)psʾk. The page itself could not be fetched (HTTP 403), so this is recorded as a lead, not as a citation.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Sogdian\",\n          \"words\": \"ps`k\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sogdian psʾk (Manichaean script), read psāk/(ʾ)psāk, 'garland, crown'. Gharib's dictionary derives it precisely as the chart does, from the -ka- derivative of the Avestan word: 'ps'k M p(s)sāk (ps'q) < Av. pusa-ka-; MP pwsg ... garland, crown', with references to Henning BSOAS 11, 74, and Gershevitch GMS §171. The Sogdian form shows the regular north-east Iranian syncope of the unstressed first-syllable vowel (*pusāka- > psāk) and retention of the final -k that Middle Persian had voiced to -g. The word travelled on: Old Uyghur psuk and Tocharian B pässakw are borrowings from Sogdian, and Old Armenian պսակ from the Parthian/Middle Iranian cognate.\",\n          \"derivation_fa\": \"واژهٔ سغدی psʾk (خط مانوی) خوانده psāk/(ʾ)psāk به معنی «تاج گل، تاج» است. بدرالزمان قریب در فرهنگ سغدی دقیقاً همان زنجیره‌ای را می‌دهد که نمودار نشان می‌دهد: «ps'k ... < Av. pusa-ka-؛ MP pwsg ... garland, crown» با ارجاع به هنینگ (BSOAS ۱۱، ۷۴) و گرشویچ (دستور سغدی مانوی، بند ۱۷۱). صورت سغدی افتادن قانونمند واکهٔ بی‌تکیهٔ هجای نخست را در ایرانی شمال‌شرقی نشان می‌دهد (*pusāka- ← psāk) و «ک» پایانی را نگه داشته، حال آنکه فارسی میانه آن را به «گ» واک‌دار کرده است. این واژه از سغدی به اویغوری کهن (psuk) و تخاری ب (pässakw) و از همتای پارتی‌اش به ارمنی کهن (պսակ) وام رفته است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A8%D8%B3%D8%A7%DA%A9\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"SOD:298\", \"status\": \"supports\", \"note\": \"Gharib, Sogdian-Persian-English Dictionary, entry 7435 (SOD.txt line 57722; the printed page number '299' appears just after entry 7436, so the entry lies on the 298/299 opening): 'ps'k M / p(s)sak (ps'q) © < Av. pusa-ka-; MP pwsg / garland, crown / Hen. BSOAS 11, 74.14, 15; LW 48; C2, 48V25; GMS 171'. Note that Gharib's numbering is by entry, not page — Nourai's '298' matches the printed page, and the gloss is 'garland, crown', exactly the chart's.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SOD\", \"where\": \"entries 7435, 7436 and the homograph 2845 (SOD.txt lines 57722, 26393)\", \"stance\": \"supports\", \"note\": \"Entry 7435 is the crown-word; the Buddhist-Sogdian homograph 2845 'ps'k f(o)sak? \\\"bearing, subjection\\\"' is a different word, so the reading psāk 'garland' must be taken from the Manichaean entry, as Gharib does.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/بساک, cognates\", \"stance\": \"supports\", \"note\": \"Lists 'Sogdian ʾpsʾk' as cognate with Middle Persian/Parthian pusag, alongside Old Uyghur psuk and Tocharian B pässakw.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Greek\",\n          \"words\": \"puknos\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Greek πυκνός (Nourai's 'puknos' is his usual u-for-υ transliteration) 'close, solid, thick, dense; sagacious'. The older, epic form is πυκινός, from the root plus the -ino- suffix: Watkins 'Suffixed form *puk-ino- in Greek pukinos, later puknos, strong, fast, thick', with syncope of the unstressed middle vowel giving Attic πυκνός. Pokorny 849 sets it beside the adverb πύκα 'tight, firm, dense' and the compositional form πυκι- (πυκι-μήδης 'sensible'), with the denominative πυκάζω 'make tight, wrap densely'. The semantic link to the Iranian 'diadem/head-band' words is 'pressed/bound tightly together'.\",\n          \"derivation_fa\": \"واژهٔ یونانی πυκνός (که نورایی به شیوهٔ همیشگی خود «puknos» می‌نویسد، با u برای υ) به معنی «انبوه، فشرده، ستبر، سفت» و نیز «هوشمند» است. صورت کهن‌تر و حماسی آن πυκινός است، یعنی ریشه به‌علاوهٔ پسوند -ino-؛ واتکینز می‌نویسد «صورت پسونددار *puk-ino- در یونانی pukinos و سپس puknos»، با افتادن واکهٔ بی‌تکیهٔ میانی که صورت آتیک πυκνός را می‌دهد. پوکورنی (ص ۸۴۹) آن را کنار قید πύκα «سفت، انبوه» و صورت ترکیبی πυκι- (πυκι-μήδης «خردمند») و فعل πυκάζω «سفت بستن، انبوه پوشاندن» می‌نهد. پیوند معنایی با واژه‌های ایرانی «دیهیم/سربند» همان مفهوم «به‌هم فشرده، تنگ بسته» است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%CF%80%CF%85%CE%BA%CE%BD%CF%8C%CF%82\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985: 'puk-1. To make fast. Suffixed form *puk-ino- in Greek pukinos, later puknos, strong, fast, thick: PYKNIC; PYCNIDIUM, PYCNOMETER. [Pok. 2. puk- 849.]' (AHD_watkins1985.txt line 876).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 849 s.v. puk̑-2\", \"stance\": \"supports\", \"note\": \"'Adverb. πύκα \\\"tight, firm, dense, sensible, wise\\\", in compound πυκι- (πυκι-μήδης \\\"sensible, wise\\\"), out of it πυκινός newer πυκνός \\\"dense, tight, firm, proficient\\\", πυκάζω \\\"make tight, firm, wrap dense\\\".'\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. 82 (WLD_Bd2_pages.txt line 5471 ff.)\", \"stance\": \"supports\", \"note\": \"'Gr. πυκνός \\\"fest, dicht, derb, tüchtig, solid\\\", Zsform πυκι- in πυκι-μήδης \\\"verständig\\\" ..., von wo aus πυκινός ... πύκα Adv. \\\"fest, dicht\\\" ... πυκάζω \\\"mache fest oder dicht, dränge zs.\\\"'\"},\n            {\"src\": \"IEC\", \"where\": \"Mann s.v. puk̑- (IEC.txt line 13748)\", \"stance\": \"supports\", \"note\": \"'Gk. cf. púka, adv. \\\"close-fitting\\\"; puknós, pukinós, adj. \\\"compact\\\"'.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/πυκνός\", \"stance\": \"supports\", \"note\": \"'Possibly from PIE *puḱ- \\\"press together\\\"; cognates Avestan pusā \\\"headband, diadem\\\", Albanian putë. Poetic form πυκινός.'\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"pycnometer\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"A 19th-c. scientific compound, not an inherited word: Greek πυκνο- (combining form of πυκνός 'dense') + μέτρον 'measure', hence 'density-measurer' — an instrument, usually a calibrated flask, for determining the density of a liquid or solid. Klein: 'pycno-, before a vowel pycn-, combining form meaning \\\"close, thick, dense\\\", as in pycnometer. — Gk. πυκνο-, πυκν-, fr. πυκνός'; 'pycnometer, n., an instrument for measuring the density of liquids or solids. — Compounded of pycno- and Gk. μέτρον, \\\"measure\\\"'. Watkins lists PYCNOMETER (misprinted 'PYCNOMTER' in the 1985 text) among the English derivatives of puk-1, together with PYKNIC and PYCNIDIUM. So Nourai's arrow Greek puknos > English pycnometer is right in substance, with the usual proviso that the coinage is modern and learned.\",\n          \"derivation_fa\": \"«pycnometer» واژه‌ای ساختهٔ سدهٔ نوزدهم در زبان علم است، نه واژه‌ای میراثی: از صورت ترکیبی یونانی πυκνο- («انبوه، چگال») به‌علاوهٔ μέτρον «اندازه»، یعنی «چگالی‌سنج» — ابزاری (معمولاً بطری مدرج) برای سنجش چگالی مایع یا جامد. کلاین می‌نویسد «pycno-، پیش از واکه pycn-، صورت ترکیبی به معنی \\\"نزدیک، ستبر، چگال\\\" چنانکه در pycnometer؛ از یونانی πυκνός» و «pycnometer: ساخته از pycno- و μέτρον یونانی». واتکینز نیز PYCNOMETER را در کنار PYKNIC و PYCNIDIUM در شمار مشتق‌های انگلیسی ریشهٔ puk-1 می‌آورد. پس پیکان «یونانی puknos ← انگلیسی pycnometer» در اصل درست است، با این یادآوری که واژه ساختی نوین و دانشورانه است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%CF%80%CF%85%CE%BA%CE%BD%CF%8C%CF%82\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. puk-1 lists 'PYKNIC; PYCNIDIUM, PYCNOMTER' [sic, for PYCNOMETER] (AHD_watkins1985.txt line 876), and the English index has 'PYCNOMTER puk-1' (line 2144).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. pycno- / pycnometer (KLN_1966.txt lines 31141-31143)\", \"stance\": \"supports\", \"note\": \"'pycno- ... combining form meaning \\\"close, thick, dense\\\", as in pycnometer. — Gk. πυκνο-, πυκν-, fr. πυκνός, \\\"close, solid, thick, dense\\\" ... cogn. with Avestic pusa-, \\\"headband\\\"'; 'pycnometer, n., an instrument for measuring the density of liquids or solids. — Compounded of pycno- and Gk. μέτρον, \\\"measure\\\".'\"},\n            {\"src\": \"POK\", \"where\": \"IEW 849 s.v. puk̑-2\", \"stance\": \"supports\", \"note\": \"Supplies the Greek base πυκνός from which the modern compound is formed; Pokorny of course has no modern English derivatives.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Greek\",\n          \"words\": \"am-pus\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"There is no Greek word *ampus. The word meant is ἄμπυξ (ámpyx), gen. ἄμπυκος — 'a woman's diadem, frontlet; a horse's headband; the rim of a wheel' — which is precisely the form Pokorny prints on the cited page: 'gr. ἄμπυξ m. \\\"headband\\\"' (IEW 849, s.v. puk̑-2), and which Mann gives as 'ám-pux, gs: -pukos, m & f \\\"chaplet\\\"'. The final consonant is the velar of the root *puk̑- + -s of the nominative, written ξ; Nourai's 'am-pus' drops the velar, i.e. it transliterates ξ as plain s. The 300 dpi render of PDF p. 408 shows 'am-pus : headband' in the printed box, so this is the book's own error and the JSON extraction is faithful. The morphology Nourai implies is the standard one — a root noun with the prefix ἀμ- (ἀμφί 'around'), so 'that which goes round (the head)' — but note that Beekes rejects the connection and treats ἄμπυξ as Pre-Greek, on the ground that 'the notion \\\"thick, solid\\\" does not seem to fit the objects in question'; Wiktionary records both views. Word real, chain traditional, form as printed wrong.\",\n          \"derivation_fa\": \"واژه‌ای به صورت *ampus در یونانی وجود ندارد؛ آنچه مراد است ἄμπυξ (ámpyx، اضافی ἄμπυκος) است به معنی «دیهیم زنانه، سربند، پیشانی‌بند اسب، طوقهٔ چرخ» — و درست همین صورت است که پوکورنی در همان صفحهٔ ۸۴۹ ذیل puk̑-2 چاپ کرده («gr. ἄμπυξ m. \\\"Stirnband\\\"») و مان نیز «ám-pux, gs: -pukos» می‌آورد. همخوان پایانی، کامی ریشهٔ *puk̑- به‌علاوهٔ -s نشانهٔ فاعلی است که با «ξ» نوشته می‌شود؛ «am-pus» نورایی این کامی را انداخته و ξ را «s» ساده نویسانده است. تصویر ۳۰۰ نقطه‌ای صفحهٔ ۴۰۸ نشان می‌دهد که خودِ کتاب «am-pus : headband» چاپ کرده، پس خطای چاپی کتاب است نه خطای خوانش اسکن. ساخت واژه نیز همان تحلیل سنتی است (اسم ریشه‌ای با پیشوند ἀμ- از ἀμφί «پیرامون»)، ولی بیکس این پیوند را نمی‌پذیرد و ἄμπυξ را واژه‌ای پیشایونانی می‌داند، چون معنی «ستبر، فشرده» با این اشیاء جور درنمی‌آید؛ ویکی‌واژه هر دو دیدگاه را ثبت کرده است.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"am-pus\",\n          \"correct_form\": \"ἄμπυξ / ám-pyx (gen. ἄμπυκος)\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%E1%BC%84%CE%BC%CF%80%CF%85%CE%BE\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:849\", \"status\": \"partial\", \"note\": \"IEW 849 s.v. puk̑-2 does have the word on the cited page and with the cited meaning — 'gr. ἄμπυξ m. \\\"headband\\\"' (POK_full.txt, OCR 'gr. a|j-nu^ m. \\\" headband \\\"') — but the form is ἄμπυξ, not 'am-pus'. Reference supports the derivation, contradicts the spelling.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"IEC\", \"where\": \"Mann s.v. puk̑- (IEC.txt line 13748)\", \"stance\": \"partial\", \"note\": \"'cf. ám-pux, gs: -pukos, m & f \\\"chaplet\\\", fr. ámbh-; (late Gk. also \\\"tyre\\\")' — Mann's hyphenated ám-pux is evidently the shape Nourai was copying, with the final -x lost.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/ἄμπυξ\", \"stance\": \"partial\", \"note\": \"'a woman's diadem; frontlet / a horse's headband / the rim of a wheel'; gen. ἄμπυκος. Traditional view: 'a root noun prefixed with ἀμ-, belonging to πύκα \\\"solidly\\\" and πυκνός \\\"compact\\\"', with Avestan pusā 'headband, diadem'; but 'the notion \\\"thick, solid\\\" does not seem to fit the objects in question', so Beekes takes it as a Pre-Greek borrowing with a typical Pre-Greek suffix.\"},\n            {\"src\": \"BOOK\", \"where\": \"PDF p. 408, lowest Greek box (data/verification/sources/refs/ocr/BOOK/408.png)\", \"stance\": \"supports\", \"note\": \"The render shows 'Greek | POK:849' / 'am-pus : headband' — the extraction is faithful; the misprint is the book's.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-408.json > /dev/null && echo \"JSON OK\"",
 "description": "Write verification JSON for page 408"
}
```


### [2026-09-14T01:15:07.045Z] TOOL RESULT

```
JSON OK
```


## [2026-09-14T01:15:11.108Z] TOOL CALL #96: Bash

```json
{
 "command": "python3 tools/verify_check.py 408",
 "description": "Run verify_check for page 408"
}
```


### [2026-09-14T01:15:12.307Z] TOOL RESULT

```
nodes verified: 15/15
node verdicts: {'plausible': 3, 'confirmed': 9, 'disputed': 1, 'transcription_suspect': 2}
root verdicts: {'confirmed': 3}
ref checks: {'partial': 9, 'supports': 12, 'not_checked': 1}
books consulted: {'supports': 36, 'partial': 9, 'silent': 4, 'contradicts': 3} | by book: {'Wiktionary': 7, 'IEC': 5, 'WLD': 5, 'KLN': 4, 'ARY': 3, 'POK': 3, 'CHEUNG': 3, 'PHD': 3, 'Etymonline': 2, 'BRT': 2, 'NYB': 2, 'BOOK': 2, 'SOD': 2, 'HUB': 1, 'LAT': 1, 'AHD': 1, 'BLY': 1, 'HRN': 1, 'MON': 1, 'FRS': 1, 'BQT': 1, 'Encyclopaedia Iranica': 1}
```


## [2026-09-14T01:15:27.950Z] AGENT

Done. `python3 tools/verify_check.py 408` reports 0 PROBLEM lines.

**Page 408 (book p. 378) — 3 entries (2 redirects skipped: Pu 3 → Apo, Pug → Peuk), 15 nodes**

- Root verdicts: 3 confirmed (Pu 2 = Pok. pū̆-1 847; Pŭ 4/Peua = Pok. pū̆-2 : peuə- 848-849; Puk = Pok. puk̑-2 849).
- Node verdicts: 9 confirmed, 3 plausible, 1 disputed, 2 transcription_suspect.
- ref_check: 12 supports, 9 partial, 1 not_checked. consulted: 36 supports, 9 partial, 4 silent, 3 contradicts.

Disputed / transcription_suspect:
- **Pu 2, English "pus"** (disputed) — pustule is right, but *pus* is not from Latin `pustula`; L. pūs belongs to the *rot* root (Nourai's own Pŭ 4). Watkins pū-2 §5a, Klein s.v. pus, Etymonline all put it there.
- **Pŭ 4, Germanic "fŭ-faz"** (transcription_suspect, error_in: book) — impossible form; Watkins/Klein/WLD have Gmc. **\*fūlaz* (< *pū-lo-*, whence Goth. fūls, OE fūl). The printed page shows `fŭ-faz`, so the extraction is faithful.
- **Puk, Greek "am-pus"** (transcription_suspect, error_in: book) — the word is ἄμπυξ / ámpyx (gen. ἄμπυκος), as Pokorny 849 and Mann print it; the book drops the final velar. Printed page confirms `am-pus`.

Plausible (noted, not errors): Persian پوک — Pokorny/Horn/Hübschmann have pūk but glossed "blowing, bellows", not "empty"; Avestan `pusā-ka` is unattested (Gharib's reconstruction) and pusā- means simply "diadem"; Persian پساک/بساک may be a Sogdian/Parthian loan rather than a direct descendant of MP pusag (shape -āk, final -k).

**No extraction errors found** — the JSON matches the printed page everywhere I checked. Page image saved to `data/verification/sources/refs/ocr/BOOK/408.png`; 9 web sources archived via `fetch_source.py`. Bonus: the chart's NOTE about the Ferdowsi couplet and the cross of Jesus is confirmed by Noushin, *Farhang-e Shahnameh* p. 151 s.v. پوده.
