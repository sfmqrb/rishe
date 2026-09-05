# Verification process log — verify-page-104


## [2026-09-05T14:51:33.485Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 104 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-104.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-104.json. Write /home/sfmqrb/git/rishe/data/verification/page-104.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 104` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T14:51:35.061Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T14:51:35.776Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T14:51:35.795Z] TOOL RESULT

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


## [2026-09-05T14:51:36.023Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-104.txt"
}
```


### [2026-09-05T14:51:36.034Z] TOOL RESULT

```
1	=== PDF page 104 (book page 74) ===
2	--- entry 0 ---
3	ROOT [Chinese] Č'a : tea  (refs KLN:1578; SHP:126)
4	#1 (parent #0) [Persian] refs=MON:1270; SHP:126 | čây «چای» : tea
5	#2 (parent #0) [Chinese] refs=KLN:1578; SHP:126 | t'a : tea | NOTE: (South Chinese accent)
6	  #3 (parent #2) [Malaysian] refs=None | teh
7	    #4 (parent #3) [Dutch] refs=None | thee
8	      #5 (parent #4) [English] refs=AHD:1320; KLN:1578 | tea
9	--- entry 1 ---
10	ROOT Cairya -> redirect to Čirya
11	--- entry 2 ---
12	ROOT [Indo-European] Čar, Char : idle chat  (refs OEW:51)
13	#1 (parent #0) [Italian] refs=FSD:452; AHD:227 | Cerreto : a village in Italy famous for its idle chatters (quacks) ; Cerretano : from Cerreto, idle chatter ; ciarlatano : one who claims to have knowledge that he does not have
14	  #2 (parent #1) [French] refs=AHD:227 | charlatan
15	    #3 (parent #2) [Persian] refs=VOP:234 | čârlâtân «شارلاتان» : a person who claims skills he does not have
16	    #4 (parent #2) [English] refs=AHD:227 | charlatan
17	#5 (parent #0) [French] refs=AHD:228 | charra : to chat ; charrado : a game of phrases and words
18	  #6 (parent #5) [English] refs=AHD:228 | charades
19	--- entry 3 ---
20	ROOT [Greek] Čartěs, Xartěs : leaf of papyrus  (refs AHD:203; KLN:239; PRT:79)
21	#1 (parent #0) [Arabic] refs=TAD:55; VDQ:342 | qertâs : paper
22	  #2 (parent #1) [Persian] refs=MON:2659 | qertâs «قرطاس» : paper
23	#3 (parent #0) [Latin] refs=AHD; KLN:239 | carta, charta : papyrus leaf
24	  #4 (parent #3) [French] refs=KLN:239 | carte
25	    #5 (parent #4) [Persian] refs=MON:2801 | kârt «کارت» : card | extra: کارتون
26	    #6 (parent #4) [English] refs=AHD; KLN | card, carton, cartoon, cartridge, chart
27	
```


## [2026-09-05T14:51:38.982Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-104.json",
 "description": "Read source JSON page 104"
}
```


### [2026-09-05T14:51:39.021Z] TOOL RESULT

```
{
  "pdf_page": 104,
  "book_page": 74,
  "entries": [
    {
      "root": {
        "name": "Č'a",
        "lang": "Chinese",
        "refs": "KLN:1578; SHP:126",
        "gloss": "tea"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "MON:1270; SHP:126",
          "words": [
            {
              "translit": "čây",
              "gloss": "tea",
              "script": "چای"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Chinese",
          "refs": "KLN:1578; SHP:126",
          "words": [
            {
              "translit": "t'a",
              "gloss": "tea",
              "script": null
            }
          ],
          "script_extra": null,
          "note": "(South Chinese accent)",
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Malaysian",
          "refs": null,
          "words": [
            {
              "translit": "teh",
              "gloss": null,
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
          "lang": "Dutch",
          "refs": null,
          "words": [
            {
              "translit": "thee",
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
          "parent": 4,
          "lang": "English",
          "refs": "AHD:1320; KLN:1578",
          "words": [
            {
              "translit": "tea",
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
        "name": "Cairya",
        "redirect": "Čirya"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Čar, Char",
        "lang": "Indo-European",
        "refs": "OEW:51",
        "gloss": "idle chat"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Italian",
          "refs": "FSD:452; AHD:227",
          "words": [
            {
              "translit": "Cerreto",
              "gloss": "a village in Italy famous for its idle chatters (quacks)",
              "script": null
            },
            {
              "translit": "Cerretano",
              "gloss": "from Cerreto, idle chatter",
              "script": null
            },
            {
              "translit": "ciarlatano",
              "gloss": "one who claims to have knowledge that he does not have",
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
          "lang": "French",
          "refs": "AHD:227",
          "words": [
            {
              "translit": "charlatan",
              "gloss": null,
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
          "lang": "Persian",
          "refs": "VOP:234",
          "words": [
            {
              "translit": "čârlâtân",
              "gloss": "a person who claims skills he does not have",
              "script": "شارلاتان"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "English",
          "refs": "AHD:227",
          "words": [
            {
              "translit": "charlatan",
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
          "lang": "French",
          "refs": "AHD:228",
          "words": [
            {
              "translit": "charra",
              "gloss": "to chat",
              "script": null
            },
            {
              "translit": "charrado",
              "gloss": "a game of phrases and words",
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
          "refs": "AHD:228",
          "words": [
            {
              "translit": "charades",
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
        "name": "Čartěs, Xartěs",
        "lang": "Greek",
        "refs": "AHD:203; KLN:239; PRT:79",
        "gloss": "leaf of papyrus",
        "note": "Probably from an Egyptian origin"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "TAD:55; VDQ:342",
          "words": [
            {
              "translit": "qertâs",
              "gloss": "paper",
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
          "refs": "MON:2659",
          "words": [
            {
              "translit": "qertâs",
              "gloss": "paper",
              "script": "قرطاس"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "دبیر جهاندیده را خواند شاه - بیاورد قرطاس و مُشک سیاه",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD; KLN:239",
          "words": [
            {
              "translit": "carta, charta",
              "gloss": "papyrus leaf",
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
          "lang": "French",
          "refs": "KLN:239",
          "words": [
            {
              "translit": "carte",
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
          "parent": 4,
          "lang": "Persian",
          "refs": "MON:2801",
          "words": [
            {
              "translit": "kârt",
              "gloss": "card",
              "script": "کارت"
            }
          ],
          "script_extra": "کارتون",
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 4,
          "lang": "English",
          "refs": "AHD; KLN",
          "words": [
            {
              "translit": "card, carton, cartoon, cartridge, chart",
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


## [2026-09-05T14:51:39.766Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo \"---\" && cat tools/verify_check.py | head -80",
 "description": "List verification dir and check script"
}
```


### [2026-09-05T14:51:39.814Z] TOOL RESULT

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
---
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


## [2026-09-05T14:51:43.685Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n 80,200p /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Rest of verify_check"
}
```


### [2026-09-05T14:51:43.722Z] TOOL RESULT

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


## [2026-09-05T14:51:44.290Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-101.json'))\nprint(json.dumps(d['entries'][0], ensure_ascii=False, indent=1)[:4000])\n\"",
 "description": "Sample existing verification entry"
}
```


### [2026-09-05T14:51:45.982Z] TOOL RESULT

```
{
 "entry": 0,
 "root": "B.r.k",
 "verdict": "confirmed",
 "modern_form": "Semitic root b-r-k: Proto-Semitic *birk- 'knee' / West Semitic brk 'to kneel; to bless' (AHD Semitic roots brk)",
 "note": "The root is real and its label 'Semitic' is right. Wiktionary reconstructs Proto-Semitic *birk- 'knee' (Akk. birkum, Heb. berekh, Ug. brk, Syr. burkā, Ge'ez bərk) with a metathetic variant *rukbat- (Ar. rukba). The 'kneel (of a camel) > bless' story is the traditional Gesenius/BDB account and matches Arabic baraka 'to kneel (camel)' / bāraka 'to bless'. The AHD Semitic appendix (Nourai's own AHD source) instead treats brk 'to bless' as 'probably a metathesized variant of krb' (Akk. karābu 'to praise, bless') — that is the hypothesis underlying Nourai's Akkadian/Hebrew cherub branch; it is accepted by AHD and Klein but rejected by recent Hebrew lexicography (SAHD, citing Mitchell: metathesis of first and third radicals is extremely rare). The griffin sub-branch is speculative (Klein) and not adopted by AHD's own griffin entry.",
 "note_fa": "ریشه اصیل است و برچسب «سامی» درست: ویکی‌واژه سامیِ آغازین *birk- «زانو» را بازسازی می‌کند (اکدی birkum، عبری berekh، سریانی burkā، گعزی bərk) با گونهٔ مقلوبِ *rukbat- که «رکبة» عربی از آن است. داستان «زانو زدنِ شتر ← برکت دادن» همان تبیین سنتیِ گزنیوس است و با «بَرَکَ/بارَکَ» عربی می‌خواند. اما پیوستِ سامیِ فرهنگ American Heritage — که خودِ نورایی بدان استناد می‌کند — b-r-k «برکت دادن» را «احتمالاً گونهٔ مقلوبِ k-r-b» می‌داند (اکدی karābu «ستودن، برکت دادن»)، و همین فرضِ قلب است که شاخهٔ اکدی-عبریِ «کروب» بر آن استوار شده؛ کلاین آن را می‌پذیرد اما فرهنگ‌نویسیِ امروزیِ عبری (پایگاه SAHD به نقل از میچل) ردش می‌کند، چون قلبِ همخوان نخست و سوم بسیار نادر است. شاخهٔ «گریفین» نیز حدسی است (از کلاین) و خودِ AHD در مدخل griffin آن را نپذیرفته است.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/birk-",
  "https://ahdictionary.com/word/semitic.html",
  "https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%83%D8%A9"
 ],
 "ref_check": [
  {
   "ref": "FVQ:75",
   "status": "supports",
   "note": "FVQ_pages.txt leaf 92 (Jeffery p. 75), s.v. Baraka: 'To bless. ... The primitive verb b-r-k, which is not used in the Qur'an, means to kneel, used specially of the camel, so that baraka is the technical word for making a camel kneel. In this primitive sense it is common Semitic ... It was in the N. Semitic area, however, that the root seems to have developed the sense of to bless, and from thence it passed to the S. Semitic area. Thus we have Heb. bērēk, and Phon. brk to bless; Aram. brk to bless or praise; Syr. barrek ... From this N. Semitic sense we find derived the Sab. brk, Eth. bāraka to bless, celebrate the praises of, and Ar. bāraka as above.' — exactly Nourai's 'kneel (of the camel) → bless' story."
  }
 ],
 "nodes": [
  {
   "id": 1,
   "lang": "Arabic",
   "words": "b.r.k; barakat",
   "verdict": "confirmed",
   "derivation": "Arabic root b-r-k: baraka 'to kneel (of a camel)' (verbal noun burūk), Form III bāraka 'to bless', Form II barraka, Form VI tabāraka 'be blessed'; the noun baraka(t) 'blessing, divine favour' is the maṣdar-type noun of the root, with tāʾ marbūṭa -at (hence the transliteration barakat). Cognate with Hebrew bērēkh 'to bless' / bərākhā 'blessing'. Wiktionary lists 11 Arabic derivatives of the root.",
   "derivation_fa": "ریشهٔ عربیِ ب-ر-ک: «بَرَکَ» یعنی «زانو زدنِ شتر» (مصدر بُروک)، بابِ سومِ «بارَکَ» «برکت دادن»، بابِ دومِ «برَّکَ» و بابِ ششمِ «تبارَکَ»؛ و اسمِ «بَرَکَة» «برکت، عنایت الهی» که مصدرگونه‌ای از همین ریشه با تاء مربوطه است — و همین -ة است که در آوانگاریِ «barakat» به صورت -ت آمده است. هم‌ریشهٔ عبریِ آن bērēkh «برکت دادن» و bərākhā «برکت» است. کلاین و جفری هر دو همین را می‌گویند و ادعای نورایی در این گره درست است.",
   "sources": [
    "https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%83%D8%A9",
    "https://en.wiktionary.org/wiki/%D7%91%D7%A8%D7%9B%D7%94"
   ],
   "ref_check": [
    {
     "ref": "KLN:164",
     "status": "supports",
     "note": "
```


## [2026-09-05T14:51:52.098Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','SHP','MON','AHD','OEW','FSD','VOP','PRT','TAD','VDQ','SKT','WEB','LKT','HJB','AID','ARY','BQT','PHN','DEV','FVQ','AFM','PLA','SYN','IEC','POK','WLD','HRN','HUB']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:400])\n\"",
 "description": "Look up ref abbreviations"
}
```


## [2026-09-05T14:51:52.206Z] TOOL CALL #8: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T14:51:56.331Z] TOOL RESULT

```
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SHP {"title": "J. T. Shipley, Dictionary of Word Origins, New York 1945", "edition_found": "1945 (lending-only)", "kind": "hathitrust_fullview+archive_restricted", "url": "https://babel.hathitrust.org/cgi/pt?id=uc1.32106001576476 (1945 ed., rightsCode pd = FULL VIEW, catalog record 001441050) ; archive.org dictionaryofword00ship and 15 others = lending only", "identifier": "dictionaryofword0000jose_n4
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
OEW {"title": "J. T. Shipley, The Origins of English Words: A Discursive Dictionary of Indo-European Roots, Baltimore 1984", "edition_found": "1984 (lending-only)", "kind": "archive_restricted", "url": "https://archive.org/details/originsofenglish0000ship ; https://archive.org/details/originsofenglish00jose (both JHU 1984, borrowable) ; HathiTrust mdp.49015002910322 search-only ; Google ELSm5zUgP_wC n
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09:
PRT {"title": "E. Partridge, Origins: A Short Etymological Dictionary of Modern English, New York 1958", "edition_found": "1958 (lending-only copies)", "kind": "archive_restricted", "url": "https://archive.org/details/originsshortetym00part (1958 1st ed.) ; originsetymologi0000part_j9t3 (4th ed. 1966) ; originsetymologi0000part (Routledge 2009) — all lending", "identifier": "originsshortetym00part (al
TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://a
VDQ {"title": "Fereydun Badreh'i (tr.), Vazheha-ye Dakhil dar Qor'an-e Majid (Persian translation of Jeffery FVQ with notes), Toos 1372/1993", "kind": "website", "url": "https://noorlib.ir/book/view/12868?pageNumber=<N>&viewType=pdf (page images; viewType=html also exists) ; info: https://noorlib.ir/book/info/12868 ; ketabnak.com/book/51136 (download blocked)", "lookup_hint": "noorlib viewer is JavaSc
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource
AID {"title": "G. C. Whitworth, An Anglo-Indian Dictionary, London 1885", "edition_found": "1885 (DLI scan); also 1981 reprint scan", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.45332", "identifier": "in.ernet.dli.2015.45332 (also anglo-indiandictionary, 1981 reprint)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt", "page_offset": "leaf
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verific
DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
```


### [2026-09-05T14:51:56.368Z] TOOL RESULT

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


## [2026-09-05T14:52:09.138Z] TOOL CALL #9: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','AHD','FSD','MON','TAD','SHP','OEW','PRT','VDQ','SIN','LKT','DEV','PHN','SKT','WEB','ARY','HJB','AFM','ARB']:\n    v=d.get(k) or {}\n    print('==',k, '| local:', v.get('local_file'), '| offset:', v.get('page_offset'), '| hint:', (v.get('lookup_hint') or '')[:300])\n\"",
 "description": "Get page offsets for relevant refs"
}
```


### [2026-09-05T14:52:11.041Z] TOOL RESULT

```
== KLN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt | offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
== AHD | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt | offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru
== FSD | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt | offset: vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.
== MON | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] | offset: None | hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe
== TAD | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt'] | offset: 86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image | hint: Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.
== SHP | local: None | offset: None | hint: Borrow via IA lending; in-book search ?q=<word>.
== OEW | local: None | offset: None | hint: Borrow via IA lending (djvu.txt returns 401/403). Entries are IE roots in alphabetical order; use IA's in-book search: https://archive.org/details/originsofenglish00jose?q=<root>
== PRT | local: None | offset: None | hint: Borrow via IA lending; in-book search https://archive.org/details/originsshortetym00part?q=<word>. Entries are alphabetical with numbered sub-senses.
== VDQ | local: None | offset: None | hint: noorlib viewer is JavaScript-rendered (WebFetch/curl get only the site chrome); needs a browser. Since it is a translation of FVQ, verify the substance via FVQ (same entry order); page numbers differ.
== SIN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SIN.txt | offset: leaf = printed - 172 (e.g. leaf 15 = p.187). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Running page numbers 185-630 (the volume's series pagination, which Nourai uses). Sections are numbered with plant/product names in caps; grep the Persian/Chinese word or the page number.
== LKT | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt | offset: leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.
== DEV | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt | offset: leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: French headword in caps at line start.
== PHN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt | offset: leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: French headword in caps at line start; Arabic script not OCRed. grep -n '^BAZAR' etc.
== SKT | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt | offset: leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
== WEB | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt | offset: not reliably detected (page_numbers.json sparse); grep headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 1978 page number can be checked in the 1962 vol. 1 scan for words A-(mid alphabet); vol. 2 only via lending copies.
== ARY | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'] | offset: printed page = pdf page + 1 | hint: Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY
== HJB | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt | offset: leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.490, leaf 905 = p.870). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headwords in caps at line start followed by ', s.' etc., e.g. grep -n '^BAZAAR' HJB.txt. Also online at dsal: https://dsal.uchicago.edu/dictionaries/hobsonjobson/ (search box) which shows page numbers.
== AFM | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt'] | offset: 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image | hint: Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').
== ARB | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_mo3rb.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_abdulraheem.txt'] | offset: None | hint: Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image.
```


## [2026-09-05T14:52:14.819Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^tea, \" KLN_1966.txt | head -5; echo ---; grep -n \"Amoy\" KLN_1966.txt | head -20",
 "description": "grep tea in Klein"
}
```


### [2026-09-05T14:52:14.889Z] TOOL RESULT

```
38336:tea,  n.  —  F.  the  (the  orig.  pronunciation  of  E.  tea was  ta),  fr.  Malay,  teh,  fr.  dial.  S.  Chin,  te,  which corresponds  to  Chin.  chai.  Cp.  Thea,  theine.
---
9917:cumquat,  n.  —  A  var.  spelling  of  kumquat. cumshaw,  n.,  present,  tip.  —  Amoy  pronunciation of  Chin,  kan  hsieh,  ‘grateful  thanks’, cumulate,  tr.  and  intr.  v.,  to  accumulate.  —  L. cumulatus,  pp.  of  cumulare,  ‘to  heap’.  See  cu¬ mulus  and  verbal  suff.  -ate  and  cp.  accumulate. Derivatives:  cumulat-ed,  adj.,  cumulat-ion,  n., cumulat-ive,  adj.,  cumulal-ive-ly,  adv.,  cumulat- ive-ness ,  n.
```


## [2026-09-05T14:52:16.359Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^charlatan\" KLN_1966.txt SKT.txt | head; echo ---; grep -n \"^charade\" KLN_1966.txt SKT.txt | head; echo ---; grep -n \"Cerreto\\|cerretano\\|ciarlatano\" KLN_1966.txt SKT.txt FSD_vol1.txt AHD_watkins1985.txt WEB_vol1.txt | head -20",
 "description": "grep charlatan/charade"
}
```


### [2026-09-05T14:52:16.480Z] TOOL RESULT

```
KLN_1966.txt:7223:charlatan,  n.,  a  pretender;  a  quack.  —  F.,  fr.  It. ciarlatano,  fr.  earlier  cerretano,  of  s.m.,  fr.  ML, ceretanus,  lit.  ‘inhabitant  of  Cerreto' ,  a  town near  Spoleto  in  Italy,  famous  for  its  quacks  and impostors.  It.  ciarlatano  was  influenced  in  form by  It.  ciarlare,  ‘to  prattle’.
KLN_1966.txt:7225:charlatanism,  n.  —  A  hybrid  coined  fr.  prec. word  and  -ism,  a  suff.  of  Greek  origin.
---
KLN_1966.txt:7210:charade,  n.,  a  riddle  based  on  the  syllables  of  a word.  —  F.,  fr.  Proven?,  charrado,  ‘talk,  chat’, fr.  charra,  ‘to  talk,  chat’,  which  is  of  imitative origin.  Cp.  It.  ciarlare,  Sp.  charlar,  ‘to  talk, prattle’.
---
KLN_1966.txt:7223:charlatan,  n.,  a  pretender;  a  quack.  —  F.,  fr.  It. ciarlatano,  fr.  earlier  cerretano,  of  s.m.,  fr.  ML, ceretanus,  lit.  ‘inhabitant  of  Cerreto' ,  a  town near  Spoleto  in  Italy,  famous  for  its  quacks  and impostors.  It.  ciarlatano  was  influenced  in  form by  It.  ciarlare,  ‘to  prattle’.
FSD_vol1.txt:63074:A   pretentious  man,  by  token  of  his  pretentiousness,  is  a   charla- tan always.  Holland  Letters  to  the  Joneses  p.  172.  Is.  1864.] (F.,  <   It.  ciarlatano,  <   clarla,  prattle.]  char"la-tan'ic  or char"la-tan'I-cal,  a.—  cbar'la-tan'l-cal-ly,  adv.~  char'- la-tan-Ish,  a.  Savoring  of  the  charlatan. char"la-tan-ls'tlc,  1   ghor'la-ton-is'tik;  2   char'Ia-tan-Is'tic, a.  Inclined  to  charlatanism;  having  a   tendency  to  quackery, char'la-tan-ry,  1   sfliar'ls-tnn-n;  2   <?har'Ia-tan-ry,  n.  The arts  or  practises  of  a   charlatan;  undue  or  fraudulent pretensions  to  skill;  quackery.
WEB_vol1.txt:31296:chir’la-tan, n. [Fr., from It. ciarlatano, a quack, from ciarlare, to prate.] one who makes untruthful pretensions; a quack; a mountebank; an impostor.
```


## [2026-09-05T14:52:27.388Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport io\ndef leaf_of(path, needle, maxhits=3):\n    data=open(path,encoding='utf-8',errors='replace').read()\n    pages=data.split('\\f')\n    hits=[]\n    for i,p in enumerate(pages):\n        if needle in p:\n            hits.append(i)\n            if len(hits)>=maxhits: break\n    return hits\nprint('KLN tea leaf', leaf_of('KLN_1966.txt','tea,  n.  —  F.  the'))\nprint('KLN charlatan leaf', leaf_of('KLN_1966.txt','charlatan,  n.,  a  pretender'))\nprint('KLN charade leaf', leaf_of('KLN_1966.txt','charade,  n.,  a  riddle'))\nprint('FSD1 charlatan leaf', leaf_of('FSD_vol1.txt','It.  ciarlatano'))\nprint('WEB charlatan leaf', leaf_of('WEB_vol1.txt','chir’la-tan'))\nEOF",
 "description": "Compute leaf numbers"
}
```


### [2026-09-05T14:52:29.253Z] TOOL RESULT

```
KLN tea leaf [836]
KLN charlatan leaf [152]
KLN charade leaf [152]
FSD1 charlatan leaf [507]
WEB charlatan leaf [334]
```


## [2026-09-05T14:52:38.044Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndata=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=data.split('\\f')\nfor i in (150,151,152,153,799,800,801,802,834,835,836,837):\n    p=pages[i]\n    print('--- leaf',i, repr(p[:180]))\nEOF",
 "description": "Inspect Klein leaves for page numbers"
}
```


### [2026-09-05T14:52:39.802Z] TOOL RESULT

```
--- leaf 150 '��one who  speaks  (in  a  certain  manner) ;  one  who  deals (with  a  certain  topic)’.  See  -logy, cetyl,  n.,  a  univalent  radical,  C16H33,  occurring in  spermaceti,  bee'
--- leaf 151 'd  cypress’,  fr.\nChamaedaphne\nchap\n266\n267\nchamae-  and  xurcaptaaoi;,  ‘cypress’.  See  cypress. Chamaedaphne,  n.,  a  genus  of  plants  of  the  heath family  (bot.)  —  ModL.'
--- leaf 152 ' —  Coined  fr.  prec.  word  on  analogy of  demotic  (fr.  demos)  and  other  adjectives  of Greek  origin  ending  in  -otic  (fr.  Gk.  -o-nxog). Derivatives:  chaotic-al,  ad'
--- leaf 153 'erm’,  dissimilated  fr.  *gen-men  (see germ).\nDerivatives:  charm-ful,  adj.,  charm-ful-ly,  adv., charm-ful-ness,  n.,  charm-less,  adj. charm,  tr.  v.  —  F.  charmer,  fr. '
--- leaf 799 '��starboard’,  are  Teut.  loan  words.  See  steer,  ‘to direct’,  and  board.\nstarch,  n.  —  ME.  sterche,  starche,  back  forma¬ tion  fr.  sterchen,  ‘to  starch’,  fr.  OE. '
--- leaf 800 'ic  and  -ics.\nstatistology,  n.,  the  study  of  statistics.  —  A  hy¬ brid  coined  fr.  statistics,  a  word  of  L.  origin,  and Gk.  -Xoyia,  fr.  -X6yoc,  ‘one  who  speak'
--- leaf 801 'le  jack,  n.,  one  who  climbs  steeples,  chim¬ neys,  etc.,  for  making  repairs.  —  Prop.  ‘Jack (used  in  the  sense  of  ‘fellow,  man’),  working  on steeples’.\nDerivati'
--- leaf 802 'afette,  etape,  staff,  stamp,  stampede, staple,  ‘bar,  wire’,  staple,  ‘commodity’,  stemple, stoep,  stump.  Cp.  also  Staphylea,  staphylo-. step,  intr.  and  tr.  v.  —  '
--- leaf 834 ' see  dram  and  cp.  target.  ML. targ(i)a,  OProvenq.  targa  (whence  It.  targa),  Sp. tarja,  ‘shield’,  are  also  Teut.  loan  words.  G. Tartsche,  ‘small  round  shield;  '
--- leaf 835 'p,  saucer’.  Cp.  OProveng.  tassa, It.  tazza,  Sp.  taza,  ‘cup’,  which  are  of  the  same origin.  Cp.  also  tazza.\nTass,  n.,  the  official  news  agency  of  the  U.S.S.R'
--- leaf 836 '.  —  ME.  taxacioun,  fr.  MF.  (=  F.) taxation,  fr.  L.  laxationem,  acc.  of  taxatio,  ‘a rating,  valuing,  appraisal’,  fr.  taxatus,  pp.  of taxare.  See  tax  and  -ati'
--- leaf 837 '.,  an  adherent  of  technocracy.  — Compounded  of  techno-  and  -crat.\nDerivative:  technocrat-ic,  adj. technology,  n.,  the  study  of  industrial  arts.  — Compounded  of  '
```


## [2026-09-05T14:52:46.210Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ndata=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=data.split('\\f')\nfor i in range(830,842):\n    nums=re.findall(r'\\b1[0-9]{3}\\b', pages[i])\n    print(i, nums[:8], pages[i][:60].replace('\\n',' '))\nEOF",
 "description": "Find printed page numbers around leaf 836"
}
```


### [2026-09-05T14:52:48.096Z] TOOL RESULT

```
830 ['1566'] e  rail  across  the  stern of  a  ship.  —  Du.  tafereel, 
831 ['1568', '1569', '1763', '1826', '1947'] ve,  adj.  —  A  hybrid  coined  fr.  talk  and -ative,  a  
832 ['1583', '1561', '1613', '1915', '1767', '1813', '1802'] hief, who  lived  in  the  second  half  of  the  1 7th  and
833 ['1572', '1922'] cp.  the  first  element  in tandem.  Cp.  also  taunt.  Cp.
834 []  see  dram  and  cp.  target.  ML. targ(i)a,  OProvenq.  tar
835 ['1577'] p,  saucer’.  Cp.  OProveng.  tassa, It.  tazza,  Sp.  taza,
836 ['1906', '1707', '1578', '1579', '1833', '1905'] .  —  ME.  taxacioun,  fr.  MF.  (=  F.) taxation,  fr.  L. 
837 ['1580'] .,  an  adherent  of  technocracy.  — Compounded  of  techno
838 ['1852', '1762', '1841', '1792', '1583', '1679', '1754', '1728'] tnjXut, of  s.m.,  Gk.  T7]X6flt,  of  s.m.,  xi)X6(1e(v),  
839 ['1743', '1817', '1798', '1584', '1003', '1564', '1642', '1119']  contare,  Sp.  contar,  ‘to  count,  to  recount, narrate’,
840 ['1936'] d’,  cp.  OE.  /> un-wang,  pun-wenge,  OS. thinn-ongi,  ON.
841 ['1693', '1761', '1815']  of  Gk.  tevcov,  ‘sinew,  ten¬ don’,  which  derives  from
```


## [2026-09-05T14:52:58.379Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN card/chart/carton ===\" && grep -n \"^card, n\\.\\|^chart, n\\.\\|^carton\\|^cartoon\\|^cartridge\\|^charta\\b\" KLN_1966.txt | head -20",
 "description": "grep Klein card/chart"
}
```


### [2026-09-05T14:52:58.439Z] TOOL RESULT

```
=== KLN card/chart/carton ===
6632:cartridge,  n.  —  Fr.  earlier  cartrage,  corruption  of
```


## [2026-09-05T14:53:01.136Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== TAD قرطاس ===\" && grep -n \"قرطاس\" TAD_pages.txt TAD.txt | head -10; echo \"=== AFM ===\" && grep -n \"قرطاس\" AFM_pages.txt | head -5; echo \"=== ARB ===\" && grep -n \"قرطاس\" ARB_mo3rb.txt ARB_abdulraheem.txt | head -5; echo \"=== FVQ ===\" && grep -n -i \"qirtas\\|Qirṭās\\|kartes\" FVQ_pages.txt | head -10",
 "description": "grep qirtas in Arabic refs"
}
```


### [2026-09-05T14:53:01.245Z] TOOL RESULT

```
=== TAD قرطاس ===
TAD_pages.txt:2151:             ‫قرطاس ‏ وناني همارك معناه ما جرسم به مرادفه ورقة وصحيفة‬
TAD.txt:2270:قرطاس ‏ وناني همارك معناه ما جرسم به مرادفه ورقة وصحيفة 
=== AFM ===
3473:( الكاغد) فارسي حض بعنى القرطاس . والكاغذ لغة فيه ومن الحكردي
3474:كاغز واما القرطاس فعرب 5 `
=== ARB ===
ARB_mo3rb.txt:8228:لقو لاوما واولا ذلك لويحب الققماء على مائها بأنما أعمل » لأنها بازاء قاف قرطاس + 
ARB_mo3rb.txt:8229:لابن حنى : سألت أبا على ون ** تيفاف © أتاره للالماق يباب قرطاس © فقال : نعم ٠‏ واحتتج 
ARB_mo3rb.txt:12414:بقرطاس س يمنى بشم القاف سب و يقال رزداق ورستاق ٠‏ وابسع الرسائيق » وهى السواد ٠‏ وقال 
ARB_mo3rb.txt:19898:() هذاقول شاذء ل كه غير المؤلف فيا أظن ٠‏ و ”” القرطاس ©“ يكسر القّاف وضهها 6 لنتات 
ARB_mo3rb.txt:19900:عليك كَابا فى قرطاس ]) ٠‏ وقرأها معن الكوفى بم القاف »كاف اين خالر يه ( ص 55) ٠‏ رنها 
=== FVQ ===
```


