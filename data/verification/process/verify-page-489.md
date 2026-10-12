# Verification process log — verify-page-489


## [2026-09-14T03:08:34.939Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 489 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-489.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-489.json. Write /home/sfmqrb/git/rishe/data/verification/page-489.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 489` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T03:08:35.922Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T03:08:36.662Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T03:08:36.759Z] TOOL RESULT

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


## [2026-09-14T03:08:37.197Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-489.txt"
}
```


### [2026-09-14T03:08:37.222Z] TOOL RESULT

```
1	=== PDF page 489 (book page 459) ===
2	--- entry 0 ---
3	ROOT Sŭtus -> redirect to Seu 3
4	--- entry 1 ---
5	ROOT [Indo-European] Svas : thresh, beat grain  (refs SYN:510)
6	#1 (parent #0) [Avestan] refs=SYN:510 | xvasta : threshed ; a-xvasta : unthreshed ☞Ne 1
7	  #2 (parent #1) [Persian] refs=SYN:510; MON:1455 | xost «خوست ( خست )» : pressed, squeezed, mashed | extra: آبخوست ، پای خوست ، چنگال خوست
8	--- entry 2 ---
9	ROOT [Indo-European] Swâd : sweet  (refs POK:1039)
10	#1 (parent #0) [Avestan] refs=POK:1040; FFD:51 | xwâs, xwâd : to desire ; xvâsto : sweetened by cooking ; xvand : sweet taste ; xvandra-kara : pleasing ☞Kwer
11	  #2 (parent #1) [Pahlavi] refs=HRN:110; BQT:783 | xvâstan : to desire, want
12	    #3 (parent #2) [Persian] refs=BQT:783 | xâstan «خواستن» : to want | extra: خواست، خواستار، خواهش، خواه
13	#4 (parent #0) [Sanskrit] refs=POK:1039; KLN:1552 | svad : sweet, desirable ; svâdati : to desire, want
14	#5 (parent #0) [Germanic] refs=AHD; KLN:1552 | swôtja : sweet
15	  #6 (parent #5) [English] refs=None | sweet
16	#7 (parent #0) [Latin] refs=AHD | suâdĕre : to advise as good (sweet) option ; per-suâdere : to advise intensively, persuade
17	  #8 (parent #7) [English] refs=None | persuade
18	--- entry 3 ---
19	ROOT [Indo-European] Swei; Sweib : to bend, twist; move swiftly like a snake  (refs POK:1041)
20	#1 (parent #0) [Avestan] refs=POK:1041 | xšvira : swift ; xšvaewa : swift
21	  #2 (parent #1) [Pahlavi] refs=BQT:1319,1329 | šĕpâk : fast, easy to understand
22	    #3 (parent #2) [Persian] refs=BQT:1319,1329; HRN:178,179; MON:2115 | šîbâ «شیبا» : a large snake ; šîvâ «شیوا» : easy to understand, clear
23	#4 (parent #0) [Germanic] refs=AHD | swîp : sweep ; swîf : fast move
24	  #5 (parent #4) [English] refs=None | sweep ; swift, swap, sway, swivel
25	--- entry 4 ---
26	ROOT Sweib -> redirect to Swei
27	
```


## [2026-09-14T03:08:40.043Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-489.json",
 "description": "Read source JSON for page 489"
}
```


### [2026-09-14T03:08:40.084Z] TOOL RESULT

```
{
  "pdf_page": 489,
  "book_page": 459,
  "entries": [
    {
      "root": {"name": "Sŭtus", "redirect": "Seu 3"},
      "nodes": []
    },
    {
      "root": {
        "name": "Svas",
        "lang": "Indo-European",
        "refs": "SYN:510",
        "gloss": "thresh, beat grain"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "SYN:510",
          "words": [
            {"translit": "xvasta", "gloss": "threshed", "script": null},
            {"translit": "a-xvasta", "gloss": "unthreshed", "script": null, "see": ["Ne 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "SYN:510; MON:1455",
          "words": [
            {"translit": "xost", "gloss": "pressed, squeezed, mashed", "script": "خوست ( خست )"}
          ],
          "script_extra": "آبخوست ، پای خوست ، چنگال خوست",
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Swâd",
        "lang": "Indo-European",
        "refs": "POK:1039",
        "gloss": "sweet"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:1040; FFD:51",
          "words": [
            {"translit": "xwâs, xwâd", "gloss": "to desire", "script": null},
            {"translit": "xvâsto", "gloss": "sweetened by cooking", "script": null},
            {"translit": "xvand", "gloss": "sweet taste", "script": null},
            {"translit": "xvandra-kara", "gloss": "pleasing", "script": null, "see": ["Kwer"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "HRN:110; BQT:783",
          "words": [
            {"translit": "xvâstan", "gloss": "to desire, want", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:783",
          "words": [
            {"translit": "xâstan", "gloss": "to want", "script": "خواستن"}
          ],
          "script_extra": "خواست، خواستار، خواهش، خواه",
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:1039; KLN:1552",
          "words": [
            {"translit": "svad", "gloss": "sweet, desirable", "script": null},
            {"translit": "svâdati", "gloss": "to desire, want", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD; KLN:1552",
          "words": [
            {"translit": "swôtja", "gloss": "sweet", "script": null}
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
            {"translit": "sweet", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "suâdĕre", "gloss": "to advise as good (sweet) option", "script": null},
            {"translit": "per-suâdere", "gloss": "to advise intensively, persuade", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "persuade", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Swei; Sweib",
        "lang": "Indo-European",
        "refs": "POK:1041",
        "gloss": "to bend, twist; move swiftly like a snake"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:1041",
          "words": [
            {"translit": "xšvira", "gloss": "swift", "script": null},
            {"translit": "xšvaewa", "gloss": "swift", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:1319,1329",
          "words": [
            {"translit": "šĕpâk", "gloss": "fast, easy to understand", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:1319,1329; HRN:178,179; MON:2115",
          "words": [
            {"translit": "šîbâ", "gloss": "a large snake", "script": "شیبا"},
            {"translit": "šîvâ", "gloss": "easy to understand, clear", "script": "شیوا"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "swîp", "gloss": "sweep", "script": null},
            {"translit": "swîf", "gloss": "fast move", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "sweep", "gloss": null, "script": null},
            {"translit": "swift, swap, sway, swivel", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Sweib", "redirect": "Swei"},
      "nodes": []
    }
  ]
}
```


## [2026-09-14T03:08:40.815Z] TOOL CALL #4: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T03:08:40.865Z] TOOL RESULT

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
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt` (truncated before the lexicon's h–z section, ~p. 208 on)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT_full.txt` (complete archive.org djvu text — use this for lexicon pages 208–215: haumavarga-, siyamam, etc.)
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


## [2026-09-14T03:09:01.734Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n 1,80p tools/verify_check.py; echo ---; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['SYN','POK','MON','BQT','HRN','AHD','KLN','FFD']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600])\n\"",
 "description": "Inspect verify_check and refs metadata"
}
```


### [2026-09-14T03:09:02.898Z] TOOL RESULT

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
---
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s
```


## [2026-09-14T03:09:06.902Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['SYN','POK','MON','BQT','HRN','KLN','FFD','BRT','PHD']:\n    e=d.get(k,{})\n    print('==',k, '| offset:', e.get('page_offset'), '| local:', e.get('local_file'), '| hint:', str(e.get('lookup_hint'))[:300])\n\"",
 "description": "Print page offsets"
}
```


### [2026-09-14T03:09:08.102Z] TOOL RESULT

```
== SYN | offset: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt | hint: Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
== POK | offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt | hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' giv
== MON | offset: None | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] | hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe
== BQT | offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] | hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d
== HRN | offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt | hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
== KLN | offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt | hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
== FFD | offset: 115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X). | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages_faseng.txt'] | hint: Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).
== BRT | offset: Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt | hint: Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
== PHD | offset: leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt | hint: Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).
```


## [2026-09-14T03:09:13.328Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"lemma: su̯ād\\|lemma: su̯ad\\|lemma: su̯eib\\|lemma: su̯ei\\b\" POK_full.txt | head -20\necho \"=== search alt\"\ngrep -n \"^Root / lemma: su\" POK_full.txt | sed -n 1,80p"
}
```


### [2026-09-14T03:09:13.429Z] TOOL RESULT

```
=== search alt
83246:Root / lemma: su-, su- 
83275:Root / lemma: suard- 
83287:Root / lemma: suad- 
83346:Root / lemma: suad- : sweet 
83367:Root / lemma: sueid-1 
83386:Root / lemma: sueid-2 
83424:Root / lemma: suei-, sui- {*g"hei- : ksuel) 
83468:Root / lemma: suekru- {*RueRur-a) 
83511:Root / lemma: suek- 
83724:Root / lemma: suel-l(k-) 
83754:Root / lemma: suel-2 
83833:Root / lemma: suel-4 
83839:Root / lemma: sue-lo- suellio(n)- 
83878:Root / lemma: suelplo-s 
83894:Root / lemma: suem- 
83939:Root / lemma: sueng-, suenk- : sueg-, suek- {*g"heng- : ksueng-) 
83982:Root / lemma: suenk-, sunk- 
83996:Root / lemma: suento- sunto- 
84010:Root / lemma: suen- 
84037:Root / lemma: suep-1, sup- {* kuep-1) 
84086:Root / lemma: suep-2, sup-, sueb- 
84141:Root / lemma: suergh- {*g"hergh- : ksuergh-) 
84162:Root / lemma: suer-1 (also ser-?) 
84188:Root / lemma: suer-2 
84233:Root / lemma: suer-3 
84255:Root / lemma: suer-4 
84282:Root / lemma: suer-5 
84337:Root / lemma: sueid- {* ksue/d- < g'^heid-) 
84355:Root / lemma: sue(i)- 
84432:Root / lemma: suT-, -g-, -k-, -p- 
84463:Root / lemma: suomb(h)o-s 
84484:Root / lemma: suordo-s 
84507:Root / lemma: su-ro-, sou-ro- 
84546:Root / lemma: su-s, suu-6s 
84596:Root / lemma: sus- 
84604:Root / lemma: sus- : to buzz, derived from Root / lemma: Rues-, Rus- : to puff, sigh. 
84620:Root / lemma: sus- {*ksus)
```


## [2026-09-14T03:09:14.705Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR>=530 && NR<=540' SYN.txt | grep -n \"THRESH\" | head\necho \"=== find THRESH heading\"\ngrep -n \"THRESH\" SYN.txt | head -20"
}
```


### [2026-09-14T03:09:15.752Z] TOOL RESULT

```
=== find THRESH heading
12819:AGRICULTURE, VEGETATION 509 8.34 THRESH , Lith. kulti Goth. Ariskan 1. pipe skja Lett. Kult ; anol? HP On eae, ChSl.  mlatiti, vrésti cist : Sw. ”  réska SCr.  mlatiti, vrijeci paler fribbiare OE jperscan Boh. mlatiti pallre ME _ thresche Pol. mlécié jrillar NE thresh (thrash) Russ. ‘molotit! — :  treera Du. dorschen Skt. _mr-, prati-han- * dofuairce (3 se) OHG drescan Av.  aasta- ‘threshed’ puailim MHG dreschen dyr ial NHG dreschen dourn
12838:8.35 THRESHING-FLOOR
```


## [2026-09-14T03:09:21.176Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '12815,12845p' SYN.txt"
}
```


### [2026-09-14T03:09:21.228Z] TOOL RESULT

```
(rier) Sp. trillar, Rum. treera
ifr. Lat. tribulare ‘ ee: press, oppress’, aa tribulum ‘threshing-sled’ (in (above) a harrow), fr. root of terere Teta Pee, 1088. REW 8885 : Te, . b 7 ¢ , at. battuere ‘beat? aon bao
3, I rutey” do-fuairee (Wh, 10d6) lit. destig . S a to- fo- and org- ‘strike, Teysen, Gear. a3 2.250, 590. Thur-
igitized by Arya Samaj Foundation Chennai and eGangotri
AGRICULTURE, VEGETATION 509 8.34 THRESH , Lith. kulti Goth. Ariskan 1. pipe skja Lett. Kult ; anol? HP On eae, ChSl.  mlatiti, vrésti cist : Sw. ”  réska SCr.  mlatiti, vrijeci paler fribbiare OE jperscan Boh. mlatiti pallre ME _ thresche Pol. mlécié jrillar NE thresh (thrash) Russ. ‘molotit! — :  treera Du. dorschen Skt. _mr-, prati-han- * dofuairce (3 se) OHG drescan Av.  aasta- ‘threshed’ puailim MHG dreschen dyr ial NHG dreschen dourn
NIv. buailim ‘strike, beat’ (9.21) and ‘thresh’.
W. dyrnu, Br. dourna, orig. ‘beat with the hand’, fr. W. dwrn ‘fist’, Br. dourn ‘hand’ (4.33).
4. Goth. priskan, OF perscan, OHG drescan, etc., general Gmce. (in lit. NE tendency to differentiate thresh in old sense from thrash in secondary, but latter also the usual form among farmers), perh. : Lith. treskéts ‘crack, rattle’, ChSl. tréskt ‘crash’; or/and fr. the root *ter- in Lat. terere ‘rub’ (cf. above, 2), etc. Walde-P. 1.730. Falk-Torp 1255. Feist 503. NED s.v. thrash.
5. Lith. kulti, Lett. kult, lit. ‘strike, beat’ : Lith. kalti, Lett. kalt ‘strike, ham- mer, forge’, ChSl. kolja, klati, ‘stick, slaughter’, Lat. percellere ‘strike down’, etc. Walde-P. 1.486 ff. Walde-H. 1.226.
6. Chl. mlatitz, etc., general Slavic : mlatt ‘hammer’, mléti ‘grind’, Lith. maltit, Lat. molere ‘grind’, etc. (5.56). Walde-P. 2.284 ff. Berneker 2.73.
Late ChSl. vréSsti, vrticha, SCr. vrijecz (cf. also ChSl. vrachi ‘threshing’, Russ. voroch ‘heap of grain’), prob. as orig. ap- plied to threshing by dragging : Lat. verrere ‘sweep’, etc. Walde-P. 1.292. Miklosich 383.
7. Skt. mr- ‘crush’ (: Lat. molere ‘grind’, etc., 5.56) is the technical ex- pression for ‘thresh’ in Cat. Br. 1.6.1.3,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
510
and ‘reap’. Macdonell-Keith 1.182.
Skt. pratihan-, epd. of han- ‘strike’, occurs in RV 10.48.7 with play on
‘thresh’ and ‘thrash’.
Ay. x*asta- ‘threshed’, ax'asta- ‘un-
Digitized by Arya Samaj Foundation Chennai and eGangotri
SELECTED INDO-EUROPEAN SYNONYMS
following the words for ‘plow’, ‘sow’,
threshed’ (cf. NPers. pai-xvastg ‘trodden by foot’), fr. xah- ‘press’, Otherwise Barth. 874 f. (“Et.?”), Suppl. 246 (fr root ending in dental), but the deriy, fe:
x*ah- (Aryan *svas-) seems Perfect ip form and sense.
8.35 THRESHING-FLOOR
Giee otis Goth. gaprask Lith. klojimas, kluonas, NG adn ON lafi (lofi) klaimas Lat pe Dan. lo Lett. piedarbs, kluons
It. ara Sw. loge ChSl. gumtno Fr. aire OE pirsceflor SCr. gumno
Sp. era ME thresschinge floore Boh.  mlat
Rum. arie NE threshing-floor Pol. klepisko Ir. tthland Du. _—_dorschvloer Russ. gumno, tok Nir. —_urlar an bhuailte OHG  tenni Skt. khala-
W. Ulawr dyrnu MHG tenne Av. shiek
Br. leur NHG tenne
Words for ‘threshing-floor’ are in part derived from verbs for ‘thresh’ (mostly in combination with ‘floor’). Most of them are from the notions of ‘open space’, ‘floor’, ‘flat surface’, with special- ization.
```


## [2026-09-14T03:09:22.025Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '83346,83370p' POK_full.txt; echo \"=== 83287\"; sed -n '83287,83346p' POK_full.txt"
}
```


### [2026-09-14T03:09:22.105Z] TOOL RESULT

```
Root / lemma: suad- : sweet 
Root / lemma: ad(u)-, ad-ro- 
English meaning: water current 

Root/ lemma: alca- {more properly alcS). ek"- 

English meaning: water, river 

Root / lemma: from- 

English meaning: to draw (water), ladle 

Root / lemma: au(e)-9, aued-, auer- 

English meaning: to flow, to wet; water, etc.. 



References: WP. II 516 f., WH. II 611 f.. Frisk 104, 166, 184f. 
Page(s): 1039-1040 

Root / lemma: sueid-1 

Meaning: to shine 

=== 83287
Root / lemma: suad- 

Meaning: sweet 

Material: 1. suadu-s'sweei': Old Indie svadii-, f. si/ao'i/f "sweet, mellifluous'; gr. n5u(;, f. -sTa 

(*-£Fia), -u, Dorie dbdc, "sweet'; with formants -mo-. aSupoc;, hom. r|5u|J0(; "pleasant'; Latin 

suavis {*suadu/s) "sweet'; Old Saxon swot/. Old High German suoz/. Old English swete. 

Old leelandie Sj^/a" sweet'; gall. PN SuadurTx, -genus, Irish Sadbt PN; about Gothie sut/'s' 

peaeeful, gentle', s. Mayrhofer KZ 71 , 74 f. under 73, 116 f. 

Kompar. Superl. Old Indie svadTyas-, gr. nSiwv; Old Indie svadistha-= gr. riSiarog; 



2. suados-n. Sijftigkeit, satisfaction ': ved. pra-svadas-^ mellifluous, pleasant', p£Air|5r|(; 
' mellifluent ', nSoc; n. " vinegar ' (gr. n5o(; n. 'benefit, advantage', absents). 

3. suadonom, -a. Old Indie svadanam, gr. n5ovn f. 'lust'. 

4. verbs and other nominal formation: 

Old Indie ved. svadate"\s pleased, enjoys' = gr. fi5o|jai (Boeotian Fa5o|jr|) 'freue 
myself; 

Avestan x'asto' through eook gar (sehmaekhaft) gemaeht, eooked, boiled' = Old Indie 
5i/a//5-'gewurzt'; Old Indie svada- m. 'taste, Wohlgesehmaek', Baluehi vad^saW! 
(Mittelbegriff 'Wurze'); 

eausative respeetively intensive svadayati {= Latin suadeo, see below) and svadayati 
'sehmaekhaft, annehmbar make; taste, eat, drink; relish, enjoy ', zero grade sudayati 
'belonging einriehten, good make, fertigmaehen = slay, destroy' (with the same ablaut 
grade Perf. susudima; suda- m. ' eook ', Lithuanian sudyti, Gothie sutis); 

with analog, a. svadat/'makes sehmaekhaft, wijrzt', svadate ' schmeckt' , participle 
svatta-, nasalized Avestan x'andra-kara-^avM^euehmes making = eompliant', afgh. x'and 
'Wohlgesehmaek, pleasure' (compare gr. avSavw); 

Gr. nSopai (see above); aa\\zyoc, ' pleases ', not certainly here as participle to s-Aorist 
riaoTO (the Lenis unexplained); *aFc(5£U), *ar|5£U) (hom. ar|5na£i£, a5r|K6T£(;) 'bin 
querulous ', lokr. F£Fa5r|K6Ta (a or 5?); av5avu) 'gefalle', Aor. hom. £ua5£, gortyn. £Fa5£, 
Perf. £a5a (: Old Indie sasvade), acpavSavw 'miftfalle' (acpaSia 'enmity'), Ionian aboc, m. 
'decision', a5r||Ja Hes. ds., au9a5r|<;, Ionian auTU)5r|c; 'hubristie, overbearing, selbstgefallig' 
(*auToFa5r|<;). C(Fa5n(; ' querulous ', whereof aa5£Tv 6xA£Tv, anop£Tv Photios; this -es-stem 
cxboc, is previously gr. neologism from av5avu) from; 

Latin suadeo, -ere^rate' (i.e. 'mache einem etwas gefallen'); 

Lithuanian sudyti^ spice, salzen'; 

perhaps here Old English swatanP\. 'beer', Scots Gaelic sn/a/s 'fresh gebrautes beer'. 

Maybe alb. {*huad-) anda 'appetite, desire, wish' related also to Hittite anza 'desire'??? 



Root / lemma: suad- : sweet
```


## [2026-09-14T03:09:47.761Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Page(s): 104[012]\" POK_full.txt | head -20"
}
```


### [2026-09-14T03:09:47.814Z] TOOL RESULT

```
83466:Page(s): 1040-1041 
84430:Page(s): 1041-1042
```


## [2026-09-14T03:09:48.884Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"sueib\\|su̯eib\\|sueip\" POK_full.txt | head -20; echo ===; sed -n '84355,84440p' POK_full.txt"
}
```


### [2026-09-14T03:09:48.945Z] TOOL RESULT

```
Exit code 1
84114:"quick, fast (drehend)' from *sueib^-nio-; Gothic af-, bi-swafrban "abwischen'. Old Icelandic 
(eval):2: == not found
```


## [2026-09-14T03:09:50.753Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '84355,84435p' POK_full.txt"
}
```


### [2026-09-14T03:09:50.808Z] TOOL RESULT

```
Root / lemma: sue(i)- 

Meaning: to bend, turn, swing 

Note: (see also se^-and sueng-^bex\6') 

Material: Gr. oTpoc; "aufwarts bent, curved, stumpfnasig, spottisch' (in addition gikxoc; 

"disgust, all tadeind'?); perhaps also ox^oc, "pit, pothole' (*incurvation?); 

cymr. c/7w/o'"lebhafte turn, Kunstgriff', chwidrs\dr\ in Kreise drehend, dizzy ', chwidr 
"quick, fast, fleeting, iJbereilt'; chwimm. {*suT-smo-) "movement, actuation ', Adj. "quick, 
fast', chwyfxw. 'movement' {*suhmo-, compare under Germanic swfm-), chwyf/o ' movere' , 
bret. f/nva/, gmnva/'s\c\r\ bewegen, ruhren'; 

cymr. c/7byK/7 "movement', chwil {*suT-lo-) "sich quick, fast drehend'; chwylav\6 chwel 
{*suhlo-, -/a compare Norwegian svil) " turn, run, flow', corn, whey/^work', Old Irish se/" 
turn, gyration, stretch of time'. Middle Irish of-ser turn after right', tuath-biT turn after 
links'; 

Middle Low German swaien, swe/men's'\c\r\ schwingen'; as participle Old Icelandic svad 
n. " glide, smooth flowing movement, slipping, skidding ', {*su9-to-), 5i/5d5 "glide, slide'. 
Old English 5M/ad/a/7"(ein)wickeln', engl. swath(e). Middle Low German Middle High 
German swade^Reihe from gemahtem Gras, Schwaden\ 



Norwegian si//777a "waver, lurch', Middle High German smmen ds.; Old English swrmam. 
" dizziness, giddiness; swindle, Ohnmacht', Old Icelandic sv/m/, Dutch zw//m6s.; Middle 
High German swTmel, swimmer dizziness, giddiness; swindle '; Old Icelandic sve/mrm., 
sve/mn. 'GetiJmmel, tumult', si/e//775'umherziehen'. Middle High German swe/mm. 'das 
Schweben, Schweifen, Schwingen', SM/e//77e/7'sichschwingen, waver'; Norwegian si///n. 
"Spirale; the frizzy Samenbeutel dorschartigerfish'; Low German sty/?'Schwung, gyration, 
Bummein', sw/ren^s\c\r\ schwingend bewegen, umherfliegen, in Saus and Braus leben'. 

sue/b-: Avestan xsvaewayat-astra-^ 6\e Peitsche schwingend', A-siz/Vwa- "agile'; Gothic 
midJa-sweipains^S\v\\^\\}\! (actually "Fegung the center'); Old Icelandic si/e/p5 "throw, 
umhijllen'. Old English 5M/apa/7 "swing, sweep, wash away, drive, push'. Old Saxon swep 
"fegte fort'. Old High German SM/e/>^/7 "swing, schweifen, quarrel', SM/e//"Umschwung, tail' 
= Old Icelandic si/e'/p/'"band, strap, Schlingung, curled hair'. Old Icelandic si//pa"lash, 
scourge, bullwhip, horsewhip; spur'. 

sue/c/-:\n Lithuanian svfesti, Latvian si//es/ "throw', frequentative Lithuanian svaidyti, 
Latvian si/a/(y/7"wiederholt toss, fling'; whether Latvian si/a/Ty/? "anoint, smear' (under under 
sueid-) here? 

sueig-: QermaxWc also "nachgeben, slacken ' (from suh " dwindle ' derive ) "(cunning) 
etwas drehen, dodge, deception ' : Old High German swThhon, Old English swTcian 
"schweifen, wander, cheat, deceive'. Old Icelandic svTkva sykva {u-'^resev\{), si//7^a "cheat, 
deceive, betray ', Old English swTcan^ abandon, cheat, deceive', poet. " leave, depart, 
wander'. Old Saxon swTan6s. "languish'; Old High German sbv/77/75/7 "languish, slacken, 
abandon ', Middle High German swTchm. "Zeitlauf, 5-5ty/C'/7"heimlicher Fortgang', 
SM/e/ic/7e/7 "languish'; Old Icelandic sviku. " betrayal, deceit'. Old English swicu. ds.. Old 
High German biswihrw. ds.; 

Lithuanian svaTgtr dizziness, giddiness; swindle bekommen', svaigineti^ giddy 
umherwanken', russ. 5i//g5/'"herumtreiben'; 

Tocharian A M/5M/e/r£/"gelogen', B waike^\\Q, falsity'. 

sueik-:Q\^ Icelandic si/e/^/'"pliable', m. "flexible stalk', Swedish dial. svTga, sveg 
"sichbiegen', Kaus. Old Icelandic si/e/5y5"bend'. Pass, sv/gna^be bent, bow, nachgeben', 
sv/'g/m. "flexible stalk'; Old High German swe/ga^catt\e shed' (*netting). 

sue/p-:0\6 Icelandic si//7^ "swing, turn, umherschweifen, schweben'. Old English swTfan 
"turn, sweep, wash away (engl. SM///?"quick, fast'), wave'. Old Icelandic sue/f/a ^swng', 



Middle High German swibein, swivelen'\wdc\\ Old High German sweibon^sdcwNebeu, 
swing', 5i4/eM/7'schweben'. 

Latvian svaipTV lash, flog ', si///7s//>^y's'Hasenfufl, Zierbengel'. 

References: WP. II 518 ff., Vasmer2, 591 f., Johannesson 794 ff. 
Page(s): 1041-1042 

Root / lemma: suT-, -g-, -k-, -p- 

Meaning: to fade, weaken, etc..
```


## [2026-09-14T03:10:12.052Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### BRT xvah / xvasta\"; grep -n \"x\\\"ah\\|x'ah-\\|xvah-\\|hvah\" BRT.txt | head -20\necho \"### BRT threshed/dreschen\"; grep -n -i \"dreschen\" BRT.txt | head -20\necho \"### BRT xšviwra / agile\"; grep -n \"xsviwra\\|x§viwra\\|xsvaewa\\|xšviwra\\|xšvaēwa\\|xsvaevva\\|xsvibra\" BRT.txt | head -20"
}
```


### [2026-09-14T03:10:12.133Z] TOOL RESULT

```
### BRT xvah / xvasta
3406:•  j.  aS'ä-  f.,  Plur.  'Grund  und  Boden, HoP:  yö  nSit  nar>m  alavamm  hvahva ''iä&va  JasSntfm  xsnaoita  va  xsnävayeite vä  "wer  einen  Gläubigen,  der  auf  seinen Hof  kommt,  nicht  bewirtet  oder  bewirten lässt"  V.4g-
4189:•  j.  aohvah- : awÄ»j^  Adj.,  PPfA.:  s.^aA-,
6964:•  j.  ahvah-:  rtw,5»j- Adj.,  PPfA, :  s.  'ah- mit  No.  2.
7201:•  j.  ahvah-:  rtw^w/- Adj.,  PPfA. :  s.  ^ah- mit  No.  3.
7592:•  j.  ahvah-  :  ai>hus-  Adj.,  PPfA.:  s.  '^ah-. Vgl.  akvah'.
11123:•  j.  £axvah-'' :  cakul-  Adj.,  PPfA,:  s.  kl-. >)  Ansatz  des  Vollstamms  unsicher;  es  ist nur  caiust  bezeugt.
18869:•  j.  näfa-  m.  'Nabel' :  °/S¥.3  g.  a)  'Ver- wandtschaft, Familie':  Aaväi  kscit  '/ai''> havayäi  vise  Aaväi  zantave  Aavayäi  äaiA- Aave  "jede  für  ihre  Familie  . ."  Yt  13.66; —  *yavata  Ai  °/e  *x"ahwan/tä  (sd.)  N,  I7.
22192:•  j.  vaoxvah- '' :  i'aöi«/-  Adj.,  PPfA.: s.  'vak:
### BRT threshed/dreschen
### BRT xšviwra / agile
10945:•  j.  xsvaewa-  1)  Adj.  'sich  rasch  schwin- gend,   schnellend':    azayS  "wänhS    "sich
```


## [2026-09-14T03:10:15.004Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### PHD xwastan\"; grep -n \"^xwāst\\|^xwāh\\|^xwast\\|xwāstan\" PHD.txt PHD_mackenzie.txt | head -20\necho \"### PHD šēb\"; grep -n \"^šēb\\|^šēw\\|^šyb\" PHD.txt PHD_mackenzie.txt | head -20\necho \"### NYB\"; grep -n \"xvāstan\\|xvāst\\|xvāh-\" NYB_vol2_glossary.txt | head -20\necho \"### CHEUNG\"; grep -n -i \"xwāstan\\|xwāst \\|HuaH\\|hwad\" CHEUNG.txt | head -30"
}
```


### [2026-09-14T03:10:15.117Z] TOOL RESULT

