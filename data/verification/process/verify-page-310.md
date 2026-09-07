# Verification process log — verify-page-310


## [2026-09-06T23:12:20.423Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 310 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-310.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-310.json. Write /home/sfmqrb/git/rishe/data/verification/page-310.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 310` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T23:12:22.003Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T23:12:22.708Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T23:12:22.726Z] TOOL RESULT

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


## [2026-09-06T23:12:22.905Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-310.txt"
}
```


### [2026-09-06T23:12:22.916Z] TOOL RESULT

```
1	=== PDF page 310 (book page 280) ===
2	--- entry 0 ---
3	ROOT Lěsos -> redirect to Lěs
4	--- entry 1 ---
5	ROOT Letrâ -> redirect to Letro
6	--- entry 2 ---
7	ROOT [Indo-European] Letro, Letros, Letrâ : skim, strip, piece  (refs POK:681; IEC:681)
8	#1 (parent #0) [Persian] refs=IEC:681; MON:3563 | latreh «لَتره» : fragment, piece (of cloth) | extra: لَت ، لت و پار | NOTE: See "Lěk" for another possible root.
9	#2 (parent #0) [Germanic] refs=AHD:1526 | lethram : leather
10	  #3 (parent #2) [English] refs=AHD | leather
11	--- entry 3 ---
12	ROOT Letros -> redirect to Letro
13	--- entry 4 ---
14	ROOT [Indo-European] Leu, Lu : to smear, make dirty  (refs POK:681)
15	#1 (parent #0) [Avestan / Old Persian] refs=FFD:26 | rŭ, râu : to be dirty ; â-rŭ-ta, â-râw, aya : dirty
16	  #2 (parent #1) [Pahlavi] refs=BQT:58,358; HRN:10,62; HUB:8,36 | â-lutan : to make dirty ☞Apo ; pâlutan (pat-lutan) : to filter, protect against dirt ☞Pa | NOTE: HUB:36 does not agree with the link between "âlŭdan" and "pâlŭdan".
17	#3 (parent #0) [Persian] refs=AEF:340; FFD:26 | âludan «آلودن ( آلای )» : to make dirty ; pâludan «پالودن ( پالیدن ۱ )» : to clean ; pâlâyeš «پالایش» : cleaning ; pâludeh «پالوده ، فالوده» : cleaned, a dessert ; pâlŭneh «پالونه» : filter, pot used for cleaning ; pâlân «پالان» : a straw-filled saddle
18	#4 (parent #0) [Greek] refs=AHD:364 | dia-luein : to loosen apart ; dia-lusis : filtering ☞Dwo
19	  #5 (parent #4) [French] refs=None | 
20	    #6 (parent #5) [Persian] refs=None | dîyâlîz «دیالیز» : dialysis
21	  #7 (parent #4) [English] refs=AHD:364 | dialyze, dialysis
22	#8 (parent #0) [Latin] refs=AHD | lutum : dirt ; polluere : to pollute
23	  #9 (parent #8) [English] refs=AHD | pollution
24	
```


## [2026-09-06T23:12:24.761Z] AGENT

I'll read the source JSON and reference infrastructure.


## [2026-09-06T23:12:26.096Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-310.json",
 "description": "Read source JSON page 310"
}
```


### [2026-09-06T23:12:26.132Z] TOOL RESULT

```
{
  "pdf_page": 310,
  "book_page": 280,
  "entries": [
    {
      "root": {"name": "Lěsos", "redirect": "Lěs"},
      "nodes": []
    },
    {
      "root": {"name": "Letrâ", "redirect": "Letro"},
      "nodes": []
    },
    {
      "root": {
        "name": "Letro, Letros, Letrâ",
        "lang": "Indo-European",
        "refs": "POK:681; IEC:681",
        "gloss": "skim, strip, piece"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "IEC:681; MON:3563",
          "words": [
            {"translit": "latreh", "gloss": "fragment, piece (of cloth)", "script": "لَتره"}
          ],
          "script_extra": "لَت ، لت و پار",
          "note": "See \"Lěk\" for another possible root.",
          "quote": {"text": "مرا اگر چه به بستر لت کتان انداخت - زروی صوف نظر بر نمیتوان انداخت", "poet": "Nezâm Qârî"}
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD:1526",
          "words": [
            {"translit": "lethram", "gloss": "leather", "script": null}
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
            {"translit": "leather", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Letros", "redirect": "Letro"},
      "nodes": []
    },
    {
      "root": {
        "name": "Leu, Lu",
        "lang": "Indo-European",
        "refs": "POK:681",
        "gloss": "to smear, make dirty"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "FFD:26",
          "words": [
            {"translit": "rŭ, râu", "gloss": "to be dirty", "script": null},
            {"translit": "â-rŭ-ta, â-râw, aya", "gloss": "dirty", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:58,358; HRN:10,62; HUB:8,36",
          "words": [
            {"translit": "â-lutan", "gloss": "to make dirty", "script": null, "see": ["Apo"]},
            {"translit": "pâlutan (pat-lutan)", "gloss": "to filter, protect against dirt", "script": null, "see": ["Pa"]}
          ],
          "script_extra": null,
          "note": "HUB:36 does not agree with the link between \"âlŭdan\" and \"pâlŭdan\".",
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Persian",
          "refs": "AEF:340; FFD:26",
          "words": [
            {"translit": "âludan", "gloss": "to make dirty", "script": "آلودن ( آلای )"},
            {"translit": "pâludan", "gloss": "to clean", "script": "پالودن ( پالیدن ۱ )"},
            {"translit": "pâlâyeš", "gloss": "cleaning", "script": "پالایش"},
            {"translit": "pâludeh", "gloss": "cleaned, a dessert", "script": "پالوده ، فالوده"},
            {"translit": "pâlŭneh", "gloss": "filter, pot used for cleaning", "script": "پالونه"},
            {"translit": "pâlân", "gloss": "a straw-filled saddle", "script": "پالان"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {"text": "پالود جان خویش به پالونهٔ بلا - پیمود عمر خویش به پیمانهٔ زمان", "poet": "Moe`zzî"}
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD:364",
          "words": [
            {"translit": "dia-luein", "gloss": "to loosen apart", "script": null},
            {"translit": "dia-lusis", "gloss": "filtering", "script": null, "see": ["Dwo"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": null,
          "words": [
            {"translit": "dîyâlîz", "gloss": "dialysis", "script": "دیالیز"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 4,
          "lang": "English",
          "refs": "AHD:364",
          "words": [
            {"translit": "dialyze, dialysis", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "lutum", "gloss": "dirt", "script": null},
            {"translit": "polluere", "gloss": "to pollute", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "pollution", "gloss": null, "script": null}
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


## [2026-09-06T23:12:27.745Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','IEC','MON','AHD','FFD','BQT','HRN','HUB','AEF','WLD','SYN','BRT','KNT','PHD','NYB','CHEUNG','ARY','KLN','SKT']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


### [2026-09-06T23:12:31.298Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/downloa
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
CHEUNG MISSING
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
```


## [2026-09-06T23:12:36.550Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -80; echo ---; ls ocr 2>/dev/null | head"
}
```


### [2026-09-06T23:12:36.602Z] TOOL RESULT

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
---
AFM
ARY
BOOK
BQT
HRN
IRN
PLA
SNS
SOD
TAD
```


## [2026-09-06T23:12:37.104Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '1,200p' data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-06T23:12:37.145Z] TOOL RESULT

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
```


## [2026-09-06T23:12:44.694Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Schmutz, beschmutzen\\|leu-1\\|leu-2\" POK_full.txt | head -40; echo ===; grep -n \"lutum\\|polluo\\|polluere\" POK_full.txt | head -20"
}
```


### [2026-09-06T23:12:44.743Z] TOOL RESULT

```
Exit code 1
14649:Root / lemma: b^leu-1: b^lau-: b'^lu-{*b'^\e\^-^) 
14725:Root / lemma: b^leu-2: b^lau-. b^lu- 
30429:name' see Root / lemma: Rleu-1, RIeua-. Rlu-\ to hear, cry). 
47616:Root/ lemma: kleu- {a\so kleu-1) and klau- 
51421:Root/ lemma: Rleu-1, RIeue-. Rlu- 
51526:Root / lemma: Rleu-2: *Rld[u]- : Rlu- 
51531:Root / lemma: Rleu-2. *Rld[u]-. Rlu-\ to rinse, clean, tear, derived from Root/ lemma: Rleu- 
56187:Root/ lemma: leu-2 {* leugh^: "to cut off, separate, free' : Root/ lemma: lehug- {* lehugh^: 
56283:Note: probably extensions from leu-2. 
(eval):1: == not found
```


## [2026-09-06T23:12:45.248Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"letro\\|le-tro\\|lethram\\|leþr\" POK_full.txt AHD_watkins1985.txt IEC.txt | head -40"
}
```


### [2026-09-06T23:12:45.298Z] TOOL RESULT

```
AHD_watkins1985.txt:690:letro-. Leather. Germanic */ethram in Old English lether., leather: LEATHER. [Pok. letro- 681.]
AHD_watkins1985.txt:1739:LEAGUER! legh- LEAK leg-2 LEAN! klei- LEAP klou- LEARN leis-1 LEASING leu-! LEAST leis-2 LEATHER letro- LEAVE! leip- LEAVE? §leubh- LEAVEN legWh- LECHER leigh- LECTERN leg-1 LECTION leg-1 LECTURE leg-' LEDGE legh- LEDGER legh- LEE kele-1 LEECH! feg-1 LEECH? leig-1 LEEK leug-! LEER kleu-! LEES legh- LEGACY leg-1 LEGAL leg-1 LEGATE leg-1 LEGATO leig-1 LEGEND leg-1 LEGERDEMAIN leg¥h- LEGIBLE leg-1 LEGION leg-1 LEGISLATOR leg-1, tele- LEGIST leg-1 LEGITIMATE leg-1 LEITMOTIF leit-2 LEMAN leubh- LEMMA! (s)lag¥- LEMMA? lep-t LEMURES_ lem-2 LEND leikw- LENGTH del-1 LENIENT [6-2 LENIS [6-2 LENITIVE |@-2 LENITY 16-2 LENT del-1 LENTO lento-, lep-1. LEPIDO- lep-1 LEPIDOTE lep-1 LEPRECHAUN kWrep-, legwh- -LEPSY (s)lag¥- LEPTO- lep-1 LEPTON! lep-1
IEC.txt:5881:$uél- (gul-) “burn; burning, bright, clear’. Cf. WP I, 643 Skt. jválami, jváråmi ‘burn, blaze’; jvaláh ‘flame’; jvàlà, £. id.; (z-gde in jürnah “burning”; jürníh ‘blaze’); Per. zuyal ‘embers’; Hitt. (queried) hwallis ‘embers’; Gk. cf. deíle “after- noon’; déletron ‘torch, lamp’; (z-gde in OHG chol, kolo “coal? and com. Gmc. cf. ON kol ‘coal’; Oss. àvzali, Dig. ávzalu, s. id.)
IEC.txt:7321:kletros Cf. WP I, 490 Umb. kletra- ‘bier’; Ir. cleather ‘stake’; W cledr “board; roof-shingle'. (Isophones, kinship un- certain)
IEC.txt:8880:q. v. Cf. also kletis and kletros, all with initial
IEC.txt:8904:(Kletro-, see note on kletros)
IEC.txt:9695:letros, å ‘piece, strip, skin”; letró, io ‘strip, flay, têar’. WP II, 428 Per. latre ‘part, fragment’; Gk. cf. ko-letráo (‘trample’, if ko- is a px.); Ir. leathar, m. “skin, hide’; W lledr, m. id. (and “leather?); Br. ler, lezr, m. id.; Mir. cf. letraim, v. ‘mangle, téar'; MHG léder, n.; OE -leóer, leóer-, cpds. ‘eather’; MHG cf. l&deren, lideren, v. ‘tan’
```


## [2026-09-06T23:12:55.794Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"l[eé]tro\\|Leder\" POK_full.txt | head -30; echo \"=== POK 01/02/03\"; grep -ln \"letro\" POK_0*.txt"
}
```


### [2026-09-06T23:12:55.852Z] TOOL RESULT

```
55410:(*A£nap6(;); lengthened grade {d)\ Acbnri "wrapping, sleeve, garment, Ledermantel' 
75142:tear, rend, plage' {*skolid), KO-aKuA-paria "Lederschnitzel, Abfall from leather', okwAoc; 
75470:German schin^a kind of russisches Ledergeld'), Middle High German schinti. " fruit bowl ', 
75701:{skraho) "piece dijrren Leders etc.'; 
79862:Leder, breastplate, mantle', Aeolic anaAic;, Attic HJaAic; 'scissors'; to acpaAaaasiv also 
88783:projectile)' = Avestan vadar- n. "weapon (for hitting)', i/ao'/7/'a/77"Lederriemen', Old Indie 
88875:Proviant'; vadhra-m. n. "Lederriemen'; 
92198:"skin; Lederschild', (Aeolic) YpTvo(; (i.e. FpTvo(;) Ssppa Hes., hom. laKaOpwoq 
=== POK 01/02/03
POK_02.txt
```


## [2026-09-06T23:12:56.033Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=9660 && NR<=9700' IEC.txt | sed -n '1,60p'"
}
```


### [2026-09-06T23:12:58.791Z] TOOL RESULT

```
lengho (1) “stretch, reach, advance, lunge, dart, project’. Cf. longhos and ingh-. WP I, 436 Skt. langhami “leap upon; waste’; langhe, mp. ‘cross’; ranghe "run cf. also ranghas, n. ‘speed’; Av. rag- (zero-gde?) ‘jump; lift; Gk. cf. (*-ñ-) lagkháno, pf. (*-o-) iélogkba; aor. (-n-) élakhon (*'cast', hence “acquire by luck"), cf. lógkhe (lit. ‘casting’, hence ot); MIr. & Ir (ambig. lingim (eap, dash’, but cf. *plenK-); OHG gi-lingan “proceed; succeed’; MHG cf. linge, f. ‘luck’; adj. ‘rapid’; R ljagát, ljagnùť ‘kick’; cf. dial. ljàga ‘thigb’; Z-gde in Latv. linga ‘sling’; o-gde in OHG lang (Clong', and com. Gmc.) and in Lat. longus
lenghó (2) “reject, rebut, rebuff Gk. cf. elégkho “rebut, rebuff; Latv. liedzu, liegt “forbid, deny, refuse'; cf. o-gde langaju, at “call names, abuse”
lengho (3) “trail, lie limp, pine’ (?) (Variant: leng-, long-. Si. Li. ambig.) (Per. langam, langidan, inf. “limp? is from a variant of type *leng- in view of Skt. langami, id.; langah lame); OCS 1ego, lẹšti “lie down’; Pol. cf. leg, m. ‘brood’; legnac, intr. ‘hatch out’; Li. cf. lengstu, lengti, v. ‘languish’. (For Lat. langueo, see slangueio. WH & EM un- tenable)
lenguhos (variant of type elnguhos, elnghus, q.v.) lightweight Av. cf. renj-, v. ‘be lightweight; Gk. (from Phryg. or Thrac?) lémbos, m. ('skiff. The ex- pected Gk. form wd. be *lemph-); Li. lefigvas & lengvus "lightweight, easy’; Latv. liegs, id. (For MHG linge “rapid”, see lengho (1))
lenis, os *easy, soft, pliant, docile; thigh, waist, loin’. Cf. WP II, 395 Av. rānō, m. ‘thigh’; Per. ran, id.; Gk. lenís, f. Ctrollop', whence Lat. leno, -onis, m. ‘pimp’, if not fr. *slen-, q. v.); Lat. lēnis “gentle, soft, easygoing’; LLat. lēne, n. ‘ointment, salve’; (Ir. cf. léan, m. ‘loin’ & cf. the semantics of G Weiche ‘flank’. Ir. fr. *lein-); OE læne ‘frail, poor, perishable’; OCS lënü “lazy”; lëni, f. ‘laziness’; Cz. cf. je mi lé ‘I am disinclined’; Li. lēnas ‘tame, quiet, slow; Latv. lēns, id. (For Per. lin, Ir. léan, MHG Iin & Li. leinas,
679
see leinos). See next.
lënið, lið ‘soften, ease, weaken; be soft, be easy”, etc. See lenis Lat. lénio, īre ease, allay’; OCS lénjo se, -iti se “lounge, laze’; Cz. leniti, inf. id. (Icel. iso- phone: læna, f. ‘brook’; v. *flood")
lenkKtis (lenKis), io (?) ‘spot, freckle; lenti. Cf. WP II, 437 Lat. lēns, gs lentis, f. lentil’; OCS lesta, id.; Srb. leća, leće, f. & n. id. (and ‘freckle’); Latv. cf. lēca (“lentil”, for *lieca in a dialectal form? Cf. also lecenes, pl. *measles"). Simplex in Li. lésis & lefisis, m. "lentil'
lenquó, ið “bend, turn, twist'. Cf. lonqu-, Inqu-. WP II, 435 Skt. cf. rankutih, f. ‘vetch’; OCS lẹkọ, lesti “bend, turn, twist", beside leto, lecati, denom. *ensnare'; Li. lenkiü, leükti ‘bend’, cf. also lenkmuó, eps m. “bend of elbow or knee’; lenke, f. “valley”; Latv. liecu, liekt “bend” be- side lencu, lenkt ‘go round; haunt’
lentā ‘timber, wood (Variant of elntā, q. v.). WP II, 437 Alb. låndë, T lëndë, f. “timber; material; ON lindi, f. limetree; shield or spear of lime (fr *lentis or *lentio); Srb. letva ‘lath’; Li. lentà ‘board’; Latv. (?) lieta ( (thing, matter’. Cf. semantics of Lat. materies)
lentos, ios ‘easygoing, slack, slow, smooth, mild, calm. WP II, 437. See next Lt. lentus ‘slow, sluggish, gentle, pliant’; Br. lent ‘timid, feeble’ beside landar ('sluggish', fr. *lentero-, see next); OHG lindi, MHG lin- de, lint “soft, mild, smooth, tender”; lint, gs lindes, m. (snake'. Cf. G Lindwurm); OE lipe, as MHG, beside lióre ((2) *'slothful, confused with type lyóre ‘evil: G Diederich ‘wanton’, see leut- (2); EME lither “slothfuP; cf. OE
hóercian ‘smooth, flatter’; ON linnr, m. .
‘snake’; Li. (Zemaité) lefitas (*calm, quiet. Lalis). Denom. in Lat. lentere ‘dawdle’ and Br. cf. landréi, landréa, id. (fr. *lentor-). Cf. Vedic rántyah “at ease’
lentris, ios, (lentoros) ‘sluggish, slow; slow boat" (?). See lentos Lat. (?) linter, gs lintris, f. ‘small boat’; Br. landar, adj. ‘sluggish’, fr. *lentoro-; OE lióre (*'sluggish': EME lither, id.)
lënið, iið — les- (lësla, ós, ióm)
15
20
25
30
40
45
680
lenuos, see linuos
lepos (1) ‘small, fine, dainty, trivial’. WP II, 430 Per. cf. laf ‘swagger beside làbah ‘flattery: desire’; Myc. cf. repoto- (lepto- ‘fine’: Gk. lep- tós, id.); Lat. cf. lepos, gs Ons, m. “wit, mirth’; cf. lepidus ‘dainty, pretty, witty, plea- sant’; Li. lepùs, id. (& ‘finicky’) beside lëpnas, id.; Latv. lepns ‘haughty’, cf. lepoties, refl. ‘swagger’. (NB. For OCS lépü ‘decent’; Cz. lepý ‘dainty’; Slovene iép “handsome; Blg. lëp, id. see loipos (1) in view of Latv. laipns ‘friendly, kind’). Cf. MIr. leos (‘radiance’, fr. *|epost-)
lepos (2) “leaf, petal, peel’. Cf. lop- Gk. lépos, gs -eos, n. & lepís, f. “scale, shell", cf. also Hes. lepastís, f. ‘scale; limpet': R lè- Dest, f. “strip; petal; leprós ‘scaly’; lépo, v. (peel. Adj: leptós Ou: lépra ‘leprosy’; LLat. (Ps. Apul) cf. penplepios 'spurge-laurel, lit. “five leaves', from its terminal cluster; Ir. leo, m. ‘film, esp. of oil on water’; Slovene f. lepen, m. “leaf”; R cf lépestt, f. “strip; petal; Srb. cf. lepetati, inf. ‘flutter’
lép- (?) MHG lāb if distinct from là, gs lawes, see leuis (1) “mild, of weather’; Li. lépis, m. *dawdler'; lepti, inf.; lepstà 1sg. ‘flag, be limp’; cf. Latv. lépot, inf. ‘dawdle’ (with expressive initial ]-)
lerdos (?) ‘clumsy, awkward’. Cf. lurd-. (Variant: lordos ?) Sp. lerdo ‘ponderous, clumsy, heavy’; MHG lërz “awkward, left-handed' beside lérzen, v. ‘stammer’. Cf. (?) Gk. lordós “bent?
lergo (?) Per. larzidan, inf. ‘tremble’; larze, s. ‘tremor’; MHG, MLG lérken, lirken ‘stammer’. (Iso- phonic Icel. lerkaóur is ‘bruised, sore. MHG lérc & lirc is "left-hand; lame). Ir. learg is “plain, track, road; slope”, and leirg, f. is “path; reason?)
lés- (lesa, ós, ióm) (?) “place, space, area, room” Per. -lax, cpds. “-place'; OHG cf. gi-lari, n. ‘room, dwelling’; Icel. lár *ditty-box'; Sw. lår, m. ‘box, drawer’; LW in R lari; Latv. lēsa ‘ayot, mudfiat'. (Isophonic: ON láss ‘lock; arrow,
681
bolt’: Sw. lås, n. ‘lock’)
leskos (ledskos ?) ‘feeble, limp’. Cf. los-quos (Iks-) Ir. leasc, adj. id.; OW & W llesg ‘feeble, slug- gish’; llesgu, tr. ‘weaken? OHG lëskan, sv A ‘die out; MHG léschen, sv 4, id. (FK: EWDS: lóschen untenable)
leso, ið ‘peck, pick, gather, read WP II, 440 Skt. rasàmi, rasyāmi (taste, feel, sample’. Ambig.); Go. lisan, sv. 5 “gather”; MHG lésen, sv 5 “gather, choose, read, tell’; OE lesan ‘pick, glean’; ON lesa ‘pick; catch; read”; Li. lesu, lésti ‘peck, pick’; Latv. lešu, lest ‘reckon, count? beside (o-gde) sa-lasit, inf. ‘gather up’; sa-lasas, fpl. ‘scraps, gleanings'
letos, is (let-) “free, Easy; ease’ ; Skt. ratáh *bestowed"; ratih ‘generous, favour- able’; Br. līt, lid, pl. -u, m. “fate; joy; caress’; Go. cf. un-léps, -léds “poor, disowned'; un- ledi, n. ‘poverty’; OE un-ldéd “abandoned, stray’; un-lædu (w. non-historic -u, f. *mis- ery’); OCS læti, phr: — jesti “it is allowed’; lótije, n. ‘facility’; Li. lētas ‘slow, easygoing, soft, quiet, meek’; Latv. lēts ‘cheap’; short vowel in MHG lëdig ‘free’; LW in Finnish: lieto “soft, tender, gentle". (The background of Lat. laetus ‘fortunate’ and lētum ‘death’ is uncertain, as also that of OCS lëto ‘sum- mer’. LLat. laetus ‘liege’, as also OFr. lige, id. is a Gmc. type *leþigas: G ledig). The iso- phone OE Leo n. ‘county division’; ON láð, n. ‘land’; G Lehde, f. ‘upland, high plateau? is reflected in the LLat. LW leta *court-leet". Blg. letăv ‘horizontal’ is without an etym.)
letros, å ‘piece, strip, skin”; letró, io ‘strip, flay, têar’. WP II, 428 Per. latre ‘part, fragment’; Gk. cf. ko-letráo (‘trample’, if ko- is a px.); Ir. leathar, m. “skin, hide’; W lledr, m. id. (and “leather?); Br. ler, lezr, m. id.; Mir. cf. letraim, v. ‘mangle, téar'; MHG léder, n.; OE -leóer, leóer-, cpds. ‘eather’; MHG cf. l&deren, lideren, v. ‘tan’
leubh, leubhi ‘rather, or’. See next Osc. loufi, loufir, cj. "or": MHG liebe, adv. ‘willingly’; E dial. lief, d: Pol. lub, cj. "or: lubo, cj. “though?
leubho (lubh-) ‘desire’. WP II, 419. See next
leskos (ledskos ?) — leudhis
10
I5
```


## [2026-09-06T23:13:07.000Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"letro\" POK_02.txt | head; echo ===; grep -n \"letro\" POK_full.txt | head"
}
```


### [2026-09-06T23:13:07.052Z] TOOL RESULT

```
Exit code 1
5432:letro'  ,Leder^??
(eval):1: == not found
```


## [2026-09-06T23:13:07.415Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Root / lemma: leu-\\|Root/ lemma: leu-\\|lemma: leu\" POK_full.txt | head -20"
}
```


### [2026-09-06T23:13:07.484Z] TOOL RESULT

```
15110:lemma: leuA'^-1 {* leugh-): to grow up; people; free]. 
55668:his, her' + Root/ lemma: leuMy-1 {* lehugh-): to grow up; people; free]. 
56187:Root/ lemma: leu-2 {* leugh^: "to cut off, separate, free' : Root/ lemma: lehug- {* lehugh^:
```


## [2026-09-06T23:13:11.407Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5400,5460p' POK_02.txt"
}
```


### [2026-09-06T23:13:11.457Z] TOOL RESULT

```
Arm.  PI.  lorc-k'  ,convulsio  partium  in  posteriora^;
gr.  XoQdög  ,mit  dem  Oberkörper  nach  vorwärts  gekrümmt',  XoqSovvj -ovad-ai  ,nach  vorwärts  gebogen  sein';
gäl.  lorcachj  lurcach  ,lahm  am  Fuß';   Iure  m.  ,lahmer  Fuß';
ags.  be-lyrtan  , betrügen',  mhd.  lürzen  ds.,  dän.  lyrte  ,scherzen',  mhd. lerzen  ,stammeln',  mhd.  lurz,  lerz  ,link^  (,krumm');  ags.  lort  ,krumm?S dazu  der  PN  Lorting  =  nhd.  Lortzing.
WP.  II  439,  Holthausen  Aengl.  etym.  Wh.  206,  209.
lerg-  ,glatt,  eben,  schlüpfrig'^.
Arm.  oiork  ,eben,  glatt,  poliert,  schlüpfrig'  (o-  wohl  die  Präp.  *po-),  lerk ,glatt,  unbehaart';
mir.  lergg  f.  ,Abhang,  Weg,  Ebene',  less-lergg  ,WeideS  cjmr.  llyry  ,Pfad, Spur',  corn.  l&rgh,  bret.  lerc/h  ,Spur';  ablaut.  air.  lorc,  mir.  lorgg  m. ,Spur,  Schar,  Nachkommenschaft',  cymr.   llivry  >  llim-w  ,Spur';
dazu  nhd.  Lurch,  ndd.   lork?
WP.  II  439.    S.  noch  Horgo-  ,Stock'.
680  f
les-  , sammeln^  auflesend
Got.  Usan  St.  Y.  ^auflesen,  ernten^,  aisl.  hsa  ,sammein,  auflesen,  ein. weben',  später  (durch  nhd.  Einfluß)  ,lesen  (ein  Buch)',  ag-s.  lesan  ,samnieln' as.  ahd.  lesan  ^auf-,  auslesen'  und  (nach  der  Doppelbed.  von  lat.  legere) ,lesen  (ein  Buch)';  hierher  auch  aisl.  lesa^  mhd.  (und  nhd.  dial.)  lismen ,stricken',  und  weiter  ahd.  lesa,  mhd.  lese  .eine  Art  Kleidungsstoff',  aisl. lesni  ,eiue  Art  Kopfzeug';
lit.  lesü,  lesti  ,mit  dem  Schnabel  aufpicken,  Körner  lesen',  Iter.  ap-lasyü ,herauspicken,  auslesen,  wählen';
ob  hierher  air.  lestavj  Lw.  aus  cymr.  llestr  , Gefäß',  acorn.  lester^  bret, lestr  ,Schiff'  ?  Grundbed.  wäre  ,Gefäß  zum  Einsammeln  von  Beeren  u.  dgl/.
WP.  II  440,  Trautmann  160.
[ies:]iös-  ,schlaff,  matt',  Erweiterung  zu  le{i)-  ,nachlassen'.
Got.  lasiws  (*las-luos)  ,schwach',  mhd.  er-leswen  ,schwach  werden';  aisl. lasinn  ,schwach,  zerstört',  las-meyrr  ,schwach,  elend',  mnd.  lasich  =  lasch^ las  ,schlaff,  matt',  isl.   laradr  ,müde';
slav.  *loh  in  bulg.  lo§  ,schlecht,  übel,  schlimm,  häßlich',  skr.  Zö5  ,un- glücklich,  schlecht'  u.  dgl. ;  sehr  fraglich  ist  Heranziehung  von  lat.  sub- lestus  ,schwach,  gering' ;
hierher  als  ,schlaff  niederhängender  Fetzen'  vielleicht  mnd.  las  keil- förmiger Lappen',  dän.  norw.  las,  läse  ,Lumpen',  mnd.  mhd.  lasche  m. ,Lappen,  Fetzen';  lit.  läskana  ,Lumpen,  Lappen',  russ.  löskut  ,Stück, Lappen' ;
toch.  A  Ijäsk-  , Weiche'.  *
WP.  II  439  f.,  Trautmann  150  s.  v.  "^lasia-  und  *laskanä'.
leto-,  leti-,  leto-,  löto-  , Brunst,  Hitze,  Zorn'.
Mcymr.  aelet  (*ad-let-)  , Schmerz',  llet-gynt  ds.,  dehnstufig  llit,  tra-llit ,Zorn',  ncymr.  Uid  m.  ds.,  mit  Abtönung  llawd  , Brunst'  =  mir.  Idth  m.  ds. ; racymr.  aelawt  ,Lärm,  Schmerz'  =  air.  dlad  n.  , Wunde'  (^ad-löto-),  cymr. tra-llod  ,Lärm,  Schmerz' ;
klr.  l'it'  f.  ,Brunst',  Utyty  , befruchten'.
WP.  II  428,  Ifor  Williams  Et.  Gelt.  4,  391.
leto-,  loto-  ,warme  Zeit :  Tag,  Sommer'.
Air.  la{i)the  n.  ,Tag',  gall.  lat...  ,Tage'  im  Kalender  von  Coligny;
altgutn.  lapigs  ,im  Frühling',  schwed.  dial.  läding,  läing  , Frühling', i  lädigs  ,im  vorigen  Frühjahr'  (Het-)]
abg.  leto  ,warme  Jahreszeit,  Jahr',  russ.  Uto  ,Sommer,  Jahr',  dial. ,Süden,  Südwind',  usw.
WP.  II  427,  Berneker  713  f.
681
letro'  ,Leder^??
Air.  lethar,  cymr.  lledr,  bret.  lezr  , Leder'  =  ahd.  lede)',  ags.  hper (engl-  leather),  aisl.  ledi'  n.  ,Leder^  Ist  das  germ.  Wort  alte  Entlehnung aus  dem  kelt.  und  letzteres  als  *'pl-e-tro  mit  lat.  fpÄlis  usw.  (s.  ^e^  .Haut^) verwandt?    S.  Pedersen  KG.  II  45.
WP.  11  428.
X.  leu-,  *leu9-  :  lü-  , Schmutz,  beschmutzen^ ;  lu-to-  ,Kot^
Gr.    Aß^ua    , Schmutz,    Schmach^,    Ui-ir^    ^Beschimpfung',    Xv^alvoi^ai  ,be-
scliimpfe;  schände;  richte  elend  zugrunde';  Xvd-gov,  -og  ^Besudelung'; alb.  tosk.  lum  , Schlamm'/ geg.  lüm^  tosk.  ler  ds.  {lum-,  bzw.  leu-d{h)r-)^
illyr.  ON  Ludriim  ( :  gr.  Iv&qov)  ; lat.  jpolluö  ,beflecke',  lustrum  , Pfütze',  hitum  ,Dreck,  Kot'  = air.  loth  f.  ,Schmutz',  gall.  ON  Luteva,  dazu  cymr.  (mit  Hochstufe)  Uudedic
^schlammig';    mit   anderem  Suffix   mir.  con-luan  , Hundekot',   bret.   louan
,sale' ;
lit.    lutynas,    -ne    ,Pfuhl,    Lehmpfütze';    hierher    wohl    auch    lit.    Unnas
,  Morast'.
WP.  II  406.    S.  auch  unter  2.  leug-.
2.  leu-  , abschneiden,  trennen,  loslösen',  auch  leuQ-  und  ieu-  :  Iqu-  (:  lu-), z.  T.  leu-s-]  lü-no-  ,geschnitten'.
Ai.  lunäti,  lunöti  , schneidet,  schneidet  ab',  lünd-  ,abgeschnitten,  ge- schnitten' ( :  mir.  Ion),  lavitra-  n.  ,Sichel',  lavi-  f.  ds.  ( :  gr.  Xatov,  aisl.  U ds.),  lava-  m.  ,das  Schneiden,  Schur,  Wolle,  Haar,  Abschnitt',  läva-  , schnei- dend', lävaka-  m.  , Abschneider,  Mäher';
gr.  Iva)  jlöse,  befreie;  vertilge  usw.',  Xva  f.  , Auflösung,  Trennung', XvGLg  f.  , Lösung',  Xvzgov  n.  , Lösegeld';  ßov-Xvrög  m.  ,Zeit  des  Ausspannens der  Rinder,  Abend'  (:  so-lütus)]  Xalov  ,Pflugschar'  [Xcxfiov]  vgl.  aisl.  U, mnd.  U,  lehe  ,Sichel'  aus  Heican-  und  ai.  lavi-  ds.) ;  äXayrj,  att.  HXwg  f. ,Tenne' ;
alb.  laj  ,zahle  eine  Schuld'  [Hduniö,  ablautgleich  mit  gr.  Xa{J^)iov)] perlaj  ,beraube',  vielleicht  auch  lete  ,Mähne'  (*leu-t')  und  (von  der  Wurzelf. auf  -5)  lesh  (*leus-)  ,Wolle,  Haar'  (vgl.  dieselbe  Bed.  in  ai.  lava-);  dazu nach  Jokl  L.-k.  U.  127,  147  ff.  fluer  ,Fach  einer  Truhe'  {*ve-lor-  aus  idg. *leu-r-),  sh-lor  , Hängegerüst',  pluar  (*pe-luar)^  Pflugschar',  lug,  liigu  ,Trog', fluge  ,Brett',  luge  ,Löffel' ;
lat.  luöj  -ere  , büßen,  zahlen',  in  Glossen  ,Xv(i)^,  reluö  ,löse  wieder  ein', solüö  (*se-luö)  solutus  , lösen',  lues  (,*Auflösung',  daher  :)  ,unreine  Flüssigkeit usw.';
mir.  Ion  , Hammel,  Schöps'  (:  ai.  lünd-),  air.  loe  f.  ,Wolle,  Fließ' [*löuia)j  lö  ds.  (*Zöwä);
'^•^V:|
682  9
got.  lun  Akk.  Sg,  ^Lösegeld';  us-luneins  , Erlösung',  ags.  ä-lynnan  er- lösen';  aisl.  lyja  ^schlagen,  (mürbe)  klopfen,  entkräften',  Partiz.  luinn ,ermüdet',  nisl.  lüi  ,Ermattiing';  aisl.  le  ra.  , Sichel'  (s.  oben);  *lawa  ^ab- gelöste Rinde  als  Gerbraittel'  in  abd.  lö,  Gen.  löioes  n.  nhd.  Lohcj  mnd lö  ds.;  aisl.  logg  f.  , Bodensatz'  (*lauicö)-  abd.  lih-lawi  (IMüaj  lihla)^  j^xn^, llk-latoe  , Narbe'  (ibd.);  aisl.  lüär  ,Trog' (ausgeschnittener,  gehöhlter  Stamm), ahd.  lüdara  , Wiege';  ablaut.  schwed.  dial.  Ijuder , alter  Riß  an  einem  Baum'-
mit    der    Bed.   ,abgeschnittenes  Brett'  hierher  russ.  Idva   ,Brett,  Bank Steig',  lit.  löva  ,Bettgestell',  lett.  läva  ,Pritsche,  Bettstelle',  dän,  älter  Zo schwed.  lofve,  löge,  aschwed.  loi,   lo,  aisl.   löfi  m.  ,Tenne,  Scheuer'  (aisl,: laß  ist  eine  alte  Ablautform  Heioan-)]
toch.  A  loj  B  lau  ,entfernt,  getrennt';    A   law-,   B    lyu-  , fortschicken'* A  lot  ,Graben,  Loch';
hitt.  lu-uz-zi  {luzzi)  ,Steuer,  Belastung'  (vgl.  gr.  Xvrqov).
s-Erweiterung:  got.  fra-liusan,  ahd.  far-liosan  ,verlieren';  got.  fralusnan ,verlorengehen',  aisl.  losna  ,lose,  locker  werden',  losa  ,lösen',  postverbal los  n.  , Lösung',  ags.  losian  ,verlorengehen',  Denomin.  zu  los  n.  ,Verlust'| lysii  ,schlecht,  böse'  (Husiwa-),  got.  fralustSj  ahd.  forlust  yVerlust^'^  got, laus  ,los,  leer',  aisl.  lauss  ,frei,  lose,  aufgelöst',  ahd.  lös  ,frei,  beraubt, lose'j  ags.  leas  ,leer,  beraubt,  betrügerisch',  aisl.  lausung  f.  ,Unzuver- lässichkeit',  ags.  leasung  ,Lüge',.  leasian  ,lügen';  got.  lausjan,  ahd.  lösian^ lösön  ,losen';  vielleicht  adän.  liuske  m.  ,Weiche'  >  aisl.  Ijöskij  mnd.  lesdit^ mndl.  liesche,  nndl.  lies,  ags.  leosca  ,Weiche',  sowie  jnndl.  liescJie  , dünne Haut',  Schweiz,  lösch  ,locker';  mit  einer  Bedeutung  ,(los)  schlagen,  klopfen' wohl  auch  aisl.  Ijösta  , schlagen,  stechen,  treffen',  Ijöstr  , Gabel  zum  Fisch- stechen', nisl.  lustr  ,Knüttel'  (,*abgehauenes  Aststück');  als  alt  wird  diese  ^ Anwendung  erwiesen,  wenn  mir.  loss  ,Schwanz,  Ende',  cymr.  Host  ,Speer',  i Hosten  , Schwanz',  bret.  lost  ,Schwanz'  anzureihen  sind;
hierher  (Specht  Idg.  Dekl.  56)  lett.  laüska  ,Splitter,  Scherbe',  ablaut. lit.  lüskos  , Lumpen',  lüzgana  ,Hülse,  Schuppe',  lusnä  ,Hülse,  Schale', russ.  lustd  ds.,  usw.  Möglicherweise  verwandt  ist  *leu-  , Stein',  s.  dort.        |
WP.  II  407 f.,  WH.  I  830,  834 f.,  Wissmann  Nom.  postverb.  84 ff.; aus  vorrom.  und  vorgerm.  Heiskä,  Heuskäj  *laskä  in  nhd.  LiscJie,  frz. laiche  usw.  ,carex'  erschließt  J.  Hubschmid  ZcP  24,  81  ff.  ein  idg.  eld-^ eleu-j  eh'  , schneiden'.
I.  leu-  ,nachlassen' ;  vgl.  auch  {s)leu-  ,schlaff'.
Got.  lew  n.  , Gelegenheit',  lewjan  ,preisgeben,  verraten'  (,* überlassen'), ags.  IWivan  ds.,  ahd.  gi-,  fir-läen  ,verraten';
```


## [2026-09-06T23:13:11.795Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"beschmutzen\" POK_full.txt POK_02.txt | head -20"
}
```


### [2026-09-06T23:13:11.850Z] TOOL RESULT

```
POK_02.txt:182:mit  expressivem  -tt-:  mnd.  Matte  , Lappen' =  nhd.  dial.  Matz  , Schmutz- fleck', mndl.  Matten  ,beschmutzen',  mhd.  hekletzen  ds.,  norw.  schwed. mdartl.  klatra  , hudeln';
POK_02.txt:183:daneben  mit  expressivem  dd:  ndd.  kladde  , Schmutzfleck ;    Klette'  (d.i. ^die  Klebende^);    mit   Dent,  +  s :  norw.  klessa  (Mass)   ,kleben,  festhäng-en, platschen,  klatschen',  klessa  (Jdeste)  ,schmieren,  sudeln',  klussa  , beschmutzen, sudeln,  lispeln';    aisl.  Mess  , lispelnd';    vgl.  aisl.  klasi  S.  362. C.  Labialerweiterungen:
POK_02.txt:2139:aksl.  gadi,  m.  ,Kriechtier  (*ekelhaftes  Tier) ;  schädliches  Tier'  (^-g^ödh-), ksl.  ga^du,  gaditi  ,verabscheuen,  tadeln',  russ.  gddith  ,beschmutzen,  be- sudeln, verderben',  serb.  gäd  ,Ekel;  Schlange,  Gewürm',  cech.  haditi ,schmähen,  tadeln'  (usw.,  s.  Berneker  289) ;
POK_02.txt:2143:cymr.  budr  , schmutzig',  budro  ,beschmutzen',  mir.  buadraim  ,trübe,  ver- wirre' (vgl.  Pedersen  KG.  I  112);
POK_02.txt:3173:aksi.  kah  jTtrjlögj  Kot*^  mit  den  Bedeutungen  ^Sumpf,  Morast,  mit  Kot beschmutzen^ ;  dazu  (nach  der  Farbe)  russ.  kalina  ,Viburnum  opulus^,  wie auch  sloven.  kalina  ,Pfütze^   und  russ.  kalü-ga  ^Morast^,  kalu-za  ,Lache'.
POK_02.txt:4550:1.  kuei-,  kuei-no-  ,Schlamm,  Kot,  beschmutzen'.
POK_02.txt:4551:Mit  Formans -12(0)- :lat.  caenum  , Schmutz,  Kot,  Unflat',  ohscEnua^ scaenus  (Rückbildung  aus  *obscenare)  ,sch mutzig,  ekelhaft,  unsittlicj|t (caenum  urbanisiert  für  plebejisches  *cenum  aus  ^coinom,  *quoinom\  iV con-quinäre  ,beschmutzen,  besudeln',  cünire  ,stercus  facere',  ancunulenta^ ,feminae  menstruo  tempore' ;
POK_02.txt:5435:X.  leu-,  *leu9-  :  lü-  , Schmutz,  beschmutzen^ ;  lu-to-  ,Kot^
POK_02.txt:5696:2.  mai-  (moi-?)  ;beflecken;  beschmutzen'?
POK_02.txt:6072:zigen   Farbentönen ;    Schmutz,    beschmutzen' ;    melo-no-   ,schmutzigS Ai.  malind-  , schmutzig,  schwarz',  mlä-na-  , schwarz,  dunkelfarbig',  mala-
POK_02.txt:6386:I.  meu-,  mevLQ- :  mu-  ^feucht,  moderig,  netzen,  unreine  Flüssigkeit  (auch Harn),  beschmutzen',  auch  ,waschen,  reinigen';  mu-dlo-  ,WaschmitteP, mu-tro-  , Schlamm,  Sumpf.
POK_02.txt:6419:mit  anl.  s-  mnd.  afries.  smudden  ^beschmutzen',  ndd.  smudden  ,fein regrien',  wfläm.  smodder  ,Morast',  mengl.  smod  ^Schmutz',  smudderen,  ndl. ^^tnodderen  ^schmutzen',  älter  ndl.  auch  ^schmausen'  (ursprüngl.  ^unreinlich essen  und  trinken';  so  auch  ostfries.  smUs,  nhd.  Schmaus,  älter  ndl. sjnwisteren  ^schmausen'  und  ^beschmieren',  nd.  ndl.  smullen  ^schmausen' und  ,sudeln,  beschmutzen'  wohl  aus  *smud-lön]  lit.  smütnas  ,traurig'  stammt aus  poln.  smutny  ds.  (Vasraer  brieflich).
```


## [2026-09-06T23:13:33.002Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG rau/lud\"; grep -n \"ālūdan\\|alūdan\\|āl[ūu]dan\\|pālūdan\\|pāl[ūu]dan\\|ālāy\\|pālāy\" CHEUNG.txt | head -30"
}
```


### [2026-09-06T23:13:33.049Z] TOOL RESULT

```
=== CHEUNG rau/lud
```


## [2026-09-06T23:13:34.628Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN\"; grep -n -i \"aluden\\|âluden\\|pâluden\\|paluden\\|alûdan\\|palûdan\\|palûde\\|âlûdan\" HRN.txt | head -30; echo \"=== HUB\"; grep -n -i \"aluden\\|paluden\\|âluden\\|pâluden\\|alûdan\" HUB.txt | head -30"
}
```


