# Verification process log — verify-page-380


## [2026-09-07T20:35:22.012Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 380 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-380.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-380.json. Write /home/sfmqrb/git/rishe/data/verification/page-380.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 380` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T20:35:24.474Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T20:35:25.184Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T20:35:25.201Z] TOOL RESULT

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


## [2026-09-07T20:35:25.809Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-380.txt"
}
```


### [2026-09-07T20:35:25.830Z] TOOL RESULT

```
1	=== PDF page 380 (book page 350) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Pa, Pa-ter, Poti, Potiš : Pa: to protect, to feed. Pa-ter: protector, feeder (of the family), father ☞ Ter 3. Poti, Potiš: protector, husband, power, also self. This has probably started as a nursery word and became a usual term in the Indo-European languages. Compare with the root "Baba".  (refs POK:787,842; SYN:103; KAS:10)  PART 2
4	#1 (parent #0) [Pahlavi] refs=BQT:202 | pâp, Pâpak : father. Suffix -k indicates respect and love. | NOTE: BQT claims these are cognates with Latin "papa" but does not give details.
5	  #2 (parent #1) [Persian] refs=BQT:202; HRN:34; NYB:150; MON:428; AEF:197 | bâb 1 «باب ۱» : father | extra: بابا، بابو، بابک، بابکان | NOTE: The words "bâb" and "bâbŭ" as a title of respect may be from a different root and mixed up with "bâbâ:father" See root "Baba".
6	#3 (parent #0) [Germanic] refs=AHD | fôd : food ; fadar : feeder, father
7	  #4 (parent #3) [English] refs=AHD; DVS:142 | food, feed, fur ; father, pattern
8	#5 (parent #0) [Latin] refs=POK:847; AHD | potere (potis) : to be able ; pâscere : to feed ; pater : feeder, father
9	  #6 (parent #5) [English] refs=AHD; DVS:142 | potent, potential, power, possible, possess ; pasture, pantry, company ; paternal, patronage
10	#7 (parent #0) [Greek] refs=AHD | pater, pappas
11	  #8 (parent #7) [English] refs=AHD; DVS:142 | patriot, Pope, papa
12	--- entry 1 ---
13	ROOT Pag -> redirect to Pak
14	--- entry 2 ---
15	ROOT Pais -> redirect to Pis
16	--- entry 3 ---
17	ROOT Paita -> redirect to Pele
18	--- entry 4 ---
19	ROOT [Indo-European] Pak, Pag : to fasten  (refs POK:787)
20	#1 (parent #0) [Avestan] refs=POK:787; KLN:1110 | pas : to tie, fetter
21	#2 (parent #0) [Latin] refs=KLN; AHD | pangere : to fasten ; pacîcî : to agree ; pâlus : stick, pole ; pâgus : boundary staked out on ground ; prô-pâgĕs : offspring
22	  #3 (parent #2) [English] refs=AHD | pact, compact ; peace, pace, Pacific, pacify ; pole, palette ; peasant ; propagate
23	
```


## [2026-09-07T20:35:27.596Z] AGENT

I'll read the source JSON and the reference infrastructure.


## [2026-09-07T20:35:29.717Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-380.json'))\nprint(json.dumps(d,ensure_ascii=False,indent=1)[:8000])\n\"",
 "description": "Read page 380 source JSON"
}
```


### [2026-09-07T20:35:31.029Z] TOOL RESULT

```
{
 "pdf_page": 380,
 "book_page": 350,
 "entries": [
  {
   "root": {
    "name": "Pa, Pa-ter, Poti, Potiš",
    "lang": "Indo-European",
    "refs": "POK:787,842; SYN:103; KAS:10",
    "gloss": "Pa: to protect, to feed. Pa-ter: protector, feeder (of the family), father ☞ Ter 3. Poti, Potiš: protector, husband, power, also self. This has probably started as a nursery word and became a usual term in the Indo-European languages. Compare with the root \"Baba\"."
   },
   "part": 2,
   "nodes": [
    {
     "id": 1,
     "parent": 0,
     "lang": "Pahlavi",
     "refs": "BQT:202",
     "words": [
      {
       "translit": "pâp, Pâpak",
       "gloss": "father. Suffix -k indicates respect and love.",
       "script": null
      }
     ],
     "script_extra": null,
     "note": "BQT claims these are cognates with Latin \"papa\" but does not give details.",
     "quote": null
    },
    {
     "id": 2,
     "parent": 1,
     "lang": "Persian",
     "refs": "BQT:202; HRN:34; NYB:150; MON:428; AEF:197",
     "words": [
      {
       "translit": "bâb 1",
       "gloss": "father",
       "script": "باب ۱"
      }
     ],
     "script_extra": "بابا، بابو، بابک، بابکان",
     "note": "The words \"bâb\" and \"bâbŭ\" as a title of respect may be from a different root and mixed up with \"bâbâ:father\" See root \"Baba\".",
     "quote": {
      "text": "سدیگر بپرسیدش افراسیاب - ازایران و از شهر و از مام و باب",
      "poet": "Ferdowsî"
     }
    },
    {
     "id": 3,
     "parent": 0,
     "lang": "Germanic",
     "refs": "AHD",
     "words": [
      {
       "translit": "fôd",
       "gloss": "food",
       "script": null
      },
      {
       "translit": "fadar",
       "gloss": "feeder, father",
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 4,
     "parent": 3,
     "lang": "English",
     "refs": "AHD; DVS:142",
     "words": [
      {
       "translit": "food, feed, fur",
       "gloss": null,
       "script": null
      },
      {
       "translit": "father, pattern",
       "gloss": null,
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 5,
     "parent": 0,
     "lang": "Latin",
     "refs": "POK:847; AHD",
     "words": [
      {
       "translit": "potere (potis)",
       "gloss": "to be able",
       "script": null
      },
      {
       "translit": "pâscere",
       "gloss": "to feed",
       "script": null
      },
      {
       "translit": "pater",
       "gloss": "feeder, father",
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
     "lang": "English",
     "refs": "AHD; DVS:142",
     "words": [
      {
       "translit": "potent, potential, power, possible, possess",
       "gloss": null,
       "script": null
      },
      {
       "translit": "pasture, pantry, company",
       "gloss": null,
       "script": null
      },
      {
       "translit": "paternal, patronage",
       "gloss": null,
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 7,
     "parent": 0,
     "lang": "Greek",
     "refs": "AHD",
     "words": [
      {
       "translit": "pater, pappas",
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
     "parent": 7,
     "lang": "English",
     "refs": "AHD; DVS:142",
     "words": [
      {
       "translit": "patriot, Pope, papa",
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
    "name": "Pag",
    "redirect": "Pak"
   },
   "nodes": []
  },
  {
   "root": {
    "name": "Pais",
    "redirect": "Pis"
   },
   "nodes": []
  },
  {
   "root": {
    "name": "Paita",
    "redirect": "Pele"
   },
   "nodes": []
  },
  {
   "root": {
    "name": "Pak, Pag",
    "lang": "Indo-European",
    "refs": "POK:787",
    "gloss": "to fasten"
   },
   "nodes": [
    {
     "id": 1,
     "parent": 0,
     "lang": "Avestan",
     "refs": "POK:787; KLN:1110",
     "words": [
      {
       "translit": "pas",
       "gloss": "to tie, fetter",
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 2,
     "parent": 0,
     "lang": "Latin",
     "refs": "KLN; AHD",
     "words": [
      {
       "translit": "pangere",
       "gloss": "to fasten",
       "script": null
      },
      {
       "translit": "pacîcî",
       "gloss": "to agree",
       "script": null
      },
      {
       "translit": "pâlus",
       "gloss": "stick, pole",
       "script": null
      },
      {
       "translit": "pâgus",
       "gloss": "boundary staked out on ground",
       "script": null
      },
      {
       "translit": "prô-pâgĕs",
       "gloss": "offspring",
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
     "lang": "English",
     "refs": "AHD",
     "words": [
      {
       "translit": "pact, compact",
       "gloss": null,
       "script": null
      },
      {
       "translit": "peace, pace, Pacific, pacify",
       "gloss": null,
       "script": null
      },
      {
       "translit": "pole, palette",
       "gloss": null,
       "script": null
      },
      {
       "translit": "peasant",
       "gloss": null,
       "script": null
      },
      {
       "translit": "propagate",
       "gloss": null,
       "script": null
      }
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


## [2026-09-07T20:35:31.394Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','SYN','KAS','BQT','HRN','NYB','MON','AEF','AHD','DVS','KLN','WLD','IEC','PHD','BRT','ARY','SKT','WEB','FSD','HUB','CHEUNG']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400] if v else 'MISSING')\n\"",
 "description": "Check refs_online for needed abbreviations"
}
```


### [2026-09-07T20:35:32.865Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
KAS {"title": "M.A. Hasani Da'i al-Eslam, Khod-amuz-e Zaban-e Sanskrit, Danesh 1361/1982", "kind": "website", "url": "https://ketabnak.com/book/108067 (131 pp. PDF, login)", "lookup_hint": "Not on archive.org.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "PDF page exists; not fetched."}
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
DVS {"title": "P. Davies, Roots: Family Histories of Familiar Words, McGraw-Hill 1981", "edition_found": "1981 (lending-only)", "kind": "archive_restricted", "url": "https://archive.org/details/rootsfamilyhisto0000davi (lending)", "identifier": "rootsfamilyhisto0000davi", "local_file": null, "page_offset": null, "lookup_hint": "Borrow via IA lending; in-book search ?q=<word>.", "notes": "RE-SEARCH 202
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
CHEUNG MISSING
```


## [2026-09-07T20:35:37.421Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n 1,120p data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-07T20:35:37.462Z] TOOL RESULT

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


## [2026-09-07T20:35:39.066Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','SYN','BQT','HRN','NYB','MON','AHD','KLN','WLD','IEC','PHD','BRT','ARY','SKT','HUB']:\n    v=d[k]\n    print('===',k)\n    for f in ['kind','local_file','page_offset','lookup_hint','scans','url']:\n        if v.get(f): print('  ',f,':',str(v[f])[:300])\n\""
}
```


### [2026-09-07T20:35:40.366Z] TOOL RESULT

```
=== POK
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt
   page_offset : POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' giv
   url : https://archive.org/details/indogermanisches01pokouoft
=== SYN
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt
   page_offset : leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
   url : https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca
=== BQT
   kind : archive_djvu+local_scan_ocr
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/re
   page_offset : vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vo
   lookup_hint : grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d
   scans : [{'volume': '3', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'o
   url : https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indi
=== HRN
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt
   page_offset : leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
   url : https://archive.org/details/grundrissderneu00horngoog
=== NYB
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt
   page_offset : Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.
   url : https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg
=== MON
   kind : website+archive_djvu
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/in
   lookup_hint : Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe
   url : https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)
=== AHD
   kind : archive_djvu+website+archive_restricted
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt
   page_offset : 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
   lookup_hint : Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru
   url : https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only
=== KLN
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt
   page_offset : KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/detai
   lookup_hint : Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
   url : https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein
=== WLD
   kind : archive_djvu
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verificat
   page_offset : Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.tx
   lookup_hint : Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.
   url : https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 
=== IEC
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt
   page_offset : TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
   url : https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987
=== PHD
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt
   page_offset : leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).
   url : https://archive.org/details/a-concise-pahlavi-dictionary
=== BRT
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt
   page_offset : Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th 
   lookup_hint : Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
   url : https://archive.org/details/altiranischeswr00bartgoog
=== ARY
   kind : local_scan_ocr
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt']
   page_offset : printed page = pdf page + 1
   lookup_hint : Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY
   scans : [{'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf', 'first_printed': 1, 'last_printed': 546, 'pdf_offset': -1, 'lang': 'fas+eng', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.tx
=== SKT
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt
   page_offset : leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
   url : https://archive.org/details/aconciseetymolo01skeagoog
=== HUB
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt
   page_offset : leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
   url : https://archive.org/details/persischestudie00hbgoog
```


## [2026-09-07T20:35:47.114Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"lemma: p\" POK_full.txt | head -80"
}
```


### [2026-09-07T20:35:47.166Z] TOOL RESULT

```
6181:/ lemma: ped-2, p6d-\ (foot, *genitalia). 
13541:peu-1, peua-. pu-\ "to clean, sift' , Root/ lemma: peu-2'. "to research, to understand' (see 
16193:Common Armenian Celtic (often alb.) initial pi- > A, see Root/ lemma: plab-\ to babble, 
16935:deesse : Portuguese deusa ' goddess '. [see Root / lemma: per-2\ to go over; over]. 
32748:Root/ lemma: p'^eA/i? (Germanic) and p'^eZ-d'^d (Slavic) 
33470:It is a compound of Root/ lemma: ghosti-s\ stranger; guest + Root/ lemma: poti-s: 
37014:eater)' derived Root/ lemma: ghers-, gher-\ "rigid, *pig' > Root/ lemma: portto-s\ pig' : 
55379:It seems that from Root / lemma: plab-\ (to babble, etc..) derived Root/ lemma: lep-1\ 
63201:Root / lemma: psi-s {*he- psi-s) 
63215:Root / lemma: psi- {*he- psi-) 
64667:Root / lemma: pando-s 
64683:Root / lemma: pank-, pang- 
64711:Root / lemma: pap(p)a 
64733:Root / lemma: parika 
64747:Root / lemma: pasto- 
64761:Root / lemma: paus- 
64779:Root / lemma: paR- and pag- 
64845:Root / lemma: pan- 
64861:Root / lemma: par- 
64875:Root / lemma: paso-s 
64889:Root / lemma: pauson- : puson- 
64909:Root / lemma: pa- : pa- and pa-t- : pa-t- 
65001:Root / lemma: peig-1 and peik- 
65051:Root / lemma: pe/g-1 and peiR- 
65096:Root / lemma: pei-m(i)- 
65114:Root / lemma: peisk-, pisk- 
65176:Root / lemma: peis-2, speis- 
65199:Root / lemma: pej(9)-, pi- 
65451:Root / lemma: peR-1, peR-, poR- 
65469:Root / lemma: peR-2 
65506:Root / lemma: pe/T'- {*k"'ek"'hd) 
65584:Root / lemma: pe/a- pla- 
65653:Root / lemma: peli-s- pel-s- 
65673:Root / lemma: peIR- : polR- 
65707:Root / lemma: pel-1, pela-, ple- 
65713:Root/ lemma: pel-1, pels-, ple-\ full, to fill; to pour; town (?), derived from a prefixed pe- + 
65870:Root / lemma: pel-2a, pelQ- : pla- 
65905:Root / lemma: pel-2b, pel-en-, pel-t-, pel-u- 
65944:Root / lemma: pel-3a 
65980:Root / lemma: pel-3b, pela- ple- 
66018:Root / lemma: pe/~4 
66037:Root / lemma: pel-5 
66056:Root / lemma: pel-6 
66144:Root / lemma: pelpo- or polpo- 
66156:Root / lemma: penk^e 
66195:Root / lemma: pen-1 
66217:Root / lemma: pen-2, pen-ko- 
66250:Root / lemma: pent- 
66301:Root / lemma: perd- 
66318:Root / lemma: perg-1 
66324:Root/ lemma: perg-1 \ "pole; trunk' derived from lllyrian : Baltic : Slavic prefix pre- + ga 
66353:Root / lemma: perg-2 
66371:Root / lemma: perk-1, prek- 
66379:Root/ lemma: perk-1, prek-\ to fill, derived from Root/ lemma: *(s)p(h)ereg-, (s)p(h)erag-, 
66418:Root / lemma: pertt-1 
66436:Root / lemma: perti-2, preR- 
66468:Root / lemma: perR-3, pfR- 
66490:Root / lemma: perti-4, preR-, pfR- 
66530:Root / lemma: pericu-s 
66537:the oldest IE cognate, hence Root/ lemma: pertcu-s'. oak derived from an earlier Root 
66569:Root / lemma: per-1, pera- : pre-, preu- 
66577:Root / lemma: per-1, pere- : pre-, preu- : to drizzle, sprinkle, jet, derived from Root / 
66631:Root / lemma: per-2 
66947:Root / lemma: per-2. B. per-, pera- 
67039:Root / lemma: per-2: C. per-, pera- 
67071:Root / lemma: per-2. D. per- 
67102:Root / lemma: per-2. E. per- 
67128:Root / lemma: per-3, per-g- 
67172:Root / lemma: persna, -snT-, -sno- 
67190:Root / lemma: pers- 
67196:Root/ lemma: pers-\ to drizzle, sprinkle; dust, ashes, derived from Root/ lemma: per-1, 
67220:Root / lemma: perth- {*pe-horghi-a) 
67228:Root / lemma: perth-{*pe-horghi-a)\ pole; sprout, derived from a prefixed pe- of Root/ 
67248:Root / lemma: pes-3, pesos 
67266:Root / lemma: pet-1, pet-, peta- 
67304:Root / lemma: pet-2, peta- : pte- pto- (gr. pta^ 
67438:Root / lemma: peuR- and peug- 
67462:Root / lemma: peu-1, peuQ- : pu- 
67483:Root / lemma: peu-2 
67507:lemma: peu-1, peua-. pu-\ "to clean, sift' , Root/ lemma: peu-2\ "to research, to
```


## [2026-09-07T20:35:48.098Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Page(s): 78[5-9]\\|Page(s): 84[0-4]\\|Page(s): 82[7-9]\" POK_full.txt | head -40"
}
```


### [2026-09-07T20:35:48.158Z] TOOL RESULT

```
64355:Page(s): 785-786 
64369:Page(s): 786 
64590:Page(s): 785 
64681:Page(s): 788 
64707:Page(s): 789 
64731:Page(s): 789 
64745:Page(s): 789 
64759:Page(s): 789 
64843:Page(s): 787-788 
64859:Page(s): 788 
64871:Page(s): 789 
64887:Page(s): 789 
64951:Page(s): 787 
67460:Page(s): 828 
67481:Page(s): 827 
67511:Page(s): 827 
67518:Page(s): 827 
67524:Page(s): 828 
67575:Page(s): 828 
67603:Page(s): 829 
67840:Page(s): 827 
67878:Page(s): 829 
68622:Page(s): 840-841 
68656:Page(s): 841 
68696:Page(s): 841-842 
68740:Page(s): 842 
68758:Page(s): 842 
68772:Page(s): 843 
68908:Page(s): 842-843 
68966:Page(s): 844 
68986:Page(s): 843-844
```


## [2026-09-07T20:35:53.939Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '64779,64845p' POK_full.txt\necho \"=====PA====\"\nsed -n '64909,64960p' POK_full.txt"
}
```


### [2026-09-07T20:35:54.007Z] TOOL RESULT

```
Root / lemma: paR- and pag- 

Meaning: to repair, strengthen 

Grammatical information: present *pag-mi, paR-si, paR-ti 

Material: Old Indie pas- (Instr. PI. padbhfh) " loop, noose, snare, rope', pasa-m. ds., pajra- 

" thickset, strong'; 

Avestan pas- " join each other, fasten, bind, piece together a jigsaw puzzle, fit together ', 
fsabis^ in chains ' (about pourupaxsta-^ a lot, richly folded ' s. Benveniste BSL. 29, 106 f.); 

gr. naaaaAoq, Attic naTTaAo(; m. 'peg, plug, nail' (-ki-), nnaau), Attic nnTTw ' Trnyvupi '; 
TTnyvOpi (Doric -5-) ' fasten by hitting; allow to solidify, congeal ' (snaynv, nEnnya, 
nriKT6(;), nnypa n. "plant, rack ', nr|y6(; "tight, firm, strong', nnyavov n. " Raute ', vau-nnyo(; 
' shipbuilding master ', nr|yuAi(; Adj. f. " reifig, icy ', nayo(; m. "ice, hoarfrost ' (also Dat. PI. 
naysGi "frost'), hom. " crag cliff; naxvr) (*na^va) " hoarfrost, frost', nayn " loop, noose, 
snare, dragnet ', naKTOw "make tight, firm, close, block ', a-ira^ "simple, just'; na^ Adv. 
"enough!'; here nriyn, Doric naya " ueuNe '; 

Latin pacTsco {sek. -or) " einen Vertrag oder Vergleich festmachen, abschlieflen ', Old 

Latin pacio^ pactio ', pacunV paciscuntur ', pax, -c/'sf. "peace; friendly disposition ' 

(Umbrian pase tua^ pace tua ' in the address of divinities), yoa/i/s "picket, pole' (from *pak- 

slos, compare Demin. paxillus); pango {pepigr, renamed peg/ afier freg/, and panx/) " 

r 

befestigen, einschlagen; aneinanderfijgen, schriftlich verfassen, festsetzen ' (to the 

nasalization of present compare Germanic *fa/jxan), compages^ ]o\x\\. ', pag/na{*\he 

papyrus stripes added to the sheet) " sheet of paper, side, column ', pagus^ rural 

community, village, construction ', propago, propages^ Setzlinge ', propagare^ einen 

Setzling in der Erde festmachen, daher fortpflanzen '; Umbrian pase {see above), paca 

Adv. " causa ', Oscan prupukid^ ex antepacto ?', Umbrian Paelignian Marrucinian pacri- " 

propitius, placatus '; Middle Irish age^\\mb, member, pillar' {*pagio-), ^//"pleasant' {*pagli-\ 



or as *pokli- to Old Icelandic faegiligr^s., s. *peR-1l); cymr. ae/c»o'"limb, member' 
{*paglatu-)\ 

Germanic Nasalpras. *farjxan (: Latin pangd) in Gothic fahan. Old Icelandic fa. Old 
English fon. Old High German fahan. Old Saxon fahan an6 fangan' capture ', Gothic 
gafahn.. Old Icelandic fengr. Old English fengm.. Old High German fangm. " catch, booty 
'; Old High German fuoga' joint ', gafuogi^ fitting', hJ-fuoge^ matchmaker ', Old High 
German fuogen. Old Saxon fogian^ add ', Old English gefegan^ fit, connect ', Middle High 
German vagen^ add '; from *pag-:Q\^ Saxon fac^ encirclement, Umzaunung ', Middle 
Low German i/a/rm. ds. "dividing off, partitioning off. Old High German fah^ moenia ', 
Modern High German Fach, einfach; from temporal department Old English /fee 'stretch of 
time'. Middle Low German vaken, vake. Late Middle High German ^ei/ac/?' often'. Middle 
High German drier vacher' thrice, three times '; 

Slavic *yC»aza-m. in sloven, paz ' \o\nt ', paz' wooden wall '. 

References: WP. II 2 f., WH. II 232 f., 235 f., 245 f., Trautmann 209. 
Page(s): 787-788 

Root / lemma: pan- 
=====PA====
Root / lemma: pa- : pa- and pa-t- : pa-t- 

Meaning: to feed, graze 

Material: Armenian hauran^ herd' {*pa-tro-), /701//1/ 'herdsman, shepherd' {*oui-pa-)\ gr. 

Doric TTavia rrAnapovn, navia TanArjaiJia; Latin pasco, -ere, pavi, pastum 'allow to graze, 

fijttere', Dep. ' devour, graze' {*pas-scd), yoas/o/'' herdsman, shepherd'. 

Maybe Alb. {* pastor!) i6>5/'/' herdsman, shepherd'. 

Note 

Alb. i6>a/''grass, fodder', bares^ walk, stroll ' derived from alb. {*barma) it'SAna 'medicine, 

herb, grass' from lat. pharmacum < gr. pharmakon from Egyptian Coptic pahre, fahn" cure'. 

Lat. pabu/um load' {*pa-d^/om), pan/s'bread' (because oi past/7/us' pellet, globule from 
meal, flour' from *pa-st-nis)\ Messapie iravoc, 'bread' is Latin loanword; Old Irish ain-chess 
' bread basket'; 



perhaps as Venetic-lllyrian element in Celtic *pa-ro-^ willow ' in cymr. pawr' willow ', PI. 
porion, therefrom Verbalnom. pori. Middle Breton peuriff, bret. yOe^/7" graze'; with -//to- suffix 
Old Icelandic fodru.. Old English fodoru.. Old High German fuotarlood'; Old Church 
Slavic pasg, past/'graze' ( *pasRd)\ Tocharian A pas-, B pask- 'beware, guard'; Hittite 
pahs- {pahhas-) " shield '. 
Maybe alb. Geg me pa, aor. pashe'to watch, protect'. 

With -^further formations: gr. naiEopai 'eat and drink '; aTraaToq ' without meal and 
drink, beverage, liquid which is swallowed to quench one's thirst, draught, potion'; doubtful 
Old Irish as{a)/d' it grows' (" increases '), Middle Irish 55' Wachsen ' {*pat-to-)\ Gothic 
fodjan^ nourish ', Old Icelandic f0da. Old English fedan. Old Saxon fodian. Old High 
German fuotenAs., Old English foda, engl. /boo^'nourishment, food'. Old English fostor 
ds.. Old Icelandic fostr^ upbringing, sustenance, livelihood' {*pat-tro-)\ ablaut. Old High 
German kauatoV pasta ' (Old High German Gl. 2, 333, 65), /^/^/7^a 'nourishment, food'. 
Middle Low German vedemei. ' acorn mast '. 

References: WP. II 72 f., WH. II 246 f., 260, Trautmann 207 f.; 
See also: compare also pen-lleed'. 
Page(s): 787 

Root / lemma: {peg- :) pog- : pog- pok-s- {*pegh-) 

Meaning: shoulder, hip, side 

Material: Old \x\(X\c paksa-vn. 'shoulder, wing' and ' side posts ', paksas-n. 'side'; common 

Old Indie -gh- > -ks-
```


## [2026-09-07T20:35:55.515Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '68700,68780p' POK_full.txt\necho \"=====pater====\"\ngrep -n \"lemma: pater\\|lemma: p9ter\\|lemma: pater-\\|pater, poti\" POK_full.txt | head\nsed -n '67860,67890p' POK_full.txt"
}
```


### [2026-09-07T20:35:55.612Z] TOOL RESULT

```
Meaning: owner, host, master, husband 

Material: Old \nd'\c pat/-, Avestan pa///- "master, mister, lord, master, consort, partner'; Old 

Indie /Oa//7/"" mistress, wife', Avestan paz?/?/- 'mistress'; Old \nd\c patyate^\r\errsc\nt, is 

teilhaftig' (: Latin potior); 

Avestan x'ae-pati- "er selbst'; 

gr. hogk; ' husband ', nowia "mistress (of Hauses), wife'; 5£a-noiva 'mistress of 
Hauses' (*5£a-novia, from *5£a-noTvia), 5£a-n6Tr|<;, -ou "master, mister of Hauses' (see 
above S. 198); alb. pata^had', y05s/7e"gehabt' {*pot-to-) (to a present as Latin potior. Old 
Indie yoa/ya/e); 

Latin potis {potior, potissimus) "wealthy, mighty', possum. Old Latin also potis sum 
"kann', potui, potensirom an e-denominative as Oscan putiad ^possW, putians 'poss\nt', 
Latin potestas^ power', potior, -TrT{potrtur and potTtui) "sich bemaehtigen'; com-pos 
"teilhaftig' (*"Mitherr'), tiospes, -itis' guest's friend ', pael. iiospus {*gtiosti-pots^ Qasihexx'); 
ein unflektiertes *poti 'selbst' placed in utpote^as natijrlich, da namlich, namely', actually 



*ut *pote{esf) "as es possible is = naturiicli', furtlierwitli syncope in m/hr-, meo-, suapte 
etc.; 

Gotliic bru^-fa^s^ bridegroom ', /7£//70'a-/&A'5"Befelilsliaber about 100 Mann'; engl. fad 
"strong, valiant, big, large'; 

Lithuanian pa/s "husband' and "selbsf (old patis), Latvian pats^ householder ' and 
"selbsf, Lithuanian K/espa/s "master, mister' (old viespatis). Old Prussian pattiniskun f\Vk. f. 
" matrimony '; f. Old Lithuanian viespatnr, *patn/'under influence of *yOa//- transfigured to 
*patr\n Old Prussian waispattin f\Vk. "wife, woman', Lithuanian pat/^\N\ie', Latvian pat/ 
"Wirtin'; indekl. particle Lithuanian pat, Latvian yC>a/"selbst, even, straight'; about Old 
Church Slavic gospodb "master, mister', see above S. 453; 

Hittite -yC»s/"eben(so), also, rather'; Tocharian A pa/s "husband'. 

References: WP. II 77 f., WH. I 660 f., II 350 f., 379 f., Trautmann 208, Benveniste 
Origines 1, 63 f., Pedersen Hittite 77 f., Endzelin Latvian Gr. 396 f. 
Page(s): 842 

Root / lemma: po-ti 

Meaning: against 

Note: through das Adv.-forms -//(compare *proti- : *pro above S. 815 f.) from *po (see 

below *apo' ab') extended 

Material: Avestan pa/'t/, ap. /05//y proverb, and preposition "against, entgegen, to, auf, by'; 

"an; for, um'; "from - from'; "in - toward, in'; hom., Boeotian, lak. etc. nori "np6(;' proverb. 

and preposition "against - toward, against, compared with; an, to', "in - toward, from-'. 

References: WP. II 77, Schwyzer Gr. Gr. 2, 508 f. 

Page(s): 842 

Root / lemma: pougo- or pougho- 

Meaning: clear, sound 

Note: only Celtic and Slavic 

Material: Old Irish o^"jungfraulich', oge"Jungfraulichkeit'; Czech pouhy^ pure, bare, 

simple, just'. 

References: WP. II 77. 

Page(s): 843 

Root / lemma: p6(i)-1 : (pa/-?:) pT- 



Meaning: to graze 

Material: Old Indie pati, Avestan /7a///"hutet, bewacht, schijtzt', Old Indie go-pa- m. 
=====pater====
Old Indie Dyaus pita eic. see above S. 413. 

Ableitnngen: Old Indie p///ya- gr. naTpiO(;, Latin yOa/A/^s'vaterlich', Middle Irish aithrei. 
"vaterliche family'; Old Indie pftrvya-, Avestan tuirya- ( *ptarvya-), Latin patruus. Old High 
German fetiro, fatirro, fatureo {Gerfr\an\c*faduru/a-) "Vaterb ruder', Modern High German " 
cousin ', Old English f^dera ^Vatersbruder' (compare gr. naTpu)(;from*yC>a//(9i/sds., with 
verschobener meaning naTpu)iO(; "vaterlich'); Old pers. hama-pitar-= gr. opo-narajp, 
compare Old Icelandic sam-fedra^irom the same Vater' {*-fadrjans)\ compare gr. naTpui6(; 
"Stiefvater' (after priTpuia " stepmother '), Armenian yaurayds.; only single-linguistically are 
gr. narpn, Attic narpa 'Vaterland', naTpi(;, -i5o(;f. ds., Latin patriads., patronus 
'Schutzherr', patro, -are "vollbringe, vollziehe'; proprius 'e\gen, eigentijmlich, bestandig' 
from * prop(a)trios "from den nponaTop£(;, den Altvorderen as ererbter Besitz uberkommen' 
(?), s. WH. II 374 f.; mcymr. e^y/yd'dwelling'could originally as 'vaterlicher possession ' 
with Middle Irish a///?/-© identical sein; Old Icelandic fedgarP\. "father and son' (compare gr. 
narpiKoq 'vaterlich'); fedginP\. "parents' {*fedr-gin). 

References: WP. II 4, WH. II 263 ff.; of babble-word pa-derive ? KretschmerWZKM. 51, 
315 f; or to pd(i)- shield, watch? 
Page(s): 829 

Root / lemma: phel- 
See also: s. (s)p(ti)el-. 
Page(s): 851 

Root / lemma: pher- 
See also: s. (s)p(h)er-. 
Page(s): 851 

Root / lemma: phol- 

Meaning: to fall
```


## [2026-09-07T20:36:11.116Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Page(s): 84[5-9]\" POK_full.txt | head\necho \"---context of 847---\"\nawk 'NR>=68990 && NR<=69120' POK_full.txt | head -60"
}
```


### [2026-09-07T20:36:12.404Z] TOOL RESULT

```
69012:Page(s): 845 
69038:Page(s): 845 
69057:Page(s): 845 
69079:Page(s): 846 
69104:Page(s): 845-846 
69121:Page(s): 846 
69135:Page(s): 846 
69139:Page(s): 846 
69155:Page(s): 846 
69174:Page(s): 846-847 
---context of 847---
Meaning: willing, covetous, active 

Material: Gothic (faihu-)friks\qe\(i-) greedy ', Old Icelandic frekr^ greedy, strong, hard, 

agile, lively'. Old English frecc^ greedy, audacious' {*frakja-). Old High German freh^ 

greedy ', Modern High German frech(i\a\. also "agile, lively, fresh'; Old English fraec^ 

eager, avid, audacious'. Middle Low German vrak, Norwegian Swedish dial, frak, Danish 

^■5^ "quick, fast, gamy'; Norwegian fraecAs. {*frakJa-)\ Old Icelandic fr0kn, fr0kinn^Qaxr\y\ 

Old English /^ec/7e "audacious, wild'. Old Saxon frokn/'wM, cheeky, foolhardy ', Old High 

German Frohn, Fruochan-\v\ PN; /^d/7/7/"iactura'; poln. pragnqc^ greedy long, want', 

Czech prabnouf/ lust, crave' etc.; here Old Icelandic frakkr^ gamy' and the VN Franken. 

References: WP. II 88; 

See also: belongs to gr. anapyau) "bin horny, lustful', see below sp(h)er(e)g-. 

Page(s): 845 



Root / lemma: prep- 

Meaning: to come in sight 

Material: Armenian erev/m'\Ner6e visible, ersclieine', erevak' shape, Bild, mark, token, 

sign', eres{*prep-s-), mostly PI. eresk'^iace, Miene, sight, Vorderseite', eresem 'ze'\ge 

myself, erscheine'; also orova/n^beWy' etc. {*prop-n-/o-)7 