```
### PHD xwastan
PHD.txt:663:xwāb [hw’b | N ~] sleep. xwābar [hw’l | M xwbr] beneficent. ~ig [-yk!] beneficial. —ih: beneficence, benefit. xwad [BNPSE < A b-nps-h; hwt' | M xwd, N ~] self; indeed. САҢ: selfhood, essence. xwaday [лору | M xwd'y, N ~] lord. ~th: lordship, sovereignty. ~war [-w’/] lordly. xwad-dósag [hwtdwsk'] self-indulgent. 7h : self-indulgence. xwah [AH TE < A *hth | N ~] sister. 1, ?x wüh-, ~išn, v. xwastan, xwāstan. xwahar [AH TEL v. xwah ; hw'hl | (M xwr), N xwdhar] sister. xwahl [eo hl | (M xwhr), № ~] bent, crooked. xwā(h)rīh [hw (h)yh | M xw'ryy] happiness, bliss. xwālist [hw’lyst' | (M xw’ryst)] sweetest. xwamn [hwmn', hmn' | M xwmn] sleep, dream. ~-wizar [-wc'/] interpreter of dreams, oneirocritic. xwān [hw!n! | M xw’n, N ~] tray, table. xwandan, xwān- [KRY TWN-, KLY TWN-tn! < А У д | M xwnd, xw'n-, N xwāndan) call, summon. Xwanirah [hwnyls = Av. x"aniraüa-] the central, inhabited continent of the earth. !xwar [kwl | M xwr, N ~] sun; cal. 11th day. Zwar [kwl = Av. x"ara-] a degree of sin. xwar-, —išn, v. xwardan. lxwàr [kw] | M xwr, N ~] light, easy; mean, abject. ~ih: ease; v. also x wührih. *xwar [%w/ | M xwr] food. xwür-, —išn, v. xwārīdan. xwaran [%w/n! | M xwrn] banquet. xwarāsān [hwlsn! | M xwr'?n, N ~] sunrise, east. xwār-bār [how?1b?l | M xwr w Pr, N ~] food and drink. xwardan, xwar- [OS TEN-tn! < Ath, V fth; hwltn! | M xwrdn, xwr-, N ~] eat, consume. ~išn: food. ~ignig : edible. ~išnīh: eating, consumption. xwardār [hwit?I] (legally) edible, not murdār. xwardig [hwityk' | M xwrdyg, N ~i] food. xwārēn [hw’lyn'] edible. xwārēn- [hw’lyn-] cause to eat, drink; feed; irrigate. xwarģ [wig | J xwwrg] ember. xwārīdan, xwār- [heo?1-ytnt] drink. —išn: drink, drinking.
PHD.txt:665:xwarūfrān [hwl(’)wpl’n' | M xwrwpr'n) sunset, west. xwarrah [GDE < A gdh | (M prh, N farr)] fortune, glory, splendour. ~6mand [-’wmnd] fortunate, glorious. xwarséd, v. xwarxséd. xwartar [hw ltl] minor (sins). xwarwarān [hwlwPn!, -bPn'] = xwardfran. xwar(x)8éd [Azl(h)syt' | M xwrxšyd, № xuršēd] sun. xwāstag [NKSY A < A nksy’; hw'stk! | M xw’stg, N ~a] property, wealth. i ~õmand [-wmnd] wealthy. xwastan, !xwāh- [(Y)PLHWN-tn! < А V plh; hwstn!, hw'd- | J xwh-, N xwast] tread, trample; thresh. ~išn: trampling. xwāstan, *xwāh- [BOYHWN-stn! < A МУ Бу; hw'stn!', hwd- | M xw’stn, xt h-, N ~] seek, want, desire; attract, acquire. --j&n : desire, attraction. xwastüg [hwstwk!' | N xustū] confessing, believing. ~ih: confession, belief, faith. xwaš [BS YM < А bsym; hw | M xw, N ~] pleasant, sweet, nice. ~ih: pleasantness, pleasure. xwēd [Awyt! | M xwyd, N ~] moist, fresh. ~ih: moisture, freshness. xwédódah [hwytw(k)ds, -d^t! = Av. x"aetwada0a-] kin-marriage. xwēn-āhan [Ahw(y)n ?syn! = Av. x"aéna- (ayah-)] shining metal. xwēš [NP ŠE < А npf-h; hwyš | M xwy(b)s, N ~] (one's) own. ~ih: possession. ~awand [kwyš*wnd | N ~] relative, kinsman. xwēšēnīdan, xwēšēn- [/nwyfyn-ytn!] appropriate, make one’s own. xwēš-kār [леу dutiful. ~th: proper function. xwēš-tan [NPSE tn! | N ~] self. xwéy [hwyd | N xway] sweat, perspiration. xwistan [hwystn'] sweat, perspire. xwurd [hwlt' | N ~] small, little. xwurdag [hwltk' | N ~a] something small, particle; astr. lunar mansion; (horse's) pastern. ~ih: smallness.
PHD.txt:718:acquire ayāftan, handóxtan, wind- ādan, xwāstan.
PHD.txt:1571:desire (v.) abāyistan, kāmistan, xwāstan,
PHD_mackenzie.txt:5648:xwastal1 [NKSYA < A nksy'; hw)stk' I M XlV)stg, N .......a] property,
PHD_mackenzie.txt:5651:xwastan, lxwah- [(Y)PLHWN-tn l < A"; p[~; hwstn', h'llld- I J xwh-,
PHD_mackenzie.txt:5654:xwastan, ixwiih- [BOYHWN-stn l < A ..; bCy; hw)stn l , hw)d- I M
PHD_mackenzie.txt:5657:xwastiil1 [hwstwk I N xusiU] confessing, believing.
PHD_mackenzie.txt:8701:xwastanl              \\~\~Cl)   pazdagih                A(J~tU
PHD_mackenzie.txt:10061:xwastagI                 ""C» 5\     nigar-                 -~,\
PHD_mackenzie.txt:10435:xwastan1
PHD_mackenzie.txt:11912:xwastiigih              .AU~'~        ""   uskarisn                 ,~~~
PHD_mackenzie.txt:11913:xwastiig                  \.sne» to'"      uskardan                 ,,~,U)ya
PHD_mackenzie.txt:12122:xwastan                       \\tUtNt»         anag                              t~~
### PHD šēb
### NYB
2131:jāyišn [y?dšn'], 70!? jahišn [yhšn'] For- tune, luck, dispensation 2?!. 145; ~ u zaman <i> brihenišn rād 14'?, v. zaman; murvāk ~ i névak augury (and) good Fortune (i.e., good Fortune revealed through augury) 18!; pat névak ~ <u> yazdän hayyārēh with good fortune and the help of the gods 121-4; 121°; pat ~ hayyārēh i pat martömän xrat veh For- tune (giving aid to =) favouring men, wisdom is the best thing [she gives] 7012-13, Skr. v. siddheh sahāyatāyai ma- nusyanam buddhih uttamā; cf ke [for ka] ~ hayyär pat martömän cis + xrat veh when Fortune (is a helper to =) favours men, wisdom is the best of things PT 675-5, with the explanation cé hakar par- kast xvāstak be šavēt aivāp cahārpād be mirét xrat bē mānēt for if wealth dwindles and is lost or animals die wisdom remains; pātixšāi han névaktar i... xrat u dānišn nēvak api-$ ~ hayyäreh apāk that ruler
3711:tan [tn'] body, passim, stalk of a plant 9524; ~ u jan body and vital spirit 1523. 6422 (the constituents of human physical nature); ~ u jan u hir u xvāstak 4%; kanišn 4 jan u višopišn i ~ the destruc- tion of the vital spirit and the decom- position of the body (= the physical death) 64191; ~o as opposed to the immortal soul, ruvān 6625. 6820, 6927, 7615-17-18; — — also refers to the human individual as a whole, with all its physical and spiritual qualities, cf 65? sqq. 6611. 8414. 8671; har —-E rad hamgöhr fravahr et 4 x"eš paitak it is revealed that every human individual has its own fravahr (g. v.) of the same substance as itself 88°; xueš.— and ~ 4, avēš v. aueš; — ~ i pasen the ultimate form of existence the Universe will be given after the now running eycle of millenia has elapsed, the next world, Eternity; very often ristaxéz (q. v.) u ~ + pasen: 12%, 6411-13, 7118-19, 7610, 8326, 8821, 919; ~ 4 pasén alone 5212-13, 66°. 677. 934. 104%. — Av. (633 sqq.) tanū-; common Ir.
4360:to summon a p. to one’s side 2?-3-12, 56, 104 ete.; without 6 pes 625, 73. 315; Ohur- mazd ast hac damik ... x“ahét O. will call up the bones from the earth 100'2-13; vas a«vāhišn (q.v.) i rüpak-karihà xvāhēt he clamourously utters many implorations 7426-27, — 3. to ask, to demand: pat zan ~ to marry a wife 675; pat zanéh ~ to ask in marriage 1165-5; hac Papak past (g. v.) u zinhär xvāst 214; 3 rēc jamān x“äst he solicited a time of three days for consideration 11819; 121%; mizd dātihā ~ to demand reward righteously 8120-21; hac x"at karap margēh 4 Zartuxšt x"àst, apar cé āivēnak margēnītan he asked the karap himself about the manner of Z.'s death, how to put him to death 4812-13; sāi u baz ~ hac to exact tribute from 177. 58%; Pourušasp hàn hom hac Dugdāv apāc x"àst P. asked D. to give him back that Haoma 42?4-25,. 4, to seek,to search,to look for, to ponder, to strive to attain: api-ščin hàn hom x"àst they searched for that Haoma 409; pat ~ 4 hàn i či zuarrah in striving to attain his Glory 4614, more fully + an inf: api-š hàn xarrah bē aydftan x“dst 4618; — with an abstr. subst. as its obj.: v. cärak, ddrišn, dösäram, hucasmeh, ken, panäh, zivišn, ete.; cf also s. v. az"àyisneh. — Olr *hväz-, MPrth wx'št, pres. wz?z-; MPrs xw'stn, xwh-; Paz. NP z"üstan audah-; Verbum 187; Ghilain 69; Bailey, BSOS VI, 1930, 74. V. also x“dstar, -ēh, zuäyısn, -ēh.
### CHEUNG
576:say’, *huah ‘to strike, thresh’ and *xar ‘to go, pass’. 
6568:to *huah.The genuine Пг. continuation of ‘hail’ is attested in Skt. and several Ir. 
9923:*huah 141 
9981:*huah ‘to strike, thresh; [inch., intr.] to become tired’ 
9994:142 *huah 
13667:202 *Huahl 
13681:*Huah ‘to shine 
13709:*Huah ‘to dwell, remain 
13738:*HuaHl 203 
13749:*HuaH! ‘to blow’ 
13774:an unknown root. The preform should rather be: *pati- + *HuaH'. > Samadi: 145, 
13796:204 *HuaH2 
13799:*HuaH’ ‘to be incomplete, empty, lack’ 
55456:*HuaH’, *taus 
55488:*HuaH? 
55597:*dar? (s.v.), *huah (s.v.), 
55651:*Hhaus, *HuaH' (s.v.), 
55744:*(d)man (s.v.), *huah, *Hubj 
55749:*gan, *huah, *kap/f' 
55784:*damH°, *HuaH!, *pazd' 
56331:(s.v), *gauz (s.v.), *HuaH? 
56449:*Huah’, *mai9H!, *аі 
57542:*(d)man, *Huah? 
57819:*diHp, *drafs, *Huah', 
58075:*daub, *gan, *huah, *jan, 
58214:*huah
```


## [2026-09-14T03:10:27.452Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '9975,10000p' CHEUNG.txt\necho \"#### huaz\"; grep -n \"\\*huaz\\|\\*huāz\\|huaz \" CHEUNG.txt | head -20"
}
```


### [2026-09-14T03:10:27.526Z] TOOL RESULT

```
swete, Engl. sweet (etc.) 
*REFERENCES: EVP: 98; Abaev, Slovar’ I: 90 f.; EVS: 96b; Werba 1997: 401; NEVP: 97; Korn 2005: 
226, 228, 410 


*huah ‘to strike, thresh; [inch., intr.] to become tired’ 

*AVESTAN: (+ *pati-) Y Av. paiti x'arh- ‘to thresh’ = Liste: 18 

Pres. aja-: IND. 3sg. YAv. paiti x'aghaiieiti (Y 57.10); Partic.: perf. pass. Y Av. x'asta- (V 7.35) 
*MIDDLE PERSIAN: BMP hws- /xwas-/ (pret. stem) ‘to trample’ || (+ *fra-) MMP 


frxw’h- ‘to tread, trample’ > DMMPP: 158b 
Partic.: perf. pass. BMP hwst /xwast/ || (+ *fra-) Pres.: IND. 3pl. MMP frxw’hynd; Partic.: perf. pass. 
MMP prxwst 


142 *huah 


*PARTHIAN: Wx's-, xw’s- (inch.) ‘to become weak, enfeebled’ = DMMPP: 348a, 
366a 

*KHOTANESE: OKh. hvai- (hvas-) ‘to strike’ || (+ *ati-) OKh. ttähvai- ‘to thresh, 
#### huaz
```


## [2026-09-14T03:10:33.584Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '10000,10040p' CHEUNG.txt"
}
```


### [2026-09-14T03:10:33.639Z] TOOL RESULT

```
*KHOTANESE: OKh. hvai- (hvas-) ‘to strike’ || (+ *ati-) OKh. ttähvai- ‘to thresh, 
strike’ || (+ *pati-) pvah- ‘to strike’ || (+ *fra-) LKh. hahva- ‘to hash’ || (+ *nis-) 
ne’hve- (nei’hvas-) ‘to cross; conquer’ = SGS: 156, 39, 60 

*SOGDIAN: BSogd. y(w)’w(-), BSogd. xw’w(-), MSogd. x’w(-) ‘to hit, beat’ (+ pres. 
*ya-suff.), ? SSogd. xw yk PN (UppInd.257) || (+ *apa-) BSogd. ’pxw’y, CSogd. 
pwx’y, MSogd. pxw’y ‘to cut off? || (+ *aua-) BSogd. ’wx’’k ‘pestle’ (SCE: 249) || 
(+ *us-) BSogd. (’)sxw’y ‘to lift; to take’, CSogd. swx’y ‘to lift, raise’, MSogd. 
sxwst- (pret. stem) ‘to take away’ || (+ *pati-) SSogd. ptxws, BSogd. ptxw’y, CSogd. 
ptwx’y, MSogd. ptxw’y ‘to kill, put to death’ || (+ *pati-us-) ? BSogd. pcxw’y-, 
CSogd. pcwx’y- ‘to hinder, withstand’ || (+ *para- or *pari-) CSogd. prxw’y ‘to 
tread’ || (+ *fra-) BSogd. Brxw’y ‘to chop, cut up’ || (+ *nis-) BSogd. nsx(’)ws 
(pass.) ‘to be torn , || (+ *ui-) CSogd. ywx’y ‘to severe, separate, divide’ (with 
dissim. *ui ... *u > у... w) || (+ *ham-) BSogd. 'nxw y, MSogd. ’nxw’y ‘to break, 
infringe, goad’, (rather prev. *ni- ?) MSogd. nxwy ‘to crush’ 

Pres.: IND. 3sg. BSogd. y’wt, 3pl. BSogd. yw’w’nt, OPT. 3sg. BSogd. yw’w’y || (+ *apa-) Pres.: OPT. 
3sg. BSogd. ’pxw’y’y, CSogd. "pwx'y; Impf.: IND. 35р. MSogd. pxw’y; Inf.: pret. BSogd. ’pxwsty, 
BSogd. pxw’sty, CSogd. “pwxsty, CSogd. pxwsty || (+ *us-) Pres.: IND. 35р. BSogd. sxwyt, OPT. 3sg. 
BSogd. sxw’y’y; Impf.: IND. 3sg. SSogd. ’sxw’y, etc. || (+ *pati-) Pres.: IND. 3sg. BSogd. ptxw’yt, INJ. 
159. CSogd. ptwx’yw, MSogd. ptxw’yn, etc. || (+ *pati-us-) Pres.: SUBJ. 1sg. CSogd. pcx’yn, OPT. 1р1]. 
CSogd. pcx’ym; ’z-Impf.: IND. 3sg. CSogd. pcx’y’z, etc. || (+ *para- or *pari-) Pres.: OPT. 3sg. CSogd. 
prxwy’. || (+ *fra-) Pres.: IND. 3pl. BSogd. Brxw’y’ntw || (+ *niš-) Pass.: pret. intr. IND. 35р. BSogd. 
nsxwsty, 3р1. BSogd. nsx’wst’nt, OPT. 3pl. BSogd. nsxwst’ynt || (+ *ui-) Pres.: SUBJ. 3р1. CSogd. 
“ywx’ynt, Impf.: IND. 3sg. CSogd. yxw’y; Fut.: IND. 3sg. CSogd. ywxytq’; Partic.: perf. pass. CSogd. 
ywxsty, CSogd. (pl.) ywxstyt || (+ *ham-) Pres.: IMPV. 2pl. MSogd. nxwyöö; Impf.: IND. 3sg. MSogd. 
ımnxwy; Pass.: pret. intr. IND. 1sg. MSogd. "nxstyy kim ‘I have been goaded’ 


*CHORESMIAN: xw’h- ‘to thresh’, mX's- (inch.) ‘to become tired, weak’, m/X(w)’sy- 
(inch.-caus.) ‘to free, release’ || (+ *apa-) m/pxs(y)- (intr./pass.) ‘to be cut off (or 
‘struck off’ ?), m[pxy- (caus.) ‘to cut off (‘to strike off ?) || (+ *pati-) pcx’w- ‘to hit 
on, into; claw’ (+ pres. *ua-suff.). Ф The appearance of -h- in Chor. xw’h- is 
peculiar, since old Ir. *-h- regularly disappeared in Choresmian (and, indeed, in 
most, if not all, East Iranian languages). Perhaps, Chor. -h- continues the restored 
ruki *$. = Samadi: 244, 232, 245, 165, 146 

*BACTRIAN: (+ *ш-) ovyoaoo ‘loss, deprivation = S-W, Bact.: 214a 

*NWIR: Widely attested: Kurd. (Kurm.) xistin/xi-, xin-, (Sor.) xa- ‘to strike, beat; to 
place’, (orig. ppp.) NP x'ast ‘beaten road; rubbed’, Tt. xwah- ‘to thresh’, Abyan.
```


## [2026-09-14T03:10:35.353Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"xw’stn\\|xwāstan\\|xw'stn\" CHEUNG.txt | head -20; echo \"### roots list around\"; grep -n \"^\\*Hu[aā]\" CHEUNG.txt | head -30"
}
```


### [2026-09-14T03:10:35.425Z] TOOL RESULT

```
### roots list around
2103:*Huar ‘to cover’, which is not mentioned in DKS: l.c. 
13576:*Huad ‘to carry, lead (away); to marry (a wife)’ 
13610:*HuadH 201 
13651:*HuadH ‘to raise one’s voice, speak’ 
13681:*Huah ‘to shine 
13709:*Huah ‘to dwell, remain 
13738:*HuaHl 203 
13749:*HuaH! ‘to blow’ 
13799:*HuaH’ ‘to be incomplete, empty, lack’ 
13828:*Huaid(H) ‘to be devoted to’ 
13849:*Huaj ‘to put out’ 
13865:*HuanH 205 
13923:*HuanH ‘to throw (out), spread’ 
13963:*Huar! ‘to cover’ 
13988:*Huar2 207 
14024:*Huar? ‘to ward off, defend, protect (топ)? 
14097:*HuarH ? ‘to pluck, tear out; rob, plunder’ 
14134:*Huarj ? ‘to turn, lay around ?’ 
55454:*Huaid(H) 
55456:*HuaH’, *taus 
55488:*HuaH? 
55898:*Huad, *iat (s.v.), *kars/xrah 
56449:*Huah’, *mai9H!, *аі 
57044:*Huarj 
57199:*Huad 
57377:*HuarH 
57504:*Huaj 
57649:*HuarH, *raup! 
57952:*HuadH, *juar, *uab/f' (s.v.), 
58138:*HuarH
```


## [2026-09-14T03:10:40.824Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^\\*hu\" CHEUNG.txt | head -40"
}
```


### [2026-09-14T03:10:40.875Z] TOOL RESULT

```
6504:*hu- > f-), pace WIM III: 58 ff., as we have similar forms with initial f- in Elr. 
9923:*huah 141 
9954:*huad ‘to become, make savoury, pleasant’ 
9981:*huah ‘to strike, thresh; [inch., intr.] to become tired’ 
10046:*huaid 143 
10078:*huaid ‘to sweat’ 
10123:*huanH ‘to call’ 
10171:*huap/f 145 
10204:*huap/f ‘to sleep’ 
10284:*huar 1 147 
10309:*huar' ‘to consume, eat’ 
10359:*hu- > f- might explain Siv. far-, Khr. for- ‘to eat’ (and some other Central Iranian 
10401:*huar3 149 
10404:*huar? “to sound, swear’ 
10448:*huar ‘to swear’ etymologically separate from *hyar! ‘to eat, consume’. 
10460:*huar? ‘to take’ 
10489:*huar ‘to have a sore, scratch, itch’ 
10516:*huar ‘to paint, colour; to stain’ 
55660:*huad 
55664:*huad 
56039:*huar’, *kar (s.v.), *pais 
56145:*huar! 
56793:*huar* 
57188:*huad 
57190:*huad 
57330:*huar’, *pais 
57978:*huar 
58101:*huar’, *sap 
58214:*huah
```


## [2026-09-14T03:10:45.356Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '9954,9981p' CHEUNG.txt"
}
```


### [2026-09-14T03:10:45.421Z] TOOL RESULT

```
*huad ‘to become, make savoury, pleasant’ 

*AVESTAN: Y Av. x‘asta- (ppp.) ‘cooked, well done’ (Y 11.1, V 5.52, V 19.40, etc.), 
OAv. hudoma- ‘sweetness’ (Y 29.8) 

*CHORESMIAN: (+ *pati-) pcxw z- ‘to be fragrant? © Samadi: 147 f. 

*NWIR: NP x'a(y) ‘taste, flavour’, Bal. wad, Kurd. xwey ‘salt’ 

*NEIR: Pash. xwand (m.) ‘taste, pleasure’ (Cheung 2004: 129), Sariq. xud(in) ‘rich, 
buttered dough or bread’ || (+ *a-) Oss. I. axodyn/axost, D. axwadun/axwast, axust 
‘to taste’ 

*SANSKRIT: svad ‘to make, become savoury, taste’ (RV+) > EWAia II: 788 

© The laryngeal disappeared in IIr., on which see further Lubotsky 1981: 137 f. 

«PIE *sueH>d- ‘to make, become savoury’ = LIV: 606 f. | Pok.: 1039 f. 

*IE COGNATES: Gr. evade, &óe (aor.) ‘liked’, Lith. südéti ‘to salt’, Toch. A swär, OE 


swete, Engl. sweet (etc.) 
*REFERENCES: EVP: 98; Abaev, Slovar’ I: 90 f.; EVS: 96b; Werba 1997: 401; NEVP: 97; Korn 2005: 
226, 228, 410 


*huah ‘to strike, thresh; [inch., intr.] to become tired’
```


## [2026-09-14T03:10:59.021Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==132' HRN.txt | head -60"
}
```


### [2026-09-14T03:11:00.230Z] TOOL RESULT

```
— 110 —
495. lym 'Schlaf, /ahtdefK
Kä§. ;^öw?[es; hevoft 'schlafen*.
aw. /'a/wa- *Schlaf; phlv. /*'äÄ; ai. svdpiw-; arm.
^un (H. No. 295).
kurd. /evii, /evin; af/. LW. yöb; bei. ^?a/>, n. väir
(410).
496. x'^^^ 'leicht, gerade; niedrig, verächtlich', x^^ärT,
aw. /'ad-ra- (Geldner, KZ. 25, 478, Studien I, 17
folgg. ; Darm est eter. Et. ir. II, 189)'); phlv. /"är, nur
in der Bedeutung 'leicht', /"änha *leichtlich' (Sa le-
rn an n, Mel. asiat. IX, 234).
LW. kurd. /(^r; afy. /'är; bei. vär (290).
Die Bedeutung 'niedrig, verächtlich' ist erst neu-
persisch.
497. i^äfiten 'wünschen, wollen, Praes. /"ähem, /"äliis,
/"äste 'Besitz'.
ai. l/^soad-, svädati 'sich schmecken lassen, Gefallen
finden*, svädate; gr. rjdoftat. Vergl. np. /iväi (No. 502).
phlv. yyastan 'wollen, wünschen', /^ah(i)§ff, x^stär,
y^astak 'Besitztum' etc.; kurd. /^dsthi , ;jfMSfni; bei.
vergl. västa 'für "(413).
498. x^äW/ 'Tischdecke; Tisch (gedeckter)'.
aw. /^'^aini' 'Teppich, Überzug, Decke',
kurd. LW. /an; af/. /^än; bei. n. vän 'Platte, Teller'
(289).
Geldner, Studien I, 17/8.
499. yiyänden Vufen, lesen etc.', /emden, /unlde, /unyä
'Musik, /unyäyer,
aw. l/";^^«;/- in /^anaf.ca/ra- ('klirrend'); phlv.
X'^äntan, /untt (GF.) ; ai. [/^svan-, sodnati 'tönen'.
kurd. y^ändin^ /ündin 'lesen; oss. d. /önim, i. xöJiin
'nennen , heissen , rufen , einladen' (305) ; bei. vänag,
n. vanay, vänganay 'lesen, recitiren, studiren' (412);
wa;f. ^an-am 'reden, sagen, sprechen'.
*) Sahn. I, 170 Vers 745 steht np. j^^är direkt im Gegensfttz zu
(hfsvär, wie im Awesta '^^äSra- zu (Inzä^ra-,
```


## [2026-09-14T03:11:12.904Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### HUB xvastan\"; grep -n \"x'âsten\\|xvästen\\|svad\\|svādati\" HUB.txt | head -20\necho \"### BQT v2 leaf 240 area: search خواستن\"; grep -n \"خواستن\" BQT_v2_pages.txt | head -20"
}
```


### [2026-09-14T03:11:12.975Z] TOOL RESULT

```
### HUB xvastan
2027:svadhd- genannt werden, indessen wiirde letzterem nur
7026:= daJatuv; x^dham 'wiinsche', skr. svad; sipdh *Heer =
7071:ap. radiy Vegen*; x^ai {x^a) *Wohlgeschmack' = skr. svada-;
7738:geschmack' (oben p. 57), skr. svad; x^andan *rufen, lesen',
### BQT v2 leaf 240 area: search خواستن
1745:  ‫زرا که زنان بررشوهران اقتراح کهرادندی آورزوها خواستندی» «التفپیم ‪ >۶۹۲‬رك ‪ :‬بشت ‪: ۱‬‬
6075:           ‫خواستن» مشتاقانه خواستن) «فررهنك اوستا ‪ -‬انگلسی‪ .‬کنگا ص ‪ ۹۷۱۳‬چشبدن («‪.‬م‪).‬‬
10206:  ‫‪.‬‬    ‫ابر لندی ‪uidiug‬‏ (خواهس میکنم)» در ترحجمه و تفسس بهلوی ‪natsahZ‬‏‬                      ‫کردن ‪ ۰‬درخواستن)‪.‬‬
10965:             ‫فم بوستالی‌است لیکن طبیعت ‏ از‬                      ‫ملاثکه و فرختها کردن وزن خواستن ‪ 7‬و نام‬
12096:                      ‫آفتاب عالمتاب است ‪.‬‬                     ‫‪۱‬‬                    ‫خواستن باشد ‪.‬‬
14188:    ‫خواستن آرزو کردن)‪ .‬کردی ‪( 01122۷1‬من‌میخواهم) ‪ ۰‬مازندرانی ‪( 22۷722011‬کین‌خواء)‬                                                        ‫‏(‬
14230:   ‫» خواستند که خوازه‌ها‬   ‫رسف‬    ‫تزدىڭ شاور‬       ‫شنبدند که آمیر (مسعود)‬             ‫‪ 2‬اشان جون‬      ‫‪۱‬‬
14237:         ‫‪ . ۴‬مصدر مرخم «خواستن» ‪.‬‬              ‫‪1‬‬    ‫‪_ ۳‬مخفف آ خوحت («‪.‬م‪).‬‬                        ‫دهشدا) باشد ‪» .‬‬
14283:            ‫بدیبا وخوالیگران خواستند ‪.‬‬                                  ‫یکی خانه او را بباراستند‬
14314:        ‫مال واسباب وخواسته وخواستنی باشد ‪.‬‬
14341:   ‫‪٩‬‏ ‪ -‬پازند ‪. 802‬افتانی ع ‪( 05‬قشنك)»ساس کربت_‪(5۷۳3۷115‬ازلا‪( 5‬خوب)‬                             ‫دخواستن» ‪.‬‬
14351:                            ‫کردن » بمهمانی خواستن ‪ -‬دعاکردن ‪ -‬تغنی کردن‪« .‬ناطم الاطباءِ > ‪.‬‬
14637:    ‫بنظر میرسد «چیز بدست آمده‪ .‬چیز خواسته»بوده است وسیس‌بمعنی «چیزخوب» چیز خواستنی»‬
17340:                    ‫از «درخواستن‬         ‫‪۴‬‬         ‫از ‪ :‬درخش ‪ ۳‬بدن (یوند مصدری) ‪.‬‬                     ‫‪۴‬‬
19514: ‫دف زدن * کسنابه از خواستن ‪-‬‬                                      ‫دف‬                      ‫عربی بمعنی بهلو‬
19564:‫ودق رومی ‪ -‬وبکس آول وتشدید انی در عربی‬                       ‫‪-‬‬    ‫وسر فی هو ®‬    ‫دكاست بمعنی کدابی وخواستن ‪۳‬‬
19606:‫کوسفند ازآن بغورد بجای شیر خون ازیتاش‬                 ‫دق ردن د بیعنی خواستن گودایی‬
20413:                        ‫کودنه خواستن هم هست ‪.‬‬            ‫دندان ]ریز ‪ ۱‬با مزه بالف‬
20428:                 ‫و کینه خواستن هم هت ‪.‬‬
21802:                                       ‫فرزند درخواستن ‪.‬‬
```


## [2026-09-14T03:11:14.394Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### MON files\"; ls -la MON_part1.txt MON_part2.txt; head -5 MON_part1.txt\necho \"### grep خوست\"; grep -c \"خوست\" MON_part1.txt MON_part2.txt\necho \"### grep شیوا\"; grep -c \"شیوا\" MON_part1.txt MON_part2.txt"
}
```


### [2026-09-14T03:11:14.496Z] TOOL RESULT

```
### MON files
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
0 
2 


چم 
### grep خوست
MON_part2.txt:1
MON_part1.txt:6
### grep شیوا
MON_part2.txt:3
MON_part1.txt:10
```


## [2026-09-14T03:11:20.842Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 238 239 240 241 242; do echo \"=== leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v2_pages.txt | head -8; done"
}
```


### [2026-09-14T03:11:21.727Z] TOOL RESULT

```
=== leaf 238
   ‫کوپ‬                                                                             ‫خواجة اختران‬
‫خلیفة خواجه مودود وخواجه محمد ریکه‌روان‬            ‫اخة آن » کناب از تاره‬           ‫اوجه‬
                                                                                      ‫ح‬
‫خلیفة خواجه خان‌سعید درآن موضم باهم‌صحیت‬                      ‫عتری ماش ۔ وآفتاب را نیز گونند ‪۱‬‬
                                   ‫داشته اند ‪.‬‬
                                                   ‫خواجه بار ۔ با باابیمد بروزن‬
‫خواحة فلك ‪ -‬کنابه ازآتاب ‪-‬‬
                                                    ‫آشدنکرها بعربی‬
=== leaf 239
 ‫خوازه‬                                                                                                                     ‫‪۷‬‬           ‫‪-‬‬


‫بمعنی خوردنی ورزق وروزی باشد ‪ -‬و جضم اول‬                    ‫‪ -‬ونام ولاسی‌است درحوالی ری‪٩‬‏ ‪ -‬وعم‬                                        ‫هت‬
‫بروژن شماره » بمعتی دستورباشد که رسم وقاعده‬                 ‫اول و ثانی بالف کشیده بر وزن شمار " بمعنی‬
‫وقانون است ‪ -‬و طعامی را نیز کوبند که مقوی‬                         ‫باشد "‪ ۳‬وبعربی | واز کاو را خوانند ‪۰‬‬                              ‫خوردنی‬


=== leaf 240
 ‫‪“VAY‬‬                                                                                                      ‫خوای‬
‫هر گاه‬    ‫چنانکه‬   ‫ارادی باشد‬     ‫راستی » بمعنی‬         ‫سازند ‪ ۱‬؛ وبایتمعنی بقتح اول بروزن ملازه هم‬
‫کوبند «حر کت خواسی » ازآن حر کت ارادی‬                                                                ‫آمده است ‪.‬‬
                                        ‫خواهدد ‪.‬‬
                                                         ‫خو اس س بانانی معدوله بروزن طای‪.‬‬
‫حو اسه = بفتح اول بر وزن نواسه ‪۰‬‬                        ‫بمعنی خواستگار و طلبکار باشد ‪ -‬و بفتح اول‬
 ‫نند‬ ‫صورتی باشد که در فالیزها و زراعتهپا نکصب‬             ‫بروزن‌پلای» بمعنی تریس و بیم وهرای باشد ‪.‬‬
‫تا وحوش وطبور ازآن رمیده خان بکشت زار‬
=== leaf 241
‫خوان پابه‬                                                                                                      ‫یز پا‬
                                                      ‫خوالگر ‪ - ۱ )۱‬باانی معدوله بر باشد ‪.‬‬
‫حوان ه با نانی ممدوله بر وزن نان »‬                               ‫وزن شالگر (‪ .)۷‬مطبخی و طباخ و طعام پز را‬
‫کنابه ازخوردنی وماده باشد ‪ ۵‬و‪-‬طبق بزرگی‬                          ‫گویند ‪ - ۴‬و بمعنی سفره چی هم بنظر آمده‬
                                                                                                                    ‫است‬
          ‫را یز گوبند که از چوب ساخته باش‬
     ‫طندبچه‬
     ‫ق‬
=== leaf 242
 ‫‪۷‬‬                                                                                             ‫خوانچة زر‬
                                                ‫خو) نجه‪ .‬ررو خوانجه‌دد لن‪-‬‬
                                                         ‫‪۱ ۶‬‬       ‫‪۰‬‬     ‫‪۰‬‬         ‫‪۰‬‬       ‫‪۰‬‬      ‫‪۰‬‬