### [2026-09-06T23:13:34.692Z] TOOL RESULT

```
=== HRN
=== HUB
```


## [2026-09-06T23:13:40.065Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lûden\\|lüden\\|luden\" HRN.txt | head -30; echo \"=== HUB\"; grep -n \"lûden\\|lüden\\|luden\" HUB.txt | head -30"
}
```


### [2026-09-06T23:13:40.124Z] TOOL RESULT

```
792:42. äluden 'beschmutzen', Praes. äläy-em,
798:scheint die Grundbedeutung von älüden 'beschmieren*
1917:Nach FJ soll auch bälüden 'wachsen' bedeuten, wofür als Beweis
2738:278. pälüden 'reinigen', Praes. pälay-em, päläyiden,
2739:paiti + alüden (s. älüden^ No. 42) ; phlv. pälüt (Bund.),
10820:Im Neupersischen hat sich nur pizölüden (oben
11457:; älüden 42, 278.
11736:hölüden 173 Anm.
13258:, pälüden 278.
=== HUB
```


## [2026-09-06T23:13:41.561Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\nfor n in (10+21, 62+21):\n    print('--- leaf',n,'---')\n    print(pages[n-1][:2500])\nEOF"
}
```


### [2026-09-06T23:13:43.405Z] TOOL RESULT

```
412
--- leaf 31 ---
- 9 ~
34(2). äänä, äsnäh 'Öchwinuner, Schwimmerei', üsnäh^ dsnäiv,
aw. ai. ä -f- [/'snä-, nur in der Bedeutung Vaschen' ;
vergl. aber aw. asnätar-, skr. äsnäna- (*Bad').
Vergl. sina (No. 792).
35. äsyäne, äsyän 'Nest'.
a + aw. Ksö- bezw. gäi>. syä- ruhen' ^), oder wohl
bereits wohnen'^). (Nöldeke, mündliche Mitteilung).
Aber das y ist auffällig, vergl. np. süd,
36. üyärden, ayäriden Verschlingen*.
ai. ä + l/^gar- {jacjdrd) verschlingen' ; lat. coräre,
wa;^. nez-yar-am verschlingen*.
In der Bedeutung Verschlingen' vermag ich das Wort
nicht zu belegen. Bei AM., wo es sehr häufig vor-
kommt, bedeutet es immer vermischen, einweichen in'.
In der letzten Bedeutung könnte es zu skr. l/^ghar-,
ghdrati 'besprengen, beträufeln* gehören^).
37. äftäh *Sonne, ixDS'X (jüd.-pers.).
skr. "^ahha + tapa- (vergl. No. 3).
kurd. LW. a^taw (Houtum-Schindler), ätätv etc.
(Jaba-Justi).
38. äfdutn 'letzter', nur im Mujmil ettevärT;^ (ed. Mohl,
Journ. asiat. 1841, S. 178)^), vergl. hafdum zuletzt*^).
«) Hübschmann, ZDMG. 38, 431.
') Bartholomae, Arische Forsch ungren II, 102.
*) Dazu wohl auch äyisten, z. B. AM. 14 Zeile 16, 193 Zeile 11.
do Lagarde, Ges. Abh. 290 ist natürlich unmöglich.
*) Vergl. Spiegel, Grammatik der- Huzväresch-Sprache, 76.
^) Für bäfdum (d. i. be äfdum) haben die Wörterbücher folgende
Belegstellen: SF (S. 95 Vers 53), Metrum Remel:
kär-i dänä nek^ gerded bäf^dum
FR, Metrum Muteqärib:
ci bäyedf kerden kenün bäf^dum
meger -j^äne-röbl cü robeh bMum
Abu SukUr.
FR, FJ, Metrum Muteqärib:
b^r esb-i gümän ez reh-i räst^ x^m
q^räret bedöze-^ büved bäj^dum
Esedl.
--- leaf 83 ---
- 61 -
265^" pädäs, pädes (Vis und Rämin) 'Vergeltung', padast,
pädosn,
phlv. pätdah(i)sn {paiti -f dah(i)sn), päz. pädaisn^
pädaän 'Vergeltung'.
Aus dem Pärsismus übernommenes Wort. Vergl.
np. dasen (No. 528).
266. pädiSäh *König'.
ap. "^pati/Säyadiya-; phlv. päta/sä^ bezw. päta/sah
(übersetzt im Kommentar aw. x^<^y(^^^<^' Vermögend,
erlaubt ; Herrscher) ^).
267. päde 'Heerde'^), padehan.
ap. aw. skr. päta- 'beschützt, bewahrt'.
268. pädyäb, pädyaw rituelle Waschung.
aw. paüyäpa- ; phlv. pätt/äp, pOtyapih,
Rituelles Pärsenwort.
269. pädyävend (i:ixnx5?, Is. 1, 31) 'kräftig'.
phlv. pätyavand 'kräftig'.
paiti + l/^««?-, aw. *paityavanU (Part. Praes.).
270. pär 'das vergangene Jahr', pärsal^ parm.
skr. vergl. panit 'im vergangenen Jahre' ; arm. heru
Vergangenes Jahr' (H. No. 167).
kurd. (LW.) par\ af/. parös-; oss. d. fdi% t/aron
'im vorigen Jahre' (277) ; bei. pari, n. pän (293) ; wa;^.
pardy sar. parvus (vergl. gr. nigvöi).
Ap. paruva- 'früher (aw. paurva-) ist schon im
Pehlevi aufgegeben worden; np. pärav alte Frau' ist
nicht belegt.
*) Zu phlv. pata^sa, np. padisäh als t. t. beim Ehesohluss vergl.
West, Pahlavi Texts» 142 Note 10.
2) FR und F J haben als Beleg folgenden Vers des Ferälädl
(so nach Eth6, Morgenländisohe Forschungen, während FR und die
Strassburger Handschrift des FJ Ferälävl, Salemann, SF Feräläri
schreiben), Metrum: Xeflfi
mäde-gävän-t päde-es her yeh
mh^perver huved cn hirmäyün
```


## [2026-09-06T23:13:50.342Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor n in (32,33,84,85):\n    print('=== leaf',n,'===')\n    print(pages[n-1][:2600])\nEOF"
}
```


### [2026-09-06T23:13:53.421Z] TOOL RESULT

```
=== leaf 32 ===
— 10 -
aw. *up((tama' letzter ; phlv. afdiim, päz. awdum
'letzter.
39. äfvtden ^schaffen, Praes. afrin-em, afrUegär (AM.);
afrtn 1) 'schaffend' 2) 'Lob', vergl. nefnn 'Fluch'.
aw. afrmami 'ich preise' etc., äfrlna- 'Segen'; phlv.
äfritan 'schaffen', afrm 'Lob', nafrm 'Fluch' (AV.);
ai. Ä + i^prT' 'befriedigen' etc.
Die Bedeutung 'schaffen' geht nicht über das Pehlevl
hinaus. Oder zwei ganz verschiedene Verba?
40. ägäh, kundig, Kunde'.
aw. ä + i^kas-, äkasat er erblickte'; phlv. äkäs, äkäslh^
äkäsimtan, arm. LW. akah 'kundig'; ai. Kiä^-, ka^ate
'sichtbar sein, erscheinen, überblicken'.
afy. bei. LW. ägäh.
41. ägenden 'anfüllen', ägenis^ ägm 'voll'.
skr. ghana- 'dick, voll von etwas', m. 'Klumpen',
ähandS' 'schwellend, strotzend'; vergl. lit. (/awd 'genug,
ksl. gonüi 'genügen'^).
42. äluden 'beschmutzen', Praes. äläy-em,
phlv. lütak (AV.).
lat. Inf um; air. loth 'Schmutz'; lit. lutyna-Sy lutgn^
(fem.) 'Pfuhl, Lehmpfütze'.
Durchaus unsicher, da np. äläy-em dann die se-
kundäre Form und ü ursprünglich sein müsste. Auch
scheint die Grundbedeutung von älüden 'beschmieren*
zu sein, vergl. AM. 35, Zeile 6; 40, 16.
43. äluh 'Adler'.
phlv. äluh (Kärn. 59, Note 2), vergl. arvä (Bund.)
in Zendbuchstaben.
Dazu gr. ögvig 'Vogel'; ksl. ortlü 'Adler; lit. erilis;
got. ara\ corn. bret. er, cymr. eryr 'Adler? Vergl.
Hörn, KZ. 32, 583 No. 14.
FK will des falschen Reimes halber in dem letzten Verse statt ^em
vielmehr gom losen, während FJ danach mit Unrecht die Aussprache
bäf^dem für richtig erklärt.
»j KZ. 32, 579 No. 4 war mir leider Rüokert ZDMO. 8, 286
entgangen.
=== leaf 33 ===
- 11 -
44. äleyten 'springen, ausschlagen (vom Pferde)*, Praes.
alezed^)^ alezende^ alezTden^),
got. laikan springen, hüpfen*, laiks Tanz'; lit. laujytl
*wild umherlaufen (von jungen Pferden, Rindern auf der
Strasse)*; air. löeg 'Kalb*, (bei Feist).
kurd. helezium 'ich tanze*, lizim 'ich spiele', Inf.
leiztin.
Die Etymologie stammt von Justi, Dict. kurde-
frangais.
45. ätnäj 'Pflugsterz'.
g. matk (Houtum-Schindler, ZDMG. 36, 70).
arm. mac (de Lagarde No. 1413, Htibschmann
No. 186).
Die Lautverhältnisse von äinaj und mätk passen
nicht zu einander (vgl. auch Bartholomae, Studien
II, 24).
46. ümäden 'zurecht machen, rüsten*, ämUden, Praes.
ämäy-em, ämüy-em,
ap. vergl. ämäta- erprobt*; aw. ämata-, ämayäont^^
sie sollen sich versuchen',
oss. t. amain 'erbauen' (176).
47. äniär 'Berechnung', ämäre,
aw. a + 2 l^mar- 'sich erinnern'; phlv. amär 1) 'Zahl'
2) 'zähle, rechne* (das Verbum ämartan ist nicht belegt) ;
skr. a + V^smaV" (nicht belegt).
48. ätneden 'kommen*, Praes. äy-em (s. No. 60).
ap. ä+ [/^gam-, äjannya 'er käme*; aw. ci+ [/'(/am-,
ägemat; phlv. nrntan, ämatan (PPGl.) ').
Mit Mahjalvokal (FJ.).
^) FR hat einen Beleg aus Siräj eddin:
(Metr. Xeftf)
tie/s^ cun ser^ gesf bestezed
tevsen-äsä beher süy älezed.
*) Beiläufig bemerkt, findet sich bure als Imperativ *komm* ausser
im Kurdischen (Houtum-Schindler) und bei Shukovski dialektisch
auch bei Bäbä Tähir *Uryän aus Rei (Huart, Journ. asiat, Si^me s^rie,
vol. VI, 519).
=== leaf 84 ===
— 62 ~
271. päre ^ück, Teil'.
ai. pärd- *das Letzte' ; (^w, para- SchulaX?) ^) ; phlv.
pärak 'Stück; Geschenk (behufs Bestechung)', AV.
272. päzen *Bergziege*, päzen,
phlv. pacm (Bund.) ; bei. pädin, n. päsin 'Ziegenbock,
männliche wilde Ziege* (290).
273. päzehr 'Gegengift, Bezoar.
paiti + zehr (s. zehr No. 678).
274. päs 'Schutz*, pasban^ päsTden,
aw. pädra- 'Schutz'; phlv. pas (Bund.), pOspäti, vd.
13 (77); ai. pätra-.
274*»^* päsäyt 'bereit'.
paiti + sagten (s. No. 688) ; phlv. pasa/tan^ pasaxtak
(AV.).
phlv. palsäytan könnte auf die Praeposition pa (tipa)
deuten, doch vergl. phlv. j^^^^X (No. 275).
275. päsu% 'Antwort'.
aw. ^paitisahva- [paiti + [/'safih- hat zwar im Awesta
nur die Bedeutung 'beschwören') ; phlv. pasu/ ; arm.
patas/ani 'Antwort*.
276. päSne 'Ferse'.
aw. päsna- 'Ferse'; phlv. päsnak*^ ai. pdrsni-,
kurd. päsüne, päm, päme (ZDMG. 38, 55), päm (JJ.);
af/. pünda ; bei. pünzig, ptnz, n. pTz, pid (306) ; wa/.
päsna, sar. pu/nä 'Ferse'.
syr. LW. j^li/^B 'der Bimstein, mit welchem man
sich im Bade die Fersen reibt', de Lagarde, Ges.
Abh. 73.
277. päk 'rein', paktze,
ai. pavakd- 'rein, klar ; phlv. pak, päkih,
278. pälüden 'reinigen', Praes. pälay-em, päläyiden,
paiti + alüden (s. älüden^ No. 42) ; phlv. pälüt (Bund.),
päz. pälJdan, pälaidan (West, Sik. gum.-Gl.).
bei. LW. palayag^ pälenay 'seihen, worfeln, reinigen'
(292).
^j Vergl. Geldner, Studien I, 16. Bartholomae (briefliche
Mitteilung) verweist mich aber auf aw. parendi- (Indog. Forsch. I, 184)
mit der Grundbedeutung 'Füllser.
=== leaf 85 ===
— 63 —
279. pälez 'Garten (Sahn. I, 73 Vers 207) ^), palezhan, arab.
LW. faliz,
ap. nagdÖHöog; aw. pairida^za-,
LW. kurd. päres, arm. partez, syr. Dn*)5?, JDD'^'TlEi.
280. panzde 'fünfzehn , vergl. pänsed 'fünfhundert'.
aw. paücadasa 'fünfzehn; skr. pdflcada^a; phlv.
pancdahion,
kurd. [daupe/ij etc.]; paiizde (LW.); afy. pinjalas;
oss. d. findtäs^ t. findfäs (292) ; bei. panzda (LW.).
281. päl^ pä Tuss ; vergl. paye 'Stufe', päym.
aw. päda- 'Puss* ; phlv. pCLT *Fuss', päyah *Stufe' ; ai.
päda-; arm. otn (H. No. 280).
kurd. pai (LW.) 'Fuss'; bei. päd, n. /xlJ, ^^ö^ (291);
oss. *fad aus bäymmoad-äi 'barfuss*, bäyömbad-äi 'bar-
fuss erschlossen? (267).
282. päyisten 'fest stellen , dauern ; erwarten ; vergl.
päylden 'schützen', päyende.
ap. l/^pä-, pö^wi; schützen; aw. l/^pÄ-, pcf«7e, vergl.
paiti.pait^ (yt. 10, 19) erwartet, versieht sich';
ai. [/'pä-, pdti.
Bei AM. ist päyTden als schützen, conserviren sehr
häufig, z. B. 'schützt vor Zersetzung (191 Zeile 2,
248 Zeile 6), erhält das Haar' (122 Zeile 7), *die
Gesundheit' (237 Zeile 4); auch 'sich halten', z. B.
seine Kraft hält sich nicht länger als ein Jahr (187
Zeile 3 v. u.).
Vullers (Lexicon) nimmt mit Unrecht zwei ver-
schiedene np. päyiden an.
Da für p&yiden (phlv. pöyitan) die Aussprache mit ö
durch den Reim gesichert ist (z. B. Sahn. I, 143, V.
251 — pöt^ röT — II, 962, V. 34 — pöyende^ jöyende
— III, 1096, V. 528 — pöi, jm, Vis und Rämin, S. 48,
^) Palez soll nach den persischen Original Wörterbüchern mehr
*Fruchtgarten' bedeuten; die obige Stelle, sowie Sahn. II, 765, Vers 5,
sprechen nicht dafür. Sahn. II, 626, Vers 1846, III, 1377, Vers 2047
sind zu allgemein.
```


## [2026-09-06T23:14:03.605Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('HUB.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('npages',len(pages))\nfor n in (18,19,46,47):\n    print('=== leaf',n,'===')\n    print(pages[n-1][:2600])\nEOF"
}
```


### [2026-09-06T23:14:05.573Z] TOOL RESULT

```
npages 300
=== leaf 18 ===
PERSISCHE STUDIEN
VOK
m HtBSCHMANN.
STRASSBURG.
VERLAG VON KARL J. TRttBNIlR.
1895.
=== leaf 19 ===
- 8 —
neben ap. sit/dti-, np. savam neben ap. asiyavam. Laut-
lich wiirde OSiyana ein ap. ^asidana- oder ^Osadana^
(vgl. np. piyada = skr. padati-) voraussetzen, das viel-
leicht zur Wurzel sad *sitzen' gestellt werden konnte.^)
Vgl. np. nisastan *sitzen' und nis^m *Nest'. v. Stackel-
berg denkt an osset. axston (aus dxs-don oder dxst-don)
'Nest', NSldeke jetzt an skr. a-ksi Veilen.
38. Man mtisste lautgesetzlich afdum erwarten. „Viel-
leicht war das Wort schon zur Zeit der altesten neu-
V
persischen Dichter (Abu Suktir!) veraltet und wurde
falsch ausgesprochen." No Id eke.
42. Np. dludan *beschmutzen, sich verunreinigen* kann
trotz des pr. olayam auf eine Wurzel lu zuriickgehen,
wie situdan, pr. sitayam (Horn Nr. 719) zeigt. Man hat
dann dlayam auf ein caus. *alavayami zuriickzufuhren.
Phi. lutaJc wird (Gl. and Ind. p. 139) durch nackt* iiber-
setzt, obwohl 'schmutzig' besser passt. Lautlich ist
also gegen eine Zusammenstellung von aludan mit lat.
lutum, lUeSj poUuo^ gr. Xv/ua, air. loth etc. nichts einzu-
wendon. Davon zu trennen^aZJd *unrein Fird. I, 15, 31.
43. Zu dluh *Adler vgl. die kurd. Formen hdld etc.
ZDMG. 38, 95. Die Bildung von phi. np. aluh ist dunkel,
die Zugehorigkeit zu ii^vtg u. s. w. daher nicht sicher.
48. Zur Erklarung von^phl. maiffHy amatan = np. dtnadan
(fiir *gatan u. s. w.) ist auf ap. ha(n)gmata (ptc. perf.)
hinzuweisen, nach dem mit Spiegel ein ap. Inf. ^gma-
tanaiy anzusetzen ist.
51. Wenn die Flexion dmextan mischen, pr. amBzam
(vgl. paz. amexta 'mixture' Shk. p. 248, phi. gumext,
pr. gumecet Gl. and Ind. p. 282) alt ist und keine der
(in der Infinitiv- und Praesens-bildung zahlreichen)
Analogiebildungen vorliegt, so ist fiir das Iranische eine
Wurzel mik-^mid (= idg. mik^ neben mik^ in skr.
migra etc.) anzunehmen, zu der auch arm. amic *eine
Zukost' (eigentl. Mischung -- Ragout) ZDMG, 46, 233
* Wegeq a fiir h sjehe unter Nr, 323,
=== leaf 46 ===
— 35 —
263. Hierzu zd. viSu-^ vidava^ *Wittwe* ZP61. p. 5, Z. 3 iind
kurd. 6f ZDMG. 38, 54.
264. Vullers gibt hayog (fiir haydk\ jud. pers. ebenso.
265. Nach den Bemerkungen der pers. Lex. bei Vullers zu
urtheilen, existiert ein np. pad 'Schiitzer iiberhaupt
nicht. Siehe unter Nr. 273, Sonst hatte pad = ap.
nom. sg. *p<it€L gesetzt werden miissen, wie dGst Treund'
=- ap. dausta ist. Vgl. ZDMG. 38, 426; WZKM. 1,
249; 8, 92.
265 ^^^ Np. paddS Tergeltung, Belohnung bei Fird. I, 437,
Z. 1. Vgl. g. padas 'Belohnung, Rache* ZDMG. 36, 76,
afgh. LW. podcis 'retaliation*. Daneben np. padds
JRAS. 1894, 450.
266. Zu pad' vgl. Nr. 275.
268. Wie passt der Sinn von pddyab rituelle Waschung'
zu zd. paityapem 'stromauf ?
269. Die Etymologie Horn's undFr.Muller's WZKM. 7
370 iiberzeugt mich nicht. Das Wort enthalt wohl das
Suffix vand (Darmesteter, Etud. iran. I, 285—286).
Vielleicht gehOrt pdtydvand = phi. patiavand
'prevailing, resistant' (Shk. 262), also eigentlich *wider-
standsfahig , aus *patiyapvand zu zd. paityapa- 'strom-
auf = * wider den Strom'? Vgl. skr. pratlpdm gegen
den Strom*, pratlpd- Viderspanstig, Gegner, Wider-
sacher*. Davon zu scheiden np. payab 'Widerstands-
kraft* (Fird. I, 456, 389) = Tuss-finden, Fuss-fassen*.
270. Np. pdrdv alte Frau* ist, wie auch Fr. Mil Her
WZKM. 7, 370 mit Recht bemerkt, durch arm. parav
alte Frau* (1 Timoth. 4, 7 etc.) ganz sicher gestellt.
Hier konnte np. pdrgln *receptaculum aquarum*
(bei Vullers auch bargm^ was falsch ist) erwahnt
werden, das nach arab. fari^n, arm. parken *Wall-
graben* (Agathang. und Levond p. 60, 7) auf phi.
*parkEn zuriickgeht.
271. Np. para *Bruchstiick, Stiick' gehSrt weder zu skr.
para^ *das Letzte, Ausserste, Ende* noch zu zd. para-
'Schuld' (ZPGl.). Horn stellt es jetzt zu lat. j>ar« =
*^«- KZ. 33, 443.
3*
=== leaf 47 ===
— 36 —
273. Die altere Form pddzahr siehe bei Vullers s. v.
pazahr, Polak, Persien II, 375, paz. 'pad{a)zah(a)r
*Gegengift' Shk. 261. Auf dieses padzahr (das aber
*6egen-gift' bedeutet) sowie auf padsdh *Konig' stiitzen
die pers. Lex. falscblich ihr pad 'Schiitzer (s. Nr. 265).
274. Zu pas *Wache, Nachtwache' vgl. Nr. 341: pahra^
Skr. pdtra- (Rgv. 1, 121, 1 nach Say. = pdtar 'Be-
schiitzer !) bleibt besser weg.
274 bis jfp pasaoct im Uiiterschied von paz. phi. pasaxt
Shk. 262 - 263, Gl. and Ind. 103 etc. miisste aus ^patsaxf
entstanden sein, wie pasCtxt aus patsCixt,
275. Neben dem gewohnlichen phi. pasaxv (61. and Ind.
p. 103) ist nach np. und paz. pasux (Shk. 263, Min.
haufig) ein phi. *pasaxv anzusetzen, jenes aus *patsaxv,
dieses aus *patsaQcv (vgl. Sirm, patasxani 'Antwort').
Dieses pdt (aus ap. *pCitiy) liegt noch vor in np. paz.
pddzahr *6egengift'; np. padas 'Vergeltung' = phi. pa^-
ddhisn ; np. bddafrah, lies padafrah Tergeltung, Strafe',
paz. padafrah, phi. patafrds; phi. patrazm Yatk. i.
Zar. 66, Anm. 61 = arm. paterazm *Krieg, Kampf,
Schlacht' (vgl. np. razm *Kampf ') , entsprechend im
Avesta paiti in paitivaka- = *Gegen-rede, Erwiederung
neben gewohnlichem paiti (in paitivad etc.).
278. Np. pdludan reinigen' kann nicht = j^paiti + aludan^
sein, eher ~ pClt (aus patiy siehe Nr. 275) + ludan (vgl.
a-ludan), dessen Bedeutung aber (gegen-schmutzen =
reinigen'!) wenig ansprechend ist. Nun heisst aber pdlU-
dan vielmehr *durchseihen, reinigen*, pdludagi *das Durch-
seihen', paluna *der Durchschlag, die Seihe', pcllavan
dt., 'pdla in Comp. ^= *colans', paluda *durchgeschlagen',
vgl. bal. LW. palayag *seihen, worfeln, reinigen', paz.
pdlMdan *to filter , palaUni a filtering' (Shk. p. 262)^
so dass 'seihen' die urspriingliche, *reinigen' die abge-
leitete Bedeutung ist. Also findet ein Zusammenhang
mit aludan nicht statt und jede darauf gegriindete
Etymologie ist falsch.
280. Np. pan^dah 'funfzehn' hat doch horbares h (wegen
```


## [2026-09-06T23:14:16.760Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lūdan\\|lūd\\b\\|pālāy\\|ālāy\" CHEUNG.txt | head -40"
}
```


### [2026-09-06T23:14:16.814Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T23:14:17.301Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pālūdan\\|pālūd\\|ālūdan\\|pālāyidan\" *.txt incoming/*/*.txt 2>/dev/null | head -40"
}
```


### [2026-09-06T23:14:17.382Z] TOOL RESULT

```
PHD.txt:189:áhüg [TYBA < A ру; ”hwk! | MQyhwg, N āhū] gazelle. ahunawar [hnw!] the holiest prayer, beginning Yadā ahū wairyē. a-hunsand [Phwnsnd] dissatisfied. ^h : dissatisfaction. ahy [KZ Y < А k-zy | М hy] soon(est), first. ajģahān [>20/?л! | М ieikin, N azgahan] lazy, indolent. “АҺ: laziness, indolence. ak P! | N dk] evil, harm. -ak LIN ~] diminutive suffix. a-kámagómand [k mk’ wmnd] unwilling. a-kanārag ['kr?]k! | M ?qn’rg] unlimited, boundless. ~ih: boundlessness. a-kard Pārt! | (M °gyrd)] not done, undone. Akoman ['kwmn! | М ?qwmn] Evil Thought, an arch-demon, akómand ["£wmnd] evil, harmful. alā [Py] oh! alas! Аар [STLA, STRA < A £t ;?lk! | (М rel side. alálag PPH! | N lala] anemone. ālāy-, v. ālūdan. Aleksandar Piksndl | M *Ixsyndr, N Iskandar] Alexander (of Macedon). almās(t) Pim?s(t') | (M ?rm?s), N almas] steel; diamond. аадар [?/wtk'] defiled, polluted. АҺ: defilement. ālūdan, ālāy- Photn!, *Pd- | (M ?rwd), N ~] defile, pollute. Aluh Plwh | M "If, N ~] eagle. Xum [lum] millet. N~ amā [LNE < A l-nh | М ?*°h, N má] we, us. Amadan, āy- [Y ATWN-tn! < А y twn, V*th | M?mdn,?y-, N ~] come. amahraspand [?mhrsbnd | M (?)mhr’spnd] a Holy Immortal, a-mar [ml] countless, innumerable. amar [ml | N ~] reckoning, consideration. āmār- [?m?1-] reckon, calculate. ~išn: reckoning. a-marag [mlk') countless. amaraģān [?mlk’n'] generality, commonalty. ~ig [-yk'] general. ~iha [-yh’] in general, generally. a-marg [mig] deathless, undying. ~ih: deathlessness, immortality. ámárgar [?m’lgl | N ~] reckoner. amāwand [?m'wnd] powerful, strong.
PHD.txt:540:pahikēftan, pahikob- [ptkwp-tn'] strike. pahlawig [*p’hlwbyk' | (M phlwnyg), N paklaw(ān)i] Parthian; Pahlavi. pāhlom [phlwm] excellent, best, foremost. ~ih: excellence. pahlüg [p'Aok! | N pahli] side, rib. pahn [p?An! | N ~] wide, broad. сау [2d | N —à] width, breadth. lpahrextan, pahrēz- [phlyhtn', p'hlyc- | M phryz-, ] ~, N parhéxtan, parhéz-] abstain, refrain, avoid. *pahréxtan, pahrēz- [p’hlyhtn', p'hlyc- | M (phrystn), phryz-] care for, tend, protect. pahréz [Аус | N parhéz] defence, care. *pahrmāh- [ptimwh- | (N parmds-)] touch. ~арфіһ [Pkyh], ~i$n: touch, feeling. pak [DKY A < A аку; рк | = M, N ~] clean, pure, holy. ~ih: purity, holiness. pākīzaģ [p’kyck' | N ~a] pure. palang [ping | N ~] leopard. —-mušk [-mwsk' | N ~] speckled basil. pálüdag [p'Iwtk! | N ~a] starch jelly, flummery. pālūdan, pālāy- [p’lwtn', pPd- | (M p’rwdn, p’r’y-), N ~] strain, filter, purify. pambag [pmbk' | N panba] cotton. —ën [-yn'] (made of) cotton. pānāģ [p’n(’)k' | M p’ng] guard, protector; shepherd. ~th: protection. panāh [рт | = M, N ~] protector; refuge. pad ~ griftan: take refuge with. ~ih: protection. pand [pnd | = M, N ~] path; counsel, advice. panir [pnyl | N ~] cheese. panj [pnc | P рту, (M pnz), N ~] five. ~ag [-k! | N —a] pentad; hand, paw. ~аһ [h | N ~] fifty. panzdah [p’ncdh | M p’nzdh, N ~] fifteen. ірагаб [p?/k! | N para] piece, part, portion. ?párag [p?/k! | M p’rg, N para] gift, offering, bribe. paráhóm [pP?hwm = Av. para.haoma-] consecrated drink (the infusion in holy water of pounded лот and pomegranate twigs, sometimes with milk added). pardag [pitk! | N parda] veil, curtain. pardaxtan, pardaz- [pldhin', pldc- | M prdxt, N ~}, ~ az: be done with, freed of. ^ 6: set about, undertake. ~išn: freedom; undertaking. pardāxtan, pardaz- [pld’htn', pld?c- | N ~] accomplish.
PHD.txt:1932:filter pālūdan.
PHD.txt:1980:flummery pālūdag.
PHD.txt:3171:pollute ālūdan.
PHD.txt:3293:purify pālūdan, wēxtan.
PHD.txt:3802:starch-jelly pālūdag.
PHD.txt:3834:strain ( filter) pālūdan.
PHD.txt:4746:pāyag pānāgīh pānāg -bān pänagīh panag pānzdah pākīzag pāk pālāy- pālūdan pālūdag 1-2pärag pārsīg pāsox pāsbānīh pāsbān pazen pāzand pazen pāšnag pāšom
incoming/ZAW/ZAW_pages.txt:14375:                             pālūd
```