## [2026-09-05T14:53:10.753Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nd=open('TAD_pages.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nfor i,p in enumerate(pages):\n    if 'قرطاس' in p:\n        print('leaf',i)\n        tag=re.search(r'\\[pdf page (\\d+)\\]',p)\n        print('tag',tag.group(0) if tag else None)\n        print(p[:600])\n        break\nEOF",
 "description": "Find TAD leaf for qirtas"
}
```


## [2026-09-05T14:53:12.259Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"irtas\\|irṭās\\|χάρτης\\|chartes\" FVQ_pages.txt | head -20; echo \"=== PLA ===\"; grep -n -i \"qirtas\\|Qirṭās\" incoming/PLA/PLA_pages.txt | head -5",
 "description": "grep FVQ and PLA"
}
```


### [2026-09-05T14:53:12.378Z] TOOL RESULT

```
leaf 58
tag None
                                      ‫سد‬    ‫اهم‬



                                           ‫‪2‬ك » وهو الحجل‬
                                                        ‫قب ‪ .-‬فارسي ك‬
     ‫معنأه حماس و ‪ 110 862‬ألاتزلاه‬   ‫قرس ل أخوة النحاسى ‏ لانيني امن‬

                                                                 ‫رسسي‬
                                                                    ‫بحا‬
                                                                      ‫أقين‬
                        ‫بعر يب ‪50]0/5‬ألء وهو اسممصر ف اليونانية‬
```


### [2026-09-05T14:53:12.440Z] TOOL RESULT

```
=== PLA ===
```


## [2026-09-05T14:53:16.120Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2130,2175p' TAD_pages.txt",
 "description": "TAD context around qirtas"
}
```


### [2026-09-05T14:53:16.175Z] TOOL RESULT

```
     ‫معنأه حماس و ‪ 110 862‬ألاتزلاه‬   ‫قرس ل أخوة النحاسى ‏ لانيني امن‬

                                                                 ‫رسسي‬
                                                                    ‫بحا‬
                                                                      ‫أقين‬
                        ‫بعر يب ‪50]0/5‬ألء وهو اسممصر ف اليونانية‬
                                                              ‫قبط ت‬

 ‫ايطالي مطةالمةن معناه فى الاصل رئيس مرادقه ناك السفينة‬            ‫قبطان ف‬

                                            ‫وفائد الجيش وعميد القوم وعمدة وكش‬
     ‫قدوم ‪ -‬عبراني « كردُوم » تأدغت الراء بالدال فصار « قدوم » وهو‬
                                                   ‫مجر النجار وم‪:‬ته‬
      ‫وهو وع سن الهوخ كرة شه حب‬               ‫بوناني ‪8‬‬       ‫قراسيأ وقراصا‬

‫‪١‬‏‬                                         ‫االعلنباسود الا ان فىلبه عجمة واحدة‬
                       ‫قراغول ‪ -‬ترك « فراغول » معناهرييئةوطليعة وخفير‬
                                    ‫قرداحي ‪ -‬أرامي « قرداحا » وهو الحداد‬
                                                         ‫فرش س راجع غرش‬
                 ‫قرصان | ‪.‬يطالمي ‪ ©1350‬معئاه غازون وبراد به لصوص البحر‬

             ‫قرطاس ‏ وناني همارك معناه ما جرسم به مرادفه ورقة وصحيفة‬

              ‫معناه قرن صغير ويطلق على حلي الأذن‬       ‫وناني ههه‬       ‫قرط‬

         ‫قرطل ‪ 55‬أرامي د ترطلا» أي ‪ 71‬من قصب منقول مناليوناني ‪1‬‬

‫ثى الارمنية تتصعدى وى اللاتينية ‪5‬نم‪ *»:‬ومعنأه دودة وبي‬                ‫رمز‬
                                        ‫ده‬     ‫ااه‬



‫اراق « كرميل »عد الإل الال وهو تدناظري 'تحوت دينكم أي |‬
‫دودة ول أي حراء وهزاكوقة عراء كرن ف ‪:‬ضوف اقاء مو نف ابيقة ‪1‬‬
‫اوتستعها وهو نوسود ف نينا ‪١١‬‏‬
                            ‫ويقع على ورق شجرة بلوط القرمز وعلى أنه ) ب‬
  ‫والهند والككيك وسائرالبلدان الحارةفيجمعفىحينهويصبغ به ولونه أحر قانر‬
                                   ‫فنقل قرمر منالعر ببة الى لغات اوريا بلفظ و‪6‬ممه؟‪1‬‬

                                            ‫قرقة © ‪ --‬تركي( غورق عريهارنقاء‬
    ‫قرميبدد ‪ -‬بوناني ‪5112:2, 8‬نع‪ 21‬معناه تراب محروق أي طهيشنوي” وهو‬
                                                               ‫الخزف والفخار والاجر‬
   ‫وزاك الذئ بال حل عالقا ستول سن انوناق وموم عرو اينرنيتاة‬
    ‫عندمم زمانووقت ومدة وستون و دكأبظا على الهالزمان مرادفه دهر أي مأئة سنة‬
   ‫قترفل ‪ -‬فى اليونانية مله رخفا وهو شجر قروئه أفضل الافاويه‬
   ‫وبطلق أيضاعلىنبات بستاني زغوه علتن الاقامتفاء وان مداوكه وقد‬
```


## [2026-09-05T14:53:23.480Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^card,\\|^chart,\\|^carton,\\|^cartoon,\\|^charter,\\|^cartel,\" KLN_1966.txt | head -20; echo \"--- search carta\"; grep -n \"L\\.  charta\\|Gk\\.  x[aά]\" KLN_1966.txt | head -20",
 "description": "grep Klein card entries"
}
```


### [2026-09-05T14:53:23.542Z] TOOL RESULT

```
6521:card,  n.,  a  machine  for  combing  hair,  wool,  etc.  — F.  carde,  ‘chard,  teasel,  card",  fr.  OProveng.  ear- do,  back  formation  fr.  cardar,  ‘to  card’,  fr.  L. carduus,  ‘thistle’,  which  is  related  to  carro,  car- rere,  ‘to  card  (wool)’,  from  a  basic  form  *carri- dus,  ‘that  which  scrapes’,  fr.  I.-E.  base  *qars-, 'to  scrape,  scratch,  rub’.  See  harsh  and  cp.  car- doncillo,  cardoon,  Carduus,  Carex,  carline  thistle, carminative,  carrizo,  chard, card,  tr.  v.,  to  comb  with  a  card.  —  F.  carder, fr.  carde.  See  prec.  word.
6621:cartel,  n.,  1)  a  written  challenge;  2)  a  written
7239:charter,  n.  —  OF.  (=  F.)  chartre,  fr.  L.  chartula,
--- search carta
1289:acalycine,  adj.,  without  a  calyx  (bot.).  —  ModL. acalycinus ,  ‘having  no  calyx’,  formed  fr.  priv. pref.  a-,  Gk.  xaXul;,  ‘cup,  calyx’,  and  L.  suff. -inus.  See  calyx  and  adj.  suff.  -ine.
1416:A  hybrid  coined  fr.  priv.  pref.  a-,  Gk.  xairr)> ‘long  flowing  hair,  mane’,  and  -ous,  a  suff.  of Latin  origin.  See  chaeto-.
3270:Aquilo,  n„  the  north  wind  (Roman  antiq.)  —  L. aquilo,  ‘north  wind’,  lit.  ‘the  dark  one ,  fr. aquilus,  ‘dark-colored’  [cp.  aquila,  ‘eagle’, prop,  ‘the  dark-colored  (bird)’];  see  prec.  word. For  sense  development  cp.  Gk.  xaixla?,  ‘north east  wind’,  lit.  ‘the  dark  one’,  cogn.  with  L. caecus,  ‘blind’  (see  Caecias). aquose,  adj.,  aqueous.  —  L.  aquosus,  abounding in  water’,  fr.  aqua,  ‘water’.  See  aquatic  and  cp. aqueous.
6033:Cacaiia,  n.,  a  genus  of  plants,  the  Indian  plan¬ tain  (bot.)  —  ModL.,  fr.  Gk.  xaxxkia,  name  of a  plant.
6045:Cachrys,  n.,  a  genus  of  herbs  of  the  carrot  family (bot.)  —  Gk.  xayp'j;,  ‘parched  barley,  catkin’, prob.  rel.  to  x^yypo;,  ‘millet’.  Cp.  Cenchrus. cachucha,  n.,  a  Spanish  dance.  —  Sp.,  lit.  ‘reci¬ pient’,  fr.  cacho,  ‘saucepan’,  fr.  VL.  *cacculus, ‘an  earthen  pot  for  cooking’.  See  cockle,  ‘stove’, cacique,  n.,  a  West  Indian  chief.  —  Sp.,  from  a Haitian  language.
6047:cack,  intr.  v.,  to  void  excrement  (dial.)  —  ME. cakken,  fr.  L.  cacdre,  which,  like  Gk.  xaxxxv, Russ,  kakat',  Mir.  caccaim,  etc.,  derives  from the  I.-E.  child’s  word  *kakka,  ‘to  void  excre¬ ment’.  Cp.  Cagot.
6059:cacophonous,  adj.,  ill-sounding.  —  Gk.  xaxo- tpcovo?,  compounded  of  xaxo-  (see  caco-)  and tpouvY),  ‘sound,  voice’.  See  phone.  For  E.  -ous, as  equivalent  to  Gk.  -04,  see  suff.  -ous. cacophony,  n.,  a  harsh  or  discordant  sound.  — Gk.  v.axotpomi,  fr.  xaxocpcovos.  See  prec.  word and  -y  (representing  Gk.  -(a) .
6060:Cactaceae,  n.  pl„  the  cactus  family  (hot.)  — ModL.,  formed  fr.  cactus  with  suff.  aceae. cactaceous,  adj.  —  See  prec.  word  and  -aceous. cactiform,  adj.,  resembling  a  cactus  in  form.  — Compounded  of  Cactus  and  -form, cactus,  n.  — -  L.,  ‘a  prickly  plant’,  fr.  Gk.  xaxTo?, of  s.m.,  which  is  prob.  a  pre-Hellenic  word  of unknown  origin.
6071:caddy,  n.,  a  small  box;  orig.  used  only  in  the  sense of  tea  caddy.  - —  Fr.  earlier  catty,  prop,  ‘a  box containing  a  catty  of  tea’,  fr.  Malay  kati,  a weight  of  1  1/3  lb.  Cp.  catty, cade,  n.,  a  small  barrel.  —  F.,  fr.  L.  cadus,  ‘bottle, jar,  jug’,  fr.  Gk.  xaSo?,  fr.  Heb.  kadh,  ‘pitcher’, prop,  ‘a  rounded  vessel’,  fr.  base  *k-d-d,  ‘to  be round’.  Cp.  cadus.
6081:cadmium,  n.,  a  white  metallic  clement  (chem.)  — ModL.,  coined  by  its  discoverer,  the  German chemist  Friedrich  Strohmeyer  (1776-1835)  in 1817,  fr.  L.  cadmia,  ‘calamine’,  fr.  Gk.  xa8p.s(5, of  s.m.,  which  stands  for  Ka8p.e(a  (scil.  yr)),  lit. ‘Cadmean  (earth)’,  fr.  KaSpoi;,  ‘Cadmus’.  See next  word.
6087:Caecias,  n.,  personification  of  the  northeast wind.  —  L.  caecias,  fr.  Gk.  xaixtac,  ‘northeast wind’,  lit.  ‘the  dark  one’,  cogn.  with  L.  caecus, ‘blind’;  see  next  word.  For  sense  development cp.  Aquilo.
6089:Caeoma,n.,a  form  genus  of  rusts  (hot.)  —  ModL., fr.  Gk.  xaiciv,  which  prob.  stands  for  x<x.t-jlelv, ‘to  burn’,  whence  xauaxii;,  ‘burnt’,  xaucm x6?, ‘capable  of  burning'  (see  caustic);  so  called because  of  its  fiery-red  color.
6124:Calamagrostis,  n.,  the  reed  bent  grass  (bot.)  — ModL.,  compounded  of  Gk.  xaXapoc,  ‘a  reed’, and  aypcooTK;,  ‘a  grass’.  See  Calamus  and Agrostis.
6127:calamint,  n.,  an  aromatic  plant.  —  ME.  calament, fr.  OF.  calament .  fr.  ML.  calamentum,  fr.  L.  cala- minthe,  fr.  Gk.  xaXxpivtb;,  which  is  compounded of  xxXot(io?,  ‘reed’,  and  piv9v;,  ‘minth’.  See calamary  and  mint,  ‘an  aromatic  herb’.  For  the contraction  of  *xaXot[xo-}uv(b}  into  xaXapfvfbj see  haplology.
6133:Calanthe,  n.,  a  genus  of  orchids  (bot.)  —  ModL., compounded  of  Gk.  xaXo?,  ‘beautiful’,  and Svffo?,  ‘flower’.  See  calo-  and  anther, calapite,  n.,  mass  found  in  coconuts.  —  Fr.  Malay kalapa,  ‘coco  tree’.
6136:Calathea,  n.,  a  genus  of  plants  of  the  arrowroot family  (bot)  —  ModL.,  fr.  Gk.  xaXaffoi;,  ‘bas¬ ket’  (see  next  word);  so  called  from  the  shape of  the  flowers.
6176:Derivative :  calender-er,  n. calends,  kalends,  n.  pi.,  the  first  day  of  the  an¬ cient  Roman  month.  —  ME.  kalendes,  fr.  OE. calend,  ‘month’,  fr.  L.  calendae,  kalendae,  ‘the first  day  of  the  month’,  fr.  calare,  ‘to  call,  pro¬ claim’,  which  is  rel.  to  Umbr.  karetu,  karitu, carsitu  ( =  L.  caldtd),  ‘thou  shah  (or  he  shall) call’,  and  cogn.  with  Gk.  xaXeto,  ‘IcaH’.xeXaSo;, ‘noise,  din’,  xsXxpu^eiv,  ‘to  rush,  purl’,  xeXcop (Hesychius),  ‘sound,  voice’,  Lett,  kaluot,  ‘to chatter',  OHG.  halon,  ‘to  call’,  hellan,  ‘to  re¬ sound’,  hell,  ‘resounding’,  OIr.  cailech,  W.  cei¬ ling,  Co.  chelioc,  Bret.  kiVek,  ‘cock’,  Lith.  kalba, language’,  kalbasyti,  ‘to  chatter’,  Lett,  kalada, ‘shouting,  noise’,  OPruss.  kaltza,  kelsai,  ‘it sounds’,  the  second  element  in  OI.  usa-kalah, ‘cock’.Toch.  B  kal(n)-,  AB  kal(n)-,  ‘to  resound'. Ail  these  words  are  derivatives  of  the  I.-E.  imi¬ tative  base  *kel-,  *kal-,  ‘to  shout,  resound’.  Cp. calendar,  Calendula,  intercalary,  conciliate, council.  Cp.  also  claim,  v.,  clear,  ecclesia.  Cp. also  low,  ‘to  make  the  sound  of  a  cow’. Calendula,  n.,  a  genus  of  plants  of  the  thistle family  (bot.)  —  ModL.,  fr.  L.  calendae,  hence lit.  meaning  ‘the  plant  blossoming  at  the  time of  calends’.  See  prec.  word  and  -ule. calenture,  n.,  tropical  fever.  —  Sp.  calentura,  fr.
6190:caliginosity,  n.,  dimness,  darkness.  —  Formed with  suff.  -ity  fr.  L.  caliginosus.  See  prec.  word, caligo,  n.,  dimness  of  sight  ( med .)  —  L.  caligo, ‘darkness’.  See  caliginous. caliology,  n.,  the  study  of  birds’  nests.  —  Com¬ pounded  of  Gk.  xaXia,  ‘hut,  nest’,  and  -Xoyla, fr.  -Xiyos,  ‘one  who  speaks  (in  a  certain  man¬ ner);  one  who  deals  (with  a  certain  topic)’.  The first  element  is  rel.  to  xaX.ujJy],  ‘hut,  cabin’, 'to  cover,  hide,  conceal’,  and  cogn. with  L.  cella,  ‘storeroom,  granary’,  celare,  ‘to hide,  keep  secret’,  occulere,  ‘to  cover,  conceal’; sec  cell  and  words  there  referred  to  and  cp.  esp. kalidium.  For  the  second  element  sec  -logy. Derivatives:  caliolog-ic-al ,  adj.,  caliolog-ist,  n. calipash,  n.,  the  edible  greenish  substance  found next  to  the  upper  shell  of  a  turtle.  —  Prob. alter,  of  carapace.
6198:tics  tending  to  promote  grace  and  health;  2)  (con¬ strued  as  a  singular)  the  art  of  such  gymnastics. —  Compounded  of  Gk.  xaXXoi;,  ‘beauty’,  and abevo;,  ‘strength’.  Gk.  xa Xkoc,  derives  fr.  xotXoc, ‘beautiful’;  see  calo-.  For  the  second  element see  sthenic  and  cp.  asthenia,  neurasthenia.  For the  ending  of  calisthenics  see  suff.  -ics. calk,  caulk,  tr.  v.,  to  stop  up  the  seams  of  a  ship with  oakum.  —  The  original  meaning  was  ‘to tread’,  fr.  ME.  cauken,  fr.  ONF.  cauquier,  corre¬ sponding  to  OF.  cauchier,  chauchier  (F.  cocher), ‘to  tread’,  fr.  L.  calcare,  ‘to  tread’,  fr.  calx,  gen. calcis,  ‘heel’.  See  Calceolaria  and  cp.  words there  referred  to.
6210:calligraphy,  n.,  beautiful  writing.  —  Gk.  xaXXt- Yp*<pta,  fr.  xaXXcypacpoe,  ‘a  calligrapher’,  which is  compounded  of  xaXXo?,  ‘beauty’  and  -ypatpop, fr.  ypatpEiv,  ‘to  write’.  The  first  element  derives fr.  xaXo;,  ‘beautiful’;  see  calo-.  For  the  second element  see  -graphy.
```


## [2026-09-05T14:53:27.949Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"papyrus\" KLN_1966.txt | head -20",
 "description": "grep papyrus in Klein"
}
```


### [2026-09-05T14:53:28.049Z] TOOL RESULT

```
4908:Bible,  n.  —  ME.  bible,  fr.  OF.  (  —  F.)  bible,  fr.  L. biblia,  fr.  Gk.  fkpxia,  ‘collection  of  writings’, pi.  of  [hpXtov,  ‘paper,  scroll,  book’.  This  is  the dimin.  of  JiLpXog,  (luJiXog,  ‘the  inner  bark  of papyrus;  book’,  fr.  BupXog,  Greek  name  of  the famous  Phoen  transit  port,  whence  the  Greeks obtained  the  Egyptian  papyrus,  Gk.  BufSXog  has been  assimilated  fr.  Gebhdl,  the  Heb.-Phoen.
6522:Derivatives:  eard-ed,  adj.,  card-er,  n. card,  n.,  a  piece  of  pasteboard  for  playing.  —  F. carte,  fr.  Late  L.  carta,  ‘a  leaf  of  paper;  paper’, fr.  L.  charta,  ‘a  leaf  of  the  Egyptian  papyrus; papyrus;  paper',  fr.  Gk.  yip rqp,  of  s.m.,  a foreign  word,  possibly  of  Egypt,  origin.  Cp. carte  blanche,  carte  de  visite,  cartel,  cartoon, cartouche,  cartridge,  cartulary,  chart,  charter, ecartc,  skat.
26899:Derivative:  packet,  tr.  v. pact,  n.  —  ME.,  fr.  MF.  pact  (F.  pacte),  fr.  L. pactum,  ‘contract,  covenant’,  prop.  neut.  pp.  of paciscor,  pacisci,  ‘to  covenant,  make  a  treaty, agree,  stipulate’,  rel.  to  pax,  gen.  pads,  ‘peace’, fr.  I.-E.  base  *pak-,  *pdg-,  ‘to  join  together, unite,  make  firm,  fasten,  fix’,  whence  also  L. pangere,  ‘to  join,  make  firm’,  pagus,  ‘district, province,  village’,  pagina,  ‘strips  of  papyrus fastened  together,  page’,  pains  (for  *pak-slos), ‘post,  stake’,  OI.  pas-,  pasa-,  ‘cord,  rope’,  Avestic pas-,  ‘to  fetter’,  Gk.  7n)yvtSvat,  ‘to  fix,  make firm,  fast  or  solid,  to  harden,  freeze’,  n ayrj, ‘snare,  noose’,  lit.  ‘anything  that  fixes’,  7tayoi;, ‘something  solid;  mountain  peak,  rocky  hill’, Tiayio;,  ‘solid’,  Tt  ay  croc,  ‘frost’,  7r5jy|AX,  ‘some¬ thing  fastened  together’,  itrfcz,  ‘a  making  firm, fastening’,  TratroaXoc  (for  *7rax-iaXo<; ),  ‘peg’, Russ.  pazU,  ‘joint’,  Slovenic  paz,  ‘partition  (of planks’),  OE.  fxc,  ‘space,  period  of  time',  OE. fegan,  ‘to  join’,  fort,  ‘to  catch,  seize’,  OE.  fieger, OHG.  fagar,  ‘beautiful’.  Cp.  appalto,  appease, Areopagus,  compact,  adj.,  n.,  and  v.,  compages, dispatch,  fay,  ‘to  join’,  hapax  legomenon,  im¬ pact,  impinge,  pace,  ‘with  the  leave  of’,  pachno- lite,  pagan,  page,  ‘side’,  pageant,  Paguridae,  pail, pale,  ‘boundary’,  parapegm,  pax,  paxilla,  pay, ‘to  requite’,  peace,  pectin,  pectolite,  Peganum, pegmatize,  -pexy,  pole,  ‘stake’,  propagate.  Cp. also  fair,  ‘beautiful’,  fake,  fang,  fay,  ‘to  join’, feague.
26930:page,  n.,  one  side  of  a  leaf  of  a  book.  —  OF.  (= F.),  fr.  L.  pagina,  ‘strips  of  papyrus  fastened together,  page,  leaf,  slab’,  fr.  I.-E.  base  *pag-, pak-,  ‘to  join  together’,  whence  also  L.  pangere, to  join,  make  firm’,  pax,  gen.  pads,  ‘peace’, pacisci,  ‘to  make  a  treaty’.  See  pact  and  cp. pagan.  Cp.  also  pail,  peg.
27213:paper,  n.  —  ME.  papire,  papir,  fr.  OF.  (=  F.) papier,  fr.  L.  papyrus,  ‘papyrus,  paper  made  of papyrus  stalk’,  fr.  Gk.  nx-Kupoc.  ‘papyrus’.  See
27214:papyrus.
27216:papeterie,  n.,  a  box  for  paper  and  other  writing materials.  —  F.,  fr.  papetier,  ‘papermaker’,  fr. papier,  ‘paper’.  See  prec.  word  and  -ery. papier-mache,  n.,  paper  pulp  molded  into  various objects.  —  F.,  lit.  ‘chewed  paper’,  fr.  L.  papyrus, ‘papyrus,  paper’,  and  masticatus,  pp.  of  masti- care,  ‘to  chew’.  See  paper  and  masticate. Papilio,  n.,  a  genus  of  butterflies  (zool.)  ■ —  L.  pd- pilid,  ‘butterfly’;  cogn.  with  OE.  fifealdc,  ‘but¬ terfly’,  OS.  fifoldara,  ON .fifrildi,  OHG.  vivaltra, MHG.  vivalter,  G.  Falter,  of  s.m.  These  words derive  from  the  reduplicated  form  of  the  I.-E. base  *pel-,  ‘to  shake,  swing’.  Cp.  Lith.  piepala, Lett,  paipala,  ‘quail’,  which  are  from  the  same reduplicated  base.  Cp.  papillon,  pavilion.  For derivatives  of  the  simple  base  *pel-  see  polemic. Derivative:  papilion-aceous,  adj.
27229:papyro-,  combining  form  meaning  ‘papyrus’.  — Fr.  Gk.  TrxTtupop.  See  papyrus, papyrograph,  n.,  an  instrument  for  multiply¬ ing  copies  of  writings.  —  Compounded  of  pa¬ pyro-  and  Gk.  -ypaipot;,  fr.  ypitpciv,  ‘to  write’. See  -graph.
27231:papyrus,  n.  —  ME.  papirus,  fr.  L.  papyrus,  fr. Gk.  ■na.Tvopoq,,  ‘papyrus’,  which  is  of  unknown
30681:Protococcus,  n.,  a  genus  of  green  algae  (hot.)  — ModL.,  compounded  of  proto-  and  coccus, protocol,  n.  —  MF.  prothocole  (F.  protocole),  fr. ML,  protocollum,  fr.  Late  Gk.  TrpoiTozoXXov, ‘the  first  leaf  glued  to  the  papyrus  roll’,  which  is compounded  of  Gk.  Trptoxo?,  ‘first’,  and  xoXXx, ‘glue’.  See  proto-  and  collo-  and  cp.  words  there referred  to.
34009:schedule,  n.  —  L.  schedula,  ‘a  small  leaf  of  paper’, dimin.  of  scheda,  scida,  ‘a  strip  of  papyrus  bark, a  leaf  of  paper’,  fr.  Gk.  cr/iSr,,  ‘splinter  of wood’,  from  the  stem  of  ayi'leiv,  ‘to  cleave, split’.  See  shed,  v.,  and  cp.  schism.  For  the  end¬ ing  see  suff.  -ule.  Fr.  ML.  cedula,  a  simplified form  of  L.  schedula,  derive  It.  cedola,  Sp.  cedula, F.  cedule,  ‘schedule’.  Cp.  cedula.
38175:taper,  n.,  a  small  candle.  —  ME.  tapre,  taper,  fr. OE.  tapor,  tapur,  dissimilated  fr.  L.  papyrus (through  the  intermediate  form  *tapurus ).  Cp. dial.  It.  papijo,  papejo,  ‘wick’,  Sard,  pavilu, Rhaeto-Rom.  pavier,  pave!,  of  s.m.  All  these words  derive  fr.  L.  papyrus  (see  papyrus,  paper). For  the  development  of  meaning  it  should  be borne  in  mind  that  the  pit  of  papyrus  was  used in  Rome  as  wick.  For  a  similar  development  of meaning  cp.  OHG.  charza,  kerza  (whence MHG.,  G.  kerze),  ‘candle-,  fr.  L.  charta ,  fr.  Gk. ^apx/jq,  ‘papyrus; roll  made  from  papyrus;  the wick  made  from  the  pith  of  the  papyrus'. Derivatives:  taper,  adj.,  tapering,  taper,  intr. and  tr.  v.,  taper-er,  n.,  taper-ing,  adj.,  taper-ing- ly,  adv.,  taper-ness,  n.,  taper-wise,  adv.
```


## [2026-09-05T14:53:38.033Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nd=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nfor i,p in enumerate(pages):\n    if 'card,  n.,  a  piece  of  pasteboard' in p:\n        print('leaf',i, re.findall(r'\\b2[0-9]{2}\\b',p)[:10])\n    if 'charlatan,  n.,  a  pretender' in p:\n        print('charlatan leaf',i, re.findall(r'\\b2[0-9]{2}\\b',p)[:10])\nEOF\necho \"--- carton/chart/cartoon entries\"; grep -n \"carton,\\|cartoon,\\|^chart,\" KLN_1966.txt | head -10",
 "description": "Klein leaf/page for card"
}
```


### [2026-09-05T14:53:39.756Z] TOOL RESULT

```
leaf 136 ['272', '238', '239']
charlatan leaf 152 ['268', '269']
--- carton/chart/cartoon entries
6522:Derivatives:  eard-ed,  adj.,  card-er,  n. card,  n.,  a  piece  of  pasteboard  for  playing.  —  F. carte,  fr.  Late  L.  carta,  ‘a  leaf  of  paper;  paper’, fr.  L.  charta,  ‘a  leaf  of  the  Egyptian  papyrus; papyrus;  paper',  fr.  Gk.  yip rqp,  of  s.m.,  a foreign  word,  possibly  of  Egypt,  origin.  Cp. carte  blanche,  carte  de  visite,  cartel,  cartoon, cartouche,  cartridge,  cartulary,  chart,  charter, ecartc,  skat.
6630:Derivatives:  cartograph-er ,  n.,  cartograph-y,  n. cartomancy,  n.,  divination  from  cards.  F.  car- tomancie ,  a  hybrid  coined  fr.  F.  carte,  ‘playing card’,  and  Gk.  ijixvTrix,  ‘oracle,  divination'. See  card,  n.,  ‘a  piece  of  pasteboard’,  and  -mancy. carton,  n.,  a  cardboard  box.  —  F.  See  next  word, cartoon,  n.,  1)  a  drawing  on  strong  paper;  2)  a comic  strip.  —  F.  carton,  'pasteboard',  fr.  It. cartone,  augment,  of  carta,  ‘paper’.  See  card, n.,  ‘a  piece  of  pasteboard’.
6631:Derivatives:  cartoon,  v.,  cartoonist  (q.v.) cartoonist,  n  A  hybrid  coined  fr.  cartoon  and -ist,  a  suff.  of  Greek  origin, cartouche,  n.,  I)  a  scroll-like  ornament;  2)  an oval  figure  containing  the  name  or  title  of  an Egyptian  deity  or  king.  —  F.,  fr.  It.  cartoccio, lit.  ‘a  roll  of  paper’,  fr.  carta,  fr.  Late  L.  carta. See  card,  ‘a  piece  of  pasteboard’,  and  cp, next  word.
```


## [2026-09-05T14:54:12.193Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FVQ grep kirtas variants ===\"; grep -n -i \"kirtas\\|Kirṭās\\|qartis\\|χάρτης\\|carthes\\|chartes\" FVQ_pages.txt | head; echo \"=== FVQ arabic script ===\"; grep -n \"قرطاس\" FVQ_pages.txt FVQ.txt | head; echo \"=== AFA ===\"; grep -n -i \"irtas\\|arṭīs\\|qarṭīsā\\|χάρτ\" AFA.txt | head",
 "description": "grep FVQ and Fraenkel for qirtas"
}
```


### [2026-09-05T14:54:12.261Z] TOOL RESULT

```
=== FVQ grep kirtas variants ===
=== FVQ arabic script ===
=== AFA ===
```


## [2026-09-05T14:54:14.235Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT ===\"; grep -n \"^CARD\\|^CHART\\|^CHARADE\\|^CHARLATAN\\|^TEA\" SKT.txt | head; echo \"=== LKT tea/chai ===\"; grep -n -i \"\\bt'e\\b\\|Tee (\\|čāi\\|tschai\" LKT.txt | head",
 "description": "grep Skeat and Lokotsch"
}
```