‫خواو؟ = با ثانی معدوله بروزن گاو ‪۰‬‬
   ‫بممنی خواب است که بعربی نوم خوانند ‪*.‬‬
                                                 ‫‪“e‬‬                                    ‫‪6‬‬          ‫‪۲‬‏‬
                                                      ‫و حوانجه‬               ‫سهر‬       ‫خوانجه‬
```


## [2026-09-14T03:11:30.843Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==241' BQT_v2_pages.txt | tail -40"
}
```


## [2026-09-14T03:11:31.677Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -m3 -B2 -A6 \"خوست\" MON_part1.txt | head -60"
}
```


### [2026-09-14T03:11:31.898Z] TOOL RESULT

```
 ‫خو ال ‪ -‬با انی معدوله بروزن مال »‬                       ‫‏‪ me‬بائانی‌معدو له باس‌داز ‪۰‬‬       ‫خواستار"‬
 ‫دوده‌ای که بحهت ساختن سداهی ومر کب از دود‬
                                                         ‫لر وکواکار ور خواهتده و طلت هه را‬
‫چراغ کیرند؛ و صم اول بروزن جوال همأ مده‬                                              ‫کوند ‪#*.‬‬
           ‫است ‪ -‬وخوردئی را نگیوزبند *‪.۹‬‬
                                                         ‫خو استه ‪ = ۷‬بائانیمعدو له بروزن راسته»‬

                                                          ‫لءاه‬
                                                             ‫زر ومال واسباب وجمعدت ومامان وملك وا‬
          ‫وزن تاستان » دوات سیاهی رگاوبند ‪.‬‬               ‫وآ لچه دلخواه باشف ‪ 5 ۸‬وترجمه معنی همهت‬

 ‫خلوسته(‪)۳‬ا با انی مفدوله بر وزن‬
                               ‫ا‬                         ‫چنادکه‌درعربی گوبندباله‌منی فلان درفارسی گویند‬
 ‫دانسته» بمعنی‌خو الستان(‪ )۲‬است که دوات ساهی‬                                                      ‫بخواسته فلان ‪.‬‬
                                   ‫ومر کب باشد ‪.‬‬          ‫خو استی* = با ثانی ممدوله بر وزن‬

    ‫‪:‬وابته ‪1‬‬
           ‫م‪ ۱‬خ‬
              ‫(خ‪)۳‬‬                   ‫)‪ (+‬خم‪ : ۱‬خواستان !‬                      ‫‪.‬‬       ‫(خ‪)۱‬اچگشی‪:‬نه‬
   ‫» خواستند که خوازه‌ها‬   ‫رسف‬    ‫تزدىڭ شاور‬       ‫شنبدند که آمیر (مسعود)‬             ‫‪ 2‬اشان جون‬      ‫‪۱‬‬

   ‫؟ ‏ لغتی در «خوست؟ بمعنی‌مالیده‬                 ‫‪٩‬‏ ‪.‬‬
                                                      ‫حن‪۲‬و‬
                                                         ‫زنند وبسیار شادی کنند ‪« » .‬بیهفی ‪ 44‬مت‬
   ‫)‪۰٩1‬‏ ‪ « :‬باشومت آن‌باشد‬      ‫‪ .‬درلغت فری آمده ( ص‬              ‫‪ :‬آبشخوست و بای خوست‬              ‫و کوفته رگ‬
  ‫که بیای دگرفته (کوفته‪ ۰‬دهضدا)رآبخوست |آ[ن باشدکه به ‪ .‬دهشدا] آب درهم گرفته( کوفته‬
         ‫‪ . ۴‬مصدر مرخم «خواستن» ‪.‬‬              ‫‪1‬‬    ‫‪_ ۳‬مخفف آ خوحت («‪.‬م‪).‬‬                        ‫دهشدا) باشد ‪» .‬‬
   ‫اوست بلکه بخواست‬        ‫همی دانیم که حر کت هرسه قم ازان (جم) تبهذات‬                           ‫_‬     ‫®‬
   ‫از‪ :‬خواست ‪ ۳‬ار (یسوندفاعلی "مبالفه)‪.‬‬             ‫‪1‬‬          ‫‪.‬‬     ‫ی‪۱‬‬           ‫واهر است» « زادالمسافرەن ‪۷‬‬

    ‫پهلوی ‪( 8152۷2‬مال)« مینا ‪« » ۲ :۹۳۱‬اسشق ‪ . ۷۹42‬ارمنی ع ‪12150‬‬      ‫‪۲‬‬
                ‫در ‪( ۲20120501‬وارت) » پپلوی ‪( ۲2012052۷2‬وارث) «هوشمان ‪۷۹٩4۰‬‏ ‪.‬‬
         ‫آونکه را خواسته است‌داش کم‪.‬‬                        ‫‪ ۸‬حر کرا داش است خواسته لت‬
    ‫‪۱‬‏‬
     ‫>‪٤‬‬‫شهیدبلخی‪« .‬تاریخ‌ادیبات ‪ .‬ش‪.‬فق‬
   ‫‪ = ۶‬خوار («‪.‬م‪ , ).‬چنانکه درخوالگر‬                      ‫از ‪ :‬خواست ‪ +‬ی (نسبت)‪- ‎‬‬                     ‫‪٩‬‬
    ‫بقه در صفحةٌ ‪۳.۸۷‬‬
          ‫( برهان فاطع ‪)۳۰۱‬‬
```


### [2026-09-14T03:11:31.949Z] TOOL RESULT

```
2332-
2333-آداک: 21 (۱.) خشکی میان در باه جز بره» 
2334:آنخوست. 
2335-
2336-آدخ: 5 (ص.) ضوب» نغز» نیکوه 
2337-میمون» مبار ک. () بلندی در زمین» تل» 
2338-شن 
2339-
2340-ادر: »702 [ع.] (ص.) باد خایه» دبه خایه 
--
29101-سریرگاه» دار مملکت؛ دارالملک. 
29102-پسای‌خست: 0.51 [- بسای‌خاسته - 
29103:پای‌خسته - پای‌خوست] (امف.) هر چیز که 
29104-در زیر بای کو فته شده باشد» لگدکوب؛ 
29105:لکدمال؛ پای خاسته» باخسته» بای‌خوست. 
29106-پایدار: ۳۰-۲ [- بادار - بایدارنده] (افا.) 
29107-استوار» پابرجاء پادار» جاویدان» ات باقی؛ 
29108-دایم قوی» مستقی؛ وطید؛ مّ. نابایدار. نام 
29109-ختدای مان است: است:ستله و ماذار: 
29110-پایین دار. کعبتین قلب. (فع. امر از بای داشتن) 
29111-استوار باش» ابت باش؛ راسخ و پابرجا
```


## [2026-09-14T03:11:46.375Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -B3 -A6 \"خوست\" MON_part1.txt | sed -n '30,200p'"
}
```


### [2026-09-14T03:11:46.446Z] TOOL RESULT

```
47755-
47756-
47757-لحاظ نشر دعوت به دوازده ناحیه تفسیم 
47758-کرده سودند که هر ناحیه را جزیره 
47759-می نامید ند. و کسی که در جر بره دعوت 
--
51519-
51520-
51521-روغن و شیرینی در یکدیگر مالیده باشند؛ 
51522:چنگالی» چنگال‌خوست. (مج.) شخص 
51523-باریک میان. آلتی فلزی از لوازم میز 
51524-غذاخوری که دارای دسته و سه با چهار 
51525-دندانه است؛. 
51526-
51527-چنگک: 6208 (امسر.) قلات منوا 
51528-قلابی که فیل را بدان رانند وضا 
--
70007-زادخور: 7.۲ 1- زادخورده | (ص‌مف.) 
70008-ییر. سالخورده فر توت. 
70009-
70010:زادخوست: ۱:.50- زادهدخسواست | 
70011-(ص‌مف.) پیر. سالخورده. فر توت. ضعیف و 
70012-ناتوان. 
70013-
70014-زادمرد: 7-01 [1< آزادمر د| (امر .) آزاد 
70015-مرد» جوانمر ده حرء صاحب همت. 
70016-
```


## [2026-09-14T03:11:53.940Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nfor n in 109 110 111 119 120 121; do echo \"=== pdf page $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' BQT_v3_pages.txt | head -6; done"
}
```


### [2026-09-14T03:11:54.905Z] TOOL RESULT

```
=== pdf page 109
[pdf page 109]
شهی

شهی » بروزن ‎yin‏ بمعنی پادثاهی
- ودامادی است چه داماد را يزشه کوبند ۱-
وهرچیز شیرین‌باشد عموماً وحلوابی کهازشاسته
=== pdf page 110
[pdf page 110]
-۳۹

- و زمیلی را یز کویند که باران برآن بارده
ومردم وحروانات بر بالای آن تردد و آمد وشد
بسیار کرده باغند وبمدازآن آفتاب خورده‌وخشك
=== pdf page 111
[pdf page 111]
Sx

کرت ‎SHYT‏ رومی یز ‎lye‏ و بفتح
اول هم کنتماند ؛ وبابای ابجد ایزدرست است .

=== pdf page 119
[pdf page 119]
alr

‌ ۳
یر ‎Sh‏ © بروزن ‎pt stam ate pa‏ ينك
است که لوعی از جوشش روی و بدن اطفال
=== pdf page 120
[pdf page 120]
۳۲۷
‎Slant‏ ۱ با شین قطه دار بروزن
بیباك » کوسفند یکساله را کوبند - و ‎ly‏ چار
تار را 5 کفته‌الد + وآن سازی است‌مشهور؟ .
شیشاث « بروزن ميخك + بمعنی شیخاله
=== pdf page 121
[pdf page 121]
ys

شقو موری »با فان ومیم هردوبواو
رسیده و ورای قرشت بتحتالی کشیده. لغتی
است ‎Vly‏ و معتی ‎OT‏ بعربی تین‌احمق باشده
```


## [2026-09-14T03:12:00.615Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nawk 'BEGIN{RS=\"\\f\"} /شیبا|شیوا/ {match($0,/\\[pdf page [0-9]+\\]/); print substr($0,RSTART,RLENGTH)}' BQT_v3_pages.txt | head -20"
}
```


### [2026-09-14T03:12:01.700Z] TOOL RESULT

```
[pdf page 110]
[pdf page 122]
```


## [2026-09-14T03:12:04.106Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\necho \"=== 110 full\"; awk 'BEGIN{RS=\"\\f\"} NR==110' BQT_v3_pages.txt\necho \"=== 122 full\"; awk 'BEGIN{RS=\"\\f\"} NR==122' BQT_v3_pages.txt"
}
```


### [2026-09-14T03:12:05.171Z] TOOL RESULT

```
=== 110 full
[pdf page 110]
-۳۹

- و زمیلی را یز کویند که باران برآن بارده
ومردم وحروانات بر بالای آن تردد و آمد وشد
بسیار کرده باغند وبمدازآن آفتاب خورده‌وخشك
شده ‎atl‏ چنان که نردد بر ‎OT‏ دشوار ‎oy‏ -
‎a!‏ را نیز گفته‌اند که رشتة تازبانه
باشد - وبدعنیآشفته ومدهوش وس گشته‌وبیخبر
ومتحیر و شذاب زده هم آمده است - و کربه
و نوحه راگویند که ازتهایت اندوه بائدوکون
را هم کوبن که بزبان عربی دبرخواند؛ و بائالی
‎Sy ne‏ ).5 کفته‌اند و با ‎Cab‏ قافیه کرده‌اند.
شیا ۱
کویند .
‎hee‏ ۲ بکر اول بر ‎lee O39‏ »
بمعنی آميخته و برهم زده و درهم کرده باشد -
و بعه‌نی لرزان هم گفته‌اند .
شیبا فیدن ۴ - بر وزن پبچاییدن.یسنی
آرد کندم وامثال آن را در آب و غبره‌آمیختن
‎er?‏ زدن - ویمعثی لرزانیدن هم آمده‌است.
شیب ‎VE‏ م با بای فارسی بالف کتیده

و ‎Das‏ زب

بر وزن ‎led‏ مار افمی را

و لام الف » بمعنی ترشی پالا بائد و آن ظرفی

(۱) چش؛ وبابای ایجد » چك : وبا با

شیور

است که مانشد کفگیر سوراخها دارد وبدان‌چیزها
صا فکنند .

شیبك ۴ - بر وزن بی بد » یعئی بر عم
زده شود - ویلرژد +

شیب الا - بکر ‎owt‏ وقتح بای ‎sent‏
‎alle‏ کنابهازدیا است که‌عالم کون‌وضادباشد.

شیبم ۴ - بروزن بیغم ۰ یعنی برهم‌زده
وآمیخته کردم ولرزان شوم .

شیبنده ‎٩‏ - بر وزن آزیبنده » بمعتی
آمیحته و برهم زده ‎٩‏ - ولرزان باشد .

شیب و ‎abe VU‏ از زمین ‎AAT,‏
‏است - و کنایه از راست و دروغ - وگرموسرد
° هت — و داد وستد دو امردرا یز کوبند از
‎oo a,‏ ۰

شیب و ‎Ved‏ - با ‎gis‏ بتحتالی
رسیده و ببای ‎aml‏ (۱) زده, اين لغت از اتباع
است و بمعنی سر کشته و مدهوش و شتاب زده
‎Wash‏

شود ۸ ۰ یک ارل با بای فارسی
بروژن می‌لور ۰ ‎pt‏ راگویند که برادر کوچك

۱ -اوستا- ‎xshvaewa‏ , پهاوی 56۱081 , 5106۷2۷ «اسشق *۸۰».قس‌بلوچی
‎shép_mar‏ انوعی ‎LL‏ فارسی ‎je‏ شبیا» ‎xsvaewanhd l=‏ 2212220 (افعی) س

پپلوی 02( 5 202661 . رك: هوبشمان ۸۰۰ .

« خشوئو» در اوستا صفت است بممثی زود

خزنده رتند. رونده : چست وچالاك . فغراادین کر کالی در وس ررامین کوید :

سر دیوار او پر مار شیبا

- اس ال از * شیبیدن» -
۴ - رك : شیبیدن . ِ-

۷ - رك : تیب وشیپ ‎eet‏ ولیپ .

‎Ole‏ از زخم آنها با شکیبا
۴ - متعدی «شیبیدن» .
سم فاعل از «شببیدن».

‏. «قاباص ۸-۱۹۷ ۰ .

‎ta ۱‏ آعیخته شونده.
۸ = شیبور . هردو درشاهنامه ‎oul‏ حر

‏فپرست ولف آندو به ‎Trompete ۰ Tuba‏ )5.2( ترجمه ‎read‏

‏بفرمود تا بر کشیدند دای

‏همان سنج وشیپور وهندی درای»

‎ANAS Neg ‏«شاعنامة‎

‏#بپور ازآرامی وسربالی گرفته شده «نقی زاده ‎Uae‏ باد کار

‎LOTT ‏چپارم‌شمار؛‎ JL
. ‏قیبور - رك : شیپور‎ #

=== 122 full
[pdf page 122]
lea

‎YN get‏ - با ‎gh‏ مجهول و واو بالف
کشیده . بمعنی فصیح بلیغ باشد.

‏شیوا ز بان «به‌نی‌ضیح زبا نکه‌بلیغ
بیان باشد .

‏شیوان ۲ ۰ بر وزن دبوان » بمعنی
آمیخته و برهم زده - ولرزان باشد .

‏شوانیدن ۴ = بر و زن‌پیچایدن ,

‏بعمنی آمیختن و بر هم زدن باشد عموماً و آرد
‎aS‏ و مانند آلرا درآب و ‎oT gual‏ آمیختن
را کویند. خصوصاًبویمهنی لرزالیدن‌همآمدهاست.
شیوشه - نم اول و الی و فتح شین
تقطه‌رار , شوش4ٌ طلا و فره را گوبند و آن طلا
ور کداخته است که در ‎beg‏ آهثین ریزد ۴
- و دلبالهٌ خربزه وهندواله را یز گویند.
شیوم ۶ ‎che‏ واو بر وزن بیفم »

‏یعنی بر همزده کردم وآمیخته شوم و بيامیزم -
وبلرزم و لرزان گردم.

‏شیون ‎tt ued‏ مجپول بر وزن
‎yaw‏ ۰ ناله و افغایرا گوبند که درهنگام محنت
و مصیبت کنند .

‏شیو ‎YO‏ © بر وزن زیبنده » بمعنی
آمیخته و برهمزده 4 - ولرزان ‎ath‏ .

‏شیوه - با ‎gh‏ مجهول بر وزن میوه +
بمعنی ‎SM‏ و کرشمه و طور و عمل و طرز و روش
و قاعده و قانون باشد ‎٩‏ - و ‎ner‏ هثر وکمال
همهست - و خویشتن لمودن و خودا‌ابی‌وزیبابی
- وخویی ولیکوبی کردن را ليزگوبند.

‏شیهه = اول و سکون ‎vt‏
‏و فتح ها » آواز وصدای اسب را گونند وبعریی
صهیل خوالند .

‏۱ - بقول هرن اوستا ‎at) xshvaewa_‏ ؛ سربع) ؛ پولوی 5082۵1 و ‎shévak‏
‎shal‏ 5۷۵1 (لفز نده ,لیز ) «اسشق ‎care‏ و بقول هوبتمان پهلوی 5۳6۳8 ‎Ty)‏ ۱۱:۰۱)
= پارسی ‎oxshaipa_ git‏ با ‎xShvaipa_?‏ .قس : ‎las‏ «هوبدمان ۸۰۵» ‎dy‏ فاباص

‎F NMA‏ رك : شیوانیدن » شیونده.

‏۴ - متعدی ‎Cosi t®‏ (رك:شیوم.شبوان:

‏شبونده ) . دزقولی ‎shevanidan‏ ( آمیختن »هم زدن [متصوصاً در ‎ty‏ چای ]) «امام» .

‏۴ 2 شوشه («.م.) ‏ شفشه(«م.) .
شیوانبدن » شیونده .

‏9 اول شخص منارع از «شیوبدن» رك:

‏۲ - پهلری ‎shivan ( shévan‏ « باروچا ۰۲4۵ ) » ابرالی

‏پاستان - ‎xshaivan‏ ۵, اومتا- 1510 (بدبختی » فقر » احتیاج) «بارتولمه ‎Spoon‏ ص

‎. 6

‏‘ - روزلخت چون‌دمرندی زدیم رمشق

‏*- اسم صوت .

‏¥_ اس فاعل از «شیویدن» . ‎By‏ شیوایدن .

‎eT gto - ۸‏ شوندم

‏شرطآن بو د که جز ‎Oley‏ شیوه‌ديرم.
« حافظ شبرازی ۲۵۷ ©
```


## [2026-09-14T03:12:33.338Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN leaf 199 (p178)\"; awk 'BEGIN{RS=\"\\f\"} NR==200' HRN.txt | head -50\necho \"=== HRN leaf 200 (p179)\"; awk 'BEGIN{RS=\"\\f\"} NR==201' HRN.txt | head -50"
}
```


## [2026-09-14T03:12:33.932Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '10930,10975p' BRT.txt"
}
```


### [2026-09-14T03:12:34.247Z] TOOL RESULT

```
=== HRN leaf 199 (p178)
- 178 -
799. Heb, sew ^Unteres, Unterteil ; Hinterer .
aw. /svaepä' 'Hinterer (y. 9 (11) Glosse), Darme-
steter, Et. ir. I, 57; phlv. vergl. n(i)sep etc. (unter
No. 1034).
LW. kurd. siw 'Thal'; afv. sewa 'Abhang ; bei. %),
n. sef 'Abhang, Thal' (261).
Säle mann, Mel. asiat. IX, 238 will auch np. sefte,
sewe (phlv. sev(i)sn, päz. sewasn, Men.) hierher stellen.
Np. sebtden vermag ich nicht zu belegen, wohl aber
aseblden (so wird zu lesen sein) bei AM. S. 145 Zeile 7,
wo es mit menis verbunden ist und 'Übelkeit erregen
bedeutet.
800. Sehä 'Viper.
aw. /JvaeAoa- (vd. 18, 65); phlv. s(e)päk d. i. s(e)vak,
V
801. Sed *61anz, Sonne' (Sahn.).
aw. x^ci^ta- ; phlv. set, Setäsp (Gemme), Setak *).
802. Str 'Milch', stre^ sinn (Käs. 7j,sTrem); vergl. hern]sTre.
aw. apaY/slra- (?); ai. ksvrd- 'Milch'; phlv. sJr-),
sTrin, sTrimh, vergl. arm. LW. hamsirak,
kurd. bei. (368) LW. (?) sTr 'Milch'; oss. d. a/ßir,
t. ä/sir (47) ; niinj. /sTr,
803. ser 'Löwe 3).
phlv. s^r 'Löwe'.
Zu den griechischen Schreibungen von np. Seröe
vergl. Nöldeke, TabarT-Ubersetzung, S. 361 Note 2,
Persische Studien, I, S. 21.
Darmesteter, Et. ir. I, 106 nimmt ;^sa^rya- als
Grundform an, dann müsste der 'König der Tiere'
schon ein arischer Typus sein, vergl. Spiegel, Ar.
Per. 54 (wo /sadra- statt /ßad^rya- falsch ist).
^) Np. ^arupfQvt^; bezw. 2!ntTa(pdQvrjq u. 8. w., die ich, Mitteilungen,
Heft IV, S. 32 No. 23, verglichen hatte, gehören natürlich nicht hierher,
vergl. Nöldeke, Literar. Centralbl. 1892 No. 27, Sp. 967.
^) Sir bezw. slrlnlh übersetzen aw. ^soipta-^ x^cvJa-^ ;(Suis-.
') Über das Vorkommen von Löwen in Pcrsien vgl. Blanford,
S. 29 folg.
=== HRN leaf 200 (p179)
- 179 -
804. Sevä 'beredt*.
aw. /svaewa- ^schnell, schnellend'; pblv. sepak d. i.
sevük,
af/. /vai 'schlüpfrig, glatt'.
Hübschmann, KZ. 27, 107 Note, gleichzeitig
Darinesteter, Et. ir. I, 85.
S.
seil s. sed (No. 725).
r.
805. yund, yunde Schaar, Menge; versammelt' (Belege in
SF und FJ, letzterer aus Daqiql).
phlv. gund 'Heer ; arm. L\V. gu7id 'Heer, arab.
LW. jiind 'Heer*; kurd. LW. grmd , jund 'Dorf (H.-
Sch).
skr. vptdä' 'Schaar, Truppe, Heer (Nöldeke, münd-
liche Mitteilung).
Die Stadt Crunde-Säpür {^Vandev-Sapür gehört nicht
hierher, vergl. Nöldeke, TabarT-Ubersetzung S. 42
Anm.
F.
806. fer^fere 'Kleie'.
Nöldeke (mündliche Mitteilung) vergleicht lat.
fiirfur 'Kleie, Gemeng*, das zu gr. Tjooffvofo 'sich un-
ruhig bewegen', (f.vQiuo 'umrühren', ai. V^hhur-, Jar-
bhurati 'zucken' gehören soll (Fick, Vergl. Wörter-
buch^ II, 168). Nöldeke hält den Übergang von r
in / durch die Fälle phlv. äta/s, Syäva/s, n(i)yoxsTtan
für erwiesen (vergl. np. niyösiden, No. 1070 An-
merkung). Vergl. KZ. 32, 585 No. 18.
807. feV", fir-^ Praefix 'vor, hervor, vorwärts' etc., z. B. in
fer/ujeste, fersüde^ fermän,
12*
```


### [2026-09-14T03:12:34.296Z] TOOL RESULT

```
KompE.  —  Zum  V.  xinav-,  —  Pü, :    Inäyäii. I       lärJA.
•  j.  xänümaine  Inf  'zu&ieden  zu  stellen': I  xm'  akuraAe  mazdä  anulanam  spmianam
Y.3. 1 ;  r,  a-4',  10,  -22. 4,  23,'N.  47',  Vdp. Zum  V.  xsnm.-.  —  VgL  xinaama-.  —  Pü.: pa  mäyetülär'ih,  Sü. !  lanmänat^tyä,  a\.  -.  päji. iatanma.
•  g.  xSina-  Pron.  a  Pers.  Plur.:  s.  unter yäsma-.
Ableil.
•  g.  xSmika-  Adj.  (fem.  °kä-)  'eurig': s.  unter  yüsmSka-.
Ableit.  aas  xlrnH:
•  g.  xämä'vant-  Adj.  'euch  ähnlich  (usw.)': s.  unter  yäsmävarti-.
•  j.  *xSmävaya.''g^uS.u^vi-  fem,  Adj. 'die  VioTic  xs7naiby3  gSu^  urvä  enthaltend, damit  beginnend':  'va  Aäitis(sd.y^  Y.  sp Überschr.;  —  'z-am  käitlm  yasamaide  Y.
25.12.
>)  So  Mf  I,  K  4  zu  V.  7g.  [1;  vgl.  j.  mävaya- ,-a  :  g.  maibyä,  %  434.  —  >)  D.  L  Y.  JJ.
j.  xsyö  F,  J:  lies  xiayö.
•  j.    xSvaepi-    £    'Hinterer,    HinterteQ':
°paya  vainaya  bar^sna  "am  Hintern,  an der  Nase,  in  der  Höhe"  Y.5. 11  PUZ. (,  Yt/5.40)".
Vgl.  zu  Xivipiavant:  —  np.  !tb  'Unler-,  Hinter- teil'.—  ")  Abgerissenes  Zitat')  la  yim  ufairi vis  raula/  ärilyö^tariza  (sd.)  Hinler  harfhut fehlt  ein  Gen.;  vgl.  Yt.  5.  96.  Anders  DST. ZA.  3.  31.  —  ')  Das  die  NA.  zu  Yt  ig-  40 fälschlich  in  den  Text  aufgenommen  hat.
•  j.  xsvaewa-  1)  Adj.  'sich  rasch  schwin- gend,   schnellend':    azayS  "wänhS    "sich
I  rasch  (im  Bogen)  schnellende  Schlangen" V.  IÄ  65;  —  tistrlm  .  .  ys  avavai  °wl! vataite  .  .  ya^a  liyri/ . .  ",  .  der  ebenso
dby  Google
S6i
x&vaewayataäträ-
"xäviptyö
rasch  dahinfliegt,  . .  wie  der  Pfeil  .  ,"  Yt S.6.  2)   m.   'rascher   SchwuDg"    (dut
Komp.).
KompE.  —  Vgl  ta  xhiahiiayal.aSlrä:  —  Pü. :
iipäk  {wom  HB«.  PSt.  83).
•  j.  x^vaewayataäträ-  Adj.  (mask.  *ra-) 'der  die  Peitsche  kreisen  lässt,  schwingt': xsähra  . .  'ra  (APn.)  "Reiche,  wo  man die  Peitsche  schwingt"  Yt.5. 130.
PPA.,  aMt  *xivafwiiya-  Praes.  30  (Kaus.)  'in rasch  kreisende  Scbvringung  versetzen'.  — VgL  »bd.  nnfifan  usw.;  zuletzt  IF.  9.  ^^^.
•  j.  "xävaä')  indekl  Zw.  'sechs':  i^aitt  aäe tnthra  .  .t  xfi  (als  Nom.)  V.4.1;  9.34, i(7.9«;  —  a^  (als  Akk.)  x^aßt5  ■^,  4; V.  2.  30,  J.51,  7.1S,  p.ii,  32  PüZ.  (?}, /3.8,  14-i-A,  15-45.  ^7-6",  YL4.6,  F./, N.50,  *P.9,  Vd._9;  —  *j^  (als  Instr.) vayzibii'V.6y,i03;  —  xi^  sota  V.2.30, 4.12';  —  xs'  sa/äis'V.4.6,  ■^t.j.gs'».
KompA.;  Ableit.  —  aL  /ät  (Bthl.  ZDMG.jo. joil;  np.  ia/;  S  2'0.  —  Pü.:  &  —  O  Mehr- mall  xsianü  ^eichr.  —  >)  NA.  als  Komp.;  s. ■ach  V.  3.  38.
•  j.  *xSva8  Adv.  'sechsmal' :  W/  frasnä- ^ym  maismaaa  . .  %ri^  . .  ca%ru/.  .  x/°
V.7.7S;  7S',  IS*- VgL  'xhai.  —  Pu.:  6  Mr.
•  j.  x$va$.aSi-  Adj.  'mit  sechs  Augen': ailm  äahskim  ..  "hrikamsr^im  'sXm  Y.g.8.
Komp.  mil  AD.  am  Ende').  —  aX.  t^.dasam . .  jal/aifäiH  in'iJrtditara  RV,  10.  99-  6.  —  Pü. ; 6  OS.  —  ')  Nach  Mastern  wie  etwa  *kv-ali- •iii^%aX/c«(',  wo  der  Dual  berechtigt  war.
•  j.  xSva$.karäa-  n.  'durch  sechs  parallele Furchstriche  hergestellte  Abgrenzung":  •«. /raiJraya/i  Yt4.6.
VgL  hn'jhvia-.
•  j.  xiSvaä.gäya-  n.  'Längenausdehnung von  sechs  Schritten,  sechs  Schrittlängen': 'gäin  JhmJtffai/i  la%rusanqm'V,6.^i;AO.
Pü, :  6  gäm.
•  j.  xdvaS.xSapar-  n.  'Zeit  von  sechs Nächten,  d.  i.  Tagen  und  Nächten':  pasca 'Parst^^  "nach  Verlauf  von  sechs  Tagen und  Nächten"  V.ß.34.
Pi.:  >u  hol  6  iapak.   —  1)  Them.
•  j.  xävaStay-  fem.  Zw.  'sechzig':   °i auiS)ySis»mahe  (sd.)    tistryelie  da%usS    A. J.8.         3)  mit  Gen.  'tlm   ätn^aokanam V.Ä91;  J2.I-
Ableit  —  Ableit.  ans  'xivaj.  —  VgL  ai.  )a}!dy- U;  npw  iaiL  —  PQ,;  6b.
•  j,  x$va£ti'vant-  Adj.  'sechzigfach':  °vä
(nämL  asti  mi^rS)  antan  havisia  Yt  10. 6.
j.  xSvaS.dasa-  Adj.   'der   sechzehnte':
im  asanhqmca  .  .  vahisijm  V.J.  19;  — °sa  (statt  NSm.)   (nämL  yal  ahmt)  hata.-
armU  \t.  I.&.
```


## [2026-09-14T03:12:46.492Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"xSvi\\|xävi\\|xsvi\\|xhvi\\|x&vi\" BRT.txt | head -20"
}
```


### [2026-09-14T03:12:46.549Z] TOOL RESULT

