# Verification process log — verify-page-89


## [2026-09-05T13:45:18.587Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 89 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-89.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-89.json. Write /home/sfmqrb/git/rishe/data/verification/page-89.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 89` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T13:45:20.116Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T13:45:20.825Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T13:45:20.838Z] TOOL RESULT

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


## [2026-09-05T13:45:21.023Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-89.txt"
}
```


### [2026-09-05T13:45:21.036Z] TOOL RESULT

```
1	=== PDF page 89 (book page 59) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Bher 1, Bhrâ-tar : Bher 1: to carry. Bhrâ-tar: load carrier (of family), brother ☞ Ter 3  (refs POK:128,163; KAS:10; PRT:234; SYN:107)  PART 2
4	#1 (parent #0) [Old Persian] refs=POK:128 | bar : to carry, ride a horse
5	  #2 (parent #1) [Old Persian] refs=KNT:200 | â-bar : perform ; pati-â-bar : bring back, restore ☞Per 3 ; parâ-bar : take away ☞Per 1 ; pari-bar : protect, preserve ☞Per1 ; fra-bar : grant ☞Per 1
6	#3 (parent #0) [Greek] refs=AHD | pherein : to carry ; phôs-phoros : light bearing (substance) ☞Bhâ 1
7	  #4 (parent #3) [French] refs=AHD | phosphore
8	    #5 (parent #4) [Persian] refs=MON:2546 | fosfor «فسفر» | extra: فسفات
9	    #6 (parent #4) [English] refs=AHD:986 | phosphor
10	#7 (parent #0) [Avestan] refs=POK:163; KLN:204 | brâtar : brother
11	  #8 (parent #7) [Persian] refs=HRN:45 | barâdar «برادر» : brother
12	#9 (parent #0) [Sogdian] refs=SOD:107 | br`t : brother
13	#10 (parent #0) [Germanic] refs=AHD; KLN:203 | beran, burthiz, bur, brengan ; brôthar : brother
14	  #11 (parent #10) [English] refs=None | bear 1, birth, burden, bring ; brother
15	#12 (parent #0) [Latin] refs=AHD | ferre : to carry ; frater : brother
16	  #13 (parent #12) [English] refs=None | defer, differ, fertile, offer, prefer, refer, suffer, transfer ; fraternity
17	#14 (parent #0) [Indo-European] refs=IEC:19 | Ambhô-Bhor, Ambhor : a two-handed tool for carrying (hot) objects ☞Ambhi
18	  #15 (parent #14) [Persian] refs=IEC:19 | ambor «انبر» : pliers | extra: انبره ، انبردست
19	--- entry 1 ---
20	ROOT [Indo-European] Bher 2 : to cook  (refs POK:137)
21	#1 (parent #0) [Old Persian] refs=POK:137; BQT:270; HRN:47 | braij : to cook, fry
22	  #2 (parent #1) [Pahlavi] refs=SNS:103; BQT:270 | brištag : roasted ; brějan : fry roast
23	    #3 (parent #2) [Persian] refs=MON; BQT:255,270; AEF:256; FFD:37 | beresteh «برشته» : roasted, toasted ; beryân «بریان» : roasted ; berîjab «بریجب» : baking oven | extra: برشتن ؛ بریز ، بریزن
24	#4 (parent #0) [Latin] refs=AHD | frîgere : to roast
25	  #5 (parent #4) [English] refs=None | fry
26	
```


## [2026-09-05T13:45:24.835Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-89.json",
 "description": "Read source JSON for page 89"
}
```


### [2026-09-05T13:45:24.879Z] TOOL RESULT

```
{
  "pdf_page": 89,
  "book_page": 59,
  "entries": [
    {
      "root": {
        "name": "Bher 1, Bhrâ-tar",
        "lang": "Indo-European",
        "refs": "POK:128,163; KAS:10; PRT:234; SYN:107",
        "gloss": "Bher 1: to carry. Bhrâ-tar: load carrier (of family), brother ☞ Ter 3"
      },
      "part": 2,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "POK:128",
          "words": [
            {"translit": "bar", "gloss": "to carry, ride a horse", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Old Persian",
          "refs": "KNT:200",
          "words": [
            {"translit": "â-bar", "gloss": "perform", "script": null},
            {"translit": "pati-â-bar", "gloss": "bring back, restore", "script": null, "see": ["Per 3"]},
            {"translit": "parâ-bar", "gloss": "take away", "script": null, "see": ["Per 1"]},
            {"translit": "pari-bar", "gloss": "protect, preserve", "script": null, "see": ["Per1"]},
            {"translit": "fra-bar", "gloss": "grant", "script": null, "see": ["Per 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "pherein", "gloss": "to carry", "script": null},
            {"translit": "phôs-phoros", "gloss": "light bearing (substance)", "script": null, "see": ["Bhâ 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "French",
          "refs": "AHD",
          "words": [
            {"translit": "phosphore", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON:2546",
          "words": [
            {"translit": "fosfor", "gloss": null, "script": "فسفر"}
          ],
          "script_extra": "فسفات",
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 4,
          "lang": "English",
          "refs": "AHD:986",
          "words": [
            {"translit": "phosphor", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:163; KLN:204",
          "words": [
            {"translit": "brâtar", "gloss": "brother", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "HRN:45",
          "words": [
            {"translit": "barâdar", "gloss": "brother", "script": "برادر"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:107",
          "words": [
            {"translit": "br`t", "gloss": "brother", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD; KLN:203",
          "words": [
            {"translit": "beran, burthiz, bur, brengan", "gloss": null, "script": null},
            {"translit": "brôthar", "gloss": "brother", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "bear 1, birth, burden, bring", "gloss": null, "script": null},
            {"translit": "brother", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "ferre", "gloss": "to carry", "script": null},
            {"translit": "frater", "gloss": "brother", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "defer, differ, fertile, offer, prefer, refer, suffer, transfer", "gloss": null, "script": null},
            {"translit": "fraternity", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 0,
          "lang": "Indo-European",
          "refs": "IEC:19",
          "words": [
            {"translit": "Ambhô-Bhor, Ambhor", "gloss": "a two-handed tool for carrying (hot) objects", "script": null, "see": ["Ambhi"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "Persian",
          "refs": "IEC:19",
          "words": [
            {"translit": "ambor", "gloss": "pliers", "script": "انبر"}
          ],
          "script_extra": "انبره ، انبردست",
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Bher 2",
        "lang": "Indo-European",
        "refs": "POK:137",
        "gloss": "to cook"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "POK:137; BQT:270; HRN:47",
          "words": [
            {"translit": "braij", "gloss": "to cook, fry", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "SNS:103; BQT:270",
          "words": [
            {"translit": "brištag", "gloss": "roasted", "script": null},
            {"translit": "brějan", "gloss": "fry roast", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON; BQT:255,270; AEF:256; FFD:37",
          "words": [
            {"translit": "beresteh", "gloss": "roasted, toasted", "script": "برشته"},
            {"translit": "beryân", "gloss": "roasted", "script": "بریان"},
            {"translit": "berîjab", "gloss": "baking oven", "script": "بریجب"}
          ],
          "script_extra": "برشتن ؛ بریز ، بریزن",
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "frîgere", "gloss": "to roast", "script": null}
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
            {"translit": "fry", "gloss": null, "script": null}
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


## [2026-09-05T13:45:25.358Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ && sed -n 1,200p data/verification/sources/SOURCE_MATRIX.md",
 "description": "List verification dir and read source matrix"
}
```


### [2026-09-05T13:45:25.408Z] TOOL RESULT

```
agent
page-101.json
page-126.json
page-311.json
page-31.json
page-32.json
page-33.json
page-345.json
page-34.json
page-35.json
page-36.json
page-37.json
page-38.json
page-39.json
page-40.json
page-41.json
page-42.json
page-43.json
page-44.json
page-45.json
page-46.json
page-47.json
page-48.json
page-49.json
page-50.json
page-51.json
page-52.json
page-53.json
page-54.json
page-55.json
page-56.json
page-57.json
page-58.json
page-59.json
page-60.json
page-61.json
page-62.json
page-63.json
page-64.json
page-65.json
page-66.json
page-67.json
page-68.json
page-69.json
page-70.json
page-71.json
page-72.json
page-73.json
page-74.json
page-75.json
page-76.json
page-77.json
page-78.json
page-79.json
page-80.json
page-81.json
page-82.json
page-83.json
page-84.json
page-85.json
page-86.json
process
sources
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


## [2026-09-05T13:45:30.061Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-86.json'))\nprint(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:4000])\n\"",
 "description": "Inspect a recent verified page for style"
}
```


### [2026-09-05T13:45:31.715Z] TOOL RESULT

```
{
 "entry": 0,
 "root": "Bhen",
 "verdict": "plausible",
 "modern_form": "PIE *bʰen- 'to strike, wound' (Pokorny 126) — today generally merged into *gʷʰen- 'to strike, kill'",
 "note": "Pokorny IEW p. 126 really has 'bhen- ‚schlagen, verwunden‘; auch von durch den Schlag böser Geister bewirkter Krankheit (avest.)', with exactly the two branches Nourai draws: Av. bǎanayən / banta- and Gothic banja, ON bani, OE bana, OHG bano, plus 'vielleicht auch mhd. bane, ban ... ‚Bahn, Weg‘ als ‚*Durchhau durch einen Wald‘'. So the language label ('Indo-European'), the shape of the root and the gloss 'to strike' are Pokorny's own. What has changed since 1959: Watkins (AHD app.) files the whole Germanic family under gʷhen-¹ 'to strike, kill' (bracket: '[Pok. 2. gʷhen-(2)- 491, bhen- 126]'), and Wiktionary/Kroonen derive PGmc *banô 'slayer' from *gʷʰon-ō, *banō 'cleared path' from *gʷʰon-eh₂, since word-initial *gʷʰ- regularly gives Germanic b-. Under that analysis a separate *bʰen- is not needed, and Etymonline says bane has 'no certain IE etymology'. The root box is therefore correct as Pokorny, but superseded.",
 "note_fa": "«Bhen» ریشه‌ای است که پوکورنی در صفحهٔ ۱۲۶ فرهنگ ریشه‌شناسی هندواروپایی خود با معنای «زدن، زخم کردن» آورده است؛ گواه‌های آن تنها اوستایی (ban- «بیمار شدن») و ژرمنی (گوتی banja «زخم، ضربه») است، و پوکورنی خود معنای «بیماری» را به باور کهن ایرانی دربارهٔ «ضربهٔ دیوان» بازمی‌گرداند. ریشه‌شناسی امروزی (واتکینز در پیوست AHD، ویکی‌واژه، کرونن) مواد ژرمنی را ذیل ریشهٔ *gʷʰen- «زدن، کشتن» می‌نهد، زیرا *gʷʰ- آغازین در ژرمنی به b بدل می‌شود؛ بدین‌سان به ریشهٔ جداگانهٔ *bʰen- نیازی نیست. پس عنوان و معنای ریشه با پوکورنی می‌خواند، اما پژوهش امروزی آن را در ریشه‌ای دیگر ادغام کرده است؛ ادعای نورایی با احتیاط پذیرفتنی است.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7%CA%B0en-",
  "https://www.etymonline.com/word/bane"
 ],
 "ref_check": [
  {
   "ref": "POK:126",
   "status": "supports",
   "note": "POK_01.txt line 1774 (leaf = p+8, the '126' page marker stands a few lines above): 'bhen- ‚schlagen, verwunden‘; auch von durch den Schlag böser Geister bewirkter Krankheit (avest.) ... Av. bqnayan ‚sie machen krank‘, banta- ‚erkrankt, siech‘; got. banja ‚Schlag, Wunde, Geschwür‘ ... vielleicht auch mhd. bane, ban ... ‚Bahn, Weg‘ ... WP. II 149'. Root, language and gloss are exactly Nourai's."
  }
 ],
 "consulted": [
  {
   "src": "POK",
   "where": "IEW p. 126 (POK_01.txt:1774)",
   "stance": "supports",
   "note": "'bhen- ‚schlagen, verwunden‘' with the Avestan, Germanic and MHG material of the whole chart."
  },
  {
   "src": "WLD",
   "where": "Bd. II p. 149 (WLD_Bd2_pages.txt:9706-9716, OCR reads the lemma as 'bheu-')",
   "stance": "supports",
   "note": "Same article as Pokorny's, Walde-Pokorny's own wording: 'Av. bqnayon ‚sie machen krank‘ ... got. banja ... vielleicht auch mhd. bane, ban ... ‚Durchhau durch einen Wald‘ (s. Kluge und Weigand-Hirt s. v.). Bthl. Airan. Wb. 925 f.'"
  },
  {
   "src": "AHD",
   "where": "Watkins 1985, s.v. gʷhen-¹ (AHD_watkins1985.txt:545)",
   "stance": "partial",
   "note": "'gʷhen-¹. To strike, kill. 1. O-grade *gʷhon- in Germanic suffixed form *ban-ōn- in: a. Old English bana ... BANE; b. Middle High German ban, bane (> German Bahn), way, road (? < “path hewn through woods”): AUTOBAHN ... [Pok. 2. gʷhen-(2)- 491, bhen- 126.]' — same material, but filed under gʷhen-, with Pokorny's bhen- 126 only cross-referenced."
  },
  {
   "src": "SYN",
   "where": "Buck p. 304-305, §4.85 WOUND",
   "stance": "supports",
   "note": "'Goth. banja ... ON bani ‚death‘, OE bana, OHG bano ‚murderer‘, Av. banta- ‚sick‘ (4.841), etc., all prob. fr. a root *bhen- ‚strike‘. Walde-P. 2.149. Feist 80.'"
  }
 ],
 "nodes": [
  {
   "id": 1,
   "lang": "Avestan",
   "words": "ban; banta; banay",
   "verdict": "plausible",
   "derivation": "All three forms are genuine Younger-Avestan: Bartholomae lemmatises 'j., g. ban- V. ‚kranken‘. Praes. 30 (Kaus.) bǎanaya-. — PPfP. banta-',
```


## [2026-09-05T13:45:32.720Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KAS','PRT','SYN','KNT','AHD','KLN','HRN','SOD','IEC','BQT','MON','SNS','AEF','FFD','PHD','WLD','CHEUNG','BRT','HUB','ARY']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:600] if v else 'MISSING')\n    print()\n\"",
 "description": "Read refs_online entries for relevant abbreviations"
}
```


### [2026-09-05T13:45:34.393Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

KAS {"title": "M.A. Hasani Da'i al-Eslam, Khod-amuz-e Zaban-e Sanskrit, Danesh 1361/1982", "kind": "website", "url": "https://ketabnak.com/book/108067 (131 pp. PDF, login)", "lookup_hint": "Not on archive.org.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "PDF page exists; not fetched."}

PRT {"title": "E. Partridge, Origins: A Short Etymological Dictionary of Modern English, New York 1958", "edition_found": "1958 (lending-only copies)", "kind": "archive_restricted", "url": "https://archive.org/details/originsshortetym00part (1958 1st ed.) ; originsetymologi0000part_j9t3 (4th ed. 1966) ; originsetymologi0000part (Routledge 2009) — all lending", "identifier": "originsshortetym00part (also originsshortetym0000unse, bwb_P8-AVM-445, 1958)", "local_file": null, "page_offset": null, "lookup_hint": "Borrow via IA lending; in-book search https://archive.org/details/originsshortetym00part?q

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt

AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog", "lookup_hint": "Not online (searched archive.org, 

FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

CHEUNG MISSING

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it
```


## [2026-09-05T13:45:59.750Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor p in 128 137 163; do\n  echo \"===== POK printed p.$p (leaf $((p+8))) =====\"\n  awk -v n=$((p+8+1)) 'BEGIN{RS=\"\\f\"} NR==n' POK_01.txt | head -70\ndone",
 "description": "Print Pokorny pages 128, 137, 163"
}
```


### [2026-09-05T13:46:01.328Z] TOOL RESULT

```
===== POK printed p.128 (leaf 136) =====
.   bind    , melodisch^,    abret.  bann
canora^ '    WP.  II  151  f.
^eadh'  ,binden^
;^i.  hadhnäti,  erst  später  bandhati  ,bindet,  fesselt,  nimmt  gefangen, i\\iri  zus/,  av.  bandayaiti  , bindet',  Partiz.  ai.  baddhd-,  av.  ap.  basta-,  ai. hdndhana-  n.  ,das  Binden',  bandkd-h  m.  ,das  Binden,  Band',  av.  banda-  m. Bande  Fessel'  (:  aisl.  as.  bant,  ahd.  bant  n.,  nhd.  Band ;  got.  bandi,  ags. l^end  f.  ds.;  lit.  Jant^a , Vieh',  s.  unten);  ai.  bdndhu-h  m.  ,Verwandter'  (wie jfsydsQÖg).
Gr.  ftstcfia  ,Tau,  Seil'  (aus  *7tsv^a^a,  Schwyzer  Gr.  Gr.  I  287,  vgl. Bru<^mann  IF.  11,  104 f.,  auch  für  jtsa^ia  und  rcdafia),  ^tev&SQog  , Schwieger- vater* (*,durch  Heirat  verbunden') ;  hierher  nach  Pedersen  (REtlE.  1,  192) auch  ftdaxo)  , leide'  als  , werde  gebunden,  verstrickt',  wie  auch  lat.  offendö o-erate  ins  Unglück,  stoße  an',  defendö  ,lÖse  aus  der  Verstrickung';  Ttd&vr] (spät  belegt,  aber  alt),  mit  Hauchumstellung  hom.  att.  cpdrvr]  , Krippe' (Hhndh-nä'j  unter  einer  Gdbed.  ,geflochtener  Korb'  wie  kelt.  benna ,Wagenkorb');  thrak.  ßevd-  ,binden'  (vgl.  Kretschmer  Einl.  236);  alb.  bese , Vertrag;  Glaube,  Waffenstillstand';  lat.  offendimentum,  offendix  ,das  Kinn- band an  der  Priestermütze';  gall.  benna  ,genus  vehiculi',  galat.  Zeig  Biv- yiogj  cymr.  benn  ,Fuhrwerk'  (daraus  ags.  binn,  und  durch  roman.  Vermitt- lung nhd.  dial.  benne  , Wagenkasten',  ndl.  ben  ,Korb,  Mulde';  Gdf.  Hhendh- nä)'j  mir.  buinne  ,Band,  (Arm)reif'  (*bhondhia)]
got.  ags.  bindanj  aisl.  binda,  ahd.  bintan  ,binden',  got.  andbundnan  ,ge- löst  werden',  got.  bandi  usw.  s.  oben;  lit.  bendras  ,Teilhaber,  Genosse' (formantisch  gr.  Ttsvd-SQÖg  nahestehend),  bandä  ,Viehherde'  (eig.  ,das  an- gebundene Vieh').
Hierher  auch  got.  bansts  m.  , Scheuer'  (*bhondh-sti]  vgl.  in  anderer  Bed. afries.  böst  , eheliche  Verbindung'  aus  *bhondh-stu-  , Bindung';  ndd.  banse ,Kornraum,  Scheune',  ags.  *5ös,  engl,  boose  ,Viehstall',  ags.  bösig  ,Krippe', aisl.  bäss  m.  ,Raum  zum  Aufbewahren,  Viehstand'  {*band-sa-)',  jüt.  bende ,abgeteilter  Raum  im  Viehstall'  schließt  wohl  jeden  Zweifel  an  der  Ver- wandtschaft obiger  Gruppe  mit  binden  aus.
WP.  II  152,  WH.  I  102,  Feist  79,  80  f.,  93.
bbcngh-,  bhngh-  (Adj.  bbngbü-s)  ,dick,  dicht,  feist'.
Ai.  baJiü-  , dicht,  reichlich,  viel'  ,Komp.  Sup.  bamhlyas-,  bamhistha-  (= gr.  Ttaxvg)]    bahuld-  ,dick,  dicht,  ausgedehnt,  groß^  reichlich,  viel' (=  gr.
128
rtaxvKbg   Adv.  bei    Aristot.,    wenn   dies   nicht   jüngere    Bildung);    hdniha^'i (unbelegt)  ,mebrt  sich',  hhdrhhayate  ^befestigt,  stärkt';
av.  bazah-  n.  ,Höhe,    Tiefe',    basnu-  m.  ds.,   bal.   häz  ,viel',    baz  ;dicht'
gr.  Ttaxvg    ,dick,  dicht,  feist'   (Komp.  fc&aoiov),  na^oq   n.   ,Dicke'   (naci Ttccxvg  für  *7t6yxoQ  =  av.  bazah-  eingetreten),  näxeTog  ,dick;  Dicke';
aisl.  bingr  ,Haufen',  aschwed.  binge  ds.,  ahd.  bungo  ,Knolle',  nhd.  Bac) bunge]    dazu    mit   intens.  Kons.-Schärfung   aisl.    bunki    ,verstaute    Schiffst ladung',  norw.  bunka  (und  bunga)  ,kl
===== POK printed p.137 (leaf 145) =====
-k-,  s.  dort auch  über  bherg-),  bhreu-,  bhreu-q^-,  -k-  _,schneiden',  bhreus-  ,zerbrechen', hherug-  ^Schlund^
WP.  II  159  f.,  WH.  I  481  f.,  537,  865,  866,  Trautmann  27,  Mühlenbach- Endzelin  354.
4-  hher-  in  Schallworten  ,brummen,  summen'^  u.  dgl.
Arm.  bor,  -oy  ,Hummel,  Hornis^,  zum  redupl.  ai.  bambhara-h  (unbel.) jBiene^,    bambharälih    (unbel.)    ,Fliege',    bambhä-rava-h    ,das    Brüllen    der
136
Kühe^,   gr.  7t€!xq)Qr]öd)y   ,Art  Wespe^   (Bildung    wie  ävS-gr^dibv^   rsv&Qr]d(üp) ähnlich  auch  skr.  hümbar  ,HummeF,  klr.  bombär  .Maikäfer^
Hierher  wenigstens  z.  T.  (mit  gebrochener  Red.)  auch  die  bsl.  Grupp^ von   lit.   barbeti   ^klirren'^,    birbiü,    -iaü,    birbti   ,summen^,    burbiü,    Uivhe^ ^brummen,  brodeln^  u.  dgl.;  klr.  borborösy  PL  _,mürrische  Reden"^,  skr.  bf'blati. ^schwatzen'  u.  dgl.^   in  denen  freilich  die  Bedeutungen   ^undeutlich   reden! stammeln^  auf  die  Gruppe  von    ai.  barbaräh  usw.  (s.  Haba)  zurückgehen werden.
Eine.  Erw.  allenfalls  in  *bherem-  ,brummen^  und  in  den  unter  bherg, ;,brummen^  behandelten  Schallsippen.
WP.  II  161  f.,  Trautmann  39  f.
5.  bher-  ^glänzend,  hellbraun^:  bhero-s,  bberu-s,  vielfach  von  brauneu Tieren;  redupl.  bhe-btru-s,  bhe-bhro-s  ,braun;  Biber^;  flo-Bildun- gen :  bhre-no-,  bhro-no-  und  (*bheru-s :)  bhrou-no-,  bhrü-no. ,braun^.
Ai.  bhalla-k,  bhallaka-h  bhalVäka-h  ^'i.v'  (-11-  aus  -rl-)]  ahd.  bero^  ags. bera  ,Bär^  (*bheron-)j  aisl.  bigrn  ds.  (*bhernu-,  dessen  u  wie  das  n  von ai.  bhalVAka-h  aus  dem  St.  *bheru-  stammen  mag)  =  ags.  beorn  ,Krieger^ Häuptling';  aisl.  bersi  ,Bär^  (s  wie  in  Fuchs:  got.  fauhö,  Luchs:  schwed. lo)\  ablaut.  lit.  beras,  lett.  b^rs  ^braun  (von  Pferden)^;
gr.  gxxQT]'  vecpeXai  Hes.?  (*(paQe[(j]a  oder  *(paQ€J^a?  Letzternfalls  genau zu:)  (paQvvsL'  ka^rtgvvsL  Hes..,  (fQ'tvri^  (pQvvog  ^Kröte,  Frosch^  (*^die  braune^ =  ahd.  brün)]  ob  g)aor]  als  ^Wolkendecke^  zu  7.  bher-?
nep.  bhuro  ,braun^  (*bhrüro-)j  ahd.  mhd.  brün  ^glänzend,  braun^,  ags. brün,  aisl.  bränn  ds.;  russ.  mdartl.  brynä'th  ,weiß,  grau  schimmern^,  ab- lautend bruneth  ds.  (*bhrou-no-?)  und  (aus  *bhr-ono-,  -eno-)  russ.-ksl.  brom -  , weiß;  bunt  (von  Pferden)^^  russ.  bronv  (und  mdartl.  brynh),  klr.  brenity jisXh  werden,  reifen^,  aksl.  brhnije  (brenije)  ,Kot^,  slov.  brn  ^Flußschlamm';
ai.  babhrü-h  ^rotbraun;  große  Ichneumonart',  av.  baivra-,  baicri-  ,Biber'; lat.  fiber,  fibrl  ,Biber'  (auch  feber  s. 
===== POK printed p.163 (leaf 171) =====
(über  d-Ußoj  s.  unter  dhlas-  ^quetschen^); vmr.  hilf  m.  ;,catapult^  pallista'^,  hlifaldcl  ^schnell^;  lat.ßigö,  -ere  ^schlagen, iiscblagen,   zu  Boden   schlagen^   (*bhligö,   oder   allenfalls  mit  durch  fllxi^
ßictun^
veranlaßtem  w- Verlust  aus  *fllguo)]
lett.    hlaizit    ^quetschen,    schmettern,    schlagen^,   6^162^   ^schlagen^;    aksl. blizh    b^^^T>  Adv.  ,nahe^  (eigentl.  ^anstoßend^). ;yp.  II  217,  WH.  I  517,  EM.  369.    Über  russ.  hliznd  s.  unter  1.  bhlM-.
bblök-  ;Woll-  oder  Wergflocke,  Gewebe^?
Lat.  floccus  ^Wollfaser,  Flocke*  (^flöcos)  zu  ahd.  hlaha  f.  ^grobes  Lein- tuch (bes.  zu  Decken  oder  Unterlagen)',  nhd.  Blähe,  Blachej  alt.  dän.  hlaa "\yero*,  Hede^;  jetzt  hlaar  (eig.  PL),  schwed.  blänor,  hlär  ds.,  aschwed. blan    hla  ds.  (germ.  *hlahioö-),  an.  hlceja  {^hlahjön-)  ,Laken,  Bettuch^
WP.  11  217,  WH.  517  f.,  866.
bblos-q-;  -g-  in  Schallworten.
Ir,  blosc,  Gen.  bloisc  ,Lärm^  (bhlosko-)]  vgl.  auch  h'osc  ds.  unter  *bhres-] lit.  blqzgu,  -eti  intr.  ,klappern^,  blqzglnti  ^klappern,  rasselnd WP.  II  218.
bbog-  ^fließendes  Wasser,  Bach'.
Mir.  büal  f.  ,fließendes  Wasser'  (*bhoglä),  büar  m.  ,diarrhoea'  (^bhogro-)] urgerm.  *baJä-,  ahd.  bah,  nhd.  Bach,  neben  Hakja-  in  aisl.  bekkr,  ags. becc  m.  ds.
Mit  Hinblick  auf  ai.  bhatdgd-h,  lit.  bangd  ,Welle'  könnte  an  die  Wz.  bheg- ,zerschlagen,  zerbrechen'^  angeknüpft  werden.
WP.  II  149  f.,  187.
bhtgh'  oder  hhagh-  ,Schlamm,  Sumpft
Mnl.  bagger  m.  ,Schlamm',  daraus  nhd.  baggern  ,den  Schlamm  aus- schöpfen'; russ.  bagnö  ,niedrige,  sumpfige  Stelle',  Öech.  bahno  , Sumpf, Morast',  poln.  bagno  ds.
WP.  II  187,  Petersson  Heterokl.  123  f.
bhöi- :  bhQi'  :  bhi-  (bhiid-)  ,sich  fürchten';  bhoidho-s  ,fürchterlich,  abscheu- lich'. Ai.  bhdyate  ,fürchtet  sich'  (aus  Hhdietai  =  slav.  bojet^),  av.  bayente, byente  ,sie  setzen  in  Furcht',  mpers.  besänd  ,sie  sind  in  Angst'  (uriran. *bai-sk-)',  ai.  bibhki  ,fürchtet  sich',  sek.  zum  ursprünglichen  Perf.  m. Präsensbed.  bibhäya  ,bin  in  Furcht'  (bibhiyät,  bibhltana,  abibhet,  Partiz. bibhlvän  =  av.  biwivä  ,sich  fürchtend');  ai.  bhiyand-h  ,sich  fürchtend'; bhi-h  f.,  bhUi-h  f.  (:  lett.  Inf.  bities)  ,Furcht',  bhlmd-h,  ,furchtbar',  bhitd-h
162
,sich  fürchtend^  erschrocken^^  hhlo-u-h  ,furchtsam^  schüchtern,  feige*^  (wei r  =  idg.   l,  ablautend    mit  lit.    hdiUj   bailüs)-,    npers.    bäk   ,Furcht^  (a^ *bhdyaka-)'j   mit   idg.  Vereinfachung  von  äi   zu  ä  vor  Kons,   hierher  aj^ bhäma-h  etwa  ,Grimm,  Wut',  bhämitd-h  ,grimmig^
Gr.  jtid-TjTiogj  Ttid^cjv  m.  ,Affe
```


## [2026-09-05T13:46:09.311Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== grep bher- tragen ===\"; grep -n \"tragen, bringen\" POK_01.txt | head -20\necho \"=== grep bhrater ===\"; grep -n -i \"bhrä.ter\\|bhrater\\|Bruder'\" POK_01.txt | head -20",
 "description": "Locate Pokorny bher- and bhrater entries"
}
```


### [2026-09-05T13:46:09.364Z] TOOL RESULT

```
=== grep bher- tragen ===
=== grep bhrater ===
2361:got.  bröpar,  aisl.  bröäir^  ahd.  hnioder,  ags.  bröpor  ^Bruder^;  Km formen  dazu  alid.  MN  Buobo,  mhd.  buobe  ,Bube';  ags.  MN  Böfa,  Böji (>  engl,  boy)^  norw.  dial.  boa  ,Bruder^  usw.;  ferner  ahd.  MN  Buole,  mW buole  .Verwandter,  Geliebter^  mnd.  böte  .Verwandter,  Bruder'  usw.  ^ Kluge ^^  unter  Bube,  Buhle))
2362:apr.  bräti  (Vok.  brote)  .Bruder',  lit.  h'oterUis,  Kurzform  brozis,  bati bröUs,  lett.  b(r)älis  ,Brüderchen',  brätaritis  ,Ueber  Bruder!';  aksl.  h^ati braH  ,Bruder',  Kurzform  serb.  baca,  aöech.  bdt'a  ds..  russ.  bdtja,  bdSl ,Vater.  Priester'.
```


## [2026-09-05T13:46:12.856Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '2350,2372p' POK_01.txt\necho \"--- which leaf ---\"\nawk 'NR<=2362{c+=gsub(/\\f/,\"\")} END{print \"formfeeds before line 2362:\",c}' POK_01.txt",
 "description": "Print Pokorny bhrāter context"
}
```


### [2026-09-05T13:46:14.546Z] TOOL RESULT

```
Fern  bleibt  gall.  bräca  ,H.ose^;  s.  unter  1.   bhreg-  ,brechen*.
WP.  II  192,  WH.  I  540,  Kluge  11  unter  Bracke.
bhräter-  , Angehöriger  der  Großfamilie,  Bruder,  Blutsverwandter^
AI.  bhrätar-,  av.  apers.  brätar- , Bruder^;  osset.  äi^dd  ,Bruder,  Verwandter^;
arm.  eibair,  Gen.  elbaur  ds. ;  (^bhräter,  *bhrat7'ös)] neuphryg.  ßqareqs  ,frätrl^;  mys.-phryg.  braterais  =  cpq&vqaig^^ gr.    (pQi^rrjQ    (ion.)  *    dSeXcpög   Hes.,    att.   q)QäTrjQ,   cpq&xwQ   ,Mitglied    einer
(pqaTQia  (Sippe,  Brüderschaft)^;
ven.  vhraterei  ,frätrl^;
11*
164
lat.  fräter  ,Bruder^,  osk.  fratinim,  umbr.  fratrum,  fratrom  ,frätruin'  usw. (über  spätes  lat.  frätrueiis  s.  WH.  I  542);
air.  lrath{a)ir  .Bruder,  Angehöriger  der  Großfamilie^  cymr.  sg.  hrax PI.  hrodyr,  acorn.  hroder,  mbret.  hreuzVj  nbret.  breur,  PI.  breudeur  ds.;f
got.  bröpar,  aisl.  bröäir^  ahd.  hnioder,  ags.  bröpor  ^Bruder^;  Km formen  dazu  alid.  MN  Buobo,  mhd.  buobe  ,Bube';  ags.  MN  Böfa,  Böji (>  engl,  boy)^  norw.  dial.  boa  ,Bruder^  usw.;  ferner  ahd.  MN  Buole,  mW buole  .Verwandter,  Geliebter^  mnd.  böte  .Verwandter,  Bruder'  usw.  ^ Kluge ^^  unter  Bube,  Buhle))
apr.  bräti  (Vok.  brote)  .Bruder',  lit.  h'oterUis,  Kurzform  brozis,  bati bröUs,  lett.  b(r)älis  ,Brüderchen',  brätaritis  ,Ueber  Bruder!';  aksl.  h^ati braH  ,Bruder',  Kurzform  serb.  baca,  aöech.  bdt'a  ds..  russ.  bdtja,  bdSl ,Vater.  Priester'.
Vgl.  noch  ai.  bhrätrd-m  .Bruderschaft';  gr.  (pQ&TQa,  jbn.  (pQiqvqfj  ds.; bhrätrya-m:  gr.  cpQaTqla,  aksl.  bratThja^  bratbja  ds.,  lat.  frätHa   ,Frau  de Bruders'.
Toch.  A  pracar  (Dual  pratri),  B  procer.
WP.  II  193,  WH.  I  541  f.,  866,  Specht  KZ  62.  249.  Fraenkel  REtlE 6  f.,  Risch  Mus.  Helv.  1,118.
bhred{h?)-  .waten',  im  Bsl.  auch  .plantschen,  die   Zeit  vergeuden;   Unsi schwatzen';  bhrod(h)0'S  ,Furt'.
Thrak.  ON  BqsSccl]  lig.  VN  Brodionti:  vgl.  gall.  FIN  Bredamia,  t La  Brenne,  ON  Bgodevria  (Bayern).
Alb.  bretJi,  Aor.  brodha  ,hüpfen'.
Lit.  bredü  (ostlit.  brendu),  bridau,  bristi  ,waten',  Iter.  braddu,  -yti  ,waten' brastä,  brastvä  .Furt  (kotige)',  bradä  .Schlamm',  brädas  m.  ,Fischfang' (^=  slav.  brod%),  mit  sek.  Ablaut  brydis  m.  .das  Waten,  Gang  ins  Wasser'. ter.  braidaüj  -yti  .fortgesetzt  umherwaten';  lett.  brienu  (mdartl.  binedu =  ostlit.  brendü),  bridu,  brist,  Iter.  braddt  ,waten;  mit  Füßen  treten; Albernes  sprechen',  braslis  m.  ,Furt',  bridis  m.  ,Weile,  kurze  Zeit';  apr. Chucunbrast  ,des  Teufels  Durchfahrt';  Schwundstufe  ir  =  *2'  noch  in  lit. bii'dä  ,nasser  Kot',  apr.  Birdaw,  Seename.
Russ.-ksl.  breduy  bresti  .durch  eine  Furt  waten'  (tiefstufig  Präs.  *brhdg in  neprebrhdorm  .nicht  durchwatbar'.  Aor.  pribrhde,  vgl.  aöech.  'pHbrde .wird  durchwaten',  poln.  brnci6  .waten'  aus  *brtdn(^ti),  russ.  bredü,  hresti .langsam  gehen,  mit  dem  Zugnetz  fischen',  breditb  ,Unsinn  schwatzen, phantasieren',  bred,  bredina  .Weide'  (,da  oft  im  Wasser  stehend'),  r.-ksl., russ.  (usw.)  brod^  .Furt',  iter.  r.-ksl.  broditi  .waten',  russ.  broditb  ,langsam gehen,  schleichen,  umherschweifen;  gären',  skr.  brbditi  ,waten'.
WP.  II  201  f.,  Trautmann  37,  Mühlenbach-Endzelin  332  f.
165
--- which leaf ---
formfeeds before line 2362: 173
```


## [2026-09-05T13:46:20.943Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"bher-\" POK_01.txt | sed -n '1,60p'",
 "description": "Grep bher- occurrences in Pokorny"
}
```


### [2026-09-05T13:46:21.006Z] TOOL RESULT

```
1510:Lat.  fctr  (eig.  farr),  farris  n.  ,Dinkel,  Spelt;  Schrot,  MehP  aus  *far(o)s, *far(e)zes  (bzw.  *fars,  *fars-es)  =  osk.  far^  umbr.  far]  lat.  farina  ,MehF Caus  *farrlna)^  farreus  ==  umbr.  farsio,  fasiu  ,farrea^;  got.  hariz-eins C=3  lat. /arma)  ;aus  Gerste^,  aisl.  harr  m.  ,Korn,  Gerste^,  ags.  here  ,Gerste^ (*b(ir(a)z-,  bzw.  *ha7'(i)z-)]  aber  slav.  *barsina-  in  aksl.  brahno  ,Nahrung^, skr.  bräsno  ,Mehl^,  russ.  börosno  ,Roggenmehl^,  nach  Jokl  Miletic-Festschr. (1933)  119  ff.  vielmehr  zu  1.  bher-  ,tragen^    Vgl.  auch  hhares-  S.  109.
1556:bbebbru-,  bhebhro-  s.  bher-  ,braun^
1800:, aufheben,  erheben'.  Neben  bher-,  mit  them.  Vokal  bhere-,  steht  eine
1801:schwere  Basis  bhero  ibhre-.  Die  Wz.  bher-,  die  ausnahmsweise  sowoÜJ
1804:bhor-mo-s,     bher-isto-s,     bher-onti,     bher{9)'men-f     bherQ-tro^^
1805:bher-tor,  bh^-ti-s,   bhr-tia.
1832:bir  ,Solm'  (*bher-,  vgl.  got.  ftaw?-  ,Sohn'),  biß,  griech.  cal.  6i7e  , Tochter' mit  Deminutivsuffix  -ele,  -eje)]
1860:2.  bher'  etwa  , auf  wallen',  von  quellendem  oder  siedendem  Wasser  (auch  vom Aufbrausen  beim  Gähren,  Kochen,  sowie  vom  Feuer)  »sich  heftig  be- ,     wegen';    oft  mit  in-Formans;    auch  als  schwere  Basis  bbers-  :  bhr-^ bb{e)rei-,  bb(e)rf-.    Vgl.  6.  bher-.
1877:3.  bher-  ,mit  einem  scharfen  Werkzeug  bearbeiten,  ritzen,  schneiden,  reiben,
1889:Alb.  brime  ,Loch*  (*bhj'-ma),  bire  ds.  (*bhera),  ^eg.  brej,  tosk.  brenß ,nage,  streite*;  britme  ,September  und  Oktober*  (wenn  eig.  ,Ernte,  Herbst^y auf  Grund  von  *bhr-ti-  ,das  Schneiden*);  brese  ,bittere  Wurzel,  Zichorie' (,bitter*  =  ,schneidend*;  -se  aus  -tiä,  borig(e))  ,Splitter,  Span*  {^bher-  m^ Form.  -ige).
1916:5.  bher-  ^glänzend,  hellbraun^:  bhero-s,  bberu-s,  vielfach  von  brauneu Tieren;  redupl.  bhe-btru-s,  bhe-bhro-s  ,braun;  Biber^;  flo-Bildun- gen :  bhre-no-,  bhro-no-  und  (*bheru-s :)  bhrou-no-,  bhrü-no. ,braun^.
1918:gr.  gxxQT]'  vecpeXai  Hes.?  (*(paQe[(j]a  oder  *(paQ€J^a?  Letzternfalls  genau zu:)  (paQvvsL'  ka^rtgvvsL  Hes..,  (fQ'tvri^  (pQvvog  ^Kröte,  Frosch^  (*^die  braune^ =  ahd.  brün)]  ob  g)aor]  als  ^Wolkendecke^  zu  7.  bher-?
1927:g  bher-   mit  ^-Erweiterungen,   wovor   z.  T.   i-,   w- Vokale,   ^rösten,   backen^ kochen^ ijjvon  2.  bher-  ,sich  heftig  bewegen,  Avallen,  kochen^  abgeleitet.
1943:7-  bher-  ,flechten,  weben'?  bb^u-  , Gewebe'.
1955:bhereg'  in   Schallworten  ,brummen,  bellen,  lärmen  u.  dgl.',  vgl.  bher-  ds sowie  die  bei  bhreg-  ,brechen'  und  ,krachen'  begegnende  Schallbedeutung
2033:bh{e)reu-  :  bh(e)rU-,  Erw.  von  2.  bher-  ,sich  heftig  bewegen,  wallen,  bes.  vom Aufbrausen  beim  Gären,  Brauen,  Kochen  usw.' A.  Ablautstufen  bheru-  (bheru-),  bhr^-:
2036:Arm.  bark  ,scbarf,  sauer,  grausam^  (barkanam  ,ich  werde  zornig^),  ^ sehr  vieldeutig  ist,  wird  von  Dumezil  BSL.  40,  52  als  *bhr-u-  hierher, gestellt,  desgleichen  berkrim  ,ich  freue  mich^  als  *bher-u-]  sehr  unsicher!
2040:Lat.  ferveöj  -ere,  fervö,  -Sre  ,sieden,  wallen'  (über  fermentum  s.  2.  bher-f^ defi-ntum  ,eingekochter  Most,  Mostsaft'  (:  thrak.  ßgvrog,  ßgvrov,  ßgovro^ ,eine  Art  Gerstenbier';  aus  thrak.  *brütiä  (gr.  ßgvTia\  stammt  illyr.  hrUc^ ,Weintrester',  urverw.  alb.  bersi  ds.,  woraus  serb.  bersa,  birsa,  hh-ZQ Schimmel  auf  dem  Wein;  lat.  brlsa  aus  dem  Venet.  oder  Messap.).
2056:Wie  lit.  burnä,  arm.  beran  ,Mund^  (eigentl.  ,Offnung^)  zu  bher-  ,schneiden^ unter  einer  Anschauung  ,Kluft  ==  Schlund^
2387:Ai.  hhraj-  .Steifheit  (des  Gliedes),  rigor(?)^;  isl.  norw.  brok  ,steifes  Grj Borstengras';  ganz  fragwürdig  auch  in  aisl.  borkr  {Hhorgu-s),  mnd.  bor} nhd.    (eig.  ndd.)   Borke  ,rauhe,  äußere  Rinde'  (von   der  Rauhkantigkeitj ähnlich   sei  gr.    cpOQtvrj   ,harte,    rauhe   Haut,   bes.    Schweineschwarte'  z^^ unerw.  Wz.  bher-  zu  stellen).
2391:bbrei-,  bhri-  Erw.  von  bher-  ,mit  scharfem  Werkzeug  schneiden,  usw.'.
2397:Hierzu  wohl  auch  cymr.  brtoydr  , Kampf,  air.  briathar  ,Wort'  als *bhrei-trä  , Streit,  Wortstreit'  (zu  cymr.  brwyd  ,zerrissen,  durchlöchert'), vgl.  lit.  bdrti  , schelten',  refl.  ,sich  zanken',  aksl.  brati  ,kämpfen',  s.  2.  bher-^
2404:'tri    die  mit  *bhrei-g-  parallele  g'-Erw.  der   einf.  Wz.  bher-  in  lett.  berzu^
2412:bbren-  ,hervorstehen;  Kante  u.  dgl.',  wie  bher-  ds.
2429:Beziehung  zu  bher-  (bliren-)  »hervorstehen'  ist  durchaus  annehmbar;
2436:Angebl.  aus  den  Wz.  bher-  und  enek-  kontaminiert;  zuletzt  E.  Fraenke KZ.  58,  286^ f.;  63,  198.
2456:I»  bbreu-,  bbru-  Erw.  von  bher-  ,mit  scharfem  Werkzeug  schneiden,  ab- schaben usw.',  bes.  germ.  ,zerschlagen,  brechen';  bbrü-no-  (bhrou-no-) ,die  beim  Auskriechen  abgestoßene  Hauf^.
2466:Lit.  briaunä  ^Kante^   Rand,   Gesims^  {*bhreuna)j  ablaut.  mit   aisl.  brnri^ Die  Gruppe  ist  von  bher-  ^emporstehen;  Kante^  erweitert. WP.  II  196  f.,  W.  Schulze  KZ.  50,  259  =  Kl.  Sehr.  216.
```


## [2026-09-05T13:46:28.367Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== 1795-1815 ===\"; sed -n '1795,1815p' POK_01.txt\necho; echo \"=== 1855-1880 ===\"; sed -n '1855,1878p' POK_01.txt\necho; echo \"=== 1925-1945 ===\"; sed -n '1925,1945p' POK_01.txt",
 "description": "Print Pokorny bher-1, bher-2, bher-6 entries"
}
```


### [2026-09-05T13:46:28.428Z] TOOL RESULT

```
=== 1795-1815 ===
lat.  pinguis  ,fett'  ist  vielleicht  durch  Kreuzung  eines  *ßngu-is  =  Ttaxv^ bahic-  mit  einem  zu  oylmuSj  tzlcjv  gehörigen  Worte  entstanden;
toch.  B  jpkante,  pkatte  , Größe'  (Van  Windekens  Lexique  96);
hitt.  pa-an-ku-  (panku-)  ,all,  allgemein'.
WP.  II  151,  Couvreur  JI  177.
hher-  ,tragen,  bringen'  usw.  (auch  Leibesfrucht  tragen;  med.  ,ferri^),  auci
, aufheben,  erheben'.  Neben  bher-,  mit  them.  Vokal  bhere-,  steht  eine
schwere  Basis  bhero  ibhre-.  Die  Wz.  bher-,  die  ausnahmsweise  sowoÜJ
ein  themat.  wie  ein  athemat.  Präsens  bildet,  kennt,  weil  durativ,  im  Idg»
weder  Aor.  noch  Perf.;  Nominalbildungen:  bhöro-s,  bhorö-s,  bhora,
bhor-mo-s,     bher-isto-s,     bher-onti,     bher{9)'men-f     bherQ-tro^^
bher-tor,  bh^-ti-s,   bhr-tia.
Ai.  bhdrati  ,trägt',  av.  baraiti  ds.  (und  ,reiten'),  apers.   barantiy   3.  PLJ
ds.  (=  arm.  berem,  phryg.  aß-ßegsr,  gr.  cpigto,  lat.  ferö,  air.  biru^  alb.  bie%
got.  bairGj  aksl.  berq)]  ai.  bhdrti  (ebenso  wie  gr.  cpsgrSj  lat.  fert  alte  un-l
them.    Form),    bibhdrti,    bibharti,    biblifmdh,   bibhrati   (A^gl.  das  wohl  von]
*nL(pQ(xi.iev  =  bibhj-me  ausgegangene    i(T-7ttq)QdvaL    , hineinbringen'),    them.
abibhvan,  bibhramäna-h  und  av.  -bibarämi-^
Perf.  babhära  und  j ab hära  (Kreuzung  von  babhära  mit  jahära  von  hdrti)^
Partiz.  ai.  bUftd-h,  av.  bdvdte-'j  Supin.  ai.  bhdrtum'j  Kaus.  ai.  bhärdyati  =q
Iter.  av.  bäraya-j
Sup.   av.   bairista-   ,der   am   besten   pflegt,  hegt'   (=  gr.  (peqiaxog  ,vor-| züglichster,  bester',  wohl  , ertragreichster,  fruchtbarster');

=== 1855-1880 ===
132
Hierher  mit  Spezialisierung  auf  das  Austragen  des  Samenkorns:  transiti^ lit.  heriüj  heriau,  berti  , streuen'  (vom  Getreide,  dann  auch  von  Mehj Asche  usw.),  lett.  beru,  bert  ds.,  im  Ablaut  intransitiv  lit.  hyi^ü^  biraii birti  , streuen,  ausfallen*,  lett.   bifstUy   biruj   bift  , ausfallen,  abfallen',   usv^
Toch.  AB  pär-  , tragen,  bringen,  holen',  vielleicht  auch  in  A  kos-prej^ ,wieviel?'  ku-pre  ,wenn',  täprem  ,wenn*,  täpär{k)  ,jetzt',  falls  zu  gr.  li-cpQa  . . ; r6-(pQ(x  , solange  als'  (S.  129).  Über  hitt.  bar-ah-zi  ,jagt'  s.  Pedersen  Hitt.  185;
Specht  will  auch  (Dekl.  148),  mit  i-  und  it-Formans,  ags.  bri-d,  birci ,junger  Vogel',  germ.  brü-tis  ,Frau,  Braut',  ai.  bhimnd-  , Embryo',  lett. braüna,  Öech.  brnka  {*bhru-nka)  ,Nachgeburt'  hierherstellen.  S.  aber  unter bh(e)reu-  , quellen'.
WP.  II  153  f.,  WH.  I  483  f.,  527,  569,  865,  866,  Trautmann  31,  E.  Her- mann Stud.  Balt.  3,  65  f.
2.  bher'  etwa  , auf  wallen',  von  quellendem  oder  siedendem  Wasser  (auch  vom Aufbrausen  beim  Gähren,  Kochen,  sowie  vom  Feuer)  »sich  heftig  be- ,     wegen';    oft  mit  in-Formans;    auch  als  schwere  Basis  bbers-  :  bhr-^ bb{e)rei-,  bb(e)rf-.    Vgl.  6.  bher-.
Ai.  bhurdti  (Hhf-e-ti)  , bewegt  sich,  zuckt,  zappelt.  Intens. ^*ar-&Äwn^i  ds.; auch:  ,züngelt,  vom  Feuer';  bhuranydti  ,zuckt,  ist  unruhig;  setzt  in  heftige Bewegung,  rührt  um,  rührt  auf;  mit  m-Formans  ai.  bhramati,  bhrämyati jirrt  umher,  dreht  sich  herum',  bhramd-h  , wirbelnde  Flamme,  Strudel', bhfmi-h  ,beweglich;  Wirbelwind'  (s.  unten  aisl.  brimi  usw.);  bh'ärni-]^ ,heftig,  zornig,  wild,  eifrig',  dürfte  als  *bhfni-  ebenfalls  auf  der  schweren' Basis  beruhen;
hierher  wohl  av.  avabaraiti  , strömt  herab',  uzbardnte  ,sie  strömen  hervor(?)',l bardnti  ayqn  ,an  einem  Tag,  wo  es  stürmt'.
Aus  dem  Gr.  7tOQq)iQ(x)  (^rcoqcpvQ lo))  , walle  auf,  woge  auf,  bin  in  unru- higer Bewegung'  (:  si.  jdrbhurlti)'^  vermutlich  auch  (pi)qo)  »vermenge,  bringe durcheinander'  (wenn  ursprgl.  vom  Durcheinanderrühren  beim  Kochen; Gdf.  Hhoviö  mit  durch  den  Labial  bedingter  w-Färbung  des  Reduktionsvo- .  kales),  wozu  q)VQd7]p  »durcheinander*,  cpvQ(.iög  »Verwirrung',  q)VQdü)  .mische, rühre  durcheinander,  knete,  verwirre'.  '
Über  lig.  und  ven.  Namen  s.  unten.
Alb.  burme  .vollreif'  (*gargekocht)  aus  *bhormo-.
Aus  dem  Lat.  wahrscheinlich /re^t^m  undfretus,  -üs  ,Wallung  des  Meeres, bes.  Meerenge;  Brausen,  Wallen,  Hitze',  fretäle  ,Bratpfanne';
fermentiim,  Gärungsstoff,  Sauerteig'  (:  ags.  beorma,  engl,  barm,  nd.  barme, woraus  nhd.  Bärme  »Bierhefe');  auch /er-uere  S.  144;
Air.  topur,  nir.  tobar  »Quelle'  (Ho-uks-boro-),  mir.  commar  =  cymr.  cymmer »Zusammenfluß'  {*kom-bero-))  lig.  FIN  Comberanea-,  mir. /o6ar  »Quelle,  unter-
#' %
133
•rdisclier  Bach*  =  cymr.  gofer  ,BacliS  bret.  gouver  ds.  {*u[p]o'bero-), cvmr.  ^6'*^  , träufeln',  mbret.  beraff  ,fließen',  gall.  FIN  Voberä,  frz.  Woevre, Yoivre  usw.;  mit  222-Forinans  kelto-b'g".  aquae  Bormiae,  GN  Bormö,  bisp. ON  Bormäte,  FIN  Borma,  dak.  ON  BÖQ^avov,  ven.  FIN  Formiö  (aber  galL GN  j^orfö  gebort  zu  bhereu-  , wallen').   Über  mir.  6reo  , Flamme'  s.  unten.
^o-s.  beorma  m.  usw.  (s.  oben);  von  einer  Wzf.  *bi2(e)re- :  bi2(e)rö- : ahd.  brädam  m.  , Hauch,  Hitze*,  mbd.  brädem  , Dunst*,  nhd.  Brodem,  ags. hmcC  , Dunst,  Haucb,  Wind'  (engl,  breath),  aisl.  brädr  ,bitzig,  bastig*,  brad beteertes  Holz*,  brädna  ,scbmelzen*,  intrans.,  abd.  brätan,  ags.  br^dan , braten*;  ablaut.  mnd.  bröien  ,sengen,  brüten*,  mbd.  brüejen,  brüen,  nbd. hrilhen,  ags.  bröd  f.,  engl,  brood  ,Brut,  Zucbt*;  mbd.  bruot  f.  \,Hitze, Brut^y  abd.  bruoten  ^brüten^;  unbekannter  Herkunft  sind  abd.  brato  m. ,weicbes  eßbares  Fleiscb*  {Braten  erst  seit  mbd.  Zeit  zu  ,gebratenes Fleisch*  umgedeutet),  nbd.  Wild'pret,  anord.  brädo  ,Wade*,  spätlat.  ent- lehnt brädo  , Schinken*,  ags.  brmde  m.,  aisl.  bräd  , rohes  Fleiscb*.
Neben  der  sehr  fruchtbaren  Wzf.  bbereu-  (s.  dort)  ist  wohl  auch bh{e)rei-,  bh(e)ri-  anzuerkennen.  Auf  diese  kann  bezogen  werden  ai. jar-bhurl-ti,  gr.  *q)VQi-(x),  *7tOQ(pvQi-(o  (s.  oben);  mit  xn -Formantien  vermut- lich gr.  (pQL^dcj,  q)Qi^daao(xat  , bewege  mich  unruhig,  springe,  schnaube*; aisl.  brimi  ,Feuer';  mengl.  brlm  ,Glut*,  wahrscheinlich  auch  aisl.  biim  n. , Brandung',  ags.  hnm  n.  ,Meer,  See*;  die  in  brühen,  Brodem,  braten  yot- liegende  Bedeutungsfärbung  kehrt  wieder  in  norw.  prim  ,eine  Art  aus saurem  Molken  unter  starkem  Kochen  bereiteter  Käse*  (auch  nhd.  Brimsen- käse), mdartl.  auch  bi'lm  ,ds.;  auch  Kruste,  Bodensatz  einer  eingekochten Flüssigkeit*  (nbd.  bair.  Brimsen,  Brinzen  ,was  sich  beim  Mus  angebräunt an  der  Pfanne  festsetzt');  daneben  mit  formantischem  -uo-  sehr  wahr- scheinlich abd.  brio,  mbd.  brl(e),  ags.  briw  ,Brei'  (als  ,*Sud,  Gekochtes'), briwan  , kochen*;  hierzu  auch  mir.  breo  ,Flamme*  (*bhri-uo-).
Eine  s-Erw.  vielleicht  in  ai.  bhrt?ati  ,wankt,  schwankt*,  norw.  mdartl. brisa  ,anfflackern,  glänzen,  prangen;  Feuer  anmachen*,  bris  , Feuer,  Flamme*, insÄ;  , lebhaft,  munter*.
Vgl.  die  verwandten  Wurzelformen  bhereg-  ,kocben*,  bhereu-  , wallen*, bhreics-  , schwellen*,  bhrig-,  bhrüg-  , kochen,  braten*.
WF.H  157  f.,  WH.  I  482  f.,  546,  865.
3.  bher-  ,mit  einem  scharfen  Werkzeug  bearbeiten,  ritzen,  schneiden,  reiben,
spalten;  bhoros  , Abschnitt,  zu  Planken  geschnittenes  Holz^

=== 1925-1945 ===
^t  eil   B  verne,  A  |?arno  ^leuchtend^,   davon  B  perwe,   A  -paräm  ,Würde^ Erweiterungen   unseres   hher-  scheinen   hhereg-,   bherek-  .glänzend    Vgl. ferner  L  bhel-  mit  ähnlicher  Bedeutung.
WP.  11  166  f.,  WH.  I  490  f.,  Van  Windekens  Lexique   93.
g  bher-   mit  ^-Erweiterungen,   wovor   z.  T.   i-,   w- Vokale,   ^rösten,   backen^ kochen^ ijjvon  2.  bher-  ,sich  heftig  bewegen,  Avallen,  kochen^  abgeleitet.
1.  Formen  ohne  -i-  oder  -u-:   bhereg-:
Ai.   bhurdjanta  ,kochend^  (*bh,reg-);    bhrjjdti  ,röstet^,  bhrsta-h  ,geröstet,
crobraten^,  bhrUstra-h  yRöst^iamne^   bkarj{j)ayati  ,röstet,  brät',    bharjana-k
röstend,   bratend',   mpers.  barstan  ds.;  vermutlich  ist  *bhraz-  (*bh\raz-  in
bhurdjanta),  *bharz-  die  ar.  Wurzelform  und  ind.  -jj  nur  im  Präs.  *bhig-
skö,  woraus  *bhx(g)sgö  entstand,  wie  gr.  filayo)  aus  *(XLy-a'Au).
Lat.  fertum  ,eine  Art  Opferkuchen',  alat.  ferctum  {firctum,  s.  Ernout El.  dial.  lat.  165),  Partiz.  eines  *fergö  ,backe',  osk.  fertalis  ,Zeremonien;^ bei  denen  Opferkuchen  gebraucht  wurden'.
Lit.  birgelas  ,einfaches  Bier',  lett.  birga  , Dunst,  Qualm,  Kohlendunst'^ apr.  aubirgo  ,Garkoch',  birgaharkis  ,ein  größerer  Schöpflöffel'  (mit  ven.- illyr.  g).
2.  Formen  mit  i,  ei:
Npers.  biris-tan  ,braten',  b'^rezan  ,Backofen',  bal.  brejag,  bHjag  ,braten', npers.  biryän  (*brigäna-)  ,gebraten',  pam.  (umgestellt)  icirzam  ,röste,  brate' u.  dgl.  (iran.  *brij-y  *braij-).
Lat.  frlgöj  -ere  ,rösten,  dörren',  umbr.  frehtu  ,gekocht'.
3.  Formen  mit  w:  bbrüg-:
^v.  (pQ'öyaj  ,röste,  dörre,  brate',  g)QV7iTÖg  ,geröstet;  Feuerbrand',  (pqtyavov ,dürres  Holz',  q)QiysTQOv  ,Gefäß  zum  Rösten  von  Gerste'.
Merkwürdig  ist,  daß  in  den  Schallsippen  von  gr.  q)QvyiXog  ,ein  Vogel', iRt.frigö  ,quietsche',  poln.  bargiel  ,Bergmeise',  russ.  berglezz  ,Stieglitz'  die Verteilung  der  Formen  mit  u,  mit  i,  und  ohne  beides,  dieselbe  wie  in den  Worten  für  kochen  ist.
WP.  II  165 f.,  WH.  I  486  f.,  548 L
7-  bher-  ,flechten,  weben'?  bb^u-  , Gewebe'.
Hom.  (pagog  =  att.  cpäqog  n.  {^cpaqfog)  ,Tuch,  Leinwand,  Hülle,  Decke'; (potQai  Q)' vq)aivuvyTc'ki'AELvllQs.'^  yo^^uog  , Tragkorb,  Matte';
lit.  burva  ,eine  Art  Kleidungsstück',  lett.  burves  PI.  ,kleine  Segel'  {-u-
```


## [2026-09-05T13:46:43.343Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=1780 && NR<=1960 && /^[0-9]{2,4}$/ {print NR\": \"$0}' POK_01.txt\necho \"--- also inline page nums ---\"\nawk 'NR>=1780 && NR<=1960 {if ($0 ~ /(^|[[:space:]])(12[5-9]|13[0-9]|14[0-2])([[:space:]]|$)/) print NR\": \"substr($0,1,90)}' POK_01.txt",
 "description": "Find Pokorny page markers around bher entries"
}
```


### [2026-09-05T13:46:44.901Z] TOOL RESULT

```
--- also inline page nums ---
1789: 128
1820: 129
1822: Arm.  bereni  ,trage,  bringe'  (Aor.  eber  =  eq)eQS,  dbharat),  bern.  Gen.  berin Bü
1830: 130
1846: 131
1855: 132
1870: 133
1882: 134
1901: 135
1911: 136
1923: 137
1946: 138
```


## [2026-09-05T13:46:54.474Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT grep bar ===\"; grep -n \"bar-.*bear\\|bar: bear\\|patiy\\|parā-bar\\|pari-bar\\|fra-bar\" KNT.txt | head -40",
 "description": "Grep Kent for OP bar"
}
```


### [2026-09-05T13:46:54.549Z] TOOL RESULT

```
=== KNT grep bar ===
401:patiyazbayam ‘I proclaimed’, with Med. -zb-, but h*zdnam (acc.) ‘tongue’ with OP -z-, both from ТЕ ди; see also $91.
764:to Bv. MSLP 23.182-3, in DB 1.66, where he 4 would read adind : adam : (patiydbaram : adam :) 3
771:patiyabaram DB 1.68, perhaps for patiyabaram; 4
1197:pli ghu- in ОР patiy-azbayam Ч proclaimed’, Av. root zba-, Skt. pres. hudyatt.
1496:pIE ghy: patiyazbayam, Мейтат.
1579:The ethnic Pátisuvaris (to patiy ?).
1638:$133. Encursis is a frequent phenomenon in OP. The enclities are the following: Pronouns: Ist sg. асе. -md, gen. -maty, abl. -ma. 2d sg. gen. -taiy. За sg. acc. -йт, gen. -Saiy, abl. -$a; pl. acc. -&$, gen. -Sàm. acc. -dum; pl. acc. -di$. pl. aec. -àà (dubious; only in avabasa-lé DB 4.72), Coordinating conjunctions: -eà ‘and’, -vë ‘or’. Postpositions: d, patiy; both also as separate words before or after their nouns. Adverbs and particles: -am, -kavy, -ciy, -dty, never separately. -apiy, -paliy both also separately. Miscellaneous: уа in mátya DB 4.43, 48, 71; yadatya XPh 35f (miswritten yadàya XPh 39), cf. yada : tya XPh 29. müm, elsewhere orthotone, in mātyamäm DB 1.52. rádiy in avahya-radiy DB 1.6f, etc.; also separ- ately. Double enclisis: mé-tya-mém DB 1.52; rauca- pati-vd,, DB .1:207 aatpati-mé DNb 20; avā-
1654:nai-mà, nai-maty, nai-$im, nat-pati-mà, pali-maty, iyat-Saty, imat-vd, yadi-patiy, yadi-và, [us}i-ca; similarly in phrasal compounds, pati-padem, ni-padiy. By analogy, naty-di§ DB 4.73, 78.
1678:Prep. patiy, but pati-padam; party, but pari- barümiy; prefix ni- (not found separately in OP) in ni-padiy, ni-rasdtiy.
1685:ПІ. Final - before initial 4- keeps the writing ay’; the script does not show whether the -i is consonantized before the vowel, since it has no machinery for the distinction; but pati- never becomes *pa&iy- (= pašy-) in compounds, though -ty- becomes OP -8(i)y-: patiy-dvahyaiy, patiy- Giga", palty-ajald; pariy-ait(1y), niy-apatsam, viy- alarayam. |
2269:Ending in -ї: apiy (also enclitic), uparty, -diy, patiy (also enclitic).
2379:(c) Double prefixes are perhaps found in two forms: pait-à- in patiydbaram DB 1.68, ava-à-in avajaniya DB 1.51, 52; but there are some dubi- ous features even about these, сї. JAOS 62.274-5.
2396:pIE *ei-ti ‘he goes’, OP ату, Skt. éti; *i-te ‘go ye’, OP -itä in ратайа, Skt. itá; *7-dhi ‘go thou’, OP -idiy in paridiy, Skt. iht; imf. *é&-m ‘I went’, OP -dyam (for -am, 407.1) in nij-äyam [up]- üyam, Skt. dyam; imf. 3d sg. ОР а (on -S, $228.IIT) and atiy-ãiš; imf. 3d pl. with the- matic vowel from Ist sg., OP -йуа” in apariy- йуа”, -ài$a" (on -&а", 4282.1) in patiy-disa’, mid, dyad from *4-dya7ta.
2404:„ рту. *g*hn-dhi, OP jadiy, Skt. jaht; so alko 2d pi, imv. *o*hn-le, OP jata, and 3d sg. imf. mid. *egthn-lo, OP patiy-ajalà| imf. *eg*hen-m, OP ajanam, Skt. áhanam (with antevocalic de- velopment of m, $07.11), whence with the- matic vowel 3d рі. OP -ajana" in avajana* and perhaps the restored subjunctive 3d pl. i-Janá"tty.
2456:pIE *bhere-, Skt. bhárati; OP bara*tiy ‘they bear’, Skt. bháranti; imf. OP abaram, 3d sg. арата’, 3d pl. abara” abaraha", mid. abara*id; imv. 3d sg. baratuy; in epds., 3d sg. pres. á-baratiy, 2d sg. ппу. pari-barà.
2469:pAr. *kSaja- m Skt. kgáyati ‘he possesses’, OP imf. patiy-arsayaty ‘I ruled over’, ріс. zsayamna ‘ruling’; unless this is rather pIE *g52-e- ($214) to *gbé- seen in Gk. xéxrquae Ч possess’.
2520:OP avah-ya- in imf. patiy-avahyaiy ‘I appealed for help’, to stem in Av. avah- ‘help’.
2539:II. Thematic stems have subjunctives with the long thematie vowel throughout, Ist sg. and 181 and 3d pl. o, other forms é; 2d and 3d sg. and mid. as in Skt. bhár-àsi -àt -àse -äte : OP zšnāsāhy, Gahy (for *6aháhy), apa-gaudayàhy, \drau\jiyahy, pati-parsühy, pari-barühy (and -Gh*-d13), vainahy; ni-rasütty, xsndsdtiy, pati~parsatiy, bavatiy, vaind- tty; maniyahaty (for variant spellings, see Lex. s.v. ‘man-); maniydtaiy, gaubdtaty, 6adayátaty, yadataiy, vainātaiy. 3d pl. act. as in Skt. -dnis: OP vi-naéaya*tty (restored form).
2561:I. The primary ending -mi is attached directly to non-thematic stems, as in pIE *es-mz, Skt. dsmz, Av. ahmi, ОР amiy. The ending of thematic stems was the lengthening of the thematic vowel o, as in Lat. ferd, Gk. феро; but to this -б there was added in Aryan the ending -mz, as in Skt. bhdra-mt, Av. barümi, ОР pari-barümiy. Other OP examples: parsimiy, Skt. prechámi; dárayamiy, Skt. dhard- ydmi; vatndmty, jadiyämiy.
2566:І. The primary ending -si was attached directly to the present stem, whether thematic or non- thematie, but happens to oceur in OP only in sub- junetive forms: pali-parsühy (on -hy, $87), Skt. prechasi; pari-barühy and -barüh*-di& ($136), vi- kanühy and -kanáh-dif, kunavahy, xindsdhy, à- tínavühy, vainahy, apa-gaudayahy, Idrau|jtyahy; 6ühy for *даћаћу ($131); ahy for short-vowel sub- junctive (8222.1) *ahahy = Skt. dsast.
2584:III. The sigmatic aorist similarly remodeled its 3d pl. from -sat (< -s-nt) to -san(t); thus in ОК, s-aorist €\vo-av ‘they loosed’, whence strong aorist &o-cay ‘they gave’, and (late Greek) thematic éhaBo-cav ‘they took’. So also in OP, the -san j spread to some verhs,! being regularly -ha^ after a _ and -ša” after 1: abaraha^ alongside abara”, patiy- dia", opt. pass. yadiyaisa*, and with extension of — -ša” to the position after a, adurujtyasa", akuna- vasa” alongside akunava*.
2590:rat, (thematic) феру déperat. In OP we have pres. naniyaiy (= Skt. mdnye), patiy-avahyaty, and valrtaiyary (for -tayaty, §48; = Skt. varlaye). The same -at 15 found as primary ending of non-the- matic stems in Avestan and Indic, but there are no OP examples.
2591:III. This -at was used in Aryan also as second- ary ending in thematic imperfects, as in Skt. dmanye, OP amaniyary; OP ayadaw, apayaty, ham-adárayavy, ham-ataxsary, patiy-axrSayaiy.
2599:II. The secondary ending was pIE -io, as in Gk. ёферєто, Skt. dbharata; this is seen in OP ud- араай (Gk. &érero, Skt. épatata), anayatà (Skt. dnayaia), amariyata, früámáyalà, agarbüyatà, agau- bata, ham-ataxsatd, dyasatd, |a|h[yat]à, adalrayat|a, [ат]аоаій, passive akunavayatd, perhaps aor. (h)amarmalà and perf. pass. cazr[zyala] or [claxr|iyata]; non-thematie remade to thematic, avarnavaté and aisiata; non-thematic aor. akula (Skt. dkria) and imf. patiy-ajatd (Skt. dhata).
2604:I. The second smgular active of thematic stems is the stem without suffix: jivà, Skt. jiva; pari-bará, Skt. bhára, Gk. $€pe; parsa, Skt. prechd, Lat. posce. That of non-thematic stems has an accented -dhi, attached to the zero grade of the root: pIE *i-dht, OP -idiy in paraidiy and paridiy, Skt. tht, Gk. 16; pIE *gthn-dht, OP jadiy, Skt. jaht; OP pädiy, didiy (5129), G-rsnudiy.
2672:K. To express time when, as їп the adverbs paranam and paruvam ‘formerly’, and with the postposition pakiy: DB 1.20 xsapavd raucapativà ava akunavayata ‘either by night or by day, that was done’; DB 2.61f Güravaharahya mahya jiyam- nam patiy avat sam hamaranam kartam ‘on the last of the month Thuravahara, then by them the battle was fought’.
2688:with the verb ‘to rule’ probably belongs here: DNa 18f adamSdm patiyarSayaty ‘I ruled over them; DNb 15 uvaipašiyahyā xšayamna ‘ruling over my own (impulses)'. D. Partitive, expressing the whole: DB 1.37f 1 The disappearance of dative forms in OP and the as- sumption of dative functions by the genitive form makes it impossible to differentiate possessive datives with the copula, from possessive genitives; thus in XPf 28f Dérayavaus (error for -vahaus) рисӣ aniyaiciy ühatà ‘Of Darius other sons there were’, the genitive may be either a true genitive of possession, or a possessive dative. When an orthotone genitive follows the word on which it de- pends, however, there may be a presumption in favor of the dative use; ef. §309.
2694:E. Expressing time within which: DB 4.4f Һатаћуду Sarda in one and the same year’; from this use came the use of the genitive харо, DB 1.20, in a riming pair with acc. rauca and enclitic patiy, to indicate time when,
2704:trance’; DB 2.76 pasávasim Hagmatinary uzmayā- patiy akunavam ‘afterwards I put him on the stake (= impaled him) at Ecbatana’; DB 1.15 уату drayahyü ‘(those) who (dwell) by the sea’ (not ‘islanders’, since the term denotes the sa- trapy of which Dascylium was the capital, JNES 2.304). With ‘king’, singular nouns are in the loca- tive, as in DB 1.2 xSéyatiya Pérsary ‘king in Persia’, though plurals are in the genitive (§250.C); similarly DB 1.81 zšaçam tya Babtrauy ‘the kingship in Babylon’. It is a substitute for the genitive in DB 2.23f hya Madaisuvd тайа dha ‘who was chief among the Medes’ (cf. §250.D).
2705:B. Expressing place to which, with prep. уйй ‘as far as’, in DSf 32 abara yata Bābiraw ‘carried as far as Babylon’, 34 у010 Сй {уа ‘as far as Susa’; perhaps also, because of the idea of motion which seems to be in the verbs, in gátavà avástáyam (DB 1.62f), güfavü niyaSadayam (РМа 36), maškđuvā avükanam (DB 1.86), uzmayà-patiy (DB 2.76, etc.).
2728:E, Н); -patiy (see E); ласа (вее F).
2826:nouns. E- ачат, prep. W. асе. ati-, pref, w. verbs. abiy, prep. W. ace. anu», prep. w. instr. and gen. apa-, pref. w. verbs and nouns. abiy, prep. w. acc.; pref. w. verbs and nouns. ava-, pref. w. verbs. ud-, pref. w. verbs and nouns. upd, prep. w. acc.; pref. w. verbs and nouns. upariy, prep. W, асс.; pref. w. verbs. lara, prep. w. acc. ni-, prep. W. loc. in phrasal adv.; pref. w. verbs, nij-, pref. w. verbs. nipadày, prep. W. ace. T patiy, prep. ж. асе.; postp. у. acc, inst, loe; .^
2837:$269. PREPOSITIONS WITH THE ÁCCUSATIVE are the following; for patiy and pasa, used also with other cases, see §271: a"tar ‘inside’, of place where. abiy ‘to’, of goal. abiy ‘to’, of arrival at & goal, either person or
2854:rddty ‘on account of’, enclitic postposition in avahyaradzy ‘on account of this’; also orthotone post position, indicating the agent (DNb 9, 10f). IV. With the locative; see also patiy, һава,
2863:patiy with accusative, ‘against’ (DNb 22), ‘on’ in phrasal adverb patipadam (DB 1.62); as ortho- tone postposition with accusative, ‘on’, express- ing time when (DB 2.62); as enclitic postposi- tion, local ‘in, at’ with instrumental in v@apairy
2865:patiy (DB 2.76, 91; 3.52, 92), temporal ‘during’
2877:(a) The middie meaning is clear in such ex- amples as the following: DB 1.41f xSacam аш agarbiyata ‘he seized the kingship for himself’; DB 147 wãipašiyam акиіа ће made (the prov- inces) his own possession’; DB 1.55 patiydvahyaty ‘I asked aid for myself’; DB 1.93 hya Nabuk dra- cara agaubalà ‘who called himself Nebuchadrez- заг”; DB 4.38 patipayawa ‘protect thyself’.
3014:(d) Clauses of directly quoted statement as ob- ject or subject, normally without introductory conjunction: quotations of fact, with past parti- ciple or imf. ind., depending on xindsdhy and агай basdtiy, DNa 42-7; of volition, expressed by the subjunctive, depending upon amaniyaiy, DSI 3f; of wish, with the subjunctive or injunctive, de- pending upon maniyahaty, DB 4.39, DPe 20f, XPh 47; of negative command, with mà and the opt., depending upon patiyazbayam, XPh 38f; of direct question, with the imf. ind., introduced by ciya- karam ‘how many’ which is preceded by a superflu- ous tya ‘that’, and depending on тапталат, DNa 38f.
3071:тё-шв DB 1.52, 4.43, 48, 71, рану in ima pati- maiy DNb 32f despite nai-pati-mà DNb 20. Regu- lar orthotone mdm is written with the preceding in md-tya-mam DB 1.52. On adv. patiy, see П; on apiy, see III; on the postpositions, see IV.
3076:IV. The postpositions are upariy ($269; only once postposed, as separate word); рата, only in ava-parā; rādiy, in avahya-rddiy and separately; patiy, as enclitic postposition, as separate post- position, and also as preposition; -à, as formative of the locative case; kacã once (DB 1.50), separ- ately, governing a preceding enclitic. Position in the clause varies.
```


## [2026-09-05T13:47:02.324Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"bear, bring\\|‘bear’\\|'bear'\" KNT.txt | head -20\necho \"=== try leaf ===\"\nfor n in 214 215 216; do echo \"--- NR==$n ---\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' KNT.txt | head -8; done",
 "description": "Find Kent lexicon bar- entry"
}
```


### [2026-09-05T13:47:06.115Z] TOOL RESULT

```
606:І. The sequence -arty- is found in Ariya (and compounds), where Elam. has har-ri-ia, proving phonetic ar and not 7: and in the middle amariyata to root mar- ‘die’, the passive abariya to root þar- ‘bear’, and the passives akariya akariyalà kariyais to root kar- ‘do, make’. The correspond- ing Skt. forms, in the 3d sg. impf., are amriyate, abhriyale, akriyaie; but the OP forms from root kar- cannot have this vocalism, since the product would be *azriya-. In this verb then there was in these forms a vowel between the k and ће т: either а full vowel or the reduced vowel (shwa secundum or *), which assumed the full value of a short vowel in Indo-Iranian. It is likely that the other two verbs had the same formation. Thus there is no sure support for the sequence ri in OP.
1524:*bher- ‘bear’ in bara*tiy ‘they bear’; *bhor- in aršti-bara ‘spear-bearer’; *bhr- in u-bar-tam ‘well uplifted’; *bhór- in asa-büra- ‘horse-borne’, uSa-büri- ‘camel-borne’.
5191:ubarta- adj. ‘well-borne, lifted, esteemed’: u- well’ + barta- ‘borne’, pte. to bar- ‘bear’, pIE *su-bhrio- (830, $122, §242.1). ubartam asm. DB 1.21f;4.66.  ubartàm asf. DB 4.88. On meaning, cf. Altheim, ZII 3.33-5: hardly as taken by König, RulD 69.
5222:ušabāri- adj. ‘camel-borne’: usa- ‘camel’ ($79, $130), Av. ustra- (MB Gr. $109; cf. Justi, GGA 1882.488), + bāri- ‘borne by’ (8122, $126, $51521, 6160.1е), to root bar- ‘bear’. Cf. Jn. Indo-Iranian Studies Sanjana 18-20. ušabārim DB 1.86f.
5736:bara- sb. ‘bearmg, bearer’: Av. -bara-, Skt. -bhara-, Gk. -фороѕ, pIE "bhoros ($32, $122, $1431, ҮТ), to root bar- ‘bear’, in aritibara-, takabara-, vacabara-; also bāra- ‘borne by, rider of’, with vriddhi (8122, $126, 5148.1), in asabdra-, ef, usabüri-. See Hz. Ар] 95.
=== try leaf ===
--- NR==214 ---
5-6).
Dérayava'u- sb. ‘Darius’ (I, son of Hystaspes, king 522-486 ».c.; IT, son of Artaxerxes I, king 426-04 в.с.): Elam da-ri-a-ma-u-ts, Akk. da-ri- ja-mus, Gk. Дарєюѕ (by haplology for *Aapetaios; Keiper, Acta Sem. Phil. Erlangen, 1.253). From pAr. *dháragat-, pic. to root in OP dar- (§162, §240), + pAr. *yasu asn. ‘the good’ (5158.1), see OP vau-: ‘He who holds firm the good’ (Hz. Arch. Hist. Iran 40, ApI 255, 267, takes as hypocoris- tie of *ddraya-vahu-manah- ‘Holder of Good Thought’; this is rejected by Nyberg, Rel. 361).
Dérayavaus nsm. (8118.IV, 5124.2) DB 1.1, 4, 6,9, 11, 13, 171, 201, 24, 27, 35, 44, 48, 61, 71, 73, 81, 83, 90; 2.1, 5, 8, 11, 13f, 18, 29, 37, 42f, 49, 57, 64, 70, 78, 91, 92; 3.1, 9, 10f, 19f, 21, 29, 40, 49, 53, 54, 64, 69, 75, 76, 83; 4.1, 2f, 31, 33, 36, 40, 43, 45, 50, 58, 57, 59, 611, 67, 69f, 72, 76; 80, 86, 88; 5.1, 14, 18, 20, 30, 34^; DBa 1, 41,9, 14; DPa 1;
190 OLD PERSIAN
DPb; DPd 4f, 5, 12; DPe 1, 5f, 19; DPh 1, 3f; DNa 8, 15, 30f, 40, 47t; DNb 5; DSa 1, 3; DSb 1f°; DSc; рва 1°, 3°; DSe 8, 14, 30f°, 41^, 49f; DSf 5f, 8, 55; DSg 1, 3; DSi 1, 3; DSj 1, 2, 5; DSk 1, 3f; DSI 1; DSm 1, 3°; DSn 1°; DSo 2f; D8q 2; DSt 7°, DSy 1; DZa; DZb 1; DZe 4, 7; DE 12; DH 1, 8; XPc 11; XPf 16f, 30, 38; XPg 6; XSa 2; XV 17; D*Sa 2; D'Sb 1°, 3°; Аа 3; Wa 21; Wb 1; We 2; Wd 2; SDa; SDb. Dérayavahaus as nsm. XPf 25 (851; Lg. 9.39).
Dérayavaum asm. DPd 2; DNa 5; ОХЬ 4; DSe 5^; DSf 3f; DSn 2; DSp 1f°; DSt 5°; DZe 3; DE 7; XPf 221; D'Sa 2f.
Dérayavahaus gsm. (8118.1V, 5124.2) DB 3.58f; DPe; DPd 10; DPi; DNe 1f; DNd 1; DZc 3; XPa 9f; XPb 19; XPe 8f, 14; XPd 13; XPe3; XPf 13f, 17; XPh 11; ХР}; XPk; X8e 2°; XE 19; XV Mf; A!Pa 16. Dérayavaus as gsm. XPf 28 (851; Lg. 9.39); (8313.11) A’Sb, A'Sd 2, A?Hb, A?Pa 13f, 14, 17, 18. Dérayavausahya gsm. (557) АЧ, A’Sa 1, 1f, 2f, 3; A?8c 0 bis; A?He 9f, 10 (as nom., 8813.1), 18, 14 (as nom.). Dàrayavasahyà gsm. (852.VI, $57) А?На 2, 2°, 4, 4°.
daru- sb. ‘wood’: Av. déuru-, Skt. dáru-, ef. Gk. доро ‘spear’. düruv (§181) nsn. DSf 41, in phrase asd атир ‘ebony’, lit. ‘stone wood’ (§308.- nl), so called because of its hardness; but also probably аз@ because of the assonance translated Akk. aban ‘stone’, ef. Hebr. eben ‘ebony’, Gk. Веро, from Egyptian hbnj ‘ebony’ (J. Duchesne- Guillemin, BSOS 10.925-7 [1942], noting that acc. to Hdt. 3.97 the Egyptians paid a tribute of ebony logs to the Persian King). Not to be normalized dārwa to root !dar- and the phrase taken as ‘copper’ (Scheil 21.30; Kent JAOS 51.208, 53.18- 9), or as ‘iron’ (Ву. BSLP 30.1.60; who also sug- gests that dáruva may be an adj. referring to some kind of tree); not asé + instr. déruv ‘window frames of wood’ (König, Burgbau 64-5); not asd süruva ‘lead’ (Hz. Ар] 299), to Av. srva- ‘lead’ (Bthl. AIW 1649), for the slight traces do not con- firm initial s". — [dár|uv asn. DSf 51 (so Hinz, Orientalia, soon to appear; not {23mal}uv, see Lex. S.V.).
--- NR==215 ---
Hz. Ap! 136-8) nsn. as sb. ‘handiwork’, DSe 42.
Daha- adj. ‘Dahian’; pl., a province of the Persian Empire: АКК. da-a-an, Gk. Aaa (§76.V; Lg. 18.298; Hz. AMI 8.72). Dahà npm. XPh 26.
dahyu- sb. ‘land, province, district’: GAv. :
daltyu-, LAv. dahyu- daiphu-, NPers. dih ‘village’, Skt. ddsyu- ‘stranger, demon’ (5124.2, $153.IV, $166). Decl., 5183.1. See also visadahyu-.
dahyaus nsf. AmH 5, 8f (as Isf. §814b); DB 1.59; 2.28, 58, 59, 72; 3.9, 11, 20, 28, 66, 75, 79f; 5.4, 13f, 29f; DPd 6. dahydus-maty DB 4.39. dahyüum asf. (853, $72) AsH 8, 11, 13; DPd 15, 18; DNa 53. dahydvam (8124.VY) XPh 88, 58f. dahyaud (dahyuvd Wb.) isf. (M8, §124.2, 8137) DB 1.34.
dahyàva прі. ($124.7) DB 1.18, 17, 18, 28, 41; 2.6°; 4.33; DPe 7, 14; РМа 17, 39; DSe 15f, 32f; DSm 5°; XPh 15. dahyáva apf. DB 1.21, 47, 67; 4.92, XPh 31,35. dahyünüm gpf. DB 1.2; DBa 3; DPa 4; DPe 3; DNa 10; DSb 6f; DSe 9°; DZb 2{°, DZc 5; DE 15; XPa 7f; XPb 15; XPc 7; XPd 10f; XPf 10; XPh 8f; XSc 2°, ХЕ 15; XV 111; А:Ра 11f°; A’Sc 3f; Wb 5; We 6; Wd 6. dahyüv- näm (523.11) РР} 2; DH 1f. dahyusued lpf. DB 1.35.
DHum (842) asf. DSf 58; DSj 6°. DHyaum (553) А2Рә 26. -DHnám gpf. DSa 2; DSd 1; DSf 6; 056 1^; D8i 4°; DSk 2; РӘ 2°. DHyünam
LEXICON
--- NR==216 ---
rada&a, duvaista-. dürau lsn. as adv. ‘afar, far away, far and wide’ (GAv. düiré, LAv. duire, Skt. d'ré; $65, 6191.111) DNa 44. duraty apiy DSe 11, DZe 6, DE 18, XPa 9, XPb 18, XPe 8, XPd 13, XPf 13, XPh 10, XE 18, XV 14, A'Pa 14f°, A’He 17. düraiapiyy DNa 12, dürayapiy DNa 46 ($18, $136).
duradasa adv. ‘from afar’, with preceding hacá: dūra- + adv. -dä asin отада + abl. -ša asin avada&a (§135, 5191.1; ЈАО 54.37).  DSf 23.
duruj- vb. ‘lie, deceive’: Av. druj- ‘le’ (draog-, Bthl. AYW 767), pres. druZasti, sb. druzé ‘principle of evil, devil’, Skt. drúhyatí ‘deceives’, Gm. trügen, pIE *dhrugh- (876.111). See alsodrauga-. adu- rujiya imf. (§101, $103.IV, $113, 5128, 4132.1, 2, 3, $214, 5228.11) DB 1.39, 78; 3.80; 4.8, 10f, 13, 16, 18, 21, 24, 261, 29; DBb 2; DBc 2; DBd 2; DBe 3f; DBf 1; DBg 2; DBh 2f; ОВ! 2f; DB} 2f. adurujiyasa" 3d pl. imf. ($214, §218.1, $232.III) DB 4.34f. duruxiam nsn. past pte. pass. ($103.IV, $122, $128, 8132.1, 3, $242.I) DNb 52, 5f; asn. DB 4.44f, 49f.
duruva- adj. ‘firm, secure’: Av. drva-, Skt. dhruvd-; deriv. to root in OP ‘dar- ($122, $128, $150). durwä nsf. DB 4.39.
duvatsta- adj. ‘very long, very far’: superl. to dūra- ($156.IIL, §190.11 $191.0; МВ Gr. $275), ef. Skt. davisthd- with slightly different formation.
192 OLD PERSIAN
duvais[ta]m asn. as adv. ‘for a long time’ DPe 23 (cf. remarks s.v. hyà).
duvara- sb. ‘door’: Av. dvar-, Skt. dhvar-, Gk. дора, Lt. forés, NEng. door, Lith. dvéras ‘court- yard’, pIE *dhuor- dhur- and its extended forms *dhyoro- etc.; see also duvarfi-. duvarayd-maiy lsn. ($186) DB 2.75; 89f.
```


## [2026-09-05T13:47:11.317Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 223 224 225; do echo \"=========== NR==$n ===========\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' KNT.txt; done 2>&1 | head -80",
 "description": "Print Kent lexicon around page 200"
}
```


### [2026-09-05T13:47:13.636Z] TOOL RESULT

```
=========== NR==223 ===========
-. — fra&aram asn. XPf 26f, 37.
Fraéda- sb. ‘Frada’, a Margian rebel: Elam. pir-ra-da, АКК. pa-ra-da-’ ; perhaps thematic noun- stem (§141) to fra- + *dà-, with vriddhi ($126), cf. Av. früd- ‘to further, increase’ (ТИМ. AiW 1012), but more probably hypocoristie to a com- pound name ($164.П1; Bthl. AiW 1018) of which the prior part was the participial stem to the same compound verb (§162), ef. Av. adj. fradat.qaéa- ‘prospering the household’, sb. frddaj.fsav- ‘Pro- moter of flocks’ (name of a divinity; Bthl. AiW 1013-4). Not with Sen 52 (fra- + OP *ad- ‘drive’, Av. azaiti, Skt. djati, Lt. agit), nor with Justi, INB 101 (fra- + had- ‘sit’, with loss of intervocalic -h-). Fraéda nsm. DB 3.12; 4.23; ОВ] 1.
framatar- sb. ‘master, lord’ (‘giver of judicial decisions’, ace. to Hz. ApI 150-4): fra- + root mā- + agent suffix -tar- (5154.1). framatéram asm. (§124.VI, $1861) DNa 7f; DSe 7; DSf 5; DE 11; XPa 5; XPb 11; XPe 5; XPd 8; ХР? 7f; XPh 6; XE 11; XV 9; A'Pa 8°; A?He 7. frama- ібгат (852.111) A?Pa 8.
framána- sb. ‘command’ (judgment, deci- sion’, acc. to Hz. ApI 144-50): РЫ. framán, NPers.
OLD PERSIAN
fürmán; fra- + mä- + suffix -nà- ($128, $1471), ef. Skt. pramána-m ‘measure, standard’. — framánà nsf. DNa 57; DNb 28; DSj 3°, framánáyà isf. DNb 37.
fravata adv. ‘forward, downward’: Phl. frót, NPers. fáród јато; from *frava-, extension of fra- as in Gk. rpõros ‘first’ from *proya-, + -tos as in amata (§191.1I; JAOS 51.204, 53.15; Bv. BSLP 30.1.59; hardly with Kénig, Burgbau 51; not identical with Skt. isf. pravátà ‘downhill’). DSf 23f, 28.
Frovartz- sb. ‘Phraortes’, a Median rebel: Elam. pir-ru-mar-t-18, Akk. pa-ar-ti-mar-ti-1§ Gk. Ppadprys: identical either with Av. frava&i- ‘guar- dian angel, soul’, from fra- + var- ‘protect’ + -ti- (S31, 8152.11) as ‘Protection’, or with Av. fraoroti- "Siehbekennen zu’, from fra- + var- ‘choose (re- ligiously)’ + -й- (Bthl. AIW 991, 992, 976; Nyberg Rel. 334-5, prefers second view); as man’s name, probably liypocoristic of a longer compound ($164.1). — Fravarti$ пата. DB 2.14, 66, 71, 73; 4.18; DBe 1f. Fravartim asm. DB 2.17. Fravar- tas gsm. DB 2.69, 93.
fras- vb., see јтаб-.
fraša- adj. ‘excellent’ (‘tauglich’, König Burg- bau 48, Brd. АКМ 39.87): Av. frasa- ‘directed toward, useful’, formed on adv. fraša to frünk-, Skt. adv. praca to ртайс-, from pra- + añe- (Bthl. AiW 1006-7); the irregular -3- for -s- of Sy- may be a contamination of *frasa- and *frasya- (otherwise ВБ. IF 2,266-7; borrowed from Aves- tan aec. to Hz. ApI 162). Hz. ApI 156-65 (recant- ing derivation from fra- + záy- ‘shine’, ‘brilliant’, AMI 3.1-11) takes as deriv. of pra-, through an idiom of racing or fighting, as 'extra (certamen), hors (concours)’, and therefore "incomparable, su- preme’. Cf. also Hz. RHRel. 113.26; Bailey, BSOS 6.595-7; Kent, Lg. 15.169. — frasam nsn. DSa 5, DS] 6 (see frasta-, for reading). frasam asn. DNb 2; DSf 56, 56f; DSo 4^; DSs 1°.
frašta DSa 5, DS] 6: discussed by Bv. ВІР 30.1.63-4, Gr. $103, Gray AJP 53.67, Brd. WZKM 39.20-1; but fra$am @adaydlary and not frašta ðadayämaiy ($54.11) should be read in both pas- sages (Hz. AMI 3.9-10, ApI 156-8). See under frasa-.
(mu. em lere Am ee шшш. ште у. mi ease e +
LEXICON 199
fraharavam, phrasal adverb ($191.]II), ‘in all’: fra- ($1401) + asn. haravam with variant orthography ($22, $26), to haruva-. DB 1.17.
. baug- vb. ‘free’: Av. baog-, NPers. boxtén; in Attydbausna-, Bagabuxsa-.
Düxtri- sb. ‘Bactria’, a province of the Persian Empire: Elam. ba-ak-&-18, ba-ik-tur-ri-i$, Akk. ba-ah-tar, Gk. (nt. pl) Béxrpa (§9.1, $79, 6103.111). OP %-stem, for older 7-stem (8152.II), seen in Av. báxói. — Büziri$ nsf. DB 1.16; DPe 16; DNa 23; DSe 22°; D8m 9°; XPh 21. Ваг- triyd \sf. DB 3.13f, 21. Baztriya absf. DSf 36.
bag- vb., see under baga-, bàji-.
baga- sb. ‘god’: Av. baga- ‘lot, good fortune’, Skt. bhdga- ‘dispenser (of good fortune)’, Gk. -paryos ‘eater’, OCS bogi ‘god’, pIE *bhago- ($101, $122, 5143.1, V, VI); ef. Hz. ApI 105-10. See also Bagábigna-, Bagabuxsa-, Bagayddi-, bà. рада nsm. AmH 6; AsH 6; DNa 1; DNb 
=========== NR==224 ===========
1; DSe 1°; DSE 1°; D8s 1^; DSt 1; рле 1°; DE 1; XPa 1; XPb 1; XPc 1; XPd 1; XPf 1; XPh 1; XE 1; XV 1; A!Pa 1^; A*He 1; A®Pa 1, 25. bagaha npm. ($10, $119, $172) DB 4.61, 63. bagünám gpm. AsH 7; DPd 1f; DPh 9; D8f 9; DSp 1°; DH 7; XE 2; XV 2; A’He 2. bagaibiš ipm. DPd 14f, 22, 24; DSe 50f°; DSt 8; XPb 28f; XPe 12f, 15; XPd 18; XPg 13f; XSc 5°; XV 26; A'Pa 23°. Вот ($42) ipm. D’8a 3. |
Bagábigna- sb. ‘Bagabigna’, a Persian, father of Hydarnes: Elam. ba-qa-pi-ig-na; from baga- ‘sod’ + d-bigna-, pte. in -na- of an unidentified verbal root, cf. perhaps Skt. bija-m ‘seed’ (575.1, $103.IV, $160.Ie, $243). Baglalbignah{ya} gsm. DB 4.84f.
Bagabuxía- sb. ‘Megabyzus’, an ally of Darius against Gaumata: Elam. ba-qa-bu-uk-5a, Akk. ba-ga-bu-ki-$u, Gk. MeyaButos. From baga- ‘sod’ + deriv. of root baug- ‘free’ ($102, §151): ‘God-freed’ (§160.Jc). Balgabluzsa nsm. DB 4.85.
Bagayddi- adj. ‘Bagayadi’, seventh month, Sept.-Oct.: Elam. байцай$, АКК. tasritu. From baga- ‘god’, with vriddhi (8126, §165), + yad- ‘worship’, with lengthened vowel ($126, $165) and formative -2- (8152.1): ‘God-Worship Month’ (8159, $161.Ia), probably referring to Mithras, since Phl. and NPers. call this month Mihr
‘(Month of) Mithras’ (Justi, ZDMG 51.247; Bthl. AiW 952-3). Bágayádait gsm. DB 1.55.
bàji- sb. ‘tribute’: NPers. Баг; deriv. (§152.1, $165) of root seen in Skt. bhdga- ‘portion, dis- penser’, OP baga- ‘god’, the verb being Skt. bhájatt ‘apportions’, Av. bag-, РЫ. bäztän (§101, $122, $128, $126). Балт asf. DB 1.19; DPe 9; DNa 19; DSe 18; XPh 17.
batugara- sb. ‘drinking cup, saucer’: if genu- ine ($55.11; JAOS 56.215; Schaeder, БРАМ 1935. 489-96), from batu- ‘wine’ ($153.1; etymology un- certain, but Hz. ApI 114 quotes Bariaxy from Athenaeus, bk. xi, page 784a, as the Persian word for ‘phiale, cup’) + -gara- (8143.1) ‘devouring, drinking’ ($160.Ia), cf. Av. aspé.gard ‘horse-de- vouring’, Skt. aja-gará- ‘goat-swallower, boa con- strictor’, Gk. dnuo-Bédpos ‘people-devouring’, Lt. carni-vorus ‘flesh-eating’, from root in Av. gar- ‘devour’, Skt. girdit, Lt. vorat, plE *g*er-. Bv. J As. 228.233-4 suggests, and На. AMI 8.9-17, Ap! 118—5, accepts cognation rather with Skt. galati ‘drips’, gdlayat ‘pours’, as ‘wine-pourer’, cf. Lt. рате ‘pour (as an offering to the gods)’, and NPers. piyàüla ‘drinking cup’, from *pati-gdra-. bülugara пет. ($56.V) АЧ.
ba*d- vb. ‘hind’: Av. band-, Skt. bandh-, Gt. bindan, pIE *bhendh-. See also badaka-. basta (NPers. bäst) nsm. past pte. pass. (867, $85, 5120, $122, 5182.1, 52421) DB. 1.82; 2.75, 90; 5.26. basta apm. DB 3.88".
ba"daka- sb. ‘subject, servant’ (cf. König, Кыр 64): Phi. bandak, NPers. bändäh; deriv. (§146.1T) of OP *ba"da- ‘bond, fetter’, Av. banda-, Skt. bandhd-, to pIE root *bhendh- (OP ba"d-; $39, $75.11, $111, §122, 8132.1). badaka пет. DB 2.20, 30, 49f, 82; 3.13, 31, 56, 85; 5.8. badakā npf. DB 1.19.
Bábiru- sb. (Babairu- because of Pali Báveru-, MB Gr. $80) ‘Babylon’, a city (S56.III, $166); ‘Babylonia’, a province of the Persian Empire; by transfer, ‘Babylonian’: Elam. ba-pi-li, Akk. bab-ilu, bab-ilàni ‘gate of the god(s)’, Gk. Вав (§75.V, $107). See also Babirwiya-. Bahrus пет. DB 1.14, 80; DPe 10f; РМа 26; DSe 25; DSm 7°; XPh 22; as ethnic ($56.11), DN xvi, A?P 16. Babirum asm. DB 1.83f, 91 bis; 2.2, 3, 3f; 3.82, 84, 87; 4115, 30. \Babiraus absm. ($168, 6182.1) DB 2.65. Варта lsm. DB 1.78, 81;
200 OLD PERSIAN
2.5, 6; 3.79, 88, 92; 4.2; DBd 7f; DBi 11 (written Bab*raw, $22); DSf 33 as loc. with усій, 33 as abl. with Ласа (hardly a real abl., corresponding to Av. -aut despite Hz. AMI 3.55n, Kent ЈАО 53.16).
Bābirwiya- adj. ‘Babylonian’: deriv. ($144.- ПТ) to preceding. — Bábiruviya nsm. DB 1.77, 79; 8.81; 4.13; DSf 20. Babiruviyam asm. DB 3.86. Babiruviyé npm. DB 3.78; DSf 53f. Bäbiruviyä apm. DB 3.88.
bar- vb. ‘bear, lift up, esteem’: present stem bara-, Av. батат, N Pers. bard, Skt. bhárati, Gk. dpa, Lt. fert, Gt. batrip, pIE *bhere/o- (8213). See also ubarta-, uSabdri-, Gaubaruva-, bara-. bara^tiy 3d pl. ($122, 5232.1) DB 5.22f (written berety, 522); DNa 42. abaram Ist sg. imf. ($61, $75.III, 5226.1) DB 1.2
=========== NR==225 ===========
2; 4.66. abara imf. ($40, $84, 5228.) DB 1.25, 55, 88, 94; 2.25, 34f, 40, 45, 54, 60, 68, 86, 97^; 3.6, 17, 37, 45, 62, 67 (written ar?r^, 854.11), 87; 4.61, 62; DNa 50f; DSf 19°, 32; XPh 33, 45. abara” 3d pl. imf. ($10, $40, $84, $106, 8232.1) DPe 10; DSe 18°; DSf 34. aba- raha” 3d pl. imf. ($10, $218, $282.11) DNa 19f; XPh 17 (written орт, §54.1). abara"tà 3d pl. imf. mid. ($10, $236.II) DB 1.19. abariya imf. pass. (535.1, $220, $228.IT) DSf 23°, 31f, 35, 36, 38f, 40, 48, 45. abariya" 3d pl. imf. pass. ($220, 8232.11) DSf 41, 47.  baratuv imv. (5237.П) AmH 11^; DPd 14; DSk 5. аталаш inf. ($238) DNb 41.
à + bar- ‘perform’: dbaratiy ($218, $228.1) DNb 25. Cf. also Hz. Ар] 110-1, who refers to à-bar- certain other forms listed above as augmented forms of uncompounded bar-.
pati- + à + bar- ‘bring back, restore’: райуй- baram Ist sg. imf. DB 1.68 (but -à- perhaps only by influence of pardbartam, JAOS 62.275; 558, $206c).
para + bar- ‘bear away, take-away’: pardbara imf. DB 1.71, 96. pardbartam nsn. past pte. pass. (§242.1) DB 1.62, 67f.
pari- + bar- ‘protect, preserve’ (cf. Hz. Ар 112-3): paribarümiy Ist sg. (8226.]) DNb 17. paribarühy 2d sg. subj. ($27, $136, §222.IT, 4227.1) DB 4.78; paribaráh*-di$ (827, etc.) DB 4.74. pari- barā 2d sg. imv. (5237.1) DB 4.72, 88.
fra- + bar- ‘proffer, grant’: frábara imf. AmH 7; AsH 9; DB 1.12, 25, 60; DPd 3f, 7f; DPh 8; DNa 33; DSf 11; DSm 3°; DSp 2°; D8s 6; DZc 4; DH 7; A’He 18f, 20.
bara- sb. ‘bearmg, bearer’: Av. -bara-, Skt. -bhara-, Gk. -фороѕ, pIE "bhoros ($32, $122, $1431, ҮТ), to root bar- ‘bear’, in aritibara-, takabara-, vacabara-; also bāra- ‘borne by, rider of’, with vriddhi (8122, $126, 5148.1), in asabdra-, ef, usabüri-. See Hz. Ар] 95.
bard- vb. ‘be high’: Ау, baraz- ‘high’, baraz- ant- ‘lofty’, NPers. burz ‘high’, Skt. brhánt- ‘lofty’, OHG berg ‘mountain’, pIE *bhergh-; in Bardiya-, barsan-, probably in brazman-.
Bardiya- sb. Smerdis’, brother of Cambyses ($16411): Elam. bir-h-ia, АКК. bar-zi-ia, Gk. Урёрӧ ($29.02, $30). Репу. (§144.1V) of OP bard- ‘be high’ (575.11): ‘The Exalted’. Bardiya пет. DB 1.30, 32, 39, 52f; 3.25, 35, 54; 4.9, 27, 82; DBb 4f; DBh 5. Bardiyam asm. DB 1.31 bis, 51.
barSan- sb. ‘height, depth’ (S81): Av. barazan- .
(ВМ. AiW 950); deriv. of OP bard- (575.1, $155.1; Scheil 21.26; Konig, Burgbau 51; Hz. AMI 3.57; Bv. Gr. $812; Kent, JAOS 51.204, 99.15). bar$nà ism. (806, $120) DSf 26, 26f.
bav- vb. ‘become, be’: present stem bava- (8213), Av. bavatti, Skt. bhdvati, Gk. ote ‘grows’, Lt. fut ‘I was’, Lith. butt ‘to be’, NEng. be, pIE *bheu-. See also büm:-. bavatiy (§122, §228.1) XPh 55, 56. bæa"ty 3d pl. ($232.1) DNb 14 (башайу in 2d copy, Hz. ApI 115; ef. $48). abavam Ist sg. imf. DB 1.28, 60, 72; 4.5; 5.4^; DSm 6°; XPf 35, 36f; XPh 30; XSe 4°. abava imf. ($228.IT) DB 1.32, 38, 34, 40, 48, 77, 80; 2.16f, 17, 80, 94; 3.10, 11, 20, 27, 28, 76, 82, 83; 5.5, M^, 30; DSf 25; XPf 26.  abava^ 3d pl. imf. ($112, $232.IT) DB 1.76; 2.7, 93; 3.78; 4.34. bavātiy sub). ($222.11, §228.1) DNa 43, 45f; DNb 59 (Lg. 15.74; confirmed by photograph, JNES 444). [biyjä 2d sg. opt. ($114, $218.11, $223.I, $227.11) DB 4.69. буй opt. Cbhy-net, Bv. Gr. $232, comparing Av. buyd{ from *bhu-iët; but ВЫ. Gdr. IP 1. $143 takes as *bhy-i48t, = Lt. fiet, which may be either non-thematie opt. or thematic subj.; $114, $122, 5208, $218.II, §223.1, $228. ID) DB 4.56 bis, 58, 59, 741, 75, 78f, 79°.
bigna-, in d-bigna-, see Bagabigna-.
biimi- sb. ‘earth (= world or ground)’: Av. bümi-, NPers. büm, Skt. (RV) nom. bháümi bhümis; deriv. of root bhav- (see bav-) in grade bhi-, cf. Skt. aor. ábhüt, Gk. ёфо ($11, $65, §152.1V, §179.- IIT).
LEXICON
bümim asf. DNa 2, 32; DSe 2°; DSf 1; DSt 2; DZe 1f; DE 2; XPa 1; XPb 2; XPc 1; XPd 2; XPf 2; ХР 1f; ХЕ 3; XV 2f; A!Pa 2^; A?He 2. ратат, asf. ($55.1) A3Pa 2. bümiyà sf. (8179.IT) DNa 11f; DSb 9; DSe 10; Рб 5; DSs 2°, 3°; DZb 4; DZe 6; DE 17f; XPa 9; XPb 17; XPe 7f; XPd 12; XPf 12, 25; XPh 10; ХР); XE 17; XV 13; A'Pa 18°; A?8e 4°; Wb 7; Wc 8; Wd 8.
BU nsf. ($42) DSf 24, 28.
```


## [2026-09-05T13:47:24.730Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD watkins bher ===\"; grep -n \"bher-\\|bhrater\\|bhrāter\" AHD_watkins1985.txt | head -20",
 "description": "Grep Watkins for bher- and bhrater-"
}
```


### [2026-09-05T13:47:24.776Z] TOOL RESULT

```
=== AHD watkins bher ===
119:The notion of carrying is represented by the widespread root bher-' (BEAR!), found in every branch except Anatolian. This root is noteworthy in that it formed a phrase né- men- bher-, “to bear a name,” which is re- constructible from several traditions, includ- ing English. This phrase formed a counterpart to né-men- dhé-, “to give a name,” with the verb dhé-', “to set, put,” in Sanskrit, Greek, and Slavic tradition. The persistence of these expressions attests the importance of the name-giving ritual in Indo- European society.
144:The BEAVER was evidently known (*bhi- bhru-, from bher-3), at least in Europe, and the MOUSE (mds-) then as now was ubiqui- tous. The HARE, probably named from its color (kas-, “gray”), is also widespread. Do- mesticated animals are discussed below.
155:Male blood relations were designated as bhrater- (BROTHER), which doubtless ex- tended beyond those with a common father or mother; the Greek cognate means “fellow member of a clan-like group.” The female counterpart was swesor- (SISTER), probably literally “the female member of the kin group,” with a feminine suffix *-sor- and the root s(w)e-, designating the self, one’s own group.
333:bher-1. To carry; also to bear children. 1. a. Germanic *beran in (i) Old English beran, to carry: BEAR! (ii) Old English forberan, to bear, endure (for-, for-; see per’): FORBEAR; b. Germanic *bérd in Old English bér, ber, bier: BIER; c. Germanic *bér- in Old Norse bdra, wave, billow: BORE’. 2. a. Germanic *barnam in Old English bearn, child: BAIRN; b. Germanic *barwdn- in Old Eng- lish bearwe, basket, wheelbarrow: BARROW!, 3. a. Ger- manic *burthinja in Old English byrthen, burden: BURDEN}; b. Germanic *burthiz in Old Norse burdhr, birth, akin to the source of BIRTH; C. Germanic *burja- perhaps in Old Norse byrr, favorable wind: BIRR}. 4. Compound root *bhrenk-, to bring (< *bher- + *enk-, to reach; see nek-2), in Germanic *brengan in Old English bringan, to bring: BRING. 5. Latin ferre, to carry: -FER, FERTILE; AFFERENT, CONFER, DEFER!, DEFER®, DIFFER, EFFERENT, INFER, OFFER, PREFER, PROFFER, REFER, SUFFER, TRANSFER, VOCIFERATE. 6. Latin pro- brum, a reproach (< “pro-bhr-o-, “something brought before one”; pro-, before; see per'): OPPROBRIUM. 7. Lengthened o-grade form *bhor- probably in Latin far, thief: FERRET!, FURTIVE, FURUNCLE; (FURUNCULOSIS). 8. Greek pherein, to carry: -PHORE, -PHORESIS, -PHO- ROUS; AMPHORA, ANAPHORA, DIAPHORESIS, EUPHORIA, METAPHOR, PERIPHERY, PHEROMONE, TELPHER, TOCOPH- EROL. 9. Greek pherné, dowry (“something brought by a bride”): PARAPHERNALIA. [Pok. 1. bher- 128.]
334:bher-2. To cut, pierce, bore. 1. Germanic *bordn in Old English borian, to bore: BORE}. 2. Germanic *baru-ga-, castrated pig, in Old English bearg, barg, castrated pig: BARROW’. 3. Germanic *bor-, perhaps in French burin, burin: BURIN. 4. O-grade form *bhor-d- in Latin fordre, to pierce, bore: FORAMEN; BIFORATE, PERFORATE. 5. Per- haps Greek pharunx, throat (< “a cutting, cleft, pas- sage”): PHARYNX. 6. Slavic *bor- in Russian borot’, to overcome: DUKHOBOR. See extension bhreu-'. [Pok. 3. bher- 133.]
335:bher-3. Bright, brown. 1. Suffixed variant form *bhri-no- in Germanic *briinaz in: a. Old English briin, brown: BROWN; b. Middle Dutch bruun (> Dutch bruin), brown: BRUIN; Cc. Old French brun, shining, brown: BRUNET, BURNET, BURNISH. 2. Reduplicated form *bhibhru-, *bhebhru-, “the brown animal,” beaver, in Germanic *bebruz in Old English be(o)for, beaver: BEAVER!. 3. Ger- manic *ber6, “the brown animal,” bear, in Old English bera, bear: BEAR?. 4. Germanic *bernuz in Old Norse bjérn (stem ber-), bear: BERSERKER. [Pok. 5. bher- 136.] bher-4. To cook, bake. Extended root form *bhrig- in Latin frigere, to roast, fry: FRY}. [Pok. 6. bher- 137.] bherdh-. To cut. 1. Zero-grade form *bhrdh- in Germanic *burd-, plank, board, table, in: a. Old English bord, board: BOARD; STARBOARD; b. Old Norse bordh (> Swedish bord), board, table: SMORGASBORD; c. Old French borde, hut, and bort, border: BORDELLO, BORDER. 2. Possibly Latin forfex, a pair of scissors: FORFICATE. [Pok. bheredh- 138.]
342:flagitdre, to demand importunately: FLacitious. [Pok. bhlag- 154.] bhlagh-men-. Form, ritual form. Sanskrit brahmd, brah- man-, priest, and brahma, bréhman-, prayer: BRAHMA!, BRAHMAN, (BRAHMIN). [Pok. bhlagh-men- 154.] bhlé-1. To howl. Probably imitative. 1. Germanic suffixed form *blé-t- in Old English b/gtan, to bleat: BLEAT. 2. Germanic suffixed form *b/é-r- in Middle English bleren, to roar: BLARE. 3. Latin flére, to weep: FEEBLE. [Pok. bAlé- 154.] bhié-2, Also bhla-. To blow. 1. Germanic suffixed form *blé-w- in Old English blawan, to blow: BLow!. 2. Ger- manic suffixed form *blé-dram, “something blown up,” in: a. Old English blZdre, blister, bladder: BLADDER; b. Old Norse bladhra (noun), bladder, and bladhra (verb), to prattle: BLATHER. 3. Germanic extended form *blés- in: a. Old English b/ést, a blowing, blast: BLAST; b. Middle Dutch blas(e), a bladder: stncLass. 4. Variant form *bhid- in Latin flare, to blow (> flabellum, fan): FLABELLUM, FLATUS, FLAVOR; AFFLATUS, CONFLATE, (DEFLATE), INFLATE, SOUFFLE. [In Pok. 3. bhel- 120.] bhlei-. To blow, swell. Extension of bhel-2. 1. Germanic *blajjinén-, a swelling, in Old English blegen, a boil, blister: BLAIN. 2. Perhaps in the Germanic source of Old French blestre, a blister: BLISTER. [Pok. 2. bhiei- 156.] bhleu-. To swell, well up, overflow. Extension of bhel-?. 1. Possibly Germanic *b/aut- in Old Norse blautr, soft, wet: BLOAT. 2. Extended form bhleug~- in Latin fluere, to flow, and -fluus, flowing: FLUCTUATE, FLUENT, FLUERIC, FLUID, FLUME, FLUOR, (FLUORO-), (FLUSH2), FLUVIAL, FLUX; AFFLUENT, CONFLUENT, EFFLUENT, (EFFLUVIUM), (EFFLUX), (FLUORIDE), FLUVIOMARINE, INFLUENCE, (IN- FLUENZA), MELLIFLUOUS, REFLUX, SUPERFLUOUS. 3. Zero-grade form *bhlu- in Greek phluein, phluzein, to boil over: PHLYCTENA. 4. Possibly Greek phloos, phioios, tree bark (< “swelling with growth”): PHLOEM. [Pok. bhileu- 158.] bhlig-. To strike. Latin fligere, to strike: AFFLICT, CON- FLICT, INFLICT, PROFLIGATE. [Pok. bhlig- 160.] bhoso-. Naked. Germanic *bazaz in: a. Old English bzr, bare: BARE!; b. Old Swedish and Old Danish bar, bare: BALLAST. [Pok. bhoso-s 163.] bhrag-. To smell. 1. Germanic *brak- in Old High Ger- man bracc(h)o, dog that hunts game by scent: BRACH. 2. Suffixed form *bhrag-ro- in Latin fragrdre, to smell: FLAIR, FRAGRANT. [Pok. bhrag- 163.] bhrater-. Brother, male agnate. 1. Germanic *brdthar- in Old English bréthor, brother: BROTHER. 2. Latin frdter, brother: FRA, FRATERNAL, FRIAR; CONFRERE, FRATRI- CIDE. 3. Greek phratér, fellow member of a clan: PHRATRY. 4, Sanskrit bhratd, bhrdatar-, brother: PAL. [Pok. bhrdater- 163.] bhreg-. To break. 1. Germanic *brekan in: a. Old English brecan, to break: BREAK; b. Old English bréc, a break- ing: BREACH; c. Old High German brehhan, to break, akin to the Germanic source of Italian breccia, breccia: BRECCIA; d. Old French breier, to break: BRAY?; e. Old French brier (dialectal) and broyer, to knead: BRIOCHE. 2. Germanic *brak-, bushes (< “that which impedes motion”), in Old Norse *brakni, undergrowth, akin to the probable Scandinavian source of Middle English brake(n), bracken: BRACKEN, BRAKE’, BRAKE‘, 3. Nasal- ized zero-grade form *bhr-n-g- in Latin frangere, to break: (FRACTED), FRACTION, (FRACTIOUS), FRACTURE, FRAGILE, FRAGMENT, FRAIL!, FRANGIBLE; ANFRACTU- OUS, CHAMFER, DIFFRACTION, (INFRACT), INFRANGIBLE, INFRINGE, OSSIFRAGE, REFRACT, (REFRAIN?), (REFRIN- GENT), SAXIFRAGE, SEPTIFRAGAL. 4, Latin suffrdgdri, to vote for (? < “to use a broken piece of tile as a ballot”), hence suffrdgium, the right to vote: SUFFRAGAN, SUF- FRAGE. [Pok. 1. bhreg- 165.] bhréi-. Also bhri-. To cut, break. 1. Possibly Latin fricdre (> French frotier), to rub: FRAY?, FRICATIVE, FRICTION, FROTTAGE; AFFRICATE, DENTIFRICE. 2. Possi-
344:bly Latin fridre, to crumble: FRIABLE. 3. In the Celtic source of Vulgar Latin *brisdre, the source of Old French brisier and French briser, to break: BRISANCE; DEBRIS. [Pok. bhréi- 166.] bhrekv-. To cram together. 1. Probably Latin frequens, frequent, crowded: FREQUENT. 2. Suffixed zero-grade form *bhrk~-yo- in: a. Latin farcire, to cram, stuff: FARCE, FARCI, FARCY; INFARCT; b. Greek phrassein, to fence in, enclose, block up: DIAPHRAGM. [Pok. bhareky- 110.] bhrem-'. To growl. 1. Latin fremere, to growl, roar: FREMITUS. 2. Perhaps variant *brem- in Greek bronté, thunder: BRONTOSAUR. [Pok. 2. bherem- 142.] bhrem-2, To project; a point, spike; an edge. 1. Germanic *bréma-, name of prickly shrubs, in: a. Old English brém, broom: BRooM; b. Old English diminutive bremel, brém- bel, bramble: BRAMBLE. 2. Germanic *berm-, *brem-, in: a. Middle English brimme, edge: BRIM; b. Middle Dutch berme, barm, edge of a dike: BERM. [Pok. 1. bherem- 142.] bhres-. To burst. Germanic “brest- in Old English ber- stan, to burst: BURST. [Pok. bhres- 169.] bhreu-'. To cut, break up. Extension of bher-2. 1. Suf- fixed form *bhreu-d- in Germanic *breutan, to break up, in Middle English britel, brittle: BRITTLE. 2. Suffixed form *bhreu-t- in Germanic *breuthan, to be broken up, in Old English bréothan, to deteriorate: BROTHEL. [Pok. 1. bhreu- 169.] bhreu-?. To boil, bubble, effervesce, burn; with deriva- tives referring to cooking and brewing. I. 1. Germanic *breuwan, to brew, in Old English bréowan, to brew: BREW. 2. Germanic *braudam, (cooked) food, (leavened) bread, in Old English bréad, piece of food, bread: BREAD. 3. Germanic *brudam, broth, in: a. Old English broth, broth: BROTH; b. Old French breu, broth (diminutive brouet): BREWIS; IMBRUE. II. Variant form *bhré- in Germanic *brédan, to warm, with derivatives. 1. *bréd-6, “a warming,” hatching, rearing of young, in: a. Old English br��d, offspring, brood: BROOD; b. denominative *brodjan, to rear young, in Old English brédan, to beget or cherish offspring, breed: BREED. 2. Germanic *bré- d6n-, roast flesh, in: a. Old High German brat, brdto (> German Braten), roast meat: BRATWURST, SAUERBRA- TEN; b. Old French braon, meat: BRAWN. 3. Perhaps distantly related is the Germanic source of Old French brese, burning coal, ember (> French braise): BRAISE, BRAZE?, BRAZIER?, BREEZE2, III. Reduced form “bher-, especially in derivatives referring to fermentation. 1. Suf- fixed form *bher-men-, yeast, in: a. Germanic *bermén- in Old English beorma, yeast: BARM, (BARMY); b. further suffixed form *bhermen-to- in Latin fermentum, yeast: FERMENT. 2. Extended form *bherw- in Latin fervére, to be boiling or fermenting: FERVENT, FERVID, (FERVOR); DEFERVESCENCE, EFFERVESCE. IV. As a very archaic word for a spring. 1. Suffixed zero-grade form *bhru- n(e)n- in Germanic *brunnon- in Old English burn, burna, spring, stream: BOURN!, BURN?. 2. Suffixed form *bhréw-r in Greek phrear, spring: PHREATIC. [Pok. bh(e)reu- 143, 2. bher- 132.] bhreus-'. To swell. 1. Suffixed form *bhreus-t- in Ger- manic *breustam, “swelling,” breast, in Old English bréost, breast: BREAST. 2. Suffixed zero-grade form *bhrus-t- in Germanic *brust-, bud, shoot, in Old French broust, brost, shoot, twig: BROWSE. [Pok. 1. bhreu-s- 170.] bhreus-2, To break. 1. Germanic *briisjan, to crush, in Old English brysan, to crush, pound: BRUISE. 2. Suffixed zero-grade form *bhrus-to-, fragment, in Latin frustum, piece: FRUSTULE, FRUSTUM. [Pok. 2. bhreu-s- 171.] bhri-. Eyebrow. Contracted from *bhrua-. 1. Germanic *bris in Old English bri, eyebrow, eyelid, eyelash: BROW. 2. Possibly in the sense of a beam of wood, and perhaps a log bridge, found in Germanic *brugj6 (with cognates in Celtic and Slavic) in Old English brycg(e), bridge: BRIDGE}, [Pok. 1. bhrii- 172, 2. bhrii- 173.] bhrig-. Agricultural produce; also to enjoy (results,
776:sively, very (< *ne-mi-s, “not little”; *mi-, little; see mei-2): NIMIETY. 4. Latin nihilum, nothing (< *nehilum, “not a whit, nothing at all”; hilum, a thing, trifle; origin unknown), contracted to nihil, nil, nothing: NIHILISM, (NIHILITY), NIL; ANNIHILATE. 5. Latin non, not (< *ne-oinom, “not one thing”; *oino-, one; see oi-no-): Non-. 6. Italic *nek, not, in: a. Latin prefix neg-, not: NEGLECT, (NEGLIGEE), NEGOTIATE; b. Latin negdre, to deny: NEGATE; ABNEGATE, DENY, RENEGADE, (RENEGE). 7. Greek né-, not: NEPENTHE. 8. Zero-grade combining form *n- in: a. Germanic *un- in Old English wn-, not: uN-!; b,. Latin in-, not: IN-1; c. Greek a-, an-, not: A-}, (AN-); d. Sanskrit a-, an-, not: AHIMSA, AMRITA. [Pok. ne 756.] nebh-. Cloud. 1. Suffixed form *nebh-lo- in Germanic *nibla- probably in Old Norse nifl-, “mist” or “dark”: NIFLHEIM. 2. Suffixed form *nebh-eld- in: a. Latin nebula, cloud: NEBULA, NEBULOUS; b. Greek nephelé, cloud: NEPHELINE; NEPHELOMETER. 3. Suffixed form *nebh-es- in Greek nephos, cloud: NEPHOLOGY. 4. Nasal- ized form *ne-m-bh- in Latin nimbus, rain, cloud, aura: NIMBUS. See ombhro-. [Pok. (enebh-) 315.] ned-. To bind, tie. 1. O-grade form *nod- in: a. Germanic *nati- in Old English ne¢(t), a net: NET!; b. Germanic *nat-ilo, a nettle (nettles or plants of closely related genera such as hemp were used as a source of fiber), in Old English netel(e), netle, nettle: NETTLE; c. Germanic *nat-sk- in Anglo-Norman nouch, brooch: OUCH?. 2. Lengthened o-grade form *nédo- in Latin nédus, a knot: NODE, NODULE, NODUS; DENOUEMENT. 3. Re-for- mation of the root in Latin nectere (past participle nexus), to tie, bind, connect: NEXUS; (ADNEXA), ANNEX, CONNECT [Pok. 1. ned- 758.] negwh-ro-. Kidney. Greek nephros, kidney: NEPHRO-; MESONEPHROS, METANEPHROS, PERINEPHRIUM, PRO- NEPHROS. [In Pok. eng¥- 319.] negw-ro-. Adjective denoting various colors; with deriva- tives like Greek nebros, “fawn.” Latin niger, black: NEGRO, NIELLO, NIGRESCENCE, NIGRITUDE; DENIGRATE, NECROMANCY, NIGROSINE, [néhw-iz. Near. Germanic root. Old English néah, near: NEAR, NEIGHBOR, NEXT, NIGH.] nei-. To be excited, shine. 1. Suffixed form “nei-to- in Germanic *nitha-, animosity, in Old Norse nidh, scorn (> nidhingr, villain): NIDDERING. 2. Suffixed zero-grade form *ni-to- in Latin nitére, to shine: NEAT!, (NET?). 3. Possibly Persian nil, indigo: ANIL, LILAC. [Pok. 2. nei- 760.) neie-. To lead. Sanskrit nayati, he leads: NAINSOOK. [Pok. 1. nei- 760.] neig’-. To wash. Germanic *nikwiz, *nikuz in Old High German nihhus, river monster, water spirit: NIx!. [Pok. neigt- 761.] nek-', Death. 1. Latin nex (stem nec-), death: PERNI- cious. 2. Latin necdre, to kill: INTERNECINE. 3. Suffixed (causative) o-grade form *nok-eyo- in Latin nocére, to injure, harm: NOCENT, NOCUOUS, NUISANCE; INNOCENT, INNOCUOUS. 4. Suffixed o-grade form *nok-s- in Latin noxa, injury, hurt, damage: NOXIOUS; OBNOXIOUS. 5. Suffixed full-grade form *nek-ro- in Greek nekros, corpse: NECRO-, NECROSIS; NECROMANCY. 6. Greek nek- tar, the drink of the gods, “overcoming death” (*tar-, overcoming; see ter@-2): NECTAR, (NECTARINE). [Pok. nek- 762.] nek-?. To reach, attain. I. O-grade form *nok- in Ger- manic *ga-nah- (*ga-, intensive prefix; see kom), “satis- fies,” forming *gandga-, sufficient, in Old English gendg, enough: ENOUGH. II. Variant form “enk-. 1. Redupli- cated in Greek enenkein, to carry, whence onkos, a burden, mass, hence a tumor: ONCOGENESIS, ONCOLOGY. 2. Compound root *bhrenk- (see bher-'). [Pok. enek- 316.] nekw-t-. Night. O-grade form *nokv-t-. 1. Germanic *naht- in Old English niht, neaht, night: NIGHT. 2. Latin
1078:a. Latin téla, web, net, warp of a fabric, also weaver’s beam (to which the warp threads are tied): TILLER?, ToiL2; b. Latin subtilis, thin, fine, precise, subtle (< *sub-téla, “thread passing under the warp,” the finest thread; sub, under; see upo): SUBTLE. 3. Suffixed form *teks-On, weaver, maker of wattle for house walls, builder (possibly contaminated with *teks-tdr, builder), in Greek tekton, carpenter, builder: TECTONIC; ARCHITECT. 4. Suf- fixed form *teks-nd-, craft (of weaving or fabricating), in Greek tekhné, art, craft, skill: TECHNICAL, POLYTECHNIC, TECHNOLOGY. 5. Possibly Germanic *thahsu-, badger (“the animal that builds,” referring to its burrowing skill), in Old High German dahs (> German Dachs), badger but more likely borrowed from the same pre- Indo-European source as the Celtic totemic name Tazgo-, Gaelic Tadhg, “‘badger’”): DACHSHUND. [Pok. tekth- 1058.] tekv-. To run, flee. Suffixed o-grade form *tokv-so- in Iranian *taxsa-, bow, borrowed into Greek toxon, bow, also (in the plural) bow and arrow (< “that which flies’): Toxic. [Pok. tekz- 1059.] tel-. Ground, floor, board. 1. Germanic *thil-j6- in Middle Low German and Middle Dutch dele, plank: DEAL?. 2. Suffixed form *tel-n- in Latin telliis (stem telliir-), earth, the earth: (TELLURIAN), (TELLURIC), (TELLURION), (TELLURIUM), TELLURO-. 3. Possibly reduplicated form *ti-tel- in Latin titulus, placard, label, superscription, title: TITLE. [Pok. 2. tel- 1061.] tela-. To lift, support, weigh; with derivatives referring to measured weights and thence to money and payment. 1. Suffixed form *telo-mon- in Greek telamén, supporter, bearer: TELAMON. 2. Suffixed form *tel/a)-es- in: a. Greek telos, tax, charge: TOLL!; PHILATELY; b. Latin tolerdre, to bear, endure: TOLERATE. 3. Suffixed zero-grade form *th-i-, becoming *tali- (influenced by ¢dlis, such), in Latin ¢alid, reciprocal punishment in kind, “something paid out”: TALION; RETALIATE. 4. Suffixed variant zero-grade form *tala-nt- in Greek talanton, balance, weight, any of several specific weights of gold or silver, hence the sum of money represented by such a weight: TALENT. 5. Perhaps intensive reduplicated form *tantal- in Greek Tantalos, name of a legendary king, “the sufferer’: (TANTALIZE), TANTALUS. 6. Perhaps zero-grade form *tla- in Greek Atlas (stem Atlant-), name of the Titan supporting the world: ATLANTIC, ATLAS. 7. Suffixed zero-grade form *tl-é- in Germanic *thulén in Old English tholian, to suffer, endure: THOLE. 8. Suf- fixed zero-grade form *tl-to- in Latin ldtus, “carried, borne,” used as the suppletive past participle of ferre, to bear (see bher-'), with its compounds: ABLATION, COL- LATE, DILATORY, ELATE, ILLATION, LEGISLATOR, OB- LATE], PRELATE, PROLATE, RELATE, SUPERLATIVE, TRANSLATE. 9. Suffixed zero-grade form *tl-d- in San- skrit tuld, scales, balance, weight: TAEL, TOLA. 10. Nasal- ized zero-grade form *tl-n-a- in Latin tollere, to lift: EXTOL. [Pok. 1. éel- 1060.] tem-. Also teme-. To cut. I. Form *tema-. Nasalized form *t(e)m-n-a- in Greek temnein, to cut: TMESIS, TOME, -TOME, -TOMY; ANATOMY, ATOM, DIATOM, DICHOTOMY, ENTOMO-, EPITOME. II. Form *tem-. 1. Suffixed form *tem-lo- in Latin templum, temple, shrine, open place for observation (augury term < “place reserved or cut out”), small piece of timber: TEMPLE!, TEMPLE’; CONTEMPLATE. 2. Extended root *tem-d- becoming *tend- in o-grade suffixed (iterative) form *tond-eyo- in Latin tondére, to shear, shave: TONSURE. [Pok. 1. tem-, tend- 1062.] teme-. Dark. Suffixed form *tema-s-. 1. Latin temere, blindly, rashly: TEMERARIOUS, TEMERITY. 2. Suffixed form *temas-rd- in Latin tenebrae (plural), darkness: TENEBRAE, TENEBRIONID. [Pok. tem()- 1063.] temp-. To stretch. Extension of ten-. 1. Possibly Latin tempus, temple of the head (? where the skin is stretched from behind the eye to the ear): TEMPLE?. 2. Zero-grade form *tmp- perhaps in: a. Persian taftan, to weave (the
1218:AEDILE aidh- AEGIS aig- AENEOUS ayes- AEOLIPILE pulé AEPYORNIS OrF- AERIAL wer-2 AERO- wer-2 AEROBE gWei- AERODYNE deu-2 AERONAUT nau-2 AESIR ansu- AESTHETIC au-5 AESTIVAL aidh- AETHER aidh- AFFABLE bha-2 AFFAIR dhé-1 AFFECT! dhé-1 AFFECT? dhé-1 AFFECTION dhé-1 AFFERENT bher-1 AFFIANCE bheidh- AFFIANT bheidh- AFFIDAVIT bheldh- AFFILIATE dhé(i)- AFFIRM dher-2 AFFIX dhigy- AFFLATUS bhié-2 AFFLICT bhiig- AFFLUENT bhleu- AFFORD pert AFFOREST dhwer- AFFRAY  pri- AFFRICATE bhréi- AFFUSION gheu- AFTER apo- AFTERMATH mé-4 AGAIN gagina AGAINST gagina AGALACTIA melg- AGAPANTHUS andh- AGE aiw- AGENDUM ag- AGENT ag- AGERATUM gere-1 AGGLOMERATE gel-1 AGGLUTINATE gel-1 AGGRAVATE gWere-2 AGGREGATE ger-? AGGRESS ghredh- AGGRIEVE gWere-2 AGHAST gheis- AGILE ag-
1239:AMITY amma AMMUNITION mei-3 AMNESIA men-! AMNESTY men-1 AMNIOCENTESIS kent- AMOEBA mel-1 AMONG mag- AMORETTO amma AMORTIZE mer-2 AMOUNT ad-, men-2 AMOUR amma AMPHI- ambhi AMPHIBIOUS gWei- AMPHIBOLE gWelg-1 AMPHIBRACH mregh-u- AMPHIMACER mak- AMPHIMIXIS meik- AMPHIOXUS ak- AMPHISBAENA gWa- AMPHISTYLAR sta- AMPHITHECIUM dhé-1 AMPHORA bher-1 AMPHOTERIC ambho AMPHYCTYONY  tkei- AMPLEXICAUL kaul-, plek- AMPLIFY dhé-1 AMPUTATE peu- AMRITA mer-2, ne AMYLUM mele- AN! oi-no-
1242:ANA- an! ANABAENA gWa- ANABAPTIST g¥ébh-1 ANABIOSIS gWei- ANACOLUTHON sem-! ANACRUSIS kreue-2 ANADEM dé- ANADIPLOSIS dwo- ANADROMOUS der-1 ANAGLYPH gleubh- ANAGOGE ag- ANALCIME = alek- ANALECTS leg-1 ANALEPTIC (s)lag¥- ANALOGOUS leg-! ANALYSIS leu-1 ANAMNESIS men-1 ANAPEST peu- ANAPHORA bher-? ANARTHROUS ar- ANASARCA twerk- ANASTOMOSIS ste-men- ANASTROPHE  streb(h)- ANATHEMA dhé-1 ANATOMY tem- ANCESTOR ked- ANCHOR ank- ANCHORITE ghé- ANCIENT! ant- ANCILLARY kWel-1 ANCON ank-
1276:BABA baba- BABBLE baba- BABE baba- BABKA baba- BABU baba- BABUSHKA baba- BABY baba- BACILLUS bak- BACTERIUM bak- BACULIFORM bak- BAGEL bheug-3 BAGUETTE bak- Bails bheug-3 BAIRN bher-1 BaIT! bheid- BAKE bhé- BAKSHEESH bhag-' BALALAIKA baba- BALCONY bhelg- BALE! bhel-2 BALE? bhelu- BALEEN bhel-2 BALK bhelg- BALL! bhel-2 BALL2 gWele-1 BALLAD gWele-1 BALLAST bhoso-, kla- BALLET gWela-1 BALLISTA gWele-1 BALLOON bhel-2 BALLOT bhel-2 BALLOTTEMENT bhel-2 BAMBINO _baba- BAN! bha-2 BANAL bha-2 BAND! bhendh- BANDANNA bhendh- BANDIT bha-2 BANDOLEER bha-1 BANDORE pandoura BANE gWhen-1 BANG! bheg- BANIAN wen-1 BANISH bha-2 BANK! bheg- BANK? bheg- BANK? bheg- BANKRUPT bheg-, reup- BANNER bha-! BANNERET bha-1 BANNS bha-? BANQUET bheg- BANQUETTE bheg- BANSHEE gWen- BANTLING bheg- Baptist gébh-!
1278:BAPTIZE gWébh-1 BAR? gWere-2 BARB! bhardha BARBARIAN baba- BARBARISM baba- BARBAROUS_ baba- BARBEL bhardha BARBELLATE bhardha BARBER bhardha BARBETTE bhardha BARBICEL bhardha BARBULE bhardha BARD! gWera-3 BARE! bhoso- BARGAIN bhergh-? BARITE gWera-2 BARITONE gWera-2 BARIUM gWera-2 BARK! bherg- BARLEY bhares- BARM_ Dbhreu-2 BARMY bhreu-2 BARN bhares- BARO- gWera-2 BAROUCHE dwo-, ret- BARROW! bher-1 BARROW? bhergh-2 BARROW’ = bher-2 BARYON gWere-2 BARYSPHERE gWere-2 BARYTA gWere-2 BASCULE (s)keu- BASE! gWa- BASE? bassus BASIS gWa- BAS-RELIEF bassus Bass! bhar- Bass? bassus BASSET! bassus BASSO bassus BAT? bhiag- BATE? battuere BATEAU bheid- BATH! bhé- BATHE bhé- BATHOS gWadh- BATHY- gWadh- BATHYSCAPH skep- BATTEN! bhad- BATTERY battuere BATTER! battuere BATTER’ battuere BATTLE battuere BAWD bhel-2 BAWL bhel-4 Bay? bat-
1280:BE- ambhi BEACON bha-1 BEAD gWhedh- BEADLE bheudh- BEAM bheue- BEAN bha-bha- BEAR! bher-1 BEAR? bher-3 BEARD bhardha BEAT bhau- BEATIFIC deu-2, dhé-1 BEATIFY deu-2 BEATITUDE deu-2 BEAU deu-2 BEAUTY deu-2 BEAVER! bher-3 BECHE-DE-MER mori- BECK? bheg¥- BECKON bha-! BECOME gWa- BED bhedh-
1294:BENIGN deu-?, gene- BENTHOS gWadh- BENUMB nem- BEQUEATH gWet-2 BEQUEST gWet-2 BEREAVE reup- BERM bhrem-2 BERRY bha-1 BERSERKER bher-3 BESPEAK spreg- BESPRENT spergh- BEsT bhad- BETOKEN deik- BETRAY d6- BETROTH deru BETTER bhad- BETWEEN dwo- BETWIXT dwo- BEVEL bat- BEVERAGE pO(i)- BEWITCH weik-2 BEZOAR gWhen-1, pa- BHAGAVAD-GITA g@i-2 BI- dwo-
1297:BIER bher-1 BIFORATE bher-2 BIGEMINAL yem- BIGHT bheug-3
1304:BIRR! bher-1 BIRTH bher-1
1314:BOOM? bheue- BOON! pbha-2 BOON2 deu-2 BOOR bheue- BOOT? bhad- BOOTH bheue- BORDELLO bherdh- BORDER bherdh- BORE! bher-2 BORE’ bher-1 Boreas gWero-1 BOROUGH bhergh-2 BORROW bhergh-1 BORSCHT bhar- BOSCAGE busk- BOSOM beu-1 BOTH ambh6o BOTHRIUM bhedh- BO TREE bheudh- BOTTOM bhudh- BOTTOMRY bhudh- BOTULIN gWet-3 BOTULINUM gWet-3 BOTULISM gWet-3 BOUCLE beu-1 BOUGH bhaghu- BOUILLABAISSE beu-! BOUILLON beu-1 BOULDER bhel-2 BOULE! gWele-1 BOULE? beu-! BOULEVARD bhel-2, werg-
```


## [2026-09-05T13:47:25.897Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN grep baradar ===\"; grep -n \"brâdar\\|barâdar\\|Bruder\" HRN.txt | head -20\necho \"=== SOD grep br't ===\"; grep -n \"brother\" SOD_pages.txt | head -20",
 "description": "Grep Horn and Sogdian dictionary"
}
```


### [2026-09-05T13:47:25.962Z] TOOL RESULT

```
=== HRN grep baradar ===
2091:ü:^. hiräder *Bruder .
2092:a ap. hrätar^ *Bruder' ; aw. bratar^; phlv. brätar, brät ^);
2095:*Bruder, t. arwäd 'Verwandter* (30); bei. brät n.
=== SOD grep br't ===
5154:    brother                        r                                 C2, 31V21 n p 76-7; STSC 104, >brtw
6011:       brother
9918:            humdan                                                      brother
11527:     brother                                                 2717 pr»y B, M                                     ._^^
11532:         "brothers" SCE 36, 55; GMS 944, 1231; KG                  STii 8.11; TSP 6.114; Sogdica. 2.2, 4
32977:         lay brother                                                 lamb
37836:brother     479, 789, 2131, 2704                                                   0<?)cast 7488, 7493
38746:lay brother      10120                     (to)let      7359, 9792                  likeness      7424
```


## [2026-09-05T13:47:38.576Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN context 2080-2100 ===\"; sed -n '2080,2100p' HRN.txt\necho \"=== formfeeds before 2091 ===\"; awk 'NR<=2091{c+=gsub(/\\f/,\"\")} END{print c}' HRN.txt",
 "description": "Print Horn birader entry with page"
}
```


## [2026-09-05T13:47:40.941Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD entries 479 789 2131 2704 ===\"; grep -n \"^ *479 \\|^ *789 \\|^ *2131 \\|^ *2704 \\| 479 \\| 2131 \" SOD_pages.txt | head -20\necho \"=== grep Brw't / prʾt ===\"; grep -n \"βrʾt\\|brʾt\\|βr'\\''t\\|br't\" SOD_pages.txt | head -20",
 "description": "Find Sogdian brother entry"
}
```


### [2026-09-05T13:47:42.637Z] TOOL RESULT

```
=== HRN context 2080-2100 ===
2) Phlv. barin 'höchster*.— 45 —
ap. upariy 'über; aw. upairi; phlv. apar, päz. awar,
apartar, apartum; ai. upäri.
kurd. her; af/. pre- (LW. bar); oss. d. uol, t. 0/ *das
Obere*, välä Postpos. auf, über* (253) ; bei. par n. par
(283), resp. gvar (136); wa/. sar. war,
Geiger, Etymol. des Balü^i s. v. gvar (136), macht
darauf aufmerksam, dass in np. her eine von her
*Brust' gebildete nominale Praeposition und upari zu-
sammengeflossen sind. Np. her- kommt auch als Prae-
fix vor.
ü:^. hiräder *Bruder .
a ap. hrätar^ *Bruder' ; aw. bratar^; phlv. brätar, brät ^);
p/;^ ai. bhrdtar-; arm. ekbair (H. No. 91).
' kurd. barä; afy. wrör; oss. d. arwäde, erwOde
*Bruder, t. arwäd 'Verwandter* (30); bei. brät n.
bräs etc. (38); wa/. wrüt, si/n. w'rod, sar. wrödy
sangl. tt'wrd.
193. herä» *Schmuck, Schönheit*, berüzlden, berOzis^),
aw. bräza-f brOzaiü 'er strahlt'; phlv. braz(i)sah
geschmückt*, braz(i)saklh (AV.) ; ai. bhrajd-, bhrajate
=== formfeeds before 2091 ===
66
```


### [2026-09-05T13:47:43.245Z] TOOL RESULT

```
=== SOD entries 479 789 2131 2704 ===
5151:479 'pr't'r B                                            ^          aParte, arhbarte ? ©pp.; pi. -/ ^nPrt'kw
6008: 789 TY(vv) S, B                                     (»^ji          807 'kr'tk'ry B                                  fUSI,j-P
9916:                                                                   2131 >XY S                                       <>0A*
11524:2704 pr>t B, M, S                                       ^         Praxs =*brxs-, Pr'ys-, prys-
23894:      TSP 2.175                                                      Hen. Tales. 478.19, 479 n 2
23949:        Sogdica. 29.5a; Hen. Tales. 479 n 2                         TSP 2.339, 1232, 5.1, 113, 6.42; KG 411; GMS 537
=== grep Brw't / prʾt ===
11525:     Prat (pr*tf br't, pr>tr) ©<bratar      ©ob. -y; voc.         0c>)shoot,0o)throw
11537:2705 br't     C =» pr>t                                            (to)scnd
20087:         n (nbr'trty, ndywyd, np*ryqty) ©<ana ©conj.                  5716 n'p B, S           (uy> y^ jj)j>^*\o1»yv*
20597:5870 nbr'trty     C = n+br}trty =» n-, Pr't                     5887 nfryyn M                                       y^a
20598:5871 nbr'ty     C = n+br>ty =» n-, Pr>t                              nifrin (nfryn)
32360:      wipaz, uPaz ©Av. vibdzu                                 9929 wbr't C = w+br>t =» w-, Pr't
```


## [2026-09-05T13:47:51.511Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=11527 && /\\[pdf page/ {last=$0; ln=NR} END{print ln\": \"last}' SOD_pages.txt\nsed -n '11520,11540p' SOD_pages.txt",
 "description": "Find SOD page for entry 2704"
}
```


### [2026-09-05T13:47:54.020Z] TOOL RESULT

```
: 
                                                                   (rc)be roasted
          pr}yst-
       (to)scnd                    v                               GMS 825; Sogdica. 40.12; AVS 73
       Hen. Tales. 478.25                                    2716 prJxs- S                       j^-W^f^s^
2704 pr>t B, M, S                                       ^         Praxs =*brxs-, Pr'ys-, prys-
     Prat (pr*tf br't, pr>tr) ©<bratar      ©ob. -y; voc.         0c>)shoot,0o)throw
        -'; pi. -f; ob, pi. -ty                                   MSP b26, 92; impf. /?Vxs, MSP bl55
     brother                                                 2717 pr»y B, M                                     ._^^
                                                                  pare =»PrJk\ Pryy, bry
       GMS 307, 940; Frag. Lcn.; BBB 540; MSP M70-
         1; STi 33.15; STii 6.2; C2 gloss.; prhrt, brhrU          fruit

         "brothers" SCE 36, 55; GMS 944, 1231; KG                  STii 8.11; TSP 6.114; Sogdica. 2.2, 4
         348; STi 26.3; STii 6.18; C2 gloss, voc. pi. C2,    2718 pr'ys- S                                o>\z~j
         12R28, 48R27;Sund. AoFviii 1981 p214; BBB                frais ©OP frdisaya-- *fra-aisaya ©impf.
         f41, 544; Frag. Lcn. 92.9
                                                                     ftrys(y) =»prys-, frys-, pr'ys-1
2705 br't     C =» pr>t                                            (to)scnd
                                                                   MDii; MSP bl24; Frag. Len. 44.12; AVS 128
2706 prJtr ** >pr)t>r, prH
2707 pr>trt =» Pr»t                                          2719 pr'yst- S                                     o*^J
```


## [2026-09-05T13:47:58.354Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"pdf page\" SOD_pages.txt | head -3\nawk 'NR<=11527 && /pdf page/ {last=$0; ln=NR} END{print \"last tag before 11527: line \"ln\": \"last}' SOD_pages.txt",
 "description": "Locate SOD pdf page tags"
}
```


### [2026-09-05T13:48:00.945Z] TOOL RESULT

```
last tag before 11527: line :
```


## [2026-09-05T13:48:04.750Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=11527{c+=gsub(/\\f/,\"\")} END{print \"leaf(0-based)=\"c, \"printed≈\"c-66}' SOD_pages.txt",
 "description": "Compute SOD printed page for brāt entry"
}
```


### [2026-09-05T13:48:07.283Z] TOOL RESULT

```
leaf(0-based)=172 printed≈106
```


## [2026-09-05T13:48:16.919Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN brother ===\"; grep -n \"brother, fr. ME\\|brother, n\\.\" KLN_1966.txt | head -10\necho \"=== KLN bear v ===\"; grep -n \"OE beran\\|OE. beran\" KLN_1966.txt | head -10",
 "description": "Grep Klein for brother and bear"
}
```


### [2026-09-05T13:48:16.990Z] TOOL RESULT

```
=== KLN brother ===
=== KLN bear v ===
```


## [2026-09-05T13:48:18.816Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC ambh ===\"; grep -n -i \"ambh.*bhor\\|ambhor\\|amphoreus\" IEC.txt | head -20\necho \"=== IEC leaf24-26 head ===\"; for n in 24 25 26; do echo \"-- NR=$n --\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' IEC.txt | head -5; done",
 "description": "Grep Mann IEC for ambhor"
}
```


### [2026-09-05T13:48:20.517Z] TOOL RESULT

```
=== IEC ambh ===
496:ambhor-, ambhr- (for ambh-bhor, -bhr-, cf. ambhóo and bher-, bhor-) *«two-handled vessel. Skt. ambhrnahb: Per. ambar; Myc. and Gk. amphoreüs, amphiphoreus; LW in Lat. am- phora; OHG ampri; OE amber, embren; Du. emmer; Sw. (fr. LG) ámbar; LW fr. Eng. in Mir ambur, ammor, Ir. umar ‘trough’. LW fr. Gmc. in OCS oborükü ‘peck-measure’; Pol. weborek ‘pail and in OPr. wumbaris; Finn. ämpäri. (Note: G Eimer, OHG einbar derives fr. a type *oin-bhor- *one-handled vessel. G Zuber is from an R-grade, of type *du- bhor-, reduced from *dui-bhor-)
=== IEC leaf24-26 head ===
-- NR=24 --
 of the evidence is ambigu- ous. For Gk. *álthomai, althaino, álthos — omitted by Bois. and Hof. — see uldh-; íor Holth. the Gk. forms equate with ON aldinn, aldin ‘fruit’. Cf. also uoldh-)
ale$-(?), al$-(?) “sorrow, suffering’. Cf. WP I, 160; II, 423 note. Cf. alg-, sulg-. Oss. älğ (ambig.) “nausea”. (For speculations see Bois: alégo, etc., and WH & EM: neg- ligo, diligo)
aleio “grind, pound, crush'. Cf. aleuro- Hind.Beng. cf. ata, Guj. ato, Romani arno, andro, aro; Per. ard (ambig. “flour”, perhaps to Gk. ártos “bread”. Bois. and Hof. uncertain); Arm. ayam ‘grind’; Gk. aléo, v., aletós, s. Cf. Myc. (queried) aletere-, pl. *millers'
áleið, al- ‘rove, roam’. Cf. aleuos Per. cf. àv-ara, cpd. adj. ‘wandering’; Gk. &lásko, elaíno (Dor.-à-), beside áláomai; Lat. cf. the synthetic cpd. (apparently with an aph- etic px.) p-àlor, palari ‘wander’. Cf. for the px. pono, positum; pars: ars; parco: arx; pudeo (for *po-uideo “look down (?), w. the semantics of R po-zor); Latv. aleties *be rest- less
aleks-, alks- "ward off, protect. WP I, 89. Cf. alkos Skt. raksami; Arm. ayxem ‘bolt, bar; Myc. & Gk. aléxo, alexéo
-- NR=25 --
ill, all- “other? beside ail ‘second’;
10
20
25
30
-- NR=26 --
ers'
altos, ios 'high; height, fortress, sacred grove'. WP I, 86. Cf. alo (1) Skt. attah; Hitt. halcis ‘fortress’; Gk. Altis; Lat. altus; MIr. alt; Gaul. alto-; MW allt ‘grove’; Cor. als; Br. aot, pl. -u and ao&u “shore?
alus, u (?) “an edible root or tuber’. WP I, 56 Skt. aluh; Lat. alum (wrongly identified as
15
20
```


## [2026-09-05T13:48:32.100Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=496{c+=gsub(/\\f/,\"\")} END{print \"leaf(0-based)=\"c, \"printed≈\",(c-15)*2, \"to\", (c-15)*2+1}' IEC.txt\nsed -n '490,500p' IEC.txt",
 "description": "Compute IEC page for ambhor"
}
```


### [2026-09-05T13:48:33.867Z] TOOL RESULT

```
leaf(0-based)=26 printed≈ 22 to 23
ambhi (ombhi, mbhi) *on both sides; around, at. WP I, 54. Cf. abhi Myc. api (for *amphi); Gk. amphí; Illyr. ambi-; Alb. mbi, mbé; Lat. Osc. Umb. am-; Lat.
19 ambhi-quolos (ombhi-, mbhi-) — amtlos, om (amətrom)
(also) amb-; Olr. imb, imm; Ir. im, mí, um; cf. also Olr. imbe ‘fence’; Gaul. ambi-; OBrit. am-, aim-, em-; W am; Br. am; OE ymbe; OHG umbi, umbe; ON umb, um
ambhi-quolos (ombhi-, mbhi-) ‘circulating; servant Myc. api-qolo- (*amphiqwolos); Gk. amphi- polos: OLat. anculus. Cf. Skt. abhicarah (fr. *mbhiquelos), and Cz. (ambig.) úkol ‘task’
ambhmn- (ombhmn-, period". WP I, 41 - Arm. (ambig.) am (i-stem: ‘year’. Cf. samos}; Oss. cf. anz (cyear: Li. amžius "age Lat. cf. soll-emnis “annual, ritual’; OLat. per- emnis ‘annual’; MIr. amm “point of time’; Gael. ám, id.; Sequanian amn, amb, am ‘time’; cf. the cpd. am-ser (“time in W. Br.OBrit.Cor.); ON cf. imbru-dagar ('ember-days', fr. *ambheso); OE ymbryne; ymbren; WG imbs *wine-festival
ambhó (ombho, mbhó) ‘both’. WP I, 55. Cf. abh- Arm. cf. am- in am-ordziK “both testicles’; Gk. ámpho; Lat. ambo; Tokh. cf. A àmpi; antapi, antpi (a cpd. form?). (The vocalism of Skt. ubhá, -au is obscure)
ambhor-, ambhr- (for ambh-bhor, -bhr-, cf. ambhóo and bher-, bhor-) *«two-handled vessel. Skt. ambhrnahb: Per. ambar; Myc. and Gk. amphoreüs, amphiphoreus; LW in Lat. am- phora; OHG ampri; OE amber, embren; Du. emmer; Sw. (fr. LG) ámbar; LW fr. Eng. in Mir ambur, ammor, Ir. umar ‘trough’. LW fr. Gmc. in OCS oborükü ‘peck-measure’; Pol. weborek ‘pail and in OPr. wumbaris; Finn. ämpäri. (Note: G Eimer, OHG einbar derives fr. a type *oin-bhor- *one-handled vessel. G Zuber is from an R-grade, of type *du- bhor-, reduced from *dui-bhor-)
amelom (omelom) (?) *a semi-parasitic plant (mistletoe? ivy?y Lat. cf. (bapax) alimon (for *amilon, a plant injurious to trees); OCz. jmelo (spurge-olive? or sim.); Slovak omelo ‘mistletoe’; R oméla, id.; Pol. jemioła; Li. àmalas. (Note: the origin of Lat. amellus ‘aster’, and of G Mistel ‘mistletoe’ is uncertain)
mbhmn-) “circuit,
20
25
```


## [2026-09-05T13:48:44.262Z] TOOL CALL #26: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-05T13:48:44.270Z] TOOL RESULT

```


```


## [2026-09-05T13:48:46.559Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON فسفر ===\"; grep -n \"فسفر\" MON_part1.txt MON_part2.txt | head -10\necho \"=== ARY انبر ===\"; grep -n \"انبر\" incoming/ARY/ARY_pages.txt | head -20",
 "description": "Grep Mo'in for fosfor and Aryanpur for anbor"
}
```


### [2026-09-05T13:48:46.635Z] TOOL RESULT

```
=== MON فسفر ===
MON_part1.txt:79392:فسفرسانس پیدا می‌کند و روشنی خاص 
MON_part1.txt:80275:سنگ روشنایی: به فسفر وترکیبات کانی آن 
MON_part1.txt:88331:فسفر که جامد است ترکیب و به کلرور فسفر 
MON_part2.txt:3707:کرین و فسفر جامد هستند و تنها برم 
MON_part2.txt:7342:فسفریکك هستند و برای کودهای شیمیایی 
MON_part2.txt:7351:فسفر: 10:60 (.) (شیم.) جسمی است 
MON_part2.txt:7357:فسفر مایع در ۲۸۷ درجه می‌جوشد (السته 
MON_part2.txt:7360:فسفر ۱۱۴ یعنی مولکول فسفر چهار اتمی 
MON_part2.txt:7361:است. فسفر به دو صورت مختلف که 
MON_part2.txt:7363:وجود دارد: قسفر سفید و فسفر سرخ. گرب 
=== ARY انبر ===
```


## [2026-09-05T13:48:51.688Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '7335,7375p' MON_part2.txt\necho \"=== nearby page numbers ===\"\nawk 'NR>=7300 && NR<=7400 && /^[0-9]{3,4}$/{print NR\": \"$0}' MON_part2.txt\ngrep -n \"۲۵۴۶\\|2546\" MON_part2.txt | head -5",
 "description": "Read Mo'in fosfor entry"
}
```


### [2026-09-05T13:48:53.442Z] TOOL RESULT

```
فسطاط: -6۶؛ ,اقاده) [ع.] (ا.) خیمه 


۹ ۱ ۱ 
۹ فساطط. . (غم.) 

فسفات: (شیم.) املاح اسید 
فسفریکك هستند و برای کودهای شیمیایی 
دگار می رو ند. فسفات‌های قلیابی مانند 
فسفات سدیم و پتاسیم و آمونیم در آب 
محلول هستند و فسفات‌های دیگر در آب 
غیر محلول ولی در اسیدها محلولند. 
فسفات‌ها با نیترات نقره رسوب زرد فسقات 
نقره تولید می‌کنند که در اسید از تیک و 
آمونيااک هر دو حل می‌شود. 

فسفر: 10:60 (.) (شیم.) جسمی است 
جامد زرد رنگ که سطح آن به رنگ 
قهوه‌یی يا سفید است. بوی سیر می‌دهد و در 
آب غیر محلول است و چون در هوا فاسد 
می‌گردد آن را در آب نگه می‌دارند. از آب 
سنگین‌تر و در ۴۳۴ درجه ذوب می‌شود. 
فسفر مایع در ۲۸۷ درجه می‌جوشد (السته 
در محیطی بدون اکسیژن) و تکاثف نسبی 
بخار آن نشان می‌دهد که جرم مولکولی 
فسفر ۱۱۴ یعنی مولکول فسفر چهار اتمی 
است. فسفر به دو صورت مختلف که 
خواص آنها کاملاً مشخص و ممتاز است؛ 
وجود دارد: قسفر سفید و فسفر سرخ. گرب 
فسفر سفید نور تابد قرمز می‌شود. فسفر 
سرخ آتشگیر نیست و سمیت ندارد ولی 
فسفر سفید از خطرناکترین سم‌ها است. فسفر 
در آب غیر محلول است ولی در بنزین و 
سولفور کربن حل می‌شود و محلول آن 
سیار آتشکیر و خطرناکك است. چکالی 
فسفر سفید ۱/۸۴ و چگالی فسفر سرخ 
۸ است. 

فس فس: 6-5 (ق.) (عم.) به کندی» به 
7 

=== nearby page numbers ===
```


## [2026-09-05T13:49:03.227Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0er-",
 "prompt": "Give the root form, gloss, and list the descendants especially Proto-Indo-Iranian/Old Persian/Avestan, Greek pherein, Latin ferre, Proto-Germanic *beraną. Quote key lines."
}
```


## [2026-09-05T13:49:04.801Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0r%C3%A9h%E2%82%82t%C4%93r",
 "prompt": "Give the reconstructed form, gloss, and descendants: Proto-Indo-Iranian, Avestan, Old Persian, Proto-Germanic, Latin, Greek. Quote key lines."
}
```


### [2026-09-05T13:49:10.475Z] TOOL RESULT

```
# Proto-Indo-European Root *bʰer-

**Root Form:** *bʰer- (imperfective)

**Gloss:** "to bear, carry"

## Key Descendants

**Proto-Indo-Iranian:**
- *bʰárHmā (Proto-Indo-Aryan) → Sanskrit भरीमन् (bhárīman)
- *bʰárHtram (Proto-Indo-Aryan) → Sanskrit भरित्र (bharítra, "arm")

**Ancient Greek:**
- φέρω (phérō, "to bear/carry") derived from thematic *bʰér-e-ti
- φέρετρον (phéretron, "bier, litter")
- φερνή (phernḗ)

**Latin:**
- Derived forms include fortūna from *bʰr̥-tew-n-éh₂

**Proto-Germanic:**
- *beraną (see there for further descendants)
- *burjaną (from yé-present *bʰr̥-yé-ti)

## Representative Quote

The entry states: "to bear, carry" as the primary meaning, with the root classified as an "imperfective" aspect marker in Proto-Indo-European morphology.
```


### [2026-09-05T13:49:16.086Z] TOOL RESULT

```
# Proto-Indo-European *bʰréh₂tēr

**Reconstructed Form:** *bʰréh₂tēr (masculine noun)

**Gloss:** "brother"

## Key Descendants

**Proto-Indo-Iranian:** *bʰráHtā

**Proto-Germanic:** *brōþēr

**Proto-Italic:** *frātēr (leads to Latin frāter)

**Proto-Hellenic:** *pʰrā́tēr (leads to Greek)

## Notable Quote

The article states: "This lexeme is widespread, though absent from Albanian (where it was replaced with vëlla), and its existence in Anatolian is dubious."

## Important Note

The exact Avestan and Old Persian forms are not explicitly listed in this reconstruction article. The document provides Proto-Indo-Iranian (*bʰráHtā) as the intermediate proto-language, from which these later languages descended, but specific attested forms in those individual languages are not detailed on this particular page.
```


## [2026-09-05T13:49:19.239Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D8%A7%D8%AF%D8%B1",
 "prompt": "Give the Persian entry for برادر: etymology (Middle Persian form, Old Iranian, Proto-Indo-European), pronunciation, meaning. Quote the etymology section verbatim."
}
```


## [2026-09-05T13:49:21.174Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%B1%DB%8C%D8%A7%D9%86",
 "prompt": "Give the Persian entry for بریان: etymology (Middle Persian, Proto-Iranian root), meaning. Quote the etymology verbatim. Also mention any related forms like برشتن or بریژن."
}
```


### [2026-09-05T13:49:25.671Z] TOOL RESULT

```
# Persian Entry for برادر

## Etymology
The entry states that the word is "Inherited from Middle Persian [script needed] (brād, brādar), from Old Persian 𐎲𐎼𐎠𐎫𐎠 (b-r-a-t-a /⁠brātā⁠/), from Proto-Iranian *bráHtā, from Proto-Indo-Iranian *bʰráHtā, from Proto-Indo-European *bʰréh₂tēr. Cognate with English brother."

## Pronunciation
- Classical Persian: /bi.raː.ˈdar/, /ba.raː.ˈdar/
- Iranian Persian (formal): \[bæ.ɹɒː.d̪ǽɹ\]
- Tajik: \[bä.ɾɔ.d̪áɾ\]
- Audio available for Iranian Persian

## Meanings
1. **Brother** (family relation)
2. **Comrade** (military context in Iran)
3. **Dude** (colloquial term of address for men in Iran)

The entry also includes extensive dialectal variations and possessive forms across Persian-speaking regions.
```


### [2026-09-05T13:49:26.726Z] TOOL RESULT

```
# Persian Entry for بریان

**Etymology:**
The entry states: "From _[برشتن](/wiki/%D8%A8%D8%B1%D8%B4%D8%AA%D9%86#Persian "برشتن")_ (birištan, 'to roast, fry')."

This indicates the word derives from the Persian verb برشتن meaning "to roast" or "to fry," rather than from Middle Persian or Proto-Iranian roots as specified in your question.

**Meaning:**
As an adjective: grilled or roasted
As a noun: roast or kebab

**Related Forms:**
The page lists these derived terms:
- بریانی (biryānī)
- بریان کردن (biryān kardan)

The document does not mention برشتن or بریژن as related forms beyond citing برشتن as the etymological source.
```


## [2026-09-05T13:49:29.981Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D8%B4%D8%AA%D9%86",
 "prompt": "Give the Persian entry for برشتن (birištan): etymology (Middle Persian, Proto-Iranian, PIE root), meanings, related terms such as برشته. Quote the etymology verbatim."
}
```


## [2026-09-05T13:49:31.362Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%A8%D8%B1",
 "prompt": "Is there a Persian entry for انبر (anbor/ambor) 'tongs, pliers'? Give its etymology and meaning verbatim if present."
}
```


### [2026-09-05T13:49:35.781Z] TOOL RESULT

```
# Persian Entry: برشتن (birištan)

**Meaning:** to toast, roast, or fry

**Etymology:** The word derives from Middle Persian *blyštn'* (brištan, "to roast"). It ultimately traces back through a Western Iranian derivative of Proto-Indo-Iranian *\*bʰr̥ȷ́yáti* to Proto-Indo-European *\*bʰr̥ǵ-yé-ti*, stemming from the root *\*bʰerǵ* ~ *\*bʰreǵ* meaning "to roast, fry."

**Cognates:** Sanskrit भृज्जति (bhṛjjati), Latin *frigo* (source of English "fry"), and Ancient Greek φρύγω (phrúgō).

**Related Terms:** The present stem is **بریز** (beriz) or **برز** (berez), though these forms are primarily used in southern dialects like Bandar Abbasi rather than standard Persian.

**Note:** The entry is attested in biblical Persian, including Ezekiel 4:9, where it describes roasting grains.
```


### [2026-09-05T13:49:36.585Z] TOOL RESULT

```
# Persian Entry for انبر

Yes, there is a Persian entry. Here are the details:

**Meaning:** The word means "[tongs](/wiki/tongs "tongs")"

**Etymology:** The entry states it derives "From [Middle Iranian](https://en.wikipedia.org/wiki/Middle_Iranian_languages "w:Middle Iranian languages"), from [Proto-Indo-European](https://en.wikipedia.org/wiki/Proto-Indo-European_language "w:Proto-Indo-European language") _[\*h₂eḱ-](/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82e%E1%B8%B1- "Reconstruction:Proto-Indo-European/h₂eḱ-")_ ("sharp")."

The entry also notes an alternative form: انبور (anbūr / anbur), and lists multiple descendants across Turkic languages.
```


## [2026-09-05T13:49:48.626Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v1 انبر ===\"; grep -n \"انبر\" BQT_v1_pages.txt | head -20\necho \"=== BQT v1 برشته/بریان near p255-270 ===\"; grep -n \"بریان\\|برشته\" BQT_v1_pages.txt | head -20",
 "description": "Grep Borhan-e Qate for anbor, beryan, bereshte"
}
```


### [2026-09-05T13:49:48.689Z] TOOL RESULT

```
=== BQT v1 انبر ===
1710:دسانبررا بنطم کشیده. از آ نپاست:
24251:و پیش رونده - و سخن‌شنونده وفرمانبرداروقبول
28779:تو بناگه از درخت انبر بگو
28926:خانةٌ زمستانبر! گوبند که در آن ننور و بخاری
31948:باشد مطلقاً اعم از انبرون خانه واندرون دهان
32353:زنیدان, ولاشاباذه محلةٌ اسیانبر»‌محلةٌ ماحوزا « کرستنن. سامان. ۳۸۳ بعد».
=== BQT v1 برشته/بریان near p255-270 ===
13564:و جگر فیمه کشیده دز ووغن بریان کرده ,اد ۰
19327:ناپوشیده . ۰. »ریات - بکسراول (ازمصدورمشتن) کیابشده , برشته‌شده ,کباب .سه اوه -ت
20607:با سیخ کنده ای باشد که بدان بریان در تنور
25704:وخی 054 , شغنی ۳۸50 . سربکلی ۳96 (گندم برشته, آرد ساییده) «اسشق ۳۲۰». طبری
28051:تا بوغ۷)- بم‌نالث وسکون واو وغین تا به بریان گوشت پشته را کویند
28078:که مانند ماهی درمیان تایه 3 روغن برشته کرده
30011:برشته شده را کویند که بررویآ شهای آرد رز ند.
```


## [2026-09-05T13:49:51.186Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npdftoppm -f 89 -l 89 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg89 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 89 to PNG"
}
```


### [2026-09-05T13:49:53.256Z] TOOL RESULT

```
total 29624
drwx------ 2 sfmqrb sfmqrb     4096 Sep  5 09:48 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  5 01:20 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     4061 Sep  5 02:00 avestan.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5971 Sep  5 02:13 baga.html
-rw-rw-r-- 1 sfmqrb sfmqrb   189420 Sep  5 02:15 bqt440_bottom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   513902 Sep  5 02:15 bqt440.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   502834 Sep  5 02:02 bqt538_big.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    72705 Sep  5 02:02 bqt538_fn6.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24595 Sep  5 02:02 bqt538_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22593 Sep  5 02:02 bqt538_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   207980 Sep  5 02:01 bqt538.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   282104 Sep  5 01:29 bqt733_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   669351 Sep  5 01:29 bqt733.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    17369 Sep  5 01:35 bqtv1_361_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   470042 Sep  5 01:35 bqtv1_361.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   241161 Sep  5 01:36 bqtv1_398_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   482084 Sep  5 01:36 bqtv1_398.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   190109 Sep  5 01:35 bqtv1_399_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53579 Sep  5 01:36 bqtv1_399_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1625 Sep  5 01:35 bqtv1_399_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   510341 Sep  5 01:35 bqtv1_399.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    63555 Sep  5 01:43 build71.py
-rw-rw-r-- 1 sfmqrb sfmqrb     5214 Sep  5 02:23 build82a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    53401 Sep  5 02:29 build82b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    19831 Sep  5 02:31 build82c.py
-rw-rw-r-- 1 sfmqrb sfmqrb     4811 Sep  5 02:00 bulca.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22149 Sep  5 01:51 c_belloth.png
-rw-rw-r-- 1 sfmqrb sfmqrb    23219 Sep  5 01:51 c_schyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58057 Sep  5 02:29 e0full.json
-rw-rw-r-- 1 sfmqrb sfmqrb     4446 Sep  5 02:23 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb   445959 Sep  5 01:37 hrn126_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1213019 Sep  5 01:37 hrn126.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   456157 Sep  5 01:37 hrn127_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1278807 Sep  5 01:37 hrn127.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    40966 Sep  5 01:40 mk67.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58318 Sep  5 01:45 mk70.py
-rw-rw-r-- 1 sfmqrb sfmqrb    78619 Sep  5 02:02 mk73.py
-rw-rw-r-- 1 sfmqrb sfmqrb    68454 Sep  5 02:01 mk75.py
-rw-rw-r-- 1 sfmqrb sfmqrb    79383 Sep  5 02:19 mk78.py
-rw-rw-r-- 1 sfmqrb sfmqrb    52793 Sep  5 02:18 mk79.py
-rw-rw-r-- 1 sfmqrb sfmqrb    57729 Sep  5 02:31 mk81.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58379 Sep  5 02:39 mk83.py
-rw-rw-r-- 1 sfmqrb sfmqrb    76819 Sep  5 02:39 mk84.py
-rw-rw-r-- 1 sfmqrb sfmqrb    25181 Sep  5 02:44 mk86.py
-rw-rw-r-- 1 sfmqrb sfmqrb 18949704 Sep  5 02:30 mw1872.htm
-rw-rw-r-- 1 sfmqrb sfmqrb    55169 Sep  5 01:30 pg67.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57649 Sep  5 01:33 pg69.png
-rw-rw-r-- 1 sfmqrb sfmqrb    50966 Sep  5 01:33 pg69_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    77968 Sep  5 01:31 pg70.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75801 Sep  5 01:29 pg71_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71145 Sep  5 01:29 pg71.png
-rw-rw-r-- 1 sfmqrb sfmqrb   134140 Sep  5 01:44 pg72_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2377 Sep  5 01:44 pg72_afandi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11769 Sep  5 01:47 pg72_fr2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2947 Sep  5 01:44 pg72_fr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49860 Sep  5 01:44 pg72.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81180 Sep  5 01:47 pg73.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56073 Sep  5 01:48 pg74.png
-rw-rw-r-- 1 sfmqrb sfmqrb   108877 Sep  5 01:51 pg75_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    20612 Sep  5 01:51 pg75_greeklatin.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75134 Sep  5 01:51 pg75.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66505 Sep  5 01:51 pg76.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65211 Sep  5 02:00 pg77.png
-rw-rw-r-- 1 sfmqrb sfmqrb   155334 Sep  5 02:00 pg78_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63822 Sep  5 01:59 pg78.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59439 Sep  5 02:09 pg79.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58953 Sep  5 02:08 pg80.png
-rw-rw-r-- 1 sfmqrb sfmqrb    99904 Sep  5 02:15 pg81.png
-rw-rw-r-- 1 sfmqrb sfmqrb    29321 Sep  5 02:20 pg82_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    74477 Sep  5 02:20 pg82.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56108 Sep  5 02:20 pg82_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   154129 Sep  5 02:25 pg83_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7123 Sep  5 02:26 pg83_apac.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4363 Sep  5 02:26 pg83_bohyah.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67094 Sep  5 02:25 pg83.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82358 Sep  5 02:23 pg84.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63329 Sep  5 02:25 pg85.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31530 Sep  5 02:35 pg86.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79874 Sep  5 09:47 pg87.png
-rw-rw-r-- 1 sfmqrb sfmqrb   171528 Sep  5 02:45 pg89_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4628 Sep  5 02:45 pg89_ambor.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4924 Sep  5 02:45 pg89_berijan.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80984 Sep  5 09:49 pg89.png
-rw-rw-r-- 1 sfmqrb sfmqrb    77182 Sep  5 09:48 pg90.png
```


## [2026-09-05T13:49:56.920Z] TOOL CALL #37: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg89.png"
}
```


### [2026-09-05T13:49:57.265Z] TOOL RESULT

```

```


## [2026-09-05T13:49:57.263Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T13:50:12.692Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\npython3 -c \"\nfrom PIL import Image\nim=Image.open('pg89_600.png'); print(im.size)\n\"\n",
 "description": "Check existing 600dpi render size"
}
```


### [2026-09-05T13:50:14.385Z] TOOL RESULT

```
(5100, 6600)
```


## [2026-09-05T13:50:19.890Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\npython3 -c \"\nfrom PIL import Image\nim=Image.open('pg89_600.png')\n# persian roasted box region\nim.crop((2560,4380,3960,4860)).resize((2800,960)).save('crop_persian_roast.png')\nim.crop((2500,3480,3960,3760)).resize((2920,560)).save('crop_ambor.png')\n\"\nls -la crop_*.png",
 "description": "Crop Persian roast and ambor regions"
}
```


### [2026-09-05T13:50:22.417Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 30227 Sep  5 09:50 crop_ambor.png
-rw-rw-r-- 1 sfmqrb sfmqrb 65413 Sep  5 09:50 crop_persian_roast.png
```


## [2026-09-05T13:50:24.787Z] TOOL CALL #40: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_persian_roast.png"
}
```


### [2026-09-05T13:50:25.003Z] TOOL RESULT

```

```


## [2026-09-05T13:50:25.001Z] INPUT

[Image: original 2800x960, displayed at 2000x686. Multiply coordinates by 1.40 to map to original image.]


## [2026-09-05T13:50:40.626Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\npython3 -c \"\nfrom PIL import Image\nim=Image.open('pg89_600.png')\nim.crop((2600,4700,3000,4790)).resize((2000,450)).save('crop_berijab_lat.png')\nim.crop((3600,4690,3900,4800)).resize((1800,660)).save('crop_berijan_ar.png')\n\"",
 "description": "Crop berijab transliteration and script closely"
}
```


### [2026-09-05T13:50:44.113Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T13:50:46.340Z] TOOL CALL #42: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_berijab_lat.png"
}
```


### [2026-09-05T13:50:46.356Z] TOOL RESULT

```

```


## [2026-09-05T13:50:50.671Z] TOOL CALL #43: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_berijan_ar.png"
}
```


### [2026-09-05T13:50:50.688Z] TOOL RESULT

```

```


## [2026-09-05T13:51:06.224Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN p.47 area (leaf 68) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==69' HRN.txt | head -40",
 "description": "Print Horn page 47"
}
```


## [2026-09-05T13:51:07.799Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SNS brištag / brēj ===\"; grep -n -i \"brišt\\|bri.t\\|brēj\\|brej\" SNS_pages.txt | head -20\necho \"=== SYN brother 2.44 ===\"; grep -n \"BROTHER\" SYN.txt | head -10",
 "description": "Grep SNS and Buck"
}
```


### [2026-09-05T13:51:07.853Z] TOOL RESULT

```
=== HRN p.47 area (leaf 68) ===
— 47 —
201. biriäten 'braten', vergl. bertjeriy btrezen 'Backofen',
biryän, beryän (AM.).
ai. [/^bhrajj^ bh^jjdti 'rösten ; plilv. bristan Vösten*,
brejam (PPGl.), bristak (vd. 5, (134) GL), brejan (AV.)i).
kurd. birzdndin (H.-Sch.), braztin, LW. beristin *braten,
rösten'; af;\ writ geröstet', wrat-Sddl 'rösten'; bei.
brijag , brejag 'backen , rösten (39) ; wsi/, waresam,
sar. wirzam.
202. &^r/ 'Schnee.
g. mäz. gel. Ka§. varf^ verf.
aw. vafra- 'Schnee'; phlv. vafr.
kurd. vafr (H.-Sch.), befir, bafer, berf (LW.); af>.
vävra 'Schneeflocke*, Plur. 'Schnee'; bei. LW. harpi
sangl. varf, min], värfa,
203. hery 'Blatt'.
g. niaz. varak; gel. velg, valk; Käö. valg^ velg\ (vergl.
buchär. :^3, Ps. 1, 3).
aw. varekah^ (ZP61.); phlv. varg 'Blatt',
kurd. LW. (?) valg (H.-Sch.), belk, balg (Guranl, Rieu
Catalogue II, 729 a).
204. bevf/er 'Glück'.
SiW.*uparö.kara- {wergl.uparö.kairga-), deLagarde,
Beitr. z. altbaktr. Lex. 71, von Geldner, 3 Yasht 12,
gebilligt.
205. bergustuwän 'Panzer, Pferdepanzer'.
Etwa *uparö,kustapäna'; phlv. vergl. kustak \Seite'.
Vergl. np. kust (No. 854).
Im Gersäspnäme (Macan, 2103, Vers 9 v. u.) steht
die kürzere Form kustuwän (Text gustuwän), worauf
mich Herr Prof. Nöldeke aufmerksam macht.
206. bern 'Egge'.
Nur aufgenommen, weil G. Meyer (albanes. Wörter-
buch, S. 44) np. bern 'Egge als Etymon der entlehnten
*) Phlv. vrejan ist nur fehlerhafte Schreibung; np. biristen ist
durchaus nicht ungebräuchlich, wie Fr. Müller (WZKM. 5, 185) nach
V
Vullcrs meint. Ich citire nur Sahn. I, S. 20, Vers 8.
```


### [2026-09-05T13:51:07.904Z] TOOL RESULT

```
=== SNS brištag / brēj ===
4745:                                               oW*'*^*: bristaqiJi** )!
4757:0<Uf<"^^ 9°5t * bristag: j*>o^.-"l*»OH
16192:                          g5h3nlg 298/11                         getlCgD 177/14           gost I bristag 103/2
16391:barsum dan 103/7         besaz 112/4                     bristag 103/16
=== SYN brother 2.44 ===
2908:MANKIND: SEX, AGE, FAMILY RELATIONSHIP 107 2.44 2.45 BROTHER SISTER Grk. 4ded¢ds abehon NG abeAdeds, pop. Abephés 4deAH7, POP- d5epon s Lat. frdter soror It. fratello sorella Fr. frére se@ur Sp. hermano hermana Rum. frate sora Ir. brathir siur Nir.  dearbrathatr deirbhshiur W. brawd chwaer Br. breur c’hoar Goth. brépar swistar ON brddir systir Dan. _broder sdster Sw. broder syster (0) 0) brddor sweostor ME brother sister, suster NE brother sister Du. broeder zuster OHG  bruodar swestar MHG_bruoder swester NHG _ bruder schwester Lith.  brdlis sesuo Lett. bralis masa ChSl.  bratrii, brati sestra SCr. brat sesira Boh.  brair sestra Pol. brat siostra Russ. brat sestra Skt. bhratar- svasar- Av. bratar- x’ anhar-
3455:2.65 BROTHER-IN-LAW : ; Jife’s Husband’s Brother; b, W Veter: c, Sister’s Husband; d, Husband’s Sister’s Husband; éf Husbands of Sisters) Grk. Sane (a); vauBpds (b, c), aédior (e), avdpds
```


## [2026-09-05T13:51:24.089Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '4740,4765p' SNS_pages.txt\necho \"=== brejan in SNS ===\"; grep -n \"brej\\|brēj\\|brzn\\|brizn\" SNS_pages.txt | head",
 "description": "Read SNS brištag entry"
}
```


### [2026-09-05T13:51:24.153Z] TOOL RESULT

```
 The Religious Ceremonies and Cuetome of the
                               \/\V*S         Pareeee. by Uodi. p. 240.                                                                                  -^                     Vc^                :!,


                                                                                                                                                   , «j££ J   > ^i-J
                                               oW*'*^*: bristaqiJi** )!
                                                        •
                                                                                                             1




                     •   0*/oV* *o J/c^~ :bhr55Sti,/bhra35! i^J-*-                                                 ** Mi». 9.72) bhrajate                               :   ^^^ br3z . siw
     j    .>^ j>w .'^i- .^-1 bciz:                0*3 o*'       i^ «> CCA'PB. 47)                                                      IVTT-5         Oiir.Han.             II, 48.)
                                                                                                                                                                         br's^gg:
                                                                                                                                     •T/rr   ^ .j3      U*ja: brazyagtar^v5<oe^

0<Uf<"^^ 9°5t * bristag: j*>o^.-"l*»OH
                                :


                                                                               .TA/T «*         •   **                                                         •   j^j* < *-*#:
                                                                                                                                                                barOniand *t€#W                            :


                                                                                                                              J/rt ^ .j-j^ .j3Ai-x« :brfimand-tar:
=== brejan in SNS ===
```


## [2026-09-05T13:51:26.154Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD brištag ===\"; grep -n -i \"brišt\\|brēz\\|brēj\\|bristag\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== NYB ===\"; grep -n -i \"brišt\\|bristak\" NYB_vol2_glossary.txt | head -10",
 "description": "Grep MacKenzie and Nyberg for bristag"
}
```


### [2026-09-05T13:51:26.220Z] TOOL RESULT

```
=== PHD brištag ===
PHD.txt:285:brëz-, v. brištan.
PHD.txt:292:*brinj [binc | (M bryng), N birinj] bronze, brass. ~én [-yx!] bronze, brazen. brinómand [blyn’wmnd] delimited. brištan, bréz- [blystn', blyc- | M bryz-, N biristan] roast. brüg [blwk' | M brwg, N abrü] (eye)brow. büdan, b(aw)- [YHWWN-tn! < A yhwwn, У hwh; bwtn', b- | M bwdn, bw-, N büdan] be, become. bawišn: becoming, genesis. büf [bwp | N <), *büg [bwk'] owl. buland [bwind | = M, N ~] high. būm [bwm | N ~] land, earth, country. ~-€andag [-cndk'] earthquake. Ibun [bwn' | = M, N ~] base, foundation, bottom. *bun [bwn! | N ~] = wan. bunag [bznk! | N ~a] baggage; abode, camp. — daštan: dwell, settle. bun-dahišn(īh) [bzundhšn!, -yh] primal creation. bunih [bwnyh] beginning. buništ [bwnyst! | = M] foundation. ~ag [-k'] principle. bun-kadaģ [bwnktk'] original house, home. bun-xān [bwnh?n'] source. bur-, —išn, v. buridan. burāģ [bzoP RU] cutting, sharp. burām-, v. bram-. burd [bwit! | M bwrd] patient. ~ih: patience. burdan, bar- [Y BLWN-tn! < А У ybl; bwltn', bl- | M Бата, br-, N <] carry, bear, take, endure. ~išn: bearing, behaviour. burdār [bwit!]] bearer; womb. ~ih: patience. burd-ešnēhr [bwit! fnwhl | P bwrdyfnwhr] grateful, thankful. burg [bwig | (Ar. burj)] tower. buridan, bur- [bwl-ytn! | M bwr-, N ~] = bridan. —j$n: cutting. Burz [bwic] the god of agriculture. Burzénmihr [bwlcynmtr!] the third major Fire of Sasanian Eran, that of husbandmen. burzidan, burz- [bwlc-ytn'] praise, honour. ~i$n: praise, honour. —iŠnié : praiseworthy. buš [ро | N ~] mane. būšāsp [bwPsp | M bwsy'sp, N ~] sleep, sloth; dream. * but [bwt! | = M, N ~] Buddha; idol. buz [AZ < A ‘z; Бос | N ~] goat.
PHD.txt:2374:illumination abrēzišn(īh).
PHD.txt:3463:roast brištan.
=== NYB ===
```


## [2026-09-05T13:51:43.781Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB ===\"; grep -n \"bryc\\|brišt\\|bristak\\|brēz\" NYB_vol2_glossary.txt | head -10\necho \"=== KLN structure: find 'brother' ===\"; grep -n \"brother, n\" KLN_1966.txt KLN_1971.txt | head -5\ngrep -c \"\" KLN_1966.txt",
 "description": "Grep Nyberg and locate Klein brother"
}
```


### [2026-09-05T13:51:43.857Z] TOOL RESULT

```
=== NYB ===
=== KLN structure: find 'brother' ===
KLN_1971.txt:34401:brother, n. — ME., fr. OE. brodor , rel. to OS. 
KLN_1971.txt:96476:foster brother, n. — OE. fostorbrodor . See foster, 
41263
```


## [2026-09-05T13:51:46.893Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '34395,34420p' KLN_1971.txt\necho \"=== bear v ===\"; grep -n \"^bear, v\\|bear (I)\\|bear, tr. and intr\" KLN_1971.txt | head -5",
 "description": "Read Klein brother entry"
}
```


### [2026-09-05T13:51:46.980Z] TOOL RESULT

```
and cp. bread, brood. 

brothel, n. — ME. brothel , ‘worthless person, 
prostitute’, derived, fr. OE. broden, pp. of 
breodan , ‘to destroy’ ; confused in meaning with 
OF. horde l, ‘hovel’ (for which see bordel). 
brother, n. — ME., fr. OE. brodor , rel. to OS. 
brothar, ON. brodir, Dan., Swed. broder, OFris. 
brother , MDu., Du. broeder , OHG., MHG. bru- 
oder , G. Bruder , Goth. bropar, and cogn. with 
OI. bhrdtar -, Avestic bratar-, Toch. A pracar y 
B procer. Arm. eibayr (in Armenian, br became 
lb), Gk. <pp«T7jp, 9pSTCi>p, ‘member of a clan’, 
L. frdter, ‘brother’, Oscan fra t rum , fra from, ‘of 
the brothers’ (pi? gen.), OSlav. bratru, bratu , 
‘brother’, Russ., Pol., Slovak brat y Czech bratr, 
OPruss. brati, brote (voc.), ‘brother’, bratrikai , 
‘brothers’, Lith. broterelis, ‘little brother’, 
whence — through back formation — brolis, Lett. 
bralis (voc.), ‘brother’, OIr. brdthir y OW. 
broder , W. brawd, Bret, breur, ‘brother’. Cp. 
bratstvo, fraternal, friar, phratry. Cp. also pal. 
Derivatives: brother, tr. v., brother ly , adj. and 
adv., brother-U-ness , n. 

Brother Jonathan, a sobriquet for the United 
=== bear v ===
27270:bear, tr. and intr. v., to carry. — ME. beren , fr. 
95656:forbear, tr. and intr. v., to refrain from. — ME.
```


## [2026-09-05T13:51:54.618Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"brother, n\\|bring, tr\\|brotherhood\" KLN_1966.txt | head -5\necho \"--- sample of file ---\"; sed -n '1,15p' KLN_1966.txt\necho \"--- search 'bropar' ---\"; grep -n \"bropar\\|bro.ar, and cogn\" KLN_1966.txt | head -5",
 "description": "Inspect Klein 1966 file"
}
```


### [2026-09-05T13:51:54.694Z] TOOL RESULT

```
5558:Derivatives:  brat-ling,  n.,  bratt-ish,  adj. bratstvo,  n.,  brotherhood.  —  Russ.,  etc.,  formed with  suff.  -stvo  (corresponding  in  meaning  to  E. -hood),  fr.  Russ.,  Pol.,  Slovak,  brat,  etc., ‘brother’,  which  is  cogn.  with  Goth,  bropar, OE.  brodor,  ‘brother’.  See  brother, brattice,  n.,  a  partition.  —  ME.  bretasce,  ‘bar¬ tizan’,  fr.  OF.  bretesche  (F.  breteche,  bretesse ), ‘brattice’,  fr.  ML.  ( turn's )  brittisca,  ‘British tower',  fr.  OE.  Brittisc,  ‘British’.  See  British  and cp.  bartizan.
15344:fraternity,  n.  —  ME.  fraternite,  fr.  OF.  frater- nitee,  fraternite  (F.  fraternite),  fr.  L.  frater- nitatem,  acc.  of  fraternitas,  ‘brotherhood’,  fr. fraternus,  ‘brotherly’.  See  prec.  word  and  -ity and  cp.  confraternity.
28648:phratry,  n.,  1)  subdivision  of  a  tribe  in  ancient Greece;  2)  a  clan  among  primitive  races.  —  Gk. 9paTpla,  ‘brotherhood;  tribe,  clan’,  fr.  9pa- TYjp,  ‘brother’,  which  is  cogn.  with  L.  frater, Goth,  bropar,  OE.  brodor,  ‘brother’.  See  brother and  -y  (representing  Gk.  -Lot).
39030:thiazine,  thiazin,  n.,  any  of  a  class  of  ring  com¬ pounds  containing  one  sulfur  atom  and  one nitrogen  atom  and  four  atoms  of  carbon  (bio¬ chem.)  —  Compounded  of  thio-,  -az  and  -in(e). thiasus,  n.,  a  religious  brotherhood  ( Greek  antiq.) —  L.,  fr.  Gk.  (Kaooc,  ‘religious  guild,  confra¬ ternity’,  which  is  of  uncertain  origin, thiazole,  thiazol,  n.,  a  colorless  liquid  C3H3NS (chem.)  —  Compounded  of  thio-  and  azole, thick,  adj.  —  ME.  thicke ,  thikke,  fr.  OE.  piece, rel.  to  OS.  thikki,  ON.  pykkr,  pjukkr,  piokkr, Dan.  tyk,  Swed.  tjock,  Norw.  tjukk,  OFris. thikke,  MDu.  dicke,  Du.  dik,  OHG.  dicki,  dichi, ‘thick’,  dicco,  ‘often’,  MHG.  dicke,  G.  dick, ‘thick’,  fr.  I.-E.  base  *tegu-,  whence  also  OIr. tiug,  ‘thick’,  W.,  Co.  tew,  Bret,  teo,  of  s.m. Derivatives:  thick,  n.,  adv.  and  v.,  thick-en,  tr. and  intr.  v.,  thick-en-er,  n.,  thick-en-ing,  n., thick-et,  n.,  thick-et-ed,  adj.,  thick-et-y,  adj., thick-ness,  n.,  thick-ish,  thick-ly,  adjs.,  thick¬ ness,  n.  and  tr.  v.,  thick-ness-ing,  n. thief,  n.  —  ME.  theef,  fr.  OE.  peof  rel.  to  OS. thiof \  ON.  pjofr,  Dan.  tyv,  Swed.  tjuf  Norw. tjuv,  OFris.  thiaf  MDu.,  Du.  dief  OHG.  thiob, diob,  diub,  MHG.  diep,  diup,  G.  Dieb,  Goth. pi ufs,  and  possibly  cogn.  with  Lith.  tiipiu,  tupti, ‘to  squat  oneself  down’,  tupiu,  tupeti,  ‘to  crouch, squat’.  Cp.  theft  and  the  last  element  in  infang- thief,  outfangthief.
--- sample of file ---
A  COMPREHENSIVE ETYMOLOGICAL  DICTIONARY
OF  THE
ENGLISH  LANGUAGE
Dealing  with  the  origin  of  words and  their  sense  development  thus  illustrating the  history  of  civilization  and  culture
BY
Dr.  ERNEST  KLEIN
A  word  fitly  spoken  is  like  apples  of  gold  in  pictures  of  silver proverbs  25:11
VOLUME  I  A-K
ELSEVIER  PUBLISHING  COMPANY AMSTERDAM  LONDON  NEWYORK
1966
ELSEVIER  PUBLISHING  COMPANY 335  JAN  VAN  GALEN STRAAT,  P.O.  BOX  211,  AMSTERDAM
AMERICAN  ELSEVIER  PUBLISHING  COMPANY,  INC. 52  VANDERBILT  AVENUE,  NEW  YORK,  N.Y.  IOOI7
ELSEVIER  PUBLISHING  COMPANY  LIMITED RIPPLESIDE  COMMERCIAL  ESTATE BARKING.  ESSEX
First  Published  1965  -  First  Reprinted  1969
LIBRARY  OF  CONGRESS  CATALOG  CARD  NUMBER  65 -I  3229 COPYRIGHT  ©  1966  ELSEVIER  PUBLISHING  COMPANY,  AMSTERDAM ALL  RIGHTS  RESERVED
--- search 'bropar' ---
5558:Derivatives:  brat-ling,  n.,  bratt-ish,  adj. bratstvo,  n.,  brotherhood.  —  Russ.,  etc.,  formed with  suff.  -stvo  (corresponding  in  meaning  to  E. -hood),  fr.  Russ.,  Pol.,  Slovak,  brat,  etc., ‘brother’,  which  is  cogn.  with  Goth,  bropar, OE.  brodor,  ‘brother’.  See  brother, brattice,  n.,  a  partition.  —  ME.  bretasce,  ‘bar¬ tizan’,  fr.  OF.  bretesche  (F.  breteche,  bretesse ), ‘brattice’,  fr.  ML.  ( turn's )  brittisca,  ‘British tower',  fr.  OE.  Brittisc,  ‘British’.  See  British  and cp.  bartizan.
5725:brothel,  n.  —  ME.  brothel,  ‘worthless  person, prostitute’,  derived  fr.  OE.  broden,  pp.  of breodan,  ‘to  destroy’ ;  confused  in  meaning  with OF.  bordel,  ‘hovel’  (for  which  see  bordel). brother,  n.  —  ME.,  fr.  OE.  brodor,  rel.  to  OS. brothar,  ON.  brddir,  Dan.,  Swed.  broder,  OFris. brother,  MDu.,  Du.  broeder,  OHG.,  MHG.  bru- oder,  G.  Bruder,  Goth,  bropar,  and  cogn.  with
28648:phratry,  n.,  1)  subdivision  of  a  tribe  in  ancient Greece;  2)  a  clan  among  primitive  races.  —  Gk. 9paTpla,  ‘brotherhood;  tribe,  clan’,  fr.  9pa- TYjp,  ‘brother’,  which  is  cogn.  with  L.  frater, Goth,  bropar,  OE.  brodor,  ‘brother’.  See  brother and  -y  (representing  Gk.  -Lot).
```


## [2026-09-05T13:52:00.270Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=5725{c+=gsub(/\\f/,\"\")} END{print \"leaf(0-based)=\"c}' KLN_1966.txt\nawk 'NR>=5600 && NR<=5760 && /^[0-9]{3}$/{print NR\": \"$0}' KLN_1966.txt\necho \"--- bring / bear pages ---\"; grep -n \"^bring,\\|bring,  tr\\|bear,  tr\" KLN_1966.txt | head -5",
 "description": "Locate Klein 1966 page markers near brother"
}
```


### [2026-09-05T13:52:02.048Z] TOOL RESULT

```
leaf(0-based)=118
5616: 199
5641: 200
5642: 201
5692: 202
5703: 203
5727: 204
5739: 205
--- bring / bear pages ---
4607:Derivatives:  bear,  tr.  v.,  bear-ish,  adj.,  bear-ish- ness,  n.
4608:bear,  tr.  and  intr.  v„  to  carry.  —  ME.  beren,  fr. OE.  beran,  rel.  to  ON.  bera,  OFris.  bera,  Du. baren,  OHG.  beran,  ‘to  bear,  carry’,  Goth. bairan,  ‘to  bear,  carry,  give  birth  to’,  OHG.  gi- beran,  MHG.  gebern,  G.  gebaren,  Goth,  ga- bairan,  ‘to  give  birth  to’,  fr.  I.-E.  base  *bher-, whence  also  OI.  bhdrati,  ‘bears’,  bharman,  ‘sus¬ tenance,  care,  burden’,  Arm.  berem,  ‘I  bear, carry,  bring’,  bern,  ‘burden’,  Gk.  ipspeiv,  ‘to bear,  carry’,  <ptop,  ‘thief’,  L.  ferre,  ‘to  bear,  car¬ ry’,  fur,  ‘thief’.  Alb.  mbar,  bar,  ‘I  carry,  drag’, bir,  ‘son’,  OSlav.  berg,  birati  (for  earlier  bird), ‘to  bring  together,  collect,  take’,  bremg,  ‘bur¬ den’,  su-borii,  ‘assembly’,  OIr.  biru,  ‘I  carry’, W.  cymeraf  ‘I  take’,  Toch.  AB  par,  ‘to bear,  bring,  fetch’,  and  prob.  also  Toch.  B prari,  ‘finger’.  Cp.  bairn,  baron,  barrow,  ‘moun¬ tain’,  barrow,  ‘handcart’,  berth,  bier,  birth,  bore, ‘tidal  wave’,  borough,  burden,  ‘load’,  burly.  Cp. also  adiaphoresis,  adiaphorous,  afferent,  am¬ phora,  anthropophora,  Berenice,  bhat,  breba, brehon,  cataphora,  circumference,  confer,  cumber, defer,  deference,  differ,  difference,  differentiate, efferent,  -fer,  feretory,  -ferous,  ferret,  the  animal, fertile,  fortuitous,  fortune,  furtive,  furuncle,  in¬ fer,  metaphor,  offer,  opprobrium,  paraphernalia, periphery,  phoradendron,  phoresis,  Phormium, -phorous,  phosphorous,  phosphorus,  prefer,  prof¬ fer,  refer,  scirophorion,  semaphore,  Sobranje, suffer,  transfer,  varnish,  vernix  caseosa,  Vero¬ nica,  vociferate.
5661:Derivatives:  brine,  tr.  v.,  brin-er ,  n. bring,  tr.  v.  —  ME.  bringen,  fr.  OE.  bringan,  rel. to  OS.  brengjan,  OFris.  brenga,  MDu.  brenghen, Du.  brengen,  OHG.  bringan,  MHG.,  G.  bringen, Goth,  briggan,  fr.  Teut.  base  *bhrenk-.  Outside Teut.  cp.  W.  he-brnwg,  ‘to  send’,  MCo.  hem- bronk.  ‘we  lead’.
15129:forayer,  n.  —  ME.  forreier,  ‘forager’,  fr.  OF.  far¬ rier,  fr ,forrer,forer,  ‘to  forage’,  fr.  forre,  fuerre, ‘fodder’.  See  forage,  v.,  and  agential  suff.  -er. forbade,  forbad,  past  tense  of  forbid, forbear,  n.  —  See  forebear, forbear,  tr.  and  intr.  v.,  to  refrain  from.  —  ME. forberen,  fr.  OE.  forberan,  ‘to  endure,  suffer;
```


## [2026-09-05T13:52:14.029Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"pdf page\" BQT_v1_pages.txt | head -3\npython3 - <<'EOF'\nimport re\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(\"num pages\",len(pages))\nprint(repr(pages[0][:200]))\nEOF",
 "description": "Inspect BQT vol1 page file structure"
}
```


### [2026-09-05T13:52:16.673Z] TOOL RESULT

```
num pages 777
''
```


## [2026-09-05T13:52:19.306Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/ref_page.py BQT:270 2>&1 | head -60",
 "description": "Fetch BQT page 270"
}
```


### [2026-09-05T13:52:21.015Z] TOOL RESULT

```
no scan of BQT covers printed page 270 (see 'scans' in refs_online.json)
```


## [2026-09-05T13:52:30.358Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 19327 30011 28779; do awk -v L=$L 'NR<=L{c+=gsub(/\\f/,\"\")} END{print L\" -> leaf \"c}' BQT_v1_pages.txt; done\necho \"--- persian page numbers sample ---\"\npython3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (300,301,302,303):\n    print(\"=== leaf\",i,\"===\")\n    print(pages[i][:300].replace('\\n',' | '))\nEOF",
 "description": "Calibrate BQT vol1 leaf to printed page"
}
```


### [2026-09-05T13:52:32.126Z] TOOL RESULT

```
19327 -> leaf 491
30011 -> leaf 723
28779 -> leaf 694
--- persian page numbers sample ---
=== leaf 300 ===
ست و 4 سب | #احر یض « بکر اول و دای بی نقطه | و سکون ثانی وتحتانی و صاد تقطه دار ء دآروبی | است که کلف را زابل کند » و انرا صفاهانی | «گل‌کافشه» (۱) کوبند وحربی «عصفر» خوانند . | احب ۵ » بکسر اول و سکون تانی | و فتح لام سگرن بای‌اپجد و کر دال بی‌قطه | و تحتانی بالف کشیده » بسربانی کیاهی است | شیر دار که در صراها و 
=== leaf 301 ===
« ری الافی » خوانند ؛ و بجای بای بجد بای | اخت - حم اول وسکون ثالی وفوقانی» | بممنی مثل‌ومانند و قرین ولظیی باشدب وددعریی | خواهر را گویند » و بی بممنی اول نیزعریی | میدانتد ۴ . | اختر ۴ ه بر وزن افر » رابت وعلمرا | گویشد - و بمعنی بخت و طالع هم هست - | و ک وکب و ستاره را یز کوبند - و بعمتی‌فال | و شگون هم آمده است
=== leaf 302 ===
وخواهر زاده را گونند . | اخروش « با رای فرخت بر وزن خر | اخ‌تفی - جنم ثالث وفا :۰ اج و لف را | گوبند که آب دهن را جمم کردن و انداختن | باشد . کوش » خروش و غوغا و شور را کویند . | اخته - بر وزن تخته » بمعنی خابه اخریان - بر وزن پرنبان » غماش | بیرون کشید» باشد . ومتاع و اسباب و کالای بر گزیده را گویند . | ی آستان 
=== leaf 303 ===
«کراث الک رکم » خوانند . | اخسمه - بفتح اول وسکون انی و شم | سین بی نقطه و فتح عیم » بوژه را گویند و آن | شرابی‌باشد که از آرد ارزن وجو و امتال آن‌سازند. | آحسی » بروزن مخفی . نام فصبه‌است | از ماوراء النهر در ناحيهٌ فرغانه ء از بهترین آن | بارد است ۱ | 2 ‌ | کاف» بمعنی اخی است که تام قصبه ای باشد از | ماوراء الثهر۱
```


## [2026-09-05T13:52:44.457Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (476,491):\n    print(\"=== leaf\",i,\"(printed ~\",i-221,\") ===\")\n    print(pages[i][:1500])\n    print()\nEOF",
 "description": "Print BQT leaves 476 and 491"
}
```


### [2026-09-05T13:52:46.124Z] TOOL RESULT

```
=== leaf 476 (printed ~ 255 ) ===
" بر‌سان « بنتح اول می وزن نرسان :
دوشاب میاء رنگه خوشبوی را گویند - و مطلق
امت را لیز کفته‌اند از هر پیعمبی که باشد ٩‏ -
وکروه آدمپان را هم - و بکسر اول نیز آمده
است - و بضم اول اژدها را کویند .
پر سر آ هدن - کنابه ازغلبه وافزونی
و زبادئی کردن باشد . ۳
بر ص‌غنچه - نم او و غن‌قلمدار,
تضم سرو کوعی باشد و آن سیاه رنکه و فربه
میشود . سفوف آنکرم شکم را میکشد و آنرا
بحریی جوزالایهل و ثمرتالمرعر خوانند ۴ .
پر سم ۴ - بروزن‌مرهم » شاخهای‌باريكث
بی که باشد بمقدار یك‌وجب که آنرا از درخت
هوم ببرند ؛ و آن درختی است شبیه بدرخت کز
و اکر هوم نباشد درخت کر و الا درخت انار ء
و رسم بریدن آن چنان است که اول کاردی که
دس آن هم‌آهن باشد و آنرا برسم چین خوانند
(۱) چك : ژند . ۱ "
۳۹ ۱9
مس زمزم نمایند بمتی دهایکه در وقت عبلدت
آش و بدن شستن و چیزی خوردن میخوانشد
بخوانند . و برسم را با برسم چین ببرندیس‌برسم
دانرا قیز آب گفتد و آن
ظرفی باشد مانشد قل‌دان وآنرا
از طلا و نفره و امشال آن
مازند » و برسمهارا اسدرون
آن گذارند » و حرگاه خواعند
بدن بشوبند باچیزی بخورند با
زد (۱) ععنی قسمی از اقسام
کتابهای زند (۱) بخوانند چند
عدد از آن برس که بجهت آن
کار وآن فعل معین است بدست
گیرند, چنانچه بجهت خوادن
سك وندیداد که یکی از
۳ - رگ : بوس .
بقه از مضه ۲۵۵
( برهان فاطع ۳۷ )
مسعز

=== leaf 491 (printed ~ 270 ) ===
سه اوه -ت
رای تس ی
آن بکار برند و بردمید کیها یز مالند .
یر بش - بکسر اولو انی رسکون‌تاث
و شین قرشت » بمعنی آخربراش است کهپاتیدن
و فروشاندن باشد . #
‌ بخ - یر اولبررزن دریغ » خوشة
نگور با
برین" ۱ بفتح اول‌بروزن‌قرین »بمعنی
بلایین باشد یمنی بلند ترین و بالا ترین » چه
فلك‌الافلاك را باين اعنبار سپهر برین کفته‌اند -
و صبا را یز گویند چه بادبرین باد صبا است -
ر بمعتی رخنه و شکاف هم آمده است. ۳ - ونام
آتشکده‌ای‌یز هست ۴ - و بضم‌اول پارچة كوچك
و حلال‌داری باشد که از خریزه و حندوانه بریده
باشند ۴ - و.بکسر اول هر سوراخ را گویند
عموماً و سوراح تنور:را خصوصاً .
بر یی « منم اولرکسر انی بتحتانی
رسیده و نون همکسور بنین نقطهدار زده » بمعنی
بربدن و برش باشد 9 - و بمعنی راندن شکم
و بربدن آن «م هست ؛ بمعتی اينکه کویا شکم
او را از غات درد مینك .
بر دنه تب بکسر اول بروزن‌نگینه ؛یمعنی
برین است که هی سوراخ باشد عموماً - وسوراخ
شور باشف خصوصاً .
ثر لون - با ناكك مجهول و فتح راو بر
وزن دوبدن » علتی است که در بدن آدمی پیدا
مشود و هرچند برمی‌آبد پپن میگردد وخاری
میکند و آنرا درهندوستان داد میگویندوییی
قوبا خوانند ء و باینمعتی بروزن فرعون‌ودلخون
حم آمده است - و بروزن افیون کردا کرددهان
را کوبند .
« فتح اول وسکون ثافی ۰ رسمه ین
و قاعده و فانون وظرز و روش را گوبند - وامر
بریزبدن بمعنی وزیدن هم هست ٩‏ - و مخفف
بزم باشد که مجلس عيش ومهمانی است > وزمین
و یشنة بلند - و تیغ کوه را نیز گفته‌اند - و با
تشدید انی در عربی جامهٌ رسمانی ۷ - واسباب
۱ - مرکباز : بر (ل+ ین(یوندسبت).  .‏ ۴
س
داسفا ۱ : ۲ ص ۱۷۲۹ ».
تسیک
بعربی تیس خوااند با
نای‌قرشت بروزن‌قیس ۸
از عصدر بر بدن. رله:ح 4.
۴ - ازمصدر بر مدن ه پهلوی ۲18
۹ _ و
```


## [2026-09-05T13:52:56.435Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (476,491):\n    txt=pages[i]\n    print(\"=== leaf\",i,\"printed\",i-221,\"len\",len(txt),\"===\")\n    for kw in ('برشته','بریان','برشتن','بریژن','بریزن','پهلوی'):\n        if kw in txt:\n            for j,l in enumerate(txt.split('\\n')):\n                if kw in l: print(\"  [\",kw,\"]\",l.strip())\n    print('---- tail ----')\n    print(txt[-1800:])\nEOF",
 "description": "Search BQT pages 255 and 270 for roast words"
}
```


### [2026-09-05T13:52:58.720Z] TOOL RESULT

```
=== leaf 476 printed 255 len 1153 ===
---- tail ----
" بر‌سان « بنتح اول می وزن نرسان :
دوشاب میاء رنگه خوشبوی را گویند - و مطلق
امت را لیز کفته‌اند از هر پیعمبی که باشد ٩‏ -
وکروه آدمپان را هم - و بکسر اول نیز آمده
است - و بضم اول اژدها را کویند .
پر سر آ هدن - کنابه ازغلبه وافزونی
و زبادئی کردن باشد . ۳
بر ص‌غنچه - نم او و غن‌قلمدار,
تضم سرو کوعی باشد و آن سیاه رنکه و فربه
میشود . سفوف آنکرم شکم را میکشد و آنرا
بحریی جوزالایهل و ثمرتالمرعر خوانند ۴ .
پر سم ۴ - بروزن‌مرهم » شاخهای‌باريكث
بی که باشد بمقدار یك‌وجب که آنرا از درخت
هوم ببرند ؛ و آن درختی است شبیه بدرخت کز
و اکر هوم نباشد درخت کر و الا درخت انار ء
و رسم بریدن آن چنان است که اول کاردی که
دس آن هم‌آهن باشد و آنرا برسم چین خوانند
(۱) چك : ژند . ۱ "
۳۹ ۱9
مس زمزم نمایند بمتی دهایکه در وقت عبلدت
آش و بدن شستن و چیزی خوردن میخوانشد
بخوانند . و برسم را با برسم چین ببرندیس‌برسم
دانرا قیز آب گفتد و آن
ظرفی باشد مانشد قل‌دان وآنرا
از طلا و نفره و امشال آن
مازند » و برسمهارا اسدرون
آن گذارند » و حرگاه خواعند
بدن بشوبند باچیزی بخورند با
زد (۱) ععنی قسمی از اقسام
کتابهای زند (۱) بخوانند چند
عدد از آن برس که بجهت آن
کار وآن فعل معین است بدست
گیرند, چنانچه بجهت خوادن
سك وندیداد که یکی از
۳ - رگ : بوس .
بقه از مضه ۲۵۵
( برهان فاطع ۳۷ )
مسعز
=== leaf 491 printed 270 len 1516 ===
  [ پهلوی ] ۴ - ازمصدر بر مدن ه پهلوی ۲18
---- tail ----
سه اوه -ت
رای تس ی
آن بکار برند و بردمید کیها یز مالند .
یر بش - بکسر اولو انی رسکون‌تاث
و شین قرشت » بمعنی آخربراش است کهپاتیدن
و فروشاندن باشد . #
‌ بخ - یر اولبررزن دریغ » خوشة
نگور با
برین" ۱ بفتح اول‌بروزن‌قرین »بمعنی
بلایین باشد یمنی بلند ترین و بالا ترین » چه
فلك‌الافلاك را باين اعنبار سپهر برین کفته‌اند -
و صبا را یز گویند چه بادبرین باد صبا است -
ر بمعتی رخنه و شکاف هم آمده است. ۳ - ونام
آتشکده‌ای‌یز هست ۴ - و بضم‌اول پارچة كوچك
و حلال‌داری باشد که از خریزه و حندوانه بریده
باشند ۴ - و.بکسر اول هر سوراخ را گویند
عموماً و سوراح تنور:را خصوصاً .
بر یی « منم اولرکسر انی بتحتانی
رسیده و نون همکسور بنین نقطهدار زده » بمعنی
بربدن و برش باشد 9 - و بمعنی راندن شکم
و بربدن آن «م هست ؛ بمعتی اينکه کویا شکم
او را از غات درد مینك .
بر دنه تب بکسر اول بروزن‌نگینه ؛یمعنی
برین است که هی سوراخ باشد عموماً - وسوراخ
شور باشف خصوصاً .
ثر لون - با ناكك مجهول و فتح راو بر
وزن دوبدن » علتی است که در بدن آدمی پیدا
مشود و هرچند برمی‌آبد پپن میگردد وخاری
میکند و آنرا درهندوستان داد میگویندوییی
قوبا خوانند ء و باینمعتی بروزن فرعون‌ودلخون
حم آمده است - و بروزن افیون کردا کرددهان
را کوبند .
« فتح اول وسکون ثافی ۰ رسمه ین
و قاعده و فانون وظرز و روش را گوبند - وامر
بریزبدن بمعنی وزیدن هم هست ٩‏ - و مخفف
بزم باشد که مجلس عيش ومهمانی است > وزمین
و یشنة بلند - و تیغ کوه را نیز گفته‌اند - و با
تشدید انی در عربی جامهٌ رسمانی ۷ - واسباب
۱ - مرکباز : بر (ل+ ین(یوندسبت).  .‏ ۴
س
داسفا ۱ : ۲ ص ۱۷۲۹ ».
تسیک
بعربی تیس خوااند با
نای‌قرشت بروزن‌قیس ۸
از عصدر بر بدن. رله:ح 4.
۴ - ازمصدر بر مدن ه پهلوی ۲18
۹ _ ود :
شه درصفحةٌ ۷
```


## [2026-09-05T13:53:23.330Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (477,478,490):\n    print(\"=== leaf\",i,\"printed\",i-221,\"===\")\n    print(pages[i][:1400])\n    print()\nEOF",
 "description": "Print BQT leaves 477,478,490"
}
```


### [2026-09-05T13:53:25.073Z] TOOL RESULT

```
=== leaf 477 printed 256 ===
ده
نسکهای عشهور زند )۱( آست سی و پنج برسم
بدست گیرید ؛ و بجهت نك بشت ٩‏ بیست
وچهار برسم, وهنگلم بدن شتن وچیزی خوردن
و عیادت کردن پنج برسم ؛ و چون یکبار
نگ وندیداد خوانده‌شودآن برسمپا باطل گردد؛
و از جهت :سکهای دیگر و افمالی که مذکور
شد اختیار دارند ء خواهند با همان برسمها عمل
کنند و خواهند برسم نازه بدست گیرند . و از
شروط برسم بدست گرفتن بدن شستن وجامةٌ باله
پوشیدن است . و صاحب فرهنکه جپانگیری
کوید این لفت را از مجوسی که در دین خود
بغامت فاضل ود و آردشیر نام داشت و او را
مجوسان موید میدانستند و درعهدا کیر پادشاه از
کرمان بهندوستاي آمده بود تحفیق نمود » اما
درچند نخه از فرحتگههسروری‌توشته‌اند که‌برسم
ککایی است که آ تش‌پرستان درحین پرستش بردست
گیرند مگر. در يك دخه که کیاهی لوشنه شده
بود واین‌را با آنچه درفرهنگه
جهانگیری نوشته اند فی‌الجمله
تردیکی است وان اعلم .
برسم چین ه باجيم
فارسی بروزن فروردین , کاردی
بود که دستآنهم از آهن باشد
و فارسان بدان برسم از درخت
برند ؟ . #
(۱) چك : ژند .
برشیان دارو:
بر سق له - بروزن مرغوله . قرسی‌باشد
که در آن جوز و پزباز و بنگه و دیگی ادوبه
کر مکنند و خورلد .
بر سیا نا بفتح‌اول وسکون ثانیو کسر
الت و بای حطی وتون‌هردو بالف کشیده .رستنی
باشد که تخم آن‌مانندنخم کرفی‌است۴ .علت‌جرب
را نافع باشد .
بر شان باشین نفطه‌دار بروزن افشان.
+معنی اعت باشدمطلفاً از عرییغمب رکه باشد ۴ .۶
بر شا - با خای قطه‌دار بروزن کرپلاه
نم موضعی است میان ابران وتوران » و باینممنی
یبای خای قطدار چم هم آمده است ٩‏ .
۰ بر شتخحان - بر وزن کهکشان » بمعنی
برشضا است که نام حوضمی باشد م

=== leaf 478 printed 257 ===
می شیر آن" زین نهادن
سرخ‌مرد گوبند و بعربی عصا الراعی خوانندا ۰
بر شیر فرد ین نهادن - کنابه از
تهایت غالب شدن - و افزولی و زبادنی کردن
بر صحر انهادن هه کنانه از آشکار
و غلعر ساختن خاشد *
بر صیصا ‌ مشپور است. 1 او عابدی
بودة در تهامت خدایرستی . عاقبت ازشیطان فرب
خورده کمراه شظ .
بر ظاس - باطای حظی بروزن کربای,
نم شهری است از ولامت تی کستان . گوبندرویاء
آنجا پوست خوب میدارد و پوست آن رویاه را
نیز پرطلی میگونند ؛ و با.بای فارسی هم آمده
لت ۴ .
یراق نهادن » یمنی بمربة اعنی
رساتیدن ‏ و کنابه ازتركگدادن - و فراموش کردن
هم حست 4 :
بر طا نیقی » بکر نون و سکون بای
حطی و قلف بتحتانی‌رسید. ۰ بلفت بوتانی ؟ کلی
کویند تخم بان افروز است .
فرطایل- بکر تحتانی و سکون لام»
ظ‌جزیرماست‌در حتدوستان کهاز یکی ازدرختان
بت ۳۵۸ ‌-
آن جزیره بانگی عظیم و صدایی ههیپ‌می آبذ ,
و بضی کویند کوهی است در آن جزبر هکه‌شبها
از آن کوه صدای طبل و دهل و سنج میآید .
بر طیسقون - بختح اول و سکون ثانی
و اث بتحتاتی دسیده و بین بی‌نفطهٌ زده و ضم
فاف و واو و نون ساکن ؛ بلقت بونالی گل‌سرخ
را کویند و بعربی طی‌الاحمر خوانند » وبهترین
وی آن بودکه از مصر آورند » و آن قایم مقام
گل‌مخنوم است .
یرم ۴ ۰ تم اول و سکون ثامی و غين
نقطمدار ۰ شدی باشد که از چوب و خاشاكوخاله
وگل در پیش آب بندند » و بفتح اول و کسر
ثانی هم کفته‌اند . و بفتح اول و تالی‌هم‌ینآمده
است. و باین معنی بازای‌نقطه‌دار نیز درست‌است.
بر غاب * - بروزن غرقاب » بند آب‌است
یعنی جایبکه پیش آبرا بندند تا آب در آن
جمع شود .
برست ۲ - بر وزن سرمست .کیاهی
جوی‌آب رود و آنرا مج هگون

=== leaf 490 printed 269 ===
و کار بهوده و بیفایده کردن باشد . #
پر ود قلكك - کنابه ازماه است که‌قمر
باشد - و ژحل را نی زگفته‌اند 3
بر لژزن - بکر اول و تحتانی مجهول
بروزن شیمن » پرویزن باشد که بعربی غرپال
و علپال کوبند ۴ -و بممئی ترشی بالا هم آمده
لت - و ابه‌ای را نز گویند که از کل ساخته
باشند و بربالای آن‌نان پزند » و بقتح اول‌بمعنی
بر لژ ۵ » بکسر اول وئالث مجهولبروزن
سفیده . صمفی است دوایی شبیه بمسطکی وآن
سبك و خشك و بدبوی‌میباشد » و حمربان‌باززد
ریانما۰ با حای بی شطذ ولام
مشدد بالف کشیده , بربان باتره و پودنه وترخان
و نان و ییاز اون ۰
بریحی ۱ با چیم بر وزن رسیدن »
تنوری باش د که در آ نکماج و نان سنکك پزند ۰
و جربی فرن گوبند بضم فا .
بریخ زدن- بنتجبای حطی, کنایه از
خاطر محو نمودن و تلم نبردن و فرأمو شکردن
سونایدیدساختن‌ومعد وم گردانیدن- وهیچ‌انگاشتن
باشد -
بر بخ و شتن » کنابه‌از هیچ‌انگاشتن
- وکارییمدار و بی‌اثر کردن وضایم ساختن کاری
۱ - رك : برزن و پریزن . ۴ - رك : پرویزن . ۴ ٩‏ بریجن » پهلوی .
0 , ابرانی‌باستان [0۲21 * (یختن » برشتن) «اسفا ۱ : ۲ س ۷۱ *.
ری - بفتح‌اول . ظاهراً اسل آن‌از کلملانینی ۷5۲۵۸/105 کرفته شده بمعتی‌چاریای
چاپار و اب چایار وسپس بمعنی مك . سد ها باداره و دستگاه چاپار و عاقبت برمنزلی که بچندو .
حو.کز چاپار است اطلاق کردید و این منزل در بلاد ايران دو فرسنگه سه‌میلی و در ممالكشریی
اسلامی چهار فرسنکگ سهمیلی است ب «دائرءالممارف اسلام» . مولف د تفس » پرید را آزبردن فارمی
گرفه و آین‌درید و قرسی دانسته وصحیح قول اول است که مذ کور شد
۵ بریدن - بشم اول و فتح‌چهارم وتخفیف وتشدید دوم (هردو): ٍ
```


## [2026-09-05T13:53:57.552Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FFD page 37 ===\"; python3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt',encoding='utf-8',errors='replace').read()\nimport re\npages=t.split('\\f')\nprint(\"pages:\",len(pages))\nfor i,p in enumerate(pages):\n    if 'برشت' in p or 'بریان' in p or 'برز' in p:\n        print(\"--- leaf\",i,\"---\")\n        for l in p.split('\\n'):\n            if 'برشت' in l or 'بریان' in l: print(\"   \",l.strip())\nEOF",
 "description": "Search FFD for berestan"
}
```


### [2026-09-05T13:53:59.369Z] TOOL RESULT

```
=== FFD page 37 ===
pages: 115
--- leaf 40 ---
    برشتن
    برشت < فارسی میانه 07151 < ایرانی باستان ۳۳18-1*. برای 18 -> آراست. 0۲2 که
--- leaf 41 ---
    ريشةهٌ 07212 به معنی «برشته کردن» است.
    برشته کردن» است.
--- leaf 89 ---
    2 (ريشه < برشته کردن) ۳۷ 0 (ريشه - وزیدن) ۵۳
```


## [2026-09-05T13:53:59.717Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT bar-shta ===\"; grep -n \"بر شته\\|برشته\" BQT_v1_pages.txt | head\necho; echo \"=== ARY files ===\"; ls incoming/ARY/ 2>/dev/null; grep -n \"برادر\" incoming/ARY/ARY_pages.txt | head -5",
 "description": "Grep BQT for bereshte and ARY for baradar"
}
```


### [2026-09-05T13:53:59.792Z] TOOL RESULT

```
=== BQT bar-shta ===
19327:ناپوشیده . ۰. »ریات - بکسراول (ازمصدورمشتن) کیابشده , برشته‌شده ,کباب .سه اوه -ت
25704:وخی 054 , شغنی ۳۸50 . سربکلی ۳96 (گندم برشته, آرد ساییده) «اسشق ۳۲۰». طبری
28078:که مانند ماهی درمیان تایه 3 روغن برشته کرده
30011:برشته شده را کویند که بررویآ شهای آرد رز ند.

=== ARY files ===
ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf
ARY_latin_index_pages.txt
ARY_pages.txt
ARY_pages.txt.pages
545:8 چون واژه‌ی «بردن؛ در بونانی ۳۳180 و در انگلیسی 81۸14 است. واژه‌ی «برادر» در یونانی
15025:چم این واژه در زبان‌های غیر ایرانی در غیر سانسکریت: پسر برادر» پسر خواهر.
```


## [2026-09-05T13:54:07.488Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/FFD/FFD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\np=pages[40]\nprint(\"=== FFD leaf 40 ===\")\nprint(p[:1600])\nEOF",
 "description": "Print FFD leaf 40"
}
```


## [2026-09-05T13:54:08.888Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '540,556p' incoming/ARY/ARY_pages.txt\necho \"=== ARY انبر / انبور ===\"; grep -n \"انبور\\|انبردست\\|أنبر\" incoming/ARY/ARY_pages.txt | head",
 "description": "Print ARY baradar context"
}
```


### [2026-09-05T13:54:12.277Z] TOOL RESULT

```
=== FFD leaf 40 ===
[pdf page 41]
وج ان ار فعلهای فارسی دری
بخشیدن
بخشید < فارسی میانه 029870 027870 مادهٌ ماضی جعلی است. از مادهٌ مضارع
ساخته شده است.
بخش < فارسی میانه 0235 < ایرانی باستان 82۳-3*. 328 صورت اصلی 337 است» 8
پیش از 8 به #بدل شده است. ‎٩‏ برای ساختن ريشهٌ جدید به کار رفته است. 328 به معنی
«تقسیم کردن» است و واه «بخت» در فارسی دری از 025-18 آمده است. 327۳-18 صفت
مفعولی گذشته است از پسوند 14 و 085 به جای ۳۵8. به سیب شباهت لفظی که میان
«بخشودن» به معنی «عفو کردنْ» و «بخشیدن» به معنی «تقسیم کردن» هست» «بخشیدن»
در معنی «بخشودن» به کار رفته است > بخشودن.
برازیدن
برازید « فارسی میانه 053270. 073270 مادةٌ ماضی جعلی است. از مادةٌ مضارع
ساخته شده است.
براز « فارسی میانه 0732 < ایرانی باستان ۳122-8*. برای 2 - آرای. ريشهٌ 3۲37 و
فارسی میانه هر دو به معنی «درخشیدن» هستند. «برازیدن» در معنی «سزاوار
و زیبنده بودنْ» به کار رفته است.
بردن
برد < فارسی میانه 0۵07۵ < ایرانی باستان ۳7-1۵*. برای 1۵ -> آراست. 7۲ صورت
ضعیف ريشةٌ 7 است. به معنی «حمل کردن». چون 2707448 در فارسی میانه معنی
«حمل کردن به سوی متکلم» می‌دهده 0070۵ در معتی «حمل کردن از متکلم» به کار
رفته است. در فارسی دری «آوردن» و «بردن» از نظر معنی چون فارسی میانه هستند.
بر < فارسی میانه 027 < ایرانی باستان ۳۵۲-۵*. برای 2 -> آرای.
برشتن
برشت < فارسی میانه 07151 < ایرانی باستان ۳۳18-1*. برای 18 -> آراست. 0۲2 که
```


### [2026-09-05T13:54:12.324Z] TOOL RESULT

```
استدلال کرد شباهت‌های ظاهری میان واژه‌ها هميشه ملا کك همریشه بودن آنها نیست و خویشی واژه‌ها
[pdf page 21]
ک
۲ / ریشه‌های هندو اروپایی زبان فارسی
باید به طور علمی و سامانمند بررسی و اثبات گردد. مثلاً آوای یونانی 2۳3 برابر است با آوای ژرمنی
8 چون واژه‌ی «بردن؛ در بونانی ۳۳180 و در انگلیسی 81۸14 است. واژه‌ی «برادر» در یونانی
و در انگلیسی 381۸07778 است. پس از دادن چند مثال دیگر» راسموس راسک
نتیجه گرفت که طبق این اصل (یونانی 217 < ژرمنی 8). واژه‌ی یونانی ۳18005 (به معنی درخت
بلوط) با واژه‌ای انگلیسی 8182071 (به معنی درخت راش) همریشه است ولی معنی آنها دگرگونهه). ‎ .‏
‏است. چندی بعد از راسموس راسکث و دانشمند آلمانی بنام باپ (1791-1887 ,8078 ۳۸۲2)
علاوه بر همسانی‌های آوایی و واژگانی» شباهت‌های دستوری را نیز مورد بررسی قرار دادند و نشان
دادند که مثلاً واژه‌ی سانسکریت "۸018" (به معنی «آذر» يا «آتش») و واژه‌ی لاتین 10727157" نه
تنها همسانی آوایی دارند پلکه از نظر دستوری نیز دارای همسانی هستند:
اوط شوش
در سال ۱۸۱۳ ناماس بانگك (۷01-۸60 171011۸8) واژه‌ی «هند و اروپایی»
1300-5108078۸70) را نو آوری کرد. ضمناً آهنگ پیشرفت دانش زبانشناسی و پژوهش درباره
زبانهای هند و اروپایی نی ز کم کم سرعت بیشتری گرفت.
=== ARY انبر / انبور ===
```


## [2026-09-05T13:54:26.525Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN Zange ===\"; grep -n \"Zange\" HRN.txt HUB.txt | head\necho \"=== ARY latin index AMBOR/BEAR/BROTHER ===\"; grep -n -i \"ambor\\|anbor\\|AMPHORA\" incoming/ARY/ARY_latin_index_pages.txt | head\necho \"=== BQT انبر context ===\"; sed -n '1705,1715p' BQT_v1_pages.txt",
 "description": "Search Horn/Hubschmann for tongs and ARY index"
}
```


### [2026-09-05T13:54:26.591Z] TOOL RESULT

```
=== HRN Zange ===
HUB.txt:3184:zunehmen, dass g von gd» 'Zange\ gazidan *beissen'
HRN.txt:7683:^S5. gäz *Zange, Scheere' (Sahn. I, 54, 391), falsch kdz,
=== ARY latin index AMBOR/BEAR/BROTHER ===
=== BQT انبر context ===
دساتراست:
پنح‌فر جود بدید آهد از شت ۱ زر نشت ۱
که به‌پیغمبر یش راست بوده‌پن حگو اه .
این‌شاعر شیرین زبان که بی‌شك از بزر گان سخن سرایان این دوزه
است؛ دساتر‌شناسی را جز ه معلومات خودشمرده یاتکلف ب‌یاری از لفت‌های
دسانبررا بنطم کشیده. از آ نپاست:
«در تقیم طبقات‌رعیت فرمودءمه ]باد» و «نامپای‌بروج دردساثم»
وجز آن. این‌چند فقره که در اینجا نگاشتبم ازبرای نمونه است» مشتی است
نمودار خروار. | گر باین و آن‌بر میعوردکانی را که‌نام خانوادگی خودرا
از لفت‌های دساتیری بر گز بده‌اند نیژاز برای‌نمو نه یاد میکردم...
زبان‌متن دساتير بز بانهای کپن ايران چون‌فرس هخامنشی واوستایی
```


## [2026-09-05T13:54:41.750Z] TOOL CALL #63: WebSearch

```json
{
 "query": "ریشه‌شناسی واژه انبر فارسی حسن‌دوست اتیمولوژی anbor tongs Persian etymology"
}
```


## [2026-09-05T13:54:42.780Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/phosphorus",
 "prompt": "Give the full etymology of phosphorus and phosphor: Greek phosphoros, the 1670s Brand discovery, French phosphore, and the elements phos + phoros. Quote verbatim."
}
```


### [2026-09-05T13:54:49.188Z] TOOL RESULT

```
# Etymology of Phosphorus and Phosphor

**Phosphorus** derives from Latin *phosphorus* meaning "light-bringing," which itself comes from Greek *Phosphoros*, "the morning star," literally "torchbearer." 

The term breaks down into two Greek components: *phōs* ("light") and *phoros* ("bearer," from *pherein* "to carry").

**Historical Discovery:**
Henning Brand, a Hamburg merchant and alchemist, isolated phosphorus in 1669 by deriving it from urine. According to the source: *"It is the first element whose discoverer is known."* Lavoisier later demonstrated it was an element in 1777, and the term became exclusively associated with this chemical element around 1750.

**Phosphor** emerged as a related term in the 1630s, initially designating "the morning star, Lucifer," derived from the same Latin root. By 1705, its meaning expanded to encompass "anything phosphorescent."

The modern chemical term **phosphate** (1795) derives from French *phosphate* via *phosphore*, incorporating the element name with the suffix *-ate*.
```


### [2026-09-05T13:54:49.430Z] TOOL RESULT

```
Web search results for query: "ریشه‌شناسی واژه انبر فارسی حسن‌دوست اتیمولوژی anbor tongs Persian etymology"

Links: [{"title":"ریشه‌شناسی - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D8%B1%DB%8C%D8%B4%D9%87%E2%80%8C%D8%B4%D9%86%D8%A7%D8%B3%DB%8C"},{"title":"محمد حسن‌دوست - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%85%D8%AD%D9%85%D8%AF_%D8%AD%D8%B3%D9%86%E2%80%8C%D8%AF%D9%88%D8%B3%D8%AA"},{"title":"انبر - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatofa/%D8%A7%D9%86%D8%A8%D8%B1/"},{"title":"فرهنگ ریشه‌شناختی زبان فارسی | راهک","url":"https://raahak.com/?p=942"},{"title":"کتاب فرهنگ ریشه‌شناختی زبان فارسی (جلد 5)","url":"https://fanuus.org/library/%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D8%B1%DB%8C%D8%B4%D9%87%D8%B4%D9%86%D8%A7%D8%AE%D8%AA%DB%8C-%D8%B2%D8%A8%D8%A7%D9%86-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-%D8%AC%D9%84%D8%AF-5/"},{"title":"کتاب ریشه شناسی زبان فارسی - اتیمولوژی - etymology منابع زبانشناسی - عصر زبان","url":"https://asrezaban.com/%DA%A9%D8%AA%D8%A7%D8%A8-%D8%B1%DB%8C%D8%B4%D9%87-%D8%B4%D9%86%D8%A7%D8%B3%DB%8C-%D8%B2%D8%A8%D8%A7%D9%86-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C/"}]

Based on the search results, I found some relevant information about the topics in your query:

Hasandoust (محمد حسن‌دوست) is the author of a comprehensive etymological dictionary of Persian, and this etymological dictionary of Persian language was published in five volumes by the Academy of Persian Language and Literature in 2014.

Regarding the etymology of the word "anbor" (انبر - tongs), one explanation suggests it is originally composed of two words ("ham" meaning together, and "bar" from the infinitive "bordan" meaning to carry), so "ruyham" means an instrument that carries and moves things together. However, there is also a Turkish origin proposed, where "an" (ان) is a superlative prefix like in "an-bozorg" meaning greatest, and "bor" (بور) comes from the Turkish verb "burmak" meaning to twist, making "anbor" mean something like "best twister".

The search results show different etymological interpretations of the word "anbor," with both Persian and Turkish linguistic origins being proposed.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T13:55:09.960Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"phosphor, n\\|phosphorus, n\\|phosphore\" KLN_1971.txt | head -5",
 "description": "Grep Klein for phosphor"
}
```


### [2026-09-05T13:55:10.005Z] TOOL RESULT

```
94879:-escence (on analogy of opalescence, phosphores- 
119597:ignis fatuus, phosphorescent light seen hovering 
162134:Noctiluca, n., a genus of phosphorescent marine 
181183:ing form meaning phosphorus or phosphores- 
181197:phosphorus, n. — ModL. phosphorus , ‘phospho-
```


## [2026-09-05T13:55:11.975Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A7%D9%86%D8%A8%D8%B1/",
 "prompt": "What do the dictionaries (فرهنگ معین، لغتنامه دهخدا، فرهنگ عمید) say about انبر: meaning and any origin/etymology tag? Quote the Mo'in and Dehkhoda entries verbatim, including any bracketed origin marker."
}
```


### [2026-09-05T13:55:19.118Z] TOOL RESULT

```
# Dictionary Entries for انبر

**Lughtnāmeh Dehkhoda** provides the most extensive entry, describing انبر as a two-pronged metal tool for grasping fire or hot objects, with multiple historical references and poetic citations. It also notes mechanical and nautical uses.

**Farhang-i Mo'in** offers a concise definition: "آلت فلزی دوشاخه که با آن آتش یا چیزی دیگر را برگیرند" (a two-pronged metal tool for grasping fire or other things).

**Farhang-i Omid** similarly describes it as: "وسیلۀ فلزی دوشاخه با دو فک که با آن آتش یا چیز دیگر را برگیرند" (a two-pronged metal device with two jaws for grasping fire or other things).

None of these three dictionaries include an explicit etymology or origin marker in the content provided. The Dehkhoda entry references various classical Persian sources and literary examples but does not attribute the word's linguistic origin.
```


## [2026-09-05T13:55:23.217Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '181180,181210p' KLN_1971.txt",
 "description": "Read Klein phosphorus entry"
}
```


### [2026-09-05T13:55:23.276Z] TOOL RESULT

```
phosphorize, tr. v. — F. phosphoriser, fr. phos- 
phor c. See phosphorus and -ize. 
phosphoro-, before a vowel phosphor-, combin- 
ing form meaning phosphorus or phosphores- 
cence . — Fr. L. phosphorus. See next word. 




PHOSPHORUS 



558 



phosphorus, n. — ModL. phosphorus , ‘phospho- 
rus’, fr. L. Phosphorus , ‘the morning star’, fr. 
Gk. cp<»>a<p6f>6(;, ‘light-bringer; the morning 
star’, which is compounded of 9W5, ‘light’, 
contr. of 91x05, and -96P05, ‘carrying’. The first 
element derives fr. I.-E. base *bhd-, ‘to shine’, 
whence also OI. bhati, ‘shines, glitters’, bhas-. 
Might, glory’. See phantasm and words there re- 
ferred to and cp. esp. the second element in 
Pasiphae. For the second element see -phorous. 
Derivatives: phosphor-ale, tr. v., phosphore-al, 
phosphor e-ous, adjs., phosphor-esce, intr. v., 
phosphor -esc-ence, n., phosphor-esc-ent, adj. and 
n., phospkor-ism, n. (med.), phosphor-ite, n.
```


## [2026-09-05T13:55:30.761Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%81%D8%B3%D9%81%D8%B1/",
 "prompt": "What does فرهنگ معین say about فسفر — quote the entry verbatim including any bracketed origin marker such as [فر.] and the French word. Also quote فرهنگ عمید if it gives an origin."
}
```


### [2026-09-05T13:55:37.025Z] TOOL RESULT

```
# فرهنگ معین Entry

According to فرهنگ معین, the entry states:

"(فُ فُ ) [ فر. ] (اِ. ) عنصری است جامد به رنگ های سفید، زرد، قرمز، قهوه ای ، بنفش که بوی سیر می دهد و در آب حل نمی شود."

This describes phosphorus as a solid element in various colors with a distinctive odor, insoluble in water.

# فرهنگ عمید Entry

فرهنگ عمید does not provide an origin marker or French source word. It simply defines phosphorus as: "عنصر غیرفلز شیمیایی زردرنگ، با بخارهای سمّی، و قابلیت اشتعال فراوان" (a non-metallic chemical element that is yellow-colored with toxic vapors and high flammability).
```


## [2026-09-05T13:55:51.673Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0er-' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0r%C3%A9h%E2%82%82t%C4%93r' \\\n 'https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D8%A7%D8%AF%D8%B1' \\\n 'https://en.wiktionary.org/wiki/%D8%A8%D8%B1%DB%8C%D8%A7%D9%86' \\\n 'https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D8%B4%D8%AA%D9%86' \\\n 'https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%A8%D8%B1' \\\n 'https://www.etymonline.com/word/phosphorus' \\\n 'https://abadis.ir/fatofa/%D8%A7%D9%86%D8%A8%D8%B1/' \\\n 'https://abadis.ir/fatofa/%D9%81%D8%B3%D9%81%D8%B1/' ; do\n  python3 tools/fetch_source.py \"$u\" --note 'pdf page 89 (Bher 1 / Bhra-tar, Bher 2): verification of roots, Persian baradar, berestan/beryan/berijan, anbor, fosfor/phosphorus' 2>&1 | tail -2\ndone",
 "description": "Archive web sources used"
}
```


### [2026-09-05T13:55:56.250Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/4d8b4eb79876555d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8e37648abcab5621.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/194cd4cceb7815b1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c36922247dae70bd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c113f533082b6170.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dc93e6cd09178bce.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/008d977afc1818a4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e8b3b76f7c8315b2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6bc740c1e3fb93b3.txt
```


## [2026-09-05T13:56:02.398Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nmkdir -p data/verification/sources/refs/ocr/BOOK\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg89.png data/verification/sources/refs/ocr/BOOK/89.png\nls -la data/verification/sources/refs/ocr/BOOK/ | head\necho \"=== verify_check ===\"; sed -n '1,120p' tools/verify_check.py",
 "description": "Copy page PNG and read verify_check.py"
}
```


### [2026-09-05T13:56:03.843Z] TOOL RESULT

```
total 2072
drwxrwxr-x 2 sfmqrb sfmqrb   4096 Sep  5 09:56 .
drwxrwxr-x 9 sfmqrb sfmqrb   4096 Sep  5 01:38 ..
-rw-rw-r-- 1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r-- 1 sfmqrb sfmqrb  86203 Sep  4 19:03 126.png
-rw-rw-r-- 1 sfmqrb sfmqrb 105296 Sep  4 19:03 311.png
-rw-rw-r-- 1 sfmqrb sfmqrb  96466 Sep  4 19:03 33.png
-rw-rw-r-- 1 sfmqrb sfmqrb  99093 Sep  4 19:03 39.png
-rw-rw-r-- 1 sfmqrb sfmqrb  54479 Sep  4 19:03 46.png
-rw-rw-r-- 1 sfmqrb sfmqrb  99295 Sep  4 19:03 54.png
=== verify_check ===
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


## [2026-09-05T13:56:13.801Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT bratar ===\"; grep -n \"brātar\\|brätar\\|brotar-\\|brätar-\" BRT.txt | head -8\necho \"=== BRT bar- ===\"; grep -n \"^bar-\\|bar- \\[tragen\\]\\|,tragen\" BRT.txt | head -8\necho \"=== HUB brader ===\"; grep -n \"birāder\\|birader\\|brātar\" HUB.txt | head -8",
 "description": "Grep Bartholomae and Hübschmann"
}
```


### [2026-09-05T13:56:13.881Z] TOOL RESULT

```
=== BRT bratar ===
=== BRT bar- ===
=== HUB brader ===
```


## [2026-09-05T13:56:16.399Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LEW frater ===\"; grep -n \"frāter\\|frater,\" LEW_1910.txt | head -5\necho \"=== LAT frigo ===\"; grep -n \"frigo\\|frīgō\\|frigere\" LAT.txt LEW_1910.txt | head -8\necho \"=== SKT brother/bear ===\"; grep -n \"^Brother\\|Brother, \" SKT.txt | head -5; grep -n \"^Bear (1)\\|Bear, to carry\" SKT.txt | head -5",
 "description": "Grep Latin dictionaries and Skeat"
}
```


### [2026-09-05T13:56:16.485Z] TOOL RESULT

```
=== LEW frater ===
=== LAT frigo ===
LAT.txt:2332:rurale a pris le sens de "condenser, epaissir, r6duire": frigore mella
LAT.txt:2671:rent de frigere "etre froid").
LAT.txt:24184:tation, effervescence (cf .Lucr., 4,1030); 3 0 limite, fosse. Snfin, la- 451 - frigo
LAT.txt:24219:frigo, -is?: frigit correpta prima syllaba significat erigit. Ac¬
LAT.txt:24225:frigere est et friguttire cum sono sussilire... Afranius Priuigno («45):
LAT.txt:24230:frigo, -is, -xl, -ctum (et -xun),-e re: rotir, griller, frire. Le
LAT.txt:24237:in oleo ardet. Rapprochd de cppuyei.v par Festus: frigere et frictum
LAT.txt:24249:frigus, -oris n.(et a partir de S^-Augustin frigor aasc. d'apros
=== SKT brother/bear ===
```


## [2026-09-05T13:56:20.216Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '24230,24250p' LAT.txt\necho \"=== LAT frater ===\"; grep -n \"frere\\|frater\" LAT.txt | head -8",
 "description": "Read Ernout-Meillet frigo and find frater"
}
```


### [2026-09-05T13:56:20.275Z] TOOL RESULT

```
frigo, -is, -xl, -ctum (et -xun),-e re: rotir, griller, frire. Le
sens special de "frire" est secondaire. Le sens preaier est "faire
secher par la cuisson, cuire k sec"; cf. Caton, Agr.106,1 sesquilibram
salis frigito', Pl., Ba.767, frictum cicer, et CGL V 456,37, frixi cice¬
ris: fabae siccatae in sole, etc.,aais c'est au sens de "frire" que
songe Isid. quand il £crit, Or. 30,3,33, frixum a sono dictum, quandofrigus
453
in oleo ardet. Rapprochd de cppuyei.v par Festus: frigere et frictum
a Graeco uenit cppuyeiv, P.F. 80,34. - Anci en, technique. Fanroian.
M.1.35x0 et 3Saa frixa, 3504 *frlcta.
D 4 riv 4 s: frixor (Gloss.), frlxBrius, frlxBrium (et frlxUria, *frlx 5 ria
M.L.3534); frlxdra fM.L.353C; frixo,-as (Cael. Aurei.); cf. aussi
frlcticulae (S^-Jdr. )> frlcticus (Orib.); et M.L.350O *frictura, 3533
*frlxeolum.
Coapos£s: con-, ef-, re-frigB.
Le sens de onbr. frelitu, frebte n'est pas 4 tabii avec certitude.
Sans doute not expressif; on trouve ailleurs, au aene sens, des
aots senblables, nais differente: gr. cppuyoa "je fais griller", skr.
bhrjyiti "il fait griller", etc. - Cf. le groupe de friguttio.
frigus, -oris n.(et a partir de S^-Augustin frigor aasc. d'apros
calor, sudor, M.1.3513, et 1 tres basae 4 poque frigora, frigura f^ainin
=== LAT frater ===
173:famille, pater, mater, frater, les principaux animaux do-
6488:auunculus, -I ( aunc(u)lus, auonc(u)lus) m,: oncle (frere de la
6489:mbre; le frere du pbre est patruus-, a pour correspondant feminin mater¬
22364:1'figi., et coaae frater, soror, nn sens affectif; filii, A basse £poqne
24017:frater, -trls m.: i° frere par le sang, la parente £tant precisee
24018:par une 4 pithbte; /• germanus, geminus, uterinus ; 3 0 frere par alliance;
24022:peut designer le frbre et la soeur. frater s'emploie souvent comme
24024:Volo, mi frater, fraterculo tuo credas: consorti quidem in lucris
```


## [2026-09-05T13:56:21.225Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT sample ===\"; head -c 600 BRT.txt; echo; echo \"=== grep Bruder in BRT ===\"; grep -n \"Bruder\" BRT.txt | head -8\necho \"=== HUB sample ===\"; grep -n \"Bruder\" HUB.txt | head -8",
 "description": "Check BRT and HUB file contents"
}
```


### [2026-09-05T13:56:21.292Z] TOOL RESULT

```
=== BRT sample ===
Google
This  is  a  digital  copy  of  a  book  that  was  prcscrvod  for  gcncrations  on  library  shclvcs  bcforc  it  was  carcfully  scannod  by  Google  as  pari  of  a  projcct
to  make  the  world's  books  discoverablc  online.
It  has  survived  long  enough  for  the  Copyright  to  expire  and  the  book  to  enter  the  public  domain.  A  public  domain  book  is  one  that  was  never  subject
to  Copyright  or  whose  legal  Copyright  term  has  expired.  Whether  a  book  is  in  the  public  domain  may  vary  country  to  country.  Public  domain  books
are  our  gateways  
=== grep Bruder in BRT ===
3097:•  j.  a;'rae'ra9^-  m.  EN.  eines  Gläubigen, eines  Bruders  Franrasyan%:  "'^aAe  nara- vahe  alaonö  Yt/^.  131;  —  puirS  kaoia (sd.)  syävarsänai  .  .  ""^ake^a  naravaht ".  .  und  (als  Rächer  des  Ä. . ."  YLf?.i8,
6581:des..';  a)  sva.  'J^mands  (Eigentum)  sein,  J2(?);  —  ust.l(sd.)  asti  .  .  aAmSi  hyat.. ihm  eignen,  angehören,  ihm  zu  eigen,  zu  ahm  Y.  27. 14;  —  cvat  ahmrti  naire  miz- teil  werden';  A)  I  im  Ap.:  aita''  xsa-  d^nt  atshal  "wie  gross  ist  der  Lohn,  der 'i''am  AacJ  paruviyatt^  amäxam  taumäyä  dem  Mann  zu  teil  werden  wird?"  Y.8. 3ki^  "dieses  Reich  gehörte  von  alters  her  81,  A.4.4,  öi  —  akmii  aukat  vahist^m unserer  Familie"  Bh.  /.  12;  —  avahya  ys  . .  "dem  soll  das  Beste  zu  teil  werden, ki^büjiyahyä  brätä  bardiy<^  nlma*  ähJ'  der  .  ."  Y.J/.6;  50.3;  —  aiibyS  a»hSus "jener  K.  hatte  einen  Bruder,  B.  mit  |  avBi  (sd.)  ar^hat  apsnum  Y.  45. 3.  a)  mit Namen"  Bh.  f.  10.  B)  im  Aw.:  aiiii'O' ,  praedik.  Nom.  'dienen  als  .  .':  äat  pasca dqma .. ya  hpnti  spstäahe  tnainySu?  "die.. ; . .  vasS  i^ariis  aah^n  mnbyS  "aber  nach Geschöpfe,  die  die  des  heiligen  Geistes  ,  .  sollen  sie  nach  Belieben  den  Männern sind"  Yt  i^.  2 ;  —  tat  jfarpnS  .  .  yat  asti  als  Speise  dienen"  V.  6. 43.  b)  'dasein,
7701:•  j,  'arazav-  m,  EN.  eines  Gläubigen' Bruders  des  Sra/öjpada  (sd.):    'ma  (GD.) srBtöjfädä  ahonä  Yty,  115.
8917:"..als  Rächer  des  Bruders.."  Yt. /j.  28;  —
9589:•  j,  karasa'vazdah-  m.  EN.  eines  Bruders  ,  äat  [mam]  *i'^>  arihsits  aslva0  aismanam
11618:(Za/*äoTt75)  zweier  Gläubiger  r)  des  Mi- nisters Visiäspai,  Schwiegersohns  Zara- &aÄr<is">,  Bruders  FraSao^tra%  aus  der ^»j^flfamilie:  °pahe  AvSvaAe  (sd.)  Yt y- 1 03  j  — ya^rS  vS  a/sman[{sd.)  sSrtghänT ..  'pa  (VS.)  hvs^va  (sd.)  Y.  46,  17; 4g.  9 ;  —  tarn  ciitltn  'fS  hvB.gvS  tsldü :^armh  (sd.)  ala  vtnnti  Y.  5/.  18;  — yS  . .  bar?sma  */rasttrmte  ya%a  asava  °p5 */rastfrinaSa  ra/u/rif  li.Sg;  —  amava ya^a  °pü  Az.  2;  2;  Vyt_j;  —  yävaranä *frasaoslra  •/s(ND.)  ..ta  vannilcä (sd.)  . . Y./2, 7;  —  ao/i/a  tT  zarai:uslra  fralaos- tralibya  'pa^bya  Vyt.  //;  —  tarn  (näml. andvltn)  yazaia  -ps  yat  spShm  pairi.- avalnal . .  drvatqm  Yt  5.  68,  a)  °pafie aparamtahe  (sd.)  asaonS  Yt  ij.  127.
12740:0  Ah"  Y.  48.  7  ;  —  taten  matdä  'i^wahml a  *dqm^'>  '>  nipAr»Ae  mans  vohB  umnascä  . . "und  das,  o  M.,  will  ich  in  deinem  Haus-*' in  Verwahr  geben:  den  guten  Sinn  und  .  ," Y.  4;^.  10;  —  ila  asti  .  .  sp>nta  ärmaitis mana  (oämL  ahurahe)  dqmi'^  Yt  i.  35; 25*;  —  äkästSng  (sd.)  mä  msqsya  ds^Jm djAvä^LP.)  Y.50. 2;  —  ySi  ..  aiamgm  va- rtdtn . .  tsi  dalvifig  dqn ''  ya  drpgvatS  datnä (Sp.  666  o.)  Y49.4.  '  a)  GS.  la&patay-  m. '(Hausherr  sva.)  gebietender  Herr,  Ge- bieter': saoiyants  dJrtg  (GS.)  patsU  spmlä dainä  urvais  *brata  *pts  va  mazda  ahurä "des  Saoiyant,  des  gebietenden  Herrn heilige  DaSita*^  wird  (ihm)  Freund,  Bruder oder  Vater  sein,  q  MAA."  Y.  4:5. 11.
16961:•  p.  bardiya-  m.  EN.  eines  Persers, Bruders  des  Kambyses,  Smerdis:  avahyH k<^bUjiyahya  brätä  'yJ^  tiäm<i*  äA(^ Aamätä  Aamapitä  ka^büjiyahyä  Bh.  /.  lo:
=== HUB sample ===
4098:'Bruder* = ap. braid neben birddar ap. *brdtaram; ditxt *Tochter* =
5259:iiber , birOdar *Bruder\ barda *Gefangener , barz Teldarbeit',
6060:d) Einschub von i in: biradar *Bruder = ap. bra-
6380:dan *schenken H. 186; biradar *Bruder H. 192; baraz
6684:pitar-; birddar = hiradar *Bruder, ap. bratar-; madar
7131:harazat *leiblicher Bruder' auf "^hadazat = zd. hadozdta-. ^)
```


## [2026-09-05T13:56:31.630Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT brat lemma ===\"; grep -n \"brätar-\\|brätar\\|bratar-\\|brätar-  m\" BRT.txt | head; grep -n \"'brätar\\|«brätar\\|bräta r\" BRT.txt | head\ngrep -n \"bratar\" BRT.txt | head\necho \"=== E-M frater ===\"; sed -n '24017,24040p' LAT.txt",
 "description": "Find Bartholomae bratar and Ernout-Meillet frater"
}
```


### [2026-09-05T13:56:31.720Z] TOOL RESULT

```
=== BRT brat lemma ===
=== E-M frater ===
frater, -trls m.: i° frere par le sang, la parente £tant precisee
par une 4 pithbte; /• germanus, geminus, uterinus ; 3 0 frere par alliance;
/. patruSlis ou frSter seul "cousin germain" du cot£ paternel; beau-
frbre = leuiry 3 0 membre d ( une confrerie (sens qu’on retrouve enombrien):
fratrSs Arudles, c£ gr. cpptxxpa, cppaxpta. Comme gr. <x8eX<fm, le pl. fratres
peut designer le frbre et la soeur. frater s'emploie souvent comme
terme d'amiti£, e.g.: quam copiose laudatur Apronius a Timarchide...
Volo, mi frater, fraterculo tuo credas: consorti quidem in lucris
atque in furtis, gemino et simii limo nequitia, improbitate, audacia,fratiIli
- 448
Cic.,Verr.«,3,66,155. De 14 le sene spdcial qu'il a pris dans la langue
4 rotique: "aaant, aignon". Enfin, coaae a&eXcpoC, fr&ter se dit aassi
d'objets de meae natnre et rapproch 4 s; de 14 frStrare: - puerorum
mammae dicuntur, cum primum tumescunt, quod uelut fratres pares oriun¬
tur, quod etiam in frumento spica facere dicitur, P.F.8o,«i; cf. l'en-
ploi de soror, sororiare, Usit 4 de tout teaps. Paaronan. M.L.3485.
Derivas et conpos 4 s: fratria (et fratrissa Isid.) f.: uxor fratris',
fraterculus et fratellus (Scaurus GLK VII 13,13, cf. M.L.34O4, it.
fratello)', fraternus', d'o 4 dans la 1 . iap 4 riale frdternitSs, g 4 n 4 ralis 4
par lal.de 1 ’igl.; frdtruglis (fom 4 d'apres patruus/patruSlis)
"fils du frbre, cousin geraain"; M.L.3486 (logoud. /radile); frdtro, - 5 s
(d'ou fratrabi liter Inscr. de Ponp 4 i), et frSterculd , v. plus haut;
- frdtrimSnium (Not.Tir.); frdtri-clda, -cidium, faits sur pari eida.
L'un des grands noas de parenti indo-europ 4 ens, designant les aea-
```


## [2026-09-05T13:56:39.743Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '24040,24050p' LAT.txt\necho \"=== WLD Bd2 bher tragen ===\"; grep -n \"tragen, bringen\\|bher- ,tragen\" incoming/WLD/WLD_Bd2_pages.txt | head -5\necho \"=== WLD Bd2 bhrater ===\"; grep -n \"bhräter\\|bhrater\" incoming/WLD/WLD_Bd2_pages.txt | head -5",
 "description": "More Ernout-Meillet and Walde-Pokorny"
}
```


### [2026-09-05T13:56:39.809Z] TOOL RESULT

```
L'un des grands noas de parenti indo-europ 4 ens, designant les aea-
bres de la faaille, qui sont au aeae niveau par rapport au chef, le
*pater~, ce qui n 1 iaplique sans doute pas qu'iis etaieut tous ses
enfants (de aeae soror); en grec cppaTr^p, cppotTtop ne s’est conserv 4
qu'au sens de "aeabre de la aeae cppaxpia". Le aot se retrouve dans
osq. fratrum (g 4 n.plur.), oabr.frater, frater "fratres", iri. brathir,
got .bropar, ara. eibayr, skr. bhr&td (thfeae bhr&tar-). Le slave et le
baltique ont des derives: v. sl. bratru ( brotu), lit. broter-e lis, etc.
Pour l'u de fratruelis, cf. skr. bhr&trvyah, mr.brdtuiryt "fils de
fr&re". Pour la forae, cf. patruus sous pater.
fratllll: uilli sordidi in tapetis, P.F.80,14. Cf . fratellis: sor¬
=== WLD Bd2 bher tragen ===
1469: auf verfallen'** (Osten-Sacken IF. 33, 240).                         — Apr. pijsi „tragen, bringen*^,
10193:    Got. bairan „tragen, bringen, hervorbringen, gebaren“ (bSrusjds „Eltern“),
10195:              „tragen, ertragen, bringen, gebaren“, ahd. beran „tragen, bervor-
=== WLD Bd2 bhrater ===
9976:      durch aksl. bhvati erwiesen, nocb durcb "^bhrater- „Bruder‘‘, dessen
```


## [2026-09-05T13:56:44.850Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '10150,10200p' incoming/WLD/WLD_Bd2_pages.txt | head -60\necho \"=== WLD Bruder entry ===\"; grep -n \"„Bruder\" incoming/WLD/WLD_Bd2_pages.txt | head -10",
 "description": "Read Walde-Pokorny bher- entry"
}
```


### [2026-09-05T13:56:44.910Z] TOOL RESULT

```
   -fer in Zs.    ,,tragend, bringend"; fordtis                          ..trachtig'^     {do-   Erw. des Adj-
^bJioro-s „tragend‘‘,               s.   Yf. LEWb.^       s. v.   und vgl.        ksl.   brehla);
  far „Dieb“ (= gr. cpdoQy s. o. zum lat. it s. Yf. LEWb.^ s. v. m. Lit.,
                                                      :


Solmsen IP. 31, 477 A. 1, Bthl. Wf. Kl. Phil. 1916, 1027ff.);
  fors nom., forte abl. „Zufall” (,,was sich zutragt, was das Geschick bringt”)
— pal. forte „fortuna“                   (s.   o.);

   fortuna „Zufall, Gliicksfall, Gluck“ (von einem                                           %lir-tii-s).

   Air.    1. sg.         bira (Thurneysen KZ. 44, 113f.),                   3.    sg, berid ,,tragen“      asbinr
„sage'‘, dchktr           cymr. cymeraf „nehme'' usw. (Formenbestand bei
                             ,,gebe'*,
Pedersen KG. II 463 ff.); mir. bert „Bundel Geburt“ (s. o.);             ;



  air. mir. breih und (eig. Dat. Akk.) brith^ breith (gen. brithe) „da8 Tragen,
Gebaren (Inf. zu biru); Geburt; UrteiP' f^bhrta); cymr. bryd „Gedanke“
(eher %hrtu-y als "^bhrti-y s. Pedersen KG, II 34), corn, brya „Gedanke“,
a brys benen ,.from the womb of woman“, gall, nergo-bretus Amtstitel (Pick
 II ^ 16Sf., Pedersen KG. I 42, 105j;
   ir.   barn    i.                              cymr. bret. barn „I]rteiP' (wohl
                          rechtaire ..Richter' (Corm.).
 ^bb^rnoSy       oben alb. bare; Pedersen KG. I 51 nimmt -P-, d. i.
                vgl.                                                          an);
    air. braihy gen. -o ,,Gericht“, cymr. brand ..UrteiP', corn, bres ds., bret.

 hrexit „plaidoyer*, pi. brenjoti ,,les assises de la justice'', gall. Bratu-span-
 iium OK., foarovde .,ex judicio"                   ein idg. *bhra-tti zu erwageii
 nach Pedersen KG. I 52, bietet aksl, bhraii keine Handhabe; die Gruppe
 gehort trotz B. bei Pick II ^ 169 nicht zu gr. pQ)]Vy aisl. grunr
 gruna „beargwohnen'‘).
                                     ;       ;                     ;                             ;




 156                                             bher


    Got. bairan „tragen, bringen, hervorbringen, gebaren“ (bSrusjds „Eltern“),
      aisl. bera
              „tragen, ertragen, bringen, gebaren“, ahd. beran „tragen, bervor-
 bringen, Fruchttragen, gebaren“, nhd. gebaren, as. beran „gebaren“, ags.
 beran „tragen, gebaren“;
   got. aisl. ahd. as. barn, ags. beam „Kind“ (s. o.) got. barms „Brust“, schwe d.
                                                     ;

=== WLD Bruder entry ===
9976:      durch aksl. bhvati erwiesen, nocb durcb "^bhrater- „Bruder‘‘, dessen
12653:       Ai.      bhrcdar-,       av.     ap.       braiar-      „Bruder“;      arm. dbair,     gen.    elbaiir   ds.
12658:vbi „Bruder“ (? G. Meyer Alb. Stud. Ill 36; Koseform?);
12668:ags. brlpor „Bruder“; apr. brote, brati „Bruder^‘ \brair7kai ^Briiderchen^')?
26503:vas „Bruder der Frau" (Wiedemann BB. 27, 212), wozu koiycoviiav^ <PQ(x-
30347:mann", svaine ,,die Schwester der Frau", lett. sivainis „Bruder der Frau";
34201:sia*[u]ro-; s^^ur(io-) oder 8i9Ur(io-) „Bruder der Frau”.
34263:  Ygl. im allg. Curtius 381, Yf. LEWb.^ u. stio.                                   S. noch* sid^uro-       „Bruder
```


## [2026-09-05T13:57:11.178Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT ambar/anbur ===\"; grep -n -i \"ambar\\|anbur\\|ambur\" LKT.txt | head -8\necho \"=== HJB ===\"; grep -n -i \"amber\\b\" HJB.txt | head -3\necho \"=== SYN tongs 5.36? ===\"; grep -n -i \"TONGS\" SYN.txt | head -5",
 "description": "Grep Lokotsch and Buck for tongs/ambar"
}
```


### [2026-09-05T13:57:11.250Z] TOOL RESULT

```
=== LKT ambar/anbur ===
97:IB  =  Die  Reisen  des  Arabers  Ibn  Batata  durch  Indien  und  China  (14.  Jahrhun- dert). Bearbeitet  von  Hans  von  Mzik.  (Bibliothek  denkwürdiger  Reisen,  heraus- gegeben von  Ernst  Srhultze.  5.  Bd.)  Hamburg  191 1.  —  (Verweisungen  auf  den arabischen  Urtext  des  Ibn  BattOta  beziehen  sich  auf  Voyages  d'Ibn  Batoutah, texte  arabe.  arcompasrne  d'une  traduction  par  C.  Defremery  et  H.  B.  San- guinetli.    4  Buo.    Paris  1853/59.)
128:MP  =  Die  Reisen  des  Venezianers  .fVlarco  Polo  im  13.  Jahi hundert.  Bearbeitet und  herausgegeben  von  Hans  Lemke.  (Bitiliothek  wertvoller  Memoiren  heraus- gegeben von  Ernirt  Schnitze.    1.  Bd.)    Hamburg  1908.
395:'Schuppen',  gesprochen  ämbär  [von ämbästän  'anfüllen,  anhäufen'  Horn NpEt  S.  26,  Nr.  III],  ebenso  tk.  ambar. Hieraus  rum.  ambar,  hambar  'Speicher, Schuppen,  Kornboden',  Ableitung  ham- bara^;  russ.  bulg.  serb.  ambar  'Scheune, Schuppen,  Speicher',  poln.  ambar,  im- bar,  kl  russ.  ambar  'Niederlage'.  — VÖLLERS  in  ZDMG  LI,  299  Nr.  94 will  jedoch  anbär  aus  gr.  ^lunöpiov  ab- leiten.   [Gorjajew,4.  Bern  SlEtWb  28.
397:Mit  Assimilation  'ambar  gesprochen; hieraus  it.  ambra,  frz.  ambre,  sp.  pg. ambar,  [mit  ar.  Art.]  alambar,  alambre, rum.  ambrä,  ambru;  engl,  ambre,  ndl. amber,  dtsch.  Amber;  russ.  ambra.  — Aniber  ist  eine  ihrer  Herkunft  nach zweifelhafte,  ilirer  Zusammensetzung nach  unvollständig  bekannte,  sehr  teure, dunkelgraue  Masse,  die  in  früheren Zeiten  in  der  Medizin  hochgeschätzt war,  während  sie  heute  fast  nur  noch zur  Herstellung  von  Parfümen  benutzt wird.  In  rundlichen  oder  kantigen Stücken  auf  dem  Meere  schwimmend oder  am  Strande  angespült,  wird  die Ambra  im  Indischen  Ozean  gefunden und  für  feine  Sorten  je  kg  5000  Mark und  mehr  gezahlt.  Vermutlich  ist  der Amber  die  verhärtete  Kotmasse  des Pottwals  Catodon  macrocephalus  Lac. —  Dazu  engl,  yellow  amber  'Bernstein'. [DE  188/9.  Eguilaz  258.  ML  441. Gorjajew  4.
442:[Auch  ärguwän,  ärguma»;  vgl.  hebr. nrgämän,  dieses  aus  assyr.  argamamtu 'roter  Purpur',  DelHWB  129a,  und schließlich  wohl  aus  ind.vgl.ZAkkFW37] 'Purpur,  Purpurstoff,  purpurfarben' [nämlich  'dunkelviolett'  nach  P.  HAUPT in  Verhandlungendes  13.  Internationalen Orientalistenkongresses  Hamburg  1902. Leiden  1904.  S.  218[,  ebenso  tk.  erge- Iran  [Kelekian  Kamüs  68b]  'dass.  und Cercis  siliquastrum';  hieraus  rum.  ior- govan  'spanischer  Flieder,  Syringa  vul- garis'. Serb.  jergoran  'dass.'.  [Löbel EITAP  56.
732:2'i7.  Ar.  barbäris: [Entstanden  aus  nnnr  hüris  über  ambar bäris,  vgl.  FLEISCHER  in  BSGW  phil. bist.  Kl.  1881,  XXXill,  9]  'eine  Pflanze Berberis  vulgaris',  deren  Beeren  zu  Mar- mel.ide,  Sirup  oder  Eis  verarbeitet  wer- den; die  Apotheker  benutzen  ihre  Wur- zalrinde;  zuerst  wurde  die  Pflanze  von den  Arabern  verwertet.  Frz.  berberis, engl,  barberry  [aber  berberine  'die  dar- aus gewonnene  Substanz  zum  Gelb- färben'], dtsch.  Berberize,  Berberstaude, Berberisbeere.  Russ.  barbaris  'Sauer- dorn'.
1378:'Trommel,  Tamburin';  hieraus  mit  ar. Art.  sp.  adufe  'dass.',  pg.  adufe  'Schellen- trommel', arfi</"fc'8Vo  [Constancio  Dicc26c]. Wie  die  Kastagnette  arabischer  Herkunft. [DE  50.
1386:[Pijn  113]  'Seekuh,  Halicore  Dujong'  im Indischen  Ozean  [über  sie  vgl.  besonders 0.  Finsch,  Der  Dujong.  Zoologisch- ethnologische Skizze  einer  untergehenden Sirene.  Hamburg  1901.  Sammlung  ge- meinverständlicher wissenschaftlicher
=== HJB ===
1490:1592. — "We  sent  commodities  to  their king  to  barter  for  Amber-greese,  and  for  the homes  of  Abath,  whereof  the  Kin^  onel^ hath  the  traffique  in  his  hands.  Now  thus Abath  is  a  bsast  that  hath  one  home only  in  her  forehead,  and  is  thought  to  be the  female  Vnioome,  and  is  highly  esteemed of  all  the  Moores  in  those  puts  as  a  most soveraign^  remedie  against  poyson.*' — Bar- ker in  Hakl.  ii.  591.
4986:Moodeen  Sheriff  says  that  Jedfitr  is used  (in  Ind.  Materia  Medica)  for <  amber.'  Tdhasklr  (see  TABASHEEB), is,  according  to  the  same  writer,  called hdm-kdfur  *  bamboo  -  camphor ' ;  and ras-kafilr  (mercury-camphor)  ^  is  an impure  subchloride  of  mercury.  Ac- coming  to  the  same  authority,  the varieties  of  camphor  now  met  with in  the  bazars  of  S.  India  are— 1.  MfUr- i-iaifuriy  which  is  in  Tamil  called pach^iJi'ai  {i,e,  crude  kamppuram;  2. Mratl  kdfar;  3.  cklnl;  4.  haiai  (from the  BaJtta  country?).  The  first  of these  names  is  a  curious  instance  of  the perpetuation  of  a  blunder,  originating m  the  misreading  of  loose  Arabic writing.  The  name  is  unquestionably •anfMrl,  which  carelessness  as  to  points
5689:GERAME,  GABAME,  &c.,  s.  The Malayalim  hdrnbi,  a  gatehouse  with  a room  over  the  gate,  and  generally fortified.  This  is  a  feature  of  temples, &c.,  as  well  as  of  private  houses,  in ^Ii^bar  [see  Logan,  i.  821.  The  word is  also  applied  to  a  chamber  raised  on four  poets.  [The  word,  as  Mr.  Skeat notes,  has  come  into  Malay  as  sarambi or  tawmbiy  *a  house  veranda.']
=== SYN tongs 5.36? ===
5997:1, IB *dont-, *dnt-, prob. a pple. form of *ed- ‘eat’. But some think this is only a secondary association and con nect with the root of Grk. daxvw ‘bite’, OE tang ‘tongs’, etc. Walde-P. 1.120. ErmoutM. 260f. Walde-H. 1.340 f. Feist 483.
6867:OHG zanga ‘tongs’, etc. Walde-
14144:2. Lat. forfex, esp. pl. forficés (> Olt. forfice, It. forbict, Rum. foarfeci, pl.), history complicated and disputed. Prob. fr. forceps, ‘pair of tongs, forceps’ (cpd. of formus ‘warm’ and root of capere ‘take’) with phonetic changes (through an intermediate forpex by dissim.) and shift of application from ‘tongs’ to ‘shears’ owing to the similarity of shape. Walde-H. 1.526f. (with full refs.). REW 3485.
```


## [2026-09-05T13:58:04.979Z] AGENT

Now I'll write the verification file.


## [2026-09-05T14:10:28.756Z] TOOL CALL #79: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk89.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\nPIE_BHER = W + \"Reconstruction:Proto-Indo-European/b%CA%B0er-\"\nPIE_BRAT = W + \"Reconstruction:Proto-Indo-European/b%CA%B0r%C3%A9h%E2%82%82t%C4%93r\"\nWK_BARADAR = W + \"%D8%A8%D8%B1%D8%A7%D8%AF%D8%B1\"\nWK_BERYAN = W + \"%D8%A8%D8%B1%DB%8C%D8%A7%D9%86\"\nWK_BERESHTAN = W + \"%D8%A8%D8%B1%D8%B4%D8%AA%D9%86\"\nWK_ANBOR = W + \"%D8%A7%D9%86%D8%A8%D8%B1\"\nETY_PHOS = \"https://www.etymonline.com/word/phosphorus\"\nAB_ANBOR = \"https://abadis.ir/fatofa/%D8%A7%D9%86%D8%A8%D8%B1/\"\nAB_FOSFOR = \"https://abadis.ir/fatofa/%D9%81%D8%B3%D9%81%D8%B1/\"\n\nPOK128 = (\"POK_01.txt:1800 (page marker '128' at line 1789): \\\"1. bher- ,tragen, bringen' usw. \"\n          \"(auch Leibesfrucht tragen; med. ,ferri'), auch ,aufheben, erheben' ... Ai. bhárati ,trägt', \"\n          \"av. baraiti ds. (und ,reiten'), apers. barantiy 3. Pl. ds. (= arm. berem, phryg. aß-ßeQet, \"\n          \"gr. φέρω, lat. ferö, air. biru, alb. bie, got. baira, aksl. berq)\\\"\")\nPOK163 = (\"POK_01.txt:2352 (page 163, the '164' marker follows at line 2359): \"\n          \"\\\"bhrāter- ,Angehöriger der Großfamilie, Bruder, Blutsverwandter'. \"\n          \"Ai. bhrātar-, av. apers. brātar- ,Bruder'; ... gr. φράτηρ ... \"\n          \"lat. frāter ,Bruder' ... got. broþar, aisl. bróðir, ahd. bruoder, ags. bróþar ,Bruder'\\\"\")\nPOK137 = (\"POK_01.txt:1927 (page marker '137' at line 1923): \\\"6. bher- mit g-Erweiterungen, wovor z.T. i-, u-Vokale, \"\n          \",rösten, backen, kochen'; von 2. bher- ,sich heftig bewegen, wallen, kochen' abgeleitet. ... \"\n          \"2. Formen mit i, ei: Npers. biris-tan ,braten', bᵉrezan ,Backofen', bal. brejag, brijag ,braten', \"\n          \"npers. biryān (*brigāna-) ,gebraten' ... (iran. *brij-, *braij-). Lat. frīgō, -ere ,rösten, dörren'\\\"\")\nKNT200 = (\"KNT.txt leaf NR=224/225 (printed pp. 200-201): \\\"bar- vb. 'bear, lift up, esteem': present stem bara-, \"\n          \"Av. baram, NPers. bard, Skt. bhárati, Gk. φέρω, Lt. ferō, Gt. bairþ, pIE *bhere/o-\\\"; \"\n          \"then \\\"ā + bar- 'perform': ābaratiy\\\"; \\\"pati- + ā + bar- 'bring back, restore': patiyābaram\\\"; \"\n          \"\\\"parā + bar- 'bear away, take away': parābara\\\"; \\\"pari- + bar- 'protect, preserve': paribarāmiy\\\"; \"\n          \"\\\"fra- + bar- 'proffer, grant': frābara\\\"\")\nAHD_BHER1 = (\"AHD_watkins1985.txt:333 \\\"bher-1. To carry; also to bear children. 1.a. Germanic *beran in Old English beran, \"\n             \"to carry: BEAR ... 3.a. Germanic *burthinja in Old English byrthen, burden: BURDEN; b. Germanic *burthiz in \"\n             \"Old Norse burdhr, birth, akin to the source of BIRTH; c. Germanic *burja- ... 4. Compound root *bhrenk-, to bring \"\n             \"... in Germanic *brengan in Old English bringan, to bring: BRING. 5. Latin ferre, to carry: -FER, FERTILE; \"\n             \"AFFERENT, CONFER, DEFER, DIFFER, ... OFFER, PREFER, ... REFER, SUFFER, TRANSFER ... 8. Greek pherein, to carry ... \"\n             \"[Pok. 1. bher- 128.]\\\"\")\nAHD_BRAT = (\"AHD_watkins1985.txt:342 \\\"bhrater-. Brother, male agnate. 1. Germanic *brōthar- in Old English brēthor, \"\n            \"brother: BROTHER. 2. Latin frāter, brother: FRA, FRATERNAL, FRIAR; CONFRERE, FRATRICIDE. 3. Greek phratēr ... \"\n            \"4. Sanskrit bhrātā, bhrātar-, brother: PAL. [Pok. bhrāter- 163.]\\\"\")\nAHD_BHER4 = (\"AHD_watkins1985.txt:335 \\\"bher-4. To cook, bake. Extended root form *bhrig- in Latin frigere, to roast, fry: \"\n             \"FRY. [Pok. 6. bher- 137.]\\\"\")\nHRN45 = (\"HRN.txt:2091 (form-feed leaf 66 = printed p. 45; the '— 45 —' header stands at line 2080): \"\n         \"\\\"192. birāder ,Bruder'. ap. brātar ,Bruder'; aw. brātar; phlv. brātar, brāt; ai. bhrātar-; \"\n         \"arm. ełbair ... bal. brāt, brās\\\"\")\nHRN47 = (\"HRN.txt leaf 68 = printed p. 47: \\\"201. birišten ,braten', vergl. berīzen, birezen ,Backofen', biryān, \"\n         \"beryān (AM.). ai. √bhrajj, bhṛjjáti ,rösten'; phlv. bristan ,rösten', brejam (PPGl.), \"\n         \"bristak (Vd. 5, 134 Gl.), brejan (AV.) ... bal. brijag, brejag ,backen, rösten'\\\"; footnote: \"\n         \"\\\"Phlv. vrejan ist nur fehlerhafte Schreibung\\\"\")\nSOD107 = (\"SOD_pages.txt:11524 (form-feed leaf 172, printed ≈ p. 106-107): \\\"2704 prʾt B, M, S — βrāt \"\n          \"(prʾt, brʾt, prʾtr) ← brātar ... brother ... GMS 307, 940; BBB 540; ... \"\n          \"βrʾtət 'brothers'\\\"; and \\\"2705 brʾt C ⇒ prʾt\\\"\")\nIEC19 = (\"IEC.txt:496 (leaf 26; the running number '19' stands at line 492): \\\"ambhor-, ambhr- (for ambh-bhor, -bhr-, \"\n         \"cf. ambhō and bher-, bhor-) 'two-handled vessel'. Skt. ambhr̥naḥ; Per. ambar; Myc. and Gk. amphoreus, \"\n         \"amphiphoreus; LW in Lat. amphora; OHG ampri; OE amber, embren ...\\\"\")\nBQT269 = (\"BQT_v1_pages.txt form-feed leaf 490 (footer of leaf 476 prints '۲۵۵' ⇒ leaf = printed + 221, \"\n          \"so leaf 490 = printed p. 269): \\\"بریجن ... با جیم بر وزن \"\n          \"رسیدن ، تنوری باشد که در آن \"\n          \"کماج و نان سنگک پزند ، و \"\n          \"[در] عربی فرن گویند\\\" with Moʾin's footnote \"\n          \"\\\"بریجن ، پهلوی ... ایرانی \"\n          \"باستان *braij (پختن ، برشتن) \"\n          \"«اسفا ۱: ۲»\\\" (اسفا = AEF, Khāleqi Motlaq's Persian Horn)\")\nFFD37 = (\"incoming/FFD/FFD_pages.txt, leaf tagged [pdf page 41] = printed p. 37: \"\n         \"\\\"برشتن / برشت < فارسی میانه \"\n         \"brištan < ایرانی باستان *braij-\\\"; the same page has \"\n         \"\\\"بردن / برد < فارسی میانه burdan < \"\n         \"ایرانی باستان *bar-\\\"\")\nSNS103 = (\"SNS_pages.txt:16192 and :16391 (index): \\\"gōšt ī brištag 103/2\\\", \\\"brištag 103/16\\\"; \"\n          \"the glossary body at line 4757 reads \\\"gōšt ī brištag\\\" — so p. 103 of Tavoosi's \"\n          \"Šāyast nē Šāyast glossary does carry brištag 'roasted'\")\nKLN203 = (\"KLN_1966.txt:5661-5725, between the page markers '203' (line 5703) and '204' (line 5727): \"\n          \"\\\"bring, tr. v. — ME. bringen, fr. OE. bringan, rel. to ... Goth. briggan, fr. Teut. base *bhrenk-\\\"; \"\n          \"\\\"brother, n. — ME., fr. OE. brōdor, rel. to OS. brothar, ON. bródir, ... Goth. broþar, and cogn. with \"\n          \"OI. bhrātar-, Avestic brātar-, ... L. frāter\\\"\")\nKLN_BEAR = (\"KLN_1966.txt:4608 \\\"bear, tr. and intr. v., to carry. — ME. beren, fr. OE. beran, rel. to ON. bera, ... \"\n            \"fr. I.-E. base *bher-, whence also OI. bhárati, 'bears', ... Gk. φέρειν, 'to bear, carry', \"\n            \"L. ferre, 'to bear, carry' ... Cp. bairn, ... bier, birth, ... burden, 'load' ... Cp. also ... defer, deference, differ, \"\n            \"... fertile, ... offer, ... phosphorous, phosphorus, prefer, ... refer, ... suffer, transfer\\\"\")\nKLN_PHOS = (\"KLN_1971.txt:181197 \\\"phosphorus, n. — ModL. phosphorus, 'phosphorus', fr. L. Phosphorus, 'the morning star', \"\n            \"fr. Gk. φωσφόρος, 'light-bringer; the morning star', which is compounded of \"\n            \"φῶς, 'light', contr. of φάος, and -φόρος, 'carrying'. \"\n            \"The first element derives fr. I.-E. base *bhā-, 'to shine'\\\"\")\nSYN107 = (\"SYN.txt:2908 (Buck p. 107, §2.44 BROTHER): \\\"Grk. ἀδελφός ... Lat. frāter ... \"\n          \"Goth. broþar, ON bróðir ... OE brōdor, ME brother, NE brother ... Skt. bhrātar-, Av. brātar-\\\"\")\nWLD_BHER = (\"incoming/WLD/WLD_Bd2_pages.txt:10193 (WP II 153-156, the running head 'bher' with '156' at line 10190): \"\n            \"\\\"Got. bairan ,tragen, bringen, hervorbringen, gebären' ..., aisl. bera ..., ahd. beran ..., ags. beran \"\n            \",tragen, gebären'; got. aisl. ahd. as. barn, ags. bearn ,Kind'\\\"; and (line 10150) Lat. \\\"-fer in Zs. \"\n            \",tragend, bringend' ... fortuna\\\"\")\nWLD_BRAT = (\"incoming/WLD/WLD_Bd2_pages.txt:12653 (WP II 193): \\\"Ai. bhrātar-, av. ap. brātar- ,Bruder'; \"\n            \"arm. ełbair, gen. ełbaur ds.\\\" ... \\\"ags. brŋþor ,Bruder'; apr. brote, brati ,Bruder'\\\"\")\nBRT_OP = (\"BRT.txt:16961 s.v. \\\"p. bardiya- m. EN. eines Persers, Bruders des Kambyses, Smerdis: avahyā \"\n          \"kambūjiyahyā brātā ... nāma āha 'jener K. hatte einen Bruder, B. mit Namen' Bh. I 10\\\" \"\n          \"— Bartholomae lemmatises Old Persian brātar-/brātā 'Bruder' from the Behistun text\")\nHUB_BRAD = (\"HUB.txt:6060 \\\"d) Einschub von i in: birādar ,Bruder' = ap. brātar-\\\"; HUB.txt:6684 \"\n            \"\\\"pitar-; birādar = birādar ,Bruder', ap. brātar-; mādar\\\"\")\nPHD_BRISH = (\"PHD.txt:292 \\\"brištan, brēz- [blystn', blyc- | M bryz-, N biristan] roast\\\" — MacKenzie has the verb \"\n             \"brištan / pres. stem brēz-, not the by-forms brištag / brējan\")\nPHD_BURDAN = (\"PHD.txt:292 \\\"burdan, bar- [YBLWN-tn' ...; bwltn', bl- | M bārag, br-, N ˜] carry, bear, take, endure\\\" \"\n              \"and \\\"bur-dār [bwlt'l] bearer\\\" — the Middle Persian continuation of Old Persian bar-\")\nEM_FRATER = (\"LAT.txt:24017-24050 (Ernout-Meillet p. 448): \\\"frāter, -tris m.: 1° frère par le sang ... \"\n             \"L'un des grands noms de parenté indo-européens ... Le mot se retrouve dans osq. fratrum, ombr. frater \"\n             \"'fratres', irl. brathir, got. broþar, arm. ełbayr, skr. bhrātā (thème bhrātar-)\\\"\")\nEM_FRIGO = (\"LAT.txt:24230-24249 (Ernout-Meillet p. 451-453): \\\"frīgō, -is, -xī, -ctum, -ere: rôtir, griller, frire. \"\n            \"Le sens spécial de 'frire' est secondaire. Le sens premier est 'faire sécher par la cuisson, cuire à sec' ... \"\n            \"on trouve ailleurs, au même sens, des mots semblables, mais différents: gr. φρύγω \"\n            \"'je fais griller', skr. bhrjyáti 'il fait griller'\\\"\")\nMON_ANBOR = (\"Moʾin's lexicon via abadis.ir: \\\"انبر: آلت فلزی \"\n             \"دوشاخه که با آن آتش یا \"\n             \"چیز دیگر را برگیرند\\\" — \"\n             \"the definition matches Nourai's gloss ('tool for carrying hot objects') but Moʾin gives NO origin tag\")\nMON_FOSFOR = (\"Moʾin's lexicon via abadis.ir: \\\"فسفر (فُ فُ) [ فر. ] \"\n              \"(اِ.) عنصری است جامد ...\\\" — \"\n              \"[فر.] = فرانسه, i.e. Moʾin tags the word as a French loan; \"\n              \"MON_part2.txt:7342-7363 has the same article plus فسفات immediately before it\")\n\nentries = []\n\n# ---------------- ENTRY 0 ----------------\nnodes0 = []\n\nnodes0.append({\n \"id\": 1, \"lang\": \"Old Persian\", \"words\": \"bar\", \"verdict\": \"confirmed\",\n \"derivation\": \"Old Persian bar- 'to bear, carry' is well attested: 3 pl. bara⁺tiy 'they bear' (DB 5.22, DNa 42), impf. abaram/abara, imv. baratuv, inf. bartanaiy, pass. abariya (DSf). It continues PIE *bʰer-e/o- exactly as Skt. bhárati, Av. baraiti, Gk. phérō, Lat. ferō, Goth. bairþ. The second gloss 'ride a horse' is not a separate verb but the specialised Iranian use that Pokorny records for Avestan ('av. baraiti ds. und ,reiten‘') and that surfaces in the OP vr̥ddhi compounds asa-bāra- 'horse-borne' and uša-bāri- 'camel-borne' (Kent §122, §126), whence MP aswār > NP سوار savār. Nourai's box is therefore right, though 'ride' belongs to the derived bāra- stem rather than to bar- itself.\",\n \"derivation_fa\": \"پارسی باستان bar- «بردن، حمل کردن» در کتیبه‌های هخامنشی گواه دارد (barantiy «می‌برند»، abaram «بردم») و دنبالهٔ راستین ریشهٔ هندواروپایی آغازین *bʰer- است؛ هم‌ریشه با سنسکریت bhárati، اوستایی baraiti و لاتین ferō. معنای دوم که نورایی می‌آورد («سواری کردن») فعل جداگانه‌ای نیست، بلکه همان کاربرد ویژهٔ ایرانی است که در ترکیب asa-bāra- «اسب‌برده، سوار» دیده می‌شود و در فارسی نو به «سوار» رسیده است. ادعای نورایی درست است، تنها معنای دوم به ستاک مشتق bāra- بازمی‌گردد نه به خود bar-.\",\n \"sources\": [PIE_BHER],\n \"ref_check\": [{\"ref\": \"POK:128\", \"status\": \"supports\", \"note\": POK128}],\n \"consulted\": [\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon pp. 200-201 (KNT.txt leaf NR=224/225)\", \"stance\": \"supports\", \"note\": KNT200},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. bher-1 (AHD_watkins1985.txt:333)\", \"stance\": \"supports\", \"note\": AHD_BHER1},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 153-156 (WLD_Bd2_pages.txt:10150-10195)\", \"stance\": \"supports\", \"note\": WLD_BHER},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p. 19 s.v. burdan (PHD.txt:292)\", \"stance\": \"supports\", \"note\": PHD_BURDAN},\n ]})\n\nnodes0.append({\n \"id\": 2, \"lang\": \"Old Persian\", \"words\": \"â-bar; pati-â-bar; parâ-bar; pari-bar; fra-bar\", \"verdict\": \"confirmed\",\n \"derivation\": \"All five prefixed compounds are Kent's own list on the very page Nourai cites: ā + bar- 'perform' (ābaratiy, DNb 25); pati- + ā + bar- 'bring back, restore' (patiyābaram, DB 1.68 — a rare OP double prefix, Kent §379); parā + bar- 'bear away, take away' (parābara DB 1.71, 96; parābartam DB 1.62); pari- + bar- 'protect, preserve' (paribarāmiy DNb 17, paribarā DB 4.72, 88); fra- + bar- 'proffer, grant' (frābara, the standard Achaemenid formula '(Ahuramazdā) granted me this kingdom'). Phonetically pati-ā- contracts to patiyā- and para+ā to parā-, and pari- keeps its -i- before a consonant (Kent §1678). The Persian continuations Nourai cross-references (پروردن < pari-bar-, فراوردن/آوردن < ā-bar-) are the regular MP-NP outcomes.\",\n \"derivation_fa\": \"هر پنج فعل پیشونددار در همان صفحهٔ ۲۰۰ واژه‌نامهٔ کنت آمده‌اند: ā-bar- «انجام دادن»، patiy-ā-bar- «بازگرداندن» (در بیستون ۱/۶۸)، parā-bar- «بردن، ربودن»، pari-bar- «پاسداشتن، پروردن» و fra-bar- «بخشیدن، ارزانی داشتن». در فارسی میانه و نو همین ترکیب‌ها به «پروردن» (< pari-bar-) و «آوردن/فراوردن» (< ā-bar-) رسیده‌اند. ادعای نورایی درست است و عیناً با مرجعی که خود آورده می‌خواند.\",\n \"sources\": [PIE_BHER],\n \"ref_check\": [{\"ref\": \"KNT:200\", \"status\": \"supports\", \"note\": KNT200}],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW p. 128 (POK_01.txt:1800ff.)\", \"stance\": \"supports\", \"note\": POK128},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. bher-1 (AHD_watkins1985.txt:333)\", \"stance\": \"partial\", \"note\": \"Watkins lists the root and its Germanic/Latin/Greek reflexes but no Old Persian preverb compounds; \" + AHD_BHER1},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p. 19 (PHD.txt:292)\", \"stance\": \"supports\", \"note\": PHD_BURDAN},\n ]})\n\nnodes0.append({\n \"id\": 3, \"lang\": \"Greek\", \"words\": \"pherein; phôs-phoros\", \"verdict\": \"confirmed\",\n \"derivation\": \"Gk. φέρειν (phérein) 'to carry' is the direct thematic continuation of PIE *bʰér-e-ti, the same present as Skt. bhárati and Lat. ferō. φωσφόρος (phōsphóros) 'light-bearing, the morning star' is a possessive compound of φῶς (< *φάος, from PIE *bʰeh₂- 'to shine' — hence Nourai's cross-reference to his root Bhâ 1) and the -φόρος agent element of φέρω. So the node is right on both counts: only the second element belongs to Bher, the first to Bhā.\",\n \"derivation_fa\": \"یونانی باستان phérein «بردن، حمل کردن» دنبالهٔ مستقیم *bʰér-e-ti است، همان ساختی که در سنسکریت bhárati و لاتین ferō دیده می‌شود. phōsphóros «نورآور، ستارهٔ صبح» ترکیبی است از phōs «روشنایی» (از ریشهٔ *bʰeh₂- «درخشیدن») و -phoros «برنده». پس ارجاع نورایی که جزء نخست را به ریشهٔ Bhā می‌فرستد درست است؛ پژوهش امروزی هم همین را می‌گوید.\",\n \"sources\": [PIE_BHER, ETY_PHOS],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": AHD_BHER1 + \" — §8 is exactly 'Greek pherein, to carry: -PHORE, -PHORESIS, -PHOROUS; AMPHORA, ANAPHORA, ... METAPHOR, PERIPHERY, PHEROMONE'\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. phosphorus (KLN_1971.txt:181197)\", \"stance\": \"supports\", \"note\": KLN_PHOS},\n   {\"src\": \"POK\", \"where\": \"IEW p. 128 (POK_01.txt:1800ff.)\", \"stance\": \"supports\", \"note\": POK128},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 153ff.\", \"stance\": \"supports\", \"note\": WLD_BHER},\n ]})\n\nnodes0.append({\n \"id\": 4, \"lang\": \"French\", \"words\": \"phosphore\", \"verdict\": \"confirmed\",\n \"derivation\": \"French phosphore is the 18th-century learned formation on Modern Latin phosphorus, the name given to the substance Hennig Brand isolated from urine at Hamburg in 1669 because it glowed in the dark; Lavoisier proved it an element in 1777, and by then phosphore was the settled French chemical term (Etymonline: 'phosphate (1795), from French phosphate, from phosphore'). The word therefore reaches French through Latin rather than straight from Greek, but the Greek etymon in Nourai's box is right.\",\n \"derivation_fa\": \"واژهٔ فرانسوی phosphore ساختهٔ عالمانهٔ سدهٔ هجدهم میلادی بر پایهٔ لاتین علمی phosphorus است؛ نامی که پس از کشف این عنصر به دست هنیگ براند در هامبورگ (۱۶۶۹ م.) بر آن نهادند، زیرا در تاریکی می‌درخشید. پس این پیوند درست است، اگرچه واسطهٔ لاتین در نمودار نیامده است.\",\n \"sources\": [ETY_PHOS],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"The Watkins appendix (AHD_watkins1985.txt:333) files PHOSPHORUS under bher-1 §8 (Greek pherein) but says nothing about a French stage; the New College Edition main entry (AHD p. 986) is not in the local library.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. phosphorus and phosphorize (KLN_1971.txt:181180-181197)\", \"stance\": \"partial\", \"note\": \"Klein derives the English word from ModL./L./Gk. and mentions French only for the derivative: 'phosphorize, tr. v. — F. phosphoriser, fr. phosphore'; \" + KLN_PHOS},\n   {\"src\": \"WEB\", \"where\": \"Etymonline s.v. phosphorus (used as the modern English-dictionary check)\", \"stance\": \"supports\", \"note\": \"'phosphate (1795), from French phosphate, from phosphore' — confirms French phosphore as the source of the international chemical vocabulary.\"},\n ]})\n\nnodes0.append({\n \"id\": 5, \"lang\": \"Persian\", \"words\": \"fosfor «فسفر»; (extra) فسفات\", \"verdict\": \"confirmed\",\n \"derivation\": \"NP فسفر fosfor is a 19th/20th-century loan from French phosphore, taken in with the rest of the Dār al-Fonūn chemical vocabulary; French /f/ is written ف, the final -e is dropped and the word is re-stressed fosfór. Moʾin's dictionary marks it [فر.] '(from) French', which is exactly Nourai's arrow. The companion form فسفات fosfāt is likewise from French phosphate (itself phosphore + -ate, 1795), and stands immediately before فسفر in Moʾin.\",\n \"derivation_fa\": \"«فسفر» وام‌واژه‌ای است از فرانسوی phosphore که در دورهٔ دارالفنون همراه دیگر اصطلاحات شیمی به فارسی راه یافت؛ هٔ پایانی فرانسه افتاده و تکیه بر هجای پایانی نشسته است. معین در فرهنگ خود آن را با نشانهٔ [فر.] یعنی فرانسه می‌آورد و همین ادعای نورایی است. «فسفات» نیز از فرانسوی phosphate است. ادعای نورایی درست است.\",\n \"sources\": [AB_FOSFOR, ETY_PHOS],\n \"ref_check\": [{\"ref\": \"MON:2546\", \"status\": \"supports\", \"note\": MON_FOSFOR}],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Moʾin, Farhang-e Fārsi s.v. فسفر (MON_part2.txt:7342-7363; abadis.ir)\", \"stance\": \"supports\", \"note\": MON_FOSFOR},\n   {\"src\": \"WEB\", \"where\": \"Etymonline s.v. phosphorus / phosphate\", \"stance\": \"supports\", \"note\": \"'phosphate (1795), from French phosphate, from phosphore' — the French form is the donor for the modern international chemical terms.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qateʾ (17th c.) — grep of BQT_v1/v2_pages.txt for فسفر\", \"stance\": \"silent\", \"note\": \"No entry, as expected for a modern chemical loan; the word post-dates Borhan by two centuries.\"},\n ]})\n\nnodes0.append({\n \"id\": 6, \"lang\": \"English\", \"words\": \"phosphor\", \"verdict\": \"disputed\",\n \"derivation\": \"The word itself belongs to this root, but the arrow as drawn is wrong. English phosphor is first recorded in the 1630s meaning 'the morning star, Lucifer', taken straight from Latin Phosphorus < Gk. φωσφόρος, and its sense 'anything phosphorescent' is 1705; the chemical name phosphorus is Modern Latin of the 1670s. All of this is earlier than, and independent of, French phosphore. Klein: 'phosphorus, n. — ModL. phosphorus, fr. L. Phosphorus, ... fr. Gk. φωσφόρος' — no French link; Etymonline agrees. French is the immediate source of Persian فسفر (node #5) but not of the English word, so the branch French > English should be Latin/Greek > English. The ultimate etymology in Nourai's chart is nonetheless correct.\",\n \"derivation_fa\": \"خود واژه به همین ریشه می‌رسد، اما مسیری که نورایی کشیده نادرست است. phosphor در انگلیسی از دههٔ ۱۶۳۰ م. به معنای «ستارهٔ صبح» گواه دارد و مستقیماً از لاتین Phosphorus (و آن از یونانی phōsphóros) گرفته شده، یعنی پیش از آنکه فرانسه phosphore را بسازد. کلاین و اتیمآنلاین هر دو هیچ واسطهٔ فرانسوی برای واژهٔ انگلیسی قائل نیستند. پس پژوهش امروزی این پیکان را رد می‌کند، اگرچه خاستگاه نهایی (یونانی) درست است.\",\n \"sources\": [ETY_PHOS],\n \"ref_check\": [{\"ref\": \"AHD:986\", \"status\": \"not_checked\", \"note\": \"AHD:986 is a page of the New College Edition main dictionary (1975/76), which is not in the local library; only the Watkins Indo-European appendix is available locally (AHD_watkins1985.txt), and it lists PHOSPHORUS under bher-1 without any French stage.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. phosphorus (KLN_1971.txt:181197)\", \"stance\": \"contradicts\", \"note\": KLN_PHOS + \" — no French intermediary.\"},\n   {\"src\": \"WEB\", \"where\": \"Etymonline s.v. phosphorus/phosphor\", \"stance\": \"contradicts\", \"note\": \"'Phosphor ... 1630s, \\\"the morning star, Lucifer,\\\" from Latin phosphorus'; by 1705 'anything phosphorescent'. Latin, not French, is the donor.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. bher-1 (AHD_watkins1985.txt:333)\", \"stance\": \"partial\", \"note\": AHD_BHER1},\n ]})\n\nnodes0.append({\n \"id\": 7, \"lang\": \"Avestan\", \"words\": \"brâtar\", \"verdict\": \"confirmed\",\n \"derivation\": \"Av. brātar- 'brother' (also Old Persian brātar-/nom. brātā, e.g. Bh. I 10 of Smerdis) is the regular Iranian outcome of PIE *bʰréh₂tēr via Proto-Indo-Iranian *bʰráHtā: the laryngeal is lost with compensatory lengthening in the open syllable (*bʰreh₂- > brā-) and PIE *bʰ is deaspirated to b in Iranian, while Indic keeps bh- (Skt. bhrātar-). Pokorny p. 163 heads the article 'bhrāter- ,Angehöriger der Großfamilie, Bruder, Blutsverwandter‘' and cites 'ai. bhrātar-, av. apers. brātar-' first; Klein s.v. brother has 'Avestic brātar-'. Both of Nourai's citations therefore hit.\",\n \"derivation_fa\": \"اوستایی brātar- (و همچنین پارسی باستان brātar-/brātā در بیستون) بازماندهٔ قاعده‌مند هندواروپایی آغازین *bʰréh₂tēr است: حنجره‌ای (laryngeal) افتاده و واکه کشیده شده (*bʰreh₂- > brā-)، و *bʰ دمیدهٔ هندواروپایی در ایرانی به b ساده بدل شده در حالی که سنسکریت bhrātar- را نگاه داشته است. پوکورنی (ص ۱۶۳) و کلاین هر دو همین را می‌گویند؛ ادعای نورایی درست است.\",\n \"sources\": [PIE_BRAT, WK_BARADAR],\n \"ref_check\": [\n   {\"ref\": \"POK:163\", \"status\": \"supports\", \"note\": POK163},\n   {\"ref\": \"KLN:204\", \"status\": \"supports\", \"note\": KLN203 + \" — the 'brother' article sits between Klein's page markers 203 and 204, and explicitly cites 'Avestic brātar-'.\"},\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Bartholomae, Altiranisches Wörterbuch (BRT.txt:16961)\", \"stance\": \"supports\", \"note\": BRT_OP},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 193 (WLD_Bd2_pages.txt:12653)\", \"stance\": \"supports\", \"note\": WLD_BRAT},\n   {\"src\": \"SYN\", \"where\": \"Buck p. 107 §2.44 (SYN.txt:2908)\", \"stance\": \"supports\", \"note\": SYN107},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. bhrater- (AHD_watkins1985.txt:342)\", \"stance\": \"supports\", \"note\": AHD_BRAT},\n ]})\n\nnodes0.append({\n \"id\": 8, \"lang\": \"Persian\", \"words\": \"barâdar «برادر»\", \"verdict\": \"confirmed\",\n \"derivation\": \"NP برادر barādar/birādar comes not from Avestan specifically but from the common Old Iranian brātar- (Nourai's 'Avestan' box stands for Old Iranian throughout the book), through Middle Persian brād/brādar [blāt, blātl]: intervocalic -t- is voiced to -d- in Middle Persian (brātar > brādar), and the initial cluster br- is broken by an anaptyctic vowel in New Persian, which is precisely Hübschmann's point ('Einschub von i in: birādar „Bruder“ = ap. brātar-'). Horn no. 192, on exactly the page Nourai cites, sets out the whole series 'np. birāder : ap. brātar, aw. brātar, phlv. brātar, brāt, ai. bhrātar-'.\",\n \"derivation_fa\": \"«برادر» از فارسی میانهٔ brādar / brād است، و آن از ایرانی باستان brātar- (اوستایی و پارسی باستان یکسان). دو دگرگونی آوایی در کار است: ت میان‌واکه‌ای در فارسی میانه به د نرم شده (brātar > brādar)، و خوشهٔ آغازین br- در فارسی نو با واکهٔ میانجی شکسته شده است — همان که هوبشمان «افزودن i» می‌نامد. هرن در شمارهٔ ۱۹۲ صفحهٔ ۴۵ — دقیقاً همان صفحه‌ای که نورایی می‌دهد — همین زنجیره را می‌آورد. ادعای نورایی درست است.\",\n \"sources\": [WK_BARADAR, PIE_BRAT],\n \"ref_check\": [{\"ref\": \"HRN:45\", \"status\": \"supports\", \"note\": HRN45}],\n \"consulted\": [\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien (HUB.txt:6060, :6684)\", \"stance\": \"supports\", \"note\": HUB_BRAD},\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qateʾ, grep of BQT_v1_pages.txt for برادر\", \"stance\": \"silent\", \"note\": \"The word is glossed in Borhan but Moʾin attaches no etymological footnote to it in the OCR available here; no contradiction.\"},\n   {\"src\": \"MON\", \"where\": \"Moʾin s.v. برادر\", \"stance\": \"supports\", \"note\": \"Moʾin marks the word [په.] (Pahlavi), i.e. an inherited Iranian word, not a loan — consistent with the chart.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck p. 107 §2.44 (SYN.txt:2908)\", \"stance\": \"supports\", \"note\": SYN107},\n ]})\n\nnodes0.append({\n \"id\": 9, \"lang\": \"Sogdian\", \"words\": \"br`t\", \"verdict\": \"confirmed\",\n \"derivation\": \"Sogdian βrāt 'brother', written prʾt in the Manichaean and Buddhist scripts and brʾt in the Christian (Syriac) script, is Gharib no. 2704, which itself derives it '← brātar': the Old Iranian -tar stem lost its final syllable, and Old Iranian intervocalic -t- gave Sogdian -t- written with the Aramaic taw. Nourai's 'br`t' is the Christian-Sogdian spelling (Gharib no. 2705 'brʾt C ⇒ prʾt'); the oblique plural βrʾtət and the by-form prʾtr are also listed. Entry 2704 stands on printed p. 106-107, which is Nourai's SOD:107.\",\n \"derivation_fa\": \"سغدی βrāt «برادر» که در خط مانوی و بودایی prʾt و در خط سریانی/مسیحی brʾt نوشته می‌شود، در فرهنگ سغدی بدرالزمان قریب (مدخل ۲۷۰۴) صریحاً از brātar گرفته شده است؛ پسوند خویشاوندی -tar در سغدی افتاده است. مدخل ۲۷۰۴ بر صفحهٔ ۱۰۶–۱۰۷ چاپی است که همان ارجاع نورایی است. ادعای نورایی درست است.\",\n \"sources\": [PIE_BRAT],\n \"ref_check\": [{\"ref\": \"SOD:107\", \"status\": \"supports\", \"note\": SOD107}],\n \"consulted\": [\n   {\"src\": \"SOD\", \"where\": \"Gharib, Sogdian Dictionary nos. 2704-2707, 5870-5871, 9929 (SOD_pages.txt:11524ff.)\", \"stance\": \"supports\", \"note\": SOD107 + \"; the compounds nβrʾty 'nephew' (no. 5870-5871) and wβrʾt (no. 9929) are cross-referenced to the same lemma.\"},\n   {\"src\": \"POK\", \"where\": \"IEW p. 163 (POK_01.txt:2352)\", \"stance\": \"supports\", \"note\": POK163},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 193\", \"stance\": \"supports\", \"note\": WLD_BRAT},\n ]})\n\nnodes0.append({\n \"id\": 10, \"lang\": \"Germanic\", \"words\": \"beran, burthiz, bur, brengan; brôthar\", \"verdict\": \"confirmed\",\n \"derivation\": \"Every form is Watkins's own Germanic reconstruction under bher-1: *beran (OE beran 'to carry'), *burthinja/*burthiz (OE byrthen 'burden', ON burdhr 'birth'), *burja- (ON byrr 'favourable wind', Nourai's 'bur'), and the compound root *bʰrenk- (< *bʰer- + *h₁nekʷ- 'to reach') > Gmc *brengan, OE bringan. PGmc *brōthar- 'brother' belongs to the separate root bhrater- and shows Grimm's Law twice over (*bʰ- > b-, *-t- > -þ-) plus Verner voicing in the medial consonant of OE brōdor. Klein's articles 'bring' and 'brother' stand on the page Nourai cites.\",\n \"derivation_fa\": \"همهٔ صورت‌های این خانه بازساختهٔ واتکینز ذیل bher-1 هستند: ژرمنی آغازین *beraną «بردن»، *burthiz «زادن، بار»، *burja- و ریشهٔ مرکب *bʰrenk- (= *bʰer- + *h₁nekʷ- «رسیدن») که به brengan/bring رسیده است. اما brōthar «برادر» به ریشهٔ جداگانهٔ *bʰréh₂tēr می‌رسد و دو بار قانون گریم در آن عمل کرده است (*bʰ > b، *t > þ). ادعای نورایی درست است.\",\n \"sources\": [PIE_BHER, PIE_BRAT],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": AHD_BHER1 + \" ; \" + AHD_BRAT},\n   {\"ref\": \"KLN:203\", \"status\": \"supports\", \"note\": KLN203},\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 pp. 203-204 (KLN_1966.txt:5661, :5725) and s.v. bear (KLN_1966.txt:4608)\", \"stance\": \"supports\", \"note\": KLN_BEAR},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 153-156 and II 193 (WLD_Bd2_pages.txt:10193, :12653)\", \"stance\": \"supports\", \"note\": WLD_BHER + \" ; \" + WLD_BRAT},\n   {\"src\": \"SYN\", \"where\": \"Buck p. 107 §2.44 (SYN.txt:2908)\", \"stance\": \"supports\", \"note\": SYN107},\n ]})\n\nnodes0.append({\n \"id\": 11, \"lang\": \"English\", \"words\": \"bear 1, birth, burden, bring; brother\", \"verdict\": \"confirmed\",\n \"derivation\": \"OE beran > ME beren > NE bear (the verb, distinct from bear the animal, which is bher-3 'brown'); ON burdhr borrowed into northern ME as birthe > birth (replacing OE gebyrd); OE byrthen > burden with the regular ME -then > -den; OE bringan > bring, with the irregular preterite brought from *branht-. OE brōdor > ME brother > NE brother, with the -ð- of Old English spelt -th-. Every one of these is Watkins's list under bher-1 and bhrater-; Klein s.v. bear cross-refers to 'bairn, ... bier, birth, ... burden, ‚load‘'.\",\n \"derivation_fa\": \"انگلیسی کهن beran > bear، byrthen > burden، bringan > bring، و birth که وام‌گرفته از نوردیک کهن burðr است و جای واژهٔ انگلیسی کهن gebyrd را گرفته است؛ brother نیز از brōdor. باید توجه داشت که bear «خرس» به این ریشه ربطی ندارد و از *bʰer- «قهوه‌ای» است؛ نورایی هم با نوشتن «bear 1» همین تمایز را رعایت کرده است. ادعای نورایی درست است.\",\n \"sources\": [PIE_BHER, PIE_BRAT],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference of its own; it inherits AHD/KLN:203 from its parent (#10), and both were checked there.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. bear (4608), bring (5661), brother (5725)\", \"stance\": \"supports\", \"note\": KLN_BEAR},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. bher-1 and bhrater-\", \"stance\": \"supports\", \"note\": AHD_BHER1 + \" ; \" + AHD_BRAT},\n   {\"src\": \"SYN\", \"where\": \"Buck p. 107 §2.44\", \"stance\": \"supports\", \"note\": SYN107},\n ]})\n\nnodes0.append({\n \"id\": 12, \"lang\": \"Latin\", \"words\": \"ferre; frater\", \"verdict\": \"confirmed\",\n \"derivation\": \"Lat. ferō, ferre 'to carry' is the athematic/thematic present of *bʰer-, with the regular Italic change of word-initial *bʰ to f- (contrast Greek ph- and Germanic b-); its suppletive perfect tulī and participle lātus come from a different root (*telh₂-). Lat. frāter 'brother' shows the same *bʰ > f and continues *bʰréh₂tēr with the Italic shortening of the vowel before r (cf. Osc. fratrum, Umbr. frater). Ernout-Meillet call frāter 'l'un des grands noms de parenté indo-européens' and list irl. brathir, got. broþar, skr. bhrātā as its cognates — the same set as the chart.\",\n \"derivation_fa\": \"لاتین ferō/ferre «بردن» و frāter «برادر» هر دو دگرگونی ویژهٔ ایتالیک را نشان می‌دهند: *bʰ آغازین هندواروپایی در لاتین به f بدل می‌شود (در یونانی ph و در ژرمنی b). گذشتهٔ tulī و صفت مفعولی lātus از ریشه‌ای دیگر (*telh₂-) آمده‌اند. ارنو-میه frāter را از «نام‌های بزرگ خویشاوندی هندواروپایی» می‌داند. ادعای نورایی درست است.\",\n \"sources\": [PIE_BHER, PIE_BRAT],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": AHD_BHER1 + \" ; \" + AHD_BRAT}],\n \"consulted\": [\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet p. 448 s.v. frāter (LAT.txt:24017-24050)\", \"stance\": \"supports\", \"note\": EM_FRATER},\n   {\"src\": \"POK\", \"where\": \"IEW pp. 128, 163\", \"stance\": \"supports\", \"note\": POK128 + \" ; \" + POK163},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 153ff., 193\", \"stance\": \"supports\", \"note\": WLD_BHER + \" ; \" + WLD_BRAT},\n ]})\n\nnodes0.append({\n \"id\": 13, \"lang\": \"English\", \"words\": \"defer, differ, fertile, offer, prefer, refer, suffer, transfer; fraternity\", \"verdict\": \"confirmed\",\n \"derivation\": \"All eight verbs are Latin preverb + ferre borrowed into English through Old French or directly from Latin: dē-ferō > deferre 'carry away, submit', dis-ferō > differre 'carry apart', ob-ferō > offerre 'bring before', prae-ferō, re-ferō, sub-ferō > sufferre, trāns-ferō; fertile is L. fertilis 'bearing (crops)', an -ilis adjective on the same stem. Fraternity is ME fraternite < OF fraternité < L. frāternitātem, from frāternus, so it hangs on frater, not on ferre. Watkins lists exactly this set under bher-1 §5 and FRATERNAL under bhrater- §2.\",\n \"derivation_fa\": \"هشت فعل نخست همگی ترکیب پیشوند لاتین با ferre هستند که از راه فرانسهٔ کهن یا مستقیماً از لاتین وارد انگلیسی شده‌اند (differre، offerre، referre، sufferre، transferre و مانند آن)، و fertile از لاتین fertilis «بار‌دهنده». اما fraternity از راه frāternitās به frāter می‌رسد نه به ferre؛ نورایی نیز آن را جدا در سطر دوم آورده است. ادعای نورایی درست است.\",\n \"sources\": [PIE_BHER],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference of its own; the parent Latin node cites AHD, which was checked and supports the whole list (AHD_watkins1985.txt:333 §5 and :342 §2).\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. bear (KLN_1966.txt:4608) and fraternity (KLN_1966.txt:15344)\", \"stance\": \"supports\", \"note\": KLN_BEAR + \" ; \\\"fraternity, n. — ME. fraternite, fr. OF. fraternitee, fraternite (F. fraternité), fr. L. frāternitātem, acc. of frāternitās, 'brotherhood', fr. frāternus, 'brotherly'\\\"\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. bher-1 §5, bhrater- §2\", \"stance\": \"supports\", \"note\": AHD_BHER1 + \" ; \" + AHD_BRAT},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet p. 448 s.v. frāter\", \"stance\": \"supports\", \"note\": EM_FRATER},\n ]})\n\nnodes0.append({\n \"id\": 14, \"lang\": \"Indo-European\", \"words\": \"Ambhô-Bhor, Ambhor\", \"verdict\": \"plausible\",\n \"derivation\": \"The reconstruction is genuinely Mann's, on the column Nourai cites: 'ambhor-, ambhr- (for ambh-bhor, -bhr-, cf. ambhō and bher-, bhor-) „two-handled vessel‘'. So the segmentation *ambh(i)- 'on both sides' + the o-grade *bʰor-o- 'carrier' is Mann's, and the Greek witness ἀμφορεύς / ἀμφιφορεύς (> Lat. amphora) is uncontroversial. But two things differ from the chart: Mann's gloss is 'two-handled VESSEL', not 'a two-handled tool for carrying (hot) objects' (Nourai has silently substituted the Persian sense of انبر), and no other authority reconstructs a PIE noun here — Pokorny and Watkins treat ἀμφορεύς as an inner-Greek compound of ἀμφί + φέρω (Watkins files AMPHORA under bher-1 §8, i.e. Greek), and OE amber / OHG ampri are usually taken as loans from Latin amphora rather than as inherited cognates. The node is therefore correctly reported from Mann but rests on a single, minority reconstruction.\",\n \"derivation_fa\": \"این بازساخت واقعاً از آنِ من (Mann) است و در همان ستون ۱۹ آمده: ambhor- از *ambh(i)- «از دو سو» به‌علاوهٔ *bʰor- «برنده». اما دو نکته: نخست آنکه معنای من «ظرف دودسته» است نه «ابزار برداشتن اجسام داغ» (نورایی معنای فارسی «انبر» را جایگزین کرده است)؛ دوم آنکه پوکورنی و واتکینز ἀμφορεύς یونانی را ترکیبی درون‌یونانی می‌دانند و هیچ اسم هندواروپایی بازنمی‌سازند. پس با احتیاط پذیرفتنی است.\",\n \"sources\": [PIE_BHER],\n \"ref_check\": [{\"ref\": \"IEC:19\", \"status\": \"partial\", \"note\": IEC19 + \" — the reconstruction is Mann's, but his gloss is 'two-handled vessel', not Nourai's 'two-handled tool for carrying (hot) objects'.\"}],\n \"consulted\": [\n   {\"src\": \"IEC\", \"where\": \"Mann, IECD col. 19 s.vv. ambhi, ambhō, ambhor- (IEC.txt:490-496)\", \"stance\": \"partial\", \"note\": IEC19},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. bher-1 §8 and the index (AHD_watkins1985.txt:333, :1239)\", \"stance\": \"contradicts\", \"note\": \"'AMPHORA bher-1' in the index and §8 'Greek pherein, to carry: ... AMPHORA' — Watkins derives the word inside Greek from ἀμφί + φέρω and reconstructs no PIE *ambhor-.\"},\n   {\"src\": \"POK\", \"where\": \"IEW pp. 34 (ambhi) and 128 (bher-)\", \"stance\": \"silent\", \"note\": \"Pokorny lists ambhi- and bher- separately and has no compound lemma *ambhi-bhoros; grep of POK_01.txt for 'ambhor' returns nothing.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 153ff.\", \"stance\": \"silent\", \"note\": \"No *ambhor- lemma; the Greek amphoreus is not treated as an inherited compound.\"},\n ]})\n\nnodes0.append({\n \"id\": 15, \"lang\": \"Persian\", \"words\": \"ambor «انبر»; (extra) انبره ، انبردست\", \"verdict\": \"plausible\",\n \"derivation\": \"NP انبر anbor/ambor 'tongs, pliers' (with انبره and the compound انبردست 'pliers') is a real and old Persian word — Dehkhoda and Moʾin define it as 'آلت فلزی دوشاخه که با آن آتش یا چیز دیگر را برگیرند', which is where Nourai's gloss 'tool for carrying hot objects' comes from. The etymology, however, rests entirely on the two words 'Per. ambar' in Mann's article: no other source in the library derives it from *ambhi-bʰor-. Horn, Hübschmann, MacKenzie and Nyberg are silent (no Middle Persian *ambar 'tongs' is attested), Moʾin and Dehkhoda give no origin tag, and Wiktionary offers a quite different (and unsourced) derivation 'from Middle Iranian, from PIE *h₂eḱ- „sharp‘'. The internal Persian analysis that Persian writers usually give — ham- 'together' + -bar from بردن 'to carry' — would still land in this root but as a New Persian compound, not an inherited PIE noun. Formally *ambi-bara- > *ambar > انبر is unobjectionable (haplology of the two labials, n before b written ن but pronounced [m]); the derivation is possible but unproven.\",\n \"derivation_fa\": \"«انبر» واژه‌ای کهن و اصیل فارسی است؛ دهخدا و معین آن را «آلت فلزی دوشاخه که با آن آتش یا چیز دیگر را برگیرند» معنا کرده‌اند. اما ریشه‌شناسی آن تنها بر دو کلمهٔ «Per. ambar» در مدخل من تکیه دارد: هرن، هوبشمان، مکنزی و نیبرگ دربارهٔ آن خاموشند و هیچ صورت فارسی میانه‌ای گواه ندارد؛ معین و دهخدا نیز نشانهٔ خاستگاه نمی‌دهند، و ویکی‌واژه آن را به ریشهٔ دیگری (*h₂eḱ- «تیز») می‌برد. از نظر آوایی *ambi-bara- > *ambar > انبر (با حذف یکی از دو لبی) ممکن است، اما ثابت نیست؛ پس با احتیاط پذیرفتنی است.\",\n \"sources\": [WK_ANBOR, AB_ANBOR],\n \"ref_check\": [{\"ref\": \"IEC:19\", \"status\": \"partial\", \"note\": IEC19 + \" — Mann does cite a Persian reflex ('Per. ambar') in the ambhor- article, so Nourai's citation is accurate; but Mann gives no Iranian intermediate forms and glosses the family 'vessel', not 'tongs'.\"}],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Moʾin s.v. انبر (abadis.ir)\", \"stance\": \"partial\", \"note\": MON_ANBOR},\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qateʾ vol. 1, grep of BQT_v1_pages.txt for انبر\", \"stance\": \"silent\", \"note\": \"Only unrelated hits (دساتیر، زمستان‌بر، اندرون); no انبر headword with an etymological footnote in the OCR available.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss — grep of HRN.txt for 'Zange'\", \"stance\": \"silent\", \"note\": \"Horn's only 'Zange' entry is no. 785 'gāz ‚Zange, Scheere‘' (HRN.txt:7683); he has no article on انبر, so the word is not in his New Persian etymological corpus.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie — grep of PHD.txt for ambar/anbar\", \"stance\": \"silent\", \"note\": \"No Middle Persian *ambar 'tongs'; MacKenzie has only ambar-related entries of other meaning, so there is no attested Middle Iranian ancestor for the chart's arrow.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 61 (LKT.txt:395)\", \"stance\": \"contradicts\", \"note\": \"Lokotsch treats the look-alike انبار 'Speicher' as 'gesprochen āmbār [von āmbāštan ‚anfüllen, anhäufen‘ Horn NpEt S. 26, Nr. 111]' — a different word from انبر 'tongs' and no support for an *ambhi-bher- origin.\"},\n ]})\n\nentries.append({\n \"entry\": 0,\n \"root\": \"Bher 1, Bhrâ-tar\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"PIE *bʰer- 'to bear, carry' (Pokorny 128, Watkins bher-1) and PIE *bʰréh₂tēr 'brother' (Pokorny 163, Watkins bhrater-) — two separate roots in every modern handbook\",\n \"note\": \"Both halves of the box are real and the language label and glosses are right: Pokorny p. 128 has '1. bher- ,tragen, bringen‘ usw. (auch Leibesfrucht tragen; med. ,ferri‘), auch ,aufheben, erheben‘' and p. 163 has 'bhrāter- ,Angehöriger der Großfamilie, Bruder, Blutsverwandter‘'. Buck p. 107 §2.44 and Watkins confirm both. What is Nourai's own and NOT supported is the analytical gloss that ties them together — 'Bhrâ-tar: load carrier (of family)'. No standard authority derives *bʰréh₂tēr from *bʰer-: Pokorny gives them as two independent lemmas 35 pages apart, Watkins gives them two separate root entries, and Wiktionary/Beekes treat *bʰréh₂tēr as an unanalysable primary kinship term of the *-h₂ter class (like *ph₂tēr, *méh₂tēr, *dʰugh₂tēr), with the same suffix as those but no verbal root. Watkins's essay in the appendix (line 155) says only 'Male blood relations were designated as bhrater- (BROTHER), which doubtless extended beyond those with a common father or mother'. The similarity bhrā- : bher- is accidental. Everything below the box is nevertheless correct, because Nourai has drawn the two families side by side rather than one out of the other. Nourai's cross-reference '☞ Ter 3' (the -ter kinship suffix) shows he was aware of the suffix analysis.\",\n \"note_fa\": \"هر دو ریشهٔ داخل کادر واقعی‌اند و برچسب زبانی و معنا درست است: پوکورنی در صفحهٔ ۱۲۸ ریشهٔ *bʰer- «بردن، آوردن» و در صفحهٔ ۱۶۳ ریشهٔ *bʰrāter- «برادر، خویشاوند نزدیک» را جداگانه آورده است. آنچه از آنِ نورایی است و پشتیبانی ندارد، تفسیر «برادر = باربرِ خانواده» است؛ هیچ مرجع معتبری *bʰréh₂tēr را از *bʰer- نمی‌گیرد. ریشه‌شناسی امروزی «برادر» را واژه‌ای بنیادین از خانوادهٔ نام‌های خویشاوندی با پسوند *-h₂ter (مانند پدر، مادر، دختر) می‌داند که ستاک فعلی قابل تجزیه‌ای ندارد؛ شباهت bhrā- با bher- تصادفی است. با این همه، چون نورایی دو خانواده را در کنار هم و نه یکی از دلِ دیگری رسم کرده، همهٔ شاخه‌های زیرین درست‌اند. پس ریشه با احتیاط پذیرفتنی است.\",\n \"sources\": [PIE_BHER, PIE_BRAT],\n \"ref_check\": [\n   {\"ref\": \"POK:128\", \"status\": \"supports\", \"note\": POK128},\n   {\"ref\": \"POK:163\", \"status\": \"supports\", \"note\": POK163 + \" — but Pokorny keeps bhrāter- as a lemma of its own and nowhere derives it from bher-.\"},\n   {\"ref\": \"SYN:107\", \"status\": \"supports\", \"note\": SYN107},\n   {\"ref\": \"KAS:10\", \"status\": \"not_checked\", \"note\": \"Hasani Daʾi al-Eslam, Khod-āmuz-e Zabān-e Sanskrit (1361/1982) — refs_online.json records it as a login-only PDF at ketabnak.com, not on archive.org; not accessible.\"},\n   {\"ref\": \"PRT:234\", \"status\": \"not_checked\", \"note\": \"Partridge, Origins (1958) — refs_online.json records archive.org lending-only copies (originsshortetym00part); no open text available.\"},\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW pp. 128 and 163 (POK_01.txt:1800, :2352)\", \"stance\": \"partial\", \"note\": POK128 + \" ; \" + POK163 + \" — supports both roots, contradicts their union in one box.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 153-156 and II 193\", \"stance\": \"partial\", \"note\": WLD_BHER + \" ; \" + WLD_BRAT},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.vv. bher-1 and bhrater- plus the essay at line 155\", \"stance\": \"partial\", \"note\": AHD_BHER1 + \" ; \" + AHD_BRAT + \" ; the essay says 'Male blood relations were designated as bhrater- (BROTHER)' with no hint of a *bher- derivation.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck p. 107 §2.44 BROTHER (SYN.txt:2908)\", \"stance\": \"supports\", \"note\": SYN107},\n   {\"src\": \"IEC\", \"where\": \"Mann, IECD col. 19 (IEC.txt:496)\", \"stance\": \"partial\", \"note\": IEC19},\n ],\n \"nodes\": nodes0,\n})\n\n# ---------------- ENTRY 1 ----------------\nnodes1 = []\n\nnodes1.append({\n \"id\": 1, \"lang\": \"Old Persian\", \"words\": \"braij\", \"verdict\": \"plausible\",\n \"derivation\": \"The form is right but the language label is loose: *braij- is not an attested Old Persian word but the reconstructed Old/Proto-Iranian root, and that is exactly how Nourai's own sources give it. Pokorny p. 137, under '6. bher- ... ,rösten, backen, kochen‘', section '2. Formen mit i, ei', writes 'npers. biris-tan ,braten‘ ... bal. brejag, brijag ,braten‘ ... (iran. *brij-, *braij-)'. Abolghasemi (FFD p. 37) writes 'برشتن / برشت < فارسی میانه brištan < ایرانی باستان *braij-', and Moʾin's footnote in Borhan p. 269 gives 'ایرانی باستان *braij (پختن، برشتن)'. In current terms the root is *bʰerǵ- ~ *bʰreǵ-, whose zero-grade ye-present *bʰr̥ǵ-yé-ti gives Skt. bhṛjjáti and Iranian *br̥j-ya- > MP brištan.\",\n \"derivation_fa\": \"صورت درست است ولی برچسب زبانی مسامحه‌آمیز است: *braij- واژه‌ای گواه‌دار در پارسی باستان نیست، بلکه ریشهٔ بازساختهٔ ایرانی باستان است — دقیقاً همان‌گونه که منابع خود نورایی می‌نویسند. پوکورنی (ص ۱۳۷) می‌نویسد «iran. *brij-, *braij-»، ابوالقاسمی در «فعل‌های فارسی دری» ص ۳۷ می‌نویسد «برشتن < فارسی میانه brištan < ایرانی باستان *braij-»، و معین در حاشیهٔ برهان قاطع (ص ۲۶۹) همین را می‌آورد. به زبان امروزی، ریشه *bʰerǵ- ~ *bʰreǵ- است. پس با اصلاح برچسب زبانی، پذیرفتنی است.\",\n \"sources\": [WK_BERESHTAN],\n \"ref_check\": [\n   {\"ref\": \"POK:137\", \"status\": \"supports\", \"note\": POK137},\n   {\"ref\": \"BQT:270\", \"status\": \"supports\", \"note\": BQT269 + \" (the entry falls on the 269/270 opening)\"},\n   {\"ref\": \"HRN:47\", \"status\": \"supports\", \"note\": HRN47},\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW p. 137, '6. bher-' (POK_01.txt:1927)\", \"stance\": \"supports\", \"note\": POK137},\n   {\"src\": \"FFD\", \"where\": \"Abolghasemi, Feʾl-hā-ye Fārsi-ye Dari p. 37 (FFD_pages.txt leaf [pdf page 41])\", \"stance\": \"supports\", \"note\": FFD37},\n   {\"src\": \"HRN\", \"where\": \"Horn no. 201, p. 47 (HRN.txt leaf 68)\", \"stance\": \"supports\", \"note\": HRN47},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. bher-4 (AHD_watkins1985.txt:335)\", \"stance\": \"partial\", \"note\": AHD_BHER4 + \" — Watkins gives only the Latin branch and the extension *bhrig-, no Iranian material.\"},\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon — grep of KNT.txt for braij/brij\", \"stance\": \"silent\", \"note\": \"No such Old Persian lemma; the root is unattested in the Achaemenid inscriptions, which is why the label 'Old Persian' has to be read as 'Old Iranian'.\"},\n ]})\n\nnodes1.append({\n \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"brištag; brějan\", \"verdict\": \"plausible\",\n \"derivation\": \"brištag 'roasted' is genuine: Horn p. 47 cites 'phlv. ... bristak (Vd. 5, 134 Gl.)' from the Pahlavi Vendīdād gloss, and Tavoosi's Šāyast nē Šāyast glossary p. 103 has gōšt ī brištag 'roasted meat' — exactly Nourai's SNS:103. It is the -ag adjective on the past stem brišt- of the verb MacKenzie lemmatises as 'brištan, brēz- [blystn', blyc-] roast', from Iranian *br̥j-ta-. brējan is also real — Horn cites 'brejan (AV.)' from the Ardā Wīrāz Nāmag and remarks 'Phlv. vrejan ist nur fehlerhafte Schreibung', and Moʾin calls بریجن 'Pahlavi' — but Nourai's gloss for it, 'fry roast' (a verb), is wrong: brējan/brēzan is the NOUN 'baking oven', the ancestor of the NP بریزن/بریجن in his own next box. Pokorny p. 137 lists it as 'npers. bᵉrezan ,Backofen‘' and Horn as 'berīzen, birezen ‚Backofen‘'. Verdict plausible: forms right, one gloss wrong.\",\n \"derivation_fa\": \"brištag «برشته، کباب‌شده» واقعی است: هرن آن را از حاشیهٔ وندیداد پهلوی می‌آورد و در واژه‌نامهٔ شایست نه شایست (ص ۱۰۳) ترکیب gōšt ī brištag دیده می‌شود؛ این صفت با پسوند -ag از ستاک گذشتهٔ brišt- ساخته شده است (مکنزی: brištan، brēz-). brējan نیز واقعی است، اما معنای آن فعل نیست بلکه اسم است: «تنور، اجاق نان‌پزی» — همان که در فارسی نو «بریزن/بریجن» شده و نورایی خود در کادر بعدی آن را «baking oven» معنا کرده است. پس صورت‌ها درست‌اند ولی یک معنا خطاست؛ با احتیاط پذیرفتنی است.\",\n \"sources\": [WK_BERESHTAN],\n \"ref_check\": [\n   {\"ref\": \"SNS:103\", \"status\": \"supports\", \"note\": SNS103},\n   {\"ref\": \"BQT:270\", \"status\": \"supports\", \"note\": BQT269},\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p. 19 s.v. brištan (PHD.txt:292, cross-ref at :285 'brēz-, v. brištan' and :3463 'roast brištan')\", \"stance\": \"partial\", \"note\": PHD_BRISH},\n   {\"src\": \"HRN\", \"where\": \"Horn no. 201, p. 47 with footnote (HRN.txt leaf 68)\", \"stance\": \"supports\", \"note\": HRN47},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II — grep of NYB_vol2_glossary.txt for brišt/bristak/brēz\", \"stance\": \"silent\", \"note\": \"No hit in the OCR of the glossary; neither confirmation nor contradiction.\"},\n   {\"src\": \"POK\", \"where\": \"IEW p. 137 (POK_01.txt:1927)\", \"stance\": \"partial\", \"note\": POK137 + \" — Pokorny gives bᵉrezan as 'Backofen', i.e. a noun, not a verb 'fry roast'.\"},\n ]})\n\nnodes1.append({\n \"id\": 3, \"lang\": \"Persian\",\n \"words\": \"beresteh «برشته»; beryân «بریان»; berîjab «بریجب»; (extra) برشتن ؛ بریز ، بریزن\",\n \"verdict\": \"transcription_suspect\",\n \"derivation\": \"The first two words are confirmed. برشته berešte 'roasted, toasted' is the past participle of برشتن berištan (the parenthesis the book prints beside it) < MP brištan < Iranian *br̥j-ta-; بریان beryān 'roasted' is Pokorny's 'npers. biryān (*brigāna-)', and Borhan-e Qateʾ defines it 'بریان: (از مصدر برشتن) کباب‌شده، برشته‌شده، کباب'; the present stem بریز beriz that the book puts in the extras is the regular MP brēz-. The THIRD word is corrupt in two different ways. (a) The printed page shows the Persian script as «بریجَن» (final nūn, dot above, with a fatha on the jīm), not بریجب as the JSON has it — this is an EXTRACTION error, the last letter was read as bāʾ. (b) The book's own Latin transliteration 'berîjab' is itself a misprint for berījan: Borhan-e Qateʾ p. 269 has 'بریجن ... با جیم بر وزن رسیدن، تنوری باشد که در آن کماج و نان سنگک پزند، و عربی فُرن گویند' (with Moʾin's footnote 'بریجن، پهلوی ... ایرانی باستان *braij'), and Horn p. 47 gives the same word as 'berīzen, birezen ‚Backofen‘', Pokorny p. 137 as 'bᵉrezan ‚Backofen‘'. There is no Persian *berījab. The etymology itself is sound: *braij-ana- 'roasting place' > بریزن/بریجن, with the usual z/j fluctuation of the Iranian palatal.\",\n \"derivation_fa\": \"دو واژهٔ نخست درست‌اند: «برشته» صفت مفعولی «برشتن» است که از فارسی میانهٔ brištan می‌آید، و «بریان» همان است که پوکورنی با بازساخت *brigāna- می‌آورد و برهان قاطع آن را «(از مصدر برشتن) کباب‌شده، برشته‌شده» معنا کرده است. واژهٔ سوم دو خطا دارد: یکی خطای خوانش اسکن — در صفحهٔ چاپی «بریجَن» با نون پایانی آمده ولی در دادهٔ استخراج‌شده «بریجب» ضبط شده است؛ دیگری خطای چاپی خود کتاب — آوانویسی لاتین «berîjab» به جای berījan. برهان قاطع (ص ۲۶۹) می‌نویسد: «بریجن، با جیم، بر وزن رسیدن، تنوری باشد که در آن کماج و نان سنگک پزند»، و معین در حاشیه آن را پهلوی و از ایرانی باستان *braij می‌داند؛ هرن نیز «berīzen ‚Backofen‘» آورده است. واژه‌ای به شکل *بریجب در فارسی وجود ندارد.\",\n \"error_in\": \"extraction\",\n \"book_prints\": \"berîjab : baking oven   بریجَن ( بریزن ، بریز )\",\n \"correct_form\": \"berījan «بریجن» (also بریزن berīzan) 'baking oven'\",\n \"sources\": [WK_BERESHTAN, WK_BERYAN],\n \"ref_check\": [\n   {\"ref\": \"BQT:270\", \"status\": \"supports\", \"note\": BQT269 + \"; the بریان article ('از مصدر برشتن، کباب‌شده، برشته‌شده، کباب', BQT_v1_pages.txt:19327) sits on the same 269/270 opening.\"},\n   {\"ref\": \"BQT:255\", \"status\": \"partial\", \"note\": \"Leaf 476 = printed p. 255 (its footer prints '۲۵۵' and 'برهان قاطع ۳۷') is the برس-/برش- stretch of the dictionary (برسان، برسم، and on p. 256 برشان، برشتخان), so the page reference for برشته is right, but the برشته headword itself is not legible in the OCR of that leaf.\"},\n   {\"ref\": \"MON\", \"status\": \"supports\", \"note\": \"Moʾin s.v. برشته/بریان marks both as inherited [په.] words rather than loans; his etymological footnotes in Borhan (see BQT:270 above) carry the Old Iranian *braij.\"},\n   {\"ref\": \"AEF:256\", \"status\": \"not_checked\", \"note\": \"Khāleqi Motlaq's Asās-e Ešteqāq-e Fārsi (the Persian version of Horn) is print-only — refs_online.json records no online copy. It is, however, the very source Moʾin cites in the Borhan footnote to بریجن ('«اسفا ۱: ۲»'), so the citation is internally consistent.\"},\n   {\"ref\": \"FFD:37\", \"status\": \"supports\", \"note\": FFD37},\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qateʾ pp. 269-270 (BQT_v1_pages.txt leaves 490-491) and p. 255-256 (leaves 476-477)\", \"stance\": \"supports\", \"note\": BQT269},\n   {\"src\": \"HRN\", \"where\": \"Horn no. 201, p. 47 (HRN.txt leaf 68)\", \"stance\": \"supports\", \"note\": HRN47 + \" — Horn's 'berīzen, birezen ‚Backofen‘' is the word Nourai prints as berîjab.\"},\n   {\"src\": \"POK\", \"where\": \"IEW p. 137 (POK_01.txt:1927)\", \"stance\": \"supports\", \"note\": POK137 + \" — 'npers. biryān (*brigāna-) ‚gebraten‘' and 'bᵉrezan ‚Backofen‘' cover two of the three words directly.\"},\n   {\"src\": \"FFD\", \"where\": \"Abolghasemi p. 37\", \"stance\": \"supports\", \"note\": FFD37},\n   {\"src\": \"MON\", \"where\": \"Moʾin's etymological footnotes in Borhan p. 269\", \"stance\": \"supports\", \"note\": BQT269},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p. 19 (PHD.txt:292)\", \"stance\": \"supports\", \"note\": PHD_BRISH},\n ]})\n\nnodes1.append({\n \"id\": 4, \"lang\": \"Latin\", \"words\": \"frîgere\", \"verdict\": \"confirmed\",\n \"derivation\": \"Lat. frīgō, frīgere 'to roast, parch, fry' continues the i-grade of the same extended root: Watkins files it as 'bher-4. To cook, bake. Extended root form *bhrig- in Latin frigere ... [Pok. 6. bher- 137]', and Pokorny prints 'Lat. frīgō, -ere ‚rösten, dörren‘, umbr. frehtu ‚gekocht‘' immediately after the Iranian forms of Nourai's other branch. Ernout-Meillet stress that the original sense was 'faire sécher par la cuisson, cuire à sec' and that 'frire' is secondary, and compare 'gr. φρύγω ‚je fais griller‘, skr. bhrjyáti' — the same three-way i/u/zero distribution Pokorny describes.\",\n \"derivation_fa\": \"لاتین frīgō/frīgere «برشته کردن، خشک پختن» از همان ریشهٔ گسترده با واکهٔ i است: واتکینز آن را ذیل bher-4 «پختن، پوختن» با صورت گستردهٔ *bhrig- می‌آورد و پوکورنی در همان صفحهٔ ۱۳۷ بلافاصله پس از صورت‌های ایرانی می‌آورد. ارنو-میه معنای اصلی را «خشک‌پختن» می‌دانند و یونانی phrýgō و سنسکریت bhrjyáti را هم‌سنگ آن می‌آورند. ادعای نورایی درست است.\",\n \"sources\": [WK_BERESHTAN],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": AHD_BHER4}],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW p. 137 (POK_01.txt:1927, section '2. Formen mit i, ei')\", \"stance\": \"supports\", \"note\": POK137},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet pp. 451-453 s.v. frīgō (LAT.txt:24230-24249)\", \"stance\": \"supports\", \"note\": EM_FRIGO},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 165f. (cited by Pokorny at the end of the '6. bher-' article: 'WP. II 165 f., WH. I 486 f., 548')\", \"stance\": \"supports\", \"note\": \"Pokorny's own back-reference places the Latin, Greek, Indic and Iranian material of this node in one Walde-Pokorny article.\"},\n ]})\n\nnodes1.append({\n \"id\": 5, \"lang\": \"English\", \"words\": \"fry\", \"verdict\": \"confirmed\",\n \"derivation\": \"English fry is ME frien, borrowed c.1300 from Old French frire, the regular French outcome of Lat. frīgere (with the Latin infinitive remade as a 4th-conjugation *frīgīre in Vulgar Latin). Watkins ends the bher-4 entry with 'Latin frigere, to roast, fry: FRY', so the whole chain Latin > (French) > English is on record; Nourai's chart compresses the Old French stage, as he does throughout for Latin-to-English borrowings.\",\n \"derivation_fa\": \"انگلیسی fry از انگلیسی میانهٔ frien است که حدود سال ۱۳۰۰ م. از فرانسهٔ کهن frire وام گرفته شده، و آن دنبالهٔ قاعده‌مند لاتین frīgere است. واتکینز نیز مدخل bher-4 را با «Latin frigere ... : FRY» به پایان می‌برد. نورایی مانند همیشه مرحلهٔ فرانسهٔ کهن را حذف کرده است. ادعای نورایی درست است.\",\n \"sources\": [WK_BERESHTAN],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference of its own; the parent Latin node cites AHD, checked there — AHD_watkins1985.txt:335 ends bher-4 with 'Latin frigere, to roast, fry: FRY'.\"}],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. bher-4 (AHD_watkins1985.txt:335)\", \"stance\": \"supports\", \"note\": AHD_BHER4},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet pp. 451-453 s.v. frīgō (LAT.txt:24230ff.)\", \"stance\": \"supports\", \"note\": EM_FRIGO + \" — the Romance continuations are given as 'M.L.3510 et 3524 frixa, 3504 *frīcta', i.e. the etymon of Fr. frire.\"},\n   {\"src\": \"POK\", \"where\": \"IEW p. 137\", \"stance\": \"supports\", \"note\": POK137},\n ]})\n\nentries.append({\n \"entry\": 1,\n \"root\": \"Bher 2\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"PIE *bʰerǵ- ~ *bʰreǵ- 'to roast, fry' — Pokorny's '6. bher- mit g-Erweiterungen ... rösten, backen, kochen' (IEW 137), Watkins's bher-4 'to cook, bake'\",\n \"note\": \"The page number is right and so is the meaning, but the shape of the root is not what Nourai's own reference prints. Pokorny p. 137 does not have a bare '2. bher- ‚to cook‘'; it has '6. bher- mit g-Erweiterungen, wovor z.T. i-, u-Vokale, ,rösten, backen, kochen‘; von 2. bher- ‚sich heftig bewegen, wallen, kochen‘ abgeleitet' — i.e. the root that means 'to cook' is always the g-extended one (bhereg-, bhrēi-g-, bhrūg-), and Pokorny's '2. bher-' (p. 132) means 'to well up, seethe'. Nourai has taken the page-137 meaning and Pokorny's number 2 from two different lemmas. Watkins avoids the problem by giving the entry as 'bher-4. To cook, bake. Extended root form *bhrig- in Latin frigere ... [Pok. 6. bher- 137]', and today's reconstruction is *bʰerǵ- ~ *bʰreǵ- with a zero-grade ye-present *bʰr̥ǵ-yé-ti behind Skt. bhṛjjáti, Gk. φρύγω, Lat. frīgō and Iranian *brij-/*braij-. So: right page, right sense, wrong root shape and number. Everything hanging under the box is Pokorny's own material from that page.\",\n \"note_fa\": \"شمارهٔ صفحه و معنا درست است، اما صورت ریشه نه. پوکورنی در صفحهٔ ۱۳۷ ریشهٔ سادهٔ *bher- «پختن» ندارد؛ آنچه هست «۶. bher- با گسترش g، به معنای برشتن، پختن، نان پختن» است که خود را مشتق از «۲. bher- جوشیدن، برآمدن» (ص ۱۳۲) می‌داند. پس نورایی معنای صفحهٔ ۱۳۷ را با شمارهٔ ۲ از صفحهٔ ۱۳۲ درآمیخته است. واتکینز همین را به شکل bher-4 «پختن، نان پختن» با صورت گستردهٔ *bhrig- می‌آورد و ریشه‌شناسی امروزی آن را *bʰerǵ- ~ *bʰreǵ- بازمی‌سازد. بنابراین ریشه با احتیاط پذیرفتنی است؛ همهٔ مواد زیر کادر از همان صفحهٔ پوکورنی گرفته شده است.\",\n \"sources\": [WK_BERESHTAN],\n \"ref_check\": [{\"ref\": \"POK:137\", \"status\": \"partial\", \"note\": POK137 + \" — the page and the gloss are Nourai's, but Pokorny's lemma there is '6. bher-' with obligatory g-extension, not a bare '2. bher-'.\"}],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW p. 137 '6. bher-' and p. 132 '2. bher-' (POK_01.txt:1927, :1860)\", \"stance\": \"partial\", \"note\": POK137 + \" ; '2. bher- etwa ,aufwallen‘, von quellendem oder siedendem Wasser ... Vgl. 6. bher-' at p. 132.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. bher-4 (AHD_watkins1985.txt:335)\", \"stance\": \"supports\", \"note\": AHD_BHER4},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 165f. (Pokorny's own reference at the foot of the '6. bher-' article)\", \"stance\": \"supports\", \"note\": \"'WP. II 165 f., WH. I 486 f., 548' — the Walde-Pokorny article covering Skt. bhṛjjáti, Gk. φρύγω, Lat. frīgō and NP birištan.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet pp. 451-453\", \"stance\": \"supports\", \"note\": EM_FRIGO},\n ],\n \"nodes\": nodes1,\n})\n\nout = {\n \"pdf_page\": 89,\n \"book_page\": 59,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": entries,\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-89.json','w',encoding='utf-8') as f:\n    json.dump(out, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk89.py",
 "description": "Write the page-89 verification JSON"
}
```


### [2026-09-05T14:10:32.233Z] TOOL RESULT

```
written
```


## [2026-09-05T14:10:36.856Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -m json.tool data/verification/page-89.json > /dev/null && echo \"JSON OK\"\npython3 tools/verify_check.py 89",
 "description": "Validate JSON and run verify_check"
}
```


### [2026-09-05T14:10:38.720Z] TOOL RESULT

```
JSON OK
nodes verified: 20/20
node verdicts: {'confirmed': 14, 'disputed': 1, 'plausible': 4, 'transcription_suspect': 1}
root verdicts: {'plausible': 2}
ref checks: {'supports': 20, 'partial': 4, 'not_checked': 5}
books consulted: {'supports': 50, 'partial': 8, 'silent': 9, 'contradicts': 4} | by book: {'POK': 10, 'AHD': 9, 'WLD': 8, 'KLN': 6, 'PHD': 5, 'MON': 4, 'BQT': 4, 'SYN': 4, 'LAT': 4, 'HRN': 4, 'WEB': 3, 'KNT': 2, 'FFD': 2, 'BRT': 1, 'HUB': 1, 'SOD': 1, 'IEC': 1, 'LKT': 1, 'NYB': 1}
```


## [2026-09-05T14:11:01.198Z] AGENT

Page 89 (book p. 59) verified. `python3 tools/verify_check.py 89` → **0 PROBLEM lines**, 20/20 nodes.

**Counts** — nodes: 14 confirmed, 4 plausible, 1 disputed, 1 transcription_suspect. Roots: 2 plausible. Ref checks: 20 supports, 4 partial, 5 not_checked (KAS, PRT, AEF and two "None" refs — none accessible).

**Flagged items**
- **disputed** — Bher 1, node #6 English `phosphor`: the arrow French → English is wrong. Klein ("ModL. phosphorus, fr. L. Phosphorus, fr. Gk. φωσφόρος") and Etymonline (phosphor 1630s "morning star" from Latin) give no French stage; French phosphore *is* the source of Persian فسفر (#5), but not of the English word. Ultimate Greek origin is right.
- **transcription_suspect** — Bher 2, node #3, third word: **extraction error the owner must fix.** JSON has script `"بریجب"`; the printed page shows **«بریجَن»** (final nūn with dot above, fatha on jīm). Separately, the book's own Latin `berîjab` is Nourai's misprint for *berījan* — Borhan-e Qateʾ p. 269 has «بریجن … تنوری باشد که در آن کماج و نان سنگک پزند» with Moʾin's footnote «پهلوی … ایرانی باستان *braij», and Horn p. 47 / Pokorny p. 137 give the same word as *berīzen / bᵉrezan* "Backofen". Page image saved to `data/verification/sources/refs/ocr/BOOK/89.png`.

**Roots, why only plausible**
- *Bher 1, Bhrâ-tar*: both roots are real (POK 128, POK 163, Buck 107, Watkins), but Nourai's gloss "Bhrâ-tar: load carrier (of family)" ties them together — no authority derives *bʰréh₂tēr from *bʰer-; it is a primary *-h₂ter kinship term. All branches below are unaffected and correct.
- *Bher 2*: POK:137 is the right page and sense, but Pokorny's lemma there is "**6.** bher- mit g-Erweiterungen … rösten, backen, kochen"; his "2. bher-" (p. 132) means "to well up". Modern form *bʰerǵ- ~ *bʰreǵ-.

**Other plausible** — #14 *Ambhor* (Mann col. 19 really has it, but glosses "two-handled **vessel**", and Watkins/Pokorny treat ἀμφορεύς as inner-Greek); #15 Persian انبر (rests solely on Mann's two words "Per. ambar"; Horn/MacKenzie/Moʾin silent, Wiktionary gives a different origin); entry 1 #1 `braij` (reconstructed Old **Iranian**, not attested Old Persian) and #2 `brējan` (real, but it is the noun "baking oven", not a verb "fry roast").

Strong confirmations found in Nourai's own cited pages: Kent pp. 200-201 lists all five OP preverb compounds verbatim; Horn no. 192 p. 45 and no. 201 p. 47; Gharib no. 2704 (p. 106-107); Klein pp. 203-204; Abolghasemi FFD p. 37; SNS p. 103. Nine web sources archived via `fetch_source.py`.
