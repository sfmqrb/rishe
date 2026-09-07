# Verification process log — verify-page-319


## [2026-09-07T15:49:06.739Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 319 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-319.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-319.json. Write /home/sfmqrb/git/rishe/data/verification/page-319.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 319` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T15:49:08.800Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-07T15:49:09.444Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T15:49:09.462Z] TOOL RESULT

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


## [2026-09-07T15:49:09.979Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-319.txt"
}
```


### [2026-09-07T15:49:09.999Z] TOOL RESULT

```
1	=== PDF page 319 (book page 289) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Magh 2 : to fight  (refs POK:697)
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:697; AHD:1541 | ha-mazan : the warrior ☞So
5	  #2 (parent #1) [Greek] refs=AHD:40,1541; PRT:14 | amazon : woman warrior | NOTE: KLN:59 derives this from Hebrew.
6	    #3 (parent #2) [Latin] refs=None | 
7	      #4 (parent #3) [French] refs=None | 
8	        #5 (parent #4) [Persian] refs=MON5:58 | âmâzon «آمازن ۱» : warrior
9	      #6 (parent #3) [English] refs=AHD:40,1541 | Amazon 1 : woman warrior
10	    #7 (parent #2) [Spanish] refs=KLN:59 | Amazonas : referred to a tribe in South America - a Spanish explorer found their women helping men in battle.
11	      #8 (parent #7) [French] refs=None | 
12	        #9 (parent #8) [Persian] refs=MON5:58 | âmâzon «آمازن ۲» : name of a river
13	      #10 (parent #7) [English] refs=KLN:59 | Amazon 2 : name of a river
14	--- entry 1 ---
15	ROOT [Indo-European] Maghos, Maghu : young; boy, unmarried  (refs POK:696)
16	#1 (parent #0) [Avestan] refs=POK:696; KLN:924 | mağava : unmarried
17	  #2 (parent #1) [None] refs=None | 
18	#3 (parent #0) [Germanic] refs=AHD | magadi : young girl
19	  #4 (parent #3) [English] refs=None | maid, maiden
20	--- entry 2 ---
21	ROOT Maghu -> redirect to Maghos
22	--- entry 3 ---
23	ROOT [Aramaic] Mağšîsa : stone  (refs MON:4036)
24	#1 (parent #0) [Persian] refs=SKT:314; KLN:937; BQT:1938; MON:4036 | marqašîšâ «مرقشیشا» : an iron mineral (ore)
25	  #2 (parent #1) [Arabic] refs=KLN:937 | marqašîtha
26	    #3 (parent #2) [Spanish] refs=KLN:937 | marcaxita
27	      #4 (parent #3) [Middle Latin] refs=KLN:937 | marchasita
28	        #5 (parent #4) [French] refs=KLN:937 | marcassite
29	          #6 (parent #5) [English] refs=KLN:937 | marcasite
30	
```


## [2026-09-07T15:49:13.241Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-319.json",
 "description": "Read source JSON for page 319"
}
```


### [2026-09-07T15:49:13.285Z] TOOL RESULT

```
{
  "pdf_page": 319,
  "book_page": 289,
  "entries": [
    {
      "root": {
        "name": "Magh 2",
        "lang": "Indo-European",
        "refs": "POK:697",
        "gloss": "to fight"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:697; AHD:1541",
          "words": [
            {"translit": "ha-mazan", "gloss": "the warrior", "script": null, "see": ["So"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Greek",
          "refs": "AHD:40,1541; PRT:14",
          "words": [
            {"translit": "amazon", "gloss": "woman warrior", "script": null}
          ],
          "script_extra": null,
          "note": "KLN:59 derives this from Hebrew.",
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Latin",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON5:58",
          "words": [
            {"translit": "âmâzon", "gloss": "warrior", "script": "آمازن ۱"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 3,
          "lang": "English",
          "refs": "AHD:40,1541",
          "words": [
            {"translit": "Amazon 1", "gloss": "woman warrior", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 2,
          "lang": "Spanish",
          "refs": "KLN:59",
          "words": [
            {"translit": "Amazonas", "gloss": "referred to a tribe in South America - a Spanish explorer found their women helping men in battle.", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "MON5:58",
          "words": [
            {"translit": "âmâzon", "gloss": "name of a river", "script": "آمازن ۲"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 7,
          "lang": "English",
          "refs": "KLN:59",
          "words": [
            {"translit": "Amazon 2", "gloss": "name of a river", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Maghos, Maghu",
        "lang": "Indo-European",
        "refs": "POK:696",
        "gloss": "young; boy, unmarried"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:696; KLN:924",
          "words": [
            {"translit": "mağava", "gloss": "unmarried", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": null,
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "magadi", "gloss": "young girl", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "maid, maiden", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Maghu",
        "redirect": "Maghos"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Mağšîsa",
        "lang": "Aramaic",
        "refs": "MON:4036",
        "gloss": "stone"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "SKT:314; KLN:937; BQT:1938; MON:4036",
          "words": [
            {"translit": "marqašîšâ", "gloss": "an iron mineral (ore)", "script": "مرقشیشا"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Arabic",
          "refs": "KLN:937",
          "words": [
            {"translit": "marqašîtha", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Spanish",
          "refs": "KLN:937",
          "words": [
            {"translit": "marcaxita", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Middle Latin",
          "refs": "KLN:937",
          "words": [
            {"translit": "marchasita", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "French",
          "refs": "KLN:937",
          "words": [
            {"translit": "marcassite", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": "KLN:937",
          "words": [
            {"translit": "marcasite", "gloss": null, "script": null}
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


## [2026-09-07T15:49:16.076Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','KLN','SKT','MON','BQT','PRT','WLD','IEC','SYN','BRT','KNT','PHD','NYB','HRN','HUB','FVQ','AFM','PLA','ARY','WEB','FSD']:\n    v=d.get(k)\n    if v is None: print(k,'MISSING'); continue\n    print(k, v.get('kind'), '|', v.get('local_file'), '| offset', v.get('page_offset'), '|', str(v.get('lookup_hint'))[:100])\n\"",
 "description": "Inspect refs_online keys"
}
```


### [2026-09-07T15:49:17.451Z] TOOL RESULT

```
POK archive_djvu | /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt | offset POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177
AHD archive_djvu+website+archive_restricted | /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt | offset 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...i
KLN archive_djvu | /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt | offset KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; d
SKT archive_djvu | /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt | offset leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.
MON website+archive_djvu | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] | offset None | Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin t
BQT archive_djvu+local_scan_ocr | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] | offset vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-bl
PRT archive_restricted | None | offset None | Borrow via IA lending; in-book search https://archive.org/details/originsshortetym00part?q=<word>. E
WLD archive_djvu | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'] | offset Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). | Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it c
IEC archive_djvu | /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt | offset TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n 
SYN archive_djvu | /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt | offset leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discu
BRT archive_djvu | /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt | offset Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration i
KNT archive_djvu | /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt | offset leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part
PHD archive_djvu | /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt | offset leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and glos
NYB archive_djvu | /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt | offset Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at lin
HRN archive_djvu | /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt | offset leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or gr
HUB archive_djvu | /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt | offset leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part 
FVQ archive_djvu | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt'] | offset printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves) | Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p
AFM archive_djvu | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt'] | offset 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image | Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; i
PLA archive_djvu | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt'] | offset 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276). | HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of content
ARY local_scan_ocr | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'] | offset printed page = pdf page + 1 | Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page cita
WEB archive_djvu | /home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt | offset not reliably detected (page_numbers.json sparse); grep headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1
FSD archive_djvu | /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt | offset vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'.
```


## [2026-09-07T15:49:34.897Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; ls | head -60; echo ---; for f in POK_01.txt POK_02.txt POK_03.txt POK_full.txt; do [ -f $f ] && echo \"$f $(grep -c $'\\f' $f)\"; done",
 "description": "List refs dir"
}
```


## [2026-09-07T15:49:35.811Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification; ls page-31*.json; python3 -c \"\nimport json;d=json.load(open('page-317.json'));print(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:3000])\"",
 "description": "Look at an existing verification file"
}
```


### [2026-09-07T15:49:36.375Z] TOOL RESULT

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
---
POK_01.txt 352
POK_02.txt 420
POK_03.txt 415
POK_full.txt 0
```


### [2026-09-07T15:49:37.714Z] TOOL RESULT

```
page-310.json
page-311.json
page-312.json
page-313.json
page-314.json
page-315.json
page-316.json
page-317.json
page-31.json
{
 "entry": 0,
 "root": "Mad",
 "verdict": "confirmed",
 "modern_form": "PIE *mad- (laryngealist *meh₂d-) 'wet, dripping; fat, well-fed', with the derived sense 'food, fattening' — Pokorny 694-695",
 "note": "The root is genuine and standard. Pokorny 694-695 has 'Root/lemma: mad-  Meaning: wet; glossy, fat, well-fed, intoxicating', and Watkins/AHD (1985 ed., p. 38) has 'mad-. Moist, wet; also refers to various qualities of food' — Nourai's gloss 'wet, also food' is essentially Watkins' wording, and the language label 'Indo-European' is right. Walde-Pokorny II 230-232 is the same article. What is remarkable is that Pokorny's article contains almost the whole of Nourai's chart in the same order: 'ai. madati, madate … mada- m. Rauschtrank = av. maδa-; ai. madgu- ein bestimmter Wasservogel, ein Fisch = np. māγ ein Wasservogel; ai. matsya- m., av. masya Fisch (der nasse; Ableitung von einem -es-St. *mades-); mastu- n. saurer Rahm (*mad-stu-) … arm. macun sauer, geronnene Milch … iran. Worte für Dickmilch, so npers. mast, masīdan … lat. madeō, mattus trunken (*madi-to-s) … ahd. mast Futter, got. mats Speise, ags. mete, mnd. mat(e) Kamerad'. Two modern caveats: (a) Cheung (2007) and LIV split the family into *mad¹ 'to become intoxicated' (PIE *med-) and a separate Indo-Iranian *mad 'to curdle', for which no PIE root is set up; (b) the 'fish' member is no longer taken as certain (see node #1).",
 "note_fa": "ریشهٔ هندواروپایی آغازین *mad- (در نگارش امروزی *meh₂d-) به معنی «خیس، تر، چکه‌کننده؛ فربه و پرورده» و از همین‌جا «خوراک»، ریشه‌ای شناخته و پذیرفته است: پوکورنی (ص ۶۹۴–۶۹۵) آن را با معنی «تر؛ چرب، فربه، مست‌کننده» می‌آورد و واتکینز در پیوست فرهنگ American Heritage نیز «mad-. نمناک، تر؛ همچنین دربارهٔ کیفیت‌های خوراک» دارد؛ پس برچسب زبانی و معنای «wet, also food» در نمودار نورایی درست است. نکتهٔ چشمگیر آنکه تقریباً همهٔ شاخه‌های نمودار — سنسکریت madati و mada-، اوستایی maδa-، سنسکریت madgu- برابر «ماغ» فارسی، سنسکریت mastu- و ارمنی macun برابر «ماست» و «ماسیدن»، لاتینی mattus و واژه‌های ژرمنی mast/mats/mete/mate — همه در همان مقالهٔ پوکورنی و به همان ترتیب آمده‌اند، یعنی نورایی مستقیماً از پوکورنی و واتکینز برداشته است. دو نکتهٔ احتیاطی: نخست آنکه چونگ (۲۰۰۷) و فرهنگ LIV دو ریشهٔ *mad «مست شدن» و *mad «بستن، دلمه شدن» را از هم جدا می‌کنند و برای دومی ریشهٔ هندواروپایی نمی‌سازند؛ دوم آنکه پیوند واژهٔ «ماهی» با این ریشه امروز قطعی دانسته نمی‌شود (بنگرید به گرهٔ ۱).",
 "sources": [
  "https://en.wiktionary.org/wiki/mattus",
  "https://en.wiktionary.org/wiki/meat"
 ],
 "ref_check": [
  {
   "ref": "POK:694",
   "status": "supports",
   "note": "POK_full.txt line 57036 ff. (= POK_02.txt line 5645 ff., German original): 'Root/lemma: mad-  Meaning: wet; glossy, fat, well-fed, intoxicating … References: WP. II 231 f., WH. II 6 f.  Page(s): 694-695'. The page number Nourai cites is exactly right, and the article's material list is the source of his whole chart."
  }
 ],
 "consulted": [
  {
   "src": "WLD",
   "where": "Bd. II 230-232 s.v. 'mad-'",
   "stance":
```


## [2026-09-07T15:49:42.178Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Page(s): 69[5-8]\" POK_full.txt | head -20",
 "description": "Find Pokorny pages 695-698"
}
```


### [2026-09-07T15:49:42.243Z] TOOL RESULT

```
57146:Page(s): 696 
57192:Page(s): 695 
57210:Page(s): 697 
57248:Page(s): 696-697 
57287:Page(s): 697 
57302:Page(s): 697 
57342:Page(s): 698 
57522:Page(s): 698 
57544:Page(s): 698 
57561:Page(s): 698
```


## [2026-09-07T15:49:44.495Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '57100,57320p' POK_full.txt",
 "description": "Read Pokorny 695-697 region"
}
```


### [2026-09-07T15:49:44.557Z] TOOL RESULT

```
Mastung, Old English msest' beechnut'; Gothic mats'6\s\\, food'. Old Icelandic matrm., 
Old English metem., Old High German maz n. ds. (Modern High German still in Messer 
from Old High German mezzi-rahs), as well as Gothic matjan'eat, devour ', Old Icelandic 
met/a' slurp ', Old English mettanleed', Middle Low German mat{e) "buddy, friend, esp. 
in the nautical slang ' (Maat), Old High German gamazzo' buddy, friend '; in addition also 
Middle Low German met' pork ', nnd. mett' chopped flesh'. Old High German (actually 
ndd.) Mettwurst {irom andd. *matja-)\ changing through ablaut Old English Old Saxon mos 
"porridge, mash, dish, food'. Old High German muos' cooked, esp. mushy dish, food, 
eating generally ', Modern High German Mus, Gemiise {*madso-). 

References: WP. II 231 f., WH. II 6 f.; Kuiper Nasalpras. 140. 
Page(s): 694-695 

Root / lemma: mahghos, -a 

Meaning: young, servant, servant of god 

Material: Avestan mayava-' unwed, unmarried, single '; 

alb. makth'young hare'; 



Celtic *magus'\n gall. PN Magu-rTx, Proto Irish (Ogam) Maguno-, Old Irish maug, mug 
"slave'; corn, maw, bret. mao^ youngling, servant', cymr. meu-dwy' hermit, servant of God 
'; Fem. corn, mowes 'g\r\', bret. maouez^\N\ie, woman'; Celtic -5/770- derivative in Old Irish 
mam, maam(m)^ a yoke, the condition of a servant, slavery, serfdom, service, servitude '; 
abstract noun Celtic */77a^c»/-a/r/a 'maidenhood, virginity, young femininity' (other 
formations from *maghotis= Gothic magat^e, from which Celtic */77a/r"'/r"'c»/-a/r/a through 
contamination with mak"'k"'o-^V\6, child') in Middle Irish ingen maccdacht^youuig adult girl'. 
Old Irish ro-macdact q\. " fully mature ', mcymr. machteith, acorn, mahtheid^ a maid, 
maiden, virgin ', mcorn. maghteth, maghtyth ds., bret. matez^ maidservant '; nickname 
*magguos\n gall. Mapo-no-sGH, acymr. map, ncymr. malb'son'; double intensification in 
Proto Irish maqqas. Old Irish mace, nir. mac^sou'; 

Gothic magus'knave, boy'. Old Icelandic mggr'son, young man, husband'. Old Saxon 
magu'knave, boy'. Old English mago'son, man, husband, servant'; Fem. *ma{y)wr\n 
Gothic ma\/v/^g\r\' (Gen. maujds). Old Icelandic mser{f\Vk. mey) "girl', Demin. Gothic 
mawilo. Old Icelandic meyla. Old English meowie "small girl'; abstract noun *maghotis 
"young femininity', from which specifically "girl', in Gothic magat^s^youuQ wife, woman'. 
Old English maeget^ {ev\Q\. maid). Old Saxon magath. Old High German magad. Modern 
High German Magd, Demin. Madchen; 

Latvian /77ac(from mags) "small'. 

References: WP. II 228, Feist 3339. 
Page(s): 696 

Root / lemma: mahgh- : mahgh- 

Meaning: to be able; to help; power, sorcerer 

Note: 

Root/ lemma: mahgh-. mahgh-: to be able; to help; power, sorcerer : Root/ lemma: 

mahghos, -a: young, servant, servant of god. 

Material: Old Indie magha-'power, richness, gift', maghavan-, maghavat' strong', Iran. 

magu-. Old pers. magus^ sorcerer, magician ' (out of it gr. \xcxsoc,, Latin magus); 

Maybe alb. {*magh-) math'b'\g, powerful' [common alb. -g > -dh; -k > -//? shift] 

Armenian marthankh^ aid ' ( *mag-thra-); 

gr. Mnxo*^ ". (Doric (JaXC"^). Poet. pHXap ' a'd ', Mnxavr), Doric [jaxava (> Latin machinal) " 
aid, tool, artifice'; 



Gothic Old English magan, Old Icelandic mega, maga, muga, Old Frisian muga, Middle 
Low German mogen. Old High German magan, mugan^ possible, could be, might be, may 
be '; 1. Sg. present Gothic Old Saxon Old High German mag. Old Icelandic ma. Old 
English m^g. Old Frisian mer. Old Icelandic magn, meg(i)nv\. 'power, essence ', Old 
English msegen. Old High German, Old Saxon magan, meg/n6s.; Gothic mahtsi. " power 
', Old High German Old Saxon maht. Old English meaht, might. Old Icelandic mattr ds.; 

Maybe truncated alb. Geg {*mugn) mun, Tosc /77^/7o'' might' [common alb. n > a?^' shift] 

Maybe alb. mund^ defeat' 

Lithuanian magulas^ numerous, much, a lot of; 

Old Church Slavic mogg, mosti^ to be able, to be capable of ', po-mosti, Iterat. po- 
magat/"\r\e\p' etc.. Old Church Slavic mostb, russ. mocb etc. "power, strength ' (= Gothic 
mahts). 

References: WP. II 227, Trautmann 164 f., H. GiJntert, Weltkonig 108 f.; whether E. 
Fraenkel (Lexis 1, 169 f.) rightly gr. pr|xo<; with Lithuanian mokef/" to be able, understand, 
comprehend ' goes back to a root makh-, the other words could go back also in megh-: 
mogh-, compare Tocharian A /770/ra/s "mighty'. 
Page(s): 695 

Root / lemma: mahgh- 

Meaning: to fight 

Material: Gr. Apa^wv, loanword through Aeolic mediation from an Iran, people's name 

*ha-mazan- 'wamor', compare apia^aKapav' (: Aryan kar-^make') ttoAeijeTv. flETaai Hes. 

and aMa^av(ji)5£(; ai pn^sa' (of VN Hamazan-); gr. paxo|jai " fight ', paxn "fight, struggle, 

battle', paxaipa "sword, knife' (fem. to *ijaxu)v "incisive'? Oder Semitic loanword, to hebr. 

mekherah "sword'?). 

References: WP. II 227, WH. II 3, 4. 

Page(s): 697 

Root / lemma: mahg- 

Meaning: to press; to knead 

Material: Gr. jjaynvai, psfjayfjEvri to paaau) (to present s. /77e/7a/r- "knead'), fjOY£U(; " the 

kneading ', MC(Yi<; f. " kneaded mass', \xcxsz\poc, (actually |jaYTpo(;) " cook ', paySaAia "shred 

bread zum Fettabwischen'; poKipa f. " kneading or dough trough; dough tray; hutch '; 



Middle Irish maistrid^ makes butter' {*magis-tr-), bret. /77eza "knead', cymr. maeddu^ 
fight, pushing through the mix ' ( *maged-)\ 

Old Bulgarian mazg, mazat/' anoint, smear', russ. mazb " ointment ', Old Bulgarian 
maslo ' butter, oil, ointment ' ( *mag-slo-), mastb " ointment, fat' ( *mag-sti-), Latvian iz- 
/77^Qze/'circumvent, by-pass, outmaneuver, outsmart '; 

with esp. use in the building of the family of Modern High German machen {irom "knead, 
form, mould, form, join; shaped, suitable, fitting). Old Saxon (g/J-makon' make, erect, 
build'. Old High German mahhon ds.. Modern High German machen. Old English macian 
"make, cause'; Old Saxon gemaco^ comrade, the likes, one's equals ', Old High German 
gimahho^ sharing, joining in, partaking, united, associated, kindred, allied, fellow, common 
' {gimahha^ one who is united in marriage, a consort, spouse, wife, husband '), Old 
English macads., gemsecca^ds., husband ' (Old Icelandic maki^ equal, like, even, on a 
par ' is ndd. loanword). Old High German ga-mah, gi-mah' related, fitting, comfortable ' 
(p'//77a/7 "connection, domestic comfort, chamber '), un-gamah^ malus, minus idoneus ', Old 
English ge-msec^ fitting, suitable, (Old Icelandic makr^ fitting, comfortable ' is ndd. 
loanword); Old Frisian mekn. " marriage ', mekere^ matchmaker'. Middle High German 
mechele^ matchmaking '; from Germanic */775/rd derives Latin mac(h)id^ one who works 
on a scaffold, a mason, bricklayer, one who lays bricks, one who builds with stone '; out of 
it rom. *matsid, whence again Old High German stein-mezzo^ stonecutter'. 

References: WP. II 226 f., WH. II 3, Trautmann 173; 
See also: compare mak-2 and menk-. 
Page(s): 696-697 

Root / lemma: maih-1 

Meaning: to cut down, work with a sharp instrument 

Note: probably actually mai- and s- loose form besides smei- : smei- : smT- " carve, work 

with sharp tools '. 

Material: 1. Old Irish maeF bald, dull, without horns ', acymr. mair maimed, mutilated ', 

ncymr. moer bald, hairless, smooth ' {*mai-lo-s^ broken '); 

2. fltextension: Gothic maitan^\\e\N, hit, cut, clip'. Old Icelandic meita. Old High German 
me/zan'cut, clip'. Old Icelandic meitillm.. Old High German /77e/z//"chiser, Old High 
German stein-meizo^ stonecutter'; in addition Old English mTte, Old High German mTza 
"mite' (probably to gr. |ji5aq " maggot '), perhaps also Old English se-mette, engl. ant, 
emmet. Old High German a-meiza' ant ' ("whittler '); 



Maybe alb. mize, miza^ fly', mize mjaltr bee', mize dheu^ ant'. 

whether also Old Bulgarian medb "ore', russ. medb " copper'? 

3. ^extension: Old Indie methati^ injures ' (expressives //?), gr. |jiTuAo(; "mutilated, 
without horns', (jigtuAAcjo "cut (flesh)'; Old Icelandic meida' injure physically, mutilate, 
destroy ', Middle High German meidem^'(r\a\e horse' (actually "eunuch, castrated man '), 
Gothic *gamaiP-s^ crippled ', wherefore (probably after the court jester) Old High German 
gimeiV crazy, mad ', Middle High German transformed gemeiV full of life, pert, beautiful, 
dear'. Old Saxon gimed. Old English gemad, mceded\emck\.', engl. mad6s.; 

Old Lithuanian ap-maitinti^ wound, hurt ', Latvian /775//a/ "spoil, destroy', Lithuanian 
maTtelis^ castrated, fed for slaughter boar'. Old Prussian nomaytis^ castrated boar', 
ismaitinV lose, shed; suffer a loss, be defeated ' (as it. perdere); different MiJhlenbach- 
Endzelin II 552. 

References: WP. II 212, Holthausen Altwestn. Wb. 193, 194. 
Page(s): 697 

Root / lemma: maih-2 {moih-1) 

Meaning: to smudge, dirty 

Material: Gr. jjiaivu) (Aor. spiav) "sully, besmirch', piaapa n. " maculation ', fjiap6(; 

( *miuaros'7) "besudelf, piai-cpovoq "with murder befleckt'; 

Old English malu. " blot, stain, taint, blemish'. Old High German meilx^., meilai. ds.; 
Lithuanian PI. mieles, Latvian m/'e/es 'yeast'; perhaps also Lithuanian maiva' marsh 
meadow '? 

References: WP. II 243. 
Page(s): 697 

Root / lemma: mahkh-o-s, -(s)lo- 

Meaning: wild, unbridled, bold 

Material: Old Indie /775/r/7a- "alert, awake, smart, funny, exuberant ', m. " sign of joy, display 

of happiness, celebration '; 

Maybe alb. makth'bogey, nightmare'. 

gr. jJCiX^og "horny, lustful; uppig (from Weibern); in wilder lust tobend'. 

References: WP. II 226. 



Page(s): 699
```


## [2026-09-07T15:50:01.452Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"maghu\\|magh-\\|Amazon\\|magadi\\|mægden\\|magaths\" AHD_watkins1985.txt | head -30",
 "description": "Grep Watkins for magh roots"
}
```


### [2026-09-07T15:50:01.506Z] TOOL RESULT

```
710:magh-'. To be able, have power. 1. Germanic *snag- in: a. Old English magan, to be able: May; b. Old French esmaier, to frighten: DISMAY. 2. Germanic suffixed form *mah-ti-, power, in Old English miht, power: MIGHT!. 3. Germanic suffixed form *mag-inam, power, in Old English mzgen, power: MAIN}. 4. Suffixed length- ened-grade form *magh-and-, “that which enables,” in Greek (Attic) mékhané, (Doric) madkhand, device: MA- CHINE, MECHANIC, (MECHANISM), (MECHANO-). 5. Possi- bly suffixed form *magh-u- in Old Persian magus, member of a priestly caste (< “mighty one”): (MAGI), (MAGIC), MAGUS; ARCHIMAGE. [Pok. magh- 695.]
711:magh-. To fight. Hypothetical Old Iranian *ha-maz-an-,
712:“warrior” (*ha-, with < *sm-; see sem-'), possibly borrowed into Greek as Amazén, Amazon: AMAZON. [Pok. magh- 697.]
713:maghu-. Young person of either sex. Suffixed form *magho-ti- in Germanic *magadi-, with diminutive *ma- gadin-, in Old English mezgden, virgin: MAID, MAIDEN. [Pok. maghos 696.]
1235:AMATIVE amma AMATORY amma AMAZON magh-2 AMBAGE ag- AMBASSADOR ag- AMBERGRIS gher-3 AMBI- ambhi AMBIDEXTROUS deks- AMBIENT ei-1 AMBIGUOUS ag- AMBITION ei-1
1257:ARABLE are- ARBALEST arku- ARC arku- ARCADE = arku- ARCANE arek- ARCH! = arku- -ARCH arkhein ARCHAEO- arkhein ARCHAEOPTERYX pet- ARCHAIC arkhein ARCHANGEL angelos ARCHEGONIUM gene= ARCHER arku- ARCHETYPE (s)teu- ARCHI- arkhein ARCHIMAGE magh-! ARCHIPELAGO piak-1 ARCHITECT teks- ARCHITRAVE treb- ARCHIVES arkhein ARCHIVOLT arku-
1429:DIN dhwen- DINGUS _{enk-1 DINOSAUR dwei- DINOTHERE dwei- DIOCESE weik-! DIOECIOUS weik-1 DIOICOUS_ weik-1 DIOPTER oOkW- Dioscuri_ deiw-, ker-3 pip dheub- DIPHTHERIA deph- DIPHYODONT bheue- DIPLO- dwo- DIPLOCARDIAC kerd-1 DIPLODOCUS dek-1 DIPLOE dwo- DIPLOID pel-3 DIPLOMA dwo- DIPNOAN pneu- DIRE dwei- DIRECT reg-! DIRNDL tek- DISARM ar- DISASTER ster-3 DISBURSE bursa DISCERN krei- DISCIPLE dek-! DISCIPLINE dek-? DISCOMFIT dhé-1 DISCORD kerd-1 DISCOURSE kers-2 DISCRIMINATE krel- DIscuss kwét- DISDAIN dek-1 DISEMBOGUE beu-! DISFIGURE dheigh- DISGUST geus- DISK deik- DISMAL deiw-, mel-5 DISMAY magh-! DISMISS (s)meit(9)- DISPARATE pere-1 DISPATCH ped-! DISPEL pel-6 DISPENSE (s)pen- DISPERSE (s)preg- DISPLAY plek- DISPOSE apo- DISPUTE peu- DISQUISITION quaerere DISRUPT reup- DISSECT sek- DISSEMINATE 6-1 DISSENT sent- DISSERTATE ser-3 DISSIDENT sed-1 DISSILIENT sel-4 DISSIPATE swep-2 DISSOCIATE sekw-1 DISSOLVE leu-! DISSONANT swen- DISSUADE swad- DISTANT sta- DISTEND ten- DISTICH steigh- DISTINGUISH _ steig- DISTORT terkw- DISTRACT tragh- DISTRAIN  streig- DISTURB twer-! DITCH dhigw- DITTO deik- DITTY deik- DIURETIC wers-2 DIURNAL deiw- DIVA deiw- DIVARICATE wa- DIVE dheub- DIVERGE wer-3 DIVERT wer-3 DIvEs_ deiw- DIVIDE weidh- DIVINE! deiw- DIVINE? deiw- DIVULSION wel-4 Dizzy dheu-!
1788:MACERATE mag- MACHICOLATE kWel-1 MACHICOLATION kwel-1 MACHINE magh-1 MACHO mas
1792:MAGI magh-!
1793:MAGIC magh-' MAGISTERIAL meg- MAGISTRAL meg- MAGISTRATE meg- MAGMA mag- MAGNANIMOUS ane-, meg- MAGNATE meg- MAGNIFIC meg- MAGNIFICENT meg- MAGNIFICO meg- MAGNIFY meg- MAGNILOQUENT meg-, tolkw- MAGNITUDE meg- MAGNUM meg-
1794:MAGUS magh-! MAHARAJAH meg-, reg-! MAHARANI meg-, reg-! MAHARISHI meg- MAHATMA ��tmen-, meg- MAHAYANA ei-1, meg- MAHOUT meg-, mé-2 Mata ma-2
1795:MAID maghu-
1796:MAIDEN maghu- MAIEUTIC ma-2 MAIGRE mak-
1801:MAIN! magh-! MAINTAIN man-2, ten- MAJESTY meg-
1831:MAY magh-!, meg- MAYHEM mai-t MAYOR meg- MAZAEDIUM _ aidh-, mag-. MAZER smé-
1841:MEATUS mei-1 MECHANIC magh-1 MECHANISM magh-! MECHANO- magh-! MECONIUM mak-1 MECOPTERAN miak-, pet- MEDDLE meik- MEDIAL medhyo- MEDIAN medhyo- MEDIASTINUM medhyo- MEDIATE medhyo- MEDICAL med- MEDICATE med- MEDICINE med- MEDICO med- MEDIEVAL alw-, medhyo- MEDIOCRE medhyo- MEDITATE med- MEDITERRANEAN medhyo-, ters- MEDIUM medhyo- MEDLEY meik- MEDULLA (s)mer-3 MEED mizdho-
1869:MICROPYLE pulé MICTURATE meigh- MID! medhyo- MIDDLE medhyo- MipcaRD medhyo- MIDGE mu-2 MIDRIFF krep- MIDWIFE me-2 MIGHT! magh-! MIGRAINE ker-1 MIGRATE mei-1 MIL! gheslo-
```


## [2026-09-07T15:50:02.663Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^amazon\\|^Amazon\\|Amazon\" KLN_1966.txt | head -20; echo \"=== marcasite ===\"; grep -n -i \"marcasite\\|marqash\\|markasit\" KLN_1966.txt | head -20",
 "description": "Grep Klein for Amazon and marcasite"
}
```


### [2026-09-07T15:50:02.735Z] TOOL RESULT

```
2409:Amazon,  n.,  a  member  of  a  race  of  female  war¬ riors  in  Scythia  ( Greek  mythol.)  —  L.,  fr.  Gk. ’A|za£d>v,  which  prob.  derives  fr.  Heb.  ammftz, ‘strong’.  The  form  of  the  word  ’Apatov  was prob.  influenced  by  the  folk  etymology  accord¬ ing  to  which  ’Apia^tov  lit.  means  ‘without breast’,  fr.  A-  (see  priv.  pref.  a-)  and  pa£6 ?, ‘breast’  (the  Amazons  are  said  to  have  cut  off their  right  breasts  in  order  to  use  the  bow  with more  ease).
2410:Derivatives:  Amazon-ian,  adj.,  and  n.,  Amazon¬ ism,  n.
2411:Amazon,  n.,  name  of  the  largest  river  in  the  world in  volume.  —  Sp.  Amazonas,  from  prec.  word; so  called  by  Francisco  Orellana  after  his  battle with  the  Tapuyas  (in  1541),  in  allusion  to  the circumstance  that  the  women  of  the  tribe helped  the  men  in  their  fight.  Cp.  next  word, amazonite,  n.,  a  green  variety  of  microline  (min¬ eral.)  —  Formed  with  subst.  suff.  -ite  from  the name  of  the  Amazon  River,  near  which  it  occurs, ambages,  n.  pi.,  a  roundabout  way.  —  L.  am¬ bages,  ‘a  roundabout  way’,  lit.  ‘a  going  round’, compounded  of  ambi-,  ‘about’,  and  ag-,  length¬ ened  form  of  the  stem  of  agere,  ‘to  move,  drive’. See  ambi-  and  agent,  adj.,  and  cp.  ambiguous. Cp.  also  amt,  ambassador,  embassy.  For  ag-, lengthened  form  of  the  stem  of  agere,  cp.  L.  in- dag  are,  ‘to  trace  out,  investigate’,  which  is  form¬ ed  fr.  ind(u)-,  ‘in’,  and  ag-,  lengthened  form  of the  stem  of  agere  (see  indagate).
5272:Boedromion,  n.,  name  of  the  3rd  month  of  the Attic  Greek  calendar  (corresponding  to  August- September).  —  Gk.  Bo7)8pop,u*>v,  fr.  BoijSpopua (pi.),  ‘the  games  in  memory  of  the  aid  given  by Theseus  against  the  Amazons’,  fr.  po^Spoao^, ‘running  to  aid’,  lit.  ‘running  on  hearing  a  cry’, fr.  (3ot),  ‘a  cry,  shout’,  and  -8p6[xoi;,  ‘running’, which  is  rel.  to.  Spoken;,  ‘a  running’.  For  the first  element  see  reboant  and  cp.  Boethusian,  for the  second  see  dromedary.
17845:hippoid,  adj.,  resembling  a  horse  (pool.)  —  Com¬ pounded  of  hippo-  and  Gk.  -oeiSrp,  ‘like’,  fr. slSo4,  ‘form,  shape’.  See  -old  and  cp.  equoid. Hippolyte,  n.,  an  Amazon,  daughter  of  Ares; taken  prisoner  by  Theseus  ( Greek  mythol.)  — L.,  fr.  Gk.  T-mroXEiTir),  fem.  of  the  name  'I77776- Xuto?.  See  Hippolytus  and  cp.  next  word. Hippolyte,  n.,  a  genus  of  prawns  ( zool .)  —  ModL., named  after  the  Amazon  Hippolyte.  See  prec. word.
=== marcasite ===
22893:Derivatives:  marbl-ed,  marbl-y,  adjs. marc,  n.,  refuse  of  fruit,  esp.  of  grapes.  —  F.,  lit. ‘something  trodden  or  beaten’,  fr.  marcher,  ‘to walk’,  in  the  original  sense  of  this  verb:  ‘to tread’.  Sec  march,  ‘to  walk’, marcasite,  n.,  a  native  iron  disulfide  FeSa  (min¬ eral.)  —  F.  marcassite,  fr.  ML.  marchasita,  fr. Sp.  marcaxita  (ModSp.  marcasita),  fr.  Arab. marqashithd,  fr.  Pers.  marqashishd. marcclla,  n.,  a  cotton  quilting.  —  Lit.  ‘of  Mar¬ seilles',  fr.  F.  Marseille,  fr.  L.  Massilia.  Cp. Marseillaise,  Marseilles.
```


## [2026-09-07T15:50:28.159Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\ndef leafof(path, lineno):\n    txt=open(path,encoding='utf8',errors='replace').read().split('\\n')\n    pre='\\n'.join(txt[:lineno])\n    return pre.count('\\f')\nfor ln in (2409,2411,22893):\n    print(ln, 'leaf', leafof('KLN_1966.txt',ln))\nEOF\necho \"=== SKT marcasite ===\"; grep -n -i \"marcasite\\|marchasita\" SKT.txt | head",
 "description": "Compute Klein leaves; grep Skeat"
}
```