```
5541:I  —  ya>a  vJspe  *anye  're  (NP.)  Yt.  5. 69 ;  — ?r?xsö  (sd.)  .  .  xsvivii.isvatfmS  'yanqm  Yt S.6;  —  'yanqm  ifaranS  Yt.lS.o,  Ny.5.5.
7542:•  j.,  g.  ä-zutay-  f.''  'Fett,  Schmalz':  raoy- nyqtn  i'aranhim  "suitlmca  urvaranqm  Yt. /2.3.  a)  überhaupt  sva.  'feste  Ndirung' gegenüber  der  flüssigen,  im  Gegensatz  zu ' xsi'td-  'Milch' :  pars  xsvisät  (sd.)  -zaitUca  "  1 girii mal  V.  13. z8;  — xhioaica  'sBlayaEca  ■> ^.68.2;  —  t!m  'iSdiis'''  ahurB  mq%r)m tasal  .  .  mazdä  gavei  xhildimcil  *ki'B.- umiaHbys  spmt3  säsnayä  "das  Wort  vom Fett  hat  AhM. ..  für  das  Rind  geschaffen und  die  Milch  für  die  Nahrung  begehren- den durch  sein  Gebot,  der  heilige"  Y. 29.71'.  a)  Du.  in  Verbindung  mit  xhild- Du.:  xsviöa  'zütH  yazamaide  .  .  ilzSis  .  . hamsistri  \.i6.8.  2)  'Üppigkeit,  strotzende Kraft  und  Fülle':  vaKuAlm  'zBülm*^  . . frasasttm  .  .   *p3r»ndlm  yazamaidl  Y.jS.
7635:•  j.  3r9x§a-  a  £N.  eines  berühmten iranischen  Schützen**:  tiyris  . . y'im  anhat °sS  xi-vitui-Uus  xsviwi.iivaiimd  airyanqm airyö^stii:at  haca  garSit  ^anvantain  avi gairim  "der  Pfeil  , .,  den  der  PfeilschUtze if.  schoss,  der  beste  Pfeilschütze  der  Arier, vom  Berg  A.  bis  zum  Berg  X<:"   Vt.ÄÖ.
8686:•  j.  u§-  n.  'Ohr'  uzw.  «^»rischer  Wesen'': k/(NS.)  F.9(?).  A)  sonst  nur  Du.;  a)  'die Ohren':  yezi  *kva£ibya  ''-sibya''^^  aiwi.- srunvaifi  . ,  yezi  äat  nöit  /ivagibya  "Hbya aiwi.surunvait(  N.  i'ö";  Uj;  —  *'sibya F.p'>*>;  —  drimts  .  .  asi  [-//Is)  karma gava  *dvari'^ra  zafan  Yt  jr.2;  —  pairi 'si  vSrayavw»m  kam  gava  nidanzaydmoMii Yt.  j.  27;  —  g?tirvaya  h?  päoave  züvar^ pairi  iS  'si  zvrpnäioi  sk)Hd?m  si  manS kirsnüioi  Y.9.28;  —  °//  ahuralu  mazda yazamaide  darp'^räi  (sd.)  maiirahe  .  . xratüm  .  .  mar>%räi  .  .  hisvqm  . .  fra^'äküi Yt. /.  28.  a)  von  Tieren;  °H  (näml. g>us)  pairi. dar ayänli  (sd.)  daSma  .  .  Vt. 14. 56.  b)  'Gehör*,  d.  i.  Fähigkeit  richtig zu  hören  und  zu  verstehen,  sva.  'Auf- fassungs-,  Verstandeskraft':  ava  pa'oS  ava zastS  ava  °/i  däraydiiwjm  .  .  däityanqm .  . syaoiinanqm  varpzäi  Vr.  75.  1;  —  d<lya ml . .  mastim  spilnö  xsviwrjm  (sd.)  hizi'qm uruiie  -si  xratBiH  .  .  Y.62.4.
10765:•  j.  xSadrö.cinah-  m.  EM.  eines  Gläubigen: 'nat?hs  * xSviwrSspanahe  (sd.)  afaons  YL 13.  iia.
10867:•  j-,  g.  xäusta-  Adj.  'Üüssig*,  spcz.  'brei- flüssig'; a)  vom  Lehm,  sva.  'aufgeweicht': yäiia  nü  ma/yska  *xsvisti  (LS.)  '>  zjtiiS (sd.)  vfsä2'ayänti  V,  3.  3i'>,  b)  vom Metall  (Eisen),  sva.  'geschmolzen',  mit ayah-  n.  Bezeichnung  des  glühenden  Me- tallstroms beim  letzten  Gericht^*:  yqrn xstiütim  rSf\Sibyä  (sd.)  dh  ^!ci,l  iJ^rJ suxrä  .  .  aya»Ää  °tä  Y.  j/,  9;  —  *'lpm^''
10950:"xäviptyö
10985:•  j.,  g.  xSvid-  m.  'Milch';  im  Gegensatz zu  axBtay-  (sd.)  überhaupt  'flüssige  Nah- rung' im  Gegensatz  zu  fester:  pars  °isca (NS.)  äsaitisca'^  gsui  mal  "hervor  (geholt werde)  Milch  und  Fett  samrat  Fleisch" V.13.2%;  —  ■ilaica  (DS.)  azStayalFa''> Y.ßS.ii  —  am  äiStBis(sd.)  aAurB mohnm tasat  .  .  gavSi  'lihmlä'''  * AvS urusalibyS V.  25,  7;  —  *mmdäidyäi  (sd.)  «ftfem^)  Y. 1/.9.  a)  Du.  in  Verbindung  mit  äsütay- Du.:  "röa  (AD.)  äzuiti  yazamaiäeY.iG.Z; zit.  *F,5.  a)  pasca  xsavaidlm  ayara- namca  (soll  heissen)  "nach  sechs*'  Tagen" Vd.5.
10987:•  j.  xSvipta'vant-  Adj.  (fem.  'vaitl-)  'mit Melkmilch,  gemolkener  Milch  versehen'": pamtavaiti  *vaiti  (VSf.)  V.  21.  7.
10989:1  j.  "xSviptyö  va  yyt.13. VgL  V.  31.  7,  wo  xSviftavaiti.
10995:•  j.  xSvtwi.i§av-  m.  Tfeilschiltze":  ir?xsd '^^  xsviwi.isvaUmB  airyanam  Yt  Ä6;  — •/ä«  parBMv^m  "den  ferntreffenden PfeilschUtzen"  Yl/o.ioz,  77.12.
10997:•  j.  x§viwt.i§va't«ma-  Adj.  'der  beste Pfeilschlitze':  jrsxsd  (sd.)  xsviwi.isus  'mS airyanam  Yt.S.6.
11000:•  j.  xSviwrra-  Adj.  'schnell,  flink,  ge- läufig': däya  me  . .  mastim  späiiB  'nm'^ kisvam  urune  usi  "gib  mir  . .  eine  flinke Zunge,  der  Seele  Auffassungskraft"  Y.  62.4.
11002:•  j.  *xSviwrä3pa-  m.  EN.  eines  Gläu- bigen; 'paht^'>  x^tavalnyehe  (sd.)  asaanä Yty. iii; — /rJnyä  (sd.)  näiryS  'J>aAc'^ Yt.  13.140.
11004:•  j.  ■''xäviwräspana- "'  patr.  Adj.  'von X^iwräspa  abstammend,  dessen  Nach- komme': xsa'irö.cinaahö  'nahe  as'aonöYt. 13-113.         [YtJ^.iiir  lies  'aspakt.]
11005:Ableit.  aus  txsviTufäspa:  —  H  So  Pt  1. xiöiwr'-,  s.  S  26S.  30,  IF.  9.  274.
14800:•  '].  paema'vant-  Adj.,  nur  fem.  'vaili- 'die  mit  Muttermilch  versehen  ist"h  °vaHi xsviptavaiH  (VSf.)  V.  21.  7.
20358:*  S-  (>  j)  '''ni^ndäidyäi,  man  . .  daidyäi Inf.  'im  Gedächtnis  zu  behalten,  eingedenk zu  bleiben';  *m>ndäidyai  yä  tut  mazdä SäiMi  "deiner  Willensmeinung  will  ich eingedenk  bleiben,  o  M"  y.44.8;  —  tat m0i  vJcidyäi  (sd.)  vaoüä  . .  vTduyi . .  t»Jnäl daidyai  Y.  Ji.  5;  —  yS  nS  alvS  at  ll  uyl '^rayöidyäi  türahe  *mmd3idyai  xSvidstn haptaidyai  nava  dasme  yei  vS  yae^ma  V. u.  9*>.
20359:*)  Ein  kabbalistisches  Gemengsel  aus  meist ^iSischen  Wörtern,  die  lum  guten  Teil  in andrer  als  der  ihnen  zukommenden  Bedeutung gebraucht  sind.  Vgl.  Sp.  Komm.  3.  134,  Dst. ZA.  /.  113,  Gdn.  KZ.  2/.  250,  Bthl.  IFAni. 6.  41,  IF.  lt.  139-  «i'id',  aus  Y.  44.  8  ge- nommen, soll  'ßnffach'  (od.  dgl.;  Pö.:  panj td  nn)  bedeuten,  s.  dazu  No.  I.  Entsprechende Bedeutung  ist  den  Wörtern  "yi,  %räy5idyäi, türahe,  xsvidim ,  hapläidyäi  beigelegt  (sd.),  die mit  den  Zahlwörtern  für  2,  3,  4,  6,  7,  8  in  Zu- sammenbang gebracht  worden  sind,  an  die  sie z.  T.  anklingen.
```


## [2026-09-14T03:13:00.715Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npdftoppm -f 489 -l 489 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf \"$PWD/scratch-pg489\" 2>&1; ls -la scratch-pg489.png"
}
```


## [2026-09-14T03:13:01.776Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD\nfor n in 55 56 57; do echo \"=== pdf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' FFD_pages.txt | head -40; done"
}
```


### [2026-09-14T03:13:02.521Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 76897 Sep 13 23:13 scratch-pg489.png
```


### [2026-09-14T03:13:03.581Z] TOOL RESULT

```
=== pdf 55
[pdf page 55]
وا فعلهای فارسی دری
خرامیدن
«خرامید» ماد ماضی جعلی است. از مادهٌ مضارع ساخته شده است.
: «خرام» < فارسی میانه 337370 < ایرانی باستان 3+737-8*. برای ۵ > آرای. 3
پیشوند فعلی است. ۳370 صورت بالاندةٌ ريشهٌ 77870 است و 77870(«گامبرداشتن» معنی
می‌دهد.
خریدن
خرید < فارسی میانه 7770 < ایرانی باستان 3۳7-1۵*. برای 14 -> آراست. 77 صورت
ضعیف 727 است و آن به معنی «خریدن» است.
خر + فارسی‌میانةٌ مانوی 37. 77 در فارسی‌میانهٌ مانوی و «خر» در فارسی دری‌به این
سبب به وجود آمده‌اند که تصور شده «خرید» مادهٌ ماضی جعلی است و با حذف ۲4مادة
مضارع به وجود می آید. مادةٌ مضارع 3374 در فارسی میانه 778 است» از ایرانی باستان
8 83 نشاته‌ای بوده که برای ساختن ماده مضارع از ريشه به کار می‌رفته است ->
بریدن,
خزیدن
«خزید» ماده ماضی جعلی است. از مادهٌ مضارع ساخته شده است.
خز < پهلوی اشکانی 382. فارسی میانهٌ مانوی 782 < ایرانی باستان ۶۵2-۵
3-2 برای 2 > آرای. 2 صورت افزوده و 7 صورت ضعیف ريشه هستند. 1817 به
معنی «خزیدن» است.
خست + فارسی‌میانه 3881 < ایرانی باستان 3۵9-1۵*. برای 18-> آراست. 740 صورت
اصلی 8 است. 4 پیش از 1به 8 بدل شده است. ريشةٌ 24 به معنی «پاره کردن» است.
خفت < فارسی میانه 911 < ایرانی باستان ۳۵۶-۵". برای 1۵ -> آراست. 1:۸0

=== pdf 56
[pdf page 56]
ماده‌های ماضی و مضارع فارسی دری --___شش ۵۱
صورت اصلی 3 است.» 0 پیش از ۲ به ۶ بدل شده است.
خواب < فارسی میانه 330: اسم است» در فارسی دری «خواب» به عنوان مادهٌ
مضارع «خفتن» به کار رفته است. ماده مضارع در فارسی میانه کته است.
بازماندهٌ ۹۷۵۵۵* ایرانی باستان. ۵۸:* ساخته شده است از ۸82 با بدل‌شدن 0 به ؟
پیش از 8 و 82 8 برای ساختن مادةٌ آغازی از ريشه به کار می‌رفته است. برای 2 آرای.
در فارسی دری از «خفس» که به صورتهای «خسپ» و «خسب» هم به کار رفته. مادهٌ
ماضی جعلی ساخته شده است: خفسید., خسپید, خسبید.
خندیدن
خندید < فارسی میانه ۰۵414 مادهٌ ماضی جعلی است. از ماده مضارع ساخته
شده است. َ
خند < فارسی میانه 75384 < ایرانی باستان ۰*۵4 380 در فارسی میانه و ایراتی
باستان» «خندیدن» معنی می‌دهد.
خواستن
خواست < فارسی میانه 7۳391« ایرانی باستان 9-1۵:*. برای اه آراست. 7۷36
صورت اصلی ۷38 است. 4 پیش از ۲ به 5 بدل شده است. ۷30 به معتی «خواستن»
است.
خواه + فارسی میانه ۳:5 < ایرانی باستان -۷۷24:*. برای ۵ -> آرای.
خواندن
خواند + فارسی میانه ۷384 < ایرانی باستان 1:۵۵-1۵*. برای 18 > آراست. ريشةٌ :
31 به معنی «بانگ کردن» است.
خوان < فارسی میانه ۷۸37 < ایرانی باستان -۳۷3:*. برای ۵ > آرای. 1۷۷3۵
صورت بالاندةٌ ۷۵2 است.

=== pdf 57
[pdf page 57]
فعلهای فارسی دری
خوردن
خورد + فارسی میانه ۷۵7۵4 + ایرانی باستان ۷۷۵۲-1۵*. برای 2 آراست.
: خور + فارسی میانه 5۷۵7 < ایرانی باستان ۴*3۵۲-۵. برای 8 -> آرای.
و 3۷/8۲ به معنی (خوردن» و «نوشیدن» هر دو به کار رفته‌اند.
خوشیدن
«خوشید» مادةٌ ماضی جعلی است. از مادهٌ مضارع ساخته شده است.
خوش « فارسی میانه 355 < ایرانی باستان 8۸۵05-8*. برای ۵ -> آرای. ريشةٌ 1205 به
معنی «خشک شدن» است.
واژةٌ «خشک» از ريشهٌ ۳203 گرفته شده است. صورت فارسی ميانةٌ آن 1031 است. از
ایرانی باستان 8۵5-2*. 1805 صورت ضعیف ريشه و 1۵ پسوند است.
دادن
داد < فارسی میانه 434 < ایرانی باستان 43-12*. برای "18 > آراست. ريشهٌ 45
به‌معنی «دادن» است. در ایرانی باستان دو ريشةٌ 48 وجود داشته است: ۱-به معنی
«دادن»» ۲- به معنی «نهادن». «نهادن» از 13 به معنی «نهادن)» آمده است. >
نهادن.
ده < فارسی میانه 42 < ایرانی باستان ۵4۵۵5". 4202 ماد مضاعف است از 43.
داشتن
داشت + فارسی میانه 4381. به جای 4381 باید 417۵ می آمد از 4۲-12* ایرانی باستان.
7 صورت ضعیف ريشةٌ 447 است. برای 1۵ -> آراست. 4351 به قیاس با 137 1351
به‌وجود آمده است.
دار < فارسی میانه 437 < ایرانی باستان 437-۵*. برای 2 -> آرای. 437 صورت بالانده
ريشهٌ 487 است. 447 به معنی «داشتن» است.
```


## [2026-09-14T03:13:15.090Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD\nawk 'BEGIN{RS=\"\\f\"} NR==56' FFD_pages_faseng.txt 2>/dev/null | head -40 || ls"
}
```


### [2026-09-14T03:13:16.081Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T03:13:17.830Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD; ls -la; "
}
```


### [2026-09-14T03:13:17.872Z] TOOL RESULT

```
total 1452
drwxrwxr-x  3 sfmqrb sfmqrb    4096 Sep  4 14:06 .
drwxrwxr-x 23 sfmqrb sfmqrb    4096 Sep  4 14:06 ..
-rw-rw-r--  1 sfmqrb sfmqrb 1301330 Sep  4 14:06 FFD_asmaneketab.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  170624 Sep  4 14:06 FFD_pages.txt
drwxrwxr-x  2 sfmqrb sfmqrb    4096 Sep  4 13:19 FFD_pages.txt.pages
```


## [2026-09-14T03:13:23.669Z] TOOL CALL #38: Bash

```json
{
 "command": "pdftoppm -f 56 -l 56 -r 200 -png -singlefile data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf \"$PWD/scratch-ffd51-489\" && python3 -c \"\nfrom PIL import Image\nim=Image.open('/home/sfmqrb/git/rishe/scratch-ffd51-489.png'); print(im.size)\nim.crop((0,int(im.size[1]*0.45),im.size[0],int(im.size[1]*0.80))).save('/home/sfmqrb/git/rishe/scratch-ffd51-489-crop.png')\n\""
}
```


### [2026-09-14T03:13:25.290Z] TOOL RESULT

```
(1136, 1705)
```


## [2026-09-14T03:13:27.895Z] TOOL CALL #39: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/scratch-ffd51-489-crop.png"
}
```


### [2026-09-14T03:13:27.914Z] TOOL RESULT

```

```


## [2026-09-14T03:13:35.745Z] TOOL CALL #40: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/scratch-pg489.png"
}
```


### [2026-09-14T03:13:36.339Z] TOOL RESULT

```

```


## [2026-09-14T03:13:36.335Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T03:13:59.869Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### AHD swad\"; grep -n -i \"swād-\\|swad-\\|swēid\\|sweid\" AHD_watkins1985.txt | head -20\necho \"### AHD sweep/swift\"; grep -n -i \"^swei\\|swei-\\|sweib\\|swip-\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-14T03:13:59.939Z] TOOL RESULT

```
### AHD swad
148:The names for a number of insects can be reconstructed in the protolanguage, includ- ing the wasP (wopsa), the hornet (*kras-ro-, a derivative of ker-', “head,” from the shape of the insect), and the fly (mu-2). The BEE (bhei-') was particularly important as the producer of honey, for which we have the common Indo-European name melit-. Honey was the only source of sugar and sweetness (swad-, “sweet,” is ancient), and notably was the base of the only certain Indo-European alcoholic beverage, MEAD, medhu-, meaning in different dialects both “mead” (“wine” in Greece) and “honey.” The Germanic lan- guages have innovated, perhaps from a taboo on speaking the name while gathering wild honey; the common Germanic English word HONEY is from an old color adjective for “yellow,” k(e)neko-.
1036:swad-. Sweet, pleasant. 1. Germanic *swdtja- in Old English swéte, sweet: SWEET. 2. Suffixed form *swdd-é- in Latin suddére, to advise, urge (< “recommend as good”): SUASION; (ASSUASIVE), DISSUADE, PERSUADE. 3. Suffixed form *swdd-w-i- in Latin sudvis, delightful: SOAVE, SUAVE; ASSUAGE. 4. Suffixed form *swdd-es- in Greek hédos, pleasure: AEDES. 5. Suffixed form *swdd- ond in Greek hédoné, pleasure: HEDONIC, HEDONISM. [Pok. suad- 1039.]
1043:swei-2. To bend, turn. 1. Germanic o-grade form *swaip- in Old English swdpan, to sweep, drive, swing: swoop. 2. Germanic zero-grade form *swip- in Old English swift, swift, quick (< “turning quickly”): swirtT. 3. Germanic full-grade form *swif- in Middle English swyvel, a swivel: SWIVEL. 4. Possibly Germanic *swih- in Middle Dutch swijch, bough, twig: SWITCH. 5. German schwappen, to flap, splash, akin to the source of Middle English swap- pen, to splash: swaP. [Pok. swei- 1041.] sweid-'. To shine. Possible suffixed form *sweid-es- in: a. Latin sidus, constellation, star: SIDEREAL; b. Latin augury terms considerdre, to examine, “observe the stars carefully” (con-, intensive prefix; see kom), and déside- rare, to long for, investigate (formed on analogy with considerdre; dé-, from; see de-): CONSIDER, DESIRE. [Pok. 1. sueid- 1042.] sweid-2. Sweat; to sweat. I.O-grade form *swoid-. 1. Germanic *swaitaz, sweat, with its denominative *swaitjan, to sweat, in Old English sw&tan, to sweat: SWEAT. 2. Suffixed form *swoid-os- in Latin sidor, sweat: SUDORIFIC; SUDORIFEROUS. 3. O-grade form *swoid-d- in Latin siddre, to sweat: SUDATORIUM, SUINT; EXUDE, TRANSUDE. II. Suffixed zero-grade form *swid-r-os- in Greek hidrds, sweat: HIDROSIS. [Pok. 2. sueid- 1043.]
1217:ADDER nétr- ADDICT deik- ADDUCE deuk- -ADELPHOUS gWelbh- ADEMPTION em- ADENO- engW- ADEPT ap-1 ADHERE ghais- ADIABATIC gWa- ADIEU delw- ADIT ei-1 ADJACENT yé- ADJECTIVE yé- ADJOIN yeug- ADJOURN deiw- ADJUDICATE yewes- ADJURE yewes- ADJUST yeug- ADJUVANT ad- ADMIRE smei- ADMIT (s)meit(9)- ADMIX meik- ADMONISH men-t ADNATE gene- ADNEXA ned- ADO ad- ADOLESCENT al-3 ADOPT op-2 ADORE Or- ADORN ar- ADRENERGIC werg- ADSCITITIOUS skei- ADSORB srebh- ADULT al-3 ADULTERATE al-1 ADULTERINE al-1 ADULTERY al-1 ADUMBRATE andho- ADUST eus- ADVANCE ant- ADVECTION wegh- ADVENT gWa- ADVENTITIOUS gWa- ADVENTURE gWa- ADVERB wer-6 ADVERSE wer-3 ADVICE weid- ADVISE weid- ADVOCATE wekw- AECIUM weik-3 AEDES swad-
1263:ASH? os- ASININE asinus ASK ais- ASPECT spek- ASPEN apsa ASPERSE (s)preg- ASPIRATE spirare Ass? ors- ASSAI? Sa- ASSAIL  sel-4 ASSAY ag- ASSEMBLE sem-! ASSENT sent- ASSERT ser-3 ASSESS sed-1 ASSET sa- ASSEVERATE weéro- assIDUOUS_ sed-1 ASSIGN sekw-1 ASSIMILATE sem-1 ASSIST sta- ASSOCIATE sekw-1 ASSOIL feu-1 ASSONANCE swen- ASSORT ser-3 ASSUAGE swad- ASSUASIVE swad- ASSUME em- ASSURE cira ASTASIA sta- ASTATINE  sta- ASTER  ster-3
1392:CONFOUND gheu- CONFRERE bhrater- CONFUSE gheu- CONFUTE bhau- CONGE mei-1 CONGEAL gel-3 CONGENER gene- CONGENIAL gene- CONGENITAL gene- CONGERIES gerere CONGEST gerere CONGLOBATE gel-1 CONGLOMERATE gel-1 CONGLUTINATE gel-1 CONGRATULATE gWera-3 CONGREGATE ger-! CONGRESS ghredh- CONGRUENT ghréu- CONIDIUM keni- CONIOSIS keni- CONJECTURE yé- CONJOIN yeug- CONJUGAL yeug- CONJUGATE yeug- CONJUNCT yeug- CONJURE yewes- CONNATE gene- CONNECT ned- CONNIVE kneig’h- CONNOISSEUR gn6- CONNOTE gné- CONNUBIAL sneubh- CONQUER quaerere CONQUIAN kom, kWo- CONSCIENCE skei- CONSCIOUS | skei- CONSCRIPT skribh- CONSECRATE sak- CONSENT sent- CONSEQUENT sekw-1 CONSERVE ser-1 CONSIDER sweid-1 CONSIGN sekw-1 CONSIST sta- CONSOCIATE sekw-1 CONSOLE! sel-2 CONSOLIDATE sol- CONSOLUTE leu-1 CONSONANT swen- CONSORT ser-3 CONSPICUOUS _ spek- CONSPIRE spirare CONSTABLE ei-1 CONSTANT sta- CONSTELLATION  ster-3 CONSTERNATE  ster-2 CONSTIPATE  steip- CONSTITUTE sta- CONSTRAIN | streig- CONSTRUCT  ster-2 CONSUETUDE s(w)e- CONSUME em- CONTACT tag- CONTAIN ten- CONTAMINATE tag- CONTEMPLATE tem- CONTEND ten- CONTEST trei- CONTEXT teks- CONTINUE ten- CONTORT terkw- CONTOUR tera-1 CONTRA- kom CONTRABAND bha-2 CONTRACT tragh- CONTRADICT deik- CONTRARY kom CONTRAST sta- CONTRAVENE gWa- CONTRITE tere-1 CONTRIVE trep-2 CONTROL ret- CONTROVERSY wer-3 CONTUSE (s)teu- CONVALESCE wal- CONVECTION wegh- CONVENE gWa- CONVENIENT gWa- CONVENT gWa- CONVENTICLE gWa- CONVENTION gWa- CONVERGE wer-3 CONVERSE! wer-3 CONVERT wer-3 CONVEX wegh- CONVEY wegh- CONVINCE weik-5 CONVIVIAL gWei- CONVOKE wekw-
1420:DEODAR deiw-, deru DEONTOLOGY deu-1 DEPEND (s)pen- DEPICT peig-1 DEPILATE pilo- DEPLOY plek- DEPLUME pleus- DEPONE apo- DEPOPULATE populus DEPORT per-2 DEPOSIT apo- DEPRECATE prek- DEPRECIATE per-6 DEPREDATE ghend- DEPRESS per-5 DEPRIVE pert DEPTH dheub- DEPURATE peue- DEPUTE peu- DERACINATE wrad- DERANGE sker-3 DERELICT leikw- DERIVE rei-3 -DERM der-2 DERMA! der-2 DERMA? tera-1 -DERMA der-2 DERMATO- der-2 DEROGATE reg-! DERRIS der-2 DESCANT kan- DESCEND skand- DESCRIBE skribh- DESERTS = ser-3 DESERVE servus DESICCATE selkw- DESIGNATE sekw-1 DESIRE sweid-1 DESIST sta- DESMID dé- DESOLATE s(w)e- DESPAIR spé-1 DESPICABLE spek- DESPISE spek- DESPOIL spel-! DESPOND spend- DESPOT deme-! DESTINE sta- DESTITUTE sta- DESTRIER deks- DESTROY ster-2 DESUETUDE s(w)e- DESULTORY sel-4 DETAIN  ten- DETECT (s)teg- DETENT ten- DETER tres- DETERIORATE de- DETERMINE ter- DETEST trei- DETONATE (s)tene- DETOUR tera-1 DETRACT tragh- DETRIMENT tera-1 DETUMESCENCE teue- DEUCE! dwo- DEUTERAGONIST deu-? DEUTERIUM deu-!
1429:DIN dhwen- DINGUS _{enk-1 DINOSAUR dwei- DINOTHERE dwei- DIOCESE weik-! DIOECIOUS weik-1 DIOICOUS_ weik-1 DIOPTER oOkW- Dioscuri_ deiw-, ker-3 pip dheub- DIPHTHERIA deph- DIPHYODONT bheue- DIPLO- dwo- DIPLOCARDIAC kerd-1 DIPLODOCUS dek-1 DIPLOE dwo- DIPLOID pel-3 DIPLOMA dwo- DIPNOAN pneu- DIRE dwei- DIRECT reg-! DIRNDL tek- DISARM ar- DISASTER ster-3 DISBURSE bursa DISCERN krei- DISCIPLE dek-! DISCIPLINE dek-? DISCOMFIT dhé-1 DISCORD kerd-1 DISCOURSE kers-2 DISCRIMINATE krel- DIscuss kwét- DISDAIN dek-1 DISEMBOGUE beu-! DISFIGURE dheigh- DISGUST geus- DISK deik- DISMAL deiw-, mel-5 DISMAY magh-! DISMISS (s)meit(9)- DISPARATE pere-1 DISPATCH ped-! DISPEL pel-6 DISPENSE (s)pen- DISPERSE (s)preg- DISPLAY plek- DISPOSE apo- DISPUTE peu- DISQUISITION quaerere DISRUPT reup- DISSECT sek- DISSEMINATE 6-1 DISSENT sent- DISSERTATE ser-3 DISSIDENT sed-1 DISSILIENT sel-4 DISSIPATE swep-2 DISSOCIATE sekw-1 DISSOLVE leu-! DISSONANT swen- DISSUADE swad- DISTANT sta- DISTEND ten- DISTICH steigh- DISTINGUISH _ steig- DISTORT terkw- DISTRACT tragh- DISTRAIN  streig- DISTURB twer-! DITCH dhigw- DITTO deik- DITTY deik- DIURETIC wers-2 DIURNAL deiw- DIVA deiw- DIVARICATE wa- DIVE dheub- DIVERGE wer-3 DIVERT wer-3 DIvEs_ deiw- DIVIDE weidh- DIVINE! deiw- DIVINE? deiw- DIVULSION wel-4 Dizzy dheu-!
1489:EXTRACT tragh- EXTREME eghs EXTROVERSION wer-3 EXTROVERT wer-3 EXTRUDE treud- EXUBERANT euedh- EXUBERATE euedh- EXUDE sweid-2 EXULT sel-4 EXUVIAE eu-! EYAS nizdo-
1585:HEDGE kagh- HEDONIC swad- HEDONISM swad- -HEDRON sed-1 HEED kadh-
1605:HIDE! (s)keu- HIDE? (s)keu- HIDE? kei-1 HIDROSIS sweid-2 HIE kigh- HIEMAL = ghei-2 HIERARCH eis-! HIERARCHY eis-! HIERATIC  eis-1 HIERO- eis-1
2081:PERQUISITE quaerere PERSE s(w)e- PERSECUTE sekw-1 PERSEVERE wéro- PERSIFLAGE swei-! PERSIST sta- PERSPECTIVE spek- PERSPIRE spirare PERSUADE swad- PERT wer-5 PERTAIN ten- PERTINACIOUS ten- PERTURB twer-1 PERVADE wadh-2 PERVERT wer-3 PERVIOUS wegh- PES ped-!
2255:SIDE sé-2 SIDEREAL sweid-1 SIEGE sed-1 SIEGFRIED pri-, segh- SIEROZEM dhghem- SIEVE seib-
2273:SNIFF snu- SNIP snu- SNIVEL snu- SNOOP snu- SNORE sner- SNORKEL sner- SNORT sner- SNOT snu- SNOUT snu- SNOW sneig’h- SNUB snu- SNUFF! snu- SNUFFLE snu- SNUG! kes-1 sO swo- SOAK seua-2 sOAP_ seib- SOAVE swad- SOBER s(w)e- SOCIABLE sekw-1 SOCIAL sekw-1 SOCIETY sekw-1 SOCIO- sekw-1 SOCKET sU- SODALITY s(w)e- SODDEN seut- SOIL! sed-1 som? si- SOIREE sé@-2 SOJOURN deiw- SOKE sag- sol’ sawel-
2323:sTuD2 sta- STUDENT (s)teu- sTUDY (s)teu- STULTIFY _ stel- sTUM stam- STUMBLE stam- STUMP stebh- STUN (s)tena- STUPA steu(@)- STUPE steu(9)- STUPEFY (s)teu- STUPENDOUS (s)teu- STUPID (s)teu- STURDY trozdo- STUTTER (s)teu- stTy2  steigh- STYLITE sta- STYLOBATE gWa-, sta- STYPTIC steu(@)- Styx (s)teu- SUASION swad- SUAVE swad- SUB- upo SUBALTERN al-1 SUBAUDITION au-5 SUBDUCTION deuk- SUBDUE deuk- SUBITO ei-! SUBJACENT yé- SUBJECT yé- SUBJOIN yeug- SUBJUGATE yeug- SUBLUNARY leuk- SUBMERGE mezg-! SUBMIT (s)meit(9)- SUBORDINATE ar- SUBORN ar- SUBPOENA kwei-1 SUBREPTION rép-1 SUBROGATE reg-1 SUBSCRIBE skribh- SUBSEQUENT sekw-1 SUBSIDE sed-1 SUBSIDY sed-1 sUBSIST sta- SUBSTANCE sta- SUBSTITUTE sta- SUBSTRATUM ster-2 SUBSTRUCTION | ster-2 SUBSUME em- SUBTEND ten- SUBTERFUGE bheug-', upo SUBTERRANEAN ters- SUBTLE teks- SUBTRACT tragh- SUBULATE syU- SUBVENTION gWa- SUBVERT wer-3 SUCCEED ked- succincT kenk-1 succor kers-2 succuBUS keu-2 SUCCULENT seud-2 SUCCUMB keu-2 SUCCUSSION kwét- SUCH swo-
2324:SUCK seue-2 SUCTION seue-2 SUCTORIAL seue-2 SUDATORIUM sweid-2 SUDDEN ei-1 SUDORIFEROUS sweid-2 SUDORIFIC sweid-2 suDs_ seut-
2325:SUE sekw-1 SUFFER bher-1 SUFFICE dhé-1 SUFFICIENT dhé-1 SUFFIX dhig’- SUFFRAGAN bhreg- SUFFRAGE bhreg- SUFFUSE gheu- SUGGEST gerere SUICIDE s(w)e- SUINT sweid-2 SUITOR sekw-1 SULCATE selk- SULCUS selk- SULLEN s(w)e- SULTRY swel-2 SUM uper SUMMER! sem-2 SUMMIT uper
2328:SURE cilra, s(w)e- SURFACE dhé-1 SURFEIT dhé-1 SURGE reg-! SURGEON ghesor- SURGERY ghesor-, werg- SURLY sen-1 SURMISE (s)meit(9)- SURMULLET mel-2, saus- SURPLICE pel-4 SURPLUS pele-' SURPRISE ghend- SURRENDER d6- SURREPTITIOUS rep- SURROUND wed-! SURVEILLANT weg-2 SURVEY weid- SURVIVE gWei- SUSCEPTIBLE kap- SUSPECT spek- SUSPEND (s)pen- SUSPIRE spirare SUSTAIN ten- SUSURRATION swer-2 SUTLER seut- SUTRA syil- SUTTEE e@8- SUTURE syu- SVELTE wel-4 SWAB swep-2 SWAG sweng(W)- SWAIN s(w)e- SWALE swel-2 SWALLOW! swel-1 SWAMI s(w)e- SWAMP swombho- SWAN swen- SWANK sweng(w)- swaP swei-2 SWARF swerbh- SWARM swer-2 SWART swordo- SWASTIKA @S-, SU- SWEAR swer-1 SWEAT sweid-2 SWEET swad- SWELTER swel-2 SWERVE swerbh- SWIFT swei-2 SWILL swel-!
2402:TRANSIENT ei-1, tera-2 TRANSIT ei-1 TRANSITIVE ei-1 TRANSLATE tele- TRANSLITERATE deph- TRANSLUCENT leuk- TRANSMIT (s)meit(@)- TRANSMUTE mei-1 TRANSOM tere-2 TRANSPIRE § spirare TRANSPONTINE pent- TRANSPORT per-2 TRANSUDE sweid-2 TRANSVERSE wer-3 TRAP! der-1
### AHD sweep/swift
1040:swei-'
1041:IDIO-, IDIOM, IDIOT; IDIOMORPHIC, IDIOPATHY, IDIOSYN- CRASY. 11. Variant form *swei- in Irish féin, self: SINN FEIN. [Pok. se- 882.]
1042:swei-'. To whistle, hiss. Imitative root. Latin sibildre, to whistle at, hiss down: SIBILATE; CHUFA, PERSIFLAGE. [Pok. swei- 1040.]
1043:swei-2. To bend, turn. 1. Germanic o-grade form *swaip- in Old English swdpan, to sweep, drive, swing: swoop. 2. Germanic zero-grade form *swip- in Old English swift, swift, quick (< “turning quickly”): swirtT. 3. Germanic full-grade form *swif- in Middle English swyvel, a swivel: SWIVEL. 4. Possibly Germanic *swih- in Middle Dutch swijch, bough, twig: SWITCH. 5. German schwappen, to flap, splash, akin to the source of Middle English swap- pen, to splash: swaP. [Pok. swei- 1041.] sweid-'. To shine. Possible suffixed form *sweid-es- in: a. Latin sidus, constellation, star: SIDEREAL; b. Latin augury terms considerdre, to examine, “observe the stars carefully” (con-, intensive prefix; see kom), and déside- rare, to long for, investigate (formed on analogy with considerdre; dé-, from; see de-): CONSIDER, DESIRE. [Pok. 1. sueid- 1042.] sweid-2. Sweat; to sweat. I.O-grade form *swoid-. 1. Germanic *swaitaz, sweat, with its denominative *swaitjan, to sweat, in Old English sw&tan, to sweat: SWEAT. 2. Suffixed form *swoid-os- in Latin sidor, sweat: SUDORIFIC; SUDORIFEROUS. 3. O-grade form *swoid-d- in Latin siddre, to sweat: SUDATORIUM, SUINT; EXUDE, TRANSUDE. II. Suffixed zero-grade form *swid-r-os- in Greek hidrds, sweat: HIDROSIS. [Pok. 2. sueid- 1043.]
1357:CHOLE- ghel-2 CHOLER ghel-2 CHOLERA ghel-2 CHOLESTEROL ster-1 CHOLINERGIC werg- CHOLLA g(e)u-lo- CHONDRO- ghrendh- CHONDROMALACIA mel-1 CHOOSE geus- CHORAGUS_§ ag-, gher-1 CHORAL gher-1 CHORALE gher-1 CHORD? ghere- -CHORE ghé- CHORIC gher-1 CHORION ghere- CHORISTER gher-! CHOROGRAPHY ghé- CHORUS gher-1 CHOWDER kele-1 CHRESARD gher-5 CHRESTOMATHY gher-5, mendh-1 CHRISM ghréi- Curist ghréi- CHRISTEN ghréi- CHRISTIAN ghréi- CuRIsTMas ghréi- CHROMA ghréu- CHROMATIC ghréu- CHROMATO- ghréu- -CHROME ghréu- CHROMIUM ghréu- CHROMO- ghréu- CHROMONEMA (s)né- CHRONAXY ag- CHRYSANTHEMUM § andh- CHTHONIC dhghem- CHUFA swei-! CHUKAR kau-! CHUKKER kwel-1 CHURCH keue-? CHURL karlaz CHUTE kad-
2081:PERQUISITE quaerere PERSE s(w)e- PERSECUTE sekw-1 PERSEVERE wéro- PERSIFLAGE swei-! PERSIST sta- PERSPECTIVE spek- PERSPIRE spirare PERSUADE swad- PERT wer-5 PERTAIN ten- PERTINACIOUS ten- PERTURB twer-1 PERVADE wadh-2 PERVERT wer-3 PERVIOUS wegh- PES ped-!
2254:SHRED skreu- SHREW skreu- SHREWD skreu- SHRIKE ker-2 SHRIMP skerbh- SHRINK sker-3 SHRIVE skribh- SHROUD skreu- SHRUB! sker-1 SHTETL sta- SHTICK (s)teu- SHUDDER skut- SHUFFLE skeubh- SHUT skeud- SHUTTLE skeud- SIALADENITIS eng’- SIB s(w)e- SIBILATE swei-1 sic! so- SICCATIVE seikw- SICKLE _sek-
2328:SURE cilra, s(w)e- SURFACE dhé-1 SURFEIT dhé-1 SURGE reg-! SURGEON ghesor- SURGERY ghesor-, werg- SURLY sen-1 SURMISE (s)meit(9)- SURMULLET mel-2, saus- SURPLICE pel-4 SURPLUS pele-' SURPRISE ghend- SURRENDER d6- SURREPTITIOUS rep- SURROUND wed-! SURVEILLANT weg-2 SURVEY weid- SURVIVE gWei- SUSCEPTIBLE kap- SUSPECT spek- SUSPEND (s)pen- SUSPIRE spirare SUSTAIN ten- SUSURRATION swer-2 SUTLER seut- SUTRA syil- SUTTEE e@8- SUTURE syu- SVELTE wel-4 SWAB swep-2 SWAG sweng(W)- SWAIN s(w)e- SWALE swel-2 SWALLOW! swel-1 SWAMI s(w)e- SWAMP swombho- SWAN swen- SWANK sweng(w)- swaP swei-2 SWARF swerbh- SWARM swer-2 SWART swordo- SWASTIKA @S-, SU- SWEAR swer-1 SWEAT sweid-2 SWEET swad- SWELTER swel-2 SWERVE swerbh- SWIFT swei-2 SWILL swel-!
2331:SWING sweng(w)- SWINGE sweng(w)- SWINGLETREE sweng(w)- SWIRL swer-2 SWITCH swei-2 SWIVEL swei-2 swoop swei-2 SWORD swer-4 SYCAMORE moro- SYCOPHANT bha-! SYLLABLE (s)lag’- SYLLEPSIS (s)lag¥- SYLLOGISM leg-1 SYMBIOSIS gWei- SYMBOL gvele-1 SYMPATHY kWent(h)- SYMPATRIC peter- SYMPHONY bha-2 SYMPHYSIS bheue- SYMPODIUM ped-! SYMPOSIUM pd@(i)- SYMPTOM pet- SYN- ksun SYNAGOGUE ag- SYNALEPHA leip-
```


## [2026-09-14T03:14:01.340Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### KLN sweet\"; grep -n \"^sweet,\" KLN_1966.txt | head; echo \"### KLN persuade\"; grep -n \"^persuade,\" KLN_1966.txt | head\necho \"### KLN sweep/swift\"; grep -n \"^sweep,\\|^swift,\\|^swap,\\|^sway,\\|^swivel,\" KLN_1966.txt | head"
}
```


### [2026-09-14T03:14:01.432Z] TOOL RESULT

```
### KLN sweet
### KLN persuade
28308:persuade,  tr.  v.,  —  F.  persuader,  fr.  L.  persuadere, ‘to  persuade,  convince’,  fr.  per-  and  suadere,  ‘to advise'.  See  suave.
### KLN sweep/swift
37704:sweep,  intr.  and  tr.  v.  —  ME.  swepen,  ‘to  sweep, move  quickly’,  rel.  to  OE.  swapan,  'to  swoop’
37709:sweep,  n.  —  ME.  swepe,  fr.  swepen,  ‘to  sweep’.
37731:swift,  n.,  swift-moving  bird,  or  insect  or  object. —  Fr.  swift,  adj.
37757:swivel,  n.  —  ME.  swivell,  rel.  to  OE.  swifan,  ‘to move  in  a  course,  sweep'.  See  sweep,  v.,  and  cp. words  there  referred  to.
```


## [2026-09-14T03:14:17.648Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### KLN sweet\"; grep -n \"sweet,  adj\\|sweet, adj\" KLN_1966.txt | head; grep -n \"swōtja\\|swotja\\|swōtjaz\" KLN_1966.txt | head\necho \"### KLN suave\"; grep -n \"^suave,\" KLN_1966.txt | head\necho \"### IEC swad\"; grep -n \"swād\\|swad-\\|swādus\\|swadus\" IEC.txt | head -10"
}
```


### [2026-09-14T03:14:17.861Z] TOOL RESULT

```
### KLN sweet
37711:Derivative:  sweep-y,  adj. sweepstake(s),  n.  —  The  word  prop,  means ‘ sweeping  up  (i.e.  winning)  the  stakes'. sweet,  adj.  —  ME.  swete,  swote,  fr.  OE.  swete,
### KLN suave
37190:suave,  adj.,  smoothly  polite,  bland,  gracious.  — MF.  ( =  F.),  fr.  L.  suavis,  ‘sweet,  pleasant,  agree¬ able’,  which  stands  for  *swadwis,  and  is  cogn. with  OI.  svadub,  ‘sweet’,  Gk.  tljSik  (Dor.  aSu;), ‘sweet,  pleasant,  agreeable’,  r;8ovr),  ‘pleasure’, OS.  swoti,  OE.  swete,  ‘sweet’.  See  sweet  and  cp. soave.
### IEC swad
```


## [2026-09-14T03:14:19.899Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### WLD Bd2 suad\"; grep -n \"suādús\\|suād\\|sṷād\" incoming/WLD/WLD_Bd2_pages.txt | head -10\necho \"### WLD Bd2 sueib\"; grep -n \"sṷeib\\|sueib\\|xšvaēwa\\|xsvaewa\" incoming/WLD/WLD_Bd2_pages.txt | head -10"
}
```


