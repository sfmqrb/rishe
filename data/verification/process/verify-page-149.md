# Verification process log — verify-page-149


## [2026-09-05T20:21:39.422Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 149 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-149.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-149.json. Write /home/sfmqrb/git/rishe/data/verification/page-149.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 149` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:21:40.769Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:21:41.487Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:21:41.500Z] TOOL RESULT

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


## [2026-09-05T20:21:42.036Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-149.txt"
}
```


### [2026-09-05T20:21:42.052Z] TOOL RESULT

```
1	=== PDF page 149 (book page 119) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ei, Ey, I 1, Iâ 1 : to go  (refs POK:293,501; KLN:825)  PART 2
4	#1 (parent #0) [Greek] refs=AHD | ieani : to go ; ion 2 : going particle
5	  #2 (parent #1) [French] refs=None | 
6	    #3 (parent #2) [Persian] refs=None | yon «یون» : ion
7	  #4 (parent #1) [English] refs=AHD | ion
8	#5 (parent #0) [Indo-European] refs=POK:296; KLN:1761 | Yě, Yero : year ; Iě, Iěro, Iaro : year
9	  #6 (parent #5) [Avestan] refs=POK:296; KLN:1796 | yâr, yâra : year ; yâh 2, jâr, jaiti : year
10	    #7 (parent #6) [Pahlavi] refs=HRN:249 | yâirka : one year old.
11	      #8 (parent #7) [Persian] refs=BQT:2406 | hîrak «هیرک» : a baby animal
12	  #9 (parent #5) [Latin] refs=AHD | yâ-mo : beginning of year, god of doors
13	    #10 (parent #9) [French] refs=None | Janiver : January
14	      #11 (parent #10) [Persian] refs=MON:1775 | Žânvîyeh «ژانویه» : January
15	    #12 (parent #9) [English] refs=None | January, janitor
16	  #13 (parent #5) [Germanic] refs=AHD | yěram, jěram : year
17	    #14 (parent #13) [English] refs=None | year
18	  #15 (parent #5) [Greek] refs=AHD | hôros : time ; hôrâ : season
19	    #16 (parent #15) [English] refs=None | hour, horoscope
20	#17 (parent #0) [Indo-European] refs=KLN:1743 | Wi-itos : to go (gone) apart, wide ☞Wi
21	  #18 (parent #17) [Germanic] refs=None | wît, wîdaz : wide
22	    #19 (parent #18) [English] refs=None | wide
23	--- entry 1 ---
24	ROOT Ĕik -> redirect to Aik
25	--- entry 2 ---
26	ROOT [Indo-European] Eis 1 : passion  (refs POK:299)
27	#1 (parent #0) [Avestan] refs=POK:299; BQT:754 | aes-ma, aěš-ma : anger
28	  #2 (parent #1) [Persian] refs=HRN:109 | xešm (xašm) «خشم» : anger
29	#3 (parent #0) [Germanic] refs=AHD | is-areno : holy metal
30	  #4 (parent #3) [English] refs=None | iron
31	
```


## [2026-09-05T20:21:44.906Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-149.json",
 "description": "Read page 149 source JSON"
}
```


### [2026-09-05T20:21:44.941Z] TOOL RESULT

```
{
  "pdf_page": 149,
  "book_page": 119,
  "entries": [
    {
      "root": {
        "name": "Ei, Ey, I 1, Iâ 1",
        "lang": "Indo-European",
        "refs": "POK:293,501; KLN:825",
        "gloss": "to go"
      },
      "part": 2,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "ieani", "gloss": "to go", "script": null},
            {"translit": "ion 2", "gloss": "going particle", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "French",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": null,
          "words": [
            {"translit": "yon", "gloss": "ion", "script": "یون"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "ion", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Indo-European",
          "refs": "POK:296; KLN:1761",
          "words": [
            {"translit": "Yě, Yero", "gloss": "year", "script": null},
            {"translit": "Iě, Iěro, Iaro", "gloss": "year", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Avestan",
          "refs": "POK:296; KLN:1796",
          "words": [
            {"translit": "yâr, yâra", "gloss": "year", "script": null},
            {"translit": "yâh 2, jâr, jaiti", "gloss": "year", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Pahlavi",
          "refs": "HRN:249",
          "words": [
            {"translit": "yâirka", "gloss": "one year old.", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "BQT:2406",
          "words": [
            {"translit": "hîrak", "gloss": "a baby animal", "script": "هیرک"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 5,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "yâ-mo", "gloss": "beginning of year, god of doors", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "Janiver", "gloss": "January", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Persian",
          "refs": "MON:1775",
          "words": [
            {"translit": "Žânvîyeh", "gloss": "January", "script": "ژانویه"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 9,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "January, janitor", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 5,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "yěram, jěram", "gloss": "year", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "year", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 5,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "hôros", "gloss": "time", "script": null},
            {"translit": "hôrâ", "gloss": "season", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "hour, horoscope", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 0,
          "lang": "Indo-European",
          "refs": "KLN:1743",
          "words": [
            {"translit": "Wi-itos", "gloss": "to go (gone) apart, wide", "script": null, "see": ["Wi"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 17,
          "lang": "Germanic",
          "refs": null,
          "words": [
            {"translit": "wît, wîdaz", "gloss": "wide", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 19,
          "parent": 18,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "wide", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Ĕik",
        "redirect": "Aik"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Eis 1",
        "lang": "Indo-European",
        "refs": "POK:299",
        "gloss": "passion"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:299; BQT:754",
          "words": [
            {"translit": "aes-ma, aěš-ma", "gloss": "anger", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:109",
          "words": [
            {"translit": "xešm (xašm)", "gloss": "anger", "script": "خشم"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "is-areno", "gloss": "holy metal", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "iron", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-05T20:21:46.026Z] TOOL CALL #4: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/ | head -50; echo ---; ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ | head -80",
 "description": "List verification dir and refs"
}
```


### [2026-09-05T20:21:46.074Z] TOOL RESULT

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
page-129.json
page-146.json
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
---
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
```


## [2026-09-05T20:21:49.909Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n 1,80p tools/verify_check.py",
 "description": "Read verify_check tool"
}
```


### [2026-09-05T20:21:49.947Z] TOOL RESULT

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


## [2026-09-05T20:21:50.920Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-127.json'))\nprint(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:3000])\n\"",
 "description": "Sample existing verification file"
}
```


### [2026-09-05T20:21:52.821Z] TOOL RESULT

```
{
 "entry": 0,
 "root": "Dhem",
 "verdict": "confirmed",
 "modern_form": "PIE *dʰemH- (LIV² *dʰmeh₁-) 'to blow, breathe; to smoke, raise dust'",
 "note": "Pokorny IEW 247-248 heads the entry 'dhem-, dhemə- \"stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben = düster, dunkel), wehen, blasen (hauchen = riechen)\"', so Nourai's language label (Indo-European) and his gloss 'to make vapor, raise dust' are an accurate short rendering of the German. Cheung (Etym. Dict. of the Iranian Verb, *damH³) writes the same root «PIE *dʰmeH- 'to blow' = LIV: 153 | Pok.: 247 f.»; Wiktionary reconstructs *dʰemH-. Watkins/AHD carries no dhem- root (its list goes dhembh- → dhen-¹), simply because no English word reaches it through Latin or Greek, so its silence is not a disagreement. Two weak spots in the chart: the Avestan node's gloss (node 1) and the name Damāvand (node 2), which Nourai's own source BQT:878 derives from a different root.",
 "note_fa": "ریشهٔ نمودار همان ریشهٔ هندواروپاییِ آغازینِ *dʰemH- «دمیدن، فوت کردن؛ دود و بخار برخاستن» است. پوکورنی در صفحهٔ ۲۴۷ کتاب خود آن را با معنای آلمانیِ «stieben, rauchen … wehen, blasen» آورده و برگردانِ کوتاهِ نورایی («بخار ساختن، گرد برانگیختن») با آن می‌خواند؛ چونگ نیز همین ریشه را *dʰmeH- «دمیدن» (LIV ۱۵۳) می‌نویسد. پس جعبهٔ ریشه، برچسبِ زبان و معنای آن درست است و ادعای نورایی در این حد پذیرفتنی است. تنها دو نقطهٔ سست در نمودار هست: معنایی که برای صورتِ اوستایی داده شده (گرهٔ ۱) و نامِ «دماوند» (گرهٔ ۲) که خودِ مأخذِ نورایی، یعنی حاشیهٔ معین بر برهان قاطع ص ۸۷۸، آن را از ریشهٔ دیگری می‌گیرد.",
 "sources": [
  "https://en.wiktionary.org/wiki/%D8%AF%D9%85%DB%8C%D8%AF%D9%86",
  "https://en.wiktionary.org/wiki/%D8%AF%D9%85"
 ],
 "ref_check": [
  {
   "ref": "POK:247",
   "status": "supports",
   "note": "POK_01.txt (grep -n 'dbem-' → line 3513), IEW p.247: 'dbem-, dhemo- ,stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben == düster, dunkel), wehen, blasen (hauchen = riechen)'; the page continues 'Ai. dhámati ,bläst', av. daδmainya- …, npers. damīdan ,blasen, wehen', dam ,Atem, Atemzug''. Exactly the root box as drawn."
  }
 ],
 "consulted": [
  {
   "src": "WLD",
   "where": "Bd. I 851 f. (WLD_Bd1 djvu line 53642)",
   "stance": "supports",
   "note": "'dhem-, dhemə- „stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben = düster, dunkel), wehen, blasen (hauchen = riechen)“. Bedeutungsumfang wie bei Wz. *dheu- „stieben“.' — the source Pokorny 247 abridges."
  },
  {
   "src": "CHEUNG",
   "where": "s.v. *damH³ (CHEUNG.txt line 4670 ff.)",
   "stance": "supports",
   "note": "'*damH³ \"to blow, breathe; to swell\" … «PIE *dʰmeH- \"to blow\" > LIV: 153 | Pok.: 247 f.»'"
  },
  {
   "src": "AHD",
   "where": "Watkins 1985, d-list (AHD_watkins1985.txt line 377)",
   "stance": "silent",
   "note": "the appendix runs 'dhembh-. To bury. … [Pok. (dhembh-), dhmbh- 248.] dhen-¹. To run, flow.' — no dhem- entry at all, since no English word descends from it via Latin/Greek."
  },
  {
   "src": "IEC",
```


## [2026-09-05T20:22:25.739Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources; python3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nfor k in ['POK','KLN','AHD','HRN','HUB','BQT','MON','BRT','PHD','NYB','WLD','IEC','SYN','ARY','CHEUNG','SKT','WEB','FSD','LKT']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400] if v else 'MISSING')\n\"",
 "description": "Inspect refs_online for relevant abbrevs"
}
```


## [2026-09-05T20:22:26.406Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"i̯ēr-\\|i̯er-\\|Jahr\\b\" POK_01.txt | head -30",
 "description": "Grep Pokorny for year root"
}
```


### [2026-09-05T20:22:27.906Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
CHEUNG MISSING
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
```


### [2026-09-05T20:22:27.961Z] TOOL RESULT

```
340:Lat.  uls  jenseits^  *ulter,  -tra,  -trum  .jenseitig'  (ultrö,  ultra),  Komp. ulterior,  Sup.  ultimiis  =  osk.  ültiumam  .ultimam'^ ;  alat.  ollus  .ille'  (*ol-no-s, vgl.  unten  ir.  ind-oll  und  slav.  "^olni),  jünger  olle,  olll  .tunc'.  olllc  ,i\\i&'^ dehnstufig  ölim  .einst'  (wohl  nach  im,  exim  umgestaltetes  und  mit  ai. par-äri  ,\m  drittletzten  Jahr'  [vgl.  TtSQ-vai]  gleichzusetzendes  *öl{,  Loka- tivadverb, auf  das  auch  die  Glossen  olitana  .vetusta'.  olitinata  .veterata. antiqua'  —  ö  oder  Ö?  —  zurückweisen  können),  umbr.  ulo,  ulu  .illo.  illuc'; durch  Einfluß  von  is,  iste  usw.  wurde  ollus,  olle  zu  ille  umgefärbt.
341:Slav.  *olni  (idg.  *oln-ei)  =  aksl.  lani,  cech.  loni,  poln.  loni  .im  vorigen Sommer,  im  vorigen  Jahre'  (.in  jenem  Jahr',  vgl.  lat.  olll  .tunc').
925:at'  »gehen,   Jahr^
926:Ai.  dtati  ,geht,  wanderte  Hierzu  lat.  annus , Jahr' aus  *atnos  =  got.  Dat.  PL itpnam  ,Jahr^  Vgl.  Fick  I^  338,  W.  Meyer  KZ.  28,  164,  Froehde  BB.  16, 196  f.  (Bedeutungsentwicklung  wie  hei  germ.  '^jeram  ,Jahr^  zu  ie-  ,gehen'').
927:Osk.-umhr.  entspricht  akno-  ,Jahr,  Festzeit,  Opferzeit'  (mit  -tn-  zu  -kn-, Brugmann  IF.  17,  492).  Erhalten  ist  das  "Wort  in  den  Kompositis  lat. perennis  ,das  ganze  Jahr  dauernd;  beständig',  sollennis  , alljährlich  wieder- kehrend oder  gefeiert,  feierlich;  üblich'  (Nebenform  sollemnis  sicherlich analogisch  entstanden;  Thurneysen  AflL.  13,  23 ff.,  nach  omnis?)]  umbr. sev-acni-,  'per-acni-  , sollennis',  Subst.  ,hostia'.
965:Gr.  lavo)  ,scblafe^  aus  redupl.  "^i-ausö,  Aor.  i-avaai,  woneben  unredupl. Aor.  Usaa,  Inf.  äfea{o)ai]  avXtg,  -löog  , Aufenthaltsort,  Lager,  Stall,  Nacht- -  lager^,  avUlop^ai  ,bin  im  Hofe,  übernachte',  äygavXog  ,im  Freien  übernach- tend^, aiUj  ,Hof,  Wohnung^  (ursprüngl.  wohl  ,der  eingezäunte  Raum  ums Haus,  in  dem  das  Vieh  für  die  Nachtzeit  zusammengetrieben  wird');  von lavco  stammt  außer  lavd-i-iög  ,Nachtlager^,  ^r]?uavd^iA,6g  ,Schafstall^,  iviavd- (.lög  , Aufenthaltsort'  (:  hom.  inavstv  ,sein  Ruhequartier  haben')  auch  gr. Eviavxog  eigentlich  ,Rast,  Ruhestation',  daher  die  Sonnenwenden  als  Ruhe- stationen im  Sonnenlauf  {solstitium)^  dann  .Jahr,  Jahrestag'  (anders  Specht Idg.  Dekl.  15,  Schwjzer  Gr.  Gr.  l,  424^,  s.  auch  en-  ,Jahr').
1101:4.  Erweiterung  uer-s-  ^Regen^  Tau'^:  ai.  varsd-  n.  fliegen,  Regenzeit^ Jahr^  {varsati  ,es  regnet*^);  gr.  odoov  ^Harn^;  egar],  eegar]  ^Tau^^  ion.  att. ovoeo)  ;harne^  (kausativ  *uorse{ö,  f-  erwiesen  durch  die  Augmentierung ioÜQrjaa),  ovqla  ,Qm  WasservogeF;  rniv.  frass  ^Regen^  ist  älter  fross  (uros-tCij trotz  Pedersen  KG.  I  44);  hett.  iva-ar-sa-as  ;Regen'^(?)  scheint  ai.  Lw.
3430:lett.  deju,  det  ,saugen',  at-diene,  at-diemte  ,eine  Kuh,  welche  im  zweite] Jahr  kalbt',  lit.  dieni  f.  ,trächtig'  (=  ai.  dhenü-),  dienä  ds.  (=  ai.  dhenä  ,Kuh*3 apr.  dadan  , Milch'  (=  ai.  dadJian-)]  aksl.  dojg  ,säuge'  (ai.  dhdyati),  doilicQ ,Amme',  mit  e  (=  idg.  e  oder  9i)  däth  f.  ,Kinder',  deva,  devica  ,Määchen Jungfrau'  (verschoben   aus   ,*Weib'  =  ,die  säugende',    s.  Berneker  197);
4297:ie-  in  iero-  :  iöro-  :  lorO'  ,Jahr,  Sommer'  :
4298:ai.  paryärinl-  (pari-yärim-)  ,nach  einem  Jahr  erst  kalbend*  (?);
4299:av.  yärd  n.   ,Jahr*;
4300:gr.  cüQa  jjahreszeit,  Tageszeit,  Stunde,  rechte   Zeit',   a>Qog  ,Zeit,  Jahr*;
4304:oot.  jer,  anord.  är,  ags.  geär,  as.  ahd.  jär  n.  ,Jahr';
4627:Gr.  evog  ,Jahr'  Hes.,  unsicher,  ob  m.  oder  n.,  dl-evog  , zweijährig*,  rer^a-  " Evrjg,  -sg  ,  vier  jährig*,  hom.  Akk.  Sg.  '^vlv,  Akk.  PI.  iv'ijg  ,  jährig*,  TtgrjT-rjy , einjähriges  Lamm*  (zu  dor.  nqäxog  aus  *p.r^os?);  h-LavTÖg  ,Jahr'  (zu laveiv:  ,wenn   das  Jahr  ruht,  Jahreswende*??).  ^»y-
4632:Specht  Dekl.  16  stellt  dazu  das  Pron.  en  in  gr.  evrj  , jener  (Tag  oder jenes  Jahr*?).
4873:in  apr.  eristian  ,Lämmchen',  lit.  {j)erasj  lett.  jers  ,Lamm^,  litt,  mend  ^ , Lammfleisch'  =  russ.-ksl.  jarina  ,Wolle',  usw.,  sind  wohl  bsl.  *eTO': ,Bock'  und  *jörä-  ,Jahr'  (s.  oben  S.  297)  vermischt  worden;
```


## [2026-09-05T20:22:35.527Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '4280,4320p' POK_01.txt",
 "description": "Pokorny year root context"
}
```


### [2026-09-05T20:22:35.567Z] TOOL RESULT

```
f
Art,  böse*;  ahd.  ewa  (*omä)  f.  , Gesetz,  Norm,  Bündnis,   Ehe',  as.  eu m.,  ags.  cewj  cb  f.  , Gesetz,  heiliger  Brauch,  Ehe*  (für   Gleichheit  mit  tu .    , Ewigkeit'  plädiert  Weigand-Hirt  s.  v.);  vgl.  auch  got.  haüca  ,wie*  (wgq aus  *quömos  aus  *quo-oiuos]  so  auch  gr.  Ttotog  u.  dgl.  ?,  s.  unter  quo) -
e-stufig  lit.  pereiva^  pereivis  , Landstreicher*,  nach  Specht  KZ.  65,  4^ aus  einem  Adj.  *ejil$,  zu  ved.  upäyü-  ,herankommend'.
/-Bildung  wahrscheinlich  im  Intensivum  as.  llian^  ahd.  lllan  , eilen,  sich beeifern*  (aus  HjUian]  *eieliöy  Bildung  wie  lat.  sepeliö)-^  allenfalls,  doch sehr  unsicher,  norw.  dial.  eil  f.  ,rinnenförmige  Yertiefung',  schwed.  dial ela  ds.,  lit.  eiU  ,Reihe,  Furche*,  lett.  ailis  ,Fach,  Reihe'.
^^-Erweiterung  in :
arm.   ej  »Abstieg*,   ijanem   (Aor.  ej)  »herabsteigen*,    ijavank"   PI.  ^Qas haus*,  ijavor  ,Gast*;  "\
gr.  iiyfßxai'  ol/firat  Hes.,  c)i%0[iai  ,gehe  (fort),  bin  fort*,  olyyiia  ,geb3 komme*,  vielleicht  auch  l'/vog,  X-jiyiov  , Fußspur*  (als  , Tritt*);
air.  öegi^  Gen.  -ed  ,Gast*;
lit.  eigh  f.  ,Gang*.  ^
ai.  yäti  ,geht,  fährt*,  av.  yäiti  ds.,  ai.  yäna-h  m.  ,Bahn',  n.  ,Gang  ,VehikelY" av.  yäh-  n.  ,Krise,  Entscheidung*  (s-St.);  »j»^
gr.  'Ert-laaaa  jiTtiovaa^  (mit  -?^^Suffix),  Beiname  der  Demeter  (:  ai.  yati ,die  gehende*);  ^^^
lat.  Jänus  ,altital.  Gott  der  Türen  und  des  Jahresanfangs*,  jänua  ,Türö*;^
air.  ä  , Achse,  Wagen*  (idg.  *i^),  äth  ,Furt*  {^iä-tu-s)  brit.  Zubehör  ver mutet  Pedersen  KG.  1  322 f.);  ;
lit.  jöju^  jöHj  lett.  jäju,  jdt  , reiten*,  lit.  jodyti  , fortgesetzt  reiten*;
2ik.s\.  jadg^  jachati  (s-Erw.  *iä-s-)  , fahren,  vehi*,  Part.  Pass.  prä-javi^jazda ,das  Fahren,  Reiten*,  jato  ,agmen*  (s.  zu  den  slav.  Formen  Berneker  441  f., V.  d.  Osten-Sacken  IF.  33,  205,  Brückner  KZ.  45,  52,  Persson  Beitr.  348  f.); dazu  die  slav.  FIN  Jana  (Nowgorod),   Janka   (Wilna),  Jana  (Bulgarien),  -i nhd.  Jahna  (Sachsen);  s.  Rozwadowski  RSl.  6,  64.
Vielleicht  auch  hierher  lett.  Jänis  (mit  dem  christl.  Johannes  zusammen- geworfen) als  Beherrscher  der  Himmelspforte;  vgl.  darüber  E.  Fraenkel Balt.  Sprachwiss.  134 ;
toch.  A  yä  ,er  ging*,  B  yatsi  , gehen*,  mit  jp-Erw.  yopsa  ,er  trat  ein*, usw.  (Pedersen  Toch.  231);  vgl.  ai.  yäpdyati  ,läßt  gelangen  zu'.
ie-  in  iero-  :  iöro-  :  lorO'  ,Jahr,  Sommer'  :
ai.  paryärinl-  (pari-yärim-)  ,nach  einem  Jahr  erst  kalbend*  (?);
av.  yärd  n.   ,Jahr*;
gr.  cüQa  jjahreszeit,  Tageszeit,  Stunde,  rechte   Zeit',   a>Qog  ,Zeit,  Jahr*;
297
vielleicht  lat.  hörnus  ,heurigS  wenn  auf  *höiörö  ,in  diesem  Jahre*  he- i-uhend,  vgl-  ahd.  hiuru  , heuer*  aus  *hiu  järu]
urkelt.  *iarä  (^iora),  cymr.  bret.  lar  ,HenneS  gall.  PN  larilla,  mir.  eir-ln Huhn'  (air.  *«iV-m);  falsch  O'Rahilly  Eriu  13,  148  f.;
oot.  jer,  anord.  är,  ags.  geär,  as.  ahd.  jär  n.  ,Jahr';
russ.-ksl.  jara  , Frühling*,  russ.  jarb  , Sommerkorn'  (usw.,  s.  Berneker 446,  davon  Ableitungen  für  einjährige  Tiere,  z.  B.  russ.  jdrec  ,ein jähriger Biber',  j^^^«  , Schaflamm',  hxxig.  jdrka  Junges  Huhn');
dagegen  gewiß  hierher  m\id.  jän  , Reihe,  Gang',  nhd.  Ja /m  , Gang,  Reihe o-emähten  Getreides',  schwed.  mundartl.  an  ds. ""  WP.  I  102 ff.,  WH.  I  406 ff.,  658 f.,  668f.,  723,  Schwyzer  Gr.  Gr.  I  674.
2.  ^i  Ausrufpartikel.
Ai.  e  , Ausruf   der  Anrede,   des   Sichbesinnens'    usw.;    ai   ds.,    ayi  vor dem  Vokativ; av.  äi  vor  dem  Vokativ;  können  auch  zu  az,  oben  S.  10,  gehören; gr.  sia  {*eif -{•  a)  , wohlan!'  (daneben  ehv)-^ lat.  eij  hei  ,ach!'  davon,  eiulö  ,schreie  auf,  oi-ei  ,oh  weh!'; air.  (h)e  , Ausruf  der  Freude  und  des  Schmerzes'; ahd.  l'j  mhd.  nhd.  ei  sind  daraus  nicht  lautlich  entwickelt; lit.  el  , Ausruf  der  Warnung',  lett.  ei  ,heil'; skr.  ej,  poln.  russ.  ej  ,ei!'. WH.  I  396  f.,  Trautmann  67.
j.  ei-  Farbadjektiv  , rötlich,  bunt',  erweitert  (e)i-uo-,  (e)i-uä  ,Eibe'  usw.; nur  indisch:  ei-to-  ,bunt',  fem.  ei-m,  von  bunten  Tieren.
Arm.  aigi  , Weinstock'  (*oiui{a) ;
gr.  OLTjj  b'r],  oa  , Sperberbaum,  Vogelbeerbaum'  (*oiuä)  =
lat.  üva  ,Traube';
gall.  ivo-,  urir.  ma-,  air.  eo  m.,  cymr.  ywen  m.,  acorn.  hiuiiij  bret.  ivin m.  ,Eibe';
ahd.  iiüa,  mhd.  Iwe,  mnl.  ijf^  nhd.  Eibe  f.,  ags.  lio  m.,  aisl.  yr  ,Eibe' (*emo-),  nach  dem  rotbraunen  Holz  benannt;
daneben  *ei-ko-  in  ahd.  Igo,  as.  PL  IchaSj  Schweiz,  iche,  Ige^  ags.  l/i, eo/i  ,Eibe';
lit.  ievä,  jievä  f.,  lett.  (mit  abweichender  Intonation)  ieoa  ,Faulbaum* (*emä),  apr.  luivis  ,Eibe'  (*ma-),   nach  dem  rotbraunen  Holz  benannt;
russ.-ksl.  iva,  skr.  wa  (=  lett.  ieva)^  russ.  iva  ,Weide',  acech.  jiva ,Eibe,  Salweide';
ai.  ita-  ,schimmernd,  bunt',  m.  ,Roß,  Vogel,  Antilope'  usw.,  urind.  PN (14.  Jh.)  Aita-ggama  ,auf  einem  Widder  reitend'  (Kretschmer  KZ.  55,  93),
'•V    "Ä
■I
```


## [2026-09-05T20:22:36.806Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"aesma\\|aēšma\\|aešma\\|aesmo\\|Zorn\" POK_01.txt | head -20; echo ===; grep -n \"^ *eis-\\|eis- \" POK_01.txt | head -20",
 "description": "Pokorny eis- passion"
}
```


### [2026-09-05T20:22:36.856Z] TOOL RESULT

```
Exit code 1
176:Weiterbildungen:  aisl.  eisa  f.  [* aidh-s-ön-)  , Feuer',  norw.  , Feuerstätte', mnd.  ese  f.  ,Esse,  Feuerherd^  (aber  ahd.  essa  ,Esse'  s.  unter  äs-  , brennen'); av.  aesma-  m.  , Brennholz'  (*aidh-s-mo-,  vgl.  ohne  s  ai.  idhmd-li  m.  ds.); dazu  halt.  *ais7niä  in  lit.  iesme  , Brennholz';  lit.  aisträ  f.  , Leidenschaft'; acech.  niesteje  (fem.  PL)  ,Ofen',  später  nistej  (mit  7i-Vorsclilag  durch  falsche Zerlegung  der  Verbindungen  *v^n-esteje,  v^n'estejach^^  Berneker  275)  aus *aidh-s-to-]  dazu  schwundstufiges  *idh-s-to-  in  slov.  isteje,  steje  PL  ,Ofea- loch';  nach  Johansson  IF.  19,  J36  auch  ai.  isiakä  .gebrannter  Ziegel',  av. istya-  n.  , Ziegel,  Backstein'.
192:nasaliert  *ing-:  lit.  mgis  , Faulenzer',  mgas  und  angüs  ,faul,  träge',  lett. igstu,  igt  , innerlichen  Schmerz  haben,  verdrießlich,  mürrisch  sein',  ignet , einen  Ekel  haben',  ignls  , mürrischer  Mensch'  (lit.  engti  , würgen,  quälen' bleibt  wohl  fern);  aksl.  jedza  , Krankheit',  nslov.  jeza  ,Zorn',  poln.  jedza , Furie,  Hexe'  (,unwirsch'),  cech.  jezlnka  , Waldfrau'  (usw.,  s.  Berneker 268 f.;  auf  *jega,  nicht  '^aigä,  ist  daher  auch  zurückzuführen:)  russ.  bdba jagd  ,B[exe'  (s.  Brückner  KZ.  45,  318);
532:')  Dazu  .-vuch  as.  ando,  ags.  anda,  anoJa  , Aufgeregtheit,  Zorn,  Leidwesen*,  ahd.  anado, ando,  anto  .Ärger,  Zwn',  mhdi.  ande  .Gefühl  der  Kränkung',  ahd.  anadön,  antön,  nilid.  anden
545:, seinen  Zorn  auslassen',  nhd.  ahnden  unter  einer  Mittelbed.  ,vor  Erregung  keuchen'  (Klug-c s.  V.,  Falk-Torp  5  und  1428  unter  aand-^  Schröder  Abi.  9).  Über  das  zweite  a  von  ahd. anado,  ags.  anocta  s.  Specht  Phil.  Stud.  Voretzsch  36.
1470:nt7A^'  f'*2.  brocke  ^Spieß^  usw.  Unklar  ist^  inwieweit  mir.  brocc  ^Sclmmtz^^ ttn]  brocach  ^gefleckt'^;  cymr.  brock  ^Zorn^  Lärm^  Schaum'^;  nbr.  broc'hed \'6se  (=  gestochen)^  sekundärem  Bedeutungswandel  zu  verdanken  sind oder  zu  verschiedenen  Stämmen  gehören.  Auffallend  ist  der  poln.  (ven.- '11 )  FlN  Brokj  der  vielleicht  ^üachsfluß'  bedeutet. '   \yp.  II  134,  163,  164,  WH.  I  455  f.
1768:,  Hose',  mir.  holgach  f.  ,Beule,  Blase,  Blatter;  Pocken',  bolgamm  ,Schlucl^^ cymr.  hol,  bola,  holy  ,Bauch,  Sack',  hui  ,Sainenhülse'  (PL  von  holy),  bret; holc'h  ,cosse  de  lin',  vann.  pehl-en  (aus  *pehl-)  ds.,  gall.  bulga  ,Ledersac]i< (daraus  ahd.  hulga  ,lederner  Wasserbehälter*);  gall.  Belgae  ,die  Zornigen^
1893:wohl  auch  mir.  bairenn  ,Felsstück*  (dazu  bairnech  ,Tellermuschel'): air.  barae,  mir.  bara  (Dat.  barainn)  ,Zorn*,  bairnech  ,zornig*,  cymr.  bar. baran  ,Zorn*.
2971:terren  ^zanken^,  ndd.  terren,  tarren  ,reizen;  necken',  ahd.  zerren  ,zerreii'; £0t.  intrans.  dis-,  ga-taürnan  ^zerreißen'  ( :  ai.  drndti),  holl.  tornen  ,sicli auftrennen';  vgl.  nominal  ags.  as.  torn,  ahd.  zorn  ,Zorn,  Streit^  heftiger XjQwille'  und  in  ursprünglichster  Bed.  holl.  torn  ^Spaltung,  Scheidung-^ /_-  ai.  dlrnd-,  cjmr.  darn-j  auch  ai.  dlrnd-  heißt  außer  ^gespalten'  auch verwirrt;  in  Verzweiflung  befindlich');  woneben  hochstufig  anord.  tjgrn f,  (*derna),  tjarn  n.  (*dernom)  ^kleiner  See',  ursprgl.  wohl  ,Wasserloch' (y<r\.  ai.  dara-,  darl  ,Loch  in  der  Erde');  zu  ga-taürnan  trat  kausatives (iteratives)  gatarnjan  ^berauben'  (aber  ahd.  uozurnen  ^verachten'  ist penom.  von  *uo-zorn)'^  got.  gataüra  m.  _,Riß';  gataür^s  i.  ^Zerstörung' (=:  ai.  dfti-,  gr.  öciQGig)'^  anord.  tord-  in  Kompositis,  ags.  tord  n.  ,Kot' (*df-töm  ;Abscheidung',  vgl.  lett.  dirstu,  dlrst  ^cacare',  dirsa  ^der  Hintere', >Iühlenbach-Endzelin  I  470,  und  von  einer  Gutturalerweiterung  mhd. zurch,  zürch  m.  ,Tierexkremente') ;
3017:mir.  dorr  ,Zorn',  dorrach  ,rauh,  grob'  (s.  Persson  Beitr.  779  Anm.  1);
3813:Ai.  ddhvanit  ,er  erlosch,  schwand'  (vom  Zorn,  eigentlich  ,verdunstete, zerstob'),  Kaus.  dhvUnayati  ,verdunkelt',  Partiz»  dhväntd-  , dunkel',  n. ,Dunkel';  ^;
3856:lat.  furo  -ere  , rasen,  wüten'  kann  *dhusö  sein,  so  daß  Furiae  =  gr. ^viac,  vgl.  auch  v.  Blumenthal  IF.  49,  172  zu  övauacvar  BdxxccL]  ix^vaarj- iyc7tv6V(T7]  Hes.;  aber  d-vsXXa  ,Sturm,  Windsbraut'  wohl  Femininisierung  eines *^vsXog  , stürmend,  rasend',  wohl  aus  *^uJ^eAos;  ^vfiog  ;Zorn'  ist  =  ^vi^ög ,anima'  und  nicht  wegen  lett.  dusmas  .Zorn'  auf  eine  verschiedene  Grund- form *-9-vafx6g  zurückzuführen;  vgl.  Mühlenbach-Endzelin  I  521;
3872:lit.  dvesiü,  dvesiaü,  dvZsti  ,atmen,  den  Geist  aushauchen,  verenden^ lett.  dvesele  f.  ,Atem,  Seele,  Leben',  ablaut.  (*dhuos-),  lit.  dvasas  m.,  dvasiä f..  Gen.  dväsios  ,Geist',  ,Atem',  lett.  dva§a  ,Atem,  Hauch,  Geruch'  (:  russ. dvochath,  idg.  *dliuos-);  schwundstuf.  (*dhns-),  lit.  düsas  ,Seufzer'  und ,Dunst'  (==  klr.  doch),  düstü,  düsti  ,außer  Atem  kommen',  lett.  dust  ,keu-^ eben',  dusmas  ,Zorn',  lit.  düsiü,  düseti  ,schwer  aufatmen,  seufzen,  keuchen',J düsauti  ds.;  lit.  daüsos  f.  PL  (^dhous-)  ,die  obere  Luft,  Paradies',  dausmÜ, ,lüften';
3927:ags.  dracu  L  ,Plage,  QuaP,  dreccan  ,reizen,  plagen'  (?  mit  expressivem  k?)- aksl.  raz-draBg,  -dra^iti  ,zum  Zorn  reizen',  serb.  dräzlm,  drdziti  ,reizen';
4358:/.  eis-  ,(sich)  heftig,  ungestüm,  schnell  bewegen;  antreiben  =  anregen,  er- quicken; auch  vom  Entsenden,  Schleudern  von  Geschossen,  Pfeilen*; Nominalbildungen:  isoro-s  ,kräftig,  heilig',  FIN  Wort  (e)isä,  oisä usw.,  ois-mo-  , Ansturm,  Zorn*,  ois-tro-  ,Wut'.
4360:av.  aes-  ,(sich)  in  eilige  Bewegung  setzen'  (Präs.  St.  üa-,  isya-,  aesaya-, apers.  aisaya-)^  av.  aesma-  m.  ,Zorn';
4369:lat.  ira,  Plaut,  eira  (*eisa)  ,Zorn';
4925:gr.  lesb.  dgtvcüj  (*dQl-viüj)  ,setze  in  Bewegung,  errege,  reize  zum  Zorn'1* egig,    -löog  ,Streit'    (vielleicht   im   i   zu    unserer   Wurzelform,   falls  nicht i- besser  nach  Schwyzer  Gl.  12,  17  zu  igstdo)  , stütze,  stemme,  stoße,  drängeO^r* ark.   igivvsiv  ,zürnen'  aus  ^Egivvg  eig.  ,die  den  Mörder  verfolgende,  ztiivj nende  Seele  des  Ermordeten'  (??) ;  ''**S'
5031:dazu  mit  dem  Begriffe  teils  der  unruhigen,  auch  ziellosen  Beweguno- teils der  Aufgeregtheit,  des  gewalttätigen  Zornes:  *"
5036:arm.  her  ,Zorn,  Neid,  Hader';
(eval):1: == not found
```


## [2026-09-05T20:22:43.103Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=4200 && NR<=4300 && /^[0-9]{2,4}$/ {print NR\": \"$0}' POK_01.txt; echo \"=== eis area page markers\"; awk 'NR>=4330 && NR<=4400 && /^[0-9]{2,4}$/ {print NR\": \"$0}' POK_01.txt; echo \"=== eis-\"; sed -n '4355,4375p' POK_01.txt",
 "description": "Locate Pokorny page markers"
}
```


### [2026-09-05T20:22:44.703Z] TOOL RESULT

```
=== eis area page markers
=== eis-
urgerm.  *aihter  ,Besitzer'  ist  aus  läpp,  äitdr  ds.  zu  erschließen  (:  ai. isitar-  ds.);
nach  Pedersen  Groupement  30  f.  hierher  toch.  B  aik-,  ais-  ,wissen'.
WP.  I  105,  Feist  20.
/.  eis-  ,(sich)  heftig,  ungestüm,  schnell  bewegen;  antreiben  =  anregen,  er- quicken; auch  vom  Entsenden,  Schleudern  von  Geschossen,  Pfeilen*; Nominalbildungen:  isoro-s  ,kräftig,  heilig',  FIN  Wort  (e)isä,  oisä usw.,  ois-mo-  , Ansturm,  Zorn*,  ois-tro-  ,Wut'.
Ai.  i§näti,  isyati  ,setzt  in  Bewegung,  schwingt,  schnellt  (spritzt  aus), treibt  an;  eilt,  drängt  vorwärts',  Bsati  , gleitet'  {esd-  ,eilend',  ha-  ,das  Hin- eilen'), isate  , enteilt'  (Adv.  Isdt  ,annähernd'),  isanat  ,er  trieb  an',  isanyäti ,treibt  an,  regt  an',  isaydti  ,ist  frisch,  rege,  kräftig;  erfrischt,  belebt',  is- f.  ,Erquickung,  Labung'  (auch  in  is-kxti-  ,Heilung'),  isird-  {'.Xaqög,  Isara) ,stark,  regsam';
av.  aes-  ,(sich)  in  eilige  Bewegung  setzen'  (Präs.  St.  üa-,  isya-,  aesaya-, apers.  aisaya-)^  av.  aesma-  m.  ,Zorn';
gr.  dor.  \(XQÖg  (:ai.  isird-),  att.  Isqoq  (f  :  er,  Schwyzer  Gr.  Gr.  I  482), lesb.  ion.  Iqog  (*isros)  ,kräftig,  rüstig';  weiter  gr.  hdcv,  iveo)  (wenn  mit i  zu  lesen,  so  daß  aus  *iav-ao),  -sca  herleitbar)  .entsende,  leere  aus;  gieße aus',  Med.  ,entleere  mich'  (vgl.  ai.  isnäti);  öla),  diofiai  {ölooaTO,  ävwiaTog^ dv-cüiaTLj  ü)LO-9-rjV,  ölg^slq)  ,meine,  komme  mit  meinen  Gedanken  worauf, verfalle  worauf,  bei  Hom.  mit  i  entweder  durch  metr.  Dehnung  aus *d-i:'[(7]-w  oder  aus  *d-t[ö"]iö,  nachhom.  oT^at  (aus  6io[.iaL)]
mit  ablaut.  oi:
olfxa  ,stürmischer  Angriff,  Andrang',  oif^dü)  .stürme  los',  beides  von Raubvösreln,   wie   ved.  esati   auch   vom   Losschießen   des   Raubvogels  auf
300
f
seiu    Nest    (gr.    Grundf.    *ol(T(.ia,    vgl.    av.    ae§ma-);    hierher    auch  ," olavQog  ;Wut   und  die  sie   durch  ihren   Stich  erregende  Bremse^,  nj verwandt   mit   lit.  aisträ   ^heftige    Leidenschaft',    aistrüs    jleidenschaftS (nicht  besser  oben  S.  12);  in  ähnlicher  Bed.  larva^ei'  ögyllsTai-^
ob  gr.  idoi-iai  ,heile';  iargög  ,Arzt'  hierher  gehören,  ist  zweifelhaft- att.  Formen    ohne   Asper    sprechen   eher   gegen   intervok.   -s-  und gegen   anlaut.  ei-;    bei   einem    Kulturwort   wäre   fremder   Ursprung verwunderlich;  Theander  (Eranos  21,  31  ff.)   geht  von  dem  heiligea Id  aus,  was  auch  die  .schwankende  Quantität  des  l  (die  Heilgötter  *ij ^Irjad)  L,  ""Idawr,  'Ii^aojv  m.  usw.,  vielleicht  auch  der  Stammesname  ^Id(Ä\ vgl.  Schwyzer  Gr.  Gr.  I  80,  als  ta-Rufer)  erklären  würde;
lalvo)  ,wärme'  hat  l  und  braucht  trotz  Schwyzer   Gr.  Gr.  I  681/ 700  nicht  dazu  zu  gehören;   s.  oben  S.  11  und  W.  Schulze  Qu.  ep.  381^ nach  Wissmann  Nomina  postverb.  203  soll  ido^at  die  lautsymbolisch' dehnte  Schwundstufe  der  Wz.  eis-  darstellen,  brauchte  also  der  Quantit differenz  wegen  nicht  von  ialvo)  getrennt  zu  werden;  \\
lat.  ira,  Plaut,  eira  (*eisa)  ,Zorn';
vielleicht  hierher   gall.   Isarno-   PN,   isarno-dori  ,ferrei  ostii*,   air. mir.  larann   n.,   cymr.    haiarn   (erfordert   t-),    acorn.    hoern,   bret.   tio"^ , Eisen'  als  das  ,starke  Metall'  im  Gegensatz  zur  weicheren  Bronze;   -l
germ.  *isarnan  n.,  got.  eisarn,  ahd.  as.  anord.  isarn  ,Eisen'  ist  we« des  l-  vielleicht  aus  ven.-illyr.  *eisarnon  vor  dem  germ.  Wandel  von  ei l  entlehnt;  vgl.  den  ven.  FIN  ^ladqaq,  später  Isarcusj  nhd.  Eisack  (Tii
dazu  der  urir.  PN  I(s)aroSj  air.  /är,  balkanillyr.  iseo-^  messap.  isaretf (Krähe  IF.  46,  184 f.);
ferner  vielleicht  das  kelt.-ligur.-ven.-illyr.-balt.  FIN  Wort  Is-  im FIN  Isara,  nhd.  Isar,  Iser,  frz.  Isere]  *Isiäj  frz.  Oise]  *IsuTä,  engl, usw.  (Pokorny  Urillyrier  114  f.,  161);
die  nhd.  FIN  III,  Illach,  Hier  können  auch  auf  vorgerm.  *Is-l-  zurÜcl gehen  und  mit  den  lett.  FIN  Islinej  Islicis,  wruss.  Isla  (kann  wegen  des -sl-  nicht  echt  slav.  sein)  usw.  verglichen  werden;  der  Name  der  Illen *Illnrä  kann  mit  dem  VN  der  Illyrii  verglichen  werden;  .  •
die  Vollstufe  *jE'w-  außer  in  Isarcus  noch  in  vielen  halt.  FIN:  *Ei8iäf lit.  lesiä,  *Eislä,  lit.  leslä,  lit.  Eisra,  usw.  (Büga  RSl.  6,  9  f.,  Rozwa- dowski  RSl.  6,  47);  hingegen  führt  Büga  wruss.  Istra,  lett.  SeeN  Istra^ lit.  FIN  Isra,  apr.  FIN  Instrutis  ,Inster'  und  thrak.  "'lazQog  auf  *In8tr' zurück;    bisher  hatte  man  ^'larqog  aus  *Is-ro-s  erklärt;  ^
```


## [2026-09-05T20:22:54.530Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"gehen'\\?\\s*$\\|^.\\{0,6\\}ei-\\s*,gehen\\|ei-  ,gehen\" POK_01.txt | head; echo ===; grep -n \"Jahresanfangs\" POK_01.txt; echo ===; awk 'NR>=4180 && NR<=4300' POK_01.txt | grep -n \"^29[0-9]$\\|^30[0-9]$\"",
 "description": "Find Pokorny ei- gehen entry"
}
```


## [2026-09-05T20:22:55.237Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^ei-\\|eis-\\|iron\\|Janus\\|janitor\" AHD_watkins1985.txt | head -40",
 "description": "Grep Watkins AHD"
}
```


### [2026-09-05T20:22:56.515Z] TOOL RESULT

```
4246:I.  ei-  ,gehen',  erweitert  ei-dh-,  ei-gh-,  i-tä-  und  i-ä-,  i-e-  :  iö-  :  19-]  Nominal- bildungen i'to-,  oi'UO-,  oi-tO'  und  i-ter,  Gen.  i-ten-os  ,Weg'. Ai.    imi,    kl,    imdh,   ydnti  ,gehen',  av.    aelti,   yeinti,   apers.  aitiy   ,geht', themat.  Med.  ai.  dya-te   usw.  (das  scheinbar   dehnstufige  ai.   äiti,   av.  äiti ,adit'  ist  *ä-a{ti,  mit  Präf.  ä);
(eval):1: == not found
```


### [2026-09-05T20:22:56.583Z] TOOL RESULT

```
<persisted-output>
Output too large (70.4KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/bvsnbo9nv.txt

Preview (first 2KB):
128:Man and His Physical Environment. A large number of terms relating to time, weather, seasons, and natural surroundings can be reconstructed from the daughter lan- guages, some of which permit certain infer- ences about the homeland of the Indo-European-speaking people before the period of migrations took them to the differ- ent localities where they historically appear.
171:Indo-European had a verb “‘to cook” (pekv-, also having the notion “to ripen’’) and an adjective “raw” (om-). Another op- eration is denoted by peis-', “to crush.” Meat (méms-) was an established item of diet, and some sort of sauce or broth is indi- cated by the term yeue- (*yii-s-, JUICE, from Latin). Other household activities included spinning ((s)né-'), weaving, (webh-) and sewing (syd-). The verb wes-* (WEAR) is ancient and everywhere attested. The Indo- European garment was probably belted: y6és-, “to gird.”
172:The Indo-Europeans knew metal and met- allurgy, to judge from the presence of the word ayes- in Sanskrit, Germanic, and Latin. The term designated copper and perhaps bronze. Iron is a latecomer, technologically, and the terms for it vary from dialect to dialect. Latin has ferrum, while the Ger- manic and Celtic term was *isarno-, properly “holy (metal),” doubtless so called because the first iron was derived from small meteor- ites. Gold was known from ancient times, though the names for it vary; ghel-2, prob- ably “yellow (metal),” and aurum (*aus-, Latin aurum), are widespread. Silver was arg-, with various suffixes, doubtless mean- ing “white (metal).”
...
</persisted-output>
```


## [2026-09-05T20:23:01.970Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"ei-!\\|ei-1\\|ei-'\\|To go\\.\" AHD_watkins1985.txt | head -20; echo \"=== yer\"; grep -n \"yér-\\|yer-\\|Year\\.\\|yéro-\\|yéra-\" AHD_watkins1985.txt | head -20",
 "description": "Grep Watkins for ei- and yer-"
}
```


### [2026-09-05T20:23:02.096Z] TOOL RESULT

```
<persisted-output>
Output too large (42.4KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/b65vhjg57.txt

Preview (first 2KB):
117:General Terms. It is appropriate to begin with a sampling of basic terms in the lexicon, which have no special cultural value but attest to the richness of the tradition. All are widespread in the family. There are two verbs expressing existence, es- and bheue-, found in English Is, Latin esse, and English BE, Latin fu-turus (FUTURE), respectively. There are verbs “to sit” (sed-'), “to lie” (legh-, kei-'), “to stand” (sta-). There are a number of verbs of motion, like g’a-, “to come,” ei-', “to go,” tera-?, “to cross over,” sek’-', “to follow,“ kei-3, “to set in motion,” and the variants of rolling or turning motion in wel-3, wer-%, k”el-'.
148:The names for a number of insects can be reconstructed in the protolanguage, includ- ing the wasP (wopsa), the hornet (*kras-ro-, a derivative of ker-', “head,” from the shape of the insect), and the fly (mu-2). The BEE (bhei-') was particularly important as the producer of honey, for which we have the common Indo-European name melit-. Honey was the only source of sugar and sweetness (swad-, “sweet,” is ancient), and notably was the base of the only certain Indo-European alcoholic beverage, MEAD, medhu-, meaning in different dialects both “mead” (“wine” in Greece) and “honey.” The Germanic lan- guages have innovated, perhaps from a taboo on speaking the name while gathering wild honey; the common Germanic English word HONEY is from an old color adjective for “yellow,” k(e)neko-.
...
</persisted-output>
```


## [2026-09-05T20:23:07.339Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"JANITOR\\|janitor\\|JANUARY\\|January\\|Janus\\|janua\" AHD_watkins1985.txt | head -20",
 "description": "Grep AHD for Janus"
}
```


### [2026-09-05T20:23:07.391Z] TOOL RESULT

```
428:ei-'. To go. 1. Full-grade form *ei- in: a. Latin ire, to go: ADIT, AMBIENT, (AMBITION), CIRCUIT, COITUS, COMITIA, EXIT!, EXIT?, INTROIT, ISSUE, OBITUARY, PERISH, PRAE- TOR, PRETERIT, SEDITION, SUBITO, SUDDEN, (TRANCE), TRANSIENT, (TRANSIT), (TRANSITIVE); b. Greek ienai, to go: ION; ANION, CATION, DYSPROSIUM. 2. Suffixed zero-grade form *i-t- in: a. further suffixed form *i-t-yo- in Latin initium, entrance, beginning (in-, in; see en): COMMENCE, INITIAL, (INITIATE); b. Latin comes (stem comit-), companion (< “one who goes with another”; com-, with; see kom): COUNT?; CONCOMITANT, CONSTA- BLE, (VISCOUNT). 3. Suffixed form ‘*i-ter in Latin iter, journey (> Late Latin itinerdre, to travel): (ERRANT), EYRE, ITINERANT, ITINERARY. 4. Extended form *yd- (< *yaa-) in suffixed forms *yd-no-, yd-nu- in: a. Latin Janus, archway, and Jdnus, god of doors and of the beginning of a year: JANITOR, JANUARY, JANUS; b. San- skrit ydnam, way (in Buddhism, “mode of knowledge,” “vehicle”): HiINAYANA, MAHAYANA. [Pok. 1. ei- 293.]
1698:JAMB kamp- JANITOR ei-1 JANUARY ei-1 Janus ei-1 JAVELIN ghabholo- JEALOUS ya- JELLY gel-3 JEOPARDY yek- JESS yé-
```


## [2026-09-05T20:23:08.086Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"HOROSCOPE\\|horoscope\\|hora\\b\\|HOUR\" AHD_watkins1985.txt | head -20",
 "description": "Grep AHD for hour"
}
```


### [2026-09-05T20:23:08.141Z] TOOL RESULT

```
979:in: a. Latin sollus, whole, entire, unbroken: SOLICITOUS; b. Latin sollemnis (second element obscure), celebrated at fixed dates (said of religious rites), established, relig- ious, solemn: SOLEMN. II. Variant form *sob-. 1. Suffixed zero-grade form *sb-u- giving *sal-u- in Latin saliis, health, a whole or sound condition: SALUBRIOUS, SALU- TARY, SALUTE. 2. Suffixed zero-grade form “slo-wo- giv- ing *sala-wo- in Latin salvus, whole, safe, healthy, uninjured: SAFE, SAGE?, SALVAGE, SALVO!, SAVE!, SAVE. [Pok. solo- 979.] sp6-1. To thrive, prosper. Contracted from *spea-. 1. Suf- fixed o-grade form *sp6-ti- in Germanic *spddiz in Old English spéd, success: SPEED. 2. Suffixed form *spé-s- in Latin spés (plural spérés), hope, with denominative spérdre, to hope: DESPAIR, ESPERANCE. 3. Suffixed zero-grade form “spo-ro- in Latin prosperus, favorable, prosperous (traditionally regarded as from pro spéré, according to one’s hope; pro-, according to; see per’): PROSPER. [Pok. 3. sp(h)éi- 983.] spé-?. Long, flat piece of wood. Contracted from *speo-. I. Basic form *spé-. 1. Germanic *spé-nu- in: a. Old English spén, chip of wood, splinter: SPOON; b. Old Norse spdnn, shingle, chip: SPANNEW. 2. Possibly Greek sphén, wedge (formation unclear; earliest Greek form *sphdan): SPHENE, SPHENO-. II. Suffixed zero-grade form *spa-dh-. 1. Germanic *spadan in: a. Old English spadu, digging tool: sPADE!; b. Middle High German spat (> German Spat), spar: SPATHIC. 2. Greek spathé, broad blade: SPADE?, SPATHE, SPATULA, SPAY. [Pok. sp(hjé- 980.] spei-. Sharp point. I. Basic form *spei-. 1. Germanic *spituz in Old English spitu, stake on which meat is roasted: sPIT?. 2. Germanic *spitja- in German spitz, pointed: spitz. 3. Germanic *spi-ra- in: a. Old English spir, slender stalk: SPIRE!; ACROSPIRE; b. possibly Mid- dle Dutch spierlinc, a small, slender fish, smelt, akin to the source of Old French esperlinge, smelt: SPARLING. 4. Germanic “spik- in Old Norse spik, nail, perhaps akin to the possible source of Middle English spyk, spike: SPIKE}. 5. Germanic *spil- in Middle Low German spile, wooden peg: SPILE, SPILL?. 6. Suffixed form *spei-nd in Latin spina (> Old French espin), thorn, prickle, spine: SPINE, SPINEL, SPINNEY; PORCUPINE. 7. Suffixed form *spei-kd in Latin spica, point, ear of grain: SPICA, SPICA, SPICULUM, SPIKE?. IT. Extended o-grade form *spoig- in Germanic *spaik6én- in Old English spdca, spoke: SPOKE}. [Pok. 1. sp(hjéi- 981.] (s)peik-. Bird’s name, woodpecker, magpie. 1. Suffixed form *peik-o- in Latin picus, woodpecker: PICARO, (PICKET), (PIKE!), (PIQUE). 2. Suffixed form *peik-d- in Latin pica, magpie: PICA2, PIE2. [Pok. (s)piko- 999.] spek-. To observe. I. Basic form *spek-. 1. Germanic *spehon in: a. Old French espier, to watch: ESPY, SPY; b. Germanic derivative *speh-6n-, watcher, in Old Italian spione, spy: ESPIONAGE. 2. Suffixed form *spek-yo- in Latin specere, to look at: SPECIMEN, SPECIOUS, SPECTA- CLE, SPECTRUM, SPECULATE, SPECULUM; ASPECT, AUS- PICE, CIRCUMSPECT, CONSPICUOUS, DESPISE, EXPECT, FRONTISPIECE, INSPECT, INTROSPECT, PERSPECTIVE, PROSPECT, RESPECT, (RESPITE), RETROSPECT, SUSPECT. 3. Latin speciés, a seeing, sight, form: SPECIES; ESPE- CIAL. 4, Latin -spex (< *-spek-), “he who sees,” in: a. haruspex, diviner (see ghere-); b. auspex, augur (see awi-). 5, Suffixed form *spek-d- in Latin (denominative) déspicari, to despise, look down on (de-, down; see de-): DESPICABLE. 6. Suffixed metathetical form *skep-yo- in Greek skeptesthai, to examine, consider: SKEPTIC. IT. Ex- tended o-grade form “spoko- metathesized in Greek skopos, one who watches, also object of attention, goal, and its denominative skopein (< *skop-eyo-), to see: SCOPE, -SCOPE, -SCOPY; BISHOP, EPISCOPAL, HOROSCOPE, TELESCOPE. [Pok. spek- 984.] spel-'. To split, break off. 1. Extended form *speld- in Germanic *spilt- in Middle Dutch spelte, wheat (prob-
1192:yér-. Year, season. 1. Suffixed basic form *yér-o- in Germanic *jéram in Old English géar, year: YEAR. 2. Suffixed o-grade form *ydr-d- in Greek hdrd, season: HOUR; HOROLOGE, HOROLOGY, HOROSCOPE. [In Pok. 1. ei- 293.]
1648:HORN ker-1 HORNBEAM ker-1 HORNBLENDE ker-1 HORNET ker-1 HORNITO gWher- HOROLOGE yér- HOROLOGY yér- HOROSCOPE spek-, yér- HORROR ghers- HORST kert- HORTATIVE gher-5 HORTICULTURE gher-1 HOSE (s)keu- HOSPICE ghos-ti- HOSPITAL ghos-ti- HOSPITALITY ghos-ti- HosT! ghos-ti-
1651:HOUR yér-
```


## [2026-09-05T20:23:19.267Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"eis-\\|IRON \\|IRON$\\|isoro\\|isaro\" AHD_watkins1985.txt | head -20; echo \"=== WIDE\"; grep -on \"WIDE [a-z-]*[0-9]*\" AHD_watkins1985.txt | head -10; echo; grep -n \"wi-dho-\\|widh-\\|To go apart\" AHD_watkins1985.txt | head",
 "description": "Grep AHD for eis- and wide"
}
```


### [2026-09-05T20:23:21.501Z] TOOL RESULT

```
<persisted-output>
Output too large (51.9KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/bkkywaso4.txt

Preview (first 2KB):
171:Indo-European had a verb “‘to cook” (pekv-, also having the notion “to ripen’’) and an adjective “raw” (om-). Another op- eration is denoted by peis-', “to crush.” Meat (méms-) was an established item of diet, and some sort of sauce or broth is indi- cated by the term yeue- (*yii-s-, JUICE, from Latin). Other household activities included spinning ((s)né-'), weaving, (webh-) and sewing (syd-). The verb wes-* (WEAR) is ancient and everywhere attested. The Indo- European garment was probably belted: y6és-, “to gird.”
189:Most interesting are the cases where from two or more traditions (usually including Homer and the Rig-Veda) it is possible to reconstruct a poetic phrase or formula con- sisting of two members. Such are the expres- sions ‘“‘imperishable fame,” *klewos ndhg’hitom (kleu-', dhg“hei-); “holy (men- tal) force,” *isorom menos (eis-', men-'); and the “weaver (or crafter) of words,” the Indo- European poet himself, *wek”om teks-on (wek”, teks-). The immortality of the gods (*n-mrto-, from mer-?) is emphasized anew by the vivid verb phrase nek-' tera-?, “to overcome death,” appearing in the Greek word nektar, the drink of the gods. And at least one three-member formula (in the sense of the word in traditional oral poetry) can be reconstructed for the poetic language of prayer, on the combined evidence of four languages, Latin, Umbrian, Avestan, and Sanskrit: “Protect, keep safe, man and cat- tle!” (pa- wi-ro- peku).
...
</persisted-output>
```


## [2026-09-05T20:23:24.955Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^eis-\\|eis-'\\. \\|eis-1\\.\" AHD_watkins1985.txt | head; echo ===; grep -n \"IRON eis\\|IRON \" AHD_watkins1985.txt | head -5; echo ===; grep -n \"WIDE \" AHD_watkins1985.txt | head -5",
 "description": "Targeted AHD greps"
}
```


### [2026-09-05T20:23:25.037Z] TOOL RESULT

```
Exit code 1
431:eis-1. In words denoting passion. 1. Suffixed form “eis-d- in Latin ira, anger: IRASCIBLE, IRATE, IRE. 2. Suffixed zero-grade form “is-(a)ro-, powerful, holy, in Greek hie- ros, “filled with the divine,” holy: HIERATIC, HIERO-; HIERARCH, (HIERARCHY), HIEROGLYPHIC, HIEROPHANT. 3. Germanic *isarno-, “holy metal” (possibly from Celtic), in Old English ise(r)n, iren, iron: IRON. 4. Suf- fixed o-grade form *ois-tro-, madness, in Greek oistros, gadfly, goad, anything causing madness: ESTRUS; (ES- TRONE). [Pok. 1. eis- 299.]
432:eis-2. Ice, frost. Germanic *is- in Old English is, ice: ICE; ICICLE. [Pok. 2. ei-s- 301.]
828:fixed o-grade form *pozk-itd in Germanic *faihithé in Old French faida, hostility, feud: FEUD!. [Pok. 2. peig-795.] peis-'. To crush. 1. Suffixed zero-grade form *pis-to- in Latin pistillum, pestle: PESTLE, PISTIL. 2. Nasalized zero-grade form *pi-n-s- in Latin pinsdre, to pound: PISTON. 3. Possibly suffixed form *pis-lo- in Latin pilum, javelin, pestle: PILE?. 4. Perhaps Greek ptissein (pt- for p-), to crush, peel: PTISAN, (TISANE). [Pok. 1. (peis-2), pis- 796. peis-2. To blow. Germanic “fis- in Old Norse fisa, to fart, akin to the Scandinavian source of Middle English fise, fart: F1zGIG. [Pok. 2. peis- 796.] peisk-. Fish. Zero-grade form *pisk-. 1. Suffixed Ger- manic form “fisk-a- in: a. Old English fisc, fish: FISH; b. Middle Dutch vische, vis, fish: WEAKFISH. 2. Suffixed form “pisk-i- in Latin piscis, fish: PISCARY, PISCATORIAL, PISCES, PISCI-, PISCINA, PISCINE; GRAMPUS, PORPOISE. [Pok. peisk- 796.] pek-'. To make pretty. 1. Possibly Germanic “fagra- in Old English feger, beautiful: FAIR}. 2. Possibly Germanic *fagin-, *fagan-, to enjoy, in Old English fegen, joyful, glad (> fagnian, to rejoice): FAIN, FAWN}. [Pok. 1. pek- 796.] pek-?. To pluck the hair, fleece, comb. 1. Extended form *pekt- in Germanic *fehtan, to fight, in Old English feohtan, to fight: FIGHT. 2. Suffixed extended form *pekt-en- in: a. Latin pecten, a comb: PECTEN; b. zero-grade. form *pkt-en- in Greek kteis (genitive ktenos < *pktenos), a comb: CTENIDIUM; CTENOID, CTENOPHORE. [Pok. 2. pek- 797.] peku-. Wealth, movable property. 1. Germanic *fehu- in: a. Old Norse fé, property, cattle: FELLOW; b. Old French fie, fief: FEE; c. Medieval Latin feudum, feudal estate: FEUD?; INFEUDATION. 2. Suffixed form “peku-n- in Latin peciinia, property, wealth: PECUNIARY; IMPECUNIOUS. 3. Suffixed form *peku-l- in Latin peciilium, riches in cattle, private property: PECULATE, PECULIAR. [In Pok. 2. pek- 797.] pekv-. To cook, ripen. 1. Assimilated form (in Italic and Celtic) *kvekw- in Latin coquere, to cook: COOK, CUISINE, (CULINARY), KILN, KITCHEN, QUITTOR; APRICOT, BISCUIT, CONCOCT, DECOCT, PRECOCIOUS, RICOTTA. 2. Greek pe- pon, ripe: PEPO. 3. Greek peptein, to cook, ripen, digest (> peptos, cooked): PEPTIC; DRUPE, EUPEPTIC, PEPSIN, PEPTONE, PUMPKIN. 4. Greek -pepsia, digestion: DYSPEP- sia. 5. Sanskrit pakva-, ripe: PUKKA. [Pok. peky- 798.] pel-1. Dust, flour. 1. Latin pollen, fine flour, dust: PoL- LEN. 2. Latin pulvis, dust: POWDER, PULVERIZE. 3. Latin palea, chaff: PAILLASSE, PALEA. 4. Greek palunein, to sprinkle flour: PALYNOLOGY. 5. Greek poltos, porridge (made from flour), probably borrowed via Etruscan into Latin as puls, pottage: POULTICE, PULSE?. [Pok. 2 b. pel- 802.] pel-2. Pale. 1. Suffixed variant form *pal-wo- in: a. Ger- manic *falwaz in Old English fealu, fealo, reddish yellow: FALLOW DEER; b. Latin pallére, to be pale: PALE, PAL- LID, PALLOR; APPALL; C. Latin palumbés (influenced in form by Latin columbus, dove), ringdove, “gray bird”: PALOMINO. 2. Suffixed form “pel-ko- probably in Ger- manic *falkén-, falcon (< “gray bird”), in: a. Old French girfaut, gyrfalcon: GYRFALCON; b. Late Latin falcé, falcon (but Germanic *falkén- is also possibly from the Late Latin): FALCON. 3. Suffixed extended form *peli- wo- in: a. Greek pelios, dark: PELOPS; b. o-grade form *poli-wo- in Greek polios, gray: POLIOMYELITIS. 4. Per- haps Greek pelargos (< *pelawo-argos), stork (< “black- white bird”; argos, white; see arg-); PELARGONIUM. [Pok. 6. pel- 804.] pel-3. To fold. 1. Extended o-grade form *polt- in Ger- manic *falthan, *faldan in: a. Old English fealdan, faldan, to fold: FoLD!; b. Old High German faldan, to fold: FALTBOAT; Cc. Germanic compound “*faldistélaz, “folding stool” (*stdlaz, stool; see sta-), in Medieval Latin compound faldistolium, folding chair: FALDSTOOL;
(eval):1: == not found
```


## [2026-09-05T20:23:36.916Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; wc -l KLN_1966.txt KLN_1971.txt; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(json.dumps(d['KLN'],ensure_ascii=False,indent=1))\"",
 "description": "Klein file info"
}
```


### [2026-09-05T20:23:38.723Z] TOOL RESULT

```
   41262 KLN_1966.txt
  271509 KLN_1971.txt
  312771 total
{
 "title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67",
 "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein",
 "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
 "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.",
 "notes": "Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt (paginated by leaf); /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt (plain djvu.txt, no page marks)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt"
 ],
 "cites": "page number, continuous across the two volumes (1966–67)"
}
```


## [2026-09-05T20:23:45.154Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 -c \"\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\np=t.split('\\f')\nprint('leaves',len(p))\nprint('--- last leaf ---')\nprint(p[-1][:1500])\n\"",
 "description": "Klein leaf count and tail"
}
```


### [2026-09-05T20:23:47.000Z] TOOL RESULT

```
leaves 903
--- last leaf ---
��true’,  and  Gk. ruov,  fr.  mtoraiv,  ‘to  look  at,  examine’.  See very  and  -scope.  The  correct  form  would  be alethoscope  (fr.  Gk.  dcXvjffrji;,  ‘true’  and  -rsy.6- mov ) .
veratral,  n.,  the  radical  C9H10O4  (chem.)  —  Form¬ ed  with  adj.  suff.  -al  fr.  L.  verdtrum,  'hellebore’. See  veratrine.
veratric,  adj.,  pertaining  to  a  white  crystalline acid. —  Formed  with  adj.  suff.  -ic  fr.  L.  verdtrum, ‘hellebore’  (see  veratrine) ;  so  called  because  it  is easily  obtained  by  the  decomposition  of  vera¬ trine.  \
veratridine,  also  veratridin,  n.,  an  amorphous  al¬ kaloid  obtained  from  sabadilla  seeds, C36H61OnN  (chem.)  —  Coined  fr.  L.  verdtrum, ‘hellebore’  (see  next  word),  and  the  chem. suffixes  -ide  and  -ine  (resp.  -in), veratrine,  n.,  also  veratrin,  veratrina,  veratria,  a poisonous  mixture  of  alkaloids  obtained  from sabadilla  seeds,  used  in  medicine  in  the  treat¬ ment  of  rheumatism,  neuralgia,  etc.  —  F.  vera¬ trine,  fr.  ModL.  veratrina,  fr.  L.  verdtrum,  ‘helle¬ bore’,  fr.  verare ,  ‘to  tell  the  truth’,  fr.  verus, ‘true’;  so  called  because
```


## [2026-09-05T20:23:55.721Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\np=t.split('\\f')\nfor i,leaf in enumerate(p):\n    for w in ['\\nion,','\\nyear,','\\nwide,','\\nhour,','\\nJanuary,','\\njanitor,','\\niron,','\\nhoroscope,']:\n        if w in leaf:\n            print('LEAF',i,repr(w))\nEOF",
 "description": "Find Klein headword leaves"
}
```


### [2026-09-05T20:23:57.851Z] TOOL RESULT

```
LEAF 400 '\nhoroscope,'
LEAF 437 '\nion,'
LEAF 445 '\nJanuary,'
```


## [2026-09-05T20:24:09.046Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nleaf=t[437]\ni=leaf.find('\\nion,')\nprint(leaf[max(0,i-1200):i+1500])\nEOF",
 "description": "Read Klein ion entry"
}
```


### [2026-09-05T20:24:11.110Z] TOOL RESULT

```
e’  (to  make  the name  of  this  element  equal  in  ending  to  chlorine and  fluorine),  which  was  coined  by  its  discov¬ erer,  the  French  chemist  Bernard  Courtois (1777-1838),  in  1811  fr.  Gk.  lociS-fy;,  ‘like  a violet’,  fr.  (ov,  ‘violet’,  and  -oetSfji;,  ‘like’,  fr. eI8o;,  ‘form,  shape’;  so  called  by  him  from the  color  of  its  vapor.  See  iolite  and  -oid.  For the  ending  see  chem.  suff.  -ine. iodism,  n.,  iodine  poisoning  (med.)  —  See  prec. word  and  -ism.
iodize,  tr.  v.,  to  treat  or  impregnate  with  iodine. —  See  iodine  and  -ize.
iodo-,  before  a  vowel  iod-,  combining  form meaning  iodine.  —  Fr.  ModL.  iodum,  fr.  F. iode.  See  iodine.
iodoform,  n.,  a  crystalline  compound  (chem.)  —
A  blend  of  iodine  and  chloroform, iolite,  n.,  a  blue  mineral.  —  G.  lolit,  coined  by the  German  geologist  and  mineralogist  Abra¬ ham  Gottlob  Werner  (1750-1817)  in  1810  fr. Gk.  fov,  ‘violet’,  and  >10o;,  ‘stone’.  Crk.  fov is  prob.  a  Mediterranean  loan  word.  Cp.  the first  element  in  Jantbine  and  the  second  element in  Leucojum.  Cp.  also  violet.  For  Gk.  Xf&o? see  -lite,  litho-.
ion,  n.,  either  of  the  two  elements  into  which  a compound  is  decomposed  through  electrolysis.
—  Gk.  fov,  neut.  of  lav,  ‘going’,  pres.  part,  of tcvai,  ‘to  go’,  fr.  I.-E.  base  */-,  ‘to  go’,  whence also  L.  Ire,  ‘to  go’,  iter  (gen.  itineris),  ‘a  journey’ ; see  itinerate.  The  word  ion  was  introduced  into electricity  by  the  English  physicist  and  chemist Michael  Faraday  (1791-1867);  cp.  anion,  cation, -ion,  suff.  forming  nouns  denoting  state,  con¬ dition  or  action.  —  L.  -id,  gen.  -ionis  (either directly  or  through  the  medium  of  OF.  and  F. -ion).  Cp.  -ation,  -ition.
Ionian,  adj.  and  n.  —  Formed  with  suff.  -an  fr. L.  Ionius,  fr.  Gk.’Idmoi;,  ‘Ionian’,  fr.’Tcav  (gen. Tcovoe),  contraction  of  Titov  (gen.  Taovo^), ‘Ionian’,  fr.  orig.  *TiFtov,  whence  Heb.  Yawdn, Akkad.  Iamanu,  Idvanu,  Egypt.  Yfvana,  Y*- vanna,  ‘Greek’.  Cp.  also  OI.  Yavanah,  OPers. Yauna,  ‘Greek’,  OI.  yavanika,  ‘Greek  woman’; ‘curtain  (in  the  theater)’,  lit.  ‘Greek  (partition)’. Ionic,  adj.  —  L.  lonicus,  fr.  Gk.  Ttov.xic,  ‘Ionic’, fr.  Tov.  See  prec.  word  and  -ic. ionium,  n.,  a  radioactive  element  pertaining  to the  uranium  group  (chem)  —  ModL.,  formed fr.  ion  with  suff.  -ium;  so  called  in  allusion  to its  ionizing  power.
ionize,  tr.  v.,  to  separate  into  ions.  —  Formed  fr. ion  with  suff.  -ize.
ionosphere,  n.,  that  part  of  the  earth’s  atmospher
```


## [2026-09-05T20:24:24.531Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in [399,400,436,437,445]:\n    nums=re.findall(r'(?m)^\\s*(\\d{3,4})\\s*$', t[i])\n    nums2=re.findall(r'\\b(7\\d\\d|8\\d\\d)\\b', t[i][:300]+t[i][-300:])\n    print(i, nums[:6], nums2[:6])\nEOF",
 "description": "Find printed page numbers in Klein leaves"
}
```


### [2026-09-05T20:24:26.714Z] TOOL RESULT

```
399 ['742'] []
400 ['743'] []
436 ['812', '813'] []
437 ['814'] []
445 ['824', '825'] []
```


## [2026-09-05T20:24:34.019Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nleaf=t[445]\ni=leaf.find('\\nJanuary,')\nprint(leaf[max(0,i-2500):i+900])\nEOF",
 "description": "Read Klein January/janitor"
}
```


### [2026-09-05T20:24:35.705Z] TOOL RESULT

```
press tightly’,  and  orig.  meaning  ‘fruit  pressed  to¬ gether’.
Jamaica.  —  Short  for  Jamaica  rum. jamb,  n.,  sidepost.  —  F .jambe,  fr.  Late  L,  gamba, ‘leg’.  See  gamb  and  cp.  words  there  referred  to. Cp.  also  enjambment. jamb,  v.  —  See  jam,  v.
jamboo,  jambool,  jambul,  n.,  the  Java  plum;  the rose  apple.  —  Hind,  jambu,  ‘the  rose  apple’,  fr. OI.  jambuh,  jambdh,  which  is  prob.  of  non- Aryan  origin.
825
jamboree,  n.,  gathering  (esp.  of  boyscouts).  — Of  Hindu  origin;  introduced  by  Rudyard Kipling  (1865-1936).
James,  masc.  PN.  • —  Late  L.  Jacdmus,  altered fr.  Jacdbus.  See  Jacob  and  cp.  jimmy, jamesonite,  n.,  a  lead  antimony  sulfide  (mineral.)
—  Named  after  Professor  Robert  Jameson  of Edinburgh  (1774-1854),  who  analyzed  it.  For the  ending  see  subst.  suff.  -ite.
jampan,  also  jompon,  n.,  a  kind  of  sedan  (India).
—  Bengali  jhapdn,  fr.  Hind,  japan,  jhappan,  fr. jSp,  ‘a  cover’.
Jane,  fern.  PN.  —  F.  Jeanne,  fr.  OF.  Jehane,  fr. ML.  Johanna,  Joanna.  See  Joan  and  cp.  Jean, fern.  PN.  Cp.  also  demijohn,  jenny.
Jane,  n.,  a  small  Genoese  coin.  —  OF.  Jane,  fr. ML.  Janua,  ‘Genoa’.  Cp.  L.  Genua,  whence  It. Genova,  F.  Genes.
Janet,  fem.  PN.  —  A  dimin.  of  Jane  (q.v.) jangada,  n.,  a  kind  of  catamaran.  —  Port.,  fr. Malayalam  cahhdtam,  fr.  OI.  sarpghatah,  a joining  together  of  timber,  union’, jangar,  n.,  a  raft.  —  Port,  jangada.  See  prec.  word, jangle,  intr.  and  tr.  v.  —  ME .janglen,  ‘to  chatter, quarrel’,  fr.  OF.  jangler,  ‘to  chatter’,  which  is of  Teut.  origin.  Cp.  MDu.  jangelen,  Du.  jen- gelen,  ‘to  whine’,  dial.  G.  jangeln,  ‘to  speak  in a  whining  manner', 'which  are  prob.  imitative. Cp.  jingle.
Derivatives:  jangl-er,  n.,  jangl-ing,  n. jangle,  n.  —  ME.,  fr.  OF.  jangle,  fr.  jangler.  See jangle,  v.
Janissary,  n.  —  See  Janizary, janitor,  n.,  doorkeeper,  porter.  —  L.,  formed with  suff.  -tor  fr.  jams,  ‘a  covered  passage,  ar¬ cade’,  which  is  of  uncertain  origin.  It  is  perh. cogn.  with  OI.  ydnah  (masc.),  path  ,  (neut.), ‘a  going’,  ydti,  Avestic  yditi.  ‘goes,  travels’,
Janthina,  n.,  a  genus  of  pelagic  snails  (zoo/.)  — ModL.,  fr.  L.  ianthinus,  ‘violet  blue’,  fr.  Gk. lavtkvo ?,  which  is  compounded  of  fov,  ‘violet’, and  (tv $04,  ‘flower’.  See  iolite,  anther  and  -ine (representing  Gk.  -ivo?).
January,  n.  —  L.  Januarius  (mensis),  ‘the  month dedicated  to  Janus.  See  Janus  and  -ary.
Janus,  n.,  ancient  Italian  god  of  doors  and  gates, entrances  and  beginnings;  represented  with  two faces.  —  L.  Janus,  personification  of  janus, ‘arched  passage,  arcade’,  whence  janua,  ‘door’. See  janitor  and  cp.  January.
Jap,  adj.  and  n.  —  Colloquial  abbreviation  for Japanese.
Japan,  n.  —  Chinese  Jih-pun  (corresponding  to Jap.  Ni-pon),  ‘sunrise’,  formed  fr.  jih  (resp.  Jap. ni),  ‘sun’,  and  pun  (resp.  Jap.  pon),  ‘origin’, japan,  n.,  a  hard  kind  of  varnish.  —  Fr.  prec. word;  so  called  because  this  varnish  was  orig. used  in  Japan.
Derivative:  japan,  tr.  v.,  to  lacquer  with  japan. Japanese,  adj.  and  n.  —  Formed  fr.  Japan  with suff.  -ese.
Japanesque,  adj.,  in  the  Japanese  style.  —  A hybrid  formed  f
```


## [2026-09-05T20:24:46.672Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(890,903):\n    nums=re.findall(r'(?m)^\\s*(\\d{3,4})\\s*$', t[i])\n    head=t[i][:60].replace('\\n',' ')\n    print(i,nums[:4],head)\nEOF",
 "description": "Check Klein last leaves pages"
}
```


### [2026-09-05T20:24:48.512Z] TOOL RESULT

```
890 ['1680']   universolog- ist,  n. univocal,  adj.,  having  one  meani
891 []   the  past  participle. urea,  n.,  crystalline  compound  
892 ['1003'] us.  See  use, n.,  and  -age. usance,  n.  —  ME.  usaunce,
893 [] id.  Cp.  also uvea,  uvula. uvanite,  n.,  a  hydrous  uran
894 [] andering’,  formed with  gerundive  suff.  -bundus  fr.  vag
895 ['1691'] ,  bodies  of  those  who were  slain  in  battle’,  wol,  ‘
896 ['1692'] ��,  nr^  (Hesychius), ‘web’,  L.  pannus,  piece  of  cloth
897 []   —  A  hybrid  coined  fr.  vari¬ ola  and  suff.  -ite  (r
898 ['1694', '1695'] agential  suff.  -or. vau,  also  waw,  n.,  the  sixth  let
899 ['1696']   F.)  veine,  fr.  L. vena,  ‘blood  vessel,  watercourse, 
900 [] r’, vojina,  ‘war’,  Gk.  iep.ai  (for  ‘I  as¬ pire  to,  t
901 [] , ventricle,  n.,  cavity  in  an  organ  of  the  body.  — 
902 [] ��true’,  and  Gk. ruov,  fr.  mtoraiv,  ‘to  look  at,  exa
```


## [2026-09-05T20:24:56.900Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^year, n\\.\\|^wide, adj\\|^iron, n\\.\\|^hour, n\\.\" KLN_1971.txt | head",
 "description": "Grep Klein 1971 headwords"
}
```


### [2026-09-05T20:24:56.957Z] TOOL RESULT

```
116225:hour, n. — ME., fr. OF. ure , ore, hore (F. heure), 
126746:iron, n. — ME. iren, iron, fr. OE. tse(r)n, Trent, rel. 
267049:wide, adj. — ME. wide, fr. OE. wid, rel. to OS., 
269593:year, n. — ME. yere, fr. OE. gear, rel. to OS.,
```


## [2026-09-05T20:24:59.943Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '269593,269615p' KLN_1971.txt; echo \"=== WIDE\"; sed -n '267049,267070p' KLN_1971.txt; echo \"=== HOUR\"; sed -n '116225,116245p' KLN_1971.txt; echo \"=== IRON\"; sed -n '126746,126770p' KLN_1971.txt",
 "description": "Read Klein 1971 entries"
}
```


### [2026-09-05T20:25:00.109Z] TOOL RESULT

```
year, n. — ME. yere, fr. OE. gear, rel. to OS., 
OHG., MHG. jar, ON. dr, Dan. aar, Swed. dr, 
OFris. ger, Du . jaar, G. Jahr, Goth, jer, ‘year’, 
and cogn. with Avestic yar i , ‘year’, Gk. &poc, 
‘year’, <&poc, ‘any limited time, the time of day, 
hour, season spring, year’ (whence L. hdra, 
‘hour’), OSlav. jarti, ‘spring’, L. hornus (for *ho- 
yor-inos), ‘of this year’ (from the abl. *ho yoro , 
‘in this year’). All these words possibly mean lit. 
‘that which goes or passes’, and derive fr. I.-E. 
*ye-ro, an enlargement of base *ye itself an 
enlargement of base *ey-, ‘to go’, whence Gk. 
slut, tevoa, L. eo, ire, ‘to go’. See itinerate and 
cp. yore and the first element in yahrzeit. Cp. al- 
so horary, hour. 

Derivatives: year-ling, n., yearly (q.v.) 
yearly, adj. — ME. yerely , yeerly , fr. OE. 
gear lie, formed fr. gear , ‘year’, with suff. -lie. 
See year and adj. suff. -ly. 
yearly, adv. — ME. yerely, yerly, fr. OE. gearlice, 
formed fr. gear, ‘year’, with suff. -lice. See year 
and adv. suff. -ly. 
=== WIDE
wide, adj. — ME. wide, fr. OE. wid, rel. to OS., 
OFris. wid, ON. vidr, Dan., Swed. vid, Du. wijd, 
OHG., MHG. wit, G. weit, fr. Teut. *wida-, cor- 
responding to I.-E. *wi-ito-, which is formed fr. 
I.-E. base * wi-, ‘asunder’, and the pp. stem of 
I.-E. *ei-, ‘to go’. For the first element see with, 
for the second see itinerant. 

Derivatives: wide, adv. (q.v.), wide , n., wide-ly, 
adv., wid-en , v., widen-er , n., wideness (q.v.), 
wid-ish, adj. 

wide, adv. — ME., fr. OE. wide, fr. wid, ‘wide’ 
(adj.) See wide, adj. 

wideness, n. — ME. widnesse, fr. OE. widnes, fr. 

wid, ‘wide’. See wide, adj. and -ness, 
widgeon, n., any of various kinds of migratory 
wild ducks. — Prob. from a NOF. var. of F. 
vigeon, vingeon, fr. L. vipionem, acc. of vipio, ‘a 
kind of small crane’, a word of Balearic and 
=== HOUR
hour, n. — ME., fr. OF. ure , ore, hore (F. heure), 
fr. L. hora, ‘hour’, fr. Gk. <£pa, ‘any limited 
time, the time of day, hour, season spring, year’, 
which is cogn. with Avestic jar*, ‘year*, OSlav. 
jarii, ‘spring’, L. hornus (fr. *hd-yorinos), ‘of this 
year’, Goth, jer, OE. gear, ‘year’. See year and 
cp. words there referred to. Cp. also Horae, 
horal, horary, the first element in horography, 
horologe, horoscope, and the second element in 
encore. 

Derivatives : hour-ly, adj. and adv. 
houri, n., a nymph of the Moslem Paradise; (fig.) 
a seductive woman. — F., fr. Pers. hurt, fr. 
Arab, hur, pi. of ah war, fem. haurd', ‘having 
beautiful black eyes’, fr. hawira, ‘had black 
eyes’, which is rel. to Heb. bawdr, Aram.-Syr. 
hdwar, ‘was white’, Heb, hur, ‘white stuff’, horf, 
‘white bread’. The A in Pers. hurl is a formative 
element serving to denote the singular, 
house, n. — ME. hus , hous , fr. OE. hits, rel. to 
=== IRON
iron, n. — ME. iren, iron, fr. OE. tse(r)n, Trent, rel. 
to OS. isarn , ON. isarn, jam, OFris. iser(n ), 
MDu. iser, Du. ijzer, OHG. isarn , isan, MHG. 
isern, iser, isen, G. Eisen, Goth, eisarn, isarn. 
These words, as well as the Gaul. PN .Isarno- and 
OIr. iarann , iarn, W. haiam, OCo. hoern, ‘iron*, 
are prob. Illyrian loan words, and orig. denoted 
the ‘strong’ metal (in contradistinction to the 
softer bronze). Cp. OI. i?irah, ‘vigorous, strong’, 
Gk. Iep6c, ‘strong’, and see ire. 

Derivatives: iron, adj. and v., iron-er, n., iron- 
ing, n., irony (q.v.) 

Iron Curtain. — Coined by Winston Churchill in 
1946 (in a speech at Fulton, Mo., U.S.A.) 
ironic, also ironical, adj. — Late L. ironicus, fr. 
Gk. eiptovixds, ‘dissembling’, fr. sZpcav, ‘dis- 
sembler’, See irony and -ic, resp. also -al. 
Derivative: ironical-ly , adv. 
ironmold, n. — Altered fr. iron mole by folk ety- 
mology, which associated this word with mold. 
See iron and mole, ‘spot’. 

Derivative: ironmold , tr. and intr. v.
```


## [2026-09-05T20:25:19.177Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources; python3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nfor k in ['HRN','BQT','MON','BRT']: print(k, d[k].get('cites'), '|', d[k].get('lookup_hint','')[:300], '|', d[k].get('page_offset',''))\n\"",
 "description": "Ref lookup hints"
}
```


## [2026-09-05T20:25:19.956Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"hīrak\\|hirak\\|hērak\\|herak\\|yāirka\\|yairka\" HRN.txt | head -20",
 "description": "Grep Horn for hirak"
}
```


### [2026-09-05T20:25:21.645Z] TOOL RESULT

```
HRN page number of Horn, Grundriss der neupersischen Etymologie (1893); entries are also numbered | Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann. | leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
BQT page number, continuous across the five volumes of Mo'in's edition (1342/1963 = Amir Kabir 1362 reprint); Mo'in's etymological footnotes are the cited material | grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d | vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
MON page number of Mo'in's six-volume Farhang-e Farsi; MON5:… / MON6:… = volume 5 / 6 (proper names) | Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe | None
BRT column number (the Altiranisches Wörterbuch is numbered by column, two per page) | Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops. | Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
```


### [2026-09-05T20:25:21.685Z] TOOL RESULT

```
9471:Np. hest hat sein h von heft bezogen wie herakl.
22640:herakl. oxrw 1095.
```


## [2026-09-05T20:25:27.442Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor i in (269,270,271):\n    print('=== leaf',i)\n    print(t[i][:2500])\nEOF",
 "description": "Read Horn leaves around p.249"
}
```


### [2026-09-05T20:25:29.017Z] TOOL RESULT

```
leaves 412
=== leaf 269
— 248 —
80, 318), Tüchtigkeit*; ai. sündra-, skr. sundani^)
'schön*: phlv. hunar, arm. LW. hnar.
LW. kurd. huner; af;'. bei. (95) hunar.
1/1109. henffäm *Zeit', Ungarn (AM. 213 Zeile 4 v. u.).
ap. *han(/ama' *Zeit*, vergl. aw. aiwLgäma^ 'Winter ;
phlv. hangäm (päz. ögäm), arm. LW. angam *Cbel,
Unglück'.
^1110. henöz noch* (reimt auf iös, 5ö5, y ö-e bei Firdös i
und im Burzönäme, Macan, 1533 Vers 3 v. u., 1583
Vers 17, 2260 Vers 6, 2212 Vers 1), henüz (reimt
auf äz, teinüz, Sadi, Gulistän, Sprenger, 93 Zeile
1 V. u.; 10, 7; Sahn. I, 135 Vers 118)2), ^^^ (gä^n.
I, 67 Vers 97).
Darmes teter. Et. ir. II, 114, 115 ist durchaus
verfehlt.
Zusammenhang mit arm. hanapaz *immer (WZKM.
5, 355, Fr. Müller) ist schon wegen des Bedeutungs-
y Unterschiedes nicht wahrscheinlich.
^1111. {\)hös, hus * Verstand, Klugheit*, huslwär Verständig*.
aw. tisi die beiden Ohren •^) (J. von Fierlinger,
^^J \ KZ. 27, 335); dor. wg, cofatoc, lat. atiri,% lit. austs,
\ ^v^'t got. cmsö etc.; phlv. hös bezw. ös * Verstand*, arm. LW.
' US ^Gedächtnis, Verstand, Acht* (Hübschmann,
No. 237).
Die abgeleitete Bedeutung * Verstand* aus der ur-
sprünglichen 'Ohr' ist erst mittelpersisch.
1112. {2)Jiö8 *Tod* (Vis und Rämin, Seite 82 Vers 13) 4).
aw. aosah' 'Tod'; phlv. hös, hösömand, ahös 'un-
sterblich (Men.).
Eigentum, das Vullers auf diese Weise seinen Büchern einverleibt hat.
Allerdings ist die Klaue des Löwen an sehr vielen Stellen auch ohne
Citat, dai>- Vullers übrigens gewiss nicht mala fide unterlassen hat,
deutlich zu erkennen. Die Lesung uner verbietet wohl die Etymologie.
M Vergl. Jacobi, KZ. 31, 315.
*) Sämmtliche Belege stammen von Herrn Prof. Nöldeke.
^) Ausführliche Angabe der Literatur pro und contra neuerdings
bei Johansson, BB. 18, 25.
*) Stellen aus dem Öähnärae bei Spiegel, Glossar, 368.
=== leaf 270
- 249 —
4ll3. höm 'Haomastrauch, -pflanze*; vergl. hfun (d-majüH
. -^wo^ *Magierhaoma (eine nicht näher zu bestimmende
^^|j^' Pflanze, AM. 268).
'' aw. haowa-; phlv. hötn; ai. soma-.
bei. vergl. hörn (LW., 99).
V1114. Äe^ jemand, jemals*, mit Negation 'niemand, nichts;
ec (äähn. I, S. 4 Vers 59).
W^ Käs. K. Z. ec,
ap. *(tiva ~r ciy (Salemann, Mel. asiat. IX, 241);
phlv. ec bezw. hec (päz. hec, hSöi),
1115. herhud *Feuerpriester , herkede, hermend, {her *Feuer',
das man daraus erschlossen hat, ist aber bedenklich^).
aw. aeAlrapaiti' ; phlv. ehrpat (Inschriften), lierput,
herpatastän, herputlh bezw. erpat,
1116. lilrek, {^hereh?) 'Bockchen, Zickchen'.
ap. *yö*V7/ra- 'Jährling (Tomas chek, Centralasiat.
Studien II, 766).
si/n. yirk 'ausgewachsenes , männliches Schaaf,
Zuchtwidder.
Wenn die Etymologie richtig ist, so hätten wir
in diesem Worte die einzige neupersische Spur des
aw. yär-, ap. -yära-.
' 1117. hezutn (Is. 30, 88), hezem 'Brennholz*; Mme-).
^c^^ S- i^^i(^\ Käs. Q. K. hezem, ezem,
^ aw. a^sma^^') 'Brennholz'; phlv. esw (nur um-
schreibend), hEzam bezw. ezam (päz. hezam) ; ai. idlimd-.
kurd. ezink (H.-Sch.); minj. czma.
*) FJ hat zwar einen Vers von Emir Muizzi; im Awesta und
Pehlevl kommen ae^ra- oder ehr *Feuer* auch nicht vor.
*j Nicht gehört hierher syr XOPDi tal«»- NDVNi Nnom? Low,
Aramäische Pflanzennamen, 8. 146.
^) Das is in aesma- beruht auf einer 'Verschleppung*, wie in gr.
TTHOfiu., o(i/ur^ etc. (Joh. Schmidt, KZ. 27, 814, Bartholomae, Ar.
Forschungen II, 86).
=== leaf 271
— 250 —
1,V.
1118. i, L Izäfe.
aw. f/at; phlv. /", päz. i.
Das Neutrum nimmt auch Caland, Zur Syntax
der Fronomina im Awesta, S. 24 als Grundform des
np. ? der Izäfe an ').
{^118»''^ yfi oder.
Da die Lesung des entsprechenden, jedenfalls aber
mit %" anlautenden Pehlevlwortes ganz unsicher ist,
so lässt sich keine sichere Etymologie aufstellen.
Die neueste Fr. Müller\s (WZKM. IV, :35(i), der
als Grundform ap. "^adcivd annimmt, ist möglich aber
auch nicht beweisbar. ,, . , ,.
\/fll9. {\)yäd ^Erinnerung, Gedächtniss', yädifär.
aw. yäta- 'Gedächtniss (Geldner, Studien I, 10,
Note 2); phlv. ijät (vd. 19 (96)), sonst äyät^).
Anders Fr. Müller, WZKM. 5, 265.
1120. {lyyäd (Suflix), in hunyäd,
ap. 'data-, vergl. No. 521.
Wl21. yär 'Freund', yärl-, yärwer (Sahn. I, 126 Vers 1117).
V
yäwer^ yawert (AM. 162 Zeile 2; Sahn. I, 219 Anm. 5,
Calc).
phlv. äyär (die Lesung scheint durch haniäyär, z. B.
Men. 2, 77, erwiesen zu werden; der 6-Strich ist
wie in äyät 'Erinnerung ganz belanglos bezw. un-
gehörig), äyünh'^).
Fr. Müller sucht WZKM. 5, 67 noch über das
PehlevT hinaus zu kommen, meiner Ansicht nach
^) Die Wiedergabe der Izafe durcli e im zweiten Paraslprakä^a
(Weber, S. 8) ist ohne etymologischen Wert und kann nicht zu sprach-
lichen Schlüssen verwendet werden; richtig mit / findet sie sich 8. 25
Note 7 und 49 Note 2 ausgedrückt. Mit e (oder vielmehr ye) wird die
Izäfe im heutigen Persisch, so viel ich weiss, nur nach vorhergehendem
hä-i maxfty ausgesprochen, z. B. bende-ye isläm.
^) Phlv. yät ist vielleicht nur umschreibend.
3j Beruht mand. LW. j<T){<nN *Helfer' (Nöldeke, Mand. Gr.
41H Note 2) nur auf einer falschen Päzendlesung? Aber np. yärer?
```


## [2026-09-05T20:25:48.833Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; ls | grep -i \"^BQT\\|^MON\\|^ARY\\|^SOD\\|^IRN\"; echo ===; grep -n \"syn\\.\" HRN.txt | head -5",
 "description": "List BQT files"
}
```


### [2026-09-05T20:25:48.889Z] TOOL RESULT

```
Exit code 1
BQT_alt_v1.txt
BQT_dli_part1.txt
BQT_v1_djvu.xml
BQT_v1_pages.txt
BQT_v1.txt
BQT_v2_pages.txt
BQT_v2.txt
MON_part1.txt
MON_part2.txt
SOD_pages.txt
SOD.txt
(eval):1: == not found
```


## [2026-09-05T20:25:49.593Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[130][:2200])\nEOF",
 "description": "Horn page 109"
}
```


### [2026-09-05T20:25:51.484Z] TOOL RESULT

```
-- 109 -
will auch np. /äsdk (jüd.-pers. T^^Z, Is. 7, 24) heran-
ziehen.
490. xiSm, xesm *Zorn*.
aw. aesma- 'Zorn*; phlv. /ism, x(h^fi^'
491. yi^eSTn 'bläulich, blauschwarz'; vergl. x^sisar (äähn. I,
157 Vers 510).
aw. a/saena- (Darmesteter, Et. ir. II, 53); phlv.
/asTn (Jamaspji, Pahlv. Dict. II, 421; falsch asgun,
asTu, 241), ;^ai;fm« oder axsin(?), vd. 22 (12).
kurd. stn, heslu 'blau ; afy. s7n bezw. xtn; oss. ä/sinäg
'Taube (46; vergl. Hübschmann, ZDMG. 38, 427/8);
sar. xoin, siyn. soin 'blau, yidg. ayßin (Tomaschek,
BB. VII, 204).
492. lele {jule) 'Wunde, Spitzes; Geschwätz', /ehden,
aw. hareöis; phlv. havak bezw. yarah^ vd. 2 (89).
Die Etymologie stammt von West (PPGl.s. vJialeh);
die Bedeutung der aw. und mittelp. Worte ist unsicher,
ebenso die Grundbedeutung des neupersischen. Im Men.
fasst West päzJiala als 'foolish, silly'. de Lagarde,
Beitr. z. altb. Lex. 38 wollte aw. /"ara- * Wunde' ver-
gleichen.
493. %ufn^ ;^Mw/;, yiimh Topf, Krug , /umre (HIOID, Is. 13, 12).
aw. /umba- *Topf ; phlv. yurnb*^ ai. Jcmnhhd',
kurd. LW. /um: bei. kumb, n. fftimh 'Teich, Pfuhl;
mit Wasser gefüllte Vertiefung im Felsgestein* (204);
wa/. Imbun,
494. fmkde 'Gelächter, ymdtden.
phlv. /andlta^i, yandak (PPGl.).
kurd. kenin 'lachen' ; bei. kandag, n. Uanday, yanday,
LW.') handag (186); wa/. känd-am, sar. söwrf-am (?).
oss. d. ;^odww, t. ;^wd/w (303) scheint hiervon ge-
trennt werden zu müssen und zu [/^svad- zu gehören.
Oder ist doch Urverwandtschaft vorhanden?
ffindeq 'Graben' siehe s. v. kenden (No. 869).
») Vergl. Bartholomae, ZDMG. 44, 550.
I
```


## [2026-09-05T20:26:00.508Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor i in (209,210,211,212,213):\n    seg=t[i]\n    print('=== leaf',i, seg[:600].replace('\\n',' | '))\nEOF",
 "description": "BQT vol2 around p.754"
}
```


### [2026-09-05T20:26:02.360Z] TOOL RESULT

```
leaves 684
=== leaf 209                                                                                                 ‫یوا‬ |  |  | ‫‪٩‬‏ ‪-‬‬    ‫ند‬ |          ‫زبان‬ |             ‫دانوتن‬ |                  ‫که در زیربغل جامه و می‬              ‫باشد ‏‪٩‬وآن‌یز؛ کوچکی‌استکه در میان‌آن‬ |              ‫ویمعنیآینه زالو هم‌آمده امتا ‪۰‬‬          ‫بافته بسته باشند‬       ‫شم‬ |                                                                              ‫رنیبا‬ |                                                                                  ‫بسما‬ |                                                                                    
=== leaf 210            ‫‪۷‬ی‬‫‪۲‬‬ |  |  |  |                                                                       ‫خشتنشار ‪ = ۱‬بفتح اول وشین نقطه‌دار‬ |  ‫کنابه از زر بر ه‬          ‫‪-‬‬   ‫کردن‬          ‫خشخاش‬                   ‫بالفکشیده بر وزن بهمنبار ‪ .‬مرغابی بزر گی‬ |                                              ‫ریزه کردن باشد ‪.‬‬        ‫است تیره رنگ و میان‌سراوسفیدمیباشدوبتر کی‬ |                                                                                                 ‫قعقلداق خواند ‪.‬‬ |  | ‫وسکون دوشین وبك نای قرشت * بمعنی خشت‬ |  ‫شد‬        ‫خای‬   ‫دو‬    ‫نکش‬       ‫‌‬   ‫‪5‬‬   ‫خشت‬        
=== leaf 211   ‫دهان‬    ‫خك‬                                                                                                     ‫‪۳‬و‪۷‬‬ |  ‫مازه ‪ ,‬شاخهای خشکی را کوبند که از درخت‬ |       ‫‪-‬ت دگرخفتتهر‌ااند ‪.‬‬ ‫ودس‬‫پاشن‬ |                                 ‫وده ب‬ |                                     ‫برب‬                          ‫وزن‌دزد(‪ )۱‬افثار » نخود و ماش و عدس و باقلا‬ | ‫حشت لسشجتالورست که اوراسنگه‬                                                               ‫ناد ‪.‬‬   ‫نتر‬ |                                                                                                     ‫و]‬ ‫گثال‬ |         
=== leaf 212     ‫‪4‬‬ |  |  |                                                                 ‫خشثك دیش د بکر رای بقیطه‬ |                                             ‫‪.‬‬   ‫خممر فزق‬       ‫و سکون تحتالی و شين نقطه دار ‪ .‬بمعنی مکر‬ | ‫خشاث مغز = بمعنی‌خنك سراست که‬                                   ‫وحله‌وفاق وفریفتن وبازی‌دادن وبهانه کردن(‪)۱‬‬ |                                                                ‫وخشکیی رایزگونند که بر‬          ‫_‪)۲‬‬ |                                                                                                  ‫دن(‬ |                                                              
=== leaf 213                                                                                                                 ‫‪۷۲‬‬ |  |  |  ‫بزر کهتیرء رن میانسرسفید باشد و ترکان‬                            ‫خشی ه بنتح اول بروزن چمن گ‪.‬یاهی‬ | ‫قثقلداق میگوبند ‪ ۰‬وبضم اول نیز درست است "‬                         ‫باشد کهاز آن جامه بافند و فقیران ودروشان‬ | ‫و بشاین نقطه دار همآمده است چه در فارسی‬                           ‫پوشند ‪ -‬وبکر اول مخفف خشین است» ‪ ۰‬آن‬ |  ‫سین وشین هردو بهم تبدیل می‌بابند ؛ و بجای‬                         ‫بازبی باشد نه‌سقید وله سباء ‪ -‬ودرعربی هرچیز‬ |  ‫لون بای حطی هکمفته اند کهبر وزن
```


## [2026-09-05T20:26:10.887Z] TOOL CALL #34: Bash

```json
{
 "command": "timeout 900 python3 tools/ref_page.py BQT:754 --image 2>&1 | tail -60",
 "description": "Fetch BQT page 754"
}
```


### [2026-09-05T20:26:12.729Z] TOOL RESULT

```
no scan of BQT covers printed page 754 (see 'scans' in refs_online.json)
```


## [2026-09-05T20:26:15.996Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(json.dumps(d['BQT'].get('scans'),ensure_ascii=False,indent=1))\"; echo ===; sed -n '1,60p' tools/ref_page.py",
 "description": "Inspect BQT scans config"
}
```


### [2026-09-05T20:26:17.873Z] TOOL RESULT

```
Exit code 1
[
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
]
(eval):2: == not found
```


## [2026-09-05T20:26:22.010Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 900 python3 tools/ref_page.py BQT:2406 --image 2>&1 | tail -70",
 "description": "Fetch BQT page 2406"
}
```


### [2026-09-05T20:26:29.449Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 489; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2406.png
REF: BQT:2406  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 489  OCR-lang: fas

هيرك4 -4۹-
که درتمام عمر با زنان نزدیکی نکرده است . هیرون؟ - بکسراول وضم ثالث بروزن
هیرل۱ « بر وزن زبر3 » بچةٌ پز را | بیرون؛ نوعی آزلی‌است وبمربی آنر! قسب‌خوانند
گونند که بزغاله باشد ؛ و بعی کفته اند که | وآن محکم ومیان پرمیباشد. کوبند اکر بهار
همجنانکه بچهٌ کوسفند را بره میخوانند بچهٌ وگل آن بگوش رودکوشرا کر کند وگل آن
شتررا هيرك میگوبند . به پلیةٌ برزده میماند .
یرهنل - با میم بر وزن ربشخند هیری؟* - بکسر اول بر وزن و معنی
یکی از القاب گشتاسب است ومعنی آن عاید | خیرست و آن کلی باشد مرو ف که شبها بوی
وعبادت کننده باشد ۴- یام رودخانه‌ای هم‌هست | خوش‌کند .
درولایت نیمروز۴ . هیز * بکسر اول بروزن حبز است که

۱ - هرن این‌کلمه را ازپارسی‌باستان 2۲1168 ل*#(بکاله)؛ ازاوستابی -87لا» پارسی
باستانی -8۳8ل - (سال) می‌پندارد «اسشق۱۱۱۹* و هوبشمان این وجد اشتقاق را درست نمیداند
«هوبشمان ۱۱۱۹ شغنی‌کاکالا (ليك نمو کرده, کوسفند نر؛ فوچ) «اسشق۱۱۱۹>؛ کردی لفط
(میش بی‌دم ) لا بژاد درروم ایلی مت ] «زابا ص40۷ . «هبرك. بزغاله»«رشیدی» ۰

۴ - رشیدی کوید : «هین » آتش » و هیرکده یعنی آتشکده و هیربد و هیرمند آتش
پرست که ملازم آنش باشد - و هیرمند لغب کفتاسب" بواسطةٌ ملازمت آتش پرستی» . رك : حه
س4 . هرن 138۲13600 را در ذبل «هیرید» ذ کر کرده , لوید: کلمه مشکوکست «اسشق
۵ ولف‌هیرمند 18۳21886آر1 بمعنی‌آتش پرست آورده » بانکاه يك بت فردوسی وآنهم
درخ دیگر بجای هیرمند «هیربد» آمده, وبمعنی لقب کشتاسب هم درفهرست ولف لیامده‌است.
دراوستا هم بدین معابی لیست. رك: ح۳ .

۴ <هلمند. دراوستا - 11881082821 (نام رودست. فیلمند), افغابی 8817۸8۵,
درترجمهٌ ساسکربت ۵81۵7280 «بارتولمه ۹-۱۷۲۸؟*۰ دربونانی ۳1782800708 «داثرع -
الممارف اسلام . فرانوی ج ۱ ۱۵*۰ ستون ۱ حوضهٌ رود هامون که شامل قمتی از ابران
واففاستان وبلوچستان است قریب 0۰۰۲۰۰۰ کیاومتر مربع مساحت دارد طول رود هیرمند قریب
۰ کیلومتر وطوبل ترین رود واقع بین سند و فرات محوب میشود. وی در*۹ کیلومتری
غربیکابل در کوه باباسرچشمه میگیرد وراه تاریخی بامیان وپیشاوربفاصله ۲۰ کیلومتر ازسرچشمة
هیرمند ازروی آن عبورمیکند. این‌رود درقسمت علیا بسیارپرآب ودرزمین داور عرض آن‌به۹۰۰
هتر میرسد ودرتابستان از۳*۰ متر کمتن نمیشود. شمبةٌ مهم‌آن «ارغنداب» (۸.م.) است که‌م رکب
ازچپارشعبهٌ مختلف میباشد. ر4: کیهان. جغرافیای‌طبیمی ۹۹-۹۳. رشیدی کوبد: «صاحب قاموس
«دندمند» تصحیح کرده و وجهی ندارد.» ۴ - «هیرون, نوعی ازخرماست وکوبند مراد
ازو قسب‌است.» «تحفةٌ حکیم‌مژمن( «وقسب, خرمای‌خشك که دردهان ریز ه کردد.» «منتهی‌الارب»
ورك: دزی ج۲ ص۶۸ ۷۷: هیرونی. فرهنگه نوسان «قب» را قسب خوانده بممنی لی کرقته‌اند |

۵ -*- خیری (ه.م.) «رشیدی» .
```


## [2026-09-05T20:26:49.866Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i in range(205,225):\n    if 'خشم' in t[i] or 'اهریمن' in t[i]:\n        print('leaf',i,'khashm count',t[i].count('خشم'))\nEOF\necho ===; grep -n \"hirek\\|hīrek\\|yāirka\\|yairka\\|hirak\" HUB.txt | head -20",
 "description": "Find khashm in BQT v2; Hubschmann hirek"
}
```


### [2026-09-05T20:26:51.621Z] TOOL RESULT

```
Exit code 1
leaf 212 khashm count 5
leaf 213 khashm count 4
leaf 215 khashm count 1
leaf 223 khashm count 1
leaf 224 khashm count 1
(eval):8: == not found
```


## [2026-09-05T20:26:54.548Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (212,213):\n    print('===== leaf',i)\n    print(t[i])\nEOF",
 "description": "Print BQT v2 leaves 212-213"
}
```


### [2026-09-05T20:26:56.418Z] TOOL RESULT

```
===== leaf 212
    ‫‪4‬‬


                                                                ‫خشثك دیش د بکر رای بقیطه‬
                                            ‫‪.‬‬   ‫خممر فزق‬       ‫و سکون تحتالی و شين نقطه دار ‪ .‬بمعنی مکر‬
‫خشاث مغز = بمعنی‌خنك سراست که‬                                   ‫وحله‌وفاق وفریفتن وبازی‌دادن وبهانه کردن(‪)۱‬‬
                                                               ‫وخشکیی رایزگونند که بر‬          ‫_‪)۲‬‬
                                                                                                 ‫دن(‬
                                                                                                   ‫شرد‬
                                                                                                     ‫اآو‬
                                                                                                       ‫بذر‬
                                                                                                         ‫وع‬
              ‫بی‌ته ودیوانه‌وش وتند خوی باشد ‪٩‬‏‬
                                                                                      ‫روی زخم بسته شود ‪٩‬‏ ‪.‬‬
‫خشکنانه ‪ = ۲‬بانون‌بر وزن موربانه‪.‬‬
      ‫نانیراگوبند که آنرا بی‌نان خورش خورند ‪.‬‬                  ‫خثك ر بشه » بنتح تن فرتت ‪۱‬‬
                                                               ‫بمعنی بهانه کردن و عذر آوردن باشد چنانکه‬
‫خشکنای « با ون بالف کشد‬                                        ‫اکر گوند خنك رشه میکند مرادن ‪,‬اشد‬
‫زده » نای کلورا گویند ‪ ۰‬و بعربی حلقوم‬
                                      ‫بتحتانی‬
                                                               ‫که بهانه میکند ‪ -‬وخشکی روی زخم را نیز‬
                                                    ‫خوانند ‪.‬‬                                            ‫کو‬
‫خشکو اھ » باواو ‪.‬بر وزن و ععنی‬
                                                               ‫خشکسار؟ ‪ -‬باسینبی قطهبروزن‬
      ‫خشکفاست که نانخمیر برتیامده وفطیرباشد‪.‬‬                   ‫بردبار » زمینی را گوبند که از آب دور باشد ‪-‬‬
    ‫بضم اول‌وفتح کاف" معروف‬              ‫جخشکه‪۹‬‬                       ‫و زمیلی که باران برآن لباریده باشد ‪.‬‬
‫است کهپلاو بیروغن باشد ‪ -‬وآرد گندم نايشته‬
                             ‫را نگیوزیند ‪¥.‬‬
                                                               ‫خثك سبرف=تح ین بی‌نقطه بروزن‬
                                                               ‫ففل کرء تندخوی ویهوده کوی وسيك ومی‌نه(‪)۴‬‬
‫خشل ‪ -‬بنتح اول والی وسکون لام ‪۰‬‬                                          ‫وسودامی ودیوانه مزاج رگاوایتت ‪۴‬‬
‫نوعی از صمغ است و انرا مقل گوبند و بمقل‬
                                                               ‫خشاث شا نه ‪ -‬باشین نقطه دار بالف‬
‫‪۰‬‬    ‫را افع ‪,‬اشد‬   ‫تواسیر‬       ‫‪.‬‬       ‫ازرق مشهور است‬
                                                               ‫کشیده وفتح نون ک»نابه از مردم متکبرباشد ‪.‬‬
‫و بمربی خضلاف خوانند و بضی کوبند خضلاف‬
     ‫درخت مقل مکی است ‪ .‬افهاعلم (‪۴. )4‬‬                         ‫خثك عنان ه بکر عين بینقطه ‪.‬‬
                                                                  ‫کنابه از اسبی است که فرمان بردار نباذد ‪.‬‬
‫خشمن*'۔ بکر اول و میم بر وزن‬
       ‫چ رکن » خشمگین و خشمناك را گونند ‪*.‬‬                     ‫خشگفا* ه بافای بالف کشیده " نان‬
                            ‫‪.‬‬       ‫دن‬
                                     ‫ر‪:‬‬‫کچش‬
                                         ‫(‪ )۲‬چك »‬                       ‫(‪ )۱‬چك ‪ .‬چس ‪ :‬آوردن ‪.‬‬
                   ‫(‪ )4‬چك ‪ -:‬افناملم‬                       ‫چك دش تسیود کر ر رار ‪:‬‬
    ‫‪ _ ۴‬از ‪ :‬خشك ط‪ -‬سار‬                    ‫رش ‪۰‬‬         ‫‪ ۴‬رکه‪:‬خك‬          ‫‪.‬‬   ‫رشه‬   ‫‪:‬ختك‬    ‫رک‬    ‫‪۱‬‬


     ‫© _ از ‪ :‬خثك ‪ +‬فا( = وا باءیمعنی بخته) «اسفا‬                     ‫رك‪ :‬خشككث‌مخز‬     ‫‪۴‬‬        ‫(یوند مکان)‪.‬‬

     ‫‪ - ۷‬معرب آن خشکنانم‬                        ‫خشك سر‬
                                                     ‫‪ ۷‬رك ‪:‬‬                   ‫‪ ۲ :۱‬ص )‪٩۷‬‏ ورك ‪ :‬خشکوا ‪.‬‬
          ‫خشکنا («‪.‬م‪.).‬‬     ‫=‬       ‫‪۸‬‬           ‫‪.‬‬    ‫ج اص ‪۳۲۷۳‬‬    ‫وخشکنايك (یكن نون دوم درحردو) دزی‬

            ‫‪ ۰‬در پهلوی ‪03000‬اعنتا (خشمگن) ‪.‬‬               ‫‪ - ٩‬از ‪ :‬خشك ‪( ۲+‬لست)‪. ‎‬‬
     ‫‪ ٥‬یکشخ ‪ -‬مطب زا[روا ‪ :‬كشخ ی‪) +-‬یردصم( ‪ ].‬یولهپ هاتان‪5‬اتاعات ‪‎‬سانم ‪» ۲۷۷‬‬
                          ‫تسوبی » یرتدض ‪ -‬مدع ‪-‬تفاطل متخسو‌یگنتی هک زا ندماد ناراب ‪‎‬دشاپ ‪.‬‬
     ‫رکب لوا » یولپپ طقیطصص ‪ .‬طنءطسم ( ‪‎‬زیر ‪‎ êshm‬سان ‪.( < ۲۷۳‬‬                              ‫‪‎ ٥‬خشم‬
    ‫اوستا ‪ * 30۳11502 -‬بارتولمه ‪« » ۵۳‬ییبرکه‪ ۷۰۱٩ ‎‬؛ غضب و قهر ‪ :‬پ«ادشاهی بکشتن بیگناهی‪‎‬‬
      ‫غیه در صفحا ‪۵۵۷‬‬

===== leaf 213
                                                                                                                ‫‪۷۲‬‬


 ‫بزر کهتیرء رن میانسرسفید باشد و ترکان‬                            ‫خشی ه بنتح اول بروزن چمن گ‪.‬یاهی‬
‫قثقلداق میگوبند ‪ ۰‬وبضم اول نیز درست است "‬                         ‫باشد کهاز آن جامه بافند و فقیران ودروشان‬
‫و بشاین نقطه دار همآمده است چه در فارسی‬                           ‫پوشند ‪ -‬وبکر اول مخفف خشین است» ‪ ۰‬آن‬
 ‫سین وشین هردو بهم تبدیل می‌بابند ؛ و بجای‬                         ‫بازبی باشد نه‌سقید وله سباء ‪ -‬ودرعربی هرچیز‬
 ‫لون بای حطی هکمفته اند کهبر وزن بدیدار‬                                                             ‫درشت را گوشد ‪۳‬‬
                                                   ‫باشد ‪.‬‬         ‫خشنان ‪ -‬ب باضمول بر وزن برهان ‪۰‬‬
‫‪ -‬بر وزن بلنگ ‪ ,‬زاغ سر‬                    ‫حشنگ‬                                       ‫فرخنده وخجسته ومبارك راگوبند ‪.‬‬
‫وسر کجل و کجلی را کوبند ‪ -‬و مردم کچل را‬                           ‫ک=نابه ازمنافق‌بودن‬            ‫دن‬
                                                                                                  ‫شیلو‬
                                                                                                     ‫ش‬ ‫خ‬
                                           ‫تگبفزته‌اند‪.‬‬                                             ‫وطاق کردن باشد ‪.‬‬
         ‫‪۱‬‬       ‫‪۲‬‬     ‫معیم ‪. _ ۵‬‬
 ‫حشنو = بامول والك بروزن‌پر کو‪.‬‬                                   ‫خشی خاله = بروزن‌طر بخانه‪ .‬خانه‌ای‬
 ‫مخفف خشنود است که راضی وخوشحال باشد ‪۰‬‬
                                                                  ‫‪۰‬ویند که ازتی بوربا سازند ‪ -‬و خانه‌ای رانيز‬
                                                                                                            ‫گ‬
                    ‫ویفتح اول هم درست است ‪۴#.‬‬                      ‫گته‌اند که بر در ورنجرءآن خار شتری ندند‬
  ‫حشنی ‪ -‬بضم اول و کر الك بورزن‬                                    ‫و آب بر آن پاشند تاهوا و نیم سرد درون‬
                    ‫‪.‬‬        ‫ند‬
                              ‫وهبرا‬
                                  ‫گحش‬
                                    ‫معطی » زن فا‬                                                                         ‫ی‬
‫واو ‪۰‬‬    ‫بصم اول ونانی وسکون‬          ‫=‬   ‫حشو‬                     ‫= بقتح اول باسن بینقطه‬            ‫ر‪۶‬‬
 ‫مادر زن ومادر شوهر باشد ‪٩‬‏ ‪ -‬ویقتح اول در‬                        ‫بمعتی خشتنشار است که مرعابی‬            ‫بروزن طلبکار »‬



  ‫‪«- ۴‬خدن‌بروزن كتف سعتی‬               ‫ورك‪ :‬خشن‪,‬خشنار‪.‬‬                  ‫حشن سید نود“ «لفت‌قرس ‪۶‬‬          ‫‪ ۱‬کے‬

  ‫را شتافتن بخاتهاء‬      ‫بینم که مردمان مر گرمای‌سخت‬                  ‫‪#‬اهم‬       ‫‪۴‬‬    ‫ت‪۱‬شرح‌قاموی*‪.‬‬
                                                                                                  ‫ت»‬‫سس‬
                                                                                                     ‫شت ازهر چىز ا‬

  ‫زیر کد‪ .‬وخشن خالها رخوردن‌طعامپا | وشراب ها که حرارت طبیمی راازترا کیب مردم رفع‬
  ‫از ‪ :‬خشن‬      ‫‪۴‬‬               ‫‪,‬‬   ‫خش ‌خاله‬   ‫‪:‬‬   ‫رك‬                 ‫‪« €‬جامع الحکمتن‬          ‫‪...‬دقع همی کنند ‪.‬‬


  ‫ماو‬    ‫‪ .‬لفة حعمی «دارندة (سر) آبی شیاه وه‬                     ‫سر‬    ‫طم ار( =‬           ‫‏‪ERE‬‬
                               ‫‏‪E‬‬                           ‫سل‬                                               ‫أست‬     ‫مرعی‬

         ‫عقاب تیز برباید (ارباید‪ .‬دهخدا) خشنار‪».‬‬                             ‫از آن کردار مکرودم رباید‬
  ‫«لفت فرس ‪.*۱ ۶۲‬‬

  ‫خسو ‪ ۰‬خرو «اسفا! ‪ ۲ :‬ص ‪۰ ۵۸‬‬                           ‫‪۱‬‬             ‫_ مخفف « ختنود“ «(‪.‬م‪. ).‬‬                ‫©‬
             ‫‪ .‬زن مادر بود ‪ .‬فرخی (سستالی) گوید‪: ‎‬‬                     ‫رك ‪ :‬خرو وخوش ‪«:‬خخو‬               ‫و‬        ‫‪۶ “°‬‬   ‫‪AA‬‬

                ‫حنگجویرا دماد ‪۰‬‬             ‫خشوی‬                             ‫ی‬   ‫دشاات‬    ‫کا سگال خو و‬


  ‫«لفت فرس ‪۸۰4۰‬‬
  ‫سم اول ‪ ۰‬اوستابی_ ‪ . 212000۳5-011‬بازند ‪ , 0001152۷2‬پهلوی‬                                        ‫‪ ¥‬خحشنو و‬

  ‫خو هال ورك‬            ‫اض‬     ‫ار تولمه ‪۸۵6‬‬             ‫‪۸‬‬   ‫راضی) «اسفا! ‪ ۲:‬ص‪. ۳۸ ۰ ۷۱ ۰ ۱۳‬‬          ‫(‬  ‫‪1‬‬
                                                                                          ‫‪٩‬‏‬    ‫تق‬
                                                                                                 ‫‏‪۵۰٩‬سو‬
                                                                                                    ‫هوشمان ا‬

                                                                                                   ‫‪۶۵۷‬‬       ‫حه‬
                                                                                                              ‫صهفاز‬
                                                                                                                  ‫قی‬
    ‫‪۲۵‬‬    ‫گلتان‬
              ‫» «‬        ‫‪.‬‬   ‫داری زبان خود میسند‬             ‫خشمی که‌برمن‬        ‫بموج‬     ‫فرمان داد ‪ .‬گفت ‪ :‬ای ملك‬

         ‫خ‪٥‬شمگیی_ [از ‪ :‬خشم (ه‪.‬م‪ + ).‬کین ( پسوند اصاف) ] غضبناك خ»شمناك‪. ‎‬‬
  ‫‪xishm_ nûk‬‬            ‫‪٥‬انمخخ ل ‪: -‬زا[ مشخ )‪.‬مه( ‪ +‬كان دنوي( )فاصا ] ‪‎ +‬یوله‬
                                                    ‫‪.‬‬       ‫؛ غضبناك » درخشم ‪ »,‬خشمگن‬           ‫‪4۸۱۰‬‬     ‫د اسفا‪۷ : ۱‬ص‬
```


## [2026-09-05T20:27:07.855Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"aesma\\|aêsma\\|aēšma\" BRT.txt | head -10; echo \"=== yar\"; grep -n \"Jahr'\\|,Jahr\\|Jahr\\b\" BRT.txt | head -20",
 "description": "Grep Bartholomae"
}
```


### [2026-09-05T20:27:07.925Z] TOOL RESULT

```
2726:i.  aesma-   m.    'Brennholz',   Flur,    und
13329:•  j.  däityö.aesma-  Adj.  'die  gehörigen Brennhölzer  habend,  daraus  bestehend': aEsmsm  (sd.)  'smam  "  N.  /oj.
13330:vKorapA.  —  Pü. :  'fehlt.  —  ')  AP.  auf  kollekt. AS.  belogen;  s.  aesma-  No.  i.
13351:vKonipA.  —  Pü, :  fehlt,  —  0  Auf  kollelcL  AS. , bezogen?     S,  aesma-  No.   1.  |
18931:mit  fra  'herzutragen,  -bringen  zu  — ' (Akk.):  aesmanqmat  .  .  vasyäi/ (sd.)  .. ratSu^ nmätism /rSnSsayata{'i2.1)  K.3. 5;  5.
19489:•  j.  maesma-  m.  'Harn',  als  rituelles j  Reinigungs-  und  als  Heilmittel  verwendet*';
19493:■  j.  maesman-  n.  'Harn',  als  Rcimgungs- und  Heilmittel'':  Ävam  tanüm  pairi.- yaozdat^Ua  gius'mana  apäca  paiti  avd^a
22152:vaesma-
24858:•  j.  rao^as.caesman-  m.  EN.  eines  der sechs  Genossen  des  SaoSyant  bei  der Auferstehung,  Ralav  des  Karsvar  Art- ta/iT'^:  'mariß  a/aeirS  \'t.  1^3.  128;   iii.
26533:•  j.  staoyah-'*  Adj,  'der  umfangreichere, stärkere,  grössere':  aesmanqmcit . .  vazyäis (sd.)  stais'ca  'yJbls  A.3.^.
=== yar
2613:emes  Lingenmasses ;  s.  No.  a.  -  ')  M.l  dem  Lehrern  je   ein  Jahr    larig  gehen;  v^l-  -.iTiter
3797:•  j.  aiwLgäma-  m.  r)  'Winter';  fra  hama (stL)  iocinte  aHa  'me  V.j.io;  —  hama.. °me  "während  des  Sommers  . .  im  Winter" F.  2jb;  V.5.4a,  75.45,  "-^.46,  47,  4^'\ $0,  j/,  103'.  3)  sva,  'Jahr':  hasannm •manqm  Yt().  lo;  ig.2^,  V.  2.41.
3988:*)  Mit  dei  ersten  Anlegung  der  Gürtelschnur (heute  iiuti)  volliieht  sich  die  Aufnahme  des jungen  Ma^ayasHa  in  die  Religionsgemeinde. Sie  geschieht  jetzt  nach  dem  7.,  früher  nach dem   15.  Jahr,  vgl.  Yt.  S.   13    (unter  ayav-)    und
4536:•  j.  an-us'kante  Inf.  'nicht  (wieder)  aus- zugraben':^j/  aitika  zsmS  nikante  spsnasifa irista  ,  .  ttaimtm  yär3.dräjS  an'  "wenn man  hier  in  die  Erde  eingräbt  tote  Hunde und  . .,  ein  halbes  Jahr  lang,  (um  sie  nicht sva.)  ohne  sie  wieder  auszugraben"  V.  J.36.
5920:•  j.  a-sravayant-  Adj,  'nicht  vortragend, aufsagend,  rezitirend';  a)  mit  Akk.:  yB gaisS  (NS.)  'yS  tiaimpm  yäri.dräjJ  "wer  die G.  ein  halbes  Jahr  lang  nicht  aufsagt" N.  44;  41-45''.  b)  ohne  Obj.  '(die vorgeschriebenen  Gebete)  nicht  sprechend': yS  salte  haurvqm  tarasca  xsapatum  ayo' Z)mns  °yif  amarä  V.  /Ä  5 ;  —  *frasrävüy3 rüiufris  tidit  *'°yS'^  N.  104.
6106:slahe  a)  (nändich  ma)  heisst  der  2.  Monat im  Jahr:  pait^aca  cdiwansatimca  tnaiyji- xar7mayehe  (sd.)  'saht  vaAisiaAe  dd^tisS ^3-  7-  ß)  (nämlich  ayari)  heisst  der
7429:Adj.:  h5  imqm  ztim  aiwihiai  . .  mtyae- janS /ri>a  sp»nta  'matte /raca  sva  ..  V. 2. 10;  —  yazamaide  iwam  maf'^a/um (sd.) yam  °tim  sp^ntqm  Y. /o.  10.  a)  auch einfach  sva.  'Erde':  'äirisum  spmtaya  'tsis rar^na (sd.)  apayasaite  V.  ;Ä'.64;  —  avt titn  spayät{%&.)  sptntayh  °tsii  timS  äca  V. 3-35-  Anhang  zu  A.  tJrmaisi s"  d)  {nsimi. mif)  heisst  der  i2.Monat  im  Jahr:  sp>ntaya 'tsii  mSrshs  Vd.  2/.  ß)  (näml.  ayan)
10730:ntanauhl  '%r3J  hcUü  paitt.mraot  asä  kuL- haxa  Y.32.  2;  —  mazdä  , .  vokü  uxfya (sd.)  manavAä  °hr3  aiälä  ustä  tanüm Y._jj.  10;  —  yahmi  spfntJ  %wä  mainyU urvafse  jass  mafsds  "ärä  ahmt{s,A.)  voha mananha  Y.43.6;  —  aAmäicä  «ärJ  (als Sah].)  ^^ /asaj  (sA.)  mananha  voha  asaüä Y.3Q.  7;  —  ahmsi  dqn  (sd.)  .  .  mazdä •^rJ  armaitf  ahurS  Y.  47.  i;  —  kj  binx- 'iqm  täil  ''hrJ  mal  ärmaitim  ^..44.1;  — kada  masda  ala  mal  ärmai/i/ /imaj  (sd.) •^ra  Y.48.11;  — yqm  Asi  °'^ra  voAuäi cdiit  (sA)  tnananhi  Y.^o.y,  —  mazdi dadät . .  haurvat3  aminlätasca  . .  asahyica ..  •UraAyä  sarS  (sd.)  Y.^jj.ai.  a)  im YHapt,  mit  va^hav-K^y.as>m..vahist>m ..vohuia  maiid ..  vokucä  '"hrsm  \.3~.i,i.\ —  asäatcä  hacä  varahsuseä  mananhs  vatf- ksusca  'hrai  Y. J5. 10.  a)  im  jAw.,  mit va i rya- Adj. :  '^rtm  vairTm  amihm  sptn- hm  yazamaide  S. 2.  4 ;  Vr.  20.  i;  —  ahurS mazdä  . .  vohu  manö . .  ahm  vahist»m  .  . ''i:r>m  VairTm  .  ,  spmta  ärmaitis  .  .  Y. 57.  24;  1.1  f.,  /tf.  3,  Yt/.  25,  4.  i;  —  ahu- rake  maxdä  .  .  vanh^us  mananhB aiahe ..'"hrahe  vairyeke..  Y.70.2;  —  aku- rai  masdäi  . .  aläi  . .  °^rai  vairyät  armatSe V,  iff.  iii  G.J.  s;  —  vaAu  manauha  haH- mnS  aläca  .  .  '^r3ca  ya  vairya  FrW.  /, I ;  —  viscihnm  dim  ayasata  Syapta  (sd.) ■ira  vairyaY.2Q-^(J\  k)  xlaiirahe  vair- yeht  a)  (nämlich  mS)  heisst  der  6.  Monat im  Jahr:  pancaca  haptaitttn  *pailisJiahyehe (sd.)  '"hrahe  vairyehe  anayranqm  A.  3. 9.  ß>    (nämlich    ayani)    heisst    der  4.
12268:Ais  srayataAai  h(üa  vourukaiat  äaf  maf/a us.fravSfite  .  .  Yt  Ä  40;  —  ~'y^e  stärS raevat5  i^armauuAatS  YtS.  o,  56,  57,  Y. I.ii,  27.2;  —  'rim  drvB.caimamm  Yt ■Kr 2,  Ny./.8.  a)  Hstryehe  a)  (nämj. mä)  heisst  der  4.  Monat  im  Jahr:  xA/aäim *mailysiümahe  (sd.)  'ryeke  da^usS  A.  3. 8.  ß)  (n��ml.  ayan)  heisst  der  13.  Monats- tag: 'ryeie  stärJ  ra^fa/ff  s^armanuhaiS S.Z.  13;  vgl.  2.13,  y.i6.4.
12660:—  haca  '%ulat  mazdi  Yx. $.  7; —■  ys  °%va sf^nts  mainyus  \L  10. 143;  — '^usS  'dtisö dadOibÜ  (s.  o.)  raocibls  Y,  j&6'';  — *xi»ümaine  '%usS  N.  4j.  a)  da'äusS et)  (nämt.  mä)  heisst  der  10.  Monat  im Jahr:  aiiaiilm  maihyäiryehe  (sd.)  '"^usö v>r3%rafnafu  k.3. 11.  ß)  (nämL  ayars) heisst  der  8.,  15.  und  23,  jedes  Monats: °^us3  akurake  mazds  ratvalS  . .  S.  i.  8, >S.  23°';    vgL  2.8,  IS,  23,    Y./6.  4-6;
13875:schlechtes  Jahr,  Misswachs  bnogend  -.pairt- '
14853:i)  'fliegen,  sich  im  Flug  stürzen  auf-'  v.j.  11.  2)  in  -/arischer  Art 'einher- {Jaiü  mit  Lok.):  kazanrim  iiunqm  .  .  gehen'<>:  yat  nä  \Jahika\  pasca  panca- mainyavasä  patinti  katiurile  patH  daeva-  1  jasTm  sarn^m  frapalaitii''  anaiwyästa (ad.) t1qmYt.10.119.  2) 'fallen,  hinabstUrzenlj,^  anabdäts  vä  "wenn  ein  Mann  [ein (s.  auch  4):  pairikä  .  .  yü  starö  hnma  Weib]  nach  (vollendetem)  fünfzehnten  Jahr (sd.)  patmOi  aniar»  tarn  asmammca   Yt  !  ^\^Yia  geht  ohne  .  ."  V.  18.  54.  3)  in
15235:•  j.  'pancUi.dasa-')  Adj.  (fem.  'sl)  'der fünfzehnte':  °wm  asat»hqmca  .  .  vahistsm V.  /.  18;  —  dasimB  yat  ahmt  . .  cd^rudasS . .  'sa  (sUtt  NSm.)  Yt.  /.  8;  —  pascä  'sim saniam    "nach   (vollendetem)   15.  Jahr"">
17418:•  j.  by-ä'rixti  Inf. 'bis  irrigare,  (das  Wasser) zweimal  hin  (zur  Wiese)  zu  lassen,  über  zu lassen':  &aj  yaval  zä  .  .  yavat  ai^a  a/s 'ü  upa.üjvariii  frabaväi  "wie  gross  (soll) das  Grundstück  (sein)?  .  .  so  dass  das Wasser  (des  Grabens)  ausreicht,  um  zwei- mal (im  Jahr)  vermittelst  Durchstechens (des  Damms)  übergelassen  zu  werden"  V. ! /4.13'^    ,  ,      I
17419:Zum  V.  raek-,  —  Pü. ;  täk  3  bar  pa  3  baxHhiih (Hds.  ark£t)  pa  3  känakik;  undeutlich.  — : 1)  D.  h.  das  Grundstück  soll  so  gross  sein, ' dass  es  dnich  ÖfTnung  des  oberhalb  gezogenen  j Bewäiserongsgrabens  zweimal  im  Jahr  unter ' Wasser  gesetzt  werden  kann.  1
17822:sae^antätvirshraynaiY.  26. 10; — gSuicä hudätahs  gayehyäcä  mard^nB  .  .  °itm  Y. y-  7;  2j.  a,  26.  S,  Yt  13.  87;  —  «ÄM^ zar^uStrahe  ipitämahe  asaons  -sie  Y.  6S. 22;  3. 2,  4. 23, 16. 2,  23. 2,  24-  S,  7'-  2-  Vr. /ö,  2,  YtÄ  2,  J_J.  87,  Vd.(?;  —  ahe  nars aSaonS  'Jtm  yazamaide  yS  asmffj^ativä nqma  Yt,  /. 30;  13. 95 ff.  (oft),  Y. 23. 2, 26. 5% FrW.  2. 1,  3;  —  hvSuyä  asaonyä  'sim  Yt ''5-^39!  '39f-'*;  —  kanyä  *va}>uis  asaonya [. .]  °slm  Yt  13.  141 ;  141  f.'°;  —  auch  dem AÄM.  und  andern  Gottheiten  wird  eine Fr.  KUgeschrieben**':  vispanqmca  anAqm paoiryanqm  'Sinqm  .  .  °sm  avqm  yqm ahurahe  masda  .  .  °iay5  .  .  ya  ampsanqm spintanqm  .  .  yqmca  ährö  urväzistake  .  . yqmca  sraohhe..yqmca  alnSyqmca  apH.. YtJ^.  80-86;  Y.26.2i.,  V./»?.'4; — äyese yelti  *ä  *fravaM<y)'^  ahurahe  mazdä  am»- sanqm  sparUanqm  . .  Y.  25. 2 ;  —  gaom  (statt Gen.)  agvJS-dätahe  urunB  °Sim  S.2.  I2;i2; —  sogar  den  Fravalay  selber  (!) :  aSäunqm "sinqm  uyranqm  .  .  paoiryjJkaisanqm  'si- nqrrt  nabänazdistanqm  'ünqm  '/ayU  xihaiä ayantu  ahmya  nmaneYt.i3.1s6.  A)/ra- vaHnqm  a)  (näral,  mä)  heisst  der  i .  Monat  im Jahr^:  asäunqm  'sinqmY.i. 11.  ß)(näml, ayar?)  heisst  der  19,  Monatstag:  asäunam 'sinam  uyranam  S.j.  19;  vgl. 2. 19,  Y.10.5. •)*Nach  dem  GrBd.  (s,  DsT.  ZA.  3.  500, Blocket  RHR.J2. 104)  ist  der  Mensch  aus  fünf Bestandteilen lusammengesetit:  ian,yän,  nmän, äiinai  aad /ravakr.  Vom  letzten  heisst  es; y>ti- vahr  an  i  pcs  i  Öhrmazd  i  :^aiäl,  und  über  sein Verhältnis  mm  fiß/ö»  wird  geiagt:  ruvän  S/ra. vakr  pativast,  ku  iän  rm/ä»  marnjcmtan  ne  tiniän. S.  noch  DkB.  269  {218.  6):  io  (fravahr)  haf  lan yut  bavtt  lan  hil  lör  u  aiär  mänri.  Die  Schaffung der  fr.  (bei  West;  "prolotypes,  primary  ideas of  the  good  creations")  ist  nach  Bd.  /.  8, 34.  1 zu  Beginn  des  ersten  Mitleniums  erfolgt;  nach 2.  10  f.  entscheiden  sie  sich,  'lan  tariaiihä'  gegen die  Welt  der  Driig  zu  liämpfen.  Über  ihre,  ins- besondere  kiiegeiischeTäligkeitalsSchutzgeister und  Manen  gibt  das  ihnen  gewidmete  Yt  13 Auskunft.  Ihre  Zahl  wird  Yt.  13.  59  ff.  auf  99  999 eingegeben,  vgl.  jcludra-*)  and  Mx.  4g.  16,  52. 23,  29;  weniger  bestimmt  Yt.  13.  64,  66.  All- jährlich während  der  letzten  fünf  Tage  der sechsten  (letzten)  Jahreszeit  und  der  sich  an- schliessenden fünf  Schalttage  kommen  dieManen, ihre  frühere  Heimat  zu  besuchen  (Yt.  13.  49) und  werden  dann  besonders  gefeiert  (s.  hantas- pa%niae<iaya-)ii).  Vgl.  noch  Cld.  Totenverehrung 48,  BahadoorN.  D.  Khandalawala  Cama  Mem. Vol'  205,  JN.  GIrPh.  2.  643,  SÖDEftBLOM  RHR. 3g.  229,  373,  La  vie  future  7.  Das  Nichtauf- treten  der  fr.  in  den  (eig.)  Gä%äs  (s.  unten  No.  l) ist   bemerkenswert;    zum  Teil   aber   entspricht
18490:•  j.  naema-  1)  Adj.  'halb':  '«am  bay^m Vd.  2;  —  'nam  ySr»  "ein  halbes  Jahr (lang)"  N.45i*44'^;  —  'mmi  yJn.drä/ä "eine halbe  Jahreslänge  (hmdurch)"  V. j.gö, ti.44i  42;  —  paourwn  va  'm^m  yän apar?m  va  "das  erste  Halbjahr  oder  das zweite"  N.  44)  —  pimrumca  'me  asne (bz.  xia/ne)  aparvmca  "die  eiste  Hälfte  des Tags  (bz.  der  Nacht)  und  die  zweite"  V. 4. 45*>.  3)  m.  a)  'Hälfte,  latus  alterum': ya(  vS  'mim  yat  va  'hri^wi  .  .  V,  if ,  32, 16.  2,  Y.  Jp.  7;  V.Äioi;  — aWsr  'mat.. uparät  *mat  y.i4.T,  6'.  8,  N.5_j,  P.  23;  — haoyat  hol  +*mS/3' . .  dalinat  hat  *'mai^ N.  75;  —  '^fraoirilarai  'mat  N.fi?;  — *aevahmat  'mat  N.  7p;  —  paurvat  va 'mat  aparät  va  ^.Jj;  —  antarä^  (sd.) 'm^  V.5.43»,  51,  6.2,  3,  7.77,  8.^1,  42, 104,5.15,  16,  N.öo,  6p',  *7jT,  54,  104^; II';  —  *va  *'ma  N.pp*';  —  vaHbya 'maltiya  "von  beiden  Seiten"  V./_y.3 1—37 PüZ.*;  —  apaxtarat  haca  *mat  V.ig.i, H.2.25,  FrW,/o.43";  V.j^.s,  H.2.7,  A. 4.6.  b)  'Seite'  überhaupt:  vlspe  'mq (AP.)  F.jg;  —  vlspa^työ  'maübys  Yl /0.41;  —  ahmst  'mäi ..yahmäi  'tnanqm YtJO.  19;  y.  3,  V.Ä80;  —  usastaratibyö haca  'maiiiys  V./p.5;  1,  H.2.  35,  V.7.  2, *i6,  FrW.JO.42.
18947:•  j.  n«mata-"  m,  1)  'Reisig':  nasui  tga- 'kaite  .  ,  7flä(i  .  .  'tS  tarS  yan  "die  A''. verschwindet . .  wie  übers  Jahr  das  (dürre) Reisig"  V.p.  46'';  —  avi  Um  spayUt  . . vJspaca  avi  tiyra  *-ia  ".  .  und  auf  lauter spitzes  (dorniges)  Reisig"  V.J.35; — katgAus .  .  äraasca  *'taheca  ayanheca  "die  Nutz- niessung  von  Holz  und  Reisig  und  Eisen- gerät"  V.5.38.  2)  'Geflecht  aus  Reisig, Hürde'  (nur  Komp.),
19646:Eig.  'Mittjahr*;  ir.  *madjiäria-,  haplol.  aus *niaäiai-iär^a  entstanden  (falsch  J  306,  3) Der  Nume  läist  schliesien,  dass  in  ältester Zeit  das  Jahr  mit  dem  Sommersolsliz  begann; s.  Roth  ZDMG.  34-  711,  Gor.  OK.  324.
19662:*)  Ursprünglich  Sommersannwendfest  ist  es später  dem  Andenken  an  die  Schaffung  des Wassers  geweiht. Der  leuteTag(iS. des 4.Monats) ist  der  105.  Tag  des  Jabrs;  mit  ihm  schliesst die  erste  Hälfte  der  auf  310  Tage  (7  Monate) gerechneten  warmen  Zeit;  »gl.  V,  /.  3  Gl.,  Bd. 35.  7.  Heutzutage  ffillt  er  auf  Anfang  Janaar. War  er  in  alter  Zeit  der  Sommersonnwendtag (30.  Jani),  so  begann  das  alte  Jahr  am  g.  Man. So  Roth.  West  und  Dst.  dagegen  setzen  den Jahresanfang  auf  den  Tag  nach  der  Frlihlings-
```


## [2026-09-05T20:27:15.140Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '2718,2745p' BRT.txt",
 "description": "Bartholomae aesma context"
}
```


### [2026-09-05T20:27:15.189Z] TOOL RESULT

```
•  j.  aevö.sarad-  m.  EN.  eines  Gläubigen: !     i,a,änTt  (iö/a«),  '(lu  V.'ji):  /m  nr^Sn  3^Js/är
'irite   -rt'iö  (GS.)  fyuslake  asaonö  "des  0-,  |       bSIan,  (sonst):    jr"jj/Jr  bülanlX    —    >)  Ausser
Sohns   des  ^.,    Sohns   des  .S  . ."  Yt /j.         ^  x,..  ,..__._-_„. ,.        ,.  j._
"5- Lig.  'einiiEMtifi'.
•  g.  aerav-    Adj.    (etwa)    'schimmenid': fiwf'j  ^it^  asnqm  uxsä   (sd.)  agurui  Y,
und  *iSla  könnten  alle  Formen  auch  dem Perfekt  lugewiesen  werden,  S  '62.  —  ')  Them.
—  Ü  Steht  •jf;cäry(sd.)  statt  des  gen.  Inf.,  so lässt  sich  der  Gen.  gäiMiiam  durch  Attraktion erklären;  s.  lu  anujctSf  No.  I.  —  ••)  Hds.  iJti.
—  -■)  Hds.  ii/a.  —  i>)  Hds.  hrn.  —  !)  S  3/S No.  2.    —   S)  Zu   S  37'.    —   *>  Vgl.   Pü.   lu
i.  aesma-   m.    'Brennholz',   Flur,    und
Uiflitized  by  VjOOQ  IC
a?
Sing,  in  kollekt.  Sinn');  'ma  frasaocayähi\     Lavaquellen  enthaltend".    VgL   Bthl.IF.j. V.  *.  7  5 ;  /4-  7 ;  —  a  -man  y'äsamiha  V.  i8.       ■  24-  -  •>  NS.,  S  ^5- »9;  5-z;  — "'«ff  ■■  ^<»"  Y.J.2;  — '«ffJ'Taj«  j.    aezah-    n.    'Verlangen':     "zö    (AS.) baolulmca  Y.^'i,  7.26,  Äi,  22.3;  —  ''ma  J'isatim    aisahe   "sie  (beide)   kamen
(sva.  'nach  dem)  Verlangen  des  verlangen- den" Yt  J5.82'>.
Zum  V.  äs-;  s.  unter  ana-,  —  aL  ihm-  n.  — )  VgL  iKoDstT.  Dbr.  AiS.  185. j-,  g.  'aeä-  V.  'suchen'.  Praes.  3  isa-, a  isa-,  *»Ja-'',  14  b  tfasa-,  aisasa-", 17  (Fut)  aifya-,  30  (Iter.)  aSsaya-;  Perf. iyals-^,  yals-i\  —  PPfP.  isla-,  PFP.  k><7-;
(AD.)  baom  Y.7.2; —  Aa  »i?  bara  'm (AP.)  bansmaca  U.io^;  —  'masca  bam- maca  N.  7/T.;  —  *kava  °ma  (IS.)  Aava bansmana  N.  108-,  — ■  °m>m  aSaya  b^nlsm Y.62.^;   —  yü  °md  (AP.)''  asaya   barat  * V.Ä79;    —    *kva    a/Sqm  (AP.)  ^'mim^    ' paiti.barat    N. /oj;    — ■    cvat    nä    nit?ma 'mähe  patti.barS  ratufri^  "wie  viel  Brenn-    _  .  .
holz  zum  mindesten  darbringend  ist  man  Inf-  <^t^^;  Absol.  'agi?m,  •iünbrn. r.f'  N.106;  —  iat  tä  °ma  (^V.)  yaoz-  i)  '(etwas)  suchen,  suchen  nach  -, dayqn  ar>h>n  V.  7. 28;  ■ — ■  pairi  urvarä-  aufsuchen':  yd  aüm  mainimnö  ahm byasca  varsoäbyasca  'tnaiil^ö  "abseits  von  isimnS  ahm  apa.rao'iayeiU  {sA.)  .  .  dru- Bäumen  und  Sträuchem,  die  Brennholz  jimca  vinasti  V.  7.78;  —  Med.  auch  in sind  (geben)"  V. /6'.  2;  —  Auskam  °m»m  reflex,  Sinn:  vSrrinahe  .  .  yS  vazaite  .  . Y.JI.8; — Auskanqm  ..  'manqm  ,.  nafi-  axsa/hi  {sä.)  xsa/hTm  tsfmnS  \'t  14.  20; tanqm  ..  xraozdvanam  ..  varidvanamY.    ao.  a)  mit  Dat.  comm.:  vlstäspahe  ..
7. 3IJ/5.24,  /.^.  2j3;  —  'manqm  ..husatqm  yö  .  .  asäi  ravö  yaisa*''  .  .  ravö  t'TvaAa A.j.  5';  —  'manqm  yaozdätanqm  Y.t8.  "V.,  der  dem  Asa  ..  Raum  suchte,  .. 19;  22;  —  'mtmi'f  .  .  hüBs  *rat>cas.pai-  'Raxaa  fand"  Yty.gg;  —  äat /rasüspnie ristqm  Y.  62. 10;  —  'mgm^  däityS.aüman  \ .  .  fravalayö  .  .  ap>m  ais^mna^  haväi "Brennholz,  das  aus  den  gehörigen  Brenn-  käcit  näfai  (sd.)  ". .  um  Wasser  zu  suchen hSlzem  besteht"  N.  ioj;   —   aiUm  'mrm  jede  für  .  ."  Yt/_J.66.  b)  ohne  Obj.:
yö  vaoce  *n)ma<,ka  nqma  Yx.14-  55-  balsaz3m  (sd,)  ..  upöisaym  ..yezi  is»mnö
KompA,,  E.  —  Zum  »i.  V,  indhati,  gr.  a:%a.  .  ttSit  vifldaiU  (sd.)   V.  y.36.  2)   'zU    Cf-
Aus  ir.  *ai:ama-,  S5J 1-  8.  —  np.  iiam.  —  langCD  sucheo,   haben  wollen,  begehren,
Pu  :  ^-r«4'.  -    '>  ^f"^"  S.Lg.  mehrmals  angehen':     ^ar^nö  .  .  yat  isat  Jra,?rase
mit   dem  Flur,  des  Attributs  verbunden  vor-  ,,  ,     „  ,~        "        ™
kommt;».  No.  3.  -  ')  llnthem.(?).  -  3)  S.  Y\.ig.$(>;iz;  —  apatat  /raarase  :^ar7n5
No.   t.  —  1)  Das  wegen  des  r  als  gelW.  an-  isö  zara'iuiträi  (als  Gen.)  YL/9.82;  56;
zusehen  isi.  —   äat   vö    kasäl    ma^anqm  .  .  :^ar)nS
•  j.  aesmö.barvtay-  f.  'Darbringuog  von  isa^ta  Yt.  i^.  53;  — yff  naeeim  isaiti  huna- Brennholz':  alvayacif  °niii  (IS.)'*  aiva-  ranqm'V.ij.i9;Aog.48;  —  äiä ..Ayämii , . yacit  bar7sm3.stir?iH  Y.24~  aiavanö  tnsyä  istsm^^  rJiVl'(sd,)  Y.  40. 4;
Pü.!  fsm  bariiniA.  —  D  Hds.  'u.  __  _ya;ja  /g^  isaaa  Vyt/2(?)  a)   mit
•  j.  aesmö.zasta-  Adj.  'Brennholz  in  der  Dat  'etwas  (Akk.)  haben  wollen,  begehren, Hand  haltend,  mit  Brennholz  in  der  Hand' :  erstreben  für  -':  yö  . .  tanuye  tsaite  >rä- yas3  ^WJ  .  .  frayazaite  "stö  Y.62.1;  V.  ^r^m  V.  ij,  19;  —  ä'irava  .  .  manmtam 3.1.  isimtiö  dalnayäi   am^m   iamnö  tanuye
```


## [2026-09-05T20:27:15.935Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"yär-\\|yär\\.\\|'yär\\|yära-\" BRT.txt | head -20",
 "description": "Bartholomae yar"
}
```


### [2026-09-05T20:27:16.029Z] TOOL RESULT

```
3188:*J  Gemeint  ist  die  Zerstörung  des  Thebens  und alles  was  daiil  dient:  die  äaimichc  Gegen- achöpRing  [fiailyäta-)  in  dem  «Äunschen  gaya-. Vgl-  Bd.  I.  [ ;  iuadahiimk  i  ehrmazii  u  palyätak i  süräk  mrniii,  was  wesentlich  das  selbe  besagt wie  g'  ajy'.  Ohne  pa'ilyära-  wären  alle  aiiiri- sehen  Wesen  unsterblich.  S.  noch  Bd.  i.  6: kar  S  Hl  amiar  dahün  i  Shrmatd  tanärakömaH,!  u akanätakSmand  ei  en  an  i  andar  har  2än  meniik patmäii  ('Verlrag'}  däii/iid.  —  Pü.  beiiehl  die Stelle  auf  die  Schiffung  und  Tötung  des  Gaya Maritan.
4869:•  ).  ayan-,  j-,  g.  ayar-  n.  'Tag';  a) Gegensatz  zur  Nacht:  *oim  . .  'yar>  (NS.) tYjasaiti  .  .  a?va  v3  xsapa  Aog.  J/;  ■ — ai»ke  'yan  (GS.)  .  .  airikh  xsaj>ö  \t.  i .-iZ, i/.S;  Vyt.J0(?);  —  hamahe  °yqn  hamayn 1-3  xsa/w  Y.  S7-3I,  Yt.ÄS4;  '  10.  iij  (f), Vyt^f?);  —  vlspsU  'yqnia  (AP.)  xlaf- nas.'a  Y.  57. 1 7,  Yl  /.  i  i  ;  —  *frayaire  "yan (LS.)  bavaiti  (sd.j  hubai,rü  .  .  aia  apare 'y<pi  ■-  Aog.  35;  —  */rayarfne  vä  uza- yariu^fsd.)  va  *'yan''>  N.5;  —  dvadasati- hiinm  (sd.)  asü  *ayrim  °yar)  F.  27  b 27b;  —  °yqn  (LS.)  va  varstafsö  var»t3.vTrt [sd.)JaiJnti  V.S.^.  b)  als  der  Zeitraum von  Sonnenaufgang  zu  Sonnenaufgang: iiz£.a  yan  mainyenie yaty3r)N.2.^\ ^räyö  yara''  Vd.  ly;  <),  if),  si;  —  pasca xsavaidim  (sd.)  yaranqm^a'''  Vd.  f)\  11, '5>  '9  '■  c)  sva.  festgesetzter,  bestimmter Tag:  myazdahe  ''ya''''  (LS.)  "am  Tag  des My:'  N. Si-,  "y:;  *^jj  —  kaia  (sd.)  yiri (AP.)  daxiärS  .  .  drfs  Y.  43-  T,  —  yan ami^näitii&d.)  juye  tanus  Aog.^j.  d) 'Zeit':  vUpI  'yärj  (AP.)  dangö.jyäiöU (sd.)  .  .  "alle  Tage  . ."  Y.  43-  2.
7576:•  p.  *äNitiyära-''  m,  Name  einer  Land- schaft in  Armenien:  */-«*  tiämä"  dahyäuS arminaiy  Bh.  2, 11.
10195:(Inkoh,)7r<ja-'',  z^jayäraya-'^,  3o(Kaus.) gäraya-,  7  +  30  (Kaus.)  yräraya-,  yräyrä- ya-i*;  Tert  1  /ayär-, ßyar-,jayar-.  —  Inf, gairf,  'yrärayd.
10818:•  p.  xäayäräan-'*  m.  EN.  eines  persischen Königs,  Xerxes,  Sohns  Darius  L;  adam 'iä'^  x^äyaiiyt^  *vazark^  ..  dilrayi^va- Aaus  xsJya'iiyahyä pu^^f^  *haxämani^iy<^ X.7.2,  5;  8;  —  %ätly  -ya  x/äyahiy<^  X. i.Z,  4,  2. 3,5.3,  .^.3,  7.3;  —  trura*maedä .  ,  hyJ'  'ism  (AS.)"'  x^yakiyam  akunaui X.  I.  I,  6.  1;  —  -yircahyd'^  dürayJ'va- ''usakyd  x^,lya~^iyaAyJpuk''^^Am.i;  — artax/a'i''aky3  'yärcakyä*'  xläya'hiyahyä />uh''a''ä  Am.  j; —  arioxlayä  'iä^'>  xi'a- ya'hiyt^^'^  'pu^a"  's'a  därayc^va^ui'i^  xla- yaiiyJ^^  piii^"^  Ao.  1. 2.  [S.  noch  zu xarlädafyn^
12099:Ableit  lU  lafä+yär-;  ei  mag  ein  *tarS yän (AP.)  'über  die  Jahre  hinaus'  zu  Grunde  liegen,
13461:*vazarii^..vistäspahyä  pu^^t^  arsamahyä naps  AaxSmaniüyc^  Bh.  1.1;  4.i^,D.i,2, 4- 1,  5. 1,  6.  2,  4,  12,  16,  18,  ig;  15;  X. 3-  3.  7-  3.  Am.  /;  Ao.  7.  2 ;  —  %äliy  'vJ'us xiäya%iyJ'  Bh.  /.  z  ff.,  2.  i  ff ,  J.  i  ff.,  4.  i  ff., j.  I ff,  D. 4-i,  3.  5- 2.  3.  6- 3.  4.  5,  7.  'J. /j.  3 ;  —  a'ura'masdä  .  .  kauv  "v^um xiäydiriyam  adadi^  D.  ^  i;  ö'.  1,  ^j  — 'vahaus  x^ayaHiyaAya  Bh.j.  9,  D.j,  4. 2, S,g,  77. 1,  X.7.  2,  9.3,5;  —  'va''usaAyä'^ vistäspahyä  puäi^tr'^  Am.  1;  —  "xsayär- lahyä  °v<^uhAyä'^  xsäyahiyaAyj  fu^'i^^^ Am.  7;  —  xsayärSä  'vc^us''*  x/äydiiyO**^ pü^''afi  Ao.l.x.  2)  Darius  II.,  Sohns
13785:•  p.  dusiyär-  n.  'Missjahr,  Misswachs': imäm  dahyäum  mä  ajamiyl^  . .  mä  'ram (NS.)'>  D.^3;  —  imäm  dahyäum  c^ura''- mazdä  pätuv  hacä  kainäya  hacä  °ra'  D. 4.3.
13883:Ableit.  aus  *äui-yär-  n.,  vgl.  duiiyär:  narö  .  .  VyL  12  (?).
17421:'hyär-  n.  'Zeit  von  iwei  Jahren',  Komp.:  *hi +yär:  S  ZÄÄ   U.  —  PÜ.:  2  «/  drahnäi. j.  bylyi  N.  43--  lies  bityL
21631:Man  erwartete  *yavärina;  all  Komp.  au«  yma- +*ar3iia-  n.,  eig.  Instrament  zum  Mahlen des  Getreides';  ■.  zn1izJa-undGIrFh./.3ti[. — np. yävar, yär.  — Pfi. :  iur/öt  1  ör/'gemahlenei Getreide'i    erLi    äiyäi  i  fa  datt  '«ine  Hand*
21633:isS;  yär-  —  yäs-  mit  a  1188
24393:—  vJspimca  asmamm  .  .  vlspss{s.  lya strsus  Y.  7/.  9;  —  vJsppm  aa>m  paiti zrv3n?m  F.JJ;  —  vTspimca  tn^nm spfntiiti  yatamaide  "das  ganze  heilige Wort  ■  -"  Y.  77.  s;  6,  20.3,  Vr. /_J.  i;  — "Pfm  (ASn.)  dusmatimca  dtdüxttrnca  duz- varsDmca  V.J.  20;  42,  7.52  PüZ.,  Yt /o. 105',  Y.7;.8ä,  4;  —  'p»n  imal..yat aniar»  zqm  asmatamca  Yt  70.95;  ig.Z, H./.16,  2.2,  V.20.5J;  —  vssp?m  imal karsvan  yat  :i^anira'^»m  H,  /.  14;  Yt 10.  13;  —  vlspitnca  datim  viddySm  Y. 77.  5;  4;  —  %riyßm  . .  naimtm  . .  visptm larB  ''yäri.dräjeklm  N.  42;  —  vTspam vacö  fraväk)m  (sd.)  haurum  vacB  fraväksm Y.  ig.  14;  2r.  2;  —  'pqm  yqm  astvaitlm gai%qm  Yt.  ig.  94;  —  'Pqm  asaonS  stlm (Stverz.)  iaitfm^a  iavaintlmca  büsyeintlmla y.  ig.  9;  usw.;  7/.  9;  — -  vispqm  Avqm lanam  W.S.40;  —  vJiPqmca  aipi  imqm zqm  Y.57.33;  7/.9,  Yt/0.2;  —  vfspqm^a lialnqm  mSzdayasnfm  Y.  71.4;  5,  Vyt /4';
24488:•  j.  vi8pö.ayära-  Adj.  'alle  Tage  während' : v>rfir)m  'yär?m  .  .  iarB.ySritn  "Sieg,  der alle  Tage  währt,  . .  der  die  Jahre  über- dauert" Yt  if).  54.
25922:•  j.  sata-yär-  n.  'Zeitraum  von  hun- dert Jahren':  upa  %wa  hixsaisa  .  .  'ysn ". .  auf  hundert  Jahre  . ."  Vyt.  4j.     Wert-
30472:Ableit  aas  *hu-yär-  n. j.  Au.vaxJ'  N.  46' :  lies  iä  varl".
```


## [2026-09-05T20:27:23.734Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"aēšma\\|aesma-   m\\|aeSma\\|aeima\\|'Wut'\" BRT.txt | head -20; echo \"=== around 21633\"; sed -n '21600,21640p' BRT.txt | grep -n \"yär\\|Jahr\" ",
 "description": "Bartholomae aesma Zorn + yar entry"
}
```


### [2026-09-05T20:27:23.807Z] TOOL RESULT

```
2726:i.  aesma-   m.    'Brennholz',   Flur,    und
13332:Komp.:  •aeima- Aäj.+Sav-,  S  ^ÖJ-  —  Pü.: däli/iä  tsni  iave.
=== around 21633
14:(zu  Yt.  r4):    mii,yäri,    —    D  Zu   %'3s6.  3;
32:Man  erwartete  *yavärina;  all  Komp.  au«  yma- +*ar3iia-  n.,  eig.  Instrament  zum  Mahlen des  Getreides';  ■.  zn1izJa-undGIrFh./.3ti[. — np. yävar, yär.  — Pfi. :  iur/öt  1  ör/'gemahlenei Getreide'i    erLi    äiyäi  i  fa  datt  '«ine  Hand*
34:isS;  yär-  —  yäs-  mit  a  1188
35:•  j.  (,  P->  yäi-  n.  'Jahr"':  tai^a  ayar>  Gottheiten  der  sechs  Jahreszeiten  und  der mait^UJiU yai  'n  'Sind  die  halten  für  eben  jeweils  am  Ende  gefeierten  fünMgigen Tag,  was  ein  Jahr  (ist)"  V.  2.41;  —  •«  Jahresfeste*':  'ya  (AP.)  aiavana  aiahe aar/ J^3Mff^raJU(sd.)  tj'atll'V.S.46V}iZ.;  ratavS  Y,  2.  9;   17,  Vr.  2.  2;  —   'yaültyS
37:halbes  Jahr  lang"  N,45'  *44''  ^^z"  *4[3'''        **  ''^'"   Nsunen    finden   nch   i.  B.  Vr.  /.  3,
```


## [2026-09-05T20:27:32.530Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Zorn\" BRT.txt | head -20",
 "description": "Bartholomae Zorn"
}
```


### [2026-09-05T20:27:32.577Z] TOOL RESULT

```
2854:SupeH.  lum  V.  ij.--.  —  -  VgL  Yu  ij.  9«-      15.  -13:  S.    'aza-.] •  j.    aesina-,    j^  g.  aessma-    m.    'Zorn.       ^'s'-  ■^ '•  t;j'a  —  j:  i :  jv  s  --^-'.  so  V  ^ Wut,  Raseref,  insbes.  religiüie,  ge^en  das       gr..araj  .ar«.;  vg'.c-   —  "> Rind  sich  richtende  (nur  g.l:  ä  ml  ^nüml. das  Rindi  'jmJ  A-r:js.'J  . .  ,l/:is.TjJ  isd.'
4289:Zorn  V.  drang-,    %    SOg.  8.   —    VgL  ananoi.- dtuila:  i
4324:Zorn  V.  ^ah;    eig.  'kein  DabeiEcin   habend';'
11433:Zorn  V.  iflj".  —  ")  Dh.  damit  wir  sie  als Ausgleich  gegenüber  üblen  Werken  benutien können.  Anders  Gdn.  KZ.  25.  491,  ;i8('Kech- nnng'),  Jh.  JAOS.  U-  ccxii  ('account'),  DsT. ZA.  3.  453  ('anias').
11468:KompE  -  Zorn  V./«^/-.  -  Vgl  -^lüy-.  -   ,  j   ^^^^     fiavant-')  Adj.  (fem.  -vai/f.)
12097:Zorn   Praes.   taui-vaya-  des  V.  Uar-.    —   Pü.:
12456:Zorn  V.  sah-.  —  Pü.:  i  din  ämSxt,  eil.:  ya!/ tart  isla.
12691:Zorn    V.  ><^aj- ').     —     Pü. !  frifiimSvtmtd, ')  Wegen  yJ  i.  Si;}  aA.   Seiner  Bildung  nach vergleicht  lich  </*  etwa  mit  yemya-.
12693:Zorn  V.  lÄji-,  —  ai.  Jastd-  Adj.  —  Pü. :  dänäi; dänikikä.  —  0  So  Pt4;  NA.  dangrä.  — »)  Ansg.  daakrim.
13569:Ableit.  —  Zorn  V.  dar!-.  —  ai.  Tgl.  ädhi-se Inf.  —  Pü.:  darrilSr,  erL:  kiim  biiak  iail>) kan/t;  SüErl. ;  ys  me  jhiaz-i:;/iärani  kurult.  — I)  VgL  IF.  p.  261.  —  >*  Vgl.  imiö^a/ay-.
14849:•  j.  paHka-  Adj.  "kochend' KompE-  —  Zorn  V.  pak:
15130:•  j.  paity-ä8a-  m.  'Antwort":  «Sa  F.jf, Zorn  V.  ad:  —  Vi.t  fatat^  gämihi.  —  ')  Ob vielmehr  jSPfA.?
15499:Zorn    V.   'ah-;    -ngl.  farö.as/ay;  paräki-a-    und     i)    ISn.    'räca    'foit,    weg':    p'    tOraiJa    F. (in  A):  anJar  an/iian.  Su.  (in  A):  fiuraj  sam-   -',,,'  ,     »C.  ^  <.,     ,.     .
15630:Zorn  V,  spä-.    —    Pü.!  fa  apc  hilisHUf,  i.  Sp.
16663:KompE.  —  Zorn  V.  ia}r-.  —  Pu.:  Wjrrj);  s.  mit  n  'austeilen  an— '(Dat'):  ta  (näml. noch  No.  2.   -   n  Hds.  •xira.    -    >)  Pü.:  ^^^j        vtboxsaiti  äbyS  daitiAubyS  seilte
18750:klärte  xich  das  W»rl  jedenfalls  als  'männlicbi Rede  fahrend'.  Die  DeDtnng  GIrPh.  3.  6^2 halle  ich  für  falsch.  5.  noch  No.  4.  —  *}  Zorn ai.  Wort  inleUt  Fav  JAOS.  j6.  clxxu  (mit Mbr  bedenklicher  Elymologie)  und  Oldek- BERC  ZDMG.5^51  (aus  'narämiamiah;  also Dissimilation  t).
18775:-  ä  Zorn
19254:Zorn  V.  har-  mit  tu;   iSchr.  «.  S  ^S.  48,  — Y\\.:  pa  afe  sardärlh. j.  näaohanUü:  i.  unter  hat-.
19758:•  j.  'mana-  m,  'Sinn,  WiUe',  sva.  manaA-. KompE.  —  Zorn  V.  ■'man-.
19870:Zorn  V.  ^man-.  —  ai.  mäniav-  m.  —  Fn. :  ptU- män ') ;  zu  V,  Jj  'die  Erl. :  pährel  i  gBifandäit ni  kunit.  —  »)  Vgl.  "bibh-  No.  9.
```


## [2026-09-05T20:27:42.335Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"xesm\\|xēšm\\|xašm\\|xesm\" PHD_mackenzie.txt | head; echo \"=== NYB\"; grep -n \"xesm\\|xēšm\\|aesma\" NYB_vol2_glossary.txt | head; echo \"=== PHD sal/year\"; grep -n \"^sar\\b\\|sāl\\|'year'\" PHD_mackenzie.txt | head",
 "description": "MacKenzie/Nyberg xesm"
}
```


### [2026-09-05T20:27:42.413Z] TOOL RESULT

```
8001:wrath xesm.                             you asma.
=== NYB
=== PHD sal/year
4493:sar [LOY8E < A T'lh; sll M ST, N -] head; top, summit; end, begin-
```


## [2026-09-05T20:27:45.686Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"xesm\\|xism\\|hesm\" PHD_mackenzie.txt | head -20; echo \"=== search x section\"; grep -n \"^xes\\|^xe\\b\" PHD_mackenzie.txt | head -20",
 "description": "MacKenzie xesm entry"
}
```


### [2026-09-05T20:27:45.753Z] TOOL RESULT

```
5555:x~AIYl eysm, hfm I M xysm, N xism] anger; the demon Wrath.
8001:wrath xesm.                             you asma.
=== search x section
```


## [2026-09-05T20:27:50.888Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"ژانویه\" MON_part1.txt MON_part2.txt | head; echo \"=== NYB\"; grep -n \"xesm\\|xēsm\\|xism\\|aesm\" NYB.txt NYB_vol1.txt NYB_vol2_glossary.txt 2>/dev/null | head",
 "description": "Mo'in janviye, Nyberg xesm"
}
```


### [2026-09-05T20:27:50.961Z] TOOL RESULT

```
MON_part2.txt:43374:ژانویه؛ فوربه؛ مارس. آوریل. مه ژوئن» 
MON_part1.txt:73066:ژانویه: 26 (.) ماه او سال فرنگی 
=== NYB
```


## [2026-09-05T20:27:54.675Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '73060,73075p' MON_part1.txt; echo ===; sed -n '43368,43380p' MON_part2.txt; echo \"=== NYB files\"; ls | grep NYB; grep -n \"xēšm\\|xešm\\|hēšm\" NYB_vol2_glossary.txt | head",
 "description": "Read Moin janviye context"
}
```


### [2026-09-05T20:27:54.744Z] TOOL RESULT

```
Exit code 1
زاندارمری: آعح۶500 (امر.) اداره‌ای 
که مأمور حفظ نظطم در جاده‌ها و راه‌های 
خارج از شهر و قری و قصبات می‌باشد و 
آن از ادارات وزارت کشور است؛ ادارة 
امنیه» ادارةٌ ضبطبه. 

ژانویه: 26 (.) ماه او سال فرنگی 
مطایق با اواخر دی و اوایل بهمن. 
ژئوفیزیک: :204721 (امر.) یزیک کر؟ة 
زمین و آن علمی است که بحث کند از 
نیروهای فیزیکی و پدیده‌های مربوط به 
زمین که به وسیلةٌ نقشه‌های تحت الارضی و 


ژئولوزی 
زلزله‌سنج‌ها و ادوات دیگر الکتر ومغناطیس 
(eval):1: == not found
```


## [2026-09-05T20:28:02.472Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('MON_part1.txt',encoding='utf-8',errors='replace').read()\nprint('formfeeds',t.count('\\f'))\nimport re\n# lines that are bare numbers near 73066\nlines=t.split('\\n')\nfor i in range(72900,73120):\n    s=lines[i].strip()\n    if re.fullmatch(r'[\\d۰-۹]{3,4}',s):\n        print(i,s)\nEOF",
 "description": "Check MON page markers"
}
```


### [2026-09-05T20:28:04.314Z] TOOL RESULT

```
formfeeds 0
```


## [2026-09-05T20:28:13.942Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,50p' tools/fetch_source.py",
 "description": "Inspect fetch_source.py"
}
```


### [2026-09-05T20:28:13.979Z] TOOL RESULT

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


## [2026-09-05T20:28:20.506Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81ey-\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/y%C3%A9h%E2%82%81r%E2%80%90\" \\\n \"https://www.etymonline.com/word/ion\" \\\n \"https://www.etymonline.com/word/January\" \\\n \"https://www.etymonline.com/word/hour\" \\\n \"https://www.etymonline.com/word/year\" \\\n \"https://www.etymonline.com/word/wide\" \\\n \"https://www.etymonline.com/word/iron\" ; do\n echo \"--- $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 149, roots Ei/Eis, checking ion/January/hour/year/wide/iron chains\" 2>&1 | tail -2\ndone",
 "description": "Archive web sources batch 1"
}
```


### [2026-09-05T20:28:25.468Z] TOOL RESULT

```
--- https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81ey-
/home/sfmqrb/git/rishe/data/verification/sources/web/a20c273b41f2ed77.txt
--- https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/y%C3%A9h%E2%82%81r%E2%80%90
/home/sfmqrb/git/rishe/data/verification/sources/web/fd81acc5dfb20261.txt
--- https://www.etymonline.com/word/ion
/home/sfmqrb/git/rishe/data/verification/sources/web/ceb2964b56af4c55.txt
--- https://www.etymonline.com/word/January
/home/sfmqrb/git/rishe/data/verification/sources/web/58758e92a9178487.txt
--- https://www.etymonline.com/word/hour
/home/sfmqrb/git/rishe/data/verification/sources/web/b926d73ab2316f05.txt
--- https://www.etymonline.com/word/year
/home/sfmqrb/git/rishe/data/verification/sources/web/ebce33edf300af7d.txt
--- https://www.etymonline.com/word/wide
/home/sfmqrb/git/rishe/data/verification/sources/web/6a58205c92573292.txt
--- https://www.etymonline.com/word/iron
/home/sfmqrb/git/rishe/data/verification/sources/web/f468b1989abd6608.txt
```


## [2026-09-05T20:28:28.517Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in a20c273b41f2ed77 fd81acc5dfb20261; do echo \"===== $f\"; head -c 300 $f.txt; echo; grep -o \"Proto-Indo-European.\\{0,200\\}\" $f.txt | head -5; done",
 "description": "Check wiktionary fetch results"
}
```


### [2026-09-05T20:28:30.185Z] TOOL RESULT

```
===== a20c273b41f2ed77
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81ey-
FETCHED: 2026-09-05T20:21:45Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/h₁ey- - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/h₁ey- - Wiktionary, the free dictionary 

 Jump to 
Proto-Indo-European/h%E2%82%81ey-
Proto-Indo-European/h₁ey- - Wiktionary, the free dictionary
Proto-Indo-European/h₁ey- - Wiktionary, the free dictionary 
Proto-Indo-European 
Proto-Indo-European subsection 
===== fd81acc5dfb20261
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/y%C3%A9h%E2%82%81r%E2%80%90
FETCHED: 2026-09-05T20:28:22Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
Proto-Indo-European/y%C3%A9h%E2%82%81r%E2%80%90
```


## [2026-09-05T20:28:32.743Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; sed -n '1,200p' a20c273b41f2ed77.txt | tail -160",
 "description": "Read PIE h1ey- page"
}
```


### [2026-09-05T20:28:32.789Z] TOOL RESULT

```
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
 Derived terms 

 1.2 
 See also 

 1.3 
 References 

 Toggle the table of contents 

 Reconstruction:Proto-Indo-European/ h₁ey- 

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

 *h₁ey- ( imperfective ) [ 1 ] [ 2 ] [ 3 ] 

 to go 

 Derived terms
 [ edit ] 

 Terms derived from the Proto-Indo-European root *h₁ey- (74 c, 0 e) 

 *h₁éy-ti ~ *h₁y-énti ( athematic root present ) 

 *h₁e-h₁óy-e ~ *h₁e-h₁y-ḗr ( stative ) 
 Proto-Germanic: *ijjē , *ijjēdun (past tense of *gāną , *ganganą )
 Old English: ēode , ēodon 
 Middle English: yode 
 English: yode , yede 

 Gothic: 𐌹𐌳𐌳𐌾𐌰 ( iddja ) , 𐌹𐌳𐌳𐌾𐌴𐌳𐌿𐌽 ( iddjēdun ) 

 *h₁oy-ós ( nominalization ) [ 4 ] 
 Proto-Tocharian: [Term?] ( “ sheep, goat ” ) 
 Tocharian B: eye 

 *h₁i-tó-s 

 *h₁éy-mn̥ ( “ course, way ” ) 
 Proto-Indo-Iranian: *Háyma 
 Proto-Indo-Aryan: *Háyma 
 Sanskrit: एमन् ( éman ) 

 *h₁éy-ti-s ~ *h₁i-téy-s 

 *h₁ey-n- 
 Proto-Tocharian: 
 Tocharian B: aiñye ( “ traversable ” ) [ 5 ] 

 *h₁ey-tw-om ( verbal noun ) 
 Proto-Tocharian: 
 Tocharian B: aittäṃ ( “ forth ” ) [ 6 ] 

 Proto-Italic: 
 Oscan: eituam ( “ money, cattle ” ) 

 *h₁éy-tr̥ ~ *h₁i-tn-és ( r/n-stem ) 

 *h₁óy-to-s [ 7 ] [ 8 ] [ 9 ] 
 > ? Proto-Celtic: *oitos ( see there for further descendants )

 > ? Proto-Germanic: *aiþaz ( see there for further descendants )

 Proto-Hellenic: 
 > ? Ancient Greek: οἶτος ( oîtos , “ fate, doom ” ) 

 *h₁éy-wr̥ ~ *h₁i-wén-s [ 10 ] ( or descendants from *h₂i wa [ 11 ] ) 
 Proto-Anatolian: 
 Hittite: 𒄿𒉿𒅈 ( i-wa-ar /⁠iwr̩⁠/ , “ in the manner of, like ” ) ( with zero-grade from weak stem ) 

 > ? Proto-Indo-Iranian: *Hiwa ( < *h₁i-wn̥ ? ) 
 Proto-Indo-Aryan: *Hiwa 
 Sanskrit: इव ( iva , “ in the manner of, like ” ) ( see there for further descendants )

 Unsorted formations 
 Proto-Albanian: *ainja 
 Albanian: eja
```


## [2026-09-05T20:28:42.631Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yeh%E2%82%81r-\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81eys-\" \\\n \"https://en.wiktionary.org/wiki/%D8%AE%D8%B4%D9%85\" \\\n \"https://en.wiktionary.org/wiki/%DA%98%D8%A7%D9%86%D9%88%DB%8C%D9%87\" \\\n \"https://en.wiktionary.org/wiki/%CF%8E%CF%81%CE%B1\" \\\n \"https://www.etymonline.com/word/janitor\" ; do\n echo \"--- $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 149 verification\" 2>&1 | tail -1\ndone; echo; grep -l \"FETCH FAILED\" data/verification/sources/web/*.txt | head -20",
 "description": "Archive web sources batch 2"
}
```


### [2026-09-05T20:28:47.313Z] TOOL RESULT

```
--- https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yeh%E2%82%81r-
/home/sfmqrb/git/rishe/data/verification/sources/web/003529da0fded286.txt
--- https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81eys-
/home/sfmqrb/git/rishe/data/verification/sources/web/c38754783be58032.txt
--- https://en.wiktionary.org/wiki/%D8%AE%D8%B4%D9%85
/home/sfmqrb/git/rishe/data/verification/sources/web/07a864cba0b68cd1.txt
--- https://en.wiktionary.org/wiki/%DA%98%D8%A7%D9%86%D9%88%DB%8C%D9%87
/home/sfmqrb/git/rishe/data/verification/sources/web/37b488db00e8bbd4.txt
--- https://en.wiktionary.org/wiki/%CF%8E%CF%81%CE%B1
/home/sfmqrb/git/rishe/data/verification/sources/web/6cc9c59028561d2a.txt
--- https://www.etymonline.com/word/janitor
/home/sfmqrb/git/rishe/data/verification/sources/web/f528d07ee66cc891.txt

data/verification/sources/web/0c78e031adf264d3.txt
data/verification/sources/web/0af573ddd8850565.txt
data/verification/sources/web/13142f9e8661032d.txt
data/verification/sources/web/1ec52071e8412e12.txt
data/verification/sources/web/1ddec17b8b6fd73d.txt
data/verification/sources/web/245b71668203ff4f.txt
data/verification/sources/web/28614795e7ece081.txt
data/verification/sources/web/2cfb3dc919ae0b68.txt
data/verification/sources/web/2de46ebb4dd7ede2.txt
data/verification/sources/web/32677354f8f654fe.txt
data/verification/sources/web/489eaf3d6f8b2883.txt
data/verification/sources/web/4cbbccb28279c822.txt
data/verification/sources/web/5e0b29b559b719f2.txt
data/verification/sources/web/64e79609d0be30fd.txt
data/verification/sources/web/64ac72685954b530.txt
data/verification/sources/web/6fb31785225e4417.txt
data/verification/sources/web/78fb0757f04b76ee.txt
data/verification/sources/web/8379e855f01ca436.txt
data/verification/sources/web/85e6c7af8f236bfe.txt
data/verification/sources/web/9c835b7d502e3ae2.txt
```


## [2026-09-05T20:28:50.323Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in 003529da0fded286 c38754783be58032 07a864cba0b68cd1 37b488db00e8bbd4; do echo \"===== $f\"; sed -n '1,5p' $f.txt; done",
 "description": "Check batch 2 statuses"
}
```


### [2026-09-05T20:28:52.440Z] TOOL RESULT

```
===== 003529da0fded286
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yeh%E2%82%81r-
FETCHED: 2026-09-05T20:28:44Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/yóh₁r̥ - Wiktionary, the free dictionary

===== c38754783be58032
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81eys-
FETCHED: 2026-09-05T20:28:45Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/h₁eysh₂- - Wiktionary, the free dictionary

===== 07a864cba0b68cd1
URL: https://en.wiktionary.org/wiki/%D8%AE%D8%B4%D9%85
FETCHED: 2026-09-05T20:28:45Z
STATUS: 200
TITLE: خشم - Wiktionary, the free dictionary

===== 37b488db00e8bbd4
URL: https://en.wiktionary.org/wiki/%DA%98%D8%A7%D9%86%D9%88%DB%8C%D9%87
FETCHED: 2026-09-05T20:28:46Z
STATUS: 200
TITLE: ژانویه - Wiktionary, the free dictionary
```


## [2026-09-05T20:28:56.003Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo \"##### yohr\"; grep -n \"yóh₁r\\|Descendants\\|Avestan\\|Ancient Greek\\|Proto-Germanic\\|Noun\" 003529da0fded286.txt | head -30; echo; awk '/From Wiktionary/,0' 003529da0fded286.txt | head -60",
 "description": "Read PIE year page"
}
```


### [2026-09-05T20:29:09.032Z] TOOL RESULT

```
##### yohr
4:TITLE: Reconstruction:Proto-Indo-European/yóh₁r̥ - Wiktionary, the free dictionary
6:Reconstruction:Proto-Indo-European/yóh₁r̥ - Wiktionary, the free dictionary 
65: Noun 
74: Descendants 
81: Reconstruction:Proto-Indo-European/ yóh₁r̥ 
147: Noun
150: *yóh₁r̥   n ( oblique stem *yéh₁n- ) [ 2 ] 
170: *yóh₁r̥ 
190: *yóh₁r̥ 
192: *yóh₁rih₁ 
194: *yóh₁r̥h₂ 
200: *yóh₁r̥ 
202: *yóh₁rih₁ 
204: *yóh₁r̥h₂ 
210: *yóh₁r̥ 
212: *yóh₁rih₁ 
214: *yóh₁r̥h₂ 
272: Proto-Germanic: *jērą [ 2 ] ( see there for further descendants )
274: *yóh₁r-o-s , *yóh₁r-eh₂ 
281: Ancient Greek: ὥρᾱ ( hṓrā ) , ὥρη ( hṓrē ) — Epic , Ionic ( see there for further descendants )
287: Descendants
290: Terms derived from the Proto-Indo-European word *yóh₁r̥ 
297: Younger Avestan: 𐬫𐬁𐬭𐬆 ( yār ə ) ~ 𐬫𐬃 ( yā̊ ) , 𐬫𐬁 ( yā ) )
300: Avestan: 𐬛𐬎𐬲𐬌𐬌𐬁𐬌𐬭𐬌𐬌𐬀 ( dužiiā i riia , “ bad year, drought, harvest bringing bad seasons ” ) 
308: Avestan: 𐬵𐬎𐬌𐬌𐬁𐬌𐬭𐬌𐬌𐬀 ( huiiā i riia , “ good year, non-drought year, harvest bringing good seasons ” ) 
316: ↑ 2.0 2.1 Kroonen, Guus ( 2013 ), “*jēra-”, in Etymological Dictionary of Proto-Germanic (Leiden Indo-European Etymological Dictionary Series; 11 )‎ [1] , Leiden, Boston: Brill , →ISBN , page 273 
322: ^ Kümmel, Martin Joachim ( 2015 ), “Suppletive Phenomena in Older Indo-Iranian Noun Inflection”, in Diachrony and Suppletion ‎ [2] , Prague 
324: Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/yóh₁r̥&oldid=92151904 "
372: Reconstruction:Proto-Indo-European/ yóh₁r̥ 

 From Wiktionary, the free dictionary

 (Redirected from Reconstruction:Proto-Indo-European/yeh₁r- ) 

 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Etymology
 [ edit ] 

 Beekes mentions a possible derivation from *(H)yeh₁- ( “ to send ” ) . [ 1 ] 

 Noun
 [ edit ] 

 *yóh₁r̥   n ( oblique stem *yéh₁n- ) [ 2 ] 

 year 
 Synonyms: *ǵʰéyōm , *wétos 

 growing season or harvest season 
 Synonym: *semh₂- 
 Antonym: *ǵʰey- 

 Inflection
 [ edit ] 

 Athematic, acrostatic

 singular

 collective

 nominative

 *yóh₁r̥ 

 *yéh₁ōr 

 genitive

 *yéh₁n̥s 

 *ih₁nés 

 singular

 dual

 plural

 collective

 nominative

 *yóh₁r̥ 

 *yóh₁rih₁
```


## [2026-09-05T20:29:23.218Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; awk '/From Wiktionary/,0' c38754783be58032.txt | head -70",
 "description": "Read PIE h1eysh2 page"
}
```


### [2026-09-05T20:29:25.246Z] TOOL RESULT

```
 From Wiktionary, the free dictionary

 (Redirected from Reconstruction:Proto-Indo-European/h₁eys- ) 

 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Root
 [ edit ] 

 *h₁eysh₂- [ 1 ] [ 2 ] [ 3 ] 

 to strengthen [ 2 ] 

 to propel [ 2 ] 

 Derived terms
 [ edit ] 

 Terms derived from the Proto-Indo-European root *h₁eysh₂- (15 c, 0 e) 

 *h₁is-né-h₂-ti ~ *h₁is-n-h₂-énti ( nasal-infix present ) [ 2 ] [ 4 ] 
 Proto-Hellenic: *ihnā́ō 
 Ancient Greek: ἰνάω ( ináō ) 

 Proto-Indo-Iranian: *HišnáHti 
 Proto-Indo-Aryan: *HiṣṇáHti 
 Sanskrit: इष्णाति ( iṣṇā́ti ) 

 *h₁is-yé-ti ( zero-grade ye-present ) ( < *h₁ish₂-yé-ti [ 2 ] with Pinault's law ) 
 Proto-Indo-Iranian: *Híšyati ( see there for further descendants )

 *h₁i-h₁éysh₂-ti ~ *h₁i-h₁ish₂-énti ( i-reduplicated athematic root present ) [ 2 ] [ 5 ] 
 Proto-Hellenic: 
 > ? Ancient Greek: ἰάομαι ( iáomai , “ to cure, heal ” ) 

 Proto-Indo-Iranian: *HiHáyšHti 
 Proto-Iranian: *HiHáyšHti 
 Avestan: 
 Old Avestan: 𐬌𐬱𐬆𐬧𐬙𐬍 ( išəṇtī , 3pl.pres.act.ind. ) 
 Younger Avestan: 𐬌𐬱𐬀𐬝 ( išat̰ , 3sg.pres.act.inj. ) 

 *h₁oysh₂-éye-ti ( causative ) [ 2 ] 
 Proto-Indo-Iranian: *HayšHáyati ( see there for further descendants )

 *h₁éysh₂-eh₂ [ 6 ] 
 Proto-Italic: *eizā 
 Latin: īra ( “ anger, wrath ” ) ( see there for further descendants )

 *h₁oysh₂-éh₂ 
 ⇒ Proto-Germanic: *aisōną ( see there for further descendants )

 *h₁óys-mo-s ( < *h₁óysh₂-mo-s with the Saussure effect ) 
 Proto-Hellenic: 
 Ancient Greek: οἶμα ( oîma ) 

 Proto-Indo-Iranian: *Háyšmas 
 Proto-Iranian: *Háyšmah ( see there for further descendants )

 References
 [ edit ] 

 ^ Pokorny, Julius ( 1959 ), “ eis- ”, in Indogermanisches etymologisches Wörterbuch [ Indo-European Etymological Dictionary ] (in German), volume 1, Bern, München: Francke Verlag, pages 299-301 

 ↑ 2.0 2.1 2.2 2.3 2.4 2.5 2.6 Rix, Helmut , editor ( 2001 ), “*h₁ei̯sh₂-”, in Lexikon der indogermanischen Verben [ Lexicon of Indo-European Verbs ] (in German), 2nd edition, Wiesbaden: Dr. Ludwig Reichert Verlag, →ISBN , page 234 

 ^ Cheung, Johnny ( 2007 ), “ *HaišH ”, in Etymological Dictionary of the Iranian Verb (Leiden Indo-European Etymological Dictionary Series; 2), Leiden, Boston: Brill, →ISBN , page 159
```


## [2026-09-05T20:29:25.319Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; awk '/From Wiktionary/,0' 07a864cba0b68cd1.txt | head -60; echo \"########## JANVIYE\"; awk '/From Wiktionary/,0' 37b488db00e8bbd4.txt | head -40",
 "description": "Read khashm and janviye"
}
```


### [2026-09-05T20:29:27.245Z] TOOL RESULT

```
 From Wiktionary, the free dictionary

 See also: چشم and جسم 

 Gulf Arabic
 [ edit ] 

 Etymology
 [ edit ] 

 Root 

 خ ش م 

 1 term 

 From Arabic خَشَم ( ḵašam ) . Cognate with Hijazi Arabic خشم ( ḵušum ) and Iraqi Arabic خشم ( ḵaš(i)m ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /ˈχə.ʃɪm/ 

 Noun
 [ edit ] 

 خَشِم • ( ḵašim )  m ( plural خْشُوم ( ḵšūm ) ) 

 nose 

 Hijazi Arabic
 [ edit ] 

 Etymology
 [ edit ] 

 From Arabic خَشَم ( ḵašam ) . Cognate with Gulf Arabic خشم ( ḵašim ) and Iraqi Arabic خشم ( ḵaš(i)m ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /xu.ʃum/ , [xʊ.ʃʊm] 

 Noun
 [ edit ] 

 خشم • ( ḵušum )  m ( construct state خُشْم ( ḵušm ) , plural أخشام ( ʔaḵšām ) ) 

 nose 

 Iraqi Arabic
 [ edit ] 

 Etymology
 [ edit ] 

 From Arabic خَشَم ( ḵašam ) . Cognate with Hijazi Arabic خشم ( ḵušum ) and Gulf Arabic خشم ( ḵašim ) .

 Pronunciation
 [ edit ] 
########## JANVIYE
 From Wiktionary, the free dictionary

 Azerbaijani
 [ edit ] 

 Etymology
 [ edit ] 

 Borrowed from French janvier , from Latin Iānuārius .

 Noun
 [ edit ] 

 ژانویه ( janviyə ) 

 ( South Azerbaijani ) January 

 See also
 [ edit ] 

 ( Gregorian calendar months ) : ژانویه ( janviyə ) , فئوریه ( fevriyə ) , مارس ( mars ) , آوریل ( avril ) , مه ( mə ) , ژوئن ( juən ) , ژوئیه ( juiyə ) , اوت ( ut ) , سئپتامبر ( septambr ) , اوْکتوْبر ( oktobr ) , نوْوامبر ( novambr ) , دئسامبر ( desambr ) 

 Persian
 [ edit ] 

 Persian Wikipedia has an article on: ژانویه 

 Wikipedia fa 

 Etymology
 [ edit ] 

 Etymology tree

 Proto-Indo-European *yeh₂- der. 
 Proto-Indo-European *yeh₂-no- 
 Proto-Italic *jānos 
 Latin iānus 
 Latin Iānus
```


## [2026-09-05T20:29:36.242Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; grep -n \"Persian\" 07a864cba0b68cd1.txt | head -20",
 "description": "Locate Persian section in khashm page"
}
```


### [2026-09-05T20:29:36.286Z] TOOL RESULT

```
99: Persian 
101: Toggle Persian subsection 
274: Persian
277: Persian Wikipedia has an article on: خشم 
284: From Middle Persian ʾyšm, xyšm ( xēšm , “ anger ” ) , from Old Persian *aišima (compare Avestan 𐬀𐬉𐬱𐬆𐬨𐬀 ( aēšəma ) , 𐬀𐬉𐬴𐬨𐬀 ( aēṣ̌ma ) ), from Proto-Iranian *HayšHmah , from Proto-Indo-Iranian *HayšHmas , from Proto-Indo-European *h₁oysh₂-mo-s , from *h₁eysh₂- .
293: ( Classical Persian ) IPA ( key ) : /ˈxaʃm/ , /ˈxiʃm/ 
333: Iranian Persian
369: From Classical Persian خشم ( xašm , “ anger, rage ” ) . 
419: Persian terms inherited from Middle Persian 
420: Persian terms derived from Middle Persian 
421: Persian terms inherited from Proto-Iranian 
422: Persian terms derived from Proto-Iranian 
423: Persian terms inherited from Proto-Indo-Iranian 
424: Persian terms derived from Proto-Indo-Iranian 
425: Persian terms inherited from Proto-Indo-European 
426: Persian terms derived from Proto-Indo-European 
427: Persian terms with IPA pronunciation 
428: Rhymes:Persian/aʃm 
429: Rhymes:Persian/aʃm/1 syllable 
430: Rhymes:Persian/iʃm
```


## [2026-09-05T20:29:39.175Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 120 python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/H%C3%A1y%C5%A1mah\" --note \"page 149, Eis 1 root, Avestan aesma / Persian xasm\" 2>&1|tail -1; timeout 120 python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%DB%8C%D9%88%D9%86\" --note \"page 149, Persian yon 'ion'\" 2>&1|tail -1",
 "description": "Fetch Proto-Iranian Haysmah and یون"
}
```


### [2026-09-05T20:29:42.219Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/755d52e7e3ce9ed8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5a036997824f6860.txt
```


## [2026-09-05T20:29:47.432Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; sed -n '1,5p' 5a036997824f6860.txt; grep -n \"Persian\" -A3 5a036997824f6860.txt | sed -n '1,60p'",
 "description": "Read yon page"
}
```


### [2026-09-05T20:29:47.486Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/%DB%8C%D9%88%D9%86
FETCHED: 2026-09-05T20:29:42Z
STATUS: 200
TITLE: یون - Wiktionary, the free dictionary

199: Borrowed from Sanskrit यवन ( yavana ) , itself from Ashokan Prakrit 𑀬𑁄𑀦 ( yona ) , from Old Persian 𐎹𐎢𐎴 ( y-u-n /⁠yauna⁠/ ) . Doublet of یونان ( yūnān ) and جون ( javan ) .
200-
201- Pronunciation
202- [ edit ] 
--
288: Urdu terms derived from Old Persian 
289- Urdu doublets 
290- Urdu terms with IPA pronunciation 
291- Rhymes:Urdu/ən
```


## [2026-09-05T20:29:48.672Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; awk '/^ Persian$/,0' 37b488db00e8bbd4.txt | head -70",
 "description": "Read janviye Persian section"
}
```


### [2026-09-05T20:29:50.335Z] TOOL RESULT

```
 Persian
 [ edit ] 

 Persian Wikipedia has an article on: ژانویه 

 Wikipedia fa 

 Etymology
 [ edit ] 

 Etymology tree

 Proto-Indo-European *yeh₂- der. 
 Proto-Indo-European *yeh₂-no- 
 Proto-Italic *jānos 
 Latin iānus 
 Latin Iānus 

 Proto-Indo-European *-yós der. 
 Proto-Italic *-āzios 
 Latin -ārius 

 Latin Iānuārius 
 Old French janvier 
 French janvier bor. 
 Persian ژانویه 

 Borrowed from French janvier .

 Pronunciation
 [ edit ] 

 ( Iran, formal ) IPA ( key ) : [ʒɒːɱ.vi.jé] 

 Readings

 Iranian reading ? 

 žânviye

 Audio ( Iran ) : ( file ) 

 Proper noun
 [ edit ] 

 Dari

 جنوری 

 Iranian Persian

 ژانویه 

 Tajik

 январ 

 ژانویه • ( žânviye ) 

 ( Iran ) January 

 See also
 [ edit ] 

 Gregorian calendar months in Persian · ماه‌هایِ تَقْویمِ میلادی ( mâh-hâ-ye taġvim-e milâdi ) 
 (Iranian Persian) ( layout · text ) 

 January 

 February
```


## [2026-09-05T20:30:01.091Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; grep -n \"^ Persian\\|ion \\|French\" 5a036997824f6860.txt | head -20; echo \"### etymonline January\"; awk '/January/,0' 58758e92a9178487.txt | head -40",
 "description": "Check yon Persian + etymonline January"
}
```


### [2026-09-05T20:30:02.930Z] TOOL RESULT

```
59: Toggle Shina subsection 
65: Pronunciation 
73: Toggle Urdu subsection 
79: Pronunciation 
90: Toggle Ushojo subsection 
112: Discussion 
143: Page information 
151: Printable version 
235: ( figurative , Hinduism ) a follower of a religion of foreign (usually of non- Dharmic origin )
280: Shina terms with IPA pronunciation 
290: Urdu terms with IPA pronunciation 
### etymonline January
URL: https://www.etymonline.com/word/January
FETCHED: 2026-09-05T20:28:23Z
STATUS: 200
TITLE: January - Etymology, Origin & Meaning of the Name

January - Etymology, Origin & Meaning of the Name 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of January 

 January (n.) 

 late 13c., Ieneuer (early 12c. in Anglo-French), from Old North French Genever , Old French Jenvier (Modern French Janvier ), from Latin Ianuarius (mensis) "(the month) of Janus " (q.v.), to whom the month was sacred as the beginning of the year according to later Roman reckoning.

 The English word is cognate with Italian Gennaio , Provençal Genovier , Spanish Enero , Portuguese Janeiro . The form was gradually Latinized by c. 1400. It replaced Old English geola se æfterra "Later Yule." In Chaucer, a type-name for an old man. Also see New Year's Eve .
 also from late 13c. 

 Entries linking to January 

 Janus 

 ancient Italic deity, to the Romans the guardian god of portals, doors, and gates; patron of beginnings and endings, c. 1500, from Latin Ianus , literally "gate, arched passageway," perhaps from PIE root *ei- "to go" (cognates: Sanskrit yanah "path," Old Church Slavonic jado "to travel"). He is shown as having two faces, one in front the other in back (they may represent sunrise and sunset and reflect an original role as a solar deity). His temple in Rome was closed only in times of peace. Related: Janian .

 New Year's Eve 

 "evening before the first day of the new year," c. 1300; "þer þay dronken & dalten ... on nwe gerez euen" ["Sir Gawain and the Green Knight"]. The Julian calendar began on January 1, but the Christian Church frowned on pagan celebrations of this event and chose the Feast of the Annunciation (March 25) as its New Year's Day.

 The civic year in England continued to begin January 1 until late 12c., and though legal documents then shifted to March 25, popular calendars and almanacs continued to begin on January 1. Gower ( "Confessio Amantis," late 14c.) writes of "The frosti colde Janever, Whan comen is the newe yeer," and in 1579 Spenser ("Shepherd's Kalendar") wrote that "according to the simplicitie of common understanding" the year began in January. The calendar reform of 1751 restored the Julian New Year in England.
```


## [2026-09-05T20:30:10.345Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in ceb2964b56af4c55 b926d73ab2316f05 ebce33edf300af7d 6a58205c92573292 f468b1989abd6608 f528d07ee66cc891; do echo \"##### $f\"; awk '/Origin and history of/,0' $f.txt | head -18; done",
 "description": "Read etymonline entries"
}
```


### [2026-09-05T20:30:12.040Z] TOOL RESULT

```
##### ceb2964b56af4c55
 Origin and history of ion 

 ion (n.) 

 1834, introduced by English physicist and chemist Michael Faraday (suggested by the Rev. William Whewell, English polymath), coined from Greek ion , neuter present participle of ienai "go," from PIE root *ei- "to go." So called because ions move toward the electrode of opposite charge.
 also from 1834 

 Entries linking to ion 

 cation (n.) 

 "positively charged ion," 1834, from Latinized form of Greek kation "going down," neuter present participle of katienai "to go down," from kata "down" (see cata- ) + ienai "to go" (from PIE root *ei- "to go"). Proposed by the Rev. William Whewell, English polymath, and published by English physicist Michael Faraday. Compare ion .

 electron (n.) 

 coined 1891 by Irish physicist George J. Stoney (1826-1911) from electric + -on , as in ion (q.v.). Electron microscope (1932) translates German Elektronenmikroskop .

 Ionic 
##### b926d73ab2316f05
 Origin and history of hour 

 hour (n.) 

 c. 1200, "divine office prescribed for each of the seven canonical hours; the daily service at the canonical hours;" c. 1300, "time of day appointed for prayer, one of the seven canonical hours," from Old French ore , hore "canonical hour; one-twelfth of a day" (sunrise to sunset), from Latin hora "an hour;" poetically "time of year, season," from Greek hōra a word used to indicate any limited time within a year, month, or day (from PIE *yor-a- , from root *yer- "year, season;" see year ).

 The Church sense is oldest in English. The meaning "one of the 24 equal parts of a natural solar day (time from one sunrise to the next), equal hour; definite time of day or night reckoned in equal hours," and that of "one of the 12 equal parts of an artificial day (sunrise to sunset) or night, varying in duration according to the season; definite time of day or night reckoned in unequal hours" are from late 14c.

 In the Middle Ages the planets were held to rule over the unequal hours. As late as 16c. distinction sometimes was made in English between temporary (unequal) hours and sidereal (equal) ones. The meaning "time of a particular happening; the time for a given activity" (as in hour of death ) is mid-14c.

 The h- has persisted in this word despite not being pronounced since Roman times. Replaced Old English tid , literally "time" (see tide (n.)) and stund "period of time, point of time, hour," from Proto-Germanic *stundo (compare German Stunde "hour"), which is of uncertain origin. German Uhr likewise is from French.

 Greek hora could mean "a season; 'the season' (spring or summer)." In classical times it sometimes meant "a part of the day," such as morning, evening, noon, night. The Greek astronomers apparently borrowed the notion of dividing the day into twelve parts (mentioned in Herodotus) from the Babylonians. Night continued to be divided into four watches (see watch (n.)); but because the amount of daylight changed throughout the year, the hours were not fixed or of equal length.

 As a measure of distance ("the distance that can be covered in an hour") it is recorded from 1785. At all hours "at all times" is from early 15c. For small hours (those with low numbers) see wee (adj.).
 also from c. 1200 

 Entries linking to hour 
##### ebce33edf300af7d
 Origin and history of year 

 year (n.) 

 "a full round of seasons, the interval between equinoxes, the time occupied by the sun in passage through the zodiac," Middle English yer , from Old English gear (West Saxon), ger (Anglian) "year," from Proto-Germanic *jēr "year," reconstructed to be from PIE root *yer- "year, season," probably [Watkins] originally "that which makes [a complete cycle]," and from verbal root meaning "to do, make."

 Also by Middle English as "any space of about 365 days or 12 calendrical months, without regard to starting point. Years as "period of life" is by early 13c.

 Germanic cognates include Old Saxon, Old High German jar , Old Norse ar , Danish aar , Old Frisian ger , Dutch jaar , German Jahr , Gothic jer "year." IE cognates outside Germanic include Avestan yare (nominative singular) "year;" Greek hōra "year, season, any part of a year," also "any part of a day, hour;" Old Church Slavonic jaru , Bohemian jaro "spring;" Latin hornus "of this year;" Old Persian dušiyaram "famine," literally "bad year."

 Entries linking to year 

 G 

 seventh letter of the alphabet, invented by the Romans; a modified gamma introduced c. 250 B.C.E. to restore a dedicated symbol for the "g" sound. For fuller history, see C .

 Before the vowels -e- , -i- , and -y- , Old English initial g- changed its sound and is represented in Modern English by consonantal y- ( year , yard , yellow , young , yes , etc.). In get and give , however, the initial g- seems to have been preserved by Scandinavian influence. Also see gu- .

##### 6a58205c92573292
 Origin and history of wide 

 wide (adj.) 

 "having relatively great extension from side to side; having a certain or specified extension from side to side;" Old English wid , also "vast, long," also used of time; from Proto-Germanic *widaz (source also of Old Saxon, Old Frisian wid , Old Norse viðr , Dutch wijd , Old High German wit , German weit ), which is perhaps (Watkins) from PIE *wi-ito- , from root *wi- "apart, away, in half."

 The meaning "distended, expanded, spread apart" is attested by c. 1500; the sense of "embracing many subjects" is from 1530s. The meaning "missing the intended target" is from 1580s. Of a dialect, "characterized by a broad accent," by mid-15c.

 As a second element in compounds (such as nationwide , worldwide ) and meaning "extending through the whole of," it is from late Old English. Wide-screen in reference to cinema projection is by 1931.

 wide (adv.) 

 "to a distance; with a large space between," Old English wide ; see wide (adj.). By 1580s as "away from or to the side of a mark."

 Wide open "unguarded, exposed to attack" is by 1915, originally in pugilism. Late Old English and Middle English also had widewhere "far and wide, everywhere."

 Entries linking to wide 

##### f468b1989abd6608
 Origin and history of iron 

 iron (n.) 

 Middle English iron , iren , yron , from Old English iren , variant (with rhotacism of -s- ) of isen , later form of isern , isærn "the metal iron; an iron weapon or instrument," from Proto-Germanic *isarn (source also of Old Saxon isarn , Old Frisian isern , Old Norse isarn , Middle Dutch iser , Old High German isarn , German Eisen ).

 This perhaps is an early borrowing of Celtic *isarnon (compare Old Irish iarn , Welsh haiarn ), which Watkins suggests is from PIE *is-(e)ro- "powerful, holy," from PIE *eis "strong" (source also of Sanskrit isirah "vigorous, strong," Greek ieros "strong"), on the notion of "holy metal" or "strong metal" (in contrast to softer bronze).

 Both an adjective and a noun in Old English, but in form an adjective. The alternative isen survived into early Middle English as izen . In southern England the Middle English word tended to be ire , yre , with loss of -n , perhaps regarded as an inflection; in the north and Scotland, however, the word tended to be contracted to irn , yrn , still detectable in dialect.

 Right so as whil that Iren is hoot men sholden smyte. [Chaucer, c. 1386]

 Chemical symbol Fe  is from the Latin word for the metal, ferrum (see ferro- ).

 The meaning "metal device used to press or smooth clothes" is from 1610s. The meaning "golf club with an iron head" is by 1842. To have (too) many irons in the fire "to be doing too much at once" is from 1540s. Iron lung "artificial respiration tank" is from 1932. The iron crown was that of the ancient kings of Lombardy, with a thin band of iron in the gold, said to have been forged from a nail of Christ's Cross.

 Iron horse "railroad locomotive" is from an 1839 poem. Iron maiden , instrument of torture, is from 1837 (probably translating German eiserne jungfrau ). The unidentified French political prisoner known as the man in the iron mask died in the Bastille in 1703. In British history, Wellington was called the Iron Duke by 1832.

##### f528d07ee66cc891
 Origin and history of janitor 

 janitor (n.) 

 1580s, "an usher in a school," later "doorkeeper" (1620s), from Latin ianitor "doorkeeper, porter," from ianua "door, entrance, gate," from ianus "arched passageway, arcade" (see Janus ) + agent suffix -tor .

 The meaning "caretaker of a building, man employed to see that rooms are kept clean and in order" is recorded by 1708. Fem. forms were janitress (1806), janitrix (1818). In Horace, Cerberus is ianitor of Hell.
 also from 1580s 

 Entries linking to janitor 

 Janus 

 ancient Italic deity, to the Romans the guardian god of portals, doors, and gates; patron of beginnings and endings, c. 1500, from Latin Ianus , literally "gate, arched passageway," perhaps from PIE root *ei- "to go" (cognates: Sanskrit yanah "path," Old Church Slavonic jado "to travel"). He is shown as having two faces, one in front the other in back (they may represent sunrise and sunset and reflect an original role as a solar deity). His temple in Rome was closed only in times of peace. Related: Janian .

 janitorial (adj.) 

 1869, from janitor + -ial .
```


## [2026-09-05T20:30:25.775Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls site/pages/149.jpg 2>/dev/null; pdftoppm -f 149 -l 149 -r 300 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg149 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 149"
}
```


### [2026-09-05T20:30:28.299Z] TOOL RESULT

```
site/pages/149.jpg
total 15188
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 16:30 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  5 16:02 ..
-rw-rw-r-- 1 sfmqrb sfmqrb  752374 Sep  5 16:12 bqt362_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  624515 Sep  5 16:12 bqt362.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 1032029 Sep  5 16:13 bqt362_mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb  385716 Sep  5 16:13 bqt363_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  338175 Sep  5 16:13 bqt363_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  692415 Sep  5 16:13 bqt363.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  956665 Sep  5 16:11 bqt553_foot2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  746413 Sep  5 16:11 bqt553_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  512022 Sep  5 16:10 bqt553.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  154316 Sep  5 16:07 bqt_bot389.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168738 Sep  5 16:07 bqt_bot390.png
-rw-rw-r-- 1 sfmqrb sfmqrb  520653 Sep  5 16:07 bqt_n389.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  527392 Sep  5 16:07 bqt_n390.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   67648 Sep  5 16:29 build128.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56126 Sep  5 16:29 build136b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   13830 Sep  5 16:22 build136.py
-rw-rw-r-- 1 sfmqrb sfmqrb   66341 Sep  5 16:28 build139.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53260 Sep  5 16:29 build142.py
-rw-rw-r-- 1 sfmqrb sfmqrb   21485 Sep  5 16:29 build148.py
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:18 kent.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     222 Sep  5 16:30 leaf.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57617 Sep  5 16:20 mk129.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74680 Sep  5 16:26 mk131.py
-rw-rw-r-- 1 sfmqrb sfmqrb   33365 Sep  5 16:25 mk133.py
-rw-rw-r-- 1 sfmqrb sfmqrb   42635 Sep  5 16:29 mk140.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51288 Sep  5 16:30 mk143.py
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:13 oldpers_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   22067 Sep  5 16:29 part0.json
-rw-rw-r-- 1 sfmqrb sfmqrb   14156 Sep  5 16:22 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb   53212 Sep  5 16:08 pg130_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74748 Sep  5 16:08 pg130.png
-rw-rw-r-- 1 sfmqrb sfmqrb  107108 Sep  5 16:08 pg130_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80793 Sep  5 16:15 pg131.png
-rw-rw-r-- 1 sfmqrb sfmqrb   46793 Sep  5 16:20 pg133.png
-rw-rw-r-- 1 sfmqrb sfmqrb   87739 Sep  5 16:10 pg134.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66991 Sep  5 16:16 pg135.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68320 Sep  5 16:08 pg136_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63248 Sep  5 16:08 pg136.png
-rw-rw-r-- 1 sfmqrb sfmqrb   45014 Sep  5 16:12 pg137.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74330 Sep  5 16:11 pg138.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70436 Sep  5 16:10 pg140.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63658 Sep  5 16:13 pg144.png
-rw-rw-r-- 1 sfmqrb sfmqrb   89133 Sep  5 16:09 pg145.png
-rw-rw-r-- 1 sfmqrb sfmqrb   60631 Sep  5 16:11 pg147.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81770 Sep  5 16:20 pg148.png
-rw-rw-r-- 1 sfmqrb sfmqrb   72186 Sep  5 16:30 pg149.png
-rw-rw-r-- 1 sfmqrb sfmqrb   96854 Sep  5 16:29 pg151.png
-rw-rw-r-- 1 sfmqrb sfmqrb   39131 Sep  5 16:28 pg153.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep  5 16:14 prt.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  333088 Sep  5 16:16 sod135_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1817364 Sep  5 16:16 sod135.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  101641 Sep  5 16:15 sod136_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1892712 Sep  5 16:15 sod136.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   56398 Sep  5 16:26 write144.py
```


## [2026-09-05T20:30:37.897Z] TOOL CALL #65: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg149.png"
}
```


### [2026-09-05T20:30:38.455Z] TOOL RESULT

```

```


## [2026-09-05T20:30:38.452Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-05T20:31:06.776Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"hirek\\|hlrek\\|Zickchen\\|Böckchen\\|Bockchen\\|yäirka\\|Jährling\" HUB.txt | head -20",
 "description": "Hubschmann hirek"
}
```


### [2026-09-05T20:31:06.857Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:31:10.384Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"hirak\\|hlrak\\|hirck\\|hlrek\\|herek\\|1116\" HUB.txt | head -20; echo \"=== size\"; wc -l HUB.txt",
 "description": "Hubschmann search 2"
}
```


### [2026-09-05T20:31:10.485Z] TOOL RESULT

```
3755:1116. Ich halte die Etymologie fiir falsch.
=== size
10982 HUB.txt
```


## [2026-09-05T20:31:14.475Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '3735,3775p' HUB.txt; echo \"--- leaf\"; python3 - <<'EOF'\nt=open('HUB.txt',encoding='utf-8',errors='replace').read()\ni=t.find('1116. Ich halte die Etymologie')\nleaf=t[:i].count('\\f')\nprint('leaf',leaf,'printed page approx',leaf-10)\nEOF",
 "description": "Read Hubschmann rejection of hirek"
}
```


### [2026-09-05T20:31:16.495Z] TOOL RESULT

```
zd. h'ama- und hama-,
Hierher: np. hamdl 'der Gleiche, Genosse' (Fird.
I, 142, 249) = skr. samarfha- ^entsprechend'.
llQ2bi8. j^p Jiiifnand (sprich humana?) = paz. hiimana
(Shk. 251 etc.) = phi. humanak (Gl. and Ind. 55 etc.),
also aus hu + mdndJc. Daher wohl auch humanand
ahnlich' zu lesen.
1103. Dem np. hama all, ganz' (pi. hamagan) steht paz.
hama, phi. hamak gegeniiber.
1104. Aus ap. "^hamaiy ware np. *Aam geworden. Hierher
np. hamesa 'immer .
1105. Nicht sicher.
1109. Arm. aw^'am heisst 'Mai' {mi angam *einmar etc.) und
*auch'.
1111. Zd. usi heisst 1) Verstand, Einsicht, Sinn, 2) 'die
beiden Ohren*, letzteres nach § 26 des Nirangistan
bei Darmesteter, Zend-Avesta III, p. 95, 96
Anm. 5.
1113. 1st hum zu sprechen (wegen m). Vgl. den Reim auf
bum bei Vullers.
1116. Ich halte die Etymologie fiir falsch.
1118. Man wird I = paz. i doch an ap. hya, hya an-
kniipfen miissen. Der Stamm ya- liegt altpersisch
nur in Adv. wie yada vor. Im Paz. lautet das Re-
lativum ya- (in ya-m, ya-t, ya-s, ya-sctn) = ap. hya,
hya (da ya- zu ja- geworden ware).
1118 — 1121. Ich halte die Pazendlesungen , nach denen die
Worter ein anlautendes a verloren haben-), fiir be-
achtenswerth: ayclo oder (vgl. v-aya bei Fird.),
ayad *Gedachtni8s', ayadagar 'memorandum* Shk. 235,
ayar *Helfer 2). Zu np. Isfandyar vgl. phi. Spand-
*) Langes a fallt nioht ab!
') Das mand&isohe LW. adyaura *Helfer* ist nach N old eke
ganz sioher.— 107 —
yat Yatk. i. Zar. 57, 59, West, PT. II, 137, Bdh. Gl.
173, Dink art V, 19, arm. Spandiat Sebeos 30,
Aspandiat Mos. Kalank. I, 372, 378, 382—384 .-=
zd. speutodata-, gr. S^fFi'daddzfjc {Kte sis. s).
1123. Np. ya«a = ph.*i/asak setzt zd. ap. ^yfl^r/- voraus.
1st ayasa richtig und die altere Form, so ist eben
*ayasa anzusetzen und eine andere Etyniologie zu
--- leaf
leaf 116 printed page approx 106
```


## [2026-09-05T20:31:29.708Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; ls | grep -i \"ARY\\|aryanpur\"; echo \"=== CHEUNG\"; grep -n \"HaišH\\|HaisH\\|aēšma\\|aesma\" CHEUNG.txt | head -10",
 "description": "Find ARY and Cheung"
}
```


### [2026-09-05T20:31:29.771Z] TOOL RESULT

```
NYB_vol2_glossary.txt
=== CHEUNG
10996:*HaisH ‘to set in motion’ 
33210:aesma-, 157 
57793:*HaisH, *Har’, *kaiH, *zai'
```


## [2026-09-05T20:31:32.229Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '10990,11040p' CHEUNG.txt",
 "description": "Read Cheung HaisH"
}
```


### [2026-09-05T20:31:32.273Z] TOOL RESULT

```
*REFERENCES: Werba 1997: 162; ESIJa I: 124 


*Haiz 159 


*HaisH ‘to set in motion’ 

*AVESTAN: aëš- ‘to set in motion’ || (+ *pati-) ‘to restore, (?) permit’ || (+ *pari-) ‘to 
clean, gather ?’ (Kellens 1976: 91f.; Kellens 1984: 21 n. 1, 101 n. 1) || + *fra-) ‘to 
speed forward’ || Liste: 13 

Pres. {1} them.: IND. 3pl. OAv. isonti (Y 46.9), med. YAv. pairisonte (V 14.7), INJ. 3sg. YAv. isat (Vd 
2.32), SUBJ. 35р. paitisät (Y 44.2, Yt 13.137), 3р1. OAv. isántr (Y 45.7), YAv. paitisan (Y 60.6), med. 
YAv. pairisánte (V 6.8), OPT. 3pl. YAv. pairisaiianta (V 6.7), IMPV. 2р1. YAv. paitisata (Y 57.13); Pres. 
{2} 1а-: IND. lsg. OAv. fraeisiia (Y 49.6), 1р1. fraešiiamahi (Y 35.4, Y 61.1, Y 71.25, etc.), ҮАУ. 
fraesiiamahi (Vr 22.1, P 3(34)); Partic.: pres. {1} YAv. paitisant- (P 12 (13), Vyt 52), med. (ad hoc?) 
Y Av. paitiSana (Y 55.6; Kellens 1974: 323), med. caus. Y Av. para. “aéSaiiamna- (N 68) 

«OLD PERSIAN: (+ *fra-) frais- ‘to send forth’ = Kent: 164b 

Caus.: impf. IND. 159. fraisayam <f-r-a-i-8-y-m> (DB 1.82, DB 2.30, DB 2.82, DB 3.2, рв 3.13, DB 
3.30, DB 3.84), «f-r-a-i-&-[y]-[m]» (DB 2.19), <f--a-i-8-y-m> (DB 2.72), <[f]-[r]-[a]-[iJ-[8]-y-m> (DB 
5.7), 3sg. fraisaya <f-1-a-i-8-y> (DB 3.55, DB 3.60, DB 3.71) 

*MIDDLE PERSIAN: Q The formally and semantically similar BMP forms, MMP 
frystg, BMP plystk /fréstag/ ‘angel, apostle’ and BMP plyst’tn /fréstadan/ ‘to send’, 
sim., go back to *fra- + *staH. 

*PARTHIAN: frystg ‘messenger, apostle’ > DMMPP: 160b f. 

*KHOTANESE: (+ *4-) i8s- (15-) ‘to return’ (< inch. *ā-iš-s-) || (+ *pati-) OKh. patis- 
‘to withdraw’ || (+ *fra-) hei’- (etc.) ‘to send’ = SGS: 13, 14, 68, 154 f. 

*SOGDIAN: (+ *apa-) SSogd. pys- ‘to send off, away’ (SDMG II: 128) || (+ *fra-) 
SSogd. prys, BSogd. pr’’sy, CSogd. frys, SSogd. prysy (old caus.) ‘to send’ 

(+ *apa-) Pass.: pret. IND. 3sg. (?) SSogd. pyst ‘(the letter) was sent away’; Partic.: perf. pass. (?) SSogd. 
pyst || (+ *fra-) Widely attested: Pres.: IND. 15р. SSogd. pr'ys'm, OPT. 25р. SSogd. pryšyš, etc. || 
*CHORESMIAN: Q On Chor. pry- ‘to leave, let go; to repudiate (wife); to take out (+ 
с)’ see *HraH!. 

*NWIR: (+ *fra-) Zaz. ristis/risen- ‘to send’, (old caus. ppp.) NP firistah/firestah 
‘angel; messenger’ || (+ *ui-) ? Bal. gisit/gis- ‘to separate, untangle, divorce, 
straighten out, release’. 0 According to Shahbakhsh, Bal. gis- is probably a variant 
of géc- (*(Нуџаіё): the outcome -3- is typical for the eastern dialects of Bal. (cf. Korn 
2005: 229). 

*SANSKRIT: es ‘to set in motion’ (RV+) = EWAia I: 271 

«PIE *H;eisH»;- ‘to rush, impel, unleash, release’ = LIV: 234 | Pok.: 299 ff.
```


## [2026-09-05T20:31:42.771Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"یون:\" MON_part1.txt MON_part2.txt | head -10; echo \"=== IEC year\"; grep -n \"iēros\\|jēram\\|jēra-\\|iēro-\" IEC.txt | head -10; echo \"=== SYN year\"; grep -n \"^14.71\\|Latin annus\\|Goth. jer\" SYN.txt | head -10",
 "description": "Moin yon; Mann/Buck year"
}
```


### [2026-09-05T20:31:42.864Z] TOOL RESULT

```
MON_part2.txt:5331:قدراسیون: (سا.) اتحاد جند 
MON_part2.txt:5764:فراکسیون: ۵۲ (۱.) دسته‌ای از 
MON_part2.txt:16907:کاپیتولاسیون: «۰رعتاتآجت(.) حقی که 
MON_part2.txt:16936:الفای کاییتولاسیون: در سال ۱۹۱۷ م. 
MON_part2.txt:19569:کامیون: 0 (ا.) اتومسل بر رگ برای 
MON_part2.txt:22593:کرومانیون: ۵۲۵0۸ (۱.) ۳۳۹ از 
MON_part2.txt:26658:اجرای معاملات کنند. حق کسیون: حق 
MON_part2.txt:27233:کنسولتاسیون: ۱( ( مشاوره» 
MON_part2.txt:39364:لژیون: 27 (.) در روم قدیم؛ واحدی 
MON_part2.txt:65231:ملیون: 6111-09 [ع.] 9 ِ( 3 
=== IEC year
=== SYN year
24349:Grk. &pa ‘period of time’, in Hom. esp. ‘time of year, season’ or ‘fitting time’, later esp. ‘time of day, hour’, but wider use continued in part (so even NG kap- moon pa ‘considerable time, quite a while’) : Av. yara, Goth. jer, ete. ‘year’ (14.73), Slavie jaro ‘spring’ (14.75), all prob. fr. *yé-, yd- beside *yd- (cf. Skt. ya- ‘go’, Lith. joti ‘ride’, etc.), extensions of ei-, i- ‘go’. Walde-P. 1.105. Boi- sacq 1083.
25293:leing ‘daily’ Goth. jer, Av. yara ‘year’, etc. Walde-P. 2. Grk. ane ; 113}. Dor, a ‘népa, Dor. dutpa, poet. Fuap, OPers. rauca (xSapava raucapativa
25680:14.71 MONTH
25784:Boh. jaro, Pol. obs. jar, jarz, old jaro, Russ.-ChSl. jara : Goth. jer ‘year’, etc. (14.73). Berneker 446 f. Brickner 199.
```


## [2026-09-05T20:31:49.840Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"14.73 YEAR\\|14.72 HOUR\" SYN.txt; sed -n '24340,24355p' SYN.txt",
 "description": "Buck 14.72/14.73"
}
```


### [2026-09-05T20:31:49.894Z] TOOL RESULT

```
25709:14.73 YEAR Grk, gros, buavrds Goth. jér, abn, alapbni Lith. metaz NG 0500s, ros ON @ Lett. gads lat. annus Dan. ar ChSl.  léto : pO Sw. dr SCr. godina coal OE géar Boh. rok Ru eg ME ~ yeer Pol. rok ie Pe NE year Russ. god Nir Dliadain Du. jaar Skt. vatsara-, varsa-, ha- V . bliadhain OHG jar yana- Br, lwyddyn MHG jar Ay. yar-, sarad-, aeons NHG jahr OPers. @ard-
or in some cases specialized in
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
a Saree ©
Digitized by Arya Samaj Foundation Chennai and eGangotri
954 SELECTED INDO-EUROPEAN SYNONYMS
Some of the words for ‘time’ are from roots for ‘stretch’ or ‘measure’, with es- tablished temporal, rather than spatial, application. Others are of diverse and partly obscure orig.
Besides the most generic terms, there are others which are used mostly for a point or period of time (not time in its duration). These may become more generic (as Grk. xacpés) but, more fre- quently, are further specialized (e.g. to ‘year’, ‘day’, or esp. ‘hour’) or restricted to certain phrases (e.g. NE while).
1. Grk. xpévos, etym. dub. Possibly, with analysis xp-dvo-s (cf. @p-dvo-s) and as orig. ‘the comprehensive’, fr. the root seen in Skt. Ar- ‘bring’, Osc. heriiad ‘capiat’, etc. Boisacq 1071 f.
Grk. xatpés ‘fitness, opportunity’ and esp. ‘fitting time, season’, used of special times, not duration of time, but in NG the pop. word for ‘time’ (xpévos pop. ‘year’), root connection dub., perh. best as orig. ‘section of time’ fr. *kap-.ds : kelpw ‘cut off, shear’, etc. Walde-P. 1.419, 2.584. Boisacq 538 ftn. Walde- H. 1.206.
Grk. &pa ‘period of time’, in Hom. esp. ‘time of year, season’ or ‘fitting time’, later esp. ‘time of day, hour’, but wider use continued in part (so even NG kap- moon pa ‘considerable time, quite a while’) : Av. yara, Goth. jer, ete. ‘year’ (14.73), Slavie jaro ‘spring’ (14.75), all prob. fr. *yé-, yd- beside *yd- (cf. Skt. ya- ‘go’, Lith. joti ‘ride’, etc.), extensions of ei-, i- ‘go’. Walde-P. 1.105. Boi- sacq 1083.
2. Lat. tempus (> Romance words), etym. much disputed, but prob. as ‘stretch of time’ : Lith. tempti ‘stretch’, etc., fr. *tem-p-, beside *ten-d- in Lat. tendere ‘stretch’, extension of *fen- in Skt. tan-, Grk. retvw ‘stretch’ (cf. Ir. tan, below, 3). Walde-P. 1.721. Ernout-M. 1025 f. (without etym.).
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Se ee ee See ee
Rum. vreme (mostly replaced now in lit. language by timp), fr. Slavic (cf below, 6). Tiktin 1780 f.
3. Ir. aimser, ete., general Celtic deriv. of simple form in Ir. amm ‘time, occasion, point of time’, NIr. am (gen eral term now; aimsir esp. ‘weather’, cf. McKenna), etym.? Pedersen 1.80.
Iv. tan, rare in later period in lit. sense, mostly used as conjunction in tan, mm tain ‘when’ : Skt. tan-, Grk. rely, Lat. tendere ‘stretch’. Walde-P. 1.723, Stokes 128. Otherwise Pedersen 2.14,
```


## [2026-09-05T20:31:57.278Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"jēros\\|jeros\\|iero-s\\|jēro-\\|jēr\\b\" IEC.txt | head -10; echo \"---\"; grep -n \"Goth. jēr\\|Goth. jer\\|OHG. jār\" IEC.txt | head -10; echo \"--- eismos\"; grep -n \"oismos\\|aēšma\\|aesma\" IEC.txt | head",
 "description": "Mann IEC greps"
}
```


### [2026-09-05T20:31:57.369Z] TOOL RESULT

```
---
--- eismos
```


## [2026-09-05T20:32:00.886Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; wc -c IEC.txt; grep -c \"\" IEC.txt; grep -n \"Goth\\. jer\\|jer 'year'\\|Av. yār\" IEC.txt | head; echo ---; grep -in \"isarnom\\|isarno\" IEC.txt WLD*.txt 2>/dev/null | head; ls | grep -i WLD",
 "description": "IEC size and WLD files"
}
```


### [2026-09-05T20:32:00.991Z] TOOL RESULT

```
3311889 IEC.txt
20499
6489:ior- (1) “time, period". C£. WP I, 3 & 105, and iér-. (Indo-Iran. ambig.) Av. yārə “year”; OPer. -yara “year, season’; Gk. hóros, bor, id.; LW in Lat. hora & Alb. herë ‘time, fois’; Lat. cf. h-ornus (“of this season or year”, fr. *ho-ior-, cf. ho-die); W cf. ior *eter- nal: ON cf. ent ‘younger’; also (?) oeska (Cchildhood', if. for *ioriska); Srb. jàr ‘heat’; OCz. j&t “spring; spring corn’; Cz. jaro ‘spring’; Blg. jarà ‘reflected glow’; Slovak jar, f. ‘spring’: Slovene jar ‘precocious’; Ukr. jaryj, adj. ‘springtime’; R jarovój summer": jàrka “year- ling ewe
---
IEC.txt:6258:(Isernos, om ‘iron’. Celtic and Gmc. Prob. a LW in Gmc. Cf. WP I, 4 Mir íarnn, n.; Ir. iarann, m.; OCor. hoern; Gaul. isarno-; Br. huarn; W haiarn; Go. eisarn, n.; OE isern, Isen, iren, n.; ON ísarn, járn; MHG īTser, id. (Per. ahan ‘iron’ is of uncertain origin))
WLD_band3.txt
```


## [2026-09-05T20:32:08.567Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^iér-\\|iér- \\|iēr-\" IEC.txt | head -5; echo ---; grep -n \"^ei- \\|eimi\\|Gk. eimi\\|^ei-\" IEC.txt | head -8; echo \"--- WLD3\"; grep -n \"iero-\\|iēro\\|eis-\" WLD_band3.txt | head -10",
 "description": "Mann ier- and ei-; WLD index"
}
```


### [2026-09-05T20:32:08.654Z] TOOL RESULT

```
16137:sKiros (skiros) (2) “clear, bright; clarity, bril- liance'. WP IL, 536. A Germanic form of type sKiér- occurs as a variant Alb. hir, m. ‘grace’; Go. skeirs, adj. “clear, bright"; OE sar, ON skírr, Sw. skir, id.; OCS Stirü, adj. ‘whole’; Pol. szczery, adj. “honest, pure’; Ukr. SCyryj, adj. ‘sincere’; Cz. čirý, adj. ‘sheer, mere’. (NB. A variant of type *skiër- arises in E sheer, G schier “clear; slim; dainty’, and in Sw. skär ‘clear, pure’. Mod. Icelandic has skir & skýr in the same sense. OHG displays the variants skëri, and the adv. skéro, sciaro “sharp; quickly")
---
554:anguos, om, à (?) ‘limb; gait’. Cf. anguó Skt. (ambig.) ángam; cf. Gk. -ambos in the cpds. thrí-, í-, dithur-, itthumbos (see dhreiu-, i- and eimi, didhur-, suidh-); cf. kher-ámbe (a mollusc: *hand-limb'. Pelasgian wds. accdg. to H. Frisk GEW)
3418:Av. dvar(eimi), v. ‘rush’; Gk. thoüros “rush- ing’; Ir. duar ‘crowd’; cf. also Skt. a-dhvaráh (a religious ceremony); Sw. däre "Tool dhuoros “entrance, court. WP I, 871. Cf. dhuer-, dhur- Lat. (ambig.) forus *hatchway'; forum *mar- ket; OCS dvorü (and com. Sl.) ‘court, yard’; Li. dváras (farm. Perh. SI. LW) dhuos- *drooping, ailing; spirit, exhalation, expiry’. Cf. dhues-, dhus- Skt. cf. (ambig.) dhvasrah *withered"; MIr. dássaim *madden'; EME cf. dwas-light *will- o"-the-wisp'; Sw. dåse (“sluggard”, cf. E dial. dozy, fr. Scand.); dásig ‘sleepy’; Li. dvásas, dvasià ‘spirit’; dvasus ‘ailing, pining (dhuriə, a zero-formula to dhuer-, dhuor-, dhur- ‘door’. etc.) WP I, 870 Gk. thairós singularized: ‘hinge of door
3461:eigh- ‘force, strength’. Cf. iegua Skt. cf. ihah, -ā (2) ‘effort’; Ir. éin, adj. (Cable, fr. *eighin-?); Li. eigà Cporocessg Cf. *ei-, *i- “go? under eimi); o-gde in Go. aih (pf.-pres.
3471:eik- “go; vanish; perish’. (Extn. of ei-, i- ? See eimi below) Tokh. B yk- "on: Gk. (ambig.) eíko “withdraw, yield”; oke adv. “in vain’; cf. (?) pro-ika ‘gra- tis’; pro-ix, -ikós “gif: Alb. ik “flee, depart; Umb. eikvas-atis (in phr. ahtis-per.. . ‘for de- parted souls'?); Li. cf. eikvoti ‘squander’ be- side eiklüs ‘nimble’. (Isophonic are Lat. 1co, ere; OLat. eic- "strike
3474:eimi (eio) ‘go’. WP I, 102. (Plural forms: i-) Skt. émi, 1 pl. imáh; Av. aei(mi); OPer. ay-; Hitt. cf. ca-imi, cpd.; Myc. ijon, pr. pt. “going; Hom. eimi, pl. men: pr. subj. eið, íð; EMAlb. íhem (-h- due to hiatus, or fr. *-sK-); Lat. eo, īre; Pael. cf. eite! *go!; Umb. etu, 3s. jussive; W âf “shall go? beside awyf “may I go’; Br. an, 1s. pr.; inn, 1sg. fut.; EMLi. eimi; Latv. eimu, iemu, eju, id. Cf. Latv. eja ‘path’ & Li. eimé! let's go!
3477:eiså, io (ois-) ‘go, dash, impetus, outburst’. Cf. eismn-, oisá, eimi Skt. (ambig.) éSa ‘search; desire’; Lat. (ambig.) ira ‘anger’; Icel. cf. írafár *overhaste'; Li. cf. eislùs ‘going’; eisena ‘gait’
3479:eisio ‘shall go’. Cf. eimi Skt. esyàmi; Gk. eið (pres. subj.); Li. eisu, ei- siu; Latv. iešu (The Li. form eisu is that of the Bible translation)
3484:eiuem ‘all right, come on! Skt. evám, id.; Gk. eien, id. (Li. isophonic eivà! is a dual form of ei-, see eimi)
--- WLD3
3009:erquicken 1. eis- 106, fallen L. Had-'339. | Fell 11, pel- 55*,
3128:(tierischer) 3. yeis- 245. z: oh3. 1. ba- 122 mammeln 862. gfe SP. Ll. ker- 413. echeifan Ghed- 571
3214:“s erg tn welzen d- 613. | wohl ql 3236 Shenk 401, | wickeln 7. wes BUD. wohlbeholien ile 510* wat 212." | Wider ef- 854. | wolilgensigt (sein) ans- 68. L, wd 224), widerwartly ; 1. | wo t megh- 256 dhewes- B43 mt | tgs me it ace kei oe | re ™ i dhem- 85] Widorwitle 2, 0d 174 Wohnraum 2. qef- 333, ea. Gr", ote gners 1 <t SO epee- Bat" Wo tret- 757. ua 1, Wiedehopt (RB Wolf yasloy 213, gioje 061, | Wiedorkduen. rewmen- sae a Biméei 244%. | cum duc ter, | Welko 2 (enebi-) ASL. : ili 103, | Wiesel kek meis- 245°, Wag aide. | wild Leveu- 840%. | Cauaktey eae bage . ja" Willena sein 4. md- 238°. Walle 4. wer- 260 * pai) 72* willkommen bhelgh- 182° | 4. yel- 200. ghei- G91, | Willkommen heifen 2, pel’. 16°. qlam- 400, ae 7. mel- 204". Ag. G2. 2, (dew-) 778. | wollen 3 uai- 228, Kyeit-'4i0. | Wimmeln 2. we | weak: 24a. dhereg- 17s.) Winden = 2. 2, yet 20M. | t es yazih- 220 | 1. efi} 303". er- £86, “ | Wollflocke bAl6k- 217", reves 356°. : Wollllocken  plews- 96°. (iro Ti. 5 Wollzewand 7. mel- 204". _ Salons 748 Wolltier 4 ri 200. 2. yendh- 261 wollisti, a\lég- T12*. ld 3a ican Lane 12 ‘ srt ae ome irep- Tot. Tok ae dhergh 963, | Wintligen 1 9 yell 293, | Windung ju- 75". 4 a Sepa Winter 2 w- 45ge. | ion wirbeln qeerp- GOL, 2. =: EVEN, eae anne. AE egal wirken 2 508*- | wischen
```


## [2026-09-05T20:32:19.818Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== PHD yairka/hirak\"; grep -n \"yʾyrk\\|yairk\\|hyrk\\|hirak\" PHD_mackenzie.txt | head; echo \"== NYB xesm\"; grep -n \"xēšm\\|xesm\\|xism\\|hesm\" NYB_vol2_glossary.txt NYB.txt NYB_vol1.txt 2>/dev/null | head; echo \"== NYB files\"; ls NYB*; echo \"== ARB/ARP\"; head -3 ARP.txt",
 "description": "More checks"
}
```


### [2026-09-05T20:32:19.893Z] TOOL RESULT

```
== PHD yairka/hirak
== NYB xesm
NYB_vol1.txt:8722:‘hsm: hesm‏ 
NYB_vol2_glossary.txt:1986:hesm [hsm] fuel 443. 4815-16, — Borrowed from Av. (26)aésma- < *aizma-, NW *hézm, whence NP hčzum, hézam; SW *aióma- > *ēhm > "em, v. ēmak.
NYB_vol2_glossary.txt:1990:hesm
NYB_vol2_glossary.txt:2842:oškan [>wškn'] a verbal form used as pt. pass. and as pret. pass. 3d p. sg., to *throw: aš 6 pasēh gav apāc rānēnīt (g. v.) with the gl. kü apāc ~ ‘that is: it (his hand) was flung backward’ 485 -$; 62 gurg zat zanak (g. v.) with the gl. ki dahan évak apäk dit frot ~ ‘that is: his jaws were clasped together (the upper jaw was clasped down against the lower jaw)’ 5067; [(ka) dēn-ākāhēh ~ (when) reli- gious knowledge is overthrown DkM 33379; ātaxš mänäk aparociónik hesme m hàn i xét like a fire which has to be kindled but is thrown into wet fuel, ibid. 411°]. As it stands, this form can only be derived from *avis-kan- (the root *kan- ‘to throw’ found, e. g., in apakan- dan, q.v.), thus originally *avis-kanta- > *ēškand > oškann with assimilation of -nd > -nn, but the form is singular, as only old -nd, as far as we know, under- went this assimilation, not -nd- < -nt-. The inf. of this vb. shows the regular form expected: cé andar én mātagdān 6s- kandan [’wSkn'dn'] apāyišnīk dart druš- take [-k' +1, for -keh] vicārihēt ‘the (trouble-hardness =) troublesome diffi- culties which in this book inevitably
NYB_vol2_glossary.txt:4005:frasang many parasangs 7%; ~ simén, ~ asp névak 1965; — with a personal subst.: —-än martöm (cas. obl.) 418, but also ~ frazänak martom (cas. obl.) 455; ~ āzātān u vazurgän (cas. obl.) 16°; ~-dn vazurg-spāsān (for cas. rect.) 1061; — less often placed after its subst. without or with the izGfat: névakéh ~ 351; anākēh ~ 95* (as against pat ~ andkéh 761); hesm i ~ 4815; gāvān + ~ 483-26; aspān i ~ 4013, — 2. as a pred.: numerous, great 41, 201? sq. 871; — in a compound: hesm ~ quick to anger 1074. — 3. subst. pl. cas. obl: 6 ~-dn to many people 3643 and passim. — 4. adv. very: ~ vazurg 8’; ~ pahréc 55°; — ka —-ic however much 463, 8122-23, 9112. — OP vasiy; MPrthPrs ws; Paz. vas; NP bas.
NYB_vol2_glossary.txt:4945:aésma-: hesm
NYB_vol2_glossary.txt:7202:hézum, hézam: hesm
== NYB files
NYB.txt
NYB_vol1.txt
NYB_vol2_glossary.txt
== ARB/ARP
0^/^ilfi^^/^  Ry^>(a  tfe.'^v^ÄJ^'^y^Tt^
>>
.'^/^^^yilG^.'^
```


## [2026-09-05T20:32:37.045Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"wrath\\|Wrath\" NYB_vol2_glossary.txt | head -8",
 "description": "Nyberg wrath"
}
```


### [2026-09-05T20:32:37.092Z] TOOL RESULT

```
1267:*depasten ["dypstyn'] "full of wrath 10316, — Cf Ps. dypsty, dypsny rendering Syr ruģzā ‘wrath’. Text spspyn’, correct- ed by Dhabhar to spstyn' and combined with NP sapist 'nasty'. This spstyn' may, however, be read dypstyn' as well; the assumed meaning of this w. would suit the context better. [MPrs ^npspyn M 985 (S) is indistinetly written and guite uncertain].
1287:distak [dystk'] *treated, manipulated, or the like: pat Hēšm zahr ~ "treated with (the demon) Wrath's poison 2516-17 = 2814, — In the edition the first letter is a marked d, hence the reading dystk' is cogent. Because of -ist- this must be a SW form corresponding to a NW form with -i$t-, but its meaning in this context make it impossible to combine it with NW dištan (v. next w.): a weapon is not “built” or “‘formed’’. It would be tempt- ing to connect it with Skr dih- ‘to daub, to smear', but the corresponding Av. (673) dačz- has other significations (cf diz), and the Phl. renderings of it (Vd 39.13.18, 733. 1536) have run wild and are no more recognizable (they can scarcely be brought together with dés-, v. the next w.).
1987:hēšm [hyšm, hšm] wrath, anger: Artax- šer ~ grift A. was seized by anger 37; ~ kartan to become angry 154. 6815; ke ~ 6 tan nē hilét who leaves no room for anger 8414; ~ vas quick to anger 10?!; ~ rād dāšt persisted in his anger 101°; tāi bē nišastan à ~ until the anger sub- sides 6817-18; the work of Ahriman is ~ u kén u anästeh 7822; ~ u ken räd 14%; - personified as a demon, one of the chief evil powers: ~ dev 6123: equal to Ahri- man 68%; in company with Az 103°;
1993:the opposite of Vahuman 654-5; Srēš his chief adversary 665. 7711, 2516, 2814 v.s. v. distak; — his epithets: mūtak and tanäpuhrak 619%; zürdrus 7211-12, 103977; v. these ws. — Av. (35 sq.) aēšma- (Asmodatos, Book of Tobit 3:8 Av. ačšmo.dačva-); MPrth ‘smg’n ‘devils of wrath’; MPrs xysm; Paz. NP rašm, zism.
1995:hčšmakan [hyšmkn'] angry 1422. abstr. x(a)šmagami Antià 1235. hešmēh [hšmyh] an outburst of fury 6815. — Probably only kēšm + the indef. art. -€: ~ mà kun, ce mart ka hešm kunet ... Paz. substitutes xašmgini (cf the preceding w.), Skr. v. kopa. hešm-kāmakihā [hšmk”mkyh”] in the manner of one whose volition is deter- mined by wrath, furiously 7425, Paz. zasm-kämihä.
3109:must go back to *pati-yam- ‘to take hold of’, from Av. (1262sg.) yam-, chiefly with preverbs. I find *pāyam as a v. n. in two passages: 1. DkM 285 aköman ... menisn päyam ‘A. holding Mind in his grasp’; 2. ibd. 501? páyam hešm andar ménisn “Wrath taking Mind in his grasp’ (?). — Zsprm VIII, 4 has a somewhat divergent, perhaps more original version of the story 441-9: ^L ZLWN ‘L y’twk’n, MH-t L>? HWH-nd byšznyt'l, BR’ L'WHL ‘L h'nk' ZLWN, YDH BYN ml PWN "MŠH' ZY TWR’ ZY MDM thé YDLWN-t', hysme bwd wt'p' PWN NPSH-tn' zhk' MNW-t PWN 'škmb' = mà šav o yātūkān, cē-t nē hend bēšazanī- tar, bē apāc 6 xanak šav, dast andar mal pat rógn % gāv i apar ātaxš burt, hésm-ic bod vitāp pat x"ēš-tan zahak ké-t pat aš- kamb ‘do not go to the sorcerers, for they cannot heel thee, but go back home, rub thy hand with ox-tallow which has been. set on fire, and burn fragrant fuel for the benefit of thy offspring which is in thy womb’.
3435:*sim-depahr [symdyphl] "of horrid wrath 2222. — Hypothetical. Av. (1580) sima- ‘terrifying, horrid’; depahr ‘wrath’ (g.v.) suits the context well, but it ought to have been spelt dyp’hl. As it now stands the 2nd element looks like sp'l = spār, but I fail to see what this would mean here.
3717:tanäpuhrak [tn’pwhlk'] guilty of a tanä- puhr sin, 1.e. of a deadly sin which can only be atoned for by hard flogging or (later) by a very high fine, and which involves the excommunication of the eulprit until he has suffered his punish- ment; applied to Hésm, the demon of Wrath: the originator of deadly sin 61, — Adj. of tanäpuhr, the Milr. adaption of Av. (636 sq.) tanu.parada- ‘whose body is forfeited’, thus an adj. whereas BP tanüpuhr is used as a subst. for the sin itself. f
```


## [2026-09-05T20:32:53.921Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for f in POK_01.txt POK_02.txt POK_03.txt; do echo \"== $f\"; grep -n \"^501$\" $f | head -3; done",
 "description": "Find Pokorny page 501"
}
```


### [2026-09-05T20:32:55.616Z] TOOL RESULT

```
== POK_01.txt
== POK_02.txt
== POK_03.txt
```


## [2026-09-05T20:34:08.207Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^ *501 *$\" POK_0*.txt POK_full.txt | head; echo ---; grep -n \"501\\b\" POK_02.txt | head -5; echo \"=== try full with page tags\"; head -20 POK_full.txt",
 "description": "Pokorny page 501 search"
}
```


### [2026-09-05T20:34:08.278Z] TOOL RESULT

```
---
1886:WP.  I  668  ff.,  Meillet  Introduction^  165,  Specht  KZ.  62,  111,  Schwyzer Gr.  Gr.  I  298,  300,  330,  501^  675«,  Trautmann  75  f.
4493:Ai.  kßipdti   ,wirft,    schleudert',  Kaus.  ksepdyati,    ksiprd-h   ,schnell';    mit Media  aksl.  osiba-jg,  -ti  ,sich  abwenden',  russ.  lihdth  , werfen',  sibkij  ,schnell', ^sibdth  , abschlagen',  osibdhsja  ,sich  irren'. WP.  I  501.
=== try full with page tags
List of language abbreviations in tlie lED 



Abbreviation Language name 


Aeq. 




Aequian 


Akk.
```


## [2026-09-05T20:34:13.269Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for f in POK_01.txt POK_02.txt; do echo \"== $f\"; grep -nE \"^[0-9]{3}$\" $f | head -3; grep -nE \"^[0-9]{3}$\" $f | tail -3; done",
 "description": "Pokorny page marker ranges"
}
```


### [2026-09-05T20:34:15.158Z] TOOL RESULT

```
== POK_01.txt
1347:100
1357:101
1381:103
5030:337
5069:339
5118:341
== POK_02.txt
17:350
35:351
52:352
6644:759
6673:761
6698:763
```


## [2026-09-05T20:34:18.323Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; n=$(grep -nE \"^50[01]$\" POK_02.txt | head -2); echo \"$n\"; ln=$(grep -nE \"^500$\" POK_02.txt | head -1 | cut -d: -f1); echo \"line $ln\"; sed -n \"$((ln-30)),$((ln+40))p\" POK_02.txt | head -80",
 "description": "Read Pokorny page 500-501"
}
```


### [2026-09-05T20:34:20.287Z] TOOL RESULT

```
line 
sed: invalid option -- '3'
Usage: sed [OPTION]... {script-only-if-no-other-script} [input-file]...

  -n, --quiet, --silent
                 suppress automatic printing of pattern space
      --debug
                 annotate program execution
  -e script, --expression=script
                 add the script to the commands to be executed
  -f script-file, --file=script-file
                 add the contents of script-file to the commands to be executed
  --follow-symlinks
                 follow symlinks when processing in place
  -i[SUFFIX], --in-place[=SUFFIX]
                 edit files in place (makes backup if SUFFIX supplied)
  -l N, --line-length=N
                 specify the desired line-wrap length for the `l' command
  --posix
                 disable all GNU extensions.
  -E, -r, --regexp-extended
                 use extended regular expressions in the script
                 (for portability use POSIX -E).
  -s, --separate
                 consider files as separate rather than as a single,
                 continuous long stream.
      --sandbox
                 operate in sandbox mode (disable e/r/w commands).
  -u, --unbuffered
                 load minimal amounts of data from the input files and flush
                 the output buffers more often
  -z, --null-data
                 separate lines by NUL characters
      --help     display this help and exit
      --version  output version information and exit

If no -e, --expression, -f, or --file option is given, then the first
non-option argument is taken as the sed script to interpret.  All
remaining arguments are names of input files; if no input files are
specified, then the standard input is read.

GNU sed home page: <https://www.gnu.org/software/sed/>.
General help using GNU software: <https://www.gnu.org/gethelp/>.
```


## [2026-09-05T20:34:23.017Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -nE \"^49[5-9]$|^50[0-5]$\" POK_02.txt | head -12",
 "description": "Pokorny markers near 500"
}
```


### [2026-09-05T20:34:24.732Z] TOOL RESULT

```
2301:495
2422:505
```


## [2026-09-05T20:34:27.834Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=2301 && NR<=2422' POK_02.txt | grep -nE \"^[a-zA-Z].{0,60}$|gehen|Jahr\" | head -40",
 "description": "Pokorny pp.495-505 headwords"
}
```


### [2026-09-05T20:34:29.822Z] TOOL RESULT

```
3:g^hr^-ns-o-  (auf  Grund  eines  es-St.  gVire-nes-) -.
5:WP.  I  687  ff.,  WH.  I  532ff.,  Trautmann  79,  102.
6:gbuoig"-  ,leuchten,  Schein'.
14:g^hre-  , riechen,  wittern,  spüren';  g^hre-ti  ,Riechen'.
17:toch.  A  kram,  B  kor  ,Nase'.
18:WP.  I  697,  WH.  I  540.
23:WP.  I  699.
24:H.
27:ha  ha!    Interjektion  des  Lachens.
33:lett.  lls  /jStockfinster'  {Hlus))
35:WP.  I  163,  Trautmann  103.
36:ili-  ,Weichen,  Eingeweide,  Geschlechtsteile'?
41:WP.  I  163  f.,  WH.  I  673  f.
47:av.  yä-tu-  m.  , Zauberei,  Zauberer',  yä-sä  ,Wunsch';
53:iä-  jgehen'  s.  oben  S.  296.
54:iag-  ,religiös  verehren';  iagos-  n.  ,Verehrung'.
62:WP.  I  195,  Schwjzer  Gr.  Gr.  I  303.  ^
63:iagh-  _,nachjagen,  begehren^?
66:WP.  I  195  f.
67:iäi  s.  oben  S.  285.
68:räzn-  (oder  iem- :  i^m- :  iöm-)  ,graben,  aufgraben^.
71:WP.  I  198  f.,  Berneker  444.
72:iäm  s.  oben  S.  285.
82:feg-  ^Eis^;  nur  germ.  und  kelt.
88:ihilla  (=  *jichilla)  ,stiria' ;
93:ieg^ä  ,Kraft,  Jugendkraft^
97:WP.  I  206f.,  Trautmann  107.
98:iek-  ,sprechen^,  auch  von  feierlicher,  bittender  Rede.
107:iek-  :  pk-  ,heilen^  ?
111:m^-l{t-),  Gen.  iek^-n-6s  ,Leber^
113:gr.  ^rcaQy  -arog  {^-V'-tos);
118:Eine  uridg.  Grundform  *liekurt  scheint  mir  zu  gewagt.
```


## [2026-09-05T20:36:36.185Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== AHD WIDE\"; grep -on \"WIDE [a-z()-]*[0-9]*\" AHD_watkins1985.txt | head -5; echo; grep -n \"wi-. Apart\\|^wi-\\. \\|wi-ito-\\|Apart, in half\" AHD_watkins1985.txt | head -5; echo \"== MON yon\"; grep -nE \"^یون|یون\\b\" MON_part1.txt MON_part2.txt | grep -i \"یون:\" | head -5; grep -n \"یون: \" MON_part1.txt MON_part2.txt | head -5",
 "description": "AHD wi- root; MON yon"
}
```


### [2026-09-05T20:36:36.287Z] TOOL RESULT

```
== AHD WIDE

1167:wi-. Apart, in half. 1. Suffixed form *wi-itos in Germanic *widaz in Old English wid, wide (< “far apart”): WIDE. 2. Suffixed (comparative) form *wi-tero- in Germanic *withr6, against, in: a. Old English wither, against, with its derivative with, with, against: WITH, WITHERS; b. Old High German widar, against: GUERDON; WITHERSHINS. [Pok. 1. wi- 1175.]
== MON yon
MON_part2.txt:5331:قدراسیون: (سا.) اتحاد جند 
MON_part2.txt:5764:فراکسیون: ۵۲ (۱.) دسته‌ای از 
MON_part2.txt:16907:کاپیتولاسیون: «۰رعتاتآجت(.) حقی که 
MON_part2.txt:16936:الفای کاییتولاسیون: در سال ۱۹۱۷ م. 
MON_part2.txt:19569:کامیون: 0 (ا.) اتومسل بر رگ برای 
MON_part2.txt:5331:قدراسیون: (سا.) اتحاد جند 
MON_part2.txt:5764:فراکسیون: ۵۲ (۱.) دسته‌ای از 
MON_part2.txt:16907:کاپیتولاسیون: «۰رعتاتآجت(.) حقی که 
MON_part2.txt:16936:الفای کاییتولاسیون: در سال ۱۹۱۷ م. 
MON_part2.txt:19569:کامیون: 0 (ا.) اتومسل بر رگ برای
```


## [2026-09-05T20:36:47.121Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 120 python3 tools/fetch_source.py \"https://fa.wikipedia.org/wiki/%DB%8C%D9%88%D9%86\" --note \"page 149, Persian یون 'ion' — confirming the word and its European-scientific origin\" 2>&1|tail -1",
 "description": "Fetch fa.wikipedia yon"
}
```


### [2026-09-05T20:36:49.780Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/ac9aa625b58b751c.txt
```


## [2026-09-05T20:36:52.612Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; sed -n '1,5p' ac9aa625b58b751c.txt; grep -n \"یون\" ac9aa625b58b751c.txt | head -6",
 "description": "Check fa wiki yon"
}
```


### [2026-09-05T20:36:52.667Z] TOOL RESULT

```
URL: https://fa.wikipedia.org/wiki/%DB%8C%D9%88%D9%86
FETCHED: 2026-09-05T20:36:49Z
STATUS: 200
TITLE: یون - ویکی‌پدیا، دانشنامهٔ آزاد

4:TITLE: یون - ویکی‌پدیا، دانشنامهٔ آزاد
6:یون - ویکی‌پدیا، دانشنامهٔ آزاد 
59: انرژی یونیزاسیون 
62: روش‌های یونیزاسیون 
65: یون‌های رایج 
68: کاربردهای مواد یونیزه
```


## [2026-09-05T20:36:59.217Z] TOOL CALL #87: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg149.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/149.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -5",
 "description": "Copy page PNG for audit"
}
```


### [2026-09-05T20:36:59.283Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  90918 Sep  5 10:16 92.png
-rw-rw-r--  1 sfmqrb sfmqrb  93420 Sep  5 10:18 94.png
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-05T20:46:00.608Z] TOOL CALL #88: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-149.json <<'JSONEOF'\n{\n  \"pdf_page\": 149,\n  \"book_page\": 119,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Ei, Ey, I 1, Iâ 1\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *h₁ey- 'to go' (Pokorny 1. ei- 293), with the zero grade *h₁i- and the extended stem *yeh₂-/*yā- 'to go' (Pokorny 501, cross-referring to p. 296)\",\n      \"note\": \"The root box is right: Pokorny IEW 293 heads the entry 'I. ei- ,gehen', erweitert ei-dh-, ei-gh-, i-tā- und i-ā-, i-e- : iō- : iə-; Nominalbildungen i-to-, oi-uo-, oi-to- und i-ter, Gen. i-ten-os ,Weg'', and p. 501 carries the cross-reference 'iā- ,gehen' s. oben S. 296', so Nourai's four citation forms Ei / Ey / I 1 / Iâ 1 are exactly Pokorny's ei- / i- / iā-. Watkins/AHD 'ei-¹. To go. [Pok. 1. ei- 293]' and Wiktionary *h₁ey- agree. Two structural problems on the chart, neither of them in the root box: (a) the whole 'year' branch (#5) hangs on this root only in the older (Pokorny/Klein/Watkins) analysis — Beekes and current Wiktionary keep *yóh₁r̥ 'year' apart from *h₁ey- and connect it at most with *(H)yeh₁- 'to send'; (b) node #9 (Latin Jānus) is drawn under the YEAR node, but AHD and Pokorny both place iā-no- under the 'go' root itself, not under iē-ro- 'year' — Nourai seems to have followed the physical layout of Pokorny p. 296, where the iā- section and the iēro- section stand next to each other. Two printed forms are corrupt: 'ieani' (#1, for Greek ienai) and 'yâ-mo' (#9, for *yā-no-); both are the book's own misprints, faithfully extracted.\",\n      \"note_fa\": \"جعبهٔ ریشه درست است: پوکورنی در صفحهٔ ۲۹۳ کتاب خود ریشهٔ «ei- ‹رفتن›» را با گسترش‌های ei-dh-، ei-gh-، i-tā-، i-ā- آورده و در صفحهٔ ۵۰۱ نیز ارجاع «iā- ‹رفتن›، نگاه کنید به ص ۲۹۶» را ثبت کرده است؛ پس چهار صورتی که نورایی می‌آورد (Ei، Ey، I 1، Iâ 1) همان ei- / i- / iā- پوکورنی است. واتکینز در پیوست ریشه‌های هندواروپایی و ویکی‌واژه (*h₁ey-) نیز همین را می‌گویند. دو اشکال ساختاری در نمودار هست، هیچ‌کدام در خودِ جعبهٔ ریشه: نخست آنکه شاخهٔ «سال» (گرهٔ ۵) تنها در تحلیل کهن‌ترِ پوکورنی و کلاین و واتکینز به این ریشه بسته می‌شود و پژوهش امروزی (بیکس و ویکی‌واژه) واژهٔ *yóh₁r̥ «سال» را جدا می‌داند؛ دوم آنکه گرهٔ ۹ (ژانوسِ لاتین) زیر گرهِ «سال» کشیده شده حال آنکه جای درست آن مستقیماً زیر خودِ ریشهٔ «رفتن» است. افزون بر این، دو صورت چاپی نادرست است: «ieani» به جای ienai یونانی و «yâ-mo» به جای yā-no-؛ هر دو خطای چاپی خودِ کتاب است و استخراج داده‌ها امانت‌دارانه انجام شده.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81ey-\",\n        \"https://www.etymonline.com/word/ion\",\n        \"https://www.etymonline.com/word/January\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:293\", \"status\": \"supports\", \"note\": \"POK_01.txt line 4246 (page marks 291/294 either side): 'I. ei- ,gehen', erweitert ei-dh-, ei-gh-, i-tā- und i-ā-, i-e- : iō- : iə-; Nominalbildungen i-to-, oi-uo-, oi-to- und i-ter, Gen. i-ten-os ,Weg'. Ai. imi, ēti, imáh, yánti ,gehen', av. aēiti, yeinti, apers. aitiy ,geht''. Exactly the root box as drawn.\"},\n        {\"ref\": \"POK:501\", \"status\": \"supports\", \"note\": \"POK_02.txt line 2353, between the standalone page marks 495 (line 2301) and 505 (line 2422): the I- section carries the cross-reference entry 'iā- ,gehen' s. oben S. 296.' — i.e. Nourai's fourth citation form 'Iâ 1 : to go' is Pokorny's iā-, referred back to the ei- entry.\"},\n        {\"ref\": \"KLN:825\", \"status\": \"partial\", \"note\": \"Klein 1966 leaf 445 (running page numbers 824/825 printed on the leaf), s.v. janitor: 'L., formed with suff. -tor fr. jānus, ‘a covered passage, arcade’, which is of uncertain origin. It is perh. cogn. with OI. yānaḥ (masc.), ‘path’, … ‘a going’, yāti, Avestic yāiti, ‘goes, travels’.' Klein therefore supports the *yā- 'go' connection but calls jānus 'of uncertain origin' and only 'perh. cogn.' — looser than Nourai's arrow.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, e-list (AHD_watkins1985.txt line 428)\", \"stance\": \"supports\", \"note\": \"'ei-¹. To go. 1. Full-grade form *ei- in: a. Latin ire, to go … b. Greek ienai, to go: ION … 4. Extended form *yā- (< *yaə-) in suffixed forms *yā-no-, yā-nu- in: a. Latin Jānus, archway, and Jānus, god of doors and of the beginning of a year: JANITOR, JANUARY, JANUS … [Pok. 1. ei- 293.]'\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, s.v. eimi (IEC.txt line 3474)\", \"stance\": \"supports\", \"note\": \"'eimi (eio) ‘go’. WP I, 102. (Plural forms: i-) Skt. émi, 1 pl. imáh; Av. aei(mi); OPer. ay-; … Lat. eo, īre' — the same root, referred to Walde-Pokorny I 102.\"},\n        {\"src\": \"WLD\", \"where\": \"WP I 102 ff. (cited by Pokorny at the foot of the ei- entry: 'WP. I 102 ff., WH. I 406 ff., 658 f., 668 f., 723')\", \"stance\": \"supports\", \"note\": \"Walde-Pokorny Bd. I 102 ff. is the source Pokorny abridges for ei- 'gehen'; only the Register (Bd. III) is on disk locally, so the article itself was read through Pokorny's and Mann's citations of it.\"},\n        {\"src\": \"Wiktionary\", \"where\": \"Reconstruction:Proto-Indo-European/h₁ey-\", \"stance\": \"supports\", \"note\": \"'*h₁ey- (imperfective): to go', with *h₁éy-ti ~ *h₁y-énti, *h₁i-tó-s, *h₁éy-tr̥ ~ *h₁i-tn-és etc. — the modern shape of the same root.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Greek\",\n          \"words\": \"ieani; ion 2\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"The Greek verb is ἰέναι (iénai) 'to go', the athematic infinitive of εἶμι (eîmi) < PIE *h₁éy-ti, and ἰόν (ión) is the neuter nominative/accusative singular of its present participle ἰών, ἰοῦσα, ἰόν 'going'. The book prints 'ieani', which is not a Greek word at all: the -na- and -ai are transposed, a misprint for 'ienai'; the extraction reproduces the page faithfully (see the page image). The gloss on the second word, 'going particle', is likewise a slip of the pen for 'going participle' — Klein s.v. ion has 'Gk. ἰόν, neut. of ἰών, “going”, pres. part. of ἰέναι, “to go”'. The claim itself (Greek ienai / ion from the root) is correct and is verbatim AHD.\",\n          \"derivation_fa\": \"فعل یونانی درست ἰέναι (ienai) «رفتن» است، مصدرِ ستاکِ بی‌میانوندِ εἶμι که از *h₁éy-ti هندواروپایی آغازین می‌آید، و ἰόν (ion) صورتِ خنثای اسم فاعل حالِ همان فعل، یعنی «رونده»، است. آنچه در کتاب چاپ شده — «ieani» — واژه‌ای یونانی نیست و قلبِ حروفِ ienai است؛ تصویرِ صفحهٔ چاپی نشان می‌دهد که خطا از خودِ کتاب است نه از خوانشِ اسکن. همچنین «going particle» باید «going participle» (اسم فاعل) می‌بود. اصلِ ادعا — یعنی برگرفتن ienai و ion از این ریشه — درست است و عیناً همان چیزی است که واتکینز در پیوستِ ریشه‌های هندواروپاییِ فرهنگ American Heritage آورده.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"ieani\",\n          \"correct_form\": \"ienai\",\n          \"sources\": [\"https://www.etymonline.com/word/ion\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 (AHD_watkins1985.txt line 428) under ei-¹: '1. … b. Greek ienai, to go: ION; ANION, CATION, DYSPROSIUM.' — the correct spelling ienai, and precisely the arrow Nourai draws.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 leaf 437 (printed pp. 814-815), s.v. ion\", \"stance\": \"supports\", \"note\": \"'ion, n. … — Gk. ἰόν, neut. of ἰών, “going”, pres. part. of ἰέναι, “to go”, fr. I.-E. base *i-, “to go”, whence also L. īre, “to go”, iter (gen. itineris), “a journey”.'\"},\n            {\"src\": \"Etymonline\", \"where\": \"s.v. ion\", \"stance\": \"supports\", \"note\": \"'1834, introduced by English physicist and chemist Michael Faraday (suggested by the Rev. William Whewell …), coined from Greek ion, neuter present participle of ienai “go,” from PIE root *ei- “to go.”'\"},\n            {\"src\": \"POK\", \"where\": \"IEW 293-296 (POK_01.txt line 4246 ff.)\", \"stance\": \"supports\", \"note\": \"the ei- article lists the Greek forms of the root; the participle ἰών/ἰόν is the regular *h₁y-ont- formation to εἶμι.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"An empty pass-through box whose only function is to route the Greek word to Persian. Historically the step is not Greek → French: 'ion' was coined in English in 1834 by Faraday on a suggestion of William Whewell, and French ion is a borrowing of that English scientific coinage a few years later. Nourai's arrow is a shorthand for 'the Greek word, in its modern learned use, reached Persian through French'; the intermediate English coinage is skipped (though it is drawn as a sister box, #4).\",\n          \"derivation_fa\": \"این جعبه تهی است و تنها نقشِ گذرگاه دارد تا واژهٔ یونانی را به فارسی برساند. از دید تاریخی گامِ «یونانی ← فرانسه» دقیق نیست: واژهٔ ion را در سال ۱۸۳۴ فارادی در انگلیسی و به پیشنهادِ ویلیام هیوئل ساخت و فرانسه آن را چند سال بعد از انگلیسی وام گرفت. پس فلشِ نورایی کوتاه‌نوشتِ «واژهٔ یونانی در کاربردِ علمیِ نو، از راهِ فرانسه به فارسی رسید» است و حلقهٔ انگلیسی از قلم افتاده، هرچند در جعبهٔ همسایه (گرهٔ ۴) آمده است.\",\n          \"sources\": [\"https://www.etymonline.com/word/ion\"],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"the chart gives no reference for this node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Etymonline\", \"where\": \"s.v. ion\", \"stance\": \"partial\", \"note\": \"'1834, introduced by English physicist and chemist Michael Faraday (suggested by the Rev. William Whewell, English polymath), coined from Greek ion' — the coinage is English, not French.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 leaf 437 (pp. 814-815), s.v. ion\", \"stance\": \"partial\", \"note\": \"'The word ion was introduced into electricity by the English physicist and chemist Michael Faraday (1791-1867)' — again English, with no French stage mentioned.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"yon «یون»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian یون (yon) 'ion' is a 20th-century scientific loan from French ion [jɔ̃]; Persian renders the French initial [j] with ی and the nasal vowel with ون, giving yon. It belongs to the same layer of French-mediated chemistry vocabulary as یونیزاسیون (yonizāsyon) and یونیده; the Persian Wikipedia article یون is the standard chemistry entry ('یون به اتم یا مولکولی گفته می‌شود که بار الکتریکی خالص دارد'). It is not connected in Persian with the homograph یون / یونان 'Ionia, Greece' (that one goes back to Old Persian Yauna).\",\n          \"derivation_fa\": \"«یون» در فارسیِ نو وام‌واژه‌ای علمی از سدهٔ بیستم است که از فرانسویِ ion گرفته شده؛ همخوانِ آغازینِ فرانسوی [j] با «ی» و واکهٔ خیشومیِ آن با «ون» نوشته می‌شود. این واژه از همان لایهٔ واژگانِ شیمیِ فرانسوی‌تبار است که «یونیزاسیون» و «یونیده» نیز از آن‌اند. باید توجه داشت که این «یون» با «یون / یونان» به معنای سرزمینِ ایونیه هم‌ریشه نیست؛ آن یکی به پارسی باستانِ Yauna بازمی‌گردد. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://fa.wikipedia.org/wiki/%DB%8C%D9%88%D9%86\",\n            \"https://en.wiktionary.org/wiki/%DB%8C%D9%88%D9%86\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"the chart gives no reference for this node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1/MON_part2, searched for a headword 'یون:'\", \"stance\": \"silent\", \"note\": \"Mo'in's lexicon has ژانویه, کامیون, فراکسیون, لژیون etc. but no separate headword یون 'ion' turned up in the OCR — the chemical term is later than the dictionary's core vocabulary.\"},\n            {\"src\": \"Wikipedia (fa)\", \"where\": \"fa.wikipedia.org/wiki/یون\", \"stance\": \"supports\", \"note\": \"the standard Persian chemistry article is headed یون, confirming the form and meaning printed on the chart.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/یون\", \"stance\": \"silent\", \"note\": \"the page carries Urdu/Shina/Ushojo یون 'Greek' (< Sanskrit यवन, ultimately Old Persian 𐎹𐎢𐎴 yauna) but has no Persian section for the chemical term — a homograph, unrelated to this chart.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"ion\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English ion, 1834: Michael Faraday published the term (on the suggestion of William Whewell) for the particles that migrate in electrolysis, taking Greek ἰόν 'going' unchanged, 'so called because ions move toward the electrode of opposite charge'; the sister coinages anion (ἀνιόν 'going up') and cation (κατιόν 'going down') were made at the same moment. Watkins files ION, ANION, CATION under ei-¹.\",\n          \"derivation_fa\": \"«ion» در انگلیسی به سالِ ۱۸۳۴ برمی‌گردد: مایکل فارادی، به پیشنهادِ ویلیام هیوئل، واژهٔ یونانیِ ἰόν «رونده» را بی‌هیچ دگرگونی برای ذره‌هایی به کار برد که در برق‌کافت جابه‌جا می‌شوند، «زیرا یون به سوی الکترودِ با بارِ مخالف می‌رود». هم‌زمان anion (ἀνιόν «بالارونده») و cation (κατιόν «پایین‌رونده») نیز ساخته شد. واتکینز هر سه را ذیلِ ریشهٔ ei-¹ آورده است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/ion\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 line 428, ei-¹ 1b: 'Greek ienai, to go: ION; ANION, CATION, DYSPROSIUM.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 leaf 437 (pp. 814-815), s.v. ion\", \"stance\": \"supports\", \"note\": \"'ion, n., either of the two elements into which a compound is decomposed through electrolysis. — Gk. ἰόν … The word ion was introduced into electricity by the English physicist and chemist Michael Faraday (1791-1867); cp. anion, cation.'\"},\n            {\"src\": \"Etymonline\", \"where\": \"s.v. ion\", \"stance\": \"supports\", \"note\": \"'1834 … coined from Greek ion, neuter present participle of ienai “go,” from PIE root *ei- “to go.” So called because ions move toward the electrode of opposite charge.'\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Indo-European\",\n          \"words\": \"Yě, Yero; Iě, Iěro, Iaro\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Pokorny sets exactly this section inside the ei- article on pp. 296-297: 'ie- in iero- : iōro- : ioro- ,Jahr, Sommer'', with av. yārə n. ,Jahr', gr. ὥρα ,Jahreszeit … ', got. jēr, ags. gēar, ahd. jār. Klein s.v. year derives all of them 'fr. I.-E. *ye-ro, an enlargement of base *ye-, itself an enlargement of base *ey-, “to go”', and Watkins heads his root yēr- 'Year, season' with '[In Pok. 1. ei- 293]'. So Nourai's node reproduces the Pokorny-Klein-Watkins doctrine of 1959-85 accurately, including his double citation form (Yě/Yero beside Iě/Iěro/Iaro, i.e. the same forms written with y- and with i-). Modern scholarship, however, no longer derives the word from 'to go': Wiktionary reconstructs an acrostatic r/n-stem *yóh₁r̥ (oblique *yéh₁n-) 'year, harvest season' and reports only Beekes's tentative link to *(H)yeh₁- 'to send'. Hence 'plausible', not 'confirmed': the forms and the daughter languages are right, the attachment to the 'go' root is the older view.\",\n          \"derivation_fa\": \"پوکورنی همین بخش را در صفحه‌های ۲۹۶ و ۲۹۷ و در درونِ مقالهٔ ei- آورده است: «ie- در iero- : iōro- : ioro- ‹سال، تابستان›» با شواهدِ اوستاییِ yārə «سال»، یونانیِ ὥρα «فصل»، گوتیِ jēr و انگلیسیِ باستانِ gēar. کلاین نیز ذیلِ year همه را از *ye-ro می‌گیرد که گسترشِ *ye- و آن هم گسترشِ *ey- «رفتن» است، و واتکینز ریشهٔ yēr- را با یادداشتِ «در پوکورنی ذیلِ ei- ص ۲۹۳» ثبت کرده. پس گرهِ نورایی آموزهٔ پوکورنی و کلاین و واتکینز را درست بازمی‌تاباند و دو صورتِ نوشتاری (با y و با i) نیز همان است. اما ریشه‌شناسیِ امروزی این واژه را دیگر از «رفتن» نمی‌گیرد: ویکی‌واژه ستاکِ r/n ای *yóh₁r̥ (حالتِ غیرفاعلی *yéh₁n-) «سال، فصلِ خرمن» را بازسازی می‌کند و تنها پیوندِ احتمالیِ بیکس با *(H)yeh₁- «فرستادن» را می‌آورد. از این رو حکم «با احتیاط پذیرفتنی است».\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yeh%E2%82%81r-\",\n            \"https://www.etymonline.com/word/year\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:296\", \"status\": \"supports\", \"note\": \"POK_01.txt lines 4297-4305, with the standalone page mark '297' after the Greek line, i.e. the section begins on p. 296: 'ie- in iero- : iōro- : ioro- ,Jahr, Sommer': ai. paryāriṇī- ,nach einem Jahr erst kalbend'; av. yārə n. ,Jahr'; gr. ὥρα ,Jahreszeit, Tageszeit, Stunde, rechte Zeit', ὧρος ,Zeit, Jahr'; … got. jēr, anord. ār, ags. gēar, as. ahd. jār n. ,Jahr'.'\"},\n            {\"ref\": \"KLN:1761\", \"status\": \"supports\", \"note\": \"Klein s.v. year (read in KLN_1971.txt line 269593; the paginated 1966 scan on disk breaks off at c. p. 1697, so the page number 1761 itself could not be seen): 'and cogn. with Avestic yāri, “year”, Gk. ὧρος, “year”, ὥρα … All these words possibly mean lit. “that which goes or passes”, and derive fr. I.-E. *ye-ro, an enlargement of base *ye-, itself an enlargement of base *ey-, “to go”.' — exactly Nourai's arrow.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985, y-list (AHD_watkins1985.txt line 1192)\", \"stance\": \"supports\", \"note\": \"'yēr-. Year, season. 1. Suffixed basic form *yēr-o- in Germanic *jēram in Old English gēar, year: YEAR. 2. Suffixed o-grade form *yōr-ā- in Greek hōrā, season: HOUR; HOROLOGE, HOROLOGY, HOROSCOPE. [In Pok. 1. ei- 293.]'\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 14.72 HOUR (SYN.txt line 24349)\", \"stance\": \"supports\", \"note\": \"'Grk. ὥρα ‘period of time’ … : Av. yāra, Goth. jer, etc. ‘year’ (14.73), Slavic jaro ‘spring’ (14.75), all prob. fr. *yē-, yō- beside *yā- (cf. Skt. yā- ‘go’, Lith. joti ‘ride’, etc.), extensions of ei-, i- ‘go’. Walde-P. 1.105.' — Buck states Nourai's arrow explicitly.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann, s.v. ior- (1) (IEC.txt line 6489)\", \"stance\": \"supports\", \"note\": \"'ior- (1) “time, period”. Cf. WP I, 3 & 105, and iēr-. Av. yārə “year”; OPer. -yara “year, season”; Gk. hóros … LW in Lat. hora & Alb. herë “time” … R jarovój “summer”; jàrka “yearling ewe”.'\"},\n            {\"src\": \"Wiktionary\", \"where\": \"Reconstruction:Proto-Indo-European/yóh₁r̥\", \"stance\": \"partial\", \"note\": \"'*yóh₁r̥ n (oblique stem *yéh₁n-): year; growing season or harvest season' with 'Beekes mentions a possible derivation from *(H)yeh₁- (“to send”)' — the modern reconstruction does NOT hang the word on *h₁ey- 'to go'.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Avestan\",\n          \"words\": \"yâr, yâra; yâh 2, jâr, jaiti\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Avestan yār- n. 'year' (nom.-acc. yārə, also yā̊, yā) is genuine and is the direct Iranian reflex of the word in node #5: Bartholomae, Altiranisches Wörterbuch, s.v. 'yār- n. ‘Jahr’' (running head 'isə; yār- — yās-', col. 1188), whence compounds like naēma-yār- 'half a year', yārə.drājah- 'the length of a year', huyāirya- 'good year' and dužyāirya- 'bad year'. 'jâr' is simply yār written in the older j- transliteration of Avestan y- (Justi's and Spiegel's convention, which Nourai's sources sometimes keep). The other two words are wrongly glossed: Avestan yāh- n. is not 'year' but 'crisis, decision' (Pokorny p. 296 'av. yāh- n. ,Krise, Entscheidung' (s-St.)'), and yāiti is the 3sg. of yā- 'goes, travels' (Pokorny, ibid., 'ai. yāti ,geht, fährt', av. yāiti ds.'). Both belong to the parent root *yeh₂- 'to go' one level up, not to the 'year' box. Hence the node is right for yār/yāra/jār and mis-glossed for yāh 2 and jaiti.\",\n          \"derivation_fa\": \"صورتِ اوستاییِ yār- «سال» (yārə، و نیز yā̊ و yā) اصیل است و بازتابِ مستقیمِ همان واژهٔ گرهِ پیشین در ایرانی است؛ بارتولومه در فرهنگِ ایرانیِ باستان ذیلِ «yār- n. ‹Jahr›» (ستونِ ۱۱۸۸) آن را با ترکیب‌هایی چون naēma-yār- «نیم‌سال»، yārə.drājah- «درازای یک سال»، huyāirya- «سالِ خوب» و dužyāirya- «سالِ بد» آورده است. «jâr» چیزی جز همان yār نیست، نوشته‌شده به شیوهٔ کهنِ آوانویسیِ اوستایی که y را j می‌نوشت. اما دو واژهٔ دیگر معنایشان نادرست است: yāh- اوستایی «سال» نیست بلکه «بحران، تصمیم» است (پوکورنی، ص ۲۹۶) و jaiti/yāiti صیغهٔ سومِ شخصِ فعلِ yā- «می‌رود» است (همان‌جا). این دو به ریشهٔ مادر، یعنی *yeh₂- «رفتن»، تعلق دارند نه به جعبهٔ «سال». پس گره برای yār/yāra/jār درست است و برای yāh 2 و jaiti خطای معنایی دارد.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yeh%E2%82%81r-\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:296\", \"status\": \"partial\", \"note\": \"POK_01.txt line 4299 gives 'av. yārə n. ,Jahr'' under 'ie- in iero- …' — supports yār/yāra. But the same page, a few lines above (line 4293 f.), files the other two forms under the iā- 'go' section with different meanings: 'ai. yāti ,geht, fährt', av. yāiti ds., … av. yāh- n. ,Krise, Entscheidung' (s-St.)'. So Pokorny contradicts the gloss 'year' for yâh 2 and jaiti.\"},\n            {\"ref\": \"KLN:1796\", \"status\": \"not_found\", \"note\": \"Klein's two-volume dictionary ends at p. 1776, so a page 1796 does not exist (and the local 1966 scan breaks off around p. 1697 in any case). The Avestan material Nourai wants is in Klein at p. 1761, s.v. year: 'cogn. with Avestic yāri, “year”' — most likely a typo for 1761 or for the 1971 one-volume pagination.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch, s.v. yār- (running head 'isə; yār- — yās- mit a 1188')\", \"stance\": \"supports\", \"note\": \"'j. (, p.) yār- n. ,Jahr': taθa ayarə maiθiiaiti yaθa yārə “sie halten für eben den Tag, was ein Jahr (ist)” V. 2.41'; also 'naēmam yārə “ein halbes Jahr (lang)” N. 45' and 'sata-yār- n. ,Zeitraum von hundert Jahren''.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"Reconstruction:Proto-Indo-European/yóh₁r̥, Descendants\", \"stance\": \"supports\", \"note\": \"'Proto-Iranian … Younger Avestan: 𐬫𐬁𐬭𐬆 (yārə) ~ 𐬫𐬃 (yā̊), 𐬫𐬁 (yā)', with the compounds dužiiāiriia- 'bad year, drought' and huiiāiriia- 'good year'.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 14.73 YEAR (SYN.txt line 25709)\", \"stance\": \"supports\", \"note\": \"the language table for 'year' lists 'Av. yār-, sarəd-' beside Goth. jēr, OE gēar, OPers. θard-.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"yâirka\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The form comes from Horn, Grundriss der neupersischen Etymologie, no. 1116 on p. 249 — but Horn labels it Old Persian, not Pahlavi, and marks it as a reconstruction: 'hīrek, (herek?) ‘Böckchen, Zickchen’. ap. *yāirka- ‘Jährling’ (Tomaschek, Centralasiat. Studien II, 766)', adding the caveat 'Wenn die Etymologie richtig ist, so hätten wir in diesem Worte die einzige neupersische Spur des aw. yār-, ap. -yāra-.' So (a) the language label on the chart is wrong — this is an unattested Old Iranian *yāirka-, an -ka- diminutive of *yāra- 'year' meaning 'yearling', invented by Tomaschek, not a recorded Middle Persian word (MacKenzie's Concise Pahlavi Dictionary has nothing of the kind); (b) the gloss 'one year old' is Horn's 'Jährling'; and (c) the etymology is rejected outright by Hübschmann, Persische Studien p. 106, ad Horn 1116: 'Ich halte die Etymologie für falsch.' Mo'in repeats both sides in his footnote at Borhan-e Qate' p. 2406.\",\n          \"derivation_fa\": \"این صورت از هرن، «طرحِ ریشه‌شناسیِ فارسیِ نو»، شمارهٔ ۱۱۱۶ در صفحهٔ ۲۴۹ گرفته شده؛ اما هرن آن را پارسی باستان می‌خواند نه پهلوی، و با ستاره یعنی بازسازی‌شده می‌نویسد: «hīrek (herek؟) ‹بزغاله، بچه‌بز›؛ پارسی باستانِ *yāirka- ‹یک‌ساله› (به نقل از توماشک)»، و خود می‌افزاید «اگر این ریشه‌شناسی درست باشد، تنها ردِّ اوستاییِ yār- در فارسیِ نو همین واژه است». پس نخست برچسبِ زبان در نمودار نادرست است — این *yāirka- صورتی ناموجود و بازسازیِ ایرانیِ باستان است، پسوندِ تصغیرِ -ka- بر *yāra- «سال» به معنای «یک‌ساله»، نه واژه‌ای ضبط‌شده در فارسیِ میانه (در فرهنگِ پهلویِ مکنزی چنین واژه‌ای نیست). دوم آنکه هوبشمان در «پژوهش‌های پارسی» صفحهٔ ۱۰۶ دربارهٔ همین شمارهٔ ۱۱۱۶ می‌نویسد: «این ریشه‌شناسی را نادرست می‌دانم». معین نیز در حاشیهٔ برهان قاطع ص ۲۴۰۶ هر دو رأی را آورده است. پس پژوهشِ امروزی این حلقه را رد می‌کند.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"HRN:249\", \"status\": \"partial\", \"note\": \"HRN.txt leaf 270 (page mark '- 249 -'), no. 1116: 'hīrek, (herek?) ‘Böckchen, Zickchen’. ap. *yāirka- ‘Jährling’ (Tomaschek, Centralasiat. Studien II, 766). … Wenn die Etymologie richtig ist, so hätten wir in diesem Worte die einzige neupersische Spur des aw. yār-, ap. -yāra-.' The page has the form and the derivation, but as Old Persian, reconstructed, and hedged — not as a Pahlavi word.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien, p. 106 (HUB.txt line 3755, notes on Horn's numbers)\", \"stance\": \"contradicts\", \"note\": \"'1116. Ich halte die Etymologie für falsch.' — Hübschmann rejects precisely this derivation of hīrek from the 'year' word.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary, searched for yʾyrk / yairk / hyrk\", \"stance\": \"silent\", \"note\": \"no such Middle Persian word is recorded; MacKenzie's only relevant entries are sāl 'year' and sar 'head, end' — i.e. there is no attested Pahlavi *yāirka to which the chart's box could refer.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' p. 2406, Mo'in's footnote 1\", \"stance\": \"partial\", \"note\": \"«هرن این کلمه را از پارسی باستان *yāirka (بزغاله)، از اوستایی yāra-، پارسی باستانی *yāra- (سال) می‌پندارد … و هوبشمان این وجه اشتقاق را درست نمی‌داند» — Mo'in reports Horn's derivation and Hübschmann's rejection of it side by side.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Persian\",\n          \"words\": \"hîrak «هیرک»\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The Persian word is real and the gloss is right: Borhan-e Qate' p. 2406 has «هیرک (بر وزن زِبِر) بچهٔ بز را گویند که بزغاله باشد؛ و بعضی گفته‌اند که همچنانکه بچهٔ گوسفند را بره میخوانند بچهٔ شتر را هیرک میگویند» — 'a kid; some say the young of a camel', which is Nourai's 'a baby animal', and Horn glosses it 'Böckchen, Zickchen'. What is disputed is the derivation drawn here. Tomaschek's and Horn's account (NP hīrak < Old Iranian *yāirka- 'yearling', a -ka- diminutive of *yāra- 'year', with the regular Persian change of initial y- to h-) is attractive because the semantic type is well attested in the same root — compare Russian jarka 'yearling ewe' from the same *ior- (Mann, IEC s.v. ior-) — but Hübschmann declared it false (Persische Studien p. 106, ad Horn 1116) and Mo'in's own footnote on the very page Nourai cites records that rejection. No modern Iranian etymological dictionary revives it, so the chain 'year' → hīrak must be marked disputed.\",\n          \"derivation_fa\": \"خودِ واژه و معنایش درست است: برهان قاطع در صفحهٔ ۲۴۰۶ می‌آورد «هیرک، بر وزن زِبِر، بچهٔ بز را گویند که بزغاله باشد؛ و بعضی گفته‌اند که همچنانکه بچهٔ گوسفند را بره می‌خوانند بچهٔ شتر را هیرک می‌گویند»، و هرن نیز آن را «بزغاله» معنی می‌کند. آنچه محلِّ اختلاف است، خودِ اشتقاق است. تحلیلِ توماشک و هرن — یعنی هیرک از ایرانیِ باستانِ *yāirka- «یک‌ساله»، پسوندِ تصغیرِ -ka- بر *yāra- «سال»، با ابدالِ منظمِ y آغازین به h در فارسی — از نظرِ معنایی وسوسه‌انگیز است، چرا که در همین ریشه نمونهٔ روسیِ jarka «میشِ یک‌ساله» را داریم (مان، ذیلِ ior-). با این همه هوبشمان آن را نادرست خوانده و خودِ معین در حاشیهٔ همان صفحه‌ای که نورایی به آن ارجاع می‌دهد این رد را ثبت کرده است. هیچ فرهنگِ ریشه‌شناختیِ نوینِ ایرانی این وجه را زنده نکرده، پس این حلقه ردشده است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"BQT:2406\", \"status\": \"partial\", \"note\": \"Borhan-e Qate' (Mo'in's ed.) p. 2406, fetched with tools/ref_page.py BQT:2406 --image (vol. 4, pdf p. 489; cached at data/verification/sources/refs/ocr/BQT/2406.png): headword «هیرک … بچهٔ بز را گویند که بزغاله باشد» supports the word and the meaning, and footnote 1 gives Horn's *yāirka etymology — but immediately adds «و هوبشمان این وجه اشتقاق را درست نمی‌داند».\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"Grundriss no. 1116, p. 249\", \"stance\": \"partial\", \"note\": \"'hīrek, (herek?) ‘Böckchen, Zickchen’ … syn. yirk ‘ausgewachsenes, männliches Schaaf, Zuchtwidder’. Wenn die Etymologie richtig ist …' — Horn himself only offers the derivation conditionally.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien p. 106 (HUB.txt line 3755)\", \"stance\": \"contradicts\", \"note\": \"'1116. Ich halte die Etymologie für falsch.'\"},\n            {\"src\": \"IEC\", \"where\": \"Mann, s.v. ior- (1) (IEC.txt line 6489)\", \"stance\": \"partial\", \"note\": \"'R jarovój “summer”; jàrka “yearling ewe”' — the semantic type ('year' → name of a yearling animal) does exist in this root, which is why the guess was made; but Mann lists no Persian reflex.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Latin\",\n          \"words\": \"yâ-mo\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"The intended form is the suffixed PIE stem *yā-no- (Watkins: 'Extended form *yā- (< *yaə-) in suffixed forms *yā-no-, yā-nu- in: a. Latin Jānus, archway, and Jānus, god of doors and of the beginning of a year: JANITOR, JANUARY, JANUS'), which yields Latin iānus 'arched passageway', iānua 'door' and the god Iānus. The page prints 'yâ-mo' with an m — an impossible formation, and the book's own misprint for 'yâ-no'; the extraction is faithful (see the page image). The gloss 'beginning of year, god of doors' is a straight translation of Pokorny p. 296, 'lat. Jānus ,altital. Gott der Türen und des Jahresanfangs', jānua ,Türe''. Note also that the box is attached to the YEAR node (#5), whereas both Pokorny and Watkins put the Jānus word under the 'go' root itself, in the iā- section — Nourai's placement follows the physical adjacency of the two sections on Pokorny p. 296, not their logic.\",\n          \"derivation_fa\": \"صورتی که در نظر بوده *yā-no- است، همان ستاکِ پسونددارِ هندواروپایی که واتکینز می‌نویسد: «صورتِ گسترده‌ی *yā- در ستاک‌های پسونددارِ *yā-no- و *yā-nu-: لاتینِ iānus ‹گذرگاهِ طاق‌دار› و Iānus ‹خدای درها و آغازِ سال›». اما در صفحه «yâ-mo» با میم چاپ شده که ساختی ناممکن است و خطای چاپیِ خودِ کتاب است، نه خطای خوانشِ اسکن (تصویرِ صفحه گواه است). معنایی هم که داده شده («آغازِ سال، خدای درها») برگردانِ دقیقِ عبارتِ پوکورنی در ص ۲۹۶ است. نکتهٔ دیگر آنکه این جعبه زیرِ گرهِ «سال» کشیده شده، حال آنکه پوکورنی و واتکینز هر دو واژهٔ Jānus را زیرِ خودِ ریشهٔ «رفتن» و در بخشِ iā- می‌آورند؛ گویا نورایی از همجواریِ دو بخش در صفحهٔ ۲۹۶ پوکورنی به اشتباه افتاده است.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"yâ-mo\",\n          \"correct_form\": \"yâ-no (PIE *yā-no-, whence Latin Iānus / iānua)\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/January\",\n            \"https://www.etymonline.com/word/janitor\",\n            \"https://en.wiktionary.org/wiki/%DA%98%D8%A7%D9%86%D9%88%DB%8C%D9%87\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins 1985 line 428, ei-¹ item 4: 'Extended form *yā- (< *yaə-) in suffixed forms *yā-no-, yā-nu- in: a. Latin Jānus, archway, and Jānus, god of doors and of the beginning of a year: JANITOR, JANUARY, JANUS'. The etymology is exactly Nourai's, but the form is *yā-no- (not yâ-mo) and it hangs on ei-¹ directly, not on yēr-.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 296 (POK_01.txt, iā- section of 1. ei-)\", \"stance\": \"supports\", \"note\": \"'lat. Jānus ,altital. Gott der Türen und des Jahresanfangs', jānua ,Türe'' — verbatim the gloss printed on the chart, and it stands in the iā- 'gehen' section, not in the iēro- 'Jahr' section.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 leaf 445 (p. 825), s.vv. janitor, Janus\", \"stance\": \"partial\", \"note\": \"'Janus … L. Jānus, personification of jānus, “arched passage, arcade”, whence jānua, “door”' and, s.v. janitor, jānus 'is of uncertain origin. It is perh. cogn. with OI. yānaḥ ‘path’ … yāti, Avestic yāiti ‘goes, travels’' — the same connection, but hedged.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"ژانویه, etymology tree\", \"stance\": \"supports\", \"note\": \"'Proto-Indo-European *yeh₂- → *yeh₂-no- → Proto-Italic *jānos → Latin iānus → Latin Iānus' — the modern notation of the very form the book misprints.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"French\",\n          \"words\": \"Janiver\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Latin Iānuārius (mensis) 'the month of Janus' (Iānus + the adjectival suffix -ārius) gave Old North French Genever and Old French Jenvier, modern French janvier; Anglo-French had Ieneuer already in the early 12th century, and the Middle English reflex is Janever/Janiver (Gower, late 14c.: 'The frosti colde Janever, Whan comen is the newe yeer'). The form printed here, 'Janiver', is therefore a real medieval Anglo-French/Middle English spelling rather than the standard Old French citation form jenvier/janvier — accurate enough as a stage, but not the form from which either English January (Latinized c. 1400) or Persian ژانویه was actually taken.\",\n          \"derivation_fa\": \"لاتینِ Iānuārius (mensis) «ماهِ ژانوس»، ساخته از Iānus و پسوندِ صفتیِ -ārius، در فرانسویِ شمالیِ کهن Genever و در فرانسویِ کهن Jenvier و در فرانسویِ امروز janvier شده است؛ در فرانسویِ انگلونرمن از آغازِ سدهٔ دوازدهم Ieneuer دیده می‌شود و صورتِ انگلیسیِ میانه Janever/Janiver است (گاور، اواخرِ سدهٔ چهاردهم: «The frosti colde Janever»). پس «Janiver» که در کتاب آمده املایی واقعی از سده‌های میانه است، ولی صورتِ معیارِ فرانسویِ کهن jenvier/janvier است و نه این؛ افزون بر آن، نه انگلیسیِ January (که حدودِ ۱۴۰۰ به شکلِ لاتینی بازگشت) و نه «ژانویه»ی فارسی از این صورت گرفته نشده‌اند. با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://www.etymonline.com/word/January\"],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"the chart gives no reference for this node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Etymonline\", \"where\": \"s.v. January\", \"stance\": \"partial\", \"note\": \"'late 13c., Ieneuer (early 12c. in Anglo-French), from Old North French Genever, Old French Jenvier (Modern French Janvier), from Latin Ianuarius (mensis) “(the month) of Janus” … The form was gradually Latinized by c. 1400.' Gower's 'The frosti colde Janever' is quoted there — the nearest attested form to the book's 'Janiver'.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 leaf 445 (p. 825), s.v. January\", \"stance\": \"partial\", \"note\": \"'January, n. — L. Januarius (mensis), “the month dedicated to Janus”. See Janus and -ary.' Klein takes English January straight from Latin and records no French intermediate form.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"ژانویه, etymology tree\", \"stance\": \"partial\", \"note\": \"'Latin Iānuārius → Old French janvier → French janvier' — the standard chain names janvier, not Janiver.\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"Persian\",\n          \"words\": \"Žânvîyeh «ژانویه»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian ژانویه (žānviye) is a 20th-century borrowing of Modern French janvier [ʒɑ̃vje], taken in with the rest of the Gregorian month names (فوریه, مارس, آوریل, مه, ژوئن …): French [ʒ] is written ژ, the nasal ā is rendered ān, and the French final -ier [je] appears as -یه, the same substitution seen in فوریه (février) and ژوئیه (juillet). Mo'in's Farhang-e Farsi has «ژانویه … ماه اول سال فرنگی، مطابق با اواخر دی و اوایل بهمن». Dari uses جنوری (from English) and Tajik январ (from Russian) instead, which shows the French route is specific to Iranian Persian.\",\n          \"derivation_fa\": \"«ژانویه» وام‌واژه‌ای از فرانسویِ janvier است که در سدهٔ بیستم همراه با دیگر نام‌های ماه‌های میلادی (فوریه، مارس، آوریل، مه، ژوئن…) وارد فارسی شد: همخوانِ [ʒ] فرانسوی با «ژ»، واکهٔ خیشومی با «ان» و پایانهٔ -ier [je] با «-یه» نوشته می‌شود، درست همان‌گونه که در «فوریه» و «ژوئیه» می‌بینیم. معین در فرهنگِ فارسی می‌نویسد «ژانویه … ماه اول سال فرنگی، مطابق با اواخر دی و اوایل بهمن». آنکه در فارسیِ افغانستان «جنوری» (از انگلیسی) و در تاجیکی «январ» (از روسی) به کار می‌رود نشان می‌دهد که راهِ فرانسوی ویژهٔ فارسیِ ایران است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%DA%98%D8%A7%D9%86%D9%88%DB%8C%D9%87\"],\n          \"ref_check\": [\n            {\"ref\": \"MON:1775\", \"status\": \"partial\", \"note\": \"the entry is there — MON_part1.txt line 73066: «ژانویه: [فر.] (اِ.) ماه اول سال فرنگی مطابق با اواخر دی و اوایل بهمن» (the OCR renders the bracketed French tag as '26 (.)'), and MON_part2.txt line 43374 lists it at the head of the month names «ژانویه؛ فوریه؛ مارس، آوریل، مه، ژوئن». The local Mo'in OCR carries no page numbers, so the page 1775 itself could not be confirmed.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Farhang-e Farsi, s.v. ژانویه (MON_part1.txt line 73066)\", \"stance\": \"supports\", \"note\": \"«ژانویه: … ماه اول سال فرنگی مطابق با اواخر دی و اوایل بهمن» with a French origin tag — the word, the meaning and the French source as the chart has them.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/ژانویه, Persian section\", \"stance\": \"supports\", \"note\": \"'Borrowed from French janvier.' … 'ژانویه • (žânviye) (Iran) January', with the sister forms 'Dari جنوری, Tajik январ' — confirming both the loan and Nourai's transliteration Žânvîyeh.\"}\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"English\",\n          \"words\": \"January, janitor\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English January: Middle English Ieneuer (late 13c.), from Anglo-French/Old North French Genever, Old French Jenvier, from Latin Iānuārius; the spelling was re-Latinized to January by c. 1400, displacing Old English geola se æfterra 'Later Yule'. English janitor is a direct 16th-century Latinism: 1580s 'an usher in a school', then 'doorkeeper' (1620s), from Latin iānitor 'doorkeeper, porter', from iānua 'door' from iānus 'arched passageway'; the modern sense 'caretaker of a building' is recorded from 1708. Watkins files both under ei-¹.\",\n          \"derivation_fa\": \"«January» در انگلیسی از انگلیسیِ میانهٔ Ieneuer (اواخرِ سدهٔ سیزدهم) می‌آید که از فرانسویِ انگلونرمن Genever و فرانسویِ کهن Jenvier و در نهایت از لاتینِ Iānuārius گرفته شده؛ املای آن حدودِ سالِ ۱۴۰۰ دوباره لاتینی‌وار شد و جای واژهٔ انگلیسیِ باستانِ geola se æfterra («یولِ پسین») را گرفت. «janitor» وام‌واژه‌ای مستقیم از لاتین در سدهٔ شانزدهم است: نخست (دههٔ ۱۵۸۰) به معنای دربانِ مدرسه، سپس «دربان» (دههٔ ۱۶۲۰)، از لاتینِ iānitor «دربان» از iānua «در» از iānus «گذرگاهِ طاق‌دار»؛ معنای امروزیِ «سرایدار» از ۱۷۰۸ ثبت شده است. واتکینز هر دو را ذیلِ ei-¹ آورده. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/January\",\n            \"https://www.etymonline.com/word/janitor\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"the chart gives no reference for this node; the parent box's AHD reference covers it — Watkins lists 'JANITOR ei-1  JANUARY ei-1  Janus ei-1' in his English index (AHD_watkins1985.txt line 1698).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Etymonline\", \"where\": \"s.vv. January, janitor\", \"stance\": \"supports\", \"note\": \"'janitor (n.) 1580s, “an usher in a school,” later “doorkeeper” (1620s), from Latin ianitor “doorkeeper, porter,” from ianua “door, entrance, gate,” from ianus “arched passageway, arcade”'; and for January the Anglo-French/Old French chain quoted above.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 leaf 445 (p. 825), s.vv. janitor, January, Janus\", \"stance\": \"supports\", \"note\": \"'janitor, n., doorkeeper, porter. — L., formed with suff. -tor fr. jānus, “a covered passage, arcade”'; 'January, n. — L. Januarius (mensis), “the month dedicated to Janus”'.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985, English index (line 1698)\", \"stance\": \"supports\", \"note\": \"'JANITOR ei-1 JANUARY ei-1 Janus ei-1'.\"}\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"Germanic\",\n          \"words\": \"yěram, jěram\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *jēra- (neuter *jēran/*jēram) 'year', the regular suffixed o-stem *yēr-o- of the word in node #5; Nourai's double spelling yěram / jěram is again the same form written with y- and with j-. Its descendants are Gothic jēr, Old Norse ár, Old English gēar (West Saxon) / gēr (Anglian), Old Saxon and Old High German jār, Dutch jaar, German Jahr. Kroonen's Etymological Dictionary of Proto-Germanic reconstructs *jēra- and derives it from the PIE r/n-stem.\",\n          \"derivation_fa\": \"ژرمنیِ آغازین *jēra- (خنثی *jēran) «سال»، همان ستاکِ پسونددارِ *yēr-o- ی گرهِ ۵ است؛ دو املایی که نورایی می‌آورد (yěram و jěram) باز هم یک صورت‌اند که یک بار با y و یک بار با j نوشته شده. بازماندگانِ آن گوتیِ jēr، نروژیِ باستانِ ár، انگلیسیِ باستانِ gēar (وسکسی) و gēr (انگلی)، ساکسونیِ باستان و آلمانیِ علیای باستانِ jār، هلندیِ jaar و آلمانیِ Jahr است. کرونن در فرهنگِ ریشه‌شناختیِ ژرمنیِ آغازین همین *jēra- را بازسازی می‌کند و آن را از ستاکِ r/n هندواروپایی می‌گیرد. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/year\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yeh%E2%82%81r-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 line 1192: 'yēr-. Year, season. 1. Suffixed basic form *yēr-o- in Germanic *jēram in Old English gēar, year: YEAR.' — the chart's form jěram is Watkins's *jēram.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. year (KLN_1971.txt line 269593; = KLN:1761 of the two-volume ed.)\", \"stance\": \"supports\", \"note\": \"'ME. yere, fr. OE. gēar, rel. to OS., OHG., MHG. jār, ON. ár, Dan. aar, Swed. år, OFris. gēr, Du. jaar, G. Jahr, Goth. jēr, “year”'.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"Reconstruction:Proto-Indo-European/yóh₁r̥, Descendants\", \"stance\": \"supports\", \"note\": \"'Proto-Germanic: *jērą [Kroonen, Etymological Dictionary of Proto-Germanic, p. 273]'.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 14.73 YEAR (SYN.txt line 25709)\", \"stance\": \"supports\", \"note\": \"the table lists Goth. jēr, ON ár, OE gēar, ME yeer, NE year, Du. jaar, OHG/MHG jār, NHG Jahr for 'year'.\"}\n          ]\n        },\n        {\n          \"id\": 14,\n          \"lang\": \"English\",\n          \"words\": \"year\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old English gēar (West Saxon), gēr (Anglian) 'year' < Proto-Germanic *jēra-; the OE initial g- before a front vowel was the palatal [j], which Middle English wrote y- (yer, yeer), whence modern year. The sense 'a full round of seasons, the interval between equinoxes' is the inherited one; 'years' for 'period of life' appears by the early 13th century.\",\n          \"derivation_fa\": \"انگلیسیِ باستانِ gēar (وسکسی) و gēr (انگلی) «سال» از ژرمنیِ آغازینِ *jēra- می‌آید؛ g آغازینِ انگلیسیِ باستان پیش از واکهٔ پیشین آوای کامیِ [j] داشت و در انگلیسیِ میانه y نوشته شد (yer، yeer)، و از همان‌جا year امروزی پدید آمد. معنای «دورهٔ کاملِ فصل‌ها، فاصلهٔ میانِ دو اعتدال» همان معنای موروثی است و کاربردِ «سال‌ها» به معنای «دورانِ زندگی» از آغازِ سدهٔ سیزدهم دیده می‌شود. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/year\"],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"the chart gives no reference for this node; the parent box's AHD reference covers it ('Germanic *jēram in Old English gēar, year: YEAR').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Etymonline\", \"where\": \"s.v. year\", \"stance\": \"supports\", \"note\": \"'Middle English yer, from Old English gear (West Saxon), ger (Anglian) “year,” from Proto-Germanic *jēr “year,” reconstructed to be from PIE root *yer- “year, season”'; and s.v. G: 'Before the vowels -e-, -i-, and -y-, Old English initial g- changed its sound and is represented in Modern English by consonantal y- (year, yard, yellow …)'.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. year\", \"stance\": \"supports\", \"note\": \"'year, n. — ME. yere, fr. OE. gēar' — the same chain.\"}\n          ]\n        },\n        {\n          \"id\": 15,\n          \"lang\": \"Greek\",\n          \"words\": \"hôros; hôrâ\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Greek ὥρᾱ (hṓrā, Ionic ὥρη) 'season, time of year, time of day, hour' continues the o-grade *yōr-ā of the 'year' word: PIE initial *y- regularly becomes rough breathing h- in Greek (as in ὗς, ὥρα), and *ō gives Greek ω. Beside it stands ὧρος (hôros) 'time, year', the bare r-stem, glossed by Hesychius and used in ἐπ-ώρ- compounds. Pokorny p. 296-97 lists both: 'gr. ὥρα ,Jahreszeit, Tageszeit, Stunde, rechte Zeit', ὧρος ,Zeit, Jahr''. Nourai's glosses ('time' for hôros, 'season' for hôrâ) match.\",\n          \"derivation_fa\": \"یونانیِ ὥρᾱ (hōrā، در گویشِ ایونی ὥρη) به معنای «فصل، هنگامِ سال، هنگامِ روز، ساعت» دنبالهٔ صورتِ o-دارِ *yōr-ā ی همان واژهٔ «سال» است: *y آغازینِ هندواروپایی در یونانی به‌طورِ منظم به دمِ درشت (h-) بدل می‌شود و *ō به ω. در کنارِ آن ὧρος (hōros) «زمان، سال» است، همان ستاکِ ساده با r که هزوخیوس آن را ضبط کرده. پوکورنی در ص ۲۹۶–۲۹۷ هر دو را می‌آورد: «یونانیِ ὥρα ‹فصل، هنگامِ روز، ساعت، هنگامِ درست›، ὧρος ‹زمان، سال›». معنایی که نورایی برای هر دو داده با همین می‌خواند. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/hour\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 line 1192: 'yēr-. Year, season. … 2. Suffixed o-grade form *yōr-ā- in Greek hōrā, season: HOUR; HOROLOGE, HOROLOGY, HOROSCOPE.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 296-297 (POK_01.txt line 4300)\", \"stance\": \"supports\", \"note\": \"'gr. ὥρα ,Jahreszeit, Tageszeit, Stunde, rechte Zeit', ὧρος ,Zeit, Jahr'' — both words, both glosses, in the 'Jahr, Sommer' section.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 14.72 HOUR (SYN.txt line 24349)\", \"stance\": \"supports\", \"note\": \"'Grk. ὥρα “period of time”, in Hom. esp. “time of year, season” or “fitting time”, later esp. “time of day, hour” … : Av. yāra, Goth. jer, etc. “year”'.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann, s.v. ior- (1) (IEC.txt line 6489)\", \"stance\": \"supports\", \"note\": \"'Gk. hóros, hōr-, id.; LW in Lat. hora & Alb. herë “time, fois”'.\"}\n          ]\n        },\n        {\n          \"id\": 16,\n          \"lang\": \"English\",\n          \"words\": \"hour, horoscope\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"hour: c. 1200, from Old French ore/hore 'canonical hour', from Latin hōra (a borrowing of Greek ὥρα), first in the ecclesiastical sense 'one of the seven canonical hours', then from the late 14th century 'one of the 24 (or 12) parts of the day'; the silent h- was restored in spelling on the Latin model. horoscope: Greek ὡροσκόπος 'hour-watcher, the one who observes the rising sign at the hour of birth' = ὥρα + σκοπός (root *spek- 'to observe'), Latin hōroscopus, Old French horoscope, English from the 16th century. Watkins files HOUR, HOROLOGE, HOROLOGY and HOROSCOPE under yēr- (and HOROSCOPE also under spek-, for its second element).\",\n          \"derivation_fa\": \"«hour» از حدودِ سالِ ۱۲۰۰ در انگلیسی است، از فرانسویِ کهنِ ore/hore «ساعتِ عبادت»، از لاتینِ hōra که خود وامی از یونانیِ ὥρα است؛ نخست در معنای کلیسایی «یکی از هفت ساعتِ نمازِ روزانه» و از اواخرِ سدهٔ چهاردهم در معنای «یک بیست‌وچهارمِ شبانه‌روز». حرفِ h که تلفظ نمی‌شود بعدها به پیرویِ املای لاتینی بازنویسی شد. «horoscope» از یونانیِ ὡροσκόπος «نگرندهٔ ساعت» است، مرکب از ὥρα و σκοπός (از ریشهٔ *spek- «نگریستن»)، سپس لاتینِ hōroscopus و فرانسویِ کهنِ horoscope. واتکینز هر دو را ذیلِ yēr- آورده است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/hour\"],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"the chart gives no reference for this node; the parent box's AHD reference covers it — Watkins's English index has 'HOROLOGE yér- HOROLOGY yér- HOROSCOPE spek-, yér-' and 'HOUR yér-' (AHD_watkins1985.txt lines 1648, 1651).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Etymonline\", \"where\": \"s.v. hour\", \"stance\": \"supports\", \"note\": \"'c. 1200 … from Old French ore, hore “canonical hour; one-twelfth of a day”, from Latin hora “an hour”; poetically “time of year, season”, from Greek hōra … (from PIE *yor-a-, from root *yer- “year, season”; see year). … The h- has persisted in this word despite not being pronounced since Roman times.'\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. hour (KLN_1971.txt line 116225)\", \"stance\": \"supports\", \"note\": \"'hour, n. — ME., fr. OF. ure, ore, hore (F. heure), fr. L. hora, “hour”, fr. Gk. ὥρα … See year and cp. words there referred to. Cp. also Horae, horal, horary, the first element in horography, horologe, horoscope.'\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985, spek- entry (line 979) and yēr- entry (line 1192)\", \"stance\": \"supports\", \"note\": \"HOROSCOPE is listed under both spek- ('Greek skopos, one who watches … HOROSCOPE') and yēr-, i.e. it is the compound hōra + skopos.\"}\n          ]\n        },\n        {\n          \"id\": 17,\n          \"lang\": \"Indo-European\",\n          \"words\": \"Wi-itos\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"This is Klein's and Watkins's analysis of the Germanic adjective 'wide': PIE *wi-ito- 'gone apart', a compound of the adverb/prefix *wi- 'apart, in half, asunder' (the root Nourai cross-refers to with '☞Wi') and *i-to-, the verbal adjective of *h₁ey- 'to go' — literally 'having gone apart, far apart'. Watkins: 'wi-. Apart, in half. 1. Suffixed form *wi-itos in Germanic *widaz in Old English wid, wide (< “far apart”): WIDE. [Pok. 1. wi- 1175.]' The analysis is old and widely repeated, but it is not certain: Etymonline reports it as 'perhaps (Watkins) from PIE *wi-ito-', and Germanic etymological handbooks treat *wīdaz as of unclear formation. Hence 'plausible'.\",\n          \"derivation_fa\": \"این همان تحلیلی است که کلاین و واتکینز از صفتِ ژرمنیِ «wide» به دست می‌دهند: *wi-ito- هندواروپایی به معنای «ازهم‌رفته»، مرکب از پیشوند/قیدِ *wi- «جدا، دو نیم، از هم» (همان ریشه‌ای که نورایی با نشانهٔ ارجاعِ «Wi» به آن حواله می‌دهد) و *i-to-، صفتِ فعلیِ ریشهٔ *h₁ey- «رفتن»؛ یعنی «آن‌که از هم رفته، فراخ». واتکینز می‌نویسد: «wi-. جدا، دو نیم. ۱. صورتِ پسونددارِ *wi-itos در ژرمنیِ *widaz در انگلیسیِ باستانِ wid ‹فراخ›». این تحلیل کهن و پرتکرار است اما قطعی نیست: اتیمانلاین آن را با قیدِ «شاید» می‌آورد و فرهنگ‌های ژرمنی ساختِ *wīdaz را روشن نمی‌دانند. پس با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://www.etymonline.com/word/wide\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1743\", \"status\": \"supports\", \"note\": \"Klein s.v. wide (read in KLN_1971.txt line 267049; the paginated 1966 scan on disk stops at c. p. 1697, so p. 1743 itself could not be seen): 'fr. Teut. *wida-, corresponding to I.-E. *wi-ito-, which is formed fr. I.-E. base *wi-, “asunder”, and the pp. stem of I.-E. *ei-, “to go”. For the first element see with, for the second see itinerant.' — verbatim Nourai's node, cross-reference to 'Wi' included.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985, w-list (AHD_watkins1985.txt line 1167)\", \"stance\": \"supports\", \"note\": \"'wi-. Apart, in half. 1. Suffixed form *wi-itos in Germanic *widaz in Old English wid, wide (< “far apart”): WIDE. … [Pok. 1. wi- 1175.]'\"},\n            {\"src\": \"Etymonline\", \"where\": \"s.v. wide\", \"stance\": \"partial\", \"note\": \"'from Proto-Germanic *widaz …, which is perhaps (Watkins) from PIE *wi-ito-, from root *wi- “apart, away, in half”' — the same analysis, but explicitly flagged as uncertain.\"},\n            {\"src\": \"POK\", \"where\": \"IEW 1175 (1. wi-), cited by Watkins\", \"stance\": \"partial\", \"note\": \"Pokorny files the Germanic word under wi- 'auseinander' but does not commit to the compound *wi-ito- as a proto-form.\"}\n          ]\n        },\n        {\n          \"id\": 18,\n          \"lang\": \"Germanic\",\n          \"words\": \"wît, wîdaz\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *wīdaz 'wide, vast', a thematic adjective (nom. sg. m. *wīdaz, the chart's second form; the first, wît, is the Old/Middle High German shape wît with final devoicing). Its descendants are Old English wīd 'wide, vast, long (also of time)', Old Saxon and Old Frisian wīd, Old Norse víðr, Dutch wijd, Old and Middle High German wīt, German weit, Danish and Swedish vid.\",\n          \"derivation_fa\": \"ژرمنیِ آغازین *wīdaz «فراخ، پهناور»، صفتی با ستاکِ o (فاعلیِ مفردِ مذکر *wīdaz، همان صورتِ دومِ نمودار؛ صورتِ نخست، wît، شکلِ آلمانیِ علیای باستان و میانه است با بی‌واک‌شدنِ همخوانِ پایانی). بازماندگانِ آن: انگلیسیِ باستانِ wīd «فراخ، پهناور، دراز (برای زمان نیز)»، ساکسونیِ باستان و فریزیِ باستانِ wīd، نروژیِ باستانِ víðr، هلندیِ wijd، آلمانیِ علیای باستان و میانهٔ wīt، آلمانیِ weit، دانمارکی و سوئدیِ vid. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/wide\"],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"the chart gives no reference for this node; the parent box's KLN:1743 covers it ('fr. Teut. *wida-').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Etymonline\", \"where\": \"s.v. wide\", \"stance\": \"supports\", \"note\": \"'Old English wid, also “vast, long,” also used of time; from Proto-Germanic *widaz (source also of Old Saxon, Old Frisian wid, Old Norse viðr, Dutch wijd, Old High German wit, German weit)'.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. wide (KLN_1971.txt line 267049)\", \"stance\": \"supports\", \"note\": \"'ME. wide, fr. OE. wid, rel. to OS., OFris. wid, ON. viðr, Dan., Swed. vid, Du. wijd, OHG., MHG. wit, G. weit, fr. Teut. *wida-'.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 (line 1167)\", \"stance\": \"supports\", \"note\": \"'Germanic *widaz in Old English wid, wide'.\"}\n          ]\n        },\n        {\n          \"id\": 19,\n          \"lang\": \"English\",\n          \"words\": \"wide\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old English wīd 'having great extension from side to side; vast, long' > Middle English wide > modern wide, with the regular Great Vowel Shift of OE ī to /aɪ/. The adverb wide continues OE wīde. Later senses are English developments: 'distended, spread apart' (c. 1500), 'embracing many subjects' (1530s), 'missing the intended target' (1580s).\",\n          \"derivation_fa\": \"انگلیسیِ باستانِ wīd «فراخ، پهناور، دراز» به انگلیسیِ میانهٔ wide و سپس به wide امروزی رسیده، با همان تحولِ منظمِ ī به /aɪ/ در جابه‌جاییِ بزرگِ واکه‌ها. قیدِ wide نیز دنبالهٔ wīde ی انگلیسیِ باستان است. معناهای پسین‌تر همه در خودِ انگلیسی پدید آمده‌اند: «گشوده، از هم باز» (حدودِ ۱۵۰۰)، «دربرگیرندهٔ موضوع‌های بسیار» (دههٔ ۱۵۳۰) و «خطاکننده به هدف» (دههٔ ۱۵۸۰). ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/wide\"],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"the chart gives no reference for this node; KLN:1743 on the grandparent box covers it.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Etymonline\", \"where\": \"s.v. wide (adj.) and wide (adv.)\", \"stance\": \"supports\", \"note\": \"'“having relatively great extension from side to side …” Old English wid'; 'wide (adv.) “to a distance; with a large space between,” Old English wide'.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. wide\", \"stance\": \"supports\", \"note\": \"'wide, adj. — ME. wide, fr. OE. wid' with 'Derivatives: wide, adv., wide, n., wide-ly, adv., wid-en, v.'\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 2,\n      \"root\": \"Eis 1\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *h₁eysh₂- 'to set in violent motion, impel, rush' (Pokorny 1. eis- 299; LIV² *h₁ei̯sh₂- 234)\",\n      \"note\": \"Pokorny IEW 299 heads '1. eis- ,(sich) heftig, ungestüm, schnell bewegen; antreiben = anregen, erquicken; auch vom Entsenden, Schleudern von Geschossen, Pfeilen'; Nominalbildungen: isǝro-s ,kräftig, heilig', … ois-mo- ,Ansturm, Zorn', ois-tro- ,Wut'.' Nourai's one-word gloss 'passion' is not Pokorny's but Watkins's: AHD 'eis-¹. In words denoting passion. [Pok. 1. eis- 299.]' — and since Nourai's node #3 (is-areno 'holy metal') is also verbatim Watkins, the whole chart is built on the AHD entry with a POK page tacked on. The root, the language label and the (loose) gloss are all defensible; the modern shape is *h₁eysh₂- with a laryngeal (Rix, LIV² 234; Cheung, Etym. Dict. of the Iranian Verb, *HaišH). The one soft spot is the gloss 'holy metal' on node #3, where Pokorny and Klein prefer 'the strong metal'.\",\n      \"note_fa\": \"پوکورنی در صفحهٔ ۲۹۹ ریشهٔ «۱. eis-» را چنین معنی می‌کند: «به‌تندی و شتاب حرکت کردن یا به حرکت درآوردن؛ برانگیختن؛ نیز پرتابِ تیر و سلاح»، و از ساخت‌های اسمیِ آن isǝro-s «نیرومند، مقدس»، ois-mo- «تاخت، خشم» و ois-tro- «دیوانگی» را می‌شمارد. معنایی که نورایی داده — تنها واژهٔ «passion» — از پوکورنی نیست بلکه عیناً از واتکینز است: «eis-¹ در واژه‌هایی که بر شور و خشم دلالت دارند». چون گرهِ سومِ نمودار («is-areno: فلزِ مقدس») نیز واژه‌به‌واژه از واتکینز است، پیداست که کلِّ این نمودار بر پایهٔ مدخلِ AHD ساخته شده و ارجاعِ پوکورنی تنها افزوده شده است. ریشه، برچسبِ زبان و معنای (کلیِ) آن پذیرفتنی است؛ صورتِ امروزیِ آن *h₁eysh₂- با حنجره‌ای است (ریکس در LIV² ص ۲۳۴ و چونگ ذیلِ *HaišH). تنها نقطهٔ سست معنای «فلزِ مقدس» در گرهِ ۳ است که پوکورنی و کلاین به‌جای آن «فلزِ نیرومند» می‌گویند.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81eys-\",\n        \"https://www.etymonline.com/word/iron\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:299\", \"status\": \"supports\", \"note\": \"POK_01.txt line 4358 (the standalone page mark '300' falls a few lines later, so the entry opens on p. 299): '1. eis- ,(sich) heftig, ungestüm, schnell bewegen; antreiben = anregen, erquicken; auch vom Entsenden, Schleudern von Geschossen, Pfeilen'; Nominalbildungen: isǝro-s ,kräftig, heilig', FlN Wort (e)isā, oisā usw., ois-mo- ,Ansturm, Zorn', ois-tro- ,Wut'.'\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, e-list (AHD_watkins1985.txt line 431)\", \"stance\": \"supports\", \"note\": \"'eis-¹. In words denoting passion. 1. Suffixed form *eis-ā- in Latin ira, anger: IRASCIBLE, IRATE, IRE. 2. Suffixed zero-grade form *is-(a)ro-, powerful, holy, in Greek hieros … 3. Germanic *isarno-, “holy metal” (possibly from Celtic), in Old English ise(r)n, iren, iron: IRON. … [Pok. 1. eis- 299.]' — Nourai's gloss 'passion' is Watkins's wording.\"},\n        {\"src\": \"CHEUNG\", \"where\": \"Etymological Dictionary of the Iranian Verb, s.v. *HaišH (CHEUNG.txt line 10996)\", \"stance\": \"supports\", \"note\": \"'*HaišH “to set in motion” … Avestan aēš- “to set in motion” … Old Persian (+ *fra-) fraiš- “to send forth” … PIE *h₁eisH₂- “to rush, impel, unleash, release” = LIV: 234 | Pok.: 299 ff.'\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, s.v. eisā, -io (ois-) (IEC.txt line 3477)\", \"stance\": \"supports\", \"note\": \"'eisā, io (ois-) “go, dash, impetus, outburst”. Cf. eismn-, oisā, eimi. Skt. éṣa “search; desire”; Lat. ira “anger”' — the same root with the same 'anger' derivative.\"},\n        {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 106 (WLD_band3.txt line 3009, Register: 'erquicken 1. eis- 106')\", \"stance\": \"supports\", \"note\": \"the index volume of Walde-Pokorny, the only volume on disk, sends 'erquicken' to 1. eis- at WP I 106 — the article Pokorny abridges on p. 299.\"},\n        {\"src\": \"Wiktionary\", \"where\": \"Reconstruction:Proto-Indo-European/h₁eysh₂-\", \"stance\": \"partial\", \"note\": \"'*h₁eysh₂-: to strengthen; to propel', with *h₁éysh₂-eh₂ > Latin īra and *h₁óys-mo-s (< *h₁óysh₂-mo-s with the Saussure effect) > Greek οἶμα, Proto-Iranian *Háyšmah. The modern gloss is 'strengthen, propel'; 'passion' is a label taken from the derivatives.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"aes-ma, aěš-ma\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan aēšma- m. 'wrath, fury' (Old Avestan aēšəma-, Young Avestan aēṣ̌ma-, which is what Nourai's double spelling aes-ma / aěš-ma renders) < Proto-Iranian *Haišmah < PIE *h₁óysh₂-mo-s, the o-grade *ois-mo- 'onset, anger' that Pokorny reconstructs (the -š- is the regular Iranian outcome of *-s- after the diphthong, and the laryngeal is lost by the Saussure effect). It is exactly cognate with Greek οἶμα 'stormy onset' (of a bird of prey) and Latin īra 'anger'. In the Avesta Aēšma is also the demon of Wrath, Aēšma-daēva, adversary of Sraoša, whose name reaches the Book of Tobit as Asmodeus. Caution: there is a homonym Avestan aēsma- (with plain s) 'firewood', a completely different word (< *aidh-s-mo-, whence NP هیزم hīzom), and Pokorny lists it under aidh- 'to burn' — the chart's word is the one with š.\",\n          \"derivation_fa\": \"اوستاییِ aēšma- (نرینه) «خشم، غضب» — در اوستایِ گاهانی aēšəma- و در اوستایِ نو aēṣ̌ma-، که همان دو املای نمودار (aes-ma و aěš-ma) است — از ایرانیِ آغازینِ *Haišmah و آن از *h₁óysh₂-mo-s هندواروپایی می‌آید، یعنی همان ساختِ *ois-mo- «تاخت، خشم» که پوکورنی بازسازی کرده؛ š بازتابِ منظمِ s پس از مصوتِ مرکب در ایرانی است. این واژه دقیقاً هم‌ریشهٔ οἶμα یونانی «حملهٔ توفنده» و īra لاتین «خشم» است. در اوستا «اَئشمَ» دیوِ خشم نیز هست (aēšma-daēva)، هماوردِ سروش، که نامش در کتابِ طوبیت به «اَسمودئوس» رسیده. هشدار: واژهٔ هم‌آوایِ aēsma- (با سِ ساده) به معنای «هیزم» واژهٔ دیگری است (از *aidh-s-mo-، ریشهٔ «سوختن») که فارسیِ «هیزم» از آن است و نباید با این یکی درآمیخت. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81eys-\",\n            \"https://en.wiktionary.org/wiki/%D8%AE%D8%B4%D9%85\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:299\", \"status\": \"supports\", \"note\": \"POK_01.txt line 4360: 'av. aēš- ,(sich) in eilige Bewegung setzen' (Präs. St. iša-, išya-, aēšaya-, apers. aišaya-); av. aēšma- m. ,Zorn''; and at line 4372 f. the comparison 'gr. Grundf. *oisma, vgl. av. aēšma-'.\"},\n            {\"ref\": \"BQT:754\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' p. 754 = BQT_v2_pages.txt leaf 212 (the page ends with the continuation note «بقیه در صفحهٔ ۷۵۵»), footnote 5 s.v. خشم: «خشم [بکسر اول، پهلوی … xēšm …]. اوستا -aēšma* «بارتولمه ...» ؛ غضب و قهر» — Mo'in gives the Avestan aēšma- and cites Bartholomae, exactly the arrow drawn.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Bartholomae, Altiranisches Wörterbuch, cols. 35 f. (BRT.txt line 2854)\", \"stance\": \"supports\", \"note\": \"'j. aēšma-, j. g. aēšəma- m. ,Zorn, Wut, Raserei, insbes. religiöse, gegen das Rind sich richtende (nur g.)''. (The homonym at col. 27, 'i. aēsma- m. ,Brennholz'', is the firewood word — a different lemma.)\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (Glossary), s.v. hēšm (NYB_vol2_glossary.txt lines 1987-1993)\", \"stance\": \"supports\", \"note\": \"'hēšm [hyšm, hšm] wrath, anger … personified as a demon, one of the chief evil powers … — Av. (35 sq.) aēšma- (Asmodaios, Book of Tobit 3:8 Av. aēšmō.daēva-); MPrth ʾsmgʾn “devils of wrath”; MPrs xyšm; Paz. NP xašm, xišm.' Nyberg's '(35 sq.)' is the Bartholomae column.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"Reconstruction:Proto-Indo-European/h₁eysh₂-\", \"stance\": \"supports\", \"note\": \"'*h₁óys-mo-s (< *h₁óysh₂-mo-s with the Saussure effect): Proto-Hellenic → Ancient Greek οἶμα; Proto-Indo-Iranian *Háyšmas → Proto-Iranian *Háyšmah'.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"xešm (xašm) «خشم»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian خشم xašm (Classical also xešm/xišm) 'anger' descends from Middle Persian xēšm / hēšm (Book Pahlavi ʾyšm, xyšm, hšm; Manichaean MP xyšm), which continues Old Iranian *aišma- = Avestan aēšma-: the Old Iranian initial diphthong aē- is reduced and acquires the secondary onset x-/h- that Book Pahlavi writes both ways, and Middle Persian ē is shortened to a/i in the New Persian form; the demon-name is retained in Zoroastrian Middle Persian as Xēšm, the demon of Wrath. Horn's entry is exactly this chain, and MacKenzie confirms the Middle Persian form. Note that Nourai's chart jumps straight from Avestan to New Persian and skips the Middle Persian stage, which is the crucial link.\",\n          \"derivation_fa\": \"«خشم» در فارسیِ نو (در فارسیِ کلاسیک خِشم/خِشم نیز) از فارسیِ میانهٔ xēšm / hēšm می‌آید — در پهلویِ کتابی به سه گونه ʾyšm، xyšm و hšm نوشته شده و در فارسیِ میانهٔ مانوی xyšm — و آن خود دنبالهٔ *aišma- ی ایرانیِ باستان، همان aēšma- ی اوستایی، است: مصوتِ مرکبِ آغازینِ aē- کوتاه شده و آغازهٔ ثانویِ x-/h- گرفته است، و ē ی فارسیِ میانه در فارسیِ نو به a/i بدل شده. در متونِ زردشتیِ فارسیِ میانه «خشم» همچنان نامِ دیوِ خشم است. مدخلِ هرن دقیقاً همین زنجیره را می‌دهد و مکنزی صورتِ فارسیِ میانه را تأیید می‌کند. تنها نکته آنکه نمودارِ نورایی از اوستایی یکراست به فارسیِ نو می‌جهد و حلقهٔ فارسیِ میانه را که مهم‌ترین حلقه است نمی‌آورد. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AE%D8%B4%D9%85\"],\n          \"ref_check\": [\n            {\"ref\": \"HRN:109\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 130 (page mark '-- 109 -'), no. 490: 'xišm, xešm ,Zorn'. aw. aēšma- ,Zorn'; phlv. xišm, xēšm.' — the Avestan source, the Middle Persian stage and the New Persian outcome, exactly as the chart has them (with both of Nourai's variants xešm and xašm covered by Horn's xišm/xešm).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary (PHD_mackenzie.txt line 5555)\", \"stance\": \"supports\", \"note\": \"'[xʾyšm] xēšm, hēšm | M xyšm, N xišm] anger; the demon Wrath.' — the Middle Persian link Nourai's chart omits.\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, s.v. hēšm\", \"stance\": \"supports\", \"note\": \"'hēšm [hyšm, hšm] wrath, anger … Av. (35 sq.) aēšma- … MPrs xyšm; Paz. NP xašm, xišm.'\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' p. 754, Mo'in's footnote s.v. خشم\", \"stance\": \"supports\", \"note\": \"«خشم [بکسر اول، پهلوی xēšm …]. اوستا -aēšma* «بارتولمه ...»؛ غضب و قهر».\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/خشم, Persian section\", \"stance\": \"supports\", \"note\": \"'From Middle Persian ʾyšm, xyšm (xēšm, “anger”), from Old Persian *aišima (compare Avestan aēšəma, aēṣ̌ma), from Proto-Iranian *HayšHmah, from Proto-Indo-Iranian *HayšHmas, from Proto-Indo-European *h₁oysh₂-mo-s, from *h₁eysh₂-.'\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Germanic\",\n          \"words\": \"is-areno\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The word is Proto-Germanic *īsarna- 'iron' (Gothic eisarn, Old Norse ísarn/járn, Old High German/Old Saxon īsarn, Old English īsern), matched by Celtic *īsarno- (Gaulish PN Isarno-, isarno-dori 'ferrei ostii', Old Irish íarn, Welsh haiarn). Nourai's form 'is-areno' inverts the suffix (*is-r̥-no- / *īsarno-), but the analysis he gives is exactly Watkins's: from the suffixed zero grade *is-(e)ro- 'powerful, holy' (the same formation as Greek ἱερός), i.e. iron as the 'holy metal', supposedly because the first iron worked was meteoritic. This is one of two readings. Pokorny (p. 300) explains the Celtic-Germanic word as 'das ,starke Metall' im Gegensatz zur weicheren Bronze' and thinks Germanic *īsarnan is borrowed, because of its ī-, from a Venetic-Illyrian *eisarnon; Klein s.v. iron says the same ('prob. Illyrian loan words, and orig. denoted the “strong” metal'), and Mann calls it 'Celtic and Gmc. Prob. a LW in Gmc.' So the root connection is standard, but the gloss 'holy metal' and the plain Germanic label are Watkins's option, not the consensus — hence 'plausible'.\",\n          \"derivation_fa\": \"واژه در اصل *īsarna- ی ژرمنیِ آغازین است («آهن»: گوتیِ eisarn، نروژیِ باستانِ ísarn/járn، آلمانیِ علیای باستان و ساکسونیِ باستانِ īsarn، انگلیسیِ باستانِ īsern) و همتای سلتیِ *īsarno- را دارد (نامِ گُلیِ Isarno-، ایرلندیِ باستانِ íarn، ولزیِ haiarn). صورتی که نورایی می‌نویسد («is-areno») جایِ اجزای پسوند را جابه‌جا کرده، اما تحلیلی که می‌دهد عیناً از واتکینز است: از صورتِ صفرْپایهٔ پسونددارِ *is-(e)ro- «نیرومند، مقدس» — همان ساختی که ἱερός یونانی از آن است — یعنی آهن به‌عنوانِ «فلزِ مقدس»، گویا از آن رو که نخستین آهنِ کارشده آهنِ شهاب‌سنگی بوده است. اما این تنها یکی از دو خوانش است: پوکورنی در صفحهٔ ۳۰۰ آن را «فلزِ نیرومند در برابرِ مفرغِ نرم‌تر» می‌داند و صورتِ ژرمنی را به‌سببِ ī آغازین وام‌واژه‌ای از ونتی–ایلیریِ *eisarnon می‌شمارد؛ کلاین نیز همین را می‌گوید و مان آن را «سلتی و ژرمنی، احتمالاً وام‌واژه در ژرمنی» می‌خواند. پس پیوندِ ریشه‌ای پذیرفته است ولی معنای «فلزِ مقدس» و برچسبِ سادهٔ «ژرمنی» رأیِ واتکینز است نه اجماع؛ از این رو با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://www.etymonline.com/word/iron\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 line 431, eis-¹ items 2-3: 'Suffixed zero-grade form *is-(a)ro-, powerful, holy, in Greek hieros, “filled with the divine,” holy … 3. Germanic *isarno-, “holy metal” (possibly from Celtic), in Old English ise(r)n, iren, iron: IRON.' Also Watkins's introduction (line 172): 'the Germanic and Celtic term was *isarno-, properly “holy (metal),” doubtless so called because the first iron was derived from small meteorites.' — the chart's gloss verbatim.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 299-300 (POK_01.txt, eis- entry)\", \"stance\": \"partial\", \"note\": \"'vielleicht hierher gall. Isarno- PN, isarno-dori ,ferrei ostii', air. mir. iarann n., cymr. haiarn …, ,Eisen' als das ,starke Metall' im Gegensatz zur weicheren Bronze; germ. *isarnan n., got. eisarn, ahd. as. anord. isarn ,Eisen' ist wegen des ī- vielleicht aus ven.-illyr. *eisarnon … entlehnt' — 'strong metal', and Germanic as a loan.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. iron (KLN_1971.txt line 126746)\", \"stance\": \"partial\", \"note\": \"'These words, as well as the Gaul. PN Isarno- and OIr. iarann, iarn, W. haiarn … are prob. Illyrian loan words, and orig. denoted the “strong” metal (in contradistinction to the softer bronze). Cp. OI. iṣiraḥ, “vigorous, strong”, Gk. ἱερός, “strong”, and see ire.'\"},\n            {\"src\": \"IEC\", \"where\": \"Mann, s.v. Isernos (IEC.txt line 6258)\", \"stance\": \"partial\", \"note\": \"'Isernos, -om “iron”. Celtic and Gmc. Prob. a LW in Gmc. … Gaul. isarno-; Br. huarn; W haiarn; Go. eisarn, n.; OE isern, isen, iren, n.; ON ísarn, járn' — no 'holy' gloss.\"},\n            {\"src\": \"Etymonline\", \"where\": \"s.v. iron\", \"stance\": \"partial\", \"note\": \"'This perhaps is an early borrowing of Celtic *isarnon …, which Watkins suggests is from PIE *is-(e)ro- “powerful, holy” … on the notion of “holy metal” or “strong metal” (in contrast to softer bronze)' — both readings left open.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"iron\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old English īsern, later īsen, then īren with rhotacism of the intervocalic -s-, whence Middle English iren/iron and modern iron; the alternative īsen survived into early Middle English as izen, and in the south the word tended to lose its -n (ire, yre) while in the north it contracted to irn/yrn. The chemical symbol Fe is from the unrelated Latin ferrum.\",\n          \"derivation_fa\": \"انگلیسیِ باستانِ īsern، سپس īsen و آنگاه īren با بدل‌شدنِ s میان‌واکه‌ای به r (روتاسیسم)، که به انگلیسیِ میانهٔ iren/iron و سپس iron امروزی رسیده است. صورتِ دیگر، īsen، تا آغازِ انگلیسیِ میانه به شکلِ izen مانده بود؛ در جنوبِ انگلستان این واژه گرایش به افتادنِ n داشت (ire، yre) و در شمال به irn/yrn فشرده می‌شد. نشانهٔ شیمیاییِ Fe از واژهٔ بی‌ربطِ لاتینِ ferrum گرفته شده است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/iron\"],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"the chart gives no reference for this node; the parent box's AHD reference covers it ('Germanic *isarno- … in Old English ise(r)n, iren, iron: IRON').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Etymonline\", \"where\": \"s.v. iron\", \"stance\": \"supports\", \"note\": \"'Middle English iron, iren, yron, from Old English iren, variant (with rhotacism of -s-) of isen, later form of isern, isærn “the metal iron; an iron weapon or instrument,” from Proto-Germanic *isarn'.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. iron (KLN_1971.txt line 126746)\", \"stance\": \"supports\", \"note\": \"'iron, n. — ME. iren, iron, fr. OE. īse(r)n, īren, rel. to OS. isarn, ON. ísarn, járn, OFris. iser(n) … Goth. eisarn, isarn.'\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-149.json > /dev/null && echo \"JSON OK\"",
 "description": "Write page-149 verification JSON"
}
```


### [2026-09-05T20:46:03.578Z] TOOL RESULT

```
JSON OK
```


## [2026-09-05T20:46:07.792Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/verify_check.py 149",
 "description": "Run verify_check for page 149"
}
```


### [2026-09-05T20:46:09.822Z] TOOL RESULT

```
nodes verified: 23/23
node verdicts: {'transcription_suspect': 2, 'plausible': 6, 'confirmed': 13, 'disputed': 2}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 11, 'not_checked': 9, 'partial': 5, 'not_found': 1}
books consulted: {'supports': 45, 'partial': 16, 'silent': 3, 'contradicts': 2} | by book: {'KLN': 13, 'Etymonline': 12, 'Wiktionary': 9, 'POK': 5, 'AHD': 5, 'SYN': 4, 'IEC': 4, 'MON': 2, 'BRT': 2, 'HUB': 2, 'PHD': 2, 'BQT': 2, 'NYB': 2, 'Wikipedia (fa)': 1, 'HRN': 1}
```


## [2026-09-05T20:46:32.081Z] AGENT

Done. Verification file written: `/home/sfmqrb/git/rishe/data/verification/page-149.json` — `verify_check.py 149` reports 0 PROBLEM lines.

**Page 149 (book p. 119) — 2 roots, 23 nodes**
- Root verdicts: confirmed 2 (Ei/Ey/I 1/Iâ 1; Eis 1)
- Node verdicts: confirmed 13, plausible 6, disputed 2, transcription_suspect 2
- Ref checks: supports 11, partial 5, not_found 1, not_checked 9 (nodes with `refs=None`)
- Books consulted: POK, AHD/Watkins, KLN (1966 paginated + 1971), WLD (Register), IEC, SYN, BRT, HRN, HUB, PHD, NYB, BQT (vols 2 and 4), MON, CHEUNG, Wiktionary, Etymonline, fa.wikipedia. 13 web pages archived via `fetch_source.py`.

**disputed**
- Ei — #7 Pahlavi `yâirka` "one year old": Horn 1116 (p. 249) gives it as **Old Persian** `*yāirka-` (Tomaschek's reconstruction), not Pahlavi, and hedges it; Hübschmann, Persische Studien p. 106 ad Horn 1116: "Ich halte die Etymologie für falsch." MacKenzie has no such MP word.
- Ei — #8 Persian `hîrak` هیرک: the word and gloss are right (BQT p. 2406, fetched as image), but Mo'in's own footnote on that page records Hübschmann's rejection of the 'year' derivation.

**transcription_suspect (both `error_in: book` — extraction is faithful)**
- Ei — #1 Greek `ieani`: impossible form; the book misprints Greek `ienai` (ἰέναι). Page image confirms "ieani" in print.
- Ei — #9 Latin `yâ-mo`: the book prints `yâ-mo` for AHD's `*yā-no-` (→ Lat. Iānus/iānua).

**No extraction errors** — every form, gloss, script and ref in `page-149.json` matches the printed page (image copied to `data/verification/sources/refs/ocr/BOOK/149.png`).

**Other things worth the owner's eye (recorded in the entry notes, not flagged verdicts):**
- Node #9 (Janus) is drawn under the *year* node, but Pokorny and Watkins both put `iā-no-` under the 'go' root itself; Nourai seems to have followed the page layout of Pokorny 296.
- The whole 'year' branch (#5) hangs on 'to go' only in the Pokorny/Klein/Watkins analysis; Beekes/Wiktionary keep `*yóh₁r̥` separate — hence `plausible`.
- #6: `yâh 2` and `jaiti` are mis-glossed 'year'; Pokorny p. 296 has Av. `yāh-` 'Krise, Entscheidung' and `yāiti` 'goes' — they belong to the parent 'go' root.
- `KLN:1796` (#6) does not exist: Klein's two-volume set ends at p. 1776; the substance is at KLN:1761 s.v. *year*. Likely a typo.
