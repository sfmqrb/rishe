# Verification process log — verify-page-119


## [2026-09-05T18:02:27.041Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 119 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-119.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-119.json. Write /home/sfmqrb/git/rishe/data/verification/page-119.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 119` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T18:02:28.656Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T18:02:29.381Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T18:02:29.397Z] TOOL RESULT

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


## [2026-09-05T18:02:29.699Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-119.txt"
}
```


### [2026-09-05T18:02:29.727Z] TOOL RESULT

```
1	=== PDF page 119 (book page 89) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Der 1, Derô, Drtis, Drtos : to split, to tear  (refs POK:206; IEC:165)
4	#1 (parent #0) [Avestan] refs=POK:206; SYN:565 | dar 1, dareta : to split ; nîš-dar : a sharp tool for tearing ☞Někš
5	  #2 (parent #1) [Pahlavi] refs=SYN:565 | darîtan : to tear ; dart : pain ; něš-tar : a sharp, pointed tool ☞Někš
6	    #3 (parent #2) [Persian] refs=BQT:848; POK:206; SYN:565 | darîdan «دریدن» : to tear ; dard «دَرد» : pain ; nîšdar «نیشدر» : a tool for cutting | extra: نیشتر
7	#4 (parent #0) [Avestan] refs=POK:208 | dereta : cuts, harvests ; deretô : cut, mown
8	  #5 (parent #4) [Persian] refs=POK:208; HRN:124 | dero «دِرو» : harvest ; dorŭdan «دُرودن» : to harvest
9	#6 (parent #0) [Persian] refs=IEC:165 | dŭl «دول» : animal skin used for carrying water | NOTE: MON & BQT derive this word from Arabic
10	#7 (parent #0) [Avestan] refs=POK:206 | darěna : a cut in earth, ravine
11	  #8 (parent #7) [Persian] refs=BQT:845; HUB:62; HRN:124 | darreh «درّه» : valley
12	#9 (parent #0) [Germanic] refs=AHD | teran : to tear
13	  #10 (parent #9) [English] refs=None | tear 2 : to pull apart
14	#11 (parent #0) [Greek] refs=AHD | der-ma : skin
15	  #12 (parent #11) [English] refs=None | derma, -derm, derma : related to skin ; pachyderm : thick-skinned animals ☞Bhengh
16	--- entry 1 ---
17	ROOT [Indo-European] Drep, Drop, Drap, Drapses : a piece of cloth, banner  (refs POK:211; IEC:159)
18	#1 (parent #0) [Avestan] refs=SYN:396; POK:211; IEC:159 | drafšâ, drafšô : banner
19	  #2 (parent #1) [Persian] refs=BQT:838; HRN:123 | derafš «درفش ٢» : banner
20	#3 (parent #0) [Latin] refs=AHD; IEC:159 | drappus : cloth
21	  #4 (parent #3) [English] refs=None | drape
22	
```


## [2026-09-05T18:02:32.670Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-119.json",
 "description": "Read page 119 source JSON"
}
```


### [2026-09-05T18:02:32.709Z] TOOL RESULT

```
{
  "pdf_page": 119,
  "book_page": 89,
  "entries": [
    {
      "root": {
        "name": "Der 1, Derô, Drtis, Drtos",
        "lang": "Indo-European",
        "refs": "POK:206; IEC:165",
        "gloss": "to split, to tear"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:206; SYN:565",
          "words": [
            {
              "translit": "dar 1, dareta",
              "gloss": "to split",
              "script": null
            },
            {
              "translit": "nîš-dar",
              "gloss": "a sharp tool for tearing",
              "script": null,
              "see": ["Někš"]
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "SYN:565",
          "words": [
            {
              "translit": "darîtan",
              "gloss": "to tear",
              "script": null
            },
            {
              "translit": "dart",
              "gloss": "pain",
              "script": null
            },
            {
              "translit": "něš-tar",
              "gloss": "a sharp, pointed tool",
              "script": null,
              "see": ["Někš"]
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:848; POK:206; SYN:565",
          "words": [
            {
              "translit": "darîdan",
              "gloss": "to tear",
              "script": "دریدن"
            },
            {
              "translit": "dard",
              "gloss": "pain",
              "script": "دَرد"
            },
            {
              "translit": "nîšdar",
              "gloss": "a tool for cutting",
              "script": "نیشدر"
            }
          ],
          "script_extra": "نیشتر",
          "note": null,
          "quote": {
            "text": "پردهٔ پندار می باید درید - توبهٔ تزویر می باید شکست",
            "poet": "Attâr"
          }
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:208",
          "words": [
            {
              "translit": "dereta",
              "gloss": "cuts, harvests",
              "script": null
            },
            {
              "translit": "deretô",
              "gloss": "cut, mown",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "POK:208; HRN:124",
          "words": [
            {
              "translit": "dero",
              "gloss": "harvest",
              "script": "دِرو"
            },
            {
              "translit": "dorŭdan",
              "gloss": "to harvest",
              "script": "دُرودن"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "چو دشنام گویی دعا نشنوی - بجز کِشتهٔ خویشتن نَدرَوی",
            "poet": "Sa`dî"
          }
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Persian",
          "refs": "IEC:165",
          "words": [
            {
              "translit": "dŭl",
              "gloss": "animal skin used for carrying water",
              "script": "دول"
            }
          ],
          "script_extra": null,
          "note": "MON & BQT derive this word from Arabic",
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:206",
          "words": [
            {
              "translit": "darěna",
              "gloss": "a cut in earth, ravine",
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
          "lang": "Persian",
          "refs": "BQT:845; HUB:62; HRN:124",
          "words": [
            {
              "translit": "darreh",
              "gloss": "valley",
              "script": "درّه"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {
              "translit": "teran",
              "gloss": "to tear",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "English",
          "refs": null,
          "words": [
            {
              "translit": "tear 2",
              "gloss": "to pull apart",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {
              "translit": "der-ma",
              "gloss": "skin",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "English",
          "refs": null,
          "words": [
            {
              "translit": "derma, -derm, derma",
              "gloss": "related to skin",
              "script": null
            },
            {
              "translit": "pachyderm",
              "gloss": "thick-skinned animals",
              "script": null,
              "see": ["Bhengh"]
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
        "name": "Drep, Drop, Drap, Drapses",
        "lang": "Indo-European",
        "refs": "POK:211; IEC:159",
        "gloss": "a piece of cloth, banner"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "SYN:396; POK:211; IEC:159",
          "words": [
            {
              "translit": "drafšâ, drafšô",
              "gloss": "banner",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:838; HRN:123",
          "words": [
            {
              "translit": "derafš",
              "gloss": "banner",
              "script": "درفش ٢"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "جهان شد زگرد سواران بنفش - درخشان سنان و درفشان ۱ درفش ۲",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD; IEC:159",
          "words": [
            {
              "translit": "drappus",
              "gloss": "cloth",
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
          "refs": null,
          "words": [
            {
              "translit": "drape",
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


## [2026-09-05T18:02:33.399Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T18:02:33.442Z] TOOL RESULT

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


## [2026-09-05T18:02:39.674Z] TOOL CALL #5: Bash

```json
{
 "command": "ls data/verification/ | head -50 && python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','IEC','SYN','BQT','HRN','HUB','AHD','MON','WLD','BRT','PHD','NYB','CHEUNG','KLN','SKT','ARY']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600])\n\""
}
```


### [2026-09-05T18:02:41.246Z] TOOL RESULT

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
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf
CHEUNG null
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it
```


## [2026-09-05T18:02:47.686Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 214 215 216 217; do echo \"=== leaf $n (printed $((n-8))) ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' POK_01.txt | head -80; done"
}
```


### [2026-09-05T18:02:49.901Z] TOOL RESULT

```
=== leaf 214 (printed 206) ===
cq  1,  251  ff.  hat  gezeigt,  daß  öiddayLO}  ,lehre,  unterrichte'  zu dedae  und  nicht  zu  lat.  discö  (s.  oben  unter  dek-)  gehört.  Daß  auch  da- (als  *dns-)  zu  unserer  Wz.  zu  stellen  sei,  ließe  sich  am  besten  dadurch erklären,  daß  man  annimmt,  aus  öiddayux)  {*di-daa-o%w)  sei  irrtümlich  eine Wurzel  *da-  abstrahiert  worden  (M.  Scheller  briefl.);
vgl.  zuletzt  Schwyzer  Gr.  Gr.  I  307  und  s.  unter  2.  dms-,
WP.  I  793.
2.  dens'  ,dicht'.
Gr.  daavg  ,dicht'  :  lat.  densus  ds.;  der  direkten  Herleitung  aus  *dmu8 widerspricht  nicht  die  Erklärung  von  *d(^w  aus  *dnsö  (s.  oben  unter 1.  dens-)',  allerdings  sind  die  von  W.  Schulze  (Kl.  Sehr.  116 f.)  angeführten Beispiele  von  -a-  aus  idg.  -i^s-  nicht  durchaus  beweisend.  Andererseits kann  davXög  ,dicht  bewachsen'  auf  Sa-vlög  ( :  (jlrj)  zurückgehen,  aber daaxöv  öaav  usw.  wird  kaum  durch  Abstraktion  zu  dd-axiog  ,schattenreich' {*did-GY.iog)  gebildet  sein.  Meillet  MSL.  22,  63   will   das   a  in  daavg  als
203
expressive  Gerainata  oa  erklären  (?).  Über  den   phok.  ON  ^avllg  s.  WH,
Über  alb.  dent  , mache  dicht^,  usw.  s.  unter  3.  dhen-.
Lat.  dönseö,  -ere  (Perf.  densl  nur  bei  Charisius  Gr.-Lat.  I  262^  4)  ,dicht machen^,  Denominativ  von  densus  ,dicht^  (*densos  oder  *dnsos,  event. *denstws).
Hitt.  dassu^  (Dat.  Sg.  ta-as-ht-u-i)  ^stark^
WP.  I  793  f.,  WH.  I  341  f.,  Schwyzer  Gr.  Gr.  I  307.
dcph'  jStarapfen,  stoßen,  kneten*.
Arm.  to'p'el  (-em,  -eci)  ^schlagen';  gr.  öecpo)  ^knete^,  walke^,  argiv.  decpidaatal ^Walker^;  mit  s-Erw.  öhpo)  (Aor.  Partiz.  dexpr^^aag)  ,knete;  gerbe^  (daraus lat.  depsö),  dexpa  ^gegerbte  Haut^;  dicp^ega  ;,Leder^  {*ÖLipT6Qcc)j  serb.  depim, depiti  , stoßen,  schlagen'^,  poln.  deptac  ^treten'^.
WP.  I  786,  WH.  I  342,  Scliwjzer  Gr.  Gr.  I  298,  351.
/.  der-  (:  ddr-,  d^r-)  oder  dör-  :  dor-  ,Spanne  der  Hand^
Gr.  döjQOv  jHandfläche,  Spanne  der  Hand^  (Längenmaß),  öq&ööcoqov  ,der Abstand  von  der  Handwurzel  zur  Fingerspitze^,  hom.  i'AxaLÖsyiddioQog ,16  Spannen  lang^,  tiefstufig  ark.  Akk.  daqiv  aTttda^rjv  Hes.  (lak.  ödosiQ lies,  ist  Feblschreibung  für  öägig^  Schwyzer  Gr.  Gr.  I  506);
alb.  dore  ,Hand-  aus  *dörom  (M.  La  Piana  IF.  58,  98);
aisl.  iari-a  ,ausbreiten^,  ten-a  ds.
Nur  unter  einem  Ansatz  duer-  :  dur-  oder  diiör  :  diidv  :  dur-  lautlich  zu rechtfertigen  wäre  Vergleich  mit  kelt.  dur-no-  in  air.  dorn  ,Faust,  Hand', cymr.  dwrn  ,Hand^,  dyrnod  (mcymr.  dyrnawt)  ,Ohrfeige^,  dyrnaid  (mcymr. dyrneit)  ,Handvoll^  bret.  dorn  ,Hand',  dournek  ,wer  große  Hände  hat'; doch  stehen  diese  Worte  auch  in  der  Bedeutungsfärbung  ,gehallte Hand,  Faust,  Faustschlag^  so  weit  von  den  gr.  ab,  daß  sie  eine  Vereini- gung mit  ihnen  nicht  heischen.
Für  kelt.  *durno-  erwägt  m
=== leaf 215 (printed 207) ===
an  andrerseits  Verwandtschaft  mit  lett.  düre^ düris  ,Faust';  dieses  ist  zu  lett.  duhij  düru,  duft  ,stechen,  stoßen*  zu stellen  (vgl.  piignus : pungo)-  ob  so  auch  kelt.  dur-no-?  Vgl.  Mühlenbach- Endzelin  I  529  und  s.  unter  4.  der-,
WP.  I  794  f.
2.  {der-),  redupl.  der-der-,  drdor-,  gebrochen  redupl.  dor-d-,  dr-d-  ,murren, brummen,  plaudern';  Schallwort. Ai.    dardurd-h    ,Frosch,   Flote*^;    air.  deirdrethar   ,tobt^,    PN   Deirdriu  f. (^der-der-iö)]    bulg.  d^rd&h,   ,schwatze;    murre',   serb.    drdljati    ,plappern', sloven.  drdrdti  ,klappern,  schnarren';
204
mit  gebrochener  Reduplikation:  gr.  ödgda'  ii^liaoa  Hes.,  ir.  dord  ,1 fo-dord  ^Brummen,  Baß^^  an-dord  ,helle  Stimme'  (,Nicht-Baß'),  cymr.  di ^Lärm'  (cymr.  twrdd  ^Lärm'   hat    das   U  von   tiorf  ds.  übernommen), dordaid  ^brüllt'   (vom  Hirsch);   lit.  dardeti,  lett.  dardet,  därdet   ,knarrea^ toch.  A  tsärt-  ^klagen,  weinen'   (Pedersen  Toch.  Sprachg.  19),   mit  seki därer  Palatalisation  seri-  (Van  Windekens  Lexique  145).
Die  kelt.;,  tochar.  und  baltoslav.  Worte  könnten  auch  zu  3.  dher-  gehöre
WP.  I  795,  Mühlenbach-P]ndzelin  I  447.
3.  (der-),  dra-,  dreb-,  drem-,  dreu-  ^laufen^,  treten,  trippeln'.
drä' :
Ai.  dräti  ,läuft,  eilt',  Intens,  ddridrätl  ,sch weift  umher,  ist  arm',  ddri-dr ,umhersch weifend,  bettelhaft';
gr.  äno-didQ&a^u)  ,laufe  weg',  Fut.  ÖQ&ao^iai,  Aor.  HÖqav]   ÖQaGfAÖg^  ion^ SQrja(.i6g  ,Flucht',  äögGarog  ,nicht  zu  entfliehen  suchend',  ögaTteir^g  ,Flücht«;^|| ling',  ÖQGTTsrevcü  ,laufe  davon,  reiße  aus'  (vgl.  zum  -7t-  ai.  Kaus.  drä'payati ,bringt  zum  laufen',  Aor.  adidrapat  [unbelegt]  ,lief');  :f
ahd.  zittaröm  (^di-drä-mi)  ,zittere',  aisl.  titra  ,zittern,  zwinkern'  (ursprüngj lieh  etwa  ,unruhig  trippeln,  zappeln');
vielleicht  hierher  slav.   *dropy  ,Trappe'  (Machek  ZslPh.  17,  260),  poli öech.  dropj  älter  drop{i)a  usw.,  daraus  mhd.  trap(pe)f  trapgans.
dreb-:
Lit.  drehüy  -eti  ,zittern,  beben';
poln.  (usw.)  drabina  ,Leiter';
ags.    treppan    (*trapjan)    ,treten',    mnd.   ndl.    trappen    ,stampfen',    nd( tripperiy  nhd.    (nd.)   trappeln,  trippeln,  mhd.   (nd.)   treppe,   trappe  f.,  nhd.^ Treppe,  ags.   trmppe  f.  ,Falle',  nhd.   Trappel,  ostfries.  trappe,  trap  ,Falle,s Fußbrett';  .        .  '
durch  emphatische  Nasalierung,  wie  in  nhd.  patschen  —  pantschen^ ßcken  —  fiencken  (s.  W.  Wissmann  Nom.  Postverb.  160  ff.,  ZdA.  76,  Iff.) erklären  sich:
got.  ana-trimpan  ,herantreten,  bedrängen',  mnd.  trampen  ,stampfen', mhd.  (ndd.)  trampeln  ,derb  auftreten',  engl,  tramp,  trample  ,treten',  mhd. trumpfen  ,laufen,  trollen'.
drem- :
Ai.  drdmati  ,läuft'.  Intens,  dandramyate  ,läuft  hin  und  her';
gr.  Aor.  eöga^ov,  Perf.  dedgoixa  ,laufen',  dgöfiog  ,Lauf';
ags.  trem,  trym  ,Fußtapfe',  an.  tramr  ,Unhold'  (s.  oben),  mhd.  tremefn ,schwanken',  dän.  trimle  ,rollen,  purzeln',  schwed.  mdartl.  trumla  ds.,  mhd. trame  ,Sprosse  einer  Leiter,  Treppe' ;
205
hierliet-  wohl  die  nhd.  FIN  Dramme  (Gotting-en),  Dremse  (Magdeburg)^ •lus  *Dromiä  und 
=== leaf 216 (printed 208) ===
 *Dro7nisä  (wohl  nordillyr.),  dazu  poln.  (illyr.)  Drama /Schlesien);  bulg.  Dramatica  (thrak.);  s.  Yasmer  ZslPh.  5,  367^  Pokorny Urillyrier  3,  37,  127;
unsicherer  ist  Woods  KZ.  45,  62  Anreihung  von  serb  d'hiati  ,schütteln^, Ji^mnuti  ^erschüttern,  erbeben  lassen^,  sloven.  drmati  ^schütteln,  rütteln^, drdmiti  ,aus  dem  Schlaf  rütteln^,  drävipati  ,unsanft  rütteln^,  cech.  drmlati fitzen,  wirren;  die  Lippen  bewegen,  als  ob  man  sauge^,  drmoliti  ,kurze Schritte  machen^  (dies  in  der  Bed.  gut  passend;  ,schütteln^  aus  ,mit  dem Fuße  anstoßen^?),  drmotiti  ,plaudern'^  (wohl  Bedeutungskreuzung  mit  der Schallwurzel  2.  der-der-,  s.  dort).
dreu-  (z.  T.  mit  ü  als  Tief  stufe,  wohl  auf  Grund  von  ^dreuä^-),  FIN (Partiz.)  dr(o)u(u)entl/iä:
Ai.  drdvati  ,läuft,  auch  zerfließt^,  FIN  Dravanti,  drutd-  ,eilend^,  av. drävaya-  ,laufen^  (von  daevischen  Wesen),  draoman-  n.  , Angriff,  Ansturm^, aesmö-drüt{a)-  ,von  Aesma  her  anlaufend,  zum  Angriff  entsendet^  (sehr unsicher  ai.  di^dvina-m,  drdvinas-  n.  ,Gut,  Vermögen^,  av.  draonah-  n.  ,bei der  Besitzverteilung  zufallendes  Gut,  Vermögensanteil'  etwa  als  ,fahrendes Gut^?);
illjr.-pannon.  FIN  Dravos  {^drouo-s),  daraus  serbokr.  Drdva,  vgl.  apoln. Drawa  (illyr.  Lw.);  idg.  *dyoiient-  ,eilend'^  >  illyr.  *draueiit-  (:  oben  ai.  Dra- vanti)y  daraus  dial.  *trauent-  im  FIN  Tgaevr-  (Bruttium)  >  ital.  Trionto] idg.  *druuent-j  illyr.  *druent-  im  poln.  FIN  Driveca,  nhd.  Dreicenz]  ital. *truent-  im  FIN  Truentus  (Picenum);
gall.  FIN  (aus  dem  Nordillyr.?)  Druentia  (frz.  la  Drance,  Drouance, Durance,  Schweiz,  la  Dranse)'^  *Drutos,  frz.  le  Drot]  Druta,  frz.  la  Droude]
lit.  Seename  *Drüv-inias  (wruss.  Dryiüiaty)]  apreuß.  Bach  Drawe.
Auf  dreu-j  Partiz.  ^dru-to-  beruht  vielleicht  (s.  Osthoff  Par.  I  372  f. Anm.)  got.  trudan  ,treten^,  anord.  troda,  trad  ds.;  ags.  tredan,  ahd.  tretan ,treten^  (bei  Osthoffs  Anschauung  Ablautneubildung),  ahd.  trata  ,Tritt, Spur,  Weg,  Trift^,  as.  trada  ,Tritt,  Spur^,  ags.  trod  n.,  trodu  f.  ,Spur, Weg^  (engl,  trade  ,Handel^  ist  nord.  Lw.),  ahd.  trotaj  mhd.  trotte  f.  ,Wein- presse^.  Intens,    ahd.   trottön   ,treten^;    nhd.   dial.  trotteln  ,langsam  gehend
Hierher  auch  die  germ.  Wz.  *tru-s-  in  ostfries.  trüseln  ,taumeln,  stolpern, unsicher  oder  wankend  gehen^,  trüsel  , Taumel,  Schwindel^,  ndl.  treuzelen ,trendeln,  trödeln*^,  westfäl.  trüseln^  trudseln  ,langsam  rollen^,  mhd.  trollen i^truzlön)  ,sich  in  kurzen  Schritten  laufend  fortbewegen^,  nhd.  trollen, schwed,  mdartl,  trösale  ,Köbold^,  norw.  mdartl.  trusal  ,Tor,  Narr^,  trusk ,verzagter  und  beschränkter  Mensch'^,  sowie  (als  *truzld-)  anord.  ti^oll  n. ,Unhold'^  mhd.  trol,  trolle  m.  ,Kobold,  Tölpel,  ungeschlachter  Mensch' (vgl.   unser  Trampel  in  gleicher   Bed.;   die  Wandalen  nannten   die  Goten
206
Tqovlovg,    Loewe   AfdA.  27,  107);    in   gleicher  Weise  steht  neben   germ,      f tre-m-  (s.  unten)  anord.  tram
=== leaf 217 (printed 209) ===
r  ,Unhold'.  |
Im   Germ,  außerdem    mit    i-Vokalismus    mnd.    trlseln,   westfäl.    trids^ly^      i ,rollen,  taumeln^,  holl.  trillen  ,zittern^  (woraus  ital.  trillare  ^beben,  Trillep schlagen')  usw.  Gegen  Verbindung  von  ai.  drdvati  mit  av.  dvaraiti  ,geht* s.  unter  *dheu-y  *dheuer-  ^stieben^
WP.  I  795  ff.,  Krähe  IF.  58,  151  f.,  Feist  45.
4.  der-,  schwere  Basis  dero-,  dre-  ,schinden,  die  Haut  abziehen,  abspalten  1 spaltend
Ai.  dar-  ,bersten  machen,  spalten,  sprengen*^,  Präs.  der  leichten  Basis' ddrsi,  adar,  ddrtj  w-Präs.  der  schweren  Basis  dfnäti  ,zerspringt,  birst^ Opt.  dfräyät,  Perf.  daddra^  Partiz.  dj-ta-j  von  der  schweren  Basis  dirnd-i Kaus.  darayati,  Intens,  dardirat,  ddrdarti  (vgl.  av.  darddar-  ,spalten'] dech.  drddm,  drdati  , rupfen,  abrupfen'),  dardarlti  ,zerspaltet',  dara-h  mj darl  f.  ,Loch  in  der  Erde,  Höhle'  (:  gr.  dogög  ,Schlauch',  lett.  nuddaraS ^Abfall  von  Bast',  ksl.  razdorb),  dfti-h  m.  ,Balg,  Schlauch'  (=  gr.  ödgatg^ got.  gataürps,  russ.  derth),  darmdn-  m.  ,Zerbrecher'  (:  gr.  Ö€Q(.ia  n.),  wo-] neben  von  der  schweren  Basis  ddriman-  , Zerstörung';  -dätn-  ,zerspaltend^ (==r  gr.  dfJQig),  dära-  m.  ,Riß,  Spalte,  Loch',  däräka-  , zerreißend,  zer-l spaltend',  dari-  in  dardarl-ti,  darl-man-  mit  i  für  1=9  (vgl.  Wacker- nagel Ai.  Gr.  I  20),  kaum  nach  Persson  Beitr.  779  von  der  /-Basis;  npers.| Inf.  diriSarij  darlöan,  jüd.-pers.  darln-iSn]
av.  darddar-  (s.  oben)  ,spalten',  Inf.  ddrdnq.m  ( :  ai.  dxnäti),  Iter.  däraya-, Partiz.  ddrdtö  (=  ai.  dfid-)]
arm.  tefem  ,häute  ab,  schinde,  mache  schwielig'  (wegen  f  wohl  zur  Wzf. *der-s-y  Persson  Beitr.  779  Anm.  1);  unsicher  arm.  tar  ,fremd(es  Land)', tara-  ,außer,  ohne,  fern',  taray  Aor.  ,nahm  Reißaus'  (Persson  Beitr.  778  a  2);
gr.  degct)  ,häute  ab,  schinde',  lO-Präs.  ÖEigcods.  (wie  lit.  derü  neben  diriii), Aor.  Pass.  iddQrjv,  Partiz.  dgaTÖg^  dagrög  (=  ai.  di'td-)]  öogög  ,Schlauch' (=  ai.  dara-j  lett.  nuö-daras)',  ödgaig  ,das  Abhäuten'  (=  ai.  dfti-)j  woneben mit  (geneuerter)  Hochstufe  att.  deggig,  -swg  ,Haut,  ledernes  Kleid,  Decke'; digTQOv,  diss.  öhgov  ,Haut  im  Körperinnern';  degag,  -axog  n.  ,Fell'  (schwere  | Basis?),  deqog  n.,  diqy^a  n.,  öoqd  ^Fell';  dehnstufig  dfiQig,  -log  (poet.)  ,Streit, Kampf  (=  ai.  -däri-)-  hierher  wohl  auch  öag-öalvü)  ,beschmutze'  statt *öaQ-daLQ(o  ( :  ai.  ddr-dar-ti)  ?
cymr.  corn.  bret.  dam  ,Stück,  Teil'  (=  ai.  dirnd-)]
got.  dis-tairan  (=  gr.  öequ))  ,auseinanderreißen',  ga-tairan  ,zerreißen, zerstören',  ags.  teran  ,zerreißen',  ahd.  zeran,  fir-zeran  ,zerreißen,  zerstören'; mhd.    {ver)zern^   nhd.    (yer) zehren   ,verzehren,   verbrauchen',   mengl.,  mnd.
207
terren  ^zanken^,  ndd.  terren,  tarren
```


## [2026-09-05T18:03:01.137Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 218 219 220 221 222 223; do echo \"=== leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' POK_01.txt; done"
}
```


### [2026-09-05T18:03:02.597Z] TOOL RESULT

```
=== leaf 218 ===
  ,reizen;  necken',  ahd.  zerren  ,zerreii'; £0t.  intrans.  dis-,  ga-taürnan  ^zerreißen'  ( :  ai.  drndti),  holl.  tornen  ,sicli auftrennen';  vgl.  nominal  ags.  as.  torn,  ahd.  zorn  ,Zorn,  Streit^  heftiger XjQwille'  und  in  ursprünglichster  Bed.  holl.  torn  ^Spaltung,  Scheidung-^ /_-  ai.  dlrnd-,  cjmr.  darn-j  auch  ai.  dlrnd-  heißt  außer  ^gespalten'  auch verwirrt;  in  Verzweiflung  befindlich');  woneben  hochstufig  anord.  tjgrn f,  (*derna),  tjarn  n.  (*dernom)  ^kleiner  See',  ursprgl.  wohl  ,Wasserloch' (y<r\.  ai.  dara-,  darl  ,Loch  in  der  Erde');  zu  ga-taürnan  trat  kausatives (iteratives)  gatarnjan  ^berauben'  (aber  ahd.  uozurnen  ^verachten'  ist penom.  von  *uo-zorn)'^  got.  gataüra  m.  _,Riß';  gataür^s  i.  ^Zerstörung' (=:  ai.  dfti-,  gr.  öciQGig)'^  anord.  tord-  in  Kompositis,  ags.  tord  n.  ,Kot' (*df-töm  ;Abscheidung',  vgl.  lett.  dirstu,  dlrst  ^cacare',  dirsa  ^der  Hintere', >Iühlenbach-Endzelin  I  470,  und  von  einer  Gutturalerweiterung  mhd. zurch,  zürch  m.  ,Tierexkremente') ;
daneben  von  der  schweren  Basis  anord.  tröd  n.  _,Latten,  Unterlage  aus Stangen'  (*drö-to-7n)j  mhd.  truoder  f.  , Latte,  Stange,  daraus  gefertigtes Gestell';  ahd.  trMa  ,Franse'  (nhd.  Troddel),  mhd.  trödel  (für  Hrädel) jHolzfiber';
eigentlich  zu  der-{e)u-  (s.  unten)  mit  Nasalinfix  gehören  *df-nu-ö  in mhd.  trünne  f.  ,laufende  Schar,  Zug,  Schwärm;  Woge',  ahd.  abe-trunnig, ab'trunne  ,abtrünnig/  ant-trunno  ,Flüchtling',  und  *dren-uö  in  trinnan  ,sich absondern',  mhd.  Irinnen,  traun  ,sich  trennen  von,  fortlaufen',  nhd.  entrinnen (*ent-tr innen),  Kaus.  germ.  *trannian  in  mhd.  trennen  ,schneiden',  nhd. trennen,  holl.  (mit  Umstellung)  tarnen,  tornen  ,trennen'  (letztere  jedenfalls unmittelbarer  aus  *der-  ^spalten'  zu  gewinnen;  das  7in  von  germ.  *trennan aus  -WW-);  sicher  hierher  schwed.  mdartl.  trinna,  trenta  ,gespaltener  Zaun- ständer', ferner  mit  der  Bed.  ,abgespaltenes  Stammstück  als  Scheibe,  Rad' ahd.  trennila  ,Kugel',  trennilön  ,rollen',  mnd.  trint,  trent  ,kreisrund',  trent m.  ,Rundung,  ringsumfassende  Linie',  ags.  trinde  f.  (oder  trinda  m.) ,runder  Klumpen',  mhd.  trindel,  trendel  ,Kugel,  Kreisel'  u.  dgl.
Mit  gebrochener  Redupi.  oder  formantischem  -d-  (vgl.  gr.  dagöccivo)  und Öech.  drdati)  und  aus  ,reißen,  unfreundlich  zerren'  erklärbarer  Bed.  wohl hierher  germ.  *trat-,  *trut-  in  ags.  teart  ,streng,  scharf,  bitter',  mndl.  torten, holl.  tarten  ,reizen,  herausfordern,  trotzen',  mnd.  trot  ,Trotz',  mhd.  tra^, truz,  -tzes  ,Widersetzlichkeit,  Feindseligkeit,  Trotz',  nhd.  Trotz,  Trutz, trotzen,  bair.  tratzen  ,necken';  mit  der  Bed.-Entw.  ,zerfasert'  —  ,dünn,
=== leaf 219 ===
 fein,  zart'  vielleicht  (?)  mnd.  tertel,  tertlik  ,fein,  zierlich,  verzärtelt',  dän. teertet  ,zimperlich'  (vielleicht  auch  norw.  mdartl.  tert,  tart  ,kleiner  Lachs', terta  ,kleine  Spielkugel');  ahd.  nhd.  zart  (letzteres  aus  *dor-tö-,  vgl.  mpers. dart  ,geplagt',  npers.  derd  ,Schmerz'  Wood  KZ.  45,  70);
lit.  diriü  (:  ScIqü}),  zem.  derü  (:  diga)),  dirti  ,schinden,  Rasen  oder  Torf
208
abstechen^  (schwere  Basis  gegenüber  ai.  dfti-^  gr.  dagaig^  ßot  gataii7J^\^ nudh'tas,  geschunden^;,  lett.  nuddara  ,Stange  mit  bekappten  Ästen;  Schnitt^ Brot',  PI.  -as  .Abfälle,  bes.  von  Bast^  (:  Mühlenbach-Endzelin  II  772,  j^j^ dara-j  gr.  dogog),  lit.  dernä  ,Brett,  Bohle^;  mit  «-farbiger  Tiefstufenforu^ lit.  duriü,  dürti  .stechen'  (Prät.  duriau)  =  serb.  ü-drim  {ü-driti)  .schlagen^ (russ.  u-dyrü^  .schlagen'  mit  Iterativstufe  zu-  "^dzr-j  vgl.  lit.  duria^ Berneker  179  f.).  Dagegen  sind  lit.  dufnas  .rasend,  dumm',  lett.  dufns  auj^ dem  Slav.  entlehnt;  vgl.  Mühlenbach-Endzelin  I  519.  ;
Slav.  *derö  und  *diriö  in  aksl.  derg,  dbrati  ,reißen,  schinden'  und  *d\a^ {serh.  zädi^em,  6ech.  dru)',  u-darjg,  u-dariti  .schlagen'   (*(^ör-,  vgl.  "^der^x^ gr.  örjQig),  mit  Iterativstufe  razdirati  .zerreißen',   serb.  iz-dirati  .sich  n)^ mühen   (sich   schinden);   Reißaus   nehmen'   (dazu  aksl.  dira  .Riß';   s.  Ber- neker 201,  wo  auch  über  die  Bed.-Entw.  der  wohl  verwandten  Sippe  serl dira  ,Weg.  den  ein  Heer  gezogen  ist  oder  zieht',  bulg.  dir'a  .Spur  eini Menschen  oder  Tieres,  oder  von  Rädern',  dir\  ,suche,  spüre,   verfolge*) über  *d^r-  in  serb.  ü-drim  s.  oben;
Nomina:  mit  g-Stufe  sloven.  u-d^r  ,Schlag',  mit  o-Stufe  aksl.  razdorb  .Riß, Spaltung'  (=  ai.  dara-,  gr.  öoqog,  lett.  nud-daras),  serb.  ü-dorac  .Angriff, mit  Schwundstufe  (idg.  ^dfto-)-.  serb.  ksl.  razdrtth  .zerrissen',  klr.  dertyj .gerissen,  geschunden'  (=  ai.  dfta-)]  idg.  *drti-:  russ.  derh  .Überbleibsel von  geschrotetem  Getreide.  Kleie;  Rodeland'  (==  ai.  dfti-  usw.);  russ. (usw.)  dern^  .Rasen'  (:  ai.  dlrnd-  usw.,  Bed.  wie  in  lit.  dirti  ,Rasen  ab- stechen'): russ.  dermo  ,Lumpenzeug,  Untaugliches,  Kehricht,  Schmutz' (*Abfall  beim  Spalten,  Abschälen),  derkij  ,rasch,  geschwinde',  dranh  f. .Dachschindel,  Latte',  drjanh  =  ^dermö',  drdka  ,Schlägerei',  drac  ,Nagel- zieher',  o-driny  PI.  .Spreu'  usw.
Mit  l-  erweitert  lit.  nu-dirliotl  ,die  Haut  abziehen',  serb.  drljäm^  diljati .eggen',  drljlm,  dfljiti  .entblößen'  (Berneker  255);
toch.  AB  tsär-  .trennen',  tsro
=== leaf 220 ===
rye  .Spalt.  Riß'  (Pedersen  Toch.  Sprachg.  19).
d(e)ri-  (:  *derei'?)  nur  spärlich  belegt  (s.  bes.  Persson  Beitr.  779 f.):
Gr.  dgi-j-ivg  .(schneidend,  zerspaltend)  durchdringend,  scharf,  herb,  bitter' {wohl  nach  d^vg  umgebildet  aus  ^dgi-i-iög  oder  -a^ög),  lett.  drisme  .Riß, Schramme',  vielleicht  (wenn  nicht  Ablautsentgleisuug  zu  lit.  dreskiü  auf Orund  von  dessen  Tiefstufe  drisk-)  aus  lett.  driksna  (^'-drlskna)  .Schramme', dratska  ,Zerreißer',   vgl.   Mühlenbach-Endzelin   I  488  f.,  500;
fern  bleibt  ÖQllog  , Blutegel,  Penis',  eigentl.  ,Sch wellender',  zu  dqidovaccv' ■9-dXXovaav  Hes.  (M.  Scheller  briefi.).
Mit  u-Formans  von  der  leichten  (der-eu-)  und  schweren  Basis  {dero-u-, ^dr-u-)  ,zerreißen.  (das  Land)  umbrechen,  aufreißen,  ernten':  doro-uäi df-uä  .Getreideart',  deru-,  de-dru-  usw.  .zerrissene  Haut'.
Mpers.  drüii,  drüdan  .ernten';
209
,       o-erm.  Formen  mit  Nasalinfix  s.  oben  S.  207 ;
hicrliei'  anord.  trjöna  t  [*dreu-n-ön-)  , Rüssel  des  Schweins^  (,aufreißend,
ühlendO;  ^''2/^**  "'  ^^'^  ^^^^-  ^^'^^^  (*dreu-lo-)  m.  ,Scfinauze^  Maul,  Mund, I  *ppo^  nor\v.  mdartl.  müle-trjosk,  -trusk  (* dreit-sko-)  ,Pf erdemaul'  (Falk- Torp  u-  tryne).  Wegen  der  Bed.  unsicherer  ist  Falk-Torps  Anreiliung  unter
oii  i"id  trygle  von  anord.  trauda  , mangeln,  zu  kurz  kommen,  im  Stich lassen'  traudla  Adv.  ;kaum',  iraudr  ,verdrossen^  und  —  mit  ^-Erweiterung ^_  .ic-s.  tT'iician  , fehlen,  ermangeln,  zu  kurz  kommen'  (nengl.  dial.  to  triick fail'    nind.  trüggelen  , betteln,  betrügen');
lett.  drugt  ,sich  mindern,  zusammensinken'  (ir.  drocli,  cymr.  driog  ,karg, •chlecht"'  von  einer  ^-Erw.?,  Mühlenbach-Endzelin  I  505).
ai.  durvä  ,Hirsegras'  {df-iiä)]
vol.  gr.  delph.  daqdra  f.,  thess.  ödgavog  m.  ,Brot'  (*c?ra-),  maked.  dQdf.iig  ds. ;
<rall.  (lat.)  dravoca  , Lolch'  (*drd-u-)]  bret.  draok^  dreok,  cymr.  drewg <ls.  sind  aus  dem  Roman,  entlehnt  (Kleinhans  bei  Wartburg  III  158);
mndl.  tarice,  terioe,  holl.  tarioe  ,Weizen',  engl,  tare  ,Unkraut,  Lolch, Wicke'  (germ.  'Ha^-uö,  idg.  *dorduä)]
lit.  dlrva  , Acker'  (*c?r-wä,  mit  Intonationswechsel  der  ä-Stämme),  eigentl. , Aufgelockertes',  dirvönas  ,ehemaliges,  jetzt  als  Wiese  benutztes  Ackerland' (vo'l.  zur  Bed.  russ.  mdartl.  dor  ,Neubruch,  Rodland',  rözderth  ,urbar  ge- machtes Land'),  lett.  druva  ,der  bestellte  Acker,  Saatfeld'  (Mühlenbach- Endzelin  I  470,  505),  russ.  (s.  Berneker  186)  derevnja  ,Dorf  (ohne  Kirche); Landgut',  mdartl.  ,Stück  Feld',  pdset  derevnj
=== leaf 221 ===
u  ,bestellt  das  Feld';
mit  der  Bed.  ,Hautausschlag'  (,sich .  absplitternde  Hautschuppen,  rissige Haut'):
ai.  dar-dru-  m.  ,Art  Hautausschlag',  dar-dü-  m.  (unbelegt),  da-drü-  m., da-dru-ka-  m.  , Aussatz';
lat.  derhita  f.  ,Flechte'  ist  Lw.  aus  gall.  *dei^eta  (vgl.  auch  mir.  deir, air.  "^der  aus  *dera  ,Flechte'),  zu  cymr.  tarwyden,  tarwden  (PL  tarived) (neben  darwyden  durch  Einfluß  der  Präfixgruppe  t-ar-,  Pedersen  KG.  I 495),  mbret.  dervoeden,  nbret.  deroueden  ,Flechtenübel'  (^deru-eit-)\
germ.  *te-tru-  in  ags.  teter  , Ausschlag',  ahd.  zittaroh  {*de-dru-ko-s  =  ai. dadruka-),  nhd.  Zitterich  , Ausschlag';
lit.  dedervinZ  ,flechtenartiger  Ausschlag'  (Trautmann  47,  Mühlenbach- Endzelin  I  450;  vgl.  in  ähnlicher  Bed.  von  der  Wzf.  *der-  öech.  o-dra, PI.  o-dry  ,Friesel,  -n',  poln.  o-dra  ,Masern',  von  der  ^-Erweiterung  bulg. dHgm-se  ,reibe  mich,  jucke  mich,  werde  krätzig');
dereg- :
Mndl.  treken  st.  V.  ,ziehen'  und  ,schaudern',  ahd.  trehhan  ,schieben, stoßen,  stoßweise  ziehen,  scharren,  scharrend  verdecken',  Hrakjan  in  mnd. trecken  ,ziehen  (tr.  intr.)',  ags.  trceglian  ,to  pluck',  womit  wegen  der  gleichen
14
210
Vokalstellung  vielleicht  lett.  dragdt  ,zerren,  reißen,  erschüttern,  schütteli^ draguls  , Fieberschauer',  dräga  ,eine  starke  zornige  Person,  die  viel  leistet und  viel  verlangt'  zu  verbinden  ist;  lett.  drigelts,  drigantSj  lit.  driganta^ ,Hengst'  sind  Lw.  aus  poln.  drygant]  vgl.  Büga  Kalba  ir  s.  128,  Mühlen, bach-Endzelin  I  498.
deregh'  (s.  Persson  Wzerw.  26,  Berneker  254  und  212  m.  Lit.) ;
Ags.  tiergan  (germ.  *targian)  ,necken,  reizen',  mnd.  tergen,  targen  , zerren reizen',  hoU.  tergen,  nhd.  zergen  , ziehen,  zerren,  ärgern',  schwed.  mdartl. targa  ,mit  den  Zähnen  oder  einem  schneidenden  Werkzeug  zerren',  norw. mdartl.  terga  ,necken';  lit.  dirginu,  dirginti  ,(den  Hahn  des  Gewehres) spannen';  russ.  dergath  ,zupfen,  ziehen,  reißen'  (usw.),  sü-doroga  ,Kramp['.
derek- :
/dqsKavov  Name  eines  Vorgebirges  in  Kos  (wie  JgeTtavov  mehrfach  als Name  von  Vorgebirgen,  Bugge  BB.  18,  189),  öög-^ai'  xovldsg,  öeq-kvIIelv olaoTTOtBLv  (eigentlich  ,die  Haut  aufreißen*  Avie  gleichbed.  ösqiivXXblv)  Hes.-
gr.  doQTTog  m.,  öÖQTtov  n.  , Abendessen'  (*c?or/c-f  wo- Formans)
=  alb.  darke  ,  Abendessen,  Abend*  (unklar  die  Ablautverhältnisse  in dreke  , Mittagessen*;  vgl.  Persson  Beitr.  859');  vielleicht  zum  (nordillyr.?) ON  Jgcxy.oviva  (leg.  JagxovLva?)   in  Württemberg,   als   ,Ort  zum   Rasten';
sloven.  drkam,  drcerrij  drkati  , gleiten,  glitschen,  auf  dem  Eise  schleifen; rennen,  Trab  laufen'  (wohl  aus  , Reißa
=== leaf 222 ===
us  nehmen'),  öech.  drkati  , stoßen, holpern*,  bulg.  dircam,  dHcm  , ziehe,  riffle  Flachs,  Hanf  (Berneker  255, Persson  Beitr.  85,  359).
deres- :
Arm.  terem  (s.  oben  unter  der-)]
mir.  dorr  ,Zorn',  dorrach  ,rauh,  grob'  (s.  Persson  Beitr.  779  Anm.  1);
vermutlich  ags.  teors,  ahd.  zers  ,penis',  norw.  ters  , Nagel';  auch  anord. tjasna  f.  ,Art  Nagel'  aus  *tersnö7i'?,  norw.  trase  .Lappen,  Lumpen*,  trasast , zerfasert  werden',  tras  , Reisig',  trask  , Abfall,  Plunder';
sloven.  drdsati  , auf  lösen,  trennen*,  cech.  drdsati  , kratzen,  ritzen,  streifen*, drasta,  drdsta  , Splitter,  Fetzen;  Gewand',  draslavy  ,rauh,  holprig',  tief- stufig drsen  ,rauh',  drsnaty  ,holprig'  (vgl.  oben  mir.  dorr).
dre-sk:
lit.  su-dryskii,  -driskaü,  -driksti  ,zerreißen',  dreskiü,  dreskiau^  -dreksti , reißen',  draskaü,  draskyti  iter.  ,zerreißen',  lett.  draskät  ds.,  draska , Lumpen',  lit.  drekstlne  lentä  ,gerissene  Latte,  dünn  gespaltenes  Holz' (Leskien  Abi.  325,  Berneker  220,  224).
bulg.  drdskam,  drd.H^  (*drascg)  ,kratze,  scharre;  liege  an,  sorge  um', perfektiv  drdsm  (^draskng);  draska  , Kratzer,  Riß*;  cech.  alt  z-dfies- kati  und  (mit  Assimilation  des  Auslauts  an  den  tönenden  kn\B.\it)  z-dfiez-
211
.    .•    zerbrechen',    df-ieska,   dfiezha  , Splitter,  Span',    heute  drizha    ,Span*; ^oxJdrzazga  ,SpHtter';
^,{\t  formantischem  -p-:
drep-,  drop'i
A».  drapi-h  m.  ,Mantel,  Kleid',  drapsd-h  m.  , Banner  (?)*  (=  av.  drafsa-
F-ihne,    Banner'),    Ht.    dräpanos    f.  PI.    ,Weißzeug,    Kleider',    lett.    dräna
}\vohl    *dräp-na)    ,Zeug',    Tuch';    gallorom.    drappus    ,Tuch'   (PN  Drappö,
Dnippus,  Drajppes,  Drapönus)    ist   wohl   ven.-ill.   Lw. ;    der    a-Vokal    aus
iJcr.  0  oder,  wie  das  -pp-,  expressiv;
cry.  öoSTtu)  ,breche  ab,  schneide  ab,  pflücke',  dqeTtdvrj,  ÖQSTtavov  , Sichel', auch  ÖQdnavov  (daraus  alb.  drapen  ds.),  das  durch  Assimilation  von dgsTtavrj  zu  *ÖQa7tdvr]  zu  erklären  ist;  o-stufig  Sqcütivcü'  diaxÖTtTw  Hes. (=r  serb.  dräpljem),  ÖQCjjia^,  -y,og  , Pechpflaster,  um  Haare  auszuziehen*, Soiorta%it,o)  , reiße  Haare  aus';  anord.  trqf  n.  PI.  ,Fransen',  trefr  f.  PL  ds., ti-eßa  ,zerfasern',  mhd.  trabe  f.  , Franse';
*dröp-  in  russ.  drjdpa-ju,  -th  (mit  unklarem  ja),  dial.  drdpatb,  drapdh kratzen,  reißen',  serb.  dräpam,  dräpljem,  drdpati  , zerreißen,  abnutzen; kratzen',  poln.  drapac  ,kratzen,  schaben,  reiben,  fliehen';
dj-p-,  slav.  "^dwp-  in  bulg-.  dirpam,  perfektiv  dripm  , reiße,  ziehe, schleppe';  serb.  drpäm^  drjpati  und  drplm,  drpiti  , reißen';
bsl.  dreh-,  drob-  , Fetzen,  Kleider'  in  lett.  drebe  f.  ,Zeug,  Kleid,  Wäsche', lit.  drohe  f.  , Leinwand',  dräbanas  m.  ,Lumpen,  Fetzen',  drahüzis,  drohü^is m.  , Kleid';  osorb.  drahy  m.  PL  , Kleiderzeug',  öech.-mähr.  zdraby  m.  PI. ,Lumpen,  Fetzen'  haben  wohl  durch  Einfluß  der  Wz.  *  droh-  (s.  unter dhrehh-)  , zerschneiden,  zerstückeln'  -b-  statt  -p-]
drip- :
Gall.  (ven.-ilL)  PN  Drippia,  Dripp
=== leaf 223 ===
önius  (vgl.  oben  Drappus  usw.);
bulg.  dripa  , Lappen,  Fetzen',  sloven.  dripam  (dripljem),  dripati , zerreißen, Durchfall  haben',  cech.  dripa  , Fetzen',  dripati  , reißen,  zerreißen';
drup- :
Gr.  ÖQVftTO)  , zerkratze',  drroÖQVTiTcOy  -dgvcpa)  (mit  sekundärem  q)  statt  7t, s.  Persson  Beitr.  859)  ,kratze  ab,  schinde  die  Haut  ab',  ÖQvcpi^  ,das  Zer- kratzen, Abstreifen',  dQVTclg  ,eine  Dornenart'.
Zum  Wechsel  von  a:i  :u  in  ,mots  populaires'  vgl.  Wissmann  Nomina postverbalia  162  ff.
WP.  I  797  ff.,  WH.  I  342 f.,  373,  861,  Trautmann  51  f.
derbh'   , winden,    zusammendrehen',    dorbhö-s    , Zusammengedrehtes,    Gras- büschel, Rasen'. Ai.  dibhdti  , verknüpft,  flickt  zusammen,  windet',  Partiz.  sdndxhdha-  ,z\i- sammengebüschelt',    drhdhi-    f.    , Windung,    Verkettung',    av.    ddrdwda-    n.
14*
212
,Muskelbündel',    PL    ,MuskelfleischS    ai.   darhhä-    m.    ,Grasbüscliel,    Gra darbhana-  n.  , Geflecht';
arm.  torn  .axoivlov,  funiculus,  laqueus*  (*dorhh-n-)]
gT.   öaQTtT]   ,Korb'   ist  aus  ^dagcpr]  und  TaQTtrj  ds.  kontaminiert  (Günte IF.  45,  347);
ags.  tearflian  (*tarbalön)  ,sich  rollen*,  ahd.  zerhen,  prät.  zarpta  rej ,sich  drehen,  sich  umdrehen';  e-stufig  mhd.  zirben  schw.  V.  ,sich  im  Kreise drehen,  wirbeln',  nhd.  mdartl.  Schweiz,  zirbehi  ds.,  nhd.  Zirbeldrüse Zirbelwind  (wohl  auch  Zirbel  ,pinus  cembra',  s.  unter  deru-)]  schwach- stufig-  ags.  torfian  , werfen,  steinigen'  (vgl.  drehen  :  engl,  tlirow),  wie  anord. tyrfa  ,mit  Rasen  bedecken',  anord.  torf  n.  ,Torf',  torfa  f.  , Torf  schölle ags.  turf  f.  ,Torf,  Rasen',  ahd.  z'urba,  zurf  f.  , Rasen'  (nhd.  Torf  aus  de; Ndd.);  ags.  ge-tyrfan  ,to  strike,  afflict';
wruss.  dörob  ,Korb,  Schachtel',  russ.  alt  u-dorobb  f.  ,Topf',  dial.  ü-dor^ , schlechter  Topf  (,*mit  Lehm  bestrichener  Flecht werktopf'),  wrusg^ <Zoro6'/c  , krümmen,  biegen';  schwachstufig  *cZb?*6a  in  ymss.  derbd  ,Rodeland Neubruch*,  derbovdth  ,vom  Moos,  vom  Rasen  säubern;  den  Anwuchs  aus- roden', derbith  , rupfen,  zupfen,  raufen',  serb.  drbdcati  , kratzen,  scharren' cech.  drbdm  und  drbu,  drbati  , kratzen,  reiben;  prügeln',  mit  Hochstufe russ.  derebith  , zupfen,  reißen'  (vielleicht  hat  sich  in  letztere  Sippe  eine ÖÄ-Erw.  von  der-  , schinden',  släv.  dero  dwati  eingemischt).  S.  Bernekelr 211,  254  mit  Lit.
WF.  I  808.
der{ep)-  , sehen'?
Ai.  ddrjmna-   m.  , Spiegel';   gT.  dgcoTtduLv,   öqcütctsiv   , sehen'   (mit  Dehn- stufe der  2.  Silbe??).  Vgl.  auch  dodcüj  ,sehe'  und  de^-k-  ,sehen'. WP.  I  803;  zum  Formans  -ep-  vgl.  Kuiper  Nasalpräs.  60  f.
dero-,  drä'  ,arbeiten'.
Gr.  dqdü}  (*dQCcicü)  , mache,  tue^  Konj.  dgöj,  äol.  3.  PL  ÖQälGi,  Aor.  att. edqaaa,  hom.  öoTjaTrjQ  , Arbeiter,  Diener',  ÖQäfia  , Handlung',  dodvog-  egyov, ngä^ig  .  .  .  övraf-ug  Hes.,  dÖQavi^g  , untätig,  unwirksam,  schwach',  hom. �
```


## [2026-09-05T18:03:26.664Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"##### HRN leaf 144-146 (p.123-125)\"; for n in 144 145 146; do echo \"--- leaf $n ---\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' HRN.txt; done"
}
```


### [2026-09-05T18:03:28.347Z] TOOL RESULT

```
##### HRN leaf 144-146 (p.123-125)
--- leaf 144 ---
— 122 —
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
machen* (Hörn); vergl. got. tairan, ahd. zeraii, nhd.
zehren,
phlv. d(irt (vd. 20 (13)), dartak 'geplagt' (AV.); arm.
vergl. trtnm 'betrübt* (?) (Hübsch mann No. 278).
LW\ kurd. bei. (47) dard.
Nöldeke (mündliche Mitteilung) möchte derd zu
np. äzar (No. 20) stellen.
551. darust 'gesund, richtig, duriistl; vergl. tendumstX
aw. ^drva- + asti- gesunden Leibes* , oder wohl
besser drva- + sü- (vergl. aw. ayösti-), wie mir Bar-
tholomae vorschlägt; ap. diiruva- 'gesund'; phlv.
duritst^ durustih; ai. dhncvd- 'fest, bestimmt, bleibend'.
LW. kurd. durust 'wahr'; bei. driist 'voll, ganz,
vollständig' (86); wa/. drust, driist 'ganz, vollständig.
Anders Fr. Müller, WZKM. 5, 66; vergl. aber
unter np. dire/t (No. 548).
552. durust 'rauh, grob, stark, durustt,
ap. iXrfars- 'wagen', adarmans, darsma 'heftig, sehr';
aw. \/dar€S' 'wagen', darsi-; ai. \/dharS', dhfmoii
'J Unter sozen (Öcitc HDJ.
--- leaf 145 ---
— 123 —
Als eine Bestätigung für diese Etymologie dient der
Umstand, dass Herr Prof. Nöldeke mir dieselbe
ebenfalls mitteilte; er war besonders von ai. (Ißtä- in
der Bedeutung *keck, frech' ausgegangen ^).
553. direfS Fahne, Banner'.
aw. drafsa- 'Banner -); phlv. draß^ arm. LW. draus;
ai. drapsd' 'Tropfen*.
oss. LW. (jrisa Tahne (von JStackelberg, Fünf
oss. Erz. 81).
Die ursprüngliche Bedeutung von ar. drapsd- ist
unsicher; Fick, Vorgl. Wörtbch. ^ I, 241, setzt
zweifelnd 'flutend, wallend' als solche an. Np. direfs
soll auch *Blitz, Glanz' bedeuten, vergl. direßän,
direfsiden, jüd.-pers. t^l^E»*!"! (Is. 41, 25) (phlv. draßntk
zitternd', AV. , drafset Bund.); in dieser Bedeutung
scheint ein Zusammenhang mit np. duru/s (so hiutet
die ursprüngliche Vokalisation), diiriiysün, duruyßlden
V
vorhanden zu sein, wie denn auch im 8<ähnäme oft
die Formen in den Varianten durcheinander gehen
(z. B. I, 107 Vers 839). Duriiyß etc. halte ich für
Composita, wohl mit Praep. ati, deren zweites Glied
ruys (No. 610) ist.
551. derniän *Arzenei', vergl. darß (No. 523), dermene'^)
^Absinth'.
i^dhar- 'halten', vergl. aw. drva- gesund'; phlv.
darwan 'Arzenei'.
LW. kurd. af/. bei. (48) darmän,
555. durüd, duröd (8ähn. I, 50 Vers 301, 170 Vers 751),
'Segenswunsch, Gebet'.
*j Vergl. auch SFgnirt^? *Frecliling*.
'-) *Banner', nicht Waife, wie Darmes t et ci-, Et. ir. II, 273 über-
Hetzt. Auch im Sähnäme heisst direfs niemals Lanze'. Mand. LW.
Nii^£»NT1 bedeutet *Kreuz* (Nöldeke, Mand. Gramm. 309 Nore i).
Greldner^s Übersetzung von aw. (jaos drafsö (y. 10, 14J durch
*ein Tropfen Milch* (Metrik, S. 153) ist schwerlich richtig (s. Ausgabe).
^) dramna (Bund), syr. LW. ^^O")*!-
--- leaf 146 ---
— 124 —
aw. droatäl- 'Geisundlieit' ') ; plilv. drüt (Men. ; AV.),
drütik courtoous' (West II, 280).
556. durüclen 'crndtcn\ Praes. diretv-em diretvldeiij durüd
'Erndto', JN^ni ^Erndte' (Is. 9, 2).
aw. vergl. dereta-, adereta- {t/ava-) ^geschnittenes,
gemähtes (sc. Korn)'; päz. drüdan erndten (PPGl.,
Men.).
kurd. dirün, dirütin erndten', dirün 'Erndte*; wa/.
drdw-am.
Das 3 in jüd.-pers. )x5l*n zwingt direivem zu lesen
und mit Spiegel, Arische Periode, 70 gr. Ooftko
'pflücken* zu vergleichen.
557. iliiröy, deröy 'Lüge; unwahr.
ap. drauga- *Lüge*; i\\^\ draoya'\ phlv. dröy, dröy,
LW. kurd, durüy; af/. daröy; bei. davöy^ drög,
n. dröy (49).
558. dnrüne 'Regenbogen'.
skr. drum- 'Bogen' (spät und selten).
bei. drm, drmuk 'Regenbogen* (85); yidg. LW.
drün,
bei. drin beweist, dass die ebenfalls überlieferte
np. Aussprache dnrüne falsch ist, vergl. Hübsch-
mann, ZDMG. 44, 555.
559. derves 'Bettler; arm', deryös (Vis und RämTn, S. 395,
Vers 8), deryös, deryöz, deryöze.
aw. vergl. driyu- 'arm*, fem. driwt- {*driyvJ-),
driwika- {?); phlv. daryöä, daryösih.
Die neupersisehen Formen sind im Einzelnen schwer
zu erklären. Auch derey 'Jammer, Elend', Grund-
bedeutung 'Mangel, Beraubtsein*, dereyä gehören nach
Nöldeke (mündliche Mitteilung) hierher.
560. derre 'Thal, Schlucht'.
aw. darenä- 'Thal, Schlucht'; Adovu, Ptolem. 6, 1
(Spiegel, ZDMG. 32, 721).
») Vergl. Fr. Müllor, WZKM. 5, 352.
```


## [2026-09-05T18:03:39.399Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"##### HUB leaf 71-73 (p.61-63)\"; for n in 71 72 73; do echo \"--- leaf $n ---\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' HUB.txt; done"
}
```


### [2026-09-05T18:03:41.106Z] TOOL RESULT

```
##### HUB leaf 71-73 (p.61-63)
--- leaf 71 ---
— 60 -
527. Np. »lnhdr 'Schutz, Sicherheit, Zuflucht' ist natiirlich
nicht aus az in ddr entstanden, da d hier nicht zu h
werden konnte. Andreas erklart sfinhar aus az m
har von Wzl. har *servare (ZDMG. 47, 704), Fr.
M tiller setzt es = zd. *zaend-hara- *Waflfenschutz'
(WZKM. 8, 96). Die letzte Erklarung scheint mir
die beste. Zum Gebrauch von zmkdr als Interjektion
gi^b acht* vgl. d. Achtung!, mhd. wafenl etc.
528. Nach Noldeke ddSn, wie es der Etymologie ent-
spricht.
534. Arm. catiacem *kenne' gehort nicht hierher. Der In-
finitiv ddnistan ist aus dem Praesens danam neu
gebildet, wie uberhaupt alle hier angefuhrten irani-
schen Formen zum Praesensstamm iran. zdna- = np.
dana- gehSren. Vgl. dazu unten Nr. 793.
538. Np. ddh nach Vullers = 'ancilla, serva, famula.
540. Arm. dpir setzt phi. diplr voraus und macht mir
Horn's phi. dipivar nicht wahrscheinlich. F r. M u 1 1 e r
fuhrt (WZKM. 7, 376) np. dwdn ^Tribunal' auf phi.
*attvdn = arm. atean zuruck, was ich nicht fur richtig
halte. Np. daftar, arab. LW. daftar, diftar — gr.
SKp^iga (Noldeke).
541. Armenische Frauennamen mit duxt sind haufig, nur
gerade Tigranaduxt kommt meines Wissens nicht vor.
542. Zu skr. daksa- gehSrt daksina- *tuchtig, recht* = zd.
dasina-. Also ware skr. daksa- = zd. *dasa' = np.
das (nicht daooS), Vgl. Fr. Muller, WZKM. 8, 94.
546. Np. dar 'hinein, in' aus andar wie darun aus andarUft,
darx^'ar aus andarx^ar. Vgl. deutsch raus = heraus,
rein = herein u. s. w.
547. Die Gleichung paz. np. der lange = ap. darga- wider-
spricht den Lautgesetzen , scheint aber gleichwohl
richtig. Ich vermute Umstellung von ap. darga- zu
^dagra- = ^dayra-, das zu der wurde wie zd. anayrandm
= phi. np. aneran^ zd. tiyri- = np. t%r ist.
548. Etymologie dunkel.
550. Etymologie dunkel.
--- leaf 72 ---
^ 61 —
551. Aus ap. *duruva8ti' ware np. durost geworden, vgl.
dur6d (Nr. 555) aus *duiruvata;t'. FUr skr. drdhd- 'fest,
hart, stark, dauerhaft, ganz' (WZKM. 7, 374) = zd.
^dareida- oder *dareSta^ ware im Persischen *dis^ zu
erwarten. Ich kann np. durust ganz, voUstandig,
richtig, wahr, gesund*, paz. durust, drust ganz, voU-
standig Min. Gl. 66 (LW. bal. drust^ afgh. drast ganz,
vollstandig' u. s. w.) nur auf ein iran. "^drusta- = skr.
*drutta-- u. s. w. zuriickfiihren.
552. Np. duruSt rauh, grob, derb, hart (afgh. LW. durust
'rauh, hart streng, miirrisch) setzt ein iran. ^drusta^
voraus. Aus ^drsta^ (= skr. dhr^fd^ *keck, frech*) ware
np. *dist geworden.
553. Sicher ist hier nur die Gleichung: np. dirafS = phi.
drafs = arm. draus =■ zd. drafSa- Banner, Fahne.
Die Vermutung uber die Etym. von np. duruxs ist sehr
ungliicklich. Np. dirafStdan *to flash' JRAS. 1894,
p. 461.
554. Zu damidn *Heilmittel, Mittel* gehort auch arm.
LW. darman *Verpflegung, Pflege, Nahrungsmittel,
Proviant, Futter (ursp. Tnterhalt* von Wzi. dhar
*halten).
555. In den citierten Versen reimt durod SLuf furdd und
xod, aber im Paz. erscheint drud (Min. Gl. 64, Shk. 242).
Das Wort gehSrt zupadrUd (Horn Nr. 288), das bei
Fird. I, 167, v. 689 auf pUd *subtemen', nach N5ldeke
meist auf WSrter mit -ud (wie numud) reimt. Dazu
arm. LW. druat in druati-R 'Lob, Preis, Lobeserhebung ,
druatem lobe, preise'.
556. Np. durudan, diravtdan ernten, mahen, schneiden',
(Fird. I, 18, 12; 22,49), praes. diravam weistauf eine
Wurzel iran. drU. Will man das Wort zu gr. ipenw
stellen, muss man annehmen, dass ein mittelp. *draftan :
*drawam spater nach der Analogic von Verben wie MnU-
dan : sinavam zu durudan : diravam geworden ware.
Ich haJte aber diese Annahme fiir bedenklich (vgl. paz.
drUnend 3. pi. 'sie erndten' Min. 62, 21) und verweise
--- leaf 73 ---
^ 62 —
wegen der jiid. pers. Form auf Nr. 598: dSwdna = np.
devdna mit w fiir urspr. v.
559. Das Verhaltnis der verschiedenen Formen ^) zu einander
sowie die Etymologie bleiben dunkel. Ebenso bleibt
mir die Etymologie von dirBy *Verweigerung, Wider-
willen, Kummer , das Horn mit N old eke hier-
her, F r. M u 1 1 e r zu got. idreiga *Reue stellt, zweifel-
haft. Auf keinen Fall gehort zd. driwt- und driwika-
hierher, das fem. von driyu- arm' lautete drlm-
ys. 57, 4, 10.
560. Wenn zd. darencL- zur Wzl. skr. dar 'bersten, spalten'
gehort (got. gatalran, hd. zehren, zerren), ware es von
got. dal = hd. Thai zu trennen.
561. Aus ap. draya- oder drayah- wurde phi. drayaky
daraus np. *draya, das mit Umstellung von ra zu ar
(vgl. farman aimframan u. s. w.) zu da/ryd wurde. Aus
ap. daryah- ware phi. *darydk = dBrdk (vgl. jiid. tat.
deiroh 'Meer, Miller p. 65) = np. *dera geworden.
562. Ap. *dartanaiy, pr. *drndmiy (skr. drnCtmi) wurde zu
mp. = *dartan : *dirram (vgl. bal. diray, dinay), daraus
*dartan : darram und mit Neubildung des Inf. naeh
dem Praesens: darrldan (dartdan): darram {dar am).
Der Farhang i. Sh. fiihrt auch dirldan auf. Dazu als
ptc. pr. daranda, diranda = afgh.LW. darindq Veissend'
(Tier).
563. Die Regel : ap. d aus iran. z =^ rv^, z (im Inlaut) lasst
sich nicht begriinden. Die Formen di» und dez konnen
dialectisch sein (wie dez in den erwahnten trans-
oxanisehen Ortsnamen) oder miissen auf ap. "^diza-,
^daiza- zuruckgefiihrt werden. Im Pers. wechselte z
mit d aus z in denselben Wurzeln, vgl. donam neben
farzcLna (= phi. frazdnak) ; maltdan (von mard- aus
marz) neben mitstan (von mrz) u. s. w. Oder sind auch
*) Im Phi. und Paz. ersoheint daryoi (Min. GH. 55, 8hk. 241,
Gl. and Ind. 264 etc.), das auf ftlteres *driy68 (aus *driy5s?) zuruck-
gehen muss.
```


## [2026-09-05T18:03:51.058Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"##### SYN leaf 589 (p.565)\"; awk 'BEGIN{RS=\"\\f\"} NR==589' SYN.txt; echo \"##### SYN leaf 420 (p.396)\"; awk 'BEGIN{RS=\"\\f\"} NR==420' SYN.txt"
}
```


### [2026-09-05T18:03:52.671Z] TOOL RESULT

```
##### SYN leaf 589 (p.565)
discussed here in 9.14 ff,
536
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
Ph i Se ee op
wo
Digitized by Arya Samaj Foundation Chennai and eGangotri
{JSCELLANEOUS PHYSICAL ACTS, ETC. 537 -
: 9.942 Dury
(as Artist) 9.943 Firrine, SurraBLe PAINTER E 966 PAINTING, icru® 9.95 Can, May 987 (sb.) , 9.96 Hasy nT : (@ 988 Fe (vb. ‘Paint 6 House’) 9.97 Dirricuir 989 Tans 9.98 Try! (Make Trial of, Test) v BE 9.99 Try? (Attempt, Endeavor) Me pecow® 9.992 Way, MANNER a NzED, ‘im 9.993 HarrEn T, UST 9,94 QuGH ? 911 DO, MAKE ; Goth. taujan, waurkjan Lith. (pra)daryti, veikti
Grk. xptigow, wove ON gér(v)a Lett. darit NG xhvw, oridv Dan. gére ChSl.  tvoriti (délati) Ist. facere, agere Sw.  gora SCr. Giniti, raditi, praviti I. fare OE don, (ge)wyrcan, Boh.  Ginili, robiti, délati R — Jaire macian Pol. czynié, robid, dzialaé Sp. hacer ME _ do(ne), make, wirche Russ. delat’, tvorit' pia ist a NE do, make ren Lg : i Du. doen, maken Vv. tara-, varaz~ NIr. il Pad OHG  tuon, wirken, mahhon i Ae (1 sg. gran) MHG tuon, machen ‘ NHG tun, machen
Words for ‘do’ and ‘make’ are treated together because these most generic no- tions of action are so commonly ex- pressed by the same word; and where there are pairs of words, roughly dis- tinguished by the feeling for the action itself or the implication of result respec- lively, the idiomatic differentiation is never quite the same for different lan- Guages and periods, not even in the case of such closely allied pairs as NE do, ees tun, machen; (cf. NHG
ian a is he doing?) ation from a a. e Test on generali- 28 ‘place ae variety of notions, Teady’, Bs & esa » ‘make 'ause to be ee ep get through’,
for a Wider esp work .
of the lesg Nee vey, Including many Sons not Mentio alternative expres- Aipead ree ef. Yoshioka, Languages ae in the Indo-
TE *ghz. « Cago diss.). » Crk * Place, put’, in Skt. * ln, Lith déti, ChSl. déti z ? . détz,
etbs of , Euro
CC-0. In Public Domain.
etc. In these the prevailing meaning is still ‘place, put’, but the sense of ‘make’ is occasional in Indo-Iranian, rather fre- quent in Greek, and develops in Slavic. ‘Do, make’, prevails from the earliest times in Italic, and also in the WGme. group, though here with considerable survival of ‘put’. Walde-P. 1.826 ff. Ernout-M. 325. Walde-H. 1.440 ff. Berneker 194.
Lat. facere (> Romance words), Ose. fakiiad, Umbr. facia ‘faciat’; OE don, ME done, don, do, NE do, Du. doen, OHG, MHG tuon, NHG tun; ChSl. (fr. déti) délo ‘work’, whence vb. délati ‘work’, later ‘do, make’ (below, 7).
2. Grk. dw and sé&w, in Hom. the commonest verbs for ‘do’, fr. the same root as épyov, répyov ‘work’, OF weorc ‘work’, etc. (9.12), Av. varaz- ‘work, do’.
Grk. dpdw, in Hom. ‘do service’ (cf. dpnornp ‘laborer’), elsewhere ‘do’ (hence dpiua ‘act’), but mostly poet. : Lith. daryti, Lett. darit ‘do’. Walde P. 1.803.
Grk. rpicow, Att. rparrw, Ion. rpjoow,
Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
538
in Hom. ‘pass through’ (the sea), ‘ac- complish’, in Attic ‘act, do’ (with em- phasis on the action): wépa, 7épav ‘be- yond, across’, etc. Walde-P. 2.32.
Grk. qotéw,
##### SYN leaf 420 (p.396)
l
1. Grk. xpdpvov (Hom.), xpdupvov | ajuin, juin, etc. whence, as if pl., new Sg.
(xpéuvoy Hesych.), dim. xpoupbdiov > NG kpopptd., xpeuptdr : Ir. crem, W. craf, OE hramsa, Lith. kremusé ‘wild garlic’. Walde-P. 1.426. Boisacq 520.
2. Lat. cépa (> Rum. ceapd, OF. cive, Ir. ciap in folichep ‘porrum, capil- losa cepa’, OF ctpe; late dim. cépulla > It. ctpolla, Sp. cebolla, OHG zwibolla, etc. [pop. association with words for ‘two’ and ‘ball’]; MHG zibolle > Lith. cibulé, Boh. cibule, Pol. cebula; MLG sipolle > Lett. stpuols), with Grk. dial. kami’ ra oxopoda. (Hesych.), loanword fr. un- known source. Ernout-M. 176. Walde- H. 1.201. REW 1817, 1820. Vendryes, De hib. voc. 124. Weigand-H. 2.1355.
Late Lat. anid (> OE ynne in ynne- léac, epd. with léac ‘leek’; Fr. oignon > ME unyon, etc. > NIr. inniun, W. wyn- wyn coll., sg. wynwynyn; Br. ognon coll., sg. ognonenn, fr. Fr.; Du. dial.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
grasak ‘pea’), Boh. hraéch, Pol, groch Russ. goroch (coll.; gorogina ‘a pea’) : Skt. ghrs- ‘rub’, ete. Walde-P. 1.695 Berneker 331 f. 4
6. Skt. kalaya-, satina-, both ob
S Uhlenbeck 48, 326. tie
ut), prob. (though disputed) the same word as unié (fr. anus ‘one’) commonly applied to a single large pearl, and so not improbably by farmers to the onion. Ernout-M. 1126. REW 9073. Peder- sen 1.207. Franck-v. W. 12,716.
3. Dan. rédlég, Sw. rédlok, epd. of words for ‘red’ (15.66) and ‘leek’ (ON laukr, OE léac, etc.).
4. Lith. svoginas (now preferred to cibulé, NSB), fr. some Asiatic form be- longing with Turk. svogan ‘onion’. Hehn, Kulturpflanzen’ 205.
5. SCr., Russ. luk, fr. Gmc. word for ‘leek’, ON laukr, etc. Berneker 744. Stender-Petersen 302 f.
6. Skt. palaéndu-, cpd., first part dub., second part : anda- ‘egg’ (cf. andika- name of a plant with edible bulbs). Uhlenbeck 159.
0D AND DRINK; COOKING AND UTENSILS F
Digitized by Arya Samaj Foundation Chennai and eGangotri
373
5.69 CABBAGE
; Goth. ..-- a kopuslas pagaross xpauBn ON ee me tapuosts Gtk: gyav0 . Dan. kaa Ba NG brassic caulis Sw. kal SCr. kupus Lat. cavolo OE cawel Boh.  kapusta, zeli Li chow ME cole, caboche Po}. kapusta i berza, col NE cabbage Russ. kapusta im, vared kool Rum. mi, braissecl ene or vit eabaiste (ca) 1) MHG kal WW, bresychen (caw NHG Kohl (kraut)
Br. kaolenn
4uBn, fr. the appearance of eed : kpauBos “dry, crack- p, ‘blight in grapes when they shriv- Leer ce Wade P. 2,588 f, Boisacq 507. )
Grk. pédavos (Att. for xpauBn), beside jadov's ‘radish’ : pdms, padus ‘a fing. of turnip’, Dor. saga ‘a kind of radish’, Lat. rgpum ‘rape, turnip’, OHG ruoba, NHG (weisse) ribe ‘turnip’, rote riibe ‘beet’, geloe riibe ‘carrot’. Walde-P. 2.341. Emout-M. 852.
’ NG daxavo, sg. of Adxava ‘vegetables’ (5.65).
2, Lat. brassica, etym.? Mostly re- placed in VLat. by caulis, but the source of It. brasca (arch.), Ir. braisse
```


## [2026-09-05T18:04:02.828Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"9\\.28\" SYN.txt | head -20; echo \"-----BANNER\"; grep -n -i \"banner\\|9\\.27 TEAR\\|FLAG\" SYN.txt | head -30"
}
```


### [2026-09-05T18:04:02.902Z] TOOL RESULT

```
2390:Du. geschlachit, MHG geslehte, NHG geschlecht ‘kin, family, clan’ (19.28), orig., like OHG slahta, ‘sort, kind’, whence ‘sex’. Weigand-H. 2.698.
3700:Dan. slegtninge, Sw. sldktingar, de- rivs. of slegt, slakt ‘race, family’ (19.28).
3737:SCr. porodica, Boh. rodina, Pol. rod- zina, derivs. of ChSI. rodi, etc. ‘birth, race’ and ‘family’ in wide sense (19.28).
9882:6. Lith. drabuzis ‘garment’, sg. coll. or pl. ‘clothes’, Lett. drébe ‘cloth, gar- ment’, pl. ‘clothes’ : Lith. drobé ‘linen cloth’, Boh. z-draby ‘rags, tatters’, prob. fr. an extension of IE *der-, in ChSI. dtrati, OE teran, etc. ‘tear’ (9.28), with development fr. ‘rag’ to ‘cloth’, then ‘gar- ment’. Mithl.-Endz. 1.497. Buga, Kalba ir Senové 228. Berneker 219.
14164:7. Skt. kartart- ‘shears’ or ‘dagger, knife’, see 9.28.
14289:9.28 TEAR (vb. trans.)
14363:(9.28), ete. Walde-P. 1.98. Falk-Torp 228.
14372:‘bleach’, also ‘peel’ and ‘flay’ (Gerof s.v.), Sorb. bélié also ‘peel’, Develop. ment apparently through ‘cleanse’ \ ‘scrape off’ > ‘peel, flay’, (cf. history of Fr, déchirer ‘tear’, 9.28). Buga, Kalba ir Senové 28. Berneker 55.
20122:4, Lith. plesti ‘tear’ (9.28), also ‘rob’.
23221:Boh. dira, Pol. dziura, Russ. dyra : ChSI. dirati ‘tear’ (9.28). Berneker 201.
26924:dirati, etc., general Slavic for ‘tear’, Goth. tairan ‘tear’, etc. (9.28). Berne- ker 201.
32741:Russ. rodina, fr. rod ‘descent, race, family’ (19.28).
33036:19.28 TRIBE, CLAN, FAMILY (in Wide Sense)
34369:Russ. drat'sja, refl. of drat’, ChSl. diratt ‘tear’ (9.28).
35393:Lith. is%pléga (NSB, Lalis) : ixplésti ‘tear out, rob’, epd. of pléstz ‘tear’ (9.28), whence also plésimas used for ‘spoils’ in NT, Lk. 11.22 (pl. Trowitsch, sg. Kur- schat).
-----BANNER
1725:2. Lat. fulgur n. (gen. -uris) and fulgor m. (gen. -dris) : fulgére ‘flash’, flagrare “blaze’, Grk. ¢déyw ‘blaze’, etc. Hence It. folgore, Rum. fulger (OFr. fuildre, fouldre, foudre rarely of visual
2078:Ir. daig (MW goddaith ‘great fire, conflagration’, Loth, RC 38.169) : Skt. dah- ‘burn’, etc. (1.84). Pedersen 1.108,
2088:1. From the root of Grk. greyw, Lat. flagrare ‘burn, blaze’, etc. . Walde-P. 2.214. Ernout-M. 666f. Walde-H. 1.518. :
2091:2. Rum. flacdré, fr. *flacula (It. fiaccola ‘torch’), this fr, Lat. facula ‘torch’ (dim. of fax id.) with / fr, flamma, flagrare. Cf. W. ffagl ‘blaze, flame, torch’ fr. Lat. facula. REW 3137.
2163:Grk. ¢déyw, déyouar ‘blaze, burn’ b, gdéyw also ‘kindle’, or ‘burn’ a : dddé ‘flame’, Lat. flamma ‘flame’, flagrare ‘blaze’, etc. (1.82). Walde-P. 2.214.
9098:1. Grk. wdaxots, gen. -obyros (> Lat. placenta), fr. rdaxdeas ‘flat? : mAaé ‘any- thing flat’, ON flaga ‘slab of stone’, NE
9099:flagstone, Lett. plakt ‘become flat’, etc., fr. an extension of the root seen in Lat. planus ‘flat’, ete. (12.7 1). Walde-P. 2.90. After mAaxods was formed a whole Series, tupods ‘cheese-cake’, olvotrra ‘wine- cake’, etc.
9883:Lith. drapanos (pl.; sg. rare) ‘clothes’ : Skt. drapi- ‘cloak, mantle’, Av. drafSa- ‘banner’, ChSI. drapati ‘scratch, tear’, fr. an extension of IH *der- in words for ‘tear’. Here also perh. late Lat. drappus (Fr. drap) ‘cloth’, Walde-P. 1.802. Berneker 220. Walde-H. 1.373. REW 2765.
9949:Lat. pannus (‘piece of cloth’, esp. ‘rag’), Goth. fana (reg. for péxos), OHG fano (NHG fahne like OE fana, ON fani specialized to ‘banner’) : Grk. rjvn ‘thread on the bobbin, woof’, pl. ‘web’,
18254:word fr. the Gme. group OHG mast ‘pole flagstaff’, esp. ‘mast’, OB mest, ON mastr ‘mast’. Stender-Petersen 282 f Walde-P. 2.235 f. (rather as cognate with Gme. group). Walde-H. 2.19.
18649:2. Lat. vélum, orig. ‘cloth’, as ‘gail’ mostly pl. véla (>It., Sp. vela, Fr. voile), prob. fr. *weg-s-lo-m, cf. vexillum dim. ‘ensign, banner’ ; Ir. Sigim ‘weave’, etc., IE *weg-. Walde-P. 1.247, By- nout-M. 1082.
25967:aiyh ® - Diel, Fragmenta Lippe es p. 387), soppaivouar, ut. sole or. oappoHnY sb. dodpnats; ae ie anys ond part : Skt. ghra- ‘smell’; gprs 82° (> Olt. olere, OFr. oloir, Sp. Jat, ol@r Ain odefacere (Festus), sbs. olfactus (> Sp. olfato), odore, Fr. odeur; Sp. olor b.), whence odorart (> It. wiorart); odoratus (> it. odorato, Fr. doral) ; Lith. wostr (1sg. uodéiu), Lett. yost; Arm. hot (sb., obj.), hotim (vb., Doe wvpitw ‘rub with ointment’ (deriv. of pbpov ‘ointment, perfume’), late puplfonae ‘be fragrant with’, whence NG pupitw (pop. ‘smell’ both subj. and obj.), pupifopar (lit. ‘smell’ subj.). Hence also, fr. aor. form, Bulg. mris, SCr. mirisati, and, fr. a parallel aor. lujpwoa (: pupdw), late ChSl. mzrosati, Rum. mirosi, sb. miros. NG pupword formed to late Grk. nupd&dns, cpd. of pipov and the root of 3tw (above, 1), parallel to eiddns ‘fragrant’, etc. 3, Lat. fragrare, VLat. flagrare (> OFr. flairier obj., but Fr. flairer subj. ‘take a smell of, try to recognize by the smell’), prob. : OHG bracko ‘hunting dog’, MHG br@hen ‘smell’. Walde-P. 2.192, Ernout-M. 385. Walde-H. 1.540. REW 3476. Wartburg 3.746 f.
26569:Dan., Sw. blank (of surfaces), fr. MLG blank ‘shining white’ = OHG blanc ‘shining white’ (NHG blank), ON blakkr ‘pale’ : Lat. flagrare ‘flame, burn’, Grk. prey ‘burn, blaze’, ete. Walde-P. 2.215. Falk-Torp 80. Franck—-v. W. 69.
26721:OE blec, ME blak, NE black (as sb. OE blac, OHG blach, OS blak ‘ink’), etym. disputed, prob. : OHG ODlecchen, MHG blecken ‘be visible, let see’, OHG blanc ‘shining white’, Du. blaken ‘burn, glow’, Lat. flagrdre ‘flame, burn’, Grk. gdéyw ‘burn, blaze’, etc., with develop- ment of ‘black’ fr. ‘burnt’ or ‘shining black’(?). Walde-P. 2.215. Falk-Torp 87. NED s.v.
32442:W. llech, lit. ‘flat stone, slat’ : Ir. lecc ‘stone, flagstone’, etc.
```


## [2026-09-05T18:04:13.359Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=9860 && NR<=9900' SYN.txt | grep -n \"\" | head -60; echo \"=== find page marker near 9883\"; awk 'NR<=9883 && /^[0-9]{3}$|^ *[0-9]{3} *$/ {p=$0; l=NR} END{}' SYN.txt; python3 - <<'EOF'\nimport re\nlines=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor target in (9883,14289):\n    for i in range(target,max(0,target-400),-1):\n        m=re.search(r'\\b(3\\d\\d|5\\d\\d)\\b', lines[i])\n        if re.fullmatch(r'\\s*\\d{3}\\s*', lines[i]):\n            print(target,'prev page marker line',i,repr(lines[i]));break\nEOF"
}
```


### [2026-09-05T18:04:15.444Z] TOOL RESULT

```
1:lr. ¢mbrdca ‘clothe’ (6.11). » Pl. ‘clothing’, V, 7).
2:»» above, 1,
3:G; PERSONAL ADORNMENT AND CARE
4:igitized by Arya Samaj Foundation Chennai and eGangotri
5:395
6:Pedersen 1.24), W., Br. dillad, OCorn. dillat ‘clothes’, etym.? Henry 98.
7:Ir. étach, étiud ‘clothes’, NIr. é@adach ‘cloth, clothes’, fr. Ir. in-tuigur, étim ‘clothe’ (6.11). Pedersen 2.514, 655.
8:W. guwisg, Br. gwisk, gwiskamant, above, 1.
9:5. Goth. wasti, above, 1.
10:ON kledi, Dan. kleder, Sw. kldder (pl.) ‘clothes’, sg. ‘cloth’ or ‘garment’, Sw. klddning ‘garment’, coll. ‘clothes’, OE clapes, etc. (pl.) ‘clothes’, sg. ‘cloth’, MHG kleit, NHG kleid, Du. kleed ‘gar- ment, dress’, pl. ‘clothes’, MHG klez- dunge, NHG kleidung, Du. kleeding (coll.) ‘clothing’, fr. words orig. meaning ‘cloth’ (6.21).
11:ON buningr, binadr ‘equipment’ and esp. ‘clothing’, fr. bua ‘equip, prepare, dwell’ : Goth. bauan ‘till, dwell’, OHG, OE buan ‘dwell’, TE *bheu- ‘become, be’. Walde-P. 2.140 ff.
12:ON fot, pl. of fat ‘vessel’ = OF fat, OS fat, OHG faz ‘vessel’, cf. Goth. fétjan ‘adorn’, ga-féteins ‘adornment’ : Lith. puodas ‘pot’, OHG fazzdn ‘hold, contain, prepare’, also ‘dress’. Walde-P. 2.22. Falk-Torp 200.
13:OE gewéde, ME iwede, wede (NE widow’s weeds), OHG giwati, wat, MHG wat (coll.) ‘clothing’, orig. ‘cloth’, cf. ON vad ‘cloth’ (6.21).
14:OE réaf ‘spoils, booty’, but esp. ‘gar- ment’, pl. ‘clothes’ : OHG roub ‘booty’, etc. 20.48).
15:OE hregl ‘garment, robe, cloak’, etc. (NE rail, night-rail, NED), OHG hregil ‘garment’ (rare), perh. through ‘woven piece’ : ON hrel ‘weaver’s reed’, Grk. kpéxw ‘strike, weave’, xpéxn ‘woof’, etc. Walde-P. 1.483.
16:OE scriad ‘dress, clothing, garment’, ME schroud sometimes also general for ‘clothing’ (NE shroud) = ON  skrid ‘ornament, furniture’: OE scréadian ‘cut off, prune’ (NE shred), OHG scrotan,
17:CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
18:Digitized by Arya Samaj Foundation Chennai and eGangotri
19:396
20:etc. Walde-P. 2.586. NED s.v. shroud, sb.1.
21:NE dress, fr. vb. dress (6.11).
22:ME garnement, NE garment ‘an article of clothing’, pl. ‘clothes’ (now rather rhetorical, but garment-makers’ union), fr. OF r. garnement ‘equipment’, deriv. of garnir ‘furnish, equip’.
23:6. Lith. drabuzis ‘garment’, sg. coll. or pl. ‘clothes’, Lett. drébe ‘cloth, gar- ment’, pl. ‘clothes’ : Lith. drobé ‘linen cloth’, Boh. z-draby ‘rags, tatters’, prob. fr. an extension of IE *der-, in ChSI. dtrati, OE teran, etc. ‘tear’ (9.28), with development fr. ‘rag’ to ‘cloth’, then ‘gar- ment’. Mithl.-Endz. 1.497. Buga, Kalba ir Senové 228. Berneker 219.
24:Lith. drapanos (pl.; sg. rare) ‘clothes’ : Skt. drapi- ‘cloak, mantle’, Av. drafSa- ‘banner’, ChSI. drapati ‘scratch, tear’, fr. an extension of IH *der- in words for ‘tear’. Here also perh. late Lat. drappus (Fr. drap) ‘cloth’, Walde-P. 1.802. Berneker 220. Walde-H. 1.373. REW 2765.
25:Lith. rubaz (pl.) ‘clothes’ (formerly the usual word), fr. WhRuss. rub = ChSI. rabi ‘cloth’ (6.21).  Briickner, Sl. Fremdworter, 128.
26:Lith. aprédas, aprédalas (sg. as coll.) ‘clothing’, fr. aprédyti ‘clothe’ (6.11).
27:Lett. apg’érbs (sg. as coll.) ‘clothing, costume’, fr. apg'érbt ‘clothe’ (6.11). Also Lith. abgerbas ‘a suit of clothing’.
28:7. ChSl. odezda (odéa, odénije), SCr. odjeéa, odijelo, Boh. odév, Pol. odziez, odzienie, Russ. odezda (coll.), fr. ChSl. odéti, odéjati, etc. ‘clothe’ (6.11).
29:CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
30:SELECTED INDO-EUROPEAN SYNONYMS
31:ChSl. riza, translating Suna, éoOns, xiTwy, and dOdrmop (Jagié, Entstehungsgesch. 392) : Russ riza ‘chasuble’, Bulg. riza ‘shirt’, Boh. Fiza ‘a long garment’, Lith. ryzai ‘rags? (borrowed), otherwise obscure, Miklo. sich 279.
32:SCr. ruho, Boh. roucho, Pol, Tucho ‘garment, clothing’ (OPruss, rikat ‘clothes’ fr. Pol.), Bulg. roucha ‘cloth’ late ChSI. rucho ‘load, cloth, Spoils’, te orig. ‘spoils’, fr. the root in ChSI. rusiti ‘wreck, destroy’, Lith. raustz ‘root up’, etc., IE *reu-s-, extension of *reu-, Walde-P. 2.356. Briickner 467, Hence NG podxa ‘clothes’, Rum. rufa, ‘soiled clothes’.
33:SCr. haljina ‘garment’, pl. ‘clothes’ : halja ‘dress, coat’, Bulg. halina ‘long up- per garment’, fr. Turk. hal: ‘carpet, rug’. Berneker 383.
34:Boh. Sat, Pol. szata ‘garment’, pl. ‘clothes’ (now more common in Boh, than in Pol.) orig.? Briickner 542.
35:Boh. oblek ‘garment, suit of clothes’, fr. oblékati ‘clothe’ (6.11).
36:Pol. suknia ‘garment’, pl. ‘clothes’, fr. sukno ‘cloth’ (6.21).
37:Russ. plat’e (also esp. woman’s dress) : ChSl. plati ‘cloth’ (6.21).
38:YHA, tuaroy ‘linen cloth?
39:8. Skt. vasana-, Av. vavhana-, Skt., Ay. vastra-, above, 1.
40:Skt. cela~ ‘garment, clothes’, fr. cil- (rare) ‘put on clothes’, etym. dub., perh. : Lith. kailis ‘hide, pelt’. Uhlen- beck 93.
41:igitized by Arya Samaj
=== find page marker near 9883
9883 prev page marker line 9877 '396'
14289 prev page marker line 14279 '565'
```


## [2026-09-05T18:04:19.639Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=14279 && NR<=14380' SYN.txt"
}
```


### [2026-09-05T18:04:21.422Z] TOOL RESULT

```
igitized by Arya Samaj Foundation Chennai and eGangotri
565
oxantw ‘dig’, etc. Briickner 543.
Pol. tupaé (also Ukr. tupaty ‘split’) : tupié ‘peel, flay, plunder’, Boh. loupatz, -itt ‘peel, plunder’, Russ, lupit’ ‘peel’, SCr. lupiti ‘strike a blow’, Lith. lupti ‘peel, flay’, Goth. laufs ‘leaf’, ete., perh. Skt. lup- ‘break’, Walde-P. 2.417 £. Berneker 746.
Russ. kolot’ : Chl. klati ‘stab, slay’, Boh. klatz ‘stab, split’, Lith. kalti, Lett. kalt ‘strike, forge’, ete. Walde-P. 1.438. Berneker 551 f.
7. Skt. bhid- : Lat. Jindere, above, 2.
Av. dar- : Skt. dr- ‘burst, tear, split’, Grk. dépw ‘flay’, OF teran ‘tear’, etc., IE *der-. Walde-P. 1.797 ff.
Skt. chid-, Av. sid- : Grk. above, 1.
Walde-P. 2.559 ff.
oxifa,
9.28 TEAR (vb. trans.)
Grk.  craphoow Goth. tahjan, distairan Lith. plegti, dréksti NG  tecxitw ON rifa, slita Lett. plést, draskat Lat. scindere Dan. rive ChSI.  dtrati It. _stracciare Sw. riva, slita SCr. _ kidati, trgati Fr. déchirer OE teran, slitan Boh. _ irhati, rvati Le rasgar, desgarrar ME lere, rende, ryve Pol. drzeé, rwaé ot ae NE tear (rend) Russ. vat’, drat’ ao ‘ Du. scheuren Skt. dy- v a 8()racaim OHG - slizan, zerran, rizan Av. nis-dar Bn ee MHG slizen, zerren, rizen NHG reissen Words for
‘tear’ are used, part] dis- creished by prefixes, for ie sieves Pleces’ or for ‘tear off? (from the main Tn the latter Sense they overlap Snatch, pluck, ete.’ & ords that may be rendered a eee expression for the €nce’ and do not eet ‘tear’ are not Laas iri a : of the words, though listed » Af€ more Commonly used zerreissen, Russ - ‘tear apart’, Words for ‘tear’ and
‘tear off
1h tgp,
‘flay’ (9.29). Walde-P. 1.797 ff. Feist 120. Berneker 185.
Here as ‘tear’ : Goth. dis-tairan ‘tear, burst’ (leather bottles, where Grk. biyvunt; also ga-tatran ‘destroy, break’), OE teran, ME tere, NE tear, OHG zer- ran, MHG zerren (NHG ‘tear off, pull, tug’; OHG fir-zeran ‘destroy’, NHG verzehren ‘consume’); ChSI. dirati, Pol. drzeé, Russ. drat’, dirat’ (SCr. derati, Boh. drati mostly in secondary uses); Skt. dr- ‘burst, tear’ Av. niSdar- ‘tear out’ (Barth. 689). Cf. also Toch. tsar- ‘separate’ (SSS 483).
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
| Digitized by Arya Samaj Foundation Chennai and eGangotri
SELECTED INDO-EUROPEAN SYNONYMS
566
2. Grk. craphoow (orapay- as in ond- payne ‘a piece torn off’, emapaynds ‘a tear- ing, rending’) prob. with connection through ‘noise of tearing’ : Skt. sphiij- ‘rumble, crash’, Lith. spragéli ‘crackle’, etc. (Walde-P. 2.672 ff., but crapacow separated, 2.668). Persson, Beitrige 869.
NG tecxitw, cpd. (with ge- for é&- as reg., fr. é&e in augmented forms) of oxltw ‘split’ (9.27).
3. Lat. scindere (also ‘split’) : Grk. oxite ‘split’, etc. (9.27).
It. stracciare, with OF. estracier ‘tear’, fr. *extractiare (influenced in use by dis-) : Lat. extrahere, distrahere, epds. of trahere ‘draw, pull’. REW 2692. Wartburg 2.331.
Fr. déchirer, cpd. form of OF’. eschirer, prob. fr. a Frank. *skiran : OE sciran ‘make clear’ (: OE scir ‘clear, bright’, etc., 15.57), ON skira, OFris. skirja ‘cleanse, purify’, EFris. schiren also ‘smooth off’, ete., with development through ‘scrape off’ to ‘tear off’. Cf. on Lith. bielyti ‘flay’, 9.29. Braune, Z. rom. Ph, 20.355 ff. Gamillscheg 295. Other- wise REW 7990.
Sp. rasgar (beside rascar ‘scratch’), fr. *rasicare, deriv. of Lat. rddere ‘scrape, scratch’ (pple. rdsus). REW 7074.
Sp. desgarrar, deriv. of garra ‘a claw’, prob. fr. Gallic, cf. W. gar ‘thigh’, Br. gar ‘leg’. REW 3690.
Rum. rupe (also ‘break’), fr. Lat. rumpere ‘break’ (9.26).
4. Ir. rébaim, Nir. réabaim, etym.? (Stokes 228 : ON rifa, etc., below, 5).
NI. stracaim (sracaim, Dineen), Gael. srac etym.?
W. rhwygo, MBr. roegaff : Skt. rikh-, likh- ‘rend, scratch’, Lith. rektz ‘cut bread’, Grk. épetxw ‘rend’, etc., fr. IE *reik(h)- an extension (parallel to *rezp- in ON rifa, etc., below, 5) of *rei-. Walde-P. 2.343 f. Pedersen 1.122.
2 CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Br. regi, prob. a variant of Tega ‘to furrow’, a deriv, of OBr. rec=W, rhyop ‘furrow’ (8.212). Henry 231.
5. Goth. distairan, OF teran, OHG zerran etc., above, 1.
Goth. tahjan (for orapicow ‘tear’, also for oxopritw ‘scatter’) : Goth. tagl ‘hair’ OE tagl ‘tail’, etc. (4.18), Skt. daca. ‘fringe of cloth’. Goth. development through ‘shred, tear in shreds’. Walde- P. 1.785. Feist 470 f. (with alternative view).
ON rifa, Dan. rive, Sw. riva (ME rive, ryve fr. Norse) : Grk. épetzw ‘tear down’, fr. IE *retp-, an extension of *rei-. Walde-P. 2.345. Falk-Torp 906.
ON slita, Sw. slita, OF slitan (NE slit), OHG slizan, MHG slizen (NHG schleissen ‘slit’), prob. fr. an extension of *skel- in Lith. skeltz ‘split’, etc. (9.27). Walde-P. 2.595 f.
OE rendan, ME rende, NE rend, OFris. renda, not elsewhere in Gme. and outside connections dub. Walde-P. 2.374, 578. NID s.v. rend, vb.'.
Du. scheuren, MDu. scoren (cf. Du. scheur, MDu. score ‘a rent, tear’, ON skor ‘notch, cleft? (> OE scoru, NE score) : ON skera, OE sceran ‘cut’, etc. (9.22). Franck-v.W. 584. Walde-P. 2.576.
OHG rizan (mostly ‘cut into, write’, but also ‘tear’), MHG rizen, NHG reissen, esp. zerreissen: OF  writan ‘carve, write’, etc., but both phonetic (parallel forms with or without init. w?) and semantic relations complicated. Walde-P. 1.287, 2.344. Weigand-H. 2.563. Falk-Torp 897. Feist 574.
6. Lith. plésti, Lett. plést : ON fla, OE flzan, etc. ‘flay’ (9.29). Walde-P. 2.98.
Lith. dréksti, draskyti, Lett. draskat OBoh. z-dfieskati ‘break in pieces’, Bob. drizhatt ‘slice, split’, etc., fr. IE ¥dre-sk-y
on of *der- (above, 1). Walde- an extens! Berneker 220 f., 224.
p. 1,803.
7, Chsl. dirati chsl. triignalt, in cpds. meaning — trgali, Boh. Le rob. (with varian Lat. tergere ‘wipe 0
Ide-P. 1.732. ae kidati : Russ.
: etc., above, 1. Piast triizati (mostly ‘tear off, pluck’, SCr. (both also ‘pluck’), s of final guttural) : ff’, Skt. trh- ‘crush’.
kidat’ ‘throw’,
MISCELLANEOUS PHYSICAL ACTS, ETC, Ne .
igitized by Arya Samaj Foundation Chennai and eGangotri
567
ChSl. iskydati ‘throw out’, ON skjota, OE scéotan, OHG sciozan ‘shoot’, etc. Walde-P. 2.554. Berneker 676.
Boh. rvati, Pol. rwaé, Russ. rvat! : ChSl. riivati ‘tear off, pluck’, Lith. rauti ‘root out’, Lett. raut ‘pluck, carry off, etc.’, perh. Lat. é-ruere ‘tear out, pluck out’ (but history of Lat. ruere and epds. difficult), Skt. ru- ‘break in Pieces’, etc. Walde-P. 2.352. Briickner 470,
8. Skt. dr-, Av. ni&-dar- above, 1.
9.29 FLAY, SKIN
Goth. Lith. — dirti, bielyti, lupti
CL ae ON fla Lett.  dirat
NG iabere Dan. flaa ChSl.  (dirati)
c pears Sw. jld SCr. — derati, guliti
Ie Pier OE fléan, hyldan Boh.  dfiti
4 . — desollar ME fle(n) _ Pol. —zdzieraé, tupié
male jupui NE flay, skin Russ. _ sdirat’
Ir. fennaim Du. villen Skt. bso
Nir. feannaim OHG scintan, fillen Av. vi-nad-
W. — blingo, digroent MHG _schinden, villen
Br. _—digroc’henna NHG - schinden, hiuten
Words for ‘flay’ are mostly from roots seen also in words for ‘tear’ or ‘peel’ or are derivs. of words for ‘skin, hide’.
Secondary uses, as ‘flog, despoil, plunder’, etc., are widespread, and in some languages ‘flay’ in the old literal sense 1s Now more commonly expressed by new derivs. of words for ‘skin’ (so od not flay, in common use), or by ae fe them (Russ. sdirat!
‘oat, ete.), though such phr. entered in the the, phrases are not 1. TE *der- in d ‘ oa words for ‘flay’ and a ee 1.797 ff. ay’ : Grk. 3¢ ith 6¢ Honk felts 7 €pw (with Oéppa. it skin, hide’), NG Oepva ,
. drat’,
. » Cpd. of glibere Mee ean , €, ete, (9.27). Walde-
P. 1.661. 1.610 f.
It. scorticare, Fr. écorcher, fr. late Lat. excorticdre ‘flay’ (so used in Form. An- dec., e.g. Pirson, Merow. und Karol. Formuliire, No. 7), deriv. of Lat. corter ‘bark’, REW 2988. Gamillscheg 340.
Sp. desollar, epd. of des- = Lat. dis- and a deriv. of Lat. follis ‘leathern bag’. REW 3422.
Rum. jupui, etym.? Tiktin 880 f.
Ernout-M. 426 f. Walde-H.
3. Ir. fennaim, NIv. feannaim, etym. dub. G.§S. Lane, Language 13.24.
W. blingo, etym. dub., perh. fr. a vari- ant form of the root seen in Dan. flenge ‘slash’ and without nasal in ON fla ‘flay’, etc. (below, 4). Loth, RC 41.229 f.
W. digroeni, Br. digroc’henna epd. of di- priv. and W. croen, Br. kroc’henn ‘skin, hide’ (4.12).
4. ON fla, Dan. flaa, Sw. fla, OE fléan, ME fle(n), NE flay : Lith. plégti ‘tear’
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
568
(9.28), ete. Walde-P. 1.98. Falk-Torp 228.
OE (be-)hyldan, fr. hold ‘carcass’ = ON hold ‘flesh’ (4.13).
NE skin = sb. skin used verbally.
Du. villen, OHG fillen, MHG villen (but mostly in OHG and often in MHG ‘flog, scourge’), derivs. of Du. vel, etc. ‘skin, hide’ (4.12).
OHG scintan, MHG, NHG schinden, deriv. of OHG *scind : ON skinn ‘skin, hide’, etc. (4.12).
NHG hduten, deriv. of haut ‘skin, hide’ (4.12).
5. Lith. dirti, Lett. dirat, above, 1.
Lith. bielyti, fr. WhRuss. béliti ‘flay’ = Russ. belit’ ‘whiten, bleach’ : ChSI. bélz ‘white’, etc. (15.64). Cf. Bulg. bélja
SELECTED INDO-EUROPEAN SYNONYMS
‘bleach’, also ‘peel’ and ‘flay’ (Gerof s.v.), Sorb. bélié also ‘peel’, Develop. ment apparently through ‘cleanse’ \ ‘scrape off’ > ‘peel, flay’, (cf. history of Fr, déchirer ‘tear’, 9.28). Buga, Kalba ir Senové 28. Berneker 55.
Lith. lupti (but mostly and Orig, ‘peel’) : Lett. lupt ‘peel’, Russ. lupit! etc. ‘peel’ (Pol. twpié also ‘flay’), Goth, laufs, etc. ‘leaf’, perh. Skt. lup- ‘break’, Walde-P. 2.417 f. Berneker 746.
6. SCr. derati, etc., above, 1.
SCr. guliti, etym.? Berneker 362,
Pol. tupié : Lith. lupti, above, 5.
7. Skt. dr- not quotable for ‘flay’, Other words?
Av. vi-naé-, root connection? Barth, 1038.
9.31 RUB Grk.  rpiBw Goth. bnauan Lith.  trinti NG tplBw ON gnia Lett. _ berzt, trit Lat. fricare, terere Dan. gnide ChSl. tréti It. Sregare Sw. gnida” SCr.  trljati, ribati Fr. Jrotter OE gnidan Boh. trti Sp. frotar, fregar ME = gnide (gnodde), rubbe Pol. trzeé Rum. freca NE rub Russ.  teret’ Tr. commelim Du. wrijven Skt. ghrs- Nir. cuimlim OHG  gnitan, riban Av. Ohh W. rhwhio MHG gniten, riben
Br. rota NHG reiben
```


## [2026-09-05T18:04:34.249Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 96 97 98 99; do echo \"=== IEC leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' IEC.txt | head -60; done"
}
```


### [2026-09-05T18:04:35.999Z] TOOL RESULT

```
=== IEC leaf 96 ===
insect, worm’. WP I, 777 Arm. tiz ‘tick, cf. dim. tzruk ‘leech’, fr. *digruka-); Gk. cf. dik- (for *dig- in dík- tamnon, lit. “tick-killer?, cf. Sl. Girm-dava 'dit- tany’, an odorous plant); OE ticia; Du. teek; OHG zécho. (LWs in It. zecca & Fr. tique, fr. different Gmc. dials.)
diio, diie- “fly, flee’ Skt. diyami; Gk. do díemai, id.; cf. díomai ‘pursue’; Latv. cf. deju, diet “jump, dance’
dik- (root-theme of deiK-, doiK-, q.v.) Oss. cf. áv-disan; (ambig.) MHG zich (“proof; fame'; Gk. cf. deigma, id.)
diKnos ‘proud, noble, noted’. Cf. deiK-, diK- Oss. cf. äv-dīsän ‘witness’; Lat. dignus; ON tign ‘honour’; tiginn *well-born'
diKo, ið ‘show’. See deiK-, diK-, etc. WP I, 776 Skt. cf. diSàmi, 3s didesti; Av. cf. disa (:OLat. *dixo, cf. Osc. 3s. dicust “shall show’); Oss. cf. áv-disín, -desun (‘show’, fr. apo- °)
diKos, iom, à ‘manifestation’. Cf. deik-, diK- etc. WP I, 776 Skt. dis, disa; Av. disyəm ‘teaching’; Gk. díkë ‘custom, right’; W cf. go-ddeg Cutter: ance’, fr. *upo- ?); MHG zic, gs ziges (oxy- tonic: *diKós «accusation"); ON tigi, n. id.
diKtós, iós ‘shown’; diKtis ‘revelation’. See deiK-, diK-, etc. Å Skt. distáh; distih; Oss. cf. áv-dist ‘shown’; Myc. cf. proper name Dikata-de (:Gk. Diktàn- de); OE obt ‘accusation’: MHG ziht, id. Lat. dictus, beside dictum ‘saying, reproach’ and prob. digitus, LL dicitus “finger”, cf. Skt. dis- tam “direction, fate, allocation’; (uncertainly) Sw. titta, Norw. titte (Cook peep’. See did-)
didhuró, ið — diu-, diuos, om (diu-)
I0
20
25
30
35
40
45
148
dindilo, ið “itch, tickle, coax Ir cf. dinnle ‘itch’; MHG zinzeln ‘coax’; EM. tintelen ‘tingle’. (For Gk. dendíllo, see duindil-)
(dindh- see dent-)
dink- (?) *dot, point? Skt. dinkah ‘nit; Li. dinkis ‘penis’; cf. zingel ‘spike’
dinos, om, à, is ‘day, daytime’. WP I, 774 Skt. dínah, am; Lat. cf. nün-dinum 'market- day’, cf. peren-dinus; MIr. nóin-den ‘nine-day period'; tré-denas 'three-day period'; denus ‘24-hour day’; Ir. tréa-dan ‘three-day period’; ar dhinn, as adv. “in broad daylight; Go. sin-teins ‘daily’; OHG cf. lengizin: OE leng- ten ‘spring, Lent; OCS (and com. Sl.) dinù ‘day’. Li. dienà, Latv. diena ‘day’ represents a variant *dein-, but cf. diem-.
(di-reg-, see dē- dis, reg-, only in Lat. di- rigo; MIr. dírigim ‘straighten; send")
dis- “apart, away, un-, dis-. WP I, 821 Arm. z- (in z-erc ‘free’, z-ercanem "release: Gk. di- in di-ékho, -othéo, -zémai, -óko (perh. also in di-pháo (2) 'seek); Alb. z- (in z-vjerdh ‘wean’, fr. *dis-uergh-), z-vesh Cundress", fr. *dis-uesio); Lat. dis-; OBr. Br. W di-; Ir. dí-; Ir. dí-, id. OHG zir-, zer, MHG zer-
ditis (1) ‘brightness, daytime’. Cf. diu-, diém, dièu- Skt. ditib ‘brightness’; Av. (ambig.) dita (look, perh. fr dhi-, q.v); Per. (ambig.) didan (‘to see’. Cf. dhi-); Alb. ditë ‘day’
ditis (2) ‘division’. Cf. dai-, daio, di- Skt. ditih, id: OE tid; OHG zit; ON tíð ‘stime’; Dër (&beloved', lit. *especial'); MHG cf. zidel-, cpds. *judge-
diu-, diuos, om (diu-) ‘sky, day’ (oblique theme of diéus, q.v.) Skt. div, den, divám; Arm. tiv; Oss. cf. äv- diu, -deu Cdol Ger. Ab-gott); Hiero-Hitt. Tiwa-; Myc. diwe(i) (dat. sg. ‘to Zeus’; Diwo-, Diwija (names); Gk. cf. eu-día, én-dios; dia (a goddess); Alb. cf. dívet “it dawns’; Lat. dium, OLat. diu “in the daytime'; Lat. cf. also bi-duum, sub-dio, -di1ü; Ir. in-diu ‘toda
=== IEC leaf 97 ===
y’; dia, gs dæ “god; day”; W dyw ‘day’; OW cf. diew “days”; cf. W he-ddiw ‘today’; Br. hé-ziu, id.; Cor. dew-, dæ-, cpds. ‘day’; OE Tīw ‘Mars’:
MHG
149
Cz. div *wonder. For the radical diu- cf. Skt. dyü-táh, pp. ‘shone’: OE ty-tan ‘to shine; Lat. Ju-piter, etc.
diuesnos (duesnos, diuesinos) "of day, of heaven'. Cf. diu i Skt. cf. divas- (cpds. *heaven-); divan ‘day’; Arm. erkin, erkink (i-st. “heaven'); Gk. cf. eu-dieinós “fine, of weather.
diuotos (diuit-, diuiot-, diut-) “divine; divin- ity'. Cf. dieu-, ditis, dieus, diu-, diu-. WP I, 772 Skt. cf. dyütáh, pp. ‘shone’, divyatà ‘divinity’; dyutih, Ved. dyut ‘splendour’; Tokh. A sat, B $ate "och: HHitt. Tuwatas (name of a king); Alb. zot “lord”; Lat. dives, -itis ‘rich’; OBr. duiutit ‘divinity’; W duwdid, duwdod, id.; Cor. cf. dewes ('goddess', fr. a type *diu- itio); Ir. diadha “divine; dia, pl. déithe “god; day'
diui (loc. sg cons. st. as adv.) “by day’. Cf. dieus, diu-, etc. Skt. diví; Gk. diwí, dif; Lat. diu; OIr. cf. in- diu; W cf. he-ddiw
diuio ‘shine, light up’. Cf. diu-, etc. See next Skt. divyàmi ‘shine’; Av divyei-; Alb. dívet, 3s ‘dawns’; OCS divljo se, diviti se "be sur- prised'; Latv. cf. dīvains ‘strange’
diuios ‘heavenly, divine, wonderful, strange". Cf. diu-, etc. Skt. divyáh; Arm. cf. tir, tiwr “god, idol; Myc. diwijo-; Gk. díios, dios; Lat. dius, beside divus, a *god'; MIr. diadha; OW dydd, pl. diew ‘day’; W dydd; Cor. deih, dyth, jeth *dze-, d: OCS divij, adj., divija, s. ‘wild; wildness; OCz. diví ‘wonderful’; Li. cf. dývas, usu. pl. d$vai ‘monster, wonder’; Late cf. dīvains ‘strange’. Derivative forms: Hes. díalos ‘bright: Br. déol, W duwiol ‘divine’ fr. *diuiolos. Further: Lat. divinus; Cz. divný ‘strange’; Li. dývinas, id. fr. *diuinos
diém, acc. sg. theme of diëu-, q. v. Skt. dyam; Gk. zén; Alb. zoné; Lat. diem
diemi ‘tie’. See deio (1)
dieso ‘ferment’. See ieso. WP I, 208
diéu- (1) ‘shine, burg". See dieus, diu-, etc. Skt. dyote, 3s; Li. dziaunu, dziáuti beside dziüstu, džiūti “dry in the open; Latv. Zauju, Zaut, id.
10
15
20
25
30
35
40
45
diuesnos (duesnos, diuesinos) — dlghió
150
dieu- (2), dieunio ‘goddess’ Alb. zonjë ‘lady’; Skt. cf. dyünam ‘zodiacal sign of the sun’; Lat. cf. Jüno; EMAIb. cf. zevé ‘goddess’
dieu- (3) ‘strike, beat". Skt. dyaumi ‘attack’; Ved. dyotayami (pp. dyuttah) ‘break’; Li. dZiauju, -ti ‘thrash’
dieus, obl. diu- (cons. stem) ‘god, sky”. Cf. diu-, etc. WP I, 772. Also: deiuos, à (variant) ‘god, goddess; demon, demoness' Skt. dyáuh; deváb; Per. div ‘demon’; Oss. cf. äv-dīw, -dew (*demon'. Cf. G “Ab-gott'); Thess. cf. dagüs “ritual wax image”; Arm. tiwr, tir ‘god, idol; tiv ‘day’; Av. cf. paiti-dayus *very-deceitful' beside daevo ‘demon’; Myc. cf. diwijewe ds.; Gk. Zeüs; Gk-Albanian Die, gs Diesé ‘God’; EMAlIb. zevé ‘goddess’; OLat. deiuos, L deus; Osc. deivo gp; deívaí fs. dat.; Gaul. divo; W duw; Br. dué; Mir dia, déa, i.s. diu; Runic Go. tyz; OE Tiw ‘Mars’; ON Tyr, pl. tívar; OHG cf. Zios-tac ‘Tuesday’: OE Tiwes-dag, id.; OCS divü ‘portent, wonder’; divo, -ese, id.; dijevü ‘divine’; Li. diévas, voc. Die; Latv. dievs; OPr. deiws; Finn. LW taivas ‘sky’
diu (z-gde radical of diëu-, q.v.). Cf. Skt. dyü-táh (pp of dīvyāmi, vb. “shine'); OE cf. ty-tan ‘sparkle, shine?
dlukus (dulk-) ‘sweet, mild, soft. WP I, 816 Gk. gluküs (variant: deükos); Alb. i n-dulkét *overripe, ripened on the tree’; ndülket, 3s *ripens on the tree, is mellow’; Lat. dulcis.
dleio (dien) ‘yearn, lon
=== IEC leaf 98 ===
g’. Cf. WP I, 810 Lat. doleo ‘fret, sorrow; OCz. dlieti ‘tarry’;
` OCS pro-dijo, -dliti ‘lengthen’
dlghis, io length, distance’. Cf. dlghos (1). Cf. WP I, 813 Oss. dårg, id.; Ir. dluighe ‘separation’; OCS diüzi “length?. Cf. also Mir dluigim, Ir. dluighim ‘separate’; OCS dlüZgo, iti *extend'; Go. tulgjan 'strengthen'. See next
dighio (u-basis) *owe, be indebted, be obliged’. WP I, 868. dhlgh- (?) Mir. dligim, Ir. dlighim “owe; deserve, claim, have the right beside dlecht (lawful, fr. *dIghitó-); OW dylyu ‘deserve, be due: W dyleu "be obliged"; Br. dléut, inf. ‘owe’; Cz.
151
dlužím ‘owe’; R dolZü, -àt, id. Goth. dulgs “debP is isolated. Cf. Tokh. A talke, B telki ‘sacrifice, and PreobraZenskit: dolgü. Cf. dighos (2)
dighos (1) (dologhos and variants) "long, lasting, durable’. WP I, 813. Cf. de-/do- and legh- Skt. dirgháh; Av. daroyo; OPer. darga-; Oss. darg (beside därg, dárg-cà "length; Gk. dolikhós, en-delekhés; Hitt. dalugis; Lat. cf. in-dulgeo ‘indulge, concede’; Ir dluighe ‘separation’; Go. tulgus; OE tulge ‘firm’; OS tulgo ‘very’; OCS dlügü; Pol. długi; Srb. düg
dlghos (2) ‘necessity, rigour, duty, debt. WP I, 868. dhlghos (?) Ir. dlig ‘proper’; cf. dliged (duty, debt, law": W dyled, Cor. deleth) beside Ir. dlighe ‘law’; Br. dlé ‘debt’; W dyl ‘due, debt, right" beside dylw ‘duty’; OCS dlügü; Pol. dług; Srb. dûg, id. Cf. dlghio.
dmon- (theme of dom- *house"). Cf. WP I, 787 Skt. cf. dam-patib “head of the house’; Av. doma ‘dwelling? beside nmanom ‘house’; Arm. cf. tun, id.; Cypr. cf. ki-dnón ‘thither’; Li. nàmas, namai; Latv. nams (?) (but cf. nem-, nom- 'divide")
dm-pedom (-pods) “site, land, footing, base” Gk. dá-pedon “ground, floor; Br. danvez *building-material; OHG, MHG zumft ‘guild; rule, status, discipline OE toft ‘site; ON tupt, topt ‘homestead’; Dan. toft *'smalihold- ing’; Norw. tomt ‘site’. Cf. Gk. héme-, hume- dapós ‘native’ and Myc. edapo-, Gk. é-daphos, (f. fr. *sed-dmbhos, and ki-dáphe “lie- aground’ > 'fox). (Gk. oü-das fr. *oio-dms *Jevel-ground" (?))
dintos (dmotos, dmatos), cf. dom-, dəmis Skt. damtáh; Gk. dmétos ‘domesticated’; OBr. domet-ic; W dofawd, s.
dnguhà ‘tongue’. WP I, 792. Cf. $uhuó, ĝu- hon- Tokh. A (?) kantu, BO) kantwo (by metath.?); OI at dingua, L lingua; Go. tuggo, OHG zunga (and com.Gmc.)
dns-, dnt- ‘close, thick’. WP I, 793 Gk. dasüs; Alb. cf. i dándun, i déndun
dighos — doghà
20
25
30
35
40
45
132
‘dense’, fr. *dntmno-); Lat. densus
dnts-, dont ‘tooth’. Cf. ednt-. Cf. WP I, 120 Skt. dan, dat, dant-; Av. cf. dantan; Per. dandan, beside dande ‘rib’; Oss. cf. dändäg (dim. type); Gk. cf. datü-sso: Go. cf. tunpus; Lat. cf. dens, -tis, gp dentum (Varro, later dentium); Osc. duntes “by the teeth'; Olr. dét; W dant, pl. daint & dannedd; Br. dant, pl. dent; Cor. dans, pl dyns, danneth; Go. tunpus, cf. also aíhva-tundi (o horsetooth' i. e. *briar); OHG zand (i-st.); Swiss zant, pl. zaent; Du. OS tand; OE top, pl. tep; ON tonn, pl. tenn, tenur & téór; Li. dantis, pl. danty, id.
do ^to, towards. Cf. dé. WP I, 770. Cf. endo, ndo Av. -da; Per. -da, -dā in i-dà ‘here’, ava-dà ‘there’; Hitt. -ta, -da in dame-da ‘elsewhere’; Gk. (?) in do-keúð “watch for, do-enüo, -néo “bend”, etc.; Lat. -do in quan-do; MIr. & Ir. do; OBr. do; Br. da (by WSP); W dy- (cpds.); OS.OE to; OHG zuo; MHG also ze (by WSP); Du. te (by WSP); Fris. to; OCS do (cf. also -da in ko-da ‘where’, fr. do); cf. also OCS da-Ze-do “as far as’; OLI. da- (vb.px); Latv. da-, id.
do- (theme of dídomi, dómi, and cf. dotós). Cf. dón-, dotis Venetic cf. doto “I will give’, donasto ‘I have given’; Lat. do, donum, etc.; ON tæja
=== IEC leaf 99 ===
 ‘grant, help, avail
do-ar- (by crasis > dar- ?). Cf. do and ar- (3) Arm. cf. taraj “I brought; W daru (inf. *fin- ish’); Li. (?) daraŭ, inf. daryti ‘do’
dö- (dódmi, dídomi, fut. dosio) ‘give’. WP I, 814 Skt. dádàmi, dadmi, fut. dasyámi; OPer. dā-; Av. daóámi; Per. cf. inf. dàdan; Arm. tam, fut. tac; Gk. dídomi, fut. dóso; Lat. do; W cf. dod (imperatv. *give!); ON cf. tæja ‘grant’; OCS fut. damí; OLi. duomi, fut. duosiu, duosu
dogos, is, ios, (n) ‘spike, tine’. WP I, 785 Hitt. cf. cakkis (of uncertain mng.); MHG zacke, G Zacken 'spike, spur; LG tacken ‘spike, twig’; Du. tak ‘branch’; ME tack; Li. dagys ‘thistie’; Latv. dadzis "bur
dogha “holding, reception’. See de$h- & cf. WP I, 783
153
Gk. dokhé; Li. dagà “harvest? (but in sense of ‘heat’, see dhoguh-)
doiKos, à ‘revelation, vision’. Cf. deiK-, diK-. WP I, 776 Skt. deSáh; Av daeso; Oss. des “wonder”, dis ‘surprise’; (Arm. tes, o-st. is fr. *derK- according to AM); Ir. cf. daochán trage; MHG zeige (oxyt. prototype: indication”); OE tah *teaching'; Cz. dés “terror”
doiuos, ios ‘godlike, heavenly’. WP I, 773. Cf. deiuo-, dieus, diu-, etc. Skt. deváh; Av. cf. daev-, v. *Cheat'; OPer. daiva- ‘demon’; Lat. divus; Li. cf. deive *god- dess’; Finn. LW taivas “heaven?
dõios ‘giving; gift. Cf. do-, dídomi, etc. Skt. dayah; Cz. -daj, -dej (in cpds.)
doK-, doKeið “perception, reception; make perceive, make receive’. See deK-. WP I, 783 Gk. dokéo ‘seem’; cf. dóke (*received *opin- ion"); Lat. doceo; OIr. doich ‘apparent’; OS cf. fra-tah ‘ornament’; fra-tahon ‘adorn’; OCS do3o, dositi “find”
dokt-, doket (?) “shaped; shaper Av. daxsta, om ‘tool’; Lat. doctus (?); LG tacht ‘shaped’
dol- (dolaio, -eið) ‘devise, shape, contrive’. Cf. dolos (1) Gk. cf. denom. dolóð ‘fake, trap’; Lat. dolō, āre ‘shape, trim’; Sw. tälja, id.; OCS cf. dly, gs dlüve ‘pickaxe’; dato ‘chisel’
doligh-, see dlgh- (1). (Variants include Av. dareyo ‘long’, dareyus & driyus ‘poor’; Ir. doluighe “long illness’, beside dlighe, adj.)
dolos, us (1) ‘noose, knot, trick, device. WP I, 808 Gk. dólos; Lat. dolus; Osc. acc. dolom; Olr. dul ‘snare’ beside dolb, dailbe ‘deceit’; Ir. dol ‘snare’, dolbh ‘sorcery’; W dôl. pl. dolau, dolydd ‘noose’ beside dolen, id.
dolos, is (2), see dalis
doma1g (domaio, dmäið), eio ‘tame, domest- icate’. Cf. domos, us, dəm-, dm-. WP I, 788 Skt. damayāmi, pp. damitah; Oss. domin, dämun; Hitt. cf. damas(mi); Gk. damáo; Lat. domo, are; LOIr. damnaim; OBr. cf. domet- ic, adj. ‘tame’; cf. OBr. ar-domaul, id.; Br. don- va; W dofa; Cor. dova; OHG zamon; Go. ga- tamjan; OE temian; ON temja; cf. tamiór,
doiKos, à — dongheió
10
15
20
25
30
35
40
45
154
adj.; OCS pri-domljo, iti
dombos “lump, block W dom ‘dung’; Norw. tamp ‘knotted rope’; Sw. tamp (‘knotted rope; lout'; cf. Norw. tampa ‘hoyden’); OCS dobü ‘tree, timber”. In com.. SL “oak'; cf. OCS dobrü, dobrava ‘forest’; R cf. dubina ‘club’. (A variant arises in ON teppa, Sw. täppa, Norw. teppe, v. ‘to bung’, whence Fr. LWs tampon and tapon)
dombrā, 'dombərå (?) ʻa droning musical instrument’ Skt. cf. dambarah (‘din’, a Dravid. wd.?); Per. cf. zambüra (‘guitar’, prob. fr. Arab.); Li. dambrà “bagpipes; accordeon'
domeió, see domáio
dómi, see dö-
domitos ‘tame, domesticated'. See domàio Skt. damitah; Oss. dánt, domd; Lat. domitus; OBr. cf. domet-ic, adj. ‘tamed’; ON tamiór
domios “domestic, for taming’ Skt. damyah ‘bullock for taming’; Alb. dem ‘bull’; W dot pl. dofion ‘tame’
domn- (1) ‘dwelling’. Cf. domos, us and demo. WP I, 787 Arm. (ambig. prob. *-ó-) tun, gs tan “house”, tanik ‘roof; Gk. dóma; Blg. dam (stable,
if nota LW)
domn- (2) ‘gift. WP
```


## [2026-09-05T18:04:43.214Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 102 103 104 105 106; do echo \"=== IEC leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' IEC.txt; done"
}
```


### [2026-09-05T18:04:44.959Z] TOOL RESULT

```
=== IEC leaf 102 ===
- ?). (Pol. dur = *typhus?)
dou (theme of dö- “give'); douit-. Av. dào, adj. (giving; Arm. cf. tuav (‘was given’, fr. *douoto); Cypr. dowénai, inf.; Orch. dónai, id.; Osc. cf. -tuvetu, Umb. pur-douitu!, impv. “let him give’; LOIr. duais ‘gift; Arm. tvi¢ (‘giver = OCS davici, id. fr. *douitios). Cf. Cz. dav, ppp. “having given?
douo?, douuð? ‘go’. Cf. WP I, 779 Skt. davàmi "eo: MHG zouwen “set out, dash off; G zauen, id.
drab- ‘step, tread". See next MLG trappe ‘stairway’; (G Treppe fr. LG); Salic trappa; OE treppe ‘trap’; Li. Žemaitē drabynos, pl. ‘ladder’
drabið ‘tread, tramp, trample, crush’. Cf. drab- Du. trappen ‘kick, tread’; OE treppan ‘trap; tread’; OCS drobljo, drobiti ‘crush’; Cz. po- drobiti *subjéct
drăgh- ‘harass, torment; grieve’ Skt. draghe mp. ‘tire, torment’; Ir. dragh ‘annoyance’, draghan ‘resentment’; OE trega ‘misery, pain’; tregian ‘harass; feel repugnance at; ON trega ‘grieve’; tregr ‘unwilling’; tregi ‘sorrow’
draio (dràmi, dídra-) ‘run’. WP I, 795 Skt. drámi, dadra-; Gk. didrásko, fut. dráso (Doricism?) (‘will on: Skt. dras-); drénai, inf. mp.
drăk- «téar; detachment, piece’. W dragio ‘têar; drag ‘piece’; OCS dročọ se, -iti se ‘be insolent; Pol. Ukr. droczyć, dročyty ‘tease’; R cf. drok ‘furze’; (*-à- in) Big. draka ‘thorn’ OCS dracije ‘thorns, briars'; R & Slovene dráka ‘scuffle, fight
159
(draku “tëar”. See dakru)
drāmi, etc. see dräig
drapsos (drap-) “cloth, cloth-length, sheet. WP I, 802 Skt. drapsáh "Tag: Av. drafo, id.; Per. di- raf$, id.; Arm. draws, id. (fr. Pers.); LLat. drappus (whence It.Fr.Sp.); OE træf ‘tent: ON traf *headcloth'; Li. cf. drapanos ‘clothes’
drasgos ‘a song-bird' Br. drask ‘thrush’; OCS drozgü ‘finch’
drauiom ‘tray, trough’? (dreuuio-, dreunio-). Cf. dreuin- below Hes. draión ‘trough, bathtub’; Sw. tró ‘tray’; (phon. of OE trige, for *triege is obscure: *dreuyio-?). A variant occurs in Skt. dronah, -am “trough, tub'. (For Hes. draión, cf. druo-, etc.)
drég- «drag, dawdle’ OHG tréchan ‘draw’; MHG tréchen ‘pull, scrape, scratch’; Upper G trechen; Du. trek- ken; (Ge in) Sw. tråk ‘toil; tráka ‘dally, dawdle, toil; Li. cf. dregstu, drégti (2) “drag, téar
dréks- (?) (1) ‘pluck, t&ar'; (2) ‘dry, wither (1) Skt. dráksa “vine, grape’; Blg. dréxa "ear, ment’ (2) Skt. drākhāmi ‘wither’: (Blg. dréxál ‘limp’ is OCS drexlü, adj. ‘saď’).
dreutis (drutis) ʻa song-bird’ Arm. (ambig.) artiwt, artujt & artut, gs artuti (i-st. lark?); W drudwy ‘starling’; Ir. druid, id.
dreutos ‘bold, daring, strong, firm’. Cf. druuo-, dru-, etc. W drud ‘bold, daring; dear": MHG triute ‘darling’; OE treowp ‘truth, pledge, faith’; isophonic w. Li. driáučius “log, beam’
dreueros ‘flowing; fluid’ Skt. dravaráh, adj. id.; Arm. aytiwr, ayter, gs. & eytiwr, -ter ‘marsh’
dreuin- (dreun-) “wooden; wood, wooden object?. Cf. drauio- Skt. dronah, -am ‘trough, tray’; OE treowen “wooden, treen'; ON cf. trjóna (2) “pole?
drislos, drisəl- “turn, twist. Gk. drilos ‘earthworm’; Du. tril ‘spree’; Sw. trilla ‘roller’. Cf. also an alleged MLG triselen "roll" beside Norw. trille, Sw. trilla, id.
draku — drouàá
20
25
30
35
40
45
160
drob- (?) “large bird" MLG trap, trappe '*bustard'; Du. cf. trap- gans, id.; Cz. drob, Pol. drób “poultry”. (Pol. drop, Srb. Blg. droplja *bustard' are LWs)
dromblio- (dromb-) *tread, tramp'. Cf. WP I, 797 & I, 876 MLG & LG trampeln; Li. dramblys ‘elephant’; cf. Sw. trampa, v., and tramp, s. ‘treadle’. (Sole instance of e-gde in Go. -trimpan ‘tread’)
dromos ‘course, way’. WP I, 796 
=== IEC leaf 103 ===
Skt. cf. dram- ‘to run’; Gk. drómos; LG tram ‘rung of ladder’; OE. trem ‘footstep’; Norw. tram ‘threshold’
drongos, å ‘mass, company, tribe, settle- ment’. Cf. WP I, 860 Skt. drangah, -a ‘town’; Ir. drong ‘company, tribe, people’; Gallo-Lat. drungus ‘crowd’; Gaul. drungos ‘mass’; OBr. drogn (sic) ‘company’. (LWs in OCS drogarí ‘member of a troop’ fr. Med. Gk. drouggários fr. LLat. drungarius)
dróp9ð, ið ‘pluck, têar’. WP I, 801 Gk. dropto ‘pluck’; cf. drõpax, s. ‘depilatory’; Pol. drapać; Cz. drápu, at Blg. drapam; Srb. drápljem, drapati ‘scratch, téar
dropsos (?) ‘droplet; shower’ Skt. drapsáh 'droplet; Arm. tarap ‘shower’
dros- (drosios?) (?) ‘droppings’. Gk. drósos Cdewi pl. ‘tėars’); Alb. dra, gs drau & draje ‘lees’; E cf. trash beside Sw. trasa (?) ‘rag
droudhos, ā ‘forced, constrained; straint’. Cf. drudh- & WP I, 800 ON trauór ‘reluctant’; trauð ‘difficulty’; cf. trauóa (v. "Tat Latv. draudi, pl. ‘threats’; draudēt ‘to threaten’; Li. cf. draudimas "ban: warning; insurance’; draudZiü, draüsti “ban; warn; insure'
drounios, see dreun-, drauio-
droustos “held, tight, firm, constrained’. Cf. droudh-, drudh- ON traustr ‘trusty’; traust “help, protection’; Li. uZ-draustas, adj. “forbidden?”
drouà ‘timber; hole in tree’ Skt. cf. dravyah “of trees'; cf. dravyam *ob- ject, thing’; R drovà “firewood'; Li. dravis, f. & drave ‘hollow in tree’; Late drava ‘hive; bee-hole'; Hes. cf. droós “strong, hard’; én-
con-
161
droia “heartwood of tree?
dru- (radical) ‘timber, tree’. Cf. druu-, dru- to-, etc. WP I, 804 Skt. dru; Av. dru ‘timber; spear’; Gk. drüs *oak'; Alb. dru, gs. druje & drü, gs drüni “timber, tree’; cf. Gk. én-druon *yokepeg"; dráos ‘woodland’ (*druuo-); Li. cf. sü-drus ‘stout, solid’. (Myc. has dru-, duru- in various cpds.) |
drubho, ið “scratch, scrape'.«Cf. WP I, 800 Gk. drüpto, aor. mp. edrüphen, id.; Cz. drbu, ati, id. Á
drubhos, à ‘scratch, scrape’. Cf. drubho Gk. druphé ‘scratching’; Hes. druphoí 'scrap- ings’; Cz. drb, id.
drudhol-, see durdhol- (1) & (2)
drudhó, ið “crush, squeeze’. Cf. droudh- and WP I, 800. Cf. dhrgh-, drut- Alb. (ambig.) drudh ‘crush’; drudhe, drudhé ‘crumb’; drudhem, mp. “hurtle? (see dhrgh-); (MIr. druidim 'shut, push, drive, force'; druit *compression' suggest a variant: *drut-, q. v.); Go. trudan ‘tread’; SWGer. trotten “press grapes; ON troða ‘tread, press, stuff; Cz. cf. drdy “fits, fears?
drüið (druuo, ið, drün-) ‘harden, strengthen’. Cf. druo-, dru-, drutos Alb. n-dryj ‘bolt’; dr$, gs drýni, s. “bolt, bar, lock’; MHG trüwen “trust, hope’; ON tryggja, tryggva "make firm’; trà ‘faith’; OPr. druwit, inf. ‘to believe’; Li. cf. drütas "firm". (The Greek form hi-drüo, hi-drüno “set, fix? seems to represent a formula of type *sid- + °. Hes. has a form drüomai ‘hide’).
drukos “hard, firm, wooden’ Gaul. drucos ‘evil’; Br. druk, drug ‘bad’; W drwg, Cor. drok, drog, id. (the semantic shift is not clear); Olr. & Ir. droch-, cpds., id.; OHG truha ‘wooden chest; MHG truhe, id. (and “wooden canal); Latv. cf. drukns “solid, firm’; Li. cf. drüktas, id. (beside drūtas); Cz. cf. dréet ‘stare ať. (Ir. droich ‘dwarf may belong here)
drümos “forest, scrub” Skt. drumáh ‘tree’; Gk. drümós, pl. drúmá ‘thicket’; OCS drümü, R drom ‘dense forest’; Big. cf. drăm-kaš 
=== IEC leaf 104 ===
'*thicket
drums- ‘réfuse’
dru- — drunos, om, is
10
15
20
25
30
35
40
45
162
OE cf. trüs ‘brushwood, firewood’; Li. drum- stai, pl. ‘sludge’; Latv. cf. drumsla ‘réfuse,
waste' drus- (1) “tangle, confuse; confusion”
Go. cf. ufar-trusnjan ‘scatter’; ON tros "under. growth’: Sw. dial. tross (Crubbish': Mod. Icel. tros, id.); ON trosna ‘tangle’; Cz. drchati “tangle, confuse’.
drus-, drusos (2) “firm, solid”. Cf. dru-, drsus, druos, drutos, etc. Gaul. drusus “firm, boid’; LW in Fr. dru; (LG tros ‘proud, defiant reflects, like Du. trots, an obscure G Trotz, MHG trutz, trotz, s. but the radical *dru- is common to all forms); Li. cf. sü-drus 'solid'
drut- (1) “press, crush? Ir. (ambig.) druidim (force. Cf. drudh-); Cz. drtit ‘crush’. (For Go. trudan, ON troða, see drudh-)
drut- (drutis, drudis) (2), cf. dreutis, etc. and WP I, 761 Arm. artujt, gs artuti ‘lark is ambig.; Ir. druid ‘starling’; SW Ger. cf. Trose (thrush? or *greenfinch")
drütos (1) “wooden, of oak, of hardwood; solid, firm, strong’. WP I, 804 Per. durüd ‘timber, plank’; Arm. cf. artuc Cjuniper, fr. *drutio-); Gk. drútë ‘wooden bowl, wooden coffin’; Alb. i drutë ‘wooden’; Lat. cf. in-druticare Clusurate fr. Gaul.); Mir druit (€compression', but cf. drudh-); Gaul. drutos (sturdy, brisk’, substr. in Fr. dru); Li. drūtas “thick, solid, strong’. Cf. also dru- in Gk. dru-pepés ‘ripened on the tree’; drü-ppà ‘olive’. (The source of Gk. hi- drütós “set, established" is uncertain, perh. fr. *sed-, *síséd-)
drütos (2) ‘frivolous; fool’. Same as (1) (?) Ir. drúth ‘frivolous; silly et": OE trüp "but. foon’; ON trüór ‘juggler
druuos, om, is ^wooden, hard; wood'. WP I, 804. Cf. druos, deru- doru, dru- Skt. druváyah ‘wooden bowl; druvayam ‘wooden measure’; Gk. drúos ‘woodland’; cf. én-druon *yoke-peg'; drüinos "of oak’; Alb. dru, gs. druje & druni 'timber; ON trú ‘faith’; Pol. drwa ‘firewood’; R drovà, n.pl. id.; OCS cf. *drüvinü (= Gk. drúïnos)
163
*wooden', in drüvin-ica “bedroom; OPr. dru- wis ‘faith’. Cf. also a type: druuod- ‘a wood- land being’ in Gk. druádes, pl.: Gaul. druidai, pl.; Ir. druadh ‘druid’. (For MHG trut, trute “goblin; fairy: LG drude, id. see dhrudh-. For drun, see drüio)
drbh- (dorbh-) ‘turf, peat, sod’. WP I, 808 Skt. cf. darbháh ‘tuft of grass’ beside drbhàmi, v. (2) ‘bunch’; OHG zurba; OS.OE.Du. turf; ON torf, torfa; Sw. torva ‘turf, peat; (alleged) R derbà ‘cleared land” is ambig.; Li. LW dur- pes fr. Gmc. as also Finn. turve ‘peat, turf. G Torf is fr. LG.
drbhó, ið ‘twist, turn’. Cf. dorbh- Skt. drbhámi (2) ‘weave’; (o-gde in Ir. darb, dairb ‘weevil’; doirbh 'cattle-tick'; OE tear- flian ‘turn, wallow’; MHG zerben; Wh. R. dorobjic)
drd- ‘shake, rattle’ Skt. cf. drduh (a dance); Slovak cf. drdrať ‘rattle’; Cz. cf. drndat ‘wag’; Rum dárdalá ‘trembler, stammerer (LW?); Li. dirdü, éti, v. ‘rumble’. (For Alb. dridh, tr. ‘shake’; dridhem ‘tremble’, see below: dhrig-, though possible as *drd-). See durdholos
drdh- “linger, laze, doze Cf. drm- Gk. dartháno, darthé
=== IEC leaf 105 ===
o; Cz. (ambig.) drdol "dot: Li. cf. dirdénu, -dénti ‘crawl, as traf- fic’. (For Arm. tartam ‘hesitant’, cf. Gk. tetra- maíno ‘tremble’, qua *títrém-)
drgl- (?) ‘fail, fal LG torkeln ‘tumble, stumble’; Big. cf. drágla ‘feeble woman, trollop’; drágla$ ‘weakling; jade (horsey; drágliv «lean, weak’. The Blg. forms are ambig. cf. dhrugh-.
drgh- ‘têar, pull, pluck’. Cf. dorgheið Ir. cf. driog ‘pang, pain’; Icel. torga ‘devour’; R. dérgat, nut ‘pluck, pull, pil’; Cz. drhnout ‘scour, scrub’, cf. drhlice, f. ‘pilling imple- ment: Li. dírginti ‘irritate’
drêh- ‘scrape, graze’. Cf. drgh- Oss. äv-därzín ‘wipe, graze’; Big. drázam ‘break (flax)'; dárzalka ‘hackle, flax-breaker’
drK- (radical) ‘see’. See derK-, dorK-, drks-. WP I, 806 & see next Skt. dr$, adj. ‘seeing’; dr$ih 'sight'; Olr. cf. drech (&aspect', fr. *drKs-); Ir. dreach, drioch, id.; W drych *mirror
drbh- (dorbh-) — drs-
10
15
20
25
30
35
40
45
164
drKmn- ‘aspect Gk. cf. (e-gde) dérgma “look, aspect; Br. dremm, W drem, id.
drKsos, à, ios “vision”. See derK-, dorkK-, drK-, etc. | Skt. -drksah (cpds. “-looking'); Olr. drech; Ir. dreach, drioch “aspect, appearance; W drych ‘mirror’; Per. cf. duruxsam “shine”
drktis “seeing, sight, brightness? Cf. derk-, dork-, drk- & WP I, 806 Skt. drstih; Av. (o-gde) darstis; Alb. dritë ‘light’; MIr. cf. drithle ‘flash’; OBr. cf. -drichet- ‘scope’; OHG zorcht, zoraht, adj. ‘bright; OS torht, id. OE torht (id. & *brightness")
drm- “sleep, drowse'. WP I, 821 Lat. dormio, ire; EMCz. cf. drmek (a sedative: *agnus castus")
drnos, is (drmn-, dorn-) (1) “piece, part. Cf. dero Delphic Gk. cf. dárma 'skin'; Br. Cor. W darn ‘piece’; LW in ONorm. darne, id. (fr. *dorn-); Du. cf. tornen “rip up, come unsewn'; Russ. dern, Blg. & OCS drán, drünü; Pol. dar: Cz. drn ‘clod, sod?
drnos (2) *harsh'. Cf. drs- Skt. dirnáh ‘desperate’; MIr. drenn ‘warlike’; OBr. cf. ar-dren, id. MHG (ambig.) zorn (*angry'. Cf. dusnós); OE torn ('cruel, bitter, oppressive’. Ambig. as MHG); Du. cf. tornen, v. ‘dun, press for payment’; Gk. cf. draíno *be strong, be prepared for
dro, ið (dor-) ‘skin, tan, téar. Cf. dero, dor- & WP I, 797 Skt. drnami, tr. intr. ‘burst, téar'; Av. cf. də- rota, pp. ‘cleft’; Gk. daíro, adj. dartós ‘flay, flog; MHG cf. pp. ge-zoren: E torn; OCS díro, dréti & diréti ‘plunder’; Cz. du dřít ‘scour, swot beside deru, drát ‘strip, pluck a fowl’; Li. diriu, dirti ‘skin’; Late cf. (freq.) diraju, diråt, id.
drpo, io ‘fling, rant, rage’. Cf. drbh- Skt. drpyami ‘set on fire; rage’; OE torfian ‘fling, shoot, stone, surge’; ge-tyrfan “strike, afflict; E cf. to turf out; Du. turven op, Fris. turvje op ‘hit, beat. (The Gmc. forms ambig. cf. drbh- and drubh-. Cf. also dhrbh-). Cf. OSw. tyrva, Sw. torva till ‘to pelt
drs- “hard, harsh; hardness, harshness'.
165
Skt. cf. drsad ‘rick, stone of mil; Av. doros ‘sorrow’; Du. torsen ‘endure, be weighed down’; OCz. drsati sé ‘defy’; Cz. drsný “harsh?
drtis ‘têaring, scraping; têar, skin’. See next & cf. WP I, 797: dero Skt. drtih ‘skin’; Per. dül *water-skin'; Gk. dársis ‘skinning; milling’; Go. ga-taürps “de- struction’; Cz. drť? ‘powder, sawdust’; R (al- leged) derť ‘bran’
drtos (1) ‘torn, flayed, cut, worn, ground’. Cf. drtis, dero, etc. Av. doroto (1) ‘cut, mown’; Gk. dartós, dra- tós *flayed'; Ir. cf. dartán ((clod', fr. *dort-); Pol. darty ‘split’; Big. dárt 
=== IEC leaf 106 ===
‘decrepit’; Li. dìr- tas, dirtas ‘torn, flayed'. Cf. *-dër- in Skt. avadaritah ‘burst open’; OCS u-dir-ati ‘to flay’
drtos; drtis (2) “dirt, excrement'. (Same as drtis, drtos, (1) ?) Gk. (Delphic) daráta ‘cake’; Ir. cf. dairt ‘clod’; OE tord ‘excrement’; ON. Sw. tord-, in cpds.; Latv. cf. dirst ‘to excrete’
drtos (3) (?) ‘time-honoured’ Skt. drtah ‘honoured’; Blg. dárt “old, hoary’
druāið, see druió
druis, io “wood, trees, brushwood'. WP I, 804. Cf. druos, deru-, doru- Gk. dría, npl. ‘copse, wood”; cf. also magü- daris gum-tree': MIr. dair ‘oak’, dairbh-eog, -re ‘oak forest’; W dryw ‘druid’; ON tyri, tyrir ‘fir; OCS drüvije ‘timber; Srb. drvlije, id.
druið (druàio) ‘press, harass; strive” Av. cf. driwis ‘begging’; driwikom ‘poverty’; Gk. dráo ‘do’; OE tyrwian ‘harass’; Pol. cf. drwic (taunt, fr. a variant *duru-, *druu-); Slovak drviť ‘thrash; wolt. (Isophonic forms are Albanian dryj “lock, bolt, bar" and Li. dirvà ‘arable field’, dirvónas ‘fallow land’. Arm. trorem ‘pound, powder’ seems to represent a form *deruo- or *duruo-). Skt. cf. dūrvāmi (var. of dhürv- "hurt?
drum-, drumn- 'strong, firm' Hiero-Hitt. cf. tarawana- ‘prince’; Alb. (am- big.) dr$, gs drýni, m. “bolt, bar. lock; OW drwn ‘strong’; Olr. & Ir. dron, id.; OE trum, id.; trym (2) ‘firmament’; LG cf. tórnen ‘bridle, check
druos, om, drus, dru- ‘wood, timber, tree’.
drtis — duio
15
20
23
30
35
40
45
166
See druis, deru-, doru-, etc. WP I, 804 Skt. druh, dru; Av. drvo “firm, hale’; Hitt. cf. *daru, taru ‘wood’; Gk. drüs; cf. én-druon *yoke-peg'; dén-dron (if for *dem-druom “building timber); ké-dros; ha-drós (“ mature”, cf. OCS sü-dravü “hale”, fr. *sm-doruo-); Alb. drü, gs drüni & and dru, gs druje 'timber'; Mir cf. daur-, cpds. *wood-'; OE tyrwa, tyrwe (tar, adjectival form fr. *druios, à "of tree’); Srb. drvo ‘tree; timber’; R drovà ‘firewood’
du- (reduced element of duou, duð ‘two’, q. V.) Lat. du-plus; OE tū; Li. du; Per. du; G cf. Zu-ber “tub?
dudos, à, io (1) “tip, top, topknot; end, tail, penis’. See next Arm. čuč (Cpenis', by induced palatalism via *diudio-); Irish dúd ‘stump’; dúid (3) “penis”; OHG MHG zutzel *dummy-teat'; OS tuttili, id.; Du. toot 'topknot, spiral; E dial. tot “bush, tuft’; ON tuttr (tom-thumb'; Icel. tota “point”, toti ‘snout’; Sw. tott ‘tuft. See next
düdos, à, is (2) “pipe, tube”. (Some features are common w. (1), q.v.) Ir. dúd “ear, horn, pipe’; düid «lower neck: cf. düideán (‘neck, throat', fr. *düdion-); OFris. tüte ‘mouth’; Fris. tüt, wd: tut, tute ‘spout, nozzle’; Du. tuit ‘spout, nozzle; tip, peak’. See (1); ME tout ‘arse’; Sw. tut ‘snout, pipe, larynx; tip’; Li. dudà 'reedpipe'; Latv. dūda ‘flute’. Here belong also Ir. dúd ‘tingle in the ear": Du. tuiten, v. id.
dudukos ‘tufted, hoopoe’ LG cf. tutig ‘fond, silly’; Cz. dedek ‘hoopoe’; Li. dudùkas, id.
düdul- ‘swing, sway; jaunty; cocky person" Arm. cf. totyey *moor-buzzard'; Du. tuitelen ‘totter’; Fris. cf. tütel ‘sweetheart’; Latv. iso- phone in dūdulis ‘horn, for playing
düduró, ið ‘hoot, drone’ Arm. ttřem ‘fart’; Du. cf. variant in toeteren ‘hoot, toot’: Fris. tüterje, id. (fr. *dōdərið/ *dūd-); LG cf. tuterig ‘confused’; Tuterkram ‘nonsense’; Blig. dádrja ‘mutter; twaddle’; Latv. cf. dudināt ‘roll, as thunder; mutter
duio (doubt. Cf. duoi-, dui-, dueiio, du-, etc. WP I, 819 Gk. cf. duázo, id.; ON tyja, id.; cf. Alb. dyzoj
167
“fold, double’; ndër-dýzash (tin doubt, fr. *entro-, *duia-)
duk- (theme of deuk- ‘pull’, etc.). WP I, 780 Gk. cf. endukés ‘hearty’; Alb. nduk “pull out hair’; Lat. dux, gp ducum; W dwg ‘bearing, carrying; OHG heri-zogo ‘leader; MHG zoc, gs zoges
```


## [2026-09-05T18:05:01.911Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la BQT_v2_pages.txt && grep -n \"pdf page\" BQT_v2_pages.txt | head -5 && grep -n \"pdf page\" BQT_v2_pages.txt | tail -3 && echo \"---- search darreh/dorridan\" && grep -n \"درفش\\|دریدن\\|درّه\" BQT_v2_pages.txt | head -40"
}
```


### [2026-09-05T18:05:02.002Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4339896 Sep  4 14:06 BQT_v2_pages.txt
---- search darreh/dorridan
3834:   ‫شهمیر زادی ‪٣‬لا‏ ك ‪ ۲ .‬ص ‪ ۹۷۱۰‬ک»یلکی ‪.۲8086‬ساس کرت ‪٩( ۲21200‬‏ چترشاهی‪,‬درفش‬
4627:      ‫وحلهٌ یوتاندن» حفاطت؛ چترآفتابی» آفتاب گیر؛ ‪6‬و‪( 5201201‬درفش‌شاهی) «وبلیامز ‪٤٩٤:۱‬‏ *‪.‬‬
8328:               ‫و زدست زبان حرف گیران رستند‪.‬‬                    ‫کاغذ بدریدند و قلم بشکتند‬
13237: ‫درجایی باشد مالند سوزن و جوال دوز و درفش‬
17552:‫درفشان ‪ = ۴‬بروزن درختان » بمعنی‬                     ‫دزن ‪ -‬کنابه‬
17565:‫فا وشین قرشت » افزارست کفش دوزان و امثال | کشیده ‪ .‬همان درفش‌کاوان است که علم‌فربدون‬
17585:        ‫‪۱‬‬                                            ‫‪ ۲‬اسم فاعل از« درفشیدن» («‪.‬م‪: ).‬‬
17586:        ‫مفكتاب فروزان شده ز روی زمین‪.‬‬                         ‫بك آفتاب درفشان شده زروی سپهر‬
17588:  ‫‪ -‬فشان (فشاننده) ‪ ,‬آنکه در‬       ‫‪ - ۸‬درفشان م اول وسکون دوم وفتح سوم » از ‪ :‬در‬
17592:  ‫خود مانند گاو درش در جنبش‌باشند‪ ».‬در متن اوستابجای گاو درفش ‪ 2۳5/2۳1 ۰‬لاڇ ‪ 6‬ودر‬
17593: ‫تفسیر پپلوی «کاو درفش » بعنی علمگاو آءده ‪ .‬ابن لغت درست یادآور درفش کاوبانی‌است که‬
17597:                           ‫بردن بکسی باشد ‪.‬‬        ‫درفشه = بم اول وثانی وسکون‌فاوفتح‬
17620:                                ‫‪ - ٩‬درفشی کردن ب‌عنی مشهور کردن » رسوا کردن‪: ‎‬‬
17634:          ‫همی خواندش کاویالی درفش ‪.‬‬                     ‫فروهشت از زرد وسرخ وبنفش‬
17636: ‫بنا بقول ابوربحان ( آثارالبافیه ص ‪ ) ۲۲۲‬ابن رابت که « درفش‌کابیان » نام داشت‬
17638: ‫نوسد ‪ « :‬درفش کایبان یعنی علم‌کابیان ‪ ,‬کیکه بضرحاك شورید تا آفرویدن ضحاك را بکشت ‪.‬‬
17639: ‫درفش کابی از پوست خرس بود و نیز کویند از پوست شیر بود ‪ .‬پادشاهان فری آنرا فرخنده‬
17648: ‫کرد کهآ را ازچوبه گبررفتند وخود درفش را باره باره ومیان‌سلمانان قسمت کردند‪( ».‬غرراخبار‬
17654:  ‫قیمت جواهر درفش به ‪ ۶۰۰۰۰۳‬لیر انگلیسی تخه‌ین شده است ‪ ( .‬پور داود ب‪.‬سنا اص ‪۵۷۱‬‬
17823:‫وممنی درفش است که افزار دفش دوزان و امثال‬      ‫رد ‪ -‬وبا واو مجهول» چوب‬
17847:  ‫‪ = ۴‬درفش («‪.‬م‪ > ).‬دراراك (ساطانآباد) بدین معتی ‪5۷00۳3‬‬                      ‫هوشمان اساً ‪.‬‬
17860:  ‫آشکار است که «دروش» درین شمر سوزنی ضبط دیگری از کلمة « درفش » (« م‪ ).‬فارسی است‬
17861:  ‫که هنوز در زبان فارسی رایج است و «داغ درفش » گوبند و از قدیم در ابران معمول بوده است‬
17862:  ‫که برای امتبازچهاریابان وستوران دربهارهر سالگرء هابی راکه درهمان سالزاده میشدند بادرفشی‬
17864:  ‫واین‌عمل‌داغ‌زن‌را«درفشرداغ *یا«داغ‌درفش؟میگفتند‪.‬درین‌صورت له دروش کلم تازست وله بمعنی‬
17865:  ‫‪ -‬رك‪ :‬درفش ‪.‬‬     ‫شاست‪.‬معید نفسی‪ .‬دربارة چندلفت فارسی‪ .‬بادناءة پورداودج ‪. ۷۲۲4‬‬
17866:             ‫‪muincyroD = ۸‬‏ «لك ‪ ۲‬ص “‪1A‬‏ ‪.‬‬               ‫‪ ۷‬سکر‪ :‬درفش ‪.‬‬
21534:  ‫‪ - ۴‬از ‪ :‬دهان ‪ +‬در (دریدن) ‪٣‬‏ ‪( ۰‬پسوند اسم مصدر ) ‪.‬رك ‪:‬‬                          ‫ورك ‪ :‬آژى دحاك ‪.‬‬
```


## [2026-09-05T18:05:08.356Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('npages',len(pages))\nimport re\n# find page index containing certain line\nfor i,p in enumerate(pages[:3]):\n    print('---',i,repr(p[:300]))\nEOF"
}
```


### [2026-09-05T18:05:10.210Z] TOOL RESULT

```
npages 684
--- 0 ''
--- 1 '                                         \u202b\u202a7\u202c\u202c\n\n                          \u202bرن\u202a۳\u202c\u202c\n    \u202bنات\u202c\n      \u202bا م\u202c\n              \u202bلض\u200cبال \u202a ۰ ۲۶\u202cرک\u202c\n\u202b\u202a۱\u202c\u202c       \u202bاسا تعدولیدیارتم و\u202c\n                                     \u202b\u202a7\u202c\u202c\n\u202b\u202a ۰\u202cو زل رسوا »وا روون لات سا روصا مواقم\u202c      \u202bوتان\u202c\n\n                      \u202b\u202a۴2 ۱\u202c\u202c\n'
--- 2 '                   \u202bم\u202c \u202bو\u202c\n\u202bنآکو سخنیم بیاموزد مرا\u202c\n                       \u202bد\u202c \u202bد\u202c \u202bل\u202c \u202bج\u202c \u202bم\u202c \u202bة\u202c \u202bچ\u202c \u202bا\u202c \u202bی\u202c \u202bد\u202c\n\u202bعلى \u202a۰\u202c\u202c             \u202bبند گر دا ند \u202a۰\u202c\u202c                       \u202b\u202a۳\u202c\u202c      \u202b\u202a۳7\u202c\u202c\n\n\u202bداربان مقدمهٌ مجلد اول برحان قاطع ( صفحدٌ صد وسی ودو ) نگارنده از\u202c\n                                   '
```


## [2026-09-05T18:05:13.380Z] TOOL CALL #18: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:845 2>&1 | head -60"
}
```


### [2026-09-05T18:05:15.243Z] TOOL RESULT

```
no scan of BQT covers printed page 845 (see 'scans' in refs_online.json)
```


## [2026-09-05T18:05:17.769Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\nEOF"
}
```


### [2026-09-05T18:05:19.309Z] TOOL RESULT

```
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
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt"
 ],
 "page_offset": "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').",
 "covers_etymology": true,
 "notes": "Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Provenance caveat: picofile is a general file host, the uploads are not from a library; treat as a grey copy (the book is in copyright in Iran). | vol 4 (م–ی) OCR text, tesseract fas+eng, pages tagged [pdf page N], printed = pdf+1917 | vol 5 (ta'liqat) OCR text, printed = pdf-5 | vol 3 (ش–ل) OCR text (689/721 pages), printed ≈ pdf+1203..1209",
 "scans": [
  {
   "volume": "3",
   "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf",
   "first_printed": 1208,
   "last_printed": 1925,
   "pdf_offset": -1205,
   "page_map": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json",
   "lang": "fas",
   "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt",
   "ocr_note": "689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py"
  },
  {
   "volume": "4",
   "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf",
   "first_printed": 1920,
   "last_printed": 2475,
   "pdf_offset": -1917,
   "lang": "fas",
   "offset_note": "printed = pdf+1917, checked at pdf 150 and 500",
   "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt"
  },
  {
   "volume": "5",
   "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf",
   "first_printed": 1,
   "last_printed": 290,
   "pdf_offset": 5,
   "lang": "fas",
   "note": "vol 5 = ta'liqat (addenda) with its own pagination 1-290; cite as BQT5:<page>. Plain BQT:<n> with n<1208 refers to vols 1-2 (OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt), not to this scan.",
   "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt",
   "requires_volume": true
  }
 ],
 "cites": "page number, continuous across the five volumes of Mo'in's edition (1342/1963 = Amir Kabir 1362 reprint); Mo'in's etymological footnotes are the cited material"
}
```


## [2026-09-05T18:05:24.325Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(293,308):\n    p=t[i]\n    print('='*20,'leaf',i,'=> printed ~',i+543)\n    print(p[:1400])\nEOF"
}
```


### [2026-09-05T18:05:25.878Z] TOOL RESULT

```
<persisted-output>
Output too large (31.4KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/b2x04jlmq.txt

Preview (first 2KB):
==================== leaf 293 => printed ~ 836
   ‫ے‪6‬‬
  ‫درحسی‬                                                                                        ‫سح‬     ‫‪۳۳‬‬



‫از زنبور سياه هم هت که چوب را ضوراخ‬                      ‫درج تنگ کنایه ازدمان معشرق‬
                                         ‫میکند ‪. ۴‬‬                                                    ‫است ‪.‬‬
‫درختلك دانا س بکر کاف » دم‬                               ‫درح ‪ ۱‬كر = ضم دال دوم » بمعنی‬
‫فهتأاب بکرددبر کپای‬       ‫درختی‌است که بپرجانب ک‬         ‫اهیه ازدهان معشوق باشد ‪.‬‬
                                                                                ‫درج تنک اکستنک‬
 ‫کوبند درخت‬ ‫ی‬ ‫ض‬ ‫ع‬ ‫ب‬ ‫و‬ ‫‏‬ ‫‪٩‬‬ ‫آن رویجانب آفتاب کنند‬         ‫در ح دهقان = کنابه کاتزاب تاریخ‬
                             ‫وقواق همان است ‪.‬‬
                                                         ‫و قول‬     ‫است‪ .‬چه دهقان مورخ را می‌گویند ‪۴‬‬
 ‫سنبه ‪ = °‬بفتح لون «معنی‬             ‫د‬
                                 ‫حرتنه‬                       ‫عوغتبرر‬
                                                                   ‫دهقانرانرزکویند‪ -‬وبمه‌نی‪-‬خن معمتبر‬
‫درخت ابه است که پرنده‌ای راشد که درخت را‬                                                        ‫‪.‬‬     ‫هم هھ‬


    ‫با منقار سوراخ‪ .‬میکند ودرختینه سنبه ه‬
 ‫آمده‬                                                    ‫در جگر گل گرفتن «کناه‌اززر‬
           ‫است که بعد ازفوقالی تحتالی باشد 
==================== leaf 294 => printed ~ 837
  ‫—‪~Art‬‬                                                                                                    ‫درخشان‬

‫ثالثو سکون‌واومعدو له‪,‬‬    ‫دق‬   ‫=‬    ‫خور‬       ‫در‬           ‫اوینا کرده است ‪ -‬ونام دهی استازولات قابن‬
  ‫بمعنی لایقو سزاوار ودر وسم‪-‬و در خورشید‪8‬‬                   ‫وقهستان‪ ,‬ودرا تساکلیم راخوب میبافند‪ -‬وبمعلی‬
                                ‫‪ -‬ودرطمام باشد ‪. ۷‬‬
 ‫با واو ممدوله بروزن شب‬                 ‫د‬
                                        ‫رخو‬
...
</persisted-output>
```


## [2026-09-05T18:05:29.610Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i in (295,296,301,302,303,304,305):\n    p=t[i]\n    print('='*20,'leaf',i,'=> printed ~',i+543)\n    print(p[:2500])\nEOF"
}
```


### [2026-09-05T18:05:31.601Z] TOOL RESULT

```
==================== leaf 295 => printed ~ 838
  ‫درسار‬                                                                                         ‫سم پوس‬
        ‫ند‬
         ‫گحقوکسی‬
               ‫است که سخنان بد ولالایق در‬                ‫فش کن »‬
                                                               ‫درذهی = بمایم بروکزن‬
 ‫درر کر دن ‪ -‬کنابه از فاش گردسن‬                            ‫مخغاف دردمئتد استت که ‪.‬ردم افتاده و دردداك‬
                                                                                         ‫‪¥.‬‬   ‫وخا" کاریاشد‬
                            ‫آوشکارا شدن باشد ‪.‬‬

 ‫دررمان ‪ = °‬بفتح اول وئالی بر وزن‬
                                                         ‫سیاره‌را گویند که زحل ومشتری ومریخ و آفتاب‬
‫تمکدان » رشته و رسماق نافته را گوبند که در‬
                                                                           ‫وزهره وعطارد وقمر باشند ‪.‬‬
                                  ‫سوزن کشند ‪.‬‬
                                                           ‫در دور ‪ -‬ضماول واك‌بروزن پرزوره‬
 ‫درون ‪ - ۱‬بروزن‌ارزن» به‌منی سوزن‬
                                                         ‫وگوشد‬      ‫گرداب مهلك وغرق کننده را گویند ‪۰‬‬


                                        ‫زند ‪. ۷‬‬
                                                           ‫در ذه ‪ = ۴‬صم‌اول بروزن مرده ‪ ۰‬دردی‬
 ‫درز فف = بر وزن فرزند » جای بسیار‬
 ‫ربزشی را گودند اعم ازجنکه گاه ومسلخ‪.‬‬          ‫خون‬
                                                                    ‫شراب وآب وروغن وامثال آن باشد ‪.‬‬
                                                         ‫= صم اول » کنابه از کربه‬    ‫در ر یی‬
 ‫‪3‬رد ه = بروزن هرزه‪ .‬توده وبشتةً علف‬
‫وخار وخاتاك باشد ‪ -‬و بمعنی درز هم هت که‬                           ‫کک وک کو د کن با‬
 ‫چاك دوخته باشد ‪ - 4‬ودختر رایز کوند ‪- ۸‬‬                  ‫درر ‪ = ۴‬بروزن لرز » شکاف جامه را‬
 ‫است که‌درژه‬   ‫ویمعئی اول ا رای فارسی همآمده‬               ‫کوندکه دوخته باشند‪ -‬ودختران کوچك سالرا‬
                                       ‫باشد ‪¥.‬‬                                                ‫ندز گفته‌اند ‪۲‬‬


‫در سار = باسین بی‌قطه بروزن اغیار‪,‬‬
‫درقلمه ومسوطه وخانه‬     ‫دبواری باشد که در مش‬             ‫تخته‌ای بکاهش‌دآسیابانان درییش آگبذارند تا‬
‫یکشند چنانکه درقلعه و خاله تمودار لباشد تب‬                 ‫آب بطرف دیگر رود و آنرا درزاد آسیا یز‬
‫وبرده‌ای رانیز گونند که دریش درخانه يباویزند‬                                                       ‫گوند ‪.‬‬
                ‫سویمعنی ذر گاء نزآمده‌است ‪۹‬‬              ‫درر بان ‪۵‬اشتین د کنابه 
==================== leaf 296 => printed ~ 839
                                                                                                                               ‫درساره‬
                             ‫ونندرمتی هم هت ‪. ۴‬‬                      ‫روزن کهواره ‪ .‬بہمنی درسار‬
                                                                                             ‫دمر‪-‬سپار‬
‫درستان ‪٩‬‏ = روزن‌دمکدان‪ .‬شاگردانه‬                                    ‫است که دبوار پش درفلمه وخانه و پرده باشد »‬
‫باشد وآن‌درمی جلف است که دعك ازاجرت استاد‬                            ‫است »چه ساره‬           ‫ومعنی تکریبی آن لپزرددره‬
                                        ‫‪ ۱‬بثا گرد دهند ‪8‬‬                                                       ‫پرده را گونند ‪:‬‬
 ‫درستاران ‪ -‬بفتح اول وثانی بورزز‬                                      ‫درسو ر = بابای‌قارسی بوزرن‌برفروز»‬
‫که شا کرد انه‌باشد ‪.‬‬     ‫بمعنی‌درستان‌است‬        ‫برستاران»‬
                                                                     ‫امرازسپوختن باشدا که بعنف دراندرون کردن‬
‫درسته س بفتح اول وثائی بروزن‌لبسته‪,‬‬                                                             ‫است یعنی در اندرون کن ‪.‬‬
‫و گذشتن آزجرام وششدن‬                   ‫یمعنتی عفو ورحمت‬                ‫درست ؟ د جنم اول و ثاسبیکوون‬
                                         ‫‪.‬‬   ‫گناه باشد ‪۷‬‬             ‫ثالث وفوقالی؛ لقض‌شکته وغاط باشد؟ وبعربی‬
‫در سمی ‪ = ۸‬بذم اول و فتح الث بر‬                   ‫صحیح‌خوانند؟ ‪-‬وبمعنی درهم ودینار وزری‌باشد‬
‫ه در‬ ‫ک‬ ‫ت‬ ‫س‬ ‫ا‬ ‫ن‬ ‫ا‬ ‫ر‬ ‫و‬ ‫ا‬    ‫م‬ ‫»‬
                            ‫ا‬ ‫ن‬ ‫ی‬ ‫ت‬ ‫ف‬ ‫ل‬ ‫ا‬ ‫ن‬ ‫ز‬ ‫و‬ ‫|‬ ‫‏‬ ‫که بااششترفهیازداردوبعربی طازجه خوانند ‪٩-‬‬
‫وبند وبمعنی حت | حبالة بپرام بود ‪٩‬‏ ‪ -‬وبکرثالث بروزن مفلی‬             ‫وزروسیم وطلاو نقره را نگیز‬

                                                   ‫‪۰‬‬         ‫‪:‬‬
                                                        ‫سپوختن‬              ‫امر از ‪ ۶‬در سیوختن »‬
                                                                           ‫رك‬                                  ‫‪-‬‬       ‫‪۱‬‬
     ‫‪ ۴‬پ‪-‬پلوی ‪( 4511۲1‬سالم م»تقبم ؛ راست) «منای‪« ۲۷۲:۳./5۷۳‬تاوادیا ‪۰۹۳۰‬‬
 ‫و ‪ . 6510۳1‬از ابرانی‌باستان» قرب ‪ithsrd-urd‬‏ ‪( L_ithsrd_avurd# #‬درست‪.‬سالم)‬
     ‫از‪ , ۸ 2۷۷۳-‬اوستا ‪ ۰ 2۷۲-‬بارسی باستان ‪( 2۷۲۳0‬الم) «بارتولمه ‪۵۷۱۳0 ۰12 ۷۸۷‬‬
  ‫«ندی پاستان ‪٤1‬ا‪5۲‬‏ (نظرء نگاه) ‪ .‬رك‪۲ :‬ر گے ‪۰۹ ۹۵‬؛ کردی ‪۶11۲‬لا (راست‪ .‬صحیح)»‬
 ‫‪:‬‬     ‫ورك‬   ‫>‬   ‫‪6‬‬   ‫‪ ۰‬تمام ( ”سدق‬       ‫) کامل‬        ‫‪tsürd‬‬   ‫‪.‬‬ 
==================== leaf 301 => printed ~ 844
 ‫دروا‬                                                                                                      ‫ب‪۱‬ح‬


‫گونشد‪ -‬و نمعتی وقت‬      ‫‪ ۹۳‬وهللا کت راز‬    ‫ومحنت ‪6‬‬         ‫ين‬
                                                            ‫اول و فستح‬              ‫در مسرا اتاک‬
‫وساعت وزمان باشد ‪ - ۱‬ویم‌نی‌ئبات وآرام ‪١‬‏ ۔‬                             ‫باشد‬   ‫‪٤‬‏ دار المرب وضرانخانه‬   ‫می‌قطه(‪)۱‬‬

‫وتأخبرهم هت ‪ - 1‬وعالمآ خرت رانز کفته‌اند‪-‬‬
                                                          ‫‪-‬ف فارسی ‪ ۰‬صراف‬
                                                                        ‫دبرمنگ‌زفکنا‬
‫نمام ‪(۱۲‬‬       ‫درکات‬     ‫اشاره است‬     ‫و ترد موقن‬
                                                                                                         ‫را گویند ‪۱‬‬
 ‫محبوس‌ودن‪.‬‬     ‫بازماند گان و بقمد تغیدات وهمی‬
                                                           ‫درمل = بورزن بلبل » غله رکاویند‬
‫دنرگیدان‪ ۷‬د بکراول‪ .‬بعنی‌درنگه‬
                                                          ‫که هنوز خوب نرسیده باشد وآنرا بربان کنند‬
‫کردن است که ثبات و آرام ورز‪,‬دن ‪ -‬وتأخیر‬
                                                                                                          ‫وخور ند ‪.‬‬
                                       ‫کردن باشد ‪.‬‬
                                                          ‫در میان بودن = بمعئی در رهن ودر‬
‫نون‬     ‫بفتح‬     ‫زهادن =‬        ‫در ورد‬
                                                                                 ‫گروبودن باشد ‪.‬‬
‫و واو ک»نابه ازدرهم پیچیدن ‪ -‬و ینهان کردن‪-‬‬
‫و بی نام و تان ساختن ‪ -‬و در ‪-‬وراخ نهادن‬                   ‫درن = بالون وحرکت‌غیرمعلوم» زلورا‬
                                               ‫باشد ‪.‬‬
                                                          ‫در‬    ‫و‬       ‫کویند اکر او را خعك ساز ند‬         ‫بکشد و‬

 ‫كر نه س بکراول وسکون انی فوتح‬                            ‫شیشه کرخانه بخور کنند هرشيشة کبودی که در‬
          ‫ثالث » تبغ وشمشیر آبدار راکوبند ‪2.‬‬                                     ‫آنجا باشد بشکند و باقی نماند ‪.‬‬
‫در وا = بفتح اول وسکون انی و واو‬                          ‫در ند د بروزن سمند » بمعتی شکل‬
‫سردان و حیران‬
            ‫بالف کشیده » س رکشته و ک‬                      ‫ودمایل وصورت ومانندوسان‌باشد چتانکه گویند‬
‫باشد ‪ - ۸‬وسرنگونآو‪.‬خته ونگون وبا کونهرا‬                                  ‫فلك درند یعتی فلك سان و فلك مالند‬

‫یز کویند ‪- 4‬وچیزی‌ذرورقوحاجت ومابحتاجرا‬         
==================== leaf 302 => printed ~ 845
  ‫‪~A‬‬                                                                                              ‫حره اج‬

                                                      ‫فام سلاطین وبزرگان هندوستان است ‪ -‬وبمعنی‬
                                                      ‫درست وتحتیق هم‌آمده است‪ ۷‬؛ ودروای باضافة‬
                                                                                     ‫تسانی تدز گفته‌اند ‪۰‬‬
‫باشد کهبر دو طرف راه از برای شان فرسنگك‬
                                          ‫صاز لد ‪.‬‬    ‫درواخج ‪ = 5‬بفتح اول وسکون آخر‬
                                                      ‫قطه دار باشد » حالت برخاسن از‬              ‫که خای‬
 ‫درو انه = بر وزن پروانه ‪ ۰‬سوراخی‬
‫باشد که بربام خانه کنند واردیان برآن گذاشته‬            ‫بیماری باشد که بعربی نقاهت گوبند و‪-‬بمعنی‬
                                                      ‫شجاع و دلیر ‪ -‬و شجاعت ودلیری ‪ -‬و محکم‬
                            ‫برالوالد ویزیر ایند ‪.‬‬
                                                      ‫ومضبوط ایزنگدفتسهو‌ایمعنی‌بقین ودرست وتحقیق‬
 ‫درواه ‪ = 1‬بر وزن درگاه " بمعنی‬                      ‫همرت کهلقیض کمان باشد ‪ -‬و بمعنی درشتی‬
          ‫سرلگون ‪ -‬وحبران ‪ -‬وضروری باشد ‪*.‬‬            ‫؛ و بجای حرف‬        ‫و علظت نیز (‪ )۱‬آمده ات‬

 ‫دروابست ‪ = ۳‬بروزن ومعتی‌دریاست‬                       ‫تائی زای فارسی هم گفته‌اند ‪ -‬وعیب وعار رایز‬
                                                                                                  ‫ّي‬
             ‫باشد که ضروری ومایحتاج است ‪.‬‬
‫درو بطارس ‪ ۰ ۵‬بح اول و ثالی‬                           ‫درو ار ‪ - ۲‬بر وزن خروار » بمعنی‬
 ‫بواو رسیاه کوسربای ابجد (‪ )۳‬وطای حطی(‪)4‬‬              ‫درواب تاست که‌خروریومابستاح باشد‪.‬وسرگشته‬
 ‫ھا ن هر دو‬      ‫و ن‬    ‫ورای مکور‬      ‫بالف کشده‬
                                                                  ‫وسرنگون وحىراقرا همگویند ‪¥.‬‬

                                                      ‫بقتح اول ‪ 3‬سکون آخر‬            ‫از ‪۳‬‬       ‫درو‬

 ‫وآن بشتر بر درخت بلوط کپنه پبهیده شود ‪.‬‬              ‫که زی فارسی باشد » بمعتی دروار است که‬
‫اکرآنرا باشاخ وب رک وبیخ بکوبند و بربیغ‬               ‫وبمعنی‌سررنگون‌هم‬    ‫و مایحتاج ود ‪-۴‬‬            ‫خروزی‬
‫و فالج و لقوه‬    ‫»‬   ‫ضماد کنند موی را سرد‬      ‫موی‬                                               ‫هنت ® ‪.‬‬
                                  ‫‪۰‬‬   ‫را هفك است‬


 ‫درو ‪ - 3‬بروزن سرود » بمعنی صلوات‬                                                           ‫کوش باشد ‪.‬‬
 ‫ات ‪٩‬‏ خکد
==================== leaf 303 => printed ~ 846
 ‫دروقیئون‬                                                                            ‫مرت‬
‫میگشاید وبعربی مبضم خوانند ‪ ۴‬؛ وباین ممثی‬     ‫استغفار واز انان سناش و دعا وحیوانات دیگر‬

‫بفتح اول همگفته‌اند ‪ -‬و با واو معروف درعربی‬    ‫تسبیح باشد ‪ -‬و نام روز پاجم امت از خمة‬
‫داغ وشاترا خوانند ‪ - 6‬و بکر اول بر وزن‬         ‫مترقةٌ سالهای ملکی ‪ -‬وماضی دروندن‌هم‌هست‬
‫وممنی درفش است که افزار دفش دوزان و امثال‬      ‫رد ‪ -‬وبا واو مجهول» چوب‬
                                                                     ‫یعتی غله را دکرز‬
‫آتیاباشد؟ ‪ -‬وطم روزجنکه را کهممته‌اند ‪-‬‬        ‫ودرخت وتخته باشد وچوب نراش را ازین جهت‬
‫وفوطه را یز کونند که درروزجنگه‌بربالای خود‬                          ‫برند ‪*. ۴‬‬    ‫وگ‬‫کود‬
                                                                                     ‫در‬
‫آهنین ودستار بندند ‪ -‬و بمعنی روشنی آهمده‬      ‫در ودن ؟ د بروز نکشودن‪.‬در وکردن‬
                                 ‫است ‪#. ۷‬‬
                                              ‫و بربدن غله باشد ‪ ۰‬و درو يدن هم باین معئی‬
                                                                                        ‫أت ‪.‬‬
‫درو فینون‪ -‬بفتح‌اول وثائیبواورسیده‬
‫وقاف مفتوح و تحتالی ساکن ولون بوواکشده‬         ‫دروش ‏ م اول و واو مجهول بر‬
‫متی ‪ ۸‬و بعنی‬
           ‫رتیواس‬
                ‫و بنون دیگر زده » لف‬           ‫نشتر<جام راگوبن دکه بدان رکه‬         ‫وزن صروش»‬


 ‫‪ - ۴‬دردخهة خطی «لفت محای شوشتر» متعاق‬                ‫» دروندنل ‪.‬‬   ‫‪ - ۷‬رك‪ :‬درودن‬
 ‫بكتابخانة علامه دهشدا لز آهده‪ :‬درود یمعتی جوب و تخته و درخت و از بجهت جوت تراش را‬

 ‫‪ - ۴‬از‪:‬درو ‪« ۵۲‬هوشمان‪۹۵‬ه» ‪٣‬‏ دن* بوندمصدری؟پاز دد‪ .0۲4 01‬کردی‬                ‫ند‪.‬‬
                                                                                ‫کر‬‫وی‬
                                                                                   ‫کود‬
                                                                                     ‫در‬
 ‫ور ‪:‬‬       ‫‏‪( dirûtin . dirûn‬درو کردن) ‪nûrid ۰‬‏ (درو) ‪ ۰‬وخی ‪ma‬‏ _ ‪ » ward‬اسذق ‪٩‬‏‬
  ‫‪ = ۴‬درفش («‪.‬م‪ > ).‬دراراك (ساطانآباد) بدین معتی ‪5۷00۳3‬‬                      ‫هوشمان اساً ‪.‬‬
 ‫‪ _9‬ابن استنباط ادرست را ازین بيت‬               ‫) « مکی‌نژاد » ‪.‬‬      ‫ان‬
                                                                       ‫اانجو‬
                                                                           ‫رفاث‬  ‫( آل‬
                                                                              ‫ست ک‬
    
==================== leaf 304 => printed ~ 847
 ‫)‪“1‬‬                                                                                                  ‫دروك‬




 ‫باشدا ‪ -‬ونام شهربست (‪ )۳‬درخراسان مابن مرو‬                ‫کوبند بونالی است » بمەنی نباتی کهبدرخت‬
‫وناکه‌آنها یز دوشپراند © ‪ -‬وینم اول پیمانة‬                ‫زیتون ماند لکن از بك کز کوناه تر میباشد‬
‫غله راء‌گوبند ‪ -‬و دعابی باشد که مفان درستایش‬             ‫وبر کش درازتر از برک زیتون امت وکل آن‬
‫خدابتمالی‌و ذرآخوانندویرخوردایها بدمند‪ .‬وبعداز‬            ‫سفید میشود ر تخم آن بمقدار کرسنة کوچك‬
‫آن‌بشورندا وهرچز که‌یر آن‌درون‌خوانده‌ودمیده‬              ‫میباشد و طبع آن همچوطبم بنرالینج (‪ )۱‬است‬
‫ند گوبند مشته شده و هرچیز تخوانده باشند‬
                                        ‫باش‬
                                                                   ‫واگ زیده خوزه یم کهلتز برد‬
‫تایشته یمنی‌ناخوانده " چه یشتن با نحتانی وشین‬             ‫دروك ‪ -‬م اول بروزن‌سلوك ه»یزم‬
‫قرشت (‪ )4‬وفوقاتی» بمعنی خواندن باشد بزبان‬                                             ‫پاريك رکاوبند ‪.‬‬
                                 ‫زند وپازند (‪. ۷ )۵‬‬       ‫در و گر = بض‌اول وثالی (‪ )۲‬وفتح‌کاف‬
‫درون اروده کنابه از صاحب دل‬                               ‫فارسی » مخفف درود گر الست که استاد چوب‬
               ‫وصاحب مجاهده باشدب و‬
‫کی را دگزونند که‬                                          ‫تراش باشد وبعربی‌تجار گوبند‪ -‬ویک اول وفاح‬
                         ‫دل مردمان بدست آ ورد ‪4۸‬‬         ‫ثالی‪ .‬شخصبکه غله میبرد ودروميکند ‪ ۴‬واو را‬
‫درو نج = بفتح اول و رابع و سکون‬
                                                                                ‫بعربی حصاد خوانند ‪. ۴‬‬
‫» ‪ ۰‬وآن دوای باشد‬            ‫جيم ‪ +‬معرب درو لك ات‬         ‫درون = بفتح اول » بمعنی اندرون ‪۴‬‬

   ‫(‪ )۳‬چك ‪ :‬شهری ه‌هت ‪۰‬‬                     ‫وئالی ‪۳‬‬      ‫)‪ (۲‬چك‪:‬‬         ‫بزراشیج ‪۰‬‬   ‫جك‪:‬‬      ‫)‪(۸‬‬


                                       ‫‪ :‬ژند و باژند ‪.‬‬   ‫(ه) چك‬          ‫(‪ )4‬چك ‪- :‬قرشت ‪.‬‬

          ‫‪. ۴‬از درو (هم‪( ۳ + ).‬یوند فاعلی و شنل ‪).‬‬                        ‫رك‪ :‬درود کر ‪.‬‬       ‫‪- ۱‬‬

   ‫‪ = ۴‬اندرون ( «‪.‬م‪ .) .‬اشکاشمی‬                     ‫‪ - . ۳‬حصاد درودن انت ر ک‪ :‬منتهی الارب‪.‬‬

                                 ‫‪ ۰ 00‬مریکلی ‪ « 0131‬کربرسن ‪, ۷۷۰‬کیلکی ‪: 80۲‬‬
                   ‫درون عاقت بر کن ‪۰‬‬     ‫که رش‬                      ‫حذر کن زدود دروتهای رش‬
   ‫‪‎‬ناتلکد« ‪. ۰4٩‬‬
   ‫‪ - °‬دره‌عجم البلدان و حدود العالم تیامده» اما در ذبل عالمآرای عباسی ناد شده ‪ .‬رك‪:‬‬
   ‫‪ 00۲4 _ ۱
==================== leaf 305 => printed ~ 848
  ‫دره‬                                                                                                                ‫ز‪6‬ح‬
                                                                                                                       ‫بی‬


 ‫کنابه ازشکم باشد © ‪ -‬و قوس قزح (‪- ۱ )۳‬‬                         ‫بشکل عقرب وببب آن درونج عفربی خوانندش‪.‬‬
 ‫کومان‌حلاجی رانیزکوبندا ؛ وم اول هم‌بدو‬                      ‫کرم وخشك‌است دردویم(‪ ۱)۰‬کز ندکی‌جانورانرا‬
  ‫ون‬
   ‫ک‪۳‬م)ا‬
       ‫معنی آخر است کقهوس قزح (‬                                ‫کوش اکر فدری از آن درمان‌خانه‬                         ‫افع است‬

                              ‫حلاجی ‪ ۷‬باشد ‪#.‬‬                  ‫بیاویزند از طاعون ایمن باشند‪ .‬و اکرسوراخ‬
                                                                ‫کنند ودرمیان هردوران زن حانملدهفآوریززند‬
 ‫درو لزه و درو یره ‪ ۵‬س با زای‬
                                                                                    ‫آن زن از آفتها محفوظ باشد ‪.‬‬
 ‫هوز و زای فارسی ‪ .‬هر دو آمده است برءزن‬
  ‫تحققه (‪ » )4‬بمعنی دربوزه کودایی باشد ‪9.‬‬                     ‫درو ند = بفتح‌اول بروزن فرزند »نام‬
                                                                ‫پهلوانی‌است ‪-‬ودام داروبی‌هم‌هست ‪ - ۱‬وچنکک‬
‫درو یش سلطان دل = شاره‌برور‬                                     ‫وقلاب رانیز کوبند وبعربی‌معالاق خوانند ‪ -‬وم‬
 ‫کاینات است که بیغمیر ما صلوات الهعله وآله‬                     ‫اول بده‌ذهب ونامقید وفاق‌را گویند بزیان زند‬
                               ‫وسلم باشد ‪.‬‬                                                                 ‫ویازند (‪ )۲‬؟ ‪.‬‬
 ‫دره = بفتح اول و تشدید الی» شکنبة‬                            ‫درون ‪۵‬کنآاربهه‌ازیداندرون وکینه‌ور‬
 ‫کوسفند وغیرء باشد ‪ -‬کوشادکی ميان ده کوه‬                                                                    ‫ومنافق باشد ‪.‬‬
‫رکاپریبزند ‪٩‬‏ ؛ویتخفیف ثالی از همین معنی‬                        ‫؛صفر‬
                                                                   ‫‪ -۳‬بروزن عروسك م‬                        ‫وك‬
                                                                                                            ‫نرل‬
                                                                                                              ‫د‬
 ‫دارد‪ -‬ونام‌ولاتی‌هم‌هت ازملك بدخشان که مردم‬                   ‫درون باشد » و بیخی است دوایی شبیه بعقرب‬
‫آنجا یخوش صورتی مشپورند و انارخوب درا لجا‬                       ‫که آنرا درونج عقربی گویند » و درونج معرب‬
```


## [2026-09-05T18:05:46.397Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(306,312):\n    print('='*20,'leaf',i,'=> printed ~',i+543)\n    print(t[i][:2200])\nEOF"
}
```


### [2026-09-05T18:05:48.064Z] TOOL RESULT

```
==================== leaf 306 => printed ~ 849
   ‫نت‬                                                                            ‫درة آسمان‬
‫همآمده است ‪ -‬و بکراول درفربی آلت ضرب | باشد وآن زرست‌رايج ووزنیاست معروف ‪.۷‬‬
‫بررزن سررشته» بمعنی‌جود‬     ‫رشت‬
                              ‫ه‬ ‫د‬                                              ‫وزدارا گوبند ‪.‬‬
                          ‫در آسمان ‏کنابهازکهکنانانت‪ | .‬وعطا وکرم باشد ‪#.‬‬
‫در هم بقلی ‪ = ۲‬مشهور أست ‪٠‬‏ وآن‬                                    ‫وآارا بعریی مجره خواند ‪.‬‬
‫زری بوده‌منتوب برای ‪,‬هودی کهآ را رای‌الیفل‬        ‫هرام » بروزن فرجام ؛ یمعنی درهم‬
                                                                                ‫د‬
                                     ‫رك‪ :‬بشلی ‪.‬‬    ‫‪۴‬‬         ‫‪ - ۱‬رك ‪ :‬درهم » درم ‪.‬‬

                                                                           ‫شه از صفسه ‪۵6۸‬‬

  ‫‪ #‬درهم ‪ -‬بفتح اول وسوم » از‪ :‬در (حرف اضافه) هم ؛ شوش ‪ .‬مختلط‪ .‬شوریده؛‬
      ‫دلتان ‪. ۳:۰‬‬
                ‫را) ونفی کنند تاچندین دزهم چرا گنت ک‬            ‫اد‬
                                                                 ‫شزیندش‬
                                                                      ‫(ودی‬
                                                                         ‫آشفته‪* :‬ملك فرم‬
          ‫(ك‪ :‬درم) ‪.‬‬
                   ‫وفتح (رکسر) سوم » معرب» واحد كوك نقره و واحد وزن ر‬                  ‫وکل‬
                                                                                         ‫رای‬
                                                                                           ‫م‬
  ‫‪ #‬ورویش ‪ .-‬شنح اول » پپلوی ‪hsöyird‬‏ ( فقیر؛ تھی دست ) « ای ‪> ۲: ۲۷۲‬‬
 ‫رتا‪00‬ع‪ . 120‬بازید ‪ . 05۵67780‬هردواز اوسا ‪« 11081۳-‬بارتولمه ‪ . ۷۷۷‬شک کلمه[ شکر‬
  ‫و رك‪ :‬اسشق وهوبشمان ‪ 4۵۵‬؛ دولف «تفس» اصلآ نرا ”در بیش بمعتی‬             ‫ست‪ .‬رك‪ :‬لبر که‬
   ‫قتام الیاب دانته‪ .‬وغالباآترا بممنی ( گدای درخاله ها) گرفته‌الد ف«ولری ‪ . ۱.‬ص ‪٩۳۸: 2‬‏‬
  ‫‪ 04۸ ۳‬ولی ابن اشتقاق عامیانه است ‪ .‬رف‪ :‬مقالة ‪ ۴۲۴‬درباب تاربخ عرب در‪۵‬ا‪1‬ا‪٩06۳‬‏ ج‬
   ‫‪ ,‬شمارء *س‪۹۸‬ه‪ .‬در چپار مقالة نظامی عروضی (ص‪)٩۸‬‏ نام شاهری «پسردرغوش ‪٩‬م‏ده‬             ‫‪۷‬‬
                             
==================== leaf 307 => printed ~ 850
  ‫دربا‬                                                                                ‫==‬

‫عالمبدر گاءاومیامدندوزبان‌یکدیگر رالمیفهمیدند‬       ‫میکفتند و آن زر برابربك کف وستی (‪ )۱‬بوده‬
 ‫بهمن فرمود تا داشمندان زبان فارسی را وضع‬          ‫یمتی آلمقدا رکه چون دست راپهن سازند وآب‬
 ‫کردند و آدرا دری ام نهادند یعنی زبالیکه‬                     ‫بر کف دست بربزند پرایر ابستد ‪.‬‬
‫بدرگاه پادشاهان تکلمکنند ‪ ۳‬وحکم کرد تادر‬            ‫دری‪ = ۱‬بفتح اول بروزن پری » لفت‬
 ‫گوبند ؛ و جماعتی‬   ‫تمام عمالكث باين زبان سخن‬      ‫پارسی باستانی است » و وجه نة آلرا بسنی‬
  ‫بررآآند که وضع این زبان در زمان <مشید شد»‬        ‫بفصیح تعبیر کرده‌اند‪ ۱‬وحرلفتی که درآن نتصانی‬

 ‫وبستی دیگ رگوند درزمان بهرام ؛ ودری بدان‬           ‫لباشد دری‌می‌گوند همجو اشکم وشکم ویگوی‬
‫سبب خوانند که هرکس ازخانةٌ خود بیرون آبد‬            ‫ووی و بشنود وشنود اومثال ابنها پی اشکم‬
                                                                                         ‫ک‬
  ‫باین زبان منکلم شود (‪ )۵‬واين وجه خوبی‌تست‬         ‫وبگوی وبشنود دری باشد ؛ وجممی گویند لفت‬
 ‫چه برهر تقدیر کهفرض کنند آدرا واضمی‬               ‫ساکنان چند شهربوده است که آن بلخ و بخارا‬
  ‫میباید ووضع آلرا سببی درکاراست ‪ -‬و منوب‬           ‫وبدخشان ومرو است ؛ و بعضی گوبند دری زبان‬
 ‫پدر کوه را نیز کویند همچو كبك دری و این‬           ‫اهل بهشتاستکه(‪)۷‬رسرل سلی‌افعلیهوآ له(‪)۳‬‬
 ‫باعتبار خوش‌خوانی هم میتوان )‪(٩‬‏ بود که باشد‬       ‫فرموده اند که « لان اهل الجنة عربی او (‪)4‬‬
  ‫" زیراکه بهترین لفات فارسی زبان دری است =‬         ‫فارسی دری » وملاكة آسمان چپارم بلغت دری‬
 ‫وبا بای خطاب بممنی ظرف وظرفیت پاذد ‪۰ ۴‬‬             ‫تکلم میکنند ؛وطایفه‌ای‌بر آشد که مردمان گداره‬
  ‫در یا= ممروف‌است‌وبعریی‌بحرخوانند؟‬               ‫کیان بدان متکم‌میشده‌اند ؛ و گروهی کوبند که‬
 ‫وازد محقفین‌آشاره بذات یال واجب‌الوجود است ‪۰‬‬       ‫در زمان بهمن اسفندبار چون مردم از اطراف‬

            ‫(‪ )۳‬چك‪ :‬مله‌ال لام ‪.‬‬          ‫)‪ (1‬چيك‪ :‬چه ‪۰‬‬           ‫)‪ (۱‬چك‪ :‬بکفدستی ‪.‬‬
          ‫‏(‪ )٩‬چك ‪ :‬متوالك ‪.‬‬          ‫(ه) خم‪ :۱‬حرف زلف ‪.‬‬                  ‫(‪ )4‬چش ‪ :‬و‪.‬‬

                                            ‫‪ :‬بيست وینج ببمد‪. ‎‬‬   ‫رك‪ :‬مقدمه » ص‬       ‫‪٩‬‬

         ‫‪ ۰‬داخل هنی ‪.‬‬ 
==================== leaf 308 => printed ~ 851
       ‫با‪1‬ه‬                                                                                       ‫دریاب‬
‫دبرای بصره «کنابه ازیبالًبز رکه‬                      ‫دیراب ه بروزن غرقاب» درباراگوبند‬
                          ‫پرشراب باشد ‪.‬‬              ‫کبهحبعررخبیواند‪٩‬‏ ‪ -‬وامرازدریافتن وفهمیدن‬
 ‫ذبرای سائله ‪ -‬کنابه از دربانی‬
 ‫است که مروارید داشته باشد ‪ -‬و شراب را یز‬            ‫دریا پار ‪ - ۴‬بابای ابجد (‪ )۱‬بروزن‬
                                          ‫کن‬          ‫پهنادار » دربای برزک رگوایند ‪ -‬و نام شهری‬
 ‫دریای لعل کنابهازیباله وسراحی۔‬                     ‫همهت ‪ -‬وولاسی را نز گوند که مر کناردر با‬
                            ‫وخم پرازذراب باشد ‪.‬‬                                                ‫‪۶.‬‬
                                                                                                ‫باشد ؟ ‪#‬‬
  ‫دریای قبره کنابه از شب تاريك ‪-‬‬                      ‫در باك ‪ = °‬بروزن ومعتی ترباك است‬
                           ‫ودوات پسریاهی باشد ‪.‬‬      ‫که افیون باشد ‪ -‬ودقع کنند؛ زهررا نیز گویند‬
‫در اشم = کنابه از مروارید بزرکه‬                                                ‫ومعربآن تراق است »‪:‬‬
 ‫است که بکدانة تاها در صدف باشد ‪ -‬کونانه‬
 ‫از حضرت رسالت یناه صلوات اه عليه وآله یز‬             ‫دریا «ککشنابه ازشراب‌خواری که‬
                                                                                     ‫‪۰‬‬    ‫شود ‪۹‬‬   ‫دير من‬
                                          ‫‪۰‬‬   ‫هست‬

  ‫در بيخ افتادن ک«نابه ازانت‬                         ‫ددمعتي دربا کش ات که‬       ‫۔‬   ‫در با نوش‬


   ‫ککهسی درمقام خرابی و استیصال کسی شود ‪.‬‬              ‫رود مت‬      ‫اعت که‬      ‫کنابه از شراب خواری‬

                                                                                                   ‫نشود ‪.‬‬
 ‫در بان د ببضرووزلن‌بریدن» بمعنی‬
 ‫درو دن باشد که بریدن غله است‪ - ۷‬وبفتح‌اول‬            ‫دربای اخضر ‪ -‬کنابه از آسمان‬
                        ‫بمعنی باره کردن باشد ‪. ۸‬‬                        ‫‪.‬‬   ‫هم ھت‬   ‫ونام دریای‬     ‫‪۹‬‬   ‫اس‬



                                                                            ‫(‪ )۱‬چك ‪ :‬یابا ‪.‬‬

   ‫‪.‬‬    ‫بار (یوند مان‬      ‫از‪ :‬درا‬    ‫‪۴‬‬        
==================== leaf 309 => printed ~ 852
 ‫دربو‬                                                                                                  ‫‪٩‎‬و‬

‫و کردا کرد خانه واطراف هرچیز رادز کفته‌اند‬                ‫در یم د بکراول وانی‌سحتانیمجهول‬
‫در انداژند تا در کشوده‬        ‫و چوییکه در پس‬             ‫طمه ابست که آبرا‬
                                                                        ‫کشده و یفن نقطه دار زده »‬
          ‫لگردد ؛ ویکراول هم مده است `‬                    ‫درمقام تأسف و حسرت کویند ‪ -‬وبمعنی افوس‬
                                                           ‫شتته‬‫ذا‬‫گصیر‬
                                                                    ‫واندوه ودشوار واندوه کردن بر تق‬
‫در بور ‪ ۴‬هبسر وزن هر روز ‪ ۰‬بمعلی‬
                                                                     ‫باشد؛ وبضم اول هم بنظرآمده است ‪.‬‬
         ‫و کدابی باشد ‪.‬‬       ‫به‬
                               ‫کتدکه‬
                                   ‫دربوزه ام‬

‫در بوری ‪ = ۴‬بروزن هرروزه » بسعئی‬
                                                          ‫دریگان ‪ ۱‬بااك مجهول کواف‬
                                                         ‫فارسی بروزن حریفان ‪ ۰‬نوعی از اعمال و اشکال‬
          ‫دربوزاست که کدبه و کدابی باشد هة‬
                                                                  ‫فجومی باشد » ومعرب آن دریجان است ‪.‬‬
‫در بوش ؟ ‪ -‬بروزن خر کوش کدا‬
                                   ‫‪a‬‬


                                                         ‫در یو اس (‪)١‬ہ‏ با الك مجهول وواو‬
                  ‫ومسکن را گونند ‪۰‬‬          ‫ودرورش‬
                                                          ‫بروزن بلیناس » چارچوب در خانه راکویند =‬




                                                                          ‫)‪ (۱‬چش ‪ :‬دربوای (‪)۱‬‬

  ‫درکان ‪ 202606۲‬درهندوی‌مر کب از‪( ۱۲ = 1۲1 :‬ے) ‪ ( 20۵۷ +‬بخش»‬                                       ‫‪۱‬‬
 ‫بیرولی درتحقیق ماللهند(ص‪ )۷۰۳‬کوید ‪ 2:‬الا ثلاثو نسمی دریکان ولافائدة‬                 ‫بپر) * نی سه‌بهره‬
  ‫فی‌ذ کرها لانها ای تسمی عندنا دربجانات سنها؛‪ .‬وهمو درالتنهیم (س ‪ )4۰4‬آرد‪«:‬دریگان‌چست؟‬
 ‫وخداو ندانثان بخلاف و حوه»‬    ‫‪ ۰‬ومردمان ما آ را در بسجان‌خوانند»‬      ‫برجهااند نزديك حندوان‬            ‫هم سك‬

‫يدجم بر
==================== leaf 310 => printed ~ 853
                                              ‫يان هفتم‬
                ‫در دال بی‌نقطه با زای نقطه دار مشتمل بر ده لغت‬


                          ‫وزهره وعطارد باشد ‪*.‬‬           ‫در = بکر اول و سکون ثالی » قلعه‬
                                                          ‫بالاخاله را‬   ‫وبفتح اول کوثشك و‬        ‫‪۳ ۱‬‬       ‫وحصارباشد‬
‫فلك ‪ ,‬دمتار را گویند‬      ‫بروژن‬    ‫=‬   ‫درك‬

‫دستارچه را‬    ‫و روپاك است ؛‪ :‬و بى‬         ‫که یل‬            ‫کربند؛ و با زای (‪ )۱‬فارسی هم باين دو معنی‬
                                                                                                ‫آهوه است (<( ‪۳‬‬
              ‫گفته‌اند که دستمال وروياك باشد ‪۰‬‬
                                                          ‫رتا ‪ -‬بکراول وسکون انی وفتح‬
                                                                                    ‫داف‬
‫درمار = طم اول بروزن گلزار ‪ .‬دام‬
                                                           ‫لامحصاری‬     ‫بالف کشیده ‪۰‬‬   ‫وفای ساکن ‪۳‬‬              ‫همر ه‬
‫جابی است که‌کان سرب در آیجاست وکان نوعی‬
 ‫لزاجور دهم متصل بدانهاست وآر الاحجو رددزماری‬
                                            ‫ا‬
                                                           ‫وقلعه‌ایست که شاپوربنا کرده بوده‌است ؛ وبجای‬
                                                                          ‫فوقانی نون هم بنظرآمده است ‪#.‬‬
                                        ‫‪. ۵‬‬   ‫کو‬
                                                           ‫‪ ۳‬دال ایح بروزن بیاره‬          ‫‪9 ۳‬‬    ‫دردار‬
‫و دال أ جد‬    ‫اول‬   ‫بكر‬        ‫در ندیس ‪۰‬‬


‫بروزن فرنگیس ‪ ۰‬بممنی همانا و ظاهرا و کوبا‬                             ‫کوتوال وضابط وحافظ قلمه راکویند ‪.‬‬

‫د بکراول وسکون ثالی‬               ‫درهر چ‬                             ‫معاون وباری دهنده وثربك دزد باشد ‪.‬‬

‫وهای مفتوح برای فرشت )‪ (£‬وجیم رده » له‬                     ‫دارورای‬      ‫طینه‬
                                                                           ‫قحش‬
                                                                             ‫نبفل‬
                                                                                ‫در دافشره ‪= ۴‬‬
‫پیشینیان باشد و آنرا بسربا
==================== leaf 311 => printed ~ 854
                                                               ‫يان هشتم‬
                    ‫در دال بی‌نقطه با زای فارسی مشتمل بر سی وهفت لغت‬


‫دزاامه ه = بکر اول وفتح آخر‬                                                  ‫‪ = ۵‬بکر اول و سکون ثالی » قلمه‬
 ‫بمعنی دژکام ات که زاهد ویرهیز کار )‪(٩‬‏ ‪-‬‬                                    ‫وحصارباشد ‪- ۱‬وبمعلی زشت و‪,‬دوبدخوی وخشم‬
‫وخواجه‌سرا باشد ؛ وبفتح‌اول لز درست است‪.‬‬                                        ‫نزد‪-‬‬
                                                                                   ‫انی‬
                                                                                     ‫‌را‬
                                                                                       ‫هکی‬
                                                                                         ‫تند‬
                                                                                           ‫فبب‬
                                                                                             ‫گوچ‬
                                                                                               ‫وقهر نیزهست ‪- ۴‬‬
‫دز ] اه ‪ ۱‬ت باها بمعنی درآ پاداست‬
‫که سهمگن وخشمآ لود باشد ‪ -‬وبداندش وتند‬                                                                                   ‫‪۰‬‬    ‫است‬   ‫درست‬   ‫قىر‬




‫شده رانیز کرد ‪ -‬کووتوال و محافظت کنندة‬                                       ‫و دال‬         ‫ایجد‬     ‫با بای‬        ‫دژ] باد ‪ ۴‬ت‬
                                    ‫ذلعه را هم گفته‌اند ‪۰‬‬
                                                                             ‫بر وزن اشارات » بمعنی سهمگین و خشم آلود‬
‫دز | گه »مخنف دگژاآه است ‪ ۷‬که‬
‫خشمکن وقهرناك و‪-‬بداندیش ‪ -‬وکوئوال قلمه‬
                                                                                                                                    ‫&‬

                                                                             ‫درا گام ‪ = ۴‬با کاف فارسی بر وژن‬
                                                               ‫باشف‬          ‫زاهد‬         ‫و یمعتی‬         ‫دلارام »خواجه سرا را کت‬
‫بععتی‬      ‫دل»‬
             ‫لزونک‬
```


## [2026-09-05T18:06:13.047Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(280,330):\n    p=t[i]\n    for m in re.finditer(r'صفح\\S*\\s*\\D{0,4}([۰-۹0-9]{2,4})', p):\n        print('leaf',i,'est',i+543,'->',m.group(0).replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T18:06:15.024Z] TOOL RESULT

```
leaf 284 est 827 -> صفحة ‪۳۲۸
leaf 289 est 832 -> صفحه ‪۳۸
leaf 299 est 842 -> صفحه ‪۸۳۸
leaf 303 est 846 -> صفحهٌ ‪۸۶۸
leaf 314 est 857 -> صفحهٌ ‪۵۵۸
leaf 315 est 858 -> صفحهٌ ‪6۵۸
leaf 326 est 869 -> صفحه ‪۷۸
```


## [2026-09-05T18:06:24.534Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (299,303,314,315):\n    p=t[i]\n    for m in re.finditer(r'.{60}صفح\\S*\\s*\\D{0,4}[۰-۹0-9]{2,4}.{20}', p, re.S):\n        print('leaf',i,'::',repr(m.group(0)))\n    print('---')\nEOF"
}
```


### [2026-09-05T18:06:26.498Z] TOOL RESULT

```
leaf 299 :: '                                                   \u202bبقبه از صفحه \u202a۸۳۸\u202c\u202c\n \u202bازچرم بوده است '
---
---
leaf 314 :: '                                           \u202b\u202a0\u202c\u202c\n  \u202bبقیه در صفحهٌ \u202a۵۵۸\u202c\u202c\n\n \u202b(برهان فاطع \u202a)'
---
leaf 315 :: '                                                   \u202bبقبه از صفحهٌ \u202a6۵۸\u202c\u202c\n  \u202bبودغا \u202a« 501\u202cا'
---
```


## [2026-09-05T18:06:41.239Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (297,298,299,308):\n    print('='*25,'leaf',i,'=> printed',i+540)\n    print(t[i])\nEOF"
}
```


### [2026-09-05T18:06:43.075Z] TOOL RESULT

```
========================= leaf 297 => printed 837
                                                                                                                   ‫‪ ۴۱۳‬بت‬


                                                              ‫هآمده استِ ؛ وباین معنی باشین قرشت نیز‬
  ‫غدارل ‪ -‬بروژن پ هشن‬
                         ‫‪.‬‬    ‫آب ذلك‬          ‫که در یش‬

                                                                                                                   ‫گفته‌اند ‪.‬‬
                                          ‫باشد‬     ‫وه‬          ‫درس حوان د باواوممدوله بروزن‬
‫ب رکاله ‌ راهی را‬    ‫وزن‬     ‫بر‬     ‫درغا له‬                    ‫سخت جان ‪ .‬شا گردرا کوبند » وشخصیکه پیش‬
‫گوبند که ازمیان کوه‌بگذرد وآنرا بعربی شمب‬                                        ‫‪۱‬‬                  ‫بو اند ‪۱‬‬     ‫‪ 3-۳‬ری‬

 ‫وفرجة ميان دو کوه را نز کفته‌اند ‪۰‬‬              ‫خوانند ‪-‬‬      ‫درس ‪ ۱‬د بورزن عرصه » بمعنی درسته‬
                                                                                           ‫است که بش؛ددن وعفو باشد‪.‬‬
                                    ‫‪۰‬‬   ‫قند‬   ‫درحوالی‪-‬حر‬
                                                               ‫درش ‪ ۰‬بح اول و انی وسکون شین‬
 ‫» هرزه‬      ‫وزن یدمست‬       ‫در عست‪ -‬بر‬                        ‫قرشت ‪ ۰‬نام نوعی ازخبارست» وآن پاريك ودراز‬
                                  ‫وناه‌عقول را کویند ‪۰‬‬         ‫میشود ‪ - ۴‬وبسکون انی پایگاه وطوبلة اسبانرا‬
                                                                                                ‫گونند ‪۶ .‬‬
‫دعرلیکی د بالام وبای ابجد وکاف بر‬
‫دار‬     ‫تن ‪ ۰‬درهرا گونن که بره‬            ‫هر هفت‬     ‫ورن‬       ‫‌ کاءه ازمردم کشف‬                ‫در شت ند‬

 ‫باشد ؛ بمضی دري راگوبند که پیش آن پنجره‬                                                                         ‫طبع باشبد ‪.‬‬
 ‫داشته باشد ومردم از عقب پنجره نمابان باشند؛‬                  ‫در شته = بروزن ومعنی درسته است که‬

‫و معنی اول بهتر است چه غلیکن بمعنی پنجره‬                                         ‫وذشتن اکزناه باشد ‪#.‬‬
                                                                                                    ‫ردن گ‬
                                                                                                        ‫عکفو‬
‫‪ :‬وعم ثالث وفتح‪,‬ای فارسی هم نظر | مده‬                ‫است‬
                                                               ‫درشی مه بفتح اول و انی بر وزن‬
                                                 ‫است ‪. 3‬‬       ‫حبشی » بمعنی درش است که خیار باريك ودراز‬
‫م ثالث با زبادتی‌نحتالی‬      ‫‏‪e‬‬   ‫درغلیکس‬                                                                              ‫باشد ‪.‬‬
‫که در‬      ‫ماسن‌کاف و نون ‪ ۰‬به‌عتی درغاسکن ‪A‬‏‬                          ‫‌زشدن‬
                                                                           ‫لا‬‫جبه‬
                                                                               ‫در عرق شدن هخکنا‬
‫پنجره‌دار باشد؛ وبا بای فارسیتا کن‌هم‌درست است‪.‬‬                           ‫وخجلت کشبدن و شرمنده شدن باشد ‪.‬‬
                                                               ‫درغ ؟ = پروژن برق * بتدیراگویند‬

      ‫معرب‌آن بز «درش»*ابن درید» ‪ .‬رکه ‪:‬درشی‪.‬‬                  ‫‪۴‬‬             ‫‪.‬‬       ‫درسته» درشه‪‎‬‬     ‫ر؟‬       ‫‪١‬‬

   ‫‪(22‬آرودی است که‌بسحونریزد‬                  ‫غام ‪0۲‬‬        ‫‪ ۳‬در‬             ‫» (ھ‪ .‬م‪. ‎).‬‬     ‫ورغ‬    ‫«‬    ‫مصحف‬       ‫‪۴‬‬



                             ‫رك‪ :‬درغلبکین ‪.‬‬           ‫‪۵‬‬            ‫‪.‬‬     ‫‪۸‬‬       ‫‪.‬حدود‬    ‫میئورسکی‬        ‫«حجدود الءالم ‪۷۲‬؛‬




      ‫(رأت» سعی کردن ) ‪.‬هندی باستان ‪۲5۳20-‬‬
                                         ‫(جرأت ‪ .‬جارت‪ .‬کوشش) و اوستا ‪ 0156۳31‬ج‬
  ‫‪۰‬‬     ‫وهو‪.‬شمان از ريشةٌ ابرانی‪ 0 ۵6۳5۵۳-‬حدی مزند ‪ ۶‬هویشمان ‪۲۵۵۹‬‬                                        ‫میداند «اسدق ‪۲‬‬
      ‫افغانی ‪« 605۵۷۲0‬هوبشمان‌اضا» ‪ .‬کیلکی ‪405‬نا‪۲‬نا؛ ناهموار ‪ .‬ناصاف‪ -‬زمخت‪.‬سخت » خشن‪-‬‬
                                                                                             ‫غلظ‪ .‬کشف رك‪ :‬درشتی ‪۰‬‬

  ‫‪ ۵‬دشرتی ‪ -‬حم اول و دوم‪ « .‬از‪:‬درشت ‪ +‬ی (مصدری) ؛ درشت بودن » سختی و ستم‬
      ‫تندی‪(« :‬شاهدان) تا خوب و لطیفند درشتی کنند وچون درشت شوند تلطف‬                                  ‫با جور ‪ -‬ترش‌روبی ‏‬
                                                     ‫کنند و دوستی لمایند ‪« ».‬کلتان ‪. ۱۶۱2‬‬
   ‫مأخون از آلمالی‬           ‫‪ ۵‬درشکه ‪ -‬بطم اول و دوم و کمر چهارم ‪ .‬از روسی ‪۴020۳‬‬
   ‫‪6‬درشکه)؛ گردونۀ چهار چرخه که با اکسشبیده شود و اطافکی برای حمل مسافر‬                ‫(‬
                          ‫دارد که‌مقف آلرا میتوان بلند کرده برافراخت وبا تاکرده خواباند ‪.‬‬

========================= leaf 298 => printed 838
  ‫‪-‬‬                                                                           ‫در غو رگی مویز شدن‬

                                                     ‫که آنجا شراب خوب میشود » شوراب درغمی‬
 ‫فروغ‌وروشنی ‏‪ - ٩‬وچیزی که درخشان ‪,‬اشد ‪۵‬‬
 ‫وفوطه‌ای که درروز جنگ بربالای دستار و خود‬          ‫موسیقی که شنیدن‌آن غم‌والم از دل بیرون کند‬
            ‫‪,‬‬   ‫هل‬   ‫که بت رکی دولغها کون‬                         ‫ت رکیبیآن درالدوه باشد‪¥ .‬‬   ‫وهعنی‬


‫درفشان ‪ = ۴‬بروزن درختان » بمعنی‬                     ‫دزن ‪ -‬کنابه‬
                                                              ‫در غو ر گی مشو ب‬
       ‫لرزان باشد ‪ -‬ویمعنی تابان هم هت ‪. ۸‬‬                ‫‪.‬‬      ‫ب)اشدشند‬
                                                                        ‫از بمراد رسیدن وضایع (‪۱‬‬
‫فش کاو ان ‪ ۹‬س یاواوبالف کشید»ه‬        ‫در‬
                                                     ‫ذر عیش‪ -‬بر وزن دروش »‪ ۰‬بمعنی‬
 ‫» وشرح‬     ‫گر‬
             ‫نا‬‫هاوة‬
                  ‫علم بفدرون‌است ومنوب بک‬            ‫ابوه و بسیار باشد ‪ -‬و نام لوعی از زردآلو هم‬
               ‫آن دراخترکاوبان مذ کور شد ‪.‬‬                                                    ‫‪.‬‬   ‫نے‬


‫در فش کاو بان‪-٩ ۰‬‏ بابای‌حطی بالف‬                    ‫در فش » بکراول وقح انیوسکون‬
‫فا وشین قرشت » افزارست کفش دوزان و امثال | کشیده ‪ .‬همان درفش‌کاوان است که علم‌فربدون‬
                                    ‫باشد ‪.‬‬  ‫آیشان را ‪ ۴‬علمی رانیز گونند که‌در روزجنگه‬

                                                                          ‫شائع‪.‬‬   ‫)‪ ۱‬حك‪:‬‬


  ‫‪ «0-۱‬قال (کری) فاخبرنی عن‌اطب‌الشراب والذه ‪ .‬قال (رمدلخوش آرزو )‪:‬العنبی‪...‬‬
  ‫وخیره‌البلخی والمروروزی والبوشنجی والبتی والجوری والقناوزی و الدرغمی« ثعالبی ‪ .‬غرراخبار‬
 ‫‪ .‬رك ‪ :‬خرو قبادان وربدك وی » ترجمة تکارنده ( مجلهٌ آموزش و برورش سال"‬                  ‫ملوكالفرس‬
                                                                                    ‫‪‎ )٤‬دنب ‪: ۵۷‬‬
            ‫وز فر توبهار شد آراسته زمی‪‎‬‬                       ‫آمد بپار خرم و آورد خرمی‬
            ‫با بانگگ زیروم بود وقحف درغمی‪‎.‬‬              ‫خرم بودهمیشه بدین فصل آدمی‬
  ‫‪K‬‬    ‫یرپچونم ‪‎‬ینأغماد ‪۱۹۷‬‬   ‫‪2‬‬

  ‫‪ ۴‬رامت » بیرق » اوستا‪( 20512۳0 -‬بیزق) » پهلوی‪‎‬‬       ‫‪ = ۴‬دروش («م‪. )-‬‬
  ‫‪ . drafsh‬عیتمرا ‪ ۳810510‬كر ‪ :‬قشسا و نامشبوه ‪ » ۵۳‬برعمنآ شفردزین ‪‎‬حینافم« ‪> ۷۳‬‬
  ‫‪ ۴‬رکه‪ :‬آذرخش‪‎.‬‬                  ‫و درفی » ترکی ع‪ :‬درفس ( بکر اول و فتح دوم ) « تفس * ‪.‬‬
  ‫‪« _ ٦‬بدانکه درین کتاب دولغه مدالاست ‪ .‬امادرمتنشسکی‪‎‬‬                ‫® _ رك ‪ :‬درخشدن‪. ‎‬‬
      ‫وفته که بطا اولی است فقط ‪« ».‬چكصس ج“‬
                                         ‫مجای دال‪ .‬طای حطی وتای‌فرشت هردوآورده گ‬
        ‫‪۱‬‬                                            ‫‪ ۲‬اسم فاعل از« درفشیدن» («‪.‬م‪: ).‬‬
        ‫مفكتاب فروزان شده ز روی زمین‪.‬‬                         ‫بك آفتاب درفشان شده زروی سپهر‬
  ‫دمزی‪ .‬لیشایوری ‪. > ۹۳۵‬‬
  ‫‪ -‬فشان (فشاننده) ‪ ,‬آنکه در‬       ‫‪ - ۸‬درفشان م اول وسکون دوم وفتح سوم » از ‪ :‬در‬
                       ‫(جواهر) را بیفشاند ویخش کند ‪ -‬آنکه درسخن او معانی بلئد وعالی بأشد ‪.‬‬
  ‫آ تانکه از آن (هوم) لوشندند بدلخواه‬      ‫‪« :‬نباید از برای من‬        ‫‪ - ۹‬درستاه‪۱ : ۰۱‬‬
                                                                   ‫م‪8‬ده‬
  ‫خود مانند گاو درش در جنبش‌باشند‪ ».‬در متن اوستابجای گاو درفش ‪ 2۳5/2۳1 ۰‬لاڇ ‪ 6‬ودر‬
 ‫تفسیر پپلوی «کاو درفش » بعنی علمگاو آءده ‪ .‬ابن لغت درست یادآور درفش کاوبانی‌است که‬
      ‫بقیه دصرفسهٌ ‪۹۳۸‬‬
 ‫(برهان فاطع‪)۰۱۱‬‬

========================= leaf 299 => printed 839
                                                                                       ‫رت‬
                           ‫بردن بکسی باشد ‪.‬‬        ‫درفشه = بم اول وثانی وسکون‌فاوفتح‬
‫در فنحك = بفتح اول وئالك وسکون‪:‬‬                         ‫بیغ وشمشیر باشد ‪.‬‬      ‫عتن»ی‬
                                                                                   ‫مرش‬
                                                                                     ‫بن ف‬
                                                                                        ‫شی‬
‫ثانی ولون که رابع باشد وجیم مفتوح بکاف زده»‬        ‫فرشی۔ بکراول وفتح انی وسکون‬
                                                                             ‫‪3‬‬
 ‫گرا ییکه‌درخواب برمردم‌افتد نورآابحربی‌کابوی‬      ‫ت‪,‬رحابتعانی کشیده ‪ ,‬خودرا مشهور ماختن‬
                                                                                       ‫بلث‬
                                                                                         ‫ثا‬
                                     ‫خوالند ‪.‬‬                               ‫وعلم کردن ماشد ‪. ۱‬‬

  ‫واف‬‫در قه = بفتح اول وسکون انی ق‬                  ‫در فشیدان ؟ ‪-‬بروزن‌ومعنید‪.‬خشیدن‬
 ‫مفتوح» بمعنی زره باشد که بعربی درع خوانتد‬        ‫است که تابن ومنورباشد ‪ -‬و بمعنی لرزیدن هم‬
‫است کهبعریی جنه‬        ‫ه‬
                       ‫دظر‬
                         ‫ممبن‬
                            ‫آر ه‬
                               ‫وبمعنی سپ‬                                           ‫‪1‬‬   ‫است‬   ‫اى‬


                                   ‫گنت ‪. ۴‬‬

                                ‫‪ - ٩‬درفشی کردن ب‌عنی مشهور کردن » رسوا کردن‪: ‎‬‬
            ‫دجهران‪‎.‬‬   ‫بکشنتن‬
                            ‫و م‬
                              ‫خفشی‬
                                 ‫در‬                       ‫بگفتارکرسیوز بکدمان‬
  ‫ةمانهاش« خب ‪‎‬ج ‪‎ ۳‬ص‪- * ٩۰۱‬‬
                       ‫‪‎‬ندشخرر ‪.‬‬     ‫=‬   ‫‪ ۴‬زا ‪‎ :‬شقرد ‪ ٣‬ندب ( دنوسپ یردصم )‬
      ‫درفة بمعنی سپر ‪ .‬عربی است جمع ‪ :‬درق » ادراق » دراق ‪ « .‬ناطم‌الاطبا > ‪.‬‬     ‫‪۴‬‬


                                                                             ‫بقبه از صفحه ‪۸۳۸‬‬
 ‫ازچرم بوده است ‪ .‬آغاز داستانی این علم معروف است‪.‬کاوث آهنگرازستم ضحاك بتوه آمد وآن‬
 ‫پوست آکههنگران بران بندند برسرچوبی بلندکرده مردم رپابدشاه پیداد گربشورانید ف‪.‬ربدون‬
                                                ‫آن علم را بفال دك کرفت بزر و کوهربیاراست ‪:‬‬
          ‫همی خواندش کاویالی درفش ‪.‬‬                     ‫فروهشت از زرد وسرخ وبنفش‬
 ‫« فردوسی *‬
 ‫بنا بقول ابوربحان ( آثارالبافیه ص ‪ ) ۲۲۲‬ابن رابت که « درفش‌کابیان » نام داشت‬
 ‫ازیوست خرس بود‪ .‬وبقول دبگرازپوست شیر» و بزرو گوهرآراسته بود ‪ .‬خوارزمی درمفانیح‌الملوم‬
 ‫نوسد ‪ « :‬درفش کایبان یعنی علم‌کابیان ‪ ,‬کیکه بضرحاك شورید تا آفرویدن ضحاك را بکشت ‪.‬‬
 ‫درفش کابی از پوست خرس بود و نیز کویند از پوست شیر بود ‪ .‬پادشاهان فری آنرا فرخنده‬
  ‫آسزپبروزی‬
          ‫دانسته بزر وجواهر گرانبها بباراستند» (مفانیح ص ‪ .)۳۷‬عالبی نوسد ‪« :‬دراش‌کاوه پ‬
 ‫بدست عربی از فببلة‬     ‫سکیه‬
                           ‫درجن‬
                              ‫ااد‬
                                ‫فدت‬
                                  ‫فریدون بزر و کوهر آراسته شده علم مقدی ابران بو‬
 ‫جح افتاد ‪ .‬سمدبر‪ .‬وقاص آلرا جزو ذخایر وجواهریزد گرد ترد عمرین خطاب فرستاد ‪ .‬عمرآمر‬
 ‫کرد کهآ را ازچوبه گبررفتند وخود درفش را باره باره ومیان‌سلمانان قسمت کردند‪( ».‬غرراخبار‬
  ‫ملولالفرس ‪.‬عالبی‪ .‬باهتمام زتثبرکه ص ‪ ۲۳‬و‪ )۸۳-۹۳‬بلعمی نوسد ‪ « :‬بمد ازوی (فآریدون)‬
 ‫(رفش را ) میداشتند هریکی پیرابه جوواهر چندی بر آن‬
                                                 ‫بادشاه بپادشاه میآمد و عزبزش د‬
 ‫می‌بستند تا وقت بزدگردشاه ‪ .‬چون مسلمانان خزينةٌ او غارت کردند؛ ارواییش امیرالموّمنین عس‬
 ‫خطاب رضی‌الله عنه آوردند وامیرالممتن بفرمودتاآن گوهرها برداشتند آون‌پوست راسوختند‪».‬‬
  ‫قیمت جواهر درفش به ‪ ۶۰۰۰۰۳‬لیر انگلیسی تخه‌ین شده است ‪ ( .‬پور داود ب‪.‬سنا اص ‪۵۷۱‬‬
                                 ‫متن وحاشیه ) ورك ‪ :‬اخترکاوان » اخترکاوبان » ورك ‪ :‬کاوه ‪۰‬‬
                                    ‫‪ #‬ورغمی ‪ -‬بفتح ارل وسوم » منسوب بدرغم (ه‪.‬م‪. ).‬‬

========================= leaf 308 => printed 848
       ‫با‪1‬ه‬                                                                                       ‫دریاب‬
‫دبرای بصره «کنابه ازیبالًبز رکه‬                      ‫دیراب ه بروزن غرقاب» درباراگوبند‬
                          ‫پرشراب باشد ‪.‬‬              ‫کبهحبعررخبیواند‪٩‬‏ ‪ -‬وامرازدریافتن وفهمیدن‬
 ‫ذبرای سائله ‪ -‬کنابه از دربانی‬
 ‫است که مروارید داشته باشد ‪ -‬و شراب را یز‬            ‫دریا پار ‪ - ۴‬بابای ابجد (‪ )۱‬بروزن‬
                                          ‫کن‬          ‫پهنادار » دربای برزک رگوایند ‪ -‬و نام شهری‬
 ‫دریای لعل کنابهازیباله وسراحی۔‬                     ‫همهت ‪ -‬وولاسی را نز گوند که مر کناردر با‬
                            ‫وخم پرازذراب باشد ‪.‬‬                                                ‫‪۶.‬‬
                                                                                                ‫باشد ؟ ‪#‬‬
  ‫دریای قبره کنابه از شب تاريك ‪-‬‬                      ‫در باك ‪ = °‬بروزن ومعتی ترباك است‬
                           ‫ودوات پسریاهی باشد ‪.‬‬      ‫که افیون باشد ‪ -‬ودقع کنند؛ زهررا نیز گویند‬
‫در اشم = کنابه از مروارید بزرکه‬                                                ‫ومعربآن تراق است »‪:‬‬
 ‫است که بکدانة تاها در صدف باشد ‪ -‬کونانه‬
 ‫از حضرت رسالت یناه صلوات اه عليه وآله یز‬             ‫دریا «ککشنابه ازشراب‌خواری که‬
                                                                                     ‫‪۰‬‬    ‫شود ‪۹‬‬   ‫دير من‬
                                          ‫‪۰‬‬   ‫هست‬

  ‫در بيخ افتادن ک«نابه ازانت‬                         ‫ددمعتي دربا کش ات که‬       ‫۔‬   ‫در با نوش‬


   ‫ککهسی درمقام خرابی و استیصال کسی شود ‪.‬‬              ‫رود مت‬      ‫اعت که‬      ‫کنابه از شراب خواری‬

                                                                                                   ‫نشود ‪.‬‬
 ‫در بان د ببضرووزلن‌بریدن» بمعنی‬
 ‫درو دن باشد که بریدن غله است‪ - ۷‬وبفتح‌اول‬            ‫دربای اخضر ‪ -‬کنابه از آسمان‬
                        ‫بمعنی باره کردن باشد ‪. ۸‬‬                        ‫‪.‬‬   ‫هم ھت‬   ‫ونام دریای‬     ‫‪۹‬‬   ‫اس‬



                                                                            ‫(‪ )۱‬چك ‪ :‬یابا ‪.‬‬

   ‫‪.‬‬    ‫بار (یوند مان‬      ‫از‪ :‬درا‬    ‫‪۴‬‬         ‫‪ _ ۳‬رلك‪ :‬دریافتن ‪.‬‬            ‫‪ - ۱‬رك‪ :‬دربا ‪.‬‬

       ‫‪ - ۴‬جاپ جنوبی لارستان کورمان را ‪ ۶‬دربابار» گوبند ‪.‬کهره‪:‬‬                            ‫رك‪ :‬بار‪. ) ۷ :‬‬

   ‫‪Quatremère. Not. et Extr., XIV. 281, ۰‬‬
                                                                            ‫رك‪ :‬ترباك ‪.‬‬      ‫‪۵‬‬


               ‫که چل صبح در مغ سرا میگریزم‬              ‫‏‪ ٩‬مرا ز اربمین منان‌چون پرسی‬
              ‫ز جور لهنکگ عنا میگربزم ‪.‬‬                ‫باصاف دربا کشانند کا نجا‬
   ‫«خاقانی شروانی ‪. ۸۷۲‬‬
   ‫‪ ۰‬ازرشة اوستابی‬      ‫از‪ :‬در(ه‪.‬م‪٣ ).‬‏ بدن (پسونده‌صدری)‬   ‫‪-‬‬               ‫‪ - ¥‬رك‪ :‬درودن ‪.‬‬
       ‫‏‪( 816۳64 -. dar‬شکافتن) ‪ ۰‬پهلوی ‪, 0211120‬هندی باستانی‪« 1157۵1 . ۲۵1 -‬اسعق‪۲۹‬ه»‬
                                                     ‫( دربدن ) ‪.‬‬     ‫در اوراق مانوی پهلوی ‪0۷۲۷‬‬
              ‫‪,gninneH‬‬       ‫‘‪A tsil fo elddiM‬‬         ‫م ‪naisreP ...‬‏‬       ‫‏‪509 , 621 ,1, p.82.‬‬
       ‫کردی ‪. 7271760‬افغانى ‪, 12721‬بلوچی ‪ 8۵۳1‬و‪ 82۳۳11‬و ‪ 08271‬و ‪ihdg‬‏‪.an‬سربكلى‏‬
   ‫‪« 0700721-2‬اسشق ایضا» ورك‪ :‬هوبتمان ‪۲٩۵‬‏ در فارسی بمعنی لازم‌هم آمده بعنی پاره‬
   ‫شدن‪( « :‬محمود) کفت اورا (ابوربحان بیرونی‌را) بمبان سرای فرو اندازند ‪ ...‬بوریحان‌یر آن‌دام‬
           ‫آمد ودام درید واآهسته بزمن فرودا مد چنانکه بروی افکار نشب ‪« ».‬چهارمقاله ص ‪۷۵٩‬‏ ‪.‬‬
       ‫بقبه در صفحه ‪٩۸۸‬‏‬
```


## [2026-09-05T18:06:59.353Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[305][2000:])\nEOF"
}
```


### [2026-09-05T18:07:00.955Z] TOOL RESULT

```
وزن عروسك م‬                        ‫وك‬
                                                                                                            ‫نرل‬
                                                                                                              ‫د‬
 ‫دارد‪ -‬ونام‌ولاتی‌هم‌هت ازملك بدخشان که مردم‬                   ‫درون باشد » و بیخی است دوایی شبیه بعقرب‬
‫آنجا یخوش صورتی مشپورند و انارخوب درا لجا‬                       ‫که آنرا درونج عقربی گویند » و درونج معرب‬
                                                                                                    ‫زک‬
‫مدشود ‪ .-‬و ضاحمول و تشدید الی پوستی چند‬
 ‫باذد باريك که بر هم بدوزند با برهم ببافند‬                     ‫درو نه = بفتح اول وبا واو مجهرل بر‬
‫کوناهکارانرا بدان تنبه سازند وکاه باشد که‬                      ‫وزن نموله » بمعنی درونك است‪ .‬وآن کیاهی‬
 ‫دهل ولقاره رابدان نوازند ویمعتی‌دلیل وبرهان‬                  ‫باشد شبیه بعقرب ‪ - ۴‬وبمعنی درون همهت که‬
   ‫)‪ (4‬چك‪ :‬تخففه‪.‬‬            ‫)س( چش‪ :‬فوی‌وفز ح ‪.‬‬             ‫(‪)۲‬چك‪ :‬ژند وباژند‪.‬‬            ‫)‪ (۱‬چكث‪ :‬دوم‪.‬‬

    ‫»هرند) *مماس ‪۷۲ ۲‬‬        ‫(کافر ‪ ۰‬می دمن‬       ‫بپلوی ار‬                   ‫‪— ¥‬‬        ‫‪.‬مصحف؟* درو ‪1۵‬؟‪.‬‬            ‫‪ ۱‬ظ‬

    ‫دروغ‌پرست " |زاوستا_ ‪ « 602۷۲1 - ›4 812۷89‬بارتولمه ‪ » 4۷۷۲‬پازند وپارسی ‪04۳2۷721‬‬
   ‫رك‪ :‬درو نك درولج ‪۰‬‬        ‫‪> ۴‬‬        ‫‪ -‌ ۳‬رك‪ :‬درو له‪.‬د؛ ولج ‪۰‬‬              ‫لیب رکد‪ »+۰‬ورك ‪:‬اسشق ص‪۳ ۴۲۲ ۰۲‬‬

   ‫‪anurd‬‏ ( کمان ‪ ۰.‬قوی) » تلوچی‬              ‫ت‬    ‫ماک‬           ‫‪۹‬‬                      ‫رك‪ :‬درون ‪.‬‬              ‫‪6‬‬
                                     ‫‏‪ dîn uk , 0‬سوف )حرق » اغدوب ع ‪ 4۳00‬قشسا« ‪. 00۸‬‬
   ‫«ومان وی( کیومرث) بدان‌روز کار چوبین بود بی‌استخوان » بکپاره چون درون‬
                                                                       ‫ک‬                                        ‫‪۷‬‬
                                   ‫درووزه (ھ م‪ (.‬۾ دریوز *‬           ‫=‬   ‫‪۸‬‬              ‫حلاحجان» «نوروزنامه ‪۹۳٩‬‏ ‪.‬‬
    ‫وخی ‪۲621‬‬       ‫(بطلموی ‪(1‬‬            ‫_ اوستا ‪_ûnerad‬‏ (دره‪ ,‬گردنه) ‪ ۳‬سونالی ‪anrûD‬‏‬

   ‫فارسی بمعنّی‬   ‫»ودر‬       ‫ع ‪ered‬‏‬    ‫هو ‪.‬شمان ایض » در ‪9۳‬‬                 ‫و رك‬      ‫‏‪ 9 dher‬أسشق ‪“°‬‬               ‫سریکلی‬

   ‫‪ ۰‬یر لی‬   ‫‪earread‬‏‬   ‫؛ گلکی‬      ‫ارل ودوم)‬     ‫(بكر‬       ‫اسلام ‪ :‬دره‬     ‫الممارف‬   ‫دائرة‬       ‫رك‪:‬‬   ‫وادی عر هی آبد ‪۰‬‬


    ‫سنگری ولاسگردی ‪» 64۲۲310‬سرخه‌بی‬                         ‫‪.-‬دانی ‪۲۲3‬‬             ‫ونطذزی ‪ ۱ .۵« 8۳۳20‬ص‪54‬‬
                                                        ‫‪.‬‬     ‫‪ .‬نهمرزادی ‪« ۲۲00‬ك‪ .‬ص‪۱۸۱‬‬                                    ‫‪6‬‬
    ‫‪4۸‬‬   ‫نقه درصفحه؟‬     ‫‪۳‬‬     ‫‪ ۰‬ددن‬     ‫درودن‬   ‫رك‪:‬‬   ‫وياجم‪.‬‬    ‫اول وفتح دوم‬       ‫نکر‬        ‫=‬   ‫ادن‬    ‫درو‬   ‫‪¥‬‬
```


## [2026-09-05T18:07:17.651Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT dar- / darəna / drafša / niš.dar\"; grep -n \"daren\\|darən\\|drafša\\|drafsa\\|niš\\.dar\\|nis\\.dar\\|niśdar\" BRT.txt | head -40"
}
```


### [2026-09-05T18:07:17.705Z] TOOL RESULT

```
=== BRT dar- / darəna / drafša / niš.dar
```


## [2026-09-05T18:07:20.509Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && wc -l BRT.txt && grep -n -i \"drafsa\\|drafša\\|drafs\" BRT.txt | head -20; echo \"--- darena\"; grep -n -i \"darena\\|darana\\|dar9na\\|dardna\" BRT.txt | head -20"
}
```


### [2026-09-05T18:07:20.593Z] TOOL RESULT

```
30724 BRT.txt
7675:•  j.  «rsSwö.drafSa-  Adj.  (fem.  'sä-)  'mit hoch  aufgerichtetem  Banner':  Aa»tayäsca,. °/ajni  Yt.  /,  1 1 ;  —  bäxölm  srJram  "sam V.J.6.
10145:dem,  was  das  Rind  liefert;  i) 'Fell,  Haut':  ahurai  a  mS  urva  'Suscit  azya  Y.2g. mä  .  ,  yaia  *'aof  drafsö  (sd.)  .  .  Y.  /o.  1  5  '3>.  a)  neben  'gaya-  (sd.):  nimS  °Sus 14.  2)Tleisch':  pars xh'isca{sd.)  5zBi-\  mmö  gayehe  Y.68.  22;  Vr.  z/.  a;  —  fra tisca'jus  matY.13.%9,;  —  nöii  payS  fsula  .vasayS  ..  yqmca  asnö  ..  spu  ..  zsmS (sd.)  nSii  'Jul  .  .  paiti.baire  V.  7.  77;  —  I .  .  un-arayd  .  .  -Jus  .  .  gayeke  Vl  13. kat  na  .  .  -Jus'  ataifya  (sd.)    aslryeiti  N. '  86.  a)    GS.    mit  tasan-  m.  (sd.,   auch
10454:tisit  hainyS  ra%ff  nsit  uzgprjpiS  drafsö Yt.  Ä56;  —  uzg?r>plgm  vä  i-arisjm  va Vd.  5.  z)  '(die   Hände)   ausstrecken,
16091:•  j.  p9r«9*u.drafSa-  Adj,  (fem.  'sä-)  'der ein  breites  Banner  führt':  haOtayaiHa  .  . 'sayä  Yt7.  II.
16092:Pü.!  pur  drafs,  erl.:  tu  dtaß  vas  därind.
23503:•  j.väTOTnaadv.-artige  Verbindung;  i)'nach Wunsch,  ex  voluntate':  uta  he  Sstam xraiBm  ava.baraiti  V  tbayantäi  "und dem  verschafft  sie  nach  (seinem)  Wunsch . .  Weisheit,  der  sie  anruft"  Yt.  ij.  3 ; 5. 130.  2)  'nach  Belieben,  beliebig, willkürlich';  ma  mi  yaha  *gaeS  drafsS asitS  *v°  *Ä(«(Sp.  581  f.)  Y.io.  14.
--- darena
12873:•  j.  dar«na-,  darana-  n.  i)  'Befestigung'
13482:•  j.  däuru.-upa.darana-  d.  'aus  Holz (-Stangen  od.  dgl.)  aufgerichtete  Hütte">: yat  'tu  vä  *tumats.aiwi.varane  vä  spS  nS vä  iri>yai  V.  cV.  1.
14949:•  j.  paiti.darana-  n.  'Ort  des  Verweilens, Aufenthaltsort':  /m  imqm  damqm  .  .  fra- pinaoiti  satim  * paitiltananqm  (sd.)  haxaa- nm  °ranqm  (GP.)  V._j.  31.
```


## [2026-09-05T18:07:26.449Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '12860,12900p' BRT.txt; echo \"#### search simplex drafsa entry\"; grep -n \"Banner\\|Fahne\" BRT.txt | head -30"
}
```


### [2026-09-05T18:07:26.538Z] TOOL RESULT

```
mit  Hl  1)  "niedei^,  festhalten':  yö  nö aisqm  aahunqm  kälqm  tiidilrS  anhat Vytjo  (?).  3)  'sich  verborgen  hallen':
iräsat  {sd.)  yimö  .  .  dfui.maaahyli'a  (sd.) Ab  st>rit3  nidäral  upairi  zam  ".  .  musste er  sich  verborgen  halten  .  ."  Vt.  ifi.  34-
mit  vT  i)  'diribere,  verteilen':  iataarj p>r)nA  (sd.)  viöilrayöii  avi  pa^qm  Yl 14.44.  a)  'zuteilen,  verleihen':  vfösra- yeiti  upastqm  *p^r>nJ  (sd.)  nurrfanqm  Yt 14.  36-  a)  'durch  Auseinanderhalten stützen,  festhalten;  erhalten':  mi^nm  .. yj  stunä  vf',Hrayeiti  . .  nmrinuAe  Yt  10.  7%;
693
I  —  fravafwfS  .  .  yä  asmanfm  vnäraym ya  äptm  vJaaraym  yä  zqm  v^äraym  yx gqm  viiäraym  yä  barf%riyva  puisri  vtbä- raym  Y.  23.1;  —  ärfhqm  raya  . .  v^Sragm .  .  aom  asmamm  Yt  13. 1;  4,  9,  11;  — yat  sptntd  matnyui  v^arayai  asman?m  Yt. 13.  aS;  ag.  Vgl.  noch  bes.  "i-fiÄ'äJw  Yt 13.  aS,  3)  Med.  'festhalten  an  -'  (AbL): uxihe  (sd.)  xra%we  vidrvanahe^^^  asät V.  4. 45.  4)  'einstemmen,  feststeinmen': nSii  päla  vüarayäti  "die  Füsse  kann  er nicht  einstemmen"  YtJO.48.  5)  'hin- wegbringen über  . ,  {tarB  mit  Akk.)  zu  — ' (Lok,):  Aa  asäunqm  urvat0  tarB  ctnvatB P>r>tUm  vfaärayäti'*^  Aaao{sd.) yazalanqm V, /p.  30;  —  yahmat  haca  puhrS  Aaom urvatifm  ärtvaiptr^tam  *vl%ärayat  Vd2; —  nSit  tarB  änvat.ptnlBm  "viiärayfntjm aam  yB  aAurö  Nik.2.  6)    '(mit    den
Sinnen)  auffassen,  empünden' : , .  «ar/  alaonD urva  urvaräAu(sd.)ca  paiti  *baatisi^a  vi- dilär?mns  salayeiti  H.  2.  7;  a5.
mit  Aam  —  ?  — :  nBit  Aayi^m  Aandaratle P.  15-
Die  Bedeutui^  'halleD'  eignet  insbesondete dem  Praes.  däraya:  —  ai.  dkfIhSh,  dutAaral, dhäriyati,  dhiryitf,  dadhära,  dadhränäi,  di- dhära;  dkpih;    np.   därad;   s.  roch   No,  Z-4.
—  Pü.:  däslan;  s.  noch  No.  S,  6,  8-It,  13, 17,  18.  —  ■>  Das  ä  der  Stammnlbe  kaminl jedenfalls  vom  Pries.  30.— »Vgl.  aL  didÜrtä-S.
—  3)  VgU  ai.  dharüna-  Adj.  —  *)  S.  No.  16. Die  einzige  awe$t  Form  der  Art.  Nach  iL dhäri-tä^  in  dhäräy-ati  wäre  ar.  *dkäri-iiliu aX%  Pissivpraeiens  daia  lu  erwaiten;  es steht  nichts  im  Weg,  das  y  von  jAw.  diryiilt für  iy  la  nehmen.  Vgl.  übrigens  laf-  No.  I, aber  auch  ZDMG.  Ja  690.  —  i)  Tä.:  dartär, Sü.:  ttfiaKsah.  —  «)  Hds.  dramm  mit  An- glei chung  des  Ausgangs  an  die  Nachbir- worte.  Pü.  las»!  da* Wort  aus.— 7)  Sol  Das spricht  durchaus  gegen  Fovs  adärayJ',  KZ. J/.  560,  —  *)  Pü.;  därik,  er].:  apc  nt  dandrl% S.  No.  9  nnd  dqidra-  No,  1,-9)  Pü.i  därem, er!.:  aptaidandem;  a.  N0.8.  —  w)?;!.!  därend, erl.:  kus  afar  äff  citend.  —  ">  S  29^-  6  h- l'ü.:  mk/iilan;  s.  No.  13.  —  ")  Wort].:  non Sicram  curat  sibi  es^e  ärmatim.  —  '1)  Pü.:  pa «ikSUiH;  s.  Xo.  II.  —  M)  FOT  KZ,  ^.  560 will  adäravam  wegen  Eü.  —  'J)  El  scheint etwas  ausgefallen  in  sein.  Vgl.  Gdn.  KZ. lg.  544,  der  'ein  jedes'  ergänzt;  iihnlich  Cu>. Toten  Verehrung  53.  Anders  GcR.  OK.  389. -— >»)  So  M3;  vgl.  No,  4-  —  '"  1^.:  </""'{?)■
—  iS)  Pü.:  viarend.
p.  daray' :  lies  dray',  i.  unter  sray,
•  j,  "daräj^  ä  AüvS*  FiV/.S.  i.
•  j.  dar«na-,  darana-  n.  i)  'Befestigung'
dby  Google
693  darga-  -
(nur    Komp.).  a)    'Aufenthall?    (nur
Komp.).  a)  'Aufenthaltsort,  Wohnsitz, Schlupfwinkel'":  gaus  .  .  ya  •rwuÄK" mi^röjintjqm  ma^änam  .  . /raxarsta  (sd.) "das  Rind  . .,  das  zu  den  Schlupfwinkeln der  .  -  fortgezerrt  wird"  Yt  lo.  38.
KompE.  —  Zum  V.  3dar-.  —  ai,  dhararia-  a.
'Hallen'.  —  ')  Anders  b«i  HokN  NpEk  IH.
—  ')  S  411-  3  d. •  p.  darga-,  g.  daraga-,  j.  dar«}-a-  Adj. (fem.  °7J-)  'lang';  i)  räumlich:  Ufa  tarn car^am  yqm  'yqm  YtJp.  77;  5.50;  — mi^rtm  . .  yeAha  'yäat  bäeava  .  .  Yt.  10. 104.  z)  zeitlich:  M<?i«(sd.)  tat  äs  nsit 'y?m  Yt.5. 65;  —  "iimal  aipi  zrvätum Y.62.3,\tig.a6;  13.53;  —  °f^^  ^yo (sd.)  t^mattks  Y.31. 20;  —  'yayäsca  paiti danyjjltdis  YL  /y.  1 3  j ;  Y.68.11;  —  tsm (nämL  kämtm)  msi  data  'gahys  *yaos{^^^ vairyS  stSis  Y.  43.  13;  —  hyatcä  -gSm *Jr3gvö.d»dyS  rasö  {sd.)  Y.jo.ii; — ptn- fum/a  (sd.)  barjsma  starane  °y?mca  yasram ..yaaJnS'Vt.iO.iiSi—ya^a  Sicä  *aiivi- iayama  'ya  amiiayana  . .  hr^yrnya^^aSum (sd.)  Yt  70.  7  7 ;  —  °gäi  Tsyai  bfzvait!  hax- maim  (sd.)  Y.  40.  3;  —  'yai  hax^räi  Vt 10.  T),  17.6;  — fravaiayS . .  hulhaxmanS . .  'yaa'fyj  Aax^oralifyff  Vt  13.  30;  —  'y^m Aaxma  V.  60.  j;  —  dättm  tS tanuye  :^ar»nB ' urvnaläi  •y?m  havanfum  (sd.)  Yt77.  22; F.^b;  —  urunaica  'ye  havanhe  A.  i.ii; —  'yäi  AaosravaAAsi  .  .  -yai  AavafiAäi Vjtjs;  —  a  'yät  ^ä.bairyilt  (sd.)  Y. öo.  6;  —  'yqfi  upayanayä  (Stverz.)  Y, /.  13  usw.;  —  'ya  (APn.)  data  .  .  sara- >uäraAe  T.  ^6  {?);  —  iaia  tl  'yim  ävSya (sd.)  aakal  H.2. 34;  16.  a)  Adj.  an Stelle  unsres  Adv.'':  :^afsa  'yd  tna^äka "schlaf  lang,  o  Mensch"  V.  rÄ  16;  — earäiti  .  .  yä  'ya  apu%ra  aHti  V.  3.  34; 34.  b)  ASn.  als  Adv.:  H  utä,  'gam  jlvä
(sd.)  Bh.  .^  10,  16;  —  'ytm  fva  uHa  Jva A.  /.  I  2 ;  —  rapHicä  ts  nS  'gimcä  ultäcä Y.  4i-  4 ;  —  yO'  /fl«»  aAmai  harne  gätvS 'Jim  histinta  Yty.  57;  —  yS  kainJnS Sahaire  (sd.)  'ysm  ayrvS  Y.  o.  23;  Vt ^7-  59";  —  ^'^i  ■  ■  ""f^**^  ■  ■  azarisS  .  , 'y^m  yat  yave  vispsi  F._^h.
KompA-  ~  ai.  dSrgkä-  Adj. ;  mp.J),  ooss.  iiiiry ; np.  -vgl.  der<).  —  Vgl.  dräjäk:  —  Pü.:  dtr, (in  V.  63.  3):  dra$tg%\  (lu  F.  I.  St.  imd  als Bciw.  von  u/H^anä-):  dai~j.  —  0  Vgl  DbB. VglS.  7.  459.  —  '>  Wo  'i>m  in  Erinnening an  Y.  9.  33   fOr   ein   andres  Wort  eingesetzt
dar9go.}yätay-
694
EU  lein  scheint.  —  3)  SWienAW.  67.  844-  13  = dar^  dirät  bäiad.  —  4)  Wohl  aus  'dargia-, GIrPh.7.  J73;nnrichtie/b.34.  —  i)  läi  i an i drang  iamän.  Mp.  drang,  np.  lAriiii^  entspricht dem  lat.  impii.
•  p.  dargatn,  g.  daragnm,  j.  daraj-sm Adv.:  s.  darga-.
•  j.  danj'a.arätaya-'^  Adj.  'mit  langem (liiDzen)schaft':  arstayasHi  .  .  'taya  (NP.) Yt  10.  39;  —  mihnm  . .  tHüarstTm  'talrn Yt/0.  102;  f7. 12.
■  g.  dar»gäyav-  Adj,  'langdauemd':  'yu .  .  rafms  Y.  28.  6;   —    %wakmt  rafmakl
'yau  Y.  41-  4-
Komp. :  darifa--\-äyav-.  —  >i.  dirghäyav-  Adj. 'langlebig'.  —  PS.  (dRn.):  dfr  yänih,  dtr  rtuä- nlh.
•  j.  darvj'ain.Jitay-  f.  'langes  Leben': Sfrinami  tava  nara  daäAupaiti  vohu.}xH us.jTti  'jUi  (soll  heissen)  "ich  segne  dich, o  . .,  mit  gutem  Leben,  mit  hohem  Leben, langem  Leben"  Az,  7;  Vyt/.
Vgl.  darifd.jility:  —  IMi. ;  der  Ih-iinli,
•  j.  dar9/Ö.angu§ta-  Adj.  (fem.  'tä-)  'mit langen  Fingern,  mit  langen  schmalen Händen"':  kainim  Ha  (NPf.)  Yt/7.11.
')  Ein  Schönheitsieichen;  vgl.  Artaxerxts  L Beiwort  Longimaiios,     S.  in  dar>-fö,bäzav-.
•  j,  daraj'ö.upa'stay-  f.  'lang  dauernder Unterstand':  iM%»i  nmana  .  .  hUtmte  a^.- paourvh  'stse  "ihre  Häuser  stehen  da  . ., die  weitaus  ersten,  zu  langdauemdem  Unter- stand" Yt/7.8.
Zum  V.  slä:  —  Vgl  ufaslä-  mit  S  soj,
•  j.  darsj'ö.gava-  Adj,  (fem.  °vä-)  'lang- händig",  von  Bafyasta  (sd.):  haiyasta  'va FrW./o.42,  Yt  Jo!97,  V./i'.i6,  /;. 9.
Pö.:  dir  gau,  drang  gav;  erl.  (in  V.  ii):  fa hat  kos  I  ap?  rasfl,  (besser  FtW.):  hatvisp a^  i  asfemand  fKt  /;<tv  apar  isältl.  Vgl.  übrigen* Haug  SBajrtAW.  1868.  a.  30.
•  j,  darUT-ö.x^a^Ta-  n.  'lange  Herrschaft': 'ärjM  xsa'israke  A  /.  8.
Pa.:  der  j^alSiik.
#### search simplex drafsa entry
7675:•  j.  «rsSwö.drafSa-  Adj.  (fem.  'sä-)  'mit hoch  aufgerichtetem  Banner':  Aa»tayäsca,. °/ajni  Yt.  /,  1 1 ;  —  bäxölm  srJram  "sam V.J.6.
8628:•  j.  uz'gai^ptö.draßa-  Adj.  (fem.  °jvi-) 'der  das  Banner  hochhebt,  entfaltet"*: hainayasla  *°sayä''>  Yt7. 11;  —  frava- i'ayS  ..  'sä  Yt.JJ.37.
11233:schwankend  wie  das  Banner  im  Wind;  $  2/7 No.  1.
13958:aLrfAwyai(DhP.'i™/aB';vel.rfAz.o/ä-ni.*Fahne';' desZiels;  inia  aglam   aila  druxl  yä  nasus Bthl.  GlrPh.  /.  159.  —  Npü.:  (^d«  rS)  ml.  upadvasaitil  . .  paitisa  hl  . .  antarät  nai-
14061:•  3.  draföa-  m.  'Fahne,  Banner':  mä  . . ya%a  *gaes°i3'^..*vär^ma*caire(sd.)"..v/ie das  Stierbanner •> .."  Y.fo.  14.  a)  sonst von  den  Feldzeichen  der  Feinde  Irans *AainslyS  ya  us  xrünm  -htn  girminqn  Y. 57.25;  —  haiiiayas^a  .  .  xrQr?m  '/»m iarvntayä  Yt  J.  1 1 ;  —  nsii  ihra  airyi daiAhävö  frqi  (sd.)  hySi  hai»ia  .  .  nsii AasnyS  rdhs  nöit  usgprtptö  "so  Yt.  Ä  56; —  kaca  'sayS  (als  Fem.!)  pin\u.usg>r»p- tayä  Yt.4.3.
14062:KompE.;  Ableit.  —  ai.  drapsi-  m.  'Banner' ä), np.  dirafi;  lEt.  vgl.  Wn.  AiGr.  /.  242,  WOiu noch  mp.  draf^nd  (2,^.;  5.  Ji-a*.  mitNo.  5). — Pü.;  dra/s^\  Npü.:  ««i;* 'Waffe',  Sü.:  lailram 'Waffe';  s.  noch  No.  1.  —  ')  Pü.:  gäv  draß, SU. :  f;ffaJäiiyä.   Cremeint  isl  das  Reichsbanner
14064:der  iranischen  Könige,  du  nach  der  Sage vom  Schmied  JCava  geschaffen  wurde,  indem er  »ein  Ledenchnrzfell  anf  eine  Stange  steckte; danach  bedeutete  g'  dr"  eig.  'Rindsleder- banner'; eher  möchte  das  Banner  das  Bild eines  Stiers  oder  Siierkopfs  enihallen  haben. Vgl.  noch  Jtisn  NB.  160.  —  •)  Gdh.  VSi.^. 57  bestreitet  diese  Bedentimg  des  ai.  Wortes.
14065:—  31  D.  i.  'Banner',  wie  das  «rm.  LW,  äraui beweist;  s.  Hbu.  AGr.  /.  146.
16091:•  j.  p9r«9*u.drafSa-  Adj,  (fem.  'sä-)  'der ein  breites  Banner  führt':  haOtayaiHa  .  . 'sayä  Yt7.  II.
```


## [2026-09-05T18:07:43.523Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"spalten\\|zerreissen\\|zerreißen\" BRT.txt | sed -n '1,40p'"
}
```


### [2026-09-05T18:07:43.582Z] TOOL RESULT

```
5093:•  j.  ava  paröit  *d«rflna_m''  Inf.  'entzwei zu  spalten,  entzwei  zu  sprengen':  ava  mS azii  . . parsii  pairt^nam  arthvqm  ava.d°'' saäayelti  (sd.)  V.  18. 19^'.
5761:spalten,  zerstört,  versehrt':  '/a  , .  gäus buyai  (sd.)  *Unt  altm  'bm  tiars  . .  aap US  ahäiril Jkaisd  Y.60.3.
12838:•  j.  'dar-  V.  'spalten'.  Praes.  7  dar^ dar-,  1 1  dfrmä-^^,  30  (Iter.)  däraya-,  — PPfP.  dinta-',  Inf.  *'d3rmqm.  [Vgl  noch d^TTTiinti^
12839:'spalten,  au&palten,  durch  Spalten  mit einer  Öffnung  versehen':  aat  t!  . .  fm.- yuxta  *Aqm.ivamca  (sd)  .  .  d)nta  .  .  aka YL  10. 1 35,
15057:Zam  V.  f*^*-') ;  /'  nach  s  5J  H.  I.  -  PB-  = ,  zulegt,  ist  er  r.,  wenn  er  die  zugelegten  zuerst atac  nastnisniA  rai.    —    >)  Gegen  Hbh.s  Zu-  ,         ° '     .         '       „   . ,         ,.,"      * .  ,  .. sammenstellung     mit    np.    «W/«^   'spalten',   spreitet,  ist  er  «r.     N./07(?).  A)  Name
15610:•  j.  pairi^sm  Adv.  'um  und  um,  ganz und  gar':  pairika  yä  duiyairya  vispahe atfA3uI  astvats  parsii  p"  ar?hvqm  ava.- Msflyai  (sd.)  "die  F.  des  Misswachses würde  die  Lebenskraft  der  ganzen  körper- lichen Welt  gani  und  gar  entzwei  spalten" ■ytÄ54;    —    ava    ml  Stil  .  .  paröit  p'
25776:•  j.  saed-  V.  'spalten'.  Praes.  27  s&,ya-; Perf.  I  his&-.  —  PPfP.  'sista-.
25777:'spalten':  ''s^yat  F.  12. mit  ava  und  parStt  'entzwei  spalten, zerspalten,  zerstören':  pairikaya  duiyüirya vupahe  a^hsu^  astvatd  paroit  pairi^nmt (sd.)  avhvam  ava.hisüyüt  Yt.  tV.  54'*. ai.  chidyalf,  ekhidt ;  mp.  apasihät  (s.  zu  tah-')  *), viiislai,  np.  gmiilan,  sbaL  titu/ag,  sisla.  — Vgl.  zEt.  Hbm.  ZDMG.  38.  425.  Bthi.  Stnd. 3.  4,  Bgm.  IF.  6.  92.  —  Pü.  (tu  F.):  *via- heia.  -~  ")  Vgl.  V.  /(f.  19.  —  a)  S.  ferner Pü.  lu  ajyamna-,  atisla-  (,  wo  avismiin  zu lesen),  jayäi,  'Jyä-,  frajyätay-,  sä-  (No.  3), j^Wa-,jKii&ä(;MK.>G]osi.23,  Sg.-Gloss.233b. —  J)  Geschr.  n  dd  at  statt  n  dd  adt ;  Mx.  6g.  36 hat  die  Bombay  er  Ausgabe  dddadi,  aber  die Kieler  zeigt  dd  dat.
29969:•  j.  ^ham.ivä-  f.  Name  eines  Teils  vom  Ge- schirr des  mit  Pferden  bespannten  Wagens, vli  'Deichsel':  äal  ti  (näml.  aurvants)  vXspa /rü.yuxta  'vqmca  simqmca  simöihrqmca dirita  huhr^la  ^upairi.späta  aka  bastom "und  die  (Renner)  sind  alle  angeschirrt an  die  Deichsel  und  den  Halsring  und das  Joch,  die  mit  dem  aufgespaltenen wohlgefertigten  üb  ergesteckten  Zapfen  zu- sammengehalten sind"  Yt.  jo.  ia5(?).
```


## [2026-09-05T18:07:51.169Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '12830,12860p' BRT.txt; echo \"###### nis.dar\"; grep -n \"niS\\.\\|niš\\.\\|ni§\\.\" BRT.txt | head -20"
}
```


### [2026-09-05T18:07:51.239Z] TOOL RESULT

```
•  j.  davay-  m.  'Betrug'.
KompE.  —  Zum  V.  idai-;  %  36S,  37.  —  mp. vgl  a^auiai;  s.  in  aiauay-.  —  Vgl.  Pö,  in daway-.
•  j.  davayant-  Adj,  (fem,  yäniv-),  PPA,: s,  'dai-.
•  j.  "startvs  vä  puiti  psSti  davaisne  »a" V,  7. 43  PüZ.
•  j.  dava^ah-  Adj,  (?)  —  ?  — :  draxs  hx pairiJvarat  büiü  dalvB  i%yejB  mariaomm •si  V.  Jp,  i;  2.
Gmnz  unklar,  —  Pü. :  fte/tär.
•  j,  "davösa  Vyt  44.
Stammt  woU  ans  V.  31.  10  l^davqtanä).
•  j.  'dar-  V.  'spalten'.  Praes.  7  dar^ dar-,  1 1  dfrmä-^^,  30  (Iter.)  däraya-,  — PPfP.  dinta-',  Inf.  *'d3rmqm.  [Vgl  noch d^TTTiinti^
'spalten,  au&palten,  durch  Spalten  mit einer  Öffnung  versehen':  aat  t!  . .  fm.- yuxta  *Aqm.ivamca  (sd)  .  .  d)nta  .  .  aka YL  10. 1 35,
mit  ava  und  paröii:  s.  Inf.  (Sp.  173). mit  pairi  'durch  Drehen  auszerren,  ab- drehen' :  yat . .  malyHka  . .  un  pairi.dara- yanti  dalma  As  pairi. urvaZsayHnH  "wenn , ,  die  Menschen  .  .  die  Ohren  abdrehen, die  Augen  ihm  (dem  RindJ  ausreissen" Yl  14-  56.
mit  ni!  'herauszenen,  reissen  aus  -' (AaA  mit  Abi.):  ^«äa  vfhrks . .  bar3%rya^ haca  ptihr^m  niidarjjiairyat  "als  ob  ein ,. Wolf  das  Kind  aus  dem  Mutterleib  heraus- risse" V.  18.  38.
■L  dardinti,  t^yjäyai,  äärayati;  dflai, ;  Dp.  darrJ- dani  gr.  ipenif.  —  Pü. ;  darrUan.  —  ')  Nur  im Inf. •  j.  *dar-  V.  'achten',    Ptaes,  27  dir^ya-. —  PPfP.   •dir^ta-. 'achten':  s.  adsrstö.'. mit  3  'achten  auf  — ,  wachen  über  — ' (Akt.):    darssa  na  pairyaoxtaca  umllanä *äd»nyäte ''  nyde  uslanavaitt!  vJsph  frasu- maitls  (sd.)  P.  S^-
ai.  adriyate  'er  beachtet';  BtüI..  IF.  ra.  300, —  Pü,  («Q  P-):  ''örÄ*  inträ',  (in  V.  i6.  l8): adäJt.  —  "VDsT.s  öflla^^'istTlI.  nureinVetsehen;
•  j,,  g,,  p.  3dar-  V.  'halten;  fassen'. Praes.  i  ä3n-,  dr-,  2  dam-  (?),  4  dara-, 5  däiär-'^,  16  (Des.)  dtdar^Ia-''^,  20  'dru-3\ 24  daraya-(?),  30  (Iter.)  däraya-,  30  +  27 (Pass.)  *'d3rya-''^;  PrP.  adariy;  Perf.  i da^är- :  dadr-,  dalr-,  1  dädr-\  J-Aor,  i dänr- :  dars:  ~  PPfP,  d^r^ta-;  Inf.  dar»- dyai,   dar?hräi,  därayS;  Absol.  dtnigm.
1)  "halten,  festhalten,  zurückhalten':  yS vS  x^ayqs  adqs  drJtä  (Opt.)>>  ayantsm urvatsii  (sd.)  .  .  Y.  4^.  5 ;  —  ys  mqm (näml.  Aaomsm)  aiwishubm  därayehi  ya%a tsyüm  Y. //.  3;  —  vupe  haoma  . .  yaiäi qsaAu  dtritänks  Y.  10.  17;  —  ya%a v»krk5  vaysi  (sd.)  taile  *dramnB^1  hart- ääe  Vtf««'«  (sd.)  V.  73. 8;  —  IfravartÜ .  .  duvarayämaiy  bastir  adariy  Bh.a.  13; 15;  —  s.  noch  Inf.  därtys  und  dSra- yap.  a)  mit  Abi.  'zurUck-,  ab-,  fern- halten von  — ':  ke  paeiryS  .  .  ährB  tafmii därayat  tanaoi  haca  mafyehe  V,  20.  i ; I.  q)  mit  abL  Inf.  'halten,  wehren, dass  nicht  — ';  kasnil  dgrtta  samiä  . .  ava- pastsii  (sd.)    V.  44.  4.  b)    mit   Dat
'zurückhalten  zu  — ':  kl  paoiryS . .  yaskim yaskäi  därayat  V.  20.  i;   i.  2)  'woran
(Akk.)  festhalten,  es  beobachten,  nicht davon  abgehen':  \datant  tyJ'  mans  atti^ *adariy''^  "das  Gesetz,  das  meine,  es  wurde gehalten"  D.  6'.  3 ;  —  Ayat  aksyü  (sd.)  ults yS  ahm  dadrl  Y._5J.8;  —  nanm  asavan^m dalrän^m^^  Aumahm^a  maus  .  .  Vr.  2. 5.  a)  fest  im  Gedächtnis  behalten, immer  daran  denken':  siaeta  yemya  .  . dadräna^*  paid/äna  Y.55.6; — yal  dim (nämt,  ahutum  vairTm)  .  .  aakus  .  .  asa- xtai  (sd.)  *sa^qs  dadrän5'°'^  ..  Y.  sg. 10.  3)    'darauf   halten,    dass  — ',    mit
Akk.  und  Inf.,  negirt  sva.  'sich  nicht  darum sorgen,  dass  — ';  nsit  spinlqm  dsr»st"'> ahmsi  stsi  armaitim  "nicht  sorgt  er  sich darum,  die  Arm.  tür  sich  zu  haben"  Y. 4Q.  2"'.  4)  'Jemanden  (Akk.)  verbinden, verpflichten,  zwingen  zu  -'  (Inf,):  kämahyä .  .  ySm  vä  *nasäl  darfst'^*  (V?(sd,)  Y.  43. rj.  5)  Des,,  im  Med.  absol.  'intendere, sich  anschicken  zu  -'  (Inf.):  hyat  ma dngvh  dldar^satä  *ainaiihs  "wenn  der ZV»/genosse  sich  anschickt  mich  zn  ver- gewaltigen" Y.  46. T-  6)  'in  Besitz  nehmen, sich  erwerben;   in  Besitz,  inne,   zu  eigen
dby  Google
691
3dar-  6  a
haben,  besitzen':  I  ima  Ja^sva^  /yS*  aäam *adarsiy  Aaää  (sd)  ana  pärsS  kära  D. 5.2;  —  t^ut^masdämaiy  upastam  abarJ* ylta  im<^  x/ah^am  adary''<'  vasnä  e^urJ'- matdsht^  ima'  xsali^am  därayämiy  "..  bis dieses  Reich  in  Besitz  genoramcn  war  . . habe  ich  dieses  Reich  in  Besitz"  Bh.  7.9:
—  äakyavi^  tyä  däraya^v<^ui , .  adärayir D.6'.4;l  —  yä  (näml  j^aVJ)  därayaj vahishm  mans  tä  .  .  uxsyS  (sd)  Y._y/.  7;
—  *h^l>nte  amt^ä  spinta  sfannS  dära- yänii ..  ^antiS  baxi»nti  YL  7.3;  —  s.  noch InC  dindyäl  und  II  däray<^'.  a)  D  mili- tärisch 'besetzt  halten':  karJ'  .  .  tigram adärayt^  avadä  *a*iäatä  (sd.)  Bh.  /. 18.  7)  '(mit  den  Sinnen)  auffassen, vernehmen':  s.  Int  darfhräi.  8)  absolut 'sich  aufhalten,  weilen' :  s.  AbsoL  a)  bes. '(wo)  seinen  festen  Wohnsitz  haben':  Auga- naia  nämc^  vardanam  ..  avadä  adäraya* Bh.2. 3;  ^.5.  9)  labsol.  'sich  halten, Stand  halten',  militärisch:  Aya^  mudaisuvä ma%tft<^  aht^  kami . .  naiy  adsrayi^  Bh. 2.6.
Undeutlich:  ti  (näml.  fravasayj)  ysiö- yanti  .  .  have  asaJti  Söi^raica  ya^a  as3 mat^ammia  aiwisitJe  dahära  Yt  J_J.67'5'.
mit  ava  'adhibere,  anwenden',  mit  Inf.: ava  pa})ö  ava  zast!  ava  usi  därayavuDm maxdayasna  .  .  dJttyanani  .  .  iysd^nartqm 7-ar»x3i  (sd.)  "wendet  die  FUsse,  wendet die  Hände,  wendet  den  Verstand  an,  um  .." Vr.  15. 1.
mit  ttpa  'stutzen,  festhalten':  fravasayH ,  .  y3  .  .  upaMiiraym  asmaiam  Yt.  JJ,Z9.
xäwpaiti  'redhibere,  zurückbringen  in  — ' (Lok.):  *Z'ljräAu  (sd.)  paiti  tanusu  atti-a gayd  *daryäte  (Konj.)'*'  FrW.4.3,
ant/ra  —  ?  — :  fraäarii'ta',s,A.)(it  täiri- tiam  fradaraysit  N.  Ö7,
mit  Hl  1)  "niedei^,  festhalten':  yö  nö aisqm  aahunqm  kälqm  tiidilrS  anhat Vytjo  (?).  3)  'sich  verborgen  hallen':
###### nis.dar
14243:')  Im  Ausgang  an  dmäspum  und  dniS.slaorqm angeschlossen.  Sonst  wäre  'süm  za  ervorten, ».  RV.  5.  75-  9-
19950:i)  'etwas  (Akk)  merken,  im  Gedächtnis behalten,  dessen  eingedenk  sein' :  mat  täÜ vTspai^  ylfi  tsi  mq%ra  tnanntl  "mit  allen denen,  die  deiner  Worte  eingedenk  sind" y.43.1^; — ta  vs  urvotä  i&A.)  manntn .  .  sJngAamahX  Y.  31.  i.  a)  'merken auf—'  (Akk.):  ^ass  itthaire  . .  ave  aipi daß,yaniS..Aismar3ntB'^Uo.^S;  b)'be- merken':  karS  masyS yB  ranh^h .  .varjss.- '  stavanhm  äpS  urvaäim  marayäte  Yt. 14.29.         2)  Gebete  usw.  (Akk.)  'sich  ins
23151:1  Vyt.  3ä,  40 :  liei  vasna,  %.  pauniS.-  1  'j/ata
```


## [2026-09-05T18:08:05.235Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"darrīdan\" \"darr\" \"dard\" \"drafš\" \"drūdan\" \"nēštar\" \"nēš\" \"dröd\"; do echo \"### $w\"; grep -n -i \"$w\" PHD.txt | head -8; done"
}
```


### [2026-09-05T18:08:06.818Z] TOOL RESULT

```
### darrīdan
3945:tear (v.) darrīdan.
### darr
308:dahigān [dhywk’n' | N dihgān] countryman, farmer. dahliz [d^hlyc | (M dhryz), N ~] portico. dahm [d?hm] virtuous, pious; a full member of the Mazdean community, initiate. dahom [hwm | M dhwm, N ~] tenth. dalman [d”/mn' | N dál(man)] lammergeyer, eagle. dam- , ~išn, v. daftan. īdām [d”m | = M] creature, creation. здат [Pm | = M, N ~] tame animal. здат [d’m | P d’mg, N ~] net, snare, trap. dāmād [d?r?t! | M 424, N ~] bridegroom, son-in-law. ~ih: condition of a bridegroom, son-in-law. daménag [dmynk'] fan. damidan [dmytn'] = daftan. dān-, —išn, v. dānistan. -dàn [-d’n' | = M, N ~] suffix, -holder, -container. dàn(ag) [d”x(k)! | N ~a] seed, grain. Н dānāg [4>рА! | М dwg, N dana] knowing, wise. ША zn kh ~ih: knowledge, wisdom. ar dandàn [KK A < А kk’; dnd’n' | = M, N ~] tooth. dānistan, dān- [YDOYTWN-stn' < A У yd‘; d’n-stn' | M d^n-ystn, N ~] know. ~ign: knowledge. ~i8ndmand [- отпа) knowing. dar [BBA < A bb’; dl | M dr, N =] door; palace; chapter, subject. dar [d?] | M d@’r-, N ~] tree, gallows; wood. dar-, -išn, v. dāštan. -dār [-d'/| M -d’r, N ~] suffix, -holder, -keeper. Р darāy [dPg | J ~, N darāy] bell. *darak [dlk'] section, paragraph. darband [B B Abnd | N ~] gate. darbās [dips] palace. dard [dit! | M drd, N ~] pain. ~отапа [отла | M -wmnd, N ~mand] ill, suffering. dārēn [d'/yn! | М drwyn] wooden. darģāh [dig’s | N ~] doorway. dargardih [d*/krtyh | M d’rgyrdyh] crucifixion. dar-handarzbed [BB A-, dl-hndlcpt'] chamberlain. darigbed [dlykpt'] palace superintendent. *darmag [d?/mk!'] fine, delicate. darmān [dim?n! | M drmn, N ~] remedy, medicine. darridan, darr- [SDKWN-tn! < A V sdg; dl-ytn! | N <] split, tear. dàrüg [d"Iwk! | М drwg, N dari] drug, medicament. dār-wāzīg [Tlw cyk! | N dár-bàz] (pole-)acrobat. darz [dlc | N ~] seam. ~ig [-уА! | N darzi] tailor.
3783:split darridan, škaftan, wisistan.
3945:tear (v.) darrīdan.
4787:darridant sagr sagrih sëm
4809:darr-t
5370:darridan m К ey grēh PV drahnāy p" m druxtan wey da grawih җә уў» dro, 1-2ргам у» drang E » druwand 2 iD druwandih ҷу» >
5378:muy! Cst-! éstádant jagar ozan-t ózadant -gar dar, gar yal darr- draya dravābār dravāb draxt darāy
### dard
172:a-dàd [471], a-dādestān [?- DYNA, -dtst^n'] illegal, unjust. ih: injustice, illegality. a-dahm P@?hm] uninitiated. -ādan [- m! | P dn, N ~] suffix forming secondary infinitives. a-dàn [??п! | M din ignorant. ~ih: ignorance. «адап [??!] wealthy, solvent; wealth. “Аһ: wealth. a-dard [Pdlt'] painless. áüdaróg [wk], ātaxš 1 ~ : the simplest kind of sacred fire. adehig (’dhyk'] indigenous, domestic. adén [?tyn! | М dun) entry. *adén- ['dyn- | = M] bring, lead. ādišt Ptyst'] fire-stand. : ae. D i ‚ (ed уд ádüg Ptwk! | M "?dwg] capable. adur twr! | Mdwr, N ādar] fire; the god ‘Fire’; cal. gth month; oth day. adurestar [twrystl] ashes. ~én [-yx!] ashen. adur- gah [twrg’s] fire altar. ЖЕСЕ, āfrāh PSPs | М ??р?Л] teaching, doctrine. alva 2 KM N facaz\ ‘ace Luch >a-frasāwand [' Bl? wnd] imperishable. afridan, àfrin- / āfur- Pžlytn', ?Blyn-, *pwl- | M 'p(w)ryd, "po -— P >f+yn-, N āfarīdan, afarin-] praise, bless; create. áfrin ['pryn! | M?pryn, N áfarin] praise, blessing. 9544. "tien ~agan [-k”n!] Afrinagan prayers. аїгӧёар [ēlwšk! | N ~ a] a sweetmeat made of flour, butter, and honey. ‚ *afsálàn Pfs'Px!' | (N ābsālān)] springtime. afsān (?psn! | (M ?р?ле), N afsāna] story, fable. afsardan, afsar- ['psi-tn'] cool down. afsārdan, afsar- Pfs?/-tn'] cool, freeze, extinguish. „išn: cooling. afsáy-, v. afsūdan. afsénistan, afsén- [*5syx-stn!, v. abesihén-idan] destroy. --i$n : destruction. afsin [swn | N afsün] spell, incantation. M psan afsös [psws | N ~] scorn, mockery. ~gar [-g/] mocker. afsūdan, afsāy- ['pswtn!, *ps*d-] enchant, protect by spell. afšāndan, afšān- [5Zz?n-tn! | N ~] spread, scatter, sow. afSardan ['5?Its! | N ~] = afšurdan. af$urdan, afšār- 'Pfwltn!,?pP?l- | N ~] press, compress, crush. āfurīdan, afur- ?fwl-ytn', v. Afridan] create. ~išn: creation. -ag [-À! | M -g, N -a] suffix forming (i) adjectives, from nouns and verbal stems, (ii) nouns, from adjectives and present stems.
207:~ widardan: outstrip. andarag [adig] in, between, among. andarmāh [?ndim’h] new moon. andarón [?ndlwn! | M ?ndrwn, N —rün] inside, within, andarway [ndlw?d | (P ?ndrw'z)] air, atmosphere.
308:dahigān [dhywk’n' | N dihgān] countryman, farmer. dahliz [d^hlyc | (M dhryz), N ~] portico. dahm [d?hm] virtuous, pious; a full member of the Mazdean community, initiate. dahom [hwm | M dhwm, N ~] tenth. dalman [d”/mn' | N dál(man)] lammergeyer, eagle. dam- , ~išn, v. daftan. īdām [d”m | = M] creature, creation. здат [Pm | = M, N ~] tame animal. здат [d’m | P d’mg, N ~] net, snare, trap. dāmād [d?r?t! | M 424, N ~] bridegroom, son-in-law. ~ih: condition of a bridegroom, son-in-law. daménag [dmynk'] fan. damidan [dmytn'] = daftan. dān-, —išn, v. dānistan. -dàn [-d’n' | = M, N ~] suffix, -holder, -container. dàn(ag) [d”x(k)! | N ~a] seed, grain. Н dānāg [4>рА! | М dwg, N dana] knowing, wise. ША zn kh ~ih: knowledge, wisdom. ar dandàn [KK A < А kk’; dnd’n' | = M, N ~] tooth. dānistan, dān- [YDOYTWN-stn' < A У yd‘; d’n-stn' | M d^n-ystn, N ~] know. ~ign: knowledge. ~i8ndmand [- отпа) knowing. dar [BBA < A bb’; dl | M dr, N =] door; palace; chapter, subject. dar [d?] | M d@’r-, N ~] tree, gallows; wood. dar-, -išn, v. dāštan. -dār [-d'/| M -d’r, N ~] suffix, -holder, -keeper. Р darāy [dPg | J ~, N darāy] bell. *darak [dlk'] section, paragraph. darband [B B Abnd | N ~] gate. darbās [dips] palace. dard [dit! | M drd, N ~] pain. ~отапа [отла | M -wmnd, N ~mand] ill, suffering. dārēn [d'/yn! | М drwyn] wooden. darģāh [dig’s | N ~] doorway. dargardih [d*/krtyh | M d’rgyrdyh] crucifixion. dar-handarzbed [BB A-, dl-hndlcpt'] chamberlain. darigbed [dlykpt'] palace superintendent. *darmag [d?/mk!'] fine, delicate. darmān [dim?n! | M drmn, N ~] remedy, medicine. darridan, darr- [SDKWN-tn! < A V sdg; dl-ytn! | N <] split, tear. dàrüg [d"Iwk! | М drwg, N dari] drug, medicament. dār-wāzīg [Tlw cyk! | N dár-bàz] (pole-)acrobat. darz [dlc | N ~] seam. ~ig [-уА! | N darzi] tailor.
651:wénig [wynyk! | M wynyg, N bini] nose. wénO£ [wynwk' | N bunü] lentil. wēš [zoy£ | = M, N béf] more. wé&ag [wysR! | N beta] thicket, wood. --estün [-st?n'] woodland. ~ig [-yk'] silvan. wēwag [wdpk! | N béwa] widow. 1wéxtan, wez- [NSSHWN-tn! < А V nsh; wyhtn', wyc- | P wyxt-, N bextan, béz-] sift, select, choose, separate, cleanse, purify, winnow. ~išn: selection. *wēxtan, wēz- [wyhtn!, wyc-] swing, brandish, throw, pour out. Wīdadafš [wydtpš = Av. wīdašafšū-| the south-western continent of the earth. widang [wtng | P wdng] trouble, distress, constraint. widār [xt' | N gudár] passage, entrance. widarag [wtlg | M wdr, N guàar] path, passage. widardan, wider- [wtitn!, wt(y)l- | M wd(y)r-, N guóar-] pass (by, away), cross, die. : ~išn(īh): passage, crossing, death. ~i$nig : transient. widārdan, widār- [xwt?/-tn! | M wyd’r-, N guóárdan] let pass, transport; endure, suffer. widārīdan [w?lytn'] = widardan. widaštan [wtstn' | N gušaštan] = widardan. widāxtan, widāz- [wt’hin', wtc- | (P wd’c-), N gudaxtan, gudāz-| melt, dissolve. widāzīhistan, widazih- [wt’cyh-stn'] be melted, dissolved. wider- , -išn(-īģ, -ih), v. widardan. widerān [wt(y)?n! | N guóarán) transient, dying. widest [zot(y)st! | N bidast] (hand) span (9 in.). ~ig [-yk'] span-sized, midget. widimās [wtym’s | (M wyd’m’s)] wonder, miracle. ~ig [-уА!] wonderful. ~ih: miracle. widimušt [wtymust | M wd(y)mwšt] astonished. ~ih: astonishment. *widwar [wytwl] contented, resigned, consoled. ~ih: contentment, resignation, consolation. wiftag [wyptk'] passive sodomite. wigrad [zogPt! | N bīdār] awake, alert. wigradan, wigras- [zog tn, wgl’s- | M wygr'd, wygr’s-] awaken, rouse. ~i$n(ih): awakening. wih-, v. wistan. wihan(ag) [zh?n(k)', (b-) | M wl?ng, N bahāna] cause, reason. wihēz- [wyhyc- | M twhyz-] move, progress. wihéz(ag) [wyhyc(k')] movement, progression.
1444:cross widardan, (widaštan).
1601:die (v.) murdan, widardan, (widaš- tan).
3012:outstrip andar widardan.
3031:pain bēš, dard, pim.
### drafš
314:~th: friendship, love. 140$ [dws | N ~] shoulder. 2108 [duš | N ~] last night, previous evening. dēš-, —išn, v. Ł 2 dēšīdan, !doxtan. dēšag [dwsk'] dear, loving. —ih: love. došaram [dwi?m | M dw%’rm] love. dēšastar [dušstl] west. īdēšīdan, 458- [dws-ytn!] like, love. ~ign: liking, pleasure. *došidan [dwsytn'] = *dóxtan. dēšīzap [dwsyck' | (M дох, ] dwskyzh), N —a] maiden, virgin. “АҺ: maidenhood, virginity. dówom [2wm | N ~] -second (in compound numerals). 1dóxtan, dēš- [dwhtn', dws | N ~] milk. *dóxtan, döz- [dwhtn', dwc- | N ~] sew. dóys?r [dwysl = Av. dõiðra-} eye. dēz-, v. ?dóxtan. drafš [dips | P drfš, N ~] banner. drafšīdan, drafš- [dipi-ytn! | P drfi-, N ~] 1. shine; 2. tremble. drahm [ZWZN! < А zwza | M drhm, N dir(h)am] drachm. dra(h)nāy [di(k)rd) length. dramanag [dimnk! | N dirmana] wormwood. dranģ [ding | N dirang] period, duration. dranjidan, dranj- [dInc-ytn!] speak. ~išn: speech. draxt [4/0)А | M drxt, N diraxt] tree. drày-, ~išn, v. drāyīdan. drayā(b) [dlyd?(p) | M dry?b, N darya(b)] sea. ~-bār LI | N -bàr] sea-shore. агауӣп-јбуіёп [did?n ywdsn'] one who speaks while eating. ~ih: (the sin of) speaking while eating. drayidan / drayistan, drāy- [dPd-ytn!, -stn! | M dryst, dPy-, N daráyidan] speak (daevic), chatter. —išn: chatter. drāz [dlc | N diráz] long. *drém [dlym] phlegm. driyó$ [41220 | N daryūš, darwé§] poor, needy. ~th: poverty. dró [KDBA < А kdb’; dlwb! | M drw, (N daróy)] lie, deceit. drd [SRM < A šim; dlwt! | M атта, N daród] health, well-being, prosperity, peace. dró-dadwarih [KDB A d'twblyh] false judgement. īdron [dlwn' | N dariina] bow. *drón [dlwn' | N darūn] consecrated bread, ceremony in which c.b. is used.
599:u- [AP- < А р | M'w-] = ud (when followed by a suffixed pronoun, e.g. u-š). ud [W < А w | M ?wd, N u] and. udrag (^wdlk! = Av. udra-] otter. ul (LALA < А I-*P | M ?wl] up(wards). ~ āmadan: rise, ~ih: upward direction. ul-āmadān [LALA YATWNPn!',*wl?mt?n") astr. ascendant. *ul-drafš, v. xurdrus. ummēd Pwmyt! | N ~] hope. ~war [-w?/ | N ~] hopeful. Urdwahišt Pertwhst'] = Ardwahist. Urišlīm Pwlyštym | N ~] Jerusalem. urmód Pwlmwt! | (N amród)] pear. *uruspar Pwlwspl = Av. uru0Bar-] intestines, womb; core, essence. urwahm(an) [wig hm(n') | M ?wrw’hm-] joyful. ~ЛЬ : joy, pleasure, delight. urwar Pwlwl | M ?wrwr] plant(s), vegetable.
925:banner drafš, nīšān.
3630:shine brāzīdan, drafšīdan, frēgīh- istan, tāftan, (tābīdan).
4064:tremble Candidan, drafšīdan, larz- idan.
5361:garmowar garmowarih *dramanag garmscr darbās drubustih drubust drafš
5362:drafš-
5363:drafšīdan
### drūdan
2868:mow drūdan.
### nēštar
### nēš
803:antidote anēš, jud-bëš, pādzahr.
1417:countless amar(ag), anēšmār, авар.
1502:death marg(īh), ēš, widerišn(īh), P murd; moment of — gyān kandan; deserving — margarzān; risk —, fight to ~ anēš xwardan.
1507:deceased anēšagruwān; v. blessed.
2383:immortal ahēš, amarg, anēš(ag).
2384:immortality ahēšīh, amargih, anēša- gih.
2446:innumerable amar, anēšmār, азар.
2848:mortal anēšxwar, géhanig, marg- ómand, 686mand, sazišnīg,
### dröd
```


## [2026-09-05T18:08:15.024Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"drūdan\\|dru(n)\\|drūy\" PHD.txt | head -10; echo \"=== PHD line 316 area (dr..)\"; sed -n '315,317p' PHD.txt | head -c 3000"
}
```


### [2026-09-05T18:08:15.093Z] TOOL RESULT

```
2868:mow drūdan.
=== PHD line 316 area (dr..)
drón yastan 28 duš-čihr
drón yaštan: consecrate the sacrificial bread. drēš [410] mark, branding; punishment. ~ag [-k!] *desolation. drēšīdan, dro$- [d/w$-ytn'] brand. drēūšom [dlwšwm] mark. droz-, v. druxtan. drózan [dlwen! | M, J drwzn] lying, liar. ^h: falsehood. drubušt [di(w)pwst'] fortress. ~ih: defence, fortification. drüdan, *drün- (HCDLWN-tn! < A У hsd | M ача, (dwr-), N durüdan, diraw-] reap, mow. drust [drw(y)st' | (M dryst), N durust] right; well, healthy. —Ih: righteous; health. drustabed [drwystpt'] chief physician. društ [dlwšt' | N durust] harsh, rough, severe. ~ih: harshness, severity. ~-Awaz, ~-éwaz [-p'c, ~yw’c] harsh-spoken. druwand [dlwnd | M drwnd] evil, sinful, unrighteous. ~īh: sin, unrighteousness. druxtan, dróz- [dlwhtn', dlwc- | M drwxt, drwz-] lie, deceive. druz [dlwe | (P drwj)] demon. айа [dwt! | M dwd, N ~] smoke. düdag [dwtk! | N —a] family. dudigar [dtykl | M dwdygr, N digar] second. duj-, = duš-. ~-daft [dwsdpt'] ill-breathing, short of breath. ~-dānāg [dwšd”7?k!] ignorant. ~-dén [dwšdyn' | M dwjdyn-] of evil religion. «=dēys*rīh [dwsdwyslyh] the evil eye. ~-gand (dtwsgnd | P dwjgnd] stinking. ~-gandih: stench. dum(b) [dwm(b') | N ~] tail. ~dmand [-'wmnd) tailed. ааг [LH YK'! < А rhyq; dul | M dur, N ~] far, distant, remote. durgar [dwlgl | N ~] carpenter. dusraw [dwslwb!] notorious, dishonoured. ^Ah : notoriety, dishonour. duš- [dws- | = M] ill-, evil-. ~īh: evil, wickedness. ~-абаһ [dw??^ Es] foolish, stupid, ignorant. ~-абаһіһ : foolishness, stupidity. ~-arz [2 ic] worthless. 7--Ca&m [-cém] envious. —-Ca$mih: envy. ~-tihr [-cyhl | M dwfcyhr] ugly, hideous.
duš-ēwāz��h 29 dwāzdahān
```


## [2026-09-05T18:08:27.933Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"darH\\|\\*dar \\|drau\\|\\*dru\" CHEUNG.txt | head -30"
}
```


### [2026-09-05T18:08:27.986Z] TOOL RESULT

```
541:*-eH,, one certain example: *darH ‘to have pain’ (Lat. doleo ‘I suffer, am in pain’) 
4954:*KHOTANESE: ? LKh. paha-drauvi ‘embroidered’ (KT2 18,11a) 
4960:*drauH. 
4990:*darH ‘to have pain’ 
5012:*darH would go back to an old eH;-formation of *dar?. 
5977:*drau2 77 
6010:*drau! *to call on' 
6026:served all three meanings, on which see also *drau’, *drau’. 
6036:*drau? ‘to run’ 
6038:*AVESTAN: Y Av. drauu- ‘to run (?) [daevic]; lead astray’ = Liste: 32 
6045:78 *drau3 
6061:*drau ‘to lead astray, delude’ 
6064:*AVESTAN: ? Y Av. drauu- ‘to run (?) [daevic]; lead astray ?° = Liste: 32 
6066:Partic.: pres. med. ? YAv. dramne (< *draomna- ?) (V 13.8); Caus.: pres. SUBJ. 3sg. YAv. drauuaiiat (Y 
6090:(= Ir. *drau’), Pkt. dhutta- (m.) ‘villain, rogue’. > EWAia I: 802, s.v. dhvar 
6092:© This root should be separated from *drau^ ‘to run’ (?), on which see Schwartz 
6103:*draub ? ‘to scratch, peel off ?' 
6112:*drauH 79 
6119:dropt ‘to tear, scratch; to comb’. > If Oss. reduvyn, etc. does contain *draub, we 
6120:will need to assume some sort of phonological loss of the *-r-: *fra-draub- > 
6138:*drauH ‘to cut (down), mow, reap’ 
6160:*MISC: Orm. dir-, Par. durr- ‘to reap; to mow’, Orm. drau ‘harvest, reaping’ (< Pers.) 
6174:80 *drau(H)s ? 
6177:*drau(H)S ? ‘to make a mark, brand’ 
6198:Q The evidence for the root *drauš is somewhat ambiguous, particularly, 
6203:ingressive s-formation of a root *dreuH-, which is attested in IIr. only (*drauH): 
6212:*drauj ‘to lie, deceive’ 
6266:*drauš ? ‘to grind’ 
6275:© In ESIJa П: l.c., a root *draus is reconstructed, with the meanings ‘to break in 
6279:though; they may rather suggest a different origin, on which see also *drau(H)&. The
```


## [2026-09-05T18:08:31.670Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6138,6175p' CHEUNG.txt; echo \"#### darH pain\"; sed -n '4985,5015p' CHEUNG.txt; echo \"#### dar tear?\"; grep -n \"^\\*dar\\|to tear\\|to split\" CHEUNG.txt | head -20"
}
```


### [2026-09-05T18:08:31.767Z] TOOL RESULT

```
*drauH ‘to cut (down), mow, reap’ 

*MIDDLE PERSIAN: MMP dwr- (BMP HsDLWN-) ‘to reap, mow’ = DMMPP: 139a, 
145b 

Pres.: IND. 3pl. MMP dwrynd; Partic.: perf. pass. MMP dr‘wd 

*KHOTANESE: LKh. drv- ‘to bite, cut? > SGS: — 

*CHORESMIAN: дгу- ‘to mow’ = Samadi: 67 

*NWIR: NP durüdan/dirav- ‘to cut, mow, reap’, Kurd. (Kurm.) dirün, dirutin/diru-, 
(Sor.) dirünawa/dirü- ‘to reap, mow’, Kurd. (Sina) dirawan, (LW) Awrom. dirawan 
‘hired reaper’, Tal. dave ‘to reap, mow’, Abyan. dórün, Abz. doro, Ard. duro, Nn. 
durow, Gz. dürün, Qohr. derün, Semn. derow, Shamerz. deru, Tr. deran, Varz. deron 
*harvest? 

*NEIR: Pash. Iwawol ‘to reap’, Yi. lorí-/lorei-, M. läri-/luriy-, Ishk. dbray-/dbred, 
Sangl. deráy- ‘to reap’, Wa. draw-/drot- ‘to reap; to mow, cut’, Pash. lau, law (LW ?, 
< IAr.), Wa. d(o)reiw(n), Yghn. dirówa, M. loráwa, Yi. Іогбуо, Sh. cow, Bart. caw 
‘harvesting, reaping’ 

*MISC: Orm. dir-, Par. durr- ‘to reap; to mow’, Orm. drau ‘harvest, reaping’ (< Pers.) 
*SANSKRIT: drav ‘to cut down’ (RV), ‘to harm, damage’ (JB) > EWAia I: 756 

© This root is attested in Пг. only, it might be an enlarged root of IE *der- ‘to tear, 
split’ (*dar?), or at least contaminated with it. 


*PIE — = LIV: 129 | Pok.: 208 f. 

*REFERENCES: JIFL II: 224a, 520; MacKenzie 1966: 93; DKS: 171a; WIM II/2: 659; Werba 1997: 297; 
Steblin-Kamenskij 1999: 149, 156; Cabolov 2001: 313 £; Lecoq 2002: 575, 593, 616 (passim); ESIJa II: 
457 ff. 


80 *drau(H)s ? 

#### darH pain


*dars 61 


*darH ‘to have pain’ 

*MIDDLE PERSIAN: MMP drd, BMP dr /dard/ ‘pain, illness’ || (+ *a-) MMP ’y’rd-, 
BMP ’d’It- /ayard-/ (iter.) ‘to suffer; to be distressed, tormented’, MMP ’y’rdysn 
‘distress, torment’ (with -d- from /dard/ ?) || (+ *ui-) ? MMP w(y)d'r- ‘to suffer, 
endure’ (with restored -d- from /dard/ ?). ® Rastorgueva — Edel'man, ESIJa I: 215 f. 
connect MMP ’y’rd-, BMP ’d’It- /ayard-/ to Skt. ага ‘to scatter’, which 15 
semantically difficult. = DMMPP: 138a, 80a, 339a 

(+ *à-) Pres.: IND. 3sg. BMP ’d’Ityt /ayarded/, 3р1. MMP *’y’rdynd, SUBJ. 3р1. MMP ’y’rd’nd; Partic.: 
perf. pass. MMP ’y’rdyd || (+ *ш-) Pres.: IND. 3sg. MMP wyd’ryd, 3р1. MMP wyd’rynd; Partic.: perf. 
pass. MMP wd’st 

*PARTHIAN: drd ‘pain || (+ *ui-) w(y)d’r- ‘to suffer, endure’ = DMMPP: 139a, 339a 
Pres.: IND. 2sg. wyd’ryh, 3pl. wd’rynd; Partic.: perf. pass. wyd’r’d 

*CHORESMIAN: Ord ‘pain’ 

*NWIR: NP dard ‘pain, affliction’, widely borrowed, e.g. Abyan. dard, Abz. dard, Nn. 
dard, Qohr. dard, Zaz. derd ‘pain’ 

© The Ir. forms above are probably etymologically related to the forms of *dar?: 
*darH would go back to an old eH;-formation of *dar?. 

«PIE *dl-eH;- ‘to suffer, be in pain’ (< ‘to be in a state of tearing, breaking’). 0 The 
suffix *(е)Н, is a well-known IE suffix indicating the state or mood in which the 
#### dar tear?
487:*baid ‘to split’, Skt. srav / plav = Ir. *hrau / *fraw ‘to flow’, Skt. kram / gam / dram 
1469:*baid ‘to split’ 
1482:*SANSKRIT: bhed ‘to split? (RV) = EWAia II: 273 
1542:*NWIR: Tr. sunja/(v)sönj- ‘to tear’ || (+ ?) ? Tr. vsónj- ‘to break’. Ф The initial -s- and 
4743:*darl 57 
4775:*dar! *to hold, keep; [intr.] to dwell 
4859:*dar2 59 
4888:*dar? ‘to tear, split’ 
4889:*AVESTAN: YAv. dar- ‘to tear’ || (+ *aua-) ‘to tear down’ || (+ *pari-) ‘to tear off by 
4903:*MIDDLE PERSIAN: BMP dl- (SDKWN-) /darr-/ ‘to tear, cut’, BMP dlyn- /darren-/ ‘to 
4916:*NWIR: NP darridan, Bal. dirt/din-, dir(r)- ‘to tear up’, Kurd. dirin/dir- ‘to be torn’, 
4917:dirandin/dirin- (caus.), Zaz. dira ‘to tear off, cut off’, Awrom. diriáy/dir- ‘to tear’, 
4918:Gur. (Kand.) айтап (ppp.) ‘carved up, in pieces’, -därr- ‘to tear off, smash, carve 
4919:up’, Jow. bam-der-/a-der- ‘to tear off’, Khuns. dir-/dira, Siv. deria ‘to be torn’, 
4920:(caus.) Khuns. dirn-/dirna, Siv. der-/däränd, Tal. darniye ‘to tear [tr.]’, NP dar 
4934:*SANSKRIT: dar ‘to tear, split? (R V+). Ф The set-variants are secondary, on which see 
4937:«PIE *der- ‘to tear, split? = LIV: 119 f. | Pok.: 206 ff. 
4939:ТЕ COGNATES: Gr. óépo ‘I skin’, OCS дьай, Lith. dirti (diriu) ‘to tear’, Goth. 
4942:dis-tairan ‘to tear up’, Engl. to tear, etc. 
4950:*darb (*darf) ‘to join, tie, sew (together)’
```


## [2026-09-05T18:08:42.457Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"der-\\b\" AHD_watkins1985.txt | head -20; echo \"======\"; grep -n \"drep\\|derma\\|pachyderm\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-05T18:08:42.525Z] TOOL RESULT

```
366:diphthera, prepared hide, leather (used to write on): DIPHTHERIA. 2. Latin littera, letter (possibly borrowed from Greek diphthera in the sense of “tablet” via Etrus- can): LETTER, LITERAL, LITERARY, LITERATE, LITERA- TIM; (ALLITERATE), ALLITERATION, (ILLITERATE), OBLITERATE, TRANSLITERATE. [Pok. deph- 203.] der-', Assumed base of roots meaning “to run, walk, step.” 1. Zero-grade form “dr- in extended Germanic form “*tred- in: a. Old English tredan, to step: TREAD, TREADLE; b. Middle Low German trade, course, track: TRADE. 2. Extended form *dreb- in Germanic *frep-, “something on or into which one steps,” in: a. Old English treppe, treppe, snare: TRAP; b. Middle Low German trappe, stair: TRAP’, c. Middle Dutch trappe, stair: WENTLETRAP; d. Old French trap(pje, snare: EN- TRAP; @. Middle Dutch érippen, to stamp, trample: TRIP. 3. Nasalized Germanic root *tremp- in: a. Middle Low German trampen, to stamp, tread: TRAMP; b. Italian trampoli, stilts: TRAMPOLINE. 4. Germanic *iérott- (ex- pressive derivative of *tred-) in Old French ¢roter, to trot: TROT. 5. Root form *drd- possibly in reduplicated Germanic form *ti-trd- in Old Norse titra, to tremble: TEETER. 6. Root form *drem- in suffixed o-grade form *drom-o- in: a. Greek dromos, a running, race, race- course: -DROME, DROMOND, -DROMOUS; ANADROMOUS, LOXODROMIC, PALINDROME, PRODROME; b. Greek dro- mas, running: DROMEDARY. [Pok. 3. (der-) 204.] der-2, To split, peel, flay; with derivatives referring to skin and leather. 1. Germanic *teran in Old English teran, to tear: TEAR}. 2. Germanic *ter-t- in Old English teart, sharp, severe: TART). 3. Suffixed zero-grade form *dr-tom, “‘something separated or discarded,” in Ger- manic *turdam, turd, in Old English tord, turd: TURD. 4. Reduplicated form *de-dr-u- in Old English teée)r, eruption, skin disease: TETTER. 5. Greek derris, leather covering: DERRIS. 6. Suffixed form *der-mn in Greek derma, skin: -DERM, DERMA!, -DERMA, DERMATO-; EPI- DERMIS. 7. Perhaps extended root *drep- in the Celtic source (itself borrowed) of Late Latin drappus, cloth (> Old French drap): (DRAB!), DRAPE, TRAP?. [Pok. 4. der- 206.) derbh-. To wind, compress. Zero-grade form “drbh- in Germanic *turb- in: a. Old English turf, slab of sod or peat: TURF; b. Medieval Latin turba, turf: TURBARY. [Pok. derbh- 211.] dere-. To work. Variant form *drd- (< *draa-) in Greek dran, to do: DRAMA, DRASTIC. [Pok. dero- 212.] dergh-. To grasp. 1. Perhaps Germanic *targ- in Old French targe, shield: (TARGE), TARGET. 2. Perhaps zero-grade form *drgh- in Greek drassesthai, to grab (> drakhmé, “handful,” drachma): DRACHMA. [Pok. dergh- 212.] derk-. To see. Suffixed zero-grade form *drk-on(t)- in Greek drakén (> Latin dracé), serpent, dragon (< “mon- ster with the evil eye”): DRAGON, (DRAGOON), (DRAKE?2), RANKLE. [Pok. derk- 213.] deru. Also dreu-. To be firm, solid, steadfast; hence specialized senses “wood,” “tree,” and derivatives refer- ring to objects made of wood. 1. Suffixed variant form *drew-o- in: a. Germanic *trewam in Old English tréow, tree: TREE; b. Germanic *freuw6 in Old English tréow, pledge: TRUCE. 2. Variant form *dreu- in Germanic *treuwaz in: a. Old English tréowe, firm, true; TRUE; b. Old English tréowian, triiwian, to trust: TROW; c. Old Norse tryggr, firm, true: TRIG!; d. Germanic abstract noun *treuwithé in Old English tréowth (> Middle English tro(u)the), faith, loyalty, truth: TROTH, TRUTH; BETROTH; @. Germanic abstract noun *traustam in Old Norse traust, confidence, firmness: TRUST; f. Old Norse denominative treysta, to trust, make firm, akin to the probable source of Old French triste, waiting place (< “place where one waits trustingly”): TRYST. 3. Variant form “drou- in Germanic *traujam in Old English trég, trig, wooden board: TRAY. 4. Suffixed zero-grade form
369:*dru-ko- in Germanic *trugaz in Old English trog, wooden vessel, tray: TROUGH. 5. Suffixed zero-grade form *dru-mo- in Germanic *trum- in Old English trum, firm, strong (> trymman, to strengthen, arrange): TRIM. 6. Variant form *derw- in Germanic *terw- in Old Eng- lish fe(o)ru, resin, pitch (obtained from the pine tree): TAR}. 7. Suffixed variant form *dri-ro- in Latin diirus, hard (of whose English derivatives many represent a semantic cross with Latin dirdre, to last long; see deue-): DOUR, DURAMEN, DURESS, DURUM; (DURA MA- TER), ENDURE, INDURATE, OBDURATE. 8. Lengthened zero-grade form *dré- in Greek drus, oak: DRUPE, DRYAD; GERMANDER, HAMADRYAD. 9. Reduplicated form *der-drew-, dissimilated with suffix in *den-drew- on in Greek dendron, tree: DENDRO-, DENDRON; PHILO- DENDRON, RHODODENDRON. 10. Celtic compound *dru-wid-, “knower of trees” (*wid-, to know; see weid-), the Celtic priestly caste, associated with a tree-cult, probable source of Latin druides, druids: DRUID. 11. O-grade form *doru- in Sanskrit daru, wood, timber: DEODAR. [Pok. deru- 214.]
1242:ANA- an! ANABAENA gWa- ANABAPTIST g¥ébh-1 ANABIOSIS gWei- ANACOLUTHON sem-! ANACRUSIS kreue-2 ANADEM dé- ANADIPLOSIS dwo- ANADROMOUS der-1 ANAGLYPH gleubh- ANAGOGE ag- ANALCIME = alek- ANALECTS leg-1 ANALEPTIC (s)lag¥- ANALOGOUS leg-! ANALYSIS leu-1 ANAMNESIS men-1 ANAPEST peu- ANAPHORA bher-? ANARTHROUS ar- ANASARCA twerk- ANASTOMOSIS ste-men- ANASTROPHE  streb(h)- ANATHEMA dhé-1 ANATOMY tem- ANCESTOR ked- ANCHOR ank- ANCHORITE ghé- ANCIENT! ant- ANCILLARY kWel-1 ANCON ank-
1420:DEODAR deiw-, deru DEONTOLOGY deu-1 DEPEND (s)pen- DEPICT peig-1 DEPILATE pilo- DEPLOY plek- DEPLUME pleus- DEPONE apo- DEPOPULATE populus DEPORT per-2 DEPOSIT apo- DEPRECATE prek- DEPRECIATE per-6 DEPREDATE ghend- DEPRESS per-5 DEPRIVE pert DEPTH dheub- DEPURATE peue- DEPUTE peu- DERACINATE wrad- DERANGE sker-3 DERELICT leikw- DERIVE rei-3 -DERM der-2 DERMA! der-2 DERMA? tera-1 -DERMA der-2 DERMATO- der-2 DEROGATE reg-! DERRIS der-2 DESCANT kan- DESCEND skand- DESCRIBE skribh- DESERTS = ser-3 DESERVE servus DESICCATE selkw- DESIGNATE sekw-1 DESIRE sweid-1 DESIST sta- DESMID dé- DESOLATE s(w)e- DESPAIR spé-1 DESPICABLE spek- DESPISE spek- DESPOIL spel-! DESPOND spend- DESPOT deme-! DESTINE sta- DESTITUTE sta- DESTRIER deks- DESTROY ster-2 DESUETUDE s(w)e- DESULTORY sel-4 DETAIN  ten- DETECT (s)teg- DETENT ten- DETER tres- DETERIORATE de- DETERMINE ter- DETEST trei- DETONATE (s)tene- DETOUR tera-1 DETRACT tragh- DETRIMENT tera-1 DETUMESCENCE teue- DEUCE! dwo- DEUTERAGONIST deu-? DEUTERIUM deu-!
1434:DOTE dud- DOUBLE dwo- DOUBLET dwo- DOUBLOON dwo- DOUBLURE dwo- DOUBT dwo- DOUCEUR dik-u- DOUCHE deuk- poucH dheigh- DOUGHTY dheugh- DOUR deru. DOVE! dheu-1 DOWAGER dé- DOWEL dheubh- DOWER do- Down! dhino- pDowN2 dheu-! pown’ dhiino- Dowry do- DOXOLOGY dek-1 DOYEN deki DOZE dheu- DOZEN dekm, dwo- DRAB! der-2 DRAB? dher-! DRABBLE dher-! DRACHMA dergh- DRAFT dhragh- DRAG dhragh- DRAGON derk- DRAGOON derk- DRAIN dreug- DRAKE? derk- DRAMA dera- DRAMATURGE werg- DRAPE der-2 DRASTIC dere- DRAW dhragh- DRAY dhragh- DREAM dhreugh- DREARY dhreu- DRECK sker-4 DREGS dher-1 DRENCH dhreg- DRIFT dhreibh- DRILL! tere-1 DRINK dhreg- DRIP dhreu- DRIVE dhreibh- DRIVEL dher-! DRIZZLE dhreu- -DROME der-1 DROMEDARY der-1 DROMOND der-1 -DROMOUS der-1
1464:ENTO- en ENTOMO- tem- ENTRAILS en ENTRAP der-1 ENTREPRENEUR ghend- ENTRESOL sel-1 ENTROPY trep-2 ENUMERATE nem- ENUNCIATE neu-! ENURESIS wers-2 ENVOI wegh- ENVOY! wegh- ENVY weid- ENZYME yeud- EO- aus-! EQOHIPPUS ekwo- EON aiw-
1468:EPIBOLY gWele-1 EPIC wekw- EPICARDIUM kerd-1 EPICENE kom EPICRITIC krei- EPIDEMIC da- EPIDERMIS der-2 EPIDIDYMIS dwo- EPIDOTE do- EPIGASTRIUM gras- EPIGEAL gé EPIGENE gene- EPIGONE gene- EPIGRAM gerbh- EPIGRAPH gerbh- EPILEPSY (s)lag- EPILOGUE leg-1 EPIMYSIUM mis- EPIPHANY bha-1 EPIPHYSIS bheue- EPISCOPAL spek- EPISODE en, sed-2 EPISTASIS sta- EPISTAXIS stag- EPISTEMOLOGY sta- EPISTLE  stel- EPISTYLE sta- EPITAPH dhembh- EPITASIS ten- EPITHELIUM dhé@(i)- EPITHET dhé-1 EPITOME tem- EPOCH segh- EPODE wed-2 EPONYM nd-men- EPONYMOUS nd-men- EPOS wekw-
1769:Lox! =laks- LOXODROMIC  der-1 LOYAL leg-1 LUBRICATE sleubh- LUBRICIOUS sleubh- LUBRICITY sleubh- LUCARNE leug-1 LUCENT leuk- LUCID leuk- LuciFER leuk- LUCIFERIN leuk- Lucina leuk- LUCRATIVE lau- LUCRE aus LUCUBRATE leuk- LUCULENT leuk- LUDICROUS leid-
2040:PALIMPSEST bhes-1, kwel-1 PALINDROME der-1, kwel-1
2136:PRO-2 per? PROBABLE per! PROBE pert PROBITY per! PROBLEM gWele-1 PROBOSCIS g¥6- PROCEED ked- PROCLAIM kele-2 PROcLITIC § klei- PROCLIVITY klei- PROCREATE ker-3 PROCTITIS prdkto- PROCTOLOGY prdkto- PROCTOR cura PROCTOSCOPE prdkto- PROCUMBENT keu-2 PROCURATOR cura PROCURE cura PROCYON kwon- PRODIGAL ag- PRODIGY ég- PRODROME der-1 PRODUCE deuk- PROFANE dhés- PROFESS bha-2 PROFESSOR reg-! PROFFER bher-1 PROFICIENT dhé-1 PROFILE gWhi- PROFIT dhé-1 PROFLIGATE bhiig- PROFOUND bhudh- PROFUSE gheu- PROGENITOR gene- PROGENY gene- PROGLOTTID glégh- PROGNOSIS gnd- PROGRAM gerbh- PROGRESS ghredh- PROHIBIT ghabh- PROJECT yée- PROLAN al-3 PROLAPSE leb-1 PROLATE tele- PROLEGOMENON leg-! PROLEPSIS (s)lag¥- PROLETARIAN al-3 PROLIFEROUS _al-3 PROLIFIC al-3 PROLIX wleik- PROLOCUTOR tolkw- PROLOGUE leg-1 PROLONG del-1 PROLUSION leid- PROMENADE men-2 PROMINENT men-2 PROMISCUOUS meik- PROMISE (s)meit(e)- PROMOTE meue- PROMPT em- PRONE per! PRONEPHROS _ negwh-ro- PRONOUN no-men- PRONOUNCE neu-! PROOF per! PROPAGATE pag- PROPEL pel-6 PROPEND (8)pen- PROPER pert PROPERTY per? PROPHET bha-2 PROPHYLACTIC phulax PROPINQUITY per? PROPIONIC ACID peie- PROPITIOUS pet- PROPOLIS pele-3 PROPORTION pere-2 PROPOSE apo- PROPRIOCEPTION per! PROPRIOCEPTOR per? PROPTOSIS pet- PROPYLAEUM pulé PROPYLON pulé PROROGUE reg-1 PROS- pert PROSCRIBE skribh- PROSE wer-3 PROSECUTE sekw-1 PROSELYTE leudh-1 PROSOMA teue- PROSOPOPEIA kWwel-2, per! PROSPECT spek- PROSPER spé-1 PROSTATE sta- PROSTHESIS dhé-1 PROSTITUTE sta- PROSTOMIUM ste-men-
2341:TARGE dergh- TARGET dergh- TARSUS  ters- TART! der-2
2348:TEAM deuk- TEAPOY ped-1 TEAR! der-2
2349:TEAR? dakru- TECHNICAL teks- TECHNOLOGY teks- TECTONIC teks- TECTRIX (s)teg- TECTUM (s)teg- TEEM! deuk- TEEN? deu-3 TEETER der-1 TEETOTUM teuta- TEGMEN (s)teg- TEGMENTUM (s)teg- TEGULAR (s)teg- TEGUMENT (s)teg- TEIGLACH dheigh- 'TELAMON tele- TELANGIECTASIA ten- TELE- kwel-2 TELEKINESIS kei-3 TELEOLOGY kWel-1 TELEOST kWel-1, ost- TELESCOPE spek- TELEUTOSPORE kwel-1 TELIC kwel-1 TELIUM kwel-1 TELL del-2 TELLURIAN tel- TELLURIC tel- TELLURION tel- TELLURIUM tel- TELLURO- tel- TELO- kwel-1 TELPHER bher-1 TEMERARIOUS teme- TEMERITY teme- TEMPLE! tem- TEMPLE? temp- TEMPLES tem-
2364:TETRAHEDRON sed-! TETTER der-2 TEUTON teuta- TEXT teks- THALIA dhal- THALLUS dhal- THAN to- THANATOS dhwene- THANE tek- THANK tong-
2398:TOXOPLASMA pele-2 TRABEATED treb- TRABECULA treb- TRACHEA dher-1 TRACHEOPHYTE bheue- TRACHOMA dher-1 TRACHYTE dher-1 TRACT! tragh- TRACTABLE tragh- TRACTION tragh- TRADE der-1 TRADITION d6- TRADUCE deuk- TRAGACANTH ak- TRAGEDY wed-2 TRAIL tragh-
2400:TRAIN OIL dakru- TRAIT tragh- TRAITOR d6- TRAJECT yé TRAMMEL macula, trei- TRAMP der-! TRAMPOLINE der-1 TRANCE ei-1 TRANQUIL kweie-2 TRANS- tere-2 TRANSACT ag- TRANSCEND skand- TRANSCRIBE  skribh- TRANSDUCER deuk- TRANSECT sek- TRANSFER bher-1 TRANSFIGURE dheigh- TRANSFIX dhig¥- TRANSFUSE gheu- TRANSGRESS ghredh-
2402:TRANSIENT ei-1, tera-2 TRANSIT ei-1 TRANSITIVE ei-1 TRANSLATE tele- TRANSLITERATE deph- TRANSLUCENT leuk- TRANSMIT (s)meit(@)- TRANSMUTE mei-1 TRANSOM tere-2 TRANSPIRE § spirare TRANSPONTINE pent- TRANSPORT per-2 TRANSUDE sweid-2 TRANSVERSE wer-3 TRAP! der-1
2403:TRAP2 der-2
2404:TRAP? der-1
2406:TRAPUNTO peuk- TRAUMA tera-1 TRAVAIL pag- TRAVE treb- TRAVEL pag- TRAVESTY wes-4 TRAY deru TREACLE ghwer- TREAD der-1 TREADLE der-1 TREASON d6- TREAT tragh- TREBUCHET beu-1 TRECENTO dekm, trei- TREE deru TREFOIL bhel-3 TREMATODE tere-! TREMENDOUS trem- TREMOR trem- TREMULOUS trem- TRENCH tera-2 TREPAN! tere-1 TREPHINE trei- TREPID trep-1
======
366:diphthera, prepared hide, leather (used to write on): DIPHTHERIA. 2. Latin littera, letter (possibly borrowed from Greek diphthera in the sense of “tablet” via Etrus- can): LETTER, LITERAL, LITERARY, LITERATE, LITERA- TIM; (ALLITERATE), ALLITERATION, (ILLITERATE), OBLITERATE, TRANSLITERATE. [Pok. deph- 203.] der-', Assumed base of roots meaning “to run, walk, step.” 1. Zero-grade form “dr- in extended Germanic form “*tred- in: a. Old English tredan, to step: TREAD, TREADLE; b. Middle Low German trade, course, track: TRADE. 2. Extended form *dreb- in Germanic *frep-, “something on or into which one steps,” in: a. Old English treppe, treppe, snare: TRAP; b. Middle Low German trappe, stair: TRAP’, c. Middle Dutch trappe, stair: WENTLETRAP; d. Old French trap(pje, snare: EN- TRAP; @. Middle Dutch érippen, to stamp, trample: TRIP. 3. Nasalized Germanic root *tremp- in: a. Middle Low German trampen, to stamp, tread: TRAMP; b. Italian trampoli, stilts: TRAMPOLINE. 4. Germanic *iérott- (ex- pressive derivative of *tred-) in Old French ¢roter, to trot: TROT. 5. Root form *drd- possibly in reduplicated Germanic form *ti-trd- in Old Norse titra, to tremble: TEETER. 6. Root form *drem- in suffixed o-grade form *drom-o- in: a. Greek dromos, a running, race, race- course: -DROME, DROMOND, -DROMOUS; ANADROMOUS, LOXODROMIC, PALINDROME, PRODROME; b. Greek dro- mas, running: DROMEDARY. [Pok. 3. (der-) 204.] der-2, To split, peel, flay; with derivatives referring to skin and leather. 1. Germanic *teran in Old English teran, to tear: TEAR}. 2. Germanic *ter-t- in Old English teart, sharp, severe: TART). 3. Suffixed zero-grade form *dr-tom, “‘something separated or discarded,” in Ger- manic *turdam, turd, in Old English tord, turd: TURD. 4. Reduplicated form *de-dr-u- in Old English teée)r, eruption, skin disease: TETTER. 5. Greek derris, leather covering: DERRIS. 6. Suffixed form *der-mn in Greek derma, skin: -DERM, DERMA!, -DERMA, DERMATO-; EPI- DERMIS. 7. Perhaps extended root *drep- in the Celtic source (itself borrowed) of Late Latin drappus, cloth (> Old French drap): (DRAB!), DRAPE, TRAP?. [Pok. 4. der- 206.) derbh-. To wind, compress. Zero-grade form “drbh- in Germanic *turb- in: a. Old English turf, slab of sod or peat: TURF; b. Medieval Latin turba, turf: TURBARY. [Pok. derbh- 211.] dere-. To work. Variant form *drd- (< *draa-) in Greek dran, to do: DRAMA, DRASTIC. [Pok. dero- 212.] dergh-. To grasp. 1. Perhaps Germanic *targ- in Old French targe, shield: (TARGE), TARGET. 2. Perhaps zero-grade form *drgh- in Greek drassesthai, to grab (> drakhmé, “handful,” drachma): DRACHMA. [Pok. dergh- 212.] derk-. To see. Suffixed zero-grade form *drk-on(t)- in Greek drakén (> Latin dracé), serpent, dragon (< “mon- ster with the evil eye”): DRAGON, (DRAGOON), (DRAKE?2), RANKLE. [Pok. derk- 213.] deru. Also dreu-. To be firm, solid, steadfast; hence specialized senses “wood,” “tree,” and derivatives refer- ring to objects made of wood. 1. Suffixed variant form *drew-o- in: a. Germanic *trewam in Old English tréow, tree: TREE; b. Germanic *freuw6 in Old English tréow, pledge: TRUCE. 2. Variant form *dreu- in Germanic *treuwaz in: a. Old English tréowe, firm, true; TRUE; b. Old English tréowian, triiwian, to trust: TROW; c. Old Norse tryggr, firm, true: TRIG!; d. Germanic abstract noun *treuwithé in Old English tréowth (> Middle English tro(u)the), faith, loyalty, truth: TROTH, TRUTH; BETROTH; @. Germanic abstract noun *traustam in Old Norse traust, confidence, firmness: TRUST; f. Old Norse denominative treysta, to trust, make firm, akin to the probable source of Old French triste, waiting place (< “place where one waits trustingly”): TRYST. 3. Variant form “drou- in Germanic *traujam in Old English trég, trig, wooden board: TRAY. 4. Suffixed zero-grade form
```


## [2026-09-05T18:08:54.881Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### KLN tear\"; grep -n \"tear, v\\.\\|'tear'\\|drape\\|derma, n\\.\\|pachyderm\" KLN_1966.txt | head -20"
}
```


### [2026-09-05T18:08:54.953Z] TOOL RESULT

```
### KLN tear
6644:caryatid,  n.,  a  draped  female  figure  supporting  a column  (archil.)  —  L.  Caryatides,  fr.  Gk.  Kapu- a-rdtep,  ‘priestesses  of  Artemis  (=  the  Roman Diana)  at  Caryae',  sing.  Kapoaxi;;  so  called  fr. Kxpjxi,  ‘Caryae’,  a  town  in  Laconia  (prob.  in allusion  to  the  dance  of  the  virgins  at  the  festival held  in  the  temple  of  Artemis  Caryatis  at  Caryae). Caryocar,  n.,  a  genus  of  trees  of  the  family  Cary- ocaraceae  (hot.)  —  ModL.,  compounded  of  Cik. xxpoov,  ‘nut,  walnut’,  and  vA p,  ‘head’;  so called  in  allusion  to  the  large  fruit.  See  careen and  cranium  and  cp.  Carya.
10963:-derm,  suff.  meaning  ‘skin,  covering’,  as  in  blas¬ toderm.  —  Fr.  Gk.  Seppa,  ‘skin’.  See  derma  and cp.  pachyderm.
10964:derma,  also  derm,  n.,  skin,  esp.  the  layer  of  the skin  below  the  epidermis  ( anat .)  —  ML.  derma, fr.  Gk.  Seppa,  ‘skin’,  formed  with  suff.  -pa  (see -m),  from  the  stem  of  Sepetv,  Setpeov,  ‘to  flay’ (whence  also  Sepap,  Sipoq,  Seppt;,  8op&,  ‘skin’, Sapat?,  ‘tearing,  flaying,  separation’),  which  is cogn.  with  Goth,  dis-tairan,  ‘to  tear  to  pieces’, OE.  teran,  ‘to  tear’.  See  tear,  ‘to  rend’,  and  cp. words  there  referred  to.  Cp.  also  adermia,  ec- deron,  endermic,  epidermis,  exodermis,  hypo- dermis,  leucoderma,  pachyderm,  taxidermy, xeroderma.
11990:Derivatives:  dogmatiz-ation ,  n.,  dogmatiz-er ,  n. doily,  also  doiley,  doyly,  n.,  an  ornamental  nap¬ kin.  • —  Named  after  Doily  or  Doyley,  a  London draper,  who  flourished  in  the  early  years  of  the 1 8th  cent.
12190:drab,  n.,  1)  a  kind  of  cloth  of  brownish-yellow color;  2)  a  brownish-yellow  color.  —  F.  drop, ‘cloth’,  fr.  Late  L.  drappus,  fr.  Gaulish  *drappo-. See  drape  and  cp.  drabbet.
12229:Derivatives .  dramaturg-ic,  adj.,  dramaturg-ist, n. drank,  past  tense  of  drink.  —  ME.  dranc,  fr.  OE. dranc,  fr.  drincan,  ‘to  drink’.  See  drink, drape,  tr.  v.  —  F.  draper,  ‘to  cover  with  cloth, drape',  fr.  drop,  ‘cloth’,  fr.  Late  L.  drappus, which  is  prob.  of  Gaulish  origin  and  ult.  de¬ rives  fr.  I.-E.  *1 ire-p-,  ‘to  tear  off’,  whence  also OI.  drapih,  ‘mantle,  garment’.  Lith.  drapanos (pi.),  ‘linen,  women’s  linen,  undergarment’  (the original  meaning  prob.  was  ‘a  piece  tom  off’), Gk.  SpeneiM,  ‘to  pluck’,  Russ,  drapati,  drjdpati, Pol.  drapac,  Serbo-Croat,  drapati,  ‘to  scratch, tear’.  I.-E.  *dre-p-  is  a  -p-enlargement  of  base *der-,  ‘to  flay’,  whence  Gk.  Sepsiv,  ‘to  flay’, Seppa,  ‘skin’.  See  derma  and  cp.  drab,  ‘a  kind of  cloth’,  trap,  ‘clothes’.  Cp.  also  the  first  ele¬ ment  in  drepanoid.
12230:drape,  n.  —  Partly  fr.  F.  drap,  partly  fr.  drape,  v. draper,  n.  - —  ME.,  fr.  AF.  draper,  which  cor¬ responds  to  OF.,  F.  drapier,  fr.  drap,  ‘cloth’. See  drape,  v.,  and  agential  suff.  -er. drapery,  n.  —  OF.  (=  F.)  draperie,  fr.  draper,  ‘to cover  with  cloth,  drape’.  See  drape,  v.,  and -ery.
12231:Derivative:  drapery,  tr.  v.
12257:Drepanis,  n.,  name  of  a  genus  of  birds  (zool.)  — ModL.,  fr.  Gk.  Spciravlp,  a  kind  of  bird,  prob. ‘the  swift’,  fr.  SpemxvT),  ‘sickle’;  so  called  from its  sickle-shaped  wings.  See  next  word, drepanoid,  adj.,  sickle-shaped.  —  Compounded of  Gk.  SpsTOivY),  ‘sickle,  reaping  hook’,  and -oEiSf)?,  ‘like’,  fr.  eiSop,  ‘form,  shape’.  The first  element  is  rel.  to  Sp^irstv,  ‘to  pluck’;  see drape.  The  second  element  derives  fr.  Gk.  ISop, ‘form,  shape’ ;  see  -oid.
26884:pachyderm,  n.,  a  thick-skinned  animal,  as  the elephant,  rhinoceros  and  hippopotamus.  —  F. pachyderme,  fr.  Gk.  rrayuSeppog,  ‘thick-skin¬ ned’,  which  iscompounded  of  wxxbi;,  ‘thick’,  and Sepp.a,  gen.  S^pjzaTog,  ‘skin’.  See  pachy-  and derma.
26885:pachydermatous,  adj.,  1)  thick-skinned;  2)  insen¬ sitive.  —  See  prec.  word  and  -ous. pachydermia,  n.,  abnormal  thickness  of  the  skin (med.)  —  Medical  L.,  fr.  Gk.  nayoSepiita, ‘thickness  of  the  skin’,  fr.  7taxbSepjxog,  ‘thick- skinned’.  See  pachyderm.
26886:Derivative:  pachydermi-al,  adj. pachymeningitis,  n.,  inflammation  of  the  dura mater  (med.)  —  Medical  L.,  formed  from  next word  with  suff.  -itis.
38322:taxidermy,  n.,  the  art  of  preparing,  stuffing  and mounting  the  skins  of  animals.  —  Compounded of  taxi-,  Gk.  8£pp.a,  ‘skin’,  and  suff.  -y  (repre¬ senting  Gk.  -(a).  See  derma  and  cp.  the  second element  in  pachyderm.
38347:tear,  tr.  and  intr.  v.,  to  putfapart,  rend.  —  ME. teren,  fr.  OE.  teran,  rel.  to  OS.  terian,  ‘to  con¬ sume’,  far-terian,  ‘to  destroy’,  MLG.,  MDu., Du.  teren,  ‘to  consume’,  OHG.  zeran,  fir-zeran, ‘to  destroy;  to  consume  (whence  MHG.  zern, ver-zern,  G.  zehren,  ver-zehren,  ‘to  consume’), OHG.,  MHG.,  G.  zerren,  ‘to  tear’,  Goth,  dis- tairan,  ga-tairan,  ‘to  tear,  destroy;  to  tear  to pieces’,  fr.  I.-E.  *dere-,  *der-,  ‘to  rend,  divide; to  flay’,  whence  also  OI.  drnati,  ‘cleaves,  bursts’, Gk.  SspE'.v,  ‘to  flay’,  8sp(j.a,  ‘skin’,  Sopa,  ‘skin’ Sapaii;,  ‘tearing,  flaying,  separation’,  OSlav. dero,  dlrati,  ‘to  tear,  flay’,  Lith.  dir  it,  dirti,  ‘to flay’,  Arm.  terem,  ‘I  flay’,  W.,  Co.  Bret,  darn, ‘piece’.  Cp.  also  Toch.  tsar,  ‘a  hand’,  prop,  ‘that which  tugs  or  tears’.  Cp.  derma  and  words  there referred  to.  Cp.  also  darn,  dartars,  Derris,  drab, ‘a  kind  of  cloth’,  drape,  tart,  ‘sour’,  tetter,  trap, ‘clothes’.
39913:trap,  n.,  clothes,  baggage.  —  ME.  trappe,  prob. fr.  OF.  (==  F.)  drop,  ‘cloth’.  See  drape  and  cp. trappings.
40088:tricolor,  tricolour,  n.,  a  national  flag  composed  of three  colors.  — -  F.  tricolore ,  fr.  earlier  drapeau tricolore,  ‘a  flag  of  three  colors’,  fr.  Late  L.  tri¬ color,  ‘three-colored’,  fr.  tri-  and  L.  color,  ‘color’. See  color,  n.
41004:valance,  n.,  piece  of  drapery.  —  ME.  valaunce, vallance,  prob.  fr.  Valence  in  SW.  France,  where this  material  was  made.  Cp.  Valencia  and  Valen¬ ciennes  lace.
```


## [2026-09-05T18:09:03.079Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"دول\\b\" MON_part1.txt MON_part2.txt 2>/dev/null | head -10; echo \"### BQT v2 دول\"; python3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i,p in enumerate(t):\n    if re.search(r'دول\\s*[=۔\\-]', p) or 'دول ' in p:\n        # find headword-ish\n        for m in re.finditer(r'.{0,80}دول.{0,120}', p):\n            s=m.group(0)\n            if 'دلو' in s or 'عربی' in s or 'معرب' in s:\n                print(i, i+540, repr(s))\nEOF"
}
```


### [2026-09-05T18:09:04.887Z] TOOL RESULT

```
MON_part2.txt:828:و قسمت مرکزی بنام مدولر موسوم است. 
MON_part2.txt:1212:غرعر: ۵۲۲ (اصت.) آوازی که از دولابت 
MON_part2.txt:2448:که ی در آخر کتات افزایند» جدول 
MON_part2.txt:2450:منظور اصلی از جدول مذکور ذکر کلمات و 
MON_part2.txt:2874:توانگری» بی‌نبازی» دولتمندی. 
MON_part2.txt:3428:که کودکان بدان بازی الک‌دولک کنند. 
MON_part2.txt:3436:دولک. 
MON_part2.txt:3471:سپاهیان در روز جنگ بر سر نهند؛ دولفه. 
MON_part2.txt:5193:حق. عدول از حق. (امص.) تبهکاری: فسق 
MON_part2.txt:5334:دا ها ور دولتی متحد در ا نند. 
### BQT v2 دول
360 900 ' \u202bکه وخربطه که\u200cبرمیانندند دولمیان خوانند\u202c                   \u202bدوك و گروهةٌ ریسمان و پنبه گذارند » وبعربی\u202c'
360 900 '    \u202bدول \u202a ۳\u202cآب» معرب آن هم دولاب\u202c              \u202bاز ِ\u202c     \u202b\u202a۹\u202c\u202c          \u202b\u202a3\u202c\u202c   \u202bدولت\u202c   \u202bرك\u202a:\u202c\u202c     \u202b\u202a۹\u202c\u202c        \u202b\u202a. 6 ۲ : 4۸۸\u202c\u202c'
558 1098 '                   \u202bفرخنگه رشدی دز آمده \u202a « :\u202cستاره بمعنی مسطر جدول سطاره است\u200cبطا وعربی است\u202c'
```


## [2026-09-05T18:09:08.502Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[360])\nEOF"
}
```


### [2026-09-05T18:09:10.491Z] TOOL RESULT

```
  ‫‪ ۵‬ات‬   ‫تن‬
                                                                                                    ‫د وگاله‬


 ‫دول = بانالیمجهول بروزن غول د؛لو‬                        ‫دگوافه ‪ ۱‬ه باخفای ثانیوکاف فارسی‬
 ‫آبکتی رگاویند‪ - 9‬و برح دلو را گیفزته‌اند‬                ‫بند و صف آن يك‬ ‫پروزن فلانه ‪ ,‬عدد دگوورا‬
  ‫که بر جحبازدهم باشد ازدوازده بروج فلکی ‪1‬‬                ‫لماز همست ٍِ‪.‬‬  ‫ت‬‫کدو ر‬‫به از‬    ‫او‬‫کتن‪-‬‬‫اس‬
 ‫ویمعتی مکار ومحیل وشطاح ‪ -‬وبی‌حیا ‪ -‬وسفله‬
 ‫هم هت ‪ ۷‬و‪-‬دولآمارا نگیوزبند‪ , ۸‬و آن‬                     ‫گواو مره بکسر واو دوبم ک؛نایه‬
                                                                                     ‫د‬
                                                          ‫واوزمین را بز‬
                                                                      ‫ازشب وروز باشد ‪ -‬وبرج ور ک‬
‫ظرقی باشد مربع و مخروطی شکل که آبرا از‬
                                                                                                    ‫تفا‬         ‫کو‬
 ‫چوب سازند و در مر کز مخروطی آن سوراخی‬
 ‫کنند ومحاذی سوراخ سنگه آسیا نصب نمایند‬                  ‫«کنایه‌از آسمان‌وزمین‬     ‫دو گاهو اره‬
‫و پراز غلهسازند ‪ -‬و تیرکشتی را لفیزته اند‬                                                                 ‫‪.‬‬     ‫ات‬
 ‫وآن چوب بلندی باشد کهدر وسط کشتی بپرای‬
 ‫کنند ‪ -‬وبه‌عنی که وخربطه همآمده است‌چه‬                   ‫را کوبند که در آن‬            ‫کی‬
                                                                                        ‫چسبد‬
                                                                                           ‫و و‬
                                                                                             ‫کوقجه‬
                                                                                                 ‫صند‬
 ‫که وخربطه که‌برمیانندند دولمیان خوانند‬                   ‫دوك و گروهةٌ ریسمان و پنبه گذارند » وبعربی‬
 ‫وتح ثالی » پوست بيخ درخت‬
                        ‫و چم اول ف‬                                ‫حفش خوالند وجمع آن احفاش است ‪.‬‬
 ‫زبتون هندی است ‪ -‬و در عریی جمع دولت‬                      ‫دی را ګوبند که‬
                                                                       ‫دوك ردیهوک‬
                             ‫باشد ‪٩‬‏ ‪.‬‬                       ‫وطتاب خیمه وامثال آن تابند‬         ‫يدان رسمان‬

 ‫ات وشرابرا‬      ‫بالام "لف ؛ سو‬   ‫دولا ت‬

                                       ‫فة‬      ‫کو‬        ‫دکوله دار ب=ضم کاف وظهور ها‪.‬‬
 ‫دولاب د بر وزن دوشاب » یممنی‬                             ‫کنایه آافزتاب وماه ‪ -‬وروز وشب ‪ -‬ودویادشاه‬
 ‫چرخ وآ نچه‌درسیر ودورباشد‪ -‬ومخزن و گنجينهة‬                                                      ‫چبار باشد ‪.‬‬
 ‫کوچت رالیز گوبند ‪ -‬وسودا ومعامله ودادوستد‬                ‫‪ -‬کنابه اززمابرفتنه‬          ‫دشومگوال‬
 ‫بان را دولابی‬   ‫بافراط راتیز گفته اند ‪ ۰‬ومشوب‬
                                                          ‫و طلم واءام فقر و فاقه و افتادن بحادئة عظدمی‬
                                        ‫گونتد ‪.‬‬                                                               ‫باشد ‪.‬‬

  ‫دولاب هینا = کنایه از آسان‬                             ‫دو گوشی ‪ = ۴‬کلاهی راکوبند که‬
                                                          ‫دکووش داشته باشد از دوطرف چنااکه کرشهارا‬
  ‫دو لابه= بروزن رودابه» بممئی‌دولاب‬                      ‫سوبو کووزه را لگیوزبندکه دو‬
 ‫است که چرخآ بکشی‪ -‬کونجینه ومخزن کوچك‬                                                    ‫دسته داشته باشد ‪.‬‬

                                            ‫باشد ‪.‬‬         ‫دو گو هر = کنابه ازهقل‌وروح‌است‪.‬‬

   ‫‪« 6 -‬یب رک ‪۸‬ه“ ‪.‬‬               ‫کاله (یوند اعاف وست) ؛پبلوی ‪4‬‬                     ‫‪ - ۱‬از ‪ :‬دو‬
   ‫‪ -‬دان (یسوندمکان وظر فت) ‪۰‬‬      ‫از ‪ :‬دوك‬   ‫‪> ۳‬‬           ‫؟ ‏ مخصوصاً لماز صبح را گویند ‪.‬‬
   ‫© = رلو (عر) = سربانی ‪ 310121‬د اسفا ‪:۱‬‬                     ‫‪ - ۴‬از ‪ :‬دو کوش ی(سبت)‪.‬‬
    ‫‪ - ۷‬نیز بمە‌نیآلت‬       ‫=ور (خوارزمی) = دلو(عر) گداه شماری ‪. » ۳۰۲‬‬
                                                                     ‫‪ ۱‬د‬                         ‫‪‎‬ص‪. ٩۵ ۲‬‬

   ‫کویند مکی نژار» ‪:‬‬     ‫تناسل مرد » طبری دول «صاب طدری‪ »۸۹۳‬و در اراك (ساطان] باد) هم ال‬
                                                                 ‫حاننکر‬                     ‫‪-‬‬   ‫‪۸‬‬
   ‫ت = ‪lud‬‏ ( چرخدن » دور زدن ‪ ۰‬جنباددن ‪ ¢‬بالا آوردن ) » وبليامز‬

    ‫دول ‪ ۳‬آب» معرب آن هم دولاب‬              ‫از ِ‬     ‫‪۹‬‬          ‫‪3‬‬   ‫دولت‬   ‫رك‪:‬‬     ‫‪۹‬‬        ‫‪. 6 ۲ : 4۸۸‬‬

                                                                                 ‫‪ ۶‬دزی ج ‪ ۱‬ص‪. ۲: ۷4 ۷‬‬
```


## [2026-09-05T18:09:31.731Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### HRN nestar\"; grep -n -i \"nester\\|nistar\\|neätar\\|nestar\\|niStar\" HRN.txt | head; echo \"### HUB\"; grep -n -i \"nestar\\|nistar\" HUB.txt | head; echo \"### NYB\"; grep -n -i \"darr\\|drafs\\|drod\\|drud\\|dard\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-05T18:09:31.814Z] TOOL RESULT

```
### HRN nestar
9218:nester 'Lanzette'.
### HUB
3666:animal, puncture, lancet'; nastar und nestar a lancet' ;
3668:voraussetzt). Np. nestar bei Fird. I, 46, 214.
8421:tasta- ; neS 'Spitze, Stachel', nestar *Lanzette*, skr. neksana- ;
### NYB
1202:darrak [drky] ravine, or rock HajB: 7. 13, Prth. equivalent vēm (q. v.). - NP darrah ‘a valley between hills. V. Nyberg, Christensen Vol., p. 69.
1203:dart [dlt'] pain, illness 43?3. 5415, 8620, 905, — MPrthPrs drd, Paz. NP dard.
1349:dritan [SDKWN-tn'] drin- [SSDKWN-] to tear to pieces, to slit 502. 1027-8 (v.s. v. daštan). — Av. (689) !dar-, pres. darand- (Skr middle droite). Reading according to FrP 18; BP also darritan darr- = NP dar(r)idan dar(r)-.
1434:én [inser., Ps. ZNH, but already in the inser. the z is often stunted; BP ZNH] dem. pron. this here, always referring to the present situation, that of the speaker, or to what is to follow; no pl.: api-n pad pat én darrak% nihat api-n tigr tar han citak be apakand we set our foot on this rock here and shot the arrow beyond that cairn yonder HajB:6-8; én damik this earth, our earth; én dam, én dam u dahisn, en getäh this world; én apécak vēh-dēn íi mäzdesnän this pure good religion of the Mazdayasnians 84? eto.; always én dén this (our) religion, of the Mazdaism; pat én apēgumān būtan ku to entertain no doubt about the fact that 634 etc.; vicčirišn ... en kū the explan- ation is this that 121"; — én i forms an elliptic gen.: frdc én % man yaz perform what here is mine (my duty, the rite incumbent on me on this occasion) 535; én būt i 6 peš gobam this happened which I am now going to tell 54!?; — én and, v. and. — Skr ena-; not in Av. and OP; SW w.: MPrs. ‘yn (no pl, instead im&sän, imin are used); Paz. NP in. Tedesco, Dial. 216.
2135:ka [MT], with encl. ’MT-m = ’MT-t = ka-t, °MT-š = ka-š ete.: 'MT-e = ka-c: A. conj. when, as, while; because; though, whilst; if; that. 1. temporal: standard type of period referring to the past: Pāpak ka-š hàn saxtan āšnūt kas fréstit by P. when by him this word was heard a man was sent = when P. heard this he sent a man 21!; passim; if con- taining an encl. pron. the apodosis is introduced a) by adak + encl., e. g. api-n ka én tigr vist adak-in . . . vist and when We shot this arrow, We shot it ... HajB: 4-6; 545-5; — b) by api- + encl., e. g. ka hac star frac būt api-š ... guft kū then he said 60?*; — c) by the independent forms of the enclitics: am, at, aš, aman, atān, ašān: hän étén amavandeh + ka zivandak bit hom am bit that great vigour which was mine when I was alive 345-6; ka giyāk-ē päh i gospandan vēnēnd ašān avd sahét when they see somewhere a flock of sheep it will seem astonishing to them 9724-25; — the apodosis may be introduced by adak alone (v. this w.); by pas (914-*); by andar han in the meantime (561°); — ka ... apāc àyet aš Kat-Xosroi bē 6 patirak āyēt ka pat vài našast ēstēt when he comes back he will
2710:darraky — to put one’s feet on the rock HajB:6-7.12-13; tigr andar kamān ~ to put the arrow to the bow (-string) 100%; catrang ~ to arrange a game of chess 11914.20.21. gartänäk be ~ to cast the dice 1202122; pat ... ~ to deposit in... 10719, 11312; apar ~ to put (wood) on (the fire) 95°; dast apar ~ to put one's hand (to work) 6215; bé ~ to deposit 4216, to take off (a garment) 5717; — nam m to give a name, to name 1025-36, 11421, 11623; pat nām i ... ~ to name after 1201-2; mēnišn ~ 6 to ponder on 5?2-?3, — Av. (721 sq.) ni-dä-; MPrs nh’dn, nyh?dg, Verbum 194; Ps. nyd?t; Paz. nahādan; NP nihādan; only SW.
3001:2pat[PWN; Prth. inser. pty] A. prep.; not governing encl. pronouns (in pat-šān dra- sanéh 10974 the enel. belongs to the follow- ing subst.). I. in a concrete sense: 1. local: in, on, upon, at; (to pass) over (a bridge), through (a passage); (to remain, dwell) with a p.; passim; 'pn LGLH PWN ZNH drky HNHTWN = api-n päd pat én darraky nihāt HajB: 6-7. (12-13), Prth NGRYN pty ZK wym HQ’YMW-t HajA: 6—7. (11-12); PWN ZK Psy ZY ... = pat hàn rah" 1... on the road to... P1:4. — 2. time: pat ham Sap 16°; pat- vastak hamë pat sap ka 5!; sap 1 sitikar pat usbam 1012-8 ; pat ul vaxšišneh inazdeh
4090:vem  (Prth) [wym] rock HajA:6.11 (= Prs darrak). — Av. (1836) vačma-; Arm. lw. vem; MPrs (1) wym (S).
4240:vitartan [wtltn'], viturtan [wtwltn'], vi- taštan [wtštn'], vitir- [wtyl-] to pass: andar dašt bē vitart passed over the plain 318; pat kustak + deh vitart passed outside the village 619-17; to pass by 7!1.15.22; bē vitast drove ahead 71’; to cross a bridge 7225.27; to go through a stream 101%. 10323; kë vitīrēndv the passers-by 12815; — pt. vitart, viturt deceased: vitart coll. the deceased 837. 8413; viturtān martūmān 10517. — Av. (640) vi-tar- = OP; MPrth w(y)drdn w(y)dr- (S, MHC); MPrs pres. wdyr- (S); Ps. pt. wilty, pres. wtyl-, wtl-; Paz. vadardan vadirdan, pres. vadar-, va- der-, vadir-; NP guöastan guóar-. Verbum 206, Ghilain 57.
5606:drfs: drafs
6529:dar: ~ d(a)raxt: draxt dard: dart
6534:draž: ~ drenžešn: dranjišn drud: drot
6838:vadardan: vitartan
7098:darridan, darr-: dritan
7099:darrah: darrak
```


## [2026-09-05T18:09:42.313Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^drafs\\|drafs \\[\" NYB_vol2_glossary.txt | head; grep -n \"drōt\\|drot \\[\" NYB_vol2_glossary.txt | head"
}
```


### [2026-09-05T18:09:42.374Z] TOOL RESULT

```
1351:drot [dlwt'; SRM] benediction (in salu- tations, etc.), welfare, prosperity 14°. 1710, 1918, 12129; ~ 6 ruvän dätan to say farewell to one's life, to die 293-1. — < Olr *druvatüs, nom. of Av. (782 sq.) drvatčit-; MPrthPrs drwd; Paz. drüd; NP durud.
```


## [2026-09-05T18:09:50.099Z] TOOL CALL #42: Bash

```json
{
 "command": "sed -n '1,40p' tools/fetch_source.py"
}
```


### [2026-09-05T18:09:50.148Z] TOOL RESULT

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


## [2026-09-05T18:09:54.637Z] TOOL CALL #43: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/der-\" \\\n \"https://en.wiktionary.org/wiki/دریدن\" \\\n \"https://en.wiktionary.org/wiki/درفش\" \\\n \"https://en.wiktionary.org/wiki/دره\" \\\n \"https://en.wiktionary.org/wiki/درد\" \\\n \"https://en.wiktionary.org/wiki/درودن\" \\\n \"https://www.etymonline.com/word/drape\" \\\n \"https://www.etymonline.com/word/tear\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 119, roots Der 1 / Drep: verification of Nourai's chart\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-05T18:10:00.141Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/a5705981f1b1cc3d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/500ca1a9773183b5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e88a31773bae6a1b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1fc4bf29ab2e1f21.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/425cc300d277326c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cd87c430605e5bea.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2d48dc03c75d342b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2d9a52ce95203851.txt
```


## [2026-09-05T18:10:03.001Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 500ca1a9773183b5 e88a31773bae6a1b 1fc4bf29ab2e1f21 425cc300d277326c cd87c430605e5bea; do echo \"############ $f\"; sed -n '1,10p' $f.txt; echo \"...\"; grep -n -A12 -i \"Etymology\" $f.txt | head -60; done"
}
```


### [2026-09-05T18:10:04.574Z] TOOL RESULT

```
############ 500ca1a9773183b5
URL: https://en.wiktionary.org/wiki/دریدن
FETCHED: 2026-09-05T18:09:56Z
STATUS: 200
TITLE: دریدن - Wiktionary, the free dictionary

دریدن - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 
...
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
--
145: Etymology
146- [ edit ] 
147-
148- From Middle Persian [Book Pahlavi needed] ( SDKWN-tn', dl-ytn' /⁠darridan, darr-⁠/ , “ to split, to tear ” ) , [ 1 ] Northern Luri دڕنیێ ( derrnyı , “ to split ” ) from Proto-Indo-Iranian *dar- , ultimately from Proto-Indo-European *der- ( “ to tear, split ” ) . Cognate with English tear and Ancient Greek δέρω ( dérō , “ I skin, I flay ” ) .
149-
150- Pronunciation
151- [ edit ] 
152-
153- ( Classical Persian ) IPA ( key ) : /da.riː.ˈdan/ 
154-
155- ( Dari, formal ) IPA ( key ) : [d̪ä.ɾiː.d̪än] 
156-
157- ( Dari, formal ) IPA ( key ) : [d̪ä.ɾiː.d̪än] 
############ e88a31773bae6a1b
URL: https://en.wiktionary.org/wiki/درفش
FETCHED: 2026-09-05T18:09:58Z
STATUS: 200
TITLE: درفش - Wiktionary, the free dictionary

درفش - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 
...
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Descendants 
72-
73- 1.3.2 
74- References 
--
82: Etymology 
83-
84- 2.2 
85- Pronunciation 
86-
87- 2.3 
88- Noun 
89-
90- 2.4 
91- Adjective 
92-
93- 2.4.1 
94- Derived terms 
--
168: Etymology
169- [ edit ] 
170-
171- Inherited from Middle Persian [Book Pahlavi needed] ( dlpš /⁠drafš⁠/ , “ banner ” ) , perhaps from a hypothetical Proto-Iranian *drafš- ( “ to "behave" like a banner, fly up, shine, tremble ” ) , perhaps from Proto-Indo-European *drep- ( “ to cut, tear off (a piece) ” ) . Cognate with Parthian 𐫅𐫡𐫜𐫢 ( drfš /⁠drafš⁠/ ) , Northern Luri درڢش ( derwş ) , Avestan 𐬛𐬭𐬀𐬟𐬱𐬀- ( drafša- ) , Sogdian [script needed] ( ʾrδʾšp ) , Sanskrit द्रप्स ( drapsá ) ; outside Indo-Iranian, compare in particular Late Latin drappus ( “ piece of cloth ” ) . Akin to the borrowings: Old Armenian դրաւշ ( drawš ) , Old Georgian დროშაჲ ( drošay ) , დრაუჟი ( drauži ) , Ossetian тырыса ( tyrysa ) , туруса ( turusa ) , Classical Syriac ܕܪܦܫܐ ( drap̄šā ) .
172-
173- Pronunciation
174- [ edit ] 
175-
176- ( Classical Persian ) IPA ( key ) : /di.ˈrafʃ/ , /da.ˈrafʃ/ 
177-
178- ( Dari, formal ) IPA ( key ) : [d̪ɪ.ɾäfʃ] , [d̪ä.ɾäfʃ] 
179-
180- ( Dari, formal ) IPA ( key ) : [d̪ɪ.ɾäfʃ] , [d̪ä.ɾäfʃ] 
--
241: Etymology
242- [ edit ] 
243-
244- From Classical Persian درفش ( dirafš , “ standard; banner ” ) .
245-
246- Pronunciation
247- [ edit ] 
248-
249- ( Standard Urdu ) IPA ( key ) : /d̪ʊ.ɾəfʃ/ , /d̪ə.ɾəfʃ/ , /d̪ɪ.ɾəfʃ/ 
250-
251- Noun
252- [ edit ] 
253-
############ 1fc4bf29ab2e1f21
URL: https://en.wiktionary.org/wiki/دره
FETCHED: 2026-09-05T18:09:58Z
STATUS: 200
TITLE: دره - Wiktionary, the free dictionary

دره - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 
...
73: Etymology 1 
74-
75- 2.1.1 
76- Noun 
77-
78- 2.1.1.1 
79- Derived terms 
80-
81- 2.1.1.2 
82- Descendants 
83-
84- 2.1.2 
85- Further reading 
--
88: Etymology 2 
89-
90- 2.2.1 
91- Noun 
92-
93- 2.2.1.1 
94- Descendants 
95-
96- 2.2.2 
97- Further reading 
98-
99- 3 
100- Pashto 
--
116: Etymology 
117-
118- 4.2 
119- Pronunciation 
120-
121- 4.3 
122- Noun 
123-
124- 4.3.1 
125- Descendants 
126-
127- 4.4 
128- References 
--
329: Etymology 1
330- [ edit ] 
331-
332- Borrowed from Classical Persian دَرَه ( dara , “ valley; crack, fissure ” ) .
333-
334- Noun
335- [ edit ] 
336-
337- دره • ( dere ) 
338-
339- valley , dale , vale 
340- Synonym: وادی ( vadi ) 
341-
--
384: Etymology 2
385- [ edit ] 
386-
387- Borrowed from Arabic دُرَّة ( durra , “ single pearl ” ) . 
############ 425cc300d277326c
URL: https://en.wiktionary.org/wiki/درد
FETCHED: 2026-09-05T18:09:59Z
STATUS: 200
TITLE: درد - Wiktionary, the free dictionary

درد - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 
...
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 1.2.1 
68- Derived terms 
69-
70- 1.2.2 
71- Descendants 
72-
73- 1.3 
74- Further reading 
--
82: Etymology 1 
83-
84- 2.1.1 
85- Pronunciation 
86-
87- 2.1.2 
88- Noun 
89-
90- 2.1.2.1 
91- Derived terms 
92-
93- 2.1.2.2 
94- Descendants 
--
100: Etymology 2 
101-
102- 2.2.1 
103- Alternative forms 
104-
105- 2.2.2 
106- Pronunciation 
107-
108- 2.2.3 
109- Noun 
110-
111- 2.2.3.1 
112- Descendants 
--
126: Etymology 
127-
128- 3.2 
129- Pronunciation 
130-
131- 3.3 
132- Noun 
133-
134- 3.3.1 
135- Declension 
136-
137- 3.4 
138- Further reading 
--
227: Etymology
228- [ edit ] 
229-
230- From Persian درد ( dard ) .
############ cd87c430605e5bea
URL: https://en.wiktionary.org/wiki/درودن
FETCHED: 2026-09-05T18:09:59Z
STATUS: 200
TITLE: درودن - Wiktionary, the free dictionary

درودن - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 
...
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
73- 1.4 
74- Further reading 
--
140: Etymology
141- [ edit ] 
142-
143- From Middle Persian [script needed] ( HCDLWN-tn' /⁠drūdan⁠/ , “ to reap; to mow ” ) .
144-
145- Pronunciation
146- [ edit ] 
147-
148- ( Classical Persian ) IPA ( key ) : /du.ruː.ˈdan/ 
149-
150- ( Dari, formal ) IPA ( key ) : [d̪ʊ.ɾuː.d̪án] 
151-
152- ( Dari, formal ) IPA ( key ) : [d̪ʊ.ɾuː.d̪án]
```


## [2026-09-05T18:10:10.330Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"##### دره Persian section\"; sed -n '/^ Persian *$/,/^ Turkish/p' 1fc4bf29ab2e1f21.txt | head -80; echo \"##### درد Persian\"; sed -n '150,230p' 425cc300d277326c.txt"
}
```


### [2026-09-05T18:10:12.049Z] TOOL RESULT

```
##### دره Persian section
 Persian 

 Toggle Persian subsection 

 4.1 
 Etymology 

 4.2 
 Pronunciation 

 4.3 
 Noun 

 4.3.1 
 Descendants 

 4.4 
 References 

 Toggle the table of contents 

 دره 

 13 languages 

 فارسی 
 Français 
 Hrvatski 
 ಕನ್ನಡ 
 한국어 
 Kurdî 
 Lietuvių 
 Malagasy 
 پښتو 
 Русский 
 Тоҷикӣ 
 Türkçe 
 中文 

 Entry 

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
 Cite this page 
 Get shortened URL 

 Print/export

 Create a book 
 Download as PDF 
##### درد Persian
 Français 
 Hrvatski 
 Magyar 
 Bahasa Indonesia 
 日本語 
 한국어 
 Kurdî 
 Malagasy 
 Norsk bokmål 
 Polski 
 پنجابی 
 پښتو 
 Português 
 Русский 
 سرائیکی 
 Slovenščina 
 Shqip 
 Türkçe 
 中文 

 Entry 

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

 See also: دزد 

 Ottoman Turkish
 [ edit ] 

 Etymology
 [ edit ] 

 From Persian درد ( dard ) .
```


## [2026-09-05T18:10:15.567Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### دره: Persian etym body\"; grep -n \"Middle Persian\\|Proto-Iranian\\|Proto-Indo\\|darrag\\|Hasandust\\|valley\" 1fc4bf29ab2e1f21.txt | head -20; echo; echo \"### درد: Persian etym body\"; grep -n \"Middle Persian\\|Proto-Iranian\\|Proto-Indo\\|Hasandust\" 425cc300d277326c.txt | head -20"
}
```


### [2026-09-05T18:10:15.641Z] TOOL RESULT

```
### دره: Persian etym body
212: Arabic spelling of dara , dərə ( “ valley , canyon ” ) 
332: Borrowed from Classical Persian دَرَه ( dara , “ valley; crack, fissure ” ) .
339: valley , dale , vale 
351: بورغاج دره ( burgac dere , “ sinuous valley ” ) 
424: valley 
441: Uncertain, possibly from Proto-Indo-European *der- ( “ to tear, split ” ) or *dʰel(h₂)- ("valley"), the existence of which is uncertain, see Proto-Germanic *dalą for more. Cognate with Avestan 𐬛𐬀𐬭𐬈𐬥𐬁 ( darenā ) and Sogdian 𐫔‎𐫡 ( δar- ) .
484: valley 

### درد: Persian etym body
272: From Middle Persian dlt' ( dard , “ pain ” ) , from Proto-Iranian *dar-ta- ( “ torn, burning, pain ” ) , [ 1 ] from Proto-Iranian *darH- ( “ to have pain ” ) , from either Proto-Indo-European *der- ( “ to tear, split ” ) or Proto-Indo-European *delh₁- ( “ to split, suffer, be in pain ” ) , the latter which Cheung considers to be related to the former. [ 2 ] [ 3 ] See also دریدن ( daridan , “ to ravage, attack ” ) .
405: From Proto-Iranian *dr̥ti- ( “ manure, feces ” ) , from Proto-Indo-European *dʰṛ-to- , from Proto-Indo-European *dʰreyd- ( “ to have diarrhea ” ) , whence also English dirt , Old Norse dríta ( “ to defecate ” ) , and Russian дриста́ть ( dristátʹ , “ to shart ” ) . Possibly related to Proto-Indo-European *dʰerh₃- ( “ to spring, leap ” ) (whence perhaps Sanskrit धारा ( dhārā , “ current, torrent ” ) ). [ 1 ] 
497: Borrowed from Classical Persian درد ( dard ) , from Middle Persian dlt' ( dard , “ pain ” ) .
567: Persian terms inherited from Middle Persian 
568: Persian terms derived from Middle Persian 
569: Persian terms inherited from Proto-Iranian 
570: Persian terms derived from Proto-Iranian 
571: Persian terms derived from Proto-Indo-European 
578: Persian terms inherited from Proto-Indo-European 
583: Urdu terms derived from Middle Persian
```


## [2026-09-05T18:10:25.007Z] TOOL CALL #47: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/دول\" \\\n \"https://en.wiktionary.org/wiki/دلو\" \\\n \"https://en.wiktionary.org/wiki/نشتر\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 119: Persian dul (node 6, Arabic dalw?) and neštar (node 3)\" 2>&1 | tail -1\ndone"
}
```


### [2026-09-05T18:10:28.133Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/506fa1c30a4e210d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d22e349d6d3dc8bb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cc1156343776cce9.txt
```


## [2026-09-05T18:10:31.277Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 506fa1c30a4e210d d22e349d6d3dc8bb cc1156343776cce9; do echo \"##### $f\"; grep -n -i \"^ From\\|Borrowed from\\|Inherited\\|Etymology$\" -A3 $f.txt | grep -v \"^--$\" | sed -n '1,40p'; done"
}
```


### [2026-09-05T18:10:33.141Z] TOOL RESULT

```
##### 506fa1c30a4e210d
281: From Wiktionary, the free dictionary
282-
283- See also: Appendix:Arabic roots/د و ل 
284-
812: > Turkish: düvel ( inherited ) 
813-
814- Etymology 3
815- [ edit ] 
821: Borrowed from English dhole .
822-
823- Alternative forms
824- [ edit ] 
1014: Etymology
1015- [ edit ] 
1016-
1017: From Arabic أولاءِ ( ʔulāʔi ) , plural of ذَا ( ḏā ) , apparently with ḏa- prefixed by analogy with the singular forms (thus *ḏaʾulāʾi > *ḏawla > dōla ). Compare the same in several other dialects.
1018-
1019- Pronunciation
1020- [ edit ] 
1044: From Proto-Common Turkic *töl .
1045-Compare Azerbaijani döl ( “ fetus ” ) .
1046-
1047- Noun
1077: From Arabic دُوَل ( duwal ) , plural of دَوْلَة ( dawla , “ state ” ) . Arabic plural of دولت ( devlet ) .
1078-
1079- Noun
1080- [ edit ] 
1089: > Turkish: düvel ( inherited ) 
1090-
1091- References
1092- [ edit ] 
1104: From Middle Persian [script needed] ( dōl , “ bucket; Aquarius ” ) of Semitic origin, compare Arabic دلو ( dalw ) , Classical Syriac ܕܰܘܠܳܐ ( dawlā ) (absolute form ܕܘܿܠ ( dōl ) ), Akkadian 𒁕𒇻 ( /⁠dalū, dūlu⁠/ , “ bucket ” ) . Akin to Old Armenian դոյլ ( doyl ) .
1105-
1106- Pronunciation
1107- [ edit ] 
1179: Borrowed from Arabic دُوَل ( duwal ) .
1180-
1181- Pronunciation
1182- [ edit ] 
1227: From child speak; compare English doo .
##### d22e349d6d3dc8bb
250: From Wiktionary, the free dictionary
251-
252- Arabic
253- [ edit ] 
270: From Proto-Semitic . Compare Akkadian 𒁕𒇻 ( /⁠dalū, dūlu⁠/ , “ bucket ” ) , Aramaic דול ( daul , “ bucket ” ) , Classical Syriac ܕܰܘܠܳܐ ( dawlā , “ pail, bucket ” ) , Hebrew דְּלִי ( dəlī , “ pail, bucket ” ) , as well as the loanwords from Semitic Old Armenian դոյլ ( doyl ) and Persian دول ( dul , “ bucket ” ) .
271-
272- Pronunciation
273- [ edit ] 
553: Inherited from Proto-Turkic *tēlbe .
554-
555- cognates
556-
618: From دلـ ( dile- , “ to wish ” ) +‎ ـو ( -ü ) .
619-
620- Alternative forms
621- [ edit ] 
640: Etymology
641- [ edit ] 
642-
643: Borrowed from Arabic دَلْو ( dalw , “ pail, bucket ” ) .
644-
645- Noun
646- [ edit ] 
677: Etymology
678- [ edit ] 
679-
680: Borrowed from Arabic دَلْو ( dalw ) .
681-
682- Pronunciation
683- [ edit ] 
779: Arabic terms inherited from Proto-Semitic 
780- Arabic terms derived from Proto-Semitic 
781- Arabic 1-syllable words 
782- Arabic terms with IPA pronunciation 
795: Old Anatolian Turkish terms inherited from Proto-Turkic 
796- Old Anatolian Turkish terms derived from Proto-Turkic 
797- Old Anatolian Turkish lemmas 
798- Old Anatolian Turkish adjectives 
801: Ottoman Turkish terms borrowed from Arabic 
802- Ottoman Turkish terms derived from Arabic 
##### cc1156343776cce9
133: From Wiktionary, the free dictionary
134-
135- Arabic
136- [ edit ]
```


## [2026-09-05T18:10:39.720Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -B2 -A6 \"Persian\" cc1156343776cce9.txt | sed -n '1,80p'"
}
```


### [2026-09-05T18:10:39.774Z] TOOL RESULT

```
63-
64- 2 
65: Persian 
66-
67: Toggle Persian subsection 
68-
69- 2.1 
70- Noun 
71-
72- Toggle the table of contents 
73-
--
145- نُشْتَرَ ( nuštara ) /nuʃ.ta.ra/ : first-person plural non-past passive jussive of اِشْتَرَى ( ištarā ) 
146-
147: Persian
148- [ edit ] 
149-
150- Noun
151- [ edit ] 
152-
153- نشتر • ( neštar ) 
--
159- Categories : Arabic non-lemma forms 
160- Arabic verb forms 
161: Persian lemmas 
162: Persian nouns 
163-
164- Hidden categories: Pages with entries 
165- Pages with 2 entries 
166-
167- This page was last edited on 8 September 2024, at 00:37.
168-
```


## [2026-09-05T18:10:46.274Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9210,9225p' HRN.txt; echo \"==== HUB 3660-3672\"; sed -n '3655,3672p' HUB.txt; echo \"==== HUB 8415-8425\"; sed -n '8415,8425p' HUB.txt"
}
```


### [2026-09-05T18:10:46.353Z] TOOL RESULT

```
Mel. asiat. IX, 241); phlv. mc (AV.?), päz. nfz.
Das Wort heisst aber nlz (nicht uez), es reimt
auf äz; ebenso hemz, das die Wörterbücher fälsch-
lich mit B sprechen lassen.
1066. ne»t *ist nicht*, vest^^),
päz. nestj nesU,
ap. naiy + asti,
1067. neS 'Spitze, Stachel; Gift (AM. S. 10 Zeile 5 v. u.)',
nester 'Lanzette'.
ai. vergl. neksana- spitzer Stab, Spiess', zu [/'neks-,
niksati 'durchbohren' (Hörn).
1068. nek 'schön, gut', nekö, nekt, new 'wacker, Held'
(Sahn, I, 416 Vers 555, HI, 1106 Vers 707, von einer
Frau).
*) Wenn phlv. n{i)käm^ vd. 7 f 192) Gl , wirklich 'matrice' bedeutet
— was ich bezweifle - so müsstc es nCOgüm gelesen werden, um mit
==== HUB 3660-3672
'Stengel* = skr. nadd- 'Schilf, Schilfrohr = arisch
"^narda- (Geiger, Etym. und Lautl. des Afgh. Nr. 140).
*) Vgl. arm. hrauer *Einladung* = zd. frava^Sa^ ; arm. paiu&r
*Befehl' = zd. *paitivae3a' (jpaitiva^Say^mi *ioh kUndige an*) nach
Fr. Miiller, WZKM. 7, 371.— 104 -
1062. Lies afgh. nllkq (Raverty nlkceh) und ap. apanyaka-.
1064. Im Paz. stets ntro (Min. und Shk.) geschrieben !
1065. Die Etymologie ist lautlieh unmoglich. Nur ein
urspr. ^aniddid wiirde direct zu np. nl^ fiihren. Vgl.
oben Nr. 457 und Fr. M tiller, WZKM. 5, 67.
1067. Dazu afgh. LW. nes 'the sting of any venomous
animal, puncture, lancet'; nastar und nestar a lancet' ;
arm. LW. n§iirj nstrak Xanzette' (das ein phi. *mstir
voraussetzt). Np. nestar bei Fird. I, 46, 214.
1069. Ist nt/m zu sprechen, vgl. paz. n^m, afgh. LW. nlm,
Hier fehlt np. nlmroz 'Mittag' und n%ma *Halfte' = bal.
nemag 'Richtung, Seite*, phi. nBmak part, direction
etc. Gl. and Ind. 251, afgh. nBmai 'a half.
==== HUB 8415-8425
selbstandigem pasu- (idg. pek^u-).
M Vgl. tran»oxanisch ixseS bei N o 1 d e k e , mand. Gram. Einl. p.l3.— 236 —
§ 129. Idg. kh = iran. ap. s = np. s:
kas 'AchselhQhle' = zd. kasa-, skr. kaksa-: sas *sechs'
zd. xsvaSf idg. svek^s ; s^wa *Kamm* = gr. xra^ ; ^'^^
*Beir = zd. ^cisa-, arm. tasem 'behaue'; tast 'Becken' = zd.
tasta- ; neS 'Spitze, Stachel', nestar *Lanzette*, skr. neksana- ;
casm 'Auge* = zd. dasman-, skr. caksus ; arm. LW. sahapet
'Schutzgeist* (5. Jhd.) = zd. soid-rapaiti- ; sen *Dorf * =
zd. -say ana, Wrzl. k^si wohnen'.
Dazu auch as 'Bruhe' H. 29, Osam *Trank' H. 30,
```


## [2026-09-05T18:11:06.255Z] TOOL CALL #51: Bash

```json
{
 "command": "ls site/pages/119.jpg 2>/dev/null; pdftoppm -f 119 -l 119 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg119 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-05T18:11:08.952Z] TOOL RESULT

```
site/pages/119.jpg
total 34900
drwx------ 2 sfmqrb sfmqrb     4096 Sep  5 14:11 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb    48417 Sep  5 10:19 build93.py
-rw-rw-r-- 1 sfmqrb sfmqrb    59425 Sep  5 10:54 build98.py
-rw-rw-r-- 1 sfmqrb sfmqrb     4811 Sep  5 02:00 bulca.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2950 Sep  5 10:15 c_anth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2661 Sep  5 10:15 c_armonica.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5133 Sep  5 14:10 c_avestan120.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22149 Sep  5 01:51 c_belloth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9603 Sep  5 10:50 c_byz2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11328 Sep  5 10:49 c_byz_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    18289 Sep  5 13:48 c_fr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13620 Sep  5 13:48 c_germ2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10949 Sep  5 13:48 c_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3138 Sep  5 10:50 c_heb1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4953 Sep  5 10:50 c_heb2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    15141 Sep  5 13:51 c_hektaton.png
-rw-rw-r-- 1 sfmqrb sfmqrb      914 Sep  5 11:04 chicane.html
-rw-rw-r-- 1 sfmqrb sfmqrb    18737 Sep  5 13:51 c_kent.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10687 Sep  5 13:48 c_lat2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13469 Sep  5 14:10 c_latin120.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4845 Sep  5 10:50 c_root3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30227 Sep  5 09:50 crop_ambor.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25024 Sep  5 09:50 crop_berijab_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    39114 Sep  5 09:50 crop_berijan_ar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65413 Sep  5 09:50 crop_persian_roast.png
-rw-rw-r-- 1 sfmqrb sfmqrb    23219 Sep  5 01:51 c_schyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1795 Sep  5 10:50 c_scyth2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2953 Sep  5 10:50 c_scyth3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4885 Sep  5 10:49 c_scyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3019 Sep  5 10:15 c_sus.png
-rw-rw-r-- 1 sfmqrb sfmqrb    33345 Sep  5 10:55 e0.102.json
-rw-rw-r-- 1 sfmqrb sfmqrb    38686 Sep  5 10:34 e0.95.json
-rw-rw-r-- 1 sfmqrb sfmqrb    58057 Sep  5 02:29 e0full.json
-rw-rw-r-- 1 sfmqrb sfmqrb     4446 Sep  5 02:23 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb    26175 Sep  5 10:38 e1.95.json
-rw-rw-r-- 1 sfmqrb sfmqrb      456 Sep  5 10:56 g.py
-rw-rw-r-- 1 sfmqrb sfmqrb   445959 Sep  5 01:37 hrn126_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1213019 Sep  5 01:37 hrn126.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   456157 Sep  5 01:37 hrn127_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1278807 Sep  5 01:37 hrn127.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    24046 Sep  5 13:38 latin.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49033 Sep  5 10:53 mk100.py
-rw-rw-r-- 1 sfmqrb sfmqrb    17464 Sep  5 10:55 mk102b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    25511 Sep  5 10:58 mk102c.py
-rw-rw-r-- 1 sfmqrb sfmqrb    21655 Sep  5 10:53 mk102.py
-rw-rw-r-- 1 sfmqrb sfmqrb    62559 Sep  5 11:04 mk103.py
-rw-rw-r-- 1 sfmqrb sfmqrb    79255 Sep  5 13:30 mk104.py
-rw-rw-r-- 1 sfmqrb sfmqrb    47159 Sep  5 13:30 mk105b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    31652 Sep  5 13:24 mk105.py
-rw-rw-r-- 1 sfmqrb sfmqrb    62837 Sep  5 13:37 mk108.py
-rw-rw-r-- 1 sfmqrb sfmqrb    40927 Sep  5 13:43 mk109.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63862 Sep  5 13:46 mk110.py
-rw-rw-r-- 1 sfmqrb sfmqrb    48342 Sep  5 14:00 mk113.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61685 Sep  5 14:01 mk114.py
-rw-rw-r-- 1 sfmqrb sfmqrb    60434 Sep  5 14:01 mk115.py
-rw-rw-r-- 1 sfmqrb sfmqrb    76964 Sep  5 14:09 mk116.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb    67712 Sep  5 10:03 mk87.py
-rw-rw-r-- 1 sfmqrb sfmqrb    66054 Sep  5 10:10 mk89.py
-rw-rw-r-- 1 sfmqrb sfmqrb    70790 Sep  5 10:04 mk90.py
-rw-rw-r-- 1 sfmqrb sfmqrb    48553 Sep  5 10:03 mk91.py
-rw-rw-r-- 1 sfmqrb sfmqrb    27206 Sep  5 10:38 mk95b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    39501 Sep  5 10:34 mk95.py
-rw-rw-r-- 1 sfmqrb sfmqrb    49433 Sep  5 10:35 mk96.py
-rw-rw-r-- 1 sfmqrb sfmqrb    54149 Sep  5 10:47 mk97.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61159 Sep  5 10:50 mk99.py
-rw-rw-r-- 1 sfmqrb sfmqrb 18949704 Sep  5 02:30 mw1872.htm
-rw-rw-r-- 1 sfmqrb sfmqrb    32690 Sep  5 13:24 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb     3057 Sep  5 10:05 patch87.py
-rw-rw-r-- 1 sfmqrb sfmqrb    71589 Sep  5 10:41 pg100.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68145 Sep  5 10:44 pg102.png
-rw-rw-r-- 1 sfmqrb sfmqrb   114170 Sep  5 10:49 pg103_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79623 Sep  5 10:49 pg103.png
-rw-rw-r-- 1 sfmqrb sfmqrb   169766 Sep  5 10:57 pg104_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22122 Sep  5 10:58 pg104_charlatan.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78826 Sep  5 10:57 pg104.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31584 Sep  5 11:00 pg104_tea.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82500 Sep  5 10:57 pg105.png
-rw-rw-r-- 1 sfmqrb sfmqrb    55270 Sep  5 11:01 pg106.png
-rw-rw-r-- 1 sfmqrb sfmqrb    48976 Sep  5 11:01 pg107.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68501 Sep  5 13:26 pg108.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63543 Sep  5 13:30 pg109.png
-rw-rw-r-- 1 sfmqrb sfmqrb     6518 Sep  5 13:38 pg110_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67502 Sep  5 13:29 pg110.png
-rw-rw-r-- 1 sfmqrb sfmqrb    36325 Sep  5 13:32 pg110_yeth.png
-rw-rw-r-- 1 sfmqrb sfmqrb    46559 Sep  5 13:32 pg110_zbn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72718 Sep  5 13:38 pg111.png
-rw-rw-r-- 1 sfmqrb sfmqrb    50381 Sep  5 13:37 pg112.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65357 Sep  5 13:45 pg113.png
-rw-rw-r-- 1 sfmqrb sfmqrb   117231 Sep  5 13:48 pg114_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1253 Sep  5 13:48 pg114_french.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11671 Sep  5 13:48 pg114_latin.png
-rw-rw-r-- 1 sfmqrb sfmqrb    83933 Sep  5 13:46 pg114.png
-rw-rw-r-- 1 sfmqrb sfmqrb   163144 Sep  5 13:51 pg115_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70699 Sep  5 13:51 pg115.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64811 Sep  5 13:57 pg117.png
-rw-rw-r-- 1 sfmqrb sfmqrb    42354 Sep  5 14:05 pg118.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78691 Sep  5 14:11 pg119.png
-rw-rw-r-- 1 sfmqrb sfmqrb    84971 Sep  5 14:10 pg120_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    50224 Sep  5 14:06 pg120.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb   134852 Sep  5 09:54 pg88_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11747 Sep  5 09:54 pg88_e0spine.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31391 Sep  5 09:55 pg88_join.png
-rw-rw-r-- 1 sfmqrb sfmqrb    98452 Sep  5 09:54 pg88.png
-rw-rw-r-- 1 sfmqrb sfmqrb    26700 Sep  5 09:54 pg88_spine.png
-rw-rw-r-- 1 sfmqrb sfmqrb   171528 Sep  5 02:45 pg89_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4628 Sep  5 02:45 pg89_ambor.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4924 Sep  5 02:45 pg89_berijan.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80984 Sep  5 09:49 pg89.png
-rw-rw-r-- 1 sfmqrb sfmqrb    77182 Sep  5 09:48 pg90.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63799 Sep  5 09:55 pg91.png
-rw-rw-r-- 1 sfmqrb sfmqrb   157177 Sep  5 10:09 pg92_500.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8494 Sep  5 10:09 pg92_avestan.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3476 Sep  5 10:09 pg92_pahlavi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    90918 Sep  5 10:07 pg92.png
-rw-rw-r-- 1 sfmqrb sfmqrb    93420 Sep  5 10:15 pg94.png
-rw-rw-r-- 1 sfmqrb sfmqrb    44047 Sep  5 10:16 pg94_sogd.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49714 Sep  5 10:16 pg94_urvar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78178 Sep  5 10:11 pg95.png
-rw-rw-r-- 1 sfmqrb sfmqrb   163439 Sep  5 10:15 pg96_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72929 Sep  5 10:15 pg96.png
-rw-rw-r-- 1 sfmqrb sfmqrb   101597 Sep  5 10:41 pg99_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8738 Sep  5 10:41 pg99_french.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65608 Sep  5 10:40 pg99.png
```


## [2026-09-05T18:11:11.948Z] TOOL CALL #52: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg119.png"
}
```


### [2026-09-05T18:11:12.533Z] TOOL RESULT

```

```


## [2026-09-05T18:11:12.530Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T18:11:27.216Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls incoming/WLD/ && grep -n \"schinden\" incoming/WLD/WLD_Bd1_pages.txt | head -10"
}
```


### [2026-09-05T18:11:27.278Z] TOOL RESULT

```
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
1098:engti „schinden, qualen, bedrueken“, bei Pilkau aucb „schlagen“, arkli nuengti „ein
53440:slov. guliti „wetzen, reiben, schinden * (vgl. Berneker SlEWb. 362, wo altere,
69282:,,stechen“,               s.   u. "tier-           ,,schinden' ).
71375:dheragh -, ilhrty- (vgl. auch Anklange unter tier- „schinden“, Wzf. deryh-,
71491: u.     der-     „schinden“), Vf. LEWb. 2              prastan (s. u. *terck-
72562:der- ,,spalten, schinden s. unter eigenem Stichworte.
74974:  Beziehung zu *dcr- „schinden, spalten (Curtius 5 235) wird durch die     11
75214:4. der-, set-Basis          dere- „schinden, die Haut abziehen, abspalten, spalten".
75345:      lit.    dirti   „schinden, Rasen oder Torf abstechen“ (set-Form gegeniiber
75790:Miihlenbach-Endzelin I 470, zu der- „schinden“.
```


## [2026-09-05T18:11:30.211Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '75214,75290p' incoming/WLD/WLD_Bd1_pages.txt; echo \"..... drep-\"; grep -n \"drep-\\|drappus\\|drapsa\" incoming/WLD/WLD_Bd1_pages.txt | head"
}
```


### [2026-09-05T18:11:30.304Z] TOOL RESULT

```
4. der-, set-Basis          dere- „schinden, die Haut abziehen, abspalten, spalten".
   Ai. dar-     „bersten machen,        spalten, sprengen", anit-Praes. ddrsi ad art,           ,


dart   ,
        n-Praes. der set-Basis (drndti ), opt. drmynt , Pf. dadilra , Ptc. (anit)
drta -, (set) dirnd-, Kaus. ddrayati, Intens. dardirat, dardarti (vgl. av. dar idar-
„spalten“; cech. drdam , drdati „rupfen, abrupfen" Berneker 254), dardanti
„zerspaltet“; dar a- m., dart f. „Loch in der Erde, Hohle“ (: gr. dood?
„Schlauch“, lett. nuodaras ,,Abfall von Bast", ksl. razdorz), drti - m. „Balg,
Schlauch" (= gr. dagaig, got. gataidrps , russ. dertd), danndn- m. „Zerbrecher“
(: gr.     degpa n.), woneben die set-Form darlman- „Zerstorung“; -dari „zer-
spaltend" (= gr. dfjgig), dcira- m. „Rifi, Spalte, Loch“, daraka- „zerrei6end,
zerspaltend", dan- in dardari-ti, dan-man- mit 7 fur i = a, kaum nach
Persson Beitr. 779 (nw.) von der i-Basis (s. u); np. Inf. dirldan , dun dan                                    ,


jiid.-pers. dartn-isn ;
   av. darddar-       (s.       o.)   „spalten“,   Inf.    ddronqm   (:   ai.   drndti ), Iter, dctraya -,
 Ptc. danta-(=        ai. drta-).

   Arm. terem „haute  ab, schinde, mache Bchwielig" (Meillet Msl. 8, 165,
 Zweifel bei Hiibschmann Arm. Gr. I 497; wegen r wohl zur Wzf. *der-s                                          ,


 Persson Beitr. 779 Anm. 1); vielleicht arm. tar „fremd(es Land)", iara-
 „au6er, ohne, fern", taray Aor. „nahm ReiBaus"        (s. Pedersen KZ. 39, 3 7 2 f                        .


 Persson Beitr. 778a 2; anders       Hiibschmann    Gr.  I 496f., gr. dsgco „haute
 ab, schinde", deigto ds., Aor. pass, eddorjv Ptc. dgaxog dagrog {— ai. drta-)-,
                                                               ,                ,


 dogog „Schlauch“ (= ai. dar a-, lett. nud-daras); dagotg „das Abhauten"
 (= ai. drti-), woneben mit (geneuerter) Hochstufe att. deggig, -scog „Haut,
 ledernes Kleid, Decke"; degigov, diss. dergov „Haut im Korperinnern";
 degag, -axog n. „Fell“ (set-Form), degog n., deoya n., dogd „Fell ‘; dehnstufig
 drjgig, -log (poet.) „Streit, Kampf" (= ai. -dari--, Ostboff Pf. 1 18, 607 m. Lit.);
    [alb. djer „vernichte, verliere" (G. Meyer Alb. Wb. 70) ist nach Peder-

 sen KZ. 36, 325 f. vielmehr *dz-bier, zu bher- „tragen“;j
   cymr. corn. bret. darn ,, Stuck, Teil" (= ai. dirnd--, Fick II 4 149); aber
 mir. drcnn „Streit“, drennach ,,ziinkisch", abret. ardren gl. „praepugnus“ nicht
 aus *drn-uo- ibd. vgl. dt. Zorn, sowie ai. drndti).
                            ;
798                                                    der-


  Auch ir. dretell „Liebling“ (Fick II 4 155) bleibt fern, s. Pedersen KG. I
131,   160.
  Got. dis-tairan             (= gr. dioco) „auseinanderreiBen“, gatairan „zerreiBen,
zerstoren",         ags.     teran     „zerreifien“,     ahd. zeran       ,
                                                                              ftr-zeran        „zerrei£ien, zer-
storen“;      as.   farterian        mnd.    tercn,     mhd. (ver)zern         ,
                                                                                   nhd.    (
                                                                                               ver)zehren      „ver-
zehren,   verbrauchen“, mengl., mnd. terren „zanken“, nd. terren tarren                                ,

,,reizen, necken“, ahd. zerren „zerren“; got. dis         ga-taurnan „zerreiBen
                                                       -,
(intr.)“ (: ai. drndti ir. drenn ), holl. tornen „sieh auftrennen“, ygl. nominal
ags. as. torn, ahd. zorn „Zorn, Streit, heftiger Unwille" und in urspriing-
lichster Bed. holl. torn „Spaltung, Scheidung“ (= ai. dirna -, cymr. darn-,
auch dirna- heiilt auBer „gespalten“ auch „verwirrt, in Yerzweiflung be-
findlich“; s. u. lit. durnas „rasend, dumm“), woneben hocbstufig anord. tjqrn
f. ( *derna ), tjarn n. ( *dernom ) „kleiner See“, ursprgl. wohl „Wasserloch“
(vgl. ai. dara      dart „Loch in der Erde“)       zu qataurnan trat kausatives
                                                                      ;


(iteratives) gatarnjan „beraaben“, (aber ahd. uozurnen „verachten“ ist
Denom. von *uoeorn, trotz Holthausen IF. 14, 340, Grienberger SB.
WienerAk. 142, YIII 92); got. gafaura m. „RiB“, gataurps f. „Zerstorung“
(= ai. drti -,       gr. dagatg)-,      anord. tord-       in     Zs.,    ags. tord       n.   „Kot“   (
                                                                                                           *dr-tom
„Abseheidung“, vgl. lett. dbstu , d'irst „cacare“, difsa „der Hintere“, Miihlen-
..... drep-
75539:   Mit p-Erweiterung (vgl. o. slav. dri-p-, und u. *drep-), gr. dgvmw „zer-
75673:„Mantel, Kleid", drapsa- m. „Banner“ (diese Bed. von Geldner Yed. St. Ill 57
75725:oder aus zu *drep- gehorigem *drap-s- wegen der germ. s-Formen ent-
```


## [2026-09-05T18:11:33.397Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '75665,75700p' incoming/WLD/WLD_Bd1_pages.txt"
}
```


### [2026-09-05T18:11:33.450Z] TOOL RESULT

```
s.    *dereyp- „Baum“),           obgleich es der Bed. „Dorn“ (*,,Zerrei6er“) weniger
entspricht.
      Anord. trqf n. pi., trefr f. pi. „Fransen", trefja „zerfasern", irefill m. „Faser,
Lumpen", mhd. trabe f. „Franse“ (Falk-Torp u. trave II       nicht als *drobh-,      ;

drebh- zu slav. drobiti „zerrei8en", das zu got. gadraban „aushauen“, idg. dh-).
  Mit der Bed. „abgerissenes Stuck Tuch, Kleid" (vgl. u. cech. drasta
^Splitter, Fetzen, Gewand" zu drasati „ritzen, kratzen") ai. drapi- m.
„Mantel, Kleid", drapsa- m. „Banner“ (diese Bed. von Geldner Yed. St. Ill 57
bestritten) = av. drafsa- „Fahne, Banner", lit. drapanos f. pi. „Wei£Szeug,
leinene Unterkleider der Frauen", allenfalls auch die noch nicht be-
stimmte (s. Korting LRWb. 367 m. Lit., Meyer-Liibke RomEtWb. Nr. 2765)
Quelle von ital. drappo „Tuch", drappello „Fetzen, Fahne", frz. drap „Tuch“,
drapeau „Fahne“.
      Uber ein      in   slav.    *dwba      vielleicht ein gemischtes *der-bli-            s.   u. derbh-
„winden“.
      Wzerw. der-k, dre-k-
iiber dognov,        alb.   darks    s. o.   unter *dre-p -     ;
                                                                     Aosy.avov       Name eines Yorge-
birges in  Kos (wie Aosjiavov mehrfach als Name von Yorgebirgen, Cur-
tius° 493, Bugge BB. 18, 189), bony.ai xovideg, dsQxvlkeiv alponoxsiv (eigent-
                                                    '


lich „die Haut aufrei8en“ wie gleichbed. Ssguv/dsivj Hes. (Fick BB. 28, 99;
„ob dgdy.mv wirklich vom Blicken <5 egneo'dai benannt ist?“); sloven, drkarn                             ,

drcem, dfkati „ gleiten, glitschen, auf demEise schleifen; rennen, Trablaufen“
(wold aus „Rei[:jaus nehmen“), cech. drkati „stofien, holpern“, bulg. dircam,
dncm „ziehe, riffle Flachs, Hanf“ (Berneker 255, Persson Beitr. 85, 359).
  Wzerw. der-s- und dre-s -, dre-sk-
vermutlich ags.          teors,    ahd. zers „penis“          (s.   o.   unter d(c)rf-);   auch anord.
tjasna f. „Art Nagel" aus *tersnon-1 (Fick III 4 158); arm. terem (s. o. unter
der-)\  ir. dorr „Zorn“, dorrach „rauh, grob" (s. Persson Beitr. 779 Anm. 1,

auch Fick II 4 152.
```


## [2026-09-05T18:11:40.174Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"دریدن\\|درفش\\|درو کردن\\|درودن\\|دره\" ARY_pages.txt | head -20; echo \"### latin index\"; grep -n -i \"DARIDAN\\|DERAFSH\\|DARRE\\|DOROW\\|DARIDAN\" ARY_latin_index_pages.txt | head -20"
}
```


### [2026-09-05T18:11:40.248Z] TOOL RESULT

```
831:نواحی تورفان و دره‌ي تارم مورد تاخت و تاز اقوام ترک قرار گرفت و زبانهای تخاری (مانند ۱
5905:فارسی (28/814): تنجیدن, تنج (به چم "بخود پیچیدن" و درهم فشرده شدن۳)
7967:پازگشت به : دریدن
8060:دروء درودن» درویدن ] ۲۷۵
8073:۱ این واژه با واژه‌ی "دریدن" همریشه است. بازگشت به: دریدن. ۰
9735:۳ چم این واژه در زبان ارمنی: آبکند» دره, :
12053:۱ ۲ چم این واژه در زبان سانسکریت: کشیدن» دریدن
15723:آلمانی (0870/۸2): بدره ها 5
### latin index
```


## [2026-09-05T18:11:42.596Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && sed -n '7940,7990p' ARY_pages.txt; echo \"==================\"; sed -n '8050,8090p' ARY_pages.txt"
}
```


### [2026-09-05T18:11:42.658Z] TOOL RESULT

```
صربی (۸07ق557): زر برهان قاطع : ۸۲۹
پرهمی (80[75214/۷):
یادداشت. :
۱-بازگشت به: دازا درنگ.
۲-چم این واژه در زبان گوتیکه: دراز مدت؛ پایا؛ محکم
اوستایی (/47857۸): 182۸[۸11,08۸[130 سانسکریت (845777):
پهلری (47ات۸: 03۸۷۸۷, 07۸31۳۸ شلد ای 073018۸9
ا
[pdf page 270]
نج ۰ ۹
۳۷۱۱۵۵
اسلاوی کهن ۰ (۲70ا؟ ۲7086/7) 0ا0):
0107۸ پسگشت‌ها یی
لپستانی (بقذناه): 06 0
روسی (87899/7): 0۸ 0 (1۵688) 0
چک (25207)): 06۸ 1 (۳۲671) :728( هل
صربی (85814(۷): 03 82-3 نا
اسلوا کی (5-0740): 01216۸ برهان قاطع : ۸۳۹
هنیت (7777[78): اد نگ رن ۱۱۸۱
یادداشت:
بازگشت به: دراز» درنگ
پهلری (۲7القهه): 27 پسگشت‌ها هار۲ :
کردی (020(8): 0 ,2۸330 7 م20
بلوچی (71تاته8): ری ۱۱1۹ 6 (۴۸۹۲) :22 من ۸۸
افغانی (پشتر) (4۳0/۸(77): زر۵ ۱۳۲ 4 ۸/1000
تخاری ۸4 (۸ 7003/74(7): ۰ 0۸3017 برهان قاطع : ۸۳۴
یادداشت: ۱
پازگشت به : دریدن
,
ا
اوستایی (4۲857/4(0): 3۸187 بف28352 تخاری 8 (8 70707۸1۸(7): ه4 ۲۸
پهلوی (7اتلهه): 2 سانسکریت (84(78۹7077): 12۸77
ازستی (0958776): 5 ارمنی (4(/8(/14(7: ۰ 0833۸37 ,213۸4
کردی (67307517): 22 آلبانی (1427لمقلم): 2037
تخاری ۸ (۸ ((703۸73): هتیت (7177175): 7۸3۸77۲
۰ ,16 ,71282
[pdf page 271]
اّ
پسگشت‌ها دب ند 1 (88۸71) :۱۷۸0052/2
8 00200 برهان قاطع رن ۸۳۵
پا شور 9
یادداشت: و
چم این واژه در اوستایی و سانسکریت: محکم کردن
چم اين واژه در ارمنی: خیاط ربسمان ۰
چم این واژه در اوستی: جامه
چم اين واژه در زبانهای تخاری: اجازه دادن» رخصت دادن.
چم این واژه در کردی: ریسمان
۲- در زبان پهلوی واژه‌ی 2۸16210 به چم «خیاط» بکار می‌رفته است.
اوستایی (۸۲87/27): ید ۱۱ هلندی (7ع017): رید ای بان نی
پارسی باستان (۸(۷ای۳87 صا0): لیتوانی (۸2]897لا73ر): نارای ۱۱
۷-1 با1 1011-08517 پروسی کهن (40۷ا۳#055 0ا0): 081718
==================
َ اپرلندی کهن (تلدلم[ صاه). 10۴
یادداشت,
۱- واجریشه‌ی هند و اروپایی این ریشه در اصل همان واجریشه‌ای است که واژه‌ی «دراز» از آن ناشی شده
است.
۲ بازگلست به: دراز
چم این واژه در زبانهای اوستایی و پهلوی: طولانی» پایدار,
۴ چم این وأژه در زبانهای رومانس (ناشی از لاتین) و ژرمنی: دراز» طولانی
ا
[pdf page 274]
6666
دروء درودن» درویدن ] ۲۷۵
پهلری (۲7مالل۸): 0310۸07 لیترانی (771۸(/49۷):
کردی (82[57): تلود نی ۱زا 2811 ,ا3الت28 ,تا+057 :
تخاری ۸ (۸ ۰:70 18075
سانسکریت (85(/5777): پسگشت‌ها 5
7 ,0۸3 +034 زر ۳
یرنانی (07530): 58 ,0830 6 (1۸35) ی
اسلاوی کهن (ع1ماد 63 تال صان): 9 (۸5۸8) :2406212
8۸ ,0880 507 ک ان
روسی (۷ل75514چ): 0 برهان قاطع + ۸۴۱
چک (25301): ت08 لفت‌نامه دهخدا: ۷ و ۱۰۶۹۵
صربی (587814/۷7): 1 اد ۷۱۱
بادداشت,
۱ این واژه با واژه‌ی "دریدن" همریشه است. بازگشت به: دریدن. ۰
۲ چم بیشتر واژه‌های غیر ایرانی این فهرست: بریدن؛ تراشیدن.
‌
| تواکلس سوزی اش ی هد
اوستایی (۸887427): 7 ,0306 ,0۸306
او ابفت08۸06 ,08028۸37 020 افغانی (پشتو) (/4۸۳0/7۸/۷):
پارسی باستاً(0(ما دا رم : 7 0۸3361 ۱
۸ ,08۸6۸ سانسکریت (5۸(/587):
پهلری (۸(7]۸1): اسر زا +07 ,0۳0677۸8 ,07017۷۸7
7 ,330 ,010673 ,00۷ ایسلندی کهن (010۸۵7/(م5 صا۵):
کردی (08278/7): 0817۷۷۰ ,01081767 20۸0
بلوچی (37لنانتم8): ساکسرنی کهن (40۸ 8107706۸71:)012
سم
[pdf page 275]
۶ )وا
آلمانی کهن (027۸/49 ۲/07 صران): پسگشت‌ها شید درا
7106۸0 26 امین
آلمانی (7(ف054): لادنی ایا 300 (800 ار بر 270430
```


## [2026-09-05T18:11:51.607Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && sed -n '9700,9760p' ARY_pages.txt"
}
```


### [2026-09-05T18:11:51.660Z] TOOL RESULT

```
ایركدی کهن (#فل#/ 012): ۰ 810 ,8850 256 تلا
ولزی (84 )+ نان 1 (01100) :0/05
برتونی (/87870): 13۸ 2 (01100) 357
گالیکه (0۸81]70): ند 3 (۸778) ۸400
برهان قاطع : 1.۸۳
بادداشت:
۱- چم این واژه در زبان آلمانی نوین؛ سرزنده.
چم این واژه در زبان هلندی: جیره.
۲- یکی از چم‌های واژه‌ی انگلیسی 011101 زنده.
۳ بازگلت به: زیستن.
2۸07۸ ,207
اوستایی (47887۵/۷): فریزی کهن ((۲۷۹1۵ 010): 17۸
خ2۸07118 بال2۸07۸ آلمانی کهن (/(08704۸ 2۷/0 ۵ا۵):
1 پهلوی (1شالتم۳۸): 7207 ۸ ,61022۸
هو «سانسکر یت (8۸/51077): آلمانی (0874۸۷): ود ند ان
20306 ,103011 انگلیسی کهن (2۸0/1 012): ۰ 0807۸05 ۱
ارمنی (۸//8142): 7 ب,08[ انگلیسی (8لا600): 0
یونانی 078850): 60 ,01852۸ دانمارکی (0۸۷/80): 0052
لانین (7/0): ۰ ۲۲۵۲۶۵ ,57۸00 سوئدی (91752154): 207۸
گرتیکد (ع00771): 01137۸ نروژی (/087801۸): 207۸
ایسلندی کهن (/504(/210۸71۸۸ 00): هلندی (0ل07): 0 ,0007
۸ ,978ت0۲ 60107۸ لیتوانی (۸(/1۸/۷تا777):
[pdf page 329]
ُ
ا
۰ زود ۱
6۸1 ,۷۸85 پسگشت‌ها ده اد اد ی
لتونی (لتی) ((477۸ل): ات 48 200200
9 (07) 2 ۸ :22( ها
کک هام ۹ جهمی روم 1
۱ لغت‌نامه دهخدا: ۱۳۲ ا
یادداشت: ی
۱ واژه‌ی زور" به چم "آب مقدس که در مراسم زرتشتی پاشیده می‌شود" نیز از همین واجریشه است
(اوستابی:2۸0711۸؛ پهلری: 2:013). ۱
۲ چم این واژه در زبان‌های ژرملی و زبان لاتین: جاری شدن؛ آبگونه شدن. ۱
۳ چم این واژه در زبان ارمنی: آبکند» دره, :
۳ ا
اوستایی (47887/400): ۸ ,701 ایسلندی کهن (/54(/0/0141 0ا۲)0شاید)
پارسی پاستان (۳8۴۹1۵۸۷ صا0): 717۸ ده
پهثری (1لاماتا۸ه). 0 ,701
کردی (00/5(7): 71711 ,211 ,275 رنآ2 پسگشت‌ها از ادن ۲
بلرچی (//4۲0): ۰ 21773 ,217 ,207 9 ۸0800
اففانی (پشتو) (۸۳017۸(۷1): 2 9 (01166) :2ل52 ۸لز
سانسکریت (84۸/5507): 2.1317771 ب۳۸لآل برهان قاطع : ۱۰۳۳
یادداشت: ۰
شاید این واژه‌ها هم از همین واجريشه باشند: گرتیکه: 8 آلمانی کهن: 98۸7؛ انگلیسی کهن:9021۸ انگلیسی:
نان :
:
اوستایی (4587۸4): 3 5۸۷۸8 ,ا3۵7[ ,تشاد
پهلری ([اللم۸ه): 6 208 ارمنی (4748401): 3
کردی (07(01374): اد زد زا بونانی (0220): (شاید) 05
سانسکریت (84(507): ایسلندی کهن (524701۸4۷۵(۷ صا۲)0(شاید)
۱۲
[pdf page 330]
زور (به چم "نادرست و دروغ") / ۳۳۱
3 پسگشت‌ها 055
گالی (ل8لاتا0): (شاید) دید 99 20802900
8 (878006) ام ارم
برهان قاطع + ۱.۳۳
| م‌اگلیس سوازای ارس سا ۱88۵8
اوستایی (/۸587/4): ,218۸5 انگلیسی ([8۸01./5): اد ۱۸|
```


## [2026-09-05T18:11:59.300Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -m3 -A4 \"drape (v\" 2d48dc03c75d342b.txt | head -20; echo \"=== tear\"; grep -n -m3 -A6 \"tear (v\" 2d9a52ce95203851.txt | head -20; echo \"=== PIE der- wikt\"; grep -n -A20 \"Root\" a5705981f1b1cc3d.txt | sed -n '1,40p'"
}
```


### [2026-09-05T18:11:59.392Z] TOOL RESULT

```
23: drape (v.) 
24-
25- c. 1400, drapen , "to ornament with cloth hangings;" mid-15c., "to weave into cloth," from Old French draper "to weave, make cloth" (13c., in Modern French "to cover with mourning-cloth, dress, drape"), from drap "cloth, piece of cloth, sheet, bandage," from Late Latin drapus , which is perhaps of Gaulish origin (compare Old Irish drapih "mantle, garment"). Meaning "to cover with drapery" is from 1847. Meaning "to cause to hang or stretch out loosely or carelessly" is from 1943. Related: Draped ; draping .
26- also from c. 1400 
27-
--
30: 1660s, "cloth, drapery," from drape (v.). Jive talk slang for "suit of clothes" is attested from 1945. Drapes "curtains" is by 1895. 
31- also from 1660s 
32-
33- Entries linking to drape 
34-
--
37: 1715, "yellowish-gray; of the color of natural, undyed cloth," from the trade name for the color itself (1680s), which is from an earlier noun drab, drap meaning "thick, woolen cloth of a yellowish-gray color" (1540s), from French drap "cloth, piece of cloth" (see drape (v.)). The figurative sense of "dull, not bright or colorful" is by 1880.
38-
39- Apparently this word is not related to earlier noun drab "a dirty, untidy woman" (1510s), "a prostitute" (1520s), which might be from Irish drabog , Gaelic drabag "dirty woman," or perhaps it is connected with Dutch and Low German drabbe "dirt;" compare drabble . The notion seems to be of dabbling in the wet and mud.
40-
41- The meaning "small, petty debt" (the sense in dribs and drabs ) is by 1828, of uncertain connection to the other senses.
=== tear
62: tear (v.1) 
63-
64- [rend, pull apart by force] Middle English tēran "destroy by reducing to fragments; tear apart (an animal); rend to pieces (a book, garment)," from Old English teran "pull apart by force; lacerate" (class IV strong verb; past tense tær , past participle toren ), from Proto-Germanic *teran (source also of Old Saxon terian , Middle Dutch teren "to consume," Old High German zeran "to destroy," German zehren , Gothic ga-tairan "to tear, destroy"), from PIE root *der- "to split, flay, peel."
65-
66- The Old English past tense survived long enough to get into Bible translations as tare before giving place 17c. to tore , which is from the old past participle toren . The sense of "pull by force" (away from some situation or attachment) is by early 14c. (in tear down ), hence to be torn between two alternatives (desires, loyalties, lovers, etc.), by 1871; tear (oneself) away "go unwillingly" (1797). The intransitive sense of "part, divide, or separate readily" is from 1520s.
67-
68: To tear one's hair (out) in grief or frenzy was in Old English. For tear into , see tear (v.3). The print media tear-sheet "page featuring an ad, clipped from the publication and sent to the advertiser as proof," is by 1930.
69-
70: tear (v.2) 
71-
72- [weep, cry] late Old English teren , "shed tears;" from tear (n.2). From 1650s as "fill with tears" mainly in American English. Related: Teared; tearing . The Old English verb tæherian , tearian "to weep" apparently did not survive into Middle English.
73- also from early 15c. 
74-
75- tear (n.2) 
76-
=== PIE der- wikt
62: Root 
63-
64- 1.1.1 
65- Alternative reconstructions 
66-
67- 1.1.2 
68- Derived terms 
69-
70- 1.1.3 
71- Descendants 
72-
73- 1.2 
74- References 
75-
76- Toggle the table of contents 
77-
78- Reconstruction:Proto-Indo-European/ der- 
79-
80- Add languages 
81-
82- Reconstruction 
--
137: Root
138- [ edit ] 
139-
140- *der- [ 1 ] [ 2 ] 
141-
142- to split , to separate 
143-
144- to tear , to crack , to shatter 
145-
146- Alternative reconstructions
147- [ edit ] 
148-
149- *derH- [ 1 ] 
150-
151- Derived terms
152- [ edit ] 
153-
154- Terms derived from the Proto-Indo-European root *der- (56 c, 0 e)
```


## [2026-09-05T18:12:04.507Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -m2 \"TEAR (1)\\|Tear (1)\\|tear (1)\\|DRAPERY\\|Drapery\\|drapery\" SKT.txt | head; grep -n \"teran, to tear\\|to tear.*Teut. type\" SKT.txt | head -5"
}
```


### [2026-09-05T18:12:04.581Z] TOOL RESULT

```
5390:I>rape,  to  cover  with  cloth.  (F.«1 K.  draper,  to  make  cloth  —F.  ^n^.  ( I-ow  L.  draffus  Prob.  from  Ice!.  * to  beat  (from  the  fulling  process^ Drub.     Der.  drap-er,  drapery.
20561:vaunt.    (F.  — L.)      F.  tt   vanter,    to boast.  — Low  L.  Manitare,  to  speak  vanity^ I        flatter;  (F.  se  ww/^- to  flatter  oneself). •       A  fre<incntotive  form  from  uamir^  vain, Vair,  a  kind  of  far;  icc  Varioiu. Valance,    a    fringe    of    drapery,    now applied    to   a   part    of   the    bed-hangings. (F.-L.)      Chaucer   has  'a  litel   kerchief of   vaitnct;^    Assembly   of   Foulcs,    fji. Prob.  named  from  Valfna  in  Ffancc,  near Lyons  (still  famoas  for  &ilksl.  — L.  UaUntux, a  name  given  to  several   towns,  evidently with   the  sense  of  'strong.*  — L.   maient-, stem  of  prei.  pt.  of  ualerty  to  be  strong ; we  Valid.      ^  Johnson   derives  it  from VaUntia  in  Spain ;  but  was  it  ever  finmous for  silk? Vale,  a  valley  ;  sec  Valley. Valediction,  Valentine,  VaUriui ; MC  Valid.
```


## [2026-09-05T18:12:11.782Z] TOOL CALL #61: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-05T18:12:11.825Z] TOOL RESULT

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


## [2026-09-05T18:13:40.822Z] AGENT

Now I'll write the verification file.


## [2026-09-05T18:20:54.907Z] TOOL CALL #62: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-119.json <<'JSONEOF'\n{\n  \"pdf_page\": 119,\n  \"book_page\": 89,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Der 1, Derô, Drtis, Drtos\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *der- (*derH-) 'to split, flay, tear', heavy base *derə-/*drē-; nominal derivatives *dr̥tis 'a flaying, skin' and *dr̥tos 'torn, flayed'\",\n      \"note\": \"Pokorny 206-211 heads the root exactly as Nourai writes it: '4. der-, schwere Basis derə-, drē- «schinden, die Haut abziehen, abspalten, spalten»'. Nourai's 'Derô' = Pokorny's derə- (the set-base), 'Drtis/Drtos' = Mann IEC 165 headwords drtis 'têaring, scraping; têar, skin' and drtos 'torn, flayed, cut, worn, ground' (= Skt. dr̥ti-/dr̥ta-, Gk. δάρσις/δαρτός, Goth. gataurþs). Language label (Indo-European) and gloss ('to split, to tear') are both right; the modern reconstruction is *der-, with *derH- an alternative (Wiktionary, LIV 119f.).\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *der- (یا *derH-) به معنای «شکافتن، دریدن، پوست کندن» با پایهٔ کشیدهٔ *derə-/*drē-؛ از آن نام‌های *dr̥ti- «پوست، مشک» و *dr̥to- «دریده، بریده» ساخته شده است. پوکورنی (ص ۲۰۶ تا ۲۱۱) دقیقاً همین صورت‌ها و همین معنا را می‌آورد و مان (فرهنگ تطبیقی هندواروپایی، ص ۱۶۵) نیز drtis و drtos را سرواژه کرده است. پس نام ریشه، برچسب زبانی و معنای آن در نمودار نورایی درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/der-\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:206\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 217 (printed p.206): '4. der-, schwere Basis derə-, drē- «schinden, die Haut abziehen, abspalten, spalten»' — the entry runs pp.206-211 and contains ai. dr̥ti-, dr̥ta-, gr. δάρσις, δαρτός, got. gataurþs, i.e. Nourai's Drtis/Drtos.\"},\n        {\"ref\": \"IEC:165\", \"status\": \"supports\", \"note\": \"IEC.txt leaf 105 (printed p.165): 'drtis «têaring, scraping; têar, skin». See next & cf. WP I, 797: dero — Skt. drtih «skin»; Per. dül «water-skin»; Gk. dársis; Go. ga-taürþs' and immediately after 'drtos (1) «torn, flayed, cut, worn, ground» ... Av. dərəto (1) «cut, mown»'.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I 797-803\", \"stance\": \"supports\", \"note\": \"WLD_Bd1_pages.txt l.75214: '4. der-, set-Basis derə- «schinden, die Haut abziehen, abspalten, spalten»' with ai. dr̥ti- «Balg, Schlauch», av. darədar- «spalten», Ptc. dərəta- (= ai. dr̥ta-), np. Inf. dirīδan, darīδan.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. der-2\", \"stance\": \"supports\", \"note\": \"'der-2, To split, peel, flay; with derivatives referring to skin and leather ... [Pok. 4. der- 206.]' — same root, same gloss, same Pokorny page.\"},\n        {\"src\": \"SYN\", \"where\": \"p.565 (§9.27 SPLIT, §9.28 TEAR)\", \"stance\": \"supports\", \"note\": \"'Av. dar- : Skt. dr̥- «burst, tear, split», Grk. δέρω «flay», OE teran «tear», etc., IE *der-. Walde-P. 1.797 ff.'\"},\n        {\"src\": \"CHEUNG\", \"where\": \"s.v. *dar2\", \"stance\": \"supports\", \"note\": \"'*dar2 «to tear, split» ... «PIE *der- «to tear, split» = LIV: 119 f. | Pok.: 206 ff.'; IE cognates Gr. δέρω, OCS дьрати, Lith. dirti, Goth. dis-tairan, Engl. to tear.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"dar 1, dareta; nîš-dar\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Young Avestan ¹dar- 'to split' is well attested: Bartholomae col. 689 gives 'j. ¹dar- V. «spalten». Praes. 7 darədar-, 11 dərənā-, 30 (Iter.) dāraya-, PPfP. dərəta-, Inf. *dərənąm', comparing ai. dr̥ṇāti, gr. δέρω, Pahl. darrītan, NP darīdan. So 'dar 1' (Nourai's homograph number for the verb) and the participle dərəta- are correct. The second item is the problem: Av. niš.dar- is not a noun but the same verb with the preverb niš- 'out', 'herausziehen, reissen aus' (Vd. 18.38 'yaθa vəhrkō ... barəθryāt̰ haca puθrəm niš.darənąiryāt̰' — 'as if a wolf tore the child out of the womb'), and Buck p.565 lists it exactly so: 'Av. niš-dar- «tear out» (Barth. 689)'. Nourai's gloss 'a sharp tool for tearing' reads the later Persian noun nēštar 'lancet' back into the Avestan verb; the niš- here is the preverb, not nēš 'point, sting' (his ☞Někš cross-reference).\",\n          \"derivation_fa\": \"ستاک اوستایی ¹dar- «شکافتن، دریدن» به‌خوبی گواهی شده است؛ بارتولمه (ستون ۶۸۹) صورت‌های حال darədar- و dərənā-، ستاک سببی dāraya- و صفت مفعولی dərəta- را می‌آورد و آن را با سنسکریت dr̥ṇāti و یونانی δέρω و پهلوی darrītan و فارسی «دریدن» می‌سنجد؛ پس «dar ۱» و «dareta» درست است. اما nīš-dar در اوستا اسم و ابزار نیست، بلکه همان فعل با پیشوند niš- «بیرون» است، یعنی «بیرون کشیدن، دریدن و بیرون آوردن» (وندیداد ۱۸٫۳۸). بنابراین معنایی که نورایی برای آن نوشته («ابزار تیزِ دریدن») نادرست است و در واقع معنای «نیشتر» فارسی نو را به واژهٔ اوستایی نسبت داده است. حکم: بخش نخست پذیرفتنی و بخش دوم با احتیاط.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/der-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:206\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 217: 'av. darədar- (s. oben) «spalten», Inf. dərənąm (: ai. dr̥ṇāti), Iter. dāraya-, Partiz. dərətō (= ai. dr̥tá-)'.\"},\n            {\"ref\": \"SYN:565\", \"status\": \"partial\", \"note\": \"SYN.txt l.14289ff (printed p.565): §9.27 'Av. dar- : Skt. dr̥- «burst, tear, split»' and §9.28 'Skt. dr̥- «burst, tear» Av. niš-dar- «tear out» (Barth. 689)'. Buck has the forms but glosses niš-dar- as a verb 'tear out', not as a tool.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"col. 689 s.v. ¹dar-\", \"stance\": \"partial\", \"note\": \"'j. ¹dar- V. «spalten» ... mit niš «herausziehen, reissen aus -» (Abl.): yaθa vəhrkō ... puθrəm niš.darənąiryāt̰ «als ob ein Wolf das Kind aus dem Mutterleib herausrisse» V.18.38'. The compound exists, but as a verb; 'Pü.: darrītan', 'np. darīdan'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"s.v. *dar2 'to tear, split'\", \"stance\": \"supports\", \"note\": \"'*AVESTAN: YAv. dar- «to tear» || (+ *aua-) «to tear down» || (+ *pari-) «to tear off»' — the Avestan verb with preverbs, PIE *der-.\"},\n            {\"src\": \"HRN\", \"where\": \"no. 1067, p. ~213\", \"stance\": \"contradicts\", \"note\": \"On the second word: 'nēš «Spitze, Stachel; Gift», nēstar «Lanzette». ai. vergl. nekṣana- «spitzer Stab, Spiess», zu √nekṣ-, nikṣati «durchbohren»' — Horn puts nēštar under nēš, not under dar-.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"darîtan; dart; něš-tar\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Two of the three words are exactly right. (a) MP darrītan/darr- (Book Pahlavi heterogram SDKWN-tn' < Aram. √sdq, phonetic dl-ytn') 'to split, tear' — MacKenzie p.25 'darrīdan, darr- ... split, tear'; Nyberg II 1349 'drītan [SDKWN-tn'] drīn- to tear to pieces, to slit ... Av. (689) ¹dar- ... BP also darrītan darr- = NP dar(r)īdan'. Nourai's 'darîtan' is the older reading of the same word. (b) MP dard 'pain' (Nyberg 'dart [dlt'] pain, illness ... MPrthPrs drd, Paz. NP dard'; MacKenzie 'dard [dlt' | M drd, N ~] pain'); Nourai's 'dart' is Horn's/Pokorny's book-script transliteration (POK p.208 'vgl. mpers. dart «geplagt», npers. derd «Schmerz»'). Cheung derives it from Ir. *darH- 'to have pain' < *dl̥-eH₁-, 'an old eH₁-formation of *dar²' — i.e. the same root, so the arrow holds. (c) nēš-tar 'lancet' does NOT contain dar-: Horn no.1067 and Hübschmann §129 analyse NP nēš 'point, sting' (Ir. *naikša-, cf. Skt. nikṣ- 'pierce', nekṣana- 'piercing instrument') plus the old instrument suffix -tar/-tra-; Hübschmann adds that Armenian nštir, nstrak 'lancet' presupposes a Pahlavi *nēštir. MacKenzie has no nēštar at all. Worst-word verdict: disputed.\",\n          \"derivation_fa\": \"دو واژه از سه واژه درست است. یکم، فارسی میانهٔ darrītan/darr- (هزوارش SDKWN-tn'، آوانگاشت dl-ytn') «شکافتن، دریدن» که مکنزی و نیبرگ هر دو آن را ثبت کرده و به اوستایی dar- بازگردانده‌اند؛ صورت «darîtan» نورایی همان است. دوم، dard «درد» که نیبرگ آن را dart [dlt'] و برابر پارتی/فارسی میانهٔ مانوی drd می‌آورد؛ چونگ آن را از ایرانی *darH- «درد داشتن» می‌داند که خود گسترش لارنگالی همان ریشهٔ *dar «دریدن» است، پس پیوند با ریشه برقرار است. سوم، «نیشتر» از dar- نیست: هرن (شمارهٔ ۱۰۶۷) و هوبشمان (§۱۲۹) آن را nēš «نوک، نیش» (ایرانی *naikša-، هم‌ریشه با سنسکریت nikṣ-) به‌علاوهٔ پسوند ابزارساز کهن -tar می‌دانند و هوبشمان می‌افزاید که وام‌واژهٔ ارمنی nštir صورت پهلوی *nēštir را پیش‌فرض می‌گیرد. حکم: در مجموع پژوهش امروزی این بند را رد می‌کند، هرچند دو واژهٔ نخست پذیرفته است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%AF%D8%B1%DB%8C%D8%AF%D9%86\",\n            \"https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D8%AF\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"SYN:565\", \"status\": \"partial\", \"note\": \"SYN p.565 §9.28 has Av. niš-dar- 'tear out' and the IE *der- family, but Buck gives no Pahlavi forms at all and nothing on nēštar; it supports darrītan/dard only indirectly through Av. dar-.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"p. 25 s.v. darrīdan, dard\", \"stance\": \"supports\", \"note\": \"'darrīdan, darr- [SDKWN-tn' < A √sdq; dl-ytn' | N ~] split, tear'; 'dard [dlt' | M drd, N ~] pain. ~ōmand ill, suffering'. No entry nēštar.\"},\n            {\"src\": \"NYB\", \"where\": \"Glossary nos. 1349, 1203\", \"stance\": \"supports\", \"note\": \"'drītan [SDKWN-tn'] drīn- to tear to pieces, to slit 502 ... — Av. (689) ¹dar-, pres. dərənā-. ... BP also darrītan darr- = NP dar(r)īdan darr-'; 'dart [dlt'] pain, illness ... — MPrthPrs drd, Paz. NP dard'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"s.v. *darH 'to have pain'\", \"stance\": \"supports\", \"note\": \"'MMP drd, BMP dr /dard/ «pain, illness» ... The Ir. forms above are probably etymologically related to the forms of *dar2: *darH would go back to an old eH₁-formation of *dar2.'\"},\n            {\"src\": \"HUB\", \"where\": \"p. 236 §129\", \"stance\": \"contradicts\", \"note\": \"'np. nēš «Spitze, Stachel», nēštar «Lanzette», skr. nekṣana-' listed among the reflexes of idg. kʰ = iran. š; p.104 ad no.1067: 'arm. LW. nštir, nstrak «Lanzette» (das ein phl. *nēštir voraussetzt)'. The -tar is not dar-.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"darîdan «دریدن»; dard «دَرد»; nîšdar «نیشدر» (extra: نیشتر)\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"darīdan 'to tear' and dard 'pain' are impeccable. Mo'in's footnote 8 at Borhan-e Qate' p.848 says: 'از: در + یدن (پسوند مصدری) از ریشهٔ اوستایی dar- (شکافتن)، پهلوی darītan، هندی باستان dar-, dr̥ṇāti ... در اوراق مانوی پهلوی dryd (دریدن) ... کردی dirandin ... ورک: هوبشمان ۲۹۵'. Hübschmann p.62 no.562 works out the morphology: OP *dartanaiy, pres. *dr̥nāmiy → MP *dartan : *dirram → darram, with the infinitive rebuilt on the present, darrīdan (darīdan); the geminate -rr- comes from the n-present *dr̥nā-. dard < MP dard < Ir. *dar-ta- (Horn no.550 'derd «Schmerz» ... phlv. dart, dartak «geplagt»'). The third word is the trouble: the book prints 'nîšdar : a tool for cutting  نیشدر ( نیشتر )' — the JSON is faithful to the page, and نیشدر is Nourai's own analytic respelling of the real Persian word نیشتر nēštar 'lancet', which Horn 1067 and Hübschmann §129 derive from نیش nēš 'point, sting' + the instrument suffix -tar, not from دریدن.\",\n          \"derivation_fa\": \"«دریدن» و «درد» بی‌گمان از این ریشه‌اند. معین در حاشیهٔ برهان قاطع (ص ۸۴۸، یادداشت ۸) می‌نویسد: «از: در + یدن (پسوند مصدری) از ریشهٔ اوستایی dar- (شکافتن)، پهلوی darītan ...»؛ و هوبشمان (ص ۶۲، شمارهٔ ۵۶۲) راه تحول را چنین می‌کشد: پارسی باستان *dartanaiy با ستاک حال *dr̥nāmiy، فارسی میانه *dartan : *dirram، سپس darram و مصدر نوساختهٔ «دریدن» بر پایهٔ ستاک حال؛ دوگانگی «رّ» بازماندهٔ همان ستاک حالِ n-دار است. «دَرد» نیز از فارسی میانهٔ dard از ایرانی *dar-ta- است (هرن، شمارهٔ ۵۵۰). اما واژهٔ سوم درست نیست: کتاب «نیشدر (نیشتر)» چاپ کرده و «نیشدر» صورت تحلیلی و ساختگی خودِ نورایی است؛ واژهٔ راستین «نیشتر» است که هرن و هوبشمان آن را «نیش» + پسوند ابزارساز «-تر» می‌دانند، نه «نیش» + «در (دریدن)». پس این بند در بخش سوم مردود است. (خطای چاپ یا خوانش در کار نیست؛ استخراج با صفحهٔ چاپی می‌خواند.)\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%AF%D8%B1%DB%8C%D8%AF%D9%86\",\n            \"https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D8%AF\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:848\", \"status\": \"supports\", \"note\": \"BQT_v2_pages.txt leaf 308 = printed p.848 (offset +540, fixed by the 'بقیه از صفحهٔ ۸۳۸' note on leaf 299 = p.839). Mo'in's fn. 8: 'از: در (ه.م.) + یدن (پسوند مصدری) از ریشهٔ اوستایی dar- (شکافتن)، پهلوی darītan، هندی باستانی dar-, dr̥ṇāti ... در اوراق مانوی پهلوی dryd (دریدن). Henning, A list of Middle Persian ... p.82 ... ورک: هوبشمان ۲۹۵'.\"},\n            {\"ref\": \"POK:206\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 217 (p.206): 'npers. Inf. dirīδan, darīδan, jüd.-pers. darīn-išn'; and on p.208 (leaf 219) 'vgl. mpers. dart «geplagt», npers. derd «Schmerz» (Wood KZ. 45, 70)'.\"},\n            {\"ref\": \"SYN:565\", \"status\": \"partial\", \"note\": \"Buck p.565 gives the IE *der- 'tear' family (ChSl. dirati, OE teran, Skt. dr̥-, Av. dar-) but lists no New Persian forms.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"p. 62 no. 562\", \"stance\": \"supports\", \"note\": \"'Ap. *dartanaiy, pr. *dr̥nāmiy (skr. dr̥ṇāmi) wurde zu mp. *dartan : *dirram (vgl. bal. dirag, dinag), daraus *dartan : darram und mit Neubildung des Inf. nach dem Praesens: darrīdan (darīdan) : darram (daram).'\"},\n            {\"src\": \"HRN\", \"where\": \"no. 550, p. 122\", \"stance\": \"supports\", \"note\": \"'derd «Schmerz». Wohl zu ai. 1 √dar- «spalten, zerreissen, bersten machen»; vergl. got. tairan, ahd. zeran, nhd. zehren. phlv. dart (vd. 20), dartak «geplagt» (AV.)'.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"s.v. دریدن and درد\", \"stance\": \"supports\", \"note\": \"دریدن: 'From Middle Persian (SDKWN-tn', dl-ytn' /darrīdan, darr-/, «to split, to tear») ... from Proto-Indo-European *der-'. درد: 'From Middle Persian dlt' (dard), from Proto-Iranian *dar-ta- «torn, burning, pain», from Proto-Iranian *darH-, from either PIE *der- ... or *delh₁-, the latter which Cheung considers to be related to the former.'\"},\n            {\"src\": \"HRN\", \"where\": \"no. 1067\", \"stance\": \"contradicts\", \"note\": \"For the third word only: 'nēš «Spitze, Stachel»; nēstar «Lanzette». ai. vergl. nekṣana- «spitzer Stab, Spiess», zu √nekṣ-, nikṣati «durchbohren»'. Np. nēstar already in Firdausī I, 46, 214.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Avestan\",\n          \"words\": \"dereta; deretô\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Av. dərəta- is the past participle of ¹dar- 'to split' (Bartholomae col. 689 'PPfP. dərəta-'; Pokorny p.206 'Partiz. dərətō (= ai. dr̥tá-)'; Mann IEC 165 s.v. drtos: 'Av. dərəto (1) «cut, mown»'), so 'deretô : cut, mown' is exactly right and is Nourai's second gloss. The first gloss, 'dereta : cuts, harvests', is a finite verb that Avestan does not attest in that sense; the harvest meaning comes only from Horn no.556, who cites 'aw. vergl. dərəta-, a-dərəta- (yava-) «geschnittenes, gemähtes (sc. Korn)»' — the compound a-dərəta- yava- 'unmown grain' (Vd.). So the node is a participle used twice, once with an over-specific verbal gloss.\",\n          \"derivation_fa\": \"dərəta- در اوستا صفت مفعولی ستاک dar- «شکافتن، بریدن» است؛ بارتولمه آن را PPfP همین فعل می‌داند و پوکورنی (ص ۲۰۶) آن را برابر سنسکریت dr̥tá- می‌گذارد و مان (ص ۱۶۵ ذیل drtos) معنای «بریده، درو شده» را برایش می‌آورد. پس «deretô: بریده، درو شده» درست است. اما «dereta: می‌بُرد، درو می‌کند» به‌عنوان فعل صرف‌شده در اوستا گواهی ندارد؛ معنای «درو» تنها از ترکیب a-dərəta- yava- «غلهٔ درونشده» می‌آید که هرن (شمارهٔ ۵۵۶) نقل کرده است. حکم: با احتیاط پذیرفتنی؛ یک صورت با دو معنا آمده و معنای نخست دقیق نیست.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/der-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:208\", \"status\": \"partial\", \"note\": \"Pokorny p.208 (POK_01.txt leaf 219-220) is the der-eu- section: 'Mit u-Formans von der leichten (der-eu-) und schweren Basis (derə-u-, *dr̥-u-) «zerreissen, (das Land) umbrechen, aufreissen, ernten» ... Mpers. drūn, drūdan «ernten»'. It says nothing about dərəta-; the participle is on p.206 instead. The 'harvest' idea is on p.208 but attached to the u-stem, not to dərəta-.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"col. 689 s.v. ¹dar-\", \"stance\": \"supports\", \"note\": \"'Praes. 7 darədar-, 11 dərənā-, 30 (Iter.) dāraya-, — PPfP. dərəta-, Inf. *dərənąm' — the participle exists; the gloss there is 'spalten', not 'harvest'.\"},\n            {\"src\": \"IEC\", \"where\": \"p. 165 s.v. drtos (1)\", \"stance\": \"supports\", \"note\": \"'drtos (1) «torn, flayed, cut, worn, ground». Cf. drtis, dero, etc. — Av. dərəto (1) «cut, mown»; Gk. dartós, dratós «flayed»' — Nourai's gloss 'cut, mown' is copied verbatim from Mann.\"},\n            {\"src\": \"HRN\", \"where\": \"no. 556, p. 124\", \"stance\": \"supports\", \"note\": \"'durūden «ernten» ... aw. vergl. dərəta-, a-dərəta- (yava-) «geschnittenes, gemähtes (sc. Korn)»; pāz. drūdan «ernten»' — Horn is where the harvest gloss of dərəta- comes from.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"dero «دِرو»; dorŭdan «دُرودن»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"NP durūdan / deraw- 'to reap, mow' and the verbal noun deraw 'harvest' are real and old (Firdausī I, 18, 12; 22, 49; Judaeo-Persian; Pāzand drūdan), and they do belong to the *der- family — but not through the participle dərəta- drawn in the chart. MacKenzie p.28: 'drūdan, *drūn- [HCDLWN-tn' < A √ḥṣd | M dwr-, N durūdan, diraw-] reap, mow'; Cheung sets up Ir. *drauH- 'to cut (down), mow, reap' (MMP dwr-, Chwar. δrw-, NP durūdan/dirav-, Kurd. dirūn, Wakhi draw-) and adds 'This root is attested in IIr. only, it might be an enlarged root of IE *der- «to tear, split» (*dar²), or at least contaminated with it', citing Pok. 208 f. Hübschmann p.62 no.556 reaches the same conclusion: 'Np. durūdan, diravīdan «ernten, mähen, schneiden», praes. diravam weist auf eine Wurzel iran. drū', and he expressly doubts the alternative link to Gk. δρέπω. So the ancestor is the u-extension *dr(a)u-, and Nourai's arrow from dərəta- is a simplification: same root family, wrong immediate parent. Nourai's vocalisation 'dorŭdan' should be durūdan/durōdan.\",\n          \"derivation_fa\": \"«درو» و «درودن» (با ستاک حال «درو-») واژه‌هایی کهن‌اند: در شاهنامه، در متن‌های یهودی‌فارسی و در پازند drūdan دیده می‌شوند و از فارسی میانهٔ drūdan (هزوارش HCDLWN-tn') می‌آیند؛ مکنزی معنای «درو کردن، دِرویدن» را برایش می‌دهد. اما پدرِ بی‌واسطهٔ آن dərəta- نیست: چونگ ریشهٔ ایرانی *drauH- «بریدن، درو کردن» را بازسازی می‌کند و می‌گوید این ریشه تنها در هندوایرانی گواهی دارد و «شاید گسترشی از ریشهٔ هندواروپایی *der- باشد یا دست‌کم با آن آمیخته باشد» (با ارجاع به پوکورنی ۲۰۸). هوبشمان نیز (ص ۶۲، شمارهٔ ۵۵۶) از ستاک حال «دِرَوَم» نتیجه می‌گیرد که ریشهٔ ایرانیِ drū در کار است. پس ادعای نورایی در کلیت (هم‌ریشگی با «دریدن») درست است، ولی پیکان نمودار از صفت مفعولی dərəta- کشیده شده که دقیق نیست؛ افزون بر این آوانگاشت درست durūdan است نه dorŭdan.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D9%88%D8%AF%D9%86\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:208\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 220, just above the '209' running number, i.e. printed p.208: 'Mit u-Formans von der leichten (der-eu-) und schweren Basis (derə-u-, *dr̥-u-) «zerreissen, (das Land) umbrechen, aufreissen, ernten» ... Mpers. drūn, drūdan «ernten»'.\"},\n            {\"ref\": \"HRN:124\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 146 = printed p.124: 'no. 556. durūden «ernten», Praes. dirawem, dirawīden, durūd «Ernte», ... aw. vergl. dərəta-, adərəta- (yava-) «geschnittenes, gemähtes (sc. Korn)»; pāz. drūdan «erndten». kurd. dirūn, dirūtin «erndten»'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"p. 28 s.v. drūdan\", \"stance\": \"supports\", \"note\": \"'drūdan, *drūn- [HCDLWN-tn' < A √ḥṣd | M dwr-, N durūdan, diraw-] reap, mow.'\"},\n            {\"src\": \"CHEUNG\", \"where\": \"s.v. *drauH\", \"stance\": \"partial\", \"note\": \"'*drauH «to cut (down), mow, reap» ... NP durūdan/dirav- ... © This root is attested in IIr. only, it might be an enlarged root of IE *der- «to tear, split» (*dar2), or at least contaminated with it. *PIE — = LIV: 129 | Pok.: 208 f.' — same family, different immediate preform than dərəta-.\"},\n            {\"src\": \"HUB\", \"where\": \"p. 62 no. 556\", \"stance\": \"partial\", \"note\": \"'Np. durūdan, diravīdan «ernten, mähen, schneiden» (Fird. I, 18, 12; 22, 49), praes. diravam weist auf eine Wurzel iran. drū. Will man das Wort zu gr. δρέπω stellen, muss man annehmen ... Ich halte aber diese Annahme für bedenklich.'\"},\n            {\"src\": \"ARY\", \"where\": \"pdf pp. 274-275 s.v. درو، درودن، درویدن\", \"stance\": \"supports\", \"note\": \"Aryanpur's entry gives Avestan/Old Persian/Pahlavi/Kurdish/Baluchi/Pashto cognates and note 1: 'این واژه با واژهٔ «دریدن» همریشه است. بازگشت به: دریدن' (cross-refs Borhan-e Qate' p.841 and Dehkhoda).\"},\n            {\"src\": \"BQT\", \"where\": \"p. 843 (leaf 303) fn. 4 s.v. درودن\", \"stance\": \"supports\", \"note\": \"'از: درو «هوبشمان ۹۵» + دن (پیوند مصدری)؛ پازند drūdan؛ کردی dirûtin, dirûn (درو کردن), dirûn (درو)'.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Persian\",\n          \"words\": \"dŭl «دول»\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"NP دول dūl/dōl 'leather bucket, skin for drawing water' is a Semitic loan, not an Iranian inheritance. It is already Middle Persian dōl 'bucket; (the zodiac sign) Aquarius', borrowed from Aramaic/Syriac dawlā (absolute dōl), ultimately Proto-Semitic (Akkadian dalū/dūlu 'bucket', Hebrew dəlī, Arabic dalw دلو); Old Armenian doyl is the same loan, and Persian usage was reinforced by Arabic dalw in the Islamic period. Mo'in says the same in his footnote to Borhan-e Qate' p.900 s.v. دول ('= دلو (عر)'), which is precisely the NOTE Nourai himself prints. Phonologically an inherited *dr̥ti- could never yield dūl (an inherited *dr̥- gives dar-/dard, cf. dard; and -l for inherited -r/-t is impossible). Nourai's only authority is Mann, who lists 'Per. dūl «water-skin»' under drtis, and that entry of Mann's is simply an error — no Iranian dictionary follows it.\",\n          \"derivation_fa\": \"«دول» به معنای «دَلو، مشک آب‌کشی» وام‌واژهٔ سامی است نه میراث ایرانی. این واژه در همان فارسی میانه به‌صورت dōl «دلو؛ برج دلو» دیده می‌شود و از آرامی/سریانی dawlā (صورت مطلق dōl) گرفته شده که خود به سامی آغازین بازمی‌گردد (اکدی dalū/dūlu، عبری dəlī، عربی دَلو)؛ ارمنی کهن doyl نیز همین وام است و در دورهٔ اسلامی کاربرد آن با «دَلو» عربی تقویت شده است. معین در حاشیهٔ برهان قاطع (ص ۹۰۰ ذیل «دول») همین را می‌نویسد: «= دلو (عر)» — یعنی همان نکته‌ای که خود نورایی هم در پانوشت نمودار آورده است. از نظر آوایی نیز *dr̥ti- هندواروپایی هرگز در فارسی «دول» نمی‌شود (بازتاب آن «درد» گونه است، و «ل» در برابر «ر/ت» موروثی ناممکن است). تنها مأخذ نورایی مان است که «Per. dūl» را زیر drtis آورده، و این مدخل مان خطاست. حکم: پژوهش امروزی ادعای نورایی را رد می‌کند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%AF%D9%88%D9%84\",\n            \"https://en.wiktionary.org/wiki/%D8%AF%D9%84%D9%88\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IEC:165\", \"status\": \"supports\", \"note\": \"Mann does say it: IEC.txt leaf 105 (p.165) s.v. drtis: 'Skt. drtih «skin»; Per. dül «water-skin»; Gk. dársis «skinning; milling»; Go. ga-taürþs «destruction»'. The citation is accurate; the claim in it is not.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BQT\", \"where\": \"p. 900 (leaf 360) s.v. دول, Mo'in fn. 6\", \"stance\": \"contradicts\", \"note\": \"Headword 'دول = با نون/الف مجهول بروزن غول، دلو آب‌کشی را گویند'; footnote: '= دلو (عر) = سریانی ... = دلو (عر)'. Mo'in makes it the Arabic/Syriac word.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"s.v. دول (Persian) and دلو (Arabic)\", \"stance\": \"contradicts\", \"note\": \"دول: 'From Middle Persian (dōl, «bucket; Aquarius») of Semitic origin, compare Arabic دلو (dalw), Classical Syriac ܕܰܘܠܳܐ (dawlā) (absolute ܕܘܿܠ (dōl)), Akkadian dalū, dūlu «bucket». Akin to Old Armenian դոյլ (doyl).' دلو: 'From Proto-Semitic ... as well as the loanwords from Semitic Old Armenian doyl and Persian دول (dul, «bucket»).'\"},\n            {\"src\": \"POK\", \"where\": \"pp. 206-211\", \"stance\": \"silent\", \"note\": \"Pokorny's der- article lists no Persian dūl anywhere; the Iranian material is limited to av. darədar-, mpers. drūdan, npers. darīdan, derd.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Avestan\",\n          \"words\": \"darěna\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Av. darəna- is a real word, but its meaning and its root are disputed. Bartholomae col. 693 enters it as 'j. darəna-, darana- n. 1) «Befestigung» (nur Komp.); 2) «Aufenthalt»; 3) «Aufenthaltsort, Wohnsitz, Schlupfwinkel»' (Yt 10.38, of cattle dragged off to the lairs of the mithra-breakers) and derives it from ³dar- 'to hold' (cf. Skt. dhāraṇa- 'holding'), adding the pointed remark 'Anders bei Horn NpEt.' Horn no.560 is the other side: 'aw. darəna- «Thal, Schlucht»', which is the gloss Nourai copies. Hübschmann p.62 no.560 keeps it conditional: 'Wenn zd. darəna- zur Wzl. skr. dar «bersten, spalten» gehört (got. gatairan, hd. zehren, zerren), wäre es von got. dal = hd. Thal zu trennen.' Modern Wiktionary likewise calls the whole group 'Uncertain'. So the arrow root→darəna- follows Horn against Bartholomae; defensible, not settled.\",\n          \"derivation_fa\": \"darəna- در اوستا واژه‌ای واقعی است، اما هم معنا و هم ریشه‌اش محل اختلاف است. بارتولمه (ستون ۶۹۳) آن را «استحکام؛ اقامتگاه، کمینگاه» می‌داند و به ستاک سومِ dar- «نگاه داشتن» (هم‌ریشه با سنسکریت dhāraṇa-) بازمی‌گرداند و صریحاً می‌افزاید «نزد هرن دیگرگونه است». هرن (شمارهٔ ۵۶۰) همان معنایی را می‌دهد که نورایی آورده: «دره، تنگه». هوبشمان (ص ۶۲) محتاطانه می‌نویسد: «اگر darəna- اوستایی به ریشهٔ سنسکریت dar «شکافتن» بازگردد، باید آن را از dal گوتی/Tal آلمانی جدا دانست.» ویکی‌واژه نیز این خانواده را «نامطمئن» می‌خواند. پس نورایی جانب هرن را گرفته است؛ ادعا با احتیاط پذیرفتنی است، نه قطعی.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D9%87\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:206\", \"status\": \"not_found\", \"note\": \"Read the whole der- article, POK_01.txt leaves 217-223 (printed pp. 206-211): Pokorny nowhere lists Avestan darəna- or NP darra. His Iranian material is av. darədar-, dərənąm, dāraya-, dərətō, mpers. drūdan, npers. darīdan/derd.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"col. 693 s.v. darəna-\", \"stance\": \"contradicts\", \"note\": \"'j. darəna-, darana- n. 1) «Befestigung» (nur Komp.) 2) «Aufenthalt» 3) «Aufenthaltsort, Wohnsitz, Schlupfwinkel» ... KompE. — Zum V. ³dar-. — ai. dhāraṇa- n. «Halten». — ¹) Anders bei Horn NpEt.'\"},\n            {\"src\": \"HUB\", \"where\": \"p. 62 no. 560\", \"stance\": \"partial\", \"note\": \"'Wenn zd. darəna- zur Wzl. skr. dar «bersten, spalten» gehört (got. gatairan, hd. zehren, zerren), wäre es von got. dal = hd. Thal zu trennen.' — accepts the connection only conditionally.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"s.v. دره (Persian), Etymology\", \"stance\": \"partial\", \"note\": \"'Uncertain, possibly from Proto-Indo-European *der- («to tear, split») or *dʰel(h₂)- («valley») ... Cognate with Avestan 𐬛𐬀𐬭𐬈𐬥𐬁 (darenā) and Sogdian δar-.'\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Persian\",\n          \"words\": \"darreh «درّه»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"NP darra 'valley, gorge' (with geminate -rr-, like darrīdan) is standardly connected with Av. darəna- and so with dar- 'to split' — 'the split in the earth'. Mo'in's footnote 9 at Borhan-e Qate' p.845 s.v. دره gives exactly that: 'اوستا daranū- (دره، گردنه) ... ورک: هوبشمان' with Gilaki darreh and other dialect forms. Horn no.560 has 'derre «Thal, Schlucht»; aw. darəna- «Thal, Schlucht»'. Nyberg's glossary supplies the missing Middle Persian link: 'darrak [drky] ravine, or rock (Parthian equivalent vēm) — NP darrah «a valley between hills»' (Hajjiabad inscription), so NP darra continues MP darrak. The reservation is the same as at node 7: Bartholomae reads the Avestan word as 'lair, stronghold' from dar- 'to hold', and Wiktionary calls the etymology uncertain, mentioning a rival *dʰel(h₂)- 'valley'.\",\n          \"derivation_fa\": \"«درّه» با «رّ» مشدد — درست مانند «دریدن» — به‌طور معمول با darəna- اوستایی و از آن راه با ریشهٔ dar- «شکافتن» پیوند داده می‌شود، یعنی «شکافِ زمین». معین در حاشیهٔ برهان قاطع (ص ۸۴۵، یادداشت ۹) همین را می‌نویسد: «اوستا daranū- (دره، گردنه) ... ورک: هوبشمان»، و صورت‌های گویشی مانند گیلکی darreh را می‌افزاید؛ هرن (شمارهٔ ۵۶۰) نیز «دره: وادی، تنگه؛ اوستایی darəna-» دارد. نیبرگ حلقهٔ میانی را به دست می‌دهد: در کتیبهٔ حاجی‌آباد فارسی میانه darrak «دره یا صخره» (برابر پارتی vēm) آمده و او آن را با «درّهٔ» فارسی نو یکی می‌داند. اما همان تردید بند پیشین برجاست: بارتولمه واژهٔ اوستایی را «کمینگاه، استحکام» از ستاک dar- «نگاه داشتن» می‌داند و ویکی‌واژه ریشه‌شناسی را نامطمئن می‌خواند. حکم: با احتیاط پذیرفتنی.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D9%87\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:845\", \"status\": \"supports\", \"note\": \"BQT_v2_pages.txt leaf 305 = printed p.845 (offset +540). Headword 'دره = بفتح اول و تشدید ثانی ... گشادگی میان دو کوه را گویند'; Mo'in's fn. 9: 'اوستا daranū- (دره، گردنه) ... و رک: هوبشمان ایضاً ... در فارسی بمعنی وادی عربی آید. رک: دائرةالمعارف اسلام: دره؛ گیلکی darreh'.\"},\n            {\"ref\": \"HUB:62\", \"status\": \"partial\", \"note\": \"HUB.txt leaf 73 = printed p.62, no. 560: 'Wenn zd. darəna- zur Wzl. skr. dar «bersten, spalten» gehört ..., wäre es von got. dal = hd. Thal zu trennen.' Hübschmann grants the derivation only as a hypothesis.\"},\n            {\"ref\": \"HRN:124\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 146 = printed p.124, no. 560: 'derre «Thal, Schlucht». aw. darəna- «Thal, Schlucht»; Δάρνη, Ptolem. 6, 1 (Spiegel, ZDMG. 32, 721).'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"NYB\", \"where\": \"Glossary no. 1202 s.v. darrak\", \"stance\": \"supports\", \"note\": \"'darrak [drky] ravine, or rock HajB: 7. 13, Prth. equivalent vēm (q.v.). — NP darrah «a valley between hills». V. Nyberg, Christensen Vol., p. 69.' — gives the Middle Persian stage the chart omits.\"},\n            {\"src\": \"BRT\", \"where\": \"col. 693 s.v. darəna-\", \"stance\": \"contradicts\", \"note\": \"Assigns darəna- to ³dar- 'halten' with the sense 'Befestigung / Aufenthaltsort, Schlupfwinkel', noting explicitly 'Anders bei Horn NpEt.'\"},\n            {\"src\": \"Wiktionary\", \"where\": \"s.v. دره (Persian)\", \"stance\": \"partial\", \"note\": \"'Uncertain, possibly from PIE *der- «to tear, split» or *dʰel(h₂)- («valley») ... Cognate with Avestan darenā and Sogdian δar-.'\"},\n            {\"src\": \"ARY\", \"where\": \"ARY_pages.txt, no headword entry found\", \"stance\": \"silent\", \"note\": \"Grepped 'دره' across ARY_pages.txt; the hits are inside other articles (e.g. the note 'چم این واژه در زبان ارمنی: آبکند، دره' under زور). Aryanpur has no separate درّه article.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Germanic\",\n          \"words\": \"teran\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The Germanic strong verb *teraną 'to tear' (class IV) continues PIE *der- with the regular Grimm shift *d > Gmc. t: Gothic dis-tairan, ga-tairan 'tear apart, destroy', Old English teran, Old High German zeran, fir-zeran, MHG (ver)zern > NHG (ver)zehren. Pokorny p.207 has 'got. dis-tairan (= gr. δέρω) «auseinanderreissen», ga-tairan «zerreissen, zerstören», ags. teran «zerreissen», ahd. zeran, fir-zeran'. Watkins der-2 §1: 'Germanic *teran in Old English teran, to tear: TEAR¹.' Nourai's box is labelled 'Germanic' but the form he prints, teran, is the Old English one; Proto-Germanic would be *teraną.\",\n          \"derivation_fa\": \"فعل قوی ژرمنی *teraną «دریدن» بازماندهٔ مستقیم ریشهٔ *der- هندواروپایی است؛ «د» آغازین بر پایهٔ قانون گریم در ژرمنی به «ت» بدل شده است: گوتی dis-tairan و ga-tairan «از هم دریدن، ویران کردن»، انگلیسی کهن teran، آلمانی علیای کهن zeran و fir-zeran که به zehren/verzehren آلمانی امروز رسیده است. پوکورنی (ص ۲۰۷) و واتکینز (ذیل der-2) هر دو همین زنجیره را می‌آورند. تنها نکته آن است که صورت چاپ‌شده در جعبهٔ «ژرمنی»، یعنی teran، در حقیقت صورت انگلیسی کهن است و ژرمنی آغازین *teraną می‌شود. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/tear\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. der-2: 'To split, peel, flay ... 1. Germanic *teran in Old English teran, to tear: TEAR¹. ... [Pok. 4. der- 206.]'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 207\", \"stance\": \"supports\", \"note\": \"'got. dis-tairan (= gr. δέρω) «auseinanderreissen», ga-tairan «zerreissen, zerstören», ags. teran «zerreissen», ahd. zeran, fir-zeran «zerreissen, zerstören»'.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. tear (v.)\", \"stance\": \"supports\", \"note\": \"'ME. teren, fr. OE. teran, rel. to OS. terian ... OHG. zeran, fir-zeran ... Goth. dis-tairan, ga-tairan ... fr. I.-E. *derə-, *der-, «to rend, divide; to flay»'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 798\", \"stance\": \"supports\", \"note\": \"'Got. dis-tairan (= gr. δέρω) «auseinanderreissen», gatairan «zerreissen, zerstören», ags. teran «zerreissen», ahd. zeran, fir-zeran'.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"English\",\n          \"words\": \"tear 2\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English tear 'to pull apart' (Nourai's 'tear 2', distinguished from the homograph tear 'a drop from the eye', which is from PIE *dakru-) is Middle English tēren, from Old English teran, a class IV strong verb (past tær, participle toren); the modern past tore is built on the old participle and displaced tare in the 17th c. Etymonline: 'from Old English teran «pull apart by force; lacerate» ... from Proto-Germanic *teran ... from PIE root *der- «to split, flay, peel».' No reference is printed on the box; none is needed for so standard a chain.\",\n          \"derivation_fa\": \"فعل انگلیسی tear «دریدن، از هم کندن» (که نورایی آن را «tear ۲» می‌نامد تا از هم‌نویسهٔ tear «اشک» جدا شود؛ آن یکی از ریشهٔ *dakru- است) از انگلیسی میانهٔ tēren و انگلیسی کهنِ teran می‌آید، فعل قوی ردهٔ چهارم با گذشتهٔ tær و صفت مفعولی toren؛ گذشتهٔ امروزی tore در سدهٔ هفدهم بر پایهٔ همان صفت مفعولی ساخته شد و جای tare کهن را گرفت. اتیمانلاین آن را به ژرمنی آغازین *teraną و از آنجا به ریشهٔ *der- بازمی‌گرداند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/tear\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The box carries no reference in the book; checked instead against Etymonline, Klein and Watkins (see consulted).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Etymonline\", \"where\": \"s.v. tear (v.1)\", \"stance\": \"supports\", \"note\": \"'Middle English tēren «destroy by reducing to fragments; tear apart» from Old English teran «pull apart by force; lacerate» (class IV strong verb; past tense tær, past participle toren), from Proto-Germanic *teran ... from PIE root *der- «to split, flay, peel».'\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. tear\", \"stance\": \"supports\", \"note\": \"'tear, tr. and intr. v., to pull apart, rend. — ME. teren, fr. OE. teran ... fr. I.-E. *derə-, *der- ... Cp. derma and words there referred to.'\"},\n            {\"src\": \"AHD\", \"where\": \"index and s.v. der-2\", \"stance\": \"supports\", \"note\": \"Index: 'TEAR¹ der-2'; 'TEAR² dakru-' — confirming Nourai's homograph numbering.\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"Greek\",\n          \"words\": \"der-ma\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Greek δέρμα, gen. δέρματος 'skin, hide' is the -mn̥ noun of δέρω 'I flay' — Watkins: 'Suffixed form *der-mn̥ in Greek derma, skin: -DERM, DERMA¹, -DERMA, DERMATO-; EPIDERMIS.' Pokorny p.207 sets it beside Skt. darmán- 'Zerbrecher' and lists the whole Greek family δέρω, δείρω, δαρτός, δορός 'wineskin', δάρσις 'a flaying', δέρρις 'leather covering', δορά 'hide'. The semantic step is 'what is flayed off' > 'skin'. Nourai's hyphenated 'der-ma' is just his way of showing the suffix.\",\n          \"derivation_fa\": \"واژهٔ یونانی δέρμα (اضافهٔ δέρματος) «پوست» اسمی است که با پسوند *-mn̥ از فعل δέρω «پوست می‌کَنم» ساخته شده است؛ واتکینز آن را «صورت پسوندی *der-mn̥» می‌نامد و پوکورنی (ص ۲۰۷) آن را در کنار سنسکریت darmán- و دیگر هم‌خانواده‌های یونانی δαρτός، δορός «مشک»، δάρσις «پوست‌کنی» و δορά «پوست» می‌آورد. تحول معنایی روشن است: «آنچه کنده می‌شود» ← «پوست». نگارش «der-ma» در نمودار تنها برای نشان دادن پسوند است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/der-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. der-2 §6: 'Suffixed form *der-mn̥ in Greek derma, skin: -DERM, DERMA¹, -DERMA, DERMATO-; EPIDERMIS.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 207\", \"stance\": \"supports\", \"note\": \"'gr. δέρω «häute ab, schinde» ... δορός «Schlauch» ... δάρσις «das Abhäuten» ... δέρος n., δέρμα n., δορά «Fell»'; and 'darmán- m. «Zerbrecher» (: gr. δέρμα n.)'.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. derma\", \"stance\": \"supports\", \"note\": \"'derma ... fr. Gk. δέρμα, «skin», formed with suff. -μα ... from the stem of δέρειν, δείρειν, «to flay» ... which is cogn. with Goth. dis-tairan, OE. teran «to tear».'\"}\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"English\",\n          \"words\": \"derma, -derm, derma; pachyderm\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English derma / -derm / -derma / dermato- are learned borrowings of Greek δέρμα, taken through Modern Latin from the 17th-19th c. medical vocabulary (Klein: 'derma, also derm, n., skin ... ML. derma, fr. Gk. δέρμα'); the combining form -derm is used in blastoderm, epidermis, taxidermy, xeroderma. pachyderm is a 19th-c. borrowing of French pachyderme (Cuvier's zoological class Pachydermata, 1795), from Greek παχύδερμος 'thick-skinned' = παχύς 'thick' + δέρμα; Nourai's ☞Bhengh cross-reference for παχύς is right (PIE *bʰenǵʰ- 'thick, dense'). No reference is printed on the box.\",\n          \"derivation_fa\": \"واژه‌های انگلیسی derma و جزءهای ترکیبی -derm و -derma و dermato- وام‌واژه‌های دانشورانهٔ یونانی δέρμا هستند که از راه لاتین نو در واژگان پزشکی سده‌های هفدهم تا نوزدهم به انگلیسی رسیده‌اند (کلاین ذیل derma) و در blastoderm، epidermis، taxidermy و xeroderma دیده می‌شوند. pachyderm در سدهٔ نوزدهم از فرانسهٔ pachyderme گرفته شده که خود از ردهٔ جانورشناسیِ Pachydermata (کوویه، ۱۷۹۵) و در نهایت از یونانی παχύδερμος «کلفت‌پوست» = παχύς «کلفت» + δέρμα است؛ ارجاع نورایی به ریشهٔ Bhengh برای παχύς درست است (هندواروپایی *bʰenǵʰ- «ستبر، انبوه»). ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/der-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference printed on the box; checked against Klein and Watkins (see consulted).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.vv. derma, -derm, pachyderm\", \"stance\": \"supports\", \"note\": \"'-derm, suff. meaning «skin, covering», as in blastoderm. — Fr. Gk. δέρμα.'; 'pachyderm, n., a thick-skinned animal ... — F. pachyderme, fr. Gk. παχύδερμος, «thick-skinned», which is compounded of παχύς, «thick», and δέρμα, gen. δέρματος, «skin».'\"},\n            {\"src\": \"AHD\", \"where\": \"index s.v. der-2\", \"stance\": \"supports\", \"note\": \"Index lines '-DERM der-2 / DERMA¹ der-2 / -DERMA der-2 / DERMATO- der-2 / EPIDERMIS der-2'; DERMA² is separately assigned to terə-1, i.e. a different word.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Drep, Drop, Drap, Drapses\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *drep-/*drop- 'to tear off, pluck', a p-extension of *der-; nominal *drap-so- 'a piece torn off, cloth, banner'\",\n      \"note\": \"Pokorny p.211 heads exactly this section: 'Mit formantischem -p-: drep-, drop-' inside the der- article, with 'ai. drapi- m. «Mantel, Kleid», drapsá-h m. «Banner (?)» (= av. drafsa- «Fahne, Banner»), lit. drāpanos f. Pl. «Weisszeug, Kleider», lett. drāna «Zeug, Tuch», gallorom. drappus «Tuch»; gr. δρέπω «breche ab, schneide ab, pflücke», δρεπάνη «Sichel»'; and Mann IEC 159 has the headword 'drapsos (drap-) «cloth, cloth-length, sheet»'. So Nourai's four root shapes (Drep, Drop, Drap, Drapses) and the gloss 'a piece of cloth, banner' are taken accurately from his two sources, and the whole group is standardly treated as a p-enlargement of *der-.\",\n      \"note_fa\": \"پوکورنی در ص ۲۱۱، درون همان مقالهٔ der-، بخشی دارد با عنوان «با پسوند -p-: drep-، drop-» که در آن سنسکریت drapi- «ردا، جامه» و drapsá- «درفش (؟)» برابر اوستایی drafsa- «درفش، بیرق»، لیتوانیایی drāpanos «جامه‌ها»، لتونیایی drāna «پارچه»، گالورومی drappus «پارچه» و یونانی δρέπω «می‌چینم، می‌بُرم» آمده است؛ مان نیز (ص ۱۵۹) سرواژهٔ drapsos (drap-) «پارچه، تکه‌پارچه» را دارد. بنابراین هر چهار صورتی که نورایی برای ریشه آورده و نیز معنای «تکه‌پارچه، درفش» درست و برگرفته از همین دو مأخذ است، و این خانواده به‌طور معمول گسترشِ p-دار ریشهٔ *der- شمرده می‌شود.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D9%81%D8%B4\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:211\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 222 (printed p.211): 'Mit formantischem -p-: drep-, drop-: Ai. drapi-h m. «Mantel, Kleid», drapsá-h m. «Banner (?)» (= av. drafsa- «Fahne, Banner»), lit. drāpanos f. Pl. «Weisszeug, Kleider», lett. drāna (wohl *drāp-na) «Zeug, Tuch»; gallorom. drappus «Tuch» ... ist wohl ven.-ill. Lw.'\"},\n        {\"ref\": \"IEC:159\", \"status\": \"supports\", \"note\": \"IEC.txt leaf 102 (printed p.159): 'drapsos (drap-) «cloth, cloth-length, sheet». WP I, 802 — Skt. drapsáh «rag»; Av. drafšo, id.; Per. dirafš, id.; Arm. drawš, id. (fr. Pers.); LLat. drappus (whence It. Fr. Sp.); OE træf «tent»; ON traf «headcloth»; Li. cf. drapanos «clothes».'\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I 802\", \"stance\": \"supports\", \"note\": \"'Mit der Bed. «abgerissenes Stück Tuch, Kleid» ... ai. drapi- m. «Mantel, Kleid», drapsa- m. «Banner» (diese Bed. von Geldner Ved. St. III 57 bestritten) = av. drafsa- «Fahne, Banner», lit. drapanos ... ital. drappo «Tuch», frz. drap «Tuch», drapeau «Fahne».'\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. der-2 §7\", \"stance\": \"partial\", \"note\": \"'7. Perhaps extended root *drep- in the Celtic source (itself borrowed) of Late Latin drappus, cloth (> Old French drap): (DRAB¹), DRAPE, TRAP².' Watkins accepts the extension only tentatively and does not mention the Indo-Iranian banner word.\"},\n        {\"src\": \"SYN\", \"where\": \"p. 396 (§6.12 clothing)\", \"stance\": \"supports\", \"note\": \"'Lith. drapanos (pl.) «clothes» : Skt. drapi- «cloak, mantle», Av. drafša- «banner», ChSl. drapati «scratch, tear», fr. an extension of IE *der- in words for «tear». Here also perh. late Lat. drappus (Fr. drap) «cloth». Walde-P. 1.802.'\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"drafšâ, drafšô\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Young Avestan drafša- m. 'flag, banner' is well attested (Bartholomae: 'j. drafša- m. «Fahne, Banner»: mā ... yaθa gə̄uš drafšō «... wie das Stierbanner ...» Y. 10.14; otherwise of the enemy standards, Yt 1.11, Yt 5.56, Yt 4.3'); Nourai's two shapes are the stem drafša- and the nominative singular drafšō. Bartholomae equates it directly with Skt. drapsá- 'Banner' and NP dirafš, and gives Pahlavi drafš. The word is the *drap-so- noun of the p-extended root, 'the torn-off piece of cloth' > 'flag' — the same nominal type as Lith. drāpanos 'clothes' and Skt. drapi- 'mantle'.\",\n          \"derivation_fa\": \"drafša- در اوستای متأخر به معنای «درفش، بیرق» به‌روشنی گواهی شده است؛ بارتولمه آن را «Fahne, Banner» می‌آورد و شاهدِ gə̄uš drafšō «درفش گاو» (یسنا ۱۰٫۱۴) و نیز کاربردهای آن دربارهٔ درفش دشمنان ایران را نقل می‌کند. دو صورتی که نورایی نوشته، در حقیقت ستاک drafša- و نهادی مفرد drafšō است. بارتولمه آن را مستقیماً برابر سنسکریت drapsá- و فارسی «درفش» می‌گذارد و صورت پهلوی drafš را هم می‌دهد. این واژه اسمِ *drap-so- از ریشهٔ p-دار است، یعنی «تکه‌پارچهٔ کنده‌شده» ← «بیرق»، از همان گونهٔ لیتوانیایی drāpanos و سنسکریت drapi-. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D9%81%D8%B4\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"SYN:396\", \"status\": \"supports\", \"note\": \"SYN.txt l.9883 (printed p.396): 'Lith. drapanos (pl.; sg. rare) «clothes» : Skt. drapi- «cloak, mantle», Av. drafša- «banner», ChSl. drapati «scratch, tear», fr. an extension of IE *der- in words for «tear». Here also perh. late Lat. drappus (Fr. drap) «cloth».'\"},\n            {\"ref\": \"POK:211\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 222 (p.211): 'Ai. drapi-h m. «Mantel, Kleid», drapsá-h m. «Banner (?)» (= av. drafsa- «Fahne, Banner»)'.\"},\n            {\"ref\": \"IEC:159\", \"status\": \"supports\", \"note\": \"IEC p.159 s.v. drapsos: 'Av. drafšo, id.' ('cloth, cloth-length, sheet' > banner), beside Skt. drapsáh and Per. dirafš.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"col. 767 s.v. drafša-\", \"stance\": \"supports\", \"note\": \"'j. drafša- m. «Fahne, Banner»: mā ... yaθa *gə̄uš drafšō ... «wie das Stierbanner» Y.10.14 ... KompE.; Ableit. — ai. drapsá- m. «Banner», np. dirafš ... — Pü.: drafš; Npü.: nēzak «Waffe»'. Compounds ərəδwō.drafša-, uz.gərəptō.drafša-, pərəθu.drafša- confirm the noun.\"},\n            {\"src\": \"PHD\", \"where\": \"p. 27 s.v. drafš\", \"stance\": \"supports\", \"note\": \"'drafš [dlpš | P drfš, N ~] banner'; also 'drafšīdan, drafš- ... 1. shine; 2. tremble'.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"s.v. درفش, Etymology 1\", \"stance\": \"supports\", \"note\": \"'Inherited from Middle Persian (dlpš /drafš/, «banner»), perhaps from a hypothetical Proto-Iranian *drafš-, perhaps from Proto-Indo-European *drep- («to cut, tear off (a piece)»). Cognate with Parthian drfš, Avestan drafša-, Sanskrit द्रप्स (drapsá); outside Indo-Iranian, compare in particular Late Latin drappus.'\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"derafš «درفش ٢»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP dirafš/derafš 'banner' continues MP drafš (Book Pahlavi dlpš, Parthian drfš) from Av. drafša-, with the regular New Persian anaptyctic vowel breaking up the initial cluster dr- (dr- > dir-/der-, as in dirang, dirāz). Hübschmann p.61 no.553 states it flatly: 'Sicher ist hier nur die Gleichung: np. dirafš = phl. drafš = arm. draus = zd. drafša- «Banner, Fahne»' — the Armenian loan drawš proves the Middle Persian form. Nourai's homograph number ٢ separates it from درفش ١ 'awl, cobbler's needle'. The Ferdowsī couplet he quotes (درخشان سنان و درفشان درفش) is the standard illustration, and Borhan/Mo'in even list دروش as a variant.\",\n          \"derivation_fa\": \"«درفش» فارسی نو دنبالهٔ فارسی میانهٔ drafš (پهلوی کتابی dlpš، پارتی drfš) و آن از اوستایی drafša- است؛ واکهٔ میانجی در آغاز واژه خوشهٔ dr- را شکسته و آن را به dir-/der- بدل کرده است، درست مانند «دراز» و «درنگ». هوبشمان (ص ۶۱، شمارهٔ ۵۵۳) با قاطعیت می‌نویسد: «تنها چیزی که در اینجا مسلم است این برابری است: فارسی نو dirafš = پهلوی drafš = ارمنی drawš = اوستایی drafša-»؛ وام‌واژهٔ ارمنی گواهِ صورت فارسی میانه است. عدد ۲ در نمودار برای جدا کردن این واژه از «درفشِ ۱» (درفشِ کفشگری، درفش دوزندگی) است. حکم: ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D9%81%D8%B4\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:838\", \"status\": \"supports\", \"note\": \"BQT_v2_pages.txt leaf 298 = printed p.838 (offset +540, confirmed by the 'بقیه از صفحهٔ ۸۳۸' catch-line on leaf 299). Headword 'درفش' ('همان درفش کاویان است که علم فریدون ...'); Mo'in's fn. 4: 'رایت، بیرق، اوستا drafša- (بیرق)، پهلوی drafš ... ارمنی drawš ... و درفشی، ترکی: درفس'.\"},\n            {\"ref\": \"HRN:123\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 145 = printed p.123, no. 553: 'dirafš «Fahne, Banner». aw. drafsa- «Banner»; phlv. drafš, arm. LW. drauš; ai. drapsá- «Tropfen». oss. LW. ɣrisa «Fahne» ... «Banner», nicht Waffe, wie Darmesteter übersetzt. Auch im Šāhnāme heisst dirafš niemals «Lanze».'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"p. 61 no. 553\", \"stance\": \"supports\", \"note\": \"'Sicher ist hier nur die Gleichung: np. dirafš = phl. drafš = arm. drauš = zd. drafša- «Banner, Fahne». Die Vermutung über die Etym. von np. duruxš ist sehr unglücklich. Np. dirafštīdan «to flash» JRAS. 1894, p.461.'\"},\n            {\"src\": \"PHD\", \"where\": \"p. 27\", \"stance\": \"supports\", \"note\": \"'drafš [dlpš | P drfš, N ~] banner' — the Middle Persian link with the New Persian equivalence marked.\"},\n            {\"src\": \"NYB\", \"where\": \"Glossary index\", \"stance\": \"supports\", \"note\": \"Index entry 'drfs: drafs' (l.5606) referring the Book-Pahlavi spelling to the reading drafš.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"s.v. درفش\", \"stance\": \"supports\", \"note\": \"'Inherited from Middle Persian drafš «banner» ... Cognate with Parthian drfš, Avestan drafša-, Sanskrit drapsá ... Akin to the borrowings: Old Armenian դրաւշ (drawš), Old Georgian drošay, Ossetian tyrysa, Classical Syriac drap̄šā.'\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Latin\",\n          \"words\": \"drappus\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The form is real but it is Late/Gallo-Roman drappus 'cloth' (first in Merovingian charters), not Classical Latin, and its own origin is contested. Mann (IEC 159) simply lists 'LLat. drappus (whence It. Fr. Sp.)' under drapsos, which is Nourai's warrant. Pokorny p.211 is more guarded: 'gallorom. drappus «Tuch» (PN Drappō, Drappus, Drappes, Drapōnus) ist wohl ven.-ill. Lw.; der a-Vokal aus idg. o oder, wie das -pp-, expressiv' — i.e. a Venetic-Illyrian loan into Gallo-Roman, with the -pp- expressive. Watkins says only 'Perhaps extended root *drep- in the Celtic source (itself borrowed) of Late Latin drappus'. Klein: 'Late L. drappus, which is prob. of Gaulish origin and ult. derives fr. I.-E. *dre-p-'. Skeat dissents altogether, deriving drappus from Icelandic drepa 'to beat' (the fulling process). So: a Latin word in the loose sense, of substrate (Celtic or Venetic-Illyrian) transmission, with the *drep- etymology probable but not secure.\",\n          \"derivation_fa\": \"این صورت واقعی است، اما لاتین کلاسیک نیست: drappus «پارچه» واژه‌ای لاتینِ متأخر/گالورومی است که نخست در اسناد مروونژی دیده می‌شود، و خاستگاه خودش محل بحث است. مان (ص ۱۵۹) تنها می‌نویسد «لاتین متأخر drappus (که ایتالیایی و فرانسه و اسپانیایی از آن آمده‌اند)» و همین مستند نورایی است. پوکورنی محتاط‌تر است: «gallorom. drappus «پارچه» ... احتمالاً وام‌واژه‌ای ونتی-ایلیری است؛ واکهٔ a از o هندواروپایی یا مانند -pp- تأکیدی است.» واتکینز نیز فقط می‌گوید «شاید ریشهٔ گسترش‌یافتهٔ *drep- در منبع کِلتی (که خود وام‌گرفته است) لاتین متأخر drappus». کلاین آن را «احتمالاً گالی و در نهایت از *dre-p- هندواروپایی» می‌داند، ولی اسکیت یکسره مخالف است و آن را از ایسلندی drepa «کوبیدن» (کار نمدمالی) می‌گیرد. حکم: با احتیاط پذیرفتنی؛ برچسب «لاتین» ساده‌سازی است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/drape\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt s.v. der-2 §7: 'Perhaps extended root *drep- in the Celtic source (itself borrowed) of Late Latin drappus, cloth (> Old French drap): (DRAB¹), DRAPE, TRAP².' Watkins qualifies both the root and the transmission.\"},\n            {\"ref\": \"IEC:159\", \"status\": \"supports\", \"note\": \"IEC p.159 s.v. drapsos: 'LLat. drappus (whence It.Fr.Sp.)' listed as a direct member of the *drap- family.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 211\", \"stance\": \"partial\", \"note\": \"'gallorom. drappus «Tuch» (PN Drappō, Drappus, Drappes, Drapōnus) ist wohl ven.-ill. Lw.; der a-Vokal aus idg. o oder, wie das -pp-, expressiv' — Pokorny makes it a borrowing, not an inherited Latin word.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. drape\", \"stance\": \"supports\", \"note\": \"'F. draper ... fr. drap, «cloth», fr. Late L. drappus, which is prob. of Gaulish origin and ult. derives fr. I.-E. *dre-p-, «to tear off», whence also OI. drapih ... I.-E. *dre-p- is a -p-enlargement of base *der-, «to flay».'\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. Drape\", \"stance\": \"contradicts\", \"note\": \"'Drape, to cover with cloth. (F.) F. draper, to make cloth — F. drap. (Low L. drappus). Prob. from Icel. drepa, to beat (from the fulling process); see Drub.' Skeat rejects the *drep- etymology.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 802\", \"stance\": \"partial\", \"note\": \"Calls Italian drappo / French drap 'die noch nicht bestimmte ... Quelle', i.e. of undetermined source, while grouping it with the drapi-/drafsa- family.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"drape\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English drape (c. 1400 drapen 'to ornament with cloth hangings', mid-15c. 'to weave into cloth') is from Old French draper 'to weave, make cloth' (13c.), a denominative of drap 'cloth, sheet, bandage', from Late Latin drappus. The chart draws the arrow straight from Latin to English, skipping the Old French stage; the sense 'to cover with drapery' is only 1847 and 'to hang loosely' 1943. The same Late Latin word gives English drab¹ (the cloth colour, via French drap) and trap 'clothes, baggage'. No reference is printed on the box.\",\n          \"derivation_fa\": \"فعل انگلیسی drape (نخست حدود ۱۴۰۰ به‌صورت drapen «با پارچه آراستن» و در میانهٔ سدهٔ پانزدهم «بافتن») از فرانسهٔ کهن draper «بافتن، پارچه ساختن» (سدهٔ سیزدهم) می‌آید که خود فعلی است ساخته‌شده از drap «پارچه، ملافه» و آن از لاتین متأخر drappus. نمودار پیکان را یکراست از لاتین به انگلیسی کشیده و مرحلهٔ فرانسهٔ کهن را نیاورده است. معنای «با پرده پوشاندن» تنها از ۱۸۴۷ و معنای «شل و رها آویختن» از ۱۹۴۳ است. از همین واژهٔ لاتین متأخر، انگلیسی drab (رنگ پارچهٔ خام) و trap «رخت و بنه» نیز آمده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/drape\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference printed on the box; checked against Etymonline, Klein and Skeat (see consulted).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Etymonline\", \"where\": \"s.v. drape (v.)\", \"stance\": \"supports\", \"note\": \"'c. 1400, drapen, «to ornament with cloth hangings;» mid-15c., «to weave into cloth,» from Old French draper «to weave, make cloth» (13c.) ... from drap «cloth, piece of cloth, sheet, bandage», from Late Latin drapus, which is perhaps of Gaulish origin.'\"},\n            {\"src\": \"KLN\", \"where\": \"s.vv. drape, drab, trap\", \"stance\": \"supports\", \"note\": \"'drape, tr. v. — F. draper, «to cover with cloth, drape», fr. drap, «cloth», fr. Late L. drappus'; 'drab, n. ... F. drap, «cloth», fr. Late L. drappus, fr. Gaulish *drappo-'; 'trap, n., clothes, baggage. — ME. trappe, prob. fr. OF. drap.'\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. Drape\", \"stance\": \"partial\", \"note\": \"'F. draper, to make cloth — F. drap. (Low L. drappus)' — the French chain agrees; only the ultimate origin differs (Skeat: Icel. drepa).\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-119.json > /dev/null && echo \"JSON OK\""
}
```


### [2026-09-05T18:20:59.183Z] TOOL RESULT

```
JSON OK
```


## [2026-09-05T18:21:03.996Z] TOOL CALL #63: Bash

```json
{
 "command": "python3 tools/verify_check.py 119"
}
```


### [2026-09-05T18:21:05.832Z] TOOL RESULT

```
nodes verified: 16/16
node verdicts: {'plausible': 6, 'disputed': 3, 'confirmed': 7}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 16, 'partial': 6, 'not_found': 1, 'not_checked': 3}
books consulted: {'partial': 9, 'supports': 34, 'contradicts': 8, 'silent': 2} | by book: {'Wiktionary': 6, 'KLN': 6, 'BRT': 5, 'HUB': 5, 'HRN': 4, 'PHD': 4, 'POK': 4, 'CHEUNG': 3, 'NYB': 3, 'ARY': 2, 'BQT': 2, 'WLD': 2, 'Etymonline': 2, 'AHD': 2, 'SKT': 2, 'IEC': 1}
```


## [2026-09-05T18:21:15.590Z] TOOL CALL #64: Bash

```json
{
 "command": "python3 - <<'PY'\nimport json\nidx=[json.loads(l) for l in open('data/verification/sources/web/index.jsonl',encoding='utf-8')]\nrecent={e['url'] for e in idx if e.get('fetched','')>='2026-09-05'}\nv=json.load(open('data/verification/page-119.json'))\nused=set()\ndef walk(o):\n    if isinstance(o,dict):\n        for k,val in o.items():\n            if k=='sources': used.update(val)\n            else: walk(val)\n    elif isinstance(o,list):\n        for i in o: walk(i)\nwalk(v)\nimport urllib.parse\nallurls={e['url'] for e in idx}\nfor u in sorted(used):\n    d=urllib.parse.unquote(u)\n    print('OK ' if (u in allurls or d in allurls) else 'MISSING', u, '->', d)\nPY"
}
```


### [2026-09-05T18:21:17.204Z] TOOL RESULT

```
OK  https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D8%AF -> https://en.wiktionary.org/wiki/درد
OK  https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D9%81%D8%B4 -> https://en.wiktionary.org/wiki/درفش
OK  https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D9%87 -> https://en.wiktionary.org/wiki/دره
OK  https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D9%88%D8%AF%D9%86 -> https://en.wiktionary.org/wiki/درودن
OK  https://en.wiktionary.org/wiki/%D8%AF%D8%B1%DB%8C%D8%AF%D9%86 -> https://en.wiktionary.org/wiki/دریدن
OK  https://en.wiktionary.org/wiki/%D8%AF%D9%84%D9%88 -> https://en.wiktionary.org/wiki/دلو
OK  https://en.wiktionary.org/wiki/%D8%AF%D9%88%D9%84 -> https://en.wiktionary.org/wiki/دول
OK  https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/der- -> https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/der-
OK  https://www.etymonline.com/word/drape -> https://www.etymonline.com/word/drape
OK  https://www.etymonline.com/word/tear -> https://www.etymonline.com/word/tear
```


## [2026-09-05T18:21:21.253Z] TOOL CALL #65: Bash

```json
{
 "command": "python3 - <<'PY'\nimport io\np='data/verification/page-119.json'\ns=io.open(p,encoding='utf-8').read()\nn=s.replace('یونانی δέρما','یونانی δέρμα')\nassert n!=s\nio.open(p,'w',encoding='utf-8').write(n)\nPY\npython3 -m json.tool data/verification/page-119.json >/dev/null && python3 tools/verify_check.py 119 | tail -3"
}
```


### [2026-09-05T18:21:23.220Z] TOOL RESULT

```
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
AssertionError
root verdicts: {'confirmed': 2}
ref checks: {'supports': 16, 'partial': 6, 'not_found': 1, 'not_checked': 3}
books consulted: {'partial': 9, 'supports': 34, 'contradicts': 8, 'silent': 2} | by book: {'Wiktionary': 6, 'KLN': 6, 'BRT': 5, 'HUB': 5, 'HRN': 4, 'PHD': 4, 'POK': 4, 'CHEUNG': 3, 'NYB': 3, 'ARY': 2, 'BQT': 2, 'WLD': 2, 'Etymonline': 2, 'AHD': 2, 'SKT': 2, 'IEC': 1}
```


## [2026-09-05T18:21:26.070Z] TOOL CALL #66: Bash

```json
{
 "command": "grep -o \"δέρم[اs]*\\|یونانی δέρ.\\{0,3\\}\" data/verification/page-119.json | sort -u"
}
```


### [2026-09-05T18:21:27.653Z] TOOL RESULT

```
یونانی δέρμα 
یونانی δέρμا 
یونانی δέρω و
```


## [2026-09-05T18:21:31.441Z] TOOL CALL #67: Bash

```json
{
 "command": "python3 - <<'PY'\nimport io\np='data/verification/page-119.json'\ns=io.open(p,encoding='utf-8').read()\nn=s.replace('δέρμا','δέρμα')\nprint(n!=s)\nio.open(p,'w',encoding='utf-8').write(n)\nPY\npython3 -m json.tool data/verification/page-119.json >/dev/null && echo OK && python3 tools/verify_check.py 119"
}
```


### [2026-09-05T18:21:33.377Z] TOOL RESULT

```
True
OK
nodes verified: 16/16
node verdicts: {'plausible': 6, 'disputed': 3, 'confirmed': 7}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 16, 'partial': 6, 'not_found': 1, 'not_checked': 3}
books consulted: {'partial': 9, 'supports': 34, 'contradicts': 8, 'silent': 2} | by book: {'Wiktionary': 6, 'KLN': 6, 'BRT': 5, 'HUB': 5, 'HRN': 4, 'PHD': 4, 'POK': 4, 'CHEUNG': 3, 'NYB': 3, 'ARY': 2, 'BQT': 2, 'WLD': 2, 'Etymonline': 2, 'AHD': 2, 'SKT': 2, 'IEC': 1}
```


## [2026-09-05T18:21:55.357Z] AGENT

Page 119 (book p. 89) verified — `data/verification/page-119.json` written, `verify_check.py 119` shows 16/16 nodes and **0 PROBLEM lines**.

**Tally:** roots 2 confirmed · nodes 7 confirmed, 6 plausible, 3 disputed · ref checks 16 supports / 6 partial / 1 not_found / 3 not_checked · 53 `consulted` entries across 16 books.

**Disputed:**
- Der 1, node #6 `dŭl «دول»` — not from *dr̥tis. It is MP `dōl` 'bucket, Aquarius', a Semitic loan (Aram./Syr. `dawlā`, Akk. `dalū`, Ar. `دلو dalw`); Mo'in at BQT p.900 and Wiktionary both say so, and Nourai's own NOTE concedes it. Mann (IEC:165) really does list "Per. dūl 'water-skin'" under *drtis — the citation is honest, Mann is simply wrong.
- Der 1, nodes #2 `něš-tar` and #3 `nîšdar «نیشدر»` — `darîtan/darrīdan` and `dart/dard` are fully confirmed (MacKenzie, Nyberg, Cheung, Mo'in's BQT p.848 footnote), but `nēštar` 'lancet' does not contain `dar-`: Horn no. 1067 and Hübschmann §129 derive it from `nēš` 'point, sting' (Ir. *naikša-, Skt. `nikṣ-`, `nekṣana-`) + the instrument suffix `-tar` (Arm. loan `nštir` ⇒ Pahl. *nēštir).

**Notable "plausible" cases:** #1 Av. `niš-dar-` is a *verb* 'tear out' (preverb niš- + dar-, Barth. col. 689), not "a sharp tool"; #4/#5 `درو/درودن` belong to Ir. `*drauH-` (Cheung; Pok. 208 "Mpers. drūn, drūdan"), not to the participle `dərəta-`; #7/#8 `darəna- → درّه` follows Horn 560 and Mo'in (BQT p.845 fn. 9, "اوستا daranū-") against Bartholomae col. 693, who reads `darəna-` as 'lair, stronghold' from `dar-` 'to hold'; entry-1 #3 `drappus` is Late/Gallo-Roman and of contested (Celtic or Venetic-Illyrian) origin — Skeat rejects the *drep- etymology outright.

**Extraction errors: none.** I checked the printed page (pdftoppm of PDF p. 119): the book itself prints `nîšdar : a tool for cutting  نیشدر ( نیشتر )`, so the odd spelling نیشدر is Nourai's own analytic respelling and the JSON is faithful.

**Data note for the owner (not this page):** `refs_online.json` gives BQT vol. 2 as "printed ≈ leaf + 543 (±3)". In this range it is exactly **leaf + 540**, fixed by the catch-lines "بقیه از صفحهٔ ۸۳۸" on leaf 299 (= p. 839) and "بقیه در صفحهٔ ۸۵۵" on leaf 314 (= p. 854). All three BQT citations on this page (838, 845, 848) resolve correctly with +540 and would have missed with +543.