### [2026-09-14T03:14:19.980Z] TOOL RESULT

```
### WLD Bd2 suad
### WLD Bd2 sueib
34578:     sueib-:     midjasweipains „Sintflut‘' (eig. Fegung der Mitte"): aisl.
```


## [2026-09-14T03:14:24.034Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\nawk 'BEGIN{RS=\"\\f\"} /midjasweipains/ {match($0,/\\[pdf page [0-9]+\\]/); print substr($0,RSTART,RLENGTH); print}' WLD_Bd2_pages.txt | head -60"
}
```


### [2026-09-14T03:14:25.044Z] TOOL RESULT

```
520                                              sueid-


     Noreen Ltl. 150, Zupitza Gut. 94.
     sueip: aisl. m/’a „schwiiigen, drehen, umherschweifen, schweben'', ags.
swifan jjbewegen, fegen, umherschweifen'^ (engl. swift „schnell") afris. sxmfa
„schwenken“, aisl. sueifla „8chwingen“, mhd. stvibeln^ stvivelen „taumeln“,
ahd. siveibon „schwebeii, schwingen'' (==^tveib6n, s. ^ueip-), sweben „schweben‘'.
   Lett. (Endzelin KZ. 44, 64) svaiplt „peitschen'', svipaste, svipstis „Hasen-
fu6, Windbeutel, Zierbengel".
     sueib-:     midjasweipains „Sintflut‘' (eig. Fegung der Mitte"): aisl.
                   got.
siieipa           schleudern, umhulleii“, ags. svapan „schwmgen, fegen,
           „werfen,
streichen (vom Winde)", as. sw€2^ jjfegte fort", ahd. siveifan „schwmgen,
in drehende Bewegung setzen, sich schlangeln", ahd. sweif „Umschwung,
Schwanz" = aisl. sveipr „umschlingendes Band, Schlingung, gekrauseltes
Haar", aisl. svipa „Peitsche" (usw., s. Pick 111^ 555, Falk-Torp u. sv0be^
sveiv, wo auch iiber ahnliche Worte mit ^f-Yokalismus);
   ay. xsaewayat-astra- „die Peitsche schwingend" u. dgl. (s. u. ueip-),
   Ygl. im allgem. Persson Wzerw. 192 f, Beitr. 934 f.. Pick III^, 553 ff.                           —
Wie weit die Ausbildung dieser Gruppen in Wechselwirkung mit den
Gruppen uei-^         -p-, -6- „biegen usw." erfolgte, entzieht sich noch
genauerer Beurteilung; iiber den problematischen Yersuch, die Formen
mit n und sn und solche mit ks- unter idg. qsn oder squ- zu vereinigen,
s. u.   ueip-.


1.   sueid- „glanzen, schimmern".
  Av. x'^aena- „gluhend, lohend" (Trautmann Grm. Ltges. 15; braucht aber
nicht auf eine kiirzere Wzf. snei- bezogen zu werden, sondern aus *x^aed-
na-);     lat.   sldiis^   -eris „Gestirn“, constderare „betrachten“,                  deslderare „ver-
langen" (zur Bed.-Yermittlung mit sldus s. Yf. LEWb.^ unter consldero,
neuerdings Persson Beitr. 366 fiP., wogegen wieder Hartmann GL 6, 334, 344);
lat. siidtis „trocken, heiter (vom Wetter)", sudtim „der klare Himmelsraum,

heiteres Wetter" {f^siApido-s, -m; Palk-Torp u. svide; bisher mit ^sam-
„trocken, diirr" verknupft);
     alit. svidtis      „blank,   glanzend", svidu^        ~eti   „glanzen",     lett. svtshi^   svtdif,
svtst „anbrechen,          vom Tage", lett. svdidU „salben“ (eig. „glanzen machen")
z.   B. Yf. LEWb.^ s. V.
     Aber ags. sweo-tol           „offenbar,   deutlich,     klar"     s.   u. *dei’   „hell glanzen".
Nasaliert        ai.   gvindate (Dhatup.) „glanzt,  wohl fiir *sivwdate nach
                                                          ist weiS",

Qvetd-h usw. (Meillet Et. 179; s. kneit-)] aber iiber gr. tvddXXopai und ir.
find, cymr. givynn „wei6" s. u. wid- „sehen"; auch die Deutung von got.
tvintnis, ahd. Wintar „Winter" als „der Weise" (Kluge® s. v., IJhlenbecks
PBRB. 30, 326) verdient nicht den Yorzug vor der Yerb. m. lat. unda
usw. als „nasse Jahreszeit" (s. Falk-Torp u. vintet')] eine Wzf. ohne anl. 5-
ist demnach nicht nachgewiesen.

  Ein ahnliches '^sueit-', aber in der Bed. „sengen, brennen" in aisl. svTda^
sveid „sengen, brennen",     ahd. sivtdan „brennen"; dazu wohl als Aorist-
praesens ahd. swedan „langsam schwelend verbrennen" und mit Ablaut-
entgleisung (z. B. Ehrlich KZ. 41, 293 f.) mhd. swadsm „Rauchschwaden,
Dunst u. dgl. (verschiedene Erwagungen z. B. bei Charpentier KZ. 40,427f.,
Petersson LXJA. 1915, 42f,               s.   auch   u.   uendh- „d6rreii“).           AuBerhalb des
```


## [2026-09-14T03:14:32.846Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\ngrep -n \"suād-\\|suad- \\|svādati\\|suadere\\|suadeo\" WLD_Bd2_pages.txt | head -10\necho \"=== try page\"; awk 'BEGIN{RS=\"\\f\"} /schmackhaft/ && /x.asta|x\\^asta|svad/ {match($0,/\\[pdf page [0-9]+\\]/); print substr($0,RSTART,RLENGTH); print substr($0,1,1500)}' WLD_Bd2_pages.txt | head -60"
}
```


### [2026-09-14T03:14:33.774Z] TOOL RESULT

```
34040:Hiramel^, vgl. ai. sii-diva- „sch6ner Tag^'; oder zu ^suad- „su6‘‘??); aksl.
=== try page

    "^suaq^-iO-    (im Akzent allerdings gegen das Slav, konti’astierend) zu
    unterstiitzt        durch die labiale Umgebung, anzunebmen;                                                   wui'de, da
    das Lokr. f on erhaltenes jo- zeigt, wohl friihzeitig dissimilatorisch (gegen
    das ji) zu 0:770^.
       S. Wiedemann      EB. 29, 31 Iff. (wo wie bei Boisacq und Yf. LEWb.^ 752
    Lit. iiber   andere Deutungen von onog^ das gewiB nicbt zu Ctp- „Wasser,
    Plu6“). Nicbt annebmbar ist mir aber Anreihung von lat. sums j,Saft“
    (aucb scbon bei J. Scbmidt PL 205; abnlieb Trautmann GGA. 1911, 250:
    angeblicb                                  aucb lat. Umbildung eines ^‘snag^los
    nacb sugo vertrete icb nicbt; vielmebr von Anfang an zu seuq-^ seug- „saugen,
    Saft“), desgleicben von lat. sanguis fs. u, es-rgV,-)  da 6 gr. uTzalog „weicb,  ;



    sanft‘' (Pedersen KZ. 36, 2S5 zw.) eigen tlicb „saftig’‘ gewesen sei, ist un-
    erweislicb (andere Deutungsversucbe bei Boisacq s. v.) isl. saggi m. ^Feucb-              ;


    tigkeit‘‘, ags. secg, gar-secg ,,Meer“ (Pick 111^ 426 zw., Falk-Torp u. sagle)
    bleiben fern.
      DaB idg. suaq][os eine Erw. von sen- „SafL* sei (Persson Wzerw. 8 f., 176,
    215 f. Anm. 2, Trautmann aaO.), ist, da nur auf die Anlautgruppe aufge-
    baut, bocbst fraglicli ein unbefriedigender, anderer Ankniipfungsvers aucb
                                            ;



    bei Osthoff IF. 4, 283 f.


    

           ;




                                              suarcl-   — suei-, sui-                              517

„Salz“ (Mittelbegriff „Wurze‘‘, Ygl. auSer dem unter "^sal „Salz“ bemerkten
noch  lit. sadyti „wurzen, salzen“ und gr. fjdog .n, „Essig'‘, ^doojua auch
„Wiirze, Pikantes“,                ^^dvvtTjgeg „Salz“,         Fick KZ. 22, 196, Fraenkel KZ. 42,
234);
   Kaus. bzw. Intensivum svadai/ati (= lat. suddeo^ s, u.) und svaddyati
„schmackbaft, geniefibar, annehmbar machen; kosten, genie6en“, tiefstufig
sUdayati          einrichten, zurecht bringen, gut machen, auch fertigmachen
=  toten, vernichten^‘ (mit derselben Ablautstufe Pf. susUdimd^ suda-li
„Koch‘‘,       lit.   sudyti^ got, suts^       s.    o.);
     mit d (wahrscheinlich aus betontem 9): svddati „macht schmackhaft, an-
genehm, wurzt“, svddate ,,schmeckt, ist schmackhaft^', Ptc. svattd - nasaliert             ;


av. x^andra-kara- „angenehmes tuend = gefallig", afgh. x^and „Wohlge-
schmack, Yergniigen" (machen auch fiir gr. dvbdvo9 hereits ursprachliches
Alter der Nasalierung wahrscheinlich, Bartholomae IF. 7, 95).
   Grr. fjdoixat (s. o.); dojuavog in der vorwiegenden Bed. „erfreut" wohl nach

J. Schmidt KZ. 27, 320 hieher als Ptc. zum s-Aorist fjoaro; der Lenis iiber-
nommen von dojusvog ,.gerettet, geborgen", das als "^ns-s-fnenos (Wacker-
```


## [2026-09-14T03:14:41.687Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\nawk 'BEGIN{RS=\"\\f\"} /x\\^andra-kara/ {match($0,/\\[pdf page [0-9]+\\]/); print substr($0,RSTART,RLENGTH)}' WLD_Bd2_pages.txt\nawk 'BEGIN{RS=\"\\f\"} /midjasweipains/ {match($0,/\\[pdf page [0-9]+\\]/); print \"sueib:\",substr($0,RSTART,RLENGTH)}' WLD_Bd2_pages.txt\necho \"=== search xvasto in WLD\"; grep -n \"Kochen schmackhaft\\|x\\^asto\\|x\\^astO\" WLD_Bd2_pages.txt | head"
}
```


### [2026-09-14T03:14:42.787Z] TOOL RESULT

```
sueib: 
=== search xvasto in WLD
```


## [2026-09-14T03:14:49.207Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -A4 \"^شیوا\" MON_part1.txt MON_part2.txt | head -40\necho \"=== خوست headword\"; grep -n -A4 \"^خوست\\|^خُست\\|خوست:\" MON_part1.txt MON_part2.txt | head -20"
}
```


### [2026-09-14T03:14:49.312Z] TOOL RESULT

```
MON_part1.txt:88347:شیوا 3 (ص .) فصیح» بلیغ. 
MON_part1.txt:88348:شیوانیدن: 31-227 (مص م 0( آمیختن» 
MON_part1.txt-88349-بر زد (عتوهاا: آرد گندم و مانند آن را 
MON_part1.txt-88350-در آب و امثال وی آمیختن (خصوصا). 
MON_part1.txt-88351-لرزانیدن. 
MON_part1.txt-88352-شیوشه: (30532)0 [- شوشه] (.) شوشه 
=== خوست headword
MON_part2.txt:6015:خوست ] (ص‌مف.) کوفته» پایمال شده. 
MON_part2.txt-6016-فرخشه: (5:)0:] |- فرخشته ] (.) نوعی 
MON_part2.txt-6017-شیرینی که آن را با آرده شکر: روغن و مغز 
MON_part2.txt-6018-بادام سازند» قطائف؛ لو ز بنه. 
MON_part2.txt-6019-
MON_part1.txt:70010:زادخوست: ۱:.50- زادهدخسواست | 
MON_part1.txt-70011-(ص‌مف.) پیر. سالخورده. فر توت. ضعیف و 
MON_part1.txt-70012-ناتوان. 
MON_part1.txt-70013-
MON_part1.txt-70014-زادمرد: 7-01 [1< آزادمر د| (امر .) آزاد
```


## [2026-09-14T03:14:54.531Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== part2 6005-6020\"; sed -n '6005,6020p' MON_part2.txt\necho \"=== part1 88335,88350\"; sed -n '88335,88350p' MON_part1.txt"
}
```


### [2026-09-14T03:14:54.611Z] TOOL RESULT

```
=== part2 6005-6020
میمون. مطرب؛ توازنده و سازنده. (کگیا.) 
خجسته. گل هميشه بهار. 

فرنسحی: ۳۹۹ (حامص.) زرشتی» 
تا مشک اه تناس نی 
سستی. ناتوانی. 

فرخراد: 01-] | - فرحزاده | (ص‌ مف.) 
آنکه به طالع میمون متولد شده مبا رک زاد. 
فشرخسته: (۵-)۲۵۱۸:] (یای خسته 
خوست ] (ص‌مف.) کوفته» پایمال شده. 
فرخشه: (5:)0:] |- فرخشته ] (.) نوعی 
شیرینی که آن را با آرده شکر: روغن و مغز 
بادام سازند» قطائف؛ لو ز بنه. 