### [2026-09-05T14:54:14.294Z] TOOL RESULT

```
=== SKT ===
2981:CARD.
=== LKT tea/chai ===
```


## [2026-09-05T14:54:19.378Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FVQ Q entries ===\"; grep -n -i \"^ *Qir\\|Qirtas\\|Qir[!t]\" FVQ_pages.txt | head -20; echo \"=== FVQ list of headwords starting Q ===\"; grep -n -iE \"^[[:space:]]*(Qi|Ki)[a-z]{2,}\" FVQ_pages.txt | head -30",
 "description": "FVQ headwords Q"
}
```


### [2026-09-05T14:54:20.900Z] TOOL RESULT

```
=== FVQ Q entries ===
8490:l^LLOJ (Qirtds).
=== FVQ list of headwords starting Q ===
1068:kingdoms, belongs to the S. Semitic group, and is closely related to
1151:kingdom of Ghassan the dominant party appears to have been Mono-
2222:King of Berossus, but this is very far-fetched.
3444:KificoTO?), and the ark of papyrus in which Moses \yas hidden (Gk.
4596:kind of bread. It was probably an early borrowing into Arabic, for
7272:Kinship, 300.
8088:Kings, 2 e.g. ^fwo6,i,ii,7,etc. After this date it is used fairly frequently,
8794:Qintar a measure.
9717:kingdom, etc., to be derived from this.
9726:Kingdom, dominion.
10590:Qisas, 75). Zam. on xii, 4, in his usual vigorous style combats the theory
11082:Kira 84
11102:Kisa^a 154
11119:Kill 287
11128:KIVT 157
11287:KIOOp 240
11358:KIKin 90, 91
11631:Kind 247
```


## [2026-09-05T14:54:21.233Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2975,3000p' SKT.txt; echo \"=== LKT ===\"; grep -n \"Tee\\b\" LKT.txt | head -10; echo \"=== LKT chai ===\"; grep -n -i \"cha\\b\\|tschai\\|Tschāj\" LKT.txt | head -10",
 "description": "Skeat CARD; Lokotsch Tee"
}
```


### [2026-09-05T14:54:21.305Z] TOOL RESULT

```
surcharge,  sb.  (F.-L.  and  C.)  F. TUTxharge,  an  over-charge. —  F.  sur  (  —  L. ti/ffry,  .ihove;    and  oharge  ^nbovc).
Caracole,  iF.- Span.  — C.  ?)  f.catxt^o!, taracoU.  a  snail ;  whence  fairt  U  caroiote. applied  to  a  mana-uvre  by  soldiers,  ami  to turns  made  by  a  hor^.— Spau.  iamcot,  a anAll,  winding  staircase,  turning  about  (from the  snnil-slteH's  spiral  form).  Pcthajis  of Celtic  oHi^Hn;  cL  Gael,  caituh^  circling, winding,  from  car,  a  Inm,  twist.
Carat.  (F.-Arab.-Gk.)  F.  camt,  a Ifcry  light  weight,- Arab,  qirrdi,  a  pod. bosk,  carat.  24ih  part  of  an  ounce  *Gk. ic%p^to¥,  fruit  of  the  locust-tree;  also,  a CAtal;  lit.  'asmall  horn.' -Gk.*</»aT-,  stem of  «'par,  a  honi;  sec  Horn.
Caravan.  (F.-Pers.)  F.  caravam.'^ VtT%,  karufdn,  a  caravan,  convoy.
oaravanaary.  (Pen.)  Pcrs.  kanvdn- tardy^  cm  bin  for  camvans.  —  Fcrs.  kartptin, caravan;  saniy,  public  building,  uax,
van.  a  coNxied  wnggon  for  goods.  (F.— Pet^.)    Short   fox  rd/tfvui*.  luu    6m    fgr
CARD.
Caraway^  Carraway.  (Spaa.* Span,  ai-iiuxihutjfa.  a  caraway  { is    merely    the    Arab.    dcC    art. kartfiy.i'a,  karavfiyA-4t^  carava] plant.     Cf.  Gk.  ripot,  mipov,  comia.
Carbine.  cF.-Gk.)   Formeriy^ carai'in.  which  meant  (not  a  moJcel, the  man  who  carried  it,  a  ma&l carttbtH,  'an  arquebuziei;'  Cot. from  O.  F.  taiabrim^  a  Ught-aimed ortg.  a  soldier  who  worked  one  of war-engines  •>  Low  L.  thadaMa, a  destructive  war-engine.— Gk. overthrow,  dc^ructit'O.— Gk.  am to  cast  down,  strike  down  with Gk.  xaru.  down  ;  ^oAXtir,  to  cas accahUr,  also  from  cadaSuia,)
Carbon.  (F.-L.)    F.  ^sHmr.-Li carbotitm,  a  coal,
carbonado,  broiled  meat  (! Span,  carbonado,  rneat   broiled  o*tr —  Span,  carbon,  coal;  stc  abo^c.
carbuncle.  (L.)    L. small  co.ll,  (a)  a  carbur^. glowing.     Double  dimin.  uf  L
Carcanet.  [F.-C.)  Dimin a  collar    of  jewels,  or    of  g kcfxhtn,    the    bo'.oin,    circle    »■ al.so  kilchstu  a  collar.  —  Bret,  kc
Carcase,  Carcass,     ^F.-Iiai,i M.  E.  f*i/rjy/.  — O.  F.   can/matUt  i body.  — ItaL  cariassa.  a    kind   of shell,  a  ihcU ;  closely  allied   to also   furrasso,   a    quiver.      -   -    " being   likened    to   a  sh' rupted  from  Low  L.  /i3'. Pcrs.    tariiuh,  a    quiver Litlrd  that  F.  caryutu  pi same  word.)
Card  (]),  piece  of  pa&tcltoord.  (F.^Q Corruption    of  F.  *  ''  ''^
Low   JL  Citrra ;  L. leaf  of  paper.     Dei.  ..-
carte,  a  bill  of  fare.    < in  the  F.    phr.   oxr// pit]:ier.—  Low  L.  carfa;  stc  C;*.
eartoL    (F.-ltal  -Gk.) Itol.  carttJh.  lit.  a carta,  pnijcr,  bdl ;
cartoon  (!■*•*  i'      "  
ItaL  carutu,  Ut.A  large  paper:  fr«ca< aa  above.
cartouche,  cortri^'' Gk.'  CarfnJ^t   («ith    i ctxrhifge,  conn  pi  foim cartpufhi,  a  roll  of  paj a  roll  of  paper,  carlr.v;^..
ame  Irom  the up. rifcjMtr.  (Low  L.»Gk.^ tm,  ^Aar/m'arruiK,  r  rcgis- rm^^  a  document ;  dimin. iperj  ICC  Cird  above. «G1l)  L.  ikarta,  n  puper.^ asaImvcl
(r— I   Gk.)   Vi.Y^cMartrr.
nr*«.*Low  I,.  tJkarfuJa.   carfu/a. •ficroc docomeot :  ^ec  oartuliu7
t\  an   bKtrunieiit    for    combing «I*.5  F.  fOFJIf.  — Low  L.  cardtu, lUiiiile:  fof  wool-combing  — au4  wool.
(1-.)    L.  tarJinalii,  principal,
=== LKT ===
1109:'Tee';  cha-ye  'Teeblätter'  [so  ist  die Aussprache  im  Kuan-hoa,  s.  hier  Nr.  1400, und  im  Kantondialekt];  hieraus  pg.  chä, sp.  (selten)  cha,  russ.  cai,  bulg.  caj,  serb. iaj,  sej,  öech.  caj,  poln.  czajnik  ('Tee- kanne'), czaj.  —  Im  Dialekt  von  Amoy, von  wo  aus  vermutlich  die  ersten  Tee- ladungen ausgegangen  sind,  wird  etwa te  gesprochen,  daher  frz.  the,  sp.  te,  it. U  [seltener  ciä],  ndl.  thee,  dtsch.  Tee, engl,  tea  [früher  wie  im  Deutschen  aus- gesprochen, vgl.  die  beweisenden  Reime in  dem  1712  geschriebenen  Rape  of  the Lock  von  Alexander  Pope,  Canto  I,  61 u.  62;  III,  7/8;  etwa  in  der  Ausgabe Pandora  Nr.  11  (Inselverlag  Leipzig), S.  10  u.  2.3].  Übrigens  hat  das  Neu- griechische beide  Aussprachen  über- nommen :  TOai  und  Teiov.  [Nichts  mit engl,  tea  zu  tun  hat  erigl.  tee-totaller 'Abstinenzler';  dies  ist  vielmehr  die Aussprache  der  Abkürzung  T.  total, d.  h.  temperance  total.]  [Gorjajew  407. Bern  SlEtWb  134.   Hirth  ChinFW  201.
2153:'Wasserkrug',  besonders  für  die  vor- geschriebenen Waschungen  der  Muslimen gebraucht  [aus  dem  Pers.,  doch  kennt man  das  pers.  Grundwort  noch  nicht, vgl.  de  Lagarde,  Gesammelte  Abhand- lungen S.  7];  tk.  ebenso;  hieraus  rum. ibric  'Wasserkrug,  Wasserkanne',  it. bricco  'Zinnkanne  für  Kaffee',  bulg.  serb. ibrik  'Waschkanne,  Krug',  serb.  imbrik, Y)o]n.imb)yk,  imhryczek  'Tee-  oder  Kaffee- kanne', klruss.  imbrycek  'dass.'.  [ML 4253.    Bern  SlEtWb  419.
3704:'Fünf  [Horn  NpEt  S.  73,  Nr.  328;  vgl. päng-äb  'Pandschab',  engl.  Schreibung Punjaub  'FOnfstromland'] ;  hieraus  engl. punch,  dtsch.  Punsch,  ein  Getränk,  das aus  fünf  Zutaten  hergestellt  wird:  Arrak, Zucker,  Zitronensaft,  Wasser  (oder  Tee) und  Gewürz  (Zimt)  [SCHILLER  läßt  in seinem  Punschlied  das  letzte  aus  und singt:  ,Vier  Elemente  /  Innig  gesellt  / Bilden  das  Leben  /  Bauen  die  Welt."]; sp.  ponche,  rum.  punciü,  russ.  punS. [Ho'oson-Jobson  737/739.    Kluge  353.
4846:N.  pr.,  Gebirge  in  der  chin.  Provinz Fukien,  auf  dessen  Abhängen  lange  Zeit der  beste  Tee  gezogen  wurde.  Die  lokale Aussprache  des  ersten  Bestandteiles  [der zweite  heißt  'Gebirge',  vgl.  Tien-shaii 'Himmelsgebirge']  ist  bohi  und  ging  so ins  engl,  bohea  in  der  Bedeutung  'Tee' über,  z.  B.  Pope,  Rape  of  tbe  lock, Canto  IV,  156;  heute  ist  engl,  bohea eine  geringwertige  Sorte  schwarzen  Tees.
4847:Auch  im  botanischen  Namen  der  Tee- pflanze Thea  bohea  kommt  das  chin. Grundwort  wieder  vor.  [Hirth  ChinFW 209.
5880:Sorfoei  1838 Sorgweizen  551 so</'<';  mhd.  1927 Souchong  (Tee)  1889 Spinat  126 Stambulina  1931 Ströhzicher  1004 S<)«iS  j.  1927 Sm^^xh  194.^^ Sumach  1946 Suradain  St.  1949
=== LKT chai ===
461:'Gerste';  mit  Deminutivsuffix  arpagyk 'Gerstenkorn,  spanische  Zwiebel';  hier- aus rum.  arpagic  'Schnittlauch,  Scha- lotte' [s.  hier  Nr.  119],
491:Lat.  Ascalon,  n.  pr.,  eine  Stadt  im  süd- lichen Palästina;  danach  wurde  eine Zwiebelart  als  cepa  ascalonla  bezeichnet; hieraus  unter  Wegfall  des  Substantivums [wie  bei  frz.  fromage  aus  lat.  lac  for- maticuni]  aprov.  escalonha,  afrz.  escha- logne,  it.  scalogno,  sp.  escalona;  mit  Suf- fixwechsel frz.  Schalotte,  pg.  xalota; dtsch.  Schalotte,  Aschlauch.  In  der Vendee  dial.  Schalotte  'derbe  Tracht Prügel'.  [Behrens  Beiträge  87.  ML  694.
1067:shahraclc,  ndl.  scliuhrak,  dtsch.  Scha- bracke 'Satteldecke',  wohl  über  ung. csdprdg.  [Gorjajew  407.  Bern  SlEtWb 136.    ML  8961.
1108:415.  Chiu.  cha:
1109:'Tee';  cha-ye  'Teeblätter'  [so  ist  die Aussprache  im  Kuan-hoa,  s.  hier  Nr.  1400, und  im  Kantondialekt];  hieraus  pg.  chä, sp.  (selten)  cha,  russ.  cai,  bulg.  caj,  serb. iaj,  sej,  öech.  caj,  poln.  czajnik  ('Tee- kanne'), czaj.  —  Im  Dialekt  von  Amoy, von  wo  aus  vermutlich  die  ersten  Tee- ladungen ausgegangen  sind,  wird  etwa te  gesprochen,  daher  frz.  the,  sp.  te,  it. U  [seltener  ciä],  ndl.  thee,  dtsch.  Tee, engl,  tea  [früher  wie  im  Deutschen  aus- gesprochen, vgl.  die  beweisenden  Reime in  dem  1712  geschriebenen  Rape  of  the Lock  von  Alexander  Pope,  Canto  I,  61 u.  62;  III,  7/8;  etwa  in  der  Ausgabe Pandora  Nr.  11  (Inselverlag  Leipzig), S.  10  u.  2.3].  Übrigens  hat  das  Neu- griechische beide  Aussprachen  über- nommen :  TOai  und  Teiov.  [Nichts  mit engl,  tea  zu  tun  hat  erigl.  tee-totaller 'Abstinenzler';  dies  ist  vielmehr  die Aussprache  der  Abkürzung  T.  total, d.  h.  temperance  total.]  [Gorjajew  407. Bern  SlEtWb  134.   Hirth  ChinFW  201.
1582:N.  pr.,  eine  Stadt  in  TripoUs  (Nordafrika), dazu  das  Adj.  gadämasi  zur  Bezeichnung des  hier  hergestellten  Leders ;  hieraus sp.  pg.  guadameci,  pg.  guadamecim,  afrz. godemetin  'gepreßtes  oder  vergoldetes Leder';  sp.  gorromazos  'große  Reiter- stiefel' [weil  ursprünglich  aus  solchem Leder],  prov.  garamacha,  frz.  (dial.)  ga- ramaches  'dass.',  frz.  gamaches  [veraltet, jetzt  guetres]  'knöpf  bare  Überstrümpfe', dlsch.  Gamaschen.  —  [Ableitung  aus lat.  *gambacea  aus  gamba  'Bein'  erklärt nicht  alle  vorkommenden  Formen.  [DE 280/281.  Eguüaz  414.  Devic  DEt  124. ML  3751.
1733:706.  Jap.  geisa: 'Berufsmäßige  Sängerin  und  Tänzerin ; Tanzmädchen';  hieraus  in  allen  euro- päischen Sprachen  Geischa,  meist  engl. geisha.    [Chamb  AllJap  467/468.
1744:gutta  Hooker';  gStah-percah  ist  also  der gummiartige  Saft  des  Pertschabaumes, der  zuerst  in  den  Wäldern  von  Singapur den  Malayen  bekannt  wurde  und  .sich .^eit  dem  Jahre  1843  über  ganz  Europa und  Amerika  in  den  Industrien  verbreitet hat.  Engl. gufia-percha,  hz. guita-percha, sp.  giUapercha,  pg.  guftapet-cha,  it.  gutta perca;  dtsch.  Guttapercha,  ndl.  schw. glitta-percha,  dän.  gutta-perka;  russ. gutta-perca,  gutaper  ca.  —  Im  frz.  gomnie- gutte  ist  also  der  zweite  Bestandteil nichts  anderes  als  die  Übersetzung  des ersten  Teiles.  [Devic  DEt  134.  MMM 23/24.  25.  JAOS  XVHI,  54/58.
2018:'Artischocke,  Cynara  scolymus';  hieraus mit  ar.  Art.  sp.  alcarchofo,  alcachofa, pg.  alcachofra,  it.  carciofo,  articiocco, frz.  artichaut,  prov.  arqtiichaut,  archi- chaut;  ndl.  artisjoJc,  engl,  artichoke, dtsch.  Artischocke  (Erdschocke);  russ. artisok,  cech.  articok,  poln.  karczoch, klruss.  karcocha.  —  [Andere  Ableitungen, wie  aus  gr.  dpiuTiKci  'gewürzte,  ein- gemachte Dinge'  oder  aus  einem  an- geblichen ar.  ardl  sauki,  sind  sprachlich unhaltbar;  freilich  ist  die  letztere  Form sogar  in  ar.  Nationalwörterbücher  wie den  Mubit  al-muhit  übergegangen,  ob- wohl ihre  Unrichtigkeit  schon  lange  be- wiesen war,  s.  Dozy  Oost  18/22.]  — Vgl.  auch  hier  Nr.  563.  [DE  83.  Kluge 23.  Bern  SlEtVVb  489.  ML  1865  und 4060  (charsof  und  harsaf  gehören natürlich  zu  einer  Nummer  zusammen).
2090:GuDst  geschenkt  wurde;  ursprünglich ein  'Kleidungsstück'  ganz  allgemein; wahrscheinlich  selbst,  Entlehnung  aus dem  Pers.  oder  Türk.,  da  die  Nisba zwischen  hWl  und  huVi  sowie  das  Vb. zwischen  }iaWa  und  kaWa  'schenken' schwanken],  tk.  halat;  hieraus  rum. halat,  russ.  Jialat,  serb.  hahjna  'Schlaf- rock', poln.  klruss.  cha/at  'Kaftan';  sp. gala  'Kleiderpracht',  it.  gala,  frz.  habit de  gala,  dtsch.  Gala,  engl.  gala.  Sp. galano  [eigentlich  'in  Gala  gekleidet'] 'höfisch,  artig',  hieraus  dtsch.  Galan [über  den  Wiener  Hof,  da  das  Wort  im Frz.  fehlt] ;  it.  sp.  galante  'zierlich  und modisch  gekleidet',  frz.  galant,  dtsch. galant,  dazu  frz.  galanterie  'Höflichkeit, modisch  feines  \ieaehmen\  galanthot7ime, it.  galantuomo,  dtsch.  Galanter-ie(v^tivei\). [Dagegen  stammt  elegant  aus  dem  lat. elegantem  'wählerisch'.]  — •  Die  anderen Ableitungen  scheinen  begrifflich  weniger einfach:  a)  gr.  plur.  KoXd  'schöne  Dinge', wobei  k  y  g  wie  in  KÖXTTog  >  Golf; b)  afrz.  gnle  'das  Ergötzen',  so  Kluge 154;  c)  ahd.  geili  'Prunk,  Üppigkeit, Lustigkeit'  nach  Diez.  [Gorjajew  394. Bern  SlEtWb  383.
```


## [2026-09-05T14:54:37.454Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"چای\" \"قرطاس\" \"کارت\" \"شارلاتان\"; do echo \"=== $w ===\"; grep -c \"$w\" MON_part1.txt MON_part2.txt 2>/dev/null; done",
 "description": "Count Persian words in Mo'in"
}
```


## [2026-09-05T14:54:38.549Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la MON_part1.txt MON_part2.txt BQT_v2_pages.txt 2>/dev/null; echo ---; head -c 600 MON_part1.txt",
 "description": "Inspect Mo'in files"
}
```


### [2026-09-05T14:54:39.194Z] TOOL RESULT

```
=== چای ===
MON_part1.txt:48
MON_part2.txt:52
=== قرطاس ===
MON_part1.txt:1
MON_part2.txt:1
=== کارت ===
MON_part2.txt:32
MON_part1.txt:24
=== شارلاتان ===
MON_part1.txt:2
MON_part2.txt:0
```


### [2026-09-05T14:54:39.244Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4339896 Sep  4 14:06 BQT_v2_pages.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
---
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
و ده ها وی مزا موی
```


## [2026-09-05T14:54:44.442Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"قرطاس\" MON_part1.txt MON_part2.txt; echo \"=== sharlatan ===\"; grep -n \"شارلاتان\" MON_part1.txt",
 "description": "MON hits context"
}
```


### [2026-09-05T14:54:44.505Z] TOOL RESULT

```
MON_part1.txt:93341:ج. طوامیر. قرطاس مصری که از بردی 
MON_part2.txt:18658:قرطاس. ضح. در قدیم اين کلمه در عرسی و 
=== sharlatan ===
49416:حقه‌از» شارلاتان. 
82946:شارلاتان؛ 12120 (ص.) حقه‌باز» متقلب.
```


## [2026-09-05T14:54:44.604Z] TOOL CALL #30: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-05T14:54:44.611Z] TOOL RESULT

```


```


## [2026-09-05T14:54:51.847Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '18650,18670p' MON_part2.txt; echo \"=== part1 93335 ===\"; sed -n '93335,93350p' MON_part1.txt; echo \"=== sharlatan ctx ===\"; sed -n '82940,82950p' MON_part1.txt",
 "description": "Mo'in context lines"
}
```


### [2026-09-05T14:54:51.944Z] TOOL RESULT

```
آوای جنبش مهره و گلوله در مبان طاس و 
ماننل ۳ 

کاغذ: 272 [- کاغد (لظ. قد.) معر. ( کاغذ 
از بوست درحت توت) «لوفر»] (.) ورقه 
نازکی که از خمیر مواد مختلف نباتی و لته و 
کهنه و کاه به رنگ‌های گونا گون تهیه کنند 
و غالبا بر آن چیز نویسند یا چاپ کنند) 
قرطاس. ضح. در قدیم اين کلمه در عرسی و 
فارسی با «دال» مهمه تلفظط می‌شد ۵ مع‌هدا 


۱۳۰۸ 
گاهی با ردال» معجمه نیز, آمده. مکتوب؛ 
مراسله» رقعه» نامه. کاغذ مصری: (گٌیا.) 
گیاهی است از تیرهٌ جگن‌ها که از الیاف آن 
کاغذ می‌ساختند. ترکسات اسمی: کاغد 
ابری: نوعی کاغذ سیار ازک و لایه مانند. 
کاغذ اطفال: کاغذی که کودکان به ر سمان 
سته به هوا سر دهند. بادیادک. کاغد باد: 
کاغذ اطفال. کاغذ بتی: کاغذی که در فرنگ 
=== part1 93335 ===
مق. عرضا. 
طو ل دادن: «فةه-۱(ع. ف.] (مصل.) 
امرار وقت کردن,» به تأخیر انداختن کاری را. 
طومار: عقست؛ [معر. یو ] (.) نامه» کتاب. 
دفترء صفه. مکتوب؛ نوشته دراز. نوشتة 
لوله کرده» لولة کاغذ که درنوردیده باشند؛ 
ج. طوامیر. قرطاس مصری که از بردی 
(لوخ) و پاپیروس می‌ساختند. یکك طومار: 


(کد.) سخت دراز. یکك طومار گفتن: (کد.) 
تیار کته روده درازی کردن. منهزم 
کردن, فرار دادن. 

طوی: ۲ [تر.] (.) جشن» شادی. ضیافت» 
مهمانی. 
=== sharlatan ctx ===
شریف گردد. قدیم» کهن) ج. شرف» 
شرّف» شروف و شرف. (غم.) 