### [2026-09-07T15:50:29.879Z] TOOL RESULT

```
2409 leaf 43
2411 leaf 43
22893 leaf 503
=== SKT marcasite ===
```


## [2026-09-07T15:50:30.011Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== MON part1/2 مرقشیشا / آمازن ===\"; grep -n \"مرقشیشا\\|مرقشیش\\|آمازن\" MON_part1.txt MON_part2.txt | head -20; echo \"=== BQT v4 ===\"; grep -n \"مرقشیشا\\|مرقشیش\" incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v3_pages.txt BQT_v1_pages.txt BQT_v2_pages.txt 2>/dev/null | head -20",
 "description": "Grep Persian sources for marqashisha / amazon"
}
```


### [2026-09-07T15:50:30.115Z] TOOL RESULT

```
=== MON part1/2 مرقشیشا / آمازن ===
MON_part1.txt:80276:اطلاق شود؛ مرقشیشا حجر النور؛؟ حجر 
=== BQT v4 ===
incoming/BQT/BQT_v4_pages.txt:727:و ایرانیان آلرا بسورمرقشیشا ومارقشیشا نقل کرده‌اند « نخب‌الذخائر ص ۱۵ ح 2 > . در سربافی
incoming/BQT/BQT_v4_pages.txt:3025:مرقشیشا * - بسنی مارقعیعا است هرگ - بنم اول وسکون ثالی و کاف
BQT_v1_pages.txt:10799:جوهری است ت که آنرا مرقشیشا خوانند وبعربی
BQT_v1_pages.txt:13315:عملی حم‌هست که از نقره و مرقشیشاکه یکی از
BQT_v2_pages.txt:21841:           ‫بلغت ہوتانی نوعی از مرقشیشا باشد ‪.‬‬            ‫فارسیان عکیندند وجشن سازند بنا برقاعده‌کلیه‬
BQT_v2_pages.txt:22117: ‫د یگ بر دینگ = بکسراولوسکون‬                     ‫مرقشیشاست » وآنرا دیفروجس بحذف الف یز‬
BQT_v2_pages.txt:25869:‫روصه دورخ بار ‪ -‬کنابه از‬                                ‫مرقشیشا کوبند و بعربی <جرالنور خوانند و در‬
```


## [2026-09-07T15:50:52.209Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nfor path,leaf in (('KLN_1966.txt',43),('KLN_1966.txt',503)):\n    pages=open(path,encoding='utf8',errors='replace').read().split('\\f')\n    p=pages[leaf]\n    print('=====',path,leaf, 'len',len(p))\n    print(p[:300].replace('\\n',' | '))\n    print('...TAIL...')\n    print(p[-300:].replace('\\n',' | '))\nEOF",
 "description": "Inspect Klein leaves 43 and 503 heads"
}
```


### [2026-09-07T15:50:53.638Z] TOOL RESULT

```
===== KLN_1966.txt 43 len 11469
I.-E.  *am-ro-, fr.  base  *am-,  ‘bitter’,  which  is  rel.  to  *omo-. Taw,  unripe’,  in  OI.  amah,  ‘raw,  unripe,  un¬ cooked’,  Gk.  cop.6<;,  of  s.m.  See  omo-,  ‘raw,  un¬ ripe’,  and  cp.  amargoso,  maraschino,  margosa, and  the  second  element  in  picamar.  For  the  -re¬ formative 
...TAIL...
p6<no:;  is  ‘fragrant’.  (For  the exquisite  smell  of  ambrosia  cp.  Homer,  Odys¬ sey,  1 8,  192-3.)  ’ApiPpoaio?  is  prob.  a  Semitic loan  word,  with  the  original  meaning  ‘as  fra¬ grant  as  ambergris;  pertaining  to  amber',  and d|xPpooia  stands  for  apppoaia  £8<o8y),  ‘amber¬ 
===== KLN_1966.txt 503 len 11717
anx  cat. | many,  adj.  and  n.  —  ME.  mani,  moni,  meni,  fr. OE.  manig,  monig,  mxnig,  rel.  to  OS.  manag. Late  ON.  mangr,  Dan.  mangen,  Swed.  mangen, OFris.  manich,  menich,  MDu.  menich,  Du. menig,  OHG.  manag,  MHG.  manec,  G.  munch, Goth,  manags,  ‘many  a,  many’,  and  cog
...TAIL...
 marc,  mush,  ‘a  march  on  foot  . Several  philologists  derive  OF.  marcher  fr. Frankish  *markdn,  ‘to  mark,  to  imprint  (one’s steps)’ ;  see  mark,  ‘boundary ;  sign  .  It.  marciare and  Sp.  marchar ,  ‘to  march’,  are  borrowed  tr. | F.  marcher. | march,  n.,  a  walking.  —  MF.  (
```


## [2026-09-07T15:50:54.179Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; wc -l MON_part1.txt MON_part2.txt; grep -n \"\\[pdf page\\|\\f\" -c MON_part1.txt 2>/dev/null; python3 -c \"\nt=open('MON_part1.txt',encoding='utf8',errors='replace').read();print('ff',t.count(chr(12)));print(t[:400])\"",
 "description": "Inspect MON text files"
}
```


### [2026-09-07T15:50:55.639Z] TOOL RESULT

```
  99339 MON_part1.txt
  94500 MON_part2.txt
 193839 total
0
ff 0
0 
2 


چم 
نسم ی 


تمه موی موم 
3 


ماما نا موس ملاس 
روم و3 


2 
7 
س 


همجمج مد هعرج ی وه جر ج مهو موجه و وید جع مج وی ۶ج و وم مب و وج 5 
ادا ما ما زو ماه مرو ماخ( نوم شام 4و منم مخ نامه مدش نامع 

مه مر وه ود 

3 ور 133131313 


هم مشب جج جب بیج چم مدوجو 
چم وم 
جر 


درل ولو ونر نو تلا رت 
11 


مج جرج جر یی میج 6و یوج هو هجوج وی یویر جر دم مور و 555 
و ده ها وی مزا موی ماما میو و موه ومد
```


## [2026-09-07T15:51:19.276Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^maid,\\|maid,  n\\.\\|maiden,  n\\.\" KLN_1966.txt | head; echo ---; python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf8',errors='replace').read().split('\\n')\nimport sys\nfor i,l in enumerate(t):\n    if 'maid,' in l and 'magath' in l.lower() or ('maiden' in l and 'mzgden' in l) :\n        print(i+1, l[:600])\nEOF",
 "description": "Find Klein maid entry"
}
```


### [2026-09-07T15:51:20.656Z] TOOL RESULT

```
16252:gleemaiden,  n.,  a  female  minstrel  (archaic).  — OE.  gleo-mxgden,  ‘female  minstrel’.  See  glee and  maiden.
22582:maid,  n.  —  Shortened  fr.  maiden.
22583:Derivative:  maid-ish,  adj. maidan,  n.,  an  open  space  in  towns  of  India.  — Hind,  and  Pers.  maydan,  fr.  Arab,  maydan. maiden,  n.  —  ME.  meiden,  fr.  OE.  mtegden,  di- min.  of  magged,  mtegd,  ‘maid’,  which  is  rel.  to OS.  magath,  OFris.  maged,  megith,  OHG.  ma- gad,  MHG.  maget,  ‘virgin,  maid',  G.  Magd, ‘maid,  maidservant’,  Madchen,  ‘girl,  maiden, maid’  (prop,  contraction  of  Magdchen,  ’a  little maid  or  maidservant’),  OE.  mago,  ‘son,  man, attendant,  servant’,  ON.  mbgr,  ‘son’,  Goth. magus,  ‘boy,  servant’,  magaps,  ‘virgin’,  and cogn.  with  Avestic  mayava-,  ‘unmarried’,  OIr. maug ,  mug,  ‘slave’,  and  prob.  also  with  Olr. macc,  W.  mab,  ‘son’.  Cp.  may,  ‘maiden  .  Cp. also  Mac-.
23566:Merlin,  n.,  in  medieval  legend,  a  Welsh  magician and  seer  who  lived  at  King  Arthur’s  court.  — ML.  Merlinus,  fr.  W.  Merddin,  Myrddin,  fr. OCeltic  *  Mori-dunon,  a  name  lit.  meaning  ‘of the  seahill’,  fr.  *mori,  ‘sea’,  and  ‘dunom,  ‘hill’. See  mere,  ‘sea’,  and  dun,  ‘hill’, merlon,  n.,  the  solid  part  of  a  battlement.  F. merlon,  fr.  It.  merlone,  augment,  of  merlo,  merla, ‘battlement’,  prob.  contraction  of  mergola,  di- min.  formed  fr.  L.  merge.?,  ‘a  two -pronged  pitch- fork’,  lit.  ‘that  which  is  used  for  plucking  off’, rel.  to  merges,  ‘sheaf’,  and  possibly  cogn.  with Gk.  dpipYEiv,  ‘to  gather  (fruit,  etc.)’,  opop- yvuvai,  ‘to  wipe’,  and  OI.  mrjati,  ‘wipes’, mermaid,  n.  —  Lit.  ‘maid  of  the  sea’,  fr.  ME.
---
22583 Derivative:  maid-ish,  adj. maidan,  n.,  an  open  space  in  towns  of  India.  — Hind,  and  Pers.  maydan,  fr.  Arab,  maydan. maiden,  n.  —  ME.  meiden,  fr.  OE.  mtegden,  di- min.  of  magged,  mtegd,  ‘maid’,  which  is  rel.  to OS.  magath,  OFris.  maged,  megith,  OHG.  ma- gad,  MHG.  maget,  ‘virgin,  maid',  G.  Magd, ‘maid,  maidservant’,  Madchen,  ‘girl,  maiden, maid’  (prop,  contraction  of  Magdchen,  ’a  little maid  or  maidservant’),  OE.  mago,  ‘son,  man, attendant,  servant’,  ON.  mbgr,  ‘son’,  Goth. magus,  ‘boy,  servant’,  magaps,  ‘virgin’,  and cogn.  w
```


## [2026-09-07T15:51:29.298Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; ls; echo ===; python3 -c \"\nt=open('KLN_1966.txt',encoding='utf8',errors='replace').read().split(chr(10))\nfor ln in (22582,22893):\n    print(ln,'leaf', chr(10).join(t[:ln]).count(chr(12)))\"",
 "description": "List all refs and compute Klein leaves"
}
```


### [2026-09-07T15:51:30.799Z] TOOL RESULT

```
Exit code 1
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
SKT.txt
SNS_pages.txt
SNS.txt
SOD_pages.txt
SOD.txt
SPG_keilinschriften1881.txt
SYN.txt
TAD_pages.txt
TAD.txt
tessdata
TLM.txt
UNV.txt
WEB_vol1.txt
WLD_band3.txt
ZAP.txt
(eval):1: == not found
```


## [2026-09-07T15:51:38.303Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf8',errors='replace').read().split('\\n')\nfor ln in (22582,22893):\n    print(ln,'leaf', '\\n'.join(t[:ln]).count('\\f'))\np=open('SKT.txt',encoding='utf8',errors='replace').read().split('\\f')\nprint('SKT leaves',len(p))\npg=p[334]\nprint('--- SKT leaf 334 head ---'); print(pg[:400])\nimport re\nprint('marc' in pg.lower())\nEOF\necho \"=== grep SKT variants ===\"; grep -n -i \"marcas\\|markas\\|marchas\" SKT.txt | head",
 "description": "Klein leaves and Skeat page 314"
}
```


### [2026-09-07T15:51:39.727Z] TOOL RESULT

```
22582 leaf 496
22893 leaf 503
SKT leaves 657
--- SKT leaf 334 head ---
ntrodactioo  of  new Mm.  (.Ck  )  Ck.  i^i>^,  new:  -Koyitx, k  Xv^ac.  discourse,  from  \iym»,  to _•«  new  ^below),
W,    •   oovicc     (L.  —  Gk.)     L.
>Gk.  rt^urof,  lit.  new  planted,
ice. •Gk,  vto-v.  new;  ^vr-^v,
.  |^*wt>,  from  ^««y,lo  grow,
Allied  to  Be.
.*tl    (L -Gk.)    L.   Mott'
r»vr«^mff,    novel.   —  Gk.
iparstive  of  Woi,  new;   sec
M.  E.  MTUv;   A.  S.   m
False
=== grep SKT variants ===
```


## [2026-09-07T15:51:51.991Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources; python3 -c \"\nimport json;d=json.load(open('refs_online.json'));\nfor k in ['SKT','MON','BQT','PRT','AHD','KLN']:\n    print(k, json.dumps(d[k],ensure_ascii=False)[:700]); print()\n\"",
 "description": "Check SKT/MON bibliographic details"
}
```


### [2026-09-07T15:51:53.285Z] TOOL RESULT

```
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c

PRT {"title": "E. Partridge, Origins: A Short Etymological Dictionary of Modern English, New York 1958", "edition_found": "1958 (lending-only copies)", "kind": "archive_restricted", "url": "https://archive.org/details/originsshortetym00part (1958 1st ed.) ; originsetymologi0000part_j9t3 (4th ed. 1966) ; originsetymologi0000part (Routledge 2009) — all lending", "identifier": "originsshortetym00part (also originsshortetym0000unse, bwb_P8-AVM-445, 1958)", "local_file": null, "page_offset": null, "lookup_hint": "Borrow via IA lending; in-book search https://archive.org/details/originsshortetym00part?q=<word>. Entries are alphabetical with numbered sub-senses.", "notes": "RE-SEARCH 2026-09: 8 lending

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
```


## [2026-09-07T15:52:03.078Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\np=open('SKT.txt',encoding='utf8',errors='replace').read().split('\\f')\nimport re\nfor i,pg in enumerate(p):\n    low=pg.lower()\n    if 'march' in low and 'marble' in low:\n        print('leaf',i,'-> printed ~',i-20)\n        print(pg[:1500])\n        break\nEOF",
 "description": "Locate M section in Skeat"
}
```


### [2026-09-07T15:52:04.494Z] TOOL RESULT

```
leaf 296 -> printed ~ 276
 E. markis.  —  O.  F.  marJh's,  later  marquis.  *  a marqaene,  goveranur  of  a  frontirc  town  ;' Cot  —Low  L.  manhensis,  %  prefect  of  the marches,  —O.  H.  G.  marcha,  a  march  or boundary.
remark,  to  take  notice  of.  (F.-I« and  Teut.)  F.  remarquer,  to  mark,  note, heed.*-L.  re-,  again;  marqutr,  to  mark, from  marguf,  sb.  a  mark;  see  Mark (above).
Mark  (2),  a  coin ;  see  Mark  (1).
Market ;  see  Merit.
Marl,  a  rich  earth.  (F.  -  L.)  O.  F. marit  ^F.  tnarju).  m  Low  L.  tnargiia, dimiD.  of  Low  L.  mar^^  marl  (PUny).
Marline  ,  see  Mar.
Marmalade ;  see  Melltfluoiu.
Marmoset,  a  small  Aitieric3n  monkey, (F.  — L.)  Much  older  than  the  discovery of  America ;  M.  E.  marmostttt,  a  kind  of ape  (Maundeville,  p.  aio).  —  O.  F.  mar- moset, F.  marmoHset, '  the  cock  of  a  cistern or  fountain,  any  flntick  image  from  who^e leats  water  trllleth,  any  puppet  or  andck;' Cot.  Thus  it  meant  a  grotesque  creature, '^fiS-  A  grotesque  ornament  on  a  fountain. Kormeci.  by  a  Parisian  change  of  r  to  /,  as in  chaise  for  ehaire,  (a  chnir).  from  Low  L. marmorelum,  a  thing  made  in  marble,  ap- plied to  fountains.  [Thus  the  rtu  dts  mar- mousfti  in  Paris  was  called  in  Low  Latin xticut  marmtrrtterttm ;  Littri.]  —  L.  marmor, marbie ;  sec  Marble.  %  This  seems  to  be quite  CDiitcL;  at  the  same  time,  the  trans- frrmce  in  sense  from  Mrinklng-fountain'  t
```


## [2026-09-07T15:52:16.243Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls data/extracted/ | head; grep -rl \"SKT\" data/verification/sources/*.md 2>/dev/null; grep -n \"SKT\" data/verification/sources/SOURCE_MATRIX.md | head",
 "description": "Look for bibliography of abbreviations"
}
```


### [2026-09-07T15:52:16.318Z] TOOL RESULT

```
batch
NEXT_CHUNK
RETRY.txt
test
data/verification/sources/SOURCE_MATRIX.md
32:- **SKT** — W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967
33:  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt`
188:- **SKT** — W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967
189:  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt`
```


## [2026-09-07T15:52:27.532Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for f in LKT.txt DOZ.txt DEV.txt PHN.txt AFM.txt AFM_pages.txt PLA_pages.txt incoming/PLA/PLA_pages.txt FVQ_pages.txt WEB_vol1.txt FSD_vol3.txt FSD_vol2.txt AFA.txt LAM.txt; do [ -f \"$f\" ] && echo \"--- $f\"; [ -f \"$f\" ] && grep -n -i \"marcasit\\|marqash\\|markasit\\|marchasit\\|marcaxit\\|مرقشیث\\|مرقشیشا\" \"$f\" | head -6; done",
 "description": "Grep western sources for marcasite"
}
```


### [2026-09-07T15:52:29.090Z] TOOL RESULT

```
--- LKT.txt
3180:1374.  Arain.  makkasitä: 'Schwefelkies' [vielleicht  wegen  der Spren- kelung  nach  syr.  kessä  'Spreu'  so  ge- nannt; im  übrigen  ist  das  Wort  noch nicht  erklärt],  hieraus  ar.  markasitä Bezeichimng  der  'Kiese'  mit  Ausnahme derer  von  Antimon  und  Wismuth  [vgl. kulil,  hier  Nr.  1227,  und  itmld,  hier Nr.  918]  und  ferner  sp.  kat.  marcasita, marquesita,  pg.  marcasita,  marquezita [Constancio  Dice  677  c],  frz.  marcassite, it.  marcassita;  engl,  marcasite,  dtsch. Markasit  'rhombische  Modifikation  des Eisenkieses'.  (Devic  DEt  157.  Eguilaz 444.  A.  Sadebeck,  Über  den  Namen , Markasit".    Im  Neuen  Jahrbuch  für
5375:markasitä  1374
5813:JUacheier  1497 Madapolam  1342 Magazin  1362 Maharadscha  1692 Mah-Jong  1338  a Mamluk  1384 Mammon  1386 Mammut  1385 M'indarin  1400 Mandoline  2015 Mandarin  1400 Mango  1393 Mangrove  1394 Manguxte  1395 Manichäer  1397 Jlf«MM«  1398 manna  ahd.  1398 Marabu  1410 Marienkäfer  1417 Markab  St.  1420 Markasit  1374
6101:madapollam  1342 madias  1345 magazine  1362 maharajah  1692 mah-djong  1338  a mahout  1352 mamnluke  1384 mamelttke  1384 manihmk  1384 mammon  1386 »«ammuife  1385 manatee  541 mandarin  1400 mangis  1395 mangle  1394 mango  1393 mangosteen  1395 mangrove  1394 marigustin  1395 wafwn«  1398 marabou  1410 marcasite  1374 marchpane  1452 /»/rtsfc  1436 masque  1436 mattrexs  1446 meerschauin  1416 Messiah  1437 mikado  1468 minarct  1463  a J/0(/J*«  (Great)  1494 mohair  1497 moZ/a  1448 moloch(ize)  1379 wionsoow  1451 moolah  1448 tnoonshee  1512 mordechi  1478 mordishee  1478 morocco  1406 mosÄ;  1435 moslem  1516  a mosque  1435 »woxa  1480 moxibustion  1480 /»McÄ;  71
7306:madeixa  476 ■mahona  1449 I  manä  1398 i  mandil  1391 i  mandonguilla  355 I  maquila  1373 i  maravedi  1515 [  marcasita  1374 I  marfega(ssa)  1413
8241:marcasita  1374
--- DOZ.txt
--- DEV.txt
3848:Marcaxita,  esp.  voy.  Marcassite.
3849:Marchasita,  b.  lat.  voy.  Marcassite.
--- PHN.txt
--- AFM.txt
--- AFM_pages.txt
--- incoming/PLA/PLA_pages.txt
--- FVQ_pages.txt
--- WEB_vol1.txt
112772:mir-ca-sit/ic, mär-çå-sit'ic-ăl, a. pertaining to marcasite; of the nature of marcasite.
--- FSD_vol3.txt
--- FSD_vol2.txt
--- AFA.txt
--- LAM.txt
```


## [2026-09-07T15:52:41.074Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== DEV Marcassite ===\"; grep -n -i \"marcassite\" DEV.txt | head; echo; sed -n '/Marcassite/,+25p' DEV.txt | head -60",
 "description": "Read Devic marcassite entry"
}
```


## [2026-09-07T15:52:41.976Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '112765,112775p' WEB_vol1.txt; echo \"=== DOZ ===\"; grep -n -i \"marcas\\|marques\" DOZ.txt | head",
 "description": "Webster marcasite entry and Dozy"
}
```


### [2026-09-07T15:52:42.495Z] TOOL RESULT