فرخفال: ۸۲۲۵ [ف. ۳3 (ص‌مر.) 
=== part1 88335,88350
آلی: (شیم.) مبحث ترکیباتی است که بدن 
گباهان و جانوران را تشکیل داده‌اند و چون 
در سوختن این اجسام اگر اکسیژن به اندازة 
کافی نباشد مقداری کربن باقی می‌ماند» اين 
بخش از شیمی را شیمی ترکیبات کربن 
می‌نامند. .. 
شیمی دان: «05-. [فر. ف - شیمی داننده] 
(ص‌فا.) آنکه علم شیمی داند. 
شیمیست: اءأحلذ (1.) شیمیدان» آنکه علم 
شیمی داند» کیمیادان» کیمیاوی. 
شین: («5)«* (ع.] (.) زشتی 
زین. 
شیوا 3 (ص .) فصیح» بلیغ. 
شیوانیدن: 31-227 (مص م 0( آمیختن» 
بر زد (عتوهاا: آرد گندم و مانند آن را 
در آب و امثال وی آمیختن (خصوصا).
```


## [2026-09-14T03:15:12.632Z] TOOL CALL #50: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-14T03:15:12.639Z] TOOL RESULT

```


```


## [2026-09-14T03:15:17.195Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%A7%D8%B3%D8%AA%D9%86",
 "prompt": "Give the full Persian etymology section for خواستن (xâstan) 'to want': Middle Persian form, Proto-Iranian/Proto-Indo-Iranian reconstruction, PIE root, and any cognates or cited authorities (Cheung, Hasandust, MacKenzie)."
}
```


## [2026-09-14T03:15:18.745Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/sweet",
 "prompt": "Give the etymology of 'sweet': Old English swete, Proto-Germanic form, PIE root, and cognates (Latin suavis, suadere, Sanskrit svadus, Greek hedys)."
}
```


### [2026-09-14T03:15:23.551Z] TOOL RESULT

```
# Etymology of "Sweet"

## Origin Path

The word "sweet" traces back through several linguistic layers:

**Old English:** From Old English *swete*, the Mercian form *swoete*, meaning "pleasing to the senses, mind or feelings; having a pleasant disposition."

**Proto-Germanic:** These forms derive from Proto-Germanic *\*swotja-*, which also produced cognates in Old Saxon, Old Frisian, Swedish, Danish, Dutch, and German.

**Indo-European Root:** The ultimate source is the PIE root *\*swād-*, meaning "sweet, pleasant."

## Key Cognates

The entry identifies several related words across Indo-European languages:
- **Latin:** *suavis* ("pleasant") and *suadere* ("to advise," literally "to make something pleasant to")
- **Sanskrit:** *svadus* ("sweet")
- **Greek:** *hedys* ("sweet, pleasant, agreeable") and *hedone* ("pleasure")

## Semantic Expansion

Beyond taste, "sweet" expanded to describe things "pleasing to the ear" (Old English), "beautiful, desirable" (mid-14c.), and in persons, "gracious, kind" with "pleasant manners" (Old English).
```


### [2026-09-14T03:15:23.927Z] TOOL RESULT

```
# Persian Etymology of خواستن (xâstan)

Based on the Wiktionary entry, here's what's documented:

**Middle Persian Source:** The entry states the word derives "From Middle Persian _hwʾstn'_ (/⁠xwāstan⁠/)."

**Proto-Iranian/Indo-European:** The Southern Kurdish section provides broader etymological context, indicating the term stems "from Proto-Iranian _*xwaz-_ ('to want; to wish'), of uncertain origin. Perhaps ultimately from Proto-Indo-European _*sweh₂d-_ ('sweet')."

**Cognates:** The entry notes the Southern Kurdish form خواستن (xwastin) is "Cognate with Persian _خواستن_ (xâstan, 'to want')."

**Limitations:** The main Persian section does not cite specific scholarly authorities like Cheung, Hasandust, or MacKenzie. The only referenced work appears in the Southern Kurdish references section: Nourai, Ali (2011), *An Etymological Dictionary of Persian, English and other Indo-European Languages*, page 459—though this authority isn't explicitly linked to the Persian etymology explanation above.
```


## [2026-09-14T03:15:28.786Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/persuade",
 "prompt": "Give the etymology of 'persuade': Latin persuadere, per- + suadere, and the PIE root."
}
```


## [2026-09-14T03:15:29.805Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/sweep",
 "prompt": "Give the etymology of 'sweep' and any mention of related words swift, swoop, swivel, swap, sway and their PIE root."
}
```


### [2026-09-14T03:15:32.157Z] TOOL RESULT

```
# Etymology of "Persuade"

The word "persuade" originates from Latin **persuadere**, which combines two elements:

- **per-**: meaning "thoroughly, strongly"
- **suadere**: meaning "to urge, persuade"

The root **suadere** traces back to the Proto-Indo-European (PIE) root ***\*swād-***, which means "sweet, pleasant." This ancient root also gave rise to the English word "sweet."

The term entered English around 1510s via Old French *persuader*, carrying the meaning of "lead to the opinion or conclusion, make (one) believe or think."
```


### [2026-09-14T03:15:35.752Z] TOOL RESULT

```
# Etymology of "Sweep"

**Origin:** "Sweep" derives from Middle English *swepen* (early 14c.), replacing earlier *swope*. The word traces to Old English *swapan* "to sweep" or possibly a Scandinavian source.

**Related Words Mentioned:**
- **Swoop:** Related to sweep through Old English *swapan*. The meaning "pounce upon with a sweeping movement" emerged by the 1630s, with spelling influenced by "Scottish and northern England dialectal *soop*."
- **Swipe:** Possibly "a dialectal variant of sweep" or from obsolete *swip/swaip* meaning "a stroke, blow."

**PIE Root:** The document indicates a possible connection to PIE *\*swei-* "to bend, turn," though this is noted as uncertain. The swoop entry mentions this root may underlie the Proto-Germanic *\*swaip-* form.

**Not Mentioned:** The provided content does not include etymologies for *swivel*, *swap*, or *sway*, so these cannot be addressed based on the source material.
```


## [2026-09-14T03:15:41.490Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/sway",
 "prompt": "Etymology of 'sway' (verb): Scandinavian source, Old Norse sveigja, Proto-Germanic form, PIE root."
}
```


## [2026-09-14T03:15:43.390Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%DB%8C%D9%88%D8%A7",
 "prompt": "Persian شیوا: meaning and etymology (Middle Persian, Avestan xšvaēwa, any cited source)."
}
```


### [2026-09-14T03:15:47.387Z] TOOL RESULT

```
# Etymology of "Sway"

## Verb Origin

The verb "sway" emerged in the early 14th century from Scandinavian origins. According to etymonline, it likely derives from "Old Norse _sveigja_ 'to bend, swing, give way.'" The term may have merged with an unrecorded Old English relative and potentially connects to related words like "swag" and "swing."

## Semantic Development

The word's meanings evolved progressively:
- **Early 14c**: "move, go, go quickly"
- **Late 14c**: "swing, waver, move in a swaying or sweeping motion"
- **c. 1500**: "move or bend from side to side" due to weight imbalance
- **1550s-1570s**: Transitive sense developed; came to mean "lean away from vertical"
- **1590s**: Figurative usage emerged, meaning "cause to be directed toward one side, prejudice"

## Noun Form

The noun appeared by the late 14th century, initially describing "movement from side to side, circular movement." By the 1510s, it acquired the sense of "controlling influence," as in the phrase "under the sway of," possibly alluding to symbolic power like "the sway of the scepter, or of the sword, embodying and illustrating government."
```


### [2026-09-14T03:15:49.131Z] TOOL RESULT

```
# شیوا (Shiva) - Word Summary

Based on the Wiktionary entry, **شیوا** is a Persian word with multiple meanings:

## Primary Definitions

**As an adjective:** "eloquent" with synonyms including فصیح (fasih) and رسا (rasâ).

**As a proper noun:** It functions as both a male and female given name meaning Shiva, and also appears as a surname.

## Etymology

The word has two documented etymological paths:

1. **From Persian roots:** Derived from شیو (šiv) plus the suffix ـا (-ā), functioning as an adjective form of the verb شیفتن (šiftan), meaning "to disturb, to disorder, to confuse, to fall in love."

2. **From Sanskrit:** The entry notes it comes "from indian shiva," referencing the Hindu deity Shiva.

## Pronunciation Variants

The pronunciation varies across Persian dialects, ranging from /ʃeː.ˈwaː/ in Classical Persian to [ʃiː.vɒ́ː] in Iranian Persian, with different realizations in Dari, Tajik, and other regional variants.
```


## [2026-09-14T03:16:37.257Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### BRT xvasta\"; grep -n \"x\\\"asta\\|x\\^asta\\|xvasta\\|x'asta\" BRT.txt | head -10\necho \"### BRT col near xSviwrra (line 11000)\"; sed -n '10995,11002p' BRT.txt | head -20\necho \"### BRT col header search around\"; awk 'NR>10960 && NR<11010 && /^[0-9]{3}$|^8[0-9][0-9]/' BRT.txt | head"
}
```


### [2026-09-14T03:16:38.538Z] TOOL RESULT

```
### BRT xvasta
7213:•  j.  a-x'asta-  Adj.  "nicht  gedroschen': agtavai  i^astanam  (sd.)  aSavat  "tanain {yavanqm)  ¥.7.35.
7217:•  j.  a-x'asta-  Adj,  "ungekocht':  ralu/ris
20770:yä  frasä  (sd.)  ävlsyä  ya  vä  .  .  *p?r9- saag  taya  yJ  (s.  a)  va  . .  tä  .  .  vamakl Y.31. 13;  s.  a  undNo.  la.  B)imjAw.; das  Relativ  ist  a)  substantivisch:  yat^a ahmat  asti  tnazyS  yalca^  ..  tat  nö  dayata Y.6$.\\\  — ya  tat  .  .  nigäaA^nti  *nishi- laitt  (sd.)  mit  tarn  ..  *daste  hupu^rlm  Y. JO.  IS;  —  yim  vasante  ahurä^kB  .  ,  t?>n vaiata  .  .  Yt.  i4-  39;  —  yä  paiti  .  .  tä paiti  N./o^(?);  —  s.  noch  Y.  55.  z  (unter ß)  und  V.J.  41  im  Anhang;  —  mit  Gen. part:  yäsla  ankam  (nämL  fravasiiiqm) nivämnte  ta  ..  YL/j.  68;  —  dgl.;  die Beziehung  ist  ungenau:  yejihl  hätqm  .  . vavhs  .  .  ahurS  vat^ä  .  .  yänkamcä tqseä  täscä  yasamaide  Y.  27. 1 5  '*.  ß)  ad- jektivisch :  yqm  . .  asava  asayqm  (sd.)  va^a tarn  drvä  pvjiivä  Vr.  22.  2;  — ya  nS  fanti gääsä  hanihrasaittiZa  ,  ,  yä  (zu  n)  nS Afttti  :^an%3mca  . .  ta  . .  Y.  55.  2 ;  —  im Sinn  von  quantus  (s.Sp.  1207  m.,  1209  m.): yä    hg  ux^astatB   ta-    mrifsaslatS    Yt,  7.
### BRT col near xSviwrra (line 11000)
•  j.  xSvtwi.i§av-  m.  Tfeilschiltze":  ir?xsd '^^  xsviwi.isvaUmB  airyanam  Yt  Ä6;  — •/ä«  parBMv^m  "den  ferntreffenden PfeilschUtzen"  Yl/o.ioz,  77.12.
Eig.i  'des  Pfeile  schnell  sind'.  —  Vgl,  xiviwi.-
•  j.  x§viwt.i§va't«ma-  Adj.  'der  beste Pfeilschlitze':  jrsxsd  (sd.)  xsviwi.isus  'mS airyanam  Yt.S.6.
Superl.  zu  xsvhvijSav:
•  j.  xi^viwi.väza-  Adj.  'schnell  dahin- fahrcnd,  fliegend':  ti^trjm  stänm  ..'växsm
•  j.  xSviwrra-  Adj.  'schnell,  flink,  ge- läufig': däya  me  . .  mastim  späiiB  'nm'^ kisvam  urune  usi  "gib  mir  . .  eine  flinke Zunge,  der  Seele  Auffassungskraft"  Y.  62.4.
KotDpA.  —  Vgl.  lEt.  xivatioayiü.aSirä-.  —  Fü.: S^k. —  >)  Ob 'r^n?  Man  beachte  aber,  dass neben  lUwä-  f,  ein  hau-  m.  voikommt.  — «)  S.  dain  SWienAW.  67.  846.  6,  wo  *iipäk Aitvän  mit  Jirm  tiitäit  (vgl.  zu  huduna-)  er- läutert wild.
•  j.  *xSviwrä3pa-  m.  EN.  eines  Gläu- bigen; 'paht^'>  x^tavalnyehe  (sd.)  asaanä Yty. iii; — /rJnyä  (sd.)  näiryS  'J>aAc'^ Yt.  13.140.
### BRT col header search around
564
```


## [2026-09-14T03:16:39.558Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### SKT sweet\"; grep -n \"^sweet\\b\\|^sweet (\" SKT.txt | head -5\necho \"### SKT sweep\"; grep -n \"^sweep\\|^swift\\|^sway\\|^swivel\\|^swap\" SKT.txt | head -10\necho \"### KLN sweet text\"; sed -n '37711,37725p' KLN_1966.txt\necho \"### HUB ctx\"; sed -n '7020,7032p' HUB.txt; echo ---; sed -n '7066,7075p' HUB.txt"
}
```


### [2026-09-14T03:16:39.670Z] TOOL RESULT

```
### SKT sweet
### SKT sweep
19006:sweep,  verb.  (E)  M.  E.  swipen.  A weak  verb,  answering  to  A.  S.  /w^/Mn*. not  U!<d,  the  regular  causal  form  of^A.S. swdpan,  to  swoop  (above).
### KLN sweet text
Derivative:  sweep-y,  adj. sweepstake(s),  n.  —  The  word  prop,  means ‘ sweeping  up  (i.e.  winning)  the  stakes'. sweet,  adj.  —  ME.  swete,  swote,  fr.  OE.  swete,
‘sweet,  pleasant’,  rel.  to  OS.  swoti,  ON.  ssetr,
Swed.  sot,  Dan.  sod,  MDu.  soete,  Du.  zoet,
OHG.  swuo^i,  suo3i,  MHG.  siieye,  G.  sufi,  fr.
I.-E.  base  *swad-,  ‘sweet,  pleasing  to  the  taste’, whence  also  OI.  svddah,  ‘agreeable  taste,  flavor’, svadati,  ‘makes  savory’,  svadate,  ‘tastes,  is  sa¬ vory’,  svaduh,  ‘sweet’,  Gk.  rjSu?  (for  *swadu),
‘sweet’,  rjSca&at  (for  *swadesthai),  ‘to  rejoice’, avSdvc.v  (for  *swandanein),  ‘to  please’,  L. suavis  (for  *suadvis ),  ‘sweet’,  suadere,  ‘to  advise’
(lit.  ‘to  make  tasteful’),  Lith.  sudyti,  ‘to  spice, salt’.  Cp.  Aedes,  assuage,  dissuade,  hedonic,  per¬ suade,  soave,  suave,  the  first  element  in  Hedychi- um  and  the  second  element  in  algedonic.  1
Derivatives:  sweet,  n.,  sweet-en,  tr.  and  intr.  v., sweet-en-ing,  n.,  sweet-ing,  n.,  sweet-ish,  adj., sweet-ish-ly,  adv.,  sweet-ish-ness,  n.,  sweet-ly, adv.
sweetheart,  n.  —  Compounded  of  sweet  and heart.  i
Derivatives:  sweetheart,  tr.  and  intr.  v.,  sweet- heart-ing,  n.
swell,  intr.  and  tr.  v.  —  ME.  swellen,  fr.  OE. swellan,  rel.  to  OS.  swellan,  ON.,  Norw.  svella,
Swed.  svalla,  OFris,  swella,  MDu.  swellen,  Du.  j
zwellen,  OHG.  swellan,  MHG.  swellen,  G.  1
schwellen.
Derivatives:  swell,  n.,  swell,  adj.  (colloq.), swell-ing,  n.  and  adj.,  swell-ish,  adj.  (colloq.) swelter,  intr.  v.,  to  be  faint  from  heat.  —  ME. sweltren,  swelteren,  freq.  of  swelten,  ‘to  die, faint',  fr.  OE.  sweltan,  ‘to  die’,  rel.  to  OS.  swet- tan,  ON.  svelta,  Goth,  sviltan,  ‘to  die’,  Du. zwoel,  G.  schwiil,  ‘sultry’,  OE.  swelan,  OFris.
### HUB ctx
Hormizd = ap. a(h)uramazda; azdahd *Drache* = arm.
aMahak, zd. azis dahako, u. s. w. In alien diesen Fallen
stand im Ap. der Verschlusslaut d.
§ 92. Ap. d hatte nach Vokalen die Geltung als
Spirans J und wurde im Paz. und Np. zu h oder y = i.
a) zu A: diham gebe* = zd. dadqmi^^di^. ipt. dadatuv
= daJatuv; x^dham 'wiinsche', skr. svad; sipdh *Heer =
zd. spada-, ap. {Taxma-)spaia' ; zirih *Panzer', paz. zreh,
phi. zrBh, arm. zrah-lc (5. Jhd.) == zd. zrada-, syr. NIIT,
arab. zarad ; nihadan *hinlegen' = ap. *nidatanaiy, pr. niham
aus "^nihiham = ap. *niSadamiy, vgl. zd. nidadat, skr. ni-
dadhatiy dazu w^'A^n Verborgen = ap. *m'J^wa-; paz. as^
t?a/i«J Min. Gl. 19 = phi. astv(i)hat Phi. Min. p. 11, Z. 2
---
wie?' = zd. kada; Dai *der zehnte MonatV zd. dadvd; nai
*Rohr , g. nad 'Rohr = skr. nada-, vgl. nai TlOte' aus
^nada-; pai Tussspur = zd. paia-, ap. nipadiy; x^ai
*Schweiss* = zd. x^'a^da- (also x'ai aus x'aiy); pai {pa) 'Fuss*
= zd. pada- ; -ra Casuspartikel = paz. ra, phi. rai wegen',
ap. radiy Vegen*; x^ai {x^a) *Wohlgeschmack' = skr. svada-;
boi {ho) *Geruch* = zd. baoidi- (arm. buidenik Moses, Geogr.
616, wohl boyicenik zu lesen = np. boy i ctnt 'chinesisches
Parfum'); roi {ro) 'aes vel stannum fusum' = bal. rDd 'Kupfer ,
arm. avoir 'Messing, skr. loha-; roi {rd) 'Gesicht' = zd.
```


## [2026-09-14T03:17:06.395Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### HUB page of line 7026\"; awk 'NR<=7026{n=gsub(/\\f/,\"\")} END{}' HUB.txt; python3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt',encoding='utf8',errors='replace').read()\nlines=t.split('\\n')\nimport re\nfor target in (7026,7071):\n    pre='\\n'.join(lines[:target])\n    print(target,'leaf',pre.count('\\f'))\nEOF\necho \"### SKT sweet\"; grep -n \"swete\" SKT.txt | head -5\necho \"### ARY خواستن\"; grep -n \"خواستن\" incoming/ARY/ARY_pages.txt | head -5"
}
```


### [2026-09-14T03:17:07.374Z] TOOL RESULT

```
### HUB page of line 7026
7026 leaf 208
7071 leaf 209
### SKT sweet
### ARY خواستن
3205:چم این واژه در زبان‌های غیرایرانی: خواستن» ترجیح دادن» بهتر دانستن» گزیدن.
7274:۸ / خواستن, خواست
14021:چم این واژه در آلمانی کهن و ولزی: اشتیاق» خواستن. بشید
```


## [2026-09-14T03:17:11.342Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==209' HUB.txt | head -3\necho \"=== ARY ctx\"; sed -n '7255,7300p' incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-14T03:17:12.310Z] TOOL RESULT

```
— 198 —
rujt^^m^, ad. ddrayemiy skr. dhardydmi 'halte, trage') ent-
Kapitel 16: ap. d.
=== ARY ctx
ساکسونی کهن 54300۸0 010): 5178881۸01 9 ۶0/0300
فریزی کهن (97ف51ل۲۶ 010): :امه
7 817۲852 1 (1773۵710) ,1034 (3014۳0211)
آلمانی کهن ((027(44 03ات صاه): 237 نقق منم لط0
لد اد ین :۸2052/215
انگلیسی کهن (8(01/5 طا0): 1 (0۸8۸31) ,133 (51.557)
7 5178۸ 270 : ماه
اسلاوی کهن (ع۷7ها5 تل#6ناتزه صا0): 348 60 :0۸/0/5
1 ,81۳۸1 1 (90۱/3018365) ود
لهستانی (۳0/87)+ ۳ ,852 ۸2/100
روسی (0۷فا55تا): 7 800 7 (51587) ,کا2 (273۸4)
صربی (587814/4): 7 ]5۳۸۷۸7۲ ,لال8۸ برهان قاطم + ۷۸۰
برهمی (80118211424): 1 588
او ی :
در زبان‌های ایرانی برای "خواب" (به چم "خفتن") و "خراب" (به چم "آنچه در خواب دیده می‌شود") یکك واژه‌ی
۱ واحد بکار می‌رود ولی در اکثر زبان‌های اروپایی برای این دو حالت دو واژه‌ی تمایز بکار می‌رزد. گاهی این دو
: واژه همريشه و گاهی ناهمریشه‌اند. در این فهرست واژه‌های همریشه وابسته به هر دو حالت داده شنده است. :
۱ ۰
[pdf page 247]
۸ / خواستن, خواست
آوستابی (4287/۷): یناه لیتوانی (۸۷ال۸تا 77 7آا): دا دا ری
بهلری (۲1اهاتزهه): ۸7
کردی (180150)): پسگشت‌ها ۹ ۸8782265
08710 ,20/۸8712 0 ۸000
سانسکریت (5275807): 26 نقققماتساطط
5 8۷۸2-870۸7 9 (۷۸۲) :25( ۸
آرمنی (۸ا/2452/): 0۸۴ 9 (81۸0) 57
برنانی (07888): تف800(1 ,11500۸1۸ 1 (088138) :۸10
این (0710): 5۷۸0585 ,8۷۸080 برهان قاطع : ۷۸۳
بادداشت:
۱ بازگشت به: شیرین.
فارسی (/۳881۸4): خوال (به چم "دو ده‌ای که برای ساختن مرکب از دود چراغ می‌گیرند")
اوستی (08557/6): ۸۲ دانمارکی (0۸۸/187): اک زان
سغخدی (/90001۸): نی نید سرئدی (317810150): این
خُتنی (2707۸/1885): 112۸۸ نروژی (/(0/05014: لاد
لاتین (/47): ۰ 9080588۳ ,8507255 هلندی (0076(7): اي ۸۷
گرتیک (007710): دی اد
نورس کهن (۸0782 010): دای امد پسگشت‌ها ۸5
ساکسونی کهن (54:00۷ ۰:01 8۷۷۸۲ 6 200220
فریزی کهن (۷لفا8لج7 صرا0): داد 0 (8۸35) 80
آلمانی کهن (/050/40 ۱۵ صا0): 3 داان :5/ نم ظ الما
4 برهان قاطع : ۷۸۲
آلمانی (0882/(۷): اما اند هن لغت‌نامه دهخدا: ۱۰۰۳۷
انگلیسی کهن 8۸۷01820 2ت0): 8۷/8۸7 فرهنگ معین : ۱۳۳۹
انگلیسی (50/ا8(/0): لا اون
ا
```


## [2026-09-14T03:17:23.831Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf8',errors='replace').read()\nlines=t.split('\\n')\nfor target in (37711,28308,37704,37190):\n    print(target,'leaf',('\\n'.join(lines[:target])).count('\\f'))\nEOF"
}
```


### [2026-09-14T03:17:25.023Z] TOOL RESULT

```
37711 leaf 823
28308 leaf 621
37704 leaf 823
37190 leaf 812
```


## [2026-09-14T03:17:32.731Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==789' KLN_1966.txt | head -12\necho \"=== leaf 790\"; awk 'BEGIN{RS=\"\\f\"} NR==791' KLN_1966.txt | head -6"
}
```


### [2026-09-14T03:17:33.713Z] TOOL RESULT

```
. name  of  the  campanula.  See  speculum  and  -ia.
speculate,  intr.  v.,  to  think,  conjecture.  —  L.  spe¬ culate,  pp.  of  speculari,  ‘to  watch,  observe,  ex¬ amine’,  fr.  specula,  ‘lookout,  watchtower’,  fr. specere,  ‘to  see,  look  at’.  See  speculum  and verbal  suff.  -ate  and  cp.  prec.  word.
speculation,  n.  —  ME.,  fr.  Late  L.  speculdtio,  gen. -onis,  fr.  L.  speculatus,  pp.  of  speculari.  See  prec. word  and  -ion.
speculative,  adj.  —  ME.  speculatif,  fr.  MF.  (= F.)  speculatif  (fern,  speculative ),  fr.  Late-L.  specu¬ lates  (fern,  speculated),  fr.  L.  speculatus,  pp. of  speculari.  See  speculate  and  -ive.
Derivatives:  speculative,  n.,  speculative-ly,  adv., speculative-ness,  n.
speculator,  n.  —  L.  speculator,  ‘looker  out,  spy, explorer’,  fr.  speculatus,  pp.  of  speculari.  See speculate  and  agential  suff.  -or.
speculatory,  adj.  —  L.  speculatorius,  fr.  specula- tus,  pp.  of  speculari.  See  speculate  and  adj.  suff. -ory.
speculum,  n.,  mirror.  —  L.,  fr.  specere,  ‘to  see, look  at’ ;  see  species  and  cp.  speculate.  Cp.  also spiegeleisen.  For  sense  development  cp.  looking- glass.
sped,  past  tense  and  pp.  of  the  verb  speed.  —  ME. spedde,  fr.  OE.  spedde,  past  tense  and  pp.  of spedan.  See  speed,  v.
speech,  n.  — -  ME.  speche,  fr.  OE.  spiec,  fr.  earlier sprxc,  rel.  to  OS.  spraka,  OFris.  spreke,  MDu. sprake,  Du.  spraak,  OHG.  sprahha,  MHG.
sprache,  G.  Sprache,  ‘speech’,  and  to  OE. sprecan,  ‘to  speak’.  See  speak.
Derivatives:  speech,  n.,  speech-er,  n.,  speech-ful, adj.,  speech-ful-ness,  n.,  speech-ing,  n.,  speech¬ less,  adj.,  speech-less-ly,  adv.,  speech-less-ness,  n. speechification,  n.  —  Formed  from  next  word.
=== leaf 790
ument  for  meas¬ uring  blood  pressure  in  the  arteries.  —  Com¬ pounded  of  sphygmo-  and  manometer, sphygmometer,  n.,  an  instrument  for  measuring the  strength  of  the  pulse  beat.  —  Compounded of  sphygmo-  and  Gk.  p6tpov,  ‘measure’.  See meter,  ‘poetical  rhythm’, sphygmophone,  n.,  an  instrument  for  rendering the  pulse  beat  audible.  —  Compounded  of sphygmo-  and  Gk.  9<uvy,  ‘sound,  voice’.  See phone,  ‘speech  sound’.
sphygmoscope,  n.,  an  instrument  for  examining the  pulse  beat.  —  Compounded  of  sphygmo- and  Gk.  -axomov,  fr.  <jxo7teIv,  ‘to  look  at, examine’.  See  -scope.
sphygmus,  n.,  the  pulse  (rued.)  —  Medical  L.,  fr. Gk.  o'puypo;,  ‘pulsation’,  fr.  <j9u£eiv,  (for *<j9uy-iEw),  ‘to  beat,  pulsate’,  whence  also £-<j9uxto<;,  ‘pulseless’;  possibly  derived  fr. *sphuk-,  a  gradational  var.  of  *sphek-,  ‘to  move convulsively’,  whence  aodxEXoc,  ‘convulsive movement,  gangrene’;  see  sphacelus  and  cp. sphygmo-,  asphyxia.  See  Hofmann,  EWG.,  p. 347  s.v.  cnpu^co.
Sphyraena,  n.,  a  genus  of  pikelike  fishes  (ichthyol.) —  ModL.,  fr.  L.  sphyraena,  ‘a  kind  of  seafish’, fr.  Gk.  <J9upaiva,  ‘hammer  fish’,  fr.  mpijpa, ‘hammer’,  which  is  rel.  to  <J9upov,  ‘ankle’, ajraipeiv,  ‘to  move  convulsively’,  from  I.-E. base  *(s)p(h)er-,  ‘to  move  convulsively’.  See spurn  and  cp.  words  there  referred  to. Sphyraenidae,  n.  pi.,  a  family  of  fishes  (ichthyol.) — ModL., formed  from  prec.  word  with  suff.-idae. spica,  n.,  a  spike  (hot.)  —  L.  spica,  ‘ear  of  com’.
See  spike  and  cp.  spicate. spicate,  spicated,  adj.,  1)  forming  a  spike;  2)  ar¬ ranged  in  spikes.  —  L.  spicatus,  pp.  of  spicare, ‘to  furnish  with  ears  or  spikes’,  fr.  spica.  See prec.  word  and  adj.  suff.  -ate,  resp.  also  -ed. spiccato,  adj.,  detached  (musical  direction)  —  It., pp.  of  spiccare,  ‘to  detach,  cut  off’,  formed  with change  of  pref.  fr.  impiccare,  ‘to  hang’,  which  is of  uncertain  etymology.
spice,  n.  —  ME.,  fr.  OF.  espice  (F.  epice),  fr.  Late L.  species,  ‘spice’,  fr.  L.  species,  ‘kind,  sort’.  See species.
```


## [2026-09-14T03:17:48.473Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR>=820 && NR<=826 {print \"---leaf\",NR-1; print substr($0,1,120)}' KLN_1966.txt\necho \"=== numbers\"; awk 'BEGIN{RS=\"\\f\"} NR==824' KLN_1966.txt | grep -o \"1[5-7][0-9][0-9]\" | head"
}
```


### [2026-09-14T03:17:49.528Z] TOOL RESULT

```
---leaf 819
,  surface.  —  L.  superficies,  ‘top,  sur¬ face’,  fr.  super-  and  facies,  ‘face’.  See  face  and cp. 
---leaf 820
plier,  ‘to  beseech,  en¬ treat’  (fr.  L.  supplicdre;  see  supplicate). Derivatives:  supply,  n.,  suppliance 
---leaf 821
  intr.  v.  —  ME.  surmisen,  fr.  MF. surmis,  surmise,  masc.  and  fem.  pp.  of  surmetre, ‘to  lay  to  one�
---leaf 822
r, sustenance,  n.  —  ME.,  fr.  OF.  sustenance,  souste- nance  (F.  soutenance),  fr.  Late  L.  sustinentia, ‘e
---leaf 823
, orig.  ‘of  the  color  of  dirt',  fr.  I.-E.  base  *  sword-, ‘dirty,  dark,  black’,  whence  also  sordes, 
---leaf 824
  waste  away,  lan¬ guish,  disappear’,  whicn  is  rel.  to  OE.  swindan, ‘to  waste  away,  languish,  vanish�
---leaf 825
s  there  referred to.  Cp.  also  monosyllable,  dissyllable,  trisyllable, tetrasyllable,  decasyllable,  dodecasyllab
=== numbers
1760
1552
1553
1688
1772
1552
1700
```


## [2026-09-14T03:17:55.108Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==824' KLN_1966.txt | grep -n -o \".\\{60\\}155[0-9].\\{60\\}\" | head -6\necho \"=== leaf 823 nums\"; awk 'BEGIN{RS=\"\\f\"} NR==823' KLN_1966.txt | grep -o \"1[45][0-9][0-9]\" | head"
}
```


### [2026-09-14T03:17:56.185Z] TOOL RESULT

```
53:  the  Dutch botanist  Emanuel  Swert  (Sweert)  (born  in  1552). For  the  ending  see  1st  suff.  -ia. swerve,  intr.  a
=== leaf 823 nums
1510
1551
```


## [2026-09-14T03:18:02.004Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==823' KLN_1966.txt | grep -n -o \".\\{80\\}1551.\\{80\\}\"; echo \"---1510\"; awk 'BEGIN{RS=\"\\f\"} NR==823' KLN_1966.txt | grep -n -o \".\\{60\\}1510.\\{60\\}\"\necho \"=== leaf 822 nums\"; awk 'BEGIN{RS=\"\\f\"} NR==822' KLN_1966.txt | grep -o \"\\b1[45][0-9][0-9]\\b\" | head"
}
```


### [2026-09-14T03:18:03.093Z] TOOL RESULT

```
---1510
=== leaf 822 nums
1548
1549
```


## [2026-09-14T03:18:21.650Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### POK thresh roots\"; grep -n \"dreschen\" POK_full.txt | head -10\necho \"### POK sues\"; grep -n \"^Root / lemma: sues\\|lemma: suas\" POK_full.txt | head"
}
```


### [2026-09-14T03:18:21.725Z] TOOL RESULT

```
### POK thresh roots
### POK sues
```


## [2026-09-14T03:18:29.459Z] TOOL CALL #67: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK data/verification/sources/refs/ocr/FFD && cp scratch-pg489.png data/verification/sources/refs/ocr/BOOK/489.png && cat > data/verification/sources/refs/ocr/FFD/51.vision.txt <<'EOF'\nFFD (Abolghasemi, Fe'l-hā-ye Fārsi-ye Dari), printed p. 51 = PDF page 56, read from the page image\n(pdftoppm -f 56 of FFD_asmaneketab.pdf), section «خواستن»:\n\nخواستن\nخواست ← فارسی میانه xwāst ← ایرانی باستان *xwās-ta. برای ta ← آراست. xwād صورت اصلی\nxwās است، d پیش از t به s بدل شده است. xwād به معنی «خواستن» است.\nخواه ← فارسی میانه xwāh ← ایرانی باستان *xwād-a. برای a ← آرای.\n\n(immediately above, same page:)\nخند ← فارسی میانه xand ← ایرانی باستان *xand. xand در فارسی میانه و ایرانی باستان «خندیدن» معنی می‌دهد.\n\nUsed for: page 489 (book p. 459), root Swâd, node #1 (Avestan xwâs, xwâd 'to desire').\nEOF\necho saved"
}
```


### [2026-09-14T03:18:30.532Z] TOOL RESULT

```
saved
```


## [2026-09-14T03:18:34.017Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"thresh\" POK_full.txt | head -10; echo \"=== POK_01 dreschen\"; grep -c \"dreschen\" POK_01.txt POK_02.txt POK_03.txt 2>/dev/null"
}
```


### [2026-09-14T03:18:34.100Z] TOOL RESULT

```
9302:space, site, courtyard, threshing floor; esp. a playground; hence, in gen., play ' (actually " 
13467:alb. fsiii, psiii, mes/ri's\Neep, thresh'; 
17105:threshing floor ', 51vr| (Hom.), Aeolic 5ivva (compare Aivvo|j£vr|<;, Hoffmann Gr. D. II 484) 
17113:dancing around', 5ivu) Aeolic 5ivvu) "thresh'; hom. 5iuj "flee', 5io|jai " chase away' (with 
17623:flat place on the threshing floor, threshing floor ' (Berneker 208, Trautmann 51 , different 
20560:n.. Modern High German Tenne^ barn floor, threshing floor, flattened loam ground or 
20561:wooden floor as a threshing place, hallway, ground, place, surface generally ', Dutch 
20563:a row or layer of vines '; as " smoothly trodden place good as threshing floor ' can be also 
38418:feasible); pa5r|v Adv. 'in footstep '; pa5oq m. 'way', paGpoq m. 'grade, threshold, footstep 
40487:Slavic *(g'c»K^o'c» "cattle'. Old Church Slavic ^i/-/77i>/7c» "threshing floor', i.e. " place where 
=== POK_01 dreschen
POK_03.txt:1
POK_01.txt:0
POK_02.txt:1
```


## [2026-09-14T03:18:44.574Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/خواستن' --note 'page 489, root Swâd, node #3 Persian xâstan: Wiktionary etymology (MP xwāstan; PIr *xwaz-, perhaps ultimately PIE *sweh2d-)' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/sweet' --note 'page 489, root Swâd, nodes #5/#6: OE swete < PGmc *swotja- < PIE *swad-' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/persuade' --note 'page 489, root Swâd, nodes #7/#8: L. persuadere = per- + suadere, PIE *swad-' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/sweep' --note 'page 489, root Swei/Sweib, nodes #4/#5: sweep, swoop, OE swapan, PIE *swei- to bend, turn' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/sway' --note 'page 489, root Swei/Sweib, node #5: sway < ON sveigja, not from the sweib- extension' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/شیوا' --note 'page 489, root Swei, node #3 Persian šīvā: Wiktionary derives it from šiv + -ā (šiftan), an alternative to Horn Av. xšvaēwa-' 2>&1 | tail -3"
}
```


### [2026-09-14T03:18:47.415Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/1ab6ad031c49803a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/38cd95e3b50f688f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1bf9eaea585a1272.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2da2920b0b918a79.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fe452757d2f6e9e6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b9ad0c3df81912c0.txt
```


## [2026-09-14T03:20:38.673Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'EOF'\nimport json\nd=json.load(open('data/verification/page-385.json'))\nfor e in d['entries']:\n    for n in e['nodes']:\n        if n.get('ref_check') and any(r.get('status')=='not_checked' for r in n['ref_check']):\n            print(json.dumps(n,ensure_ascii=False,indent=1)[:1200]); break\n    else: continue\n    break\nEOF"
}
```


### [2026-09-14T03:20:40.021Z] TOOL RESULT

```
{
 "id": 4,
 "lang": "English",
 "words": "punka",
 "verdict": "confirmed",
 "derivation": "English punkah (also punka) is an 18th-19th c. Anglo-Indian borrowing of Hindi paṅkhā. It is first recorded in Indian English contexts in the 17th c. (W. Finch 1610 'two Punkawes to gather wind', Bernier 1668 'their great Pankas, or Fans') and settles in the sense Nourai gives — the big cloth-on-frame fan slung from the ceiling and worked by a rope-pulling servant (the punkah-wallah) — during the Raj. The English spelling with -k- (no aspirate) reflects the usual anglicisation of Indic kh.",
 "derivation_fa": "واژهٔ انگلیسی punkah/punka وام‌واژه‌ای انگلیسی‌ـ‌هندی از paṅkhā هندی است. نخستین کاربردهای آن در متون انگلیسیِ هند از سدهٔ هفدهم میلادی است (فینچ ۱۶۱۰، برنیه ۱۶۶۸) و در دورهٔ استعمار بریتانیا معنای ویژهٔ «بادبزن بزرگ پارچه‌ای آویخته از سقف که خدمتکار با ریسمان می‌کشد» یافته است. نبودِ «h» در املای انگلیسی، بازتاب عادیِ ساده‌شدن همخوان دمیدهٔ هندی در انگلیسی است. ادعای نورایی درست است.",
 "sources": [
  "https://en.wiktionary.org/wiki/punkah"
 ],
 "ref_check": [
  {
   "ref": "KLN:1272",
   "status": "supports",
   "note": "Klein 1966 p.1272: 'punka, punkah, n., a large curtain serving
```


## [2026-09-14T03:20:42.958Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification\ngrep -ho '\"ref\": \"[^\"]*\"' page-3*.json | sort | uniq -c | sort -rn | head -8"
}
```


### [2026-09-14T03:20:43.063Z] TOOL RESULT

```
    275 "ref": "AHD"
    179 "ref": "None"
     63 "ref": "(none cited)"
     43 "ref": "MON"
     26 "ref": "KLN"
     23 "ref": "(none)"
     23 "ref": "BQT"
     11 "ref": "none"
```


## [2026-09-14T03:20:47.450Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>10940 && NR<11020 {if (length($0)<8 && $0 ~ /[0-9]/) print NR\": \"$0}' BRT.txt\necho \"--- context of header lines\"; sed -n '11006,11020p' BRT.txt | cut -c1-120"
}
```


### [2026-09-14T03:20:48.451Z] TOOL RESULT

```
10948: S6i
10992: 564
11019: S6S
--- context of header lines
[Hier  fehlendes  s.  unter  i.]
•  j.,  g-i  p.  °<S,  j.  'ca  enkl.  Part.  (jAw. und  YHapL  unvollständig).  A)  Zur  Ver- bindung von  zwei  od
Ap.:
vas?iS  (^ur^masdähe^  mana^a  dä- fD.4.2.  B)imAwr.;  i)die Glieder  sind  nominal'';  a)  sie  folgen  sich unmittel
—  karapä  usixsca  Y.  44-30;  —  karapanB kävayascä  Y.  46. 11;  —  dssta  mazdä  xsa- ya/ä  Y.  2<9.  7 ;
—  yätavB  pairikis^a  YtÄ44;  — vTspe  daSva  masySca  Yt/p.  29;  —  ahsm ratBmla  ga^anam  Yljj.  9a  (s.  da
5 ;  —  antan  pitar}  pu%r»nca  Vt.  jo.  1 1 7 ;
^  hvq-m  anu  ustXm  taessmca  V.  2. 11;  — bcu>t?ntB  suhm  larsrum^a  baoomtB  aofom urväxnmca  Yt.  15.  69;  -
—  maitiyB  3%raiä  Y.  31.  y,  22;  — mainya  syaoianäis^ä  Y.  Ji.  ai;  —  pa- s?u/vTräat^äY.3i.i5;  — 
—  daMyunqm  eätanqm  azätanqm^a  YL  if). 56;  —  have  atahi   M%raica   Yt.  7j.  67;
—  %ioähü  gathaha  tanmica  Y. 43.T;  — 3^ai^  syaö^anai^  hisvasca  Y.5J.  13;  — msr^tB  bpfstaca  damayäi 
—  kava^bya  p^aHbya  x^a^diyäia  varsa V.  tf.  46;  —  zara%ustrMn  atnm  pairi.- yaozdd^snlim  gä^äsca  sräva
dby  Google
S6S
•Ca  A  I  1  I  b
```


## [2026-09-14T03:21:01.040Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"droschen\\|dreschen\" BRT.txt | head\necho \"=== col of line 7213\"; awk 'NR>7150 && NR<7230 {if (length($0)<8 && $0 ~ /[0-9]/) print NR\": \"$0}' BRT.txt\necho; sed -n '7210,7220p' BRT.txt | cut -c1-200"
}
```