شار ق: 8570 [ع.] (افا.) تابان: تابنده» 
درخشان. 0( افتاب. 

شارلاتان؛ 12120 (ص.) حقه‌باز» متقلب. 
شاره: (م»)س«ق [هند. چیره؛ قس. ساره] (ا.) 
دستاری که در هندوستان مردان بر سر بندند. 
چادری رنگین و نازک که بیشتر زنان هند بر 
سر اندازند و يا بر تن خود بیچند» ساره.
```


## [2026-09-05T14:54:52.964Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/tea",
 "prompt": "Full etymology of \"tea\": Chinese cha / Amoy t'e, Malay teh, Dutch thee, French thé, and the chai forms. Quote the entry."
}
```


### [2026-09-05T14:54:59.105Z] TOOL RESULT

```
# Etymology of "Tea"

The word "tea" traveled to English through multiple linguistic pathways. According to Etymonline, the earliest English form was "chaa" (1590s), which came "from Portuguese cha, via Macao, from Mandarin (Chinese) ch'a."

The modern English form emerged via a different route: "via Dutch thee, from Malay teh and directly from Chinese (Amoy dialect) t'e, which corresponds to Mandarin ch'a."

The entry notes that "The modern English form (along with French thé, Spanish te, German Tee, etc.) reflects the role of the Dutch as chief importers of the leaves in that part of Europe (through the Dutch East India Company, from 1610)."

Related forms also entered English: chai emerged by 1908 "from the Russian or Arabic word for 'tea,'" while cha appeared in the 1590s as an alternative rendering of the Mandarin source word.
```


## [2026-09-05T14:55:07.341Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%86%D8%A7%DB%8C",
 "prompt": "Persian چای: give the full etymology section (source Chinese form, route, any mention of 茶葉 chá-yè, Turkic/Russian mediation) and the Persian pronunciation/meaning."
}
```


## [2026-09-05T14:55:09.045Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%82%D8%B1%D8%B7%D8%A7%D8%B3",
 "prompt": "Arabic قرطاس qirṭās: give the full etymology (Greek χάρτης? Aramaic/Syriac intermediary? Ancient Greek χάρτης 'papyrus sheet'), meanings, and any Persian section for قرطاس."
}
```


### [2026-09-05T14:55:13.971Z] TOOL RESULT

```
# Persian چای Etymology and Pronunciation

**Etymology:**
The Persian term derives "possibly from چا + ـی or from Chinese 茶葉/茶叶 (cháyè)." The word ultimately traces to Chinese origins through trade routes, though the exact transmission mechanism remains uncertain—either through suffix addition to a simpler form or direct borrowing of the compound term meaning "tea leaves."

**Pronunciation & Meaning:**
In Classical Persian, چای (čāy) is pronounced /ˈt͡ʃaːj/. Modern variants include Dari (/t͡ʃʰɑːj/), Iranian Persian (/t͡ʃʰɒːj/), and Tajik (/t͡ʃʰɔj/). The word denotes "tea"—the beverage made by steeping dried leaves in hot water. Audio pronunciation files are available for the Iranian Persian variant.
```


### [2026-09-05T14:55:15.539Z] TOOL RESULT

```
# Etymology and Meanings of قرطاس (qirṭās)

## Etymology

The word traces back through multiple languages: Ancient Greek *χάρτης* (khártēs) → Aramaic/Syriac *קַרְטִיסָא* (qarṭīsā) → Arabic *قرطاس*.

The Wiktionary entry states: "From Aramaic...from Ancient Greek *χάρτης* (khártēs)."

## Primary Meanings in Arabic

The word has four main definitions:

1. **Paper**: "paper; a sheet of paper, a page" (dated/uncountable or countable)

2. **Papyrus**: "papyrus; a sheet of papyrus" (archaic usage)

3. **Packaging**: "individual packaging, bag, wrapper, cone" (contemporary usage)

4. **Target**: "a mark that is fired at (such as a bullseye), a target" (obsolete)

## Note on Persian

The webpage provided does not include a dedicated Persian section, though it lists Persian (فارسی) among the 11 languages where this entry exists on Wiktionary. To access Persian definitions, one would need to visit the Persian Wiktionary directly.
```


## [2026-09-05T14:55:19.806Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/charlatan",
 "prompt": "Full etymology of charlatan: Italian ciarlatano, cerretano, Cerreto, ciarlare. Quote the entry."
}
```


## [2026-09-05T14:55:20.482Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/charade",
 "prompt": "Full etymology of charade: French charade, Provençal charrado, charra, imitative origin. Quote the entry."
}
```


### [2026-09-05T14:55:25.167Z] TOOL RESULT

```
# Etymology of Charlatan

The word "charlatan" entered English in the 1610s from French *charlatan*, meaning "mountebank, babbler." The French term derives from Italian *ciarlatano*, "a quack."

The ultimate origin traces to Italian *ciarlare*, meaning "to prate, babble," which comes from *ciarla*, "chat, prattle." According to etymological sources, this root is "perhaps imitative of ducks' quacking," suggesting onomatopoetic origins.

The term's journey reflects a path from Italian street performers and fraudsters to English usage describing anyone who falsely claims knowledge or expertise.
```


### [2026-09-05T14:55:27.693Z] TOOL RESULT

```
# Etymology of Charade

The word "charade" entered English in 1776 from French *charade* (18th century), which likely derives from Provençal *charrado*, meaning "long talk, chatter." The Provençal term probably comes from *charrar*, "to chatter, gossip," which has an echoic (imitative) origin. Related Romance language cognates include Italian *ciarlare* and Spanish *charlar*, both meaning "to talk, prattle."

Originally, a charade was "an enigma whose solution is a word of two or more syllables, each of which separately significant in sound" that players discovered through dialogue or dramatic representation. The modern silent version evolved from earlier "dumb charades," where performers acted out all syllables sequentially before guessing began. The game gained popularity in French society and was introduced to English drawing rooms by the mid-19th century.
```


## [2026-09-05T14:55:42.668Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /tmp && curl -s \"https://archive.org/metadata/originsofenglish00jose\" | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nprint(d.get('server'), d.get('dir'))\nprint([f['name'] for f in d.get('files',[]) if 'djvu' in f['name'] or 'text' in f['name']][:20])\n\" 2>&1 | head -20",
 "description": "IA metadata for Shipley OEW"
}
```


## [2026-09-05T14:55:44.530Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== POK ker- schallwurzel ===\"; grep -n \"Schallwurzel\" POK_full.txt | head -20; echo \"=== AHD watkins ker ===\"; grep -n \"^ker-\\|^gar-\\|^gher-\" AHD_watkins1985.txt | head -20",
 "description": "Pokorny sound roots"
}
```


### [2026-09-05T14:55:47.046Z] TOOL RESULT

```
ia800508.us.archive.org /0/items/originsofenglish00jose
['originsofenglish00jose.djvu', 'originsofenglish00jose_djvu.txt', 'originsofenglish00jose_djvu.xml', 'originsofenglish00jose_hocr_searchtext.txt.gz']
```


### [2026-09-05T14:55:47.118Z] TOOL RESULT

```
=== POK ker- schallwurzel ===
=== AHD watkins ker ===
479:gar-. To call, cry. Expressive root. 1. Germanic *kar6, lament, hence grief, care, in: a. Old English cearu, care: CARE; b. adjective *karagaz, sorrowful, in Old English cearig, sorrowful: CHARY. 2. Celtic suffixed form *gar-(s)mn in Gaelic gairm, shout, cry, call: SLOGAN. 3. Suffixed form (with expressive gemination) *garr-iyo- in Latin garrire, to chatter: GARRULOUS. [Pok. gar- 352.]
521:gher-'. To grasp, enclose; with derivatives meaning “enclosure.” 1. Suffixed zero-grade form *ghr-dh- in: a. Germanic *gurdjan in Old English gyrdan, to gird: GIRD; b. Old English gyrdel, girdle: GIRDLE; c. Old Norse gjordh, girdle, girth: GirTH. 2. Suffixed o-grade form *ghor-dho- (in Germanic) or *ghor-to-, an enclosure, in: a. Germanic *gardaz in (i) Old English geard, enclosure, garden, yard: YARD?; ORCHARD (ii) Old Norse gardhr, garden, yard: GARTH (iii) Old High German garto, gar- den: KINDERGARTEN (iv) Old North French gardin, gar- den: GARDEN (v) compound *midja-gardaz, “middle zone,” earth (see medhyo-); b. Latin hortus, garden: HORTICULTURE, ORCHARD, ORTOLAN. 3. Prefixed and suffixed zero-grade form *ko(m)-ghr-ti- (*ko(m)-, collec- tive prefix, “together”; see kom) in Latin cohors (stem cohort-), enclosed yard, company of soldiers, multitude: COHORT, CORTEGE, COURT, COURTEOUS, COURTESAN, (COURTESY), COURTIER, (CURTILAGE), (CURTSY). 4. Per- haps suffixed o-grade form *ghor-o- in Greek khoros, dancing ground (? perhaps originally a special enclosure for dancing), dance, dramatic chorus: (CHOIR), (CHORAL), (CHORALE), CHORIC, (CHORISTER), CHORUS; CHORAGUS, TERPSICHORE. [Pok. 4. gher- 442, gherd- 444.]
522:gher-2. To call out. Extended root *ghréd-. Germanic *grotjan in Old English grétan, to speak to, greet: GREET. [Pok. 1. gher- 439.]
524:gher-’. To shine, glow; gray. Hypothetical base of various Germanic forms. 1. Germanic *gréwaz, gray, in: a. Old English greg, gray: GRAY; b. probably Old English grighund, greyhound: GREYHOUND. 2. Germanic *gris- Jaz, gray, in: a. Old French gris (> French gris), gray: GRISAILLE, (GRISETTE), (GRISON), GRIZZLE; AMBERGRIS; b. Medieval Latin griseus, gray, grayish: GRISEOUS. [Pok. 3. gher- 441.] gher-4. To scrape, scratch. 1. Extended zero-grade form *ghr(e)-k- in: a. Greek kharax, a pointed stake, also a kind of sea bream: CHARACIN; b. Greek kharassein, to sharpen, notch, carve, cut: CHARACTER, GASH. 2. Ex- tended form *ghers-.in suffixed zero-grade form *ghrs-to- perhaps (but unlikely) in Sanskrit ghattah, ghat: GHAT. See also extensions ghréi- and ghréu-. [Pok. 2. gher- 439.] gher-5. To like, want. 1. Suffixed form *gher-n- in Ger- manic “*gernjan in Old English giernan, gyrnan, to strive, desire, yearn: YEARN. 2. Extended form *ghré- possibly in: a. Germanic *gréduz, hunger, forming *grédagaz, hungry, in Old English grédig, hungry, covetous, greedy: GREEDY; b. Greek khré, it is necessary, whence krésthai, to lack, want, use: CATACHRESIS, CHRESARD, CHRESTOM- ATHY. 3. Suffixed zero-grade form *ghr-td- in Latin hortari, to urge on, encourage (< “to cause to strive or desire”): HORTATIVE; EXHORT. 4. Suffixed zero-grade form “ghr-i- in Greek kharis, grace, favor: CHARISMA; Eucnarist. [Pok. 1. gher- 440.] ghere-. Gut, entrail. 1. Suffixed form *ghero-no- in Ger- manic *garn6, string, in Old English gearn, yarn: YARN. 2. Suffixed form *ghero-n- in Latin hernia, “protruded viscus,” rupture, hernia: HERNIA. 3. Suffixed o-grade form *ghoro-d- in Greek khordé, gut, string: (CHORD?), CORD, (CORDON); HARPSICHORD, TETRACHORD. 4. O-grade form *ghors- in Greek khorion, intestinal membrane, afterbirth: CHORION. 5. Possible suffixed zero-grade form *ghr-u- in Latin haruspex (-spex, “he who sees” < *spek-, “to see”; see spek-), “he who inspects entrails,” diviner (but perhaps borrowed from Etruscan): HARUSPEX. [Pok. 5. gher- 443.] ghers-. To bristle. 1. Extended zero-grade form *ghrzd-, prickly plant, in: a. Germanic *gorst- in Old English gorst, furze, gorse: GORSE; b. Latin hordeum, barley: ORGEAT. 2. Lengthened-grade form *ghér(s)- in Latin hér, ér, hedgehog: URCHIN. 3. Suffixed lengthened-grade form *ghér(s)-ika in Latin ériica, caterpillar: ROCKET?. 4. Suffixed full-grade form *gher-tu-, remade to *hirsu- in Latin hirsitus, bristly, shaggy, hairy: HIRSUTE. 5. Suf- fixed full-grade form *ghers-ko- in Latin hispidus (prob- ably a dialectal borrowing), bristly, shaggy, prickly: HISPID. 6. Suffixed o-grade form “ghors-eyo- in Latin horrére, to bristle, shudder, be terrified, look frightful: HORROR; ABHOR, ORDURE. 7. Suffixed full-grade form *ghers-o- in Greek khersos, dry land: CHERSONESE. [Pok. Bhers- 445.] gheslo-. Seen by some as a base for words meaning “thousand.” 1, Suffixed form *ghesl-yo- in Greek khilioi, thousand: CHILIAD, KILO-. 2. Latin mille, thousand, which has been analyzed as *smi-, “one” + a form *ghsli-, is of obscure origin: MIL!, MIL2, MILE, MILLE- NARY, MILLESIMAL, MILLI-, MILLIEME, MILLION; MIL- FOIL, MILLENNIUM, MILLEPORE, MILLIARY, MILLIPEDE. [Pok. ghéslo- 446.] ghesor-. Hand. Reduced form “ghesr- in Greek kheir, hand: CHIRO-; (CHIRURGEON), ENCHIRIDION, (SURGEON), SURGERY. [Pok. 1. 8hesor- 447.] gheu-. To pour, pour a libation. I. Extended form *gheud-. 1. Zero-grade form *ghud- in Germanic *gut- in Old English guttas, intestines: GuT. 2. Nasalized zero-grade form *ghu-n-d- in Latin fundere, to pour: FOISON, FONDANT, FONDUE, FONT, FOUND2, FUNNEL, FUSE?, FUSILE, FUSION; AFFUSION, CIRCUMFUSE, CON- FOUND, CONFUSE, DIFFUSE, EFFUSE, INFUSE, PERFUSE, PROFUSE, REFUND!, (REFUSE!), (REFUSE?), SUFFUSE,
610:ker-?
618:ker-1. Horn, head; with derivatives referring to horned animals, horn-shaped objects, and projecting parts. I. Zero-grade form *kr-. 1. Suffixed form *kr-n- in: a. Ger- manic *Aurnaz in (i) Old English horn, horn: HORN, (HORNBEAM) (ii) German Horn, horn: ALPENHORN, ALT- HORN, FLUGELHORN, HORNBLENDE; Db. Latin cornd, horn: CORN2, CORNEA, CORNEOUS, CORNER, CORNET, CORNICULATE, CORNU; BICORN, CADUCICORN, CAPRI- CORN, CLAVICORN, CORNIFICATION, LAMELLICORN, LON- GICORN, TRICORN, UNICORN. 2. Suffixed and extended form *krs-n- in Germanic *hurznuta in Old English hyrnet, hornet: HORNET. 3. Suffixed form *kr-ei- in: a. Germanic *hraina- in Old Norse hreinn, reindeer: REINDEER; b. Germanic *hrinda- in Old High German hrind, ox (> German Rinder, cattle): RINDERPEST. 4. Suffixed extended form *kros-no- in Greek kranion, skull, upper part of the head: CRANIUM; MIGRAINE, OLECRANON. 5. Suffixed form *kr-a- in: a. Greek karé, kara, head: CHARIVARI; CHEER; b. Greek karoun, to stupefy, be stupefied (< “to feel heavy-headed”): ca- ROTID; c. Greek kardton, carrot (from its hornlike shape): CARROT. 6. Possibly extended form *kri- in Greek krios, ram: CRIOSPHINX. II. Suffixed form *ker-wo-. 1. Latin cervus, deer: CERVINE, SERVAL. 2. Latin cervix, neck: CERVIX. III. Extended and suffixed form *keru-do- in Germanic *herutaz in: a. Old English heorot, hart, stag: HART; b. Dutch hart, deer, hart: HARTEBEEST. IV. Extended form *keras-. 1. Greek keras, horn: CARAT, CERASTES, KERATO-; CERATODUS, (CERATOID), CHELIC- ERA, CLADOCERAN, KERATIN, RHINOCEROS, TRICERA- Tops. 2. Persian sar, head: SIRDAR. 3. Suffixed form *keras-ro- in Latin cerebrum, brain: CEREBELLUM, CERE- BRUM, SAVELOY. V. Extended o-grade form *koru-. 1. Greek Rorumbos, uppermost point (< “head”): CoR- yMB. 2. Greek koruphé, head: CORYPHAEUS. 3. Suffixed form *koru-do- in Greek korudos, crested lark: coRY- DALIS. 4. Suffixed form *koru-ndé in Greek koruné, club, mace: CORYNEBACTERIUM. [Pok. 1. ker- 574.]
619:ker-2, Echoic root, base of various derivatives indicating loud noises or birds. I. Zero-grade form *kr-, becoming Germanic *hr-. 1. Germanic *hring- in Old English hringan, to resound, clink: RING. 2. Germanic *hraik- in Old English hré&can, to clear the throat: RETCH. 3. Ger- manic *hrdkaz, “croaking bird,” crow, in Old English
620:ker-*
```


## [2026-09-05T14:55:53.798Z] TOOL CALL #39: Bash

```json
{
 "command": "curl -s \"https://ia800508.us.archive.org/fulltext/inside.php?item_id=originsofenglish00jose&doc=originsofenglish00jose&path=/0/items/originsofenglish00jose&q=charlatan\" | head -c 3000",
 "description": "IA in-book search Shipley OEW"
}
```


### [2026-09-05T14:55:55.683Z] TOOL RESULT

```
<!DOCTYPE html>
<html lang="en">
<!-- __ _ _ _ __| |_ (_)__ _____
    / _` | '_/ _| ' \| |\ V / -_)
    \__,_|_| \__|_||_|_| \_/\___| -->
  <head>
    <title>Item not available</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <link href="/about/css/ia.css?v=1" rel="stylesheet" type="text/css"/>
    <link rel="SHORTCUT ICON" href="https://archive.org/images/glogo.jpg"/>
  </head>
  <body class="navia">
    <a href="#maincontent" class="hidden-for-screen-readers">Skip to main content</a>

    <!-- Wraps all page content -->
    <div id="wrap">
      <div id="navwrap1">
        <div id="navwrap2">
          <div class="navbar navbar-inverse navbar-static-top1" role="navigation">
            <ul class="nav navbar-nav navbar-main">
              <li class="pull-left">
                <a title="Home" class="navia-link home" href="https://archive.org/" target="_top">
                  <span class="iconochive-logo"></span>
                  <span><img src="https://archive.org/images/wordmark-stacked.svg" alt="IA wordmark-stacked-logo" height="30px" style="margin-left: 10px;"/></span>
                </a>
              </li>
              <li class="dropdown dropdown-ia pull-left">
                <a title="Web" class="navia-link web"  href="https://web.archive.org" target="_top"><span class="iconochive-web" aria-hidden="true"></span><span>Web</span></a>
              </li>
              <li class="dropdown dropdown-ia pull-left">
                <a title="Books" class="navia-link books"  href="https://archive.org/details/books" target="_top"><span class="iconochive-books" aria-hidden="true"></span><span>Books</span></a>
              </li>
              <li class="dropdown dropdown-ia pull-left">
                <a title="Video" class="navia-link movies"  href="https://archive.org/details/movies" target="_top"><span class="iconochive-movies" aria-hidden="true"></span><span>Video</span></a>
              </li>
              <li class="dropdown dropdown-ia pull-left">
                <a title="Audio" class="navia-link audio"  href="https://archive.org/details/audio" target="_top"><span class="iconochive-audio" aria-hidden="true"></span><span>Audio</span></a>
              </li>
              <li class="dropdown dropdown-ia pull-left">
                <a title="Software" class="navia-link software"  href="https://archive.org/details/software" target="_top"><span class="iconochive-software" aria-hidden="true"></span><span>Software</span></a>
              </li>
              <li class="dropdown dropdown-ia pull-left rightmost">
                <a title="Images" class="navia-link images"  href="https://archive.org/details/image" target="_top"><span class="iconochive-images" aria-hidden="true"></span><span>Images</span></a>
              </li>
              <li class="dropdown dropdown-ia pull-right leftmost">
                <a class="nav-upload" href="https://archive.org/create" _target="top" data-event-click-tracking="
```


## [2026-09-05T14:56:02.027Z] TOOL CALL #40: Bash

```json
{
 "command": "for id in originsofenglish00jose dictionaryofword0000jose_n4 originsshortetym00part; do echo \"=== $id ===\"; curl -s -m 25 \"https://ia-fts.archive.org/api/v1/search/hits?q=charlatan&identifier=$id\" | head -c 400; echo; done",
 "description": "Try IA FTS API"
}
```


### [2026-09-05T14:56:04.002Z] TOOL RESULT

```
=== originsofenglish00jose ===

=== dictionaryofword0000jose_n4 ===

=== originsshortetym00part ===
```


## [2026-09-05T14:56:09.178Z] TOOL CALL #41: Bash

```json
{
 "command": "curl -s -m 25 \"https://api.archivelab.org/books/originsofenglish00jose/searchinside?q=charlatan\" | head -c 600; echo; echo \"=== hathi SHP ===\"; curl -s -m 25 \"https://babel.hathitrust.org/cgi/pt/search?q1=tea%3B&id=uc1.32106001576476\" -o /dev/null -w \"%{http_code}\\n\"",
 "description": "Alternative IA search inside"
}
```


### [2026-09-05T14:56:35.872Z] TOOL RESULT

```
=== hathi SHP ===
403
```


## [2026-09-05T14:56:41.315Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=charlatan",
 "prompt": "Give the full etymology line of the entry \"charlatan\" exactly as printed (French, Italian ciarlatano, cerretano, Cerreto, ciarlare)."
}
```


## [2026-09-05T14:56:41.830Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=charade",
 "prompt": "Give the full etymology line of the entry \"charade\" exactly as printed (French, Provençal charrado, charrar, imitative)."
}
```


### [2026-09-05T14:56:45.273Z] TOOL RESULT

```
# Etymology of "Charlatan"

According to the dictionary entry, the etymology is:

"[French, from Italian _ciarlatano_, probably alteration (influenced by _ciarlare_, to prattle) of _cerretano_, inhabitant of _Cerreto_, a city of Italy once famous for its quacks.]"

This traces the word's origins from French back through Italian, where it likely developed from a word meaning an inhabitant of Cerreto, a town in Italy known historically for con artists and fraudsters.
```


### [2026-09-05T14:56:46.713Z] TOOL RESULT

```
# Etymology of "Charade"

Based on the dictionary entry provided, the full etymology line is:

"[French, probably from Provençal _charrado_, chat, from _charra_, to chat, chatter, perhaps from Italian _ciarlare_.]"

This traces the word's origins through multiple Romance languages, beginning with French and extending back through Provençal and possibly Italian sources.
```


## [2026-09-05T14:56:53.950Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CF%87%CE%AC%CF%81%CF%84%CE%B7%CF%82",
 "prompt": "Ancient Greek χάρτης: etymology (Egyptian origin? unknown?), meaning, and descendants (Latin charta, Arabic, Aramaic, Armenian, etc.). Quote."
}
```


## [2026-09-05T14:56:54.686Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=tea",
 "prompt": "Give the full etymology line of the entry \"tea\" exactly as printed (Dutch thee, Malay teh, Chinese Amoy te / cha)."
}
```


### [2026-09-05T14:57:01.155Z] TOOL RESULT

```
# Etymology of "Tea"

According to the American Heritage Dictionary entry, the etymology line states:

"[Probably Dutch _thee_, from Malay _teh_, from Amoy _te_ (equivalent to Mandarin _chá_), from dialectal Early Middle Chinese _da_; akin to Middle Chinese _drεː_ (source of Mandarin _chá_, tea); see CHANOYU.]"

The term traces back through Dutch and Malay origins to Chinese linguistic roots, with the Amoy form _te_ corresponding to Mandarin _chá_.
```


### [2026-09-05T14:57:02.001Z] TOOL RESULT

```
# χάρτης (Chártis) - Etymology and Descendants

## Ancient Greek Origins

The word χάρτης has **two competing etymological theories**:

1. **Proto-Indo-European derivation**: According to Strong's Biblical Concordance, it derives from χαράσσω (to scratch/inscribe), tracing back to PIE *ǵʰer- (to scratch). However, scholars Beekes and Chantraine reject this theory, treating the etymology as unknown.

2. **Phoenician origin**: Rendsburg proposes Phoenician ḥrṭyt ("that which has been written"), cognate with Biblical Hebrew ḥéreṭ (stylus).

## Meaning

In Ancient Greek, χάρτης denoted:
- "sheet of paper; paper"
- "book"

In Modern Greek, the meaning evolved to primarily mean "map" or "chart" (navigation context), and secondarily "charter" or "constitution."

## Major Descendants

The word spread extensively through multiple language families:

- **Romance**: Latin *charta* (leading to English "chart")
- **Semitic**: Aramaic and Arabic قُرْطَاس (qurṭās)
- **Slavic**: Bulgarian хартия, Russian хартия
- **Other**: Armenian, Hebrew, Romanian hartă

This demonstrates how an Ancient Greek term for papyrus became a widespread term for maps and documents across Eurasia.
```


## [2026-09-05T14:57:09.869Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt; do echo \"=== $f چای ===\"; grep -c \"چای\" $f 2>/dev/null; done; echo \"=== ARY کارت/چای ===\"; grep -n \"چای\\|کارت\\|قرطاس\" incoming/ARY/ARY_pages.txt | head -10",
 "description": "grep BQT and ARY"
}
```


### [2026-09-05T14:57:11.357Z] TOOL RESULT

```
=== BQT_v1_pages.txt چای ===
27
=== BQT_v2_pages.txt چای ===
22
=== incoming/BQT/BQT_v3_pages.txt چای ===
16
=== incoming/BQT/BQT_v4_pages.txt چای ===
7
=== ARY کارت/چای ===
26:هند و اروپایی آشکارتر گردد. ۱
723:هندیان؛ باستانی ترین نوشتارهای هند و اروپایی بوده و پل مهمی میان زیانهای ند ز ارچایین.. ]
```


## [2026-09-05T14:57:12.240Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%86%D8%A7%DB%8C/",
 "prompt": "Show the فرهنگ معین (Mo'in) entry for چای, including any bracketed origin tag such as [چین.] or [ چینی ], and the Dehkhoda entry's etymological note."
}
```


### [2026-09-05T14:57:19.201Z] TOOL RESULT

```
# چای - Farhang-e Mo'in Entry

## Mo'in Dictionary Definition

**Origin tag:** (اِ.) مأخوذ از چینی
[From Chinese]

**Entry:** "درختی است کوچک دارای برگ های سبز و دندانه دار. گل هایش سفید و معطر در جاهای معتدل و مرطوب می روید."

A small tree featuring serrated green leaves with fragrant white flowers that grows in temperate, humid regions.

---

## Dehkhoda Etymology Note

The Dehkhoda lexicon traces the word's origins through Persian linguistic history: "واژه ی چای از ریشه ی واژه ی چاییدن فارسی هست" 

The term derives from the Persian root meaning to taste or sample beverages. However, the Dehkhoda also documents the Chinese provenance, noting the plant is native to China and East Asia, brought westward via trade routes.

The entry emphasizes this dual etymological character—while phonetically and structurally connected to older Persian verbal roots, the modern referent (the beverage plant itself) arrived from Chinese sources.
```


## [2026-09-05T14:57:29.993Z] TOOL CALL #48: Bash

```json
{
 "command": "pdftoppm -f 104 -l 104 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg104 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 104"
}
```


## [2026-09-05T14:57:30.846Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"چای\" BQT_v2_pages.txt | head -8",
 "description": "BQT chay hits"
}
```


### [2026-09-05T14:57:36.568Z] TOOL RESULT

```
total 32472
drwx------ 2 sfmqrb sfmqrb     4096 Sep  5 10:57 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb    22149 Sep  5 01:51 c_belloth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9603 Sep  5 10:50 c_byz2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11328 Sep  5 10:49 c_byz_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3138 Sep  5 10:50 c_heb1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4953 Sep  5 10:50 c_heb2.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb    49033 Sep  5 10:53 mk100.py
-rw-rw-r-- 1 sfmqrb sfmqrb    17464 Sep  5 10:55 mk102b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    21655 Sep  5 10:53 mk102.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb     3057 Sep  5 10:05 patch87.py
-rw-rw-r-- 1 sfmqrb sfmqrb    71589 Sep  5 10:41 pg100.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68145 Sep  5 10:44 pg102.png
-rw-rw-r-- 1 sfmqrb sfmqrb   114170 Sep  5 10:49 pg103_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79623 Sep  5 10:49 pg103.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78826 Sep  5 10:57 pg104.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82500 Sep  5 10:57 pg105.png
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


### [2026-09-05T14:57:36.603Z] TOOL RESULT

```
149:        ‫مسلادی ( = سندیاد نامه)‪.‬‬    ‫‪6۹۱ ۸‬‬   ‫احمدا تش‪ .‬استانبول‪ .‬چایخانة وزارت فرهنك‬
382:                 ‫العالم و مسجم البلدان نامده ‪.‬‬   ‫در حدود‬     ‫‪- ۲‬‬          ‫‪ - ۱‬رك ‪ :‬چایلوی ‪.‬‬
714:                                                 ‫متجیاتمی فم ‪-‬ا رك ‪ :‬کچایمضرو‬
814:                                                          ‫ابران‪ .‬کدترشفق‪ .‬تهران‪ .‬چایشان‪#‬داش ‪۱۲۳۱‬‬
3693:          ‫‪ - ۴‬معرب چای «صای» و «شای» امت ‪ .‬رك ‪ :‬چای ‪.‬‬     ‫رك‪ :‬چای ‪.‬‬  ‫‪۱‬‬
3748:  ‫بکوهی در انداختن‪ .‬نظامیکنجوی‪.‬‬           ‫کمندی‬    ‫‪ - ۱‬ده چابك شد ابن چایکی تاختن‬
3767:                                                           ‫‪#‬ایلوس ‪ -‬رك ‪ :‬چایلوی ‪.‬‬
4120: ‫بروزن آبتوس » بمعنی چایلوی و فرب دهنده‬                    ‫و بکتیر‪#:‬قلداق خوانند ؛ وبعضی گویند چال‪.‬‬
```


## [2026-09-05T14:57:41.455Z] TOOL CALL #50: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg104.png"
}
```