```
=== DEV Marcassite ===
1683:Marcassite.  Pyrite  de  fer.  Esp.  marquesita ,  autrefois  mar- caxita,  portug.  marquezita,  ital.  marcassita,  bas  lat.  mar- chasita.  De  l'arabe  Ux^ïyo  marqachithâ ,  que  Boctbor  écrit Ikjuioyo  marqachUâ ,  en  persan,  AamjUmJ>w<>  marqachicha  (Ri- chardson).  La  première  orthographe  est  celle  de  Razi (man.  déjà  cité,  fol.  5o  recto)  et  celle  du  traité  d'alchimie de  Djabir  (Géber),  man.  n*"  1080  du  suppl.  arabe  de  la Bibl.  nat.  folio  6  recto  et  passim,  et  en  général  la  seule que  j'aie  rencontrée  dans  les  manuscrits.  Aussi  je  soupçonne fort  le  2fJi*.jj*t:iyA  marqachicha  ci -dessus  d'être  une  fausse lecture,  causée  par  la  facile  confusion  du  c2>  th  avecle  ^ji  ch.
3846:Marcassita,  ital.\o\.  Marcassite.
3847:Marcassite.
3848:Marcaxita,  esp.  voy.  Marcassite.
3849:Marchasita,  b.  lat.  voy.  Marcassite.
3855:Marquesita,  esp.  voy.  Marcassite.
3856:Marquezita ,  pg.  voy.  Marcassite.
5117:vîLu/  »^j*  pers.  Yoy.  Alchimie,  lu. -j~«  voy.  Astronomie,  lo. U-wàj>y«  voy.  Marcassite. xù-^-iiJ>j«  voy.  Marcassite. lh>,Aj>y«  voy.  Marcassite. <-.^5^  voy.  Markab. ^y9  voy.  Moringe. ^-«  voy.  Moringe. i^y»  voy.  Astronomie,  30. iôj) j«  voy.  Madrague. t_>*xx*«-«  voy.  Mosarabe. »Xss^vj»  voy.  Mosquée. ïy^r^  voy.  Mascarade. Je.'M-ji  voy.  Mistique. liL-j*  voy.  Musc. ^jiSi**^  voy.  Mesquin. ^.^•-L»*^  voy.  Musulman. jU*«w«  voy.  Mousselin. n*)TDD  voy.  Massore, Î12^12  voy.  Miscbna. J^tjrut  voy.  Alchimie,  hn. ^3Xu3»  voy.  Bangue. ïJsu»  voy,  Matras. ^Ja.*  voy.  Matelas. iCSJa.»  voy.  Matraca. »^yj£u9  voy.  Matamore, iojsjt»  voy.  Almadie. (jjnjjuo  voy.  Mézéréon. <_>yL«  voy.  Garbin. ïyjt^  voy.  Almagra. Ixx/»  tnal.  voy.  Mangue. o*«5^  ma/,  voy.  Mangoustan, Y  ^^M  mal.  voy.  Manglier. ^^^iCk«  mft/.  voy.  Mangoustan, ^*w.^JCx,«  ï/i«/.  voy.  Mangoustan. 4pjL«  voy.  Mufti. ^^UL»  voy.  Macabre, jj^.      -Uu»  voy.  (iiiïniacan.

Marcassite.  Pyrite  de  fer.  Esp.  marquesita ,  autrefois  mar- caxita,  portug.  marquezita,  ital.  marcassita,  bas  lat.  mar- chasita.  De  l'arabe  Ux^ïyo  marqachithâ ,  que  Boctbor  écrit Ikjuioyo  marqachUâ ,  en  persan,  AamjUmJ>w<>  marqachicha  (Ri- chardson).  La  première  orthographe  est  celle  de  Razi (man.  déjà  cité,  fol.  5o  recto)  et  celle  du  traité  d'alchimie de  Djabir  (Géber),  man.  n*"  1080  du  suppl.  arabe  de  la Bibl.  nat.  folio  6  recto  et  passim,  et  en  général  la  seule que  j'aie  rencontrée  dans  les  manuscrits.  Aussi  je  soupçonne fort  le  2fJi*.jj*t:iyA  marqachicha  ci -dessus  d'être  une  fausse lecture,  causée  par  la  facile  confusion  du  c2>  th  avecle  ^ji  ch.
Marfil  ou  Morfil.  Ivoire.  Esp.  marfil,  portug.  marfim. On  trouve  aussi  les  formes  olmafi,  almafil  (x*^  siècle).  Les Arabes  appellent  l'ivoire  Juà!!  <_;l3  nâh  al-fil,  dent  de  l'é- léphant, et  c'est  de  là  qu'on  a  voulu  tirer  ma rjil,  étymo- logie  acceptée  des  uns  (Diez,  Defrémery),  repoussée  par les  autres  (Engelmann,  Dozy^).  L'origine  reste  donc  in-
'  M.  Dozy  dit  que,  dans  l'expression  nab  al-fil,  le  génie  de  la  langue  ne permet  pas  de  supprimer  l'article  et  de  dire  nahfd;  cependant  Boctlior  tra-
158  DICTIONNAIRE  ÉTYMOLOGIQUE
certaine.  La  syllabe  finale  semble  bien  être  l'arabe  Jcô fil,  éléphant;  mais  peut-être  la  première  partie  est-elle un  mot  asiatique  ou  africain,  étran^i^er  a  l'arabe  et  ayant le  même  sens  que  nCih,  dent.
Il  y  a,  en  vieux  français,  un  terme  qui  n'esl  pas  sans offrir  quelque  analogie  avec  la  première  syllabe  de  mar- fd.  C'est  le  mot  mire ,  défense  de  sanglier  (d'où  sanglier miré,  sanglier  de  cinq  ans,  déjà  muni  de  ses  défenses), correspondant,  comme  sens,  à  l'italien  sanna,  zanna  (qui est  l'arabe  ^^  sinn,  dent).  L'origine  de  mire  est  inconnue.
Markab.  Etoile  a  de  la  constellation  de  Pégase.  De  l'a- rabe L^y>  markab,  monture.
Mascarade.  Esp.  et  portug.  mascara,  masque;  ital.  ma- schera,  même  sens.  Il  a  été  surabondamment  démontré  par divers  étymologistes ,  contrairement  à  l'opinion  de  Diez, et  notamment  par  MM.  Malin  et  Dozy,  que  mascara  et  ma- schera  ne  sont  rien  autre  que  l'arabe  »-ià*^^  maskhara  si- gnifiant bonjfon,  farceur,  histrwn ;  plaisanterie ,  drôlerie,  mo- querie. Je  crois  inutile  de  reproduire  les  arguments  exposés en  détail  dans  le  Glossaire  de  MM.  Engelmann  et  Dozy. (Voy.  p.  3o/i  et  suiv.)
Il  y  a  longtemps  que  Chardin  écrivait,  dans  son  Voyap-e en  Perse  :  crlls  (les  Persans)  appellent  ces  sortes  de  di- vertissements r^irtsrrtrc^  c'est-à-dire  jeu,  plaisanterie,  raille- rie ,  représentation ,  d'oii  est  venu  notre  mot  de  mascarade.  5j (Edit.  Smith,  p.  s/jq.)
Massore.   Travail    critique    fait  par   les    docteurs  juifs
duil  le  mot  dont  il  est  ici  question  par  J^  ^j-w  sinnfd,  expression  (oui  A fnit  pareille  à  la  forme  contestée.  Et,  en  outre,  il  existe  un  certain  nombre de  mots  composés,  tels  que  '^^^to  mn-onard,  y^^-;  henzeher  (loupe,  litlér. fila  du  jxnmrt) ,  elc.  où  rnrliclo  manque.  Il  n'y  a  doue,  aucune  impossibilili' à  ce  ((iron  ait  dit  nah-fil.
DES  MOTS  DORIGINE  ORIENTALE.  159
connus  sous  le  nom  de  massorètes,  pour  fixer  le  texte  de la  Bible.  De  l'hébreu  n'^^Dip  masôrah.  tradition,  lecture traditionnelle.
Mat.  Ternie  du  jeu  des  échecs.  (Voy.  Echec.) Mnt,  adjectif,  au  sens  de  terne,  vient  du  mat  des  échecs, r^ Dans  les  anciens  auteurs,  dit  M.  Littré,  mat  signifie las,  humilié;  c'est  de  ce  sens  c|u'on  est  allé  au  sens  de  terne, ([ui  paraît  très-récent,  v  L'espagnol  a  tnate,  couche  de  blanc avant  de  dorer,  qui  est  assurément  le  même  mot.  11  est remarquable  qu'en  hindoustani  le  terme  o>Lo  mât,  importé du  persan,  a  aussi  les  deux  sens  :  check-maie;  astonished, conj'oanded.  (Shakespear,  Dict.  Hindust.  and  Engl.^
Matamore.  Silo  pour  le  grain,  ce  Les  Maures  et  les  Arabes, dit  Raynal\  serrent  leurs  grains  dans  des  matamores  ou
magasins  souterrains   La  forme  des  matamores  ne
diffère  que  peu  de  celle  de  nos  puits.  5?  C'est  l'arabe 5jj^.Uxfl  maimôra,  fosse  souterraine,  silo.
De  ce  mot  vient  l'espagnol  mazmorra,  cachot,  fosse, prison.  On  peut  voir,  dans  la  Relation  du  sieur  Mouette"^, qui  fut  captif  au  Maroc  de  16-70  à  1681,  la  description de  la  mazmorra  où  on  le  renfermait  la  nuit  avec  les  autres esclaves  :  ^^  C'étaient  de  vrais  silos  creusés  sous  terre  .  .  . on  faisait  descendre  les  esclaves  dans  ce  trou  par  une échelle  de  corde.  ??
Matassins.  Esp.  matachin,  portug.  muchachim ,  ital.  mat- tacino.  M.  Dozy  dérive  ingénieusement  ces  mots  de  l'arabe xzi^^  ouadjh,  visage,  employé  dans  le  sens  de  masque,  d'où
un  verbe  ^^'  tawadjdjah,  se  masquer,  et  enfin  le  parti-
'   Hist.  philos,  des  Etats  harharesques ,  édit.  Peiichet,  t.  I",  p.  A7. *  Dans  le  Tour  du  monde,  t.  P',  p.  210.
160  DICTIONNAIRE  ÉTYMOLOGIQUE
cipe  i^yjo  moutawadjdjdi,  au  pluriel  ^^^^yu  moutawadj- djihîn,  personnes  masquées,  matassins^  (Voy.  G/oss.  p.  Boc), 3io.)
Matelas.  Esp.  et  portug.  almadraque ,  prov.  almatrac, ital.  matarazzo  y  maierasso,  bas  lat.  almatracum,  matera- cium,  mataricium,  almatricmm,  vieux  fr.  materas,  mathelas, mnUeral,  matelat.  De  l'arabe  ^-k^  matrah,  lit,  matelas,  dans Boctbor.  Ce  mot  vient  de  la  racine  •^■Ji^  tarah,  jeter,  qui  a donné  un  autre  mot  de  sens  analogue,  iCa^Lb  tarfdia, coussin.
Pour  comprendre  comment  le  lieu  où  l'on  jette,  ou bien  la  chose  jetée  [matrah,  motrah)  a  pu  s'entendre  d'un lit,  d'un  matelas,  il  suffit  de  se  rappeler  que  les  Orien- taux n'ont  ou  n'avaient  pas  de  lits  proprement  dits,  à  la façon  des  nôtres,  avec  un  châlit,  mais  qu'une  simple  cou- verture, un  matelas  jeté  à  terre  en  tenait  lieu.  On  peut comparer  les  expressions  latines  stratum,  stragulum,  ratta- chées à  sternere.
MatracX.  Roue  garnie  de  marteaux  de  bois.  (Besche- relle.)  Ce  mot  est  espagnol,  et  dans  cette  langue  il  dési- gne aussi  la  crécelle  de  bois  qui  remplace  les  cloches  à certains  jours  de  la  semaine  sainte.  C'est  l'arabe  iCï^k^  m/- traqa,  marteau,  instrument  pour  frapper,  de  la  racine  ^-b tarag ,  frapper.  On  connaît,  bien  que  les  dictionnaires français  ne  le  donnent  pas,  le  mot  matraque,  employé  en Algérie  dans  le  sens  de  bâton,  trique;  c'est  la  prononcia-
Marcassita,  ital.\o\.  Marcassite.
Marcassite.
Marcaxita,  esp.  voy.  Marcassite.
Marchasita,  b.  lat.  voy.  Marcassite.
Marched,  voy.  Alchimie,  19.
Marfil.
Marfim,pg'.  voy.  Marfil.
Margomar,  esp.  voy.  Récamer.
Markab.
Marquesita,  esp.  voy.  Marcassite.
Marquezita ,  pg.  voy.  Marcassite.
Martach,  voy.  Alchimie,  19.
Martath,  voy.  Alchimie,  19.
Masal,  voy.  Alchimie,  ^2.
Masase,  voy.  Bangue.
Mascara,  hisp.  voy.  Mascarade.
Mascarade.
Mascarè,  voy.  Mascarade.
Maschera,  ital.  voy.  Mascarade.
Masloc,  vov.  Bangue.
Maslocco,  ital.  voy.  Bangue.
Massac,  voy.  BanpjUe.
Massore.
Mat.
Matachin,  esp.  voy.  Matassins.
Matamore.
vîLu/  »^j*  pers.  Yoy.  Alchimie,  lu. -j~«  voy.  Astronomie,  lo. U-wàj>y«  voy.  Marcassite. xù-^-iiJ>j«  voy.  Marcassite. lh>,Aj>y«  voy.  Marcassite. <-.^5^  voy.  Markab. ^y9  voy.  Moringe. ^-«  voy.  Moringe. i^y»  voy.  Astronomie,  30. iôj) j«  voy.  Madrague. t_>*xx*«-«  voy.  Mosarabe. »Xss^vj»  voy.  Mosquée. ïy^r^  voy.  Mascarade. Je.'M-ji  voy.  Mistique. liL-j*  voy.  Musc. ^jiSi**^  voy.  Mesquin. ^.^•-L»*^  voy.  Musulman. jU*«w«  voy.  Mousselin. n*)TDD  voy.  Massore, Î12^12  voy.  Miscbna. J^tjrut  voy.  Alchimie,  hn. ^3Xu3»  voy.  Bangue. ïJsu»  voy,  Matras. ^Ja.*  voy.  Matelas. iCSJa.»  voy.  Matraca. »^yj£u9  voy.  Matamore, iojsjt»  voy.  Almadie. (jjnjjuo  voy.  Mézéréon. <_>yL«  voy.  Garbin. ïyjt^  voy.  Almagra. Ixx/»  tnal.  voy.  Mangue. o*«5^  ma/,  voy.  Mangoustan, Y  ^^M  mal.  voy.  Manglier. ^^^iCk«  mft/.  voy.  Mangoustan, ^*w.^JCx,«  ï/i«/.  voy.  Mangoustan. 4pjL«  voy.  Mufti. ^^UL»  voy.  Macabre, jj^.      -Uu»  voy.  (iiiïniacan.
cy!  JaJLjL*  voy.  Almicantarat. (;5^lX«  voy.  Moucre, d2A-«  wîrt/.  voy.  Emblic. 2^  voy.  Alchimie,  /io. •^^D  voy.  Melchite,  Moloch L^;i.3X•  voy.  Mélochie, iÇj:k.^L»  voy.  Mélochie. <jl5^  voy.  Mélochie, y^Jm  mal.  voy.  Bambou, Uj«  voy,  Almène. »jU-«  voy.  Minaret. ^j^ULl«  turc,  voy.  Mangal. (S'^^pt  voy.  Moise. oo^  pers.  voy.  Mobed, y 3^  voy.  Muezzin, (^^yt  voy.  Astronomie,  36. •■^y9,  ï^yi  voy.  Musacées. j««^  voy.  Mousson. Juks^  voy.  Mousseline, ù^iyi  voy.  Mulâtre. J^  voy.  Mollah. -^  voy.  Momie, ^j:JL«p»  voy,  Miramolin, Ly«^  voy.  Momie. A^^  voy.  Momie, (^rl^  voy,  Mahari. y^  voy,  Mahari, OsJLg^  voy,  Ohnde. U~y9  pers.  voy,  Mirza. Jwu«  j^er.s,  voy.  Mils. ^Jy^  voy.  Mai  mon,
»m/,  voy.  Mainate.
J.^1  t^Lj  voy.  Marfil. .x^U  voy.  Astronomie,  i  o, ^lj  voy.  ]Minarct. S-iP)^  voy,  Nargliileh, JK^U  vo).  Noria.
I
Ii\DE\  DES  MOTS  ORIENTAUX.
277
AàU  pers.  voy.  Naffe. NyiLj  voy.  Nacairo. cjoU  voy.  Nabab. L^  voy.  Nabalhéeti. *JLJ>  voy.  Nabca. j-Ls?  voy.  Alchimie,  66. frUç  voy.  Nuque. ^yàr^j  voy.  Neskhi. ^jj— «J  voy.  Nizeré. rj.LùJ  voy,  Alcbimie,  yo. (jUu  per.f.  voy.  Nichan. ^^jLj  voy.  Natron. -Uàj  voy.  Nizam. wJaj  voy.  Nadir. >jl3  voy.  Noria.
```


### [2026-09-07T15:52:42.565Z] TOOL RESULT

```
mirc, n. a mark (weight or coin). [Obs.]
mär- çän’dð, a. [It., ppr. of marcare, to mark.] same as marcato.
mir’can-tant, n. a merchant. (Obs.}
mar’ca-site, n. [Fr. marcassite, prob. of Ar. origin.}
1. formerly, crystallized iron pyrites, used in the eighteenth century for ornaments.
2. a piece of this, especially as an ornament,
3. iron disulfide, FeS:, a mineral resembling iron pyrites. $ 3
mir-ca-sit/ic, mär-çå-sit'ic-ăl, a. pertaining to marcasite; of the nature of marcasite.
mir-cas/sin, n. [Fr.] in armorial bearings, a young wild boar.
mär-cä’tõ, a. [It., pp. of marcare, to mark.] in music, emphatic; accented.
mär-cel’, n. [after M. Marcel, 19th-c. Fr. hair- dresser.] a series of even waves or tiers put in the hair: also marcel wave.
=== DOZ ===
```