### [2026-09-14T03:21:01.995Z] TOOL RESULT

```
6980:•  j.  a-x*asta-  Adj.  *nicht  gedroschen':  *!i  stllY.43.z\ — yakmya  3p5..^waxs3iite altavat  ifastaiiqm  (sd.)  aSavat  'tanqm  *3  iskafymT^  pouruttm^a  Yt/O.  14;  — {yavanqm)  V.  7,35.  paityaogit  (sd.)  ta  akmai  jassit . .  iaurSui
7213:•  j.  a-x'asta-  Adj.  "nicht  gedroschen': agtavai  i^astanam  (sd.)  aSavat  "tanain {yavanqm)  ¥.7.35.
=== col of line 7213
7197: 299
7227: 3CI
7228: an  3

•  j,  a-x^arant-  Adj.  'nichtessend':  naiUs •nntam  tva  fidii  ..  asayam(sd.)  ..V.^.^y
•  j.  a-x*ar3ta-  Adj.  'unfassbar,  unnahbar', vom  ofar^nah-  (sd.):  uyrpm  °i3m  :^ar3m mazfiaöJlim  .  .  yakmi  faiti  "pamfäd (sd.)  sptntasca  mainytd  anrasca  aetahmt paiti  at  'te  Y
Et.?0  Bed.  nach  Pü.—  Pü.:  agrifl,  erl. :  fai aqrißVi  c  ktt  fafrahang  3  J^i'r  iäyel  karlait.  — ■')  Ohne  Wert  Sp.  Komm.  3.  66,  Gdw,  VSt. 2.  179.
•  j.  a-x'asta-  Adj.  "nicht  gedroschen': agtavai  i^astanam  (sd.)  aSavat  "tanain {yavanqm)  ¥.7.35.
l'ü.:  fehlt.
•  j.  a-x'^Sra-  Adj,  (fem.  °rä^  'unbequem, lästig':  druxi  're  (VSf.)  fvsmziie  V.  7tS'. 30.  36.
Pü.:  flj^J.;/;,  erl.;  hil  nnaiiik  H  äiiH  nest.
•  j.  a-x'asta-  Adj,  "ungekocht':  ralu/ris
*paySbii  :^astäti  ■'taisca  N.  57.
VgL  ana.3^äsla-.  —  Pü.:  afuj:t.
•  j.  a-x'^äa-  n.  "Nichtessen":  ^aiaya  vTsps atihuS  .  .  jvaiti  'se  framiryelte  V._j.  33,
```


## [2026-09-14T03:21:10.191Z] AGENT

Now I'll write the verification file.


