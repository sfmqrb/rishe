# Verification process log — verify-page-418


## [2026-09-14T01:11:46.731Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 418 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-418.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-418.json. Write /home/sfmqrb/git/rishe/data/verification/page-418.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 418` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:11:47.619Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:11:48.432Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:11:48.449Z] TOOL RESULT

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


## [2026-09-14T01:11:48.933Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-418.txt"
}
```


### [2026-09-14T01:11:48.966Z] TOOL RESULT

```
1	=== PDF page 418 (book page 388) ===
2	--- entry 0 ---
3	ROOT Reg 2 -> redirect to Rek
4	--- entry 1 ---
5	ROOT [Indo-European] Reg 3 : to dye, color  (refs POK:854)
6	#1 (parent #0) [Sanskrit] refs=SYN:1051 | raj, râga, ranga : be colored, grow red
7	  #2 (parent #1) [Pahlavi] refs=HRN:138; BQT:964; PHD:72 | rang : color
8	    #3 (parent #2) [Persian] refs=MON:1677 | rang «رنگ (آبرنگ، رنگرز، رنگ آمیزی)» : color ; rang-â-rang «رنگارنگ (رنگ برنگ، رنگین)» : colorful ; rangîn kamân «رنگین کمان» : rainbow
9	#4 (parent #0) [Persian] refs=IEC:1065; MON:1640 | rajîdan «رَجیدن (رزیدن ، رنگرز)» : to color, to paint
10	#5 (parent #0) [Sanskrit] refs=OEW:333; AHD:1536 | râkšâ, lâkša : (red) color ; lac : an insect with red eyes, a swarm of such insects, a large number (100,000). | NOTE: POK:32 and KLN:47,856 derive these words from the Indo-European root "Alek:to protect".
11	  #6 (parent #5) [Persian] refs=KLN:856; BQT:1878 | lâk «لاک» : red resin, lacquer | NOTE: See "Alek" for another possible root.
12	    #7 (parent #6) [Portuguese] refs=None | 
13	      #8 (parent #7) [French] refs=None | 
14	        #9 (parent #8) [English] refs=SKT:281 | lacquer, Shellac
15	#10 (parent #0) [Persian] refs=KLN:856; BQT:1900 | lak «لَک» : hundred thousand (soldiers) | NOTE: See "Alek" for another possible root.
16	  #11 (parent #10) [Arabic] refs=AFM:141; FVF:613 | lajj : a large number of people, also the deepest point of sea.
17	    #12 (parent #11) [Persian] refs=MON:3569 | lojjeh «لُجّه» : the deepest point of sea | NOTE: See "Alek" for another possible root.
18	#13 (parent #0) [Greek] refs=SYN:1051; OEW:333 | rhegos : color, dye (red) ; rego-lith : red stone
19	  #14 (parent #13) [English] refs=SYN:333 | regolith
20	--- entry 2 ---
21	ROOT Regh -> redirect to Redh
22	--- entry 3 ---
23	ROOT Rei -> redirect to Leudh
24	
```


## [2026-09-14T01:11:51.652Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-418.json | head -200",
 "description": "Read source JSON page 418"
}
```


### [2026-09-14T01:11:51.730Z] TOOL RESULT

```
{
  "pdf_page": 418,
  "book_page": 388,
  "entries": [
    {
      "root": {
        "name": "Reg 2",
        "redirect": "Rek"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Reg 3",
        "lang": "Indo-European",
        "refs": "POK:854",
        "gloss": "to dye, color"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "SYN:1051",
          "words": [
            {"translit": "raj, râga, ranga", "gloss": "be colored, grow red", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "HRN:138; BQT:964; PHD:72",
          "words": [
            {"translit": "rang", "gloss": "color", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:1677",
          "words": [
            {"translit": "rang", "gloss": "color", "script": "رنگ (آبرنگ، رنگرز، رنگ آمیزی)"},
            {"translit": "rang-â-rang", "gloss": "colorful", "script": "رنگارنگ (رنگ برنگ، رنگین)"},
            {"translit": "rangîn kamân", "gloss": "rainbow", "script": "رنگین کمان"}
          ],
          "note": null,
          "quote": {"text": "غلام همّت آنم که زیر چرخ کبود - زهرچه رنگ تعلّق پذیرد آزاد است", "poet": "Hâfez"}
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Persian",
          "refs": "IEC:1065; MON:1640",
          "words": [
            {"translit": "rajîdan", "gloss": "to color, to paint", "script": "رَجیدن (رزیدن ، رنگرز)"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "OEW:333; AHD:1536",
          "words": [
            {"translit": "râkšâ, lâkša", "gloss": "(red) color", "script": null},
            {"translit": "lac", "gloss": "an insect with red eyes, a swarm of such insects, a large number (100,000).", "script": null}
          ],
          "note": "POK:32 and KLN:47,856 derive these words from the Indo-European root \"Alek:to protect\".",
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "KLN:856; BQT:1878",
          "words": [
            {"translit": "lâk", "gloss": "red resin, lacquer", "script": "لاک"}
          ],
          "note": "See \"Alek\" for another possible root.",
          "quote": {"text": "همی گفت و پیچید بر خشک خاک - زخون دلش خاک همرنگ لاک", "poet": "Onsorî"}
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Portuguese",
          "refs": null,
          "words": [],
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
          "refs": "SKT:281",
          "words": [
            {"translit": "lacquer, Shellac", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Persian",
          "refs": "KLN:856; BQT:1900",
          "words": [
            {"translit": "lak", "gloss": "hundred thousand (soldiers)", "script": "لَک"}
          ],
          "note": "See \"Alek\" for another possible root.",
          "quote": {"text": "درآن نه سایر ماند نه طایر از بر خاک - دو لک ز لشکر او شد به زیر خاک نهان", "poet": "Onsorî"}
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Arabic",
          "refs": "AFM:141; FVF:613",
          "words": [
            {"translit": "lajj", "gloss": "a large number of people, also the deepest point of sea.", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "Persian",
          "refs": "MON:3569",
          "words": [
            {"translit": "lojjeh", "gloss": "the deepest point of sea", "script": "لُجّه"}
          ],
          "note": "See \"Alek\" for another possible root.",
          "quote": {"text": "کشتی هرکه در این لجّهٔ خونخوار افتاد - نشنیدیم که دیگر به کران می آید", "poet": "Sa`dî"}
        },
        {
          "id": 13,
          "parent": 0,
          "lang": "Greek",
          "refs": "SYN:1051; OEW:333",
          "words": [
            {"translit": "rhegos", "gloss": "color, dye (red)", "script": null},
            {"translit": "rego-lith", "gloss": "red stone", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "English",
          "refs": "SYN:333",
          "words": [
            {"translit": "regolith", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Regh",
        "redirect": "Redh"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Rei",
        "redirect": "Leudh"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-14T01:11:52.249Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T01:11:52.297Z] TOOL RESULT

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


## [2026-09-14T01:12:19.311Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','SYN','HRN','BQT','PHD','MON','IEC','OEW','AHD','KLN','SKT','AFM','FVQ','FVF','LKT','HJB','ARY']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n    print('---')\n\"",
 "description": "Inspect refs_online entries"
}
```


## [2026-09-14T01:12:20.434Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"reĝ-\\|reg-.*färben\\|färben\" POK_full.txt | head -40",
 "description": "Grep Pokorny for reg- färben"
}
```


### [2026-09-14T01:12:20.460Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
---
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
---
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
---
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
---
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
---
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
---
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
---
OEW {"title": "J. T. Shipley, The Origins of English Words: A Discursive Dictionary of Indo-European Roots, Baltimore 1984", "edition_found": "1984 (lending-only)", "kind": "archive_restricted", "url": "https://archive.org/details/originsofenglish0000ship ; https://archive.org/details/originsofenglish00jose (both JHU 1984, borrowable) ; HathiTrust mdp.49015002910322 search-only ; Google ELSm5zUgP_wC no view", "identifier": "originsofenglish00jose (also originsofenglish0000ship)", "local_file": null, "page_offset": null, "lookup_hint": "Borrow via IA lending (djvu.txt returns 401/403). Entries are 
---
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
---
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
---
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
---
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/
---
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou
---
FVF {"title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968", "kind": "website", "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)", "lookup_hint": "Alphabetical by Persian headword; noorlib page number N is the scan page — browser needed to read. Not on archive.org.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "PDF exists 
---
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 
---
HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt", "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.4
---
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 
---
```


### [2026-09-14T01:12:20.514Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:12:23.181Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -60; echo \"=== POK sizes\"; ls -la POK*",
 "description": "List refs dir"
}
```


### [2026-09-14T01:12:23.237Z] TOOL RESULT

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
=== POK sizes
-rw-rw-r-- 1 sfmqrb sfmqrb  981836 Sep  4 14:06 POK_01.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1137861 Sep  4 14:06 POK_02.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1170809 Sep  4 14:06 POK_03.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 3971883 Sep  4 14:06 POK_full.txt
```


## [2026-09-14T01:12:26.665Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -c 800 POK_full.txt; echo; echo \"=== count farben\"; grep -c \"farben\" POK_full.txt; grep -c \"färben\" POK_full.txt",
 "description": "Inspect POK_full head"
}
```


### [2026-09-14T01:12:26.744Z] TOOL RESULT

```
List of language abbreviations in tlie lED 



Abbreviation Language name 


Aeq. 




Aequian 


Akk. 




Akkadian 


Alan. 




Alanian (=Old Ossetic) 


Alb. 




Albanian 


Anat. 




Anatolian 


Ang. 




Anglian 


AngN 




Anglo-Norman 


Aram.- 


■Iran 


Aramaeo-lranian 


Ash. 




Ashkun 


Ass. 




Assyrian 


Auk. 




Aukshtaitian 


Bactr. 




Bactrian 


Bel. 




Belorussian 


Br. 




British 


Bret. 




Breton 


BVan. 




Bas-Vannetais 


CCI. 




Continental Celtic 


Chak. 




Chakavian 


Chor. 




Chorasmian 


Clb. 




Celtiberian 


Class. 


Skt. 


Classical Sanskrit 


Co. 




Cornish 


Corn. 




Cornouillais 


Dae. 




Dacian 


Dan. 




Danish 


Dard. 




Dardic 


Dzuk. 




Dzukian 


EBI. 




East Baltic 


EGm. 




East Germanic
=== count farben
3
0
```


## [2026-09-14T01:12:31.800Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==510' POK_02.txt | head -80",
 "description": "Print Pokorny p.854 area"
}
```


## [2026-09-14T01:12:32.884Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"854\" POK_full.txt | grep -i \"reg\\|dye\" | head -20; echo \"===\"; grep -n -i \"to dye\" POK_full.txt | head -20",
 "description": "Grep POK_full for dye"
}
```


### [2026-09-14T01:12:32.926Z] TOOL RESULT

```
(Bash completed with no output)
```


### [2026-09-14T01:12:33.006Z] TOOL RESULT

```
===
63937:Maybe zero grade in alb. {*ng"h-en) ngjyenfXo wet, moisten; to dye, color, imbue'.
```


## [2026-09-14T01:12:35.972Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in POK_01 POK_02 POK_03 POK_full; do echo -n \"$f pages: \"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' $f.txt; done",
 "description": "Count POK pages"
}
```


### [2026-09-14T01:12:37.108Z] TOOL RESULT

```
POK_01 pages: 363
POK_02 pages: 433
POK_03 pages: 429
POK_full pages: 1
```


## [2026-09-14T01:12:42.766Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nprint(d['POK']['page_offset']); print(d['POK'].get('lookup_hint'))\nprint('---SYN'); print(d['SYN'].get('lookup_hint'))\nprint('---KLN'); print(d['KLN']['page_offset']); print(d['KLN'].get('lookup_hint'))\nprint('---BQT'); print(d['BQT'].get('page_offset')); print(d['BQT'].get('lookup_hint')); print(d['BQT'].get('scans'))\nprint('---MON'); print(d['MON'].get('page_offset'))\nprint('---SKT'); print(d['SKT'].get('lookup_hint'))\nprint('---IEC'); print(d['IEC'].get('lookup_hint'))\n\"",
 "description": "Get full page offsets"
}
```


### [2026-09-14T01:12:44.195Z] TOOL RESULT

```
POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
---SYN
Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
---KLN
KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
---BQT
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
[{'volume': '3', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', 'ocr_note': '689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py'}, {'volume': '4', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', 'first_printed': 1920, 'last_printed': 2475, 'pdf_offset': -1917, 'lang': 'fas', 'offset_note': 'printed = pdf+1917, checked at pdf 150 and 500', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt'}, {'volume': '5', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', 'first_printed': 1, 'last_printed': 290, 'pdf_offset': 5, 'lang': 'fas', 'note': "vol 5 = ta'liqat (addenda) with its own pagination 1-290; cite as BQT5:<page>. Plain BQT:<n> with n<1208 refers to vols 1-2 (OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt), not to this scan.", 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', 'requires_volume': True}]
---MON
None
---SKT
Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
---IEC
Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
```


## [2026-09-14T01:12:48.101Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 85[3-5]\" POK_full.txt | head -20; echo \"=== lemma reg\"; grep -n \"^Root / lemma: reg\\|^Root / lemma: reĝ\\|lemma: re[gĝ]\" POK_full.txt | head -30",
 "description": "Find Pokorny lemma near p.854"
}
```


### [2026-09-14T01:12:48.173Z] TOOL RESULT

```
69489:Page(s): 853 
69509:Page(s): 853 
69515:Page(s): 853 
69530:Page(s): 854 
69548:Page(s): 854 
69712:Page(s): 854-857 
70977:Page(s): 853 
70998:Page(s): 854 
71050:Page(s): 853 
71055:Page(s): 853 
71060:Page(s): 853 
71065:Page(s): 853 
71084:Page(s): 853 
71092:Page(s): 853 
=== lemma reg
27825:{arg-Tj, fgi-\ "glittering, white, fast' and its subsequent zero grade Root/ lemma: reg-1\ 
69534:Root / lemma: reg-2 
69550:Root / lemma: reg-1 
69567:zero grade Root/ lemma: reg-1 \ "right, just, to make right; king'. 
69716:Root / lemma: reg-2, reR- {rek-7)
```


## [2026-09-14T01:12:50.510Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '69480,69600p' POK_full.txt",
 "description": "Print Pokorny reg entries"
}
```


### [2026-09-14T01:12:50.565Z] TOOL RESULT

```
Germanic *reb-"\n heftiger Bewegung sein', Middle Higli German rebensiem Vb. "sicli 
bewegen, rijhren', Modern High German Bavarian reb/sch ' a\ert, awake, smart', Swiss 
rabe/n'rant, roister'. Middle High German /'(9i6'e/7"traumen, baffle sein'. Middle Low 
German reven^ nonsensical talk, speak, think', Norwegian dial, rava 'h\n and hertaumein' 
etc. 

References: WP. II 370, Szemerenyi ZDMG. 101, 207 ff.; 
See also: extended from er-. 
Page(s): 853 

Root / lemma: rdd^-2 

Meaning: to roof 

Material: Gr. epscpu), spsniu) "ijberdache' (*uberwolbe), uitJ-npecpnc; 'with hoher 

Bedachung', 6po(po(; 'das reed, wherewith man die Hauserdeckt, roof, ceiling', opocpn 

"Bedachung'; Old High German /7//77//'ei6'a 'cranium' (*'brain -bedachung'); Old High 

German rippa, rippi. Old Saxon nbbi. Old English nbb. Old Icelandic rifv\. ' rib ' ( *r^'^Jo-\ 

die Rippen cover die Brusthohle, as das Dach das Haus); russ. -Church Slavic rebro^ rib '; 

engl. reef reef is Danish loanword 

References: WP. II 371, Trautmann 241. 

Page(s): 853 

Root / lemma: red- rod- 
Meaning: flow' 

See also: see above S. 334 {ered-). 
Page(s): 853 

Root/ lemma: re5'-/(and sreg-7) 

Meaning: to paint 

Material: Old Indie rajyat/larbt sich, rotet sich', newer rajyate, Kaus. rajayati^iarb\!, 

secondary ranjayatr, ragam. 'das Farben, rote paint, color'; 

gr. ps^u), Aor. ps^ai ' paint ', psYMO 'gefarbter Stoff', paysuc; (also poy£U(;) Tarber', 
Xpuao-pay£(; xPuaopa(p£(; Hes.; daft ps^u) keinen vowel suggestion experienced has, is 
auffallig; compareSchwyzer Gr. Gr. 1, 310 and Boisacq 838. 

References: WP. II 366. 
Page(s): 854 



Root / lemma: reg-2 

Meaning: to see 

Note: only albanesisch and Baltic 

Material: Alb. may'sehe an, look, see'; Lithuanian regiu, reget/'see', ragana^ witch ' 

(compare ' wicked look'), /'e^//77a5 'visible, apparent, manifest, obvious', Latvian redzet 

"see'. 

References: WP. II 366, Jokl Stud. 75. 

Page(s): 854 

Root / lemma: reg-1 

Meaning: right, just, to make right; king 

Grammatical information: forms Indo Germanic neither root present nor perfect tense; 

participle Perf. Pass, reg-to-^ law ' 

Note: 

Alb. shq/pe ' eag\e' seems related to Old \n6\c rj7-pya ' darting along ' epithet of the bird 
syena- ("eagle, falcon'), [Rumanian soim "falcon'], Avestan arazi-fya- (cf. gr. ap^icpo(; asTOi; 
irapa FlEpaaK; H., aivinoijj), Armenian arcui{< *arci-wl) "eagle' which is evidently a form of 
the same word; that it is Macedonian confirms its reality. 

Alb., gr., Avestan, and Old Indie prove that from Root/ lemma: er-1, or- : "eagle' derived 
extended Root/ lemma: ar(e)-g-{arg-?), fgi-\ "glittering, white, fast' and its subsequent 
zero grade Root/ lemma: reg-1 \ "right, just, to make right; king'. 

Material: Old Indie „^ya//; nasalized //t/s//" stretches itself, it hurries (from horses)'; probably 
also irajyati {W\Vc\ unclear /■) " arranges, orders, enacts, decrees '; rjLi-, Avestan srezu-^ 
just, right ' (in addition arszus^ finger'. Gen. srezvo), Kompar. Superl. Old Indie rajlyas-, 
rjTyas- " straight ', rajistha-, Avestan razista- " the justest, justest '; 

Old Indie ^/yra- from horses = rju-gamin, rjrasva-, Avestan arazraspa- EN actually " 
whose steeds haste straight on; with fast horses ', next to which compound form *rji- in rji- 
pya-{2. part unclear) " soaring straight ahead ' (epithet of syena- " eagle, falcon '), Avestan 
arazi-fya- m. " eagle, name of a mountain or mountains ', by Hes. ap^icpoc; (i.e. ap^icpo(;) 
a£T6(;napa FIspaaK;, Armenian arciv{*arcivi) " eagle ' (beside it *rju-pya-, ap. *ardufya-\x\ 
npers. aluh "eagle', compare gr. aiYuni6(;, if transfigured by folk etymology after ai^ from 
*apYuni6(;); rji-svan- EN actually " with fast dogs ', compare in gr. dp^oq, (from *apY-pO(; 
diss.) " fast, quick ', above S. 64; 



Maybe zero grade in alb. (*p^i(po(;), ^icpo-, shqiponje^ea<^\e', alb. Geg Shqipni, alb. Tosc 
Shq/per/land of the eagles'. 

Old Indie raj/-'s\ch aufrichtend, straight', rajf- RV perhaps "line, row' (= Middle Low 
German reke under S. 856); rajas- (Avestan razah-) n. 'Raum'; 

Avestan raz- {razayeiti, participle rasta-, gr. opsKToq, Latin rectus, Gothic rafhts, Avestan 
rast9m"\n gerader direction') " direct, aim, point, gerade richten, sort, order, arrange', 
razan-'order, statute ', rasnu-' justified, legitimate ' (compare gr. 6p£Yvu-|ji), probably also 
razura-n., razurat 'wood, forest', razare, razan- " command, alignment '; rasman-m. n. 
"Schlachtreihe' (: gr. opsypa, Latin regimen); 

Old Indie raj- (Nom. Sg. rat) "king' (= Latin rex. Old Irish rf, s. also Gothic reiks), rajan- 
ds., rajnro^ueeu, FiJrstin', rasp, rajati"\s king, herrscht, glares, gleams' (denominative), 
rajya-^ royal ' (= Latin regius, compare also Old High German rJhhl), rajya-, rajya-v\. 
"power, rule' (= Middle Irish rTge, compare also Gothic reiki), /'5s//7'"Herrscherin', rastra-n.
```


## [2026-09-14T01:13:08.052Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN grep DYE\"; grep -n \"^4\\.7[0-9] \\|DYE\" SYN.txt | head -20",
 "description": "Grep Buck for DYE"
}
```


### [2026-09-14T01:13:08.107Z] TOOL RESULT

```
=== SYN grep DYE
7193:4.71 BEGET (of Father)
7248:4.72 BEAR (of Mother) Grk.  tlxrw yervdw Goth. gabairan Lith.  gimdyti NG yovi ON ala, feda (bera) Lett. dzemdét Lat. parere Dan. ffde ChSl.  roditi It. partorire Sw.  féda SCr.  roditi Fr. enfanter OE beran, cennan (fédan) Boh.  roditi Sp. parir ME bere Pol. — rodzié Rum. naste NE bear Russ. rodit’ Tr. do-fuismim, biru Du. baren Skt.  jan-, si Nir. _betrim, iuismim OHG (gi)beran, kindon Av. zan-, hu- W. planta, gent MHG (ge)bern, kinden
7260:4.73 PREGNANT Goth. inkilpo, pat es pees vos <2 ieee ON unguo, Ulett, hafan- ett. gr Grk. (yyvearpane” tb a id A di, med barni ChSl. neprazdtna NG pracgnans, GRE Dan.  frugtsommelig, svan- SCr. _trudna, breda, nose¢a lat. inciéns | iatoreg: ger; dreglig Boh. téhotna; brezt gravida, ncn a, P Sw. havande; draktig Pol. brzmienna, ciezarna te na Deine OE getacnod, bearn-éacen, Russ. beremennaja Fr encernle, 9” pee 4 med cilde Skt.  garbhini-, garbhavati-, Sp. prenada, Pets ME with childe, with barne etc. Rum. insdr Fie ut NE pregnant, with child Avy. pubra- lorrac . ; drachti Ir. ‘i hea- Du. zwanger; 9g Nir. bruinneach, tourch GHik. smaieee sach MHG _ swanger, trehtec, w. _ beichtog swere : razez, dougerez eee Breese eraeees NHG  schwanger; trdchtig
7344:4.75 DIE; DEAD; DEATH
7452:4.77 CORPSE
7479:4.78 BURY (the Dead) Goth. ga-, us-filhan, gana- Lith. (pa)laidoti, pakasti
10322:6.39 DYE (vb.)
```


## [2026-09-14T01:13:08.987Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN rang\"; grep -n \"rang\" HRN.txt | head -30",
 "description": "Grep Horn for rang"
}
```


### [2026-09-14T01:13:09.048Z] TOOL RESULT

```
=== HRN rang
193:immer herangezogen. In Bezug auf das Kurdische sind
819:frangais.
1576:ap. *avaranga- oder wohl besser '^abiranga- (vergl.
1577:skr. ranga- Tarbe* und auch 'Schauplatz, Theater);
1578:phlv. hil]aürank (statt avrang), AV. 14, 8. (Hörn).
1737:phlv. vatrang (PPGl., Bund.), vatreng (Bund.), vatreg
3106:kurd. LW. pilink; afy. prang,
5554:LW. kurd. renk, reng; af/. rang; bei. rang (216).
6599:np. sök *Ähre, Granne* nicht herangezogen werden.
9327:reich, prangend*; phlv. varc bezw. varj, varcömamJ
10538:schreibend, vgl. dranggav.
11394:getrennt, während sonst e überall gleichmässig mit li rangirt. Auch s
15883:dranggar 9ä^'\
```


## [2026-09-14T01:13:14.349Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5540,5570p' HRN.txt; echo \"=== which leaf\"; awk 'BEGIN{RS=\"\\f\"} {n++; if (index($0,\"LW. kurd. renk, reng\")>0) print \"leaf\",n-1}' HRN.txt",
 "description": "Print Horn rang entry"
}
```


## [2026-09-14T01:13:15.235Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10322,10360p' SYN.txt",
 "description": "Print Buck 6.39 DYE"
}
```


### [2026-09-14T01:13:15.677Z] TOOL RESULT

```
Ktesias bei Photius 44*^ 3, 4. ylrtvai fuy.oov hv üe^öaig
(lovidiov, (o 71 i^fUTTio aar og ovdti' ianv, dkk^ aXov diuTiXeMv
TnjusXijg rce svrog' yccxi vo/iuLovniv avs/tKO aal ^oooot T{)b-
(fjtod^ai ro C(pov' ovouaCsvai Jt ^vvräxtjg Plut. Artox.
19, 3. QVvödy.Tj rj'kiy.ov nsQiövsQa Hesych.
de Lagarde, Ges. Abh. 225; zuerst Reland,
Dissertatio de reliquiis veteris linguae persicae.
622. rendlden 'schaben, kratzen*, rende.
ai. [/'rad', rddati 'kratzen, ritzen'; phlv. randUan
(AV.).
kurd. renin; bei. randag *kämmen' (312).
623. {\)reny 'Farbe*.
skr. rafiga- 'Farbe*; arm. LW. erafig 'Farbe* (H.,
. No. 96).
LW. kurd. renk, reng; af/. rang; bei. rang (216).
') Audi uriu. rum 'Meiisclicnliuui'u .- 139 -
624. {2)renff *Bergschaaf* (Vis und RäniTn, S. 144 Vers 13,
245 Vers 2 v. u.; Scliefer, Chrest. pers. 11, 249,
17 «.).
skr. ranku- *eine Art Antilope' (Nöldeke, münd-
liche Mitteilung).
625. revän 'Seele'.
aw. urvan- (d. i. tiruvan') *Seele*; phlv. riivän (ge-
schrieben )X2n), ruvdmk.
626. robäh *Fuchs'.
g. rüwüs *Fuchs (Semn. rüwä *Katze').
aw. raopis (?) ; plilv. röpäs, röbas ; ai. löpa^d- (skr.
lopäka- 'Art Schakal') *Fuchs'; arm. a)Me8 *Fuchs'
(Hübschmann No. 9).
Verg]. Bartholomae, Bß. 10, 294, der gr. dhimfj^
für ein Lehnwort hält; ebenso G. Meyer, Indog.
=== which leaf
leaf 159
```


### [2026-09-14T01:13:15.816Z] TOOL RESULT

```
6.39 DYE (vb.)
Grk. Béxrw Goth. .... NG Badw ON lita Lat. _tingere, inficere Dan. farve It. lingere Sw. farga Fr. leindre OE
Sp. lefiir ME dye Rum. boi, vépsi NE dye Ir. (dathaigim) Du. __verven Nir. dathuighim OHG farawen W. liwio MHG verwen Br. liva NHG farben
Lith. dazyti, parvuoli Lett. krdsuot (pervet) ChSif se �� SCr. bojadisati (farbatt)
déagian, telgan Boh.  barvili
Pol. farbowad (barwié) Russ. krasit’ Skt. ranjaya-
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Sy ee
cLorHl listed mean simply a used alike for ‘dye i a board, house, ete.). m the notion of ‘dip’,
applicable to the process of ly
‘dip’ (Hom.+); hence ‘dipping, dye’, Badets (new pres. to aor. éBawa) ubmerge, overwhelm’, f the sea’, etc. Walde- 4, Falk-Torp 504.
1, Grk. ante idye’, of. Bagh idyer' NG pee ON ko)eia 8 osw. kvaf ‘depth 2 7.1674. Boisaca 11
9, Lat, tingere ‘dip, soak’, hence ‘dye’ oh lingere, Fr. teindre, Sp. tenir liye, stain’), of. inctus ‘a dipping, dye- ing’, tinctor ‘dyer’ : Grk. reyyo wet, moisten’, OHG thunkon, dunkon ‘dip, gak’, Walde-P. 1.726. Ernout-M. 1041. REW 8750.
Lat. inficere, lit. ‘put into’, hence esp. ‘put into a dyeing vat, dye, color’ (cf. infeclor ‘dyer’), cpd. of facere ‘do, make’, Ernout-M. 324.
Lat. fiicdre, rarely ‘dye’ (wool), most- ly ‘paint the face’, deriv. of fiaicus name fa plant and the dye made from it, touge’, borrowed fr. Grk. ¢ixos id. Emout-M. 396, pare ae boiangiu kotsch 328, Bea
Rum. vdpsi, Te also and orig, ‘q Biya (above 1 (late Ch}. 9, 1713,
‘dyer’) : boia ‘dye, paint’. Lo-
8. vb. for ‘paint’, but ye’, fr. Grk. aor. infin. ), perh. through Slavic - vaptsati ‘stain’, ete.). Tiktin
+ 3. Ty, a iain mitigim (quotable?), Nir. 5. Ny. of Ir. dath ‘color, dye’ W. lity; : tWwio, Br. liva both also ‘paint’ . , 4 . ae Br, liow ‘color, dye, ee at. livor ‘bluish e275 Pedersen
NG; PERSONAL ADORNMENT AND CARE
igitized by Arya Samaj Foundation Chennai and eGangotri
415
4, ON lita, deriv. of lr ‘color’, orig. ‘complexion, appearance’ : Goth. wlits, OE wlite ‘appearance, form’. Walde-P. 1.293. Falk-Torp 679.
OHG farawen, MHG verwen, NHG farben, Du. verven, Dan. farve, Sw. farga, derivs. of sbs. OHG farawa, etc. (MLG verwe > Dan. farve, Sw. fdrg) ‘dye, paint, color’ : OHG faro ‘colored’, Grk. mepxvés ‘dark, livid’, Skt. preni- ‘speck- led’, etc. Walde-P. 2.45. Falk-Torp 206.
OE déagian, ME, NE dye, derivs. of OE déah, déag ‘dye’, NE dye, prob. : OE déagol, OHG tougal ‘secret, hidden’, but root connection and semantic se- quence dub. (see 17.36). Walde-P. 1.838.
OE telgan (only in gl.) deriv. of telg ‘dye, paint’, etym.?
5. Lith. parvuott, Lett. pervét, Boh. barvit?, Pol. barwié, farbowaé, SCr. far- batz, derivs. of the nouns for ‘dye, paint’, these loanwords of different periods fr. MHG varve, MLG verwe, or NHG farbe (above, 4).
Lith. daZyti, orig. ‘dip’ hence ‘dye’ (cf. dazas ‘dye, color’), etym.? Walde-P. 1.786.
Lett. krdsuot, deriv. of krasa ‘dye, paint’, loanword fr. Slavic (cf. Russ. krasit’, below, 6).
6. SCr. bojadisati, also ‘paint’, deriv. of boja ‘dye, paint’, this from Turk. boya id.
Russ. krasit’, ‘adorn’ hence ‘dye, paint’, fr. krasa ‘beauty, adornment’ : late ChSl. krasa ‘beauty’, OBoh. krasa ‘light, splendor’, etc. Berneker 607. Walde-P. 1.418 ff.
7. Skt. ra(v)jaya-, caus. of ra(i)j- ‘be bright, colored, red’ (cf. raga- ‘coloring, dyeing’, rakta- ‘colored, red’) : Grk. pétw ‘dye’, peyebs or payebs ‘dyer’ (all rare). Walde-P. 2.366.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
2.8.48 2 |. 6S
Digitized by Arya Samaj Foundation Chennai and eGangotri
416 SELECTED INDO-EUROPEAN SYNONYMS
6.41-6.59. The attempt to set up even approximate synonyms meets with more than the usual difficulty in the case of articles of dress, owing to the radical differences in the costume of various peoples and periods. Thus there are so many kinds of cloaks and coats with their distinctive names that it is diffi- cult to select the most important, and in the case of some words even the as- signment to one or the other group is arbitrary. Conversely, there is nothing in early periods like the modern trousers, which evolved from the short breeches or the long stockings or leggings. The early Cretan figurines show a remark- ably modern woman’s costume with separate jacket and skirt, but there was nothing similar among the Greeks or Romans of the classical period. Their ‘tunic’, a jersey-like garment, might
from the point of view of fun called a ‘coat? (and is in fa
Ction be
```


## [2026-09-14T01:13:29.660Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD rang\"; grep -n \"^rang\\|rang \" PHD.txt | head -20; echo; echo \"=== PHD_mackenzie\"; grep -n \"rang\" PHD_mackenzie.txt | head -20",
 "description": "Grep MacKenzie for rang"
}
```


### [2026-09-14T01:13:29.728Z] TOOL RESULT

```
=== PHD rang
170:abilag 5/4! | N ~a] blister. a-bim [bym] fearless. āb-kāmag [5A mk! | N ~a] a thick, sour soup. abnüs Pžēnws | (N ābnūs)] ebony. a-biy Pbwd] senseless. ~ih: senselessness. à abr РЫ, Séi | N ~] cloud. M bel abrang [ing | N aurang] glory, splendour. abrastan, abraz- [AP stn',SPc- | М ?br?st, N (afráttan), afrdz-] lift, raise. abraz [Pe | N afrāz] acclivity. abrēšom Pflyš(u)m | M? bryfwm, N ~} silk. ~én [-yn!] silken. abróxtan, abróz- ['piwhtn', ?phoc- | M brwxt, ?)brwc-, N afróxtan, afróz-] light, kindle, illuminate, polish. ~i$n(ih): illumination. āb-tazan Pftcn!] watercourse. a-bun [*dwx!] baseless, bottomless. a-burd-framān ['bwltplm^n'] disobedient. ~th: disobedience. aburnāy f(w)lnd, v. purnāy | N burnā] under age, child. ^h : childhood. aburnáyag [?A(w)/n’(d)yk'] child. abus [pws] (woman) having just given birth. “АҺ: childbirth. арив, -tan Pws, -tn! | M ’bwws, v. ábestan] pregnant. „il: pregnancy. abydxtan, abyóz- Phywhtn', ?bywc-] join, mix. āb-zan zn! | N ~] bath. labzar [el pel] M *6c*7, N afzār] instrument, means; spice. *abzar [6271 | M bail skill, power; powerful. „ūmand [-wmnd] skilled, able. abzāy-, —išn, у. abztidan, abzón [?pzwn! | M, J ”*bzwn, N afzün] increase, growth. ~ig [-yk!] increasing, expansive, bountiful. ~igih: bountifulness. abzüdan, abzáy- ['pzwtn!,^?pzd- | M ?bz'y-, N afzüdan, afzāy-] in- crease, grow. ~i$n: increase, growth. a-čār [cI] inevitable, Jee ~ag [-k'] compelled.
212:anērān [?7°3?n'] non-Eran, the world beyond Eran. an-érang [?n’ylng] blameless. an-espās [’nsp’s] ungrateful. ~ih: ingratitude. 2 AY angubén [DW BS Y.A < A dbf ; ?ngpyn! | N angubin] honey. By? Wat), angür [AN BE < A ‘nb’; ?ngwl | N ~] grape. А AC k angust Pngwst! | (N angust)] finger, toe; unit of length (š in.). Va м ~arig [-lyk'] finger ring. „bān [-p’n'] finger-guard, -stall. anidan, ānay- [HY TYWN-tn! < А hyty, ^? th; ?nytn!] bring, lead. anig Payk! | (N pēšānī)] front, forehead. anī-z [AH RN(y)e, v. any | N niz] other also. anjir Pncyl | N ~] fig. anódag [nwtk! | M ?nwdg] strange, alien. ~ig [-yk'] foreign. ünóh, *ànóy [TME < A tmh | M ?nwh, ?wy] there. an-dst Pwwst'] infirm, unreliable. anos [nws] lit. immortal, i.e. the next life; elixir, antidote. — xwardan : risk death, fight to the death. anošag Pxwšk! | M ?nwsg, N ~a] immortal. «ii: immortality. ~-ruwan [-lwb’n'] the late, deceased. an-Ošmār [?7wsm’l] countless, innumerable. anó$-xwar [поў] mortal. *апбу, v. ānēh. anSahrig [nstr'yk'] slave. an-umméd P7wmyt! | J *nwmyd, N nauméd] hopeless, despairing. an-uspurrig [^r wspwlyk') imperfect. any [AH RN < A *hrn; (corruptly, 2К?у = *dn-i) | M ?n()] other. a-pattüg [ptwk!] impatient. a-paymān (?ptm?n!] immoderate. ~ih : immoderation. *apédag [ругА! | P?pyd(g)] lost, stray. ~dar [-d?/] custodian of stray animals. a-petitig žtytyk!] unrepentant, unconfessed. 7h : unrepentance. a-petyürag Pf(y)tyd'lk'] without misfortune, unassailed. a-pohisn Pwhšn'] incorruptible. appar [?5/ | М ’pr] robbery, theft. appar ['P?/] taken away, removed. ~ih : removal, loss, deprivation. apparag [25/6] robber. appurdan, appar- [YHNCLWN-tn' < A yhnslwn, V asi: >pl- | M эрит, *p(w)r-] steal. ~išn: stealing, theft. a-pursišnīg Ppwrsinyk'] irresponsible.
298:čāšt [ой | N ~] lunch, meal. 1~ag [-k'] food. &а$їар [c'štk'] doctrine. čāštan, čāš- [c?s-tn'] teach. ~išn: teaching. čatrang [cting | (Ar. šatranj)] chess. *taw(la)gan [cwpk'n!! | Ar. sawlajan, N čaugān] (curved) polo-stick ; polo. CaxSágih [ch kyh] (sense of) taste. čaxšišn [chsfn! | M, J схі, N ¿aš-] taste, flavour. 148 [ME < A mh | M cy, N či] what, which. ~ ray: for what, why. ~ih: quiddity, essence. tčē [ME, v. 166] for, because, since, as, that. &ë-ëwënag [ME ^ dwynk!] how. ~ith : circumstances. čegām-iz [су?т-с | M cyg^myc], —-6(w): a little; whatever. Cegámag [cyk”mk! | N &(ag)áma] song, snatch. €éh- , —išn, v. idan. *téhag [cyhk'] grief. čehel [40 | N chil] forty. Céh-widarag [cyhwtlg] = činwad puhl. čēlān [cy”x! | = M, N ~] dagger. ~gar [-kl, -gl | N ~] swordsmith. Cér [cyl | M cyr, N —] victorious, triumphant, brave. —Ih: bravery. Cérihistan, Cérih- [cylyh-stn'] triumph, be victorious. īčīdan, čīn- [cytn', cyn- | M cyydn, cyn-, N ~] gather, pile up. ~išn: gathering. *čīdan, čēh- [cytn', cyh- | M cy-] mourn, lament, grieve. ~i8n : lamentation. ~i$nig¢ : mournful. ihr [cyhl | M cyhr, № ~] form, shape, appearance, face. žčihr(aģ) [cyhl(k') | M сулу, P -g, № ~] seed, origin; nature, essence. Cihrénidan, čihrēn- (cyhlyn-ytn'] form. Cihrig [cyhlyk'] natural. čihr-šnāsīh [суйру] physics. čim [c(y)m | M сут, N ~] reason, cause, purpose, meaning. ~ (ray): why? Cim-gó6wáàgih [сут gwh’kyh] logic. čimīģ [cymyk!] purposeful. čīn-, ~i8n, v. idan. čīnag [cynk! | P cyng, N ~a] grain, bait. Cinàr [су | N ~] oriental plane tree. činwad [cynw(p)t'], ~ puhl: the ‘divider bridge’ which separates the souls of the righteous dead, who cross, from those of the wicked, who fall off.
321:ë ру | (M hyb)] particle giving the present tense optative sense. é, v, éd, éw. ēbāraģ [*dyp'lk', ^dwlk! | N éwàr] evening. ébgat(ih) ['ybgt!, -yh = Av. aifi.gati-] (onslaught of) Evil; the Adver- sary. ēbsrūsrim [>ур-, ?ybslwslym = Av. atBisrūdrima-) the gah from sunset to midnight. ébyünghan [>ур-, ?ywby?nghn!, etc. = Av. aiBydshana-] sacred girdle, = kustig. ёё Pye | (P ?ушус), N héc] (with a negative) not any. ēčand, v. éw-Cand. éd (HN A < A hr? | M? yd] this; v. dāštan. ~ ray ёё [cf. N z-é-rá] because, since. édar [LTME < À I-tnh | M?ydr, N ~] here. édin [ytwn'! | N ēdūn] thus, so. ~ih: (correct) manner. ëg [ADYN' < А *dyn | М ?yg] then, thereupon. ëk Pywk' | M yk, N yak] one. ëkanag [Pywk’nk! | N yagana) submissive, obedient. ^h : submission, obedience. ēk-dād [ywkd’t'] sole-created. ēmēd [*dmyt'] hope. ēn [ZNE < A znh | M *yn, N in] this. -ën [-yz! | = M, N -in] suffix forming adjectives of material or quality. -endag [-ndk! | M -yndg, N -anda] suffix forming present participles. -én-idan [-yn-ytn' | M -yn-ydn, (N -àn-)] suffixes forming causative and transitive denominative verbs. *énókén Pynw(k)kyn' = Av. *aēnē.kaēnā-) heiress (under the obligation of continuing her father's line). enya рулу | (M ?n’y)] otherwise, moreover. lër [d] | M Zur, v. azér] down, below; low; under. — ud abar: upside down. tēr Pyl] noble; hero, ~ih: nobility, good conduct. Eran [y”x! | N ~] Eran, (land of) the Aryans. ~ag [-k'] an Eranian, Aryan. érang [”y/ng] blame, condemnation; error, heresy. ~ih: = érang. éranj-, v.  * éraxtan. Ērān|-šahr (yPnitr! | N ~] land of the Aryans. —-wëz [-wyc] (original) home of the Aryans. 1ёгахќап, ёгапј- Pylhtn!, ?уЇпс- | J ?yrxt] blame, condemn, damn.
510:~ pazd- : blow, play the flute. *nāydāģ [nywt’k'] deep, unfordable, navigable. nayestàn [KN Y Ast^n! | N ~] reed-bed, cane-brake. nāyīzaģ [»vck! | N ~a] small reed, straw. nay-sray [rds d] flautist. nazd [nzd | = M, N ~] near. nazdik [nzdyk! | = M, N ~] near. ~ih: proximity. nazdist [x3dst'] first. nàzišn [x*cšn! | N nāsi$] 1. boasting; 2. kindness. nàzuk [n’cwk! | (M wzwg), N ~] tender, gentle; fickle. né [L4 < AP | M ny, N na] no, not. nék [nywk! | M nyk, N ~] good, beautiful. ~th: goodness. nék-góhr [nywk gwhl] good-natured, virtuous. ~ih: goodness, virtue. nēkēģ [nywhkwk! | M nyyquiw!, IN neho] == пёк. nem [PRG < А plg; nym | = M, N —] half. ~ag [nymk! | N ~a] half, side, direction. ~-аѕр [5р] centaur; astr. Sagittarius. ~-rōz [-lwe | M -rwe, N ~] midday, south. ~-tan [-tn' | N ~] middle of the body. nérang [nylng | N <] incantation, charm, spell. пёгӧб [nylwk! | M nyrwg, N nero] strength, power. ~omand [-’wmnd] strong, powerful.
555:rabih [/pyh | M rbyh] noon, midday (heat). rad [/t! | N —] (spiritual) chief, master. АҺ: office of rad. rad [Pu | P rd, N ~] generous, liberal. ~ih: generosity, liberality. radag [itk! | M rdg, N rada] line, rank, row. radómand [/t?^wmnd] having a rad. rad-passag [/tps’k'] ceremonies of the gáhanbar festivals. radunay [/twny = Av. ratunaya-] one under the guidance of a rad. raftan, raw- [SGY TWN-tn! < А V sg’; lwb- | M rptn, rw-, N ~] go, move, proceed. ~išn, v. rawišn. raftār [/pt?] | N ~] goer. rag А! | M rg, N ~] vein. «ЛЬ: disposition, character. ray [/gy | P rg] quick, swift. ray [Pg | N —] meadow, plain. rah [/s, lh, [hy | M rh(y)] chariot, wagon. rah-, у. rastan. rah [Ps | M rh, N ~] road, way. rahag [/hk! | P rhg] = rag. rāh-dār [lsd] | N ~] brigand, highway robber. ~ih: brigandage. rahig [/syk!, Ikyk' | M rhyg, N rahi] child, page. ~ih: childhood. rāh-nimāy [Psnm?d | (M r’-hnmwd’r), № ~numa] guide. ram [Pm | М әт, N ~] peace; cal. 21st day. ram(ag) [/m(k') | P rm, N ram(a)] herd, flock. ráménidan, rāmēn- [Pmyn-ytn! | M ?myn-] give peace, pleasure. rāmišn [P min! | M rmyfn, N rāmi$] peace, ease, pleasure. ~ig [-vk! | N —z#] peaceful, at ease. ran [Рп! | N ~] thigh. P rān- [/^n-] fight. randidan, rand- [/nd-ytn! | N —] scratch, grate, abrade. rang [/ng | M rng, N —] colour, dye. ranj [Inc | P rnj, (M rnz), N ~] toil, trouble. ~ag [-k' | N —a] troubled. ranjénidan, ranjén- [/ncyn-ytn'] trouble.
605:wad-baxt [wtP ht! | N badbaxt] unfortunate. wad-dil [wtdyl | M wddyl, N baddil] coward(ly). wadgarih [wtglyh] evil-doing. wād-ģirdaģ [w° tgltk' | (N gird-bād)] whirlwind. wad-góhr [wtgwhl | N bad-gauhar] ill-, low-born. wad-kamag [wtk’mk'] malevolent. ~ih: malevolence. wadrang [w’ ting | N bādrang] citron. cc Dë [-bwd | N -bóya] lemon balm. wad|-tóhm [wttwhm] = wad-góhr. ~-wazag [-w’ck! | (N gawāža)] abuse. --.Xém [-hym] ill-natured. waf- [wp- | Р wf-, (N bàf-)] weave. ~išn: weaving. wafr [wp! | M wpr, N barf] snow. ~énag [-ynk!] а sweetmeat. waydān [wy?n! = Av. waybana-] head (ahuric). wahāg [wP?k! | M тор, N baha] trading; value. — burdan: value, estimate. wahār [wh], (bj?l) | M wkr, № bahar] spring. ~ig [-уЁ! | N -z] spring, vernal. wahig [ZZLA < A Semi (?); whyk' | M whyg, N *bahi] kid; astr. Capricorn. wahist [ол | M whyst, N bihist] paradise. ~Ig [-yk! | N -1] (worthy) of paradise. Wahman [whwmn' | M whmn, N bahman] Good Mind, the first Amahra- spand, guardian of cattle; cal. 11th month; 2nd day. wāhmān [*w-n! = whmn' | MOw^hmn, J whmn, N bahman] so-and-so. Wahrām [wlhl?’n', whPm | M whr’m, N bahram] god of war, victory; astr. Mars; cal. zoth day. ātaxš 1~: a major sacred fire. wak [wk! | N bak] frog. wālan [zo n! | (IN barzan)] settlement, community walg [wlg] = warg. walidan, wāl- [w]-ytn! | N bdlidan] grow, increase, prosper. ~išn: growth. wümidan, wam- [w’m-yin'] vomit. wan [wn' | N bun] tree; stock, stem. ~ i $urgünig : pistachio tree. ~ 1 was-téhmag: the Tree of Many Seeds. wān-, ~išn, v. wanidan. wanafšag [zvnpšk! | N bunafša) violet. Wanand [wnnd] astr. Vega. wandaģ [wndk'] rope, cord. wang [KALA < А ql’; wng | = M, N bang] voice, cry. wānīdan, wan- [wn-ytn! | M w’n-yst] conquer, overcome, destroy.
4939:1% rēš rēšīdan rēšag rēšk��n rēškēnīh ristag ridan rédak raw- ruwanig ruwan rawagih rawágén- rawagénidan rawag rawišnīh rawišn rang 1-3r6y
5212:wigrad wigridan nerang n��rógómand nerog nilopal nirmadomand nirmad ncm, wem wūmār wēmārīh nēmasp wimand wimandómand wimandig wimustan nemag ncmroz ncmtan niság wisbed
5241:wasswarih naxsag waxšišn wahistig wahišt wüdám ` wādgirdag wād wādrang wüdrangboy wādbān nabānazdišt tāt
5370:darridan m К ey grēh PV drahnāy p" m druxtan wey da grawih җә уў» dro, 1-2ргам у» drang E » druwand 2 iD druwandih ҷу» >

=== PHD_mackenzie
57:the stranger to Pahlavi of the necessity of covering what is now
347:   The main entries, with two exceptions, are arranged throughout
740:  -- wirastan: rearrange.
814:abrang ['plng I N aurang] glory, splendour.
1100:an-erang [)n)ylng] blameless.
1113:anOdag [)nwtk' I M )nwdg] strange, alien.
1159:arastan, aray- [)l'stn', 'l'd- IN....,] prepare, arrange, adorn.
1160: ....,isn: arrangement, adornment.
1550:beganag [byk)nk I N ......a] strange; stranger.
1748: ~atrang [ctlng I (Ar. latranJ)] chess.
2047:dran~ [d1ng I N dirang] period, duration.
2217:erang [)ylng] blame, condemnation; error, heresy.
2218: --ih: = erang.
2853:Harborz [hlbwle I N Alburz] the mountain range surrounding the world.
3709:nerang [nylng 1 N --] incantation, charm, spell.
4162:        arrange, adorn.
4335: rang [lng I M_rng, N ......] colour, dye.
4367:rayenag [l'dyn'k l I M r'yn'g] arranger.
4368:rayenidan, rayen- Wdyn-ytn l I M r'yn-ydn] lead, direct, arrange,
4370:  -iAn: action, function; arrangement.
```


## [2026-09-14T01:13:30.729Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB rang\"; grep -n \"rang\\b\\|erang\" HUB.txt | head -30",
 "description": "Grep Hübschmann for rang"
}
```


### [2026-09-14T01:13:30.833Z] TOOL RESULT

```
=== HUB rang
209:'Temperament*, Matlkan i catrang § 13) , amiza 'commixtus, coitus,
599:133. Np. . aurang (so , resp. jetzt durdng gesprochen,
601:Nebenform afrang und zahlreichen Nebenbedeutungen
678:oder vacUan)^) zu lesen, vgl. Matikan i catrang § 21,
684:von bddrang nennt Vuller's noch vOrang (= maz.
687:meris', vgl. afgh. LW. badrang a kind of cucumber*.
690:vcUrang.
2551:erwahnte np. sa Tribut = phi. sak (Matikan i 5atrang,
5068:Panther (aus *pulang) = afgh. prang *a tiger, a panther,
5426:212, zd. vdta-; bddrang 'Citrone =^ phi. vatrang\ badam
5613:Velum*; variing *Gurke, Citrone', np. badrang, balang, va-
5614:rang, phi. latrang?; vars *Haar' = phi. vars; vaver, vave-
7871:329); ap. Zaranka- = np. Zarang (arab. Zaranj Hauptstadt
8536:taiig 61. and Ind. 121 ; rang 'Bergschaf -^ skr. rankii- ;
8821:u. s. w. ; erang 'Farbe' = np. rang; zangapan *Beinschiene',
9642:p. 20, Nr. 133. Vgl. phi. awrang (gescbrieben aprang) 'Pomp',
9643:MatikSn i 5atrang p. 5, § 20, Z. 11, das man
10281:aurang 20, 269.
10297:bddrang 22.
```


## [2026-09-14T01:13:37.591Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} {n++; if (index($0,\"rang [/ng | M rng\")>0) print \"PHD leaf(1-based)\",n, \"=> printed p.\", n-1-21}' PHD.txt; echo \"=== HUB context 8815-8830\"; sed -n '8810,8830p' HUB.txt",
 "description": "Locate PHD page and HUB context"
}
```


### [2026-09-14T01:13:38.709Z] TOOL RESULT

```
PHD leaf(1-based) 96 => printed p. 74
=== HUB context 8815-8830
gulu *Kehle', zd. garah-; gulula 'Kugel* H. 929; gand 'Ge-
stank', zd. gainti-; gandum 'Weizen, skr. godhuma-; gunda
'Hefenballen', zd. gunda-; gos 'Ohr ^= ap. gausa-; gun
'Farbe* == zd. gaona-; guh 'Sehmutz, Koth* = zd. guda-;
gohar 'Ursprung H. 948, oben p. 96; ges^ gesU 'Locken\
zd. ga^sa-; gehan *Welt* = zd. gaedanqm (gen.pl.); angust
'Finger, Zehe' = zd. angiista-; angist 'Kohle', vgl. skr. an-
gdra- ; bang 'Bilsenkraut* — skr. bhanga- ; 7'ang 'Farbe' =
skr. rafiga-.
Im Armenischen stelit hier ebenfalls g: gah 'Thron,
Sessel*; ganj 'Schatz* = np. ganj\ goin 'Farbe*, ^rat; 'Pfand*
u. s. w. ; erang 'Farbe' = np. rang; zangapan *Beinschiene',
zd. zanga- 'Knochel'.
Das anlautende y von yund 'Menge, Sehaar H. 805,
oben p. 83 kann ich nicht erklaren.— 247
§ 139. Ap. g nach Vokalen und r = y bleibt im
Np. als }': mury 'Vogel' ^= zd. mereya-; mary 'Wiese'
(oben p. 98) = zd. mareya- ; may profunditas*, mayak
Grube* H. 985 ■= zd. maya- Xoch*; muy^ may *Magier
= ap. magu' (= tnayii'); mey *Wolke* = zd. maeya--^ arDy,
aroq 'Rulpsen', gr. iotvyo^iai; dyardan 'deglutire'? H. 36;
```


## [2026-09-14T01:13:43.329Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^lac,\\|^lacquer\\|^lac \\|^shellac\\|^lakh\\|^lac\" KLN_1966.txt | head -20",
 "description": "Grep Klein for lac"
}
```


### [2026-09-14T01:13:43.393Z] TOOL RESULT

```
10182:lachrymal.
20948:lace,  n.  —  ME.  las,  lace,  fr.  OF.  taz,  las  (F.  lacs), ‘noose,  snare',  fr.  L.  laqueus,  of  s.m.  (whence also  It.  laccio,  Sp.  lazo),  fr.  Italic  base  *laq-,  ‘to ensnare',  whence  also  L.  lacere,  ‘to  entice’,  deli- cere,  ‘to  entice,  allure,  delight’.  Cp.  F.  lacet, ‘lace,  noose,  snare',  dimin.  of  lacs.  Cp.  also lasso,  which  is  a  doublet  of  lace.  Cp.  also  lash, ‘to  bind’,  latchet,  delectation,  delicate,  delicious, delight,  elicit,  enlace,  IUicium,  interlace. Derivatives:  lac-y,  adj.,  laci-ly,  adv.,  laci-ness,  n. lace,  tr.  and  intr.  v.  —  ME.  lacen,  fr.  OF.  lacier (F.  lacer),  fr.  OF.  laz,  las.  See  lace,  n. Derivatives:  lac-ed,  adj.,  lac-ing,  n. Lacedaemonian,  also  Lacedemonian,  adj.,  of,  or pertaining  to,  Lacedaemon  or  Sparta;  n.,  a Lacedaemonian  or  Spartan.  —  Formed  with  suff. -ian  fr.  L.  Lacedaemonius,  fr.  Gk.  AcoceSat-
20952:lacertian,  adj.,  pertaining  to  lizards.  —  Formed with  suff.  -ian  fr.  L.  lacertus,  lacerta.  See  prec. word.
20956:lacertilian,  adj.,  pertaining  to  the  Lacertilia.  — Formed  from  prec.  word  with  suff.  -an. Derivative:  lacertilian,  n.,  one  of  the  Lacertilia. laches,  n.,  remissness  in  asserting  a  right.  —  ME. lachesse,  fr.  OF.  laschesse,  fr.  lasche  (F.  Idche), ‘loose,  slack’,  fr.VL.  *lascus  (whence  also  O Prov¬ en?.  lasc),  which  was  formed — through  the metathesis  of  i  (=  cs)  into  sc — fr.  L.  laxus, ‘wide,  loose,  open’.  See  lax  and  cp.  lash,  ‘soft and  watery’.  The  regular  E.  equivalent  of  the  F. suff.  -esse  is  -ess  (q.v.);  laches  (with  a  single  -s) forms  an  exception  to  this  rule  (cp.  riches). Lachesis,  n.,  one  of  the  Fates  in  Greek  mythol¬ ogy.  —  L.,  fr.  Gk.  Aaxeatc;,  lit.  ‘the  appor¬ tioned  disposer  of  lots’,  fr.  XayeTv,  aor.  II  inf.  of Xa YX.avetv,  ‘to  obtain  by  lot’ ;  of  uncertain  ori¬ gin.
20959:lactase
20964:laciniate,  laciniated,  adj.  —  Formed  from  prec. word  with  adj.  suff.  -ate,  resp.  also  1st  -ed. Derivative:  laciniat-ion,  n. lacinula,  n.,  a  small  Iacinia  (bot.  and  zool.)  — - ModL.,  dimin.  of  Iacinia.  For  the  ending  see suff.  -ule.
20966:lack,  tr.  and  intr.  v.  —  Either  fr.  lack,  n.,  or  fr. MDu.  laken,  ‘to  be  wanting;  to  blame’,  which  is rel.  to  MDu.  lac.
20967:lackadaisical,  adj.,  listless.  —  Formed  from  the interj.  lackadaisv,  fr.  lackaday;  coined  by  the English  novelist  Laurence  Sterne  (1713-68). lackaday,  interj.  —  Aphetic  form  of  alack-a-day.
20973:laconism,  n.,  1)  laconic  (i.e.  brief)  way  of  expres¬ sion;  2)  a  laconic  utterance.  —  MF  (=  F.)  la- conisme,  fr.  Gk.  Aocxomcrp.oi;,  ‘imitation  of  the Lacedaemonians,  laconism’,  from  the  stem  of Aaxom^Etv.  See  next  word  and  -ism. laconize,  tr.  and  intr.  v.,  to  imitate  the  Lacedae¬ monians.  —  Gk.  AaxamCsiv,  ‘to  imitate  the Lacedaemonians  (in  dress,  manners  etc.)’,  fr. Aaxcov,  ‘Laconian,  Lacedaemonian,  Spartan’. See  Laconic  and  -ize.
20974:lacquer,  lacker,  n.,  a  kind  of  varnish.  —  MF. lacre,  fr.  Port,  lacre,  ‘sealing  wax’,  fr.  laca,  ‘gum lac',  which  derives  fr.  Hind,  lakh,  ‘lac’,  fr.  OI. lak.;b,  See  lac,  ‘a  resinous  substance'. Derivatives:  lacquer,  tr.  v.,  lacquer-er,  n.,  lac- quer-ing,  n.
20975:lacquey,  n.  —  A  var.  of  lackey, lacrima],  adj.  —  See  lachrymal, lacrimatory,  adj.  —  See  lachrymatory, lacroixite,  n.,  a  complex  basic  fluophosphate (mineral.)  —  Named  after  the  French  mineralo¬ gist  Frangois-Antoine- Alfred  Lacroix  (1863- 1948).  For  the  ending  see  subst.  suff.  -ite. lacrosse,  n.,  a  game  in  which  a  ball  is  thrown  by means  of  a  long-handled  racket,  the  crosse.  —  F. la  crosse,  ‘the  crozier,  the  racket  used  in  certain games’,  fr.  fern.  def.  article  la  (fr.  L.  ilia,  fem.  of ille,  ‘that’)  and  WTeut.  *krukja,  ‘crutch’.  See ille  and  crutch  and  cp.  crosse,  crossette,  crosier, lactarene,  also  lactarine,  n.,  material  made  from casein  of  milk,  used  in  calico  printing.  —  Form¬ ed  with  suff.  -ene,  resp.  -ine,  fr.  L.  lac,  gen.  lac- tis,  ‘milk’.  See  lacteal.
20977:lactase,  n.,  an  enzyme  capable  of  decomposing lactose  (biochem.)  —  Formed  with  suff.  -ase  fr. L.  lac,  gen.  lactis,  ‘milk’.  See  lacteal,  adj.
20978:lactate
20980:lactate,  intr.  v.,  to  secrete  milk  (rare).  —  L.  lac- tatus ,  pp.  of  lactare,  ‘to  contain  milk;  to  suckle young’,  fr.  lac,  gen.  lactis,  ‘milk’.  See  lacteal, adj.,  and  verbal  sufF.  -ate. lactate,  n.,  a  salt  of  lactic  acid  ( chem .)  —  See  lac¬ tate,  v.
20981:lactation,  n.  • —  Late  L.  lactdtid,  gen.  -dnis, ‘a  suckling’  [prob.  through  the  medium  of  MF. (=  F.)  lactation],  fr.  L.  lactatus,  pp.  of  lactare. See  lactate,  v.,  and  -ion.
20983:lactesce,  intr.  v.,  to  become  milky.  —  L.  lacte- scere,  'to  become  milky’,  inchoative  of  lactere, ‘to  contain  milk,  be  milky’,  fr.  lac,  gen.  lactis. See  lacteal,  adj.,  and  -esce. lactescence,  n.,  the  process  of  becoming  milky.  — Formed  from  next  word  with  suff.  -ce. lactescent,  adj.,  becoming  milky.  —  L.  lactescens, gen.  -entis,  pres.  part,  of  lactescere,  ‘to  become milky’.  See  lactesce  and  -ent. lacti-,  combining  form  meaning  ‘milk,  milky, milklike’.  —  L.  lacti-,  fr.  lac,  gen.  lactis,  ‘milk’. See  lacteal,  adj.
20984:lactic,  adj.,  pertaining  to  milk  (used  in  chemistry). —  Formed  with  suff.  -ic  fr.  L.  lac,  gen.  lactis, ‘milk’.  See  lacteal,  adj.,  and  -ic  and  cp.  galactic, lactide,  n.,  a  compound  formed  from  lactic  acid (chem.)  —  Formed  with  suff.  -ide  fr.  L.  lac,  gen. lactis,  ‘milk’.  See  lacteal,  adj. lactiferous,  adj.,  yielding  milk.  —  Compounded of  lacti-  and  L.ferre,  ‘to  bear,  carry’.  See-ferous. lacto-,  combining  form  meaning  ‘milk’.  —  Fr.  L.
20985:lac,  gen.  lactis,  ‘milk’.  See  lacteal,  adj. lactometer,  n.,  an  instrument  for  measuring  the purity  of  milk.  —  A  hybrid  coined  fr.  L.  lac, gen.  lactis,  ‘milk’,  and  Gk.  pcrpov,  ‘measure’. See  lacteal,  adj.,  and  meter,  ‘poetical  rhythm’. The  correct  form  is  galactometer  (q.v.),  in which  both  elements  are  of  Greek  origin, lactose,  n.,  sugar  of  milk  (chem.)  —  Coined  by the  French  chemist  Marcclin-Picrrc-Eugene Berthelot  (1827-1907)  fr.  L.  lac,  gen.  lactis, ‘milk’  (see  lacteal,  adj.),  and  subst.  suff.  -ose. lacuna,  n.,  a  gap.  —  L.  lacuna,  ‘ditch,  pit,  pool, pond,  hole,  hollow,  cavity’,  dimin.  of  lacus,  ‘ba¬ sin,  tank,  tub,  a  large  reservoir  for  water,  lake’. See  lake,  ‘pool’,  and  cp.  lagoon.
20991:lacustrine,  adj.,  pertaining  to  a  lake.  —  Prob.  fr. F.  lacustre,  which  was  formed  fr.  L.  lacus,  ‘lake,’ on  analogy  of  paluster,  ‘marshy,  swampy’  (fr. palus,  ‘marsh,  swamp’).  See  lake,  ‘pool’,  and adj.  suff.  -ine.
21027:lakh
```


## [2026-09-14T01:13:44.371Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"^LAC\\|^LACQUER\\|lakh\\|shellac\" SKT.txt | head -20",
 "description": "Grep Skeat for lac"
}
```


### [2026-09-14T01:13:44.436Z] TOOL RESULT

```
1935:Block,  alarceiikceoiwooiL  *.C)  I ^/^..W.  pite,  a  block;  GarL  aidl /^or.  a  block,  romd  aM^  ti^iVh Cf.  Irish  kbgk,  a  fncncoU  O.  Irofcl fragment.     Henoe  alto  Do.  *.^ Swed.  */*-*,    O.  H   G.  b' plakha.     Doublet.  ti»£.     1
3571:lack.
9809:lac;  put  for  raA/d,  lac.  ••  Skt. yp.  of  roAj't  to  dye,  colonr.  redden  ; .  rm^ffOt  colonr,  paint-  Der.  gitm- f-iae.
9837:Laconic,  brief  and  pithy.  (L.  *  Gk.) L.  LaionicHs,  Laconian.  ~  Gk.  Aacaifunir^ Lacooian.*  Gk.  AtUarv.a  Lacoai&n,  Spartan. These  men  wee  celcbrBtcd  for  their  brief and  pithy  locution.
9838:Lacquer;  see  Loo  (i)-
9839:Lacteal.  relRting  to  milk.  (L.)  From L.  lactt-us,  milky.  ••  L.  Ifut-^  stem  of  lac^ milk,  -^  Gk.  ToAturr-,  stem  of  70^0,  milk* Root  unknown.
10035:wiik  ffrfb  -iA  (A.S  -^ •oleic  Tcr^  iasc,  to  poar  oat. water;  M.  E.  Jbw^,  lo  bak  oi ■hat  Ifcc  ■rtMfc'nW  we  of Ci^boHiaMlr.  'UciawsbTsi God  towrfff  Hfa  sifti:  AlKt. 607.  kaB«ostoA.S;. (a  doabtial  vocd  ■ 17221:  Da.  f— w,  G.  iriim,  10 CC  Gk.  AotACmt.  to  ani<7  g«L  ^  *^ woni »  slaKHl  ceitaialy-  E^  bat  «aa  pfi early  Goalased  with /na.  DafcJMW^w
23087:lace— lasso.
```


## [2026-09-14T01:13:55.417Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"resinous  substance\\|lakh,  n\\|lac,  n\" KLN_1966.txt | head -10; echo \"=== leaf of lacquer\"; awk 'BEGIN{RS=\"\\f\"} {n++; if (index($0,\"lacquer,  lacker,  n.\")>0) print \"KLN leaf\",n}' KLN_1966.txt",
 "description": "Find Klein lac entry"
}
```


### [2026-09-14T01:13:56.582Z] TOOL RESULT

```
9942:curacy,  n.  —  Formed  fr.  curate  with  suff.  -cy. curare,  curari,  n.,  a  blackish  resinous  substance used  by  the  Indians  as  arrow  poison.  —  Fr. Tupi  urari,  lit.  ‘he  to  whom  it  comes  falls’.  Cp. ourali,  woorali.
15701:named  after  the  Spanish  botanist  Mariano Martinez  de  Galinsoga  (died  in  1 797). galiot,  galliot,  n.,  a  small  swift  galley.  —  F. galiote,  fr.  OF.  galie.  See  galley, galipot,  gallipot,  n.,  resinous  substance  of  certain pines.  —  F.  galipot,  of  unknown  origin. Galium,  n.,  a  genus  of  plants,  the  bedstraw  (hot.) —  ModL.,  fr.  Gk.  yotliov,  ‘bedstraw’,  coined  by Dioscorides  fr.  yaXoc,  ‘milk’  (see  galactic);  so called  by  him  because  used  in  place  of  rennet. For  the  ending  see  suff.  -ium. gall,  n„  bile.  —  ME.  galie,  gawle,  fr.  OE.  gealla, galla,  rel.  to  ON.  gall,  OS.,  OHG.  galla,  MHG., G.  galie,  and  cogn.  with  Gk.  /oAr),  L.  fel,  fr.  I.-E. base  *ghel-,  ‘to  shine;  yellow,  yellowish  green, green’.  See  choler  and  cp.  words  there  referred  to. gall,  n.,  gallnut.  —  F.  galie,  fr.  L.  galla,  ‘gallnut’, prop,  ‘a  globulous  excrescence’,  fr.  I.-E.  base *gel-,  ‘to  form  into  a  ball’.  See  glebe,  globe, and  cp.  ellagic.
20947:Derivative:  labyrinthical-ly,  adv. labyrinthitis,  n.,  inflammation  of  the  labyrinth (med.)  —  Medical  L.,  formed  fr.  L.  labyrinthus (see  labyrinth)  with  suff.  -itis. lac, lakh,  n.,  1)  one  hundred  thousand;  2)  a  great number.  —  Pers.  lak,  fr.  Hind,  lakh,  ult.  fr.  OI. Idkfa,  ‘one  hundred  thousand’,  prop,  ‘sign, mark’,  rel.  to  Uksati,  laksayati,  ‘marks,  charac¬ terizes,  defines’,  and  prob.  also  to  rdkyd,  ‘pro¬ tection,  deliverance,  preservation,  observation’, rak$ati,  ‘protects,  delivers,  preserves,  observes’, and  cogn.  with  Gk.  dXi'Eiv,  aX£xsiv,  ‘to  ward off.  See  Alexander  and  cp.  Lakshmi. lac,  n.,  a  red  resinous  substance.  —  Pers.  lak,  fr. Hind,  lakh,  fr.  OI.  lakfa,  lit.  ‘one  hundred thousand’  (see  prec.  word),  a  name  given  to  the insects  Cocca  ilicis,  in  allusion  to  their  great number.  Their  name  is  used  also  to  denote  the resin  of  the  Quercus  cocci/era,  which  flows  from this  tree  in  consequence  of  the  sting  of  these insects.  Cp.  lacquer  and  the  second  element  in shellac.  Cp.  also  the  second  element  in  Phyto¬ lacca.
20974:lacquer,  lacker,  n.,  a  kind  of  varnish.  —  MF. lacre,  fr.  Port,  lacre,  ‘sealing  wax’,  fr.  laca,  ‘gum lac',  which  derives  fr.  Hind,  lakh,  ‘lac’,  fr.  OI. lak.;b,  See  lac,  ‘a  resinous  substance'. Derivatives:  lacquer,  tr.  v.,  lacquer-er,  n.,  lac- quer-ing,  n.
21031:lakh,  n.  —  See  lac,  ‘one  hundred  thousand  (ru¬ pees)’.
21740:lilac,  n.  —  MF.,  fr.  Sp.  lilac,  fr.  Arab,  ldylak,  lilak, fr.  Pers.  lilak,  var.  of  nilak,  ‘bluish’,  fr.  nil,  ‘blue, indigo’,  fr.  OI.  nilah,  ‘dark  blue’,  which  is  of  un¬ certain  etymology.  It  possibly  derives  fr.  I.-E.
27072:paludic,  adj.,  paludal.  —  Formed  with  adj.  suff. -ic  fr.L.  palus,  gen.  paludis,  ‘marsh’.  See  paludal. Paludicella,  n.,  a  genus  of  polyzoans  (zool)  — ModL.,  compounded  of  L.  palus,  gen.  paludis, ‘marsh’,  and  cella,  ‘cell’.  See  paludal  and  cell. Paludicolac,  n.  pi.,  an  order  of  birds;  also  called Gruiformes  (ornithol)  —  ModL.,  lit.  ‘inhabi¬ tants  of  marshes’,  fr.  L.  palus,  gen.  paludis, ‘marsh’,  and  colere,  ‘to  inhabit’.  See  paludal  and cult.
27758:Derivatives:  pay,  n.  (q.v.),  pay-able,  adj.,  pay¬ ee,  n.,  pay-er ,  n.,  pay-ing,  n.,  payment  (q.v.) pay,  n.  —  ME.  paye,  pay,  fr.  OF.  paie  (F.  paye), back  formation  fr.  paler,  paer.  See  prec.  word, pay,  tr.  v.,  to  coat  with  pitch  (naut.)  —  Obsol.  F. peier,  ‘to  coat  with  pitch’,  fr.  OF.  pe’ier,  fr.  L. piedre,  fr.  pix,  gen,  picis,  ‘pitch’,  which  is  cogn. with  Gk.  Ttiaaot,  (for  *7tixia),  ‘pitch’.  See  pitch, ‘a  resinous  substance’.
28378:Pete,  n.  —  Dimin.  of  Peter, petechia,  n.,  one  of  a  number  of  small  crimson or  purplish  spots  on  the  skin  ( med .)  —  Medical L.,  fr.  It.  petecchia,  ‘speck’,  which  prob.  derives fr.  Gk.  riT-rdixiov,  ‘tablet  for  writing  on,  label, ticket;  plaster’,  dimin.  formed  fr.  ttiTTa,  t uaax, ‘pitch’,  which  is  cogn.  with  L.  pix,  gen.  picis, ‘pitch’.  See  pitch,  ‘a  resinous  substance’. Derivatives:  petechi-al,  petechi-ate,  adjs.
28718:Phytolacca,  n.,  a  genus  of  plants,  the  pokeweed (bot.)  —  A  ModL.  hybrid  coined  fr.  Gk.  9UT0V, ‘plant’  and  ModL.  lacca,  fr.  Hind.  lakh.  See phyto-  and  lac,  ‘a  resinous  substance’. Phytolaccaceae,  n.  pi.,  the  pokeweed  family  (bot.)
=== leaf of lacquer
KLN leaf 462
```


## [2026-09-14T01:13:57.011Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} {n++; if (index($0,\"lac;  put  for\")>0) print \"SKT leaf\",n, \"printed p.\", n-1-20}' SKT.txt; sed -n '9800,9815p' SKT.txt",
 "description": "Find Skeat lac page"
}
```


### [2026-09-14T01:13:58.113Z] TOOL RESULT

```
SKT leaf 259 printed p. 238
labiate.  (L.)     A  botnnical  lerm.  *  L. hh  urn,  a  Up:  with  suffix  aft  (L.  -o/aa). Laboratory ;  see  Labour. Iiabotir.  toil.    (F.  -  L)     M.  E.  /a/wir. —  O.  F.  /a/>citr  (later  /a/ri*r).-L.  lahcrtfHt ace  of  /0i^r,  /ii^M,  toil.     Allied  to  rvdur, itivnpth.     (v^RABU.) bwabotiP.  (F.  -  L.  I  with  t^prtJU,)
Coined  by  prefiring  E.  ir-  («*r1  *» ia^tmr,  a  word  of  K.  origin  (•bow,
elaborate.  (Ui     I.-  riahoratm,  pp tlahorart,  lo  labour  greatly.  —  I-  /. greatly;    Uhcf-art,  to  work,  froia labour.
laboratory.    (L.^      Formerly /»f7  (Blount  r.  *  O.  F.  f/it/vm/MWj Formed   from  L.  tiatternim^  pp. ni'T,  to  cUtiOfate,  work  oat,
laborioua.  (F.  -  L)  M.  E  ' ritms.  •  F.  hbontux.  —  L..  4i»rt toilsome.  — L^  /isAfln-,  crude  £atm  i^i la  boor.
LABURNUM.
atiee.  (I.)    h,  Mmrmtm, ^  xvi.  l8.  fcthApi^a/&urrtum, rinth.  a.  muc.  /F.  -  L.  -  Gk.) rintkt.  ••  L.  Iaf>yrinthHS.  •  Gk.Xa- r.  «  mue.  a  pUce  full  of  Unes  or
Pet  for  kafvpt»9oti    Irom  Ktxfpn, >iQi/pa,  ft  lane. (1),  a  rninuttft  substance.  (Pert.—
Pen.  /ai«  /«>,  gum-Uc,  whence t  lake  is  obtained  for  dyeing.  —  Skt.
lac;  put  for  raA/d,  lac.  ••  Skt. yp.  of  roAj't  to  dye,  colonr.  redden  ; .  rm^ffOt  colonr,  paint-  Der.  gitm- f-iae.
tiar,  looker,  a  sort  of  vamith.  (F. -Pctv-Skt.)  F.  lacn  (Cot.V- errv.  icatini^'Wax.  — Port,  laca,  gum- en  la^,  gum  lac  (above).
I  (}),  a  crimsoD  colour.   (F.  — Pen.
K  iaque  i.Cot. )  —  Pers.  idk,  lake. Zai,  gain-lac  (above). \j\  %  hundred   thouMind.  (Hind.*
Imni  iai  <  alw  t4Mh),  a  lac  -  bkt. ft   hundred    thou&and;    appatently Cemce  to  the  number  of  lac-insccti It ;  see  I*ao  ( i ).
.  a  cord,  lic.   (F.-L)     M.  E.  iai, 0.  F. /ar,  /o^i,  a,  snare,  noose. —  L. -,  a  ncoic,  ariare,  knot.     Allied  to T,  to  allnre;  <f.  E.  tlicit,  dt light. t>.  a  noose.  (Spnn.  —  L.)
EL  lu):  mod.  bpan  toio,
```


## [2026-09-14T01:14:12.772Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} {n++; if (n>=456 && n<=463) {print \"----LEAF\",n; print substr($0,1,300)}}' KLN_1966.txt",
 "description": "Print Klein leaves 456-463 heads"
}
```


### [2026-09-14T01:14:13.860Z] TOOL RESULT

```
----LEAF 456
‘stalk,  blade’, Lett,  zeiju,  ziet,  ‘to  rise’  (said  of  flowers;  also fig.)  See  chine,  ‘valley’,  and  chink,  ‘crack’.
key,  tr.  and  intr.  v.  —  ME.  keyen ,  fr.  key ,  keye, ‘key’.  See  key,  n. key,  n.  —  A  var.  of  quay.
Keziah,  i)  fern.  PN.;  2)  
----LEAF 457
 n.,  a  kind  of  East  Indian  brocade.
Hind,  kimkhab,  fr.  Pers.  kimkhdb. kind,  n.  —  ME.  kinde,  kund,  kende,  fr.  OE.  cynd, ge-cynd,  ‘kind,  nature,  quality,  manner,  origin, generation,  offspring’,  rel.  to  OE.  cyn,  ‘kind, kin’.  See  kin  and  cp.  kind,  adj. kind,
----LEAF 458
yoav,  ‘to  wail, groan,  weep’,  yooq,  ‘wailing,  groaning,  weeping’, OE.  cyme,  ‘fine,  beautiful,  splendid’,  orig.  ‘frail, delicate,  tender’.  See  comely, kith,  n.,  now  used  only  in  the  phrase  kith  and  kin. —  ME.  cuththe,  kith,  fr.  OE.  cydd(u)-,  ‘know�
----LEAF 459
f  a  small  hill.  —  ME.  knot,  fr.  OE. cnoll,  ‘hill  top,  hill’,  rel.  to  ON.  knollr,  ‘hilltop’, MLG.,  MHG.,  G.  knolie,  ‘clod,  glebe,  lump', Du.  knot,  ‘turnip’,  and  to  OHG.  nollo,  Du.  nol, ‘a  hill’.
Derivative:  knoll-y,  adj.
knoll,  tr.  and  intr.  v.
----LEAF 460
,  fr.  Krieg,  ‘war’,  and  Spiel,  ‘game’. The  first  element  is  of  uncertain  origin.  For  the second  element  see  spiel  and  cp.  the  second  ele¬ ment  in  bonspiel,  glockenspiel.
Krigia,  n.,  a  genus  of  plants,  the  dwarf  dandelion (bot.)  —  ModL.,  named  after  Da
----LEAF 461
pertaining  to,  or  formed  with, the  lips  and  teeth.  —  Compounded  of  labio-  and dental.
Derivative :  labiodental,  n.,  a  sound  formed  with the  lips  and  teeth.
labium,  n.,  a  lip  or  a  liplike  part  (anat.,  zool.,  bot. etc.)  —  L.,  ‘lip’.  See  labial, labor,  labou
----LEAF 462
.  lakmoes,  fr.  MDu. leecmos,  fr.  leken  (Du.  lekken ),  ‘to  drip,  leak’, and  mos  (=  Du.  moes),  ‘green  vegetables ;  pulp’. The  first  element  is  rel.  to  OE.  leccan,  ‘to  mois¬ ten,  water’ ;  see  leak.  The  second  element  is  rel. to  OE.,  OS.,  OFris.  mos,  �
----LEAF 463
-ly,  adv.,  laggard-ness,  n.
lagniappe,  n.,  gift,  gratuity.  —  Amer.  F.,  fr.  Amer. Sp.  la  hapa,  ‘the  gift’,  fr.  Sp.  la,  ‘the’,  fern,  of  el, fr.  L.  ille,  ‘that’  (see  ille),  and  Amer.  Sp.  hapa, yapa ,  ‘lagniappe’,  fr.  Quechua  yapa,  ‘something added
```


## [2026-09-14T01:14:25.438Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"shellac\\|shell-lac\" SKT.txt | head; echo \"=== leaf 300-303 heads\"; awk 'BEGIN{RS=\"\\f\"} {n++; if (n>=300 && n<=303) {print \"----LEAF\",n; print substr($0,1,200)}}' SKT.txt",
 "description": "Check Skeat shellac and leaf 300"
}
```


### [2026-09-14T01:14:26.540Z] TOOL RESULT

```
=== leaf 300-303 heads
----LEAF 300
keimtticus.  —  Gk.  fuiQi)-
posed   (o  Icam.  belonging  to
\  esp.  to  mathematics.  —  Gk.
em  of  ttii9rffia,  a  lesson.  *  Gk.
Ifetnre  of  fioffiayity,  to  leara.
Hattina;  mx-  Mature.
----LEAF 301
  as  Spaa,  dtsmajar, to  dismay,  ttrriiy.  The  O.  F.  dtsmaytr was  early  supplanted  by  esmayer  in  the tame  sense,  which  only  rtiffercd  in  substi- tuting the  prefix  cs-  ^L,  ex'\  f
----LEAF 302
lit.  sense  ii  * cf.  O.  Du.   moiffhi,   moHktt spot,  blot,'  HcJibam.    The in  M,  H.G.  mau.  O.  H. ^  Wholly  iincnnr-^  '-'   - a  leper,  which  IT' from    O.  V.    «(->    ^ miur,  wr
----LEAF 303
  tmdicus  (above)  ;  meduatt.
meditate.  <L.)  From  pp.  of  L- meditari,  to  ponder  :  a  frequent,  verb,  tap- po;»c(l  to  be  fruHi  the  uunc  base  as  mtdtri^ to  heal  (above).
remedy.
```


## [2026-09-14T01:14:48.038Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC grep rag/ranj\"; grep -n \"^rag-\\|^ranǵ\\|^rang-\\|^ranj\\|^reĝ\\|^reg-\\|^rag\\b\" IEC.txt | head -20; echo \"=== search rajidan\"; grep -n -i \"rajidan\\|razīdan\\|razidan\" IEC.txt | head",
 "description": "Grep Mann IEC"
}
```


### [2026-09-14T01:14:48.113Z] TOOL RESULT

```
=== IEC grep rag/ranj
14439:reg- (2) “reach, rule’, etc. See following entries, and especially rēĝs
=== search rajidan
```


## [2026-09-14T01:14:49.314Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: alek\\|lemma: alek-\" POK_full.txt | head; echo \"===\"; grep -n \"Page(s): 3[12]\" POK_full.txt | head",
 "description": "Find Pokorny alek-"
}
```


### [2026-09-14T01:14:49.389Z] TOOL RESULT

```
===
4140:Page(s): 31-32 
4174:Page(s): 32 
4190:Page(s): 32 
4215:Page(s): 32-33 
26251:Page(s): 310-311 
26305:Page(s): 314-315 
26409:Page(s): 315-316 
26512:Page(s): 316-318 
26614:Page(s): 318-319 
26858:Page(s): 311-314
```


## [2026-09-14T01:14:51.639Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4160,4195p' POK_full.txt",
 "description": "Print Pokorny p.32 alek-"
}
```


### [2026-09-14T01:14:51.697Z] TOOL RESULT

```
Old English ea/g/an' protect, defend ' {*algdjan)\ Gothic alhs{i., conservative stem) ' 
temple ', Old English ealh. Old Saxon a/ahm. ds., Proto Norse-Runic a/uh' amulet' (?), 
Old Lithuanian e/kas, alkas m. ' holy grove, place on a hill where one has made of early 
victims ', Latvian e/ksm. 'Idol, god' (Germanic and Baltic words originally ' holier, seclusive 
or the usufruct deprived grove '); 

Tocharian B a/55/r" remove'. 



References: WP. I 89 f. 

See also: S. similar root areg- close, protect '. 

Page(s): 32 



Root / lemma: a/gh- {* heigh-) 
Meaning: "frost, cold' 
Material: 

Latin algor' frost, cold ', algeo, -ere' freeze, to be cold ', belong algidus' co\6' according to 
Liden, studies z. Old Indie and compare Sprachgesch. 66, to Old Icelandic Gen. Sg. elgiar, 
nisi, elgurru. " snow flurry with strong frost, half-molten snow '. Germanic s-stem *a/j/z- 
disguised itself with Latin algor, Indo Germanic *alghes-. 
References: WP. I 91, WH. I 29. compare Petersson Aryan under Arm. Stud. 126. 



Page(s): 32 

Root / lemma: alg"!!- 

Meaning: 'to earn, price, value, *precious bright metal'
```


## [2026-09-14T01:14:52.419Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '14380,14460p' IEC.txt",
 "description": "Print Mann reg- area"
}
```


### [2026-09-14T01:14:52.471Z] TOOL RESULT

```
(qusür-, a possible variant for types listed
1061
under qusór-, q. v. Oss. cf. xür, Dig. xurä ‘gravel, rubble’; Icel’
rab- (rabəl-) Lat. (ambig.) rabio, ére, v. ‘rave, rage’; rabies, f. id.; MHG (ambiguous) reffen, v. ‘snatch; bully, reprimand’; cf. G raffen, v. ‘snatch’; Du. rap, adj. ‘agile’; Sw rapp, adj. ‘dashing’; LG cf. rappeln, v. ‘clatter’; Rappel, m. ‘fit, whim, freakishness'; G Raffel, f. ‘chatterbox’. (For Du. rapen, v. ‘gather’; Sw. rappa, v. ‘snatch’; G raffen, id. a prototype *krab-, q.v. is possible)
(rād- see rod-, and cf. WP II, 369)
rād- (rðd-?) ‘glad’. (Vowel ambig. in Gmc. & Sl. Cons. ambig. in Sl.) OE rot, adj. “glad; noble; excellent'; cf. rëtan, v. ‘cheer; OCS radü, adj. ('glad; willing’, and com. S1.); radi “for the sake of”; Cz. rád, adv. ‘gladly’
radh- (or rodh-?) “seek, find, get OE redian, v. ‘reach, find, effect; OCz. roditi, inf. ‘seek, want Li. cf. randü, ràsti, v. “find”; pf: radaü; cf. also radejas, m. 'finder'; Latv. rodu, rast, pf: radu, v. as Li. (Note: EME to redd ‘to save’; MHG retten, v. id. is held to derive from *krat- OT. Romani rodav “seek? equates with Hindi dhündhna, inf. id. Icel. rata, ratast ‘find the way, succeed' derives from a type *rad- or *rod-, *urad-, *urod-)
rādh- ‘show, tell, declare, speak’. WP I, 429 Olr. ro-radid, 3s. (speaks': Li. pra-ródyti 'in- dicate, suggest); Ir. rádh, pl. ráidhte, m. ‘speech, word, expression’; rádhaim, ráidhim, v. “speak, say’; OBr. cf. am-raud, s. ‘thought’; W rhawdd, m. 'clarity, perspicacity'; cf. ad- rodd, v. (tell, relate’: Li. at-Cródyti *appear); Go. rōdjan, v. ‘talk, speak’; bi-rodjan, v. *mur- mur’; ON ræða, v. ‘speak’; f. ‘conversation’; Li. ródau, yti, v. ‘show’; Latv. rādu, it, id.
raio (uraió?) ‘seethe with excitement Gk. eráo, éràmai, eráomai, v. love w. passion"; Pol. roić, v. “imagine, dream’; roic sig (and com. Sl. fswarm"); OCS roj, m. ‘swarm’ beside
rab- (rabol-) — rantis, os, us
R
10
20
25
30
35
40
45
1062
syrja, f. ‘sediment’; Li. cf. šiurkštus, adj. *rough, rugged")
Pol. zd-rój, Cz. zdroj, m. “bubbling source”. (Semantics of G schwiürmen and E swarm)
ráios, us (rói-?) ‘splendour’. Cf. WP IL 365 Av. (ambig.) rais, f. ‘glitter; OE rogian, v. ‘blossom, thrive’; ON rói, m. “rest, pause’; OHG cf. ruowa, róa, f. id. beside ruowen, rüin, v. id. OCS (and com. Sl.) raj, m. “para- dise'; Li. (LW fr. S1.?) rojus, m. id.
(rak- “noise”, etc. See Supt: R)
rameió ‘quieten, appease, pacify; rest, ac- quiesce, subside’. See following entries. Radi- cal: ram-. WP II, 372 Skt. ramáyami, v. “set at rest; rest, stay, enjoy’; (short grade in) ramáyami, v. “delight? & Av. ram-, v. ‘rest, enjoy oneself; ramaye(imi), v. ‘quieten’; ON róma, v. (1) ‘assent’; roema, v. ‘approve of; Li. romiü, Eti, v. ‘quieten; ac- quiesce' beside roméju, Eti, v. ‘subside’; (short grade in) raméju, eti, v. ‘subside, abate’; Latv. raminat, inf. ‘tame’ beside ràmit, inf. 'cas- trate’. Denom. in Gk. erémázo am deserted'
ràmos, à (ram-) ‘restful, quiet, tame, alone; rest, quietude, solitude’. WP II, 372. Cf. rā- meió Skt. ramah, ramáh, adj. (pleasant; ramah, ramam, mn. ‘delight’; Av. rāma, f. ‘rest; plea- santness'; Per. ràm, adj. ‘tame, docile’; aram, adj. (quiet; Gk. erémos, adj. ‘deserted’; cf. kh&-ramos, m. ‘hideout’; Li. romüs, ramus, adj. quiet; romà, f. ‘quietude’; Latv. råms, as Li. (A zero-grade formula of type *rm- ari- ses in Av. airime, adv. ‘restfully’ and in Skt. rátih, f. “peace, quietude’: Li. rimtis, f. id.; cf. Li. rimstu, rimti, v. ‘subside’; Latv. rimstu, rimt, id. beside rimts “quiet')
rantis, os, us “side, part Umb. (queried) randem-e rufrier (‘to the wall? side? of Rubrius’. E. Vetter: Hb. der ital. Dia- lekte, p. 235); Ir. rann, pl. rannta, f. “part: verse’; Br. rann, pl. -u, m. ‘part’; W rhan, pl. -au, f. id.; OHG rant, MHG rant, gs: randes,
1063
sm. ‘rim’; OE, OS rand, id.; ON rond, f. id.; (LW in) Finn. ranne, obl. rant-, id.
rap- (rop-?) (1). See Supt:R: rop- ON rafr, npl. rafir, m. “fatty parts of fish’; raf, n. ‘amber’; OCS Ukr. ropa, f. ‘pus. (Iso- phone: Slovene ropa ‘peat’; Blg. ròpa *hollow")
rap- (rapo, io) (2) ‘snatch’ Per. (ambig.) rabūdan, rubaidan, v. (‘seize, ravish’, cf. lab-); Lat. rapio, Gre v. ‘seize, snatch’; LG raffen, v. id. beside raffig ‘greedy’; Icel. refja, v. ‘defraud’; Slovene rópati, inf. ‘plunder’; Srb. cf. ropac, m. 'death-throes'. (NB. For High Ger. raffen, LG rapen see rab-)
rāp- (1) ‘creep’. Cf. rep-, róp-. WP II, 370 OE cf wudu-rofe, f. ‘woodruff; Li. ropà, ‘creeper, reptile; beside ropóju, -óti, v. ‘creep, crawl; Latv. rapus, adj. ‘creeping’, cf. rapu, adv. *creepingly'; rāpulis, s. ‘crawler, climber’
ràp- (rápà, is, io, us) (2) 'taproot'. WP II, 341 Per. cf. rafe “a plant resembling garlic'; Lat. rapa, f. ‘rape’; OHG ruoba, f. ‘taproot’; MHG ruobe, rüebe, wf. id.; ON cf. rófa, f. ‘coccyx; mod. rófa, f. ‘taproot’; rófu-bein 'rump-bone'; Li. rópe, f. ‘taproot, turnip’
rapsió (rapotio) 'shout, bluster, bully’. (Vari- ant rasp-) OHG refsen, MHG refsen & respen, v. ‘bully’; OE repsan, v. ‘blame’; ON refsa, v. (“punish?. NB: ON has both -fs- and -ps- as reflexes of IE *-ps-, cf. the parallel raftr & raptr 'rafter'); Srb. cf. ropcem, roptati, v. ‘brawl’; Blg. ropščà, roptàja, id.; OHG cf. rafsunga, s. ‘blame’ and Sw. räfst, m. ‘reproof
rár-, see rór-. Short vowel in Scots rair, rare, v. roar’, in phr: raring to go); Li. raruoti, inf. id.
rásó, ið ‘roar, rush, shout’. WP II, 342. Cf. rés- Skt. rasàmi, rase, v. ‘roar’; rasanam, n. ‘roar, roaring’; Av. ráh-, ‘resound; praise’; Scots to raize, v. ‘to madden’ beside E dial. to rooze, v. ‘roar — of a fire’; Du. cf. roes, m. “tipsiness'; ON rasa, v. ‘rush’ beside ras, n. “race, dash’; Sw. rasa, v. (2) ‘rave, rage"; ras, n. ('din; exu- berance', but rosa, v. ‘praise’; Norw. rose, id. beside Sw. ros, pl. -er, f. ‘praise?’ are from a
rap- (rop-?) — rëdh-
20
25
30
35
40
45
1064
type *kràs-, see this and cf. Supt: RK: kras-). Extns. in Skt. rasitám, n. ‘noise’; Go. razda, f. ‘speech’; OHG rasta, f. id.; OE reord, fn. id.; ON rodd, f., cpds: radd-, id.; cf. also răst- in Skt. ratami ‘bawl, braw?!; Icel. rósta, f. ‘brawl beside ON rost, f. u-stem (1) “race, current’. (For MHG ràsen, see rés-)
(rát-, see rət- and cf. reið (1))
råtis ‘good, generous; generosity, good- ness”. Cf. reio (1) and rotos Skt. ratíh, adj. “generous, gracious, bountiful’; f. ‘favour’; Av. raitis, f. ‘generosity’; Latv. cf. ratns, adj. ‘good, well-behaved'"
rátio “float; duck Lat. cf. (?) ratiara *barge, lighter? beside ratis ‘raft; Alb. rosé, f. ‘duck’: Srb. raca, f. id. (Cf. sense of E duckboard?)
(rátos (1) and (2), see rotos (1) and OH
rauk- ‘rough, hoarse, rasping; roar, shout. Cf. roukos Lat. raucus, adj. ‘hoarse’; OCS cf. po-rukŭ, adj. ‘harsh’; Blg. ruk, m. ‘shout’; ručà, v. ‘rush, crash’; rukam, rukvam, v. ‘hurtle’; Slovak ru- čať, Slovene ručiti, inf. ‘bellow’; Srb. rüka, f. ‘roar’
raul- Icel. raula, v. ‘croon’; Li. raulóti, inf., also raulióti ‘bellow, rut
Gun ‘uproot’. Cf. reu-, rou- Gk. (?) rhaío, v. destroy’. Ambig.); Du. roien ` & roeien, v. ‘uproot’; Li. rauju & raunu, inf: rauti, v. (id. & *téar, pull) beside raviu, eti, v. ‘weed’; rovimas ‘plucking, pilling'; Latv. ràva ‘chink, crack
ráuos (?) Lat. (ambig.) rávus, adj. ((3) ‘blunt, dull". For sense of “dun, tawny’ cf. ghràuos above. In sense of ‘hoarse’, cf. ghrauó, ið above. (OE, rów, adj. and s. ‘quiet; quietude’. Cf. WP I, 144 and roua)
rédh- ‘means, state, effec. Cf. WP I, 75 & IT, 369 Skt. ràdhami, ràdhyami, v. ‘rejoice; prosper; achieve; prepare’; radhnómi ‘prepare; pros- per; perfect’; rādhas, n. ‘favour’; Av. rāð(eimi), v. ‘prepare; proffer’; raóáh-, n. ‘gift, offering’; raóo, m. ‘lord’; Go. cf. *garéps implied in ga- redaba, adv. ‘respectfully’; MHG rat, sm.
1065
*counsel; council; raten, sv. 7. “advise, order”; OE rëde n. ‘gear’; f. ‘reading, design’; adj. ‘ready, skilled’; ON ráð, n. “advice, means, plan, desire, authority”; Li. (LW?) redas, reda, mf. "order, preparation'; Latv. (LW?) redes, pl. ‘harness’
régü, ið (regs-?) “see, observe". Cf. WP II, 366. (Variant rüg-) Gk. cf. a-régo, v. (^help, save’, fr. *sm-?), cf. a-rogé, f. ‘help’; o-gde: OHG ruohh, MHG ruoch, sm. & f. ‘care’; OHG ruohhen, OS rokian; OE recan, ON rækja, v. ‘care’. Cf. rüg- below. (Uncertainly Skt. laksámi “note, observe); (short vowel in) Li. reen eti, v. ‘see’; Latv. regu, redzēt, v. id. beside (long- gde) rēgs, m. “vision, ghost: (short o-gde in) R róZa, f. *grimace' (here?)
reguos (variant form of ereguos, q.v.). WP II, 367
regio ‘dye, tinge; be tinged’. WP II, 366 Skt. rájyami, v. “get coloured, flush’; Per. ra- zam, v. ‘dye, tinge’; Gk. rhézo (rheg-), v. (2) ‘dye’; cf. rhégma, n. ‘dyed object
rég- (1) 'streak, line, cut, téar, notch, groove”. Cf. ureg- Skt. rajih, m., rajih, f. ‘streak, line, row’; Oss. cf. raz, s. ‘front; W cf. rheian, pl. au f. (stripe), fr. *region-); Icel. rák, f. ‘streak’; (ambig. in OCS rézü, m., réza, f. “cut, gash’ and in Li. reZis, gs: -io, m. id. but preferably, with Gk. rh&xis, f. ‘fissure’ to type ure$-, q. v.)
reg- (2) “reach, rule’, etc. See following entries, and especially rēĝs
régonio ‘woman, queen’. Cf. regs Skt. rajfiib, f. ‘queen’; OIr. rígain, Ir. ríoghan, id.; W rhian, rhiain, id. Cf. Lat. regina, id.
refimn- (regmn-) ‘projection, extent. Cf. rego Skt. rjiman, m. ‘straightness’; Av. rasman, m. “army column’; Per. razm, s. ‘battle’; Oss. razmä, adv. “ahead, on’; prp. ‘towards’; Gk. óregma “outreach; extent'; Lat. regimen, n. ‘rule; rudder; MHG cf. ge-rëch, adj. "Dt ready; upright’; ge-rich, sm. & sn. ‘revenge, punishment’
rēĝios ‘royal’. Cf. re&s and derivs. Skt. rajyáh, id.; Lat. regius, id.; Ir. cf. rígh-, cpds. id.; ríghe, f. ‘kingdom’; (early LW in)
régó, ið (regs-?) — reido
20
25
30
35
40
45
1066
Go. reikeis ‘powerful’; OHG rihhi ‘rich’
régó ‘spread, reach, extend, rule’. Cf. régs and derivs. WP II, 362 Skt. rajami, raje, v. ‘rule; Vedic rajmi, 3s: rasti, id.; Av. raz-, v. (2) “arrange, order’; Oss. cf. a-razín, pp: a-rást, v. ‘set up; reach’; Tokh. A rák-, rak-; B råk-, rak, v. ‘cover, spread"; Gk. orégo, v. “stretch, extend, reach'; Lat. rego, Gre pf: rēxī, v. (rule, manage? beside porgo, Gre, v. "eo: Olr. gem, Ir. righim, v. “stretch, reach’; cf. Ir. (denom.) ríoghaim, v. “crown”; OS (denom.) gi-rekon, wv. “prepare — food”; OE recan, sv. 5. ‘go, move, bring’; Sw. räcka, OSw. rækka, v. ‘reach’; Go. uf-rakjan, id. (Gmc. forms in o-gde) beside Du. LG. raken, v. (2) ‘touch, hit upon, reach’; Sw. råka, v. id. (fr. *re8-) as also Li. reZ-tas, m. ‘law and order, discipline, status quo'
ré$s ‘chief, king’. Cf. régo. WP II, 363 Skt. ràj, rat, id.; Av. cf. rajis, f. ‘kingdom’; Lat. réx, gpl. regum, as Skt.; MIr. rí, gs: ríg, righ, id.; Gaul rix ‘chief; W rhi, id.; (LW in Br. rué ‘king’; LW in OHG rihhi, etc. see régios)
ré8st- (rogst-) ‘stretch, extent’. Cf. rego and next. Variant rest- Skt. cf. rajisthab, adj. 'straightest; Av. cf. råstəm, adv. “straight ahead; Gk. cf. orekh- théo, v. “stretch, extend”; (Alb. rresht “row, line’ is a prob. DW in view of initial rr-, cf. Lat. restis); W rhes, pl. -i & au £. (Crow, rank". LW?); Cor. res, pl. resyow, f. id. (LW?); Go. (o-gde) cf. rasta, f. “stretch of road, mile’; OHG rasta, id.; MHG reste, sf. id. See next
(regtos, is, see reKtos, is)
reibhos (1) ‘gay, bright’. Cf. roibh- (2) Ir. riabh, adj. ‘azure’; cf. riabhach, adj. ‘strip- ed'; (o-gde in) ON reifr, adj. ‘cheerful’; Li. raibas, adj. ‘motley, gay’; Latv. raibs, id.
reibhos (2) ‘rich, abundant’ MDu. rijf, rive; Fris. rjue, adj. ‘abundant’; MLG rive, adj. ‘generous’; LG riev, adj. “luxu- rious’; OE rife, adj. 'abundant'; ON oft adj. “acceptable, good’; mod. ‘ample, abundant ; Li. riebüs, adj. ‘rich, fat’; cf. ON o-gde reifr *cheerful" and (1)
reidó (?) Gk. ereído, v. (2) ‘prop, lean’; Lat. cf. ridica,
1067
f. “vine-prop, support’ (Isophonic: Gk. ereído (1) “thrust, pierce, force")
```


## [2026-09-14T01:15:04.713Z] TOOL CALL #32: Bash

```json
{
 "command": "pdftoppm -f 418 -l 418 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg418 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg418.png",
 "description": "Render PDF page 418"
}
```


### [2026-09-14T01:15:06.564Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 87213 Sep 13 21:15 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg418.png
```


## [2026-09-14T01:15:06.903Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON rang\"; grep -c \"رنگ\" MON_part1.txt MON_part2.txt 2>/dev/null; echo \"=== rajidan\"; grep -n \"رجیدن\\|رزیدن\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head",
 "description": "Grep Mo'in for rajidan"
}
```


### [2026-09-14T01:15:06.995Z] TOOL RESULT

```
=== MON rang
MON_part1.txt:859
MON_part2.txt:888
=== rajidan
incoming/MON/MON_2vol_Adena_v2_djvu.txt:734:نقض عهد کردن. خیانت ورزیدن. (امص.) 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:959:شدن» غفلت ورزیدن. فریب خوردن. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:2074:آمرزیدن گناه را. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:2076:راء آمرزیدن. (امص.) آمرزش. غفران 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:2099:غفیر: :۵۲ (ع.] (مصم.) آمرزیدن گناه 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:2590:غنیمت. خیانت ورزیدن. (امص.) خیانت. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:11977:جای گرفتن. بات ورزیدن: (سصع.) آرام 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:17356:کاری کردن؛ حدمت او ورزیدن. به کار در 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:21557:بزرگی ورزیدن. جوانمرد گردیدن. (امص.) 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:30031:نمودن» بخل ورزیدن.
```


## [2026-09-14T01:15:08.736Z] TOOL CALL #34: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg418.png"
}
```


### [2026-09-14T01:15:09.282Z] TOOL RESULT

```

```


## [2026-09-14T01:15:09.266Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T01:15:17.653Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 418 -l 418 -r 600 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg418hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg418hi.png'); print(im.size)\nw,h=im.size\n# rajidan box approx y 590-650 of 2200 scale -> fraction\nim.crop((int(0.40*w),int(0.255*h),int(0.80*w),int(0.30*h))).save('pg418-rajidan.png')\n\"; ls",
 "description": "Crop rajidan box at 600dpi"
}
```


### [2026-09-14T01:15:22.739Z] TOOL RESULT

```
(5100, 6600)
391-top.png
394hi.png
394-zoom.png
400-bot.png
400-top.png
agents.txt
beekes410.txt
bqt390_436_foot.jpg
bqt390_436_top.jpg
bqt390_662_foot.jpg
bqt390_662_top.jpg
bqt390_n436.jpg
bqt390_n662.jpg
build-389.py
build-390.py
build-391.py
build393.py
build-394.py
build-395.py
build-396.py
build-398.py
build-400.py
build-401.py
build-405.py
build-406.py
build-407.py
c404-empty.png
c404-greek.png
c404-patil.png
c404-pest.png
c404-symp2.png
c404-symp.png
c412_cedar.png
c412_makrome.png
c412_makrome_zoom.png
c412_meqrameh.png
c412_meq_zoom.png
c412_sedr_zoom2.png
c412_sedr_zoom.png
crop14-394.png
crop18-394.png
crop411_a.png
crop411_b.png
crop411_c.png
edit_about.py
edit_research.py
ffprof
pg390b.jpg
pg390b.png
pg390.png
pg391big.png
pg391crop.png
pg391.png
pg391root.png
pg391sog.png
pg392.png
pg393.png
pg394hi.png
pg394.png
pg397.png
pg398.png
pg399-crop1.png
pg399-greek.png
pg399.png
pg399-sog.png
pg400big.png
pg400_fa_heli.png
pg400_fr2.png
pg400_french.png
pg400_kasak2.png
pg400_kasak3.png
pg400_kasak.png
pg400.png
pg402.png
pg404hi.png
pg404.png
pg405.png
pg406.png
pg407.png
pg408-ampus.png
pg408-germ.png
pg408.png
pg409.png
pg410hi.png
pg410-k2.png
pg410-kadm2.png
pg410-kadm.png
pg410-persian.png
pg410.png
pg410-q2.png
pg410-qedam.png
pg411_300.png
pg411.png
pg412_hi.png
pg412.png
pg412_uhi.png
pg413.png
pg414-greek.png
pg414.png
pg415.png
pg418hi.png
pg418.png
pg418-rajidan.png
queue.txt
sem410.html
u_mak.png
u_meq.png
u_sedr.png
write397.py
write-402.py
```


## [2026-09-14T01:15:26.223Z] TOOL CALL #36: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg418-rajidan.png"
}
```


### [2026-09-14T01:15:26.457Z] TOOL RESULT

```

```


## [2026-09-14T01:15:26.453Z] INPUT

[Image: original 2040x297, displayed at 2000x291. Multiply coordinates by 1.02 to map to original image.]


## [2026-09-14T01:15:30.195Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg418hi.png'); w,h=im.size\nim.crop((int(0.42*w),int(0.288*h),int(0.80*w),int(0.315*h))).resize((int(0.38*w*1.2),int(0.027*h*1.2))).save('pg418-raj2.png')\n\"",
 "description": "Crop rajidan word"
}
```


### [2026-09-14T01:15:31.932Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:15:34.261Z] TOOL CALL #38: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg418-raj2.png"
}
```


### [2026-09-14T01:15:34.337Z] TOOL RESULT

```

```


## [2026-09-14T01:15:34.335Z] INPUT

[Image: original 2325x213, displayed at 2000x183. Multiply coordinates by 1.16 to map to original image.]


## [2026-09-14T01:15:37.993Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg418hi.png'); w,h=im.size\nc=im.crop((int(0.60*w),int(0.302*h),int(0.80*w),int(0.322*h)))\nc=c.resize((c.width*2,c.height*2))\nc.save('pg418-raj3.png'); print(c.size)\n\"",
 "description": "Crop the Persian script of rajidan"
}
```


### [2026-09-14T01:15:39.903Z] TOOL RESULT

```
(2040, 264)
```


## [2026-09-14T01:15:41.978Z] TOOL CALL #40: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg418-raj3.png"
}
```


### [2026-09-14T01:15:42.091Z] TOOL RESULT

```

```


## [2026-09-14T01:15:42.082Z] INPUT

[Image: original 2040x264, displayed at 2000x259. Multiply coordinates by 1.02 to map to original image.]


## [2026-09-14T01:15:53.291Z] TOOL CALL #41: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-14T01:15:53.299Z] TOOL RESULT

```


```


## [2026-09-14T01:15:57.026Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D9%86%DA%AF",
 "prompt": "Give the full Persian etymology section for رنگ (rang) 'colour': Middle Persian form, Proto-Iranian/Sanskrit connection, whether it is said to be a borrowing from Sanskrit raṅga or inherited, and cited authorities."
}
```


## [2026-09-14T01:15:57.966Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/regolith",
 "prompt": "Give the full etymology of regolith, including the Greek source word, its meaning, who coined it and when."
}
```


### [2026-09-14T01:16:02.243Z] TOOL RESULT

```
# Etymology of Regolith

**Coinage and Date:** The term was coined in 1897 as a geology term.

**Greek Source:** The word derives from the Latinized form of Greek *rhēgos*, meaning "rug, blanket."

**Compound Construction:** It combines the Greek element with *lithos* (stone), creating a compound that literally translates to something like "blanket of stone."

**Definition:** In geological usage, regolith refers to "unconsolidated rocky material covering bedrock."

**Etymology Chain:** The Greek *rhēgos* traces back to the Proto-Indo-European root *\*reg-* (3), which means "to dye." This same root also appears in the Sanskrit *raga-s* (harmony, melody) and relates to the concept of color and mood.

The webpage does not identify a specific individual credited with coining the term, only that it entered geological terminology in 1897.
```


### [2026-09-14T01:16:02.469Z] TOOL RESULT

```
# Persian Etymology of رنگ (rang)

**Middle Persian Form:**
"From Middle Persian lng (rang)"

**Proto-Iranian Connection:**
The word derives "from Proto-Iranian *rang- ('to colour, dye'), ultimately from Proto-Indo-European *reng- ('to dye')."

**Sanskrit Connection:**
The etymology notes cognates including "Sanskrit रञ्ज् (rañj, 'to be dyed or coloured, to redden, grow red, glow')." However, this represents a cognate relationship rather than direct borrowing—both Persian and Sanskrit descended from a common Indo-European ancestor.

**Inheritance vs. Borrowing:**
The Persian term is presented as inherited from Middle Persian, not borrowed from Sanskrit. The page states both languages share Indo-European roots through "Proto-Indo-European *reng-."

**Cited Authority:**
Cheung, Johnny (2007), *Etymological Dictionary of the Iranian Verb* (Leiden Indo-European Etymological Dictionary Series; 2), Brill, page 314.
```


## [2026-09-14T01:16:13.862Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"rang\\|RANG\" CHEUNG.txt | grep -i \"dye\\|colour\\|color\\|\\*rang\" | head -20; echo \"=== direct\"; grep -n \"^\\*rang\\|\\*ranǰ\\|\\*rang-\" CHEUNG.txt | head",
 "description": "Grep Cheung for *rang"
}
```


### [2026-09-14T01:16:13.947Z] TOOL RESULT

```
20604:*MIDDLE PERSIAN: MMP me BMP rng /rang/ ‘colour’ || (+ *abi-) BMP ’brng 
20618:*NWIR: NP razidan/ ‘to colour, dye, taint, tinge’, NP rang ‘colour’, NP raxš ‘a 
20628:*MISC: Arm. (LW) erasx ‘reddish’, ? Arm. erang ‘colour’ 
=== direct
```


## [2026-09-14T01:16:16.320Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '20580,20660p' CHEUNG.txt",
 "description": "Print Cheung *rang entry"
}
```


### [2026-09-14T01:16:16.389Z] TOOL RESULT

```
*AVESTAN: YAv. rona- (n.) ‘battle, fight" (Yt 14.25, V 7.52), OAv. rāniið.skərəiti- 
‘dispensing joy’ (Y 44.6, Y 47.3, Y 50.2, Y 18.4) 

*MIDDLE PERSIAN: MMP rn ‘refreshment’? > DMMPP: 296a 

*KHOTANESE: ? Khot. ranam (Gpl.) ‘fighters’ 

*CHORESMIAN: rns- ‘to be in heat? => Samadi: 172 

*SANSKRIT: ran” ‘to rejoice, be pleased’ (RV+) > EWAia II: 427 

9 This apparently Пг. root has no certain IE provenance. 


*PIE — > LIV: - | Pok.: 327 
*REFERENCES: DKS: 361a; Werba 1997: 369 


*ra(n)j ‘to colour, dye’ 

*OLD PERSIAN: (+ *4-) ? El-OP /äranjanam/ <ha-ra-an-za-na-um> ‘decoration’ (cf. 
Hinz 1971: 23) 

*MIDDLE PERSIAN: MMP me BMP rng /rang/ ‘colour’ || (+ *abi-) BMP ’brng 
/abrang/ ‘splendour’ > DMMPP: 296a 

*KHOTANESE: rräsa- ‘dark coloured’ 

*SOGDIAN: ? BSogd. rxs- ‘Rakhsh [= Rustam’s horse]? || (+ *fra-) CSogd. (f)$(n)y 
šw ‘lamp-black, soot’ (Sims-Williams 1983: 50) 


314 *rap/f 


*CHORESMIAN: rxtyk, rxtk ‘red’ 

*NWIR: NP razidan/ ‘to colour, dye, taint, tinge’, NP rang ‘colour’, NP raxš ‘a 
mixture of red and white, Rakhsh [= Rustam’s horse]’ (LW, < Sogd. ?), Bal. rajit, 
ratk/raj- ‘to tan (skin)’, (EHB) raxt/raj ‘to dye’, Kurd. ras ‘black’ (LW ?) || (+ *abi-) 
NP abranjan ‘a bracelet or anklet (of gold or silver)’ (also auranjan), NP aurang 
‘throne, beauty, glory, honour’ (au-: "Eastern" pronunciation ?) 

*NEIR: Rosh. réz-, Yzgh. raz- ‘to colour the eyes’, Ishk. reZ-/rüyd ‘to colour 
brows/eyelashes’, Yzgh. cam-raZak ‘stick for applying collyrium’ || (+ *fra- ?) Sh. 
arizm, Sariq. rizm, Wa. rizm ‘lamp-black, soot’ (Sims-Williams, Lei 

*MISC: Arm. (LW) erasx ‘reddish’, ? Arm. erang ‘colour’ 

*SANSKRIT: raj ‘to colour, to become red’ (AV+) = EWAia II: 424 

«PIE *(s)reg- ‘to colour (dark)’ ? = LIV: 587 | Pok.: 854 

*IE COGNATES: Gr. péGo ‘I dye, paint’, Gr. pñyoç (n.) ‘carpet, rug’, Gr. (inscr.) 
poyevc (m.) ‘dyer’ 

*REFERENCES: Morgenstierne 1942: 265; EVS: 16a, 71a, 23b; DKS: 362a f.; Benzing 1983: 564; Polomé 
1989: 220; Werba 1997: 224; Steblin-Kamenskij 1999: 296; Shahbakhsh: s.v. raj- 


*rap/f ‘to help, assist, support’ 
*AVESTAN: rap- ‘to help, assist’ = Liste: 56 
Pres. them.: ОРТ. Zeg. OAv. rapöis (Y 41.4), IMPV. 25р. OAv. агара (Y 49.1); Partic.: pres. rapant- 


*KHOTANESE: Khot. tcarampha- ‘staff, stick’ || (+ *pati-) parah- (parih-) ‘to be 
established’, LKh. pariph- (caus./tr.) ‘to establish’, paraha- ‘support’? = SGS: 81 f. 
9 Further Ir. cognates are unknown. 


“PIE LIV: - | Pok.: 
*REFERENCES: EVP: 65; IIFL II: 259a, 420a, 549a; Abrahamian 1936: 124, no. 63; EVS: 91a; Puhvel III: 
176 ff.; Steblin-Kamenskij 1999: 398 


*rarz ‘to shake, tremble’ 
*MIDDLE PERSIAN: BMP llc- /larz-/ ‘to shake, tremble’, MMP mz ‘(fever’s) 


shivering, ague’ > DMMPP: 296b
```


## [2026-09-14T01:16:29.976Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=419 && NR<=423 {print \"----LEAF\",NR; print substr($0,1,1500)}' BQT_v2_pages.txt",
 "description": "Print BQT vol2 leaves near p.964"
}
```


### [2026-09-14T01:16:31.099Z] TOOL RESULT

```
----LEAF 419
     ‫ه‬
     ‫ا ی‬                                                                                                         ‫کراب‬
 ‫آا‬
  ‫کویمتد‪ .‬وشمشیری که برپهلوی‌اسب‌بندند وار‬                   ‫تبواشد ‪ ۰ ۱‬و بعربی ات‬                ‫ن)ی‬
                                                                                                    ‫مدع(‪۱‬‬
                                                                                                        ‫باژن‬
                                                                                                           ‫وپ‬
                            ‫زمر رکابی هم خوانند ‪.‬‬
 ‫راسه ‪ - ۴‬پم اول بروزن خلاصه ‪.‬‬
                             ‫ک‬                               ‫ر کاب = بکراول بروزن‌قاب پىاله‌ای‬
                                                                                  ‫يمعي‬          ‫‪E‬‏‬             ‫ماشف هشت‬


             ‫وآفرا (‪ )۲‬بعربی ابو مدلج گوبند‪.‬‬                                      ‫=‬   ‫است‬    ‫هم خفن‬      ‫سواری‬     ‫لب‬



 ‫رکاشه ‪ - ۴‬با شن شطه دار‪ .‬بر وزن‬                                                 ‫ودرعربی حل
----LEAF 420
  ‫رکو‬                                                                                         ‫‪-‬‬
                                                                                            ‫‪-۹-‬‬

  ‫بلفت زند وپازند (‪ )۱‬بمعنی شما باشد کهخطاب‬            ‫ر کو تا ‪ ‌ ۱‬بقعح اول وثالی بواورسیده‬

  ‫باتمظیم وخطاب‌باجمم است» وبسربی اگنتومیند‪.‬‬           ‫وفوقانی بالفکشیده» بزبان زندوپازند(‪ )۱‬بمعنی‬
 ‫ر کیدن ؟ ‪ ۰‬بروزن مکیدن‪ ,‬بعنی‌خود‬                                        ‫هوش باشد ‪۰‬‬    ‫هشار وصاحب‬


          ‫بخود سخن کفتن از روی قپر و نشب ‪.‬‬             ‫ر کو م ‪ ۲‬د بفتح اول بروزن سوم »‬

                                        ‫يان هیحدهم‬
                 ‫یوت‬
                   ‫اغت‬
                     ‫نه ل‬
                        ‫کسیزد‬
                            ‫دررای بنیقطه بکااف فارسی مشتمل بر‬
 ‫جان۔ بکرثائی» کنابه‌ازشربان‬        ‫رگ‬

                          ‫وحبل‌الورید باشد ‪. ۸‬‬
 ‫رکه‬    ‫بمعنتی‬    ‫خو ابا نیدن ‪-‬‬     ‫رگ‬
                
----LEAF 421
 ‫=‬                                                                                                    ‫کرول‬
‫وچادرىك‬   ‫‪-‬‬   ‫رکوه است که کهنه ولتۀمىتممل ‏‬
                                                         ‫ر گول » بنم اول و باالك مجهول‬
                                                         ‫بروزن سلوك؛ بمعنی ر کواست که کربای وجامه‬
‫ر یك ‪ = ۲‬بروزن رمید‪ .‬ماضی رگیدن‬                                           ‫ولنة کهنة ازهمرفته باشد ‪.‬‬
                                                        ‫زرگوه = بکر اول و سکون ثالی‬
                     ‫زد ‪.‬‬    ‫خود سخن گفت وحرف‬           ‫و پور های هوز (‪ ۰ )۱‬بمعنی ر کوست کهلته‬
   ‫»ی‬
    ‫عنن‬
      ‫ممید‬
         ‫بن ر‬
            ‫ر گیدن ‪ - ۴‬بر وز‬                              ‫لكخت‬
                                                             ‫کپنه و کر بای آزهم رفته باشد‪ -‬وچادر ي‬
‫با خود سخن‬    ‫عبت‬    ‫از روی قهر و‬       ‫آهته‌اهته‬                                            ‫‪.‬‬   ‫را یز گوبند‬


                                       ‫کفتن باشد ‪.‬‬     
----LEAF 422
 ‫رمکان‬                                                                                               ‫هت‬
                                                                                                      ‫‪-‬‬

‫روش» بممنی‌تبدیل‌است که ازبدلکردن‌باشد ‪- ۴‬‬              ‫رمارم = بفتح اول ورای قرشت بروزن‬
              ‫‪۰‬‬   ‫وبممنی رمیدن هم آمده است ©‬            ‫«مادم » بمعنی مقابل _وکونا کون ‪٩‬‏ پریوسته‬
‫رمظان ‪ ۱‬با فای شقطه دار بروزن‬                                           ‫ومتعافب وپی دربی باشد ‪. ۴‬‬
‫شیطان * نام یکی از احاب دين مجوی بوده‬                   ‫رماس » بفتح اول بر وزن تمای »‬
    ‫وباعتقاد او لور مختار است وظلمت موجب ‪.‬‬              ‫دوای‬   ‫مصطکی را گوند ‪ ۰‬و ان صمغی است‬

‫بر وزن سك ‪ ,‬بمعئی رمه‬            ‫رمك ‪۲‬‬                  ‫وآنرا رماست هم میگوبند بافوقالی درآخر(‪.)۱‬‬
‫و ابلشی اسب غویره‬          ‫فهند‬
                              ‫سکل‬
                                ‫کتوکه‬
                                    ‫اس‬                  ‫بقت
----LEAF 423
  ‫”‪IY‬‬

‫رمه ‪ - ۳‬بنتح اول و ثالیم»من یکله‬                               ‫= بفتح اول وثالی بروزن چمن»‬
                                                                                                        ‫رهن ‪۱‬‬


 ‫کوسفند وابلخی اسب باشد ‪ -‬و سپاہ ولشکر ‪-‬‬                      ‫»نی مجموع و همه‬     ‫مع‬‫ود (ب‪)۱‬‬‫زدن‬
                                                                                             ‫ازن‬
                                                                                               ‫پغت‬
                                                                                                 ‫بل‬
                                                              ‫باشد چنانکه هکروگایهند «رمن‌را دبدم» یمتی‬
‫وجمعیت مردم را گهفتمه‌اند ‪ -‬و پروین را لیز‬                                              ‫همه را رمجوع را ديدم ‪.‬‬
 ‫کوبند که‌بعربی بثارخوانند؟ ‪ -‬ودرعربی‌پاتشدبد‬
                                                              ‫رمو لك یانول بر وزن سلوکه ‪.‬‬
 ‫الی ‪ ,‬استخوان پوسیده و پوسیده شدن چیزی‬
```


## [2026-09-14T01:16:39.952Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} {n++; if ($0 ~ /رنگ/) print n}' BQT_v2_pages.txt | head -30",
 "description": "Find leaves with رنگ in BQT vol2"
}
```


### [2026-09-14T01:16:41.009Z] TOOL RESULT

```
20
22
24
25
26
28
31
34
35
41
42
44
56
64
65
66
79
88
90
91
92
94
98
99
101
129
135
145
147
161
```


## [2026-09-14T01:16:44.105Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} {n++; if (n>=424 && n<=432) {print \"----LEAF\",n,\" printed~\",n+543; print substr($0,1,1200)}}' BQT_v2_pages.txt",
 "description": "Print BQT v2 leaves 424-432"
}
```


### [2026-09-14T01:16:45.191Z] TOOL RESULT

```
----LEAF 424  printed~ 967
  ‫رند افریس‬                                                                                                         ‫وت‬
 ‫خوشبو وخوشگوار حم آمده است‪ -‬وبممنی گرد‬
‫وفبار باشد چه خاکے رند کردیرا کوبن که از‬                                                    ‫و بممنی خشم و قهر وب‬
                                                                    ‫حم هست‪ -‬و رنگه‬
‫روی خاک برخیزد ‪ -‬و مورد را نکیفزته‌اند که‬                                                     ‫‪.‬‬   ‫‪۴‬‬   ‫ولون را نیز گویند‬


 ‫بعر بی آی خواند ‪٩‬‏ ‪ .‬وبعضی گوبند رلد درخت‬
                                                                    ‫ر نحال س بروزن‌چنگال‪ ,‬طمعام‌رخوردلی‬
 ‫غار است ‪٩۱۰‬‏ وآن درختی باشد برزکه وربکه‬
                                                                                                               ‫رگاونند ‪.‬‬
 ‫آن بزرکت�
----LEAF 425  printed~ 968
    ‫سوه‬                                                                                                ‫ردان خاك بیز‬
‫و دام‬       ‫وباین‌معتی با زای قطمرار هم مده است ‪-‬‬                   ‫وعلم پادشاهی هم هست ‪ .‬کوبند در جزیره‌ای از‬
 ‫کیاهی است بهاری که اکثر چرندکان خصوصاً‬                              ‫جزابر اودرختی است که بارآن درخت‌مرغ است‬
            ‫کوسفند بچریدن‌آن فربه وگرد‬
 ‫نهو‪-‬عی ازچرم‬                                                                             ‫‪.‬‬     ‫ودیگر عجایبات هم هت‬
                                         ‫باشد سیاه رنگه ‪.‬‬            ‫نردان خا پکیزنابه از باريك‬
 ‫گ" بروزن خندیدن» ‪:‬هنی‬                    ‫دن‬
                                           ‫بلد‬
                                             ‫ر‬                       ‫بینان ودفیق نظران کوالکه دقیقه�
----LEAF 426  printed~ 969
‫رنگه رییع‬                                                                                    ‫‪-0‬‬
                                                                                              ‫‪‎‬ی ‪٩‬‬


                                      ‫‪.‬‬     ‫ویات‬
                                               ‫خ‬       ‫‪ ۱-7‬طرزوروش‬         ‫بوشند ‪۰‬‬    ‫ژنده‌ای که دروشان‬

                                                        ‫‪-‬ثل‬
                                                          ‫‪ ۲۱‬م‬        ‫و سرت وقاعده و فالون باشد ‪۰‬‬
                                                          ‫یر‬
                                                           ‫ش‪-‬‬‫‪.‬‏ ‪۳۱‬‬            ‫ناند‬
                                                                                 ‫ور‬‫گبه‬
                                                                                     ‫ومانشد ونظر وش‬
                  ‫وسیرت جوان مردان باشد ‪. ۱‬�
----LEAF 427  printed~ 970
   ‫نت‬                                                                                          ‫رنگه رزگلگون‬


                                                           ‫نگ رر گلگون ‪-‬کنابه از راب‬
                                                                                   ‫ر‬
                    ‫تاریکی وتیر گی هوا باشد ‪.‬‬                              ‫فروش است و بعربی خمار گویند ‪.‬‬
 ‫رنگیدن = بر وزن لنگیدن ‪ ,‬روسدن‬                        ‫ر نگر و تا د بکر اول وسکون ثالی‬
                               ‫ورستن گیاء باشد ‪.‬‬
                                                       ‫فوفانی‬      ‫و‬   ‫بواو رصیده‬    ‫بی ناه‬    ‫رای‬       ‫‪1‬‬    ‫» فتح ثالی‬




‫ر نگینا = بانون بالف کشیده‪ .‬شفترنگه‬                    ‫در‬      ‫معروف‬       ‫است‬      ‫جاتوری‬    ‫آن‬     ‫و‬       ‫»‬   ‫گوند‬   ‫را‬

          ‫ب
----LEAF 428  printed~ 971
 ‫روادان‬                                                                                                                     ‫=‪“۷‬‬

 ‫ویآنشتر دآربهای‬
               ‫پلای ‪ ۰‬رستنیی باشد ب‬                                 ‫= بروزن هوا؛ بمعنی‌جایزوجاری‬                            ‫روا‬
‫استاده روید و بمربی جرجیرالماء و کرفس‌الماء‬                         ‫ورواح وروان باشد ‪ -‬ویمعتی حصول‌کار هم‌هست‬
                                                ‫خوانند ‪. ۷‬‬          ‫همچون‌کام روا وبضم اول درعربی دیدار وخویی‬
‫رواق ‪ -‬بکسر اول بر وزن عراق ‪۰‬‬                                       ‫بی سيراب‬  ‫عمردر‬‫منظر باشد ‪ - ۴‬وبکسر اول ه‬
‫وابوایکه درمر تة‬            ‫پیشگاه خانه را گو‪.‬ند ‪9 ۲‬‬                ‫شدن را کوبند ‪ - ۴‬ر ریسماییکه بدان باربر‬
                               
----LEAF 429  printed~ 972
  ‫سره‬                                                                                    ‫روان آورد‬

                     ‫داشن را فيز گویند ‪٩‬‏‬        ‫سیفتح واو وسکون را‬         ‫روان ورد‬
‫رو با د بض اول و بای ابجد بالف‬                   ‫بخرد و دانا و صاعب‬      ‫حکیم و‬     ‫و دال بی‌شطه ‪,‬‬


           ‫کشیده ‪ ,‬بمعنی روباه تربك است‬
                                                                                    ‫و‬   ‫را گونند‬   ‫عقل‬



           ‫عنبالملب خوانند در اختبارات ‪۰#‬‬        ‫روان بخش ‪ ۰ ۱‬فدرمخته‌ایت که‬
‫رو باه تر بك ‪ -‬نم تای فرشت (‪)4‬‬                    ‫علم وداش با اوست وبعربی اورا (‪ )۱‬روح‌القدس‬
                                                                                             ‫خوالند ‪.‬‬
‫و فتح بای ابجد(ه) وسکون کاف؛ سگه انکور‬
‫باشد )‪(٩
----LEAF 430  printed~ 973
  ‫رود بار‬                                                                                            ‫‪4‬‬
‫لخت پپلوی است ومر کب است از روخ و چاو ‪--‬‬                      ‫بویان ‪ = ۱‬بکراك بروزن‌رومیان‪.‬‬
                                                                                          ‫ر‬
  ‫کویخاه بلند سادة‬
                 ‫بممتی تارك سر ساده » چه ر‬                    ‫بمعنی اربیان است که ملخ آبی باشد و بعریی‬
  ‫بی‌برگے وباراست وچکاد بالای پیشانی که ترديك‬                ‫جرادالیحر خوانند ‪ .‬چون آنرا با نخود سياه‬
                              ‫بتارك سر باشد ‪.‬‬                 ‫بکوبند و برلاف ضماد کنند حب‌القرع رابیرون‬
  ‫رود سم اول و سکون ثالی مجپول‬                                                                        ‫‪¥.‬‬   ‫آورد‬




 ‫و دال ابجد (‪ ۰ )۳‬حر رودخانةٌ عظیم �
----LEAF 431  printed~ 974
    ‫سه‬                                                                                                   ‫رودزم‬

                         ‫مفرد روده همگفته‌اند ‪:‬‬         ‫کوحار » نامبلوکی است و شهری است مابین‬
‫رودلاخ ‪ - ۴‬بلام بالفکید وبخای‬                            ‫گیلان وقزوین‪ -‬وبمعنی جداول آب ورودخانهای‬
 ‫یطه دار زده ‪ ۰‬جابیکه دران رودخانه و جشمه‬
                                          ‫نق‬             ‫بز رکے وجابیکه درآن رودخاله (‪ )۱‬بیارجاری‬
                                                                                          ‫باشد ‪#.‬‬
                           ‫‪ 3‬زهاب مار باشد ‪۰‬‬

‫باشد»‬   ‫رونای‬   ‫بروزن سوزن»‬          ‫رودن‬
                                                         ‫رودزم ‪ -‬بكر () ثالك و تم‬
‫وآن کاهی است که چیزها بدان رنگه کنند ‪1‬‬                    ‫ز
----LEAF 432  printed~ 975
     ‫روز خوش‬                                                                                           ‫‪-4۷۱-‬‬
      ‫لش مد و او را در‬   ‫و غراشان‬         ‫ویادشاهان(‪)۳‬‬
                                                           ‫رو ر ‪ -‬ممروفت و بعربی نهار وبوم‬
      ‫زمان دربان خوانند و روزبانان جمع ِ‬                  ‫فنتیاب همهت چنانکه گوبند‬     ‫آمع‬
                                                                                         ‫گوبند ‪ -‬وی‬
     ‫گا‪-‬هبان‪-‬‬
            ‫دربانان باشد‪ .‬وسر هنگه‪ -‬ووچانوش‬                ‫دروز برآهد» مرادآن باشدکه آفتاب برآهد ‪-‬‬
 ‫و شقیم را گوبند ‪ -‬و بمعتی جلاد هآمده‬                      ‫کونایه از ظاهر وآشکارا وروشن باشد ‪ -‬وبمعنی‬
                                             ‫است ‪. ۴‬‬       ‫روز کارهم هت ت که کنابه ازفرصتباشد
```


## [2026-09-14T01:16:58.573Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==424' BQT_v2_pages.txt | tail -40",
 "description": "Print full BQT v2 leaf 424"
}
```


### [2026-09-14T01:16:59.721Z] TOOL RESULT

```
 ‫با همزه و فا ورای‬                ‫ر ندافریس ‪-‬‬                       ‫کوبند که از چوب جدا شود ‪ -‬و دست افزاری‬
 ‫فرشت )س( وبای حطی )‪ (£‬وسفن سمفص(‪)٥‬‏ ر‬                              ‫رودگران بدان چوب و نخته تراشند ‪- ۷‬‬ ‫کده‬
 ‫بادشاه‬   ‫بمعنی‬           ‫انگیز ‪E‬‏‬               ‫ت‬
                                                 ‫اع >‬    ‫وون‬
                                                                    ‫وامر برندیدن هم هت یعتی برند‪ - ۷‬وچوب‬
   ‫بادشاهان باشد که کنابه از پرورد گار اک‬                           ‫و معلی‬           ‫تراش و تراشنده را نز گفته اند ‪۸‬‬

                      ‫‪-‬خصیکه ‪ ...‬سلامت باشد‪.‬‬
                                           ‫وش‬‫(‪ )۲‬خم ‪: ۱‬‬                                 ‫‪:‬بیمار ‪.‬‬
                                                                                               ‫(‪ )۱‬خم‪ ۱‬و‬
                        ‫() چك‪ - :‬سعفص ‪.‬‬                        ‫)‪(٤‬‏ چك ‪ :‬وبا‬                ‫(‪ )۳‬چك‪ :‬و را ‪.‬‬

   ‫رنجه › بپلری [‪« 12۲‬باروچا ‪( 2[71۵۲ ۰ ۹۵۲‬غم » درد ‪ ۰‬تاراحتی) » دراوراق‬ ‫‪۱‬‬
             ‫تورفان ‪( 212۲‬درد) ازماسکریت ‪ ( 612۷[۲‬در اضطراب شدن) رك ‪ :‬سر که ‪:۱۹۱‬‬
         ‫که له رات رسد زخلق» نه رنج‪.‬‬                                          ‫کر کزندت رسد ز خلق مرلج‬
   ‫«کلتان ‪. ۷۲1۰‬‬
                                                                                        ‫‪:‬‬   ‫رنگ‬   ‫؛‬   ‫رك‬      ‫‪۳‬‬


                ‫ابن برنج ازعفیق وآن از در‪.‬‬                                    ‫پهلو از پبه و کردن ازخون پر‬
       ‫نظامی کنجوی دروصف کورخر « هفت یکر ‪ ۰‬چاپ‌ارمغان ‪۳.2‬‬

                                                     ‫رلج («‪.‬م‪ ).‬چ‬    ‫اب‬   ‫‪۳۴‬‬            ‫ترجمه «دق» ‪.‬‬          ‫‪۴‬‬
                ‫‪.‬‬   ‫کرد‬   ‫را رنسه‬      ‫خود‬   ‫سممین‬    ‫ساعد‬
                                                                     ‫*ر‪-‬که باپولاد بازو پنجه کرد‬
                                                                                               ‫ه‬
   ‫« کلستان ‪. ۳1۰‬‬
        ‫ارندندم؟ ‪.‬‬                ‫‪ ۸‬مضفف‬         ‫‪:‬لدندن ‪.‬‬
                                                        ‫‪ - ۷‬رك ر‬     ‫‪ -‬رك‪ :‬رنده ‪-‬‬ ‫‪۹‬‬

                          ‫‪. ۸۳‬‬        ‫‏‪ ٩‬رید = مورد ‏ ‪sutryM 51۵۷۵۲۳۳06‬‏ ت«ایتی‬
       ‫بر که بو ( = غار) = ونااداه ‪ 8۲0۱21‬د ایتی ‪ ۳۸۱‬و ‪.۹۹۱‬‬                                       ‫‪ ۶‬رند =‬
                              ‫‪.‬‬    ‫ص‪۷۸۱‬‬
                                      ‫(فر) «لك ‪۲‬‬          ‫‪reirual‬‏‬        ‫ص‬    ‫است‬   ‫محتی ر لد درالجز بره معمول‬      ‫این‬

                                                                                 ‫‪ -۱‬رك ذ‪:‬اقی (ذافنی) ‪.‬‬
                ‫آنگاه توبه ‪ .‬استغفر اد‬                                ‫‪ -۴‬من رند و عاشق در موسم کل‬
   ‫‪.‬‬        ‫‪۹‬‬       ‫شبیرازی‬
                          ‫د‬       ‫« حافط‬
```


## [2026-09-14T01:17:15.797Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} {n++; if (n>=423 && n<=428) {print \"====LEAF\",n; print $0}}' BQT_v2_pages.txt | grep -n \"رنگ\\|rang\\|پهلوی\\|====\" | head -60",
 "description": "Find رنگ headword leaf in BQT v2"
}
```


### [2026-09-14T01:17:16.886Z] TOOL RESULT

```
1:====LEAF 423
69:====LEAF 424
73:                                                                    ‫حم هست‪ -‬و رنگه‬
119:                                                                                        ‫‪:‬‬   ‫رنگ‬   ‫؛‬   ‫رك‬      ‫‪۳‬‬
143:====LEAF 425
149:                                         ‫باشد سیاه رنگه ‪.‬‬            ‫نردان خا پکیزنابه از باريك‬
198:              ‫کاروانی دیگرم بخشید بختی جمله رنگه *‪.‬‬                           ‫کاررانی بیراکم داد جمله بارکش‬
203:        ‫مراازآن لب باقوت رنگه‌باند رنکه» دلت فری‪.*۱۹۷‬‬                                ‫مکر چو پرد* شرم ازمیانه بردارد‬
205:====LEAF 426
206:‫رنگه رییع‬                                                                                    ‫‪-0‬‬
227:‫را لز‬    ‫و محیل‬     ‫دهنده‬     ‫و فرب‬   ‫بر آورد ‪-‬‬        ‫رنگه بمعنی‌خودرو ورنگیدن بمعنی‌روییدن بود‪.‬‬
246:‫سفید کردن بکار برند و آنرا سنگه برکان هم‬                ‫کی‌طمعی وتوقمی‌دارد کوبند «رنگی برونداری»‬
248:‫ازرنگ برفرار‬        ‫لکستنا=به‬‫نگ‬ ‫ر‬                       ‫‪٩٩-‬‏‬      ‫خال ونقطة سیاهی که برجامی گذارند ‪۰‬‬
256:  ‫( یکنوع مز کوهی )‪ ۱‬اسشق ‪4۲٩‬‏ ‪ 5‬درنگه ‪ ,‬گوسیند‬                     ‫‏‪ ١‬در سالسکومت‪10 -‬‬
263:                              ‫‪ «۴‬رنگه‪ ۰‬حیلت و وستانبافشدرخ»ی (سیستانی) فت ‪:‬‬
264:     ‫که کاه جتن ازآنجا چگونه سازد رنگه ‪».‬‬                        ‫ور ببجنگه یاز آبدش بدان کوشد‬
267:   ‫‪ -‬رك ‪ :‬ریگ آوردن ورنگه بر آوردن ‪۰‬‬                      ‫‪.‬‬     ‫ده‬
274:         ‫زهر چه رنگه تعلق پذیرد آزاد است‬                      ‫غلام همتآنمکه زیر چرخ کبود‬
276:         ‫رك ‪ :‬رنه » رنگه آوردن ‪۱‬‬           ‫‪_ 4‬‬         ‫ریگ بر آوردن ‪۰‬‬         ‫‪ :‬ریگ‬    ‫رك‬    ‫‪¥‬‬
279:                                                                                ‫آرا رنگه کند» صباغ‪.‬‬
281:====LEAF 427
282:   ‫نت‬                                                                                          ‫رنگه رزگلگون‬
288: ‫رنگیدن = بر وزن لنگیدن ‪ ,‬روسدن‬                        ‫ر نگر و تا د بکر اول وسکون ثالی‬
295:‫ر نگینا = بانون بالف کشیده‪ .‬شفترنگه‬                    ‫در‬      ‫معروف‬       ‫است‬      ‫جاتوری‬    ‫آن‬     ‫و‬       ‫»‬   ‫گوند‬   ‫را‬
298:‫زرنگینان ‪ -‬بکرشوتزنیبان » بمعنی‬                                                                      ‫‪۰ ۱‬‬         ‫آمده است‬
304:                               ‫کمان‪ -‬بنح‌کان‪,‬‬              ‫اشبمر‌فروش وابر‪:‬شم گرورنگه رزباشد‪ -‬ومحیل‬
316:                                                                   ‫وفریب دهنده باشد ‪ -‬ورنگه رز‪ -‬وآ‬
322:                                                                                                             ‫رنگه کنند ‪۰‬‬
353:====LEAF 428
368:‫روان = بفتح اول و الیبالف کشیده‬                                     ‫وآب تیره رنگگ را نگیفزته‌اند » وبضم اول حم‬
```


## [2026-09-14T01:17:24.791Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==426' BQT_v2_pages.txt | sed -n '40,80p'",
 "description": "Print BQT leaf 426 footnotes"
}
```


### [2026-09-14T01:17:25.698Z] TOOL RESULT

```
                                                                                         ‫‪ ۷‬ک‬
‫سفید کردن بکار برند و آنرا سنگه برکان هم‬                ‫کی‌طمعی وتوقمی‌دارد کوبند «رنگی برونداری»‬
                                                       ‫‪ ۷‬سب‬         ‫لمتوانی کرد »‬      ‫سمنی أخذ و جری‬
‫ازرنگ برفرار‬        ‫لکستنا=به‬‫نگ‬ ‫ر‬                       ‫‪٩٩-‬‏‬      ‫خال ونقطة سیاهی که برجامی گذارند ‪۰‬‬
                          ‫وبی‌تفیر باشد ‪.‬‬              ‫شدن ‪۰‬‬        ‫ب‬‫ومل‬‫خر ف‬
                                                                           ‫شیرین کاری بعنی مصد‬
               ‫ر نگ ر بیع = بکس‬                          ‫جمالت‬   ‫‪ - ۰‬جلاجل دایره ‪۳ ۰‬ب‪۱‬ا‪-‬خخش‬
                         ‫رواج ورونق بهار باشد ‪۰#.‬‬       ‫آمیخته ‪ -۷۲۳ ۴۰‬شرم وحیا ‪-۵.۳۳‬داراستی‬

                                                                   ‫(‪ )۱‬چك ‪ ,‬چش ‪ :‬ظافت ‪.‬‬

  ‫( یکنوع مز کوهی )‪ ۱‬اسشق ‪4۲٩‬‏ ‪ 5‬درنگه ‪ ,‬گوسیند‬                     ‫‏‪ ١‬در سالسکومت‪10 -‬‬

                                                          ‫)وید ‪:‬‬
                                                               ‫وبز کوهی باشد ‪ .‬فرخی (سیستانی گ‬
         ‫هید گاه زبهر زه کومان نرونگه ‪» .‬‬                        ‫ز سر ببرد شاخ وزتن بدرد پوست‬
   ‫‪. ۰‬‬   ‫‪ 2‬لت فری ‪۱۲‬‬

                              ‫‪ «۴‬رنگه‪ ۰‬حیلت و وستانبافشدرخ»ی (سیستانی) فت ‪:‬‬
     ‫که کاه جتن ازآنجا چگونه سازد رنگه ‪».‬‬                        ‫ور ببجنگه یاز آبدش بدان کوشد‬
                                                                                            ‫ک‬
   ‫« لت فری ‪. > ۱۹۲‬‬
   ‫‪ -‬رك ‪ :‬ریگ آوردن ورنگه بر آوردن ‪۰‬‬                      ‫‪.‬‬     ‫ده‬
                                                                 ‫امین‬
                                                                    ‫م‪ ۲‬ه‬
                                                                       ‫رك ‪ :‬شمارء ‪۳‬‬         ‫‪۳‬‬
             ‫و آزادان از تعلقات مادی ‪:‬‬            ‫‪۱‬‬           ‫‪۸۱‬همین ماده ‪.‬‬     ‫رة‬
                                                                                 ‫ا‪:‬‬‫مرك‬
                                                                                     ‫ش_‬‫®‬
         ‫زهر چه رنگه تعلق پذیرد آزاد است‬                      ‫غلام همتآنمکه زیر چرخ کبود‬
   ‫«حافظط شیرازی ‪.* ۷۲‬‬
         ‫رك ‪ :‬رنه » رنگه آوردن ‪۱‬‬           ‫‪_ 4‬‬         ‫ریگ بر آوردن ‪۰‬‬         ‫‪ :‬ریگ‬    ‫رك‬    ‫‪¥‬‬

   ‫* رلگرو ‪ -‬بقتح اول وچپارم » از ‪ ::‬ریگب ‪ +‬رز (رزیدن) (ه‪.‬م‪ .).‬کسکه بارچه وجز‬
                                                                                ‫آرا رنگه کند» صباغ‪.‬‬
```


## [2026-09-14T01:17:32.441Z] TOOL CALL #52: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1878 2>&1 | head -60",
 "description": "Fetch BQT page 1878"
}
```


### [2026-09-14T01:17:33.711Z] TOOL RESULT

```
REF: BQT:1878  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 675  OCR-lang: fas

لآغون -۱۸۷۸-
دیگر آبستن نشود و اگر بخود برگیرد آبستن | کشاده و خوبشتن ستایی و خودسایی باشد ۷ -
کردد ۱ . و بیخیا و بیخیابیرا نیز کوبند .
لاغون ؟ - بروزن هامون ,بلغترومی لاقیس ۸ - بافای بتختانی کشیدموبسین
بیعنی لاغوس باشد که خرکوش است . بی‌نقطهٌ زده » نام دیوی است که مردم را در نماز
لاغینه - بروزنآدینه » درختی‌است(۱) وسوسه‌کند ؛ و باین معنی بجای حرف‌ئثالك قاف
که آب از بالای آن بتدریج فرود آید و جمع هم بنظرآمده است .
شود ؛ و باین معنی بحذف نون هم بنظر آهده لا لگ - بروزن خاك » بمعنی طفار وکاسه
است که لاغیه باشد ؛ و بجای نون نای مثلئه هم | اوكاسة چویین باشد ‎٩‏ - و لاله پشت و کاسه پشت
ذیده شده امت که لاغیئه باشد اّاعلم ۴ . را نیز کوبند *۱- و نام رنگی است مشهور ۱۱
لاغمیه ؟ - بر وزن بادیه » نباتی است | که درهندوستان بهم میرسد و بدان‌چیزها رنگه
وآ بر گلی‌باشد مانن د کل شبت و زنبور عل‌کل | کنند و آن شبنمی باشد که بر شاخهای درخت
آنرا خورد وچون‌ب رگی‌با شاخی ازآن جداکنند | کنار و درختهای دیگر نشیند و منجمد کردد
شیر بسیاری از وی برآید . گرم و خشك امت | وآلرا بگیرند و بکوبند و بیزند . ازآن رنکه
درسیم » اگر از چوب آن برآبی که ماهی‌داشته | سرخی حاصل کردد که مصوران و نقاشان هم کار
باشد اندازند همه ماهیان بر روی آب افتند - | کنند و غازة زنالرا نیز ازآن سازند ونغالةٌ آن
و در عربی سخن باطل وزن بیهوده کوی را | مانند صمغ باشد , و بدان کارد وشمشیر وخنجر
کربند 9 . وامثالآ ترا دردسته محکم کنند و بکارهای‌دیگر
لاف ۱ - بروزن‌کاف » کلام‌فتول‌وعبارت | نیز هیاید - واهر چیز ضایع و زبون را نیز
(۱) لغت نامه :۳ ( منبت او در پستی کوه باشد که ) برای تکمیل عبارت افزوده شده.
۱ رك : خرکوش . ۴ - رك : لاغوس . ۴ - رك4 : لاغیه .
۴ - در عقار ۲۱۵ آهده : « لاعية ( با عین مهمله ) هی الحلبلاب » و بعجمية الاندلی
لختربوله ( 1301871018 ) و قد ذکرناها من اصناف الیتوع .> در بض دخ مانند ابن البیطار
« لاغیه » آمده ولی صحیح با عين مهمله است - ۷0110706 (قر) « عقار ۷۱۵ ف >.
‎٩‏ - رك : منتهی‌الارب ؛ و رك : لاغ - ‎٩‏ - پهلوی 13 ( شکایت ) « منای
* ۲:۷۸ کردی 18۶ و 12۷ ( سخن بیپوده ) « ژابا ص ۳۷۵ .
۷ -ایاز بیم زبانم نزندگشته وهاژ کجا شد آنهمه دعوی و لاف وآنپمه ژاز ۲
لبیسی ۸« لغت نامه » .
۸ -ظ . مصحف لاقیس ( هی ککتف ۰ فوس کننده و بدی اندازنده میان مردم ...
لفن عیب کردن « منتهر.الارب > ) :
نو کفتی که عفربت لاقیس ( لافیس ) بود بزختی نمودار ابلیی بود .
سعدی شیرازی « رشیدی > « لغت نامه ؟ .
‎٩‏ لاوکه ۰ ۱۶ جلد خزفی‌ض جانوران. ذبل سنگه پشت . اقص:لا پشت.
۹۱ لك << 6 . در بونانی 18۳3۳2 ۰ فرانوی 180406 » از هندی متوسط 1۸۴152
کرفته شده . بضی پنداشته‌اند در قرن اول و دوم مبلادی باروپا رسیده . ولی مانن دکكلمهٌ غندی
فلفل, پیشتر بیونان رسدهء‌بود (353 .0 ,02626761۷ ۸۵۵6 ,6ناوناهاو۸ 70۲2۸1 )
بنلم 7.۳11110281 . و رك : دزی « لك > . ورد : 0۰585 ,1۳880162 - 5100 گنها
```


## [2026-09-14T01:17:33.995Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFM lajj\"; grep -n \"لج\\b\\|( اللج )\\|اللجة\\|لجة\" AFM_pages.txt | head -20",
 "description": "Grep Addi Shir for lajj"
}
```


### [2026-09-14T01:17:34.056Z] TOOL RESULT

```
=== AFM lajj
78:كانوا بالجزيرة مجاورين لليونان ٠‏ و بكر للهند والدشة . وعمد القس وازد مان انا
105:الفارسية ܢܐܬ واخاء بالخاء والماء الفارسسة بالفاء او بالماء )ܝ بالقاف ٠‏ والجيم
128:ويعان المترجم في مقدمته انه زاد على الكتات 1 حثيرة اخدها م ن الج
184:ܨ (( 56( الحارض الضعيف من القوم و عو لجل 955
272:د لجع ١‏ يء يلتف على شجر الوط والصنو بر كأنة مقشود من عرق وهو
326::8 من الننهات الست ت الموجودة في 0 ولجموعها 5 شّش واه وهي هذه :
693:+ (المليكج ) شجر في حجم الزيتون 8 قريب الطبع ٠‏ ن الأملج 100
815:رد وقال غيدهم ضرب من الجواهر ( البيهان ܘ
876:وهو من مننولات البلتم ويعرف بعشب الجبل .£
972:` الجل القصيد < ب كهتر وهو ܐ م 6 أي صخيد ومن ثر وي
980:* (المحنبار 1 ܐܐ( الجل = والعظيم !+ ܙ العظي
1031:الجريال المعرب ٠‏ ويون الفارسي تصحيف كون وقالوا 0 ` لونة لون النار
1038:+ ( الجيرون ) ܓ يبت 9 وهو السراج
1039:ܨ (الجراهية ) من الامور عظا 0 3 2 ܨ اي جلبتهم معرب
1042:(الجَروهق ) ما مع مستديرًا كهيئة الكبّة مه معرب ¥ £ 10(
1044:± (الجزير) بلغة اها ل العراق من يختاره اهل القرية لما ينوبهم من تفقات من
1085:المدش ܒ الضجيج 0 ٠‏ اذا الجَلَس اختلاط 511 في !ܥܨ ܝ ܪ̈ܝ ܝܐ
1090:× (الجلغل ) تعيب كل وه العرش ܐܒ 6 ܚܨܐ
1091:“د (الجَلّخ ) 7930 بها السكين ܕܧܕܩܐ تعريب 5 آلة 123 ݂ܟ
1093:* ( الجْلندى والعْلندّد ) الفاجر معرب كلنده
```


## [2026-09-14T01:17:53.268Z] TOOL CALL #54: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1900 2>&1 | head -50",
 "description": "Fetch BQT page 1900"
}
```


### [2026-09-14T01:17:54.388Z] TOOL RESULT

```
REF: BQT:1900  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 697  OCR-lang: fas

له خلیفه ۱۹۰۳
ندیه خلیفه > نام نوعی‌ازحلوا باشد. لقوه ؟ - بفتح اول بروزن فعوه, علتی
لفوماش ۱ < بنج ال ۶۳۳۵ | جي مدرد کرین جکایهای ساختاش

رسیده و میم بالف کشیده و بشین نقطه‌دار زده » ساحب لفوه چون درآن بیند صحت پاید - وور
نام پدر ارسطاطالیس بوده : عربی‌شتری را گوبند که زودآبستن شود -وبکس
لقومه ؟ - بنتح ول و میم » بمعنی | اول هم درعربی » عقاب ماده را گوبند ؛ وبممنی

لقوماش است که پدر ارسطاطالیی باشد . اول نیز بعضی کویند عربی است .

بیان شانزدهم
درلام با کاف تازی مشتّمل بر پانزده لغت
لت - بنتح اول وسکون نانی, صدهزار باشد و خواه کهته - و داغ و لكکهٌ جامه واغیر
راآگونند پمنی عدد هرچیز که صد هزار رسید: آنرا هم میگوبند ۷ - و نام طابقه ای باشد از
آنرا لك خوانند ۴ - وبمعنی ابله واحمق‌ونادان | کردان صحرانشین ۸ - و بیموی و صاف را نیز
هم‌هت ‎٩‏ - وسخنان بیهوده و هرزه و هذبانرا ۲ کوبند ‎٩‏ - وبم‌اول » هرچیز کنده وناتراشیده
نی ز کوبند ‎٩‏ - و جامه ولتهٌ کهنهٌ باره پاره شده | باشد ۱۶ - و کلوله (۱) و برآهد کی وگره
و رختی و لباسی که مردم روستا پوشند خواه لو | که در اعضا بهم رسد - ورنگی است مشهو رکه

(۱) چك + وگره .

۱ - مصحف « نقوماخی »> « الفپرست ص ۳4۵ > 871008386815 ( انگه ) ۰
( 311602006 فر ). ۴ رد :جح ۰.۱ ۴ - (عر ) ۸ لقوة بالفتح » بیماری
کجی دهان و روی از علت - و نیز لقوة دیگر . زن زود بارگی رکه در اول دفعه بارگیرد, ناقة
لقوة کذلکه ... ونیز لفوه عقاب ماده - با زن شتابکار چست وسبك . لقاء ککاء والذاه جمم. »
منتهی‌الارب > . ۴ - هندی است « غیاث » در هندوستانی لاک , از سانسکریت «ژابا
ص *۳۸ 6 :

دران نه سایر ماند و نه طایر از برخاك دو لك ز لشکر او شد بزبر خاك نهان .
عنصری بلخی « لغت نامه » .
9 < لوك .
‎٩‏ -گفت ریمن مرد خام لك درای پیش آن فرتوت پیر زار خای .
۱ لبیمی ۸« لخت نامه ».

۷ -فی : لکه. ۸ - لابقه ای از ابلهای کرد ابران که درکلیائی کرماناه و
همدان واصقهانو کردستان و اسفند] باد وچهارکاوه وعلی‌وردی مسکن دارند. رك : کیهان,جغرافیای
سیاسی ص ‎٩۳‏ - ونیز نام طایقه‌ای از طوایف قشقائی «کیهان . جغرافیای سیاسی ص ۸۳>. و هم
طابفه‌ای از زندیه که آن خود بردو بخش بود : یکی لك و دیگری زند که آنرا ۸ زندلکی » و
اسطلاحاً «زنلکی» گوبند و اکتون فم در اطراف عراق و سلطانآباد مشغول حشم داری میباشند
«بادگارسال دوم شمارة ۱۹۰۷ ۰ ‎٩‏ * لق < لم. ۱۶ درافغاستان بممنی‌کلفت ولکی‌است,
```


## [2026-09-14T01:17:54.978Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -5 AFM_pages.txt; echo \"...\"; grep -n \"pdf page\" AFM_pages.txt | sed -n '135,150p'",
 "description": "Inspect AFM pages structure"
}
```


### [2026-09-14T01:17:55.047Z] TOOL RESULT

```
8
0
ܥܝ
ܶܡ 7
ܫ ܢ 0 ܣܚ
...
```


## [2026-09-14T01:18:10.630Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in AFM.txt AFM_alt.txt AFM_pages.txt; do echo \"=== $f\"; grep -n \"اللج\\|( اللجة\\|لجة )\\|اللجّ\" $f | head -10; done",
 "description": "Grep AFM variants for lajj"
}
```


### [2026-09-14T01:18:11.710Z] TOOL RESULT

```
=== AFM.txt
3523:1 4 ܨܐ }ܝ ܢ والفضة من ܗܘ واللجام ܨ | ܕ عن ܝ 0 
5735:ܐ اللجام ) تعريب لكام وهو بالارامسة ܠܓܡܐ ܠܘܓܡܐ وباحدشة 1010 + 
=== AFM_alt.txt
1782:الت فيها خلق جناب الق جل رعلا جميع الكائنات ٠‏ تقل اللجوس في كاب الزن 
3344:ا ما صنع من الذهب والفضّة من السرج واللجام والركاب ١او‏ عن استون ومعناه 
5582:٭ (الكىلجة ) كمل معروف لاهل العراف رهی 3 وسعة امان ا تعر یب کله 
5594:( اللجَام ) تعریب لام وهو بالارامیة 8 لېد وبالشة صژاعء! 
=== AFM_pages.txt
2165:1 4 ܨܐ }ܝ ܢ والفضة من ܗܘ واللجام ܨ | ܕ عن ܝ 0
3607:ܐ اللجام ) تعريب لكام وهو بالارامسة ܠܓܡܐ ܠܘܓܡܐ وباحدشة 1010 +
```


## [2026-09-14T01:18:17.853Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"اللك\\|( اللك )\\|اللكّ\" AFM_alt.txt | head -10; echo \"=== leaf of لجام\"; awk 'BEGIN{RS=\"\\f\"} {n++; if ($0 ~ /اللجَام/ || $0 ~ /اللجام/) print \"leaf\",n}' AFM_alt.txt | head; echo \"=== total leaves\"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' AFM_alt.txt",
 "description": "Find AFM lak and lajam leaf"
}
```


### [2026-09-14T01:18:18.927Z] TOOL RESULT

```
291:( الأسكجة واللك ت6ا ماما اا 0 
1812:٭ ( الكو ار) الاء اللكثير التعير تعريب جور وهو القدح الملفحان 
2147:+ ( الخال واللكّل واللخّل ) حلبة من فة او من ذهب تلسها النساء في 
3390:EI اللك النعان بن اعرء القاس بن اوس‎ e السدير)‎ ( 3¢ 
3828:ومشر 4 .ونا مات أعر اللك ان يكن ضدفن بعر واكام وتنفّش صورتة على قر . 
3938:الشاروف ) اللكنسة تعريب حأروب . والظاهر ان الكامة اراميّة الاصل‎ ( 
5224:ضا ا دودة صغارة تعس ف اء Ra‏ الصغار من ٠ ET‏ وقىل هو اللك 
5611:ا واللكن لغة فيه تعريب لكن ومنة السر باذ حص .والترك لن 
5997:ايضاً ٠‏ وسات مته نوروز الاصة ان اللك شد ا جاس على مز بے لاطت 
6096:# (اللك) شجر الدب وقيل الزعءرور فارساتة لك وهو الزعرور ويقر به الأرنسي 
=== leaf of لجام
leaf 1
=== total leaves
1
```


## [2026-09-14T01:18:24.813Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json;d=json.load(open('refs_online.json'));print(json.dumps(d['AFM'],ensure_ascii=False,indent=1))\"",
 "description": "AFM ref details"
}
```


### [2026-09-14T01:18:25.994Z] TOOL RESULT

```
{
 "title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)",
 "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"
 ],
 "page_offset": "198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image",
 "covers_etymology": true,
 "notes": "Arabic OCR fair; Syriac/Latin etyma partially garbled.",
 "cites": "page number of Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba (1908)"
}
```


## [2026-09-14T01:18:29.279Z] TOOL CALL #59: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py AFM:141 2>&1 | head -40",
 "description": "Fetch AFM page 141"
}
```


### [2026-09-14T01:18:30.376Z] TOOL RESULT

```
no scan of AFM covers printed page 141 (see 'scans' in refs_online.json)
```


## [2026-09-14T01:18:33.657Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} END{print \"AFM_pages leaves:\",NR}' AFM_pages.txt; awk 'BEGIN{RS=\"\\f\"} {n++; if (n>=147 && n<=152) {print \"====LEAF\",n,\" printed~\",n-8; print substr($0,1,900)}}' AFM_pages.txt",
 "description": "Print AFM leaves near 149"
}
```


### [2026-09-14T01:18:34.722Z] TOOL RESULT

```
AFM_pages leaves: 197
====LEAF 147  printed~ 139
ܚܝܚ @ ܛ¿ | ܝܚ
ܕܪ | آذان الفار. وقال فى البرهان || 3 0 غريثة حق ܝ ܐܢܐ :31
5 3 ابن ܩܙ ; 1 ( 1:10 عرز و 0 وهو فاسي 3 ܬ
بالعر بَة السمسق والعبقر فحق القئا ». والسمسق تعر ܢ اليونالي « ܘܘ
3070 الرماح وهو شجر :> 7 ول ثر 0 0
حجم التوت © كن داغلة نواة مستطية تعريب مران 5 له سجر الرماح لان
كات 09 7 والسهام وهذا الشجر كثير الوجود في قرى 33 في قضاء
109 ديسو ¦[ وت زعم 4 ܨ[ ܡ̄ܘܪܢܝܬܐ وهو نوع من من الرماح ܢ اصل
3 + ; 1
)04( 0 036 ܡ ومن بان اي حافظ 95 وبال
)9 01 الَأ ومرزبالي. ازا
( ܐܠܝ ) دار المرضى تصحيف بوارستان وهو عركب من يار اي مريض
ومن ܚ اي حل المريض ٠و‏ ي
====LEAF 148  printed~ 140
ܕ 311 تب
( الأست) كامة فارسية اسم للبن ومنة التكردي ,)ܝܝ و ܡܣܬܐ بالسريايّة
الدارحة
(ل) ل قيل فارسي ° ( يط الحيط) والصواب !2 تري
0 المس) النحاس 7
+ ܢ الغلام اسن 85 والوحه 39 00 7 5 امن ܘܟ 0
~ ÷
( !]ܚܝ ) فاسي خض وهو 3 الكف ومنة - بالتركة » 2
0 نوع من اطيب :9 فاسي ܕܫܐ ܐܘ ام ام اللرذان ܠܝ الفرس ]
سمعوا بام جرذان وهي كع صفراء قالوا ܐ جاغوا:« اين موثمان» ( اقرب
ܬܕܐܙܒ) ܕܐܐ ܐ نه
( | هد ) اللقاح 09 وقيل 00 ( 3 .قال في شفاء الغليل 1 `
عق الباذجان معرب
(اللان) 3 مان ܕܬܕ كل عار مانع
(الأملم) دواء ٠‏ وهو ܳܨ ܚܨ ينبت في الهند معرب 11
(النج) منك ك وهو حب ا�
====LEAF 149  printed~ 141
< 3:(+ 3 3
يضعون عليه قليلا من اللح ٠‏ فبقدر ما كان يذوب الملح كان الماجنون يخاو ܬܨ تلك
الاحجار الدقيقة الى الخارج
مانيذ ) الجرية: بقيتها مأخوذة من مأرنيده اي 01
+ 0 5144 ܨܢ منش )3 10 الهّة ويوافقفة ܨ 1165
والانتكليزي 11170 ܕܐ ريق 14 اي فكر ونأ ܨ
0 )ܕܐ )381 05 7 موتر اي‎ ١
ܢ‎ 491 3
1 2 ܝ الغنى مأخوذ من معيكار اي دأ به العظمة
1 الخاتم فارسي 59 فعا وقالوا مهرَ
ܫ 0 الور ܟ واصل 1 0 حافظ |
7 0 0 6 90 49577 35 610 والعاؤقة
جان) عد الفرس مركب من 3309 331
06 (3061 ܚܚ اول الشماء 0 نقدم عند ܨ 3 0:3 0-3 بق في ܡ
وهو اليوم السادس عشر من شهر « ܝܢ * وذلك عند نزول ܐܚܨ ا >
ل�
====LEAF 150  printed~ 142
د < 35
3010 رةه كامت النساء 3 1011 لعة فيها ܐܠܝ تمر يبب هر رهي
خرزة لوا ` كاون المرجان
ܢ مره
# ( مضل ) 5 5 مركب من مه اي كبير وسالي لي .مسن
1 ܨܝ § البأورة تعريب مما وهو حجر شه 5 وقيل هر ܐܐ تبه
ملو ول يوان فقيه الفرس ܠ المجوس 3:5( وججعة
ܨ
( لوم ) ببى الشبع فارسي تكلموا 4 0:27 ܨ
(ليَة) فشر بشىء من ܇ الأدرية ܣ من ܐܝ اي الخير 1:0 يبه اي
ܝ
( الميبحتج » العنب المطبوخ مركب من تمي )1١(‏ اي <> ومن إبخته اي مطبوخ
وهو عسبل العنب ١‏ كن الاطباء يغلونة مرة ثانية »= والعسل
4 فشحة مجبهة همده 18 رلم اليل قل كلمن انام 1ه
ܨܐܘ واضبطرابه عند السباق٠وق
====LEAF 151  printed~ 143
_ 4¿ ܙ -
وا لندة 80( 3 اما فرتكل 5 ان اللاندة تعريب 1 `
(ص: ܥ )
6( بالياء 9 بهمزة ܓ 5( فيها الماء والمثقب ويقال
2 وصفها ابن السكيت والفراء وابو حاتم ٠‏ وفي التهذيب عن ابن الاعرابي : ويقال
اللمازاب 3 0 يتقديم الراء المهمة وتاخيرها ونقله الليث وجساعة ( اقرب
الوارد» :قات ان ܐܠ ܐܢ ܨ ܝܢ من ܘܬ اي بول ومن آب اي ماء ܕܝܙܝ النسمية
ظاهر (راجع ` لكل :4 )
ܣ 10 ® 099 2 من مي اق شراب بم الى"
.܀
ܗܐ
9
١‏ ابابا 6 فول الذي 'يككل به فارسيّة ميل ` = ܟ اله
معرب عن اليونافي «</نم٠‏ فالفارمي ايضاً ܨܕ ܝ عن اليونافى وملة ايضاً
ܡܝܠܐ بالارامسية .وما الم 
====LEAF 152  printed~ 144
ܢ ܀ © | ܝܝܚ
لغتان فيه ٠‏ والظاهر ان الافظة ارامية الاصل ذعي ܐܢܒܘܒܐ باللغة البابليَة
ܕ ܐܝܟ ܨܐܬ و > دنه حدم ܐܬܐ .ܕ % ܨܝ ܨ ܝܨ 811 )ܙ(
ومعئاها الأننوبة والمزمار ܨ ܐ من ܢܒܒ اي صرخ وتخ ٠‏ .وان ܒܝܒܐ
و ܒܘܒܝܐ اى المجرى والة: ناة 885 | ܗ ܐܐ ܨ ]711 (راجع كلمة
ندب في هذا ܐܐܝ “راجع @ فرئكل ص 7١:‏ )
ܨ عر شجرة 0 و يم عاد ܐܒ وتفاحي مكلك انع
(الأنار) فارسي محض اي 21( واصل 0 المت ومنسة الارائئ”
ܐܡܒܪܐ ܙ !ܚܐ او عشمار بالتركة والكردنة 87 ܐܕ 27 000 متنا 101
اواليو الي بومتومن؟ 9 ܬܘ
ܪ الذي يد 90 صوف تعر يس الإريده أي غير روز
ومنه ܢܒܪܢܢܢܐ بالارامسة
```


## [2026-09-14T01:18:44.890Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} {n++; if ($0 ~ /اللك/) print \"leaf\",n,\"printed~\",n-8}' AFM_pages.txt | head; echo \"=== leaves 144-147\"; awk 'BEGIN{RS=\"\\f\"} {n++; if (n>=144 && n<=147) {print \"====LEAF\",n,\"printed~\",n-8; print substr($0,1,1100)}}' AFM_pages.txt",
 "description": "Find AFM lak entry leaf"
}
```


### [2026-09-14T01:18:45.967Z] TOOL RESULT

```
leaf 20 printed~ 12
leaf 88 printed~ 80
leaf 144 printed~ 136
=== leaves 144-147
====LEAF 144 printed~ 136
ܒܝ <
(اللاخشة ) الاإطربة وهي طعام كاخيوط من الدقيق . واللاخوشة ܕ )ܪܫܐ
ܬܰܝܨܳܐ رهى .7 اك
15063 21411 30 54890
)1:00 واللكن لغة فيه تعريب لَكَن ومنة السر 0 ܝܐ 6(
والكردي 1:3 ¢ 2
+ ( اللقّازق ) ويقال ثقائق اسم لأحد الأمعاء وبه سي معى | ام ابعشو و ܐܠܨ .
دس ععاوم 1 م مرب يكبا الغليل ) .قات وهو معرب ܐ نه وهو العصب
بد ( الك ) صبغ 7 ` ܟܝܬ به جاود المعزى تعر يب لك
1 ܫ الرأة القصيرة الذميمة وقيل الطوية الحزية وقيل مقاوب الرهلة
وهي الت لا 5 ܇ ` ني مشا تقلا ( اقرف الوارة؟؟ اتلتهنا وده
عن ܐܚ̈ܐ ܬ ومعناها المرأة الحممّاء
± (اللادّة ) ثوب حرير 598 لاد
(اللوياء » 90547 7( 0108 10595( 109433803
فرنكل ( ص : £ \ ) | ܝܐ مأخوذة من الارامي لله صم" . ويقريا !"ܨ +0084
اي ܐܝܢ
* ( الأور) أبن متوس
====LEAF 145 printed~ 137
د ܨ¿ ܙ عا
ܐܝ اليم
(الألي) آلة من حديد يطين بها تعريب ماله ْ ܝ ܐ فيه
¥= #1 تَميضين مانا ܙܐ فيه عاك اك اكاب 110
* ( المرونة ) ܡܚ ܡ من منت القوم اذا احتملت مُوُوتتهم ( اقرب
ܝ 90 01:3 ± 73000 0003 $ ان المرونة
معر بة عن 2 < ܨ أمدث ٠‏ ܨܐ ܡܐܢܐ بالارامسة
ْ المتراس) ما تست به من حائط ووه من العدو وخشة توضع خلف الباب‎ ١
3 قال ,”ܝܨ 630 تعريب اليونالي 0 - وعلى ظني‎
الفارسي مترس واصل معناه :لا تيكف . وسبس التسمية ظاهر‎
* (المثك) الاتريم ربح فارسّة -
(الج) حب امش 2 ماش ونه الارامي "فح داا 3
0 )080 لغة في الماش او معرب الارائي | تتح" . ومنة ماش بالتركيّة
7 3 00 2
( الأجشون) السفيثة ܐܝ مصبغة تعريب ܘܬܘܨ واصل ا
(الكّدةِ) المعونة تعريب ܢܫܝ
( ܐܠ ܥܳܨܨ ) لس الفسّاق وبي�
====LEAF 146 printed~ 138
ܓ 1 ܐܐܠ
( ܕܙ يون ) سجر ورقة ܐ الزيتون وزهره الى !ܐܩ له ثر كالكير تعريب
2س © ܣܦ
مازر بون
83 اكرت) . 5( بلا ننات وقتل الارض لا مجن 355 ` مرعاها‎ (١+
ܨܝ‎ 3
> ماخوذة عن مرده ܕܘܫܐܐܬܐ‎
* ( !]ܨ ܢ ܣܣ رس ج فقيل ܝܣܝܣ ܤܣ
قات فان كان ܥܠ المرداسنج فهو ܨ عن ܗ ع ܕܬܕ | ܝ امرداسنج ٠‏ وان كان
ون و اموه رج ار ܣ اطبا رن
الفارسى عروه تصحيف العرلي الأروح
15 صغار ,+ شيل كيار الدر ܡ وقبل 2 جان 1 , 0 :
وقال 3990 لا ܨ تانق هو ام م داعي ܨ تقدير زيادة < ܝ 3
5 58 الاصل ٠‏ قلت 0 1 قيل هو مر ‫ من مر وهي من ادوات
التريين ومن جان ومعثاها الروح ٠‏ وهده لكايه موحودة 0 اللغفات فى
مرجان ܙܡ 40 والكر د و تش لحدداة ܐܐ بالارامية 0 أو 03
15 .2 ( 5 : ` 1 ܕܢ 95:5 00 5 26 ܕ 1113101101116
(ننات) بالفرنسة ٠‏ وم
====LEAF 147 printed~ 139
ܚܝܚ @ ܛ¿ | ܝܚ
ܕܪ | آذان الفار. وقال فى البرهان || 3 0 غريثة حق ܝ ܐܢܐ :31
5 3 ابن ܩܙ ; 1 ( 1:10 عرز و 0 وهو فاسي 3 ܬ
بالعر بَة السمسق والعبقر فحق القئا ». والسمسق تعر ܢ اليونالي « ܘܘ
3070 الرماح وهو شجر :> 7 ول ثر 0 0
حجم التوت © كن داغلة نواة مستطية تعريب مران 5 له سجر الرماح لان
كات 09 7 والسهام وهذا الشجر كثير الوجود في قرى 33 في قضاء
109 ديسو ¦[ وت زعم 4 ܨ[ ܡ̄ܘܪܢܝܬܐ وهو نوع من من الرماح ܢ اصل
3 + ; 1
)04( 0 036 ܡ ومن بان اي حافظ 95 وبال
)9 01 الَأ ومرزبالي. ازا
( ܐܠܝ ) دار المرضى تصحيف بوارستان وهو عركب من يار اي مريض
ومن ܚ اي حل المريض ٠و‏ يقال 4 ܢ ܠ خستهخانه
(المرك) المأ برن مأختوذ عن رك اي اموت
د (المزو) ` بيض دقاق برَاقة تقدح منها النار. 71 ايضاً اسم جا
```


## [2026-09-14T01:19:00.007Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%84%D8%AC%D8%A9",
 "prompt": "Give the Arabic etymology of لجة (lujja) 'deep water, main sea' and of the root ل ج ج: is it a native Arabic root (lajja 'to persist'), or a loanword from Persian? Quote what is said."
}
```


### [2026-09-14T01:19:01.295Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T01:19:03.135Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%B2%E0%A4%BE%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A4%BE",
 "prompt": "Give the Sanskrit etymology of लाक्षा (lākṣā) 'lac, red dye': is it derived from *rākṣā / rañj- 'to dye', or from rakṣ- 'to protect', or considered non-Indo-Aryan? Quote the sources cited (Mayrhofer/EWAia, Turner)."
}
```


### [2026-09-14T01:19:10.412Z] TOOL RESULT

```
# Sanskrit Etymology of लाक्षा (lākṣā)

Based on the Wiktionary entry, the etymology is **uncertain**, with three main competing theories:

## Primary Hypothesis: *rakṣa / rañj- Connection

The most developed theory links it to *lakṣa/*rakṣa meaning "red; redness," connected to the root rañj- ("to become red"). Mayrhofer's *Etymologisches Wörterbuch des Altindoarischen* (1996) is cited as the source, though the exact page reference provided is 477, volume 2.

## Secondary Theory: Proto-Indo-European *laḱs-

An alternative traces it to Proto-Indo-European *laḱs- ("salmon, trout"), related to words in Latvian, Middle Low German, and Russian.

## Tertiary Theory: From lakṣa (100,000)

A third proposal derives it from लक्ष (lakṣa, "one hundred thousand"), referring to the insects gathered to produce the resin.

The entry explicitly states the etymology is "Uncertain" and does not favor any single theory decisively. The American Heritage Dictionary and Barnhart Dictionary of Etymology are also cited as references for the lac entry generally.
```


## [2026-09-14T01:19:15.460Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%84%D8%AC%D9%91",
 "prompt": "Arabic لجّ / لُجّة: give the etymology and meanings. Is the root ل ج ج native Semitic (lajja 'to persist, be obstinate; to clamour') and لُجّة 'deep water, main sea' derived from it?"
}
```


### [2026-09-14T01:19:16.849Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T01:19:17.118Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/lac",
 "prompt": "Give the full etymology of 'lac' (the resin) and of 'lakh/lac' (100,000), including Persian lak, Hindi lakh, Sanskrit lakṣā/lakṣa, and any statement about the meaning 'hundred thousand'."
}
```


### [2026-09-14T01:19:22.600Z] TOOL RESULT

```
# Etymology of Lac (the Resin)

**English Origin (1550s):** The word entered English from French *lacce*, displacing the earlier *lacca* (found in medical texts from the early 15c.). This displaced the earlier form and likely absorbed it.

**Medieval Latin to Persian Chain:** The path traces back through Medieval Latin *lacca*, then Persian *lak*, then Hindi *lakh* (Prakrit *lakkha*), finally reaching Sanskrit *laksha* meaning "red dye," whose ultimate origin remains uncertain.

**The "Hundred Thousand" Theory:** According to Klein and Century Dictionary, the Sanskrit term literally means "one hundred thousand" and supposedly references the vast insect populations that gather on trees to produce the resinous substance.

**Alternative Theories:** Other etymologists propose different origins—Watkins suggests Sanskrit *laksha* may derive from an Indo-European root word for "color, dye," while Barnhart hypothesizes a connection to English *lax* or *lox* (salmon), with the resin supposedly named after salmon coloration.

The document notes the original Sanskrit meaning and numerical association but indicates scholarly disagreement about the true source of the word.
```


## [2026-09-14T01:19:29.208Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"lacquer\\|shellac\\|lākṣā\\|laksa\\|lac\\b\" AHD_watkins1985.txt | head -20; echo \"=== reg- dye\"; grep -n -i \"^reg-\\|reg-.*dye\\|To dye\" AHD_watkins1985.txt | head -20",
 "description": "Grep Watkins AHD for reg- dye"
}
```


### [2026-09-14T01:19:29.294Z] TOOL RESULT

```
671:extensions in: a. Old English slim, slime: sLIME; b. Old English slipor, slippery: SLIPPERY; Cc. Old English *slice, smooth (> Middle English slike, smooth): sLick; d. Old English lim, cement, birdlime: LIME; e. Old English lam, loam: LOAM; f. Old Norse s/éttr, smooth, sleek, akin to the probable Scandinavian source of Middle English slight, slender: SLIGHT; g. Middle Dutch and Middle Low German slippen, to slip, slip away, akin to the probable source of Middle English slippen, to slip: sL1P!; h. Middle Low German slépen, to drag: SCHLEP. 2. Suffixed form *lei-mo- in Latin limus, slime: LIMACINE, LIMICOLINE. 3. Suffixed form */ei-w- in Latin oblivisci (ob-, away; see epi), to forget (< “to wipe, let slip from the mind”): OBLIVION, OUBLIETTE. 4. Extended form *(sjleia- in: a. nasalized zero-grade form */i-n-a- in Latin linere, to anoint: LINIMENT; b. Suffixed zero-grade form *li- (< *lig-) in Greek litos, plain, simple: LiToTEs. [Pok. 3. lei- 662.] léi-. Also lei-. To flow. 1. Extended form “/eib- in Latin libdre, to pour out, taste: LIBATION; PRELIBATION. 2. Possibly suffixed extended form */eit-os- in Latin litus, shore: LITTORAL. [Pok. 4. lei- 664.] leid-. To play, jest. Suffixed o-grade form *loid-o- in Latin lidus, game, play, with its derivative lidere, to play (but both words may possibly be from Etruscan): LUDICROUS; ALLUDE, COLLUDE, DELUDE, ELUDE, ILLU- SION, INTERLUDE, PRELUDE, PROLUSION. [Pok. leid- 666.] leie-. To waste away. Zero-grade form “li- (< *lia-) in Greek limos, hunger, famine: BULIMIA. [In Pok. 2. lei- 661.] leig-'. To bind. 1. Germanic */ik- in Middle Low German lik, leech line: LEECH?. 2. Zero-grade form */ig-d- in Latin ligare, to bind: LEAGUE!, LEGATO, LIABLE, LIEN, LIGASE, LIGATE; ALLOY, (ALLY), COLLIGATE, COLLIGATIVE, FURL, OBLIGE, (RALLY), RELY. [Pok. 4. leig- 668.] leig-?. Poor. Perhaps Greek oligos, few, little: OLIGO-. [Pok. 1. leig- 667.] leig-5. To leap, tremble. O-grade form */oig- in Germanic *laik- in: a. Old English -lac, suffix denoting activity: WEDLOCK; b. Old Norse leika, to play: LARK?. [Pok. 3. leig- 667.] leigh-. To lick. 1. Greek leikhein, to lick: ELECTUARY. 2. Zero-grade form *lig- in Germanic *likk6n in: a. Old English liccian, to lick: Lick; b. Old French lechier, to live in debauchery: LECHER. 3. Nasalized zero-grade form *ling- in Latin lingere, to lick: ANILINGUS, CUNNI- LinGus. [Pok. leigh- 668.] leikw-, To leave. 1. Basic form *leikv- in Greek leipein, to leave: ECLIPSE, ELLIPSIS. 2. O-grade form *loikv- in: a. Germanic */aihwnjan in Old English lénan, to lend, give (< “to leave to”): LEND; b. suffixed form *loikv-nes- in Germanic */aihwniz in Old Norse Jan, loan: LOAN. 3. Zero-grade form *likv- in Germanic *-lif-, left, in: a. Germanic *ain-lif-, “one (beyond ten),” in Old English endleofan, eleven (see oi-no-); b. Germanic *twa-lif-, “two left (beyond ten),” in Old English twelf, twelve (see dwo-). 4. Nasalized zero-grade form *li-n-kv- in Latin linquere, to leave: DELINQUENT, DERELICT, RELINQUISH. [Pok. leike- 669.] leip-. To stick, adhere; fat. 1. Germanic *libam in Old English Jif, life (< “continuance”): LIFE, LIVELY. 2. Ger- manic “libén in Old English lifian, libban, to live: LIVE}. 3. Germanic */aibjan in Old English léfan, to leave, have remaining: LEAVE!. 4. Germanic “libro in Old English lifer, liver (formerly believed to be the blood-producing organ): LIVER}. 5. Zero-grade form *lip- in Greek lipos, fat: L1po-. 6. Variant form *aleibh- in Greek aleiphein, to anoint with oil (> aleiphar, unguent): ALIPHATIC; SYNA- LEPHA. [Pok. eip- 670.] leis-'. Track, furrow. 1. O-grade form *lois- in: a. Ger- manic */aist- in Old English Jast, lést, sole, footprint: Last’; b. Germanic */laistjan, “to follow a track,” in Old English /éstan, to continue: LAST?; c. suffixed form *lois-G in Germanic */aiz6 in Old English Jar, learning:
739:melg-. To rub off; also to milk. I. 1. Zero-grade form *mig- in Latin mulgére, to milk: EMULSION. 2. Full-grade form *melg- in Germanic *melkan, to milk, was contami- nated with an unrelated noun for milk, cognate with the Greek and Latin forms given in II. below, to form the blend *meluk- in: a. Old English meolc, milc, milk: MILK; b. suffixed form *meluk-ja-, giving milk, in Old English -milce, milch: MILCH Cc. Old High German miluh, milk: MILCHIG. II. Included here to mark the unexplained fact that no common Indo-European noun for milk can be reconstructed is another root *g(ajlag-, *g(a)lakt-, milk, found only in: a. Greek gala (stem galakt-), milk: (GA- LACTIC), GALACTO-, GALAXY; AGALACTIA, POLYGALA; b. Latin lac (stem lact-), milk: (LACTATE), LACTEAL, LACTESCENT, LACTO-, LETTUCE; C. the blended Germanic form cited in I. 2. above. [Pok. melg- 722, glag- 400.]
776:sively, very (< *ne-mi-s, “not little”; *mi-, little; see mei-2): NIMIETY. 4. Latin nihilum, nothing (< *nehilum, “not a whit, nothing at all”; hilum, a thing, trifle; origin unknown), contracted to nihil, nil, nothing: NIHILISM, (NIHILITY), NIL; ANNIHILATE. 5. Latin non, not (< *ne-oinom, “not one thing”; *oino-, one; see oi-no-): Non-. 6. Italic *nek, not, in: a. Latin prefix neg-, not: NEGLECT, (NEGLIGEE), NEGOTIATE; b. Latin negdre, to deny: NEGATE; ABNEGATE, DENY, RENEGADE, (RENEGE). 7. Greek né-, not: NEPENTHE. 8. Zero-grade combining form *n- in: a. Germanic *un- in Old English wn-, not: uN-!; b,. Latin in-, not: IN-1; c. Greek a-, an-, not: A-}, (AN-); d. Sanskrit a-, an-, not: AHIMSA, AMRITA. [Pok. ne 756.] nebh-. Cloud. 1. Suffixed form *nebh-lo- in Germanic *nibla- probably in Old Norse nifl-, “mist” or “dark”: NIFLHEIM. 2. Suffixed form *nebh-eld- in: a. Latin nebula, cloud: NEBULA, NEBULOUS; b. Greek nephelé, cloud: NEPHELINE; NEPHELOMETER. 3. Suffixed form *nebh-es- in Greek nephos, cloud: NEPHOLOGY. 4. Nasal- ized form *ne-m-bh- in Latin nimbus, rain, cloud, aura: NIMBUS. See ombhro-. [Pok. (enebh-) 315.] ned-. To bind, tie. 1. O-grade form *nod- in: a. Germanic *nati- in Old English ne¢(t), a net: NET!; b. Germanic *nat-ilo, a nettle (nettles or plants of closely related genera such as hemp were used as a source of fiber), in Old English netel(e), netle, nettle: NETTLE; c. Germanic *nat-sk- in Anglo-Norman nouch, brooch: OUCH?. 2. Lengthened o-grade form *nédo- in Latin nédus, a knot: NODE, NODULE, NODUS; DENOUEMENT. 3. Re-for- mation of the root in Latin nectere (past participle nexus), to tie, bind, connect: NEXUS; (ADNEXA), ANNEX, CONNECT [Pok. 1. ned- 758.] negwh-ro-. Kidney. Greek nephros, kidney: NEPHRO-; MESONEPHROS, METANEPHROS, PERINEPHRIUM, PRO- NEPHROS. [In Pok. eng¥- 319.] negw-ro-. Adjective denoting various colors; with deriva- tives like Greek nebros, “fawn.” Latin niger, black: NEGRO, NIELLO, NIGRESCENCE, NIGRITUDE; DENIGRATE, NECROMANCY, NIGROSINE, [néhw-iz. Near. Germanic root. Old English néah, near: NEAR, NEIGHBOR, NEXT, NIGH.] nei-. To be excited, shine. 1. Suffixed form “nei-to- in Germanic *nitha-, animosity, in Old Norse nidh, scorn (> nidhingr, villain): NIDDERING. 2. Suffixed zero-grade form *ni-to- in Latin nitére, to shine: NEAT!, (NET?). 3. Possibly Persian nil, indigo: ANIL, LILAC. [Pok. 2. nei- 760.) neie-. To lead. Sanskrit nayati, he leads: NAINSOOK. [Pok. 1. nei- 760.] neig’-. To wash. Germanic *nikwiz, *nikuz in Old High German nihhus, river monster, water spirit: NIx!. [Pok. neigt- 761.] nek-', Death. 1. Latin nex (stem nec-), death: PERNI- cious. 2. Latin necdre, to kill: INTERNECINE. 3. Suffixed (causative) o-grade form *nok-eyo- in Latin nocére, to injure, harm: NOCENT, NOCUOUS, NUISANCE; INNOCENT, INNOCUOUS. 4. Suffixed o-grade form *nok-s- in Latin noxa, injury, hurt, damage: NOXIOUS; OBNOXIOUS. 5. Suffixed full-grade form *nek-ro- in Greek nekros, corpse: NECRO-, NECROSIS; NECROMANCY. 6. Greek nek- tar, the drink of the gods, “overcoming death” (*tar-, overcoming; see ter@-2): NECTAR, (NECTARINE). [Pok. nek- 762.] nek-?. To reach, attain. I. O-grade form *nok- in Ger- manic *ga-nah- (*ga-, intensive prefix; see kom), “satis- fies,” forming *gandga-, sufficient, in Old English gendg, enough: ENOUGH. II. Variant form “enk-. 1. Redupli- cated in Greek enenkein, to carry, whence onkos, a burden, mass, hence a tumor: ONCOGENESIS, ONCOLOGY. 2. Compound root *bhrenk- (see bher-'). [Pok. enek- 316.] nekw-t-. Night. O-grade form *nokv-t-. 1. Germanic *naht- in Old English niht, neaht, night: NIGHT. 2. Latin
858:plak-'. Also plak-. To be flat. Extension of pele-2. 1. Germanic *fléh6 in Old Norse fl6, layer, coating: FLOE. 2. Variant form *pldg- in: a. Germanic *flék- in Old English fléc, flatfish: FLUKE!; b. Germanic *flakaz in Norwegian flak, flat piece, flake, probably akin to the Scandinavian source of Middle English flake, flake: FLAKE}; c. Germanic *flak- in Old Norse flaki, fleki, hurdle: FLAKE?. 3. Extended form *plakd in Germanic *flag6 in Old Norse flaga, layer of stone: FLAG, FLAW}. 4. Possibly suffixed (stative) form *plak-é-, to be calm (as of the flat sea), in Latin placére, to please, be agreeable: PLACEBO, PLACID, PLEA, (PLEAD), PLEASANT, PLEASE; COMPLACENT. 5. Lengthened suffixed form *plak-G- in Latin placdre, to calm (causative of placére): PLACABLE, PLACATE. 6. Nasalized form *pla-n-k- in Latin plancus, flat, flat-footed, whence planca, board: PLANCHET, PLANK, PLANK-SHEER. 7. Variant form *plag- in: a. perhaps Latin plaga, net (? < “something ex- tended”): PLAGIARY; b. Greek plagos, side: PLAGAL, PLAGIO-, PLAYA. 8. Root form *plak- in Greek plax, flat, flat land, surface: PLACENTA, PLACOID. 9. Variant form *pelag- in Greek pelagos, sea: PELAGIC; ARCHIPELAGO. [Pok. 1. pla-k- 831.]
893:culdre, to rake, in Provengal rasclar (> French racler), to rake, scrape: RACLETTE. [Pok. 2. réd- 854.] reg-'. To move in a straight line, with derivatives mean- ing “to direct in a straight line, lead, rule.” I. Basic form *reg-. 1. Suffixed form *reg-to- in Germanic *rehtaz in Old English riht, right, just, correct, straight: RIGHT. 2. Latin regere, to lead straight, guide, rule (past partici- ple réctus, hence adjective réctus, right, straight): REALM, RECTITUDE, RECTO, RECTOR, RECTUM, REGENT, REGIME, REGIMENT, REGION; CORRECT, DIRECT, ERECT, RECTANGLE, RECTIFY, RECTILINEAR, RISORGIMENTO, SURGE. 3. Greek oregein (with prothetic vowel from oldest root form *sreg-), to stretch out, reach out for: ANORECTIC, ANOREXIA. II. Lengthened-grade form *rég-, Indo-European word for a tribal king. 1. Celtic suffixed form *rig-yo- in Germanic *rikja- in: a. Old English rice, realm: BISHOPRIC; b. Old Norse riki (> Norwegian rik), realm: RIKSMAL; c. Old English rice, strong, powerful: RICH. 2. Latin réx, king (royal and priestly title): REAL, REGAL, REGULUS, REIGN, ROYAL; INTERREX, REGICIDE, REGIUS PROFESSOR, VICEREINE, VICEROY. 3. Suffixed form *rég-en- in Sanskrit raja, rdjan-, king, rajah (femi- nine rdjni, queen, rani), and rdjati, he rules: RAJ, RAJAH, (RANI), (RYE2); MAHARAJAH, MAHARANTI. III. Suffixed lengthened-grade form *rég-old in Latin régula, straight piece of wood, rod: RAIL!, REGLET, REGULAR, REGULATE, RULE, IV. O-grade form *rog-. 1. Germanic *rak6 in Old English raca, racu, rake (implement with straight pieces of wood): RAKE!, 2,Germanic *rak- in Middle Dutch rakke, framework: RACK}, 3. Possibly Germanic *rankaz (with nasal infix) in Old English ranc, straight, strong, hence haughty, overbearing: RANK?. 4, Germanic *rak- inaz, ready, straightforward, in Old English gerecenian, to arrange in order, recount (ge-, collective prefix; see kom): RECKON. 5. Suffixed form *rog-d- in Latin rogdare, to ask (< “stretch out the hand”): ROGATION, ROGATORY; ABROGATE, ARROGATE, CORVEE, DEROGATE, INTERRO- GATE, PREROGATIVE, PROROGUE, SUBROGATE, SUPERER- ocaTE. 6. Suffixed form *rog-o- in a possible Latin noun *rogus, “extension, direction,” perhaps in a Latin phrase *é rogd, “from the direction of” (€ < ex, out of; see eghs), contracted into ergd, therefore, in consequence of: ARGAL, ERGO. V. Lengthened o-grade form *rég-. 1. Ger- manic *rdkjan in Old English rec(c)an, to pay attention to, take care (formally influenced by Old English reccan, to extend, stretch out, from Germanic *rakjan): RECK. 2. Germanic *rdékja- in Old English receléas, careless (-léas, lacking; see leu-1):; RECKLESS. [Pok. 1. reg- 854.] reg-2. Moist. 1. Suffixed variant form *rek-no- in Ger- manic *regnaz, rain, in Old English reg(e)n, rén, rain: RAIN; RAINBOW. 2. Possibly Latin rigdre, to wet, water: IRRIGATE. [Pok. 2. reg- 857.] reg-3. To dye. Lengthened-grade form *rég-. 1. Suffixed form *rég-és- in Greek rhégos, blanket, rug: REGOLITH. 2. Sanskrit rdgah, color, red: RAGA. 3. Perhaps Sanskrit raékshd, earlier form of lékshd, red dye: Lac}. [Pok. 1. reg- 854.] regv-es-. Darkness. Oldest root form *areg’-es-. Greek Erebos (with prothetic vowel), Erebus, a place of dark- ness under the earth: EREBUS. [Pok. regt-os- 857.] rei-1, To scratch, tear, cut. I. Extended form ‘reik-. 1. Germanic *rigon- in Italian riga, line (< “something cut out’’): RIGATONI. 2. Suffixed form *rei-md or *reig-sma in Latin rima, crack, cleft, fissure: RIMOSE. 3. Suffixed o-grade form *roik-wo- in Germanic *rai(h)-wa- in Old English raw, réw, a line, row: ROW!. II. Possible extended form *reipp-. Germanic *raipaz, rope, in: a. Old English rap, rope: ROPE; b. compound *stig-raipaz, “‘mount-rope,” in Old English stigrap, stirrup (see steigh-). III. Extended form *reip-. 1. Ger- manic *rifan, in Old Norse rifa, to tear: RIVE. 2. Zero-grade form *rip- in: a. Germanic *77fti- in Danish rift, breach, akin to the Scandinavian source of Middle English rift, rift: R1FT!; b. Germanic *rif- in Old English
1726:LAAGER legh- LABEL leb-! LABELLUM leb-2 LABIAL leb-2 LABILE leb-1 LABIUM leb-2 LABOR leb-1 LABRET leb-2 LABRUM leb-2 Lac! reg-3 LACCOLITH laku- LACERATE |@k- LACHRYMAL dakru- LACINIATE l@k- LACK leg-2 LACROSSE ger-2 LACTATE melg- LACTEAL melg- LACTESCENT melg- LACTO- melg- LADDER Klei- LADE kla-
1750:LIGHTER? legwh- LIGNEOUS  leg-! LIGNI- leg-1 LIGNUM VITAE gWei- LIGULE dngha LIKE! [ik- LIKE? [ik- LIKELY lik- LILAC nei- LIMACINE  lei- LIME = lei- LIMICOLINE lei- LIMN leuk- LIMP kel-1, leb-1 LINDEN _ lento- LINE! lino- LINE? fino- LINEN fino- Linc! del-1 LING? lenk- LINGER del-1 LINGERIE lino- LINGO dnghi LINGUA dnghd LINGUIST dngha LINIMENT lei- LININ lino- LINK! kleng- LINK? Jeuk- LINKS kleng- LINNET fino- _ LINOLEIC ACID [ino- LINSEED lino- LINT Tino-
=== reg- dye
178:The notion of government and sovereignty was well represented. The presence of the old word for tribal king, *reg- (reg-'), only in the extreme east (RAJAH) and the extreme west (Latin réx, Celtic -rix) virtually guarantees its presence in the earliest Indo-European society. (Here is an example of the phenom- enon of marginal or peripheral conservation of a form lost in the central innovating area). Roman tradition well attests the sacral char- acter of kingship among the Indo-Europeans. The functions of king and priest were differ- ent aspects of a single function of sover- eignty. It is this which is symbolized by the divine name *dyeu-poter- (deiw-), the chief of the gods.
892:reg-'
893:culdre, to rake, in Provengal rasclar (> French racler), to rake, scrape: RACLETTE. [Pok. 2. réd- 854.] reg-'. To move in a straight line, with derivatives mean- ing “to direct in a straight line, lead, rule.” I. Basic form *reg-. 1. Suffixed form *reg-to- in Germanic *rehtaz in Old English riht, right, just, correct, straight: RIGHT. 2. Latin regere, to lead straight, guide, rule (past partici- ple réctus, hence adjective réctus, right, straight): REALM, RECTITUDE, RECTO, RECTOR, RECTUM, REGENT, REGIME, REGIMENT, REGION; CORRECT, DIRECT, ERECT, RECTANGLE, RECTIFY, RECTILINEAR, RISORGIMENTO, SURGE. 3. Greek oregein (with prothetic vowel from oldest root form *sreg-), to stretch out, reach out for: ANORECTIC, ANOREXIA. II. Lengthened-grade form *rég-, Indo-European word for a tribal king. 1. Celtic suffixed form *rig-yo- in Germanic *rikja- in: a. Old English rice, realm: BISHOPRIC; b. Old Norse riki (> Norwegian rik), realm: RIKSMAL; c. Old English rice, strong, powerful: RICH. 2. Latin réx, king (royal and priestly title): REAL, REGAL, REGULUS, REIGN, ROYAL; INTERREX, REGICIDE, REGIUS PROFESSOR, VICEREINE, VICEROY. 3. Suffixed form *rég-en- in Sanskrit raja, rdjan-, king, rajah (femi- nine rdjni, queen, rani), and rdjati, he rules: RAJ, RAJAH, (RANI), (RYE2); MAHARAJAH, MAHARANTI. III. Suffixed lengthened-grade form *rég-old in Latin régula, straight piece of wood, rod: RAIL!, REGLET, REGULAR, REGULATE, RULE, IV. O-grade form *rog-. 1. Germanic *rak6 in Old English raca, racu, rake (implement with straight pieces of wood): RAKE!, 2,Germanic *rak- in Middle Dutch rakke, framework: RACK}, 3. Possibly Germanic *rankaz (with nasal infix) in Old English ranc, straight, strong, hence haughty, overbearing: RANK?. 4, Germanic *rak- inaz, ready, straightforward, in Old English gerecenian, to arrange in order, recount (ge-, collective prefix; see kom): RECKON. 5. Suffixed form *rog-d- in Latin rogdare, to ask (< “stretch out the hand”): ROGATION, ROGATORY; ABROGATE, ARROGATE, CORVEE, DEROGATE, INTERRO- GATE, PREROGATIVE, PROROGUE, SUBROGATE, SUPERER- ocaTE. 6. Suffixed form *rog-o- in a possible Latin noun *rogus, “extension, direction,” perhaps in a Latin phrase *é rogd, “from the direction of” (€ < ex, out of; see eghs), contracted into ergd, therefore, in consequence of: ARGAL, ERGO. V. Lengthened o-grade form *rég-. 1. Ger- manic *rdkjan in Old English rec(c)an, to pay attention to, take care (formally influenced by Old English reccan, to extend, stretch out, from Germanic *rakjan): RECK. 2. Germanic *rdékja- in Old English receléas, careless (-léas, lacking; see leu-1):; RECKLESS. [Pok. 1. reg- 854.] reg-2. Moist. 1. Suffixed variant form *rek-no- in Ger- manic *regnaz, rain, in Old English reg(e)n, rén, rain: RAIN; RAINBOW. 2. Possibly Latin rigdre, to wet, water: IRRIGATE. [Pok. 2. reg- 857.] reg-3. To dye. Lengthened-grade form *rég-. 1. Suffixed form *rég-és- in Greek rhégos, blanket, rug: REGOLITH. 2. Sanskrit rdgah, color, red: RAGA. 3. Perhaps Sanskrit raékshd, earlier form of lékshd, red dye: Lac}. [Pok. 1. reg- 854.] regv-es-. Darkness. Oldest root form *areg’-es-. Greek Erebos (with prothetic vowel), Erebus, a place of dark- ness under the earth: EREBUS. [Pok. regt-os- 857.] rei-1, To scratch, tear, cut. I. Extended form ‘reik-. 1. Germanic *rigon- in Italian riga, line (< “something cut out’’): RIGATONI. 2. Suffixed form *rei-md or *reig-sma in Latin rima, crack, cleft, fissure: RIMOSE. 3. Suffixed o-grade form *roik-wo- in Germanic *rai(h)-wa- in Old English raw, réw, a line, row: ROW!. II. Possible extended form *reipp-. Germanic *raipaz, rope, in: a. Old English rap, rope: ROPE; b. compound *stig-raipaz, “‘mount-rope,” in Old English stigrap, stirrup (see steigh-). III. Extended form *reip-. 1. Ger- manic *rifan, in Old Norse rifa, to tear: RIVE. 2. Zero-grade form *rip- in: a. Germanic *77fti- in Danish rift, breach, akin to the Scandinavian source of Middle English rift, rift: R1FT!; b. Germanic *rif- in Old English
```


## [2026-09-14T01:19:40.742Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} END{print \"SYN leaves:\",NR}' SYN.txt; for L in 1075 357; do echo \"==== LEAF $L (printed ~$((L-24)))\"; awk -v L=$L 'BEGIN{RS=\"\\f\"} NR==L {print substr($0,1,1200)}' SYN.txt; done",
 "description": "Print Buck leaves for p.1051 and p.333"
}
```


### [2026-09-14T01:19:41.792Z] TOOL RESULT

```
SYN leaves: 1545
==== LEAF 1075 (printed ~1051)
(obs.), Corn. gurth-uher, etym. dub. Pokorny Z. celt. Ph. 15.377 (vs. Pedersen 1.75, etc.).
Br. abardaez, etym.? Henry 2. Er- nault, Dict. étym. 193.
5. Goth. andanahti, lit. ‘the period extending toward the night’ (and, anda- ‘on, to’ and nahis ‘night’). Feist 47.
ON kveld (Dan. kveld poet. and arch.), Sw. kvdll, NIcel. kvéld, OE cwield in cwield-tip (cwild-, cwyld-) ‘evening-time’, cwield-seten ‘evening sitting, first part of night’, OHG quilti-werc ‘evening work’, prob. identical with OE cwield ‘destruction, death’ : OE cwelan ‘die’, cwellan ‘kill’, OHG quelan ‘suffer tor- ment’, Lith. galas ‘end’, etc. Walde-P. 1.690. Falk-Torp 604. Hellquist 538.
ON aptann (distinguished from kveld as longer, lasting from mid-afternoon on, cf. einn aptann at kveldi; NIcel. aftan, poet.), Dan. aften, Sw. afton; with differ- ent formation and grade of root syllable OE @fen, ME even, Du. avond, OHG abant, etc. (OE @fning ‘approach of eve- ning’ > ME, NE evening), prob. fr. the root in Goth. ifluma ‘following, later’, afar ‘after’, Skt. apara- ‘Jater, western’, Grk. éri ‘to, on’, ové ‘late’, etc. Walde- P. 1.123. Falk-Torp 15.
==== LEAF 357 (printed ~333)
trudan now mostly ‘fee-
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
SELECTED INDO-EUROPEAN SYNONYMS
ble’ or ‘pregnant’), all derivs. of Chs] trudt, SCr., Pol. trud ‘toil, exertion’, ete, (see under Dan. treat, above, 4). :
SC. wmoran, fr. umoriti ‘tire, kil? = ChSl. wmortti ‘kill’ (4.76). 2.80.
Boh. unaveny fr. unaviti ‘tire, fatigue’ epd. of naviti id., fr. nati ‘waste aay, languish’ : ChSI. -nytz ‘be sluggish’, Lith. novytt ‘torment, oppress’, apparently from the same root as Lett. nave ‘death’, ete. (4.75). Walde-P. 2.316. Miklosich 218.
Boh. mdly, also ‘faint’ : Pol. madly ‘faint, weak’, ChSl. miidlt ‘slow’, Pol, mudzié ‘delay, pass the time’, ChS, muditi ‘loiter’, etc., outside connections? Briickner 347 f.
Pol. zmeczony, fr. zmeczyé ‘exhaust, fatigue’, cpd. of meczyé ‘torture, harass’ : Pol. meka, ChSl. maka, etc. ‘torture’, ChSl. mektikt ‘soft’, Lith. minkyti ‘knead’, Grk. nacow ‘press, knead’, OF mengan ‘mix’, etc. Walde-P. 2.268. Berneker 2.48. Briickner 328.
Russ. ustavsi7, perf. act. pple. of ustavat’ ‘get tired’: Boh. ustati ‘get tired, cease’, Pol. ustaé
```


## [2026-09-14T01:19:54.149Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} {n++; if ($0 ~ /INDEX|Index of/) print \"leaf\",n, substr($0,1,120)}' SYN.txt | head -10",
 "description": "Find Buck index start"
}
```


### [2026-09-14T01:19:55.237Z] TOOL RESULT

```
leaf 30  Lidén, Arm. Stud. E. Lidén, Armenische Studien. Lidén, Stud. E. Lidén, Studien zur altindischen und vergleichenden
```


## [2026-09-14T01:19:59.319Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} {n++; if (n>=1100 && n<=1500 && $0 ~ /rhegos|ρῆγος|ρεγος|pnyos|pfyos/) print \"leaf\",n}' SYN.txt | head; echo \"--- look for sanskrit index\"; awk 'BEGIN{RS=\"\\f\"} {n++; if (n>=1060 && n<=1120) print n\": \"substr($0,1,90)}' SYN.txt | head -60",
 "description": "Look at Buck end matter"
}
```


### [2026-09-14T01:20:00.586Z] TOOL RESULT

```
--- look for sanskrit index
1060: cpd. of dé ‘from, down’ and sinere ‘let, permit’, earlier ‘place, put’. Ernou
1061: at rpéropat Hesych., Foie ‘shrink, sink’, etc. Walde-P. 2.387 {. Falk-Torp 645 f.
ME 
1062: low). Falk-Torp 289.
OE gearo, ME yare (NE yare now obs. or dial.), OHG garo, MHG gare, NH
1063: ; NG pop. wévra; Fr. toujours, fr. OF r. toz jorz, also tozdis, lit. ‘all days’; Rum.
1064:  punar, asakrt Rom, agen”) OHG  ofto Av.  ..- “ in a MHG oft(e) 1 aad NHG oft, haufig 
1065: ��in heaps, crowds’ (fr. haufe ‘heap’), hence ‘abundant(ly)’, and later ‘f
1066: iktin 1067, 1682); Ir. iar n-tairib, i n-aairib (Thes. 2.332.21, 23; war ‘hour, time’,
1067: th. ni hwanhun, neg. with deriv. of hwan ‘when’ and ‘at any time’, like ni hwashun
1068: dwar
i * »
Soh
Digitized by Arya Samaj Foundation Chennai and eGangotri
990 SELECTED INDO
1069:  for ‘day’, | Gall. lat. (Calendar of Coligny) : ChSI.
tainly those of the large inher
1070: ng general Slavic; Ved. nakt- (nom. Sg. nak, to an inherited group, pointing clearly | acc
1071: ora, Fr. aurore, Rum. aurora); Ir, faar (‘sunrise’), W. gwawr (Br. gwere-laouen ‘mor
1072: braz- ‘shine, beam’, Goth. bairhts, etc. ‘bright’. Walde-P. 2.170. Berneker 85.
Le
1073: hSl. mraki ‘latkness’, beside Lith. mirgéti ‘glim- mer, twinkle’, fr. a guttural 
1074: ��), Sp. mediodia, Rum. amiazi, amiadi (Lat. ad mediam diem), miezul zilet; Ir. medon 
1075: (obs.), Corn. gurth-uher, etym. dub. Pokorny Z. celt. Ph. 15.377 (vs. Pedersen 1.75, etc.)
1076: k., | and Du. vandaag with van ‘from, of”. Balto-Slavic, and a part of the Gmc. Du. he
1077:  beside adv. dat. in OHG mor- gane, MHG morgen(e), NHG, Du. mor- gen. Weigand-H. 2.219. Fr
1078: smer, IF 42.179 ff. Miihl.-Endz. 4.446.
14.51 HOUR Grk apa Goth. hweila Lith. valanda (ady
1079:  Kurschat, etc.), fr. MLG stunde ‘hour’. Mihl.-Endz. 3.1106 f.
5. ChSl. godina (reg. r
1080: ion of time, see under ‘hour’ (14.51).
14.53 CLOCK, WATCH
Grk. — cpods-ytov Goth. Li
1081: r. Lat. horologium, Loth, RC 32.305.
NIt. clog, fr. Ir. cloc(c) ‘bell’ = W. cloch ‘b
1082: woche
Br. sizun
On the much-discussed origin of the week and the names of the week days, e
1083: cl. a ee in the Peregrinatio about EW on ae the Romance words Berecond ere (but influenced
1084: a feria lunedi lundt lunes lunt segunda feira luan luan dydd llun dilun manudagr mdnudagur
1085: f these old, the others special Irish terms. Cf. the references in 14.51.
1. Ecclesiastica
1086: yds caBBarwy (Mk. 16.2), Srumin sabbatd = xpirn caBBarov (Mi. 16.9), fruma sabbatd = rpoc&
1087: . For Saturday the Lat. Saturnus was retained, at least in Anglo- Frisian and Low German (
1088: oh. and Pol., and a few others of common words applied to different months (e.g. listopad,
1089:  to reflect a distinctive IE Widespread far. The second is more Various us oe formal group
1090:  ‘period of time’ (14.11), as elsewhere in Slavic with various special applications, b
1091: donell- Keith 1.110 f.
14.74. ‘Winter’.
1. IE *gheim-, *§hyem-, etc., prob. with m-su
1092: r. proljeée, also Boh. podlett ‘early summer, spring’, lit. ‘pre-summer’ (SCr. Lj
1093: ly not clear (the suggested analogy of Lat. autwmnus is based on its false etym.). Henry 1
1094: r. the root seen in Grk. dpapickw ‘fit’, etc. Walde-P. 1.70.
11 PeRcEIVE BY THE SENSES
1095: g and sight the parallel re- lations between the subj. and obj. aspects are less obvious a
1096: nse of touch, and, in general, the vbs. for ‘touch’ are the most important in this gro
1097: . Grimm, Die fiinf Sinne (1848 = KI. Schriften 7.193 ff.), and, for IE, F. Bechtel, Ueber 
1098: ub. (Walde-P. 2.29).
Ir. mothaigim, vbl. n. mothugud (see RIA Contrib. s.vv.), NIy. mothui
1099: ntvinden, em- phinden, NHG empfinden : OE onfindan ‘nd out, discover, experience, be awa
```


## [2026-09-14T01:20:06.854Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} {n++; if (n>=1125 && n<=1135) {print \"==LEAF\",n; print substr($0,1,400)}}' SYN.txt",
 "description": "Print Buck leaves ~1129"
}
```


### [2026-09-14T01:20:07.887Z] TOOL RESULT

```
==LEAF 1125
less probably with retention of an early relation to the notion ‘shine’, as assumed by Berneker 203 and Walde-P. 1.774.
Boh. patfiti, Pol. patrzeé ‘look’, also ‘belong to’ as SCr. patriti, etym.? Briickner 399. .
ChSI. stimotriti, Russ. smotret’ : Lith. matyti ‘see’ (above, 10).
12. Skt. dre-, ete., above, 2.
Skt. pac-, above, 3.
Ay. vaen-, OPers. vain- ‘see’ (most widesprea
==LEAF 1126
ian ‘show the way, guide, direct,’
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
1046 SELECTED INDO-EUROPEAN SYNONYMS
OHG wisan, MHG wisen, NHG weisen, Du. wijzen ‘show the way, direct, point’, etc.), fr. adj. ON vtss, OE, OHG wis ‘wise’ (17.21), hence orig. ‘make one wise, knowing’ (put one wise in US. slang). 
==LEAF 1127
e’, but esp. ‘bring to light, show’, mid. ‘appear’),
with sb. ¢dos ‘light’, whence Hom. dacivw ‘shine’, daewéss ‘bright’, Att. pas (gen. gwrés) ‘light? whence ¢uwreivds ‘bright? (¢writw mostly trans. ‘light up’); Skt. bha-, bhas-, Av. ba-.
2. IE *leuk-, as in sbs. for ‘light’ (1.61). Walde-P. 2.408 ff. Brnout-M. 570 ff. Walde-H. 1.823f. REW 5136. Falk-Torp 67
==LEAF 1128
t, white’ (15.64), Skt. hari- ‘tawny, yel- low’, OE geolo, OHG gelo ‘yellow’, etc. (15.69). Walde-P. 1.624 ff. Falk-Torp 328 f.
7. Lith. Sviesti, ChSl. svétiti, general Slavic (in part refl.) : ChSl. svété ‘light’, Skt. cveta-, Av. spaéta-, Goth. hweits ‘white’, etc. (15.64). Walde-P. 1.470.
Lith. Zibéti (Lett. zibét ‘lighten, glim- mer’) : Lith. Ziebti ‘light a fire�
==LEAF 1129
ar
——$——$— eee
Skt. guci-, ¢ukra-, dyu- mant-, ete.
raoxsna-, xSaéla-, banvant-, etc.
‘shine’ (15.56). Some are simply pples. of the latter, and many other such words for ‘shining’ might have been included as virtually equivalent to ‘bright’.
1. Grk. Xapympés (NG pop. only in fig. sense ‘splendid’; in lit. sense Napmepés) : Aayrw ‘shine’ (15.56).
Grk., Ion. daevds
==LEAF 1130
��shine’, etc. Walde-P. 2.536. Falk-Torp 1008 f.
ON Jjéss, Dan. lys, Sw. jus, OF léoht (use of NE light for ‘bright’ now obs.; cf. NED), OHG lioht, etc., adjs. to sbs. for ‘ight’ (1.61).
ON hetdr, OE hddor, OHG heitar ‘clear, bright’ (esp. of the sky) : Skt. citra- ‘conspicuous, clear, bright’, Lith. skaidrus ‘clear, bright’, ete. Walde-P. 2.537. Falk-Torp 446.
Dan., Sw
==LEAF 1131
less other objects of sight are distributed else- where, e.g. ‘form, shape’ under spatial relations.
Most of the words for ‘color’ reflect such notions as ‘covering’, ‘surface, skin’, ‘countenance, look’, or the ‘hair’ of animals, indicating that they were used primarily with reference to the color, the complexion of human beings, or the color of animals, which is that of t
==LEAF 1132
. Miihl.-Endz. 2.267. Berneker 607 f.
6. SCr. boja (also ‘paint, dye’), fr. Turk. boya ‘paint, dye’. Berneker 68.
Boh. barva, Pol. (old) barwa, now farba, fr. MHG varwe, NHG farbe (above, 4). Berneker 44.
Pol. kolor, fr. Lat. color (above, 2). Briickner 246.
Russ. cvet (pl. cveta) = cvet (pl. cvety) ‘flower, bloom, blossom’, ChSI. cuétii ‘flower’, general Slavic. Berneker 656.
7. 
==LEAF 1133
ers are of various sources.
1. TE *tem-, etc., as in sbs. for ‘dark- ness’ (1.62). Walde-P. 1.720f,
Ir. temen, temnide (here also W. tywyll? cf. ref. in 1.62); Lith. tamsus, Lett. tumss; ChSl. timtni, SCr. taman, etc., general Slavic; Skt. tamasa- (AV 11.9.22).
2. Grk. uédas, xedauvds ‘black’ (15.65), also ‘dark’ in color,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
NG
==LEAF 1134
 still much fluctuation and over- lapping in the application of color words. There is only one group of cognates that is so widespread and consistent in mean- ing as to point clearly to an IE color name with definite application, namely the group for ‘red’. There are some cases of agreement between two branches in words applied to the same color, and there are some extensive groups from a comm
==LEAF 1135
d-, etc.). Walde-P. 1.237, Pedersen 1.41. Stokes 265.
Ir. gel, NIr. geal : OE geolo, ete. ‘yel- low’ (15.69).
Ir. ban : Skt. bha-, Av. ba- ‘shine’, etc, (15.56).
W. can, Br. kann (‘brilliant white’) : (or loanword fr.) Lat. candidus ‘bright’ (15.57). Walde-P. 1.352. Pedersen 1.199. i
4. Goth. hweits, OE hwit, etc., general Gme. : Skt. cveta-, Av. spaéta- ‘white’, ChSl. své& s
```


## [2026-09-14T01:20:14.174Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==1131 || NR==1132' SYN.txt | head -70",
 "description": "Print Buck 15.61 COLOR"
}
```


### [2026-09-14T01:20:15.219Z] TOOL RESULT

```
less other objects of sight are distributed else- where, e.g. ‘form, shape’ under spatial relations.
Most of the words for ‘color’ reflect such notions as ‘covering’, ‘surface, skin’, ‘countenance, look’, or the ‘hair’ of animals, indicating that they were used primarily with reference to the color, the complexion of human beings, or the color of animals, which is that of their hair, But there is also a use of ‘ower’ for
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
—SSSS3600SS OOS ee
‘color’, and some are connected with words used elsewhere of some special color.
1. Grk. xpdya (also xpéa, xpord) : xews ‘skin, surface’, rarely also ‘complex- ion, color’, xpatw ‘touch the surface’, whence ‘tinge, stain’, xpatw ‘scrape, graze, wound slightly’, Lith. grusti ‘bruise, crush’, etc. Walde-P. 1.648 ff. Boisacq 1071.
2. Lat. color (> Romance words), as orig. ‘covering’ : occulere, célare ‘hide’ (cf. Skt. varna-, below, 7). Walde-P. 1.432, Ernout-M. 206. Walde-H. 1.247.
Rum. faté ‘face, surface’, also ‘color’, fr. VLat. facia=faciés ‘face’. REW 3130.
3. Ir. dath, perh. : Ir. date ‘agreeable (cf. NIr. dathamhail ‘pleasant, comely, graceful’). Pedersen 1.418. .
Ir. li, lig (also ‘splendor’), W. liv, Br. liv or liou, OCorn. liu (cf. also OBr.
yum, da-liu gl. fascus), prob. : ‘be bluish-black, livid’, livor
tow gl. Bie Iat. a color’, etc. Walde-P. 2.715.
iplue-blac
Ide-H. Pedersen 1,51. Wald
Stokes 251.
ae N litr (NIcel. litur reg. word for ae Dan. Id mostly replaced by c }
Jso ‘countenance, complexion’ : ee wiitan ‘look’ (15.52). Walde-P. 1.293. Falk-Torp 679.
“OE bleo and bleoh (after feoh, etc.), ME ble, OS bi, OFris. bli(e)n, perh. : Goth. bleips ‘merciful, gentle’, OF blios talad’, ete, Lith. blyvas ‘violet-colored’, and also OHG blio, etc. ‘lead’ (‘blue’ metal), all fr. a root *bhlet- ‘shine(?)’. -Walde-P. 2.210. Feist 99.
OE hiew, ME hew, NE hue, orig. form, appearance’, as Goth. hiwi, etc. (12.51). NED s.v. hue, sb.?.
OHG farawa, MHG varwe, NHG farbe, Du. verf (MLG varwe > Dan. farve, Sw. farg), beside adj. OHG faro ‘colored’, ete, this prob. (*pork-wo-) : Skt. preni- ‘speckled, dappled’, Grk. mepxvés ‘dark- colored, livid’, Ir. ere ‘gay-colored, red’, ete. Walde-P. 2.45. Falk-Torp 206. Franck-v. W. 731.
ME colur, colo(u)r, NE color (colour), Du. kleur (older coloor, caloor), fr. OF. color, col(o)ur, coulour, etc., Fr. couleur Ds, 2). NED s.v. Franck-v. W.
5. Lith. spalva = Lett. spalva ‘feath-
SENSE PERCEPTION
Digitized by Arya Samaj Foundation Chennai and eGangotri
1051
ers, hair on quadrupeds, color of the hair of animals’, etym. dub., prob. : Lat. spolium ‘skin of an animal stripped off, spoils of war’, Grk. oodds ‘skin gar- ment’, etc., fr. the root of OHG spallan, etc. ‘split’. Walde-P. 2.679. Miuhl.- Endz. 3.983.
Lett. krasa, esp. ‘beautiful complex- ion, beauty’, as ‘color’ also krass (Lith. krosa ‘color’, in Kurschat krosas, is no longer used, neither form in Lalis or NSB), fr. the Slavic, ChSl., Russ. krasa ‘beauty’, cf. Russ, kraska ‘paint’ (9.88), krasnyj ‘red’ (15.66)
. Miihl.-Endz. 2.267. Berneker 607 f.
6. SCr. boja (also ‘paint, dye’), fr. Turk. boya ‘paint, dye’. Berneker 68.
Boh. barva, Pol. (old) barwa, now farba, fr. MHG varwe, NHG farbe (above, 4). Berneker 44.
Pol. kolor, fr. Lat. color (above, 2). Briickner 246.
Russ. cvet (pl. cveta) = cvet (pl. cvety) ‘flower, bloom, blossom’, ChSI. cuétii ‘flower’, general Slavic. Berneker 656.
7. Skt. varna-, also and orig. ‘cover- ing’, fr. vr- ‘cover’.
Skt. rafiga-, raga- : raj- ‘be colored, grow red’, Grk. pétw ‘dye’, peyebs ‘dyer’, etc. Walde-P. 2.366.
Av. gaona- ‘hair’, also ‘color’ (Yt. 8.58; cf. Afgh. yuna ‘hair, color’, NPers. gin ‘color’) : Lith. gaurai ‘hair’, etc. (4.14). Walde-P. 1.557. Barth. 482.
15.62 LIGHT (in Color)
Ne aint Dan. ys Lith.  Sviesus It, voixrés Sw. us Lett. gaiss h, chiaro ME (pale) SCr. _ svijetao 8p. ug NE light Boh. svitly, jasny Rum. dens Du. _ helder, licht Pol.  jasny
Mr 5 aes MHG lieht Russ. _ svetlyj
ieee rom NHG hell (lich) Br golen
a7 sklaer
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
1052
Most of the words for ‘light’ in color are the same as those for the broader ‘light’ = ‘bright’ (15.57), and this spe- cial use is mostly modern. So NE light in this sense from 15th cent., MHG lieht rarely in cpds. as liehibla ‘light blue’, NHG licht usual in Austria vs. hell with reference to color (Kretschmer, Wort- geogr. 234).
Other terms are:
1. Grk. Aevxés, orig. ‘bright’, but mostly ‘light in color’, esp. ‘white’ : Lat. liz, OF leoht ‘light’, etc. (1.61).
2. NG dvowxrés, lit. ‘open’, fr. dvoiyw ‘open’. Similarly, and prob. by seman- tic borrowing, Rum. deschis, fr. deschide ‘open’ (12.24).
Digitized by Arya Samaj Foundation Chennai and eGangotri
SELECTED INDO-EUROPEAN SYNONYMS
3. NIr. éadtrom, ‘light’ in weight (15.82), also ‘light’ in color (Dinneen McKenna), doubtless after the double use of NE light in which two different words are merged.
ME pale (NE also Sometimes in this sense, as pale blue, etc., cf. NED S.V, fr. OF r. pale, Lat. pallidus ‘pallid,.pale’ ‘ Grk. zedtés ‘livid’, odds ‘gray’, Skt, palita- ‘gray, hoary’, pandu- ‘whitish yellow, white’, OE fealo, OHG falo, Lith. palvas ‘fallow’ (‘light brownish or red- dish yellow’), ChSI. plavii (renders Aeukds Jn. 4.35, but with reference to fields of grain, hence here also ‘yellowish’), Walde-P. 2.53 f. Ernout-M..725.
15.63 DARK (in Color) Grk. —_péAas, xedarvds Goth.~ i... Lith. tamsus NG Babbs, oxodpos ON dékkr Lett. tums Lat. fuscus, pullus Dan. mérk, dunkel ChSl.  timinit It. scuro, cupo Sw. mork, dunkel SCr.  taman Fr. foncé, sombre OE wann. (deorc) Boh. temny Sp. obscuro ME dark, wan, dosc Pol. ciemny Rum. inchis NE dark Russ. temnyj Tr. dorche, temen Du. donker Skt. krsna-, ¢yama-, Nir. dorcha OHG  tunchal tamasa- W. tywyll MHG _ tunkel Av. axSaéna- Br. du NHG dunkel
Many of the words for ‘dark’ in color are the same as those for ‘dark’ = ‘lack- ing light’, these again mostly connected with the sbs. for ‘darkness’ already dis- cussed in 1.62. Some are the same as, or derived from, those for ‘black’; some rest on the notion of ‘deep’; oth
```


## [2026-09-14T01:20:26.372Z] TOOL CALL #72: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B1%D8%AC%DB%8C%D8%AF%D9%86/",
 "prompt": "Is there a Persian entry رجیدن? Quote the Dehkhoda and Mo'in (فرهنگ معین) definitions if present, and say whether the word means 'to dye/colour'. Also report whether the page redirects to رزیدن."
}
```


## [2026-09-14T01:20:27.620Z] TOOL CALL #73: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B1%D8%B2%DB%8C%D8%AF%D9%86/",
 "prompt": "Quote the Dehkhoda and Mo'in entries for رزیدن: meaning and any etymology note (Pahlavi form)."
}
```


### [2026-09-14T01:20:30.445Z] TOOL RESULT

```
# Persian Entry رجیدن

Yes, there is a Persian entry for رجیدن on this Abadis dictionary page.

**Dehkhoda Definition:**
"رنگ کردن" (to dye/colour) and "لکه کردن" (to stain/spot)

**Mo'in (فرهنگ معین) Definition:**
The page attributes both definitions to Farhang-e Farsi-ye Mo'in: "رنگ کردن" and "لکه کردن"

**Does it mean 'to dye/colour'?**
Yes, the word does mean to dye or colour, as confirmed by both lexicographic sources cited.

**Redirect to رزیدن?**
The page notes "رجوع به رزیدن" (see also رزیدن), indicating a cross-reference rather than a full redirect.
```


### [2026-09-14T01:20:32.265Z] TOOL RESULT

```
# Dehkhoda and Mo'in Entries for رزیدن

**Dehkhoda's entry:**
"رنگ کردن" (coloring/dyeing) is the primary meaning, with additional senses including "رنگرزی کردن" (the work of a dyer) and "لکه کردن" (staining).

**Mo'in's entry:**
This lexicon defines the term simply as "رنگ کردن" (to color or dye).

**Etymology note:**
The Dehkhoda dictionary indicates the term derives from classical Persian sources including "برهان" (Burhan) and "فرهنگ خطی" (manuscript dictionaries), though no explicit Pahlavi form is cited in the provided content. The word relates to the occupational term "رنگرز" (dyer), suggesting roots in textile-dyeing practices in Persian language history.
```


## [2026-09-14T01:20:38.715Z] TOOL CALL #74: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%84%D8%AC%D9%87/",
 "prompt": "Quote the فرهنگ معین (Mo'in) and Dehkhoda entries for لجه / لجّه: meaning and the origin tag (e.g. [ع.] for Arabic). Does Mo'in mark it as Arabic?"
}
```


## [2026-09-14T01:20:40.950Z] TOOL CALL #75: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%84%D8%AC%D8%AC",
 "prompt": "Arabic root ل ج ج: give the verb لَجَّ (lajja) meaning and the nouns لُجَّة (lujja) 'deep water, main sea' and لَجَّة (lajja) 'clamour, noise of a crowd'. Is it treated as a native Arabic/Semitic root?"
}
```


### [2026-09-14T01:20:42.379Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-14T01:20:42.516Z] TOOL RESULT

```
# فرهنگ معین and Dehkhoda Entries for لجه

**Dehkhoda Entry:**
The word is marked as Arabic origin "[ع اِ]" and defined as: "میانه آب دریا" (middle of the sea water).

**Mo'in Entry:**
Marked as Arabic origin "[ع . ]" with the definition: "(لُ جَّ ) میانة دریا" (middle of the sea).

**Answer:** Yes, Mo'in marks لجه as Arabic, using the notation "[ع . ]" (where ع = Arabic/عربی).
```


## [2026-09-14T01:20:54.361Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FVQ lujja\"; grep -n -i \"lujja\\|lujjah\\|Lujj\" FVQ.txt FVQ_pages.txt | head; echo \"=== AFA\"; grep -n \"لجة\\|لجّة\" AFA.txt | head; echo \"=== PLA asbaghi lak\"; grep -n -i \"lakk\\|lak \" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -20",
 "description": "Check Jeffery/Fraenkel/Asbaghi"
}
```


### [2026-09-14T01:20:54.447Z] TOOL RESULT

```
=== FVQ lujja
=== AFA
=== PLA asbaghi lak
1378:Sr - > ablag: "schwarz-weiß" pers. 6 aus dem pers. euı ablak "schwarz- 
3181:zuel - ”’ahlilaf = halilak s. nalllaß. 
17135:lyJ) - kahäk = kalak a. v. » 
17472:e- lagf: "ungeheure Menge" pers. _D lak "tausend" 
17529:GW) - laglag: "Storch" — pers. Zu» Lak-lak CT mp. „)) laklak 11, 
17602:&=- lilaß = nilag a. v. < pers. Sus 1ilak "Flieder" — engl. lilac,
```


## [2026-09-14T01:21:00.198Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '17465,17485p' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt; echo \"=== page tags\"; grep -n \"lagf\\|lağğ\\|ungeheure Menge\" incoming/PLA/PLA_pages.txt | head",
 "description": "Print Asbaghi lajj entry"
}
```


### [2026-09-14T01:21:00.270Z] TOOL RESULT

```
w 


&- latt: "langhalsiges Trinkglas" pers, 7 ?. 
ZJ - latüt: Pl. v.Zulatt ga. v. 


e- lagf: "ungeheure Menge" pers. _D lak "tausend" 


1. Fremdwörterbuch s. v. 

2. Chista Bd. 10 s. v. 

3. BQ. s. v., Addai Scher s. v. 

4. Wahrig s. v. 

5. Fremdwörterbuch s. v. 

6, Schregle s. v., Fremdwörterbuch s, v. 
=== page tags
13412:anlJ)-           kailagfa:            "Kornmaß"              pers.              3,
13495:e-        lagf:          "ungeheure                 Menge"                  pers.        _D lak "tausend"
```


## [2026-09-14T01:21:03.588Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} {n++; if ($0 ~ /lagf: +\"ungeheure/) print \"leaf\",n}' incoming/PLA/PLA_pages.txt; sed -n '13480,13510p' incoming/PLA/PLA_pages.txt",
 "description": "Locate Asbaghi lajj page"
}
```


### [2026-09-14T01:21:04.557Z] TOOL RESULT

```
leaf 255
      Br
     -.
aIy-               lakiyya:             "Lack,         Flüssigkeit,                  die       an   der    Luft      bei       dünnem       Auftragen
          zu       einem       festhaltenden                     Schutzfilm               wird"            hindustan            >> pers,          B>   ar.   6,


ob) -          libäs:          "Bekleidung"                  =    al-basa            q.    v.
          albasa:             Pl.       v.«wls       libäs        _.

 w
&-        latt:          "langhalsiges                    Trinkglas"                pers,       7 ?.


ZJ - latüt:                    Pl.       v.Zulatt                ga. v.

e-        lagf:          "ungeheure                 Menge"                  pers.        _D lak "tausend"




1.    Fremdwörterbuch                          s.    v.
2.    Chista             Bd.       10     s.    v.
3.    BQ.          s.    v.,       Addai        Scher        s.        v.
4.    Wahrig             s.    v.
5.    Fremdwörterbuch                          s.    v.
6,    Schregle                s.    v.,        Fremdwörterbuch                      s,    v.
7. Muhit s. v., Addai                                Scher        s. v.
8.    Addai             Scher       s.     v.
118m                                                                              2eal                                                      lukäna
```


## [2026-09-14T01:21:13.312Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LKT lack/lac\"; grep -n -i \"lakscha\\|lākṣā\\|Lack\\b\\|laca\\|lacre\" LKT.txt | head -15; echo \"=== FSD regolith\"; grep -n -i \"regolith\" FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt WEB_vol1.txt | head; echo \"=== FSD shellac\"; grep -n -i \"shellac\\|shell-lac\" FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt WEB_vol1.txt | head -5",
 "description": "Grep Lokotsch and Funk&Wagnalls"
}
```


### [2026-09-14T01:21:13.446Z] TOOL RESULT

```
=== LKT lack/lac
651:dem  Pers.,  etwa  pük  Horn  NpEt  S.  75, Nr.  339  '^Brennholz'],  ebenso  tk.  bakam; hieraus  rum.  bäcan  'Blauholz',  russ. bakan  Tlorentinerlack'.  Bakkam  ist dasselbe  wie  Fernambuk-  oder  Brasil- holz, Caesalpinia  echinata  Lam.,  seit  der Entdeckung  Amerikas  unser  gebräuch- lichstes Rotholz,  das  die  Portugiesen 1.540  in  den  südamerikanischen  Wäldern in  großen  Mengen  fanden  [wie  Haema- toxylon  campechianum  L.  oder  Cam- pecheholz unser  gebräuchlichstes  Blau- liolz  ist].  Im  angloind.  sappanwood  ist wahrscheinlich  tamul.  shappu  oder  ma- layäl.  shappannani  "rot'  als  Grundwort anzusetzen.  Der  dritte  bereits  genannte Name  Brasil  oder  Brazil,  schon  im Mittelalter  gebraucht,  ist  noch  nicht  er- klärt.   [Hobson-Jobson  794.
680:'2U3.  Ar.  Balkis: X.  pr.,  Name  der  sagenhaften  Königin von  Saba,  die  zur  Zeit  Salomos  lierrschte, vgl.  Koran  Sure  27,  wo  der  Name  aller- dings nicht  genannt  wird.  Nach  A.  Rösch, Die  Königin  von  Saba  als  Königin  Bil- qls.  Eine  Studie.  Leipzig  1890  ist  das ar.  Wort  vom  gr.  uaWaKiq  'Kebsweib' abzuleiten  [das  gr.  Wort  mufs  selbst  wie lat.  pallaca  vom  hebr.  oder  phöniz.  pi- leges  'Kebsweib,  Buhle'  kommen;  die Benennungen  unsittlicher  Personen  und Verhcältnisse  pflegen  von  dem  niedriger stehenden  Volk  aus  dem  Sprachschatz des  höher  gebildeten  übernommen  zu werden].  Nach  Löbel  EITAP  11  soll mit  Berufung  auf  Laurian  §i  Maxim, Glosariu  de  vorbe  sträine  In  limba  ro- mänä.  Bucure§ti  1876,  p.  50  das  Wort im  Türkischen  die  Bedeutung  'dick  und groß'  haben  [fehlt  aber  bei  Kelekian Kämüs].  Hieraus  rum.  balciz,  halcäz 'garstig,  plump,  stämmig'.  —  Die  von Löbel  a.  a.  0.  gegebene  Ableitung  vom gr.  TTaXaid  KüZiKoq  'Ruinen  von  Kyzikos am  Marmarameere'  ist,  weil  semantisch unzulässig,  abzulehnen.
1459:'Keil;  Klotz  oder  Stock  als  Marter- instrument zur  Bastonnade'  [Beschrei- bung von  CHERBONNEAU  in  JAs  1849, I,  546] ;  hieraus  kat.  span.  falca  'Keil', pg.  fälaca  'Bank  zur  Bastonnade',  rum. /'a/aH^'a 'Stockschläge  auf  die  Fußsohlen'; poln.  falagi  plrl.  in  der  Redensart  zadac komu  t^gie  falagi  'jmd.  verprügeln'. [DE  262.  Devic  DEt  114.  ML  3164  u. 315L    Karlowicz  420/421.
2230:'Kragen'  [Stamm  jak,  jan  'Seite,  Ufer, Rand'  Vämbei-y  TktEt  Wb  S.  1 12,  Nr.  123] ; hieraus  rum.  laca  'Halskragen'.
3019:'Marke,  Fleck;  hunderttausend',  [und nach  den  100000,  d.h.  unzähligen  In- sekten Cocca  ilicis,  welche  durch  ihren Stich  auf  quercus  coccifera  die  harzige Absonderung  bewirken]  'Lack';  hieraus in  der  urspiünglichen  Bedeutung  bind. läkh  '100000',  engl,  lack  'dass.,  bes. 100000  Rupien'  und  ferner:  sp.  pg.  laca 'Lack',  ZßCT-e 'Siegellack',  frz  Jag?«e 'Lack', it.  lacca  'Lack,  Siegellack',  rum.  lac; engl,  lac,  ndl.  lak,  dtsch.  Lack  und  engl. shellac  [eigentlich  'Schalenlack',  da  er zu  kleinen,  dünnen  Täfelchen  geformt wird],  ndl.  schellak,  dtsch.  Schellack; russ.  lak,  Vb.  lakirowat',  bulg.  serb.  lak, Vb.  serb.  lakowati,  Cech.  lak,  Vb.  lako- vaü,  poln.  lakier,  Vb.  lakierowac.  [Hob- son-Jobson  499/501.  Dozy  Oost  57/59. Kluge  274.  DE  295/296.  Devic  DEt 150/151.    Gorjajew  180.
4516:2004.  Ar.  taläk: 'Ehescheidung' ;  hieraus  pg.  talaca  'Schei- dung'.   [DE  347.    Eguilaz  .500.
4772:'Läufer,  Eilbote'  [vom  Stamme  jol,  ol. ul  'gehen',  Vämbery  TktEtWb  S.  134. Nr.  145  I];  hieraus  [wohl  am  wahrschein- lichsten über  ngr.  oüXdKnt  MSOS  II,  239] frz.  laquois,  it.  lacM,  sp.  pg.  lacayo 'Diener';  dtsch.  Lakai.  Unmittelbar wurde  übernommen  rum.  olac  'Schnell- post', oläcar  'reitender  Eilbote'.
4927:2207.  Chiu.  zat-liao: 'Chinesischer  Lack';  hieraus  sp.  charol 'leuchtender  dauerhafter  Lack',  Vb.  cha- rolar  [Dicc  Ca<f  696  c],  pg.  charäo,  xa- räo  'chin.  Lack'  [Constancio  Dicc  974a]. [ZfromPh  XXXV,  568.    ML  9606.
5877:Schäker  1788 schäk-ern  1788 Schakren  j  17i>8 Schal  1802 Schalet  ].  1804 Schalotte  119 Schamane  1928 Schanifott  653 schamponieren  417 Schanze  1059 Scharlach  1794 scharlät  iiilid.  1794 Scharriic'arri  1849 Schasmin  942 Schauhe  737 Schaum pun  417 Sc/iaii/e  j.  1927 Äc/iea«  St.  1771 Schebecke  1740 Scheck  1762 Scheich  1775 Schellack  1295 «■cAer/f  1852 Schibbolet  1891 schicker  ].  1787  b Schicksei' j.  1789 Schikane  434 Schin(hiindchen )  420 Schlamastik  j.  1920 Schlammassel  j.  1920 SfA/t«/'  j.  1804 Schlemiel  1882 Schlemihl  1882 Schlimasdlnik  j.  1920 Schlimasel  j.  1920 Schmuck  1946 Schmiere  (stehen)  j.  1813 Schmu  (machen)  j.  1884 .Sc/if/i?iZ  j.  1811 ÄcÄ»«««  j.  1884 schmusen  j.  1884 Schmuser  j.  1884 Schoberbartel  j.  259 schofel  j.  1751 Äf/io^e  j.  1927 Schübe  mhd.  737 Schuhjack  1679 SefeZ^os  j.  184  a sf/"eZ«  j.  2210
7442:Pacorus  569 pallaca  203 pandura  2015 paradisum  1631 pascha(Ks)  1652 pastinaca  912 pelusia  1647 penidium  583 jp?M^e«  887 pomarancia  1555 pontica  (niix)  355 pyramis  1457
8306:lacayo  2130
=== FSD regolith
=== FSD shellac
WEB_vol1.txt:98317:lithographic ink; an ink used for writing on stone or for transferring autcgraphically from paper to stone. It is composed of wax, dry white soap, tallow or lard, shellac, mastic, and lampblack.
WEB_vol1.txt:104587:lac, n. (Hind. lékh; Sans. lakshd.] a resinous substance deposited upon certain trees in southern Asia by a variety of scale insect. While still Sacked to twigs and dried, it is called stick-lac; when dissolved out and sepa- rated from the twigs it is called seed-lac, and when strained through a cloth and dried it constitutes shell-lac, or the shellac of com- merce. Lac is used extensively in making var- nishes, lacquers, sealing wax, dyés, etc. _
WEB_vol1.txt:104635:é č Y of 5 r < $ 3. lakken, to lack, blame; compare D. lac/quér (-kér), n. [Fr. lacr, Moths, fate, from lanchanein, to obtain by lot or fate, ie Mette OLD. lecken to Tai] lac, from Per. lak, lac.] e, from laca, i la in Greek and Roman mythology, laken, ; : eye 1a ales h oes gum to happen.) in Gr í eA ont 1. (a) to be short (with of or in); (b) to . a clear varnish consisting that one ue a pera who measured ou pA el. gum resins dissolved in aha shellac fe z ponpen OT crimoli mali. he young lions do lack and suffer hunger. quick-drying solvents, with or w Pd Othe Jach’ry-mal, a. (ML. lacrimalis, Rogers, The young “APs. xxiv. 10. cellulose: pigments may be u at nee 3 rom L, lacrima, al oe for, or pro £ 2. to be wanting or missing; to be deficient.’ to form lacquer enamels. o lacque tears: Aa See ne aaber of small Peradventure there shall ede DVEF the me a n obtained fr m cert ch’'ry-m? an rri — Gen. xviii. 28. 4 i nd Japa 3 e tagiseefoundin ancient oman sepulchers, pop- lack oN Sees bs deficient in or ventirely smooth, highly polished fant o give a hard. la Tany supposed to have been a receptacle for ESATA OUE. . x 3. a decorative article or artel i la the tears of mourners; a lachrymatory. 4 If any of you lack wisdom, let him ask of wood and coated with this licae made of y 2. [pl.| the lachrymal glands, which produce God. f — Jamesi. 5. i Formerly, also spera lacker as tears. A 2. to want; to need. ac’qu€r, v.l. to varnish; to coat wi Also spelled poem f shedding tears: 3. to blame; to reproach; fo detract, (ObF to Germs with lacquer: formertacae, lach-ry-m4/tion, n. the act of sheddi ` 3. to suffer the absence or deprivation of; — spelled lacker. a la weeping, . o miss. [Obs. lac/quér-ér, n. one who lacquers: lach'ry-ma-tor, n, [from L. lacrima, a tear; jack vt. if PF cal usage, to pierce the hullof | maker. | 4 quers; a lacquer and -alor.| a substance that irritates the n a of (a ship) with shot. [Rare.] lac/quér-ing, n. the act of putting on a and produces tears, as tear gas: also spelled joy" interj. an exclamation of sorrow or re- _ also, the covering of lacquer or varnish Bae lacrimator. _ . pl. lach'ry:ma:to/ries gret; alas!: usually preceded by good. [Obs.] lac’quēr red, a yellowish-red color, often ay le lachy ma COT ys ni o A a. = lack-å-dāi’ṣiçăl, a. showing lack of interest or | in lacquer work. sed lo ML, lacrimatorium, trom lacrima, a tear.}a lacka miancnids listless lac’quér tree, a trec, Rhus vernicife lacheymal yer aa o ee AE ESL] adv. in a lackadaisical , cashew family. era, of the lach’ry:ma-to’ry, a. of, causing, orproducing lack-a-dai’si-cal-ly, - lac/quey (-key), n., v.l. and v.i. lackey [Ob tears: also spelled lacrimalary- lack’a-dai-sy, a. same as lackadaisical. lac'ri:măl, a. and 7. same as lachrymal, A lach’ry-mi-form”, a. shaped like a tear. _ lack’a-dai-Sy, inlerj. same as lackaday. la/cri-miin/d6, a. [It.] in music, plaintive; Ja Tach'ry:möse, a. [L. lacrimosus, from lacrima. ack’à-dāy, interj. àn exclamation of sorrow or menting: a direction to the performer, lz a tear.] } 7 ful regret. [Archaic.] lac’/ri-ma-tor, n. same as lachrymator, Pe een tedtearsicacd, © lacker, n. one who lacks. lac/ri-ma-to"ry, a. and n.; pl. lag’rimatgr x cause to ery and shed tears; sad. lack’ér, 7. and v.t. a ie ries, same as lachrymalory. l EA (DSI Tae eae aaieees lack/ey, 7.; pl. lack’eys, [OFr. laquay, a lack- Jge/ri-mdse, a. same as lachrymose, Bs lac/i-ly, adv. in a lacy manner or pattern. ey, also a soldier; Sp. lacayo, a fackey, fG0t= JAcrimo’so, a. same asilai mia $ lāc’i-ness, n. a lacy quality or T man; compare ae worthless, servile, Pr. la-croix’ite (la-krwiz/ite), n. [named after lac’ing, n. 1. the act of one who laces. lacai, a gormand. 3 K Aa oh Antoine Lacroix, a French mineralogist, 2. ashing. $ f Š 1. a male servant of low rank, usually in basic, hydrous fuophosphaterss ales 3, acord used in drawing tight or fastening; some sort of livery or uniform. + gl. calcium, manganese, and sodium: it is found : laces in general; Toue Gin boo bin ce 2. a follower who has no will of his own; a in yellowish-grecn crystals. i 3 ing, the cords which pass through holes toady. x = I (eos). #. (Er laeront iA pierced in the boards of the book, binding Jack/ey, v.t.; lackeyed, pl., pp.; lackeying, ppr. lacrosse Cee) el e; la, the, and them to the back; O in nautical nane to attend as or as if a lackey; to attend serv- ick Ge aa ct È y ope used to fasten two partsofa jlely. À ck, cros E or rey together or to bind them to lack/ey, v.i. to act as lackey; to pay servile ela abc oe the yard, boom, or gaff; (c) in machinery, a thong “attendance. 3 dians, in which two GU Ue aA of leather by which belts are lackey cat/ér-pil-lar, the larva of a lackey teams of ten men gach, e AN ce tilver brai to tri eg ee using long-handled, i 2 “4. gold or silver braid used to trim a uni- Jack’ey moth, a common European moth of pe eon Derg ry o | form, etc. pee the genus Clisiocampa, especially Clisiocampa $dvance the ball across ti 5. in bridge building, a system of braces joy stria: so called because the forewings, the field into the op- _ which conn sne bars of a truss, without which are striped, are supposed to resemblea Ponents’ goal. It is a lz eonan each other. lackey’s livery. 5 A avorite feld sport in 6. in ornithology, a border of a eae lack/lus’tér, lack’lus”tre (-tér), a. lacking tavenie ee aT leo which differs in color from the web: also, the “brightness; dull; as, lackluster eyes. redin England and i i petant Egioration of the plumage, consid- lack/lus’tér, lack’lus’tre, n. absence of the United States. - | SRS eee brightness; dullness. (Rare. lacrosse’ stick, the | Oh Rogi Be manes: a complex of tores K lac'moid,n [lacmusand-oid. aviolet-bluedye. ` packet used in playing H la FSC OAs AO a fat they e o lac/mus, n. (D. lakmoes, lacmus; lak, lac, and the gamc of lacrosse. separated without breaking, although no two tac ’ s 1 Ki ser are interlinked moes, pulp.) same as litmus. > ae lac/ry DAL e e A ĵ : a-:cin’La, n- pl. la-cin/i-ae, [L., the lappet or La-cO/ni-an, a. [L. Laconia, Laconia, sparta, = same as : as lachrymalory. | ; aan ofa are zt re from Laco (-onis); Gr. Lak6n, a Spartan.) of lac/ry-mar-y, 2 and 1 Seon as lachy- | > 1. in botany, one of the straps or tags form- or pertaining to Laconia in ancient Greece. Jac/ry-ma-to-ry, n. and 4. Y : ing the fringe on the outer portion of tps or to its inhabitants; Spartan; Lacedaemon- eas scratch GENESIO i $ lade of the petals of certain flowers; also, _ ian. > : 4 c/ry: , a. Sa a fi z chest Bye tions making this fringe. La-co/ni-in, n. a native or inhabitant of La- Jact-, same as laclo-. damino.] any of a group f- 2. in entomology, the blade or apex of the conia; a Spartan; a Lacedaemonian. lac/tam, 2. Hadons dS containing m 1 z ate ject Ee ae CEE Oe EREN an oN CO Sip the ring, formed by ti | | la-cin’i-a a-cin/iat-ed, a. [L. lacinia, a taining to Laconia, Laconian, from Lakōn, an -Nt -uv om ihe amino ane m : cen eee ; l inhabitant of Laconia, a Laconian or Spartan. ] elimination of EN oO anhydride of # g 1. adorned with fringes; fringed. 1. same as Laconian. [Rare.] eee aie carboxy eroan ; 5 ei la 2. cut deeply into narrow, jagged seg- 2. [l-] short; brief; pithy; sententious; ex- amino aoga i ee i amide.) ac | ments: said of leaves, petals, bracts, etc. pressing mu in few words Prier me man lac, nm HS nE HNO: R la ini e Laconians; as, Ris p f 3 menr ees fel eaa a hem, and forma, a S pithy, short, brief, curt, epi- Jac/tint, a. m dactans Cry oes ie lactis: f + yö A ammatic, terse. to contain milk, to £ ~ {Rare}. nyo lae, (dim. of onic n. 1.laconism; a brief, pithy mode milk.) suckling; giving suck [Preparation ; of expression. Ra f l aa lac/ta-réne, Hae taine -calico printini la 2. a brief, pithy expression; a laconism: casein or milk ; ee „used chiefly in the plural; as, he spoke in cet the colors. aati : 4 pLose g came as laciale i, O oe lac/ta-ry, 2. A Tactáries, a dairy: ym la cin'ū-lá, 7.; pl. la-cin’u-lae, (dim. from L. 3. a laconic person. | lac’ta-ry, .; pl. lac a diastase.) an. eny es E cinia, a flap, hem.] in botany, (a) a minute 44.con/i-ca, n. pl. of laconicum. Jac/tase, 2. [laci- and G pdin the intr cose i (b) the abruptly inflexed acumen or j4 Con/i-cil-ly, adv. in a laconic manner; “present in certain yeasts anc ose into & nt of each of the petals of an umbelliferous briefly: con cisely: eee nimals, which splits la ; üla i i i a-con/i-cism, n. same as laconism. and galactose. 5 la Besar a: cn botany. (@) pa ving E SA n.; pl. la-con/i-ca, [L.] in an- lac/tate, v.1.; loota tea ey pp con! 5i jo ing la Paernas DE peeso cient Rome, a vapor bath; a chamber either [L: lagali: ER r oe dis, milk.] us = Pee 3 i te ve suck, aC; ME. lak, lac. pereant compan D. ni a bathing cevahishuent or separate, hea givest secrete mill, sae ing. defective. ON else fare ERA z e young. . ilk; poe not having lac/O-nism, n. [Gr. Lakénismos, the imitation nee puck ae convert into m i 3 y. of the Lacedaemonians or Spartans in man- lac RNE (Rare.] sae read wale: Í not having any; ners, dress, etc., from Lak6nizein, to imitate _ milklike. fac, lactis, milk: a t ' the Lacedaemonians, to speak laconically, to lactate n tic acid f milk i Ia 3. the thins d. laconize.]
WEB_vol1.txt:108702:lith’6-typ”y, n. a process of stereotyping by pressing the types in ft mold, or matrix, the resulting hollows being filled with a mix- ture of gum shellac, fine sand, tar, and linseed
FSD_vol4.txt:5301:Seal'ingswax",  I   sil'iq-waks',  2   sel'ing-wfiks',  n   A   mix- ture, as  of  shellac  and  turpentine  with  a   pigment,  as vermilion  or  lampblack,  that  is  fluid  when  heated,  but qmckly  solidifies  on  cooling  used  for  making  seals,  as on  letters  documents  or  bottles  8eaJ'»wax''l.
```


## [2026-09-14T01:21:26.909Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} {n++; if ($0 ~ /Marke,  Fleck;  hunderttausend/) print \"LKT leaf\",n,\" printed~\",n-1-26}' LKT.txt; sed -n '3015,3020p' LKT.txt | cut -c1-300; echo \"=== WEB regolith\"; grep -n -o -i \"regolith[^ ]*\" WEB_vol1.txt | head -3; echo \"=== PLA leaf255 printed\"; cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json;d=json.load(open('refs_online.json'));print(d['PLA'].get('page_offset'));print(d['LKT'].get('cites'))\"",
 "description": "Get LKT page and PLA offset"
}
```


### [2026-09-14T01:21:27.974Z] TOOL RESULT

```
LKT leaf 131  printed~ 104
'Zange'  [vom  Vb.  lakat  'fassen,  auf- heben']; hieraus  mit  ar.  Art.  sp.  alicates, alicantes  'Biegzange',  frz.  alicate  'kleine Zange,  Heren  sich  die  Klempner  bedienen'. [DEFREMERY  in  JAs  1862,  I,  92.  DE 140.  DevicDEt22.  Lammens  Rem  14/15.
1294.  Ar.  laklak:
'Storch'  [onomatopoetische  Bildung  nach dem  Klappern  des  Schnabels,  ebenso  wie ass.  lakalaka  Del  HWB  885  a],  ebenso tk.  leklek,  vulg.  lejlek  [mit  Erweichung des  Gutturals  wie  in  Beg  >  bej,  s.  hier Nr.  282]  'Storch,  Kranich';  hieraus  rum. liliac  'Fledermaus';  serb.  
1295.  Sskr.  läksä:
'Marke,  Fleck;  hunderttausend',  [und nach  den  100000,  d.h.  unzähligen  In- sekten Cocca  ilicis,  welche  durch  ihren Stich  auf  quercus  coccifera  die  harzige Absonderung  bewirken]  'Lack';  hieraus in  der  urspiünglichen  Bedeutung  bind. läkh  '100000',  engl,  lack  'dass.,  bes.
1296.  Tk.  laksa:
=== WEB regolith
=== PLA leaf255 printed
301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).
entry number of Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs (1927)
```


## [2026-09-14T01:21:34.847Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"LAC, s\\|LAC,\\|lákh\\|laksha\" HJB.txt | head -10",
 "description": "Grep Hobson-Jobson for lac"
}
```


### [2026-09-14T01:21:34.914Z] TOOL RESULT

```
12862:LAC,
13229:LILAC,  8.  This  plant-name  is eventually  to  be  identified  with  anil Q^.v.),  and  with  the  Skt.  niUt,  *of  a aark  colour  (especially  dark  blue  or black)  * ;  a  fact  which  might  be  urged in  favour  of  the  view  that  the  ancients in  Asia,  as  has  been  alleged  of  them in  Europe,  belonged  to  the  body  of the  colour-blind  (like  the  writer  of this  article).    The  Indian  word  takes,
20734:[STICKLAC,  s.  Lac  encrusted  on sticks,  which  in  this  form  is  collected in  the  jungles  of  Central  India.
```


## [2026-09-14T01:21:36.985Z] TOOL CALL #82: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E1%BF%A5%E1%BF%86%CE%B3%CE%BF%CF%82",
 "prompt": "Ancient Greek ῥῆγος: give the meaning and the etymology (Proto-Indo-European root, connection with ῥέζω 'to dye', Beekes' view)."
}
```


### [2026-09-14T01:21:42.896Z] TOOL RESULT

```
# Ancient Greek ῥῆγος

## Meaning
The word denotes "blanket, coverlet" or "cover, cushion" (for beds or chairs).

## Etymology
According to the Wiktionary entry, ῥῆγος is "a result noun from the same root as ῥέζω (rhézō, 'to dye, color'), meaning something like 'that which has been dyed.'"

However, the entry notes a complication: "the vowel ῆ (ê) and the exact stem alternation ῥεζ- (rhez-) vs ῥηγ- (rhēg-) do not line up neatly," suggesting the morphological relationship is not straightforward.

The entry cites Robert S. P. Beekes' *Etymological Dictionary of Greek* (2010) as the source for this analysis. While the document doesn't explicitly state the Proto-Indo-European root, it indicates the word ultimately derives from the root underlying ῥέζω, which relates to dyeing or coloring—possibly referencing materials that have been colored or treated textiles used as coverings.
```


## [2026-09-14T01:21:47.755Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '12862,12885p' HJB.txt | cut -c1-700; echo \"=== leaf\"; awk 'BEGIN{RS=\"\\f\"} {n++; if ($0 ~ /^LAC,/ ) print \"HJB leaf\",n}' HJB.txt | head",
 "description": "Print Hobson-Jobson LAC"
}
```


### [2026-09-14T01:21:49.046Z] TOOL RESULT

```
LAC,
Portuguese  in  India  (p.  88).    I  cannot explain  it.    [See  BAO.J
1799. — "The  kionms  or  oonvents  of  the Rhahaans  are  different  in  their  structure from  common  houses,  and  much  resemble the  architecture  of  the  Chinese  ;  they  are made  entirely  of  wood ;  the  roof  is  com- posed of  different  stages,  supported  by .strong  pillars,"  ko.—Synus,  p.  210.
KTTHE^  s.  Hind.  Kaiihl,  A form  of  cursive  Nagiri  character,  used by  Bunyas,  &c.,  in  Gangetic  India.  It is  from  Kdyath  (Skt.  Kdya8tha)y  a member  of  the  writer-caste.
LAO,  8.  Hind.  Idkhy  from  Skt. ■lakshd,  for  rdkshd.  The  resinous  in- <:rustation  produced  on  certain  trees <of  which  the  dhok  (see  DHAWK)  is one,  but  chiefly  Peepnl,  and  khomim fkuiumy  ktufwnU>\  i.e.  Schleichera  Hjma^ trijuga)  by  the  puncture  of  the  Lac insect  {Goccus  Lacca,  L.).  See  Boocburahy in  Vol.  III.  A8,  jBa.,  384  seqq;  ("and  a full  list  of  the  trees  on  wnicn  the insect  feeds,  in  Watty  Earn.  Did,  ii. 410  M^.].  The  incrustation  contains 60  to  70  per  cent,  of  resinous  lac,  and 10  per  cent  of  dark  red  colouring matter  from  which  is  manufacturea lac-dye.  The  material  in  its  original <;rude  form  is  
Though  Idk  bears  the  same  sense  in Persian,  and  lak  or  Ivk  are  used  in modern  Arabic  for  sealing-wax,  it would  appear  from  Dozy  (Gloe.y  pp. 2d5-6,  and  Oosterlingenj  57),  that identical  or  approximate  forms  are used  in  various  Arabic-speaking  regions for  a  variety  of  substances  giving  a  red dye;,  including  the  coccus  ihcis  or iLermes.  Stil^  we  have  seen  no  evi- dence that  in  India  the  word  was applied  otherwise  than  to  the  lac  of our  heading.    (Qarcia  says  that   the
Arabs  called  it  loc-svmutriy  'lac  of Sumatra ' ;  probably  because  the  Pegu lac  was  brought  to  die  ports  ',of Sumatra,  and  purchased  there.)  Aiid this  the  term  in  the  Periplus  seems imquestionably  to  indicate ;  whilst  it is  probable  that  the  passage  quoted from  Aelian  is  a  much  misconceived account  of  the  product  It  is  not nearly  so  absura  as  De  Monfart's account  below.  The  English  word hke  for  a  certain  red  colour  is  from thia  So  also  are  lacquer  and  lackered ware,  because  Ux  is  used  in  some  of  the varnishes  with  which  such  ware  is prepared.
c.  A.D.  80-90.— These  articles  are  imported
(to  the  ports  of  Barhariciy  on  the  W.  of  the
Red  Sea)  from  the  interior  parts  of  Ariake : —
"  ^Idripot  *I»8iK6t  Kal  orSfivjJM  (Indian
iron  and  steel)
•  •  *  «  «
Periplus,  §  6.
c.  250.— "There  are  produced  in  India animals  of  the  size  of  a  beetle,  of  a  red colour,  and  if  you  saw  them  for  the  first time  you  would  compare  them  to  cinnabar. They  have  very  long  legs,  and  are  soft  to the  touch  ;  they  are  produced  on  the  trees that  bear  elecCrum,  and  they  feed  on  the fruit  of  these.  The  Indians  catch  them and  crush  them,  and  with  these  dye  their red  cloaks,  and  the  tunics  under  these,  and everything  else  that  they  wish  to  turn  to this  colour,  and  to  dye.  And  this  kind  of clothing  is  carried  also  to  the  Kizig  of Persia.  — Aelian,  de  Nat.  Animal,  iv.  46.
c.  1348. — The  notice  of  lacca  in  Pegolotti is  in  parts  very  difficult  to  translate,  and we  do  not  feel  absolutely  certain  that  it refers  to  the  Indian  nroauct,  though  we believe  it  to  be  so.  Thus,  after  ezpuiining that  there  are  two  classes  of  /oroo,  the  mo- tura  and  acerbaj  or  ripe  and  imripe,  he  goes on  :  "  It  is  produced  attached  to  stalks,  t.e. to  the  branches  of  shrubs,  but  it  ought  to be  clear  from  stalks^  and  earthy  dust,  and sand,  and  from  eostvrre  (?).  The  stalks  are the  twigs  of  the  wood  on  which  it  is  pro- duced, the  eostiere  or  Jwe,  as  the  Catalans call  them^  are  composed  of  the
1610.— "There  also  grows  a  very  large quantity  of  lacoa  (or  Itura)  for  makinff red  colour,  and  the  tree  of  this  is  formea like  our  trees  which  produce  walnuts." — Vartkemoy  238.
1516.— "Here  (in  Pegu)  they  load  much fine  laqoar,  which  grows  in  the  country." — Barbota,  Luhon  Acad.,  866.
LACGABIVE  ISLANDS,
500
LACK.
1519.—"  And  because  he  had  it  much  in chanre  to  get  all  the  leu:  (alacre)  that  he ooula,  the  governor  knowing  through  infor- mation of  Uie  merchants  that  much  came  to the  Coast  of  Choromandel  by  the  ships  of Pegu  and  Martaban  that  frequented  that ooast.  .  .  ."—Correaf  ii.  667.
1668.— "Now  it  is  time  to  speak  of  the iBCTBy  of  which  so  much  is  consumed  in  this country  in  closing  letters,  and  for  other  seals, in  the  place  of  wax." — OarciOj  f.  112».
1582.— "  Laker  is  a  kinde  of  gum  that  pro- cedeth  of  the  ant."— Ca*toil«ia,  tr.  by  N.L., f.  33.
=== leaf
```


## [2026-09-14T01:21:59.847Z] TOOL CALL #84: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%84%D8%A7%DA%A9",
 "prompt": "Persian لاک: list the senses and etymologies given (especially 'lac, resin/lacquer' and any Sanskrit/Prakrit source), and note any Middle Persian form."
}
```


## [2026-09-14T01:22:00.889Z] TOOL CALL #85: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/lakh",
 "prompt": "Give the etymology of 'lakh' (100,000) — Hindi lakh, Sanskrit lakṣa, and what the original meaning of lakṣa is said to be."
}
```


### [2026-09-14T01:22:04.547Z] TOOL RESULT

```
I appreciate your question, but I must be honest: the web page content provided is from Etymonline's homepage and footer, which contains navigation, branding, and support information—but it does not include any dictionary entries or etymological data about the word "lakh."

To answer your question about lakh's etymology, I would need access to the actual entry from Etymonline's dictionary database, which isn't present in the material you've shared. I cannot provide the etymology you're requesting based solely on this homepage content.

If you have access to Etymonline's actual entry for "lakh," please share that text, and I'd be happy to provide the etymology with proper attribution.
```


### [2026-09-14T01:22:05.089Z] TOOL RESULT

```
# Persian لاک (lâk) - Senses and Etymologies

## Senses

**Etymology 1** (native Persian origin):
1. Trough; wooden vessel
2. Tortoise shell (literal and metaphorical)

**Etymology 2** (borrowed):
1. Nail polish (short form of "lâk-e nâxon")
2. Lacquer

## Etymology Details

**Etymology 2** involves borrowing from Prakrit *lakkhā* ("lac"), which derives from Sanskrit *लाक्षा* (lākṣā). The entry notes cognates including Hindi *लाख* (lākh, "lac") and English "lac."

**Etymology 1** traces to Old Iranian *nāwaka-* (diminutive of Proto-Iranian *náHuš*, meaning "boat"), representing a contraction of *لاوک* (lâvak, "kneading trough") with an *l* < *n* sound change.

## Middle Persian

The entry contains no explicit mention of a Middle Persian form.
```


## [2026-09-14T01:23:17.570Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && awk 'BEGIN{RS=\"\\f\"} END{print \"Bd2 leaves:\",NR}' WLD_Bd2_pages.txt; grep -n \"reĝ-\\|rajyati\\|ῥέζω\\|rajyate\\|rajayati\" WLD_Bd2_pages.txt | head -10",
 "description": "Grep Walde-Pokorny Bd2 for reĝ-"
}
```


### [2026-09-14T01:23:18.731Z] TOOL RESULT

```
Bd2 leaves: 724
```


## [2026-09-14T01:23:23.129Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"färben\" WLD_Bd2_pages.txt | head -20; echo \"=== find page 366\"; awk 'BEGIN{RS=\"\\f\"} {n++; if (n>=380 && n<=400 && $0 ~ /re[ĝgg]-|rag-|ragam/) print n}' WLD_Bd2_pages.txt | head",
 "description": "Grep WLD Bd2 for färben"
}
```


### [2026-09-14T01:23:24.234Z] TOOL RESULT

```
=== find page 366
387
```


## [2026-09-14T01:23:27.122Z] TOOL CALL #88: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && awk 'BEGIN{RS=\"\\f\"} NR>=385 && NR<=389 {print \"==LEAF\",NR; print substr($0,1,800)}' WLD_Bd2_pages.txt",
 "description": "Print WLD Bd2 leaves 385-389"
}
```


### [2026-09-14T01:23:28.193Z] TOOL RESULT

```
==LEAF 385
                                                        ,




380                                          lauq(o)        laqu-


des Superlativs XdQcoxaTog in Aa/apog (oder Xa^sQog) aufzulosen (Schulze
Qu. ep. 26 in. Lit, Boisacq 558, Bechtel Lex. 212); got Imm n, ahd. Ida
(n.,m.) „Lohn, Vergeltung‘‘, an. laun n. pi., ags. lean ds.; air. log, luag^
loach „Lohn, Preis“  (mit g- oder ^/i-Formans, das in Worten ahnlicher
Bed. sonst allerdings nicht zu belegen ist), folad {folidh) „Substanz‘^ -=
cymr. golud „Eeichtum“, acorn, tvuhidoc „dives‘' {^iipo-lati-to-7n)\ s. zuletzt
Pedersen KG. II 39 ^), [aber gall. Uellaimo-dnmim Orfcsname, Cassl-tiellaunus
Mannername, Catu-nellamii Yolksname ist vielmehr in vell-aim- zu zer-
legen], cymr. IJaiven „fr6hlich“ (usw. n. Pokorn
==LEAF 386
                                                                 ;   ^        ;




                                                          lak-, leg-      — lat-                                        381


   Fick KZ. 22, 553, Wb.   531, IP 237, III* 358,                                              Falk-Torp u. laag, Zu-
pitza Gutt. 134, Vf. LEWb.^ u. lacus, Berneker 730                                             (wo gegen Entlehnung
des    si.    Wortes aus dem Germ., ahd. lahlia^ 'woriiber s. ^kg-                                          „ti‘opfeln“).

    Moglieberweise mit alter Bed.-Entw. von ,,Einbiegung, Niederung^', zu
5
  ,sumpfige Niederung^', sodaB zuWz. (o)lPq- j,biegen'^ vgl. lit. lanka ,jNiede-
rung, Sumpf“ zu lenhti „biegen“.


lak- oder leg- „sehen''?

==LEAF 387
382                                                   lat-, slat-



     aisL lepja (^lapjon-) „Lehin, Schmutz^, ahd. Utto 5 ,Ton, Lehm“, nhd. Letten
(dessen         e,   obwohl       in   bair.-alem. Mdarten ofifen          —   s.   Kluge ® s. v., Kauff-
mann Schwab. Mdart. 59                    — doch Umlaut             -e ist).
   Persson AVzerw. 171,111, Pick 11* 238, Stokes BB. 23, 53.           Wruss.                —
iaiok „Dachrinne“ (woraus   lit. latakas „zsgelaufenes Wasser, AVasserrohre“),

gruss. lotokz „Mulde, Riiine‘‘ u. dgl. bleiben fern (Berneker 735, sowie u.
lat- ,.Latte“, wo auch iiber ksl. laHih ,,%vxQa^^ usw.).
   Mit anl. s- scheinen yerwandt: abg. sloia „na6kaltes Wetter“, serb. sVota
„feiner Eegen“ usw. (s. y. d. Osten-Sacken IP.
==LEAF 388
                              lap-: l9p-        — lab-, labh*(?), lap(h)-                            383

Bemeker 735;          slav.   Bed. -Kern          ist     .,Einne‘');    arm. last „Holzflo6, Boot‘‘
(Scheftelowitz       BB. 29, 32   ;
                                      s.   lazd- oder lozd-,            si.



lap- lap- „leuchten, gliihen, brennen^^.
         :




   Gr. )Afi7io:> „leuchte “5 kajundg „racker‘, kajujigog „leuchtend*‘ (mit ursprgl.
blofi praesensbildendem Nasal; ai. lampaia- „gieng, liistern^ nach Uhlen-
beck Ai. Wb. 258 als „glanzend, gluhend“ oder „vor Begier brennend‘‘
heranzuzieben,       ist   daber aucb formell unwahrscheinlich)                   ;
                                                                           
==LEAF 389
                                                                                              ;




384                           laba^(u)g-, -ug-   ;   laba^(u)g-, -ug-


daher wohl ursprgl. zu HapQi)- „lecken“, aber mit der anderen Eeihe zu
einer   vollstandigen       Einheit   fiirs   slav.     Sprachgefiihl       verwachsen).   Wohl
Neuschopfungen mit pp sind itaL lappare^                   frz.   laper (brauchen niclit germ,
zu sein), nhd. lappen „lecken“ (G. Meyer Wb. 237) daneben nhd. mdartl.  ;


lahbe „Lippe‘\ lahern „lang8am, einfaitig reden; leckend trinken", skr.
(Lw. ?) lahati „saufen wie Hunde oder Katzen'' u. dgl. (Berneker 681).
  Gr. Xapvooco ,verschlinge“
                        5
                                    oder Hahliiik-id^ dem slav. lub^z-ati
```


## [2026-09-14T01:23:43.772Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && awk 'BEGIN{RS=\"\\f\"} NR==371 {print substr($0,1,1500)}' WLD_Bd2_pages.txt; echo \"###\"; grep -n \"reĝ\\|rajyati\\|rajayati\\|ragas\\|Farber\" WLD_Bd2_pages.txt | head -20",
 "description": "Print WLD Bd2 leaf 371"
}
```


### [2026-09-14T01:23:44.816Z] TOOL RESULT

```
366                                          reg-


  lat. rigare zu got. rign usw. unter Annahme eines idg. gh gestellt Yon
Vanicek 273, Curtius 19t, Hoffmann BB. 26, 136. Dock ist gh durch gr.
Pqsxco (for *juqsxc6) nicht erwiesen (G. Meyer, Alb. Wb. 374, Hoffmann aaO.),
da idg. mr- r- sehr unsicher ist,
                  :




1.   reg- „farben".
     Ai. rdjyati „farbt sich, rotet sich“, raga-h „das Farben, Farbe, Rot‘';
     gr. Q£^(jo^ aor. ge^ai „farben‘‘,     giyjua ,,gefarbter Stoff^\ gaysvg (auch go-
ysvg) „FarbeF‘,                     ‘
                                                       Hes. bom. g^yog {giyog Anakr.)
n.   „gefarbter Teppich, bunte Decke*^, grjysvg' ^acpevg Hes.
  Curtius 185f.; mit fernzuhaltendem (so ^reg'^os „Dunkelheit“) Fick                           F
117, 299, 526.  Gr. grjyog nicht besser als ^^grjyog „geflochtener Teppich‘^
zu einer Wechselform ureg- der Wz. uerg- (s. uer-) „drehen“ nach Mar-
strander IF. 22, 334 (wo g<b^ „eine Spinnenart^' yerglichen wird; dock ist
letzteres     = gd)^ „Beere“, yne auch gd^ dieselbe Doppelbed. hat,                   s.   Prell-
witz ^ 395,      Lehmann ZfcPh. 6, 436 a 3) oder der Wz. uerg-                    „Egyov^^   (dt.
Werk und Werg^ ahd. werah{-hh-\ were n. nach Hirt PBrB. 23, 354); An-
laut    kann jedenfalls nicht aus II. IX, 661 xmed xe g}]y6g re gefolgert
werden, s. Persson Beitr. 509, und            m
                                      der Dehns
###
16531:ders „na6 und fett), Rasen“, mauragas, muragas pi. ,.Mauseobr (Sumpf-
18489:neker 88) „Farberrote“ ist nicht Yorzuziehen.                —
20148:modhro- oder madhro- „blau; Farberpflanze'*^?
20150:eale, glatte Wiesenrote“, ahd.  matara ^Farberrote^^, ags. mcede^'e, mceddre
24195:,,Farber“ AnschluB.          Da6 keinen Yokalvorschlag erfahren hat, ist
```


## [2026-09-14T01:24:00.410Z] TOOL CALL #90: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/%D8%B1%D9%86%DA%AF' \\\n 'https://www.etymonline.com/word/regolith' \\\n 'https://en.wiktionary.org/wiki/%E0%A4%B2%E0%A4%BE%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A4%BE' \\\n 'https://www.etymonline.com/word/lac' \\\n 'https://abadis.ir/fatofa/%D8%B1%D8%AC%DB%8C%D8%AF%D9%86/' \\\n 'https://abadis.ir/fatofa/%D8%B1%D8%B2%DB%8C%D8%AF%D9%86/' \\\n 'https://abadis.ir/fatofa/%D9%84%D8%AC%D9%87/' \\\n 'https://en.wiktionary.org/wiki/%E1%BF%A5%E1%BF%86%CE%B3%CE%BF%CF%82' \\\n 'https://en.wiktionary.org/wiki/%D9%84%D8%A7%DA%A9' ; do\n python3 tools/fetch_source.py \"$u\" --note 'page 418, root Reg 3 (to dye, color): rang/rajidan/lak/lojjeh/rhegos-regolith verification' 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-14T01:24:07.442Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/1d8a9d9c04ead15b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0f2a4f0eab447e48.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6c2a20a6c64283f2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c6bf173537ac213e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4f0e65ec5f95fb89.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/662ab5f8eea22c49.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e2ff68ca64cef30a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/23d15743743155c4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4ef2ee5554c9eadb.txt
```


## [2026-09-14T01:24:10.626Z] TOOL CALL #91: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-14T01:24:10.685Z] TOOL RESULT

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


## [2026-09-14T01:35:00.963Z] TOOL CALL #92: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-418.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_RANG   = \"https://en.wiktionary.org/wiki/%D8%B1%D9%86%DA%AF\"\nW_REGO   = \"https://www.etymonline.com/word/regolith\"\nW_LAKSA  = \"https://en.wiktionary.org/wiki/%E0%A4%B2%E0%A4%BE%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A4%BE\"\nE_LAC    = \"https://www.etymonline.com/word/lac\"\nA_RAJ    = \"https://abadis.ir/fatofa/%D8%B1%D8%AC%DB%8C%D8%AF%D9%86/\"\nA_RAZ    = \"https://abadis.ir/fatofa/%D8%B1%D8%B2%DB%8C%D8%AF%D9%86/\"\nA_LOJ    = \"https://abadis.ir/fatofa/%D9%84%D8%AC%D9%87/\"\nW_RHEGOS = \"https://en.wiktionary.org/wiki/%E1%BF%A5%E1%BF%86%CE%B3%CE%BF%CF%82\"\nW_LAK    = \"https://en.wiktionary.org/wiki/%D9%84%D8%A7%DA%A9\"\n\nPOK_NOTE = (\"POK_full.txt l.69548 ff. ‘Root / lemma: reĝ-/ (and sreg-?) – Meaning: to paint \"\n            \"[G. färben] – Material: Old Indic rajyati ‘färbt sich, rötet sich’ … ragam. \"\n            \"‘das Färben, rote paint, color’; gr. ρεζω ‘paint’, ρεγμα ‘gefarbter Stoff’, \"\n            \"ραγευς ‘Farber’ … References: WP. II 366. Page(s): 854.’\")\n\nWLD_NOTE = (\"WLD_Bd2_pages.txt leaf 371 = printed p.366: ‘1. reĝ- „färben“. Ai. rájyati „färbt sich, \"\n            \"rötet sich“, rága-ḥ „das Färben, Farbe, Rot“; gr. ῥέζω, aor. ῥέξαι „färben“, \"\n            \"ῥέγμα „gefärbter Stoff“, ῥαγεύς (auch ῥογεύς) „Färber“, … hom. ῥῆγος n. \"\n            \"„gefärbter Teppich, bunte Decke“, ῥηγεύς· βαφεύς Hes.’\")\n\nAHD_NOTE = (\"AHD_watkins1985.txt l.893: ‘reg-3. To dye. Lengthened-grade form *rēg-. 1. Suffixed form \"\n            \"*rēg-es- in Greek rhēgos, blanket, rug: REGOLITH. 2. Sanskrit rāgaḥ, color, red: RAGA. \"\n            \"3. Perhaps Sanskrit rākshā, earlier form of lākshā, red dye: LAC1. [Pok. 1. reg- 854.]’ \"\n            \"— Nourai’s root name ‘Reg 3’ and its gloss come straight from this Watkins entry.\")\n\nSYN_NOTE = (\"SYN.txt leaf 1131/1132 = printed pp.1050–1051, §15.61 COLOR, paragraph 7: ‘Skt. rañga-, \"\n            \"rāga- : raj- “be colored, grow red”, Grk. ῥέζω “dye”, ῥεγεύς “dyer”, etc. Walde-P. 2.366.’ \"\n            \"Nourai’s gloss ‘be colored, grow red’ is Buck’s wording verbatim.\")\n\nIEC_NOTE = (\"IEC.txt p.1065 (leaf ~547): ‘regio “dye, tinge; be tinged”. WP II, 366 — Skt. rājyāmi, v. \"\n            \"“get coloured, flush”; Per. razam, v. “dye, tinge”; Gk. rhézō (rheg-), v. (2) “dye”; \"\n            \"cf. rhégma, n. “dyed object”.’\")\n\nCHEUNG_NOTE = (\"CHEUNG.txt ll.20596–20628, pp.313–314: ‘*ra(n)j “to colour, dye” … MIDDLE PERSIAN: \"\n               \"MMP rng, BMP rng /rang/ “colour” … NWIR: NP razidan “to colour, dye, taint, tinge”, \"\n               \"NP rang “colour” … SANSKRIT: raj “to colour, to become red” … PIE *(s)reg- \"\n               \"“to colour (dark)” … Pok.: 854. IE COGNATES: Gr. ῥέζω “I dye, paint”, Gr. ῥῆγος (n.) \"\n               \"“carpet, rug”, Gr. ῥογεύς “dyer”.’ Cheung makes MP rang an inherited Iranian form, \"\n               \"not a loan from Indic.\")\n\ndata = {\n  \"pdf_page\": 418,\n  \"book_page\": 388,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [\n    {\n      \"entry\": 1,\n      \"root\": \"Reg 3\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *reĝ- / *(s)reg- ‘to dye, colour’ (Pokorny 854 ‘reĝ- färben’; Watkins AHD reg-3 ‘to dye’; Walde-Pokorny II 366)\",\n      \"note\": (\"The root box is correct in every respect. Pokorny IEW p.854 has ‘reĝ- (and sreg-?) \"\n               \"„färben“’ with exactly the material Nourai draws (Skt. rajyati / rāga-, Gk. ῥέζω / \"\n               \"ῥαγεύς); the numbering ‘Reg 3’ and the gloss ‘to dye’ are taken over from Watkins’ \"\n               \"AHD appendix, where reg-1 = ‘move in a straight line / king’, reg-2 = ‘moist’ and \"\n               \"reg-3 = ‘to dye’. Cheung 2007: 313 f. reconstructs the Iranian branch as *ra(n)j \"\n               \"‘to colour, dye’ < PIE *(s)reg-. Two substantive problems on this page, both of them \"\n               \"Nourai’s and not the scanner’s: (a) the Pahlavi/Persian rang branch is hung under \"\n               \"Sanskrit, whereas MP rang is an inherited Iranian continuation of *ra(n)j, a cognate \"\n               \"of Skt. raṅga- rather than a borrowing from it; (b) the Greek box glosses ῥῆγος as \"\n               \"‘color, dye (red)’ and ‘rego-lith’ as ‘red stone’, while every source (Walde-Pokorny \"\n               \"II 366, Watkins, Beekes) makes ῥῆγος a ‘dyed rug, blanket’ and ‘regolith’ an 1897 \"\n               \"English coinage meaning ‘blanket of stone’. The lak / lajj / lojjeh branch rests on \"\n               \"the old conflation of Skt. lākṣā ‘lac’ with lakṣá- ‘100,000’, which Nourai himself \"\n               \"flags in his NOTE (POK:32, KLN:47,856 = root ‘Alek’ ‘to protect’).\"),\n      \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *reĝ- / *(s)reg- «رنگ کردن، رنگین شدن» در پوکورنی \"\n                  \"صفحهٔ ۸۵۴ و در پیوست واتکینز (AHD) زیر reg-3 آمده است؛ عنوان «Reg 3» و معنای آن \"\n                  \"در کتاب نورایی عیناً از همین پیوست گرفته شده. چونگ (۲۰۰۷، ص ۳۱۳–۳۱۴) شاخهٔ ایرانی را \"\n                  \"*ra(n)j «رنگ کردن» بازسازی می‌کند. دو اشکال اساسی در نمودار هست: یکی آنکه «رنگ» فارسی \"\n                  \"زیر سنسکریت نشانده شده، حال آنکه rang فارسی میانه میراثی ایرانی و هم‌ریشهٔ raṅga- \"\n                  \"سنسکریت است نه وام‌گرفته از آن؛ دیگر آنکه معنای واژهٔ یونانی ῥῆγος «فرش و پوشش رنگین» \"\n                  \"است نه «رنگ سرخ»، و regolith واژه‌ای انگلیسی از سال ۱۸۹۷ میلادی به معنای «پوشش سنگی» \"\n                  \"است. در مجموع ادعای نورایی دربارهٔ خود ریشه درست است.\"),\n      \"sources\": [W_RANG, W_REGO, W_RHEGOS],\n      \"ref_check\": [\n        {\"ref\": \"POK:854\", \"status\": \"supports\", \"note\": POK_NOTE}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. II p.366 (WLD_Bd2_pages.txt leaf 371)\", \"stance\": \"supports\", \"note\": WLD_NOTE},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. reg-3 (AHD_watkins1985.txt l.893)\", \"stance\": \"supports\", \"note\": AHD_NOTE},\n        {\"src\": \"IEC\", \"where\": \"Mann p.1065 s.v. regio\", \"stance\": \"supports\", \"note\": IEC_NOTE},\n        {\"src\": \"CHEUNG\", \"where\": \"pp.313–314 s.v. *ra(n)j\", \"stance\": \"supports\", \"note\": CHEUNG_NOTE}\n      ],\n      \"nodes\": []\n    }\n  ]\n}\n\nN = data[\"entries\"][0][\"nodes\"]\n\nN.append({\n  \"id\": 1,\n  \"lang\": \"Sanskrit\",\n  \"words\": \"raj, râga, ranga\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"Skt. raj- / rañj- (pres. rajyati, later rajyate, caus. rajayati / rañjayati) ‘to be dyed, \"\n    \"become red, glow’, with the deverbal nouns rāga- m. ‘dyeing, (red) colour, hue’ and \"\n    \"raṅga- m. ‘colour, paint’ (the -ṅ- of raṅga- is the nasal infix of the rañj- present, \"\n    \"generalised into the noun). Pokorny 854 puts precisely these forms at the head of the \"\n    \"root reĝ- ‘färben’, as do Walde-Pokorny II 366 and Buck §15.61; the root vowel is the \"\n    \"inherited e-grade, Indo-Iranian *a. Nourai’s gloss ‘be colored, grow red’ is Buck’s wording \"\n    \"for raj- verbatim (SYN p.1051). Semantically rāga- later widens to ‘passion, mood’ and \"\n    \"gives the musical term rāga.\"),\n  \"derivation_fa\": (\n    \"ریشهٔ سنسکریت raj-/rañj- (حال rajyati) «رنگین شدن، سرخ شدن» و اسم‌های rāga- «رنگ، رنگ‌کردن» \"\n    \"و raṅga- «رنگ» دنبالهٔ مستقیم ریشهٔ هندواروپایی *reĝ- «رنگ کردن» است؛ نونِ raṅga- همان نون میانجی \"\n    \"ستاک حال rañj- است که به اسم هم راه یافته. پوکورنی (۸۵۴)، والده–پوکورنی (جلد ۲، ۳۶۶) و \"\n    \"باک (بند ۱۵٫۶۱) همین صورت‌ها را می‌آورند؛ معنایی که نورایی نوشته عیناً عبارت باک است. \"\n    \"ادعای نورایی درست است.\"),\n  \"sources\": [W_RANG],\n  \"ref_check\": [\n    {\"ref\": \"SYN:1051\", \"status\": \"supports\", \"note\": SYN_NOTE}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"p.854 s.v. reĝ- ‘färben’\", \"stance\": \"supports\", \"note\": POK_NOTE},\n    {\"src\": \"WLD\", \"where\": \"Bd. II p.366\", \"stance\": \"supports\", \"note\": WLD_NOTE},\n    {\"src\": \"AHD\", \"where\": \"Watkins s.v. reg-3\", \"stance\": \"partial\", \"note\": \"AHD lists ‘Sanskrit rāgaḥ, color, red: RAGA’ under reg-3 but not raṅga- or the verb raj-; same root, shorter material.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann p.1065 s.v. regio\", \"stance\": \"supports\", \"note\": IEC_NOTE},\n    {\"src\": \"CHEUNG\", \"where\": \"p.314\", \"stance\": \"supports\", \"note\": \"Cheung s.v. *ra(n)j lists ‘SANSKRIT: raj “to colour, to become red” (AV+) = EWAia II: 424’.\"}\n  ]\n})\n\nN.append({\n  \"id\": 2,\n  \"lang\": \"Pahlavi\",\n  \"words\": \"rang\",\n  \"verdict\": \"disputed\",\n  \"derivation\": (\n    \"The Middle Persian word is right: MacKenzie, Concise Pahlavi Dictionary p.74 gives ‘rang \"\n    \"[lng | M rng, N ~] colour, dye’, and the Manichaean spelling rng confirms it. What is wrong \"\n    \"is the arrow: Nourai makes Pahlavi rang descend from Sanskrit raj/rāga/raṅga, whereas modern \"\n    \"Iranian etymology treats it as inherited. Cheung 2007: 313 f. sets up Proto-Iranian *ra(n)j \"\n    \"‘to colour, dye’ (< PIE *(s)reg-, Pok. 854) with MP rang ‘colour’, NP razīdan, Khot. rrāsa- \"\n    \"‘dark coloured’, Chorasmian rxtyk ‘red’, Pamir rēz-/raz- ‘to colour the eyes’ — a whole Iranian \"\n    \"family that cannot be a loan from Indic. Horn no.623 (p.138 f.) likewise only equates np. rang \"\n    \"with skr. raṅga- and reserves his ‘LW.’ label for the words Kurdish renk, Pashto rang and \"\n    \"Baluchi rang that were borrowed *from* Persian; Hübschmann, Pers. Stud. §138 (p.246) files \"\n    \"rang ‘Farbe’ = skr. raṅga- among the regular Old Iranian *-ng- correspondences. So Skt. raṅga- \"\n    \"and MP rang are sister forms of PIE *reĝ-, not mother and daughter; Nourai’s ultimate root is \"\n    \"nevertheless correct.\"),\n  \"derivation_fa\": (\n    \"صورت فارسی میانه درست است: مکنزی (ص ۷۴) rang «رنگ، رنگ‌مایه» را با نوشتار lng و صورت \"\n    \"مانوی rng آورده است؛ اما پیکان نمودار نادرست است. به باور چونگ (۲۰۰۷، ۳۱۳–۳۱۴) rang بازماندهٔ \"\n    \"ریشهٔ ایرانی آغازین *ra(n)j است که نمودهای دیگرش ختنی rrāsa-، خوارزمی rxtyk «سرخ» و \"\n    \"افعال پامیری rēz-/raz- است؛ این گستره را نمی‌توان وام‌واژهٔ هندی دانست. هرن (شمارهٔ ۶۲۳) نیز فقط \"\n    \"رنگ فارسی را با raṅga- سنسکریت برابر می‌نهد و وام‌واژه بودن را فقط دربارهٔ کردی renk و پشتو rang \"\n    \"می‌گوید که از فارسی گرفته شده‌اند. پس: raṅga- سنسکریت و rang پهلوی هم‌ریشه‌اند نه مادر و فرزند؛ \"\n    \"پژوهش امروزی مسیر نورایی را رد می‌کند، هرچند ریشهٔ نهایی همان است که او گفته.\"),\n  \"sources\": [W_RANG],\n  \"ref_check\": [\n    {\"ref\": \"HRN:138\", \"status\": \"partial\", \"note\": (\"HRN.txt l.5548–5554, Horn no.623 (printed p.138 f., the page break ‘- 139 -’ falls inside \"\n        \"the entry): ‘623. (1)reng ‚Farbe‘. skr. rañga- ‚Farbe‘; arm. LW. erang ‚Farbe‘ (H., No. 96). \"\n        \"LW. kurd. renk, reng; afɣ. rang; bel. rang (216).’ Horn equates NP rang with Skt. raṅga- but \"\n        \"does not derive it from Sanskrit — his ‘LW.’ marks are on the Kurdish/Pashto/Baluchi words \"\n        \"borrowed from Persian.\")},\n    {\"ref\": \"BQT:964\", \"status\": \"partial\", \"note\": (\"BQT_v2_pages.txt leaf 426 (printed ≈ 966–969 by the running-head estimate, leaf+543±3) carries the \"\n        \"رنگ entry with exactly the Hāfez line Nourai prints («غلام همت آنم که زیر چرخ کبود / ز هر چه رنگ \"\n        \"تعلق پذیرد آزاد است») and Mo‘in’s footnote ‘* رنگرز … از: رنگ + رز (رزیدن)’. Borhan gives \"\n        \"the word and its senses; it says nothing about descent from Sanskrit, and the OCR of this \"\n        \"scan does not preserve a Latin-script Pahlavi form on the page.\")},\n    {\"ref\": \"PHD:72\", \"status\": \"supports\", \"note\": (\"PHD.txt leaf 96 = printed p.74 (two printed pages per leaf region, the entry sits on the 72/74 \"\n        \"opening): ‘rang [lng | M rng, N ~] colour, dye’. MacKenzie confirms the Pahlavi form and gloss \"\n        \"Nourai gives.\")}\n  ],\n  \"consulted\": [\n    {\"src\": \"CHEUNG\", \"where\": \"pp.313–314 s.v. *ra(n)j ‘to colour, dye’\", \"stance\": \"contradicts\", \"note\": CHEUNG_NOTE},\n    {\"src\": \"HUB\", \"where\": \"Persische Studien §138, p.246 (HUB.txt l.8821)\", \"stance\": \"partial\", \"note\": \"Hübschmann: ‘rang ‚Farbe‘ = skr. raṅga-’, listed among the words keeping Old Iranian -ng-; and ‘erang ‚Farbe‘ = np. rang’ for the Armenian loan. An equation of cognates, not a derivation from Sanskrit.\"},\n    {\"src\": \"PHD\", \"where\": \"p.74 s.v. rang\", \"stance\": \"supports\", \"note\": \"‘rang [lng | M rng, N ~] colour, dye’ (PHD.txt leaf 96).\"},\n    {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II (glossary)\", \"stance\": \"silent\", \"note\": \"grep ‘rang’ in NYB_vol2_glossary.txt returns only compounds (nērang, ērang); no separate rang ‘colour’ lemma found.\"}\n  ]\n})\n\nN.append({\n  \"id\": 3,\n  \"lang\": \"Persian\",\n  \"words\": \"rang; rang-â-rang; rangîn kamân\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"NP رنگ rang continues MP rang [lng] without change (Middle Persian final -ng is stable into New \"\n    \"Persian, cf. tang, sang); Wiktionary, following Cheung 2007: 314, gives ‘from Middle Persian lng \"\n    \"(rang), from Proto-Iranian *rang- “to colour, dye”, from PIE *(s)reg-’. The derivatives in the box \"\n    \"are transparent New Persian formations on that noun: آب‌رنگ āb-rang ‘water-colour’ (āb ‘water’ + rang), \"\n    \"رنگرز rangraz ‘dyer’ = rang + -raz, the present stem of رزیدن razīdan ‘to dye’ (so Mo‘in’s footnote \"\n    \"in Borhan-e Qāte‘ at the رنگرز entry: ‘از: رنگ + رز (رزیدن)’), رنگ‌آمیزی rang-āmīzī ‘colouring’; \"\n    \"رنگارنگ rang-ā-rang ‘of many colours’ is the common Persian intensifying reduplication X-ā-X \"\n    \"(cf. gunāgun, sarāsar), beside the variant رنگ برنگ and the adjective رنگین rangīn (rang + -īn); \"\n    \"رنگین‌کمان rangīn-kamān ‘rainbow’ is literally ‘coloured bow’, a modern calque-like compound of \"\n    \"rangīn + kamān ‘bow’. The Hāfez line quoted in the box is the one Borhan-e Qāte‘ itself cites at \"\n    \"رنگ.\"),\n  \"derivation_fa\": (\n    \"«رنگ» فارسی نو دنبالهٔ بی‌تغییرِ rang فارسی میانه است (خوشهٔ پایانی ‑ng در فارسی نو می‌ماند، مانند \"\n    \"تنگ و سنگ). ساخته‌های داخل کادر همه زایشی و روشن‌اند: آب‌رنگ (آب + رنگ)، رنگرز (رنگ + رز، \"\n    \"ستاک حال رزیدن؛ همان‌گونه که معین در حاشیهٔ برهان قاطع می‌نویسد: «از: رنگ + رز (رزیدن)»)، \"\n    \"رنگ‌آمیزی؛ «رنگارنگ» ساخت تکراری X‑ا‑X فارسی است (مانند گوناگون، سراسر) و «رنگین‌کمان» \"\n    \"واژه‌ای مرکّب از رنگین + کمان است. بیت حافظ همان است که در مدخل «رنگ» برهان قاطع آمده. \"\n    \"ادعای نورایی دربارهٔ این گره درست است.\"),\n  \"sources\": [W_RANG],\n  \"ref_check\": [\n    {\"ref\": \"MON:1677\", \"status\": \"not_checked\", \"note\": (\"The print volumes of Mo‘in are not on disk with their pagination; the online text (vajehyab / \"\n        \"abadis, فرهنگ معین) carries the entry رنگ with the senses Nourai gives but no page number, so the \"\n        \"citation itself could not be verified. Content-wise Mo‘in’s رنگ agrees.\")}\n  ],\n  \"consulted\": [\n    {\"src\": \"BQT\", \"where\": \"Borhan-e Qāte‘, رنگ (BQT_v2_pages.txt leaf 426)\", \"stance\": \"supports\", \"note\": \"The entry gives رنگ = «لون» with the Hāfez line Nourai quotes, and Mo‘in’s footnote on رنگرز: ‘از: رنگ + رز (رزیدن)’.\"},\n    {\"src\": \"HRN\", \"where\": \"no.623, p.138 f.\", \"stance\": \"supports\", \"note\": \"‘(1)reng ‚Farbe‘ … LW. kurd. renk, reng; afɣ. rang; bel. rang’ — NP rang is the source of the neighbouring languages’ words.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"p.314\", \"stance\": \"supports\", \"note\": \"‘NWIR: … NP rang “colour”’ under *ra(n)j.\"},\n    {\"src\": \"ARY\", \"where\": \"Aryanpur, فرهنگ ریشه‌های هند و اروپایی\", \"stance\": \"silent\", \"note\": \"grep of رنگ in ARY_pages.txt and of ‘rang’ in ARY_latin_index_pages.txt produced no usable headword entry for رنگ in this OCR.\"}\n  ]\n})\n\nN.append({\n  \"id\": 4,\n  \"lang\": \"Persian\",\n  \"words\": \"rajîdan\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"The etymological claim is right, though the headword form deserves a note. The Iranian verb is \"\n    \"رزیدن razīdan ‘to dye, to colour’ (pres. stem raz-), the direct continuation of Proto-Iranian \"\n    \"*ra(n)j ‘to colour, dye’ < PIE *(s)reg- (Cheung 2007: 314, ‘NP razīdan “to colour, dye, taint, \"\n    \"tinge”’); Mann, IEC p.1065 s.v. regio ‘dye, tinge’ cites precisely ‘Per. razam, v. “dye, tinge”’ \"\n    \"beside Skt. rājyāmi and Gk. rhézō — exactly the arrow Nourai draws from the root. Old Iranian \"\n    \"*ra(n)j- lost its nasal in the plain verb stem (MP raz- : rang from the nasal-infixed noun), and \"\n    \"-īdan is the ordinary New Persian infinitive suffix. رنگرز rangraz ‘dyer’, which Nourai puts in \"\n    \"the box, is rang + raz-, the same stem. The headword رجیدن rajīdan is itself attested — Dehkhodā \"\n    \"and Mo‘in both give رجیدن ‘رنگ کردن، لکه کردن’ with the cross-reference ‘رجوع به رزیدن’ — so \"\n    \"it is a lexicographers’ variant of razīdan (ز / ج graphic-phonetic variation), not a misprint; \"\n    \"razīdan is the primary form and the one the sources derive.\"),\n  \"derivation_fa\": (\n    \"ادعا درست است. فعل اصلی «رزیدن» (ستاک حال: رز‑) است که بازماندهٔ ریشهٔ ایرانی آغازین *ra(n)j \"\n    \"«رنگ کردن» است؛ چونگ (۲۰۰۷، ۳۱۴) و مان (فرهنگ تطبیقی هندواروپایی، ص ۱۰۶۵) هر دو همین فعل \"\n    \"را کنار rajyati سنسکریت و ῥέζω یونانی می‌نشانند. نونِ میانجی در ستاک فعل افتاده (raz‑) ولی در اسم \"\n    \"مانده (rang). صورت «رجیدن» نیز ساختگی نیست: دهخدا و معین آن را به معنای «رنگ کردن، لکه کردن» \"\n    \"با ارجاع «رجوع به رزیدن» آورده‌اند؛ پس دگرگونی ز/ج و گونهٔ فرعی است، نه خطای چاپی.\"),\n  \"sources\": [A_RAJ, A_RAZ],\n  \"ref_check\": [\n    {\"ref\": \"IEC:1065\", \"status\": \"supports\", \"note\": IEC_NOTE},\n    {\"ref\": \"MON:1640\", \"status\": \"not_checked\", \"note\": \"Mo‘in’s printed pagination is not available on disk; the online فرهنگ معین text via abadis.ir does carry رجیدن ‘رنگ کردن، لکه کردن — رجوع به رزیدن’, i.e. the word and gloss Nourai gives, but the page number could not be checked.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"CHEUNG\", \"where\": \"p.314 s.v. *ra(n)j\", \"stance\": \"supports\", \"note\": \"‘NWIR: NP razidan “to colour, dye, taint, tinge”, NP rang “colour” … PIE *(s)reg- … Pok.: 854.’\"},\n    {\"src\": \"BQT\", \"where\": \"رنگرز footnote (BQT_v2_pages.txt leaf 426)\", \"stance\": \"supports\", \"note\": \"Mo‘in’s footnote ‘* رنگرز … از: رنگ + رز (رزیدن)’ identifies رز as the present stem of رزیدن ‘to dye’.\"},\n    {\"src\": \"HRN\", \"where\": \"Grundriss, r- section\", \"stance\": \"silent\", \"note\": \"Horn has no entry for razīdan/rajīdan; grep of ‘razid’/‘rajid’ in HRN.txt returns nothing.\"},\n    {\"src\": \"MON\", \"where\": \"فرهنگ معین s.v. رجیدن / رزیدن (abadis.ir)\", \"stance\": \"supports\", \"note\": \"رجیدن: ‘رنگ کردن، لکه کردن — رجوع به رزیدن’; رزیدن: ‘رنگ کردن، رنگرزی کردن’.\"}\n  ]\n})\n\nN.append({\n  \"id\": 5,\n  \"lang\": \"Sanskrit\",\n  \"words\": \"râkšâ, lâkša; lac\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\n    \"Skt. lākṣā f. ‘lac, the red resinous incrustation left on trees by Kerria lacca / Coccus lacca, \"\n    \"and the red dye made from it’ is old and real; the form *rākṣā that Nourai puts first is the \"\n    \"reconstructed earlier shape, with the regular Indo-Aryan r- > l- change, and is exactly what \"\n    \"Watkins prints: ‘reg-3. To dye … 3. Perhaps Sanskrit rākshā, earlier form of lākshā, red dye: \"\n    \"LAC’ (AHD appendix). Hobson-Jobson s.v. LAC likewise: ‘Hind. lākh, from Skt. lakshā, for rākshā’, \"\n    \"and Skeat s.v. Lac(1) derives lākṣā from rakta, pp. of rañj- ‘to dye, colour, redden’. But the \"\n    \"word is tentative even in the sources that print it (‘Perhaps’, ‘for rākshā’): Mayrhofer EWAia \"\n    \"II 477 calls the etymology uncertain and lists three rivals — *lakṣa/*rakṣa ‘red(ness)’ to rañj-, \"\n    \"a PIE *laḱs- ‘salmon’ colour-word, and derivation from lakṣá- ‘100,000’. That third one is what \"\n    \"Klein and Lokotsch adopt (‘named from the 100,000 insects’), and it is a folk-etymological \"\n    \"conflation of two different words. The second item in Nourai’s box, ‘lac’, is not a Sanskrit \"\n    \"word at all: it is the English/Medieval Latin form of the resin name, and the gloss ‘an insect \"\n    \"with red eyes, a swarm of such insects, a large number (100,000)’ belongs to Skt. lakṣá- \"\n    \"‘mark, stake; 100,000’, a separate lemma. Nourai’s own NOTE (POK:32, KLN:47,856 = root ‘Alek’ \"\n    \"‘to protect’) records the rival derivation via rakṣ- ‘to protect’ correctly.\"),\n  \"derivation_fa\": (\n    \"واژهٔ سنسکریت lākṣā «لاک، صمغ و رنگ سرخ» اصیل است و صورت کهن‌ترِ بازساختیِ آن *rākṣā است \"\n    \"(تبدیل قاعده‌مند r > l در هندوآریایی). واتکینز در پیوست AHD می‌نویسد: «شاید سنسکریت rākṣā، \"\n    \"صورت کهن‌تر lākṣā، رنگ سرخ»؛ هابسن‑جابسن و اسکیت نیز همین را می‌گویند. اما مایرهوفر \"\n    \"(EWAia II ۴۷۷) ریشه را نامطمئن می‌داند و سه فرضیه می‌آورد. نکتهٔ مهم: آنچه نورایی در کادر \"\n    \"به نام «سنسکریت lac» آورده اصلاً سنسکریت نیست و معنای «صدهزار» از آنِ واژهٔ دیگری است: \"\n    \"lakṣá- «نشانه، صدهزار». این دو واژه را کلاین و لوکوچ یکی گرفته‌اند که ریشه‌شناسی عامیانه است. \"\n    \"پس ادعای نورایی با احتیاط پذیرفتنی است.\"),\n  \"sources\": [W_LAKSA, E_LAC],\n  \"ref_check\": [\n    {\"ref\": \"OEW:333\", \"status\": \"not_checked\", \"note\": \"Shipley, The Origins of English Words (1984) is lending-only on archive.org (djvu.txt returns 401) and is not on disk; p.333 could not be read.\"},\n    {\"ref\": \"AHD:1536\", \"status\": \"supports\", \"note\": AHD_NOTE + \" Page 1536 falls inside the 1975 New College appendix (pp.1505–1550), where the r- roots stand.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"p.854 s.v. reĝ-; p.32 s.v. alek-\", \"stance\": \"partial\", \"note\": \"Pokorny’s reĝ- p.854 lists no lākṣā at all (only rajyati, rāga-, Gk. ῥέζω); p.32 has alek- ‘abwehren, schützen’ with Skt. rákṣati, which is the rival derivation Nourai’s NOTE refers to. So POK supports neither the lac link nor contradicts it — it simply does not make it.\"},\n    {\"src\": \"KLN\", \"where\": \"1966 ed. pp.857 f. (leaf 462) s.vv. ‘lac, lakh’ and ‘lac (red resinous substance)’\", \"stance\": \"contradicts\", \"note\": \"Klein: ‘lac, n., a red resinous substance. — Pers. lak, fr. Hind. lakh, fr. OI. lakṣā, lit. “one hundred thousand” … a name given to the insects Coccus ilicis, in allusion to their great number’, and under ‘lac, lakh’ he refers OI. lākṣa to rakṣati ‘protects’ and Gk. ἀλέξειν. Klein therefore takes the ‘100,000’ word as primary, not the dye word.\"},\n    {\"src\": \"SKT\", \"where\": \"Concise Etym. Dict. p.238 (SKT.txt leaf 259) s.v. Lac (1)\", \"stance\": \"supports\", \"note\": \"‘Lac (1), a resinous substance. (Pers.—Skt.) … Skt. lākṣā, lac; put for rakṣā, lac. — Skt. rakta, pp. of rañj, to dye, colour, redden; raṅga, colour, paint.’ Skeat derives the lac word from the ‘dye’ root, as Nourai does.\"},\n    {\"src\": \"HJB\", \"where\": \"Hobson-Jobson pp.499–500 s.v. LAC\", \"stance\": \"supports\", \"note\": \"‘LAC, s. Hind. lākh, from Skt. lakshā, for rākshā.’\"},\n    {\"src\": \"LKT\", \"where\": \"Lokotsch no.1295 (LKT.txt leaf 131, printed ≈104)\", \"stance\": \"contradicts\", \"note\": \"‘Sskr. lāksā: „Marke, Fleck; hunderttausend“, [und nach den 100000 … Insekten Coccus ilicis …] „Lack“’ — Lokotsch too starts from the ‘mark / 100,000’ sense.\"}\n  ]\n})\n\nN.append({\n  \"id\": 6,\n  \"lang\": \"Persian\",\n  \"words\": \"lâk\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"Persian لاک lāk ‘lac, the red resin and the lacquer made from it’ is a loan out of India: Skt. \"\n    \"lākṣā > Middle Indic (Prakrit) lakkhā > NP lāk, the Prakrit geminate -kkh- being simplified and \"\n    \"the vowel lengthened in Persian (Wiktionary s.v. لاک, Etymology 2: ‘Borrowed from Prakrit \"\n    \"*lakkhā, from Sanskrit लाक्षा (lākṣā)’). Mo‘in says the same in his footnote to the Borhan \"\n    \"entry (BQT p.1878, n.11): ‘لاک … در یونانی lakka، فرانسوی laque، از هندی متوسط lakkha گرفته شده’. \"\n    \"The trade route is the one Hobson-Jobson documents: lac reached the Iranian world and the \"\n    \"Mediterranean from Bengal, Pegu and the Deccan (already in the Periplus, 1st c. CE, and \"\n    \"Aelian c. 250 CE describes the red-dyeing insect, adding that the cloth was carried ‘to the \"\n    \"King of Persia’). Arabic then took the word over from Persian as lakk (Addi Shir, AFM p.≈136: \"\n    \"‘(اللك) صبغ … تعریب لك’; Asbaghi, PLA p.240 ‘lakiyya … hindustan >> pers. لاک > ar.’). \"\n    \"— Note that Persian also has a homonymous native لاک ‘wooden trough; tortoise shell’ (< OIr. \"\n    \"*nāwaka-), unrelated to this one.\"),\n  \"derivation_fa\": (\n    \"«لاک» فارسی به معنای صمغ و رنگ سرخ وام‌واژه‌ای هندی است: از سنسکریت lākṣā از راه هندی میانه \"\n    \"(پراکریت) lakkhā، که همخوانِ مشدّد آن در فارسی ساده شده و واکه کشیده شده است. معین در حاشیهٔ \"\n    \"برهان قاطع (ص ۱۸۷۸، پانوشت ۱۱) همین را می‌نویسد: «لاک … در یونانی lakka، فرانسوی laque، \"\n    \"از هندی متوسط lakkha گرفته شده». سپس عربی آن را از فارسی به صورت «لکّ» معرّب کرد (ادی شیر). \"\n    \"توجه شود که «لاک» دیگری هم در فارسی هست (کاسهٔ چوبی، لاک پشت) که ریشه‌اش جداست. ادعای \"\n    \"نورایی درست است.\"),\n  \"sources\": [W_LAK, E_LAC],\n  \"ref_check\": [\n    {\"ref\": \"KLN:856\", \"status\": \"supports\", \"note\": \"Klein 1966 (leaf 462, the ‘lac’ opening, pp.857 f.; vol. II begins at p.855 with L, so Nourai’s ‘856’ lands on this entry): ‘lac, n., a red resinous substance. — Pers. lak, fr. Hind. lakh, fr. OI. lakṣā … Cp. lacquer and the second element in shellac.’ Klein confirms the Persian word and its Indian source (though he puts the ‘100,000’ sense first).\"},\n    {\"ref\": \"BQT:1878\", \"status\": \"supports\", \"note\": \"BQT_v3_picofile.pdf pdf page 675 = printed 1878 (tools/ref_page.py BQT:1878): ‘لاک … و نام رنگی است مشهور که در هندوستان بهم می‌رسد و بدان چیزها رنگ کنند و آن شبنمی باشد که بر شاخهای درخت کنار … نشیند و منجمد گردد … از آن رنگ سرخی حاصل گردد’, with Mo‘in’s footnote 11 on the Middle Indic source. The page also carries the ‘Onṣorī line Nourai quotes.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"HJB\", \"where\": \"Hobson-Jobson pp.499–500 s.v. LAC\", \"stance\": \"supports\", \"note\": \"‘Though lāk bears the same sense in Persian, and lak or lukk are used in modern Arabic for sealing-wax … The English word lake for a certain red colour is from this. So also are lacquer and lackered ware.’\"},\n    {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen, printed p.240 (PLA_pages.txt leaf 255)\", \"stance\": \"supports\", \"note\": \"‘lakiyya: „Lack, Flüssigkeit, die an der Luft … zu einem festhaltenden Schutzfilm wird“ hindustan >> pers. لاک > ar.’ — the Indian > Persian > Arabic route.\"},\n    {\"src\": \"AFM\", \"where\": \"Addi Shir, printed ≈p.136 (AFM_pages.txt leaf 144)\", \"stance\": \"supports\", \"note\": \"‘( اللك ) صبغ … يصبغ به جلود المعزى تعريب لك’ — Arabic lakk ‘a dye used on goatskins’ is arabised Persian lak.\"},\n    {\"src\": \"WEB\", \"where\": \"Webster’s New Twentieth Century Dict. s.v. lac\", \"stance\": \"partial\", \"note\": \"‘lac, n. [Hind. lākh; Sans. lakshā] a resinous substance deposited upon certain trees in southern Asia …’ — same origin, Persian step omitted.\"}\n  ]\n})\n\nN.append({\n  \"id\": 7,\n  \"lang\": \"Portuguese\",\n  \"words\": \"\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"The empty pass-through box is the Portuguese stage of the word. Portuguese traders in the \"\n    \"Indies from c.1500 brought both laca ‘gum lac’ and its derivative lacre ‘sealing-wax, lacquer’ \"\n    \"(Correa 1519 already writes alacre of lac bought on the Coromandel coast — Hobson-Jobson \"\n    \"p.500). Klein s.v. lacquer: ‘MF. lacre, fr. Port. lacre, “sealing wax”, fr. laca, “gum lac”, \"\n    \"which derives fr. Hind. lakh, “lac”’; Skeat s.v. Lacquer: ‘Port. lacre, sealing-wax. — Port. \"\n    \"laca, gum lac’. The -re of lacre is the usual Portuguese reshaping of the noun.\"),\n  \"derivation_fa\": (\n    \"کادر خالی، مرحلهٔ پرتغالی زنجیره است. بازرگانان پرتغالی از سدهٔ دهم هجری/شانزدهم میلادی واژهٔ \"\n    \"laca «صمغ لاک» و مشتقّ آن lacre «موم مهر، لاک الکلی» را از هند و خلیج فارس به اروپا بردند؛ \"\n    \"کلاین و اسکیت همین مسیر را می‌دهند. ادعای نورایی درست است.\"),\n  \"sources\": [E_LAC],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the book (refs=None); checked against Klein and Skeat instead.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"1966 ed. leaf 462 s.v. lacquer\", \"stance\": \"supports\", \"note\": \"‘MF. lacre, fr. Port. lacre, “sealing wax”, fr. laca, “gum lac” …’\"},\n    {\"src\": \"SKT\", \"where\": \"Concise Etym. Dict. p.238 s.v. Lacquer\", \"stance\": \"supports\", \"note\": \"‘Lacquer, lacker, a sort of varnish. (F.—Port.—Pers.—Skt.) F. lacre (Cot.) — Port. lacre, sealing-wax. — Port. laca, gum-lac … Pers. lāk, gum lac (above).’\"},\n    {\"src\": \"LKT\", \"where\": \"Lokotsch no.1295\", \"stance\": \"partial\", \"note\": \"‘sp. pg. laca „Lack“, lacre „Siegellack“, frz. laque „Lack“, it. lacca …’ — Lokotsch lists the Iberian forms but takes them straight from Indic, without a Persian stage.\"}\n  ]\n})\n\nN.append({\n  \"id\": 8,\n  \"lang\": \"French\",\n  \"words\": \"\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"The French stage. Middle French borrowed the Portuguese word twice: lacre ‘sealing-wax, \"\n    \"lacquer’ (16th c., the form Cotgrave 1611 registers as lacre) and laque ‘lac, lake pigment’. \"\n    \"Klein: ‘lacquer … MF. lacre, fr. Port. lacre’; Skeat: ‘F. lacre (Cot.) — Port. lacre’; Lokotsch \"\n    \"no.1295 lists ‘frz. laque „Lack“’ in the same family. English then took lacquer/lacker from the \"\n    \"French form, with -er for -re as in sepulchre/sepulcher, meagre/meager.\"),\n  \"derivation_fa\": (\n    \"مرحلهٔ فرانسوی. فرانسوی میانه دو صورت را از پرتغالی وام گرفت: lacre «موم مهر، لاک» (که کوت‌گریو \"\n    \"در ۱۶۱۱ ضبط کرده) و laque «لاک، رنگ لاک». انگلیسی صورت نخست را گرفت و ‑re را به ‑er بدل کرد. \"\n    \"ادعای نورایی درست است.\"),\n  \"sources\": [E_LAC],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference given in the book for this node (refs=None); checked against Klein, Skeat and Lokotsch.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"1966 ed. leaf 462 s.v. lacquer\", \"stance\": \"supports\", \"note\": \"‘lacquer, lacker, n., a kind of varnish. — MF. lacre, fr. Port. lacre …’\"},\n    {\"src\": \"SKT\", \"where\": \"p.238 s.v. Lacquer and Lake (2)\", \"stance\": \"supports\", \"note\": \"‘F. lacre (Cot.)’ for lacquer; and ‘Lake (2), a crimson colour. (F.—Pers.) F. laque (Cot.) — Pers. lāk, lake.’\"},\n    {\"src\": \"DEV\", \"where\": \"Devic, Dict. étym. des mots français d’origine orientale\", \"stance\": \"partial\", \"note\": \"Lokotsch no.1295 cites ‘Devic DEt 150/151’ for laque; the local DEV.txt OCR of those pages is too corrupt to quote verbatim, but the reference is to the same Indian origin.\"}\n  ]\n})\n\nN.append({\n  \"id\": 9,\n  \"lang\": \"English\",\n  \"words\": \"lacquer, Shellac\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\n    \"lacquer (also lacker, from the 1590s) is exactly as drawn: MF lacre < Port. lacre < laca < \"\n    \"Hind. lakh / Pers. lāk < Skt. lākṣā (Klein s.v. lacquer; Skeat ‘Lacquer … (F.—Port.—Pers.—Skt.)’). \"\n    \"shellac, however, does not come through Portuguese and French at all: it is an English compound \"\n    \"of shell + lac (1713), translating the trade term ‘shell-lac’, the lac purified and dried in thin \"\n    \"flakes or ‘shells’, beside stick-lac and seed-lac — Skeat lists it as a derivative of his Lac (1) \"\n    \"(‘Der. gum-lac, shell-lac’), Webster explains ‘when strained through a cloth and dried it \"\n    \"constitutes shell-lac, or the shellac of commerce’, and Lokotsch no.1295 glosses ‘engl. shellac \"\n    \"[eigentlich „Schalenlack“, da er zu kleinen, dünnen Täfelchen geformt wird]’. So the second word \"\n    \"in the box hangs off node 6 (lac) directly, not off the French node.\"),\n  \"derivation_fa\": (\n    \"واژهٔ lacquer دقیقاً همان مسیر نمودار را طی کرده است: فرانسوی میانه lacre < پرتغالی lacre < laca \"\n    \"< فارسی لاک < سنسکریت lākṣā. اما shellac از راه فرانسه نیامده؛ ترکیبی انگلیسی از shell \"\n    \"(«پوسته، ورقه») + lac است (۱۷۱۳ م.) و به لاکی گفته می‌شد که به صورت ورقه‌های نازک خشک می‌شد. \"\n    \"پس این واژه مستقیماً به گرهِ «لاک» وابسته است نه به گره فرانسوی؛ ادعای نورایی دربارهٔ \"\n    \"lacquer درست و دربارهٔ shellac با احتیاط پذیرفتنی است.\"),\n  \"sources\": [E_LAC],\n  \"ref_check\": [\n    {\"ref\": \"SKT:281\", \"status\": \"partial\", \"note\": \"Skeat has the entries Nourai needs — ‘Lacquer, lacker, a sort of varnish. (F.—Port.—Pers.—Skt.)’ and ‘Lac (1) … Der. gum-lac, shell-lac’ — but in the 1911 Concise (the copy on disk) they stand on p.238 (SKT.txt leaf 259), not p.281; leaf 302 = printed 281 is in the M- words (mask…, medicus). Content supports the arrow, the page number does not match this edition.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"1966 ed. leaf 462 s.v. lacquer; s.v. shellac\", \"stance\": \"supports\", \"note\": \"‘lacquer … MF. lacre, fr. Port. lacre … fr. Hind. lakh, “lac”, fr. OI. lakṣā. See lac, “a resinous substance”’, with ‘Cp. … the second element in shellac’ at lac.\"},\n    {\"src\": \"WEB\", \"where\": \"Webster’s New Twentieth Century Dict. s.vv. lac, lacquer\", \"stance\": \"supports\", \"note\": \"‘lacquer … [Fr. lacre … from laca … from Per. lak, lac]’; and at lac: ‘when strained through a cloth and dried it constitutes shell-lac, or the shellac of commerce.’\"},\n    {\"src\": \"LKT\", \"where\": \"Lokotsch no.1295\", \"stance\": \"supports\", \"note\": \"‘engl. lac, ndl. lak, dtsch. Lack und engl. shellac [eigentlich „Schalenlack“, da er zu kleinen, dünnen Täfelchen geformt wird], ndl. schellak, dtsch. Schellack.’\"},\n    {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard Dict.\", \"stance\": \"silent\", \"note\": \"grep of ‘shellac’ in FSD_vol1–4 finds only the compound ‘Sealing-wax … a mixture, as of shellac and turpentine’ (vol.4 l.5301), no etymological entry.\"}\n  ]\n})\n\nN.append({\n  \"id\": 10,\n  \"lang\": \"Persian\",\n  \"words\": \"lak\",\n  \"verdict\": \"disputed\",\n  \"derivation\": (\n    \"The Persian word is real — Borhan-e Qāte‘ p.1900 opens the لک entry with ‘لک … صدهزار باشد … \"\n    \"عدد هرچیز که صد هزار رسید آنرا لک خوانند’ and quotes the very ‘Onṣorī line Nourai prints \"\n    \"(«دو لک ز لشکر او شد بزیر خاک نهان»). But it does not belong to this root. Mo‘in’s footnote \"\n    \"on that same page says plainly ‘هندی است «غیاث»، در هندوستانی لاک، از سانسکریت’, and Klein \"\n    \"s.v. ‘lac, lakh’ has ‘Pers. lak, fr. Hind. lakh, ult. fr. OI. lākṣa, “one hundred thousand”, prop. \"\n    \"“sign, mark”, rel. to lakṣati, lakṣayati, “marks”, and prob. also to rákṣā … rakṣati “protects”, \"\n    \"and cogn. with Gk. ἀλέξειν “to ward off”. See Alexander’. So NP لک is a mediaeval loan from Indic \"\n    \"lakṣá- / Hindi lākh ‘100,000’, a word Watkins does NOT put under reg-3 (his reg-3 lists only rāga- \"\n    \"and lākṣā ‘red dye’), and whose own etymology is uncertain — the ‘mark’ sense points to lakṣ- \"\n    \"‘to mark’ or to alek- ‘to protect’ (Pok. 32), exactly the alternative Nourai’s NOTE concedes. \"\n    \"Attaching لک ‘hundred thousand’ to the root ‘to dye’ rests on the old conflation of the two \"\n    \"Sanskrit words, which Mayrhofer (EWAia II 477) treats as unproven.\"),\n  \"derivation_fa\": (\n    \"واژهٔ فارسی «لک» به معنای صدهزار واقعی است و برهان قاطع (ص ۱۹۰۰) همان بیت عنصری را می‌آورد \"\n    \"که نورایی نقل کرده؛ اما این واژه به این ریشه تعلق ندارد. معین در همان صفحه در پانوشت \"\n    \"می‌نویسد: «هندی است … در هندوستانی لاک، از سانسکریت»، و کلاین نیز فارسی lak را از هندی \"\n    \"lākh و آن را از سنسکریت lakṣa «صدهزار، در اصل نشانه» می‌داند که با rakṣati «پاسداری \"\n    \"کردن» و یونانی ἀλέξειν پیوند دارد (ریشهٔ Alek، پوکورنی ۳۲). پژوهش امروزی این انتساب \"\n    \"را رد می‌کند: «لک» وام‌واژه‌ای هندی است و یکی گرفتن آن با lākṣā «لاک» ریشه‌شناسی \"\n    \"عامیانه است.\"),\n  \"sources\": [E_LAC, W_LAKSA],\n  \"ref_check\": [\n    {\"ref\": \"KLN:856\", \"status\": \"contradicts\", \"note\": \"Klein 1966 (leaf 462): ‘lac, lakh, n., 1) one hundred thousand; 2) a great number. — Pers. lak, fr. Hind. lakh, ult. fr. OI. lākṣa, “one hundred thousand”, prop. “sign, mark”, rel. to lakṣati, lakṣayati, “marks, characterizes, defines”, and prob. also to rákṣā … rakṣati, “protects” … and cogn. with Gk. ἀλέξειν, … See Alexander.’ Klein’s route for لک is Indic, and his root is Alek-, not reg- ‘to dye’.\"},\n    {\"ref\": \"BQT:1900\", \"status\": \"partial\", \"note\": \"tools/ref_page.py BQT:1900 (BQT_v3 pdf page 697) gives the لک entry: ‘لک – بفتح اول وسکون ثانی، صدهزار باشد … آنرا لک خوانند’ with the ‘Onṣorī verse Nourai quotes; but Mo‘in’s footnote 4 there says ‘هندی است «غیاث»، در هندوستانی لاک، از سانسکریت’, i.e. an Indic loan, not an inherited Iranian word.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins s.v. reg-3\", \"stance\": \"contradicts\", \"note\": \"Watkins puts only ‘Sanskrit rāgaḥ, color, red’ and ‘Perhaps Sanskrit rākshā … red dye: LAC1’ under reg-3; the numeral word lakh is not there.\"},\n    {\"src\": \"POK\", \"where\": \"p.32 s.v. alek-\", \"stance\": \"partial\", \"note\": \"POK_full.txt, Root/lemma alek- ‘abwehren, schützen’, Page(s): 32 — the root under which Klein files lākṣa/rakṣati; Nourai’s own NOTE points here.\"},\n    {\"src\": \"LKT\", \"where\": \"Lokotsch no.1295\", \"stance\": \"contradicts\", \"note\": \"‘hieraus in der ursprünglichen Bedeutung hind. lākh „100000“, engl. lack „dass., bes. 100000 Rupien“’ — the numeral sense is the original Indic one and spreads from India, not from Iran.\"},\n    {\"src\": \"HJB\", \"where\": \"Hobson-Jobson s.v. LACK, LAKH (p.500)\", \"stance\": \"contradicts\", \"note\": \"Hobson-Jobson treats lakh ‘100,000’ as Hind. lākh from Skt. lakṣa, an Indian numeral term taken into Anglo-Indian usage.\"}\n  ]\n})\n\nN.append({\n  \"id\": 11,\n  \"lang\": \"Arabic\",\n  \"words\": \"lajj\",\n  \"verdict\": \"disputed\",\n  \"derivation\": (\n    \"Two different Arabic words are merged in this box. (a) لَجّ lajj ‘an enormous quantity, a great \"\n    \"crowd’: Asbaghi, Persische Lehnwörter im Arabischen p.240, does list it as a Persian loan — \"\n    \"‘lağğ: „ungeheure Menge“ pers. لک lak „tausend“’ — so for this sense Nourai has a modern \"\n    \"supporter, the Persian numeral لک being arabised with the doubled final consonant normal in \"\n    \"Arabic monosyllables (cf. لکّ lakk ‘lac’ from the same Persian word in its other sense). \"\n    \"(b) لُجّة lujja ‘the deep of the sea, deep water’, which is what Nourai’s second gloss and the \"\n    \"next node actually rest on, is native Arabic: it belongs to the sound root ل-ج-ج (لَجّ lajja \"\n    \"‘to persist, be importunate’, لَجّة lajja ‘the clamour of a crowd’, لُجّي lujjī ‘of the deep’), it \"\n    \"is Qur’ānic (Q 27:44 حَسِبَتْهُ لُجَّةً; Q 24:40 بَحْرٍ لُجّيٍّ), and Jeffery’s Foreign Vocabulary of \"\n    \"the Qur’ān does not list it among the loanwords. Addi Shir, whom Nourai cites, has no لجّ entry \"\n    \"at all — his ل section has اللك ‘lac dye, arabised lak’ and اللجام ‘bridle, arabised lagām’, nothing \"\n    \"else. The ‘deepest point of sea’ half of the box is therefore not derivable from Persian lak.\"),\n  \"derivation_fa\": (\n    \"در این کادر دو واژهٔ عربی یکی شده‌اند. نخست «لَجّ» به معنای انبوهی و شمار بسیار؛ اصباغی در \"\n    \"وام‌واژه‌های فارسی در عربی (ص ۲۴۰) آن را وام‌گرفته از «لک» فارسی می‌داند؛ پس این نیمهٔ \"\n    \"ادعا پشتیبان امروزی دارد. ولی «لُجّة» به معنای «ژرفای دریا» عربی اصیل است و از ریشهٔ سالم \"\n    \"ل‑ج‑ج (لَجّ «پافشاری کردن»، لَجّة «هیاهوی جمعیت») می‌آید، در قرآن آمده (نمل ۴۴؛ نور ۴۰) و \"\n    \"جفری در واژگان بیگانهٔ قرآن آن را وام‌واژه نمی‌شمارد. ادی شیر هم که نورایی بدو استناد کرده \"\n    \"اصلاً مدخل «لجّ» ندارد. پس نیمهٔ دوم ادعا را پژوهش امروزی رد می‌کند.\"),\n  \"sources\": [A_LOJ],\n  \"ref_check\": [\n    {\"ref\": \"AFM:141\", \"status\": \"not_found\", \"note\": \"Addi Shir has no لجّ entry. AFM_pages.txt leaf 149 (≈ printed p.141) is already in the م- words (مانیذ، مهر، مرونة، متراس); the ل- section on leaf 144 (≈ p.136) has ‘( اللك ) صبغ … تعريب لك’ and ‘( اللجام ) تعريب لگام’, nothing on lajj. Grepping the whole AFM text for اللج / لجة returns only اللجام.\"},\n    {\"ref\": \"FVF:613\", \"status\": \"not_checked\", \"note\": \"Emam Shushtari, فرهنگ واژه‌های فارسی در زبان عربی, is not on archive.org and has no local copy; the noorlib scan needs a browser session, so p.613 could not be read.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PLA\", \"where\": \"Asbaghi 1988, printed p.240 (PLA_pages.txt leaf 255)\", \"stance\": \"supports\", \"note\": \"‘lağğ: „ungeheure Menge“ pers. لک lak „tausend“’ — the only modern authority that backs Nourai’s arrow, and only for the ‘great number’ sense.\"},\n    {\"src\": \"FVQ\", \"where\": \"Jeffery, The Foreign Vocabulary of the Qur’ān\", \"stance\": \"silent\", \"note\": \"grep of ‘lujj’ / ‘Lujja’ in FVQ.txt and FVQ_pages.txt returns nothing: Jeffery does not treat Qur’ānic لُجّة (27:44) / لُجّيّ (24:40) as a foreign word.\"},\n    {\"src\": \"AFA\", \"where\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen\", \"stance\": \"silent\", \"note\": \"grep of لجة in AFA.txt returns nothing — Fraenkel does not claim the word for Aramaic either, consistent with a native Arabic root.\"},\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. ‘lac, lakh’\", \"stance\": \"silent\", \"note\": \"Klein records the Persian > Hindi > Sanskrit chain for lak but knows nothing of an Arabic lajj derived from it.\"}\n  ]\n})\n\nN.append({\n  \"id\": 12,\n  \"lang\": \"Persian\",\n  \"words\": \"lojjeh\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\n    \"The step actually drawn here — Arabic > Persian — is right: لُجّه lojje ‘the deep of the sea’ is \"\n    \"an Arabic loanword in Persian, and Mo‘in tags it accordingly, ‘[ع.] (لُ جَّ) میانهٔ دریا’, as does \"\n    \"Dehkhodā ‘[ع اِ] میانه آب دریا’; it is a literary Arabism of the classical poets, the Sa‘dī line \"\n    \"Nourai quotes being the standard citation. It entered Persian with the whole Qur’ānic-Arabic \"\n    \"vocabulary after the 3rd/9th century, keeping the Arabic gemination and taking the Persian \"\n    \"final -e of the Arabic tā’ marbūṭa. What is not supportable is the round trip implied by the \"\n    \"chart (Persian lak > Arabic lajj > Persian lojje): the Arabic word Persian borrowed is لُجّة \"\n    \"‘deep water’ of the native root ل-ج-ج (see node 11), not Asbaghi’s لَجّ ‘huge number’. Nourai’s own \"\n    \"NOTE again offers ‘Alek’ as an alternative root.\"),\n  \"derivation_fa\": (\n    \"گامی که در این گره رسم شده — عربی > فارسی — درست است: «لُجّه» معرّب نیست بلکه وام‌واژه‌ای عربی \"\n    \"در فارسی است و معین آن را با نشانهٔ [ع.] «میانهٔ دریا» آورده است؛ از راه ادب عربی و قرآنی \"\n    \"پس از سدهٔ سوم هجری به فارسی راه یافته و تاء مربوطهٔ آن در فارسی به هٔ غیرملفوظ بدل شده است. \"\n    \"اما چرخهٔ دورانیِ مورد ادعای نورایی (لک فارسی < لجّ عربی < لجّهٔ فارسی) پذیرفتنی نیست؛ \"\n    \"واژه‌ای که فارسی وام گرفته همان لُجّةِ ریشهٔ سالم عربی است.\"),\n  \"sources\": [A_LOJ],\n  \"ref_check\": [\n    {\"ref\": \"MON:3569\", \"status\": \"partial\", \"note\": \"The printed Mo‘in pagination is unavailable, but the فرهنگ معین text (abadis.ir s.v. لجه) gives ‘[ع .] (لُ جَّ) میانة دریا’ — the word and gloss Nourai prints, expressly marked Arabic, which is what his chart needs at this node but not what it claims about the Arabic word’s own origin.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"فرهنگ معین s.v. لجه (abadis.ir)\", \"stance\": \"supports\", \"note\": \"‘[ع .] (لُ جَّ) میانة دریا’ — Arabic tag confirmed; Dehkhodā on the same page: ‘[ع اِ] میانه آب دریا’.\"},\n    {\"src\": \"FVQ\", \"where\": \"Jeffery\", \"stance\": \"silent\", \"note\": \"لُجّة is Qur’ānic (27:44) yet absent from Jeffery’s list of foreign words — evidence that the Arabic source word is native.\"},\n    {\"src\": \"PLA\", \"where\": \"Asbaghi p.240\", \"stance\": \"partial\", \"note\": \"Asbaghi lists لجّ ‘huge number’ < Pers. lak but has no entry for لجّة ‘deep of the sea’, i.e. he does not claim the sense Persian re-borrowed.\"}\n  ]\n})\n\nN.append({\n  \"id\": 13,\n  \"lang\": \"Greek\",\n  \"words\": \"rhegos; rego-lith\",\n  \"verdict\": \"disputed\",\n  \"derivation\": (\n    \"ῥῆγος rhḗgos is a genuine Homeric word of this root, but it does not mean ‘color, dye (red)’: it \"\n    \"means ‘dyed rug, blanket, coverlet’. Walde-Pokorny II 366, under ‘1. reĝ- „färben“’, has ‘hom. \"\n    \"ῥῆγος n. „gefärbter Teppich, bunte Decke“’ beside ῥέζω ‘färben’, ῥέγμα ‘gefärbter Stoff’ and \"\n    \"ῥαγεύς/ῥογεύς ‘Färber’; Watkins (AHD reg-3) ‘Greek rhēgos, blanket, rug’; Cheung 2007: 314 lists \"\n    \"‘Gr. ῥῆγος (n.) “carpet, rug”’ among the IE cognates; Beekes (EDG 2010) explains it as a result \"\n    \"noun to ῥέζω, ‘that which has been dyed’, while noting that the η-vocalism and the ῥεζ-/ῥηγ- \"\n    \"alternation are not straightforward. Buck §15.61 (the page Nourai cites) gives only ῥέζω ‘dye’ \"\n    \"and ῥεγεύς ‘dyer’, not ῥῆγος, and never a sense ‘color’. The second item, ‘rego-lith : red stone’, \"\n    \"is not a Greek word at all: regolith is an English coinage of 1897 (see node 14), and its \"\n    \"first element is ῥῆγος ‘blanket’, not ‘red’. The root affiliation Nourai draws is sound; the two \"\n    \"glosses in the box are both wrong, and the printed page (PDF p.418) shows they are the book’s, \"\n    \"not the extraction’s.\"),\n  \"derivation_fa\": (\n    \"ῥῆγος واژه‌ای هومری و از همین ریشه است، اما معنای آن «رنگ (سرخ)» نیست؛ «فرش و رواندازِ رنگین» \"\n    \"است. والده–پوکورنی (جلد ۲، ۳۶۶) زیر ریشهٔ reĝ- «رنگ کردن» می‌نویسد: «ῥῆγος هومری، فرش رنگ‌شده، \"\n    \"روانداز رنگارنگ»؛ واتکینز، چونگ و بیکس نیز همین را می‌گویند (بیکس: «آنچه رنگ شده است»). \"\n    \"باک در همان صفحه‌ای که نورایی ارجاع داده تنها ῥέζω «رنگ کردن» و ῥεγεύς «رنگرز» دارد. \"\n    \"افزون بر این، «rego-lith» اصلاً واژه‌ای یونانی نیست. این دو خطا از خود کتاب است نه از خوانش اسکن.\"),\n  \"sources\": [W_RHEGOS, W_REGO],\n  \"ref_check\": [\n    {\"ref\": \"SYN:1051\", \"status\": \"partial\", \"note\": SYN_NOTE + \" Buck gives ῥέζω ‘dye’ and ῥεγεύς ‘dyer’ — the root connection Nourai wants — but no ῥῆγος and no noun meaning ‘color, dye (red)’.\"},\n    {\"ref\": \"OEW:333\", \"status\": \"not_checked\", \"note\": \"Shipley 1984 is lending-only on archive.org and not on disk; the page could not be read.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. II p.366\", \"stance\": \"contradicts\", \"note\": WLD_NOTE + \" — ῥῆγος is glossed ‘gefärbter Teppich, bunte Decke’, not ‘colour’.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins s.v. reg-3\", \"stance\": \"contradicts\", \"note\": \"‘Suffixed form *rēg-es- in Greek rhēgos, blanket, rug: REGOLITH.’\"},\n    {\"src\": \"POK\", \"where\": \"p.854\", \"stance\": \"partial\", \"note\": \"Pokorny cites ‘gr. ῥέζω … ῥέγμα „gefarbter Stoff“, ῥαγεύς (also ῥογεύς) „Farber“’ but not ῥῆγος (Walde-Pokorny, his own source, does).\"},\n    {\"src\": \"CHEUNG\", \"where\": \"p.314, IE cognates\", \"stance\": \"partial\", \"note\": \"‘Gr. ῥέζω “I dye, paint”, Gr. ῥῆγος (n.) “carpet, rug”, Gr. (inscr.) ῥογεύς (m.) “dyer”’ — same root, different meaning.\"}\n  ]\n})\n\nN.append({\n  \"id\": 14,\n  \"lang\": \"English\",\n  \"words\": \"regolith\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"regolith is a learned English compound coined in 1897 by the American geologist George P. \"\n    \"Merrill for the mantle of loose, unconsolidated rock debris lying on bedrock: Gk. ῥῆγος \"\n    \"‘blanket, rug’ + λίθος ‘stone’, i.e. ‘blanket of stone’ (Etymonline s.v. regolith; Watkins lists \"\n    \"REGOLITH as the sole English reflex of reg-3). The connecting -o- is the ordinary Greek \"\n    \"compositional vowel. The derivation from the Greek word is therefore exactly as drawn; only \"\n    \"the sense ‘red stone’ attached to it in the previous box is wrong.\"),\n  \"derivation_fa\": (\n    \"regolith واژه‌ای ساختگی و دانشی است که در ۱۸۹۷ میلادی در زمین‌شناسی ساخته شد: از یونانی \"\n    \"ῥῆγος «روانداز، پوشش» و λίθος «سنگ»، یعنی «پوشش سنگی» که بر سنگ بستر را می‌پوشاند؛ \"\n    \"واتکینز نیز همین واژه را تنها بازتاب انگلیسی ریشهٔ reg-3 می‌داند. ساخت واژه درست رسم شده؛ \"\n    \"تنها معنای «سنگ سرخ» در کادر پیشین نادرست است.\"),\n  \"sources\": [W_REGO],\n  \"ref_check\": [\n    {\"ref\": \"SYN:333\", \"status\": \"not_found\", \"note\": \"Buck p.333 (SYN.txt leaf 357) is §4.8x/16.x on ‘tired, weary’ — nothing about stone, soil or Greek ῥῆγος. The citation looks like a slip for OEW:333 (Shipley), the reference used for the Greek node next to it.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins s.v. reg-3\", \"stance\": \"supports\", \"note\": \"‘Suffixed form *rēg-es- in Greek rhēgos, blanket, rug: REGOLITH’, and the index line ‘REGOLITH reg-3’.\"},\n    {\"src\": \"WEB\", \"where\": \"Webster’s New Twentieth Century Dict., vol. I\", \"stance\": \"silent\", \"note\": \"grep of ‘regolith’ in WEB_vol1.txt returns nothing; the word is absent from this edition’s OCR.\"},\n    {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard Dict.\", \"stance\": \"silent\", \"note\": \"grep of ‘regolith’ in FSD_vol1–4 returns nothing.\"},\n    {\"src\": \"KLN\", \"where\": \"Klein, Comprehensive Etym. Dict.\", \"stance\": \"silent\", \"note\": \"no regolith headword found in KLN_1966.txt.\"}\n  ]\n})\n\nout = \"/home/sfmqrb/git/rishe/data/verification/page-418.json\"\nwith io.open(out, \"w\", encoding=\"utf-8\") as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"wrote\", out)\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-418.py",
 "description": "Build page-418.json"
}
```


### [2026-09-14T01:35:02.213Z] TOOL RESULT

```
wrote /home/sfmqrb/git/rishe/data/verification/page-418.json
```


## [2026-09-14T01:35:06.495Z] TOOL CALL #93: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-418.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 418",
 "description": "Validate and run verify_check"
}
```


### [2026-09-14T01:35:07.613Z] TOOL RESULT

```
JSON OK
nodes verified: 14/14
node verdicts: {'confirmed': 7, 'disputed': 4, 'plausible': 3}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 6, 'partial': 6, 'not_checked': 7, 'contradicts': 1, 'not_found': 2}
books consulted: {'supports': 26, 'partial': 10, 'contradicts': 8, 'silent': 11} | by book: {'KLN': 6, 'CHEUNG': 5, 'POK': 4, 'AHD': 4, 'LKT': 4, 'SKT': 3, 'HJB': 3, 'PLA': 3, 'WEB': 3, 'WLD': 2, 'BQT': 2, 'HRN': 2, 'MON': 2, 'FSD': 2, 'FVQ': 2, 'IEC': 1, 'HUB': 1, 'PHD': 1, 'NYB': 1, 'ARY': 1, 'AFM': 1, 'DEV': 1, 'AFA': 1}
```


## [2026-09-14T01:35:14.385Z] TOOL CALL #94: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg418.png data/verification/sources/refs/ocr/BOOK/418.png && ls -la data/verification/sources/refs/ocr/BOOK/418.png",
 "description": "Copy page image for audit"
}
```


### [2026-09-14T01:35:14.463Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 87213 Sep 13 21:35 data/verification/sources/refs/ocr/BOOK/418.png
```


## [2026-09-14T01:35:34.683Z] AGENT

Page 418 (book p. 388) verified. `verify_check.py 418`: 14/14 nodes, **0 PROBLEM lines**.

**Verdicts** — root: 1 confirmed (`Reg 3` = PIE \*reĝ-/\*(s)reg- "to dye"; Pokorny 854, Walde-Pokorny II 366, Watkins AHD `reg-3`, whose numbering Nourai copied). Nodes: 7 confirmed, 3 plausible, 4 disputed.

**Disputed**
- `#2 Pahlavi rang` — drawn as descending from Sanskrit; Cheung 2007:313f. makes MP rang an inherited continuation of Proto-Iranian \*ra(n)j (with Khotanese rrāsa-, Chorasmian rxtyk, NP razīdan). Horn no.623 and Hübschmann §138 only equate it with Skt. raṅga-. Same ultimate root, wrong route.
- `#10 Persian lak "100,000"` — Mo'in's own footnote at BQT 1900 ("هندی است … از سانسکریت") and Klein make it a loan from Hindi lākh / Skt. lakṣá-, which Watkins does *not* put under reg-3; rests on the old lākṣā/lakṣa conflation.
- `#11 Arabic lajj` — Asbaghi (PLA p.240) *does* support lajj "huge number" < Pers. lak, but لُجّة "deep of the sea" is native Arabic (root ل-ج-ج, Qur'ānic 27:44, absent from Jeffery). Addi Shir has no لجّ entry at all.
- `#13 Greek rhegos / rego-lith` — glosses are wrong: ῥῆγος is "dyed rug, blanket" (WP II 366 "gefärbter Teppich"; Watkins "blanket, rug"; Beekes "that which has been dyed"), not "color, dye (red)"; and "rego-lith : red stone" is not Greek — regolith is an 1897 English coinage meaning "blanket of stone".

**Plausible**: `#5` Skt. rākṣā/lākṣā (Watkins "Perhaps"; Mayrhofer calls it uncertain — and "lac" listed as a Sanskrit word is not one); `#9` shellac is English *shell + lac*, not via the Portuguese→French chain; `#12` lojjeh is correctly an Arabic loan in Persian (Mo'in tags [ع.]) but the Persian→Arabic→Persian round trip is not supportable.

**Reference checks**: 6 supports, 6 partial, 1 contradicts (KLN:856 for node 10 — Klein files lak under *Alek-*), 2 not_found, 7 not_checked. Two citation slips worth noting: **SKT:281** — Skeat's Lac/Lacquer entries are on p.238 of the 1911 Concise (p.281 is in M-); **SYN:333** for *regolith* — Buck p.333 is "tired, weary", almost certainly a slip for OEW:333.

**Extraction errors: none.** The printed page (PDF 418, rendered and read) matches the JSON exactly, including `rajîdan رَجیدن (رزیدن، رنگرز)` — and رجیدن is genuine (Dehkhodā/Mo'in: "رنگ کردن، لکه کردن — رجوع به رزیدن"), a variant of رزیدن, so no transcription flag. Page image archived at `data/verification/sources/refs/ocr/BOOK/418.png`; 9 web sources archived via `fetch_source.py`.