gr. npsnu) "falle in die Augen, erscheine, steche hervor, zeichne myself from', npsnsi 
"es ziemt sich', dpi-, 5ia-, £k-, £u-, [}Zici--npzTTr\q 'hervorstechend, sich auszeichnend'; Gso- 
np6no(; ' seer ' ("the sich from god from vernehmlich Machende'); perhaps npauiq " 
phren'; different above S. 620. 

Old Irish ricMlorm, shape', cymr. aM/? 'species' {*prp-tu-)\ 

Old High German furben^c\eav\, clean, sweep, wash away ' ("in die Augen fallend make, 
ein Ansehen give'). Middle High German vurbe^ cleaning, purification; Sternschnuppe', 
Old Low German wel gifurvicl^cas\.a\ 

References: WP. II 89. 
Page(s): 845 

Root / lemma: pret- prvt- 
Meaning: to understand 

Material: Middle Irish /'a//7a/^/o'"bemerkt'; Gothic fraNu. "sense, mind, reason', fral=>jan, 
fro^^ understand, comprehend ', /h?A's "smart, sensible, wise'. Old Icelandic frodr. Old 
Saxon Old English frod. Old High German fruot6s.. Middle High German vruotec, vruetec 
"quick, fast determined, alert, awake, smart, valiant'. Modern High German Swiss fruetig 
"blithe, glad, fresh, valiant, quick, fast', also Old High German /^5o'"strenuus efficax', 
fradah-ITh^ procax'; perhaps Old High German a/7/-/^/s/"interpretatio' {*pret-sti-)\ Lithuanian 
prantu, prasti^ habitual, customary become', su-prasti^ understand, comprehend ', protas
```


## [2026-09-07T20:36:12.737Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^pā-\\|^pəter-\\|^poti-\\|^pag-\\|^pak-\\|^pā̆k̑-\\|^pater\" AHD_watkins1985.txt | head -20\necho \"=== search loose ===\"\ngrep -n \"To protect, feed\\|To fasten\\|Powerful; lord\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-07T20:36:12.808Z] TOOL RESULT

```
863:poti-
870:poti-. Powerful; lord. 1. Latin potis, powerful, able (> potestas, power): PODESTA, POSSESS, POWER. 2. Latin compound posse, to be able (contracted from potis, able
=== search loose ===
204:pa-. To protect, feed. Contracted from *pao-. kak-2. A round object, disk. Germanic root.
812:os-. Ash tree. Germanic “aski- in Old English zsc, ash: ASH?2. [Pok. 6s- 782.] 6s-. Mouth. 1. Latin ds (stem 6r-), mouth, face, orifice, and derivative dstium (< suffixed form *6s-to-), door: ORAL, OS!, OSCULATE, OSCULUM, OSTIARY, OSTIUM, USHER; INOSCULATE, ORIFICE, ORINASAL, OROTUND, OSCITANCY, PERORAL. 2. Possibly Latin auriga, chari- oteer (< *6r-ig-, “he who manages the (horse’s) bit”; -ig-, driving, from *ag-; see ag-): AURIGA. [Pok. 1. 6us- 784.] ost-. Bone. 1. Latin os (stem oss-), bone: 082, OSSEOUS, OSSICLE, OSSUARY; OSSIFRAGE, OSSIFY. 2. Greek osteon, bone: OSTEO-; ENDOSTEUM, EXOSTOSIS, PERIOSTEM, SYN- OSTOSIS, TELEOST. 3. Suffixed form *ost-r- in: a. Greek ostrakon, shell, potsherd: OSTRACIZE, OSTRACOD; b. Greek ostreon, oyster: OYSTER; C. variant form in Greek astragalos, vertebra, ball of the ankle joint, knuck- lebone, Ionic molding: ASTRAGAL, ASTRAGALUS. [Pok. ost(h)- 783.] ous-. Also aus-. Ear. 1. Suffixed form *ous-en- in Ger- manic *auzan- in Old English éare, ear: EAR}. 2. Suffixed form *aus-i- in Latin auris, ear: AURAL!, AURICLE; AURIFORM, ORMER. 3. Latin auscultdre, to listen to (*aus- + *kli-to-, inclined; see klei-): AUSCULTATION, scouT!. 4. Suffixed basic form *ous-os- in: a. Greek ous (stem 6t-), ear: OTIC, OTO-; MYOSOTIS, PAROTID GLAND; b. Greek Jagés, hare (< */ag-ous-, “with drooping ears”; *lag-, to droop; see slég-). [Pok. dus- 785.] owi-. Sheep. 1. Germanic *awi- in Old English ewe, eowu, ewe: EWE. 2. Latin ovis, sheep: OVINE; OVIBOS. [Pok. oui-s 784.] pa-. To protect, feed. Contracted from *pas-. 1. Suffixed form *pé-trom in Germanic *fodram in: a. Old English fédor, fodder: FODDER; b. Old French feurre, fodder: FORAGE; C. Old French forreure, trimming made from animal skin, fur (< “sheath, case, lining”): FuR. 2. Suf- fixed form *pd-dhlom (doublet of *pd-trom) in Latin padbulum, food, fodder: PABULUM. 3. Extended form *pat- in: a. Germanic *féd-, food, in Old English foda, food: Froop; b. Germanic denominative *fédjan, to give food to, in Old English fédan, to feed: FEED; Cc. suffixed form *pdt-tro- in Germanic *fdstra- in Old English fostor, food, nourishment: FOSTER. 4. Extended form *pds- in: a. suffixed form *pds-sko- in Latin pdscere, to feed: PASTURE; ANTIPASTO, PESTER, REPAST; b. Latin pdstor, shepherd: PASTOR; C. suffixed form *pds-t-ni- in Latin pGnis, bread (diminutive pastillus, medicine tablet): PANADA, PANATELA, PANNIER, PANOCHA, PANTRY, PAS- TILLE, (PENUCHE); APPANAGE, COMPANION, (COMPANY). 5. Suffixed form *pd-ti- in Iranian *pdti- in Persian pdd, protecting against: BEZOAR. 6. Suffixed form *pd-won-, protector, in Old Persian khshathra-pdvd, protector of the province: SATRAP. [Pok. pd- 787, 1. pd(i)- 839.] pag-. Also pak-. To fasten. 1. Lengthened-grade form *“pak- in Germanic *fogjan, to join, fit, in Old English fégan, to fit closely: FAY}. 2. Nasalized form *pa-n-g- in: a. Germanic *fangiz, seizure, in (i) Old English fang, feng, plunder, booty: FANG (ii) Dutch vangen, to catch: VANG; b. Latin pangere, to fasten: COMPACT!, IMPINGE. 3. Root form *pak- in: a. Latin pdx, peace (< “a binding together by treaty or agreement”): PACE?, PAY!, PEACE; APPEASE, PACIFIC, PACIFY; b. Latin pacisci, to agree: PACT. 4. Suf- fixed form *pak-sio- in: a. Latin pdlus, stake (fixed in the ground): PALE!, PALISADE, PEEL’, POLE?; IMPALE, TRA- VAIL, (TRAVEL); b. probably Latin pdla, spade: PALETTE, PEEL*. 5. Lengthened-grade form *pdg- in: a. Latin pdagus, “boundary staked out on the ground,” district, village, country: PAGAN, PEASANT; b. Latin pdgina, “trellis to which a row of vines is fixed,” hence (by metaphor) column of writing, page: PAGE?, PAGEANT; c. Latin prépdgés (pré-, before, in front; see per'), layer of vine, offspring (< “a fixing before”): PROPAGATE; d. Greek pégnunai, to fasten, coagulate: PECTIN, PEGMA- TITE. [Pok. pak- 787.] pan-. Fabric. 1. Germanic *fandn- in: a. Old English
870:poti-. Powerful; lord. 1. Latin potis, powerful, able (> potestas, power): PODESTA, POSSESS, POWER. 2. Latin compound posse, to be able (contracted from potis, able
```


## [2026-09-07T20:36:25.398Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '870p' AHD_watkins1985.txt | cut -c1-1400\necho \"=== peter ===\"\ngrep -on \"p[e6a]ter-\\. Father[^[]*\\[Pok[^]]*\\]\" AHD_watkins1985.txt | head -5"
}
```


### [2026-09-07T20:36:25.466Z] TOOL RESULT

```
poti-. Powerful; lord. 1. Latin potis, powerful, able (> potestas, power): PODESTA, POSSESS, POWER. 2. Latin compound posse, to be able (contracted from potis, able
=== peter ===
```


## [2026-09-07T20:36:28.300Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '870,872p' AHD_watkins1985.txt | cut -c1-2500\necho \"=== grep pater/father root ===\"\ngrep -n \"Father\\.\" AHD_watkins1985.txt | head"
}
```


### [2026-09-07T20:36:28.362Z] TOOL RESULT

```
poti-. Powerful; lord. 1. Latin potis, powerful, able (> potestas, power): PODESTA, POSSESS, POWER. 2. Latin compound posse, to be able (contracted from potis, able
prak-
+ esse, to be; see es-): POSSIBLE, POTENT; (IMPOTENT), PREPOTENT. 3. Form *pot- in: a. compound *ghos-pot-, “suest-master,” host (see ghos-ti-); b. compound *dems-pot-, “house-master,” ruler (see deme-'). 4. Old Persian pati-, master: PADISHAH. [Pok. poti-s 842.] [prak-. To make, do. Greek root. Greek prassein (Attic prattein), to effect, do: PRACTICAL, (PRACTICE), PRAG- MATIC, PRAXIS. [In Pok. 1. per 811.]] prek-. To ask, entreat. 1. Basic form *prek- in Latin *prex, prayer (attested only in the plural precés), with denominative precdri, to entreat, pray: PRAY, PRAYER?, PRECARIOUS; DEPRECATE, IMPRECATE. 2. Suffixed zero-grade form *prk-sk- becoming *pork-sk-, contracted into *posk- in suffixed form *posk-to-, contracted into *posto-, which appears in Latin postuldre, to ask, re- quest: POSTULATE; EXPOSTULATE. [Pok. 4. perk- 821.] prep-. To appear. Suffixed zero-grade form *prp-yo- in Germanic *furbjan, to cause to have a (good) appearance, polish, in Old French fo(u)rbir, to polish, burnish: FuR- BISH. [Pok. prep- 845.] preu-. To hop. 1. Zero-grade form *pru- in Germanic *fru- in Old English frogga (with obscure expressive suffix -gga), frog: FROG. 2. Extended o-grade form *prowo- in Germanic *frawaz in: a. Middle Dutch uro, “leaping with joy,” happy: FROLIC; b. Old High German fré, happy, in frewida, joy (> German Freude): scHa- DENFREUDE. [Pok. preu- 845.] preus-. To freeze, burn. 1. Germanic *freusan, to freeze, in Old English fréosan, to freeze: FREEZE. 2. Suffixed zero-grade form *prus-to- in Germanic *frustaz, frost, in Old English forst, frost, frost: FROST. 3. Suffixed form *preus-i- in Latin *preusis, *preuris, act of burning, whence denominative pririre, to burn, itch, yearn for: PRURIENT, PRURIGO, PRURITUS. 4. Suffixed zero-grade form *prus-ina in Latin pruina, hoarfrost: PRUINOSE. [Pok. preus- 846.] pri-. To love. Contracted from *pria-. 1. Suffixed form *priy-o- in Germanic “frijaz, beloved, belonging to the loved ones, not in bondage, free, in: a. Old English fréo, free; FREE; b. Dutch vrij, free: FILIBUSTER. 2. Suffixed (participial) form “priy-ont-, loving, in Germanic ‘“fri- Jjand-, lover, friend, in Old English friond, fréond, friend: FRIEND. 3. Suffixed shortened form *pri-tu- in Germanic *frithuz, peace, in: a. Old High German fridu, peace: SIEGFRIED; b. Old French esfreer, to disturb: AFFRAY; c. Germanic *frij-, peace, safety, in compound *berg-frij-, “high place of safety” (see bhergh-?). 4. Suffixed fem
=== grep pater/father root ===
846:ré, feather, in Old English fether, feather: FEATHER. 2. Latin petere, to go toward, seek: -PETAL, PETITION, PETULANT; APPETITE, COMPETE, IMPETUS, PERPETUAL, REPEAT. 3. Suffixed form *pet-nd in Latin penna, pinna, feather, wing: PANACHE, PEN!, PENNA, PENNATE, PEN- NON, PINNA, PINNACLE, PINNATE, PINNATI-, PINNULE. 4. Suffixed form *pet-ro- (see 6ku-). 5. Suffixed form *pet-yo- in Latin propitius, favorable, gracious, originally a religious term meaning “falling or rushing forward,” hence “eager,” “well-disposed” (said of the gods; pro-, forward; see per'): PROPITIOUS. 6. Suffixed zero-grade form *pt-ero- in Greek pteron, feather, wing, and pterux, wing: -PTER; ACANTHOPTERYGIAN, APTERYX, ARCHAEOP- TERYX, COLEOPTERA, MECOPTERAN, PERIPTERAL, PLE- COPTERAN, PTERIDOLOGY, PTEROCERCOID, PTERYGOID. 7. Suffixed zero-grade form “pt-ilo- in Greek ptilon, soft feathers, down, plume: COLEOPTILE. 8. Suffixed variant form *pté-no- in Greek pténos, winged, flying: STEAROP- TENE. 9. Reduplicated form *pi-pt- in Greek piptein, to fall: PTOMAINE, PTOSIS; PERIPETEIA, PROPTOSIS, SYMP- TOM. 10. O-grade form “pof- in Greek potamos (-amo-, Greek suffix), “rushing water,” river: HIPPOPOTAMUS. [Pok. 2. pet- 826.] pete-. To spread. 1. Suffixed o-grade form “pota)-mo- in Germanic *fathmaz, “length of two arms stretched out,” in Old English fethm, fathom: FATHOM. 2. Suffixed (stative) variant zero-grade form *pat-é- in Latin patére, to be open: PATENT, PATULOUS. 3. Variant zero-grade form in nasalized form *pat-no- probably in Latin pan- dere (past participle passus < *pat-to-), to spread out: PACE!, (PAS), (PASS), PASSIM; EXPAND, REPAND. 4. Suf- fixed form *pet-alo- in Greek petalon, leaf: PETAL. 5. Suf- fixed form *pet-ano- in Greek patané (? < *petand), platter, “thing spread out”: (PAELLA), PAN!, PATEN, (PATINA!), (PATINA2). [Pok. 1. pet- 824.] [petra. Cliff. Greek noun. Collective formation from petros, rock, stone (of unknown origin). PETRO-, PET- ROUS; PARSLEY, PETRIFY, SALTPETER.] peu-. To cut, strike, stamp. 1. Suffixed (participial) zero-grade form *pu-to-, cut, struck, in: a. Latin putdre, to prune, clean, settle an account, think over, reflect, consider: PUTAMEN, PUTATIVE; (ACCOUNT), AMPUTATE, COMPUTE, COUNT!, DEPUTE, DISPUTE, IMPUTE, REPUTE; b. possibly Latin puteus, well (> Old English pyét): Prt’. 2. Variant form *pau- in: a. suffixed form *pau-yo- in Latin pavire, to beat: PAVE, (PAVE); b. suffixed (stative) form *paw-é- in Latin pavére, to fear (< “to be struck”): PAVID; C. perhaps Greek paiein, to beat: ANAPEST. [Pok. 3. péu- 827.] peue-. To purify, cleanse. Suffixed zero-grade form *pii-ro- (< *pua-ro-) in Latin purus, pure, and purgdre, to purify (< “piir-igdre; second element agere, to drive; see ag-): PURE, PURGE, PURITAN; COMPURGATION, DEPU- RATE, EXPURGATE, (SPURGE). [Pok. 1. peu- 827.] peuk-. Also peug-. To prick. Zero-grade form “pug-. 1. Suffixed form *pug-no- in Latin pugil, pugilist, and pugnus, fist, with denominative pugndare, to fight with the fist: PONIARD, PUGILISM, PUGIL STICK, PUGNACIOUS; IMPUGN, OPPUGN, REPUGN. 2. Nasalized zero-grade form *pu-n-g- in Latin pungere, to prick: BUNG, POIGNANT, POINT, POINTILLISM, PONTIL, (POUNCE!), (POUNCE?), PUNCHEON!, PUNCTUATE, PUNCTURE, PUNGENT; COM- PUNCTION, EXPUNGE, SPONTOON, TRAPUNTO. 3. Greek pugmé, fist: (PYGMAEAN), PYGMY. [Pok. peuk- 828.] pezd-. To fart. 1. Suffixed form *pezd-i- in Germanic *fistiz, a fart, in Middle English fisten, to fart: FEIST, FIZZLE. 2. Latin pédere, to fart: PETARD. 3. Possibly Latin pédis, louse (? < “foul-smelling insect”): PEDICU- LAR. See also perd-. [Pok. pezd- 829, 2. peis- 796.] peter-. Father. 1. Germanic *fadar in Old English feder (> Middle English fader), father: FATHER; FOREFATHER. 2. Latin pater, father (> patrare, to bring about): PADRE, PATER, PATERNAL, PATRI-, PATRICIAN, PATRIMONY, PA- TRON; EXPATRIATE, IMPETRATE, PERPETRATE. 3. Greek
```


## [2026-09-07T20:36:34.029Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('AHD_watkins1985.txt',errors='replace').read()\ni=t.find('peter-. Father.')\nprint(t[i:i+1400])\nEOF"
}
```


### [2026-09-07T20:36:35.322Z] TOOL RESULT

```
peter-. Father. 1. Germanic *fadar in Old English feder (> Middle English fader), father: FATHER; FOREFATHER. 2. Latin pater, father (> patrare, to bring about): PADRE, PATER, PATERNAL, PATRI-, PATRICIAN, PATRIMONY, PA- TRON; EXPATRIATE, IMPETRATE, PERPETRATE. 3. Greek
51
plat-
patér, father: PATRIOT; ALLOPATRIC, EUPATRID, PATRI- ARCH, SYMPATRIC. [Pok. paté(r) 829.]
p(h)ol-. To fall. Suffixed form *phol-no- in Germanic *fallan in: a. Old English feallan, to fall: FALL; b. Ger- manic causative *falljan, “to cause to fall,” strike down, in Old English fellan, fyllan, to cut down: FELL; c. Ger- manic compound *bi-fallan, to fall, happen (*bi-, by, at; see ambhi), in Old English befeallan, to fall: BEFALL. [Pok. phél- 851.]
[phulax. Watcher, guard. Greek noun of unknown origin, related to phulassein (Attic phulattein), to guard, pro- tect. PHYLACTERY, PHYLAXIS; PROPHYLACTIC. ]
pik-. Pitch. Latin pix (stem pic-), pitch: PAY?, PICEOUS, PITCH!; PICOLINE, PITCHBLENDE. [In Pok. pei(a)- 793.]
pilo-. Hair. A possible root. 1. Latin pilus, hair: PELAGE, PILAR, PILE’, PILOSE, PILUS, PLUCK, PLUSH, POILU; CAT- ERPILLAR, DEPILATE. 2. Suffixed reduced form “pil-so- possibly in: a. Latin pilleus, pileus, felt cap: PILEUS, PILLAGE; b. Greek pilos, felt: PILOCARPINE. [Pok. pi-lo- 830.]
pipp-. To peep. Imitative root. 1. Latin pipdre, to chirp (> Old High German pfiffa, pipe): FIFE, PIPE. 2. Latin
```


## [2026-09-07T20:36:36.129Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('AHD_watkins1985.txt',errors='replace').read()\nfor key in ['pap(p)a','papa.','PAPA','Pope','patriot']:\n    i=0\n    n=0\n    while n<4:\n        i=t.find(key,i+1)\n        if i<0: break\n        print('>>>',key,i,repr(t[max(0,i-200):i+250]))\n        n+=1\nEOF"
}
```


### [2026-09-07T20:36:37.394Z] TOOL RESULT

```
>>> pap(p)a 426538 'n Flemish frequen- tative pamperen, to cram with food, akin to the source of Middle English pamperen, to pamper: PAMPER. 2. Latin pappa, food (> Middle English pap, soft food): PAP?, POPPYCOCK. [Pok. pap(p)a 789, ba*mb- 94.] papa. A child’s word for “father,” a linguistic near-uni- versal found in many languages. 1. French papa, father: PAPA. 2. Greek pappas, father, and pappos, grandfather: PAPPUS, POPE. [Pok. pap(p)a 789.] paso-. Kinsman by mar'
>>> pap(p)a 426753 '*mb- 94.] papa. A child’s word for “father,” a linguistic near-uni- versal found in many languages. 1. French papa, father: PAPA. 2. Greek pappas, father, and pappos, grandfather: PAPPUS, POPE. [Pok. pap(p)a 789.] paso-. Kinsman by marriage. Latin parri- (for pari-) in compound parri-cida (oldest form paricidas), murderer of a near relation: PARRICIDE. [Pok. pdso-s 787.] past-. Solid, firm. 1. Germanic *fastuz, firm, fast, in: a. Old English fest'
>>> papa. 7643 'ge: in the languages of most countries where the bird is known, the cuckoo has a name derived from the noise it makes. A vast number of languages around the globe have “baby-talk” words like mama and papa. Fi- nally, languages commonly borrow words and other features from each other, in a whole gamut of ways ranging from casual or chance contact to learned coinages of the kind that English systematically makes from Latin and Greek. But where all '
>>> papa. 426563 ' pamperen, to cram with food, akin to the source of Middle English pamperen, to pamper: PAMPER. 2. Latin pappa, food (> Middle English pap, soft food): PAP?, POPPYCOCK. [Pok. pap(p)a 789, ba*mb- 94.] papa. A child’s word for “father,” a linguistic near-uni- versal found in many languages. 1. French papa, father: PAPA. 2. Greek pappas, father, and pappos, grandfather: PAPPUS, POPE. [Pok. pap(p)a 789.] paso-. Kinsman by marriage. Latin parri- (for '
>>> PAPA 426677 'od (> Middle English pap, soft food): PAP?, POPPYCOCK. [Pok. pap(p)a 789, ba*mb- 94.] papa. A child’s word for “father,” a linguistic near-uni- versal found in many languages. 1. French papa, father: PAPA. 2. Greek pappas, father, and pappos, grandfather: PAPPUS, POPE. [Pok. pap(p)a 789.] paso-. Kinsman by marriage. Latin parri- (for pari-) in compound parri-cida (oldest form paricidas), murderer of a near relation: PARRICIDE. [Pok. pdso-s 787.] '
>>> PAPA 784077 'ura PANE pan- PANEGYRIC ger-! PANEL pan-\nPANICLE pan- PANMICTIC melk- PANMIXIS meik- PANNIER pa- PANOCHA pa- PANOPTIC okw- PANORAMA wer-4 PANSY (s)pen-\nPANT bha-1 PANTHEON dhés- PANTRY pa-\nPAP? pap-2\nPAPA papa\nPAPILLA pap-1\nPAPPUS papa\nPAPULE pap-!\nPAR pere-2\nPARA-! pert\n-PARA pere-1 PARABLE gWelg-1 PARABOLA gW¥ele-1 PARACHUTE pere-1 PARACLETE kele-2 PARADE pere-1 PARADIGM deik- PARADISE dheigh-, pert PARADOX dek-! PARAFFIN pau- PARAGRAPH gerbh- '
```


## [2026-09-07T20:36:51.520Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD pāp/pab ===\"\ngrep -n \"^pāb\\|^pab\\|^pāp\\|^pap\\|^pid \\|papak\\|pābag\" PHD.txt PHD_mackenzie.txt | head -30\necho \"=== NYB glossary ===\"\ngrep -n \"^pāp\\|^pap\\|pāpak\\|papak\\|^pit\\|^pid\" NYB_vol2_glossary.txt | head -30"
}
```


### [2026-09-07T20:36:51.582Z] TOOL RESULT

```
=== PHD pāp/pab ===
=== NYB glossary ===
2864:pid (pa) [pd; LGLH; Prth NGRYN] foot, with the indef. art. —-ē [LGLH +1) 18", 241° ete. passim; HajA:6.11 (Prth); HajB:6.12 (LGLH). - Av. (842) päd-; MPrth p'd; MPrs p’y; Paz. pdé, pah; NP pā(y).
2872:pidak [p'dk'] station, sphere of the celestial bodies 522. 932-9. 104°. — Also p’hk' = pähak. — Av. (887) páóa-; Paz. päya (Mx); NP päyah.
3159:pit [>B'; pt'], cas. obl. pitar [PBY-tl; ptl 143], pl. cas. obl. pitarän PBY-tl’n'] fa- ther; the difference between pit and pitar is fading: pit is the subj. of the sentence 22°. 3216, 3716, 633, but the cas. obl. in the majority of cases; the cas. obl. pitar is much restricted in use, and stands for the cas. rect. 2711. 28?!; voc. pit 10018, pitar 27°; — pl. parents 2712, 3818, 4115-26, 513 (all in the function of cas. obl.). — Olr pitar-, nom. pita > Milr pit; pitar is a secondary formation. NP old pid, commonly ptdar. — MPrthPrs pyd, pydr indifferently used. V. also apé-pit.
3160:pitik [ptyk] belonging to the father, is the better reading, instead of patitik, 41? pat — mändak for a lapse affecting the father; thus Antiá and two of Sanjana’s MSS.
7330:pid, pidar: pit
```


## [2026-09-07T20:36:52.486Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN leaf 55 (p.34) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==56' HRN.txt | head -60"
}
```


### [2026-09-07T20:36:53.848Z] TOOL RESULT

```
=== HRN leaf 55 (p.34) ===
— M -
Praefix im Neupersischen vergl. unter No. 345; upa
als Praefix liegt vor in peldrüd (No. 288), pi[ndästen
(No. 331), pelnhan (No. 332), pe[dld (No. 289), pe[send
(No. 319), pe[gah (No. 324).
Beide Formen, he und pe-, als Reflexe von pati und
upa^ Verstössen gegen die Lautgesetze.
145. bä, eba *mit, zu .
päz. awäk *mit', awakth (vergl. Verlorenes Spraeh-
gut' No. 37).
kurd. LW. ba; bei. gön, n. gö {^gvä) mit' etc.* (124).
Eine ältere Form lässt sich nicht nachweisen. Aus
dem Begriff des 'Verbundenseins mit, des Anhaften«*
erklärt sich auch die folgende Verwendung von ba
§ähn. P. VI, 270, Vers 1331: ba merd-t gurd ser-l
X^^s^rä /ßr^ bayed sümurd 'dann soll er als ein Held
sein eignes Haupt für nichts achten'.
146. "bä, -wä (in Comp.) 'Speise, Brühe; kochend', z. B.
ispedbäy nänba etc.
Vergl. g. (Yezd) päkevi 'Küche*.
aw. nasu]paku' ^Leichen kochend, -verbrennend*;
skr. pdka- bezw, päkd- (Hörn, Indog. Forsch. H, 141).
phlv. spetväk (vd. 13 (78) Gl.) wird kaum np. ispedbä
sein (Spiegel, Commentar 306).
147. bäb Tater (JSähn. I, 43 Vers 172), Grossvater, vergl.
bäba, babek^).
g. bawg,
phlv. papak (vergl. Nöldeke, Kärnämak, 35 Note 3;
Hörn, Mitteilungen, Heft IV, 24, ZDMG. 44, 658
No. 44).
arm. LW. pap^) 'Gross vater*.
kurd. bäwä, ba]plr, bäwuk (H.-Sch.).
\J148. bäj 'Tribut', bä^, baz, vergl. bäjbän *Zolleinnehmer* etc.
ap. büß' Tribut*; vergl. n^ozipaCtg' ä^cog A^iiftvog
yal TivQivog dnrog xui xvnaolaanv ore(favog yal olvog
*) Pähj Pap bedeutet im Np. nur *Pap8t* (ital. papa).
*) Arm. hav *Gro88vater* stellt S. Bugge mit Petermann wohl
richtig zu lat. avus.
```


## [2026-09-07T20:37:04.926Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB p150 = leaf 158 ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==159' NYB_vol2_glossary.txt | head -50"
}
```


## [2026-09-07T20:37:06.069Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 420 421 422 423 424; do echo \"##### leaf $n\"; awk -v N=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==N' BQT_v1_pages.txt | head -8; done"
}
```


### [2026-09-07T20:37:06.133Z] TOOL RESULT

```
=== NYB p150 = leaf 158 ===
rning a subst. or an adv. and forming with them compound pre- positions and adverbs: 6 berön, 6 nazdik, O pasth, 6 patirak, o peš (frac 6 peš, andar 6 peš); in a frame prep.: 6... rón; v. these ws.; — prev.: 6 druž früc mat the drug came to the place 5715-16; jn this case the ideogr. KN is common: 348 twice. 6521, 9422. — The form LH = 67 as a prep. 1612. 4210, 4424-25, 5617, — 6 cannot govern an encl. pron.; if such a pron. is affixed to the prep. it always belongs to the governed subst.: 6-š zäyısn until his birth 44!2; frāc ör-Sän deh vénam I foresee for their country 504; — in certain cases 6 is replaced by the adv. avis (g. v.). — Represents both Av. (163) ava, OP ava, and Av. (180 sqq.) avi, ao; MPrthPrs ’w; Paz. ó. The ideogr. KN originally rep- resented MIr (MPrthPrs) 6h < Av. (171 sq.) avada, OP avadä ‘thus’; in BP, having lost its final -%, it is used as 6, but chiefly
143
Ohurmazd
— Av. (1044) nava-; MPrth nw’g; MPrs nwg; Paz. nó, nu; NP nau.
Notar [nwtl] one of the forefathers of Vištaspa, Av. (1037) Naotara-, also the name of the clan and its domicile (in East Iran) 4317. 5017. 5315; v. further s. v. Rdg.
Nötärän [nwt'ln'] patron. of Notar 1148.
nózdahom [nwzdhwm; 19-wm] the nine-
teenth.
nin [KN] now, —-ic 41919 ete.; —-ip 5319 v.s. v. -p(i); tài ~ til now 719; andar 6 ~ until now 4014; hac ~ frdc from now on 6112; ~ ka now that 1098.
— MPrs nwn; NP niin, ak-niin.
as a prev. — % 39% read v, g. v.; ’wey 1091” = 6-cz (encl. -c).
+6dak [**wd*k'] the name of a river, probably an affluent of the Euphrates 117’, v. Nyberg, Karlgren Vol. 320-324. — MS and ed. ’wsk'.
ögön [^wgwn; HKYN 467] so, in such a manner, in such à way; (running) as follows 1916, 11812; ~... kū so ... that HajB:9. 81!; ~ cigón SO ... as 25? ete.; ~ homänäk cigon (or kt), v. homänäk; ne ~-1c not even so, not even if that be the case 46". — < pron. ava- (v.s. v. 62) + gon < Av. (482) gaona- ‘hair’ and ‘colour of the hair’, then ‘colour’ in general; inser. ’wgwn; MPrth ’w’gwn; MPrs "wn, wn = ä’ön; Paz. awa < *auvón < "auyon.
*ögräi [^wgl'y] the act of dipping down, of the scales of the balance: kč héc kustak ~ nē kunēt (the balance) which does not go down on either side, which maintains perfect equilibrium 72%. — < ava + gräy-, v. grätan; v. BSOAS XVII, 1955, 247 n. 1. No reading marks in Cod. K, but Sanjana marks the -g-.
Ohurmazd [’whrmzd] 1. the name of the Supreme God, OP Ahuramazdah, passim ;
www.parsianjoman.org | ool wok
Ohurmazd
dātār ~, passim; ~ apazonik (q. v.); ~ + x"atài 1222, 745. 75%. "7922, 85H. 894. 12015; ~ bag 2117. 22%; rēc + ~ the first day of the month 95%. — 2. the star of Jupiter 510-12, 77, — 3. n. pr. of human beings: a) the king ~ son of Shapuhr 165—179. 11618; ~ son of Artaxsér 11617; b) a Mobad 1104. — Av. (285 sqq.) Ahura- Mazdāh- in two separate ws.; inser. Prth 'hwrmzd; Prs ^whrmzdy, but as n. pr. of an ordinary man hwlmzdy (KZ); MPrth Prs ^whrmyzd (*whrmzdbg ‘the primordial man’); Paz. Hormezd (Hurmazda and other forms); NP Hur
```


### [2026-09-07T20:37:07.457Z] TOOL RESULT

```
##### leaf 420
ایولز
ایو اد « بانانی مجهول بر وزن شیرازه
بمعتی آراسته و بیراسته باشه ۱ .
بسعنی ابواز است که آراسته و پیراسته باشد ۳ .
الوان ه بروز نکوان . صقه و طاق را
بند ۴ ,:
ابوانس بفتح‌اول وسکون ثانی‌وثالث
بالف کشیده و نون مکسود بین بی‌نقطةٌ ده .نام
##### leaf 421
و شش لت و نات
بیان اول
با - , دمعم مع است که‌بجهت عصاحت
باشد - ویمعنی به بفتح بای ابجد - و مضاف به
اسامی آشها مانند ماست باوزیره با و کدوباوامثال
آن ۱ - و مخفف باد و باشد» هم هست .
بااوش « با حمزء بواو رسیده بر وزن
پاپوش » خیار بزرکی باش دکه بجهت تخم نگاه
##### leaf 422
۱ بابادشاه دست زدن ۱ متشه د<
است؛ و این صفیر بجهت تعظیم است .
پا یل » یکر الك بر وزن قابل , بلفت
بونانی نام ستار هشتری بباشد ۵ - و بسنی
مشرق را یز کویند - و نام شهری است مشهود
در وسط عراق ٩‏ » و عراق وسط عالم است پس
باین اعتبار بایل مر کز دابرة عالم باشد وازمداین
مبعةٌ عراق عرب است » و در کنار فرات‌برجااب
##### leaf 423
بت ۷۲۰۳ ح-
قلعهٌ آن شهر بوده چاهی است عمیق . گویندحاروث
و ماروت در اتحاه محبوی آند» و جضم الث حم
هقلح آنتتته. :
یا بو نه ‌ با تای‌فرشت مر وزن بالوده ۰
کوزة پرآب را کویند . وباین معنی بجای حرف
ثالت تای قرشت هم آمده است .
با بو 4 - با نون بروزن وارونه .کیاهی
##### leaf 424
ودریجة کوچك را گوند» وظاهراً ابن لفت‌باجهك
است که مصفر باجه باشده و باجه مخفف بادجه
و پادجه بمعنی باد گیر و باد گیر جایی و دوزنی
را کویند که باد از آنآمدو شد نماید واله‌اعلم .
۱ باجه پفتح جیم بروزن راجه ؛ دربچه
و دوژنه (۱) بزر که را گوشد ۱ . ۱
باحور با حای حملی بروزن کافور »
بخاربر| گوین که درهوای کرم از زمین‌برخیزد-
```


## [2026-09-07T20:37:15.712Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"papa\\|pāpak\\|Papak\\|pāp\\b\" BQT_v1_pages.txt | head -20\necho \"=== leaf numbers containing باب  ===\"\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'باب' in p and 400<i<440:\n        print(i, [l for l in p.split('\\n') if 'باب' in l][:6])\nEOF"
}
```


