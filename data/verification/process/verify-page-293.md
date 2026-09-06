# Verification process log — verify-page-293


## [2026-09-06T22:12:46.931Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 293 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-293.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-293.json. Write /home/sfmqrb/git/rishe/data/verification/page-293.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 293` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T22:12:48.585Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T22:12:49.276Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T22:12:49.292Z] TOOL RESULT

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


## [2026-09-06T22:12:49.475Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-293.txt"
}
```


### [2026-09-06T22:12:49.488Z] TOOL RESULT

```
1	=== PDF page 293 (book page 263) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Kwer, Qwer : to make, form  (refs POK:641)  PART 2
4	#1 (parent #0) [Avestan] refs=POK:641 | čâra : to mediate ; vi-čir : to judge, judgment ☞Wi
5	  #2 (parent #1) [Persian] refs=BQT:1778,1809,1814,2258; HRN:205,242 | čâreh «چاره» : relief, solution ; vačar «وچر» : judgment ; gozîr «گزیر ( ناگزیر )» : relief, remedy
6	  #3 (parent #1) [Arabic] refs=None | 
7	    #4 (parent #3) [Persian] refs=BQT:2279 | vazîr «وزیر» : judge, minister
8	#5 (parent #0) [Sanskrit] refs=AHD | sams-krta : worked before, prepared
9	  #6 (parent #5) [Persian] refs=MON5:809 | sanskrît «سنسکریت ( سانسکریت )» : Sanskrit
10	  #7 (parent #5) [English] refs=None | Sanskrit
11	#8 (parent #0) [Sogdian] refs=SOD:32 | krty` : work, manner ; n`-krtk : not done, uncoined silver ☞Ne 1
12	  #9 (parent #8) [Persian] refs=BQT:2157 | noqreh «نقره» : silver | NOTE: Compare with the etymology of Persian word "sîm: silver"
13	--- entry 1 ---
14	ROOT [Indo-European] Krep, Krep-ed-tro : Krep: body. Krep-ed-tro: body eaters, carnivorous creatures ☞ Ed  (refs POK:620; KLN:355)
15	#1 (parent #0) [Avestan] refs=POK:620 | kerefs : body ; xrafstra : carnivorous creatures
16	  #2 (parent #1) [Pahlavi] refs=SNS:40 | xrafstar : pests, troublesome creatures
17	    #3 (parent #2) [Persian] refs=SNS:40; MON:1411,1419 | xerafstar «خِرَفستَر ( خِستَر )» : pest
18	#4 (parent #0) [Latin] refs=AHD | corpus : form, body
19	  #5 (parent #4) [French] refs=AHD:300; KLN:355 | cors : body ; corset : little body, bra
20	    #6 (parent #5) [Persian] refs=MON | korset «کرست» : bra
21	    #7 (parent #5) [English] refs=AHD:298 | corpse, corporation, corset
22	--- entry 2 ---
23	ROOT Kwermi -> redirect to Wer 2
24	
```


## [2026-09-06T22:12:52.726Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-293.json",
 "description": "Read source JSON for page 293"
}
```


### [2026-09-06T22:12:52.761Z] TOOL RESULT

```
{
  "pdf_page": 293,
  "book_page": 263,
  "entries": [
    {
      "root": {
        "name": "Kwer, Qwer",
        "lang": "Indo-European",
        "refs": "POK:641",
        "gloss": "to make, form"
      },
      "part": 2,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:641",
          "words": [
            {"translit": "čâra", "gloss": "to mediate", "script": null},
            {"translit": "vi-čir", "gloss": "to judge, judgment", "script": null, "see": ["Wi"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1778,1809,1814,2258; HRN:205,242",
          "words": [
            {"translit": "čâreh", "gloss": "relief, solution", "script": "چاره"},
            {"translit": "vačar", "gloss": "judgment", "script": "وچر"},
            {"translit": "gozîr", "gloss": "relief, remedy", "script": "گزیر ( ناگزیر )"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Arabic",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "BQT:2279",
          "words": [
            {"translit": "vazîr", "gloss": "judge, minister", "script": "وزیر"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "AHD",
          "words": [
            {"translit": "sams-krta", "gloss": "worked before, prepared", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "MON5:809",
          "words": [
            {"translit": "sanskrît", "gloss": "Sanskrit", "script": "سنسکریت ( سانسکریت )"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 5,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "Sanskrit", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:32",
          "words": [
            {"translit": "krty`", "gloss": "work, manner", "script": null},
            {"translit": "n`-krtk", "gloss": "not done, uncoined silver", "script": null, "see": ["Ne 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "BQT:2157",
          "words": [
            {"translit": "noqreh", "gloss": "silver", "script": "نقره"}
          ],
          "script_extra": null,
          "note": "Compare with the etymology of Persian word \"sîm: silver\"",
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Krep, Krep-ed-tro",
        "lang": "Indo-European",
        "refs": "POK:620; KLN:355",
        "gloss": "Krep: body. Krep-ed-tro: body eaters, carnivorous creatures ☞ Ed"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:620",
          "words": [
            {"translit": "kerefs", "gloss": "body", "script": null},
            {"translit": "xrafstra", "gloss": "carnivorous creatures", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "SNS:40",
          "words": [
            {"translit": "xrafstar", "gloss": "pests, troublesome creatures", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "SNS:40; MON:1411,1419",
          "words": [
            {"translit": "xerafstar", "gloss": "pest", "script": "خِرَفستَر ( خِستَر )"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "corpus", "gloss": "form, body", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "French",
          "refs": "AHD:300; KLN:355",
          "words": [
            {"translit": "cors", "gloss": "body", "script": null},
            {"translit": "corset", "gloss": "little body, bra", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "korset", "gloss": "bra", "script": "کرست"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 5,
          "lang": "English",
          "refs": "AHD:298",
          "words": [
            {"translit": "corpse, corporation, corset", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Kwermi",
        "redirect": "Wer 2"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-06T22:12:53.497Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T22:12:53.534Z] TOOL RESULT

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


## [2026-09-06T22:13:27.969Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','BQT','SOD','SNS','MON','HRN','AHD','KLN','HUB','PHD','NYB','BRT','WLD','IEC','SYN','SKT','FVQ','PLA','AFM','LKT','ARY','LEW','LAT','CHEUNG','FSD','WEB','ISS','TAD','ARB']:\n    v=d.get(k)\n    if v: print(k, json.dumps(v, ensure_ascii=False)[:600]); print()\n\""
}
```


## [2026-09-06T22:13:28.236Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '1,80p' tools/verify_check.py && echo ---- && ls data/verification/ | head -30"
}
```


### [2026-09-06T22:13:29.871Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

ISS {"title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967", "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute", "kind": "google_books_preview+archive_restricted", "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317936 (v.6, search-only) ; archive.org khotanesetexts0103bail (vols I-III only, lending)", "identifier": "dictionary-of-khotan-saka (substitute); khotanesetexts0103bail is vols I-III, lending-only", "lo

TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; insi

ARB {"title": "al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edition)", "kind": "archive_djvu", "url": "https://archive.org/details/mo3rb (probably the Shakir edition) ; https://archive.org/details/almo3rab_gwaliqy_f_abduraheem (F. 'Abd al-Rahim ed., Damascus 1990) ; also uc1.aa0003615705 / AAlexandrina-148752 (Sachau's Leipzig 1867 ed.) ; text on shamela.ws", "lookup_hint": "Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image.", "lo
```


### [2026-09-06T22:13:29.915Z] TOOL RESULT

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
```


## [2026-09-06T22:13:32.230Z] TOOL CALL #7: Bash

```json
{
 "command": "sed -n '80,200p' tools/verify_check.py"
}
```


### [2026-09-06T22:13:32.271Z] TOOL RESULT

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


## [2026-09-06T22:13:34.049Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"641\" POK_full.txt | head -5; echo \"=== POK grep k*er- make\"; grep -n \"machen, gestalten\\|gestalten, machen\" POK_full.txt | head -20"
}
```


### [2026-09-06T22:13:34.113Z] TOOL RESULT

```
1651:a//KC» (f.pl.) "grass' (Adams 9)] (differently Pedersen Tocharian 641). about gr. aGnp " an 
32554:References: WP. I 553, Trautmann 82, Pokorny Urillyrier 56^ WH. I 576, 632, 641. 
37426:References: WP. I 542 ff., WH. I 451 , 641 f. 
52834:Page(s): 640-641 
52860:Page(s): 641 
=== POK grep k*er- make
```


## [2026-09-06T22:13:36.347Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '52780,52900p' POK_full.txt"
}
```


### [2026-09-06T22:13:36.405Z] TOOL RESULT

```
Page(s): 640 

Root / lemma: k''el-3{*k''ehul-) 

Meaning: swarm, flock, shoal, school, clan, herd, crowd 

Material: 

In o- grade: 

Old Indie kula-mv\. 'herd, bulk, mass; gender, sex'; 

In zero- grade: 

Old Indie krstf-i. 'people, people'; 

In e- grade: 

gr. TsAoq n. 'troop, multitude, crowd'; 



Old Church Slavic celjadbi. ' servants ', collective to that in celoveki, "person' present 
celo-. 

References: WP. I 517, Berneker 141 f., Meillet BSL. 22, 18 f., Kuiper Proto-Munda 55. 
Page(s): 640 

Root / lemma: Icem- {*k''ehum-) 
Meaning: to swallow, sip 
Material: 

In a- grade: 

Old Indie camat/ and camat/'* slurps ', participle acanta-, camasa-m. "drinking bowl, 

goblet', camu-m. ' platter'; npers. cam^ the eating ', cam/5an ^ 6nnk' , osset. cumun^ slurp 

I. 

In e- grade: 

Armenian k'im-k'P\. "faux, guttur' ( *k"'ema^\ dubious is gr. £T£|J£v npsAvsv and tsjjvovtq 
[probably Tspovra] ajJEAvovTa Hes., whereas afJEAysiv in the later meaning " soak, saturate, 
absorb the liquid, squeeze '; 

In o- grade: 

with ablaut grade a npers. kam^ palate', afghan. kumai6s.\ 

nisi, hvoma {iroxw *hvama, Indo Germanic *k"emd= Old Indie camati) " swallow, devour, 
engulf, consume', hvomai. " esophagus, gullet'. 

References: WP. I 514. 
Page(s): 640-641 

Root / lemma: Icene {*k^ehus-) 

Meaning: particle of generalization/uncertainty 

Material: 

In a- grade: 

Old Indie cana, Avestan cina^ any, whatever, anyone, anybody, at all '; often negative, 

e.g. Old Indie na ekas cana "no, not at all, not'; 

Maybe alb. ca" any, some '; 

In e- grade: 



Germanic -j/>7 in Old Icelandic hver-gin^ by no means, not at all, in no way ', Old 
English asachs. Old High German hwer-gin^ anywhere, in any place, someplace, 
somewhere, in some place ' (from /7M/5/''where' + -gin) from Old High German io-wergin. 
Middle High German iergen. Modern High German irgend. (tmmor^Hittit^l^^t^^^ 

References: WP. I 399 f., Wackernagel-Debrunner III 562. 
Page(s): 641 

Root / lemma: k''enth-{*k''ehuth-) 
Meaning: to suffer, endure 
Material: 

In e- grade: 

Gr. -ntyQoc, n. 'affliction, mourning, grief, misfortune'; nachhom. na9o(; n. 'affliction, 
misfortune, ferventness, passion', rraaxu) {*k"nth-skd). Put. nsiaopai, Aor. EnaGov, Perf. 
nsnovGa 'suffer, bear, endure ' (ns- for t£- after the forms with na-, tto-); 

Old Irish cess(a)im^\ suffer' {*k"enth-t6 ox *k"enth-s-d), cessad^ a suffering '. 

Pedersen KG. II 486 assumes a nasalized cognate in Old Irish ar-cessi{ *k"et-sT-) ' 
spares, takes pity ' (meaning would be as in Lithuanian pakenteti^ be patient with 
somebody '), cymr. arbedu{*k'^et-) 'spare, look after', bret. erbedi^ recommend ' (older 
also 'spare, look after'), acorn. henbidiaV sparing, frugal, thrifty, economical, niggardly, 
stingy, penurious, parsimonious '. 

Lithuanian kenciu, k§str withstand, suffer, bear, endure'. 

In a- grade: 

Lithuanian {*pa-kanta) pakantai. ' patience ', kancia^ suffering, pain, anguish, misery, 
distress, martyrdom, excruciation, torment, torture, purgatory, rack, sting ', ziem-kintis^ 
den Winter uber aushaltend ', Latvian c/'esu c/esf suffer, bear, endure, brook ', ziem-ciesis 
( *kentsia-) ' member one to the family of the winter green plants (Pyrolaceae) belonging 
type of low shrubs: Pyrola '; 

References: WP. I 513, Trautmann 126 f., Schwyzer Gr. Gr. 1, 708. 
Page(s): 641 

Root / lemma: k''er-1 {*k''ehur-) 



Meaning: to do 

Material: Old Indie karot/{\rc\per. kuru), krnoti^ does, accomplishes ', participle krta-, kara- 
" doing, making ', m. 'hand, elephant's trunk ', kara-^ making ', m. "feat, dead, act',
```


## [2026-09-06T22:13:40.375Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '52900,52990p' POK_full.txt"
}
```


### [2026-09-06T22:13:40.428Z] TOOL RESULT

```
" doing, making ', m. 'hand, elephant's trunk ', kara-^ making ', m. "feat, dead, act', 
karman-v\. "action, work', karmara-h' smith '; /rr//- "feat, dead, act'; sam-krt^ ov\ce'\ besides 
with s- pari-skar- an6 sam-skar-, 

Avestan ksrsnaoitT makes, performs, acts ', /rara/ay- "feat, dead, act', Infin. karstae. 
Old pers. akunavam, karta-, Avestan cara^ tool, aid ', np. car^ tool ', cara^ tool, help, 
artifice' (= Slavic cara^ charm, spell', see below); 

Oscan petiro-pert^ quadruple, four times, fourfold ' (: Old Indie sam-krt)\ 

cymr. paraf effectuate, cause, obtain ', verbal noun peri, wherefore redupl. (from a 
redupl. present?) probably cymr. pybyr^ energetic, vigorous '; 

Old Irish cm//? "shape', cymr. pryd {*k"rtu-) "shape, time'; in addition perhaps Old Irish 
Cru(i)thin, mcymr. Prydyn " Picts '; cymr. Prydain " Britannia, ancient Roman name for the 
island of Great Britain ' the ending is attributed to Rhufain {Rdmanl); acorn, prit, mcorn. 
prys, bret. pred^^xme'; Middle Irish creth^ poem ' {*k'rto-), cymr. prydu^ poetize ', prydydd 
"bard'; 

Lithuanian kuriu, kurt/'erect, build, make', out of it perhaps "start a fire, heat '; Latvian 
kurt' stimulate, heat ', Old Prussian kura' build, construct, create '; different above S. 572. 

Here with the meaning " cheat somebody, bewitch ', also Old Indie /rr/ya ("action, feat, 
dead, act':) "the bewitching, charm, spell' , gr. itpaq n. " miracle sign ', nsAwp n. " monster, 
horror ', T£Au)piO(; \^tyoi(;, nsAcbpioq Hes.; the n- is Aeolic; TTsAwp, TsAwp dissimilated from 
*TT£pu)p, *T£p(ji)p; Lithuanian ker/u, kereti^ conjure, practice witchcraft ', /reras "charm, 
spell', Slavic carai. "charm, spell' in Old Bulgarian carodejb^ magician ', carii. PI. "charm, 
spell, allurement ' etc.; 

perhaps with aniaut. s- (compare Old Indie sam-skar-) Old Indie a-scarya- " strange, 
wonderful ', n. "wonder, miracle'. Old Icelandic skarsu. "a monster; giantess ', skersat " 
giantess ', skyrsem. "( nauseous) omen, sign, phantom ' (whose suffix includes the zero 
grade of es-stem itpaq). 

References: WP. I 517 f., WH. I 165, 273, Trautmann 127. 
Page(s): 641-642 

Root / lemma: k''er-2{*k''ehur-) 



Meaning: a kind of dish or pot 

Material: Old Indie caru-^ kettle, pot, pan', wherefore probably Aa/'/ra/'r water jug', kararjka- 

"cranium'; 

Old Irish co/z^Ae (though not from *k"eriJo-, but from *k"eriJo-), cymr. pair, corn, per^ 
kettle '; 

Old Norse hverrm. " kettle ', Old English hwer. Old High German (hjwerds. 

/7-extension lies before in: Middle Irish cernt " platter ', nisi, hvorn' bone in the fish 
head ', Norwegian dial. hvann6s.; Gothic fvafrneii. 'cranium'. Old Icelandic hvernai. " 
pots and pans, set of cooking utensils '. 

References: WP. I 518. 
Page(s): 642 

Root / lemma: k''eru- {*k''ehur-) 

Meaning: to chew; to grind 

Material: Old Indie c5/'i/5// "chews up, crushes ', participle curna-s, m. "fine dust, powder, 

meal, flour' (in -J- influenced the second vowel after the basis k"eru-l)\ different about 

can/a//above S. 576, 582; 

gr. Topuvri oitwSe^ t£ Hes. (assimil. from *T£puva), nopuvav [jayiSa Hes. (development 
from gradational */r"'c»/'i//7a or Aeolic form of Topuvri), nupvov n., PI. nupva (Hom.) " wheat 
bread ' (-u- in still to inquiring connection with the second vowel from *k"'eru-). 

References: W P. I 519. 
Page(s): 642 

Root /lemma: Icetuer-, Icetuor-, ICetur-xw., k''etes(o)r-i. {* k''ehut-ehsor-) 

Meaning: four 

Note: (contains?? *50/'"wife, woman') 

Material: 

In a- grade: 

Old Indie catvarahm. (Akk. caturah), catvariu., catasraht; Avestan ca^warom. (Gen. 
caturqm), catarjrdi., npers. cahar, 

Latin quaftuor {a seems, as hom. moupzc;, ©to continue); 
In e- grade:
```


## [2026-09-06T22:13:48.685Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD kwer\"; grep -n -i \"kʷer\\|k[wu]er-\\|kwer-\" AHD_watkins1985.txt | head -20; echo \"=== AHD sanskrit\"; grep -n -i \"sanskrit\" AHD_watkins1985.txt | head -20; echo \"=== AHD krep\"; grep -n -i \"krep-\\|kwrep\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-06T22:13:48.762Z] TOOL RESULT

```
=== AHD kwer
652:kwelek-. Bundle. Proposed by some as the root of Latin culcita, mattress, sack, which is more likely of unknown origin: QUILT. [Pok. kuelak- 630.] kwelp-. To arch. 1. Germanic *hwalbjan in Old English *hwelfan, hwylfan, with parallel form *hwelman (> Middle English whelman), to turn over: WHELM. 2. Suf- fixed o-grade form *kwolp-o- in Greek kolpos, bosom, womb, vagina: GULF; COLPITIS, COLPOSCOPE, COLPOS- copy. [Pok. 2. kuelp- 630.] kwen-. Holy. Suffixed zero-grade form *kwn-s-lo- in Germanic *hunslam in Old English hisl, hiisel, Eucha- rist: HOUSEL. [Pok. kuen- 630.] kwent(h)-. To suffer. 1. Suffixed form *kventh-es- in Greek penthos, grief: NEPENTHE. 2. Zero-grade form *kenth- in: a. Greek pathos, suffering, passion, emotion, feelings: PATHETIC, PATHO-, PATHOS, -PATHY; PATHOGNO- MONIC, SYMPATHY; b. suffixed form *k“nth-sko- in Greek paskhein, to feel, suffer: PROTOPATHIC. [Pok. kventh- 641.] kwép-. To smoke, cook, move violently, be agitated emotionally. Hypothetical base of possibly related words. 1. Suffixed variant form *kup-yo- in Latin cupere, to desire: COVET, CUPID, CUPIDITY; CONCUPISCENCE. 2. Zero-grade form *kwap-, becoming *kwap- possibly in: a. Latin vapor, steam, vapor: VAPOR; EVAPORATE; b. Latin vapidus, that has emitted steam or lost its vapor, flat, poor: VAPID; c. Greek kapnos, smoke: ACAP- niA. [Pok. kuép- 596.] kver-1, To make. 1. Sanskrit karoti, he makes: SANSKRIT. 2. Suffixed form *kver-6r with dissimilated form *kel-6r in Greek pelér, monster (perhaps “that which does harm”): PELORIA. 3. Suffixed form *ker-as- in Greek teras, monster: TERATOCARCINOMA, TERATOGEN, TERA- TOID, TERATOMA. 4, Suffixed form *ker-mn in Sanskrit karma, act, deed: KARMA. [Pok. 1. kver- 641.] kwer-2. Something shaped like a dish or shell. Suffixed variant form *k”ar-yo- in Scottish Gaelic coire, cauldron, hollow, whirlpool: corrt&. [Pok. 2. kver- 642.] kwerp-. To turn oneself. 1. Germanic *hwarb- in Old English hwearf, wharf (< “place where people move about”): WHARF. 2. Germanic *hwerban in: a. Old Norse hverfa, to turn: VARVE; b. Old Norse *hvirfa, to whirl, perhaps assimilated to Danish hvirre, to whir, akin to the Scandinavian source of Middle English whirren, to whir: WHIR; C. Old Norse hAvirfla, to whirl: WHIRL; d. Old North French werble, a warbling: WARBLE!. 3. Possibly suffixed zero-grade form *kwrp-o- in Greek karpos, wrist: CARPAL, CARPUS. [Pok. kuerp- 631.] kwes-. To pant, wheeze. 1. Germanic *hwésjan in Old Norse huzsa, to hiss: WHEEZE. 2. Latin queri, to com- plain: QUARREL!, QUERULOUS. 3. Suffixed zero-grade form *kus-ti- in Greek kustis, bladder, bag (< “bellows”): cyst, cysTo-. [Pok. kues- 631.] kwé6t-. To shake. Zero-grade form *kwet-, becoming *kwat- in Latin quatere (past participle quassus, in composition -cussus), to shake, strike: CASCARA, KVETCH, SCUTCH, SQUASH?; CONCUSS, DISCUSS, PERCUSS, RESCUE, succussIoNn. [Pok. kuét- 632.] kvetwer-. Four. I. O-grade form *ketwor-. 1. Probably Germanic *fe(d)wor- in: a. Old English féower, four: Four; b. Old English féowertig, forty: FORTY; c. Old English féowerténe, fourteen: FOURTEEN. 2. Latin quat- tuor (> Italian quattro), four: CAHIER, CARNET, QUATRAIN; CATER-CORNERED, QUATTROCENTO. IT. Mul- tiplicatives *kveturs, kvetrus, and combining forms *kvetur-, *kvetru-. 1. Latin quater, four times: (CARIL- LON), QUATERNARY, QUATERNION, QUIRE’. 2. Latin gua- drus, four-sided thing, square: CADRE, QUADRATE, QUARREL?, QUARRY?; SQUAD, SQUARE, TROCAR. 3. Latin quadri-, four: QUADRI-. 4. Latin quadra, square: QUA- DRILLE!. 5, Latin quadrdns, a fourth part: QUADRANT. 6. Latin quadrdagintd, forty (-gintd, ten times; see dekm): QUARANTINE. 7. Variant form *ket(w)r- in: a. Greek tetra-, four: TETRA-; b. Greek tessares, tettares,
1394:CONVOLVE wel-3 CONVULSE wel-4 cook pekw- cOoKY kak-2 cooL gel-3 COOPER ku- COOPERATE op-1 CO-OPT op-2 COORDINATION ar- COPE! kel-1 COPEPOD kap- COPIOUS op-1 COPRO- kekw- COPULA ap-! COPULATE ap-1 COPY op-1 CORACIIFORM ker-2, merph- CORACOID ker-2 CORBEL ker-2 CORBINA ker-2 CORD ghere- CORDATE kerd-1 CORDIAL kerd-1 CORDIFORM kerd-1 CORDON ghere- COREOPSIS sker-! CORGI kwon- CORIACEOUS sker-1 CORIUM §sker-1 cOoRM sker-! CORMORANT ker-2 CORN! gre-no- CORN2 ker-1 CORNEA ker-1 CORNEL ker-6 CORNEOUS ker-1 CORNER ker-1 CORNET ker-1 CORNICULATE ker-1 CORNIFICATION ker-1 CORNU_ ker-1 CORNUCOPIA op-! CORONA sker-3 CORONOID  sker-3 CORPORAL! kWrep- CORPORAL’ kWrep- CORPORATE kWrep- CORPOREAL kWrep- CORPOSANT kWrep-, sak- CORPS kWrep- CORPSE kWrep- CORPULENCE kWrep- CORPUS krep- CORPUSCLE kWrep- CORRADE réd- CORRECT reg-! CORRIDOR kers-2 CORRIE kWer-2 CORROBORATE reudh-! CORRODE réd- CORRUGATE ruk-2 CORRUPT reup- CORSAGE kWrep- CORSAIR kers-2 CORSE kWrep- CORSET kWrep- CORTEGE gher-1 CORTEX sker-1 CORUSCATE sker-2 CORVEE reg-! CORVINE ker-2 Corvus ker-2 CORYDALIS_ ker-1 CORYMB_ ker-1 CORYNEBACTERIUM bak-, ker-1 CORYPHAEUS_ ker-1 COSMONAUT nau-2 COSMOPOLITE pele-3 cosmos kes-3 cost sta-
1710:KalILYARD SCHOOL kaul- KAINITE ken-3 KALE kaul- KALEIDOSCOPE kal-2, weid- KaMA kas KAMASUTRA ka-, syii- KAME gembh- KARMA kWer-1 KARYO-  kar-1 KEEL! gWel-3 KEEL? ku-
2071:PEG bak- PEGMATITE pag- PEJORATION ped-1 PELAGE pilo- PELAGIC plak-1 PELARGONIUM pel-2 PELECYPOD ped-1 PELISSE pel-4 PELLAGRA ag-, pel-4 PELLICLE pel-4 PELL-MELL meik- PELLUCID leuk- PELOPS okw-, pel-2 PELORIA kwer-1 PELT! pel-4 PELTATE pel-4 PELTRY pel-4 PELVIS pel-7 PEN! pet-
2354:TENTH dekm TENUOUS ten- TENURE ten- TENUTO ten- TEPID tep- TERATOCARCINOMA kWer-1 TERATOGEN kWer-1 TERATOID kWer-1 TERATOMA kWer-1 TERCEL trei- TERCET trei- TEREDO tera-! TERETE tere-1 TERGIVERSATE wer-3 TERM ter- TERMINATE ter- TERMINUS _ter- TERN? trei- TERPOLYMER trei- TERPSICHORE gher-!, terp-
=== AHD sanskrit
49:. . . the Sanskrit language, whatever be its antiquity, is of a wonderful structure; more perfect than the Greek, more copious than the Latin, and more exquisitely refined than either, yet bearing to both of them a stronger affinity, both in the roots of verbs and in the forms of grammar, than could possibly have been produced by accident; so strong, indeed, that no philologer could examine them all three, without believing them to have sprung from some common source, which, perhaps, no longer exists.
50:Jones was content with the assertion of a common original language, without exploring the details. Others took up the cause, notably the German philosopher Friedrich von Schle- gel, to whom is principally due the popular diffusion of the long-lived misconception that the European languages were in some sense derived from Sanskrit. But it remained for another German, Franz Bopp, to found the new science of comparative grammar, with the publication in 1816 of his work On the conjugational system of the Sanskrit lan- guage, in comparison with that of the Greek, Latin, Persian, and Germanic languages. He was twenty-five when it appeared.
66:A number of Indo-European languages show a similar word for the kinship term “daughter-in-law”: Sanskrit snusd, Old Eng- lish snoru, Old Church Slavonic snikha (Russian snokhd), Latin nurus, Greek nuos, and Armenian nu. Albanian has nuse in the meaning “bride,” a meaning shared by the Armenian form. In a patrilocal and patriar- chal society (such as most, if not all, early Indo-European-speaking societies), where the bride went to live in her husband’s fa- ther’s house, “daughter-in-law” and “bride” were equivalents.
67:All of these forms, spoken of as cognates, provide evidence for the phonetic shape of the prehistoric Indo-European word for “daughter-in-law” that is their common an- cestor. Sanskrit, Germanic, and Slavic agree
70:Sanskrit, Latin, Greek, Armenian, and Al- banian agree in showing the first vowel as -u-. We know from other examples that Slavic w regularly corresponds to Sanskrit u and that Germanic o (of Old English snoru) in this position has been changed from an earlier u. It is thus justifiable to reconstruct an Indo-European word beginning *snu-.
71:For the consonant originally following *snu-, closer analysis is required. The key is furnished first by the Sanskrit form, for we know there is a rule in Sanskrit that s always changes to s (a sh-like sound) after the vowel u. Hence a Sanskrit snus- must go back to an earlier *snus-. In the same position, after u, an old s in Slavic changes to kh (like the chin Scottish loch or German ach); hence the Slavic word, too, reflects *snus-. In Latin always, and under certain conditions in Ger- manic, an old -s- between vowels became -r-. For this reason Latin nurus and Old English snoru may go back to older *snus- (followed by a vowel) as well. In Greek and Armenian, on the other hand, an old -s- between vowels disappeared entirely, as we know from nu- merous instances. Greek nuds and Armenian nu (stem nuo-) thus regularly presuppose the same earlier form, *snus- (followed by a vowel). Finally, that -s- between vowels is still preserved—almost accidentally, one might say—in Albanian nuse. All the com- parative evidence agrees, then, on the Indo- European root form *snus-.
72:For the ending, the final vowels of Sanskrit snusd, Old English snoru, and Slavic sniikha all presuppose earlier -d (*snus-d), which is the ordinary feminine ending of these lan- guages. On the other hand, Latin nurus, Greek nuds, and Armenian nu (stem nuo-) all regularly presuppose the earlier ending *-os (*snus-os). Here is an apparent impasse, but the way out is given by the gender of the forms in Greek and Latin. They are feminine, even though most nouns in Latin -us and Greek -os are masculine.
73:Feminine nouns in Latin -us and Greek -os, since they are an abnormal type, cannot have been created afresh; they must have been inherited. This suggests that the original Indo-European form was *snusos, of femi- nine gender. On the other hand, the common- place freely formed ending for feminine nouns was *-d. It is reasonable to suggest that the three languages Sanskrit, Germanic, and Slavic replaced the peculiar feminine ending *-os (because the ending was nor- mally masculine) with the normal ordinary feminine ending *-d, and thus that the oldest form of the word was *snusos (feminine).
74:One point remains to be ascertained: the accent. Four of the language groups in which the word for “daughter-in-law”.is attested reflect the Indo-European accent: Sanskrit, (Balto-)Slavic, Greek, and Germanic. The first three are agreed in showing a form ac- cented on the last syllable: snusd, snokhd, nuds. The Germanic form is equally precise, however, since the rule is that old -s- became -r- (as in Old English snoru) only if the accented syllable came after the -s-. On this basis we may add the finishing touch to our reconstruction: the complete form of the word for “daughter-in-law” in Indo- European is *snusds.
87:pod- (PODIATRIST). Germanic *fotuz (FOOT) reflects the lengthened o-grade *pdd-. The zero grade of the same root shows no vowel at all: *pd-, a form attested in Sanskrit.
119:The notion of carrying is represented by the widespread root bher-' (BEAR!), found in every branch except Anatolian. This root is noteworthy in that it formed a phrase né- men- bher-, “to bear a name,” which is re- constructible from several traditions, includ- ing English. This phrase formed a counterpart to né-men- dhé-, “to give a name,” with the verb dhé-', “to set, put,” in Sanskrit, Greek, and Slavic tradition. The persistence of these expressions attests the importance of the name-giving ritual in Indo- European society.
131:The other celestial bodies recognized were the sun, sawel-, and the stars, ster-3. There is evidence from several traditions for similar designations of the constellation Ursa Major, though these may not go back to the earliest Indo-European times. The movement of the sun dictated the names for the points of the compass. EAST is derived from a verbal root aus-', “to shine,” as is the word for “dawn” (Latin Aurora), divinized since Indo- European times on the evidence of Greek, Lithuanian, and Sanskrit. The setting sun furnished the word for “evening” and “west”:
150:Man and Society. For man himself, a number of terms were employed, with differ- ent nuances of meaning. The general terms for “man” and “woman” are wi-ro- (VIRILE) and *g”end- from g’en- (GYNECOLOGY). For man as a human being, the oldest word was apparently *manu- (man-'), as preserved in English MAN and in Slavic and Sanskrit. In other dialects we find interesting metaphori- cal expressions, which attest a set of religious concepts opposing the gods as immortal and celestial to mankind as mortal and terres- trial. Man is either *mortos, “mortal” (mer-2, “to die’), or *dhghomyo-, ‘“‘earthling”’ (dhghem-, “earth”).
172:The Indo-Europeans knew metal and met- allurgy, to judge from the presence of the word ayes- in Sanskrit, Germanic, and Latin. The term designated copper and perhaps bronze. Iron is a latecomer, technologically, and the terms for it vary from dialect to dialect. Latin has ferrum, while the Ger- manic and Celtic term was *isarno-, properly “holy (metal),” doubtless so called because the first iron was derived from small meteor- ites. Gold was known from ancient times, though the names for it vary; ghel-2, prob- ably “yellow (metal),” and aurum (*aus-, Latin aurum), are widespread. Silver was arg-, with various suffixes, doubtless mean- ing “white (metal).”
179:Indo-European is particularly rich in relig- ious vocabulary. An important form, which is also found only in the peripheral languages Sanskrit, Latin, and Celtic, is the two-word metaphoric phrase *kred-dha-, literally “to put (dhé-') heart (kerd-').” The two words have been joined together in the western languages, as in Latin crédé, “I believe.” Here a term of the most ancient pagan relig- ion has been taken over by Christianity. A common word for religious form (bhlag- men-) may be preserved in BRAHMIN, a member of the priestly class, from Sanskrit.
189:Most interesting are the cases where from two or more traditions (usually including Homer and the Rig-Veda) it is possible to reconstruct a poetic phrase or formula con- sisting of two members. Such are the expres- sions ‘“‘imperishable fame,” *klewos ndhg’hitom (kleu-', dhg“hei-); “holy (men- tal) force,” *isorom menos (eis-', men-'); and the “weaver (or crafter) of words,” the Indo- European poet himself, *wek”om teks-on (wek”, teks-). The immortality of the gods (*n-mrto-, from mer-?) is emphasized anew by the vivid verb phrase nek-' tera-?, “to overcome death,” appearing in the Greek word nektar, the drink of the gods. And at least one three-member formula (in the sense of the word in traditional oral poetry) can be reconstructed for the poetic language of prayer, on the combined evidence of four languages, Latin, Umbrian, Avestan, and Sanskrit: “Protect, keep safe, man and cat- tle!” (pa- wi-ro- peku).
254:The final item in most entries of the Dic- tionary of Indo-European Roots is an abbre- viated reference to Julius Pokorny’s Indogermanisches Etymologisches Worter- buch (Bern, 1959). This, the standard work of reference and synthesis in the Indo- European field, carries a full range of the actual comparative material on which the roots are reconstructed. This Dictionary presents only those aspects of the material that are directly relevant to English. For example, the English word MANY is found at the root menegh-, “copious.” This entry describes the transition of the Indo- European form through Germanic *managa- to Old English manig, mznig, “many.” It does not cite the evidence on which this assertion is based, but it refers to [Pok. men(e)gh- 730]. The entry men(e)gh- on page 730 in Pokorny’s dictionary cites, in addition to the Old English word, the forms attested in Sanskrit, Celtic, Gothic, Old High Ger- man, Old Norse, Slavic, and Lithuanian,
280:al-1, Beyond. 1. Variant *ol-, “beyond,” in: a. suffixed forms “*ol-se-, *ol-so- in Old Latin ollus in Latin ille (feminine illa); “yonder,” that: ALARM, ALERT, ALLIGA- TOR; b. suffixed forms “*ol-s, *ol-tero- in Latin uls, *ulter, ultra; beyond: OUTRE, ULTERIOR, ULTIMATE, ULTRA-, UTTERANCE®, 2, Suffixed form *al-tero-, “other of two,” in: a. Latin alter, other, other of two: ALTER, ALTER- CATE, ALTERNATE, ALTRUISM; SUBALTERN; b. Latin adulier, “one who approaches another (unlawfully), an adulterer” (ad-, to; see ad-), hence adulterdre, to commit adultery with, pollute: ADULTERATE, ADULTERINE, ADULTERY. 3. Extended form *alyo-, “other of more than two,” in: a. Germanic *aljaz (with adverbial suffix) in Old English elles, else, otherwise: ELSE; b. Latin alius, other of more than two: ALIAS, ALIEN; ALIBI, ALIQUOT, HIDALGO; Cc. Greek allos, other: AGIO, ALLO-; ALLEGORY, ALLELOMORPH, MORPHALLAXIS, PARALLAX, PARALLEL, TROPHALLAXIS. [Pok. 1. al- 24.] al-2, To wander. 1. Latin ambuldre, to go about, walk (ambi-, around; see ambhi): ALLEY!, AMBULATE; FU- NAMBULIST, PREAMBLE. 2. Latin exsul, exul, wanderer, exile (ex-, out; see eghs): EXILE. [Pok. 3. al- 27.] al-3, To grow, nourish. I. Suffixed (participial) form *al-to-, “grown,” in: 1. Germanic *alda- in: a. Old Eng- lish eald, ald, old: ALDERMAN, OLD; b. Old English (comparative) ieldra, eldra, older, elder: ELDER}; c. Old English (superlative) ieldesta, eldesta, eldest: ELDEST; d. Germanic compound *wer-ald-, “life or age of man” (see wi-ro-). 2. Latin altus, high, deep: ALT, ALTIMETER, ALTO, HAUGHTY, HAWSER; ALTITUDE, ALTOCUMULUS, ALTOSTRATUS, ENHANCE, EXALT, HAUTBOY. II. Latin alere, to nourish: ADOLESCENT, (ADULT), ALIBLE, ALI- MENT, ALIMONY, ALTRICIAL, ALUMNUS; COALESCE. III. Suffixed (causative) form “ol-eye- in Latin abolére, to retard the growth of, abolish (ab-, from; see apo-): ABOLISH. IV. Compound form “pro-al- (pro-, forth; see per’) in Latin prélés, offspring: PROLAN, PROLETARIAN, PROLIFEROUS, PROLIFIC. V. Extended form *aldh- in Greek althein, althainein, to get well: ALTHEA. [Pok. 2. al- 26.] al-4, To grind, mill. Suffixed form ‘*al-euro- in Greek aleuron, meal, flour: ALEURONE. [Pok. 5. al- 28.] [al-5. All. Germanic root. Suffixed form *al-na- in Ger- manic *allaz in Old English all, eall, eal-, al-, all: ALL; ALSO.] albho-. White. 1. Possibly Germanic ‘*albiz, *albaz, if meaning “white ghostlike apparitions,” in: a. Old Eng- lish e/f, elf: ELF; b. Old Norse alfr, elf: OAF; c. Old High German Alberich, “elf-ruler,” akin to the source of Old French Auberon: OBERON. 2. Latin albus, white (> Old Spanish alba, dawn): ABELE, ALB, ALBEDO, ALBESCENT, ALBINO, ALBITE, ALBUM, ALBUMEN, ALBURNUM, AU- BADE, AUBURN; DAUB. 3. Greek alphos, dull-white lep- rosy: ALPHOSIS. [Pok. albho- 30.] alek-. To ward off, protect. Earlier form *olek-. 1. Suf- fixed zero-grade form “alk-d- in Greek alké, strength: ANALCIME. 2. Extended form *aleks- in Greek alexein, to protect: ALEXIPHARMIC. [Pok. aleg- 32.] algwh-. To earn, be worth. Sanskrit arhati, he is worthy: ARHAT. [Pok. algvh- 32.] alu-. In words related to sorcery, magic, possession, and intoxication. Suffixed form *alu-t- in Germanic *aluth- in Old English (e)alu, ale: ALE. [Pok. alu- 33.] ambhi. Also mbhi. Around. Probably derived from ant-. 1. Reduced form *bhi in Germanic *bi, *bi- (intensive prefix) in: a. Old English bi, bi, be, by: By}; b. Old English bi-, be-, on all sides, be-, also intensive prefix: BE-; C. Middle Dutch bie, by: BILANDER; d. Old High German bi (> German bei), by, at: Brvouac. 2. Germanic *umbi in: a. Old English ymbe, around: EMBER DAY;
284:tives: a. ekhinos, hedgehog (< “‘snake-eater”): ECHINO-, ECHINUS; b. ekhidna, snake, viper: ECHIDNA. [Pok. ang#(hji- 43.] ank-. Also ang-. To bend. I. Germanic *ank- in Old Norse *ankula and Middle English ancle, ankle: ANKLE. Il. Suffixed form *ank-ulo-. 1.Germanic *ang-ul- in: a. Old English angul, angel, fishhook: ANGLE!; b. prob- ably Latin Angli, the Angles: ANGLE. 2. Greek ankulos, crooked, bent: ANKYLOSIS; ANCYLOSTOMIASIS. ITI. Greek ankura, anchor: ANCHOR. IV. Greek ankdn, elbow: AN- CON. V. Sanskrit anka, hook, avicati, he bends: PALAN- QUIN. VI. Suffixed variant form *onk-o- in Latin uncus, hooked, bent: UNCINARIA, UNCINATE, UNCINUS, UNCUS; UNCIFORM. VII. Suffixed form *ang-olo- in Latin angu- lus, angle, corner: ANGLE*, [Pok. 2. ank-, ang- 45.] ano-. Ring. 1. Latin dnus, ring, anus: ANUS; ANILINGUS. 2. Latin diminutive annulus, ring, signet ring: ANNULAR, ANNULET, ANNULUS. [Pok. dno- 47.] ans-. Loop, handle. Latin dnsa, handle: ANSATE. [Pok. ansa 48.] ansu-. Spirit, demon. 1. Germanic *ansu- in Old Norse dss, god: AEsIR. 2. Suffixed reduced form *nsu-ro- in Avestan ahura, spirit: AHURA Mazpa, Ormazp. [Pok. ansu- 48.] ant-. Front, forehead. I. Inflected form (locative singular) *anti, “against,” with derivatives meaning in front of, before; also end. 1. Germanic *andi- in Old English and-, indicating opposition: UN-?; ALONG. 2. Germanic *andja- in Old English ende, end: END. 3. Latin ante, before, in front of, against: ANCIENT!, ANTE, ANTE-, ANTERIOR; ADVANCE. 4. Greek anti, against, in enantios, opposite: ANTI-; ENANTIOMER, ENANTIOMORPH. 5. Compound form *anti-oko-, “appearing before, having prior aspect” (*akw-, appearance; see okW-), in Latin antiquus, former, antique: ANTIC, ANTIQUE. 6. Reduced form *nti- in Ger- manic *und- in Old Norse und (> Middle English un-), until, unto: UNTIL. 7. Variant form “anto- in Sanskrit antah, end, in Vedantah, essence of the Veda: VEDANTA. II. Probable inflected form (locative plural) *antbhi, “on ter sides of,” whence *ambhi. See ambhi. [Pok. ant-s 48. ap-'. To take, reach. 1. Latin apere, to attach, join, tie to: APT, (APTITUDE), ATTITUDE; (INEPT). 2. Latin apisci, to attain: ADEPT. 3. Latin apex, top, summit (< “something reached”): APEX. 4, Prefixed form *co-ap- (co-, together; see kom) in Latin cdpula, bond, tie, link: copuLa, COPULATE, COUPLE. 5. Perhaps Latin ammentum, dmen- tum (< *ap-mentum, “something tied”), thong, strap: AMENT!, [Pok. 1. ap- 50.] ap-2, Water, river. Iranian ap- in Persian ab, water: JULEP. [Pok. 2. ap- 51.] apero-. Shore. Perhaps a derivative of ap-?. Suffixed form *dper-yo- in Greek épeiros, land, mainland, conti- nent: EPEIROGENY. [Pok. dpero- 53.] apo-. Also ap-. Off, away. 1. Germanic *af in: a. Old English of, zf (> Middle English of, of-), off: oF, OFF, OFFAL; b. Old English ebba, low tide: EBB; c. Old High German aba, off, away from: ABLAUT; d. Germanic *aftan- in Old English zftan, behind: ABAFT. 2. Latin ab, ab-, away from: AB-!. 3. Greek apo, away from, from: apo-. 4, Suffixed (comparative) form “*ap(o)-tero- in Germanic *aftar- in Old English zfter, after, behind: AFTER. 5. Suffixed form *ap-t-is- in Germanic *aftiz in Old English eft, again: EFTsoons. 6. Suffixed form *apu-ko- in Germanic afug- in Old Norse dfugr, turned backward: AWKWARD. 7. Possible root *po(s), on, in: a. Russian po, at, by, next to: PoGROM; b. Latin post, behind, back, afterward: POST-, POSTERIOR; POST- MORTEM, PREPOSTEROUS, PUISNE, (PUNY); C. Latin pd- nere, to put, place, from *po-sinere (sinere, to leave, let; of obscure origin): APPOSITE, (APPOSITION), COMPONENT, (COMPOSE), (COMPOSITE), (COMPOSITION), (COMPOUND), DEPONE, DEPOSIT, DISPOSE, EXPOUND, IMPONE, IMPOSE, INTERPOSE, OPPOSE, POSITION, POSITIVE, POST, POSTS,
293:aryo-. Lord, ruler; self-designation of the Indo-Iranians and perhaps of the Indo-Europeans. Lengthened-grade form *dryo- in Sanskrit drya-, noble, Aryan: ARYAN. [Pok. arjo- 67.]
=== AHD krep
621:hréc, rook: RooK!. 4. Germanic *hraban, *hrabnaz, raven, in Old English hrefn, raven: RAVEN}. 5. Extended form *krep- in Latin crepdre, to crack, burst, creak: CREPITATE, CREVICE; DECREPIT, DECREPITATE, QUEBRA- cHo. 6. Extended form *kri- in Germanic *krik- in Old French criquer, to creak, click: CRICKET!. II. Variant form *skr-. 1.Germanic *skrik- in Old English scric, thrush: SHRIKE. 2. Germanic *skrékjan- in Old Norse skrekja, to shriek: SCREAK, SCREECH. 3. Germanic *skrainjan, to shout, shriek, in Old Norse screma, to scream, perhaps akin to the possible Scandinavian source of Middle English scremen, to scream: SCREAM. III. O-grade form *kor-. 1. Latin corvus, raven: CORBEL, CORBINA, CORMORANT, CORVINE, Corvus. 2. Greek ko- rax, raven (> korakias, chough): CORACIIFORM, CORA- com. [Pok. 1. ker- 567.] ker-3. To grow. 1. Suffixed form *ker-es- in Latin Cerés, goddess of agriculture, especially the growth of grain: CEREAL, CERES. 2. Extended form *kré- (< *krea-) in: a. suffixed form *kré-yd- in Latin credre, to bring forth, create, produce (< “to cause to grow”): CREATE, CREOLE; PROCREATE; b. suffixed form *kré-sko- in Latin créscere, to grow, increase: CRESCENDO, CRESCENT, CREW!; AC- CRUE, CONCRESCENCE, CONCRETE, DECREASE, EXCRES- CENCE, INCREASE, RECRUIT. 3. Suffixed o-grade form *kor-wo-, “growing,” adolescent, in Greek kouros, koros, boy, son: DIOSCURI, HYPOCORISM. 4. Compound *sm-kéro-, “of one growth” (*sm-, same, one; see sem-'), in Latin sincérus, pure, clean: SINCERE. [Pok. 2. ker- 577.) ker-4, Heat, fire. 1. Suffixed form *ker-té in Germanic *herthé in Old English heorth, hearth: HEARTH. 2. Zero-grade form *kr- in: a. Latin carbé, charcoal, ember: CARBON, CARBUNCLE; b. extended form *krem- in Latin cremdre, to burn: CREMATE. 3. Possibly suffixed and extended form *kera-mo- in Greek keramos, potter’s clay, earthenware: CERAMIC. 4. Possibly variant ex- tended form *krds- in Russian krasa, beauty (< “bril- liance of fire”): CRASH?. [Pok. 3. ker(a)- 571.] ker-5. Also kere-. To injure. Suffixed zero-grade form *kro-yé- in Latin cariés, decay, caries: CARIES. [Pok. 4. her- 578.] ker-8. A kind of cherry. 1. Suffixed zero-grade form *kr-no- in Latin cornus, cornel tree: CORNEL. 2. Full- grade form *ker- probably in Greek kerasos, cherry: CHERRY. [Pok. 4. ker- 572.] kerd-', Heart. 1. Suffixed form *kerd-en- in Germanic *hertén- in Old English heorte, heart: HEART. 2. Zero-grade form *krd- in: a. Latin cor (stem cord-), heart: CORDATE, CORDIAL, COURAGE, QUARRY!; ACCORD, CONCORD, CORDIFORM, DISCORD, MISERICORD, RECORD; b. suffixed form *krd-yd- in Greek kardia, heart, stom- ach, orifice: CARDIA, CARDIAC, CARDIO-; DIPLOCARDIAC, ENDOCARDIUM, EPICARDIUM, MEGALOCARDIA, MYOCAR- DIUM, PERICARDIUM. 3. Possibly *kred-dha-, “‘to place trust” (an old religious term; *dho-, to do, place; see dhé-'), in Latin crédere, to believe: CREDENCE, CREDI- BLE, CREDIT, CREDO, CREDULOUS, GRANT; MISCREANT, RECREANT. [Pok. kered- 579.] kerd-2. Craft. Suffixed form *kerd-d in Old Irish cerd, art, artist: CAIRD. [Pok. 2. kerd- 579.] kerdh-. Row, herd. Suffixed form *kerdh-d@ in Germanic *herdo in Old English heord, herd: HERD. [Pok. kerdho- 579.] kere-. To mix, confuse, cook. 1. Variant form *kra- (< *kraa-) in Germanic *hrdr- in: a. possibly Old English hrér, lightly boiled, half-cooked: RARE?; b. Middle Dutch roer, motion: UPROAR. 2. Zero-grade form “krp- in: a. suffixed form *kro-ti- in Greek krasis, a mixing: IDIOSYNCRACY; b. suffixed form *kro-ter- in Greek kra- ter, mixing vessel: CRATER. [Pok. hero- 582.] kerp-. To gather, pluck, harvest. Variant karp-. 1. Ger- manic *harbistaz in Old English herfest, harvest: HAR- VEST. 2. Latin carpere, to pluck: CARPET; EXCERPT,
656:kerep-. Body. 1. Suffixed form *krep-es- in Germanic *hrifiz in Old English Arif, belly: MipRIFF. 2. Suffixed zero-grade form *krp-es- in Latin corpus, body, sub- stance: CORPORAL, CORPORAL’, CORPORATE, CORPOREAL, CORPOSANT, CORPS, CORPSE, CORPULENCE, CORPUS, COR- PUSCLE, CORSAGE, CORSE, CORSET; LEPRECHAUN. [Pok. 1. krep- 620.]
1394:CONVOLVE wel-3 CONVULSE wel-4 cook pekw- cOoKY kak-2 cooL gel-3 COOPER ku- COOPERATE op-1 CO-OPT op-2 COORDINATION ar- COPE! kel-1 COPEPOD kap- COPIOUS op-1 COPRO- kekw- COPULA ap-! COPULATE ap-1 COPY op-1 CORACIIFORM ker-2, merph- CORACOID ker-2 CORBEL ker-2 CORBINA ker-2 CORD ghere- CORDATE kerd-1 CORDIAL kerd-1 CORDIFORM kerd-1 CORDON ghere- COREOPSIS sker-! CORGI kwon- CORIACEOUS sker-1 CORIUM §sker-1 cOoRM sker-! CORMORANT ker-2 CORN! gre-no- CORN2 ker-1 CORNEA ker-1 CORNEL ker-6 CORNEOUS ker-1 CORNER ker-1 CORNET ker-1 CORNICULATE ker-1 CORNIFICATION ker-1 CORNU_ ker-1 CORNUCOPIA op-! CORONA sker-3 CORONOID  sker-3 CORPORAL! kWrep- CORPORAL’ kWrep- CORPORATE kWrep- CORPOREAL kWrep- CORPOSANT kWrep-, sak- CORPS kWrep- CORPSE kWrep- CORPULENCE kWrep- CORPUS krep- CORPUSCLE kWrep- CORRADE réd- CORRECT reg-! CORRIDOR kers-2 CORRIE kWer-2 CORROBORATE reudh-! CORRODE réd- CORRUGATE ruk-2 CORRUPT reup- CORSAGE kWrep- CORSAIR kers-2 CORSE kWrep- CORSET kWrep- CORTEGE gher-1 CORTEX sker-1 CORUSCATE sker-2 CORVEE reg-! CORVINE ker-2 Corvus ker-2 CORYDALIS_ ker-1 CORYMB_ ker-1 CORYNEBACTERIUM bak-, ker-1 CORYPHAEUS_ ker-1 COSMONAUT nau-2 COSMOPOLITE pele-3 cosmos kes-3 cost sta-
1739:LEAGUER! legh- LEAK leg-2 LEAN! klei- LEAP klou- LEARN leis-1 LEASING leu-! LEAST leis-2 LEATHER letro- LEAVE! leip- LEAVE? §leubh- LEAVEN legWh- LECHER leigh- LECTERN leg-1 LECTION leg-1 LECTURE leg-' LEDGE legh- LEDGER legh- LEE kele-1 LEECH! feg-1 LEECH? leig-1 LEEK leug-! LEER kleu-! LEES legh- LEGACY leg-1 LEGAL leg-1 LEGATE leg-1 LEGATO leig-1 LEGEND leg-1 LEGERDEMAIN leg¥h- LEGIBLE leg-1 LEGION leg-1 LEGISLATOR leg-1, tele- LEGIST leg-1 LEGITIMATE leg-1 LEITMOTIF leit-2 LEMAN leubh- LEMMA! (s)lag¥- LEMMA? lep-t LEMURES_ lem-2 LEND leikw- LENGTH del-1 LENIENT [6-2 LENIS [6-2 LENITIVE |@-2 LENITY 16-2 LENT del-1 LENTO lento-, lep-1. LEPIDO- lep-1 LEPIDOTE lep-1 LEPRECHAUN kWrep-, legwh- -LEPSY (s)lag¥- LEPTO- lep-1 LEPTON! lep-1
```


## [2026-09-06T22:13:50.330Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT cara\"; grep -n \"čārā\\|cara-\\|c1ara\" BRT.txt | head -30; echo \"=== BRT vicira\"; grep -n -i \"v[iī]čira\\|vicira\" BRT.txt | head -20"
}
```


### [2026-09-06T22:13:50.414Z] TOOL RESULT

```
=== BRT cara
9206:•  j'i  g->  P-  *kar-  'sich  einherbewegen'. Praes.  3  cara-,  iara-'\  24  caraya-  [,  »5 cara^a\  —  Inf.  *(aire.
11222:•  j.  cara-  Adj.  'sich  einherbew^end, veisans'.
11881:•  p.  tacara-  'Palast,  königliche  Privat- wohnimg':  darayt^vt^u^  .  .  Aj"«*  imam •ram  akuiiaus  D,  /.
=== BRT vicira
```


## [2026-09-06T22:13:59.624Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== xrafstra\"; grep -n -i \"xrafstra\\|hrafstra\\|rafstra\" BRT.txt | head -20; echo \"=== kehrp\"; grep -n -i \"kdhrp\\|kehrp\\|kahrp\\|ksbrp\\|kshrp\\|Gestalt, Körper\\|Körper, Gestalt\" BRT.txt | head -20"
}
```


### [2026-09-06T22:13:59.695Z] TOOL RESULT

```
=== xrafstra
4115:FrW.  4.3;  —  'rahe  mainySus  dämanam ^'^  '5'  3i  —  y^t  titarat  °rS  matnyus dähim  alahe  .  .  antan  pairi.aväit^m  (sd.) fokuca  mattö  atarsca  /J  hg  taurvayatsm tba^ä  °rahe  mainySus  drvats  Yt  7_J,  7  7  f. ; 13;  — yint  nöit  tiurr/pttte  'rS  mainym nsit  yatavS  fairikssca  Vt  1^.44;  —  ailm dahakim..yqm..  drujim  fraca  k>rmlat  'rS mainyus  Y.(?.8;  —  aal  ahe  paityarim  frä- ijrMiat  'rö  mainyus . .V.l. 2;  'J0.3,Aog.2^; —  pairiAä  .  .  yä  uzdtihat  'rS  mainyuS  .  , paiHj>r)tSe  Yt,  A",  39;  —  taxm?m  urupi  .  . yat  barata  'tvm  mainyBm  framitim  (sd.) aspake  JaArpa  ^risatjm  aiwi.gämanam Vt./^.  29;  — paiti.psrme  'nm  mainyBm V, /o.  5;  —  fränämiliti  duhjarstavari'  °r3 mainyus  ax^amanS  Yt/p.  96;  3.^;  — naiHs  xsayät  °rö  mainyus  duzdalnS  FrW. 4.  a ;  —  xsnagiira  akurahe  mazdä  tarSidlti 'raAe  mainyius  Yt.  i.  o;  —  daxstanam  ydi Amli  'rahe  ntainySus  daxstim  V.  2.  29;  P, 2-2,  Y,  7i>,  11;  —  apayafUamah^a  'rahe mainyius  xrafstra  Yt.  21.1;  —  'rif  mainyus . .  dtävanam  daivS  V.  ig.\;  —  vJspB.mahr- käatca  pairi  drvatat  yat  -rst  mainyaot VL/_j.7i;  /0.118,  Y.2-j~-i,  V.'/o.ie;  — ai  duida  °ra  mainyS  V.ii).^;  g,  1,44,  lt. 10,  Yt//.  19; —  iaÖx  dusda  'ra  mainyö V.  i^,  1 2 ;  —  *'rahe ''  *mainy9us  duzdamanH Y.  Ö/.  2;  V. /p.6;  —  skutara  "ra  mainyö V.  79. 3;  —  "rS  mainyus  pouru.mahrkS (Stveri.)  Yt  10. 97 ;  usw.
4122:—  kahyäcit  'yavanqm  xrafstranqm  V.  16. 12;  —  ma  hwä  ^'yavS  manisiis  * ästaraita Vyt.  J7(?);  —  kat  tat  dqma  "yava  (statt NSn.)  'J  altarfhqm  drlmanam  V.  ij.  5.
8857:(sA)  Jasti  N,/oj; — ^kaAyl^^"^  dahmanqm sao^räoa  (si)  *ratu/rU  N,  40 ;  —  draos (sd.)  z-iJ  paiti  söinma  unam  vä  katcit  vS paiti  sidaranqm  N.  IQO;  —  kahmäicit yanhqm  jasS  Yt  13.  41;  41,  V.  7.  7: —  yahmäl  kahmäiHt  na^nanqtn  va ä'ird  baoiöTm  baraiti  ahmst  kahmätHi naimanam  .  .  paiH.jasalH  ütars welcher  (Seite)  her  nach  irgend Seite  der  Wind  des  Feuers  Geroch  ver- breitet, von  der  her  nach  irgend  einer Seite  wendet  sich  ^.."  V.iV.So; — pasBm .  .  7-ohu^aorvm  vä  käcit  (IS.)  vä  gaona- nqm  hamS4;aontm  (sd.)  Yt.  8.  58;  *Aog. »7;  —  di^e  saite  kahyJat . ,  xrafstranqm V.  16.12;  —  kasatinm  kaAhhcit  va^wa- nqm  A.  j,  11;  — 'in  Verbindung  mit  anya- A(tj.  '.ilius  (]uispiam':  anys  kasat  ar?hsiis astiatö  N.  6j.  a)  Piur.  im  Sinn  unsres zurück  weisenden  'welche,  solche', Zeichnung  einer  uobestimniten  Zahl:  äjal aaaelqm  . .  hj/il  (APa)  upaÄsSi  (sd.)  N. io().  a)sva.|jedermann,  jeder,  quisque' fravalayS  . .  ijp^m  aZi?mnil  (sd.)  havä käHt  (NSf.)  näfäi  ". .  suae  quaeque  origini" Yt.  13. 66;  —  äai  anyähu  ratufrisu  latai>rS *kai3h^scil^^  bar?smqn  frastaraitys  (sd.) N.  ;o2;  —  sdäi  (sdl)  *Aahyä^t^*^  paiti V.33. 1 1.  a)  mit  Gen.  part:  hazatinm vairyaiiqm  . .  kßsalia  alsqm  vatryanqm  . . "tausend  Seebuchten  .  .  und  jede  dieser Seebuchten  . ."  Y.  Ö5.4;  4;  —  kasHt avAius' (sd.)  aslvate  F.  36';  P.  y,  V.  7.50, iO- 19,  P.43  (kakynat);  —  Hat  vö  kasat masyjiiqm  .  .  ¥1/5.53;  Vr.^.5;  — yäva- ranJ  kascit  sao^antqm  Y.12.J;  —  iäat tanuHam  V.  16.10;  —  ka^häscit  tanunqm H.  /.  5 ;  —  kahmai^t  häiqm  "Jedem  der Seienden"  Y.J5.8;  /fl.ii',  F.^b'«;  — kakyäcii  hstqm  V, /2, 4;  —  ijmcit  paiti cairusanqm  (Stverz.)  V.tf. 31  usw.;  — a^'ahe  pasvd  {sA.)  ..  aliiqm  *kakmaicit*''^ td'ia  */rayarihqm  (sd.)  N.  65.  a)  mit
9549:KompA-,  E.  —  ai.  ;(■.'■/>,;  (IS.) 7),  Ta.y.karp,  arm. LW.  kop.  —  Vgl.  huk4i>>pta-  iind  irafstra-  No.«. —  I'ü. !  karp,  (zu  F.) :  karf  i  güsl;  Pü. ;  kaiet^ram.
10635:•  j.,  g.  xrafstra-  n.  i)  im  gAw.  'wildes Tier,  Raubtier":  atibyS  mas  äsä  syasdat (sd.)  yentat  ahmat  aurunä  'rH  (AP.)  Y. $4.  9.  a)  im  Plur.  als  Bezeichnung  für die  nicht  sesshaften  Religionsfeinde  und deren  Gölter,  sva.  'Raubgesindel':  anä mq'ira  maxist?in  väurüimaidl  (sd.)  Tä (A'P.)  hizvä  Y.  28.5;  —  pari  *vä  vJspäis pars  vaox?mä  dalviliscil  °räis  maSyäis^ä "losgesagt  haben  wir.  uns  von  allen  Xraf- stra^ (allem  Raubgesindel),  den  Daivas wie  den  Menschen"  "  Y.34. 5 ;  verwendet  Y. ig.  2.  2)  im  jAw,  Bezeichnung  fUr  alle schädlichen  ((/iZÄischen)  Tiere,  bes.  der niederen";  paitUtätie  a/astaca  zBüdiftaca apayantamaheca  a?prahe  mainyius  °ra Yt  21.1;  —  duye  Saite  kahyäcit  ar>rö.- mainyavanqm  "ranqm  ava.janyäl  V.  16. 12;  —  ähva  vyar?hähva  (sd.)  e^mB  'ra ham.bavainti  yim  tnasyäka  spis(sd.  tiqma aojaitt  V.  z/. 3;  —  *maxSiMhrpa  ..*akara- tum-driwyi  (sd.)  ya%a  taehdistäiS  'räis V.  7.  2;  —  Y.  ig.  2:  s.  unter  1.
10637:•  j.  xrafstra-gan-  m.  'Xraßiratmt-^,  ein Werkzeug  zum  Töten  kleinerer  schädlicher Tiere"';  °lrain>m  *ainim  baraili  V.l^.z; —  yalsam  sayanam  d^aurune..''trayngm (statt  NS.)  V./4-8.
15093:•  j.  paitt-ätät^e,  -ätätayae-i^  Inf.  '(und) zu  widerstehen,  zu  bestehen',  uzw,  iAxfl'ische Wesen  und  Anfechtungen;  a)  mit  Akk, •/Äf  ajastaca  tlizdi^taca  .  .  xrafstra  Yt. 21. 1.  b)  mit  Gen.:  't}e  .  .  druj5  'tSe . .  iialsiirtis  Yt.  ij.  129;  'o.Si  ^^°i  '3^^ i3S-'38'°,  142,  Y.6S.B,  60.4,  ?'■  '7'' YL(7.4i,  5.12,  y.130,  131,  136',  137'. 138',  Vr.20.  2,  V.  20.3'J,  S.2.i3i  — avaiAAi  pairikayäi  'fayaSca  paitiscapta- yaica  Y.  16.  8.
21263:. ,  aparaöhayäe  y  v  naimsm  y  v  ä«'- /um  y  V  cahru/um  y  V  paatartkum '^■ig.y,  Y.6.32*,  l6.2*; — yä  *xsudra(ßd.) *y'il  y  yazmti  y  v°  *hqm.ralhwpnii y'v' ..  N.  61.  n)  in  aülimiliger  Ver- wendung; xrafstrMn  ava.janaita  maotrim dänSjiaritm  y"  v'  hama  duyt  laile  kahyä- cit  .  .  xrafstranqm  ava.janyät  y  v  .  . zaOta  "das  Xr.-Geschmeiss,  die  kömer- schleppende  Ameise  soll  er  im  Sommer töten,  zweihundert  Stück,  dagegen  (zwei- hundert Stück)  beliebiger  Xr.s  soll  er  im Winter  töten"  V.  16. 12  {?).
25912:—  'tun  iayalanqm  YtiO,  2;  —  -Dm paitiitanam  hatargrim  . .  baivari  V.j.31; Yt5.2i.'5.3,  ;j.7i,  H.j.s,  sVar„8,  Yt, ig.d;  —  %rii 'tat! käta.H%anqm  "mit  drei mal  hundert . ."  V.4.  5;  Wytig.  a)  mit attrib.  Einerzahlen":  ca'^warasca . . garays cahwarpsat3m(sd.)ia  dvaica  °ite  (ND.) dvaica  hazanre  Ytjp.  7;  —  %räyS  *°la (NP.)  F.  2j;  —  yä  ..  vazinH  xsvas  *°tais'' (ab  Nom.)  haxarfnnila  Yt  5.  95;  — navaca  yaskS  navaitlsca  navaca  °ta  navaia hatatira  rtavasJs(,sd.ya  baevqn  V.  22,  z;  Yt. ^.?-  S9-  ^)  ™''  Gen.:  duye  °ite  kakyä- Ht  .  .  xrafstranqm  V.  16.  12;  4.  2i';  — tisrS  'ta  upätananqm  V.  4. 1 1 ;  1 1 ;  — ia%w3rS  'tu  äirpjaokanqm  V.<?.  84;  ff.  21';
27064:•  j.  spi§-'>  n.  'Laus,  Milbe  (od.  dgl.)': Sat . .  xrafstra  hqm.bavainti  yiin  masyäia spis{NS.)  nqma  aojaile yim  tnasyäta  yaom yavS.kva  nnganh}nti  vastra  vasträhva ".  .  die  Xr.  . .,  was  die  Leute  'Laus' nennen,  was  den  Leuten  das  Getreide  in den  Speichern  wegfrisst,  die  Kleider  in den  Kammern"  V.iy.^'K
27177:mit  Abi.  'vor  — ':  ySi  , .  armaitlm  . . b>nxtqm  (sd.)  . ,  avatatai  . .  alifye  mai' ala  syazdai  yava^  ahmat  aurunH  xrafstra ".  .  vor  denen  weicht  Asa  gar  sehr  zu- rück, so  weit  als  vor  uns  die  wilden  Raub- tiere" Y,j4.  9.
30091:—  irpiuxhai  vacanhqm  xsayamnB  (sd.) •w?i>  vass  Y.31, 19.  a)  gAw.  IS.  und IP.  sva.  'durch,  im  Reden,  Sprechen'*'; ySi . .  aiiitnim  varyäm  (sd.) . .  o^ilt/  'tubls Y.  49-  4i  —  urvä  .  ,  x^äii  ^aohanäil 'zvascä"'  asahyä  nqsvä  pa%S  "die  Seele  , ., da  sie  in  ihrem  Tun  und  Reden  vom  Weg des  Ai^a  abgegangen  ist"  Y. 51.15; '"'zvä'f>  av?r>ts{si.)  Y.^lj.  i;  —  anä  mq^rä mazist>m  vüurSimaidc  (sd.)  xrafstra Y.  atV.  5,  a)  in  Verbindung  mit  »jcob-: ydi  rJ  fyao%anäis  särffitf  (sA.)  ..  *'zv3^^ uxlaii  vaivhJus  manavAs  Y.  5/.  3;  — vahUtfm  'svä  ux%äis  , .  }>änü  . .  tastsibyä syadkatiiJ  v?r3zyat  (sd.)  Y.  47.  2.
=== kehrp
4454:•  j.  an-ästravana-'*  Adj,  —  ?  — :  srinm kshrpsm  'nim^''  bavahi  ya'ia  kava  syJ- FarsänS  Az._j,
6536:Vfil.  aiakva-.  —  Pü. :  fehlt. •  j.  azay-  m.  i)  'Schlange',  ein  ^ÄiÄisches Tier:  /<fiws.tara  ya^a  'zayS  xsvoewanhs V.iS.ßs;  —  'Sinam  udarS.>rasanam  .  . °iinam  spakanqm  kahrpunanam  (sd.)  V. 14.%.  a)  Sing,  in  koll.  Sinn:  äat  ahe paityänm  .  .  'zimca  yim  raoioibtn  (sd.) zj'rtM/a..V./.2''; — yai3  '%wä  niHt  aiwi,- Jruzilnti  •iisea  arütuiisca  "damit  dir kein  Arg  antun  können  Schlangen  und  .." YL5, 90.  2)  schlangenähnlichcs  Untier 'Drache,  Ungeheuer'":  'zdis  sairitaAe simahe  vlsS.valpahe  Y.().3o;  —  'zis .  . gäuitava . .  vTraja  Aog.  ~S;  —  'leis  vJlspahe N.  48;  —  ktrasäsps  .  .  yS  jartat  °ilm (sd.)  yim  aspB.garpm  mnganm  ..
7817:•  g.  a^nman-  n.  'Stetigkeit;  Unaufhörlich- keit': al  kahrplm  utayäitJs  äadät  armaiti^ 'mä  (AP.)'*  "und  Arm.  verlieh  den  Leibern Dauer  und  Stetigkeit"  Y.jo.;.  a)  LS. °m7nT  als  Adv.  'stets,  ewiglich;  unaufhör- lich"'; yi  'mSnl  mazdn  srävi  ahurd  "der ewiglich  MAk.  heisst"  Y.  45. 10;  —  yaii' gqm  karaps  usixscä  (sd.)  alhmUi  däii yücä    kavä   *'mJnI^^    urüdSyatä  (sd.)    Y.
8199:•  g.  'uta-yütay-  i)  Adj,  'perpetuus, dauernd,  beständig':  data  vi  amtr^tascä 'yUitl  (ASn.)  haurvatas  draonH  "schenkt, o  If.  und  A.,  euer  beständig  währendes Gut"  Y.JJ.8.  2)  f.  'perpctuitas,  Dauer, Beständigkeit':  aimrttäitl  *asaottö  urvä ais3  'yatä  (LS.  &v^  'immer')  ja  furqlsadm (sd.)  drfgvats  Y.  4$.  7;  —  ap  kshrpim 'yüitls  (AP.)  dadat  ärmaitii  qnmä  (sd.) ".  .  corponim  perpetuitates  .  ."  Y.jo. 7.  a)  mit  totfl"-  f.  verbunden:  ha  zi nS  husöi^»mä  (sd.)  Aa  «Jf  'yüitim  dat t^Tsim  Y.4S.6;  —  'yüitl  (IS.)  t^vlsim *gatJ/'i(s±)  vasfmTY.43. 1.  a)  in  Dual- verbindung damit:  Ayal..  M^t  (sd.)  . .  haur- väta  am}r?tata  .  .  ahmai  stsi  dqti  (sd.) iivin  'yBiiT(AD.)  Y.^lj.io;  Si.j^ 34.11.
9062:mit  lii,  niy  'eingraben,  verscharren':  yö iiars  .,  irtri'iusS  zumc  kshrpa  nikaiiiti  V. j.  40  PüZ.;  —  altafia  ..  aSta  vastra  fraca k3r3ntm  niia  kanaym  V.  7.  12;  —  yat aialta  zimS  nikante  (3SPM.)  späiias^a  .  . ttimskante  (sd.)  V.J.  36;  8;—  jarW  (sd,) .  .  zjme  nikante  (NDf.)  V.  7.  47;  j. ra.  a)  II  'vergraben'  sva.  'aus  der  Er- innerung verschwinden  machen,  in  Ver- gessenheit bringen':  uta  lyt/'  kunavahy ava''faiy  a''ura''mazdä  nika''tuv  "und  was du  tust,  das  soll  dir  AHM.  in  Vergessen- heit bringen"  Bh.  4.  1 7  ''.
9158:—  ks  UKtmSm  (sd.)  cBrM"^  . ,  pu'^nm pure  Y.  44. 7 ;  —  kjrmaomi  "iwam  hacat.- pu^rqm  V.2^.6;  — yat  k^rmaot..  *amar- /an/a  fasu  vira  V.p.  4;  Yt5.  30,  /j.  16 [k^rmavani);  —  matdqmcä  (s,  i  c)  büiricä kjrpsvä  .  .  xrapaitl  (sd.)  Ayat  ahmat  aibi Y.  4n.  I ;  —  yi  umm  pinmm  k?rpnaoiti  . . bantjm.'a  drum  k^rmaoUi  V.  22.5;  uj.^%, Y.  10,13;  —  \hatm  parsam  hami'i''iyam akunaus  Bh.  4.2;  2%  3;  —  ya'ia  asym amasyq  (sd.)  kmnaväni  .  .  karh'qn  Yt. 5.30;  —  ts  k>rmava  mdwaire  ajyamnem V.2.z8;  36  {kirnittol);  — yat  amm  patti.- irist»m  /rä.nastirii  kjnnaaiti  V.  r/,  42;  — armadsth  atiyh  äps  k^nnaoi  Yt.5,78;— >J( Im  firasJmisA.)  *k3rjnaon'^^  ahsm  Y.30.9; Yt.iil.ii  (k^rMavqn),  89  {k»rma7,;li) ;  — yezi  iidit . .  mazdayasna  . .  kahrpsm  kvars.- dar^slm  (sd.)  k:>rmavqn  V.5,14;  13  (wo k^r»nai)t,  statt  Plur,);  —  raeko  (sd.)  mS haca  aühij  s»mat  vatihö  k^rjnaoiii  Yt. iy.2o;  10.2S;  —  ya  *a/r3.ur7'isval  (sd.) hrmavainti  irmi  Yt  13.  z6;  —  I  av<^taiy (^urJ'mazdä  ^mazänam  (sd.)  kunautiro Bh.  4.'6;   —  ava'^  adam  patipadam{%iL)
9326:•  j.  kahrpuna-  m.  Name  eines  a'aft'ischen  j  schleppten  sie  die  Weiber  den  Menschen Tiers'*:  baivan  alinam  spakanqm  •■nanqmX-^^^'  Yt. /g.  80".
9535:kahrp-  Noten
9545:•  j.,  g.  kahrp-,  ksr?/-^'^  f.,  n.'>  'das  sieht- ' bare  Äussere  jedes  Wesens  und  Dings, , äussere  Erscheinung,  sichtbare  Gestalt': sraliiqm  at  tSt  'p/m  (AS.)  -^pam  (GP.)  j ävaedayamakl  tnazdä  ahurä  iinä  raota  . . avat  y.ll  hvarS  aväcT  Y._J(*'.  6;  — para avtiiriAe  hü  "^warstö  (sd.)  'pya  (LS.)  Y. ' /p.  8;  —  asmamm  ,  ,  y3  hislaite  ayanhs 'pa  (IS.)  x^amahe  (sd.)  ".  .  mit  der  Er- scheinung von.,  (sva. ..  anzusehen  wie..)'' YL  13.  2.  A)  insbes.  von  lebenden Wesen;  auch  vom  gestalteten  Stoff  selbst 'Leib,  Körper';  i )  von  Menschen  und Göttern:  aj  'psm  (GP.)  utayuitil  dadat ärmaitis  qnmä  (sd.)  Y.jo.  7;  — ■  yd>!a varsnahe  'palie^^  dsus  (sd.)  N.  7o(7;  — paiti  ainii  .  .  'p^m  .  .  gaia/ie  .  .  °ppm  .  . säJiar/  .  .  "Pim  .  .  abmatr/aAe  .  .  'P^m ..jahikayüi  ..  -p.m  Y.//.  30-32;  32;  — avqm  'P^m  yazamaide .  -yqtn . .  k^r^säspahe Yt /?.  61;  Az._J;  —  üjasat . .  viriisra-fitä ..vätahe  'pa  (IS.)  Vt/4-2;  —  mi%nm..
9573:•  j,  karanavant- Adj.,  PPA.;  s.'kar-Tati\kairy3  yava  gaestis  gaöavarS  Y.g.io;  — No.  S.  kshrptm    .  .  yam   sämake  (sd.)    'pake   Yt
11964:•  j.  tanu.kahrp-  Adj.  'die  Gestalt  der eigenen  Person  habend' (?) '*,  von  Söhnen: puHrS  zayanle  °pa  kiArpa  Vyt  V;  3.
12243:•  j.  t^yah-  Adj.  (fem.  •yeil-)  'der  tapfrere,  |  xiapatis  .  .  'rys  .  .  kshrpm   ra^wayäti
15293:Name  eines  aus  Milch  hergestellten  alko- holischen Getränks,  wohl  'Kumis':  x^au- drinqm  °yat)Aam  N.  67;  66.  Undeut- lich: rafu/ris  *nairiAayS  kihrpa  nöii 'yatshs  nsit  suns  k?hrpa  'yatfho  ratufril v?hrkayä  kshrpala  'yanhaca  N.  5p; mananhs  nSit  'yar?hs  N,  6y  *'.
16038:•  j.  päurva-  m,  EN,  eines  Mannes*':  tarn (näml.  artdvJm)  yazala  'vö  yd  vifr3  tiai'äzB yat  dim  usca  uzdvqnayat  .  .  %raitaoiid rrunyahe  kshrpa  ka'hrkasahe  ".  .  P.,  der kundige  Schiffer  . ."  Yt.  3. 6 1  ">.  [S.  noch *atvs.gava-  No.  4.]
17809:•  j.,  g.''  fravaäay-  f.  ^Fravasay*'>,  Be- zeichnung für  das  dem  Gläubigen  eigene Unsterbliche,  das  Element,  das  schon  vor setner  Geburt  vorhanden  war  und  ihn  über- dauert. So  lang  der  Gläubige  lebt,  wacht seine  Fr.  als  Schutzgeist  Über  ihn.  Die Gesammtheit  der  Fr.  der  Gläubigen  aber spielt  eine  ähnliche  Rolle  wie  die  indischen pitärah,  die  römischen  ««««■:  'sayö  hütti^ Aatqm..aigAu^qm..bUsyantqin{Sf.^^i  m.) a!'aanqmYt.i3.2\;—ä  hätqmca  anhusqfnca zätanqmca  azätanqinca  asaonqm  ilajasmiu °sayd  Y.  öj.  6;  —  aat  anyaisqm  'say!> jvanqm  narqm  aiaonqm  aojyehfi .  ,  ya^a iristanqm  "aber  im  übrigen  sind  die  Fr. der  lebenden  Gläubigen  stärker  als  die der  gestorbenen"  Yl;_j.  17;  —  vispäbyö asaonibyS  *nbyS  y3  irlrüu/qm  .  .  yasia jvantqm  .  .  yäsca  narqm  azätanqm  Y. 24-5;  —  vispanqmca  änhqm  alaonqm asaoninqmla  ila  yaxamatde  °stm  Yt,  ij. 148';  —  neben  'aAs-,  *da?nä-  usw.; alaonqm  aiaoninqmla  ahümla  dafaqtnca baoiasca  urvarumca  °slmca  Y.  26'.  4;  — gai^ssca  asdsbJlca  us'tänqsca  kahrpasca Uvlilsca  baohasia  urvämmca  'sTmca  Y. 55,  I ;  —  xardkuitrahe  . .  'Am  . .  sravä  . . dainqm  . .  varvtifmca  tkais»nca  Y.  16. 2 ; —  manä  . .  dalnä  . .  urunS . .  'say!)  (als  AP.)
20276:mit  frä  i)  'als  Norm  au&tetlen,  an- ordnen, befehlen';  yät  ySsia  framTma%a (3PPfA.)-'>  ya  Moiya . .  vaxlmtz dafvdsuitä (sd.)  "seitdem  ihr  das  verfügt  habt, dass . ."  Y.  J2. 4",  s)  Med.  'sich  messen, erproben  an  — ':  'framata-.  3)  'ver- bilden, umbilden,  verwandeln  in  — '  (Instr.): yal  barata  aursm  mainySm  framitim aspahe  kshrpa  "dass  er  den  AM.  ritt,  den in  Rossgestalt  verwandelten"  Yt75. 29.
21224:Au.irixt^m(sd.)..trinaxtiYt.io.6B.  a)init' vorhergehendem  vTspum  S  aAm3J  'donec, bis':  näa  difyäi  aäa  ^rityäi  vJsp^m  ä ahmst  y'  hl  han/asaitt  yaia  iahrutiim *yär?  N.42;  43,  Vd..#.  3)  mit  dem Konj.  (oder  Inj.)  in  fiiCuiischem  Sinn:  yai (s.  V)  .  .frasna  (sd.)  paiti.mravSm  y  mgm ftrpsai  axtys  Yt  j.  8z;  —  y  irista  paiti us»hiltqn  ..  äa%aite  fras>m  vasna  anhui Yt  Jp.  1 1 ;  —  y  astvatjTTls  fraxHäite  .  . avaaa  drujpm  nilbarat  Yt  jg.  92  f.;  —  y yavs  dqyät  aal  daeva  :^um  (sd.)  y^  ■  ■ äayap  äaO  ..  V.,;.  32;  —  asti  zT  ana avavai  uxäata  (sd.)  ya'äsa  y  dim  vJsp5 ar»huf  äsaxiat  (sd.)  . .  pairi  irtkyqstätat (sd.)  haraite  Y.ig.  10.  /)  im  Sinn  des lat  Fut  II:  aSaha  hr  tanüm  . .  »idaihyqn vTsppm  3  ahmat  .  .  yat  (s.  c.)  frä  vayS patqn  ,  .  äat  y°  ('wenn')  ht^  frä  vayS patqn  fra  urvara  ux^qn  nysttiä  apa.- tacin  .  .  ariala  .  .  kahrptm  kvanJansJm kmnaot  V.  5.  i  a  £ ;  —  *fra  *ma  . .  *gara- yffi/ (sdj)  y  raful  fritsil  *a/asäi  N.  ip;  — y  dim  iatäj..paia  *avaMääiV.S.too(t); io3(?); — yai  nSiriAa  voAunls  atwi.vamäl y  (nachdem')  Al  'kray3  xlafiia  sacatüe V.  16. 8;  — y  ('nachdem')  kl  tanul  hilkvi Mymii  pqsnu  bavat  pascaSa  .  .  jasBtt  V. p.  31.  a)  mit  vorhei^ehendem  pasca 'postquam':  aem  ai^he  asti  utvanam  yal (s.  V)  nä  pasla  y  usthtÜäi^^  .  .  änV aÄOT  ■  upajtuyät  V.  18.  43;  s.  V.  18.  49 (unter    4).  b)    mit    vorhergehendem
22023:mit  ä  Kaus.  i)  'Jemandem  (Dat.,  Gen.) etwas  zusprechen,  zu-,  überweisen,  widmen, weihen':  sral/lam  al  tdi  kshrpim  k3krpqm ävaläayamaAl  "pulcenimam..  tibi  formam formarum  dedicamus"  Y,jö.6;  —  stüts garS  .  .  oAurSi  .  .  acä  avafdayamahl  Y. 4'-  ^;  4-  i;  —  hai'ake  urunS  Aaomq ilva^ayainahl  Yi.li.i;  i',  13,  16',  21, 4.  2,  Y.  4.  2  ff.,  24. 1,  3',  5;  — yai  usäähm yat  ävisttm'*''  yäha  dri  ava^ayaf  ahurS .  .  ya%a  dis  az>m  yS  zaota  3va^yemi  . . viovä  däityqm  avistim  Vr. //.  19;  19;  — paili  tl  m^rvya  . .  imä  srvä  v  " imä  srvä  ävasoayemi  "ich  weise  dir . .  diese Nägel  zu,  ich  überweise , ."  V.  77. 9 ; — Aaoms aviits^*^  aiwi.visis  YL  10.  i^o.  2) 'Je- mandem (Dat.)  etwas  anvertrauen':  ahmät fumankl  ävaidayamaidl  gag%Bscä  tan- vasiä  . .  Y.5&  2;  —  aat  dll  ava^ayamahi ga%äbys  . .  Y.5J.  i;  i.
23661:•  j.  v»r3*rl-gan-  ■>  :  -^ra-y/i-  Adj,  'wehr-  ^^  ^j/i  mainyavanam  yazatanam  sayS.- haft,  siegreich";  a)  von  a)  Göttern  und ,  i^^gj  .  _  .„5  ahuraiatö  Yt  /4.  i';  —  sonst ß)  Menschen;  zu  a.)-.  ahumi  matdäi  .  . ;  stets  mit  aAuraläfa-.  äjasat  vassmnS  'nS '%r<r}ne  ^aäat^Mhai  WT.n.i;^.S5.ä,;aAuralatS  ha  kihrpa  varasake  Yt.  14. —  'hraja  (NS.)  sraasS  .  .  a/yS  Y.  57.  3,  j  ,  j  .  j  (1,3^^^,  AiÄ^^ta},  7  {gSu/  hhrpa), 14;  j2;  —  sraosS  .  .  huraols  •%raja  V.  I  g  {aspahe  k>hrpa),  11  (kZ/tbä;  kshrpa), ig.  40i  Vr.  /5.  3,  /(;.  i,  Yt  //.  7,  Y.  2.  7, 1  17  („a^/  Ä;'/!^?»«),  19  {m>nr/aAe  kfhrpa), 57.1,  Az.6;  —  jr.rw'ijAe  ..  '%räjara  Y. ;  33  {ma^ahe  kihrpa),  25  {batahe  k?hrpa), i.  7;  —  -iflomö-  .  .  'ärfl/a  Y.9. 16;  Yt  27  {j/fra^^  kihrpa);  —  'nS  ahuraoats  .  . '4-57>  —  <nryamam>M  ..  amavanhm  ys  _  upaJiaxtö  a.mimar>ha  süja  nijainH '%rajamm  -^.54.2,  G.i.6;  —  fravaiayS  hamfrp-^sYtio.T=i.;i4.(>2,6z;—''hmai ..ha^ra  väta  '%räjana  Yt./J.47;  —,  dahat  'nS  aiuralatB  fnxBtsxä  bäzvä  aojs Aähra  vaia  •>rajanS  (sUtt  IS.)''  Yt  JO.  1  yt.;^  ag;  i_  7*1,48,  54;  —  am?inca  Au- 9,  12.  4,  13-  48.  ß)  '%raß  taxmB  %rag-^ :  /^Äw,  .  .  •«j-mA  ahurdmhm  Y.  2,  6 ;  /ff. /fftwi^  Yt5.6i;  Az.2;  —  yaha  'hraja  j^  j-^.  ^g^  Vr.  2.  8,  Yt  14.  5%  V.  /p.  37, vtmat.pflafts  fraxStane  Y. p.  20;  — /Ämi  l  Az.  7;  —  "«b-**  ahuralatahe  vanaintyism asti  aiava  ''iira/a  '^. 58-  r,—  ^"r^oiS . .\  „paratate  Vr.  1.  6,  Y.  /.  6;  Yt  /4.  o,  43, ^Ä  taxma  saosyatüS  ySi  taxma  'hrO/ans.  ^g_  a)  vtn%raynahe  (nUml.  afun-) (NP.)  YL/j.  38;  —  buyama  J-ic^on/Sl  heiast  der  20.  Monatstag:  -»aÄ^  ff Ä«r«3j- ^jflMÄ  •%räjat0  Y.70.4.  Pß)  bes.  /a/i,;  S. /.20;  vgl  2.20.  Y.  16.  5;  —  a/iäi- vom  SaoiyantAst!;aljr9ta-.  sac^yas  '%ra/a  ^  ,r«  «a/gj,j,rfrf*  rfaäaiJ  'nahe  A. ^.  1 1. »WOTff  astvat.3r?tasca  nama  YtiJ.  129;  V.l  •)  ihm  ist  Yt  14  geweiht;  s.  noch  Yt.  lO. ig.$,  Vyt^o;    —    astvat.9rftahe  •%raynS  7i.    Vgl.  Dst.  ZA.  3.  559,    Hbm.  AGr.  /.  75;
26811:•  j.  spaka-  Adj.  'hundeartig,  Hunds*'; aHaam  •kanam  kahrpunanam  (sd.)  V. 14.  S-
```


## [2026-09-06T22:14:00.322Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN 205 leaf 226\"; awk 'BEGIN{RS=\"\\f\"} NR==227' HRN.txt | head -60"
}
```


### [2026-09-06T22:14:02.047Z] TOOL RESULT

```
=== HRN 205 leaf 226
- 205 -
919. gu^lr 'Hilfsmitter, guz^rden (Sahn. I, 61 Vers 519),
ffuzer, guzerden; vergl. näguztr.
Etwa "^viöarija-, vergl. skr. vi -r- i^car- 'ausführen,
vollführen'.
Hat mit reztr (No. 1084) nichts zu tun.
920. gustäx *kühn, frech', busta/ (nicht belegt), vergl.
usta/ (ebenfalls unbelegt).
aw. *vistaka', vergl. stax^'a-, phlv. sta^mak (Darme-
steter. Et. ir. 62)0; P^lv. v{i)stax (Mgn.), arm. LW.
vstah unverzagt'.
921. gtisterden ausbreiten', guster, vergl. blster (No. 218).
ai. vi -f- [/'sfar- ausbreiten'; phlv. v{i)siarta)i aus-
breiten*.
922. guMMen 'zerbrechen, trennen', Praes. gmihem^ gml
kerden Verabschieden, entlassen' (Öähn. I, 74 Vers 236),
pin '^''Di: Verstössen (Jer. 3, 8), vergl. gusll (Vullers),
gtisilänlden (Öähn. I, 88 Vers 494).
phlv. v{i)sastan (Bund.), v{i)sastakih (PPGl.).
Darmesteter, Et. ir. I, 84 hat das Wort auf eine
\/^*Qard' zurückgeführt, die neben ai. gar^, gpidti *zer-
brechen' auf iranischem Boden existirt haben müsse.
Bartholomae (briefl. Mitteilung) denkt an eine Ver-
mischung der beiden synonymen Wurzeln sk^heid- (aw.
sa^d-, hisidyäf; ai. dhed-, chindtti; bei. sindag, n. sinday,
Hübschmann, ZDM6. 44, 559) und k\er- (ai. ^c/r-,
Cfnäti). Ifp. gusisten wäre ap. *visistanaig (aus *«^z-
sid'tanaiy), dagegen gtisilem ap. *visardann (aus sar-
mit dem d von sid-). Er verweist dazu auf die
Wochenschr. f. klass. Phil., 1892 Sp. 397.
Der Inf. guslxten ist ganz unklar.
923. gusäden offnen , sich öffnen ; Praes. gusay-em,
gusüden, gusäyis (Öähn. I, 169 Vers 734).
phlv. v{i)sätan oflfnen'.
Darmesteter, Et. ir. I, 59 Note 3 nimmt als
Grundbedeutung von np. gvsäden sich freuen , indem
') An *v%8taxf'(i' hatten schon Fr. Müller, Kuhn und Schleiclier's
Beiträge V, 139 und Spiegel, Kommentar T, 64 gedacht.
```


## [2026-09-06T22:14:17.389Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== Abhilfe\"; grep -n \"Abhilfe\" BRT.txt | head -20; echo \"=== entscheidend\"; grep -n \"entscheidend\" BRT.txt | head -20"
}
```


### [2026-09-06T22:14:17.453Z] TOOL RESULT

```
=== Abhilfe
15035:•  g.  paiti.vyädä-  Adj.  'wieder  heimzahlend, Vergeltung  übend'":  apascä  v&..avaocama .  .  nä/a  -da  (APC)  paitT.s!ndi  "und  euch, Wasser, ..  die  ihr  im  Unglück  Vergeltung «bend  Abhilfe  schafft"  Y.^.5.
15051:•  g.  paiü.s5nda-  Adj.  (fem.  -da-)  'entgegen-  j  alwatum  Yt  12. 3.  b)  'nach  vom  hin, wirkend,  Abhilfe  schaffend"»:. o/Bj.-'a  »i..|Vom':  •/«  hl  fiB.n.J  (sd.)  antarät  namit avaocämä  .  .  näsü  faitl.vySda  (sd.)  'da  ■  bnatMyam  .  .  aBa  druxs  .  .  upaMvqsaiH Y..JÄS-  |V.<y.4i;  4a-44.5.  iSt  i6^  18';  —  pasca
=== entscheidend
7577:<)  Sonst  oMtiy*  gelesen.  So  wie  oben  klingt mir  der  Name  wahrscheinlicher.  Eü.  ist  nicht entscheidend.
19212:•  j.   ni-vätay-  f.  'entscheidender  Sieg":  Bh.  7. 13.
19214:Dinge  zwischen  den  beiden  Geistern  der  L^^d  des  Namens  gebe. entscheidende   Sieg   stattfinden   wird"   Y.      Eig.  'Niederlassung',  mm  v.  säy,   ai.  vgl.
21727:eschatologisch  von  dem  entscheidenden  formtist;  «.  >ra^rf-3  a.  Nach  Y. 3/ (du  eine  Art 'Schlusswerk',  das  den  Sieg  der  <rÄ«nschen  ,  Kommenlar  des  GebetB  bildet  -  lur  Pü.  duD Welt  vollenden  wird";  ftyal  damh  vaAüli^s.  West  SBE.  j/.  463  )  ist  es  »on  ZanAni/ra ya/^isd.)  miidi  aiS  y&Xtä  (sd.)  j,j;ir,  verkflndigt  worden  im  GegensaU  .um  .4fa«M- /iP\  \r   i  1     j,     ■     .         \'i  ."■"!  '<i"«-Gebet,  die  alt  Offcn^ianiiigen  AJaira'
27827:*>  Ich  halte  es  fär  sicher,  dut  Zart&uSira eine  geichichtlicbe  PersöoUcbkeiE  ist,  sowie  dass die  Gä%äs  im  wesentlichen  auf  ihn  lurückgehen. TiELB  GeschRelAIt.'  3.  275  CTklärt  mit  Recht den  Zar.  des  jüngeren  Awesla  (ül  "eine  vSIlig mflhische  Person",  aber  dnss  er  «chon  in  den Gä%äs  "eine  legendarischc  Penon"  sei,  mnss ich  ihm  bestreiten.  Ich  finde  vielmehr,  dass er  uns  hier  darcba,as  körperlich  nnd  meaichlich entgegenicitt.  Sein  Reformationswcrli  ist  noch in  den  ersten  Anlangen  begriffen.  Nur  ent wenige  einflussreiche  Männer  sind  dafür  ge- wonnen, nm  es  aU  Soosyanl  {lA.)  zu  nnterstütien : SD  ausser  dem  Sohn  Iial.väslra{i.  lara^tütray- a) nnd  dem  Vitersbruder /ftiiyöt.m^wAa  inibeson- dere der  Fürst  yäiäipa,  sodann  Jämäiftt,  dessen Minister,  und  Fralaoslra,  deren  beider  Interesse durch  Knüpfung  verwandtschaftlicher  Bande  ge- festigt, wird  -  Zar,  beiratet  Frai.z  Tochter  und gibt  Jim.  seine  jüngste  Tochter  ßimraaslä lar  Ehe  -,  femer  der  TKrer  Fryäna-  (s.  Ntr.}. Auf  der  andern  Seite  setzen  die  den  alten Göttern  iäana-)  wie  Mi^ra,  Haoma  usw.  und ihrem  Kult  treu  bleibenden  Fürsten  {kaii)^-, säslar-)  nnd  Priesler-Lehrer  [kivapan;  uäg-')  wie Bindva,  Grlhma  dem  Neuerer  heftigen  Wider- sland entgegen,  lo  dass  er  häufig  genug  in  bittere Klagen  Bosbrieht  und  der  Besorgnis  Ausdruck gibt,  ob  er  seine  Mission  werde  fortfuhren  können (vgl.  iB.  Y.  46.  i).  Beieichnend  ßr  die  ■Wirk- lichkeit der  Verhältnisse,  unter  denen  die  (7ü^s entstanden  sind,  ist  die  Strophe  Y.Jf.  iz.  Haite ich  sonach  an  Zar.  als  historischer  Figur  durch- aus fest,  so  sehe  ich  doch  anderseits  jeden  Ver- such, die  Zeit  seines  Auftretens  genauer  zu  be- stimmen, für  aussichtslos  an.  Nach  der  heimischen Chronologie  (s.  West  SBE.  47.  xxvm)  würde Zar.%  Geburt  in  das  Jahr  660  v.  Chr.  fallen, und  Jh.  Zor.  174  hält  das  für  wesentlich treffend :  "the  period  . .  just  before  the  Achae- menian  power  [is]  the  approximate  date  of Zoroaster's  life".  Ich  glaube,  wir  werden  wesent- lich weiter  zurückzugreifen  haben,  und  urteile über  Jn.s  Ausführungen  wie  Tiele  GeschRelAlt.> 2.275,430.  Einer  Chronologie,  die  damit  rechnet, dass  ein  Lehrer  des  Glaubens,  der  als  erster 100  Schüler  um  sich  versammelte  (s.  ^sarna-\ 100  Jahre  nach  der  ersten  Verkündigung  der neuen  Lehre  geboren  wird  und  100  Jahre  att stirbt,  kann  ich  kein  Vertrauen  schenken.  S.  auch No.  I  zu  vüläspa-.  —  Die  Angabe,  Zar.  sei  im Weslen  von  Irin  geboren  (s.  rayay-),  ist  mit  der Tatsache,  das«  alle  entscheidenden  Stellen  de* Awesta  (insbes.  Yt.  ig.  66  f.)  auf  Entstehung  im Osten,  in  der  Gegend  des  //äiniinsees  hinweisen, keineswegs  unvereinbar.  Es  lisst  sieb  sehr  wohl begreifen,  dass  der  Reformator  seine  Heimat verlies!,  weil  er  keinen  Anklang  fand,  oder  auch verlassen  musite.  So  mag  sich  auch  seine  starke Betonung  wirtschaftlicher  Giundsätie  (s.  väilrya-) erklären.  Der  Westen  Irans  stand  zweifellos auf  einer  wirtschaftlich  wesentlich  höheren  Stufe als  der  Osten,   wo  man  sich  noch  lange   nicht
30092:KompA.  1  Ableit.  —  S.  auch  Aitvä-  l.  —  Vgl. np.  labäH,  3.1.  jiMia-  f.«.  —  Pü. :  Ausvän.  — ')  Das  muk.  Geschlecht  ist  i.uf^lig,  wiid »ber  durch  alle  entscheidenden  Sielleo  ver- bürgt;  IF,  lO.  20z.  —  »)  Unsicher,  da  der Anfang  des  Wort»  lersiört  ist;  BB.  14.  245.  — i)  GS.  —  4)  LS.  statt  IS. ;  S  409  mit  No.  3.  — S>  S.  tasUiiyä;  Sp,  1685  m.  —  *)  Der  LS. dient  als  IS.  {s.  No.  5)  und  wird  im  Sandhih nach  dem  Muster  des  gleichlautenden  GS. (».  N'o.  4)  behandelt;  Bthl.  IF.  10.  102.  — 7)  So  K4;  NA.  :fenJ.  —  S)  NA,  aJä.M!vi; s.  aber  Pt  4  usw.  —  9)  Worüber  luletit  Colutz OrStudies  of  iheOr.Cluh  of  Philadelphia  167, BLoouFtSLD  AJPh.  f6.  426,  Wn.  AiGr.  r.  161, 163,  Fay  JAOS.  i6-  ccxxvm,  Pederson  KZ. jÄ  201  und  -  mit  treffender  Kritik  -  Uhlem- BECK  WAiSpr.  101.
```


## [2026-09-06T22:14:17.561Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN 242 (leaf 264)\"; awk 'BEGIN{RS=\"\\f\"} NR==264' HRN.txt | head -60"
}
```


### [2026-09-06T22:14:19.222Z] TOOL RESULT

```
=== HRN 242 (leaf 264)
— 242 —
1078. vevd/kj 'Wachtel', rerdej, verflj, vertek.
ai. varfikä' ^WachteF; phlv. oartak (Papyrus, Hörn,
ZDMG. 43, 50); gr. oorvh
kurd. verdl, //arnfrr?^ 'Wachtel' (H.-Sch.); af/. vvaraz\
ORS. LW. (?) rärdcä; bei. f/vardäf/ Gebirgsrebhiihn' ;
WSL/. VOlc.
1079. verseng 'würdig, achtbar (unbelegt).
ap. onn(7(iyyrjC' of &vf(jyiTa( tov ßnöi'krjo^^ noorrdyyai
y.ah'ovrai nfgtöri (Herod. VII, 85), de Lagarde, Ges.
Abb. 191.
Die Grundbedeutung wird 'gewichtig sein (vei'gl.
se7ig, No. 747); rer -- ap. vpar'nj also wer, wie in
versäz {wersäz) ?
1080. very 'Wasserwehr, hery.
skr. vdrga- 'Abwender\ also zu [/^vnrj- , vdrjafi
(Nöldeke, mündliche Mitteilung).
1081. vemste, beziste nur in nnon, nnDTZ (Is. 66, 8;
66, 17).
phlv. v(i)jastak; Pärsenwort, sonst r/ujasfak,
1082. vei^ey Frosch', arab. LW. vazayat 'Eidechsenart'.
aw. vazayä' 'Frosch'; phlv. vazay, vazag.
kurd. LW. vizdq 'Frosch' (H.-Sch.).
V
1083. i^ezlden 'wichen'; bezän (Sahn. I, 284 Anm. 2).
ai. \/vah-^ väliati 'wehen (dahinfahren vom Winde);
phlv. vajttan wehen'; kurd. LW. vezin, vazdmn
'wehen (H.-Sch.).
1084. ve^lr (arab. LW.) 'Vezir; Gelehrter ^), gezJr, gizlr*^),
talm. ns^T»!:.
*) So im indischen Persisch häufig, vergl. z, B. Maä»ir-i Mah-
wiidsähl Fol. 38 (Berliner Handschrift Ms. orient. Fol. 535).
Im modernen Spaniscli ist der Vezir als alguacil, alvazil etc. zum
'Häscher, Polizeidiener* (auch veraltet 'Scharfrichter' und im Schiffs-
wesen der Beamte, Mer auf einem Kriegsschiffe für alles sorgen muss,
was zum Wasserproviant gehört*, s. F. Boooh-Arkossy, Spanisch-
Deutsches Handwörterbuch^ s. v.J degradirt, vergl. Dozy -Engel-
mann, Glossaire des mots espagnols et portugais d6riv^s de Parabe*,
S. 129.
*) Nur in einem AbuM Ma*änl- Verse.
```


## [2026-09-06T22:14:26.134Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN leaf 265 (p243)\"; awk 'BEGIN{RS=\"\\f\"} NR==265' HRN.txt | head -40"
}
```


## [2026-09-06T22:14:26.943Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT Mittel\"; grep -n \"'Mittel\\|Mittel,\\|Hilfsmittel\" BRT.txt | head -25"
}
```


### [2026-09-06T22:14:27.930Z] TOOL RESULT

```
=== HRN leaf 265 (p243)
- 243 -
aw. Vieira- 'Entscheider ; phlv. v(i)öfr 'Entscheidung ;
Entscheider, Richter ; arm. LW. vcir ^Entscheidung.
1085. veng, ving 'leer; arm'.
aw. vergl. wwa- *leer, mangelnd'^); ai. und- Voran
etwas fehlt, unzureichend'; arm. unain *leer' (H.
No. 236); got. van 'Mangel*; gr. bvvi^ ermangelnd'
(zu einer {/^ven-*, Osthoff, Morph. Unt. IV, 368 ff.,
dagegen zu einer |/^m-, Bartholomae (briefl. Mit-
teilung) unter Verweis auf BB. XVII, 121 und Per
Persson, Wurzelerweiterung 83 zu einer l'eua-).
Die Anregung zu dieser Zusammenstellung verdanke
ich Herrn Prof. Nöldeke, der lat. vanus vergleichen
wollte, das mir aber (vergl. väcuus) nicht dazu zu
gehören scheint. Nachträglich sehe ich auch Toma-
schek zu sar. vanao 'Leerheit, Eitelkeit, Müssiggang,
Faulheit'.
1086. vir Sinn, Verstand; Gedächtniss'-), hir, her (8,
Vullers), Viru 'im Gedächtniss habend'.
g. vir därtmün 'erinnern', vtr svdmün Vergessen'.
aw. *nra' 'Einsicht' in livtra- etc. (Darmesteter,
Et. ir. II, 183); phlv. vir, vlräk im Gedächtniss
habend* (Bund.).
kurd. Mr 'Gedächtniss*; bei. glr 'Gedächtniss, Er-
innerung' (110).
1087. werän, werane wüst', heran.
phlv. aperän 'wüst' (M6n.), aperämh (Ganj-T äayakän,
1); päz. awlrän.
Fr. Müller stellt (WZKM. 5, 260) arm. LW. aver
'zerstört, wüst ; Zerstörung, Wüste*, averem 'zerstören,
wüst machen' dazu, aber arm. e steht nur in per-
sischen Lehn Worten für e.
>) Jackson, Amer. Journal of Philology, Vol. XI, 87 folg.
«) Reimt auf sir 'Milch* (Öflhn. I, 240 Vers 1982).
16*
```


### [2026-09-06T22:14:27.975Z] TOOL RESULT

```
=== BRT Mittel
11272:•  j.  £ärä-  f.  'Mittel,  Hilfsmittel"»:  "ram F.  IQ.
11671:Ableit.  aus  jtva-,  —  ai.  fevya-  n-  'Mittel  tum Leben'.  —  Pü.  (lu  Aog.);  üvanJai,  (lu  H.): pa  ihiandakih;  (lua):  gSsl  iiivand,  inSü.erl.: dugdham.  —  ")  Statt ynya-j  S  ^S.  II,  I7.  — »)  D.  \.jriya;  -c  statt  -ya  ($  268.  32),  -uy Statt  -ru-  (S  268.  19).  —  ))  Im  Gegen»,  in baekya-.
16505:YtÄfio.       o)iiberhaupt'Hilfsmittel,Hitter:j  7;    —  fravalay5  'zyä  YLij.30,  3a;
24013:•  j,  vi-tira-  m.  'Durchgang,  Gang'  (im Stall,  sva.  Abteilung) :  caat  yavat  nmämm (näml,  gavayanfm)i  .  .  ävadasa  Ta  (NF.) upima  nava  'ra  mahma  xhias  °ra  nittma "Wie  gross  soll  der  Stall  sein?  Zwölf Gänge  sollen  (drin)  sein  höchstens,  neun im  Mittel,  sechs  mindestens"  V.  j4.  14".
```


## [2026-09-06T22:14:37.529Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD\"; grep -n -i \"wizir\\|wiz̆ir\\|čārag\\|carag\\|xrafstar\\|kirb\\|karb\" PHD.txt | head -30; echo \"=== PHD_mackenzie\"; grep -n -i \"wizīr\\|wizir\\|xrafstar\\|čārag\" PHD_mackenzie.txt | head -20"
}
```


### [2026-09-06T22:14:37.610Z] TOOL RESULT

```
=== PHD
125:did ... add other. add dig |YTMAL < А *?{т?1 | N di] yesterday. delete *drém ... (read balgam) drubušt ... add protective. drust [drw(d)st' ... duš-čihr ... add ill-natured. duš-nām [-n^m | (M dwjn'm), N ~] add ill-famed. dušwār [dwáw?l | (M dwjw'r), ... ékanag ... for obedient read loyal, faithful. ~th : for obedience read loyalty, faithfulness. for Farrēbāg... read KFarrēbāy [pinb(^)g] ... frayad |pl(y)d^t' | N faryad] ... delete M pry'd. frazand |prz/znd | ... frusag ... add M prwšg. garódman ... read | P grdm'n. gazdum |gcd(w)m, gzd(w)m |... guftàr ..., ~th : add eloquence. hambar |hm-, hnb] |... add  hamest |hmyst'] whose good and bad deeds weigh equal. ~(ag)an |-(k)^n'] limbo, the neutral station between heaven and hell. delete hammist ..., ~(ag)an ... handarz ... add M °’ndrz. hammoxtan, hammoz-, ~i8n : add learning. hast |TWMNYA < A tmny ; ... add hūg [HZWLYA < A hzyr’; hwk' | M hwg, N xiig] pig. add hūkar(ag) |hwkl(k') | N xükara] porcupine. (not hedgehog) add *huzārag [hwc’lk | N хијага) little, small, few. !jadag ... add fortune. jüdan ... | M jwwdn, jwy- ... add karawuš [kl wš| N ^] wine-press. delete karbunag ... read karbūg |klpwk', klbwk'| lizard. kardagān ... add service (ofthe gods). delete karxēš vds
223:āwēnišnīg : blameworthy. a-wēnišnīģ Pzwynšnyk'] invisible. awérag [”wylk!] = awērān. awērān Pwyln', ?5yPn! | N wērān] desolate, ruined. awestad ['zos??t! | M *zxoyst?d, N ēstād] master (craftsman). awestām [*wst?m | M ?wyst?m] province, district. awestarag [”wstlk! | N ustura] razor. awestardan, awestar- [*xvst/-tn! | P °wystr-, N suturdan] wipe; shave. mišn : wiping. awestwār Pwstwb’l | M ?wystw?r, N ustuwār] firm, reliable. “Аһ: reliability, firmness. awēšān [OLE?n, у. бу | М юу п, N ēšān] they, those. a-wināh Pwrs] innocent. a-winast [”wnst'] unharmed, immaculate. awiš [wbš | M ?wys] to him, it; postposition (= ©) to. awištāb Puwst*5 | M ’wyst?b, N šitāb] oppression. P awištādan, awišt- ['zoft2tn! | P ?wyst!dn] stand. awištāftan, awištāb- ['wi?j-tm | M ?wyšt?b-, N sitāftan, šitāb-] oppress; hasten (tr.). tāwištan, tāwāš- [HTYMWN-tn! < A Мут, V htm; ?wbstn' | M *wyšt] seal. a-wiyabanig Pwyd?f?nyk! | N biyābānī] astr. fixed (star). a-wizirignig Pweylinyk'] unavoidable, inevitable. āwurdan, awar- [YHYTYWN-in' < A hyty, У № | M wrd, "wr-, N ~] bring. āxēzīdan [>лусуѓп!] = āxistan. āxistan, āxēz- Phstn', ?hyc- | М *xyst, ?xyz-] rise, stand up. Axrámidan, āxrām- >А?т-уѓп! | M ?xr’m-, N xiram-idan] stride, strut. axtar [Atl | M *xtr, N ~] star, constellation, sign of the zodiac. axtar(ā)mār [Phil(?)m’/] astrologer. ~th: astrology. laxw Dell being, existence, world. ?axw Phw! | M *xvx] mind, will; vital force. *axw Phu'] lord. a-xwamn [’hwmn'] sleepless. axwān Phw’n'] = захм. a-xwārīh ['Aw'iyh] unhappiness. āxwarr [hwi | N àxur] manger, stable. --Sālār [-srd?I] head groom. a-xwaš [D BS YM] unpleasant; unhappy. ~ih: unhappiness. a-xwēškār [kwyšk'I] undutiful. ay Dy | N —J that is to say. āy-, у. amadan. ayāb [уор | М ik, N уд] or. ayāb- v. ayāftan.
296:čābuk [c’Swk! | N ~] agile, nimble; excellent. ~th: agility. čādur [c?twl | N ~] sheet, veil. éagad [ck*t! | (N ¿ahad), J ¿eyad] peak, summit. сабаг [cki] wife (of the second degree). саһ [ол | N ~] pit, well. čahār [ALBA < A?rb‘; ch?l | M с, N ~] four. ~dah [cl’ldh | N ~] fourteen. ~-рау [cb Ip d | N ~ > čārwā] quadruped. čakēk [ckwk | N ~, cakáwak] lark. čakuč [cktwc | N čakuš] hammer. čambar [cmbl | N ~] circle, hoop. čamišn [cmšn! | M cmbyšn (?)] urination; lavatory. ` бапа [спа | = M, N ~] how many, much?; so many, much; some, a few. ~ih: amount, quantity. čandal [cndl | N ~] sandalwood. čandīdan, čand- [cnd-ytn! | (M cn-ystn)] tremble, quake. ~išn: trembling, movement. čang [eng | M bung, N ~] harp. ~-sray [-sPd] harpist. са�� [c7] = Carag. багар [clk' | M erg] pasture, grazing; flock. čārag [c?]k! | N ~a] means, remedy. ~garih [-glyh] ability, savoir faire. Carb [с/р | P crb, N ~] mild, gentle; fatty, oily. ~ih: gentleness; fattiness. ~išn [-sn'] fat, oil. ~і&потапа [-šrwmnd) oleaginous. Carm [с/т | M crm, N ~] skin, hide, leather. čārūģ [c wk! | N čārū] lime, mortar. „ēn [-yn!] limy. Carz [сіх | N ~] bustard. čāšīdan [c'$-ytn!] = čāštan. čašm [A YNE < A ‘ynh; ст | = M, N ~] eye. léaSmag [cfmk! | М cšmg, N ~a] spring, source. tčašmaģ [cfmk!] renowned. čašmaģāh [cšmk?s | M csmg’h] obvious, public, notorious. ~ih: notoriety, condemnation. čašm-arešk [cém ?ly$k!] envious. ^h: envy. čašm-dīd [cšm dyt'] visible, obvious. čāšnīg [c nyk! | M спус, N čāšnī] taste.
424:kaman [kin’n' | = M, N ~] bow. 5; 7 ~dar [-d'] | N ~] archer, bowman. ha er mae 4 ba kamar [kml | N —] waist; belt, girdle. ~-band [-bnd | N ~] belt. kāmģār [Emil | P k?*mg?*r, N ~] powerful, absolute. kamist [Amyst'] least. —jh: pad ~ih, at least. kāmistan, kām- [YCBEN-stn' < A ysbh, V shh; k*m-(y)stnt M k*m-yst] want, desire. kám|-rawág [km izvb*k! | N ~rawa] successful. ~-Z1(w)isn [-zywsn'] free, independent. kam-zór [kmzwl | N ~] weak. ~ih: weakness. kan-, v. kandan, kanar [kwl | N ~] side, edge; embrace. ~ag [-k' | M kr?rg, N ~a] edge, limit, boundary. --agómand [-k’wmnd | M -gwmnd] limited, finite. kandan, kan- [HPLWN-tn! < А V hpr; kn-dn', -tn! | M knd, N ~] dig; raze, destroy. kanig [knyk! | M knyg] girl, maid. kanizag [knyck! | M knycg, N kaniz(ak)] — kanig. kantigr [kntgl] quiver. kāpūr [ро | Ar. kāfūr] camphor. kar-, v. kardan. 1Kar [21 | M Pr, N ~] work, deed, affair. ~ framüdan: put to use. 2kàr [%'7], pl. —àn: (other) people. зкаг [%'/] butter. kār-, v. kištan. karafs [klips | N ~] celery. kār-āgāh [РА | N ~] skilled, experienced. ~ih: skill, experience. karak [krk! | N ~] quail. karan [kľn' | P bein, N ~] side, edge, end, limit. kārawān [%?/zv?x! | P k*rw'n, N kārwān] caravan, military column. ~ig [-yk! | N ~7] caravaneer, traveller. karb [klp] priest hostile to Zoroaster. karbāš [5/0 | N karbas, etc.] lizard. karbunag [k/pnk!, klbnk'] lizard. kard [krt! | M kyrd, N ~] action; matter, affair. кага [SK YN A < A skyn’; Kit! | N ~] knife. ikardag [kltk!] division, section, portion. *kardag [krtk!, kltk! | N karda] action. kārdāg [k'/d?k'] traveller, wanderer, migrant. kardaģān [Art-, Rlt&?n! | M kyrdg”n) action. kardagàár [Artk?l | M kyrdg’r, № ~] mighty. C 6084 E
428:kem [kym] less, fewer; v. kam. кёп [kyn' | = M, N kīn(a)] hate, malice, revenge. ~ig [-yR'] malicious, vengeful. kennār [Rl] lyre, harp. ~-sray [-sPd] harpist. kénwar [kynwl | (M kynw’r), N kinawar] vengeful, vindictive. ««īh: vindictiveness. kër [kyl | N ~] penis. kēsar [kysl] Caesar. këš [kyš | = M, N ~] dogma, faith (especially non-Mazdean). ~-dar [-d’/] sectary, non-Mazdean. keSidan, keš- [k(y)$-ytn! | (M kr$-), N kafidan] pull, draw. Kēwān [kyw’n! | Ar. kaywān] astr. Saturn. kēwūd [kypwt! | M R'ywd] box, ark. kilēl [R]yl | N ktlīd)] key. kirb [klp | M kyrb] body, form. kirbag [krpk' | M kyrbg, N Аја] virtue, good deed. ~ig [-y%!] virtuous, pious. kirbakkar [krpkkl | M kyrbkr] beneficent. ~ih: beneficence. kirih- [OBYDWNyh-, v. kardan, kiyh- | M kyryh-] be done, made. kirm [kim | M krm, N —] worm, serpent. kirrénidan, kirrén- [klyn-ytn'] rend; create (daevic). kirróg [k(y)lwk! | M grwg] artisan, craftsman; skilled. ~th: arts, crafts, craftsmanship, skill. kiš [k(y)š | M АЎ, N ~] furrow, line. kišnīz [kšnyc] = gi$niz. kištan, kar- [ZL Y TWN-tn! < А У ar; kyštn!, Pl- | M kyšt, kis- N ~] till, furrow; sow. kištār [ZLY TW NTt'l] tillage. kišw, ~4n [kysw', x! | P Аун] tillage. ~(an)zar [-c?/ | (N kištzār)] field. ki$war [Rystol | M kyswr, N ~] region, clime, continent. kišwzār, v. kišwānzār. kūb-, v. koftan. kódak [kxwtk! | M gwdk, N ~] young, small; baby. kof [kwp | = M, N koh] hill, mountain; hump. ~ag [-4! | N Абла] saddle. ~ig [-yk! | N kēkī] wild, mountain-. koftan, kūb- [kwp-tn' | N ~] beat, pound, crush. kör [kwl | M kar, N ~] blind. ~-dil [-dyl | M -dyl, N ~] blind-hearted, incorrigible. kūstan [kwstn' | = M, N ~] beat, pound. kūš-, v. kóx&-. kēšk [how fA! | N ~] pavilion, palace, kiosk.
657:wizürd-wars [wc'/t' wls] with parted hair. wizāstan, wizāy- [wyz'stn!, wyz'd- | M wy2’y-, N guzáy-] injure, impair, prejudice. ~išn: injury. ~išnīg: injurious. wizén [wcyn! | N guzin] choice. wizend [wz(y)nd | M wzynd, N guzand] hurt, harm, injury. wizéngar [wcynkl] chooser; selective. | wizidan, wizin- [weytn', wcyn- | M weyd, N guzīdan, guzīn-| choose, select, prefer, discriminate. wizihidan, wizīh- [w(y)cyh-ytn'] be separated. „išn(īh): separation; dawn(ing). wizin- , v. wizidan. wizir [weyl] decision, judgement. wiziristan, wizir- [wcyl-stn! | J bzyr-, N guzir-) be able to dispense with, avoid. ~iSnig : avoidable. wizistan [westn' | M weyst] teach. wizóstan, wizóh/y- [wewstn', wewd- | (J bzwb-, N pizohidan)] examine, investigate. -~i§n : investigation. wizüdan [wyzwin'] = wizastan. wizurd [wewlt'] valid, genuine, true. ~th: validity, truth. Wērūbaršt [w’wklwblst' = Av. wouru.barasti-] the north-western con- tinent of the earth. Wērūjaršt [w>wklwelft' = Av. wouru.jarasti-] the north-eastern con- tinent of the earth. wurróyistan, wurróy- [H YMNN-stn! < A hymn, У °тп | M wrwyst, (wrw-), J *brwy-, grww-, N brw-, girawidan] believe; choose. —išn [wlwdén'] belief. wuzurg [LBA < Arb’; wc(w)lg | M wzrg, N buzurg] big, great. ~ith: size, greatness. wuzurg-framadar [LBA plm't I) prime minister.
661:2xān [/?п! | P л?п] spring, source. хапар [BYTA < A рур; h'nR! | N хапа] = іхап. xandidan, xand- (*GHBHWN-yitn' < A V ghk, or У *ghqh; hnd-ytn' | (M xnyst), N —] laugh. xānīg [/?nyk! | M x?nyg, N xàni] = *xān. xar (HMRA < А hmr’; hl | N ~] donkey, ass. хаг [P1 | M ær, N ~] thorn. xar-buz [hibwe | M xrbwz] oryx. xar-g68 [higws | N ~] rabbit, hare. хаготапа [/PPwmnd] thorny. xār-pušt [/?Ipwst! | N ~] porcupine, hedgehog. xastan [hstn' | M xst, N ~] wound, injure. xašën [hsyn! | N хайл] (dark) blue. хауар [Pd(y)k! | N xdya] egg. ~-dés [-dys] oval, egg-shaped. xayüg [Ah )dwk! | N xayū] saliva, spittle. xaz [hz | N —] marten. xém [лут] nature, character. xëšm [?yfm, hfm | M xysm, N xifm] anger; the demon Wrath. --én [-ya! | M -yn) angry. xindag [hyndk' | M xyndg] ill, sick. ~th: illness, sickness. xir [C BW! < А sbw; hyl | M хут] thing, matter. xirs [hls | N ~] bear. xišt [Ast! | (P hystyg), N ~] brick. хбё [hwk' | N xwk, xóy] nature, character, disposition. x6n [DM YA < А dm’; һит! | M хоп, N хип] blood. xormā [TE A tmryn; hwlm’k' | N ~] date. xrad [hit! | M xrd, N xirad] wisdom, reason. ~ig, ~Omand [-yā!, тиа | N -mand] wise. xrafstar [hlpst] = Av. xrafstra-] reptile, noxious creature. xridan, xrin- [ZBNN-tn! < A V zbn| M xryd, xryn-, N xaridan, (xar-)] buy. xróhak [hlwhk' | N ~] coral. xrēs [DYLK A < A dkr’; hlws | P xrws, N xurós] cock. xróstan [Alwstn! | M xrwst] call, cry. xüb [hwp | M xwb, N ~] good. ~th: goodness. xuftan, xufs- [HLMWN-tn! < А У Ыт; hwptn', hwps- | М xwpt, N xuftan, xusp-] sleep. xūg [HZWL УА < А hzyr; hwk' | N ~] pig. xükar(ag) [hwkl(k') | N xūkara] hedgehog. xumb [kwmb! | M xwmb, N ~] jug, pitcher. xunak [hwnk' | M xwnk, N xunuk] happy; cool. xurdruš [kwldlwš, -dlpš = Av. xrwidruf] ‘with a bloody club’ (epithet of Xēšm, later misinterpreted as *ul-draff ‘*with raised banner’).
692:ability čāraggarīb, hunar, šāyendag- ih, tuwānīgih; extent of ones — tuwān-sāmān.
906:avoid pahrēxtan, wiziristan. avoidable wizirisnig. avoidance ānābišn.
979:beneficence hudā(ha)gīh, kirbakkarih, xwābarīh.
980:beneficent hudā(ha)g, hugar, kirbak- kar, xwābar.
1036:body kālbod, kirb, tan.
1300:compelled ačārag.
1440:creature dim; noxious ~ xrafstar.
1515:decision wizarišn, wizir.
2010:form (n.) brahm(ag), čihr, dēs(ag), éwén(ag), gēn(ag), jadag, kālbod, kirb; of the same — hamdēsag.
2126:good (a.) huda(ha)g, nēk(ēg), new, weh, xūb, hu-, P naxšag; ~ char- acter huxémih; — deed huwatršt, kirbag; — repute husrawih; — rule hupādixšāyīh; ~ ruler hupádix- šā(y); ~ speech hüxt; ~ spirit spenag mēnēg; ~ thought humat; of ~ behaviour hukunišn; of ~ character huxém; of — religion hudén; of — repute husraw; of — speech hu-éwaz, hu-gówisn; of ~ stock pad-góhr(ag); of ~ thought humenišn.
2513:judgement ^ dadestàn, dadwarih; handāzišn, wizir. Jug xumb.
2636:lime Carag; (a.) čārūgēn.
2651:lizard karbaS, karbunag.
2945:noxious creature xrafstar.
3129:pious dahm, kirbagig; v. righteous.
3220:priest āsrē, asrén, dastwar, hérbed, mowbed, māns?rbar; ~ hostile to Zoroaster karb; first officiating ~ zēt; second officiating ~ rāspīg.
3393:reptile xrafstar.
4229:virtue hunar, hunarāwandīh, hu- waršt, kirbag, nék-góhrih.
4607:саг čārūgēn Čārūg čāraggarīh Čārag čābukīh čābuk: čāš- čaxšāgīh
4992:karbāš karbunag karg kirīh- askamb! kirrén- kirrēnīdan kilēl
4996:kulang kirrdg sett kargās karkēhan kark karm, kirm karmīr karb, kirb karafs karbunag karzang kardār
5000:kirbakkarih kirbag, kofag
5026:Кой kirbagig kirbakkar
=== PHD_mackenzie
1335:a-wizirisnig [)wcyllnyk ] unavoidable, inevitable.
5499:wiziristan, wizir- [wcyl-stn l I J bzyr-, N guzir-] be able to dispense
5569:xrafstar [hlpstl = Av. xrafstra-] reptile, noxious creature.
5976:as (av.) 6won, 6yon; (cj.) ~e; - if      avoid pahrextan, wiziristan.
5977:   ~iyon ka.                             avoidable wizirisnig.
6308:creature dam; noxious....., xrafstar.      damn eraxtan.
6342: custom dastwarih. ewen(ag).                decision wiziirisn. wizir.
6431:dispense with wiziristan.               draught ahang.
6856:ill-will duskam.                          inevitable acar, awizirisnig.
6903: intermediary mayanJig.                       handazisn, wizir.
7189:noxious creature xrafstar.             oppression awistab, handraxtagih,
7448:reptile xrafstar.                        richness tuwiingarih; V. wealth.
7850:unavoidable awizirisnig.                 unspecified aniimcistig.
9918:                                  U'(,)UU\          wizir
9920:nisem                               ~\              wizir-
9922:niscmag                          \~,                wiziristan
9924:niseb                                  ~\           wizirisnig                   \~~<;,
11710:xrafstar             \~~               iiranj
11888:mardomihl          ~"'t-o            ...   awizirisnig               '1)~,\'"
```


## [2026-09-06T22:14:38.412Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB\"; grep -n -i \"wicir\\|wičīr\\|vičīr\\|xrafstar\\|čārak\\|carak\" NYB_vol2_glossary.txt | head -30"
}
```


### [2026-09-06T22:14:38.478Z] TOOL RESULT

```
=== NYB
```


## [2026-09-06T22:14:50.234Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD krty\"; grep -n \"krty\\|nʼkrtk\\|n'krtk\\|nʾkrtk\" SOD.txt | head -20; echo \"=== SOD nqrh\"; grep -n \"نقره\" SOD.txt | head -20"
}
```


### [2026-09-06T22:14:50.293Z] TOOL RESULT

```
=== SOD krty
11283:582  »pyz'krtyh    B  .Lfu,jr 
11284:(o)pizak(r)tya/i   OPyzktyh)   ^'Pzykrtyh 
11317:589  'pyzktyh    B  =*  >pyz>krtyh 
11403:604  'pz'y'krtyh   B  &&+? '*sj£*j. 
11404:(o)poze  ?,  -(o)krtya   Opzykrtyh,  »Pz'yk(h) 
11406:>krtyh)   ^'Pyz'krtyh 
11441:607  >pz>yk(h)  >krtyh  -*  >pz>y>krtyh 
11478:614  'pzykrtyh  =*  'Pz'y'krtyh 
12799:(o)krte  Okrtyy,  >krt'k,  *krtkt  'ktyy,  }qtyy)  ©ace. 
12801:ykrt\v\  f.  >kr0   -^kty*,  qty\  >krty,  qty2 
12825:825  >krty    B,  S  (j^  ^~>  Jj)l»J'ij-*<jf 
12826:(a)krte   Okrt'k,  'krtyy)   ©ace.  >krtw,  f.  }krt\  inf. 
12828:>krty   =*}kty\  'krt'y 
12834:826  >krty)   M,  B  l^lo^X 
12835:(o)krtya   Okrtyh)   ©Skt.  karman   ©f.  n.   =>>kty\ 
12850:827  'krty'kh   S  fluf  .xj-* 
12851:(a)krtyak 
12856:828  >krty>kryyh   M 
12857:(o)krtya-kare 
12861:829  'krtyh   B,  S  =»  }krty> 
=== SOD nqrh
```


## [2026-09-06T22:14:52.554Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB xrafstar\"; grep -n -i \"xrafstar\\|xrafstr\" NYB_vol2_glossary.txt | head; echo \"=== NYB wicir\"; grep -n -i \"wicir\\|wizir\\|vicir\" NYB_vol2_glossary.txt | head; echo \"=== NYB carak\"; grep -n -i \"cārak\\|c'rak\\|čārak\" NYB_vol2_glossary.txt | head; echo \"=== NYB kirb\"; grep -n -i \"kirb\\|karp\" NYB_vol2_glossary.txt | head"
}
```


### [2026-09-06T22:14:52.673Z] TOOL RESULT

```
=== NYB xrafstar
1766:could come 41-12; (Hutös) ke ... 30 ~ zāt estet H. of whom 30 children were born 2423; xrafstr + pat došaxu ~ xtartan dahénd noxious animals of which they give them to eat in Hell 769-19; 4 dmécisn kē martóm ~ the four '(complexions" of which man consists 1200-11. 4 A of which (are the following facts), “inter alia" 11012-13, — 2. replaces hac + the 3d p. pron.: Artaxsér ~ zat A. was born of her 272; 148. 164. 192. 489.14, 49%, 685. 742. 10819. 109%. 1125; ~ ... ~ part of it... part of it 11022-28; with a generic reference: 100?" (of women). 95! (from the plants). 1028-? (referring to the pl. göspandän); v. also haciš-kas, haciš-mas; — rarely, through full association with the encl. pron., hac-išan 5418 (heš?n'). 1018 (MN-š'n', text uncertain). - In BP haciš coincides graphically with api-š; all haciš found in this book are listed above. A certain confusion occurs: apt-š written MN-S (instances v. s. v. āvēntšn); in Paz. often azaš for api-š and awaš for haciš.
2213:*karbök [klbwk'] an Ahrimanic animal, one of the xrafstrs (q.v.), uncertain which, 581. — Probably a poisonous lizard: Av. (455) baévara ažinam spakanqm kahr- punanqm Vd. 145 = Phl bévar az 4 sak karpok ‘10.000 dog-snakes, viz. karpok', with the gl. mār/l/-bānak (Vd. 1873 m’lwb’nk' or m'lb'nwk') and the ex- planation ē *sakēh-aš & kū apäc 6 kin mišinet ‘that is: its dog-nature consists of its sitting down on its tail’. Av. azinqm spakanam kahrpunanqm signifies ‘dogish, kahrpu-ish snakes’, karpu-na- being an adj. parallel with spaka-; Phl karpok < *karpava-ka-, parallel form klb’h BAA p. 43° (J klb’k), cf perhaps NP karavah ‘an animal of black colour; it is said that its bite is worse than the bite of a snake’ (BQ). When wandering in the other world Kartér sees (SM 1. 40) in Hell klbwk" u an xrafstr. O. Paul, Exeg. Beitr. zum Avesta (1939), 28, guoting Junker, ZII II, 243, translates 'lizard?, com- paring NP words which seem to be rather distant; wrongly BSOAS XVII, 1955, 237 n. 1.
4293:xrafstr [hlpstl] Ahrimanic, noxious ani- mals 76%, — Borrowed from Av. (538) arafstra-.
5222:katäma-: katam katära- (katarascit): katarcihé Kavärasman-: Karazm kaväta-: kavät kavi-: kai kavi-: kayak kavi-(usan-): Käyös kay-: citan kohrp-: karp keresaspa-: Krišāsp kū (kuda): kū kutaka-: kötak xrafstra-: xrafstr xratu-: xrat xrvidru-: xurdruš ni-xšata-: šastan xša0ra-: šahr xSa0ra-vairya-: šahrēvar pati-xSay: pätixsäi xšinaka-: šmah xŠnā-: šnāxtan xšnav: Šnāyišn (ava/avi-) xšnav-: ošntitak xšusta-: šustan x$viwra-: "šif(a)rg xUaöna-ayah-: xYan-asén xUačpal0ya-: xVēš xVafna-: xYamn x"üirizam-: xVārizm xUanat.caxra: x"andan
=== NYB wicir
4114:vicar decision, decree 818. — Paz. vazar, Skr. v. vicéra; Mx 271° Phl. brih u zamänak u vicir $ brin but Paz. breh u jamqna u vazar i barin (Skr. v. nyāya for vazar).
4116:Cod. K has wel 818, is wanting for Mx 2719; the other MSS have weyl = vicir in both places, accepted by S and A. BQ quotes NP vajar, vacar ‘judicial decree’ from the legal language, probably from Zoroastrian usage. Olr *vi-cara- from vi--car- (v. the preceding w.) which also signifies in Skr ‘to perform, to accomplish’ (caus. vi-cärayati ‘to deliberate’, v. vicär- tan). From this vi-car- also inf. vicurtan ‘to perform, to bring about’ DkM 834}, pt. vicurt, vicart ‘valid, authentic, true’, v. Dhabhar, PYV, Gl. 177. Cf also NP guzar, guzir ‘remedy, help’, also guzard; guzardan ‘to apply a remedy’. Arm. lw. véar ‘payment, achievement’, véar-em ‘to accomplish’ (< vicar- or vicär-).
4125:vicir
4128:‘decree, judgment, sentence’ shows through its -7- < -rn- that the OIr form was *vicirna- < *vicrna-, cf Skr cirna-, (« *efna-) pt. of car-. — NP guzir(ah) ‘help, remedy’. [Av. (1438) vicira- ‘he who decides’ does not belong to this group.] Hence the den. vb. viciritan ‘to give a decision’, from which impers. vicirét (‘it can possibly be decided thus’ =) ‘it is possible’ DkM 557*°. 558%, and NP guzirad ‘it. is necessary’ (Sn); further
6934:cirna-: vicir
=== NYB carak
1103:cārak remedy, expedient, means 8H. 79%; ~ kartan to remedy, to repair, to re- move 1122-35, ~ 4 ., OT -Š ~, OT subst. + ~, z"üstan to try to find an expedient for a p. 98, to try to get hold of, to seize, to overcome 813, 341-2, 9620, 1029-10, — Paz. cāraa (SGV), NP cärah. earütik [c tyk] girl 3812-14, 441-9. — Bor- rowed from Av. (581) carāttī-.
1141:..ma... 708; pat —-ic cārak...nē... 792; —-ic āštēh 78% (interrogation). 796 (... n& ...); —-ic bazak ... nē... 809; ~-tc ... nē... in no way 34?!.
=== NYB kirb
1842:ham-karpéh [hmklpyh] the quality, or state, of being of the same form, or shape, as another: pat ~ % amahraspan- dàn as being of the same shape as the Amahraspands 38?6, with the gl. kū etón būt cigon amahraspand-ē. — V. karp.
2208:kar [k'1] work, act, deed (also evil), busi- ness, errand, matter, case, task, cas. obl. kārē [k'ly], käreh [k'lyh] (ef s. v. karp); with indef. art. kār-ē [k'14-1] anything 1122, something 104°; pat kār-ē for some business 1417; 3511-14, 5027 etc., passim; — 6 butan i ham-ic kārē frahaxtak in order that all might be instructed in this matter (viz. in the new religion) 10811; pat martom käreh through human work (= as far is humanly possible) 1172; — ~ framiitan to bring about 19%; ~-om tō framāyē do thou thy duty to me! 2722; amāh dp i tč pat ~ né apäyet we do not need thy water 1423; 375-5; andar 6 ~ kartan to begin using regularly 9614; pat én ~ ku with the commission to ask: “.. — often coordinated with another notion so as to form a hendiadys expressing that the notion is put into practice: ~ u kirpak (work and religious virtue =) meritorious religious deeds 13% and passim; ~ u dätistän, v. this w.; ~ u räyenisn prac- tical function 87? (in this construction u is very often wanting in MSS and edi- tions); — šahrē -än (pl. cas. obl.) “‘state- work" — penal servitude, forced labour 92; zanč ~-dn 834 v.s.v. zan. — = NP. Av. only in the adj. kära-vant- (465); on OP kära- v. kürécür. — V. also a-kär, dast-kārēh, "ham-kär, kām-kār, kār-dāk, kàür-nàmak. ' > god
2213:*karbök [klbwk'] an Ahrimanic animal, one of the xrafstrs (q.v.), uncertain which, 581. — Probably a poisonous lizard: Av. (455) baévara ažinam spakanqm kahr- punanqm Vd. 145 = Phl bévar az 4 sak karpok ‘10.000 dog-snakes, viz. karpok', with the gl. mār/l/-bānak (Vd. 1873 m’lwb’nk' or m'lb'nwk') and the ex- planation ē *sakēh-aš & kū apäc 6 kin mišinet ‘that is: its dog-nature consists of its sitting down on its tail’. Av. azinqm spakanam kahrpunanqm signifies ‘dogish, kahrpu-ish snakes’, karpu-na- being an adj. parallel with spaka-; Phl karpok < *karpava-ka-, parallel form klb’h BAA p. 43° (J klb’k), cf perhaps NP karavah ‘an animal of black colour; it is said that its bite is worse than the bite of a snake’ (BQ). When wandering in the other world Kartér sees (SM 1. 40) in Hell klbwk" u an xrafstr. O. Paul, Exeg. Beitr. zum Avesta (1939), 28, guoting Junker, ZII II, 243, translates 'lizard?, com- paring NP words which seem to be rather distant; wrongly BSOAS XVII, 1955, 237 n. 1.
2225:karp [klp'], cas. obl. karpēk [klpyh] 95**, the external, visible form of living be- ings: der-pattäi ... ~ dārēnd they will have their external form everlasting (= an everlasting bodily form) 10515; — as the second element of a compound: mdtak ~ having female shape 5717; pat kanik ~ in the shape of a maiden 731; 6 martom karpéh into human shape 9526; mart ~~, martë [GBR? 4-1] ~ 104%; 9621, 9819; 6 hàn 4 uštur ~ 9915, — Av. (467 sq.) kahrp-; Arm. lw. kerp; MPrs kyrb (A-H I), but Paz. karf.
2226:karpéh v. the preceding w.
2463:13%, but cas. obl. marté in the compound marté-karp 1049, v. karp; pl. cas. rect. ~ 5112; pl. cas. obl. —-än [GBR?-n']: gen. 28, 1512, 2523.27, P2:5 (GBR’-n); dat. 5312; agent 5319; — bandak ~ a slave 51$; varzékar =--ē a farmer 14"; ~ 4 artēštār the warrior 1316; magvé-~, még-~, v. magi; — as a mere indef. pron. 20°. 6615. 6815, 7039; — ~ 4 ahlav 3915. 829, but in pl. cas. obl. ahlavan —-än, druvandan ~-n 5312-13, — Av. (1148) marata- mars- tan-, whence MPrth mrd = Paz. NP mard ; Av. more common (ibid.) mašya- < martya- = OP martiya-, whence MPrs myrd.
2505:matak [NKB; m’tk'] female: gor ~ 112-4 (m’tk'); ~ karp 5717; čvak nar u čvak m 949-10.,,.., a-~ female... non-female 1041617, — Arm. lw. matak; MPrs m’yg (!); Paz. mädagi = abstr. mätakeh (SGV VIII, 16) and = mātakīk (ibd. XV, 27); NP mddah: from mat (g. v.).
2723:nikand [nknd] pt. = pret. 3d p. sg. 92%, uncertain: api-§ góhr  x"arrah be ~ seems to mean: he projected, threw forth, (from his own essence) its (= the earth’s) substance-light, i. e. the heavenly light which forms the substance of the material world, cf BdA p. 11? Ohur- mazd hac han i xvēš xvatēh getäh rošneh uy hac getäh rošneh karp + dāmān i xue$ frac brihénit, where gētāh rošneh seems to be a synonym of göhr xtarrah; nikandan from ni + the root kan- ‘to throw’ which is found in apakandan (g.v.).
3083:pat-sén [PWN syn'] breast bodice 5718, — DkM 63514-15: apar-ic 6 tē, Zartuxst, druž bē dvārēt mätak-karp, zarren-patsen (ku pistin-pin dārēt), v. pistan. — FrP 31 sénak, NP sinah ‘bosom, breast’.
3140:pēš-karp [pyš klp'] of conspicuous shape 56’, with the gl. ku pat tan cašmtar bit.
```


## [2026-09-06T22:15:08.216Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD nkrtk\"; grep -n \"nkrtk\\|n>krtk\\|n'krtk\\|nJkrtk\\|n\\*krtk\" SOD.txt | head -20; echo \"=== SOD uncoined\"; grep -n -i \"uncoined\\|silver\" SOD.txt | head -20"
}
```


### [2026-09-06T22:15:08.275Z] TOOL RESULT

```
=== SOD nkrtk
46321:na-krte,  nak(s)te,  nakarte  (n'krt'y,  n>krtk) 
46351:5761  n'krtk  ->  n»krt>k 
46375:5762  n'krtkvwnc   B 
46383:5763  n>krtk-(w)   B,  S 
=== SOD uncoined
40124:silver 
46336:silver  coloured 
46345:silvern 
46379:silvern 
46385:silver 
46397:silvern 
46436:silvern 
46441:silvern 
46446:silver(/io/  coined) 
46453:silvern 
46472:(o/)silver,  silvern 
93653:silver     4903,  5756,  5763,  5771, 
93656:silver  coloured     5758 
93657:silvern     5759,  5762,  5765,  5769,
```


## [2026-09-06T22:15:09.343Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls incoming/BQT/ && echo \"=== v4 head\"; head -3 incoming/BQT/BQT_v4_pages.txt && grep -c \"pdf page\" incoming/BQT/BQT_v4_pages.txt"
}
```


### [2026-09-06T22:15:09.396Z] TOOL RESULT

```
BQT_v3_pagemap.json
BQT_v3_pages.txt
BQT_v3_picofile.pdf
BQT_v4_pages.txt
BQT_v4_pages.txt.pages
BQT_v4_picofile.pdf
BQT_v5_pages.txt
BQT_v5_pages.txt.pages
BQT_v5_picofile.pdf
=== v4 head
[pdf page 1]
[pdf page 2]
ه
553
```


## [2026-09-06T22:15:11.268Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '46300,46480p' SOD.txt"
}
```


### [2026-09-06T22:15:11.321Z] TOOL RESULT

```
dragon 

TSP  3.131  &  etc.;  BSTBL,  Intox.  35,  Padm.  10; 
Frag.  Len.  9329:  O7  29;  BBB 

5754  nVm   C  J~*  jjju  «l^U 
na-kam   (L'k'm) 

unwilling 

BSTii  889.21;  Benv.  JA  1955,  310;  C2,  27R10  "not 
desiring" 

5755  nVstn'k   B  (U->;/  ^  :jt^>)v^U  «>^J 
nak-astane 

bathing  poo\(dragon-pond) 

TSP  3.126;  BSTBL,  Vim.  80;  GMS  1118 

5756  nWk   B  (•>J'li)SJLJsc*ji 
na-krte,  nak(s)te,  nakarte  (n'krt'y,  n>krtk) 

=>n'qty 
si\ver(not  coined) 
VJ  85,  55d,  558,  618,  8C;  BSTBL,  Dhy.  259, 

n>krt}kw;  VJ  46,  12(,  976,  n'krt'y,  VJ  84,  494, 

1163;  Dhy.  257 

5757  n'krt'y    B  =»  n'krt'k 

5758  n5krt>y  p>my   B  ^*j6 
na-krte-  Pame 

silver  coloured 

BSTBL,  Dhy.  262 

5759  n'kr^yn'k    B  ^j, 
nakrtene  (n'krt'yn'y,  n'krtyn'k)  ^n'ktn'k, 

n^tynyy,  n'krtynch 

silvern 

BSTBL,  Dhy.  259,  260,  261 

5760  n'krt'yn'y  =»  n'krt'yn'k,  n'ktynyy 

5761  n'krtk  ->  n»krt>k 


—■^■^^^AHH^^^M^^ 


mmm 


231 


n'mqyn 


j/»j* 


^ 


>n*qty 


5762  n'krtkvwnc   B 

na-krte-yonc 

silvern 

BSTBL,  Dhy.  290,  292 

5763  n>krtk-(w)   B,  S 
na-krte,  nak(ar)taku 
silver 

VJ  46,  12(,  976;  Anc.  Lett.  5.10,  21,  22,  27; 
BSTBL,  Dhy.  z*0,  292 

5764  n'krtyn'k  =*  n'krt'yn'k 

5765  n'krtynch   S  ^ju 
na-k(or)tenc,  nakrtcne   ©f.  adj.  =»n}ktync, 

n,krt»yn*k  * 

silvern 
MDii  Nov.  4R20 

5766  n'kry'cyq    M 
na-karya-cik   «*kry*cyq 
untimely 
GMS  1014,  1120;  Sund.  Man.  Lett.  310.11 


JtJ^^jJ  i*\>JJ^<i\j 


J**  jjX  ij\^ 


>rk 


A* 


Kjt-Oj* 


Lpi6^ 


5767  n'kt'rq   M 
na-k(o)t-  ark  ©adj. 
inactive,  ineffective 
Sogdica.  29.9,  GMS  1156 

5768  n'kt'rky'h   M 
na-k(o)t-arkya  ©adv. 
inactively 
Sogdica.  29.7  n  p30;  GMS  1156 

5769  n'qtc*  ?   M 
na-k(o)tca  ©f.  adj.  =»n*krtynch 
silvern 
BBB  el4 

5770  n'ktn'k    B 
nak(o)tne   =»nlkrtynch,  n'krtfy^k 
silvern 
TSP  7.12 

5771  n'qty   C 
na-k(s)te  GVkrt'y)  ©ace.  -tw 
silver(/io/  coined) 

STi  45-12,  49.1;  BBB;  GMS  1054,  -tw,  -fy,  BSTii: 
C2,  51R18,  21,  102R18 

5772  n'ktync   M 
na-k(3)tenc  ©f.  adj.  ^n'krtynch 
silvern 
Hen.  Sogd.  Cpds.  1945,  151;  GMS  1273 

5773  nJktynyy   M 
na-k(o)tene   (n'krt'yn'y) 


*_5  _j£~ ^0 


IfijAi 


iji°J* 


CSiO* 


(o/)silver,  silvern 

GMS  1054;  Hen.  Tales.  473.47;  BBB 

5774  n'm         *  (0>>>^  j-O^.^^ 
nam   ©<naman-   ©ob.  -y;  pi.  -/ 

name
```


## [2026-09-06T22:15:20.637Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pdf page\" SOD_pages.txt | head -3; echo ---; awk '/\\[pdf page 98\\]/,/\\[pdf page 100\\]/' SOD_pages.txt | head -80"
}
```


### [2026-09-06T22:15:22.309Z] TOOL RESULT

```
---
```


## [2026-09-06T22:15:25.000Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -5 SOD_pages.txt; echo \"---count\"; grep -c $'\\f' SOD_pages.txt; echo \"--- leaf 98\"; awk 'BEGIN{RS=\"\\f\"} NR==99' SOD_pages.txt | head -60"
}
```


### [2026-09-06T22:15:26.635Z] TOOL RESULT

```
 SOGDIAN
DICTIONARY
Sogdian - Persian - English


---count
642
--- leaf 98
                                                                                                                        'kySrp




33

     sinner                                                           TSP 2; Hen. Texts. 716; GMS 1558
     GMS      1125                                               854 'kwprm =» )kw5prm
                                                                 855 >kwrS(5) M                                           UT
841 'kt'nyy M                                        .lAjUjlT
                                                                     kur5 =»kwr5(5), qwrG
    (o)ktani ^'kr^nyCh), qt>ny                                       where
    sin, evil deed
                                                                      GMS 159, 1533
    BBB f9, 24; GMS 1035, 1038

842 >ktVk M                                          u^<*^3      856 'kwrts'r =» kwrts}r
    (o)kt-ark ©ob. pi. -tyy                                      857 'kws'nyk S
    dutiful, having carried out
                                                                      kosanik      ^kws'nyk^
    Gcrsh. Sogd. Cpds. 142; Sund. KG 2328                                                                               &f
                                                                      (o/)Kushan
                                                                      MDiii p!02
843 »ktw8»r- ** ^rtw^r-
                                                                 858 >kwsty B
844 >kty> M                                            J*"jf         kuste ? ©Skt. kustha                   (w_/ ^</)? loJ
     (o)ktya      Okrtyh, }qtyy)   ^'krt'y, *krty, qty2,              costusiname of a plant)
       >krty>
     action, act                                                      TSP 1172, 19.20 n p232
                                                                                                              (wS^L»^ t^^J^r ^
     BBB 627; GMS 948; Gersh. Sogd. Cpds. 141                    859 >kwts>r      B, S

845 'ktyy =* >krt>y                                                   (o)kutsar
                                                                      where to
846 >qtyy     C ** 'krt'y, )kty)
                                                                      VJ 407 etc.; KG 330; GMS 461 n 1, 1534;
847 >k\vl B, S                        (0>> j^-J J~>)^J<>*!U "*
                                                                         dog
                                                            f^          'ifcwi-Sy.GMS 1532; SCE 516
    (o)ko ^kw\ k-, kV
    to, towards                                                  860 >kwt-(y)       B, S                                  JL
    Anc. Lett. 1.7, 3.9 11,20                                        (o)kut     Ckwtyy, kwty, }qwtyst)      ©nom. gen. -y;
848 W         B                                                        abl. -»; pi. -(>)yh, -1st    =»kwt

     (o)ku ^k'w3, kw3
     wherever                                                        GMS 159; Frag. Len. 83 b 6, 93, 37; -y, TSP
                                                                       2.772, 3.138, 254, 13.188; Anc. Lett. 3.24; SCE
     VJ 531 etc.; BSTBL, Vim. 165; TSP; GMS 159,
       1555                                                            313; abl. >kwt\ SCE 124; TSP 3.188; pi. >kwtyh,
                                                                       SCE 226; TSP 2.784; >qwtyst, GMS 1186
849 >qwc- C                                            j^J\      861 >kw(-)ty B                      .^           <<T^> <b*f
    akoc =»*qwc-, 'k'we-
                                                                     (o)ku-ti, ku-tc ? (kwty, JkwZY)
    GcOhang, (rc)suspend
                                                                     where, how
    BSTii 867.25; C2, 27R25
                                                                     GMS 1532, 1516; VJ 43\ SCE 91, 206, 396; 'kwty
850 'kwc'n'y B                     (jW^-^/v^/
    (o)kocane ^kwc'n'k                                                 pw nwkr, TSP 2.871, "absolutely"
```


## [2026-09-06T22:15:30.334Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==98' SOD_pages.txt | head -70"
}
```


### [2026-09-06T22:15:31.849Z] TOOL RESULT

```
'krt'rzt'k

                                                                                                                            32
 815 'krt'rzt'k B                                     L^.Suir    827 'krty'kh      S                                fluf .xj-*
      Okr^rztk) ^krt'rzt'w                                           (a)krtyak
      absolutely                                                     sin, evil deed
                                                                     Sund. MHC p27.10
      TSP 6.188, 14.14 n p203; Benv. Notesiv 496;
                                                                 828 >krty>kryyh      M
        Mack, n p50, 22 BSTBL
 816 »krt'rzt'w    B                                UiW              (o)krtya-kare                                  15^'lM*

      ^krt'rzt'k                                                     performer
                                                                     Hen. Sogdica. 55.14 p57
      absolutely
      BSTBL, Padm. 61, 67; Dhy. 22(N); TSP 6.28                  829 'krtyh     B, S =» }krty>

 817 'krt'rztk =* ^rl'rzt'k                                     830 'krtyy M => >krty, >krt>y
                                                                831 >ks- B                                      *J^./<jy
 818 'krt'sp's B                              ^LUUij,^!*,            (o)kasc, (o)kos(e)?      Oks}y) ©Av. kdrdsa-, Khwar
     (o)krt-sspas ©Pahl. krtsp*s                                       yks =*ks-    -
     obedient, dutiful
                                                                     small, thin
     BSTBL, Dhy. 7; Gersh. Sogd. Cpds. 140, 147
                                                                     GMS 1201; Benv. VJ n p94, 39d; Inst. >ks\ SCE
819 'krt'wcy B                                ju^" j>ju /un-           76; pi. >kstK VJ 1264; MSP bl58
    certainly
     BSTBL, Dhy. 400                                            832 >ks>y =* >ks-
                                                                833 >qsy C
820 >krt>y B, S                   (jy >^- j;)J^ <X                   a/akasc ?
    (o)krte Okrtyy, >krt'k, *krtkt 'ktyy, }qtyy) ©ace.               overseer
                                                                                                                     ^U* <^U»o
       ykrt\v\ f. >kr0   -^kty*, qty\ >krty, qty2                    BSTii 897.73; STSC 58; C2, 55R13
     action, deed                                                                                                    cJjO^j
                                                                834 >ksn    B
     TSP; Sogdica. 60; KG; MSP; BSTBL; STii 10.28;
       MD                                                            (o)kasn, ksan ? ©Skt. ksana =»ksn2
                                                                     time, moment
821 'krtch B, S                                        u*<jf         TSP 2.121 n pl70
    (o)krtc ©f. adj. ^kr^y
                                                                835 >kst-     M, S
    action, deed
     TSP 8.86-, VJ 1053; MDii; 'jfcrcfc, Frag. 5.10                  (o)kist, kost   =>qs-                           X. iir
822 >krtk => >krt>y                                                 GMS
                                                                    0<?)sow926; MDiii
823 >krtw ** >krt>y                                             836 »ksty(y) M
824 'krtwS'r-    B, S     (0>> >^^ jjJo^^i o^                        (o)kiste, koste
    (o)krtu-6ar OktwS'r-, 'kS'r-, qtJr-) ©perf . st.                 OcOsow, sowing, tilling
      =»>krt-, qG'r-                                                 BBB 570; Tales. 470.55; GMS 926, 931
     (to)do
     GMS 167, 877; BBB 518, 706                                 837 >ksyc M, C                              (£l <^1)J&
                                                                    akasec ? CksMc) ©Av. aka-           ^'xsyc
825 >krty B, S              (j^ ^~> Jj)l»J'ij-*<jf                  hook                                        >krt-.
    (a)krte Okrt'k, 'krtyy) ©ace. >krtw, f. }krt\ inf.              Hen. Sogdica. 30.11a
      >krty =*}kty\ 'krt'y                                      838 >kt- M, C
    action, deed
                                                                    (o)k(o)t Cqt-)        ©pt. st. =*kwn-
    VJ; TSP; BSTBL; SCE 475; STii; MDii; GMS 847;
      BBB 542                                                         krt-, qt-
                                                                                                             ^ ji)d^ to* J*
826 >krty) M, B                                                     0o)do, (r6»)become
                                               l^lo^X               GMS 144, 148, 578, 603
    (o)krtya Okrtyh) ©Skt. karman           ©f. n. =>>kty\
                                                                839 >qt- =¥ >kt-
      qty2, qty>
    action                                                      840 'qt'nyk'ry M
                                                                                                       ^kr^nk'ry,
    VJ; TSP; SCE; BSTBL; Frag. Len. 92.6; STii 10;                  (o)ktani-kare ©ob. pi. ~ty
                                                                      'krt'nyk'r'k, qt'nyq'ry
      GMS 948; S W, AO 1981, 14; C2 pl33
```


## [2026-09-06T22:15:46.334Z] TOOL CALL #29: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T22:15:46.343Z] TOOL RESULT

```


```


## [2026-09-06T22:15:50.307Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%88%D8%B2%DB%8C%D8%B1",
 "prompt": "Give the full etymology sections for Persian وزیر and Arabic وزير: origins, Middle Persian wizīr, Avestan vīčira-, and any dispute about Arabic w-z-r 'burden'."
}
```


## [2026-09-06T22:15:51.611Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D9%82%D8%B1%D9%87",
 "prompt": "Give the full etymology of Persian نقره 'silver' and of Arabic نقرة. Mention any Sogdian nʾkrtʾk 'uncoined silver' connection."
}
```


### [2026-09-06T22:15:56.082Z] TOOL RESULT

```
# Etymology of وزیر (wazīr)

Based on the Wiktionary content provided, I can only offer limited information:

## Persian وزیر

The article states: "Borrowed from Arabic وَزِير (wazīr)." No further etymological details about Middle Persian, Avestan, or disputed origins appear in the source material.

## Arabic وزير

The page references Arabic وَزِير (wazīr) as the source, but the actual Arabic entry content is not included in the provided text.

## Important limitation

The content you've shared does not contain the detailed etymological information you're requesting about:
- Middle Persian *wizīr*
- Avestan *vīčira-*
- Disputes regarding the Arabic root w-z-r and its meaning ("burden")

To obtain this comprehensive etymological analysis, you would need to access the full Arabic entry on Wiktionary or consult specialized historical linguistics sources on Indo-Iranian and Semitic language connections.
```


### [2026-09-06T22:15:57.575Z] TOOL RESULT

```
# Etymology of Persian نقره and Arabic نقرة

Based on the Wiktionary entry provided:

**Persian نقره (nuqra/noġre):** The entry states it was "Borrowed from Arabic _نُقْرَة_ (nuqra)."

**Arabic نقرة:** The source document does not provide detailed etymological information about the Arabic term itself, only that the Persian word derives from it.

**Sogdian Connection:** The references section mentions "Gharib, B. (1995), 'n'krtk-(w)'" in the _Sogdian dictionary: Sogdian–Persian–English_. This indicates a Sogdian term n'krtk-(w) exists, suggesting a potential etymological link to the Persian/Arabic forms, though the document does not explicitly describe the relationship or provide the Sogdian term's meaning beyond the page reference.

The available content confirms a Persian-from-Arabic borrowing pattern but lacks comprehensive etymological depth regarding proto-language origins or detailed Sogdian connections.
```


## [2026-09-06T22:16:04.294Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad 2>/dev/null || mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; for w in \"%D9%86%D9%82%D8%B1%D9%87\" \"%D9%88%D8%B2%D9%8A%D8%B1\" \"%D9%88%D8%B2%DB%8C%D8%B1\" \"%DA%86%D8%A7%D8%B1%D9%87\"; do echo \"=== $w\"; curl -s \"https://en.wiktionary.org/wiki/$w?action=raw\" | head -120; done"
}
```


### [2026-09-06T22:16:07.081Z] TOOL RESULT

```
=== %D9%86%D9%82%D8%B1%D9%87
==Persian==
{{chemical element box|fa}}
{{wp|fa:}}

===Etymology===
{{ety|fa|:bor|ar:نُقْرَة|text=+|tree=1}}

===Pronunciation===
{{fa-IPA|nuq`ra}}

===Noun===
{{fa-noun|cls=نُقْرَه}}

# [[silver]] {{gloss|metal}}
#: {{syn|fa|{{fa-l|سِیم}}|q=literary}}
#* {{RQ:fa:Masnavi|I|178|زر و نقره گر نبودندی نهان / پرورش کی یافتندی زیر کان‌|{{xlit|fa-cls|زَرّ و '''نُقْرَه''' گَر نَبُودَنِی نِهَان / پَرْوَرِش کَی یَافْتَنْدِی زیرِ کَان}}|If gold and '''silver''' were not hidden, how would they get nourishment [grow and ripen] in the mine?|cls=1}}

====Derived terms====
* {{fa-l|نُقْرَه‌اِی}}

====See also====
{{col2|fa
|{{fa-l|طِلَا//طَلَا|t=gold}}
|{{l|fa-ira|برنز|tr=boronz|t=bronze}}
}}

===References===
• ↑ Gharib, B. (1995), “n'krtk-(w)”, in ''Sogdian dictionary: Sogdian–Persian–English'', Tehran: Farhangan Publications, page 231

{{C|fa|Chemical elements|Metals}}=== %D9%88%D8%B2%D9%8A%D8%B1
{{also|وزیر}}
==Arabic==

===Etymology===
The original attested meaning is “assistant”, and the political sense only arose in the {{w|Umayyad period}}. Likely related to the verb {{l|ar|وَزَرَ|t=to carry, to shoulder}} with the root {{ar-root|و ز ر}}, meaning “someone who carries a burden”, but owing to the idea of assistance by handmen this may be denominal. Likely borrowed from an {{bor|ar|ira|-}} term surfacing as {{cog|pal||tr=wcyl|ts=vičīr|t=decision, judgment}}, {{cog|ae|𐬬𐬍𐬗𐬌𐬭𐬀|tr=vīcira|t=arbitrator, judge|lit=deciding, one who is taking or has made a decision}}, {{cog|xcl|վճիռ}}.

===Pronunciation===
{{ar-pr|وَزِير}}
* {{audio|ar|Ar-وزير.ogg}}

===Noun===
{{ar-noun+|وَزِير|m|pl=وُزَرَاء}}

# [[minister]], cabinet minister
# [[vizier]]
# [[helper]], [[assistant]]
# {{lb|ar|chess}} [[queen]]

====Declension====
{{ar-decl-noun|وَزِير|pl=وُزَرَاء}}

====Derived terms====
* {{l|ar|وَزِير الْخَارِجِيَّة||[[foreign minister]], [[Secretary of State]]}}

====Related terms====
* {{l|ar|وِزَارَة}}
* {{l|ar|وِزَارِيّ}}

====Descendants====
{{top2}}
* {{desc|bor=1|ca|algutzir|alts=1}}
** {{desc|bor=1|it|aguzzino}}
** {{desc|bor=1|pms|argosin|lagosin}}
* {{desctree|fa-cls|وزیر|tr=wazīr|bor=1}}
* {{desc|bor=1|syc|ܘܙܝܪܐ|tr=wazzīrā}}
** {{desc|aii|ܘܲܙܝܼܪܵܐ}}
* {{desc|bor=1|en|wazir}}
* {{desc|bor=1|ms|wazir}}
** {{desc|id|wazir}}
* {{desc|bor=1|es|alguacil|alguazil|aguacil}}
** {{desc|bor=1|en|alguazil}}
* {{desc|sw|waziri|bor=1}}
{{bottom}}

===See also===
{{table:chess pieces/ar}}

===References===
* {{R:ar:Cheung|pages=19–20}}
* {{R:Eilers:1962|pages=216–218}}
* {{R:ar:Lane|page=2939b}}
* {{R:ar:Shapira-IA|page=182}}

{{C|ar|Government|Occupations}}

==Pashto==

===Etymology===
{{bor+|ps|ar|وَزِير|tr=assistant}}.

===Pronunciation===
* {{IPA|ps|/wəzir/}}

===Proper noun===
{{head|ps|proper noun|g=m|tr=Wëzír}}

# [[Wazir]], a [[Pashtun]] tribe
# {{given name|ps|male|Arabic|xlit=Wazir}}

{{C|ps|Tribes}}

==South Levantine Arabic==

===Etymology===
{{ety|ajp|:inh|ar:وَزِير|text=+|tree=1}}

===Pronunciation===
* {{ajp-IPA|wazīr<p:waˈziːr>}}
* {{audio|ajp|LL-Q55633582 (ajp)-Khalil.rantissi-وزير.wav|a=al-Lidd}}

===Noun===
{{ajp-noun|g=m|tr=wazīr|pl=وزرا|pltr=wuzara}}

# [[minister]]
# {{lb|ajp|chess}} [[bishop]]

====See also====
{{table:chess pieces/ajp}}=== %D9%88%D8%B2%DB%8C%D8%B1
{{also|وزير}}

==Ottoman Turkish==

===Etymology===
{{bor+|ota|ar|وَزِير}}. {{root|ota|ar|و ز ر}}

===Noun===
{{ota-noun|head=وزیر|tr=vezir|pl=وزیرلر|pltr=vezirler}}

# [[minister]], cabinet minister
# [[vizier]]
# [[helper]], [[assistant]]
# {{lb|ota|chess}} [[queen]]

====Descendants====
{{top2}}
* {{desc|tr|vezir}}
* {{desc|bg|вези́р|bor=1}}
* {{desc|frm|visir|bor=1}}
** {{desc|fr|vizir|visir}}
** {{desc|ca|visir|bor=1}}
** {{desc|nl|vizier|bor=1}}
** {{desctree|en|vizier|bor=1}}
** {{desc|it|visir|bor=1}}
** {{desc|pt|vizir|bor=1}}
** {{desc|es|visir|bor=1}}
* {{desc|de|Wesir|bor=1}}
* {{desc|la|vezirus|bor=1}}
* {{desc|lt|viziris|bor=1}}
* {{desc|mk|везир|bor=1}}
* {{desc|pl|wezyr|bor=1}}
* {{desc|ro|vizir|bor=1}}
* {{desc|ru|визи́рь|bor=1}}
* {{desc|sh|-|bor=1}}
*: {{desc|sh|вѐзӣр|sclang=1}}
*: {{desc|sh|vèzīr|sclang=1}}
* {{desc|sv|vesir|bor=1}}
* {{desc|uk|візи́р|bor=1}}
{{bottom}}

==Persian==
{{wp|fa:}}

===Etymology===
{{ety|fa|:bor|ar:وَزِير|text=+|tree=1}}

===Pronunciation===
{{fa-IPA|wa`zīr}}

===Noun===
{{fa-noun|cls=وَزِیر|pl=وزرا|pltr={{fa-xlit|وُزَرَا}}|pl2=وزیران}}

# [[minister]]
# [[vizier]]
# {{lb|fa|chess}} [[queen]]

====Related terms====
{{col|fa|وزارت<tr:{{fa-xlit|وِزَارَت}}>}}

====Descendants====
{{top2}}
* {{desc|prs|وزیر|tr=wazīr}}
* {{desc|fa-ira|وزیر|tr=vazir}}
* {{desc|tg|вазир}}
** {{desc|yai|ԝазир|bor=1}}
* {{desc|az|vəzir//вәзир|bor=1}}
* {{desc|bor=1|bn|উজির|tr=uzir}}
* {{desc|chg|وزیر|bor=1}}
** {{desc|ug|ۋەزىر//вәзир|bor=1}}
** {{desc|uz|vazir//вазир|bor=1}}
* {{desc|gu|વજીર|bor=1}}
* {{desc|inc-hnd|-|bor=1}}
*: {{desc|hi|वज़ीर|विज़ीर}}
*: {{desc|ur|وَزِیر}}
* {{desctree|bor=1|ota|وزیر|tr=vezîr}}
* {{desc|ps|وزیر|tr=wazír|bor=1}}
* {{desc|pa|-|bor=1}}
*: {{desc|pa|sclang=1|ਵਜ਼ੀਰ}}
*: {{desc|pa|sclang=1|وَزِیر}}
{{bottom}}

===See also===
{{table:chess pieces/fa}}

{{C|fa|Government|Occupations}}

==Urdu==

===Etymology===
{{bor+|ur|fa-cls|وَزیر|tr=vazīr}}, from {{der|ur|ar|وَزِير}}. {{root|ur|ar|و ز ر}}

===Pronunciation===
* {{ur-IPA|vazīr}}

===Noun===
{{ur-noun|m|head=وَزِیر|hi=वज़ीर|pl=وُزَرا,وَزِیران}}

# {{lb|ur|government}} [[minister]]
#: {{uxa|ur|'''وَزِیرِ''' تِجارَت| '''minister''' of commerce}}
# [[vizier]]
# {{lb|ur|chess}} [[queen]] / [[fers]]
#: {{syn|ur|فَرْزِین}}

====Declension====
{{ur-noun-c-m|1=وزیر|2=vazīr}}

====Related terms====
{{col|ur|وِزارَت}}

====See also====
{{table:chess pieces/ur}}

===References===
* {{R:Rekhta}}
* {{R:Platts}}=== %DA%86%D8%A7%D8%B1%D9%87
==Old Anatolian Turkish==

===Etymology===
{{bor+|trk-oat|fa-cls|چاره|tr=čâre}}.

===Noun===
{{head|trk-oat|noun|tr=çāre}}

# {{lb|trk-oat|medicine}} [[cure]], [[remedy]], [[medicine]], [[treatment]]; an application, medicine, or treatment that relieves or [[cure]]s a disease.
#: {{syn|trk-oat|ام|tr=em|دوا|tr2=devā| علاج|tr3=ʼilāc|درمان|tr4=dermān}}
#: {{ant|trk-oat|سم|tr=sem|اغو|tr2=aġu|زهر|tr3=zehr}}
# {{lb|trk-oat|figurative}} [[solution]], [[remedy]]
#: {{syn|trk-oat|ام|tr=em|دوا|tr2=devā|درمان|tr3=dermān}}

====Derived terms====
{{col|trk-oat|بی‌چاره<tr:bī-çāre><t:[[uncurable]]; [[helpless]]>
|چاره‌سز<tr:çāresüz><t:[[uncurable]]; [[helpless]]>
|چاره ایتمك<tr:çāre ẹtmek><t:to [[cure]]>
|چاره اولمق<tr:çāre olmaq><t:to [[solve]], to [[cure]]>
}}

====Descendants====
* {{desc|az|çarə}}
* {{desctree|ota|چاره|tr=çare}}

===Further reading===
* {{R:trk-oat:Cetin|page=76|çāre}}

==Ottoman Turkish==

===Etymology===
{{inh+|ota|trk-oat|چاره|tr=çāre}}, from {{der|ota|fa-cls|چاره|tr=čâre|t=remedy, help}}.

===Noun===
{{ota-noun|tr=çare}}

# [[remedy]], [[cure]], a [[medicine]] or [[treatment]] that relieves a [[disease]]
#: {{syn|ota|درمان|tr1=derman|دوا|tr2=deva|علاج|tr3=ʼilac}}
# [[remedy]], [[expedient]], [[solution]], something that [[correct]]s or [[counteract]]s
#: {{syn|ota|درمان|tr=derman}}

====Derived terms====
{{col3|ota
|چاره بولمق<t:to find a remedy><tr:çare bulmak>
|چاره‌پرداز<t:one who prepares a remedy><tr:çareperdaz>
|چاره‌جو<t:one who seeks a remedy><tr:çarecu>
|چاره‌ساز<t:one who prepares a remedy><tr:çaresaz>
|چاره‌سز<t:irremediable><tr:çaresiz>
|چاره‌یاب<t:one who finds a remedy><tr:çareyab>
}}

====Descendants====
* {{desc|tr|çare}}
* {{desc|sq|çare|bor=1}}
* {{desc|hy|չարէ|չարա|bor=1}}
* {{desc|mk|чаре|bor=1}}

===Further reading===
{{col-top|2|click to expand}}
* {{R:tr:OTK|çare1|vol=1|page=889}}
* {{R:ota:Hindoglu|page=175b}}
* {{R:ota:Kelekian|page=459}}
* {{R:ota:Meninski|C|column=1458|Remedium}}
* {{R:ota:Meninski|L|column=1548}}
* {{R:tr:Nishanyan|çare}}
* {{R:ota:Redhouse|page=704}}
{{col-bottom}}

==Persian==

===Etymology===
From {{inh|fa|pal|tr=cʾlk'|ts=čārag|t=means, remedy|sc=Phlv}}, suffixed form of synonymous {{m|pal|tr=cʾl|ts=čār|sc=Phlv}}, ultimately probably from {{der|fa|ine-pro|*kʷer-|t=to do; to make; to build}}. Akin to {{cog|xcl|ճարակ}}, an Iranian borrowing.

===Pronunciation===
{{fa-IPA|čā`ra}}

===Noun===
{{fa-noun|cls=چَارَه}}

# [[remedy]], [[help]]
# [[solution]], [[answer]]

====Derived terms====
* {{l|fa|بی‌چاره|tr=bê-čâre}}

====Descendants====
* {{desc|ba|сара|bor=1}}
* {{desc|kk|шара|bor=1}}
* {{desc|gu|ચારા|bor=1}}
* {{desc|acm|چارة|bor=1}}
* {{desctree|trk-oat|چاره|tr=çāre|bor=1}}
* {{desc|tk|çäre|bor=1}}

===Further reading===
* {{R:xcl:AG|page=188}}
* {{R:pal:CPD|page=21}}
```


## [2026-09-06T22:16:19.314Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; for w in \"%D9%86%D9%82%D8%B1%D8%A9\" \"Reconstruction:Proto-Indo-European/k%CA%B7er-\" \"Reconstruction:Proto-Indo-European/kr%C3%A9p-\" \"%F0%90%AC%A9%F0%90%AC%8C%F0%90%AC%80%F0%90%AC%8B%F0%90%AC%99%F0%90%AC%8C%F0%90%AC%81\"; do echo \"=== $w\"; curl -s \"https://en.wiktionary.org/wiki/$w?action=raw\" | head -80; echo; done"
}
```


### [2026-09-06T22:16:21.717Z] TOOL RESULT

```
=== %D9%86%D9%82%D8%B1%D8%A9
{{also|نقره}}

==Arabic==
{{ar-rootbox|ن ق ر}}

===Noun===
{{ar-noun|نَقْرَة|f|pl=نَقَرَات}}

# {{ar-instance noun of|نَقَرَ}}

====Declension====
{{ar-decl-noun|نَقْرَة|pl=نَقَرَات}}

====Descendants====
{{q|via plural form {{m|ar|نَقَرَات}}}}:
* {{desc|az|nəqərat|nəqarət|bor=1}}
* {{desc|chg|نقرات|ts=näqärāt|bor=1}}
** {{desc|uz|naqarot|naqorat}}
** {{desc|ug|نەقرات}}
* {{desc|ota|نقرات|tr=nakarat|bor=1}}
** {{desc|tr|nakarat}}

===Noun===
{{ar-noun|نُقْرَة|f|pl=نُقَر,نِقَار}}

# [[cavity]], [[cleft]], [[socket]]
# {{lb|ar|archaic}} [[concentration]] of [[silver]], [[high]]-[[quality]] [[silver]]
# [[hollow]] of the [[backneck]], {{w|condyloid fossa}}

====Declension====
{{ar-decl-noun|نُقْرَة|pl=نُقَر|pl2=نِقَار}}

====Descendants====
* {{desc|chg|نقرة|ts=nuqrä⁠|bor=1}}
** {{desc|ug|نوقرە}}
** {{desc|uz|nuqra}}
* {{desc|la-med|nucra|nocra|bor=1|qq=variant forms of {{m|la|nucha}}}}
* {{desc|axm|նուկրայ|bor=1}}
* {{desc|fa|نقره|tr=noqre|bor=1|t=silver}}
** {{desc|lrc|نووغڕںە|tr=nuqerrə}}
* {{desc|syc|ܢܘܽܩܪܐ|tr=nuqra|bor=1|t=hole; silver}}

===Noun===
{{ar-noun|نِقْرَة|f}}

# [[quarrel]], [[strife]], [[hassle]]

====Declension====
{{ar-decl-noun|نِقْرَة}}

===Further reading===
* {{R:ar:Hyrtl|pages=188–193}}
* {{R:sog:Gharib|head=n'krtk-(w)|page=231}}

{{C|ar|Silver|Bones}}

==Moroccan Arabic==
{{ary-rootbox|ن ق ر}}
{{chemical element box|ary}}

===Etymology===
{{ety|ary|:inh|ar:نُقْرَة|text=+|tree=1}}

===Pronunciation===
* {{IPA|ary|/nuq.ra/}}

===Noun===
{{ary-noun|g=f|tr=nuqra|pl=-}}

# [[silver]]
#: {{syn|ary|فضة|tr=faḍḍa}}

{{c|ary|Metals}}
=== Reconstruction:Proto-Indo-European/k%CA%B7er-
{{reconstructed}}
==Proto-Indo-European==
{{etymon|ine-pro|id=do|pos=root}}

===Etymology===
The original meaning is often reconstructed as "to carve, to shape by cutting", based on the Anatolian forms.<ref name="Kloekhorst" /><ref name="LIV" />

===Root===
{{ine-root|pf}}<ref name="LIV">{{R:ine:LIV|head=*k<sup>u̯</sup>er- '(ab)schneiden, schnitzen'|page=391}}</ref><ref>{{R:ine:EIEC|362}}</ref>

# to [[do]]
# to [[make]]
# to [[build]]
# [[bowl]], [[vessel]]

====Synonyms====
* {{?}} {{l|ine-pro|*yeh₁-|gloss=to do, make; act vigorously}}<ref>{{R:ine:Mallory:2006|369}}</ref>
* {{l|ine-pro|*h₂er-|gloss=to prepare, make ready}}

====Derived terms====
{{rootsee}}

* {{l|ine-pro|*kʷért|*kʷér-t ~ *kʷr-ént|pos=root aorist}}<ref name="LIV" /><ref name="Kloekhorst">{{R:ine:Kloekhorst2008|head=kuer-<sup>zi</sup>|pages=486-487}}</ref>
* {{l|ine-pro||*kʷr̥-néw-ti ~ *kʷr̥-nw-énti|pos=néw-present}}<ref name="LIV" />
** {{desc|iir-pro|*kr̥náwti}} {{see desc}}
* {{l|ine-pro||*kʷr̥-sḱ-éti ~ *kʷr̥-sḱ-ónti|pos=sḱe-present}}<ref name="LIV" />
** {{desc|ine-ana-pro}}
*** {{desc|hit|𒆪𒉿𒅈𒀸𒆠𒄑𒍣|tr=ku-wa-ar-aš-ke-ez-zi|ts=kuwaraškezzi}}
* {{l|ine-pro||*kʷér-(h₁)s-eti ~ *kʷér-(h₁)s-onti|pos=(h₁)se-desiderative}}<ref name="LIV" />
** {{desc|ine-ana-pro}}
*** {{desc|hit|tr=ku-e-er-šu-un|pos=1sg.pret.act.}}, {{l|hit|tr=kur-ša-a-i|t=to cut off|pos=2sg.imp.act.}}
* {{l|ine-pro||*kʷí-kʷr̥-(h₁)s-eti ~ *kʷí-kʷr̥-(h₁)s-onti|pos=reduplicated (h₁)se-desiderative}}<ref name="LIV" />
** {{desc|ine-ana-pro}}
*** {{desc|hit|tr1=ku-kur-ša-an-t-|tr2=ku-gur-ša-an-t-|t2=to cut up, to mutilate|pos2=part.|unc=1}}<ref>{{R:ine:Kloekhorst2008|head=kukkurš-<sup>zi</sup>|page=491}}</ref>
** {{desc|iir-pro|*číkr̥Hšati}}
*** {{desc|inc-pro|*ćíkr̥Hṣati}}
**** {{desc|sa|चिकी॑र्षति}}
* {{l|ine-pro||*kʷér-kʷor- ~ *kʷér-kʷr̥-|pos=intensive}}<ref name="LIV" />
** {{desc|ine-ana-pro}}
*** {{desc|hit|tr=kurkuriyat}}
** {{desc|iir-pro|alt=*kárkr̥-}} {{q|as if from {{m|ine-pro||*kʷor-kʷr̥-}}; expected {{m|iir-pro||**čárkr̥-}}}}
*** {{desc|inc-pro|alt=*kárkr̥-}}
**** {{desc|sa|करि॑क्रत्|pos=act. participle}}<ref group="note">With restoration of the initial {{IPAchar|/k/}} and irregular addition of ''-i-'' as if from a root {{m|ine-pro||*kʷerH-}}.{{attn|ine-pro}}</ref>
* {{l|ine-pro||*kʷor-éye-ti ~ *kʷor-éy-onti|pos=éye-causative}}<ref name="LIV" />
** {{desc|iir-pro|*kāráyati}}
*** {{desc|inc-pro|*kāráyati}}
**** {{desc|sa|का॒रय॑ति|का॒रय॑ते}}
* {{l|ine-pro||*kʷe-kʷór-e|pos=perfect}}
** {{desc|iir-pro|*čakā́ra}}
*** {{desc|inc-pro|*ćakā́ra}}
**** {{desc|sa|च॒कार॑|t=has made}}
*** {{desc|ira-pro}}
**** {{desc|ae|𐬗𐬁𐬑𐬭𐬀𐬭𐬆|pos=3pl.perf.}}
**** {{desc|peo|𐎨𐎧𐎼𐎡𐎹𐎠|ts=caxriyā|pos=3sg.perf.opt.}}
* {{l|ine-pro||*kʷér-os}}
** {{desc|gem-pro|*hweraz|t=cauldron}} {{see desc}}
* {{l|ine-pro||*kʷér-ōr}}
** {{desc|grc|πέλωρ|t=supernatural monster}}
*** {{desc|grc|πελώρῐος|der=1}}
**** {{desc|el|πελώριος|t=gigantic, enormous}}
* {{l|ine-pro||*kʷór-o-s}}
** {{desc|iir-pro|*kā́ras}}
*** {{desc|ira-pro|*kā́rah}}
**** {{desc|pal|tr=kʾl|ts=kār|t=work; deed; affair}}
***** {{desc|fa|کار|tr=kâr|t=work}}
* {{l|ine-pro||*kʷér-tis ~ *kʷr̥-téy-s}}
** {{desc|iir-pro|*kŕ̥tiš}}
*** {{desc|inc-pro|*kŕ̥tiṣ}}
**** {{desc|sa|कृति॑|t=the act of doing}}
*** {{desc|ira-pro|*kŕ̥tiš}}
**** {{desc|ae|𐬐𐬆𐬭𐬆𐬙𐬌|t=doing; action}}
***** {{desc|pal|-|ts=-kird, -gird|bor=1|t=-doing; -making}} {{q|only in the combination Avestan loanwords, e.g. {{l|pal|𐫛𐫡𐫢𐫏𐫃𐫏𐫡𐫅}}, {{l|pal|tr=plškrt'|ts=frašagird|sc=Phlv|t=restoration}}, from {{l|ae|𐬟𐬭𐬀𐬱𐬋𐬹𐬐𐬆𐬭𐬆𐬙𐬌}}}}
*****: {{desc|pal|tr=-krt'|sc=Phlv|sclang=1}}
*****: {{desc|pal|-𐫃𐫏𐫡𐫅|sc=Mani|sclang=1}}
* {{l|ine-pro||*kʷér-tu-s ~ *kʷr̥-téw-s}}
** {{desc|cel-pro|*kʷritus|t=form; shape}} {{see desc}}
* {{l|ine-pro||*kʷr̥-tó-s}}
** {{desc|iir-pro|*kr̥tás}} {{see desc}}
* {{l|ine-pro||*kʷr̥-yos}}
** {{desc|cel-pro|*kʷaryos|t=cauldron}} {{see desc}}

=== Reconstruction:Proto-Indo-European/kr%C3%A9p-
<!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<title>Wikimedia Error</title>
<style>
* { margin: 0; padding: 0; }
body { background: #fff; font: 15px/1.6 sans-serif; color: #333; }
.content { margin: 7% auto 0; padding: 2em 1em 1em; max-width: 640px; display: flex; flex-direction: row; flex-wrap: wrap; }
.footer { clear: both; margin-top: 14%; border-top: 1px solid #e5e5e5; background: #f9f9f9; padding: 2em 0; font-size: 0.8em; text-align: center; }
img { margin: 0 2em 2em 0; }
a img { border: 0; }
h1 { margin-top: 1em; font-size: 1.2em; }
.content-text { flex: 1; }
p { margin: 0.7em 0 1em 0; }
a { color: #0645ad; text-decoration: none; }
a:hover { text-decoration: underline; }
code { font-family: sans-serif; }
summary { font-weight: bold; cursor: pointer; }
details[open] { background: #970302; color: #dfdedd; }
.text-muted { color: #777; }
@media (prefers-color-scheme: dark) {
  a { color: #9e9eff; }
  body { background: transparent; color: #ddd; }
  .footer { border-top: 1px solid #444; background: #060606; }
  #logo { filter: invert(1) hue-rotate(180deg); }
  .text-muted { color: #888; }
}
</style>
<meta name="color-scheme" content="light dark">
<div class="content" role="main">
<a href="https://www.wikimedia.org"><img id="logo" src="https://www.wikimedia.org/static/images/wmf-logo.png" srcset="https://www.wikimedia.org/static/images/wmf-logo-2x.png 2x" alt="Wikimedia" width="135" height="101">
</a>
<div class="content-text">
<h1>Error</h1>

<p>Not Found</p>
</div>
</div>
<div class="footer"><p>If you report this error to the Wikimedia System Administrators, please include the details below.</p><p class="text-muted"><code>Request served via cp1100 cp1100, Varnish XID 822121689<br>Upstream caches: cp1100 int<br>Error: 404, Not Found at Sun, 06 Sep 2026 22:16:21 GMT<br><details><summary>Sensitive client information</summary>IP address: 187.15.139.71</details></code></p>
</div>
</html>

=== %F0%90%AC%A9%F0%90%AC%8C%F0%90%AC%80%F0%90%AC%8B%F0%90%AC%99%F0%90%AC%8C%F0%90%AC%81
<!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<title>Wikimedia Error</title>
<style>
* { margin: 0; padding: 0; }
body { background: #fff; font: 15px/1.6 sans-serif; color: #333; }
.content { margin: 7% auto 0; padding: 2em 1em 1em; max-width: 640px; display: flex; flex-direction: row; flex-wrap: wrap; }
.footer { clear: both; margin-top: 14%; border-top: 1px solid #e5e5e5; background: #f9f9f9; padding: 2em 0; font-size: 0.8em; text-align: center; }
img { margin: 0 2em 2em 0; }
a img { border: 0; }
h1 { margin-top: 1em; font-size: 1.2em; }
.content-text { flex: 1; }
p { margin: 0.7em 0 1em 0; }
a { color: #0645ad; text-decoration: none; }
a:hover { text-decoration: underline; }
code { font-family: sans-serif; }
summary { font-weight: bold; cursor: pointer; }
details[open] { background: #970302; color: #dfdedd; }
.text-muted { color: #777; }
@media (prefers-color-scheme: dark) {
  a { color: #9e9eff; }
  body { background: transparent; color: #ddd; }
  .footer { border-top: 1px solid #444; background: #060606; }
  #logo { filter: invert(1) hue-rotate(180deg); }
  .text-muted { color: #888; }
}
</style>
<meta name="color-scheme" content="light dark">
<div class="content" role="main">
<a href="https://www.wikimedia.org"><img id="logo" src="https://www.wikimedia.org/static/images/wmf-logo.png" srcset="https://www.wikimedia.org/static/images/wmf-logo-2x.png 2x" alt="Wikimedia" width="135" height="101">
</a>
<div class="content-text">
<h1>Error</h1>

<p>Not Found</p>
</div>
</div>
<div class="footer"><p>If you report this error to the Wikimedia System Administrators, please include the details below.</p><p class="text-muted"><code>Request served via cp1100 cp1100, Varnish XID 848140588<br>Upstream caches: cp1100 int<br>Error: 404, Not Found at Sun, 06 Sep 2026 22:16:21 GMT<br><details><summary>Sensitive client information</summary>IP address: 187.15.139.71</details></code></p>
</div>
</html>
```


## [2026-09-06T22:16:37.313Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; for u in \"Reconstruction:Proto-Indo-European/krep-\" \"corpus%23Latin\" \"corset\" \"%E0%A4%B8%E0%A4%82%E0%A4%B8%E0%A5%8D%E0%A4%95%E0%A5%83%E0%A4%A4\" ; do echo \"=== $u\"; curl -s \"https://en.wiktionary.org/wiki/$u?action=raw\" | head -60; echo; done"
}
```


### [2026-09-06T22:16:40.167Z] TOOL RESULT

```
=== Reconstruction:Proto-Indo-European/krep-
{{also|Reconstruction:Proto-Indo-European/kerp-}}
{{reconstructed}}
==Proto-Indo-European==
{{etymon|ine-pro|id=body|pos=root}}

===Root===
{{ine-root}}<ref>{{R:gem:EDPG|head=*hrefiz-|page=244}}</ref>

# [[body]]

====Alternative reconstructions====
* {{alt|ine-pro|*ḱrep-}}<ref>{{R:itc:EDL|head=corpus, -oris|pages=137–138}}</ref>

====Derived terms====
{{rootsee}}

* {{l|ine-pro||*kérp-s ~ *kr̥p-é-s}}
** {{desc|cel-pro|*krixs|t=body}} {{see desc}}
** {{desc|iir-pro|*kŕ̥ps}}
*** {{desc|inc-pro|*kŕ̥ps}}
**** {{desc|sa|कृप्|tr=kṛ́p}}, {{l|sa|कृपा|tr=kṛpā́|pos=instr. sg.}}
*** {{desc|ira-pro|*kŕ̥pš}}
**** {{desc|ae|𐬐𐬆𐬵𐬭𐬞𐬇𐬨|pos=acc. sg.}}
**** {{desc|pal|tr=klp|ts=kirb|sc=Phlv}}
**** {{desc|xcl|կերպ|bor=1}}
* {{l|ine-pro||*krép-os ~ *krép-es-os}}
** {{desc|gem-pro|*hrefaz}} {{see desc}}
** {{desc|itc-pro|*korpos}} (The change in the stem vowel may be a conflation of the ''*s''-stem noun with the root noun {{m|ine-pro||*kérp-s ~ *kr̥p-é-s}})
*** {{desc|la|corpus}} {{see desc}}
* {{l|ine-pro||*krop-n̥-yo-}}<ref>{{R:xcl:Lidén:1906|pages=22–23}}</ref>
** {{desc|hyx-pro|-}}
*** {{desc|xcl|որովայն}}

; Unsorted formations:
* {{desc|sqj-pro|*krepa}}
** {{desc|sq|krep}}
* {{desc|sqj-pro|*kurpna}}
** {{desc|sq|kurm}}
* {{desc|unc=1|cel-pro|*krittā}} {{q|unlikely}} {{see desc}}

===References===
{{reflist}}
=== corpus%23Latin
{{also|Corpus}}
==English==
{{was wotd|2016|June|10}}

===Etymology===
{{root|en|ine-pro|*krep-}}
{{bor+|en|la|corpus||body}}. {{doublet|en|corpse|corps|riff#Etymology 2}}.

===Pronunciation===
* {{IPA|en|/ˈkɔːpəs/|a=RP}}
* {{IPA|en|/ˈkɔɹpəs/|a=GA}}
* {{audio|en|en-au-corpus.ogg|a=AU}}
* {{rhymes|en|ɔː(ɹ)pəs|s=2}}
* {{hyphenation|en|cor|pus}}

===Noun===
{{en-noun|corpora|+|corpusses|corpi<l:hypercorrect>}}

# A [[collection]] of [[written]] or [[spoken]] texts.
#* {{quote-journal|en|year=2011|author=Patrick Spedding; James Lambert|title=Fanny Hill, Lord Fanny, and the Myth of Metonymy|journal=Studies in Philology|volume=108|issue=1|page=113|text=No one suggests that Browning intended to mean vagina when he wrote “owls and bats, / Cowls and twats,” because the context does not allow for it, nor does the greater context of the Browning '''corpus'''.}}
## {{lb|en|specifically|linguistics}} Such a [[collection]] in form of an [[electronic]] [[database]] used for [[linguistic]] analyses.
##: {{syn|en|digital corpus|text corpus}}
##* {{quote-book|en|author=Mihail Mihailov; Hannu Tommola|chapter=Compiling Parallel Text Corpora: Towards Automation of Routine Procedures|editor=Wolfgang Teubert|title=Text Corpora and Multilingual Lexicography|series=Benjamins Current Topics|seriesvolume=8|location=Amsterdam|publisher=w:John Benjamins Publishing Company|year=2007|page=60|isbn=978-90-272-2238-1|passage=Text '''corpora''' are being used in most current lexicographic projects. Applied linguistic research is another field where text '''corpora''' are welcome as an inexhaustible source of empirical information, a polygon for testing various linguistic tools&nbsp;– spell-checkers, OCRs, machine translation systems, NLP systems, etc.}}
##* {{quote-book|en|author=Anabel Borja|chapter=Corpora for Translators in Spain. The CDJ-GITRAD Corpus and the GENITT Project.|editors=Gunilla [M.] Anderman; Margaret Rogers|title=Incorporating Corpora: The Linguist and the Translator|location=Clevedon, North Somerset|publisher=Multilingual Matters|year=2008|page=248|isbn=978-1-85359-986-6|passage=Comparable '''corpora''' are made up of texts in different languages that may be related in various ways, but are not translations of each other. They may have nothing in common at all, or be on the same subject, of the same genre, or from the same chronological period, etc.}}
##* {{quote-book|en|editors=Gerry Knowles; Briony Williams; L[ita] Taylor|chapter=Introduction|title=A Corpus of Formal British English Speech: The Lancaster/IBM Spoken English Corpus|location=Abingdon, Oxon.; New York, N.Y.|publisher=w:Routledge|year=2013|page=1|isbn=978-0-582-05639-8|passage=The Lancaster/IBM Spoken English '''Corpus''' began in September 1984 as part of a research project into the automatic assignment of intonation {{...}} The original design of the '''corpus''' was determined by the need to provide data for research into speech synthesis. As a result, unlike most other '''corpora''' currently being used in the computational linguistics field, the SEC exists in several forms. {{...}} However, whatever the original motivation for compiling a '''corpus''', it quickly becomes an object of interest in its own right. New users find it valuable for applications for which it was not designed.}}
#* {{quote-book|en|author=Giuseppina Balossi|chapter=Corpus Approaches to the Study of Language and Literature|title=A Corpus Linguistic Approach to Literary Language and Characterization: Virginia Woolf's The Waves|series=Linguistic Approaches to Literature|seriesvolume=18|location=Amsterdam|publisher=John Benjamins Publishing Company|year=2014|page=41|isbn=978-90-272-3407-0|passage=A '''corpus''' approach is a useful methodology for observing, describing and interpreting the stylistic features of language in literary and non-literary texts.}}
#* {{quote-journal|en|year=2018|author=James Lambert|title=A multitude of ‘lishes’: The nomenclature of hybridity|journal=English World-Wide|page=4
|url=https://www.researchgate.net/publication/318367113_A_multitude_of_lishes_The_nomenclature_of_hybridity
|text=Today, computer databases and '''corpora''' infinitely increase the ease of this type of research, but the collecting process remains essentially the same.}}
# {{lb|en|physics}} A [[structure]] of a special [[character]] or [[function]] in the animal body.
#: {{ux|en|the '''corpus''' of the uterus}}
# {{lb|en|uncommon}} A [[collection]] or [[body]] of [[object]]s with similar [[characteristic]]s.
#: {{syn|en|collection|Thesaurus:body}}
#* {{quote-book|en|author=Dimitǎr Draganov|chapter=New Coin Types of Hadrianopolis|editor=Ulrike Peter|title=Stephanos Nomismatikos: Edith Schönert-Geiss zum 65. Geburtstag|series=Griechisches Münzwerk|location=Berlin|publisher=w:Akademie Verlag|year=1998|page=221|isbn=3-05-003294-4|passage=About a hundred years ago in Germany, the publishing of '''corpuses''' of the ancient Greek coinages was started. {{...}} The significance of those, and some other '''corpuses''' is exclusive, because they allowed an enormous amount of numismatic material kept in museum and private collections all over the world, to be studied and systematized.}}
#* {{quote-book|en|author=Margaret Darling; Barbara Precious|chapter=Introduction|title=A Corpus of Roman Pottery from Lincoln|series=Lincoln Archaeological Studies|seriesvolume=6|location=Oxford|publisher=Oxbow Books|year=2014|page=1|isbn=978-1-84217-487-6|passage=An assessment in 1991 proposed publication of the results of this work in three stages: {{...}} secondly, a '''corpus''' of the Roman pottery to present the type series and to discuss the fabrics and forms recovered, {{...}}}}
# {{lb|en|archaic}} The [[body]] of a [[man]] or [[animal]].

====Usage notes====
* Of the plurals, ''corpora'' is the most common one.<ref>{{R:GNV|corpora,(corpuses*40),(corpusses*5000)}}</ref>

====Derived terms====
{{col|en|metacorpus|noncorpus|procorpus|subcorpus
|corpus callosum
|corpus cavernosum
|corpus delicti
|corpus language|corpus manager|corpus linguistics
|corpus luteum
|corpus spongiosum
|corpus striatum
|aligned parallel corpus|corpus cavernosum clitoridis|corpus cavernosum penis
|habeas corpus
}}

====Related terms====
{{rootsee|en|ine|krep}}

====Translations====
{{trans-top|linguistics: collection of writings}}
* Arabic: {{t|ar|مَتْن|m}}, {{t|ar|مَكْنَز لُغَوِيّ|m}}
* Belarusian: {{t|be|ко́рпус|m}}, {{t+|be|збор|m}}

=== corset
==English==
{{wp}}

===Etymology===
From {{inh|en|enm|corset}}, from {{der|en|fro|corset}}. Equivalent to {{suf|en|corse|-et|nocat=1}}.
[[Image:Corset Harpers Bezar1893f.gif|thumb|right|An 1893 corset, front and back.]]

===Pronunciation===
* {{IPA|en|/ˈkɔː(ɹ).sɪt/}}
*: Sometimes pronounced {{IPA|en|/kɔː(ɹ)ˈsɛt/}} (''nonstandard'') by revivalists.
* {{rhymes|en|ɔː(ɹ)sɪt|s=2}}
* {{audio|en|LL-Q1860 (eng)-I learned some phrases-corset.wav|a=UK}}

===Noun===
{{en-noun}}

# A [[woman]]'s [[foundation garment]], reinforced with [[stay]]s, that supports the [[waistline]], [[hip]]s and [[bust]].
#* {{RQ:Harper Lee Mockingbird|passage=Today was Sunday, and Aunt Alexandra was positively irritable on the Lord’s Day. I guess it was her Sunday '''corset'''.}}
# {{lb|en|historical}} A tight-fitting [[gown]] or [[basque]] worn by both men and women during the [[Middle Ages]].
# {{lb|en|UK|finance|historical}} A [[regulation]] that limited the [[growth]] of British banks' [[interest]]-bearing [[deposit]]s.

====Synonyms====
* {{l|en|stays}}, ''see also'' '''[[bodice]]''' ''and'' '''[[underbodice]]'''

====Derived terms====
{{col|en|diaper corset|anticorset|corsetery|corsetless|corsetlike|corsetmaker|corsetmaking|corsetwear|corseted|hourglass corset|neck corset|corset effect|corsetry}}

====Translations====
{{trans-top|woman's garment}}
* Arabic: {{t|ar|كورسيه|m}}
*: Hijazi Arabic: {{t|acw|كورساج|m|tr=kōrsāj}}, {{t|acw|مَشَد|m|tr=mašad}}
* Armenian: {{t+|hy|սեղմիրան}}
* Bulgarian: {{t|bg|корсе́т|m}}
* Catalan: {{t+|ca|cotilla|f}}
* Chinese:
*: Mandarin: {{t|cmn|緊身褡|tr=jǐnshēndā}}
* Cornish: {{t|kw|korset|m}}
* Czech: {{t|cs|korzet|m}}
* Danish: {{t+|da|korset|n}}, {{t|da|snørliv|n}}
* Dutch: {{t+|nl|korset|n}}, {{t+|nl|keurs|n}}
* Esperanto: {{t|eo|korseto}}
* Finnish: {{t+|fi|korsetti}}
* French: {{t+|fr|corset|m}}
* German: {{t+|de|Korsett|n}}, {{t|de|Schnürleib|m}}
* Greek: {{t+|el|κορσές|m}}
* Hebrew: {{t+|he|מחוך|m|tr=makhokh}}
* Hungarian: {{t+|hu|fűző}}
* Icelandic: {{t|is|lífstykki|n}}
* Ido: {{t+|io|korseto}}
* Italian: {{t+|it|corsetto|m}}
* Japanese: {{t+|ja|コルセット|tr=korusetto}}
* Korean: {{t|ko|코르셋}}
* Maranao: {{t|mrw|korsit}}
* Norwegian:
*: Bokmål: {{t|nb|korsett|n}}
*: Nynorsk: {{t|nn|korsett|n}}
* Persian: {{t+|fa|شکمبند|tr=šekamband}}, {{t+|fa|کرست|tr=korset}}
* Polish: {{t+|pl|gorset|m}}
* Portuguese: {{t+|pt|espartilho|m}}, {{t|pt|corset|m}}
* Romanian: {{t+|ro|corset|n}}

=== %E0%A4%B8%E0%A4%82%E0%A4%B8%E0%A5%8D%E0%A4%95%E0%A5%83%E0%A4%A4
{{also|संस्कृति}}
==Hindi==
{{wp|hi:+ भाषा}}
[[File:BhagavadGita-19th-century-Illustrated-Sanskrit-Chapter 1.20.21.jpg|thumb|'''संस्कृत''']]

===Etymology===
{{root|hi|inc-pro|*kar-}}
{{root|hi|iir-pro|*kar-}}
{{root|hi|ine-pro|*kʷer-}}
{{root|hi|sa|कृ}}
{{root|hi|sa|संस्कृ}}
{{lbor|hi|sa|संस्कृत|tr=saṃskṛtá|t=put together, refined}}.

===Pronunciation===
* {{hi-IPA}}
* {{audio|hi|Hi-संस्कृत.oga}}

===Adjective===
{{hi-adj|ind=1}}

# [[perfect]], [[refined]]

===Proper noun===
{{hi-proper noun|f|ur=سنسکرت}}

# {{tcl|hi|Sanskrit|id=Q11059}}
#: {{cot|hi|प्राकृत}}

====Declension====
{{hi-ndecl|<F.sg>}}

===References===
* {{R:hi:Dasa||4895}}
* {{R:hi:Chaturvedi||766}}
* {{R:hi:McGregor||970}}
* {{R:hi:Bahri||627}}

{{C|hi|Languages}}

==Marathi==

===Etymology===
{{root|mr|ine-pro|*kʷer-}}
{{lbor|mr|sa|संस्कृत|tr=saṃskṛtá|t=perfected, refined}}.

===Pronunciation===
* {{mr-IPA}}

===Proper noun===
{{mr-proper noun}}

# {{tcl|mr|Sanskrit|id=Q11059}}

===References===
* {{R:mr:Berntsen}}

{{topics|mr|Languages}}

==Nepali==
```


## [2026-09-06T22:16:52.967Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT 9535-9560\"; sed -n '9535,9560p' BRT.txt; echo; echo \"=== BRT 10630-10650\"; sed -n '10630,10650p' BRT.txt"
}
```


### [2026-09-06T22:16:53.031Z] TOOL RESULT

```
=== BRT 9535-9560
kahrp-  Noten
•  j.  k}r»la-  f.  'Schneiden,  Zerschneiden, Zerstören  (?).
KompE.  —  Zum  V.  kant-.  —  ai.  vgl.  k^lä- f.  -Spalt'.
•  j.  k^r^täe  Inf.  'zu  vollstrecken';  yJ nistayeiti  i'  sraoiyqm  "der  bestimmt  die Strafe  zu  vollstrecken"  Yt. /o,  log.
Zum  V.   'iar-;  vgl.  *'i:jnlay.. j.  '"kmtu  V.  /.  38:  E.  kant-  mit  No.  a.
•  g.  kar«dus-  n.  'Schutz,  Hilfe,  Beistand': hätqm  hvB  aojists  yakmSi  zavSng  jiinä °dusä  "der  Seienden  stärkster  ist  der, dem  ich  zu  Hilfe''  komme,  wenn  er  ruft" Y.2/;.3'>.
Vgl.  ai.  (hardii-  n.  *Schutz,  Schutzwehr',  got. siildus;  Bthl.  Slud.  3.  $8;  zuletzt  dazu  Ol- DENBEKG  ZDMG.  5S-  313.  Zur  DilTereaz  im Anlaut  vgl.  ai.  cAavi  'Fell',  gr.  enim,  got. skauda  und  gr.  cürg;,  lat.  cutis,  ahd.  hül.  — Pü. !  hai  asiän  äit  özöniandlar  kt  Ö  in  fa  j*J. nisn  raset  ä  karlärih  (Sü.:  karifti-e],  erl.!  ka\ x'äiitnd  ka  'kjr  u  karfak  kun''  kuntt.  — ')  Eig.  'mit  Hilfe'i  vgl.  RV.  /.  30.  7:  gämä  , nünäm  tti  'vasä  gegen  J.  9.  I :  a  nüridm  ,  . Xaatam  öiase.  —  ')  Vgl.  iSt.  BtHL.  AF.J.3S. MlLLsG.aiö  und  Dst.  ZA.  ^215  muten  uns  I grammatisch  unmÖ-;Ucbe  Dinge  tu.  |
•  j.  "iiarals  (sd.)  karaS^an"  N.(?7.  '
•  j.  karaÖTvan-  Adj.  'der  hütet,  bewahrt': , mihrlf  vlsps  mazdayasnaiiqm  .  .  iriawääi (sd.)  'wäU  Vt./0.  120.
Aus  ar.   "kj-t-uan-,  zum  got.  V.  halda».     Uii-
•  j.,  g.  kahrp-,  ksr?/-^'^  f.,  n.'>  'das  sieht- ' bare  Äussere  jedes  Wesens  und  Dings, , äussere  Erscheinung,  sichtbare  Gestalt': sraliiqm  at  tSt  'p/m  (AS.)  -^pam  (GP.)  j ävaedayamakl  tnazdä  ahurä  iinä  raota  . . avat  y.ll  hvarS  aväcT  Y._J(*'.  6;  — para avtiiriAe  hü  "^warstö  (sd.)  'pya  (LS.)  Y. ' /p.  8;  —  asmamm  ,  ,  y3  hislaite  ayanhs 'pa  (IS.)  x^amahe  (sd.)  ".  .  mit  der  Er- scheinung von.,  (sva. ..  anzusehen  wie..)'' YL  13.  2.  A)  insbes.  von  lebenden Wesen;  auch  vom  gestalteten  Stoff  selbst 'Leib,  Körper';  i )  von  Menschen  und Göttern:  aj  'psm  (GP.)  utayuitil  dadat ärmaitis  qnmä  (sd.)  Y.jo.  7;  — ■  yd>!a varsnahe  'palie^^  dsus  (sd.)  N.  7o(7;  — paiti  ainii  .  .  'p^m  .  .  gaia/ie  .  .  °ppm  .  . säJiar/  .  .  "Pim  .  .  abmatr/aAe  .  .  'P^m ..jahikayüi  ..  -p.m  Y.//.  30-32;  32;  — avqm  'P^m  yazamaide .  -yqtn . .  k^r^säspahe Yt /?.  61;  Az._J;  —  üjasat . .  viriisra-fitä ..vätahe  'pa  (IS.)  Vt/4-2;  —  mi%nm..
yaihe  vanuM  °fs  Yt/0, 60;  —  "pfm  srao- Iahe .  .yasamaide  'pftn  rasnaes . .  'p^m^*  . , Yt.  //,  21  f.;  —  paoiryä  dasa  xiapanJ  .  . listryB  .  .  'pf/n  rai'^wayeiti  .  .  nars  'pa (IS.)  panco-dasanhS  ".  .  formam  induit ,  , viri  forma  .  ."  Yt  Ä  13;  16,  iS;  — mae^imca  värimta  yä  ts  (näml.  Haomakt) 'piin  vaxlayats  V. /O-3;  —  vupimca  'ß (als  AS.)^'  ahurahe  mazdä  yazamaide  Y. 77.4;  — yat  dim  mazaos  (sd.)  °/J  türahe V.  13.  39;  —  pueril  zayante  tanuAshrpa 'pa  Yyt.i;  —  biDX'jqm  tnöi  firasaostrd ..dalddiit  "pJm  (AS.)'y.5/.  17;  —  upa.- iaht  ar?dvi .  .  kainlnB  'pa  srtraya  Yt 5.  64;  H.  2.  9;  —  yq/"  ■  ■  car.liii/iqm  'pa sralstqm  dildansa  H.  2.  10;  9,  YL5.  34, j/'.  11;  —  yeAAä  'pS  hurae'-aya  Yt  y. i9o(?);  —   'fimca   F.^jht?)^'.  a)    sva.
('Leichnam':  nDrfjtm  ..  upa  tarn  'ptm ' fratauharaitl  yqm  iristake  maiyeheV.^.x; ' — pqslö./ra'^a?»h»m  (sd.)  Al  kam?r?}.»m Ivinä^ay^n  ..  as.:^arft3maEiby3  ..*k3r»ß.- ifarqm  '/s  (als  Akk.)*'  paiti  nisirinuyJl \va\)qm  .  ,'^. 3.20;  —  yd  nar!  asaonö 1  iriri>usö  z»m  -pa  (statt  AS.)  nikainti  V. j.  40  PüZ.;  —  ma:dayasrta  aStsm  'pim hvarp-dansim  (sd.)  k?rjiiavqn  V.  5.  13; 14;  —  s.  noch  KompA.  a)  im  Gegen- satz zu  urvan-,  matiah-,  ifvTsl-:  ahurahe mazda  . .  yeähe  urfa  . .  "pas.'a  (NP.)  y3 ral^wayeiti  (sd.)  .  .  Yt  13.  81;  —  yö aSnatthaiti  nö  maiiS ,  .  nB  'p?m  Y.  9.  ag; —  frä  tS  'p»mca  imulmca  yao'zda'^äni V.3i,6;  —  ima  'pasca  tn-lsls:a  Vr.j/,3; Y.  55.  1.  3)    von   Tieren:  yal  barata
arjnm  mainyüm  /ramiUm  aspahe  'pa (IS.)  Yt;p.29;i¥.i8,zi,r4.9;  —  ahmli . . üjasat  vaztmnö  i'sri^raynS  uftrahe  'fa ■  Yt. /4- n;  P-J-i  —  nizbayemi  iistrtni  .  . \gius  'pa  Y.if}.3T,  Yt&i6,  74.7;  —  he I  'pa  varäzaie  Yt  ;^  1 5 ;  —  maiiahe  'pa  Yt |j4.23;  —  bUzahe  'pa  Yt  74.25;  —  yat dim  us;a  usdi'qnayat  .  .  '^raltaonS  m^?- yahe  -pa  kahrkäsahe  Yt.  J.  6 1 ;  —  m»rrjahe 'pa  vär^iiahe  Yt/4. 19,  /9.35;  —  zaf- nimnpitt  .  .  :^ar^n3  m^rjyahe  'pa  fra^usap Vt/'>.34.  Undeutlich:  ratufris  *n.liri- A-ayi  'pa  näij  payauhs  nSit  sun5  'pa payai?h5  ratufris  v>hrkaya  'pa'a  paya- uha^a  N.j()*',  [V,  7.  a:  lies  maxHJ!'^
KompA-,  E.  —  ai.  ;(■.'■/>,;  (IS.) 7),  Ta.y.karp,  arm. LW.  kop.  —  Vgl.  huk4i>>pta-  iind  irafstra-  No.«. —  I'ü. !  karp,  (zu  F.) :  karf  i  güsl;  Pü. ;  kaiet^ram.
db,Google
469  kwsß.x'^a^  —  k^mCiJ  a  470
iäyai,{7.aY.s&-  i'^'rim.  ?i.noch7.a6ui>irfi-.,^gs  pravrasyatt:   vispe  bavat  aiwi.vanyh
kiripmfa  lu  lesen  ist,  %2g4-  1  (doch  s.  :<';.*r-    "-'P-??-
^w«,  tihrfaifa).  —  »)  N.  /o5,  Y.  //.  4,  V.  ■  Eig.  etwa  'maeere  (d.  i.  geringe)  Ausdauer 3  20  5  I3f  ■  s  No  4  —  Jl  Them  •  Pö  5  bei  ■  besitzend'») —  O  Nach  der  o-Dekl. —  >)  Falsch t-arhia:    —    4)  Der  Gebrauch  von  i^ri/i   als       J"ST1  NB.  16a.
A^^-  ?■  ^w  ^  T'  ^'  ^°i, '"/"'"'  ""■  J'"^^"''' '  •  J-  kui^sänay-  m.  EN.  eines  von  Haoma
dass   das  Wort  fem.  und  ntr.  war;    doch  s.  ■*  ..               ,   '            ,           .     ,        _  .
S  381.  —  s)  S.  No.  1.  —  *)  In  DsT.s  Über-  gestürzten,  den  mazrfavajwischen  Pnestern
Setzung,  Z.\.  ^,  118  wird  kihrf  ausgelassen,  feindgesinnten  Fürsten":  haomS  l>mcit yim
-~    n    Nur  in  dieser  Form;    sie  ist  auch  im  'säfrim  apa.xsai:rfmi%A.)nisähayat^'g.^^.
Aw.  die  häufigste.  »j    y>si.    ZA.  2.  93    meint:     "K.    reprisente

=== BRT 10630-10650
Superl.  lu  •jrroSToan/-  0  (aus  ar.  *kratiianl-  aus *ktatuigaiit-  ■>)  nach  Wörtern  wie  madila-, bairijla-  :  moianf-,  AaranI-  i  s.  noch  xnAuvmna: —  Pü. :  srailklum,  erl. :  dänätlum.  —  0  Vgl, asjrraiiaaiama:  Zur  arischen  Reduktion  von ^»  in  *)  {=  Aw.  %w)  s.  ZDMG.  jo.  690. Enlsprechena  auch  in  j.  aitupsAtaaißai.  Falsch BB.  //.  341.    .
•  g.  xrap-  V.,  nur  mit  atbi  'angelegen sein'.     Praes.  2  xrafa-.
'Jemandem  (Abi.)  angelegen  sein,  sein Anliegen  (Sehnen,  Hoffen)  bilden':  ahü (sd.,  Sp.  3  o.)  at  paiti  adähü  tnazää  akurä masdqmtä  bSiricä  kar^svä  räitl  tot  xra- paiti  ahmat  hyat  aib[  hyat  mliditn  *mavai- iim  (sd.)  . .  "bei  diesen  Heimzahlungen jetzt,  o  MAh.,  gedenk  dessen  und  erfülle es,  was  unser  Anliegen  bildet,  durch  deine Gewährung  des  Lohns,  den.."  Y.  40.1".
Vgl.  gr.  jipj'jiiij?  —  lü,:  Tai  Im  S  e  i  lö  jra/ fänaiih'l  -  ö  diu  -  hai  Sil  kam  apar  -  tarn newaiih  hai  an;  Sü.:  dakfinlbhmiämi  tava buddhiroksäyai.  —  ')  S.  noch  Y,  _JJ.  5 :  kuxsa- %rSJjmiii  (sd.)  .  .  xic&nm  ahmai  kyai  ailii dadimahifä  .  .,  wo  eine  Ellipse  vorliegt.  — *l  I>ST.  ZA. /.  171  übersetzt  danach:  "faisant UMralit^  ä  ta  JRiligion],  proieclrice  de  l'Inlel-
ligence",  und  meint:  xrapaiti  serait  donc  xta- iupaill  {. .  paili  ctant  pa-ä  ^  pi-ti)",
•  j.,  g.  xrafstra-  n.  i)  im  gAw.  'wildes Tier,  Raubtier":  atibyS  mas  äsä  syasdat (sd.)  yentat  ahmat  aurunä  'rH  (AP.)  Y. $4.  9.  a)  im  Plur.  als  Bezeichnung  für die  nicht  sesshaften  Religionsfeinde  und deren  Gölter,  sva.  'Raubgesindel':  anä mq'ira  maxist?in  väurüimaidl  (sd.)  Tä (A'P.)  hizvä  Y.  28.5;  —  pari  *vä  vJspäis pars  vaox?mä  dalviliscil  °räis  maSyäis^ä "losgesagt  haben  wir.  uns  von  allen  Xraf- stra^ (allem  Raubgesindel),  den  Daivas wie  den  Menschen"  "  Y.34. 5 ;  verwendet  Y. ig.  2.  2)  im  jAw,  Bezeichnung  fUr  alle schädlichen  ((/iZÄischen)  Tiere,  bes.  der niederen";  paitUtätie  a/astaca  zBüdiftaca apayantamaheca  a?prahe  mainyius  °ra Yt  21.1;  —  duye  Saite  kahyäcit  ar>rö.- mainyavanqm  "ranqm  ava.janyäl  V.  16. 12;  —  ähva  vyar?hähva  (sd.)  e^mB  'ra ham.bavainti  yim  tnasyäka  spis(sd.  tiqma aojaitt  V.  z/. 3;  —  *maxSiMhrpa  ..*akara- tum-driwyi  (sd.)  ya%a  taehdistäiS  'räis V.  7.  2;  —  Y.  ig.  2:  s.  unter  1.
KompA.  —  El.?J)  —  Pü.  (zu  1);  xral  slarl*), Sü.  1  buddhija4a^,  buddhinaslah,  (zu  Y.  34.  g): ksudrajantui,  erl,:  duflasv.ipadai  pärvaliyah; (lu  l)  xta/sir  (Transskr.).  "  ')  daäiäücä  . . mafyäiirä  sind  attributiv  gedacht.  —  'i  Wie solche  hundertweis  zu  erschlagen  als  verdienst- liches Werk  gilt;  s.  auch  j-rn/j/riJf a«-.  —  31  Die Zerlegung  in  V™/-(s.  i/r>/-)-t*s/ra-  (zum  ai. V.  arfmi)  ist  wenigstens  denkbar;  ^40,1//. — *)  Vgl.  dazu  DsT.  ZA.  r.  208:  "il  ne  serail pas  imposstble  que  ceUe  etymologie  füt  exacte et  quo  ihrajsira  soit  pour  khral\ii)stara,  d'oü "khtalkslaia,  *k/ira/slara".
•  j.  xrafstra-gan-  m.  'Xraßiratmt-^,  ein Werkzeug  zum  Töten  kleinerer  schädlicher Tiere"';  °lrain>m  *ainim  baraili  V.l^.z; —  yalsam  sayanam  d^aurune..''trayngm (statt  NS.)  V./4-8.
•)  Im  Mp.  mar  gan  'Schlangentöter'  genannt ; es  ist  ein  Stock  mit  einem  I.edcrriemen  am Ende;  s.  Bd.  28.  21,  Hauo  Essays'  365,  DsT. ZA.  3-  S'-
Pii. :  xra/slr  gan  (transskr.),  erl. :  mär  gan,  s.  *).
-  ■)  S.  dam  Hbm.  KZ.  36.   175. j.  xrayäatr'a  N.  6/:  lies  xar'.
•  j.  y5  vanhpnti  .  .  paiti. vatikqsca  "xra.- uru.baouriSfii  N.^/.
Pü.:  .i-fli-O  bariinn.  —  ')  D.i.  'Esel',  für  *jv.
—  =)  Für  baouiü.
•  j.  xrlohaya-  den.  Praes.  31,  nur  mit \fra  'erschüttern'.
dby  Google
539  xru-   -
Med.  (in  pass.  Sinn)  'erschüttert  werden,
ins  Schwanken  geraten':   Jra    maifiyamm
xr3rphayete  spüoaAe  xrvJsyantoAe  Yt.JO.56.
Ableit.   aus  »xräa/ia-  m.,    lu    einer  Basis  ar.
```


## [2026-09-06T22:17:08.228Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://iranicaonline.org/articles/xrafstra",
 "prompt": "What is the etymology of Avestan xrafstra-? Does it derive from kəhrp- 'body' + a root meaning 'eat' ('body-eater')? Give the details and the Pahlavi/New Persian descendants (xrafstar, xarafstar)."
}
```


## [2026-09-06T22:17:09.959Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN corpse/corset\"; grep -n -i \"corset\" KLN_1966.txt | head -10; echo \"---\"; grep -n -i \"corse, n\\|corpse\" KLN_1966.txt | head -10"
}
```


### [2026-09-06T22:17:10.023Z] TOOL RESULT

```
=== KLN corpse/corset
5941:business,  n.  —  Formed  fr.  busy  with  suff.  -ness, busk,  n.,  strip  of  steel,  formerly  of  whalebone, placed  in  front  of  a  corset.  —  F.  busc,  fr.  It. busco,  lit.  ‘a  stick  of  wood’,  which  is  of  Teut. origin.  Cp.  OHG.  busc,  ‘bush’,  and  see  bush, ‘shrub’.
9298:corsage,  n.  —  F.,  formed  with  suff.  -age  fr.  OF. cors  (F.  corps),  ‘body’.  See  corps  and  cp.  corse, corset.
9300:corse,  n.  (poet.)  —  A  var.  of  corpse, corselet,  corslet,  n.,  armor  for  the  body.  —  F. corselet,  lit.,  ‘little  body’,  dimin.  of  OF.  corj(F. corps),  ‘body’.  See  corps  and  cp.  next  word, corset,  n.,  a  close-fitting  undergarment;  stays.  — F.  corset,  lit.  ‘a  little  body’,  dimin.  of  OF.  cors  (F. corps),  fr.  L.  corpus,  ‘body’.  See  corpus  and  -et and  cp,  corps.
9301:Derivatives:  corset,  tr.  v.,  corset-ing,  n.,  corset- ry,  n.
36668:stay,  n.,  support;  pi.,  a  corset.  —  MF.  estate.  See prec.  word.
---
6066:cadaver,  n.,  a  dead  body,  a  corpse.  —  L.,  ‘a  dead body,  a  corpse’,  fr.  cadere,  ‘to  fall’;  see  cadence. For  sense  development  cp.  Gk.  7rxo>p.x,  ‘corpse’, which  is  rel.  to  — (ttxgiv,  ‘to  fall’  (perf.  rre7xx<oxx).
6067:and  Heb.  nlbheldh,  ‘carcass,  corpse’,  fr.  ndbhel, ‘it  decayed,  withered’,  which  is  rel.  to  ndphdl, ‘he  fell’.  Cp.  ptomaine.
6068:Derivatives:  cadav-er-ic,  adj.,  cadaverous  (q.v.) cadaverous,  adj.,  looking  like  a  corpse;  pale.  — L.  cadaverdsus,  ‘corpselike’,  fr.  cadaver,  ‘a  dead body,  corpse’.  See  cadaver  and  -ous. Derivatives:  cadaverous-ly,  adv.,  cadaverous¬ ness,  n.
9252:—  F.,  fr.  L.  corpus.  See  corpus  and  cp.  corpse and  corse.
9253:corpse,  n.  —  ME.  corse,  corps,  ‘body’,  fr.  OF. cars,  fr.  L.  corpus.  See  prec.  word.  The  MF.  and modern  F.  spelling  corps  is  due  to  the  influence of  L.  corpus.
9254:corpulence,  corpulency,  n.,  fatness.  —  L.  corpu- lentia,  ‘grossness  or  fleshiness  of  body’,  fr.  cor- pulentus.  See  next  word  and  -ce,  resp.  -cy. corpulent,  adj.,  fat.  —  F.,  fr.  L.  corpulentus, ‘fleshy,  fat,  stout’.  See  corpus  and  -ulent. Derivatives:  corpulent-ly ,  adv.,  corpulent-ness, n. corpus,  n„  body.  —  L.  corpus,  gen.  corporis, ‘body’,  prob.  cogn.  with  OI.  kfp-,  ‘form,  beauty’, Avestic  klrlfsh,  gen.  k6hrpd-,  ’form,  body’,  OE. hrif,  OHG.  href,  ‘womb,  belly,  abdomen’,  OFris. hrif  href,  ‘belly’;  prob.  fr.  I.-E.  base  *qwrep-, *q”rp-,  enlargement  of  *qwer-,  ‘to  make,  form’, whence  OI.  krnfiti,  karSti,  ‘makes’,  Avestic  kar-, ‘to  make’,  k*rfnaoiti,  ‘makes’,  OPers.  kar-,  ‘to make’,  kara-,  ‘maker’,  Lith.  kuriu,  kurti,  ‘to build’,  OPruss.  kura,  ‘he  built’,  Olr.  crulh, ‘figure,  shape’,  W.  pryd,  ‘appearance,  look'.  Cp. corporal,  corporate,  corporation,  corporeal,  cor¬ poreity,  corposant,  corps,  corpse,  corpulent, corse,  incorporate.  Cp.  also  Sanskrit  and  words there  referred  to.  Cp.  also  the  second  element  in midriff.
9300:corse,  n.  (poet.)  —  A  var.  of  corpse, corselet,  corslet,  n.,  armor  for  the  body.  —  F. corselet,  lit.,  ‘little  body’,  dimin.  of  OF.  corj(F. corps),  ‘body’.  See  corps  and  cp.  next  word, corset,  n.,  a  close-fitting  undergarment;  stays.  — F.  corset,  lit.  ‘a  little  body’,  dimin.  of  OF.  cors  (F. corps),  fr.  L.  corpus,  ‘body’.  See  corpus  and  -et and  cp,  corps.
9632:crematory,  adj.  —  ModL.  crematorius,  ‘pertai¬ ning  to  cremation’,  fr.  L.  crematus,  pp.  of  cre¬ mare.  See  cremate  and  adj.  suff.  -ory. crematory,  n.  —  ModL.  crematorium,  ‘a  place for  burning  corpses’,  fr.  L.  crematus,  pp.  of  ere- mare.  See  cremate  and  subst.  suff.  -ory. crembalum,  n.,  a  jew’s  harp.  —  ModL.,  fr.  Gk. xpspjiaXov,  ‘castanet’.  See  crepitate, cremnophobia,  n.,  a  morbid  fear  of  precipices ( med .)  —  Medical  L.,  compounded  of  Gk. xprjp.vog,  ‘an  overhanging  bank,  precipice,  cliff, crag’,  and  -cpojBtx,  ‘fear  of’,  fr.  <p6(3os,  ‘fear’.  The first  element  is  rel.  to  Gk.  x.pr(uvr(u,!.,  ‘I  hang  up, suspend’ ;  see  cremaster.  For  the  second  element see  -phobia.
10407:Derivatives:  the  hybrid  words  deacon-ess,  n., deacon-hood,  n.,  deacon-ry,  n.,  deacon-ship,  n. dead,  adj.  —  ME.  dede,  deade,  deed,  fr.  OE.  dead, ‘dead’,  rel.  to  OS.  dod,  Dan.  dad,  Swed.  dod, OFris.  dad,  MDu.  doot,  Du.  dood,  OHG.  tot, tod,  MHG.  tot,  G.  tot,  ON.  daudr,  Goth,  daups, ‘dead’,  fr.  Teut.  participial  base  *dau-pa,  *dau- da,  ‘dead’,  formed  with  participial  suff.  -pa,  -da (=  I.-E.  suff.  -*to),  fr.  Teut.  base  *dau-,  ‘to  die’, which  corresponds  to  I.-E.  base  *dhew-,  *dheu-, *dhow-,  *dhou-,  ‘to  pine  away,  die’.  Fr.  * dhwei - an  enlargement  of  this  base,  derive  Arm.  di, ‘dead  body,  corpse’,  OIr.  t lith,  ‘end,  death’, OSlav.  daviti,  Russ,  davit’,  ‘to  choke,  suffocate’. Cp.  death,  die,  dwindle.  Cp.  also  funeral.  For the  formation  of  Teut.  adjectives  from  past participles  cp.  cold,  loud,  old,  sad.
12496:Derivatives:  dwell,  n.,  dwell-er,  n.,  dwell-ing,  n. dwindle,  intr.  v.  —  Dimin.  of  next  word.  The verb  dwindle  was  first  used  by  Shakespeare, dwine,  intr.  v„  to  waste  away  ( archaic  and  dial. Brit.)  —  ME.  dwinen,  fr.  OE.  dwinan,  ‘to  lan¬ guish,  waste  away,  vanish’,  rel.  to  ON.  dvina, MDu.  dvinen,  Dan.  tvine,  of  s.m.,  Du.  verdwij- nen,  ‘to  waste  away,  vanish’,  and  cogn.  with Arm.  di,  ‘dead  body,  corpse’,  OIr.  dith,  ‘end, death’;  fr.  I.-E.  nase  *dhwei-,  enlargement  of base  *dhew-,  *dheu-,  ‘to  pine  away,  die’,  whence Goth,  diwans,  ‘mortal’,  and,  with  vowel  grad¬ ation,  OS.  doian,  ON.  deyja,  ‘to  die’.  Goth. daups,  ‘dead’.  See  dead  and  cp.  prec.  word. Derivative:  dwindl-er,  n.
```


### [2026-09-06T22:17:10.154Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-06T22:17:24.073Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SNS xrafstar\"; grep -n -i \"xrafstar\\|xrafstr\\|xistar\\|xarafstar\" SNS.txt SNS_pages.txt | head -20; echo \"=== SNS 40 leaf\"; grep -n \"pdf page\" SNS_pages.txt | head -3"
}
```


### [2026-09-06T22:17:24.131Z] TOOL RESULT

```
=== SNS xrafstar
SNS.txt:3952:.^^l^. rf ^O^W.>-*'J^> :xrafstar: W* 
SNS.txt:3953:(Wir. Wan. firystrs jl* &*>. 538) xrafstra-:fc- 
SNS.txt:3958:If/lM [**!*)**« xrafstaran: ^oV 
SNS.txt:3959:^T^ :xrafstar I ablg: >W* ^*"*~ 
SNS.txt:4198:(•j's o*** : ^) xrafstarSn: ^^«*»oV-»^Uv \?\>oa»4j i-U> 
SNS.txt:11574:jfr!*il**il :surak I xrafstaran: ^^t>- - 3^ v 
SNS.txt:29704:xrafstra- 40/10 
SNS.txt:30705:xrafstar 40/9 
SNS.txt:30707:xrafstaran 40/13-44/16 
SNS.txt:30709:xrafstar I ablg 40/14 
SNS_pages.txt:2375:           ijtfj^Ajj    Ly.ai.^Ajy 'JjjjitfUjt :ard3y            fravard: ^OPo-**"                         .^^l^. ^O^W.>-*'J^> :xrafstar:
SNS_pages.txt:2380:                                                                                                                                                                    xrafstra-:fc-
SNS_pages.txt:2391:                                                                                                               [**!*)**« xrafstaran:
SNS_pages.txt:2394:                                  .>£*• .^.Iki .jtJjjl :art§star:                 L^u^                   ^T^ :xrafstar I ablg: >W* ^*"*~
SNS_pages.txt:2576:                                                                                                                                                                     ^) xrafstarSn:                                     ^^«*»oV-»^Uv \?\>oa»4j i-U>
SNS_pages.txt:7980:                                                                             jfr!*il**il :surak I xrafstaran:
SNS_pages.txt:15299:                                                              xrafstra- 40/10          x v 30ra- 59/6
SNS_pages.txt:15688:xrafstar 40/9            xvastag 58/3                        x v as -101/2              yast I n3var 315/2
SNS_pages.txt:15689:xrafstaran 40/13-44/16   xvastan 111/8                       x v astar 101/4            yast I vlrastag 28
SNS_pages.txt:15690:xrafstar I ablg 40/14    x vad 106/12                        x vSdflgdah 78/8           yast jamag 316/13
=== SNS 40 leaf
```


## [2026-09-06T22:17:25.518Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9240,9260p' KLN_1966.txt | grep -o \"^[0-9]*\" | head; echo \"--- search page markers near\"; awk 'NR>9200 && NR<9320' KLN_1966.txt | grep -n \"^\\s*3[45][0-9]\\s*$\" | head"
}
```


### [2026-09-06T22:17:27.405Z] TOOL RESULT

```
--- search page markers near
64:357
```


## [2026-09-06T22:17:33.237Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3945,3965p' SNS.txt; echo \"=== KLN page markers\"; awk 'NR>9100 && NR<9310 {if ($0 ~ /^[0-9]{3}$/) print NR\": \"$0}' KLN_1966.txt | head"
}
```


### [2026-09-06T22:17:35.143Z] TOOL RESULT

```
■ TY/1Y^ -('j***) 5raet :{, 
.H/VT^ *T*-i-:sn&sag arSySd: ^(X **W 

(^^■^) WciWwh*l»-*Ht cahar:>*'LB J :^>- 
catasrah, cattirah, catvarah: ^d^- caQwar- :fc- 
UM**T/f4 -T/V^ ./^^; 5ihar: V W* W 577) 

.^^l^. rf ^O^W.>-*'J^> :xrafstar: W* 
(Wir. Wan. firystrs jl* &*>. 538) xrafstra-:fc- 
/W$ \\/kS*r\tt<S >(*+*») xarwastar : LI, 45) 

lA-4/To ^ . H 

If/lM [**!*)**« xrafstaran: ^oV 
^T^ :xrafstar I ablg: >W* ^*"*~ 

.Jie 'J> : xrad: y»i« 

GUW»,535) xrat^S^j/ kratav-: ^j^ xratu- ife 

Uttn^a: oit. Han. p. 50.)gira-, grata: ^u* 
=== KLN page markers
9133: 350
9152: 351
9176: 352
9264: 357
```


## [2026-09-06T22:17:42.839Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"خرفستر\" \"خستر\" \"کرست\" \"سنسکریت\" \"نقره\" \"وچر\" \"ناگزیر\"; do echo \"=== $w\"; grep -c \"$w\" MON_part1.txt MON_part2.txt 2>/dev/null; done"
}
```


### [2026-09-06T22:17:44.666Z] TOOL RESULT

```
=== خرفستر
MON_part2.txt:0
MON_part1.txt:0
=== خستر
MON_part2.txt:0
MON_part1.txt:1
=== کرست
MON_part2.txt:5
MON_part1.txt:0
=== سنسکریت
MON_part2.txt:0
MON_part1.txt:0
=== نقره
MON_part1.txt:77
MON_part2.txt:81
=== وچر
MON_part1.txt:8
MON_part2.txt:4
=== ناگزیر
MON_part2.txt:6
MON_part1.txt:2
```


## [2026-09-06T22:17:47.098Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== کرست MON_part2\"; grep -n \"کرست\" MON_part2.txt | head -6; echo; echo \"=== وچر MON_part1\"; grep -n \"وچر\" MON_part1.txt | head -8"
}
```


### [2026-09-06T22:17:47.164Z] TOOL RESULT

```
=== کرست MON_part2
5126:می‌دارند با به جوراب يا کرست و با پستان‌ها 
21942:کرست: ۱ (.) سینه بند و شکم بند 
21944:کرستون: [(- قرسطون. معر.] (.) 
32776:کستم |( کت کسلت) بق هت کرستگا: 
35318:می‌نامیدند ( کرستسن. ایران در زمان 

=== وچر MON_part1
11257:و میدانی» دوچرخه‌سواری» شنا و اسکی 
11259:دوچرخه‌سواری دو نوع استارت است: 
12239:دوچرخه سواری» دو و میدانی» اسکی؛ شنا» 
16413:دوچرخه‌سواری» سوارکاری» اسکی؛ 
28121:جلو رفتن در شناء دوچرخه سواری و غیره. 
29621:دوچرخه. (سه.) زبانةٌ کوچکی است که در 
50617:چشم وچراع: (-.60۲) 0-62۲ (امر.) 
63498:دوچرحه: (0-)10-272 (امر .) دستگاهی
```


## [2026-09-06T22:17:53.177Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '21935,21950p' MON_part2.txt"
}
```


### [2026-09-06T22:17:53.243Z] TOOL RESULT

```
خم» چین و شکن (موی» جامه و غیره). 
۱ کر سان: 2 |[ کارسان] (امر.) طرفی 
مدور و صندوق مانند که از گل با چوب 
سازند و نان و حلواو مبوه و مانند آن در آن 
کر سان: 0 (هند. کر سان» کسان؛ سنس. 
کرشمان] (زراعت) (ص‌فا..) کشاورز» 
فلاح. 
کرست: ۱ (.) سینه بند و شکم بند 
زنان. 
کرستون: [(- قرسطون. معر.] (.) 
ترازوی بزرگك. 
۱ کررسی: آهت۲0 (ع.] (ا.) سر یر» نخت. حرف 
سخن) خود ره کرسی نشاندن: (عم 
سخن خود را تحمیل کردن. صندلی؛ ج 
(ع.) کراسی. (جف) حاکمنشین»مرکز نس 
(نو.) (دانشگاهی) درس تحصصی یک
```


## [2026-09-06T22:17:53.712Z] TOOL CALL #44: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:2157 2>&1 | head -40"
}
```


### [2026-09-06T22:17:59.724Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 240; check the printed number and re-run with --pdf-page if off)
REF: BQT:2157  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 240  OCR-lang: fas

-۷و۱- قره
کرنا راکوبند ۱ - و بمعنی فریاد همهست ۴ | تختانی » حکم وفرمانی باش د که سلاین و حکام
- وعربان گریز راکوبند که از کربختن‌است ۴. | بجهت جمع شدن و کرد آمدن سپاء ار الشکن
نفیر نامه « بفتح اول و کسرئانی‌وسکون | می لوسند (۱).
بیان شا نزدهم
درنون با قاف مشتمل برسی وسه لغت و کنایت
نقاب خضر] - کنابه از آسسان بهر دو معنی آمده است 8 .
است ۴ . نقد شش روده * - کنایه ازدیا
نقاب یی - کنایه از شب است که و مافیها است ۴ .
بعربی لیل کویند ۴ . نقد گیر ان ۱ «کنایه ازمردمانی باشد
نند جان ه کنایه از جان است که | که رشوت میگیرند ورشوت میشوراد - وطالبان
روح باشد - وزر وسیم سره رایج را نیز گفته‌اند. دیا را نیز گوبند ۴ .
نقد روآن - بسسنی‌نقب جان است که ره - بنم اول, معروف است که بعربی
کنایه از جان - و زر وسیم رایج باشد چه روان | فنه‌کوبند ۷ - وکنایه ازهرچیز سفید هم‌هت

69 چش : لوسند . :

۹ - شکل فدیمترآن « بپور» . کردی 881۳2 (شیپور) « ژابا ص 8۲۲ > » معرب نفینر
« دزی ج ۲ ص ۷۰۰ >. مجازاً فضمی ازکرنا که بیخترفلندران دارند وبآن ۶ شاخ نفیر» و «بوق
نفیر» هم کوبند « فرهنگه نظام >.- درموسیقی نام آوازیست ازدستگاه همایون «فرهنگه نظام».

۴ - نه من کردم از دست جورت لفیر ‏ که خلفی ز خلفی یکی کشت هکیر :

َ سعدی 2 فرهنگه نظام ؟ .
و ر4 : تذ کرتالاولیاه چاپ آرویا ج ۱ ص۲۱۱ ی‌ه. ۴ - (عر) ۵ لفیرکامیر » گروه هردم
ازسه تا ده - وفومی که بکاری‌پیش روند وبا کسی گريزند یاازهم کر‌يزند درجنگه.*«مننهی‌الارب».

۴ - رك : رشیدی . * - رك : روان . ‎٩‏ - جمع « نقدگیر» ( از: نقد
(عر) + گیرل کیرنده] ).

۷ - درسندی 8*۴۲ (سیم) ر4 : 60۳۵۳۳۵۱۲6 6ل [3۶92 ,01916 8.860۷6
5 .۱929,0 قله۳ 02706۰ 2۵906 5084016006۰ وآن مر کیت از*8 (۱ه نا) ملد
11۹ (کرده)؛ و مراد نامکوك اآست (از افادات شفاهی استاد بنویست) . درعریی همانی‌متعدد
دارد از جمله « القطمة‌المذابة من‌الذهب والفضة » وفی‌الاساسی ( من‌الفسة ) .> «اقرب‌الموارد » ولی
بمعنی‌سیم وسیم درمعدن متحدث است «دزی ج۲ ص۱۰ فلزی قیمتی‌سپید رنگه ده ازجهت
ارزش پی از زر (طلا) قرار دارد :
```


## [2026-09-06T22:18:31.092Z] TOOL CALL #45: Bash

```json
{
 "command": "for p in 1778 1809 1814; do echo \"############ BQT:$p\"; python3 tools/ref_page.py BQT:$p 2>&1 | head -30; done"
}
```


### [2026-09-06T22:18:46.031Z] TOOL RESULT

```
############ BQT:1778
REF: BQT:1778  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 575  OCR-lang: fas

بیان هشتم
در کاف فارسی با ذال نقطه دار مشتمل بر پنج لغت
عد اردن < چم اول بروزن شماردن, "گذشت ‎٩‏ - جنم‌اول‌وفتح ثانی‌وسکون
بمعنی گذاشتن باغد۱ - وبمعنی اداکردن ۳ - | شین نقطه دار وفوفانی » ماضی گذشتن باشدبچند
وحبا(۱) نمودن پمنی‌پیش کش کردن هم هست- | معنی - وبمعنی عبرهم هت یمنی عبور کردواز
ویمعنی گذرانیدن هم آمده است بچادممنی؟۴ ۰ ارو وی ریا است که
۰ ۰ ق گوشند - و ماضی بیش افتادن
گذادرش؟ - بنم اول وکر رابع بمربی ربق ای ی ۳
5 هت بمنی پیش افتاد - وماضی گذشتن بمعنی
وسکون شین نقطه دار»بمعنی گذشتن وترذدادن- 8 : .2 ۱
5 ترك دادن هم آمده است که از ترك و تجرید
وادا نمودن ‎٩‏ - وگذرانیدن بچند همنی باشد. ی ۱
ناش ۹ : باشد - وتجاوز از کناه وتقصیر را ی ز گوندمنی
سین - باشن‌وتای قرشتبروزن | ویگر این‌کار نمیکند » وعآل این دومعنی یکی
ومعنی گذاردن‌است که‌بهادن ‎٩‏ - وادا کردن۷٩‏ است چه هردو را غرض ترك دادن باشد-وبمعنی
وحبا نمودن - وکنرانیدن بجند آهمنی باشد ۰ بعد هم هت چنالکه گوبند «از گذشت آن»بمنی
گذر نامه < جم اول » خطجواز باشد بعد از آن واز بعد آن *۹- ودر مقام غیر وجز
پستی نوشته‌ای که مسافرانرا دهند تا از کذربابان م استعمال: میشود - وکنایه ازقطع شدن نفس
وراه داران وامثالآها کی مانع ابشان‌شود ۸ ۰ | آخرین آدمیزاد است ۰
(۱) خم ۱ : جیا - ۱
۹ - راد :گذاعتن ۰ ۳ ‌ باین‌معنی گزراردن» (ه.م.) ات ۰
۴ < گذاعتن » پهلوی ۰۷1127۲180 ارمنی ع۰۷12۳ هندی باستان 7 «اسشق
۴۳ » اوستا ۷1-1۸7 «بارتولمه ۹4۰ «لیبر کس ۲4۹ در فارسی بمعئی متمدیآمده . یعنی
عور دادن : نیزه گذار.رك : هوبشمان یرک ی ره ار - آسم مصدر ازه گذاردن 6 (ه.م.).
یو باین‌ممنی* گزارش»( م.( است. ۹ گذاردن ۰ - رد : گزاردن ۰
۸ - همه دباات ودین ورز و تيك رائی کن
که سوی خلد برین باغدت گذر نامه .
۰ شهید بلخی « لغت فرص ۸۵۵۳ ۰
############ BQT:1809
(no exact page map; using offset -1205 -> pdf page 604; check the printed number and re-run with --pdf-page if off)
REF: BQT:1809  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 604  OCR-lang: fas

۱۸۰۷ کربوه
کشیده و بفین نقطه‌دار زده » بمعنی گریز است گریودوم ؟ - بنتح اول و ثانی
که ا زکربختن باشد . بتحتانی رسیده و بواو زده وضم دال و سکون‌واو
گریفتن ۱ - بافا . بر وزن و معنی ومیم » بمعنی خیانت باشد و آن ودیمت‌راخیات
گربختن است (۱) کردن و آنکار نمودن است .
بسن است ۰ گربون * م۱ ی ۰
۳ ۰ « قح اول بروزن پریزن»
گریگاه ؟ - بکس اول . در دیگه علتی است که آترا بپندی داد و بعربی قوبا
بربان پلاوجاییر! گوبند که‌محاذی کردن گوسفند گوبند ‎..٩‏
‏ن باشد #۰
بربان باشد از.۲ گریوه ۷ - بفتح اول و رابع » کوه
گریواده < با ثالك مجهول و واد | پت و پشتهٌ بلند را کوبند - و یکسر اول هم
و زای هوز بروزن دلیرانه » بمعنی هار است که | آمدهء است ۸ - و زمین بلند وپشتةٌ خا کیرالیز
مروارید ولمل وامثال آن باشد که بررشته کشیده | کوبند که باران آنرا رخنه کرده بزیر آهده
باشند . باشد. ۶

(۷) چش : باشد -

۱-اظ . مسحف « کریختن » با «کریفتن > ر4 :کریشتن ‎ .‏ .

۲ - رك :کری . ۴ - محیح برای مهمله است » مرک از: کری( کردن) +
واره (پوند نبت واتصاف) [رك .۰ رشیدی] با از :گربو (کردن )۳ واره (پسوند) با حذف يك
واو « فرهنگه نظام > جمماً یمنی لابق کردن (قس : کوشواره ) « رشیدی > :"

ز بژم مخنقةٌ یافت شاخ کل منظوم چو باد کرد کربواره شجر منثور .

انیراخیکتی ۸« رشیدی .
############ BQT:1814
(no exact page map; using offset -1205 -> pdf page 609; check the printed number and re-run with --pdf-page if off)
REF: BQT:1814  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 609  OCR-lang: fas

کزف ۱۸۱۳۳
وآن‌کز در ولاییت خرامان رواج دارد . درخت کز را کوبند وبعریی طرفا خوانند 8 .
گزف ۱« بنتح اول و سکون قانی وفاء گزماز ك ۱ « بفتح اول وسکون‌انی
بمعنی قیرباشد وآن صدفی است‌سیا هکه‌برکشتی | و میم بالف کشیده و زای قطه‌دار مفتوح بکاف
رجهازمالند وسیم سوخته را نیز کوبند- وسواد | زده, بارومیوة درخت کزرا میگوبند (۱)ومعرب
زر گربراهم گفته‌اند؛ وجضم اول نیز بنظرآمده‌است | آن جزمازج است و بمریی "ثمرة الطرفا خوانند
وبا زای فارسی هم هست . وحص‌الانل همان است با ای مثلثه .
گزل 4 - بر وزن نسکه .هر چیز که گزمازو ۷ - بر وزن شفتالو : بممنی
بدان تفیدر ذائلقه کنند ۴ - و سرمازده رانیز | گزمازك است که موه درخت کز باشد .
کوبند ۴ . گز ملك بکسرئانی وض‌ثالث‌وسکون
گزلک - بکر اوز و لام وسکون‌نانی | لام وکاف » بمعنی کزشایکان است ۸ و آن‌مقدار
وکاف :کارد كوچك دسته درازراگوبندگ۴ -ونوعی | يك ارش ولیم است بچی ز کی کم .
از قلم تراش را هم گفته‌اند که سر آن برکشته گز ند ‎٩‏ - بروز ن کمند . بممنیآسیب
و دلباله‌اش باررك باشد و بیشتر از جانب هصر وآفت و رنج و چشم زخم باشد .
آورند . گلزنند « با نون بروزن فرزند » جوال
گم - بفتح اول وسکون ثانی و میم : پرکاه راکوبند *۱.

(۱) چش : کوبند .

۱- ر4 :کزف »کف » کشف ؛ و رك :کرف . ۴ - چیزی که بداز شراب
خورند از قبیل میوه وآجبل و جز آنها » نقل » مزه «فرهنگه نظام» . سراج کوید : «ک ز که
بوزن نمك » هر چه برآن تغیین ذائقه کنند در شراب » و در برهان تغییر ذالفه مطلفاً و آن
خطاست.» (سراح‌اللغات بنل فرهنگه نظاءم ج ۵ ص لط) . ۴ - هرضی عشهپو رکه بعربی
تشنج گوبند «رشیدی > «کز4 زدن زخم » تشنج و بدی زخم ازآب برداشتن با بو بردن.میرالهی
همدانی (گوید ) :
دل خو نگرفته است که دشمن هم از غمش در هم کشیده روی چو زخم کزك زده .>
```


## [2026-09-06T22:19:04.937Z] TOOL CALL #46: Bash

```json
{
 "command": "for p in \"1809 606\" \"1816 612\" \"2258\" ; do set -- $p; echo \"############ BQT:$1\"; if [ -n \"$2\" ]; then python3 tools/ref_page.py BQT:$1 --pdf-page $2 2>&1 | head -28; else python3 tools/ref_page.py BQT:$1 2>&1 | head -28; fi; done"
}
```


### [2026-09-06T22:19:11.806Z] TOOL RESULT

```
############ BQT:1809 606
expected ABBR:page (e.g. BQT:918 or MON5:528)
############ BQT:1816 612
expected ABBR:page (e.g. BQT:918 or MON5:528)
############ BQT:2258
(no exact page map; using offset -1917 -> pdf page 341; check the printed number and re-run with --pdf-page if off)
REF: BQT:2258  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 341  OCR-lang: fas

بیان <چهارم
در واو با جیم ابجد مشتّمل برپاج لفت و کنایت
وجارش!۱ » بکسر اول بر وزن ِ وج رگر۴ ه بفتح‌کاف فارسی وسکون
سفارش , بلفت زند و پازند ‎)٩(‏ بممنی کدازش | رای قرشت » مفتی وافتوی دهنده راکوبند چه
وکاهیدن وضمیف ولاغن شدن باشد . وجر بمعنی فتوی آمده است .
وجر؟ - بفتح اول وئاتی وسکون رای وچنك؟ « بروزن شزك » منقارمرغان
قرشت ؛ بمعنی فتوی باشد ومعنی آنرا درکنز | را کوبند .
اللفت () دستور حاکم شرع در هثل شرعی وجود ساز معادن - کنابه از
نوشته‌بودند » وباین‌ممنی با جیم فارسی‌هم آهده | آقتاب عالمتاب است .
است .
بیان پنجم
در وأو با یم فارسی مشتمل بر دو لغت
و چر* - بفتح اول وئانی وسکون رای ۱ قرشت , بمعنی فتوی باشد و آن دستور حاکم

(۱) چك : ژد ویاژند . . (۲) صحبح «کنزاللفه» است .

۱ -ساظ . مصحف «وناژشن» . ۸« وتاچشن » ۷)1(]2011(5120 پپلوی بممتی گدازش.رك :
اسشق ‎۸٩۱‏ ور4: کداختن.- اما وجارش * وجارشن بپلوی بممتی گزارش (۸.م.) است .

۴ * «وجر» (ه.م.) قس: وجارش: گزاره, گزارش «خرده اوستا ص۷۸ ۰

۴ «وچر گر» (ه.م ) ورك: خرده اوستا ص۷۸ . ۴ -ظ . مصحف «چنگه»
(«.م.) و «و» عطف‌است. - دراوستا- ۷161۳2 بمعنی فتوی دهنده‌است. ازهمین لغتاست
کلمهٌ «وزی » (م ) که عرب از ایرانی بماریت گرفته . در فرهنگها لغات «وجر؟ و « وجارش >
و "وج گر» بمعانی گزاره باگزارش ( شرح ونفیر ) وفتوی ودستور وفتوی دهنده با مفتی ضبط
```


## [2026-09-06T22:19:20.694Z] TOOL CALL #47: Bash

```json
{
 "command": "python3 tools/ref_page.py --help 2>&1 | head -20"
}
```


### [2026-09-06T22:19:22.399Z] TOOL RESULT

```
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


## [2026-09-06T22:19:24.644Z] TOOL CALL #48: Bash

```json
{
 "command": "echo \"############ BQT:2279\"; python3 tools/ref_page.py BQT:2279 2>&1 | head -30; echo; echo \"############ BQT:1816 (pdf 612)\"; python3 tools/ref_page.py BQT:1816 --pdf-page 612 2>&1 | head -30"
}
```


### [2026-09-06T22:19:34.693Z] TOOL RESULT

```
############ BQT:2279
(no exact page map; using offset -1917 -> pdf page 362; check the printed number and re-run with --pdf-page if off)
REF: BQT:2279  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 362  OCR-lang: fas

-۷۷۷۹- وژنگه

ورزق٩‏ ‌- بفتح اول وئالی وسکون‌قاف, وزمه* ‌- بفتح‌اول ومیم وسکون ثالی.
معروف است و اورا فوك خوانند وبمربی شفدغ | آخر فضل زمستان راکوبند چه وزمه باد» بادی
گوبند؟ . باشد که درآخر زمتان وزد .3

وزك - بنتح اول والی وسکون کاف, زیر « با ثالك مجهول بروزن زریس ۰
درخت پده را کویند؟ , وآن درختی است که ۲ زردچوبه را کوبند۹ - وبا ثالك معروف‌درعربی
هرکز بارندهد و بعربی غرب خوانند . کوبند | بمعنی دستورباشد۷ .
اکر شخصی را زلو بگلو رفته باشد آب بر که وزیری* - بروزن امیری » نوعی از
آبراگرفته برحلق او ریزند برآید۴ . انجیرباغد وآن میوه‌است معروف +

بیان دهم

وژن - بفتح اول و ثالی بروزن چمن » وژ نگ < بنم اول بر وزن تفنگه .
کنافت ونجاست را کوبند ‎٩‏ . توژی*۱ باشد جگری رنگ که برپایین تیریعنی

۱- موّلف سراج نوشته : « وزغ , بفتحتین غوك » وبقاف که شهرت گرفته لهجدعراقیان
است و صاحب برهان حرف اصلی پنداشته با آنکه مکرر نوشته که قاف در فارسی لیست .بقل
« فرهنگه نظام ج ۵ ص مب >. : ۴ - رك : وزغ » وزغه ۰ ۴ -رك4 : یده ۰

۴ - « وز4 بوزن و معنی وزغ >« رشیدی >. 8 - *زم» بمعنی سرماست. ر4:
زمتان ؛ ظ. «و» اول زاید وحرف عطف است . ‎٩‏ - مصحف « زربر».

۷ -کلمه معرب است « اسشق ۰۱*۸۶ از ۷101۲ ( با ۷۵17 ) پپلوی ۸« باروچا ۳۳۶
ار اوستایی ۷1178 قتوی دهنده 3 پورداود . خرده اوستا ص ۷۸ ۰5 آرمنی ۷1۳ » لیز آرمنی
7 * فارسی 8121۲ ( دهخدا » ریش‌مفید ده » محصل مالیات ) » -ربانی 862178[/6(ژاندارم)

############ BQT:1816 (pdf 612)
REF: BQT:1816  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 612  OCR-lang: fas

بیان یازدهم
در کاف فارسی با زای فارسی مشتمل 32 چهار لغت
وا ۱ - بنم اول و نانی‌بالف کدیده | بمعتی فیرباشد وآن صمفی‌است سباه که بر درز-
و بزای فارسی زده » چینه دان مرغانرا کوبنن | های کشتی و جهاز مالند - و بمعنی سیم سوخته
وبعربی حوصله خواند .# وسواد زرگری هم آمده است .
ارچ هر
گزدهم بفتح اول و سکون ثانی گم - بنم اول و سکون ثالی و میم ء
وفتح دال ابجد وها وسکون میم » دام پهلوانی | درخت سده را کوبند که درخت پعه غال است
است ایرانی ۰ وبمربی شجرقةالیق خوانندگ - وبمعتی اندوه ودل
گوف ؟ < بفتح اول و سکون نانی وفاء تنگی هم بنظرآمده است 8 .
بیان دواز دهم
در کاف فارسی با سین بی نقطه مشتّمل بر بیست و بك لغت وکنایت
کار ۹ ۰ سم اول بروزن دچارء بمعنی باشد بچه و بمعئی خوردن هم هست‌لیکن‌خوردن
گذارباشد که از گذاشتن است۷ - وامربگذاشتن | شراب وغم خوردن ۱۴.
هم هست بعتی بگذار ۷ - وبمعتی خورندة غم گسارده ۱۴ بروزن و معنی کذاشته
و خورنده شراب لیز هت ۸ همچو مگ ار است .
و میگار ‎٩‏ . مت » بنتح اول‌بروزن دست » بمعنی
گساردن *۱- "پروزن ومعمنی گذاشتن۷ | زشت و قبیح و نازیبا باشد ۱۴. ۱
۱ ۹ - رد :کزار . در رشیدی «گزار بالسم, چینه‌دان مرغ » اما دردشهٌ سروری بکاف
تازی آمده ». ۲ - ۳ط87548 ( پهلوان ایرانی ) ۶ فپرست ولف ؟.
۴ -رك :کزف ,کشف . ورك :کرف . ۴ - رك : رشیدی .
8 - مسحف «کرم» ( بشم اول ) . ‎٩‏ - رك : کاردن .
۷ - تلفظی درگذاردن . ۸ - اسم فاعل مرخم .
‎٩‏ - اندهگار من شد واندء بمن گذاغت وامق چه کرد درقم مضرا, من‌آ نکنم.
* از :گار (ه.م.)+دن ( پوند مصدری ) . ۹۱ باین معنی شاهدی باد
تکرده‌اند رك : کار گارده ۰ ۴قی: باده گسار, غمگار ۰ ورد ح ۹۳
ارزگ ام مفعول ازه گاردن» (و.م.):
سافیا مر مرا ازآن می ده که غ من از و گارده شد. آپوشکور بلخی «رشدی»؛ ۰
```


## [2026-09-06T22:20:02.770Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON خرفس\"; grep -n \"خرفس\\|خرفست\\|خفستر\" MON_part1.txt MON_part2.txt | head -8; echo \"=== MON خستر ctx\"; grep -n \"خستر\" MON_part1.txt | head -3; echo \"=== IEC krep\"; grep -n -i \"krepos\\|krep-\\|k'rep\" IEC.txt | head -10; echo \"=== SYN body\"; grep -n \"corpus, .*body\\|Av. kəhrp\\|kehrp\" SYN.txt | head -10"
}
```


### [2026-09-06T22:20:02.864Z] TOOL RESULT

```
=== MON خرفس
=== MON خستر ctx
8344:اخسترمار: 1- .2 (ص‌مر.) اختر شمار» 
=== IEC krep
7844:krekos — krep-
7860:krep- ‘rumble, roar, resound’ Skt. cf. krape, mp. ‘lament’; a-krapista ‘he
15883:skrep- ‘hawk, rasp, scrape, rustle’. (Variant in Cz.) ON cf. skrjáfa, v. ‘rustle’; Cz. chfapét, v. “be hoarse, crackle, crack’; cf. chfaplavy, adj. ‘hoarse, cracked — of voice’; (mod. chrap-); Li. skrepsiu, -sēti, v. ‘creak, grate’; cf. skrep- liai, mpl. ‘phlegm’
=== SYN body
6595:4. OE hrif (also sometimes ‘belly’; cf. NE midriff), OHG (h)ref, prob. : Lat. corpus, Skt. krp- ‘body’, etc. (4.41). Walde-P. 1.486.
```


## [2026-09-06T22:20:04.557Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd1 kʷer\"; grep -n \"q\\\"er-\\|qŭer-\\|qṷer-\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10; echo \"=== WLD Bd1 krep\"; grep -n \"qṷrep-\\|q\\\"rep\\|krep-\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10"
}
```


### [2026-09-06T22:20:04.624Z] TOOL RESULT

```
=== WLD Bd1 kʷer
=== WLD Bd1 krep
```


## [2026-09-06T22:20:10.562Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN 4.41 body\"; grep -n \"4\\.41\" SYN.txt | head -8; echo; sed -n '6560,6600p' SYN.txt"
}
```


### [2026-09-06T22:20:10.622Z] TOOL RESULT

```
=== SYN 4.41 body
1620:Lith. uola ‘rock’ (also ‘whetstone’), Lett. wola ‘pebble, egg, rock’ : Lett. velt, Lat. volvere ‘roll’, Lith. apvalus, ON valr ‘round’, etc. (Walde-P. 1.298 ff., without uola). Miihl.-Endz. 4.416.
5520:5. Lith., Lett. wodega (in Lett. of limited scope), etym: dub. Walde-P. 1.175. Miihl.-Endz. 4.412.
6385:in -6os) to o7q0v" or7G0s (Hesych.), this : Skt. stana- ‘woman’s breast’, etc. (4.41). Walde-P. 2.663.
6395:breast’ (4.41). Walde-P. 2.81. Stokes 55. Otherwise (: Lat. pectus) Pedersen 1.90, etc. (cf. Walde-P. 2.17).
6403:4.41 BREAST?
6439:2. NG pacrdpr, deriv. of Grk. paorés ‘breast’, and uti ‘breast’ (4.41) also ‘udder’.
6440:3. It. poppa, mammella, same as for ‘woman’s breast’ (4.41).
6446:Br, tez : Fr. tette ‘teat’, etc. Cf. 4.41, Rum. (did.

6. Lith. pilvas ‘belly’, etym.? Les-
kien, Ablaut 359 : Lith. piltt ‘pour’, pilnas ‘full’. Better (though ultimately perh. the same root) : Lat. pélvis ‘basin’, Grk. ré\da ‘bowl, pail’, etc. (Walde-P. 2.56 ff., without pilvas). Cf. the mod- ern anatomical application of pelvis.
Lett. véders, above, 1.
Lith. skilvis ‘stomach’ (so in transla- tions of NT, 1 Tim. 5.23; ef. also Kur- schat, Lalis, Gailius-Slaza, etc.), perh. (cf. Lett. skilva, ‘maw of birds’) : Lith. skeltt ‘split’, ete. Walde-P. 2.594.
Lith. pilvélis, pilvukas (given for ‘magen’ by Senn, Lit, Sprachl., pp. 42, 267), dims. of pilvas ‘belly’.
Lett. pazirds ‘stomach’, epd. of pa ‘under’ and zirds ‘heart’. Mihl.-Endz. 3.98.
z CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
source, or from the same source as, Grk. Hapowros ‘bag, pouch’. Buck, IF 25.257.
7. ChSl. crévo ‘belly, womb’, Boh, stfevo, SCr. crijevo, Pol. trzewo ‘intesting’ OPruss. kermens ‘body’, root connec. tion? Walde-P. 2.577, Berneker 150, Briickner 581.
ChSl. qiroba ‘belly’(?), ‘womb’ (much less frequent than éévo, Jagié, Entste- hungsgesch. 421; the examples are Where Grk. kotha is ‘womb’, but this may be accidental), SCr., Bulg., Russ, utroba ‘womb’ (in church language), Pol. wq- troba ‘liver’, all: ChSl. jetro ‘liver’, etc. (4.45).
SCr. irbuh ‘belly’, Pol. dial. telbuch id., Russ. trebucha ‘intestine’, etc., etym,? Miklosich 364, Briickner 567,
Boh. biich, bricho, Pol. brzuch, Russ, brjucho ‘belly’ : Goth. brusts ‘breast’, etc. (4.40), orig. ‘swelling’, Walde-P. 2.198. Berneker 95 ff.
Boh. Zivot, Pol. zywot ‘belly, womb’, Russ. Zivot ‘belly’ (Lith. Zyvatas ‘womb’ fr. Pol. or Russ.), same as the word for ‘life’, ChSI. Zivotii, Boh. Zivot, etc. (4.74), applicable to either ‘belly’ (as ‘stomach’) or ‘womb’, as the source of life,
ChSl. (late) zelqdiikt, SCr. Zeludac, etc., general Slavic for ‘stomach’, etym.? Against deriv. fr. Zelqdt ‘acorn’ (Briick- ner 665), see Meillet, Etudes 322 ff.
8. Skt., Av. udara-, above, 1.
Skt. jathara- ‘belly, womb’ : Goth. kilpet ‘womb’, OE cild ‘child’, fr. IE *gel-t-, beside *gel- in words for round objects. Walde-P. 1.614. Feist 311.
Av. marsi- ‘belly’, perh. orig. ‘bag’ (cf. Ir. bolg, etc., above, 4), and the
gor BODY; BODIL pAR
are related to those wo eye aa have been discussed in 4.46. Yee others the commonest source is mou er", while some are words for ‘body’ or lap used in specialized sense, or of various other sources.
1. Grk. pirpa (in Aristot. HA 510° distinguished from ‘orépa or deddis ‘womb’ as the ‘tube and opening of the womb’; in NG the technical word for ‘vomb’, pop. ora); Lat. matrix ‘breeding animal’, late ‘womb’ (> It. matrice, etc.); SCr. materica, all derivs. of word for ‘mother’, as It., Sp. madre, Dan. moder, Boh., Russ. matka ‘mother’ also used for ‘womb’. Cf. also NHG mutterleib, gebarmutter, etc.
Grk, borépa (the most usual technical sia Hipp., saa etc.; cf. also Yorpos’ yaornp Hesych.), appar : Vorépos ‘latter, behind’, ai ee per’, ud ‘upwards’, so orig. ‘back part’ ‘upper part’? Or coy aa ae Sk ? perh. ultimately :
t. udara- ‘belly’ y
ely, ete. (4.46) with
analogical r i Baling a Fe mmation. Walde-P.1.191.
Grk. deAgis below, 7,
2,
vere Be volva, vulva, prob. : Lat. vol- foot, Grig ae ‘hollow of the hand or P.1301, | “HG Wrapper’, ete. Walde-
» Sin ‘breast?
(rare) : Skt, garbha-, etc.,
fr, L t . G lap’) ai, «te Lat. sinus “fold Sion fon ( ae / oe the common expres-
Digitized by Arya Samaj Foundation Chennai and eGangotri
Y FUNCTIONS AND CONDITIONS 255
4.47 WOMB
th. wamba, gipus, kilpet Lith.  Zyvatas sarpty yaoTnPy xothla, ae kvidr Lett. mdtes miesas, mates ; etc. Dan. moderliv klepis rot dtd, BATPS Sw. moderlif oer &révo, atroba erus, i hrif, innop r.  materica \ Cries mare Ue ME wombe Boh. Zivol, matka get ma Pere NE womb Pol.  zywot, lono * — matriz, maare, Du. baarmuoder Russ. matka Rum. pintece OHG (h)ref, wamba Skt.  garbha-, yoni- brit MHG  barmuoter, muoterlip Ay. garawa-, barabri- Ir, brid (wambe) croth, bru NHG mutterleib, gebdérmut- kof ter, schoss The majority of the words for ‘womb’ 3. W. croth (formerly also ‘belly’) :
W. crwth, NIr. cruit ‘hump’, Lith. krutis ‘breast’, etc. (4.40). Walde-P. 1.489.
4. OE hrif (also sometimes ‘belly’; cf. NE midriff), OHG (h)ref, prob. : Lat. corpus, Skt. krp- ‘body’, etc. (4.41). Walde-P. 1.486.
MHG muoterlip, NHG mutterleib, Dan. moder(s)liv, ivumoder, Sw. moderlif, lifmoder, cpds. of words for ‘mother’ and ‘body’ (4.11), the latter also used alone for ‘womb’ (as NHG lezb in Luther).
MHG barmuoter, NHG gebdrmutter, Du. baarmuoder, cpds. of words for ‘bear’ and ‘mother’.
NHG schoss ‘lap’ (orig. part of a gar- ment), also used for ‘womb’. Weigand- H. 2.782.
5. Lett. mates miesas or mates klépis, lit. ‘mother’s body’ or ‘mother’s lap’, translations of NHG mutterleib, mutter- schoss.
6. Pol. tono ‘lap’ (ChSI. lono ‘bosom, lap’, etc.) also used for ‘womb’, like NHG schoss.
```


## [2026-09-06T22:20:12.598Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD kahrp\"; grep -n \"kohrp\\|kahrp\\|kdhrp\\|krp-\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10; echo \"=== WLD qer machen\"; grep -n \"gestalten\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10"
}
```


### [2026-09-06T22:20:12.676Z] TOOL RESULT

```
=== WLD kahrp
30598:Ai. k’pd instr. sg. ,, Gestalt, Schonheit -- , av. karaf's, gen. kahrpo „Gestalt, 
=== WLD qer machen
6159:Alben (urspriinglich wohl ,,weifiliche Nebelgestalten‘ : ; nicht wahrschein- 
32579:1. q!er- „machen, gestalten“, vielleicht urspriinglich von irgendeiner nicbt 
52514:„stechen“). Lat. fngo , -ere, finxi, fictum ,,eine Masse gestalten, bilden,
```


## [2026-09-06T22:20:19.756Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD 30590-30615\"; sed -n '30590,30615p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt; echo; echo \"=== WLD 32575-32605\"; sed -n '32575,32605p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-06T22:20:19.820Z] TOOL RESULT

```
=== WLD 30590-30615
des got. anord. Wortes frir „Dach“ von hrdst, rdf, usw. wenig iiberzeugend 
und muB andrerseits das pers. Wort nicht ursprgl. „Dach“ bedeutet haben. 
Vielleicht aber ist krada und die iibrigen bsl. Worte ein Fall von Storung 
der Gutturalreihen, die Wz. samtlicher obiger Worte daher als bred- an- 
setzbar. 

1. qrep-, qrp- „Leib, Gestalt' - (qtrep-1 s. u.). 

Ai. k’pd instr. sg. ,, Gestalt, Schonheit -- , av. karaf's, gen. kahrpo „Gestalt, 
Leib -- , mp. karp „K6rper' ; (av. xrafstra- n. ,,Raubtier“ aus qrrp 4- [e] d-tro- 
zu eel- „essen -- ? Bthl. Wb. 538); aber av. hu-karopta- „schongeformt“ 
ti. kljitd- „geordnet, hergestellt“ (von Haaren und Nageln: ,,beschnitten“), 
kulpatP ,,wird geordnet, wird zuteil 1- , kalpdynti „ordnet an, verteilt, teilt 
zu - sind wohl Abkommlinge von (s)ijrl-p- „schneiden“ (Persson KZ. 33, 
289 f., Uhlenbeck Ai. Wb. 48 f.: an aich ware „verteilt, disponiert“ gleicher- 
weise aus (s)qer-p- ..schneiden" gewinnbar, zu welchem Uhlenbeck Ai. Wb. 
63 f. das Nomen k>'p- stellt, als ,,Schnitt, Gestalt 11 , s. u.). 

Alb. (Jokl SBAkWien 168, I 80) wahrscheinlich s-krep , s-kep ,,gleiche 
ein wenig -- = idg. sent, som, sm-, vgl. zur Bed. ahd. gi-I/h ,,gleich“ : hh 
„Leib -- ). Lat. corpus , -oris „Leib, Korper 1- , auch mir. erz .,Leib“ (*q)-pis, Fick 
II 4 97 zw., Stokes KZ. 36, 275; unsicher); vermutlich ahd. Qi)ref m. ..Leib, 
Unterleib, Mutte rleib“, afries. href , hrif, „Bauch“, ags. hrif n. „Mutterleib, 
Bauch -- (Fick IP 97; das von Trautmann Grin. Ltg. 13 eingewendete ags. -i- 
ist aus *hrcfiz- = qrepes- zu rechtfertigen, vgl. den es-St. lat. corpus; anders 
Fick III 4 103: als *qriji- von einer sonst ungestutzten Wzf. ( s)qreip - neben 

=== WLD 32575-32605
kommenschaft, Kinder, Familie, Clan“, cymr. plant „Kinder“ (Fick II 4 63 f.) 
ist vielmehr = air. eland „planta“, Lw. aus lat. planta (Thurneysen Hdb. 
520, 522, Pedersen KG. I 234, 235). 

1. q!er- „machen, gestalten“, vielleicht urspriinglich von irgendeiner nicbt 
mehr bestimmbaren Handwerkstatigkeit. 

Ai. karoti (Imper. Jcuru), krnoti „macht, vollbringt“, Ptc. krtd -, kara- 
„tuend, machend“, m. „Hand, EIefantenrussel“ (kaum in der Bed. „Hand“ 
zu arm. kil „Spanne“, s. Pedersen KZ. 39, 377), kara- „machend, m. Tat“, 
karman- n. „Handlung, Werk“, karmara-h „Schmied“; daneben mit s- 
pari-skar- und sq-skar -; 

av. koronaoiti „macht, vollfuhrt, bereitet, tut“, ap. akunavam , karta -; av. 
Sara „Mittel, Hilfsmittel", np. car „Mittel“, cara „Mittel, Ililfe, List" (Bthl. 
Wb. 584 ; cara = si. Sara „Zauber“, s. u.). 

Cymr. paraf „bewirke, verschaffe", inf. peri , 3. sg. Praet. peris, corn, pery 
„du wirst machen", wozu redupl. (aus einem redupl. Praes.? Zupitza 
KZ. 35, 266) wobl cymr. pybyr „tatkraftig“ (Entlebnung von paraf aus lat. 
pario -f- par o — s. Osthoff Arch. f. Rel.-Wiss. 8, 63 — wiirde dadurch etwas 
fraglich). 

Air. cruth „Gestalt“, cymr. pryd „Aussehen“ (i efirtu -, s. Fick II 4 60, Zu- 
pitza KZ. 35, 254; Thurneysen Hdb. § 222; cymr. pryd „Zeit, Mahlzeit". 
acorn, prit „Zeit" weiB ich trotz Pedersen KG. I 43 kaum damit in der 

34 *
```


## [2026-09-06T22:20:30.302Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 620\\|Page(s): 619-620\" POK_full.txt | head; echo \"---\"; grep -n \"krep-1\\|Icrep-\\|k''rep\" POK_full.txt | head"
}
```


### [2026-09-06T22:20:30.361Z] TOOL RESULT

```
48449:Page(s): 620 
48455:Page(s): 620 
48488:Page(s): 620 
48760:Page(s): 620 
48766:Page(s): 620 
---
48390:Root / lemma: krep-1, kfp- 
48398:Root / lemma: krep-1, kfp- : body derived from -p- suffix of Root / lemma: (s)ker-4, (s)kera- 
48421:Root / lemma: krep-1, kfp- : body derived from -p- suffix of Root / lemma: (s)ker-4, (s)kere- 
48747:Root / lemma: krep-1
```


## [2026-09-06T22:20:32.263Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '48388,48460p' POK_full.txt"
}
```


### [2026-09-06T22:20:32.312Z] TOOL RESULT

```
Root / lemma: krep-1, kfp- 

Meaning: body 

Note: (or k^erp-l see below) 

Comments: 

Root / lemma: krep-1, kfp- : body derived from -p- suffix of Root / lemma: (s)ker-4, (s)kera- 

, (s)kre- : to cut 

Material: Old Indie krpa\x\s\x. Sg. "shape, beauty', Avestan karafs, kahrpam^sha^e, body'. 

Middle Persian karp " body ' (Avestan xrafstra- n. ' predator ' from *krep + *[e]d-tro-\.o ed- 

■eat'?); 

perhaps (?) alb. sh-krep, sh-kep^ resemble a little ' (5/7= Indo Germanic sem, som, sm-, 
compare to meaning Old High German gi-ITh^ alike ': ^'body'); 

Common alb. Celtic -e- grade. 

Maybe taboo words alb. shkrep^ rock, fire rock ', shkrep, shkref, shkreh^ trigger, fire', 
shkrepje^ glance, flare, gun '. 

But alb. qep " sew ' < sh-kep , shqep^ unpick, rip, tear, take out stitches; unfasten threads, 
resemble a little '; shqepoj^ to be lame'. 

Comments: 

Root / lemma: krep-1, kfp- : body derived from -p- suffix of Root / lemma: (s)ker-4, (s)kere- 

, (s)kre- : to cut 

(3) (s)kerp-, (s)krep-: 

alb. karpe, karme {*korp-n-) 'rock, cliff' krep, shkrep'rocW, slope'; 



Latin corpus, -or/sn. " body'; 

Middle irisli cnt "body' {*krpes)\ 

Old High German {h)refm. "body, lower abdomen, womb'. Old Frisian href, hr/TbeWy', 
Old English hr/fn. "womb, belly' {*hrefiz- = *krepes-). Old English mid(h)rif. Old Frisian 
midref phren, diaphragm, wall of muscles or membranes that separates the chest cavity 
from the abdominal cavity ' ("*cavity in the middle of the body '). 

Gr. npani(;, mostly PI. Ahzc, " phren', which would prove the initial sound as k" , is 
doubtful in its affiliation, because the suitable meaning from Old English mid(h)rif\s 
probably based on the first part of the compound; 

it would have to be then npani(; a short form to a similar composition; after Vendryes 
RC 44, 313 ff., Specht KZ. 68, 193 ff. would be Indo Germanic *k"'erp- taboo metathesis to 
*perk"-^\\ie, world, oak' (Gothic fa/r/vus 'wor\d'). 

References: WP. I 486 f., WH. I 277 f. 
Page(s): 620 

Root / lemma: krep-2 

See also: see above S. 567 ff. under ker-1. 

Page(s): 620 

Root / lemma: kret-1 

Meaning: to shake
```


## [2026-09-06T22:20:44.344Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFM وزير\"; grep -n \"وزير\\|الوزير\" AFM.txt | head -6; echo \"=== PLA wazir\"; grep -n -i \"wazīr\\|wazir\\|vizier\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -8; echo \"=== LKT wesir\"; grep -n -i \"wesir\\|vizier\\|vezir\" LKT.txt | head -6"
}
```


### [2026-09-06T22:20:44.416Z] TOOL RESULT

```
=== AFM وزير
905:ܐ 3) فارسي حض ووعناه ܚ لَب به ٠‏ الوزير نظام الملك | 
=== PLA wazir
19688:wabara 271 wazir 
19718:Nis- wuzarä: Pl. v. wazir q. v. 
19721:23 - wazir: "Minister" ms vicir am. vicira 11 air. *vicirna. 
=== LKT wesir
1498:'Feldherr,  Vezier'  [zu  pers.  färzänä 'weise,  gelehrt'  Horn  NpEt  S.  1 81 ,  Nr.  8 1  ö]; da  im  orientalischen  Schach  neben  dem König  [säh  s.  hier  Nr.  1762]  nicht  die Königin,  sondern  der  Wesir  die  Haupt- figur war,  wurde  hieraus  afrz.  ferce, fierge,  nfrz.  vierge  [mit  volksetymolo- gischer Umdeutung  zur  „Dame"],  prov. fersa  ;  bulg.  serb.  ferz,  russ.  ferz'  'Dame oder  Königin  (im  Schachspiel)'.  [Mikl SlEtWb  58a.  Bern  SlEtWb  280/281. ML  3266.
1519:'Elefant'  [aus  pers.  fil;  wohl  durch ägyptische  Zwischenhändler  aus  einer hamitischen  Spiache,  vgl.  in  der  Sprache der  Tuareg,  dem  Temasirt,  elu  'Elefant', wozu  der  ägypt.  Art.  p  (worüber  hier Nr.  274)  kam ;  aus  demselben  Grund- wort gr.  SXeqpa?,  lat.  elephantus];  hier- aus über  tk.  fil  bulg.  fil  'Elefant',  serb. filj  als  Adj.  'elefanten-';  auf  unmittel- barem Wege  durch  den  Elfenbeinhandel wurde  altisl.  fill,  dän.  fil  'Elefant',  fils- bein  u.  filsben  'Elfenbein'.  —  Aus  näb ul-fll  'Zahn  des  Elefanten'  entstand  sp. marfil,  pg.  marßm  [mit  Wechsel  der  an- lautenden Nasale  unter  Einfluß  des  b und  gleichzeitiger  Dissimilation  des  ersten /].  BATST  in  RomForsch  I,  130;  DE- FREMhJRY  in  JAs  5.  serie  t.  XIX,  90  sq. —  In  den  romanischen  Sprachen  ist fll  als  Benennung  der  dem  Könige  und ilem  Wesir  [d.  h.  der  Dame  oder  Kö- nigin] nächststehenden  Schachfigur  mit alfäris^sp.  alferez  usw.  [s.  hier  Nr.  591] vermengt  worden  [vgl.  ähnlich  russ. usw.  slon  'Elefant'  und  'Läufer  im Schachspiel',  MSISI  774/775];  die  Folge hiervon  war  eine  Änderung  in  der  Auf- fassung der  betr.  Figur:  der  Kriegselefant wurde  zum  Fahnenträger,  Läufer,  frz. sogar  durch  volksetymologische  Um- deutung  zum  Hofnarren  [die  somit  frei- gewordene Rolle  des  Elefanten  wurde auf  den  Turm  übertragen].  Im  einzel- nen ist  it.  alfido,  alfino,  sp.  alfil,  arfil, pg.  alfil,  alfir,  alfim,  prov.  alfi,  fol,  afrz. aufin,  frz.  fou  'Läufer'.  —  [Das  vom Kalifen  HARUN  AR-RAS1d  Karl  dem Großen  geschenkte  Schachspiel  im  kai- serlichen Schatz  zu  Nürnberg  enthält noch  Elefanten!]  [DE  113/114  u.  302. Eguilaz  167.  ML  3291.  Bern  SIEtWb 281.
4835:'Erster  Minister,  Regent'  [vom  Vb.  wa- zara  'tragen',  weil  der  erste  Minister die  Lasten  trägt,  die  eigentlich  dem Herrscher  aufgebürdet  sind ;  andere  von ar.  Philologen  gegebene  Ableitungen s.  De  Sacy  ChrAr.  I,  i248;  II,  298]; zur  Bezeichnung  des  Ministerpräsidenten an  orientalischen  Höfen  in  alle  euro- päischen Sprachen  übergegangen:  sp.  pg. kat.  visir,  sp.  pg.  vizir^  frz.  vizir;  ndl. engl,  vizier,  dtsch.  Wesir;  russ.  wizir. Als  Lehnwort  findet  es  sich  als  sp.  al- vacil,  alguazil  'Gerichtshäscher'  [z.  B. los  alguaciles  de  la  Santa  Inquisiciön], pg.  alvazir,  alvazil  'Schöffenrichter',  al- f/uazil  'Gerichtsdiener',  guazil  'Statt- halter', frz.  alguazil  [aus  dem  Sp.], nrgousin  'Stockmeister  im  Bagno',  it. aguzzino  'Sklavenaufseher'.  —  Über  Ge- schichte und  heutige  Verwendung  des Titels  Wezir  vgl.  NO  Hl,  61.  [DE  129. Devic  DEt  18/19.  34/35.  Lammens Rem  13/14.
6267:vizier  2160
7635:Vizier  2160
```


## [2026-09-06T22:20:45.421Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG kar\"; grep -n \"guz[iī]r\\|gozir\\|wizīr\\|wizir\" CHEUNG.txt | head -10; echo \"=== HUB\"; grep -n -i \"vezir\\|wezir\\|guzir\" HUB.txt | head -10"
}
```


### [2026-09-06T22:20:45.499Z] TOOL RESULT

```
=== CHEUNG kar
=== HUB
5802:'dahinfahren , wehen*; vaztr 'Vezir', aus dem Arabischen
8069:ap. cisciy; vazlr (arab. LW.) 'Vezir', zd. vlcira- *der die
```


## [2026-09-06T22:20:55.327Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/corset",
 "prompt": "Give the full etymology entry for corset (and any mention of Old French cors, corps, corpus)."
}
```


## [2026-09-06T22:20:56.703Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Sanskrit",
 "prompt": "Give the full etymology of Sanskrit: samskrta, sam- + karoti/krta, and the date/route of the English word."
}
```


### [2026-09-06T22:21:02.449Z] TOOL RESULT

```
# Sanskrit Etymology

**Full Etymology:**
Sanskrit derives from the Sanskrit term *samskrtam*, meaning "put together, well-formed, perfected." This breaks down into two components:

- **sam-**: "together" (from PIE root *sem-, meaning "one; as one, together with")
- **krta-**: "to make, do, perform" (from PIE *kwer-, meaning "to make, form")

**Route to English:**
The word entered English around 1610s, referred to as the ancient sacred language of India. It was recognized as "the cultivated or literary language, distinguished from the vulgar dialects," and was regarded by some as a perfect language spoken by the gods.

The term remained a learned language long after ceasing to function as everyday speech among native speakers.
```


### [2026-09-06T22:21:07.244Z] TOOL RESULT

```
# Etymology of Corset

**Word Form:** corset (n.)

**Time Period:** Late 14c. (mid-13c. in Anglo-Latin)

**Original Meaning:** "A kind of laced bodice, close-fitting body garment"

**Language Origin:** From Old French *corset* (13c.), meaning "bodice, tunic"

**Root Etymology:** The Old French term derives from *cors*, meaning "body," which traces back to Latin *corpus* "body." This ultimately stems from the Proto-Indo-European root *\*kwrep-*, signifying "body, form, appearance."

**Semantic Shift:** The modern definition—"stiff supporting and constricting undergarment for the waist, worn chiefly by women to shape the figure"—emerged in 1795.

**Historical Note:** Corsets fell from fashion following World War I, as evidenced by a 1931 reference describing how from 1924-1927, combined corset and brassière sales in Cleveland declined by 11 percent as the "boyishly slender figure" replaced previous ideals.

**Related Forms:** Corseted/corsetted (1829), corseting, corsetry, and corsetier (corset-maker, by 1848).
```


## [2026-09-06T22:21:17.122Z] TOOL CALL #60: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%DA%86%D8%A7%D8%B1%D9%87' --note 'page 293, root Kwer 2, Persian čāreh < MP čārag < PIE *kʷer-' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%88%D8%B2%D9%8A%D8%B1' --note 'page 293, root Kwer 2, Arabic wazīr borrowed from Iranian MP wizīr / Av. vīcira-' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%86%D9%82%D8%B1%D9%87' --note 'page 293, root Kwer 2, Persian noqre silver, Wiktionary derives from Arabic nuqra, cites Gharib n-krtk' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%86%D9%82%D8%B1%D8%A9' --note 'page 293, root Kwer 2, Arabic nuqra cavity / high-quality silver, root n-q-r; further reading Gharib Sogdian n-krtk p231' 2>&1 | tail -3"
}
```


### [2026-09-06T22:21:20.810Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/e0864fe808354c3b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a36dedc97d3e5531.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bcf39b8ae8d46151.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/47d4b7bd0136178c.txt
```


## [2026-09-06T22:21:26.988Z] TOOL CALL #61: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7er-' --note 'page 293, root Kwer 2, PIE *kʷer- to do/make/build' 2>&1 | tail -2; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/krep-' --note 'page 293, root Krep, PIE *krep- body; Av. kəhrpəm, MP kirb, Latin corpus' 2>&1 | tail -2; python3 tools/fetch_source.py 'https://www.etymonline.com/word/corset' --note 'page 293, root Krep node 5/7, corset < OF cors < L corpus' 2>&1 | tail -2; python3 tools/fetch_source.py 'https://www.etymonline.com/word/Sanskrit' --note 'page 293, root Kwer 2 nodes 5-7, Sanskrit < samskrtam sam- + krta- < PIE *kwer-' 2>&1 | tail -2; python3 tools/fetch_source.py 'https://www.etymonline.com/word/corpse' --note 'page 293, root Krep node 7, corpse < OF cors < L corpus' 2>&1 | tail -2"
}
```


### [2026-09-06T22:21:32.016Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/05ebe20cc6379e2e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/692b4f6157707c9f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dbb47f416b7ae1de.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3fa00232da2140c2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fc71e9765f3aa705.txt
```


## [2026-09-06T22:21:39.337Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%AE%D8%B1%D9%81%D8%B3%D8%AA%D8%B1/",
 "prompt": "What do Dehkhoda / Mo'in say about the Persian word خرفستر? Give the definition and any etymological note (Avestan/Pahlavi origin), and any variant form like خستر."
}
```


## [2026-09-06T22:21:40.601Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%A9%D8%B1%D8%B3%D8%AA/",
 "prompt": "What do Dehkhoda / Mo'in say about the Persian word کرست? Give the definition and the origin tag (e.g. [فر.] French corset)."
}
```


### [2026-09-06T22:21:45.825Z] TOOL RESULT

```
# Dehkhoda and Mo'in on خرفستر

**Dehkhoda's Definition:**
"Harmful creatures such as snake, willow, lizard, toad, mouse, ant, flea, bee, locust, fly, spider, worm, beetle, louse, lice, and any other small harmful animal."

**Mo'in's Definition:**
According to Farhang-e Mo'in, it means: (1) a harmful and damaging animal like snake or scorpion; (2) a harmful creature attributed to Ahriman in Zoroastrianism.

**Etymology & Variants:**
Both sources note the Avestan origin: *xrafstra* (Pahlavi: *xrafstar*). The variant form **خستر** (*khaster*) is also documented in classical Persian dictionaries. 

Etymologically, خرف reportedly means "spark/flame" and ستر means "to wipe away/destroy," suggesting the word may originally mean "that which destroys the sacred fire."
```


### [2026-09-06T22:21:46.707Z] TOOL RESULT

```
# Dehkhoda and Mo'in Dictionary Definitions of کرست

**Dehkhoda's Definition:**
"شکم بند زنان. بندی پهن و کش آمدنی و چسبان که زنان بر سرین و شکم و قسمتی از سینه بندند" (a women's waist band; a wide, elastic binding that women wear around their hips, abdomen, and part of the chest)
- **Origin tag:** [فرانسوی] (French)

**Mo'in's Definition:**
"سینه بند، شکم بند، تن پوشی طبی برای جلوگیری از افتادگی یا جا به جایی اندام ها" (a chest band, waist band, or medical garment to prevent sagging or displacement of body parts)
- **Origin tag:** [فر.] (French)

Both sources identify the word as borrowed from French and describe it as a restrictive garment worn by women to shape the torso.
```


## [2026-09-06T22:22:23.671Z] TOOL CALL #64: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D8%AE%D8%B1%D9%81%D8%B3%D8%AA%D8%B1/' --note 'page 293, root Krep node 3, Persian xarafstar Dehkhoda+Moin, Av. xrafstra / Phl xrafstar, variant خستر' 2>&1|tail -1; python3 tools/fetch_source.py 'https://abadis.ir/fatofa/%DA%A9%D8%B1%D8%B3%D8%AA/' --note 'page 293, root Krep node 6, Persian korset [فر.] from French corset' 2>&1|tail -1"
}
```


## [2026-09-06T22:22:26.091Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT corpse\"; grep -n -i \"^corpse\\|corpse, a dead\\|Corse, a corpse\\|corslet\" SKT.txt | head -6; echo \"=== SKT sanskrit\"; grep -n -i \"Sanskrit\\b.*krita\\|Samskrita\" SKT.txt | head -4; echo \"=== ARY چاره\"; grep -n \"چاره\" incoming/ARY/ARY_pages.txt | head -5; echo \"=== ARY نقره\"; grep -n \"نقره\" incoming/ARY/ARY_pages.txt | head -5"
}
```


### [2026-09-06T22:22:28.075Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/260b571630d4fad0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f194cc9c1e536145.txt
```


### [2026-09-06T22:22:28.149Z] TOOL RESULT

```
=== SKT corpse
4142:corslet.  (F.  -.  L.)  F.  corselet,  '  a  little body/  Cot. ;  hence  body  armour.  Double diroin.  of  O.  F.  con,  body  ;  sec  oorps.
4153:Corset,  Corslet;  sec  Corporal  (>].
=== SKT sanskrit
16475:Sanskrit.  (Skt)  Sltt  soMkrita,  lit '  $>'mmetncaUy  formed.'  —  Skt.  sam,  to- gether :  krita,  made,  from  kri,  to  make.
=== ARY چاره
=== ARY نقره
2281:فارسی (۳8۵۵۷):__ ارزیز (به چم قلع , فلز سپید و نقره فام) 2
2306:چم‌های این واژه در زبان‌های این فهرست: فلز سپید» نقره) سپید.
```


## [2026-09-06T22:22:33.903Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"corps\\.\" SKT.txt | head -4; echo ---; grep -n \"Corporal (2)\\|Corporal  (>\\]\" SKT.txt | head -4; sed -n '4130,4145p' SKT.txt"
}
```


### [2026-09-06T22:22:33.975Z] TOOL RESULT

```
4138:corps,  corpse,  corse,  a  body.  (F.— L.)  Here  tvrps  is  mcM).  F. ;  fw«  is  fiom torpst  by  loss  of  /.  M.  E.  corps.  ••  O.  F. corfi,  con,  the  body.  —  L.  corpus,
4141:cornet.  (F.  — L.)  F.  corset,  a  pair  of slays ;  dimin.  of O.  F.  cors,  body;  see  corps.
---
4153:Corset,  Corslet;  sec  Corporal  (>].
OB»>boTsc4  t&lmftl  (F.'L.)
COSTAL.
95
•*««/,  one;
I  F.    amirpme.  •-  L.    $ini-,    for cortiu,  horn.
ComicOi  CoroUa,  Corollary;  sec Orown.
Coronation,  Coroner,  Coronet ;  see Crown.
Cor];>oral  (i) ;  see  Oapitat Corporal(j),  belonging  tothebody.  <L.) L.  torf^oralu,   bodily.  ■>L.  torfor-,  stem  o( C0rfui,  the  budy.     Der.  (from  L.  corpor) corporate,  corftor-e-ai  (L.  cer/ore-ut).  See.
corps,  corpse,  corse,  a  body.  (F.— L.)  Here  tvrps  is  mcM).  F. ;  fw«  is  fiom torpst  by  loss  of  /.  M.  E.  corps.  ••  O.  F. corfi,  con,  the  body.  —  L.  corpus,
corpulent.  ^F.-L.)  F.  corpuUnt.  — L.  corpu  Unttu,  fat.  —  L.  corpus.
corpUBola.  (L.)  L.  corpusculum^ double  dimin.  of  corpus.
cornet.  (F.  — L.)  F.  corset,  a  pair  of slays ;  dimin.  of O.  F.  cors,  body;  see  corps.
corslet.  (F.  -.  L.)  F.  corselet,  '  a  little body/  Cot. ;  hence  body  armour.  Double diroin.  of  O.  F.  con,  body  ;  sec  oorps.
Incorporate.    (L.)      L.   iruorpomtus,
Ep.  of  in-corporare,  to  furnish  willi  a  body ; ence  to  fonn  into  a  body.
Correct;  ^e  Bogont.
```


## [2026-09-06T22:23:23.865Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG car\"; grep -n \"^\\*čar\\|^\\*kar\\|\\*čar \\|\\*kar1\\|\\*kar 'to do\" CHEUNG.txt | head -20"
}
```


### [2026-09-06T22:23:23.916Z] TOOL RESULT

```
=== CHEUNG car
3287:*čar(H) and *gam! ? Rastorgueva — Edel’man (ESIJa П: 261 f.) cite a late Skt. form 
15502:*kar8/*xrah. 
15768:*kar ‘to do, make’ 
15819:*kar 237 
15919:*karé ? ‘to strike’ 
15927:*karH2 239 
15939:*kard ? ‘to stick, keep down ?’ 
15960:*karH! ‘to celebrate, praise’ 
15984:*karH ‘to spread out, scatter (esp. seed), sow; to make furrows, plough’ 
15989:*karaja- ~ *krsta- (i.e. root *kars-/*xrah-) in Pir. cf. Emmerick 1966: 612; Sims- 
16048:*kars/*xrah 241 
16074:*karp ? ‘to lament, moan, mumble’ 
16092:*kars/*xrah ‘to draw, plough’ 
16172:*kartl 243 
16180:*kars-/xrah- and *karH’- either show mutual influence, cf. Sh. kiräx(t), etc., or are 
16196:*kart! ‘to cut’ 
16271:*kart? ‘to twist, turn’ 
16305:*karz ? ‘to cheat, deceive’ 
55117:*kard (s.v.), *tund 
55142:*kar (s.v.), *pas (s.v.), *sam
```


## [2026-09-06T22:23:26.827Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15768,15820p' CHEUNG.txt; echo \"=== čar section\"; grep -n \"^\\*čar\" CHEUNG.txt | head; grep -n \"čar ‘to\\|char ‘to\" CHEUNG.txt | head"
}
```


### [2026-09-06T22:23:26.902Z] TOOL RESULT

```
*kar ‘to do, make’ 

*AVESTAN: kar- ‘to do, make’ || (+ *fra-) ‘perficere’ || (+ *ham-) ‘to perform a Yasna 
for someone’ = Liste: 14f. 

Pres. nu-: IND. 1sg. YAv. kerenaomi (V 21.6, V 21.10, V 21.14, Vyt 49), 25р. (?) YAv. kərənüši (Y 
10.13), 3sg. Y Av. koronaoiti (V 13.41, V 13.51, V 19.43, etc.), 3pl. YAv. "koronuuainti (Yt 13.26), impf. 
lsg. YAv. akoronom (V 22.1, V 22.8, V 22.14), impf. 2sg. Y Av. akoron(a)uuo (Y 9.15), impf. 3sg. (?) 
Y Av. frakoronaot (X3 V 22.2), INJ. 3sg. YAv. koronaot (V 2.32 f., V 2.36, V 2.38, etc.), SUBJ. 1sg. 
YAv. keronauuani (Yt 15.16, Yt 15.20, Yt 17.57, etc.), 3pl. OAv. koronaon (Y 30.9), 3pl. YAv. 
koronauuan (Yt 19.11), OPT. 3sg. YAv. kerenuiiat (V 14.17, V 18.10, VdPZ 18.51 f., Мр 14), YAv. 
koronoit (FrK 73), Y Av. frakoronoit (ViD 15), IMPV. 2sg. Y Av. koronüiói (Y 9.28), Y Av. koronauua (V 
2.25, V 2.28, У 2.30), impf. IND. 3sg. (?) YAv. frakoronaot (V 22.2); Aor. athem.: INJ. 3sg. OAv. cörot 
(Y 44.7, ? Y 45.9), SUBJ. 1sg. OAv. carani (Y 44.17), 3sg. OAv. caraiti (Y 51.1), OAv. carat (Y 46.4), 
OPT. 3sg. ? OAv. coirit (Y 45.9, Kellens — Pirart 1991: 193), IMPV. med. 250. OAv. korosuua (Y 40.1); 
Perf.: IND. 3pl. YAv. *caxrara (V 4.46); Partic.: pres. YAv. koronuuant- (Fr.), perf. pass. YAv. ?korota- 
(Y 26.9, Yt 10.128, V13.23, V 19.30), etc.; Pass.: pres. IND. 3sg. Y Av. kiriieiti (Yt 10.111), 3pl. ҮАУ. 
kiriieinti (V 3.9). © The form YAv. koronüsi can also interpreted as (emend.) med. 2sg. "koronüse, 
Hoffmann - Forssman 1996: 215. 

*OLD PERSIAN: kar- ‘to do, make, build’ — Kent: 179a 

Pres. nu- IND. 3sg. kunautiy <ku-u-n-u-ti-y> (DNb 24), <ku-u-n-u-[t]-[iJ-[y]> (DSs 3), 
<[ku]-[u]-[n]-u-t-i-y> (055 4), impf. lsg. akunavam <a-ku-u-n-v-m> (A’Sd 3), akunäm 
<[a]-[ku]-[n]-a-m> (XSc 3, ? A?Ha 5), ? akuvanasäsa <a-ku-v-n-8-a-8> (A’Sde 3), 3sg. akunaus 
<a-ku-u-n-u-8> (D'Sb 3), akunas <a-[ku]-u-n-8> (A’Sa 3 f), 3pl. akunava", med. 3pl. akunava"tà 
<a-ku-u-n-v-t-a> (DB 3.12, DSf 48), <a-[ku]-[u]-[n]-[v]-t-a> (DB 5.6), SUBJ. lsg. kunavanaiy 
<ku-u-n-v-a-n-i-y> (081 4), 2sg. kunavahy <ku-u-n-v-a-h-y> (DB 4.75, DB 4.79), med. 3sg. kunavätaiy 
<ku-u-n-..-v-a-t-i-y> (DNb 56), IMPV. 3sg. kunautuv <ku-u-n-u-tu-u-v> (DB 4.76); Aor. athem.: IND. 
med. 3sg. akuta <a-ku-u-t-a> (DB 1.47, CMb 4), I pl. akumä <a-ku-u-m-a-> (DB 1.90), IMPV. med. 2sg. 
kuSuva <ku-u-8-u-v-a> (DNb 50); Perf.: OPT. 35р. caxriyä <с-х-г-і-у-а> (DB 1.50); Partic.: perf. pass. 
karta-; Inf.: cartanaiy <c-r-t-n-i-y> (DB 1.94, DB 2.33, DB 2.44, etc.), <c-r-t-n-i-y> (2.38), <c-r-t-n-i-y> 
(DB 3.43, DB 3.65); Pass.: impf. IND. 3sg. akunavayatä <a-ku-u-n-v-y-t-a> (DB 1.20, DB 1.24, akariya 
<a-k-r-i-y> (DSf 37, XPh 42), 3р1. акагіуа"іа <a-k-r-i-y-t-a> (DB 3.92), OPT. 3sg. kariyais <k-r-i-y-i-8> 
(DNb 9, DNb 11) 

*MIDDLE PERSIAN: MMP kwn-, qwn-, BMP kwn- (‘BYDWN-) /kun-/ ‘to make, do’ || 
(+ *us-) BMP ’wsk’l- /uskar-/ (caus.) ‘to think, consider, discuss’ || (+ *pati-) BMP 
ptk’1/pahikar-/ (caus.) ‘to request, claim, consult, MMP phykr, BMP ptkl /pahikar/ 
‘picture, image’, MMP phyk’r, BMP рік? /pahikar/ ‘battle, struggle’ || (+ *ni-) 
MMP ng’r- (caus.) ‘to paint, draw’, MMP ner ‘picture’ || (+ *ui-) MMP w(y)c’r- 
(caus.) ‘to separate, divide, spread, interpret, decide....; perform, accomplish’ || (+ 
*ham-) MMP hng’r- (orig. caus.) ‘to (ac)count, reckon’, BMP hng’l- /hangär-/ ‘to 
perform, offer (thanks); calculate, determine; consider > DMMPP: 213b f., 275a, 
240b, 351b, 181a 

Widely attested: Pres.: IND. 1sg. MMP qwnym, "kwnym, 3sg. MMP kwnyd, etc.; Partic.: pres. MMP 
kwn'n, perf. pass. MMP qyrdg, MMP kyrd, дуга, Pass.: pres. IND. 3sg. MMP kyryhyd, 3р1. MMP 
qyryhynd, SUBJ. 3sg. MMP qyryh'd || (+ *us-) Caus.: pres. IND. 3pl. BMP ’wsk’lynd /uskarénd/, 


*kar 237 

=== čar section
3287:*čar(H) and *gam! ? Rastorgueva — Edel’man (ESIJa П: 261 f.) cite a late Skt. form
```


## [2026-09-06T22:23:33.302Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15820,15920p' CHEUNG.txt"
}
```


### [2026-09-06T22:23:33.352Z] TOOL RESULT

```
sk’lynynd /skarénénd/; Partic.: perf. pass. caus. BMP ’wsk’lt /uskard/ || (+ *pati-) Caus.: pres. IND. 3pl. 
BMP ptk’lynd /pahikarend/ || (+ *ni-) Pres.: IND. 3sg. MMP ng’ryd, 3р1. MMP ng rynd; Partic.: perf. 
pass. MMP ng’rd || (+ *ui-) Pres.: IND. 3sg. MMP we’ryd, IMPV. 2sg. MMP we’r, Partic.: perf. pass. 
MMP wyc’rd || (+ *ham-) Caus.: pres. IND. 35р. BMP hng’lyt /hangaréd/, 3р1. MMP hng’rynd, BMP 
hng’lynd /hangarénd/; Pass.: pres. IND. 3pl. MMP hng’ryhynd (M7983 I Vii,11); Partic.: perf. pass. BMP 
hng’It /hangard/ 

*PARTHIAN: kr- ‘to do, make’ || (+ *pati-) pdk’r- ‘to contend, strive’, pdkr ‘picture’ || 
+ *fra-) ? ‘frg’r- ‘to be dejected’ || (+ *ni-) ng’r- ‘to paint, draw’, ng’rgr ‘painter’ || 
(+ *ui-) wyc’r- ‘fulfil, perform’ = Ghilain: 57, 73 f. | DMMPP: 207 f., 269b, 85b, 
351b 

Pres.: IND. Isg. kr’m, 25р. qryh, 35р. kryd, qryd, 1р1. “kr’m, 2р1. Куа, 3р1. krynd, qrynd, SUBJ. 1sg. 
kr’n, 25р. kr’h, 3sg. kr’h, OPT. 25р. qryndyh, IMPV. 2sg. kr, 2pl. kryd; Partic.: perf. pass. kyrd; Inf.: 
kyrdn, qyrdn || (+ *pati-) Pres.: IND. 3pl. pdk’rynd || (+ *fra-) Pres.: IND. 1pl. ‘frg’r’m || (+ *ni-) Pres.: 
IND. 3sg. ng ryd || (+ *ui-) Pres.: IND. 25р. wyc ryy, 3sg. we’ryd, wyc’ryd 

*KHOTANESE: yan- “о do, make’ || (+ ui-) LKh. güjsar- ‘to harm, injure? = SGS: 
110 £, 29 

*SOGDIAN: SSogd. (k)wn-, BSogd. (k)wn-, CSogd. wn- ‘to do, make, perform, 
cause’, SSogd. (”)krt- (pass.) ‘to happen, occur; to become, be situated’ || (+ *pati-) 
BSogd. ptkr'k, ptkr'kw, ptkr'y, CSogd. ptq'ry (m.) ‘image’ || (+ *ui-) ? CSogd. 
wycyr’mnty (m.) ‘explanation’ (< Wir. ?), Sogd. w(y)c( rt ‘exactly’ 

Widely attested: Pres.: IND. 1sg. MSogd. kwn’m, 2sg. BSogd. wn’y, CSogd. "um, 3sg. SSogd. kwnty, 
BSogd. kwnty, MSogd. kwndyy, MSogd. qwndyy, etc. 

*CHORESMIAN: m/k- ‘to make, do’, (+ d") to say’ || (+ *abi-) ? m/’Bk’ry- ‘to look up’ 
|| (+ *pati-) pckr- (denomin. ?) ‘to set, put up (spear)’ || (+ *fra-) sk’ry- (caus.) ‘to 
colour, paint’ || (+ *ham-, *ni-) m/nk’ry- ‘to settle (a score) with someone; to say 
goodbye ?’. © The forms of m/k- with frequent diacritic tasdid | ] in Arabic script 
apparently point to assimilation of the consonant group *kn- (without *-r- !): > -kk-. 
|| Althought it is not entirely clear whether m/’Bk’ry- does contain the root *kar, the 
relation to Yi. uZér-/uZur, M. uZar-/uZir is surely undeniable, in view of the meaning. 
= Samadi: 94, 1, 141, 192, 128 

*BACTRIAN: к1р- ‘to do, act, make, etc.’ || (+ *pati-ham-) midayynp- ‘to agree, settle’ 
|| (+ *ui-) owonp- ‘to argue, quibble’ || (+ *ham-) ? ayyapyo, ayyapyo, ayyapayo 
‘property (in land), estate’. 0 Sims-Williams compares о1стр- with MMP w(y)c’r-, 
Sogd. w(y)c()rt. > S-W, Bact.: 199a, 177a, 217b, 213, 218a 

*NWIR: Widely attested: NP kardan/kun-, Bal. kan-/ku(r)t-, Kurd. (Kurm.) kirin/ki-, 
(Sor.) kirdin/ka-, Zaz. kerdis/ken-, Awrom. kardáy/kar-, Abyan. kardan/e-kar-, Anar. 
-ike/eker-, Ard. käd/ker-, Fariz. kärdän/-kär-, Yar. kärdän/-kor-, -kär-, Gz. ker-/ke-, 
kart, Gil. (Rsht.) kudoen/kun-, Gur. (Kand kärd-/-kär-, Ham. Кагійп/Кег-, Isfah. 
Кагійп/Кег-, Jow. bam-Ka/a-Ker-, Meim. bem-Ka/a-Ker-, Khuns. kir-/kirt, Khr. 
hi-kerd/hi-ker-, Mah. kir-/kär-d, Nn. kärtin/kir-, Natan. -kärd-/kor- (1sg.), kär-, 


| 


238 *karé ? 


Qohr. Ка(гаа)/Кег-, Semn. -kärd-, -kürc-/-kür-, Sang. hä-kärt-/hä-kän-, (subj.) 
hä-kär-, Shamerz. ha-kordan/ha-kon-, Siv. k(y)ar-, k(y)er-, kir-/k(y)erd, kird, Soi 
kärd-/kir-, Sorkh. ha-kärdan/hä-koen-, Lasg. hä-kärd-/hä-kän- ‘to do, make’, Kurd. 
(Kurm.) kärin/kär-, kanin/kan- (caus.) ‘to be able’, Awrom. kıriay/kıria- (pass.) ‘to 
be done’ || (+ *us-) NP sigälidan/sigäl- ‘to think, meditate (mischief)’ || (+ *pati-) NP 
paykar ‘picture, statue’ || (+ *ni-) NP nigastan/nigar- ‘to paint’ || (+ *ham-) NP 
ingastan/ingar- ‘to suppose; consider, believe’, angaridan/ angär- ‘to think, imagine, 
estimate; to paint, figure’, Yar. -hängäst/-hängar-, Jow. angor-/ (supplet. bam-vot < 
*yat), Meim. bem-henga:ft/a-heger-, Khuns. éngar-/engast, Nn. -Engäst/engar-, 
Natan. -hängäst ‘to talk, speak’, NP angärah ‘revenue-book, cash-account’ 

*NEIR: Oss. I. kenyn/kond, Купа, D. kanun/kond, kind, Pash. kawol, kral, Sh. (Baj.) 
kin-/Cüd, Rosh. kin-/ctig, Sariq. kan-/Cewg, Yzgh. k"on-/keg, Ishk. ken-/kül-, Yi. 
ken-/kor-, M. kan/ker- ‘to do’, Yghn. kün-/ikta, Wa. car-/kort ‘to do, make’, 
(redupl.) Wa. korc(o)r-, koc(o)r-/ke(r)kayn-, ko(r)cart- ‘can, to be able’ || (+ *abi, 
*aua- or *ui-) ? Yi. uZér-/uZur, M. uZar-/uZir ‘to perceive, look’ || (+ *ham-) ? Oss. I. 
enk’aryn/enk’ard (pref. sec. ?), D. ank’arun/enk’ard ‘to feel, comprehend’ (< NP 
?), Pash. angur ‘agreement’ 

*MISC: Par. kan-, kur-, kör, Orm. k-/dak ‘to do, make’ (< Pash. ?) = k-/däk, Orm. 
kin-/kinok, kin-/kwulak ‘to copulate’ (euphem.) = kan-/kanók 

*SANSKRIT: kar ‘to do, to make, to act’ (RV+) = EWAia I: 307 

© The rather generic ‘to do, make’ has apparently developed into more specific 
activities, ranging from “painting, depicting’ to ‘arguing, fighting’. 

*PIE *k”er- ‘to do, make, construct’? = LIV: 391 | Pok.: 641 

*IE COGNATES: Hitt. /kuer-/ ‘to cut’, Welsh paraf ‘to process’, Olrish cruth ‘form’, 
Lith. kung (kürti) ‘I found, build’, etc. 

*REFERENCES: KPF I: 82b, 143b f., 207b f., 247b f.; Ivanow 1926: 420, 426; EVP: 34; KPF II: 207 f.; 
IIFL 1. 266a f., 398a f.; Christensen, Contributions I: 71, 168 f., 261; Christensen, Contributions II: 60 f., 
116 f., 161; Abrahamian 1936: 116, 130; IIFL II: 196, 217b; Lambton 1938: 42b, 78a; Abaev, Slovar’ I: 
579; Andreev — PeSéereva: 275b ff.; MacKenzie 1966: 100; EVS: 40b; Lecoq 1974: 58; WIM I: 70; WIM 
H/1: 78; WIM Ш: 110 £; Werba 1997: 168 f.; Paul 1998: 303; Steblin-Kamenskij 1999: 112, 218; 
Cabolov 2001: 518, 514 f.; Lecoq 2002: 108 f., 138 ff. (passim); Kiefer 2003: 199; Korn 2005: 314, 393 
(passim) 


*karé ? ‘to strike’
```


## [2026-09-06T22:25:51.986Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk -v RS='\\f' 'NR==8079||NR==8080{print NR\": \"substr($0,1,400)}' HUB.txt 2>/dev/null | head -5; echo \"--- find leaf of line 8069\"; awk 'NR<=8069' HUB.txt | grep -c $'\\f'"
}
```


## [2026-09-06T22:25:52.864Z] TOOL CALL #71: Bash

```json
{
 "command": "for pp in \"1809 606\" \"1814 611\"; do set -- $pp; echo \"###### BQT:$1 (pdf $2)\"; python3 tools/ref_page.py BQT:$1 --pdf-page $2 2>&1 | head -14; done"
}
```


### [2026-09-06T22:25:53.658Z] TOOL RESULT

```
--- find leaf of line 8069
228
```


### [2026-09-06T22:25:55.177Z] TOOL RESULT

```
###### BQT:1809 606 (pdf )
expected ABBR:page (e.g. BQT:918 or MON5:528)
###### BQT:1814 611 (pdf )
expected ABBR:page (e.g. BQT:918 or MON5:528)
```


## [2026-09-06T22:26:02.206Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==229' HUB.txt | head -12"
}
```


## [2026-09-06T22:26:03.007Z] TOOL CALL #73: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1809 --pdf-page 606 2>&1 | head -12; echo \"#####\"; python3 tools/ref_page.py BQT:1814 --pdf-page 611 2>&1 | head -12"
}
```


### [2026-09-06T22:26:03.976Z] TOOL RESULT

```
— 218 —
Nach i und u wird idg. sv zu ap. siw (vgl. ap. pdti-
suvaris) = np. sv oder durch Einftihrung von x^ aus den
Formen, die mit x^ anlauten, sx^: dusvar schwierig = arm.
d^var, zd. dus + x^a&ra-, dann im Gegensatz zu x^ar
leicht': dusx^dr (vgl. § 96, b); Obisx^ar *Tranke' (oben p. 5),
vgl. zd. aiwisx^ared^a- geniessbar , dusx^ared-a-f dusx^arenah-
u. s. w.
In den arm. LW. wird x^d- durch xo- wiedergegeben :
xostak *Besitz* = phi. x^astak; xortik-U ^Speisen = phi.
x^artik, np. x^ardl, zd. x^areti- u. s. w., ebenso in Namen:
Xofeam = pers. Xorahdn, gr Xopidvf^g, Xmgtuvrjg Tab. 292
```


### [2026-09-06T22:26:05.843Z] TOOL RESULT

```
REF: BQT:1809  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 604  OCR-lang: fas

۱۸۰۷ کربوه
کشیده و بفین نقطه‌دار زده » بمعنی گریز است گریودوم ؟ - بنتح اول و ثانی
که ا زکربختن باشد . بتحتانی رسیده و بواو زده وضم دال و سکون‌واو
گریفتن ۱ - بافا . بر وزن و معنی ومیم » بمعنی خیانت باشد و آن ودیمت‌راخیات
گربختن است (۱) کردن و آنکار نمودن است .
بسن است ۰ گربون * م۱ ی ۰
۳ ۰ « قح اول بروزن پریزن»
گریگاه ؟ - بکس اول . در دیگه علتی است که آترا بپندی داد و بعربی قوبا
بربان پلاوجاییر! گوبند که‌محاذی کردن گوسفند گوبند ‎..٩‏
‏ن باشد #۰
#####
REF: BQT:1814  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 609  OCR-lang: fas

کزف ۱۸۱۳۳
وآن‌کز در ولاییت خرامان رواج دارد . درخت کز را کوبند وبعریی طرفا خوانند 8 .
گزف ۱« بنتح اول و سکون قانی وفاء گزماز ك ۱ « بفتح اول وسکون‌انی
بمعنی قیرباشد وآن صدفی است‌سیا هکه‌برکشتی | و میم بالف کشیده و زای قطه‌دار مفتوح بکاف
رجهازمالند وسیم سوخته را نیز کوبند- وسواد | زده, بارومیوة درخت کزرا میگوبند (۱)ومعرب
زر گربراهم گفته‌اند؛ وجضم اول نیز بنظرآمده‌است | آن جزمازج است و بمریی "ثمرة الطرفا خوانند
وبا زای فارسی هم هست . وحص‌الانل همان است با ای مثلثه .
گزل 4 - بر وزن نسکه .هر چیز که گزمازو ۷ - بر وزن شفتالو : بممنی
بدان تفیدر ذائلقه کنند ۴ - و سرمازده رانیز | گزمازك است که موه درخت کز باشد .
کوبند ۴ . گز ملك بکسرئانی وض‌ثالث‌وسکون
```


## [2026-09-06T22:26:17.710Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8060,8075p' HUB.txt"
}
```


### [2026-09-06T22:26:17.752Z] TOOL RESULT

```
*ein Mass fiir Getreide*, ap. xani&i^ (oben p. 89); gudazam
*schmelze', zd. vi-tac-^ gurezam 'fliehe', zd. vi-ric; giizaram
'vollziehe, bezahle' =^ arm. vcareni, skr. vi-car; guzinam 'suche
aus*, zd. vi'Ci ; guzlr 'Hilfsmittel' = "^vicfya- (oben p. 94) ;
maztdan 'saugen , bal. micag 'saugen ; maviz ^) 'Rosinen' =
hdX.mamc (Geiger, Lautlehre p. 28); moza *Schuh' = arm.
mucak 'kleiner Schuh' ; namaz *Gebet' aus '^namac H. 1040, oben
p. 102 ; namzam 'spiele' (ein Instrument) H. 1046, unsicher,
oben p. 102; ciz etwas aus *czc = *acc, urspr. "^cid-cid,
ap. cisciy; vazlr (arab. LW.) 'Vezir', zd. vlcira- *der die
Entscheidung hat', phi. v{i)c%r , arm. vcir 'Entscheidung,
Richterspruch' (oben p. 94), vgl. Noldeke, Tab. 53, 444;
dihltz, dahliz 'Vorhalle, Halle* = arm. dahlic 'Zelle' (5. Jhd.),
s. p. 263; Vahriz N. pr. Tab. 223 — arm. Vahric (Laz.
Pharp.); Suff. zi in sagzt 'Sake' (s. p. 240), razT Von Rai'
(davon 'Pa^inrfvrj 'Rai' bei Theophylact), tctzi 'arahiscli =
```


## [2026-09-06T22:26:20.117Z] TOOL CALL #75: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B3%D8%A7%D9%86%D8%B3%DA%A9%D8%B1%DB%8C%D8%AA/",
 "prompt": "What do Dehkhoda / Mo'in say about the Persian word سانسکریت (or سنسکریت)? Give the definition and any note on its origin (Sanskrit saṃskṛta, meaning 'perfected/put together')."
}
```


### [2026-09-06T22:26:27.422Z] TOOL RESULT

```
# Dehkhoda and Mo'in on سانسکریت

**Dehkhoda's Definition:**
According to Lughati-nama Dehkhoda, the entry simply states: "سانسکریت. ( اِخ ) رجوع به سنسکریت شود" — it directs readers to consult the entry for سنسکریت (alternate spelling).

**Mo'in/Farhangi Farsi's Definition:**
This source provides extensive detail, describing it as "زبان علمی قدیم و مقدس هندوان" (an ancient scientific and sacred language of Hindus). The entry characterizes Sanskrit as one of the important Indo-European languages, closely related to Avestan, and notes its role as the language of Vedic texts and Hindu civilization.

**Origin Note:**
Neither classical dictionary entry explicitly discusses the Sanskrit etymology (saṃskṛta). However, the Farhangi Farsi emphasizes Sanskrit's status as a refined, scholarly language tied to the Vedas and Hindu intellectual traditions, suggesting recognition of its cultivated nature without stating the literal meaning of the Sanskrit root.
```


## [2026-09-06T22:26:38.028Z] TOOL CALL #76: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D8%B3%D8%A7%D9%86%D8%B3%DA%A9%D8%B1%DB%8C%D8%AA/' --note 'page 293, root Kwer 2 node 6, Persian sanskrit/sanskrit entry in Dehkhoda + Farhang-e Moin' 2>&1|tail -1"
}
```


### [2026-09-06T22:26:41.818Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/9ea86e225f678049.txt
```


## [2026-09-06T22:34:30.797Z] TOOL CALL #77: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-293.json << 'JSONEOF'\n{\n  \"pdf_page\": 293,\n  \"book_page\": 263,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Kwer, Qwer\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *kʷer- 'to do, to make, to build' (Pokorny 641-642 kʷer-1 'to do'; LIV² 391 *kʷer- '(ab)schneiden, schnitzen'; Watkins/AHD kʷer-1 'To make')\",\n      \"note\": \"Pokorny's lemma kʷer-1 (pp. 641-642) collects exactly the material Nourai puts in this chart: Old Indic karóti / kṛṇóti 'does, accomplishes', ptc. kṛtá-, sam-kṛt, and with s-mobile pari-skar-, sam-skar-; Avestan kərənaoiti, OP akunavam, karta-; and 'Avestan čārā 'tool, aid', np. čār 'tool', čāra 'tool, help, artifice''. AHD (Watkins) has 'kʷer-1. To make. 1. Sanskrit karoti, he makes: SANSKRIT ... 4. Suffixed form *kʷer-mn̥ in Sanskrit karma ... [Pok. 1. kʷer- 641]'. Cheung, Etymological Dictionary of the Iranian Verb, s.v. *kar 'to do, make', gives PIE *kʷer-, Pok. 641, and — decisively for this chart — files the *ui- compound there: MMP/BMP w(y)cʾr- (caus.) 'to separate, divide, interpret, decide ...; perform, accomplish', Parthian wycʾr-, Sogdian (ʾ)krt-. Language label (Indo-European) and gloss (to make, form) are both right. 'PART 2' marks the second half of a root whose chart is split over two pages. The one thing the chart does not say, and Klein does (s.v. corpus, p. 355), is that the root of the next entry, *kʷrep- 'body', is itself an enlargement of this root — so entries 0 and 1 on this page are ultimately the same root.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *kʷer- «کردن، ساختن، پرداختن» (پوکورنی، ص ۶۴۱-۶۴۲؛ واتکینز در پیوست AHD؛ LIV ص ۳۹۱). بازساخت، برچسب زبانی و معنای پیشنهادی نورایی هر سه درست است: پوکورنی زیر همین سرواژه سنسکریت karóti و kṛtá- و sam-kṛt، اوستایی kərənaoiti، پارسی باستان akunavam / karta- و نیز اوستایی čārā «چاره، وسیله» و فارسی čār / čāra را گرد آورده است. چونگ نیز در فرهنگ ریشه‌شناختی فعل ایرانی، ذیل ستاک *kar «کردن»، همین ریشه را با ارجاع به پوکورنی ۶۴۱ می‌آورد و — که برای این نمودار مهم است — فعل پیشوندی *ui-kār- (فارسی میانهٔ wizārdan / wizīr) را هم به همین ستاک بازمی‌گرداند. تنها نکتهٔ ناگفته آن است که کلاین ریشهٔ مدخل بعدی همین صفحه (*kʷrep- «تن») را گسترش‌یافتهٔ همین ریشه می‌داند.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/kʷer-\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:641\", \"status\": \"supports\", \"note\": \"POK_full.txt (grep 'Page(s): 641'): 'Root / lemma: kʷer-1 ... Meaning: to do. Material: Old Indic karoti (Imper. kuru), kṛṇoti 'does, accomplishes' ... sam-kṛt; besides with s- pari-skar- and sam-skar-. Avestan kərənaoitī 'makes, performs, acts' ... Avestan čara 'tool, aid', np. čar 'tool', čara 'tool, help, artifice' ... References: WP. I 517 f. Page(s): 641-642.' Exactly the root, label and gloss Nourai gives.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I 517 (WLD_Bd1_1930_dli_70244_djvu.txt l.32579)\", \"stance\": \"supports\", \"note\": \"'1. qʷer- „machen, gestalten“, vielleicht ursprünglich von irgendeiner nicht mehr bestimmbaren Handwerkstätigkeit. Ai. karoti ... av. kərənaoiti ... av. čārā „Mittel, Hilfsmittel“, np. čār „Mittel“, čāra „Mittel, Hilfe, List“ (Bthl. Wb. 584)'.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. kʷer-1\", \"stance\": \"supports\", \"note\": \"'kʷer-1. To make. 1. Sanskrit karoti, he makes: SANSKRIT ... [Pok. 1. kʷer- 641.]' — the same root, gloss and Pokorny page.\"},\n        {\"src\": \"CHEUNG\", \"where\": \"s.v. *kar 'to do, make' (CHEUNG.txt l.15768-15915)\", \"stance\": \"supports\", \"note\": \"'*PIE *kʷer- ‘to do, make, construct’? = LIV: 391 | Pok.: 641'; under Middle Persian: '(+ *ui-) MMP w(y)cʾr- (caus.) ‘to separate, divide, spread, interpret, decide....; perform, accomplish’', under Sogdian 'SSogd. (ʾ)krt- (pass.)'.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"čâra; vi-čir\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Both words belong to this root, but Nourai's glosses are wrong in part of speech. Av. čārā- is a feminine NOUN, not a verb 'to mediate': Bartholomae AiW col. 584 has 'j. čārā- f. „Mittel, Hilfsmittel“' (means, remedy), and Pokorny 641 and Walde-Pokorny I 517 both file it under *kʷer- beside np. čār 'tool' and čāra 'tool, help, artifice'. Phonetically it is a lengthened-grade *kʷēr-eh₂-, with the Indo-Iranian palatalisation *kʷ > č before the front vowel *e. Av. vīčira- is an adjective 'deciding, one who decides, arbitrator' (AiW col. 1438), vi- 'apart, asunder' + the same root in its Iranian shape kar-/čar-; the corresponding verb is the *ui- causative *ui-kāraya- 'to separate, decide, interpret, perform', which Cheung files squarely under *kar 'to do, make' = PIE *kʷer- (MMP w(y)cʾr-, Parth. wycʾr-, Sogd. wyc(y)rʾmnty 'explanation'). Two reservations keep this from 'confirmed': Pokorny's article at 641 cites only čārā, not vīčira-, and Nyberg (Manual of Pahlavi II, s.v. vicīr) explicitly detaches Av. vīčira- from the Middle Persian wizīr group, which he derives from *vi-cṛna- (Skt. cīrṇa-, ptc. of car-).\",\n          \"derivation_fa\": \"هر دو واژه به همین ریشه بازمی‌گردند، اما معنای نورایی از نظر مقولهٔ دستوری دقیق نیست. اوستایی čārā- اسم مؤنث است به معنی «چاره، وسیله، دستاویز» (بارتولمه، ستون ۵۸۴) نه فعلِ «میانجیگری کردن»؛ پوکورنی (۶۴۱) و والده-پوکورنی (ج ۱ ص ۵۱۷) آن را کنار čār و čāra فارسی زیر همین ریشه آورده‌اند. از نظر آوایی صورت *kʷēr-eh₂- است با کشش واکه و ابدال *kʷ به č در برابر واکهٔ پیشین (همگونی کامی هندوایرانی). اوستایی vīčira- صفت است به معنی «تصمیم‌گیرنده، داور» (بارتولمه، ستون ۱۴۳۸)، از پیشوند vi- و همان ریشه به صورت kar-/čar-؛ چونگ فعل پیشوندی *ui-kāraya- «جدا کردن، تصمیم گرفتن، تفسیر کردن، به‌جا آوردن» را قاطعانه زیر ستاک *kar می‌گذارد (فارسی میانهٔ w(y)cʾr-، پارتی wycʾr-، سغدی wycyrʾmnty «شرح»). دو ملاحظه مانع از «تأیید کامل» است: خودِ پوکورنی در ص ۶۴۱ فقط čārā را می‌آورد نه vīčira- را، و نیبرگ صریحاً vīčira- اوستایی را از گروه wizīr فارسی میانه جدا می‌کند و آن را از *vi-cṛna- می‌گیرد. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/kʷer-\",\n            \"https://en.wiktionary.org/wiki/چاره\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:641\", \"status\": \"partial\", \"note\": \"POK_full.txt kʷer-1: 'Avestan čara 'tool, aid', np. čar 'tool', čara 'tool, help, artifice' (= Slavic čara 'charm, spell')' — supports čāra, but the article says nothing about vi-čir / vīčira-.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"col. 584 (BRT.txt l.11272)\", \"stance\": \"supports\", \"note\": \"'• j. čārā- f. „Mittel, Hilfsmittel“' — a noun 'means, remedy', not a verb; Nourai's gloss 'to mediate' is loose.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 517\", \"stance\": \"supports\", \"note\": \"'av. čārā „Mittel, Hilfsmittel“, np. čār „Mittel“, čāra „Mittel, Hilfe, List“ (Bthl. Wb. 584)' under qʷer- „machen, gestalten“.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"s.v. *kar, Middle Persian / Parthian sections\", \"stance\": \"supports\", \"note\": \"'(+ *ui-) MMP w(y)cʾr- (caus.) ‘to separate, divide, spread, interpret, decide....; perform, accomplish’ ... PARTHIAN (+ *ui-) wycʾr- ‘fulfil, perform’' — the vi-čar- family is under *kar = PIE *kʷer-.\"},\n            {\"src\": \"NYB\", \"where\": \"vol. II Glossary s.v. vicīr\", \"stance\": \"partial\", \"note\": \"'vicīr ... ‘decree, judgment, sentence’ shows through its -r- < -rn- that the OIr form was *vicirna- < *vicṛna-, cf Skr cīrṇa-, ptc. of car-. — NP guzir(ah) ‘help, remedy’. [Av. (1438) vicira- ‘he who decides’ does not belong to this group.]' — Nyberg separates the Avestan adjective from the MP noun.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"čâreh «چاره»; vačar «وچر»; gozîr «گزیر ( ناگزیر )»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"چاره: from MP čārag [cʾlk'] 'means, remedy' (MacKenzie, CPD p. 21; Nyberg II 'cārak remedy, expedient, means ... NP čārah'), a -ag derivative of MP čār < Av. čārā-; MP final -ag > NP -a/-e regularly (čārag > čāra). وچر: Borhān-e Qāṭeʿ p. 2258 has وجر / وچر 'فتوی ... دستور حاکم شرع', and Moʿin's footnote there says outright 'در اوستا vīčira- بمعنی فتوی‌دهنده است. از همین لغت است کلمهٔ «وزیر» که عرب از ایرانی به عاریت گرفته'; the immediate source is MP wizīr [wcyl] 'decision, judgement' (MacKenzie p. 92), and Nyberg notes that 'BQ quotes NP vajar, vačar ‘judicial decree’ from the legal language, probably from Zoroastrian usage'. گزیر / ناگزیر: MP wizīristan, wizīr- 'to be able to dispense with, avoid' and a-wizirišnīg 'unavoidable, inevitable' (MacKenzie pp. 15, 92) give NP gozīr and nā-gozīr, with the regular Middle Persian w- > New Persian gu-/go- before -i (wizīr > gozīr, cf. wizārdan > gozārdan, wizīdan > gozīdan). Horn no. 919 (p. 205) has 'guzīr „Hilfsmittel“ ... Etwa *vičārya-, vergl. skr. vi + √car- „ausführen, vollführen“', and Hübschmann p. 218 has 'guzīr „Hilfsmittel“ = *vičṛya-' in the same list as 'guzāram „vollziehe, bezahle“'. All three words are therefore correctly hung under the Avestan node.\",\n          \"derivation_fa\": \"«چاره» از فارسی میانهٔ čārag «چاره، درمان» (مکنزی ص ۲۱؛ نیبرگ: cārak ... NP čārah)، خود ساختهٔ čār + پسوند -ag، و -ag پایانی فارسی میانه در فارسی نو به -ه بدل شده است. «وچر»: در برهان قاطع ص ۲۲۵۸ مدخل «وجر / وچر» به معنی فتوی و دستور حاکم شرع آمده و معین در حاشیه می‌نویسد «در اوستا vīčira- بمعنی فتوی‌دهنده است؛ از همین لغت است کلمهٔ وزیر که عرب از ایرانی به عاریت گرفته»؛ صورت میانجی فارسی میانهٔ wizīr «رأی، داوری» است (مکنزی ص ۹۲) و نیبرگ آن را اصطلاحی از زبان حقوقی زردشتیان می‌داند. «گزیر / ناگزیر» از فارسی میانهٔ wizīristan / wizīr- «توانستن چشم پوشید، گریز داشتن» و a-wizirišnīg «ناگزیر» است، با تحول قاعده‌مندِ w- فارسی میانه به گـ در فارسی نو (wizīr > گزیر، چنان‌که wizārdan > گزاردن و wizīdan > گزیدن). هرن (شمارهٔ ۹۱۹، ص ۲۰۵) و هوبشمان (ص ۲۱۸) هر دو گزیر را به *vičārya- / *vičṛya- بازمی‌گردانند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/چاره\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"HRN:205\", \"status\": \"supports\", \"note\": \"Horn, Grundriss, p. 205 no. 919 (HRN.txt leaf 227): 'guzīr „Hilfsmittel“, guzīrden (Šāhn. I, 61 Vers 519), guzēr, guzērden; vergl. nāguzīr. Etwa *vičārya-, vergl. skr. vi + √car- „ausführen, vollführen“. Hat mit rezīr (No. 1084) nichts zu tun.'\"},\n            {\"ref\": \"HRN:242\", \"status\": \"supports\", \"note\": \"Horn p. 242 no. 1084 'vezīr (arab. LW.) „Vezir; Gelehrter“, gezīr, gizīr', continued on p. 243: 'aw. vīčira- „Entscheider“; phlv. v(i)čīr „Entscheidung; Entscheider, Richter“; arm. LW. včir „Entscheidung“' — the Avestan etymon Nourai draws the arrow from.\"},\n            {\"ref\": \"BQT:2258\", \"status\": \"supports\", \"note\": \"ref_page.py BQT:2258 (v4 pdf p. 341): headwords 'وجر ... بمعنی فتوی باشد' and 'وچر ... بمعنی فتوی باشد و آن دستور حاکم [شرع]'; footnote 4: 'در اوستا vīčira- بمعنی فتوی دهنده است. از همین لغت است کلمهٔ «وزیر» که عرب از ایرانی بعاریت گرفته'.\"},\n            {\"ref\": \"BQT:1778\", \"status\": \"not_found\", \"note\": \"ref_page.py BQT:1778 (v3 pdf p. 575, exact page map) prints the 'بیان هشتم در کاف فارسی با ذال نقطه‌دار' section: گذاردن، گذارش، گذاشتن، گذرنامه، گذشت. No چاره / وچر / گزیر entry; Moʿin's footnote there derives گذاشتن from Phl. vitārtan, Av. vi-tar-, and cross-refers to گزاردن. Possibly Nourai meant the گزاردن cross-reference.\"},\n            {\"ref\": \"BQT:1809\", \"status\": \"not_checked\", \"note\": \"The v3 scan has no exact page map above p. 1778; rendering with the offset gave printed p. 1807 (گریختن، گریوه، گریواره), i.e. the local offset is about two pages short, so the exact printed 1809 could not be landed on. It falls in the گر/گز section, a couple of pages before گزیر.\"},\n            {\"ref\": \"BQT:1814\", \"status\": \"not_checked\", \"note\": \"Same offset problem: the render gave printed p. 1813 (گزف، گزل، گزلک، گزمازک، گزند). گزیر follows within two or three pages, so the citation is in the right neighbourhood but could not be verified line by line.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"p. 21 s.v. čārag; p. 92 s.v. wizīr, wiziristan; p. 15 s.v. a-wizirišnīg\", \"stance\": \"supports\", \"note\": \"'čārag [cʾlk' | N ~a] means, remedy'; 'wizīr [wcyl] decision, judgement'; 'wiziristan, wizīr- [wcyl-stn' | J bzyr-, N guzīr-] be able to dispense with, avoid'; 'a-wizirišnīg [ʾwcylšnyk'] unavoidable, inevitable'.\"},\n            {\"src\": \"NYB\", \"where\": \"vol. II Glossary s.v. cārak, vicar\", \"stance\": \"supports\", \"note\": \"'cārak remedy, expedient, means ... Paz. cāraa (SGV), NP cārah'; 'vicar decision, decree 818 ... BQ quotes NP vajar, vacar ‘judicial decree’ from the legal language, probably from Zoroastrian usage. OIr *vi-cara- from vi-+car- ... Cf also NP guzar, guzir ‘remedy, help’.'\"},\n            {\"src\": \"HUB\", \"where\": \"p. 218 (HUB.txt leaf 229)\", \"stance\": \"supports\", \"note\": \"'guzāram „vollziehe, bezahle“ = arm. včarem, skr. vi-car; ... guzīr „Hilfsmittel“ = *vičṛya- (oben p. 94)'.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Arabic\",\n          \"words\": \"\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"A pass-through box: the unnamed Arabic word is وزير wazīr 'helper, assistant; minister'. Nourai's arrow (Avestan > Arabic) is the Iranianist account, and it has good modern backing: Wiktionary's Arabic entry says 'The original attested meaning is “assistant”, and the political sense only arose in the Umayyad period. Likely related to the verb وَزَرَ “to carry, to shoulder” ... but owing to the idea of assistance by handmen this may be denominal. Likely borrowed from an Iranian term surfacing as Pahlavi wcyl /vičīr/ “decision, judgment”, Avestan vīcira “arbitrator, judge”, Armenian վճիռ' (citing Cheung's Arabic-Iranian loan study 19-20 and Eilers 1962: 216-218). Asbaghi, Persische Lehnwörter im Arabischen, no. 23, is unambiguous: 'wazīr: „Minister“ mp. wicir, aw. vicira, air. *vicirna'. Against this stand the Arabic philologists and Lokotsch no. 2160, who derive wazīr entirely within Arabic from wazara 'to carry', 'weil der erste Minister die Lasten trägt, die eigentlich dem Herrscher aufgebürdet sind'. Since the Semitic derivation is morphologically impeccable (faʿīl of a real root) and the Iranian one rests on a semantic and formal near-match, the honest verdict is plausible, not confirmed. The chart's silence about the Arabic form itself (the box has no word) is an extraction-faithful reproduction of an empty box in the book.\",\n          \"derivation_fa\": \"این جعبه گذرگاهی است و واژهٔ عربی ناگفتهٔ آن «وزیر» است. پیکان نورایی (اوستایی ← عربی) همان دیدگاه ایران‌شناسان است و پشتوانهٔ امروزی دارد: ویکی‌واژه در مدخل عربی وزير می‌نویسد که معنای کهن آن «دستیار» بوده و معنای سیاسی‌اش در دورهٔ اموی پیدا شده، و آن را «به احتمال زیاد وام‌گرفته از واژه‌ای ایرانی» می‌داند که در فارسی میانه wičīr «رأی، داوری» و در اوستایی vīcira «داور» و در ارمنی վճիռ نمود یافته است. اصبغی نیز در «وام‌واژه‌های فارسی در عربی» (شمارهٔ ۲۳) می‌نویسد: wazīr از فارسی میانهٔ wičir، اوستایی vicira، ایرانی باستان *vicirna. در برابر، لغویان عرب و لوکوچ (شمارهٔ ۲۱۶۰) آن را از ریشهٔ عربی «وزر» (بار برداشتن) می‌گیرند، که از نظر صرفی بی‌عیب است. پس ادعای نورایی با احتیاط پذیرفتنی است، نه قطعی.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/وزير\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"The node carries refs=None in the book; nothing to check. The claim was tested against Asbaghi (PLA), Hübschmann, Lokotsch and Wiktionary instead — see consulted.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PLA\", \"where\": \"no. 23 (PLA_asbaghi_1988_ia_djvu.txt l.19721)\", \"stance\": \"supports\", \"note\": \"'23 - wazīr: „Minister“ mp. wicir, aw. vicira, air. *vicirna' — Asbaghi lists wazīr among the Persian loanwords in Arabic, with exactly Nourai's Avestan etymon.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 2160 (LKT.txt l.4835)\", \"stance\": \"contradicts\", \"note\": \"'„Erster Minister, Regent“ [vom Vb. wazara „tragen“, weil der erste Minister die Lasten trägt, die eigentlich dem Herrscher aufgebürdet sind; andere von ar. Philologen gegebene Ableitungen s. De Sacy ...]' — Lokotsch keeps the word wholly Arabic.\"},\n            {\"src\": \"HUB\", \"where\": \"p. 218\", \"stance\": \"supports\", \"note\": \"'vazīr (arab. LW.) „Vezir“, zd. vīcira- „der die Entscheidung hat“, phl. v(i)čīr, arm. včir „Entscheidung, Richterspruch“' — Hübschmann treats the Arabic word as the Iranian one.\"},\n            {\"src\": \"AFM\", \"where\": \"AFM.txt (grep وزير)\", \"stance\": \"silent\", \"note\": \"Addi Shir's Alfāẓ al-fārisiyya al-muʿarraba has no headword وزير; the only hit is an incidental mention of الوزير نظام الملك. He does not list it among the Persian arabicisms.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"vazîr «وزیر»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian وزیر is a borrowing back from Arabic wazīr, i.e. an Arabic-mediated round trip: Middle Persian wizīr 'decision, judgement; judge' > Arabic wazīr (reshaped to the faʿīl pattern and attached to the Arabic root و ز ر) > New Persian vazīr. Horn no. 1084 flags it as 'vezīr (arab. LW.)' while still giving the Avestan/Pahlavi etymon on the next page, and Hübschmann p. 218 does the same. Moʿin's footnote at Borhān-e Qāṭeʿ p. 2279 s.v. وزیر states it in so many words: 'کلمه معرب است ... از vičīr پهلوی ... از اوستایی vīčira- فتوی‌دهنده (پورداود، خردهٔ اوستا ص ۷۸)؛ ارمنی včir ... فارسی vazīr (دهخدا: ریش‌سفید ده، محصل مالیات)؛ اسپانیایی alguazil'. The inherited (non-borrowed) Persian outcome of the same Middle Persian word is گزیر in node 2 — vazīr and gozīr are therefore doublets, one via Arabic and one direct.\",\n          \"derivation_fa\": \"«وزیر» فارسی نو وام‌واژه‌ای است از عربی، یعنی نمونهٔ روشن یک رفت‌وبرگشت: فارسی میانهٔ wizīr «رأی، داوری، داور» ← عربی وزير (که در قالب فعیل ریخته و به ریشهٔ «و ز ر» بسته شد) ← فارسی نو وزیر. هرن (شمارهٔ ۱۰۸۴) آن را «وام‌واژهٔ عربی» می‌نامد و در همان حال ریشهٔ اوستایی vīčira- و پهلوی wičīr را می‌آورد، و هوبشمان (ص ۲۱۸) نیز چنین می‌کند. معین در حاشیهٔ برهان قاطع ص ۲۲۷۹ می‌نویسد: «کلمه معرب است ... از vičīr پهلوی ... از اوستایی vīčira- فتوی‌دهنده (پورداود، خردهٔ اوستا ص ۷۸)». نکتهٔ درخور توجه آنکه بازماندهٔ مستقیم و بی‌واسطهٔ همان واژهٔ فارسی میانه در فارسی «گزیر» است؛ پس «وزیر» و «گزیر» دوگانه (doublet) اند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/وزير\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:2279\", \"status\": \"supports\", \"note\": \"ref_page.py BQT:2279 (v4 pdf p. 362), entry وزیر, footnote 7: 'کلمه معرب است «اسشق ...» از vičīr پهلوی «بارتولمه ۳۳۶» از اوستایی vīčira- فتوی دهنده؛ پورداود، خردهٔ اوستا ص ۷۸؛ ارمنی včir ... فارسی vazīr (دهخدا، ریش‌سفید ده، محصل مالیات)، اسپانیایی alguazil (ژاندارم)'. Exactly Nourai's arrow.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"p. 242-243 no. 1084\", \"stance\": \"supports\", \"note\": \"'vezīr (arab. LW.) „Vezir; Gelehrter“ ... aw. vīčira- „Entscheider“; phlv. v(i)čīr „Entscheidung; Entscheider, Richter“; arm. LW. včir'.\"},\n            {\"src\": \"PHD\", \"where\": \"p. 92 s.v. wizīr\", \"stance\": \"supports\", \"note\": \"'wizīr [wcyl] decision, judgement' — the Middle Persian source form; MacKenzie's index also gives 'decision wizārišn, wizīr' and 'judgement ... wizīr'.\"},\n            {\"src\": \"PLA\", \"where\": \"no. 23\", \"stance\": \"supports\", \"note\": \"'wazīr: „Minister“ mp. wicir, aw. vicira, air. *vicirna'.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"sams-krta\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sanskrit saṃskṛtá- 'put together, well-formed, perfected, consecrated, refined' = sam- 'together' (PIE *sem-) + s-mobile + kṛtá- 'made, done', the past passive participle *kʷr̥-tó- of karóti. Pokorny 641 lists the compound in the article itself ('sam-kṛt; besides with s- pari-skar- and sam-skar-'), and AHD's kʷer-1 entry gives the English derivative SANSKRIT under 'Sanskrit karoti, he makes'. The parasitic -s- of sam-s-kṛta- is the well-known Old Indic s-insertion after sam- and pari- before kar-. Nourai's gloss 'worked before, prepared' misreads sam- 'together' as 'before'; the standard rendering is 'put together, perfected'.\",\n          \"derivation_fa\": \"سنسکریت saṃskṛtá- «به‌هم‌برنهاده، به‌کمال‌رسیده، پیراسته، تقدیس‌شده» مرکب است از پیشوند sam- «با هم» (هندواروپایی *sem-)، «س» میانجی، و kṛtá- «کرده»، صفت مفعولی ریشهٔ kar-/*kʷr̥-tó-. خودِ پوکورنی در ص ۶۴۱ ترکیب sam-kṛt و صورت‌های sam-skar- و pari-skar- (با «س» افزوده) را در همین مدخل آورده، و واتکینز در پیوست AHD واژهٔ انگلیسی SANSKRIT را زیر همین ریشه ثبت کرده است. «س» میانجی در sam-s-kṛta- همان افزایش شناختهٔ هندی باستان پس از sam- و pari- پیش از kar- است. تنها ایراد، برگردان نورایی است: «worked before» یعنی sam- را «پیش» گرفته، حال آنکه sam- به معنی «با هم» است. ریشه و مسیر درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/Sanskrit\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. kʷer-1: 'To make. 1. Sanskrit karoti, he makes: SANSKRIT.' The index also lists 'KARMA kʷer-1'. The Sanskrit language-name is thus derived from this root in the very appendix Nourai cites.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 641, s.v. kʷer-1\", \"stance\": \"supports\", \"note\": \"'... kṛti- 'feat, deed, act'; sam-kṛt 'once'; besides with s- pari-skar- and sam-skar-.'\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt l.16475 s.v. Sanskrit\", \"stance\": \"supports\", \"note\": \"'Sanskrit. (Skt.) Skt. saṃskṛta, lit. „symmetrically formed.“ — Skt. sam, together; kṛta, made, from kṛ, to make.' — Skeat glosses sam- as 'together', not 'before'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 517\", \"stance\": \"supports\", \"note\": \"'Ai. karoti ... Ptc. kṛtá- ... daneben mit s- pari-skar- und saṃ-skar-.'\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Persian\",\n          \"words\": \"sanskrît «سنسکریت ( سانسکریت )»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"A modern learned borrowing of the language name, not an inherited word: Persian سنسکریت / سانسکریت entered the language in the 19th-20th century, either straight from Sanskrit saṃskṛta- or through European orientalist usage (French sanscrit, English Sanskrit), which is why both a short (سنسکریت) and a long-vowel (سانسکریت) spelling circulate. That it is a loan rather than a cognate is guaranteed by the initial s-: the inherited Iranian correspondent of Skt. sam- is ham- (Av. ham-, MP ham-, NP هم-, e.g. MP hangārdan < *ham-kāraya-), so an inherited Persian reflex of saṃskṛta- would have begun with ham-, not san-. Dehkhodā's entry سانسکریت simply refers to سنسکریت, and Moʿin's Farhang-e Fārsi (the aʿlām volumes Nourai cites as MON5:809) has the language entry, describing it as 'زبان علمی قدیم و مقدس هندوان' and one of the important Indo-European languages, closely related to Avestan.\",\n          \"derivation_fa\": \"«سنسکریت / سانسکریت» وام‌واژه‌ای است نو و کتابی، نه واژه‌ای موروثی: در سدهٔ سیزدهم و چهاردهم خورشیدی، یا مستقیم از خودِ saṃskṛta- سنسکریت یا از راه کاربرد شرق‌شناسان اروپایی (فرانسوی sanscrit، انگلیسی Sanskrit) به فارسی آمده و به همین سبب دو املای کوتاه و کشیده در کنار هم رواج دارد. دلیل قاطع وام‌بودن آن «س» آغازی است: معادل موروثی sam- سنسکریت در ایرانی ham- است (اوستایی ham-، فارسی میانه ham-، فارسی «هم-»، مانند hangārdan از *ham-kāraya-)، پس اگر واژه موروثی می‌بود باید با «هم-» آغاز می‌شد نه «سن-». دهخدا مدخل «سانسکریت» را به «سنسکریت» ارجاع می‌دهد و فرهنگ فارسی معین (همان جلد اعلام که نورایی به آن ارجاع داده) آن را «زبان علمی قدیم و مقدس هندوان» و از زبان‌های مهم هندواروپایی و خویشاوند نزدیک اوستایی می‌خواند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/سانسکریت/\",\n            \"https://www.etymonline.com/word/Sanskrit\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON5:809\", \"status\": \"partial\", \"note\": \"Moʿin's volumes 5-6 (aʿlām) are not among the local scans and vajehyab/abadis carry only the lexicon volumes' text; the entry itself was read through abadis' reproduction of Farhang-e Moʿin s.v. سانسکریت ('زبان علمی قدیم و مقدس هندوان ... از زبان‌های مهم هندواروپایی، نزدیک به اوستایی'), which confirms that Moʿin has the entry, but the page number 809 could not be verified against the print.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"abadis reproduction of Farhang-e Moʿin s.v. سانسکریت\", \"stance\": \"supports\", \"note\": \"'زبان علمی قدیم و مقدس هندوان' — the language name, with a cross-reference from سانسکریت to سنسکریت in Dehkhodā.\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. Sanskrit\", \"stance\": \"supports\", \"note\": \"'Skt. saṃskṛta, lit. „symmetrically formed“' — the etymon of the Persian and English names alike.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"Sanskrit\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English Sanskrit is attested from the 1610s, from Sanskrit saṃskṛtam 'put together, well-formed, perfected' (sam- 'together' + kṛta- 'made'), and became the general European name of the language after Sir William Jones and the Calcutta orientalists in the 1780s. Skeat: 'Sanskrit. (Skt.) Skt. saṃskṛta, lit. “symmetrically formed.” — Skt. sam, together; kṛta, made, from kṛ, to make.' Watkins/AHD lists SANSKRIT as the English word under kʷer-1, so the whole chain PIE *kʷer- > Skt. kṛtá- > saṃskṛta- > English Sanskrit is exactly as the chart draws it.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی Sanskrit از حدود ۱۶۱۰ میلادی به کار رفته و مستقیماً از saṃskṛtam سنسکریت «به‌هم‌برنهاده، پیراسته» (sam- «با هم» + kṛta- «کرده») گرفته شده، و پس از کار ویلیام جونز و شرق‌شناسان کلکته در دههٔ ۱۷۸۰ نام عمومی این زبان در اروپا شد. اسکیت می‌نویسد: «Sanskrit ... از saṃskṛta سنسکریت، به‌لفظ „متقارن‌ساخته“؛ از sam „با هم“ و kṛta „کرده“ از kṛ „کردن“». واتکینز نیز در پیوست AHD واژهٔ SANSKRIT را زیر ریشهٔ kʷer-1 آورده است؛ پس زنجیرهٔ هندواروپایی *kʷer- ← سنسکریت kṛtá- ← saṃskṛta- ← انگلیسی Sanskrit دقیقاً همان است که نمودار نشان می‌دهد. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/Sanskrit\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"refs=None in the book. Checked instead against Etymonline, Skeat and the AHD appendix — see sources and consulted.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"SKT.txt l.16475\", \"stance\": \"supports\", \"note\": \"'Sanskrit. (Skt.) Skt. saṃskṛta, lit. „symmetrically formed.“ — Skt. sam, together; kṛta, made, from kṛ, to make.'\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. kʷer-1 and the index\", \"stance\": \"supports\", \"note\": \"'kʷer-1. To make. 1. Sanskrit karoti, he makes: SANSKRIT.'\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Sogdian\",\n          \"words\": \"krty`; n`-krtk\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both words are the Sogdian continuation of the same root. Gharib's Sogdian Dictionary p. 32 (the page Nourai cites) has no. 825 'ʾkrty ... (a)krte ... action, deed' and no. 826 'ʾkrtyʾ ... (a)krtya ... ©Skt. karman ... action' — Nourai's krty` is ʾkrtyʾ, with the Sogdian prothetic aleph before the initial cluster; his gloss 'work, manner' is looser than Gharib's 'action, deed'. Sogdian krt- is the past stem of kun- < Old Iranian *kar- 'to do' (Cheung, s.v. *kar: 'SSogd. (ʾ)krt- (pass.) “to happen, occur; to become”'). The second word is at Gharib p. 231, not p. 32: nos. 5756 and 5763 'nʾkrtʾk / nʾkrtk-(w) ... na-krte, nak(ar)taku ... silver (not coined)', privative nā- 'not' + krt- 'made', literally 'un-wrought', with the derivatives nʾkrtʾynʾk 'silvern' and nʾkrtʾy pʾmy 'silver-coloured'. The semantics 'not made / not struck' > 'bullion, silver' is exactly what the gloss 'uncoined silver' says.\",\n          \"derivation_fa\": \"هر دو واژه دنبالهٔ سغدی همان ریشه‌اند. غریب در فرهنگ سغدی ص ۳۲ (همان صفحه‌ای که نورایی ارجاع داده) شمارهٔ ۸۲۵ «ʾkrty ... کردار، کنش» و شمارهٔ ۸۲۶ «ʾkrtyʾ ... برابر karman سنسکریت، کنش» را دارد؛ صورت krty` نورایی همان ʾkrtyʾ است با «الف» آغازینِ پروتتیک سغدی، و معنای «کار، شیوه» اندکی آزادتر از «کردار، کنش» غریب است. ستاک krt- در سغدی ستاک گذشتهٔ kun- و از ایرانی باستان *kar- «کردن» است (چونگ، ذیل *kar). واژهٔ دوم اما در ص ۲۳۱ فرهنگ غریب است نه ص ۳۲: شماره‌های ۵۷۵۶ و ۵۷۶۳ «nʾkrtʾk / nʾkrtk-(w) ... سیم (نامسکوک)»، مرکب از پیشوند نفی nā- «نه» و krt- «کرده»، یعنی به‌لفظ «ناکرده، ناساخته». تحول معنایی «ناساخته، نازده» به «شمش، سیم» همان است که در معنای «uncoined silver» آمده. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"SOD:32\", \"status\": \"partial\", \"note\": \"SOD_pages.txt leaf 98 = printed p. 32 (leaf 99 carries the printed number 33): '825 ʾkrty B, S | (a)krte (ʾkrtʾk, ʾkrtyy) ... action, deed'; '826 ʾkrtyʾ M, B | (a)krtya (ʾkrtyh) ©Skt. karman ©f. n. ... action'. Supports the first word. The second word, nʾ-krtk, is NOT on p. 32: it is at p. 231, nos. 5756 'nʾkrtʾk ... na-krte, nak(s)te, nakarte ... silver (not coined)' and 5763 'nʾkrtk-(w) ... na-krte, nak(ar)taku ... silver'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SOD\", \"where\": \"p. 231 nos. 5756-5773\", \"stance\": \"supports\", \"note\": \"'5756 nʾkrtʾk B ... na-krte ... silver (not coined)'; '5759 nʾkrtʾynʾk ... silvern'; '5771 nʾqty C ... na-k(s)te ... silver (not coined)' — the privative nā- + krt- formation, glossed by Gharib himself as 'not coined'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"s.v. *kar, Sogdian section\", \"stance\": \"supports\", \"note\": \"'*SOGDIAN: SSogd. (k)wn-, BSogd. (k)wn-, CSogd. wn- “to do, make, perform, cause”, SSogd. (ʾ)krt- (pass.) “to happen, occur; to become, be situated”' under PIE *kʷer-, Pok. 641.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Persian\",\n          \"words\": \"noqreh «نقره»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The chart takes the minority, Iranian side of a genuine dispute, and its own cited reference is where that side is stated. Moʿin's footnote at Borhān-e Qāṭeʿ p. 2157 s.v. نقره says: 'در سغدی nʾkrtk (سیم) ... و آن مرکب است از *nā (نه، نا) + krt (کرده)؛ و مراد نامسکوک است (از افادات شفاهی استاد بنونیست)' — i.e. Benveniste, in conversation, took Sogd. nʾkrtk as nā- + krt- 'uncoined'; and Moʿin adds that in Arabic نقرة has several senses, e.g. 'القطعة المذابة من الذهب والفضة', but that the sense 'silver, silver in the mine' is late/modern (محدث), citing Dozy II 10. The majority view, given by Wiktionary and by the Arabic lexicographers, keeps Persian نقره a straight loan from Arabic نُقْرَة nuqra 'cavity, hollow; concentration of silver', a nomen vicis of the sound root ن ق ر 'to hollow out'. The chart's NOTE (compare سیم) is a real argument for the Iranian side: NP سیم 'silver' is Greek ásēmon 'unstamped, uncoined (silver)', an exactly parallel 'uncoined' > 'silver' shift in the same language. Against it is the phonology: Sogd. nʾkrtʾk > nuqra requires losing the medial -k(a)rt- cluster, and the Arabic form is morphologically transparent. Both accounts are alive; hence plausible, not confirmed.\",\n          \"derivation_fa\": \"نمودار در اینجا جانب اقلیت یک اختلاف واقعی را گرفته، و درست همان مرجعی که خودش ارجاع داده جای بیان این دیدگاه است. معین در حاشیهٔ برهان قاطع ص ۲۱۵۷ ذیل «نقره» می‌نویسد: «در سغدی nʾkrtk (سیم) ... و آن مرکب است از *nā (نه، نا) + krt (کرده)؛ و مراد نامسکوک است (از افادات شفاهی استاد بنونیست)»، و می‌افزاید که «نقرة» در عربی معانی متعدد دارد، از جمله «القطعة المذابة من الذهب والفضة»، ولی معنای «سیم و سیم در معدن» در عربی مُحدَث است (به نقل از دُزی، ج ۲ ص ۱۰). دیدگاه اکثریت — که ویکی‌واژه و لغویان عرب دارند — «نقره» فارسی را یکسره وام‌واژهٔ عربی نُقْرَة «گودی؛ پارهٔ سیم گداخته» از ریشهٔ «ن ق ر» می‌داند. یادداشت خودِ نمودار (مقایسه با «سیم») استدلال خوبی به سود سوی ایرانی است: «سیم» فارسی از یونانی ásēmon «بی‌نشان، نازده» است، یعنی همان تحول معنایی «نامسکوک ← سیم» در همین زبان. در برابر، از نظر آوایی گذر nʾkrtʾk سغدی به nuqra افتادن خوشهٔ میانی -krt- را می‌طلبد و صورت عربی از نظر صرفی شفاف است. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/نقره\",\n            \"https://en.wiktionary.org/wiki/نقرة\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:2157\", \"status\": \"supports\", \"note\": \"ref_page.py BQT:2157 (v4 pdf p. 240), entry نقره in the باب نون-قاف section, footnote 7: 'در سغدی nʾkrtk (سیم) رک: [Gauthiot-]Benveniste, Essai de grammaire sogdienne ... وآن مرکب است از *nā (نه، نا) + krt (کرده)؛ و مراد نامسکوک است (از افادات شفاهی استاد بنونیست). در عربی معانی متعدد دارد از جمله «القطعة المذابة من الذهب والفضة» ... ولی بمعنی سیم و سیم در معدن محدث است «دزی ج۲ ص۱۰»'. This is precisely Nourai's arrow, credited to Benveniste.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SOD\", \"where\": \"p. 231 no. 5756\", \"stance\": \"supports\", \"note\": \"'nʾkrtʾk ... na-krte ... silver (not coined)' — the Sogdian form and meaning Moʿin/Benveniste build on. Wiktionary's Arabic نقرة entry itself carries 'Further reading: Gharib, „nʾkrtk-(w)“, Sogdian dictionary, page 231', i.e. even the Arabic-origin entry acknowledges the Sogdian comparison.\"},\n            {\"src\": \"MON\", \"where\": \"Wiktionary fa/ar نقره, نقرة\", \"stance\": \"contradicts\", \"note\": \"Wiktionary's Persian نقره: 'Borrowed from Arabic نُقْرَة (nuqra)'; the Arabic نُقْرَة entry: 'cavity, cleft, socket; (archaic) concentration of silver, high-quality silver', root ن ق ر, with Persian listed as a descendant. The mainstream account reverses Nourai's arrow.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Krep, Krep-ed-tro\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *krep-, *kr̥p- 'body' (Pokorny 620 krep-1; Walde-Pokorny I 486 qrep-, qr̥p- 'Leib, Gestalt'; Watkins/AHD kʷrep- 'Body'); the compound *kʷr̥p-[e]d-tro- 'body-eater' > Av. xrafstra-\",\n      \"note\": \"Pokorny 620 is exactly this entry, double lemma and all: 'Root / lemma: krep-1, kr̥p- ... Meaning: body ... Old Indic kṛpā ... Avestan kərəfs, kahrpəm “shape, body”, Middle Persian karp “body” (Avestan xrafstra- n. “predator” from *krep + *[e]d-tro- to ed- “eat”?) ... Latin corpus, -oris n. “body” ... References: WP. I 486 f. Page(s): 620'. Walde-Pokorny I 486 has the same, crediting the compound analysis to 'Bthl. Wb. 538'. So Nourai's second lemma 'Krep-ed-tro: body eaters' and the cross-reference '☞ Ed' are not his invention but Pokorny's/WP's own — though both mark it with a question mark, and Bartholomae's own note at col. 538 calls the division only 'wenigstens denkbar' and records Darmesteter's rival *xratu-star-. Klein p. 355 s.v. corpus gives the same root and adds a link Nourai does not draw: 'prob. fr. I.-E. base *qʷrep-, *qʷr̥p-, enlargement of *qʷer-, “to make, form”' — i.e. this root is an extension of entry 0's root on the same page.\",\n      \"note_fa\": \"پوکورنی در ص ۶۲۰ دقیقاً همین مدخل را با هر دو صورتش دارد: «krep-1، kr̥p- ... معنی: تن ... هندی باستان kṛpā؛ اوستایی kərəfs، kahrpəm «شکل، تن»؛ فارسی میانه karp «تن» (اوستایی xrafstra- «جانور درنده» از *krep + *[e]d-tro- به ریشهٔ ed- «خوردن»؟) ... لاتین corpus». والده-پوکورنی (ج ۱ ص ۴۸۶) نیز همین را دارد و تجزیهٔ ترکیب را به بارتولمه (ستون ۵۳۸) نسبت می‌دهد. پس صورت دوم ریشه در نمودار نورایی («Krep-ed-tro: تن‌خواران») و ارجاع «☞ Ed» ساختهٔ او نیست، بلکه از خودِ پوکورنی و والده-پوکورنی است؛ هرچند هر دو آن را با علامت پرسش آورده‌اند و بارتولمه خود این تجزیه را تنها «دست‌کم اندیشیدنی» می‌خواند و صورت رقیب دارمستتر (*xratu-star-) را هم ثبت می‌کند. کلاین در ص ۳۵۵ ذیل corpus همین ریشه را می‌آورد و نکته‌ای می‌افزاید که نورایی نگفته است: این ریشه گسترش‌یافتهٔ *kʷer- «کردن، ساختن» است، یعنی همان ریشهٔ مدخل نخست همین صفحه. ادعای نورایی درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/krep-\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:620\", \"status\": \"supports\", \"note\": \"POK_full.txt l.48390: 'Root / lemma: krep-1, kr̥p- | Meaning: body | ... Old Indic kṛpā instr. sg. “shape, beauty”, Avestan kərəfs, kahrpəm “shape, body”. Middle Persian karp “body” (Avestan xrafstra- n. “predator” from *krep + *[e]d-tro- to ed- “eat”?) ... Latin corpus, -oris n. “body” ... References: WP. I 486 f., WH. I 277 f. Page(s): 620.'\"},\n        {\"ref\": \"KLN:355\", \"status\": \"supports\", \"note\": \"Klein 1966 p. 355 (page markers 352 and 357 bracket the entries) s.v. corpus: 'L. corpus, gen. corporis, “body”, prob. cogn. with OI. kṛp-, “form, beauty”, Avestic kərəfš, gen. kəhrpō, “form, body”, OE. hrif ... prob. fr. I.-E. base *qʷrep-, *qʷr̥p-, enlargement of *qʷer-, “to make, form” ... Cp. corporal, corporate, corporation ... corps, corpse, corpulent, corse'; and s.v. corset: 'F. corset, lit. “a little body”, dimin. of OF. cors (F. corps), fr. L. corpus.'\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I 486 (WLD_Bd1_1930_dli_70244_djvu.txt l.30596)\", \"stance\": \"supports\", \"note\": \"'1. qrep-, qr̥p- „Leib, Gestalt“ ... Ai. kṛpā́ instr. sg. „Gestalt, Schönheit“, av. kərəfš, gen. kahrpō „Gestalt, Leib“, mp. karp „Körper“; (av. xrafstra- n. „Raubtier“ aus qʷr̥p + [e]d-tro- zu ed- „essen“? Bthl. Wb. 538) ... Lat. corpus, -oris „Leib, Körper“.'\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kʷrep-\", \"stance\": \"supports\", \"note\": \"'kʷrep-. Body. 1. Suffixed form *krep-es- in Germanic *hrifiz in Old English hrif, belly: MIDRIFF. 2. Suffixed zero-grade form *kʷr̥p-es- in Latin corpus, body, substance: CORPORAL, ... CORPS, CORPSE, CORPULENCE, CORPUS, CORPUSCLE, CORSAGE, CORSE, CORSET. [Pok. 1. krep- 620.]'\"},\n        {\"src\": \"SYN\", \"where\": \"Buck 4.47, citing Walde-P. 1.486\", \"stance\": \"supports\", \"note\": \"'OE hrif (also sometimes “belly”; cf. NE midriff), OHG (h)ref, prob. : Lat. corpus, Skt. kṛp- “body”, etc. (4.41). Walde-P. 1.486.'\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"kerefs; xrafstra\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"kerefs is the nominative singular kərəfš of Av. kəhrp-/kərəf- (f./n.), whose meaning Bartholomae (AiW cols. 469-470) gives as 'das sichtbare Äussere jedes Wesens und Dings, äussere Erscheinung, sichtbare Gestalt' and, of living beings, 'Leib, Körper' — so Nourai's gloss 'body' is right, and his spelling matches Pokorny's ('Avestan kərəfs') and Klein's ('Avestic kərəfš') letter for letter; it continues *kr̥p-s beside Skt. kṛ́p- and Lat. corpus. xrafstra- n. is genuinely Avestan and genuinely means what Nourai says: Bartholomae col. 538 defines it as, in the Gāthās, 'wildes Tier, Raubtier' and in the Younger Avesta 'Bezeichnung für alle schädlichen (daēvischen) Tiere'. The claim that needs hedging is the derivation of the second word from the first: Walde-Pokorny I 486 and Pokorny 620 both give it as *kʷr̥p-[e]d-tro- 'body-eater' to *ed- 'to eat' — but both put a question mark on it, they credit it to Bartholomae AiW 538, and Bartholomae's own footnote there says only that the division into kərəf- (see kahrp-) + -stra- 'zum ai. V. ad(mi)' is 'wenigstens denkbar', while quoting Darmesteter's competing *xratu-star- / *xrafstara-. Modern reconstruction (Wiktionary's *krep- page) lists kəhrpəm but not xrafstra-. Hence plausible: the first word confirmed, the second word's attachment to this root traditional but explicitly tentative in the very sources Nourai cites.\",\n          \"derivation_fa\": \"«kerefs» صورت فاعلی مفرد kərəfš از ستاک اوستایی kəhrp-/kərəf- است که بارتولمه (ستون‌های ۴۶۹-۴۷۰) معنایش را «نمود بیرونی و دیدنی هر موجود و هر چیز، شکل آشکار» و در مورد جانداران «تن، پیکر» می‌آورد؛ پس معنای «body» نورایی درست است و املای او مو به مو با پوکورنی («kərəfs») و کلاین («kərəfš») می‌خواند. این صورت دنبالهٔ *kr̥p-s است، هم‌ریشه با kṛ́p- سنسکریت و corpus لاتین. xrafstra- نیز واژه‌ای است اوستایی و معنایش همان است که نورایی می‌گوید: بارتولمه (ستون ۵۳۸) آن را در گاهان «جانور وحشی، درنده» و در اوستای نو «نام همهٔ جانوران زیانکار دیوی» تعریف می‌کند. آنچه باید با احتیاط پذیرفت اشتقاق واژهٔ دوم از واژهٔ نخست است: والده-پوکورنی (ج ۱ ص ۴۸۶) و پوکورنی (ص ۶۲۰) هر دو آن را *kʷr̥p-[e]d-tro- «تن‌خوار» از ریشهٔ *ed- «خوردن» می‌گیرند، اما هر دو علامت پرسش می‌گذارند و آن را به بارتولمه نسبت می‌دهند، و خودِ بارتولمه در همان ستون ۵۳۸ فقط می‌نویسد که تجزیهٔ kərəf- + -stra- (به ریشهٔ ad- «خوردن» سنسکریت) «دست‌کم اندیشیدنی است» و صورت رقیب دارمستتر (*xratu-star-) را هم می‌آورد. بازساخت‌های امروزی (ویکی‌واژه ذیل *krep-) kəhrpəm را می‌آورند ولی xrafstra- را نه. پس واژهٔ نخست تأیید و پیوند واژهٔ دوم با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/krep-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:620\", \"status\": \"supports\", \"note\": \"'Old Indic kṛpā instr. sg. “shape, beauty”, Avestan kərəfs, kahrpəm “shape, body”. Middle Persian karp “body” (Avestan xrafstra- n. “predator” from *krep + *[e]d-tro- to ed- “eat”?)' — both of Nourai's words, in his spelling, with the compound analysis he uses, but hedged by a question mark.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"cols. 469-470 s.v. kahrp-, kərəf-; col. 538 s.v. xrafstra-\", \"stance\": \"supports\", \"note\": \"'• j., g. kahrp-, kərəf- f., n. “das sichtbare Äussere jedes Wesens und Dings, äussere Erscheinung, sichtbare Gestalt” ... A) insbes. von lebenden Wesen ... “Leib, Körper” ... — ai. kṛ́p- (IS.), ... arm. LW. kerp. — Vgl. hukəhrpta- und xrafstra- No. [3].' And s.v. xrafstra-: '“wildes Tier, Raubtier” ... im jAw. Bezeichnung für alle schädlichen (daēvischen) Tiere', with footnote 3 'Die Zerlegung in kərəf-(s. kahrp-)-stra- (zum ai. V. ad-mi) ist wenigstens denkbar' and footnote 4 citing Darmesteter ZA I 208 that xrafstra might stand for *xratu-stara-.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 486\", \"stance\": \"supports\", \"note\": \"'av. kərəfš, gen. kahrpō „Gestalt, Leib“, mp. karp „Körper“; (av. xrafstra- n. „Raubtier“ aus qʷr̥p + [e]d-tro- zu ed- „essen“? Bthl. Wb. 538)'.\"},\n            {\"src\": \"NYB\", \"where\": \"vol. II Glossary s.v. karp\", \"stance\": \"supports\", \"note\": \"'karp [klpʾ] ... the external, visible form of living beings ... — Av. (467 sq.) kahrp-; Arm. lw. kerp; MPrs kyrb, but Paz. karf.'\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"xrafstar\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Middle Persian xrafstar [hlpstl] 'reptile, noxious creature' is not an inherited form but a learned taking-over of the Avestan word into the Zoroastrian Pahlavi books: MacKenzie's Concise Pahlavi Dictionary marks it as such in the headword itself — 'xrafstar [hlpstl = Av. xrafstra-] reptile, noxious creature' — and Nyberg is explicit: 'xrafstr [hlpstl] Ahrimanic, noxious animals 76; — Borrowed from Av. (538) xrafstra-.' The only formal change is the anaptyctic vowel that breaks the final cluster -stra > -star, regular in Middle Persian (cf. Av. -tra > MP -tar in other Avestan borrowings). Nourai's gloss 'pests, troublesome creatures' matches the Pahlavi usage, where the xrafstars are the daēvic vermin a pious man is meritoriously required to kill.\",\n          \"derivation_fa\": \"فارسی میانهٔ xrafstar (نوشتار hlpstl) «جانور موذی، خزندهٔ زیانکار» صورتی موروثی نیست بلکه وام‌گیری کتابی واژهٔ اوستایی در متون پهلوی زردشتی است: مکنزی همین را در خودِ سرواژه می‌آورد — «xrafstar [hlpstl = اوستایی xrafstra-] خزنده، جانور موذی» — و نیبرگ صریح‌تر می‌نویسد: «xrafstr ... جانوران اهریمنی موذی ... وام‌گرفته از اوستایی (۵۳۸) xrafstra-». تنها دگرگونی صوری، واکهٔ میانجی (anaptyxis) است که خوشهٔ پایانی -stra را به -star می‌شکند، که در فارسی میانه قاعده‌مند است. معنای «آفات، جانوران آزاررسان» که نورایی داده با کاربرد پهلوی می‌خواند، جایی که کشتن خرفستران کاری ثواب شمرده می‌شود. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"SNS:40\", \"status\": \"supports\", \"note\": \"Tavoosi, Vāže-nāme-ye Šāyast nē Šāyast p. 40: the index (SNS.txt l.29704, 30705) gives 'xrafstar 40/9', 'xrafstra- 40/10', 'xrafstarān 40/13-44/16', 'xrafstar ī ābīg 40/14'; the entry itself (SNS.txt l.3952-3959) reads 'خرفستر xrafstar: ... (اوستایی) xrafstra- (بارتولمه ۵۳۸) ... خروستر xarwastar', i.e. the Pahlavi word with its Avestan etymon and Bartholomae's column, exactly Nourai's arrow.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"p. 95 s.v. xrafstar\", \"stance\": \"supports\", \"note\": \"'xrafstar [hlpstl = Av. xrafstra-] reptile, noxious creature'; MacKenzie's English index: 'creature ... noxious ~ xrafstar', 'reptile xrafstar'.\"},\n            {\"src\": \"NYB\", \"where\": \"vol. II Glossary s.v. xrafstr\", \"stance\": \"supports\", \"note\": \"'xrafstr [hlpstl] Ahrimanic, noxious animals 76; — Borrowed from Av. (538) xrafstra-.' Nyberg's Avestan-to-Pahlavi index also lists 'xrafstra-: xrafstr'.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"xerafstar «خِرَفستَر ( خِستَر )»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian خرفستر is the survival of MP xrafstar in the Zoroastrian and lexicographical tradition rather than in ordinary speech. Dehkhodā defines it as 'جانوران موذی چون مار، سوسمار، وزغ، موش، مور، کیک، ملخ، مگس، عنکبوت، کرم، شپش و هر جانور خرد آزاررسان دیگر', and Farhang-e Moʿin as '(۱) جانور موذی و آزاررسان مانند مار و عقرب؛ (۲) در آیین زردشتی، آفریدهٔ زیانکار منسوب به اهریمن'; both mark the Avestan origin xrafstra- and the Pahlavi xrafstar. The contracted variant خستر which Nourai puts in parentheses is likewise recorded in the classical Persian dictionaries, and the Šāyast nē Šāyast glossary adds a further variant خروستر xarwastar. The Persian form keeps the Pahlavi shape unchanged apart from the vocalisation xerafstar; a genuinely inherited word would not have preserved the Avestan cluster this faithfully, which is another sign that the whole chain is a bookish one.\",\n          \"derivation_fa\": \"«خرفستر» فارسی نو بازماندهٔ xrafstar فارسی میانه است، اما نه در زبان روزمره بلکه در سنت زردشتی و در فرهنگ‌ها. دهخدا آن را «جانوران موذی چون مار، سوسمار، وزغ، موش، مور، کیک، ملخ، مگس، عنکبوت، کرم، شپش و هر جانور خرد آزاررسان دیگر» و فرهنگ معین «۱. جانور موذی و آزاررسان مانند مار و عقرب؛ ۲. در آیین زردشتی آفریدهٔ زیانکار منسوب به اهریمن» تعریف می‌کند و هر دو ریشهٔ اوستایی xrafstra- و صورت پهلوی xrafstar را یادآور می‌شوند. گونهٔ کوتاه‌شدهٔ «خستر» که نورایی در پرانتز آورده نیز در فرهنگ‌های کهن فارسی ثبت است، و واژه‌نامهٔ شایست نه شایست گونهٔ «خروستر» xarwastar را هم می‌افزاید. صورت فارسی جز مصوت‌گذاریِ xerafstar تغییری نکرده است؛ واژه‌ای که به‌راستی موروثی می‌بود خوشهٔ اوستایی را این‌قدر دست‌نخورده نگاه نمی‌داشت، و همین نشانهٔ دیگری است بر کتابی بودن کل این زنجیره. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/خرفستر/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"SNS:40\", \"status\": \"supports\", \"note\": \"Same page as node 2; the glossary entry gives the Persian headword خرفستر with the Avestan etymon and the variant خروستر xarwastar, and 'xrafstar ī ābīg' at 40/14.\"},\n            {\"ref\": \"MON:1411,1419\", \"status\": \"partial\", \"note\": \"The local Moʿin OCR (MON_part1/part2) contains no خرفستر at all (grep returns nothing for خرفستر/خرفس), so the printed pages 1411 and 1419 could not be located in the scan; the entry was instead read in abadis' reproduction of Farhang-e Moʿin, which does have خرفستر with the Avestan/Pahlavi note and the variant خستر, so the substance of the citation checks out even though the page numbers could not be.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"abadis, Farhang-e Moʿin + Loghatnāme-ye Dehkhodā s.v. خرفستر\", \"stance\": \"supports\", \"note\": \"Dehkhodā: 'جانوران موذی چون مار، سوسمار، وزغ، موش، مور، کیک، ...'; Moʿin: 'جانور موذی و آزاررسان مانند مار یا عقرب؛ در آیین زردشتی آفریدهٔ زیانکار منسوب به اهریمن'; both give Avestan xrafstra- / Pahlavi xrafstar, and the variant خستر is documented.\"},\n            {\"src\": \"PHD\", \"where\": \"p. 95\", \"stance\": \"supports\", \"note\": \"'xrafstar [hlpstl = Av. xrafstra-]' — the Middle Persian link between the Avestan word and the New Persian one.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Latin\",\n          \"words\": \"corpus\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin corpus, gen. corporis, n. 'body, substance' continues an Indo-European s-stem *krép-os / *krép-es-os beside the root noun *kérp-s ~ *kr̥p-és (whence Av. kərəfš, Skt. kṛ́p-); the -o- of Italic *korpos is probably due to the conflation of the two formations. Watkins/AHD reconstructs it as the 'suffixed zero-grade form *kʷr̥p-es-' and derives from it the whole English family CORPORAL, CORPORATE, CORPS, CORPSE, CORPULENCE, CORPUS, CORPUSCLE, CORSAGE, CORSE, CORSET, with the reference '[Pok. 1. krep- 620]'. Nourai's gloss 'form, body' is right — corpus covers both the physical body and, in later Latin, any organised body or collection.\",\n          \"derivation_fa\": \"corpus لاتین (اضافی corporis) «تن، پیکر، جسم» دنبالهٔ یک نام‌ستاکِ s-دار هندواروپایی *krép-os / *krép-es-os است در کنار نام‌ستاک ریشه‌ای *kérp-s ~ *kr̥p-és (که kərəfš اوستایی و kṛ́p- سنسکریت از آن است)؛ واکهٔ -o- در ایتالیایی باستان *korpos احتمالاً از آمیختن این دو ساخت پدید آمده است. واتکینز در پیوست AHD آن را «صورت درجهٔ صفرِ پسوندی *kʷr̥p-es-» می‌گیرد و کل خانوادهٔ انگلیسیِ CORPORAL، CORPORATE، CORPS، CORPSE، CORPUS، CORSET و جز آن را از آن مشتق می‌داند، با ارجاع «[Pok. 1. krep- 620]». معنای «form, body» که نورایی داده درست است، زیرا corpus هم بر تن و هم — در لاتین متأخر — بر هر پیکرهٔ سازمان‌یافته دلالت دارد. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/krep-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. kʷrep-: 'Body. ... 2. Suffixed zero-grade form *kʷr̥p-es- in Latin corpus, body, substance: CORPORAL, CORPORAL, CORPORATE, CORPOREAL, CORPOSANT, CORPS, CORPSE, CORPULENCE, CORPUS, CORPUSCLE, CORSAGE, CORSE, CORSET; LEPRECHAUN. [Pok. 1. krep- 620.]'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p. 355 s.v. corpus\", \"stance\": \"supports\", \"note\": \"'corpus, n., body. — L. corpus, gen. corporis, “body”, prob. cogn. with OI. kṛp-, “form, beauty”, Avestic kərəfš, gen. kəhrpō, “form, body” ... prob. fr. I.-E. base *qʷrep-, *qʷr̥p-, enlargement of *qʷer-, “to make, form”.'\"},\n            {\"src\": \"POK\", \"where\": \"p. 620\", \"stance\": \"supports\", \"note\": \"'Latin corpus, -oris n. “body”; Middle Irish crí “body” (*kr̥pes); Old High German (h)ref m. “body, lower abdomen, womb”.'\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt l.4138 s.v. corps, corpse, corse\", \"stance\": \"supports\", \"note\": \"'corps, corpse, corse, a body. (F.—L.) ... M. E. corps. — O. F. cors, the body. — L. corpus.'\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"French\",\n          \"words\": \"cors; corset\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old French cors 'body' is the regular Gallo-Romance outcome of Latin corpus: loss of the final -us, and -rp- > -rs before the consonant cluster simplified. The modern French spelling corps is a 15th-16th c. learned re-latinisation (Klein: 'The MF. and modern F. spelling corps is due to the influence of L. corpus'). corset is its diminutive in -et, attested in French from the 13th c. in the sense 'bodice, tunic': Klein p. 355, 'corset, n., a close-fitting undergarment; stays. — F. corset, lit. “a little body”, dimin. of OF. cors (F. corps), fr. L. corpus'; likewise corselet 'little body' > body armour. Nourai's gloss for corset, 'little body, bra', puts the literal French sense next to the modern Persian one; the specifically shaping undergarment sense is only from 1795 (Etymonline).\",\n          \"derivation_fa\": \"cors فرانسویِ کهن «تن» بازتاب قاعده‌مند corpus لاتین در گالو-رومانس است: افتادن -us پایانی و تحول خوشهٔ -rp- به -rs. املای امروزی corps بازلاتینی‌سازی کتابیِ سده‌های پانزدهم و شانزدهم است (کلاین: «املای corps در فرانسویِ میانه و امروزی زیر تأثیر corpus لاتین است»). corset مصغّر آن با پسوند -et است و از سدهٔ سیزدهم در فرانسه به معنی «نیم‌تنه، بالاپوش تنگ» گواهی شده؛ کلاین در ص ۳۵۵: «corset ... از فرانسوی corset، به‌لفظ „تنِ کوچک“، مصغّر cors فرانسوی کهن، از corpus لاتین»، و همچنین corselet «تنِ کوچک» که به زره سینه گفته شد. برگردان نورایی («little body, bra») معنای لفظی فرانسوی را در کنار معنای امروزی فارسی گذاشته است؛ معنای خاصِ «شکم‌بند اندام‌آرا» تنها از ۱۷۹۵ میلادی است (اتیمآنلاین). ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/corset\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:355\", \"status\": \"supports\", \"note\": \"Klein 1966 p. 355: 'corsage, n. — F., formed with suff. -age fr. OF. cors (F. corps), “body”. See corps and cp. corse, corset.' / 'corselet, corslet, n., armor for the body. — F. corselet, lit., “little body”, dimin. of OF. cors (F. corps), “body”.' / 'corset, n., a close-fitting undergarment; stays. — F. corset, lit. “a little body”, dimin. of OF. cors (F. corps), fr. L. corpus.'\"},\n            {\"ref\": \"AHD:300\", \"status\": \"not_checked\", \"note\": \"AHD:300 is a page of the main dictionary text of the 1975/76 New College edition (presumably the corps/corpse/corset column); the only AHD text on disk is the standalone Watkins 1985 appendix of Indo-European roots, which has no page 300. The appendix entry kʷrep- does list CORPS, CORPSE and CORSET, which is the substance of the citation.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"SKT.txt l.4141, 4153 s.v. corset, corslet\", \"stance\": \"supports\", \"note\": \"'corset. (F. — L.) F. corset, a pair of stays; dimin. of O. F. cors, body; see corps.' / 'corslet. (F. — L.) F. corselet, “a little body”, Cot.; hence body armour. Double dimin. of O. F. cors, body.'\"},\n            {\"src\": \"WEB\", \"where\": \"Etymonline s.v. corset\", \"stance\": \"supports\", \"note\": \"'corset (n.), late 14c. (mid-13c. in Anglo-Latin), “a kind of laced bodice”, from Old French corset (13c.) “bodice, tunic”, from cors “body”, from Latin corpus “body” ... the sense “stiff supporting and constricting undergarment” is from 1795.'\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Persian\",\n          \"words\": \"korset «کرست»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian کرست is a 20th-century loan straight from French corset, part of the wave of French clothing and medical vocabulary that entered Persian through Dār al-Fonūn and the Tehran press. Both Dehkhodā and Moʿin tag it as French: Dehkhodā 'شکم‌بند زنان. بندی پهن و کش‌آمدنی و چسبان که زنان بر سرین و شکم و قسمتی از سینه بندند [فرانسوی]', Moʿin 'سینه‌بند، شکم‌بند، تن‌پوشی طبی ... [فر.]'; the printed Farhang-e Moʿin has 'کرست: سینه‌بند و شکم‌بند زنان'. Phonetically the French final -t is pronounced in the Persian form (korset, not *korse), as regularly in Persian Gallicisms taken from the written form. Persian therefore reaches Latin corpus only through French, exactly as the chart draws it.\",\n          \"derivation_fa\": \"«کرست» فارسی وام‌واژه‌ای است از corset فرانسوی در سدهٔ چهاردهم خورشیدی، بخشی از همان موج واژگان پوشاک و پزشکی فرانسوی که از راه دارالفنون و مطبوعات تهران وارد فارسی شد. دهخدا و معین هر دو آن را فرانسوی می‌دانند: دهخدا «شکم‌بند زنان ... [فرانسوی]» و معین «سینه‌بند، شکم‌بند، تن‌پوشی طبی ... [فر.]»؛ در چاپ فرهنگ فارسی معین آمده «کرست: سینه‌بند و شکم‌بند زنان». از نظر آوایی «ت» پایانی فرانسوی در صورت فارسی تلفظ می‌شود (korset نه *korse)، چنان‌که در بیشتر وام‌واژه‌های فرانسوی که از صورت نوشتاری گرفته شده‌اند. پس فارسی تنها از راه فرانسوی به corpus لاتین می‌رسد، درست همان‌گونه که نمودار کشیده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/کرست/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON\", \"status\": \"supports\", \"note\": \"Farhang-e Moʿin s.v. کرست: '[فر.] سینه‌بند، شکم‌بند، تن‌پوشی طبی برای جلوگیری از افتادگی یا جابه‌جایی اندام‌ها' (read via abadis); the local Moʿin OCR (MON_part2 l.21942) has the same headword: 'کرست: ۱ سینه بند و شکم بند زنان'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part2 l.21942 and abadis s.v. کرست\", \"stance\": \"supports\", \"note\": \"'کرست: سینه بند و شکم بند زنان' with the origin tag [فر.] = French.\"},\n            {\"src\": \"KLN\", \"where\": \"p. 355 s.v. corset\", \"stance\": \"supports\", \"note\": \"'F. corset, lit. “a little body”, dimin. of OF. cors (F. corps), fr. L. corpus' — the French word that Persian borrowed.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"corpse, corporation, corset\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three are Latin corpus by way of French. corpse: Middle English cors/corps 'body', from Old French cors < Latin corpus; the -p- was restored in the spelling in the 15th-16th c. under Latin influence, and the word narrowed to 'dead body' (Klein: 'corpse, n. — ME. corse, corps, “body”, fr. OF. cors, fr. L. corpus'; Skeat treats corps, corpse, corse as one word). corporation: from Late Latin corporātiō(n-) 'the making into a body', from corporāre 'to form into a body' < corpus, adopted in English in the 15th c. for a body of persons that the law treats as one person. corset: from Old French corset as in node 5, in English from the late 14th c. Watkins/AHD lists CORPS, CORPSE, CORPORATE and CORSET together under kʷrep-. Nourai gives no glosses here, and none are needed.\",\n          \"derivation_fa\": \"هر سه واژه از corpus لاتین‌اند و از راه فرانسوی به انگلیسی رسیده‌اند. corpse: انگلیسی میانه cors/corps «تن» از cors فرانسویِ کهن و آن از corpus لاتین؛ حرف «p» در سده‌های پانزدهم و شانزدهم زیر تأثیر لاتین به املا بازگردانده شد و معنای واژه به «تنِ مرده» تنگ شد (کلاین: «corpse ... از cors فرانسوی کهن، از corpus لاتین»؛ اسکیت corps و corpse و corse را یک واژه می‌شمارد). corporation: از corporātiō لاتینِ متأخر «به‌پیکره درآوردن»، از corporāre «پیکر ساختن» از corpus، که در سدهٔ پانزدهم در انگلیسی برای گروهی از افراد به کار رفت که قانون آنان را یک شخص می‌شمارد. corset: از corset فرانسوی کهن (مانند گرهٔ ۵)، در انگلیسی از اواخر سدهٔ چهاردهم. واتکینز در پیوست AHD واژه‌های CORPS، CORPSE، CORPORATE و CORSET را با هم زیر ریشهٔ kʷrep- آورده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/corpse\",\n            \"https://www.etymonline.com/word/corset\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:298\", \"status\": \"not_checked\", \"note\": \"AHD:298 is a page of the main text of the 1975/76 New College edition (the corporal-corpuscle column); only the Watkins appendix is on disk, which has no page 298. Its entry kʷrep- does list CORPORATE, CORPS, CORPSE and CORSET, i.e. the three words of this node, so the substance of the citation is right.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p. 355 s.v. corpse, corporation, corset\", \"stance\": \"supports\", \"note\": \"'corpse, n. — ME. corse, corps, “body”, fr. OF. cors, fr. L. corpus. ... The MF. and modern F. spelling corps is due to the influence of L. corpus.'; corpus entry cross-refers to 'corporal, corporate, corporation, corporeal ... corps, corpse, corpulent, corse, incorporate'.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt l.4138-4153\", \"stance\": \"supports\", \"note\": \"'corps, corpse, corse, a body. (F.—L.) Here corps is mod. F.; corse is from corpse by loss of p. M. E. corps. — O. F. cors, the body. — L. corpus.'\"},\n            {\"src\": \"WEB\", \"where\": \"Etymonline s.v. corpse, corset\", \"stance\": \"supports\", \"note\": \"corset 'late 14c. ... from Old French corset (13c.) “bodice, tunic”, from cors “body”, from Latin corpus ... PIE root *kʷrep- “body, form, appearance”'.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-293.json > /dev/null && echo \"JSON OK\""
}
```


### [2026-09-06T22:34:33.621Z] TOOL RESULT

```
JSON OK
```


## [2026-09-06T22:34:38.092Z] TOOL CALL #78: Bash

```json
{
 "command": "python3 tools/verify_check.py 293"
}
```


### [2026-09-06T22:34:40.059Z] TOOL RESULT

```
nodes verified: 16/16
node verdicts: {'plausible': 4, 'confirmed': 12}
root verdicts: {'confirmed': 2}
ref checks: {'partial': 4, 'supports': 12, 'not_found': 1, 'not_checked': 6}
books consulted: {'supports': 38, 'partial': 1, 'contradicts': 2, 'silent': 1} | by book: {'SKT': 6, 'NYB': 4, 'PHD': 4, 'MON': 4, 'WLD': 3, 'KLN': 3, 'BRT': 2, 'CHEUNG': 2, 'HUB': 2, 'PLA': 2, 'POK': 2, 'SOD': 2, 'WEB': 2, 'LKT': 1, 'AFM': 1, 'HRN': 1, 'AHD': 1}
```


## [2026-09-06T22:34:49.372Z] TOOL CALL #79: Bash

```json
{
 "command": "python3 - << 'PY'\nimport json,urllib.parse\nidx=set()\nfor line in open('data/verification/sources/web/index.jsonl'):\n    try: idx.add(json.loads(line)['url'])\n    except Exception: pass\nd=json.load(open('data/verification/page-293.json'))\nurls=set()\ndef collect(o):\n    if isinstance(o,dict):\n        for k,v in o.items():\n            if k=='sources': urls.update(v)\n            else: collect(v)\n    elif isinstance(o,list):\n        for i in o: collect(i)\ncollect(d)\nfor u in sorted(urls):\n    enc=urllib.parse.quote(u, safe=':/?#[]@!$&\\'()*+,;=%~')\n    print(('OK  ' if (u in idx or enc in idx) else 'MISS'), u)\nPY"
}
```


### [2026-09-06T22:34:51.369Z] TOOL RESULT

```
OK   https://abadis.ir/fatofa/خرفستر/
OK   https://abadis.ir/fatofa/سانسکریت/
OK   https://abadis.ir/fatofa/کرست/
OK   https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/krep-
OK   https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/kʷer-
OK   https://en.wiktionary.org/wiki/نقرة
OK   https://en.wiktionary.org/wiki/نقره
OK   https://en.wiktionary.org/wiki/وزير
OK   https://en.wiktionary.org/wiki/چاره
OK   https://www.etymonline.com/word/Sanskrit
OK   https://www.etymonline.com/word/corpse
OK   https://www.etymonline.com/word/corset
```


## [2026-09-06T22:35:11.159Z] AGENT

Done. `data/verification/page-293.json` written; `verify_check.py 293` reports 16/16 nodes, 0 PROBLEM lines.

**Page 293 (book p. 263) — 2 entries (Kwer/Qwer part 2; Krep, Krep-ed-tro), 1 redirect skipped (Kwermi → Wer 2)**

- Roots: 2 confirmed. Nodes: 12 confirmed, 4 plausible. Ref checks: 12 supports, 4 partial, 1 not_found, 6 not_checked. 42 book consultations (POK, WLD I, AHD/Watkins, KLN, SKT, BRT, PHD, NYB, HRN, HUB, CHEUNG, SOD, SNS, PLA, LKT, AFM, MON, BQT).

Plausible (no `disputed`, no `transcription_suspect`):
- Kwer #1 Avestan `čâra; vi-čir` — čārā- is a noun "means, remedy" (BRT 584), not a verb "to mediate"; Pokorny 641 cites čārā but not vīčira-, and Nyberg detaches Av. vīčira- from MP wizīr (< *vi-cṛna-). Root membership still right (Cheung files *ui-kar- under *kar = *kʷer-).
- Kwer #3 Arabic (empty box = wazīr) — Iranian origin backed by Wiktionary/Cheung/Eilers, Asbaghi no. 23, Hübschmann, Moʿin; Lokotsch 2160 and the Arab philologists keep it inside Arabic w-z-r.
- Kwer #9 `noqreh نقره` — Nourai follows Moʿin/Benveniste (BQT 2157 footnote: Sogd. nʾkrtk = nā- + krt- "uncoined"); mainstream (Wiktionary, Arabic lexica) makes it a loan from Arabic nuqra. Chart's own NOTE (cf. سیم < Gk. ásēmon "uncoined") is a genuine argument for the Iranian side.
- Krep #1 Avestan `kerefs; xrafstra` — kərəfš confirmed; the *kʷr̥p-[e]d-tro- "body-eater" analysis of xrafstra- is Pokorny 620 / WP I 486, but both mark it with a question mark and Bartholomae (col. 538) calls it only "wenigstens denkbar".

No extraction errors found: the JSON matches the chart, and Nourai's odd spellings (`kerefs`, `krty\``) are the book's own / Pokorny's and Klein's own.

Citation problems the owner may want noted: BQT:1778 does not contain any of node 2's words (it is گذاردن/گذشتن); BQT:1809 and 1814 could not be landed on exactly (the v3 scan's page map is ~2 pages off above p. 1778); MON:1411,1419 could not be located (خرفستر is absent from the local Moʿin OCR — verified via abadis instead); MON5:809 and AHD:298/300 refer to volumes/editions not on disk.