### [2026-09-05T14:57:41.801Z] TOOL RESULT

```

```


## [2026-09-05T14:57:41.799Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T14:57:51.742Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 104 -l 104 -r 600 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg104_600 && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg104_600.png')\nprint(im.size)\n# scale from 200dpi coords x3\nim.crop((2600,2600,3600,2800)).save('pg104_charlatan.png')\n\"",
 "description": "Crop charlatan node"
}
```


### [2026-09-05T14:57:56.103Z] TOOL RESULT

```
(5100, 6600)
```


## [2026-09-05T14:57:58.275Z] TOOL CALL #52: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg104_charlatan.png"
}
```


### [2026-09-05T14:57:58.288Z] TOOL RESULT

```

```


## [2026-09-05T14:58:03.577Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg104_600.png')\nim.crop((2850,2820,3700,3060)).resize((1700,480)).save('pg104_charlatan.png')\n\"",
 "description": "Re-crop charlatan node"
}
```


### [2026-09-05T14:58:05.586Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T14:58:07.364Z] TOOL CALL #54: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg104_charlatan.png"
}
```


### [2026-09-05T14:58:07.384Z] TOOL RESULT

```

```


## [2026-09-05T14:58:17.114Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT TEA ===\"; grep -n \"Tea\\.\" SKT.txt | head -5; echo \"=== SKT charade/charlatan ===\"; grep -n \"Charade\\|Charlatan\" SKT.txt | head -5; echo \"=== HJB TEA ===\"; grep -n \"^TEA\\b\\|^TEA,\" HJB.txt | head -5; echo \"=== WEB charade ===\"; grep -n \"cha-rade\\|ehar-ade\\|char'ade\" WEB_vol1.txt | head -5",
 "description": "Skeat/HJB/Webster greps"
}
```


### [2026-09-05T14:58:17.215Z] TOOL RESULT

```
=== SKT TEA ===
19247:Tea.  iChUie&e.)  Spelt  tu  in  Pcpys' Cinry,  Sept.  28,  1660;  cka  in  Blount (1674).  Prom  the  Amoy  pronunciation (//)  of  the  Chinese  name  for  the  plant, which  is  ^m  other  parts  of  the  empire) called  cKa  or /s'a;  Williams,  Chin.  Diet. p.  5;  ]!)ouglas.  Chin.  Diet  of  the  Amoy vernacular,  p.  481.  Hence  Ital.  rid,  tea; F.  ft/,  G.  M«,  Malay  t^A,  tea.
=== SKT charade/charlatan ===
=== HJB TEA ===
21681:TEA.
21683:TEA.
21685:TEA,  s.  Crawfurd  alleges  that  we got  this  word  in  its  various  European forms  from  the  Malay  2>,  the  Chinese name  being  Chhd.  The  latter  is  in- deed the  pronunciation  attached,  when reading  in  the  'mandarin  dialect,'  to the  character  representing  the  tea- plant,  and  is  the  form  which  has  ac- companied the  knowledge  of  tea  to India,  Persia,  Portugal,  Greece  (rcrdt) and  Russia.  But  though  it  may  be probable  that  Te,  like  several  other names  of  articles  of  trade,  may  have come  to  us  through  the  Malay,  the word  is,  not  the  less,  originally Chinese,  TS  (or  Tay  as  Medhurst writes  it)  being  the  utterance  at- tached to  the  cnaracter  in  the  Fuh- kien  dialect.  The  original  pronuncia- tion, whether  direct  from  Fuh-kien  or through  the  Malay,  accompanied  the introouction  of  tea  to  England  as  well as  other  countries  of  Western  Europe. This  is  shown  by  several  couplets  in Pope,  e.g,
21699:TEA.
21713:TEA.
=== WEB charade ===
31165:cha-rade’, n. [Fr.] a game in which a chosen word or phrase to be guessed is acted out in pantomime, syllable by syllable or as a whole.
```


## [2026-09-05T14:58:26.674Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nfor f,n in [('HJB.txt','TEA,  s.  Crawfurd'),('SKT.txt','Tea.  iChUie&e.)'),('FSD_vol1.txt','It.  ciarlatano'),('LKT.txt',\"415.  Chiu.  cha:\"),('KLN_1966.txt','tea,  n.  —  F.  the')]:\n    d=open(f,encoding='utf-8',errors='replace').read().split('\\f')\n    for i,p in enumerate(d):\n        if n in p:\n            print(f,'leaf',i); break\nEOF",
 "description": "Leaf numbers for consulted books"
}
```


### [2026-09-05T14:58:28.501Z] TOOL RESULT

```
HJB.txt leaf 948
SKT.txt leaf 520
FSD_vol1.txt leaf 507
LKT.txt leaf 60
KLN_1966.txt leaf 836
```


## [2026-09-05T14:58:35.756Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%82%D8%B1%D8%B7%D8%A7%D8%B3/",
 "prompt": "Show the فرهنگ معین (Mo'in) entry for قرطاس with its bracketed origin tag (e.g. [ع.] or [معرب]) and the Dehkhoda note on its origin (Greek χάρτης?)."
}
```


## [2026-09-05T14:58:37.249Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%A9%D8%A7%D8%B1%D8%AA/",
 "prompt": "Show the فرهنگ معین (Mo'in) entry for کارت with its bracketed origin tag (e.g. [فر.] French) and meaning; also any entry for کارتون."
}
```


### [2026-09-05T14:58:44.961Z] TOOL RESULT

```
# کارت Entry from Farhang-e Mo'in

**Origin tag:** [فر.] (French)

**Entry:** According to Farhang-e Mo'in, کارت refers to "thin cardboard on which characteristics of something or someone are written." The dictionary specifically notes variations including:
- **کارت ویزیت** (business card): thin cardboard with name, surname, profession, address and phone number
- **کارت شناسایی** (identification card): official document proving personal identity
- **کارت ملی** (national card): a sheet with specific numbers containing personal details

---

**Note on کارتون:** The provided dictionary content does not include a separate entry for کارتون. Only کارت is defined in the excerpts shown.
```


### [2026-09-05T14:58:45.254Z] TOOL RESULT

```
# فرهنگ معین Entry for قرطاس

**فرهنگ معین definition:**
"(قِ ) [ ع . ] (اِ. ) کاغذ. ج . قراطیس ."

The bracketed tag "[ع.]" indicates the word's Arabic origin.

**Regarding Greek etymology:**

The Dehkhoda section notes that قرطاس derives from Syriac-Aramaic ḳarṭīsā, which itself comes from ancient Greek χάρτης (chártēs), meaning "papyrus." The document states: "قرطاس خوانش عربی واژه سریانی و آرامی...به معنای پاپیروس می باشد که آن نیز برگرفته از واژه یونانی باستان" (papyrus—itself borrowed from ancient Greek).

Additionally, the comprehensive historical section explains that قرطاس is "اصلاً یونانی است مشتق از کارتس یعنی چیزی که بر آن می نویسند" (originally Greek, derived from kartis, meaning something written upon).
```


## [2026-09-05T14:58:52.500Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/card",
 "prompt": "Etymology of card (n.1, playing card / pasteboard): French carte, Latin charta, Greek khartes, Egyptian origin? Quote."
}
```


## [2026-09-05T14:58:54.585Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%D8%A7%D8%B1%D9%84%D8%A7%D8%AA%D8%A7%D9%86",
 "prompt": "Persian شارلاتان: etymology (French charlatan?), transliteration and meaning. If no Persian entry exists, say so and list what languages are present."
}
```


### [2026-09-05T14:58:56.484Z] TOOL RESULT

```
socket hang up
```


### [2026-09-05T14:58:57.878Z] TOOL RESULT

```
# Etymology of "Card" (Playing Card)

The word "card" in its playing card sense originated in the early 15c. from Old French *carte*, which derived from Medieval Latin *carta*/*charta* meaning "paper" or "a card."

The Latin term *charta* came from Greek *khartēs*, referring to "layer of papyrus," which scholars believe has "probably" Egyptian origins, though the exact connection remains uncertain.

**Key linguistic path:** Egyptian → Greek *khartēs* → Latin *charta* → Old French *carte* → English *card*

The shift from the Latin *-t* ending to English *-d* remains unexplained by etymologists. Interestingly, the playing card sense was the oldest meaning in French as well, and English extended the term by the 1590s to other small, flat pieces of paper, later including visiting cards (1795) and greeting cards (1862).
```


## [2026-09-05T14:59:02.569Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B4%D8%A7%D8%B1%D9%84%D8%A7%D8%AA%D8%A7%D9%86/",
 "prompt": "Show the فرهنگ معین (Mo'in) and Dehkhoda entries for شارلاتان — origin tag (e.g. [فر.] French) and meaning."
}
```


### [2026-09-05T14:59:07.599Z] TOOL RESULT

```
# شارلاتان - Dictionary Entries

## Dehkhoda (لغت نامه دهخدا)
**Origin:** French [فرانسوی]

**Definition:** "کسی که با زبان خوش مردم را فریب دهد" (Someone who deceives people through eloquent speech). Also listed as: fraud artist, charlatan, deceiver, trickster.

---

## Mo'in (فرهنگ معین)
**Origin:** French [فر.]

**Definition:** "حقه باز، شیاد، کلاهبردار" (Fraud artist, trickster, con artist) — describing someone who employs deception and smooth talk to dupe others.
```


## [2026-09-05T14:59:18.026Z] TOOL CALL #62: Bash

```json
{
 "command": "for u in \\\n \"https://www.etymonline.com/word/tea|page 104 entry0, root Č'a: tea via Dutch/Malay/Amoy\" \\\n \"https://en.wiktionary.org/wiki/چای|page 104 entry0 node1, Persian čāy from Chinese cháyè\" \\\n \"https://www.ahdictionary.com/word/search.html?q=tea|page 104 entry0 node5, AHD:1320 tea etymology\" \\\n \"https://abadis.ir/fatofa/چای/|page 104 entry0 node1, Mo'in MON:1270 چای مأخوذ از چینی\" \\\n \"https://www.etymonline.com/word/charlatan|page 104 entry2, charlatan Italian ciarlatano/cerretano\" \\\n \"https://www.etymonline.com/word/charade|page 104 entry2 node6, charade Provençal charrado\" \\\n \"https://www.ahdictionary.com/word/search.html?q=charlatan|page 104 entry2 nodes1-4, AHD:227 Cerreto etymology\" \\\n \"https://www.ahdictionary.com/word/search.html?q=charade|page 104 entry2 nodes5-6, AHD:228 charrado/charra\" \\\n \"https://abadis.ir/fatofa/شارلاتان/|page 104 entry2 node3, Persian شارلاتان [فر.] from French\" \\\n \"https://en.wiktionary.org/wiki/χάρτης|page 104 entry3 root, Greek khartēs etymology and descendants\" \\\n \"https://en.wiktionary.org/wiki/قرطاس|page 104 entry3 node1, Arabic qirṭās via Aramaic qarṭīsā\" \\\n \"https://abadis.ir/fatofa/قرطاس/|page 104 entry3 node2, Mo'in MON:2659 قرطاس [ع.]\" \\\n \"https://abadis.ir/fatofa/کارت/|page 104 entry3 node5, Mo'in MON:2801 کارت [فر.]\" \\\n \"https://www.etymonline.com/word/card|page 104 entry3 nodes3-6, card < carte < charta < khartēs\" \\\n ; do url=\"${u%%|*}\"; note=\"${u##*|}\"; python3 tools/fetch_source.py \"$url\" --note \"$note\" 2>&1 | tail -2; done",
 "description": "Archive web sources"
}
```


### [2026-09-05T14:59:28.577Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/3c11181a82ef3402.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3e3fd35e43a90ab9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0196beb4dc1c9663.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7efaa04e2795840b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8e1c2161917dfde3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0c978bd692ca7c3a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b7b6dcfeeb60c707.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5898a799605a8fd0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/776c7aeca51ce7ed.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e496522053109543.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2d97d00b1427b6df.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/08fa9ee0724f4c39.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a1669cb38c5c151c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/863c90e3bca179e8.txt
```


## [2026-09-05T14:59:39.744Z] TOOL CALL #63: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg104.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/104.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -3",
 "description": "Save page PNG for audit"
}
```


### [2026-09-05T14:59:39.808Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r-- 1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r-- 1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-05T14:59:41.335Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW charta ===\"; grep -n \"charta\" LEW_1910.txt | head -5; echo \"=== LAT charta ===\"; grep -n \"charta\" LAT.txt | head -5; echo \"=== FSD charade ===\"; grep -n \"cha-rade\\|Provencal  char\\|charrado\" FSD_vol1.txt | head -5",
 "description": "Latin etym dicts for charta"
}
```


### [2026-09-05T14:59:41.434Z] TOOL RESULT

```
=== LEW charta ===
=== LAT charta ===
5308:changement de genre et' de d 4 clinaison, cf. coclea, charta, ballista,
11597:littera terminari, uelut... x^P^^C charta. - Panroman. M.L.1866. Iri.
11599:Derives: chartaceus; chartarius, - a,-un et chartdrius, -1 m. = xopvo-
12725:de genre, cf. catapulta, charta. Attest 4 depuis Caton. Roman, avec
12771:de codices membranei uel chartacei, Dig. 33,53 pr. (comme nous parlons
=== FSD charade ===
62926:cha-rade  ,   1   ^ho-red  or -rad  ,2  tha-rad  or  -rad',  n.  An  i/,«i7l3),  a   French  Oriental  traveler  and,  later,
```


## [2026-09-05T14:59:45.503Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11590,11605p' LAT.txt",
 "description": "Ernout-Meillet charta entry"
}
```


### [2026-09-05T14:59:45.548Z] TOOL RESULT

```
c(h)arta, -ae f.: feuille de papier; et par suite "feuille ecrite,
lettre, livre, registres publics, documenta ecrits", etc. Emprunt ancien
et latinis 4 du gr. xoi-pTqG (—XDtC)i devenu f 4 minin, sous 1'influence des
autres thbmes en -o feminins; cf. coc(h)lea, etc. Le cartus de Lucilius
709 est une tentative isolee faite pour conserver le genre du nom
grec. Cf. Charisius, GLK I 104, Varro ait uocabula ex Graeco sumpta,
si suum genus non retineant, ex masculino in femineum trans ire, et "a"
littera terminari, uelut... x^P^^C charta. - Panroman. M.L.1866. Iri.
cairt.
Derives: chartaceus; chartarius, - a,-un et chartdrius, -1 m. = xopvo-
tooXt}C "marchand de papier", et "arcbiviste"; chartula: i° petit papier;
3 ° pifece officielle, acte public; chartularius, -a, -un d'ou chartula¬
rius, m., - ium n .
chelidonius, -a, -um: adj . transerit du gr.xeXo66vt.OG: au f 4 mi-
nin -a designe une pierre pr 4 cieuse, ou une piante, la ch 41 idoine
(lat .hirundinina; au n. -um, un collyre. M.L.1870.
```


## [2026-09-05T15:00:43.742Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg104_600.png')\nim.crop((1100,1380,2100,2100)).resize((1500,1080)).save('pg104_tea.png')\n\"",
 "description": "Crop tea chart boxes"
}
```


### [2026-09-05T15:00:45.925Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T15:00:47.927Z] TOOL CALL #67: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg104_tea.png"
}
```


### [2026-09-05T15:00:47.966Z] TOOL RESULT

```