## [2026-09-07T15:53:05.226Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; python3 - <<'EOF'\nt=open('BQT_v4_pages.txt',encoding='utf8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor i,p in enumerate(pages):\n    if 'مرقشیشا' in p or 'مارقشیشا' in p or 'مرقعیعا' in p:\n        print('=== leaf(0-based)',i,'pdfpage?',i+1,'printed ~',i+1+1917)\n        print(p[:2500])\n        print('-----')\nEOF",
 "description": "Find marqashisha in Borhan vol 4"
}
```


### [2026-09-07T15:53:06.527Z] TOOL RESULT

```
leaves 553
=== leaf(0-based) 20 pdfpage? 21 printed ~ 1938
[pdf page 21]
مار شحاکی -۱۹۳۸-
هفت بند است که استادان تابی فوازند . وآنرا از قفای سراو برمیآورند » وآن سبزرنگه
مارضحاکی «کنایه از زنجیر است | است و خاکستری رنه هم میشود - و پازه‌ر را
که بر پای مجرمان نهند . اور ی
مارقش - با فا بروزن بارکش, کنایه رل < با نون و دال ایجد بر
ازشحاه ماران است ۹ . : وژن غارتگر , مخفف مادراندر است که زن پدر
مارقشیشا ؟ - بنتم قاف وشن به ها ۱
تحتانی رسیده و شین دبگر بالف کشیده » بمعنی ر 8 < یکس تالت و فتح نون » بام
مرقعیعا است و آن جوهریست که در دوا ای گیاهی است که‌آلرا بعربیلحیةالتیی 8 خوانند.
چشم بکار برند وآن اقسام می‌باشد : ذهبی وفضی مار فه سر - یکی تاك و خم نون .
و نحاسی و حدیدی و شبهی . بهترین‌آن ذهبی | کنایه از نه فلك است. .
است. گوبند چونآترا بشکنند درون‌آن زرافعان مارو « بروزن جارو (۱) » بمعنی مادر
داشد - است که والده باشد؟ - وبزبان هندی‌ناممقامیت
مار کیا ؟ - بسسنی مارگیاء ات که | از موسیقی .
مارچوبه باشد و بس‌بی علیون است .8 مادون ۷ - بر وزن قارون » ستگی
مادمصری - بکر ثاك ,کنایه از است که آنرا با سرمه در چش م کشند. سقیدیرا
نیزه و سنان مصری باشد . ببرد - و نام دوائی هم هست که آترا مروخوش
مادمهره - مهرء‌است که بامارمیباشد | کوبند . بغار آن دود سر را نافع است.
() چك . چش : خارو -
۹ - دکرکفت شحاك شاه جهان شنیدست گفتارت اندر بهان .
مرا مارفتش‌خواندی و بدسرشت مرا نام بردی بگفتار زشت .
آمدی طوسی « فرهنگه نظام > .
۴ <مرقتیها . فرادویان مرقشیدا را ازعربی گرفته ۸12702898116 نامیدند. وعرب
ازآرامیان این کلمه را اخذ کرده‌اند . درآرامی «مرقعینا» يا «کیفا مقشیثا > بمعنی سنگی سخت
است . عرب « کیفا > را حذف و راء بین میم وقاق را بعوض محذوف آوردند برای خفت تلفظ:
و ایرانیان آلرا بسورمرقشیشا ومارقشیشا نقل کرده‌اند « نخب‌الذخائر ص ۱۵ ح 2 > . در سربافی
این کلمه با 00 , یجای ۳0 آمده ‏ اما ریشةآن مشخص نیت « دزی ج ۲ اس ۳۵۸4
۴ - مصحف « مارگیا > مخفف « مارگیاه > (ه.م.) است .
۴ - مار بمعتی مادر آمده ( رك : مار » واقی : مازیره ) و رك : مادندر .
8 -ر4 : لحیقالتیی در تحفه حکیم موّمن . ‎٩‏ - ر3ك : مار ؛ ماور -
۷ - از پونانی 3/1870 (< ۸12۳070 ) « دزی ج اس ۵۹۶ :۲
ورك : این‌پیطار ( ج ۸ ص ۱۲۹ 1
مار یاه - [ لغة نبات ( غبیه به ) مار ] ۰ اسم فارسی نبانی است قربب بدوذرع »
برکش شبیه ببرکه بید ‏ وکلش زرد وقیةٌ او شبیه بسر مار ومنبتش حریم جبال آنربایجان ...
وظن‌حقی رآنست که او اخبون باشد . « تحفةٌ حکیم موّمن » رك : اخبون .
( برهان قاطع ۲۴۵ )

-----
=== leaf(0-based) 77 pdfpage? 78 printed ~ 1995
[pdf page 78]
-۱۹۹۰- م رکه
مرغول است که پیج و تاب - و زلف وکا کل‌تاب | حجرالنور خوانند -
خورده - و شمه پیچان وغلطان - وعیش. وتشاط مرقع ‎٩‏ دار ابلیمی ۲ - یعنی
باشد - و بمعنی طره - و دستار - و موی‌پیشانی | طابقة شیطانی - وخليفة ابلیی -وکنایه ازاعمال
هم‌آمده است . تاغایت کردن باشد در لبلی تقوی و توف -
مرغ بافوت پر - کنایه از آتش | و بطریق خطاب هم‌آمدء ۸ پمنی‌اینها: توبی وتو
است که بعربی نار خواتند . میکنی ؛ و باین معنی بلفظ مرقع دار امانی هم
هرق - با قاف بروزن سرمد ۱ ۰ نام بنظرآمده است .
دارویی‌است کهآبرا بهندی داتوره کوبند وبتاتوله مرقون * - بروزن مجنون. دام یکی
شهرت دارد ۴ - و افیون و ترباك رانیز بدین | از اسحاب مجوی است و او اصل رااسه میداند:
نام خوانند ۴ - و در عربی جایی را کویند که | نور‌وطلمت, ومعدل‌جامع که سبب‌امتزاج‌واختلال
میت را در آن دفن مازند ۴ . است .
مرقشیشا * - بسنی مارقعیعا است هرگ - بنم اول وسکون ثالی و کاف
وآن جوهری باش د که دردازوهای چشم پکارپرند» | فارسی » آب بینی راگوبند که سطبر وغلیظشده
وآن اقام میباشد: ذهبی‌وفشی ونحاسی وحدیدی | باشد *۱- و بفتح اول معروف اسْت که هردن
وشبهی ۰ وبخترین‌آن ذهبی است » وآنرا بمریی | باشد ۱۱ :

۱ - بدو معتی اول (عر) چم اول وکسر سوم « دزی اج اص ۵2۷

۲ - در تداول مغرب داتوره ۳ 421۳0 ( فر ) راگوبند « دزی ج۱ ص ۵4۷ ۰

۴ - مرقده‌افیون ۳ 0۳1۷773 ( فر ) «دزی ج۱ ص۵2۷ . «افیون, دواء مشهورالعین +
معلوم بهذاالاسم . وقدتمیه بض عامة البلاد المرقد » وخولین الخشخاش آلاسود بند جفافه ویشبه
بالربوب » « عقار ۳۵ ». لوف کوید : المرقد ( بفتح میم و قاف ) بجای المرقد ( چم میم وکسر
قاف بمعنی خواب آور » منوم ) ۳ 0011772 « عقار وف >. ۴ - (ص) «خوایگاه و کور»
« منتهی‌الارب > . «مارقشیها (ه.م.) و رك : دزی ج اص ۹۸4 ۰ نخبه۱و۱۸۸ ۰

- خرقةٌ صوفیان که رقعه رقمه برهم دوخته باشند و اسم مفعول جعلی است «گنجينة
کنجوی‌س ۰۹۱۸۳ ۷ - از ابلیی ( عیطان )ی ( نبت ) .

۸ - درین صورت « ی > آخرشمین دوم شخص مفرد ( مخاطب ) است .

518006 ‏مسحف و مغفف مرقیون ۸18۳0107 فیلوف گنوسی 4 متولد در‎ - ٩
‏در اوایل قرن دوم میلادی . وی فرزندکشیش‌سینوپ بود و تحت نظرروحانیان:مسیحی قرییت‌شد.‎
‏ولی بعد اورا طرد وتبعیدکردند . ولوبه « رم > پناه برد وسپی مجدداً بکلیسا با زکشت وباردیگر‎
‏نفی‌پلد شد. وی هم خود را مصروف تعلیم عفاید كنوستيك کرد » و افکار او را چندتن ازشاکردان‎
‏معتقد ومصمم آودر امپرانوری روم نا ابران » انتشار دادند . مرقوتیه بسه اصل قائّل بودند: خدای‎
‏نيك ,1 فرید کار ( روحی که هرچند عادل وقادر بود » درمرتبه‌ای اسقل از خدا قرار دارد )+وهاده‎
‏(که در اصل بد است ) . جهان مخلوطی است از نيك وبد . ر4 : دائرةالمعارف بریتالیا ۰ لاروی‎
. ‏بز رکه » الفهرست ابن‌الندیم چاپ مص 2۷۶ . * رك : جهانگیری‎

۱- پهلوی ۰13878 اوستا: 132810۳68 « بارتولمه ۱۱۸۹ > « نیب رکه صس۵ ۱۶ >.قس:
آرمنی ([13
-----
```


## [2026-09-07T15:53:49.336Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT maghava ===\"; grep -n \"ma\\(γ\\|y\\|g\\)ava\\|maγav\\|mayava\" BRT.txt | head -10; echo \"=== BRT hamaz ===\"; grep -n \"hamaz\\|ha-maz\\|hamazan\" BRT.txt | head -10; echo \"=== KNT ===\"; grep -n -i \"hamaz\\|magu\" KNT.txt | head -10; echo \"=== HUB/HRN magh ===\"; grep -n -i \"maγava\\|mayava\\|magad\" HUB.txt HRN.txt | head",
 "description": "Grep Bartholomae/Kent for Avestan forms"
}
```


### [2026-09-07T15:53:49.423Z] TOOL RESULT

```
=== BRT maghava ===
8937:mit  para  i)  dnwS.  2:  hyat  mJzdtm zara'äiustrS  magavabyS  (sd.)  hiU  para  Y. 3/.  15.  2)    in   der   exegetischen   Litt.
10219:{sd.)..'rd  thmSmY.$0.^\  —  Ayal  mlzihm zard^usirO  magavadj/U {sA-)  Üsisl  para  "rd d»mSnS  ahurS  masds  jasat  (sd.)  Y,  5/. 15.  b>  im  jAw.  (immer  in  der  Folge ^  nm°):  xsnäts  asaonqtn  urvanö  p3rayeiiiti . .  avi  'rS  nmäiDin  mal^amm  ahurake. mazdS  ..  amgsanam  spfntanqm  ..  anyalsam asaonam  V.ip.32; — 'rS  nmäitpm  ahurahe mazdä  yazamaide  Vr.  7.  i;  —  °rJ  nmämm asti  "nfrfyö  asävaoyd  Ytj.  4^4;  —  *°rB iimUne  ahurahe  hvSyaomm  Yt.^j,  3;  — zaoirä  .  .  ni  hJs  dasva  *'rS  nmäne  Yt, 10.^2;  —  urvätam  , ,  m»rtkw3fä3m  kuma- taglu  .  .  häxtagsu  ,  .  hvarstaiht  .  .  *°r5 nmansm  Ylij.  84;  —  ahurahe  mazdS.  g" fumän^i  yat  srlr?m  VyLJ'^^;  —  °r!f  sp3n- tahe  n>mäne  Vyt  28.  a)  sonst  mit raoxma-  Adj.:  raoxliam  "rS  ntnSrum  S. 2.30;  —  haca  raoxiha  *°rB  ttmäna  .  . .rr/ata  haca  duianha  Yt. /().  44;  —  mt- "ir^m  ..yim  yasata  ahurB  mazdä  raexsnät paiii  *'r5  nmänät  Yt  iQ.  IJ3;  *I33;  — raoxmahe  *°r5  nmänahe  S./.30,  Yt.72.37,
10855:•  j.,  g.  xSi-  f  'Not,  Elend':  x^3  (GS.)''> dangSm  ayU  (sd.)  Umanhö  Y.31.20;  — paiiistaße  xsayasca  (GS.)''  amayavay&sla Y.7/.  17;  —  xUm^'>  F.J.
11741:Korrelat;  a)  substantivisch;  a)  im  gAw.: yaitat  (Sp.öi^m.)  mtzdim  ..  ndil  däifl,  kä tim  (ASm.)  ahyn  *mainis{sd.}  at^fiat  Y.44. 19;  —  ySngstü  masds  .  .  minal  (sd.)  , ., fing  zbaya(s6..)'^.46.  14;  — yqsca  haxsai (sd.)  .  .,  frö  iail  vlspais.  .  \'.46. 10;  — ya^qm  ndi^  hvarltStS  vqs  duzvari'tä,  lOi daft'fng (sA.)  dqn  \.4g.^;  —  Ayat  vä  IBi näntanqm  vazUttm  . ,,  tä  (IS.)  &wä  pairi- jasämaidl  Y.^.y,  —  y3  vS  ..  mazdä *>tämqm  dadät,  täis  vif  yazamaidl,  iai/^.. Y.JA4;  —  ptTMä  . ,  yä  iiudö  dadpntl .., ya^ia  tä  (NSf)  anfun  Y,_J/.  14;  —  yäsca tsi  g3na  ..,  ta  yazamaidi'H.38. 1;  —  hyai Urvätern  . .,  tat  ns  .  .  vüo^  Y.  j/.  3;  — : yä  frasS  (sd.)  ävJsyä  yä  vä  .  .  *p)r3saHl tayä  .  .,  ta  (APn.)  . .  aÜT  vamahi  Y. J/.13;  7  i..St,46.^;—y(i/ravaxIyä,ym tä  .,  Aai^tyi  Y.44. 6;  33-J3i  —  mit Numerus  wechseP*:  Ayat  mt:d)m  zardhustrS magavabyS  (sd.)  cöist  parä  .  .,  tä  (APn.) j'J  .  .  saväis  *avT!l  (sd.)  Y.5J.  15;  — yehyä  .  -  vaAistfm  .  .  vaida  masdä  .  ,,  tq yaaäi  Y.5/,  22;  —  at  yS  aktm  drigväitl . . var.'faiil  vaftkäu  vä  cSiäiaitl  (sd.)  astlm, töi  (NPm.)  värai  (sd.)  rädmtl  .  .  Y. j^.  2.  b)  im  jAw.:  yim  (näml.  a/rumf) vaiänte  aAurStsAS  .  .,  t»m  vafata  .  .  Vt. '4-  39t  —  yaUa  .  .  aiti  mazyS  . ,,  tat  no däyata  Y,  65. 14;  —  y^  -  ■  nigänhinti *msAii,aiti  (sd.),  nsit  tarn  . .  Y. /o.  15;  — yqm  alava  aiayqm  va^a,  tarn  drvä 7VT6va  Vt.  22,  2 ;  —  yeAhl  kätqnt . .  vanAS .  .  ahurS  val%S  .  .  yänAanUä,  tqscä täscll  yazamaidlY.2-j.\^\ — yh  nS  fanti gä'iä    hari^ravaitisca  .  .,  tä  m  Amti
20310:•  j.  mäyav-  Adj.  '(in  besonderer  Weise und  Richtung)  geschickt,  gewandt;  findig*: nairyB.sanhasca  yS  'yus  Yt  10,  52.  VgL mayava-.
20768:jAiw.;  das  Relativ  ist  a)  substantivisch: yOi  däityayaona  ''car^nta  ..noil  aitaEsqm.. N.52;—  s.  noch  N.55(Sp.  1205  0. j; — mit  Gen.  part:  yatca  aSaliqm  ra%wqm faoiryö  paiti  ä./asät  hävanänim  (sd.)  a^m astayeiti  N.  ^2;  —  die  Beziehung  ist  un- genau: yä(AFn.)  *malz5  vä  ..  *srävayeiti aUaiiqm  (Sp.  1 4  u.)  vacqm . .  N.  J7.  ß)  ad- jektivisch :  yä  (NDm.)  nara  iämSjfarn^a . . hamqm  aSe  *x^äudrim  (sd.)  saoisram  ba- rälB'lü.64.  e)  ta-  (Sp.617  m.);'A)  im gA^.;  das  Relativ  ist  et)  substantivisch: yastap''  mxidsm  . .  nsit  däill  ia  iim . .  Y. 44. 19;  — yBi  aisirMtn  varadm  ..yaisqtn nSit  Avarstäis  vas  duivar/ia  tst . .  Y.  4g. 4; —  ffyi  urvafymisd.)  cazdsnnhvadi^s tainS-.vaocH  Y.J/.3; — ^^(NPn.)  vS  abi- frä  ta  xsairakya  'Y.33. 13;  — yn  (APn.)W( asä  ya  asäi  g7ul  tasä  (sd.)  mraot ..  tä  . . Y.  46.  g;  31.7,  44.6; — yqscä  haxSai  . . fi-5  mis  vJspäis..  Y.46. 10;  —  yfngs/S"'^ ..  hadimöi  mina/fsd.)  ..  ßng  zbayä  Y. 46.14;  —  mit  Gen.  part:  hyat  vä  tsi nämanqm  väzut>tn  .  .  tä  'hwa  pairijasä- maidl  Y.36.3;  —  die  Beziehung  ist  un- genau: ylf  akftn  dr>gväiti . .  zastSibyä  (sd.) va  varisaitl  vanhäu  va  cöihait!{sd.)  asftm tdi  varäi(sd.)  rädtnilY.ss.z*'^; — yehya . ,  vahist3in  valda  (sd.)  mazda  . .  tq  yatäi Y.  5/,  2a*>;  —  hyaX"'>  miidsm  ..  magavabyö (sd.)  Mit  para  ta  vf..saväi/*c>vTii(,s±) Y. 5/.  15;  —  yam"^  da  .. ränSibya  xSnüt^ni /i>'o/(Sp. I20I  m.)  urvatim  ..tat  n} .,  vaocä Y.^J.3;  vgL57.9  (Sp.  1216  m.);  —  ya (zu  ß)  frasä  (sd.)  avl^ya  yä  (zu  ß)  . .  *p)r?- salte..y}  vä  ..  ayaniaite*baßm  /J(APn.) . .  valnahi  Y.31. 13  "''.  3)  adjektivisch: yäsc'ä  tat  g?nä  . .  vairya  tä  yazamaide  Y. 38.  r ;  —  yä  vS  .  .  *namqm  dadät . .  täis va yasamaidlY. 38.  i,\—  yä  ihids  dadtnts da%ranqm  (sd.)  hacä  ai'äunS  yäs{za.  it)a . .  dngvSJjbyö  ya%a   tä  a»Am  Y.j/.  14;
22701:•  j.  *vaya'vant-  Adj.  (fem.  *vai/T-)  'mit Vögeln  versehen,  bevölkert':  iä^a  asäum apa.jas3  sitibyasca  haca  gaomaiOhyaica *'vaitibyasca*^  Itaca  mayavaitibyas^a  (sd.) H.2. 16.
27788:•  j.,  g.  zaraO'uätra-  m.  EN.  des  Stifters der  mosi/ischen  Religion,  aus  der  Spitatna- (sd.)familie,  Sohns  des  Poumfaspa  und der  iJwySii.wa*);  a)  im  gAw.:  aim  möi idä  visiJ  (Sp.  1315  u.)  yf  n}  afvS  säsnä (sd.)  gäiatä  'rS  spitämö  hvS  ta  . .  vaHl . . iankirg^ra  {sA.)  iravayetihl  Y.2t>.  8;  — yS  mq%rä  (sd.)  *vaam  .  .  baraitT  urva%ö as'd  tumar?hs  'r3  Y.J0.6;  —  a^  ahurS hv5  mainyäm  'rS  V3rmtlmazda  yasß  Hlca spSnisiS  Y. 4?- 16;  —  at  höi  aoji{zA.)  'rS paourvim  ^hai^ys.dvaisa  .  .  Y.  4j,  8;  — at  ratqm  (sd.)  °r5  lanvascl£  ifaAyä  ustartsm dadäitl  paurvatatjm  (sd.)  ^.33.  14;  — hyal    mlidim    °rS    magavabyB  (sd.)    iBist
=== BRT hamaz ===
=== KNT ===
815:атта DB 4.92, as read by KT; perhaps hamazmaiā (JAOS 62.269).
2000:To these names may be added those of three large districts which were not governmental prov- inces: Karmdna, Varkdna, Margus with ethnic Márgava; ethnic Pätišwariš, to an unknown place-name; Нататат&уа, patronymic family- name to Hazémani§; Magus, denoting а member of the priestly clan of Media.
2156:Nom. Sg. Masc.: magus, piruš, sikabrus, ад). ш@татйун$; names of kings, Dérayava'us, Kürus; place-names, Abirddus, Kud"ru&, Qata- gus, Babiru’, Māļruļš, Margus, Hindu.
2157:Асе. Sg. Masc.: magum, zrafum, gidum; Dära- yava’um; Babirum, Margum; visadahyum; per- haps [agurum].
2663:D. As double object, one of the person and the other of the thing: DB 1.44f айа xšaçam tya Gaumdta hya magus айта Kabügiyam ‘this king- ship which Gaumata the Magian took away from Cambyses’ or ‘of which Gaumata deprived Cam- byses’; so also 1.46f, 59, 65f, and its passive in 1.49f hya атат Gaumàlam Шат magum тёасат ditam салтта ‘who might make that Gaumata the Me- dian deprived of the kingship’, DB 4.65 лау Skaurim (= skaubim) пай tunwatam züra akuna- vam ‘neither to the weak nor to the powerful did І do wrong’. DPd 20-2 айа adam yànam jadiya-
2666:E. As appositive to another accusative: DB 1.49f Gaumdtam tyam magum; DPd 21 haw Da- rayavaum xSdyatiyam adadà ‘he created King Darius’.
2798:II. From the originally relative type Gaumdia hya magus (DB 1.44, ete.) without the copula, there came the accusative type Gaumdtam tyam magum (DB 1.49f, etc.), where the articular use is assured.
3488:36 sdva : І martiya : magus : dha : Gaumáta : пата : hauv : udapatatà : hacd : Рай 37 yduvadaya : Arakadri$ : n&ma : Каша : hacd : avadaSa : Viyaxnahya : mah
3492:44 : Darayavaus : xSayafiya : айа : xSacam : tya : Gaumáta : һуа : magus : adin
3494:46 ha : pasiva : Gaumata : һуа : magus : adinà : Kabüjiyam : uta : Pirsam : шй
=== HUB/HRN magh ===
```


## [2026-09-07T15:54:06.270Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"unverheirat\" BRT.txt | head; echo \"=== maga entries ===\"; grep -n \"^• *[jg]\\.,\\? *ma[yγ]a\" BRT.txt | head -20",
 "description": "Grep Bartholomae for unverheiratet and maga"
}
```


### [2026-09-07T15:54:06.338Z] TOOL RESULT

```
19537:•  j.  Taa.ja.wa.-  Adj.  'unverheiratef:  näiri- vaite  . .  ahntäl  pourum  framraomi  .  .ya%a 'vs  fraväxsöit  "dem  beweibten  spreche  ich den  Vorrang  zu  vor  dem,  dass  einer  unver- heiratet altem  sollte"  V,  4. 47.
=== maga entries ===
19925:•  j.  mayah-  n.  "Begattung,  Beischlaf: vaitumnfm  yä  fravSit  (Sp.  932  m.)  Yt, 79.80;  —  stryö  °yä  faryiufi^(_sd.)  upaväzB A.,;.4;  F.i/.
```


## [2026-09-07T15:54:18.988Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '19500,19560p' BRT.txt; echo \"=== leaf/col ===\"; python3 -c \"\nt=open('BRT.txt',encoding='utf8',errors='replace').read().split(chr(10))\nprint('leaf',chr(10).join(t[:19537]).count(chr(12)))\"",
 "description": "Read Bartholomae context around unverheiratet"
}
```


### [2026-09-07T15:54:20.352Z] TOOL RESULT

```
(nach   DsT.)    maisma   iamait;   aber   BLOcaST
Lei.  156  hat  iitmqit.  —  »)  Das  wäre  etwa  ir.
'ufail-samaJi'.
j.  'tnaez-  V.  'harnen'.   Fraes.  3  maeza-.
'harnen,  Hain  lassen',  von  Menschen und  Tieren;  yat  is  faiti  fralsttm  maf- isnli  pasvasca  staoräca  V.J.  6;  —  -ia«- hqm  na  gäisanqm  .  .  aratujriit  ya *maizS*^  vä  *frä  va  saimns{sA.)  srSva- yeiti  N.J7.  a)  mit  Inhaltsakk.:  par(^t dvaHbya  yOi  aahtn  i^altvada&asca  a^ai- tvadai^Ts^a  aae  malsma  malsayanta  (Opt) yaiibyS  .  .  Jroinyante  V.  8. 1 3.
mxfrä  'nach  vorne  pissen  vor  — ,  hinans- pissen  über-' (Akk.)  ;^ai  nä  faurva  Jrabda (sd.)  frahdöJräjO  framauaiii  V.  18.  40.
ai.  mlkaii,  np,  metaä.  —  Pü.:  mitiOH  (GltPh. /.  301,  Sp.  VendPü.  so«,  3..1etzte(  Wort)  — ■)  Hds.  yoftff,  aber  Pti.:  mnä». g.  »maez-  V.  'hegen'.  Praes.  3  mua-. 'hegen,  sorglich  pflegen  (das  Rind)': yais  gqm  karapa  usixJ(sd.)eS  ai&mai  data
dby  Google
:io9
"^maezant-
, .  nSit  htm  mltSn  a/5  västrwt  frädaiähi "wie  sie  . .  das  Rind  der  Raserei  preis- geben, statt  dass  sie  es  hegeo*',  um  durch Asa    die   Landwirtschaft  zu   fördern"   Y.
Aus  »x.'smaif-;  %.  tahd.  smiUkm  'schöntun'.
—  Pü.:  paia  ntiid,  Sa.  i  frasädcfu.  —  0  Wört- lichi  "nicht  faber)  hegen  sie  es,   um  .  .",  —
—  1)  JusTls  Obeisetiung  PrJ.<Kf.247  verstehe ich  nicht
•  j.  *maezant-  Adj.,  PPA.:  s.  '/waa-  (mit No.  i).
•  j.  maeäa-  m.;  mae^-  f.  'Schaf;  Schaf- mutter': 'iahe  kihrpa  aurunahe  Yt.i4.z3; —  'hhe  . .  yat  varsnSi!  tatsMarahe  (sd.) "eiaesSchafbocks.."YU7.56; — hazanntn 'ianain  N.  ^2;  —  °/(  vihrkavaiti  (sd.)  V. ig.  33;  —  °iinqm  damunqm  '(Schafmutter') paiti.puiiranqm  A.J.  7.
KompE.;   Ableit.    —    ai.  mtfä-  m.,    m^f/.  f.; mp.  (Pü.),  np.  »ifL
•  j.  maeäina- Adj.  "vom  Schaf  herrührend, daiiir  bestimmt,  ovillus':  'Hmm  yavaah?nt Aog.  82;
ÄbleiL  aus  nia^io:  —  Pü. :  meiii,  mätak  i  mii
•  j.  maoSanö.kara-  Adj.  (fem.  °kairl-) 'Lust,  Wollust  bereitend':  jahikayii  .  . •kairyäi  Y,p.3a,
Vgl.  ahiinuita:  —  ai.  moiiana-  n.;  vgt,  moda- m.  'Lust'.    —   Pü.!    mülai   (Stt.:   mandatvam) tartär,  erl.:  Hc  iapäh  kuncl;  vgl.  unlermräfa-. j.  BiaairJ':  s.  maurvay:
•  p.  maka-  Adj.,  bezeichnet  ein  Volk, Ol  Mä<ä»'>;  Sing,  in  koUekt  Sinn:  ima dahyäva'^  tyH  manä  patiyaiia"  .  .  hatagvi harJ'uvatii  'ia"  Bh.  1.6;  D,  J.  2.
')  Am  Golf  von  Omäa,  an  dessen  Nordküste Makrän  gelegen  isl;  vgL  JusTi  GIrPh,  2,  434.
•  g.  maga-  m.  'Bund,  Geheimbund' '',  spez, von  der  mra^wZ/Hschen  Religionsgemein- schaft: aila  v3  mlzdim  (sd.)  anAal  aAya 'gahyä  Y.55, 7;  —  (wrayaäJ  (sd.)  'gitn tJm  y.53-T,  —  tarn  kavä  vT/dJs/S  'gahyä xsa^rä  nasal  •■yqm  ästJm  (sd.) . .  ". .  zu- gleich mit  der  Obherrschaft  über  den Bund.,"  Y.  51,  i6;  —  is  vä  vatahSus manaaks  aastä  'gäi  ^r^ivlf  (sd.)  Y.  57. 11; —  bes.  mit  mat-:  aj  mä  masa  ySzSm matdä  fräxsnTtß  rnaesi  'gäi  S  faHl.tänaiä (sd.)  Y.  2p.  1 1 ;  —  zara'hustra  kastS  asavä
Inaj«-  II 10
urva%B  mazsi  'gäi  "o  Z.,  welcher  Gläubige ist  dein  Freund  für  den  grossen  Bund?" Y.  46. 14.  \Y.4S.10:  lies  maäaiya.'] AbleiL  —VgL  ima-fa-,  —  Et?»).  —  Pü.: majTAf  erl.:  apecaklh,  apicak  vihih;  SQ.:  Ulla- mateam,  maAattvam  (er),  nirmalani  ullamalvarn) nsw. ;  Npü. :  jcäliä.  —  >)  So  nach  Gdn.  KZ. 38,  joo;  *.  auch  JU5TI  PrJ.  SS.  Das  Wort ist  ein  Term.  lechn.,  dessen  eigentliche  Be- deutung nicht  zu  ennicteln.  —  9)  Schwerlieh mit  ai.  magAd-  n.  identisch.
•  j.  'maj^-  m.,  mayä-  f.'>  'Loch  im  Erd- boden, Grube':  srvabya  (sd.)  'f»m  ava.- kanöis'V.iy.T,  5,  F.i7; —  baTvari  'yanqin (GPf)  irimaitinqm  aiühh  z?mö  aipt.kan- yät  V.  14. 6.  a)  insbes.  von  den  zu Zwecken  ritueller  Reinigung  gegrabenen Lochern":  mazdayasna  aiäAa  z?md  %rii (sd.)  'yjm  ava.kanay>n  dva  'fa  frasnä^aym malsmana  giul  *Bim  äp3  "die  Mazday. sollen  in  der  Erde  drei  Löcher  graben, zwei  Löcher  —  da  sollen  sie  mit  Rindsurin waschen  — ,  eins  —  mit  Wasser  — "  V.  76'.  1 2 ; Ä37; — paoirtm  upa  'fim  nt^w^>söis . . iitim  Ufa  . .  xltUm  upa  . .  "hrayS  anya  'ya ni^TVinssis  "ein  erstes  Loch  sollst  du  aus- stechen, ein  zweites  . .  ein  sechstes  . .  drei weitre  Löcher  sollst  du  ausstechen"  V. p.  6  ff.;  70. 18;  —  ^rJyS  yim  antari  vlta (sd.)  atitan  %räyS  {xh/as,  novo)  'ya  fra^ iärayBisY.g.  ii>;  11',  12,31; — arttanca (sd.)  .  .  'ya  (NP.)  V.p.  11;  —  karsascit frakäraySiS . .  ^ai  hala  'yaHbya  V.p.io; 29;  — paoirJfn  upa  *yim  frä.nasui  nanm (statt  NS.)  bavaiii  "am  ersten  Loch  . ." V.p.  28;  3iJ;  —  US  tansm  snayaSa  us vasirät  (statt  AP.)  gius  maSsmana  qpäca nava  (sd.)  upa  °ypm  "er  soll  seinen  Leib und  seine  Kleider  bei  den  neun  Löchern , .  waschen"  V.5.  54.
*>  Es  sind  deren  drei,  bei  der  'Reinigung  der neun  Nächte'  (iarasiiüni  i  nuA  Saia)  -  V.  p  — aber  neun.  DieZahlen  entsprechen  den  Öffnungen des  menschlichen  Leibes  (vgl.  ai.  srolai-),  bz. den  drei  hauptsäckiichsCen  (Mund,  After  und Gesclileclitsteii).     VgL  'maia-.
Abieil.  —  np.  mal  'Tiefe',  vgl.  ma-ßk  'Grube'.
—  mp.  mal.  —  i)  Nur  V.  14.  6.
•  j.  'ma]^-  n.  Name  des  die  'neun Löcher"  enthaltenden  Reinigungsraumes*': pascaita  ava  tä  niikioöii  .  .  *anfarym arioim  'yahe  *pänntarem  haca  anyaHlyS mayaäbyö  "drauf  soll  (er)  ,  .  sich  zu denen  auf  die  andre  Seite  des  Reini- gungsraumes setzen,  die  von  den  andern
dby  Google
IUI  iraaja.-
(zuvor  bezeichneten   sechs)  Löchern  ge- sondert ist"  V.p.29''.
*)  Ein  nach  aussen  durch  dcei  parallele  Furcb- itriche  abgegrenztes  Rechteck  auf  dem  Bodeo, Von  6  zu  16  Schritt,  auf  der  langen  Mittellinie drei  Löcher  mit  Wasser  und  sechs  mit  Rinder- bam  enthaltend.  Der  Raum  ist  zunächst  in iwei  wieder  mit  je  drei  Furchstrichen  umzogene Abteilungen  getchiedeo,  eine  kleinere  mit  den Wasser-  und  eine  grössere  mit  den  Hamlöchern. In  der  letitem  Abteilung  ist  abermals  durch drei  Furcbstiiche  an  der  den  Wasserlöchern abgekehrten  Seite  eine  Unterabteilung  mit  drei Löchern  geschaffen.  Die  Furch  st  riebe  werden  zu je  dreien  gezogen  der  Reibe  nach  l)um  die  Unter' abteilung,  3)  um  die  grössere  Abteilung,  3]  um beide  Abteilungen,  4}  um  die  kleinere  Abteilung ; Tgl.  zu  antariiür.  Dann  werden  an  bestimmten Stellen  des  Raums  Steine  od.  dgl.  niedergelegt. Vgl.Sp.  10450.  und  dieZeichnungenbeiWESTSBE. /1J.43S  und  DsT.ZA.2.  l6z  (dessen  Erliulerungen aber  nicht  stimmen).  Abweichend  Sp.  Übers,  i, Tafel  Zur  Reinigungszeremonie  s.West  aO.431. Ableit.  aut  'BiaYo-(mit  Verschiebung  des  Wort- akzents?]!),  etwa  'Raum  mit  den  Lochern'. — Pü. :  msej.  —  ■)  D.  i.  er  soll  von  der  grossem Abteilung  (PüErL  pa  gömH)  in  die  kleinere gehen.  —  *)  Ob  etwa  miy"  zu  lesen?
•  p.  magav-  {:  j.  moyu-)  Adj.,  bezeichnet einen  medischen  Volksstamm,  fdr  den  die Priesterwürde  vorbehalten  war,  'magisch, Magier'*';  /  martiy^  'gu!  äht^  gaumSt<^ nätnii'  Bh./.ii;  13%  14^,  ^.2,  b;  —  gau- matam  tyam  'gum  Bh./.ijJ,  16,^18.
■>  LitteraluT  bei  Jn.  Zor.  ö. KompA.  (s,  miypi'\  —  Et?  Die  Herkunft  des Worts  aas  dem  Assjmschen  (ZDMG.5J'.  16S} wird  vunNÖLDEKE  (Brief  oj.  06. 03}undBez0LD (BriefoS.  06. 03)  bestritten.  —  mp.  maiüi,  np.
•  j.  Taa.ja.wa.-  Adj.  'unverheiratef:  näiri- vaite  . .  ahntäl  pourum  framraomi  .  .ya%a 'vs  fraväxsöit  "dem  beweibten  spreche  ich den  Vorrang  zu  vor  dem,  dass  einer  unver- heiratet altem  sollte"  V,  4. 47.
Ableit.  aus  *maTav-  m.  'cselebs'.  —  VgL  got. magus  'Knabe',  maga^s  'Jungfrau'  [usw.,  FiCK Wb.4  3.  198).  —  Fü.:  i  öi  i  läiriilmand  . . hal  i  i  pti  ..fräl  gdwim  . .  Hgön  Ufa  marfih fräl  raft  islel;  dazu  die  ErL:  in  tan  ntsl  'd.  i.; er  hat  kein  Weib*.
•  g.  maga'van-  Adj.  'der  zum  'Bund', zur  zardSsustr&^OR'o.  ReligionsgemeinschaÜ gehört,  Sündler':  hyat  tmzd>m  iarai:mirB •vabyB  Mst  para  "was  Zar.  den  Bündlern als  Lohn  in  Aussicht  gestellt  hat"  Y.5/.  15;  1 —  yä  srvye  pari  {iAi)  *'gaonO'1  Y.^.  7. 1
**matay-  iiia
Pü.  (zu  Y.jt):  fia  pmtm  iHo-pi,  oA.:  fa  oft- lak  vihih;  (zu  Y.  5/):   f  m  dn  n  dan  n  (^pü.: mimtvätil,  ob  ma-^kSni  —  ')  NA.  'gSutä;  s. auch  V.  //.  7. j.  maj'na-  Adj.   (fem.  *«J-)   i)  "nackt,
°Ha{ND.)  anaiv/i.- 'BS  apajpayai  vasfrä t  *tanBni  N.55"';  — oss,  lauter*:  'nS  Bia'^rä
I.  täjnäg,  gr. -    I)  Einmal
entblösst':  dva  t vasfra  V.S.io;  — Yt.j9.s6;  —  •«?« 'na  F.  II.         a)*bl N.2«
Ableit.   —  Vgl.  i
yvfiMc  (von  denen  jedei  ant  emi
laut  weist].     —    Pü.:  briknak.
mayari'.  —  »)  Text:  afasläk  ngö
•  j.  ma}^3nta-  Adj.  'nackt,  entblösst*: vari>ian/(as(sd.yit  'tasat  P.  //,  ■*!*.  tOf)  '*.
Ableit.  aus  mayna-,  auffill,  Bildung;  vgl  HoRW GIrPh.  I  b.  146.  —  Pü.:  TÜSlai.  —  ')  Wo das  Wort  ganz  entstellt  isL
•  j.  maxäl-  f.  'Fliege':  druxs  yä  nasus  .. nivSiryete  mqnaym  ahe  >fl5a  'syä  par^mm (sd.)  M.8.6'9;  23  PüZ.;  —  basvan 'sinam »rrfaitinatn  ava.Janyät  V.  14.  f>;  —  °H F.  II.       '[V.7.2  lies:' maxä.i^Är^a.].
KompA.  —  mp.  (Pü.)  maxi,  kurd,  mil,  aif. mal;  vgl.  ai.  mditiiä-  f.  'Biene',  np.  magas.
•  j.  *niaxäi.V«hrp-"  f  'Fliegengestalt':  a^a druxs  ya  nasus  upa.dvqtaiti  .  .  'kihrpa srr^aitya  V.  7.  %.
Pü.:  pa  maxi  karf.  —  ■)  NA.  trennt.
•  j.  maxäi.b3r«ta-  Adj.  'von  Riegen  ver- tragen, fortgeschleppt':  '0  nasu/  Y.S-i; j.  14  PüZ.;  —  aite  nasävö  ya  .  .  'taca nasui  V.  5. 4,
Pü. :  max!  buri.
•  j.  maxätay-  m.  EN.  eines  Gläubigen: sps.pt&ü  °Uis  alaonB  "des  Sp.,  Sohns  des M.  . ."  Yt  13.  116;  —  payanharo  'ieis aiaons  Yt.  13. 116.
Eig.  Bed.?
•  p.  maäya-  Adj.,  bezeichnet  ein  Volk'*: ima  dahySvJ'  fyä  adam  agarbäyam  , .  'yS (NPm.)  D.ff.3;  —  iyam  (sd.)  'ya  D./o(?).
')    liERODOT  4.  I9I;   ^ffi{iu(;   vgl.  JUSTI  GlrPh.
=== leaf/col ===
leaf 618
```


## [2026-09-07T15:54:37.220Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls site/pages/319.jpg 2>/dev/null; mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad; pdftoppm -f 319 -l 319 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg319 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/",
 "description": "Render PDF page 319"
}
```


### [2026-09-07T15:54:38.963Z] TOOL RESULT

```
site/pages/319.jpg
total 700
drwx------ 2 sfmqrb sfmqrb   4096 Sep  7 11:54 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  7 11:48 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    251 Sep  7 11:49 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   3537 Sep  7 11:53 c_migare2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   1829 Sep  7 11:53 c_migare3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   2261 Sep  7 11:53 c_migare4.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3958 Sep  7 11:53 c_migare.png
-rw-rw-r-- 1 sfmqrb sfmqrb  19652 Sep  7 11:53 c_semita2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   2639 Sep  7 11:53 c_semita.png
-rw-rw-r-- 1 sfmqrb sfmqrb  40259 Sep  7 11:50 ferdowsi2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  30950 Sep  7 11:51 ferdowsi3.png
-rw-rw-r-- 1 sfmqrb sfmqrb  28946 Sep  7 11:51 ferdowsi4.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4298 Sep  7 11:50 ferdowsi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  97817 Sep  7 11:50 pg318hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  62558 Sep  7 11:50 pg318.png
-rw-rw-r-- 1 sfmqrb sfmqrb  67293 Sep  7 11:54 pg319.png
-rw-rw-r-- 1 sfmqrb sfmqrb  65279 Sep  7 11:49 pg324.png
-rw-rw-r-- 1 sfmqrb sfmqrb 163982 Sep  7 11:53 pg327hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  73619 Sep  7 11:52 pg327.png
-rw-rw-r-- 1 sfmqrb sfmqrb     40 Sep  7 11:49 queue.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   1308 Sep  7 11:54 v2001.txt
```


## [2026-09-07T15:54:42.182Z] TOOL CALL #29: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg319.png"
}
```


### [2026-09-07T15:54:42.534Z] TOOL RESULT

```

```


## [2026-09-07T15:54:42.529Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T15:55:05.079Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n 1,200p tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-07T15:55:05.118Z] TOOL RESULT

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


## [2026-09-07T15:55:07.529Z] TOOL CALL #31: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-07T15:55:07.538Z] TOOL RESULT

```


```


## [2026-09-07T15:55:11.588Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/marcasite",
 "prompt": "Give the full etymology section for marcasite verbatim, including the chain through French/Medieval Latin/Arabic/Syriac/Aramaic/Persian and any notes on the direction of borrowing."
}
```


## [2026-09-07T15:55:12.179Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Amazon",
 "prompt": "Quote the full entry for Amazon (Greek Amazon, the folk etymology 'without breast', the Iranian ha-mazan hypothesis, and the river name)."
}
```


### [2026-09-07T15:55:16.866Z] TOOL RESULT

```
# Etymology of Marcasite

Based on the Wiktionary entry provided, the etymology section contains the following information:

**Etymology tree shown:**
- Sumerian _𒈥𒄩𒅆𒆠_ (Marhaši) → derived
- Arabic _مَرْقَشِيتَا_ (marqašītā) → derived
- English **marcasite**

**Etymology text:**
"From Medieval Latin _marchasita_ et al., from Arabic _مَرْقَشِيتَا_ (marqašītā)."

The entry does not provide an extended chain through French, Persian, Syriac, or Aramaic in the etymology section itself. The etymology tree indicates the word traveled from Sumerian through Arabic to Medieval Latin and into English. While translations appear in multiple languages (including Classical Syriac and Aramaic versions listed in the translations section), the etymology section does not explicitly trace borrowing through those languages or discuss directional borrowing beyond stating the Medieval Latin and Arabic origins.
```


### [2026-09-07T15:55:18.264Z] TOOL RESULT

```
# Amazon Etymology Entry

**Origin:** The term enters English in the late 14c. from Old French or Latin, deriving from Greek *Amazon*, likely from "an unknown non-Indo-European word."

**Greek Root:** The word probably stems from "an unknown non-Indo-European word, or possibly from an Iranian compound *\*ha-maz-an-* '(one) fighting together.'"

**Folk Etymology:** A popular but incorrect explanation derives the term from "a- 'without' + mazos, variant of mastos 'breast,'" giving rise to the legend that "the Amazons cut or burned off one breast so they could draw bowstrings more efficiently."

**River Name:** The Amazon river in South America was "rechristened with this name by Francisco de Orellana, 1541, after an encounter with female warriors." Some scholars propose instead that "the river name is a corruption of a native word in Tupi or Guarani meaning 'wave.'"
```


## [2026-09-07T15:55:29.499Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%91%CE%BC%CE%B1%CE%B6%CF%8E%CE%BD",
 "prompt": "Give the etymology of Ancient Greek Ἀμαζών verbatim: any mention of Iranian *ha-mazan-, the a- + mazos folk etymology, Beekes' view (pre-Greek/unknown), and citations."
}
```


## [2026-09-07T15:55:31.265Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/maga%C3%BEs",
 "prompt": "Give the etymology of Proto-Germanic *magaþs verbatim: the PIE root, related forms (Avestan, Old Irish, Gothic magaþs), and descendants including Old English mægden."
}
```


### [2026-09-07T15:55:32.066Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T15:55:36.660Z] TOOL RESULT

```
# Etymology of Proto-Germanic *magaþs

Based on the Wiktionary source, here's the etymological information:

**Origin:** The term derives "from pre-Germanic *magʰ-ot-(i-), a feminine derivative of *maguz ('boy')" with a suffix also appearing in *brūdiz ('bride').

**Key note on roots:** The article indicates this word pair "is likely of foreign or substrate origin," rather than having a clear Proto-Indo-European pedigree.

**Related forms:** A cognate exists in Proto-Celtic *magotaxtā ('young girl, servant girl').

**Descendants:** The word evolved into numerous Germanic languages:
- Old English: mæġeþ, mæġþ
- Gothic: magaþs
- Dutch: maagd, meid
- German: Magd, Maid
- West Frisian and Old Frisian forms

The article emphasizes this reconstruction is "hypothesized to have existed based on comparative evidence" rather than directly attested.
```


## [2026-09-07T15:55:43.696Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E1%BC%88%CE%BC%CE%B1%CE%B6%CF%8E%CE%BD",
 "prompt": "Give the etymology of Ancient Greek Ἀμαζών verbatim: Iranian *ha-mazan- hypothesis, the a- + mazos folk etymology, Beekes/pre-Greek view, and any cited sources."
}
```


## [2026-09-07T15:55:45.577Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%B1%D9%82%D8%B4%D9%8A%D8%AA%D8%A7",
 "prompt": "Give the Arabic entry مرقشيتا verbatim: etymology (Aramaic/Syriac/Persian/Sumerian Marhaši), meaning, and descendants."
}
```


### [2026-09-07T15:55:50.041Z] TOOL RESULT

```
# Etymology of Ἀμαζών

## Folk Etymology
The Greeks proposed: "ἀ- (a-, 'not') + μαζός (mazós, 'breast')" suggesting Amazons removed their right breast to shoot arrows better. However, this explanation is "almost certainly a folk etymology" since artwork consistently depicts them with intact breasts.

## Iranian Hypothesis
The word likely derives from Old Persian *hamazan- ("warrior"), possibly reanalyzed as "hama-zan" meaning "together-beating/striking/slaying," referencing military comradeship. This theory accounts for the absent initial aspirated *h-, as Ionic Greek lost aspiration early.

## Proto-Indo-European Theory
An alternative native Greek origin from Proto-Indo-European *n̥-mn̥gʷ-yō ("manless one") has been proposed, deriving from *mongʷyos ("man"). However, this explanation is "deemed unlikely by Hjalmar Frisk."

## Additional Theories
The etymology section notes: "Numerous other etymologies have been proposed, generally tracing the word back to Iranian, Greek or (West/East) Caucasian languages."

**Note:** The page does not cite Beekes or pre-Greek theories specifically in the provided text.
```


### [2026-09-07T15:55:52.688Z] TOOL RESULT

```
# مرقشيتا (Marcasite)

**Meaning:** A feminine Arabic noun referring to "marcasite, pyrite, and similar minerals of ferrous sulfate."

**Etymology:** The word traces through multiple ancient languages:
- From Aramaic _marqəšīṯā_
- Ultimately from Akkadian _marḫašītu_ ("glass or artificial gem"), itself derived from the Akkadian term for a precious stone
- The stone name originates from Sumerian _mar-ḫa-šiKI_, referencing the Mesopotamian region Marhasi

The entry notes the word "encountered in Persian as _marqašišâ_" and influenced by Persian _šiše_ (glass).

**Descendants:** The Arabic term spawned several European borrowings:
- Medieval Latin _marchasita_, which produced:
  - English: marcasite
  - French: marcassite
  - Spanish: marcasita
- Spanish also adopted: _margajita_
```


## [2026-09-07T15:56:09.162Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://vajehyab.com/?q=%D8%A2%D9%85%D8%A7%D8%B2%D9%86",
 "prompt": "Is there an entry for آمازن (from Farhang-e Mo'in / other dictionaries)? Quote any entry text, including definitions of آمازن or آمازون as warrior women or the river."
}
```


## [2026-09-07T15:56:11.533Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%85%D8%B1%D9%82%D8%B4%DB%8C%D8%B4%D8%A7/",
 "prompt": "Quote the entries for مرقشیشا, especially the فرهنگ معین and لغت‌نامه دهخدا sections, including any etymology tag (e.g. [آرامی] or [ع.]) and the definition."
}
```


### [2026-09-07T15:56:13.901Z] TOOL RESULT

```
# Entry for آمازن

Based on the webpage content, there is an entry from **Lughat-name Dehkhoda** (دهخدا):

"آمازن . [ زُ] (اِخ ) نام رودی بزرگ در آمریکای جنوبی ، و آن بزرگترین ِ رودهای جهان است"

This defines آمازن as "the name of a large river in South America, and it is the greatest of the world's rivers."

The entry shown focuses exclusively on the geographical definition (the Amazon River) rather than the mythological or warrior-related meaning. No definitions related to Amazon warrior women appear in the visible search results on this page.
```


### [2026-09-07T15:56:18.213Z] TOOL RESULT

```
# مرقشیشا - Dictionary Entries

## لغت‌نامه دهخدا
**Etymology:** The word originates from Aramaic "مرقشیثا" or "کیفا مقشیثا" meaning hard stone.

**Definition:** "جوهری باشد که در داروهای چشم بکار برند" (a substance used in eye medicines), with varieties including gold, silver, copper, and iron types.

## فرهنگ معین
**Definition:** "پیریت سفید که در قدیم به عنوان دارو در معالجۀ درد چشم کاربرد داشته است، سولفور طبیعی آهن" (white pyrite formerly used as medicine for eye pain; natural iron sulfur).

The entries emphasize its historical pharmaceutical use and mineral composition as a white-colored iron sulfide compound.
```