### [2026-09-07T20:37:17.024Z] TOOL RESULT

```
=== leaf numbers containing باب  ===
407 ['و اماننه و آزرده را نز گویند ؛ و بابددانت', 'می\u200cبابد فای سعفض یز تبدیل مییابد چنانکه در']
415 ['اول نیشاپور است ۷ . از پادشاهان بابل هم بوده است', 'بابکان » بزر کترین شهرباران: شاپوراول. شاپور دوم ؛ انوشرهءان داد کر دردورتاسلامی\u200cسلسله\u200cهای:']
418 ['چون مار را بخورد شفا بابد » و بعربی\u200cبقرالوحش']
421 ['شايسته و درخورباشد چنانکه کوبند :«فلانی باب', 'باره وحق نیز هست همجنانکه گونند :9 در باب', 'باب بانات بالفکشیده ,پر ٩\u200f']
422 ['۱ بابادشاه دست زدن ۱ متشه د<', 'پاب\u200cدن بروزن باد زن» سیخ کباب\u200cرا', 'اوبود واو رابدان سب اردشیربابکان گفتندی ۴ -', 'فیروزه هرت که آنرا شهر بابکی میگونند-', 'و صفیی باب هم هست چنانکه مامك تصفیر مام', '۱ - چون : بابالاهر . بابلجعفی , پایا افضل  .\u200f ۴ - بیونانی ۳60683 «اشتینگاس» .']
423 ['باییزن - بروژن\u200cتاییدن» بمعنی بابیزان']
424 ['بقلم آ قای اقبال وداثرةالمعارف اسلام. \u200f ۷ - رل: بابوئه . ۸ - باج و باژ و باز باین معنی', 'پرستندة آذر زردهشت. همی\u200cرفت باباژ و برسم بمشت . فردوسی\u200cطوسی «مزدیسنا۲۵۳ببمد»']
425 ['نیکی را گربند» وبابای فارسی هم آمدماست ۷ -']
432 ['و ب میباشد , و علاج آنرابچیز های سرد بابد']
434 ['چیزی حمجو : حندوبار ودربابار و جویبار واأمثال', 'بابارگرفته . ۱٩\u200f - اباری راگویند که بجپت']
439 ['کلمه پیداست که بابد از «باد» مشتق باشد نه از «باز» و تاچار کلمه در اصل «بادییج» بوده وبلملای']
```


## [2026-09-07T20:37:22.753Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==422' BQT_v1_pages.txt\necho \"#################### leaf 421\"\nawk 'BEGIN{RS=\"\\f\"} NR==422' BQT_v1_pages.txt >/dev/null\nawk 'BEGIN{RS=\"\\f\"} NR==423' BQT_v1_pages.txt | tail -30"
}
```


### [2026-09-07T20:37:24.084Z] TOOL RESULT

```
و شش لت و نات
بیان اول
با - , دمعم مع است که‌بجهت عصاحت
باشد - ویمعنی به بفتح بای ابجد - و مضاف به
اسامی آشها مانند ماست باوزیره با و کدوباوامثال
آن ۱ - و مخفف باد و باشد» هم هست .
بااوش « با حمزء بواو رسیده بر وزن
پاپوش » خیار بزرکی باش دکه بجهت تخم نگاه
دارند - و خوشه کوچك انگور را نی زگویند .
پاپ « بسکون بای ابجد » بمعنی
شايسته و درخورباشد چنانکه کوبند :«فلانی باب
فلالی است * معنی‌شابستةٌ فلالی است - و بمعنی
باره وحق نیز هست همجنانکه گونند :9 در باب
فلانی > بعنی درحق فلانی ودربار فلالی‌سوبمعنی
پدرهم آمده اس تکه‌بمربی والد کویشد ؟ » وباین
ممنی بلفت زند وپازند (۱) پابای فارسی باشد ۴
و مربی درخانه را گویند ۴ .
باب بانات بالفکشیده ,پر ٩‏
و جد را گوبندکه پدر پدر و پدر ملدر باشد -
(۱) چك : ژئد و بازند .
9 بپردومعنی مذ کور؛ رك: ایا ۰
۴ - دزفولی‌شا..
۵ اشکاشمی 92۵29۶ ۰ دخی
بقنه درسفحهٌ ۲۰۲
( بر های فاطع۴۰ )
#################### leaf 421
یا بادشاه دست‌ردن کنابه از
برابری با پادشاه کردن باشد درهمه چیز .
با بادی ‏ بارای فرخت بروزن‌ناهاری»
ملفت بونانی ۴ قلفل سیاه راگونند که در آش
بر کیرد هر کز آبستن نگرده .
پاب‌دن بروزن باد زن» سیخ کباب‌را
گوند مطلقا » خراه آهنی باشد خواه چوبی ۰
با باك « بروزن‌ناوك » بمعنی امین‌واستوار
باشد و بادشاه عظ‌الشانی که اردشیردخنرزادة
اوبود واو رابدان سب اردشیربابکان گفتندی ۴ -
و پرورنده و پدر را نیز گویند ۴ - و نوعی از
فیروزه هرت که آنرا شهر بابکی میگونند-
و صفیی باب هم هست چنانکه مامك تصفیر مام
۱ - چون : بابالاهر . بابلجعفی , پایا افضل  .‏ ۴ - بیونانی ۳60683 «اشتینگاس» .
دك ۱ ص ٩۲۰۱‏ . ؟ - پپلوی ۳20۵1 « تب رکه ۱۷۰ » ۳۵۵۵8 نام پسی ساسان
(52520 موبد معبد اناهید دد استخر) ؛ و او نیز بشفل پدر متصوب کشت و وی پدر اردشیراول
موسی سانالیان است .۶ کریسئنشن . ساسان ۸٩‏ * . ۴ - باين ممنی‌مر کب‌از: یاب(پدر)
- 2 (پسوند دال برعزت و محیت) , و موف در آخر همین لفت مجددا آنرا یادکرده است .
۵ درسربانی ال با 61 ستارهشتری است. ۱ - بابل , در زبان‌بابلی "1۷ - 9۶ - 82
بمعتی باب ابل یمنی باب‌الة با دروازة خدا ؛ در اوستا 180۷۴ و در پارسی‌باستان ( کنیبییسنون)
۷ (حالت مفعول فیه از (21۳۷) , ,ثقل توربة (سفرتکوین ۱۱ : )٩‏ شهربابل را از
آن‌جهت لین نام خواندند که خدا در آنجا زان همه ماکنان زمین را مخلوط کرد ( پلیل )
«نفی» ولي صحیح همانت که مذ کور شد . شهر بابل یکی از شهرهای مهم اکد ۸۵80 ودر
ماحل فرات واقع و بعداً پایتخت درلت بابل کردید و در زمان هخامنشیان بکی از چهار پابتخت
ايران بود.. و نیز بدائرة المعارف اسللام رجوع شود .
بقیه ازصفحهةٌ ۲۰۱
8 سنکلیی ۰02۷۵ سریکلی02» بودعا۳2۵ (یدربز رکه) « کربرسن۷4* » کیلکی ودزفولی
4 بمعنی پدربز رکث. امادرلهجة اخیر طبقات بالاومتوسط «باباهرا بمعنی‌پدر اسعمال کنند و پدر
بز رکمرا 880 202 گویند . درلانینی ۳3۳8 و درنازی‌هم باباستممل است «تفی» -
هت مامات اس وبابا خر تومشوئی . چوخوانمت استر. سنابی‌غزلوی .
```


## [2026-09-07T20:37:53.293Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB pap ===\"\ngrep -n \"Pāpak\\|Papak\\|pāpak\\|p'pk\\|Päpak\\|pap\" NYB_vol2_glossary.txt | head -20\necho \"=== NYB page150 locate ===\"\npython3 - <<'EOF'\nt=open('NYB_vol2_glossary.txt',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if '\\n150\\n' in p or p.strip().startswith('150'):\n        print('leaf',i,p[:200].replace('\\n','|'))\nEOF"
}
```


### [2026-09-07T20:37:54.564Z] TOOL RESULT

```
=== NYB pap ===
875:azd [’zd] information 187; proclamation 202-9. — Av. (228) azda = OP; OAram. lw. ’azdä Dan. 2°, pap. 'zd; MPrthPrs "zd (S); Arm. lw. azd.
878:bag [bg, bk'; inser. bgy, Prs RHY”, Prth ’LH?] 1. god 381! [bk', a quotation from Y. 1019]; pl. eas. obl. —-an [bg?n!] 75! (opp. dēvān). 1131?; garān —-än kof the mountain of the mountain gods 20? (v. s. v. gar). — 2. lord: Ohurmazd ~O. the Lord, of the supreme god 211’. 2224; — of kings: Käyös ~ 458; ~ Päpak HajA:4. B:4. SPrs:8. Prth:8; ~ Artaz- šahr HajA:3. B:3. SPrs:6. Prth:6; 1091, 111%; ~ Sähpuhr HajA:1. B:1. SPrs:4. 11. Prth:4. 6. 8. P1:1. P2:9; ~ Ohurmazd P1:3; ~ Xēsrēi 10921; pitar ~ P1:10; — pl. cas. obl. —-än [SRHY?-n, bg'n'] as a pl. majestatis: öisän —-ān Šahpuhrv P 2:8, without the king's name Pl:4; šmāh ~-dn addressing the king
1612:gal [gl] coll. the gang, the villeins labouring on the estates of the kings, the satraps, the magnates, etc.; in war their military crew 207; pl. cas. obl. ~ -an + Kirm the attendants of K. KnS VI, 8 = KnA p. 275. — OP *garda- attested by the Bab. lw. gardu in deeds and docu- ments of the Achaemenian epoch (a gardu-patu = OP *garda-pati- is also mentioned), and by the Aram. lw. grd? in the Fayyum pap., v. Driver, Doc.,
1692:Gor-ArtaxSér-x"arrah [gwl 'Ithšdi GDH] town in Pars built by Artaxsér 1 Papakan 11615, — Cat. 94, where references to other sources are given; I mention: KnS IV,
1754:expressed (nominal sentence as in the Semitic languages): man Sähpuhr hom 154; tē ke he? 737; to rād ke Dugdav he 4721. en rētak ke hast? who is this boy? 1617; Artaxsér ... nē pat giyāk hast 6?" sq.; kë zan-& hac õi hucihrtar nest ‘qua pulchrior non est mulier', who is the most beautiful of all women 259-19; ēzšān amüh hem ke ... we are of those who 5723-24, šmāh ke xtēn het 6111; sagr hend 86%, — 3. in the 3d p., together with a subst. virtually in dat., or with a pron. in cas. obl., it expresses ‘to possess’ xdnak i-t hast the house that belongs to thee 5325-26; fradandan i-5 hast the chil- dren he has 142; with ràd as in NP: Papak rüd pus-é hast 3?. — 4. Together with verbal or other nouns it forms periphrastic verbal expressions, e. g. han- dešitar vicītār hom 125; frēftār hah 3419; matür hom 46’; kartar hom 101?’; brihenäk hend 7777; ke (cas. obl.) vitīrišn nest which is incorruptible 66°; tö hän-ic äkäh he this thou knowest 399; hayyär hend they help 106%; -š hayyaréh hénd they help him 1001-12; pat kamēstārēh + spihr hénd they offer resistance to the. Sphere 8721; ké (cas. obl.) Mihr u Mah pat pust hah which M. and M. protect 317-8, ete. — 5. auxiliary vb. forming compound tenses: būt hom, būt hend I was, they were, eto., v. Grammar; notice: HWH-nd, regularly hend, must stand for the subju. händ 14? (fut.). 335 (cond.). — 6. Wrong use of the ideogr. HWH-: a) HWH-wm for the encl. pron. lst p. sg., added to the pret. pass. in order to emphasize the agent-
1804:is analysed (pp. 6.26 sqq.), regarded this as the original form and derived it from ham + bav- (būtan), comparing MPrs hmb’w ‘rival’ (S, also MirMan III. 14). It may, however, represent, and be read, hmb’g = ham-bäg as well, from Av. (952) bäga- ‘loft, share’; Aram. lw. (pap. Cowley and Kraeling) hnbg in the phrase hngyt w hnbg = hangēd w*hanbag ‘own- ing cattle and real property jointly with another’, Eilers, AfO XVII, 333a (MPrth h’mgyh < *häma-gaida-, MHC); MPrth ^mb?g ‘comrade, rival’.
2135:ka [MT], with encl. ’MT-m = ’MT-t = ka-t, °MT-š = ka-š ete.: 'MT-e = ka-c: A. conj. when, as, while; because; though, whilst; if; that. 1. temporal: standard type of period referring to the past: Pāpak ka-š hàn saxtan āšnūt kas fréstit by P. when by him this word was heard a man was sent = when P. heard this he sent a man 21!; passim; if con- taining an encl. pron. the apodosis is introduced a) by adak + encl., e. g. api-n ka én tigr vist adak-in . . . vist and when We shot this arrow, We shot it ... HajB: 4-6; 545-5; — b) by api- + encl., e. g. ka hac star frac būt api-š ... guft kū then he said 60?*; — c) by the independent forms of the enclitics: am, at, aš, aman, atān, ašān: hän étén amavandeh + ka zivandak bit hom am bit that great vigour which was mine when I was alive 345-6; ka giyāk-ē päh i gospandan vēnēnd ašān avd sahét when they see somewhere a flock of sheep it will seem astonishing to them 9724-25; — the apodosis may be introduced by adak alone (v. this w.); by pas (914-*); by andar han in the meantime (561°); — ka ... apāc àyet aš Kat-Xosroi bē 6 patirak āyēt ka pat vài našast ēstēt when he comes back he will
2343:*kurtīk, pl. cas. obl. kurtīkān [kwltykn!'] villeins, slaves or bondmen employed in different occupations on, an estate: ~ šu- pānān slave shepherds 1°. — I follow the reading of Antiä, whose text reproduces the basic MS of Kn, that of Mihrapan (v. I, p. XII). S. has kurtān ‘Kurds’ (ef kurtān šāh KnS V, 1). Itis of course pos- sible that ~ is ultimately derived from the national name of the Kurds, who were notorius nomad  cattle-breeders (BQ notices kurd in the sense, inter alia, of cūpān(ān) and gēsjand-carān) but it cannot have an ethnie sense here. The narration presupposes that Sasan was a slave within easy reach of Papak, to be summoned. into his presence at any mo-
2346:ment, not a Kurd to be fetched from some more or less distant Kurdish tribe. The w. kurtik must then, be a generic designation of slaves of the estate, and may etymologically have nothing to do with the Kurds. The gang of slaves war scrambled together from widely different nationalities (v.s.v. gal). Thus it was quite natural that Papak, to whom Sasan was but a slave of unknown nation- ality, should ask him whether there had been any king among his forefathers (212-13).
2421:a-mast ‘not intoxicated’ and (1447) vi- bayha-, explained in Phl by yuvat hac has mast ‘intoxicated without wine’; NP bang borrowed in Arab as banj. I main- tain my former interpretation, which Bthl. also had, seeing in this narcotic some sort of hemp, i.e. hashish. The full treatment of the question must be reserved for a special paper.
2941:Päpak [p’pk'] the father of King Arta- xščr, receives the naked title King (MLK? = šāh): HajA:4. B:4. ŠPrs:8. Prth: 8; 1-3 passim. — NP bab, baba ‘father’.
2943:Papakan patron. of Päpak: Artaxšer 4 ~ 11. 6%, 1091, 1169-16; belonging to Papak: Staxr + ~ 10719,
3198:2räd [l’d; inser. and Ps. Pdy] postpos. l. for the sake of, because of, for, on behalf of, in favour of (7220-21), con- cerning (37?. 2919 etc. passim); ham cim ~ for that very reason 512-13, 671-2; han cim ~ 342, & ~ 795. 9626, 982° for that reason; ēt ~ cé because (conj.) 773-5; ce ~ why? 3511. 795; õi ke ~ for whom 183; — preceded by an inf. or a v. n.: in order to, for the purpose of, because: ditan i Zartuxšt ~ (in order) to see Z. 4777, 5218-19; ves avis matārēh i xrat ~ because more wisdom had been allotted to him 9041-12; — forms together with hac or pat a frame preposition: hac bim i Artaxšēr ~ for fear of A. 1525; 3719. 4612-19; hac hin cim ~ 118%; kirpak i pat dat ~ kart for the sake of Law 6419; pat omet +... ~ in hope of 1211917; pat hän cim ~ cé because (conj.) 10421-22, — 2. used as in NP: a) ‘to, for’: cahārpādān ~ ap hamë dat 1419; Papak ~ héc fradand ne būt P. had no child 19; 32-4, 422;  ménam to ~ nevakeh 4771, v.s. v. méni- tan; 427; frazand i zu&s m kar u kirpak bē- dimoxtan 652-23; — b) denoting the dir. obj. of the pres. tense: hakar né han ~ <apdc> dārēt if you do not abjure that (religion) 191; 2520-21; 453; — c) denoting
3369:sahikéh [s’hykyh] resplendence, magni- ficence 1052. — Abstr. of sahik ‘resplendent magnificent’, also ‘showy’, v. PR 32%, PT 166"; NP sahi ‘fresh, young; erect (of a cypress)’, v. Kanga in a (typed) paper on the PT passage, 1953, p. 11. From sahistan.
3578:šah [šh; MLK?, Prs inser. MRK?] king, ruler, regent; placed after the name of the king or the ruler: Däräi ~ 61°; Päpak ~ HajB: 4; Vistasp ~ (often -šh written in one word with the name), passim; after the name of the governed people, country, or town: Sakän ~ P1:2. P2:4; Käpul ~ 8?; 1167-1178, passim; — dturčin ~ the supreme religious authority
3592:šahridar ([Str'yd’l, štr'd'l, Prs inscr. Stldl-] ruler, of Pāpak as the Arsacid sub-regent of Pars 1°; of the emperor of Rome (Byzance) 17°; of the high officer sent by the Indian king to the Sassanid court 118°. 1215; pl. cas. obl. ~-dn of the highest class of the Sassanian society, the governors, or vice-roys HajB:5. — Prth. official language hstrdr-, v. xšahr- idar; Ps Stld’! ‘king’; MPrth Shra’r; MPrs šhry'r; Paz. saharyär ; NP šahriyār.
4015:Anahit Pērikhanian, to whose paper in REA, N.S.V, 1968, 9—30. reference is made here once and for all.
4360:to summon a p. to one’s side 2?-3-12, 56, 104 ete.; without 6 pes 625, 73. 315; Ohur- mazd ast hac damik ... x“ahét O. will call up the bones from the earth 100'2-13; vas a«vāhišn (q.v.) i rüpak-karihà xvāhēt he clamourously utters many implorations 7426-27, — 3. to ask, to demand: pat zan ~ to marry a wife 675; pat zanéh ~ to ask in marriage 1165-5; hac Papak past (g. v.) u zinhär xvāst 214; 3 rēc jamān x“äst he solicited a time of three days for consideration 11819; 121%; mizd dātihā ~ to demand reward righteously 8120-21; hac x"at karap margēh 4 Zartuxšt x"àst, apar cé āivēnak margēnītan he asked the karap himself about the manner of Z.'s death, how to put him to death 4812-13; sāi u baz ~ hac to exact tribute from 177. 58%; Pourušasp hàn hom hac Dugdāv apāc x"àst P. asked D. to give him back that Haoma 42?4-25,. 4, to seek,to search,to look for, to ponder, to strive to attain: api-ščin hàn hom x"àst they searched for that Haoma 409; pat ~ 4 hàn i či zuarrah in striving to attain his Glory 4614, more fully + an inf: api-š hàn xarrah bē aydftan x“dst 4618; — with an abstr. subst. as its obj.: v. cärak, ddrišn, dösäram, hucasmeh, ken, panäh, zivišn, ete.; cf also s. v. az"àyisneh. — Olr *hväz-, MPrth wx'št, pres. wz?z-; MPrs xw'stn, xwh-; Paz. NP z"üstan audah-; Verbum 187; Ghilain 69; Bailey, BSOS VI, 1930, 74. V. also x“dstar, -ēh, zuäyısn, -ēh.
4627:Abbreviations 234 Abbreviations OAr Old Aryan sg. singular OAram Old. Aramaic Skr Sanskrit obj. object Skr. v. Sanskrit version OInd Old Indian st. stem OIr Old Iranian st.abs. status absolutus OP Old Persian subj. subject opp. opposite, opposed to subju. subjunctive opt. optative subst. substantive (ist, 2nd, 3d) p. person suff. suffix . sup. superlative pap. PEE S. V. (sub voee) under the word pass. passive S patr. patronymic Ww be ne t Paz Pazand - tads (ern) ers. pron. ersonal pronoun ; à Phi Pahlavi SUE ROE pl. plural . pos. positive Talm Talmud(ic) poss. possessive th. thing | postp. postposition trans. transitive prec. preceding pref. prefix ult. (in ultimo) in the end of the prep. preposition page pres. present tense pret. preterite v verso (of a folio) prev. preverb var. various reading, variant pron. pronoun vb. verb, pl. vbs. — verbs Prs Persian WIr West Iranian Prth Parthian viz. (videlicet) namely Ps. Psalms pt: participle w. word, pl. ws. = words r recto (of a folio) rel. adv. relative adverb Yt Yašt
7029:bab, baba: Papak
=== NYB page150 locate ===
leaf 165 �� Paz. pédq-bar ‘apostle’ (SGV); Ps. ptw*mbPn id. (v. above); NP paiyam-bar, payam- bar.|paitištan [p?ytyšt'n', pyt?yšt?n', pytyšt?n'] leg 407-8. 5616, 933. — Borrowed from Av. (837) paitistána-.|pai
```


## [2026-09-07T20:37:54.841Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB entry 147 ===\"\ngrep -n \"^ *147\\.\\|147\\. bāb\\|147\\. bab\" HUB.txt | head\necho \"=== HUB bab ===\"\ngrep -n \"bāb \\|papak\\|bābā\" HUB.txt | head -20"
}
```


### [2026-09-07T20:37:54.914Z] TOOL RESULT

```
=== HUB entry 147 ===
=== HUB bab ===
```


## [2026-09-07T20:38:03.061Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('NYB_vol2_glossary.txt',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if \"Päpak [p’pk'] the father\" in p or 'Päpak [p’pk' in p:\n        print('LEAF',i)\n        print(p[:600])\n        print('...tail...')\n        print(p[-400:])\nEOF"
}
```


### [2026-09-07T20:38:04.324Z] TOOL RESULT

```
LEAF 165
�� Paz. pédq-bar ‘apostle’ (SGV); Ps. ptw*mbPn id. (v. above); NP paiyam-bar, payam- bar.
paitištan [p?ytyšt'n', pyt?yšt?n', pytyšt?n'] leg 407-8. 5616, 933. — Borrowed from Av. (837) paitistána-.
paitiyärak [pytyd’Ik'], patiyärak [ptyd^lk'] everything that counteracts and checks the good powers: adversaries, of the evil powers 421, 7117; wicked devices 667°, 70%. 8325; scourge 661. 861°. — Borrowed from Av. (840) paityära-.
paitiyarakéh counteraction, resistance
7918, paitiyär-käreh [—-k'lyh] the act of doing harm 37H.
pak [DKY?] clean, pure 922. 94?; hamén $ ~ full summer 94?; ~ bütan hac to
...tail...
n.org | perl wb
pardaxtan
151
Pirs
and Covetousness and the devils re- mained slain and finished (destroyed) M 4708-7 (S); to be ready with, to get rid of (hac): Vištāsp ka hac kārēcār i apāk Arjāsp pardaxt būt as soon as V. had got to the end of the war with A. 1088; [bë ~ to be taken away from (hac), to be refused: xYarišn hac zan i dastän bē pardacét food is taken away from, refused to, a menst
```