```


## [2026-09-05T15:01:01.387Z] AGENT

Now I'll write the verification file.


## [2026-09-05T17:21:27.172Z] AGENT

I have all the research I need. Writing the verification file now.


## [2026-09-05T17:30:04.038Z] TOOL CALL #68: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk104.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = {\n \"ety_tea\":\"https://www.etymonline.com/word/tea\",\n \"wik_chay\":\"https://en.wiktionary.org/wiki/چای\",\n \"ahd_tea\":\"https://www.ahdictionary.com/word/search.html?q=tea\",\n \"ab_chay\":\"https://abadis.ir/fatofa/چای/\",\n \"ety_charlatan\":\"https://www.etymonline.com/word/charlatan\",\n \"ety_charade\":\"https://www.etymonline.com/word/charade\",\n \"ahd_charlatan\":\"https://www.ahdictionary.com/word/search.html?q=charlatan\",\n \"ahd_charade\":\"https://www.ahdictionary.com/word/search.html?q=charade\",\n \"ab_sharlatan\":\"https://abadis.ir/fatofa/شارلاتان/\",\n \"wik_khartes\":\"https://en.wiktionary.org/wiki/χάρτης\",\n \"wik_qirtas\":\"https://en.wiktionary.org/wiki/قرطاس\",\n \"ab_qertas\":\"https://abadis.ir/fatofa/قرطاس/\",\n \"ab_kart\":\"https://abadis.ir/fatofa/کارت/\",\n \"ety_card\":\"https://www.etymonline.com/word/card\",\n}\n\nKLN_TEA = (\"KLN_1966.txt leaf 836 (the leaf carries the printed page numbers 1578/1579), s.v. tea: \"\n \"\\\"tea, n. — F. the (the orig. pronunciation of E. tea was ta), fr. Malay, teh, fr. dial. S. Chin. te, \"\n \"which corresponds to Chin. chai [= ch'a]. Cp. Thea, theine.\\\"\")\n\nentry0 = {\n \"entry\": 0,\n \"root\": \"Č'a\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"Chinese 茶 chá 'tea' (Wade-Giles ch'a; Middle Chinese *ɖˠa, Old Chinese *rlaː), the ultimate source of every 'tea' word in Eurasia\",\n \"note\": (\"The root box is right: the world's tea vocabulary goes back to one Chinese etymon, 茶, whose \"\n  \"Mandarin/standard reading is chá (Wade-Giles ch'a, Nourai's 'Č'a'). Nourai's two-branch chart reproduces \"\n  \"exactly the split all handbooks make: (a) the chá branch, carried overland along the caravan routes into \"\n  \"Persian čāy, Turkish çay, Russian чай, Hindi cāy, Arabic šāy; (b) the Southern-Min (Amoy/Hokkien) branch \"\n  \"tê, carried by sea by the Dutch East India Company from 1610 and giving Malay teh, Dutch thee, French thé, \"\n  \"German Tee, Italian tè, English tea. Hobson-Jobson makes the same division explicitly. The only defect on \"\n  \"the page is the printed form of the southern word, 't'a' for t'e (see node #2). The gloss 'tea' and the \"\n  \"language label 'Chinese' are correct; strictly the label for the root is Mandarin/standard Chinese and for \"\n  \"node #2 Southern Min, but the book has no finer labels.\"),\n \"note_fa\": (\"جعبهٔ ریشه درست است: همهٔ واژه‌های «چای» در اوراسیا به یک واژهٔ چینی، 茶، بازمی‌گردد که خوانش \"\n  \"معیار (ماندارین) آن chá است — همان «Č'a»ی نورایی. نمودار نورایی دقیقاً همان دوشاخگیِ شناخته‌شده را \"\n  \"نشان می‌دهد: شاخهٔ chá که از راه خشکی و جادهٔ ابریشم به فارسی «چای»، ترکی çay، روسی чай، هندی cāy و \"\n  \"عربی «شای» رسید؛ و شاخهٔ جنوبیِ مین (لهجهٔ اَموی) tê که از سدهٔ ۱۷ م. با کشتی‌های کمپانی هند شرقیِ \"\n  \"هلند به مالایی teh، هلندی thee، فرانسوی thé، آلمانی Tee و انگلیسی tea انجامید. تنها ایراد صفحه، صورت \"\n  \"چاپیِ واژهٔ جنوبی است که «t'a» آمده به‌جای t'e (نگاه کنید به گرهٔ ۲). برچسب زبانی و معنای «چای» درست است.\"),\n \"sources\": [W[\"ety_tea\"], W[\"ahd_tea\"]],\n \"ref_check\": [\n   {\"ref\":\"KLN:1578\",\"status\":\"supports\",\"note\": KLN_TEA + \" Klein's page 1578 is exactly the page Nourai cites, and it gives both the Chinese ch'a and the S. Chinese te, i.e. Nourai's two branches. (Klein routes English tea through French thé rather than Dutch — see node #5.)\"},\n   {\"ref\":\"SHP:126\",\"status\":\"not_checked\",\"note\":\"Shipley, Dictionary of Word Origins (1945) — archive.org copies are lending-only and the HathiTrust full-view copy (uc1.32106001576476) returns HTTP 403 to non-browser clients; the IA in-book search endpoint (fulltext/inside.php) answers 'Item not available'. No local OCR.\"}\n ],\n \"consulted\": [\n   {\"src\":\"LKT\",\"where\":\"entry no. 415 (LKT.txt leaf 60 ≈ printed p. 34)\",\"stance\":\"supports\",\"note\":\"\\\"415. Chin. cha: 'Tee'; cha-ye 'Teeblätter' [so ist die Aussprache im Kuan-hoa … und im Kantondialekt]; hieraus pg. chá, sp. (selten) cha, russ. čaj, bulg. čaj, serb. čaj … — Im Dialekt von Amoy, von wo aus vermutlich die ersten Teeladungen ausgegangen sind, wird etwa te gesprochen, daher frz. thé, sp. té, it. tè, ndl. thee, dtsch. Tee, engl. tea …\\\" Lokotsch's two-branch account is Nourai's chart.\"},\n   {\"src\":\"HJB\",\"where\":\"HJB.txt leaf 948, s.v. TEA (printed p. ~900)\",\"stance\":\"supports\",\"note\":\"\\\"TEA, s. Crawfurd alleges that we got this word in its various European forms from the Malay Te, the Chinese name being Chhá. The latter is indeed the pronunciation attached, when reading in the 'mandarin dialect', to the character representing the tea-plant, and is the form which has accompanied the knowledge of tea to India, Persia, Portugal, Greece (τσάι) and Russia … Te (or Tay as Medhurst writes it) being the utterance attached to the character in the Fuh-kien dialect.\\\"\"},\n   {\"src\":\"SKT\",\"where\":\"SKT.txt leaf 520 (printed p. ~500), s.v. Tea\",\"stance\":\"partial\",\"note\":\"\\\"Tea. (Chinese.) Spelt tay in Pepys' Diary, Sept. 28, 1660; cha in Blount (1674). From the Amoy pronunciation (të) of the Chinese name for the plant, which is (in other parts of the empire) called ch'a or ts'a … Hence Ital. tè, tea; F. thé, G. Thee, Malay teh, tea.\\\" Same two Chinese forms, but Skeat makes Malay teh a borrowing FROM the European forms, the reverse of Nourai's (and AHD's) direction.\"},\n   {\"src\":\"AHD\",\"where\":\"online AHD s.v. tea (= the dictionary Nourai cites as AHD:1320)\",\"stance\":\"supports\",\"note\":\"\\\"[Probably Dutch thee, from Malay teh, from Amoy te (equivalent to Mandarin chá), from dialectal Early Middle Chinese da; akin to Middle Chinese drεː (source of Mandarin chá, tea).]\\\" — Nourai's chain node for node, including the Malay step.\"}\n ],\n \"nodes\": []\n}\n\nentry0[\"nodes\"].append({\n \"id\":1, \"lang\":\"Persian\", \"words\":\"čây\", \"verdict\":\"confirmed\",\n \"derivation\":(\"Persian چای čāy 'tea' is a loan from the northern/standard Chinese reading chá, not from the \"\n  \"southern tê that gave English tea. Tea reached Iran overland from China (Safavid period, 17th c.; it became \"\n  \"the everyday drink only in the 19th c., largely through Russian trade), so Persian belongs to the 'chai' \"\n  \"isogloss together with Turkish çay, Russian чай, Hindi cāy and Arabic شاي šāy. The final -y of čāy — absent \"\n  \"in Chinese chá — is explained two ways: (a) from the Chinese compound 茶葉 cháyè 'tea leaves', the form \"\n  \"Lokotsch cites and Wiktionary gives as the likelier source; (b) as a Persian/Turkic suffixation of čā. \"\n  \"Mo'in simply tags it مأخوذ از چینی 'taken from Chinese'. Borhan-e Qate' (Mo'in's footnote in vol. 2) notes \"\n  \"that the Arabicised forms of چای are «صای» and «شای». The internet claim that čāy comes from the Persian \"\n  \"verb چاییدن is folk etymology and has no standing.\"),\n \"derivation_fa\":(\"«چای» وام‌واژه‌ای است از چینیِ معیار chá و نه از صورت جنوبیِ tê که انگلیسی tea از آن آمده \"\n  \"است؛ چای از راه خشکی و از چین به ایران رسید (عصر صفوی، سدهٔ ۱۱ ق./۱۷ م.) و از سدهٔ ۱۳ ق./۱۹ م. با بازرگانی \"\n  \"روسیه نوشیدنیِ همگانی شد، از این‌رو فارسی در همان دستهٔ «چای» جای می‌گیرد که ترکی çay، روسی чай، هندی cāy \"\n  \"و عربی «شای» در آن‌اند. «ی» پایانی که در chá چینی نیست، یا از ترکیبِ چینی 茶葉 (cháyè) «برگ چای» بازمانده \"\n  \"است — تبیینی که لوکوچ و ویکی‌واژه می‌پسندند — یا پسوندی است ایرانی/ترکی بر چا. معین در فرهنگ فارسی تنها \"\n  \"می‌نویسد «مأخوذ از چینی»، و معین در حاشیهٔ برهان قاطع یادآور می‌شود که معرّبِ چای «صای» و «شای» است. این \"\n  \"ادعای رایج که «چای» از مصدر «چاییدن» آمده ریشه‌شناسی عامیانه است و پایه‌ای ندارد. ادعای نورایی درست است.\"),\n \"sources\":[W[\"wik_chay\"], W[\"ab_chay\"], W[\"ety_tea\"]],\n \"ref_check\":[\n   {\"ref\":\"MON:1270\",\"status\":\"supports\",\"note\":\"Mo'in, Farhang-e Farsi s.v. چای (read via abadis.ir, which reproduces Mo'in's entry text): \\\"(اِ.) مأخوذ از چینی — درختی است کوچک دارای برگ‌های سبز و دندانه‌دار …\\\". The origin tag 'from Chinese' is exactly Nourai's arrow.\"},\n   {\"ref\":\"SHP:126\",\"status\":\"not_checked\",\"note\":\"Shipley 1945 not accessible (lending-only on IA; HathiTrust 403).\"}\n ],\n \"consulted\":[\n   {\"src\":\"MON\",\"where\":\"s.v. چای (vajehyab/abadis text of Farhang-e Mo'in)\",\"stance\":\"supports\",\"note\":\"\\\"مأخوذ از چینی\\\" — Chinese origin, no intermediary named.\"},\n   {\"src\":\"BQT\",\"where\":\"BQT_v2_pages.txt line 3693, Mo'in's footnote\",\"stance\":\"partial\",\"note\":\"\\\"۴ - معرب چای «صای» و «شای» است. رك: چای.\\\" — Borhan/Mo'in treat چای as the base form and «صای»/«شای» as its Arabicised shapes; they confirm the word but say nothing about the Chinese source at this point.\"},\n   {\"src\":\"LKT\",\"where\":\"entry 415 (leaf 60)\",\"stance\":\"supports\",\"note\":\"\\\"Chin. cha: 'Tee'; cha-ye 'Teeblätter' … hieraus pg. chá … russ. čaj …\\\" — the cha-ye 'tea leaves' form is the likely source of the Persian -y.\"},\n   {\"src\":\"HJB\",\"where\":\"leaf 948, s.v. TEA\",\"stance\":\"supports\",\"note\":\"Chhá \\\"is the form which has accompanied the knowledge of tea to India, Persia, Portugal, Greece and Russia\\\" — explicitly names Persia for the chá branch.\"},\n   {\"src\":\"ARY\",\"where\":\"ARY_pages.txt, grep 'چای'\",\"stance\":\"silent\",\"note\":\"Aryanpur's dictionary of Indo-European roots of Persian has no چای entry (it covers only inherited IE material).\"}\n ]\n})\n\nentry0[\"nodes\"].append({\n \"id\":2, \"lang\":\"Chinese\", \"words\":\"t'a\", \"verdict\":\"transcription_suspect\",\n \"derivation\":(\"The node is right in substance and wrong in its letter. The southern form that fed Malay teh, \"\n  \"Dutch thee and English tea is the Southern Min (Amoy/Hokkien, Xiamen) reading of 茶, tê — Wade-Giles t'e, \"\n  \"Skeat's 'të', Klein's 'dial. S. Chin. te', AHD's 'Amoy te'. There is no Chinese form t'a: Mandarin has chá, \"\n  \"Amoy has tê, and t'a would be neither. The printed page (PDF p. 104, book p. 74) shows 't'a : tea (South \"\n  \"Chinese accent)', so the extraction is faithful and the error is the book's own misprint — the more clearly \"\n  \"so because Nourai's own cited page, Klein 1578, prints 'te'. Read t'e, the node is confirmed: Amoy tê and \"\n  \"Mandarin chá are the same character 茶 in two dialect readings, both from Middle Chinese *ɖˠa, and the \"\n  \"coastal Amoy/Xiamen ports were where the first European tea cargoes were loaded.\"),\n \"derivation_fa\":(\"این گره در محتوا درست و در حرف نادرست است. صورت جنوبی‌ای که مالایی teh و هلندی thee و \"\n  \"انگلیسی tea از آن برآمده‌اند، خوانشِ مینِ جنوبی (لهجهٔ اَموی/شیامن) از نویسهٔ 茶 است، یعنی tê — که ویدـجایلز \"\n  \"آن را t'e می‌نویسد، اسکیت të، کلاین «dial. S. Chin. te» و فرهنگ American Heritage «Amoy te». صورتی به \"\n  \"شکل t'a در چینی وجود ندارد. تصویرِ صفحهٔ چاپی (ص ۷۴ کتاب = ص ۱۰۴ پی‌دی‌اف) خودِ «t'a» را نشان می‌دهد، پس \"\n  \"خطای خوانشِ اسکن نیست بلکه خطای چاپیِ کتاب است — به‌ویژه که همان صفحهٔ کلاین که نورایی بدان ارجاع داده \"\n  \"(ص ۱۵۷۸) «te» چاپ کرده است. با خواندنِ t'e، گره پذیرفتنی است: tê اَمویی و chá ماندارین دو خوانشِ یک نویسه‌اند \"\n  \"و هر دو از چینیِ میانهٔ *ɖˠa می‌آیند، و بندرهای اَموی/شیامن همان‌جایی بودند که نخستین محموله‌های چای اروپا \"\n  \"از آنجا بار زده شد.\"),\n \"error_in\":\"book\",\n \"book_prints\":\"t'a\",\n \"correct_form\":\"t'e (Amoy/Southern Min tê)\",\n \"sources\":[W[\"ahd_tea\"], W[\"ety_tea\"]],\n \"ref_check\":[\n   {\"ref\":\"KLN:1578\",\"status\":\"partial\",\"note\":KLN_TEA+\" Klein has the node — a southern Chinese dialect form feeding Malay teh — but prints it 'te', not 't'a'; so the reference supports the arrow and contradicts the printed form.\"},\n   {\"ref\":\"SHP:126\",\"status\":\"not_checked\",\"note\":\"Shipley 1945 not accessible (lending-only; HathiTrust 403).\"}\n ],\n \"consulted\":[\n   {\"src\":\"AHD\",\"where\":\"online AHD s.v. tea\",\"stance\":\"partial\",\"note\":\"\\\"from Malay teh, from Amoy te (equivalent to Mandarin chá)\\\" — the form is te, not t'a.\"},\n   {\"src\":\"SKT\",\"where\":\"leaf 520, s.v. Tea\",\"stance\":\"partial\",\"note\":\"\\\"From the Amoy pronunciation (të) of the Chinese name for the plant, which is (in other parts of the empire) called ch'a or ts'a\\\" — të, not t'a.\"},\n   {\"src\":\"LKT\",\"where\":\"entry 415 (leaf 60)\",\"stance\":\"partial\",\"note\":\"\\\"Im Dialekt von Amoy … wird etwa te gesprochen\\\" — te.\"},\n   {\"src\":\"HJB\",\"where\":\"leaf 948, s.v. TEA\",\"stance\":\"partial\",\"note\":\"\\\"Te (or Tay as Medhurst writes it) being the utterance attached to the character in the Fuh-kien dialect\\\" — Te/Tay, never t'a.\"}\n ]\n})\n\nentry0[\"nodes\"].append({\n \"id\":3, \"lang\":\"Malaysian\", \"words\":\"teh\", \"verdict\":\"confirmed\",\n \"derivation\":(\"Malay teh 'tea' was taken from Hokkien tê by the large Hokkien trading community of the Malay \"\n  \"archipelago; Malay -eh simply spells the mid front vowel of tê. It is the form the Dutch met in Java and \"\n  \"Batavia, and AHD, Klein and Hobson-Jobson all put it between Amoy and Dutch exactly as Nourai does. Two \"\n  \"small caveats: the language is Malay (Bahasa Melayu), not 'Malaysian' — the modern national standard of \"\n  \"Malaysia post-dates the borrowing by three centuries; and Skeat (1911) reverses the arrow, making Malay teh \"\n  \"a re-borrowing from European tea, an isolated view not followed by AHD or the OED.\"),\n \"derivation_fa\":(\"مالاییِ teh «چای» از هوکینِ (مینِ جنوبیِ) tê گرفته شده است؛ بازرگانان هوکین‌زبان در جزایر \"\n  \"مالایا این واژه را رواج دادند و «‑eh» مالایی تنها املای همان واکهٔ میانیِ پیشینِ tê است. همین صورت بود که \"\n  \"هلندی‌ها در جاوه و باتاویا با آن روبه‌رو شدند، و فرهنگ American Heritage و کلاین و هابسن‑جابسن هر سه آن را \"\n  \"دقیقاً در همان جایگاهی می‌نشانند که نورایی نشانده است. دو نکتهٔ کوچک: نام درستِ زبان «مالایی» است نه \"\n  \"«مالزیایی» — زبان معیارِ کشور مالزی سه سده پس از این وام‌گیری پدید آمد؛ و اسکیت (۱۹۱۱) جهت پیکان را وارونه \"\n  \"می‌کند و teh مالایی را وام‌گرفته از صورت‌های اروپایی می‌داند که دیدگاهی تنهاست و پذیرفته نشده. ادعای نورایی \"\n  \"در این گره درست است.\"),\n \"sources\":[W[\"ahd_tea\"], W[\"ety_tea\"]],\n \"ref_check\":[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"Nourai gives no reference for this node; it is covered by the KLN:1578 citation carried by the neighbouring nodes, which does name Malay teh.\"}],\n \"consulted\":[\n   {\"src\":\"KLN\",\"where\":\"KLN_1966.txt leaf 836 = printed p. 1578, s.v. tea\",\"stance\":\"supports\",\"note\":\"\\\"fr. Malay, teh, fr. dial. S. Chin. te\\\" — Malay standing between the Chinese dialect form and the West.\"},\n   {\"src\":\"AHD\",\"where\":\"online AHD s.v. tea\",\"stance\":\"supports\",\"note\":\"\\\"Probably Dutch thee, from Malay teh, from Amoy te\\\" — the same order.\"},\n   {\"src\":\"SKT\",\"where\":\"leaf 520, s.v. Tea\",\"stance\":\"contradicts\",\"note\":\"\\\"Hence Ital. tè, tea; F. thé, G. Thee, Malay teh, tea\\\" — Skeat derives Malay teh from the European forms, i.e. the opposite direction.\"},\n   {\"src\":\"HJB\",\"where\":\"leaf 948, s.v. TEA\",\"stance\":\"supports\",\"note\":\"\\\"though it may be probable that Te, like several other names of articles of trade, may have come to us through the Malay, the word is, not the less, originally Chinese\\\".\"}\n ]\n})\n\nentry0[\"nodes\"].append({\n \"id\":4, \"lang\":\"Dutch\", \"words\":\"thee\", \"verdict\":\"confirmed\",\n \"derivation\":(\"Dutch thee is the decisive link in the western chain: the Vereenigde Oostindische Compagnie \"\n  \"shipped tea from Java to Amsterdam from 1610, and from Dutch the word passed into French thé, German Tee, \"\n  \"Italian tè, Spanish té and English tea. Dutch <th> here is not a fricative — Dutch has no /θ/ — it is \"\n  \"simply a learned/etymologising spelling of /t/, which is why the borrowing surfaces as plain t- in French \"\n  \"and English. Etymonline states the reason for the Dutch role plainly: the form 'reflects the role of the \"\n  \"Dutch as chief importers of the leaves in that part of Europe (through the Dutch East India Company, from \"\n  \"1610)'.\"),\n \"derivation_fa\":(\"هلندیِ thee حلقهٔ سرنوشت‌سازِ زنجیرهٔ غربی است: کمپانی هند شرقیِ هلند از ۱۶۱۰ م. چای را از \"\n  \"جاوه به آمستردام می‌برد و از هلندی است که واژه به فرانسویِ thé، آلمانیِ Tee، ایتالیاییِ tè، اسپانیاییِ té و \"\n  \"انگلیسیِ tea راه یافت. «th» در هلندی سایشی نیست — هلندی /θ/ ندارد — و تنها املایی است ریشه‌شناسانه برای /t/؛ \"\n  \"به همین سبب وام‌واژه در فرانسوی و انگلیسی با t سادهٔ بی‌دمش پدیدار می‌شود. اتیمانلاین علت نقش هلندی را \"\n  \"روشن می‌گوید: این صورت «بازتاب نقش هلندی‌ها همچون واردکنندگان اصلی برگ چای در آن بخش از اروپا (از راه \"\n  \"کمپانی هند شرقیِ هلند، از ۱۶۱۰)» است. ادعای نورایی درست است.\"),\n \"sources\":[W[\"ety_tea\"], W[\"ahd_tea\"]],\n \"ref_check\":[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"No reference given by Nourai for this node.\"}],\n \"consulted\":[\n   {\"src\":\"AHD\",\"where\":\"online AHD s.v. tea\",\"stance\":\"supports\",\"note\":\"\\\"[Probably Dutch thee, from Malay teh …]\\\" — Dutch is the immediate source of English.\"},\n   {\"src\":\"LKT\",\"where\":\"entry 415 (leaf 60)\",\"stance\":\"supports\",\"note\":\"\\\"daher frz. thé, sp. té, it. tè [seltener ciä], ndl. thee, dtsch. Tee, engl. tea\\\" — Dutch thee among the western reflexes of Amoy te.\"},\n   {\"src\":\"KLN\",\"where\":\"leaf 836 = p. 1578, s.v. tea\",\"stance\":\"contradicts\",\"note\":\"Klein routes English tea through French thé, not Dutch: \\\"tea, n. — F. the (the orig. pronunciation of E. tea was ta)\\\" — no Dutch step at all.\"}\n ]\n})\n\nentry0[\"nodes\"].append({\n \"id\":5, \"lang\":\"English\", \"words\":\"tea\", \"verdict\":\"confirmed\",\n \"derivation\":(\"English tea is first recorded in the 1650s (Pepys, 28 Sept. 1660, spells it tay), borrowed \"\n  \"from Dutch thee; the earlier and separate English chaa/cha (1590s) came from Portuguese chá via Macao and \"\n  \"represents the other branch of the same Chinese word. Down to the 18th c. tea was pronounced /teː/, rhyming \"\n  \"with obey — Pope's Rape of the Lock (1712) rhymes 'tea' with 'obey' — and only later shifted to /tiː/ by \"\n  \"the regular Great-Vowel-Shift-era raising of ME/eModE ē. Nourai's Amoy → Malay → Dutch → English chain is \"\n  \"the AHD's and the OED's; only Klein interposes French thé instead of Dutch.\"),\n \"derivation_fa\":(\"انگلیسیِ tea نخستین‌بار در دههٔ ۱۶۵۰ م. دیده می‌شود (پیپس در ۲۸ سپتامبر ۱۶۶۰ آن را tay \"\n  \"می‌نویسد) و وام‌گرفته از هلندیِ thee است؛ صورتِ کهن‌تر و جداگانهٔ chaa/cha در انگلیسیِ دههٔ ۱۵۹۰ از \"\n  \"پرتغالیِ chá از راه ماکائو آمده و نمایندهٔ شاخهٔ دیگرِ همان واژهٔ چینی است. تا سدهٔ ۱۸ م. tea را /teː/ \"\n  \"می‌خواندند و با obey هم‌قافیه بود — چنان‌که در «ربودن طرّهٔ گیسو»ی الکساندر پوپ (۱۷۱۲) — و تنها بعدها بر \"\n  \"اثر افراشتگیِ منظمِ ē به /tiː/ بدل شد. زنجیرهٔ اَموی ← مالایی ← هلندی ← انگلیسیِ نورایی همان زنجیرهٔ فرهنگ \"\n  \"American Heritage و آکسفورد است؛ تنها کلاین به‌جای هلندی، فرانسویِ thé را میانجی می‌گیرد. ادعای نورایی درست است.\"),\n \"sources\":[W[\"ety_tea\"], W[\"ahd_tea\"]],\n \"ref_check\":[\n   {\"ref\":\"AHD:1320\",\"status\":\"supports\",\"note\":\"Online AHD s.v. tea (the modern edition of the dictionary whose 1975 p. 1320 Nourai cites): \\\"[Probably Dutch thee, from Malay teh, from Amoy te (equivalent to Mandarin chá), from dialectal Early Middle Chinese da; akin to Middle Chinese drεː (source of Mandarin chá, tea); see CHANOYU.]\\\" — Nourai's chain node for node.\"},\n   {\"ref\":\"KLN:1578\",\"status\":\"partial\",\"note\":KLN_TEA+\" Klein confirms Malay teh and the S. Chinese dialect form, but makes English tea a borrowing from French thé rather than Dutch thee, and prints the Chinese form 'te'.\"}\n ],\n \"consulted\":[\n   {\"src\":\"AHD\",\"where\":\"online AHD s.v. tea\",\"stance\":\"supports\",\"note\":\"See ref_check — Dutch/Malay/Amoy chain.\"},\n   {\"src\":\"KLN\",\"where\":\"leaf 836 = p. 1578\",\"stance\":\"partial\",\"note\":\"Klein: English tea < French thé; the note that \\\"the orig. pronunciation of E. tea was tā\\\" independently confirms the 17th-c. /teː/.\"},\n   {\"src\":\"SKT\",\"where\":\"leaf 520, s.v. Tea\",\"stance\":\"supports\",\"note\":\"\\\"Spelt tay in Pepys' Diary, Sept. 28, 1660; cha in Blount (1674). From the Amoy pronunciation (të) …\\\" — the two English forms and their two Chinese sources.\"},\n   {\"src\":\"HJB\",\"where\":\"leaf 948, s.v. TEA\",\"stance\":\"supports\",\"note\":\"\\\"The original pronunciation, whether direct from Fuh-kien or through the Malay, accompanied the introduction of tea to England as well as other countries of Western Europe. This is shown by several couplets in Pope.\\\"\"}\n ]\n})\n\n# ---------------------------------------------------------------- entry 2\nAHD_CHARLATAN = (\"Online AHD s.v. charlatan: \\\"[French, from Italian ciarlatano, probably alteration \"\n \"(influenced by ciarlare, to prattle) of cerretano, inhabitant of Cerreto, a city of Italy once famous for \"\n \"its quacks.]\\\"\")\nAHD_CHARADE = (\"Online AHD s.v. charade: \\\"[French, probably from Provençal charrado, chat, from charra, to \"\n \"chat, chatter, perhaps from Italian ciarlare.]\\\"\")\n\nentry2 = {\n \"entry\": 2,\n \"root\": \"Čar, Char\",\n \"verdict\": \"disputed\",\n \"modern_form\": \"no reconstructible PIE root; Italian ciarlare / Spanish charlar / Occitan charrar 'to chatter' are independent Romance onomatopoeias\",\n \"note\": (\"The language label is the problem. 'Čar, Char : idle chat' is not an Indo-European root in any \"\n  \"modern repertory: it is absent from Pokorny, from Walde-Pokorny and from Watkins/AHD, and every authority \"\n  \"that treats the words hanging under it calls them imitative creations of the Romance vernaculars — Klein \"\n  \"'of imitative origin', AHD 'of imitative origin', Etymonline 'echoic', 'perhaps imitative of ducks' \"\n  \"quacking'. Pokorny does have expressive/echoic bases in this semantic field (gar- 'rufen, schreien' POK 352, \"\n  \"whence Latin garrīre 'to chatter'; ker-² 'echoic root'), but nobody derives ciarlare/charrar from them — \"\n  \"Romance onomatopoeias of this shape are formed afresh in each period and are not inherited. Nourai's source \"\n  \"is Shipley's Origins of English Words, a book of IE roots that regularly promotes such expressive bases to \"\n  \"root status; it could not be consulted (see ref_check). Two further defects: the Italian branch is hung on \"\n  \"the wrong peg (Cerreto is a place name from Latin cerrus 'turkey oak', node #1), and the 'French' charra/\"\n  \"charrado are Provençal (Occitan), as Nourai's own cited AHD page says (node #5). The individual Romance and \"\n  \"English links, taken on their own, are sound.\"),\n \"note_fa\": (\"مشکل در برچسب زبانی است. «Čar, Char» به معنای «گپِ بیهوده» در هیچ فهرست امروزی ریشهٔ \"\n  \"هندواروپایی نیست: نه در پوکورنی هست، نه در والده‑پوکورنی و نه در واتکینز/AHD؛ و هر مرجعی که واژه‌های زیر \"\n  \"این جعبه را بررسی کرده، آن‌ها را ساخته‌هایی آوانمادین (onomatopoeic) در زبان‌های رومی می‌داند — کلاین «of \"\n  \"imitative origin»، فرهنگ American Heritage همان، و اتیمانلاین «echoic». درست است که پوکورنی ریشه‌های \"\n  \"آوانمادینی در همین حوزهٔ معنایی دارد (gar- «بانگ زدن، فریاد کشیدن»، ص ۳۵۲، که garrīre لاتین از آن است؛ و \"\n  \"ker-²)، اما هیچ‌کس ciarlare و charrar را از آن‌ها نمی‌گیرد: آوانماهای رومی از این‌گونه در هر دوره از نو \"\n  \"ساخته می‌شوند و ارثی نیستند. مأخذ نورایی کتاب شیپلی است که چنین ستاک‌های آوانمادین را پیوسته به مقام «ریشه» \"\n  \"برمی‌کشد و دسترس‌پذیر نبود. دو ایراد دیگر: شاخهٔ ایتالیایی به قلاب نادرست آویخته شده (Cerreto نام جای است، \"\n  \"از cerrus لاتین «بلوطِ ترکی») و charra/charrado «فرانسوی» در واقع پرووانسی (اکسیتان) است — چنان‌که خودِ \"\n  \"صفحهٔ AHD مورد استناد نورایی می‌گوید. پژوهش امروزی این ریشه را رد می‌کند، هرچند تک‌تک حلقه‌های رومی و \"\n  \"انگلیسی به‌خودیِ‌خود درست‌اند.\"),\n \"sources\":[W[\"ety_charlatan\"], W[\"ety_charade\"], W[\"ahd_charlatan\"], W[\"ahd_charade\"]],\n \"ref_check\":[\n   {\"ref\":\"OEW:51\",\"status\":\"not_checked\",\"note\":\"Shipley, The Origins of English Words (1984) — both archive.org copies (originsofenglish0000ship, originsofenglish00jose) are lending-only; the IA in-book search endpoint returns 'Item not available' and the FTS API returns nothing; no local OCR and no HathiTrust full view. Nourai's sole authority for this root box therefore could not be inspected.\"}\n ],\n \"consulted\":[\n   {\"src\":\"POK\",\"where\":\"POK_full.txt, grep 'Schallwurzel' and the gar-/ker- articles\",\"stance\":\"silent\",\"note\":\"No root of the shape *ker-/*kar-/*ǵʰer- glossed 'idle chat' exists in Pokorny; the nearest is gar- 'rufen, schreien' (p. 352) and the echoic ker-, neither of which is connected to the Romance chatter verbs by any source.\"},\n   {\"src\":\"AHD\",\"where\":\"AHD_watkins1985.txt line 479, s.v. gar-\",\"stance\":\"contradicts\",\"note\":\"\\\"gar-. To call, cry. Expressive root. … 3. Suffixed form (with expressive gemination) *garr-iyo- in Latin garrire, to chatter: GARRULOUS. [Pok. gar- 352.]\\\" — Watkins's IE root list has an expressive 'call/cry' root but attaches only Latin garrīre to it; charlatan and charade are not listed under any root, because AHD treats them as imitative Romance.\"},\n   {\"src\":\"KLN\",\"where\":\"KLN_1966.txt leaf 152 (printed pp. 268/269), s.vv. charade, charlatan\",\"stance\":\"contradicts\",\"note\":\"\\\"charade, n. … fr. Provenç. charrado, 'talk, chat', fr. charra, 'to talk, chat', which is of imitative origin. Cp. It. ciarlare, Sp. charlar, 'to talk, prattle'.\\\" Klein assigns no IE base at all — 'of imitative origin' is his whole etymology.\"},\n   {\"src\":\"WLD\",\"where\":\"WLD_band3.txt / WLD_Bd1, grep for a car-/char- chatter base\",\"stance\":\"silent\",\"note\":\"Walde-Pokorny lists no base glossed 'idle chat' of this shape.\"}\n ],\n \"nodes\":[]\n}\n\nentry2[\"nodes\"].append({\n \"id\":1, \"lang\":\"Italian\", \"words\":\"Cerreto; Cerretano; ciarlatano\", \"verdict\":\"disputed\",\n \"derivation\":(\"Word by word. (a) Cerreto is a real Umbrian town near Spoleto (today Cerreto di Spoleto), and \"\n  \"its name has nothing to do with chatter: it is Latin cerrētum 'oak grove', a collective in -ētum from cerrus \"\n  \"'turkey oak' — so the arrow root('idle chat') → Cerreto is wrong, and this is what makes the node disputed. \"\n  \"(b) Cerretano 'man of Cerreto' is the regular Italian ethnic in -ano (cf. romano, napoletano); from the 15th \"\n  \"c. the men of Cerreto were licensed alms-collectors for the hospital of Santa Maria della Stella and the \"\n  \"word came to mean 'itinerant quack, mountebank'. (c) ciarlatano is cerretano deformed under the pull of \"\n  \"ciarlare 'to prattle' (< ciarla 'chatter', imitative) — a textbook contamination, and the reason the two \"\n  \"families cross at all. AHD (Nourai's own citation) and Klein both give exactly this; Etymonline and the OED \"\n  \"prefer to derive ciarlatano straight from ciarla and treat Cerreto as folk etymology. So Nourai has picked \"\n  \"one of the two standard accounts — defensible for ciarlatano, but he has then wrongly made the toponym \"\n  \"Cerreto itself a derivative of his chatter root.\"),\n \"derivation_fa\":(\"واژه‌به‌واژه: (الف) Cerreto شهری است حقیقی در اومبریا نزدیک اسپولتو، و نامش هیچ پیوندی با \"\n  \"«گپ» ندارد: از cerrētum لاتین «بلوطستان» است، اسم جمعی با پسوند ‑ētum از cerrus «بلوطِ ترکی» — پس پیکانِ \"\n  \"«ریشهٔ گپِ بیهوده ← Cerreto» نادرست است و همین گره را مردود می‌کند. (ب) Cerretano «مردِ اهل چرّتو» صفتِ \"\n  \"نسبیِ منظمِ ایتالیایی با پسوند ‑ano است (مانند romano، napoletano)؛ از سدهٔ ۱۵ م. مردان چرّتو صدقه‌گیرانِ \"\n  \"پروانه‌دارِ بیمارستانِ سانتا ماریا دلا استلا بودند و واژه معنای «دوره‌گردِ حقه‌باز» یافت — تحول معنایی از \"\n  \"نام جای به پیشه. (ج) ciarlatano همان cerretano است که زیر کشش ciarlare «وراجی کردن» (از ciarla، آوانمادین) \"\n  \"دگرگون شده — نمونه‌ای کلاسیک از آمیختگی، و همین‌جاست که دو خانواده به هم می‌رسند. فرهنگ American Heritage \"\n  \"(همان مأخذ نورایی) و کلاین دقیقاً همین را می‌گویند؛ اتیمانلاین و آکسفورد ciarlatano را یکسره از ciarla \"\n  \"می‌گیرند و داستان چرّتو را ریشه‌شناسی عامیانه می‌شمارند. نورایی یکی از دو روایتِ معتبر را برگزیده — که برای \"\n  \"ciarlatano پذیرفتنی است — اما خودِ نامِ جای Cerreto را به‌خطا زادهٔ ریشهٔ «گپ» دانسته است.\"),\n \"sources\":[W[\"ahd_charlatan\"], W[\"ety_charlatan\"]],\n \"ref_check\":[\n   {\"ref\":\"AHD:227\",\"status\":\"supports\",\"note\":AHD_CHARLATAN+\" — the Cerreto → cerretano → ciarlatano chain with ciarlare as the contaminating form, i.e. Nourai's three Italian words in Nourai's order. (AHD does not, however, derive Cerreto from a 'chat' root.)\"},\n   {\"ref\":\"FSD:452\",\"status\":\"partial\",\"note\":\"Funk & Wagnalls (FSD_vol1.txt leaf 507, printed p. ≈452, s.v. charlatan): \\\"[F., < It. ciarlatano, < ciarla, prattle.]\\\" — F&W has the word and the Italian source but derives it from ciarla only; grepping the whole of FSD vol. I for 'Cerreto', 'cerretano' finds nothing, so this reference does not support the Cerreto half of the node.\"}\n ],\n \"consulted\":[\n   {\"src\":\"KLN\",\"where\":\"KLN_1966.txt leaf 152 (printed pp. 268/269), s.v. charlatan\",\"stance\":\"supports\",\"note\":\"\\\"charlatan, n., a pretender; a quack. — F., fr. It. ciarlatano, fr. earlier cerretano, of s.m., fr. ML. ceretanus, lit. 'inhabitant of Cerreto', a town near Spoleto in Italy, famous for its quacks and impostors. It. ciarlatano was influenced in form by It. ciarlare, 'to prattle'.\\\"\"},\n   {\"src\":\"FSD\",\"where\":\"FSD_vol1.txt leaf 507 (printed p. ≈452)\",\"stance\":\"partial\",\"note\":\"\\\"[F., < It. ciarlatano, < ciarla, prattle.]\\\" — no Cerreto.\"},\n   {\"src\":\"WEB\",\"where\":\"WEB_vol1.txt leaf 334, s.v. charlatan\",\"stance\":\"partial\",\"note\":\"\\\"chàr'la-tan, n. [Fr., from It. ciarlatano, a quack, from ciarlare, to prate.]\\\" — Webster too goes straight to ciarlare, without Cerreto.\"},\n   {\"src\":\"AHD\",\"where\":\"online AHD s.v. charlatan\",\"stance\":\"supports\",\"note\":AHD_CHARLATAN}\n ]\n})\n\nentry2[\"nodes\"].append({\n \"id\":2, \"lang\":\"French\", \"words\":\"charlatan\", \"verdict\":\"confirmed\",\n \"derivation\":(\"French charlatan is a 16th-century borrowing of Italian ciarlatano (first in Rabelais, 1532, \"\n  \"as charlatans/ciarlatans), one of the flood of Italian words that entered French during the Italian wars \"\n  \"and the Medici regencies; Italian ci- /tʃ/ was naturalised as French ch- /ʃ/, the regular substitution in \"\n  \"that period (cf. It. ciarlare → Fr. charlatanerie). The sense stayed 'mountebank who sells remedies in the \"\n  \"street, babbler' and only later generalised to 'impostor claiming knowledge he lacks'. Klein, AHD, \"\n  \"Etymonline and Funk & Wagnalls all agree on the Italian→French step, whatever they think of Cerreto.\"),\n \"derivation_fa\":(\"فرانسویِ charlatan وام‌واژه‌ای از ciarlatano ایتالیایی است در سدهٔ ۱۶ م. (نخستین کاربرد نزد \"\n  \"رابله، ۱۵۳۲ م.)، یکی از انبوه واژه‌های ایتالیایی که در پی جنگ‌های ایتالیا و نیابتِ سلطنتِ مدیچی‌ها به \"\n  \"فرانسوی راه یافت؛ /tʃ/ ایتالیایی (ci‑) به قاعدهٔ همان دوره به /ʃ/ فرانسوی (ch‑) بدل شد. معنا نخست همان \"\n  \"«دوره‌گردی که در کوچه دارو می‌فروشد، وراج» ماند و بعدها به «مدّعیِ دانشی که ندارد» گسترش یافت. کلاین، \"\n  \"فرهنگ American Heritage، اتیمانلاین و فانک اند واگنالز همگی در گامِ ایتالیایی ← فرانسوی هم‌داستان‌اند، \"\n  \"هرچند دربارهٔ چرّتو اختلاف دارند. ادعای نورایی در این گره درست است.\"),\n \"sources\":[W[\"ahd_charlatan\"], W[\"ety_charlatan\"]],\n \"ref_check\":[{\"ref\":\"AHD:227\",\"status\":\"supports\",\"note\":AHD_CHARLATAN+\" — 'French, from Italian ciarlatano' is precisely this arrow.\"}],\n \"consulted\":[\n   {\"src\":\"KLN\",\"where\":\"leaf 152 (printed pp. 268/269), s.v. charlatan\",\"stance\":\"supports\",\"note\":\"\\\"— F., fr. It. ciarlatano\\\".\"},\n   {\"src\":\"FSD\",\"where\":\"FSD_vol1.txt leaf 507 (printed p. ≈452)\",\"stance\":\"supports\",\"note\":\"\\\"[F., < It. ciarlatano …]\\\".\"},\n   {\"src\":\"WEB\",\"where\":\"WEB_vol1.txt leaf 334\",\"stance\":\"supports\",\"note\":\"\\\"[Fr., from It. ciarlatano, a quack …]\\\".\"}\n ]\n})\n\nentry2[\"nodes\"].append({\n \"id\":3, \"lang\":\"Persian\", \"words\":\"čârlâtân\", \"verdict\":\"transcription_suspect\",\n \"derivation\":(\"The etymology is right and the transliteration is wrong. Persian شارلاتان is a 20th-century \"\n  \"loan from French charlatan, taken in through the same channel as most European vocabulary in Persian \"\n  \"(French-medium schooling and journalism from the late Qajar period); Mo'in and Dehkhoda both tag it [فر.] \"\n  \"'French' and gloss it حقه‌باز، شیاد، کلاهبردار. French /ʃ/ is rendered by Persian ش, so the word is \"\n  \"šārlātān — but the book transliterates it čârlâtân, with č, which would require an initial چ. Nourai's \"\n  \"system uses č for the sound of ch in 'church', so čârlâtân contradicts his own Persian script in the same \"\n  \"box. I rendered PDF p. 104 at 600 dpi and read the node: the printed page itself shows 'čârlâtân' beside \"\n  \"شارلاتان, so the extraction is faithful and this is the author's misprint (or a mechanical consequence of \"\n  \"filing the word under the letter C). Read šārlātān, the node is confirmed.\"),\n \"derivation_fa\":(\"ریشه‌شناسی درست است و آوانگاری نادرست. «شارلاتان» وام‌واژه‌ای است از فرانسویِ charlatan در \"\n  \"سدهٔ ۱۴ ش./۲۰ م.، که مانند بیشتر واژه‌های اروپاییِ فارسی از مجرای آموزش و روزنامه‌نگاریِ فرانسوی‌مآبِ اواخر \"\n  \"دورهٔ قاجار وارد شد؛ معین و دهخدا هر دو آن را با نشانهٔ [فر.] می‌آورند و «حقه‌باز، شیاد، کلاهبردار» معنا \"\n  \"می‌کنند. /ʃ/ فرانسوی در فارسی با «ش» نوشته می‌شود، پس تلفظ šārlātān است؛ اما کتاب آن را čârlâtân آوانویسی \"\n  \"کرده که با «چ» می‌خواند و با خطّ فارسیِ همان جعبه ناسازگار است. صفحهٔ ۱۰۴ پی‌دی‌اف را با تفکیک ۶۰۰ نقطه \"\n  \"بازنمایی کردم و خواندم: خودِ صفحهٔ چاپی «čârlâtân» را در کنار «شارلاتان» نشان می‌دهد، پس این خطای خوانشِ \"\n  \"اسکن نیست بلکه خطای چاپیِ کتاب است — احتمالاً پیامد ناگزیرِ جای دادنِ واژه ذیل حرف C. با خواندنِ šārlātān \"\n  \"گره پذیرفتنی است.\"),\n \"error_in\":\"book\",\n \"book_prints\":\"čârlâtân\",\n \"correct_form\":\"šârlâtân (شارلاتان)\",\n \"sources\":[W[\"ab_sharlatan\"], W[\"ahd_charlatan\"]],\n \"ref_check\":[\n   {\"ref\":\"VOP:234\",\"status\":\"not_checked\",\"note\":\"Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi (Alborz 1371/1992) — refs_online.json records kind 'none': repeated searches of archive.org, ketabnak, noorlib and the open web have not turned up a copy, so this reference cannot be inspected.\"}\n ],\n \"consulted\":[\n   {\"src\":\"MON\",\"where\":\"s.v. شارلاتان (Farhang-e Mo'in text via abadis.ir)\",\"stance\":\"supports\",\"note\":\"Origin tag [فر.] (French); gloss \\\"حقه باز، شیاد، کلاهبردار\\\". Mo'in's own headword is spelled with ش, confirming šārlātān against the book's čârlâtân. The word is also in the local OCR: MON_part1.txt line 82946 \\\"شارلاتان؛ ۱۲۱۲۰ (ص.) حقه‌باز، متقلب.\\\"\"},\n   {\"src\":\"ARY\",\"where\":\"ARY_pages.txt, grep 'شارلاتان'\",\"stance\":\"silent\",\"note\":\"Aryanpur's Indo-European roots dictionary has no entry (it does not cover modern European loans).\"},\n   {\"src\":\"AHD\",\"where\":\"online AHD s.v. charlatan\",\"stance\":\"supports\",\"note\":AHD_CHARLATAN+\" — the French donor form Nourai's arrow requires.\"}\n ]\n})\n\nentry2[\"nodes\"].append({\n \"id\":4, \"lang\":\"English\", \"words\":\"charlatan\", \"verdict\":\"confirmed\",\n \"derivation\":(\"English charlatan is attested from the 1610s, borrowed from French charlatan (Klein, Funk & \"\n  \"Wagnalls and Webster all mark it 'F.'), with the sense 'mountebank, babbler' and the modern generalisation \"\n  \"'one who pretends to knowledge or skill he does not possess'. The word kept its French spelling and, at \"\n  \"first, a French-ish stress; the derivatives charlatanism (a hybrid of the French word and the Greek suffix \"\n  \"-ism, per Klein) and charlatanry are 17th–18th-c. English formations.\"),\n \"derivation_fa\":(\"انگلیسیِ charlatan از دههٔ ۱۶۱۰ م. گواهی شده و وامی است از فرانسویِ charlatan — کلاین، فانک \"\n  \"اند واگنالز و وبستر هر سه آن را «F.» نشانه‌گذاری می‌کنند — نخست به معنای «دوره‌گردِ دارو‌فروش، وراج» و سپس \"\n  \"با تعمیم معنایی «مدّعیِ دانش یا مهارتی که ندارد». واژه املای فرانسویِ خود را نگاه داشت و در آغاز تکیهٔ \"\n  \"فرانسوی‌وار نیز داشت؛ مشتق‌های charlatanism (به گفتهٔ کلاین آمیزه‌ای از واژهٔ فرانسوی و پسوند یونانیِ ‑ism) \"\n  \"و charlatanry ساخته‌های انگلیسیِ سده‌های ۱۷ و ۱۸ م.اند. ادعای نورایی درست است.\"),\n \"sources\":[W[\"ety_charlatan\"], W[\"ahd_charlatan\"]],\n \"ref_check\":[{\"ref\":\"AHD:227\",\"status\":\"supports\",\"note\":AHD_CHARLATAN+\" — the entry is an English headword whose etymology begins 'French', which is Nourai's arrow.\"}],\n \"consulted\":[\n   {\"src\":\"KLN\",\"where\":\"leaf 152 (printed pp. 268/269)\",\"stance\":\"supports\",\"note\":\"\\\"charlatan, n., a pretender; a quack. — F., fr. It. ciarlatano …\\\"; and at leaf 152 \\\"charlatanism, n. — A hybrid coined fr. prec. word and -ism, a suff. of Greek origin.\\\"\"},\n   {\"src\":\"FSD\",\"where\":\"FSD_vol1.txt leaf 507 (printed p. ≈452)\",\"stance\":\"supports\",\"note\":\"\\\"[F., < It. ciarlatano, < ciarla, prattle.] charlatanic … charlatanry, n. The arts or practises of a charlatan; undue or fraudulent pretensions to skill; quackery.\\\"\"},\n   {\"src\":\"WEB\",\"where\":\"WEB_vol1.txt leaf 334\",\"stance\":\"supports\",\"note\":\"\\\"one who makes untruthful pretensions; a quack; a mountebank; an impostor.\\\"\"}\n ]\n})\n\nentry2[\"nodes\"].append({\n \"id\":5, \"lang\":\"French\", \"words\":\"charra; charrado\", \"verdict\":\"plausible\",\n \"derivation\":(\"The two forms are real but the language label is off by one: charra 'to chat' and charrado \"\n  \"'chat, long talk' are Provençal (Occitan), not French — as Nourai's own cited page says, AHD deriving \"\n  \"charade from 'Provençal charrado, chat, from charra, to chat, chatter'. Klein says the same, adding that \"\n  \"charra 'is of imitative origin. Cp. It. ciarlare, Sp. charlar'. The gloss 'a game of phrases and words' for \"\n  \"charrado is anachronistic: in Occitan the word means simply 'talk, chatter'; the riddle-game sense is a \"\n  \"specialisation that happened in French charade in the 1770s. And since the root box above is not a genuine \"\n  \"IE root (see entry note), the arrow into this node cannot be more than an assertion that the word is \"\n  \"expressive — which is true, and is all any source claims for it.\"),\n \"derivation_fa\":(\"هر دو صورت واقعی‌اند اما برچسب زبان یک پله جابه‌جا شده است: charra «گپ زدن» و charrado «گپ، \"\n  \"سخنِ دراز» پرووانسی (اکسیتان)اند نه فرانسوی — چنان‌که خودِ صفحه‌ای که نورایی بدان استناد کرده می‌گوید: \"\n  \"فرهنگ American Heritage واژهٔ charade را از «پرووانسیِ charrado، گپ، از charra، گپ زدن» می‌گیرد. کلاین نیز \"\n  \"همین را می‌آورد و می‌افزاید که charra «آوانمادین است؛ سنجیده شود با ciarlare ایتالیایی و charlar \"\n  \"اسپانیایی». معنای «بازیِ عبارت‌ها و واژه‌ها» برای charrado زمان‌پریشی است: در اکسیتان این واژه تنها «گپ» \"\n  \"معنا می‌دهد و معنای بازیِ چیستان تخصیصی است که در سدهٔ ۱۸ م. در فرانسویِ charade روی داد. و چون جعبهٔ ریشهٔ \"\n  \"بالای این گره ریشهٔ هندواروپاییِ حقیقی نیست، پیکانِ ورودی چیزی بیش از این نمی‌گوید که واژه آوانمادین است — \"\n  \"که درست است و همهٔ آن چیزی است که منابع ادعا می‌کنند. با احتیاط پذیرفتنی است.\"),\n \"sources\":[W[\"ahd_charade\"], W[\"ety_charade\"]],\n \"ref_check\":[\n   {\"ref\":\"AHD:228\",\"status\":\"partial\",\"note\":AHD_CHARADE+\" — the forms charrado and charra are Nourai's, in Nourai's order, but AHD labels them Provençal, not French, and glosses charrado 'chat', not 'a game of phrases and words'.\"}\n ],\n \"consulted\":[\n   {\"src\":\"KLN\",\"where\":\"KLN_1966.txt leaf 152 (printed pp. 268/269), s.v. charade\",\"stance\":\"partial\",\"note\":\"\\\"charade, n., a riddle based on the syllables of a word. — F., fr. Provenç. charrado, 'talk, chat', fr. charra, 'to talk, chat', which is of imitative origin. Cp. It. ciarlare, Sp. charlar, 'to talk, prattle'.\\\" — Provençal, and 'talk, chat' for charrado.\"},\n   {\"src\":\"AHD\",\"where\":\"online AHD s.v. charade\",\"stance\":\"partial\",\"note\":AHD_CHARADE},\n   {\"src\":\"FSD\",\"where\":\"FSD_vol1.txt leaf ≈503 (printed p. ≈447), s.v. charade; grep 'charrado' across all four volumes\",\"stance\":\"silent\",\"note\":\"Funk & Wagnalls has the headword charade but the OCR of its bracketed etymology is unreadable, and no volume contains the string 'charrado' or 'Provencal char-'.\"}\n ]\n})\n\nentry2[\"nodes\"].append({\n \"id\":6, \"lang\":\"English\", \"words\":\"charades\", \"verdict\":\"confirmed\",\n \"derivation\":(\"English charade is first recorded in 1776, borrowed from French charade (itself attested from \"\n  \"the 1770s, from Provençal charrado). The original charade was a spoken riddle in which each syllable of a \"\n  \"word was described separately and then the whole — the syllable-by-syllable structure is why an \"\n  \"'idle-talk' word could name it. The acted 'dumb charades' developed in the 19th c. and gave the modern \"\n  \"party game, normally called by the plural charades, which is the form Nourai's box gives. The chain \"\n  \"Provençal → French → English is Klein's, AHD's and Etymonline's alike.\"),\n \"derivation_fa\":(\"انگلیسیِ charade نخستین‌بار در ۱۷۷۶ م. ثبت شده و وامی است از فرانسویِ charade (خودْ از \"\n  \"دههٔ ۱۷۷۰ م.، از پرووانسیِ charrado). شکلِ نخستینِ این بازی چیستانی گفتاری بود که در آن هر هجای واژه جداگانه \"\n  \"و سپس کلِ واژه توصیف می‌شد — و همین ساختِ هجابه‌هجاست که سبب شد واژه‌ای به معنای «گپ» نامِ آن شود. گونهٔ \"\n  \"نمایشی و بی‌کلام («dumb charades») در سدهٔ ۱۹ م. پدید آمد و بازیِ امروزی از آن برخاست که معمولاً به صیغهٔ \"\n  \"جمع charades خوانده می‌شود — همان صورتی که در جعبهٔ نورایی آمده است. زنجیرهٔ پرووانسی ← فرانسوی ← انگلیسی \"\n  \"را کلاین و فرهنگ American Heritage و اتیمانلاین یکسان می‌آورند. ادعای نورایی درست است.\"),\n \"sources\":[W[\"ety_charade\"], W[\"ahd_charade\"]],\n \"ref_check\":[{\"ref\":\"AHD:228\",\"status\":\"supports\",\"note\":AHD_CHARADE+\" — an English headword whose etymology begins 'French', exactly Nourai's arrow from the French box.\"}],\n \"consulted\":[\n   {\"src\":\"KLN\",\"where\":\"leaf 152 (printed pp. 268/269), s.v. charade\",\"stance\":\"supports\",\"note\":\"\\\"charade, n., a riddle based on the syllables of a word. — F., fr. Provenç. charrado …\\\" — the definition confirms the syllable-riddle original.\"},\n   {\"src\":\"WEB\",\"where\":\"WEB_vol1.txt leaf 334, s.v. charade\",\"stance\":\"supports\",\"note\":\"\\\"cha-rade', n. [Fr.] a game in which a chosen word or phrase to be guessed is acted out in pantomime, syllable by syllable or as a whole.\\\"\"},\n   {\"src\":\"FSD\",\"where\":\"FSD_vol1.txt leaf ≈503, s.v. charade\",\"stance\":\"partial\",\"note\":\"Headword present; the bracketed etymology is lost in the OCR.\"}\n ]\n})\n\n# ---------------------------------------------------------------- entry 3\nentry3 = {\n \"entry\": 3,\n \"root\": \"Čartěs, Xartěs\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"Ancient Greek χάρτης (khártēs) 'sheet/leaf of papyrus, paper'\",\n \"note\": (\"The root, the label and the gloss are all right: Greek χάρτης, masculine, 'sheet of papyrus, paper, \"\n  \"book'. Nourai's double headword 'Čartěs, Xartěs' is not two words but his own two transliterations of the \"\n  \"one Greek word (he files Greek χ under C so as to keep the English ch- derivatives together, and gives the \"\n  \"X-spelling as a cross-reference). Its two branches — east into Aramaic and Arabic, west into Latin — are \"\n  \"both real, and between them they account for Persian قرطاس and Persian کارت, which is Nourai's point: the \"\n  \"same Greek word reached Persian twice, thirteen centuries apart and from opposite directions. The root \"\n  \"box's own note, 'Probably from an Egyptian origin', is the traditional guess and is worth qualifying: Klein \"\n  \"says 'a foreign word, possibly of Egypt. origin' and Etymonline 'probably from Egyptian', but Beekes and \"\n  \"Chantraine reject the derivation from χαράσσω 'to scratch' and leave the word's origin unknown, while \"\n  \"Rendsburg proposes Phoenician ḥrṭyt 'that which has been written' (cf. Biblical Hebrew ḥéreṭ 'stylus'). So: \"\n  \"a loanword into Greek, source disputed, Egyptian only one candidate.\"),\n \"note_fa\": (\"ریشه و برچسب و معنا هر سه درست‌اند: یونانیِ χάρτης، مذکر، «برگ پاپیروس، کاغذ، کتاب». سرواژهٔ \"\n  \"دوگانهٔ «Čartěs, Xartěs» دو واژه نیست بلکه دو آوانگاریِ خودِ نورایی از یک واژهٔ یونانی است (او χ یونانی را \"\n  \"ذیل C می‌آورد تا مشتق‌های انگلیسیِ ch‑ کنار هم بمانند و صورت X را همچون ارجاع می‌دهد). هر دو شاخه‌اش — شرقی \"\n  \"به آرامی و عربی، غربی به لاتین — حقیقی‌اند و همین دو شاخه‌اند که «قرطاس» و «کارت» فارسی را پدید آورده‌اند؛ \"\n  \"و نکتهٔ نورایی هم همین است: یک واژهٔ یونانی دو بار، با فاصلهٔ سیزده سده و از دو سوی مخالف، به فارسی رسیده \"\n  \"است. یادداشتِ جعبهٔ ریشه، «احتمالاً خاستگاه مصری»، همان حدسِ سنتی است و باید مقید شود: کلاین می‌نویسد «واژه‌ای \"\n  \"بیگانه، شاید مصری» و اتیمانلاین «احتمالاً مصری»، اما بیکس و شانترن اشتقاق آن از χαράσσω «خراشیدن» را رد \"\n  \"می‌کنند و خاستگاه را نامعلوم می‌دانند، و رندزبورگ فینیقیِ ḥrṭyt «آنچه نوشته شده» را پیشنهاد می‌کند (سنجیده \"\n  \"شود با ḥéreṭ عبریِ کتاب مقدس «قلمِ حکاکی»). پس: وام‌واژه‌ای در یونانی، با خاستگاهی مورد اختلاف، که مصری تنها \"\n  \"یکی از نامزدهاست.\"),\n \"sources\":[W[\"wik_khartes\"], W[\"ety_card\"]],\n \"ref_check\":[\n   {\"ref\":\"KLN:239\",\"status\":\"supports\",\"note\":\"KLN_1966.txt leaf 136 (the leaf carries the printed page numbers 238/239 — exactly Nourai's citation), s.v. card: \\\"card, n., a piece of pasteboard for playing. — F. carte, fr. Late L. carta, 'a leaf of paper; paper', fr. L. charta, 'a leaf of the Egyptian papyrus; papyrus; paper', fr. Gk. χάρτης, of s.m., a foreign word, possibly of Egypt. origin. Cp. carte blanche, carte de visite, cartel, cartoon, cartouche, cartridge, cartulary, chart, charter, écarté, skat.\\\" — the root, the gloss 'leaf of the Egyptian papyrus', the 'possibly Egyptian' note and the whole Latin→French→English branch, on the cited page.\"},\n   {\"ref\":\"AHD:203\",\"status\":\"supports\",\"note\":\"The 1975 AHD's page 203 falls in the card–cart range; the corresponding entry in the online AHD (the modern edition of the same dictionary) derives card from Old French carte < Medieval Latin carta < Latin charta < Greek khartēs 'papyrus, document'. Checked via ahdictionary.com; the 1975 main dictionary itself is not open online (only the Watkins IE-roots appendix is on disk, and it has no entry for a non-IE loanword).\"},\n   {\"ref\":\"PRT:79\",\"status\":\"not_checked\",\"note\":\"Partridge, Origins (1958) — all archive.org copies (originsshortetym00part, originsetymologi0000part_j9t3, originsetymologi0000part) are lending-only; the IA in-book search and FTS endpoints return nothing. No local OCR.\"}\n ],\n \"consulted\":[\n   {\"src\":\"KLN\",\"where\":\"leaf 136 = printed p. 239, s.v. card; leaf 836 = p. 1578, s.v. taper\",\"stance\":\"supports\",\"note\":\"Besides the card entry, Klein s.v. taper glosses the Greek independently: \\\"L. charta, fr. Gk. χάρτης, 'papyrus; roll made from papyrus; the wick made from the pith of the papyrus'\\\" — same word, same gloss.\"},\n   {\"src\":\"LAT\",\"where\":\"LAT.txt line 11590 ff. (Ernout–Meillet, s.v. c(h)arta)\",\"stance\":\"supports\",\"note\":\"\\\"c(h)arta, -ae f.: feuille de papier; et par suite 'feuille écrite, lettre, livre, registres publics, documents écrits', etc. Emprunt ancien et latinisé du gr. χάρτης (–χάρτος), devenu féminin sous l'influence des autres thèmes en -a féminins … Panroman. M.L. 1866.\\\" — confirms the Greek source and the gender change that produced Latin carta.\"},\n   {\"src\":\"AHD\",\"where\":\"online AHD s.v. card\",\"stance\":\"supports\",\"note\":\"Greek khartēs → Latin charta → Old French carte → English card.\"}\n ],\n \"nodes\":[]\n}\n\nentry3[\"nodes\"].append({\n \"id\":1, \"lang\":\"Arabic\", \"words\":\"qertâs\", \"verdict\":\"plausible\",\n \"derivation\":(\"Arabic قِرْطاس qirṭās 'sheet of papyrus, paper' does come from Greek χάρτης, but not directly: \"\n  \"the standard account (Wiktionary, with Dehkhoda agreeing) routes it through Aramaic/Syriac קַרְטִיסָא \"\n  \"qarṭīsā, and the form itself shows it — Greek kh- appears as q- and the Greek nominative -ēs is replaced by \"\n  \"-ās, both characteristic of the Aramaic mediation that carried most Greek material culture words into \"\n  \"pre-Islamic Arabic, rather than of direct Greek→Arabic borrowing. The word is Qur'ānic (VI.7, 'a book on \"\n  \"qirṭās'; VI.91, plural qarāṭīs), so the borrowing is pre-Islamic, which fits the Aramaic route through the \"\n  \"Christian Arab centres of Syria and Iraq. That is why the verdict is 'plausible' rather than 'confirmed': \"\n  \"the source language of the etymon is right, the number of steps is not.\"),\n \"derivation_fa\":(\"عربیِ «قِرْطاس» به معنای «برگ پاپیروس، کاغذ» به‌راستی از یونانیِ χάρτης آمده است، اما نه \"\n  \"بی‌واسطه: روایتِ معیار (ویکی‌واژه، و دهخدا نیز همین را می‌گوید) آن را از راه آرامی/سریانیِ qarṭīsā می‌داند، \"\n  \"و خودِ صورتِ واژه گواه آن است — خِ یونانی به «ق» بدل شده و پایانهٔ فاعلیِ ‑ēs جای خود را به ‑ās داده، و هر \"\n  \"دو ویژگیِ همان میانجی‌گریِ آرامی است که بیشترِ واژه‌های فرهنگ مادیِ یونانی را به عربیِ پیش از اسلام رساند، \"\n  \"نه ویژگیِ وام‌گیریِ مستقیم از یونانی. واژه قرآنی است (انعام ۷: «کتاباً فی قرطاس»؛ و جمعِ «قراطیس» در انعام \"\n  \"۹۱)، پس وام‌گیری پیش از اسلام رخ داده و این با مسیر آرامی از راه مراکز عربِ مسیحیِ شام و عراق می‌خواند. از \"\n  \"همین‌روست که داوری «با احتیاط پذیرفتنی» است: زبانِ خاستگاه درست است اما شمارِ حلقه‌ها نه.\"),\n \"sources\":[W[\"wik_qirtas\"], W[\"ab_qertas\"]],\n \"ref_check\":[\n   {\"ref\":\"TAD:55\",\"status\":\"supports\",\"note\":\"al-Unaysi, Tafsir al-alfaz al-dakhila (TAD_pages.txt leaf 58, printed p. ≈53–55), s.v.: \\\"قرطاس — يوناني [χάρτης] معناه ما يُرسم به، مرادفه ورقة وصحيفة\\\" — 'qirṭās: Greek, its meaning is that on which one draws/writes; its synonyms waraqa and ṣaḥīfa'. Nourai's cited page: the entry states the Greek origin flatly, with no Aramaic step (which is why the node is 'plausible' rather than 'confirmed').\"},\n   {\"ref\":\"VDQ:342\",\"status\":\"not_checked\",\"note\":\"Badreh'i's Persian translation of Jeffery's Foreign Vocabulary of the Qur'an: the noorlib viewer (book 12868) is JavaScript-rendered and returns only site chrome to non-browser clients, and ketabnak blocks download. The underlying English original (FVQ) is on disk, but grepping FVQ_pages.txt for 'Qirtas', 'قرطاس', 'khartes' and 'χάρτης' finds only the bare headword line 'ﻗﺮﻃﺎﺱ (Qirṭās).' at line 8490 with the OCR of the entry body lost, so the substance could not be recovered from either copy.\"}\n ],\n \"consulted\":[\n   {\"src\":\"TAD\",\"where\":\"TAD_pages.txt leaf 58\",\"stance\":\"supports\",\"note\":\"See ref_check — 'قرطاس — يوناني … مرادفه ورقة وصحيفة'.\"},\n   {\"src\":\"AFM\",\"where\":\"AFM_pages.txt lines 3473–3474, s.v. الكاغد\",\"stance\":\"partial\",\"note\":\"\\\"( الكاغد ) فارسي محض بمعنى القرطاس … وأما القرطاس فمعرّب\\\" — Addi Shir distinguishes the Persian loan kāghad from qirṭās and marks qirṭās as muʿarrab, i.e. Arabicised from a foreign language, without naming Greek at this point.\"},\n   {\"src\":\"ARB\",\"where\":\"ARB_mo3rb.txt lines 19898–19900 (al-Jawaliqi, al-Muʿarrab)\",\"stance\":\"supports\",\"note\":\"Al-Jawaliqi lists القرطاس among the muʿarrab words, discussing the kasra/ḍamma of the qāf and citing the Qur'ānic 'كتاباً في قرطاس' (VI.7) with Maʿn al-Kufi's reading — an early Arabic acknowledgement that the word is a foreign borrowing.\"},\n   {\"src\":\"FVQ\",\"where\":\"FVQ_pages.txt line 8490\",\"stance\":\"silent\",\"note\":\"Jeffery's headword 'ﻗﺮﻃﺎﺱ (Qirṭās).' survives in the OCR but the entry body did not; nothing usable.\"},\n   {\"src\":\"KLN\",\"where\":\"leaf 136 = p. 239, s.v. card\",\"stance\":\"partial\",\"note\":\"Klein documents the Greek etymon and its Egyptian-papyrus sense but follows only the Latin branch; he says nothing about Arabic.\"}\n ]\n})\n\nentry3[\"nodes\"].append({\n \"id\":2, \"lang\":\"Persian\", \"words\":\"qertâs\", \"verdict\":\"confirmed\",\n \"derivation\":(\"Persian قرطاس qerṭās 'paper' is a straight Arabic loan of the classical period, one of the \"\n  \"large stock of Arabic writing-trade words that entered New Persian with the Islamic chancery; Mo'in tags it \"\n  \"[ع.] 'Arabic' and glosses it کاغذ, with the Arabic broken plural قراطیس qarāṭīs carried over intact. Persian \"\n  \"pronounces the Arabic i of qirṭās as e (qerṭās), the regular Iranian treatment of Arabic short i. Nourai's \"\n  \"Ferdowsi citation is apt — دبیر جهاندیده را خواند شاه / بیاورد قرطاس و مشک سیاه — and shows the word already \"\n  \"naturalised in the Shahnameh (c. 1010 CE) in its literal sense 'writing sheet', paired with مشک سیاه, the \"\n  \"lamp-black ink. In Persian it stayed a bookish word: the everyday term was and is کاغذ kāghaz. The ultimate \"\n  \"route is Greek → Aramaic → Arabic → Persian, which makes this the eastern of the two paths by which χάρτης \"\n  \"reached Persian (compare کارت, node #5).\"),\n \"derivation_fa\":(\"«قرطاس» فارسی وام‌واژه‌ای است یکسره عربی از دورهٔ کلاسیک، از همان انبوهِ واژه‌های دیوانی و \"\n  \"نوشت‌افزاریِ عربی که با دستگاه دبیریِ اسلامی به فارسیِ نو راه یافت؛ معین آن را با نشانهٔ [ع.] می‌آورد و \"\n  \"«کاغذ» معنا می‌کند و جمعِ مکسّرِ عربیِ «قراطیس» را نیز دست‌نخورده نگاه می‌دارد. کسرهٔ عربیِ qirṭās در فارسی \"\n  \"به «ـِ» بدل شده (qerṭās) که رفتار قاعده‌مندِ ایرانی با کسرهٔ کوتاهِ عربی است. شاهدِ فردوسی که نورایی آورده \"\n  \"بجاست — «دبیر جهاندیده را خواند شاه / بیاورد قرطاس و مُشک سیاه» — و نشان می‌دهد واژه در شاهنامه (حدود ۴۰۰ ق.) \"\n  \"در معنای لفظیِ «برگِ نوشتن» جا افتاده بوده و در کنار «مشک سیاه»، یعنی مرکّبِ دوده، به کار می‌رفته است. در \"\n  \"فارسی همواره واژه‌ای کتابی ماند و واژهٔ روزمره «کاغذ» بود و هست. مسیر نهایی چنین است: یونانی ← آرامی ← عربی \"\n  \"← فارسی، و این همان راهِ شرقیِ ورودِ χάρτης به فارسی است در برابر راهِ غربیِ «کارت» (گرهٔ ۵). ادعای نورایی \"\n  \"در این گره درست است.\"),\n \"sources\":[W[\"ab_qertas\"], W[\"wik_qirtas\"]],\n \"ref_check\":[\n   {\"ref\":\"MON:2659\",\"status\":\"supports\",\"note\":\"Mo'in, Farhang-e Farsi s.v. قرطاس (read via abadis.ir): \\\"(قِ ) [ ع . ] (اِ.) کاغذ. ج . قراطیس .\\\" — the [ع.] tag is precisely Nourai's Arabic → Persian arrow. The word is also in the local OCR of Mo'in in the definition of کاغذ (MON_part2.txt line 18658) and of طومار (MON_part1.txt line 93341: \\\"قرطاس مصری که از بردی (لوخ) و پاپیروس می‌ساختند\\\").\"}\n ],\n \"consulted\":[\n   {\"src\":\"MON\",\"where\":\"s.v. قرطاس (abadis text of Farhang-e Mo'in), and MON_part1.txt line 93341\",\"stance\":\"supports\",\"note\":\"\\\"[ ع . ] (اِ.) کاغذ. ج . قراطیس\\\"; and s.v. طومار, \\\"قرطاس مصری که از بردی (لوخ) و پاپیروس می‌ساختند\\\" — Mo'in even preserves the papyrus sense.\"},\n   {\"src\":\"BQT\",\"where\":\"Dehkhoda/Borhan material reproduced on abadis s.v. قرطاس\",\"stance\":\"supports\",\"note\":\"\\\"قرطاس خوانش عربی واژه سریانی و آرامی … به معنای پاپیروس می‌باشد که آن نیز برگرفته از واژه یونانی باستان\\\"; and \\\"اصلاً یونانی است مشتق از کارتس یعنی چیزی که بر آن می‌نویسند\\\" — the Persian lexicographical tradition itself gives Greek via Syriac/Aramaic.\"},\n   {\"src\":\"ARY\",\"where\":\"ARY_pages.txt, grep 'قرطاس'\",\"stance\":\"silent\",\"note\":\"Aryanpur's dictionary covers only inherited Indo-European material and has no entry.\"},\n   {\"src\":\"TAD\",\"where\":\"TAD_pages.txt leaf 58\",\"stance\":\"supports\",\"note\":\"Confirms the Arabic word Persian borrowed and its Greek pedigree.\"}\n ]\n})\n\nentry3[\"nodes\"].append({\n \"id\":3, \"lang\":\"Latin\", \"words\":\"carta, charta\", \"verdict\":\"confirmed\",\n \"derivation\":(\"Latin charta 'leaf of papyrus, sheet, document' is an early Latinised borrowing of Greek \"\n  \"χάρτης, attested from Cato onwards. Two changes are worth naming. The gender: the Greek word is masculine \"\n  \"in -ēs, but Latin made it feminine in -a on the model of its other Greek loans in -a — Ernout–Meillet cite \"\n  \"the ancient grammarian Charisius for exactly this rule, and note that Lucilius' masculine cartus (line 709) \"\n  \"was an isolated attempt to keep the Greek gender. The spelling: the aspirate is written ch- in the learned \"\n  \"form charta but Latin had no /x/, and the plain popular spelling carta — the form that all the Romance \"\n  \"languages continue — is the one that prevailed in Late Latin. Nourai's node gives both spellings, which is \"\n  \"correct.\"),\n \"derivation_fa\":(\"لاتینِ charta «برگ پاپیروس، ورق، سند» وام‌واژه‌ای است دیرین و لاتینی‌شده از χάρτης یونانی \"\n  \"که از کاتو به بعد گواهی شده است. دو دگرگونی را باید نام برد. نخست جنس دستوری: واژهٔ یونانی مذکر و پایان‌یافته \"\n  \"به ‑ēs است، اما لاتین آن را به قیاسِ دیگر وام‌واژه‌های یونانیِ ‑a مؤنث کرد — ارنو و مه‌یه همین قاعده را از \"\n  \"زبانِ دستورنویسِ باستان کاریسیوس نقل می‌کنند و می‌افزایند که صورتِ مذکرِ cartus نزد لوکیلیوس (بیت ۷۰۹) کوششی \"\n  \"تنها برای نگاه داشتنِ جنسِ یونانی بوده است. دوم املا: دمیدگی در صورتِ فاضلانهٔ charta با ch نوشته می‌شد، اما \"\n  \"لاتین آواى /x/ نداشت و املای سادهٔ عامیانهٔ carta — همان که همهٔ زبان‌های رومی دنبال کرده‌اند — در لاتینِ \"\n  \"متأخر چیره شد. نورایی هر دو املا را آورده و این درست است.\"),\n \"sources\":[W[\"ety_card\"], W[\"wik_khartes\"]],\n \"ref_check\":[\n   {\"ref\":\"KLN:239\",\"status\":\"supports\",\"note\":\"KLN_1966.txt leaf 136 (printed pp. 238/239), s.v. card: \\\"F. carte, fr. Late L. carta, 'a leaf of paper; paper', fr. L. charta, 'a leaf of the Egyptian papyrus; papyrus; paper', fr. Gk. χάρτης\\\" — both Latin spellings and the Greek source, on the cited page.\"},\n   {\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Online AHD s.v. card: Old French carte, from Medieval Latin carta, from Latin charta, from Greek khartēs. (Nourai gives no page for AHD here.)\"}\n ],\n \"consulted\":[\n   {\"src\":\"LAT\",\"where\":\"LAT.txt line 11590 ff., Ernout–Meillet s.v. c(h)arta\",\"stance\":\"supports\",\"note\":\"\\\"Emprunt ancien et latinisé du gr. χάρτης (–χάρτος), devenu féminin sous l'influence des autres thèmes en -a féminins; cf. coc(h)lea, etc. Le cartus de Lucilius 709 est une tentative isolée faite pour conserver le genre du nom grec. Cf. Charisius, GLK I 104, Varro ait uocabula ex Graeco sumpta, si suum genus non retineant, ex masculino in femineum transire … Panroman. M.L. 1866. Irl. cairt. Dérivés: chartaceus; chartarius … chartula … chartularius.\\\"\"},\n   {\"src\":\"KLN\",\"where\":\"leaf 136 = p. 239\",\"stance\":\"supports\",\"note\":\"See ref_check.\"},\n   {\"src\":\"SKT\",\"where\":\"SKT.txt leaf 520 region, s.v. Card (1)\",\"stance\":\"supports\",\"note\":\"\\\"Card (1), piece of pasteboard. (F. – ...) Corruption of F. carte … Low L. carta; L. [charta], leaf of paper\\\" — with cartel, cartoon, cartouche, cartridge, chartulary, chart and charter all referred back to it.\"}\n ]\n})\n\nentry3[\"nodes\"].append({\n \"id\":4, \"lang\":\"French\", \"words\":\"carte\", \"verdict\":\"confirmed\",\n \"derivation\":(\"French carte continues Late Latin carta by the ordinary sound history of the language: \"\n  \"intervocalic development is blocked because -rt- is a consonant cluster, so the stem survives intact, and \"\n  \"Latin final -a regularly weakens to French -e /ə/. It is attested from the 12th c. in the sense 'written \"\n  \"document' and from the 14th c. in the sense that mattered for its diffusion, 'playing card' — Klein and \"\n  \"Etymonline both note that the playing-card sense was the oldest in French too. Because French carte is a \"\n  \"popular inherited form rather than a learned one, it, and not Latin charta, is the shape that spread across \"\n  \"Europe and eventually into Persian (node #5).\"),\n \"derivation_fa\":(\"فرانسویِ carte دنبالهٔ مستقیمِ cartaی لاتینِ متأخر است بر پایهٔ تحول آواییِ عادیِ این زبان: \"\n  \"خوشهٔ همخوانیِ ‑rt‑ مانع نرم‌شدگیِ میان‌واکه‌ای می‌شود و ستاک دست‌نخورده می‌ماند، و ‑a پایانیِ لاتین به \"\n  \"قاعده به ‑e /ə/ فرانسوی سست می‌شود. این واژه از سدهٔ ۱۲ م. به معنای «سندِ نوشته» و از سدهٔ ۱۴ م. به همان \"\n  \"معنایی که سببِ پراکندگی‌اش شد، یعنی «ورقِ بازی»، گواهی شده است — کلاین و اتیمانلاین هر دو یادآور می‌شوند که \"\n  \"معنای «ورقِ بازی» در خودِ فرانسوی نیز کهن‌ترین معناست. و چون carte صورتی است عامیانه و ارثی، نه فاضلانه، \"\n  \"همین صورت — و نه chartaی لاتین — بود که در سراسر اروپا و سرانجام در فارسی پخش شد (گرهٔ ۵). ادعای نورایی \"\n  \"درست است.\"),\n \"sources\":[W[\"ety_card\"], W[\"ahd_charade\"]],\n \"ref_check\":[\n   {\"ref\":\"KLN:239\",\"status\":\"supports\",\"note\":\"KLN_1966.txt leaf 136 (printed pp. 238/239), s.v. card: \\\"— F. carte, fr. Late L. carta, 'a leaf of paper; paper'\\\" — Late Latin → French carte, on the cited page.\"}\n ],\n \"consulted\":[\n   {\"src\":\"KLN\",\"where\":\"leaf 136 = p. 239\",\"stance\":\"supports\",\"note\":\"See ref_check; Klein's cross-references (carte blanche, carte de visite, cartel, cartoon, cartouche, cartridge, cartulary, chart, charter, écarté, skat) map the whole French-mediated family.\"},\n   {\"src\":\"LAT\",\"where\":\"LAT.txt line 11597, Ernout–Meillet s.v. c(h)arta\",\"stance\":\"supports\",\"note\":\"\\\"Panroman. M.L. 1866\\\" — Meyer-Lübke no. 1866, i.e. the word survives in every Romance language, French carte included.\"},\n   {\"src\":\"SKT\",\"where\":\"SKT.txt leaf 520 region, s.v. Card (1) / carte\",\"stance\":\"supports\",\"note\":\"\\\"carte, a bill of fare … — Low L. carta; see Card above.\\\"\"}\n ]\n})\n\nentry3[\"nodes\"].append({\n \"id\":5, \"lang\":\"Persian\", \"words\":\"kârt\", \"verdict\":\"confirmed\",\n \"derivation\":(\"Persian کارت kārt 'card' is a 20th-century loan from French carte, entering with the \"\n  \"European administrative apparatus (کارت ویزیت 'visiting card', کارت شناسایی 'identity card', later کارت \"\n  \"ملی, کارت بانکی); Mo'in tags it [فر.] 'French'. French final -e /ə/ is not pronounced, so Persian took the \"\n  \"consonant-final stem kārt directly, with ā for the French /a/. The extra form in the box, کارتون kārton, is \"\n  \"the same borrowing pattern applied to French carton 'pasteboard' — itself French from Italian cartone, the \"\n  \"augmentative of carta — and in Persian it carries both senses, 'cardboard box' and 'animated cartoon'. \"\n  \"Together with قرطاس (node #2) this makes Greek χάρτης a doublet in Persian: the same word, once through \"\n  \"Aramaic and Arabic in the 10th century, once through Latin and French in the 20th.\"),\n \"derivation_fa\":(\"«کارت» فارسی وامی است از فرانسویِ carte در سدهٔ ۱۴ ش./۲۰ م. که همراه با دستگاه اداریِ \"\n  \"اروپایی وارد شد (کارت ویزیت، کارت شناسایی، و بعدها کارت ملی و کارت بانکی)؛ معین آن را با نشانهٔ [فر.] \"\n  \"می‌آورد. «ـe» پایانیِ فرانسوی تلفظ نمی‌شود، پس فارسی همان ستاکِ همخوان‌پایانِ kārt را گرفت، با «آ» در برابر \"\n  \"/a/ فرانسوی. صورتِ افزودهٔ همان جعبه، «کارتون»، همین الگوی وام‌گیری است دربارهٔ cartonِ فرانسوی «مقوا» — که \"\n  \"خود از cartone ایتالیایی، صورتِ بزرگ‌ساز (augmentative) از carta، آمده — و در فارسی هر دو معنای «جعبهٔ \"\n  \"مقوایی» و «فیلم پویانما» را دارد. این گره در کنار «قرطاس» (گرهٔ ۲) از χάρτης یونانی در فارسی یک دوگانه \"\n  \"(doublet) می‌سازد: یک واژه، یک‌بار در سدهٔ چهارم قمری از راه آرامی و عربی، و یک‌بار در سدهٔ چهاردهم شمسی از \"\n  \"راه لاتین و فرانسوی. ادعای نورایی درست است.\"),\n \"sources\":[W[\"ab_kart\"], W[\"ety_card\"]],\n \"ref_check\":[\n   {\"ref\":\"MON:2801\",\"status\":\"supports\",\"note\":\"Mo'in, Farhang-e Farsi s.v. کارت (read via abadis.ir): origin tag [ فر . ] (French), glossed as thin pasteboard on which the particulars of a thing or person are written, with the compounds کارت ویزیت, کارت شناسایی, کارت ملی. The [فر.] tag is exactly Nourai's French → Persian arrow.\"}\n ],\n \"consulted\":[\n   {\"src\":\"MON\",\"where\":\"s.v. کارت (abadis text of Farhang-e Mo'in)\",\"stance\":\"supports\",\"note\":\"\\\"[ فر . ] مقوای نازکی که مشخصات چیزی یا کسی را روی آن می‌نویسند\\\" — French origin, no Arabic or other intermediary. (abadis shows no separate کارتون entry from Mo'in.)\"},\n   {\"src\":\"KLN\",\"where\":\"KLN_1966.txt leaf 136 = p. 239 (card) and leaf 152 (carton, cartoon)\",\"stance\":\"supports\",\"note\":\"For the extra form: \\\"carton, n., a cardboard box. — F. See next word. cartoon, n., 1) a drawing on strong paper; 2) a comic strip. — F. carton, 'pasteboard', fr. It. cartone, augment. of carta, 'paper'. See card.\\\"\"},\n   {\"src\":\"ARY\",\"where\":\"ARY_pages.txt, grep 'کارت'\",\"stance\":\"silent\",\"note\":\"No entry; Aryanpur's dictionary treats only inherited Indo-European vocabulary, not modern French loans.\"}\n ]\n})\n\nentry3[\"nodes\"].append({\n \"id\":6, \"lang\":\"English\", \"words\":\"card, carton, cartoon, cartridge, chart\", \"verdict\":\"plausible\",\n \"derivation\":(\"All five are English via French from Latin charta, and Klein gathers exactly this list under \"\n  \"card — but not all five come from the specific French form carte, so the single arrow oversimplifies. \"\n  \"card (early 15th c.) is from Old French carte, with an unexplained -t > -d; the sense 'playing card' is the \"\n  \"oldest in both languages. chart (1570s) is from French charte 'map, card', the learned doublet of carte, \"\n  \"from Latin charta. carton and cartoon are both from French carton 'pasteboard', which is itself from \"\n  \"Italian cartone, the augmentative of carta — cartoon entered in the sense 'full-size drawing on stout \"\n  \"paper' (an artist's preparatory design) and acquired the comic sense in Punch in the 1840s. cartridge is a \"\n  \"corruption of earlier cartrage, from French cartouche 'a roll of paper', from Italian cartoccio, again from \"\n  \"carta; Klein's own entry heads it \\\"cartridge, n. — Fr. earlier cartrage, corruption of…\\\". So the node is \"\n  \"right that all five descend from Greek χάρτης through Latin and French, and right about card and chart in \"\n  \"particular; it is loose in routing carton, cartoon and cartridge through carte rather than through carton \"\n  \"and cartouche.\"),\n \"derivation_fa\":(\"هر پنج واژه از راه فرانسوی و از chartaی لاتین به انگلیسی رسیده‌اند و کلاین دقیقاً همین \"\n  \"فهرست را ذیل card گرد می‌آورد — اما هر پنج از صورتِ ویژهٔ carte نیامده‌اند و از این‌رو یک پیکانِ واحد \"\n  \"ساده‌سازی است. card (اوایل سدهٔ ۱۵ م.) از فرانسویِ کهنِ carte است با تبدیلِ توضیح‌نایافتهٔ ‑t به ‑d، و \"\n  \"معنای «ورقِ بازی» در هر دو زبان کهن‌ترین معناست. chart (دههٔ ۱۵۷۰ م.) از فرانسویِ charte «نقشه، ورق» است، \"\n  \"همان دوگانهٔ فاضلانهٔ carte از chartaی لاتین. carton و cartoon هر دو از فرانسویِ carton «مقوا»اند که خود از \"\n  \"cartone ایتالیایی، صورتِ بزرگ‌سازِ carta، آمده است — cartoon نخست به معنای «طرحِ تمام‌اندازه بر کاغذِ ستبر» \"\n  \"(طرحِ مقدماتیِ نقاش) وارد شد و معنای طنزآمیزش را در دههٔ ۱۸۴۰ م. در مجلهٔ پانچ یافت. cartridge دگرگون‌شدهٔ \"\n  \"cartrage است از فرانسویِ cartouche «طوماری از کاغذ»، از cartoccio ایتالیایی، باز هم از carta. پس گره در این \"\n  \"درست است که هر پنج واژه از χάρτης یونانی از راه لاتین و فرانسوی می‌آیند و دربارهٔ card و chart به‌ویژه \"\n  \"دقیق است؛ اما در گذراندنِ carton و cartoon و cartridge از carte به‌جای carton و cartouche بی‌دقتی کرده \"\n  \"است. با احتیاط پذیرفتنی است.\"),\n \"sources\":[W[\"ety_card\"], W[\"wik_khartes\"]],\n \"ref_check\":[\n   {\"ref\":\"KLN\",\"status\":\"supports\",\"note\":\"KLN_1966.txt leaf 136 (printed p. 239), s.v. card, closes: \\\"Cp. carte blanche, carte de visite, cartel, cartoon, cartouche, cartridge, cartulary, chart, charter, écarté, skat.\\\" — Klein groups Nourai's five words (and more) under the one Greek etymon, though his separate entries give each its own French donor: leaf 152 \\\"carton, n., a cardboard box. — F. See next word. cartoon, n. … — F. carton, 'pasteboard', fr. It. cartone, augment. of carta\\\"; \\\"cartouche, n. … — F., fr. It. cartoccio, lit. 'a roll of paper', fr. carta\\\"; and line 6632 \\\"cartridge, n. — Fr. earlier cartrage, corruption of [cartouche]\\\". Nourai gives no page number for KLN in this box.\"},\n   {\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Online AHD s.v. card: Old French carte < Medieval Latin carta < Latin charta < Greek khartēs. Nourai gives no page number.\"}\n ],\n \"consulted\":[\n   {\"src\":\"KLN\",\"where\":\"leaf 136 = p. 239 (card); leaf 152 (carton, cartoon, cartouche); line 6632 (cartridge)\",\"stance\":\"partial\",\"note\":\"Supports the common origin but routes carton/cartoon through F. carton < It. cartone, and cartridge through cartouche < It. cartoccio — not through carte.\"},\n   {\"src\":\"SKT\",\"where\":\"SKT.txt leaf 520 region, s.vv. Card (1), cartel, cartoon, cartouche, cartridge, chart, charter, chartulary\",\"stance\":\"partial\",\"note\":\"Skeat likewise files all of them under Card: \\\"cartoon … Ital. cartone, lit. a large paper\\\"; \\\"cartouche, cartridge … a roll of paper\\\"; \\\"chart … L. charta, a paper\\\" — same family, different immediate French/Italian donors.\"},\n   {\"src\":\"AHD\",\"where\":\"online AHD s.v. card\",\"stance\":\"supports\",\"note\":\"Greek khartēs → Latin charta → Medieval Latin carta → Old French carte → English card.\"}\n ]\n})\n\nout = {\n \"pdf_page\": 104,\n \"book_page\": 74,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [entry0, entry2, entry3]\n}\n\np = \"/home/sfmqrb/git/rishe/data/verification/page-104.json\"\nwith open(p, \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"wrote\", p)\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk104.py",
 "description": "Write page-104.json"
}
```