## [2026-09-07T15:56:33.194Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== IEC maghos/maghu ===\"; grep -n \"^magh\\|magho\\|maghu\" IEC.txt | head -15; echo \"=== SKT amazon ===\"; grep -n -i \"^Amazon\\|Amazon\" SKT.txt | head -5; echo \"=== FSD amazon ===\"; grep -n -i \"am'a-zon\\|amazon\" FSD_vol1.txt | head -5; echo \"=== WEB amazon ===\"; grep -n -i \"am'a-zon\\|Am'a-zon\\|amazon\" WEB_vol1.txt | head -5",
 "description": "Grep Mann, Skeat, Funk, Webster"
}
```


### [2026-09-07T15:56:33.329Z] TOOL RESULT

```
=== IEC maghos/maghu ===
10245:maghido, ið (maghdið) “beat, pound, crush? OW, W maeddu, v. ‘pound, buffet’; OCz. mož- diti, inf. ‘pound, crush’; R možžù, moZZit, id. (OCS po-mozdati ‘weaken’ seems to be related to Gk. mokhthéo ‘toil, suffer’. Cf. mogh- and derivatives)
16376:smaghos, à ‘toil, turmoil". (Celt. and Li. am- big. Gk. also, but Bois. untenable) Gk. mákhe, f. ‘battle (a type *mnghå: *mongh-:G Hand-gemenge seems improb- able); cf. mákhlos, adj. ‘fierce; lewd’; Ir. am- big. smag, m. ‘slap’, smaig, f. “discipline” appear to be Eng. LWs, since no vb. occurs); W cf. maon, pl. ‘crowd, surge’; Li. (ambig.) smagus, adj. “sharp, strong, smart’; MHG cf. smaht, sm. (2) ‘faintness’; G schmachten, v. ‘faint’ and perh. Lat. maereo, ere, v. ((mourn', if for *smagher-)
=== SKT amazon ===
=== FSD amazon ===
13423:Those  dreadful  Amazons,  'g&Uant  viragoes,’  who  .   .   .   carried victorious  arms  .   .   .   into  Syria  and  Asia  Minor.
13426:Tho  other  amazon  kind  Heaven Had  arm’d  with  spirit,  wit,  and  satire.
13427:Gray  A   Long  Slorg  at.  8. {L.,  <   Gr.  Amazon.]  Am"a-zo'nI«ant.—  Am'a-zoneant", n.  A   formicid  ant  (Polycrgus  rufesccns)  that  carries  off  the young  of  other  species  and  enslaves  them.— A.  stone*  a bright  verdigris-green  inicrocllne  feldspar,  used  as  a   gem; amazoulte.
13428:am'a-zon",  n.  1.  An  American  parrot  (genus  Chry - softs);  as,  the  mealy  amazon  (C.  /arnnosa).  2.  One  of various  humming°birds.  [   <   the  river  Amazon.]
13429:see  amateur.]  —   -ly,  adc*—  amatorlal  muscles,  the  ob-  Am'a-zon*,  n.  A   river  flowing  across  northern  South Uque  muscles  of  the  eye:  so  called  because  used  in  ogling.  America  from  the  Andes  to  the  Atlantic;  length,  about
=== WEB amazon ===
6335:Am/a-z6n, n. (L., from Gr. Amaz6én; a priv., and mazos, breast. Derived by Greek folk etym. from the legend that the Amazons cut off the right breast to facilitate the use of the bow and javelin.]
6341:6. an Amazon ant.
6343:Am.-4a-z0/ni-an, a. 1. pertaining to or resem- bling an Amazon; hence, of masculine man- ners; warlike: applied to females.
6344:2. belonging to the River Amazon in South America, or to the country around it. am/a:zon-ite, n. Amazon stone.
6345:Am/a:z6n stone, a bright green variety of microlite, used as a gem, found on the banks of the Amazon River and elsewhere.
```


## [2026-09-07T15:56:44.273Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== IEC magh other ===\"; grep -n \"maghu\\|maghoti\\|magho-\\|mogho\\|magos\" IEC.txt | head -10; echo \"=== SYN Magd/magaths ===\"; grep -n \"magaþs\\|magaths\\|Magd\\b\" SYN.txt | head -10; echo \"=== SYN machomai ===\"; grep -n -i \"máchomai\\|makhomai\\|máchē\" SYN.txt | head -5",
 "description": "Grep Mann and Buck"
}
```


### [2026-09-07T15:56:44.346Z] TOOL RESULT

```
=== IEC magh other ===
10467:mëghos (2) ‘kinsman, esp. by marriage. Same as (1)? (Gmc. only) Go. megs 'son-in-law ; MHG mac, gs mages, sm. & màge, wm. (*blood-kinsman' sic!); OE mag, pl. magas, mf “male or female kinsman’; mága, wm., mage, wf. id. (m. also ‘son, des- cendant'); OS màg, m. ‘male kinsman’; OFris. mëch, mei, m. id.; ON mágr, gs mágs ‘male kinsman by marriage’; cf. mágkona ‘female kinsman by marriage’; OE cf. also m&gp, f. ‘clan’; ON mægð, f. “kinship by marriage’. Cf. moghos (2). (The semantic notion linking this word with *meghos (1) is suggested by the formulae in Cor. broder-da: Fr. beau-frére: Du. schoon-broeder: Big. draginko *brother- inlaw’
10470:me$gont- ‘size, quantity’. Cf. me£-, etc. and unrelated moghont- Olr. mælt, Ir. méid, m. f. ‘quantity’; OW meint, W maint, f. ‘quantity, size, amount’; cf. cy- faint “how much’; Cor. kem-mys, ke-myns
10996:moghotos, à, is “strong; strength’. (Variant of type moghtis, q. v.) Gaul. cf. mageto-, mogeti- (in names); Ir. cf. mocht ‘large’; mochta, pp 'enlarged'; Olr. mochta & mogda, id. (and *mighty'); R mogo- tà “strength, force’.
=== SYN Magd/magaths ===
=== SYN machomai ===
```


## [2026-09-07T15:56:46.242Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; python3 - <<'EOF'\npages=open('WLD_Bd2_pages.txt',encoding='utf8',errors='replace').read().split('\\f')\nprint('leaves',len(pages))\nfor p in (227,228):\n    leaf=p+5\n    print('==== printed',p,'leaf',leaf)\n    print(pages[leaf-1][:1800])\nEOF",
 "description": "Read Walde-Pokorny II pp.227-228"
}
```


### [2026-09-07T15:56:47.650Z] TOOL RESULT

```
leaves 725
==== printed 227 leaf 232
                                                         :                                         ;




                                      magh- magh
                                            :                magh-                              227

passend sein'‘ usw., letzteres fiir got. mtgs „Schmegersohn^‘, ahd. mag
„Verwandter'‘ and fiir ahd. gimahalo „Gatte, Brautigam'', fem. gimahala,
mahalen „verloben“, nhd. Gemalil{m), vermdhlen, die ein von anahalen
„sprechen“, got. mapljan verschiedenes "^niaJiljan voraussetzen sollen, aber
gewiB vielmehr als      offentlicher Yersammlnng fiir verbiinden erklaren^^
bei ahd. mahalen,        „Yersaininlung^^ zu verbleiben haben. Die Sippe
got. megs,    lit.   megti vereinigt sich unter idg. megli-              5
                                                                             ,Wohlgefallen; lieb-
reiche Gesinnung^.
  Nicht hieher arm. macanim, macmim „anhaften, gerinnen^^ usw. (vom
Begriff der fetten Schmiere  oder des Anknetens, Meillet Msl. 10,279, in
anderer Gruppierung bei Liden BB. 21, 99 f., s. u.; von Charpentier KZ.
46, 38 zu mosgo- „Mark“ gestellt), das w^ohl sicher zu mad- ,,na6''.



magh- magh- „k6nnen, vermogen, helfen“.
          :




   Gr,               dor. jady^og „Hilfsmittel“,                     dor. juayavd „Hilfsmittel
List;    Werkzeug; Mittel, etvvas zu erlangen“;
   got. fnag (Inf.     magan, Praet. ynahta) „vermag, kann'',                 aisl.   ma (Inf. mega;
vermag nicht idg. e-Yokalismus zu stiitzen, Meillet Msl. 14, 335), ahd. mag
Unagan), as. mag (nitigan), ags. mceg ds.
   aisl. magn, megin „Kraft, Macht“, ags. mcegcn, as. megin, ahd. magan.

megin ds.: got. mahts „Kraft, Macht“, ahd. as. maid, ags. meaht, might,
aisl. mdttr ds.;

   abg. mogq^ most! „konnen, vermogen'', pomos
==== printed 228 leaf 233
228                         iuag(h)-   — mat- oder mot-
ii[iag(h)-   „etwas.Kleines“??
    Alb. module „Erbse‘‘, lit. moHs „Kleinigkeit‘' (Pedersen KZ. 36, 335 zw.)
lit. 7nazas „klein‘\ mdftnfi   „klein macben, verringern'' (Wood Mod. Phil.
11, 31 8f. vergleicht mdzas nicht uberzeugend mit nhd. mdhtln),


maghn- „Knabe, Jungling, nnverheiratet'' und zugehorige Pem.-Bldgn.
   Av. mayava- „unYerheiratet“ (Bartholomae Airan. Wb. 1111); kelt. "^magiis
(s. zum Vokalismus Pokorny KZ. 45, 73)     in gall. Magii-rix^ ir. (Ogam)
magu, air. mang, mug „Sklave'‘; corn, matv^ bret. mao „Jungling, I)iener“,
cymr. meu-dwy „Ein8iedler‘^ (eig. „Diener Gottes“); Pem. com. mowcs
„Madchen“, bret. maouez „Prau''; kelt. -mo- Ableitung in air. mam, mdam
,jugum, servitus“ (Lit. bei Liden BB. 21, 99, der es aber selber unrichtig
zu germ. *makdn stellt, s. *mag- „kneten“); Abstraktum kelt. *magot-acta
jjJungferaschaft, junge Weiblichkeit'* (weitergebildet aus ^maghotis     =  got.
magaps) in ir. ingen maccdacht ,junges erwachsenes Madchen^^, air. ro-
macdact gl. „superadulta“, acorn, mahtheid „virgo‘‘, mcorn. maghteth, maghtyth,
ds., bret. matez „Dien8tmadchen“ (gegen Verbindungen dieser Pormen mit
air. macc, cymr. mah „Sohn“ s. Yf. Tiber alteste sprachl. Beziehungen zw.
Kelten und Italikern 60ff.) got. magus „Knabe“, aisl. mqgr „Sohn, junger
                                 ;


Mann“, as. magu „Knabe“, ags. magu               Sohn, Mann“; Pem. ^ma{y)wJ
in got. mawi „Madchen“ (gen. maujds\ aisl.             (Acc. mey) „Madchen‘‘,
Demin, got. mawilo^ aisl. meyla, ags. meowle „kleines Madchen'^; Abstractum
*maghotis „junge Weiblichkeit^', woraus konkret „Madchen“, in got. magaps
,
 junge Prau“, ags. mmgep (engl. maid)^ as. magath^ ahd. magad^ nhd. Magd^
Demin. Mddchen, Die kelt.- germ. Yerkniipfun
```


## [2026-09-07T15:56:59.622Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; grep -n -i \"amazon\\|ha-mazan\\|hamazan\" WLD_Bd2_pages.txt | head; echo \"=== kaempfen near magh ===\"; python3 - <<'EOF'\npages=open('WLD_Bd2_pages.txt',encoding='utf8',errors='replace').read().split('\\f')\nfor p in (226,227):\n    print('==== printed',p)\n    t=pages[p+5-1]\n    print(t[:1200])\nEOF",
 "description": "Find Walde-Pokorny magh- fight"
}
```


### [2026-09-07T15:57:01.077Z] TOOL RESULT

```
=== kaempfen near magh ===
==== printed 226
226                           maqh-o-s, “{s)lo-   — mag-

maqh’O-s, -(s)lo- „ausgelas8eii“?
  Ai. maichd- „munter, lustig, ausgelassen", m. „Freudeiibezeiguiig, Feier,
Preis^.
  Gr. fidxXog „geil, iippig (von Weibern); in wilder Lust tobend
Aeschylos)“.
  Prellwitz     s. v., Uhlenbeck Ai. Wb. 209.




miko- Oder nioko- moko- „Ebene, Steppe“?
                       ;



  Aisl. md^r i^moha-z) „Steppe, Heide‘‘      :    ir.   macha „Ebene'‘ (wohl aus ma-
Jcosia Oder malzovia^ nicht nach Fick II ^ 196 aus ^makaia).               Fick III^ 322,
Falk-Torp u. mo, Unsicher.


mag- „kneten, drucken, streichen'^
  Gr. fxayrjvai, jne/biayjLieyr] zu fidaoco (zum Praes.       s.   menq- „kneten“), jLia-
yevg „der Knetende‘‘, juaylg „geknetete Masse^‘, judysiQog (eigentlich judylgog,
Wackernagel IF. 25, 326f.) „Koch“, juaySaXla „Stuckchen Brot zum Fett-
abwischen“ (ob auch /nd^a oder /LidCa „Teig aus Gerstenmehl, Fladen**?
s. Boisacq s. v. m. Lit.; eher die jiidische Maize nach ABmann Phil. 67,
199 an);
  air.    maistre „Butterfa6“ (^mag-s-eh^ia)^ mir. maistir „buttern, quirlen“
(Stokes BB. 25, 256;     nicht besser ist Pedersens KG. II 45 Gdf. mnq-s-tr7,
zur Wz. menq-^ bret. meza „kneten“, c
==== printed 227
                                                         :                                         ;




                                      magh- magh
                                            :                magh-                              227

passend sein'‘ usw., letzteres fiir got. mtgs „Schmegersohn^‘, ahd. mag
„Verwandter'‘ and fiir ahd. gimahalo „Gatte, Brautigam'', fem. gimahala,
mahalen „verloben“, nhd. Gemalil{m), vermdhlen, die ein von anahalen
„sprechen“, got. mapljan verschiedenes "^niaJiljan voraussetzen sollen, aber
gewiB vielmehr als      offentlicher Yersammlnng fiir verbiinden erklaren^^
bei ahd. mahalen,        „Yersaininlung^^ zu verbleiben haben. Die Sippe
got. megs,    lit.   megti vereinigt sich unter idg. megli-              5
                                                                             ,Wohlgefallen; lieb-
reiche Gesinnung^.
  Nicht hieher arm. macanim, macmim „anhaften, gerinnen^^ usw. (vom
Begriff der fetten Schmiere  oder des Anknetens, Meillet Msl. 10,279, in
anderer Gruppierung bei Liden BB. 21, 99 f., s. u.; von Charpentier KZ.
46, 38 zu mosgo- „Mark“ gestellt), das w^ohl sicher zu mad- ,,na6''.



magh- magh- „k6nnen, vermoge
```


## [2026-09-07T15:57:06.818Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; python3 - <<'EOF'\npages=open('WLD_Bd2_pages.txt',encoding='utf8',errors='replace').read().split('\\f')\nt=pages[227+5-1]\nprint(t[1200:4000])\nEOF",
 "description": "Rest of WLD p.227"
}
```


### [2026-09-07T15:57:08.161Z] TOOL RESULT

```
n, helfen“.
          :




   Gr,               dor. jady^og „Hilfsmittel“,                     dor. juayavd „Hilfsmittel
List;    Werkzeug; Mittel, etvvas zu erlangen“;
   got. fnag (Inf.     magan, Praet. ynahta) „vermag, kann'',                 aisl.   ma (Inf. mega;
vermag nicht idg. e-Yokalismus zu stiitzen, Meillet Msl. 14, 335), ahd. mag
Unagan), as. mag (nitigan), ags. mceg ds.
   aisl. magn, megin „Kraft, Macht“, ags. mcegcn, as. megin, ahd. magan.

megin ds.: got. mahts „Kraft, Macht“, ahd. as. maid, ags. meaht, might,
aisl. mdttr ds.;

   abg. mogq^ most! „konnen, vermogen'', pomosti, iter, pomagati „helfen“
usw., abg. mosth, russ. moch usw\ ,,Macht, Starke" (== got. maids).      Ent-
lehnung der slav. Sippe aus der germ. (Hirt PBrB. 23, 335, Wiedemann
BB. 28, 63, Uhlenbeck PBrB. 30, 300) widerlegt durch Trautmann KZ. 46,
180fiF. (s. auch Berneker II 67 f., 70), der aus der alten Opt.-Form skr.-ksl.

7noz^ „potes", skr. moz, tech. alt.     ,,
                                           potest" got. mageis, magi ein altes
                                                                :




unthem. Praes. "^magli-mi ^mogh-me. Opt. "^nidgh-iem usw^ erschlieBt. Nach
                                  ;


Trubeckoj (Slavia I 14ff.) ware die slav. Form Umbildung eines alten Praet.
  Lehnworte sind (nach Briickner AfslPh. 20, 490)     apr. massi „kann" (aus
poln. moze\   muslngin Acc. „moglich" (umgebildet aus poln. moznij\ lit.
pamagoti „helfen", magoti „nutzen, taugen" (aus dem Slav.).
   Ygl. Osthoff PBrB. 15, 21 Iff., Fickl^ 104, 279, 508 (hier, wie II^ 197,
mit Unzugehorigem, bes. der Sippe ^^megili)- grofi" s. d.), usw.
   Die germ. Sippe trotz \Yiedemann aaO. (auch Collitz Schwach. Praet. 39,
der sich auf das Praet. mahta beruft, das aber nach Sverdrup lA. 35, 8
fiir "^magda stehn kann) nicht zu gr. p.ay.o6g. pfjxog (Wz. mafc- „lang und

diinn"), was auch Entl. der si. Sippe aus dem Germ, zur Yoraussetzung
hatte.



magh- „kampfen".
  Gr.                  Lw. aus einem            iran.   Yolksnamen ^lia-mazan- „Krieger",
vgl.   apataxagav (:       ar.   Icar-   „machen")-
                                           Tzokepelv, Ueooai Hes.     gr. adyo-         :


pai „kampfe", adyg] ,,Kampf, Schlacht". paypioa „Schwert, Messer".
   Lagercrantz Xenia Lideniana (191 2). 270 ff. [Citat nach Boisacq 1093, 1118;
8. diesen 616 iiber bisherige Deutungen von payopai].
```


## [2026-09-07T15:57:21.434Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for f in AFM.txt AFM_pages.txt incoming/PLA/PLA_pages.txt ARY_pages.txt incoming/ARY/ARY_pages.txt HRN.txt HUB.txt AFA.txt; do [ -f \"$f\" ] && printf \"--- %s: \" \"$f\" && grep -c \"مرقش\\|marqas\\|marqash\\|Markasit\" \"$f\"; done; echo; echo \"=== ARY amazon/marqashisha ===\"; grep -n \"مرقشیشا\\|آمازن\" incoming/ARY/ARY_pages.txt | head",
 "description": "Check Addi Shir, Asbaghi, Aryanpur, Horn, Hübschmann for the word"
}
```


### [2026-09-07T15:57:22.711Z] TOOL RESULT

```
--- AFM.txt: 0
--- AFM_pages.txt: 0
--- incoming/PLA/PLA_pages.txt: 0
--- incoming/ARY/ARY_pages.txt: 0
--- HRN.txt: 0
--- HUB.txt: 0
--- AFA.txt: 0

=== ARY amazon/marqashisha ===
```


## [2026-09-07T15:57:28.939Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"markas\\|marqas\\|marqaš\\|markaš\\|Schwefelkies\\|Kies\\b\" AFA.txt | head -10; echo \"--- size\"; wc -l AFA.txt; head -5 AFA.txt",
 "description": "Check Fraenkel for marqashitha"
}
```


### [2026-09-07T15:57:28.994Z] TOOL RESULT

```
--- size
17457 AFA.txt
Google
This is a digital copy of a book that was prcscrvod for gcncrations on library shclvcs bcforc it was carcfully scannod by Google as pari of a projcct
to make the world's books discoverablc online.
It has survived long enough for the Copyright to expire and the book to enter the public domain. A public domain book is one that was never subject
to Copyright or whose legal Copyright term has expired. Whether a book is in the public domain may vary country to country. Public domain books
```


## [2026-09-07T15:57:42.310Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A2%D9%85%D8%A7%D8%B2%D9%86/",
 "prompt": "Quote all dictionary entries for آمازن (Dehkhoda, Mo'in, others): both the river sense and any 'warrior women' sense."
}
```


## [2026-09-07T15:57:42.458Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n 1,40p tools/fetch_source.py",
 "description": "Check fetch_source.py usage"
}
```


### [2026-09-07T15:57:42.495Z] TOOL RESULT

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
```


### [2026-09-07T15:57:44.768Z] TOOL RESULT

```
The server returned HTTP 400 Bad Request.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-07T15:57:47.102Z] AGENT

Now archiving the web sources I used.


## [2026-09-07T15:57:52.727Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/marcasite' --note 'page 319, root Mağšîsa: English marcasite < ML marchasita < Arabic marqašītā (Wiktionary etymology tree Sumerian Marhaši > Arabic)'; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%85%D8%B1%D9%82%D8%B4%D9%8A%D8%AA%D8%A7' --note 'page 319, root Mağšîsa: Arabic marqašītā < Aramaic marqəšīṯā < Akkadian marḫašītu < Sumerian Marhaši; notes Persian marqašišâ as a later reshaping under influence of šīše'; python3 tools/fetch_source.py 'https://www.etymonline.com/word/Amazon' --note 'page 319, root Magh 2: Greek Amazon, Iranian *ha-maz-an- hypothesis, Orellana 1541 river name, Tupi alternative'",
 "description": "Archive first three web sources"
}
```


### [2026-09-07T15:57:55.727Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/bd910d0f2adc31fb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d6432ad500cecbeb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4c27d25b1fb19db8.txt
```


## [2026-09-07T15:58:04.385Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%E1%BC%88%CE%BC%CE%B1%CE%B6%CF%8E%CE%BD' --note 'page 319, entry Magh 2 node 2: Ancient Greek Ἀμαζών etymology, Iranian *hamazan- vs folk etymology a-+mazos'; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/maga%C3%BEs' --note 'page 319, entry Maghos/Maghu nodes 3-4: PGmc *magaþs < pre-Gmc *magʰ-ot-(i-), fem. of *maguz; Wiktionary flags the pair as possibly substrate'; python3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D9%85%D8%B1%D9%82%D8%B4%DB%8C%D8%B4%D8%A7/' --note 'page 319, root Mağšîsa: Dehkhoda quotes Moin - Aramaic مرقشیثا / کیفا مقشیثا \"hard stone\"; Moin defines مرقشیشا as white pyrite used in eye medicine'; python3 tools/fetch_source.py 'https://vajehyab.com/?q=%D8%A2%D9%85%D8%A7%D8%B2%D9%86' --note 'page 319, entry Magh 2 nodes 5/9: Dehkhoda آمازن = name of the great river of South America'",
 "description": "Archive remaining web sources"
}
```


### [2026-09-07T15:58:08.135Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/80525a046968a6a2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/702cea493fd5d1f4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3fcbc6a0d2d84fa2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a22a1459a3794cae.txt
```


## [2026-09-07T15:58:11.238Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in 3fcbc6a0d2d84fa2 a22a1459a3794cae; do echo \"===== $f\"; grep -o \"آمازن[^\\n]\\{0,200\\}\\|مرقشیشا[^\\n]\\{0,300\\}\" $f.txt | head -8; done",
 "description": "Verify archived Persian pages contain the entries"
}
```


### [2026-09-07T15:58:12.542Z] TOOL RESULT

```
===== 3fcbc6a0d2d84fa2
مرقشیشا - معنی در دیکشنری آبادیس
مرقشیشا - معنی در دیکشنری آبادیس 
مرقشیشا
مرقشیشا. [ م َق َ ] ( اِ ) اصل کلمه آرامی است و آن کیفا مقشیثا باشد یعنی سنگ سخت. ( یادداشت مرحوم دهخدا ). جوهری باشد که در داروهای چشم بکار برند و آن را اقسام باشد: ذهبی و فضی و نحاسی و حدیدی و شبهی ، و بهترین آن ذهبی است و آن را به عربی حجرالنور خوانند. ( برهان ). اسم یونانی سنگی است ، و او ذهبی و فضی و 
مرقشیشا درسیستم رومبواِدریک متبلور میشود، وزن مخصوص آن بین 4/6 تا 4/8 است و سختی آن بین 6 تا 6/5 است ( یعنی شیشه را خط می اندازد ). بعلت همین سختی جالب توجه و رنگ سفیدش در جواهرسازی مورد استعمال دارد. در اکثر زمینهای گچی و گل سفیدی فراوان است. در تشکیلات گچی اطراف فرحزاد تهران سنگ مزبور بسیار یافت میشود و 
مرقشیشا و توتیا و... ( التفهیم ).
مرقشیشای زر
مرقشیشا در سیستم رومبوادریک متبلور میگردد . این سنگ دارای وزن مخصوص بین ۴/۶ تا ۴/۸ است و سختی آن بین ۶ تا ۶/۵ است ( یعنی شیشه را خط میاندازد ) . بعلت همین سختی جالب توجه و رنگ سفیدش درجواهر سازی مورداستعمال دارد . اسید کلریدریک را بر آن اثری نیست ولی اسیر نیتریک در آن تاثیر دارد و آنرا تجریه میکند . در اکث
===== a22a1459a3794cae
آمازن | واژه یاب
آمازن | واژه یاب 
آمازن
آمازن . [ زُ] (اِخ ) نام رودی بزرگ در آمریکای جنوبی ، و آن بزرگترین ِ رودهای جهان است .
آمازن بطول 1500 هزار گز.
آمازن زیست کند و هم در مجاری آبهای دیگر برزیل .
```


## [2026-09-07T15:58:41.532Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"^Maid\\|Maiden\\b\" SKT.txt | head -5; echo \"=== FSD maiden ===\"; grep -n \"maid'en\\|mad'en\\|mzgden\\|mægden\" FSD_vol3.txt FSD_vol2.txt 2>/dev/null | head -5; echo; mkdir -p ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg319.png ocr/BOOK/319.png && ls -la ocr/BOOK/ | tail -3",
 "description": "Grep Skeat/Funk for maid; copy page PNG"
}
```


### [2026-09-07T15:58:42.873Z] TOOL RESULT

```
7819:Ooasamor.  (£.)  M.  E.  gossottur,  gwtt- JOiner,  lit  'gooif •summer,'  The  prov.  E. name  (in  Craven)  is  summer-goese.  Named from  the  downy  api^atance  of  the  film. Also  called  summer-€olt  (Whitby);  also tummtr-gauu  tcorruptly).  Cf.  C.  torn- mtrJaJtn  (lit  snmmer-thrcadi),  ]^ossamer ; Pu.  tomtrtit alien,  Swed.  scmmeriraJ,  the sanie  But  in  G.  it  is  also  called  miuUhfn- sffmrnrr,  lit  Maiden  -  summer,  der  atu Weihtr  spmmer^  the  old  women's  sunmier. It  would  appear  that  summer  is  here  used in  the  sense  of  'summer  film/  so  that gossamer  —  goose -summer -film.  (Better sftclt  ffossomtr  or  gosiummtr).
10928:mietreea.  a  lady  of  a  household.  (F.  • L.^     0.  F,  maistresse.  '  a  raiatress,  dame  ; ' Cot.  {F.mai/resse.)   Fcta.  of  O.V.maistre, a  master  ;  mtc  niaater  (above). AlagnoUa.    (K.)      A  genua  of  plants named  after  Pierre  jI/e^^w/,  of  MootpcUier, in  i- ranee;  died  a.i..  1715. Magpie,  a  bini.  (F.-L.-Gk. ;  a«</ F. —  L . )     A  Uo  ca  1 1  ed  Bnagpt-pU,  ^i^gg^^y  -/". Mag  is  short  for  Magoi  -  F.  Afargof,  a familiar  form  of  F.  Margverite,  alsu  used to   denote  a  magpie.      This  ii  from   L. Margarita^    fik.  fuxfrfapirrftf   a   pearl ;  cC Pers.    muruftirii/.  a   fiearl.     /W  ■»  F.  /i>, from  L.  fica,  a  magpie ;  see  Pie  (x). Mahogany,  a  trc«.   (W.  Indian.)    The native  S.  American  name  (Webster). Mahometan ;  see  Mohammedao. Maid.  Maiden:  see  May  {,i). Mail  (I),  »tccl  network;  sec  Maculate. Mail    (3),  a   letter-bag.    (F.-U.  H.  G.) M.  E.  mo/f.  — O.  F*.  ma/e  {¥.  ma/Ze),  a  bag. wallet  —  O.  H.  G.    malaho,    a    leatheni wallet. +Gae].  and  Iri:>h  jwo/a,  a  bag:  Gk. /i«A7'.'F,  hide,  skin.
11276:nmd,  maiden.  (E)  M.  E.  mayde, merely  short  for  earlier  maidtn,  meidm. A.  S.  magdtH,  a  maiden :  short  lor  mageS- *H  *.  dimin.  form  of  magtf^f  a  maiden. Again,  mag-iZ  is  allied  to  magUt  a  son,  a kinsman,  and  to  m^,  mdgr,  a  maiden (aniwering  to  later  M.  E.  may).  Ma;^ atiswers  to  Goth.  ma^tJij,  a  virgin,  maid, and  ny^ffu,  a  son  or  kinsman,  to  Goth. magtiSf  Icel.  m&gr,  a  boy.  orig.  *a  growing lad,'  one  inci easing  in  strength.  From Teut.  basL*  MAG,  to  have  strength.  Par. maiden-hocdt  al&o  spelt  maidtn-fitad.
=== FSD maiden ===
FSD_vol3.txt:2001:Mad'den, 1 mad'en; 2 mkd'On, HIr FrodBrlc (>/iilR0l->/i

-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-07T15:58:51.329Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK; ls -la | grep 319; python3 -c \"\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt',encoding='utf8',errors='replace').read().split(chr(10))\nprint('leaf for 11276:', chr(10).join(t[:11276]).count(chr(12)))\"",
 "description": "Confirm PNG copied and Skeat leaf"
}
```


### [2026-09-07T15:58:52.721Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  67293 Sep  7 11:58 319.png
leaf for 11276: 300
```