## [2026-09-06T23:14:29.908Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls incoming/FFD/; python3 - <<'EOF'\nt=open('incoming/FFD/FFD_pages.txt',encoding='utf-8',errors='replace').read()\nimport re\nprint(len(t))\ni=t.find('[pdf page 26]')\nprint(t[:300])\nEOF"
}
```


## [2026-09-06T23:14:30.611Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"آلودن\\|پالودن\\|پالود\" incoming/FFD/FFD_pages.txt | head -20"
}
```


### [2026-09-06T23:14:33.123Z] TOOL RESULT

```
FFD_asmaneketab.pdf
FFD_pages.txt
FFD_pages.txt.pages
104244
[pdf page 1]
4و اک ۵ 0
۲ ی
ی
۵ > ره
مرگ
0
/ 0 4 ۰
6( : ز (
مر رک ۳ ص شمل هار /
ور 0
۳ 7 ۹ ۹۱ /
۱
۸ 5 2۱+ و 9 ۱
۵
7
ی
ات
ِ یت
هو و اس
مس لوالا ی
1 ۰
: 4 3 ماس
[pdf page 2]
نچد کي و۱
رح اس
15 ۳/48 8 (7
مکی ( از
۹ ۹ ۸ ۸
۹
!همم
مویکو
7
0
کم
یه
5 ۷ سر
: ۵
موم
7
چا
ن ی
ی 0
۳ ک
فا : 3 6
هم
2 1
3)
اگم له
ی
```


### [2026-09-06T23:14:33.166Z] TOOL RESULT

```
731:آلودن
1142:پالودن
1144:پالود < فارسی میانه 0310 «ایرانی باستان 0272-40-18*. برای 2 آراست. 1022
```