## [2026-09-14T03:32:23.685Z] TOOL CALL #74: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-489.json <<'JSONEOF'\n{\n  \"pdf_page\": 489,\n  \"book_page\": 459,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [\n    {\n      \"entry\": 1,\n      \"root\": \"Svas\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"Proto-Indo-Iranian *su̯as- / Proto-Iranian *hu̯ah- 'to strike, thresh, trample' (Cheung, EDIV 141 f.); no such root in Pokorny\",\n      \"note\": \"The root box is lifted straight out of Buck's synonym dictionary: SYN 510 (§8.34 THRESH) writes 'Av. xʳasta- “threshed”, axʳasta- “unthreshed” (cf. NPers. pai-xʳasta “trodden by foot”), fr. xʳah- “press”. Otherwise Barth. 874 f. (“Et.?”), Suppl. 246 (fr. root ending in dental), but the deriv. fr. xʳah- (Aryan *svas-) seems perfect in form and sense.' Buck's asterisked form is therefore ARYAN, i.e. Indo-Iranian, not Indo-European, and Nourai's language label 'Indo-European' overstates it: greps of POK_full.txt, POK_01-03 and AHD_watkins1985.txt find no PIE root *su̯as-/*su̯es- 'thresh' (Pokorny has no entry; Watkins none). Cheung 2007 reconstructs Proto-Iranian *huah 'to strike, thresh; [inch.] to become tired' on a wide Iranian base (Av., MP, Parthian, Khotanese, Sogdian, Choresmian, Bactrian, Kurdish, Balochi) but offers no IE etymology and no PIE preform. Bartholomae himself marked the Avestan verb 'Et.?'. So: the Iranian root is real and the gloss 'thresh, beat grain' is right; only its projection back to PIE is unsupported.\",\n      \"note_fa\": \"ریشهٔ که نورایی «Svas» می‌نامد عیناً از باک (Buck, ص ۵۱۰) گرفته شده است؛ اما باک خود آن را «آریایی» (یعنی هندوایرانی) می‌خواند نه هندواروپایی آغازین. در پوکورنی و والده‌پوکورنی و واتکینز هیچ ریشهٔ *su̯as- به معنی «خرمن‌کوبی» دیده نمی‌شود. چونگ (Cheung) ریشهٔ ایرانی آغازین *hu̯ah «زدن، کوبیدن، خرمن کوبیدن» را بازسازی می‌کند ولی برای آن ریشهٔ هندواروپایی قائل نیست؛ بارتولومه نیز ریشه‌شناسی فعل اوستایی را ناشناخته دانسته است. پس معنی و ریشهٔ ایرانی درست است، اما برچسب «هندواروپایی» با احتیاط پذیرفتنی است.\",\n      \"sources\": [],\n      \"ref_check\": [\n        {\"ref\": \"SYN:510\", \"status\": \"supports\", \"note\": \"SYN.txt, §8.34 THRESH, printed p. 510 (grep -n 'THRESH' SYN.txt → line 12819 ff.): 'Av. x*asta- “threshed”, ax'asta- “unthreshed” (cf. NPers. pai-xvastg “trodden by foot”), fr. xah- “press” ... but the deriv. fr. xʳah- (Aryan *svas-) seems perfect in form and sense.' Exactly Nourai's root, gloss and reconstruction — but as an Aryan (Indo-Iranian), not IE, form.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"POK_full.txt, roots su-/suard-/suad-/sueid- (lines 83246-83400)\", \"stance\": \"silent\", \"note\": \"no root *su̯as-/*su̯es- 'dreschen, thresh' anywhere in Pokorny; grep 'thresh' in POK_full.txt returns only 'threshing floor' passages under other roots.\"},\n        {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt\", \"stance\": \"silent\", \"note\": \"Watkins' appendix has swad-, swei-1, swei-2, sweid-1/2 but no root for 'thresh'.\"},\n        {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt lines 9981-10045, s.v. *huah\", \"stance\": \"partial\", \"note\": \"'*huah “to strike, thresh; [inch., intr.] to become tired” ... Y Av. paiti x'aŋh- “to thresh” ... Partic. perf. pass. YAv. x'asta- (V 7.35) ... BMP hws- /xwas-/ ... hwst /xwast/'. Supports the Iranian root and its meaning; no PIE preform is given, so the IE label is not supported.\"},\n        {\"src\": \"WLD\", \"where\": \"WLD_Bd2_pages.txt\", \"stance\": \"silent\", \"note\": \"greps for 'suad'/'sueib' hit only the 'sweet' and 'bend' roots; Walde-Pokorny has no *su̯as- 'dreschen'.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"xvasta; a-xvasta\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Young Avestan xʳasta- is the perfect passive participle of the verb xʳaŋh-/xʳah- 'to thresh, trample' (present paiti xʳaŋhaiieiti, Y 57.10), formed with the ordinary Iranian -ta- participle on a root-final sibilant: *hu̯ah-ta- > xʳas-ta-. Bartholomae AiW col. 300 lists the privative compound a-xʳasta- 'nicht gedroschen' from Vd 7.35, where the context is unthreshed grain (yavanẹm) — precisely Nourai's 'unthreshed' with the IE privative prefix *n̥- > Av. a-. Cheung (EDIV s.v. *huah) cites the same participle (V 7.35) and the same present. Beware the exact homonym printed immediately below it in Bartholomae, a-xʳasta- 'ungekocht' (N 57), which belongs to the 'sweet' root of the next chart on this page; Nourai keeps the two apart correctly. The cross-reference to root 'Ne 1' for the a- privative is right.\",\n          \"derivation_fa\": \"صورت اوستایی xʳasta- اسم مفعول (صفت مفعولی با پسوند -ta-) از ریشهٔ xʳaŋh-/xʳah- «کوبیدن، خرمن کوبیدن» است (مضارع: paiti xʳaŋhaiieiti در یسنا ۵۷،۱۰)؛ از *hu̯ah-ta- با تبدیل h به s پیش از t. بارتولومه (ستون ۳۰۰) صورت منفی a-xʳasta- «خرمن‌نکوبیده» را از وندیداد ۷،۳۵ دربارهٔ غلهٔ خرمن‌نکوبیده می‌آورد؛ پیشوند a- همان پیشوند نفی هندواروپایی *n̥- است. توجه شود که همانجا هم‌آوای دیگری a-xʳasta- «نپخته» هست که به ریشهٔ دیگر (شیرین/پختن) می‌رسد و نورایی آن دو را درست جدا کرده است. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"SYN:510\", \"status\": \"supports\", \"note\": \"SYN.txt p. 510: 'Av. x*asta- “threshed”, ax'asta- “unthreshed” ... fr. xʳah- “press”' — both words of the node, with Nourai's glosses.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"BRT.txt line 7213, col. ~300\", \"stance\": \"supports\", \"note\": \"'j. a-x'asta- Adj. “nicht gedroschen”: ašavai xʳastanam (sd.) ašavat tanam (yavanẹm) V.7.35' — and four lines below, the distinct homonym 'j. a-x'asta- Adj. “ungekocht”: ... N.57'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt lines 9981-9990, s.v. *huah\", \"stance\": \"supports\", \"note\": \"'*AVESTAN: (+ *pati-) Y Av. paiti x'aŋh- “to thresh” ... Partic.: perf. pass. Y Av. x'asta- (V 7.35)'.\"},\n            {\"src\": \"POK\", \"where\": \"POK_full.txt\", \"stance\": \"silent\", \"note\": \"Pokorny has no entry covering Av. xʳasta- 'threshed' (his xʳasto under suad- p.1039 is the 'cooked' homonym).\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"xost\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Middle Persian xwastan, present xwah- [hwstn' | J xwh-] 'tread, trample; thresh' (MacKenzie, CPD p. 95) continues Av. xʳah-; its past stem xwast is inherited directly as New Persian خوست xost 'crushed, trodden, mashed'. The vowel a > o is the usual rounding after the labiovelar xʷ- before the cluster -st, and the xʷ- itself was simplified to x- in later New Persian. The simplex survives chiefly in the compounds Nourai lists: آبخوست āb-xost 'island' (land 'pounded together' by water — Mo'in glosses it 'خشکی میان دریا'), پای‌خوست pā-xost 'trodden underfoot' (= Buck's NPers. pai-xʳasta), and چنگال‌خوست čangāl-xost, the dish of bread crumbled and mashed with butter and sugar. Cheung records the same word under *huah: '(orig. ppp.) NP x'ast “beaten road; rubbed”'. The variant خست xast printed in parentheses in the chart is the same stem with the unrounded vowel (cf. Mo'in's پای‌خست = پای‌خوست).\",\n          \"derivation_fa\": \"«خوست» بازماندهٔ مادهٔ ماضی فارسی میانهٔ xwast از مصدر xwastan (مضارع xwah-) به معنی «لگدکوب کردن، خرمن کوبیدن» است (مکنزی، فرهنگ کوچک پهلوی، ص ۹۵) و آن هم از ریشهٔ اوستایی xʳah-. واکهٔ a در پی خوان دولبی xʷ- به o گراییده است. این واژه در فارسی نو بیشتر در ترکیب‌ها مانده است: «آبخوست» (جزیره)، «پای‌خوست/پای‌خست» (لگدکوب) و «چنگال‌خوست». حاشیهٔ معین بر برهان قاطع (ص ۷۸۳) نیز «خوست» را به معنی «مالیده و کوفته» می‌آورد و از لغت فرس گواه می‌آورد. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"SYN:510\", \"status\": \"supports\", \"note\": \"SYN.txt p. 510: '(cf. NPers. pai-xvastg “trodden by foot”)' — Buck cites exactly the compound پای‌خوست that Nourai puts in the extras box.\"},\n            {\"src\": null, \"ref\": \"MON:1455\", \"status\": \"supports\", \"note\": \"Mo'in's text confirms the words — MON_part1.txt line 29102: 'پای‌خست: [= پای‌خاسته - پای‌خسته - پای‌خوست] (امف.) هر چیز که در زیر پای کوفته شده باشد، لگدکوب، لگدمال'; line 51522 'چنگالی، چنگال‌خوست'; line 2334 'آبخوست' s.v. آداک/جزیره. The local MON OCR carries no page tags, so the page number 1455 itself could not be checked.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"PHD.txt p. 95 (leaf 116), s.v. xwastan\", \"stance\": \"supports\", \"note\": \"'xwastan, !xwāh- [(Y)PLHWN-tn! ...; hwstn!, hw'd- | J xwh-, N xwast] tread, trample; thresh. ~išn: trampling.' MacKenzie's 'N xwast' is precisely this New Persian word, and he keeps it apart from xwāstan 'seek, want'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt line ~10040, *huah, *NWIR section\", \"stance\": \"supports\", \"note\": \"'(orig. ppp.) NP x'ast “beaten road; rubbed”, Tt. xwah- “to thresh”'.\"},\n            {\"src\": \"BQT\", \"where\": \"BQT_v2_pages.txt leaf 240-241 = printed pp. 783-784, Mo'in's footnotes\", \"stance\": \"supports\", \"note\": \"footnote: 'لغتی در «خوست» بمعنی مالیده و کوفته ... آبخوست و پای خوست ... در لغت فرس آمده: پای‌خوست آن باشد که بپای گرفته (کوفته) ... آبخوست آن باشد که به آب درهم گرفته (کوفته)'.\"},\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt lines 2334, 29102-29105, 51522\", \"stance\": \"supports\", \"note\": \"آبخوست / پای‌خست، پای‌خوست 'کوفته شده زیر پا' / چنگال‌خوست — all three compounds of the extras box are in Mo'in with the sense 'crushed, pounded'.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 2,\n      \"root\": \"Swâd\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *sweh₂d- (older notation *su̯ād-) 'sweet; to make/become savoury'\",\n      \"note\": \"Pokorny 1039-1040 s.v. su̯ād- 'suß' is exactly this root, with su̯ādu-s 'sweet' (OInd. svādú-, Gr. ἡδύς, Lat. suāvis, OE swēte), su̯ādos- n., verbs svadate / ἥδομαι / Lat. suādeo. Watkins (AHD) 'swad-. Sweet, pleasant. [Pok. suad- 1039]'; Cheung EDIV s.v. *huad cites 'PIE *sueH₂d- “to make, become savoury” = LIV 606 f. | Pok.: 1039 f.'. Root name, language label and gloss are all correct; the only quarrel on this chart is whether New Persian خواستن belongs here (see nodes 2 and 3).\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *sweh₂d- (در نوشتار کهن‌تر *su̯ād-) به معنی «شیرین، خوش‌مزه کردن» است؛ پوکورنی ص ۱۰۳۹–۱۰۴۰، واتکینز (swad-) و چونگ (*huad) همه همین را می‌گویند. بازمانده‌های آن سنسکریت svādú-، یونانی hēdýs، لاتین suāvis/suādēre و انگلیسی sweet است. نام ریشه، برچسب زبانی و معنای آن درست است؛ تنها بحث‌انگیز در این نمودار پیوستن «خواستن» فارسی به این ریشه است.\",\n      \"sources\": [\"https://www.etymonline.com/word/sweet\"],\n      \"ref_check\": [\n        {\"ref\": \"POK:1039\", \"status\": \"supports\", \"note\": \"POK_full.txt line 83287 ff.: 'Root / lemma: suad- — Meaning: sweet ... 1. suadu-s “sweet”: Old Indic svadu-, f. svadvi ... Latin suavis (*suaduīs) ... Old English swete ... Page(s): 1039-1040.'\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II 516 f. (WLD_Bd2_pages.txt, the su̯ād- entry running into p. 517)\", \"stance\": \"supports\", \"note\": \"'Kaus. bzw. Intensivum svadáyati (= lat. suādeo, s. u.) und svādáyati „schmackhaft, genießbar, annehmbar machen“ ... av. xʳandra-kara- „angenehmes tuend = gefällig“, afgh. xʳand „Wohlgeschmack, Vergnügen“'.\"},\n        {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt line 1036, s.v. swad-\", \"stance\": \"supports\", \"note\": \"'swad-. Sweet, pleasant. 1. Germanic *swōtja- in Old English swēte, sweet: SWEET. 2. Suffixed form *swād-ē- in Latin suādēre ... PERSUADE ... [Pok. suad- 1039.]'\"},\n        {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt lines 9954-9975, s.v. *huad\", \"stance\": \"supports\", \"note\": \"'*huad “to become, make savoury, pleasant” ... «PIE *sueH₂d- “to make, become savoury” = LIV: 606 f. | Pok.: 1039 f.'\"},\n        {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 823 (printed pp. 1550/51), s.v. sweet\", \"stance\": \"supports\", \"note\": \"'fr. I.-E. base *swad-, “sweet, pleasing to the taste”, whence also OI. svādaḥ ... Gk. ἡδύς ... L. suavis (for *suadvis), suadere, “to advise” (lit. “to make tasteful”)'.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"xwâs, xwâd; xvâsto; xvand; xvandra-kara\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Two of the four items are straight Avestan and confirmed; two are not. (a) xʳasta- (Nourai's 'xvâsto') 'made savoury by cooking, cooked' is Pokorny's 'Avestan xʳasto „durch Kochen (schmackhaft) gemacht“ = Old Indic svādita-'; Bartholomae AiW col. 300 has the privative a-xʳasta- 'ungekocht' (N 57). It is the exact homonym of the 'threshed' participle of the previous chart, from a different root. (b) xʳandra-kara- 'doing what is pleasing, compliant' is Avestan and nasalised (*su̯ad-n-ro-), as Pokorny and Walde-Pokorny II 517 say; Nourai's cross-reference to root Kwer for the second member (-kara- 'making') is correct. (c) 'xvand “sweet taste”' is NOT Avestan: both Pokorny ('afgh. xʳand „Wohlgeschmack, pleasure“') and Walde-Pokorny and Cheung ('Pash. xwand (m.) “taste, pleasure”') label it Pashto/Afghan; Nourai has silently promoted it into the Avestan box. (d) 'xwâs, xwâd “to desire”' is no attested Avestan verb either: it is Abolghasemi's reconstructed Old Iranian root *xwād- with its pre-dental allomorph xwās-, posited precisely to yield MP xwāst/xwāh (FFD 51), and Nourai's second cited reference is that page.\",\n          \"derivation_fa\": \"از چهار صورت این خانه، دو تا اوستایی اند و دو تا نیستند. xʳasta- «پخته و خوش‌مزه‌شده» (پوکورنی ۱۰۳۹) و xʳandra-kara- «دلپسند، خوشایند» (همانجا و والده‌پوکورنی جلد ۲ ص ۵۱۷) هر دو درست‌اند؛ اما xvand «مزهٔ شیرین» در همان منابع صریحاً پشتو (افغانی) دانسته شده، نه اوستایی، و xwās/xwād نیز فعل اوستایی نیست بلکه ریشهٔ بازساختهٔ «ایرانی باستان» است که ابوالقاسمی در «فعل‌های فارسی دری» ص ۵۱ برای توجیه xwāst/xwāh آورده است. پس خانه در کل پذیرفتنی است ولی برچسب «اوستایی» برای دو صورت آخر نادرست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"POK:1040\", \"status\": \"partial\", \"note\": \"POK_full.txt, suad- (pages 1039-1040): supports xʳasto 'through cooking (schmackhaft) gemacht' and 'nasalized Avestan x'andra-kara- „angenehmes machend = compliant“', but the very next words are 'afgh. x'and „Wohlgeschmack, pleasure“' — Pokorny calls xvand Afghan (Pashto), contradicting the Avestan label; and he has no Avestan verb 'xwās/xwād to desire'.\"},\n            {\"ref\": \"FFD:51\", \"status\": \"supports\", \"note\": \"Abolghasemi, Fe'l-hā-ye Fārsi-ye Dari p. 51 (PDF p. 56, read from the page image, saved to data/verification/sources/refs/ocr/FFD/51.vision.txt): 'خواست ← فارسی میانه xwāst ← ایرانی باستان *xwās-ta. ... xwād صورت اصلی xwās است، d پیش از t به s بدل شده است. xwād به معنی «خواستن» است.' — the source of Nourai's pair xwâs, xwâd 'to desire', though Abolghasemi calls it Old Iranian, not Avestan.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II 517\", \"stance\": \"partial\", \"note\": \"'av. xʳandra-kara- „angenehmes tuend = gefällig“, afgh. xʳand „Wohlgeschmack, Vergnügen“' — supports xʳandra-kara- as Avestan, contradicts the Avestan labelling of xvand.\"},\n            {\"src\": \"BRT\", \"where\": \"BRT.txt line 7217, col. ~300\", \"stance\": \"supports\", \"note\": \"'j. a-x'asta- Adj. “ungekocht”: ... N. 57' — the negated form guarantees the Avestan participle xʳasta- 'cooked'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt lines 9954-9962, s.v. *huad\", \"stance\": \"partial\", \"note\": \"'Y Av. x'asta- (ppp.) “cooked, well done” (Y 11.1, V 5.52, V 19.40) ... *NEIR: Pash. xwand (m.) “taste, pleasure”' — confirms xʳasta- as Avestan and xwand as Pashto; Cheung lists no Avestan verb 'to desire' under this root.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"xvâstan\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Middle Persian xwāstan, present xwāh- [BOYHWN-stn' / hw'stn', hw'd- | Man. MP xw'stn, xw'h-] 'to seek, want, desire; to attract, acquire' is a real and common word (MacKenzie, CPD p. 95), and MacKenzie keeps it rigorously apart from xwastan/xwah- 'tread, thresh' of the previous chart. The derivation Nourai draws — from the 'sweet' root — is the classical one: Horn, Grundriss no. 497 (p. 110) puts NP xʳāsten 'wünschen, wollen' with 'ai. √svad-, svādati „sich schmecken lassen, Gefallen finden“; gr. ἥδομαι' and cites 'phlv. xʳāstan „wollen, wünschen“'; Hübschmann, Persische Studien §92 (p. 198), lists 'xʳāham „wünsche“, skr. svad' among the words showing Old Persian d > h; Abolghasemi (FFD 51) formalises it as OIr *xwād-a- > MP xwāh-, *xwās-ta- > MP xwāst. Against it stands the Parthian evidence: Nyberg (Manual II, s.v. xʳāstan) gives 'OIr *hvāz-, MPrth wx'št, pres. wx'z-; MPrs xw'stn, xwh-', and a Parthian present in -z- cannot come from *-d-; accordingly Cheung's EDIV puts Av. xʳasta- 'cooked' under *huad but does not list xwāstan there at all, and Wiktionary gives Proto-Iranian *xwaz- 'to want', 'of uncertain origin. Perhaps ultimately from Proto-Indo-European *sweh₂d- “sweet”'. So: an old, respectable, still-possible derivation, not the modern consensus.\",\n          \"derivation_fa\": \"فارسی میانه xwāstan (مادهٔ مضارع xwāh-) «خواستن، طلبیدن» واژه‌ای مسلم است (مکنزی ص ۹۵) و مکنزی آن را به‌دقت از xwastan «خرمن کوبیدن» جدا می‌کند. ریشه‌شناسی‌ای که نورایی می‌آورد همان رأی کهن است: هرن (بند ۴۹۷، ص ۱۱۰) «خواستن» را با سنسکریت svad و یونانی hḗdomai می‌سنجد، هوبشمان (مطالعات فارسی، بند ۹۲، ص ۱۹۸) xʳāham را در شمار واژه‌هایی می‌آورد که d پارسی باستان در آنها به h بدل شده، و ابوالقاسمی هم *xwād-a- > xwāh می‌نویسد. در برابر، نیبرگ صورت ایرانی باستان *hvāz- و مادهٔ مضارع پارتی wxʾāz- را گواه می‌آورد که از *-d- برنمی‌آید؛ چونگ نیز «خواستن» را زیر *huad نیاورده است و ویکی‌واژه ایرانی آغازین *xwaz- می‌دهد و پیوند با *sweh₂d- را تنها «شاید» می‌داند. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%A7%D8%B3%D8%AA%D9%86\"],\n          \"ref_check\": [\n            {\"ref\": \"HRN:110\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 131 = printed p. 110, no. 497: 'xʳāsten „wünschen, wollen“, Praes. xʳāhem ... ai. √svad-, svādati „sich schmecken lassen, Gefallen finden“, svādate; gr. ἥδομαι ... phlv. xʳāstan „wollen, wünschen“, xʳāh(i)šn, xʳāstār, xʳāstak „Besitztum“' — exactly Nourai's Pahlavi-from-*swād- arrow.\"},\n            {\"ref\": \"BQT:783\", \"status\": \"partial\", \"note\": \"BQT_v2_pages.txt leaf 240/241 = printed pp. 783-784 carries the خواس/خواستار/خواسته entries, and Mo'in's footnote gives the Pahlavi: 'پهلوی xvāstak (مال) «مینوی ۲:۹۳۱» ... ارمنی ... هوبشمان ۴۹۷'. It documents the Pahlavi stem but offers no root etymology, so it supports the MP form, not the arrow from Avestan.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"PHD.txt p. 95 (leaf 116)\", \"stance\": \"partial\", \"note\": \"'xwāstan, *xwāh- [BOYHWN-stn! < A √b'y; hw'stn!', hw'd- | M xw'stn, xw'h-, N ~] seek, want, desire; attract, acquire.' Confirms the form and meaning; MacKenzie gives no etymology, and lists xwastan 'thresh' as a separate lemma.\"},\n            {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt line 4360, s.v. xʳāstan\", \"stance\": \"contradicts\", \"note\": \"'— OIr *hvāz-, MPrth wx'št, pres. wx'z-; MPrs xw'stn, xwh-; Paz. NP xʳāstan ... Verbum 187; Ghilain 69; Bailey, BSOS VI' — Nyberg reconstructs a root in *-z-, not the *-d- of the 'sweet' root.\"},\n            {\"src\": \"ARY\", \"where\": \"ARY_pages.txt, pdf p. 247, entry 'خواستن، خواست'\", \"stance\": \"supports\", \"note\": \"Aryanpur groups خواستن with Avestan, Pahlavi, Sanskrit svad-, Latin SUADEO/SUADERE, Old English SWETE and adds the cross-reference 'بازگشت به: شیرین' — the same family Nourai draws.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"xâstan\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"New Persian خواستن, classically xʷāstan, is the direct continuation of MP xwāstan with no change beyond the loss of the labial glide of xʷ- (the so-called vāv-e ma'dūla, still written خوا- but silent from about the 16th-17th c., hence modern xāstan); the present stem خواه xāh continues MP xwāh-. The extras of the box are the regular derivatives: خواست (past stem used as a noun, 'will'), خواستار (agent in -ār, MP xwāstār), خواهش (verbal noun in -išn, MP xwāhišn), خواه (present stem as an independent word); to these Mo'in's footnote at Borhan 783 adds خواسته 'property' = MP xwāstag. The step from MP to NP is beyond doubt; what remains 'plausible' rather than 'confirmed' is only the further step back to the 'sweet' root (see node 2): Horn 110, Hübschmann §92 and Aryanpur take it, Nyberg's *hvāz- and Wiktionary's Proto-Iranian *xwaz- ('of uncertain origin, perhaps ultimately from PIE *sweh₂d-') do not. Note also that the Wiktionary page's only bibliographical reference for this family is Nourai 2011 p. 459 — this very page — so it is no independent witness.\",\n          \"derivation_fa\": \"«خواستن» فارسی نو دنبالهٔ بی‌واسطهٔ xwāstan فارسی میانه است؛ تنها دگرگونی، افتادن «و» معدوله در تلفظ است (در نوشتار هنوز می‌ماند). مادهٔ مضارع «خواه» از xwāh- و مشتقات «خواست، خواستار، خواهش، خواسته» همه از همین ستاک‌ها ساخته شده‌اند (حاشیهٔ معین در برهان قاطع ص ۷۸۳: «خواسته ـ پهلوی xvāstak (مال)»). تا اینجا مسلم است؛ آنچه قطعی نیست رساندن این ستاک به ریشهٔ «شیرین» است که هرن و هوبشمان و آریان‌پور می‌پذیرند و نیبرگ و ویکی‌واژه نمی‌پذیرند. در ضمن تنها مأخذ ویکی‌واژه برای همین خانواده، خود نورایی ص ۴۵۹ است؛ پس گواه مستقل نیست.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%A7%D8%B3%D8%AA%D9%86\"],\n          \"ref_check\": [\n            {\"ref\": \"BQT:783\", \"status\": \"supports\", \"note\": \"BQT_v2_pages.txt leaf 240-241 (running head ۷۸۳) carries خواس، خواستار 'طلبکار و خواهنده', خواسته 'زر و مال و اسباب', with Mo'in's footnotes 'مصدر مرخم «خواستن»', 'از: خواست + ار (پسوند فاعلی)', 'پهلوی xvāstak (مال)' — the Persian word family of the box, on the cited page.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"HRN.txt p. 110, no. 497\", \"stance\": \"supports\", \"note\": \"'xʳāsten „wünschen, wollen“ ... ai. √svad- ... phlv. xʳāstan' — Horn's chain is Nourai's chain.\"},\n            {\"src\": \"HUB\", \"where\": \"HUB.txt leaf 208 = printed p. 198, Kapitel 16 §92\", \"stance\": \"supports\", \"note\": \"'xʳāham „wünsche“, skr. svad' (listed among ap. d > np. h); cf. p. 199 'xʳai (xʳā) „Wohlgeschmack“ = skr. svāda-'.\"},\n            {\"src\": \"MON\", \"where\": \"Mo'in / Borhan footnote, BQT p. 783\", \"stance\": \"supports\", \"note\": \"'پهلوی xvāstak (مال)' and 'از: خواست' for the derivatives — the Persian family is traced to the Pahlavi stem, with no rival etymology proposed.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt, root list *hu-/*Hua-\", \"stance\": \"silent\", \"note\": \"Cheung's EDIV has *huad 'to become, make savoury' and *huah 'to strike, thresh' but no entry containing NP خواستن 'to want'; a grep for xwāstan returns only index lines. His silence is why the arrow is only 'plausible'.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"svad; svâdati\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Vedic svad-/svād- is the Indic reflex of *sweh₂d-, with the expected Indo-Iranian *sw- > Skt. sv-: svadate 'is pleased, enjoys, tastes good' (= Gr. ἥδομαι), causative/intensive svādáyati 'to make savoury, season, relish' (formally = Lat. suādeo), adjective svādú- 'sweet' (= Gr. ἡδύς, Lat. suāvis < *suāduīs), noun svādá- 'taste, good flavour'. Nourai's two entries are slightly loose: 'svad' is the root/verb (not the adjective 'sweet' — that is svādú-), and the gloss 'to desire, want' for svādati is stretched to fit the Persian branch; Klein and Pokorny gloss svadati 'makes savoury' and svadate 'tastes, is savoury'. The forms and the descent are nevertheless entirely correct.\",\n          \"derivation_fa\": \"در سنسکریت ریشهٔ svad-/svād- بازتاب همان *sweh₂d- است (در هندوایرانی *sw- در هندی به sv- می‌ماند): svadate «خوش می‌آید، خوش‌مزه است»، svādáyati «خوش‌مزه کردن» (هم‌ساخت با suādeo لاتین)، صفت svādú- «شیرین» (= hēdýs یونانی، suāvis لاتین). دو نکتهٔ جزئی: «شیرین» معنای svādú- است نه ریشهٔ svad، و معنی «خواستن» که نورایی برای svādati آورده در منابع نیست و برای پیوستن به شاخهٔ فارسی کشیده شده است. در کل، ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"POK:1039\", \"status\": \"supports\", \"note\": \"POK_full.txt, suad-: 'Old Indic svadu-, f. svadvi “sweet, mellifluous” ... Old Indic ved. svadate “is pleased, enjoys” = gr. ἥδομαι ... svadayati (= Latin suadeo) ... Old Indic svada- m. “taste, Wohlgeschmack”.'\"},\n            {\"ref\": \"KLN:1552\", \"status\": \"supports\", \"note\": \"Klein 1966, s.v. sweet (KLN_1966.txt leaf 823, which carries printed pp. 1550/51, i.e. within a page of Nourai's citation): 'fr. I.-E. base *swad- ... whence also OI. svādaḥ “agreeable taste, flavor”, svadati “makes savory”, svadate “tastes, is savory”, svaduḥ “sweet”.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 812, s.v. suave\", \"stance\": \"supports\", \"note\": \"'L. suavis ... stands for *swadwis, and is cogn. with OI. svaduḥ “sweet”, Gk. ἡδύς ... OS. swoti, OE. swete.'\"},\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II 516 f.\", \"stance\": \"supports\", \"note\": \"'Kaus. bzw. Intensivum svadáyati (= lat. suādeo) und svādáyati „schmackhaft, genießbar, annehmbar machen; kosten, genießen“ ... svadati „macht schmackhaft, angenehm, würzt“, svadate „schmeckt, ist schmackhaft“'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt line 9968, *huad\", \"stance\": \"supports\", \"note\": \"'*SANSKRIT: svad “to make, become savoury, taste” (RV+) ⇒ EWAia II: 788'.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Germanic\",\n          \"words\": \"swôtja\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *swōtja- (also *swōtuz) 'sweet' is the regular Germanic outcome of *sweh₂d-u-/-i-: IE ā (< *eh₂) gives Germanic ō, and the IE *-d- becomes Germanic *-t- by Grimm's law, with the i-stem/ja-stem suffix causing i-umlaut in the West Germanic daughters. Hence OE swēte, OS swōti, OHG suoʒi/swuoʒi (> G süß), ON sœtr, Du. zoet. Watkins gives the form letter for letter: 'Germanic *swōtja- in Old English swēte, sweet'.\",\n          \"derivation_fa\": \"صورت ژرمنی آغازین *swōtja- «شیرین» برآیند قاعده‌مند *sweh₂d-u- است: آی درازِ هندواروپایی در ژرمنی به «او» (ō) بدل می‌شود و d بنا بر قانون گریم به t. پسوند -ja- موجب امالهٔ واکه در ژرمنی غربی شده است: انگلیسی کهن swēte، آلمانی کهن suoʒi (آلمانی süß). واتکینز دقیقاً همین صورت را می‌آورد؛ ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/sweet\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 1036: 'swad-. Sweet, pleasant. 1. Germanic *swōtja- in Old English swēte, sweet: SWEET.'\"},\n            {\"ref\": \"KLN:1552\", \"status\": \"supports\", \"note\": \"Klein s.v. sweet (leaf 823, pp. 1550/51): 'ME. swete, swote, fr. OE. swete “sweet, pleasant”, rel. to OS. swoti, ON. sœtr, Swed. söt ... OHG. swuoʒi, suoʒi, MHG. süeʒe, G. süß, fr. I.-E. base *swad-'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 823, s.v. sweet\", \"stance\": \"supports\", \"note\": \"full West/North Germanic cognate list, as quoted.\"},\n            {\"src\": \"WEB\", \"where\": \"etymonline (archived), s.v. sweet\", \"stance\": \"supports\", \"note\": \"'From Old English swete ... from Proto-Germanic *swotja- ... ultimately from PIE root *swad- “sweet, pleasant”.'\"},\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II 516\", \"stance\": \"supports\", \"note\": \"the su̯ādu-s section lists 'Old Saxon swōti, Old High German suozi, Old English swēte, Old Icelandic sœtr “sweet”'.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"sweet\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old English swēte (Mercian swōete) 'pleasing to the senses, mind or feelings' > Middle English swete/swote > Modern English sweet; the OE ē (i-umlaut of ō) gives ME long close e, raised to /iː/ by the Great Vowel Shift, whence the modern pronunciation with the inherited <ee> spelling. The semantic range 'pleasing to the taste' > 'pleasing to the ear' (already OE), 'beautiful, desirable' (mid-14c.), 'gracious, kind' of persons, is entirely native.\",\n          \"derivation_fa\": \"انگلیسی کهن swēte > انگلیسی میانه swete > sweet امروزی؛ واکهٔ بلندِ آن در چرخش بزرگ واکه‌ها به /iː/ بدل شده و املای کهن ee مانده است. گسترش معنایی از «خوش‌مزه» به «خوش‌آهنگ» و «دلپذیر» درون‌زبانی است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/sweet\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the chart cites no reference for this node; the chain is covered by the AHD and KLN citations of its parent.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 823, s.v. sweet\", \"stance\": \"supports\", \"note\": \"'sweet, adj. — ME. swete, swote, fr. OE. swete, “sweet, pleasant”.'\"},\n            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt line 1036 and index line 2328 'SWEET swad-'\", \"stance\": \"supports\", \"note\": \"'Germanic *swōtja- in Old English swēte, sweet: SWEET.'\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Latin\",\n          \"words\": \"suâdĕre; per-suâdere\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin suādēre 'to advise, urge' is a stative/causative in *-eh₁- built on the root: Watkins 'Suffixed form *swād-ē- in Latin suādēre, to advise, urge (< “recommend as good”)', formally the twin of Vedic svādáyati; Klein glosses it literally 'to make tasteful'. Its adjective partner is suāvis 'sweet, pleasant' < *suāduīs, with regular loss of intervocalic -d- before -u-. per-suādēre prefixes per- 'thoroughly, to the end' (an intensive, as Nourai says), hence 'to make a thing thoroughly agreeable to someone' > 'to convince'. The Latin family also gives suasion, dissuade, assuage, and (through Italian) soave.\",\n          \"derivation_fa\": \"لاتین suādēre «پند دادن، ترغیب کردن» فعلی است با پسوند *-eh₁- بر همان ریشه، هم‌ساخت با svādáyati سنسکریت؛ معنای تحت‌اللفظی آن «چیزی را خوش‌مزه/دلپذیر کردن» است (کلاین). صفت هم‌ریشهٔ آن suāvis < *suāduīs است با افتادن قاعده‌مند d میان‌واکه‌ای. per- پیشوند تأکیدی «کاملاً» است، پس per-suādēre = «کاملاً متقاعد کردن». ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/persuade\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 1036: '2. Suffixed form *swād-ē- in Latin suādēre, to advise, urge (< “recommend as good”): SUASION; (ASSUASIVE), DISSUADE, PERSUADE.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 812 s.v. suave; leaf 621 s.v. persuade\", \"stance\": \"supports\", \"note\": \"'L. suavis ... stands for *swadwis'; 'persuade ... F. persuader, fr. L. persuadere, “to persuade, convince”, fr. per- and suadere, “to advise”. See suave.'\"},\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II 517\", \"stance\": \"supports\", \"note\": \"'Kaus. bzw. Intensivum svadáyati (= lat. suādeo)'.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"English\",\n          \"words\": \"persuade\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English persuade is a 1510s borrowing, either directly from Latin persuādēre or through Old/Middle French persuader, in the sense 'lead to the opinion or conclusion, make (one) believe'. The -uādēre stem shows up in the English family as -suade/-suasion (dissuade, suasion, persuasion < L. persuāsiōnem).\",\n          \"derivation_fa\": \"واژهٔ انگلیسی persuade در حدود سال ۱۵۱۰ میلادی از لاتین persuādēre (یا از راه فرانسهٔ persuader) وام گرفته شده است؛ وام‌واژه‌ای کتابی است نه میراثی. هم‌خانواده‌های آن dissuade و persuasion اند. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/persuade\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference cited on this node; covered by the AHD citation of the Latin parent.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 621, s.v. persuade\", \"stance\": \"supports\", \"note\": \"'persuade, tr. v., — F. persuader, fr. L. persuadere, “to persuade, convince”, fr. per- and suadere, “to advise”.'\"},\n            {\"src\": \"WEB\", \"where\": \"etymonline (archived), s.v. persuade\", \"stance\": \"supports\", \"note\": \"'from Latin persuadere “bring over by talking” ... per- “thoroughly, strongly” + suadere “to urge, persuade”, from PIE root *swad- “sweet, pleasant”; entered English 1510s via Old French persuader.'\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 3,\n      \"root\": \"Swei; Sweib\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"PIE *su̯ē(i)- 'to bend, turn, swing', with the extension *su̯eib-/*su̯eip- (Pokorny 1041-1042; Watkins swei-2)\",\n      \"note\": \"Pokorny's entry on the cited page is 'Root/lemma: su̯ē(i)-, Meaning: to bend, turn, swing ... Page(s): 1041-1042', and it contains precisely the sub-root 'su̯eib-: Avestan xšvaewayat-astra- „die Peitsche schwingend“, xšvi(b)wa- „agile“; Gothic midja-sweipains; Old English swāpan “swing, sweep” ...' as well as su̯eip- (OE swīfan, engl. swift). Watkins: 'swei-2. To bend, turn. [Pok. swei- 1041.]'. So root name, page and the pairing Swei/Sweib are right. Two reservations: (a) the second gloss 'move swiftly like a snake' is not in Pokorny — Nourai has read it back out of the Avestan phrase azayō xšvaewaŋhō 'swiftly darting snakes' (Vd 18.65), which is indeed where Persian شیبا comes from, but it is a Nourai gloss, not a reconstructed meaning; (b) Pokorny has a homonymous su̯ei- 'to whistle, hiss' on pp. 1040-41 (Watkins swei-1, Lat. sibilare) which is a different root and must not be confused with this one.\",\n      \"note_fa\": \"ریشهٔ پوکورنی در صفحهٔ ۱۰۴۱–۱۰۴۲ همان su̯ē(i)- «خم کردن، گرداندن، جنباندن» است با گسترش‌های su̯eib- و su̯eip-؛ پس نام و شمارهٔ صفحهٔ نورایی درست است. دو نکته: نخست آنکه معنای دوم «تند خزیدن مانند مار» در پوکورنی نیست و نورایی آن را از عبارت اوستایی azayō xšvaewaŋhō «مارهای تندجهنده» (وندیداد ۱۸،۶۵) بیرون کشیده است؛ دوم آنکه پوکورنی ریشهٔ هم‌نگار دیگری su̯ei- «سوت زدن، فیش کردن» در ص ۱۰۴۰–۴۱ دارد که ربطی به این ریشه ندارد. در مجموع ریشه با احتیاط پذیرفتنی است.\",\n      \"sources\": [\"https://www.etymonline.com/word/sweep\"],\n      \"ref_check\": [\n        {\"ref\": \"POK:1041\", \"status\": \"supports\", \"note\": \"POK_full.txt lines 84355-84430: 'Root / lemma: su̯ē(i)- — Meaning: to bend, turn, swing ... su̯eib-: Avestan xšvaewayat-astra- „die Peitsche schwingend“, xšvi(b)wa- „agile“; Gothic midja-sweipains ... Old English swāpan “swing, sweep, wash away, drive, push” ... su̯eip-: Old Icelandic svīfa ... Old English swīfan “turn, sweep” (engl. swift “quick, fast”) ... Page(s): 1041-1042.'\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II 520\", \"stance\": \"supports\", \"note\": \"'su̯eip: aisl. svīfa „schwingen, drehen, umherschweifen“, ags. swīfan (engl. swift „schnell“) ... su̯eib-: got. midjasweipains „Sintflut“ (eig. „Fegung der Mitte“) ... ags. swāpan „schwingen, fegen“ ... av. xšvaewayat-astra- „die Peitsche schwingend“.'\"},\n        {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt line 1043\", \"stance\": \"supports\", \"note\": \"'swei-2. To bend, turn. 1. Germanic o-grade form *swaip- in Old English swāpan, to sweep, drive, swing: SWOOP ... [Pok. swei- 1041.]'\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"xšvira; xšvaewa\",\n          \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"xšvira\",\n          \"correct_form\": \"xšviwra-\",\n          \"derivation\": \"The second word is right, the first is a misprint. (a) Av. xšvaewa- is exactly what Bartholomae (AiW col. 860) gives: 'j. xšvaewa- 1) Adj. „sich rasch schwingend, schnellend“: azayō xšvaewaŋhō „sich rasch (im Bogen) schnellende Schlangen“ V.18.65; — tištrim .. yō avavat xšvaewa vataite .. yaθa tiγriš “.. der ebenso rasch dahinfliegt .. wie der Pfeil” Yt 8.6. 2) m. „rascher Schwung“. Pü.: šēpāk.' It is a *-u̯o- adjective of the su̯eib- extension (*su̯eib-u̯o- > Ir. xšvaiwa- with the regular Av. treatment of *su̯- as xšv-). (b) 'xšvira' is not an attested Avestan word. What is meant is xšviwra- (Bartholomae col. 864): 'j. xšviwra- Adj. „schnell, flink, geläufig“: dāiia mē .. mastīm spānō xšviwrəm hizụụẹm uruụē uši “gib mir .. eine flinke Zunge, der Seele Auffassungskraft” Y 62.4. Pü.: šēpāk.' The -w- has simply dropped out of Nourai's transliteration; this is important because xšviwra- of the 'nimble tongue' is the direct semantic ancestor of Persian شیوا 'eloquent', while xšvaewa- of the darting snakes is that of شیبا 'viper'. The printed page 459 itself reads 'xšvira', so the extraction is faithful and the error is the book's.\",\n          \"derivation_fa\": \"از دو صورت این خانه، دومی درست است و اولی غلط چاپی. xšvaewa- «تندجهنده، چالاک» در بارتولومه (ستون ۸۶۰) آمده است، از جمله در azayō xšvaewaŋhō «مارهای تندجهنده» (وندیداد ۱۸،۶۵)؛ این صفت از گسترش su̯eib- ساخته شده و *su̯- هندواروپایی در اوستایی قاعده‌مند به xšv- بدل می‌شود. اما «xšvira» صورتی اوستایی نیست؛ مقصود xšviwra- «تند، چالاک، روان» (بارتولومه ستون ۸۶۴، یسنا ۶۲،۴: «زبانی چالاک به من بخش») است که در ترجمه‌نویسی «w» آن افتاده است. این نکته مهم است زیرا xšviwra- (زبان چالاک) پیشینهٔ معنایی «شیوا» است و xšvaewa- (مار جهنده) پیشینهٔ «شیبا». در صفحهٔ چاپی کتاب (ص ۴۵۹) هم «xšvira» چاپ شده؛ پس خطا از خود کتاب است نه از خوانش اسکن.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"POK:1041\", \"status\": \"partial\", \"note\": \"POK_full.txt, su̯eib- section: 'Avestan xšvaewayat-astra- „die Peitsche schwingend“, xšvi(b)wa- „agile“' — supports xšvaewa- (via its compound) and knows xšviwra- only in the form xšvi(b)wa-; there is no 'xšvira' anywhere in Pokorny.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"BRT.txt line 10945 (col. 860) and line 11000 (col. 864)\", \"stance\": \"supports\", \"note\": \"col. 860 'j. xšvaewa- 1) Adj. „sich rasch schwingend, schnellend“: azayō xšvaewaŋhō ... V.18.65 ... Pü.: šēpāk'; col. 864 'j. xšviwra- Adj. „schnell, flink, geläufig“: dāiia mē .. mastīm spānō xšviwrəm hizụẹm uruụē uši ... Y.62.4 ... Pü.: šēpāk' — the correct form, with the same Pahlavi gloss.\"},\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II 520\", \"stance\": \"partial\", \"note\": \"under su̯eib- only 'av. xšāewayat-astra- „die Peitsche schwingend“ u. dgl. (s. u. u̯eip-)'; no xšvira.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"šĕpâk\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Šēpāk is a Zand gloss word, not a word of the ordinary Pahlavi lexicon (MacKenzie's CPD has no šēb-/šēw- entry). It is the Pahlavi rendering that the Zand puts on BOTH Avestan adjectives of the parent node: Bartholomae notes 'Pü.: šēpāk' under xšvaewa- (col. 860) and again under xšviwra- (col. 864). Written <šypʾk>, the letter transliterated p regularly stands for /w/ between vowels in Book Pahlavi, so Horn reads it šēvak / šēvāk (Grundriss nos. 800, 804: 'phlv. š(e)pāk d. i. š(e)vak'), and it is that reading, not the graphic šēpāk, which yields NP شیبا/شیوا. The suffix -āk/-ak is the ordinary MP adjectival formant on an Avestan stem *šēw- < xšvaiw-. Nourai's gloss 'fast, easy to understand' is a conflation: the Pahlavi word means only 'swift, darting/nimble'; 'easy to understand' is the later Persian sense of شیوا read back into it.\",\n          \"derivation_fa\": \"«شــــــــــــــــــــــــــیپاک» (شِیوک/شیواک) واژه‌ای است از زند، نه از فرهنگ معمول پهلوی (در مکنزی نیست). بارتولومه ذیل هر دو صفت اوستایی xšvaewa- و xšviwra- می‌نویسد «Pü.: šēpāk». در خط پهلوی حرف p میان دو واکه قاعده‌مند به /w/ خوانده می‌شود؛ پس هرن آن را شیوک/شیواک می‌خواند و همین خوانش است که به «شیبا/شیوا» می‌رسد. پسوند -ak/-āk پسوند صفتساز معمول فارسی میانه است. معنای «زودفهم» که نورایی آورده از آن پهلوی نیست بلکه معنای متأخرِ «شیوا» در فارسی است. در مجموع با احتیاط پذیرفتنی است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1319,1329\", \"status\": \"supports\", \"note\": \"BQT_v3_pages.txt pdf p. 110 = printed p. 1319, Mo'in's footnote 1 to شیبا: 'اوستا xšvaewa، پهلوی شیپاک (šēpāk)، شیوک (šēvak) ... قس بلوچی شیپ‌مار (نوعی مار) ... رک: هوبشمان ۸۰۰' — the Pahlavi form and both readings, exactly as in the chart.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"BRT.txt col. 860 (xšvaewa-) and col. 864 (xšviwra-)\", \"stance\": \"supports\", \"note\": \"both entries close with 'Pü.: šēpāk' (col. 864 adds the note that 'šēpāk xāirvān' is explained elsewhere) — the Pahlavi word is the Zand gloss of both Avestan adjectives.\"},\n            {\"src\": \"HRN\", \"where\": \"HRN.txt pp. 178 and 179, nos. 800 and 804\", \"stance\": \"supports\", \"note\": \"no. 800 'šēbā “Viper”. aw. xšvaewa- (vd. 18, 65); phlv. š(e)pāk d. i. š(e)vak'; no. 804 'šēvā „beredt“. aw. xšvaewa- „schnell, schnellend“; phlv. šepāk d. i. ševāk'.\"},\n            {\"src\": \"PHD\", \"where\": \"PHD.txt / PHD_mackenzie.txt\", \"stance\": \"silent\", \"note\": \"grep '^šēb|^šēw|^šyb' finds nothing: the word is not in MacKenzie's Concise Pahlavi Dictionary, which is expected for a Zand gloss.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"šîbâ; šîvâ\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Both Persian words continue Pahlavi šēwāk/šēvak (written šēpāk) with the ordinary loss of the MP -k/-g ending, and they differ only in the spelling of the medial glide, ب vs و, both standing for /w/ ~ /v/. (a) شیبا 'viper, big snake' — Horn no. 800 (p. 178) 'šēbā “Viper”, aw. xšvaewa- (vd. 18, 65)'; the Avestan passage cited is exactly azayō xšvaewaŋhō 'swiftly darting snakes', so the noun is an elliptical use of the adjective ('the darting one' = the viper), paralleled by Balochi šēp-mar 'a kind of snake' (Mo'in's footnote, Borhan p. 1319), and attested in Gorgāni's Vīs o Rāmīn: 'سر دیوار او پر مار شیبا'. (b) شیوا 'eloquent, clear' — Horn no. 804 (p. 179) 'šēvā „beredt“, aw. xšvaewa- „schnell, schnellend“; phlv. šepāk d. i. ševāk'; the semantic bridge is the Avestan xšviwrəm hizu̯ẹm 'nimble tongue' of Y 62.4, i.e. 'quick-tongued' > 'fluent' > 'clear, easy to follow'. Mo'in's dictionary glosses شیوا 'فصیح، بلیغ'. The reservation: Wiktionary derives شیوا instead from the native stem شیو (šiv) + the adjectival ـا, i.e. from شیفتن/شیویدن 'to stir up, disturb' — and Borhan indeed prints شیوا 'فصیح بلیغ' right beside شیوانیدن 'آمیختن، برهم زدن' and شیوان 'آمیخته', a homonym cluster that makes a folk-etymological pull on the word likely. So Nourai follows Horn, Hübschmann and Mo'in, which is respectable, but the derivation of شیوا is not uncontested; شیبا is the safer of the two.\",\n          \"derivation_fa\": \"هر دو واژه دنبالهٔ پهلوی شیواک/شیوک اند با افتادن قاعده‌مند پایانهٔ -ک فارسی میانه؛ تفاوت «ب» و «و» تنها دو نگارش از یک همخوان /w/ است. «شیبا» به معنی مار و افعی، به گواهی هرن (بند ۸۰۰) و حاشیهٔ معین بر برهان قاطع (ص ۱۳۱۹)، از همان صفت اوستایی xšvaewa- است که در وندیداد ۱۸،۶۵ وصف مارهاست (قس: بلوچی شیپ‌مار)؛ شاهد فارسی آن بیت فخرالدین گرگانی است: «سر دیوار او پر مار شیبا». «شیوا» به معنی فصیح و بلیغ را هرن (بند ۸۰۴) از همین خانواده می‌داند و پل معنایی آن ترکیب اوستایی xšviwrəm hizu̯ẹm «زبان چالاک» (یسنا ۶۲،۴) است. با این همه، ویکی‌واژه «شیوا» را از ستاک بومی «شیو» (از شیفتن/شیویدن) + «ـا» می‌داند، و در برهان قاطع نیز همین صفحه «شیوان، شیوانیدن» به معنی «آمیختن، برهم زدن» آمده است؛ پس احتمال ریشه‌شناسی عامیانه هست. در مجموع، «شیبا» استوارتر است و «شیوا» با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B4%DB%8C%D9%88%D8%A7\"],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1319,1329\", \"status\": \"supports\", \"note\": \"printed p. 1319 (BQT_v3_pages.txt pdf p. 110): 'شیبا ... مار افعی را گویند' with Mo'in's footnote 'اوستا xšvaewa، پهلوی شیپاک/شیوک ... خشوئو در اوستا صفت است بمعنی زودخزنده، تندرونده، چست و چالاک' + the Vīs o Rāmīn verse. شیوا with Horn's etymology stands on pdf p. 122 of the same scan (≈ printed 1331, two pages past Nourai's 1329 — the v3 scan has some mis-ordered leaves): 'شیوا ... بمعنی فصیح بلیغ باشد' with the footnote 'بقول هرن اوستا xšvaewa (تند، سریع)؛ پهلوی شیپاک و شیوک ... و بقول هوبشمان ...'.\"},\n            {\"ref\": \"HRN:178,179\", \"status\": \"supports\", \"note\": \"HRN.txt leaves 199-200 = printed pp. 178-179: no. 800 'šēbā „Viper“. aw. xšvaewa- (vd. 18, 65); phlv. š(e)pāk d. i. š(e)vak' and no. 804 'šēvā „beredt“. aw. xšvaewa- „schnell, schnellend“; phlv. šepāk d. i. ševāk' — both words, both pages, exactly as cited.\"},\n            {\"ref\": \"MON:2115\", \"status\": \"supports\", \"note\": \"Mo'in, Farhang-e Fārsi s.v. شیوا (MON_part1.txt line 88347): 'شیوا (ص.) فصیح، بلیغ' — the gloss of the chart. The local MON OCR has no page tags, so the page number 2115 itself could not be verified.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"HRN.txt pp. 178-179, nos. 800, 804\", \"stance\": \"supports\", \"note\": \"as quoted; Horn is the ultimate source of Mo'in's footnote and of Nourai's arrow.\"},\n            {\"src\": \"BQT\", \"where\": \"BQT_v3_pages.txt pdf pp. 110 and 122\", \"stance\": \"supports\", \"note\": \"both headwords with Mo'in's Avestan/Pahlavi footnotes, plus the Balochi comparison شیپ‌مار.\"},\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt lines 88347-88351\", \"stance\": \"partial\", \"note\": \"'شیوا (ص.) فصیح، بلیغ' is followed immediately by 'شیوانیدن (مص م.) آمیختن، برهم زدن ... لرزانیدن' — the homonym cluster that gives Wiktionary its alternative derivation.\"},\n            {\"src\": \"WEB\", \"where\": \"en.wiktionary.org s.v. شیوا (archived)\", \"stance\": \"partial\", \"note\": \"'From شیو (šiv) + ـا (-ā), adjective form of the verb شیفتن (šiftan) “to disturb, to disorder, to confuse”' — a native derivation, competing with Horn's Avestan one.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Germanic\",\n          \"words\": \"swîp; swîf\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"These are the two Germanic ablaut grades of the su̯eib-/su̯eip- extension. Watkins states them explicitly under swei-2: 'Germanic o-grade form *swaip- in Old English swāpan, to sweep, drive, swing: SWOOP. 2. Germanic zero-grade form *swip- in Old English swift, swift, quick (< “turning quickly”). 3. Germanic full-grade form *swif- in Middle English swyvel, a swivel.' Walde-Pokorny II 520 lists the same material under su̯eip- (aisl. svīfa, ags. swīfan, engl. swift, ahd. sweibōn) and su̯eib- (got. midja-sweipains 'deluge', lit. 'sweeping of the middle', ags. swāpan, ahd. sweif 'Umschwung, Schwanz'). Nourai's *swīp 'sweep' and *swīf 'fast move' are these; the only inexactness is the vowel — the 'sweep' grade is o-grade *swaip- (OE swāpan), not *swīp-.\",\n          \"derivation_fa\": \"این دو صورت، دو پایهٔ آوایی (ablaut) گسترش su̯eib-/su̯eip- در ژرمنی اند: واتکینز صریحاً *swaip- (> انگلیسی کهن swāpan «روفتن، چرخاندن»)، *swip- (> swift) و *swif- (> swivel) را می‌آورد و والده‌پوکورنی (جلد ۲ ص ۵۲۰) همین ماده را. تنها نادقتی نورایی در واکه است: پایهٔ «روفتن» درواقع *swaip- است نه *swīp-. در کل ادعا درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/sweep\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 1043, s.v. swei-2, as quoted: *swaip-, *swip-, *swif- with sweep/swoop, swift and swivel.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II 520\", \"stance\": \"supports\", \"note\": \"'su̯eip: aisl. svīfa „schwingen, drehen“, ags. swīfan „bewegen, fegen“ (engl. swift „schnell“) ... su̯eib-: got. midjasweipains ... ags. swāpan „schwingen, fegen, streichen (vom Winde)“ ... ahd. sweif „Umschwung, Schwanz“'.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 823 s.v. sweep; leaf 823 s.v. swivel\", \"stance\": \"supports\", \"note\": \"'sweep ... ME. swepen ... rel. to OE. swāpan, “to swoop”'; 'swivel, n. — ME. swivell, rel. to OE. swifan, “to move in a course, sweep”.'\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"sweep; swift, swap, sway, swivel\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Three of the five are secure, two are looser. sweep: ME swepen (early 14c.), a weak verb beside/replacing OE swāpan (past swēop); Skeat calls it 'the regular causal form of A.S. swāpan, to swoop', Klein 'rel. to OE. swāpan'. swift: OE swift 'moving quickly', from the zero grade *swip- 'turning quickly' (Watkins). swivel: ME swivell, from OE swīfan 'to move in a course, sweep' + the instrumental -el suffix (Klein), Germanic *swif-. swap: Watkins does list SWAP under swei-2 ('German schwappen, to flap, splash, akin to the source of Middle English swappen, to splash'), but the word's early sense in English is 'to strike, to hit' (c. 1200) and Etymonline and most modern accounts treat it as imitative, the trading sense coming from 'striking hands' on a bargain — so the connection is possible, not certain. sway: this one does not come from Nourai's Germanic *swīp/*swīf at all; ME sweyen (early 14c.) is from a Scandinavian source, cf. Old Norse sveigja 'to bend, swing, give way', i.e. Pokorny's su̯eig-/su̯eik- extension on pp. 1041-42. It belongs in the same root box but on a different branch, so the arrow as drawn is wrong for that word.\",\n          \"derivation_fa\": \"از پنج واژه، سه تا قطعی اند: sweep از انگلیسی میانه swepen در کنار انگلیسی کهن swāpan، swift از پایهٔ صفر *swip- «تندچرخنده»، و swivel از swīfan «گردیدن، روفتن». دربارهٔ swap واتکینز آن را زیر همین ریشه می‌آورد ولی ریشه‌شناسی امروزی آن را آوابند (تقلید صدای ضربه) می‌داند. اما sway از شاخهٔ *swīp/*swīf نیست؛ آن وام‌واژه‌ای اسکاندیناویایی است از نورس کهن sveigja «خم کردن، جنباندن»، یعنی از گسترش su̯eig-/su̯eik- همان ریشه. پس خانه در کل درست است ولی دو واژهٔ آخر با احتیاط.\",\n          \"sources\": [\"https://www.etymonline.com/word/sweep\", \"https://www.etymonline.com/word/sway\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference is cited on this node; its parent carries 'AHD', whose swei-2 entry covers sweep/swoop, swift, swivel and swap but not sway.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 823, s.vv. sweep, swift, swivel\", \"stance\": \"supports\", \"note\": \"'sweep ... ME. swepen, “to sweep, move quickly”, rel. to OE. swāpan, “to swoop”'; 'swift, n. ... fr. swift, adj.'; 'swivel ... rel. to OE. swifan, “to move in a course, sweep”. See sweep, v.'\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt line 19006, s.v. sweep\", \"stance\": \"supports\", \"note\": \"'sweep, verb. (E) M.E. swipen. A weak verb ... the regular causal form of A.S. swāpan, to swoop (above).'\"},\n            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt line 1043 and index line 2328\", \"stance\": \"partial\", \"note\": \"swei-2 yields SWOOP, SWIFT, SWIVEL, SWITCH, SWAP; SWAY is indexed at 'SWAG sweng(w)-'-adjacent entries and is not listed under swei-2.\"},\n            {\"src\": \"WEB\", \"where\": \"etymonline (archived), s.vv. sweep, sway\", \"stance\": \"partial\", \"note\": \"sweep: 'from Old English swāpan'; sway: 'probably from a Scandinavian source, cf. Old Norse sveigja “to bend, swing, give way”' — a different Germanic stem from *swīp/*swīf.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-489.json > /dev/null && echo \"JSON OK\""
}
```


### [2026-09-14T03:32:25.011Z] TOOL RESULT

```
JSON OK
```


## [2026-09-14T03:32:25.632Z] AGENT

You've hit your session limit · resets 2:50am (America/Toronto)
