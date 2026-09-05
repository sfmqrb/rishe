# Verification process log — verify-page-116


## [2026-09-05T17:49:39.831Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 116 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-116.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-116.json. Write /home/sfmqrb/git/rishe/data/verification/page-116.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 116` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T17:49:41.297Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T17:49:42.069Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T17:49:42.079Z] TOOL RESULT

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


## [2026-09-05T17:49:42.607Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-116.txt"
}
```


### [2026-09-05T17:49:42.629Z] TOOL RESULT

```
1	=== PDF page 116 (book page 86) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Del, Dlgho : long  (refs POK:197; KNT:190)
4	#1 (parent #0) [Avestan] refs=POK:197; BQT:829; SNS:324 | daraga, daragâ, drâjah : long ; drang : hesitation
5	  #2 (parent #1) [Persian] refs=POK:197; BQT:829,841; SNS:182 | derâz «دراز» : long ; dîr «دیر» : late ; derang «درنگ» : length of time, hesitation
6	#3 (parent #0) [Sanskrit] refs=SNS:182 | dîrğâ : late
7	#4 (parent #0) [Old Persian] refs=KNT:190 | darga : long
8	#5 (parent #0) [Germanic] refs=AHD | langaz : long
9	  #6 (parent #5) [English] refs=None | long ; belong ; along
10	#7 (parent #0) [Latin] refs=AHD | longus : long
11	  #8 (parent #7) [English] refs=None | oblong ; prolong ; longitude
12	--- entry 1 ---
13	ROOT [Indo-European] Dem, Domu : house  (refs POK:198)
14	#1 (parent #0) [Avestan] refs=POK:199; KNT:302 | demâna, nmâna, mân 3 : house ; garô-demâna : prayer house, sky ☞Gwer 2
15	  #2 (parent #1) [Pahlavi] refs=BQT:894,1949 | mân : house ; dŭtak-mân : smoke house. ☞Dheu 2 | NOTE: Family members who sit around a fire
16	    #3 (parent #2) [Persian] refs=SNS:239 | mân «مان ۲» : house ; dŭdmân «دودمان» : family
17	  #4 (parent #1) [Persian] refs=BQT:1793 | garzmân «گرزمان» : sky
18	#5 (parent #0) [Old Persian] refs=KNT:202 | mâna 2 : house ; mânya : domestic, house servant
19	#6 (parent #0) [Latin] refs=AHD | dominus : lord of the house ; domina : lady of the house
20	  #7 (parent #6) [French] refs=AHD:782 | ma-dame : my lady
21	    #8 (parent #7) [Persian] refs=MON:3681 | mâdâm «مادام»
22	    #9 (parent #7) [English] refs=AHD:782 | Madame
23	  #10 (parent #6) [Italian] refs=OEW:58 | don : lord ; donna, ma-donna : lady, my lady
24	    #11 (parent #10) [English] refs=OEW:58 | Madonna
25	  #12 (parent #6) [English] refs=AHD | dome ; domestic ; domain ; dominate ; condominium ; danger ; dungeon
26	#13 (parent #0) [Germanic] refs=None | 
27	  #14 (parent #13) [English] refs=AHD | timber
28	
```


## [2026-09-05T17:49:45.696Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-116.json",
 "description": "Read page 116 source JSON"
}
```


### [2026-09-05T17:49:45.728Z] TOOL RESULT

```
{
  "pdf_page": 116,
  "book_page": 86,
  "entries": [
    {
      "root": {
        "name": "Del, Dlgho",
        "lang": "Indo-European",
        "refs": "POK:197; KNT:190",
        "gloss": "long"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:197; BQT:829; SNS:324",
          "words": [
            {"translit": "daraga, daragâ, drâjah", "gloss": "long", "script": null},
            {"translit": "drang", "gloss": "hesitation", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "POK:197; BQT:829,841; SNS:182",
          "words": [
            {"translit": "derâz", "gloss": "long", "script": "دراز"},
            {"translit": "dîr", "gloss": "late", "script": "دیر"},
            {"translit": "derang", "gloss": "length of time, hesitation", "script": "درنگ"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "SNS:182",
          "words": [
            {"translit": "dîrğâ", "gloss": "late", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "KNT:190",
          "words": [
            {"translit": "darga", "gloss": "long", "script": null}
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
            {"translit": "langaz", "gloss": "long", "script": null}
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
            {"translit": "long", "gloss": null, "script": null},
            {"translit": "belong", "gloss": null, "script": null},
            {"translit": "along", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "longus", "gloss": "long", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "oblong", "gloss": null, "script": null},
            {"translit": "prolong", "gloss": null, "script": null},
            {"translit": "longitude", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Dem, Domu",
        "lang": "Indo-European",
        "refs": "POK:198",
        "gloss": "house"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:199; KNT:302",
          "words": [
            {"translit": "demâna, nmâna, mân 3", "gloss": "house", "script": null},
            {"translit": "garô-demâna", "gloss": "prayer house, sky", "script": null, "see": ["Gwer 2"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:894,1949",
          "words": [
            {"translit": "mân", "gloss": "house", "script": null},
            {"translit": "dŭtak-mân", "gloss": "smoke house.", "script": null, "see": ["Dheu 2"]}
          ],
          "note": "Family members who sit around a fire",
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "SNS:239",
          "words": [
            {"translit": "mân", "gloss": "house", "script": "مان ۲"},
            {"translit": "dŭdmân", "gloss": "family", "script": "دودمان"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1793",
          "words": [
            {"translit": "garzmân", "gloss": "sky", "script": "گرزمان"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "KNT:202",
          "words": [
            {"translit": "mâna 2", "gloss": "house", "script": null},
            {"translit": "mânya", "gloss": "domestic, house servant", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "dominus", "gloss": "lord of the house", "script": null},
            {"translit": "domina", "gloss": "lady of the house", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "French",
          "refs": "AHD:782",
          "words": [
            {"translit": "ma-dame", "gloss": "my lady", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "MON:3681",
          "words": [
            {"translit": "mâdâm", "gloss": null, "script": "مادام"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 7,
          "lang": "English",
          "refs": "AHD:782",
          "words": [
            {"translit": "Madame", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 6,
          "lang": "Italian",
          "refs": "OEW:58",
          "words": [
            {"translit": "don", "gloss": "lord", "script": null},
            {"translit": "donna, ma-donna", "gloss": "lady, my lady", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "English",
          "refs": "OEW:58",
          "words": [
            {"translit": "Madonna", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 6,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "dome", "gloss": null, "script": null},
            {"translit": "domestic", "gloss": null, "script": null},
            {"translit": "domain", "gloss": null, "script": null},
            {"translit": "dominate", "gloss": null, "script": null},
            {"translit": "condominium", "gloss": null, "script": null},
            {"translit": "danger", "gloss": null, "script": null},
            {"translit": "dungeon", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 0,
          "lang": "Germanic",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "timber", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-05T17:49:46.378Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T17:49:46.415Z] TOOL RESULT

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


## [2026-09-05T17:49:50.498Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KNT','BQT','SNS','AHD','MON','OEW','WLD','IEC','SYN']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n    print()\n\""
}
```


## [2026-09-05T17:49:51.037Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n 1,120p tools/verify_check.py"
}
```


### [2026-09-05T17:49:52.701Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

OEW {"title": "J. T. Shipley, The Origins of English Words: A Discursive Dictionary of Indo-European Roots, Baltimore 1984", "edition_found": "1984 (lending-only)", "kind": "archive_restricted", "url": "https://archive.org/details/originsofenglish0000ship ; https://archive.org/details/originsofenglish00jose (both JHU 1984, borrowable) ; HathiTrust mdp.49015002910322 search-only ; Google ELSm5zUgP_wC no view", "identifier": "originsofenglish00jose (also originsofenglish0000ship)", "local_file": null, "page_offset": null, "lookup_hint": "Borrow via IA lending (djvu.txt returns 401/403). Entries are 

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
```


### [2026-09-05T17:49:52.752Z] TOOL RESULT

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


## [2026-09-05T17:49:59.009Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -60 && echo ---- && grep -n \"dlonghos\\|dlongho\\|del-5\\|delegh\" POK_full.txt | head -30"
}
```


### [2026-09-05T17:49:59.081Z] TOOL RESULT

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
----
8831:lemma: del-5\ "long': Baltic with unexplained o'-loss (see below): Lithuanian ilgas, f. ilga, 
17699:Root / lemma: del-5 
17705:widespread extension delegh-3iU6 (d)longho-{see finally Persson Beitr. 889, 903 Anm. 1) 
17719:delegh-, djjgho-: 
17966:It is a common trait of alb. and Lithuanian to drop the initial da- as in Root/ lemma: del-5\ 
20002:lemma: del-5\ "long': Baltic with unexplained o'-loss (see below): Lithuanian ilgas, f. ilga. 
20651:The phonetic shift da- > a-, zero\s a common Baltic lllyrian. Compare Root / lemma: del-5
```


## [2026-09-05T17:50:01.049Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('POK_full.txt',encoding='utf-8',errors='replace').read()\nfor m in re.finditer(r'dem-|dṓm|demā?n|nmāna', t):\n    pass\n# find headword-ish lines\nidx=[m.start() for m in re.finditer(r'\\bdel-\\b', t)][:20]\nprint(len(t))\nprint(idx)\nEOF"
}
```


### [2026-09-05T17:50:03.106Z] TOOL RESULT

```
3967710
[327661, 700113, 702147, 703634, 710550, 711887, 712559, 725739, 815742, 821832, 850133]
```


## [2026-09-05T17:50:05.836Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '17690,17790p' POK_full.txt"
}
```


### [2026-09-05T17:50:05.896Z] TOOL RESULT

```
Note: 

Middle Irish deltxu. 'dew'; bret. o'e// 'humid, wet, moist ' display alb.-illyr -k > -th, -t 
subsequents. 

References: Petersson Heterokl. 198 f., different Kluge''"' under 'tallow, suet'. 
Page(s): 1 96 

Root / lemma: del-5 

Meaning: long 

Note: to put away more confidently only for Slavic, but probably the basis for the 

widespread extension delegh-3iU6 (d)longho-{see finally Persson Beitr. 889, 903 Anm. 1) 

Material: Perhaps here Old Norse /5//77a 'hinder'. Middle Low German talmen '\o\ter, be 

slow in talking and at work, stupid talk', Norwegian Dialectal Ma 'hesitate, wait, hold on', 

/^/e 'rogue, fool ' (Persson Beitr. 889); 



Old Church S\a\/'\c pro-cfb//t/"[ir\KO\/a\\ russ. c///tb' protract, hesitate', dlinai. 'length', 
Czech diei. "length', 07/// "hesitate', etc (Berneker 252); perhaps vi> dalj§^ far, aloof 
(Meillet MSL.14, 373; Berneker 177 besides other supplements). 

delegh-, djjgho-: 

zero grade Old Indie dTrgha- = Avestan daraga-, daraya-. Old pers. o'5/ig5-"long', zero 
grade compounds Superl. draghJyas-, draghistha- " longer, for a long time ', Avestan drajyo 
Adv. "further', drajistam Mn . " longest', npers. oV/az (actually comparative) "long'. Old 
Indie draghiman-, draghman-vn. "length, duration', Avestan drajdv\. "stretch, length'; 

gr. £v5£A£xn<; "continuous, persistent, enduring' ("*drag out'), evSeAexsw " continue ', 
SoAixoq "long' (to is. Schwyzer Gr. Gr. I 278, different Specht Dekl. 126), 56Aixo(; "the long 
racecourse '; 

about alb. g/ateeic see below; 

Note: 

Clearly alb. {* da-lu-ga-as-ti) g/atelong' derived from Hittite da-lu-ga-as-ti {dalugasti) n. 
"length': Old Church Slavic oyb^o/a" length' (= Old Indie dTrghata): proto Slavic. *dlgostb, 
poln. diugosc etc ds. 

Alb. and Baltic forms agree in dropping the initial d- > zero, which means that Baltic 
cognates originated from proto lllyrian: 

Alb. {* da-lu-ga-as-tl) g/ate'\ong, tall, high': Lithuanian I/gas, f. /7ga, Latvian /Igs, Old 
Prussian /7ga and ilgikdv. "long'; alb. is the only IE lang. where {* da-lu-ga-as-ti) g/ate'\ong' 
means also "tall, high' hence the name Alba Longa capital of Etruscan settlers is an alb. 
concept of building fortresses on hilltops of future Rome. 

Latin presumably indulged^ to be forbearing, patient, indulgent; to give oneself up to, 
indulge in; grant, allow, concede' (: £v5£A£xn<;, basic meaning then "be patient to 
somebody compared with, hold on patiently') from * en-dolgh-ejo. 

Maybe alb. {^ en-dolgh-ejo) Geg. ndigjoj, Tosc degjoj^ listen, hear, be submissive ', gjegj^ 
answer', Tosc ndelej, ndejej, ndjej^ feel', ndiej^ feel, hear'. 

cymr. dal, dala, daly^\\o\d, stop', bret. dalc'h^ possession ', derc'he/ 'ho\d, stop' (/"diss, 
from / compare participle dalc'het) presumably with the meaning-development as Modern 



High German " after which last ' to "long' (basic form *del(9)gh-, Zupitza BB. 25, 90 f., 
Pedersen KG. 152, 106); 

Maybe nasalized alb. ndar\\o\A, stop' : cymr. dal, dala, o'a/y'hold, stop'. 

Gothic /i//g^5 "tight, firm, steadfast' C*long, persistent, enduring '), Old Saxon tulgo My. 
"very'. Old English tulge, compounds /y/g" better, rather', Superl. tylgest^besX; 

Baltic with unexplained d-\oss (see below): Lithuanian ilgas, f. ilga, Latvian Ugs, Old 
Prussian //gaand ilgiMv. "long'; 

Old Church Slavic dli^g-b, serb. dug. Old Czech diuhy, russ. o'd/^y"long' (= Old Indie 
dTrgha-), in addition serb. duzi. "length'; Old Church Slavic o/b^o/a "length' (= Old Indie 
dTrghata); proto Slavic. *dlgostb, poln. diugosceic ds.; 

Hittite Nom. PI. da-lu-ga-e-es {dalugaes) "long', da-lu-ga-as-ti {dalugasti) n. "length'. 

/d/longho-s: 

a) Middle Persian drang, npers. d/ranglong' (but alb. g/ate, gjate, 5/a/"long' at first from 
*dlagh-t-); 

b) Latin /onguslong; spacious; of time, long, of long duration; esp. too long, tedious; of 
persons, prolix, tedious', Gothic /aggs, Old English Old High German Modern High 
German /ang{0\6 High German /angen ^become long, seem long, long, want', etc); but 
Old Irish etc /ong's\r\\p' seems to be borrowed from Latin {navis) longa; nevertheless, 
because of second meaning "vessel' and Middle Irish coblach^i\ee\! {*kom-uo-log- or *-lug- 
) though Loth (RC. 43, 133 f.) holds that word for genuine Celtic; compare also abrit. FIN 
Aoyyoc; (Ptol.) and gall. VN AOrrO-ZTAAHTEZ (Aude); aniaut. dl- remains preserved 
otherwise Celtic. In the group b) would display an already common West Indo Germanic 
simplification, might be connected with the o'-loss of Baltic ilgas . compare also Specht 
Dekl. 126.
```


## [2026-09-05T17:50:09.284Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '17790,17830p' POK_full.txt"
}
```


### [2026-09-05T17:50:09.335Z] TOOL RESULT

```
Maybe Alba Longa (Rome) capital of lllyrian - Etrus. : lllyrian AlbanollH 

References: WP. I 812 f., WH. I 694 f., 820 f., Trautmann 55, Pedersen Hittite 34 f. 
Page(s): 196-197 

Root / lemma: demel- 
Meaning: worm 



Material: Epidaur. 5£p£A£a(;f. Akk. PI., 5£MpA£T(; p5£AAai Hes.; 

perhaps alb. dhemje 'caterp\\\ar, inchworm' (could stand for *dhem//e), dhemfze, 
dhimfze^ meat maggot '. 

References: WP. I 790. 
Page(s): 201 

Root / lemma: {dema^, doma-, doiria- 

Meaning: to tame 

Material: Old Indie damyati^ is tamed; tamed ' {*dm-ietl), damta-^ tamed ' {*dm-t6s)\ Kaus. 

o'5/775y5// "tames, overmasters ' {*domeJd), participle damita-; dam/tar- ^ tamer'; dam/tva' 

taming ', damayat/" tames' {*doma-jo= Latin domd); dama-h' domesticating ', dama-h' 

taming '; 

osset. domun^ tame', npers. o'a/T? "domesticated animal'; after Pisani Crest. Indeur.2 113 
here (as *drn-so-s) o'asa-/? "fiend, non-Aryan ', actually "slave', but because of the 
incredible stem formation; 

gr. SapvaiJi, Ionian -r||Ji, Aor. £-5apa(a)aa (for *£-5£Maaa) "tame', various secondary 
reshaped, as Sapvau) etc, navSapaTwp " the all-subduer, all-tamer ', Doric SpaToc; "tamed' 
{*dm-t6s), hom. a5fjr|T0c; and aSpnc;, -htoc; " untamed, unrestrained, unwed, unmarried ', 
Ionian Perf. 5£5pr|MC('. SpnTHP "tamer', Spnaiq " taming, domestication'; 

forms with root vowel care missing in Gr.;
```


## [2026-09-05T17:50:09.882Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Root / lemma: dem-\\|Root / lemma: dem\" POK_full.txt | head"
}
```


### [2026-09-05T17:50:09.932Z] TOOL RESULT

```
17796:Root / lemma: demel- 
17881:Root / lemma: dem-, dema- 
17987:Root / lemma: dem-, derna-: "to build; house' derived from Root/ lemma: ghei-2. ghi-:
```


## [2026-09-05T17:50:12.917Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '17881,17995p' POK_full.txt"
}
```


### [2026-09-05T17:50:12.975Z] TOOL RESULT

```
Root / lemma: dem-, dema- 

Meaning: to build; house 

Material: Gr. Sspu) 'build', from the heavy basis participle Perf. Pass. 5£5pr|M£voq, Doric 

(Pindar) vEoSparoi; ' newly built', 

5£pa(; n. ' physique, shape' (\^zoob^r\, Attic inschr. -pvr| ' spanning crossbeams in the 

middle of the building ', yet n [a] could also be suffix). 



The meaning " settle, fit' in Gotliic ga-timan, Old Saxon teman, Old High German zeman 
"suit, fit', wherefore lengthened grade Goth\c ga-tem/Pa Adv. " befitting ', Middle Low 
German be-tame' fitting'. Old High German g/-zam/^ proper' and abstract zero grades Old 
High German zumft. Middle High German zumft, zunfV propriety, rule, association, guild ' 
{*drn-ti-) = Middle Irish det' disposition, temperament ' (Old Irish det/ae^bo\6, daring'), 
mcymr. danf temperament, character' (mostly Plur. de/nt), basic form *dm-to-. Loth RC 
46, 252 f. compare mcymr. cynnefin^ trustful ' (common Celtic -ns-, -nt- > -nn-), ( *kom- 
dam-Tno-). 

rostem Old Icelandic ///77it>/'" timber'. Old Saxon timbar. Old English timber^ Wrwber, 
edifice, building, building'. Old High German z/mbar't\rr\ber, building, dwelling, chamber', 
whereof Gothic t/mrjan 'buM', Old Norse timbra. Old High German z/mberen ar\d zimbaron 
" build, do carpentry, do woodwork '. 

root nouns dem-, dom-, dm-, dm- house'. 

Old \r\6\c patir dan ^ householder', Avestan d§ng patois' master of (*lord of the house)' 
with Gen. *dem-s, as also gr. 5£a-n6Tr|<; 'master, mister' (see Risch IF. 59, 12, Schwyzer 
Gr. Gr. I 547 f.). Old Indie dam-pa ff-hlor6, master' (new shifting together from *dan pat/- 
[= Avestan dang pati-], less probably with Lok. Aryan * dam as 'master in the house'); 

Avestan Lok. d^m, dqm/"\r\ the house', Lok. PI. dahv-a, Nom. -dairom proto Aryan *- 
das\r\ usi-5a r\arwe of a mountain range ('having one's house by the aurora '), wherefore 
probably Avestan ha-damoi'Lok. 'in the same house'; 

Armenian tunHorw. Akk. 'house' {*ddm), Instr. tamb{*dm-bhi), whereupon Gen. Dat. 
tan, 

gr. £v-5ov Lok., originally 'inside in house' (also reshaped to £v5o-9i, -0£v, £v5oi), 
perhaps also 5(1) {*d^m]) as Nom. Akk. Sg. n. or Lok.; 5(I)pa, 5(ji)ijaT0(; originally Akk. 
Sg.mask. *ddm-m\N\tb structure in Neutr. after arpajpa ; derivative Apia, Mvia, Aapia 
('mistress of the house'); 

as 1 . composition part in 5a|j-ap 'wife' ( *d9m-rf' governing of the house '), 5aTT£5ov ' floor 
(originally of the house)' from * dm-pedom (^an£5ov out of it after the concurrent of 5a- and 
^a- as intensive prefix; so perhaps also Ionian ^aKopo(; ' temple male servant, temple 
female servant' for *5a-Kopoq) = Swedish tomt, Old Icelandic /O/O/ 'place for edifice, 
building' in Norwegian Mdarten 'loam' (Germanic *tum-fetiz, Indo Germanic *drn-ped-). 



compare also Lithuanian dim-stis' courtyard, property; courtyard ' (2. part *sto-s\.o *sta- 
■stand"). 

o-stem domo-s:0\A Indie dama-h ^house, dwelling ', gr. 56|Joq "house' (5o[jr| "t£Txo(; 
etc? Hes), oiKO-56po(; (*-5o|j6(;) " builder ', Latin Lok. domVio a house' (= Old Indie dame 
'in a house, to a house'), dom/nus^ master, mister' from * domo-no-s. 

usiem ato/77^-s(Brugmann Grdr. I|2 1, 180 presumes an adv. Lok. *domuas originator): 
Latin domus, -usi. 'a house, dwelling-house, building, mansion, palace' (out of it is Middle 
Irish dom-, dam-liacc^ sioue house', aur-dam " pronaos (the space in front of the body of a 
temple, enclosed by a portico and projecting side- walls) ' undertaken with the thing 
together); 

Old Church Slavic dom-b m. "house', russ. doma 'at house' {*domd[u])\ *domovb: 0\6 
Russian 0^/7701/6 "after the house'; presumedly also through Old Indie damu-nas- 
"housemate' and Armenian /5/7^-/e/'"householder'; 

Maybe alb. dhoma ' room' : Old Indie o''a/77a-/7 "house'. 

a stem *dmdu- in Ionian b\\biQ„ Gen. 5|joo6(; " prisoner of war, farm laborer', Spcon " 
bondmaid ', Cretan [jvcoa f. "people in slavery, population in serfdom '; 

Aryan *dm-ana- in Avestan damana-, nmana-n. "house', also Old Indie mana-h'e6\i'\ce, 
building, dwelling'; 

Lithuanian namas, PI. /7a/77arhouse, dwelling' is dissimilated from *damas, in 
compounds as namu-darys' homemaker ', s. WH. I 861. 

Note: 

It is a common trait of alb. and Lithuanian to drop the initial da- as in Root/ lemma: del-5\ 
"long': Baltic with unexplained o'loss (see below): Lithuanian ilgas, f. ilga, Latvian ilgs. Old 
Prussian //gaand ilgiMy. "long'; alb. ^/a/e'long' Baltic and Albanian languages often drop 
the initial da- > zero. This is a common Baltic-alb.. Hence Lithuanian /7a'/77as derived from a 
nasalized form *ndamas. 

Old Irish damnae' ma{ena\\ cymr. defnydd. Middle Breton daffnez co\}\6 have originally 
signified "timber'. 

Tocharian B tern-, A tarn-, AB tarn- "create, beget, be born ' and B tsam-, AB tsam-, A 
sam-, sam-, perhaps after Pedersen Tocharian Sprachg. 2V here; 



in addition also B c(o)mel, A cmol {*cmelu) "birtli', Van Windekens Lexique 51. 

An old branching of the root is 0^/773- "tame', originally probably "tie up in the house, 
domesticate'. 

Note: 

Root / lemma: dem-, derna-: "to build; house' derived from Root/ lemma: ghei-2. ghi-: 

ghei-men-, *gheimn-\ "winter; snow'. But the gh>dhas been recorded in lllyrian alb. 

alone. This makes proto lllyrian the oldest IE branch. 

References: WP. I 786 ff.; WH. I 367, 369 f., Schwyzer Gr. Gr. I 480, 524, 547 f., 625, 

Trautmann 44.
```


## [2026-09-05T17:50:16.313Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '17995,18005p' POK_full.txt"
}
```


### [2026-09-05T17:50:16.369Z] TOOL RESULT

```
Trautmann 44. 

Page(s): 198-199 

Root / lemma: denR- 

Meaning: to bite 

Note: 

Root/ lemma: denR-\ "to bite' derived from lllyrian derivative of Root/ lemma: gerrio'^-,
```


## [2026-09-05T17:50:16.791Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"darga\\|daraga\" KNT.txt | head -20; echo ---; grep -n \"^māna\\|māna-\\|mānya\" KNT.txt | head -20"
}
```


### [2026-09-05T17:50:16.854Z] TOOL RESULT

```
585:By the Avestan and Skt. cognates: afar, Skt. атат; garma- in Garmapadahya, Skt. gharmá-; дата-, Av. sarad-; darga-, Av. daraga-, Skt. dirghd-; baršnā, Av. instr. barasna; martiya, Skt. mártya- .
961:*digho- ‘long’, OP dargam, Skt. dirghd-, Gk. доћ:ҳо.
1273:pIE *dighos ‘long’, OP adv. dargam, Skt. dirghd-s,
1355:| in darga- (568). In borrowings, an original | became OP т if the words were really assimilated into the OP: | thus Arbaird- ‘Arbela’ =
1778:IIT. With no obvious simpler nominal or verbal form: ama- in Arsdma-, asa- aspa-, u-ba-, poss. ^upa-, kaufa-, kara-, daiva-, darga-, naiba-, Parsa-, pisa-, Máda-, raba- in u-rafa-, varka- in Varkána- and Varka-zana-, Saka-, späda- in Taxma-spáda-, spára- in Vdya-spara-; the restored hana- in hana- {й-; mayüra-, of uncertain etymology; the pos- sible vāra- in ^U-vára-zmi-.
1788:VI. The vocalism of the root varies in these for- mations, being either -a- (pIE -e- or -о- or -a-), as in baga-, bara-, daiva-; or à zero grade, as in karša-, u-zma-, darga- (see Lex. s.vv.); or a vriddhied or lengthened grade (§126), as in kdma-, asa-bāra-, Margava-.
2277:Ace. Nt.: apataram, aparam, суат, dargam, ragam, dar$am, duvaislam, müram, paranam, parwam, duvitiyam, -ciy, perhaps hama (DB 4.90); compounds duwiü-paranam (first part instr.), fra-haravam (first part adv.), ha-karam (first part insep. numeral), hyáparam (abl. hyà + aparam); cf. conj. yad-iy.
2671:J. To express duration of time, as in the adv. dargam: DB 4.56 dargam jivà ‘mayest thou live long’.
3159:DB 4.56 (and 4.75) utdtaiy taumā vasiy Муй ша dargam jivà ‘and may family be unto thee in abundance, and do thou live long’, where opt. biyà' rimes with imv. *jivd.
3850:60 dausta : муа : шоу : taumà : vasty : biy& : uta : dargam : jivà
3868:15 & : utātaly : taumá : vasiy : ‚Ый: uta : dargam : jivà : utà : tya : kunavahy
5531:darga- adj. ‘long’: GAv. daraga-, LAv. daroya-, NPers. dër, Skt. dirghd-, pIE *dlgho-, ef. Ck. dodexés, Lt. longus (881, $68, $101, $148.11, VI). dargam asn. as adv. ‘for a long time’ DB 4.56, 15.
---
```


## [2026-09-05T17:50:26.203Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# map line number -> page (count \\f)\ndef pageof(lineno):\n    return t[:sum(len(l)+1 for l in lines[:lineno-1])].count('\\f')\nfor ln in [5531]:\n    print(ln, 'formfeed-page', pageof(ln))\n# search for māna\nfor m in re.finditer(r'\\bmāna[-\\s]', t):\n    s=t[max(0,m.start()-200):m.start()+300]\n    #print('---',s.replace('\\n',' '))\nidx=[i for i,l in enumerate(lines,1) if re.search(r'māna|mànya|mānya|maniya', l)]\nprint(idx[:40])\nEOF"
}
```


### [2026-09-05T17:50:28.246Z] TOOL RESULT

```
5531 formfeed-page 213
[511, 536, 596, 664, 1494, 1572, 2482, 2539, 2591, 2880, 3014, 3646, 4139, 4324, 4596, 4597, 4601, 4604, 4610, 4704, 5748, 5767]
```


## [2026-09-05T17:50:30.434Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5745,5775p' KNT.txt; echo ====; sed -n '4595,4615p' KNT.txt"
}
```


### [2026-09-05T17:50:30.521Z] TOOL RESULT

```
Exit code 1
bümim asf. DNa 2, 32; DSe 2°; DSf 1; DSt 2; DZe 1f; DE 2; XPa 1; XPb 2; XPc 1; XPd 2; XPf 2; ХР 1f; ХЕ 3; XV 2f; A!Pa 2^; A?He 2. ратат, asf. ($55.1) A3Pa 2. bümiyà sf. (8179.IT) DNa 11f; DSb 9; DSe 10; Рб 5; DSs 2°, 3°; DZb 4; DZe 6; DE 17f; XPa 9; XPb 17; XPe 7f; XPd 12; XPf 12, 25; XPh 10; ХР); XE 17; XV 13; A'Pa 18°; A?8e 4°; Wb 7; Wc 8; Wd 8.
BU nsf. ($42) DSf 24, 28. BUyà Isf. DSd 2°; DSf 7, 15, 16, 18, 24^; DSg 2; DSi 2, 4; DS) 1°; DSy 2; D'Sb 2; A’Sa 1; А4 2; A?Ha 2; A?He 9, 17; А?Ра 11.
brdtar- sb. ‘brother’: Av. brätar-, NPers. biraddr, Skt. bhratar-, Gk. @parnp ‘clan-brother’, Lt. frater, OCS bratru, Gt. brobar, pIE *bhráter- (862, 875.111, $128, $154.П). баі nsm. ($124.5, 5186.1) DB 1.29f, 39f.
brazmaniya- adj. ‘prayerful, reverent’ (cf. Kent, Lg. 21.223-9), with braz- rather than barz- (883; cf. Elam. pir-ra-us-man-ni-ia, АКК. bi-ra- 2a-man-ni-1): deriv. (§144.IV) to pAr. antecedent of Skt. bráhman- ‘religious devotion, prayer’, ef. identical Skt. deriv. brahmanyd- ‘religious’, to pIE root *bhergh- (see OP bard-; $75.1II, §95, $120, 5155.11; Henning, TPS 1944.108-18). For other views, see Kent, Lg. 13.301; Hartmann, OLZ 40.145-60; Nyberg, Rel. 367, 478; Hz. AMI 8.69, Apl 116-8 (to Av. barag- ‘to welcome’, barag- ‘rite’, Бәтәгба- ‘beloved’; wrongly, since this would give OP *bragman-); Christensen, Essai sur la démonologie iranienne 40-1; Henning, BSOS 10.506; Abayev, Iranskie Yazyki 1.134; Scherman, JAOS 65.141-3 n.23. Cf. also О. M. Dalton, Treasure of the Oxus 94-5. On form and meaning of РЫ. brahm brahmak, see Henning, TPS 1944. 108-18. brazmaniya nsm. ХР 41, 51, 54 (hardly brazmaniy isn. modifying arid; also not -niy apn. ‘divine’ with Sen 155, nor adn. in elliptic dual with Pisani, see under aria-).
т°, of dubious meaning, Se 1; taken by Justi, IFA 17.112, to be an abbreviation for OP *méraka ‘seal’, NPers. maráh.
та-, stem of ist person pron. in obl. cases of sg.; see adam.
mà conj. ‘not’, in prohibitions ete.: Av. Skt. mà, Gk. шӯ, pIE *mé ($109, §191.1, §292b). With subj.: DNb 55 (mé-taty), 58. With opt.: DB 4.59, 69, 79°; DPd 18, 19 bis, 20; XPh 39. With
201
inj.: DB 4.54; DPe 21; DNa 58, 59, 60; DNb 52 (mà-lay). With imv.: DNb 60. With lost verbs: DNb 57, DSq 4 bis; with restored subj. A'Sa 5^ bis, A?Ha 7, 7°. See also mdtya.
mā- vb. ‘measure’: Av. Skt. ma-, Lt. métior ‘I measure’. à + må- ‘extend’: атӣій npm. past ptc. pass. (6242. П) ‘noble’ DB 1.7; DBa 11. fra- + mā- ‘command’ (‘decide, judge’, acc. to Hz. ApI 154-6; ‘plan,’ Hinz, ZDMG 95.233-5); see also framülar-, framdnd-. јтатауаіа imf. mid. ($214, 5285.11) XPg 5. framatam nsn. past pte. pass. ($242.IT) DSf 19f°, 56.
таш- vb. ‘flee’: meaning established by Мат. and АКК. versions (Hüsing, KZ 38.258); probably to Skt. munthate ‘flees’ (Jn. JAOS 38.122). атида imf. ($211) DB 2.2, 71; 3.41f, 71.
Maka- sb. ‘Maka’, a province of the Persian Empire (lit. on location given in JAOS 56.217-8): Elam. ma-ak-qa, АКК. ma-ak, cf. Gk. pl. Мака ($99, $1322, SI4LITD. See also Mactya-. Maka nsm. DB 1.17; DPe 18.
magu- sb. ‘Magian’, member of a priestly order of Media: Flam. ma-ku-i3, АКК. ma-qu-&u, Gk. Méyos ($153.1). Uncertain material on mean- ing and etymology, Kónig, Klotho 4 chap. 12, and RulD 66. magus nsm. DB 1.36, 44, 46, 64, 66, 101; 4.8; DBb 2. magum asm. DB 1.50, 54, 57, 73; 4.81.
Maciya- adj. ‘Macian’; pl., name of a prov- ince of the Persian Empire: deriv. of Maka- ($99, $113, 8132.2, $144.01). Maciya пет. A?P 29. Масту for nsm. (856.11) DN xxix. Macy npm. DNa 30; DSe 230; XPh 25.
madtar- sb. ‘mother’: Av. matar-, Skt. matdr-, Gk. Dor. ратар, Lt. mäter, pIE nom. *maté, stem *máler- ($154.П): in hamdtar-.
таша conj. ‘lest, that not, not’: mà ‘not’ + conj. tya (§133, 4292р).  matya-mam (5133) DB 1.52. тайа DB 4.43, 48, 71.
mabista- adj. ‘greatest’, equal to ‘crown prince’ in XPf (Speiser ap. Kent, Lg. 9.40-1; Hz. Apl 254-8): Av. masista-, NPers. mähist, Gk. ppxio ros ‘longest’ (radical vowel after that in anxos Jength"); superl. to pIE *mak-ros, Gk. накр, Lt. macer ‘thin’, pLE root *mak- (887) ‘be long and slender’ + superl.,suffix.<ste-) (S117, $156.11,
202 OLD PERSIAN
4190.1), Gk. -сто-, Av. -tšta-, Skt. (with aspira- tion) -gha-. таб: а пет. AsH 6; DB 2.13, 24; 3.70; DPd 1; DPh 9; DSf9; DSp 1°; DH 7; XE 2; XV if; АНе1. [ma8]jiSta-ISàm] DB 5.27. mati&- lam asm. DB 2.20, 83; 3.12, 31, 57, 85; 5.6, 8, 12, 28; XPF 32.
Müda- (S166.IIT) adj. ‘Median’; masc. as sb. ‘Media’, a province of the Persian Empire: Elam. ma-da, АКК. ma-da-a-a, Gk. pl. Mado.
(1) ‘Median’: Mada nm. DB 1.49; 2.14°, 16, 18, 82; 418; DN 1°; APP 2, Madam asm. DB 2.21, 82; 3.30. Mada npm. DSf 50, 54. Майа] ipm. DB 2.23. MddatSuva lpm. DB 2.23.
(2) ‘Media’: Мада пзш. DB 1.15°, 41; 2.7; DPe 10; DNa 22; DSe 21°; Рб 8°; XPh 19. Madam asm. DB 1.47; 2.22, 28f, 48f, 68, 65 bis; 3.32f; 4.20. Méddam-ca DB 1.66f. Madaiy lsm. DB 1.84, 59; 2.15, 17, 22, 28, 66 bis, 72, 92; 3.77; DBe 10f.
tman- vb. ‘think’: Av. man-yele, Skt. mán- yale, Gk. utuova ‘(I bave thought of,) I desire’, Lat. memini ‘I remember’, pIE *men-. See also manah-. maniyary lst sg. mid. (§214, 5238.1) DNb 38. amaniyazy lst sg. imf. mid. (8214, 6233.11) DSI 3f. mantydhaiy 2d sg. subj. mid. (831, $222.11, §234.1) DB 4.39 (manl. . .); DPe 20 (maniydhay, $27, 552.11); DNa 38 (maniya- [...); XPh 47 (maniyaty, without the h*: $27, $52.VI, Lg. 13.302; Hz. AMI 8.66, ApI 243-4). maniyál|taty) sub). mid. (5222.1) DB 4.50.
^man- vb. ‘remain’: Av. man-, iterative pres. manaya- (8123, $215), Gk. pvo, Lt. maneo; prob- ably specialization of pIE *men- ‘think’ (see ‘man-) in meaning ‘remain thinking. amdnaya imf. DB 2.48, 63; amünaiya ($48) DB 2.28.
mana'uwin- adj. ‘mindful, wilful, hot-tem- pered’: from manah- + -win- (§155.V), cf. Lg. 15.170, JNES 4.47 (Hz. ApI 242 otherwise, wrongly). manauvis (remade from -07, $187) пэш. DNb 13.
manah- sb. ‘thinking power, power of will’ (Jn. Iran. Rel. $70; Kent, JNES 445-7, 232): Av. manah-, Skt. mánas-, Gk. дё ‘courage’, pIE *menos *menes- (5124.4, 4156.1). Decl., $185.I. See also manawin-, and -manis- with reduced grade in second syllable, in Ardumuni&, Harā- manik, perhaps [manis-. тапа&-са (8105) asn.
DNb32. manahà isn. (JNES 4.45; wrongly gen., Hz. ApI 240-2 and Sen 235) DNb 14.
méaniya- sb., probably ‘personal property’ in the houses; nt. adj. as collective sb., from тӣпа-, GAv. demüna-, Ау. nmana- ‘abode, house’ ($126), extension of root seen in Skt. dáma- ‘house’, Gk. 0óuos, Lt. domus. For varying views, see Tm. Lex. 116, with lit.; Gray, JAOS 21.17, 33.281-3; Bthl. AiW 1168; MB Gr. §261; Fay, JAOS 34.330-1. méaniyam-cé asn. DB 1.65.
+mamaita, see Atamatta-.
тауйта- sb. ‘doorknob’: Skt. maytikha- ‘peg’, perhaps to Skt. mi- (pres. minétz) ‘fix (as in the earth) ($100, 5148.11); ef. Hz. Ар] 258-9. mayüxa пзш. DPi; XPi.
mar- vb. ‘die’: Av. mar-, pres. miryeite ($122, $214), Skt. mriydte, Lt. moritur, pIE *mer-. See also uvdmarsiyu-, marika-, maria-, martiya-. amarijalü imf. mid. (835.1, $285.II) DB 1.43.
(eval):1: === not found
```


## [2026-09-05T17:50:38.007Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"māna-\\|mána-\\|mana- sb\\|'house'\" KNT.txt | head -30"
}
```


### [2026-09-05T17:50:38.067Z] TOOL RESULT

```
5703:framána- sb. ‘command’ (judgment, deci- sion’, acc. to Hz. ApI 144-50): РЫ. framán, NPers.
5705:fürmán; fra- + mä- + suffix -nà- ($128, $1471), ef. Skt. pramána-m ‘measure, standard’. — framánà nsf. DNa 57; DNb 28; DSj 3°, framánáyà isf. DNb 37.
```


## [2026-09-05T17:50:39.367Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5740,5760p' KNT.txt | head -5; echo ===; python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nimport re\ni=t.find('méaniya- sb')\nprint(t[i-3000:i-1500])\nEOF"
}
```


### [2026-09-05T17:50:41.344Z] TOOL RESULT

```
Exit code 1
(ВМ. AiW 950); deriv. of OP bard- (575.1, $155.1; Scheil 21.26; Konig, Burgbau 51; Hz. AMI 3.57; Bv. Gr. $812; Kent, JAOS 51.204, 99.15). bar$nà ism. (806, $120) DSf 26, 26f.
bav- vb. ‘become, be’: present stem bava- (8213), Av. bavatti, Skt. bhdvati, Gk. ote ‘grows’, Lt. fut ‘I was’, Lith. butt ‘to be’, NEng. be, pIE *bheu-. See also büm:-. bavatiy (§122, §228.1) XPh 55, 56. bæa"ty 3d pl. ($232.1) DNb 14 (башайу in 2d copy, Hz. ApI 115; ef. $48). abavam Ist sg. imf. DB 1.28, 60, 72; 4.5; 5.4^; DSm 6°; XPf 35, 36f; XPh 30; XSe 4°. abava imf. ($228.IT) DB 1.32, 38, 34, 40, 48, 77, 80; 2.16f, 17, 80, 94; 3.10, 11, 20, 27, 28, 76, 82, 83; 5.5, M^, 30; DSf 25; XPf 26.  abava^ 3d pl. imf. ($112, $232.IT) DB 1.76; 2.7, 93; 3.78; 4.34. bavātiy sub). ($222.11, §228.1) DNa 43, 45f; DNb 59 (Lg. 15.74; confirmed by photograph, JNES 444). [biyjä 2d sg. opt. ($114, $218.11, $223.I, $227.11) DB 4.69. буй opt. Cbhy-net, Bv. Gr. $232, comparing Av. buyd{ from *bhu-iët; but ВЫ. Gdr. IP 1. $143 takes as *bhy-i48t, = Lt. fiet, which may be either non-thematie opt. or thematic subj.; $114, $122, 5208, $218.II, §223.1, $228. ID) DB 4.56 bis, 58, 59, 741, 75, 78f, 79°.
bigna-, in d-bigna-, see Bagabigna-.
biimi- sb. ‘earth (= world or ground)’: Av. bümi-, NPers. büm, Skt. (RV) nom. bháümi bhümis; deriv. of root bhav- (see bav-) in grade bhi-, cf. Skt. aor. ábhüt, Gk. ёфо ($11, $65, §152.1V, §179.- IIT).
LEXICON
(eval):1: == not found
```


## [2026-09-05T17:50:53.067Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== BRT daraga ==\"; grep -n \"darəγa\\|daraγa\\|daraga\\|drājah\\|drājō\\|drāj\" BRT.txt | head -25"
}
```


### [2026-09-05T17:50:53.122Z] TOOL RESULT

```
== BRT daraga ==
12880:—  ')  S  411-  3  d. •  p.  darga-,  g.  daraga-,  j.  dar«}-a-  Adj. (fem.  °7J-)  'lang';  i)  räumlich:  Ufa  tarn car^am  yqm  'yqm  YtJp.  77;  5.50;  — mi^rtm  . .  yeAha  'yäat  bäeava  .  .  Yt.  10. 104.  z)  zeitlich:  M<?i«(sd.)  tat  äs  nsit 'y?m  Yt.5. 65;  —  "iimal  aipi  zrvätum Y.62.3,\tig.a6;  13.53;  —  °f^^  ^yo (sd.)  t^mattks  Y.31. 20;  —  'yayäsca  paiti danyjjltdis  YL  /y.  1 3  j ;  Y.68.11;  —  tsm (nämL  kämtm)  msi  data  'gahys  *yaos{^^^ vairyS  stSis  Y.  43.  13;  —  hyatcä  -gSm *Jr3gvö.d»dyS  rasö  {sd.)  Y.jo.ii; — ptn- fum/a  (sd.)  barjsma  starane  °y?mca  yasram ..yaaJnS'Vt.iO.iiSi—ya^a  Sicä  *aiivi- iayama  'ya  amiiayana  . .  hr^yrnya^^aSum (sd.)  Yt  70.  7  7 ;  —  °gäi  Tsyai  bfzvait!  hax- maim  (sd.)  Y.  40.  3;  —  'yai  hax^räi  Vt 10.  T),  17.6;  — fravaiayS . .  hulhaxmanS . .  'yaa'fyj  Aax^oralifyff  Vt  13.  30;  —  'y^m Aaxma  V.  60.  j;  —  dättm  tS tanuye  :^ar»nB ' urvnaläi  •y?m  havanfum  (sd.)  Yt77.  22; F.^b;  —  urunaica  'ye  havanhe  A.  i.ii; —  'yäi  AaosravaAAsi  .  .  -yai  AavafiAäi Vjtjs;  —  a  'yät  ^ä.bairyilt  (sd.)  Y. öo.  6;  —  'yqfi  upayanayä  (Stverz.)  Y, /.  13  usw.;  —  'ya  (APn.)  data  .  .  sara- >uäraAe  T.  ^6  {?);  —  iaia  tl  'yim  ävSya (sd.)  aakal  H.2. 34;  16.  a)  Adj.  an Stelle  unsres  Adv.'':  :^afsa  'yd  tna^äka "schlaf  lang,  o  Mensch"  V.  rÄ  16;  — earäiti  .  .  yä  'ya  apu%ra  aHti  V.  3.  34; 34.  b)  ASn.  als  Adv.:  H  utä,  'gam  jlvä
```


## [2026-09-05T17:50:53.739Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== BRT nmana ==\"; grep -n \"nmāna\\|dəmāna\\|demāna\\|garō\\.dəmāna\\|garōdəmāna\\|garō-dəmāna\" BRT.txt | head -30"
}
```


### [2026-09-05T17:50:53.797Z] TOOL RESULT

```
== BRT nmana ==
```


## [2026-09-05T17:50:57.767Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"nmäna\\|nmana\\|d»mäna\\|dsmäna\\|garö\\.d\\|garö-d\\|garöd\" BRT.txt | head -20"
}
```


### [2026-09-05T17:50:57.832Z] TOOL RESULT

```
2455:l'S.S  (wo  awÄ<f' als  LSf.),  Y.9-28';  —  w I  nH  aiäAili  i'lse  jamyät  as>mca  ..  asista  tä airihat  Aa'a  visal  güuS  buyät  Y.6'o.2i.; '  2.  S..2J.3.  52-3.  FrD.  P,  Yt.  /j.  i3;  ~  ioa fri>ä  .  .  buyata  ahmya  nmlne  Yt.  /J.  147  ; IS6f.^  Y.26.^,  62.3*;  —  fraddiäi  ahe nmanahe  ..  vlspaya  alaond  stöis  Y.52.4; 4.5',  Vr. ».  13*;  —  imim  >7oqm  .  .yänim .  .  jaioyemi  .  .  dn'atütam  aiiiAas?  tanvS ". .  Gesundheit  dieses  (meines)  Leibes"  Y. 5.19;  — yaiä  ratSm  akurö  valdil  . ,  aya qsayä(scL)Y.ji.2;  —  afäi  aAmäi  var^nai.. nidätitn  ahm  . .  iAaeiili  (sd.) . .  "und  in  diesen (ünsem)  Glauben  .  ."  Y.4ff-3;  —  aitiAa daenayä  mqs  vaca  dd^anaAe  Y.  j?.  3 1 ;  — frä  KTjri»ie(sd.)aA£(XS{.alsinstr.)da^(^a ..  aAura  ..  Vr.5.3;  —  atcäv3  mizdtm  (sd.) anhat  aAyä  magahyH  y.  S3T>  —  H  *"''^ (sd.)  maiy  aniya/ay  vasiy  astiy  kartam avJ*  ahiyäyä  dipiyä  ttaiy  nipislam  (sd.) ".  .  in  dieser  (meiner)  Inschrift  (hier)  . ." Bh,  4-  S;  —  yS  ach-a  mazdayasnalh-a  .  . ". .  wer  hier  unter  den  Af.  .  ."  V-S-z; —  aAyil  '^wil  J^rff  rtr»z3nil  .  .  pairl.ja-
2459:sSmaidf  Y.  jG.  I ;  —  ahmya  zaoi^re  imat  us  haca  aiihyS  nmänaiibyS  ..N. ^.-^^L-j^- barfsma  äyae  yäti  Y.  2-i;  aE,  Vr.2. iff.;  parö  ibisyanbyö..  a^^am  ibaisattuhatqmXx.
2461:—  ahmi  atskvö  yat  astvainti  V,  5.  Sprecher  vorgeschwebt:  jaji-a..  7rfJ»aVfl/ 39;  —  ai^hS  zimo  yat  faianaya  Yt  w.  poHbm  hl  matw  .  .  nöit  zT  ahmi  paiti 95;  — ■  anhqm  dämanqm  yat  ahurake  .  ..nairi  .  .  V.  7.51  f.;  _j.zi;  —  ^aei  iskata dätarasca  ,  .  Yl  ig.^Si  —  ar>zahiby5  sa- '  .*aoi  spita.gaona  gairi  aat  äkva  paurva- vahUyB  .,  aheca  iarsvanf  yat  :i^anira-)tähva..\.lo.ii{.; — *unäAva..raBsayaca  aal '^ahe  Vr.  70. 1 ;  — yat  ahmi  nmSm  yal^  ähva'  iyar»^ähva' {^'^  V.iy.zi.;  —  vasö »»äaÄy(MHÄ/(Stverz.)  "wenn  hier  im  Hause '/fljc'äö'fl  mazdayasna  aits  pa'^h  frayqn  . . eines  M.  .  ."  V. 5. 4 5 ;  usw. ;  — ■  aitihä  dae-  ahe  nmänahe  myasd»m  dai'^yärys  V.  S.xz; naya yat  ähuröHY .60.1;  Yt  jj.gg;  Y.  Ä  7  ■  10;  —  asfmacrjS  ,  .  yS  altahmi  aahvS  .. {•MO  yä  ahairU).  b)  substantivisch,  am  faitiMiuaiti  a  dim  näii  apivatäite  . .  para gAw.,  von  dem,  der  so  bekannt  ist,  dass  ns  ahmai^  atat?halca  soi'iraatca  ..\.g. ein  'er"  genügt,  ihn  zu  bezeichnen  ('Er'J,|52f,;  — yasca  ..  imat  ..  i<acS  fravaoc^ von  AaraMainyav :  yl  ml  nä  manxiaiti\ .  .  nsit  dim  yava  aii'ihe  ayqn  nöit  airika anyä>ä  (sd.)  ahmjt  Y.5/.10.  II)  iu'.xsafS  ..  Yt.ii.^t^^,  —  y/üse  mq>rahe schwachdeiktischemSinn 'dieser,  der,  er":  a^,;  ar  «ä  *sravat?hs . .  N.22;  —  vispim 1)  auf  Vorhergenanntes,  Vorausgehendes:,,  aya  ratu/rita  (näml.  Y.55.1— 5;  LS. (Wort  oderSatz)  zurückweisend;  i)  auf|  als  Instr.)  hvävayanh>m  .  .  paiti.barähi ein  Substantiv  oder  subsL  Pronomen;  a)  ad- ;  Y.  55.4.  o)  Das  adjekL  Pron.  steht,  wo jektivisch:  spinti  mainyü  .  .  ahyl'  *main-'AKi  Römer  die  Gen.  von  is  brauchte  (s. yius..ahm3t*mainyiusM.4y.i—^;  —  vaa-\  I  aaa,  23  aa):  aSe  mazdayasna  ..  atarj- hius  ivistl  manatshö  .  .  ahyä  vaahiul  tqm  aSoAmiti  naire  frabäraytn  .  .  yai manaahd  Y.  34-  9  f. ;  —  alnaahqm  . .  aisqm  ,  also  nä  . .  haca  aiibyö  nm3nalibyS  xsnütö alnaahqtn\.^2.it.;  —  tä ..  mainyü  {ai).)\.  .  pärayät  ",.  ex  eorutn  domis  . ."  V,^. ,,  ayä  *mainivä  ..  ayä  Y._J0.4— 6;  —  Äa-\  39;  —  yat  baväni  aiwi.vanyä  tq'irya- zaignm  yaexäinqm  .  .  balaar»  döi^ranqm  \  vant^m  . .  ahmt  gal^e  piianlhu  "dass  ich .  .    aal  äbyS  dei'iräbyB    ai-uiyasca    (DPf.)  [  Sieger  werde  über  den   7:  .  .  im  Kampf
2463:paiti  vä  xsa/ne  . .  nöit  . .  aiähe  ayqn  nöit aiiihä  xiapö  .  .  Yti.iS;  —  asankatca iöi'irSatca  ..  kaoa  nö  ahmäii*  asarahaica läiiraiüi  ..V.ff.Sif.;  55'\  56i\Y.^S.2; — sraoi»m  .  .  yö  dalnöJiisö  *da?nayä  . .  aya dalnaya  . .  Y,  57. 24;  —  , .  parö  jbi^anbyö .  .  alsqm  tbifyaniqm  Yt-  io.T%i.;  —  yaoz- däiqm  saeirqm  . .  änhqm  zaoiranqm  Yt. io. lai f.;  Y.2(j. 2;  —  vä^^m  srJr^m  .. ahmya  väse  Yt/o.  12411;  5.11;  —  äp)m andvim  . .  *atihasca  mi  *aSva^hä  apö ¥.(75.1—5;  5,  V.ö,32  (aitiha);  —  nmS- mm  .  ,  äat  ahe  nmänahe  V.^.3;  14,  40; —  narö  . .  äat  aisam  naram  aivS  iri^yai (vat  antarp  *n3rius  .  .  V.j.z?;  5.43,  44, A.4.6,  Yt.iO,i37;  —  ygi  nmüni  hqm. barämahi  . .  äat  pascaeta  ahe  nmänahe , .
2472:dalvil  . .  atibyö  kam  Y.44.20;  46.12;  — li  narS..aeiqm  nmäna  Yt.i~.yC;  g— 14.^, J0.39f.s,  33,Y./j.3,j7.37,Vr.//.i9,V.2, 43-J.i4,Ä4i,  12.1, 13.50,  i5.22,FrV/. 10. 40,  N.<S'5; — g3ui..ya  dar>nlhu  mi^rS.- drujqm  ..frazarsta  (sd.)  aglqm  rai'iya  .. hiit»nte  Yt. /o.  38;  —  vTspanqmca  , .  asae- nqm  aiaoninqmca  .,  vUpanqmca  allqm  za- ra'iuStnm  ..  *susruma ikatsim  Yt.Jj.148; —  a^qm  anyS  N.  61,  62;  —  aifam  aOiai»- kam  .  .  adqmcH  S  ahmt  .  .  vicC^ei  (sd.) aipT\.32.i;  30.1,  8,55.9;  —  haxays .. astvat.gr3take  .  .  assu  paro  fräntmlite aismü  Ytiff.g$;  — gä^a  . .  yezi  argAqm *Syutnpe  väUm  framaraiti  N.  42;  —  xi paiti  apqm  .  .  a^ra  atthqm  V.  y.  5 1 ,  Y. 6Ä7;  Yl/j.68;  —  duzvarmanhS  .  .  rä- mqmcä  J//'"'  dadätu  V.  ^3.  8 ;  —  yaia  ta r  ,  ,  minghäeä  .  .  yH  vohü  .  ,  a'iä  %WJ Si/'"'  yazamaide  Y.  j(?.4;  —  karapsAsaJ (sd.)  kfvitäsca  . .  töi  abyH  (AbL)  bairyänts (sd.)  .,  Y.52. 15; — spuda..kuir3  ayä.. Y.44-I5;  30.6,  3t.io;  —  /J  mainyn  .  . ascä  (GD.)  .  .  Y.30.3;  —  Gen.  in  Ver- bindung mit  hava-i  zasta  hl . .  frasniöa- v paityesii  V.22.7  — 13;  /.z;- — \y"t  aSahe  yat  apirmäyükahe  ahe  hava- aiwySr3hafi?m,.äat  aiijhi  ahi  aiwyästö  Y.  _v(7«  tütroö  "die  Hände  ..  des  Kindes  an ij.zb;  — ahur>m  ..  ahyä  x!a~i:räc3  ..  *hva- 1  dessen  Leib"  V.itf,  7  (?)  "';  —  dgL,  zugleich paphsiica  (sd.)  lim  .  .  yasämaidi  Y.  J7.  vorausweisend:  astvatjr3iö  ..  kB  ..  aiike if.;  —  sraosim  ..yazamaide  ahe  raya  . .  j  haxayB  /räyente  astvat.iritahe  Yt.  ip.  95: aiÄke  ama  ,.  ahe  yasna  ..  t?m  yai3i  "den '  - —  dalnqm  .  .  yao:dai%xSa  ai:a  sT  aiAka Sr.  .  .;  ob  seiner  Pracht  .  ."  Y.  57.3;  Yt.  yaoidaitii  ..  havaya  .  .  dainayä  Y.io. J-i^i  5i  9  (statt  fem.!);  —  noii  kl  anyö\i9.  a)  spez.  auf  das  Subjekt  des  gleichen urva  kaum  urvämm  paiti  irista  (sd.)  ^a-|Satzes,  Reflexivum:  ka%S  .  .  gqm  Ha- zaiti  xraosyü(a{%t^voyaca*a>»he^^.*at3hr^^  sSil  y}  kirn  ahmai  ..  stsi  usyaj  (sd.) Y.  13.9;  —  fravasayS  . .  ankam  raya  . .  Yt  ".  .  qui  eam  sibj  .  .  esse  cupiat"  Y.  ^o.  2 ; 13.2, 14—18"';  — gunäayäi  ..  za/an  ta/-  ^  —  nsit  sp>ntqm  d3r?st  (sd).  akmai  stöi San  (sd)  aya^'*  masJY.3.32;  —  vac?  ..\armaitlm  Y.4^.2;  —  hvJ  tat  n3  ..  ak- yii  . ,  akmai  straohm  dqn  Y.  45. 5 ;  —  |  mai  "'  dazdl  (sd.)  Y.  5/.  1 9 ;  —  aada  (sd.) ustä  ahmst  yahmai  .  .  kakmaicTt  . .  atca  \  vinzyötüca  It  akmai  fracä  vatöyBtü  (sd) <ihmai  Y.  43. 1  f ;  —  gavöi  . .  ha  %X  to\lt  alibyB  yöi  .  .  "..  sibi  (ipse)  . ."  Y.  J5.  6; huisii»m3  .  .  dal  .  .  at  ahyäi  .  .  masda  \- —  at  hT . .  /ravanll  (sd.)  vasirim  ahyai orvara  vaxsat  Y.4S-6;  31-9;  —  raya  ..\fntyant3m  Y.jj.  10;  —  nSit  ta  Im  x^3ui koya  aiiiAä  raiavö  Y.iff.iS;  *YyX.  50; — {vaipyö  .,  zara'iuhrtm  ..  Ayat  akml'^ paoiryö  gairis  . .  akmat  haca  garayO  tu- 1  urüraost  astö  hyat  , .  v3z3  (sd,)  Y.  31. uxiyqHYt.ig.\i.;  34,80;  —  hö  nBit..*/r3-\  12.  aa)  Der  Gen,  vertritt  dann  die  ent- nJmaite  ,.  /rä  ahmst  parö  ..  «jÄion/i;  j  sprechendeFormdeslat  suus:  airj  *i'jiri»i Y. 57-18,  ungeschickt  benutzt  Ytp.4;  lo.  baraiti  mi>akvac3  vä  irvivaca  (sd.)  vä.. 117;- —  *haltuma  . .  kacaiti  dim  . .  astica  akyl  zaridaca  manat»kac3  ", .  ex  suo  (uter- ahmi  avavat;^arin6  yäi:a  yat..Yx.ig.(>Z;\c^^)  corde  et  animo"  Y.ji.ti; —  akya —  :^aitu/  . .  vtrizifum  mat  airyamnä  . .  \xrata  frö  ma  sastB  (sd.)  vakistä  Y.  45. 6  ;
2493:/u>n  ..  Y.6"o.sf.;— ..  a/^'z'^-4r^ayS(sd.)j_j.5;  _  „yaca  h 'disänaya  Vyt5/; ..  ya>a  spä  vakrkaAe  k}r?naoiti  ya%a\ai,iAa  drujö  FrVV.  Äi ;  V.  7.52  PüZ.; — yat  v>hrkö  spa  V./_j.4i;  ~  ..  aAmai  „Ami  ar»>e  yahmi  gafi:e  Yt./2.8;  — nmänai  .  .  ^yahva  xsnBto  bavaiti  Yt  10. 1  aAmya  .  .  yahmya  .  .  aAmya '  Yyt.  4^;  — 28;—  zugleich  zurückweisend;  s.  I  i  al  ^^ft,«/«  «ar««  V.5.9  PüZ.;  Yt./.a?,  J.  10, aE.  a)  Das  adj.  Fron,  vertritt  das  lat.  [4.2',  8,  V.  7!72PuZ.,  Vyt.  39,42';  — yaj eius  (s.  I  I  a  et):  dBräi  Aa/a  aAmai  nmä- '  mlalsamcilnmSnanamca'*caratö(s^.)dva.. nät  .  .  aiiihät  vUat  .^.  aAmät  zantaot  .  ■  V.  13.49;  — c'vat.bi/ ayß-  vTtay3{sd.)  atthsn aitihat   daitiAaot    aya    ihyejä   .  .  *yeyenti  \  >j,  ^V.  ti^e   i>:a  ya>na    aAmii  Yt  IQ.
2494:yetihe    nmanaya    "weit   weg    von    dessen  l  57^  61^  63;  63':   sind  sinnlose  Ruchwor- Haus  ..  gehen..,  in  dessen  Haus  .."  Y.    (c,  ahmät,  aAmi,  aAmya,  at,  at,  äat,
2664:y.iG.T,  Vd.;i';  —  mqnaytn  ahe  yaiia  — yS  °vahe  aspmaoyäke  ..  daoiiiii  \.iS. kazatirsm  narqm  Sim'*  nanm  aäar>zayöil  n;  —  'vahe  Aillqm^''>    Hnmanahe  .  .  A,
3372:ainim  ag^rapaitiot  (sd.)  üpshöit  '>a  >. Um  aivdi:a  tüirim  T^.ii; — yujyastis  haca *nmanat    "'ha    \daniuil]     visal     Aa'ir»m *zaiUao]  *'%a  •>   *daMaot  N.  8;  ioS\  Yt. JT.3; —  dvaiibya  Aaca  mnbya  dva  nara
3480:mit  avi  'einholen':  yest  ahi  paurva.- nafmät  aal  "lam  avi  nmänaya  (sd.)  yezt paskät  aai  ma'm  avi  apaya^sS.)  Yt.i&.a.
3840:•  j,  aiwi.draoxSa-  Adj.  'zu  belügen,  zu betrügen':  mtirim  . .  ys  nsit  kahmäi  'oS nöil  nmänaie  nmandfatje  .  ,  Vt.  10. 1 7.
4575:•  j.  'an'tara-  Adj.  'der  innere,  innen  be- findlich': 'r^m  ür^Mfii  nmanahe  "ins  Innere des  Hauses"  V.6'.43;  —  'rat  W.  2.^0 PüZ.  a)  'rat  naimax  'innerhalb',  mit folg.  1)  Gen.,  z)  Lok.,  3)  Instr.,  4)  Akk., uzw.  a)  räumlich,  b)  zeitlich:"  1  a)  a'  n- hsirake  N.  Go;  104';  —  *a'  n°  *yujyastHs N.  -ji  T'*j  —  a'  W  aEi3.drajahyehe  N. Ii()',  —  a'  n°  '^rigämyt/ie  N. 65.  1  b)  a- II'  tiava.xsaparahe  V.  5. 43.  !  a)  a'  11° barj''irisi'a  y.^.^i.  3  a)  a'  n'  brrat.- byqm  V.  Ä41,  42,  g.  15,  16.  4  a)  a' tr  aSe  pa>a  "auf  diesen  Wegen"  V.  8. 104.  4b)  a°  11°  triilzär.ljaAlm'V.^.^y, —  a-  n' yanJräßV.O.a,  3,  7.77.  Tai fialinät  N.^.^3).  Ta  N.JOi(?);  —  'nm N.pj(?).
4585:•  j,  +antar«.ar98am ''  Adv,  ('zwischen  den Seiten',  sva.)  1) 'innerhalb',  mit  Gen.:  °äjw zrayanhB  V.5.19;  —  ''(am  nmänahe  "V-ff. 33,  Yt./7.6o.  2)  'diesseits':  yas;/  iava masda  kirpnaot  tacar)  *nSit  *tacar>  *'Mm'^ upairi  Avanxsaiüm  "dass  dir  M.  eine Bahn  bereite,  nicht  eine  Bahn  diesseits, (sondern)  Über  dem  Sonnenball"  YL  5, 90.
4636:KompA.,  E.  i  Ableit.  —  ai.  antär  Adv.  (usw.).  — FS.:  anäar,  andark,  andar  andark.  —  ')  Wohl aiilarän  lu  lesen.  —  >)  FoY  KZ.  35.  4z  will piiri^  Italt  d'lqr  lesen;    s.  abec  Rl.  iSt.    — 3)  l\Af,./rähU'ilintar>;'V'a.: ..  artdari.  —  *)  llds. fehlenil ;  s.  aber  Pü.,  die  iwelmal  andar  bietet. —  5)  Uiw.  Plor-i   vU,  nur'als  Vertreter  des AP. •  j.  'antara-  Adj.  'der  innere,  innen  be- findlich': °rpm  arpopui  nmänaAe  "ins  Innere des    Hauses"   V.  ö,  43;   —    VJ/V.  2. 40 PüZ.         a)   'räi  tsaemäi  'innerhalb',  mit folg.  i)  Gen.,  2)  Lok.,  3)  Instr.,  4)  Akk., uzw.  a)  räumlich,  b)  zeithch:'*  i  a)  a"  n° JiairaAe'Ü.Go;  104';  —  *a°  n°  *yii)yastsis N.  7/ T'>;    —    a'   w    aliö.draJaAyeAe    N. Ijg;  —  a'  «°  %rigäniye/ie  N.  6<}.  i  b)  a°
4818:—  weg':  viipim  a  ahmät  yat  ads  na  .  . haca  aHbyS  ttmUna^byS  . .  allristJ  pärayat yezica  .  .  hala  a^byS  nmanadbyd  tbists  . . paräiti  V.p. 39f;  13.  ij;  —  xsnata  para- yarüu  haca  ahmSJ  nmäiiät  Yt  l^.  1 5  7 ;  1 5  7 ;
4820:—  zu' :  xshms  asamqm  unänö  pärayeinii . .  avi  garS  nmänam  V.  75.32;  —  x3  patti apqm  paräiti  .  .  a^ra  . .  V.  jj.  51;  — xraosyS-taraca  (sd.)  .  .  hv5  urva  paräiti par3.asnäi  amihe  yaia  . .  V,  13. 8;  —  ya- tärö  paurvs  us>hiUaiti  paräiti  vahiltahe atshsus  y .  iS.^d.  2)  'aus  (dem  Haus) gehen  auf  — ,  zum  Zweck  der  Verrichtung von-'  (Akk.):  *kat!lmS  timänahe  a'iauru- fi9m{sd.)  pärayäf^''  N.  /;—  para  paoiryö äiti  (näml.  a^aururitm)  para  bityö  aiti para  "hrityS  äiti  aita  paräyaiti  ycc^a gae'^äbyS  *k)nti  "es  geht  der  erste  (auf Priesterdienst)  aus  . .  der  zweite  . .  der dritte.,;  es  gehen  die  weg,  die  (zum  Schutz) für  den  Hausstand  da'gelassen  worden) sind"  N, 2 (?)"'; — katärsm  *ä'irava  ctiauru- n>m  Vä  parayat  galiaiiqm  vä  asp^nns (sd.)  avat  N.^;  —  katärS  a'^aurun?rn ''parayat  nSirika  vä  nmätiSpaitiH  väi yezica  vä  ga^hä  vTmä  (sd.)  *katarascit ''parayat  N.  5;  *5";  —  *cvät  ''aiwtstXm parayap  'irixsapar>m  .  .  yS  haoys  (sd.)  . . paräiti  nsit  .  .  anaiwistim  (sd.)  ästryanti N.  4.  a)  mit  haca  und  Instr.:  cval  .  . äiirava  a'iaurumm  haca  ^gafi^äbis^para' yat  N,  4-  3)  'sich  an  etwas  (Akk.) machen':  yö  nar)m  ..  kasyat»he{%d.)  sanhai daoaili  vl^va  aval  hava  xraiwa  paräiti "—  wissentlich  mit  voller  Absicht  macht  er sich  daran— "V,  15- 2.  4)  'hingelangen zu  — '  sva.  'sich  verschaffen':  ffi.j(Akk.),. kaine-.tarS  äaxit^m  pärayät  tarS  ap»mca urvarqmfa  yezica  . .  tarS  (sd.)  daxst>m paräiti  . .  "nicht  soll  das  Mädchen  heim- lich sich  die  Regel  (wieder)  verschaffen, heimlich  sich  Wasser  und  Kraut  verschaf- fen .."  V.i5,9f.
5458:•  j.  arsSa-,  p.  arda-  i)  Adj.  'halb' (nur  Komp.).  2)  m.  'Seite':  *atitar?m (sd.)  'tijm  mayaAe  V.p.29;  —  antar?m 'fam  nmanaheV.6.i,y,  — dasinim  (vair- yastärtm)  hl  upa  "htm  Yt.  10. 100';  — visps  he  upa  'wun  (lies  -o!)  \tio.ioo; —  äasimm  hl  'Öe..  Aävöya  hl  "%€  "rechts (links)  ihm  zur  Seite", Yt. /o.  ia6;  —  ww- %asö  (sd.)  gairis  parmtarim  °c,5  (AD.) manuiahe  YL/p.i.  [V.  5.19,  5.33,  Yl j".6o:  lies  antar».am>m^
6082:jrjmuibmS  Y.57.4;  7.1,  2^.2;  —  zara- ^BsTrvm  .  .  yat  as  °hm  alavasfornd  (sd.) .■V._y.  4;  — j'aia  °ä7/  x!a%tym  cinasti  (sd) Y.20,3"';  —  äat..  ah<  nmänahe fraf^wd gäus  .  .  'um  .  .  i-ästrpm  V.J.  3;  —  asis/a itä  airihat  haca  vlsat  gaul  buyat  asUbm •am  Y.  60.  3 ;  —  us  nü  aiAhäi  vXse  jamyät •ämca  x/a^nm/a,.Y.6o.2.  III) 'Recht, reditmässiger  Anspruch  (auf  — )'  und  zu- gleich 'Gegenstand  des  Rechts,  worauf  man Anspruch  ha^  was  einem  gerecht  ist';  spez. von  dem  ftir  die  Zugehörigkeit  zur  sara- l^u/jyischen  Religion  und  das  ihr  ent- sprechende Verhalten  zugesicherte  und  da- durch erworbene  (höchste)  Anrecht,  d.  i.  das auf  das  ewige  Gut  (Paradies)  und  dieses selbst  (S.  auch  vAbleit).  i)im  gAw.:  '/,/m 'dtrndyai  (sd.) . .  räyS  asts  vanfOui  galm (sd.)  manauhs  Y.  43-  •  "'j  —  .y?"»  i^am (sd.)  data  .  ,  ahurö  °sahyä  iizäyäi  (sd.) pmdim  Y.^i.ij;  —  käds..ysi  uxifinn (sd.)  asnqm  a»!iSu^  dar^%rai  (sd.)  frS •iahyä  /rar  iitzY.46.y,  —  ya  ^aohana.. awuntStim  "hmcä  *iaibys  dänAä  (sd.) natda  xsa>r»nca  Aaurvalät3  Y.S4- läis  yüs  g/ae^ORäis  'um  xsmmbyä  dadi^l (sd.)  Y.46.  is'J>;  —  ktßarä  yas5  (sd.) hyin  'liin  Y.  5/.  4.  2)  im  jAwr.:  tßit
6516:•  j.  aS.paourva-  Adj.  'der  weitaus  vor-  (näml.  gs>a)  n5  buyqn  Aumiida  (sd.)  -ds anstehende,  erste':  aisam  nmäna . .  hisimte  Y.55.  a.
6587:Sache  gewidmet,  dazu  bereit  sein'.  B)  im Aw.:  aAe  nmänahe  ..yetiA^  aim  (?)  ar)h?n
```


## [2026-09-05T17:51:04.703Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"nmäna-\\|dsmäna-\\|d3mäna-\\|dpmäna-\\|garö\\.dsmäna\\|garö\\.d3mäna\\|garö\\.dpmäna\\|garö\\.nmäna\" BRT.txt | head -20"
}
```


### [2026-09-05T17:51:04.784Z] TOOL RESULT

```
8344:•  j.  upar5.nmäna-  Adj,  'der  sein  Haus oben,  in  der  Höhe  hat':  mihr^m  . .  'tarn Yt,  10. 140,
13119:und  GP.  mit  äaitihupalay-  (Stverz.,  unter I  a,  2  a):  nmünahe  vä  nmänS.paitiS  vTsS vä  vispaitii' tantJus  vä  zantufaitii  "itihSui vä  dair^hupaitisYtiO.18;  usw.;  —  nmäna- iiam  nmänS.paitis . . 'Äyunam  datAhupatti} Yt/0. 18.
13920:•  g.  damSna-  n.:  s.  unter  nmäna-.  *dvaäbya^^  sr?subya'iü.Osi—dva  aurvanta
15771:•  j.  paoirya  Adv.  'zu  Anlang  (der  ersten Welt)':  fravahyö  yS  ^  atthan  nmäna- namca  visqmca  . .  "die  Fr.,  die  zu  Anfang waren,  (die  Jrr.)  der  Häuser  und  .  ."  Y. 23.1.
17597:•  j.  frat3mö,nmäna-  n.  'Haus  von  erster Bedeutung  und  Grösse':  'nahe  nm^tm.paitlm . .  mah»mli.nmsnaAe  . .  V.  y.  jo  f.
18870:KompE;  AbleiL  (s.  auch  •nä/aina-).  —  VgL nä/ah-  und  itaiämadii/a:  —  np.  »ä/  'Nabel* ; ai.  Tgl.  näMqy-  f.  'Nabel',  s.  dazu  S  2j  b.  — Pü.:  Hä/ai.  —  I)  Sonst  erscheint  in  dieser  Zu- sammenstellung nmäna-  n.  'Haus',  sd.  mit  *).
18953:Eig.'ReisigCgeflechtjbedeckung',— Pü.:  nama' apar  nihumbih.  ~-  ')  NA.  tum".  —  s)  Im  Folgen- den als  nmäna-  bezeichnet.
19293:nmäna-I
19321:•  j.   nmäna-nhan-  Adj.   'der   sich   das Haus   verdient,   erworbeo   hat':  paoiryan tka^  .  .  nmänanqm/a  visqm/a  .  .  'ahänS (AP.)  visänd  ..  Yty.  151. Komp.:  nmäna—\-'Aan:
19338:•  j.  nmänö.patay-  m.  Ilerr,  Gebieter eines  Hauses,  Hausheir*;  a)  im  erg.  Sinn: •failii. .  nmand.pahni  vä  V.  12.  7 ;  Yt  ly. [o;  —  ialärff(sd.)  ..näiriia  vä  'pailii  vä N-  5',  5';  — yä  näirika  'paiti  virnyantiQ) N.  6;  —  %wqm  kaimnS  .  .  x/a^ra  .  . Jai%yänte  taxmimca  'paitJm  Yt5. 87;  1$. 40.  a)  mit  Gen.  aus  nmäna-:  nmänake vä  'paitil  vJSB  vä  vTspaitis  zantJu^  vä zaniupaiti/  daiähsul  vä  daiähupaitil  Yt. 70.18;  84;  —  nmänahe  'paitim  Vr,  J.  2, V.  7. 41,5. 37,  18.  i&;  —  avaiähe  nmänahe 'paite  (VS.)  usthista  V.  1Ä19;  —  «»«3- nahe  'patöis  Y.  13. 1,  V.  10.  5,  Vyt  16;  — nmänake  'paßt  Y.jB.a,   YL/0.17,  JJ.i;
19340:—  frat?md.nmänahe  'paitim  V.  ig.  20; 21.  b)  von  Göttern:  kaoma  'paite vispaite  , .  Y.p,  27,  a)  mit  Gen.  aus nmäna-.  ätnm  vispanqm  nmananqm  'pai- tim Y.  77. 1 1 .
19342:•  j.  lunänö-padni-,  d^m^ö-paSni-'*  f. 'Herrin,  Gebieterin  eines  Hauses,  Haus- herrin'; nmänS paitil .  .  'm  vä  V.  72.  7;  F. 2  f.;  —  d»mqn5pa%ttiY.2i.  a)  mit  Gen. aus  nmäna- :  nmänahe  "nTm  Vr.  J.  3 ;  —  nmä- nahe '^nyä  Yyt.1-;.
19603:•  j.  maSsmö.nmäna-  n.  "mittleres  Haus, Haus  von  mittlerer  Grösse':  /rai?ms.miUi- noAe  . .  'nahe  nmänU.paitlm  \.  13.20t
22915:Zum  V.  varid-,  s.  Bthl.  IF.  ro.  10.  —  ai. vgl.  vardhman-  D.  —  PQ.:  /a  kämak  (fiir vati)  andar  dm  n  n  (Sü.!  sthäne;  s.  nmäna- No.  7).  —  1)  S.  lu  Y.  3S.  3.
29131:haslAäHalayä  -,    harn  dm  n  n  1)  -   Sü. :    saia- väiiHah.    —    ')  Ad«  ar.  *]admai;    %  403.   — «)  Vgl,  iSt  Y.  30.  10,  53.  3.  -  3)  S.  nmäna- No.  7. •    j,    haäa.m^^ra-    i)    Adj.    'mit    dem Mq^ra  zusammenseiend,  mit  ihm  eins'": zara^ultrim  °nm  Vr.  13.  i.         2)  m.  '(Mit- mq'^ra''',    d.  i.)     Ergänzungs/naSra,    Er- gänzung, Nachtrag  zur  Glaubenslehre'*': 'rtm  zainiparlUm,  °räi  zairti.parstili,  'rahe <zaini.parsiahe,  'ra  (VS.)  saini.parsta  Extr. \i-4.
```


## [2026-09-05T17:51:10.735Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '19290,19320p' BRT.txt"
}
```


### [2026-09-05T17:51:10.790Z] TOOL RESULT

```
[•  j.,  g.  nQ  Adv.  'jetzt,  nun';  i)  starktonig;
dby  Google
1089
nmäna-I
1090
a)  an  der  Spiue  des  SaU(teil)cs:  at  fra- vaxsyS  n'  *gUls4Um  (sd.)  n°  sraota  . .  n' Im  vls^a  . .  *matdänAs.dam  (sd.)  Y.  4:5, 1 ; 8;  —  ahuml  n°  na  avarS  (sd.)  Y.  2p. II*'.  b)  in  andrer  Stellung,  mit  i^t: tat  nS  nat^  vanlänl  {sA.)  Y.  57.  i;  — *a%a  *naäj'''  atnim  a^rapaitim  upBissit N. //(?).  b)  schwachtonig,  hinter  dem ersten  Wort  des  Satzes:  asUta  «■  aiAkai haca  VUai  gauÜ  öuyJt  Y.  6^0.  3 ;  —  us  n' aiiihäi  vTse  JamySl  as»m^a  .  .Y.60.3;  — para  »•  ahmst  haca  asanhalca  . .  axliat . . ^■9- Sil  —  *^'i  »°  P<ira  ahmst ..  paiti. - jasätiF  .  ,  Y.g.$$;  j.^n,  F.44;  — ya'^a n'  malysha  *xh/isti  Ä?»(?(sd.)  vTiävc^einti V.2.31;  —  yavat  »'  ah  .  .  P.42{?). ai.  n«,  «M,  gr.  n>  usw.  (i.  BoM.  GrGr,3  544).  — S.  auch  nüram.  —  Pii.r  nun;  i.  noch  No.  1. — I)  S.  na-  No,  3.  ~  »)  UnEtchn;  Hds.  iä%nm trvSaiuim ;  PQ. :  tlänäiHiar,  lässt  also  ttvX  aus.
•  p.  nuram"',  j.,  g.  'nurain,  j, Adv.  'jetzt,  gegenwärtig':  ysi  para  ahmSi harne  gStvS  .  .  hifhitta  .  .  äat  tl  'rqnt fravtttinti  Yt.  /J.  57  f.;  S4j  S6;  —  »ic/»  mE Java  avanhe  'rim  ml  hara  upastqm  Yt. 5.  63;  —  Ab  mqm  'rqm  /räyazäite  . .  'rqm ahmt  yanyasca  .  .  Ylä  15;  23;  —  yat •nm  vysmbura  .  .  vohunTm  vS  tScayHnti Yt /4^  54;  — I  »♦  °r*7OT'>  %uväm  vama- vatäm  BIl^io;  —  'r^mca  yavaila  tätte (sd.)  Y.  62. 6.  a)  mit  Praen.  a  (zu  II  i  b) und  folg.  lu  'auch  jetzt  noch':  mainyü  . . yS  a  'rsmc^  häms  "durch  den  Geist,  der, o  Ah.^  auch  jetzt  noch  der  gleiche  ist"
Y.J/.7-
Anscheinend  ASn.  und  ASf.  va.%  *nüra-  Adj, —  Vgl.  nü.  —  00s».  nur  'jetit'i  vgl.  aj.  nünäm AdT.  'jetil',  np.  nun.—  Pü,:  nun,  SQ.  (zu  Y. 3z):  puBor  api.  —  ■)  Ist  das  Wort  wirklich richtig  geleien?
•  j-i  g*  'nüi^m  Adv.:  s.  unter  naram.
•  j.  'nur«m  Adv.  'in  listiger,  arglistiger Weise':  yat  dim  mairyJ  «•  aspaelu  paiti.- pamala  "als  ihn  arglistig''  der  Schurke zu  Ross  bekämpfte"  Yt  ig.  77;  — >?  mqm mairyS  n*  mans'''^ . ,  paiH^ar>tata  "..  arge List'>  im  Sinn'>  . ."  Yt5.  go.
ASn,  aas  *nura-  Adj.,  eig.  'klug';  vgl.  got. nrnttti)  'at^i^,  gr.  *oü(.  —  i)  Zur  Sache  s. unter  ratura-.  —  *)  Eine  Verbindung  wie  gr. Ititti  iaxm(.  —  Sl  *nura-  (%  Sj,  x)  verhält sich  in  got.  snutr-i  wie  np.  ä-mursaa' rnff/dü.
•  j.  nün^  Adv.:  s.  unter  nßram.
j.  Huruyi:  s.  nar-  mit  No.   14. i.  Alünn.  Wb.
j.  ntatSl  N.  logi  lies  mafrutUat^.
j.  Hmöi  N.  8-,  lid  nmänäl •  j,nrnäna-,g.,j.''dflniana-'',j.'V;'«ff»a- n.  'Behausung,  Haus',  von  jedem  zum Aufenthalt  für  Menschen  (Götter)  und Haustiere  dienenden  Bauwerk,  sowie  auch von  dem  zu  einem  Anwesen  gehörigen Gebäudekomplex;  I)  von  Wohnungen  fUr Menschen  (und  Götter):  yanyS buyä  'nshu ma^yäkanqm  Y.  6i.\;  —  ahmi  *ne  ya^ m!^ayasnBi^{Stve.Tz.)  V.5.45;  —  vasö.. mazdayasna  ahe  'nahe  myasd>m  äaihyäril V,  &22J  —  ätacäni  sünm  'mm  drvatS Yt-5'  3S;  —  <Mi  'tarn  yim  ^alpaihjm Yt5.63;  62;  —  ha%ra  'ni  avastaya  ka~ t>mca  /raslamb>m{s,ü.)Si  ..  V.  2. 26;  — yat  bä  paiti  nä  a/ava  'mm  uedasta  ä%ra- vai  gaomavat  nsirivat  ..  V.J.  2;  15.  ai; —  mürnm  . .  ylF  stunä  v^ärayeiti  iirtsi- mitahe  'nahe  Yt /O.  28;  30;  —  tBm..°na inasilä  ..  dahähi  YtJO.30; —  sraohm .. yS  driyaolca  . .  amava£  'mm  hüm.täsH  Y. $'j.  10;  —  as>m  yS  ahurB  masda  . .  yas> tat  'npm  ahnmm  srirtm  raoximm  frs- d^rirsrym  V.  22.1^;  \.Sy.2i;  —  iaiiihe ka^he  apayisire  'mm  htitaite  hi^ättm  Yt. 5.  loi;  —  aliqm  "nä  hvihätä  .  .  hUhfUe Vti7.  8;  V./j.  4g;  —  hubaotUl  ba^aite °mm  yeAhe  'ne  asis  varmhi  . .  psta  mda- ^aite  Yt.ij.6;  ij.107;  —  iha  ml  tum (nämL./4/fl)  hamJaranuha  *antary.ar^?m •nahe  srJrahe  Ytzj.öo;  jj.  147, 156';  — alU  . .  ramyai  i%a  upa  tmai  °mm  yat ahüiri  Y./O.i;  6'o.2,  Yt  14.41; — vainti ahmi  'ne  sraesS  Y.  tfo.  5;  Yt7j.  52,  FrD. /3;  —  vUfa  'na  sraoiö.psta  yazamaide  Y. 57-34)  —  damt  ha^a  ahmüt 'nät  ..rhyeja ■  •  ^'yeyenti  yejihe  *'?ya*'  sraoh  . .  astf paiti^ants  Y.57. 14;  /o.  7;  —  mä  yave imat  'mm  i^'annS  frazakXi  Y.60.  7;  Vyt 5;  —  xihsii  äfrlnstttu  {jis-viA.  fravas<rfS) ahmya  'ne  vattuhim  asim  . .  xsnüiä  para- yantu  haca  ahmst  'nät . .  msüm  gtnzänä pärayantu  haca  ahmst  'nät  ahmSkfm^a mazdayasnanqm  Yt  13. 157;  Y.  2j.  3;  — aai  ahmSi  'näi  dähäiti  gluica  vqhwa  vlra- nqm/a  Yt.!0.  a8;  —  äat  ..  ahe  'nahe/ra- pi^iws  gäu^  .  -  Y.  j.  3 ;  —  t^it  ahmi  'ne *sänaite  ä^rava . .  äat  ahmi  'ne  Sayhnte  da- hahaca..Y.ii,6;  — /raddhsi  ahe'naheY. 52.4;  4.5,  Vr./J.  13*;  —  'n?m  hS  manyaita paraJa%B  V.  ;*.  28;  ■ —  (8«  miknäi  daiva *aipi.jaiti  'ne  aiAhai  gundayai  (sd.)  V,  3.
35
dby  Google
I09I
i-Ia
nmanaDhan-
3a; —  daevanqm  anSyantqm  ahmaUa  'näi aimäiüi  °tiahe  nmans.palSe  Y.  52,  2 ;  Yt  15. t*;-~fpfvru'^wa,.aora  mainyB kaca  °nat V.  11.10;  — yaoiääta..bun  'na  V. i/.a;  1, 4,  12.2;  —  yat  aiiS  nä yS yaoldi^tyS  hala aHiiyd  'naiiiyö  xshats . .  psrayst  V.g.  39; 40,  13.22;  —  yat . .  aiiqmUt  •»anqm[ca] caratB  dva . .  V.  y.  49 ; — vTspanqm  akmya •ne  nabänasdistanqm  Y.  26'.  7 ;  —  *katämS *naAe*'>  a%auruntm  (sd.)  pärayai  N.  /;  Yt 2.11;  —  t^a.vasatfitha  avi  'tarn  airya- maim  V.  22.  7;  13;  —  tum  . .  sara%uhra *nahe  pourusaspahe'H.  g.\y,  V. /p.  4,  46, Yt  i^.  36;  —  olsmanqmHt  .  ,  vazyäi/  .  . ratsui  'tarn  fränäiayata  A. j.  5:5;  —  us3.- hista  haia  gätvs/rasasa  haca  d^mänSi'-'' Yt  16.2;  —  yavat . .  späna  dt/  hapta  'tia *pairiJ(üahi{sA.)  bavqn  V.J5.4S;  — fratara (sd.)  haca  'na  v>r3syqn  .  .  V.iö.^;  — nistara.naOnal  'nahe  V.  17.  7 ;  6. 43,  g.  33, Yt//.  60;  —  mahsmya  'naÄe  N.yX;  — parepasca  'nahe  V.  y.  45,  46;  45;  —  k»m kfmHl  aipi  'ne  gatu  *saSe  Yt5. 102;  — raocamtn  paiti  'nahe  V.  7. 14;  —  ysi  °nä hqm.6arämahi  .  .  ätnmca  .  .  3at  paslalta ahe  'nahe  spa  vä  na  vä  iriäyäj  .  .  us haca  aHbyS  'naiiby3  baraym  . .  ätnmia  . . ku%a..älr7m  aiti  barqn  ava  aitim  'rum..1 V.5-39-4i;5'33';  —  '""  '»"^^  vfti  vTsi hr3yff  kata  (sd.)  uedat^yan  aetahe  yat iristahe  V.  5.  10;  —  ahe  'nahe  upa.- %'Ui»nsqn  (sÄ)  upa^w3T»tayqn  V,  Ä  10; — yui  .  .  iristim  upaJi?r3%wSJar3m  (sd.) avajtanqn  ava  .  .  iristim  baraytn  avaha 'mm  himaym  upa  .  .  'ntm  baötayqn  . . yezi  . .  *fum  upaJ>jr3%ws.tanm  avaxanqn ava  ..  °n3m  baraytn  V.  4",  af.;  —  ratu- fris  havS  yä  'nahe  *paitiricyehe  (sd.) ^■55-  8)  bes.  im  Gegensatz  zu  Ge- meine, Gau  und  Land*);  'vsa%Pi:^..yS  hu- dänul  damanahya^  xla'hr?m  idßirahya vä  dahySu/  vä  . .  frada%äi  (sd.)  aspfrazats Y.31. 16;  —  3  eJ  'mmf'  vUsm  vä  ist^rtm vä  dahyüm  vä  ädat  dusitäcä  (sd.)  .  ,  Y. ,3/.  18;  —  im  jAw.:  mikrS  .  .  ahmäi frasanäayäti  'tamca  vfs^m^a  zantümca dahyümca  daiiihusasilmca  Yt/o.  87;  18, Y.  62. 5,  V.  Ä  1 03,  N.  6';  —  «5 ..  ahmt  'ne .. aähe  vSse  . .  ahmt  *zantvlf  . .  a^he  da^kvB ftim  vaoSata  . .  ahurpm  P./7;  Y.5.  aS,  Vr, 12.  5,  N.(?;  —  *'nyaca  (LS.)*'  vjsyaca  tarda- vaca  *da^havaca  Vr. /2.  gj  —  yujyastTm haia  *'näp'>  a^a  [. .]  vTsal  ha%r?m  {ha&i)
*zaniaoi   a%a   *datihaot  N.  8;  Y.  sy.  14;
—  fraddäiai  'naheca  visahela  zanßuica ''da^hsiaia  Yt5.6;  /0.17,  18,  83,  V.7.41, 42,  5. 37, 10.  5,  Y.  13. 1,  Vr.^.a,  Vyti6;  8;
—  paiHp?r3nt  annm  mainyüm  hala  "na . .  Visa  . .  zatäu  . .  *daAku  V.  JO.  s  j  — paoiryqn  ihalü , .  'nanamüt  vTsqmia  zantu- nqmca  dahyunqmla  Ytfj,  150;  10.18,  Y. äV,  2j.  I.  a)j.  GS.  oderGP.  mit«Ma«Ä- patay-  (sd.""',  Stverz.)  und  nmanS.pa%ni- (sd.'"',  Stverz.) :  'nahe  nmanS.paitfm . .  'nahe nmanspahnlm  VT.3. a  £;  usw.  b)  j.,  g,  mit GS.  ^arff(sd."'',  Sp.  512  f.;' Stverz,),  vom Paradies:    'nl  garS  Y..,#5.8;  50.  4,  57. 15;
—  haca  raoxsna  garU  'na  . ,  irrjata  haca dusanha  Yt.  ig.  44;  usw.  c)  g,  mit  GS. varfhsul  mananhs  dnwB."'  (vgl.  e):  tBi.. bairyantl  (sd.)  vaahSus  a  °«i^'  manaahS Y.33. 15.  d)  g.  mit  GS.  drüjS  (sd.)"" von  der  Hölle:  drüp  -«f  ¥.4:5.11,  5/.14;
—  yavBi  vispäi  drüjS  'nät  astayö  Y. 46.  II.  e)  g.  mit  GS.  aciltahyä  manar)hs dnwD.  (vgl  c):  yH  xia%ra  *grshmB  hisa- sai  (sd.)  acislahyä  'nl  mananhä  Y-32. 13,  n)  von  EehausuDgcn,  Ställen  für Tiere:  ^riiai(sd.)ca  . .  gsus  apa.jasai yalca atthat  %wyqst?mal/u  asatahqm  . .  banmus paiti  gairinqm  .  .jqfnusva  raonqtn  paxru- mag/u  (sd.)  'nax/u  V.  2.  23;  —  °n»m  gäva- yamrn  (sd.)  nava.h^nm  navajtgmat^m  . . cvat  yavat  'nsml . .  dvadasa  vltsra  (sd.)  . . V./rf.i4.'
*)  Uzw.  an  Grösse  und  Einwohnerzahl  untenan Etebend;  vgl.  SüErl,  lU  Y.  13.  I:  pahcanaratiä- rJyugmam"')  g^kam.  Im  jAw.  wird  einmal  im gleichen  Sinn  wie  timäna-  in  gleicher  Verbindung nä/a-  gebraucht;  sd.  No.  I.
KompA.,  E.;  Ableit.  —  Aus  ar.  *din.ina- (IF.  7.  62);  inm  gr.  V.  iiiua;  ai.  TgL ddma-  TD.  'Haus'.  S.  noch  mäniya-.  — Pö,;  man,  Sü.  (meist):  gr^""!  "-  '">='' No.  3,  5,  7,  10.  —  1)  Nur  Yt.  16.  2  (und F.  2  f.  im  Komp.);  ans  dem  gAw.  Bber- nommen.  —  >)  Kurzes  a  nur  Y.  J/.  16.  — 3)  Pii.:  gardimän;  s.  in  B.  —  4)  Untbem.; so    Pt4   usw.;   s.  N0.8.  —    S  Pü.:    meAan^).
—  6)  Ein  'ämre^itam' ;   s.  Wh.  Gr.»  S  f^^
—  7)  Pü.;  dmnn,  Transskr.j  SO.  (in  Y. J/.  18);  gfham,  (in  Y.  J?,I5):  tthänam.  — »)  Unthem.;  so  K  7  a  usw.;  s.  No.  4-  — 9)  Hds.  timät.  —  ">)  Auch  für  Pü.  —  ")  Pü, erLj  garitmän.  —  ")  Hds. /u/"'.
```


## [2026-09-05T17:51:11.896Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"garö\\.nmäna\\|garö\\.d\\|garö-\\|Paradies\" BRT.txt | grep -i \"garö\" | head -20"
}
```


### [2026-09-05T17:51:11.956Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T17:51:29.488Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== PHD ==\"; grep -n \"mān \\[\\|dūdag\\|dūd \\[\\|garōdmān\\|garōdmán\\|mān'\" PHD_mackenzie.txt PHD.txt | head -20"
}
```


### [2026-09-05T17:51:29.544Z] TOOL RESULT

```
== PHD ==
PHD.txt:164:abarmān [5/mn'] in charge. abarmānd ['pín?nd] inheritance, privilege. abarmānīģ [%n?nyk!] noble. abar-menišn Pf/myn$n'!] proud, haughty. abarón Pf*/xwn! | N wárün] contrary, wrong, sinful. ~ih: sin. abar-6z PóPeoc] stronger. ~ih: mastery. abar-tan [Pltn'] arrogant. ~th: arrogance. abarwēz Pfltvyc | (M *bruyj, N parwéz)] triumphant, victorious. ~ih: triumph, victory. abarzén, v. zmašk, abaxs [hš] repentant; regret. ~ЛЬ : repentance. abaxšāwand [5hP^wnd] regretful. abaxšāyīdan, abaxšāy- [5APd-ytn! | М ?bxPy-, N baxšūdan, baxšāy-) forgive, have mercy on. ~išn: mercy, forgiveness. ~i&nig : forgiving, merciful. labāxtar [*5?*4tl | M 7b’xtr] planet. žabāxtar [PP’htl | (N bāxtar ‘west’)] north. abaydag Pyrťk', v. paydag | M ?byd?g] invisible. ~th: invisibility. abày- : abayéd ['yt' | M Maud, N bāyad] it is necessary, fitting; must (+ infinitive). ~ist Pf?dst' | N bāyist] it was necessary. ~istan [?P?dstn!] be necessary, fitting; desire, want. ~išn: necessity. ~išnīg : necessary, fitting, seemly. abāz [L AWHL < A lI2(w)hr;?Pc | М Рс, N baz, wa] back, again, re-. ~ айдап б: attribute, ascribe to. 7 appoint t= ~ dāštan: withhold, restrain, prevent. ~ ēstādan az: abandon, desist from. — kardan: open. — kardan az: disengage from, wean. ~ mándan: remain behind. ~ pádan: remain, stay. — raftan : issue, go forth. ~ waštan O: turn into, become. ~ wirāstan: rearrange. abāzsār [LAWHLs'I] rebellious. ~ih: rebellion. āb-čihrag [$ cyhlk'] holding the seed, essence of water. abd [>24 | М "Gd J ?bd-] wonderful. ~ sahistan: seem wonderful (to) > marvel.
PHD.txt:170:abilag 5/4! | N ~a] blister. a-bim [bym] fearless. āb-kāmag [5A mk! | N ~a] a thick, sour soup. abnüs Pžēnws | (N ābnūs)] ebony. a-biy Pbwd] senseless. ~ih: senselessness. à abr РЫ, Séi | N ~] cloud. M bel abrang [ing | N aurang] glory, splendour. abrastan, abraz- [AP stn',SPc- | М ?br?st, N (afráttan), afrdz-] lift, raise. abraz [Pe | N afrāz] acclivity. abrēšom Pflyš(u)m | M? bryfwm, N ~} silk. ~én [-yn!] silken. abróxtan, abróz- ['piwhtn', ?phoc- | M brwxt, ?)brwc-, N afróxtan, afróz-] light, kindle, illuminate, polish. ~i$n(ih): illumination. āb-tazan Pftcn!] watercourse. a-bun [*dwx!] baseless, bottomless. a-burd-framān ['bwltplm^n'] disobedient. ~th: disobedience. aburnāy f(w)lnd, v. purnāy | N burnā] under age, child. ^h : childhood. aburnáyag [?A(w)/n’(d)yk'] child. abus [pws] (woman) having just given birth. “АҺ: childbirth. арив, -tan Pws, -tn! | M ’bwws, v. ábestan] pregnant. „il: pregnancy. abydxtan, abyóz- Phywhtn', ?bywc-] join, mix. āb-zan zn! | N ~] bath. labzar [el pel] M *6c*7, N afzār] instrument, means; spice. *abzar [6271 | M bail skill, power; powerful. „ūmand [-wmnd] skilled, able. abzāy-, —išn, у. abztidan, abzón [?pzwn! | M, J ”*bzwn, N afzün] increase, growth. ~ig [-yk!] increasing, expansive, bountiful. ~igih: bountifulness. abzüdan, abzáy- ['pzwtn!,^?pzd- | M ?bz'y-, N afzüdan, afzāy-] in- crease, grow. ~i$n: increase, growth. a-čār [cI] inevitable, Jee ~ag [-k'] compelled.
PHD.txt:180:a-ģumān ['ewrm?n!] without doubt, certain.
PHD.txt:308:dahigān [dhywk’n' | N dihgān] countryman, farmer. dahliz [d^hlyc | (M dhryz), N ~] portico. dahm [d?hm] virtuous, pious; a full member of the Mazdean community, initiate. dahom [hwm | M dhwm, N ~] tenth. dalman [d”/mn' | N dál(man)] lammergeyer, eagle. dam- , ~išn, v. daftan. īdām [d”m | = M] creature, creation. здат [Pm | = M, N ~] tame animal. здат [d’m | P d’mg, N ~] net, snare, trap. dāmād [d?r?t! | M 424, N ~] bridegroom, son-in-law. ~ih: condition of a bridegroom, son-in-law. daménag [dmynk'] fan. damidan [dmytn'] = daftan. dān-, —išn, v. dānistan. -dàn [-d’n' | = M, N ~] suffix, -holder, -container. dàn(ag) [d”x(k)! | N ~a] seed, grain. Н dānāg [4>рА! | М dwg, N dana] knowing, wise. ША zn kh ~ih: knowledge, wisdom. ar dandàn [KK A < А kk’; dnd’n' | = M, N ~] tooth. dānistan, dān- [YDOYTWN-stn' < A У yd‘; d’n-stn' | M d^n-ystn, N ~] know. ~ign: knowledge. ~i8ndmand [- отпа) knowing. dar [BBA < A bb’; dl | M dr, N =] door; palace; chapter, subject. dar [d?] | M d@’r-, N ~] tree, gallows; wood. dar-, -išn, v. dāštan. -dār [-d'/| M -d’r, N ~] suffix, -holder, -keeper. Р darāy [dPg | J ~, N darāy] bell. *darak [dlk'] section, paragraph. darband [B B Abnd | N ~] gate. darbās [dips] palace. dard [dit! | M drd, N ~] pain. ~отапа [отла | M -wmnd, N ~mand] ill, suffering. dārēn [d'/yn! | М drwyn] wooden. darģāh [dig’s | N ~] doorway. dargardih [d*/krtyh | M d’rgyrdyh] crucifixion. dar-handarzbed [BB A-, dl-hndlcpt'] chamberlain. darigbed [dlykpt'] palace superintendent. *darmag [d?/mk!'] fine, delicate. darmān [dim?n! | M drmn, N ~] remedy, medicine. darridan, darr- [SDKWN-tn! < A V sdg; dl-ytn! | N <] split, tear. dàrüg [d"Iwk! | М drwg, N dari] drug, medicament. dār-wāzīg [Tlw cyk! | N dár-bàz] (pole-)acrobat. darz [dlc | N ~] seam. ~ig [-уА! | N darzi] tailor.
PHD.txt:325:farr-, v. xwarrah. Farrūbāģ [plwb(’)g] the first major Fire of Sasanian Eran, that of priests and nobles. farrox [plhw' | M prwx, N ~] fortunate, blessed, happy. ~ih: fortune, joy, happiness. filāsūfā [pyPswkp!y] philosopher. frabih [plpyh | (P frbyw), N farbih] fat, stout. Fradadafš [pldtpš = Av. fradašafšū-| the south-eastern continent of the earth. fradág [MHL < A mhr; ИРА! | N farda] tomorrow. frādahišnīh [pP dhšnyh] increase, progress. fradom [AWLA < Ar. !?wD; pltwm | (M prtwm)] first. ~th: first, beginning. fragan [plk?n'] base, foundation; origin. fragandan, fragan- [plkn-dn'} lay foundations. frahang [pl’hng | N farhang] education; knowledge. --estàn [-st?n!] school. frahanj-, v. frahixtan. frahist [p/h(y)st! | (M pryst)] most (superlative of freh), frahixtag [plhhtk' | N farhixta] educated, trained, skilled. frahixtan, frahanj- [plhhtn', pDhnc- | P frhynj-, N far~] educate, teach, instruct. framādār [рж?РЦ commander, ruler, chief. framān [pim^n! | M frmn, N farman] order, command; a minor degree of sin. ~-burdar [-bwlt?l | N -bardār] obedient, submissive. framāy-, ~išn, v. framüdan. framds [bl(?)mwš | M pr’mws, N farámos] forgotten. framošidan [plmwšytn'] = framuštan. framüdan, framāy- [plmwin', plm'd- | M prm'dn, prmy-, N far~] order, command. — $n: order, commandment. frāmuštan, frāmēš- [pl(?)mws-in' | M prhmwst, pr’mwi-, N fard~] forget. franaftan, *franam- [pinptn!, *plnm- | M prnpt, prnm-] go, proceed, depart. franāftan, franām- [pin!ptn!, pli m- | P fri m-] 1. lead, conduct, re- move, promote; 2. profess, propagate (faith). ~išn: removal, promotion, profession. frarast [p/”Pst'] a cubit (18 in.). fràrón [p lwn'] righteous, honest. ~ih : righteousness, honesty. frasang [plsng | N farsang) parasang (4 Roman miles).
PHD.txt:392:hamēstār, —ih [hmyst!l, -yh] = hamēmāl, ~ih. hamésag [hmyfk! | M hmyšg, N —a] always. ^h : eternity. ~-86z [-swe] ever-burning. hamē-wahār [hmy whl | N haméfa-bahar] marigold. ham-éwénag [Am'dwynk!'] of the same kind, homogeneous. ham-góhr (hmgwhl! | M hmgwhr] of the same substance or nature, consubstantial. ham-ginag [hmgwnk! | M hmgwng] likewise, so. P hāmharz [A())mAlc | P I? mhyrz] adjutant, attendant. hāmīn [A*myn! |= M] summer. ~ig [-yk'] (of) summer. hāmist [KHDE, v. hammis ; )”mst!] all. ham-kār [hmk’l | N ~] collaborator. 7h : collaboration. hāmkišwar [mkyfwl | M. -wr] universe. hammis [KH DE < A k-hdh), ат... ~: together with. hammist [hmyst'] stagnant, peaceful. ~(ag)an [-(kYn'] limbo, the neutral station between heaven and : hell. vl hammóxtan, hammoz- [ALPWN-tn! < A У "Ip: hmwhtn', hmwc-, Ki hmsoz- | M hmwxtn, N āmēxtan, ámóz-] teach; learn. -išn: teaching. hammdxtar [Amwht?!] learner. ~th: learning. hammóz- , ~i8n, v. hammóxtan. —@йг [kmwcek?l | N āmēzgār] teacher. ham-nibardih [hmnpityh] (single) combat. hamēūģ [/tmwg] equal, like. hámón [k mwn' | N kāmūn] level, flat. hámoyén [/?mwdyn!] all. ham-pursag [hmpwrsk!] consulting, taking counsel. ^h : consultation. ham- |-ránih [Am nyh] battle, combat. ~-samiain [-s"m?n!] contiguous. ~-sardag [-sltk'] of the same kind, like. ~-sayag [-sdk! | N hamsáya) neighbour. ~-tag [-t*k! | N hamid] equal, peer. «tan [-tn'] of the same stature, build. ~=-tihmag [-twhmk'] relative, relation. hamwar [hmwl | N hamwār] level, abreast. hámwiür(ag) [%()mw?/, -k! | N hamwdara] always. ham-zamān [hm ODNA | N —] instantly, immediately. handām [And*m | = P, N andàm] member, limb. handarz [hndle | N andarz] advice, injunction, testament. handarzénidan, handarzén- [hndleyn-ytn!] advise.
PHD.txt:394:handāxtan, handāz- [hnd@htn', hnd?c- | M hnd?c-, № an~] plan, allot, reckon, judge. ~išn: judgement. handāxtār [%nd”%t”[] planner. handāz-, ~išn, v. handaxtan. ~ag [hnd?ck! | N andáza] measure, manner; ~ 1: like. handēmān [hndym’n' | = M] before, in the presence of. ~th: audience, presence. handēmānģar [kndym’ nkl] introducer (into the presence). „lt: introduction. handéSidan, handēš- [Ahndyti-ytn! | M hndy§-, N an~] think, consider, reflect. išn: thought, reflection. handēšīdār [hndyfyt?I] thoughtful. handēxtan, handēz- [hndwhtn', hndwc- | N an~] gain, acquire, amass. „-išn(īh): acquisition. handraxtag [hndl htk! | P ?ndrxt] oppressed. ~ih: oppression, suffering. handüdan, *handāy- [hndwtn' | (M ?nwd), N an~] smear, plaster, anoint. hangad [hngt! | P ?ngd] fortunate, rich. ~ih: fortune, wealth. hangām [hng’m | N ~] time, occasion. ~ig [-yk!] timely. hangarag [hng’lk' | N angara] reckoning. hangardan, hangàr- [hng’l-tn' | M hng^r-, N an~] consider, reckon. ~išn: consideration. hang��xtan, hangéz- [hngyhtn', hngyc- | (M hgjyn-), N an~] arouse, stimulate, stir up. ~išn: arousing. hangirdénidan, hangirdén- [hngityn-ytn'] complete, summarize. hangirdig [kngltyk'] complete, perfect; summary. ~ih: completion, summary. hangdSidag [hngw£ytk! | M ”ngwšydg] way, manner, likeness. ~ 1: like. hanģrāyīdan [hngl’dytn'] lament. hangrüdag [hnglwtk'] lamenting. hanj-, v. hixtan. hanjaftan [hncptn' | P hnjft, (M hnzpt)] be finished. hanjāftan, hanjām- [hnc’tn', hnm- | P hnj ft, hnjm-, (M hnzpt, N anjāmīdan)] finish, complete, carry out. hanjām [kne m | N anjám] end, completion, outcome. hanjaman [hncmn! | (P ?njmn, M hnzmn), N anjuman] gathering, assembly, congregation, community. ~ig [-yk'] (notable) member of the community. hanjīdan [hnc-ytn' | N ~] = hixtan.
PHD.txt:426:kardan, kun-, (P Каг-) [OBYDWN-in' < А У Фа; krtn!, kwn-, (kl-) | M kyrdn, kwn-, (P kr-), N ~] do, make, act, perform. ~išn, v. kunišn. kardār [krt-, kil | N ~] active; worker, doer. ~th: activity. kard-espās [krtsf?s] servant, attendant. kārezār [A /yc! | M k*ry2*r, N kārzār] battle(-field). kār-framān [%'/p/mn' | М k’rprm’n, Ar. qahramán] manager, overseer. karg [klg | N ~] rhinoceros. kargās [klk’s | N kargas] vulture. kárig [k’lyk'! | N kari] active; warrior. ~ih: activity. kark [АА | N ~] chicken, hen. karkéhan [k/kyhn'] chalcedony. karm [Айт | P krm] action. karmir [klmyr] red, crimson. kār-nāmaģ [Rr mk!] record, chronicle. karr [k/ | M qr, N ~] deaf. karx68 [klhwš | (IN čarxušt)] wine-press. *karzang [kleng | M kyrzng, (ЇЧ xarcang)] crab; astr. Cancer. kas [4 YŠ < A?y£ | M ks, N ~] person, somebody. ~-iz [-c] anybody, (with a negative) nobody. kāskēn [k’skyn'] lapis lazuli. (аб) murw [-&! | N kāskīna] *magpie. ~ën [-yn'] blue-green; of lapis lazuli. kastan, kāh- [R’stn', Ph- | N ~] diminish, decrease, lessen. ~iSn: decrease, diminution. kastār [kst?]] destroyer, wrongdoer. ~ih: destruction, iniquity. kāstār [ks 1] diminisher. kaš [Rs | N ~] armpit. kaSawag [kšwk! | N kašaw] tortoise. kašk [АА | N ~] dried buttermilk. kaštīg [Astyk' | N kaštī] boat, ship. tkawādak [kw’tk'] young; baby; v. kodak. ikay [AYM T < А ?уті | N ~] when? 2kay [kd | N ~] title of the dynasty of Wištāsp (patron of Zoroaster), Kayanian. ~ak [-&!] ruler hostile to Zoroaster. kayk [kdyh! | N ~] flea. kë [MNW < A mn-w | M ky, N ki] who, which. P keč [kyc | = P] person, somebody. kéd [ду | P gydyg] soothsayer, magician. ~igih [-ykyh] soothsaying, prophecy. keh [ks | M kyh, N ~] small(er), less(er), young(er). ~tar [-il | N ~] = keh.
PHD.txt:480:mehmān [m(?)hm?n' | Р myhm?n, № ~] inhabitant, guest; acceptable. ~1Һ : habitation; hospitality.
PHD.txt:545:pas-dānišnīh [4HLd’nsnyh] anti-knowledge. pasēmāl [psym’l, v. hamemal] defendant, accused. ~ih: (legal) defence. pasen [psyn! | N pasin] final, last. pasox [p’shw' | № ~] = passox. passand [psnd | N pasand] pleasure, liking. passandidan, passand- [psnd-ytn' | M psynd-, N pasandidan] like, approve. ~išn: liking, approval. ~isnig : likeable. passáxt [ps’ht'] test. passaxtan, passàz- [ps’hin', ps’c- | M ps?xt, ps’c-] fashion, prepare; insert; test. ~išn: preparation, constitution. passazag [psck! | M pscg] suitable, fitting. ~ih: suitability. passox [pshw! | M pswx, № pāsux) answer. past [pst' | N ~] low; astr. dejection. pašēmān [pšm?n! | = M, N ~] penitent, repentant. ~ih: penitence, repentance. pašm [psm | N ~] wool. ~ёп [-yn! | N ~in] woollen. pašn [psn'] bond, agreement. pāšnag [p’snk! | N ~a] heel. pāšom [p(”)$zvm) excellent. passing [pšng | N pišing] drop, exudation. paššinjag [pfnck! | N pišanja] drop. paššinjīdan, paššinj- [psnc-ytn' | N pišanjīdan) sprinkle. ~išn: sprinkling. pa&t(ag) [pšt(k)! | J pst] pact, bond, agreement. *pattān [pt’n'] noise, resonance. ~6mand [отта] resonant. pattāyistan [pi?dstn'] = pattüdan. pattüdan, pattày- [ptwtn', ptd- | P ptwdn, M pt’y-] stay, remain, last, endure. pattüg [ptwk'] enduring, patient, persevering. ^АҺһ: endurance, patience, perseverance. paxSag [phšk! | N pasa] mosquito, gnat. 1рау [pdy | N ~] foot; footstep, track. ~ 1: after. *pay [pdy | M pyy, N ~] sinew, tendon. pay [LGLE < А rglh; p'dy | M p'y, N —] foot, leg; foot (12 in.). 1,2 páy-, у, bL? pādan. payādaģ [pd’tk! | М py’dg, N piyada] on foot, foot-soldier, (chess) pawn. payag [p'd(y)k! | N paya] base, station. paydag [pyt?k! | M pyd'g, N payda] visible, obvious, revealed.
PHD.txt:547:~th: visibility, appearance. paydagénidan, paydagén- [ ГОР hinin | M pyd'gynyd] reveal, explain. paydagihistan, paydagih- [py kyh-stn'] appear, be revealed, payg [pdh! | (P рар), N ~] foot-soldier, courier. *paygal [pyg'l | N payyāla, piyála] cup, goblet. -- gar [-A/] cup-maker. payģām [pgt”m! | M pyg’m, N pay(y)ām] message. ~bar LA | N -bar] messenger, apostle. paygos [p?tktvs | M p’ygws] district, province. paymān [pim”n! | M pym?n, N ~] measure, period; moderation; treaty. 6 — madan: reach maturity. ~ag [-k! | N ~a] period, measure, proportion. paymānīģ [ptm”nyk!] moderate. ~ih: moderation. *paymar [PK DWN < А pqdwn; p'tym'l] appointment, assignment. paymāy-, v. paymüdan. paymēģ [ptmwg | M pymwg] clothes, garment. paymóxtan, paymēz- [ptmwhtn!, ptmwe- | M pymwxt, bymwc-] don, wear. paymēūzan [ptmwen' | M pymwen] garment, dress. paymüdan, paymāy- [ptmwtn', ptm’d- | N ~] measure. *payram [p’tlm] the commonalty,-people. payrāstan, payrāy- [pt-, pyPstn!, pyPd- | M ругі, pyr!y-, N pērāstan) arrange, adorn. payrayag [руРак! | M pyr)yg, N pērāya] ornament, adornment. payrēģ [ptlwk'] light, brightness. paywand [ptwnd | (M руп), N ~] connection; offspring. paywand-, v. paywastan. paywasag [ptw’sk'] leather bag, wallet. paywastag [pteostk! | N ~a] continually. paywastan, paywand- [ptwstn!, ptwnd- М pywst, (pywyn-), N ~] join, connect. paywāz- [ptw’c- | M pyw’z-] answer, reply. ~ag [-k!], —i$n: response. paz-, v. poxtan. pāzand [p’cnd | N —] the Pahlavi commentaries on the scriptures (zand), transcribed in Avestan letters. pazd [pzd | — P] oppression, persecution. pazd- [pzd- | = M] blow, play (flute). pazdaģīh [pzdkyh] expulsion. pazdénidan, pazdén- [pzdyn-ytn' | P pzd-] frighten, chase. pāzen [p’c(y)n' | М pen, N pazan] ibex. pazüg [pzwk! | (N payūk, xabazdū)] guinea-worm. ~ í gühgard / gGhward: dung worm. pazzāftan [p> tn ' (M pzpt „intr.)] (cause to) ripen.
PHD.txt:562:sabuk [spwk! | N ~] light, easy. sabz [spz, sbz | N —] green, fresh. sad [roo | M sd, N ~] hundred. Sadwés [stwys | M sdwys] a star (Fomalhaut ?). ваб [KLBA < A klb | N ~] dog. Zeag [sk!] stone. sag [PR | P g] number. sagén [skyn! | M sygyn] stony. sagr [sg] | N sēr] sated, satiate. «ЛЬ: satiety. sahig [shyk' | M shyg, N sahi] worthy. ~th : worthiness. sahistan, sah- [MDMEN-stn' = A mdmh, V dmh | (M shyd, s‘y-)] seem; seem proper. ~išn: satisfaction. sahm [skm | = M, N ~] terror. ~gin [-k(y)n! | N —gin] terrible. ~genith : terribleness. sahög [shwk'] hare. sāk [s | (N sdw)] tribute. sal [SN T < A fnt | (M sr), N <] year. -sálag [SN TA, oli | N -sala] . . . -years-old. ~ih: age (of... years). salar [srd?] | M ffr, s’r’r, N ~] leader, master. ^h : authority. salwar Leikofl perennial. sāmān [?mn! | = M, N ~] limit, boundary. —Óómand [-’wmnd | M -wmnd] bounded. samór [smzl | N ~] sable (marten). sàn [?л! | N ~] kind, manner.
PHD.txt:568:spas dāštan, ~ hangárdan: thank, give thanks. spās-dār [sp?sd?] | N sip~] grateful, thankful. ~ih: gratitude. spās|-ešnās [sp’ssn’s] grateful. —ómand [-’wmnd] grateful. spas [sp = Av. 0Bàsa-] space, atmosphere. spaxr [sp?hl | M ‘spxr, N *siparx] merrymaking, revelry. spazg [spzg | (M ‘spgj), N sipazg-] slanderous. «il: slander. spëd [spyt! | M ‘spyd, N sapéd] white. ~ag [-k! | N -a] white (of egg, etc.). —bàg [-p’k!' | N -bā] curd soup. --dàr [-?1 | N -dár] white poplar, aspen. spenag [sp(y)m?k! = Av. spanta-, cf. $annág] holy. ~ ménóg : the Good Spirit. Spig [spyk' | M ‘spyg, (N sapriy)] т. brilliance; 2. sprout, shoot. spihr [spy(y)hl | (M ‘spyr), N sipihr] sphere, sky, firmament, fate. ~ig [-yk'] heavenly. spinjanagih [spne’nkyh] hospitality. spiš [spyš | (N šipt$)) louse. Spitāmān [spyt?m?^n] of the Spitama family. spiz- [spyc- | M “рухіп, *spyz-] 1. shine; 2. sprout. —išn: 1. brilliance; 2. sprouting. spöxtan, spēz- [spwhtn', spwc- | M *spwxt, N sip~] thrust; overstep, disobey; delay, reject. ~išn: delay, rejection; disobedience. SpOz [spwe | N sipóz] disobedience; delay. ~gar LEIT N ~] disobedient; dilatory. sprahm(ag) [splhm(k') | M *sprhm(g), N siparham] flower, fragrant herb. spul [spwl] spleen. spurdan, spar- [spwiltn', spl- | N sip~] tread, trample. spurrig [spwlyk!' | (M ‘spwr), N sipari] entire, complete, perfect. ~ith: completeness, perfection. spurz [*spiz | P “spwrz, N sipurz] spleen. srat (sit! | cf. Ar. sirát] street. sraw [s/wb'] word, spell. srawénidan, srawén- [slwbyn-ytn'] report, broadcast. sraxtag [s/htk! = Av. sraxti-] side, part. sray [sd | N saray] house, hall. Igrāy-, -išn, v. srüdan. srāyīdan, ?sráy- [sPd-ytn! = Av. @rdya-] protect. ~išn: protection. srešk [sl(y)£h | (P srsk), N sirifk] drop, tear. srištan, *srēš- [s/szn! | P sryi-, N sir-~] mix, knead. sri$wadag [s/ystotk! = Av. Oriswa-] a third. sréd [s/zvt! | M srwd, N suród] song.
PHD.txt:593:tan-bahr [żn'Þ’ hl] physique. tand [tnd | = P] faint, languishing. ~ih: faintness, langour. | tan-drust [tn'drw(y)st! | N ~] healthy, whole. ~ih: health. tang [ing | = M, N ~] narrow, tight. ~ih: narrowness; distress. tanig [tn'yk! | N tani] bodily, corporal. tanigard(ig) [tnykrt(yk)! | M inygyrd] corporeal. ` tanīhā [tn'y/? | M tnyP?, N tanha] alone. tanómand [tn wmnd | N ~] corporeal. “АҺ: corporeality. tan-tdhmag [tn'twhmk'] (sap) of plants. tanuk [tnwk! | N ~] thin, shallow, tanür [tnw] | M tnwr, N ~] oven. tar [LCDr! < A l-sd; tl | M tr] over, through, across. ~ kardan, ~ menidan: abuse, despise. -tar [-z# | (M -dr), N ~] suffix forming comparative adjectives. tar [2] | M гу] darkness. tarāzēnīdan, tarāzēn- [tcyn-ytn!] weigh. tarázüg [tPcwk! | (P tPzwg), N tarazü] balance, scales; astr. Libra. targ [tlg | N ~] helmet. tarģumān [tigm?n! | M trgwmn] interpreter. tarig/k [PIyk! | M гуур, N tárik!] dark. ~th: darkness. tarist [¢/st'] = tar. tar-mānīh [t/m’nyh] perversity. tar-menišn [tImynin! | N tarmanist] perverse; contemptuous. 7h : perversity; contempt. tarr [t/, LC Dr (in error, v. tar) | N —] moist, fresh. ~ag [tik! | N ~a] vegetable. tars [2/5 | M trs, N ~] fear, respect. tarság [ts k! | M trs’g, N tarsā] Christian. tarsāģāh [15(?)/?5] respectful, reverent. ~ih: respect, reverence. tarsidan, tars- [tls-ytn' | (M tyrs??dn), N ~] fear, be afraid. tarwénidan, tarwēn- [t/zvyn-ytn! | M trw-] overcome, conquer. tas [25 | N ~] die (for gaming). tasum [tswm | = M] fourth. tāšīdan, tāš- [O i-ytn!'] cut, cleave; create. taSkanag [tšknk!] under-shirt. tašt [tšt' | N ~] bowl. tāšt [021] *certainty. ~ig [-yk'] certain. tāwān [1?(d)w’n' | N ~] compensation, obligation. taxl [t?% | (M thr), P txl, N talx] bitter.
PHD.txt:597:tru(f)Š [t/wu(p)$ | (P tryff), N turf] sour. truftag [t/wptk'] stolen; intercalary (days). tuhig [twhyk! | M twhyg, ЇЧ tuhi] empty, vain. ~ih : emptiness, void. tumbag [twmbk' | N ~a] drum. tund [twnd | N ~] sharp, violent. ~ih: violence, vehemence. Tür [twl | N ~] one of a people inimical to Eran, Turanian. ~ап [—n! | N ~] (land of) the Turanians. Turk [twlk' | N ~] Turk. tu&t [twst'] silent. tuwān [twb!n! | M twn, N ~] might, power. ~ (+infinitive): it is possible to, one can. ~ag [~k' | N —a] mighty, able. «gar [-kl | N ~] rich. ~garih: richness, wealth. ~ig [-yk'] able. ~igih: ability, power. --sāmān [-s’m’n'] the extent of one’s ability. tuxšáé [twhPk! | M рох р, N tuxsa] diligent. “Аһ: diligence, endeavour. tuxšīdan, tux&- [гол у! | (M. twxf‘yst), N ~] strive, endeavour. ~išn: endeavour, striving.
PHD.txt:605:wad-baxt [wtP ht! | N badbaxt] unfortunate. wad-dil [wtdyl | M wddyl, N baddil] coward(ly). wadgarih [wtglyh] evil-doing. wād-ģirdaģ [w° tgltk' | (N gird-bād)] whirlwind. wad-góhr [wtgwhl | N bad-gauhar] ill-, low-born. wad-kamag [wtk’mk'] malevolent. ~ih: malevolence. wadrang [w’ ting | N bādrang] citron. cc Dë [-bwd | N -bóya] lemon balm. wad|-tóhm [wttwhm] = wad-góhr. ~-wazag [-w’ck! | (N gawāža)] abuse. --.Xém [-hym] ill-natured. waf- [wp- | Р wf-, (N bàf-)] weave. ~išn: weaving. wafr [wp! | M wpr, N barf] snow. ~énag [-ynk!] а sweetmeat. waydān [wy?n! = Av. waybana-] head (ahuric). wahāg [wP?k! | M тор, N baha] trading; value. — burdan: value, estimate. wahār [wh], (bj?l) | M wkr, № bahar] spring. ~ig [-уЁ! | N -z] spring, vernal. wahig [ZZLA < A Semi (?); whyk' | M whyg, N *bahi] kid; astr. Capricorn. wahist [ол | M whyst, N bihist] paradise. ~Ig [-yk! | N -1] (worthy) of paradise. Wahman [whwmn' | M whmn, N bahman] Good Mind, the first Amahra- spand, guardian of cattle; cal. 11th month; 2nd day. wāhmān [*w-n! = whmn' | MOw^hmn, J whmn, N bahman] so-and-so. Wahrām [wlhl?’n', whPm | M whr’m, N bahram] god of war, victory; astr. Mars; cal. zoth day. ātaxš 1~: a major sacred fire. wak [wk! | N bak] frog. wālan [zo n! | (IN barzan)] settlement, community walg [wlg] = warg. walidan, wāl- [w]-ytn! | N bdlidan] grow, increase, prosper. ~išn: growth. wümidan, wam- [w’m-yin'] vomit. wan [wn' | N bun] tree; stock, stem. ~ i $urgünig : pistachio tree. ~ 1 was-téhmag: the Tree of Many Seeds. wān-, ~išn, v. wanidan. wanafšag [zvnpšk! | N bunafša) violet. Wanand [wnnd] astr. Vega. wandaģ [wndk'] rope, cord. wang [KALA < А ql’; wng | = M, N bang] voice, cry. wānīdan, wan- [wn-ytn! | M w’n-yst] conquer, overcome, destroy.
PHD.txt:677:zamān [ОЮМА < А ‘dw; gwn’, zmn! | M zmn, N ~] time, hour. ~ag [zm)nk!] = zaman. *zamānīģ [zm”nyk'] prescribed. zāmēnīdan, zāmēn- [p myn-ytn' | M z?myn-] lead, send. zamestān [z7nst?n! | (М dmyst?n), N ~] winter. zamīģ [z-, zmyk! | M zmyg, N zami] earth. ~ig [-yk'] terrestrial, earthly. ---paymānīh [-pim’nyh] geometry. zāmyād [*zmd't! (misreading of z'myzdt! = zām-yazd?) | М myd, N —] cal. 28th day. zan[NYSE < A nth; zn! | = M, N ~] (ĝl. -ān, -in) woman, wife. zan- , —i$n, v. zadan. 1zand [znd | N ~] commentary, explanation, Zend. *zand [zzd | = M] district, tribe. zandag [zndk! | N zanda] rampant. zandbed [zndpt' | M zndbyd] headman of a district, tribe. zandik [zndyk' | N ~] heretic, Manichaean. rmih: heresy. zang [zng] ankle, shank. zangig [zngyk! | N zangi] negro. zanjir [zncyl | (P zyncyhr), N —] chain. zānūg [2”nwk! | P z^nwg, N zānū] knee. zard [21 | N ~] yellow. ~1һ : yellowness. zardaģ [z/tk! | N zarda] (egg) yolk. zardak [zltk! | N ~] safflower. zard|-alüg [zit?hwk! | N ~ü] apricot. ~-tdbag [-cwpk! | N —čēba] turmeric. Zardu(x)&t [zltw(h)st' | (M zrdrwšt), N Zardust] Zaraduštra, Zoroaster. zargon [zlgwn' | P zrgwng, N zaryün] golden, green, fresh. ^ jh: greenness. zarig [zlyk' | M zryg] sorrow, grief. ~6mand [-’wmnd] sad, sorrowful. zarmān [zin?n! | M zrwn-, N ~] old man; old age, decrepitude. ~ih: old age. zarr [ZH BA < А zhb’; DHBA < A dhb | M zr-, N ~] gold. ~én [ZH B Aua. zlyn! | M zryn, N —in] golden. ~(i)gar [zlykl | N ~gar] goldsmith. zarwan [2/wp?n! | P zrw’n] old age. zastan, zāy- [zstn!, z())d-] ask, demand. zaxm [ztm, z?hm | (P jxm), N ~] wound. тау [zyd$ = Av. zaya-] instrument, weapon. ZÁy-, v. zastan. zay-, -išn(-ig), v. zádan. Zāyč(aģ) [z'yc(k') | N zāyča) horoscope. zayistan [2”dstn'] = zastan.
PHD.txt:5200:wināhgārīh d: AS 4431 niwāg aru | wināh- - 35211 winühidan TL 11 wināhišn 1745.29 41 nang Au wind- - 23 windādan Wed 11 niwéy- — 4911 niwéy- e 41) niwēyēn- -P niwčyēnīdan “тёз v 4911 niwē, wandag 155 141 wanigarih «D As" niwēyišnīh Be r^ 4311 niwévisn VU 4) VI windišnīgs Vays | windišn tr 1) wahmān', wan, win Au wanand AW nozdah ap i nog 1311 nógzad res aw nūgzādag sterd 411 nógróz an 53
```


## [2026-09-05T17:51:31.207Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== NYB ==\"; grep -n \"garōdmān\\|garōtmān\\|garōdmāt\\|dūtak\\|dūdak\" NYB_vol2_glossary.txt | head -20; echo \"== NYB man ==\"; grep -n \"^mān\\|mān, \" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-05T17:51:31.274Z] TOOL RESULT

```
== NYB ==
== NYB man ==
1227:dat [d?t'] 1. law 6413-19, 6916, 8623, 9811, — 2. age 2?9 (with the gl. hangäm). 31. 10*%. 14°. 165. 622. 104°; cas. obl. dātēh 536-22, — 3. created, pt. of dätan: dēvān ~ created by the devs 1038-10-13, — 1. Av. (726) ddta- NP ddd ‘justice, equity’. — 2. NP dad ‘life, age’. — 3. Av. (671 sq.) daēvē.dāta-. dätan [YHBWN-tn'; d’tn' 119%, 1201] dah- [always YHBWN-], lst p. sg. YHBWN-m = dahom; 3d p. sg. = 2nd p. pl. ~ -yt = dahét; lst p. pl. ~-ym = dahem; 3d p. pl. ~-d = dahénd; subju. 2nd p. sg. —-'h = dahäh 34%; imp. sg. ~ = dah; pt. = pret. pass. 3d p. sg. dāt [YHBWN-t', inser. YHBWN; d>t' 22. 922 etc.] lst sg. dāt hom 57°; 2nd p. sg. dāt h&5'1*-* 3d p. pl. dāt hend '18?, construed as an act. form 18?!; pluperf. 3d p. sg. dat estet 8712, 3d p. pl. ~ ēstēnd 94*4; opt. pass. dāt [HWH-d =] he 2%; A. to give SPrs:15; 238-21 ete. passim; apāc ~ to give back 345-6; — fräc ~ to give away 5016-1’; — v, also dröt, framān, passax", zančh. — B. 1. to put, to place,
1733:guman [gwm'n'] doubt: ~ kartan pat to doubt 1074; ~ bütan pat to be doubtful of 108?. — = NP; MPrs. gwm?n, v. Sogd. 42; Paz. gumq. — V. a-gumān, apē-gumān. gumänöh scepticism, unbelief 1083.
2101:i [Prs inscr., Ps.. ZY; BP contracted to a ligature coinciding with y: ZY, except when connected with an encl. pron.: ZY- m = i-m, ZY -t = i-t, ZY -š = 4-6, ZY-m’n' = i-mān, ZY-Vn' = i-tün, ZV šin! +-šān] A. a) relative pron., may be used as the subj. or the dir. obj. of its clause: hān i ó man mat 12°; én fradand + andar aškamb därem 1013; has no cas. obl; instead it takes an encl. pron. referring to the correlate: hàn ... i- dmocišn he whose education 80" (rare, commonly k&-$); cannot be governed by a prep.; instead the prep. is placed ?n the clause and governs a pron. referring to the corre- late: *sīh-ē (v. ?sih) ... $ hac han nēva- koktar butan ne šāyist ‘splendor quo nullus pulchrior esse poterat’, a *splend- our that was the most beautiful. ever existent 717-18; or the prep. is changed into an adv. connected with the vb. of the clause: méx i patiš bandēnd 300 xirs poles on which they fasten 300 *rings 2026 (bastan construed with pat; patiš the adv. of pat, v.s.v. patiš); in such cases ke is more usual. — b) conj.: &on l . $ so ... that 2016-17, 3226-27; cand i as much as 3119; 4 ka, hān 4 ka, v. ka; —i-šān 4, 1-8 $ when, as soon as 5811,
2403:mānā(k)kāi
2409:mānākēh 125
2411:mānākēh [m’n’kyh] similarity 11220, — Abstr. of mänäk, MPrs m'n'g ‘similar, like’ (S, A-H II, Verbum 177); Paz. manda; NP mana ‘seemingly, probably’ (Sn); mänistan ‘to resemble’. Cf homänäk.
2414:māndakēh fatigue 1471. — NP mändagi from māndah ‘tired’.
2416:mānēh [m?nyh] settlements, coll. of man (g. v.), 11418.
2423:mānišn [m'nšn'] dwelling, dwelling-place 5814 1075-12, 1179. — V. man. .
2424:mānišnūmand [m’nän’wmnd] possessing dwelling-places, well populated 574,
2425:māništ [m”?nyšt'] abode 8611. — Paz. mą- nastan (Mx).
2809:cas. rect. 6 < avah, cas. obl. õi < avahya; ēišān < gen. pl. avaisäm (OP), whence MIr "oiš which was enlarged by the ending -än of the cas. obl. pl., cf amän, -mān, (a)tän, (a)šan. MPrs ’wy, pl. ’wys’n; in Prth ava- is only preserved in adverbs. Paz. či, ošgn; NP ö(y), vay (< aváhya), pl. īšān. l
2996:pašēmānēh [pšym'nyh] repentance 10?!. 128, 6822. — MPrs pšym'n(yg) ‘repentant’ (S); Paz. pašēmg, abstr. pašēmānī; NP pasimän, pišmān, pizman, abstr. pašī- mani, pišmānī. Of NW origin: paše the NW form corresponding to SW pasé (q. v.) + *mdna- ‘measure’, ‘repentance’ being understood as an ''after-measuring''; cf framän.
7322:pašīmān, pišmān, pižmān, pašīmāni, pišmānī: pasēmānēh
```


## [2026-09-05T17:51:36.191Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dūdag\\|dūdag\\|dwtk\\|dūd \\[\\|garōdmān\\|garōd\\|garōt\" PHD.txt PHD_mackenzie.txt | head -10"
}
```


### [2026-09-05T17:51:36.249Z] TOOL RESULT

```
PHD.txt:316:drón yaštan: consecrate the sacrificial bread. drēš [410] mark, branding; punishment. ~ag [-k!] *desolation. drēšīdan, dro$- [d/w$-ytn'] brand. drēūšom [dlwšwm] mark. droz-, v. druxtan. drózan [dlwen! | M, J drwzn] lying, liar. ^h: falsehood. drubušt [di(w)pwst'] fortress. ~ih: defence, fortification. drüdan, *drün- (HCDLWN-tn! < A У hsd | M ача, (dwr-), N durüdan, diraw-] reap, mow. drust [drw(y)st' | (M dryst), N durust] right; well, healthy. —Ih: righteous; health. drustabed [drwystpt'] chief physician. društ [dlwšt' | N durust] harsh, rough, severe. ~ih: harshness, severity. ~-Awaz, ~-éwaz [-p'c, ~yw’c] harsh-spoken. druwand [dlwnd | M drwnd] evil, sinful, unrighteous. ~īh: sin, unrighteousness. druxtan, dróz- [dlwhtn', dlwc- | M drwxt, drwz-] lie, deceive. druz [dlwe | (P drwj)] demon. айа [dwt! | M dwd, N ~] smoke. düdag [dwtk! | N —a] family. dudigar [dtykl | M dwdygr, N digar] second. duj-, = duš-. ~-daft [dwsdpt'] ill-breathing, short of breath. ~-dānāg [dwšd”7?k!] ignorant. ~-dén [dwšdyn' | M dwjdyn-] of evil religion. «=dēys*rīh [dwsdwyslyh] the evil eye. ~-gand (dtwsgnd | P dwjgnd] stinking. ~-gandih: stench. dum(b) [dwm(b') | N ~] tail. ~dmand [-'wmnd) tailed. ааг [LH YK'! < А rhyq; dul | M dur, N ~] far, distant, remote. durgar [dwlgl | N ~] carpenter. dusraw [dwslwb!] notorious, dishonoured. ^Ah : notoriety, dishonour. duš- [dws- | = M] ill-, evil-. ~īh: evil, wickedness. ~-абаһ [dw??^ Es] foolish, stupid, ignorant. ~-абаһіһ : foolishness, stupidity. ~-arz [2 ic] worthless. 7--Ca&m [-cém] envious. —-Ca$mih: envy. ~-tihr [-cyhl | M dwfcyhr] ugly, hideous.
PHD.txt:649:waxšwar [whiwl | N waxtür] prophet. ~th: prophethood. P wāxtan, wāž- (w’hin', wc- | P wxtn, и?с-] say, speak. lway [wd = Av. way-] bird. *way [wd = Av. wayu- | P шуш] air, atmosphere. ~ í wattar: a demon. ~ i weh: a divinity. way [wd | M wy, N ~] woe. lway- [w*d- | M w’y-] fly. ~endag [-(y)ndk! | J w|B' ynd?] bird. wüyidan, *way- [w'd-ytn'] blow (of wind). wayodagàn [wydwtk’n! | M *wywdg'n, N bayēgān(ī)] nuptials, marriage feast. waz-, -išn(-īg), у. wazidan. waz [wc | = M, (N bāj)] word, speech; ‘grace’ (before meals). ~ griftan: say ‘grace’. 1, *wüz-, ~iSn, v. b *wāzīdan. P wāž-, v. wāxtan. wāzag [w’ck'] utterance, saying. wazay [wzy| N ~, bazay] frog. wāzār [w’c?l | M w?c'r-, N bázár] market. wāzāraģān [wlkn! | M wergn, N bázárgàán] merchant. ~ih: trade. wazidan, waz- [wc-ytn! P wz-, N ~] move, blow (of wind). ~išn: movement. ~i$nig : mobile. Iwāzīdan, wāz- [wc-ytn'] move, carry away; fly. ~išn: flight. *wazidan, w4z- [w'c-ytn! | N bāzīdan) play. wāzīģ [w'cyk! | N Бахт] game, play. wazr [wel] = *warz. wéd [wyt' | N bed] willow. weh [SPYL < А #руғ; wyh | M why, wyh, N bih] better, good. ~ih: goodness. «-dēn [-dyn' | N bih-din] of the good (Mazdean) religion. wēhm [*wyyhm | M wyhm] large, wide, broad. ~ih: width, breadth. wém [шут | = P] rock. wēmār [wyml | M wym’r, N bēmār] ill, sick. «Ih: illness. wén [wyn'] breath. wén-, ~i5n(-ig), v. didan. wēnāb [wyn’p | N binàb] vision. ~dag [-d’h', -t*k!] visible. wënäe [wyr?k! | M wyn!g, N bind] seeing. ~īh: seeing, sight.
PHD_mackenzie.txt:2101:diidal1 [dwtk I N .....a] family.
PHD_mackenzie.txt:5285:wayOdagan [wydwtk)n I M ·wywdg)n, N ba)'ogan(i)] nuptials, marriage
```


## [2026-09-05T17:51:37.920Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^man \\[\\|man \\[m'n'\\]\\|mān(išn)\\|garōtmān\\|garötmän\\|dūtak\\|dütak\" NYB_vol2_glossary.txt | head -10; echo ===; grep -n \"m'n'\\] \" NYB_vol2_glossary.txt | head"
}
```


### [2026-09-05T17:51:37.982Z] TOOL RESULT

```
Exit code 1
799:a-vinn [?wbyn'; ’wbn. PT 1664] not gaining, not winning: 1. of a p.: defeated 4215; ~ kartan to do away with 48°; — 2. of things: fruitless, wasted, lost 6814-20, 6922.27; — [kē (for ka) x"àstak xYart i pitar kart u handoat, i dütakän yāft, avinn (*wbn) būt šut ... when the fortune has been consumed that his father made and
1412:dütak [dwtk'] family 212. 1322, 3726, 386, — Talm. lw. dywig’ ‘family’; NP didah.
2399:man [inscr. and Ps. LY, books shortened L, but LY-e man-ic]| cas. obl. of the pers. pron. lst p. sg. l. me, dir. and indir. obj.: ~ ozanend 275; ~ ... sahet it seems to me 3812-13; an (q. v.) ~...
2405:man [m’n', m’ny] house, palace P1:11. 384. 531. 587-592, 6114-28; ~ 4 rösn Garod- man, of Paradise 668; ~ 7 ätaxsän the fire-temple 667°; ~ katak i Zarer the family residence of Z. 263. — MPrs m?n; Paz. man; NP màn; MPrth m’nyst’n ‘dwelling-place, monastery; < Av. (1090 sgg.) nmäna-, domčina- through the in- fluence of mändan (g. v.) V. also mānēh, māntšn.
7121:düdah: dütak
(eval):1: == not found
```


## [2026-09-05T17:51:59.649Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"drang\\|dranj\\|drqj\\|drājah\\|dräjah\\|drajah\" BRT.txt | head -10"
}
```


### [2026-09-05T17:51:59.699Z] TOOL RESULT

```
3845:Zum  V.  drang:  —  Pü. :  i^!n  'a  afiar  getoel  .  . mihria  apar  dröiel,  erU :  tu  drdy  gmoel.  — ■)  zBild.  vgl.  asratim,
4190:•  '].  a-ohvä-,  g.  a-hvä-"  f.  i)  'Antrieb des  Willens,  Schaffensdrang,  Lebenskraft' : pairika  yä  duzyäirya  vlspahe  atiksui  .  . ' faröit pairi'in^misA.)  anhvqm  avaAisiiyät\ (sd.)  Yt.Ä54;  —  ava  m!  3zis  .  .  par5it\ fairrbnpm  (sd.)  arihvqm  ava.d}nnqn  sada- 1 yäfi  (sd.)  V.  i5. 19.  2)  'Antrieb  derl Seele,  innerlicher  — ,  Gemütsdrang,  Ge-j müt'"':  kal..*manS  asti  vT/aymii'tfm{s±) anhvqm  vjmar3zist?m  (sd.)  VL  /.  2 ;  —  ' virtzvatca  (sd.)  mat^  vansvatica  attuAa  j 'W.  62,10;  —  ye  kvam  ankvam  yaozdaite\ humatsilia  .  .  V.  ^.2i^>;  si  *PÜZ.,  lO.  19  I PüZ.;  —  dusx'arpnä  . .  asH5  asti  auuhaya  \ (LS.)  ".  .  ist  unfroh  in  seinem  Gemüt"  j YLJO.105;  —  aibl  ahväha  daxst^m  dilvOi\ (sd.)  Y.5/,9;  —  yatära  vä  dim  paurva frayasäiti  fraor^t  fraxsni  avi  manö  (sd.) zrazdälöii  ar^huyal*^  (oder  avuhyat)  i>  haca ". .  gern  in  sorglichem  Sinn  aus  gläubigem Gemüt"  Yt  /o.  9;  —  fora  vi  räki  am?sä spmtn  yasmmcä  rahmtmcä  firä  mana»hä ..  vaiaahä  ..  syat>^anä  ..  dw^iy«  (IS.) » Y.7/.18.
4289:Zorn  V.  drang-,    %    SOg.  8.   —    VgL  ananoi.- dtuila:  i
4575:•  j.  'an'tara-  Adj.  'der  innere,  innen  be- findlich': 'r^m  ür^Mfii  nmanahe  "ins  Innere des  Hauses"  V.6'.43;  —  'rat  W.  2.^0 PüZ.  a)  'rat  naimax  'innerhalb',  mit folg.  1)  Gen.,  z)  Lok.,  3)  Instr.,  4)  Akk., uzw.  a)  räumlich,  b)  zeitlich:"  1  a)  a'  n- hsirake  N.  Go;  104';  —  *a'  n°  *yujyastHs N.  -ji  T'*j  —  a'  W  aEi3.drajahyehe  N. Ii()',  —  a'  n°  '^rigämyt/ie  N. 65.  1  b)  a- II'  tiava.xsaparahe  V.  5. 43.  !  a)  a'  11° barj''irisi'a  y.^.^i.  3  a)  a'  n'  brrat.- byqm  V.  Ä41,  42,  g.  15,  16.  4  a)  a' tr  aSe  pa>a  "auf  diesen  Wegen"  V.  8. 104.  4b)  a°  11°  triilzär.ljaAlm'V.^.^y, —  a-  n' yanJräßV.O.a,  3,  7.77.  Tai fialinät  N.^.^3).  Ta  N.JOi(?);  —  'nm N.pj(?).
4640:"■  alte  pa~ia  "auf  diesen  Wegen"  V.  8. 04.  4b)  a-  11°  mäzdräjahlm\.^.4y, -  a'  n' yarp.drajö'W.0.3,  3,  7.77.  "rüi iialmäi  ii.g43>.  °ra  N.  707(?);  —  'riin N.p/(?).
4791:mit  antarp,  pairi  und  ava  'umstellend dazwischen  treten':  yai  titarat  anrö  main- yuf  dähltn  .  .  aiahe  antan  pairi.avail^m (3DPrA.) '"  vohuca  manO  atarsca  "als  an- drang AM.  gegen  die  Schöpfung  . .,  da traten  schützend  dazwischen,."  yt./j.??.
4888:•  j.  ayarv.dräjah-  n.  Dauer  eines  Tages': *;irr  vä  äzaili  (sd.)  'jS  vä  vaslryll  (sd.) "(so)  soll  man  ihm  (als  Strafe)  drei  (mit der  Peitsche)  diktiren  oder  einen  Tag  lang Feldarbeit"  N.  42,  *43  '>,  6g,  83,  loff;  6g.
6993:drang-  V.  ('festhalten')  'an':  ydi  ä  vanhsus mananAs  didray%S.duy?  Y.  4S.  7.  b)  un- räumlich,  zur  Angabe  a)  des  Mittels  'mit- telst, durch,  kraft':  ys  zaotä  aSä  imüS hvS "mait^Sui  3  vahistat  kayä  (sd.)  , .  västrya ^-  JJ'6;  —  fnasdä  dadat  ,  .  Aaurvats  ,  . bärßis  a  osaAyäca  j^apai^yaj (sd.)  ..  sars \. 31.21.  ß)  der  Veranlassung 'wegen, (ziun  Dank,  in  Vergeltung)  für  — ':  gavSi ärdis'isA.)  *a  unäa  (sd.)  "> . .  ys  is
7233:drang'  V.  ('festhalten')  'an':  ysi  a  varshSus manaahS  didrayzS.duy!  Y.  4Ä  7.  b)  un- räumlich, zur  Angabe  a)  des  Mittels  'mit- telst, durch,  kraft':  yS  taots  as3  »rtzüs  hvS *mainySus  3  vaAist^i  kay3  (sd.) , .  v3stry3 ^■33-6;  —  masdh  dadät  .  .  haurvatö  .  . bßteis  ä  asa^alS  :x^3paüy3j (sd.)  ..  sarff \. 31. 21.  ß)  der  Veranlassung 'wegen, (zum  Dank,  in  Vergeltung)  für  — ':  gavSi 3rBii(sd.)  *ä  sindä (sd.)"'>  . .  yS  tlsSnghB.. V.  5/.  14;  '''4'-*';  —  väahius  as3  haozakw3t (sd.)  ä  manaahs  Y.^^j.g.  l)  des  Be- treffs S'on  wegen':  tat  '^wä  pansa  . . tiitnatahB  ä  ya'^a  tuinS  (sd.)  x^mävatS  Y. 44.1.  5)  akmat  *a  adv.-artige  Verb., sbes,  b)  '(bis)  hin  zu  — ,  usque  ad  — '; a)  räumlich:  /rasa  frayoit..a  zanga^byas- Hi  äps  a  inubyascii  V.  6.2T,  27';  —  astit 3  irtzäs  (sd.)  pa'iiS  \.33.$.  a.)  a  mit Abi.  und  mit  Akk.  nebeneinander:  pa'i'3 ■  ,  yJ  asti  razistö  ä  aiat  vakist»mca  ahum \.6S.\i.         ß)  blosser  Akk.  und  ä  mit
8063:•  g-,  j.  isya-  Adj.  (fem.  "yä-)  i)  'erwünscht; begehrenswert':  kä  %wsi  asa  äkä  (sd.) andrang  'yl  Y.4S.%;  —  asahyä  >wj.i  (sd.) aslm  yqm  'yqm  "den Preis ..,  den  begehrens- werten, welchen  . ."  Y.54.r._  2)  von Personen  'lieb,  traut':  b?rfx<iqm  nwi  .  . daldöist  (sd.)  k}krp7m  damaysi  vauhuyäi yqm  Asi  'yqm''>  dälB  x/ayqs  mazdä  ahurB . .  äzdyäi  (sd.)  "den  .  ■  Leib  der  lieben (Jungfrau)  .  .,  welcher  der  Herrscher MAh.  es  gewähre  für  ihr  gutes  Ich  .  . zu  gelangen"  Y.5^.17;  —  hyat  *aS>ia>ihz dngvats  S»äna  °y}ng  avAayS  (sd.)  Y.js, 16.  a)  insbes,  von  'airyaman-  (sd.): il  airySmä  (sd.)  "yö  rafooräi  jatitü  Y.  ^4- 1;  V.  22.9,  19,  20,  a)  mit  'airyamati- (sd.,  auch  fdSt):  mryamamm  'slm  Vr,  2. 10;  usw.;  —  airyamattö  °ye/ie  Vr.  j.8;  usw.
```


## [2026-09-05T17:52:00.873Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN diraz ==\"; grep -n \"diräz\\|diraz\\|dirang\\|dēr\\b\\|dir 'spät'\\|dēr \" HRN.txt | head -20"
}
```


### [2026-09-05T17:52:00.933Z] TOOL RESULT

```
== HRN diraz ==
4898:547. diräz 'lang, diräza; vergl. direng.
```


## [2026-09-05T17:52:11.594Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4890,4910p' HRN.txt; echo \"=== direng ===\"; grep -n \"direng\\|dirang\\|dêr\\|dër\\|dir,\\|dir '\" HRN.txt | head -20"
}
```


### [2026-09-05T17:52:11.659Z] TOOL RESULT

```
wie np. tä auch nicht aus päz. andak (s. No. 366)
Phlv. darhär? Vergl. Nöldeke, Kärnämak, 57 Note U
?) Arni. L^\ bar (Hübschmanp ZDMG. 35, 128),— 121 —
entstanden sein kann. Sollte nicht ebenfalls *(lvarain
die Urform zu der 'hinein, darin' sein? *(lraram *zur
Tür hin*, konnte sowohl 'hinein' wie 'hinaus* bedeuten ').
In Verbindung mit Verben, wie ämeden, bayistefi,
l/afte?i etc.
547. diräz 'lang, diräza; vergl. direng.
aw. drajah' 'Länge'; phlv. draj (vd. 5 (159) Gl.),
drajth^) (so ist wohl dränäT, wie immer geschrieben
ist, zu korrigiren, vergl. auch bei. dräj; phlv. -äi in
Abstracten wird immer -th zu lesen sein, vergl. masih
(AV.) gegen masai des P. Vend.^)).
kurd. dirlz; bei. drOj, n. draz, drazad, dräzT (84).
Hierher gehört auch np. der 'lange, spät, lang-
dauernd', denne, phlv. der, das nicht mit np. dar
zusammengeworfen werden darf (Geiger, Dialekt-
spaltung im BalüeT, S. 88), noch auch direkt ap. darga-
*lang', aw. dareya-, ai. dlrghä-, kurd. derg^ oss. d. t.
darg, af/. lärya gleichzusetzen ist, wie noch Geiger
=== direng ===
4898:547. diräz 'lang, diräza; vergl. direng.
```


## [2026-09-05T17:52:13.823Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4910,4945p' HRN.txt"
}
```


### [2026-09-05T17:52:13.868Z] TOOL RESULT

```
darg, af/. lärya gleichzusetzen ist, wie noch Geiger
unter bei. dBr (LW.) tut.
Anders Fr. Müller (WZKM. 5, 261); von den dort
angeführten Belegen für Ersatzdehnung mit e fallen
aber weg: phlv. kirn (siehe unter No. 865), np. phlv.
kisver (No. 858), np. tese (No. 408) — phlv. vskar
Jagd' gehört nicht zu np. bese — es bliebe also nur
np. bese, das wie np. -des (598) zu beurteilen ist.
548. dir ext *Baum'.
aw. ^dra^ta- etwa 'fest stehend* ; phlv. dra/t 'Baum'
(vd. 1 (34) Gl).
LW. arm. draxt 'Garten'.
bei. ver^l. druck, dräc, n. drask, darask 'J^aum* (82).
Fr. Müller (WZKM. 5, 261) irrt, denn ar. gh -{- t
müsste aw. zd (Bartholomae, Handbuch § 124,
*) Das Einfachste ist, mit Bartholomae (briefl. Mitteihing)
verschiedene Casus von dvar- anzunehmen: für bj den Ablativ, für a)
den Accusativ (Correoturnote).
*) Wo ein awestisches j hineingeraten ist,
') Vergl. Hörn, KZ. 32, 582 No. 8.— 122 —
Anm., Ar. Forsch. III, 22 Anm. 2) geben. Skr. djfdhä-
müsste also aw. *dereMa- entsprechen.
duriixs s. unter direfs (No. 553).
549. dei*:^, derze 'Naht', derzmän, demen, derzl (syr. LW.
pm), Käään Q.K. darzln 'Nadel' ').
g. dastmün, he-darze 'ich nähe*; Kjiö. hidastdn,
oadasten, vödastemän (S. 126).
aw. dereza- 'Fessel*, l/^rfar^-2f- 'festmachen'; ai. [y^darh-,
cte/fAöv/a-* befestigen', arm. (Zer/c/ifc 'Schneider (Schuster)*,
derjan 'Faden', handerj 'Kleid' (Hübschmann, No. 81).
oss. dares 'Kleid' (101).
Wahrscheinlich gehört np. enderz 'Rat, Ermahnung*
(phlv. andarj bezw. andarz) zu derselben Wurzel (mit
Praellx ham),
550. (lerd 'Schmerz'.
Wohl zu ai. 1 [/^dar- 'spalten, zerreissen, bersten
```


## [2026-09-05T17:52:28.072Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HUB ==\"; grep -n \"diräz\\|dirang\\|dûdmân\\|dûdman\\|dudman\\|mân 'Haus'\\|garôdmân\" HUB.txt | head -20; echo \"== IEC ==\"; grep -n \"dlongho\\|dolikho\\|dhrāgh\\|drāgh\" IEC.txt | head -10"
}
```


### [2026-09-05T17:52:28.136Z] TOOL RESULT

```
== HUB ==
== IEC ==
```


## [2026-09-05T17:52:29.483Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== AHD del ==\"; grep -n -i \"^del-\\|del-.*long\\|dlonghos\\|dlongho\" AHD_watkins1985.txt | head -10; echo \"== AHD dem ==\"; grep -n -i \"dem-.*house\\|domo-\\|dem- To build\" AHD_watkins1985.txt | head -10"
}
```


### [2026-09-05T17:52:29.559Z] TOOL RESULT

```
== AHD del ==
362:DECENT. 2. Suffixed (causative) o-grade form *dok-eye- in: a. Latin docére, to teach (< “to cause to accept”): DOCENT, DOCILE, DOCTOR, DOCTRINE, DOCUMENT; b. Greek dokein, to appear, seem, think (< “to cause to accept or be accepted”): DOGMA, (DOGMATIC); DOCETISM, DOXOLOGY, HETERODOX, ORTHODOX, PARADOX. 3. Suf- fixed form *dek-es- in: a. Latin decus, grace, ornament: (DECOR), DECORATE; b. Latin decor, seemliness, elegance, beauty: DECOROUS. 4. Suffixed form *dek-no- in Latin dignus, worthy, deserving, fitting: DAINTY, DEIGN, DIG- NITY; CONDIGN, DIGNIFY, DISDAIN, INDIGN, INDIGNANT, INDIGNATION. 5. Reduplicated form *di-dk-ske- in Latin discere, to learn: DISCIPLE, (DISCIPLINE). 6. Greek dekh- esthai, to accept: PANDECT, SYNECDOCHE. 7. Greek dok- os, beam, support: DIPLODOCUS. [Pok. 1. dek- 189.] dek-2. Referring to such things as a fringe, lock of hair, horsetail. 1. Suffixed o-grade form *dok-lo- in Germanic *taglaz in Old English teg(e)l, tail: TAIL!. 2. Perhaps Germanic *tag- in: a. Swedish tagg, prickle, akin to the Scandinavian source of Middle English tagge, pendent piece: TAG!; b. Middle High German zacke, nail (> German Zacken, point): SHAKO; Cc. Old French tache, fastening, nail: TACHE, TACK!. [Pok. 2. dek- 191.] dekm. Ten. I. Basic form *dekm. 1. Germanic *tehun in: a. Old English tien, ten: TEN; b. Old Norse an, ten (see oktd(u)). 2. Latin decem, ten: DECEMBER, DECEMVIR, DECI-, DECIMAL, DECIMATE, DECUPLE, DICKER, DIME; (DECENARY), DECENNIUM, DECUSSATE, DOZEN, DUODECI- MAL, OCTODECIMO, SEXTODECIMO. 3. Irregular Latin distributive dani, by tens, ten each (formed by analogy with néni, nine each): (DENARIUS), DENARY, (DENIER?). 4. Greek deka, ten: DEAN, DECA-, DECADE, (DECANAL), (DOYEN); DECAGON, DODECAGON. II. Extended form *“dekmt- in Germanic *-tig in Old English -tg, ten (see dwo-). III. Ordinal number *dekmto- in Germanic *te- guntha- in Old English teogotha, téotha, tenth: TENTH, (TITHE). IV. Suffixed zero-grade form *-dkm-ta, reduced to -kmtd, and lengthened o-grade form *-dk6m-ta, re- duced to *-kontd. 1. Latin -gintd, ten times: NONAGE- NARIAN, OCTOGENARIAN, SEPTUAGINT, SEXAGENARY. 2. Greek *-konta, ten times: PENTECOST. V. Suffixed zero-grade form *dkm-tom, hundred, reduced to kmtom. 1. Germanic *hundam, hundred, in Old English hundred, hundred (-red, from Germanic *radam, number; see ar-): HUNDRED. 2. Germanic *thiis-hundi, “swollen hundred,” thousand (see teue-). 3. Latin centum, hundred: CENT, CENTAL, CENTAVO, (CENTENARIAN), CENTENARY, CEN- TESIMAL, CENTI-, CENTIME, (CENTNER), CENTUM, CEN- TURY; CENTENNIAL, PER CENT, QUATROCENTO, SEICENTO, (SEN!), (SEN2), (SENITI), SEXCENTENARY, TRE- CENTO. 4. Greek hekaton, a hundred (? dissimilated from *hem-katon, one hundred; see sem-'): HECATOMB, HECTO-. 5. Avestan satam, hundred: SATEM. See also compound root wikmti. [Pok. dekm 191.] deks-. Right (opposite left); hence, with an eastward orientation, south. Suffixed form *deks(i)-tero- in Latin dexter, right, on the right side: DESTRIER, DEXTER, DEXTERITY, DEXTRO-; AMBIDEXTROUS. Compare ner-'. [In Pok. 1. dek- 189.] del-'. Long. Probably extended and suffixed zero-grade form *dlon-gho-. 1.Germanic *langaz, long, in: a. Old English lang, long, long (comparative lengra): LINGER, LoNG!; b. Old High German lang (> German Jang), long: LANGLAUF; C. Old English denominative langian, to grow longer, yearn for: LONG?; d. Latin compound Lon- gobardus, Langobardus (with Germanic ethnic name *Bardi): LOMBARD. 2. Germanic abstract noun */lang- ithé in: a. Old English lengthu, length: LENGTH; b. West Germanic */angitinaz, lengthening of day, in Old English lengten, lencten, spring, Lent: Lent; ¢. Dutch lenghe, linghe, “long one,” akin to the Low German source of Middle English lenge, ling, ling: LING}. 3. Latin longus (> French long), long: LONGERON, LONGITUDE; ELOIGN, ELONGATE, LONGEVITY, LUNGE, OBLONG, PROLONG, PUR-
1452:ELLIPSIS leikw- ELM el-2 ELOCUTION tolkw- ELODEA sel-es- ELOIGN del-1 ELONGATE del-1 ELOPE klou-
1761:-LoGY leg-', sleu- LOIN lendh-1 LOITER leud- LOLL 1[a- LOMBARD del-1 LOMENT leu(@)- LONE oi-no- LONELY oi-no- LONG! del-1 LONG? del-1 LONGANIMITY ane- LONGERON del-1 LONGEVITY aiw-, del-1 LONGICORN ker-1 LONGITUDE del-1 LOON! [a-
== AHD dem ==
364:LOIN. 4. Possibly suffixed variant *dlo-gho- in Greek dolikhos, long: DOLICHOCEPHALIC, DOLICHOCRANIAL. [Pok. 5. del- 196.] del-2. To recount, count. 1. Germanic *taljan in Old English tellan, to count, recount: TELL. 2. Germanic *tal6é in: a. Old English talu, story: TALE; b. Middle Dutch dle, speech, language: TAAL. 3. Old English denominative talian, to tell, relate, probably akin to the source of Middle English talken, to talk: TALK. 4. Per- haps Greek dolos, ruse, snare: DOLERITE. [Pok. 1. del- 193.] del-3. To split, carve, cut. 1. Suffixed form *del-to- in Germanic *teldam, “thing spread out,” in Old English teld, awning, tent: TILT?. 2. Germanic extended form *telg- in Old English telgor, telgra, twig, branch: TILLER’. 3. Perhaps o-grade form *dol-é- in Latin dolére, to suffer (? < “to be beaten”): DOLE?, DOLOR; CONDOLE, INDO- LENT. 4. Suffixed o-grade form *dold-dhraé in Latin dolabra, a heavy chopping tool (< doldre, to chisel, hew): DOLABRIFORM. [Pok. 3. del- 194.] del-*. To drip. Perhaps suffixed (stative) o-grade form *dol- in Germanic *talgaz in Middle Low German falg, talch, tallow (< “dripping fat”), perhaps akin to the source of Middle English talow, tallow: TALLOw. [Pok. 4. del- 196.] deme-'. Also dem-. House, household. 1. Suffixed re- duced o-grade form *dom-o-, dom-u-, house, in: a. Latin domus, house: DOME, DOMESTIC, DOMICILE; MAJOR- DOMO; b. suffixed form *dom-o-no- in Latin dominus, master of a household (feminine domina > Old French dame, lady): DAME, DAN?, DANGER, DoM, DOMAIN, DOMI- NATE, DOMINICAL, DOMINIE, DOMINION, DOMINO}, (DOM- INO2), DUENNA, DUNGEON; (MADAM), MADAME, MADEMOISELLE, MADONNA, PREDOMINATE. 2. Com- pound *dems-pot-, “house-master” (*-pot-, powerful; see poti-), in Greek despotés, master, lord: DESPOT. 3. Root form *dem()-, to build (possibly a separate root), in: a. Germanic *timram in Old English timber, building material, lumber: TIMBER; b. Germanic *tumfté in Old Norse topt, homestead: Torr. [Pok. dem- 198.] deme-2. To constrain, force, especially to break in (horses). 1. Suffixed o-grade form *dom-o- in Germanic *tamaz in Old English tam, domesticated: TAME. 2. O-grade form *doma- in Latin domdre, to tame, sub- due: DAUNT; INDOMITABLE. 3. Zero-grade form *dmo- in Greek daman, to tame (> adamas, unconquerable): ADAMANT, DIAMOND. [Pok. (dema-), doma- 199.] denk-. To bite. 1. Germanic *tanhuz in Old English toh, tenacious, sticky (< “holding fast”): TOUGH. 2. Germanic *tanguz in Old English tang(e), tong(e), pincers, tongs: TONGS. 3. Germanic *tang- in Old Norse tangi, a point, sting, akin to the Scandinavian source of Middle English tonge, tange, point, tang: TANG!. 4, Germanic *teng- in Old High German zinko, spike, prong: z1Nc. [Pok. denk- 201.) dens-'. To use mental force. Reduplicated and suffixed zero-grade form *di-dns-sko- in Greek didaskein, to teach: pipactic. [Pok. 1. dens- 201.] dens-2. Dense, thick. 1. Suffixed form *dens-o- or *dns-o- in Latin dénsus, thick: DENSE; CONDENSE. 2. Suffixed zero-grade form *dns-u- in Greek dasus, hairy, shaggy: DASYURE. [Pok. 2. dens- 202.] dent-. Tooth. (Originally participle of ed- in the earlier meaning “to bite.”) 1. O-grade form *dont- in Germanic *tanthuz in Old English toth, tooth: TOOTH. 2. Zero-grade form *dné- perhaps in Germanic *tunth-sk- in Old English tisc, tix, canine tooth: TUSK. 3. Full-grade form *dent- in Latin déns (stem dent-), tooth: DENTAL, DENTATE, DENTI-, DENTICLE; (BIDEN- TATE), DANDELION, EDENTATE, INDENT!, (INDENTURE), TRIDENT. 4. O-grade variant form *(o)dont- in Greek odén, odous, tooth: -ODON, -ODONT, ODONTO-; CERATO- Dus. [In Pok. ed- 287.] deph-. To stamp. 1. Suffixed form *deph-s-ter- in Greek
```


## [2026-09-05T17:52:52.728Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o \"BELONG [a-z-]*\\|ALONG [a-z-]*\\|CONDOMINIUM [a-z-]*\\|TIMBER [a-z-]*\\|MADONNA [a-z-]*\\|DOME [a-z-]*\\|MADAM [a-z-]*\\|DOMESTIC [a-z-]*\\|DANGER [a-z-]*\\|DUNGEON [a-z-]*\\|OBLONG [a-z-]*\\|PROLONG [a-z-]*\" AHD_watkins1985.txt | sort -u | head -30"
}
```


### [2026-09-05T17:52:52.782Z] TOOL RESULT

```
ALONG 
DANGER deme-
DOME deme-
DOMESTIC deme-
DUNGEON deme-
MADAM deme-
MADONNA deme-
OBLONG del-
PROLONG del-
TIMBER deme-
```


## [2026-09-05T17:53:00.298Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== SYN long ==\"; grep -n \"dirghá\\|dirgha\\|darəγa\\|daroya\\|dargam\\|longus.*IE\\|12\\.57\" SYN.txt | head -10; echo \"== SYN house ==\"; grep -n \"nmāna\\|nmana\\|dəmāna\\|demana\\|domus.*dominus\\|7\\.12\" SYN.txt | head -10"
}
```


### [2026-09-05T17:53:00.365Z] TOOL RESULT

```
== SYN long ==
5653:Rum. obraz, fr. Slavic, ChSl. obrazit ‘form, shape, image’ (12.57), SCr. obraz ‘cheek’, ete. Tiktin 1072 f.
18925:W. dal, dala, Br. dere’hel (for *delc’hel, ef. pple. dale’het) : Goth. tulgus ‘firm’, OS tulgo ‘very’, Grk. Godtxés, Skt. dirgha-, etc. ‘long’ (12.57). (Cf. NHG gelangen ‘reach, attain’ : lang ‘long’, and NE long for.) Walde-P. 1.818. Peder- sen 1.106.
21176:CHAPTER 12 spATIAL RE b) 12.51 41 Puace (S- 12.52 fa. Por (Place, Seb “ae 12.58 013. 51 12.54 yi Lie ae 12.55 ois Stan (VD: ae 12.56 yo16 REMAIN, uaa Pere) 12.57 in17 pees 12.58 12.18 Lea : 12.59 1919 Quiet (adi) ie ; : 991 COLLECT, GATHER . ms 12.62 122 Jow, UNITE ake 1293 SEPARATE (vb-) ; 12232 DiviDE 12.64 1224 Oren (vb.) 12.65 1225 Snur, CLosE (vb.) 12.66 12.26 Cover (vb.) 12.67 1227 Hin, ConcesL 12.68 1231 Hicw 12.71 1232 Low 12.72 1233 Tor 12.73 1234 Borrot 12.74 1235 Eyp 12.75 ae Por 12.76 ee 12.77 12.36 Stop 237 Mux (adj.) Teale 12.38 CENTER 12.81 12, < 78 Ricur (adj; vs. Left) yore aa ler (adj. vs, Right) 12.83 nay Aoi (adv) 12.84 pas oe adv.) 12.85 45 Easn 9 12.46 Wesr 12.91 247 Nonny 12.92 248 Sonne 12.93 12.94 829
22234:6. ChSl. daleée, SCr. daleko, etc., general Slavic, fr. adj. forms ChSl. da- lektt, SCr. dalek, etc., beside ChSl. dalja in vt dalje ‘far’, prob. : ChSl. dligu, Skt. dirgha- ‘long’ (12.57). Berneker 177. Otherwise Zubaty, l.c., and Briick- ner 84.
22465:masah- ‘length, size’, and mas- ong’ . Grk. paxpés ‘long’ (12.57). Walde-p. 2.223. Barth. 1154 ff.
22498:12.57 Grk. paxpés, dodArxds Goth. laggs NG paxpés, naxpbs ON langr Lat. longus Dan. lang It. lungo Sw. lang Fy. long OE long Sp. largo ME long Rum. lung NE long Tr. cian, long, fota Du. lang Nir. fada OHG lang W. hir, maith MHG lance Br. hir NHG lang
22501:Grk. dod:xés, poet. except in sb. 66d.- xos ‘the long course’, cf. also évdedexis ‘perpetual’; ChSI. dligit, SCr. dug, etc., general Slavic; Skt. dirgha-, Av. daraga-, OPers. darga-; Baltic with loss of d-, Lith. ilgas (OPruss. ilgi, ilga adv., Lett. ilgs adj. of time only); Hitt. dalugaés (pl.), with sb. dalugasti ‘length’. ,
22522:1. Av. daraga-, above, 1. Skt. dirgha-s but superl. masista-,
24805:Boh. zdlouhavy, fr. dlouhavy ‘longish, dull’, fr. dlouhy ‘long’ (12.57).
24909:Boh. prodlévati (prodliti, dliti) : Chsl. prodtlits ‘prolong’, Russ. dlit’, prodlit’ ‘prolong’, etc. : ChSl. dligt, ete. ‘long’ (12.57). Berneker 252 f.
== SYN house ==
761:ON heimr ‘abode’ and the usual word for ‘world’ in the broadest sense : OE ham ‘home’, etc. (7.122).
3723:2. Lat. domus ‘house’ (7.12), also the immediate ‘family’.
3726:general for the latter, see 19.23. & Many of the words are those for puke or derivatives of them. Lat. our a ‘body of servants, house- tie ee the most widespread ee olkos, olxia ‘house’ (7.12), also Y, In the earliest quotations in
3731:3. Ir. teglach, NIr. teaglach, W. teulu, epds. of Ir. tech, W. ty ‘house’ (7.12), and Ir. sluag, W. lw ‘throng, army’, hence the ‘people of the house, house- hold’. Pedersen 1.84. Walde-P. 2.716.
3733:4, Goth. gards ‘house’ (7.12) renders Grk. ofxos also in the sense of ‘family’.
3736:6. ChSl. dom ‘house’ (7.12) renders otxos also in sense of ‘family’,
4093:Ay. gavo-sténa-, aspd-stana-, etc. (above, 1) for the large animals, also (nmanam) gavayam, lit. ‘(house) for ox- en’. For small animals, as sheep, pasus-hasta-, cpd. of pasu- ‘small cattle’ (8.15) and *hasta- fr. had- ‘sit’? = Skt. sad-. Cf. Vd. 15.23 ff., where the whole series occurs.
4624:in Varro, RR 2.7.12, 18 is ‘colt’ as dis- tinguished from ‘foal’ which is regularly pullus.
7174:OE héman: him ‘dwelling, home’ (7.122), hence orig. ‘take home’ then ‘cohabit’ with vulgar sense definitely prevailing over ‘marry’, just as in the current use of NE cohabit. Direct con- nection with the sense of the orig. root, namely ‘lie’ (as Walde-P. 1.359) is un- likely.
11508:ove 2s dwell, fr. OE dwellan pps) hinder, delay’ : refl. dveljask fies ‘well’ OHG twellan . *dwel- in n ‘be benumbed, torpid’, OE nee astray’, Goth. inal op *dhwel- in Grk. Godds ‘dirt’, c. The development is fr, ‘confuse, lead ee to duader, de- intr. delay, en Walde-P. 1.842 f. Fulk-Torp 169. NED s.v. dwell, vb. MB, NE live ‘live’ = ‘be alive’ (4.74), also ‘live’ = ‘dwell’ fr. the 13th cent. and now virtually displacing dwell in spoken use. 5, Lith. gyventi, Lett. dzivuot, Chsl. ili, SCr. Zinjeti, Russ. Zit’, all meaning ‘live’ = ‘be alive’ (4.74) and also ‘live’ = ‘dwell’, Lett. majudt, fr. maja ‘house’ (7.12). 6. OhSI, vifati (cf. Mt. 13. 32 of birds ‘lodging’), obitati (*obi-vitati), Russ. obitat’ ‘dyvell? (Russ. vitat! oan Boh. vila, Pol. witaé ‘welcome’) : Lith. Tete
```


## [2026-09-05T17:53:01.822Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== IEC ==\"; grep -n \"dlongho\\|dl̥ngho\\|dlnghos\\|domos\\|domus 'house'\\|dṓm\" IEC.txt | head -10; echo; grep -n \"delegh\\|dēlgh\\|dlogho\" IEC.txt | head"
}
```


### [2026-09-05T17:53:01.889Z] TOOL RESULT

```
== IEC ==
2365:doma1g (domaio, dmäið), eio ‘tame, domest- icate’. Cf. domos, us, dəm-, dm-. WP I, 788 Skt. damayāmi, pp. damitah; Oss. domin, dämun; Hitt. cf. damas(mi); Gk. damáo; Lat. domo, are; LOIr. damnaim; OBr. cf. domet- ic, adj. ‘tame’; cf. OBr. ar-domaul, id.; Br. don- va; W dofa; Cor. dova; OHG zamon; Go. ga- tamjan; OE temian; ON temja; cf. tamiór,
2383:domn- (1) ‘dwelling’. Cf. domos, us and demo. WP I, 787 Arm. (ambig. prob. *-ó-) tun, gs tan “house”, tanik ‘roof; Gk. dóma; Blg. dam (stable,
2386:domos, üs ‘building, house’. Cf. demo, dómn- (1) Skt. dámah, am Arm. tun, gs tan (fr. *domn-); Myc. domo-; Gk. dómos, beside domé “building, wall’; én-don “at home"; Lat. domus; Mir dom; W cf. dof ‘tame’; OHG zam; OE tam; ON tamr ‘tame’, cf. OE tama ‘tameness’; OCS domü, u-st.
15220:septm (sequdm-) ‘seven’. Cf. seque, du ‘with two extra'?. Cf. sequdm Skt. saptá; Av. hapta; Per. haft; Arm. eawt'n; Tokh. A spät B sukt; Hitt. cf. septamas 'se- venth'; Gk. heptá; Lat. septem; Olr. secht; Li. septyni, Latv. septini. Cf. Alb. shtatë; W saith; Br. seiz and Cor. seyth. The ordinal of type *septomos arises in Skt. saptamah; Hitt. septamas; Lat. septimus; OPr. septmas. Variants in Gk. hébdomos & Li. sekmas; OCS sedmyj
15221:sequdm, sequdomos 'seven; seventh'. Vari- ant of type septm, q. v. Olr. cf. secht, Ir. seacht; Go. sibun, OS sibun, OE seofon; MHG siben, seben and suben; Du. zeven; Lux. zivon; OFris. sigun, siugun; Fris. saun; OCS (and Com. Sl.) sedmt Cf. further Oss. avd; Tokh. spat, beside sáptànt
15231:‘seventh’; Tokh. B sukt. In all instances the labio-velar appears to be the more archaic phoneme, especially since it is echoed in Gk. hébdomos "7th? and in Li. sekmas, id.

2157:dé-leghó (delgh-?) “lay out; lay waste’. Cf. : next Lat. deleo; Olr. dílegim ‘destroy’; Ir. dílighim ‘swamp’; (cpds. dilg- in Olr.); OBr. cf. dilein: W dilain (cdestruction'; *waste); W diléu ‘obliterate; displace’; dilead (destruction, fr. *deleghot-) (uncertainly OE telgan ‘dye’ and MHG zëlge ‘tilth, fallow field’)
```


## [2026-09-05T17:53:09.004Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"\\[pdf page\" BQT_v2_pages.txt | head -5; echo ...; grep -c \"\" BQT_v2_pages.txt; echo ---; grep -n \"دراز\" BQT_v2_pages.txt | head -5"
}
```


### [2026-09-05T17:53:09.106Z] TOOL RESULT

```
...
41071
---
1388:           ‫دراز کند » و بعربی صرار گوبندش( ‪.‬‬         ‫مردم‬   ‫صف کشیدن‬        ‫و‬          ‫زدن‬   ‫ثالی » بمعنی حلقه‬
1724:‫دراز حوب‌الفرع را افع‬            ‫های‬
2069:                                                         ‫از جنس کلنگه ونزدیث مگردن او پرهای‌دراز‬
2918:                           ‫اتهای زبانك‌آن درازاست و دانه‌های آن بزبانجه چبیده است‪ .‬د‬
2993:‫رزه‬   ‫و کنانه از باره باره و ررە‬      ‫مشود‬   ‫فس‬       ‫باربکتر و دراز ترمیباشد و طعم آن تلخ است »‬
```


## [2026-09-05T17:53:12.782Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -30 BQT_v2_pages.txt | cat -A | head -5; echo ---; python3 -c \"\nt=open('BQT_v2_pages.txt',encoding='utf-8').read()\nprint('formfeeds',t.count('\\f'))\nimport re\nprint(re.findall(r'\\[.{0,20}page.{0,10}\\]',t)[:5])\nprint(repr(t[:300]))\n\""
}
```


### [2026-09-05T17:53:14.381Z] TOOL RESULT

```
^L                                         M-bM-^@M-+M-bM-^@M-*7M-bM-^@M-,M-bM-^@M-,$
$
                          M-bM-^@M-+M-XM-1M-YM-^FM-bM-^@M-*M-[M-3M-bM-^@M-,M-bM-^@M-,$
    M-bM-^@M-+M-YM-^FM-XM-'M-XM-*M-bM-^@M-,$
      M-bM-^@M-+M-XM-' M-YM-^EM-bM-^@M-,$
---
formfeeds 683
[]
'\x0c                                         \u202b\u202a7\u202c\u202c\n\n                          \u202bرن\u202a۳\u202c\u202c\n    \u202bنات\u202c\n      \u202bا م\u202c\n              \u202bلض\u200cبال \u202a ۰ ۲۶\u202cرک\u202c\n\u202b\u202a۱\u202c\u202c       \u202bاسا تعدولیدیارتم و\u202c\n                                     \u202b\u202a7\u202c\u202c\n\u202b\u202a ۰\u202cو زل رسوا »وا روون لات سا روصا مواقم\u202c      \u202bوتان\u202c\n\n                      \u202b\u202a۴2 ۱\u202c\u202c'
```


## [2026-09-05T17:53:17.964Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))['BQT']\nfor k,v in d.items(): print(k,':',str(v)[:800]); print()\n\""
}
```


### [2026-09-05T17:53:19.564Z] TOOL RESULT

```
title : Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)

kind : archive_djvu+local_scan_ocr

url : https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir 

lookup_hint : grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | Fo

local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/v

page_offset : vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with

covers_etymology : True

notes : Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs,

scans : [{'volume': '3', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', 'ocr_note': '689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py'}, {'volume': '4', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', 'first_printed': 1920, 'last_printed': 2475, 'pdf_offset': -1917, 'lang': 'fas', 'offset_note': 'printed = pdf+1917, chec

cites : page number, continuous across the five volumes of Mo'in's edition (1342/1963 = Amir Kabir 1362 reprint); Mo'in's etymological footnotes are the cited material
```


## [2026-09-05T17:53:28.837Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\nfor leaf in (285,286,287):\n    print('=== leaf',leaf,'(printed ~',leaf+543,')')\n    print(t[leaf][:2500])\nEOF"
}
```


### [2026-09-05T17:53:30.354Z] TOOL RESULT

```
=== leaf 285 (printed ~ 828 )
 ‫دحر‬                                                                                                  ‫‪۲‬‬     ‫ی‬


                                                 ‫ك لیس بروزن طبیب » هرچیزبکهآ ترا‬
‫دلیر فلكت هکنابه از کرکب عطارد‬                                                             ‫ارم کوفته باشاد ‪.‬‬
                                   ‫‪9 .‬‬   ‫ات‬             ‫‪۰‬‬        ‫‪‌ ۰‬‬       ‫ب‬
                                                      ‫برورن وزیر» مسشی‌وتوستده‬
                                                                                  ‫‪°‬‬
                                                                                           ‫=‬
                                                                                               ‫‪۱‬‬




‫ذلیقی » بروزن حقیقی » لوعی ازقماش‬
                    ‫ناشن درلپایت لطات ‪. ۴‬‬
                                                  ‫د لسر ستان؟ ‪ -‬بمعنی دبتان است که‬
                                                  ‫مکب خاله باشد ‪ - ۴‬و بعضی گویند دفترخانه‬


                                         ‫بیان سوم‬

                   ‫بر دو لفت‬      ‫مشتمل‬        ‫در دال بی نقطه ‪ ۲‬جم‬


‫د جر = بفتح اول و کر الی و سکون‬                   ‫کج ‪ -‬بضماول وسکون الی» هرجیز که‬
‫رای قرشت ‪ ۰‬غله‌است که برا لوینا گویند ‪.۷‬‬          ‫وامثال آن مالیده شده‬           ‫وعل‬       ‫وشر‬     ‫دوشاب‬   ‫درآن‬


‫استوآ بی که وبرا درآن‌پشته‬   ‫وآن سر د وخنك‬            ‫باشد و بر دست وپا بجسبد ‪ -‬ویفتح اول درءربی‬
       ‫باشند حیض براند ‪ ۰‬کوبند عربی است ‪۰‬‬                                      ‫مرغ صحرایی راکوبند ‪. ۵‬‬




  ‫‪ - ۱‬قی‪:‬یارسی باستان‪,‬کلمامتمار)_ ‪( 11‬خط)؛ پرا کرت ‪( 1۳11-* 1014 -‬کتیبه‬
  ‫های آشوک) ؛ پهلوی ‪hîrîp(i) ۰ ۲1۳140 . ۲۵۷1۳00‬‏ ‪ d‬و ‪ ۲1۱4‬ر(کدتیبه ها) ارمنیع‬
 ‫ور‪ :‬هویشمان ‪ * 04۵‬لیر کت ‪ ۵‬و ‪.۵‬دائرة لمعارف اسلام ‪ .‬راجم برمشة‬                        ‫‏‪ dpir‬مشق ‪۰‬‬
                        ‫از‪ :‬دس (ه‪.‬م‪٣ ).‬‏ ستان (يوندمكان) ‪:‬‬             ‫‪۲‬‬               ‫‪۰‬‬    ‫دییی‪.‬را*‪ :‬دسان‬


  ‫‪ - ۴‬دیبرستان کنم در هیکل روم کنم آبین مطران را مطرا ‪«.‬خاقالی شروانی ‪۲۲٩‬‏ ‪.‬‬
 ‫‪ ۴‬اصل این نوع پارچه از دبیق ( با دبقا بقول حمزة‌بن حن و قل ياقوت از او)‬
   ‫آمده است وآن شپری‌بوده است درعصر‪:‬هپی صندوق‌ها کبشرادند وخلمت‌ها برآوردند ‪ :‬جامهای‬
  ‫دوخته و نا دوخته » ورسول برپای خاست» وهفت دواج بیرون گرفتند یکی از آن سياه و دمکر‬
 ‫© = باین محتی‬     ‫دیقی های بفدادی بفات تادر ملکانه ‪« ».‬تاریج هقی ص‪ ۷4‬متن وحاشیه» ‪.‬‬
 ‫درعربی بافته‌نشد ؛مصحف ”رج ن
=== leaf 286 (printed ~ 829 )
                                            ‫بیان جهارم‬



                      ‫* دځ بدفتح‌اول وسکون ثانی‪ .‬بمعنی | کشهراب انگوری باشد ‪.‬‬
‫انیت‬    ‫ع‬    ‫و‬     ‫ام ق‬           ‫دحتر‬              ‫خوب ولیکوباشد ‪ -‬وفوج صف را بیزکوبند ۔‬
 ‫وسره وخلاصة هرچیزهم‌هست ‪ -‬وضم اول بمعنی | که‌کنایه از شراب لمل باشد ‪ - ۵9‬و بمعنی‬
 ‫انگور ودانه انگورهم آمفه است که بعربی علب‬         ‫گاهی را‬        ‫دختر باشد ‪۴‬‬        ‫است که مخقف‬         ‫دخت‬

                             ‫| خواشد ‪.‬‬       ‫ر‬  ‫یآن‬  ‫صاز‬   ‫حد و‬ ‫نیز گویند که درمیان اب روی‬
 ‫د ختر رور گار ‪ -‬کنابه از حوارت‬        ‫ه‬ ‫ز‬ ‫ب‬ ‫ر‬ ‫خ‬ ‫ن‬ ‫ا‬ ‫د‬ ‫ب‬ ‫و‬ ‫د‬ ‫ن‬ ‫ی‬ ‫بافند آونرا درخراسان اوخ کو‬
                                 ‫کزار است ‪.‬‬
                                          ‫| رو‬        ‫آرنگه کنند؟ ‪-‬وبه‌منی لیبو باهم! مده‌است ‪/‬‬
‫بارت‬    ‫بتکده ‪.‬‬    ‫» بر وزن‬
                                     ‫‪۱‬‬
                               ‫دختره ‏‬
                                                     ‫وتهیررآسمانی س زراا نسزر کدوونند که تءنرششپیاابین ‪,‬باشد ‪.‬‬
                                                             ‫کر‬          ‫‪۱‬‬                   ‫ج‬
                                                    ‫= هم اول وسکون ثالی ونای‬                 ‫د حت‬
‫ودخت رکی ودوشیز گی باشلب ومهر برا نیزکوبند‬
                         ‫که بر که لهند ‪. ۷‬‬                             ‫قرشت » مخقف دختر است ‪#*.‬‬

 ‫ینری ‪٬‬بمعنی‏‬ ‫دختری ^ گبر‬
            ‫لوز‬                                    ‫از شراب لملی‬           ‫ااببه‬
                                                                              ‫کنفت‬
                                                                                 ‫‪-‬تر‬
                                                                                   ‫دخ‬
         ‫دختره باشد که دوشیز کی وبکارت است‬                                                              ‫باشف‬


 ‫جمی = بروزن خفتن» مخفف دوختن‬                       ‫دحتر حم = بمعنی دخترافتاب است‬

   ‫متعافب همی رسد دخ دخ ‪ ۰‬تزاریةپستانی ‪«.‬جهانگیری»‪.‬‬              ‫‪ - 0‬همچو امواج بحر لشکر شاه‬
                              ‫مصحف «رخ» ‏ روخ ‪.‬‬       ‫‪۴‬‬            ‫رك‪ :‬دخت ؛دختر ‪.‬‬             ‫‪۴‬‬
                                          ‫‪ - ۴‬بپلوی ‪txud‬‏ نیم رگ ‪ ۰۶‬ورك‪ :‬دختر ‪.‬‬
        ‫که دم وحمت ماکرد ز بند آزادت ‪.‬‬              ‫® ‪ -‬برسان بندگی دختر رز کو بدرآی‬
  ‫«حافط شبرازی ‪۵۱٩‬‏ ‪.‬‬
  ‫‪ - ۷‬امروز دختره ( از‪:‬‬                  ‫‪- ۱‬
=== leaf 287 (printed ~ 830 )
  ‫دخمه فروژه‬                                                                                         ‫‪۲۲۴‬‬


‫کتدااوروآغمازعامله بکیا‌باشد و‪-‬تبره وتازيك‬
                                         ‫اب‬                 ‫باشد ‪-‬وبمعنیاندوختن‌وجمم کردن‌هم‌هست ‪۴‬‬
                                        ‫را نیز گفته‌اند ‪۰‬‬                        ‫ودوشیدن‌را نکیوزبند ‪. ۱‬‬
‫دحم ‪ ۹‬بروزن زخم ‪ ۰‬سردابه‌ای که‬                              ‫دخقنكد ‪ ۴‬ه بروزن سوزنگر» دختر‬
                               ‫لهمل‪.‬‬         ‫مرده را دران‬   ‫ودختر زان آزشوهر‬      ‫شوهر باشد از زنی دیگر‬
                                                                                                       ‫وگ‬
 ‫د حمه = بروزن زخمه» بمعنی‌دخم‌است‬
‫که صردابة مر د گان‌باشد؛وصندوق‌موتی را گویند‬
                                                            ‫دخقه ‪ ۴‬ه بروزن کفته‪ .‬مخف دوخته‬

 ‫عموماً وکورخالاً کبرانرا خصوصاً ‪ -۷‬وآن‌چیز‬                 ‫است که خیاطت کرده‌شده باشد‪ -‬وبه‌عنی دوشنده‬
                                                                                                 ‫هما مده ار‬


            ‫میا ورد و آیرا بعر بی شعععه خوانند ‪۰‬‬            ‫دخدار » بفتح اول و دال بی‌نقطه بر‬
 ‫دخمه راندیان س کنابه آاسزمان‬                               ‫وزن دستار» چادرسیاه وسفیدبرا گویند که برروی‬
                        ‫‪۰‬‬      ‫‪.‬و‬   ‫ه‬    ‫‪۵‬‬     ‫‪۰‬‬



                                                     ‫ا‬
                                                            ‫تخت پوشند ؛ وبعضی گویند معرب تخت داراست‬
                                                                                ‫که جام خواب باشد ‪.‬‬
                            ‫ات که آسمان باشد ‪.‬‬              ‫‪ = °‬بقتح اول بروزن رخش ‪۰‬‬             ‫دحش‬




  ‫از‪ :‬وخت ‪+‬‬       ‫‪۴‬‬            ‫» دوختن‪.‬‬            ‫و‪:‬ختن‬
                                                       ‫دکه‬
                                                         ‫ال ر‬
                                                            ‫‪۴‬‬             ‫‪.‬‬    ‫دوخئن‬   ‫رکه‬   ‫=‬   ‫‪۱‬‬

                                                            ‫اندر ) فظدر يسرأندرء پدراندر و مادراندر ) ‪:‬‬


       ‫ن بدارا ‪.‬‬
               ‫تچو‬
                 ‫خهم‬
                   ‫درد‬
                     ‫با پسندر کینه دا‬                         ‫جز بمادندر نماند این جهان گړبه روی‬
  ‫رود کی‌سمرقندی( تصحیحعلامهدهشدا) ‪.‬‬
  ‫© ‪ -‬رکه‪ :‬اسشق وهوبشمان ‪.4۲۵‬بهلوی‬         ‫‪ - ۴‬اسم مفعول از «دختن
```


## [2026-09-05T17:53:38.167Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\nhits=[i for i,p in enumerate(t) if 'دراز' in p]\nprint(len(t), hits[:40])\nEOF"
}
```


### [2026-09-05T17:53:40.151Z] TOOL RESULT

```
684 [27, 32, 38, 52, 54, 73, 77, 105, 109, 127, 130, 151, 156, 157, 163, 174, 184, 185, 190, 191, 194, 224, 230, 260, 269, 272, 289, 290, 297, 301, 304, 316, 321, 322, 323, 343, 353, 371, 372, 382]
```


## [2026-09-05T17:53:49.304Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\nfor leaf in (289,290):\n    print('=== leaf',leaf)\n    print(t[leaf][:3000])\nEOF"
}
```


### [2026-09-05T17:53:50.938Z] TOOL RESULT

```
=== leaf 289
  ‫دراز دستی کردن‬
 ‫هابلای مشدد ودال ابجد‬
                     ‫دارذودا ت‬                         ‫هت بعنی بدروفاعل‌دریدتراهم میگوبند وقتی‬
‫بوار رسیده و زای هوز بکالشفیده ‪ ,‬کی را‬                 ‫که مر کب شود همجو پرده در ‪٩‬‏ ‪ -‬و لوعی از‬
‫تجربه و دانا و عاقل باشد‪ .‬که‬       ‫حهب‬
                                     ‫اک‬‫صبند‬
                                          ‫گو‬           ‫مرغ صحراییرا کوبند و آترا سحرور خوانند‬
‫اکر احیااً کاری ناصواب ازو سرزند اصلاح آن‬              ‫باسین وحا ورای بی‌نقطه بروزن فغفور ‪ -‬ویشهرا‬
‫را بدانتگ ی تواند کرد ‪ -‬وکسی را یز گوبند‬               ‫نگیوزیند که صربی بق خوانند ‪ -‬وسمعنی درون‬
 ‫کنه‌یجکنکیه‌ووصلبحدویراباهم کند تورآایعربی‬            ‫باشد که نقبض ببرون استت چنانکه گوبند ‪«۶‬در‬
                         ‫مزبل خوانند ‪.‬‬                 ‫>عنی بدرون خاله رفت ‪ - ۴‬و نام‬
                                                                                   ‫خانه رفت ی‬
                                                       ‫موه وئمردرختی است کهآ نراتوت سه کل کویند‬

 ‫وقلتبانرا گویند ‪ -‬ودرعربی دو کی باشد که بدان‬      ‫وبعربی ثمرةالملیق خوانند وربکه و ثمرآنرا با‬
                                    ‫بشم رندد ‪٩‬‏‬        ‫بهجموشاننه وبدان ریش رنگ کنند ‪ -‬وضم اول‬
                                                                          ‫درعربی بمعنی کوهرباشدگ ‪.‬‬
  ‫در ار ‪ = ۲‬پروزن نماز ‪ .‬ضقکيوتاه‬                      ‫وزن سراء نمعنی درای است‬        ‫کی‬        ‫‪5‬‬
                                          ‫باشد ‪.‬‬
                                                        ‫که زنگ وجری باشد؟ ‪ -‬و امر بداخل شدن‬
 ‫بر وزن سوادخان ‪.‬‬           ‫وران»‬
                                ‫خرا‬
                                  ‫د‬                                                        ‫هم هت‪٥‬‏ ن‬
                 ‫باینشداز ودستار خوانرا گونند‪۶ .‬‬
                                                       ‫فرو شدن = کنایه از ناود‬         ‫دراب‬
 ‫درار دستی کر دن «کنابه‌ازغارت‬                                            ‫شدن وهعدوم گردیدن باشد ‪۰‬‬



   ‫‪ - ۴‬حرف‌اضافه» کردی ‪ ( ۲29‬در ببرون ) ‪.‬بلوچیع())‬                   ‫‪.‬‬   ‫رکه‪ :‬دربدن‬    ‫‪-‬‬    ‫‪۱‬‬

  ‫‪ ( 5۲21‬درببرون » بهبیرون)» لانننی‪.]51۲0* ]5210‬پهلوی ‪«۰.۲20‬اسشق ‪. ۹4۵‬قس‪ :‬اندره‬                     ‫‪۴‬‬
   ‫‪« - ۴‬دره (جضم اول وتشدید دوم) بمعنی مروارید‬
       ‫وزن‌صرد و درات‌بطماست ‪« ».‬شرح فاموس» و دفرارستخضة‬
                                                                 ‫وجمع‌ان در بضم ودرربر‬          ‫ت‬
                                                                                                ‫گزر‬
                                                                                                  ‫ب‬
   ‫‪ = ۴‬درای(ه‪.‬م‪).‬مژ لف اخبارالصن والهنددر وصف‬                   ‫دوم هم 'مده ومفرد گرفته دده است‪.‬‬

    ‫مملکت صين (چين)آرد‪* :‬وفى کل مدينة شثی بدعی الدرا وهوجری على رأى ملك تلكالمدينة‪.‬‬
   ‫مربوط بخیط ماد على ظهر الطریق للمامة کافة و بن الملك و ينه حور من فرمخ فاا حرك‬
   ‫الخیط ا
=== leaf 290
‫سوم برس‬                                                                                              ‫هراز دم‬

                                                                     ‫‪-‬ستم وجور نمودن باشد ‪.‬‬
                                                                                          ‫کردن و‬
‫‪«,‬وآن زستتیی‬      ‫وزن ابارج» لرعی ازلبلاب است؟‬
                                                         ‫درار دم بضم‌دال دوم وسکون هیم»‬
                              ‫باشد کهبردرخت پیچد‪.‬‬        ‫سک کروابند وبتازی‌کلب خوالند ‪ -‬ومیمون ‪-‬‬
‫در افتادن ت کنانه‌ازخصومت وجنگه‬                                                      ‫وعقرب را کدفزته‌اند ‪.‬‬
                                ‫و تراع کردن باشد ‪.‬‬       ‫در ار دنبال = ینم دال‌دويم وسکون‬
‫‪ - ۴‬باسین بی قطه بر وزن‬             ‫درافی‬
                                                         ‫دون و بای ابجد بالف کشیده بلام زده ‪.‬کاو ‪-‬‬
‫بلعت اهل‌شام شفالو باشد» وآن‌مومایت‬            ‫حوادث؛‬
                                                                                       ‫واومش رگاویند ‪.‬‬
                                                                                                     ‫ک‬
                                                          ‫به ازنین‌زن چست‬
                                                                        ‫نیاره‬
                                                                            ‫کمش‬
                                                                              ‫در ار ش‬
‫درافق ‪ » ۳‬با فابروزن خلایق ‪.‬‬                                                                    ‫وچالاگ باشد ‪.‬‬
‫بمعنی درافی است که شفتالو باشد بلفت اهل‬                  ‫دنانه از شخصی است که‬
                                                                            ‫در از کار ک‬
                                                ‫شام ‪.‬‬
‫درافطی ت بفتح ارل و الی بالف‬                                   ‫باشد ومتکم بخنان لاف و گزاف کردد ‪.‬‬
‫و ضم طا و سکون‬        ‫وقاف سمحتالی رسیده‬       ‫کشده‬
                                                          ‫در ار فا ‪ -‬باون بروزن‌هزارپا‪.‬محل‬
‫سین بی‌نقطه » بیونانی‌بیخ فیلگوش باشد ‪ .‬وآن‬                                                 ‫درازیراگوبند ‪.‬‬
‫کلی است ازجنی سوسن وآ نرابعربی‌اصل‌اللوف‬
                                            ‫خوانند ‪.‬‬      ‫در از تقس هکنابه‌ازپر کوی وبرحرف‬
                                                                                                        ‫باشف ‪.‬‬

‫که آنرا بیونالی غالاغاطیتون خوانند » گووبند‬               ‫در آستی نکر دن ک=نانة از رات‬
                                                                         ‫کردن وملك خود داستن باشد ‪.‬‬

         ‫‪ _ ۷‬از ؛ دراز ‪ 4‬نا(پسوند ساختن اسم معنی ازصفت ) (لظیر‪ :‬تنگنا و تیزدا ) "‬
    ‫« دراسج » دوعی از لبلاب است و گوبند خندربلی است » «نحفةٌ نک کے‬                              ‫‪۴‬‬
 ‫درمتن کتاب مصذف بنعنی شفتالوکه بعربی خوخ‬                 ‫رقدکوهلفت‬
```


## [2026-09-05T17:53:55.129Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\nprint(t[288][:3500])\nEOF"
}
```


### [2026-09-05T17:53:56.881Z] TOOL RESULT

```
                                                       ‫يان بنحم‬

                    ‫بر دو لفت‬              ‫در دال بی‌نقطه بادال بی‌نقطه عفر‬



‫رانز گوند‪.‬‬      ‫وفلندر‬    ‫‪_۴‬‬       ‫جانوران‌درنده‌باشد‬   ‫که‬       ‫که جانور ان در نده باشدهمجو شبر و پلنگه‬         ‫گونند‬



‫وگ رکه ومانندآن ‪ - ۱‬ویبابان پرازشکار را نیز | ودرتر ککنیيزك را نیز کوبند که فرزندان کلان‬




   ‫در دال بی‌نقطه با رای بی‌نقطه مشتمل بریکصد ونود وپنج لفت و کنایت‬


 ‫مشمه ل بر صف‬      ‫هصست‬   ‫رردشت‬       ‫کتابی دراحکام ددن‬           ‫ثالی ‪ ۰‬در خانه‬   ‫»‪ -‬بفتح اول کون‬       ‫در‬



  ‫وسرای وامثال آن باشد وبعربی باب کویند ‪ ۴‬۔ | باب وآنرا «صد در نام‌نپاد‌اند ‪ -‬ونوع و جنس‬
 ‫ودره کوهرایز گفته‌الد‪ - 6‬وبمعتی کرت ومرتبه | را نیز گویند ‪ - ۷‬و بمعنی دربدن و پاره پاره‬
 ‫امر بر باره کردن هم‬           ‫و‬       ‫باشف‬    ‫کردن هم‬            ‫چنانکه‬    ‫‪ -‬وبایی که در کتابهامنوی ند‬          ‫همهت‬



    ‫‪ - ۱‬اوستا ‪( 2610124 -‬جانور وحشی)‪.‬پهلوی ‪.tad 64024 610۵1۰‬‏ «اسشقع‪4‬ه»‬
   ‫و گفت ‪ :‬مرا تشجیران و ددان بحکم اعتمادی‬                      ‫«رویاه بر حمدو له لام گفت ‪e‬‏‬        ‫«مناس ‪YT‬‏‬

   ‫ی‬    ‫‪5:۳‬‬   ‫ور‬    ‫ر کث‪ :‬دده‬        ‫رک‬            ‫‪۰‬‬    ‫‪۷:۰‬‬   ‫سند بادناه‬   ‫نزدىك تر فرستاده‌اند‪».‬‬   ‫وسفارت‬       ‫برمات‬



        ‫بی‬
         ‫اكك‬
           ‫نیز‬
             ‫غ کن‬
                ‫جشی‪.‬‬
                   ‫مرعکنیی‌جد پدری‌با مادری»خال (دائی) پبر» حبران وح‬
                                                                   ‫‪ - ۴‬دبرت‬
    ‫‪ - ۴‬پارسی باستان_ ‪( ۲3۷10‬در ‪.‬باب)‪ .‬اوستا‪ ۰ ۲2۷1 -‬پهلوی‬                                  ‫ور که ‪ :‬دادا ‪.‬‬         ‫‪۸‬‬
       ‫‪ ۳‬هندی باتان ‪ , 94۳1۷ ۰ ۲2۷‬ارمنی ‪( ۳۳1۱‬باب‪ .‬در) ‏ کردی ‪)red. ۲۵‬‏ „(‪îrad‬‬
       ‫افغانی ‪ ۰ ۲۵۷‬استی ‪. ۲2۷0‬وخی ‪۲20۰‬سر بکلی]‪ . 1۷11‬شفنی ‪ , ۲6۷۱. ۵۷14‬منجی ‪27021‬‬
   ‫سمنالی ولاسکردی ‪rab‬‏ «‬                  ‫‪ 3‬بارتولمه‪ ۷۰۲23۷0۰ ۹۹‬لیر گے بر‪ 3 » 6‬منای ‪۱‬‬                ‫»‪ 2‬اسشق ‪6 0‬‬
       ‫فنردییز‌ونطنزی ‪ ۳30‬برنی ‪٣‬ق‏‪0‬‬                     ‫‪.۲‬‬‫‪“3‬‏‬
                                                            ‫یص‪٩۹۸۱‬‬
                                                                 ‫ککے‪).‬‬
                                                                     ‫ل‪1‬ء‬
                                                                       ‫ک‌بی ‪3‬‬
                                                                            ‫شهمیرزادی ‪ . 81‬سرخه‬
                                                                                             ‫دک ‪۱ .‬ص‪٩ ۲٩۰۹‬‏ ‪:‬‬

                    ‫بی وسیلت گرد پیرامن ‪.‬‬                                  ‫درمیر و وزبر و سلطان را‬
       ‫هکلتان ‪. ۹۳۰‬‬
       ‫یز ‪ ۲۵34‬دربهلوی بهمتی باب و فصل کتاب آمده‌منای‬                      ‫‪٦‬‏‬          ‫رکه‪ :‬دره ‪۰‬‬     ‫‪- ۵‬‬

                     ‫‪ - ۷‬ه پنشتم و از هردری سخن در پیوستم ‪« ».‬کلتان*‪. 4‬‬                                      ‫‪.‬‬      ‫‪۱‬‬
```


## [2026-09-05T17:54:09.527Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\nfor leaf in range(288,302):\n    p=t[leaf]\n    lat=re.findall(r'[A-Za-zÀ-ɏ]{3,}', p)\n    if lat: print(leaf, lat[:25])\nEOF"
}
```


### [2026-09-05T17:54:11.222Z] TOOL RESULT

```
288 ['tad', 'red', 'îrad', 'rab']
289 ['zdread']
294 ['Art', 'orme', 'trad', 'drad']
295 ['darez', 'nah', 'jed', 'najrsd', 'dnamo', 'trad']
296 ['ithsrd', 'urd', 'ithsrd', 'avurd', 'tsürd', 'tsurd', 'tsurd', 'tsurud', 'sorod']
298 ['drafsh']
300 ['hãûgrid']
301 ['arêd', 'nÃmazZ', 'êhgarad', 'Henning', 'Central', 'Asian', 'Words', 'Philological', 'droftreH', 'yteicoS']
```


## [2026-09-05T17:54:23.195Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\nimport re\nfor leaf in range(296,306):\n    head=' '.join(t[leaf].split()[:12])\n    print(leaf, head)\nprint('---- search درنگ / دیر ----')\nfor i,p in enumerate(t):\n    if 'درنگ' in p and i>280 and i<330: print('درنگ leaf',i)\nfor i,p in enumerate(t):\n    if 'دیر' in p and i>290 and i<340: print('دیر leaf',i)\nEOF"
}
```


### [2026-09-05T17:54:26.139Z] TOOL RESULT

```
296 ‫درساره‬ ‫ونندرمتی هم هت ‪. ۴‬‬ ‫روزن کهواره ‪ .‬بہمنی درسار‬ ‫دمر‪-‬سپار‬
297 ‫‪ ۴۱۳‬بت‬ ‫هآمده استِ ؛ وباین معنی باشین قرشت نیز‬ ‫غدارل ‪
298 ‫‪-‬‬ ‫در غو رگی مویز شدن‬ ‫که آنجا شراب خوب میشود »
299 ‫رت‬ ‫بردن بکسی باشد ‪.‬‬ ‫درفشه = بم اول وثانی وسکون‌فاوفتح‬ ‫در
300 ‫رح‬ ‫ولام وسکون‌الی‬ ‫در لك ‪ = ۳‬تکراول‬ ‫در لك = بقتح
301 ‫دروا‬ ‫ب‪۱‬ح‬ ‫گونشد‪ -‬و نمعتی وقت‬ ‫‪ ۹۳‬وهللا کت راز‬ ‫ومحنت ‪6‬‬
302 ‫‪~A‬‬ ‫حره اج‬ ‫فام سلاطین وبزرگان هندوستان است ‪ -‬وبمعنی‬ ‫درست وتحتیق
303 ‫دروقیئون‬ ‫مرت‬ ‫میگشاید وبعربی مبضم خوانند ‪ ۴‬؛ وباین ممثی‬ ‫استغفار واز
304 ‫)‪“1‬‬ ‫دروك‬ ‫باشدا ‪ -‬ونام شهربست (‪ )۳‬درخراسان مابن مرو‬ ‫کوبند بونالی
305 ‫دره‬ ‫ز‪6‬ح‬ ‫بی‬ ‫کنابه ازشکم باشد © ‪ -‬و قوس قزح (‪-
---- search درنگ / دیر ----
درنگ leaf 301
دیر leaf 297
دیر leaf 301
دیر leaf 307
دیر leaf 308
دیر leaf 309
دیر leaf 322
دیر leaf 331
دیر leaf 332
```


## [2026-09-05T17:54:32.601Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\np=t[301]\nprint(p[-2200:])\nEOF"
}
```


### [2026-09-05T17:54:34.822Z] TOOL RESULT

```
و واو‬                          ‫در ند د بروزن سمند » بمعتی شکل‬
‫سردان و حیران‬
            ‫بالف کشیده » س رکشته و ک‬                      ‫ودمایل وصورت ومانندوسان‌باشد چتانکه گویند‬
‫باشد ‪ - ۸‬وسرنگونآو‪.‬خته ونگون وبا کونهرا‬                                  ‫فلك درند یعتی فلك سان و فلك مالند‬

‫یز کویند ‪- 4‬وچیزی‌ذرورقوحاجت ومابحتاجرا‬                   ‫در نگ = بکر اول بروزن فرنگ ‪۰‬‬
‫هم گفته‌اند که‌دروایست باشد® ‪-‬ونامفرشته‌است*‪۷‬‬              ‫صدایی‌باشد که اتزواختن ناقوس وتارسازوشکستن‬
‫کونایه ازهاروت وماررت همهت ‪ -۱۷‬وض‌اول‬                     ‫دلج‬       ‫و‬      ‫آن برآید ‪۴‬‬     ‫امثال‬   ‫و‬   ‫وآبگنه‬   ‫چینی‬




                                               ‫(‪ )۷‬چك‪ :‬زمائم ‪.‬‬                   ‫(‪ )۱‬چك‪ - :‬بی‌شقطه ‪.‬‬

  ‫در گت‬    ‫د بر ند(«‪.‬م‪۳ ).‬‬      ‫‪۳‬‬
                                                               ‫‏‪ - ١‬لفة بمعنی‌جابکه درم باشد‪.‬‬
   ‫‪ - ۱‬بباوی ‪80۵۲1‬‬                     ‫‪ ۵‬بانن حعنی «ریگ» انت‬                        ‫‪.‬‬   ‫اسم صوت‬   ‫‪_ ۴‬‬      ‫(«‪.‬م‪.).‬‬

  ‫( دراز ‪,‬آهسته) «مناس ‪ »۱۷۲:۲‬و‪arêd 8‬‏ «اونوالا ‪,nÃmazZ ۹۷۱‬‏ ‪:( 832۲61‬مان درز(‬
  ‫و ‪( 81۵۷1-802۲۵‬خداوند و صاحب زمان طویل ) » اوستا ‪êhgarad . (302۳09۷‬‏ _‬
  ‫«بارتولمه ‪« 1۹16‬نبر که › وأ‪( ۵92۲610۵۷۳22 - 20۵۳2‬زروان(زمان) یابدار)‪ .‬رك‪:‬‬
               ‫‪ Henning,‬ظ‪ .‬‏‪W.‬‬            ‫‏‪۵۷۲ Central Asian Words {¢Philological‬‬
   ‫‪.‬ص ‪droftreH 6491,‬‏ ‪.)yteicoS‬‬                   ‫ورك‪ . :‬دیرند ‪451 .‬‬
                       ‫رك‪ :‬اندروای ‪.‬‬       ‫‪۸‬‬            ‫ب‏دن (یسوند مصدری) ‪.‬‬
                                                                           ‫‪ ۷‬از‪ :‬درتك ‪٣‬‬
  ‫‪« -۶‬وا» نام فرشته (باد)‬                  ‫‏‪ - ٩‬رك‪ :‬الدربای‪ .‬اندربایستدربا دربای» درباست‪.‬‬
   ‫رك‪ :‬سار‬       ‫_‪١١‬‏ چون اروت وماروت طبق داستانما درچاه بایل‌مملفند ‏‬                            ‫امت ‪ .‬رك‪ :‬باد ‪.‬‬
                                       ‫تاهید با داستان خرداد و امرداد بقلم نگارنده ‪ ۰‬قهران ‪ .‬ص ‪. °۱‬‬

   ‫‪ #‬درو ‪ -‬یکس اول وفتح دوم ‪ ۱‬رك ‪ :‬درودن ] ‪ :‬چیدن له » بدرن‌علف و غلهٌ رسیده‬
                                                       ‫وبا لیم ری با دای وداسفاله‪ ,‬حصاد ‪.‬‬
```


## [2026-09-05T17:54:50.454Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la SNS*; echo ---; grep -n \"drang\\|dēr\\|dēr\\b\\|dūtak\\|mān\" SNS.txt | head -20"
}
```


### [2026-09-05T17:54:50.528Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 1292394 Sep  4 14:06 SNS_pages.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  325929 Sep  4 14:06 SNS.txt
---
10356:■ o^^l^^UjJ^ :drang X zainanlg: 5,^-,^ 1A 
17667:( ( _ r .ii.t$l t -,bSjv*j1 jjly. J . i ) «^U> .J^jJidrang: j^l 
17668:fl.£. Zae/mer, BSOS-& >j j {AiWb . 772) drang-:£- 
29304:drang- 324/7 
31077:vadrang 259/19 
33230:drang 324/6
```


## [2026-09-05T17:54:56.701Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '17655,17680p' SNS.txt"
}
```


### [2026-09-05T17:54:56.747Z] TOOL RESULT

```
TY1 






C^b^iA^^I^] *it?*-oij->:dron-I siganag:3V3«_j *>-» 

1/H^ '»>*«• *A*Jj* jttfjJd* o*>^ 

( ( _ r .ii.t$l t -,bSjv*j1 jjly. J . i ) «^U> .J^jJidrang: j^l 
fl.£. Zae/mer, BSOS-& >j j {AiWb . 772) drang-:£- 
• Yf/1Y^ IX, 1938 pp. 319 and 584 

•YY/YY^ ( y»V> *.^) r iL-0jjO:dr6d: *b* 

•M/1T^ _UP3 :^j .C *** a-VAjffrtji/ .-grlvag: >3*\ 

•olw i *'O lA *Ju J ( drigus : J^s) driyosan: / **-*Wi 
• ( -tj*- <s**J daryos : ^ X4tW>. 777)dri$u - zU 

. Xj« 4 ±>Jm 4jiK , jijjo : druvand:. J»^-» 
{Mir.Man.ll t 51\drvnd^L{AiWb. 783) drvant- : t-
```


## [2026-09-05T17:55:07.992Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"drang-  V\\.\\|drang- V\\.\\|didrag\\|didray\" BRT.txt | head; echo ===; grep -n \"festhalten\" BRT.txt | head -20"
}
```


### [2026-09-05T17:55:08.051Z] TOOL RESULT

```
Exit code 1
6993:drang-  V.  ('festhalten')  'an':  ydi  ä  vanhsus mananAs  didray%S.duy?  Y.  4S.  7.  b)  un- räumlich,  zur  Angabe  a)  des  Mittels  'mit- telst, durch,  kraft':  ys  zaotä  aSä  imüS hvS "mait^Sui  3  vahistat  kayä  (sd.)  , .  västrya ^-  JJ'6;  —  fnasdä  dadat  ,  .  Aaurvats  ,  . bärßis  a  osaAyäca  j^apai^yaj (sd.)  ..  sars \. 31.21.  ß)  der  Veranlassung 'wegen, (ziun  Dank,  in  Vergeltung)  für  — ':  gavSi ärdis'isA.)  *a  unäa  (sd.)  "> . .  ys  is
7233:drang'  V.  ('festhalten')  'an':  ysi  a  varshSus manaahS  didrayzS.duy!  Y.  4Ä  7.  b)  un- räumlich, zur  Angabe  a)  des  Mittels  'mit- telst, durch,  kraft':  yS  taots  as3  »rtzüs  hvS *mainySus  3  vaAist^i  kay3  (sd.) , .  v3stry3 ^■33-6;  —  masdh  dadät  .  .  haurvatö  .  . bßteis  ä  asa^alS  :x^3paüy3j (sd.)  ..  sarff \. 31. 21.  ß)  der  Veranlassung 'wegen, (zum  Dank,  in  Vergeltung)  für  — ':  gavSi 3rBii(sd.)  *ä  sindä (sd.)"'>  . .  yS  tlsSnghB.. V.  5/.  14;  '''4'-*';  —  väahius  as3  haozakw3t (sd.)  ä  manaahs  Y.^^j.g.  l)  des  Be- treffs S'on  wegen':  tat  '^wä  pansa  . . tiitnatahB  ä  ya'^a  tuinS  (sd.)  x^mävatS  Y. 44.1.  5)  akmat  *a  adv.-artige  Verb., sbes,  b)  '(bis)  hin  zu  — ,  usque  ad  — '; a)  räumlich:  /rasa  frayoit..a  zanga^byas- Hi  äps  a  inubyascii  V.  6.2T,  27';  —  astit 3  irtzäs  (sd.)  pa'iiS  \.33.$.  a.)  a  mit Abi.  und  mit  Akk.  nebeneinander:  pa'i'3 ■  ,  yJ  asti  razistö  ä  aiat  vakist»mca  ahum \.6S.\i.         ß)  blosser  Akk.  und  ä  mit
14068:•  j.,   g.    'drang-  V.   'firmare'.     Praes.
14075:•  j.  "drang-  V.  'auswendig  lernen'.  Praes, 7  i/iu/rJg-''<,  24  drmjaya-. — VVi^.draxta'.
(eval):1: == not found
```


## [2026-09-05T17:55:16.874Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \" 182/\\|182/\" SNS.txt | head -20; echo === ; grep -n \" 239/\\|239/\" SNS.txt | head -20"
}
```


### [2026-09-05T17:55:16.927Z] TOOL RESULT

```
Exit code 1
28380:slraz- 182/11 
28454:dlrgha- 182/14 
28547:navati-33/11-182/5 
29037:sarah- 182/11-231/4 
29325:navaiti- 33/11-182/5 
29582:dar3ja-/darga- 182/14 
31338:sakatOm 182/6 
31344:sar 182/10-230/18 
31371:sazSd 182/1 
32137:navad 33/11-182/4-3 
32791:girad 182/16-265/5 
32793:girand 182/20 
33155:dSr 182/13 
(eval):1: == not found
```


## [2026-09-05T17:55:22.921Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dlrgha\\|dirgha\\|dar3ja\\|dara3ja\\|dSr:\\|dSr :\" SNS.txt | head; echo ===; grep -n \"dlrgha-\\|darga-\" SNS.txt | head"
}
```


### [2026-09-05T17:55:22.974Z] TOOL RESULT

```
Exit code 1
7709:- J-L> ««oi^ <j'*** : burdSr : lo^p 
28454:dlrgha- 182/14 
29582:dar3ja-/darga- 182/14 
(eval):1: == not found
```


## [2026-09-05T17:55:25.605Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\npages=re.split(r'\\[pdf page (\\d+)\\]', t)\nprint(len(pages))\nprint(t[:300])\nEOF"
}
```


### [2026-09-05T17:55:27.465Z] TOOL RESULT

```
1
    A
>l»>'i




 O^t'

        /
« *>&
                              Shiraz University Publication




     A GLOSSARY OF
SAYIST NE SAYIST
 A pahlavi persian Glossary
             -




       and Six indexes

         '




                      By

        Mahmood Tavoossi




                 *
```


## [2026-09-05T17:55:31.043Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"darg\\|drgh\\|dirg\" SNS.txt | head -20"
}
```


### [2026-09-05T17:55:31.096Z] TOOL RESULT

```
6173:. n /vr*S .o^JJ-" 1 :handarg guftan: «*** ^ 
6258:• j«4il :andarg: •&«*• 
6261:. i,al I : handarz : £> ^ v i * l-handarz/handarg : ^ v 
11142:(/tiWfc. 693) darga/daraja^fc- 
17423:.^^bM^^ :dargah: <>«A 
29582:dar3ja-/darga- 182/14 
32649:handarg guftan 81/2 
32650:handarz/handarg 80/19 
33085:darg5h 321/14 
33918:andarg 80/16
```


## [2026-09-05T17:55:33.122Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11132,11150p' SNS.txt"
}
```


### [2026-09-05T17:55:33.185Z] TOOL RESULT

```
\o 



. W/ „«S WW. "36-37, sraoSo-carana- ,*- 

. ^ . it,. . tfVi" • •*** : detang : _ 

(/tiWfc. 693) darga/daraja^fc- 

iV i*s .^-^ - :d6rang zaraan! ** 

.^U :srQv: — J 1 **** 
. Wtrf ULito. 1642) . t U.^U:srvS-, S rO-=a- 

„ . . ;1 , ; A) *' : burd : YBLWN , t = J* « *" »*
```


## [2026-09-05T17:55:40.018Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"239/\" SNS.txt | head -20"
}
```


### [2026-09-05T17:55:40.066Z] TOOL RESULT

```
29168:raairya- 239/6 
29182:raarezaiti- 239/12 
29191:mara- 239/5 
29232:raojrna- 239/3 
29347:nmana- 239/21 
30073:m J n 239/21-252/18 
31624:rO n 239/1 
31990:mahraanih 239/14 
32302:maiisn 239/11 
32324:mar 239/4 
32326:raarlg 239/13 
32328:mar 1 sfibag 239/9
```


## [2026-09-05T17:55:43.169Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"nmana\\|nm5na\\|nmSna\" SNS.txt | head"
}
```


### [2026-09-05T17:55:43.274Z] TOOL RESULT

```
17590:{Mir. Man. gr'sm^n:^ (Atf/fc. 1090) *jU : nmana- 
29347:nmana- 239/21
```


## [2026-09-05T17:55:45.256Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '17580,17600p' SNS.txt"
}
```


### [2026-09-05T17:55:45.304Z] TOOL RESULT

```
gRM: ^«o o'jo-'i^j'^^y^U-.Jjjj :drOd: t°» 

drwd i^ (tfir. Wan. 11,51) drwd: ^U .c-l]^ :Jj) 

1A/1Y*-* {Mir. Man. 111,54) 



.tf'o> j>^«jl» '^jji^tW <J>jc «o^j/:gar5dman: t^V> 
djmana-+04£W>. 512) Vgar garS. damana- : t- 
{Mir. Man. gr'sm^n:^ (Atf/fc. 1090) *jU : nmana- 

-a/it^ -r/u^ -r/M grdm'n : >;t II, 49) 



rra 



(U^~l*b«,L*jlj
```


## [2026-09-05T17:55:53.356Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && grep -n \"گرزمان\\|گرسمان\\|گردمان\" BQT_v3_pages.txt | head -10"
}
```


### [2026-09-05T17:55:53.413Z] TOOL RESULT

```
42972:‏گردمانه ۴ = بکس اول ومیم‌بالف
44021:۴ ک رکر , ظ . از : 8870 (82۲پرستیدن) [فس: گرزمان ] دراصد ‎chy‏ نام ‎has‏
```


## [2026-09-05T17:55:56.542Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && awk 'NR>=44000 && NR<=44035' BQT_v3_pages.txt; echo \"---- page tag ----\"; awk 'NR<=44021 && /\\[pdf page/ {p=$0} END{}' BQT_v3_pages.txt; grep -n \"\\[pdf page\" BQT_v3_pages.txt | awk -F: '$1<44021' | tail -2"
}
```


### [2026-09-05T17:55:58.207Z] TOOL RESULT

```
‎UIT‏ رسمانی‌است که دروقت رشتن بردوثپیجد
‎Ques‏ تصیله خوانند ۷ .
گردی = ‎Jy) pn‏ وسکون ثانی‌وئاث
بتحتانی کشیده . نام یکی از خویشان افرسیاب
است که در کشتن ‎OS He‏ کرد و حیلها
انگیخت و او را کروی زره ليز کوبند ۸ ۰
گرو ین * = ‎IG‏ وفتح ثانی,
به‌عنی ایمان آوردن وسر باطاعت نهادن‌وپذبرفتن
و بردل محبت واطاعت شخصیراکره بستن باشد.
‎Soo”‏ اول و ‎GU‏ و ظهور ها »
معروفست اعم ازینکه دررسمان با درخت‌رامثال
آن و از جایبی بر آمده
باشد ویعربی عقد هگوبند ‎STS ۱٩‏
-وتخم خاری هم هت که
بدان پوست را دیاغت کنند ‎Ss‏
‏وآنرا بعربی قرط خوانند- ودلرا هم گفته‌اند که
عربان پال گویند - و بمشی مشکل هم بنظر

بچندین حرتش جای ی کرو کان .
امیرخسرو دهلوی «رشیدی» .

۴ ک رکر , ظ . از : 8870 (82۲پرستیدن) [فس: گرزمان ] دراصد ‎chy‏ نام ‎has‏
‏از دعاهای زرتشتیان» نام ۷۳« ک رکر» ونام۷ «کر و کر» آمده . رك : خرده اوستا . شهمرران .

‎oes‏ ۱۳۰۸ ص۳.
فرزند تو امروز ‎oy‏ جاهل و عاصی

‏فردات چه فرباد رسد پیش ‎IIS‏
‏« ناصرخروبلخی. دیوان ص۱۷۳*.

‏۴ - پهلوی ]8۲6 ( دسته , گروه ) ۰ ارمنی ع 8۳0 ( ملت » جمعیت ): بلوچی
1 , ایرالی باستان - ‎ogravathva‏ « تیب ‎oS‏ ص ‎at‏ » کردی ‎kuruh‏ (اجتماع اشضاس)

‏«ژابا صس ۳۳۱ .

‏۵ - قی :کلوله , غلوله . مخفف ‎OT‏ «کرهه ».
---- page tag ----
43874:[pdf page 599]
43972:[pdf page 600]
```


## [2026-09-05T17:56:07.423Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nimport re\nt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\nparts=re.split(r'\\[pdf page (\\d+)\\]', t)\nd={}\nfor i in range(1,len(parts),2):\n    d[int(parts[i])]=parts[i+1]\nfor p in (586,587,588):\n    print('==== pdf',p)\n    print(d.get(p,'')[:1800])\nEOF"
}
```


### [2026-09-05T17:56:08.958Z] TOOL RESULT

```
==== pdf 586

۱۷۹

گویند که برآن کوشت بیار باشد ۱ - و کنابه
از عیش ورفاهیت هم هست .

گر 990 = بکس اول وثالت,معروفت
"که اطراف ودور روباشد ۴ - و تبیحی را لیز
کوبند از مروارید کهزنان بجهت‌خوشآیند کی
ب رگرد روی خود بندند ۴ .

le ‏دابل - بش اول و کر‎ oP
‏کنابه از رستم زابلی است که رستم زال باشد.‎

گرد هرك - بنتح اول وکس ‎NE‏
‏وضم زای هوز ومیم ورای قرشت , کنابه ازسبزة
تورسته وخط لو ‎Sane‏ خوبان باشد .

گردش ۴ ‎ao‏ وزن ورزش ۰ بمعنی
کردیدن باشد که چرخ زدن است ‎٩‏ - وبمعنی
تفیبر هم هست همچنانکه رعش بمعنی تبدبل
است ‎٩‏

(۱) چش: یادشادان .
۱

دست‌بر رانش ‎pal‏ هشت زد ب رگردنم

<

و گر در رو

یعنی اطر اف چهره و

کر دکریبان

گرد شب » بفتح ‎Jol‏ ورابع .کنابه

از سیاهی شب است .

گر دشنده ۷ - بکس اولوفتح ‎Os‏
‏بروزن نیم خنده . حشرت الارض را گوبندیمنی
جانورانی که در زیر زمین خانه سازند .

گردد بکر اول بروزن خرسك .
مسف کرد باشد ۸ - ‎IT oy‏ را نیز کویند ۸ .
که خیم بز رکه مدور است ‎٩‏ ؛ و بعطی خيمةً
کوچکیرا گویند که خصوص‌پادشاه (۱)باشد۸ -
وحجله‌ای که ‎Com‏ عروس ‎DL‏ وبمعتی
‎A‏ وچیتان هم ‎ew‏ ونانی که درون آنرا
پراز حلوای ‎ad‏ ومفز بادام ویته و نغیره کنند
وپزند وآنرا درخرا-ان‌کنبه کویند۴٩- ‎Le gy‏
جمله هم ‎coe‏ پم ‎Moar‏ .
گرد گر ‎Vols‏ - بکس اول و کاف

- ران که پر از گوشت و کرد است :

این‌مثل با بادم آمدگردران با گردنت .
سوزنی سمرفندی «فرهنگک نظام»

راجم ‎Ser‏ «کرد ران با گردنت» رك : امثال وحکم دهخدا صس۱۷۹۰ ۰
‎(ss)‏

صورت .۰ ۴ -از: گرد رو (روی) ‎(jee)‏ .

۴ - ازگرد ( کردیدن) - ش ( پسوند اسم ممتر ) .

© ستاره شم رکفت کای شهربار ۱

۲ - از دساتیر. ,4 ‎Kies‏ دساتیر ص۲8۷ : رعش .
۸ - از :گرد 1 ‎aig)‏ تصفیر) .

‎in JP‏ دساتیر ص۰۷۳
‎٩‏ - دوکردك ‎stl‏ خرو ‎Le‏
‏یکی ظاهر ز بهر ‎ok‏ خوردن

‏ازین ‎PS‏ چرخ نا پایدار .
«فردوسی طوسی . شاهنامةٌ بخ‌ج۷ ص۲۰۳۷>.
‎gales SSL -۷‏

‏بر آموده بگوهر چون ‎WS‏
‏دگر پنهان برای خواب کردن.
نظام ی کنجوی «رشیدی» «فرهنگ‌نفلام».

‏۴-کردی ‎Bherdek‏ (شب زفاف « ‎ol‏ عل) «ژابا س ۰۳۵۹ .

‏بج
==== pdf 587

فارسی » ‎pines‏ پبراهن و يك تهی باشد و ‎UBT‏
‏بعربی سربال خوانند .

‎of‏ کوه - بکس اول »للم کوهی
است در ولابت مازسران! .

‏گر ۵ گیر ۴ - بت اول ۰ یمنی خجاع
ودلاور گیرنده - ‎ply‏ پبرافراسیاب هم بوده۴ -

‏گردمانه ۴ = بکس اول ومیم‌بالف
کشیده » بروزن ومعنی گرم دائه ات که لوعی
از تخم مازربون باشد و معرب آن جردمانق
است .

‎oof‏ * ه‌بروزن ارزن » عمروفت
ویعربی چید وعتق خوانند وجمع آ نگردنپاست.
وشجاع وقری وصاحب ‎a Wont‏ گوبندوجمع
‎ote of‏ باشد ۷ .

‎VO‏ = بنتح اول وئاك ونون‌بالف
کید 6 مطلق سبخ را کوبند ‎el‏ ازسیخ چوبی
‎aT,‏ که بدان کباب کنند با دان از تنور بر
آرند ۸ - و کبایی را نیز گوبندکه اول کوشت
‎LT‏ درآب جوشانند وبمدازآن ادويهةٌ ‎OT pole‏
پاشند وبر سیخ کشید کباب کنند و معرب‌آن
کردناج است - ‎Sy‏ عود و رباب وامثالآلرا

‏(۱) چش : چون .

‏۷
‏نیز کفته‌انداکه تار ‎oT,‏ بندلد ‎wth Gy‏ تاساز
آهنکه شود ‎٩‏ - و ‎se‏ بادبرهم آمده است»
‎dol se OT,‏ مخروطی که طفلان ‎OV pole,‏
پچند و از دست ‎GMAT‏ در زمین بچرخ در
‎-٩* aT‏ وآلتی را نیز کفته‌اند که ازچوب‌سازند
و بست اطفال دهند تا بدان ‎oly‏ رقتن آموزل
و بکسر اول » ‎gine‏ سیخ ‎VAS‏ - وکاسفزالو
باشد ۷۱ ویعربی رشفه خوالند - و گل سرخ را
فیز کویند .
‎US‏ بروزن اسفناج » بسسنی
کردانیده است ‎ASOT,‏ باشد که گوشت آنرا
درآب جوشانیده باشند و بعد ‎OT‏ بیخ کشند
و کباب کنند و بهترینآن مرغ جوان‌فربه‌باشد.
‎bof‏ - یک اول وفتم آخ رکه
میم باشد . ‎gles‏ است که بر اطراف کاغذ پاره
نوسند ولا غلام و کنیز کی که کرربخته باشد در
‎OT ole‏ مرقوم ‎wil‏ و درژیرسنکه ‎aig‏ بادر
‎SS‏ دفن کنند وگاهی برستون خاله هم آویز ند.
و بسی کوبند درمیان سور بوسف بابد گذاشت»
البته ‎gles cee SOT‏ نتواند رفت وبدست آید.
و ‎gm‏ ت رکیبی این لفت شهرنامه است چه (۱)

‏۱ - درجتوب قریة ‎thay (onl?‏ کوههلیمرز» «راپینو. ‎Lb de‏ مازسران واسترآباد

‏۲۰ بخشی انگلیی » , و نیز قلمه ایست در حوالی سمنان ‎Mee?‏ مهرسال ۸ شماره ص۳۳۹
وشمارء ه ص ۲4۸4 . ۴ - از: کرد ‎ge)‏ اول) + کیر ( گیر نده) .

‏۴ - )4 فهرست و
==== pdf 588

-۱۷۹۱-

بزبان پهگوی شهررا کر دگویند ۱- وسکموقش
نگن را ‎Hahei‏ :
‎FP‏ لا - بنتح اول ۰ بروزن و معنی
سروران است که بزرگان وصاحب قدرتان‌وسران
گردنان ۴ لظم © کنابه از ‎lat‏
‏نامدار است .
گردفای ۴ - بکراود و سکون ثانی
ونون بالف کشیده ‎Er IS goes » origins,‏
باشد - وچوییرا یز گوبند که برآن‌غلطکی‌صب
سازند وبدست طفلان دهند تا ‎aly‏ رفتن‌بیاموزهد
ربفتح ‎al‏ هم باین معنی وهم بمعنی چویی‌باشد
آمرودی که طفلان ربسمان بر آن پبچند و نوعی
برزمین اندازدکه تا ‎yo‏ زمان در گردش باشد
ویعربیآ ترا دوامه خوانند با تشدید واو .
گردنای ‎Ce‏ بنتح جم فارسی.
بمعنی آسمان است .
گر دن بشمشیر خار یدن - کنابه

از قرار کشته شدن بخود دادن(باتد) ۵ .

کردنه
‎os‏ خاریدن = کنابه از عثر
آوردن و بهانه کردن باشد ‎٩‏ .

گردان شتر - بکس الب وشم شین

وتای فرشت‌وسکون ‎hy‏ معروف است ۷ و کنایه
از حمیان پر زر ‎Asch‏ +
گر دنگ * .- بغتح اول بروزن‌فرسنگه,

مردم احمق ودبوث رااگونند .

گردن کش « کنابه از مردم با قوت
وقدرت ‎Ob sly‏ باشد *۱.

گر دن کنان نظم = کنابه از
شاعران صاحب قدرت و ‎lat‏ نامدار و غرا
باشد ۷۱.

گردنگل ۴"- بفتح اول و الث وکاف
فارسی و سکون نانی و رابع در آخر ۰ ‎on‏
‏کردنگ است که ابله و احمق ودیوث باشد.

گر دنه ‎=F‏ بنتح اول و الث و لبون »
بروزن ومعنی وردنه است » وآن‌چوبی باشسرها
بارك ومیان کنده که‌بدان ‎UMS‏ خمیرنان رایهن
سازند .

۱ - درخراسان امروزبهمین معنی در تلم هست «فرهشگه‌نظام‌ظاهراً روی ‎Lab‏ مدوری
نوشته مبشد (برخلاف قول رشید یکهگوید کاغذ مریست ) :

کرد نامه است که شه ‎Jal‏ هنر را کرده

۴ رشیدی بنقل از ‎he‏ میرزا .
ریق رکنم

۵ رل : . ۷

‎eye ge‏ وه «کردن + شتی

‎Tats 9 ‏شرابه‎ ol 2 ‏بگردن‎ - ۸

‎. ‏:کردنگل, ورك: جهانگیری‎ 3, ٩
ay ‏را بگیرد‎ hk ‏نه‎

‏0- کی دانم از اکابکرددکتان نظم
> انوری ایبوردی

‏۳ رك :55

‎yy .‏ : رشیدی

‏شکل ‎pout‏ که بر دابر دیتار است +
رضی
۴ - جمم گردن ‎(ee)‏ بمعنی بز رکه و

‎+ ‏«رشیدی؟‎ Soy

‎> tot ‏دزی ج ۲ ص‎ « de Suwon
۰۴ ‏وشیدی‎ ٩٩ ‏و توقف نون‎ - On Sale aie? =

‏بای یبل که
```


## [2026-09-05T17:56:15.659Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nimport re\nt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\nparts=re.split(r'\\[pdf page (\\d+)\\]', t)\nd={}\nfor i in range(1,len(parts),2):\n    d[int(parts[i])]=parts[i+1]\nfor p in (589,590):\n    print('==== pdf',p)\n    print(d.get(p,'')[:2600])\nEOF"
}
```


### [2026-09-05T17:56:17.158Z] TOOL RESULT

```
==== pdf 589

گردن نهادن - کنابه از فروتنی
کردن - وفرمانبرداری‌واطاعت نمودن (۱)نمودن
باشد ۷ . _

گردفی ‎08S‏ - کنابه از ‎oS‏
‏وتافرمانی کردن باشد .

گردو ؟ بکر اول و ‎aly HG‏
کشیده , گردکان ‎ae SV,‏

گردون سر شت = کنابه از مردم
صاحب عجب و تکبر و با ‎By‏ و تمکین و کاهل
وناموافق بائد ۴ .

گردون ‎Eye‏ - کنابه از آسان
است .

گر۵ه - بکر اول و فتح ‎Fatt‏
‏نوعی از ‎Ob‏ غیر تنك باشد 6 - و هرچیز مدور
و گرد را گویند عموماً - وپارچة زرد.مدوریرا که
بهودان بر کتف ‎le‏ خود دوزند بجهت امتباز
ازملمانان ‎Veg uel pT, byt‏ خوانند ۷

)1( چش: ‏ واطاعت.

{AVA
‏و باش کود را یز کفته‌اند - و بمعتی همه‎

ومجموع ‎gm‏ عست- وپنعتی ‎oA‏ نیز )4( آمده

است - و بفتح اول ۸ خاکه نقاشان باشد وآن
زغال سوده ات که در پارچه مته‌اند ‎BEB yy‏
های سوزن زده طراحی کرده مالند تا ازآن‌طرح
و تقش بجای دیگر ند - وآن‌کاغذ سوزن‌زده
را نیز کویند ‎٩‏ .

گرده ]لو - بنم
کرد باشد ‎ols.‏ میوه‌است شبیه پزردا لو .

گر ده بات = بابای‌ابجد بروزن‌اصفهان.
بمعنی‌نگاهبان‌باشد چه کرده بممنی‌نگاه هم آمده
است .

‎Cr 30‏ = کتابهاز] فتاب‌است-
وماء را نیز کوبند .

‏گرد گر 099 بمعنی ‎BS‏ چرخ

‏است که کنابه از آ فتاب وماه ‎Hath‏

‎“we Sah em‏ آلو

‎. feats ‏خم۱‎ (y)

‏۱ رك : رشیدی - وحاضر شدن ‎Tl,‏ شدن « فرهنگه نظام ©
- از :گرد ( بکسر ‎gC‏ ( پسوند صفیر ۰ سازند؛ اسم از صفت ) » رل: کردکان .
درختی است ( ‎Juglans‏ ) از دستة غان‌ها , باچوب محکم ‎WE ny‏ مرک ب که مفز آن روغن

‏بیاردارد. « کل کلاب ص ۲۷۸ >

‏م (پوند صفیر . سازندث اسم ازسفت)  ‎Cem) dF‏

‎. ‏رشیدی‎ HF

‏-از: گرد (بکر) +

‎ *‏ بمعنی قرص تان‌هم‌استعمال

‏شود . یهلوی ‎girtak‏ © , ارمنی 8۳۸21 , معرب جردقه « هوبشمان ۹۰۱ ۰.

‏۱ - رك : غیار .
۴ -گرده پردوش راهب ‎cre‏

‏حلقه در کوش ‎ark‏ لائم .
- از :کرد ‎pie)‏ )+ه ( سبت ) .

‎ENF‏ فیستانی «رشیدی»
‎٩‏ - نم اول . بمعنی‌کلیه (عی) است.

‏اوستا ‎veretka_ ۰ veredhka_‏ (کلیتین) . پپلوی 801۲18 . هندی - پرا کربت ‎wekka&‏
‎(as)‏ . کردی ‎gurdale‏ . بلوچی ‎guttigh‏ , وخی ‎velk‏ « اسشق ‎٩۰۵‏ > .
* گردون - بفتح اول » از :گرد (گردیدن) +-ون ( پسوند فاعلی ( = کردان,پپلوی

‎ogartén , 0‏ با ‎ovartin‏ , ۷2۲۵۵۵ < هوبتمان ۰6 - ورله : اسشق ‎Att‏
‏گردنده » چرخ - ارابه , کالکه - آسمان » فلك .

‎۰ ‏و۵‎ ۰ Vogts « Sales » ‏اول و پنجم = کشتن‎ ch - ‏دیدن‎ fo
‏تب ر که ص۰۲۳‎ > Vartate ‏بارتولمه ۱۳۹۸ » ؛ هندی‌باستان‎ > Varet - ‏اوستا‎ . 0
26۳20 ‏.کردی‎ * ۹٩ ‏کردیدن . چرخیدن | ) « اسفا ۱: ۷ ص‎ [ var. ‏نیز هندی باستان‎
‏؛ دور زدن ۰ چرخیدن - شدن » گشتن - ب رگشتن.‎ ٩۳٩۱ ‏گردش کردن »گردیدن ) « ژابا ی‎ (
. ‏تفیبر کردن - سرنگون شدن - سیر کردن »گردش کردن‎

==== pdf 590

۱۷۹۳ گرزن
گرد ۷ - نم اول و سکون ‎gl‏ وزای کویند ۴ ؛ و ‎GEL‏ نازی هم بنظر آمده است.
نقطه دار , عمود گرم - بت اول وفتح ثالی و سکون

آحنین راکو ‎moe‏ ]| الت ومیم . برادراعانیاسفندیاراست واوبدکوبی
اسفندبار پیش کشتاسب کرد و کشتاسب اسفندبار
و چماق چوب را گرز

را بند فرنمود 6 .
‎Vols J‏ پفتح اول ‎hs‏ و رایع
بالف کشیده بروزن فلك‌سان » آسمان را گویند؛
وبفتح اول وسکون ثانی هم آمده است - وعرش
اعظم را نیز گفته اند که فلك الافلاك باشد ۷ .
گردن بر وزن ارزن ۰ تاج مرصعی
بوده کیاترا بیار بز رک وسنگین وآترا پربالای
تخت محاذی سر ابشان‌با زنجیرطلامیآ وبخته‌اند .
کویند درآن صد دانه مروارید ‎oy‏ هربك بقدر
با کنجشگی وآن بانوشیروان رسیده و عربان
‎LT‏ قنقل بروزن منقل کنتندی و قنفل کیله

° کمته‌اند - و ‎dns‏ هاون را نیز کوبند -
‎esl als’,‏ هت که آلت تناسل باشد.
گرردمن ۴ ‎gi‏ اول والی‌وسکون
زای نقطه‌دار ‎Goby‏ دال بی‌نقطه و کسر میم ونون
‎woah OL‏ وپازند بمعتی‌دشمن وغنیم‌باشد.
گرزدن ۷ پم اول وفتح انی‌ورابع
وسکون ‎Ops cI‏ آخر ۰ بمعنی چاره کردن و
علاج نمودن باشد .
‎wis‏ بفتح اولو کی ثالث‌پروزن
ررزش؛تظلم وداد خواهی وتضرع وزاری‌لمودن را
۱ - پهلوی۰۷221 اوستا-۷22۲2 « بارتولمه۱۳۹۲ معرب جرز, آرمنی ع۷212,هندی
‎ott‏ ۷۵[۳2 (گرز رعد [ایندرا]) «اسشق ۹۰5 < نب رکه ص۲۳۷»» کردی 8072 « ژابا صس
‎yy. ۳۹۰ -۶۹‏ :گرزه. ۳ هز. ‎karzdiman .grOjdhmn .garazdaman‏ .
پپلوی 8501250 ( شک ) « ‎ima - ۴ ۰۰۱۱۷ Sig‏ «گرردن > ‎Cpe)‏
‏گزریدن ( رك :گرزیدن ۱) . ۴ - «گرزش, نظلم ‎ay‏ . خمروانی گفت :
بده داد من زان لبانت و کرنه سوی خواجه خواهم شد از تو ‎GG‏
‏آقای دهضدا کلمهرا مصحف «گزرش » ۳ ‎(GAS)‏ میدانند . ‎cal?‏ فری ‎۲٩۳‏ *.
۵ - و یز یکی از قهرمانان تورانی . ركه : فهرست ولف .
‎UY‏ پارسی ( مستعمل زرتشتیان ) - فارسی ‎garzman‏ ( آسمان ) . این‌کلمه‌در
اوستا 0۵۳0203 ‎nmana , garé6‏ 82۲۵ پازند 82۳6۵1۳1020 . مخدی 28۲0۳۳9۳
پارتی 6270110810 . اوراق ‎cyl‏ بپارسی‌میاله 67251120 . ‎LS,‏ پارسی- فارسی 82721۳00
تلفظ متأخر ومغلوط است ‎ines‏ (آسمان علیین » عرش خدا ) با ب‌منی وسیمتر (آسمان,بهشت).
‎Henning, Two Central Asian Words . p . 157) : 4,‏ ( ,)4 :
‎Henning , A list of Middle Persian ... , BSOS , IX,1,p.82 (‏
ورك : اسشق - هوبشمان۰۹٩ ‎(Dis)‏
‏۴ - + پارسیان بگوشد عرش است و شعرا گوبندآسمان است . دقیقی (طوسی) گوید :

مه وخورشید با برجیس وبهرام زحل با تیر و زهره بر کرزمان
همه حکمی بفرمان تورانند که ایزدمرترا دادء است‌فرمان.»

. ٩ ۳۵۷ ‏فری‎ cal?
```


## [2026-09-05T17:56:35.475Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\nprint(t[289][-1500:])\nprint('======= leaf 352 (≈p.894)')\nprint(t[352][:2200])\nEOF"
}
```


### [2026-09-05T17:56:37.260Z] TOOL RESULT

```
 'مده ومفرد گرفته دده است‪.‬‬

    ‫مملکت صين (چين)آرد‪* :‬وفى کل مدينة شثی بدعی الدرا وهوجری على رأى ملك تلكالمدينة‪.‬‬
   ‫مربوط بخیط ماد على ظهر الطریق للمامة کافة و بن الملك و ينه حور من فرمخ فاا حرك‬
   ‫الخیط الممدود ادلی حرکة تحرک الجرس ‪ .‬فمن کات له طلامة حرکک حذاالخ‌ط فبتحر که‬
   ‫الحری مه علی‌راس الملك فوژدن له بالدخول حتی هى حاله بنفه ویشر حطلامته و جمی‌للبلاد‬
                            ‫فیها ذلك‪« ».‬اخبارالسن والهند ص ‪( ۹۱6 - ۸۱‬از افادات علامه دهشدا) ‪.‬‬
       ‫معنی‌دو کث»است‬     ‫‪( -‬عر) «درارة بروزن جبانه‪.‬‬     ‫‪۱‬‬       ‫‪ -‬امر از «درآمدن؟ ‪.‬‬        ‫‪۵‬‬
     ‫‪ - ۷‬اوستا ‪( 012[800-‬طول) ‪.‬پپلوی [ک‪4‬ر‪۳‬د‪.9‬ی‪.121711‬بلوچی‬                            ‫«شرح قاموی» ‪.‬‬
    ‫‪۷۱۱٩۰‬‏‬     ‫‏‪ d۲8‬و ‪028۲0‬اسشق ‪ ۷4۵‬یز دریر‌لوی ‪«28۳10‬منای‪.»۱۷۲:۲‬استی ‪ «018۲20‬کث‪.‬است‬
     ‫کد‪ .‬اص ‪۲٩۰‬‏ »سمنالی‪2 .‬سنگسری»سرخه‌یی‬                      ‫فرىز لدی‪,‬و لطازی ‪zdread.‬‏ عرلی ‪27‬‬
                      ‫‪.‬یلکی ‪: 28۲81‬‬
                                  ‫وشهمیرزادی‪ .22۳64‬لاسگردی ‪« 28۳621‬که‪ ۲ .‬م‪ ۳۹۱۰‬ک‬
             ‫بدستهای د گر همچنین بخواهدرفت ‪.‬‬                  ‫چه سالهای فراوان و عمرهای دراز‬
      ‫‪‎‬ناتلک« ‪. 14٩‬‬
    ‫* درابر یی ‪ -‬از بونابی ‪( 00126۳2۲1‬نرده» شدکه)معرب‌آن درابزین ودربوز «دزی‬
    ‫‪#‬معحمدات عر مبه‌سامیه ص‪ » ۲ ۷۲‬و درابر ون «المتجد» رکف ‪ :‬داریز دنه دارآ فرین(‪)۱‬‬          ‫‪ ۱‬ص‪۶۳‬‬

     ‫بغيةٌ درصفحه ‪۳۸ ۰‬‬                                                                 ‫ودارفر بن (‪. )۱‬‬

======= leaf 352 (≈p.894)
      ‫پوس‬

                                     ‫کون طای باشد ‪.‬‬          ‫دو حتن ‪ -‬بر وزن سوختن » معروف‬
‫= دو ستارء شعرآی شاه‌ی‬           ‫خواهر‬          ‫دو‬           ‫لت که دوختن جامه باشد بوزن ‪٩‬‏ و دوختن‬
                                                             ‫حرع وزره باشد با تیر وئیزه مربدن دشمن ‪٩‬‏ =‬
‫میگوبند » و بعربی اختامهیل خوانند و عبور‬                     ‫وبمعنی اندوختن ومال جمع کردن هم هست‪- ۴‬‬
                        ‫وغیه‌صاء نیز گویند‪.‬‬                  ‫و شیر دوشیدن را یزگوبند ‪ - ۴‬و بمعنی ادا‬
                                                                 ‫کردن و گزاردن وام وقرض ونماز باشد‪. ۴‬‬
‫دو خبط ماون * ه کنایه از صبح‬
                                                             ‫دو <‪ - * 24‬بروزن سوخته » معروف‬
                           ‫باشد ‪۰‬‬    ‫کاذب وصبح صادق‬
                                                             ‫است ‏ ودوشیده ‪ ۱‬و‪-‬ادا کرده و گزارده رائیز‬
 ‫ی‬     ‫است‬   ‫دعروف‬    ‫‪۰‬‬   ‫زود‬    ‫رون‬    ‫‌‬   ‫د‬   ‫دو‬


‫وغم واندوم ودم وئفی راثیر کوبند ‪ -‬ودرعر ی‬                    ‫دوخ چکاد ‪ » ۲‬باجیم فارسی وکاف‬
‫بمعنی کرم باشد چه کرم ابریشم را دود الحرس‬                    ‫بر وزن کور سواد » بمعنی اصلم ‪ ۸‬باشد و آن‬
‫خوانند وکرم فرمزرا دودالصباغین » و درم قرمز‬                    ‫»‬‫چه‬ ‫شخصی است که سراو ساده و بی موی بود‬
‫جانوریست کوچك وآن دربوتة خارمیباشد وبعضی‬                     ‫دوخ یمنی ساده و چکاد بمە‌نی تارك سر و فرق‬
                      ‫گو ند در درخت بلوط باشد ‪.‬‬              ‫وجلی را کلوزبند که سراو مانند‬  ‫سراست ‪ -‬ک‬

   ‫‪ - ۱‬بهلوی‪ -‬یاز ند ‪ . ) 0۳6200 ( 03104‬استی ‪ 08 _ 0200‬و ‪03 - 0200‬‬
  ‫(محکم کردن)‪ .‬بلوچی ‪ 82661‬و‪( 1584 82‬دوختن)‪ .‬مدارزانی ‪« 606[0. 0‬اسذق ‪. ۷۷۵‬‬
    ‫گیلکی ‪ 020100‬؛ ریش کلمه بدایل ‪ 18221500 , 82000‬بلوچی‪ .‬کلم ابرانی ‪10.600‬‬
   ‫‪ ۴‬ره ‪ :‬اندوختن‌وح‪. ۱‬‬    ‫(لیزدرفارسی ‪ 712200‬پهلوی ‪ 0۲6660‬ااست رك‪« :‬هوبدمان ‪۲۷۵».‬‏‬
  ‫‪.‬‬      ‫‪02‬‬          ‫) دوشیدن )‪ 2‬بهلر ی‬              ‫هندی بتاان » رسه ‪hod -‬‏ ‪ihdgéd .‬‬         ‫‪۴‬‬
      ‫‏‪ .dûshîtan‬کردی ‪nihsûd . 8۱۱60‬‏ ‪ ( id _ mihsûd ۰‬دوخیدن )‪ .‬افعانی‪.12052۷21‬‬
      ‫اتی ‪ 0601‬و ‪01‬عنا ‪ .‬بلوچی ‪ . 08215۵0‬وخی ‪ »0712080000 , 61۳0 - 0۳2
```


## [2026-09-05T17:56:53.205Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\nhits=[i for i,p in enumerate(t) if 'دودمان' in p]\nprint(hits)\nfor leaf in hits[:2]:\n    print('=== leaf',leaf,'≈p',leaf+542)\n    p=t[leaf]\n    i=p.find('دودمان')\n    print(p[max(0,i-600):i+900])\nEOF"
}
```


### [2026-09-05T17:56:54.789Z] TOOL RESULT

```
[353, 354, 443, 653]
=== leaf 353 ≈p 895
                 ‫دود بورر‬                                                                  ‫ازآن هراراده‌ای کهخواهند کنند ‪.‬‬
                                             ‫‪٠‬‏‬            ‫ساختن باشد ‪.‬‬         ‫‪۵‬و دا ل‪ - ۲ 4‬بروزن کوساله ‪ .‬دامبازیی‬
 ‫‪٩‬‏ »بر وزن رودخاه ‪.‬‬                                  ‫دوخاه‬
                                                          ‫د‬                     ‫و‌چنان‌باشد که دوچوب بیاورند‬
                                                                                                           ‫است اطفال را“ آن‬
                              ‫دودمان وخالواده را گوند‪.‬‬                          ‫یکی بزرگ بمقدار سهوجب و دیگر یکوچك‬
                                                                                ‫بقدر بك قبضه وهر دو سر چوب کوچك را تيز‬
 ‫دود خوار د با واو ممدوله بروزن‬
‫و کلخن‬    ‫و مطبخی‬                 ‫هوشیار ‪ ,‬بامپرنده ابت‬
                                                                                ‫کنند وبرزمين گذارند وچوب بزرکه را بر سر‬
                                                                                ‫آن زنند تااززمین برخیزدفی‌الحال‌چوب نرزگه‬
               ‫تاب‪ -‬وتنباکوکش را لگیوزبند ‪.‬‬
                                                                               ‫را بآرن زد تا براه دور رود » و شخصی درآن‬
                                                                                ‫دور ایستاده است ‪ ۰۱‬کرآنرا کرفت بازی ازوست‬
                                               
=== leaf 354 ≈p 896
 ‫‪4‬‬                                                                                                                            ‫حودمان‬

‫دود = بضم اول بر وزن مور ؛ معروف‬                                   ‫دودمان‪ = ۱‬با میم بورزن دوستان »‬
‫است که تقیض ترديك باشد ‪ - ۱‬وبفتح اول ‪۷‬‬                             ‫خاندان وخانواده‪ ۴‬وقبیلهرا کوبند‪ -‬ونام موضعی‬
‫خواندن درسهای گذشته بود ‪ -‬و یالة شراب را‬                                                                ‫است نزديك بشیراز ‪.‬‬
‫واسوسانی که اخبارامراواعیان‬
                          ‫نیز کویند ‪ - ۸‬ج‬                          ‫دوده ‪ = ۴‬یسم اول بر وزن بوده ›‬
‫راتحقیق نمودهبلاطین وپادشاهان نویسند‪ -‬وبمعنی‬                        ‫دودمان و خانواده راکویند ‪ -‬و دود چراغ که‬
                       ‫‪.‬‬    ‫ابام وعهد وزمان هم هت‬                 ‫بجهت‌ساختن رمکب و سياهی گیرند‪ -‬ودود کش‬
‫دور آسران = با سین بی‌نقطه بر‬                                       ‫ر‬
                                                                    ‫پ‪-‬و‬‫وطبخ و بخاربرا گیفزته اند‬ ‫حمام م‬
‫وزن زآوورران‪ ,‬نام پادشاه جادو گران‌باشد واورا‬
```


## [2026-09-05T17:56:59.277Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\nprint(t[354][-1800:])\nEOF"
}
```


### [2026-09-05T17:57:01.231Z] TOOL RESULT

```
‫‪۱‬‬                 ‫> ‪.‬‬              ‫«اسشق‬
  ‫«کلتان ‪. ۸۸۱۰‬‬
      ‫‪ ۰‬بهلوی ‪katûd‬‏‬        ‫دودخانه‬        ‫ِ‬   ‫دودمان‬    ‫ت‬    ‫واتصاف)‬   ‫‪( ۰‬یوند نست‬            ‫از؛ دود ا‬         ‫ك‬    ‫‪۳‬‬

  ‫‪2‬‬    ‫آهتگد»‪‎‬‬   ‫دود‬       ‫مخفف‬        ‫‪o‬‬           ‫مخفف « دود آهنج» ‪۴‬‬             ‫‪۴‬‬        ‫‪۰‬‬     ‫‪6‬‬          ‫ی استق وهویشمان‬

      ‫‪ - ۱‬بهلوی ‪۲0d‬‏ (بعید) «اسشق ‪« ۸۵‬منای ‪ > ۲ : ۲۷۲‬از ابرانی باستان ‪2۳84 -‬‬
  ‫« بارتولمه ‪ »۰۵۷‬دیبرکه ‪ » ۶‬پارسی باستان و اوستا‪ .3۲00-‬هندی باستان _ ‪arûd‬‏ ‪ .‬کردی‬
  ‫‪۲‬ففانی ‪ 1۳11۰‬بلوجی ‪ ۲04‬و ‪ ۲11۰‬وخی ‪ . ۲1‬بودغا ‪« 0701‬اسدق ابا »‪ .‬کیلکی ‪. ۲110‬‬
                                                                            ‫ا‬
      ‫‪ .‬سنگری‬         ‫* سمنانی ‪rid‬‏ و ‪۲1‬‬                ‫ص‪۳۹‬‬
                                                          ‫» نطنز ی ‪rûd‬‏ ‪ °‬ك ‪۲ ۱ .‬‬                     ‫فریزندی و برلی ‪۲0‬‬
                                ‫› ‪.‬‬    ‫« ك‪ .‬ص‪۳۰۱‬‬              ‫وشهمیرزادی ‪ . ۳1‬سرخه‌بی ‪ . ۲114‬لاسگردی ‪۲‬‬
                       ‫‪( - ۷‬مر) بسن گردیدن* منتهی الارب * کردکتن « غیات اللغات» ‪.‬‬
      ‫بدست رسانیدن پیاله های شراب در مهمانی « نام الاطا > مأخوذاز(عر)‪.‬‬                                 ‫‪ - ۸‬از دست‬

  ‫"‪« .‬دو؟ بمعنی دوغ‬                            ‫رك‪ :‬دودان سرون ‪.‬‬         ‫‪۶‬‬             ‫مأخوذ از (عر)‪. ‎‬‬                    ‫‪٩‬‬
      ‫که درنسخ‌مروج‬        ‫ات‬   ‫دور اسروب» ‪bêrsarûD‬‏‬              ‫ابن نامم صحف(‬       ‫ظ›‬         ‫‪۳۱‬‬                  ‫(ه‪.‬م ) آهده‪۰ ‎‬‬
      ‫النهب « دورشرین؟ و«دوسر؟ ودرتاریخ طبری «خوراسرو؟آمده واو سر منوش چیپر (منوچهپریادشاه‪‎‬‬
      ‫بشدادی) وجد سیزدهمین زرتشت است طبق‌سنت (رك‪ :‬مزدینا جدول برایر ص ‪ )۸1‬نه دشمن‌او‪.‬‬
          ‫( برهان فاطع ‪) ۷۱۱‬‬
```


## [2026-09-05T17:57:11.504Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nimport re\nt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\nparts=re.split(r'\\[pdf page (\\d+)\\]', t)\nd={}\nfor i in range(1,len(parts),2):\n    d[int(parts[i])]=parts[i+1]\nprint(sorted(d)[:5], sorted(d)[-3:])\nfor p in (31,32,33):\n    print('==== pdf',p)\n    print(d.get(p,'')[:2200])\nEOF"
}
```


### [2026-09-05T17:57:13.295Z] TOOL RESULT

```
[1, 2, 3, 4, 5] [551, 552, 553]
==== pdf 31

مالیطرنا م۱۹۶۸
کوبند بوتانی ات .38 خوانند, وصعترا کرچه باسین بی‌نقطه است لیکن
مالیطر فا ۱ « بفتح طای حطی‌وسکون | درکتب طبی بصاد نوشته‌اند تا بشمین مشتبه‌نشود.
رای قرشت و لون بالف کشیده . و پلفت بونانی | خوردن‌آن درطمام ضمف‌چشم را نافع باشد وقوت
زاج سیاه باشد و آن را زاج کفشگران اس باصره را نگاه دارد -
میگوشد؛ وبحذف مانی‌هم آمده است که ملیطرنا مامهستان « بفتح ثالك ‏ و کسرهایروزن
باشد. + ناوکستان . دوائی است که آنرا ساذج هندی
ها » بروزن لام » مادرراگوبند وبمرپی | کوبند و آن برکی است مانند بر که کردکان
والده و ام خوانند ۲ .28 و در روی آب پیدا میشود . بخورآن بجه را از
مامك * بروزن ناوك . مصفر هام است نگ بزیرآورد(؟) -
که مادر باشد پستی ماد رک - و مادر را هم مامیشا ؟ - با ناك بتتای‌رسید. دای
میگوبند ۴۳ .#* متلئه بالف کشیده , بلفت سربانی نام رستنیی‌باشد
مامون « بروزن (۱) هامون . نوعی‌از بفایت بیمزه ودرآب بهم میرسد ودر قاضات بکار
پودنه کوهی باشد و آلرا بس‌بی صعتر الجمام | برند و عصارة آنرا شیاف مامینا خوانند .
() چك : بوزن . () چش : آرد . ۹
۱ - بونانی 33612818712 ‎٩‏ اشتینگای > . ؟ -قی : ماما ۰ مامی » لیتوانی
8 30۵ (مادر) . املاوی کلیسیابی 38778 ( ماما ) » آلبانی 136116 » وخی
.۰ سربکلی 33282 (مادر بز رکه) . افغانی 12181 (عمه » خاله) ۰ بونانی114772302 ۰
6 ( ماما » مادربز رکه ) . لاتینی 33870382 » 17121212118 ( ماما + مادربز رکه ) ۰
آلمانی عالی قدیم 30002 . 3301 ( عمه . خاله ) «اسشق ۹۹۳ > ۰ پازند 133878(مادر)
* باروچا ۰۳۱۱
شاد الا بدر مر که نه‌یینی مردم بکر جز در رحم مام نیابی دختر.
انوری ابیوردی درقصیدء راجع بحملهٌ غزان . « فرهنگه نظام » -
۴ - از : هام (هم.) + که ( پوند تحبیب و تصفیر ) .
۴ - ممیتا « دزی ج ۲ اس چ۹۱ ۰ 80818106۳ (ف) ۸« دزی جس ۲:۵0
0 مالیدن - بفتح دال » اوستا - 33872 » 1287628111 ( جاروب شده ) » پهلوی
2 ] ۸۵۵ ۰ 2۳2 ] فقاطعهل .۰ متفه ] هط۵5ل , ۵ط22720(9 ( جماع ) ۰
(جناع کردن). 2211088 ۰ 332[)1(808 ؛ هندی باستان- 2:۲2 , [ع12279180
( پاك کردن ) »کردی 2 3.3110 ( جارو ب کردن ) بلوچی 2 و2212 . 22160285
( ساییدن ‏ مالیدن , مخلوط کردن ) » استی 323۳218 ( جاروب کردن ) « اسشق ۹۹۲ 4
دست کشیدن روی چیزی ۰ چبزی را دردست مکرر فغار دادن » دوچیز را بهم فشاردادن » مشت
ومال دادن » چیزی را ( مانند رنگه , روغن ) روی جم ی کشیدن .
2 ماما.- رك : مام ؛ در تهرانی 3387528 (قابله . مام‌ناف) » در افغانی 112132 (دائی,
خال ) در فارسی آدیی بمعتی مادر است :
هت مامات اسب و باپا خر تو مشواتر 
==== pdf 32

-۱۹4۹- مانا
مامیرآن ۱ - با رای بی نقطه پروزن ِ که عربان بیت خوانند ۴ - واسباب وضروریات
غازبخان » نوعی از عروق‌السفر است وآن دوائی | خانه را نیز کوبند - و بمعنی ما باش د که متکلم
باشد زرد رنکه بسپزی مابل » باريك و کره‌رار | مح‌الغیر است ۴ - و بمعتی مارا هم هست که در
میشود . گرم و خغك است در چهارم . برقانرا مقابل شما را باشد ۴ - و امربرگذاشتن ومالدن
نافع است و آنرا بعربی بقلةالخطاطیف و شجرة | هم هست بعنی بگذار و باش و بمان ۴ - و شبه
الخطاطیف خوانند . کوبند چون +جچةٌ پرستوك در و مثل و مانند را نیز کوبند 9 - و بممنی باقی
آشیان نابینا شود مادر وی غاخی از مامبران | و ابد و جاویدان هم کفته اند - و بلفت هندی
آورده درآشیانه نهد چشم بچه‌اش بینا کردد . | بمعنی حرمت وعزت وقبول ومقبول باشد -
۱ ید هافا٩‏ - بر وزن دانا . بزبان زند
۱ ۳ میرمیران « دزی ج؟ ص۹۲۸ * مرمیران « دزی ج ۲ ص۵۸۵ ۰۹ لغت فارمی
است . فرهنگه نوبسان‌آنرا با 3611608108 (خالیدولیون [ه.م.] ) بونانیان مترادف داسته‌اند
و اسم عربی « بقلة الخطاطیف > ترجمهٌ این کلم بودانی - بعنی « گیاه پرستوها » - است -
«ناه) - 11602۵1۵ کنته‌اند که محتملا 61140186-) (فر) راکه دارای عصاره وريشهٌ زرد
رنگه است » با داروی شرقی دیگر ی که آنم دارای ریشه های زرد رنگه است بعنی عنام۲۰
8 خلط کرده‌اند . اصل گیاه اخیر از چین است وریشه های آنرا بابران وهند میبردند ودر
مغزن‌الادویه شرح آن‌آمده . مایرهوف همین قول را معتبرمیداند « عقار ۷۸۱ اف >. ور4: دزی
چص ۵۹۵ ۴ - پپلوی 28 ( خانه » مکن ) « یب رکه ص۱۶۶ * » پارسی باستان
- 328812 ( خانه » سرای ) » در پهلوی بجای - 373288 اوستایی‌کامهٌ 7320 ( خانه ) را
بکار برده اند , 28)1(9878 ۰ 28)1(501 ( منزل ) , 340028 ۰3200:9120
منز لکردن ) »و « ماندن » فارسی نیز ازهمین ربقه است . «اسشق ۹۹4*.
۴ - ضمیراول شخص‌جمع مفعولی: دادمان » گفتمان ؛ وضمیر اضافی (ملکی): کتابمان ۰
کلاهمان . درپهلوی 3328 « نیب رکه ص ۱4۵ . ۴ -ر4 : ماندن .
8 - مان صورت پسوند بمعانی‌ذیل بکاررود: الف) - مان ۳ - من ۰ ازاوستابی 1387225
بهئوی 3281128 ( اندبشیدن ) : شادمان » پشیمان: » پژمان » نربمان , رادمان » قهرمان .
دشمن « فاب ‎٩‏ ص ۰۷۳ ب )مان ( از ريشة 46۳888 (کانتها ) و 8673288 ( دیگر
بخشهای اوستا ۰ پپلوی 1328 بمعمتی خانه ) : کشتمان . دودمان » کرزمان ۶ فاب ۱ ص۷۳ح >
ج ) پسوند سازندة اسم معتی از ربشهٌ قعل : سازمان » زایمان . د): پوند سازندة آسم ذات از
مصدر مرخم : ساختمان . علاوه بر اینها پسوند مان ( از مصدر مانستن ) را ذ کر کرده اند و
« شیرمان > و «آسما
==== pdf 33

ماعلق -۹-
و یازه(۱) طم خدای عزوجل است ۱ - وبمعتی | چیزی شدن باشد بعنی شبه ومانند ونظیرشدن -
شبه و نظیر و مثل و مانند هم آمده است ۴ مانطس ‎٩‏ - با نون وطای حطی‌وسین
ویستی‌هماا - وکوبی وینداری ۴ نیز کفته‌اند. معقص وحرکت لامعلوم . حجری است هندی
مافاف ؟ - بروزن آلاف . ماماچه را | پمتی‌سنکی است که درهندوستان میباشد. کویند
کویندو جرمی قابله خوانند - و بمعنی ناف‌هم باطل‌السحر است, هر که باخود دارد سحر پروی
آمده است وآ نکوی باشد در شکم.#* کار تکند و از جمیع امراض محفوظ باشد.
هافستی * « بر وزن داستن . بصفت مانب ۷ - بنکون نون وکاف فارسی,

() چك : ژند وپاژند .

۱ - در فرهتگه دسانیر (ص ۲۹۵ ) پس از نقل قول برهان کوبد : « باید داننت که
مونا بالواو خدا را کوبند > هزوارش 51۵2. 1712۵02 بهلوی ۷۷۵1808 (خدا) رك : بونکر.
قرهتکه چهلويك س2۸ ضل۱ سور : ص۱۱۳ :۱ . جهانگیری نیز بنقل از * ژند » این کلمه
را بممتی خدا آورده . ۴ - صفت معبهه از « ماندن > بمعنی مانند بودن :
قرو ستبی دل دشمن بدا ن كلك شهابآبین بدرانی صف لشکر بدان تیغ فلك مانا -

۴ رد : ح٩‏ صفحهٌ قبل - ازرقی هروی « رشیدی > «فرهنگه تظلم».

۴ - مخفف « مام ناف » همین معنی « رشیدی > + - از : مان ( ماندن )
[ر3 : مایدن] ۳-ستن ( پوند مصدری ) جزء اول ازربِعهٌ - 138 ( آندبشیدن » تصورکردن)»
قی : اوستا 2102 2۳6 13282768 (مانند » نظیر) . نولد که «مانتن» را از ربشةٌ -۰332
ساسکریت -32288 (عکس, تصویر » ظهور, شباهت) میداند * اسشق ۹۹۷ > هوبشمان مانستن‌را
با تواستن قیل ی کرده » کوید : بنابراین مانستن (شبیه بودن) همچنانکه نول دک ه گفته ممکشست
از08339 (مانتد » شبیه) هشتق باشد » و قس : دانتن ۸ هوبشمان ۹۹۷ .

‎٩‏ - در تحقةٌ حکیم موّمن و فهرست مخزن الادوبه و ذبل قوامیس دزی تیست » شاید
مس « مالیشطم *رك : دزی ج ۷ص 090 . ۷ - از اوستا 332۷۷880 ( رلد: هاء)
این‌کلمه دریسنی‌لهجه های ابرانی بافی‌مانده : کردی 13288 ۰ 13288 ۰ 332388 :10317288
( مله ),* ژایا ص ۳۸۸ ۰ درطبری نیز 33288 :

‏مه آش پرستی ته دیم ور قدیمه بهاره ۰ بهشته, مهر ومانگه» ته دیمه.
( آتش پرستی من در پیش روی توعادت قدیم است . بهار است » بهشت. است » خورشید و ماه
است . نه رویت ) «رضاقلی هدایت . انجمن‌آرا : دیم .> در فارسی هم‌آمده است :

‏بگرمی بدیشان یکی بان زد کزآن باتک تب لرزه بر مانگه زد .

‏عنصری بلخی « انجمن‌آرا » .
و« مانگه دیم » ( ماه صورت ) در اعلام کسان آمده .

‏۵ مائشن - بختح دال ».از : مان ( ریشه )+ دن ( پوند مصدری ) ۰ ایرانی باستان
3280 * پارتولمه ۰۴۱۱۲۶ پپلوی 31284188 «لیبر که ۵-۱4۶ *
```


## [2026-09-05T17:57:29.792Z] TOOL CALL #67: Bash

```json
{
 "command": "sed -n 1,60p tools/fetch_source.py"
}
```


### [2026-09-05T17:57:29.836Z] TOOL RESULT

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
        with urllib.request.urlopen(req, timeout=60) as r:
            status = r.status
            raw = r.read(4_000_000)
            ctype = r.headers.get("Content-Type", "")
            enc = "utf-8"
            m = re.search(r"charset=([\w-]+)", ctype)
            if m: enc = m.group(1)
            body = raw.decode(enc, errors="replace")
            if "html" in ctype or body.lstrip().lower().startswith("<!doctype html") or "<html" in body[:2000].lower():
                mt = re.search(r"(?is)<title>(.*?)</title>", body)
```


## [2026-09-05T17:57:37.417Z] TOOL CALL #68: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CC%A5l%CC%A5h%E2%82%81g%CA%B0%C3%B3s\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%E1%B9%93m\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D8%A7%D8%B2\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%D9%88%D8%AF%D9%85%D8%A7%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D9%86%DA%AF\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 116 verification (Del/Dlgho 'long'; Dem/Domu 'house')\" ; done"
}
```


### [2026-09-05T17:57:42.483Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/fd56cf77026c8a06.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bc8847785715aa50.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/52448cabf42d7c97.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dda1fe7d601c7610.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/33562df0fea41d6e.txt
```


## [2026-09-05T17:57:45.399Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in fd56cf77026c8a06 bc8847785715aa50; do echo \"######## $f\"; head -c 400 $f.txt; echo; grep -n -i \"Etymology\\|descendant\\|Proto-Iranian\\|Avestan\\|Persian\" $f.txt | head -20; done"
}
```


### [2026-09-05T17:57:47.252Z] TOOL RESULT

```
######## fd56cf77026c8a06
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CC%A5l%CC%A5h%E2%82%81g%CA%B0%C3%B3s
FETCHED: 2026-09-05T17:57:39Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
######## bc8847785715aa50
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%E1%B9%93m
FETCHED: 2026-09-05T17:57:39Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/dṓm - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/dṓm - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community portal 
 
62: Etymology 
74: Descendants 
142: Etymology
249: Proto-Balto-Slavic: *damús ( see there for further descendants )
252: Proto-Hellenic: *dómos ( see there for further descendants )
254: Latin: domus ( see there for further descendants )
257: Proto-Celtic: *dāmos ( see there for further descendants )
259: Descendants
273: Proto-Iranian: *dám 
274: Avestan: 𐬛𐬀𐬨 ( dam )
```


## [2026-09-05T17:57:49.719Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '55,110p' bc8847785715aa50.txt; echo \".....\"; sed -n '140,175p' bc8847785715aa50.txt"
}
```


### [2026-09-05T17:57:49.776Z] TOOL RESULT

```
 1 
 Proto-Indo-European 

 Toggle Proto-Indo-European subsection 

 1.1 
 Etymology 

 1.2 
 Noun 

 1.2.1 
 Declension 

 1.2.2 
 Derived terms 

 1.2.3 
 Descendants 

 1.3 
 References 

 Toggle the table of contents 

 Reconstruction:Proto-Indo-European/ dṓm 

 1 language 

 Français 

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
.....
 [ edit ] 

 Etymology
 [ edit ] 

 From *dem- ( “ to build ” ) +‎ *-s ( root nominal suffix ) .

 Noun
 [ edit ] 

 *dṓm   f [ 1 ] 

 home 

 house 

 Declension
 [ edit ] 

 Athematic, acrostatic

 singular

 nominative

 *dṓm 

 genitive

 *déms 

 singular

 dual

 plural
```


## [2026-09-05T17:57:56.006Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 52448cabf42d7c97 dda1fe7d601c7610 33562df0fea41d6e; do echo \"######## $f\"; sed -n '1,6p' $f.txt; grep -n -i \"Etymology\" $f.txt | head -3; done"
}
```


### [2026-09-05T17:57:57.502Z] TOOL RESULT

```
######## 52448cabf42d7c97
URL: https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D8%A7%D8%B2
FETCHED: 2026-09-05T17:57:40Z
STATUS: 200
TITLE: دراز - Wiktionary, the free dictionary

دراز - Wiktionary, the free dictionary 
62: Etymology 
85: Etymology 1 
94: Etymology 2 
######## dda1fe7d601c7610
URL: https://en.wiktionary.org/wiki/%D8%AF%D9%88%D8%AF%D9%85%D8%A7%D9%86
FETCHED: 2026-09-05T17:57:42Z
STATUS: 200
TITLE: دودمان - Wiktionary, the free dictionary

دودمان - Wiktionary, the free dictionary 
62: Etymology 
82: Etymology 
170: Etymology
######## 33562df0fea41d6e
URL: https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D9%86%DA%AF
FETCHED: 2026-09-05T17:57:42Z
STATUS: 200
TITLE: درنگ - Wiktionary, the free dictionary

درنگ - Wiktionary, the free dictionary 
62: Etymology 
143: Etymology
```


## [2026-09-05T17:58:00.295Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== دراز\"; sed -n '140,215p' 52448cabf42d7c97.txt; echo \"=== درنگ\"; sed -n '138,190p' 33562df0fea41d6e.txt; echo \"=== دودمان\"; sed -n '165,215p' dda1fe7d601c7610.txt"
}
```


### [2026-09-05T17:58:00.370Z] TOOL RESULT

```
=== دراز

 Edit 

 View history 

 General

 What links here 
 Related changes 
 Upload file 
 Permanent link 
 Page information 
 Cite this page 
 Get shortened URL 

 Print/export

 Create a book 
 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 See also: دراژ 

 Persian
 [ edit ] 

 Etymology
 [ edit ] 

 From Middle Persian 𐯌𐮲𐮹𐮰𐮿 ( dlʾc /⁠drāz⁠/ ) , from Proto-Iranian *draHǰáh , from Proto-Indo-Iranian *draHǰʰas , ultimately derived from Proto-Indo-European *dl̥h₁gʰós .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /da.ˈraːz/ 

 ( Dari, formal ) IPA ( key ) : [d̪ä.ɾɑ́ːz] 

 ( Dari, formal ) IPA ( key ) : [d̪ä.ɾɑ́ːz] 
 ( Kabuli ) IPA ( key ) : [d̪ä.ɾɑ́ːz] 

 ( Hazaragi ) IPA ( key ) : [d̪ä.ɾɔ́ːz] 

 ( Iran, formal ) IPA ( key ) : [d̪e.ɹɒ́ːz] 

 ( Tajik, formal ) IPA ( key ) : [d̪ä.ɾɔ́z] 

 Rhymes: -aːz 

 Readings

 Classical reading ? 

 darāz

 Dari reading ? 

 darāz

 Iranian reading ? 

 derâz

 Tajik reading ? 

 daroz

=== درنگ
 From Wiktionary, the free dictionary

 Persian
 [ edit ] 

 Etymology
 [ edit ] 

 Inherited from Middle Persian dlng' ( drang , “ period, duration ” ) , from Old Persian, from Proto-Iranian *drangah , from Proto-Indo-Iranian *drangʰas , from Proto-Indo-European *dlongʰos ( “ long ” ) , see there for cognates.

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /di.ˈranɡ/ 

 ( Dari, formal ) IPA ( key ) : [d̪ɪ.ɾäŋɡ] 

 ( Dari, formal ) IPA ( key ) : [d̪ɪ.ɾäŋɡ] 
 ( Kabuli ) IPA ( key ) : [d̪ɪ.ɾäŋɡ] 

 ( Hazaragi ) IPA ( key ) : [d̪i.ɾäŋɡ̥] 

 ( Iran, formal ) IPA ( key ) : [d̪e.ɹæɲɡʲ̥] 

 ( Tajik, formal ) IPA ( key ) : [d̪i.ɾäŋɡ] 

 Rhymes: -anɡ 

 Readings

 Classical reading ? 

 dirang

 Dari reading ? 

 dirang

 Iranian reading ? 

 derang

 Tajik reading ? 

 dirang

 Noun
 [ edit ] 

 Dari

 درنگ 

=== دودمان
 From Wiktionary, the free dictionary

 Persian
 [ edit ] 

 Etymology
 [ edit ] 

 Inherited from Middle Persian [Book Pahlavi needed] ( dwtkmʾn /⁠dūtakmān, dūdagmān⁠/ ) . By surface analysis , دود ( dud , “ smoke ” ) +‎ ـمان ( -mân ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /duːd.ˈmaːn/ 

 ( Dari, formal ) IPA ( key ) : [d̪uːd̪.mɑ́ːn] 

 ( Dari, formal ) IPA ( key ) : [d̪uːd̪.mɑ́ːn] 
 ( Kabuli ) IPA ( key ) : [d̪uːd̪.mɑ́ːn] 

 ( Hazaragi ) IPA ( key ) : [d̪ud̪.mɔ́ːn] 

 ( Iran, formal ) IPA ( key ) : [d̪uːd̪.mɒ́ːn] 

 ( Tajik, formal ) IPA ( key ) : [d̪ud̪.mɔ́n] 

 Rhymes: -aːn 

 Readings

 Classical reading ? 

 dūdmān

 Dari reading ? 

 dūdmān

 Iranian reading ? 

 dudmân

 Tajik reading ? 

 dudmon

 Noun
 [ edit ] 

 دودمان • ( dūdmān / dudmân ) ( plural دودمان‌ها ( dūdmān-hā / dudmân-hâ ) , Tajik spelling дудмон )
```


## [2026-09-05T17:58:11.074Z] TOOL CALL #73: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dl%CC%A5h%E2%82%81g%CA%B0%C3%B3s\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%DB%8C%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%DA%AF%D8%B1%D8%B2%D9%85%D8%A7%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D9%85%D8%A7%D8%AF%D8%A7%D9%85\" \\\n \"https://www.etymonline.com/word/belong\" \\\n \"https://www.etymonline.com/word/timber\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 116 verification (Del/Dlgho, Dem/Domu)\" ; done"
}
```


### [2026-09-05T17:58:14.598Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/7138adb80226267f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7113dcda57f1193f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c4efbb06b827420f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2be76f2bdfcfbc08.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/74a446d24f335b66.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a17e718b3bca4163.txt
```


## [2026-09-05T17:58:17.900Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 7138adb80226267f 7113dcda57f1193f c4efbb06b827420f 2be76f2bdfcfbc08 74a446d24f335b66 a17e718b3bca4163; do echo \"######## $f\"; sed -n '3,5p' $f.txt; awk '/From Wiktionary, the free dictionary|etymonline/{found=1} found' $f.txt | sed -n '1,60p' | grep -v \"^ *$\" | head -30; echo; done"
}
```


### [2026-09-05T17:58:19.645Z] TOOL RESULT

```
######## 7138adb80226267f
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/dl̥h₁gʰós - Wiktionary, the free dictionary

 From Wiktionary, the free dictionary
 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
 Proto-Indo-European
 [ edit ] 
 Etymology
 [ edit ] 
 From the stem *delh₁gʰ- ( “ ~ to be long; to last, endure ” ) , found in Ancient Greek ἐνδελεχέω ( endelekhéō , “ to continue ” ) , ἐνδελεχής ( endelekhḗs , “ continuous ” ) and probably Latin indulgeō ( “ to concede ” ) , [ 1 ] which appears to be a compound of a marginally attested root *del(h₁)- ( “ long ” ) (cf. Russian длина́ ( dliná ) , Old Czech dél ( “ length ” ) , [ 2 ] Proto-Slavic *dьliti ( “ to last, prolong, delay ” ) [ 3 ] and Old Norse tálma ( “ to hinder ” ) ) plus an unknown root *h₁egʰ- or suffix *-gʰ- . [ 4 ] Prósper believes that this velar element is simply the root *ǵʰeh₁- (which she glosses as "to come, reach"). [ 5 ] 
 Resemblance to the synonym *dlongʰos is conspicuous and probably not by coincidence, but a formal connection is difficult, due to the presence of the laryngeal in one but not the other.
 Adjective
 [ edit ] 
 *dl̥h₁gʰós ( non-ablauting ) [ 6 ] [ 7 ] 
 long 
 Inflection
 [ edit ] 
 Thematic
 masculine
 feminine
 nominative
 *dl̥h₁gʰós 
 *dl̥h₁gʰéh₂ 
 genitive
 *dl̥h₁gʰósyo 
 *dl̥h₁gʰéh₂s 
 masculine
 singular
 dual
 plural
 nominative
 *dl̥h₁gʰós 
 *dl̥h₁gʰóh₁ 

######## 7113dcda57f1193f
STATUS: 200
TITLE: دیر - Wiktionary, the free dictionary

 From Wiktionary, the free dictionary
 See also: دیز , دير , and د ي ر 
 Brahui
 [ edit ] 
 Etymology 1
 [ edit ] 
 Inherited from Proto-Dravidian *nīr . Cognate with Badaga நீரு ( nīru ) , Kannada ನೀರು ( nīru ) , Malayalam നീര് ( nīrŭ ) , Tamil நீர் ( nīr ) , Toda நீர் ( nīr ) , Tulu ನೀರ್ ( nīrŭ ) , Telugu నీరు ( nīru ) .
 Noun
 [ edit ] 
 دِیر ( dīr ) 
 water 
 References
 [ edit ] 
 Bray, Denys ( 1934 ), “dīr”, in The Brahui Language ‎ [1] , Calcutta, India: Superintendent Government Printing, Part II: The Brāhūī Problem; Part III: Etymological Vocabulary, page 98 
 Etymology 2
 [ edit ] 
 Inherited from Proto-Dravidian *yĀr . Cognate with Tamil யார் ( yār , “ who ” ) , Kannada ಯಾರು ( yāru ) .
 Pronoun
 [ edit ] 
 دیر ( der ) 
 who 
 اونا پِن دیر اے؟ onā pin der e? What is his name? 
 References
 [ edit ] 
 Bray, Denys ( 1934 ), “dēr”, in The Brahui Language ‎ [2] , Calcutta, India: Superintendent Government Printing, Part II: The Brāhūī Problem; Part III: Etymological Vocabulary, page 97 
 Persian
 [ edit ] 
 Persian Wikipedia has an article on: دیر 
 Wikipedia fa 
 Etymology 1

######## c4efbb06b827420f
STATUS: 200
TITLE: گرزمان - Wiktionary, the free dictionary

 From Wiktionary, the free dictionary
 Persian
 [ edit ] 
 Etymology
 [ edit ] 
 Akin to Old Armenian գերեզման ( gerezman ) ; an Iranian borrowing.
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /ɡa.raz.ˈmaːn/ 
 ( Dari, formal ) IPA ( key ) : [ɡä.ɾäz.mɑ́ːn] 
 ( Dari, formal ) IPA ( key ) : [ɡä.ɾäz.mɑ́ːn] 
 ( Kabuli ) IPA ( key ) : [ɡä.ɾäz.mɑ́ːn] 
 ( Hazaragi ) IPA ( key ) : [ɡä.ɾäz.mɔ́ːn] 
 ( Iran, formal ) IPA ( key ) : [ɡʲæ.ɹæz.mɒ́ːn] 
 ( Tajik, formal ) IPA ( key ) : [ɡä.ɾäz.mɔ́n] 
 Rhymes: -aːn 
 Readings
 Classical reading ? 
 garazmān
 Dari reading ? 
 garazmān
 Iranian reading ? 
 garazmân
 Tajik reading ? 
 garazmon
 Noun
 [ edit ] 
 گرزمان • ( garazmân ) 
 the highest heaven ; heaven
 References

######## 2be76f2bdfcfbc08
STATUS: 200
TITLE: مادام - Wiktionary, the free dictionary

 From Wiktionary, the free dictionary
 Ottoman Turkish
 [ edit ] 
 Alternative forms
 [ edit ] 
 مادامه ( madama ) 
 Etymology
 [ edit ] 
 From French madame .
 Noun
 [ edit ] 
 مادام • ( madam ) 
 madam ( form of address for a European lady ) 
 Descendants
 [ edit ] 
 Turkish: madam 
 Further reading
 [ edit ] 
 Kélékian, Diran ( 1911 ), “ مادام ”, in Dictionnaire turc-français ‎ [1] (in French), Constantinople: Mihran, page 1089b 
 South Levantine Arabic
 [ edit ] 
 Etymology
 [ edit ] 
 Learned borrowing from Arabic مَا دَامَ ( mā dāma ) .
 Pronunciation
 [ edit ] 
 IPA ( key ) : /ma.daːm/ , [maˈdæːm] 
 Audio ( Jerusalem ) : ( file ) 
 Conjunction
 [ edit ] 

######## 74a446d24f335b66
STATUS: 200
TITLE: Belong - Etymology, Origin & Meaning

URL: https://www.etymonline.com/word/belong
FETCHED: 2026-09-05T17:58:14Z
STATUS: 200
TITLE: Belong - Etymology, Origin & Meaning
Belong - Etymology, Origin & Meaning 
 Search 
 Log in 
 Columns 
 Forum 
 Apps 
 Premium 
 Log in 
 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Origin and history of belong 
 belong (v.) 
 mid-14c., "to go along with, properly relate to," from be- intensive prefix, + longen "to go," from Old English langian "pertain to, to go along with," which is of uncertain origin but perhaps related to the root of long (adj.). The senses of "be the property of" and "be a member of" are attested from late 14c. Cognate with Middle Dutch belanghen , Dutch belangen , German belangen . It displaced earlier Old English gelang , with completive prefix ge- .
 also from mid-14c. 
 Entries linking to belong 
 long (adj.) 
 Old English lang "having a great linear extent, that extends considerably from end to end; tall; lasting," from Proto-Germanic *langa- (source also of Old Frisian and Old Saxon lang , Old High German and German lang , Old Norse langr , Middle Dutch lanc , Dutch lang , Gothic laggs "long").
 The Germanic words perhaps are from PIE *dlonghos- (source also of Latin longus "long, extended; further; of long duration; distant, remote," Old Persian darga- , Persian dirang , Sanskrit dirghah "long"), from root *del- (1) "long" (source also of Greek dolikhos "long," endelekhes "perpetual"). Latin longus (source of prolong , elongate , longitude , etc.) thus is probably cognate with, but not the source of, the Germanic words. The word illustrates the Old English tendency for short "a" to become short "o" before -n- (also retained in bond / band and West Midlands dialectal lond from land and hond from hand ).
 Also in Old English in reference to time, "drawn out in duration," with overtones of "serious." The old sense of "tall" now appears to be dialectal only, or obsolete. For long "during a long time" is from c. 1300. To be long on something, "have a lot" of it, is from 1900, American English slang. A long vowel (c. 1000) originally was pronounced for an extended time. Mathematical long division is from 1808. Sporting long ball is from 1744, originally in cricket. Long jump as a sporting event is attested from 1864. A long face , one drawn downward in expression of sadness or solemnity, is from 1786. Long in the tooth (1841 of persons) is from horses showing age by recession of gums (but not in this sense until 1870). Long knives , name Native Americans gave to white settlers (originally in Virginia/Kentucky) is from 1774, perhaps a reference to their swords. Long time no see , supposedly imitative of American Indian speech, is first recorded 1919 as Chinese English.
 belongings (n.) 
 "goods, effects, possessions," 1817, from plural of verbal noun from belong .
 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 More to explore
 go 
 Old English gan "to advance, walk; depart, go away; happen, take place; conquer; observe, practice, exercise," from West Germanic *gaian (source also of Old Saxon, Old Frisian gan, Middle Dutch gaen, Dutch gaan, Old High German gan, German gehen), from PIE root *ghē- "to release,
 pertain 

######## a17e718b3bca4163
STATUS: 200
TITLE: Timber - Etymology, Origin & Meaning

URL: https://www.etymonline.com/word/timber
FETCHED: 2026-09-05T17:58:14Z
STATUS: 200
TITLE: Timber - Etymology, Origin & Meaning
Timber - Etymology, Origin & Meaning 
 Search 
 Log in 
 Columns 
 Forum 
 Apps 
 Premium 
 Log in 
 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Origin and history of timber 
 timber (n.) 
 Middle English timber "wood cut and prepared for use as building material; wood suitable for making houses or ships or for carpentry;" from Old English timber , originally "building, structure," in late Old English "building material, growing trees yielding wood suitable for building," and by extension "trees or woods in general."
 This is reconstructed to be from Proto-Germanic *tem(b)ra- (source also of Old Saxon timbar "a building, room," Old Frisian timber "wood, building," Old High German zimbar "timber, wooden dwelling, room," Old Norse timbr "timber," German Zimmer "room"), according to Watkins from PIE *deme- "to build," possibly a form of the root *dem- meaning "house, household" (source of Greek domos , Latin domus ).
 For timbers in nautical slang expressions, see shiver (v.2)); the meaning is "pieces of wood composing the frames of a ship's hull" (1748). Slang timber-toes "wooden-legged man" is by 1785.
 The timber-wolf (1846), ordinary large wolf of the U.S. West, is the gray wolf, not confined to forests but so-called to distinguish it from the prairie-wolf (coyote). Timberdoodle , colloquial name for the American woodcock, is attested by 1889; earlier the name of an alcoholic drink (1842).
 timber (v.) 
 Old English timbran , timbrian , "to build," verb from the source of timber (n.). It was the chief Old English word for "to build," but now is obsolete in this sense. Compare Dutch timmeren , German zimmern . As "furnish with timber" from 1570s. As a call of warning when a cut tree is about to fall, attested from 1912 in Canadian English. Related: Timbered "wooded, having trees" (1701).
 Entries linking to timber 
 shiver (v.2) 
 "to break in or into many small pieces; to burst, fly, or fall apart at once into many pieces," mid-14c., shiveren , from shiver (n.2) or its source.
 Chiefly in the phrase shiver my timbers (1794), "a mock oath attributed in comic fiction to sailors" [OED]. Start my timbers in the same sense is by 1775; smite my timbers by 1782; split by 1786; burst by 1791). My timbers! as a nautical oath is attested by 1775, and timber (n.) "pieces of wood composing the frames of a ship's hull" seems to have been 18c. sailor's slang for "arms and legs" (perhaps with a grim awareness that some of theirs might be of wood after a sea-battle; compare timber-toe "wooden leg," in Grose). Related: Shivered ; shivering .
 build (v.) 
 Middle English bilden , from late Old English byldan "construct a house," verb form of bold "house," from Proto-Germanic *buthla- (source also of Old Saxon bodl , Old Frisian bodel "building, house"), from PIE *bhu- "to dwell," from root *bheue- "to be, exist, grow."
 Rare in Old English; in Middle English it won out over the more common Old English timbran (see timber ). The modern spelling is unexplained. Figurative use is from mid-15c. Of physical things other than buildings from late 16c. Related: Builded (archaic); built ; building .
 In the United States, this verb is used with much more latitude than in England. There, as Fennimore Cooper puts it, everything is BUILT. The priest BUILDS up a flock; the speculator a fortune; the lawyer a reputation; the landlord a town; and the tailor, as in England, BUILDS up a suit of clothes. A fire is BUILT instead of made, and the expression is even extended to individuals, to be BUILT being used with the meaning of formed. [Farmer, "Slang and Its Analogues," 1890]
```


## [2026-09-05T17:58:24.851Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && awk '/^ Persian$/{f=1} f' 7113dcda57f1193f.txt | grep -v \"^ *$\" | sed -n '1,40p'; echo \"=== madam persian ===\"; awk '/^ Persian$/{f=1} f' 2be76f2bdfcfbc08.txt | grep -v \"^ *$\" | sed -n '1,25p'"
}
```


### [2026-09-05T17:58:26.842Z] TOOL RESULT

```
 Persian
 [ edit ] 
 Persian Wikipedia has an article on: دیر 
 Wikipedia fa 
 Etymology 1
 [ edit ] 
 From Middle Persian 𐫅𐫃𐫡 ( dgr /⁠daǧr⁠/ ) , 𐫅𐫏𐫡 ( dyr /⁠dēr⁠/ ) , from Old Persian 𐎭𐎼𐎥 ( d-r-g /⁠darga⁠/ , “ long ” ) , from Proto-Iranian *dr̥Hgáh , from Proto-Indo-Iranian *dr̥Hgʰás , from Proto-Indo-European *dl̥h₁gʰós . [ 1 ] 
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /ˈdeːr/ 
 ( Dari, formal ) IPA ( key ) : [d̪eːɾ] 
 ( Dari, formal ) IPA ( key ) : [d̪eːɾ] 
 ( Kabuli ) IPA ( key ) : [d̪eːɾ] 
 ( Hazaragi ) IPA ( key ) : [d̪eːɾ] 
 ( Iran, formal ) IPA ( key ) : [d̪iːɹ] 
 ( Tajik, formal ) IPA ( key ) : [d̪eɾ] 
 Rhymes: -eːr 
 Readings
 Classical reading ? 
 dēr
 Dari reading ? 
 dēr
 Iranian reading ? 
 dir
 Tajik reading ? 
 der
 Adjective
 [ edit ] 
 دیر • ( dēr / dir ) ( comparative دیرتَر , superlative دیرتَرین , Tajik spelling дер ) 
 late ; tardy 
 Antonym: زود ( zūd  / zud ) 
 long ( of time ) 
 Inflection
 [ edit ] 
 Predicative forms of دیر ( dir ) 
 singular
 plural
 1 st person
(“I am, we are”)
 دیرم ( diram ) 
=== madam persian ===
```


## [2026-09-05T17:58:36.864Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c \"\" MON_part1.txt MON_part2.txt; grep -n \"مادام\" MON_part1.txt MON_part2.txt | head -10"
}
```


### [2026-09-05T17:58:36.940Z] TOOL RESULT

```
MON_part2.txt:94500
MON_part1.txt:99339
MON_part1.txt:14568:مادام العمر به کسی دادن. 
MON_part1.txt:65640:خاص که در ۱۸۹۸ به وسلهة مادام کوری و 
MON_part1.txt:68092:داده شود که مادام‌العمر از آن بهر من شو د. 
MON_part1.txt:74486:متوسط بین مبداً و منتهی است مادام که در 
MON_part1.txt:79161:فردی مادام العمر در راس آن قرار دارد. 
MON_part1.txt:79166:نمایندگان وی مادام العمر به سلطنت انتخاب 
MON_part1.txt:84763:شامیانه. سایبان. زه کمان مادام که بر کمان 
MON_part1.txt:91169:محمول» مادام که ذات موصوع موجود 
MON_part1.txt:93728:کجاوه. زن مادام که در هودج باشد (غم.)) 
MON_part1.txt:97834:شیثیت شی بدان است چنانکه مادام که
```


## [2026-09-05T17:58:44.560Z] TOOL CALL #77: Bash

```json
{
 "command": "for u in \"https://www.etymonline.com/word/madam\" \"https://www.etymonline.com/word/dungeon\" \"https://abadis.ir/fatofa/%D9%85%D8%A7%D8%AF%D8%A7%D9%85/\" ; do python3 tools/fetch_source.py \"$u\" --note \"page 116 verification (Dem/Domu: madame, dungeon, Persian مادام)\"; done"
}
```


### [2026-09-05T17:58:50.816Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/d54338d0e312d7c9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/829af26fbf3aca3b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/243fb357e117e9da.txt
```


## [2026-09-05T17:58:54.502Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### madam\"; grep -A4 \"madam (n.)\" d54338d0e312d7c9.txt | head -20; echo; grep -A3 \"madonna\" d54338d0e312d7c9.txt | head -12; echo \"### dungeon\"; grep -A6 \"dungeon (n.)\" 829af26fbf3aca3b.txt | head -14; echo \"### abadis madam\"; sed -n '3,5p' 243fb357e117e9da.txt; grep -n \"معین\\|فر\\.\" 243fb357e117e9da.txt | head -10"
}
```


### [2026-09-05T17:58:54.618Z] TOOL RESULT

```
### madam

 c. 1300, formal term of address to a lady (a woman of rank or authority, or the mistress of a household), from Old French ma dame, literally "my lady," from Latin mea domina (see Donna , and compare madonna ). It became a conventional term of address to women of any degree (but chiefly to the married and matronly); also "a woman of fashion or pretension" (often with a suggestion of disparagement) by 1590s. From 1719 as "a courtesan, a prostitute;" the meaning "female owner or manager of a brothel" is attested by 1871.

 The title of Madam is sometimes given here, and generally in Charleston (S. Carolina), and in the South, to a mother whose son has married, and the daughter-in-law is then called Mrs. By this means they avoid the inelegant phraseology of old Mrs. A., or the Scotch, Mrs. A senior. [Sir Charles Lyell, "A Second Visit to the United States of North America," 1849]
 also from c. 1300 
--
 madonna (n.) 

 1580s, Italian title of address or courtesy, equivalent to madam ; from c. 1600 as a noun, "an Italian lady," from Italian madonna , from Old Italian ma donna (Italian mia donna ) "my lady," from ma "my" + donna "lady," from Latin domina "lady, mistress of the house," from Latin domus "house" (from PIE root *dem- "house, household").

 Often specifically "the Virgin Mary," hence the sense of "picture or statue of the Virgin Mary," attested in English by 1640s. The U.S. singer/dancer (full name Madonna Louise Ciccone, b. 1958) attained to pop stardom in the fall of 1984.

### dungeon
 dungeon (n.) 

 c. 1300, "great tower of a castle," from Old French donjon "great tower of a castle" (12c.), from Gallo-Roman *dominionem , from Late Latin dominium , from Latin dominus "master" (of the castle), from domus "house" (from PIE root *dem- "house, household"), so called probably for its commanding position or strength. Sense of "castle keep" led to that of "strong (underground) cell" in English early 14c. The original sense went with the variant donjon .
 also from c. 1300 

 Entries linking to dungeon 

### abadis madam
STATUS: 200
TITLE: مادام - معنی در دیکشنری آبادیس

41: مادام. ( فرانسوی ، اِ ) کلمه فرانسوی است بمعنی بی بی. خانم. بانو. بیگم. خاتون. ( یادداشت به خط مرحوم دهخدا ). بانو. خانم. ( فرهنگ فارسی معین ) : 
50: فرهنگ معین
53: [ فر. ] (اِ. ) خانم ، بانو، در خطاب به بانوان شوهردار غیر مسلمان . 
101: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد.
```


## [2026-09-05T17:59:07.772Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KLN long ==\"; grep -n \"OE\\. lang\\|long, adj\\|Goth\\. laggs\" KLN_1966.txt KLN_1971.txt | head -6; echo \"== KLN madonna/donna ==\"; grep -n \"madonna\\|Madonna\" KLN_1966.txt KLN_1971.txt | head -5; echo \"== SKT oblong ==\"; grep -n \"OBLONG\\|PROLONG\\|LONGITUDE\" SKT.txt | head -6"
}
```


### [2026-09-05T17:59:07.873Z] TOOL RESULT

```
== KLN long ==
KLN_1971.txt:11756:long, adj., and cp. longeron, lunge, 
KLN_1971.txt:12108:anti-. For the second element see long, adj. 
KLN_1971.txt:28094:See long, adj., and cp. along. 
KLN_1971.txt:74991:with L. longus see long, adj. 
KLN_1971.txt:80635:‘far off’, adv. of longus , ‘long’. See long, adj., 
KLN_1971.txt:98690:row’, and lang, ‘Jong’. See furrow and long, adj. 
== KLN madonna/donna ==
KLN_1971.txt:75403:' fr. L. domina. See dame and cp. Madonna. Cp. 
KLN_1971.txt:142502:Madonna, n. — It. madonna , fr. Olt. ma donna 
KLN_1966.txt:12075:Derivative:  donnish-ness,  n. donor,  n.  —  AF.  donour,  corresponding  to  OF. doneur  (F.  donneur),  fr.  L.  donatdrem,  acc.  of donator,  ‘giver,  donor’,  fr.  donatus,  pp.  of  donare. See  donation  and  agential  suff.  -or. donna,  n.,  an  Italian  title  given  to  a  lady.  - —  It., fr.  L.  domina.  See  dame  and  cp.  Madonna.  Cp. also  Dona,  duenna.
KLN_1966.txt:22496:Madonna,  n.  —  It.  madonna,  fr.  Olt.  ma  donna (=  It.  mia  donna),  ‘my  lady’,  for  L.  mea  domina, ‘my  lady’.  See  madam  and  donna, madrague,  n.,  a  large  fishpond.  —  F.  madrague, fr.  Proven?,  madruga,  fr.  Sp.  almadraba,  fr. Arab.  almdzrabah ,  ‘the  enclosure’,  which  is formed  fr.  al-,  ‘the’,  and  mazrabah,  ‘enclosure’, fr.  zaraba,  ‘he  made  an  enclosure’, madras,  n.,  a  light  cotton  fabric.  —  So  called from  Madras,  in  India.
== SKT oblong ==
```


## [2026-09-05T17:59:14.507Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== SKT ==\"; grep -n \"^Oblong\\|Oblong\\.\\|Prolong\\|Longitude\\|Long, extended\" SKT.txt | head -6; echo \"== LEW dominus ==\"; grep -n \"dominus\" LEW_1910.txt | head -5; echo \"== LAT domus ==\"; grep -n \"domus\\b\" LAT.txt | head -5"
}
```


### [2026-09-05T17:59:14.590Z] TOOL RESULT

```
== SKT ==
12572:Oblong:  see  Long  (i).
== LEW dominus ==
== LAT domus ==
175:itait 1'uniti principale, domus et fores,- etc., reprisentent
181:des biens, non des termes d'ileveurs; de mime, domus et
2016:e.g. Enn., Tr.113, inter se sortiunt urbem, et agros, et k domus. Sp^cia-
10173:(d*aprbs domus?) - Ancien, usuel. Panroaan, M.L. 1738; gera. : westph.
11020:cenitare coeperunt , superioris domus uniuersa cenacula dicta , Varr.
```


## [2026-09-05T17:59:19.543Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"longus, -a, -um\\|longus :\\|longus,-a\\|dominus, -i\\|dominus :\" LAT.txt | head -6; echo ===; grep -n \"domus, -us\\|domus :\" LAT.txt | head -4"
}
```


### [2026-09-05T17:59:19.600Z] TOOL RESULT

```
Exit code 1
(eval):1: == not found
```


## [2026-09-05T17:59:21.717Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"longus\" LAT.txt | head -8"
}
```


### [2026-09-05T17:59:21.769Z] TOOL RESULT

```
7708:A longus. En grammaire et en rh6torique breuis subst. d6signe "la
32315:suppiante latus grace a 1 1 appui -de longus avec lequel il formait
34565:g osta supposent une forme avec n, deformation populaire d'aprbs longus ?
34596:longus. Varro Triphallo 7iepl appevoTr]TOS (569): "ego nihil Varro uideo:
34598:Senble deriv^ de longus, d^pres le type des deaideratifs en -urio;
34600:longus, -a, -uin: long. Se dit de 1 'espace et du temps, comme le
34604:511C. C’est sur longe, et non sur longus, qu'est forne longinquus
34612:(Vulg.Ambr.), M.L.3853 (e- et all~); perlongus (familier, rare),
```


## [2026-09-05T17:59:23.867Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '34600,34650p' LAT.txt"
}
```


### [2026-09-05T17:59:23.925Z] TOOL RESULT

```
longus, -a, -uin: long. Se dit de 1 'espace et du temps, comme le
gr.p,cotpoc dont il a tous lea sena. Usite de tout temps. Panroman,
M.1.5119. En iri. long, gall. llong, de longa ( nauis ), "vaisseau".
Derives et composes: longe (et longiter) "loin" et "de loin", M.L.
511C. C’est sur longe, et non sur longus, qu'est forne longinquus
"qui ae trouve au loin, eloigne", M.L.suGa, cf. prope, propinquus.
De la longinquitas, et a basse epoque longinquS,-as ; elonginquo
(ital. Ambr.); longulus "longuet", longitudS (cf. altitudo, latitudo) ;
longitia (b.lat., cf. latitia); longisco,-is Enn. ap.Non.134,19; lon-
gitrorsus, sic dicitur sicut dextrorsus, sinistrorsus , PiF.107,11;
longiturnus,-turnitas (Vulg.Cassiod.) formes sur diuturnus; longi-
tanus, cf.M.L.5118; elongo,-as: allonger; et "eloigner, 8'eloigner"
(Vulg.Ambr.), M.L.3853 (e- et all~); perlongus (familier, rare),
M.L.G41G; longo, et longio, -as (tardifs); longina trad. de
"sorte de fougere" (Diosc.), longisecus : 7ioppoo0ev (Gl.); prolongo
(l. de 1'figl.) pour profero, prorogo.
longaeuus (poet., cf. grandaeuus), ne semble pas attest^ avant Vg.,
peut-etre simple traduction du gr. p, 09 cpai,(jov, |icocpo( 3 l.OG, comme le subst.
tardif longaeuitds (Macr.Ambr.) traduit p,OKpoj 3 (Aristt.); cf.
longiuiuax (Schol.Iuu. ), longanimis,-itas,-iter, non attest 4 s avant
la Vulg. et Cassiod., et traduits de |ia>cpo8up,oc;, -8u(H,<x, eux-memes
tardifs en grec, et usuels dans la 1 . du Nouveau Testament; longimanus
(= (icotpoxei,p), longipes (Plin.), etc.
Cf.got. laggs "long"; le caractfere du rapport avec iri. long "long"
(et gaul.Xoyy 0- dans un non propre?) est discute. Autre mot dans la
partie orientale de 1 1 indo-enropeen: akr .dirghal}, v.sl. dlugH, gr.
80X1, et hitt. dalugae$ (pl.) "longa". Pour longinquus, cf. antiquus,
et oculus.
lop&da, -ae f.: patelle, genus conchae marinae, cf. Non.551,3.
Emprunt oral et populaire fait aur l'acc. du gr. Xeraxc.
loquor,-eris, locutus sum, loqui: parier, a'exprimer; neque loquilora
653 “
possumus nisi e syllabis breuibus ac longis, Quint.4,9,61. S'emploie
absolument, on avec nn coapldaent "parier de", et avec un sens p^jo-
ratif "ne parier que de", d'ou loquSx "bavard", loquScitas, loquaculus.
A remplac^ dans la 1 . usuelle fari, correspond a gr. cppa^u). Cic. et
Quint. opposent loqui qui se dit de la conversation 1 dicere qui se
dit du discours oratoire, cf. s.u. dico) et Quint. 13 , 6 , omisso tumore
in quibusdam causis loquendum est. Toutefois ce sont les compos^s de
loquor qui ont servi a traduire les teraes grecs relatifs a la rhe¬
torique, parce que les coaposes de dico etaient d£ja eaploy^s dans
des acceptions speciales, cf. edico, edictum, praedico. Ainsi le compose
Sloquor "dire tout en pariant" (defini copiose loqui, Varr., L.L.6,57)
ou "expriaer par la parole" a pris le sens de "parier avec art ou-
^loquence", de 14 eloquens, eloquentia (non aftest£ avant Cic.), et
dans la poesie dactylique eloquium pour 4 viter le cretiquej elocutio
traduit le gr. cppootc (d'ou elocutilis (Apul.), e locutor ius, elocutrix)',
circumlocutio, 7 iepicppaaic; proloquium, praelocutis, npoXoyoi'
Autres derives et coaposes: loquitor,-aris (fr 4 quentatif arch.);
loquela (arch. et poet.): parole (cf. querela), peut-etre conservi dans
quelques dialectes italiens, M.L. 5133, et loquelaris (gramn.); locutio:
```


## [2026-09-05T18:00:45.995Z] TOOL CALL #84: Bash

```json
{
 "command": "for u in \"https://www.etymonline.com/word/oblong\" \"https://www.etymonline.com/word/dome\" \"https://www.etymonline.com/word/along\" \"https://www.etymonline.com/word/don\"; do python3 tools/fetch_source.py \"$u\" --note \"page 116 verification (Del/Dlgho, Dem/Domu English nodes)\"; done\ncd data/verification/sources/web && for f in $(ls -t *.txt | head -4); do echo \"### $f\"; sed -n '5p' $f; grep -m1 -A3 \"(n.)\\|(adj.)\\|(adv.)\" $f | head -6; done"
}
```


### [2026-09-05T18:00:49.168Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/c2588b125b74acd7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/450a647b506020e1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c60268ef5756f14d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1ea02f9b9e489194.txt
### 1ea02f9b9e489194.txt

 don (n.) 

 title of respect, 1520s, from Spanish or Portuguese Don , a title of respect prefixed to a man's Christian name, from Latin dominus "lord, master, owner" (from domus "house," from PIE root *dem- "house, household").

### c60268ef5756f14d.txt

 Middle English, from Old English andlang "entire, continuous; extended" (adj.); also "alongside of" (prep.); from and- "opposite, against" (from Proto-Germanic *andi- , *anda- , from PIE *anti "against," locative singular of root *ant- "front, forehead") + lang "long" (see long (adj.)).

 Reinforced by its Old Norse cognate endlang . The prepositional sense was extended in Old English to "through the whole length of." Of position, "lengthwise," from c. 1200; of movement, "onward," from c. 1300. The meaning "in company, together" is from 1580s. All along "throughout" is attested from 1690s.

### 450a647b506020e1.txt

 dome (n.) 

 "a round, vaulted roof, a hemispherical covering of a building," 1650s, from French dome "a town-house; a dome, a cupola" (16c.), from Provençal doma , from Greek dōma "a house, housetop" (especially in reference to a style of roof from the east), related to domos "house," from PIE root *dem- "house, household."

### c2588b125b74acd7.txt

 oblong (adj.)
```


## [2026-09-05T18:09:15.553Z] TOOL CALL #85: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk116.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\nPIE_DOM = W + \"Reconstruction:Proto-Indo-European/d%E1%B9%93m\"\nPIE_DLG = W + \"Reconstruction:Proto-Indo-European/dl%CC%A5h%E2%82%81g%CA%B0%C3%B3s\"\nDERAZ  = W + \"%D8%AF%D8%B1%D8%A7%D8%B2\"\nDUDMAN = W + \"%D8%AF%D9%88%D8%AF%D9%85%D8%A7%D9%86\"\nDERANG = W + \"%D8%AF%D8%B1%D9%86%DA%AF\"\nDIR    = W + \"%D8%AF%DB%8C%D8%B1\"\nGARZ   = W + \"%DA%AF%D8%B1%D8%B2%D9%85%D8%A7%D9%86\"\nMADAM_W= W + \"%D9%85%D8%A7%D8%AF%D8%A7%D9%85\"\nE = \"https://www.etymonline.com/word/\"\nABADIS = \"https://abadis.ir/fatofa/%D9%85%D8%A7%D8%AF%D8%A7%D9%85/\"\n\ndoc = {\n \"pdf_page\": 116,\n \"book_page\": 86,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Del, Dlgho\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *del(h1)- 'long', with the extensions *delh1gh- / *dl̥h1ghós and *dlonghos 'long'\",\n   \"note\": \"Pokorny pp. 196-197 has 'Root/lemma: del-5, Meaning: long', with the note that it is 'probably the basis for the widespread extension delegh-, dl̥ngho-'; Watkins/AHD has 'del-1. Long. Probably extended and suffixed zero-grade form *dlon-gho-. [Pok. 5. del- 196.]'. Nourai's two-part root name Del / Dlgho reproduces exactly this pair, the language label (Indo-European) and the gloss 'long' are right. Modern reconstruction writes the laryngeal: *dl̥h1ghós (Skt. dīrghá-, Av. darəγa-, OP darga-) beside *dlonghos (Lat. longus, Gmc. *langaz, MP drang); Wiktionary notes that 'resemblance to the synonym *dlonghos is conspicuous and probably not by coincidence, but a formal connection is difficult, due to the presence of the laryngeal in one but not the other' - a nuance Nourai's single box hides but does not falsify.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *del(h₁)- «دراز» و گسترش‌های آن *dl̥h₁gʰós و *dlongʰos؛ پوکورنی (ص ۱۹۶-۱۹۷) آن را del-5 «long» آورده و خود یادآور شده که پایهٔ گسترش delegh-/dl̥ngho- است، و واتکینز در پیوست AHD نیز همین را دارد. پس نام دوگانهٔ «Del, Dlgho» نزد نورایی، برچسب زبانی (هندواروپایی) و معنی «دراز» هر سه درست است. تنها نکتهٔ امروزی این است که دو صورت *dl̥h₁gʰós (سرچشمهٔ سنسکریت dīrghá-، اوستایی darəγa-، پارسی باستان darga-) و *dlongʰos (سرچشمهٔ لاتینی longus، ژرمنی *langaz، فارسی میانه drang) را به سبب حضور حنجری در یکی و نبودش در دیگری به‌آسانی نمی‌توان به یک قالب واحد برگرداند. ادعای نورایی درست است.\",\n   \"sources\": [PIE_DLG, DERAZ, DERANG],\n   \"ref_check\": [\n     {\"ref\": \"POK:197\", \"status\": \"supports\", \"note\": \"POK_full.txt (Pokorny IEW) 'Root / lemma: del-5 / Meaning: long ... Note: ... probably the basis for the widespread extension delegh-, (d)longho-' ... 'delegh-, dl̥ngho-: zero grade Old Indic dīrgha- = Avestan daraga-, daraγa-, Old pers. darga- \\\"long\\\"' ... 'References: WP. I 812 f. ... Page(s): 196-197' (grep -n 'Root / lemma: del-5' POK_full.txt, line 17699).\"},\n     {\"ref\": \"KNT:190\", \"status\": \"supports\", \"note\": \"KNT.txt (Kent, Old Persian, Lexicon): 'darga- adj. \\\"long\\\": GAv. daraga-, LAv. darəγa-, NPers. dēr, Skt. dīrghá-, pIE *dlgho-, cf. Gk. dolikhés, Lt. longus'. The Lexicon is alphabetised in Old Persian order (d before b, m), so the d-entries fall around pp.189-191 - p.190 is the right page (the neighbouring m-entries carry printed page numbers 201/202 in the same file).\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"POK\", \"where\": \"pp. 196-197 s.v. del-5\", \"stance\": \"supports\", \"note\": \"'/d/longho-s: a) Middle Persian drang, npers. dirang \\\"long\\\" ... b) Latin longus ..., Gothic laggs, Old English Old High German ... lang'.\"},\n     {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. del-1\", \"stance\": \"supports\", \"note\": \"'del-1. Long. Probably extended and suffixed zero-grade form *dlon-gho-. 1. Germanic *langaz ... 3. Latin longus ... 4. Possibly suffixed variant *dlo-gho- in Greek dolikhos. [Pok. 5. del- 196.]'\"},\n     {\"src\": \"SYN\", \"where\": \"Buck 12.57 'long'\", \"stance\": \"supports\", \"note\": \"'Grk. dolikhós ... ChSl. dlŭgŭ, SCr. dug, etc.; Skt. dīrgha-, Av. daraga-, OPers. darga-; Baltic with loss of d-, Lith. ilgas ...; Hitt. dalugaeš (pl.), with sb. dalugasti \\\"length\\\".'\"},\n     {\"src\": \"WLD\", \"where\": \"cited by Pokorny as WP. I 812 f.\", \"stance\": \"supports\", \"note\": \"Pokorny's own reference line for del-5 points to Walde-Pokorny I 812 f.; the Bd. I text itself was not opened for this root (only Bd. 3 index is on disk in full).\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"daraga, daragâ, drâjah; drang\", \"verdict\": \"plausible\",\n     \"derivation\": \"Gathic Avestan daraga-, Younger Avestan darəγa- 'long' (fem. darəγā-) is the regular Iranian outcome of PIE *dl̥h1ghós: syllabic *l̥ > Ir. ar, and the voiced aspirate *gh > Av. g/γ intervocalically (Bartholomae AiWb 693 s.v. 'd. p. darga-, g. daraga-, j. darəγa- Adj. (fem. °γā-) \\\"lang\\\"'). Beside it Avestan has the s-stem drāj- / drājah- 'length, extent' (only in compounds such as ayarə.drājah- 'the duration of a day', asə.drājahyehe, mazdrājah-), the zero-grade *dr̥Hǰ-as- of the same root, which is the ancestor of NP derāz. The third word Nourai lists here, drang 'hesitation', is the problem: Bartholomae's two Avestan verbs drang- are '1drang- V. firmare' and '2drang- V. \\\"auswendig lernen\\\"' (to fix, to learn by heart) - not 'hesitation'; the form with the sense 'delay, period of time' is Middle Persian drang (Pokorny explicitly files it under */d/longho-s: 'Middle Persian drang, npers. dirang'), and Wiktionary derives NP درنگ from MP dlng' (drang) 'period, duration' via Old Persian, not from Avestan. Nourai's source for putting drang in the Avestan box is Tavoosi (SNS 324), who does refer the Pahlavi word back to Av. drang- (AiWb 772); that is a defensible but minority link, so: forms 1-3 confirmed, drang mislabelled Avestan and mis-glossed.\",\n     \"derivation_fa\": \"اوستایی daraga- (گاهانی) / darəγa- (اوستای نو) «دراز» بازتاب منظم ایرانی *dl̥h₁gʰós هندواروپایی است: لِ هجایی به ar بدل شده و *gʰ در میان دو واکه در اوستایی g/γ داده است (بارتولمه، ستون ۶۹۳). در کنار آن ستاک drāj-/drājah- «درازا، امتداد» (تنها در ترکیب‌هایی چون ayarə.drājah- «درازای یک روز») هست که پایهٔ «دراز» فارسی است. اما واژهٔ سوم، drang «درنگ»، جای چون‌وچرا دارد: بارتولمه دو فعل اوستایی drang- را «استوار کردن» و «از بر کردن» معنی می‌کند، نه «درنگ»؛ صورتی که معنی «مدت، درنگ» دارد فارسی میانهٔ drang است و پوکورنی هم آن را زیر *dlongʰos آورده است («فارسی میانه drang، فارسی نو dirang»). طاوسی در واژه‌نامهٔ شایست‌نشایست (ص ۳۲۴) درنگِ پهلوی را به drang- اوستایی (بارتولمه ۷۷۲) برمی‌گرداند و ظاهراً مأخذ نورایی همین است. پس سه صورت نخست تأیید می‌شود و «drang» با احتیاط: برچسب زبانی و معنی آن نادرست است.\",\n     \"sources\": [PIE_DLG, DERANG, DERAZ],\n     \"ref_check\": [\n       {\"ref\": \"POK:197\", \"status\": \"supports\", \"note\": \"Pokorny pp.196-197: 'zero grade Old Indic dīrgha- = Avestan daraga-, daraγa-, Old pers. darga- \\\"long\\\" ... Avestan drajō Adv. \\\"further\\\" ... Avestan drāj- \\\"stretch, length\\\"'. The same page files drang under Middle Persian, not Avestan.\"},\n       {\"ref\": \"BQT:829\", \"status\": \"partial\", \"note\": \"In the scan (BQT_v2_pages.txt, leaf 289 ≈ printed p.831; the running head two leaves earlier reads ۲۲۴ = continuous 829) Mo'in's footnote 7 to دراز reads 'اوستا drājah- (طول). پهلوی drāj ... بلوچی drāj و drāz ... نیز در پهلوی drang «معین ۲:۱۷۲»'. It gives Avestan drājah- and Pahlavi (not Avestan) drang - i.e. it supports the Avestan drājah- but contradicts the Avestan label on drang.\"},\n       {\"ref\": \"SNS:324\", \"status\": \"supports\", \"note\": \"SNS.txt (Tavoosi, Glossary of Šāyast nē Šāyast), entry on p.324: 'درنگ drang: ... (AiWb. 772) drang-: cf. Zaehner, BSOS IX, 1938 pp. 319 and 584' - Tavoosi does refer Pahlavi drang to an Avestan drang-, which is exactly Nourai's arrow.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"BRT\", \"where\": \"AiWb col. 693 (darga-/daraga-/darəγa-) and cols. 1416 f. (1drang-, 2drang-)\", \"stance\": \"partial\", \"note\": \"col. 693 'd. p. darga-, g. daraga-, j. darəγa- Adj. (fem. °γā-) \\\"lang\\\"'; but the drang- headwords are '• j., g. 1drang- V. \\\"firmare\\\"' and '• j. 2drang- V. \\\"auswendig lernen\\\"' - no sense 'hesitation'.\"},\n       {\"src\": \"KNT\", \"where\": \"p. 190 s.v. darga-\", \"stance\": \"supports\", \"note\": \"'darga- adj. \\\"long\\\": GAv. daraga-, LAv. darəγa-, NPers. dēr, Skt. dīrghá-, pIE *dlgho-'.\"},\n       {\"src\": \"HRN\", \"where\": \"no. 547, pp. 121-122\", \"stance\": \"supports\", \"note\": \"'547. dirāz \\\"lang\\\" ... aw. drajah- \\\"Länge\\\"; phlv. drāj, drājīh ... kurd. dirīz; bel. drōj'.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\", \"words\": \"derâz «دراز»; dîr «دیر»; derang «درنگ»\", \"verdict\": \"confirmed\",\n     \"derivation\": \"All three are the New Persian continuants of this root, though by three different Old Iranian stems. (1) دراز derāz < MP drāz (Book Pahlavi dlʾc), from the s-stem *drāǰah- < Proto-Iranian *draHǰáh < PII *draHǰhas < PIE *dl̥h1ghós - Horn no. 547 already set up 'aw. drājah- \\\"Länge\\\"; phlv. drāj, drāzīh', and Mo'in repeats it in the Borhān footnote; Balochi drāj/drāz and Kurdish dirīz are the sister forms. (2) دیر dēr 'late, long (of time)' < MP dēr / Manichaean dgr (daγr), from OP darga- 'long' (< PIr *dr̥Hgáh); the OP -rg- gives MP -γr- > -yr- with compensatory lengthening of the vowel, whence dēr > modern dir. Kent states the equation flatly ('darga- ... NPers. dēr'), and Tavoosi (SNS p.182) glosses Pahlavi dēr with '(AiWb. 693) darga/darəja-'; Horn (no. 547) was the dissenter, insisting that NP dēr 'darf nicht direkt ap. darga-, aw. darəγa- gleichgesetzt werden' and attaching it instead to the drāj- family. (3) درنگ derang 'delay, length of time' < MP drang 'period, duration' < PIr *drangah < PIE *dlonghos, the nasal-infixed variant that also gave Latin longus and Gmc. *langaz. So the words, the meanings and the root are right; the only structural quibble is that Persian descends from Old Persian / Middle Persian, not from the Avestan forms drawn as the parent - the Avestan box stands here (as everywhere in Nourai) for Old Iranian in general.\",\n     \"derivation_fa\": \"هر سه واژه بازماندهٔ همین ریشه‌اند، اما از سه ستاک ایرانی باستانِ جداگانه. ۱) «دراز» از فارسی میانهٔ drāz (پهلوی کتابی dlʾc)، از ستاک *drāǰah- ایرانی باستان، از *dl̥h₁gʰós هندواروپایی؛ هرن (شمارهٔ ۵۴۷) همین را آورده: «اوستایی drājah- «درازا»؛ پهلوی drāj، drāzīh»، و معین در حاشیهٔ برهان قاطع نیز همین را تکرار کرده است (بلوچی drāj/drāz، کردی dirīz هم‌ریشه‌اند). ۲) «دیر» از فارسی میانهٔ dēr / dagr مانوی، از پارسی باستان darga- «دراز»؛ خوشهٔ -rg- در فارسی میانه به -γr-/-yr- بدل شده و واکه کشیده شده و dēr داده است که در فارسی امروز «دیر» تلفظ می‌شود. کنت این برابری را صریح آورده و طاوسی (شایست‌نشایست، ص ۱۸۲) نیز dēr پهلوی را به darga/darəja- (بارتولمه ۶۹۳) بازمی‌گرداند؛ تنها هرن با آن مخالف بود و «دیر» را به خانوادهٔ drāj- می‌بست. ۳) «درنگ» از فارسی میانهٔ drang «مدت، هنگام»، از *drangah ایرانی باستان، از *dlongʰos هندواروپایی - همان صورت خیشومی‌شده‌ای که longus لاتینی و *langaz ژرمنی هم از آن‌اند. پس ادعای نورایی درست است؛ تنها باید توجه داشت که فارسی از پارسی باستان/فارسی میانه می‌آید نه از اوستایی، و در نمودارهای نورایی «اوستایی» جانشین «ایرانی باستان» است.\",\n     \"sources\": [DERAZ, DIR, DERANG, PIE_DLG],\n     \"ref_check\": [\n       {\"ref\": \"POK:197\", \"status\": \"supports\", \"note\": \"'npers. drāz (actually comparative) \\\"long\\\"' and '/d/longho-s: a) Middle Persian drang, npers. dirang \\\"long\\\"' - Pokorny pp.196-197.\"},\n       {\"ref\": \"BQT:829\", \"status\": \"supports\", \"note\": \"Mo'in's footnote to دراز (BQT_v2_pages.txt leaf 289, printed ≈829-831): 'اوستا drājah- (طول). پهلوی drāj ... بلوچی drāj و drāz'.\"},\n       {\"ref\": \"BQT:841\", \"status\": \"supports\", \"note\": \"Mo'in's footnote 1 to درنگ (BQT_v2_pages.txt leaf 301, printed ≈843): 'پهلوی drang (دراز، آهسته) «معین ۱۷۲:۲» ... اوستا darəγahe ... «بارتولمه ۱۹۱۶» ... zrvan-darəγō.xᵛaδāta- (زروان (زمان) پایدار). رك: Henning, Sogdian/Central Asian Words'.\"},\n       {\"ref\": \"SNS:182\", \"status\": \"supports\", \"note\": \"SNS.txt: 'dēr: ... ← (AiWb. 693) darga/darəja-' (index lines 'dēr 182/13', 'darəja-/darga- 182/14', 'dīrgha- 182/14'), plus 'dērang zamān' on the same page.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"HRN\", \"where\": \"no. 547, pp. 121-122\", \"stance\": \"partial\", \"note\": \"supports derāz ('aw. drājah- \\\"Länge\\\"; phlv. drāj, drājīh') but explicitly rejects the direct equation of dēr with darga-: 'np. dēr ... das nicht ... direkt ap. darga- \\\"lang\\\", aw. darəγa-, ai. dīrghá- ... gleichzusetzen ist'.\"},\n       {\"src\": \"KNT\", \"where\": \"p. 190 s.v. darga-\", \"stance\": \"supports\", \"note\": \"'darga- adj. \\\"long\\\": GAv. daraga-, LAv. darəγa-, NPers. dēr'.\"},\n       {\"src\": \"BQT\", \"where\": \"Mo'in's footnotes, printed pp. ≈831 (دراز) and ≈843 (درنگ)\", \"stance\": \"supports\", \"note\": \"see ref_check; Balochi drāj/drāz, Kurdish dirīz, Ossetic and Caspian-dialect forms are listed there too.\"},\n       {\"src\": \"HUB\", \"where\": \"Persische Studien\", \"stance\": \"silent\", \"note\": \"grep for 'dirāz', 'dirang', 'dēr' in HUB.txt returned nothing (Hübschmann does not treat these words in the pages OCR'd here).\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Sanskrit\", \"words\": \"dîrğâ\", \"verdict\": \"plausible\",\n     \"derivation\": \"The word is Sanskrit dīrghá- (Nourai's ğ = gh, â = the final vowel of the stem), the exact eastern counterpart of Av. daraga-/OP darga-, from PIE *dl̥h1ghós with syllabic *l̥ > Indic īr and *gh preserved as gh; it is one of Pokorny's headline witnesses ('zero grade Old Indic dīrgha- = Avestan daraga-'). The derivation from the root is confirmed; what is wrong is the gloss: dīrghá- means 'long' (of space and of time), not 'late'. Nourai apparently carried over the gloss of the neighbouring Persian dīr 'late'. Buck 12.57 lists 'Skt. dīrgha-' as the ordinary word for 'long', and Kent, Wiktionary and Pokorny all agree.\",\n     \"derivation_fa\": \"این واژه همان dīrghá- سنسکریت است (در نویسه‌گردانی نورایی ğ = gh)، همتای شرقی daraga- اوستایی و darga- پارسی باستان، از *dl̥h₁gʰós هندواروپایی؛ لِ هجایی در هندی باستان īr داده و *gʰ به gh مانده است. پوکورنی خود آن را نمونهٔ شاخص می‌آورد: «صفر-درجه: هندی باستان dīrgha- = اوستایی daraga-». پس پیوند با ریشه تأیید می‌شود، اما معنی نادرست است: dīrghá- یعنی «دراز» (در مکان و زمان) نه «دیر/دیرهنگام»؛ ظاهراً نورایی معنی «دیر» فارسیِ کنار آن را به اشتباه به این واژه داده است. بنابراین با احتیاط پذیرفتنی است، به شرط اصلاح معنی.\",\n     \"sources\": [PIE_DLG, DIR],\n     \"ref_check\": [\n       {\"ref\": \"SNS:182\", \"status\": \"supports\", \"note\": \"SNS index: 'dīrgha- 182/14' - the Sanskrit form is indeed quoted on p.182 of Tavoosi's glossary, in the etymology of Pahlavi dēr, alongside 'darəja-/darga- 182/14'. It is quoted there with the value 'long', not 'late'.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"POK\", \"where\": \"p. 197 s.v. del-5\", \"stance\": \"supports\", \"note\": \"'zero grade Old Indic dīrgha- = Avestan daraga-, daraγa-, Old pers. darga- \\\"long\\\"'.\"},\n       {\"src\": \"SYN\", \"where\": \"Buck 12.57 'long'\", \"stance\": \"partial\", \"note\": \"'Skt. dīrgha-, Av. daraga-, OPers. darga-' are given under the concept LONG, not LATE - i.e. the derivation is right, Nourai's gloss is not.\"},\n       {\"src\": \"KNT\", \"where\": \"p. 190 s.v. darga-\", \"stance\": \"supports\", \"note\": \"'Skt. dīrghá-' cited as cognate of OP darga- 'long'.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Old Persian\", \"words\": \"darga\", \"verdict\": \"confirmed\",\n     \"derivation\": \"OP darga- 'long', attested in the Achaemenid inscriptions only in the adverbial accusative dargam 'for a long time' (DB 4.56, 4.75: utā-taiy taumā vasiy biyā utā dargam jīvā 'and may thy family be in abundance, and mayest thou live long'). Phonologically it shows the West-Iranian treatment of the zero grade *dl̥h1gh- : *dr̥Hgha- > darga-, with -rg- kept where Avestan lenites to -rγ-. Kent's lexicon entry is the standard reference and Nourai's page number is exact. From darga- descends MP dēr, NP دیر (node 2).\",\n     \"derivation_fa\": \"پارسی باستان darga- «دراز»، که در سنگ‌نبشته‌های هخامنشی تنها در صورت قیدی dargam «دیرزمانی» به کار رفته است (بیستون ۴:۵۶ «utā dargam jīvā» = «و دیر زی»). از نظر آوایی صورتِ صفرْدرجهٔ *dr̥Hgʰa- است که در فارسیِ باستان خوشهٔ -rg- را نگه داشته، حال آنکه اوستایی آن را به -rγ- نرم کرده است. مدخل کنت (ص ۱۹۰) مرجع استاندارد این واژه است و ارجاع نورایی دقیق است. بازماندهٔ آن فارسی میانهٔ dēr و «دیر» فارسی نو است. ادعای نورایی درست است.\",\n     \"sources\": [DIR, PIE_DLG],\n     \"ref_check\": [\n       {\"ref\": \"KNT:190\", \"status\": \"supports\", \"note\": \"'darga- adj. \\\"long\\\": GAv. daraga-, LAv. darəγa-, NPers. dēr, Skt. dīrghá-, pIE *dlgho-, cf. Gk. dolikhés, Lt. longus (§81, §68, §101, §148.II, VI). dargam asn. as adv. \\\"for a long time\\\" DB 4.56, 15.'\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KNT\", \"where\": \"p. 190; texts DB 4.56, 4.75\", \"stance\": \"supports\", \"note\": \"see ref_check; the running text 'uta dargam jiva' is printed in Kent's DB text at 4.56.\"},\n       {\"src\": \"POK\", \"where\": \"p. 197\", \"stance\": \"supports\", \"note\": \"'Old pers. darga- \\\"long\\\"' listed with Skt. dīrgha- and Av. daraga-.\"},\n       {\"src\": \"TLM\", \"where\": \"Ancient Persian Lexicon\", \"stance\": \"silent\", \"note\": \"not opened for this node; Kent supersedes Tolman for the OP lexicon and gives the citation Nourai used.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Germanic\", \"words\": \"langaz\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Proto-Germanic *langaz 'long', the western reflex of *dlonghos with the regular West-IE loss of the initial d- of the cluster dl- (Pokorny: 'In the group b) would display an already common West Indo Germanic simplification'), and *o > Gmc. a; it yields Gothic laggs, Old Norse langr, Old Saxon/Old High German lang, Old English lang/long. Watkins reconstructs exactly 'Germanic *langaz, long' under del-1. The same simplification is seen in Baltic (Lith. ilgas) where the d- is lost altogether.\",\n     \"derivation_fa\": \"ژرمنی آغازین *langaz «دراز»، بازتاب باختری *dlongʰos است: خوشهٔ آغازین dl- در شاخهٔ باختری هندواروپایی ساده شده و d افتاده است (پوکورنی خود این ساده‌شدن را «ساده‌شدن مشترک هندواروپایی باختری» می‌نامد) و *o ژرمنی a داده است. بازماندهٔ آن گوتی laggs، نُرس باستان langr، ساکسون باستان و آلمانی علیای باستان lang و انگلیسی باستان lang/long است. واتکینز نیز در پیوست AHD همین *langaz را زیر del-1 آورده است. ادعای نورایی درست است.\",\n     \"sources\": [E + \"belong\", PIE_DLG],\n     \"ref_check\": [\n       {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. del-1: '1. Germanic *langaz, long, in: a. Old English lang, long, long (comparative lengra): LINGER, LONG1; b. Old High German lang ...; c. Old English denominative langian ...; d. Latin compound Longobardus ...'\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"POK\", \"where\": \"pp. 196-197 s.v. del-5, section /d/longho-s b)\", \"stance\": \"supports\", \"note\": \"'Latin longus ..., Gothic laggs, Old English Old High German Modern High German lang (Old High German langen \\\"become long, seem long, long, want\\\")'.\"},\n       {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. longus\", \"stance\": \"supports\", \"note\": \"'Cf. got. laggs \\\"long\\\"' - Gothic laggs is given as the Germanic match of Latin longus.\"},\n       {\"src\": \"SYN\", \"where\": \"Buck 12.57\", \"stance\": \"supports\", \"note\": \"'Goth. laggs, ON langr, Dan. lang, Sw. lång, OE long, ME long, NE long, Du. lang, OHG lang, MHG lanc, NHG lang'.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"English\", \"words\": \"long; belong; along\", \"verdict\": \"plausible\",\n     \"derivation\": \"long (adj.) is OE lang/long < PGmc *langaz, with the regular OE change of short a to o before -n- (whence the doublet lang/long, as in bond/band); along is OE andlang, originally an adjective 'entire, continuous' and a preposition 'alongside of', a compound of and- 'against, opposite' (PIE *anti) + lang 'long', reinforced by ON endlang; both are certain. belong is the weak link: Etymonline derives it (mid-14c. 'to go along with, properly relate to') from be- + Middle English longen 'to go', from OE langian 'pertain to, to go along with', 'which is of uncertain origin but perhaps related to the root of long (adj.)'; it displaced OE gelang 'along with, dependent on', which does contain lang. So two of the three words are confirmed and the third is probable but not proven - hence 'plausible' for the node.\",\n     \"derivation_fa\": \"«long» انگلیسی از انگلیسی باستان lang/long، از *langaz ژرمنی، با تبدیل قاعده‌مندِ a کوتاه به o پیش از n در انگلیسی باستان. «along» از andlang انگلیسی باستان است، در اصل صفت «سراسری، پیوسته» و حرف اضافهٔ «در امتداد»، مرکب از and- «در برابر» (از *anti هندواروپایی) و lang «دراز»، که صورت نُرسی endlang نیز آن را تقویت کرده است؛ این دو قطعی‌اند. اما «belong» مورد تردید است: اتیمانلاین آن را (سدهٔ چهاردهم، به معنی «همراه رفتن، مربوط بودن») از پیشوند be- و longen «رفتن» انگلیسی میانه، از langian انگلیسی باستان می‌داند و می‌افزاید که خاستگاه langian «نامعلوم است، شاید با ریشهٔ long پیوند داشته باشد». پس دو واژه تأیید و سومی تنها محتمل است؛ از این رو حکم گره «با احتیاط پذیرفتنی».\",\n     \"sources\": [E + \"belong\", E + \"along\"],\n     \"ref_check\": [\n       {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference of Nourai's own (refs=None); the parent Germanic node's AHD citation covers LONG1/LONG2 but the AHD appendix index does not list BELONG.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"AHD\", \"where\": \"Watkins 1985, index and s.v. del-1\", \"stance\": \"partial\", \"note\": \"index gives 'LONG1 del-1', 'LONG2 del-1', 'LINGER del-1', 'LENGTH del-1'; ALONG appears in the index without a root tag and BELONG is absent.\"},\n       {\"src\": \"KLN\", \"where\": \"Klein s.v. long, adj. and along\", \"stance\": \"supports\", \"note\": \"KLN_1971.txt 'See long, adj., and cp. along.' - Klein cross-refers along to long, adj.\"},\n       {\"src\": \"POK\", \"where\": \"p. 197\", \"stance\": \"supports\", \"note\": \"'Old English Old High German Modern High German lang' under /d/longho-s.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"Latin\", \"words\": \"longus\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin longus, -a, -um 'long' (of space and of time), continuing *dlonghos with the same West-IE simplification of initial dl- as in Germanic. Ernout-Meillet: 'longus, -a, -um: long. Se dit de l'espace et du temps ... Cf. got. laggs \\\"long\\\"', adding cautiously that the eastern branch has 'un autre mot' (skr. dīrgháḥ, v.sl. dlŭgŭ, gr. dolikhós, hitt. dalugaeš) - i.e. they group the two ablaut shapes as related but formally distinct, which is the modern position. Watkins files 'Latin longus (> French long)' directly under del-1.\",\n     \"derivation_fa\": \"لاتینی longus, -a, -um «دراز» (هم در مکان و هم در زمان)، دنبالهٔ *dlongʰos با همان ساده‌شدن خوشهٔ آغازین dl- که در ژرمنی هم دیده می‌شود. ارنو-مِیه در فرهنگ ریشه‌شناختی لاتینی می‌نویسند: «longus ... دربارهٔ مکان و زمان به کار می‌رود ... قس گوتی laggs»، و می‌افزایند که شاخهٔ خاوری «واژهٔ دیگری» دارد (سنسکریت dīrgháḥ، اسلاوی کهن dlŭgŭ، یونانی dolikhós، هیتی dalugaeš) - یعنی این دو صورتِ اَبلاوت را خویشاوند اما از نظر ساخت جدا می‌دانند، که دیدگاه امروزی نیز همین است. واتکینز longus را مستقیماً زیر del-1 آورده است. ادعای نورایی درست است.\",\n     \"sources\": [E + \"oblong\", PIE_DLG],\n     \"ref_check\": [\n       {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. del-1: '3. Latin longus (> French long), long: LONGERON, LONGITUDE; ELOIGN, ELONGATE, LONGEVITY, LUNGE, OBLONG, PROLONG, PURLOIN.'\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. longus\", \"stance\": \"partial\", \"note\": \"'longus, -a, -um: long. Se dit de l'espace et du temps ... Cf. got. laggs \\\"long\\\" ... Autre mot dans la partie orientale de l'indo-européen: skr. dīrgháḥ, v.sl. dlŭgŭ, gr. dolikhós, et hitt. dalugaeš (pl.) \\\"longs\\\".'\"},\n       {\"src\": \"POK\", \"where\": \"p. 197, /d/longho-s b)\", \"stance\": \"supports\", \"note\": \"'Latin longus \\\"long; spacious; of time, long, of long duration ...\\\"'.\"},\n       {\"src\": \"SYN\", \"where\": \"Buck 12.57\", \"stance\": \"supports\", \"note\": \"'Lat. longus, It. lungo, Fr. long, Sp. largo, Rum. lung' - Latin longus heads the Romance column.\"}\n     ]\n    },\n    {\n     \"id\": 8, \"lang\": \"English\", \"words\": \"oblong; prolong; longitude\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Three learned Latinisms of the 15th-16th centuries, all built on longus: oblong < Latin oblongus 'longish, elongated' (ob- 'towards, in front of' + longus), in English from the 15th c.; prolong < Old French prolonguer / Late Latin prolongāre 'to lengthen out' (pro- 'forth' + longus); longitude < Latin longitūdō 'length' (longus + the abstract suffix -tūdō, exactly like altitūdō, latitūdō - Ernout-Meillet list 'longitūdō (cf. altitudo, latitudo)' among the derivatives of longus), specialised to the geographical sense in the 14th-16th c. Watkins lists all three under del-1, and Skeat simply refers 'Oblong: see Long (1)'.\",\n     \"derivation_fa\": \"هر سه وام‌واژه‌ای عالمانه از لاتینی‌اند که در سده‌های پانزدهم و شانزدهم وارد انگلیسی شده‌اند و همه بر پایهٔ longus ساخته شده‌اند: «oblong» از لاتینی oblongus «کشیده، درازگونه» (ob- + longus)؛ «prolong» از فرانسهٔ کهن prolonguer و لاتینی متأخر prolongāre «دراز کردن» (pro- «پیش» + longus)؛ «longitude» از لاتینی longitūdō «درازا» (longus + پسوند اسم معنی -tūdō، درست مانند altitūdō و latitūdō که ارنو-مِیه هر سه را در کنار هم آورده‌اند)، که بعدها معنی جغرافیایی «طول جغرافیایی» گرفته است. واتکینز هر سه را زیر del-1 فهرست کرده و اسکیت هم می‌نویسد «Oblong: نگاه کنید به Long». ادعای نورایی درست است.\",\n     \"sources\": [E + \"oblong\"],\n     \"ref_check\": [\n       {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference of Nourai's own on this node (refs=None); the parent Latin node's AHD citation covers all three words.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. del-1 and index\", \"stance\": \"supports\", \"note\": \"'Latin longus ...: LONGERON, LONGITUDE; ELOIGN, ELONGATE, LONGEVITY, LUNGE, OBLONG, PROLONG, PURLOIN'; index lines 'OBLONG del-', 'PROLONG del-', 'LONGITUDE del-1'.\"},\n       {\"src\": \"SKT\", \"where\": \"Skeat s.v. Oblong\", \"stance\": \"supports\", \"note\": \"'Oblong: see Long (1).'\"},\n       {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. longus, derivatives\", \"stance\": \"supports\", \"note\": \"'longitūdō (cf. altitudo, latitudo)' and 'prolongo (l. de l'Égl.) pour profero, prorogo' are listed among the derivatives/compounds of longus.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"Dem, Domu\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *dem- 'to build', root noun *dṓm / *dem-s 'house', o-stem *domos, u-stem *domus\",\n   \"note\": \"Pokorny pp. 198-199: 'Root / lemma: dem-, dema- ; Meaning: to build; house', with the sub-sections 'root nouns dem-, dom-, dm- \\\"house\\\"', 'o-stem domo-s' and 'u-stem domu-s' - Nourai's paired root name Dem / Domu reproduces precisely the root and the u-stem, the language label and the gloss 'house' are right. AHD: 'deme-1. Also dem-. House, household ... [Pok. dem- 198.]'. Wiktionary reconstructs the noun as *dṓm 'home, house', 'from *dem- (to build) + *-s (root nominal suffix)'. The one point Pokorny himself flags is that the 'build' sense (Gk. demō, Gmc. *timram) may be a separate root from the 'house' noun - which matters only for node 13/14 (timber).\",\n   \"note_fa\": \"پوکورنی (ص ۱۹۸-۱۹۹): «ریشه: dem-, demə-؛ معنی: ساختن؛ خانه»، با بخش‌های «اسم‌های ریشه‌ای dem-, dom-, dm- «خانه»»، «ستاک o: domo-s» و «ستاک u: domu-s». پس نام دوگانهٔ «Dem, Domu» نزد نورایی درست همان ریشه و ستاک u است و برچسب زبانی و معنی «خانه» نیز درست است. واتکینز نیز آورده: «deme-1، همچنین dem-: خانه، خانواده». ویکی‌واژه اسم را *dṓm بازسازی می‌کند: «از *dem- «ساختن» + پسوند اسم‌ساز *-s». تنها نکته‌ای که خود پوکورنی یادآور می‌شود این است که معنی «ساختن» (یونانی démō، ژرمنی *timram) شاید ریشه‌ای جدا باشد؛ این نکته فقط بر گره‌های ۱۳ و ۱۴ (timber) اثر دارد. ادعای نورایی درست است.\",\n   \"sources\": [PIE_DOM, E + \"timber\", E + \"dome\"],\n   \"ref_check\": [\n     {\"ref\": \"POK:198\", \"status\": \"supports\", \"note\": \"POK_full.txt: 'Root / lemma: dem-, dema- / Meaning: to build; house ... root nouns dem-, dom-, dm-, dm- house ... o-stem domo-s: Old Indic dama-h \\\"house, dwelling\\\", gr. dómos ... u-stem domu-s: Latin domus, -us f. ... References: WP. I 786 ff.; WH. I 367 ... Page(s): 198-199'.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. deme-1\", \"stance\": \"supports\", \"note\": \"'deme-1. Also dem-. House, household. 1. Suffixed reduced o-grade form *dom-o-, dom-u-, house ... [Pok. dem- 198.]'\"},\n     {\"src\": \"IEC\", \"where\": \"Mann, s.v. domos, ūs and domn- (1)\", \"stance\": \"supports\", \"note\": \"'domos, ūs \\\"building, house\\\". Cf. demo, dómn- (1) Skt. dámaḥ ... Arm. tun, gs tan ... Gk. dómos ... Lat. domus; ... OCS domŭ, u-st.'\"},\n     {\"src\": \"SYN\", \"where\": \"Buck 7.12 'house'\", \"stance\": \"supports\", \"note\": \"'Lat. domus \\\"house\\\" (7.12), also the immediate \\\"family\\\"'; 'ChSl. dom \\\"house\\\" (7.12) renders oikos also in sense of \\\"family\\\"'.\"},\n     {\"src\": \"WLD\", \"where\": \"cited by Pokorny as WP. I 786 ff.\", \"stance\": \"supports\", \"note\": \"Pokorny's reference line for dem- points to Walde-Pokorny I 786 ff.; Bd. I itself not opened.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"demâna, nmâna, mân 3; garô-demâna\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Bartholomae's headword (AiWb cols. 1089-1091) is exactly Nourai's trio: '• j. nmāna-, g., j. dəmāna-, j. māna- n. \\\"Behausung, Haus\\\", von jedem zum Aufenthalt für Menschen (Götter) und Haustiere dienenden Bauwerk', with the etymology 'Aus ar. *dmāna- (IF. 7.62); zum gr. V. démō; ai. vgl. dáma- n. \\\"Haus\\\". S. noch māniya-.' - i.e. Proto-Aryan *dmāna- (zero grade *dm- of *dem- + the participial/verbal-noun suffix -āna-), whence Gathic dəmāna- with anaptyctic ə, Younger Avestan nmāna- with the dissimilatory change dm- > nm-, and the further-reduced māna-; Old Indic has the same formation in māna- 'edifice'. Bartholomae's own cross-reference 'g. dəmāna- n.: s. unter nmāna-' (col. 749) confirms the identity of the two. garō.dəmāna- 'house of song/praise' (garō, gen. of gar- 'song of praise', + dəmāna-) is the Zoroastrian highest heaven; Bartholomae files it under nmāna- section b) 'j., g. mit GS. garō ..., vom Paradies: garō nmānē Y.45.8; 50.4, 51.15', with the Pahlavi gloss 'garōdmān'. So Nourai's gloss 'prayer house, sky' and his cross-reference to the root Gwer 2 (PIE *gwerH- 'to praise') are both right.\",\n     \"derivation_fa\": \"سرواژهٔ بارتولمه (ستون‌های ۱۰۸۹-۱۰۹۱) درست همان سه صورتی است که نورایی آورده: «اوستای نو nmāna-، گاهانی و نو dəmāna-، نو māna-، اسم خنثی «خانه، جایگاه»»، با این ریشه‌شناسی: «از آریایی *dmāna-؛ قس فعل یونانی démō؛ هندی باستان dáma- «خانه». نیز نگاه کنید به māniya-». یعنی از درجهٔ صفر *dm- ریشهٔ *dem- با پسوند -āna-؛ در گاهان با واکهٔ میانجی dəmāna-، در اوستای نو با ناهمگونی dm- > nm- به nmāna-، و صورت کوتاه‌شدهٔ māna-. بارتولمه خود ارجاع می‌دهد: «گاهانی dəmāna-: نگاه کنید به nmāna-». «garō.dəmāna-» یعنی «خانهٔ سرود/ستایش» (garō، حالت اضافهٔ gar- «سرود ستایش» + dəmāna-)، بالاترین آسمانِ زردشتی، که بارتولمه آن را زیر nmāna- بخش ب آورده است: «با اضافهٔ garō، دربارهٔ بهشت» با معادل پهلوی garōdmān. پس معنی «نمازخانه، آسمان» و ارجاع نورایی به ریشهٔ Gwer 2 هر دو درست است.\",\n     \"sources\": [PIE_DOM],\n     \"ref_check\": [\n       {\"ref\": \"POK:199\", \"status\": \"supports\", \"note\": \"POK_full.txt s.v. dem-, demə- (pp.198-199): 'Aryan *dm-ana- in Avestan damana-, nmana- n. \\\"house\\\", also Old Indic mana-h \\\"edifice, building, dwelling\\\"'.\"},\n       {\"ref\": \"KNT:302\", \"status\": \"not_found\", \"note\": \"impossible page: Kent's Old Persian (1950/1953) ends at p.219 (the Lexicon runs pp.164-215). The Kent passage that actually says this is p.202 s.v. māniya-: 'from māna-, GAv. demāna-, Av. nmāna- \\\"abode, house\\\"' - so KNT:302 looks like a misprint for KNT:202 (the number Nourai cites correctly on node 5).\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"BRT\", \"where\": \"AiWb cols. 1089-1091 s.v. nmāna-; col. 749 s.v. dəmāna-\", \"stance\": \"supports\", \"note\": \"'• j. nmāna-, g., j. dəmāna-, j. māna- n. \\\"Behausung, Haus\\\" ... Aus ar. *dmāna- (IF. 7.62); zum gr. V. démō; ai. vgl. dáma- n. \\\"Haus\\\". S. noch māniya-. - Pü.: mān'; and 'b) j., g. mit GS. garō ..., vom Paradies ... Pü.: garōdmān ... Pü. erl.: garōtmān'.\"},\n       {\"src\": \"KNT\", \"where\": \"p. 202 s.v. māniya-\", \"stance\": \"supports\", \"note\": \"'from māna-, GAv. demāna-, Av. nmāna- \\\"abode, house\\\" (§126), extension of root seen in Skt. dáma- \\\"house\\\", Gk. dómos, Lt. domus'.\"},\n       {\"src\": \"SNS\", \"where\": \"Tavoosi p. 239 s.v. garōdmān / mān\", \"stance\": \"supports\", \"note\": \"'garōdmān: ← Av. garō.dəmāna- (AiWb 512 √gar + dəmāna-) ... nmāna- (AiWb 1090) ... Man. MP grʾsmʾn / grdmʾn (Mir.Man. II,49)'.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"mân; dŭtak-mân\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Middle Persian mān [mʾn] 'house, dwelling, palace' is the direct continuant of Av. māna-/dəmāna-; Nyberg's glossary (Manual of Pahlavi II, p.125) has 'man [mʾn, mʾny] house, palace ... man ī rōšn Garōdman, of Paradise ... man ī ātaxšān the fire-temple ... MPrs mʾn; Paz. mān; NP mān; MPrth mānistān \\\"dwelling-place, monastery\\\"; < Av. (1090 sqq.) nmāna-, dəmāna- through the influence of māndan'. The compound dūdag-mān (Book Pahlavi dwtkmʾn) is 'household, family' = dūdag [dwtk'] 'family' (MacKenzie p.27; Nyberg p.132 'dūtak [dwtk'] family ... NP dūdah'), itself connected with dūd [dwd] 'smoke' - hence Nourai's chart note 'family members who sit around a fire' and his cross-reference to Dheu 2 (PIE *dheu- 'smoke'). The compound is literally 'smoke-house' = the hearth-community; Wiktionary reconstructs the Middle Persian antecedent of NP dūdmān as dwtkmʾn (dūtakmān, dūdagmān).\",\n     \"derivation_fa\": \"فارسی میانه mān [mʾn] «خانه، سرای، کاخ» دنبالهٔ مستقیم māna-/dəmāna- اوستایی است؛ نیبرگ در واژه‌نامهٔ راهنمای پهلوی (جلد دوم، ص ۱۲۵) می‌نویسد: «man [mʾn, mʾny] خانه، کاخ ... man ī rōšn یعنی گرودمان، بهشت ... man ī ātaxšān آتشکده ... فارسی میانه mʾn؛ پازند mān؛ فارسی نو مان؛ پارتی mānistān «جایگاه، صومعه»؛ از اوستایی nmāna-، dəmāna- با تأثیر māndan». ترکیب dūdag-mān (پهلوی کتابی dwtkmʾn) یعنی «خاندان» = dūdag «خانواده» (مکنزی ص ۲۷؛ نیبرگ ص ۱۳۲: «dūtak خانواده ... فارسی نو دوده») + mān؛ و dūdag خود با dūd «دود» پیوند دارد - و همین است مبنای یادداشت نورایی («کسانی که گرد آتش می‌نشینند») و ارجاعش به ریشهٔ Dheu 2 «دود». پس «دودمان» تحت‌اللفظ «خانهٔ دود»، یعنی جمعِ گرداگرد اجاق است. ادعای نورایی درست است.\",\n     \"sources\": [DUDMAN, PIE_DOM],\n     \"ref_check\": [\n       {\"ref\": \"BQT:894\", \"status\": \"partial\", \"note\": \"the دودمان entry stands in the scan at BQT_v2_pages.txt leaf 354 ≈ printed p.896 (the cited 894 is within the ±2 drift of this scan). Mo'in's footnote 3 there analyses 'از: دود + مان' and glosses دوده as 'دودمان، دودخانه' with 'پهلوی dūtak' - it supports the compound but treats -mān as a suffix rather than the noun 'house'.\"},\n       {\"ref\": \"BQT:1949\", \"status\": \"supports\", \"note\": \"exact: BQT_v4_pages.txt pdf page 32 carries the printed running head ۱۹۴۹, and Mo'in's footnote 2 to مان reads 'پهلوی mān (خانه، مسکن) «نیبرگ ص ۱۴۶»، پارسی باستان māniya- (خانه، سرای)، در پهلوی به جای dəmāna- اوستایی کلمهٔ mān (خانه) را به کار برده‌اند، mān(i)stan (منزل) ... و «ماندن» فارسی نیز از همین ریشه است'; footnote 6 adds 'ب) مان (از ریشهٔ garəθma گاثاها و garōdəmāna ... پهلوی mān به معنی خانه): کشتمان، دودمان، گرزمان'.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II (Glossary), p. 125 s.v. man; p. 132 s.v. dūtak\", \"stance\": \"supports\", \"note\": \"'man [mʾn, mʾny] house, palace ... < Av. (1090 sqq.) nmāna-, dəmāna- through the influence of māndan'; 'dūtak [dwtk'] family ... NP dūdah'.\"},\n       {\"src\": \"PHD\", \"where\": \"MacKenzie p. 27\", \"stance\": \"supports\", \"note\": \"'dūd [dwt' | M dwd, N ~] smoke. dūdag [dwtk' | N ~a] family.' - the two are printed side by side, the family word being the -ag derivative of 'smoke'.\"},\n       {\"src\": \"BQT\", \"where\": \"Mo'in's footnotes, printed pp. ≈896 (دودمان) and 1949 (مان)\", \"stance\": \"supports\", \"note\": \"see ref_check.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"mân «مان ۲»; dŭdmân «دودمان»\", \"verdict\": \"confirmed\",\n     \"derivation\": \"NP مان mān 'house, dwelling' continues MP mān unchanged (it survives chiefly in compounds and in the verb ماندن 'to stay' with which Nyberg says it interacted); Mo'in's footnote to the Borhān entry مان (p.1949) states that Pahlavi used mān in place of Avestan dəmāna-, and that 'ماندن' belongs to the same root. NP دودمان dūdmān 'family, dynasty' is the regular reflex of MP dūdag-mān (dwtkmʾn), with loss of the middle syllable -ag- in the compound and the voicing t > d already in MP; Wiktionary: 'Inherited from Middle Persian dwtkmʾn (dūtakmān, dūdagmān). By surface analysis, دود (dud, \\\"smoke\\\") + ـمان (-mân)'. Mo'in lists دودمان together with کشتمان and گرزمان as the compounds containing this -mān.\",\n     \"derivation_fa\": \"«مان» فارسی نو به معنی «خانه، سرای» بی‌دگرگونی از mān فارسی میانه مانده است و بیشتر در ترکیب‌ها و در پیوند با فعل «ماندن» به کار می‌رود؛ معین در حاشیهٔ برهان قاطع (ص ۱۹۴۹) می‌نویسد که در پهلوی به جای dəmāna- اوستایی واژهٔ mān به کار رفته و «ماندن» فارسی نیز از همین ریشه است. «دودمان» بازتاب قاعده‌مند dūdag-mān فارسی میانه (dwtkmʾn) است: هجای میانی -ag- در ترکیب افتاده و t نیز پیش‌تر در فارسی میانه واک‌دار شده است. ویکی‌واژه نیز می‌نویسد: «برگرفته از فارسی میانهٔ dwtkmʾn (dūtakmān / dūdagmān)؛ در تحلیل صوری: دود + ـمان». معین «دودمان» را در کنار «کشتمان» و «گرزمان» از ترکیب‌های همین ـمان می‌شمارد. ادعای نورایی درست است.\",\n     \"sources\": [DUDMAN, PIE_DOM],\n     \"ref_check\": [\n       {\"ref\": \"SNS:239\", \"status\": \"supports\", \"note\": \"SNS index 'mān 239/21-252/18' and 'nmāna- 239/21' - Tavoosi's p.239 entry gives Pahlavi mān with Av. nmāna- (AiWb 1090) as its source, in the same paragraph as garōdmān.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"BQT\", \"where\": \"Mo'in's footnotes to مان, printed p. 1949 (BQT_v4 pdf p.32)\", \"stance\": \"supports\", \"note\": \"'پهلوی mān (خانه، مسکن) «نیبرگ ص ۱۴۶» ... در پهلوی به جای dəmāna- اوستایی کلمهٔ mān را به کار برده‌اند'; and 'مان ... : کشتمان، دودمان، گرزمان'.\"},\n       {\"src\": \"NYB\", \"where\": \"Glossary p. 125 s.v. man\", \"stance\": \"supports\", \"note\": \"'MPrs mʾn; Paz. mān; NP mān'.\"},\n       {\"src\": \"PHD\", \"where\": \"MacKenzie p. 27 s.v. dūdag\", \"stance\": \"supports\", \"note\": \"'dūdag [dwtk' | N ~a] family' - MacKenzie's NP equivalent is دوده, the simplex beside دودمان.\"},\n       {\"src\": \"HRN\", \"where\": \"Grundriss\", \"stance\": \"silent\", \"note\": \"grep for 'dūdmān', 'dudman', 'mān \\\"Haus\\\"' in HRN.txt returned nothing.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Persian\", \"words\": \"garzmân «گرزمان»\", \"verdict\": \"confirmed\",\n     \"derivation\": \"NP گرزمان garzmān/garazmān 'the highest heaven, empyrean', a Zoroastrian technical term. Mo'in's footnote to the Borhān entry (p.1793) sets out the whole chain: 'Avestan garō dəmāna, garō nmāna; Pazand garōdmān, garōθmān; Sogdian garōdmān; Parthian gʾrwdmʾn; Middle Persian grsmʾn; ... the Persian pronunciation garzmān is late and corrupt', citing Henning, 'Two Central Asian Words' p.157 and 'A List of Middle-Persian and Parthian Words' BSOS IX/1 p.82. The route is therefore Av. garō.dəmāna- > Man. MP grʾsmʾn/garōsmān (with the West-Iranian d > s/z development in this cluster, seen also in Pazand garōθmān) > NP garzmān, beside the learned Zoroastrian garōdmān; Old Armenian gerezman is an Iranian borrowing of the same word (Wiktionary). Nourai's arrow from the Avestan compound straight to the Persian word is exactly right.\",\n     \"derivation_fa\": \"«گرزمان» در فارسی نو یعنی «بالاترین آسمان، عرش»، اصطلاحی زردشتی. معین در حاشیهٔ برهان قاطع (ص ۱۷۹۳) کل زنجیره را آورده است: «اوستا garō dəmāna، garō nmāna؛ پازند garōdmān، garōθmān؛ سغدی garōdmān؛ پارتی gʾrwdmʾn؛ فارسی میانه grsmʾn؛ ... تلفظ فارسیِ garzmān متأخر و مغلوط است»، با ارجاع به دو مقالهٔ هنینگ («Two Central Asian Words» ص ۱۵۷ و فهرست واژه‌های فارسی میانه و پارتی، BSOS جلد ۹ ص ۸۲). پس راه تحول چنین است: اوستایی garō.dəmāna- ← فارسی میانهٔ مانوی grʾsmʾn (با تحول خوشهٔ dm به sm/zm در ایرانی باختری، که در پازند garōθmān هم دیده می‌شود) ← «گرزمان» فارسی نو، در کنار صورت عالمانهٔ «گروتمان/گرودمان». ارمنی کهن gerezman نیز وام‌واژه‌ای ایرانی از همین کلمه است. پیکان نورایی از ترکیب اوستایی مستقیم به واژهٔ فارسی کاملاً درست است.\",\n     \"sources\": [GARZ, PIE_DOM],\n     \"ref_check\": [\n       {\"ref\": \"BQT:1793\", \"status\": \"supports\", \"note\": \"exact: BQT_v3_pages.txt pdf page 590 carries the printed head ۱۷۹۳ with the headword گرزمان; footnote 6 there reads 'فارسی garzmān (آسمان). این کلمه در اوستا garō dəmāna، garō nmāna، پازند garōdmān/garōθmān، سغدی garōdmān، پارتی gʾrwdmʾn ... به پارسی میانه grsmʾn ... garzmān تلفظ متأخر و مغلوط است ... رك: Henning, Two Central Asian Words p.157; Henning, A list of Middle Persian..., BSOS IX,1,p.82'.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"BRT\", \"where\": \"AiWb col. 1090, s.v. nmāna- section b)\", \"stance\": \"supports\", \"note\": \"'b) j., g. mit GS. garō ..., vom Paradies: garō nmānē Y.45.8; 50.4, 51.15 ... Pü.: garōdmān ... Pü. erl.: garōtmān'.\"},\n       {\"src\": \"SNS\", \"where\": \"Tavoosi p. 239 s.v. garōdmān\", \"stance\": \"supports\", \"note\": \"'garōdmān: ← Av. garō.dəmāna- (AiWb 512 √gar + dəmāna-; nmāna- AiWb 1090); Man. MP grʾsmʾn, grdmʾn (Mir.Man. II,49)' - the Manichaean grʾsmʾn is the immediate antecedent of garzmān.\"},\n       {\"src\": \"NYB\", \"where\": \"Glossary p. 125 s.v. man\", \"stance\": \"supports\", \"note\": \"'man ī rōšn Garōdman, of Paradise' - the Pahlavi periphrasis of the same compound.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Old Persian\", \"words\": \"mâna 2; mânya\", \"verdict\": \"plausible\",\n     \"derivation\": \"Kent p.202 has only the derivative: 'māniya- sb., probably \\\"personal property\\\" in the houses; nt. adj. as collective sb., from māna-, GAv. demāna-, Av. nmāna- \\\"abode, house\\\" (§126), extension of root seen in Skt. dáma- \\\"house\\\", Gk. dómos, Lt. domus', attested once, DB 1.65 (māniyam-cā, among the things Gaumāta had taken from the people and Darius restored). So (a) OP *māna- 'house' is a reconstruction of Kent's, not an attested Old Persian lexeme with its own entry; (b) the attested word māniya- means 'household property, chattels', not 'domestic, house servant' - Kent explicitly notes the divergent interpretations (Tolman Lex. 116, Bartholomae AiW 1168 etc.). The derivation from the root is certain, the forms and glosses as Nourai prints them are only approximately Kent's; hence 'plausible'. Mo'in, incidentally, cites the same word as 'پارسی باستان māniya- (خانه، سرای)' in the Borhān footnote to مان.\",\n     \"derivation_fa\": \"کنت در ص ۲۰۲ تنها مشتق را دارد: «māniya- اسم، احتمالاً «مِلک شخصی» در خانه‌ها؛ صفت خنثی در معنی اسم جمع، از māna-، گاهانی demāna-، اوستایی nmāna- «خانه» ... گسترشی از همان ریشه‌ای که در دامَهٔ سنسکریت، dómos یونانی و domus لاتینی دیده می‌شود»، که تنها یک بار در بیستون ۱:۶۵ آمده است. پس نخست، *māna- پارسی باستان بازسازیِ خودِ کنت است نه واژه‌ای گواهی‌شده با مدخل مستقل؛ و دوم، واژهٔ گواهی‌شدهٔ māniya- به معنی «دارایی خانگی» است نه «خانگی، خدمتکار خانه» - و کنت خود به اختلاف نظرها (تولمن، بارتولمه) اشاره می‌کند. پیوند با ریشه قطعی است اما صورت و معنایی که نورایی آورده دقیقاً از کنت نیست؛ از این رو «با احتیاط پذیرفتنی». معین نیز در حاشیهٔ «مان» همین واژه را «پارسی باستان māniya- (خانه، سرای)» آورده است.\",\n     \"sources\": [PIE_DOM],\n     \"ref_check\": [\n       {\"ref\": \"KNT:202\", \"status\": \"partial\", \"note\": \"the page is exactly right (the printed page number 202 appears in KNT.txt just above the entry), but the entry reads 'māniya- sb., probably \\\"personal property\\\" in the houses ... from māna-, GAv. demāna-, Av. nmāna- \\\"abode, house\\\"'. Kent has no separate lemma māna-, and does not gloss māniya- as 'domestic, house servant'.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KNT\", \"where\": \"p. 202 s.v. māniya-; text DB 1.65\", \"stance\": \"partial\", \"note\": \"see ref_check; 'māniyam-cā asn. DB 1.65'.\"},\n       {\"src\": \"BRT\", \"where\": \"AiWb 1168 (cited by Kent) and col. 1091\", \"stance\": \"supports\", \"note\": \"Bartholomae's nmāna- article closes 'S. noch māniya-', i.e. he too files the OP word under this root, though with a different interpretation of its meaning (Kent's note refers to 'Bthl. AiW 1168').\"},\n       {\"src\": \"BQT\", \"where\": \"Mo'in's footnote to مان, printed p. 1949\", \"stance\": \"supports\", \"note\": \"'پارسی باستان māniya- (خانه، سرای)'.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"Latin\", \"words\": \"dominus; domina\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin dominus 'master of a household, lord', feminine domina 'mistress of the house, lady', a -no- derivative of the u-stem domus 'house' (< PIE *domus, beside the o-stem *domos in Gk. dómos and Skt. dáma-). Pokorny prints the formation directly: 'o-stem domo-s: ... Latin Loc. domī \\\"in a house\\\" (= Old Indic dame), dominus \\\"master, mister\\\" from *domo-no-s'; Watkins the same: 'suffixed form *dom-o-no- in Latin dominus, master of a household (feminine domina > Old French dame, lady)'. The semantics ('he of the house' > 'master, lord') are the standard Roman household model, the same one that gives dominium, dominārī, domesticus.\",\n     \"derivation_fa\": \"لاتینی dominus «صاحب‌خانه، سرور» و مؤنث آن domina «کدبانو، بانو»، مشتقی با پسوند -no- از ستاک u ی domus «خانه» (از *domus هندواروپایی، در کنار ستاک o ی *domos که dómos یونانی و dáma- سنسکریت از آن‌اند). پوکورنی این ساخت را صریح آورده است: «ستاک o: domo-s ... لاتینی domī «در خانه» ... dominus «سرور» از *domo-no-s»؛ واتکینز نیز: «صورت پسونددار *dom-o-no- در لاتینی dominus، صاحب خانواده (مؤنث domina ← فرانسهٔ کهن dame «بانو»)». تحول معنایی («آن‌که از آنِ خانه است» ← «سرور») همان الگوی خانوادهٔ رومی است که dominium و domesticus هم از آن برخاسته‌اند. ادعای نورایی درست است.\",\n     \"sources\": [PIE_DOM, E + \"madam\", E + \"dungeon\"],\n     \"ref_check\": [\n       {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. deme-1: 'a. Latin domus, house: DOME, DOMESTIC, DOMICILE; MAJORDOMO; b. suffixed form *dom-o-no- in Latin dominus, master of a household (feminine domina > Old French dame, lady): DAME, DAN2, DANGER, DOM, DOMAIN, DOMINATE, ..., DUNGEON; (MADAM), MADAME, MADEMOISELLE, MADONNA, PREDOMINATE.'\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"POK\", \"where\": \"pp. 198-199 s.v. dem-\", \"stance\": \"supports\", \"note\": \"'Latin Loc. domī \\\"in a house\\\" (= Old Indic dame \\\"in a house\\\"), dominus \\\"master, mister\\\" from *domo-no-s'; 'u-stem domu-s: Latin domus, -us f.'\"},\n       {\"src\": \"IEC\", \"where\": \"Mann s.v. domos, ūs\", \"stance\": \"supports\", \"note\": \"'domos, ūs \\\"building, house\\\" ... Lat. domus'.\"},\n       {\"src\": \"KLN\", \"where\": \"Klein s.v. donna / dame\", \"stance\": \"supports\", \"note\": \"'donna, n., an Italian title given to a lady. — It., fr. L. domina. See dame and cp. Madonna.'\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"French\", \"words\": \"ma-dame\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Old French ma dame, literally 'my lady' = ma (< Latin mea) + dame (< Latin domina, with the regular Gallo-Romance loss of the intertonic vowel: domina > *domna > dam(p)ne > dame). Etymonline s.v. madam: 'c. 1300, formal term of address to a lady ..., from Old French ma dame, literally \\\"my lady,\\\" from Latin mea domina'. Watkins puts DAME, MADAM, MADAME, MADEMOISELLE all under the domina branch of deme-1. The Old French form was already a vocative/title in the 12th c. and became the standard courtly address for a married lady.\",\n     \"derivation_fa\": \"فرانسهٔ کهن ma dame تحت‌اللفظ یعنی «بانوی من»: ma از mea لاتینی و dame از domina؛ در تحول گالو-رومی واکهٔ میان‌آوایی افتاده است: domina ← *domna ← dam(p)ne ← dame. اتیمانلاین ذیل madam می‌نویسد: «حدود ۱۳۰۰، عنوان رسمی خطاب به بانو ...، از فرانسهٔ کهن ma dame «بانوی من»، از لاتینی mea domina». واتکینز نیز DAME، MADAM، MADAME و MADEMOISELLE را زیر شاخهٔ domina از ریشهٔ deme-1 آورده است. این صورت در سدهٔ دوازدهم عنوان خطاب درباری بوده و سپس شکل معیارِ خطاب به بانوی شوهردار شده است. ادعای نورایی درست است.\",\n     \"sources\": [E + \"madam\"],\n     \"ref_check\": [\n       {\"ref\": \"AHD:782\", \"status\": \"not_checked\", \"note\": \"AHD New College Edition (1975/76) p.782 would be the main-dictionary entry 'madame'; that edition's body text is only on borrow-restricted archive.org scans, so the page itself could not be opened. The Watkins appendix of the same dictionary does list MADAM/MADAME under deme-1 with 'feminine domina > Old French dame, lady', which is the claim being made.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"Klein s.v. madam / Madonna\", \"stance\": \"supports\", \"note\": \"'Madonna, n. — It. madonna, fr. OIt. ma donna (= It. mia donna), \\\"my lady\\\", for L. mea domina, \\\"my lady\\\". See madam and donna.' - Klein's madam article is the parallel for the French form.\"},\n       {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. deme-1\", \"stance\": \"supports\", \"note\": \"'(feminine domina > Old French dame, lady): DAME ... (MADAM), MADAME, MADEMOISELLE, MADONNA'.\"}\n     ]\n    },\n    {\n     \"id\": 8, \"lang\": \"Persian\", \"words\": \"mâdâm «مادام»\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Persian مادام mādām is a 19th-20th c. loan of French madame, taken in with the wave of French vocabulary that entered Persian through the Dār al-Funūn and the Qajar embassies, and used as the title of address for a European (i.e. non-Muslim, married) lady. Mo'in's dictionary marks it '[فر.] (اِ.) خانم، بانو، در خطاب به بانوان شوهردار غیر مسلمان' ('[French] (noun) lady, madam; in addressing married non-Muslim ladies'), and Dehkhodā's note likewise: 'مادام. (فرانسوی، اِ) کلمه فرانسوی است به معنی بی‌بی، خانم، بانو، بیگم، خاتون'. It must be kept apart from the homographic Arabic conjunction ما دام 'as long as', which is a different word entirely. Ottoman Turkish مادام (madam) is the parallel borrowing from the same French source.\",\n     \"derivation_fa\": \"«مادام» در فارسی وام‌واژه‌ای است از madame فرانسوی که در سدهٔ سیزدهم/چهاردهم هجری همراه موج واژه‌های فرانسوی از راه دارالفنون و سفارت‌های عصر قاجار وارد شده و عنوان خطاب به بانوی اروپایی (شوهردار و غیرمسلمان) است. معین آن را چنین آورده: «[فر.] (اِ.) خانم، بانو، در خطاب به بانوان شوهردار غیر مسلمان»، و یادداشت دهخدا نیز: «مادام. (فرانسوی، اِ) کلمهٔ فرانسوی است به معنی بی‌بی، خانم، بانو، بیگم، خاتون». باید آن را از «ما دامَ» عربی (حرف ربط به معنی «تا وقتی که») که هم‌نویسه است جدا داشت. «مادام» ترکی عثمانی نیز وام‌گیری موازی از همان منبع فرانسوی است. ادعای نورایی درست است.\",\n     \"sources\": [ABADIS, MADAM_W, E + \"madam\"],\n     \"ref_check\": [\n       {\"ref\": \"MON:3681\", \"status\": \"partial\", \"note\": \"the entry itself is verified - Mo'in's Farhang-e Fārsi s.v. مادام: '[ فر. ] (اِ.) خانم، بانو، در خطاب به بانوان شوهردار غیر مسلمان' (quoted from the فرهنگ معین section of abadis.ir) - but the page number could not be checked: the local MON OCR files (MON_part1/2.txt) carry no page tags and the printed vol. 4 (foreign compounds) is not on disk.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi s.v. مادام (via abadis.ir)\", \"stance\": \"supports\", \"note\": \"'[ فر. ] (اِ. ) خانم ، بانو، در خطاب به بانوان شوهردار غیر مسلمان'.\"},\n       {\"src\": \"ARY\", \"where\": \"Aryanpur, Persian IE roots\", \"stance\": \"silent\", \"note\": \"not expected to carry a modern French loanword; not found in the Latin index.\"},\n       {\"src\": \"PHN\", \"where\": \"Pihan, mots français dérivés de l'arabe/persan/turc\", \"stance\": \"silent\", \"note\": \"Pihan treats the opposite direction (oriental words in French); madame is not in it.\"}\n     ]\n    },\n    {\n     \"id\": 9, \"lang\": \"English\", \"words\": \"Madame\", \"verdict\": \"confirmed\",\n     \"derivation\": \"English Madame is a re-borrowing of the modern French madame (as against the older, nativised madam, borrowed c. 1300 from Old French ma dame); it is used in English as the French title, and in the plural mesdames. Etymonline treats them in one article ('madam ... from Old French ma dame ... from Latin mea domina'), and Watkins lists MADAM and MADAME side by side under deme-1. The chain is therefore Latin domina > Old French dame > ma dame > French madame > English Madame.\",\n     \"derivation_fa\": \"«Madame» انگلیسی وام‌گیریِ دوبارهٔ madame فرانسویِ نو است، در برابر صورت کهن‌تر و بومی‌شدهٔ madam که حدود سال ۱۳۰۰ میلادی از ma dame فرانسهٔ کهن گرفته شده بود؛ در انگلیسی همچون عنوانی فرانسوی به کار می‌رود و جمع آن mesdames است. اتیمانلاین هر دو را در یک مدخل آورده («madam ... از فرانسهٔ کهن ma dame ... از لاتینی mea domina») و واتکینز نیز MADAM و MADAME را کنار هم زیر deme-1 فهرست کرده است. پس زنجیره چنین است: لاتینی domina ← فرانسهٔ کهن dame ← ma dame ← فرانسوی madame ← انگلیسی Madame. ادعای نورایی درست است.\",\n     \"sources\": [E + \"madam\"],\n     \"ref_check\": [\n       {\"ref\": \"AHD:782\", \"status\": \"not_checked\", \"note\": \"same as node 7: the New College Edition body page 782 is on borrow-restricted scans only. The Watkins appendix of the same edition lists '(MADAM), MADAME' under deme-1, which is the substance of the claim.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. deme-1 and index ('MADAM deme-')\", \"stance\": \"supports\", \"note\": \"MADAM/MADAME listed under the domina branch.\"},\n       {\"src\": \"KLN\", \"where\": \"Klein s.v. madam, Madonna\", \"stance\": \"supports\", \"note\": \"Klein derives madam from OF ma dame = L. mea domina and cross-refers Madonna to it.\"}\n     ]\n    },\n    {\n     \"id\": 10, \"lang\": \"Italian\", \"words\": \"don; donna, ma-donna\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Italian don 'lord, sir' is the proclitic shortening of Latin dominus (Spanish and Portuguese don/dom are the same word; Etymonline: 'don (n.), title of respect, 1520s, from Spanish or Portuguese Don ... from Latin dominus \\\"lord, master, owner\\\"'); donna 'lady' is Latin domina with the regular Italian assimilation mn > nn (domina > *domna > donna). Klein: 'donna, n., an Italian title given to a lady. — It., fr. L. domina.' The compound ma donna (modern mia donna) 'my lady' is the Italian counterpart of French ma dame; Klein: 'Madonna, n. — It. madonna, fr. OIt. ma donna (= It. mia donna), \\\"my lady\\\", for L. mea domina'.\",\n     \"derivation_fa\": \"ایتالیایی don «سرور، آقا» صورت کوتاه‌شدهٔ پیش‌بستِ dominus لاتینی است (don/dom اسپانیایی و پرتغالی نیز همان است؛ اتیمانلاین: «don، عنوان احترام، از ۱۵۲۰، از Don اسپانیایی یا پرتغالی ... از لاتینی dominus»). donna «بانو» از domina لاتینی است با همگونیِ قاعده‌مند mn ← nn در ایتالیایی (domina ← *domna ← donna). کلاین: «donna، عنوانی ایتالیایی برای بانو. - ایتالیایی، از لاتینی domina». ترکیب ma donna (امروزی mia donna) «بانوی من» همتای ایتالیاییِ ma dame فرانسوی است؛ کلاین: «Madonna - ایتالیایی madonna، از ایتالیایی کهن ma donna (= mia donna) «بانوی من»، به جای mea domina لاتینی». ادعای نورایی درست است.\",\n     \"sources\": [E + \"don\", E + \"madam\"],\n     \"ref_check\": [\n       {\"ref\": \"OEW:58\", \"status\": \"not_checked\", \"note\": \"Shipley, The Origins of English Words (1984), is lending-only on archive.org (djvu.txt returns 401/403) and no copy is on disk, so p.58 could not be read.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"Klein s.v. donna and Madonna\", \"stance\": \"supports\", \"note\": \"'donna, n., an Italian title given to a lady. — It., fr. L. domina. See dame and cp. Madonna. Cp. also Dona, duenna.'; 'Madonna, n. — It. madonna, fr. OIt. ma donna (= It. mia donna), \\\"my lady\\\", for L. mea domina.'\"},\n       {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. deme-1\", \"stance\": \"supports\", \"note\": \"'DOM, ... DOMINO1, (DOMINO2), DUENNA, ... MADONNA' listed under the dominus/domina branch.\"}\n     ]\n    },\n    {\n     \"id\": 11, \"lang\": \"English\", \"words\": \"Madonna\", \"verdict\": \"confirmed\",\n     \"derivation\": \"English Madonna, 1580s as an Italian title of address 'equivalent to madam', from c.1600 as a noun 'an Italian lady', from Italian madonna < Old Italian ma donna 'my lady' < Latin mea domina; from the 1640s specialised in English to 'the Virgin Mary' and hence 'a picture or statue of the Virgin'. The specialisation happened through Italian religious art, which reached English in the vocabulary of connoisseurship. Klein gives the same derivation.\",\n     \"derivation_fa\": \"«Madonna» در انگلیسی از دههٔ ۱۵۸۰ به عنوان عنوان خطاب ایتالیایی «هم‌ارز madam» به کار رفته و از حدود ۱۶۰۰ اسم است به معنی «بانوی ایتالیایی»، از madonna ایتالیایی، از ma donna ایتالیایی کهن «بانوی من»، از mea domina لاتینی؛ و از دههٔ ۱۶۴۰ در انگلیسی به «مریم عذرا» و سپس «تصویر یا تندیس مریم» تخصیص یافته است. این تحول معنایی از راه هنر دینی ایتالیا و واژگان هنرشناسی به انگلیسی رسیده است. کلاین نیز همین ریشه‌شناسی را می‌دهد. ادعای نورایی درست است.\",\n     \"sources\": [E + \"madam\"],\n     \"ref_check\": [\n       {\"ref\": \"OEW:58\", \"status\": \"not_checked\", \"note\": \"Shipley 1984 is lending-only; no local copy. (The claim itself is standard and is carried by Klein and by the AHD appendix.)\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"Klein s.v. Madonna\", \"stance\": \"supports\", \"note\": \"'Madonna, n. — It. madonna, fr. OIt. ma donna (= It. mia donna), \\\"my lady\\\", for L. mea domina, \\\"my lady\\\". See madam and donna.'\"},\n       {\"src\": \"AHD\", \"where\": \"Watkins 1985, index 'MADONNA deme-'\", \"stance\": \"supports\", \"note\": \"MADONNA is indexed to deme-1.\"}\n     ]\n    },\n    {\n     \"id\": 12, \"lang\": \"English\", \"words\": \"dome; domestic; domain; dominate; condominium; danger; dungeon\", \"verdict\": \"plausible\",\n     \"derivation\": \"Six of the seven are straightforward Latin descendants and all are listed by Watkins under deme-1: domestic < Latin domesticus (domus + -icus); domain < Old French demeine/domaine < Latin dominium 'property, lordship'; dominate < Latin dominārī, pp. dominātus; condominium < Modern Latin con- + dominium (a chancery coinage of the 18th c. for joint sovereignty); danger < Old French dangier < Vulgar Latin *dominiārium 'power of a lord' (whence 'power to harm' > 'risk'); dungeon < Old French donjon 'great tower of a castle' < Gallo-Roman *dominiōnem < Late Latin dominium, 'so called probably for its commanding position or strength', the sense 'underground cell' arising in English in the early 14th c. The exception is dome: Etymonline derives it from French dôme 'a town-house; a dome, a cupola' (16c.) < Provençal doma < Greek dōma 'a house, housetop', 'related to domos' - i.e. it comes from the Greek, not the Latin, branch of the root (Watkins files DOME under Latin domus, which is at best a simplification). Same root, wrong parent node; hence the node is 'plausible' rather than 'confirmed'.\",\n     \"derivation_fa\": \"شش واژه از هفت واژه بازماندگان مستقیم لاتینی‌اند و واتکینز همه را زیر deme-1 آورده است: «domestic» از domesticus لاتینی (domus + -icus)؛ «domain» از demeine/domaine فرانسهٔ کهن، از dominium لاتینی «مِلک، خداوندی»؛ «dominate» از dominārī؛ «condominium» ساختهٔ لاتینیِ نو (con- + dominium) برای «حاکمیت مشترک» در سدهٔ هجدهم؛ «danger» از dangier فرانسهٔ کهن، از *dominiārium لاتینی عامیانه «قدرت خداوندگار» (و از آنجا «قدرت آسیب رساندن» ← «خطر»)؛ «dungeon» از donjon فرانسهٔ کهن «برج بزرگ قلعه»، از *dominiōnem گالو-رومی، از dominium لاتینی متأخر، که معنی «سیاه‌چال زیرزمینی» را در انگلیسیِ آغاز سدهٔ چهاردهم گرفته است. استثنا «dome» است: اتیمانلاین آن را از dôme فرانسوی (سدهٔ شانزدهم) از doma زبان اُکسیتان از dōma یونانی «خانه، بام» می‌داند، یعنی از شاخهٔ یونانیِ ریشه نه شاخهٔ لاتینی. ریشه یکی است اما گرهِ پدر نادرست است؛ از این رو حکم گره «با احتیاط پذیرفتنی».\",\n     \"sources\": [E + \"dome\", E + \"dungeon\", PIE_DOM],\n     \"ref_check\": [\n       {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. deme-1: 'a. Latin domus, house: DOME, DOMESTIC, DOMICILE; MAJORDOMO; b. ... DAME, DAN2, DANGER, DOM, DOMAIN, DOMINATE, DOMINICAL, DOMINIE, DOMINION, DOMINO1, ..., DUENNA, DUNGEON'. (CONDOMINIUM is not separately indexed but is transparently con- + dominium.)\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. deme-1 and index (DOME/DOMESTIC/DANGER/DUNGEON deme-)\", \"stance\": \"supports\", \"note\": \"all four indexed to deme-1.\"},\n       {\"src\": \"KLN\", \"where\": \"Klein s.v. dame, domain, dungeon\", \"stance\": \"supports\", \"note\": \"Klein derives the dominus/dominium family from L. dominus, domus.\"},\n       {\"src\": \"POK\", \"where\": \"pp. 198-199\", \"stance\": \"partial\", \"note\": \"Pokorny gives Greek dōma only implicitly (through dômos/dō); he prints 'gr. dō (*dōm) as Nom. Akk. Sg. n. or Lok.; dōma, dōmatos originally Akk. Sg. masc. *dōm-m' - which is the Greek source of English dome, not the Latin one.\"}\n     ]\n    },\n    {\n     \"id\": 13, \"lang\": \"Germanic\", \"words\": \"\", \"verdict\": \"confirmed\",\n     \"derivation\": \"An empty pass-through box: the Proto-Germanic node is *tem(b)ra- / *timram 'building material, structure', the zero-grade *dm̥- of the verbal sense 'to build' plus the instrument suffix *-ro-, with Grimm's law *d > Gmc. t. Pokorny prints it as 'ro-stem Old Icelandic timbr \\\"timber\\\", Old Saxon timbar, Old English timber \\\"timber, edifice, building\\\", Old High German zimbar \\\"timber, building, dwelling, chamber\\\", whereof Gothic timrjan \\\"build\\\"'. Watkins keeps a caveat: 'Root form *dem(a)-, to build (possibly a separate root), in: a. Germanic *timram in Old English timber'.\",\n     \"derivation_fa\": \"این گره جعبه‌ای واسط و بی‌واژه است: صورت ژرمنی آغازین *tem(b)ra-/*timram «مصالح ساختمانی، بنا» است، از درجهٔ صفر *dm̥- در معنی «ساختن» به‌علاوهٔ پسوند ابزارساز *-ro-، با تبدیل *d ← t بر پایهٔ قانون گریم. پوکورنی آن را چنین آورده است: «ستاک ro: ایسلندی باستان timbr «چوب بنا»، ساکسون باستان timbar، انگلیسی باستان timber «چوب، بنا»، آلمانی علیای باستان zimbar، و از آن گوتی timrjan «ساختن»». واتکینز محتاطانه می‌افزاید: «صورت ریشهٔ *dem(ə)- «ساختن» (شاید ریشه‌ای جداگانه): ژرمنی *timram در انگلیسی باستان timber». ادعای نورایی درست است.\",\n     \"sources\": [E + \"timber\", PIE_DOM],\n     \"ref_check\": [\n       {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference of Nourai's own (refs=None); the child node cites AHD, which covers the Germanic form.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"POK\", \"where\": \"pp. 198-199 s.v. dem-\", \"stance\": \"supports\", \"note\": \"'ro-stem Old Icelandic timbr \\\"timber\\\", Old Saxon timbar, Old English timber \\\"timber, edifice, building\\\", Old High German zimbar ..., whereof Gothic timrjan \\\"build\\\", Old Norse timbra ...'\"},\n       {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. deme-1 §3\", \"stance\": \"partial\", \"note\": \"'Root form *dem(a)-, to build (possibly a separate root), in: a. Germanic *timram in Old English timber, building material, lumber: TIMBER; b. Germanic *tumftō in Old Norse topt, homestead: TOFT.'\"}\n     ]\n    },\n    {\n     \"id\": 14, \"lang\": \"English\", \"words\": \"timber\", \"verdict\": \"confirmed\",\n     \"derivation\": \"OE timber meant first 'building, structure', then in late OE 'building material, trees yielding wood fit for building', and by extension 'trees, woods'; the modern narrowed sense 'wood prepared for building' is Middle English. The OE verb timbran/timbrian 'to build' was the ordinary Old English word for 'build' (displaced by build only in Middle English), which shows the original verbal sense of the root very clearly; cf. German Zimmer 'room', zimmern 'to do carpentry'. Etymonline: 'from Proto-Germanic *tem(b)ra- ..., according to Watkins from PIE *deme- \\\"to build\\\", possibly a form of the root *dem- meaning \\\"house, household\\\" (source of Greek domos, Latin domus)'. The one caveat is the one Watkins and Pokorny both note: the 'build' branch may be a root of its own.\",\n     \"derivation_fa\": \"«timber» در انگلیسی باستان نخست به معنی «بنا، ساختمان» بود، سپس در اواخر دورهٔ باستان «مصالح ساختمانی و درختانِ چوبِ بنا» و به گسترش «درخت و بیشه»؛ معنی محدودِ امروزیِ «چوبِ آمادهٔ بنا» از انگلیسی میانه است. فعل timbran/timbrian انگلیسی باستان به معنی «ساختن» واژهٔ معمول آن دوره برای «بنا کردن» بود (و تنها در انگلیسی میانه جای خود را به build داد) و همین معنی فعلیِ ریشه را به‌روشنی نشان می‌دهد؛ قس Zimmer آلمانی «اتاق» و zimmern «نجاری کردن». اتیمانلاین: «از *tem(b)ra- ژرمنی آغازین ...، به گفتهٔ واتکینز از *deme- هندواروپایی «ساختن»، که شاید صورتی از ریشهٔ *dem- «خانه، خانواده» باشد (سرچشمهٔ domos یونانی و domus لاتینی)». تنها احتیاط همان است که واتکینز و پوکورنی هر دو یادآور شده‌اند: شاخهٔ «ساختن» ممکن است ریشه‌ای مستقل باشد. ادعای نورایی درست است.\",\n     \"sources\": [E + \"timber\", PIE_DOM],\n     \"ref_check\": [\n       {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. deme-1 §3a: 'Germanic *timram in Old English timber, building material, lumber: TIMBER'; index line 'TIMBER deme-'.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"POK\", \"where\": \"pp. 198-199\", \"stance\": \"supports\", \"note\": \"'Old English timber \\\"timber, edifice, building\\\" ... whereof Gothic timrjan \\\"build\\\"'.\"},\n       {\"src\": \"KLN\", \"where\": \"Klein s.v. timber\", \"stance\": \"supports\", \"note\": \"Klein derives timber from OE timber, rel. to OE timbran 'to build', Goth. timrjan, and ultimately to Gk. démein 'to build', L. domus.\"},\n       {\"src\": \"IEC\", \"where\": \"Mann s.v. domn- (1), domos\", \"stance\": \"partial\", \"note\": \"Mann keeps 'demo' (to build) and 'domos, ūs' (house) as cross-referenced but separate lemmata, which is the same caveat Watkins records.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-116.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk116.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-116.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 116"
}
```


### [2026-09-05T18:09:17.828Z] TOOL RESULT

```
ok
JSON OK
nodes verified: 22/22
node verdicts: {'plausible': 5, 'confirmed': 17}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 17, 'partial': 4, 'not_checked': 7, 'not_found': 1}
books consulted: {'partial': 9, 'supports': 49, 'silent': 5} | by book: {'POK': 9, 'AHD': 8, 'KLN': 8, 'KNT': 6, 'BRT': 4, 'BQT': 4, 'HRN': 3, 'SYN': 3, 'LAT': 3, 'NYB': 3, 'SNS': 2, 'PHD': 2, 'IEC': 2, 'HUB': 1, 'TLM': 1, 'SKT': 1, 'MON': 1, 'ARY': 1, 'PHN': 1}
```


## [2026-09-05T18:09:43.604Z] AGENT

Done. `data/verification/page-116.json` written; `verify_check.py 116` reports **22/22 nodes, 0 PROBLEM lines**.

**Page 116 (book p. 86) — 2 entries, 22 nodes**
- Root verdicts: confirmed 2 (`Del, Dlgho` "long" = POK 196-197 *del-5*/*dl̥ngho-*; `Dem, Domu` "house" = POK 198-199 *dem-*, u-stem *domu-s*)
- Node verdicts: **confirmed 17, plausible 5**, disputed 0, transcription_suspect 0
- Ref checks: supports 17, partial 4, not_found 1, not_checked 7

**The 5 `plausible` nodes**
- e0 #1 Avestan `drang` "hesitation" — Bartholomae has only Av. *drang-* "firmare / auswendig lernen"; the "delay" word is Middle Persian *drang* (so Pokorny and Wiktionary). Nourai follows Tavoosi (SNS 324), a minority link. The other three forms (daraga/darəγa/drājah) are confirmed.
- e0 #3 Sanskrit `dîrğâ` — form fine (dīrghá-), but the gloss is wrong: "long", not "late" (Nourai carried over the gloss of Persian *dīr*).
- e0 #6 English `belong` — Etymonline: OE *langian* is "of uncertain origin but perhaps related to the root of long (adj.)". *long* and *along* are confirmed.
- e1 #5 Old Persian `mâna 2 / mânya` — Kent p.202 has only *māniya-* "probably *personal property* in the houses"; *māna-* is Kent's reconstruction, and "domestic, house servant" is not his gloss.
- e1 #12 English list — `dome` is from Greek *dōma* via Provençal/French, not from the Latin *dominus* parent node; the other six (domestic, domain, dominate, condominium, danger, dungeon) are confirmed.

**Bad citation of Nourai's own (not an extraction error)**
- `KNT:302` on e1 #1: impossible — Kent's *Old Persian* ends at p.219. The passage that actually supports the arrow is p.202 (s.v. *māniya-*: "from māna-, GAv. demāna-, Av. nmāna- 'abode, house'"), i.e. almost certainly a misprint for 202.

**No extraction errors found** — the JSON matches the chart everywhere I checked; nothing needed the printed page.

**Notable confirmations from the local library**
- BQT:1949 exact hit (v4 pdf p.32): Mo'in's footnote to مان gives "پهلوی mān (خانه، مسکن) «نیبرگ ص۱۴۶» … در پهلوی به جای dəmāna- اوستایی کلمهٔ mān را به کار برده‌اند", and lists کشتمان، دودمان، گرزمان as the *-mān* compounds.
- BQT:1793 exact hit (v3 pdf p.590): گرزمان ← Av. *garō dəmāna/garō nmāna* → Pazand *garōdmān/garōθmān* → MP *grsmʾn* → NP *garzmān* ("تلفظ متأخر و مغلوط"), citing Henning.
- BQT vol. 2 page drift: the دراز entry sits at leaf 289 ≈ printed 831 and درنگ at leaf 301 ≈ 843 (cited 829/841) — the vol-2 offset is `continuous = leaf + 542`, ~2 pages off the value in `refs_online.json`.

Archived 15 web sources via `fetch_source.py` (Wiktionary دراز/دیر/درنگ/دودمان/گرزمان/مادام + PIE *dṓm*, *dl̥h₁gʰós*; Etymonline belong/along/oblong/dome/don/madam/dungeon/timber; abadis for Mo'in's مادام).