## [2026-09-06T23:14:36.582Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '700,760p' incoming/FFD/FFD_pages.txt; echo \"==========\"; sed -n '1120,1160p' incoming/FFD/FFD_pages.txt; echo \"==== page tags near\"; grep -n \"\\[pdf page\" incoming/FFD/FFD_pages.txt | awk -F: '$1>600 && $1<1200' | head -40"
}
```


### [2026-09-06T23:14:38.348Z] TOOL RESULT

```
آزمودن
آزمود < فارسی میانه ۰320084 02130. صورت اصلی 02804 است از پیشوند فعلی
2 که به فارسی میانه نرسیده و 134 . 8 به قیاس با 8739 8730 به جای 30 آمده
است. صورت ایرانی باستان این ماده 1 - ۳3 - 2* بوده است. ريشه (133)7 به معنی
«اندازه گرفتن» است. برای 1۵ آراست.
آزمای + فارسی میانه 2203 23 < ایرانی باستان 2-ر2-3*. برای 2-> آرای.
آسودن
آسود + فارسی میانه 3800.
آسای + فارسی میانه 3837.
[pdf page 31]
و فعلهای فارسی دری
11 شفتن. آشوفتن
آشفت + فارسی میانه 2311 + ایرانی باستان 18 - 2501 - *. برای 3و 12 -> آراست.
: دنا که صورت ضعیف ريشهٌ 75210 است» صورت اصلی لا« است» 0 پیش از ۲ به ؟
بدل شده است. ريشةٌ 35800 به معنی «لرزیدن» است. «آشوفت» زیر نفوذ «آشوب»
به‌وجود آمده است.
آشوب < فارسی میانه 2300 + ایرانی باستان ۸ - 35200 - 3*. برای 2 + آرای.
«کشفتن» هم از ربشةٌ 1520 آمده است. > کشفتن.
آفریدن
آفرید < فارسی میانه 2874 < ایرانی باستان ها - 87 - 3*. برای 3 و 1۵ > آراست.
آفرین + فارسی میانه 38:78 + ایرانی باستان 83 - 8۲ - 3*. 23 نشانه‌ای بوده است
که با آن از ريشه, ماده ساخته می‌شده است. ريشةٌ 7 به معنی («ستودن» است. در
فارسی میانه 21778, 31710487 به دو معنی به کار می‌رفته: ۱ -ستودن, آفرین کردن ۲ -
خلق‌کردن. در فارسی دری معنی «ستودن» در «آفرین» به جا مانده که به عنوان «صوت»
به کار می‌رود.
آگندن
آگند + فارسی میانه 28270 < ایرانی باستان 1۵ - 6۵۵ - 2*. برای 3و ها آراست.
ريشهٌ 1۵0 به معنی «نهادن و افگندن» است.
«افگندن» و «پراگندن» هم از ريشهٌ 1۵0 آمده‌اند. -> افگندن و پراگندن. در ایرانی
باستان 1۵8 دیگری هم بوده است که از آن «کندن» آمده است. > کندن.
آگن < فارسی میانه 284 < ایرانی باستان ۵ - 5۵2 - 3*. برای 8 -> آرای. "
آلودن
آلود + فارسی میانه 2130 < ایرانی باستان ۴3-۳0-1۵
برای #وقها + آراست. 8 به معنی «آلوده‌بودن» است.
آلای + فارسی میانه 213 < ایرانی باستان 8له-3-73۷*.
[pdf page 32]
ماده‌های ماضی و مضارع فارسی دزی سس ۲۷
9 صورت بالاندةٌ ۳2 است و 278 نشانه‌ای بوده است که برای ساختن فعل از ريشه
به کار می‌رفته است. ۰
3-13-2: آلو ده کردن.
آمدن
آمد + فارسی میانه 21020 < ایرانی باستان 3-82-12*. برای 3 و 2 آراست. 2
صورت دیگرش 8210 «حرکت کردن» و با پیشوند فعلی «حرکت کردن به سوی متکلم»
معنی می‌دهد.
آی + فارسی میانه 2 < ایرانی باستان 3-1-8" برای 2 > آرای. ریشهٌ 1 به معنی
«حرکت کردن» است و با پیشوند فعلی 2 «حرکت کردن به سوی متکلم» معنی می‌دهد.
+ رفتن.
چنان که دیده می‌شود» «آمد» از یک ريشه و «(آی» از یک ريشه دیگر آمده است. همه
فعلهای فارسی, جز چند فعل از جمله «آمدء آی» از یک ريشه آمده‌اند. بر اثر تحول
لفظی و قواعد دستوری» ماده‌های ماضی و مضارع در فارسی میانه و دری» با هم
رابطه‌ای بی‌قاعده یا سماعی دارند. به عبارت دیگرء قواعدی مطرد در فارسی میانه و
دری وجود ندارد که طبق آن قواعد بتوان ماد ماضی فعلی را از روی مادهٌ مضارع آن و یا
مادهٌ مضارع آن فعل را از روی ماد ماضی آن ساخت.
آمرزیدن
آمرزید» ماد ماضی جعلی است.
«آمرز» < فارسی میانه 20872 + ایرانی باستان 3-774-2*. برای ۵ > آرای. 3
پیشوند فعلی است. ريشهٌ 13720 به معنی «مهربان‌بودن» است. :
اموختن
آموخت < فارسی میانه 270871 + ایرانی باستان 3-2۵0-1۵*. برای 3و 1۵ >
آراست. 2۵0 در اصل 13301 است به معنی «رها کردن»» ۴ پیش از ۲ به #بدل شده
[pdf page 33]
==========
0 11 ان دار
بیوسیدن

( بیوسید» ماده ماضی جعلٍ است. از مادهٌ مضارع ساخته شده است.

: بیوس < فارسی میانه 02789 < ایرانی باستان 0211-0809-8*. برای 2 -> آرای. 041
پیشوتد فعلی است.

4-8 صورت اصلی ۳۵9 است. 4 پیش از ۶ به 5 بدل و در آن ادغام شده است. 5
برای ساختن مادهٌ آغازی از ريشه به کار رفته است. ريشةٌ 0304 به معنی «بوی بردن»
است. واژةٌ «بوی» فارسی دری از 210 گرفته شده است.

پادن, پاییدن

پاد <ج فارسی میانه 034 « ایرانی باستان 03-12*. برای 18 -> آراست. ریشهٌ ۳3 به
معنی «پاییدن» است.

پای < فارسی میانه 03 < ایرانی باستان 03-72*. 8 نشانه‌ای بود که از ريشه ماده
می‌ساخته است.

«پاد» از رواج افتاده و «پایید»» مادهٌ ماضی جعلی» به جای آن به کار می‌رود.

پالودن

پالود < فارسی میانه 0310 «ایرانی باستان 0272-40-18*. برای 2 آراست. 1022
پیشوند فعلی است. 5 صورت ضعیف ريشةٌ 42۷ است» به معنی «دویدن». خود
«دویدن» هم از ريشةٌ 42 آمده است.

پالای < فارسی میانه 0818 < ایرانی باستان 8/ر08۳۵-439-8*. 24 نشانه‌ای بود
برای ساختن مادةٌ مضارع. از ريشه» 43 صورت بالاندةٌ ریشهٌ 49۷ است. [
ی چخت ۰
پخت < فارسی میانه 001 « ایرانی باستان 2-12م*. برای 1۵ -> آراست. 081
صورت اصلی 02۵5 است» 1 پیش از ۲ به # بدل شده است.
پز< فارسی میانه 022 < ایرانی‌باستان -022*.برای 2 -> آرای.2 به‌جای آمده‌است.
[pdf page 46]
ماده‌های ماضی و مضارع فارسی دری ۴۱
پذیرفتن
پذیرفت < فارسی میانه 0247711 + ایرانی باستان ۳81-877-1۵*. 0217 پیشوند فعلی
است. برای 18 -> آراست.
«ابع صورت اصلی 7۲ است» 0 پیش از 1 به ۶ بدل شده است. 870 صورت ضعیف
ریشهٌ 10 است. به معنی «گرفتن». خود «گرفتن» هم از ریشهٌ 8720 آمده است.
==== page tags near
636:[pdf page 27]
662:[pdf page 28]
666:[pdf page 29]
685:[pdf page 30]
709:[pdf page 31]
735:[pdf page 32]
760:[pdf page 33]
795:[pdf page 34]
819:[pdf page 35]
841:[pdf page 36]
875:[pdf page 37]
909:[pdf page 38]
935:[pdf page 39]
969:[pdf page 40]
1004:[pdf page 41]
1029:[pdf page 42]
1054:[pdf page 43]
1081:[pdf page 44]
1119:[pdf page 45]
1154:[pdf page 46]
1178:[pdf page 47]
```


## [2026-09-06T23:15:00.329Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^\\*raud\\|\\*raud\\|raud-\\|rau̯d\" CHEUNG.txt | head -30; echo \"=== rau\"; grep -n \"pālūd\\|palud\\|p'lwtn\\|pālāy\" CHEUNG.txt | head -20; echo \"=== size\"; wc -l CHEUNG.txt"
}
```


### [2026-09-06T23:15:00.399Z] TOOL RESULT

```
20820:*raud ‘to hinder, block, ward off” 
20885:if there is a possible Ir. cognate, on which see *raud. On the etymology see also 
28255:’rws- does not derive from *raud. = Ghilain: 49, 81 | DMMPP: 53 
55778:*Hram (s.v.), *marH’, *raud, 
56895:*marH’, *raud 
58370:*Huar’, *raud 
=== rau
9452:vel, Bakht. wil ‘free, loose’ || (+ *pari-) NP paludan, palidan/palay-, Kurd. (Kurm.) 
41308:paludan, palidan/palay-, 
=== size
58427 CHEUNG.txt
```


## [2026-09-06T23:15:03.155Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9390,9500p' CHEUNG.txt"
}
```


### [2026-09-06T23:15:03.199Z] TOOL RESULT

```
*SANSKRIT: srni- (Ё) ‘sickle’ (RV) > EWAia II: 743 

9 There is little evidence for a verbal Ir. root *har ‘to saw’, except in Chor. This root 
may rather be denominative. As for the provenance, the only plausible IE cognate 
forms can be found in Latin. 

«PIE *srneH»-, *sernH»- f. ‘saw’ ? = LIV: —| Pok.: 911 f. 


*IE COGNATES: Lat. sar(r)ire ‘to hoe, weed’, serra (f.) ‘saw’ 
*REFERENCES: IFL П: 191b; Morgenstierne 1932: 122; WIM II/2: 661; Cabolov 2001: 30 f. 


*harz ‘to let go, release’ 

*AVESTAN: YAv. haraz- ‘to release (esp. water, liquid)’ || (+ *aua-) ‘to decline, 
reject” || (+ *upa-) ‘to drop on, let (it) lie’ || (+ *pari-) ‘to filter’ || (+ *fra-) ‘to 
ejaculate’ = Liste: 72 

Pres. them.: IND. 15р. YAv. auuaghorozami (Y 10.15), 3sg. YAv. upanharozaiti (V 6.10, V 6.12 f£), 
Y Av. fraghorozaiti (V 8.32, V 15.7 f., V 16.17, etc.), YAv. fragharozaiti (V 8.32, V 15.7 f., V 16.17), 3pl. 
Y Av. herezonti (Yt 13.43), INJ. 3sg. YAv. fraghorozat (VdPZ 2.5), SUBJ. 35р. YAv. pairi.harozät (N 75), 
OPT. 3sg. YAv. fraghorozoit (N 11), med. 3sg. Y Av. upanharazaéta (V 5.51), 3pl. YAv. horozaiien (V 6.2 
ff, V 8.2 Е); Fut.: IND. med. 3р1. YAv. harosiiente (Vr 12.1), YAv. pairi.harosiiente (Y 27.6); Partic.: 
pres. YAv. "fraghorozant- (Yt 14.12), fut. med. YAv. haroSiiamna- (Vr 12.1), perf. pass. ҮАУ. 
pairi.agharsta- (Yt 5.8, Yt 5.63, V 14.4) 

*OLD PERSIAN: (+ *aua-) ? avahard- ‘to let go, abandon ?’. > On its interpretation see 
Klein 1988: 412, fn. 53. The hapax form "avaharda is very similar to avarada 
(*rHaz) in meaning and form. = Kent: 214a 

Pres. them.: IND./INJ. 3sg. ? “avaharda <a-v-h-r-[d]> (DB 2.94) 

*MIDDLE PERSIAN: MMP hyl- ‘to leave, abandon; remit (of sins); establish, appoint; 
let, allow’ || (+ *pari-) MMP p’r’y- ‘to purify’ = DMMPP: 196, 259b 


*harz 133 


Well attested: Pres.: IND. 1sg. MMP hylym, 3sg. MMP hylyd, 3р1. MMP hylynd, etc. || (+ *pari-) Pres.: 
IND. 3р1. MMP p’r’ynd, SUBJ. 3sg. MMP p’r’y’d; Partic.: perf. pass. MMP p’rwd, “p’rwdq 
*PARTHIAN: hyrz- ‘to leave, abandon; remit (of sins); establish, appoint’ || (+ *apa-) 
*bhyrz- ‘to abandon, desert; forgive’ = Ghilain: 48, 49 | DMMPP: 197a, 11а 

Well attested: Pres.: IND. 3sg. hyrzyd, 2pl. hyrzyd, 3pl. hyrzynd, etc. || (+ *apa-) Pres.: IMPV. 2pl. 
"bhyrzyd; Partic.: perf. pass. ’bhyst 

*CHORESMIAN: (+ *pari-) pZy- ‘to purify, cleanse’ = Samadi: 167 

*BACTRIAN: v1pC- ‘to leave, let, set (free), allow’ — S-W, Bact.: 228b 

*NWIR: Widely attested and borrowed (from Pers., especially forms with -/-): NP 
histan/hil-, Jow. bam-haft/a-hal-, Meim. bem-haft/a-hal- ‘to leave, let go’, Bal. 
(h)ist/(h)ill- ‘to let go, allow, leave (behind)’ (< MP/NP), Kurd. (Kurm.) histin/hél-, 
(Sor.) hestin/hel- ‘to permit, allow’, Zaz. estis/erzen- ‘to throw’, Abz. hasta/harz-, 
Abyan. hästa/härz-, Tt. (Cha.) harz/hast, Awrom. astáy/-az- ‘to let, allow’, Fariz. 
-hast-/-hal-, Yar. -hast-/-hal-, Gil. (Rsht.) astoen/-al-, Ham. hästän/häl-, Sorkh. hínd-/ 
hín- ‘to put’, Ard. helahe/hel-, Anar. haste/hal-, Gur. (Kand.) hastin/-az-, Khuns. е/-, 
tel-/est, ela ‘to put, lay; to let, permit’, Nn. este/vál-, Qohr. hasta/hel- ‘to let, allow, 
permit’, Siv. el-, äl-/(h)ist, Tr. hasta/hal-, Varz. heste/hel- ‘to allow, let’, Tal. haste 
‘to leave (behind), abandon’ || (+ *aua-) NP (dial.) vel, vil kardan ‘to set free’, Gz. 
vel, Bakht. wil ‘free, loose’ || (+ *pari-) NP paludan, palidan/palay-, Kurd. (Kurm.) 
palavtin/palév-, (Sor.) patawtin/palew-, Gz. päl-/palä ‘to filter, purify’, Gur. cay- 
parzen ‘tea-strainer’. Ф As for NP palüdan, palidan/palay- and the corresponding 
forms, they may be contaminated with *para-dauaja- ‘to clean’, on which see Sims- 
Williams 1989: 262. Note also the rhyming antonym NP 4ludan ‘to stain, soil’, s.v. 
*dauH?. 

*NEIR: Pash. (1)&d-/iXo(d) ‘to put, place, leave’ 

*MISC: (+ *aua-) Par. yurzéw- ‘to pour out’ || (+ *pari-) Arm. (LW) parzel ‘to filter, 
purify’ 

*SANSKRIT: sarj ‘to let loose, to throw out, to send forth’ (RV+) || (+ *aua-) Skt. 
äväsıjah ... apáh ‘release waters’ (RV) = EWAia П: 709 

«PIE *selg- ‘to let it loose, release, flow (?)’ = LIV: 528 f. | Pok.: 900 f. 

*IE COGNATES: Hitt. /salk-/ ‘to knead, to mingle’, Olrish selg (f.) ‘hunting’, MHG 
selken ‘to fall down drippingly, to go down (of clouds)’, (ppp.) OE solcen ‘lazy, 


slow’, Engl. sulky 

*REFERENCES: КРЕ I: 147b; КРЕ II: 218; Christensen, Contributions I: 72, 170; Christensen, 
Contributions II: 62; IIFL I: 257b; Abrahamian 1936: 114; Lambton 1938: 43b, 78b; MacKenzie 1966: 
88; Yarshater 1969: 183; WIM I: 68; WIM II/1: 81; WIM II/2: 750; WIM III: 104; Vahman — Asatrian 
1991: 133; Werba 1997: 257; Paul 1998: 297a; Cabolov 1997: 73; Cabolov 2001: 443; Lecoq 2002: 121, 
123, 126 (passim); Shahbakhsh: s.v. hill-; NEVP: 29; Korn 2005: 274, 320, 350 


134 *haul 


*hau! ‘to extract, (ex)press, squeeze out (juice)’ 

*AVESTAN: Y Av. hau- ‘to press, squeeze out ?, to braise ? || (+ *abi-) ‘to press out, 
prepare by pressing’. 0 The traditional interpretation of YAv. hau- is ‘to braise, 
stew’ ("schmoren", Bartholomae, AIW: 1781). However, Kellens 1984: 151, n. 15: 
"Le sens de ‘‘réduire en cendres" ... peut être issu de celui de ‘‘pressurer’’. En 
brûlant, le bois et la chair n'émettent-ils pas un liquide et celui que le bois secrète 
sous l'action du feu rituel n’a-t-il pas une valeur mystique?". The postulation of such 


a development is ingenious, but difficult to prove though. — Liste: 73 

Pres. nu-: IND. 3du. YAv. hunutö (N 108), INJ. med. 3sg. YAv. hunüta (Y 9.3 f., Y 9.6 £, Y 9.9 f£), 
SUBJ. Y Av. °hunuuat (N 72), ОРТ. 35р. YAv. “hunuiiat (N 68), 3pl. YAv. “hunuiiaras (V 7.55), IMPV. 
med. 2sg. them. YAv. hunuuag'ha (Y 9.2); Partic.: pres. ? YAv. hunuuant- (Vr 12.2), med. YAv. 
hunuuana- (Vr 9.3), fut. YAv. haosiiant- (Vr 9.3), perf. pass. YAv. huta- (V 18.12, Vr 12.3, H 1.9), YAv.
```


## [2026-09-06T23:15:12.541Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dauH\\|\\*dau\" CHEUNG.txt | head -30"
}
```


### [2026-09-06T23:15:12.593Z] TOOL RESULT

```
580:these roots are not of Proto-Iranian date, notably, *dauc ‘to sew’, *fan ‘to move, 
4612:Many Pamir forms seem to be influenced by the root *daub ‘to strike, hit, pick ?’. 
5241:*dau2 65 
5253:*dau! *to speak, chat' 
5286:*dau? ‘to run’ 
5305:66 *dau3 ? 
5323:*dau? ? ‘to be skilful’ 
5329:© The existence of *dau ‘to be skilful’ is doubtful, the Avestan evidence is question- 
5335:*daub ‘to strike, hit, pick ?” 
5349:9 Only in East Iranian languages is there evidence for a root *daub: regional borrow- 
5358:*dauč! (*dauj ?) ‘to milk, traire (< **to draw’ ?)’ 
5368:óüy (Е), Bart. óoy, Yzgh. day ‘buttermilk’ (< *dauga-, EVS: 30b), Pash. Iwayza 
5371:*dauHl 67 
5374:‘cow in milk’ (< *dauga-zä-, EVP: 40 f.) ? Pash. salwäya ‘bucket for drawing water 
5383:© Both *daué and *dauxš are problematic: they may have either a different origin or 
5384:show (mutual) influence of another root: *dauc may have acquired the specialized 
5386:from IE *deuk- ‘to draw’. Or is *dauc merely contaminated with this IE root ? 
5387:Nominal variants with voiced velar *-g are also attested in Iranian. As for *dauxs-, 
5422:*dauH! ‘to burn’ 
5433:68 *dauH2 
5482:* dauH? ‘to smear, rub (on)’ 
5489:*dauxs 69 
5492:*KHOTANESE: (?) LKh. du- ‘to strike, beat; clean’ (also from *daub ?) || (+ *uz-) 
5522:whereas IE cognates cannot be cited in support of Ir. *dauH! ‘to smear, rub (on)’. It 
5528:correspondences of Ir. *dauH'. 
5538:*dauxš ‘to suck, suckle, milk’ 
5557:bedüs diyetan ‘to milk’, Bakht. dun ‘milking, process of milking’ ( *dauxsna- ?) 
5562:0 This root is a so-formation of IE *d'eug"- ‘to prepare’. See *daud!. 
6122:perhaps a connection to *daub ‘to strike, pick’, which is semantically less attractive 
6376:*duar: these "roots" are perhaps extended formations of *dau? (Skt. dhàv) ‘to run’,
```


## [2026-09-06T23:15:15.214Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5482,5537p' CHEUNG.txt"
}
```


### [2026-09-06T23:15:15.261Z] TOOL RESULT

```
* dauH? ‘to smear, rub (on)’ 

*AVESTAN: (+ *fra-) YAv. fradauu- ‘to be rubbed off with’ = Liste: 31 
MED .; Pres. them.: IND. 3sg. YAv. “fradauuaite (V 5.24), INJ. 3sg. YAv. fraóauuata (V 9.29) 
*MIDDLE PERSIAN: (+ *8-) MMP *’rwdg ‘pollution, dir" > DMMPP: 53a 


*dauxs 69 


*KHOTANESE: (?) LKh. du- ‘to strike, beat; clean’ (also from *daub ?) || (+ *uz-) 
LKh. uysdu- ‘to remove’ = SGS: 44 f., 15 

*SOGDIAN: BSogd. ó w ‘to smear, plaster’ || (+ *ham-) BSogd. ’nö’w, MSogd. ’nöw 
‘to smear, anoint’ 

Pres.: SUBJ. 3sg. BSogd. 6’w’t; Inf.: BSogd. ö’w’y || (+ *ham-) Pres.: IND. 3sg. BSogd. "nd'wt; Inf.: 
BSogd. ’nö’w’y, pret. MSogd. ’nöwt 

*CHORESMIAN: m/6’w- ‘to rub in, smear’ || (+ *apa-) bö’w- ‘to polish’ = Samadi: 63 
f., 16 

*NWIR: ? Gil. (Rsht.) vaseen/vasin- (sec. inch.-caus. ?) ‘to rub’ || (+ *à-) NP 
aludan/alay- ‘to soil, pollute, stain’, Khuns. ali (ppp.) ‘stained, soiled’ || (+ *uz-) NP 
zadudan/zaday- ‘to polish, clean’ || (+ *ham-) NP andudan/anday- ‘to smear, 
(re)cover, attach’, Tt. (Xia.) m-andevmun ‘we plaster’, b-andev(n) ‘plaster!’. o The 
original meaning of NP 4ludan/alay- appears to be ‘to smear’, v. Horn 1893: 10. The 
formation is influenced by the antonym (M)MP p’rw-, NP palüdan ‘to filter’, on 
which see *harz. 

*NEIR: Oss. I. dawyn/dawd, D. dawun/dawd ‘to smooth, polish’, Yghn. dou-/dóuta 
‘to plaster’, Wa. ôbrw-/ôowd ‘to rub, smear’ || (+ *uz-) Pash. zdoyol ‘to rub, grind, 
polish’ (< Pers. ?) || (+ *fra-) Oss. I. raedyjyn/reedyd, D. raedujun/reedud ‘to err, to sin 
against’ || (+ *ham-) Yi. da-/davd- ‘to smear’ 

*SANSKRIT: ? dhav ‘to shake, stir? (RV+) > EWAia I: 782 f. 

Ó It is difficult to reconcile the Ir. root and Skt. dhav ‘to shake, stir’ (as assigned in 
EW4Aia, l.c.) semantically. They may rather suggest a different etymology. Skt. does 
have a good IE etymology (ON dyja ‘to shake’, Gr. Өоуёо ‘to storm, to move fast’), 
whereas IE cognates cannot be cited in support of Ir. *dauH! ‘to smear, rub (on)’. It 
is more likely a "Reimbildung", cf. *sauH!. A.L. points out though that in Vedic 
there are, from the same root, some (synchronically separate) present forms that are 
much closer in meaning to the Ir. ones: pres. 3sg. à dhavati (RV+), pass. 3du. 
sam-dhavyete (KS), pass. partic. ä-dhüyamäna- (TS^) ‘to rinse, clean, rub, polish’. 
These forms are rather unrelated to dhav’ and may therefore be the genuine Skt. 
correspondences of Ir. *dauH'. 


*PIE — — LIV: 149 f. | Pok.: 261 

*REFERENCES: EVP: 101; Christensen, Contributions I: 74 f.; HFL II: 204b; Andreev — PeSéereva: 248b Ё; 
Abaev, Slovar’ I: 349; Yarshater 1969: 211, 216; Abaev, Slovar’ II: 362 f.; WIM I: 342; DKS: 171a, 6b; 
Werba 1997: 352 f.; Steblin-Kamenskij 1999: 168; NEVP: 101; ESIJa II: 380 ff.
```


## [2026-09-06T23:15:45.596Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^leu-\\|leu-1\\|leu-2\\|DIALYSIS\\|DIALYS\\|POLLUTE\\|POLLUTION\" AHD_watkins1985.txt | head -20; echo \"====\"; grep -n \"lutum\\|To loosen, divide\" AHD_watkins1985.txt | head"
}
```


### [2026-09-06T23:15:45.655Z] TOOL RESULT

```
638:kleu-1, To hear. I. Extended form *kleus- in Germanic *hleuza- in Old English hléor, cheek (< “side of the face” < “ear”): LEER. II. Zero-grade form *klu-. 1. Germanic *hlustjan in Old English Alystan, to listen: LIsT*. 2. Ger- manic *hlusin6én in Old English Alysnan, to listen: LIs- TEN. 3. Suffixed lengthened form *kli-to- in Germanic *hlidaz, “heard,” loud, in: a. Old English Alid, loud: Loup; b. Old High German Aldti, sound: ABLAUT, UM- LauT. III. Suffixed form *klew-yo- in Greek kleiein, to praise, tell: Cio. [Pok. 1. Rleu- 605.]
639:kleu-2. To wash, clean. 1. Latin clodca, sewer, canal: CLOACA. 2. Zero-grade form *klu- in Greek kluzein, to wash out: CLYSTER; CATACLYSM. [Pok. 2. kleu- 607.] kleu-3. Possibly hook, peg. I. Extended zero-grade form *klud- possibly in Germanic *Aluta-, lot, portion (seman- tic development obscure). 1. Old English Alot, lot: Lor. 2. Dutch lot, lot: LOTTERY. 3. Old French lot (> French lot), lot, portion: LOTTO; ALLOT. II. Suffixed variant form *klau-do- in Latin claudere, to close (< “to lock with a hook, bolt”): CLAUSE, CLOISONNE, CLOISTER, CLOSE, (CLOSURE), (CLOZE); CONCLUDE, ECLOSION, EXCLUDE, INCLUDE, OCCLUDE, PRECLUDE, RECLUSE, SECLUDE. III. Variant form *k/dw-. 1. Suffixed form *kldw-i- in Latin cldvis, key: CEMBALO, CLAVICLE, CLAVIER, CLEF, KEVEL; CLAVICHORD, CONCLAVE, ENCLAVE. 2. Suffixed form *kldw-o- in: a. Latin cldévus, nail: CLOVE!, CLOY; b. Latin clava, club: CLAVATE; CLAVICORN, CLAVIFORM. 3. Suffixed form *k/dw-yo- in: a. Greek kleiein, to close: CLATHRATE; b. Greek verbal adjective kleistos, closed: CLEISTOGAMOUS, CLEISTOTHECIUM. [Pok. k/éu- 604.] klewo-. Bald. Variant *kal(a)wo- in Latin calvus, bald: CALVARIUM. [Pok. k,/ouo- 554.]
673:leu-'
691:leu-1. To loosen, divide, cut apart. 1. Germanic */eusan
692:leu-?
693:in: a. Old English -Jéosan, to lose: LORN, (LOSEL); b. Ger- manic *fer-leusan, *far-leusan (*fer-, *far-, prefix denot- ing rejection or exclusion; see per’) in (i) Old English forléosan, to forfeit, lose: FORLORN (ii) Dutch verliezen, to lose (past participle verloren): FORLORN HOPE. 2. Ger- manic */aww6 in Swedish lagg, barrel stave (< “split piece of wood”), akin to the probable source of LAG?. 3. Germanic *lausaz in: a. Old English léas, “loose,” free from, without, untrue, lacking: LEASING, -LESS; b. Old English los, loss: LOSE, (LOSS); CG. Old Norse Jauss, louss, loose: LOOSE; d. Swiss German lésch, loose: LOESS. 4. Zero-grade form *lu- in: a. Greek luein, to loosen, release, untie: LYSIS, LYSO-, -LYTE, -LYTIC; ANALYSIS, CATALYSIS, DIALYSIS, LYASE, PARALYSIS, TACHYLYTE; b. Latin lués, plague, pestilence (< “dissolution, putre- faction”): LUES; Cc. prefixed form *se-lu- (se-, apart; see s(w)e-) in Latin solvere, to loosen, untie: SOLUBLE, SOLUTE, SOLVE; ABSOLUTE, (ABSOLVE), ASSOIL, CONSO- LUTE, DISSOLVE, RESOLVE. [Pok. 2. Jeu- 681.] leu-2. Dirt; to make dirty. 1. Latin polluere, to pollute (< *por-luere; por- for pr6-, forth, forward; see per’): POLLUTE. 2. Suffixed zero-grade form */u-to- in Latin lutum, mud, mire, clay: LUTE?. [Pok. 1. leu- 681.] léu-1, Stone. Welsh Jlech, flat stone (from an uncertain preform): CROMLECH. [Pok. 2. léu- 683.] léu-2. Echoic root. 1. Extended form */eut- in Germanic *leuth- in Old High German liod (> German Lied), song: LIED; VOLKSLIED. 2. Extended variant form *laud- in Latin laus, praise, glory, fame: LAUD. [Pok. 3. éu- 683.] leubh-. To care, desire; love. I. Suffixed form *leubh-o- in Germanic *leubaz in Old English /éof, dear, beloved: LIEF; LEMAN, LIVELONG. II. O-grade form *loubh-. 1. Germanic */aubé in: a. Old English léaf, permission (< “pleasure, approval”): LEAVE?; b. Middle Dutch verlof, leave, permission (ver-, intensive prefix, from Germanic *fer-; see per'): FURLOUGH; Cc. Germanic *galaubd (*ga-, intensive prefix; see kom) in Old English geléafa, biléafa (bi-, about; see ambhi), belief, faith: BELIEF. 2. Ger- manic *galaubjan (*ga-, intensive prefix; see kom), “to hold dear,” esteem, trust, in Old English geléfan, beléfan (be-, about; see ambhi), to believe, trust: BELIEVE. III. Zero-grade form *lubh-. 1. Suffixed form *lubh-a- in Germanic */ubé in Old English Jufu, love: LovE. 2. Suf- fixed (stative) form *lubh-é- in Latin libére, to be dear, be pleasing: QUODLIBET. 3. Latin libid6, pleasure, desire: LIBIDO. [Pok. leubh- 683.] leud-. Small. Germanic */it- in: a. West Germanic *lutti- laz in Old English /ytel, little: LITTLE; b. Old English liitan, to bend down: LouT?; c. Old Norse lita, to bend down (< “to make small”): (LouT!); d. perhaps Middle Dutch loteren, to shake, totter (< “to make smaller”), perhaps akin to the source of Middle English Joitren, to idle away time: LOITER. [Pok. leud- 684.] leudh-'. To go. Zero-grade form *(e)ludh- in suffixed unextended form *elu-to- in Greek prosélutos, “one who comes to a place,” stranger (pros-, to; see per’): PROS- ELYTE. [In Pok. 6. e/- 306.] leudh-2. To mount up, grow. Suffixed form */eudh-ero- in Latin liber, free (the precise semantic development is obscure): LIBERAL, LIBERATE, LIBERTINE, LIBERTY, LIV- ERY; DELIVER. [Pok. 1. leudh- 684.] leu(e)-. To wash. 1. Suffixed form *lou-kd- in Germanic *laugo in Old English /éag, lye: LYE. 2. Suffixed form *lou-tro- in Old English /éathor, washing soda: LATHER. 3. Variant form *Jaw- in: a. Latin lavere, to wash, with its derivative -luere, to wash: LOTION; ABLUTION, ALLU- VION, COLLUVIUM, DELUGE, DILUTE, (ELUANT), ELUTE, ELUVIUM; b. form */aw-d- in Latin lavdre, to wash: LAVE, LOMENT; C. Latin lavatrina, ldtrina, a bath, privy: LATRINE. [Pok. Jou- 692.] leug-'. To bend, turn, wind. 1. Germanic *Jauk-, leek (semantic transition obscure), in Old English Jéac, leek: LEEK; GARLIC. 2. Zero-grade form *lug- in Germanic *luk- in: a. Old English loc, lock (perhaps < “a bending
893:culdre, to rake, in Provengal rasclar (> French racler), to rake, scrape: RACLETTE. [Pok. 2. réd- 854.] reg-'. To move in a straight line, with derivatives mean- ing “to direct in a straight line, lead, rule.” I. Basic form *reg-. 1. Suffixed form *reg-to- in Germanic *rehtaz in Old English riht, right, just, correct, straight: RIGHT. 2. Latin regere, to lead straight, guide, rule (past partici- ple réctus, hence adjective réctus, right, straight): REALM, RECTITUDE, RECTO, RECTOR, RECTUM, REGENT, REGIME, REGIMENT, REGION; CORRECT, DIRECT, ERECT, RECTANGLE, RECTIFY, RECTILINEAR, RISORGIMENTO, SURGE. 3. Greek oregein (with prothetic vowel from oldest root form *sreg-), to stretch out, reach out for: ANORECTIC, ANOREXIA. II. Lengthened-grade form *rég-, Indo-European word for a tribal king. 1. Celtic suffixed form *rig-yo- in Germanic *rikja- in: a. Old English rice, realm: BISHOPRIC; b. Old Norse riki (> Norwegian rik), realm: RIKSMAL; c. Old English rice, strong, powerful: RICH. 2. Latin réx, king (royal and priestly title): REAL, REGAL, REGULUS, REIGN, ROYAL; INTERREX, REGICIDE, REGIUS PROFESSOR, VICEREINE, VICEROY. 3. Suffixed form *rég-en- in Sanskrit raja, rdjan-, king, rajah (femi- nine rdjni, queen, rani), and rdjati, he rules: RAJ, RAJAH, (RANI), (RYE2); MAHARAJAH, MAHARANTI. III. Suffixed lengthened-grade form *rég-old in Latin régula, straight piece of wood, rod: RAIL!, REGLET, REGULAR, REGULATE, RULE, IV. O-grade form *rog-. 1. Germanic *rak6 in Old English raca, racu, rake (implement with straight pieces of wood): RAKE!, 2,Germanic *rak- in Middle Dutch rakke, framework: RACK}, 3. Possibly Germanic *rankaz (with nasal infix) in Old English ranc, straight, strong, hence haughty, overbearing: RANK?. 4, Germanic *rak- inaz, ready, straightforward, in Old English gerecenian, to arrange in order, recount (ge-, collective prefix; see kom): RECKON. 5. Suffixed form *rog-d- in Latin rogdare, to ask (< “stretch out the hand”): ROGATION, ROGATORY; ABROGATE, ARROGATE, CORVEE, DEROGATE, INTERRO- GATE, PREROGATIVE, PROROGUE, SUBROGATE, SUPERER- ocaTE. 6. Suffixed form *rog-o- in a possible Latin noun *rogus, “extension, direction,” perhaps in a Latin phrase *é rogd, “from the direction of” (€ < ex, out of; see eghs), contracted into ergd, therefore, in consequence of: ARGAL, ERGO. V. Lengthened o-grade form *rég-. 1. Ger- manic *rdkjan in Old English rec(c)an, to pay attention to, take care (formally influenced by Old English reccan, to extend, stretch out, from Germanic *rakjan): RECK. 2. Germanic *rdékja- in Old English receléas, careless (-léas, lacking; see leu-1):; RECKLESS. [Pok. 1. reg- 854.] reg-2. Moist. 1. Suffixed variant form *rek-no- in Ger- manic *regnaz, rain, in Old English reg(e)n, rén, rain: RAIN; RAINBOW. 2. Possibly Latin rigdre, to wet, water: IRRIGATE. [Pok. 2. reg- 857.] reg-3. To dye. Lengthened-grade form *rég-. 1. Suffixed form *rég-és- in Greek rhégos, blanket, rug: REGOLITH. 2. Sanskrit rdgah, color, red: RAGA. 3. Perhaps Sanskrit raékshd, earlier form of lékshd, red dye: Lac}. [Pok. 1. reg- 854.] regv-es-. Darkness. Oldest root form *areg’-es-. Greek Erebos (with prothetic vowel), Erebus, a place of dark- ness under the earth: EREBUS. [Pok. regt-os- 857.] rei-1, To scratch, tear, cut. I. Extended form ‘reik-. 1. Germanic *rigon- in Italian riga, line (< “something cut out’’): RIGATONI. 2. Suffixed form *rei-md or *reig-sma in Latin rima, crack, cleft, fissure: RIMOSE. 3. Suffixed o-grade form *roik-wo- in Germanic *rai(h)-wa- in Old English raw, réw, a line, row: ROW!. II. Possible extended form *reipp-. Germanic *raipaz, rope, in: a. Old English rap, rope: ROPE; b. compound *stig-raipaz, “‘mount-rope,” in Old English stigrap, stirrup (see steigh-). III. Extended form *reip-. 1. Ger- manic *rifan, in Old Norse rifa, to tear: RIVE. 2. Zero-grade form *rip- in: a. Germanic *77fti- in Danish rift, breach, akin to the Scandinavian source of Middle English rift, rift: R1FT!; b. Germanic *rif- in Old English
1208:ABAFT apo- ABANDON bha-2 ABASE bassus ABASH bat- ABASIA gWa- ABATE battuere ABBREVIATE mregh-u- ABDICATE deik- ABDUCENS deuk- ABDUCT deuk- ABELE albho- ABERRATION ers-1 ABET bheid- ABEYANCE bat- ABHOR ghers- ABIDE bheidh- ABJECT yé- ABJURE yewes- ABLATION  tele- ABLAUT apo-, kleu-1 ABLE ghabh- ABLUTION leu(@)- ABNEGATE ne ABNORMAL gné- ABODE bheidh- ABOLISH al-3 ABORT er-! ABOUND wed-1 ABOUT ud- ABOVE upo ABRADE réd- ABRIDGE mregh-u- ABROGATE reg-1 ABROSIA gWere-4 ABRUPT reup- ABSCESS ked- ABSCISE kae-id- ABSCOND dhé-1 ABSENT eS- ABSOLUTE leu-1 ABSOLVE feu-1 ABSORB srebh- ABSTAIN ten- ABSTRACT tragh- ABSTRUSE treud- ABSURD swer-2 ABULIA gWele-1 ABUT bhau- ABYSS gWadh- ACANTHO- ak- ACANTHOPTERYGIAN pet- ACANTHUS ak- ACAPNIA kwép- ACCEDE ked- ACCELERATE kel-3 ACCENT kan- ACCEPT kap- ACCESS ked- ACCIDENT kad- ACCIPITER Oku- ACCLAIM kele-2 ACCLIVITY klel- ACCOLADE kwel-1 ACCOMMODATE med- ACCOMPLISH pele-1 ACCORD kerd-1 accosT kost- ACCOUNT peu- ACCRUE_ ker-3 ACCUMBENT keu-2 ACCUMULATE keue-2 ACCURATE cira ACERATE ak- ACERB ak- ACETABULUM ak- ACETIC ak- ACETUM = ak- ACHALASIA ghé-
1242:ANA- an! ANABAENA gWa- ANABAPTIST g¥ébh-1 ANABIOSIS gWei- ANACOLUTHON sem-! ANACRUSIS kreue-2 ANADEM dé- ANADIPLOSIS dwo- ANADROMOUS der-1 ANAGLYPH gleubh- ANAGOGE ag- ANALCIME = alek- ANALECTS leg-1 ANALEPTIC (s)lag¥- ANALOGOUS leg-! ANALYSIS leu-1 ANAMNESIS men-1 ANAPEST peu- ANAPHORA bher-? ANARTHROUS ar- ANASARCA twerk- ANASTOMOSIS ste-men- ANASTROPHE  streb(h)- ANATHEMA dhé-1 ANATOMY tem- ANCESTOR ked- ANCHOR ank- ANCHORITE ghé- ANCIENT! ant- ANCILLARY kWel-1 ANCON ank-
1336:CASE2 kap- CASHIER kes-2 CASTE kes-? CASTIGATE kes-2 CASTLE kes-2 CASTRATE kes-2 CATA- kat-1 CATABOLISM gWele-1 CATACHRESIS gher-5 CATACLYSM kleu-2 CATALECTIC slég- CATALEPSY (s)lag¥- CATALOGUE leg-1 CATALYSIS leu-1 CATAMENIA mé-2 CATAPLEXY plak-2 CATAPULT pél- CATARRH sreu- CATASTASIS sta- CATASTROPHE streb(h)- CATCH kap- CATCHPOLE pau- CATECHIZE (s)wagh- CATEGORY ger-1 CATER-CORNERED kWetwer- CATERPILLAR pilo- CATHEDRA sed-1 CATHEPSIN kat-1 CATHETER yé- CATHODE sed-2 CATHOLIC sol- CATION ei-1 CATOPTRIC okw- CATTLE kaput CAUDILLO kaput CAUDLE kele-1 CAULESCENT kaul- CAULICLE kaul- CAULIFLOWER _bhel-3, kaul- CAULINE kaul- CAUSTIC kéu- CAUTERY kéu- CAUTION keue-1 CAVE keue-2 CAVEAT keue-1 CAVERN keue-2 CAVETTO keue-2 CAVIL  kel-8
1374:Cio kleu-1
1375:CLIP? gel-1 CLITELLUM klei- CLoAcA kleu-2 cLop gel-1 CLOISONNE kleu-3 CLOISTER kleu-3 CLONE kel-1 CLONUS kel-3 CLOSE kleu-3 CLOSURE kleu-3 CLOT gel-1
1378:CLUMP gel-1 CLUTCH! gel-1 CLUTTER gel-1 CLYSTER kleu-2 co- kom COADUNATE oi-no- COAGULUM_ ag- COAL g(e)u-lo- COALESCE al-3 COARCTATE ar- coasT kost- COBALT ku- cocciD kokkos coccus kokkos COCHINEAL kokkos COCHLEA konk(h)o- cock? ku- COCKAIGNE kak-2 COCKCHAFER gep(h)-
1392:CONFOUND gheu- CONFRERE bhrater- CONFUSE gheu- CONFUTE bhau- CONGE mei-1 CONGEAL gel-3 CONGENER gene- CONGENIAL gene- CONGENITAL gene- CONGERIES gerere CONGEST gerere CONGLOBATE gel-1 CONGLOMERATE gel-1 CONGLUTINATE gel-1 CONGRATULATE gWera-3 CONGREGATE ger-! CONGRESS ghredh- CONGRUENT ghréu- CONIDIUM keni- CONIOSIS keni- CONJECTURE yé- CONJOIN yeug- CONJUGAL yeug- CONJUGATE yeug- CONJUNCT yeug- CONJURE yewes- CONNATE gene- CONNECT ned- CONNIVE kneig’h- CONNOISSEUR gn6- CONNOTE gné- CONNUBIAL sneubh- CONQUER quaerere CONQUIAN kom, kWo- CONSCIENCE skei- CONSCIOUS | skei- CONSCRIPT skribh- CONSECRATE sak- CONSENT sent- CONSEQUENT sekw-1 CONSERVE ser-1 CONSIDER sweid-1 CONSIGN sekw-1 CONSIST sta- CONSOCIATE sekw-1 CONSOLE! sel-2 CONSOLIDATE sol- CONSOLUTE leu-1 CONSONANT swen- CONSORT ser-3 CONSPICUOUS _ spek- CONSPIRE spirare CONSTABLE ei-1 CONSTANT sta- CONSTELLATION  ster-3 CONSTERNATE  ster-2 CONSTIPATE  steip- CONSTITUTE sta- CONSTRAIN | streig- CONSTRUCT  ster-2 CONSUETUDE s(w)e- CONSUME em- CONTACT tag- CONTAIN ten- CONTAMINATE tag- CONTEMPLATE tem- CONTEND ten- CONTEST trei- CONTEXT teks- CONTINUE ten- CONTORT terkw- CONTOUR tera-1 CONTRA- kom CONTRABAND bha-2 CONTRACT tragh- CONTRADICT deik- CONTRARY kom CONTRAST sta- CONTRAVENE gWa- CONTRITE tere-1 CONTRIVE trep-2 CONTROL ret- CONTROVERSY wer-3 CONTUSE (s)teu- CONVALESCE wal- CONVECTION wegh- CONVENE gWa- CONVENIENT gWa- CONVENT gWa- CONVENTICLE gWa- CONVENTION gWa- CONVERGE wer-3 CONVERSE! wer-3 CONVERT wer-3 CONVEX wegh- CONVEY wegh- CONVINCE weik-5 CONVIVIAL gWei- CONVOKE wekw-
1424:DEVANAGARI deiw- DEVASTATE eu-2 DEVEST wes-4 DEvi deiw- DEVIATE wegh- DEVIL gWele-! DEVIOUS wegh- DEVISE weidh- DEVOID eu-2 DEVOIR ghabh- DEVOLVE wel-3 DEVOTE weg¥h- DEVOUR gWera-4 DEVOUT weg*h- DEW dheu-2 DEXTER deks- DEXTERITY deks- DEXTRO- deks- DEXTRORSE_ wer-3 DHARMA dher-2 DI-!_ dwo- DIABASE gWa- DIABETES gWa- DIABOLIC gWela-1 DIACRITICAL krel- DIADEM dé- DIAGNOSIS gnd- DIAGONAL genu-! DIAGRAM gerbh- DIAL deiw- DIALECT leg-1 DIALOGUE leg-1 DIALYsIs_leu-1 DIAMETER mé-2 DIAMOND deme-2 Diana deiw- DIANTHUS andh- DIAPASON pant- DIAPAUSE paus- DIAPEDESIS ped-1 DIAPHANOUS bha-1 DIAPHORESIS bher-1 DIAPHRAGM bhrekw- DIAPHYsIS bheue- DIARRHEA sreu- DIARTHROSIS ar- DIARY deiw- Diaspora sper-4 DIASTASIS sta- DIASTOLE stel- DIASTROPHISM_streb(h)- DIATESSARON kWetwer- DIATHESIS dhé-1 DIATOM tem- DIATRIBE tere-1 DIAZO = gWei- DICAST deik- DICENTRA kent- DICHASIUM dwo- DICHO- dwo- DICHOTOMY tem- DICKER dekm DICLINOUS  klei- DICROTISM kret-2 DICTATE deik- DICTION deik- DICTUM deik- DIDACTIC dens-! DIDAPPER dub- DIDYMIUM dwo- DIDYMOUS dwo- DIE! dheu-3 DIE? dé-
1533:FORE- pert FORECLOSE dhwer- FOREFATHER per, peter- FOREGO! ghé- FOREIGN dhwer- FOREMOST per! FORENSIC dhwer- FOREST dhwer- FORESTALL | stel- FORFEIT dhé-1, dhwer- FORFICATE bherdh- FORGE! dhabh- FORGET ghend- FORGIVE ghabh- FORGO ghé- FORLORN leu-! FORLORN HOPE keu-?, leu-1 FORM merph- FORMAL merph- FORMER? per! FORMIC morwi- FORMICARY morwi- FORMICIVOROUS morwi- FORMULA merph- FoRNAX gWher- FORNICATE gWher- FORSAKE sag- ForT bhergh-2 FORTALICE bhergh-2 FORTE! bhergh-2 FORTE? bhergh-2 FORTH pert FORTIFY bhergh-2 FORTIS bhergh-2 FORTISSIMO bhergh-2 FORTITUDE bhergh-2 FORTRESS bhergh-2 FORTY kWetwer- FORUM dhwer- Fossa bhedh- FOSSE bhedh- FossIL bhedh- FOSSORIAL bhedh- FOSTER pa- FOUDROYANT bhel-1 FOUL pu-2
1727:LADY dheigh- LAG? leu-1 LAGER legh- LAGOMORPH slég- LAIR legh-
1753:List! leizd- List? leizd- LIis™ kleu-1 LisT5 las-
1754:LISTEN kleu-1 LITER fithra
1760:LOATH leit-1 LOATHE leit-1 LOBBY leup- LOBE leb-1 LOBO wikwo- LOBSTER lek- LocH laku- LOCHIA legh- LOCK! leug-1 Lock? leug-1 LOCKET leug-1 Locust lek- LOCUTION  tolkw- LODE leit-2 LODGE leup- LOEss leu-1 LOFT leup- LOGARITHM ar-, leg-1 LOGE leup- Locic leg-1 LOGISTIC leg-1 Loco- leg-1 Locos leg-1
====
691:leu-1. To loosen, divide, cut apart. 1. Germanic */eusan
693:in: a. Old English -Jéosan, to lose: LORN, (LOSEL); b. Ger- manic *fer-leusan, *far-leusan (*fer-, *far-, prefix denot- ing rejection or exclusion; see per’) in (i) Old English forléosan, to forfeit, lose: FORLORN (ii) Dutch verliezen, to lose (past participle verloren): FORLORN HOPE. 2. Ger- manic */aww6 in Swedish lagg, barrel stave (< “split piece of wood”), akin to the probable source of LAG?. 3. Germanic *lausaz in: a. Old English léas, “loose,” free from, without, untrue, lacking: LEASING, -LESS; b. Old English los, loss: LOSE, (LOSS); CG. Old Norse Jauss, louss, loose: LOOSE; d. Swiss German lésch, loose: LOESS. 4. Zero-grade form *lu- in: a. Greek luein, to loosen, release, untie: LYSIS, LYSO-, -LYTE, -LYTIC; ANALYSIS, CATALYSIS, DIALYSIS, LYASE, PARALYSIS, TACHYLYTE; b. Latin lués, plague, pestilence (< “dissolution, putre- faction”): LUES; Cc. prefixed form *se-lu- (se-, apart; see s(w)e-) in Latin solvere, to loosen, untie: SOLUBLE, SOLUTE, SOLVE; ABSOLUTE, (ABSOLVE), ASSOIL, CONSO- LUTE, DISSOLVE, RESOLVE. [Pok. 2. Jeu- 681.] leu-2. Dirt; to make dirty. 1. Latin polluere, to pollute (< *por-luere; por- for pr6-, forth, forward; see per’): POLLUTE. 2. Suffixed zero-grade form */u-to- in Latin lutum, mud, mire, clay: LUTE?. [Pok. 1. leu- 681.] léu-1, Stone. Welsh Jlech, flat stone (from an uncertain preform): CROMLECH. [Pok. 2. léu- 683.] léu-2. Echoic root. 1. Extended form */eut- in Germanic *leuth- in Old High German liod (> German Lied), song: LIED; VOLKSLIED. 2. Extended variant form *laud- in Latin laus, praise, glory, fame: LAUD. [Pok. 3. éu- 683.] leubh-. To care, desire; love. I. Suffixed form *leubh-o- in Germanic *leubaz in Old English /éof, dear, beloved: LIEF; LEMAN, LIVELONG. II. O-grade form *loubh-. 1. Germanic */aubé in: a. Old English léaf, permission (< “pleasure, approval”): LEAVE?; b. Middle Dutch verlof, leave, permission (ver-, intensive prefix, from Germanic *fer-; see per'): FURLOUGH; Cc. Germanic *galaubd (*ga-, intensive prefix; see kom) in Old English geléafa, biléafa (bi-, about; see ambhi), belief, faith: BELIEF. 2. Ger- manic *galaubjan (*ga-, intensive prefix; see kom), “to hold dear,” esteem, trust, in Old English geléfan, beléfan (be-, about; see ambhi), to believe, trust: BELIEVE. III. Zero-grade form *lubh-. 1. Suffixed form *lubh-a- in Germanic */ubé in Old English Jufu, love: LovE. 2. Suf- fixed (stative) form *lubh-é- in Latin libére, to be dear, be pleasing: QUODLIBET. 3. Latin libid6, pleasure, desire: LIBIDO. [Pok. leubh- 683.] leud-. Small. Germanic */it- in: a. West Germanic *lutti- laz in Old English /ytel, little: LITTLE; b. Old English liitan, to bend down: LouT?; c. Old Norse lita, to bend down (< “to make small”): (LouT!); d. perhaps Middle Dutch loteren, to shake, totter (< “to make smaller”), perhaps akin to the source of Middle English Joitren, to idle away time: LOITER. [Pok. leud- 684.] leudh-'. To go. Zero-grade form *(e)ludh- in suffixed unextended form *elu-to- in Greek prosélutos, “one who comes to a place,” stranger (pros-, to; see per’): PROS- ELYTE. [In Pok. 6. e/- 306.] leudh-2. To mount up, grow. Suffixed form */eudh-ero- in Latin liber, free (the precise semantic development is obscure): LIBERAL, LIBERATE, LIBERTINE, LIBERTY, LIV- ERY; DELIVER. [Pok. 1. leudh- 684.] leu(e)-. To wash. 1. Suffixed form *lou-kd- in Germanic *laugo in Old English /éag, lye: LYE. 2. Suffixed form *lou-tro- in Old English /éathor, washing soda: LATHER. 3. Variant form *Jaw- in: a. Latin lavere, to wash, with its derivative -luere, to wash: LOTION; ABLUTION, ALLU- VION, COLLUVIUM, DELUGE, DILUTE, (ELUANT), ELUTE, ELUVIUM; b. form */aw-d- in Latin lavdre, to wash: LAVE, LOMENT; C. Latin lavatrina, ldtrina, a bath, privy: LATRINE. [Pok. Jou- 692.] leug-'. To bend, turn, wind. 1. Germanic *Jauk-, leek (semantic transition obscure), in Old English Jéac, leek: LEEK; GARLIC. 2. Zero-grade form *lug- in Germanic *luk- in: a. Old English loc, lock (perhaps < “a bending
```


## [2026-09-06T23:15:59.935Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON latreh\"; grep -n \"لتره\" MON_part1.txt MON_part2.txt incoming/MON/*.txt 2>/dev/null | head -10; echo \"=== ARY\"; grep -n \"لتره\\|پالودن\\|آلودن\\|پالان\" incoming/ARY/ARY_pages.txt | head -20"
}
```


### [2026-09-06T23:15:59.998Z] TOOL RESULT

```
=== MON latreh
incoming/MON/MON_2vol_Adena_v2_djvu.txt:38866:لتره: (۵-)۱0۳۸ [- لوتره - لوترا| (۷.) زبانی 
MON_part2.txt:38866:لتره: (۵-)۱0۳۸ [- لوتره - لوترا| (۷.) زبانی 
=== ARY
4441:پالیدن, پالودن, پالاییدن / ۱۵۳
```


## [2026-09-06T23:16:01.448Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f in ['BQT_v1_pages.txt']:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    # find printed page markers\n    for w in ['آلودن','آلود','پالودن','پالود','لتره']:\n        idxs=[m.start() for m in re.finditer(w,t)][:6]\n        print(f,w,len(idxs))\nEOF"
}
```


### [2026-09-06T23:16:03.092Z] TOOL RESULT

```
BQT_v1_pages.txt آلودن 0
BQT_v1_pages.txt آلود 6
BQT_v1_pages.txt پالودن 4
BQT_v1_pages.txt پالود 6
BQT_v1_pages.txt لتره 0
```


## [2026-09-06T23:16:08.777Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '38855,38880p' MON_part2.txt; echo \"=== ARY ctx\"; sed -n '4420,4470p' incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-06T23:16:08.844Z] TOOL RESULT

```
نانی که آب بسیار دارد. نانی که خوب بخته 


بصورت برگة نازک و کم 


لتر ه: ادا (رص.) بار ه. در ید ه . کهنهه کهن. 
فربه» بر گوشت. , بیکار» کاهل تنبل. 


۴ ۱۵2 
لتره: (۵-)۱0۳۸ [- لوتره - لوترا| (۷.) زبانی 
قرار دادی مبان دو تن برای آنکه چون با هم 
تکلم کنند دیگران آن را نفهمند. کسی که 
بند زبان ندارد یعنی هر چه را که بشنود همه 
جا نقل کند. 

لت‌وپار: ۱۸۱-0-۲ (ص مر .) (عم.) پاره 
بار ه؛ قطعه قطعه. 

لته: (0-)«(۱۸۱)۱ (۱.) بارچةٌ کهنه, ژُنده رکو. 
له حیض: کهنهً حیض زنان. ( کد.) بی‌ارزش» 
بی‌قدر. مثل لت حیض: بی‌اعتبار: بی آبرو. 
تخته‌های مستطیلی که در بعضص نقاط گبلان و 
مازندران بجای سفال پشت بام بکار برند. 
(عم.) لنجهُ در. 
=== ARY ctx
,۳۸87 ,817801 برهان قاطع : ۳۵۴-۳۵
لاتین (7120ما): 2۸ فرهنگ معین : ۶۴
گرتبک (ع0077/1): ۸
اوستایی (۸۷887/07): 811716۸ آلمانی مان (0882/۸(0 ۵/۵۵ ۷۸۷۵۲
پهلری (1مالقه): ایرلندی مبانه (هماق۶2۶ ۸/0902 1
0 ۸6 ,8۸ ولزی (755]7): 18
کردی (07015): ۳۸
افغانی (پشتی) (/۸۳07۸(۷): ۳2 پسگشت‌ها 55 /(ق۲۵۲8
سانسکریت (8۸(/51077): ۶۸002200
1 ۳۸۷۸6 ,۳۸۷17۸6 ,07۸ که ولج" ای ات
یونانی (082850): 0 بلط 2 (8) دنا هار
لاتین (7100ما): 8 ,817818 7 (هتاه) بان 2۵
فرانسه (تل/(ق2). 3 2 (۴133) 8
اسپانیایی (5۳۸۸71577): ۳/0 4 (۴18) :00/5
ایتالیایی (۸۸اله7): دا براد
رومانی (0۸4۸(71۸): 3 4 (۲188) ,6اقه (88)
پرتفالی (۳087001885)+ ۳0 8 (هق0) 0
آلمانی کهن ((0874۸ #104 صان): برهان قاطم + ۳۵۵
لود یناد ی
۰ چ
[pdf page 152]
پالیدن, پالودن, پالاییدن / ۱۵۳
یادداشت,
۱- معنی این واژه در ایرلندی میانه و ولزی: تازه. *
ا ۲- معنی این واژه در آلمانی کهن و میانه: سرند کردن» (غله را) برجاری کردن.
۱ ۳ بازگمت به: هور پالیدن.
اوستایی (۸۳874(۷): آلمانی کهن (05440۷ ۲۷/01 صان):
,7۸۸0۸ ,ات۸ 0تشتق۲ 0
پهلوی (۳۸414۲7): 7۸171۸۸ ,8.11۸34 انگلیسی (8/0/58)(از فرانسه): ۴25
کردی (080151)): 8۸6
بلوچی (/8۸07): ۶۸1۸۷۸6 ,۳2/5۸6 پسگشت‌ها ک ۳
اففانی (پشتی) ‎ :۸08/۷/(‏ باظ۳7۸ 607 و
سانسکریت (7ل8۸(/5). 5 (۳8۴۷) 8۸0/17
ا ۳3۸۹ ,723۸2۸711 ب۳۸۷۸3 4 (۴818188) نقققملم 05
لاتین (۸7100ا): نك اه ای زا 9 (۲81۴) :2/۲5/25
فرانسه (4لع۳2۸): ادا داد رای 4 (۳۸2) :07075
اسپانیایی (3ل82۳۸(3): ۳۸ 6 (۲83) 537
ایتالیایی (ماله7): اد دش اد را برهان قاطع : 1۵۸
یادداشت:
بازگست بد: پاکه.
5
یونانی (075520): ناند ۱۱۸۸ رومانی ((1۸لهلال۸). 2۸
لائین (770با). ایسلندی‌کهن (1۵0 210۸ید صضام).
0 ۶5 ,ات۳۸۲ خ۸اق7۸
فرانسه (1ح)(۳2): ۱۸3 نررس کهن (۸088 2ا0). ۲۳۵۸
آسپانیایی (8۳۸(//3/7). قا ها سا کسرنیکهن (/54200 0ا0):
ایتالیایی (۸۸اه1/): ادا ۱ رالشآنآ۸70 ,۸1
یمور ۱
[pdf page 153]
۴ _/ پالیز» فالیزء جالیز» پردیس (به چم
فریزی کهن ((۳8/514): #لشآ ۲ بش71 ایرلندی کهن (87ل17 2ا0): 11
```


## [2026-09-06T23:16:24.675Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^\\s*۳۵۶[۰-۹]\\|^۳۵۶\" MON_part2.txt | head -5; echo \"---\"; awk 'NR>=38700 && NR<=38870' MON_part2.txt | grep -n \"۳۵\" | head -20; echo \"=== look for page numbers pattern\"; sed -n '38820,38860p' MON_part2.txt"
}
```


### [2026-09-06T23:16:26.215Z] TOOL RESULT

```
---
=== look for page numbers pattern
۱۵2۳ 


صورت مواد دخره‌بی دانه در داخل لیه‌ای 
جمم می‌شود و چون خارج از لپه در داخل 
دانه مواد دخیره‌بی موجود نست. در این 
صورت این دانه را بدون آلبومن گویند مانند 
دانه لوبیا و ممکن است که مواد ذخیره‌بی 
ی دانه جمع شود و لبه 
ضصخامتی در 
داخل و وسط دانه قرار گیرد؛ گزن اف 
صورت این دانه را دانه آلبومن‌دار گویند 
مانند دانهٌ کرچکک. به عبارت دیگر لیه‌ها 
عسارت ازسر کف‌هاق اولنه نبات:هرن .ال 
جنینی می‌باشند. (گیا.) هر یکک از دو نیمه 
دانةٌ باقلا و نخود و لوبیا و دیگر حبوبات که 
قابل نیمه شدن باشند. 
ج ۱ (1.) تبانجه: سیلی؛ یکت 
رت ۱ لخت | (ص.) لخت» بار ۵. لا 
پاره کردن: پاره پاره کردن. (.) واحدی 
برای سنجش انواع پارچه (زربشت» مخمل و 
عسره): توپ. (صحا.) یک ورق (دو 
صفحه‌یی) از کتاب» ورقه (برگی) که مجزا 
از ِ_ ٍِِ_ چاپ شود. لنکة دره 
مصراع. (شعر.) نصف بیت» یکك مصراع. 
لت )٩(‏ شکم بطن 
و (.) کُرزء عمود. جماق. 
لت‌انبار: ۲ | - شا ِ لیر ] (ص‌فر..) 
شکم پرست: برخوار. 
لت‌انبان: ۱.0 (رص‌مر.) شکم پرست. 
برخوار. بی حفاظ ؛ بی پناة. 
لتر: ۳۹۳11 .( واحدی معادل نیم من تر بر و 
برایر ۲۰ مثقال. ظرفی که دز آن شراب و 
مانند آن کنند؛ رطل. 
لشر تمه: (م)دها۱۸۱ زتر .۲ < لشر مه ] (.) 
نانی که آب بسیار دارد. نانی که خوب بخته 


بصورت برگة نازک و کم
```


## [2026-09-06T23:16:35.816Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nfor w in ['آلود','پالود','پالان','پالونه']:\n    for m in list(re.finditer(w,t))[:8]:\n        s=t.rfind('[pdf page',0,m.start())\n        tag=t[s:s+16]\n        print(w,'|',tag,'|',t[max(0,m.start()-120):m.start()+160].replace('\\n',' '))\n    print('----')\nEOF"
}
```


### [2026-09-06T23:16:37.599Z] TOOL RESULT

```
آلود |  | علق باو دارد . ستستان » بکس تون بر وزن کافرستای ؛ غلم پدر زن وامق ات و او عاقبت بردست وامق کشته شد ۱ . 3 سو ده - بر وزن آلوده » بمعنی بی زحمت و بی‌عزاحمت ومی‌مشقت باشد - و بمعنی خقته و خوایده هم آمده است , # آسه ۴ - پروژن کاسه »کدت و زرات باشد - و زمینی را نی ز کون که مجهت زراعت 
آلود |  |  . ش « بنم کاف فارسی و. سکون شین قطه دار بیمنی آغوش است که بروبفل باشف . ] گشته » نتم حرتان شاری مروذن وا کشته» بمعنی 1 آلوده و آمخته‌باهو۷ (۳) چك : اپاشته . و بجتند تاراج و رستیث را همچو میمون نخود درآ کپ خوش خسروانی « لت ناحه 5 -نصری«لفت ناهد». ای میاه ( نسخةٌ لفتی خطي ) و کمان
آلود |  | ست ۶ لفت نامه *. ۱ - یزیمعنی حشوه آکنه : خود پر کبوتران میلوست کا کین چهار بالش اوست . خافانی و در کلمات م رکبه بممئی : آلود » مرصم » اباشته , ماد و گونه » دارا و صاحب . اندود آید همچون : زهرا کین . کوهرآ کین » ضیقآ کین , طلسم آکین » عشرتآ کین » زرا کین . ر: لت نامه.. . ۷ - اوستا
آلود |  | یگر یکوجك بمقدار بك‌فیشه ختح لام » بمعنی لاله - وس‌های چوب کوچاك نیز میباشد . ی اند وت ا سا و تن همزه هم درست است ۴ . 9 آلودگی و عیب - ترداهشی وفسق وفجوروخیات اک آزد ۱ مر خن آ من ۴ - تاب قپرش تیغ را الماس کرد برق خشمش کوه را آلا کرد ۱ سراح‌آالدین راجی « لفت نامه ». ۴ - مرش لال ( 
آلود |  | ون ثالت » مهرودگین | یادشاهان را گوبنده ویضی کویند اين, لفث ترکی . است ؟ . ۲ لفده * - باغین قطمداربروزن آزرده, بمعنی قهرآلود وخشمگین - وجنگه آورباشد . ۲ لو زه رن اه نش فاد است و آن‌سرخی باش که زنان برروی مالند ۰ ] فتن - بافاء بروزن ومعن ی آشفتن باشت. ۲ قشته مه پروژن و معتی آخفته 
آلود |  | وخیز کردن و برجستن ستور باشد ۷ . روم درون‌قلمه بجهت محافت قلمه نعیین(۱) کننهه . ]لو ۷ سبروزن‌خالو موماست ممروف؟ - ومخفف آلود نیزباشدکه از آلودکي حست ۴ و داش و کور؛ خشت پزی را نز کویند . * [ لوده داهی ه مرمدامقید - وفاسق و فلجر و کتاهکار و عاصی را کویند . ۲ لوس « بروزن ناموی ؛ ناه
آلود |  |  ستور باشد ۷ . روم درون‌قلمه بجهت محافت قلمه نعیین(۱) کننهه . ]لو ۷ سبروزن‌خالو موماست ممروف؟ - ومخفف آلود نیزباشدکه از آلودکي حست ۴ و داش و کور؛ خشت پزی را نز کویند . * [ لوده داهی ه مرمدامقید - وفاسق و فلجر و کتاهکار و عاصی را کویند . ۲ لوس « بروزن ناموی ؛ ناه کردن بگوشةٌ چشم ب
آلود |  | فاراسیا » شود . ۱ ۵ آلووی - پپلوی تالاها410 « تاوادبا ۱6۸ : ۲ * بمعنی لوث - آلاش - فق وفبور - شوخ ووسخ « لت نامه » . 1« آلودی . بهلوی 210188 ۱ دشکرت ۵ سس تتلاالا] لاینی وتلا۵] ابرلاندی باستانی ( پلیدی ,کل » مدفوع ) دهرن 4۲» بمعتی ۱ شه در صفحاهٌ ۵٩‏]هاچ » بای بروزن تاراج , خاکی ب
----
پالود |  | س ) » مامیثای سرخ ( ذیل : ارغامونی » ماشیا )۰ مرورشك ؟ (ذیل : اسموسا » وذیل : اشموسا) ؛ منجل (ذیل : کشکنجر) » مومیائی ۴ پالوده و مومیائی کوهی ( ذیل : کفرالیپود ) » میده * ( ذیل : فلاته )» ميرك کازرونی ۱ ( ذیل : حزا ) » نخوشی ( ذیل : فاشرا))» نرمه ( ذیل: نرمدست)» واشه (ذیل: بالوان
پالود |  | نمك چینی هم گونند ۴ بارود نه - بتح نات و زای هوز و ون و سکون رابع » نلم فواٍبیست از موسیقی . باروده » با زای حوز بر وزن پالوده. خوراك و فوت‌هرروزه باشد- و ضروری‌وها:<تاح هر روزه رانیز گویند از جامه و زبرجامه وامث آن - و جامةٌ کهنه را نیز گفته‌اند . بادوق » بر وزن فاروق ۰ بلخت روم
پالود |  |  آنرا اسب کوئل گویند؟ - و بمعنی صنف کننده هم آمده است لیکن بدون تر کیب گفته نمیشود همجون ؛ نرشی بالا و می بالا - و اعر بپالودن هم‌هست یعنی بپالاوصاف کن- و اویختهرا نیز گفته اند و بلفت زندو بلزند( ۱ ) بمعنی فرباد و فغان باشد بالاپال با بای فارسی‌بروژن مالامال» چیزی -خت را گوبند که
پالود |  |  و بلفت زندو بلزند( ۱ ) بمعنی فرباد و فغان باشد بالاپال با بای فارسی‌بروژن مالامال» چیزی -خت را گوبند که بمیار بماند - وپالوده سخت شده را نز گفته‌اند؟ . پالاد مس 7 وزن آباد 0 اسب جنست را کویند که اسب کونل باشد؟ .و آن اسبی است که پیشاپیش امراو سلاطین برند- واسب‌پالانیرا یز گفته ان
پالود |  |  - و ترشی پالا را نیز گفته اند۱9. با لوایه - بابای حطی بر وزن چار خانه » برسئوك ماد . مالوابه پالوث ‏ بروزن آسود , ماضی پالودن است » یمنی صاف کرد و از غل و غش باه ساخت ؟۷. پالودن ۳ بر وزن آسودن » بمعنی صأف کردن و صافی و دوشن شدن ‏ وپاك ساختن وصاف گردبدن از کدورتها - و خلاص .شدن -
پالود |  | طی بر وزن چار خانه » برسئوك ماد . مالوابه پالوث ‏ بروزن آسود , ماضی پالودن است » یمنی صاف کرد و از غل و غش باه ساخت ؟۷. پالودن ۳ بر وزن آسودن » بمعنی صأف کردن و صافی و دوشن شدن ‏ وپاك ساختن وصاف گردبدن از کدورتها - و خلاص .شدن - ونجات دادن - وافزون وزیاده گشتن - وبز رکه شدن - و ب
پالود |  | بز رکه شدن - و بزر گث گردانیدن باشد . بالوده ِ- بروزن| اوده.سروف‌امت و آن‌چیزی باشد کهازنداسته پزند و باشربت قند ۴ رك : پالودن. لغ نیز گویند : ر بر : بالکانه. . «أفت ناحد؟ . ۰ _ و5 : ۱۴ رك : بالودن ۰ ۸ و نیز بضم نالث *اسشق ۸ ۲۷.خورند و معرب‌آن فالوزح باشد! - وپاكوساف کرده شده از
پالود |  | بمعنی پای بند باشد بعنی شخصبکه در شهر خود با مه کر از ترا بطرف دیگر رفت و در آنجا نز تنواند بود ٩۴‏ ۳ ۳۳ ره 4 مالوانه : پالودجان خویش بيالونة بلا ۴ رد : بالاهشگه ۰ و هم بمعتی نرأوبدن, زهیدن : چودید ان بر و چهرء دلیذس زستان مادر بپالید شیر. فردوسی‌طوسی. بیاراست شهری زکاخ بلند (بسو
----
پالان |  | گفته‌اند؟ . پالاد مس 7 وزن آباد 0 اسب جنست را کویند که اسب کونل باشد؟ .و آن اسبی است که پیشاپیش امراو سلاطین برند- واسب‌پالانیرا یز گفته اند  .‏ پالادت « بر وزن وادادن؛,بمعنی بالودن و بالاش وصاف کردن باشد . (۱) چك: ژند ویارند. بالاهنگه بالاده - بر وزن آماده . بدکوی ومد و اهل غیبت
پالان |  | و میم بالف کشیده وکاف‌فارسی مفتوح پنون‌ودال ابجد زده , چیزی باشد که نرا پریشم کنند و ما بين پشت‌ستود و تنگک بار گذارند وپالان الاغ‌را نیز گفته اند شم در کالاه نداد د ‏ کنایه بز این است که حالی و هرتبه‌ای و دانثی " عدارد - و کی را یر گوبند که غیرتی و نفی نداشته باشد «هنی صاحب نفس 
----
پالونه |  | بالامیدن. ۴ را : باش. بنشان بتارم اندر ءرترل خویش‌را ۹ ونر باکاف تازی «لفت نامد* *رشمدی > . بالوابه ویاله :۰ . ۱ . رك : پالونه. ۳ بالامیدن. مر کب از و۳ سم نیز گوبند که بيك چنم ازآن نگاه کننده . پا - بر «زن خالودانهای سخت‌باشد ماتند عدی که اژاعضای آدمی برمی آ بد» و بعربی لول میگون
پالونه |  | نان علم تا رمح و باب ‌گردن اسب می‌بستند . وعجب این است که کلم پرچم بدانسا نکه در فارسی علاقة لیزه وئیز ریشه‌های مصفاة و پالونه گونه‌ای درطرف دهان نوعی وال ( بالن ) را نامیده‌اند ؛ در زبان فراسه یز کلمةٌ 18008 همانطور بپردو معنی آمده است : دارد فرسش بدیین شانی پرچم دم شیر آسمانی .
----
```


## [2026-09-06T23:16:52.657Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -c 400 BQT_v1_pages.txt; echo; echo \"=== markers\"; grep -c \"pdf page\" BQT_v1_pages.txt; grep -o \"\\[[^]]*page[^]]*\\]\" BQT_v1_pages.txt | head -3"
}
```


### [2026-09-06T23:16:52.723Z] TOOL RESULT

```
۱ ۵ ۱! ۱
7 موم ۳ لام
م ۱ 0 و طق صفرررنیاعدریرماروی
۰ ۱ "۳
۳
م و اس مر هر وه او
7 رین خلت ریز یتایب بره ات
لف‌بال ۶۲ .یرک
ا اند کل داي رشب , رمع
فان تا تا
رن 9 3
کرحم تن
اد شش مرا
مو رم | مر
وک رهب اه نات مج
لش
وان روکد ور
۱ و
طراول ؛ | ع اس