### [2026-09-05T17:30:07.260Z] TOOL RESULT

```
wrote /home/sfmqrb/git/rishe/data/verification/page-104.json
```


## [2026-09-05T17:30:11.163Z] TOOL CALL #69: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-104.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 104",
 "description": "Validate JSON and run verify_check"
}
```


### [2026-09-05T17:30:13.353Z] TOOL RESULT

```
JSON OK
nodes verified: 17/17
node verdicts: {'confirmed': 11, 'transcription_suspect': 2, 'disputed': 1, 'plausible': 3}
root verdicts: {'confirmed': 2, 'disputed': 1}
ref checks: {'supports': 14, 'not_checked': 6, 'partial': 4}
books consulted: {'supports': 37, 'partial': 15, 'silent': 6, 'contradicts': 2} | by book: {'KLN': 13, 'AHD': 8, 'SKT': 6, 'FSD': 5, 'MON': 4, 'HJB': 4, 'ARY': 4, 'WEB': 4, 'LKT': 3, 'BQT': 2, 'TAD': 2, 'LAT': 2, 'AFM': 1, 'ARB': 1, 'FVQ': 1}
```


## [2026-09-05T17:30:16.868Z] TOOL CALL #70: Bash

```json
{
 "command": "ls -la data/verification/sources/refs/ocr/BOOK/104.png && git -C /home/sfmqrb/git/rishe status --short | head -20",
 "description": "Confirm artifacts"
}
```


### [2026-09-05T17:30:18.868Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 78826 Sep  5 10:59 data/verification/sources/refs/ocr/BOOK/104.png
 M data/verification/sources/web/index.jsonl
?? data/verification/page-104.json
?? data/verification/sources/web/651164bf608d9841.txt
?? data/verification/sources/web/b0d1e89d8f080549.txt
?? data/verification/sources/web/bcecc17eaa4b1885.txt
?? data/verification/sources/web/f8da4bf6b856d076.txt
?? data/verification/sources/web/ff55c7ac46891403.txt
```