## [2026-09-07T16:00:21.754Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 -c \"\nt=open('AHD_watkins1985.txt',encoding='utf8',errors='replace').read().split(chr(10))\nfor ln in (710,711,713):\n    leaf=chr(10).join(t[:ln]).count(chr(12)); print(ln,'leaf',leaf,'printed',leaf-29)\"; echo \"=== KNT 810-820 ===\"; sed -n '810,818p' KNT.txt; echo \"=== KNT hamarana ===\"; grep -n \"hamarana\\|hamaranam\" KNT.txt | head -3",
 "description": "AHD page numbers and Kent check"
}
```


### [2026-09-07T16:00:23.136Z] TOOL RESULT

```
710 leaf 68 printed 39
711 leaf 68 printed 39
713 leaf 68 printed 39
=== KNT 810-820 ===
Saylam? = $üyalüm A*Pa 4, for уат = убит.
ak"un*am* = akunüm XSc 3 and А?На 5f (only
ām visible), Аа 4 and 5 (restored); ak*unta = akund А?На 7; ak*v°n sas = akuvanasasa A’Sde 3 (and ak"un*wam* = akunavim A*Sdb 3, See $53); all for ak"un*wm* = akunavam.
akun% = akunas A’Sa 3f, D'Sbb 3, for ak*un*us = акиташ, II. The word is itself problematic or obscure:
оа DB 4.89, as read by KT; see now Cameron’s reading.
атта DB 4.92, as read by KT; perhaps hamazmaiā (JAOS 62.269).
afuray'a DNb 38, perhaps for arwàyàá (JNES 4,44, 52).
l^al"ugr? : symm = uncertain words.
Jud : тфу фат? = jvadiy : paradayadém A’Sd 3; uncertain words.
=== KNT hamarana ===
587:tarsatiy with Iran. tars- because of NPers. (0708, $ despite Av. drasaiti, from is-, both with IE Ж suffix -ske-; but Skt. trásati from "ireseti. 1 cartanaty: the c shows that a front vowel formerly 3 stood immediately after it; therefore car- from Ж *cer- from *ker-. 4 Karka, Gk. Каре, Kapuol; Elam. kur-ga-ap seems ' to have no evidential value. E | valrtaiyaty, if identical with Skt. variaye; see $ Lex. s.v. vart- for reff. ; | $32. Отр Persian ara seems to be established * in the following: E i By cognates in Skt. and Avestan: apataram, $ aparam, para, hamarana-, partaram, and the * verbal nouns -kara- and -bara- as second ele- ments of compounds. | $ By Elamite and other transcriptions: Arakadri $ (or Ark- ?), Arabäya, the final of Nabukudra- ° cara.
1694:Skt. sam-aranam, OP hamaranam; but with pre- fix, ufhamaranakara, with double writing of the initial, $ being the value after u, and A being the value when initial in the separate word. Perhaps also OP PatiSuvart§ for Рай- Swart, see Lex. s.v. Cf. Reichelt, Aw. Elmb. $103, for the same phenomenon in Avestan.
1894:hamarana-kara- ‘battle-making’; züra-kara- ‘evil- doing’; ddraniya-kara- 'gold-working'; ciyd- kara- ‘doing how much’, ava-kara- ‘doing that’.
```


## [2026-09-07T16:00:38.685Z] AGENT

Now I'll write the verification file.


## [2026-09-07T16:04:14.087Z] TOOL CALL #55: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk319a.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_MARC   = \"https://en.wiktionary.org/wiki/marcasite\"\nW_ARMARQ = \"https://en.wiktionary.org/wiki/%D9%85%D8%B1%D9%82%D8%B4%D9%8A%D8%AA%D8%A7\"\nE_AMAZ   = \"https://www.etymonline.com/word/Amazon\"\nW_AMAZ   = \"https://en.wiktionary.org/wiki/%E1%BC%88%CE%BC%CE%B1%CE%B6%CF%8E%CE%BD\"\nW_MAGATH = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/maga%C3%BEs\"\nA_MARQ   = \"https://abadis.ir/fatofa/%D9%85%D8%B1%D9%82%D8%B4%DB%8C%D8%B4%D8%A7/\"\nV_AMAZ   = \"https://vajehyab.com/?q=%D8%A2%D9%85%D8%A7%D8%B2%D9%86\"\n\nPOK697 = (\"POK_full.txt (English tr. of IEW) line 57287 ff.: 'Root/lemma: magh- Meaning: to fight. \"\n          \"Material: Gr. Ἀμαζών, loanword through Aeolic mediation from an Iran. people's name *ha-mazan- \\\"warrior\\\", \"\n          \"compare ἁμαζακάραν (: Aryan kar- \\\"make\\\") πολεμεῖν. Πέρσαι Hes. and ἁμαζανίδες …; gr. μάχομαι \\\"fight\\\", \"\n          \"μάχη \\\"fight, struggle, battle\\\", μάχαιρα \\\"sword, knife\\\" … Or Semitic loanword, to hebr. mekherah \\\"sword\\\"? \"\n          \"References: WP. II 227, WH. II 3, 4. Page(s): 697'.\")\nWLD227 = (\"WLD_Bd2_pages.txt leaf 232 (= printed p. 227, bottom): 'magh- \\\"kämpfen\\\". Gr. [Ἀμαζών] Lw. aus einem iran. \"\n          \"Volksnamen *ha-mazan- \\\"Krieger\\\", vgl. ἁμαζακαράν (: ar. kar- \\\"machen\\\") πολεμεῖν, Πέρσαι Hes.: gr. μάχομαι \"\n          \"\\\"kämpfe\\\", μάχη \\\"Kampf, Schlacht\\\", μάχαιρα \\\"Schwert, Messer\\\". Lagercrantz Xenia Lideniana (1912) 270 ff.'\")\nAHD_MAGH2 = (\"AHD_watkins1985.txt line 711-712 (leaf 68 = printed p. 39): 'magh-². To fight. Hypothetical Old Iranian \"\n             \"*ha-maz-an-, \\\"warrior\\\" (*ha-, with < *sm-; see sem-¹), possibly borrowed into Greek as Amazōn, Amazon: \"\n             \"AMAZON. [Pok. magh- 697.]'\")\nKLN59 = (\"KLN_1966.txt leaf 43 (= printed p. 59, entries amaroid…ambrosia) : 'Amazon, n., a member of a race of female \"\n         \"warriors in Scythia (Greek mythol.) — L., fr. Gk. Ἀμαζών, which prob. derives fr. Heb. ammāṣ, \\\"strong\\\". The form \"\n         \"of the word Ἀμαζών was prob. influenced by the folk etymology according to which Ἀμαζών lit. means \\\"without \"\n         \"breast\\\", fr. a- … and μαζός \\\"breast\\\"'; and 'Amazon, n., name of the largest river in the world in volume — Sp. \"\n         \"Amazonas, from prec. word; so called by Francisco Orellana after his battle with the Tapuyas (in 1541), in allusion \"\n         \"to the circumstance that the women of the tribe helped the men in their fight.'\")\n\nd = {\n \"pdf_page\": 319,\n \"book_page\": 289,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-07\",\n \"entries\": []\n}\n\n# ---------------------------------------------------------------- entry 0\ne0 = {\n \"entry\": 0,\n \"root\": \"Magh 2\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *magh- 'to fight' (Pokorny 697 magh-; Watkins/AHD magh-², kept apart from magh-¹ 'to be able, have power', Pokorny 695)\",\n \"note\": (\"The root box is right in substance and in its reference. Pokorny p. 697 does have a lemma magh- 'to fight', quite \"\n          \"separate from magh- 'können, vermögen' on p. 695, and Nourai's numbering 'Magh 2' mirrors Watkins' magh-¹ / magh-² \"\n          \"split exactly (AHD 1985 p. 39). The whole of Nourai's chart is in fact Pokorny's article: the Greek loan Ἀμαζών from \"\n          \"an Iranian people-name *ha-mazan- 'warrior' (a proposal of Lagercrantz, Xenia Lideniana 1912, 270 ff., taken over by \"\n          \"Walde-Pokorny II 227 and by Watkins). Two caveats the chart does not report: (a) the evidential base of the root is \"\n          \"thin — apart from the Amazon loan it rests on Greek μάχομαι 'I fight', μάχη 'battle', μάχαιρα 'knife, sword', and \"\n          \"Pokorny himself ends the article with an alternative 'Or Semitic loanword, to hebr. mekherah \\\"sword\\\"?'; Mann (IEC \"\n          \"16376) sets the Greek family up with s-mobile as *smaghos 'toil, turmoil' instead; (b) Nourai's chart makes the \"\n          \"Iranian word look attested, which it is not (see node #1).\"),\n \"note_fa\": (\"ریشهٔ «Magh 2» در جای خود درست است: پوکورنی در ص ۶۹۷ فرهنگ خود مدخل جداگانه‌ای با معنی «جنگیدن» دارد که از مدخل \"\n             \"magh- «توانستن» (ص ۶۹۵) متمایز است، و شمارهٔ ۲ در عنوان نورایی همان تفکیک magh-¹/magh-² در پیوست واتکینز (ص ۳۹ \"\n             \"چاپ ۱۹۸۵) است. سراسر این نمودار برگرفته از همان مقالهٔ پوکورنی است: وام‌گیری یونانی Ἀμαζών از نام قومی ایرانی \"\n             \"*ha-mazan- «جنگاور»، فرضیه‌ای که لاگرکرانتس (۱۹۱۲) پیش نهاد و والده-پوکورنی (ج ۲ ص ۲۲۷) و واتکینز پذیرفتند. دو \"\n             \"نکته را نمودار نمی‌گوید: نخست آنکه پایهٔ این ریشه سست است و جز همین وام‌واژه تنها بر μάχομαι و μάχη و μάχαιρα \"\n             \"یونانی استوار است و خود پوکورنی در پایان مقاله احتمال وام‌بودن آن از سامی (عبری mekherah «شمشیر») را هم می‌آورد؛ \"\n             \"دوم آنکه صورت ایرانی *ha-mazan- بازسازی‌شده است و در هیچ متن اوستایی یا پارسی باستان گواهی نشده (بنگرید به گرهٔ ۱).\"),\n \"sources\": [E_AMAZ, W_AMAZ],\n \"ref_check\": [{\"ref\": \"POK:697\", \"status\": \"supports\", \"note\": POK697}],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II p. 227 s.v. 'magh- kämpfen'\", \"stance\": \"supports\", \"note\": WLD227},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 p. 39 s.v. 'magh-²'\", \"stance\": \"supports\", \"note\": AHD_MAGH2},\n   {\"src\": \"IEC\", \"where\": \"Mann, col. at line 16376 s.v. 'smaghos'\", \"stance\": \"partial\",\n    \"note\": (\"IEC.txt line 16376: 'smaghos, ā \\\"toil, turmoil\\\". … Gk. mákhe, f. \\\"battle\\\" (a type *mnghā: *mongh-… seems \"\n             \"improbable); cf. mákhlos, adj. \\\"fierce; lewd\\\"' — Mann puts the Greek words under an s-mobile root *smaghos and \"\n             \"does not mention Amazon at all, i.e. a compatible but not identical reconstruction.\")}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan / Old Persian\", \"words\": \"ha-mazan\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"*ha-mazan- 'warrior, fighting together' is a RECONSTRUCTED Old Iranian compound, not an attested Avestan or Old \"\n   \"Persian word: *ha- 'together, one' (< PIE *sm̥-, whence Av. ha-, hama-; Nourai's cross-reference '☞So' points to his root for \"\n   \"PIE *sem-) + *mazan- from *magh- 'fight'. All of the evidence is indirect: Hesychius' glosses ἁμαζακάραν· πολεμεῖν, Πέρσαι \"\n   \"('*hamaza-kara-', literally 'battle-making', with Iranian kar- 'to make') and ἁμαζανίδες, plus the ethnic name Hamazan-. \"\n   \"Bartholomae's Altiranisches Wörterbuch has no hamazan- at all, and Kent's Old Persian lexicon has none either — the attested \"\n   \"OP word for 'battle' is hamarana- (= Skt. sam-araṇam), with the compound hamarana-kara- 'battle-making' that is the exact \"\n   \"formal parallel to Hesychius' ἁμαζακάραν. So the arrow root→node is sound as a hypothesis (Lagercrantz 1912; Walde-Pokorny II \"\n   \"227; Pokorny 697; Watkins expressly labels the form 'Hypothetical Old Iranian'), but the language label 'Avestan / Old \"\n   \"Persian' overstates it, and Wiktionary's alternative parse hama-zan- 'striking together' (to Av. jan-/zan- 'to strike', PIE \"\n   \"*gʷhen-) would remove the word from *magh- altogether.\"),\n \"derivation_fa\": (\"صورت *ha-mazan- «جنگاور، هم‌رزم» یک بازسازی از ایرانی باستان است و نه واژه‌ای گواهی‌شده در اوستایی یا پارسی \"\n   \"باستان: از پیشوند *ha- «باهم، یک» (از هندواروپایی *sm̥-، همان ha-/hama- اوستایی؛ ارجاع «So» در نمودار به ریشهٔ *sem- است) و \"\n   \"*mazan- از ریشهٔ *magh- «جنگیدن». همهٔ گواه‌ها غیرمستقیم‌اند: واژه‌نامهٔ هزیخیوس با دو مدخل ἁμαζακάραν «جنگیدن، [نزد] پارسیان» \"\n   \"(یعنی *hamaza-kara- «نبردسازنده» با kar- ایرانی) و ἁμαζανίδες، و نیز نام قومی Hamazan-. در «فرهنگ ایرانی باستان» بارتولومه \"\n   \"هیچ مدخل hamazan- نیست و در واژه‌نامهٔ پارسی باستان کنت نیز نیامده؛ واژهٔ گواهی‌شدهٔ پارسی باستان برای «نبرد» hamarana- است با \"\n   \"ترکیب hamarana-kara- که همتای دقیقِ صورتِ هزیخیوس است. پس پیوند ریشه با این گره به عنوان فرضیه پذیرفتنی است (لاگرکرانتس ۱۹۱۲، \"\n   \"والده-پوکورنی، پوکورنی، واتکینز که آن را صریحاً «ایرانی باستانِ فرضی» می‌نامد)، اما برچسب «اوستایی/پارسی باستان» گزافه است؛ \"\n   \"افزون بر این تجزیهٔ دیگری (hama-zan- «هم‌زنان، باهم‌کوبنده» از ریشهٔ zan-/jan- «زدن») این واژه را به‌کلی از ریشهٔ *magh- بیرون می‌برد.\"),\n \"sources\": [W_AMAZ, E_AMAZ],\n \"ref_check\": [\n   {\"ref\": \"POK:697\", \"status\": \"supports\", \"note\": POK697},\n   {\"ref\": \"AHD:1541\", \"status\": \"supports\", \"note\": (\"The 1976 AHD appendix page is not open online, but the same root article is \"\n     \"AHD_watkins1985.txt line 711 (printed p. 39): 'magh-². To fight. Hypothetical Old Iranian *ha-maz-an-, \\\"warrior\\\" (*ha-, \"\n     \"with < *sm-; see sem-¹), possibly borrowed into Greek as Amazōn' — word, gloss and morphological analysis exactly as in the \"\n     \"chart, but explicitly hypothetical.\")}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW — searched the whole text for hamaz-/ha-maz-\", \"stance\": \"silent\",\n    \"note\": \"grep -n 'hamaz\\\\|ha-maz\\\\|hamazan' BRT.txt returns nothing: the Altiranisches Wörterbuch has no such Avestan entry.\"},\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon and §32/§53 notes\", \"stance\": \"contradicts\",\n    \"note\": (\"KNT.txt line 815 lists 'amma DB 4.92, as read by KT; perhaps hamazmaiā (JAOS 62.269)' among 'words that are \"\n             \"problematic or obscure' — the only OP form remotely like it, and a conjecture. The real OP items are 'hamaranam' \"\n             \"(line 1694: 'Skt. sam-aranam, OP hamaranam; but with prefix, uθhamaranakara') and 'hamarana-kara- \\\"battle-making\\\"' \"\n             \"(line 1894). Kent knows no OP *hamazan-.\")},\n   {\"src\": \"WLD\", \"where\": \"Bd. II p. 227\", \"stance\": \"supports\", \"note\": WLD227}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Greek\", \"words\": \"amazon\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"The Greek word is Ἀμαζών, pl. Ἀμαζόνες, already in Homer (Il. 3.189, 6.186) as the name of a mythical people of \"\n   \"female warriors placed in Scythia/Pontus. Pokorny 697 and Walde-Pokorny II 227 take it as a loan 'through Aeolic mediation' \"\n   \"from Iranian *ha-mazan-, the loss of the initial h- being unproblematic since Ionic-Aeolic dropped the aspirate early \"\n   \"(psilosis) — that is exactly the arrow drawn here, and Wiktionary still gives the Iranian derivation as the leading \"\n   \"hypothesis. It is not, however, a certainty: Etymonline calls the word 'probably from an unknown non-Indo-European word, or \"\n   \"possibly from an Iranian compound *ha-maz-an- \\\"(one) fighting together\\\"', and Wiktionary adds that 'numerous other \"\n   \"etymologies have been proposed, generally tracing the word back to Iranian, Greek or (West/East) Caucasian languages', \"\n   \"including a native Greek *n̥-mn̥gʷ-yō 'manless one' (rejected by Frisk). On the chart's own NOTE — 'KLN:59 derives this from \"\n   \"Hebrew' — Klein's Hebrew ʾammāṣ 'strong' is not accepted by any current source; interestingly Pokorny's own article ends with \"\n   \"a different Semitic guess ('to hebr. mekherah \\\"sword\\\"?'), so a Semitic origin is an old minority line, not Klein's invention. \"\n   \"The a-privative + μαζός 'breast' story ('breastless') is a Greek folk etymology, as Webster and Klein both already say.\"),\n \"derivation_fa\": (\"واژهٔ یونانی Ἀμαζών (جمع Ἀμαζόνες) از هومر (ایلیاد ۳٫۱۸۹ و ۶٫۱۸۶) به‌جا مانده و نام قومی افسانه‌ای از زنان \"\n   \"جنگاور در سکاییه/پونتوس است. پوکورنی (ص ۶۹۷) و والده-پوکورنی (ج ۲ ص ۲۲۷) آن را وام‌واژه‌ای «با میانجی گویش آیولی» از ایرانی \"\n   \"*ha-mazan- می‌دانند؛ افتادن هـ آغازین دشواری ندارد، زیرا در گویش‌های یونی-آیولی «دم‌آغازین» (h) زود از میان رفت. همین است \"\n   \"پیکانی که نورایی کشیده و ویکی‌واژه نیز آن را فرضیهٔ اصلی می‌شمارد. با این همه قطعی نیست: اتیمانلاین می‌نویسد «احتمالاً از \"\n   \"واژه‌ای ناشناخته و غیرهندواروپایی، یا شاید از ترکیبی ایرانی»، و ویکی‌واژه از فرضیه‌های قفقازی و یونانی نیز یاد می‌کند. دربارهٔ \"\n   \"یادداشت خود نمودار (کلاین آن را از عبری می‌گیرد): ریشه‌گیری کلاین از عبری ʾammāṣ «توانا» امروز پذیرفته نیست، هرچند خود پوکورنی \"\n   \"هم حدس سامی دیگری (عبری mekherah «شمشیر») را در پایان مقاله آورده است. داستان «بی‌پستان» (ἀ- + μαζός) نیز ریشه‌شناسی عامیانهٔ \"\n   \"یونانی است، چنان‌که وبستر و کلاین هر دو تصریح کرده‌اند.\"),\n \"sources\": [W_AMAZ, E_AMAZ],\n \"ref_check\": [\n   {\"ref\": \"AHD:40,1541\", \"status\": \"supports\", \"note\": (\"AHD_watkins1985.txt line 711-712 (p. 39) 'possibly borrowed into Greek as \"\n     \"Amazōn, Amazon: AMAZON'; the index line 1235 confirms the dictionary entry AMAZON is keyed to 'magh-2'. AHD:40 is the \"\n     \"dictionary entry 'Amazon' in the 1976 New College edition, which is lending-only.\")},\n   {\"ref\": \"PRT:14\", \"status\": \"not_checked\", \"note\": \"Partridge, Origins, p. 14 — no open copy; archive.org holds only lending copies (originsshortetym00part).\"},\n   {\"ref\": \"KLN:59\", \"status\": \"supports\", \"note\": KLN59 + \" — i.e. the chart's NOTE reports Klein correctly.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"leaf 43 (= p. 59) s.v. 'Amazon'\", \"stance\": \"contradicts\", \"note\": KLN59},\n   {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt line 6335 s.v. 'Am'a-zōn'\", \"stance\": \"partial\",\n    \"note\": (\"Webster: 'Am/a-zōn, n. [L., from Gr. Amazōn; a priv., and mazos, breast. Derived by Greek folk etym. from the legend \"\n             \"that the Amazons cut off the right breast to facilitate the use of the bow and javelin.]' — records the Greek chain \"\n             \"L. < Gk. but attributes the a-privative analysis to folk etymology and says nothing of Iranian.\")},\n   {\"src\": \"POK\", \"where\": \"p. 697\", \"stance\": \"supports\", \"note\": POK697}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Latin\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Empty pass-through box (verified on the printed page: the box carries only the label 'Latin'). The implied form is \"\n   \"Latin Amāzōn, pl. Amāzones, a straight learned borrowing of Greek Ἀμαζών already in the Augustan poets (Virgil, Aen. 1.490 \"\n   \"'Amazonidum'; Propertius), with the regular Greek→Latin substitution of -ō- for -ω- and third-declension inflection. Klein \"\n   \"(p. 59) gives the same link: English Amazon '— L., fr. Gk. Ἀμαζών'.\"),\n \"derivation_fa\": (\"خانهٔ خالی و گذرگاهی است (بر صفحهٔ چاپی نیز جز برچسب «لاتینی» چیزی در آن نیست). صورت مورد نظر Amāzōn لاتینی است \"\n   \"(جمع Amāzones) که وام‌گیری فرهیختهٔ Ἀμαζών یونانی است و از دورهٔ آوگوستوس در شعر لاتینی دیده می‌شود (ویرژیل، انئید ۱٫۴۹۰). \"\n   \"دگرگونی آوایی چیزی جز جانشینی ō لاتینی به‌جای ω یونانی و رفتن به صرف سوم نیست. کلاین (ص ۵۹) همین حلقه را می‌آورد.\"),\n \"sources\": [E_AMAZ],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The box carries no reference in the book; the Latin link is covered by KLN:59 on the neighbouring nodes.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"leaf 43 (= p. 59) s.v. 'Amazon'\", \"stance\": \"supports\", \"note\": \"'Amazon, n., … — L., fr. Gk. Ἀμαζών' — Latin as the intermediary between Greek and the modern languages.\"},\n   {\"src\": \"FSD\", \"where\": \"FSD_vol1.txt line 13427 s.v. 'Amazon'\", \"stance\": \"supports\", \"note\": \"Funk & Wagnalls gives the etymology bracket '[L., < Gr. Amazon.]' for Amazon.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 4, \"lang\": \"French\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Empty pass-through box (the printed page shows only the label 'French'). The implied form is French Amazone, a \"\n   \"learned Latinism first in Old/Middle French in the 14th c. (Latin Amāzōn(em) > Amazone with the usual French treatment of the \"\n   \"learned accusative in -onem > -one). It is this French word that the modern Persian and, in part, the English forms rest on; \"\n   \"Etymonline dates English Amazon to the late 14th c. 'from Old French or Latin'.\"),\n \"derivation_fa\": (\"خانهٔ خالی و گذرگاهی است (بر صفحهٔ چاپی تنها برچسب «فرانسوی» دیده می‌شود). صورت مورد نظر Amazone فرانسوی است، \"\n   \"وام‌واژه‌ای فرهیخته از لاتینی که از سدهٔ چهاردهم در فرانسوی میانه دیده می‌شود (از حالت مفعولی Amāzōnem با تحول عادی -onem > \"\n   \"-one در وام‌واژه‌های فرهیخته). همین صورت فرانسوی است که آمازن فارسی و تا حدی صورت انگلیسی بر آن استوارند؛ اتیمانلاین ورود \"\n   \"Amazon به انگلیسی را اواخر سدهٔ چهاردهم «از فرانسوی کهن یا لاتینی» می‌داند.\"),\n \"sources\": [E_AMAZ],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference in the book for this box.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"leaf 43 (= p. 59)\", \"stance\": \"silent\", \"note\": \"Klein routes English Amazon straight from Latin and does not mention a French stage.\"},\n   {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt line 6335\", \"stance\": \"silent\", \"note\": \"Webster likewise gives only '[L., from Gr. Amazōn]'.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 5, \"lang\": \"Persian\", \"words\": \"âmâzon «آمازن ۱»\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"Persian آمازن âmâzon in the sense 'female warrior (of the Greek myth)' is a modern European loan, taken — as the \"\n   \"chart says — through French Amazone in the 19th-20th c. (the vowel of the second syllable, -on, is French rather than Latin \"\n   \"-ōn or English -on with schwa), and it belongs to the encyclopaedic vocabulary rather than the inherited lexicon. Its presence \"\n   \"is confirmed for the river sense by Dehkhodā ('آمازن. [زُ] (اِخ) نام رودی بزرگ در آمریکای جنوبی'), and Nourai cites Moʿin's \"\n   \"volume of proper names (MON5:58) for both senses; the entry text of the aʿlām volumes cannot be page-checked online, so the \"\n   \"page number stays unverified. Note that the commoner Persian spelling today is آمازون; آمازن is the older, French-based \"\n   \"transcription that Dehkhodā and Moʿin use.\"),\n \"derivation_fa\": (\"«آمازن» به معنی «زنِ جنگاورِ اسطوره‌های یونانی» وام‌واژه‌ای اروپایی و نو است و — چنان‌که نمودار می‌گوید — از \"\n   \"راه Amazone فرانسوی در سدهٔ سیزدهم/چهاردهم هجری وارد فارسی شده (واکهٔ هجای دوم، -ون/-ن، فرانسوی است نه لاتینی ō و نه انگلیسی). \"\n   \"این واژه از دایرهٔ واژگان دانشنامه‌ای است، نه از میراث زبانی. وجود آن در معنی رودخانه با مدخل دهخدا تأیید می‌شود: «آمازن. \"\n   \"[زُ] (اِخ) نام رودی بزرگ در آمریکای جنوبی»؛ نورایی برای هر دو معنی به جلد اعلام فرهنگ معین (ص ۵۸) ارجاع داده که متن آن \"\n   \"به‌صورت صفحه‌شمار در دسترس برنامی‌نه نیست، پس شمارهٔ صفحه بی‌گواه می‌ماند. امروز نگارش رایج‌تر «آمازون» است و «آمازن» صورت \"\n   \"کهن‌ترِ برگرفته از فرانسوی است.\"),\n \"sources\": [V_AMAZ],\n \"ref_check\": [{\"ref\": \"MON5:58\", \"status\": \"not_checked\",\n   \"note\": (\"Moʿin vol. 5 (aʿlām) is not on archive.org and vajehyab/abadis do not expose the aʿlām volumes with page numbers \"\n            \"(refs_online.json: 'Page numbers cannot be mapped online'). The word itself is confirmed in Dehkhodā via vajehyab \"\n            \"(archived): 'آمازن . [ زُ] (اِخ ) نام رودی بزرگ در آمریکای جنوبی'.\")}],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"vajehyab.com/?q=آمازن (Dehkhodā entry shown; Moʿin lexicon volumes have no آمازن)\", \"stance\": \"partial\",\n    \"note\": \"Only the river sense is quoted there: 'آمازن . [ زُ] (اِخ ) نام رودی بزرگ در آمریکای جنوبی ، و آن بزرگترین ِ رودهای جهان است'; the 'female warrior' sense is not in the searchable text.\"},\n   {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_pages.txt, grep 'آمازن'\", \"stance\": \"silent\", \"note\": \"Aryanpur's etymological dictionary has no آمازن (it treats inherited Persian vocabulary).\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 6, \"lang\": \"English\", \"words\": \"Amazon 1\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"English Amazon 'one of a mythical race of female warriors; a warlike woman' is attested from the late 14th c. \"\n   \"(Chaucer's Amazones), taken from Old French Amazone / Latin Amāzōn — so the arrow from the Latin box is right, though most \"\n   \"dictionaries route it through French as well. Etymonline: 'late 14c., from Old French or Latin, from Greek Amazon'. AHD keys \"\n   \"the entry AMAZON to the root magh-², exactly as the chart does.\"),\n \"derivation_fa\": (\"واژهٔ انگلیسی Amazon «زنِ جنگاورِ اسطوره‌ای؛ زن جنگاور» از اواخر سدهٔ چهاردهم میلادی گواهی شده (در چاسر \"\n   \"Amazones) و از Amazone فرانسوی کهن یا Amāzōn لاتینی گرفته شده است؛ پس پیکانِ نمودار از خانهٔ لاتینی درست است، هرچند بیشتر \"\n   \"فرهنگ‌ها میانجی فرانسوی را هم می‌آورند. پیوست واتکینز نیز مدخل AMAZON را زیر همان ریشهٔ magh-² می‌آورد، درست همان‌گونه که \"\n   \"نمودار نشان می‌دهد.\"),\n \"sources\": [E_AMAZ],\n \"ref_check\": [{\"ref\": \"AHD:40,1541\", \"status\": \"supports\",\n   \"note\": \"AHD_watkins1985.txt line 1235 (index): 'AMAZON magh-2', and line 711-712 gives the root article with ': AMAZON' as its English outcome.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"leaf 43 (= p. 59)\", \"stance\": \"supports\", \"note\": \"'Amazon, n., a member of a race of female warriors in Scythia (Greek mythol.) — L., fr. Gk. Ἀμαζών' (his quarrel is only with the ultimate source, not with the L. > E. route).\"},\n   {\"src\": \"FSD\", \"where\": \"FSD_vol1.txt lines 13423-13428\", \"stance\": \"supports\", \"note\": \"Funk & Wagnalls s.v. amazon '[L., < Gr. Amazon.]', with the sense 'gallant viragoes' and the derived senses (Amazon ant, Amazon stone).\"},\n   {\"src\": \"SKT\", \"where\": \"SKT.txt, grep 'Amazon'\", \"stance\": \"silent\", \"note\": \"Skeat's Concise dictionary has no entry Amazon.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 7, \"lang\": \"Spanish\", \"words\": \"Amazonas\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"Spanish (el) Amazonas is the plural of Amazona, the Spanish reflex of Latin Amāzōn; the arrow is drawn from the \"\n   \"Greek box but the borrowing is of course learned and Latin-mediated. The naming story the chart gives is Klein's, and it is \"\n   \"right in outline: the river was rechristened by Francisco de Orellana in 1541-42 (Klein: 'so called by Francisco Orellana \"\n   \"after his battle with the Tapuyas (in 1541), in allusion to the circumstance that the women of the tribe helped the men in \"\n   \"their fight'). It is called 'plausible' rather than 'confirmed' only because a competing account exists: Etymonline notes \"\n   \"that 'some scholars propose instead that the river name is a corruption of a native word in Tupi or Guarani meaning \\\"wave\\\"', \"\n   \"in which case the Greek word merely reshaped an indigenous name.\"),\n \"derivation_fa\": (\"«Amazonas» اسپانیایی جمعِ Amazona است، یعنی بازتاب فرهیختهٔ Amāzōn لاتینی؛ پیکان در نمودار از خانهٔ یونانی \"\n   \"کشیده شده، اما وام‌گیری در واقع فرهیخته و با میانجی لاتینی است. داستان نام‌گذاری که نمودار می‌آورد از کلاین است و در کل درست \"\n   \"است: فرانسیسکو د اورلیانا در ۱۵۴۱–۱۵۴۲ م. رود را چنین نامید، پس از نبردی که در آن زنان قبیله به یاری مردان می‌جنگیدند. تنها \"\n   \"از این رو «با احتیاط پذیرفتنی» است که روایت رقیبی هم وجود دارد: اتیمانلاین یادآور می‌شود که برخی نام رود را تحریفِ واژه‌ای \"\n   \"بومی از توپی یا گوارانی به معنی «موج» می‌دانند، که در آن صورت واژهٔ یونانی تنها نامی بومی را بازشکل داده است.\"),\n \"sources\": [E_AMAZ],\n \"ref_check\": [{\"ref\": \"KLN:59\", \"status\": \"supports\", \"note\": KLN59}],\n \"consulted\": [\n   {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt lines 6344-6345\", \"stance\": \"partial\",\n    \"note\": \"Webster has 'Amazonian … 2. belonging to the River Amazon in South America' and 'Am/a:zōn stone … found on the banks of the Amazon River', i.e. the river name is treated as the same word, without the naming anecdote.\"},\n   {\"src\": \"FSD\", \"where\": \"FSD_vol1.txt line 13429\", \"stance\": \"supports\", \"note\": \"'Am'a-zon*, n. A river flowing across northern South America from the Andes to the Atlantic' listed under the same headword group as the mythological Amazon.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 8, \"lang\": \"French\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Empty pass-through box (printed page: label 'French' only). The implied form is French Amazone as the name of the \"\n   \"river ('le fleuve Amazone', from Spanish Amazonas), the shape in which the geographical name reached 19th-c. Persian usage; \"\n   \"French geography books of the Qajar period are the vector for the Persian form in node #9.\"),\n \"derivation_fa\": (\"خانهٔ خالی و گذرگاهی است (بر صفحهٔ چاپی تنها برچسب «فرانسوی»). صورت مورد نظر Amazone فرانسوی در معنی نام رود \"\n   \"است («le fleuve Amazone»، از Amazonas اسپانیایی)، همان صورتی که نام جغرافیایی از راه آن به فارسی سدهٔ سیزدهم هجری رسید؛ \"\n   \"کتاب‌های جغرافیای فرانسوی دورهٔ قاجار حاملِ صورت فارسی گرهٔ ۹ بوده‌اند.\"),\n \"sources\": [V_AMAZ],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference in the book for this box.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"leaf 43 (= p. 59) s.v. 'Amazon' (river)\", \"stance\": \"partial\", \"note\": \"Klein takes English Amazon (river) straight from Spanish Amazonas, with no French stage.\"},\n   {\"src\": \"MON\", \"where\": \"vajehyab.com/?q=آمازن\", \"stance\": \"supports\", \"note\": \"The Persian form آمازن with final -n reflects French Amazone rather than Spanish Amazonas or English Amazon.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 9, \"lang\": \"Persian\", \"words\": \"âmâzon «آمازن ۲»\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Persian آمازن as a river name is attested in Dehkhodā, quoted verbatim from the archived vajehyab page: 'آمازن . \"\n   \"[ زُ] (اِخ ) نام رودی بزرگ در آمریکای جنوبی ، و آن بزرگترین ِ رودهای جهان است' ('proper name: the name of a great river in \"\n   \"South America, the greatest of the world's rivers'), with the vowel marked zu — âmâzon. It is a 19th-20th c. loan of the \"\n   \"European geographical name, mediated by French as node #8 has it, and it is a doublet of the mythological آمازن of node #5 in \"\n   \"Persian just as Amazon 1/Amazon 2 are in English.\"),\n \"derivation_fa\": (\"«آمازن» در معنی نام رود در لغت‌نامهٔ دهخدا گواهی شده است: «آمازن . [ زُ] (اِخ ) نام رودی بزرگ در آمریکای \"\n   \"جنوبی ، و آن بزرگترین ِ رودهای جهان است»؛ حرکت‌گذاری «زُ» نشان می‌دهد که تلفظ âmâzon است. این واژه وام‌گیری نامی جغرافیایی از \"\n   \"اروپا در سدهٔ سیزدهم/چهاردهم هجری است، با میانجی فرانسوی — همان‌گونه که گرهٔ ۸ نشان می‌دهد — و در فارسی دوگانهٔ «آمازن» \"\n   \"اسطوره‌ای (گرهٔ ۵) است، چنان‌که در انگلیسی Amazon 1 و Amazon 2 دوگانه‌اند.\"),\n \"sources\": [V_AMAZ],\n \"ref_check\": [{\"ref\": \"MON5:58\", \"status\": \"not_checked\",\n   \"note\": \"Moʿin's aʿlām volume is not online with pagination; the word and the gloss are however confirmed verbatim in Dehkhodā (archived vajehyab page).\"}],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"vajehyab.com/?q=آمازن\", \"stance\": \"supports\", \"note\": \"'آمازن . [ زُ] (اِخ ) نام رودی بزرگ در آمریکای جنوبی' — exactly the chart's gloss 'name of a river'.\"},\n   {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"not in Aryanpur's etymological dictionary.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 10, \"lang\": \"English\", \"words\": \"Amazon 2\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"English Amazon as the river's name is the Spanish name taken over in the 16th-17th c.: Klein, 'Amazon, n., name of \"\n   \"the largest river in the world in volume — Sp. Amazonas, from prec. word', i.e. the reference the chart gives (KLN:59) states \"\n   \"precisely this arrow. Etymonline agrees on the event ('rechristened with this name by Francisco de Orellana, 1541, after an \"\n   \"encounter with female warriors'). The derived English uses — Amazon ant, amazonite/Amazon stone, the amazon parrot — are all \"\n   \"from the river name (Funk & Wagnalls, Webster).\"),\n \"derivation_fa\": (\"Amazon انگلیسی در معنی نام رود، همان نام اسپانیایی است که در سدهٔ شانزدهم-هفدهم میلادی به انگلیسی راه یافت: \"\n   \"کلاین می‌نویسد «Amazon، نام بزرگ‌ترین رود جهان از نظر آبدهی — از Amazonas اسپانیایی، از واژهٔ پیشین»، یعنی ارجاعی که نمودار \"\n   \"می‌دهد (KLN:59) درست همین پیکان را می‌گوید. اتیمانلاین نیز در رخداد نام‌گذاری (اورلیانا، ۱۵۴۱) همراه است. کاربردهای برساخته در \"\n   \"انگلیسی — مورچهٔ آمازون، سنگ آمازون (amazonite) و طوطی آمازون — همه از نام رود گرفته شده‌اند (فانک و واگنالز، وبستر).\"),\n \"sources\": [E_AMAZ],\n \"ref_check\": [{\"ref\": \"KLN:59\", \"status\": \"supports\", \"note\": KLN59}],\n \"consulted\": [\n   {\"src\": \"FSD\", \"where\": \"FSD_vol1.txt lines 13427-13429\", \"stance\": \"supports\", \"note\": \"'am'a-zon\\\", n. 1. An American parrot … [< the river Amazon.]' and 'Am'a-zon*, n. A river flowing across northern South America' — the river name as the source of the derived English words.\"},\n   {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt lines 6344-6345\", \"stance\": \"supports\", \"note\": \"'2. belonging to the River Amazon in South America, or to the country around it'; 'Am/a:zōn stone, a bright green variety of microlite … found on the banks of the Amazon River'.\"}\n ]\n})\n\nd[\"entries\"].append(e0)\njson.dump(d, open('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/part_a.json','w',encoding='utf8'), ensure_ascii=False, indent=1)\nprint(\"entry 0 ok, nodes:\", len(e0[\"nodes\"]))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk319a.py",
 "description": "Build entry 0 of the verification"
}
```


### [2026-09-07T16:04:16.281Z] TOOL RESULT

```
entry 0 ok, nodes: 10
```


## [2026-09-07T16:09:16.304Z] TOOL CALL #56: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk319b.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_MARC   = \"https://en.wiktionary.org/wiki/marcasite\"\nW_ARMARQ = \"https://en.wiktionary.org/wiki/%D9%85%D8%B1%D9%82%D8%B4%D9%8A%D8%AA%D8%A7\"\nW_MAGATH = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/maga%C3%BEs\"\nA_MARQ   = \"https://abadis.ir/fatofa/%D9%85%D8%B1%D9%82%D8%B4%DB%8C%D8%B4%D8%A7/\"\n\nPOK696 = (\"POK_full.txt line 57146 region: 'Root/lemma: maghos, -a  Meaning: young, servant, servant of god. Material: Avestan \"\n          \"maγava- \\\"unwed, unmarried, single\\\"; alb. makth \\\"young hare\\\"; Celtic *magus … Old Irish maug, mug \\\"slave\\\" … Gothic \"\n          \"magus \\\"knave, boy\\\" … abstract noun *maghotis \\\"young femininity\\\", from which specifically \\\"girl\\\", in Gothic magaþs \"\n          \"\\\"young wife, woman\\\", Old English mæge(þ) (engl. maid), Old Saxon magath, Old High German magad, Modern High German Magd, \"\n          \"Demin. Mädchen; Latvian mazs \\\"small\\\". References: WP. II 228, Feist 339. Page(s): 696'.\")\nWLD228 = (\"WLD_Bd2_pages.txt leaf 233 (= printed p. 228): 'maghu- \\\"Knabe, Jüngling, unverheiratet\\\" und zugehörige Fem.-Bldgn. \"\n          \"Av. maγava- \\\"unverheiratet\\\" (Bartholomae Airan. Wb. 1111); kelt. *magus … got. magus \\\"Knabe\\\" … Abstraktum *maghotis \"\n          \"\\\"junge Weiblichkeit\\\", woraus konkret \\\"Mädchen\\\", in got. magaþs, ags. mægeþ (engl. maid), as. magath, ahd. magad, \"\n          \"nhd. Magd, Demin. Mädchen'. Note the lemma is spelt maghu-, which is Nourai's second root name.\")\nAHD_MAGHU = (\"AHD_watkins1985.txt line 713 (leaf 68 = printed p. 39): 'maghu-. Young person of either sex. Suffixed form \"\n             \"*magho-ti- in Germanic *magadi-, with diminutive *magadin-, in Old English mægden, virgin: MAID, MAIDEN. \"\n             \"[Pok. maghos 696.]'\")\nBRT1111 = (\"BRT.txt leaf 618, running head 'IIII/1111': '• j. maγava- Adj. \\\"unverheiratet\\\": nāirivaite . . ahmāṯ pourum \"\n           \"framraomi . . yaθa …fravāxšōit \\\"dem beweibten spreche ich den Vorrang zu vor dem, dass einer unverheiratet altern \"\n           \"sollte\\\" V. 4.47. Ableit. aus *maγav- m. \\\"cælebs\\\". — Vgl. got. magus \\\"Knabe\\\", magaþs \\\"Jungfrau\\\" [usw., FICK Wb.4 \"\n           \"3.198].' Bartholomae keeps this apart from '• g. maga- m. \\\"Bund, Geheimbund\\\"', '• g. maga-van- \\\"der zum Bund … \"\n           \"gehört\\\"' and '• p. magav- (: j. moγu-) … \\\"magisch, Magier\\\"' in the same column range.\")\nKLN924 = (\"KLN_1966.txt leaf 496 (= printed p. 924): 'maid, n. — Shortened fr. maiden.' and 'maiden, n. — ME. meiden, fr. OE. \"\n          \"mægden, dimin. of mægeð, mægð, \\\"maid\\\", which is rel. to OS. magath, OFris. maged, megith, OHG. magad, MHG. maget, \"\n          \"\\\"virgin, maid\\\", G. Magd, … OE. mago, \\\"son, man, attendant, servant\\\", ON. mǫgr, \\\"son\\\", Goth. magus, \\\"boy, \"\n          \"servant\\\", magaþs, \\\"virgin\\\", and cogn. with Avestic maγava-, \\\"unmarried\\\", OIr. maug, mug, \\\"slave\\\"'. Leaf 496 vs \"\n          \"leaf 503 (marcasite, KLN:937) = 7 leaves ≈ 13 printed pages, exactly the gap between Nourai's 924 and 937, so his \"\n          \"pagination is internally consistent with this scan (whose leaf→page offset drifts by ~+20 leaves in vol. II).\")\nKLN937 = (\"KLN_1966.txt leaf 503 (= printed p. 937): 'marcasite, n., a native iron disulfide FeS₂ (mineral.) — F. marcassite, fr. \"\n          \"ML. marchasita, fr. Sp. marcaxita (ModSp. marcasita), fr. Arab. marqashithā, fr. Pers. marqashishā.' — the chart's \"\n          \"chain #1→#6, in this order, is copied verbatim from this one line of Klein.\")\nBQT1938 = (\"BQT_v4_pages.txt pdf page 21 = printed p. 1938 (running head '-۱۹۳۸-'), headword «مارقشیشا … بمعنی مرقشیشا است و آن \"\n           \"جوهریست که در دوای چشم بکار برند و آن اقسام می‌باشد: ذهبی و فضی و نحاسی و حدیدی و شبهی … و آنرا بعربی حجرالنور \"\n           \"خوانند», with Moʿin's footnote 4: «مرقشیثا. فرانسویان مرقشیثا را از عربی گرفته marcassite نامیدند. و عرب از آرامیان \"\n           \"این کلمه را اخذ کرده‌اند. در آرامی «مرقشیثا» یا «کیفا مقشیثا» بمعنی سنگی سخت است. عرب «کیفا» را حذف و راء بین میم و \"\n           \"قاف را بعوض محذوف آوردند برای خفت تلفظ، و ایرانیان آنرا بصور مرقشیشا و مارقشیشا نقل کرده‌اند «نخب‌الذخائر ص ۱۵ ح ۲». \"\n           \"در سریانی این کلمه با … آمده، اما ریشهٔ آن مشخص نیست «دزی ج ۲ ص ۳۵۸».\" )\nDEV157 = (\"DEV.txt line 1683 (Devic, Dict. étym. des mots d'origine orientale, p. 157): 'Marcassite. Pyrite de fer. Esp. \"\n          \"marquesita, autrefois marcaxita, portug. marquezita, ital. marcassita, bas lat. marchasita. De l'arabe مرقشيثا \"\n          \"marqachithâ … en persan مرقشيشا marqachicha (Richardson). La première orthographe est celle de Razi … et celle du \"\n          \"traité d'alchimie de Djabir (Géber) … et en général la seule que j'aie rencontrée dans les manuscrits. Aussi je \"\n          \"soupçonne fort le مرقشيشا marqachicha ci-dessus d'être une fausse lecture, causée par la facile confusion du ث th \"\n          \"avec le ش ch.'\")\nLKT1374 = (\"LKT.txt line 3180 (Lokotsch no. 1374): 'Aram. makkasitā: \\\"Schwefelkies\\\" [vielleicht wegen der Sprenkelung nach syr. \"\n           \"kessā \\\"Spreu\\\" so genannt; im übrigen ist das Wort noch nicht erklärt], hieraus ar. markasitā Bezeichnung der \"\n           \"\\\"Kiese\\\" … und ferner sp. kat. marcasita, marquesita, pg. marcasita, marquezita, frz. marcassite, it. marcassita; \"\n           \"engl. marcasite, dtsch. Markasit' — Aramaic → Arabic → Romance, with no Persian link at all.\")\n\nentries = []\n\n# ---------------------------------------------------------------- entry 1\ne1 = {\n \"entry\": 1,\n \"root\": \"Maghos, Maghu\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *magʰu- / *magʰos 'young; boy, unmarried' (Pokorny 696 maghos; Walde-Pokorny II 228 maghu-; Watkins/AHD maghu-)\",\n \"note\": (\"Both root names and the gloss are the received ones, and each of Nourai's two names is the lemma of one of his own \"\n          \"references: Pokorny p. 696 heads the article 'maghos, -a: young, servant, servant of god', Walde-Pokorny II 228 heads \"\n          \"the same article 'maghu- \\\"Knabe, Jüngling, unverheiratet\\\"', and Watkins has 'maghu-. Young person of either sex'. \"\n          \"This root is quite distinct from Pokorny's magh- 'to be able; power, sorcerer' (p. 695), the family of OP magu- \"\n          \"'magus'; Nourai keeps them apart, and the separate 'Maghu → see Maghos' box on this page is only a cross-reference. \"\n          \"One modern caveat: the family is confined to Iranian, Celtic and Germanic (plus Alb. makth, Latv. mazs) and has no \"\n          \"verbal base, so Wiktionary — following Kroonen and others — notes of the *maguz/*magaþs pair that it 'is likely of \"\n          \"foreign or substrate origin' rather than inherited PIE; the reconstruction *magʰ-ot-(i-) is then a pre-Germanic, not \"\n          \"a PIE, formation.\"),\n \"note_fa\": (\"هر دو نام ریشه و معنای آن پذیرفته و متداول است، و هر یک از دو نامی که نورایی آورده سرمدخلِ یکی از منابع خود اوست: \"\n             \"پوکورنی در ص ۶۹۶ مقاله را «maghos, -a: جوان، خدمتکار» نامیده، والده-پوکورنی در ج ۲ ص ۲۲۸ همان مقاله را «maghu- \"\n             \"پسر، جوان، ناهمسر» و واتکینز «maghu-: جوانِ هر دو جنس». این ریشه با ریشهٔ magh- «توانستن؛ توان، مغ» (پوکورنی ص ۶۹۵) \"\n             \"که خانوادهٔ magu- پارسی باستان است یکی نیست و نورایی این دو را از هم جدا نگه داشته؛ خانهٔ «Maghu → بنگرید به Maghos» \"\n             \"در همین صفحه تنها ارجاع متقابل است. یک نکتهٔ احتیاطی امروزی: این خانوادهٔ واژگانی تنها در ایرانی، سلتی و ژرمنی \"\n             \"(به‌افزون makth آلبانیایی و mazs لتونیایی) دیده می‌شود و ستاک فعلی ندارد؛ از این رو ویکی‌واژه به پیروی از کرونن \"\n             \"دربارهٔ جفتِ *maguz/*magaþs می‌نویسد که «به احتمال زیاد وام‌واژه یا از زبان بومیِ زیرلایه است» و بازسازی \"\n             \"*magʰ-ot-(i-) را پیش-ژرمنی می‌شمارد، نه هندواروپایی آغازین.\"),\n \"sources\": [W_MAGATH],\n \"ref_check\": [{\"ref\": \"POK:696\", \"status\": \"supports\", \"note\": POK696}],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II p. 228 s.v. 'maghu-'\", \"stance\": \"supports\", \"note\": WLD228},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 p. 39 s.v. 'maghu-'\", \"stance\": \"supports\", \"note\": AHD_MAGHU},\n   {\"src\": \"IEC\", \"where\": \"Mann, greps for magho-/maghu-/maghoti-\", \"stance\": \"silent\",\n    \"note\": (\"Mann has mēghos (2) 'kinsman, esp. by marriage' (line 10467), moghotos 'strong; strength' (line 10996) and maghido \"\n             \"'beat, pound' (line 10245), but no *maghos/*maghu- 'young' — he does not carry this root.\")}\n ],\n \"nodes\": []\n}\n\ne1[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"mağava\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Avestan maγava- (Nourai's ğ = γ) is a real, attested adjective 'unmarried, celibate', and its single passage is \"\n   \"Vendidad 4.47, where the married man is given precedence 'over him who should grow old unmarried'. Bartholomae (AiW col. 1111) \"\n   \"sets it up as a derivative of an unattested *maγav- m. 'cælebs' and himself compares Gothic magus 'boy' and magaþs 'virgin' — \"\n   \"i.e. Nourai's arrow root→node and the sister arrow to Germanic are Bartholomae's own comparison, taken over by Walde-Pokorny \"\n   \"II 228 (which cites 'Bartholomae Airan. Wb. 1111' explicitly) and by Pokorny 696. Phonologically Av. maγava- < *maghu- + -va-, \"\n   \"with PIE *gh > Av. γ between vowels. The word must be kept apart from three homographs in the same column range of \"\n   \"Bartholomae: Gathic maga- 'confederacy, secret community', magavan- 'member of the maga' (Y 51.15) and OP magav-/Av. moγu- \"\n   \"'magus', which belong to Pokorny's other root magh- 'be able, power, sorcerer' (p. 695) — a confusion Nourai avoids.\"),\n \"derivation_fa\": (\"صفت اوستایی maγava- (که نورایی آن را mağava نوشته و ğ او همان γ است) واژه‌ای واقعی و گواهی‌شده به معنی \"\n   \"«ناهمسر، بی‌زن» است و تنها گواه آن وندیداد ۴٫۴۷ است، آنجا که مردِ همسردار را بر کسی که «ناهمسر پیر شود» برتری می‌دهند. \"\n   \"بارتولومه (فرهنگ ایرانی باستان، ستون ۱۱۱۱) آن را برساختهٔ *maγav- «مجرّد» می‌داند و خود آن را با magus «پسر» و magaþs \"\n   \"«دوشیزه» گوتی می‌سنجد؛ یعنی همین دو پیکانی که نورایی کشیده (از ریشه به این گره، و از ریشه به شاخهٔ ژرمنی) سنجش خود بارتولومه \"\n   \"است که والده-پوکورنی (ج ۲ ص ۲۲۸، با ارجاع صریح به ستون ۱۱۱۱ بارتولومه) و پوکورنی (ص ۶۹۶) پذیرفته‌اند. از نظر آوایی \"\n   \"maγava- < *maghu- + پسوند -va- است و gh هندواروپایی در میان دو واکه در اوستایی به γ بدل شده. این واژه را باید از سه همنگارِ \"\n   \"همان بخش فرهنگ بارتولومه جدا داشت: maga- گاهانی «انجمن، پیمان»، magavan- «عضو مغا» (یسنا ۵۱٫۱۵) و magav- پارسی باستان / \"\n   \"moγu- اوستایی «مغ» که به ریشهٔ دیگرِ magh- «توانستن؛ مغ» (پوکورنی ص ۶۹۵) می‌رسند — اشتباهی که نورایی از آن پرهیز کرده است.\"),\n \"sources\": [W_MAGATH],\n \"ref_check\": [\n   {\"ref\": \"POK:696\", \"status\": \"supports\", \"note\": POK696},\n   {\"ref\": \"KLN:924\", \"status\": \"supports\", \"note\": KLN924}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"AiW col. 1111 s.v. 'maγava-'\", \"stance\": \"supports\", \"note\": BRT1111},\n   {\"src\": \"WLD\", \"where\": \"Bd. II p. 228\", \"stance\": \"supports\", \"note\": WLD228},\n   {\"src\": \"HRN\", \"where\": \"HRN.txt / HUB.txt, greps for maγava/mayava/magad\", \"stance\": \"silent\",\n    \"note\": \"Horn and Hübschmann have nothing: the root left no New Persian descendant, so their Persian etymological dictionaries do not treat it.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 2, \"lang\": None, \"words\": \"\",\n \"verdict\": \"unverified\",\n \"derivation\": (\"Blank box: the printed page (pdf p. 319, checked on the rendered image, copy kept at \"\n   \"data/verification/sources/refs/ocr/BOOK/319.png) really does show an arrow running from the Avestan mağava box into an empty \"\n   \"rectangle with no language label, no word and no reference — a leftover of the author's chart layout, not an extraction \"\n   \"failure. There is nothing to verify; if anything was intended it would be the Persian/Middle Persian outcome of maγava-, and \"\n   \"no such reflex is known (Horn, Hübschmann and MacKenzie have none).\"),\n \"derivation_fa\": (\"خانهٔ خالی: بر صفحهٔ چاپی (تصویرِ صفحهٔ ۳۱۹ که نسخهٔ آن در ocr/BOOK/319.png نگه داشته شده) به‌راستی پیکانی از \"\n   \"خانهٔ mağava اوستایی به مستطیلی تهی کشیده شده که نه نام زبان دارد، نه واژه و نه ارجاع؛ این بازماندهٔ صفحه‌آرایی نمودارهای \"\n   \"نویسنده است و خطای خوانش اسکن نیست. چیزی برای بررسی نمانده؛ اگر قرار بود چیزی در آن بیاید بازماندهٔ فارسی/فارسی میانهٔ \"\n   \"maγava- بود که چنین بازمانده‌ای شناخته نیست (هرن، هوبشمان و مکنزی هیچ‌کدام آن را ندارند).\"),\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The box carries no reference (and no content) in the book.\"}],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, grep for mag-/maγ- 'unmarried'\", \"stance\": \"silent\", \"note\": \"No Middle Persian continuation of maγava- in MacKenzie's Concise Pahlavi Dictionary.\"},\n   {\"src\": \"HRN\", \"where\": \"HRN.txt\", \"stance\": \"silent\", \"note\": \"Horn's Grundriss has no New Persian reflex either.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Germanic\", \"words\": \"magadi\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"'magadi' is Watkins' notation for Proto-Germanic *magadi- (*magaþ(i)-) 'young girl, virgin', from a suffixed \"\n   \"*magho-ti- of the same root: AHD 1985 p. 39 'maghu-. Young person of either sex. Suffixed form *magho-ti- in Germanic \"\n   \"*magadi-, with diminutive *magadin-, in Old English mægden, virgin: MAID, MAIDEN' — the chart's node, its gloss and its \"\n   \"reference tag 'AHD' are simply this line. The form is well attested across the branch: Gothic magaþs 'virgin', Old Saxon \"\n   \"magath, Old High German magad (> German Magd), Old English mægeþ/mægþ; Walde-Pokorny II 228 and Pokorny 696 reconstruct the \"\n   \"abstract *maghotis 'young womanhood' > concrete 'girl' for exactly this set, and the Celtic abstract *magot-actā (Old Irish \"\n   \"ingen maccdacht, Breton matez 'maidservant') is its formal twin. Wiktionary reconstructs it as *magaþs 'from pre-Germanic \"\n   \"*magʰ-ot-(i-), a feminine derivative of *maguz (\\\"boy\\\")', with the same suffix as *brūdiz 'bride'.\"),\n \"derivation_fa\": (\"«magadi» نگارشِ واتکینز برای ژرمنی آغازین *magadi- (*magaþ(i)-) «دخترِ جوان، دوشیزه» است، از صورت پسونددارِ \"\n   \"*magho-ti- همین ریشه: پیوست واتکینز (ص ۳۹) می‌نویسد «maghu-: جوانِ هر دو جنس. صورت پسونددارِ *magho-ti- در ژرمنی *magadi- با \"\n   \"مصغرِ *magadin- در انگلیسی کهن mægden «دوشیزه»: MAID, MAIDEN» — یعنی این گره و معنای آن و برچسب ارجاع «AHD» چیزی جز همین سطر \"\n   \"نیست. این صورت در سراسر شاخهٔ ژرمنی گواهی شده است: magaþs گوتی «دوشیزه»، magath ساکسون کهن، magad آلمانی علیای کهن (> Magd \"\n   \"آلمانی) و mægeþ/mægþ انگلیسی کهن. والده-پوکورنی (ج ۲ ص ۲۲۸) و پوکورنی (ص ۶۹۶) برای همین مجموعه صورتِ اسم معنیِ *maghotis \"\n   \"«جوان‌زنی» و سپس معنای عینی «دختر» را بازمی‌سازند و همتای صوری آن اسم معنیِ سلتی *magot-actā است. ویکی‌واژه نیز *magaþs را \"\n   \"«از پیش-ژرمنیِ *magʰ-ot-(i-)، برساختهٔ مادینه از *maguz «پسر»» می‌داند.\"),\n \"sources\": [W_MAGATH],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": AHD_MAGHU}],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II p. 228\", \"stance\": \"supports\", \"note\": WLD228},\n   {\"src\": \"POK\", \"where\": \"p. 696\", \"stance\": \"supports\", \"note\": POK696},\n   {\"src\": \"KLN\", \"where\": \"leaf 496 (= p. 924) s.v. 'maiden'\", \"stance\": \"supports\", \"note\": KLN924}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 4, \"lang\": \"English\", \"words\": \"maid, maiden\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Old English mægden (a diminutive in -en of mægeþ/mægþ 'maid', from Gmc *magadi- + *-īn-) > Middle English \"\n   \"meiden, maiden > maiden; maid is the shortened Middle English by-form of maiden (13th c.), so the two English words on the \"\n   \"chart are one word. Klein p. 924: 'maid, n. — Shortened fr. maiden'; 'maiden, n. — ME. meiden, fr. OE. mægden, dimin. of \"\n   \"mægeð, mægð, \\\"maid\\\" … and cogn. with Avestic maγava-, \\\"unmarried\\\"'. Watkins gives the same in one line, ending ': MAID, \"\n   \"MAIDEN'. Skeat's Concise (p. ~280) has the same chain but attaches it to a 'Teut. base MAG, to have strength', i.e. he merges \"\n   \"this root with magh- 'to be able' — the older analysis that Pokorny and Watkins separate.\"),\n \"derivation_fa\": (\"mægden انگلیسی کهن (مصغّرِ -en از mægeþ/mægþ «دوشیزه»، از ژرمنی *magadi- + *-īn-) به meiden/maiden انگلیسی \"\n   \"میانه و سپس maiden امروزی رسیده است؛ و maid صورت کوتاه‌شدهٔ همان maiden در انگلیسی میانه (سدهٔ سیزدهم م.) است، پس این دو واژهٔ \"\n   \"نمودار در اصل یک واژه‌اند. کلاین (ص ۹۲۴): «maid: کوتاه‌شدهٔ maiden» و «maiden: از انگلیسی میانه meiden، از انگلیسی کهن \"\n   \"mægden، مصغّرِ mægeð/mægð … و هم‌ریشه با maγava- اوستایی «ناهمسر»». واتکینز نیز همین را در یک سطر می‌آورد. اسکیت در فرهنگ \"\n   \"مختصر خود همان زنجیره را دارد اما آن را به «ستاک ژرمنیِ MAG: نیرو داشتن» می‌بندد، یعنی این ریشه را با magh- «توانستن» یکی \"\n   \"می‌گیرد — همان تحلیل کهن‌تری که پوکورنی و واتکینز از هم جدا کرده‌اند.\"),\n \"sources\": [W_MAGATH],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The English box carries no reference; the parent Germanic box's AHD reference covers the link (': MAID, MAIDEN').\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"leaf 496 (= p. 924) s.v. 'maid' / 'maiden'\", \"stance\": \"supports\", \"note\": KLN924},\n   {\"src\": \"SKT\", \"where\": \"SKT.txt leaf 300 (= printed p. ~280) s.v. 'maid, maiden'\", \"stance\": \"partial\",\n    \"note\": (\"'maid, maiden. (E) M.E. mayde, merely short for earlier maiden, meiden. A.S. mægden, a maiden: short for mageð-en, \"\n             \"dimin. form of mageð … Goth. magaþs, a virgin, maid, and magu, a son or kinsman … orig. \\\"a growing lad,\\\" one \"\n             \"increasing in strength. From Teut. base MAG, to have strength.' Same chain, different ultimate root.\")},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 p. 39; index line 1795-1796 'MAID maghu- / MAIDEN maghu-'\", \"stance\": \"supports\", \"note\": AHD_MAGHU}\n ]\n})\n\nentries.append(e1)\n\n# ---------------------------------------------------------------- entry 3\ne3 = {\n \"entry\": 3,\n \"root\": \"Mağšîsa\",\n \"verdict\": \"transcription_suspect\",\n \"modern_form\": \"Aramaic/Syriac maqšīṯā 'hard (fem.)' in the phrase kēfā maqšīṯā 'hard stone' — and, for the word actually at issue, Aramaic marqəšīṯā (מרקשיתא) 'marcasite', itself from Akkadian marḫašītu\",\n \"note\": (\"The root box is a garbled rendering of the Aramaic word in Nourai's own source. Moʿin's etymological footnote to \"\n          \"Borhan-e Qateʿ (p. 1938 n. 4, quoted in full below and repeated verbatim by Dehkhodā: «اصل کلمه آرامی است و آن کیفا \"\n          \"مقشیثا باشد یعنی سنگ سخت») says the Aramaic is مرقشیثا marqəšīṯā, or the two-word phrase کیفا مقشیثا kēfā maqšīṯā \"\n          \"'hard stone'. Nourai has taken the second word of that phrase, مقشیثا, and printed it 'Mağšîsa' — with ğ where q \"\n          \"belongs (his own transliteration of the same consonant elsewhere on this page is q, cf. marqašîšâ) and with s for ث, \"\n          \"the Persian pronunciation of the Aramaic ṯ. The gloss is off in the same way: maqšīṯā is the adjective 'hard' (Syriac \"\n          \"root qšy), the word for 'stone' being kēfā, so 'Mağšîsa : stone' compresses a two-word phrase into one. The printed \"\n          \"page shows 'Mağšîsa' (rendered image kept at data/verification/sources/refs/ocr/BOOK/319.png), so the extraction is \"\n          \"faithful and the fault is the book's. Substantively there is a further problem: the modern account (Wiktionary, \"\n          \"Lokotsch no. 1374) is that the mineral name is Aramaic marqəšīṯā < Akkadian marḫašītu 'glass or artificial gem', from \"\n          \"Sumerian mar-ḫa-ši (the region Marhaši), so the 'hard stone' etymology is itself a learned folk etymology of the \"\n          \"Aramaic word, and the whole chart hangs on it.\"),\n \"note_fa\": (\"خانهٔ ریشه صورتی آشفته از واژهٔ آرامیِ منبع خودِ نورایی است. حاشیهٔ ریشه‌شناختی معین بر برهان قاطع (ص ۱۹۳۸، پانویس ۴) \"\n             \"— که دهخدا هم آن را عیناً نقل کرده: «اصل کلمه آرامی است و آن کیفا مقشیثا باشد یعنی سنگ سخت» — می‌گوید صورت آرامی \"\n             \"«مرقشیثا» است یا ترکیب دوواژه‌ای «کیفا مقشیثا» به معنی «سنگِ سخت». نورایی واژهٔ دوم این ترکیب، یعنی «مقشیثا» را \"\n             \"برداشته و «Mağšîsa» چاپ کرده است: ğ به‌جای q (در حالی که در همان صفحه ق را در marqašîšâ با q آورده) و s به‌جای ث، \"\n             \"یعنی تلفظ فارسیِ ثِ آرامی. معنا نیز به همین شکل جابه‌جا شده است: maqšīṯā صفتِ «سخت» است (از ریشهٔ سریانی qšy) و \"\n             \"واژهٔ «سنگ» همان kēfā است، پس «Mağšîsa: stone» یک ترکیب دوواژه‌ای را در یک واژه فشرده کرده. تصویر صفحهٔ چاپی نشان \"\n             \"می‌دهد که در کتاب «Mağšîsa» آمده، پس استخراج داده درست است و خطا از خودِ کتاب است. نکتهٔ محتوایی مهم‌تر: بر پایهٔ \"\n             \"پژوهش امروزی (ویکی‌واژه، لوکوچ شمارهٔ ۱۳۷۴) نامِ این کانی از آرامی marqəšīṯā و آن نیز از اکدی marḫašītu «شیشه یا \"\n             \"گوهر ساختگی» و در نهایت از سومری mar-ḫa-ši (نام سرزمین مرهشی) است؛ پس همان ریشه‌شناسیِ «سنگ سخت» خود ریشه‌شناسی \"\n             \"عامیانه‌ای فرهیخته برای واژهٔ آرامی است و کل نمودار بر آن استوار شده است.\"),\n \"error_in\": \"book\",\n \"book_prints\": \"Mağšîsa : stone\",\n \"correct_form\": \"maqšīṯā (in kēfā maqšīṯā 'hard stone'); the mineral name itself is Aramaic marqəšīṯā\",\n \"sources\": [A_MARQ, W_ARMARQ, W_MARC],\n \"ref_check\": [{\"ref\": \"MON:4036\", \"status\": \"partial\",\n   \"note\": (\"Moʿin's Farhang cannot be page-checked online (refs_online.json: 'Page numbers cannot be mapped online'), but the \"\n            \"content is verifiable twice over: (a) Moʿin's own footnote in Borhan-e Qateʿ p. 1938 n. 4 — \" + BQT1938 + \" ; (b) \"\n            \"Dehkhodā, s.v. مرقشیشا (archived abadis page): «مرقشیشا. [ م َق َ ] ( اِ ) اصل کلمه آرامی است و آن کیفا مقشیثا باشد \"\n            \"یعنی سنگ سخت. ( یادداشت مرحوم دهخدا )». Both give مقشیثا / مرقشیثا, not 'Mağšîsa', and both gloss the phrase as \"\n            \"'hard stone', not 'stone'.\")}],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"vol. 4, printed p. 1938 (pdf p. 21), s.v. مارقشیشا, Moʿin's fn. 4\", \"stance\": \"contradicts\", \"note\": BQT1938},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1374\", \"stance\": \"partial\", \"note\": LKT1374},\n   {\"src\": \"AFA\", \"where\": \"Fraenkel, Aramäische Fremdwörter im Arabischen — grep for markas/marqas/Schwefelkies\", \"stance\": \"silent\",\n    \"note\": \"Fraenkel's collection of Aramaic loanwords in Arabic does not treat this mineral name (nothing found in AFA.txt).\"}\n ],\n \"nodes\": []\n}\n\ne3[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Persian\", \"words\": \"marqašîšâ «مرقشیشا»\",\n \"verdict\": \"disputed\",\n \"derivation\": (\"The Persian word is real and well documented: Borhan-e Qateʿ (p. 1938 s.v. مارقشیشا, and again p. 1995 s.v. \"\n   \"مرقشیشا) defines it as «جوهری … که در داروهای چشم بکار برند» — a mineral used in eye-salves, in gold, silver, copper, iron and \"\n   \"brass-coloured varieties, called حجرالنور in Arabic; Moʿin's dictionary glosses it «پیریت سفید که در قدیم به عنوان دارو در \"\n   \"معالجهٔ درد چشم کاربرد داشته است، سولفور طبیعی آهن» — so Nourai's gloss 'an iron mineral (ore)' is right. What is disputed is \"\n   \"the arrow: Nourai has Aramaic → Persian directly (and then Persian → Arabic). His own source says the opposite. Moʿin's \"\n   \"footnote (BQT 1938 n. 4): «عرب از آرامیان این کلمه را اخذ کرده‌اند … و ایرانیان آنرا بصور مرقشیشا و مارقشیشا نقل کرده‌اند» — \"\n   \"the Arabs took it from the Aramaeans and the Iranians then transmitted it as marqašīšā/mārqašīšā, i.e. Aramaic > Arabic > \"\n   \"Persian. Devic (p. 157) goes further and suspects the Persian ش-form of being 'une fausse lecture' of the Arabic ث-form \"\n   \"(ث/ش are one shape apart in Arabic script), and Wiktionary says the word was merely 'encountered in Persian as marqašišâ', \"\n   \"reshaped under the influence of Persian شیشه šīše 'glass'. Lokotsch no. 1374 has no Persian stage at all. The Persian word is \"\n   \"therefore best taken as an Arabic loan in Persian (with a folk-etymological -šīšā), not as the source of the Arabic.\"),\n \"derivation_fa\": (\"واژهٔ فارسی واقعی و پرگواه است: برهان قاطع (ص ۱۹۳۸ ذیل «مارقشیشا» و ص ۱۹۹۵ ذیل «مرقشیشا») آن را «جوهری … که \"\n   \"در داروهای چشم بکار برند» می‌داند با گونه‌های ذهبی و فضی و نحاسی و حدیدی و شبهی که در عربی «حجرالنور» خوانده می‌شود، و فرهنگ \"\n   \"معین آن را «پیریت سفید که در قدیم به عنوان دارو در معالجهٔ درد چشم کاربرد داشته است، سولفور طبیعی آهن» معنی می‌کند؛ پس معنایی \"\n   \"که نورایی داده («کانی آهن») درست است. آنچه محل اختلاف است خودِ پیکان است: نورایی آرامی را بی‌واسطه به فارسی و سپس فارسی را به \"\n   \"عربی می‌رساند، در حالی که منبع خودش خلاف آن را می‌گوید. در پانویس معین (برهان، ص ۱۹۳۸): «عرب از آرامیان این کلمه را اخذ \"\n   \"کرده‌اند … و ایرانیان آنرا بصور مرقشیشا و مارقشیشا نقل کرده‌اند»، یعنی آرامی > عربی > فارسی. دِویک (ص ۱۵۷) از این فراتر \"\n   \"می‌رود و صورت فارسیِ با «ش» را «خوانشی نادرست» از صورت عربیِ با «ث» می‌داند (ث و ش در خط عربی تنها یک نقطه فاصله دارند)، و \"\n   \"ویکی‌واژه می‌نویسد این واژه در فارسی به صورت marqašišâ «دیده شده» و زیر تأثیر «شیشه» بازشکل یافته است. لوکوچ (شمارهٔ ۱۳۷۴) هیچ \"\n   \"حلقهٔ فارسی ندارد. پس این واژه در فارسی وام‌واژه‌ای عربی است — با ریشه‌شناسی عامیانهٔ «-شیشا» — نه سرچشمهٔ صورت عربی.\"),\n \"sources\": [A_MARQ, W_ARMARQ],\n \"ref_check\": [\n   {\"ref\": \"SKT:314\", \"status\": \"not_found\",\n    \"note\": (\"Skeat's Concise Etymological Dictionary has no entry for marcasite at all (grep -i 'marcas|markas|marchas' SKT.txt \"\n             \"→ nothing), and p. 314 of the 1911 edition is not even in the M range: SKT.txt leaf 334 (= printed 314) carries the \"\n             \"'neo-' entries, while the marc- entries stand on leaf 296 (= printed ~276). Either a different edition or a wrong \"\n             \"page number.\")},\n   {\"ref\": \"KLN:937\", \"status\": \"supports\", \"note\": KLN937 + \" Klein is, however, the one source that gives this direction.\"},\n   {\"ref\": \"BQT:1938\", \"status\": \"contradicts\", \"note\": BQT1938},\n   {\"ref\": \"MON:4036\", \"status\": \"partial\", \"note\": \"Same footnote as BQT:1938 (Moʿin is the editor of both); it supports the Aramaic origin but routes it through Arabic, and gives the Aramaic as مقشیثا / مرقشیثا.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"vol. 4 pp. 1938 and 1995\", \"stance\": \"contradicts\", \"note\": BQT1938 + \" Also p. 1995 s.v. «مرقشیشا … و آن جوهری باشد که در داروهای چشم بکار برند … و آنرا بعربی حجرالنور خوانند» with the cross-reference «مارقشیشا (ه.م.) و رک: دزی ج ۱ ص ۹۸۴».\"},\n   {\"src\": \"MON\", \"where\": \"abadis.ir/fatofa/مرقشیشا (فرهنگ معین section)\", \"stance\": \"partial\",\n    \"note\": \"Moʿin: «پیریت سفید که در قدیم به عنوان دارو در معالجهٔ درد چشم کاربرد داشته است، سولفور طبیعی آهن» — confirms the word and the gloss; Dehkhodā on the same page gives the Aramaic «کیفا مقشیثا … یعنی سنگ سخت».\"},\n   {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen — grep مرقش/marqas\", \"stance\": \"silent\",\n    \"note\": \"Asbaghi's inventory of Persian loanwords in Arabic does not include marqašīṯā — a telling silence against Klein's Persian→Arabic direction.\"},\n   {\"src\": \"AFM\", \"where\": \"Addi Shir, الألفاظ الفارسية المعربة — grep مرقش\", \"stance\": \"silent\",\n    \"note\": \"Addi Shir's list of Persian words arabicised does not have it either.\"},\n   {\"src\": \"HRN\", \"where\": \"HRN.txt / HUB.txt\", \"stance\": \"silent\", \"note\": \"Horn and Hübschmann do not treat the word (a late technical loan, outside their remit).\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Arabic\", \"words\": \"marqašîtha\",\n \"verdict\": \"disputed\",\n \"derivation\": (\"Arabic مرقشيثا / مرقشيتا marqašīṯā 'marcasite, pyrite' is the pivot of the whole chain, and the direction drawn \"\n   \"here (Persian → Arabic) is Klein's and only Klein's: 'fr. Arab. marqashithā, fr. Pers. marqashishā' (p. 937). Everything else \"\n   \"reverses it. Wiktionary: Arabic مَرْقَشِيتَا 'from Aramaic marqəšīṯā, ultimately from Akkadian marḫašītu (\\\"glass or artificial \"\n   \"gem\\\") … from Sumerian mar-ḫa-šiKI', the Mesopotamian region Marhaši, and adds that the word was 'encountered in Persian as \"\n   \"marqašišâ', influenced by Persian šīše 'glass'. Lokotsch no. 1374 derives Arabic markasitā from Aramaic makkasitā. Moʿin's \"\n   \"footnote explains even the shape of the Arabic word from the Aramaic phrase: «عرب «کیفا» را حذف و راء بین میم و قاف را بعوض \"\n   \"محذوف آوردند برای خفت تلفظ» (the Arabs dropped kēfā and inserted an r between m and q to compensate). Devic notes that the \"\n   \"ث-spelling is the one in the manuscripts of al-Rāzī and of Jābir's alchemical treatise (9th-10th c.) and 'en général la seule \"\n   \"que j'aie rencontrée dans les manuscrits', which makes the Arabic ث-form the older, and the Persian ش-form secondary — the \"\n   \"exact opposite of the arrow. So: the Arabic word is genuine and is the source of everything downstream, but its parent is \"\n   \"Aramaic, not Persian.\"),\n \"derivation_fa\": (\"«مرقشيثا/مرقشيتا» عربی، نامِ همین کانی، لولای همهٔ زنجیره است و جهتی که در نمودار کشیده شده (فارسی → عربی) \"\n   \"تنها از کلاین است: «از عربی marqashithā، از فارسی marqashishā» (ص ۹۳۷). دیگر منابع همه آن را برمی‌گردانند. ویکی‌واژه: عربی \"\n   \"مَرْقَشِيتَا «از آرامی marqəšīṯā و در نهایت از اکدی marḫašītu «شیشه یا گوهر ساختگی» … از سومری mar-ḫa-ši»، نام سرزمین مرهشی؛ و \"\n   \"می‌افزاید که این واژه «در فارسی به صورت marqašišâ دیده شده» و زیر تأثیر «شیشه» بازشکل یافته است. لوکوچ (۱۳۷۴) صورت عربی را از \"\n   \"آرامی makkasitā می‌گیرد. پانویس معین حتی ساختِ صورت عربی را از همان ترکیب آرامی توضیح می‌دهد: «عرب «کیفا» را حذف و راء بین \"\n   \"میم و قاف را بعوض محذوف آوردند برای خفت تلفظ». دِویک یادآور می‌شود که نگارش با «ث» همان است که در دست‌نویس‌های رازی و رسالهٔ \"\n   \"کیمیای جابر (سدهٔ سوم-چهارم هجری) آمده و «در کل تنها صورتی است که در دست‌نویس‌ها دیده‌ام»؛ پس صورت عربیِ با «ث» کهن‌تر و صورت \"\n   \"فارسیِ با «ش» ثانوی است — درست عکسِ پیکان نمودار. نتیجه: واژهٔ عربی اصیل است و سرچشمهٔ همهٔ حلقه‌های پس از خود، اما پدرِ آن \"\n   \"آرامی است، نه فارسی.\"),\n \"sources\": [W_ARMARQ, W_MARC, A_MARQ],\n \"ref_check\": [{\"ref\": \"KLN:937\", \"status\": \"supports\", \"note\": KLN937}],\n \"consulted\": [\n   {\"src\": \"LKT\", \"where\": \"no. 1374\", \"stance\": \"contradicts\", \"note\": LKT1374},\n   {\"src\": \"DEV\", \"where\": \"Devic p. 157 s.v. 'Marcassite'\", \"stance\": \"contradicts\", \"note\": DEV157},\n   {\"src\": \"BQT\", \"where\": \"vol. 4 p. 1938 n. 4\", \"stance\": \"contradicts\", \"note\": BQT1938},\n   {\"src\": \"AFA\", \"where\": \"Fraenkel\", \"stance\": \"silent\", \"note\": \"not in Fraenkel's Aramaic loanwords in Arabic.\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Spanish\", \"words\": \"marcaxita\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Old Spanish marcaxita (modern marcasita, also marquesita, margajita) is the Andalusi Arabic word taken into \"\n   \"Ibero-Romance, with -x- for Arabic ش (the regular Old Spanish rendering, x = /ʃ/) and the ث reinterpreted as -t-; the mineral \"\n   \"reached Europe through the Arabic alchemical and lapidary literature of al-Andalus. Klein p. 937 gives exactly this step ('fr. \"\n   \"Sp. marcaxita (ModSp. marcasita), fr. Arab. marqashithā'), Devic p. 157 lists 'Esp. marquesita, autrefois marcaxita', and \"\n   \"Lokotsch 1374 'sp. kat. marcasita, marquesita'; Wiktionary lists Spanish marcasita and margajita among the descendants of the \"\n   \"Arabic word.\"),\n \"derivation_fa\": (\"«marcaxita» اسپانیایی کهن (امروز marcasita، و نیز marquesita و margajita) همان واژهٔ عربیِ اندلسی است که به \"\n   \"زبان‌های ایبری راه یافته: x در آن برابرِ شِ عربی است (نگارش عادی /ʃ/ در اسپانیایی کهن) و ث به t بدل شده است؛ خودِ این کانی از \"\n   \"راه ادبیات کیمیا و جواهرشناسی عربی در اندلس به اروپا رسید. کلاین (ص ۹۳۷) همین گام را می‌آورد، دِویک (ص ۱۵۷) «Esp. marquesita، \"\n   \"پیش‌تر marcaxita» را ثبت کرده و لوکوچ (۱۳۷۴) «sp. kat. marcasita, marquesita» را؛ ویکی‌واژه نیز marcasita و margajita \"\n   \"اسپانیایی را در شمار بازماندگان واژهٔ عربی می‌آورد.\"),\n \"sources\": [W_ARMARQ, W_MARC],\n \"ref_check\": [{\"ref\": \"KLN:937\", \"status\": \"supports\", \"note\": KLN937}],\n \"consulted\": [\n   {\"src\": \"DEV\", \"where\": \"p. 157\", \"stance\": \"supports\", \"note\": DEV157},\n   {\"src\": \"LKT\", \"where\": \"no. 1374\", \"stance\": \"supports\", \"note\": LKT1374},\n   {\"src\": \"DOZ\", \"where\": \"Dozy-Engelmann, Glossaire — grep 'marcas|marques'\", \"stance\": \"silent\", \"note\": \"nothing found in DOZ.txt for this word.\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Middle Latin\", \"words\": \"marchasita\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"Medieval Latin marchasita (also marcasita, marchesita) is the form of the mineral name in the Latin alchemical \"\n   \"and lapidary tradition from the 12th-13th c. onwards (it is in the Latin translations of the Arabic alchemists and in Albertus \"\n   \"Magnus' De mineralibus). The word itself is beyond doubt; the only reason for 'plausible' is the immediate parent: Klein \"\n   \"(p. 937), whom the chart follows, has ML marchasita 'fr. Sp. marcaxita', whereas Wiktionary derives Medieval Latin marchasita \"\n   \"straight from Arabic مَرْقَشِيتَا, and Lokotsch too puts the Romance forms side by side rather than in a chain. Since the Latin \"\n   \"translations were largely made in Spain, the two accounts are not far apart, but the Spanish → Latin ordering is Klein's \"\n   \"reconstruction, not an established fact.\"),\n \"derivation_fa\": (\"«marchasita» لاتینیِ میانه (و نیز marcasita و marchesita) صورتِ این نام در سنت کیمیا و جواهرشناسیِ لاتینی از \"\n   \"سدهٔ دوازدهم-سیزدهم میلادی است (در ترجمه‌های لاتینیِ کیمیاگران عرب و در «المعادن» آلبرتوس ماگنوس آمده). خودِ واژه تردیدی ندارد؛ \"\n   \"تنها علتِ حکمِ «با احتیاط پذیرفتنی» پدرِ بی‌واسطهٔ آن است: کلاین (ص ۹۳۷) که نمودار از او پیروی می‌کند marchasita را «از \"\n   \"marcaxita اسپانیایی» می‌گیرد، اما ویکی‌واژه لاتینیِ میانه را یک‌سر از عربیِ مَرْقَشِيتَا می‌گیرد و لوکوچ نیز صورت‌های رومی را \"\n   \"پهلوی هم می‌نشاند، نه در یک زنجیره. چون ترجمه‌های لاتینی بیشتر در اسپانیا انجام شده، این دو روایت بسیار دور از هم نیستند، اما \"\n   \"ترتیبِ اسپانیایی → لاتینی بازسازیِ کلاین است، نه واقعیتی مسلّم.\"),\n \"sources\": [W_MARC, W_ARMARQ],\n \"ref_check\": [{\"ref\": \"KLN:937\", \"status\": \"supports\", \"note\": KLN937}],\n \"consulted\": [\n   {\"src\": \"DEV\", \"where\": \"p. 157\", \"stance\": \"supports\", \"note\": \"'bas lat. marchasita' listed as the Latin form, with the Spanish and Italian forms beside it.\"},\n   {\"src\": \"LKT\", \"where\": \"no. 1374\", \"stance\": \"partial\", \"note\": LKT1374 + \" Lokotsch gives no Latin stage explicitly.\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 5, \"lang\": \"French\", \"words\": \"marcassite\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"French marcassite (16th c., in alchemical and mineralogical writing) comes from Medieval Latin marchasita, with \"\n   \"the learned suffix -ite of mineral names and -ss- for the Latin -s-. Klein p. 937: 'F. marcassite, fr. ML. marchasita'; Devic \"\n   \"p. 157 heads his article 'Marcassite. Pyrite de fer' and lists the same Latin and Romance forms; Lokotsch 1374 'frz. \"\n   \"marcassite'. Moʿin's footnote makes the same point from the Persian side: «فرانسویان مرقشیثا را از عربی گرفته marcassite \"\n   \"نامیدند».\"),\n \"derivation_fa\": (\"«marcassite» فرانسوی (سدهٔ شانزدهم میلادی، در نوشته‌های کیمیایی و کانی‌شناسی) از marchasita لاتینیِ میانه \"\n   \"گرفته شده است، با پسوند فرهیختهٔ -ite که نشانهٔ نام کانی‌هاست و -ss- به‌جای -s- لاتینی. کلاین (ص ۹۳۷): «F. marcassite از ML. \"\n   \"marchasita»؛ دِویک (ص ۱۵۷) مقالهٔ خود را «Marcassite. Pyrite de fer» نام داده و همان صورت‌های لاتینی و رومی را برمی‌شمارد؛ \"\n   \"لوکوچ (۱۳۷۴) «frz. marcassite». پانویس معین همین را از سوی فارسی می‌گوید: «فرانسویان مرقشیثا را از عربی گرفته marcassite \"\n   \"نامیدند».\"),\n \"sources\": [W_MARC],\n \"ref_check\": [{\"ref\": \"KLN:937\", \"status\": \"supports\", \"note\": KLN937}],\n \"consulted\": [\n   {\"src\": \"DEV\", \"where\": \"p. 157\", \"stance\": \"supports\", \"note\": DEV157},\n   {\"src\": \"BQT\", \"where\": \"vol. 4 p. 1938 n. 4\", \"stance\": \"supports\", \"note\": \"«فرانسویان مرقشیثا را از عربی گرفته marcassite نامیدند» — Moʿin agrees on the French form, though he takes it from Arabic directly.\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 6, \"lang\": \"English\", \"words\": \"marcasite\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"English marcasite (from the 15th c. in alchemical texts; 'crystallized iron pyrites, used in the eighteenth \"\n   \"century for ornaments', now FeS₂, the orthorhombic dimorph of pyrite) is the French/Latin word anglicised, with -ite for \"\n   \"-ite/-ita. Klein p. 937 routes it 'F. marcassite, fr. ML. marchasita' as the chart does; Wiktionary has 'From Medieval Latin \"\n   \"marchasita et al., from Arabic مَرْقَشِيتَا (marqašītā)', i.e. the same word with the French stage left out; Webster's entry \"\n   \"reads 'mar'ca-site, n. [Fr. marcassite, prob. of Ar. origin]' — the Arabic origin of the English word is common ground, only \"\n   \"the Persian pre-history (nodes #1-#2) is not.\"),\n \"derivation_fa\": (\"«marcasite» انگلیسی (از سدهٔ پانزدهم میلادی در متون کیمیایی؛ نخست «پیریتِ متبلور که در سدهٔ هجدهم در زیورسازی \"\n   \"به کار می‌رفت» و امروز FeS₂، دوگانهٔ راست‌لوزیِ پیریت) همان واژهٔ فرانسوی/لاتینی است که انگلیسی شده، با پسوند -ite. کلاین (ص \"\n   \"۹۳۷) آن را — چنان‌که نمودار می‌گوید — «از F. marcassite، از ML. marchasita» می‌گیرد؛ ویکی‌واژه «از لاتینیِ میانه marchasita و \"\n   \"غیره، از عربی مَرْقَشِيتَا» دارد، یعنی همان واژه با حذف حلقهٔ فرانسوی؛ و وبستر می‌نویسد «mar'ca-site: از فرانسوی marcassite، \"\n   \"احتمالاً با اصل عربی». پس اصلِ عربیِ واژهٔ انگلیسی مورد اجماع است و تنها پیش‌تاریخِ فارسیِ آن (گره‌های ۱ و ۲) پذیرفته نیست.\"),\n \"sources\": [W_MARC],\n \"ref_check\": [{\"ref\": \"KLN:937\", \"status\": \"supports\", \"note\": KLN937}],\n \"consulted\": [\n   {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt line ~112770 s.v. 'mar'ca-site'\", \"stance\": \"supports\",\n    \"note\": \"'mar'ca-site, n. [Fr. marcassite, prob. of Ar. origin.] 1. formerly, crystallized iron pyrites, used in the eighteenth century for ornaments … 3. iron disulfide, FeS2, a mineral resembling iron pyrites.'\"},\n   {\"src\": \"SKT\", \"where\": \"SKT.txt, grep marcas/markas/marchas\", \"stance\": \"silent\", \"note\": \"Skeat's Concise dictionary has no entry for the word (see the SKT:314 ref_check above).\"},\n   {\"src\": \"LKT\", \"where\": \"no. 1374\", \"stance\": \"supports\", \"note\": \"'engl. marcasite, dtsch. Markasit \\\"rhombische Modifikation des Eisenkieses\\\"'.\"}\n  ]\n})\n\nentries.append(e3)\njson.dump(entries, open('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/part_b.json','w',encoding='utf8'), ensure_ascii=False, indent=1)\nprint(\"ok\", [len(e[\"nodes\"]) for e in entries])\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk319b.py",
 "description": "Build entries 1 and 3"
}
```


### [2026-09-07T16:09:17.792Z] TOOL RESULT

```
ok [4, 6]
```


## [2026-09-07T16:09:26.773Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; S=/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad; python3 - <<'PYEOF'\nimport json\nS='/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad'\nd=json.load(open(S+'/part_a.json',encoding='utf8'))\nb=json.load(open(S+'/part_b.json',encoding='utf8'))\nd['entries'].extend(b)\n# fix a garbled Persian clause in entry 0 node 5\nbad=\"که متن آن به‌صورت صفحه‌شمار در دسترس برنامی‌نه نیست\"\ngood=\"که متن آن با شمارهٔ صفحه به‌صورت برخط در دسترس نیست\"\nn=d['entries'][0]['nodes'][4]\nassert bad in n['derivation_fa'], n['derivation_fa'][:200]\nn['derivation_fa']=n['derivation_fa'].replace(bad,good)\njson.dump(d, open('/home/sfmqrb/git/rishe/data/verification/page-319.json','w',encoding='utf8'), ensure_ascii=False, indent=1)\nprint('entries', [(e['entry'], e['root'], len(e['nodes'])) for e in d['entries']])\nPYEOF\npython3 -m json.tool data/verification/page-319.json > /dev/null && echo \"JSON valid\"; python3 tools/verify_check.py 319",
 "description": "Merge parts, write file, validate and run check"
}
```


### [2026-09-07T16:09:28.462Z] TOOL RESULT

```
entries [(0, 'Magh 2', 10), (1, 'Maghos, Maghu', 4), (3, 'Mağšîsa', 6)]
JSON valid
nodes verified: 20/20
node verdicts: {'plausible': 5, 'confirmed': 12, 'unverified': 1, 'disputed': 2}
root verdicts: {'confirmed': 2, 'transcription_suspect': 1}
ref checks: {'supports': 16, 'not_checked': 8, 'not_found': 1, 'contradicts': 1, 'partial': 1}
books consulted: {'silent': 15, 'contradicts': 6, 'supports': 25, 'partial': 7} | by book: {'KLN': 7, 'WEB': 5, 'FSD': 4, 'MON': 4, 'LKT': 4, 'DEV': 4, 'WLD': 3, 'SKT': 3, 'HRN': 3, 'BQT': 3, 'BRT': 2, 'POK': 2, 'ARY': 2, 'KNT': 1, 'PHD': 1, 'AHD': 1, 'PLA': 1, 'AFM': 1, 'AFA': 1, 'DOZ': 1}
```


## [2026-09-07T16:09:56.005Z] AGENT

Verification file written and the checker reports 0 problems.

**Page 319 (book p. 289) — 3 non-redirect entries, 20 nodes, all verified**

- Node verdicts: 12 confirmed, 5 plausible, 2 disputed, 1 unverified
- Root verdicts: 2 confirmed (Magh 2, Maghos/Maghu), 1 transcription_suspect (Mağšîsa)
- Ref checks: 16 supports, 1 partial, 1 contradicts, 1 not_found, 8 not_checked (empty boxes with no refs, plus PRT:14 and MON5:58, neither accessible)
- Books consulted: 20 distinct (POK, WLD, AHD/Watkins, IEC, BRT, KNT, KLN, SKT, WEB, FSD, LKT, DEV, DOZ, BQT, MON, ARY, HRN, PHD, PLA, AFM, AFA)

Flagged items:
- **transcription_suspect — ROOT "Mağšîsa : stone" (Aramaic)**: the book's own garbling (`error_in: book`, page image saved to `sources/refs/ocr/BOOK/319.png`). Mo'in's footnote in Borhan-e Qate' p. 1938 n.4 (and Dehkhoda verbatim) has Aramaic مقشیثا *maqšīṯā* in the phrase کیفا مقشیثا "hard stone" — Nourai prints ğ for q and s for ث, and glosses the adjective "hard" as "stone" (kēfā is the "stone"). Modern view: Aramaic *marqəšīṯā* < Akkadian *marḫašītu* < Sumerian Marhaši.
- **disputed — #1 Persian marqašîšâ مرقشیشا**: word and gloss are fine (Borhan/Mo'in: white pyrite for eye-salves), but the arrow Aramaic→Persian is contradicted by Nourai's own BQT:1938 ("the Arabs took it from the Aramaeans … and the Iranians transmitted it as marqašīšā"), by Devic p.157 (the Persian ش-form is a misreading of Arabic ث) and by Wiktionary (Persian form reshaped after شیشه "glass"). Asbaghi and Addi Shir are both silent — telling, since they catalogue Persian words in Arabic.
- **disputed — #2 Arabic marqašîtha**: KLN:937 does say "fr. Pers. marqashishā" (so the chart follows its reference faithfully), but Lokotsch 1374, Devic, Mo'in and Wiktionary all reverse it: Aramaic → Arabic (ث-form attested in al-Rāzī and Jābir) → Persian.
- Notable "plausible" calls: #1 *ha-mazan* is labelled "Avestan / Old Persian" but is unattested in both — Bartholomae has no such entry and Kent's OP lexicon has only *hamarana-* "battle"/*hamarana-kara-*; Watkins himself writes "Hypothetical Old Iranian". Greek Ἀμαζών: Iranian loan is the leading but not certain hypothesis (Etymonline: possibly a non-IE word); the chart's NOTE reports Klein's Hebrew ʾammāṣ correctly, and that derivation is rejected today.
- **SKT:314 = not_found**: Skeat's Concise Etymological Dictionary has no *marcasite* entry at all, and p. 314 of the 1911 ed. is in the "neo-" range (marc- is ~p. 276). Wrong edition or wrong page in Nourai.

No extraction errors: the JSON matches the printed page everywhere, including the two blank pass-through boxes (Latin/French) and the genuinely empty, label-less box hanging off Avestan *mağava* (entry 1 node #2, marked `unverified` — nothing in the book to verify).

Seven web pages archived via `fetch_source.py` (Wiktionary marcasite / مرقشيتا / Ἀμαζών / PGmc *magaþs, Etymonline Amazon, abadis مرقشیشا, vajehyab آمازن). The file `data/verification/page-319.json` is written but not committed.