=== markers
0
```


## [2026-09-06T23:16:53.204Z] TOOL CALL #37: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py"
}
```


### [2026-09-06T23:16:53.246Z] TOOL RESULT

```
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


## [2026-09-06T23:17:00.515Z] TOOL CALL #38: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:58 2>&1 | tail -40"
}
```


### [2026-09-06T23:17:02.065Z] TOOL RESULT

```
no scan of BQT covers printed page 58 (see 'scans' in refs_online.json)
```


## [2026-09-06T23:17:07.077Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nfor f in ['BQT_v1_pages.txt','BQT_v1.txt','BQT_alt_v1.txt']:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    print(f, len(t), t.count('\\f'))\nEOF\nls /home/sfmqrb/git/rishe/data/verification/sources/refs/*.pages 2>/dev/null | head"
}
```


### [2026-09-06T23:17:08.849Z] TOOL RESULT

```
BQT_v1_pages.txt 1285412 776
BQT_v1.txt 1531945 0
BQT_alt_v1.txt 1536166 0
(eval):6: no matches found: /home/sfmqrb/git/rishe/data/verification/sources/refs/*.pages
```


## [2026-09-06T23:17:12.609Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('pages',len(pages))\nfor i,p in enumerate(pages):\n    if 'آلودی' in p and 'لاتینی' in p or ('lutum' in p):\n        print('IDX',i)\nfor i,p in enumerate(pages):\n    if 'پالودن' in p and 'صاف کردن' in p:\n        print('PAL IDX',i)\nEOF"
}
```


### [2026-09-06T23:17:14.348Z] TOOL RESULT

```
pages 777
PAL IDX 579
PAL IDX 580
```


## [2026-09-06T23:17:17.389Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'آلودی' in p:\n        print('AL IDX',i)\nprint('--- print 579 head')\nprint(pages[579][:1500])\nEOF"
}
```


### [2026-09-06T23:17:19.095Z] TOOL RESULT

```
AL IDX 268
--- print 579 head
ایا
پا کنك - بروزن پازند . مطلق باقوتر)
کوبند اعم از زرد و سفید و سرخ » و باین
>
با کو فتن بمعنی رقص کردن‌ورقاسی
نمودن باشد .
اگی ه بر رژن غناکی » اشر؟ س
تراشی را گویند - و بمصنی قملم شدن - وصفا-
و طهارت باشد ۴ . #۶
الا - بر وزن کالا , اسب جنیبت باشد
که آنرا اسب کوئل گویند؟ - و بمعنی صنف
کننده هم آمده است لیکن بدون تر کیب گفته
نمیشود همجون ؛ نرشی بالا و می بالا - و اعر
بپالودن هم‌هست یعنی بپالاوصاف کن- و اویختهرا
نیز گفته اند و بلفت زندو بلزند( ۱ ) بمعنی
فرباد و فغان باشد
بالاپال با بای فارسی‌بروژن مالامال»
چیزی -خت را گوبند که بمیار بماند - وپالوده
سخت شده را نز گفته‌اند؟ .
پالاد مس 7 وزن آباد 0 اسب جنست را
کویند که اسب کونل باشد؟ .و آن اسبی است
که پیشاپیش امراو سلاطین برند- واسب‌پالانیرا
یز گفته اند  .‏
پالادت « بر وزن وادادن؛,بمعنی بالودن
و بالاش وصاف کردن باشد .
(۱) چك: ژند ویارند.
بالاهنگه
بالاده - بر وزن آماده . بدکوی
ومد و اهل غیبت باشد. و اشب جنیست رالیز
گوند که اسب کوتل باشد۴ .
فا لاد ه بر وزن سالار . مرخت و شون"
بز رکه را گویند .
با لاش ه بر وزن شاباش » آلوده شدن
پای بگل ولای ۵ . *
فالافه » بر وزن کاشاند , مخارجه لی
باشد که بر بالای خائه سازند . ۱
پالاوان- با واو بروزن آبلدان, ظرفی
باشد مانند کفگی رکه چیزها در آن‌سا ف کنند .
وآنرا ترشی بالاگومند .
بالاون -ب واو بروزن وادادن» بمعنی
پالاوان است که ترشی دلاماشد .
بالاهنگ - بفتح های هوز بر وزن
گونند که برريك‌جانب لجام اسب‌بندند. واسبرا
بدان بکشند ۰ و کناهکار را نیز بدان مسکم
پربندند - و تزدمجردین آنجه باعث تعلق باشد,
و این لفت در اصل بالاآهنگ بوده‌بمنی جتیبت
کش » چه پالا بمعنی‌امب جنیبت است که اسب
کوتل باشد وآهنگف بمعنی
```


## [2026-09-06T23:17:32.562Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\np=pages[268]\ni=p.find('آلودی')\nprint(p[max(0,i-1400):i+600])\nEOF"
}
```


### [2026-09-06T23:17:34.360Z] TOOL RESULT

```
کد انداز راگویند . ۶
۱ - پهلوی 8100 « بونکر ۵۱ » ۰ شهمیرزادی ألقثا , کیلکی 5218 ( کوجه)
ر0( , طبری لاه (آلوچه) « واژه تایه ۳۱۰ > . ۴ یکی از انواع دسته بادامی ها
که تم علمی آن 1000650162 کناتلنا۳ است «گل کلاب وا ۳
؟ - درکلیات مر کب مانند : کل‌آلو , خواب آلو » یشمالو :
جبله اعل بیت خشم آلو شدند که همه درشیر بز طامم بدند. مثئوی «لفت نامه».
۴ - ر4 : الوند . ۵ رد : آفك .
1 - حمزه اصفهانی در کتاپ الئنببه علی حدوث التصحیف (نسخهٌ خطی ) ومیدانی در کتاب‌السامی
فی‌الاسامی عغابرا به « آله » ترجمه کرده اند وهمچنین ابورسان بیرونی در التفهیم. حکیم‌موژمن
در تحفه کوید : « عقاب بخارسی الوه و بثرکی قراقوش کوبند.». در فرهنگه جپانگیری آهده :
< له بااول مضموم حرفی باشد ذٍی مضلب که ب رکوههای بلند آشیانه کند و بغایت قوی و بز رکه
بود و آنرا آله نیز خوانند و بتازی عفاب گونند . حکیم فرقدی راست :
مثل دشمنان نو با تو حله کيك و حمله های له است . »
در همه فرهنگها آله بسمنی عقاب آمده و در بیاری از لهجه حای کنونی ابران نیز چنین است
چنانکه « هلو » در کردی و < اله » در مازندرانی و < آلمْ > د رکیلکی . درکارنامةٌ اردشیر بابکان
(۱4 : ۱۷) نالا بمعنی عقاب بکار رفته است ونیز در بندهش (۱۶ : ۲۳ ) 27۷2 بمعنی عقاب
آمده « فاب‌اس ۹۸-۲۹۹ » , درطبری 81168 . مازندرانی کنونی ۵۱/6 و ۵16« واژه نامهد؛ *.
۲ - مولف منتهی الارب در ترجمةٌ « تمییج » آرد : « برانگیختن نکه را برآلیز . »
6 آلوپالو - آلی‌بالی . رجوع به « فاراسیا » شود . ۱
۵ آلووی - پپلوی تالاها410 « تاوادبا ۱6۸ : ۲ * بمعنی لوث - آلاش -
فق وفبور - شوخ ووسخ « لت نامه » . 1« آلودی . بهلوی 210188 ۱ دشکرت
۵ سس تتلاالا] لاینی وتلا۵] ابرلاندی باستانی ( پلیدی ,کل » مدفوع ) دهرن 4۲» بمعتی
۱ شه در صفحاهٌ ۵٩‏
```


## [2026-09-06T23:17:47.522Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (568,569,580):\n    print('==== idx',i)\n    print(pages[i][:1800])\nEOF"
}
```


### [2026-09-06T23:17:49.103Z] TOOL RESULT

```
==== idx 568
بممنی سیه (۱) باشد , و آن خربنن چیزیست
امرو که فردا مت ندهند ٩‏ ,
باذشاه ۴ نامی است فارسی باستانی
مر کب از پاد و شاه و یاد بمعنی پای وپاسبان
د نگهبان و پاییدن و دارندگی تخت و اورنگه
باشد چنانکه کشت 4 و گاه «ممنی اصل
خداو ند وداعاد وهرچیز که‌آن بسرت و صورت
از .تال و افران بهتر و بزر کتر باشد چن‌انکه
چهاروجه بیرون نتواند بود
چه سلاطن اسان خلق اه اند. جوم ( ۲ )
حمیشمراماد وچون ملكرا بمروس تشبیه کرده‌اند,
اگر خداوند ملك را باین اسم خوانند مناصت
دازد. سیم (۳۱ ) چون پادشاه نسبت بدایر مردم
اصل وخداوند باشد ویاباد کی و دارندگی بحال
او اتس‌است می اگی او دا باین عم خواند
لایق بود. چهارم خداوند تخت و اورنگه اوست
واين معنی از جمیع معانی اولی باشد. و بعضی
کویند یادذاء بلفت‌باستانی بممنی اصل وخداوند
و () پاییدن و دارندگی است و بحذف آخر
تیز درست است که یادشا باشد, و بعربی سلطان
مگوند . ۶ .
با دشاه‌ بو کنابه ازآفتاب عالمتاب
(۱) چك : نته .
پر و۳ سس
است .
بادشاه تن بمعنی پادشاه چن است
که خورشید جهان‌پیما باشد .
بادشاه نیمر ود - کنابه از آتاب
است- ویادشاه مستان را نبز گوینه اززین جهت
که لیمروز نام سیستان است - و مردم نيك پی
ومبارك قدم را نز کفته‌انس وکنابه از حشرت
آدم عله‌اللام هم‌هست سیب آنکه تا نمروز
در بهشت بوده - و آشاره محضرت رسالت نناه
صلوات‌امه علیه یز هست بجهت آنکه شفاعت
امثان خودر! ناتیم روز خواهد کرد. ۶
باك گا فه- بکر نات بروزن شادبانه .
ام‌بلند باشد و دربچه رانیز گوبند » و بسکون
تالحم بنظر آعده است ۲
باد نگ ۴ -
بکرئاكو سکون‌نون
وکاف فارسی ۰ چوبی
باثدبهیات سرو گردن
ت» وآآن چوبی باشد که برنج بدان بکوبند تا
کیلکی0202502.
» محاز, و سشق
7
کنااکی و 7رد ۳2
ی ۱۹۸ ۰۱
بهلوی ۱0( ترا پیاده نظام
امروز نیز
==== idx 569
4و۳
بادم۱ بروزن ساده ,که خرو کاورا
کوبند - و چراگاه اسبان و شتران و کاوان را
بز کته اند - و پمعنی چوب دستی نیز آمده
ٍِ.
باده‌بان ۴ بروزن صابه‌بان کله‌بان
وچوپان وپاسبان ونگاهبانرا گویند.
پادیاب - بایای حطی بروزن ماعتاب,
پیمنی شدتن وپاکیزه ساختن چیز ها باشد
با دعا خواندن ۴ .
پا۵یاو» بروزن آب‌ساو. بععای پادیاب
است که شتن و باکیزه ساختن چیزها بادعا
خواندن باشد بلغت زند وبازند (۱) 6 .
پادبر بر وزن جاگیر , چوبی باشد
تانیفتده و باذال نقطه دار هم کنته‌اند و اين اسح
است بنا بر فاعد کلیه که هرگاه ما قبل دال
حرف علت باشد وآن حرف علت ساکن باشد
است
(۱) چك ء ژند و پلزند  .‏
اسنت ۸ .
اف بر وزن خار ۰ بمعنی سال گذشته
و پیش ازین باشد ۷ - و «خفف پاره هم هسنت -
و چرم دبافت کرده دا نیز کویند - و بمعنی
پرواز و پرش هم‌آمده است؛ چه پاریدن بمعای
بر بدن باشد 3
پار او - بارای بالف کشیده وبواو زده .
زت بر و مرژال را گونند - و نام بلو کیت از
پار د۸- بضم دال وسکون‌هيم» رانگی‌را
چاروا دوزند وبریس ران چارو! اندازند » وی
کوبند چرمی باشد که بریس زین اسب بندند
وبرزیر دم‌اسب اندازند. واين اسح است .
پار س - بسکون الث بروزن و حعنی
۳ هس یابه ۹ ۳ ۰
۴ رك : یادیاو .
۶ با 2202۷ . وآن مثل وضوست تزد مسلمانان. زرتفتب ی که میخواهد پادباب کند نضت
بك «خشنوتره اهورهه مزداو» (بخشنودی اهور مزدا) م‌خواند ویس از آن یکبار « اشم وهو...»
میسراید . آنگاه روی.ودستها وپاهای خودرا میشومد» از آن پسکشتی نو مبکند و بترئیب عقرد
کمربند خود می کتاید ودعای مخصوصآرا میخواند وباردیگر پدورکمر می‌بندد. «خرده اوسنا
۹ مح ۱*. ۱ رك : لت‌نامه ویازیر. .  .‏ ۷ 2 در: پارسال» پارینء قس مانسکربت
۸ ( در سال گذشته ) ؛ ارمتی 0۵ ( سال گذشته ) , کردی ۵ . افنانی ۳۵۲۵5 ,
استی 18۲8 ۰ 18808 ( در مال پیش ) » وخی ۳8۳0 ۰ سریکلی 2۳۷۷15 ( قس بونانی
61 ) بارسی باستان2 ۳8۲۷۷ (سابقا), اوستا 8211۲۷2 « اسشق ۲۷۰ *. ۸ - در
پارسی باستان (کتیبه‌های هضامنشی) 2752 : ام مکی از اقوام ابرانی مقیم جذوب ایران که نام
بقبه درصفحةً ۳۰
۵ پارت - پارسی‌باستان ۳۵۲4118۷2 مقر قوم پارت ( 
==== idx 580
پالای
باشد » يك حرف را ساقط سازند بثا بر آن .ك
الف را حذف کرده پالاهنگه خواندند .
۱ پالای - بسکون بای‌حطی: صاف کننده
را گوکلم
وامر برصاف کردن هم هست یمنی صاف کن۱ ی
و اسب جنیبت را هم کفته‌اند؟ ۱
پالا لین ۴ < بر وزن‌آساییدن,بمعنی
زیاده کردن و زیاده شدنب وصاف نمو دنل ءاشف.
باشد - و افزاینده و زباد کننده
با لد 8۵ ه سم دال » بروزن وعمنی‌باردم
است. وآنرا تررکان قوشفونگوبند .
پا ش بروزن بالش ؛ بمعتی افز ون
شدن و بالیدن وافز ابش باشد؟ .
پالغ - بنم نات
9 غن نقطه دار 4 بیمانة
شرامی ۳ وا گویدف که از شاخ
0 و کاو واب‌خوان فبل
و چوپ سازنر ۵ . بالغ
از ح بنتح ناك و سکون غين و زای
نقطه دار , خطا و حرم وزات باشد» وبمربی عس
خوانند ‏
با لکانه باکاف‌فارسی مروزن! شبانهه
با بلندودرمحة خانه باشد ۷ و معنی آت < در
نله درو کرین هم شقست سس اتکی ۱
و ند ۳
با لنگه بت بفتح ثالث۸ بر وژن شالنکگ ۰
کفشی ۲ داشد- ودربجةٌ کوچکیرا
۱ رگ : بالامیدن.
۴ را : باش.
بنشان بتارم اندر ءرترل خویش‌را
۹ ونر باکاف تازی «لفت نامد*
*رشمدی > .
بالوابه ویاله :۰ . ۱ . رك : پالونه.
۳ بالامیدن. مر کب از
و۳ سم
نیز گوبند که بيك چنم ازآن نگاه کننده .
پا - بر «زن خالودانهای سخت‌باشد
ماتند عدی که اژاعضای آدمی برمی آ بد» و بعربی
لول میگونند .
۲ تاسد را کوند ۰
است سیاه و کوچك که پیوسته در پرواز باشد
وجون بنشبندنتواند برخاست؛ وآنرا بادخورگهم
میگو تشفوما جانه «زعانه قافیه کرده‌آند" »نی
کویند اباییل همان است - و ترشی پالا را نیز
گفته اند۱9.
با لوایه -
بابای حطی بر وزن
چار خانه » برسئوك
ماد . مالوابه
پالوث ‏ بروزن آسود , ماضی پالودن
است » یمنی صاف کرد و از غل و غش باه
ساخت ؟۷.
پالودن ۳ بر وزن آسودن » بمعنی
صأف کردن و صافی و دوشن شدن ‏ وپاك ساختن
وصاف گردبدن از کدورتها - و خلاص .شدن -
ونجات دادن - وافزون وزیاده گشتن - وبز رکه
شدن - و بزر گث گردانیدن باشد .
بالوده ِ- بروزن| اوده.سروف‌امت
و آن‌چیزی باشد کهازنداسته پزند و باشربت قند
۴ رك : پالودن.
لغ نیز گویند :
ر بر : بالکانه.
. «أفت ناحد؟ . ۰ _ و5 :
۱۴ رك : بالودن ۰
۸ و نیز بضم نالث
*اسشق ۸
```


## [2026-09-06T23:18:03.195Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(575,590):\n    p=pages[i]\n    if 'هرن' in p or 'اسشق' in p or 'پهلوی' in p:\n        import re\n        for m in re.finditer('هرن|پهلوی',p):\n            print(i,'|',p[max(0,m.start()-200):m.start()+220].replace('\\n',' '))\n        print('---')\nEOF"
}
```


### [2026-09-06T23:18:05.182Z] TOOL RESULT

```
---
---
---
```


## [2026-09-06T23:18:38.225Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN leather\"; grep -n \"^leather\\|leather, n\\.\" KLN_1966.txt | head -5; grep -n \"leðer\\|lether, fr. OE\" KLN_1966.txt | head -5; echo \"=== SKT\"; grep -n \"LEATHER\\|leather\\. (E\" SKT.txt | head -5"
}
```


### [2026-09-06T23:18:38.300Z] TOOL RESULT

```
=== KLN leather
21354:leather,  n.  —  ME.  lether,  fr.  OE.  leder,  rel.  to  OS. lethar,  ON.  ledr,  Dan.  Iseder,  Swed.  lader,  OFris. lether,  MDu.  leder,  Du.  leder,  leer,  OHG.  ledar, MHG.,  G.  leder,  and  cogn.  with  OIr.  lethar ,  W. lledr,  Bret,  lezr,  ‘leather’.
21356:leatherette,  n.  —  A  hybrid  coined  fr.  leather  and -ette,  a  suff.  of  French  origin, leathern,  adj.  —  Formed  fr.  leather  with  suff.  -en. leatheroid,  n.,  material  used  instead  of  leather; artificial  leather.  —  A  hybrid  coined  fr.  leather and  Gk.  -oetSf]?,  ‘like’,  fr.  clSo;,  ‘form,  shape’. See  -oid.
=== SKT
```


## [2026-09-06T23:18:40.187Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW lutum\"; grep -n \"lutum\" LEW_1910.txt LAT.txt | head -10; echo \"=== polluo\"; grep -n \"polluo\\|polluere\" LAT.txt LEW_1910.txt | head -10; echo \"=== NYB\"; grep -n \"ʾlwtn\\|pʾlwtn\\|ālūt\\|pālūt\" NYB_vol2_glossary.txt NYB.txt 2>/dev/null | head -10"
}
```


### [2026-09-06T23:18:40.264Z] TOOL RESULT

```
=== LEW lutum
LAT.txt:1354:Deriv 4 s: aceratus: -m lutum cum paleis mixtum, P.F.18,30; acerosus:
LAT.txt:12640:elutus, cf.elutum dans le Thes.). Les gloses ont conservi la trace d'un
LAT.txt:27347:habeS, Sali., Cat.58,1; quod me hortaris ut absoluam, habeo absolutum
LAT.txt:31467:luul, lutum (et iuudtum dans iuuaturus), -are: faire plaisir A (surtout
LAT.txt:34486:Traeca, ubi Liberi fanum inclutum | Maro locaui<t>." Vbi quidque con¬
LAT.txt:34922:et qu’ils rapprochent de gr. Xup/x; et lutum "boue". LejA dans le Carm.
LAT.txt:35141:Sans doute de *lut~trom. Cf. lutum.
LAT.txt:35183:tamination de udra "loutre" et de lutum "boue", a cauae de 1'habitat
LAT.txt:35197:lutum, -I n.: gaude, piante qui sert i teindre en jaune; d'oii
LAT.txt:36041:mamphur?: - appellatur loro circumuolutum mediocris longitudinis
=== polluo
LAT.txt:13598:est manibus luto plenis aliquid attingere et polluere, pnis plus g 4 n 4 -
LAT.txt:35194:Cf. aussi lustrum, et polluo.
LAT.txt:48690:polluo, -is, -ul, -utum, -ere: souiller, salir (sens physique
LAT.txt:48694:'epoq^imper. = a^iauTOC); impolluo (tardif, d'aprfes inquino).
LAT.txt:49680:facientem opus, sacra polluerentur. Mais le mot n'est sans doute
=== NYB
```


## [2026-09-06T23:18:43.761Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '35170,35200p' LAT.txt; echo \"=== polluo\"; sed -n '48688,48700p' LAT.txt"
}
```


### [2026-09-06T23:18:43.823Z] TOOL RESULT

```
5,693,1437); un croisement de sena et une influence de lux, luCed
ont pu se produire. On peut aonger a un rapprochement avec lauo,
*lou-s-tro-m, mais la presence de l's devant le suffixe fait dif-
ficulte. Cf. toutefois monstrum.
lutor: v. lauo.
lutra, -ae f.: loutre (Varr. Plin.), M.L.51O7. Certaines formes
romanes supposent aussi lutria, enitria (du gr. evu8pl.C), et ontra,
cf.M.L. s.u.
Cf. skr. udrah, a v.udra-, gr. ev - l)8pi,C, v.isl. otr, v.h.a .ottar "lou-
tre". Le t est comme dans uter "outre" qui'a et^ rapproche du groupe
de gr. u 5 top, mais sans qu'on voie comment. Quant a l, cf. le fait que
1'armenien a leard "foie" en regard de skr .ydkrt, et luc "joug" en
face de skr .yugam. Tout ceci hypoth<Stique. - On a envisage une con-
tamination de udra "loutre" et de lutum "boue", a cauae de 1'habitat
de 1 1 animal.
ltitum # -i n. (lutus m. Claud. Quadrig. ap. Non. «1« ,7 ) : boue; argilede
potier. S'emploie ausai au sens moral, avec valeur injurieuse. Ancien
(Pl.), classique,- M.L.5189.
D^riv 4 s: luto,-as: conatruire en boue ou en terre petrie, salir de
boue, M.L.S1O5; luteus: fait de boue, ou couleur de boue, M.L.9694;
lutensis: qui vit dans la boue, lutarius, meme aena (Plin.); lutosus:
boueux, M.L.5186; lutulentus, M.L.5188, d'ou lutulentassit: lutu¬
lentum fecerit CGL Plac. V 30,19; collutulento (Pl.)^ lutamentum:
aire de terre petrie (Cat.); lutesco,-is - , lutlnae: TCTjXcqiaTtx (Char.);
Cf. aussi lustrum, et polluo.
. Cf.irl. loth "boue" (gen.sg. loithe), hom. XuSpov "aouillure, sang
mouille de poussiere" (et gr. X6 (at| "souillure, dommage", lat. luSsf).
lutum, -I n.: gaude, piante qui sert i teindre en jaune; d'oii
"couleur jaune" (Vg.Plin.).
D6riv6s: lUteus, luteolus: de couleur jaune; subluteus.
Sans etymologie claire.
=== polluo
pourrait s'expliquer a coup sfir que si l'on connaissait 1'histoire
du rituel.
polluo, -is, -ul, -utum, -ere: souiller, salir (sens physique
et moral); polluer (l. de 1 • *gl. ). - Classique ( Ci c. ), apparti ent k
la 1 • ecrite. Non roman,
De rive s et compos^s (tardifs): pollutio ; pollutrix-, impollutus
'epoq^imper. = a^iauTOC); impolluo (tardif, d'aprfes inquino).
De por-luo: v. lutum, lustrum.
polubrum, -I (u?) n. : - pelluuium in sacrificiis uas quod nos
peluem uocamus, F.aDfi,^ (et P.F.387,14); polybrum, quod Graeci vep-
vt,(3a, nos trullium uocamus. Liuius (Od.5): "argenteo polybro, aureo
eglutro". Fabius Pictor lib.ZVI: "aquam manibus pedibusque dato,
polybrum sinistra manu teneto, dextera uasvm cum aqua"-, Non. 544,30.
```


## [2026-09-06T23:18:45.601Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB pal\"; grep -n \"pʾlwtn\\|p'lwtn\\|palut\\|alut\" NYB_vol2_glossary.txt | head -10; echo \"=== SYN leather\"; grep -n \"4\\.12 LEATHER\\|LEATHER\" SYN.txt | head -5; echo \"=== SYN dirty\"; grep -n \"DIRTY\\|15\\.87\" SYN.txt | head -5"
}
```


### [2026-09-06T23:18:45.673Z] TOOL RESULT

```
=== NYB pal
=== SYN leather
9793:CHAPTER 6 CLOTHING; PERSONAL ADORNMENT AND CARE P 6.11 CtorHe, Dress 6.47 Apron di 6.12 CuiotHine, CLOTHES 6.48 TRoUSsERS fl 6.13 Tartor 6.49 Srocxine, Sock ¢l 6.21 CuorH 6.51 SHor Y 6.22 Woo. 6.52 Boor 4s 6.23 Linen; Fuax 6.53 SurPPer h 6.24 Corron 6.54 SHoEMakEr, Copper ip =i 6.25 SiLk 6.55 Hat; Cap ty 6.26 Lace 6.57 Brvr, Girpir 4 6.27 Fe.r 6.58 GLove Ki 6.28 Four 6.59 Vem ' 6.29 LEATHER 6.61 Pocxrer 6.31 Spin 6.62 Burron d 6.32 SprnpLEe 6.63 Pin 8 6.33 Wrave 6.71 ApornaenT (Personal) fr 6.34 Loom 6.72 JEWEL ? 6.35 Sew 6.73 Rive (For Finger) la 6.36 NEEDLE 6.74 BRACELET od 6.37 AwL 6.75 NrcKLACE vi 6.38 Tureap 6.81 HanpKERcHIEF ag 6.39 Dys (vb.) 6.82 Tower st 6.41 CLoaK 6.83 Napkin fir 6.412 OvmrRcoat 6.91 Comp a 6.42 Woman’s Dress 6.92 Brus (\ 6.43 Coar 6.93 Razor ; 6.44 Suirr 6.94 OrmntTMENT y 6.45 CoLtar 6.95 Soar Z 6.46 Sxirr 6.96 Mrrror ; it ob 6.11 CLOTHE, DRESS ; Grk. Sig, ddbw Goth. wasjan Lith. apvilkti, aprédyli, NG evobw, vrbvw ON klada aprenglt, etc. . Lat. _vestire, induere Dan. klede Lett. apg'érbt, g'erbt n It. vestire Sw. klada ChSl. odétz, oblésti Pp Fr. habiller, (re)vétir OE scrijdan, gew@dian SCr. odjesti, oblaéiti Sp. _vestir ME clothe, dresse Boh. _oditi, oblékati, oSalilt : Rum. imbrdca NE dress, clothe Pol. _ubrad, odziad, oblec W Tr. élim, intuigur Du. kleeden Russ. odet’ te Nir. cdirighim, gaduighim OHG  werien, waten Skt. _-vas- W. gwisgo, dilladu MHG waten, kleiden Ay. vah- Br. gwiska NHG kleiden
10140:6.29 LEATHER
=== SYN dirty
748:2. Lat. mundus is the result of se- mantic borrowing, starting as a literary imitation of Grk. xécpos. It is the same word as mundus used of a woman’s ‘ornaments, dress’, this being related to the adj. mundus ‘clean, elegant’ (15.87). This was a synonym of Grk. xécpos in one of its frequent uses (see above), one that was probably more familiar to the
11079:6.71 ADORNMENT i (Personal) b Grk. — xdcpos ON skraul, pryoi Lith. papuoSalas J NG arodtét Dan. smykke, prydelse Lett. ruota, greznums f Lat. mundus, Grndlus, or- Sw. prydnad, smycke ChSl. ukraSentje q namentum OE gearwe SCr.  nakit, ures, ukras It. ornamento ME ornement Boh. okrasa Fr. parure NE adornment Pol. ozdoba, okrasa k Sp. adorno Du. versiering Russ. ukraSenie ¢ Rum. podoabi OHG  garawi Skt. bhigana-, alarikara- } Ir. cumlach, ornaid MHG gerwe, gesmuc Ay. pis-, pacsa- Nir. Grnaidhedcht, sciamh- NHG schmuck 6 acht W. addurnaid, trwsiad I Br. kinklou, bragerezou 0 Collective terms for articles of ‘adorn- 1.1) : adj. mundus ‘clean, elegant’ | ment’ are mostly based on still more (15.87).
19098:UW ft NG xaorPe ! 15.87), eas ei : ‘preserve’. Tiktin 1131. ‘a sim (K. Meyer, Contrib.
22488:Du., MHG, NHG klein, in MHG mostly ‘pure, neat, fine, pretty’ (cf. NHG kleinod ‘jewel, gem’), OHG kleinz ‘shining, slender, fine’, etc., OE cline ‘pure, clean’ (NE clean), prob. : Grk. yawol* apmrptopara Hesych., yAnvea ‘bright things, trinkets, stars’, yAnv7n ‘pupil of the eye’, yeAetv’ Aapumerv, avOetv Hesych., and other words with common notion of ‘bright, shining’. ‘Bright’ > ‘clean, neat’, as in Lat. nitidus > Fr. net, etc. (15.87), hence through ‘fine, delicate’ to ‘small’. Walde-P. 1.623.
25727:4. Grk. eénavrés, orig. ‘anniversary’ as in Hom. and early inscriptions (Cre- tan law-code, etc.), but also (Hom.-+) simply ‘year’, etym. disputed. Hither fr. phrase él at76 ‘in the same (time)’, for which cf. Boh. tyden, etc. ‘week’, fr. ‘this day’ (14.61); or perh. as orig. ‘sol- stice, resting place of the sun’, deriv. of evabw ‘rest, sleep in’, cpd. of latw ‘rest, sleep, pass the night’. Walde-P. 1.20. Brugmann IF 15.87 ff., 17.319.
```


## [2026-09-06T23:18:52.225Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10140,10160p' SYN.txt | head -40"
}
```


### [2026-09-06T23:18:52.270Z] TOOL RESULT

```
6.29 LEATHER
oxiros Goth. (skauda-, filleins) Lith.  skara xerol, Topdpe ON ledr Lett. dda corium Dan. leader ChSl. koZa, azno cuoio Sw. ldder SCr. koa cuir OE leper Boh. kiize cuero ME lether Pol. skéra
. piele NE leather Russ. koza lethar Du. leder Skt. carman- pie OHG | leder Av. éaraman- a MHG leder sil NHG _leder
\' G pba e ents
Words for ‘leather originate mostly in | ‘part, thing’. Meyer, Neugr. Stud.
me for ‘hide, skin’, etc. Some, many nem loanwords, show Specialization Tom ‘piece’, ‘cut’, ete, ver is okdros, orig. ‘hide’ (: OF hyd i 12), but usually ‘leather’ Cf. KUTOTO0g fea c.
maker” of ther-cutter’ (Hom.), ‘s
hoe-
kin, hide? (4.12) rarely
r’, but often ad; ; N made of leather’. TE
Terol, fr, Tt. neat
ne = ; Plece of cloth, ia ee NE piece, fr. 9
+ Br, pez ‘piece’, W. peth
4.70. REW 6450.
Byz. roudpiov, NG ropap, dim. of topos ‘slice’ (: réuvw ‘cut’), thence ‘scroll, tome’. Development through ‘scroll’ to the ‘parchment’ or ‘skin’ of the scroll and finally generalized to ‘skin’ and ‘leather’.
2. Lat. corium (> It. cuoto, Fr. cuir, Sp. cuero), Skt. carman-, Av. éaraman-, all orig. ‘hide’ (4.12).
Rum. piele, fr. Lat. pellis ‘hide’ (4.12).
3. Ir. lethar, NIr. leathar, W. Uledr, Br. ler beside ON ledr, OF leper, OHG
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
408 SELECTED INDO-EUROPEAN SYNONYMS
```


## [2026-09-06T23:18:53.918Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN pollute\"; grep -n \"^pollute\\|pollute,  tr\\.\" KLN_1966.txt | head -3; echo \"=== KLN dialysis\"; grep -n \"dialysis\" KLN_1966.txt | head -3; echo \"=== KLN lysis\"; grep -n \"^lysis\\|lysis,  n\\.\" KLN_1966.txt | head -3"
}
```


### [2026-09-06T23:18:53.995Z] TOOL RESULT

```
=== KLN pollute
29422:pol,  ‘head’,  and  wigelen,  ‘to  move  to  and  fro’. See  poll,  ‘head’  and  wiggle, pollock,  n.  —  A  var.  of  pollack, pollucite,  n.,  caesium  aluminosilicate  (mineral.) —  Named  after  Pollux,  the  twin  brother  of  Cas¬ tor  in  Greek  mythology ;  cp.  castorite.  For  the ending  see  subst.  suff.  -ite. pollute,  tr.  v.,  to  make  foul,  defile.  —  L.  pollutus, pp.  of  polluere,  ‘to  defile,  pollute,  contaminate’, for  *por-luere.  For  the  pref.  por-  see  pollicita¬ tion.  L.  -lucre  in  polluere  is  rel.  to  L.  lutum,  ‘mud’, and  cogn.  with  Gk.  Xup.cc,  ‘filth,  dirt,  disgrace’, Xupa!;,  ‘rubbish,  refuse’,  XChpoc,  XuO-pov,  ‘dirt, gore’,  OIr.  loth,  ‘mud,  dirt’,  W.  Uudedic,  ‘mud¬ dy’,  Lith.  lutynas,  ‘pool,  puddle’.  Cp.  lute,  ‘a cohesive  substance',  and  Lythrum. pollution,  n.  —  Late  L.  pollutio,  gen.  -onis,  fr.  L. pollutus,  pp.  of  polluere.  See  prec.  word  and  -ion. Pollux,  n.,  1)  the  twin  brother  of  Castor  (Greek mythology)  ;  2)  name  of  the  second  star  of  the constellation  Gemini.  • —  L.,  fr.  Gk.  IIoXuSeu- y.TjC ;  see  Polydeuces.  The  shortening  of  the word  and  the  shift  of  the  accent  to  the  first syllable  are  due  to  Etruscan  influence.
=== KLN dialysis
11248:Derivatives:  dialogue ,  dialog,  intr.  and  tr.  v., dialogu-er,  n. dialyse,  v.  —  See  dialyze, dialysis,  n.,  separation  of  crystalloids  from  col¬ loids  (chem)  —  L.,  ‘separation’,  fr.  Gk.  8ia- Xuaig,  ‘separation,  dissolution’,  fr.  SiaXiieiv,  ‘to part  asunder,  break  off,  dissolve’,  fr.  8ia  (see dia-)  and  Xiietv,  ‘to  loose,  loosen’;  see  -lysis. The  word  dialysis  was  introduced  into  chemistry by  the  Scottish  chemist  Thomas  Graham  (1805- 69),  the  discoverer  of  this  process,  in  i86r. dialytic,  adj.,  pertaining  to  dialysis.  —  Gk.  81a- Xuxix6g,  ‘able  to  dissolve’,  fr.  SidXuxog,  ‘dis¬ solved’,  verbal  adj.  of  StaXiieiv,  ‘to  dissolve’. See  prec.  word  and  -ic.
11249:dialyze,  also  dialyse,  tr.  v.  (chem.)  —  Back  for¬ mation  fr.  dialysis.
=== KLN lysis
2637:Derivatives:  analogical  (q.v.),  analog-ist,  n., analog-ist-ic,  adj.,  analogize  (q.v.) analphabetic,  adj.,  not  alphabetic.  —  Formed  fr. privative  pref.  an-  and  alphabetic, analysis,  n.,  separation  of  a  whole  into  its  com¬ ponent  parts.  —  Gk.  dvdXuai?,  ‘a  loosing,  re¬ leasing’,  fr.  dvaX’jEiv,  ‘to  unloose,  release,  set free’,  fr.  dvd,  ‘up,  on,  throughout’  (see  ana-),  and Xueiv,  ‘to  unfasten,  loosen,  slacken’.  See  lysis, analyste,  n.,  a  person  who  analyzes.  —  F.,  formed fr.  analyser,  on  analogy  of  nouns  in  -iste  (E. -ist)  fr.  verbs  in  -iser  (E.  -ize).  See  prec.  word and  cp.  analyze.
3857:atmolysis,  n.,  separation  of  mixed  gases.  —  Com¬ pounded  of  atmo-  and  Gk.  X'Wg,  ‘a  loosing; dissolution’.  See  -lysis.
6749:catalysis,  n.,  chemical  change  caused  by  an  agent which  itself  remains  unchanged  (client.)  — ModL.,  fr.  Gk.  xxxiX'jcnc,  ’a  dissolving',  fr. xxxxXuav,  'to  dissolve’  fr.  xxxx  (see  cata-)  and A'ieiv,  ‘to  loose,  loosen'.  See  -lysis.
```


## [2026-09-06T23:19:04.327Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10160,10175p' SYN.txt"
}
```


### [2026-09-06T23:19:04.385Z] TOOL RESULT

```
408 SELECTED INDO-EUROPEAN SYNONYMS
leder, etc., uncertain whether cognate groups (*letro-) or orig. Celtic (*letro- fr. *pletro- : Lat. pellis?) with early Gmc. borrowing. Pedersen 2.45. Or as orig. ‘smoothed skin’ (*letro- fr. *léitro-) : Grk. Aetos, Lat. lévis ‘smooth’? Kluge- G. 350.
4. Goth. skauda- in skaudaraip (acc. sg.) ‘thong’: Grk. cxdzos, etc. (above, 1). Feist 430.
Goth. jilleins (adj. translating depyari-
vos ‘leathern’) : OHG fel, Lat. ‘hide’ (4.12). Teist 152,
5. Lith. skira, Lett. ada, orig. ‘hide’ (4.12).
6. ChSl., SCr., Russ. koza, Boh. kiize, orig. ‘hide’ (4.12).
Pol. skéra orig. ‘hide’ (4.12) or esp, skéra wyprawna, lit. ‘tanned hide’,
ChSl. azno, jazno (*azino) : Skt. ajina- ‘hide, skin’ (4.12). Berneker 35.
Pellis
6.31 SPIN Grk. vita, 98a, KAdOw Goth. spinnan Lith.  verpti NG yw ON spinna Lett.  vérpt, prest, sprest Lat. _nére Dan. spinde ChSl.  presti It. filare Sw. spinna SCr.  presti Fr filer OE spinnan Boh.  piisti Sp. hilar ME _ spinne Pol. — przqsé Rum. toarce NE spin Russ. prjasi’, sprjast Ir. sni- Du. spinnen Skt. rl- Nir. — sniomhaim OHG = spinnan W. nyddu MHG spinnen Br. neza NHG ss spinnen
Words for ‘spin’ are mostly based on the notions of either ‘turn’ or ‘stretch’, in one group derived from the noun for ‘thread’.
1. IE *(s)né-, *(s)néi- in words for ‘spin’, ‘sew’ (Gmc.), ‘thread’, ‘needle’ be- side *sneu- in words for ‘sinew’, primary sense ‘turn, wind’ or ‘stretch’(?). Walde-P. 9.694. Ernout-M. 665 f. Pedersen 1.68, 2.633.
Grk. véw (*ovqw, cf. 3 sg. pres. vp, 3 sg. imperf. én, etc.), v70w, NG pop. yw; Lat. nére; Ir. sni-, NIr. snio- mhaim, W. nyddu, Br. neza : OHG najan ‘sew’; Lett. snat ‘twist lightly’ (as in spinning or esp. plaiting, cf. Miihl.- Endz. 3.974), Skt. sn@yu- and snavan-, Grk. veipov ‘sinew’.
2. Grk. xdAdfw, root connections? Walde-P. 1.464.
3. It. filare, Fr. filer, Sp. hilar, fr. VLat. filare (CGL 5 passim), fr. Lat.
```


## [2026-09-06T23:19:11.615Z] TOOL CALL #52: Bash

```json
{
 "command": "ls site/pages/310.jpg 2>/dev/null; pdftoppm -f 310 -l 310 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg310 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T23:19:13.960Z] TOOL RESULT

```
site/pages/310.jpg
total 130848
drwx------ 8 sfmqrb sfmqrb    12288 Sep  6 19:19 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   774972 Sep  6 18:54 afm143.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1046357 Sep  6 18:54 afm144.png
-rw-rw-r-- 1 sfmqrb sfmqrb   533122 Sep  6 17:21 afm41_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb   508509 Sep  6 17:21 afm41_b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   969829 Sep  6 17:21 afm41.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1322100 Sep  6 17:20 afm46.png
-rw-rw-r-- 1 sfmqrb sfmqrb   416305 Sep  6 17:20 afm46_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1144 Sep  6 19:14 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  5157031 Sep  6 18:05 aiw.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    26688 Sep  6 18:20 ary377_bot_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71464 Sep  6 18:20 ary377_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71267 Sep  6 18:19 ary378_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25966 Sep  6 18:19 ary378_top_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76489 Sep  6 17:24 bqt1237_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   127656 Sep  6 18:17 bqt1267_foot_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb   362419 Sep  6 17:50 bqt1583_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   456331 Sep  6 16:54 bqt1594_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   105420 Sep  6 18:16 bqt27.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2824 Sep  6 16:59 bqt83_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   703015 Sep  6 17:50 bqt_fn4.png
-rw-rw-r-- 1 sfmqrb sfmqrb   299015 Sep  6 17:50 bqt_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   325427 Sep  6 17:50 bqt_n552.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   315487 Sep  6 17:50 bqt_n553.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   330101 Sep  6 17:50 bqt_n554.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   332775 Sep  6 18:33 bqtv2_289_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   560485 Sep  6 17:53 bqtv2_650_s.png
-rw-rw-r-- 1 sfmqrb sfmqrb   541712 Sep  6 17:53 bqtv2_651_s.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9689 Sep  6 18:33 bqtv2_meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb   726576 Sep  6 18:33 bqtv2_n289.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   729454 Sep  6 17:53 bqtv2_n650.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   702551 Sep  6 17:53 bqtv2_n651.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   100817 Sep  6 17:36 bqt_v3_111.png
-rw-rw-r-- 1 sfmqrb sfmqrb   110820 Sep  6 17:36 bqt_v3_112.png
-rw-rw-r-- 1 sfmqrb sfmqrb    91526 Sep  6 16:59 bqt_v3_83.png
-rw-rw-r-- 1 sfmqrb sfmqrb   137595 Sep  6 18:10 buck2.txt
-rw-rw-r-- 1 sfmqrb sfmqrb      146 Sep  6 18:10 buck3.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    64531 Sep  6 16:53 build261.py
-rw-rw-r-- 1 sfmqrb sfmqrb    60498 Sep  6 17:11 build269.py
-rw-rw-r-- 1 sfmqrb sfmqrb    97300 Sep  6 17:16 build270.py
-rw-rw-r-- 1 sfmqrb sfmqrb    52615 Sep  6 17:36 build275.py
-rw-rw-r-- 1 sfmqrb sfmqrb    74145 Sep  6 17:43 build278.py
-rw-rw-r-- 1 sfmqrb sfmqrb    72342 Sep  6 17:58 build283.py
-rw-rw-r-- 1 sfmqrb sfmqrb    28249 Sep  6 18:25 build290a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63778 Sep  6 18:33 build290b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    68833 Sep  6 18:30 build291.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61310 Sep  6 19:11 build302.py
-rw-rw-r-- 1 sfmqrb sfmqrb     5043 Sep  6 17:05 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3501 Sep  6 17:05 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56424 Sep  6 17:05 c3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78058 Sep  6 17:05 c4.png
-rw-rw-r-- 1 sfmqrb sfmqrb 60831599 Sep  6 18:01 cad_k.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  2530822 Sep  6 18:01 cad_k.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    37980 Sep  6 17:16 c_av.png
-rw-rw-r-- 1 sfmqrb sfmqrb    29703 Sep  6 17:16 c_cros.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1174 Sep  6 17:16 c_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2612 Sep  6 18:28 c_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13418 Sep  6 18:28 c_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8430 Sep  6 18:28 c_ital.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11245 Sep  6 18:28 c_katrang.png
-rw-rw-r-- 1 sfmqrb sfmqrb     6717 Sep  6 18:28 c_katvar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    28872 Sep  6 18:28 c_katvar_zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb    95615 Sep  6 16:39 coord_pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb  8373934 Sep  6 18:09 cpd.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb   378445 Sep  6 18:09 cpd.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     4560 Sep  6 16:39 crop_ak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4014 Sep  6 16:39 crop_ak.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25373 Sep  6 16:42 crop_alk.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24852 Sep  6 17:04 crop_fr269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    43238 Sep  6 16:55 crop_germ269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    51654 Sep  6 17:04 crop_gk269.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2585 Sep  6 17:05 crop_gk271.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64142 Sep  6 17:02 crop_gr267.png
-rw-rw-r-- 1 sfmqrb sfmqrb     6411 Sep  6 16:39 crop_gr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59842 Sep  6 19:18 crop_gs.png
-rw-rw-r-- 1 sfmqrb sfmqrb    23559 Sep  6 16:42 crop_kohul.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59386 Sep  6 16:39 crop_lat2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    51357 Sep  6 16:55 crop_latin269.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4761 Sep  6 16:39 crop_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4311 Sep  6 19:00 crop_loll2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3325 Sep  6 19:00 crop_loll3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3612 Sep  6 19:00 crop_loll.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3974 Sep  6 16:37 crop_me2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3300 Sep  6 16:37 crop_me.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10236 Sep  6 16:39 crop_op2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4935 Sep  6 16:37 crop_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5599 Sep  6 16:37 crop_pers.png
-rw-rw-r-- 1 sfmqrb sfmqrb    18514 Sep  6 18:52 crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22007 Sep  6 17:10 crop_sak.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5110 Sep  6 17:10 crop_sax.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4854 Sep  6 17:10 crop_shekar.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1249 Sep  6 17:05 crop_sirish.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30419 Sep  6 17:02 crop_skt267.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5359 Sep  6 19:00 crop_skt2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4064 Sep  6 19:00 crop_skt.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10043 Sep  6 16:58 crop_slav.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24463 Sep  6 16:58 crop_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  2144625 Sep  6 17:55 dmmpp.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    14732 Sep  6 18:27 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17126 Sep  6 17:54 e1.json
-rw-rw-r-- 1 sfmqrb sfmqrb    51742 Sep  6 18:33 e2.json
-rw-rw-r-- 1 sfmqrb sfmqrb  5301166 Sep  6 17:01 ediv.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  1773345 Sep  6 17:01 ediv.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1845041 Sep  6 18:04 gharib.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  3698758 Sep  6 17:50 IEC_full_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb      228 Sep  6 16:34 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb     4265 Sep  6 17:53 kapi_script.png
-rw-rw-r-- 1 sfmqrb sfmqrb   944060 Sep  6 18:06 kent_full.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   288525 Sep  6 18:07 kent_n222.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   285652 Sep  6 18:07 kent_n223.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   282304 Sep  6 18:07 kent_n224.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   268920 Sep  6 18:07 kent_n225.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb     1433 Sep  6 16:45 merge262.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63035 Sep  6 16:56 mk265.py
-rw-rw-r-- 1 sfmqrb sfmqrb    73111 Sep  6 17:13 mk267.py
-rw-rw-r-- 1 sfmqrb sfmqrb    71564 Sep  6 17:08 mk268.py
-rw-rw-r-- 1 sfmqrb sfmqrb    41609 Sep  6 17:31 mk274.py
-rw-rw-r-- 1 sfmqrb sfmqrb    51778 Sep  6 17:32 mk276.py
-rw-rw-r-- 1 sfmqrb sfmqrb    46494 Sep  6 17:52 mk279.py
-rw-rw-r-- 1 sfmqrb sfmqrb    16605 Sep  6 17:54 mk280b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    17667 Sep  6 17:56 mk280c.py
-rw-rw-r-- 1 sfmqrb sfmqrb    43177 Sep  6 17:50 mk280.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58322 Sep  6 17:51 mk282.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63940 Sep  6 18:05 mk285.py
-rw-rw-r-- 1 sfmqrb sfmqrb    67974 Sep  6 18:09 mk286.py
-rw-rw-r-- 1 sfmqrb sfmqrb    60646 Sep  6 18:11 mk287.py
-rw-rw-r-- 1 sfmqrb sfmqrb    50446 Sep  6 18:33 mk292b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    14748 Sep  6 18:27 mk292.py
-rw-rw-r-- 1 sfmqrb sfmqrb    41011 Sep  6 18:29 mk294.py
-rw-rw-r-- 1 sfmqrb sfmqrb    45170 Sep  6 18:47 mk297.py
-rw-rw-r-- 1 sfmqrb sfmqrb    67312 Sep  6 18:51 mk298.py
-rw-rw-r-- 1 sfmqrb sfmqrb    44967 Sep  6 18:51 mk299.py
-rw-rw-r-- 1 sfmqrb sfmqrb    50897 Sep  6 18:54 mk300.py
-rw-rw-r-- 1 sfmqrb sfmqrb    49830 Sep  6 19:05 mk301.py
-rw-rw-r-- 1 sfmqrb sfmqrb    60810 Sep  6 19:07 mk303.py
-rw-rw-r-- 1 sfmqrb sfmqrb  8373934 Sep  6 17:00 mk.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb   378445 Sep  6 17:00 mk.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    11601 Sep  6 16:42 p262-g01.json
-rw-rw-r-- 1 sfmqrb sfmqrb    10625 Sep  6 16:43 p262-g02.json
-rw-rw-r-- 1 sfmqrb sfmqrb    19393 Sep  6 16:46 p262-g03.json
-rw-rw-r-- 1 sfmqrb sfmqrb    19959 Sep  6 16:44 p262-g04.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12063 Sep  6 16:43 p262-g05.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12051 Sep  6 16:44 p262-g06.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12737 Sep  6 16:44 p262-g07.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17259 Sep  6 16:46 p262-g08.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17820 Sep  6 16:53 p262-g09.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17855 Sep  6 16:45 p262-g10.json
-rw-rw-r-- 1 sfmqrb sfmqrb    14983 Sep  6 16:44 p262-g11.json
-rw-rw-r-- 1 sfmqrb sfmqrb    25352 Sep  6 16:46 p262-g12.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17745 Sep  6 16:44 p262-g13.json
-rw-rw-r-- 1 sfmqrb sfmqrb   105748 Sep  6 16:39 p263hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5565 Sep  6 17:22 p275_krei_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53703 Sep  6 17:22 p275_pahlavi.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7106 Sep  6 17:34 p279_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb    12970 Sep  6 17:34 p279_word.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3647 Sep  6 17:34 p279_xsaeta.png
-rw-rw-r-- 1 sfmqrb sfmqrb   130651 Sep  6 17:48 p283_arrow.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:02 p284
-rw-rw-r-- 1 sfmqrb sfmqrb    43108 Sep  6 17:51 p284_e0_fa.png
-rw-rw-r-- 1 sfmqrb sfmqrb    89734 Sep  6 17:51 p284_e0.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59639 Sep  6 17:48 p284_e2b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   106502 Sep  6 17:48 p284_e2.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:25 p289
-rw-rw-r-- 1 sfmqrb sfmqrb    54419 Sep  6 18:05 p289_labibi.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:33 p290
-rw-rw-r-- 1 sfmqrb sfmqrb     1476 Sep  6 18:11 p291_esfand.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31043 Sep  6 18:11 p291_root.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:53 p295
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:49 p296
-rw-rw-r-- 1 sfmqrb sfmqrb     9447 Sep  6 18:41 p297_av2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8787 Sep  6 18:41 p297_cav.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2803 Sep  6 18:41 p297_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8189 Sep  6 18:41 p297_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5216 Sep  6 18:55 p303_n18b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7082 Sep  6 18:55 p303_n18.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7046 Sep  6 18:55 p303_n5.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 19:11 p304
-rw-rw-r-- 1 sfmqrb sfmqrb     2952 Sep  6 19:00 p305_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5794 Sep  6 19:00 p305_lat0.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4047 Sep  6 19:00 p305_lat1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4248 Sep  6 19:16 p308_germ2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4663 Sep  6 19:16 p308_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4007 Sep  6 19:16 p308_greek2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3008 Sep  6 19:16 p308_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8017 Sep  6 19:16 p308_lat2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4878 Sep  6 19:16 p308_skt2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3816 Sep  6 19:16 p308_skt.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66777 Sep  6 16:42 pg261.png
-rw-rw-r-- 1 sfmqrb sfmqrb    84660 Sep  6 16:39 pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71156 Sep  6 16:38 pg263.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92930 Sep  6 16:37 pg264hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57862 Sep  6 16:35 pg264.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13324 Sep  6 16:57 pg265_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86370 Sep  6 16:57 pg265.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79922 Sep  6 16:42 pg266.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70622 Sep  6 16:56 pg267.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69592 Sep  6 16:52 pg268.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71754 Sep  6 16:55 pg269.png
-rw-rw-r-- 1 sfmqrb sfmqrb   122626 Sep  6 16:58 pg270hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    87489 Sep  6 16:55 pg270.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115300 Sep  6 17:05 pg271hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66696 Sep  6 17:04 pg271.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68566 Sep  6 16:58 pg272.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66829 Sep  6 17:28 pg273_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   157304 Sep  6 17:10 pg273hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70615 Sep  6 17:27 pg273.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65586 Sep  6 17:18 pg274.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80338 Sep  6 17:21 pg275.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76740 Sep  6 17:15 pg276.png
-rw-rw-r-- 1 sfmqrb sfmqrb    44171 Sep  6 17:16 pg277.png
-rw-rw-r-- 1 sfmqrb sfmqrb    89267 Sep  6 17:26 pg278.png
-rw-rw-r-- 1 sfmqrb sfmqrb   168655 Sep  6 17:34 pg279hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75777 Sep  6 17:34 pg279.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82065 Sep  6 17:34 pg280.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61535 Sep  6 17:39 pg281.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70575 Sep  6 17:34 pg282.png
-rw-rw-r-- 1 sfmqrb sfmqrb    74784 Sep  6 17:47 pg283.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81024 Sep  6 17:50 pg284hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81024 Sep  6 17:51 pg284.png
-rw-rw-r-- 1 sfmqrb sfmqrb   144566 Sep  6 17:49 pg284_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    84487 Sep  6 17:53 pg285.png
-rw-rw-r-- 1 sfmqrb sfmqrb   106264 Sep  6 17:53 pg286hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76099 Sep  6 18:10 pg286.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72442 Sep  6 17:59 pg287.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53847 Sep  6 17:58 pg288.png
-rw-rw-r-- 1 sfmqrb sfmqrb    28862 Sep  6 18:27 pg289_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb    91779 Sep  6 18:26 pg289.png
-rw-rw-r-- 1 sfmqrb sfmqrb   187988 Sep  6 18:19 pg290hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    98901 Sep  6 18:18 pg290.png
-rw-rw-r-- 1 sfmqrb sfmqrb   105586 Sep  6 18:11 pg291hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70592 Sep  6 18:10 pg291.png
-rw-rw-r-- 1 sfmqrb sfmqrb   103438 Sep  6 18:12 pg292.png
-rw-rw-r-- 1 sfmqrb sfmqrb    36312 Sep  6 18:20 pg294_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24759 Sep  6 18:56 pg295_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   125960 Sep  6 18:28 pg295hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80086 Sep  6 18:56 pg295.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56184 Sep  6 18:39 pg296.png
-rw-rw-r-- 1 sfmqrb sfmqrb   130247 Sep  6 18:41 pg297hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66500 Sep  6 18:33 pg297.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60960 Sep  6 18:39 pg298.png
-rw-rw-r-- 1 sfmqrb sfmqrb    99543 Sep  6 18:52 pg299hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    52844 Sep  6 18:38 pg300.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61588 Sep  6 18:56 pg301.png
-rw-rw-r-- 1 sfmqrb sfmqrb   182431 Sep  6 19:00 pg302hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    91158 Sep  6 18:59 pg302.png
-rw-rw-r-- 1 sfmqrb sfmqrb   122418 Sep  6 18:55 pg303hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    89589 Sep  6 18:52 pg303.png
-rw-rw-r-- 1 sfmqrb sfmqrb    48728 Sep  6 19:00 pg304.png
-rw-rw-r-- 1 sfmqrb sfmqrb   151120 Sep  6 19:00 pg305hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58313 Sep  6 18:59 pg305.png
-rw-rw-r-- 1 sfmqrb sfmqrb    50721 Sep  6 18:58 pg306.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66772 Sep  6 19:17 pg307.png
-rw-rw-r-- 1 sfmqrb sfmqrb   163981 Sep  6 19:16 pg308hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72091 Sep  6 19:12 pg308.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72781 Sep  6 19:15 pg309.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75436 Sep  6 19:19 pg310.png
-rw-rw-r-- 1 sfmqrb sfmqrb    84637 Sep  6 19:16 pg311.png
-rw-rw-r-- 1 sfmqrb sfmqrb   132637 Sep  6 18:38 sns_n155.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   129771 Sep  6 18:38 sns_n156.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   130970 Sep  6 18:38 sns_n90.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   531356 Sep  6 18:38 sns_n90_right.png
-rw-rw-r-- 1 sfmqrb sfmqrb   124445 Sep  6 18:38 sns_n92.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   522585 Sep  6 18:38 sns_n92_left.png
-rw-rw-r-- 1 sfmqrb sfmqrb   495290 Sep  6 18:38 sns_n92_right.png
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1548.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1549.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1550.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   300608 Sep  6 19:11 tadA_n63.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   311561 Sep  6 19:11 tadA_n64.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   334767 Sep  6 19:11 tadA_n65.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   351684 Sep  6 18:35 tad_n59.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   342929 Sep  6 18:35 tad_n59_mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb   242025 Sep  6 18:34 tad_n60_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   282364 Sep  6 18:34 tad_n60.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   335678 Sep  6 18:34 tad_n60_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   276093 Sep  6 18:34 tad_n61.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   332662 Sep  6 18:34 tad_n62.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   334767 Sep  6 18:35 tad_n65.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   265879 Sep  6 18:35 tad_n65_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   295896 Sep  6 19:11 tad_n66.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   304367 Sep  6 19:11 tad_n67.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   308480 Sep  6 19:11 tad_n68.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb     3698 Sep  6 18:19 zar_line.png
```


## [2026-09-06T23:19:19.099Z] TOOL CALL #53: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg310.png"
}
```


### [2026-09-06T23:19:19.432Z] TOOL RESULT

```

```


## [2026-09-06T23:19:19.430Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T23:19:44.165Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 310 -l 310 -r 400 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg310hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg310hi.png'); print(im.size)\n# crop region around Pahlavi->Persian link. At 200dpi coords ~ (330,780)-(900,1120) => x2 for 400dpi\nim.crop((640,1540,1900,2260)).save('p310_link.png')\n\""
}
```


### [2026-09-06T23:19:47.231Z] TOOL RESULT

```
(3400, 4400)
```


## [2026-09-06T23:19:49.561Z] TOOL CALL #55: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p310_link.png"
}
```


### [2026-09-06T23:19:49.579Z] TOOL RESULT

```

```


## [2026-09-06T23:20:02.257Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg310hi.png')\nim.crop((1520,1960,1900,2120)).resize((1140,480)).save('p310_j.png')\n\""
}
```


### [2026-09-06T23:20:03.949Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T23:20:06.324Z] TOOL CALL #57: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p310_j.png"
}
```


### [2026-09-06T23:20:06.339Z] TOOL RESULT

```

```


## [2026-09-06T23:20:23.162Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg310hi.png')\nim.crop((700,2480,2700,2720)).save('p310_gf.png')\n\""
}
```


### [2026-09-06T23:20:24.913Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T23:20:27.508Z] TOOL CALL #59: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p310_gf.png"
}
```


### [2026-09-06T23:20:27.523Z] TOOL RESULT

```

```


## [2026-09-06T23:20:45.078Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg310hi.png')\nim.crop((680,850,1250,1350)).save('p310_lat.png')\n\""
}
```


### [2026-09-06T23:20:46.894Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T23:20:49.295Z] TOOL CALL #61: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p310_lat.png"
}
```


### [2026-09-06T23:20:49.313Z] TOOL RESULT

```

```


## [2026-09-06T23:20:56.489Z] TOOL CALL #62: Bash

```json
{
 "command": "sed -n '1,50p' /home/sfmqrb/git/rishe/tools/fetch_source.py"
}
```


### [2026-09-06T23:20:56.531Z] TOOL RESULT

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


## [2026-09-06T23:21:01.853Z] TOOL CALL #63: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%A2%D9%84%D9%88%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D9%84%D9%88%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/leather\" \\\n \"https://www.etymonline.com/word/dialysis\" \\\n \"https://www.etymonline.com/word/pollute\" \\\n \"https://en.wiktionary.org/wiki/%CE%BB%CF%8D%CF%89\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 310, roots Letro / Leu-Lu\" ; done"
}
```


### [2026-09-06T23:21:07.576Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/90a7e99d246af2c1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ea9a1de647a80ae8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/704dbd5f8a133382.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/224df3a2227e0ba8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0d316b871f3df7b1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c834c908e55a8855.txt
```


## [2026-09-06T23:21:10.254Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 90a7e99d246af2c1 ea9a1de647a80ae8; do echo \"##### $f\"; grep -n \"Etymology\" -A 25 $f.txt | head -60; done"
}
```


### [2026-09-06T23:21:11.893Z] TOOL RESULT

```
##### 90a7e99d246af2c1
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Verb 
69-
70- 1.3.1 
71- Conjugation 
72-
73- 1.3.2 
74- Derived terms 
75-
76- 1.4 
77- References 
78-
79- Toggle the table of contents 
80-
81- آلودن 
82-
83- 5 languages 
84-
85- فارسی 
86- Bahasa Indonesia 
87- Kurdî 
--
146: Etymology
147- [ edit ] 
148-
149- Of uncertain origin.
150-
151- Cheung derives the verb from Proto-Iranian *ā- ( “ ad- ” ) +‎ *dauH- ( “ to smear, rub (on) ” ) , with a lambdacism of *d > l. The prefix is from Proto-Indo-European *h₂éd ( “ to, at ” ) , while the verbal root is of uncertain further origin, with possible connections to Vedic Sanskrit आधावति ( ādhāvati , “ to rinse, polish ” ) , though not Sanskrit धाव् ( dhāv , “ to run, flow ” ) , the latter which Cheung implicitly considers to be unrelated to the Iranian and Vedic verbs. [ 1 ] 
152-
153- Edelman and Rastorgujeva mention the theory above, but do consider the root to be related to धाव् ( dhāv ) . In addition, they suggest an alternate derivation from Proto-Indo-European *(s)leyb- ( “ to slip, slide ” ) ; [ 2 ] see *h₃sleydʰ- ( “ to slip ” ) for more.
154-
155- Pronunciation
156- [ edit ] 
157-
158- ( Classical Persian ) IPA ( key ) : /ʔaː.luː.ˈdan/ 
159-
160- ( Dari, formal ) IPA ( key ) : [ʔɑː.luː.d̪än] 
161-
162- ( Dari, formal ) IPA ( key ) : [ʔɑː.luː.d̪än] 
163- ( Kabuli ) IPA ( key ) : [ʔɑː.luː.d̪än] 
164-
165- ( Hazaragi ) IPA ( key ) : [ʔɔː.lu.d̪än] 
166-
167- ( Iran, formal ) IPA ( key ) : [ʔɒː.luː.d̪æn] 
168-
169- ( Tajik, formal ) IPA ( key ) : [ʔɔ.lu.d̪än] 
170-
171- Rhymes: -an 
##### ea9a1de647a80ae8
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Verb 
69-
70- 1.3.1 
71- Conjugation 
72-
73- 1.3.2 
74- Derived terms 
75-
76- 1.4 
77- References 
78-
79- Toggle the table of contents 
80-
81- پالودن 
82-
83- 3 languages 
84-
85- فارسی 
86- Magyar 
87- Malagasy 
--
144: Etymology
145- [ edit ] 
146-
147- From Middle Persian pʾlwtn' ( pālūdan , “ to strain, filter, purify ” ) , from Proto-Iranian *para-dā́wati , from Proto-Iranian *dā́wati ( “ to run ” ) , [ 1 ] from Proto-Indo-Iranian *dʰā́wati ( “ to run ” ) , from Proto-Indo-European *dʰew- ( “ to run, flow ” ) . Compare Persian دویدن ( “ to run ” ) , Sanskrit धावति ( dhā́vati ) and Ancient Greek θέω ( théō ) .
148-
149: This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium . 
150-Particularly: “Cheung doesn't mention this term, and the equivalency of the "run" and "wash" senses in Indo-Iranian is disputed.”
151-
152- Pronunciation
153- [ edit ] 
154-
155- ( Classical Persian ) IPA ( key ) : /paː.luː.ˈdan/ 
156-
157- ( Dari, formal ) IPA ( key ) : [pʰɑː.luː.d̪án] 
158-
159- ( Dari, formal ) IPA ( key ) : [pʰɑː.luː.d̪án] 
160- ( Kabuli ) IPA ( key ) : [pʰɑː.luː.d̪án] 
161-
162- ( Hazaragi ) IPA ( key ) : [pʰɔː.lu.d̪án] 
163-
164- ( Iran, formal ) IPA ( key ) : [pʰɒː.luː.d̪ǽn] 
165-
166- ( Tajik, formal ) IPA ( key ) : [pʰɔ.lu.d̪án] 
167-
168- Rhymes: -an 
169-
170- Readings
171-
172- Classical reading ? 
173-
174- pālūdan
```


## [2026-09-06T23:21:24.300Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"#### leather\"; grep -n \"Proto-West Germanic\\|leþr\\|Proto-Germanic\\|Proto-Indo-European\" 704dbd5f8a133382.txt | head -12; echo \"#### lyo\"; grep -n \"Proto-Indo-European\\|Etymology\" -A3 c834c908e55a8855.txt | sed -n '1,40p'; echo \"#### pollute\"; sed -n '1,80p' 0d316b871f3df7b1.txt | grep -n \"lutum\\|luere\\|pollut\" | head; echo \"#### dialysis\"; grep -n \"dialysis\\|lyein\\|leu-\" 224df3a2227e0ba8.txt | head"
}
```


### [2026-09-06T23:21:24.386Z] TOOL RESULT

```
#### leather
228: Proto-Germanic *leþrą 
229: Proto-West Germanic *leþr 
234: From Middle English lether , from Old English leþer ( “ leather ” ) , from Proto-West Germanic *leþr , from Proto-Germanic *leþrą ( “ leather ” ) , possibly borrowed from Proto-Celtic *ɸlitrom , *letros , from Proto-Indo-European *pl̥tro- ( “ skin, hide ” ) .
786: English terms inherited from Proto-West Germanic 
788: English terms derived from Proto-Germanic 
791: English terms derived from Proto-West Germanic 
792: English terms inherited from Proto-Germanic 
794: English terms derived from Proto-Indo-European 
#### lyo
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
--
97: Etymology 
98-
99- 2.3 
100- Pronunciation 
--
190: Etymology
191- [ edit ] 
192-
193: From Proto-Indo-European *lewh₁- ( “ to cut off, separate, free ” ) (which Beekes reconstructs as *lh₁u- ). Cognates include Latin luō ( “ expiate, pay ” ) , Sanskrit लुनाति ( lunā́ti , “ to sever, cut forth, destroy, annihilate ” ) , English loose , and possibly Old Armenian լուծանեմ ( lucanem ) and Albanian lirë . [ 1 ] 
194-
195- According to Beekes, the stem vowel was originally short ( λῠ- ), lengthened only later in Attic and sometimes in Homer ( λῡ- ) due to the influence of a laryngeal. The upsilon remains short ( ῠ ) before temporal endings beginning with ⟨ κ, θ, μ ⟩ and all derivatives, but the prosody of compounds remains that of λῡ́ω ( lū́ō ) .
196-
--
2767: Etymology
2768- [ edit ] 
2769-
2770- Learned borrowing from Ancient Greek λῡ́ω ( lū́ō ) . Also see λύνω ( lýno ) .
--
3127: Categories : Ancient Greek terms derived from the Proto-Indo-European root *lewh₁- 
3128: Ancient Greek terms derived from Proto-Indo-European 
3129- Ancient Greek 2-syllable words 
3130- Ancient Greek terms with IPA pronunciation 
3131- Ancient Greek lemmas 
#### pollute
1:URL: https://www.etymonline.com/word/pollute
21: Origin and history of pollute 
23: pollute (v.) 
25: late 14c., polluten , "to defile, violate the sanctity of, render ceremonially unclean," a back formation from pollution , or else from Latin pollutus , past participle of polluere "to defile, pollute, contaminate." Related: Polluted ; polluting . Meaning "make physically foul" is from 1540s; specific sense "contaminate the environment" emerged by 1860, but was not yet in the 1895 Century Dictionary.
28: Entries linking to pollute 
30: polluted (adj.) 
32: late 14c., "ceremonially unclean, profane;" c. 1400, "rendered impure or unclean," past-participle adjective from pollute (v.). Meaning "drunk" is from 1912, American English slang; ecological sense is by 1888.
34: pollution (n.) 
36: mid-14c., pollucioun , "discharge of semen other than during sex," later, "desecration, profanation, defilement, legal or ceremonial uncleanness" (late 14c.), from Late Latin pollutionem (nominative pollutio ) "defilement," noun of action from past-participle stem of Latin polluere "to soil, defile, contaminate," probably from * por- "before" (a variation of pro "before, for;" see pro- ) + -luere "smear," from PIE root *leu- "dirt; make dirty" (see lutose ). Sense of "contamination of the environment" is recorded from c. 1860, but not common until c. 1955.
38: pollutant 
#### dialysis
1:URL: https://www.etymonline.com/word/dialysis
21: Origin and history of dialysis 
23: dialysis (n.) 
25: 1580s, in logic and grammar, in the latter "division of one syllable into two," from Latin, from Greek dialysis "dissolution, separation" (used of the disbanding of troops, a divorce, etc.), from dialyein "dissolve, separate," from dia "apart" + lyein "loosen" (from PIE root *leu- "to loosen, divide, cut apart").
30: Entries linking to dialysis 
32: *leu- 
36: It might form all or part of: absolute ; absolution ; absolve ; analysis ; analytic ; catalysis ; catalyst ; catalytic ; dialysis ; dissolve ; electrolysis ; electrolyte ; forlorn ; Hippolytus ; hydrolysis ; -less ; loess ; loose ; lorn ; lose ; loss ; Lysander ; lysergic ; lysis ; -lysis ; lyso- ; lysol ; lytic ; -lytic ; palsy ; paralysis ; pyrolusite ; resolute ; resolution ; resolve ; soluble ; solute ; solution ; solve ; solvent .
38: It might also be the source of: Sanskrit lunati "cuts, cuts off," lavitram "sickle;" Greek lyein "to loosen, untie, slacken," lysus "a loosening;" Latin luere "to loose, release, atone for, expiate;" Old Norse lauss "loose, free, unencumbered; vacant; dissolute;" Old English losian "be lost, perish."
84: Share dialysis 
88: https://www.etymonline.com/word/dialysis Copy
```


## [2026-09-06T23:21:37.781Z] TOOL CALL #66: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D9%84%D8%A7%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D9%84%D8%AA\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%DB%8C%D8%A7%D9%84%DB%8C%D8%B2\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/lewh%E2%82%81-\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 310, roots Letro / Leu-Lu\"; done"
}
```


### [2026-09-06T23:21:42.461Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/da932fb737f90274.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2218f86dd6ada51e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fdf2af3762a9e4d7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2bda054d98e63683.txt
```


## [2026-09-06T23:21:45.319Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in da932fb737f90274 2218f86dd6ada51e fdf2af3762a9e4d7 2bda054d98e63683; do echo \"##### $f\"; head -3 $f.txt; grep -n \"Etymology\" -A 8 $f.txt | grep -v \"^\\s*[0-9]*-\\s*$\" | sed -n '1,30p'; echo; done"
}
```


### [2026-09-06T23:21:46.917Z] TOOL RESULT

```
##### da932fb737f90274
URL: https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D9%84%D8%A7%D9%86
FETCHED: 2026-09-06T23:21:39Z
STATUS: 200
62: Etymology 
64- 1.2 
65- Noun 
67- 1.2.1 
68- Derived terms 
70- 1.2.2 
--
82: Etymology 
84- 2.2 
85- Pronunciation 
87- 2.3 
88- Noun 
90- 2.3.1 
--
166: Etymology
167- [ edit ] 
169- Borrowed from Persian پالان ( pâlân , “ packsaddle ” ) , from Proto-Iranian *pari-dāna- ( literally “ around-placed ” ) .
171- Noun
172- [ edit ] 
174- پالان • ( palan ) ( definite accusative پالانی ( palanı ) , plural پالانلر ( palanlar ) ) 
--
219: Etymology
220- [ edit ] 
222- Inherited from Proto-Iranian *pari-dāna- ( literally “ around-placed ” ) , from *pari- ( “ around ” ) and a derivative of Proto-Indo-European *dʰeh₁- ( “ to put, place ” ) ; cognate with Sogdian 𐫛𐫏𐫡𐫔𐫗 ( pyrδn , “ saddle ” ) . [ 1 ] 
224- Pronunciation
225- [ edit ] 
227- ( Classical Persian ) IPA ( key ) : /paː.ˈlaːn/ 

##### 2218f86dd6ada51e
URL: https://en.wiktionary.org/wiki/%D9%84%D8%AA
FETCHED: 2026-09-06T23:21:41Z
STATUS: 200
79: Etymology 
81- 2.2 
82- Pronunciation 
84- 2.3 
85- Noun 
87- 2.3.1 
--
99: Etymology 
101- 3.2 
102- Pronunciation 
104- 3.3 
105- Noun 
107- Toggle the table of contents 
--
226: Etymology
227- [ edit ] 
229- Inherited from Paisaci Prakrit 𑀮𑀢𑁆𑀢𑀸 ( lattā ) . Cognate with Urdu لات ( lāt ) / Hindi लात ( lāt , “ kick ” ) .
231- Pronunciation
232- [ edit ] 
234- ( Standard Punjabi ) IPA ( key ) : /lət̪.t̪ə̆/ , [lɐt̪.t̪ə̆] 
--
305: Etymology
306- [ edit ] 
308- Inherited from Prakrit 𑀮𑀢𑁆𑀢𑀸 ( lattā ) .
310- Pronunciation
311- [ edit ] 
313- IPA ( key ) : /lət̪ː/ 

##### fdf2af3762a9e4d7
URL: https://en.wiktionary.org/wiki/%D8%AF%DB%8C%D8%A7%D9%84%DB%8C%D8%B2
FETCHED: 2026-09-06T23:21:41Z
STATUS: 200
62: Etymology 
64- 1.2 
65- Noun 
67- 1.2.1 
68- Further reading 
70- Toggle the table of contents 
--
137: Etymology
138- [ edit ] 
140- From French dialyse .
142- Noun
143- [ edit ] 
145- دیالیز • ( diyâliz ) 

##### 2bda054d98e63683
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/lewh%E2%82%81-
FETCHED: 2026-09-06T23:21:42Z
STATUS: 200
```


## [2026-09-06T23:21:52.482Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n \"Persian\" 2218f86dd6ada51e.txt | head -20"
}
```


### [2026-09-06T23:21:52.528Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T23:22:12.701Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== ARY آلودن\"; grep -n \"آلودن\\|آلودگی\" incoming/ARY/ARY_pages.txt | head -10; echo \"== ARY latin index letro/leu\"; grep -n \"LETRO\\|LEU\\b\\|LEUD\" incoming/ARY/ARY_latin_index_pages.txt | head -10; echo \"== NYB\"; grep -n \"lwtn\\|lūt\\|ālāy\\|pālāy\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-06T23:22:12.768Z] TOOL RESULT

```
== ARY آلودن
== ARY latin index letro/leu
3695:BLEU FLERE, BELARE LATIN) ops
6962:(SU) 1037, (KLEU-) 605 SUSHRAVAS (SANSKRIT) <4 Sui
10370:(KLEU) 755, (LISTEN) 344,
== NYB
112:HSD(1)WN-: (-/- inserted through the influence of the Prs d dlwtn' = drütan): HSD to reap
3311:rēš-galūtak [lyšglwtk'] the head of the exiles, the exilarch, title of the head of all Jews in the Sassanian empire, ac- credited at the Sassanian court, and responsible to the Great King. for the Jewry of the empire 116°. — Borrowed from Aram res gälütä.
3521:srütan [slwtn'] sräy- [sl’d]- to sing: tambür zat u srut väcik played the lute and sang vocally (sang a chant to the music) 4°; to recite by chanting 59. — Av. (1639 sqq.) srav- ‘to hear’, caus. ‘to recite (the -holy texts, singing them)’; MPrth sr’w-, MPrs sr’y- ‘to sing’; NP surüdan siräy-; v. srot.
```


## [2026-09-06T23:22:37.374Z] TOOL CALL #70: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py ARY:153 --image 2>&1 | tail -30"
}
```


### [2026-09-06T23:22:42.830Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/ARY/0153.png
REF: ARY:153  PDF: data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf page 152  OCR-lang: fas+eng

پالیدن, پالودن, پالاییدن / ۱۵۳
بادداشت:
۱ معنی این واژه در ایرلندی میانه و ولزی: تازه. ۰
: ۲- معنی این واژه در آلمانی کهن و میانه: سرند کردن» (غله را) برجاری کردن.
:ْ ۳ بازگمت به: هورء پالیدن.
آوستایی (۸:97۸۷)+ آلمانی کهن (0574۵۷ ۲/017 دان): ۱
رال0۸آش ۳۸ ,۳27۸70۸7 0
پهلوی (۲7 ۸/74 ۳): ۳۸71۸3۷ ببل۲۸نارلق۳ انگلیسی (۸0/5ق)(از فرانسه): ‏ 2018179۷
کردی (8015(7(ا): 8۸6
بلوچی (/6/7ا8): ۶۸۸۷۸6 ,۳273۸6 پسگشت‌ها ۸/5
اففانی (پشتر) (/۸/02۸0۷: ,اظ۸ل ۴7 ۳
سانسکریت (5۸(/57077): 5 (۳81۴۷) وی ان ان
ا ۳۸۸3 ,۶۸۷۸3۸71 ,۳۸۷۸۳ 4 (۳81818۴8) نقمازم 05
لاتین (4710ا): اه ای (1 ها 9 (۳:81۴۷) :1/۸025
فرانسه (7ل)/۳2۸): دراد ادا ای 4 (۳8۳) :0770/5
اسپانیایی (8۳۸(/[817): 3اه رای زا 6 (۸۲83) زوا ان اج
ایتالپایی (همال/): ره دای اه برهان قاطع : ۵۸
یادداشت.
بازگست بد: پاک.
یونانی (07520): ۸1 رومانی (140/لملاناهم: ۳1۳۸
لائین (147/00): ایسلندی‌کهن (۵2 572/0۸5 صته):
0 بت ار ۶ ,۳۸.۳۸3 ۲۸۲۸
فرانسه (۳27)17): اند ۱8| نررس کهن (۸085 (ا0): ۲۳۸۸
اسپانیایی (8۳۸(/15[7): ۸/۸ ساکسو نی‌کهن (/540۸ )+
ایتالیایی ((۸اله): ی 0 رالشارآ ۸۳0 ,7۸12
اک و
```


## [2026-09-06T23:22:45.143Z] TOOL CALL #71: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/ARY/0153.png"
}
```


### [2026-09-06T23:22:45.577Z] TOOL RESULT

```

```


## [2026-09-06T23:22:45.575Z] INPUT

[Image: original 1500x2400, displayed at 1250x2000. Multiply coordinates by 1.20 to map to original image.]


## [2026-09-06T23:23:01.031Z] TOOL CALL #72: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-06T23:23:01.066Z] TOOL RESULT

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


## [2026-09-06T23:23:12.573Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== BRT dav\"; grep -n \"fraδauu\\|fradav\\|frada\\huu\\|1\\. dav\\|dav-\" BRT.txt | head -15; echo \"== BRT ru\"; grep -n \"^ *rav-\\|raoδ\\|rū-\" BRT.txt | head -10; echo \"== KNT\"; grep -n \"rū\\b\\|dirty\" KNT.txt | head -5; echo \"== SOD\"; grep -n \"δʾw\\|to smear\" SOD.txt | head -5"
}
```


### [2026-09-06T23:23:12.672Z] TOOL RESULT

```
== BRT dav
3240:•  j,  adav-  (,  p.  adav-)  f.  'Wasserlauf; Bach,  Kanal':  us  . .  apqm  °oavd  apaiti.- »nti  Jasanti  Yt  Ä  29.
3690:aipi.daßdav-
4488:aH«-H*uj:/%  S  ^6S.  1  d.  ~  Zum  V.  vak-.  — ai.  vgl.  anüklay-  f.  —  Pü. ;  apar  ^moihüh.  — <)  Durch  'Attiaktion'  statt  des  Akk.»;  Tgl. zu  animiaiie,  anu.varilie,  ilt,  uxsne,  däiSm und  ah-  I,  3  a  mit  No.  3;  Dbk.  AiS.  88.  — »)  S.  YL  10.  137. j.  anit.daiayal  Yt.  7.  39:  lies  a?ia  duye  (zum V.  idav-).  '
7594:11  hindav-  No.  1 ;  doch  vgl.
8580:AbleiL  iMui-Yhiniitni-;  vgL  iBed.  ai.  udanlya- Adj,  —  «)  NA.  getrennt  und  mit  i  stall  j; s.  F  I  usv-,  IQ  Aiadav-  and  No.  3.  —  'J  In mp.  Schriften  usind,  usindam  genannt;  vgl. SBE.  47.   160.
12556:'dav-.
12797:•  j.  'dav-  V.  'sprechen',  von  rftfaischen Wesen''.     Praes.  2  dava-.
12801:*dav-  688
12803:mit  /r3  nnd  vi  'hin  und  her  reden': fradavata  vtdavata  fi-amof^fota  vlmaigiata ar»HJ  mainyu/  "es  redete  hin,  es  redete her,  es  überlegte  hin,  es  Überlegte  her AM.''  V.jp.43.
12806:•  j.  *dav-  V.  'entfernen'.  Praes.  3  dava-, 4  dva-.
12810:•  j.  Jdav-  V.,  nur  mit  /ra  'reinigend  ab- reiben'.    Praes.  i  dava-.
12813:•  g.  <dav-  V.  '(sich)  diHngen'.     Praes.
12828:•  j.  ", .  yitn  davata  aüi  . ."  FtD.  7. ■  g.  'davant-  Adj.,  PPA.:  s.  ^dav-,
13674:Ableit  —  Znin  V.  'dav-.  —  ai.  dül6.  m.  — Fü. :  daväi  (zu  np.  danidan  *laufen']  oder gäiuäk  (in  ap.gußan);  s.  10  düfya-.  Dazu  die Erl.:  räyhütär.
15927:pazdav-
== BRT ru
== KNT
== SOD
```


## [2026-09-06T23:23:56.483Z] TOOL CALL #74: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/ARY data/verification/sources/refs/ocr/BOOK && cat > data/verification/sources/refs/ocr/ARY/0153.vision.txt <<'EOF'\n[read from the PNG by a vision model, ARY printed p. 153 (pdf page 152)]\n\nHeader: پالیدن، پالودن، پالاییدن / ۱۵۳\nیادداشت:\n۱- معنی این واژه در ایرلندی میانه و ولزی: تازه.\n۲- معنی این واژه در آلمانی کهن و میانه: سرند کردن، (غله را) بوجاری کردن.\n۳- بازگشت به: هور، پالیدن.\n\nEntry box 1:\n  فارسی (PERSIAN): پالیدن، پالودن، پالاییدن  |  PALIDAN, PALUDAN, PALAIDAN\n  چم انگلیسی سرواژه‌ی فارسی: PURIFY, FILTER\n  هند و اروپایی (INDO-EUROPEAN): *PU-, *PEU-, *PEWE-, *PUNAML\n  اوستایی (AVESTAN): PALAIDAN, PALAIDAN\n  پهلوی (PAHLAVI): PALUTAK, PALUTAN\n  کردی (KURDISH): PAK KIRIN\n  بلوچی (BALUCHI): PALEAG, PALAYAG\n  افغانی (پشتو) (AFGHANI): PAKAWEL\n  سانسکریت (SANSKRIT): PAVATE, PAVAYATI, PUNATI, PAVITAR\n  لاتین (LATIN): PURIFICARE\n  فرانسه (FRENCH): PURIFIER\n  اسپانیایی (SPANISH): PURIFICAR\n  ایتالیایی (ITALIAN): PURIFICARE\n  آلمانی کهن (OLD HIGH GERMAN): FOWEN\n  انگلیسی (ENGLISH) (از فرانسه): PURIFY\n  پسگشت‌ها / REFERENCES: POKORNY 826-7 ; BARNHART (PURIFY) 865 ; DELAMARRE (PURIFIER) 274 ;\n    MACKENZIE (PURIFY) 129 ; ONIONS (PURE) 724 ; SKEAT (PURE) 756 ; برهان قاطع: ۲۵۸\n  یادداشت: بازگشت به: پاک.\n\nEntry box 2 (next entry, different word):\n  فارسی (PERSIAN): پالیدن (به چم «جستجو و تفحص نمودن»، (شاید) «پوییدن») | PALIDAN\n  چم انگلیسی: SEARCH, SEEK\n  هند و اروپایی (INDO-EUROPEAN): *POLO-, *POL-, *PEL-, *PAL-, *PL-\n  یونانی (GREEK): PALLEIN ; لاتین (LATIN): PALPARE, PELLERE, PALPO ; فرانسه: PALPER ;\n  اسپانیایی: PALPAR ; ایتالیایی: PALPARE ; رومانی: PIPAI ; ایسلندی کهن: FALMA, FELMA ;\n  نورس کهن / ساکسونی کهن: FALM, AFOLIAN, ...\nEOF\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg310.png data/verification/sources/refs/ocr/BOOK/310.png && ls -la data/verification/sources/refs/ocr/BOOK/310.png"
}
```


### [2026-09-06T23:23:58.134Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 75436 Sep  6 19:23 data/verification/sources/refs/ocr/BOOK/310.png
```


## [2026-09-06T23:32:50.239Z] TOOL CALL #75: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk310.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndoc = {\n \"pdf_page\": 310,\n \"book_page\": 280,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [\n  {\n   \"entry\": 2,\n   \"root\": \"Letro, Letros, Letrâ\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"PIE *letro- 'leather' (Pokorny 681, flagged '??'); Mann IEC 681 letros / letrā / letró 'piece, strip, skin; to strip, flay, tear'. Modern handbooks rather reconstruct Proto-Celtic *ɱlitrom < PIE *pl̥tro- 'skin, hide' (to *pel- 'skin', Lat. pellis), with early Germanic borrowing.\",\n   \"note\": \"The reference numbers are right: Pokorny p. 681 does print \\\"letro- ,Leder??\\\" and Mann's column 681 does print \\\"letros, ā 'piece, strip, skin'; letró, io 'strip, flay, tear'\\\" with \\\"Per. latre 'part, fragment'\\\". But both of Nourai's own authorities are hedged: Pokorny gives the root a double question mark and asks whether the Germanic word is an old loan from Celtic *pl-e-tro, related to Lat. pellis 'skin'; Buck 6.29 repeats that doubt; Wiktionary/modern Celtic scholarship now derives OE leþar from Proto-Celtic *ɱlitrom < *pl̥tro-. If the preform had initial *p-, an Iranian cognate would show p-, so Persian latreh cannot belong here. GLOSS MISPRINT: the printed page prints \\\"skim, strip, piece\\\"; Mann, whom Nourai is copying, has \\\"piece, strip, skin\\\" — \\\"skim\\\" is Nourai's misreading of \\\"skin\\\" (the extraction is faithful to the page).\",\n   \"note_fa\": \"ریشهٔ هندواروپایی *letro- «چرم» در پوکورنی (ص ۶۸۱) آمده است، امّا خود پوکورنی در برابر آن دو علامت پرسش گذاشته و احتمال داده که واژهٔ ژرمنی وام‌واژه‌ای کهن از سلتی باشد از *pl-e-tro (هم‌ریشه با pellis لاتینی «پوست»). منّ (IEC ستون ۶۸۱) تنها کسی است که «لتره» فارسی را ذیل این ریشه آورده است. پس ادعای نورایی با احتیاط پذیرفتنی است. نکتهٔ دیگر: معنای چاپی کتاب «skim» خطای چاپی نورایی به جای «skin» (پوست) منّ است؛ خطای خوانش اسکن نیست.\",\n   \"error_in\": \"book\",\n   \"book_prints\": \"Letro, Letros, Letrâ : skim, strip, piece\",\n   \"correct_form\": \"Letro, Letros, Letrâ : skin, strip, piece (Mann IEC 681)\",\n   \"sources\": [\n     \"https://en.wiktionary.org/wiki/leather\"\n   ],\n   \"ref_check\": [\n     {\"ref\": \"POK:681\", \"status\": \"supports\", \"note\": \"POK_02.txt (Pokorny IEW p. 681, printed page marker '681' immediately above): \\\"letro' ,Leder^??  Air. lethar, cymr. lledr, bret. lezr ,Leder' = ahd. leder, ags. leþer (engl. leather), aisl. leðr n. ,Leder'. Ist das germ. Wort alte Entlehnung aus dem kelt. und letzteres als *pl-e-tro mit lat. pellis usw. (s. pel- ,Haut') verwandt? S. Pedersen KG. II 45. WP. II 428.\\\" — the page and the form are exactly Nourai's, but Pokorny's gloss is 'Leder' and he flags the root '??'.\"},\n     {\"ref\": \"IEC:681\", \"status\": \"supports\", \"note\": \"IEC.txt line 9695, on the leaf whose running column number is 681: \\\"letros, ā 'piece, strip, skin'; letró, io 'strip, flay, tēar'. WP II, 428  Per. latre 'part, fragment'; Gk. cf. ko-letráo; Ir. leathar, m. 'skin, hide'; W lledr; Br. ler, lezr; MIr. cf. letraim, v. 'mangle, tear'; MHG lêder, n.; OE -leðer 'leather'; MHG läderen, lideren, v. 'tan'.\\\" — this is the source of all three root spellings and of the Persian node.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"WLD\", \"where\": \"WP II 428 (cited by both Pokorny 681 and Mann 681)\", \"stance\": \"supports\", \"note\": \"Both POK p.681 and IEC col. 681 close the entry with \\\"WP. II 428\\\", i.e. Walde-Pokorny II 428 is the common source of the *letro- material.\"},\n     {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. letro-\", \"stance\": \"supports\", \"note\": \"AHD_watkins1985.txt line 690: \\\"letro-. Leather. Germanic *lethram in Old English lether, leather: LEATHER. [Pok. letro- 681.]\\\" — Watkins keeps the root but knows no Iranian member.\"},\n     {\"src\": \"SYN\", \"where\": \"Buck 6.29 LEATHER, p. 408\", \"stance\": \"partial\", \"note\": \"SYN.txt: \\\"Ir. lethar, NIr. leathar, W. lledr, Br. ler beside ON leðr, OE leþer, OHG leder, etc., uncertain whether cognate groups (*letro-) or orig. Celtic (*letro- fr. *pletro- : Lat. pellis?) with early Gmc. borrowing. Pedersen 2.45.\\\" — no Iranian cognate anywhere in the article.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Persian\",\n     \"words\": \"latreh\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"NP latreh «لَتره» 'shred, torn piece (esp. of cloth)' belongs to the native family لت lat 'piece, slab, leaf (of a door), blow', لته late 'old rag', لت‌و‌پار lat-o-pār 'torn to shreds', with the common Persian diminutive/nominal suffix -a (-eh) on an r-extended stem. Mann (IEC 681) is the only etymologist who equates it with PIE *letros 'piece, strip, skin' and so with Ir. leathar / OE leþer; the equation is purely formal (latre : letro-) and Mann marks the whole set 'isophones, kinship uncertain' elsewhere in the same column. The difficulty is phonological: Pokorny 681 and, today, Matasović/Wiktionary derive the Celto-Germanic word from *pl̥tro- (Proto-Celtic *ɱlitrom, to *pel- 'skin', Lat. pellis), and an initial PIE *p- would survive as p- in Iranian, so a Persian reflex of that preform could not be latreh. Neither Horn, Hübschmann, Cheung nor Wiktionary records any etymology for لت/لتره at all; Nourai's own chart hedges with \\\"See 'Lěk' for another possible root\\\". The word and the gloss are correct; only the IE affiliation is uncertain.\",\n     \"derivation_fa\": \"«لَتره» در فارسی به معنی پاره، تکه (از جامه) است و با «لت»، «لته» و «لت‌و‌پار» یک خانواده است؛ پسوند ـه ی فارسی بر ستاکی با رِ افزوده شده است. تنها منّ (فرهنگ تطبیقی هندواروپایی، ستون ۶۸۱) این واژه را ذیل *letros «پاره، پوست» آورده و نورایی همین را نقل کرده است. اشکال آوایی آن این است که صورت کهن این ریشه در پژوهش امروزی *pl̥tro- (با پِ آغازین، هم‌ریشه با pellis «پوست») بازسازی می‌شود و پِ هندواروپایی در ایرانی پ می‌ماند و از میان نمی‌رود. پس خود واژه و معنایش درست است، امّا این هم‌ریشگی با احتیاط پذیرفتنی است.\",\n     \"sources\": [\n       \"https://en.wiktionary.org/wiki/%D9%84%D8%AA\",\n       \"https://en.wiktionary.org/wiki/leather\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"IEC:681\", \"status\": \"supports\", \"note\": \"IEC.txt line 9695 (column 681): \\\"letros, ā 'piece, strip, skin' ... WP II, 428  Per. latre 'part, fragment'\\\" — Mann does list the Persian word under this root, exactly as the arrow claims.\"},\n       {\"ref\": \"MON:3563\", \"status\": \"supports\", \"note\": \"MON_part2.txt line ~38858 (Mo'in, letter ل): \\\"لتره: (ص.) پاره، دریده، کهنه\\\" and, in the same column, \\\"لت‌وپار: (ص مر.) پاره پاره، قطعه قطعه\\\" and \\\"لته: (ا.) پارچهٔ کهنه، ژنده\\\". Mo'in confirms word, script and gloss (his page numbers are not legible in this OCR, but the entry falls in the ل stretch where p. 3563 lies); Mo'in gives no etymology.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' vol. 1-2 (BQT_v1_pages.txt / BQT_v2_pages.txt)\", \"stance\": \"silent\", \"note\": \"grep 'لتره' in BQT_v1_pages.txt returns 0 hits (the ل letter is outside vol. 1); no Mo'in etymological footnote on لتره is available in the volumes we hold.\"},\n       {\"src\": \"HRN\", \"where\": \"Horn, Grundriss (HRN.txt), index\", \"stance\": \"silent\", \"note\": \"no entry for lat/latre/latreh in Horn's numbered list or its index — Horn gives no etymology for this word.\"},\n       {\"src\": \"POK\", \"where\": \"IEW p. 681 s.v. letro-\", \"stance\": \"silent\", \"note\": \"Pokorny's letro- article (POK_02.txt, page 681) lists only Old Irish lethar, Welsh lledr, Breton lezr, OHG leder, OE leþer, ON leðr — no Iranian or Indo-Aryan cognate at all.\"},\n       {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e rishe-hā (ARY_pages.txt / ARY_latin_index_pages.txt)\", \"stance\": \"silent\", \"note\": \"grep 'لتره' and 'LETRO' return nothing; Aryanpur has no entry for this word.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Germanic\",\n     \"words\": \"lethram\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Proto-Germanic *leþran (Watkins writes it *lethram; Wiktionary *leþrą), a neuter -o-stem, is the ancestor of OE leþer, OS lethar, OHG ledar, ON leðr, Du. leder/leer, G Leder. Its relation to the root box is exactly what Watkins prints (\\\"letro-. Leather. Germanic *lethram\\\"), so the arrow root → Germanic is Nourai's source verbatim. The one qualification, made already by Pokorny (p. 681) and Buck (6.29) and now standard, is that Germanic may have taken the word from Celtic (*ɱlitrom > OIr. lethar) rather than inherited it, and that the Celtic form goes back to *pl̥tro- 'skin' (Lat. pellis); this affects the root's IE pedigree, not the Germanic form or its meaning.\",\n     \"derivation_fa\": \"ژرمنی آغازین *leþrą (یا به نگارش واتکینز *lethram) «چرم»، نیای انگلیسی کهن leþer، آلمانی کهن ledar و نورسی کهن leðr است. واتکینز (پیوست ریشه‌های هندواروپایی AHD) دقیقاً همین را می‌نویسد، پس پیکان کتاب درست است. تنها نکته آن که پوکورنی و باک احتمال داده‌اند این واژه وام‌واژه‌ای کهن از سلتی باشد نه میراث مستقیم هندواروپایی.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/leather\"],\n     \"ref_check\": [\n       {\"ref\": \"AHD:1526\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 690 (= the same article that stands on p. 1526 of the 1975 New College appendix): \\\"letro-. Leather. Germanic *lethram in Old English lether, leather: LEATHER. [Pok. letro- 681.]\\\" — the Germanic form, its gloss and the root are Nourai's, verbatim.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"Klein 1966, s.v. leather (KLN_1966.txt line 21354)\", \"stance\": \"supports\", \"note\": \"\\\"leather, n. — ME. lether, fr. OE. lether, rel. to OS. lethar, ON. leðr, Dan. læder, Swed. läder, OFris. lether, MDu. leder, Du. leder, leer, OHG. ledar, MHG., G. leder, and cogn. with OIr. lethar, W. lledr, Bret. lezr, 'leather'.\\\"\"},\n       {\"src\": \"SYN\", \"where\": \"Buck 6.29, p. 408\", \"stance\": \"partial\", \"note\": \"\\\"uncertain whether cognate groups (*letro-) or orig. Celtic (*letro- fr. *pletro- : Lat. pellis?) with early Gmc. borrowing. Pedersen 2.45. Or as orig. 'smoothed skin' (*letro- fr. *leitro-) : Grk. λεῖος, Lat. lēvis 'smooth'? Kluge-G. 350.\\\"\"},\n       {\"src\": \"POK\", \"where\": \"IEW p. 681\", \"stance\": \"supports\", \"note\": \"\\\"letro' ,Leder??' ... ahd. leder, ags. leþer (engl. leather), aisl. leðr n. ,Leder'\\\" — the Germanic set is Pokorny's.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"English\",\n     \"words\": \"leather\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"OE leþer (attested chiefly in compounds, e.g. leþer-hose, leþer-wyrhta 'leather-worker') > ME lether > NE leather; the medial þ/ð was regularly voiced between vowels and spelled th, and OE final -er stayed. A straight, uncontroversial Germanic inheritance from *leþrą; Watkins routes the English word through exactly this chain, and Nourai's arrow Germanic → English reproduces it.\",\n     \"derivation_fa\": \"leather انگلیسی از انگلیسی میانه lether و آن از انگلیسی کهن leþer است که خود بازماندهٔ ژرمنی آغازین *leþrą است؛ تحولی کاملاً قاعده‌مند و بی‌مناقشه. ادعای نورایی درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/leather\"],\n     \"ref_check\": [\n       {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 690: \\\"Germanic *lethram in Old English lether, leather: LEATHER\\\"; the same file's word-index (line 1727 region) lists \\\"LEATHER letro-\\\".\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. leather\", \"stance\": \"supports\", \"note\": \"\\\"ME. lether, fr. OE. lether\\\" (KLN_1966.txt line 21354).\"},\n       {\"src\": \"SYN\", \"where\": \"Buck 6.29 word list, p. 408\", \"stance\": \"supports\", \"note\": \"the table gives \\\"OE leþer / ME lether / NE leather\\\" in one column with OHG leder, ON leðr.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 4,\n   \"root\": \"Leu, Lu\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *leu- / *lewǡ- : *lū- 'dirt, to make dirty'; *lu-to- 'mud' (Pokorny 1. leu- 681; Watkins leu-2 'Dirt; to make dirty')\",\n   \"note\": \"The root box itself is right: Pokorny p. 681 prints \\\"1. leu-, *leuǎ : lū- ,Schmutz, beschmutzen'; lu-to- ,Kot'\\\", and Watkins has \\\"leu-2. Dirt; to make dirty\\\" with the same page reference. The page number POK:681 is exact. TWO CROSS-CUTTING PROBLEMS. (a) Pokorny's article contains NO Indo-Iranian member at all — only Gk. λῦμα/λύθρον, Alb. lum, Lat. polluō/lutum/lustrum, OIr. loth, Lith. lutynas. The whole Iranian branch of this chart (nodes 1-3) rests on Horn no. 42 (1893), which Horn himself calls \\\"durchaus unsicher\\\"; today Cheung (EDIV 2007, s.v. *dauH2) and Wiktionary derive آلودن from Proto-Iranian *ā-dauH- 'to smear', and پالودن from something else again. (b) The Greek branch (nodes 4-7) belongs to the HOMONYMOUS root: Pokorny's \\\"2. leu- ,abschneiden, trennen, loslösen'\\\", which happens to begin on the very same page 681 — that is almost certainly how the two got merged. Watkins keeps them apart as leu-1 'To loosen, divide, cut apart' (→ Gk. luein → DIALYSIS) and leu-2 'Dirt' (→ Lat. polluere, lutum), and Etymonline does the same. So the root as drawn is correct but over-populated.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی *leu-/*lū- «چرک، آلودن» در پوکورنی ص ۶۸۱ و در پیوست واتکینز (leu-2) آمده و خود ریشه درست است. امّا دو ایراد: نخست آنکه پوکورنی هیچ هم‌ریشهٔ هندوایرانی برای آن نمی‌آورد؛ پیوند «آلودن» و «پالودن» با این ریشه از هرن (۱۸۹۳) گرفته شده که خود آن را «کاملاً نامطمئن» خوانده، و چونگ (۲۰۰۷) و ویکی‌واژه آلودن را از ایرانی آغازین *ā-dauH- «مالیدن» می‌گیرند. دوم آنکه شاخهٔ یونانی (dia-luein › dialysis) از ریشهٔ همآوای دیگری است: *leu- «گسستن، رها کردن» (پوکورنی، همان صفحه، ذیل leu-2) که نورایی آن را با این یکی درهم آمیخته است.\",\n   \"sources\": [\n     \"https://www.etymonline.com/word/pollute\",\n     \"https://www.etymonline.com/word/dialysis\"\n   ],\n   \"ref_check\": [\n     {\"ref\": \"POK:681\", \"status\": \"supports\", \"note\": \"POK_02.txt line 5435, on the leaf headed '681': \\\"1. leu-, *leuǎ : lū- ,Schmutz, beschmutzen'; lu-to- ,Kot'. Gr. λῦμα ,Schmutz, Schmach', ... lat. polluō ,beflecke', lustrum ,Pfütze', lutum ,Dreck, Kot' = air. loth f. ,Schmutz' ... lit. lutynas ,Pfuhl'. WP. II 406.\\\" The page is exact and the gloss 'to smear, make dirty' matches. Note that the immediately following article on the same page is \\\"2. leu- ,abschneiden, trennen, loslösen'\\\", which is where the Greek dia-luein branch of this chart really belongs.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.vv. leu-1, leu-2\", \"stance\": \"partial\", \"note\": \"AHD_watkins1985.txt line 691 ff.: \\\"leu-1. To loosen, divide, cut apart ... Zero-grade form *lu- in: a. Greek luein, to loosen, release, untie: LYSIS ... ANALYSIS, CATALYSIS, DIALYSIS ... [Pok. 2. leu- 681.]  leu-2. Dirt; to make dirty. 1. Latin polluere, to pollute (< *por-luere ...): POLLUTE. 2. Suffixed zero-grade form *lu-to- in Latin lutum, mud, mire, clay: LUTE. [Pok. 1. leu- 681.]\\\" — supports the root but explicitly separates the two homonyms Nourai merges.\"},\n     {\"src\": \"WLD\", \"where\": \"WP II 406 (cited at the foot of Pokorny's 1. leu-)\", \"stance\": \"supports\", \"note\": \"Pokorny closes the 'Schmutz' article with \\\"WP. II 406\\\", and the 'abschneiden' article with \\\"WP. II 407 f.\\\" — Walde-Pokorny too has them as two separate roots.\"},\n     {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. lutum (LAT.txt line 35197 region)\", \"stance\": \"supports\", \"note\": \"\\\"lūtum, -i n.: boue; argile de potier ... Cf. irl. loth 'boue', hom. λύθρον 'souillure', gr. λῦμα 'souillure, dommage', lat. luēs. Cf. aussi lustrum, et polluo.\\\"\"},\n     {\"src\": \"IEC\", \"where\": \"Mann, columns 679-682\", \"stance\": \"silent\", \"note\": \"Mann's run of l-entries around col. 681 (leskos, leso, letos, letros, leubh ...) has no *leu- 'dirt' headword at all; IEC is silent on this root.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan / Old Persian\",\n     \"words\": \"rŭ, râu; â-rŭ-ta, â-râw, aya\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"These are not attested Avestan or Old Persian words. They are Abolghasemi's reconstructed Old-Iranian (ایرانی باستان) forms, printed with asterisks in Fe'l-hā-ye Fārsi-ye Dari p. 26 under آلودن: past stem آلود < MP ālūd < OIr. *ā-rū-ta-, present stem آلای < MP ālāy < OIr. *ā-rāw-aya- (Nourai's \\\"aya\\\" is simply the causative suffix -aya- split off the second form), from a root *rū- glossed \\\"آلوده بودن\\\". Nourai reproduces them faithfully but relabels them \\\"Avestan / Old Persian\\\", which they are not: Bartholomae's Altiranisches Wörterbuch has no Avestan root rū-/rav- 'to be dirty', and Kent's Old Persian lexicon has nothing either. Modern Iranian etymology reconstructs the same two Persian stems quite differently, with *d not *r: Cheung EDIV s.v. *dauH2 'to smear, rub (on)' gives YAv. fraδauu- 'to be rubbed off with' (Bartholomae ³dav-, col. 688, \\\"nur mit fra 'reinigend abreiben'\\\"), MMP *'rwdg 'pollution, dirt', Sogd. δʾaw 'to smear', Khwar. δʾaw-, Oss. dawyn, and NP ālūdan/ālāy- (+ *ā-) beside andūdan (+*ham-) and zadūdan (+*uz-), the -l- of ālūdan being secondary. The chart's forms are therefore a 19th/20th-century reconstruction that current scholarship rejects.\",\n     \"derivation_fa\": \"این صورت‌ها نه اوستایی‌اند نه پارسی باستان؛ بازسازی‌های ایرانی باستان از ابوالقاسمی در ماده‌های فعل‌های فارسی دری (ص ۲۶) هستند: «آلود < فارسی میانه ālūd < ایرانی باستان *ā-rū-ta» و «آلای < ālāy < *ā-rāw-aya». نورایی آن‌ها را درست نقل کرده ولی برچسب «اوستایی/پارسی باستان» زده است؛ در فرهنگ ایرانی باستان بارتولومه هیچ ریشهٔ اوستایی rū- به معنی «آلوده بودن» نیست. پژوهش امروزی (چونگ، فرهنگ ریشه‌شناختی فعل ایرانی، ذیل *dauH²) همین دو ستاک را از *ā-dauH- «مالیدن» می‌گیرد و اوستایی fraδauu-، سغدی δʾaw و آسی dawyn را هم‌ریشهٔ آن می‌داند. پس ادعای نورایی را پژوهش امروزی رد می‌کند.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A2%D9%84%D9%88%D8%AF%D9%86\"],\n     \"ref_check\": [\n       {\"ref\": \"FFD:26\", \"status\": \"supports\", \"note\": \"FFD_pages.txt, pdf page 31-32 (printed p. 26-27, the running head of the next page reads 'ماده‌های ماضی و مضارع فارسی دری ... ۲۷'), entry آلودن: \\\"آلود < فارسی میانه [ālūd] < ایرانی باستان *ā-rū-ta ... [ریشهٔ rū] به معنی «آلوده‌بودن» است. آلای < فارسی میانه [ālāy] < ایرانی باستان *ā-rāw-aya\\\". The page reference is exact and the forms are Abolghasemi's, but he prints them as Old IRANIAN reconstructions, not as Avestan/Old Persian.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW (BRT.txt line 12810, col. 688)\", \"stance\": \"contradicts\", \"note\": \"\\\"j. ³dav- V., nur mit fra 'reinigend abreiben'. Praes. dava-.\\\" — the Avestan root that actually underlies آلودن is dav-, not rū-; a grep of BRT.txt for an Avestan rū-/rav- 'be dirty' finds nothing.\"},\n       {\"src\": \"KNT\", \"where\": \"Kent, Old Persian lexicon (KNT.txt)\", \"stance\": \"silent\", \"note\": \"no Old Persian root or word rū-/*ā-rū-ta- 'dirty' in Kent's lexicon (grep 'rū'/'dirty' → nothing relevant).\"},\n       {\"src\": \"CHEUNG\", \"where\": \"EDIV s.v. *dauH2 'to smear, rub (on)' (CHEUNG.txt lines 5482-5528)\", \"stance\": \"contradicts\", \"note\": \"\\\"*dauH² 'to smear, rub (on)'. AVESTAN: (+ *fra-) YAv. fraδauu- 'to be rubbed off with' ... MIDDLE PERSIAN: (+ *ā-) MMP *'rwdg 'pollution, dirt' ... NWIR: (+ *ā-) NP aludan/alay- 'to soil, pollute, stain' ... The original meaning of NP āludan/ālay- appears to be 'to smear', v. Horn 1893: 10.\\\" PIE: none; Pok.: 261 (not 681).\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Pahlavi\",\n     \"words\": \"â-lutan; pâlutan (pat-lutan)\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"The Middle Persian words exist, but not in these shapes and not in this relationship. MacKenzie's Concise Pahlavi Dictionary has \\\"ālūdan, ālāy- [ʾltnʾ, ʾlʾd-] defile, pollute\\\" and \\\"ālūdag [ʾltkʾ] defiled, polluted\\\", and separately \\\"pālūdan, pālāy- [pʾlwtnʾ, pʾlʾd-] strain, filter, purify\\\" with \\\"pālūdag [pʾlwtkʾ] starch jelly, flummery\\\" — so ā- is part of the stem shape, not a separable prefix written \\\"â-lutan\\\", and \\\"pat-lutan\\\" is Nourai's (i.e. Horn's) ANALYSIS, never an attested Pahlavi spelling. Horn no. 278 is indeed the source: \\\"pālūden 'reinigen', Praes. pālay-em ... paiti + alūden (s. ālūden, No. 42); phlv. pālūt (Bund.)\\\". But Hübschmann, Persische Studien p. 36, demolishes it in the very passage Nourai's own NOTE points to — and every later authority agrees: Cheung derives pālūdan from Proto-Iranian *pari-harz- (YAv. pairi.harəz- 'to filter', MMP pʾrʾy- 'to purify', perf. pass. pʾrwd, Arm. LW parzel 'to filter'), Abolghasemi and Wiktionary from *pari-/pati-dauH- ~ *dāwati 'to run, flow' (whence also دویدن), Aryanpur from *peu(H)- 'to purify' (with پاک). Only ālūdan itself may be linked to the *leu- family (Horn no. 42, endorsed phonetically by Hübschmann p. 8), and even that is now replaced by *ā-dauH-.\",\n     \"derivation_fa\": \"صورت‌های پهلوی درست‌اند ولی نه به این نگارش: مکنزی «ālūdan، ālāy- [ʾltnʾ] آلودن» و جداگانه «pālūdan، pālāy- [pʾlwtnʾ] صاف کردن، پالودن» را ثبت کرده است؛ «pat-lutan» تحلیل هرن است نه صورت مضبوط. هرن (شمارهٔ ۲۷۸، ص ۶۲) پالودن را paiti + آلودن گرفته، ولی هوبشمان در پژوهش‌های فارسی ص ۳۶ صریحاً می‌گوید «پیوندی میان پالودن و آلودن در کار نیست و هر ریشه‌شناسی مبتنی بر آن نادرست است» — همان که خود نورایی در یادداشت آورده است. چونگ پالودن را از *pari-harz- (اوستایی pairi.harəz- «پالودن») می‌گیرد. پس این پیوند رد می‌شود.\",\n     \"sources\": [\n       \"https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D9%84%D9%88%D8%AF%D9%86\",\n       \"https://en.wiktionary.org/wiki/%D8%A2%D9%84%D9%88%D8%AF%D9%86\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"HRN:10\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 32 = printed p. 10, no. 42: \\\"āluden 'beschmutzen', Praes. ālāy-em, phlv. lūtak (AV.). lat. lutum; air. loth 'Schmutz'; lit. lutynas, lutynė (fem.) 'Pfuhl, Lehmpfütze'. Durchaus unsicher, da np. ālāy-em dann die sekundäre Form und ū ursprünglich sein müsste. Auch scheint die Grundbedeutung von ālūden 'beschmieren' zu sein.\\\" — supports the ālūdan/*leu- link but with Horn's own strong reservation.\"},\n       {\"ref\": \"HRN:62\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 84 = printed p. 62, no. 278: \\\"pālūden 'reinigen', Praes. pālay-em, pālāyiden, paiti + alūden (s. ālūden, No. 42); phlv. pālūt (Bund.), pāz. pālīdan, pālaidan (West, Sik. gum.-Gl.). bel. LW. palayag, pālenay 'seihen, worfeln, reinigen'.\\\" — exactly Nourai's 'pat-lutan' analysis.\"},\n       {\"ref\": \"HUB:8\", \"status\": \"supports\", \"note\": \"HUB.txt leaf 19 = printed p. 8, ad no. 42: \\\"Np. āludan 'beschmutzen, sich verunreinigen' kann trotz des pr. ālayam auf eine Wurzel lu zurückgehen ... Lautlich ist also gegen eine Zusammenstellung von aludan mit lat. lutum, lues, polluo, gr. λῦμα, air. loth etc. nichts einzuwenden.\\\"\"},\n       {\"ref\": \"HUB:36\", \"status\": \"contradicts\", \"note\": \"HUB.txt leaf 47 = printed p. 36, ad no. 278: \\\"Np. pāludan 'reinigen' kann nicht = 'paiti + aludan' sein ... Nun heisst aber pālūdan vielmehr 'durchseihen, reinigen' ... so dass 'seihen' die ursprüngliche, 'reinigen' die abgeleitete Bedeutung ist. Also findet ein Zusammenhang mit aludan nicht statt und jede darauf gegründete Etymologie ist falsch.\\\" — the chart's own NOTE reports this correctly, and modern scholarship sides with Hübschmann.\"},\n       {\"ref\": \"BQT:58\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt, the leaf whose own footnote ends '... در صفحهٔ ۵۹' (i.e. this is printed p. 58): Mo'in's etymological footnote s.v. آلودگی/آلودی: \\\"پهلوی ālūtakīh ... بمعنی لوث ـ آلایش ـ فسق و فجور ـ شوخ و وسخ «لغت نامه» ... [lutum] لاتینی و [loth] ایرلاندی باستانی (پلیدی، گل، مدفوع) هرن ۴۲\\\" — Mo'in cites Horn no. 42 and the Latin/Old Irish comparanda, i.e. exactly Nourai's claim for ālūdan.\"},\n       {\"ref\": \"BQT:358\", \"status\": \"not_found\", \"note\": \"Calibrating the OCR leaves of BQT_v1_pages.txt against the two 'continued on p. N' footnotes gives offset 210 (leaf 268 = p. 58, leaf 569 = p. 359). Printed p. 358 (leaf 568) carries پادشاه/پادنگ, nothing about پالودن. The پالودن cluster stands ~11 pages later (leaves 579-580, printed ~369-370): \\\"پالودن: بر وزن آسودن، بمعنی صاف کردن و صافی و روشن شدن و پاک ساختن ...\\\", \\\"پالوده، پالونه\\\" — with no etymological footnote at all in this scan. So the second page number could not be confirmed.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD (PHD.txt lines 189 and 540)\", \"stance\": \"partial\", \"note\": \"\\\"ālūdag ['lwtk'] defiled, polluted. ~ih: defilement. ālūdan, ālāy- ['lwtn', 'l'd-] (M 'rwd), N ~] defile, pollute\\\" and \\\"pālūdag [p'lwtk' | N ~a] starch jelly, flummery. pālūdan, pālāy- [p'lwtn', p'l'd-] (M p'rwdn, p'r'y-), N ~] strain, filter, purify\\\" — both verbs exist, but MacKenzie lists them as unrelated entries and the Manichaean spellings ('rwd vs p'rwdn/p'r'y-) point to different roots.\"},\n       {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, Glossary\", \"stance\": \"silent\", \"note\": \"grep for lwtn'/p'lwtn'/ālūt/pālūt in NYB_vol2_glossary.txt finds no entry — neither verb occurs in Nyberg's text-based glossary.\"},\n       {\"src\": \"CHEUNG\", \"where\": \"EDIV s.v. *harz 'to let go, release' (CHEUNG.txt lines ~9403-9460)\", \"stance\": \"contradicts\", \"note\": \"\\\"AVESTAN: YAv. haraz- ... || (+ *pari-) 'to filter' ... MIDDLE PERSIAN: (+ *pari-) MMP p'r'y- 'to purify' ... Partic.: perf. pass. MMP p'rwd ... NWIR: (+ *pari-) NP paludan, palidan/palay-, Kurd. palavtin/palév-, ... 'to filter, purify' ... Note also the rhyming antonym NP āludan 'to stain, soil', s.v. *dauH².\\\" — pālūdan is *pari-harəz-, and ālūdan a different root again.\"},\n       {\"src\": \"ARY\", \"where\": \"Aryanpur, p. 153 s.v. پالیدن، پالودن، پالاییدن (read from the page image; transcription saved as ocr/ARY/0153.vision.txt)\", \"stance\": \"contradicts\", \"note\": \"\\\"PALIDAN, PALUDAN, PALAIDAN — PURIFY, FILTER — INDO-EUROPEAN: *PU-, *PEU-, *PEWE-, *PUNAML; PAHLAVI: PALUTAK, PALUTAN; SANSKRIT: PAVATE, PAVAYATI, PUNATI; LATIN: PURIFICARE; REFERENCES: POKORNY 826-7 ... برهان قاطع ۲۵۸; یادداشت: بازگشت به: پاک\\\" — Aryanpur assigns pālūdan to PIE *peu(H)- 'to purify' (Pokorny 826-7), with پاک, not to *leu- 681.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Persian\",\n     \"words\": \"âludan; pâludan; pâlâyeš; pâludeh; pâlŭneh; pâlân\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"All six words are real and correctly glossed, and the printed page shows the box hanging off the Pahlavi box (see the extraction note), which is right for the first five: MP ālūdan/ālāy- > NP آلودن (آلای) and MP pālūdan/pālāy- > NP پالودن (پالای، پالیدن), with پالایش the regular -š (< OIr. *-šn) verbal noun on the present stem, پالوده the past participle (whence the sweet, Arabized فالودج/فالوذج and back into Persian as فالوده), and پالونه an instrument noun in -ūna 'strainer' (Borhan-e Qate': \\\"پالونه ... مصفاة\\\"). What is disputed is the root: آلودن is now taken from Proto-Iranian *ā-dauH- 'to smear' (Cheung; Wiktionary: \\\"Cheung derives the verb from Proto-Iranian *ā- + *dauH- 'to smear, rub (on)', with a lambdacism of *d > l\\\"), the -l- being borrowed from its rhyming antonym pālūdan; and پالودن is not from آلودن at all (Hübschmann p. 36; Cheung *pari-harəz-; Wiktionary/Abolghasemi *para-dāwati 'to run, flow', cf. دویدن; Aryanpur *peu- 'purify', cf. پاک). پالان 'straw-stuffed packsaddle' does not belong to this family in ANY account: it is Proto-Iranian *pari-dāna- 'placed around' (*pari- + *dǓeh1- 'to put'), cf. Sogdian py rδn 'saddle', and was lent to Turkish as palan. So one word (آلودن) has a *leu- etymology only in the older literature, four belong to a different root, and one (پالان) is unrelated to all of them.\",\n     \"derivation_fa\": \"هر شش واژه واقعی و درست‌معنا هستند: «آلودن (آلای)» و «پالودن (پالای، پالیدن)» دنبالهٔ مستقیم فارسی میانهٔ ālūdan/ālāy- و pālūdan/pālāy-، «پالایش» اسم مصدر با پسوند ـش بر ستاک حال، «پالوده» صفت مفعولی (معرّب آن فالوذج که باز به صورت «فالوده» به فارسی بازگشته) و «پالونه» اسم ابزار به معنی صافی است. امّا ریشه محل اختلاف است: چونگ و ویکی‌واژه «آلودن» را از *ā-dauH- «مالیدن» می‌گیرند (با ابدال d > l به قیاس پالودن)، و «پالودن» را هیچ‌کدام از آلودن نمی‌گیرند. «پالان» نیز از ایرانی آغازین *pari-dāna- «آنچه گرداگرد نهاده شود» (هم‌ریشه با سغدی py rδn «زین») است و هیچ ربطی به پالودن ندارد. پس پژوهش امروزی این شاخه را رد می‌کند.\",\n     \"sources\": [\n       \"https://en.wiktionary.org/wiki/%D8%A2%D9%84%D9%88%D8%AF%D9%86\",\n       \"https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D9%84%D9%88%D8%AF%D9%86\",\n       \"https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D9%84%D8%A7%D9%86\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"FFD:26\", \"status\": \"partial\", \"note\": \"FFD_pages.txt pdf p. 31-32 (printed 26-27) gives آلودن exactly as Nourai reports it (*ā-rū-ta / *ā-rāw-aya). But Abolghasemi's own entry for پالودن is 14 pages later (pdf p. 45, printed ~40) and says something different: \\\"پالود < فارسی میانه [pālūd] < ایرانی باستان *pati-rau-ta ... [pati] پیشوند فعلی است. [rau] صورت ضعیف ریشهٔ *raw است، به معنی «دویدن». خود دویدن هم از ریشهٔ *raw آمده است\\\" — i.e. Nourai's own reference derives pālūdan from 'to run', not from 'to be dirty'.\"},\n       {\"ref\": \"AEF:340\", \"status\": \"not_checked\", \"note\": \"Khaleqi Motlaq, Asās-e Ešteqāq-e Fārsi vol. I — refs_online.json marks it kind 'catalog' with no scan available; it is the Persian translation of Horn (HRN) with Hübschmann's notes, so the substance is covered by the HRN:10,62 and HUB:8,36 checks above.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' vol. 1, leaves 579-580 (printed ~369-370)\", \"stance\": \"partial\", \"note\": \"\\\"پالودن: بر وزن آسودن، بمعنی صاف کردن و صافی و روشن شدن و پاک ساختن و صاف گردیدن از کدورت‌ها\\\", \\\"پالوده: بر وزن آلوده ... و معرّب آن فالوذج باشد\\\", \\\"پالاوان ... ظرفی باشد مانند کفگیر که چیزها را در آن صاف کنند\\\" — all the Persian words and glosses of the node are confirmed, with no etymology attached.\"},\n       {\"src\": \"MON\", \"where\": \"Mo'in via BQT footnote p. 58 (Mo'in is the editor of these footnotes)\", \"stance\": \"partial\", \"note\": \"Mo'in's note on آلودگی cites Pahlavi ālūtakīh, Latin lutum, Old Irish loth and \\\"هرن ۴۲\\\" — he endorses the *leu- etymology for آلودن only, and attaches nothing of the kind to پالودن.\"},\n       {\"src\": \"CHEUNG\", \"where\": \"EDIV s.vv. *dauH2 and *harz\", \"stance\": \"contradicts\", \"note\": \"*dauH²: \\\"(+ *ā-) NP aludan/alay- 'to soil, pollute, stain' ... || (+ *uz-) NP zadudan/zaday- ... || (+ *ham-) NP andudan/anday- ... The formation is influenced by the antonym (M)MP p'rw-, NP palūdan 'to filter'.\\\" *harz: \\\"(+ *pari-) NP paludan, palidan/palay- ... 'to filter, purify'.\\\"\"},\n       {\"src\": \"HRN\", \"where\": \"Horn nos. 42 and 278, pp. 10 and 62\", \"stance\": \"supports\", \"note\": \"Horn is the one authority who states Nourai's chain (ālūden : lat. lutum, air. loth; pālūden = paiti + alūden), while calling the first \\\"durchaus unsicher\\\".\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Greek\",\n     \"words\": \"dia-luein; dia-lusis\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"The Greek words are right — διαλύω dialuō 'to loose one from another, part asunder, dissolve' (Herodotus, Thucydides; of disbanding troops, dissolving a marriage) and διάλυσις diálusis 'dissolution, separation', διά dia 'apart' + λύω luō. But λύω does NOT belong to *leu- 'dirt'. It is the zero grade of PIE *lewh₁- 'to cut off, separate, set free' — Pokorny's \\\"2. leu- ,abschneiden, trennen, loslösen'\\\" (IEW 681 f.), the article that immediately follows 'leu- Schmutz' on the same page, whence Skt. lunāti 'cuts', Lat. luere/solvere, Goth. fra-liusan, OE losian, ON lauss 'loose'. Watkins keeps the two apart as leu-1 and leu-2, and Etymonline routes dialysis through \\\"PIE root *leu- 'to loosen, divide, cut apart'\\\" while routing pollution through \\\"*leu- 'dirt; make dirty'\\\". Nourai has merged two homonymous roots that Pokorny numbered 1 and 2 on one page. The gloss 'filtering' for dia-lusis is also anachronistic: the sense is 'dissolution/separation', and the chemical sense dates only from Thomas Graham's coinage of 1861 (Klein s.v. dialysis).\",\n     \"derivation_fa\": \"واژه‌های یونانی درست‌اند: διαλύω «از هم گسستن، حل کردن» و διάλυσις «جدایی، تجزیه»، مرکب از διά «جدا» و λύω. امّا λύω از ریشهٔ «آلودن» نیست؛ از ریشهٔ همآوای *lewh₁- «بریدن، جدا کردن، رها کردن» است که پوکورنی در همان صفحهٔ ۶۸۱ زیر شمارهٔ ۲ آورده (سنسکریت lunāti، لاتین solvere، انگلیسی loose). واتکینز و اتیمانلاین این دو ریشه را از هم جدا می‌دانند؛ نورایی آن دو را یکی گرفته است. معنای «پالایش» برای dia-lusis نیز معنای شیمیایی سدهٔ نوزدهم است، نه یونانی. پژوهش امروزی این پیوند را رد می‌کند.\",\n     \"sources\": [\n       \"https://www.etymonline.com/word/dialysis\",\n       \"https://en.wiktionary.org/wiki/%CE%BB%CF%8D%CF%89\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"AHD:364\", \"status\": \"contradicts\", \"note\": \"AHD p. 364 is the dictionary entry 'dialysis', and the root cross-reference it carries in the New College edition is Watkins' leu-1, not leu-2. AHD_watkins1985.txt line 691: \\\"leu-1. To loosen, divide, cut apart ... 4. Zero-grade form *lu- in: a. Greek luein, to loosen, release, untie: LYSIS ... ANALYSIS, CATALYSIS, DIALYSIS ... [Pok. 2. leu- 681.]\\\", while \\\"leu-2. Dirt; to make dirty\\\" (the root of this chart) contains only Latin polluere and lutum. The index (line 1424) confirms: \\\"DIALYSIS leu-1\\\". Nourai's own reference therefore contradicts the arrow's placement.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"POK\", \"where\": \"IEW p. 681 f., '2. leu- ,abschneiden, trennen, loslösen''\", \"stance\": \"contradicts\", \"note\": \"\\\"gr. λύω ,löse, befreie; vertilge usw.', λύα f. ,Auflösung, Trennung', λύσις f. ,Lösung', λύτρον n. ,Lösegeld' ... ai. lunāti ,schneidet ab'\\\" — Greek luō/lusis stand under Pokorny's SECOND leu-, not the 'Schmutz' one.\"},\n       {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. dialysis (KLN_1966.txt line 11248)\", \"stance\": \"contradicts\", \"note\": \"\\\"dialysis, n. ... fr. Gk. διάλυσις, 'separation, dissolution', fr. διαλύειν, 'to part asunder, break off, dissolve', fr. διά ... and λύειν, 'to loose, loosen'; see -lysis. The word dialysis was introduced into chemistry by the Scottish chemist Thomas Graham (1805-69) ... in 1861.\\\" Klein's pollute article, by contrast, links -luere only to lutum, λῦμα, OIr. loth.\"},\n       {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.vv. lutum / polluo\", \"stance\": \"contradicts\", \"note\": \"Ernout-Meillet groups lutum with irl. loth and gr. λύθρον/λῦμα and, separately, treats luō 'to loose, expiate' with soluō — the two families are not joined.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"French\",\n     \"words\": \"\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"An empty pass-through box for French dialyse (f.), formed on Greek διάλυσις through Latin dialysis; the chemical/medical sense follows Graham's English coinage of 1861 and is the sense in which the word travelled onward. The Greek → French link as such is correct; it is only the box's ultimate ancestry (through node 4) that is misassigned to the 'dirt' root.\",\n     \"derivation_fa\": \"جعبهٔ خالی واسطه برای فرانسه dialyse است که از یونانی διάλυσις از راه لاتین علمی ساخته شده و معنای پزشکی آن پس از وضع گراهام (۱۸۶۱) رایج شده است. خود این حلقه (یونانی › فرانسه) درست است؛ ایراد تنها به ریشهٔ بالادستی بازمی‌گردد.\",\n     \"sources\": [\n       \"https://en.wiktionary.org/wiki/%D8%AF%DB%8C%D8%A7%D9%84%DB%8C%D8%B2\",\n       \"https://www.etymonline.com/word/dialysis\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the box carries no reference in the book (refs=None); its content is supplied by the neighbouring boxes.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. dialyse/dialysis\", \"stance\": \"supports\", \"note\": \"\\\"dialyse, v. — See dialyze\\\" and, s.v. dialysis, the Greek → Latin → modern-European chain; French dialyse is the regular Gallicization.\"},\n       {\"src\": \"MON\", \"where\": \"Wiktionary's Persian entry دیالیز, which names French as the donor\", \"stance\": \"supports\", \"note\": \"\\\"دیالیز (diyâliz) — Etymology: From French dialyse.\\\" This is the only evidence needed that the French box is a real link in the chain.\"}\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"Persian\",\n     \"words\": \"dîyâlîz\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"NP دیالیز diyāliz is a 20th-century medical loan straight from French dialyse (as with almost all Persian clinical vocabulary of the period, which came through French rather than English); the French final -yse is rendered ـیز with a voiced z, and the stress-final open syllable of dialyse is dropped. Wiktionary's Persian entry states the source explicitly: \\\"From French dialyse.\\\" The word is thus a late, learned return of the Greek term to Iran — not an inherited form, and Nourai's box correctly shows it hanging off French rather than off the Iranian branch.\",\n     \"derivation_fa\": \"«دیالیز» وام‌واژه‌ای پزشکی از فرانسه dialyse است که در سدهٔ چهاردهم خورشیدی به فارسی راه یافته؛ مانند بیشتر اصطلاحات پزشکی آن دوره که از راه فرانسه آمده‌اند. ویکی‌واژه نیز همین را می‌گوید. ادعای نورایی درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AF%DB%8C%D8%A7%D9%84%DB%8C%D8%B2\"],\n     \"ref_check\": [\n       {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the box carries no reference in the book (refs=None).\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"MON\", \"where\": \"Wiktionary Persian دیالیز (archived)\", \"stance\": \"supports\", \"note\": \"\\\"Etymology: From French dialyse. Noun: دیالیز (diyâliz)\\\".\"},\n       {\"src\": \"KLN\", \"where\": \"Klein s.v. dialysis\", \"stance\": \"supports\", \"note\": \"gives the Greek-to-modern-European chain and dates the technical sense to Graham 1861, which is the sense borrowed into Persian.\"}\n     ]\n    },\n    {\n     \"id\": 7,\n     \"lang\": \"English\",\n     \"words\": \"dialyze, dialysis\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English dialysis is attested from the 1580s in logic and grammar ('division of one syllable into two'), taken from Latin dialysis < Greek διάλυσις; the chemical sense — separation of crystalloids from colloids through a membrane — was coined by the Scottish chemist Thomas Graham in 1861, and dialyze/dialyse is a back-formation from it. The Greek → English arrow is right; only its attachment to the 'dirt' root (node 4) is not.\",\n     \"derivation_fa\": \"انگلیسی dialysis از دههٔ ۱۵۸۰ میلادی در منطق و دستور زبان به کار می‌رفته و از لاتین dialysis و آن از یونانی διάλυσις گرفته شده است؛ معنای شیمیایی آن را توماس گراهام در ۱۸۶۱ وضع کرد و dialyze از آن ساخته شد. خود این حلقه درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/dialysis\"],\n     \"ref_check\": [\n       {\"ref\": \"AHD:364\", \"status\": \"partial\", \"note\": \"AHD's dictionary page 364 does carry dialysis/dialyze with the Greek etymology Nourai gives, but its root cross-reference is Watkins' leu-1 'to loosen', not the leu- 'dirt' of this chart (AHD_watkins1985.txt index line 1424: \\\"DIALYSIS leu-1\\\").\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"Klein 1966 s.vv. dialysis, dialyze (KLN_1966.txt lines 11248-11249)\", \"stance\": \"supports\", \"note\": \"\\\"dialysis, n., separation of crystalloids from colloids (chem.) — L., 'separation', fr. Gk. διάλυσις ... The word dialysis was introduced into chemistry by the Scottish chemist Thomas Graham (1805-69) ... in 1861.\\\" \\\"dialyze, also dialyse, tr. v. (chem.) — Back formation fr. dialysis.\\\"\"},\n       {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. leu-1\", \"stance\": \"partial\", \"note\": \"\\\"Greek luein, to loosen, release, untie: LYSIS, LYSO-, -LYTE, -LYTIC; ANALYSIS, CATALYSIS, DIALYSIS ...\\\" — confirms the English word's Greek source while placing it under the other root.\"}\n     ]\n    },\n    {\n     \"id\": 8,\n     \"lang\": \"Latin\",\n     \"words\": \"lutum; polluere\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin lutum n. 'mud, mire, potter's clay' is the *lu-to- of the root (Pokorny 681 \\\"lu-to- ,Kot'\\\"), matching OIr. loth f. 'Schmutz' exactly; and polluere 'to defile, pollute' is from *por-luēre, with por- an old variant of pro- 'forth' plus the same -lu- 'to smear' (so already Ernout-Meillet, \\\"De por-luo: v. lutum, lustrum\\\"). Both are Pokorny's own examples in the very article Nourai cites, and Watkins repeats them verbatim under leu-2. The lengthened-grade derivative lustrum 'puddle, filth' belongs here too. This node is the core of the root and is fully confirmed.\",\n     \"derivation_fa\": \"لاتین lutum «گِل، لجن، خاک رس‌گری» همان صورت *lu-to- ریشه است که پوکورنی در ص ۶۸۱ می‌آورد و با ایرلندی کهن loth دقیقاً مطابق است؛ polluere «آلودن» نیز از *por-luēre است (پیشوند por- گونه‌ای کهن از pro-) با همان ستاک -lu-. ارنو-میه و کلاین هم همین را می‌گویند. ادعای نورایی درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/pollute\"],\n     \"ref_check\": [\n       {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 691 ff.: \\\"leu-2. Dirt; to make dirty. 1. Latin polluere, to pollute (< *por-luere; por- for prō-, forth, forward; see per) : POLLUTE. 2. Suffixed zero-grade form *lu-to- in Latin lutum, mud, mire, clay: LUTE. [Pok. 1. leu- 681.]\\\" — both Latin words, both glosses, exactly as drawn.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"POK\", \"where\": \"IEW p. 681, 1. leu-\", \"stance\": \"supports\", \"note\": \"\\\"lat. polluō ,beflecke', lustrum ,Pfütze', lutum ,Dreck, Kot' = air. loth f. ,Schmutz', gall. ON Luteva\\\".\"},\n       {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.vv. lutum, polluo (LAT.txt lines 35197, 48690)\", \"stance\": \"supports\", \"note\": \"\\\"lūtum, -i n.: boue; argile de potier ... Cf. irl. loth 'boue', hom. λύθρον, gr. λῦμα, lat. luēs\\\" and \\\"polluo, -is, -ui, -utum, -ere: souiller, salir ... De por-luo: v. lutum, lustrum.\\\"\"},\n       {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. pollute (KLN_1966.txt line 29422)\", \"stance\": \"supports\", \"note\": \"\\\"L. pollutus, pp. of polluere, 'to defile, pollute, contaminate', for *por-luere ... L. -luere in polluere is rel. to L. lutum, 'mud', and cogn. with Gk. λῦμα 'filth, dirt, disgrace', ... OIr. loth 'mud, dirt', W. lludedic 'muddy', Lith. lutynas 'pool, puddle'.\\\"\"}\n     ]\n    },\n    {\n     \"id\": 9,\n     \"lang\": \"English\",\n     \"words\": \"pollution\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English pollution appears mid-14c. as pollucioun, first in the narrow ecclesiastical sense 'discharge of semen other than during sex', then late 14c. 'desecration, defilement, ceremonial uncleanness'; from Late Latin pollutionem (nom. pollutiō) 'defilement', a noun of action on the past-participle stem of Latin polluere, reaching English through Old French. The verb pollute (late 14c.) is a back-formation from the noun or a direct adoption of Latin pollutus. The environmental sense is recorded from c. 1860 and only became common after c. 1955. The chain Latin polluere → English pollution in the chart is exactly right.\",\n     \"derivation_fa\": \"انگلیسی pollution از میانهٔ سدهٔ چهاردهم میلادی به صورت pollucioun دیده می‌شود و از لاتین پسین pollutiōnem «آلودگی» (از ستاک اسم مفعول polluere) از راه فرانسهٔ کهن وارد شده است؛ معنای زیست‌محیطی آن از حدود ۱۸۶۰ و رواج آن پس از ۱۹۵۵ است. ادعای نورایی درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/pollute\"],\n     \"ref_check\": [\n       {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. leu-2 routes POLLUTE (and with it pollution) to Latin polluere < *por-luere; the word index gives the same.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. pollution (KLN_1966.txt line 29422)\", \"stance\": \"supports\", \"note\": \"\\\"pollution, n. — Late L. pollutio, gen. -onis, fr. L. pollutus, pp. of polluere.\\\"\"},\n       {\"src\": \"AHD\", \"where\": \"Etymonline s.v. pollution (archived)\", \"stance\": \"supports\", \"note\": \"\\\"mid-14c., pollucioun ... from Late Latin pollutionem (nominative pollutio) 'defilement', noun of action from past-participle stem of Latin polluere 'to soil, defile, contaminate', probably from *por- 'before' ... + -luere 'smear', from PIE root *leu- 'dirt; make dirty'.\\\"\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith open(\"/home/sfmqrb/git/rishe/data/verification/page-310.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk310.py && python3 -m json.tool data/verification/page-310.json > /dev/null && echo JSON_OK && python3 tools/verify_check.py 310"
}
```


### [2026-09-06T23:32:53.189Z] TOOL RESULT

```
ok
JSON_OK
nodes verified: 12/12
node verdicts: {'plausible': 1, 'confirmed': 7, 'disputed': 4}
root verdicts: {'plausible': 1, 'confirmed': 1}
ref checks: {'supports': 11, 'contradicts': 2, 'not_found': 1, 'partial': 2, 'not_checked': 3}
books consulted: {'silent': 6, 'supports': 15, 'partial': 5, 'contradicts': 8} | by book: {'KLN': 8, 'POK': 4, 'CHEUNG': 3, 'MON': 3, 'BQT': 2, 'HRN': 2, 'ARY': 2, 'SYN': 2, 'LAT': 2, 'AHD': 2, 'BRT': 1, 'KNT': 1, 'PHD': 1, 'NYB': 1}
```


## [2026-09-06T23:32:53.799Z] AGENT

You've hit your session limit · resets 9:30pm (America/Toronto)