## [2026-09-07T20:38:11.015Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -c \"\" MON_part1.txt\ngrep -n \"بابک\\|باب (\" MON_part1.txt | head -20\necho \"--- search papak latin in MON ---\"\ngrep -n \"Pāpak\\|Papak\\|pāpak\" MON_part1.txt MON_part2.txt | head"
}
```


### [2026-09-07T20:38:11.117Z] TOOL RESULT

```
99339
4954:فرزندی: اردشیر بابکان (اردشیر پسر 
4955:بابکک)» خسرو قادان «(خسرو بسر قاد). 
9385:منسوب به ارباب (در فارسی مفرد به حساب 
19641:بابک: ۱2۳-۴ [مصف. باب] (.) پدر (به 
48198:جلو: تا (.) سیخ کباب (چوبی یا آهنی). 
59987:( کتاب)» باب (کتاب). موضوع مطلب. 
--- search papak latin in MON ---
```


## [2026-09-07T20:38:11.567Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls -la incoming/ARY/ 2>/dev/null | head\necho \"=== ARY bab ===\"\ngrep -n \"بابا\" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-07T20:38:11.649Z] TOOL RESULT

```
total 9468
drwxrwxr-x  3 sfmqrb sfmqrb    4096 Sep  4 14:06 .
drwxrwxr-x 23 sfmqrb sfmqrb    4096 Sep  4 14:06 ..
-rw-rw-r--  1 sfmqrb sfmqrb 8102112 Sep  4 14:06 ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  586473 Sep  4 14:06 ARY_latin_index_pages.txt
-rw-rw-r--  1 sfmqrb sfmqrb  960497 Sep  4 14:06 ARY_pages.txt
drwxrwxr-x  2 sfmqrb sfmqrb   20480 Sep  4 13:30 ARY_pages.txt.pages
=== ARY bab ===
2920:۲ / بابا (واژه‌ی کودکانه به چم"پدر")
5318:۱ ایسلند ی کیره (۸0 ۲ باباایی 5 صا۵): 998999 ۶080800
```


## [2026-09-07T20:38:16.904Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '19600,19660p' MON_part1.txt"
}
```


### [2026-09-07T20:38:16.962Z] TOOL RESULT

```
فرهنک فاررسی معین 


۳۳۳ 
حکیمان: باباافضل, بابا کوهی باباجعفر» 
باباطاهرر 


بابابزرگ: 02028 (.) (ص مر . امر 0( 
بدربز رگ نیا. 


بباباشمل: امصصمک- 0203 (ص. ۱.) (عسم 0( 
لو طی» داش مشدی. 

باباغوری: آءتارقاقه [ - - باباغری» باباقری 
باقوری] (امر.) (عم.) قسمی کوری که چشم 
آماسیده و به رنگ چشم گوسفند مرده شود 
یعنی بزرگتر از حد عادی گردد. کسی که 
تخم چشم او بررآمده و نفرت‌انگیز بود و او 
را شوم دانند. کوره تاببنا. قسمی مهرة مدذور 
سیاه و سفید که برای دفع چشم‌زخم بر 
کودکان او یز ند. 

بابانوئل: 202-061 (امر.) در اصطلاح 
کودکان؛ ببری که به شب اول سال مسجان 
جامةٌ نو و شیرینی و بازیچه برای کودکان 
آرد؛ قس. بابانوروز. 

بب‌ابانوروز: 9212-۷7 (امر.) در 
اصطلاح کودکان پیری که به شب نوروز 
(شب اول سال) جامةٌ نو و شیرینی و بازیچه 
برای کودکان آرد؛ نظیر پاپا نوئل مسیحیان. 
بابت: ۱1 اغ. بابة ] (.) شایسته» سزاواره 
از در» درخور. از بات در حصوص؛ در 
عوض. به حساب. همطراز» همسر » نظیر . 
بایزن: ۱0 )۱( سیخ کباب خواه آهت 
باشد یا چوبی. 

بابک: ۱2۳-۴ [مصف. باب] (.) پدر (به 
تحبیب). 

بابل: ۵1 (.) مغرب؛ مق. خراسان به 
معنی مشر ق. 

بابو: 205 رقس. باب] (.) پدر بابا. بزرگ 
قلندران و درویشان. به معنی بابا که در اوایل 
اسماء برای شفقت با مجرد تلقیب افزایند و 
گویند. 

بابونه: (۵-)02ا0ق0 | بایونج؛ معر.] (.) 


۳۳۴ 


فرهنگ فارسی معین بایی
```


## [2026-09-07T20:38:17.455Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/ARY/ARY_pages.txt',errors='replace').read()\ni=t.find('بابا (واژه')\nprint(t[max(0,i-2500):i+1500])\nEOF"
}
```


### [2026-09-07T20:38:18.676Z] TOOL RESULT

```
سه (۳88(07): 1 5 (118۳) ۸/700
اسپانیایی (۸/18[3ط6): ۸01 برهان قاطع : 1۹۳
ایتالیایی (۷(فله)): 011
[pdf page 99]
۰ / ایرمان (به چم "مهمان"» "دوست")
اوستایی (/۵۲57): ۸۵180 رال۸۱/۸ ۸18۷ پسگشت‌ها 5
پارمی باستان (۷(فا2878 صا0): 28/۸ 7 ۶۸005200
پهلری (۲7ماتنهم): 83۸1۸0۲ ,۸۳58۸۸201 5 (۲81310) . :۸/۸215
اوستی (0558716): ۸ ,1110 برهان قاطع + 1۹۶
سانسکریت (7ل6۸(۶82): ۸27۷۸۵۸ فرهنگ معین : ۴۵
ایرلندی کهن (3نق1 صا0): ۸138611 ب8ل۸ لفت‌نامه دهخدا: ۳۷۷
: یادداشت: ‏ "
۱ ۱- چم این واژه در ایرلندی کهن: اشرافی» رادمرد. (جالب اینکه در پهلوی نیز واژه‌ی 58 به چم "رادمرد" و
آقهرمان" بود).
چم این واژه در زبان اوستایی؛ پیشوای دینی,
۲- چم واژه‌ی 88۸/۸77177 در زبان پهلری: دوستی.
اوستایی (/4۳874): ,11511۸17 لاتین (4770ل): ,5710885 ,870 ,81870
71 572 ,57۸۷۷۸71 5 57235
پارسی باستان (/2587814۸ 00): ,11187۸71 گرتبکه (007/6): را الا ان
۸0۸ ایسلندی‌کهن (۸۸ 10۸۲ید ضان):
پهلری (7ماتلم): ,87۸00۸
۸ ,88737۸0 نررس کهن (2/07858 07.0): را ان
کردی(شاید) (07821877): لاله ادن ساکسونی کهن (542:07 صضا0): ,87۸8۲0۸31
تخاری 8 (8 [(۸ل7022147): 578 ,57226 نان
سانسکریت (7ل87712:)4(/58 ,7118771۸71 فریزی کهن (/لها۶۸75 2ا0). ۱ 5۸0۸
آرمنی [4/۸48/14۸): انا ان هو
بونانی (07658): ,ل1115720۸ ,11157884 آلمانی کهن (058۸440 2۷/04 صان):
را با ان ,57۸31۸ ,5721
‌‌
[pdf page 100]
مج ددددددددددددددررررررررررججممججا
: با(به چم به همراه و "مع!) / ۱۰۱
آلمانی (0280/200): دا ان لیتوانی (7714(/400): ,8701 ,تا[8071
انگلیسی کهن (ن8(08 0۵): 87030۸3۲ 1 اد رده نج
انگلیسی (7ل5لا8(70): نکن لتونی (لتی) (/701۵ا): اد
دانمارکی (0۸۸/157): آنه57۸ ایر لندی کهن (للولقا صضاه):
سرئدی (81780/57): 8 ,1851108
نروژی (۸0877801۸7): (الرا ون پسگشت‌ها 5 ۲27
حلدی (ب0070): ۸ رن نس
اسلاری کهن (4۲//0ا5 7ل#6تانزه 012+ 9 (87۸30) ی
71 ,97۸10 ,857۸7 5 38811 8۲8۴) ههام05
لهستانی (۳07.15): 57۸ 4 (87۸30) :۸۸5/218
روسی ((551۸): ان 235 نقحلاه
چکد (280): ان 63 (857۸0) :0/0075
برهمی (80[78(11۸01): 1 7 (87۸0) +7
اسلرا کی (5].01۸/0): پا ان برهان قاطع : ۱۹۷
یادداشت: أ
ُایستادن" و زمان‌های گوناگون آن در اکثر زبان‌های هند و اروپایی معنی خود راکم و پیش حفظ کرده‌اند و اشتقاق ا
همه‌ی آنها از واجریشه‌های هند و اروپایی این فهرست است.
| گس سروالی اسر ی ۷686
اوستایی (4587۷): 6 و38۸7 ,82 چکه (ط220): 1۲
پپلوی (تماتلهم: ۰ ۸826 م۸۳ لیترانی (4۸1۸2ا 777 ): ‎٩‏ ,85
کردی (080157): 8۸ پروسی کهن (۷/فا۳۸/55 010): ۱1:1
3 مانسکريي, (87/7/شک): 2
ارمتی (45(/100(ه) یا ۰< ۸3 ب8۸ پسگشت‌ها 5
گرتیکه (00770): ۳۱" 2۸ 8 ۶0080
آلمانی کهن ((520/۸ 0ات صا): 0 (۲178) :2 2/(ع ماد
۸ ,لا8] 3 013 0
اسلاوی کهن (ع۲1ها5 نات 0ا0): برهان قاطم: (ابا) ۷۶
320 فرهنگ معین : ۳۳۶
لهستانی (۳0(1./8): 2۸ :
[pdf page 101]
۲ / بابا (واژه‌ی کودکانه به چم"پدر")
یادداشت:
معین اين واجریشه در برخی زبان‌های هند و اروپایی: با» برای؛ سپس.
کردی (62/5[4): ۸3۸ لهستانی (7ل5ا۳0): 7170
برنانی (07655): ۸ چکه (لل525): 717۸
لاتین (۸7120ل): ۸ ب28۳۸ پسگشت‌ها کیت یت
فرانسه (4ل۳8(/0): 7/۸۸ زر ۳
اسپانیایی (5۳۸۸/]977): ۳/۸ 3 (7۸71838) ۸0
پرتغالي (۳0870010238): 7۸ برهان قاطع + ۲۱
| جم‌انگلیس سروازی اش ۷۵
اوستایی (4۷887۸(۷): ایتالیایی (۵ل7۸): ۷0
۸ ا۷۸17 ,۷۸70 ۷۸2۵ رومانی (80۸۸(۷۵): ۷7 ۱
پهلری (۲7شاللمهه): اه پر تغالی (۳0/70183): ۷0
کردی (28015]4)). 2 گرتیکه (007710): 5
بلوچی (/1ع/ل8۸): زر ایسلندی کهن (/(1۸/ 5۸010۸ صاه):
آفغانی (پشتو) (470[7۸۷1): را ۷
تخاری 4 (۸4 7۸74۷ل70): ۷۷۸۸۷7 ,۷۷۸۸۲۲ نررس کهن (ظ۸08 012): الا
تخاری 8 (8 ۸ل7001۸). ان دوه سا کسونی کهن (542:0(0 010): ۷0
سانسکریت (54(/5۴8/7): ,۷87۸8 ,۷87۸ فریزی کهن (۸ما5ل2 (0): 0
۷۹7 آلمانی کهن (/02704۸0 ۲۲/0/۲ 012): ,۱۷۷130
برنانی (۸581:)0827 ,۸5 7
51 ,۷271405 آلمانی ((05/0/۸): زالان
لاتین (07/00): ۷۳۳۲71۲۸38 ,۷83۷7۲78 انگلیسی کهن (0/./3ل20 ۰:0 ۷3۵0
فرانسه (4لع/۳82۸): ۷7 انگلیسی (/8(/01/8): (الارا
اسپانبایی (82۸//3): ۷0 دانمارکی (0۸۸/157): ۷۳0
[pdf page 102]
بار (به چم "دفعه "و "نوبت") / ۱۰۳
سرئدی (352(13[7): ۷0 ولزی (1ک )+ ان ورن
نروژی (/۸/0070501۸2): ۷10 برتونی (888670): لا نراد رود
هلندی (007617): الا هت (۳۷/77772): نج ایا رد۱
اسلاوی کهن (8677نابل) 2ا0):

17 ۷۳30 ,ت۷۳78 پسگشت‌ها شرت د دا
لهستانی (01(3: ۷ یس
روسی (551۸4): ۷ 38 (130) بویا
چک (7ل280)): الا 2 ۷8۲۱ :25 ازم 205
بوهمی (80778(1142): 3 ۱ 0 (130) دا مد ها
اسلوا کی (51074): ۷ 7 (۲130) 683 ,67 :002/5
لیتوانی (۸]۷ه
```


## [2026-09-07T20:38:48.467Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK 847 ===\"\ngrep -n \"Page(s): 847\" POK_full.txt | head\npython3 - <<'EOF'\nt=open('POK_full.txt',errors='replace').read()\nimport re\n# find lemma blocks with Page(s): 847\nparts=t.split('Root / lemma:')\nfor p in parts:\n    if 'Page(s): 847' in p:\n        print('LEMMA:',p[:80].replace('\\n',' '),'|| PAGE line ok')\nEOF"
}
```


## [2026-09-07T20:38:49.423Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN leaf for p.103 (leaf=103+24=127) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==128' SYN.txt | head -50"
}
```


### [2026-09-07T20:38:49.962Z] TOOL RESULT

```
=== POK 847 ===
69195:Page(s): 847 
69338:Page(s): 847-848 
LEMMA:  ptel(e)ia   Meaning: a kind of tree   Material: Gr. nrsAsa, epidaur. nsAsa 'elm || PAGE line ok
LEMMA:  pu-1, peu- pou- a\so phu-  Meaning: to blow, blow up   Material: Old Indie /0/7 || PAGE line ok
```


### [2026-09-07T20:38:51.188Z] TOOL RESULT

```
=== SYN leaf for p.103 (leaf=103+24=127) ===
fr. hus-fru, epd. of hus ‘house’ and fru ‘mistress’, like NHG hausfrau, Du. huisvroww.
Sw. make, fem. maka, ME make prop- erly ‘mate’ : OE gemecca ‘mate’ gem- On ee well matched’, etc., these : niece ene , ete. Falk-Torp 689. Be ehlamoct ‘Spouse! , with echt ‘maria oun sooo eae es ae a .35) and genoot ‘com-
y genosse, etc.
a CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
OHG hiwo ‘husband’, hiwa ‘wife’, OF hiwa ‘wife’ (Goth. heiwa-frauja ‘master of the house’) : Lett. steva ‘wife’, Lat. civis ‘citizen’, Lith. Seimyna ‘family’, OF ham ‘home’, etc., all fr. IE *ke7- ‘lie’ in Grk. xeZua, etc., whence the notion of ‘home, household’ and also its master or mistress. Walde-P. 1.359. Walde-H. 1.224. Feist 253 f.
NHG gatte, whence fem. gattin, fr. MUG gate ‘companion’, here also Du. gade now used mostly for ‘wife’ : MLG gaden ‘be suitable’, OE gegada ‘com- panion’, td gedere ‘together’, Goth. ga- dilligs ‘cousin’, etc. Walde-P. 1.531 ff. Weigand-H. 1.628. Franck-v. W. 172.
OHG gimahalo ‘bridegroom, hus- band’, gimahala, gimala ‘bride, wife’, MHG gemahele masc. and fem., NHG gemahl, fem. gemahlin, fr. OHG mahal ‘contract’, esp. ‘marriage contract’ : Goth. mafl ‘place of assembly, market’, OE mepel ‘assembly, speech’, etc. Walde-P. 2.304. Weigand-H. 1.671.
7. ChSl. sapragt, fem. sqpraga (in Gospels ‘yoke, pair’, late ‘spouse’) with SCr., Russ. suprug, supruga, fr. epd. of prega, presti ‘yoke, harness’. Miklosich 262.
ChSI. mal(z)zena, dual ‘husband and wife’, cpd. of Zena ‘wife’, first part Gmc. (: OHG mahal, etc., above, 6) or malt ‘little’, as prefix of affection? Hence Boh. manzel, manzelka, Pol. malzonek, malzonka, etc. Berneker 2.13.
Boh. choi’ ‘spouse’, used for either ‘husband’ or ‘wife’ : ChSI. chott ‘lover, beloved’, fr. chotéti ‘wish’. Berneker 398 f.
8. Skt. bhartar- ‘husband’, bharyd- ‘wife’, lit. ‘the sustainer’ and ‘the one sustained’, fr. bhr- ‘bear, carry’ : Grk. épw ‘bear’, etc.
Skt. dara- ‘wife’, etym. dub. Uhlen- beck 124.
Cede
Digitized by Arya Samaj Foundation Chennai and eGangotri
98 SELECTED INDO-EUROPEAN SYNONYMS
2.38 MARRY (Partly distinguished as a) take a Wife; b) take a Hus
```


## [2026-09-07T20:38:59.682Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 132 133 134; do echo \"##### leaf $n\"; awk -v N=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==N' SYN.txt | head -30; done"
}
```


### [2026-09-07T20:39:01.024Z] TOOL RESULT

```
##### leaf 132
 | Lat. coniugium, conutnin Dan. giftermaal, egte; bryl- Lett.  precéSands, lauliba; | tie ie ChSl. 6; rie 1 ) | : oe Sw. iftermdl, dkta; brél- .  brakit (maliizentstvo | een zoned, es SCr.  brak, Zenidba (2), Fr. see a oats 0: bodas OE weddung, sinscipe; udaja (b); svadba Bienes. cecil gifta, brgdhlop Boh. manielstvt, stiatek, Rum. Fe ranas ME  weddyng, wedlok, Zenitba (a), vdavky It. eh nak mariage (b); svatba a priodas; neithior NE marriage (wedlock); Pol. -malzenstvo, Slub; we- Br dimezi; eured wedding : sele : ; f Du. huwelijk, echt; brut- Russ. brak, supruzestvo, ze- loft nit'ba (a), zamu- OHG  hirat, éwa; britlouft Zestvo (b); svad’ba MHG hirdat, é(we); britlouft, Skt. vivaha-, patitva-, etc. hohzit Av. nairiéwana-
NHG heirat, ehe; hochzeit
Of the words entered, the majority, like NE marriage, cover both the state and the act of marriage (marriage as an institution, or the marriage took place). A few are used only for the married state, as Lat. matrimonium, NHG ehe. Many words are used only for the cere- mony, as NE wedding in its present usage. Such words are added, but separated by a semicolon.
In some cases there are distinct words for ‘taking a wife’ and ‘taking a husband’, corresponding to the dis- tinctive verbs (2.33). These are simi- larly indicated by a and b.
Most of the words for ‘marriage’ are obvious cognates (derivs. or in some cases the source) of the verbs for ‘mar- Ty’ and have been noted in the discus- Sion of the latter (2.33). Buta few, and many of the special words for the wed- ue ceremony, are of different origin. ae ee lit. OR ae (2.31), : . coniu(n)x ‘spouse en the usual legal term itehbecs ae , and nuptial ‘wedding’ ( >
= Seg see under nibere (2.33). : mmonium (>It., Sp. mat
##### leaf 133
ri-
monio), fr. mater ‘mother’, and orig. re- ferring to the woman’s lawful mother- hood, married status, as opposed to con- cubinage.
Sp. boda(s), ‘wedding’, fr. Lat. vota ‘vows’. REW 9458.
2. Ir. lanamnas, deriv. of lanamain ‘married couple’, deriv. of lan ‘full’. Pedersen 2.62. Stokes 293 (as cpd.).
W. neithior ‘wedding’, fr. Lat. nup- tidlia. Pedersen 1.236. Loth, Mots lat. 190.
Br. eured ‘wedding’, fr. Lat. drdatio ‘prayer’. Pedersen 1.203. Cf. Sp. bodas, above.
3. ON bradkaup ‘wedding’, cpd. of brad ‘bride’ and kauwpa ‘buy’, referring to the gifts made to the bride, and re- flecting the older custom of purchasing a wife. Schrader, Reallex. s.v. Braut- kauf.
ON bridlaup, brullawp, Dan. bryllop, Sw. bréllop, OF brydhlop, OHG, MHG britlouft, Du. bruiloft ‘wedding’, epd. of brid, etc. ‘bride’ and laupa, etc. ‘run’, referring to the ceremonial fetching of the bride, this ultimately reflecting a primitive chase or robbery of the bride.
. ee CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
102 SELECTED INDO-EUROPEAN SYNONYMS
Schrader, Reallex. s.v. Raubehe. Falk- Torp 109.
OE, beside usual weddung, rarely wedlac ‘pledge’ and ‘espousals’, whence ME wedlok, NE wedlock, fr. wedd ‘pledge’ with suffix -ldc, orig. same as lac ‘gift, etc.’. NED s.v. wedlock.
OE sinscipe, cpd. of sin- ‘everlasting’ and scipe ‘condition’, hence lit. ‘perma- nent state’. Cf. sinhtwan ‘married couple’.
OE @w, OHG éwa ‘law’ (21.12) and lawful married state’, MHG é(we), NHG ehe, Du. echt (MLG echt > Dan. egte, Sw. dkia). Falk-Torp 183. Wei- gand-H. 1.405 f.
MHG honhzit, lit. the ‘high time’, used of festivals like Christmas, Easter, also of the ‘marriage festival’, as NHG hoch- zeit. Weigand-H. 1.875. Sperber, Hin- leitung 42.
4, Lith. svodba (formerly usual word for ‘wedding’), fr. Russ. svad’ba (be- low, 5).
Lett. laultba ‘betrothal, marriage’, fr. laulat ‘betroth’, this from Esth. (or Liv.) loul ‘song, betrothal song’ (Finn. laulaa ‘sing’). Mithl.-Endz. 2.428.
Lett. kazas ‘wedding’, fr. Esth. kaza ‘husband’. Mihl.-Endz. 2.206.
5. ChSI. braki (in the Gospels always of the marriage at Cana, the ‘wedding’, but there is no opportunity for any other use), SCr., Russ. brak, prob. fr. berq, b
##### leaf 134
rati ‘take’, IE *bher- ‘bear’) , orig.
‘taking the bride’, like ‘lead the bride, marry’ in Lith. vestz, etc. Berneker 81.
ChSI. malizZenisivo (late), Boh. man- Zelstvt, Pol. malzensivo : ChSl. maltizena ‘married couple’, Boh. manzel ‘husband’, etc. (2.31).
Boh. smatek, orig. ‘union’ : sntti OBoh. snieti, pple. sat, ChSl. sinetz ‘take down, take together’, cpd. of sz ‘with’ and jeti ‘take’. Gebauer 1.381. Berneker 429.
Pol. glub ‘vow’ (= Boh. slib ‘vow’), hence also ‘betrothal’ and ‘marriage’ : poslubié ‘betroth’, cpd. of lubié ‘like, love’. Hence OLith. salubas, OPruss. acc. sg. saliban ‘marriage’. Berneker 757 £. Briickner 531.
Russ. supruzestvo, fr. suprug ‘spouse’ (2.31).
SCr. svadba, Boh. svatba, Russ. svad’ba ‘wedding’, deriv. of ChSl. svatt ‘kins- man’ (: possessive svojz), then ‘one who promotes the marriage, matchmaker’, as Russ. svat, Pol. swat, ete. Miklosich 332.
Pol. wesele ‘wedding’, formerly ‘mer- riment’ : ChSI. veselije ‘merriment’ vese- li ‘merry’ (16.22), Briickner 607.
6. Skt., beside vivdha-, ete. fr. vah- ‘marry’, also patitva- ‘husbandhood’, janitva- ‘wifehood’, also pani-graha- lit. ‘grasping the hand’ (of the bride), pari- naya- (cf. pari~ni- 2.33), etc.
Ay. ndirifwana-, lit. ‘wifehood’, fr. nairi- ‘wife’.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
1 ‘ ae In Public Domain. Gurukul Kangri Collection, Haridwar
2.35. ‘Father’.
1. IE *patér-, prob.
Digitized by Arya Samaj Foundation Chennai and eGangotri
MANKIND: SEX, AGE, FAMILY RELATIONSHIP 103 2.35 2.36 2.37 FATHER MOTHER PARENTS
Grk. tari pnrnp Toxets, rexbvres, ryovets
NG jwarépas untépa yovets 7
Lat. pater mater parents
It. padre, babbo madre, mamma genttort ;
Tr. pere mere pere el mére
Sp. padre madre padres
Rum. até mama padrin{t
Ir. athir mathir tuistidt
Nir. _ athatr mathair tuismhightheoira
W. tad mam rhient
Br. tad mam tad ha mam
Goth. atta (fadar) aiper bérusjos, fadrein
ON fadir mooir fedgin
Dan. fader moder foraldre
```


## [2026-09-07T20:39:06.639Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==136' SYN.txt | head -40"
}
```


### [2026-09-07T20:39:07.911Z] TOOL RESULT

```
Lett.  téus mate vecaki
ChSl. _ otict mati rod ‘tela
SCr. _otac mati roditeljt
Boh. _ otec matka, mdtt rodite
Pol. ojciec matka (maé) rodzice
Russ. olec mat! roditelt
Skt. —_ pitar- méatar- pitarau, malarau
Av. pitar- matar- pitara
2.36. ‘Mother’. 1. IE *mdter-, prob.
starting fr. a nursery word of the pa type (above, p. 94) orig. pd, reduced to pa before the accent. Walde-P. 2.4. Here belong the Grk., Lat., Ir., Gme., and Indo-Iranian words, also Arm. hair, and Toch, A pacar, B pacer. In Balto-Slavic it is completely replaced. 2. Nursery words that have become oe usual terms. Type baba (above, p. ) in It. babbo, now a serious rival of padre, nes atta, tata (above, p. 94) in Rum. an ., Br. tad, Goth. atta (So reg., Vs. ihe) te and here not of earthly » Lith. tévas, Lett. tévs, OPruss.
taws, ChSl. otict , 3 , ete. (all the Balto- Slavic forms), Hitt. fae aad
starting fr. a nursery word of the ma type. Walde-P. 2.229. Here belong the Grk., Lat., Ir., Gme. (except Goth aipei), Balto-Slavic, and Indo-Iranian forms, also Arm. mair, and Toch. A macar, B macer. But Lith. moté became ‘woman’, and as ‘mother’ was replaced by the deriv. motyna.
2. Nursery words that have become the usual terms. Type mama (above, p. 94, Walde-P. 2.221) in It. mamma a serious rival of madre, and W., Br. mam.
Goth. aipei, prob. new fem. formed fr. some nursery word similar to, though not identical with, atta ‘father’. Feist 28.
Digitized by Arya Samaj Foundation Chennai and eGangotri
104 SELECTED INDO-EUROPEAN SYNONYMS
2.37. Words for ‘parents’ are fr. verbs for ‘beget’ or ‘bear’ (4.71, 72); fr. words for ‘old’; or are pl. or du. forms (the lat- ter, of course, more orig.), or derivs., of words for ‘father’, or rarely ‘mother’.
1. Grk. roxets (so reg. Hom.), or aor. pple. rexdvres : rixrw ‘beget, bear’ (4.71).
Grk., NG yovets : yiyvouat ‘be born’, yevvaw ‘beget, bear’ (4.71).
2. Lat. parentés (also ‘ancestors’, late also ‘relatives’), pres. pple. of par- in parere ‘bear, beget’ (4.72). Hence Rum. parinti ‘parents’, Fr. parents formerly ‘parents’ and ‘relatives’ (> ME paren- tes, NE parents), now ‘relatives’ (as ‘parents’ replaced by pére et mére), as also It. parenti, Sp. parientes. REW 6233.
Lat. patrés (as also Grk. rarépes) was commonly used for ‘forefathers’ and oc- casionally in late times for
```


## [2026-09-07T20:39:15.971Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN leaf for p.1110 (leaf ~ 1110/2+12 = 567) ===\"\nfor n in 565 566 567 568; do echo \"-- leaf $n\"; awk -v N=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==N' KLN_1966.txt | head -3; done"
}
```


### [2026-09-07T20:39:17.393Z] TOOL RESULT

```
=== KLN leaf for p.1110 (leaf ~ 1110/2+12 = 567) ===
-- leaf 565
orman-ize,  intr. and  tr.  v.,  Norman-iz-ation,  n.
Norn,  n.,  one  of  the  three  goddesses  of  fate  in Scandinavian  mythology.  —  ON.  norn  (pi. nornir),  rel.  to  Swed.  dial,  noma,  nyrna,  ‘to warn,  to  communicate  secretly',  ME.  nyrnen,  ‘to recite’,  MHG.  narren,  ‘to  growl,  snarl’.  All  these words  are  of  imitative  origin.
Norse,  adj.,  1)  Scandinavian;  2)  Norwegian.  — Obsol.  Du.  Noorsch,  ‘Scandinavian,  Norwegian’ (now  Noors,  ‘Norwegian’),  fr.  Noordsch  (now Noords),  ‘Nordic’,  fr.  Du.  noord,  ‘North’.  See next  word  and  cp.  Northman.
-- leaf 566
  Sir  Richard  Owen  (1804-92)  in  1848  fr. vcoxo.;  (also  vcotov),  ‘the  back’,  and  yopSr),  ‘a string’.  See  noto-  and  chord, notodontid,  adj.,  pertaining  to  the  Notodontidae ; n.,  any  moth  of  the  family  Notodontidae.  — See  next  word.
Notodontidae,  n.  pi.,  a  family  of  moths  ( entomol .) —  Formed  with  suff.  -idae  fr.  not-  and  the  stem of  Gk.  68cov,  gen.  686vxo<;,  ‘tooth’.  See  odonto-. Notogaea,  n.,  a  zoogeographical  realm,  com¬ prising  the  Australian,  New  Zealand  and  Neo¬ tropical  regions.  —  Gk.,  compounded  of  v6 to;, ‘the  south  wind,  the  south’,  and  y aicc,  ‘earth’. The  first  element  prop,  means  ‘the  rainy  wind’, and  is  rel.  to  votio;,  voT£p6;,  ‘damp,  moist’, voxtc,  ‘moisture,  damp’,  voxtcc,  ‘moisture, rain’ ;  see  natation  and  cp.  Notus.  For  the  second element  in  Notogaea  see  geo-, notonectid,  adj.,  pertaining  to  the  Notonectidae-, n.,  one  of  the  family  Notonectidae.  —  See  next word.
Notonectidae,  n.  pi.,  a  family  of  aquatic  insects (entomol.)  —  ModL.,  formed  with  suff.  -idae  fr. noto-  and  Gk.  vt)xt7)<;,  ‘swimmer’.  See  necto- and  cp.  words  there  referred  to. notoriety,  n.,  1)  the  quality  of  being  notorious; 2)  a  well-known  person.  —  F.  notoriete,  fr.  ML. notorietatem,  acc.  of  notorietas,  fr.  notorius, ‘well-known’.  See  next  word  and  -ity. notorious,  adj.,  well-known,  widely  known  (usu¬ ally  in  an  unfavorable  sense).  —  ML.  notorius, ‘well-known’,  fr.  L.  notus,  ‘known’.  See  know and  cp.  words  there  referred  to.  For  the  ending see  suff.  -orious.
-- leaf 567
 alpha¬ bet. —  Gk.  vu,  shortened  fr.  Heb.  nun,  name  of the  letter  n.  See  nun,  the  letter, nuance,  n.,  a  slight  difference.  —  F.,  ‘shade,  hue; a  slight  difference’,  fr.  MF.,  fr.  nuer,  ‘to  shade’, fr.  nue ,  ‘cloud’,  fr.  L.  nubes  (see  nubilous  and -ance);  so  called  with  reference  to  the  different colors  of  the  clouds.
nub,  n.,  a  knob,  lump  (rare)  —  Cp.  LG.  knubbe, ‘knob,  protuberance’,  and  see  knob,  knub. nubble,  n.,  a  small  nub.  —  Formed  fr.  nub  with dimin.  suff.  -le.
Derivative:  nubbl-y,  adj.
-- leaf 568
 numeralis,  ‘of  numbers’,  fr.  L.  numerus. See  number,  n.,  and  adj.  suff.  -al.
Derivative:  numeral,  n.
numerary,  adj.,  pertaining  to  a  number  or  num¬ bers.  —  ML.  numerdrius,  fr.  L.  numerus.  See number  n.,  and  adj.  suff.  -ary. numerate,  v.,  to  count;  to  enumerate.  —  L.  nu- meratus,  pp.  of  numerdre.  See  number,  v.  and  n., and  verbal  suff.  -ate.
```


## [2026-09-07T20:39:18.097Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN pact/peace/pagus ===\"\ngrep -n \"^pact,\\|^peace,\\|^pagan,\\|^propagate,\\|^pale,\\|^pastor,\\|^pasture,\\|^pantry,\\|^company,\\|^potent,\\|^power,\\|^possess,\\|^possible,\\|^paternal,\\|^patriot,\\|^pope,\\|^papa,\\|^father,\\|^food,\\|^feed,\\|^fur,\\|^pattern,\" KLN_1966.txt | head -40"
}
```


### [2026-09-07T20:39:18.165Z] TOOL RESULT

```
=== KLN pact/peace/pagus ===
14518:feed,  tr.  and  intr.  v.  —  ME.  feden,  fr.  OE.  fedan, rel.  to  OS.  fihljan,  ON.  feeda,  OFris.  feda, OHG.  fuotan,  Goth,  fodjan,  ‘to  feed’,  Goth. fodeins,  QE.fdda,  ‘food’.  See  food.
15559:fur,  n.  —  ME.  forre,  furre,  ‘fur’,  orig.  ‘covering’, fr.  furren,  ‘to  cover’.  See  fur,  v. fur,  tr.  v.  —  ME.  furren,  fr.  OF.  forrer  (F.  four- rer),  ‘to  cover’,  fr.  OF.  fuerre,  forre,  ‘sheath, case,  covering’  (whence  OF.  furrel,  F.  fourreau, of  s.m.),  fr.  Frankish  *fddr,  which  corresponds to  OPIG.  fotar,  fuotar,  ‘a  cover,  coverlet’.  Cp. It.  fodera,  ‘covering,  lining,  sheathing’,  which is  also  a  Teut.  loan  word,  and  see  fother. Derivatives:  furr-ed,  adj.,  furri-er,  n .,  furri-er-ed, adj.,  furri-ery,  n„  furr-ing,  n.,  furr-y,  adj.,  furr- i-ly,  adv.,  furr-i-ness,  n.
26926:pagan,  n.,  a  heathen.  —  ME.,  fr.  Late  L.  paganus, ‘countryman,  villager,  civilian’.  The  early  Chris¬ tians  called  the  heathens  ‘civilians’,  in  contra¬ distinction  to  the  ‘soldiers’  of  Christianity.  Late L.  paganus  derives  fr.  L.  pagus,  ‘district,  prov¬ ince,  village’,  prop,  ‘something  joined  together, something  united’,  fr.  I.-E.  base  *pag-,  *pak-, ‘to  join  together’,  whence  also  L.  pangere,  ‘to join,  make  firm’,  pax,  gen  .pads,  ‘pea.ee',  pacisci, ‘to  make  a  treaty’;  see  pact.  Cp.  F.  paten,  ‘pa¬ gan’,  which  also  derives  fr.  Late  L.  paganus.  Cp. also  paysage,  peasant.
26969:pale,  tr.  v.,  to  enclose  with  pales ;  to  enclose  with a  fence.  —  ME.  palen,  fr.  MF.  palir,  fr.  pal, ‘stake’.  See  prec.  word.
26970:pale,  adj.,  whitish,  wan.  —  ME.,  fr.  OF.  pale  (F. pale),  fr.  L.  pallidus,  ‘pale’,  fr.  pallere,  ‘to  grow pale’.  Sec  pallor  and  cp.  words  there  referred  to. Derivatives:  pale,  intr.  and  tr.  v.,  pale-ly,  adv., pale-ness,  n.
27199:pantry,  n.  —  ME.  panetrie,  pantrie,  fr.  OF.  pane- terie,  ‘a  place  where  bread  is  kept’,  fr.  ML. panetaria,  panitaria,  ‘a  place  where  bread  is made’,  fr.  L.  panis,  ‘bread’,  fr.  I.-E.  base  *pa-, ‘to  tend,  keep,  pasture,  feed,  guard,  protect’, whence  also  pa-bulum,  ‘food, 'father’.  See  food and  cp.  pabulum.  Cp.  also  panada,  panetela, panification,  pannage,  pannier,  pantler,  com¬ panion,  company,  impanate. pants,  n.  pi.  —  Abbreviation  of  pantaloons, pantun,  n.,  a  Malay  verse  form  consisting  of  four lines  rhyming  abab.  —  Malay.  Cp.  pantoum. paiiuelo,  n.,  a  kerchief.  — -  Sp.,  ‘kerchief,  hand¬ kerchief’,  dimin.  of  paho,  fr.  L.  pannum,  acc.  of pannus ,  ‘piece  of  cloth’.  See  pawn,  ‘pledge’,  and cp.  pane,  panel.
27202:papa,  n.,  pope;  parish  priest.  —  Eccles  L.  pdpa, ‘bishop;  pope’,  fr.  L.  pdpa,  ‘father’.  See  prec. word  and  cp.  pope.
27636:pastor,  n.  —  ME.  pastour,  fr.  OF.  pastor,  pastur, fr.  L.  pastorem,  acc.  of  pastor,  ‘shepherd’,  lit. ‘feeder’,  fr.  pastas,  pp.  of  pdscere,  ‘to  graze, pasture,  feed’,  which  stands  for  pd-scere  and derives  fr.  I.-E.  base  *pd-,  ‘to  tend,  keep,  pasture, feed,  guard,  protect’,  whence  also  L.  pd-nis, ‘bread’,  pa-bulum  (for  *pa-dhlo-m ),  ‘food’.  See food  and  cp.  words  there  referred  to. pastoral,  adj.  —  ME.,  fr.  L.  pastoralis,  ‘pertain¬ ing  to  shepherds’,  fr.  pastor,  ‘shepherd’.  See pastor  and  adj.  suff.  -al.
27641:pasture,  intr.  and  tr.  v.  —  Late  ME.,  fr.  OF. pasturer  (F.  paturer),  fr.  Late  L.  pastura.  See pasture,  n.
27662:paternal,  adj.,  fatherly  —  Formed  with  adj.  suff. -al  fr.  L.paternus,  ‘of  a  father,  fatherly’,  fr  .pater. See  pater  and  adj.  suff.  -al.
27767:peace,  n.  —  ME.  pais,  pees,  fr.  OF.  pais  (F.  paix), fr.  L.pacem,  acc.  of  pda:,  ‘peace’,  which  is  rel.  to pacisci,  ‘to  make  a  treaty’.  See  pact  and  words there  referred  to  and  cp.  esp.  appease,  pace, ‘with  the  leave  of’,  pacify,  pax.
29636:pope,  n.  —  ME.  pope,  fr.  OE.  papa,  fr.  Eccles.  L. papa,  ‘bishop;  pope’,  fr.  L.  papa,  ‘father’.  See papa,  ‘pope’,  and  cp.  papal,  poplin.
29752:possible,  adj.  —  F.,  tr.  L.  possibilis,  ‘possible  ,  fr. possum,  ‘I  am  able’.  See  possess  and  -ible. Derivatives:  possible,  n.,  possible-ness,  n.,  pos- sibl-y,  adv.
29816:potent,  adj.  —  L.  potens,  gen.  potentis,  ‘able, mighty,  powerful",  pres.  part,  of  posse  (for  potis esse),  ‘to  be  able’,  fr.  potis,  ‘able,  capable, powerful’,  which  is  cogn.  with  OI.  patih, ‘master,  husband’,  Toch.  A  pats,  ‘husband’, Gk.  ttooi?  (for  *7r6xu;),  ‘husband’,  Lith.  pads, pats,  ‘husband’,  Lith.  pats,  Lett,  pats,  Hitt,  pat, ‘self’.  Alb.  pata,  ‘I  had’  (imperf.)  pass,  ‘had’ (pp.)  and  the  second  element  in  Goth,  brup- faps,  ‘bethrothed,  fiance’,  and  in  L.  hospes  (for *hosd-pots),  ‘visitor,  guest’,  OSlav.  gospodi ‘lord,  master’.  Cp.  potence,  power,  puissant,  and the  first  element  in  possess.  Cp.  also  the  first  ele¬ ment  in  padishah,  Poseidon,  and  the  second  ele¬ ment  in  despot,  hospital,  host,  ‘landlord’,  Pra- japati.
29876:power,  n.  —  ME.  poer,  potter,  fr.  OF.  pooeir, pooir,  n.,  fr.  pooeir,  pooir,  v.,  fr.  VL.  *potere (corresponding  to  L.  posse).  See  potent  and cp.  words  there  referred  to.
30530:propagate,  tr.  and  intr.  v.  —  L.  propagatus,  pp.  of propagate,  ‘to  fasten,  peg  down,  to  set  slips;  to propagate",  fr.  prdpages,  ‘a  set,  layer  of  a  plant’, fr.  1  st  pro-  and  *pag-,  base  of  pangere,  ‘to  fasten, fix’.  See  pact  and  cp.  words  there  referred  to.
35137:power,  sorcerer,  saint’,  rel.  to  sidhyati ,  'reaches his  goal,  succeeds',  sadhuh ,  ‘right,  skilled,  ex¬ cellent;  a  holy  man’.  See  sadhu. siddur,  n.,  the  Jewish  prayer  book.  —  Mishnaic Heb.  siddur,  ‘arrangement,  order’,  fr.  sidder,  ‘he arranged,  ordered’,  Pi‘el  (—  intensive  form)  of sddhar,  which  is  rel.  to  Biblical  Heb.  sedher, ‘order’ ;  see  Seder  and  cp.  Scdra.  Siddur  in  the sense  ‘prayer  book’  is  an  abbreviation  of  siddur t^phillaf,  ‘arrangement  of  prayer’.  Cp.  the  term sedher  tsphillSth,  lit.  ‘order  of  prayers’,  used  as  a synonym  of  siddur.
```


## [2026-09-07T20:39:35.000Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^pact,\\|^pattern,\\|^pace,\\|^palette,\\|^peasant,\\|^pole,\\|^patronage\\|^patriot,\\|^food,\\|^father,\\|^possess,\\|^pacify,\\|^Pacific,\" KLN_1966.txt | cut -c1-700"
}
```


### [2026-09-07T20:39:35.068Z] TOOL RESULT

```
26876:pace,  n.,  a  step.  —  ME.  pas,  fr.  OF.  (=  F.)  pas, fr.  L.  passus,  ‘step,  stride,  pace’,  lit.  ‘a  stretching out  (of  the  leg)’,  fr.  passus,  pp.  of  pandere,  ‘to stretch  out’.  See  patent  and  cp.  pas,  passage, compass,  surpass,  trespass,  passport. Derivatives:  pace,  intr.  v.,  pac-er,  n.
26877:pace,  n.,  with  the  leave  of;  a  courteous  form  ex¬ pressing  disagreement.  —  L.  pace,  abl.  of  pax, ‘peace’.  See  pax,  peace.
27002:palette,  n.,  painter’s  color-board.  —  F.,  prop,  ‘a
29381:pole,  n.,  either  of  the  extremities  of  the  axis  of  the sphere.  —  ME.,  fr.  OF.  pole  F.  pole),  fr.  L. polus,  fr.  Gk.  776X0;,  ‘pivot,  axis,  pole’,  which stands  for  *q"'olos,  and  is  rel.  to  ttcasiv,  more usually  as  deponent,  7reXsa&at,  ‘to  be  in  mo¬ tion,  to  be’,  fr.  I.-E.  base  *qwel-,  ‘to  bend, turn’.  See  wheel  and  cp.  pulley, poleax,  poleaxe,  n.  —  Lit.  ‘head-axe’,  fr.  ME. pollax,  (cp.  LG.  pollexe);  compounded  of  poll, ‘head’,  and  axe.  The  spelling  poleaxe  is  due  to  a confusion  with  pole,  ‘a  piece  of  wood’. Derivatives:  poleaxe,  tr.  v., poleaxer,  n. polecat,  n.,  a  carnivor
```


## [2026-09-07T20:39:43.569Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"pact,  n\\.\\|pattern,  n\\.\\|patron,  n\\.\\|patriot,  n\\.\\|palette,  n\" KLN_1966.txt | cut -c1-900\necho \"=== printed page numbers near pagan ===\"\npython3 - <<'EOF'\nt=open('KLN_1966.txt',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'pagan,  n.,  a  heathen' in p:\n        print('LEAF',i)\n    if 'pact,  n' in p:\n        print('PACT LEAF',i)\nEOF"
}
```


### [2026-09-07T20:39:44.939Z] TOOL RESULT

```
8424:compact,  tr.  v.,  to  pack  together.  —  L.  compactus, pp.  of  compingere.  See  compact,  adj. Derivatives :  compacted,  adj .  (q.v.),  compact-er,  n. compact,  n.,  an  agreement;  a  covenant.  —  L. compactum,  ‘agreement’,  prop.  neut.  pp.  of compacisci,  ‘to  make  an  agreement,  form  a compact ,  from  com-  and  pacisci,  ‘to  make  a contract  or  agreement’,  which  is  rel.  to  pax,  gen. pads,  ‘peace’.  See  pact  and  cp,  compact,  adj. compacted,  adj.,  compact.  —  Prop.  pp.  of  com¬ pact,  ‘to  pack  together’.
8438:compatriot,  n.  —  F.  compatriote,  fr.  Late  L.  com- patriota,  fr.  com-  and  Late  L.  patridta,  ‘country¬ man,  patriot’.  See  patriot, compeer,  n.  —  ME.  comper,  fr.  F.  compair,  fr.  L. compar,  ‘equal  to  another’,  fr.  com-  and  par, ‘equal’.  See  peer.
13320:-eous,  adjectival  suff.  meaning  ‘of  the  nature  of’. —  L.  -eus  as  in  ligneus,  ‘of  wood,  wooden’  (fr. lignum,  ‘wood’,  see  ligneous).  Cp.  -ous. ep-,  form  of  epi-  before  a  vowel, epact,  n.,  the  excess  of  the  solar  year  over  12 lunar  months  (chronol.)  —  F.  epacte,  fr.  Late L.  epacta,  ‘an  intercalary  day’,  fr.  Gk.  feax-rai (scil.  T,|i£pat,),  ‘intercalary  days’,  fern.  pi.  of inamip,  ‘added,  intercalated’,  verbal  adj.  of inafzw,  ‘to  bring  forward,  add,  intercalate’,  fr. ini  (see  epi-)  and  aye'.v,  ‘to  lead’,  which  is  cogn, with  L.  agere,  ‘to  drive,  set  in  motion,  lead’.  See agent,  adj.,  and  cp.  words  there  referred  to. eparch,  n.,  1)  governor  of  an  eparchy;  2)  bishop of  an  eparchy.  —  Gk.  gmxpxo?,  ‘commandor, governor’,  fr.  ini  (see  epi)
18833:impact,  tr.  v.,  to  press  firmly.  —  L.  impactus,  pp. of  impingere,  ‘to  strike  against’.  See  impinge, impact,  n.,  a  striking  together;  collision;  the force  of  a  collision.  —  L.  impactus,  fr.  impactus, pp.  of  impingere.  See  impact,  v. impaction,  n.  —  L.  impactid,  gen.  -onis,  ‘a  striking against’,  fr.  impactus,  pp.  of  impingere.  See  im¬ pact,  v.,  and  -ion.
26899:Derivative:  packet,  tr.  v. pact,  n.  —  ME.,  fr.  MF.  pact  (F.  pacte),  fr.  L. pactum,  ‘contract,  covenant’,  prop.  neut.  pp.  of paciscor,  pacisci,  ‘to  covenant,  make  a  treaty, agree,  stipulate’,  rel.  to  pax,  gen.  pads,  ‘peace’, fr.  I.-E.  base  *pak-,  *pdg-,  ‘to  join  together, unite,  make  firm,  fasten,  fix’,  whence  also  L. pangere,  ‘to  join,  make  firm’,  pagus,  ‘district, province,  village’,  pagina,  ‘strips  of  papyrus fastened  together,  page’,  pains  (for  *pak-slos), ‘post,  stake’,  OI.  pas-,  pasa-,  ‘cord,  rope’,  Avestic pas-,  ‘to  fetter’,  Gk.  7n)yvtSvat,  ‘to  fix,  make firm,  fast  or  solid,  to  harden,  freeze’,  n ayrj, ‘snare,  noose’,  lit.  ‘anything  that  fixes’,  7tayoi;, ‘something  solid;  mountain  peak,  rocky  hill’, Tiayio;,  ‘solid’,  Tt 
27002:palette,  n.,  painter’s  color-board.  —  F.,  prop,  ‘a
27710:patron,  n.  —  ME.,  ‘patron;  pattern’,  fr.  MF.  (  = F.) patron,  fr.  L.  patronum,  acc.  of patronus,  ‘pro¬ tector’,  fr.  pater,  gen.  patris,  "father’.  See  father and  cp.  padrone,  patroon,  pattern,  which  are doublets  of  patron.
27719:Derivatives: patter,  a., patter-er,  n.,patter-ist,  n. pattern,  n.  —  ME.  patron,  fr.  OF.  patron,  ‘patron.
=== printed page numbers near pagan ===
PACT LEAF 180
PACT LEAF 287
PACT LEAF 416
LEAF 593
PACT LEAF 593
```


## [2026-09-07T20:39:59.345Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',errors='replace').read().split('\\f')\nfor i in (566,567,592,593,594):\n    p=t[i]\n    nums=re.findall(r'\\b1[01]\\d\\d\\b',p)\n    print('leaf',i,'first80:',p[:80].replace('\\n',' '),'| nums:',nums[:12])\nEOF"
}
```


### [2026-09-07T20:40:00.733Z] TOOL RESULT

```
leaf 566 first80:   Sir  Richard  Owen  (1804-92)  in  1848  fr. vcoxo.;  (also  vcotov),  ‘the  b | nums: ['1058', '1059']
leaf 567 first80:  alpha¬ bet. —  Gk.  vu,  shortened  fr.  Heb.  nun,  name  of the  letter  n.   | nums: ['1080', '1060', '1061']
leaf 592 first80: ddling,  moderate,  indifferent,  tol¬ erable',  orig.  ‘being  half-way  up  th | nums: ['1108']
leaf 593 first80: n.,  a  genus  of  plants  of  the  staff-tree family  (bot.)  —  ModL.,  compou | nums: []
leaf 594 first80:   n. paginal,  adj.  —  Late  L .paginalis,  ‘pertaining  to  a page’,  fr.  L.  | nums: ['1114', '1113']
```


## [2026-09-07T20:40:15.640Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '27719,27721p;27002,27004p' KLN_1966.txt | cut -c1-800\necho \"=== patriot ===\"\ngrep -n \"patriot,  n\" KLN_1966.txt | cut -c1-500\necho \"=== peasant ===\"\ngrep -n \"peasant,  n\" KLN_1966.txt | cut -c1-500"
}
```


### [2026-09-07T20:40:15.730Z] TOOL RESULT

```
palette,  n.,  painter’s  color-board.  —  F.,  prop,  ‘a
thin  piece  of  wood',  diminutive  formed  fr.  L. pala,  ‘spade,  shovel’,  which  is  of  uncertain  ori¬ gin.  It  is  perh.  rel.  to  L.  palus,  ‘stake’.  See  pale, ‘stake’,  and  cp.  pallet,  peel,  ‘baker's  shovel’.  For the  ending  seo  suff.  -ette.
palfrey,  n.,  saddle  horse  (archaic).  —  ME.,  fr. OF.  palefrei  (F.  palefroi),  fr.  ML.  palafredus, dissimilated  fr.  Late  L.  paraveredus,  generally supposed  to  be  a  hybrid  coined  fr.  Gk.  xapa (see  para-,  ‘beside’)  and  Late  L.  veredus,  ‘cour¬ ier’s  horse’,  which  is  usually  derived  from  Cel¬ tic  *  voredos ;  cp.  W.  gorwydd,  ‘horse’,  OIr.  ria- daim,  ‘I  ride’,  and  see  ride.  It  is  more  probable, however,  that  Late  L.  veredus  is  borrowed  fr. Heb.  peredh,  pheredh,  ‘mule’  (through  the  me¬ dium  of  Arab.-Pers.  bar  id,  ‘courier’).  OS.  perid, MDu.  peert,  paert,  Du.  paard,  OHG.  pfarifrit, pferfrit  (MHG  .pharvrit,phart,  G.  Pferd),  ‘horse’, are  borrowed  fr.  ML  .paraveredus.
Derivatives: patter,  a., patter-er,  n.,patter-ist,  n. pattern,  n.  —  ME.  patron,  fr.  OF.  patron,  ‘patron.
person  serving  as  an  example,  pattern’.  See  pa¬ tron.
Derivatives:  pattern,  tr.  v.,  pattern-ed,  adj., pattern-er,  n.,  patterning,  n.,  pattern-ize,  v., pattern-y,  adj.
=== patriot ===
8438:compatriot,  n.  —  F.  compatriote,  fr.  Late  L.  com- patriota,  fr.  com-  and  Late  L.  patridta,  ‘country¬ man,  patriot’.  See  patriot, compeer,  n.  —  ME.  comper,  fr.  F.  compair,  fr.  L. compar,  ‘equal  to  another’,  fr.  com-  and  par, ‘equal’.  See  peer.
27703:Derivative:  patrimonial-ly,  adv. patrimony,  n.,  anything  inherited  from  a  father  or an  ancestor.  —  ME .  patrimoigne,  fr.  OF.  (=  F.) patrimoine,  fr.  L.  patrimonium,  ‘an  estate  inher¬ ited  from  a  father,  patrimony’,  formed  fr.  pater, gen.  patris,  ‘father’,  with  suff.  -monium.  See  fa¬ ther  and  -mony  and  cp.  words  there  referred  to. patriot,  n,  —  MF.  (=  F.)  patriote,  fr.  Late  L. patriota,  fr.  Gk.  raxpuorr)?,  ‘fellow  cou
=== peasant ===
27783:Derivatives:  peart-ly,  ad v.,  pear-tness,  n. peasant,  n.  —  ME.  paissaunt,  fr.  OF.  paisant  (F. paysan ),  which  was  formed — with  change  of suffix — fr.  earlier paisenc,  fr.  pais  (F .pays),  ‘land, country’,  fr.  Late  L.  pdgensis,  ‘of  a  province  or district’,  fr.  L.  pagus,  ‘province,  district’;  see pagan.  OF.  paisenc,  paisant,  orig,  denoted  man of  a  country.  Cp.  paysage.
```


## [2026-09-07T20:40:17.351Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT pas- fetter ===\"\ngrep -n \"fesseln\\|paš-\\|pas- \" BRT.txt | head -20\necho \"=== IEC ===\"\ngrep -n \"^pak-\\|^pag-\\|^pa-\\b\\|^pater\\|^poti\\|^pa-ter\" IEC.txt | head -20"
}
```


### [2026-09-07T20:40:17.425Z] TOOL RESULT

```
=== BRT pas- fetter ===
4678:maca  *frast3niite  .  .  ditSi  °iiye  (NPm.)  .  .  'nyeke  räkWB  V.  7.4.  I  i)  wiederholt *vaäsäz*/ramravainti..vTspa^qmia  aiwi.'  'Aex  eine  .  .  der  andere';  dsityB  *'inyS'^ srurwai/i  (sd.)  K.60;  —  aivB  pants  yB  havam  {^d^  *daityö  ^'inyB^  ya'ia  *va  . . a^ahe  vTspe  'nyalhm  apatitqm  {%A.)  \.y2.  li.107;  P.57;  —  yal  he  pukra  us^zaydi^e 11;  —  ^pasävi^  adam  käram  ..fraisayam  , .  .  tiaisB  'nys  .  .  aat  'iiyB  ,  .  Y.5. 10;  — hyt^  upa  mäm  äkJ* , .  hyJ^  °niyJ'  kärJ'  avi  *'iiy3^^  suruiiraiti  (statt  Du.)  nsil  'inyS ".  .  reliquus  exercitus  . ."  Bh.^.6;  —  eä  'S. 24;  — yay^  osH  'nyS  rasnus  razUtB asti  masyB  ..  an^rn  datpm  ..upairi'tiyai^'W.J^.^'PüZ.  (unvollst  Zitat);  — \,°myam sraväis  .  .  !  .  .  ya'^a  zrayB  vountJtahm '  (näml,  käram)  *ustrabilrim  akunavam upairi  °nyh  äpB  V. §.32{.;  —  vayaol . .  'myahyJ  aspilf^A^ paiiyariayatn^'Acnem^a taratatB  (Stverz.)  'tiysis  (als  APn.)  dämqtt  \  Teil  (des  Heers)  machte  ich  kamelberit- Y.22. 24;usw.; —  \' a^urcrmazdämaiy  upas-  ten  .  ."  Bh.7. 18'';  5. 4;  —  armaeflä  'iiyA
4993:•  j.  a-vaeza-  Adj.  'silndlos,  sich  keiner Sünde  schuldig  machend':  "«^  dim  pas- 'alta  . .  fraca  syazJaySii  (sd.)  A.  j.  13;  13; —  °zS  aSa^hh  *frab»nta  dastra.tnasö (sd.)  paitiAarö  N.67;  6j.
7261:ya().         b)   eines  Nebensatzes:  yöi  nmäna kam.barSfnahi  (sd.)  .  ,  ätrsmca  .  ,  W  pas- ciota  ahe  nmänake  spä  vä  nä  va  in%yäi iüia  .  .  "wenn  wir  . ,  und  es  stirbt  dann . ., wie..?"  V.5.39;  Vd./();   —  yS  itarö  .. mpaidyeinte    .  .    ä'    ae^am    naram    afvS irtiyat    cvat  ..  V.5.27.'         3)  'lur    An- knüpfung eines  adversativen  Satzes  'aber; sondern;  vielmehr;  gleichwohl':  i'äa  main- yäe  dus^artnä^  .  .  ä°  azitn  manya  Yt.  10. 105  c;  —   nöii  .  .  vjspa  yazatinhö  .  .  ä' ..  aevd  zarä^usürä  Yt.  ij.  ig;  5,  55  aSt^^ ti-S3<  V-io.S,  ig.  5;  —  iä  fravasayS  . . acjifta     h^nti    .  .    yi    .  .    saosyantqm    ä° ai^alsqm  Jravasayö  (sd.)    .  .    Yt.  1^,  17; N,  I02;  — -  nahänazdiStö  ä'  havatam (sd.)  N.  i^;  p,  6-];    —    äs    zaotars  (sd.) kairim  ar^hath.ä'  AävanänS  {vä.m\.  kairim auAat)  yal .  .  N.  ■J2;  yS—yO,  66';  —  apa. •  •  y^  pora  ahmat  hiit?nta  .  .  3*  W  nürqm fratoHnü  Yt.ij.53f.;  $6,  5S;  —  aai{%'.Z) yakmai  xstiüts  Öavaiti  mihrS  ahmäi  jasaiti avairiie  ü.'  yahmäi  ßistS  bavatH  . .  ahmäi frasciruiayeiti  nmätamca  ..  YL/0.87, yeiihe  x^akrä^ia  nsU  aoüin  änAa  . .  para tthmat  yat    , .    ä°  yal    . .    ",  .  bevor  . aber  als  .  ."  Yt./().33f.; — yaj  Ae pu%, usjaysi^e  .  .  ikalsB  anyS  .  .  ä°    anyS  .  . \.g.io;    —  tar5.d»nanB  (sd.,  näml.  urva- rayä  ar^han)  .  .   ä'   vp?ma  agis.drajaT3h& N.90;  —  navajcsaparim  ..  aiwi^äme  ä' hama  mäzdräjakim  V.J.  42;  N,  4Ö,  4~>5'i; —  nsil    ahmi  nmäne  *sanaile  ä%rava  . ä'  .  ,  sayänie  dahakäca  "nicht  werden  . geboren  - .,   sondern    es    sollen   geboren werden  . ."  Y.  //.  6 ;  —  hau  .  .  yO  .  .  varg- thfca  Aqm.rüzayeiti .  .  a'ia  dim  upa-taala^ ydii  . .  raesayacä  (sd.)  , .  ä°  yat  . .  van- iäsca    *hqm.räzayaaha   .  .   äat    (s.   7)    .  . fascaSa  apa.bardi!  ". .  vielmehr  wenn  du dir  die  Haare    ordnest  . .,   so  sollst  du dann  .  ."  V.iy.z-i,;    —    a%>m  vTspanqm damanqm    nipäta    ahmt    .  .    ä"    ('gleich- wohl') mä  nSil  masyäka  .  .  ya'^nte  Yt  10. 54.        a)  bes.  mit  a)  folgendem  _j'iii  oder ye:i,  ß)  vorausgehendem  yezi  "wenn  aber, wenn  jedoch",  kondiz.:  a)  *yujyaslil  haca *nmänät  .  ,  ä'  yal  h!  aoxte  .  .   d^a  *hil *xiayete  ..  haxtSii  (sd.)  N.<Vf.;  V.7.3; all  (s.  8)  yS  . .  upairi  hunanm  (sd.)  mc iarät  .  .  ä°  yat  .  .  paiti  barJt  äaj  (s.  2) yal  .  .  ara  baraite  "wer  .  .  aber  wenn  er ■ .  und   wenn   er   ■  ."   P.j7f.;
8408:•  j.  upäpa-  Adj.  (fem.  'pä-)  i)  'im  Wasser befindlich,  lebend,  hausend':  dsman  . . yäca  °^ii(NPn.)  ysca  upasma  Ht.8.^%-,  — vjspamca  gqm  'pqmca  upasmqmca  "all Getier,  das  im  Wasser  und  auf  dem  Land lebt"  Y.  77.9";  —  ratavS  °panqm..  upas- manqm  Vr. /.i;  Yt/j.74;  —  ratavö  'pa .  .  upasma  Vr.  2.  i ;  —  karB  masys  'ps bütte  ..   vairyanqm   V.iff.^s;  Yt/^.  29;
9175:mit  /rS  'perficere':  frakaire  (sd.)  fra- kyr^naoi\.ig.4i  Gl.  a)  Med.  in  reflex. Sinn;  *astjm  (sd.)  i^ra  Jra^armta^"^  pas- vasca  .  .  V.  2.  II.  Wertlos:  frak}r.ma-
12953:1)  'festbinden,  fesseln':  apq^  (sd.)  gavs dam^äti  Ytro.48.  a)  Des.  '(Satzungen) aofirecht  erhalten,  (daran)  festhalten  wollen' ; aväU  urvamis  (sd.)  ya  tu  dldsrdö  (aS.)'' maa£i  Y- 4^.15,         S.  noch  dimanB.'.
12954:mit  aipi  fesseln'  (?) :  aipi  dtrfzvamm d^ratayahi'ftH  "in  Fesseln  legt  (ihn)  den Fesseln  tragenden"  Yt/.  a;  (?)♦'.
12956:mit  3  'fesseln':  HltryB  .  .  avqm  pairi- kam  adafTtayäti  bibdailla  . .  vUpabäailla .  .  ya^a  hataanm  narqm  Bim  narvm adarstaySit  Yt.  Ä  55.  Undeutlich  ;/ii«r- yqm  htm  vanm  *ad3r3zaySii  hg .  .  N.j". joit/ra  und  nT  'festmachen  sva.  unschäd- lich machen' :  aitahmaiat  nidanzaym  (sd.) fra  kimcil  nidamaym  ".  .  (so)  sollen  sie ihn  (den  Hund)  unschä<9ich  machen"  V. 13'  31-
12959:mit  Äqm  i)  'aneinander  befestigen, zusammenbindend  vereinigen':  yS  barisma .  .  hqm^risaiti  kam  va  damayäti (Konj.)  N.  <)9;  —  yezi  aat  nöit  HirB larÖMmand  handar^zanti  (Konj.)^^  aratu- /risH.  101.  a)  'fesseln':  zasta  hepaoinm kandarnayanta  V.  g.  49.  a)  mit  hatt-
12961:mit  Aain  und  nl  'zusammenfesseln':  kam gava  nidamayahii3m'°'^  Yt. /.  a?.
13924:'fesseln  sva.  einschränken,  Einhalt  tun';  I''''^''"'? ''"«^'' *'i'«^'''^(s'i-)*''«''"'-'i'''?"' m  aihms  «r'>  dyätam  (3SIM.,  in  pass.  1  "■  ■  zwölf.."  F.27a;  —  cäkwarasca  ai,a Sinn)  paia  nmim  pattz^*  *sysdäm  (sd.)  k'^'IVi'  ca^warisatimla  (sd.)  dvaila  (Nn.) y.  ^.  j.  \saite  dvatca    kaza»re  Yt.ig.-j;    —    duye
15850:•  j.  pas-  V.  'fesseln'.  j-Aor.  1  pas-.  —  PPfP. *paxita-'^.
15852:mit/d^'nndai'ii'ziisammen-.aDeinaDder- fesseln':  (^anka^tsis  flsbis  oidibTs  paiti opa.pai^st  "mit  eisernen  Fesseln  soll  man seine  Knochen  zu&ammenfesseln"  V.  ^  5 1 .
15917:•  j.  pasvant-  Adj.  (fem.  'vaiti-)  'mit *pas-  (f.  'Strick'?)"'  oder  'mit  pasav-  (m. 'Vieh'?)''  versehen':  ha  (näml.  kaine)  .  . °vaiti  V.  ig.  30.
16699:r)  'binden,  fesseln':  is'ar  pasca  puxl>m bandum  (sd.)  bandyät^''  Vd./3;  —  dazdi tm  .  .  ydha  .  .  bandayem  .  .  franrasyämm Uta  basttm  vätayeni  uta  bastfm  upana-
19043:V'5'55;  —  "°  f^'"*  ■•  oi^he  ayqn  tv  yl  hsi  n'  vTdaitl  (sd.)  Y.^i.6;3i.9]  — ai^ha  xiapS .  .  avasyäi^'*  n°  akav5  n"^ ..  a£  yastSm  n°  nä  isimnS  ayJt  (Sp.  150  m.) Yt.7.18;  —  «*  gähahe . .  tbaisö  frqstiSna  Y.46.6;  —  ysi  im  fJ  «°  i^a  mq%rtm (Sp.  595  o.)  /rasftuyat''*  Yt  11.  S;  §';  —  vanfyfii:  (sd.)  Y.45.3;  —  mit  Ellipse  von yäii  tl  ml  nöit  äaioTi ..  n°  mZ  ita  *ärihäi.-  astl:  yaT  aÜ  n°  urväta  (sd.)  advä  aibi.- fom'^  (Sp.  369  o.)  *pasu  vira  .  .  n'  pas-  dtnita  vahyiX.Sl.i;  —  es  ist  die  Verbal- c<^a  .  .  upa.dayafi^  aarS  mainyu/  Yt  form  des  vorhergehenden  positiven  Satzes /^.  izf.  zu  I  a);  mit  indikativischen  zu  ergäDzen:>J  m  ^^J/^i?^(5d.)^JV^/(sd.)
26861:•  j.,  g.  'spas-  V.  'spähen'.  Praes.  s hispas-,  10  '^spasu-Q)'^,  11  spaln-,  26 sparya:   —    PPfP.    'spasta-.  [S.   noch
26883:•  j.  'spas-  m.  'Späher,  Wächter':  spai INS.)  viftaHa  .  ,  mihrS  Yt  10.  46;  — iiii'irfm  ..  zamarthunt3m  spastm  Vt.  70. 61;  —  ydAhe  asta  rJtayS  .  .  spasS  (NP.) atühnirt  mihrahe  YL/0.  45.
29785:-    .)  D.i.    die   Macht,    wie   sie    dem   Gut-   PPn"-  '"*"-•  I°f-   °'*^'>«.   *'^3^rat. gesinnten  versprochen  ist    Pü.:  ia  ö  man  än\       l)  binden,fesseln':j'^4l'ffi(nämL<l!aAaffi) i  fa  vahaman  ilaxmak  äyii,    erL :  iS^-äns.  —    stätam  hitam  Aaitim  utvaiat  Aala  AinBtayS «)  Nach  Pa.  i^elmehr  lu  3.-   «  Sol    s^  zu    (sd.)  Yt /J.  100;  —  Ä»»'.     '    a) 'verbinden, hazaiihan-  und  Su. :  yfl  ha!hal  harati.     Falsch  ,..'       .',  .         i-fj  ._i
30649:Ableit  {Aavap').  —  Vgl.  kväpah-  Adj.  —  ai.  i äpas-  n.  'opus',  sväpas-  Adj.  —  Pü.  (ruY.J/}:  1 hupänam^•|  -  Sü.:  mtai/ä  -.,  (lu  Y. //)!  I i^äpar  'gütig';  vgl.  zu  kväpah-.  —  ')  So Pt4.  NA.  hat  hatiap'.  Them.  —  A  Statt  des  ' Vok.  —  3>  Nach  der  a-Dekl.  —  1)  Ob  aus  , ku  SpaiiA  Terderbt?     S.  kväpah-  No.  4.  ,
=== IEC ===
10800:pa-misis “hogwash?
13428:poti “near, after, behind, at. Cf. pos, post (posti). WP II, 77 Av. paiti, prp. “near, at, with, added to’; Ober, patiy, prp. “in, after, according to^; Per. pas, prp. (after. Ambig. in view of Ober pasā, see pos, but to Av. pasca: Skt. pasca accdg. to R. Kent: OPG); similarly Oss. fás- ‘behind’; Myc. posi “near”; Gk. poti, poti- ‘near; at’; Alb. (Tosk) pas, prp. “after? beside (Geg) mbas, id. (fr. *en-poti); Li. cf. -pat in some cpds.; Lat. cf. nostrá-pte (‘through our own fault”, but this is prob. to type pot- (1), q.v.)
13429:potikos, adj. type of potis, q. v. *master, hus-
13439:potis “able, powerful; master, husband’. Cf. pot-. WP II, 77 Skt. pátih, m. “owner, master, husband’; Av. paitis, m. ‘lord’; adj. ‘single’; Ober cf. pati- padam (fon its own base’, but see pot- (1) above); Per. cf. pad-Sàh ‘king’; Arm. cf. h-atuk, gs. -atki, ab. s. -atkav, adj. (same, own, pro- per' fr. a type *en-potuko-) beside unim, v. CIhave', fr. *potnio); Tokh. AB pats, pets “hus- band’; Gk. posts, m. id.; Alb. pasë, f. (^wealth', fr. *potjo); me pasé, inf. ‘to have’; pata, patshë, aor. lsg. ‘I had); OLat. pos, gs: potis, Lat. potis, gs id., adj. ‘powerful’; cf. also hos-pes, gs -pitis, m. “host”; Ir. oide, pl. oidí, m. "men, tor, foster-parent'; W od, adj. ‘noble, excel- lent; Go. -faps, m. in püsund-? ‘colonel’; brüp-^ *bridgeroom', etc ` OE faóe, faóu, wf. ‘paternal aunt? beside næ-ft. f. (‘poverty’, fr. *ne-poti-); OCS cf. potí-béga ‘woman who de- serts her busband'; Li. páts, gs patiés, m. *hus- band”; pati, f. ‘wife’; Latv. pats, m. “master, landlord'; pati, pate, f. ‘mistress, landlady’. Cf. nepóts, neptis
```


## [2026-09-07T20:40:33.570Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BRT.txt',errors='replace').read()\ni=t.find(\"j.  pas-  V.  'fesseln'\")\nif i<0:\n    i=t.find(\"pas-  V.  'fesseln'\")\nseg=t[max(0,i-6000):i+200]\nnums=re.findall(r'\\n\\s*(\\d{3,4})\\s*\\n',seg)\nprint('nearby col numbers:',nums[-8:])\nprint(repr(t[i-300:i+600]))\nEOF"
}
```


### [2026-09-07T20:40:34.850Z] TOOL RESULT

```
nearby col numbers: ['877']
'prenkelter  Stirn-,  Vorderseite\',  vom  Wild- schwein\'*:  Au  kthrpa   varszahe  .  .  \'iahe\nIL  14- 15-\n\')    Vgl,    Br£HU   Tietleben:  \'Am   Vorderteil\nob,Google\n«79\n88o\nda  Getichu  Ut  du  Bontenluar  (des  Wild- («bweins)  gewSbnlich  getpmkdt\'.  Anden Gwt  KZ.  25.  5*3.  G«-  OK.  158.\n•  j.  pas-  V.  \'fesseln\'.  j-Aor.  1  pas-.  —  PPfP. *paxita-\'^.\n\'an  nnander  befestigen,  zusammenfügen\': s.  sartmyapax^pad:\nmit/d^\'nndai\'ii\'ziisammen-.aDeinaDder- fesseln\':  (^anka^tsis  flsbis  oidibTs  paiti opa.pai^st  "mit  eisernen  Fesseln  soll  man seine  Knochen  zu&ammenfesseln"  V.  ^  5 1 .\nVgL  laßai-.  —  Po. :  /aJfnlUin,}).  —  >l%S6aE.\n•  p.  pasa  Praen.  \'nach\';  i)  örtlich  \'hinter —  nach,  dreb\',  mit  Gen.:  iäri^  .  .p°  manä asiymie^  mädam  Bh.  2.  6.  3)  zeitlich "nach",  mit  Aklc:  pasltvi^  (sbes.).\nAm  ir.  *pas  (=  idg.  *^J\')  durch  Aosgleich mit  dem'
```


## [2026-09-07T20:40:35.360Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n '^pa- \\|^pa-, \\|^pak-\\|^pag-\\|^pater\\|^pətér\\|^pa-ter' IEC.txt | head\necho \"---\"\ngrep -n 'to feed, tend\\|“to feed\\|\"to feed' IEC.txt | head -5\ngrep -n '^pako-\\|^pagos\\|^pango\\|^paks' IEC.txt | head"
}
```


### [2026-09-07T20:40:35.438Z] TOOL RESULT

```
---
12470:pakst- “fix; fixture’, etc. See påK- and next W cf. asu, asio, v. “join, cement'; OHG fasta, G Fasten “fast, fasting, Sw. fasta, v. id. (and com. Gmc.); OHG festi, adj. “firm” beside OE fæst, ON fastr, Sw. fast “firm, close, strong, fast”; cf. ON festa ‘bail; festr ds: festi, pl. fes- tar, f. “rope?
```


## [2026-09-07T20:40:42.352Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n 'påK-\\|paK-\\|pāK-' IEC.txt | head -6\necho \"=== around 12460 ===\"\nsed -n '12455,12475p' IEC.txt | cut -c1-900\necho \"=== IEC pa- feed ===\"\ngrep -n 'pasko\\|pastor\\|pask-\\|panis' IEC.txt | head -6"
}
```


### [2026-09-07T20:40:42.451Z] TOOL RESULT

```
12434:pág- (1) ‘harden, fix, fit. Cf. paK-. WP II, 3 and panĝ- Skt. paj-, radical ‘grow stiff; cf. pajráh “solid, stout’; Oss. fáz, Dig. fázà, s. lawn, flowerbed’; Arm. hoc, adj. ‘compact (fr. *pagus, cf. SEM: AE: $ 3); Gk. pégnümi, inf: pagénai ‘fix’; pégós “compact? beside págos, m. 'congeal- ment, rock, ice’; páge, pagís, f. ‘trap’; págios, ad). “fixed, firm'; OLat. pago, ére, (Lat. pango, ere) ‘fix’; pàgus, gs: -1, m. ‘landmark’; im- pages, f. ‘tenon, peg, panel-frame'; pàges and com-pàges, f. “join, setting, juncture, fitting"; LLat. pagino, are ‘compose, construct; Olr. áge, álge, m. ‘joint, member, period"; cf. ai- gred, s. "ice: aigreta, adj. ‘icy; MHG vach, sn. ‘dam, weir; piece, part, partition; fold’; G Fach, Du. vak, n. (fdivision', etc.); OE fæc, n. ‘space, interval; R paz, m. “joint, mortise’; Cz. paže, f. ('arm', fr. *pagio) beside paž-ba *gunstock, wainscot'; pažiti, inf. “box in, wall up, fix’; cf. also OCS paz-nogüti, Cz. paz- nehet claw, talon’; Ukr. cf. paz-ur, Cz. paz-our, m. id.; Ukr. R paz-üxa, f. ‘bosom’; R cf. paz- dir ‘awns’
12470:pakst- “fix; fixture’, etc. See påK- and next W cf. asu, asio, v. “join, cement'; OHG fasta, G Fasten “fast, fasting, Sw. fasta, v. id. (and com. Gmc.); OHG festi, adj. “firm” beside OE fæst, ON fastr, Sw. fast “firm, close, strong, fast”; cf. ON festa ‘bail; festr ds: festi, pl. fes- tar, f. “rope?
12508:panKtos (form of paktos, see paK-, pag-, pak- and pāĝ-) Lat. cf. pancturus, fut. inf. ‘to plant’; Lat panctio, m. ‘planting’; Ir. éacht, m. ‘pact; matter; state; feat; disaster”; éachtaim, v. ‘do, execute, commit; OCS poto (and com. SI.) ‘fetter’; (but Li. pantis, gs: pančio, m. “bond, fetter is prob. a Gmc. LW, cf. G Band)
=== around 12460 ===
hakem, v. ‘bend’, see påk- (1). The secondary mng. of Cz. páčit “calculate'; Slovak páčiť ‘evaluate’; páCit sa agree to, be pleased to’, though isophonic w. Lat. pax, etc. seems to be a variant with -k- for -K-)
pāksið “stir, move, strike’. Cf. pak- (2) OCS paso, paxati, v. tr. (1) “stir, move: Cz. pásu, páchat *commit'; R paxnuüt, inf. ‘sweep; blow'; Li. pok3iu, eti, v. ‘knock, strike, fire a gun, etc?
păk- ‘fix, tie, bind, join; bond, fixture, pact. Element of the following. WP II, 2-7. Cf. pák- (2) (note.) | Short grade in Av. pas-, v. ‘tie’; pasmom, n. ‘bond’; Arm. hasnim, v. (reach, arrive’, fr. *pak- or *pàaK-, as also) hasun ‘ripe’; hasuk ‘mature’; Gk. cf. ém-pax, gs: -pakos, m. 'guar- dian’; Lat. páciscor, v. ‘bargain’; forpex, gs: -picis, f. ‘tongs, scissors’; Go. fulla-fahjan, v. “serve, satisfy’ beside (oxytonic prototypes) OHG gi-fag, OE fzege ‘acceptable’; Go. fagrs “suitable; thankful); OHG fagar, MHG vager, ON fagr, OE fæger, Sw. fager (fair. Cf. E fair in all senses); cf. OE fægen (“joyfuP', E fain); Sw. fàgna, v. ‘cheer, entertain’; ON fagna ‘re- joice'; MHG vagen, v. ‘comply’. Cf. also MIr. acht, s. ‘stipulation’ (mod. ‘act < Lat.). Long grade in Skt. pasah, m. “bond, noose, fetter; pa$ayami, v. ‘tie
totypes in) OHG fuoga, f. ‘joint’; MHG vuoc,:
gs: vuoges, m. ‘ability, fitness’; vüege, adj. ‘fitting’; vüegen, v. join’; OE fog, adj. 'suit- able”, n. “join, joint’; OCS cf. pas-mo “skein, hank’. Extended types (*pàKmn-) in Av. pas- mən, n. ‘tie’; Gk. pégma ‘frame, truss, com- pacted snow? (LW in LLat. pegma 'scaffold- ing); LLat. pagmen-tum, n. ‘joining’; OCS, R cf. pasmo, pàsmo, n. ‘hank, skein? (Cz. = ‘zone, bel? owing to influence of unrelated pás, id.)
pāksið — pal-
15
20
25
30
35
40
45
902
paKsn- ‘fix, get’. Cf. păk- above Arm. hasanem, hasnim, v. ‘reach, arrive’; Gk. pákhnē, f. “frost, clot of blood; Hitt. cf. (?) pahhssnu(mi), v. ‘fix beside pahhs(hi) ‘hold’
pakst- “fix; fixture’, etc. See påK- and next W cf. asu, asio, v. “join, cement'; OHG fasta, G Fasten “fast, fasting, Sw. fasta, v. id. (and com. Gmc.); OHG festi, adj. “firm” beside OE fæst, ON fastr, Sw. fast “firm, close, strong, fast”; cf. ON festa ‘bail; festr ds: festi, pl. fes- tar, f. “rope?
paktos “fixed, firm; stipulation, pact. Cf. pak- Arm. hast, Let, (!) “firm, hard, solid’; Gk. p&któs, (Dor. -à-), id.; Lat. pactus ‘bargained for, m. u-st. ‘pact, bargain’; MIr. acht ('sti- pulation". But mod. Ir. acht «act influenced by Lat. actus); Go. cf. fullafahjan, v. ‘satisfy, serve
pal- (1) (palos, a, io, pal'is) ‘bare, blank, pale; space, expanse'. WP II, 61 Hitt. palhis, adj. “broad”; Lat. cf. palam, pro- palam ‘openly’; pallidus (fpale', either a synth. cpd. or fr. *palni-) beside palleo, ere, v. *be pale’; Gallo-Lat. cf. al-auda ( lark'. For -auda see áued-, áuod-); Sw. fal- (in cpds. “clearing”, also in place-names Fal- *plain-. Here EIT). OCS polü, R polyj, adj. open, bare’; polje, n. (and com. Sl.) ‘field’; cf. R polaja vodà “high water": Li. pálios, fpl. “fen, marsh’; Latv. pali, mpl. ‘flooded fields (Uncertainly Arm. nvay “dark, obscure; ailing', fr. *ni-pal-? Lat. palüs, gs: palüdis, f. ‘marsh’ is perh. a cpd., cf. üd-, üdn-, üdər water), See next
(pàl- variant of above, q.v.) Arm. (ambig.) ayawt, Let ‘dim’; alik, pl. (2) “grey hair beside alevor, adj. 'grey-haired"; Latv. palums, m. “patch, space, gap'; pals “grey”
(paln-? variant of above, q. v. Gmc. ambig. Cf. poluos) Lat. palleo, ére, v. ‘turn pale’; Icel. cf. fólna, intr. (fade, turn pale fr. *palnuo?); beside fölur, acc. fólvan, adj. (pale. Ambig. cf. po- luos); Cz. planý ‘empty, wild; fruitless’; na plano “in vain'; pláü, f. “plain, wold'; Pol. plonny ‘barren’; ptoh, f. as Cz.
pal- (2) ‘straw, chaff. Skt. ambig. Cf. pelos Skt. palah, m. id.; Lat. palea, f. ‘chaff; R cf.
=== IEC pa- feed ===
214:Sp. Spanish subj. subjunctive substr. substrate sup. supine superl. superlative Sw. Swedish Thrac. Thracian Tokh. Tokharian Ukr. Ukrainian Umb. Umbrian v. verb
12418:pä- ‘feed, guard’. Cf. pàteió, pasKó, pastor-. WP II, 71 Skt. pami, v. ‘guard, keep, hold"; Av. pai(mi), v. ‘guard, ward off; cf. Skt. aja-pab, m. 'goat- herd'; Gk. páomai, v. 'feed myself, eat and cf. aga-páo ‘love’ & pðü, gs: póeos, n. (“flock?, if for *pa-ou-, see ouis, w. vocalism of sõs, SáOS)
12534:(pástor- ‘herdsman’. Explicit only in Lat. pastor, id. OCS pastyrl, m. id. may be a Mol- davian LW in SI. For OE fostor- 'foster-': and Cz. pastor-ek, -ka ‘stepchild’ see postor-, radical: pot-, põ- 'feed"). WP II, 72
12549:pitüh, m. (2) *food'. (For OE fostor- and Cz. pastorek, see postor- in view of Arm. utem, ustr)
13423:-cild, etc.) and cf. foster-ling “foster-child?; Sw. foster, n. (foetus, child’, cpds. foster- (as Eng.); cf. fostra, v. ‘foster, rear’; OCS (dim. type) pastorükü, m. *foster-child'; Cz. pasto- rek, m. id.
20010:uenter- (uentor-) (uemster-?) *wickerwork, basket" (?); ‘bag, net? (?) Av. cf. vafita, f. ‘wicker’; Lat. venter, gs: ven- tris, m. (abdomen, stomach, womb'. Fig. sense of *bread-basket (?), cf. pàn-tex ‘paunch’, if a cpd. of panis "bread", and cf. E. dial. breadbasket = *'abdomen); Li. vénteris, gs: vénterio, m. *bownet, fishtrap', Latv. ven- teris ( fish-trap, fish-basket' or '-pot"); but cf. also Icel. vinstur, pl. vinstrar, f. “fourth stom- ach of ruminant'. See Supt: U: uemstr-
```


## [2026-09-07T20:40:47.791Z] TOOL CALL #44: Bash

```json
{
 "command": "ls tools/ && python3 tools/fetch_source.py --help 2>&1 | head -20"
}
```


### [2026-09-07T20:40:49.150Z] TOOL RESULT

```
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
Save a web source used during verification, for later cross-checking.

    python3 tools/fetch_source.py <URL> [--note "why it was fetched"]

Downloads the URL, converts the HTML to plain text, stores it as
data/verification/sources/web/<sha1(url)>.txt and appends a line to
data/verification/sources/web/index.jsonl  ({url, file, fetched, bytes, status, title, note}).
Prints the stored path. Re-fetching the same URL within a day is skipped.
```


## [2026-09-07T20:40:55.257Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/peh%E2%82%82-\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ph%E2%82%82t%E1%B8%97r\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/p%C3%B3tis\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/peh%E2%82%82%C7%B5-\" \\\n ; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 380, roots Pa/Pa-ter/Poti and Pak/Pag\" 2>&1 | tail -3; done"
}
```


### [2026-09-07T20:40:58.194Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/peh%E2%82%82-
/home/sfmqrb/git/rishe/data/verification/sources/web/ca565c6cb7f3e8ee.txt
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ph%E2%82%82t%E1%B8%97r
/home/sfmqrb/git/rishe/data/verification/sources/web/1e44382aae246b8c.txt
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/p%C3%B3tis
/home/sfmqrb/git/rishe/data/verification/sources/web/5cc57d5c414bf99b.txt
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/peh%E2%82%82%C7%B5-
/home/sfmqrb/git/rishe/data/verification/sources/web/4aed3287287bdeb2.txt
```


## [2026-09-07T20:41:01.796Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in ca565c6cb7f3e8ee 1e44382aae246b8c 5cc57d5c414bf99b 4aed3287287bdeb2; do echo \"######## $f\"; head -c 2200 $f.txt; echo; done"
}
```


### [2026-09-07T20:41:02.953Z] TOOL RESULT

```
######## ca565c6cb7f3e8ee
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/peh%E2%82%82-
FETCHED: 2026-09-07T20:40:56Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/peh₂- - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/peh₂- - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community portal 
 Requested entries 
 Recent changes 
 Random entry 
 Help 
 Glossary 
 Contact us 
 Special pages 

 Search 

 Search 

 Appearance 

 Donations 

 Create account 

 Log in 

 Personal tools 

 Donations 

 Create account 

 Log in 

 Contents

 move to sidebar 
 hide 

 Beginning

 1 
 Proto-Indo-European 

 Toggle Proto-Indo-European subsection 

 1.1 
 Root 

 1.1.1 
 Usage notes 

 1.1.2 
 Derived terms 

 1.2 
 References 

 Toggle the table of contents 

 Reconstruction:Proto-Indo-European/ peh₂- 

 Add languages 

 Reconstruction 

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
 Page information 
 Get shortened URL 

 Print/export

 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Root
 [ edit ] 

 *peh₂- [ 1 ] [ 2 ] [ 3 ] 

 to protect , to ward 

 to shepherd 

 Usage notes
 [ edit ] 

 Semantic shift from "protector" towards "shepherd, herder" can be seen in many branches, signifying the importance of herding. Unusual is the o-grade root in Greek ποιμήν ( poimḗn , “ shepherd, herdsman ” ) , where the abstract nomina agentis suffix *-mn̥ usually binds e-grade, but that hardly seems sufficient to reconstruct *h₃ in the root and to separate it from *peh₂- .

 Derived terms
 [ edit ] 

 Terms derived from the Proto-Indo-European root *peh₂- (127 c,
######## 1e44382aae246b8c
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ph%E2%82%82t%E1%B8%97r
FETCHED: 2026-09-07T20:40:57Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/ph₂tḗr - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/ph₂tḗr - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community portal 
 Requested entries 
 Recent changes 
 Random entry 
 Help 
 Glossary 
 Contact us 
 Special pages 

 Search 

 Search 

 Appearance 

 Donations 

 Create account 

 Log in 

 Personal tools 

 Donations 

 Create account 

 Log in 

 Contents

 move to sidebar 
 hide 

 Beginning

 1 
 Proto-Indo-European 

 Toggle Proto-Indo-European subsection 

 1.1 
 Etymology 

 1.2 
 Noun 

 1.2.1 
 Inflection 

 1.2.2 
 Coordinate terms 

 1.2.3 
 Descendants 

 1.3 
 References 

 1.4 
 Further reading 

 Toggle the table of contents 

 Reconstruction:Proto-Indo-European/ ph₂tḗr 

 2 languages 

 Français 
 Türkçe 

 Reconstruction 

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
 Page information 
 Get shortened URL 

 Print/export

 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Etymology
 [ edit ] 

 Often supposed to be from *peh₂- ( “ to protect, shepherd ” ) +‎ *-tḗr ( agentive nominal suffix ) . Alternatively, from a nursery form *pa . [ 1 ] It is possible that both semantic senses have contributed to the development of the term.

 Noun
 [ edit ] 

 *ph₂tḗr   m ( oblique stem *ph₂tr̥- ) [ 2 ] 

 father 
 Synonyms: *átta , *tata- 
 Hypernym: *ǵénh₁tōr 

 Inflection
 [ edit ] 

 Athematic, hysterokinetic

 singular

 nominative

 *p
######## 5cc57d5c414bf99b
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/p%C3%B3tis
FETCHED: 2026-09-07T20:40:57Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/pótis - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/pótis - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community portal 
 Requested entries 
 Recent changes 
 Random entry 
 Help 
 Glossary 
 Contact us 
 Special pages 

 Search 

 Search 

 Appearance 

 Donations 

 Create account 

 Log in 

 Personal tools 

 Donations 

 Create account 

 Log in 

 Contents

 move to sidebar 
 hide 

 Beginning

 1 
 Proto-Indo-European 

 Toggle Proto-Indo-European subsection 

 1.1 
 Etymology 

 1.2 
 Noun 

 1.2.1 
 Inflection 

 1.2.2 
 Derived terms 

 1.2.3 
 Descendants 

 1.3 
 References 

 Toggle the table of contents 

 Reconstruction:Proto-Indo-European/ pótis 

 Add languages 

 Reconstruction 

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
 Page information 
 Get shortened URL 

 Print/export

 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Etymology
 [ edit ] 

 Derksen writes: “It is often assumed that the meaning ‘lord, husband’ derives from an even older meaning ‘self’, as found in pàts” (see Lithuanian pàts ( “ ( singular masculine ) self ” ) ).

 Noun
 [ edit ] 

 *pótis   m 

 master , ruler 

 husband 

 Inflection
 [ edit ] 

 Athematic, acrostatic

 singular

 nominative

 *pótis 

 genitive

 *pótis 

 singular

 dual

 plural

 nominative

 *pótis 

 *pótih₁(e) 

 *póteyes 

 vocative

 *póti 

 *pótih₁(e) 

 *póteyes 

 accusative

 *pótim 

 *pót
######## 4aed3287287bdeb2
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/peh%E2%82%82%C7%B5-
FETCHED: 2026-09-07T20:40:58Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/peh₂ǵ- - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/peh₂ǵ- - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community portal 
 Requested entries 
 Recent changes 
 Random entry 
 Help 
 Glossary 
 Contact us 
 Special pages 

 Search 

 Search 

 Appearance 

 Donations 

 Create account 

 Log in 

 Personal tools 

 Donations 

 Create account 

 Log in 

 Contents

 move to sidebar 
 hide 

 Beginning

 1 
 Proto-Indo-European 

 Toggle Proto-Indo-European subsection 

 1.1 
 Alternative forms 

 1.2 
 Root 

 1.2.1 
 Derived terms 

 1.3 
 References 

 Toggle the table of contents 

 Reconstruction:Proto-Indo-European/ peh₂ǵ- 

 1 language 

 Русский 

 Reconstruction 

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
 Page information 
 Get shortened URL 

 Print/export

 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Alternative forms
 [ edit ] 

 *peh₂ḱ- 

 Root
 [ edit ] 

 *peh₂ǵ- [ 1 ] [ 2 ] [ 3 ] 

 to attach , fix , fasten 

 Derived terms
 [ edit ] 

 Terms derived from the Proto-Indo-European root *peh₂ǵ- (42 c, 0 e) 

 *peh₂ǵ-neu- [ 4 ] 
 Hellenic:
 Ancient Greek: πήγνυμι ( pḗgnumi , “ I secure, fasten ” ) 

 *ph₂ǵ-éh₂ye-ti ( iterative or causative verb with *-eh₂yéti ) 
 Italic:
 ⇒ Latin: prōpāgō 

 *ph₂-né-ǵ- ~ *ph₂-n̥-ǵ- ( nasal-infix present ) [ 1 ] 
 Proto-Italic: *pangō 
 Latin: pangō ( “ I fasten, fix ” )
```


## [2026-09-07T20:41:15.322Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%A8%D8%A7\" \\\n \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%A8%DA%A9\" \\\n \"https://www.etymonline.com/word/pattern\" \\\n \"https://www.etymonline.com/word/fur\" \\\n \"https://www.etymonline.com/word/pope\" \\\n ; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 380, Pa/Pak roots: Persian baba/babak, English pattern/fur/pope\" 2>&1 | tail -2; done"
}
```


### [2026-09-07T20:41:19.385Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%A8%D8%A7
/home/sfmqrb/git/rishe/data/verification/sources/web/dd49196b52b57059.txt
### https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%A8%DA%A9
/home/sfmqrb/git/rishe/data/verification/sources/web/12032c905746edc4.txt
### https://www.etymonline.com/word/pattern
/home/sfmqrb/git/rishe/data/verification/sources/web/a5aea44a77e9c57f.txt
### https://www.etymonline.com/word/fur
/home/sfmqrb/git/rishe/data/verification/sources/web/beb186cb9e8c4636.txt
### https://www.etymonline.com/word/pope
/home/sfmqrb/git/rishe/data/verification/sources/web/6a4b9c88dd565001.txt
```


## [2026-09-07T20:41:24.947Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\npython3 - <<'EOF'\nimport re\nfor f,keys in [('dd49196b52b57059',['Persian','Etymology','Middle Persian','nursery']),\n               ('12032c905746edc4',['Persian','Etymology']),\n               ('a5aea44a77e9c57f',['pattern']),\n               ('beb186cb9e8c4636',['fur ']),\n               ('6a4b9c88dd565001',['pope'])]:\n    t=open(f+'.txt',errors='replace').read()\n    i=t.find('Appearance\\n\\n move to sidebar \\n hide \\n\\n From Wiktionary')\n    if i<0: i=t.find('Advertisement')\n    print('########',f)\n    print(t[i if i>0 else 0: (i if i>0 else 0)+2000])\n    print()\nEOF"
}
```


### [2026-09-07T20:41:26.203Z] TOOL RESULT

```
######## dd49196b52b57059
Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 See also: بابو , بابه , and پاپا 

 Arabic
 [ edit ] 

 Pronunciation
 [ edit ] 

 IPA ( key ) : /baː.baː/ 

 Etymology 1
 [ edit ] 

 Borrowed from Latin pāpa .

 Noun
 [ edit ] 

 بَابَا • ( bābā )  m ( plural بَابَوَات ( bābawāt ) ) 

 ( Christianity ) pope , patriarch 

 Usage notes
 [ edit ] 

 The Bishop of Rome is often specified as بَابَا ٱلْفاتِيكان ( bābā l-fātīkān , literally “ Pope of the Vatican ” ) to distinguish him from the Coptic pope .

 Declension
 [ edit ] 

 Declension of noun بَابَا ( bābā )

 singular

 singular invariable

 indefinite

 definite

 construct

 informal

 بَابَا 
 bābā 

 الْبَابَا 
 al-bābā 

 بَابَا 
 bābā 

 nominative

 بَابَا 
 bābā 

 الْبَابَا 
 al-bābā 

 بَابَا 
 bābā 

 accusative

 بَابَا 
 bābā 

 الْبَابَا 
 al-bābā 

 بَابَا 
 bābā 

 genitive

 بَابَا 
 bābā 

 الْبَابَا 
 al-bābā 

 بَابَا 
 bābā 

 dual

 indefinite

 definite

 construct

 informal

 بَابَوَيْن 
 bābawayn 

 الْبَابَوَيْن 
 al-bābawayn 

 بَابَوَيْ 
 bābaway 

 nominative

 بَابَوَانِ 
 bābawāni 

 الْبَابَوَانِ 
 al-bābawāni 

 بَابَوَا 
 bābawā 

 accusative

 بَابَوَيْنِ 
 bābawayni 

 الْبَابَوَيْنِ 
 al-bābawayni 

 بَابَوَيْ 
 bābaway 

 genitive

 بَابَوَيْنِ 
 bābawayni 

 الْبَابَوَيْنِ 
 al-bābawayni 

 بَابَوَيْ 
 bābaway 

 plural

 sound feminine plural

 indefinite

 definite

 construct

 informal

 بَابَوَات 
 bābawāt 

 الْبَابَوَات 
 al-bābawāt 

 بَابَوَات 
 bābawāt 

 nominative

 بَابَوَاتٌ 
 bābawātun 

 الْبَابَوَاتُ 
 al-bābawātu 

 بَابَوَاتُ 
 bābawātu 

 accusative

 بَابَوَاتٍ 
 bābawātin 

 الْبَابَوَاتِ 
 al-bābawāti 

 بَابَوَاتِ 
 bābawāti 

 genitive

 بَابَوَاتٍ 
 bābawātin 

 الْبَابَوَاتِ 
 al-bābawāti 

 بَابَوَاتِ 
 bābawāti 

 Related terms
 [ edit ] 

 بَابَوِيّ ( bābawiyy ) 

 بَابَوِيَّة ( bābawiyya ) 

 Etymology 2
 [ edit ] 

 From baby talk.

 Noun
 [ edit ] 

 بَابَا • ( bābā )  m 

 ( childish ) papa , daddy , father 

 

######## 12032c905746edc4
Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 Persian
 [ edit ] 

 Etymology
 [ edit ] 

 Middle Persian 𐭯𐭠𐭯𐭪𐭩 ( Pābag ) , itself from Old Persian *Pāpakah .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /baː.ˈbak/ 

 ( Dari, formal ) IPA ( key ) : [bɑː.bák] 

 ( Dari, formal ) IPA ( key ) : [bɑː.bák] 
 ( Kabuli ) IPA ( key ) : [bɑː.bák] 

 ( Hazaragi ) IPA ( key ) : [bɔː.bák] 

 ( Iran, formal ) IPA ( key ) : [bɒː.bǽkʰʲ] 

 ( Tajik, formal ) IPA ( key ) : [bɔ.bák] 

 Rhymes: -ak 

 Readings

 Classical reading ? 

 bābak

 Dari reading ? 

 bābak

 Iranian reading ? 

 bâbak

 Tajik reading ? 

 bobak

 Noun
 [ edit ] 

 بابک • ( bâbak ) 

 a little father 

 one who educates

 a turquoise stone

 Adjective
 [ edit ] 

 بابک • ( bâbak ) 

 faithful , constant , firm , strong 

 Proper noun
 [ edit ] 

 بابک • ( bâbak ) 

 a male given name Babak 
 Babak Khorramdin 

 Descendants
 [ edit ] 

 → Middle Armenian: Պապաք ( Papakʻ ) 

 Further reading
 [ edit ] 

 Steingass, Francis Joseph ( 1892 ), “ بابک ”, in A Comprehensive Persian–English dictionary (overall work in English), London: Routledge & K. Paul 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=بابک&oldid=85703317 "

 Categories : Persian terms derived from Middle Persian 
 Persian terms derived from Old Persian 
 Persian terms with IPA pronunciation 
 Rhymes:Persian/ak 
 Rhymes:Persian/ak/2 syllables 
 Persian lemmas 
 Persian nouns 
 Persian adjectives 
 Persian proper nouns 
 Persian given names 
 Persian male given names 

 Hidden categories: Middle Persian terms with non-redundant manual transliterations 
 Persian undefined derivations 
 Pages with entries 
 Pages with 1 entry 

 This page was last edited on 24 July 2025, at 11:51.

 Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. 

 Privacy

######## a5aea44a77e9c57f
Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of pattern 

 pattern (n.) 

 a Modern English variant of patron , retaining its other old sense of "outline, plan, model, an original proposed for imitation," from Old French patron "patron, protector; model, pattern." The difference in form and sense between English patron and pattern wasn't firm before 1700s. The meaning "a design or figure corresponding in outline to an object that is to be fabricated and serving as a guide for its shape and dimensions" is by late 14c. Extended sense of "repeated decorative design" is from 1580s. From 1640s as "a part showing the figure or quality of the whole." Meaning "model or design in dressmaking" (especially one of paper) is recorded by 1792 (Jane Austen). Pattern-book is from 1774; pattern-maker is by 1851; pattern baldness is by 1916.

 pattern (v.) 

 1580s, "to make a pattern for, design, plan" (a sense now obsolete), from pattern (n.). Meaning "to make something after a pattern" is from c. 1600; that of "to cover with a design or pattern" is by 1857. To pattern after "take as a model" is by 1878.
 also from 1580s 

 Entries linking to pattern 

 patron (n.) 

 c. 1300, patroun , "a lord-master, one who protects, supports, or encourages," also "one who has the right of presenting a clergyman to a preferment," from Old French patron "patron, protector, patron saint" (12c.) and directly from Medieval Latin patronus "patron saint, bestower of a benefice; lord, master; model, pattern, example," from Latin patronus "defender, protector; former master (of a freed slave); advocate," from pater (genitive patris ) "father" (see father (n.)). A doublet of pattern (n.); also compare patroon .

 From late 14c. as "founder of a religious order," also "a patron saint." The meaning "one who advances and encourages the cause or work" of an artist, institution, etc., usually by means of the person'

######## beb186cb9e8c4636
Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of fur 

 fur (n.) 

 late 14c. "trimming or lining of a garment" (implied c. 1300 in surname Furhode "fur hood"), probably from Old French forrer , fourrer "cover with fur, line (clothing)," in general "to cover, fill with," from fuerre "sheath, scabbard" (via notion of "covering"), from Frankish *fodr or another Germanic source, from Proto-Germanic *fodram "sheath" (source also of Old Frisian foder "coat lining," Old High German fotar "a lining," German Futter , Gothic fodr "sword sheath"), from PIE root *pa- "to feed, protect."

 First applied c. 1400 to the hairy pelt of an animal, whether still on the animal or not. The Old French noun might have had the sense "hide, fur, pelt" (and thus might serve as the immediate source of the English noun), but this is not attested. Absent this, the sense transfer from the lining to the material that goes to make it probably happened in English. As an adjective from 1590s.

 To make the fur (or feathers) fly "make an effective assault or attack" is a reference to the effect of a successful shot in hunting on the hunted creature.

 I'le make the fur Flie 'bout the eares of the old Cur. [Butler, "Hudibras," 1663]
 also from late 14c. 

 fur (v.) 

 c. 1300 (implied in furred ), from fur (n.) or Old French fourrer "to line." Related: Furring .
 also from c. 1300 

 Entries linking to fur 

 furrier (n.) 

 "dealer or dresser in furs," late 15c.; as a surname late 13c. ( Osberto le ffurrere ), via Anglo-French from Old French forreor "furrier," from forrer "to line or trim with fur" (see fur (n.)).

 furry (adj.) 

 1670s, "made of fur, covered with fur," from fur + -y (2). As a noun, in reference to "anthropomorphic animal characters with human personalities," also of people who identify with them, by 1995. Related: Furriness ; furries .

 *pa- 

 *pā- , Proto-Indo-European root meaning "t

######## 6a4b9c88dd565001
Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of pope 

 pope (n.) 

 "the Bishop of Rome as head of the Roman Catholic Church," c. 1200, from Old English papa (9c.), from Church Latin papa "bishop, pope" (in classical Latin, "tutor"), from Greek papas "patriarch, bishop," originally "father" (see papa ).

 Applied to bishops of Asia Minor and taken as a title by the Bishop of Alexandria c. 250. In the Western Church, applied especially to the Bishop of Rome since the time of Leo the Great (440-461), the first great asserter of its privileges, and claimed exclusively by them from 1073 (usually in English with a capital P- ).

 Popemobile , his car, is from 1979. Pope's nose for "fleshy part of the tail of a bird" is by 1895. Papal , papacy , later acquisitions in English, preserve the original vowel.
 also from c. 1200 

 Entries linking to pope 

 papa (n.) 

 "father," 1680s, from French papa , from Latin papa , originally a reduplicated child's word, similar to Greek pappa (vocative) "o father," pappas "father," pappos "grandfather." The native word is daddy ; according to OED the first use of papa was in courtly speech, as a continental affectation, and it was not used by common folk until late 18c.

 papacy (n.) 

 late 14c., papacie , "the office or jurisdiction of a pope," from Medieval Latin papatia "papal office," from Late Latin papa "pope" (see pope ). Old English had papdom in this sense. Meaning "the succession or line of popes; the system of ecclesiastical government based upon authority of the Bishop of Rome over the Church" is from 1540s.

 papal 
 antipope 
 papist 
 popery 
 popish 
 See All Related Words (7) 

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 More to explore

 Gregorian 

 From c. 1600 of church music, in reference to Gregory I the Great (pope from 590-604), who traditionally codi
```


## [2026-09-07T20:41:39.315Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%A8#Persian\" \\\n \"https://www.etymonline.com/word/*pa-\" \\\n \"https://www.etymonline.com/word/*pag-\" \\\n ; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 380: Persian bab; PIE *pa- and *pag- root pages\" 2>&1 | tail -2; done"
}
```


### [2026-09-07T20:41:42.020Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%A8#Persian
/home/sfmqrb/git/rishe/data/verification/sources/web/a60414027323f9d1.txt
### https://www.etymonline.com/word/*pa-
/home/sfmqrb/git/rishe/data/verification/sources/web/b0acec67be28e0a9.txt
### https://www.etymonline.com/word/*pag-
/home/sfmqrb/git/rishe/data/verification/sources/web/979e8d0902c6dc65.txt
```


## [2026-09-07T20:41:46.629Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\npython3 - <<'EOF'\nt=open('a60414027323f9d1.txt',errors='replace').read()\ni=t.find('Persian\\n [ edit ]')\nprint(t[i-200:i+1600] if i>0 else t[:1500])\nEOF\necho \"############# pa-\"\npython3 - <<'EOF'\nt=open('b0acec67be28e0a9.txt',errors='replace').read()\ni=t.find('Origin and history')\nprint(t[i:i+1500])\nEOF\necho \"############# pag-\"\npython3 - <<'EOF'\nt=open('979e8d0902c6dc65.txt',errors='replace').read()\ni=t.find('Origin and history')\nprint(t[i:i+1200])\nEOF"
}
```


### [2026-09-07T20:41:48.086Z] TOOL RESULT

```
ue , matter 

 Derived terms
 [ edit ] 

 باب السعادة ( Bâbüssaâde ) 

 Descendants
 [ edit ] 

 Turkish: bap 

 Further reading
 [ edit ] 

 Nişanyan, Sevan ( 2002– ), “ bab ”, in Nişanyan Sözlük 

 Persian
 [ edit ] 

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈbaːb/ 

 ( Dari, formal ) IPA ( key ) : [bɑːb] 

 ( Dari, formal ) IPA ( key ) : [bɑːb] 
 ( Kabuli ) IPA ( key ) : [bɑːb] 

 ( Hazaragi ) IPA ( key ) : [bɔːb̥] 

 ( Iran, formal ) IPA ( key ) : [bɒːb̥] 

 ( Tajik, formal ) IPA ( key ) : [bɔb] 

 Rhymes: -aːb 

 Readings

 Classical reading ? 

 bāb

 Dari reading ? 

 bāb

 Iranian reading ? 

 bâb

 Tajik reading ? 

 bob

 Etymology 1
 [ edit ] 

 Adjective
 [ edit ] 

 باب • ( bāb / bâb ) ( Tajik spelling боб ) 

 appropriate 

 Etymology 2
 [ edit ] 

 Etymology tree

 Akkadian bābum bor. 
 Aramaic בָּבָא bor. 
 Arabic بَاب ( bāb ) bor. 
 Persian باب 

 Borrowed from Arabic بَاب ( bāb , “ gate ” ) .

 Noun
 [ edit ] 

 Dari

 باب 

 Iranian Persian

 Tajik

 боб 

 باب • ( bāb / bâb ) ( plural باب‌ها ( bāb-hā / bâb-hâ ) , Tajik spelling боб ) 

 chapter (of a written work)
 Synonyms: فصل ( fasl ) , فرگرد ( fargard ) , چپتر ( čapter ) 

 ( archaic , original sense ) door , gate 
 Synonym: در ( dar ) 
 c. 1260s , Jalāl ad-Dīn Mohammad Rūmī , translated by Reynold A. Nicholson , مثنوی معنوی [ Masnavi-ye-Ma'navi ], volume I, verse 3763: چون تو باب ی آن مدینه‌‌ی علم را
چون شعاعی آفتاب حلم را čūn tū bāb -ī ān madīna-yi ilm rā
čūn šu'ā'-ī āftāb-i hilm rā Since thou art the gate of the city of Knowledge,
since thou art the beams of the sun of Clemency. 

 Proper noun
 [ edit ] 

 Dari

 باب 

 Iranian Persian

 Tajik

 Боб 

 باب • ( bāb  / bâb ) ( Tajik spelling Боб ) 

 Báb 

 Derived terms
 [ edit ] 

 بابی ( bābī  / bâbi ) 
 بابیه ( bābiyy
############# pa-
Origin and history of *pa- 

 *pa- 

 *pā- , Proto-Indo-European root meaning "to protect, feed."

 It might form all or part of: antipasto ; appanage ; bannock ; bezoar ; companion ; company ; feed ; fodder ; food ; forage ; foray ; foster ; fur ; furrier ; impanate ; pabulum ; panatela ; panic (n.2) "type of grass;" pannier ; panocha ; pantry ; pastern ; pastor ; pasture ; pester ; repast ; satrap .

 It might also be the source of: Greek pateisthai "to feed;" Latin pabulum "food, fodder," panis "bread," pasci "to feed," pascare "to graze, pasture, feed," pastor "shepherd," literally "feeder;" Avestan pitu- "food;" Old Church Slavonic pasti "feed cattle, pasture;" Russian pishcha "food;" Old English foda , Gothic fodeins "food, nourishment."

 Entries linking to *pa- 

 antipasto (n.) 

 "small portions served from a shared platter as the traditional first course of a formal Italian meal," 1929, from Italian antipasto , from anti- "before" (from Latin ante ; see ante- ) + pasto "food," from Latin pascere "to feed," from PIE root *pa- "to feed." Earlier Englished as antepast "something taken before a meal to whet the appetite" (1580s).

 appanage (n.) 

 c. 1600, "provision made for the younger children of royal or noble families," from French appanage (16c.), restored from earlier apanage (13c.), a term in feudal law, from apaner "to endow with means of subsistence," from Medieval Latin appanare "equip with bread," from ad "to" (see ad- ) + panis "bread" (from PIE root *pa-
############# pag-
Origin and history of *pag- 

 *pag- 

 also *pak- , Proto-Indo-European root meaning "to fasten."

 It might form all or part of: Areopagus ; appease ; appeasement ; compact (adj.) "concentrated;" compact (n.1) "agreement;" fang ; impact ; impale ; impinge ; newfangled ; pace (prep.) "with the leave of;" pacific ; pacify ; pact ; pagan ; page (n.1) "sheet of paper;" pageant ; pale (n.) "limit, boundary, restriction;" palette ; palisade ; patio ; pawl ; pax ; pay ; peace ; peasant ; pectin ; peel (n.2) "shovel-shaped instrument;" pole (n.1) "stake;" propagate ; propagation ; travail ; travel .

 It might also be the source of: Sanskrit pasa- "cord, rope," pajra- "solid, firm;" Avestan pas- "to fetter;" Greek pegnynai "to fix, make firm, fast or solid," pagos "pinnacle, cliff, rocky hill;" Latin pangere "to fix, to fasten," pagina "column," pagus "district;" Slavonic paž "wooden partition;" Old English fegan "to join," fon "to catch seize."

 Entries linking to *pag- 

 appease (v.) 

 c. 1300 appesen , "reconcile," from Anglo-French apeser , Old French apaisier "to pacify, make peace, appease, be reconciled, placate" (12c.), from the phrase a paisier "bring to peace," from a "to" (
```


## [2026-09-07T20:42:01.380Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^pid\\|^pidar\\|Pābag\\|pabag\\|^pāy\" PHD.txt | head\necho \"--- PHD size ---\"; wc -l PHD.txt PHD_mackenzie.txt\ngrep -n \"pid \" PHD_mackenzie.txt | head -5"
}
```


### [2026-09-07T20:42:01.448Z] TOOL RESULT

```
4739:pidixtayth — “UCU у о
4746:pāyag pānāgīh pānāg -bān pänagīh panag pānzdah pākīzag pāk pālāy- pālūdan pālūdag 1-2pärag pārsīg pāsox pāsbānīh pāsbān pazen pāzand pazen pāšnag pāšom
--- PHD size ---
  5578 PHD.txt
 12397 PHD_mackenzie.txt
 17975 total
4230:Ipid [AB' < A )b-y; p(y)t l I M pyd] father.
4231:lipid [p(y)t l I P pyd] meat, flesh.
7722:stupid dusiigiih.                          sweetest xwiilist.
```


## [2026-09-07T20:42:07.902Z] TOOL CALL #52: Bash

```json
{
 "command": "sed -n 1,80p tools/verify_check.py"
}
```


### [2026-09-07T20:42:07.959Z] TOOL RESULT

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
```


## [2026-09-07T20:42:10.438Z] TOOL CALL #53: Bash

```json
{
 "command": "sed -n 80,160p tools/verify_check.py"
}
```


### [2026-09-07T20:42:10.476Z] TOOL RESULT

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


## [2026-09-07T20:42:56.292Z] TOOL CALL #54: Bash

```json
{
 "command": "pdftoppm -f 380 -l 380 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg380 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg380.png"
}
```


### [2026-09-07T20:42:58.091Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 79597 Sep  7 16:42 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg380.png
```


## [2026-09-07T20:43:00.755Z] TOOL CALL #55: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg380.png"
}
```


### [2026-09-07T20:43:01.310Z] TOOL RESULT

```

```


## [2026-09-07T20:43:01.307Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T20:43:16.004Z] TOOL CALL #56: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg380.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/380.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/380.png"
}
```


### [2026-09-07T20:43:16.062Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 79597 Sep  7 16:43 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/380.png
```


## [2026-09-07T20:49:36.596Z] TOOL CALL #57: Bash

```json
{
 "command": "python3 - <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_PA   = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/peh%E2%82%82-\"\nW_PTR  = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ph%E2%82%82t%E1%B8%97r\"\nW_POT  = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/p%C3%B3tis\"\nW_PAG  = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/peh%E2%82%82%C7%B5-\"\nW_BABA = \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%A8%D8%A7\"\nW_BABK = \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%A8%DA%A9\"\nW_BAB  = \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%A8#Persian\"\nE_PAT  = \"https://www.etymonline.com/word/pattern\"\nE_FUR  = \"https://www.etymonline.com/word/fur\"\nE_POPE = \"https://www.etymonline.com/word/pope\"\nE_PA   = \"https://www.etymonline.com/word/*pa-\"\nE_PAG  = \"https://www.etymonline.com/word/*pag-\"\n\ndoc = {\n \"pdf_page\": 380,\n \"book_page\": 350,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-07\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Pa, Pa-ter, Poti, Potiš\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"PIE *peh₂- 'to protect, ward, shepherd' (Pok. pā-, pə-, pā-t- 787); *ph₂tḗr 'father' (Pok. pətḗr 829); *pótis 'master, husband, self' (Pok. poti-s 842)\",\n   \"note\": \"The three items in Nourai's root box are three separate headwords in every standard repertory. (1) *peh₂- 'to protect, feed/shepherd' is real and correctly glossed: Pokorny 787 'pā-: pə- and pā-t-: pə-t-, Meaning: to feed, graze'; AHD/Watkins 'pā-. To protect, feed'; Wiktionary *peh₂- 'to protect, to ward; to shepherd'. (2) *ph₂tḗr 'father' is a separate lexeme at Pokorny 829, where Pokorny himself hesitates ('of babble-word pa- derive? Kretschmer WZKM 51, 315 f.; or to pō(i)- shield, watch?'); Wiktionary states it plainly: 'Often supposed to be from *peh₂- (to protect, shepherd) + *-tḗr (agentive nominal suffix). Alternatively, from a nursery form *pa.' So Nourai's Pa + ter analysis (his '☞ Ter 3') is one of the two live options, not a certainty. (3) *pótis 'master, husband' (Pokorny 842) is nowhere derived from *peh₂-; the gloss 'protector' is Nourai's harmonisation, but his 'also self' is well grounded (Av. xᵛaē-pati- 'er selbst', Lith. pats, Latv. pats, Hitt. -pat 'self'; Wiktionary quotes Derksen: 'It is often assumed that the meaning lord, husband derives from an even older meaning self'). Nourai's own caveat ('This has probably started as a nursery word') is exactly Buck's position (SYN 103) and is the standard view for the pa-/papa/baba family. Verdict plausible: the root and gloss for Pa are right, the Pa-ter link is a respectable but contested analysis, the Poti link is Nourai's own lumping.\",\n   \"note_fa\": \"نورایی سه سرواژهٔ جداگانه را در یک جعبه گرد آورده است. یکم: ریشهٔ هندواروپایی آغازین ‎*peh₂-‎ «پاسداری کردن، چرانیدن، خوراک دادن» درست است و پوکورنی (ص ۷۸۷) و واتکینز و ویکی‌واژه همین معنا را می‌دهند. دوم: ‎*ph₂tḗr‎ «پدر» در پوکورنی سرواژه‌ای جداگانه است (ص ۸۲۹) و خود پوکورنی در پیوند آن با ‎*peh₂-‎ تردید می‌کند؛ ویکی‌واژه می‌نویسد «بیشتر آن را ‎*peh₂-‎ + پسوند فاعلی ‎*-tḗr‎ می‌دانند، ولی شاید هم از واژهٔ کودکانهٔ ‎*pa‎ باشد». پس تجزیهٔ نورایی (پا + تر) پذیرفتنی ولی قطعی نیست. سوم: ‎*pótis‎ «سرور، شوی» (پوکورنی ۸۴۲) در هیچ منبعی از ‎*peh₂-‎ گرفته نشده است؛ اما افزودهٔ نورایی «و نیز خود» درست است، چون اوستایی ‎xᵛaē-pati-‎ و لیتوانیایی ‎pats‎ و هیتی ‎-pat‎ به معنی «خود» است. یادداشت خودِ نورایی که این خانواده از واژه‌ای کودکانه آغاز شده، همان دیدگاه باک است. حکم: با احتیاط پذیرفتنی است.\",\n   \"sources\": [W_PA, W_PTR, W_POT, E_PA],\n   \"ref_check\": [\n    {\"ref\": \"POK:787\", \"status\": \"supports\", \"note\": \"POK_full.txt, 'Root / lemma: pā- : pə- and pā-t- : pə-t- / Meaning: to feed, graze … References: WP. II 72 f., WH. II 246 f., 260 … Page(s): 787'. Exactly Nourai's 'Pa: to protect, to feed'.\"},\n    {\"ref\": \"POK:842\", \"status\": \"supports\", \"note\": \"POK_full.txt, 'Root / lemma: poti-s / Meaning: owner, host, master, husband … Avestan xᵛaē-pati- \\\"er selbst\\\" … Lithuanian pats \\\"husband\\\" and \\\"selbst\\\" … Hittite -pat \\\"eben(so)\\\" … Page(s): 842'. Supports 'protector, husband, power, also self' — except that Pokorny keeps poti-s wholly separate from pā-.\"},\n    {\"ref\": \"SYN:103\", \"status\": \"supports\", \"note\": \"Buck, SYN.txt leaf 134/136 (printed pp. 103-104): section '2.35 FATHER' opens 'IE *pətér-, prob. starting fr. a nursery word of the pa type (above, p. 94) orig. pā, reduced to pə before the accent. Walde-P. 2.4.' and lists 'Type baba (above, p. 94) in It. babbo'. This is the source of Nourai's 'probably started as a nursery word'.\"},\n    {\"ref\": \"KAS:10\", \"status\": \"not_checked\", \"note\": \"Da'i al-Eslam, Khod-amuz-e Zaban-e Sanskrit — refs_online.json marks it 'Not on archive.org; PDF page exists, not fetched'. No copy available.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. pā-, pəter-, poti-\", \"stance\": \"partial\", \"note\": \"Three separate entries: 'pā-. To protect, feed. Contracted from *paə-. … [Pok. pā- 787, 1. pā(i)- 839.]'; 'pəter-. Father. … [Pok. pətē(r) 829.]'; 'poti-. Powerful; lord. … [Pok. poti-s 842.]'. Watkins never derives pəter- or poti- from pā-.\"},\n    {\"src\": \"WLD\", \"where\": \"WP II 72 f. (pā-), WP II 4 (pətēr), WP II 77 f. (poti-s), as cited by Pokorny\", \"stance\": \"partial\", \"note\": \"Pokorny's own 'References' lines send pā- to WP. II 72 f., pətēr to WP. II 4, poti-s to WP. II 77 f. — i.e. Walde-Pokorny too keeps the three apart.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann col. ~pā- / potis\", \"stance\": \"partial\", \"note\": \"IEC.txt: 'pä- \\\"feed, guard\\\". Cf. pāteió, pasKó, pastor-. WP II, 71' and separately 'potis \\\"able, powerful; master, husband\\\". Cf. pot-. WP II, 77'. Mann has two independent headwords.\"},\n    {\"src\": \"ARY\", \"where\": \"ARY_pages.txt, pdf p.101, headword بابا\", \"stance\": \"partial\", \"note\": \"Aryanpur heads the entry «بابا (واژه‌ی کودکانه به چم \\\"پدر\\\")» — 'baba (a childish word meaning father)' — with Greek/Latin/French/Spanish/Portuguese papa as cognates and a reference 'برهان قاطع: ۲۰۱'. He treats it as a nursery word in its own right, not as a derivative of a verbal root *pā-.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Pahlavi\",\n     \"words\": \"pâp, Pâpak\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Middle Persian Pāpak / Pābag (Pahlavi script 𐭯𐭠𐭯𐭪𐭩, Inscriptional MP p'pk') is well attested — it is the name of the father of Ardašīr I, the eponym of Ardašīr ī Pābagān, and Nyberg's glossary gives it exactly as 'Pāpak [p'pk'] the father of King Artaxšēr … — NP bab, baba \\\"father\\\"'. Formally it is pāp 'papa' + the MP hypocoristic/diminutive suffix -ak (< OIr. *-aka-), the same suffix as in mām-ak beside mām 'mother'; Mo'in's footnote in Borhan-e Qāte' analyses it word for word as «باب (پدر) + ک (پسوند دال بر عزّت و محبّت)», which is verbatim Nourai's 'Suffix -k indicates respect and love'. The simplex pāp 'father' as a common noun is thin: MacKenzie's Concise Pahlavi Dictionary knows only pid 'father' and has no pāp/pābag headword, so pāp is reconstructed from the derivative and from NP bāb/bābā rather than directly attested in the Book Pahlavi corpus. The derivation from PIE *peh₂- 'protect, feed' drawn by the arrow is not the modern account: pāp(ak), like Gk. pappas, Lat. pāpa and Skt. bappa, is an independent nursery reduplication (Pokorny's separate lemma pap(p)a 789), so the arrow root→node is a lumping, not a sound-law chain. Nourai's NOTE that BQT asserts cognacy with Latin papa without argument is accurate — the Mo'in footnote simply ends «در لاتینی papa و در تازی هم بابا مستعمل است».\",\n     \"derivation_fa\": \"«پاپک/بابک» در فارسی میانه (پهلوی) به‌روشنی گواهی شده است: نام پدر اردشیر بابکان است و نیبرگ در واژه‌نامهٔ خود می‌آورد Pāpak [p'pk'] «پدر اردشیر … فارسی نو bāb، bābā». ساخت آن pāp «بابا» + پسوند تصغیر و تحبیب ‎-ak‎ (از ایرانی باستان ‎*-aka-‎) است، همان‌گونه که «مامک» از «مام» ساخته می‌شود؛ حاشیهٔ معین بر برهان قاطع دقیقاً می‌نویسد «مرکب از: باب (پدر) + ک (پسوند دال بر عزّت و محبّت)» که همان گفتهٔ نورایی است. اما سادهٔ pāp به‌تنهایی در متون پهلوی کم‌گواه است؛ مکنزی تنها pid «پدر» را دارد. از سوی دیگر پیوند آن با ریشهٔ ‎*peh₂-‎ «پاسداری کردن» پذیرفتهٔ پژوهش امروزی نیست: pāpak مانند پاپاسِ یونانی و papaی لاتین واژه‌ای کودکانه (Lallwort) است و پوکورنی آن را سرواژه‌ای جداگانه (pap(p)a ص ۷۸۹) آورده است. حکم: با احتیاط پذیرفتنی است.\",\n     \"sources\": [W_BABK, W_BABA],\n     \"ref_check\": [\n      {\"ref\": \"BQT:202\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt leaf 422 (printed p. 201, footnotes continued «بقیه در صفحهٔ ۲۰۲» / «بقیه از صفحهٔ ۲۰۱» on the facing leaf, so the entry spreads over pp. 201-202). Headword «بابک»: «… و پرورنده و پدر را نیز گویند»; footnote 3 «پهلوی Pāpak «تبرکه ۱۷۰»، Pāpak نام پسر ساسان … و او نیز بشغل پدر منصوب گشت و وی پدر اردشیر اول موسس ساسانیان است «کریستنسن، ساسان ۸۹»»; footnote 4 «باین معنی مرکب از: باب (پدر) + ک (پسوند دال بر عزت و محبت)». That is exactly Nourai's node text; the page number is one off (the entry begins on 201).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, s.v. pid\", \"stance\": \"silent\", \"note\": \"PHD_mackenzie.txt line 4230: 'pid [AB' … | M pyd] father.' Grep for pāp / pʾpk / pābag in PHD.txt and PHD_mackenzie.txt returns nothing — MacKenzie's CPD has no pāp(ak) common noun.\"},\n      {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, p. 150\", \"stance\": \"supports\", \"note\": \"NYB_vol2_glossary.txt leaf 165 (the leaf whose running head reaches 'pardaxtan 151 Pārs'): 'Päpak [p'pk'] the father of King Artaxšēr, receives the naked title King (MLK? = šāh) … — NP bab, baba \\\"father\\\".' The index also has 'bab, baba: Papak'.\"},\n      {\"src\": \"HRN\", \"where\": \"Grundriss no. 147, p. 34\", \"stance\": \"supports\", \"note\": \"HRN.txt leaf 55: '147. bāb \\\"Vater\\\" (Šāhn. I, 43 Vers 172), Grossvater, vergl. bāba, babek. … phlv. papak (vergl. Nöldeke, Kārnāmak, 35 Note 3 …). arm. LW. pap \\\"Grossvater\\\".' Horn posits the same Pahlavi papak.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"bâb 1 «باب ۱»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"NP bāb 'father' (and its family bābā, bābū, bābak, Bābakān) continues MP pāpak exactly as Horn draws it: initial Middle Persian p- is voiced to b- in the New Persian reflex of this Lallwort (as in bābā beside Arm. loan pap), and the hypocoristic -ak > NP -ak/-a, giving bābak, while the shortened bāb is a back-formation used in verse — Horn's own citation is Šāhnāme I, 43 v. 172, and the couplet Nourai prints («سدیگر بپرسیدش افراسیاب / ازایران و از شهر و از مام و باب») is a Ferdowsī attestation with the pair mām 'mother' : bāb 'father'. Borhan-e Qāte' s.v. باب: «و بمعنی پدر هم آمده است که بعربی والد گویند، و باین معنی بلغت زند و پازند بابای فارسی باشد». Nourai's NOTE is well taken but should be split two ways: (a) NP باب in the ordinary modern language is a homonym, the Arabic loan bāb 'gate, chapter' (< Akkadian bābum via Aramaic), which is why the chart labels this one 'bâb 1' — Wiktionary's Persian باب entry lists only that Arabic word and 'appropriate', and has no 'father' sense at all; (b) the honorific bābā/bābū 'venerable elder, sufi master, sir' is not a different root but the same nursery word generalised (and re-borrowed through Turkish baba and Indo-Persian bābū), so no separate 'Baba' root is needed, though Nourai's cross-reference is harmless. Note also the homonymous Arabic بابا 'pope', which Wiktionary derives from Latin pāpa — a genuinely separate, Latin-mediated path.\",\n     \"derivation_fa\": \"«باب» و خانوادهٔ آن («بابا، بابو، بابک، بابکان») دنبالهٔ فارسی میانهٔ pāpak است. پِ آغازین فارسی میانه در این واژهٔ کودکانه در فارسی نو به «ب» بدل شده (pāpak > bābak) و صورت کوتاهِ «باب» در شعر به‌کار رفته است؛ هرن (شمارهٔ ۱۴۷، ص ۳۴) گواه شاهنامه (دفتر ۱، ص ۴۳، بیت ۱۷۲) را می‌آورد و بیت فردوسی «… و از مام و باب» جفت «مام : باب» را نشان می‌دهد. برهان قاطع نیز ذیل «باب» می‌نویسد «و بمعنی پدر هم آمده است که بعربی والد گویند». دربارهٔ یادداشت نورایی: نخست آنکه «بابِ» رایج امروز واژه‌ای دیگر و معرّب/وام‌گرفته از عربی «باب» (دَر، فصل) است و ویکی‌واژه برای «باب» فارسی اصلاً معنی «پدر» نیاورده؛ دوم آنکه «بابا/بابو» در معنی احترام‌آمیز ریشهٔ جداگانه ندارد و همان واژهٔ کودکانه است که معنایش گسترده شده است. ادعای نورایی در این گره درست است.\",\n     \"sources\": [W_BAB, W_BABA, W_BABK],\n     \"ref_check\": [\n      {\"ref\": \"BQT:202\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt leaf 422 (printed p. 201-202), s.v. «باب»: «… و بمعنی پدر هم آمده است که بعربی والد گویند ؟ وباین معنی بلغت زند وپازند (۱) بابای فارسی باشد»; the footnote continued on p. 202 lists «سنگلجی bāwā، سریکلی bāb … (پدربزرگ) «گریرسن ۷۴» … در لاتینی papa و در تازی هم بابا مستعمل است «نفی»» — the undocumented Latin-papa comparison Nourai flags in his NOTE.\"},\n      {\"ref\": \"HRN:34\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 55 (printed p. 34), entry 147: 'bāb \\\"Vater\\\" (Šāhn. I, 43 Vers 172), Grossvater, vergl. bāba, babek. g. bawg. phlv. papak … kurd. bāwā, ba-pīr, bāwuk.' Horn's footnote adds 'Pāhl. Pap bedeutet im Np. nur \\\"Papst\\\" (ital. papa)'. Page and content match Nourai exactly.\"},\n      {\"ref\": \"NYB:150\", \"status\": \"supports\", \"note\": \"NYB_vol2_glossary.txt leaf 165 (printed p. 150): 'Päpak [p'pk'] … — NP bab, baba \\\"father\\\".' Nyberg himself draws the MP → NP arrow.\"},\n      {\"ref\": \"MON:428\", \"status\": \"partial\", \"note\": \"The local copy is the 2-vol Adena reprint, whose pagination differs from the 6-vol Amir Kabir set Nourai cites, so p. 428 cannot be confirmed. The entries are there: MON_part1.txt line 19641 «بابک: Pāpak [مصغّر باب] (اِ.) پدر (به تحبیب)» and «بابو: [قس. باب] (اِ.) پدر، بابا …», i.e. Mo'in gives the same MP Pāpak and the same 'diminutive of bāb' analysis.\"},\n      {\"ref\": \"AEF:197\", \"status\": \"not_checked\", \"note\": \"Khaleqi Motlaq's Persian version of Horn (Asās-e Eštteqāq-e Fārsi, vol. I) — refs_online.json has only a catalogue record (OpenLibrary), no scan. Its content for this word is by definition Horn no. 147, which was checked.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HUB\", \"where\": \"Persische Studien\", \"stance\": \"silent\", \"note\": \"grep for 'bāb', 'bab ', 'papak', 'bābā' in HUB.txt returns nothing — Hübschmann does not treat Horn's no. 147.\"},\n      {\"src\": \"ARY\", \"where\": \"ARY_pages.txt pdf p.101, headword «بابا»\", \"stance\": \"partial\", \"note\": \"Aryanpur heads it «بابا (واژه‌ی کودکانه به چم \\\"پدر\\\")» with Kurdish BAB, Greek/Latin/French/Spanish/Portuguese PAPA and 'برهان قاطع: ۲۰۱' — same word family, but classified as a nursery word, with no Iranian sound-law chain.\"},\n      {\"src\": \"BQT\", \"where\": \"vol. 1 pp. 201-202\", \"stance\": \"supports\", \"note\": \"see ref_check; also s.v. «بابک»: «و صغیرِ باب هم هست چنانکه مامک تصغیر مام» — bābak is to bāb as māmak is to mām.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Germanic\",\n     \"words\": \"fôd; fadar\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Two separate Germanic formations, both correctly placed under the root box. (a) Proto-Germanic *fōdô 'food' (OE fōda, Goth. fōdeins) and its denominative *fōdjan 'to feed' (OE fēdan, Goth. fōdjan) go back to the t-extension *peh₂-t- of the root: Watkins, 'Extended form *pāt- in: a. Germanic *fōd-, food, in Old English foda, food: FOOD; b. Germanic denominative *fōdjan … FEED; c. suffixed form *pāt-tro- in Germanic *fōstra- … FOSTER'; Grimm's law turns PIE *p- into Gmc. *f- and the long *ā of *pāt- appears as Gmc. *ō. (b) Gothic fadar / PGmc. *fadēr 'father' continues *ph₂tḗr with Grimm's law *p > f and Verner's law *t > *ð (whence the -d- of fadar, OE fæder), the accent having stood on the ending. Nourai's gloss 'fadar: feeder, father' encodes his Pa + ter analysis; that analysis is the one Wiktionary reports as the usual view for *ph₂tḗr, so the arrow is defensible, but note that Pokorny (829) and Watkins keep *ph₂tḗr as a separate lemma.\",\n     \"derivation_fa\": \"این گره دو ساخت ژرمنی جداگانه دارد و هر دو در جای درست‌اند. نخست ژرمنی آغازین ‎*fōdô‎ «خوراک» و فعل مشتق ‎*fōdjan‎ «خوراک دادن» از گسترشِ ‎*peh₂-t-‎ ریشه‌اند؛ بنا بر واتکینز «*pāt- در ژرمنیِ *fōd- (انگلیسی کهن foda) و *fōdjan (fēdan)»؛ در اینجا «پ» هندواروپایی بر پایهٔ قانون گریم به «ف» و آی بلندِ ریشه به ō بدل شده است. دوم gothic fadar از ‎*ph₂tḗr‎ می‌آید: «پ» به «ف» (قانون گریم) و «ت» بر اثر قانون ورنر به «ذ/د» بدل شده، چون تکیه بر پایانه بوده است. برچسب نورایی «fadar: خوراک‌دهنده، پدر» بازتاب همان تجزیهٔ «پا + تر» است که ویکی‌واژه آن را دیدگاه رایج می‌شمارد، هرچند پوکورنی و واتکینز ‎*ph₂tḗr‎ را سرواژه‌ای مستقل نگاه می‌دارند. ادعای نورایی در این گره درست است.\",\n     \"sources\": [E_PA, W_PTR, E_FUR],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. pā-: '3. Extended form *pāt- in: a. Germanic *fōd-, food, in Old English foda, food: FOOD; b. Germanic denominative *fōdjan, to give food to, in Old English fēdan, to feed: FEED'; and s.v. pəter-: '1. Germanic *fadar in Old English fæder (> Middle English fader), father: FATHER; FOREFATHER.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW 787 and 829\", \"stance\": \"supports\", \"note\": \"POK_full.txt s.v. pā-: 'Gothic fōdjan \\\"nourish\\\", Old Icelandic fœða, Old English fēdan … Old English foda, engl. food \\\"nourishment, food\\\"'; s.v. pətēr (Page(s): 829) lists the Germanic father words.\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. feed, food\", \"stance\": \"supports\", \"note\": \"KLN_1966.txt: 'feed … fr. OE. fēdan, rel. to OS. fōdjan, ON. fœða, OFris. fēda, OHG. fuotan, Goth. fōdjan, \\\"to feed\\\", Goth. fōdeins, OE. fōda, \\\"food\\\". See food.'\"},\n      {\"src\": \"IEC\", \"where\": \"Mann s.v. pā-\", \"stance\": \"supports\", \"note\": \"IEC.txt: 'pä- \\\"feed, guard\\\" … WP II, 71' with the Gmc. *fōd- family under the related pastor-/postor- entries ('For OE fostor- \\\"foster-\\\" … see postor-, radical: pot-, pō- \\\"feed\\\"').\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"English\",\n     \"words\": \"food, feed, fur; father, pattern\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Four of the five words are straightforward Germanic inheritances from node #3: food < ME fode < OE fōda; feed < ME feden < OE fēdan; father < ME fader < OE fæder. 'fur' is the least obvious but is correct and is the standard account: ME furre 'trimming, lining' from the verb furren < OF forrer, fourrer 'to line, cover', from OF fuerre/forre 'sheath, scabbard', from Frankish *fōdr = PGmc. *fōdram 'sheath, lining' (OHG fōtar, Goth. fōdr 'sword sheath'), i.e. the *pā-trom formation of the same root — Etymonline: 'from Proto-Germanic *fodram \\\"sheath\\\" … from PIE root *pa- \\\"to feed, protect\\\"', and Watkins puts FUR under pā- in so many words. So it reaches English through Old French but from a Germanic (Frankish) etymon, which is why Nourai's Germanic→English arrow still holds. 'pattern' is the one misfiled word: it is not Germanic at all but a Modern English variant of patron, from Old French patron, from Medieval/Latin patrōnus 'protector, model' from Latin pater — i.e. it belongs on the Latin branch (node #5/#6) beside paternal and patronage, not under Germanic fadar. Everything else confirmed; node downgraded to plausible for pattern.\",\n     \"derivation_fa\": \"چهار واژه از پنج واژه میراث مستقیم ژرمنی از گرهٔ پیشین‌اند: food از انگلیسی کهن fōda، feed از fēdan و father از fæder. «fur» دیرفهم‌تر ولی درست است: از انگلیسی میانهٔ furre، از فرانسهٔ کهن forrer/fourrer «آستر کردن»، از fuerre «نیام، غلاف»، از فرانکیِ ‎*fōdr‎ = ژرمنی آغازین ‎*fōdram‎ (آلمانی علیای کهن fōtar، گوتی fōdr «نیام شمشیر») که همان ساخت ‎*pā-trom‎ از همین ریشه است؛ پس هرچند از راه فرانسه به انگلیسی رسیده، خاستگاهش ژرمنی (فرانکی) است و پیکان نورایی برجاست. اما «pattern» در جای نادرست نشسته است: این واژه گونه‌ای از patron است، از فرانسهٔ کهن patron، از لاتین patrōnus، از pater؛ یعنی باید در شاخهٔ لاتین کنار paternal و patronage بیاید نه زیر fadar ژرمنی. به همین سبب حکم گره «با احتیاط پذیرفتنی» است.\",\n     \"sources\": [E_FUR, E_PAT, E_PA],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. pā-: '1. Suffixed form *pā-trom in Germanic *fōdram in: a. Old English fōdor, fodder: FODDER; b. Old French feurre, fodder: FORAGE; c. Old French forreure, trimming made from animal skin, fur (< \\\"sheath, case, lining\\\"): FUR.' FOOD and FEED likewise. But the AHD index line reads 'PATTERN pəter-', i.e. Watkins files pattern under the Latin/pater branch.\"},\n      {\"ref\": \"DVS:142\", \"status\": \"not_checked\", \"note\": \"P. Davies, Roots: Family Histories of Familiar Words (1981) — refs_online.json: archive.org lending-only copy, not readable.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. fur, pattern, patron\", \"stance\": \"partial\", \"note\": \"KLN_1966.txt: 'fur, v. — ME. furren, fr. OF. forrer …, fr. OF. fuerre, forre, \\\"sheath, case, covering\\\" … fr. Frankish *fōdr, which corresponds to OHG. fotar, fuotar, \\\"a cover, coverlet\\\"'; but 'pattern, n. — ME. patron, fr. OF. patron … See patron' and 'patron, n. — … fr. L. patrōnum, acc. of patrōnus, \\\"protector\\\", fr. pater'. Confirms fur, contradicts the Germanic placement of pattern.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, s.v. FUR / PATTERN\", \"stance\": \"silent\", \"note\": \"grep of SKT.txt for '^FUR' and '^PATTERN' produced no headword lines in this OCR (the caps headwords are broken up by the scan); nothing usable retrieved.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"Latin\",\n     \"words\": \"potere (potis); pâscere; pater\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Three Latin words, two of which sit correctly under the root box and one of which does not. (a) pāscere 'to graze, feed' is the sḱ-present *peh₂-sḱ-e/o- of the root (Klein: 'pāscere … which stands for pā-scere and derives fr. I.-E. base *pā-'); its participle pāstus gives pāstor 'feeder, shepherd', and the ti-derivative *pā-st-ni- gives pānis 'bread'. Confirmed. (b) pater 'father' is the regular Italic reflex of *ph₂tḗr (Pokorny 829); Nourai's gloss 'feeder, father' again encodes his Pa+ter reading. (c) potis 'able, powerful' and Vulgar Latin *potēre (for Classical posse < potis + esse, whence potuī, potēns, potestās) belong to *pótis 'master, husband', which no standard authority derives from *peh₂-; Klein s.v. potent expressly puts it with OI patiḥ, Gk. πόσις, Lith. pats, Hitt. -pat 'self', i.e. Pokorny's separate lemma poti-s (842). The chart's own reference POK:847 is wrong in any case: IEW p. 847 carries ptel(e)ia 'a kind of tree' and pū-1/peu- 'to blow'; the pages wanted are 787 (pā-), 829 (pətēr) and 842 (poti-s). Node therefore plausible.\",\n     \"derivation_fa\": \"سه واژهٔ لاتین در این گره است. یکم pāscere «چرانیدن، خوراک دادن» که ستاکِ ‎-sḱ-‎ از همان ریشه است (‎*peh₂-sḱ-e/o-‎)؛ کلاین می‌نویسد «pāscere که در اصل pā-scere است و از ریشهٔ ‎*pā-‎ می‌آید». اسم فاعل آن pāstor «چوپان، خوراک‌دهنده» و مشتق دیگرش pānis «نان» است. دوم pater «پدر» بازتاب منظم ‎*ph₂tḗr‎ در ایتالیایی باستان است. سوم potis «توانا» و لاتین عامیانهٔ ‎*potēre‎ (به‌جای posse کلاسیک از potis + esse) که به ‎*pótis‎ «سرور، شوی» بازمی‌گردد و هیچ مرجع معتبری آن را از ‎*peh₂-‎ نمی‌گیرد؛ کلاین آن را با patiḥ سنسکریت، πόσις یونانی، pats لیتوانیایی و ‎-pat‎ هیتی «خود» می‌سنجد. افزون بر این، ارجاع POK:847 نادرست است: صفحهٔ ۸۴۷ پوکورنی به ptel(e)ia «نوعی درخت» و pū-/peu- «دمیدن» می‌پردازد؛ صفحه‌های درست ۷۸۷ و ۸۲۹ و ۸۴۲ است. حکم: با احتیاط پذیرفتنی است.\",\n     \"sources\": [W_POT, W_PA, E_PA],\n     \"ref_check\": [\n      {\"ref\": \"POK:847\", \"status\": \"not_found\", \"note\": \"POK_full.txt: the lemmas whose 'Page(s):' line reads 847 are 'ptel(e)ia — Meaning: a kind of tree' and 'pū-1, peu-, pou-, also phu- — Meaning: to blow, blow up'. Neither has anything to do with potis, pāscere or pater. The relevant IEW pages are 787 (pā-: pə- and pā-t-), 829 (pətēr) and 842 (poti-s). Apparently a slip for 842.\"},\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. pā-: '4. Extended form *pās- in: a. suffixed form *pās-sko- in Latin pāscere, to feed: PASTURE …; b. Latin pāstor, shepherd: PASTOR; c. suffixed form *pās-t-ni- in Latin pānis, bread'; s.v. pəter-: '2. Latin pater, father'; s.v. poti-: '1. Latin potis, powerful, able (> potestas, power) … 2. Latin compound posse, to be able (contracted from potis, able + esse, to be)' — but as a separate root.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. pastor, pantry, potent\", \"stance\": \"partial\", \"note\": \"'pastor … fr. pastus, pp. of pāscere, \\\"to graze, pasture, feed\\\", which stands for pā-scere and derives fr. I.-E. base *pā-, \\\"to tend, keep, pasture, feed, guard, protect\\\"' and 'pantry … fr. L. pānis, \\\"bread\\\", fr. I.-E. base *pā-'; but 'potent … fr. potis, \\\"able, capable, powerful\\\", which is cogn. with OI. patiḥ, \\\"master, husband\\\", … Lith. pats, Lett. pats, Hitt. pat, \\\"self\\\"' — no link to *pā-.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann s.v. potis\", \"stance\": \"partial\", \"note\": \"IEC.txt: 'potis \\\"able, powerful; master, husband\\\". Cf. pot-. WP II, 77 … OLat. pos, gs: potis, Lat. potis … adj. \\\"powerful\\\"' — a headword independent of Mann's 'pä- \\\"feed, guard\\\"'.\"},\n      {\"src\": \"POK\", \"where\": \"IEW 842 s.v. poti-s\", \"stance\": \"partial\", \"note\": \"'Latin potis (potior, potissimus) \\\"wealthy, mighty\\\", possum, Old Latin also potis sum \\\"kann\\\", potuī, potens from an e-denominative … potestas \\\"power\\\"' — supports the Latin words, contradicts their attachment to pā-.\"}\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"English\",\n     \"words\": \"potent, potential, power, possible, possess; pasture, pantry, company; paternal, patronage\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"All nine are Latin-via-French/learned borrowings and each matches its Latin parent in node #5. potent < L. potēns, -entis, present participle of posse (potis + esse); potential < LL potentiālis; power < ME poer < OF pooir < Vulgar Latin *potēre (Klein: 'power … fr. OF. pooeir, pooir, v., fr. VL. *potere (corresponding to L. posse)') — this is precisely the *potere Nourai prints in the Latin box; possible < L. possibilis from possum; possess < L. possidēre (potis + sedēre 'to sit', 'to sit as master'). pasture < LL pāstūra from pāscere; pantry < OF paneterie from ML panetaria, from pānis; company < ML compānia 'a sharing of bread' (com- + pānis), a calque on Gothic gahlaiba. paternal < L paternus from pater; patronage < OF patronage from ML patrōnāticum, from patrōnus < pater. Nothing here is doubtful; the only caveat is inherited from node #5 (the potis group has a different PIE etymon from the pā- group).\",\n     \"derivation_fa\": \"هر نه واژه وام‌واژه‌های لاتین‌اند که از راه فرانسه یا از راه دانشورانه به انگلیسی رسیده‌اند و هر کدام با نیای لاتین خود در گرهٔ پیشین می‌خواند: potent از potēns (اسم فاعل posse)، potential از potentiālis لاتین متأخر، power از فرانسهٔ کهن pooir از لاتین عامیانهٔ ‎*potēre‎ (کلاین: «power … از pooir فرانسهٔ کهن، از ‎*potere‎ لاتین عامیانه معادل posse»)، possible از possibilis و possess از possidēre («چون سرور نشستن»). pasture از pāstūra و pantry از paneterie فرانسهٔ کهن (از pānis «نان») و company از compānia لاتین میانه «هم‌نانی». paternal از paternus و patronage از patrōnus، هر دو از pater. هیچ‌یک تردیدبرانگیز نیست؛ تنها احتیاطِ به‌ارث‌رسیده همان جدایی ریشهٔ potis از ریشهٔ pā- است.\",\n     \"sources\": [E_PA, W_POT],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. poti-: 'Latin potis, powerful, able (> potestas, power): PODESTA, POSSESS, POWER … Latin compound posse … : POSSIBLE, POTENT; (IMPOTENT), PREPOTENT'; s.v. pā-: 'Latin pāscere, to feed: PASTURE; ANTIPASTO, PESTER, REPAST … Latin pānis, bread …: PANADA, … PANTRY, PASTILLE; APPANAGE, COMPANION, (COMPANY)'; s.v. pəter-: 'Latin pater … : PADRE, PATER, PATERNAL, PATRI-, PATRICIAN, PATRIMONY, PATRON'.\"},\n      {\"ref\": \"DVS:142\", \"status\": \"not_checked\", \"note\": \"Davies, Roots (1981) — archive.org lending copy only, not readable.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.vv. potent, power, possible, pantry, pastor/pasture, paternal\", \"stance\": \"supports\", \"note\": \"'potent … pres. part. of posse (for potis esse)'; 'power … fr. VL. *potere'; 'possible … fr. L. possibilis … fr. possum'; 'pantry … fr. ML. panetaria … fr. L. pānis'; 'paternal … fr. L. paternus … fr. pater'. All as charted.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict.\", \"stance\": \"silent\", \"note\": \"grep of SKT.txt for '^POTENT', '^PASTURE', '^PANTRY' returned no headword lines in this OCR; no additional evidence obtained.\"}\n     ]\n    },\n    {\n     \"id\": 7,\n     \"lang\": \"Greek\",\n     \"words\": \"pater, pappas\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Greek πατήρ (patḗr) 'father' is the regular reflex of *ph₂tḗr (laryngeal vocalised as a, inherited accent shift in the vocative πάτερ), and belongs here on Nourai's Pa+ter analysis exactly as in node #3/#5. πάππας (pappas) 'papa', with its by-forms πάππος 'grandfather' and the vocative πάπα, is however not a derivative of the verbal root at all but an independent nursery reduplication of the pa-pa type: Pokorny gives it its own lemma pap(p)a at IEW 789, and Watkins likewise has a separate entry 'papa. A child's word for \\\"father\\\", a linguistic near-universal found in many languages. 1. French papa, father: PAPA. 2. Greek pappas, father, and pappos, grandfather: PAPPUS, POPE. [Pok. pap(p)a 789.]'. Nourai's root box anticipates the objection by saying the whole family 'has probably started as a nursery word', but as drawn the arrow root→pappas conflates two distinct Pokorny lemmas, so plausible rather than confirmed.\",\n     \"derivation_fa\": \"«πατήρ» یونانی بازتاب منظم ‎*ph₂tḗr‎ است (حنجری به a بدل شده) و بر پایهٔ تجزیهٔ نورایی (پا + تر) در جای خود نشسته است. اما «πάππας» با گونه‌های πάππος «پدربزرگ» و ندایی πάπα، مشتق ریشهٔ فعلی نیست بلکه واژه‌ای کودکانه با تکرار هجای pa-pa است: پوکورنی برای آن سرواژه‌ای جداگانه دارد (pap(p)a، ص ۷۸۹) و واتکینز نیز مدخل مستقل «papa» را می‌آورد و می‌نویسد «واژه‌ای کودکانه برای \\\"پدر\\\" که در بسیاری از زبان‌ها نزدیک به همگانی است». جعبهٔ ریشه در کتاب خود می‌گوید این خانواده «احتمالاً از واژه‌ای کودکانه آغاز شده»، ولی پیکانی که کشیده شده دو سرواژهٔ جدا را یکی می‌کند. حکم: با احتیاط پذیرفتنی است.\",\n     \"sources\": [W_PTR, E_POPE],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt s.v. pəter-: '3. Greek patḗr, father: PATRIOT; ALLOPATRIC, EUPATRID, PATRIARCH, SYMPATRIC. [Pok. pətē(r) 829.]' — supports pater. But pappas is under a different headword: 'papa. A child's word for \\\"father\\\" … 2. Greek pappas, father, and pappos, grandfather: PAPPUS, POPE. [Pok. pap(p)a 789.]'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW 789 (pap(p)a) and 829 (pətēr)\", \"stance\": \"partial\", \"note\": \"POK_full.txt has 'Root / lemma: pap(p)a … Page(s): 789' as a lemma of its own, distinct from 'pətēr … Page(s): 829' and from 'pā- … Page(s): 787'.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 2.35, p. 103\", \"stance\": \"supports\", \"note\": \"Buck: 'IE *pətér-, prob. starting fr. a nursery word of the pa type … orig. pā, reduced to pə before the accent' — i.e. Buck too traces the family to a nursery pa, which is the only sense in which pater and pappas share an origin.\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. papa, pope\", \"stance\": \"supports\", \"note\": \"KLN_1966.txt: 'papa, n., pope; parish priest. — Eccles L. pāpa, \\\"bishop; pope\\\", fr. L. pāpa, \\\"father\\\".' Klein treats pāpa as the nursery word.\"}\n     ]\n    },\n    {\n     \"id\": 8,\n     \"lang\": \"English\",\n     \"words\": \"patriot, Pope, papa\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"patriot: MF/F patriote from Late Latin patriōta from Greek πατριώτης 'fellow-countryman', from πατριά 'lineage' from πατήρ — a clean Greek→Latin→French→English chain matching the node's parent (Klein, s.v. patriot). Pope: OE papa (9th c.) from Church Latin papa 'bishop, pope', which is the Greek παπᾶς 'patriarch, bishop', originally 'father'; the title was applied to bishops of Asia Minor, taken by the Bishop of Alexandria c. 250, and claimed exclusively by the Bishop of Rome from 1073 — so the Greek parent is right, though the word reached English through Latin. papa 'father' (1680s) is the odd one out: Etymonline derives it 'from French papa, from Latin papa, originally a reduplicated child's word, similar to Greek pappa (vocative) \\\"o father\\\", pappas', and AHD files PAPA under French papa. It is thus a parallel nursery word taken from French, not a descendant of Greek πάππας; the chart's Greek→English arrow is not the route for this word. Node plausible for that reason.\",\n     \"derivation_fa\": \"«patriot» از فرانسهٔ میانه patriote، از لاتین متأخر patriōta، از یونانی πατριώτης «هم‌میهن» (از πατριά و πατήρ) می‌آید و زنجیرهٔ آن با نیای گره می‌خواند. «Pope» از انگلیسی کهن papa (سدهٔ نهم م.)، از لاتین کلیسایی papa «اسقف، پاپ»، از یونانی παπᾶς «پدر، اسقف»؛ این لقب نخست برای اسقفان آسیای صغیر و از حدود ۲۵۰ م. برای اسقف اسکندریه به‌کار می‌رفت و از ۱۰۷۳ م. ویژهٔ اسقف رم شد — پس نیای یونانی درست است هرچند واژه از راه لاتین به انگلیسی رسیده. اما «papa» (از ۱۶۸۰ م.) از فرانسهٔ papa و لاتین papa است، نه از παππας یونانی؛ یعنی واژه‌ای کودکانهٔ موازی است که از فرانسه وام گرفته شده. به همین سبب حکم گره «با احتیاط پذیرفتنی» است.\",\n     \"sources\": [E_POPE, W_PTR],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt s.v. pəter-: 'Greek patḗr, father: PATRIOT …' — supports patriot. But POPE and PAPA are indexed to the separate root: 'papa. A child's word for \\\"father\\\" … 1. French papa, father: PAPA. 2. Greek pappas, father, and pappos, grandfather: PAPPUS, POPE. [Pok. pap(p)a 789.]', and the AHD index line reads 'PAPA papa'.\"},\n      {\"ref\": \"DVS:142\", \"status\": \"not_checked\", \"note\": \"Davies, Roots (1981) — lending-only scan on archive.org, not readable.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.vv. patriot, pope, papa\", \"stance\": \"supports\", \"note\": \"'patriot, n. — MF. (= F.) patriote, fr. Late L. patriōta, fr. Gk. πατριώτης, \\\"fellow countryman\\\"'; 'pope, n. — ME. pope, fr. OE. papa, fr. Eccles. L. papa, \\\"bishop; pope\\\", fr. L. papa, \\\"father\\\"'.\"},\n      {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dict., vol. 1 (A-?)\", \"stance\": \"silent\", \"note\": \"only volume 1 of the 1962 printing is open (refs_online.json); the p- words are in the missing volume 2, so nothing could be checked there.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 4,\n   \"root\": \"Pak, Pag\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *peh₂ǵ- / *peh₂ḱ- 'to fasten, fix, attach' (Pokorny pā̆ḱ-, pā̆ǵ- 787-788; AHD pag-/pak-)\",\n   \"note\": \"Root, language label, gloss and page reference are all correct. Pokorny's lemma (POK_full.txt) reads 'Root / lemma: pāḱ- and pāǵ- / Meaning: to repair, strengthen / Grammatical information: present *pag-mi, pāḱ-si, pāḱ-ti … References: WP. II 2 f., WH. II 232 f., 235 f., 245 f., Trautmann 209. Page(s): 787-788'; Watkins has 'pag-. Also pak-. To fasten. … [Pok. pak- 787.]'; Wiktionary reconstructs *peh₂ǵ- (alt. *peh₂ḱ-) 'to attach, fix, fasten'. Nourai's two-form headword Pak, Pag reproduces exactly the ḱ/ǵ doublet the sources posit, and 'to fasten' is Watkins's own gloss word for word.\",\n   \"note_fa\": \"ریشه، برچسب زبانی، معنا و شمارهٔ صفحه همگی درست‌اند. پوکورنی سرواژهٔ «pāḱ- و pāǵ-» را با معنی «استوار کردن، بستن» در صفحهٔ ۷۸۷–۷۸۸ می‌آورد و واتکینز «pag-، نیز pak-: بستن، محکم کردن» می‌نویسد؛ ویکی‌واژه آن را ‎*peh₂ǵ-‎ (گونهٔ ‎*peh₂ḱ-‎) «چسباندن، استوار کردن، بستن» بازسازی می‌کند. دوگانهٔ «Pak, Pag» در کتاب دقیقاً همان جفت ḱ/ǵ منابع است و معنی «to fasten» واژه‌به‌واژه از واتکینز است. ادعای نورایی درست است.\",\n   \"sources\": [W_PAG, E_PAG],\n   \"ref_check\": [\n    {\"ref\": \"POK:787\", \"status\": \"supports\", \"note\": \"POK_full.txt: 'Root / lemma: pāḱ- and pāǵ- / Meaning: to repair, strengthen … Page(s): 787-788'. The entry contains Av. pas-, Lat. pangere/pacīscī/pāx/pālus/pāgus/prōpāgēs and Gmc. *fanxan — i.e. every item Nourai charts.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. pag-\", \"stance\": \"supports\", \"note\": \"'pag-. Also pak-. To fasten. 1. Lengthened-grade form *pāk- in Germanic *fōgjan … 3. Root form *pak- in: a. Latin pāx, peace … 5. Lengthened-grade form *pāg- in: a. Latin pāgus … [Pok. pak- 787.]'\"},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. pāḱ- and pāg- (1)\", \"stance\": \"supports\", \"note\": \"IEC.txt: 'pāḱ- \\\"fix, tie, bind, join; bond, fixture, pact\\\". Element of the following. WP II, 2-7' and 'pāg- (1) \\\"harden, fix, fit. Cf. pāḱ-. WP II, 3'.\"},\n    {\"src\": \"WLD\", \"where\": \"WP II 2 f. (as cited by Pokorny)\", \"stance\": \"supports\", \"note\": \"Pokorny's 'References: WP. II 2 f.' for this lemma; Band I-II of Walde-Pokorny are only partially available locally, but the cross-reference itself locates the entry.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan\",\n     \"words\": \"pas\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Avestan paš- 'to bind, fetter' is genuine and is the zero/short-grade Iranian reflex of *peh₂ḱ-: Bartholomae's Altiranisches Wörterbuch (col. 879-880) has '• j. paš- V. \\\"fesseln\\\". j-Aor. 1 paš-. — PPfP. *paxšta-', with the compound paiti-ā-paš- glossed 'zusammen-, aneinander-fesseln' and the Vendidad passage 'ayaŋhaēnibiš bibdaibiš paiti āpašta \\\"mit eisernen Fesseln soll man seine Knochen zusammenfesseln\\\" V. 4.51'. Bartholomae also lists pasvant- 'provided with *pas- (f. \\\"Strick\\\"?)' and Mann adds Av. pasman- n. 'bond'. The Indo-Iranian correspondence is Skt. pā́śa- 'cord, noose, fetter', pāśáyati 'to tie', so PIE *peh₂ḱ- > Indo-Iranian *pāć- > Av. paš- (the palatal *ć giving Avestan š), which is the standard sound law. Nourai's gloss 'to tie, fetter' is verbatim Klein's. The node has no Persian continuation drawn, which is correct: NP has no direct reflex of this verb (the empty box drawn beside it on the printed page carries no language label and no words).\",\n     \"derivation_fa\": \"اوستایی paš- «بستن، به بند کشیدن» واژه‌ای راستین و بازتاب ایرانیِ ریشهٔ ‎*peh₂ḱ-‎ است. بارتولومه در فرهنگ ایرانی باستان (ستون ۸۷۹–۸۸۰) می‌آورد «paš- فعل: fesseln (به بند کشیدن)» و صورت ترکیبی paiti-ā-paš- «به هم بستن» را با شاهد وندیداد ۴٫۵۱ «با بندهای آهنین باید استخوان‌های او را به هم بست» نقل می‌کند. هم‌ریشهٔ هندی آن سنسکریت pā́śa- «ریسمان، بند» و pāśáyati «بستن» است؛ پس ‎*peh₂ḱ-‎ > هندوایرانی ‎*pāć-‎ > اوستایی paš- (کامیِ ‎*ć‎ در اوستایی به š بدل می‌شود) که قانونی آوایی و شناخته‌شده است. معنایی که نورایی داده («to tie, fetter») واژه‌به‌واژه از کلاین است. ادعای نورایی درست است.\",\n     \"sources\": [W_PAG, E_PAG],\n     \"ref_check\": [\n      {\"ref\": \"POK:787\", \"status\": \"supports\", \"note\": \"POK_full.txt s.v. pāḱ-/pāǵ-: 'Old Indic pāś- (Instr. Pl. pāḍbhíḥ) \\\"loop, noose, snare, rope\\\", pāśa- m. ds. … Avestan pas- \\\"join each other, fasten, bind, piece together …\\\", fsabiš \\\"in chains\\\"'. Page 787-788.\"},\n      {\"ref\": \"KLN:1110\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 593 (the leaf between the pages numbered 1108 and 1113/1114, i.e. printed pp. 1109-1110), s.v. pact: '… fr. I.-E. base *pak-, *pāg-, \\\"to join together, unite, make firm, fasten, fix\\\", whence also L. pangere … pālus (for *pak-slos), \\\"post, stake\\\", OI. pāś-, pāśa-, \\\"cord, rope\\\", Avestic paš-, \\\"to fetter\\\", Gk. πηγνύναι …'. Nourai's gloss 'to tie, fetter' is Klein's 'to fetter'; the page number is exact.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch, col. 879-880\", \"stance\": \"supports\", \"note\": \"'• j. paš- V. \\\"fesseln\\\". j-Aor. 1 paš-. — PPfP. *paxšta-'; 'mit paiti- und ā \\\"zusammen-, aneinander-fesseln\\\": ayaŋhaēnibiš bibdaibiš paiti āpašta \\\"mit eisernen Fesseln soll man seine Knochen zusammenfesseln\\\" V. 4.51'.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann s.v. pāḱ-\", \"stance\": \"supports\", \"note\": \"'Short grade in Av. pas-, v. \\\"tie\\\"; pasmən, n. \\\"bond\\\" … Long grade in Skt. pāśaḥ, m. \\\"bond, noose, fetter\\\"; pāśayāmi, v. \\\"tie\\\"' and 'Extended types (*pāḱmn̥-) in Av. pasman-, n. \\\"tie\\\"'.\"},\n      {\"src\": \"KNT\", \"where\": \"Kent, Old Persian lexicon\", \"stance\": \"silent\", \"note\": \"grep of KNT.txt for a Old Persian paθ-/paš- 'bind' finds nothing; the verb is not attested in the Achaemenid inscriptions, so Kent has no entry — consistent with the chart, which labels the node Avestan only.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Latin\",\n     \"words\": \"pangere; pacîcî; pâlus; pâgus; prô-pâgĕs\",\n     \"verdict\": \"transcription_suspect\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"pacîcî\",\n     \"correct_form\": \"pacīscī\",\n     \"derivation\": \"Four of the five Latin forms are exactly right and all five belong to *peh₂ǵ-/*peh₂ḱ-. pangere 'to fasten, fix' is the nasal-infix present *ph₂-né-ǵ- (perfect pepigī, later pēgī after frēgī); pālus 'stake, pole' is *pak-slos with -ks-l- > -l- and compensatory lengthening (diminutive paxillus preserves the -k-); pāgus 'district' is literally 'boundary staked out on the ground', the lengthened grade *pāg-o-, whence pāgina 'the papyrus strips fastened together, page'; prōpāgēs / prōpāgō 'layer of a vine, offspring' is prō- + the same *pāg- ('a fixing before'). The second word is misprinted: the page (pdf 380, book 350) plainly shows 'pacîcî : to agree', which is not a Latin form; the verb is pacīscī (deponent, 1st sg. pacīscor, Old Latin paciō), 'to make a treaty, agree', related to pāx, pācis 'peace'. The JSON reproduces the printed page faithfully, so this is Nourai's own typesetting error (a dropped -s- in each syllable of pacīscī), not an extraction error. Compare Pokorny 787: 'Latin pacīscō (sek. -or) \\\"einen Vertrag oder Vergleich festmachen, abschließen\\\", Old Latin pacio, pactio … pāx, -cis f. \\\"peace\\\" … pālus \\\"picket, pole\\\" (from *pak-slos, compare Demin. paxillus); pangō … pāgus \\\"rural community, village\\\" … propāgō, propāgēs \\\"Setzlinge\\\"'.\",\n     \"derivation_fa\": \"چهار صورت از پنج صورت لاتین درست‌اند و هر پنج به ریشهٔ ‎*peh₂ǵ-/*peh₂ḱ-‎ بازمی‌گردند: pangere «استوار کردن» ستاک حالِ با میان‌وند خیشومی ‎*ph₂-né-ǵ-‎ است (ماضی pepigī و سپس pēgī به قیاس frēgī)؛ pālus «میخ، ستون» از ‎*pak-slos‎ است که خوشهٔ ‎-ksl-‎ در آن ساده شده و واکه کشیده شده (مصغّر paxillus هنوز ک را دارد)؛ pāgus «ناحیه» یعنی «مرزِ با میخ نشان‌شده»، از درجهٔ کشیدهٔ ‎*pāg-‎، که pāgina «صفحه» نیز از آن است؛ و prōpāgēs «قلمه، نژاد» از prō- و همان ‎*pāg-‎. اما واژهٔ دوم غلط چاپی است: در صفحهٔ چاپی (صفحهٔ ۳۵۰ کتاب) «pacîcî : to agree» آمده که صورتی لاتین نیست؛ صورت درست pacīscī (فعل ناگذرای مجهول‌نما، اول شخص pacīscor) «پیمان بستن» است، هم‌خانوادهٔ pāx، pācis «صلح». استخراج JSON با صفحهٔ چاپی می‌خواند، پس خطا از خودِ کتاب است نه از خوانش اسکن.\",\n     \"sources\": [W_PAG, E_PAG],\n     \"ref_check\": [\n      {\"ref\": \"KLN\", \"status\": \"supports\", \"note\": \"KLN_1966.txt printed pp. 1109-1110 s.v. pact: 'fr. L. pactum … prop. neut. pp. of paciscor, pacisci, \\\"to covenant, make a treaty, agree, stipulate\\\", rel. to pax, gen. pacis, \\\"peace\\\", fr. I.-E. base *pak-, *pāg- … whence also L. pangere, \\\"to join, make firm\\\", pagus, \\\"district, province, village\\\", pagina …, palus (for *pak-slos), \\\"post, stake\\\"'. Klein spells the verb pacisci — the book's 'pacîcî' is a misprint.\"},\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. pag-: '2. Nasalized form *pa-n-g- in … b. Latin pangere, to fasten: COMPACT, IMPINGE. 3. Root form *pak- in: a. Latin pāx, peace …; b. Latin pacisci, to agree: PACT. 4. Suffixed form *pak-slo- in: a. Latin pālus, stake … 5. Lengthened-grade form *pāg- in: a. Latin pāgus … c. Latin prōpāgēs …: PROPAGATE.' Every Latin word of the node, with 'to agree' as the gloss of pacisci — Nourai's gloss.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW 787-788\", \"stance\": \"supports\", \"note\": \"'Latin pacīscō (sek. -or) \\\"einen Vertrag oder Vergleich festmachen\\\" … pāx, -cis f. \\\"peace\\\" … pālus \\\"picket, pole\\\" (from *pak-slos, compare Demin. paxillus); pangō … \\\"befestigen, einschlagen; aneinanderfügen\\\" … pāgus \\\"rural community, village\\\" … propāgō, propāgēs \\\"Setzlinge\\\", propāgāre'.\"},\n      {\"src\": \"LEW\", \"where\": \"Walde, Lateinisches etym. Wörterbuch\", \"stance\": \"silent\", \"note\": \"LEW_1910.txt is on disk but grep for 'pacisci' / 'pango' returned no usable headword lines from this OCR (the 1910 scan's headwords are badly broken); nothing extra obtained beyond Pokorny's WH. II 232 f./235 f./245 f. cross-references.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann s.v. pāg- (1) and paktos\", \"stance\": \"supports\", \"note\": \"'OLat. pago, ēre, (Lat. pango, ere) \\\"fix\\\"; pāgus, gs: -ī, m. \\\"landmark\\\" … pāgēs and com-pāgēs, f. \\\"join, setting, juncture\\\"' and 'paktos \\\"fixed, firm; stipulation, pact\\\". Cf. pak- … Lat. pactus'.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"English\",\n     \"words\": \"pact, compact; peace, pace, Pacific, pacify; pole, palette; peasant; propagate\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Each group answers to its Latin parent in node #2. pact < L pactum, neuter past participle of pacīscī; compact (n./adj.) < L compactum / compāctus from compingere (com- + pangere). peace < ME pais < OF pais < L pācem, acc. of pāx; Pacific < L pācificus (pāx + facere); pacify < OF pacifier < L pācificāre. 'pace' here must be the preposition pace 'with the leave of' (Latin pāce, ablative of pāx, learned use from the 1860s) — the ordinary noun pace 'step' is unrelated, from L passus (pandere, *peth₂-), so the chart's list is only correct on the first reading. pole 'stake' < OE pāl < L pālus (an early Latin loan into West Germanic, alongside OHG pfāl); palette < F palette, diminutive of L pāla 'spade', which Klein calls 'of uncertain origin … perh. rel. to L. pālus' while Watkins puts it under *pak-slo- outright. peasant < ME paissaunt < OF paisant, from pais 'country' < LL pāgēnsis 'of a district' < pāgus. propagate < L prōpāgātus, pp. of prōpāgāre, from prōpāgēs. All confirmed by Klein and by Watkins's word list for pag-.\",\n     \"derivation_fa\": \"هر دستهٔ واژگانی به نیای لاتین خود در گرهٔ پیشین پاسخ می‌دهد: pact از pactum (اسم مفعول pacīscī) و compact از compingere؛ peace از pais فرانسهٔ کهن از pācem (رایی pāx)، Pacific از pācificus و pacify از pācificāre. اما «pace» در این فهرست تنها به معنی حرف اضافهٔ «pace» («با اجازهٔ…») درست است که از حالت ازی pāce می‌آید؛ «pace» به معنی «گام» از passus (از pandere) و بی‌ارتباط است. «pole» به معنی «تیر، میخ» از انگلیسی کهن pāl و آن وام‌واژه‌ای کهن از لاتین pālus در ژرمنی باختری است؛ «palette» از فرانسهٔ palette، مصغّر pāla «بیل» که کلاین آن را «شاید هم‌ریشهٔ pālus» می‌داند و واتکینز بی‌درنگ ذیل ‎*pak-slo-‎ می‌گذارد. «peasant» از paisant فرانسهٔ کهن از pais «سرزمین» از pāgēnsis لاتین متأخر و آن از pāgus. «propagate» از prōpāgāre از prōpāgēs. ادعای نورایی در این گره درست است.\",\n     \"sources\": [E_PAG, W_PAG],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. pag-: 'PACT', 'COMPACT', 'PACE², PAY¹, PEACE; APPEASE, PACIFIC, PACIFY', 'PALE¹, PALISADE, PEEL, POLE²', 'PALETTE, PEEL', 'PAGAN, PEASANT', 'PROPAGATE'. Note that AHD's PACE under pag- is PACE² 'with the leave of'; PACE¹ 'step' is indexed to petə-.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.vv. pact, compact, peace, pace, pagan, peasant, palette, propagate\", \"stance\": \"supports\", \"note\": \"'peace … fr. L. pācem, acc. of pāx … cp. esp. appease, pace, \\\"with the leave of\\\", pacify, pax'; 'pace, n., with the leave of … L. pace, abl. of pax'; 'peasant … fr. OF. paisant … fr. Late L. pāgēnsis … fr. L. pāgus; see pagan'; 'palette … diminutive formed fr. L. pala, \\\"spade, shovel\\\" … perh. rel. to L. palus, \\\"stake\\\"'; 'propagate … fr. prōpāgēs … fr. pro- and *pag-, base of pangere'.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict.\", \"stance\": \"silent\", \"note\": \"grep of SKT.txt for '^PACT', '^PEASANT', '^PROPAGATE' returned no headword lines in this OCR; no independent evidence added.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith open(\"data/verification/page-380.json\",\"w\",encoding=\"utf-8\") as f:\n    json.dump(doc,f,ensure_ascii=False,indent=1)\nprint(\"written\")\nPYEOF\npython3 -m json.tool data/verification/page-380.json > /dev/null && echo \"JSON OK\"\npython3 tools/verify_check.py 380"
}
```


### [2026-09-07T20:49:38.252Z] TOOL RESULT

```
written
JSON OK
nodes verified: 11/11
node verdicts: {'plausible': 5, 'confirmed': 5, 'transcription_suspect': 1}
root verdicts: {'plausible': 1, 'confirmed': 1}
ref checks: {'supports': 13, 'partial': 3, 'not_checked': 4, 'not_found': 1}
books consulted: {'silent': 8, 'supports': 15, 'partial': 6} | by book: {'KLN': 7, 'POK': 4, 'IEC': 4, 'SKT': 3, 'PHD': 1, 'NYB': 1, 'HRN': 1, 'HUB': 1, 'ARY': 1, 'BQT': 1, 'SYN': 1, 'WEB': 1, 'BRT': 1, 'KNT': 1, 'LEW': 1}
```


## [2026-09-07T20:49:44.761Z] TOOL CALL #58: Bash

```json
{
 "command": "python3 tools/verify_archive_sources.py 2>&1 | grep -i \"380\\|MISSING\\|OK\" | head -20"
}
```


### [2026-09-07T20:49:48.355Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T20:49:51.402Z] TOOL CALL #59: Bash

```json
{
 "command": "python3 tools/verify_archive_sources.py 2>&1 | tail -20"
}
```


### [2026-09-07T20:49:53.778Z] TOOL RESULT

```
3532 cited URLs, 9 not yet archived
archived 9, failed 0
```


## [2026-09-07T20:50:14.220Z] AGENT

Done. `/home/sfmqrb/git/rishe/data/verification/page-380.json` written; `verify_check.py 380` reports **11/11 nodes, 0 PROBLEM lines**.

**Counts (pdf 380 / book 350)** — roots: 1 confirmed (Pak, Pag), 1 plausible (Pa, Pa-ter, Poti, Potiš). Nodes: 5 confirmed, 5 plausible, 1 transcription_suspect. Ref checks: 13 supports, 3 partial, 1 not_found, 4 not_checked (KAS, AEF, DVS ×2 — no accessible copies).

**transcription_suspect**
- *Pak, Pag* → Latin node #2, "pacîcî : to agree" — impossible Latin form; the printed page (checked at 300→200 dpi, copied to `data/verification/sources/refs/ocr/BOOK/380.png`) really prints `pacîcî`, so `error_in: "book"`; correct form `pacīscī` (Klein p.1110, Pokorny 787, AHD all spell it *pacisci*). Extraction is faithful — **no data fix needed**.

**No extraction errors found.** JSON matches the printed page throughout (incl. the Ferdowsī couplet and «بابا، بابو، بابک، بابکان»).

**Notable findings (drove the `plausible` verdicts)**
- The root box lumps three separate standard lemmas: *peh₂- (POK 787, confirmed), *ph₂tḗr (POK 829), *pótis (POK 842). Wiktionary reports Nourai's Pa+ter analysis as the usual-but-contested view; *pótis is nowhere derived from *peh₂-. His "also self" is well grounded (Av. xᵛaē-pati-, Lith. pats, Hitt. -pat).
- `POK:847` on the Latin node is a wrong page — IEW 847 has *ptel(e)ia* "elm" and *pū-/peu-* "to blow"; wanted 787/829/842.
- `BQT:202` is one page late: the باب/بابک entries with Mo'in's footnote «باب (پدر) + ک (پسوند دال بر عزت و محبت)» begin on printed p. 201 (footnotes run onto 202). Otherwise it is verbatim Nourai's node text, and confirms his NOTE that BQT asserts Latin *papa* cognacy without argument.
- `HRN:34` (no. 147 bāb "Vater" … phlv. papak) and `NYB:150` (Pāpak … "NP bab, baba") both support exactly; MacKenzie has only *pid* "father", no pāp(ak) common noun.
- Misfiled words: **pattern** under Germanic (it is Latin *pater* → *patrōnus* → OF *patron*), **papa** under Greek (it is French *papa* < Latin *pāpa*), and **pappas/Pope** belong to Pokorny's separate nursery lemma *pap(p)a* 789, not *peh₂-*. Also **pace** in the Pak chart is only correct as the preposition (< abl. *pāce*), not "step" (< *passus*).