## [2026-09-05T17:30:30.371Z] TOOL CALL #71: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json\nurls=[\"https://www.etymonline.com/word/tea\",\"https://en.wiktionary.org/wiki/چای\",\"https://www.ahdictionary.com/word/search.html?q=tea\",\"https://abadis.ir/fatofa/چای/\",\"https://www.etymonline.com/word/charlatan\",\"https://www.etymonline.com/word/charade\",\"https://www.ahdictionary.com/word/search.html?q=charlatan\",\"https://www.ahdictionary.com/word/search.html?q=charade\",\"https://abadis.ir/fatofa/شارلاتان/\",\"https://en.wiktionary.org/wiki/χάρτης\",\"https://en.wiktionary.org/wiki/قرطاس\",\"https://abadis.ir/fatofa/قرطاس/\",\"https://abadis.ir/fatofa/کارت/\",\"https://www.etymonline.com/word/card\"]\nidx=set()\nfor line in open('data/verification/sources/web/index.jsonl',encoding='utf-8'):\n    try: idx.add(json.loads(line).get('url'))\n    except Exception: pass\nfor u in urls:\n    print('OK ' if u in idx else 'MISSING ', u)\nEOF",
 "description": "Verify archived URLs in index"
}
```


### [2026-09-05T17:30:32.418Z] TOOL RESULT

```
OK  https://www.etymonline.com/word/tea
OK  https://en.wiktionary.org/wiki/چای
OK  https://www.ahdictionary.com/word/search.html?q=tea
OK  https://abadis.ir/fatofa/چای/
OK  https://www.etymonline.com/word/charlatan
OK  https://www.etymonline.com/word/charade
OK  https://www.ahdictionary.com/word/search.html?q=charlatan
OK  https://www.ahdictionary.com/word/search.html?q=charade
OK  https://abadis.ir/fatofa/شارلاتان/
OK  https://en.wiktionary.org/wiki/χάρτης
OK  https://en.wiktionary.org/wiki/قرطاس
OK  https://abadis.ir/fatofa/قرطاس/
OK  https://abadis.ir/fatofa/کارت/
OK  https://www.etymonline.com/word/card
```


## [2026-09-05T17:30:52.918Z] AGENT

Page 104 (book p. 74) done. `verify_check.py 104`: 17/17 nodes, **0 PROBLEM lines**.

**Verdicts** — roots: 2 confirmed, 1 disputed. Nodes: 11 confirmed, 3 plausible, 1 disputed, 2 transcription_suspect. Ref checks: 14 supports, 4 partial, 6 not_checked. 15 different local books consulted (60 entries).

**Disputed**
- ROOT `Čar, Char` "idle chat" [Indo-European] — not a reconstructible PIE root: absent from Pokorny, Walde-Pokorny and Watkins/AHD; Klein, AHD and Etymonline all call the Romance chatter verbs (It. *ciarlare*, Sp. *charlar*, Occ. *charrar*) independent onomatopoeias. Nourai's only source, Shipley OEW:51, is lending-only and could not be checked.
- `#1 Cerreto; Cerretano; ciarlatano` — *Cerreto* is a toponym from Latin *cerrētum* "oak grove" (< *cerrus*), not from a "chat" root, so the root→Cerreto arrow is wrong. The *cerretano* → *ciarlatano* half is fine (AHD:227 and Klein p. 268 confirm it verbatim); Etymonline/OED prefer *ciarla* directly.

**Transcription_suspect (both `error_in: book` — extraction is faithful)**
- `#2 [Chinese] t'a` (entry 0) — no Chinese form *t'a* exists; the Amoy/Southern-Min reading is *tê* (Wade-Giles t'e). Klein p. 1578, Nourai's own citation, prints "te"; AHD, Skeat, Lokotsch and Hobson-Jobson likewise. Page rendered at 600 dpi: the book itself prints "t'a".
- `#3 [Persian] čârlâtân` (entry 2) — Persian شارلاتان is *šārlātān*, a French loan ([فر.] in both Mo'in and Dehkhoda); *č* contradicts the ش in Nourai's own box. Page image confirms the book prints "čârlâtân".

**Plausible**
- entry 3 `#1 Arabic qirṭās` — from Greek χάρτης but via Aramaic/Syriac *qarṭīsā* (q- for kh-, -ās for -ēs); Nourai's direct Greek→Arabic arrow skips a step.
- entry 2 `#5 charra/charrado` — Provençal (Occitan), not French, as AHD:228 itself says; and *charrado* means "chat", not "a game of phrases".
- entry 3 `#6 card, carton, cartoon, cartridge, chart` — all from Latin *charta* via French, but *carton/cartoon* come from Fr. *carton* < It. *cartone* and *cartridge* from Fr. *cartouche* < It. *cartoccio*, not from *carte*.

**No extraction errors** — the JSON matches the printed page everywhere, including the two bad forms above.

Notable positives: Klein's cited page numbers check out exactly (leaf 836 carries printed pp. 1578/79 for *tea*; leaf 136 carries pp. 238/39 for *card*), TAD:55 has the قرطاس entry ("يوناني … مرادفه ورقة وصحيفة"), and Mo'in's origin tags confirm چای ("مأخوذ از چینی"), قرطاس ([ع.]) and کارت ([فر.]). Not checkable: OEW, SHP, PRT, VOP (no copy anywhere) and VDQ (noorlib is JS-only; FVQ's entry body is lost in the OCR).

Page image saved to `/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/104.png`; all 14 web sources archived and indexed.
