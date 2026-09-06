# Verification process log — verify-page-237


## [2026-09-06T15:40:18.544Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 237 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-237.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-237.json. Write /home/sfmqrb/git/rishe/data/verification/page-237.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 237` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T15:40:20.474Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T15:40:21.283Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T15:40:21.298Z] TOOL RESULT

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


## [2026-09-06T15:40:21.299Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-237.txt"
}
```


### [2026-09-06T15:40:21.311Z] TOOL RESULT

```
1	=== PDF page 237 (book page 207) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Kam 2, Kamer, Kamp, Qam, Qem : to bend, also a cavity, vault  (refs POK:524,525)
4	#1 (parent #0) [Avestan] refs=POK:524 | kamarâ : waist, belt, also a vault
5	  #2 (parent #1) [Persian] refs=BQT:1694; MON:3068 | kamar «کمر» : waist, belt ; kamrâ «کمرا» : a room with high ceiling, also a stable | extra: کمربند
6	    #3 (parent #2) [English] refs=AHD | cummerbund, kummerbund
7	#4 (parent #0) [Old Persian] refs=POK:524,525 | kanpa : to bend ; čam : to bend, move fluently | NOTE: Compare with Avestan "xumba: bent" from Indo-European "Gěu 1:to bend".
8	  #5 (parent #4) [Persian] refs=POK:525; BQT:620,658,661,768,1439; HRN:99; FFD:48 | čapeh «چپه» : turned over, bent ; čap «چپ» : left ; čafteh «چفته» : bent ; čamîdan 1 «چمیدن» : walk flauntily ; xam «خم ۲» : a curve | extra: چمبر ؛ چماندن ، چمان ؛ خمیدن ، خماندن
9	#6 (parent #0) [Greek] refs=AHD | kamara : a vault ; kaminos : fire | NOTE: for heating a room
10	  #7 (parent #6) [Latin] refs=AHD | camera : room ; caminus : hearth
11	    #8 (parent #7) [French] refs=AHD | cabaret ; chambre
12	      #9 (parent #8) [Persian] refs=MON:2777 | kâbâreh «کاباره» : cabaret
13	      #10 (parent #8) [English] refs=AHD | cabaret, chamber
14	    #11 (parent #7) [English] refs=AHD | camera, chimney
15	#12 (parent #0) [Germanic] refs=AHD | himin, hibin : the vault (of heaven)
16	  #13 (parent #12) [English] refs=None | heaven
17	#14 (parent #0) [Latin] refs=POK:525; AHD:193 | campus : bent (land between mountains), a valley, open field ; Campania : (open fields) name of an area in Italy famous for its scales
18	  #15 (parent #14) [French] refs=KLN:266 | champaigne : open country, also name of a French district famous for its wine
19	    #16 (parent #15) [Persian] refs=MON:2001 | šâmpâyn «شامپاین» : Champaign
20	    #17 (parent #15) [English] refs=KLN:266 | Champaign, champion, camp
21	  #18 (parent #14) [Persian] refs=MON:2896; ARK:222; PLA:216 | capân «کپان» : a weighing scale | extra: قپان ، قبان
22	
```


## [2026-09-06T15:40:24.541Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-237.json",
 "description": "Read source JSON for page 237"
}
```


### [2026-09-06T15:40:24.587Z] TOOL RESULT

```
{
  "pdf_page": 237,
  "book_page": 207,
  "entries": [
    {
      "root": {
        "name": "Kam 2, Kamer, Kamp, Qam, Qem",
        "lang": "Indo-European",
        "refs": "POK:524,525",
        "gloss": "to bend, also a cavity, vault",
        "note": "See and compare with \"Gěu 1: to bend\""
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:524",
          "words": [
            {"translit": "kamarâ", "gloss": "waist, belt, also a vault", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1694; MON:3068",
          "words": [
            {"translit": "kamar", "gloss": "waist, belt", "script": "کمر"},
            {"translit": "kamrâ", "gloss": "a room with high ceiling, also a stable", "script": "کمرا"}
          ],
          "script_extra": "کمربند",
          "note": null,
          "quote": {
            "text": "چو گرگ ظلم را کشتی بزور بازوی عدلت - زانبوهی شده صحرای اقلیم تو چون کمرا",
            "poet": "A`ma`q Boxârâî"
          }
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "cummerbund, kummerbund", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "POK:524,525",
          "words": [
            {"translit": "kanpa", "gloss": "to bend", "script": null},
            {"translit": "čam", "gloss": "to bend, move fluently", "script": null}
          ],
          "script_extra": null,
          "note": "Compare with Avestan \"xumba: bent\" from Indo-European \"Gěu 1:to bend\".",
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "POK:525; BQT:620,658,661,768,1439; HRN:99; FFD:48",
          "words": [
            {"translit": "čapeh", "gloss": "turned over, bent", "script": "چپه"},
            {"translit": "čap", "gloss": "left", "script": "چپ"},
            {"translit": "čafteh", "gloss": "bent", "script": "چفته"},
            {"translit": "čamîdan 1", "gloss": "walk flauntily", "script": "چمیدن"},
            {"translit": "xam", "gloss": "a curve", "script": "خم ۲"}
          ],
          "script_extra": "چمبر ؛ چماندن ، چمان ؛ خمیدن ، خماندن",
          "note": null,
          "quote": {
            "text": "سرو چمان من چرا، میل چمن نمیکند؟ - همدم گل نمیشود ، یاد سمن نمیکند؟",
            "poet": "Hâfez"
          }
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "kamara", "gloss": "a vault", "script": null},
            {"translit": "kaminos", "gloss": "fire", "script": null}
          ],
          "script_extra": null,
          "note": "for heating a room",
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "camera", "gloss": "room", "script": null},
            {"translit": "caminus", "gloss": "hearth", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "French",
          "refs": "AHD",
          "words": [
            {"translit": "cabaret", "gloss": null, "script": null},
            {"translit": "chambre", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "MON:2777",
          "words": [
            {"translit": "kâbâreh", "gloss": "cabaret", "script": "کاباره"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 8,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "cabaret, chamber", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 7,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "camera, chimney", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "himin, hibin", "gloss": "the vault (of heaven)", "script": null}
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
            {"translit": "heaven", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 0,
          "lang": "Latin",
          "refs": "POK:525; AHD:193",
          "words": [
            {"translit": "campus", "gloss": "bent (land between mountains), a valley, open field", "script": null},
            {"translit": "Campania", "gloss": "(open fields) name of an area in Italy famous for its scales", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "French",
          "refs": "KLN:266",
          "words": [
            {"translit": "champaigne", "gloss": "open country, also name of a French district famous for its wine", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "Persian",
          "refs": "MON:2001",
          "words": [
            {"translit": "šâmpâyn", "gloss": "Champaign", "script": "شامپاین"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 15,
          "lang": "English",
          "refs": "KLN:266",
          "words": [
            {"translit": "Champaign, champion, camp", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 14,
          "lang": "Persian",
          "refs": "MON:2896; ARK:222; PLA:216",
          "words": [
            {"translit": "capân", "gloss": "a weighing scale", "script": "کپان"}
          ],
          "script_extra": "قپان ، قبان",
          "note": null,
          "quote": {
            "text": "همه گنج ارجاسپ در باز کرد - به کپان درم سختن آغاز کرد",
            "poet": "Ferdowsî"
          }
        }
      ]
    }
  ]
}
```


## [2026-09-06T15:40:25.235Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T15:40:25.275Z] TOOL RESULT

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


## [2026-09-06T15:40:32.464Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','KLN','BQT','MON','HRN','FFD','PLA','ARK','ARY','LEW','LAT','WLD','IEC','SYN','SKT','BRT','KNT','PHD','NYB','LKT','CHEUNG','FSD','WEB','TAD','AFM']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600])\n    print()\n\""
}
```


## [2026-09-06T15:40:32.834Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n 1,80p tools/verify_check.py && ls data/verification/ | head -50"
}
```


### [2026-09-06T15:40:34.247Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea

ARK {"title": "M.H. Rokn-zadeh Adamiyyat, Arkan-e Sokhan, Sharq 1347/1968", "kind": "catalog", "url": null, "lookup_hint": "Not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "none online. || RE-SEARCH 2026-09: nothing digitised on any permitted platform (archive.org, Google Books, Persian libraries/ebook stores). Check opac.nlai.ir manually / buy second-hand."}

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 

CHEUNG null

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; insi

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/
```


### [2026-09-06T15:40:34.284Z] TOOL RESULT

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
page-130.json
page-131.json
page-132.json
page-133.json
page-134.json
page-135.json
page-136.json
page-137.json
page-138.json
page-139.json
page-140.json
page-141.json
page-142.json
page-143.json
page-144.json
page-145.json
page-146.json
page-147.json
page-148.json
page-149.json
```


## [2026-09-06T15:40:39.014Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 532 533 534; do echo \"=== leaf $n ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$n\"' ' POK_01.txt | head -70; done"
}
```


## [2026-09-06T15:40:39.773Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"kam-er\" POK_full.txt | head -20; echo ---; grep -n \"kamp-\" POK_full.txt | head -20"
}
```


### [2026-09-06T15:40:41.257Z] TOOL RESULT

```
=== leaf 532 ===
=== leaf 533 ===
=== leaf 534 ===
```


### [2026-09-06T15:40:41.314Z] TOOL RESULT

```
43424:Root / lemma: kam-er- 
49214:Root/ lemma: keiner-: cancer, turtle, derived from Root/ lemma: kam-er-\ to bend, curve, 
49222:German Modern High German Hummer, presumably as ' vaulted animal' to kam-er- ' 
---
43478:Indo Germanic kamp- is possibly an extension from *kam- "bend, curve ' (see also the 
75004:*(s)kamb- rexrnuAs an kam-, kamp- 'bend' (above S. 525); sein relationship to (s)kemb-
```


## [2026-09-06T15:40:43.871Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '43400,43520p' POK_full.txt"
}
```


### [2026-09-06T15:40:43.936Z] TOOL RESULT

```
Root / lemma: kalni- 

Meaning: narrow passage 

Material: Latin callis^ lane, trod, path, footpath, forest path, pathway, sideway, trackway, 

mountain-track, forest pastures '; 

bulgar. k/an/k'room between stove, hearth and wall', serb. klanac. Gen. klanca^ defile, 
narrow passage between mountains ', sloven, klanec' defile, narrow passage between 
mountains, mountain path, rivlet of a brook, village lane ', Czech klanec^ saddle, pass, 
narrow road between mountains '. 

References: WP. I 356 f., WH. 1140 f. 
Page(s): 524 

Root / lemma: kamb- 
Meaning: ' bend, curve, crook ' 
See also: see below (s)kamb- 
Page(s): 525 

Root / lemma: kam-er- 

Meaning: to bend, curve, vaulted 

Material: Old Indie kmarati {ox\\y Dhatup.) 'is crooked'; 

Avestan kamarai. 'belt, girdle' (and '* dome '); 

gr. KpsAsGpov 'beam, ceiling, roof, house' (probably dissim. from *K[j£p£9pov), Kopiapa ' 
dome, four-poster bed; covered cart ' (to Solmsens BPhW. 1906, 852 f. assumption Carian 
origin, Kopapa AsysTai ra aacpaAr), s. Boisacq 402 Anm.; Latin loanword camera, camara^a 
vault, an arched roof, an arch'); at most KapTvoq 'oven' (certainly this could have derived 
from a culture word); 

Latin camur(us), -a, -^/t? 'arched, writhed, crooked, humped ' (dial.), genuine Latin 
camerus. 

References: WP. I 349 f., WH. I 146 f., 149 f., 306, Feist 6, 256; 
See also: s. also kam-p-. 
Page(s): 524-525 

Root / lemma: kam-p- 
Meaning: to bend 



Material: Old Indie kapana'\NO'cr(\, caterpillar, inchworm' {*kmpena), kampate '\.remb\es\ if 
originally ' writhes, curves ' (doubtful); ablaut, kumpa- (uncovered) " lahm an der Hand '; 

doubtful Old Indie kapata-u. "deceit, insidiousness' (would be *kmp-). 

gr. KaiJirn "bend", KaijnToo "curve, bend', KaiJTTuAo(;, Ka|ji|j6(; " writhed, crooked, humped 
'; Kapnri "caterpillar, inchworm'; Pannonian PN Campona; 

Maybe alb. Geg kama, Tosc kemba "leg, bent leg' : engl. Jamb n. A\so Jambe. me. [(0)Fr. 
jambe\eg, vertical support, f. Proto-Romance (whence late L gambahooi) f. gr. Kapinr).] 
The characteristic alb. m > /t?,^ shift. 

Latin campus ^i\e\(y (originally "bend, indentation, lowland, depression', as Lithuanian 
/anka\a\\ey, meadow' to /enkt/ 'bend'); 

Gothic /7a/77/fe "mutilated'. Old English hof paralyzed hands ', asachs. haf, Old High 
German /75/77r mutilated, lamed '; 

Lithuanian kampas 'po\nt, edge, angle ', Latvian kampis' Krummholz '; reduced grade 
(with Indo Germanic «= ein dark environment) Lithuanian kumptT crook oneself ', kumpas 
"crooked', Latvian kumpV become hunchbacked, crooked ', Old Prussian etkumpsMN. 
"against'; in addition probably Lithuanian kumste "fist' as *kump-ste " the fingers bending 
together '; 

perhaps poln. /rg/oa "river island covered with bush, shrubbery'. Old Church Slavic 
kqpina't\ thorn - bushes, thorns, rubus, bush, shrub', russ. /ri/yO//7a "shrubbery, bush, 
mound, knoll; bunch, fascicle, sheaf; 

Indo Germanic kamp- is possibly an extension from *kam- "bend, curve ' (see also the 
similar root (s)kamb-ixoxx\ gr. aKap(36(;, gall. Cambio-dunum e\.c.)\ yet compare also the 
nasalized equal meaning family of Old Indie capa-vn. n. "bow', capala-' resWess, 
fluctuating ', npers. cap "left', i.e. "*crooked'; Endzelin KZ. 44, 63 reminds of *capala-a\so 
in Latvian kaparuoties' wriggle ', k'eparaV wriggle, move with difficulty ', Lithuanian 
kapanotis " liegend sich aufzuhelfen suchen ' or " go laboringly '. 

References: WP. I 346, 350 f., WH. I 148 f., Trautmann 116. 
Page(s): 525 

Root/ lemma: kand-, skand- and (Old Indie) (s)kend- 
Meaning: to glow; bright, *moon 



Note: 

Root / lemma: kand- skand-and (Old Indie) (s)kend-\ "to glow; bright, *moon' derived 

from Root/ lemma: sen(o)-{*heno)\ 'old, *old moon' 

Material: Old Indie ^3/70(3// 'shines', Intens. participle cani-scadaV exceedingly gleaming' 

[*sknd-), candra- {scandra-, EN Hari-scandra-) 'luminous, gleaming, burning; m. moon', 

candana-m. n. ' sandalwood (incense '); 

gr. KQvSapoc; avGpa^ Hes.; 

alb. Geg hane, Tosc hene^moon' {*skandna) : Urdu chand'moon' 

PN Candavia : Maybe lllyrian PN Sca(n)din-avia 

(Kav5aouia), Candavii Montes. The mountains separating lllyricum from Macedonia, 
across which the Via Egnatia ran. 

Latin candeo, -e/ie 'gleam, shimmer, bright glow', transitive *candd, -ere\x\ accendo, 
incendo^ set on fire, ignite, inflame ', ca/7o'/b'i/s 'blinding, dazzling white, gleaming', candor 
' A dazzling, glossy whiteness, a clear lustre, clearness, radiance, brightness, brilliancy, 
splendor, glitter ', candela, candelabrum ' cand\est\ck, flambeaux' (out of it cymr. etc. 
cannwyll ds. {common Celtic -ns-, -nt- > -nn-}), cicindela^ little luminous beetle, oil lamp ', 
cicendula^ lamps ' (redupl. *ce-cand-)\
```


## [2026-09-06T15:41:12.805Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== AHD kam-er ===\"; grep -n -i \"kamer\\|kam-er\\|camera\\|cummerbund\" AHD_watkins1985.txt | head -20; echo \"=== AHD kemp/kamp ===\"; grep -n -i \"kamp\\|campus\\|Campania\" AHD_watkins1985.txt | head -20; echo \"=== AHD heaven ===\"; grep -n -i \"heaven\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-06T15:41:12.880Z] TOOL RESULT

```
=== AHD kam-er ===
332:grade form *bhndh- in Germanic *bund- in: a. Middle High German bunt, league: BUND?; b. Middle Dutch bondel, sheaf of papers, bundle: BUNDLE. 4. Suffixed form *bhendh-na-, “tied structure” (as of wicker), in Celtic *benna, manger, in Old English binn(e), manger: BIN. 5. Persian band, band, bandage, also a river levee: BUND!; CUMMERBUND. 6. Sanskrit badhndti (Sanskrit root bandh-), he ties: BANDANNA. [Pok. bhendh- 127.] bhengh-. Thick, fat. Extended zero-grade form *bhnghu- in Greek pakhus, thick, fat: PACHYDERM, PACHYSANDRA. [Pok. bhengh- 127.]
578:kamer-. To bend; a vault. 1. Greek kamara, a vault: (CABARET), CAMARILLA, (CAMERA), CHAMBER, (COM- RADE); (BICAMERAL). 2. Persian kamar, waist, girdle, oat something arched: CUMMERBUND. [Pok. kam-er- 524.
1295:BIB pd(i)- BIBLIOPOLE pel-5 BIBLIOTHECA dhé-1 BIBULOUS pd(i)- BICAMERAL kamer- BICEPS kaput BICORN ker-1 BICYCLE kwel-1
1328:CABARET kamer- CABEZON kaput CABLE kap- CABRILLA kapro- CABRIOLET kapro- CACHE ag- CACHEXIA segh- caco- kakka- CACODYL kakka- CACOETHES kakka-, s(w)e- CACOPHONOUS bha-2, kakka- CACOPHONY kakka- CACUMINAL keu-2 CADASTER  steigh- CADAVER kad- CADELLE kat-1 CADENCE kad- CADENT kad- CADET kaput CADRE kWetwer- CADUCEUS kar-2 CADUCICORN kad-, ker-1 CADUCOUS kad- CAECILIAN kaiko- CAECUM kaiko- CAELUM_ kae-id- CAESURA kae-id- CAGE keua-2 CAHIER kWetwer- CAINOTOPHOBIA ken-3 CAIRD kerd-2 CAISSON kap-
1332:CAM gembh- CAMARILLA kamer- CAMBIST skamb- CAMBIUM skamb- CAMERA kamer- CAMPYLOTROPOUS kamp- CAN! gno- CANAILLE kwon- CANARY kwon- CANCEL carcer CANCER kar-1
1342:CENTROBARIC gWere-2 CENTUM dekm CENTURY dekm CEPHALIC ghebh-el- CEPHALO- ghebh-el- -CEPHALOUS ghebh-el- CERAMIC ker-4 CERASTES ker-! CERATODUS dent-, ker-1 CERATOID ker-! CEREAL ker-3 CEREBELLUM ker-1 CEREBRUM ker-1 CERES ker-3 CERTAIN krei- CERVINE ker-1 CERVIX ker-1 CESSION ked- CESSPOOL spirare cEsTus! kent- CEsTUS? kae-id- CHAETA ghait- CHAETOGNATH genu-2, ghait- CHAFE dhé-1, kele-1 CHAFER gep(h)- CHAFF! gep(h)- CHAIR sed-1 CHALAZA gheled- CHALAZION gheled- CHALCID ghelegh- CHALCOCITE ghelegh- CHALCOPYRITE ghelegh- CHALCOsIS ghelegh- CHALICE kal-1 CHALLENGE kel-8 CHALONE ghé- CHAMAEPHYTE dhghem- CHAMBER kamer- CHAMELEON dhghem- CHAMFER bhreg- CHAMFRON kaput CHAMOMILE dhghem-, mélon CHANCE kad- CHANCEL carcer CHANCELLOR carcer CHANCRE kar-1 CHANGE skamb- CHANT kan-
1387:COMMODITY med- COMMON mei-! COMMOTION meue- COMMUNE mei-1 COMMUNICATE mei-1 COMMUNISM mei-1 COMMUTE mei-1 COMPACT! pag- COMPANION pa- COMPANY pa- COMPARE pera-2 COMPART pere-2 COMPASSION pé(i)- COMPEL pel-6 COMPELLATION pel-6 COMPENDIUM (s)pen- COMPENSATE (s)pen- COMPETE pet- COMPLACENT plak-! COMPLAIN plak-2 COMPLECT plek- COMPLETE pele-1 COMPLEX plek- COMPLICATE plek- COMPLICE plek- COMPLIMENT pele-1 COMPLY pele-1 COMPONENT apo- COMPORT per-2 COMPOSE apo-, paus-, COMPOSITE apo- COMPOSITION apo- COMPOUND apo- COMPRADOR pere-1 COMPREHEND ghend- COMPRESS per-5 COMPRISE ghend- COMPROMISE (s)meit(9)- COMPUNCTION peuk- COMPURGATION peue- COMPUTE peu- COMRADE kamer- con! kom
1402:CUBE keu-2 CUBICLE keu-2 CUBIT keu-2 CUCKING STOOL kakka- CUD gWet-1 CUDGEL ku- CUESTA kost- CUIRASS sker-1 CUISINE pekw- CUISSE koksa CULET (s)keu- CULINARY pekw- CULLET kwel-1 CULLIS kagh- CULM! kolem- CULMINATE kel-6 CULOTTES (s)keu- CULT kWel-1 CULTIVATE kwel-1 CULTRATE skel-1 CULTURE kvel-1 CULVER kel-5 cum kom CUMMERBUND bhendh-, kamer- CUMULATE keue-2 CUMULUS keue-2 CUNCTATION konk- CUNNILINGUS leigh-, (s)keu- CUNNING gné- CUNT ku-
=== AHD kemp/kamp ===
433:ekwo-. Horse. Possibly originally derived from kwon-. 1. Latin equus, horse: EQUESTRIAN, EQUINE, EQUITANT, (EQUITATION); EQUISETUM. 2. Greek hippos, horse: EO- HIPPUS, HIPPOCAMPUS, HIPPOGRIFF, HIPPOPOTAMUS. [Pok. ekuo-s 301.]
564:kamp-
579:kamp-. To bend. 1. Suffixed form *kamp-dé in Greek kampé, a bending, a winding: (GAM2), (GAMBADO2), (GAM-
581:BIT), GAMBOL, (GAMBREL), (GAMMON3), (JAMB). 2. Suf- fixed form *kamp-ulo- in Greek kampulos, bent: CAMPYLOTROPOUS. [Pok. kam-p- 525.] kan-. To sing. 1. Germanic *han(e)ni in Old English hen(n), hen: HEN. 2. Latin canere, to sing (> cantdre, to sing): CANOROUS, CANT?, CANTABILE, CANTICLE, CANTIL- LATE, (CANTO), CANTOR, CANZONE, CHANT; ACCENT, DESCANT, ENCHANT, (INCANTATION), INCENTIVE, PRE- CENTOR, RECANT. 3. Latin oscen, a singing bird used in divination (< *obs-cen, “one that sings before the au- gurs”; ob-, before; see epi): OSCINE. 4. Suffixed form *kan-men- in Latin carmen, song, poem: CHARM}. [Pok. kan- 525.] kand-. To shine. 1. Suffixed (stative) form *kand-é- in Latin candére, to shine: CANDENT, CANDID, (CANDIDA), (CANDIDATE), CANDLE, CANDOR; INCANDESCE. 2. Latin transitive *candere, to kindle, in compound incendere, to set fire to, kindle (in-, in; see en): (INCENDIARY), IN- CENSE. [Pok. kand- 526.] kannabis. Hemp. Late Indo-European word borrowed from an unknown source. 1. Germanic *hanipiz in Old English henep, henep, hemp: HEMP. 2. Greek kannabis, hemp: CANNABIS, (CANVAS). kanto-. A corner, a bending. Celtic *cantos, rim, border, in Latin cantus, canthus, iron ring around a carriage wheel, a wheel, rim (> Italian canto, corner): CANTEEN, CANTON; DECANT. [Pok. kan-tho- 526.] kap-. To grasp. I. Basic form *kap-. 1. Germanic *haf- in Old English hefeld, thread used for weaving, heddle (a device which grasps the thread): HEDDLE. 2. Germanic *haftjam in Old English heft, handle: Harr. 3. Form *kap-o- in Germanic *habai-, *habén in Old English habban, to have, hold: HAVE. 4. Germanic hafigaz, “containing something,” having weight, in Old English hefig, heavy: HEAVY. 5. Germanic *hafnd-, perhaps “place that holds ships,” in Old English hefen, a haven: HAVEN. 6. Germanic habukaz in Old English h(e)afoc, hawk: HAWK}, 7, Latin combining form -ceps (< *kap-s), “taker.” II. Suffixed form *kap-yo-. 1. Germanic *hafjan in Old English hebban, to lift: HEAVE. 2. Latin capere, to take, seize, catch: CABLE, CAPABLE, CAPACIOUS, CAPIAS, CAPSTAN, CAPTION, CAPTIOUS, CAPTIVATE, CAPTIVE, CAP- TOR, CAPTURE, CATCH, (CHASE!); ACCEPT, ANTICIPATE, CONCEIVE, DECEIVE, EXCEPT, INCEPTION, (INCIPIENT), INTERCEPT, INTUSSUSCEPTION, MUNICIPAL, NUNCUPA- TIVE, OCCUPY, PARTICIPATE, PERCEIVE, PRECEPT, RE- CEIVE, (RECOVER), RECUPERATE, (RX), SUSCEPTIBLE. III. Suffixed form *kap-s- in Latin capsa, repository, case: CAISSON, CAPSICUM, CAPSID, CAPSULE, CASE2, CHASE?, CHASES, CHASSIS, CHESS?; ENCHASE. IV. Length- ened-grade variant form *kdép-. 1. Germanic *hof- in compound *bi-hdf, “that which binds,” requirement, obligation (*bi-, intensive prefix; see ambhi), in: a. Old English behdf, use, profit, need: BEHOOF; b. Old English behéfian, to have need of: BEHOOVE. 2. Greek k6pé, oar, handle: copePpop. Compare ghabh-. [Pok. kap- 527.] kap(h)o-. Hoof. Lengthened-grade form kdp(h)-o- in Germanic *héfaz in Old English Adf, hoof: Hoor. [Pok. kapho- 530.] kapro-. He-goat, buck. Latin caper, he-goat (> capra, she-goat): CABRILLA, CABRIOLET, CAPELLA, CAPRIOLE, CHEVRON; CAPRIC ACID, CAPRICORN, CAPRIFIG, CAPROIC ACID. [Pok. kapro- 529.] kaput. Head. 1. Germanic *haubidam, *haubudam, in Old English héafod, head: HEAD. 2. Latin caput, head (> Italian capo, head): CABEZON, CADET, CAPE?, CAPITAL, CAPITAL, CAPITATE, CAPITATION, CAPITELLUM, CAPITU- LATE, CAPITULUM, CAPO!, CAPRICE, CAPTAIN, CATTLE, CAUDILLO, CHAPITER, CHAPTER, CHIEF, CHIEFTAIN; BI- CEPS, CHAMFRON, DECAPITATE, KERCHIEF, MISCHIEF, OCCIPUT, PRECIPITATE, RECAPITULATE, SINCIPUT, TRI- ceps. [Pok. kap-ut- 529.] kar-', Hard. I. Variant form ker-. 1. Suffixed o-grade form *kor-tu- in Germanic *harduz in: a. Old English hard,
1332:CAM gembh- CAMARILLA kamer- CAMBIST skamb- CAMBIUM skamb- CAMERA kamer- CAMPYLOTROPOUS kamp- CAN! gno- CANAILLE kwon- CANARY kwon- CANCEL carcer CANCER kar-1
1552:GAM2_ kamp- GAMBADO2 kamp- GAMBIT kamp-
1553:GAMBOL kamp- GAMBREL kamp- GAMETE geme- GAMMON3 kamp- GAMO- geme- GAMOSEPALOUS geme- -GAMOUS gema- -GAMY geme- GANDER ghans- GANG! ghengh- GANGLING ghengh- GANGLION gel-1 GANGRENE gras- GANGUE ghengh- GANNET ghans- GANOID gau- GAP ghai-
1619:HIPS keub- HIPPOCAMPUS ekwo- HIPPOGRIFF ekwo-
1698:JAMB kamp- JANITOR ei-1 JANUARY ei-1 Janus ei-1 JAVELIN ghabholo- JEALOUS ya- JELLY gel-3 JEOPARDY yek- JESS yé-
=== AHD heaven ===
136:Conceptions of the sky, heaven, were var- ied in the different dialects. As we have seen, the root deiw- occurs widely as the divinized bright sky. On the other hand, certain lan- guages viewed the heavens as basically cloudy; nebh- is “sky” in Balto-Slavic and Iranian, but “cloud” elsewhere. Another div- inized natural phenomenon is illustrated by the root (s)tene-, “thunder,” and the name of the Germanic god THOR.
275:ak-. Sharp. 1. Suffixed form *ak-yd- in: a. Germanic *akjo in Old English ecg, sharp side: EDGE; b. Germanic *akjan in Old Norse eggja, to incite, goad: EGG?. 2. Suf- fixed form *ak-u- in: a. Germanic *ahuz in Old English éar, zr, zhher, spike, ear of grain: EAR?; ACROSPIRE; b. Latin acus, needle: ACICULA, (ACUITY), ACUMEN, ACUTE, AGLET, EGLANTINE. 3. Suffixed form *ak-men, stone, sharp stone used as a tool, with metathetic variant *ka-men, with variants: a. *ka-mer- in Germanic *hama- raz in Old English hamor, hammer: HAMMER; b. *ke- men- (probable variant) in Germanic *himin-, in dissimi- lated form *hibin-, “the stony vault of heaven,” in Old English heofon, hefn, heaven: HEAVEN. 4. Suffixed form *ak-ond- in Germanic *agan6d in Old Norse dgn, chaff: awn. 5. Suffixed lengthened form *dk-ri- in Latin dcer, sharp, bitter: ACERATE, ACRID, ACRIMONY, EAGER}; CAR- VACROL, VINEGAR. 6. Suffixed form *ak-ri-bhwo- in Latin acerbus, bitter, sharp, tart: ACERB; EXACERBATE. 7. Suffixed (stative) form *ak-é- in Latin acére, to be sharp: ACID. 8. Suffixed form *ak-éto- in Latin acétum, vinegar: ACETABULUM, (ACETIC), ACETUM; ESTER. 9. Greek akantha (second element of Mediterranean origin), thorn, thorny plant: ACANTHO-, ACANTHUS; COELACANTH, PYRACANTHA, TRAGACANTH. 10. Suffixed form *ak-md- in Greek akmé, point: ACME, ACNE. 11. Suffixed form *ak-ro- in Greek akros, topmost: ACRO-; (ACROBAT), ACROMION. 12. Variant suffixed form *ok-su- in Greek oxus, sharp, sour: AMPHIOXUS, OXALIS, OXYGEN, OXYURIASIS, PAROXYSM. [Pok. 2. ak- 18, 3. kem- 556.]
360:[dan-. Low ground. Germanic root. Suffixed form *dan- Jam in: a. Old English denn, lair of a wild beast: DEN; b. possibly Old English Dene (genitive plural Dena), the Danes, and Old Norse Danr, Dane: DANE, DANISH; DANELAW. [In Pok. 2. dhen- 249.]] dap-. To apportion (in exchange). Suffixed form *dap-no- in Latin damnum, damage entailing liability (for repara- tion), harm: DAMAGE, DAMN; CONDEMN, DAMNIFY, IN- DEMNIFY, (INDEMNITY). [In Pok. dd- 175.] de-. Demonstrative stem, base of prepositions and ad- verbs. 1. Germanic *t6 in Old English #6, to: TO, TOO. 2. Perhaps Latin dé, dé-, from: DE-. 3. Latin déterior, worse: DETERIORATE. 4, Latin débilis, weak (see bel-). [Pok. de-, do- 181.] dé-. To bind. Contracted from *deo-. Greek dein, to bind: DESMID; ANADEM, ASYNDETON, DIADEM, PLASMODESMA, (SYNDESMOSIS), SYNDETIC. [Pok. dé- 183.] deigh-. Insect. Possibly in Germanic *tik-6, tikk-6 in Middle English teke, tick: TIck?. [Pok. deigh- 187.] deik-. To show, pronounce solemnly; also in derivatives referring to the directing of words or objects. I. Variant *deig-. 1. O-grade form doig- in: a. Germanic *taikjan, to show, in Old English t&can, to show, instruct: TEACH; b. Germanic *taiknam in (i) Old English tacen, tacn, sign, mark: TOKEN (ii) Old English tdcnian, to signify: BETO- KEN (iti) Gothic taikns, sign: TETCHY (iv) Old French tache, teche, mark, stain: TACHISM. 2. Latin digitus, finger (< “pointer,” “indicator”): picitT. II. Basic form *deik-. 1. O-grade form *doik- possibly in Germanic *taihw6 in Old English ta, tahe, toe: TOE. 2. Basic form *deik- in Latin dicere, to say, tell: DICTATE, DICTION, DICTUM, DITTO, DITTY; ADDICT, BENEDICTION, CONDI- TION, CONTRADICT, EDICT, FATIDIC, (INDICT), INDITE, INTERDICT, JURIDICAL, JURISDICTION, MALEDICT, PRE- DICT, VALEDICTION, VERDICT, VERIDICAL. 3. Zero-grade form *dik-d- in Latin dicdre, to proclaim: ABDICATE, DEDICATE, PREACH, PREDICATE. 4. Agential suffix *-dik- in: a. Latin index, indicator, forefinger (in-, toward; see en): INDEX, INDICATE; b. Latin jiidex (< *yewes-dik-), judge, “one who shows or pronounces the law” (jis, law; see yewes-): JUDGE, JUDICIAL; PREJUDICE; Cc. Latin vindex (first element obscure), claimant, avenger: (VEN- DETTA), VINDICATE; (AVENGE), REVENGE. 5. Greek deik- nunai, to show: DEICTIC; APODICTIC, PARADIGM, POLICY?. 6. Zero-grade form *dik- in Greek dikein, to throw (< “to direct an object”): DIsK. 7. Form *dikd in Greek diké, justice, right, court case: DICAST; EURYDICE, SYNDIC, THEODICY. [Pok. deik- 188.] deiw-. To shine (and in many derivatives, “sky, heaven, god”). I. Noun *deiwos, god. 1. Germanic *Tiwaz in: a. Old English Tiw (genitive Tiwes), god of war and sky: Tiu, (TuEspay); b. Old Norse Tyr, sky god: Tyr. 2. Latin deus, god: DEISM, DEITY, JOSS; ADIEU, DEICIDE, DEIFIC. 3. Latin divus, divine, god: DIVA, DIVINE!, (DI- VINE?). 4. Latin dives, rich (< “fortunate, blessed, di- vine”): Dives. 5. Suffixed zero-grade form *diw-yo-, heavenly, in Latin Didna, moon goddess: DIANA. 6. San- skrit devah, god, and deva-, divine: DEVI; DEODAR, DEVANAGARI. II. Variant *dyeu-, Jove, the name of the god of the bright sky, head of the Indo-European pan- theon. 1. Latin Jovis, Jupiter (> Italian Giove): JovE, JOVIAL. 2. Derivative *jou-il- in Latin Jiilius, “descended from Jupiter” (name of a Roman gens): JULY. 3. Voca- tive compound *dyeu-poter- (*pater-, father; see peater-), “O father Jove,” in Latin Juppiter, Jiipiter, head of the Roman pantheon: JuprTerR. 4. Greek Zeus, Zeus: ZEUS; (Dioscuri). III. Variant *dyé- (< *dyea-) in Latin diés, day (> Late Latin diurnum, day): DIAL, DIARY, DIET?, DISMAL, DIURNAL; ADJOURN, CIRCADIAN, (JOURNAL), (JOURNEY), MERIDIAN, QUOTIDIAN, (POSTMERIDIAN), SOJOURN. IV. Variant *deis- in Greek délos (< *deyalos), clear: PSYCHEDELIC. [Pok. 1. dei- 183.] dek-'. To take, accept. 1. Suffixed (stative) form *dek-é- in Latin decére, to be fitting (< “to be acceptable”):
697:leug-2. To break. Suffixed form *Jeug-é- in Latin ligére, to mourn (? < “to break down mentally”): LUGUBRIOUS. [Pok. leug- 686.] leugh-. To tell a lie. 1. Germanic *leugan in: a. Old English /Zogan, to lie: WARLOCK; b. Old English beléog- an, to tell lies about (be-, about; see ambhi): BELIE. 2. Germanic */ugiz in Old English lyge, a lie, falsehood: LIE’. [Pok. leugh- 686.] leuk-. Light, brightness. I. Basic form */euk-. 1. Suffixed form *leuk-to- in Germanic */euhtam in Old English léoht, liht, light: LicHT). 2. Latin lix, light: Lucrna, LUCULENT, LUX; LUCIFER, LUCIFERIN. 3. Suffixed form *leuk-smen- in Latin limen, light, opening: LIMN, LU- MEN, LUMINARY, LUMINOUS; ILLUMINATE, PHILLUMEN- 1st. 4. Suffixed form *leuk-snd- in Latin lina, moon: LUNA, LUNAR, LUNATE, LUNATIC, LUNE, LUNULA; DEMI- LUNE, SUBLUNARY. 5. Suffixed form */euk-stro- in: a. Latin listrum, purification: LUSTER, (LUSTRUM); b. Latin lastrdre, to purify, illuminate: ILLUSTRATE. 6. Suffixed form *leuko-dhro- in Latin licubrdre, to work by lamplight: LUCUBRATE. II. O-grade form *louk-. 1. Suffixed form *louk-o- in Germanic *lauhaz in Old English /éah, meadow (< “place where light shines”): LEA. 2. Suffixed (iterative) form *lowk-eyo- in Latin liicére, to shine (> licidus, shining): LUCENT, LUCID; ELUCIDATE, NOCTILUCA, PELLUCID, RELUCENT, TRANS- LUCENT. III. Zero-grade form *luk-. 1. Suffixed form *luk-sno- in Greek lukhnos, lamp: LINK?, LYCHNIS. 2. At- tributed by some to this root (but more likely of obscure origin) is Greek lunx, lynx (as if from its shining eyes): LYNX, OUNCE? [Pok. leuk- 687.] leup-. To peel off, break off. 1. Germanic *laubaz in Old English Jéaf, leaf: LEAF. 2. Germanic *laubja, “roof made from bark,” shelter, in: a. Old French loge, lodge: LODGE, (LOGE); b. Medieval Latin lobium, lobia, laubia, monas- tic cloister: LOBBY. 3. Attributed by some to this root is Germanic */uftuz, sky (traditionally explained as < “roof of the world,” vault of heaven), but probably a separate Germanic root, in: a. Old Norse opt, air, attic, sky: LOFT; ALOFT; b. Germanic */uftjan, to hold up in the air, in Old Norse /ypta, to lift: Lirt. [Pok. leup- 690.]
732:form *m6-ro- in Gaelic mor, big, great: CLAYMORE. [Pok. 4, mé- 704.] mé-4, To cut down grass or grain with a sickle or scythe. Contracted from *mea-. 1. Germanic *mé- in Old English mawan, to mow: Mow?. 2. Suffixed form *mé-ti- in Germanic *médiz in Old English m#th, a mowing, a mown crop: AFTERMATH. 3. Suffixed form *mé-twd-, a mown field, in Germanic *médw6 in Old English méd (oblique case m&@dwe), meadow: MEAD?, MEADOW. [Pok. 2. mé- 703.] med-. To take appropriate measures. 1. a. Germanic *metan in Old English metan, to measure (out): METE!; b. Germanic derivative *m#t6, measure, in Old English gem&te (ge-, with; see kom), “commensurate,” fit: MEET?. 2. a. Latin medéri, to look after, heal, cure: MEDICAL, MEDICATE, (MEDICINE), (MEDICO); METHEG- LIN, REMEDY; b. Latin meditdri, to think about, con- sider, reflect: MEDITATE. 3. Suffixed form *med-es-, replaced in Latin by *modes- by influence of modus (see 4. below), in: a. Latin modestus, “keeping to the appro- priate measure,” moderate: MODEST; IMMODEST; b. Lat- in moderdre, “to keep within measure,” to moderate, control: MODERATE; IMMODERATE. 4. Suffixed o-grade form *mod-o- in Latin modus, measure, size, limit, man- ner, harmony, melody: MODAL, MODE, MODEL, MODERN, MODICUM, MODIFY, MODULATE, MODULE, MODULUS, MOLD!, (MOOD?), (MOULAGE); (ACCOMMODATE), (COM- MODE), COMMODIOUS, (COMMODITY). 5. Suffixed o-grade form *mod-yo- in Latin modius, a measure of grain: MODIOLUS, MUTCHKIN. 6. Possibly lengthened o-grade form *méd- in Germanic *mét-, ability, leisure, in: a. Old English métan, to have occasion, to be permitted or obliged: MOTE2, MUST}; b. Germanic compound é-mot-ja- (prefix *é-, meaning uncertain, from Indo- hinppoes é, 6; see Pok. é, 6 280) in Old English émetta, rest, leisure: EMPTY. [Pok. 1. med- 705.] medhu-. Honey; also mead. 1. Germanic *medu in Old English meodu, mead: MEAD!. 2. Greek methu, wine (> methuein, to be intoxicated): AMETHYST, METHYLENE. [Pok. médhu 707.] medhyo-. Middle. 1. Germanic *midja- in: a. Old English midd(e), middle: M1D!; AMID; b. West Germanic diminu- tive form *middila- in Old English middel, middle: MIDDLE; Cc. Germanic compound *midja-gardaz, “middle zone” (*gardaz, enclosure, yard; see gher-1), name of the earth conceived as an intermediate zone lying between heaven and hell, in Old Norse Midhgardhr, Midgard: MipGarD. 2. Latin medius, middle, half: MEAN, MEDIAL, MEDIAN, MEDIASTINUM, MEDIATE, MEDIUM, MITTEN, MIZZEN, MOIETY, MULLION; INTERMEDIATE, MEDIEVAL, MEDIOCRE, MEDITERRANEAN, MERIDIAN, MILIEU. 3. Greek mesos, middle: MESO-. See also me-2. [Pok. medhi- 706.] meg-. Great. 1. Germanic suffixed form *mik-ila- in: a. Old English micel, mycel, great: MUCH; b. Old Norse mikill, great: MICKLE. 2. Suffixed form *mag-no- in Latin magnus, great: MAGNATE, MAGNITUDE, MAGNUM; MAG- NANIMOUS, MAGNIFIC, (MAGNIFICENT), (MAGNIFICO), (MAGNIFY), MAGNILOQUENT. 3. Suffixed (comparative) form *mag-yos- in: a. Latin major, greater: MAJOR, MAJOR-DOMO, MAJORITY, MAJUSCULE, MAYOR; b. Latin majestds, greatness, authority: MAESTOSO, MAJESTY; c. Latin magister, master, high official (< “he who is greater”): MAESTRO, MAGISTERIAL, MAGISTRAL, MAGIS- TRATE, MASTER, (MISTER), MISTRAL, (MISTRESS). 4. Suf- fixed (superlative) form *mag-samo- in Latin maximus, greatest: MAXIM, MAXIMUM. 5. Suffixed form *mag-to-, “made great,” in Latin mactus, worshiped, blessed, sacred: MATADOR. 6. Suffixed (feminine) form *mag-ya-, “she who is great,” in Latin Maia, name of a goddess: May. 7. Suffixed form *meg-a-l- in Greek megas (stem megal-), great: MEGA-, MEGALO-; ACROMEGALY, ALMA- GEST, OMEGA. 8. Variant form *megh- in Sanskrit maha-,
872:+ esse, to be; see es-): POSSIBLE, POTENT; (IMPOTENT), PREPOTENT. 3. Form *pot- in: a. compound *ghos-pot-, “suest-master,” host (see ghos-ti-); b. compound *dems-pot-, “house-master,” ruler (see deme-'). 4. Old Persian pati-, master: PADISHAH. [Pok. poti-s 842.] [prak-. To make, do. Greek root. Greek prassein (Attic prattein), to effect, do: PRACTICAL, (PRACTICE), PRAG- MATIC, PRAXIS. [In Pok. 1. per 811.]] prek-. To ask, entreat. 1. Basic form *prek- in Latin *prex, prayer (attested only in the plural precés), with denominative precdri, to entreat, pray: PRAY, PRAYER?, PRECARIOUS; DEPRECATE, IMPRECATE. 2. Suffixed zero-grade form *prk-sk- becoming *pork-sk-, contracted into *posk- in suffixed form *posk-to-, contracted into *posto-, which appears in Latin postuldre, to ask, re- quest: POSTULATE; EXPOSTULATE. [Pok. 4. perk- 821.] prep-. To appear. Suffixed zero-grade form *prp-yo- in Germanic *furbjan, to cause to have a (good) appearance, polish, in Old French fo(u)rbir, to polish, burnish: FuR- BISH. [Pok. prep- 845.] preu-. To hop. 1. Zero-grade form *pru- in Germanic *fru- in Old English frogga (with obscure expressive suffix -gga), frog: FROG. 2. Extended o-grade form *prowo- in Germanic *frawaz in: a. Middle Dutch uro, “leaping with joy,” happy: FROLIC; b. Old High German fré, happy, in frewida, joy (> German Freude): scHa- DENFREUDE. [Pok. preu- 845.] preus-. To freeze, burn. 1. Germanic *freusan, to freeze, in Old English fréosan, to freeze: FREEZE. 2. Suffixed zero-grade form *prus-to- in Germanic *frustaz, frost, in Old English forst, frost, frost: FROST. 3. Suffixed form *preus-i- in Latin *preusis, *preuris, act of burning, whence denominative pririre, to burn, itch, yearn for: PRURIENT, PRURIGO, PRURITUS. 4. Suffixed zero-grade form *prus-ina in Latin pruina, hoarfrost: PRUINOSE. [Pok. preus- 846.] pri-. To love. Contracted from *pria-. 1. Suffixed form *priy-o- in Germanic “frijaz, beloved, belonging to the loved ones, not in bondage, free, in: a. Old English fréo, free; FREE; b. Dutch vrij, free: FILIBUSTER. 2. Suffixed (participial) form “priy-ont-, loving, in Germanic ‘“fri- Jjand-, lover, friend, in Old English friond, fréond, friend: FRIEND. 3. Suffixed shortened form *pri-tu- in Germanic *frithuz, peace, in: a. Old High German fridu, peace: SIEGFRIED; b. Old French esfreer, to disturb: AFFRAY; c. Germanic *frij-, peace, safety, in compound *berg-frij-, “high place of safety” (see bhergh-?). 4. Suffixed femi- nine form *priy-G, beloved, in Germanic *frijj6, beloved, wife, in: a. Old Norse Frigg, goddess of the heavens, wife of Odin: Fricc; b. Germanic compound “*frije-dagaz, “day of Frigg” (translation of Latin Veneris diés, “Ve- nus’s day”), in Old English frigedeg, Friday: FRIDAY. [Pok. prdi- 844.] prokto-. Anus. Greek prokios, anus: PROCTITIS, PROCTOL- OGY, PROCTOSCOPE. [Pok. prdkto- 846.] pster-. Also ster-. To sneeze. Imitative root. 1. Suffixed form *ster-nu- in Latin sternuere, to sneeze: STERNUTATION. 2. Suffixed form *ster-t- in Latin ster- tere, to snore: STERTOR. [Pok. pster- 846.] pu-'. Also phu-. To blow, swell. Imitative root. 1. Ex- tended form *pus- in Latin pustula, a bubble, blister: PUSTULE. 2. Perhaps extended form “pit-, penis, in Latin praepiitium, foreskin (prae-, before, in front; see per’): PREPUCE. 3. Variant form *phi- in Greek phusa (> phusan, to blow), bellows, bladder: EMPHYSEMA, PHYSO- STIGMINE, PHYSOSTOMOUS. [Pok. 1. pu- 847.] pu-2, To rot, decay. 1. Suffixed form *pi-lo- in Germanic *filaz, rotten, filthy, in: a. Old English fi, unclean, rotten: FOUL; b. Old Norse fill, foul, akin to the Scandi- Navian source of FULMAR; ¢. Germanic abstract noun *filithd in Old English fylth, foulness: FILTH; d. Ger- manic denominative *filjan, to soil, dirty, in Old English fylan, to sully: FILE’; DEFILE!. 2. Extended form *pug- in Germanic *fuk- in Icelandic fiki, rotten sea grass, and
1582:HEAVEN ak-
```


## [2026-09-06T15:41:13.670Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT kamara ===\"; grep -n \"kamarƏ\\|kamara\\|kamarэ\\|kamar\" BRT.txt | head -30"
}
```


### [2026-09-06T15:41:13.721Z] TOOL RESULT

```
=== BRT kamara ===
5034:•  p.  ava'dä  {'da')  '\  j.  ava'8a  Adv.  i)  'dort, da':  \ patigrabanä  näma"  vardanam  . .  "da kamaranam  akunaus  Bh,  j.  ij  7,  9,  10, 2.6— 11^  16; — imaiy  martiyä  tyaiy  *ada- kly(sA.)  'da  aha''ta  Bh.4. 18;  j.  18',  2.  3, 6,J.4, 11,5.4;  —  didä  ..  'dasim  aväjanam Bh,  /.  13;  5. 1,  J.8'';  II  —  kva  .  .  °äa  bä  , . asne  hamsrihät  "wo  .  .  ?  .  .  dort  . ."  H.  2. 20,  *Vyt.54;  Yt6'.47>  Jp- 93>  N./5,  2^'; —  ''ha  agtaha  altahe  syao%nahe  ,  .  V.  4. 50.  a)  II  halä  avadas<^'''>  'von  da  aus': kami  udapatalä  bäbirauv  dubälJ"  namä" dahyäu/  halä  av  hauv  udapatata  Bh._j. 13;  J,  11;  —  hauv  . .  aÜyavaf"  paisiya- ^uvSdiim  haiä  av'  käram  *äyasatä  hyä''- param  *aif..  Bh.j.7  I ,  a)  'dorthin,  da- hin': U  raxa  rtSma!'  vardanam . .  'da  hauv .  .  *ä//Bh._y.6;  1. 19,  2.13;  — fravaSayS
13477:•  }.  därana'  d.  '(Mittel  zum)  Zunick-, Abhalten':  yö  htm  doste  'tum  ysi  hapfa atmsä  spmia ..kamarg^anqmai  t,t9/a."yitT de  benutzt,  die  sieben  ASp.  . .,  um  die Gegner  abzuhalten"  Yt.  2. 12  (?).
13692:äsnaila  zbayantsi  'ratca  Yt.  77.  * ;  ■ — ■  nara . .  ya  nasaum  avaJiUta  'ire  asahi  rasan- hqm  (sd.)  V.Ä'.g?;  YX.i4.^l\  —  Wp^r- sahyü  .  .  ari'tii  'raiy'''  paragmatä  "des Persers  Speer  ist  fernhin  gekommen"  D. ff.  4;  —  mit  Abi:  agibyS  'in  voha  as mand  (sd.)  Y.J4.  8.  a)  |  in  Verbindung mit  apiy  (sd.):  ahyäyä  bümiya  'raiapiy  D. 6.3;  X.I.3  (wo  'raiy  apty): —  mit  Aacä und  Abi.:  pSrs<^  marliytr  *'rayapiy''> hacä  pärsS^  kamaram  paliyajatä  D.  6. 4.  2)  Abis,  'von   fem;  fem;    femhin,
19395:—  matyd^  mam  xsnasatiy  Bh.  1. 13.  zu a):  hauv  ai?<^  hadä  kara  patil  mäm kamaranam  cartanaiy  Bh.i.  19;  2.12;  — fravartil    agarbayala    Uta    anayata    abiy
29090:•  j.  "ha'Sa,  g.,  p,  ha'dä  i)  Adv.  'an  ein und  dem  selben  Ort,  zusammen,  zugleich'; 'la  F.  2b,  24.  a)  Praen.;  a)  mit  Instr.; a)  'zusammen,  im  Verein  mit,  sammt, mit':  II  a/Vii*  adam  ,  .  jadiyämty  J'urJ'- mazdlm  'da  *vi^aiii/  bagaibis  aila*maiy t^ura^mazda  dadätuv  'du  .  .  bagaibÜ  D. 4.3;  3,  X.2. 3,  J.3',  4.3;  —  pasäva'' taxmaspad<^  "da  iam  asiyavt^  kamara- tiaiit  akunaui  'da  ci%'^t^taxmä  Bh.  2. >3'i  I.  6'.  7,  11',  I4>  i-  13,  19.  2.*i'>,  6",
29432:Zum'V.  iflf  {ar.  *sani-j-lha-),  eig.  'der  ein (feindliches)  Zusammentreflen  hat',  1.  Aamara-, kamaraita:  —  ai.  vgL  nir-flhä-  m.  —  Pö.: kamimär  (wozu  WEST  SEE.  5.  300),  —  ')  Nach F I ;  pron.  flektirt.  —  >)  Wohl  Gloise.  —  3)  Hds. har>\}%  s.  Cid,  COA.  iSg;.  403.
```


## [2026-09-06T15:41:35.595Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -on \"CAMP[A-Z]* [a-z()-]*\" AHD_watkins1985.txt | head -20; echo \"=== chimney/caminus ===\"; grep -n -i \"chimney\\|caminus\" AHD_watkins1985.txt KLN_1966.txt | head -20"
}
```


### [2026-09-06T15:41:35.653Z] TOOL RESULT

```
1332:CAMPYLOTROPOUS kamp-
1448:CAMPANE wel-
1619:CAMPUS ekwo-
=== chimney/caminus ===
KLN_1966.txt:3373:L.  area,  ‘vacant  piece  of  ground’.  See  next  word and  cp.  the  second  element  in  hectare, area,  n.  —  L.,  ‘vacant  piece  of  ground,  building, plot’,  rel.  to  arere,  ‘to  become  dry’,  hence  area orig.  meant  ‘a  place  burned  down,  a  dry,  bare  pla¬ ce’  ;  see  ardent  and  cp.  areola,  debonair.  For  sense development  cp.  G.  Esse,  ‘chimney,  forge , which  also  derives  fr.  I.-E.  base  *&s-,  ‘to  burn’. Areca,n.,  a  genus  of  palms  of  Asia  and  the  Malay Archipelago  ( hot .)  —  ModL.,  fr.  Port,  areca,  fr. Malayalam  ddakka ,  fr.  Tamil  adaikdy,  lit. ‘having  close  clusters  of  nuts’,  fr.  ddai,  close arrangement  of  the  cluster’,  and  kay,  ‘nut’.  See OED.  and  Yule-Burnell,  Hobson-Jobson,  p.35. Arecaceae,  n.  pi.,  a  family  of  plants,  the  palm family  (bot.)  —  ModL.,  formed  fr.  prec.  word with  suff.  -aceae.
KLN_1966.txt:6279:camera,  n.,  a  chamber.  —  L.,  ‘vault,  arched  roof, arch’,  fr.  Gk.  xotpdcpa,  which  is  rel.  to  xocp-Tvog (whence  L.  caminus),  ‘furnace’,  and  cogn.  with L.  camur ,  camurus,  ‘curved’,  fr.I.-E.  base  *qam-, *qem-,  ‘to  bend,  vault’.  Cp.  It.,  OProveng., Catal.  camera ,  Sp.  camara,  Port,  camara,  F.  cham- bre,  OHG.  chamara,  OS.  camara,  OSlav.  komora, Lith.  kamara ,  OIr.  camra,  which  all  derive  fr.
KLN_1966.txt:6280:L.  camera.  Cp.  chamber.  Cp.  also  camara,  Cam- barus,  camber,  chimney,  comrade,  concamerated. For  derivatives  of  a  -^-enlargement  of  base  *qarn- see  change.  Cp.  cant,  ‘slope’.  Cp.  also  heaven, camerlengo,  camerlingo,  n.,  the  papal  chamber- lain.  —  It.,  a  hybrid  coined  fr.  camera  (see  ca¬ mera)  and  the  Teut.  suff.  -ling.  Cp.  chamberlain. Cameronian,  n.,  a  follower  of  Richard  Cameron (died  in  1680).  For  the  ending  see  suff.  -ian. Camilla,  n.,  a  girl  of  noble  birth  employed  in  reli¬ gious  offices.  —  L„  fern,  of  camillus  (q.v.) Camilla,  fern.  PN.  —  Fr.  prec.  word, camillus,  n.,  a  noble  youth  employed  in  religious offices  ( Roman  antiq.)  —  L.,  fr.  Etruscan  Ca¬ millus,  ‘Mercury’,  fr.  Gk.  Ka§|i.tAog  (whence Kaa|iTAoc;),  name  of  one  of  the  Cabiri  in  Samo- thrace.  KaSpiAoc  is  prob.  related  to  KaSpog, ‘Cadmus’,  hence  of  Hebrew  origin;  see  Cad¬ mus.  The  Hebrew  origin  of  Gk.  KaSiifXog  is  sup¬ ported  by  the  fact  that  the  name  KafJeipcu  it¬ self  (whence  L.  Cabiri)  also  derives  from  He¬ brew  (see  Cabiri).
KLN_1966.txt:7416:Derivauves:  chimer-ic,  chimer-ic-al,  adjs. chimere,  n.  —  See  chimer. chimney,  n.  —  ME.  chimenee,  fr.  OF.  cheminee (F.  cheminee),  fr.  Late  L.  (camera)  caminata, ‘(a  room)  provided  with  a  chimney',  fr.  L.  ca- minus,  ‘forge,  hearth’,  fr.  Gk.  xapivoc,  which  is rel.  to  xxpdipx,  ‘vaulted  chamber’,  fr.  I.-E.  base *qam-,  *qem-,  ‘to  bend,  vault’.  See  camera  and cp.  words  there  referred  to. chimpanzee,  n.  —  From  a  S.  African  native  word, chin,  n.  —  ME.,  fr.  OE.  cin,  rel.  to  OS.,  OHG. kinni,  ON  kinn,  MHG.  kinne,  G.  Kinn,  ‘chin’.
KLN_1966.txt:15005:flue,  n.,  formerly,  a  chimney;  now,  a  channel  for the  passage  of  smoke,  etc.  —  Of  uncertain origin.
KLN_1966.txt:37767:Derivative:  Sybaritical-ly,  adv. sybotic,  adj.,  pertaining  to  a  swineherd.  —  Gk. ctuJJcotixoi;,  compounded  of  au;,  gen.  auos, ‘swine’,  and  the  stem  of  (3 oaxetv,  ‘to  feed’.  Gk. ctO;  is  a  collateral  form  of  up;  see  sow,  ‘female pig’.  For  the  second  element  see  botany,  for the  ending  see  adj.  suff.  -ic. sycamine,  n.,  mulberry.  —  L.  sycaminus,  fr.  Gk. auxapuvo;,  fr.  Phoen.  shiqmtn,  corresponding to  Heb.  shiqmim,  pi.  of  shiqmdh,  ‘mulberry’ ;  cp. Aram,  shiqma,  pi.  shiqmtn.  Cp.  also  next  word, sycamore,  sycomore,  n.,  1)  a  tree  of  Egypt  and Asia  Minor,  the  sycamore  of  the  Bible;  2)  a Eurasian  maple  tree;  3)  the  plane  tree.  —  ME., fr.  OF.  sicamor  (F.  sycomore),  dissimilated  fr. L.  sycomorus,  fr.  Gk.  auxoizopop.  For  the  first element  of  this  compound  word  see  prec.  word. The  second  element  is  identical  with  Gk.  p.£5pop, pLopop,  ‘mulberry’;  see  mulberry.
KLN_1966.txt:38058:tallage,  n.,  tax  paid  by  the  tenant  to  his  lord (Engl.  Feudal  Law).  —  ME.  taillage,  lalliage, tallage,  fr.  OF.  taillage,  lit.  ‘that  which  is  cut’, fr.  taillier  (F.  tailler),  ‘to  cut’.  See  tailor  and -age  and  cp.  tail,  ‘limitation  of  ownership’, tallboy,  n.,  1)  a  high  chest  of  drawers  (British);  2) a  kind  of  tall  chimney  pot.  —  Lit.  ‘high  wood’, fr.  F.  haul  bois,  E.  tall  being  the  translation  of F.  haul  and  E.  boy  a  corruption  of  F.  bois.  See tall  and  bush  and  cp.  highboy,  lowboy  and hautboy.
KLN_1966.txt:38803:tewel,  n.,  1)  a  hole  (obsol.);  2)  the  tuyere  of  a  fur¬ nace.  —  ME.  fuel,  ‘funnel,  chimney’,  fr.  MF. tuel,  tuiel  (F.  tuyau),  ‘pipe,  tube’,  fr.  OF.,  fr. Frankish  *put a,  of  s.m.  (whence  also  OProvcn?. tudei,  of  s.m.),  which  is  rel.  to  Goth,  put-haurn, ‘trumpet',  lit.  ‘sounding  horn’,  MDu.  tiite, MLG.  tine,  ‘anything  resembling  a  horn’ (whence  G.  Tide,  ‘paper  bag’);  of  imitative  ori¬ gin.  Cp.  tuyere.
```


## [2026-09-06T15:41:36.423Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KLN champaign p266 ===\"; grep -n -i \"champaign\\|champagne\" KLN_1966.txt | head -20; echo \"=== KLN cummerbund ===\"; grep -n -i \"cummerbund\\|kamarband\\|kamar-band\" KLN_1966.txt HJB.txt | head -20"
}
```


### [2026-09-06T15:41:36.486Z] TOOL RESULT

```
=== KLN champaign p266 ===
5748:brut,  adj..  dry  (said  of  wines,  esp.  of  champagne). —  F.,  ‘raw,  crude’.  See  brute, brutal,  adj.  —  See  brute  and  adj.  suff.  -al. Derivatives:  brutal-ity,  n.,  brutal-ize,  tr.  v. brute,  n.  —  F.  brut,  fem.  brute,  ‘raw,  crude’,  fr. L.  brutus,  ‘heavy,  dull,  stupid’,  which  is  cogn. with  Lett,  gruts,  ’heavy’,  OI.  guruh,  Gk.  (bap ti?, L.  gravis,  ‘heavy’.  See  grave,  adj.,  and  cp.  baro-, Briareus.
6289:camp,  n.  —  F.,  fr.  It.  campo,  ‘camp’,  fr.  L.  cam¬ pus,  ‘flat  space,  plain  field’  (whence  also  F . champ,  ‘field,  battlefield’),  fr.  I.-E.  base  *qamp-, ‘to  bend’,  whence  also  Gk.  xap.7tf),  ‘bend,  turn, winding  of  a  river’,  xaputTstv,  ‘to  bend,  curve, turn’,  xajjujxg,  ‘a  bending,  turning',  I  .;lh. kampas, ‘corner,  region’,  Lett,  kampis,  ‘a  crooked  piece of  wood’,  Lith.  kumpas,  ‘crooked’,  kumpti,  Lett. kumpt,  ‘to  become  bent,  to  curve’,  Goth,  hamfs, ‘mutilated’,  OHG.  hamf,  ‘crippled’  (lit.  ‘curved’), OE.  hofer,  ‘hump,  swelling’.  Cp.  campaign, campane,  campanile.  Campanula,  camper,  cam¬ pion,  campo,  campus,  campylo-,  champaign, champignon,  champion,  decamp,  encamp,  gamb, gamba,  schanz,  sconce,  ‘cover’,  the  first  element in  Camponotus,  Camptosorus,  champerty,  and the  second  element  in  elecampane,  Kulturkampf. Cp.  base  *(s)qamb-,  *(s)qemb-,  whence  Gk. nxauAnc,  ‘crooked,  bent’,  OIr.  camm,  ‘crooked, curved',  Mir.  cimb,  ‘tribute’,  cimbid,  ‘prisoner’, Gaulish  cambita,  ‘felloe’  (whence  F.  jante,  of s.m.);  see  change,
6292:campagna,  n.,  open  country.  —  It.,  fr.  Late  L. campdnia.  See  next  word, campaign,  n.  —  F.  campagne,  ‘open  country; campaign’,  fr.  It.  campagna,  fr.  Late  L.  Cam¬ pania,  ‘plain,  open  country’  (whence  also  Sp. campaha.  Port,  campanha),  fr.  campanius,  a  var. of  campaneus,  ‘pertaining  to  the  open  country', fr.  L.  campus,  ‘flat  space,  plain,  open  field’.  Cp. L.  Campdnia,  name  of  a  province  of  Italy  about Naples,  lit.  ‘the  plain  or  level  country’,  and  see camp,  n.  Cp.  also  campagna,  champaign.  Cp. also  next  word.
7158:champ,  tr.  and  intr.  v.,  to  chew'  noisily.  -  -Of  imi¬ tative  origin.  Cp.  jam,  ‘to  press  tightly’. Derivatives:  champ,  n.,  champ-er,  n. champac,  champak,  n.,  an  East-Indian  tree.  — Malay  tshampdka,  fr.  OI.  campakah,  which  is prob.  an  Austric  loan  word, champagne,  n.  —  F.,  abbreviation  of  vin  de  Cham¬ pagne,  ‘wine  made  in  the  province  of  Cham¬ pagne’,  a  name  derived  fr.  Late  L.  campania, ‘plain,  open  country’.  See  campaign  and  cp. champaign.
7159:Derivative:  champagne,  intr.  v. champaign,  n.,  open  country,  plain.  —  OF.  cham- paigne,  fr.  L.  campania.  See  campagna,  cam¬ paign,  and  cp.  champion,  scamp, champak,  n.  —  See  champac. champertor,  n.,  a  person  who  commits  the  act known  as  champerty  (law).  —  F.  champarteur, fr.  champart.  See  champerty  and  agential  suff. -or.
7163:champignon,  n.,  fungus,  mushroom.  — F., formed, with  change  of  suffix,  fr.  OF.  champegnuel, fr.  VL.  *campdniolus,  ‘that  which  grows  in  the field’,  fr.  Late  L.  campaneus,  ‘pertaining  to  the fields’,  fr.  campus,  ‘field’.  See  camp, champion,  n.  —  ME.,  fr.  OF.  champion,  fr.  Late L.  campionem,  acc.  of  campid,  ‘fighter’,  lit.  ‘one who  takes  the  field’,  fr.  L.  campus,  ‘field’.  See camp  and  cp.  champaign.
35216:Sillery,  n.,  a  champagne.  —  Named  after  Sillery, a  village  near  Reims  in  France, silly,  adj.  —  ME.  sely,  seely,  seilye,  ‘happy,  bless¬ ed,  innocent’,  fr.  OE.  sxlig,  gesxlig,  ‘happy,  for¬ tunate’,  formed  with  suff.  -ig  (=  E.  -y),  fr.  sxl, ‘time,  season,  occasion,  fortune,  happiness’.
=== KLN cummerbund ===
HJB.txt:7958:OTJMMEBBTJND,  s.  A  girdle. H.  from  P.  kamar-bandy  %.$.  *  loin-band.' Such  an  article  of  dress  is  habitually worn  by  domestic  servants,  peons,  and irregular  troops ;  but  any  waist-belt  is so  termed.
KLN_1966.txt:5029:‘manger,  crib’  (lit.  ‘place  where  the  animal  is tied  up’),  L.  of-fend-ix,  ‘a  band’,  Lith.  behdras, ‘common,  joint’,  as  a  noun  ‘partner’,  Lett. biedrs,  ‘companion,  comrade’;  see  R.Traut- mann,  Baltisch-Slavisches  Worterbuch,  p.30. Cp.  band,  ‘a  tie’,  bandhava,  bandhu,  bandoleer, bend,  besom,  bin,  bine,  bond,  bend,  bund,  bundle, bandal,  the  first  element  in  bundobust  and  the second  element  in  cummerbund,  sebundy. Derivatives:  bind,  n.,  bind-er,  n.,  bind-er-y,  n„ bind-ing,  n.  and  adj.
KLN_1966.txt:9902:cummerbund
KLN_1966.txt:9914:cummerbund,  n.,  waistband  (Anglo-Ind.)  — Hind.- Pers.  kamar-band,  fr.  Pers.  kamar,  ‘waist,  loins’, and  band,  ‘band,  bandage'.  See  bind  and  cp. band.
KLN_1966.txt:20888:lit.  ‘struggle  for  culture’,  compounded  of  Kultur (see  prec.  word)  and  Kampf,  ‘combat,  fight, struggle’,  which  is  a  loan  word  fr.  L.  campus, ‘field,  battlefield’.  See  camp, kumiss,  koumiss,  n.,  fermented  mare’s  or  camel’s milk.  —  Russ,  kumys,  fr.  Tatar  kumiz. kilmmei,  n.,  liqueur  flavored  with  carawai  seeds. —  G.  Kiimmel,  ‘cumin’,  fr.  OHG.  kumil,  a  dis- simil.  var.  of  kumin,  fr.  OF.  cumin,  comin  (F. cumin),  fr.  L.  cuminum.  See  cumin, kummerbund,  n.  —  See  cummerbund, kumquat,  also  cumquat,  n.,  a  small  orange  (Citrus Japonica).  —  Cantonese  pronunciation  of  Chin. kin-ku,  lit.  ‘gold  orange’, kuomintang,  n.,  the  Chinese  nationalist  revolu¬ tionary  party.  —  Chin.,  compounded  of  kuo, ‘nation,  nationalist’,  min,  ‘people’,  and  tang, ‘party’.
```


## [2026-09-06T15:41:49.920Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KLN heaven ===\"; grep -n -A2 \"^heaven,\\|heaven,  n\\.\" KLN_1966.txt | head -30; echo \"=== KLN cabaret ===\"; grep -n -i \"cabaret\" KLN_1966.txt SKT.txt | head -10"
}
```


### [2026-09-06T15:41:49.995Z] TOOL RESULT

```
=== KLN heaven ===
=== KLN cabaret ===
KLN_1966.txt:6007:Derivative:  cabalist-ic,  adj. cabaret,  n.  —  F.,  a  loan  word  fr.  MDu. cabret ,  denasalized  fr.  cambret,  camret,  fr. OPicard  cambrete,  dimin.  of  cambre,  ‘chamber, room’,  which  is  rel.  to  F.  chambre,  of  s.m.  See chamber  and  -et.
KLN_1966.txt:7149:Chamar,  Chumar,  n.,  i)  an  important  caste  in India;  2)  ( not  cap.)  a  leather  worker.  —  Hind. chamar,  fr.  OI.  carma-karah ,  ‘a  leather  worker’. For  the  first  element  see  shear  and  cp.  corium. The  second  element  is  related  to  OI.  kardti, krndti ,  ‘makes’,  fr.  I.-E.  base  *qwer-,  ‘to  make, form,  shape’.  See  Sanskrit,  and  cp.  words  there referred  to.  Cp.  also  churrus. chamber,  n.  —  ME.,  fr.  OF.  (=  F.)  chambre, ‘room,  chamber’,  fr.  L.  camera,  ‘vault,  arched roof,  arch’.  See  camera  and  cp.  antichamber, cabaret,  chambranle.  Cp.  also  next  word  and fille  de  chambre.
```


## [2026-09-06T15:41:51.829Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"}{n++; if (index($0,\"champaign,  n.,  open  country\")>0) print \"leaf\",n}' KLN_1966.txt; echo ---; awk 'BEGIN{RS=\"\\f\"}{n++; if (index($0,\"camp,  n.  —  F.,  fr.  It.  campo\")>0) print \"leaf\",n}' KLN_1966.txt"
}
```


### [2026-09-06T15:41:54.007Z] TOOL RESULT

```
leaf 152
---
leaf 132
```


## [2026-09-06T15:41:58.909Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['KLN'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['MON'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['FFD'],ensure_ascii=False,indent=1))\n\""
}
```


## [2026-09-06T15:42:00.504Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==152' KLN_1966.txt | grep -o \"26[0-9]\" | head; echo \"--- heaven grep\"; grep -n \"heaven,  n\" KLN_1966.txt | head; grep -n \"OE.  heofon\\|heofon\" KLN_1966.txt | head"
}
```


### [2026-09-06T15:42:00.900Z] TOOL RESULT

```
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
{
 "title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)",
 "kind": "website+archive_djvu",
 "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)",
 "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt"
 ],
 "page_offset": null,
 "covers_etymology": true,
 "notes": "covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم‌ها' instead, which do give Avestan forms (e.g. Frangrasyan) and can serve as a cross-check. noorlib has no Mo'in 6-vol entry found. The 6-vol edition itself was not found on archive.org, Google Books or HathiTrust full view. || RE-SEARCH 2026-09: still no scan of the 6-vol Amir Kabir edition (incl. vols 5-6 اعلام) on archive.org, Google Books (API quota-limited; WebSearch found no record with preview), HathiTrust (no record surfaced), noorlib, ketabnak (author page persons/6040 lists 34 Mo'in titles, none the 6-vol فرهنگ), tarikhema, picofile, scribd, Commons/Wikisource. Only the 2-vol Adena condensation exists (archive.org, mirrored on ketabnak 65980/65981, picofile, persianpdf, scribd); its image PDFs were downloaded to incoming/MON/ (the _text.pdf variants with OCR layer are at the same archive.org identifiers). The 6-vol set is purchase-only (in print: iketab.com, bookroom.ir/book/97022, 30book.com/Book/32100).",
 "cites": "page number of Mo'in's six-volume Farhang-e Farsi; MON5:… / MON6:… = volume 5 / 6 (proper names)"
}
{
 "title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995",
 "kind": "local_scan_ocr",
 "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)",
 "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages_faseng.txt"
 ],
 "page_offset": "115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X).",
 "covers_etymology": true,
 "notes": "Actual title is «ماده‌های فعل‌های فارسی دری» (Qoqnus). Open scan downloaded (image-only) and OCRed. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Entries: headword, then 'فارسی میانه ... < ایرانی باستان *...' with Latin transliterations (best read in *_pages_faseng.txt or on the page image). | OCR text, printed = pdf-5"
}
```


### [2026-09-06T15:42:02.989Z] TOOL RESULT

```
266
267
--- heaven grep
17369:Derivatives:  heave,  n.,  heav-er,  n. heaven,  n,  —  ME.  heovene,  hevene,  heven,  fr.  OE. heofon,  hefon,  rel.  to  OS.  helkm,  LG.  heben, heven,  ON.  himirn,  Goth,  himins,  OS.,  OHG. himil,  OFris.  himel,  himul,  MDu.,  Du.  hemel, MHG.  himel,  G.  Himmel,  ‘heaven,  sky’.  These words  prob.  derive  fr.  Teut.  base  *hama(n)-,  fr. I.-E.  base  *kem-,  *kam-,  ‘to  cover’.  See  chemise and  cp.  words  there  referred  to.
17369:Derivatives:  heave,  n.,  heav-er,  n. heaven,  n,  —  ME.  heovene,  hevene,  heven,  fr.  OE. heofon,  hefon,  rel.  to  OS.  helkm,  LG.  heben, heven,  ON.  himirn,  Goth,  himins,  OS.,  OHG. himil,  OFris.  himel,  himul,  MDu.,  Du.  hemel, MHG.  himel,  G.  Himmel,  ‘heaven,  sky’.  These words  prob.  derive  fr.  Teut.  base  *hama(n)-,  fr. I.-E.  base  *kem-,  *kam-,  ‘to  cover’.  See  chemise and  cp.  words  there  referred  to.
17370:Derivatives:  heaven,  tr.  v.,  heaven-ish,  adj., heaven-ish-Iy,  adv.,  heavenly  (q.v.) heavenly,  adj.  —  ME.  hevenly,  fr.  OE.  heofonlic. See  prec.  word  and  adj.  sufF.  -ly.
17371:Derivative:  heaveitli-ness,  n. heavenly,  adv.  (archaic).  —  ME.  hevenly,  fr.  OE. heofonlice ,  fr.  heofonlic.  See  heaven  and  adv. suff.  -ly.
```


## [2026-09-06T15:42:26.324Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HRN leaf for p.99 (leaf=printed+21 -> 120) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==120' HRN.txt | head -60"
}
```


### [2026-09-06T15:42:28.188Z] TOOL RESULT

```
=== HRN leaf for p.99 (leaf=printed+21 -> 120) ===
— 98 —
Auch np. ceh7'e (Wörterbücher jehre) 'Spinnrad' ge-
hört hier; dialectisch (Kasan) lautet das Wort cörd,
cöre, cir d. i. *care. In Vöniäün (Kä§än) bedeutet
car/^ auch ^Wetzstein (s. v. sunhade),
438. cer^n Teil, Haut\
s,w,carema7i' Teil'; phlv. carmm- ledern (vd. 18 (6)
Gl.); ai. cärmaU' 'Fell'.
oss. t. mr, curm, (315); afy. carman; kurd. LW.
car7n,
439. cerTdeti, weiden', cerend, cerägah {^^irrrd, Is. 30, 23),
cerämden.
aw. l/"6^ar-, caraiti gehen* ^) ; phlv. fehlt, vergl. aber
arm. LW. carak 'Weide', carakem; ai. [/car-, cdrati
'wandern, umherstreichen, weiden'.
kurd. darin \ af/. car[edal; oss. d. carun^ t. cärin
'leben, wohnen (317); bei. öarag, n. cara/ 'wandern,
umhergehen ; weiden, grasen ; reiten' (55).
Spiegel, Commentar I, 160 will auch np. cemen
'Wiese' (aus "^cermen) zu [/'car- stellen, doch ist dies
unsicher; aw. yavö.öaränlm (vd. 5, 5) wird kaum
'Getreidefeld' bedeuten, vergl. Geldner, KZ. 25, 200.
440. cesm 'Auge 2).
aw. dasman- 'Auge'; phlv. casm, casm[gäh, öasmak
('Quelle') ; ai. öaksm- 'Auge'.
kurd. zaza öim ; oss. d. caste, t. cäsf (318) ; bei. Sam,
n. c'am *Auge', öamay 'Quelle' (52, 53) ; wa/. cözm^ äi/n.
sar. cem^ sangl. sam^ minj. cam,
441. cespEden, cepsiden, cefslden (Inchoat.) 'packen, fassen*.
Zu lat. capiö (Nöldeke, mündliche Mitteilung).
Also vergl. got. hafjan 'heben', hafts 'behaftet, ge-
fesselt'; gr. aaini] 'Griff'; air. cacht 'Sklave; lett. kampt
'fassen' 3).
*) Nach Bezzenberger wäre ap. a6a]crtr/.s*Gememde weide*,
doch vergl. oben Seite 38 Anm. 1.
') AM. hat immer cism. Im 8ähn. reimt auf cesm häufig /psw,
wo man vielleicht auch cism und ^ism lesen darf.
*) Alb. kap *greife, fasse an, nehme gefangen* ist nach G. Meyer
aus t. qapnn*<i *fangen, erhaschen* entlehnt.
```


## [2026-09-06T15:42:28.300Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== CHEUNG cam ===\"; grep -n \"\\*čam\\|camitan\\|čamīdan\\|čam-\" CHEUNG.txt | head -20; echo \"=== CHEUNG kamb/xam ===\"; grep -n \"xam\\b\\|\\*kamb\\|xamīdan\" CHEUNG.txt | head -20"
}
```


### [2026-09-06T15:42:28.365Z] TOOL RESULT

```
=== CHEUNG cam ===
3736:*NWIR: ? NP čamīdan ‘to drink wine’, NP ¿am ‘eating and drinking’ (LW ?), Zaz. 
=== CHEUNG kamb/xam ===
28577:xam(b)-/xam(b)d- ‘to descend, go down’, xam(sr)v-/xamovd- (caus.) ‘to take down, 
49914:xam(b)-/xam(b)d-, 442 
49916:xam(bI)v-/xamovd-, 442
```


## [2026-09-06T15:42:33.166Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==121' HRN.txt | head -60"
}
```


## [2026-09-06T15:42:33.859Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '3700,3760p' CHEUNG.txt; echo \"=== cap left ===\"; grep -n \"‘left’\" CHEUNG.txt | head -10"
}
```


### [2026-09-06T15:42:34.599Z] TOOL RESULT

```
— 99 —
442. öu8t 'flink, tätig, passend'.
ai. l/cörf-, corföf^e 'antreiben ; sich beeilen' (Nöldeke,
mündliche Mitteilung).
Fr. Mtiller's (WZKM. 5, 68) Ableitung des Wortes
aus aw. cista- bezw. cista- ist schon wegen der Vokal-
difl^erenz (doch vergl. np. miizd) wenig wahrscheinlich.
443. eekuS 'Hammer .
aw. cakusqm, yt. 10, 130 'Hammer', Geldner, KZ.
25, 531 Note 210.
Das neupersische Wort ist nicht klar; eine Neben-
form ist öeköd oder deköj, vergl. dialektisch Kasan:
ceküSy rakoz, caküs, ödkös, vergl. kurd. cäqü, cek (H.-Sch.).
Nöldeke schlägt vor (mündliche Mitteilung), auch np.
öäk 'Spalt, Bruch' zu öekus zu stellen.
444. {\)ceni *Essen', cemfden 'trinken'.
ai. l/^(faw-, cämati (skr. camajiti) 'schlürfen',
oss. cimin, ba\dimin 'schlürfen* (320).
445. {2)ceni Sinn .
phlv. clm 'Urgrund, Ursache, Sinn .
Säle mann, Mol. asiat. IX, 233 Note 20.
446. cernber (geschrieben cenber) 'Kreis, Ring (z. B. Vis
und Ramin, S. 89 Vers 1)'.
V
phlv. cambar head-fiUet' (Säy. näSäy. HI, 4).
Zu np. cep 'links' (No. 435), gr. yAfiiJxct) 'biege',
adfinvXog (Nöldeke, mündliche Mitteilung).
Fick setzt als Wurzel für ai. capa- und gr. ad^iTiTO)
qep' an. Zu derselben Wurzel wird übrigens auch np.
xem, x^mm {*xeinp) — verschrieben in cem, Vullers s. v.
No. 12 — 'krumm, gebogen, yemtden etc. gehören.
447. eend 'einige*; wie viel?*, cendän, dendm, cendi,
aw. cvant' 'wie viel?'; phlv. cand.
kurd. LW. dend , dm; bei. cunt 'wie viel?' (64);
af;'. cof»[ira, com\ra wie viel?*; wa/. vum^ ciin, sar.
cund.
448. cöh 'Holz*.
phlv. 6öp 'Holz' (Guj. Ab.); kurd. cö, siw (H.-Sch.);
bei. LW. vöp (66); wa/. ^öpk, sar. /Jih,
7*
```


### [2026-09-06T15:42:34.659Z] TOOL RESULT

```
given for this root is ‘to congeal, coagulate, freeze, sim.’, but this is only true of a 
few passages with the present syayati (A.L.). A different interpretation (‘to fall 
down [of rain, etc.]’) seems preferable for the present Sryáte, see Kulikov, Vedic 
-ya-presents, s.v. chapt. III, si ‘fall’ (forthc.). 


«PIE? > LIV: 331 f. | Pok.: — 
*REFERENCES: IIFL II: 204, 235b; Andreev — PeSéereva: 326b; EVS: 100b; Lecoq 2002: 574b 


* аш ‘to swallow’ 

*AVESTAN: YAv. (“)Sam- ‘to swallow’ = Liste: 69 

Ү Ау. (*)Samat (P 8) 

*MIDDLE PERSIAN: (+ *à-) MMP ’sm- ‘to swallow’ = DMMPP: 54b 
Partic.: pres. pl. MMP ’sm’g’n, pass. perf. 'smyhyst 

*PARTHIAN: (+ *upa-) "b3^m- ‘о swallow, consume’ = DMMPP: 14b 
Partic.: pres. "bs^mg, perf. pass. ’bs’m’d; Inf.: ’bs’m’dn 

*KHOTANESE: LKh. tsam- ‘to swallow’ © SGS: 41 


*SOGDIAN: BSogd. š m to swallow’ || (+ *a-) BSogd. "ëm ‘to drink; swallow’ 

Pres.: SUBJ. 3sg. BSogd. §’m’th; Partic.: pres. ? SSogd. §’mn’y 'devouring ?' || (+ *a-) Pres.: IND. 35р. 
BSogd. ’’5’mth 

*CHORESMIAN: (+ *upa-) bs’m- ‘to drink’ — Samadi: 24 


40 *čjau 


*NWIR: ? NP čamīdan ‘to drink wine’, NP ¿am ‘eating and drinking’ (LW ?), Zaz. 
Simitis/Simen- ‘to drink’ || (+ *а-) NP asamidan ‘to drink’ 

*NEIR: Oss. I. cymyn/cymd, D. cumun/cund ‘to sip [tea, coffee, soup], gulp’, Pash. 
šum- ‘to drink, gulp’, Yi. sam-/Samd, M. som-/Samd ‘to drink’ 

*MISC: Orm. šam- ‘to sip’ 

*SANSKRIT: cam! ‘to sip, rinse’ (Br.+) > EWAia I: 530 

© The root must be reconstructed with initial *Ci-, on the basis of the Khotanese and 
Avestan evidence. This outcome, however, cannot be formally reconciled with Skt. 
cam'- (or other IE cognates). Ir. *&iam- has probably been influenced onomato- 
poetically (cf. EWAia, l.c.). 

«PIE *k”em- ‘to gulp, sip? > LIV: 389 f. | Pok.: 530 

*IE COGNATES: Arm. k‘amem ‘I squeeze out, sieve’, Gr. étepev ‘milked, squeezed 
out, NueAyev’ (Hes.), NIcel. hvóma ‘to gulp, swill down’ 

*REFERENCES: IIFL I: 407b; IIFL II: 252a; Abaev, Slovar’ I: 321 f.; DKS: 146; Werba 1997: 286; Paul 
1998: 314a; Cheung 2002: 126, 176; ESIJa II: 260 f.; NEVP: 79 


* ап ‘to move, go’ 
=== cap left ===
```


## [2026-09-06T15:42:47.421Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"camidan\\|čamīdan\\|to walk proudly\\|walk gracefully\\|strut\" CHEUNG.txt | head -20; echo ===; sed -n '3760,3830p' CHEUNG.txt"
}
```


### [2026-09-06T15:42:47.474Z] TOOL RESULT

```
Exit code 1
3278:*NWIR: NP Camidan ‘to walk proudly’, Bal. Camit/Cam- ‘to shake, dance, prance, 
3736:*NWIR: ? NP čamīdan ‘to drink wine’, NP ¿am ‘eating and drinking’ (LW ?), Zaz. 
15395:*NWIR: (?) NP camidan ‘to twist, bend’, NP caftah ‘curved, bent, a vaulted roof” 
(eval):1: == not found
```


## [2026-09-06T15:42:49.662Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '3240,3320p' CHEUNG.txt; echo \"==========\"; sed -n '15360,15440p' CHEUNG.txt"
}
```


### [2026-09-06T15:42:49.724Z] TOOL RESULT

```
du-Coekaenoen/du-Coekoen- ‘to glue, stick together’, NP ¿ak ‘fissure, rupture, cleft, 
crack’ 

*NEIR: Oss. I. cæğdyn/cağd, D. cae£dun/cagd ‘to shake (out); to strike the iron; to 
play on an instrument, clock’ ? Yzgh. cok-/Cokt ‘to pound; to stamp, put on a pattern 


32 *éam ? 


[of tattoos]’, Wa. cuk-/Cukt- ‘to strike’ (LW ?), ? Sh. cuy, Rosh. coy ‘breaking, 
tearing, ripping up’ (EVS: 23a: < **¢/@r/dr-agu- ?) || (+ *fra-) Oss. D. 
rezegdun/rezaxt, (inch.) D. rezaxsun/rezaxst ‘to spread around, scatter’, Oss. 
rezegd ‘heap’ || (+ *ui-) Oss. D. izæğdun/íizağd ‘to spread, scatter’, Oss. D. Z&gn& 
‘tinder’ 

*MISC: (+ *pati-) Arm. patéén (LW), Hebr. ptsgn ‘copy’ (LW, Esther 3:14), Syr. 
рагёарпа ‘copy’ (with sec. -r-, Benveniste 1934: 180 ff.) 

© The root is no doubt expressive in origin. A second expressive/onomatopoetic root 
is cited in ESIJa II: 211 f.: *éak ‘to drip; flow’. Most, if not all, Iranian forms seem 
to point to borrowing from (New) Persian cakidan/Cak-, which evidently cannot go 
back to РЇ. 

*PIE— > LIV: – | Pok.: 


*REFERENCES: Christensen, Contributions I: 62; Abaev, Slovar’ I: 298 f., 540 f.; Abaev, Slovar’ II: 363 f.; 
Edel’man 1971: 62; Nyberg II: 147a; ESIJa II: 213 ff. 


*éam ? ‘to walk’ 

*PARTHIAN: cm- ‘to walk, move to’ => Ghilain: 56, 72 | DMMPP: 125b 

Pres.: IND. 3sg. cmyd, 3р1. cmynd, SUBJ. 25р. cm’h, 1р1. cm’m; Partic.: perf. pass. H cm’d; Inf.: cm’dn 
*KHOTANESE: ? tcama- ‘leaping insect, either locust or grasshopper’ 

*NWIR: NP Camidan ‘to walk proudly’, Bal. Camit/Cam- ‘to shake, dance, prance, 
dangle’ 

*MISC: Par. é(h)im-, ¢(h)em-/c(h)imi ‘to go, move, wander’, Par. &imö ‘walking, 
gait’, Arm. (LW) ¿em ‘walk’ 

*SANSKRIT: camüra- ‘an antilope’ (Harav., Sis.) > EWAia Ш: 180 f. 

9 This sparingly attested root does not have an IE origin and may be a blend of 
*čar(H) and *gam! ? Rastorgueva — Edel’man (ESIJa П: 261 f.) cite a late Skt. form 
camura- ‘an antilope’, which would be borrowed from an Iranian, possibly Parthian, 
source. Skt. camura- is perhaps rather a so-called "substrate" word, as it 
phonologically conforms to the category of forms with long middle vowel, e.g. 
mayüra- ‘peacock’, on which see Lubotsky, Early Contacts:305 ff. 


*PIE— > LIV: – | Pok.: 
*REFERENCES: IIFL I: 246a; DKS: 139a; Shahbakhsh: s.v. ¿am- 


*tap ‘to seize, attach, stick, strike’ 

*KHOTANESE: ? Khot. cev- ‘to get? — SGS: 34 

*SOGDIAN: (+ *fra-) MSogd. Br’cp- ‘to press’ (cf. Sims-Williams, apud Sundermann 
1981: 181b) 

Impf.: IND. 3pl. MSogd. Br'cp nt (MKG: 593) 

*CHORESMIAN: čp- ‘to attach to, contrive (a lie) against (someone)’ = Samadi: 58 f. 


*éarH 33 


*NWIR: NP capidan/cap-, Gur. (Kand.) ёараи$ап kär-, Khuns. Cap-/Cäpä ‘to plunder, 
rob’ (LW), Bal. campit/Camp-, canpit/Canp- ‘to snatch’, NP cafsidan, Abz. 
cawsowa/caws-, Nn. Cäsb-, Qohr. Caspada/éasp-, Tr. Cawsa(ya)/Caws- (inch.) ‘to 
stick, adhere’, ? Anar. Capowger ‘robber, thief? 

*NEIR: Oss. cevyn/cavd, D. cævun/cavd ‘to hit, strike’, Yghn. Cümf-/£ümfta ‘to push 
(to)’, Sh. cäp-/cäpt ‘to feel, touch’, Oss. І. cefsyn/cefst, D. caefsun/caefst (inch.) ‘to 
stick, glue’, M. cab-/cavd ‘to pluck’ || (+ *us-) Oss. I. sk’afyn/sk’eft, D. (z)sk’zfun 
==========

*NWIR: Awrom. kiastay/kian-, Gur. (Bajal.) kiast-/kian-, (Gahv.) kian-, (Kand) 
kiast-/kián-, Abz. kinowa/kin-, Qohr. kinada/kin-, Siv. kin-/kine ‘to send’ || (+ *a-) 
Abyan. ајауа/ајеу- ‘to approach’ 

9 Hitherto there was no known etymology for these modern, yet relatively archaic 
forms. They are perhaps connected to the IE root *keiH>- ‘to set in motion, go’. The 
forms with initial k- reflect a caus. formation *koiH>-eIe-. 

«PIE *keiH>- ‘to set in motion, go’ = LIV: 346 | Pok.: 538 


*IE COGNATES: Gr. кіо ‘I set in motion, go’, клуёо, Lat. cieö ‘I set in motion’ 
*REFERENCES: КРЕ II: 388, 206, 415, 443; MacKenzie 1966: 100; WIM III: 111; Jusupova 2000: 85; 
Lecog 2002: 121, 124, 127, 572 (passim) 


*kamp ‘to bend’ 

*PARTHIAN: (+ *ni-) nkmb- ‘to bend’ = DMMPP: 242b 

Pres.: IND. 3sg. "nkmbyd, 3pl. nkmbynd 

*SOGDIAN: CSogd. qmp- (f.) ‘strategem, ruse’ || (+ *apa-) BSogd. pk’np- ‘to turn 
away, deflect’ || (+ *a-) ? MSogd. ”’kmb ‘to suppress, curb, restrain’ (v. Sogdica: 
43.9 f.) || (+ *ni-) BSogd. nk’np- ‘to bend; subdue’ 

(+ *apa-) Pres.: IND. 3sg. BSogd. pk’nptt || (+ *a-) Partic.: perf. pass. BSogd. ’’k’Bt’k ‘crooked, not 
straight’ f. BSogd. ’’k’Btc-(h), BSogd. ’’k’Btcy-h ‘crooked’ || (+ *ni-) Pres.: IND. 35р. BSogd. nk’npt, 
Inf.: BSogd. nk’np’y 

*CHORESMIAN: (+ *4-) m/’kfs- ‘to be(come) bend, curved; to be lowered’, (caus.) 
m['knby- ‘to bend, curve’ || (+ *us-) m/sknb- ‘to trip, stumble’ || (+ *ni-) m/nknby- 
‘to sink down’ = Samadi: 4, 181, 129 

*NWIR: (?) NP camidan ‘to twist, bend’, NP caftah ‘curved, bent, a vaulted roof” 
*NEIR: ? Pash. (Waz.) cavda ‘nook under overhanging rocks, cave’ (< NP ?) || (+ 
*ni-) Rosh. nijum ‘fall’ (in nifum ¿ug ‘they fell’) 

9 There is little evidence for a (separate) root *kamp with the meaning ‘to shake, 
tremble’, matching Skt. kamp. The Avestan form *kafsan (Yt 10.113), cited in Liste: 
14 as evidence, is unclear. These forms are often connected to Gr. xà jo ‘I bend’, 
Lith. kumpti ‘to be crooked, bent’, karmpas ‘corner’, etc. (albeit with queries in LIV, 
l.c.), which are assigned an IE provenance accordingly. However, the unusual 
structure of the forms is not typical for IE: they may rather point to borrowing from 
a substratum language, cf. Beekes 1969: 134 (also Beekes, A Greek etymological 
Dictionary, www.ieed.nl: s.v. KA LTT). 

«PIE? > LIV: 342 | Pok.: 525 

*REFERENCES: EVP: 18; GMS: раг. 676; EVS: 48b; ESIJa П: 226 Ё; МЕУР: 18 


*kan! ‘to throw, place, put; to destroy’ 
*AVESTAN: (+ *ni-) ? Y Av. ni kan- ‘to bury’ || (+ *ui-) YAv. vikan- ‘to destroy, ruin’ 


230 *kanl 


Pres. athem. {1}: IND. 3sg. ()vika(i)nti (У 3.13), *vikonti (V 3.22); Caus.: pres. SUBJ. 3sg. ҮАУ. 
vikänaiiät (V 7.51); Pres. them. {2}: OPT. 3pl. ? YAv. ni kanaiion (V 17.12) 

*OLD PERSIAN: (+ *aua-) ? avakan- ‘to throw, place on’ || (+ *ni-) nika(n)- ‘to tear 
down’ || (+ *ui-) vika(")- ‘to destroy’ > Kent: 178b 

Pres. (a)them.: impf. IND. 1sg. avakanam <a-v-a-k-n-m> (DB 1.86), viyakanam <vi-i-y-k-n-m> (XPh 
38), 3sg. viyaka <vi-i-y-k> (DB 1.64), SUBJ. 2sg. vikanahy <vi-i-k-n-a-h-y> (DB 4.71, DB 4.73), 
vikanah° <vi-i-k-n-a-h-° > (DB 4.77), IMPV. 3sg. nika" tuv <n-i-k-tu-u-v> (DB 4.80) 

*MIDDLE PERSIAN: MMP qn-, BMP kn- /kan-/ ‘to dig (up); to raze, destroy’ || (+ 
*apa-) MMP ’bgn- (BMP LMYTWN-) ‘to throw away’ || (+ *pari-) MMP prgn-, 
BMP plkn- /pargan-/ ‘to scatter, sow’ || (+ *fra-) BMP plkn- /fragan-/ ‘to throw, lay 
(the foundations)’ || (+ *ui-) MMP gwg’n-, BMP gwk’n- /gugän-/ ‘to destroy’ 
c DMMPP: 206a, 10b, 278b, 166b 
Partic.: perf. pass. MMP qnd; Pass.: pres. IND. 3pl. MMP qnyyhynd || (^ *apa-) Pres.: IND. 3sg. MMP 
“’bgnyd, 3р1. MMP ’bgnynd, SUBJ. 3sg. MMP "bond 3р1. MMP *’bgn’nd, IMPV. 2р1. MMP ’bgnyd; 
Partic.: perf. pass. MMP ’bgnd || (+ *pari-) Pres.: IND. 3sg. BMP plknyt /parganéd/, 3pl. BMP plknynd 
/parganénd/, SUBJ. 3sg. ? MMP prgn’d; Partic.: perf. pass. BMP plgndk /pargandag/, BMP plknd 
/pargand/ || (+ *fra-) Partic.: perf. pass. BMP plknd /fragand/ || (+ *ui-) Pres.: IND. 3sg. MMP gwg’nyd, 
SUBJ. 3sg. BMP gwk’n’t/guganad/; Partic.: perf. pass. MMP gwgndg
```


## [2026-09-06T15:43:15.115Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KNT kanpa/cam ===\"; grep -n \"kanpa\\|kamp\\|čam\\|cam-\" KNT.txt | head -20; echo \"=== PHD ===\"; grep -n \"kamar\\|xamb\\|xam \\|cam \\|camisn\" PHD.txt | head -30"
}
```


### [2026-09-06T15:43:15.216Z] TOOL RESULT

```
=== KNT kanpa/cam ===
=== PHD ===
424:kaman [kin’n' | = M, N ~] bow. 5; 7 ~dar [-d'] | N ~] archer, bowman. ha er mae 4 ba kamar [kml | N —] waist; belt, girdle. ~-band [-bnd | N ~] belt. kāmģār [Emil | P k?*mg?*r, N ~] powerful, absolute. kamist [Amyst'] least. —jh: pad ~ih, at least. kāmistan, kām- [YCBEN-stn' < A ysbh, V shh; k*m-(y)stnt M k*m-yst] want, desire. kám|-rawág [km izvb*k! | N ~rawa] successful. ~-Z1(w)isn [-zywsn'] free, independent. kam-zór [kmzwl | N ~] weak. ~ih: weakness. kan-, v. kandan, kanar [kwl | N ~] side, edge; embrace. ~ag [-k' | M kr?rg, N ~a] edge, limit, boundary. --agómand [-k’wmnd | M -gwmnd] limited, finite. kandan, kan- [HPLWN-tn! < А V hpr; kn-dn', -tn! | M knd, N ~] dig; raze, destroy. kanig [knyk! | M knyg] girl, maid. kanizag [knyck! | M knycg, N kaniz(ak)] — kanig. kantigr [kntgl] quiver. kāpūr [ро | Ar. kāfūr] camphor. kar-, v. kardan. 1Kar [21 | M Pr, N ~] work, deed, affair. ~ framüdan: put to use. 2kàr [%'7], pl. —àn: (other) people. зкаг [%'/] butter. kār-, v. kištan. karafs [klips | N ~] celery. kār-āgāh [РА | N ~] skilled, experienced. ~ih: skill, experience. karak [krk! | N ~] quail. karan [kľn' | P bein, N ~] side, edge, end, limit. kārawān [%?/zv?x! | P k*rw'n, N kārwān] caravan, military column. ~ig [-yk! | N ~7] caravaneer, traveller. karb [klp] priest hostile to Zoroaster. karbāš [5/0 | N karbas, etc.] lizard. karbunag [k/pnk!, klbnk'] lizard. kard [krt! | M kyrd, N ~] action; matter, affair. кага [SK YN A < A skyn’; Kit! | N ~] knife. ikardag [kltk!] division, section, portion. *kardag [krtk!, kltk! | N karda] action. kārdāg [k'/d?k'] traveller, wanderer, migrant. kardaģān [Art-, Rlt&?n! | M kyrdg”n) action. kardagàár [Artk?l | M kyrdg’r, № ~] mighty. C 6084 E
976:belt kamar(-band).
2102:girdle kamar; sacred ~ ēbyānghan, kustig.
4247:waist kamar.
4987:kardagān 1%kardāg kam kamāndār kamān kamāl kamālīg kamistīh ‘kamist kamzor kamzorih kamar kamarband maygt arz! kastār kastärīh kchtar kaf
```


## [2026-09-06T15:43:17.237Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== MON kamra ===\"; grep -n \"کمرا\" MON_part1.txt MON_part2.txt | head -5; echo \"=== MON kabare ===\"; grep -n \"کاباره\" MON_part1.txt MON_part2.txt | head -5; echo \"=== MON shampayn ===\"; grep -n \"شامپاین\\|شامپان\" MON_part1.txt MON_part2.txt | head -5; echo \"=== MON qapan ===\"; grep -n \"قپان\\|کپان\" MON_part1.txt MON_part2.txt | head -8"
}
```


### [2026-09-06T15:43:17.406Z] TOOL RESULT

```
=== MON kamra ===
MON_part1.txt:11350:حاکم؛ حکمران. ضح.- در عهد ساسانی این 
MON_part1.txt:40665:چیزی برای فریب و کمراهی دیکران. 1 
MON_part1.txt:41641:رفستن» راه را کج کردن. کمراه شدن» 
MON_part2.txt:3192:سدن» کمراه کشت . (اسص. که هت 
MON_part2.txt:3490:ی ۷ |ع:] امطل.) کمراه شین هن ا: 
=== MON kabare ===
MON_part2.txt:16802:کاباره: 02:0 (.) میکده. میخانه؛ 
=== MON shampayn ===
MON_part2.txt:75910:قبل گوریل» شامپانز ه» اورانگو تان» زیون و 
MON_part1.txt:83153:شامپانی: ««قمستة (.) نوعی شراب سفید 
MON_part1.txt:83154:کف‌دار گرانبها که آن را اصلا در «شامپانی» 
=== MON qapan ===
MON_part2.txt:11135:قسبان: 7:۰2 [سعر. کپان - قهان] (ا.) 
MON_part2.txt:20406:کپان: ۱۵۲)0(2۰ [- معر. قبان - متر. قپان] 
MON_part2.txt:71949:سنگ کپان. قبه و گویی که از فلز یراق مانند 
MON_part2.txt:71952:جایی آويخته باشند نظیر نار کپان (- قپان)
```


## [2026-09-06T15:43:26.197Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== qabban ===\"; sed -n '11130,11140p' MON_part2.txt; echo \"=== kapan ===\"; sed -n '20400,20412p' MON_part2.txt; echo \"=== kabare ===\"; sed -n '16798,16808p' MON_part2.txt; echo \"=== shampani ===\"; sed -n '83150,83160p' MON_part1.txt"
}
```


### [2026-09-06T15:43:26.294Z] TOOL RESULT

```
=== qabban ===

قسباله‌نویس: ۰-۷5 [ع. ف. - 
قباله نویسنده | (ص‌فا.) آنکه قباله نویسد؛ 
چک‌نوس» صکاککك. 

قسبان: 7:۰2 [سعر. کپان - قهان] (ا.) 
ترازویی که دارای یکت بله باشد؛ قیان. 
قانمد: 1 [ع. ف.| (امسر.) 
بالا یوش نمدی» بارانی نمدین. 

فبج: لجادر ,91 [معر. کبک ] (.) (جان.) 
=== kapan ===
فراوان می‌رو بد. 

کب آمدن.: 2۲0 (مص‌ل.) اختم: 0( 
و ات هام اهق بح یلار 
(یکی بود یکی نبود. چا. ۱۴۸:۲.) 

کپان: ۱۵۲)0(2۰ [- معر. قبان - متر. قپان] 
0( ترازو یی که یکت بله دارد و بجای بله 
دیگر سنگ از شاهین آن آویزند؛ قیان. 
کیر: ۲ (.) خانة نیی» کومه» آلونکد» 
عریش. 

کیره: (۵-)2۵۲۵ ۵ [ - - کبره] (ا.) (عم.) چرکی 
=== kabare ===
بدین مناسبت است که تشکیلات کائولن در 
چین و زاین زیاد است و اول دفعه استفاده از 
خاک چینی جهت ساختن ظروف در 
مملکت چین انجام شده است؛ خاک چینی» 
کاباره: 02:0 (.) میکده. میخانه؛ 
مشروب‌فروشی. 

کابل: ا (.) مفتول فلزی لفاف‌دار و سیم 
زیرزمینی یا زیردریایی که جهت برق و تلفن 
وتلگراف‌بکا رآید. 

=== shampani ===
صدره درلکث. 
شاما کی: -820031 (ص‌نسب. امر.) سینه‌بند 
زنان. 
شامپانی: ««قمستة (.) نوعی شراب سفید 
کف‌دار گرانبها که آن را اصلا در «شامپانی» 
(فرانسه) از بهترین اقسام انگور تهیه کنند. 
شامیو: 0 (ا.) نوعی صابون مایع که 
برای شستن و تمیز کردن و براق ساختن موی 
مر استعمال هو در 
شامپیون: (ص.) یهلوان» 
قهرمان. ضح.- احتراز از استعمال اين کلم
```


## [2026-09-06T15:43:50.205Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; ls incoming/BQT/; echo; head -c 400 incoming/BQT/BQT_v3_pages.txt; echo; grep -c \"pdf page\" incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt BQT_v2_pages.txt 2>/dev/null"
}
```


### [2026-09-06T15:43:50.260Z] TOOL RESULT

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

[pdf page 1]
[NOT OCRED - use tools/ref_page.py]
[pdf page 2]
7
Ub
sits k ge
AS ۱۰۶۲ ‏نتف‌بال‎
‏ومع‎ ‘oo ‏داي و‎ el Oe

far
en rotons ‘ ‘ ths ۰ ‏دیهان‎
‎۳ 2 7
۰ SF Ps
On Awe
۰
‏-ل‎ 9 ‘il
۱۳۴۳ ‏چاپ دوم فروردین‎
‏با تجدید نظر کامل‎
‏بسرمایه کتاپفروشی ابن سینا- تهران‎

|

incoming/BQT/BQT_v4_pages.txt:553
BQT_v2_pages.txt:0
incoming/BQT/BQT_v3_pages.txt:721
```


## [2026-09-06T15:43:51.323Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1)[:3000])\""
}
```


### [2026-09-06T15:43:54.042Z] TOOL RESULT

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
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT
```


## [2026-09-06T15:43:58.499Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,60p' tools/ref_page.py"
}
```


### [2026-09-06T15:43:58.535Z] TOOL RESULT

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


## [2026-09-06T15:44:00.898Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 600 python3 tools/ref_page.py BQT:1694 --image 2>&1 | tail -60"
}
```


### [2026-09-06T15:44:08.135Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1694.png
REF: BQT:1694  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 487  OCR-lang: fas

کمچه -۱۹۹۶-
پیرسالخورده وفرتوت راکوبند ‎٩‏ . کمر بفتح اول واثانی و اسکون
کمچه ؟ - بروزن چمچه : بلفت‌زند | رای قرشت . معروفت که میان باشد۹ -وآنچه
و پازند ملخ راکوبند و بعربی جرادخوانند. آنرا یکدور برمیان بندند از ابربشم و زرونقره
کمخا ؟ - بکر اول وخای نتلهرار | مانند حلقه وطوقی۹ - ومیانة کوه را نی زکوبند
بالف کشیده , جامهٌ منقشی را کوبند که بالوان که کم رکوه باشد ۷ - و بمعنی بلند هم آمده
مختلف بافته باشند - وبفتح‌اول هم گفته‌اندبمه‌نی است۷ .
جامه منقش بکرنگه . گمر | - بر وزن صحرا » محوطه‌ای را
کمخاب ۴ ه بکر اول بر وزن | کوبند که شبپا چهار پایان و ستورانرا در آن
گرداب » بمعنی کمضا است که جامةٌ منقش‌الوان | کنند ۸ ؛ و پاینممنی‌باکاف فارسی‌هم آمده‌است
باشد » و بفتح اول هم‌آمده است - وجامهمنقش | - و طاق بلندبرا نیز کوبند مانند طاق درگاه
یکرنگه را نیز کفته‌اند . سلاطین و امرا و دیوار بلند را هم کفته‌اند ‎٩‏
‏کمخن " ام اول‌وقتح‌انی‌وسکون و زلار ی که آمتان زردشت برمیان‌می‌بسته‌اند*۹.
خای لغذ وتای قرشت » بلغت زند وپازندبمعنی کمر آفتاب - خطی که بر مرکز
آميخته ودرهم باشد . : آقاب کنرد همجو محورودایره - ودرمو بدالفلا
۱ - بودکمپیری نود سالهٌکلان پر تشنج روی ورنگش زعفران...
« مولوی بلخی. مثنوی چاپ علاءالدوله ص6۸۱
۴ - هز, ۲۵۵2 , .3۳8(8 ( ملخ ) « پونکر ص ۱۱۳ ۰
۴ کمغاد * کمخاب (۸.م.) . «اسح بفتح‌کاف است مخفف کمخاد بمنی خواب کم
دارد .» ۶ رشیدی ». ۴ کمغاو ۶ رشیدی : کمضا» « فرهنگه نظام ».
8 - مسحف «کیخت» ‏ کمیخت ( بدآميخته ) . رك :کمیز »کمیخت .
- پهلوی 2738۴ (کمربند ).اوستا -1۳880272 (کمربند ) » کردی ع ۳6126۲(
(کمربند ) . افقانی 1۳81387 , استی‌ع 1۳270۵۲1 ( کمربند زنانه ) « اسشق ۸۹۹« لیب رکه
س ۹ ۷ - پپلوی ۴۵۳۵۶ ( 52۳81 ) ۰ اوستابی 866۳۵۵2 ( سر )
« اسشق - هوبشمان ‎۸٩۷‏ » هویشمان ( ایضا ) کوید : ره اي نکلمه واضح نیت . ر4: کمرا.
۸ - چوگر که ظلم را کشتی بزور بازوی عدلت
ز البوهی شدء صحرای اقلیم تو چون کمرا ۰
۱ عمعق بخاری « رشیدی ؟ .
‎٩‏ - در اوراق مانوی ( پپلوی ) ۹137 ( طاق " کنید ) » پودانی ۴۵۲4۲۵ ۰ آرمنی
5۶7 فارسی ( ازآرامی ) ۴۵۲8۲2 . رك : هوبشمان » دستور ارمنی ص ۱۹۶ ۰
(84. 1۰0 ,12 ,3505 ری ۲۵۵۵ 1114406 اه انز خ , وعنف۲۲)
گهی ازگردش کیوان بگردون برزند کله گهی ا زکردشگردون بکیوان بربر دکمرا.
آزرقی هروی « رشیدی؟ .
۶ ۳2378 باین هعنی مستعار از آرامی است وآرامی خود ا زكلمهٌ «کمر» فارسی
مأخوذ است » قی : 328881588 ۶ اسقا ۲:۱ ص ‎٩‏ »
چون توکمر جنگه پبندی ملك روم کمرای یبرد » بهرستند کم تو .
قطران تبریزی « رشیدی .
```


## [2026-09-06T15:44:37.478Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'].get('scans'),ensure_ascii=False,indent=1))\"; echo \"=== v2 leaves ===\"; awk 'BEGIN{RS=\"\\f\"}END{print NR}' data/verification/sources/refs/BQT_v2_pages.txt"
}
```


### [2026-09-06T15:44:39.032Z] TOOL RESULT

```
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
=== v2 leaves ===
683
```


## [2026-09-06T15:44:44.549Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"}{n++; if ($0 ~ /۶۲۰/) print \"leaf\",n}' BQT_v2_pages.txt | head; echo \"--- search chap\"; awk 'BEGIN{RS=\"\\f\"}{n++; if ($0 ~ /چپه/) print \"leaf\",n}' BQT_v2_pages.txt | head"
}
```


### [2026-09-06T15:44:46.028Z] TOOL RESULT

```
--- search chap
```


## [2026-09-06T15:44:49.134Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==75' BQT_v2_pages.txt | head -40; echo \"=== size ===\"; wc -c BQT_v2_pages.txt BQT_v1_pages.txt"
}
```


### [2026-09-06T15:44:51.089Z] TOOL RESULT

```
   ‫‪۱‬‬                                                                                           ‫چامن‬



‫‌ای بود هربع و طولانی که مکی‬
                           ‫انرکاهغذ‬
                                  ‫پآ‬‫‪۱‬و‬                            ‫باشد ‪ -‬وغابط را نیزکوبند ‪٩‬‏ ‪.‬‬
‫چنگری نام خود را بر آن نفش‬        ‫از بادشاهان‬
                                                 ‫جافه ه بر وزن شانه ‪,‬فك اسفل باشد ‪۱‬‬
 ‫کرده بودورایج گردانیده چ‪٠‬و‏ن‌مردم ذربایجان‬        ‫ونرا‬
                                                      ‫که موضع رش برآوردن و غبغب است آ‬
‫حربی ذقن گوبند ‪ - ۴‬وکلولةً خمیری که يك | و اهل تبریز قبول نکردند و عزالدین مظفر که‬
‫! که باعث و بانی چاو بودبقتل امد ؛ رسم چاو‬     ‫سخن‬    ‫وابه‬
                                                         ‫‌وکن‬‫ف‪- ۴‬‬ ‫رشود‬‫حته‬
                                                                        ‫زن بخ‬
                                                                            ‫اازآ‬
                                                                               ‫نان‬
 ‫| بط ف شد ؛ و باجيم ابجد هم بنظرامده‌است‬                                                  ‫هم مت ؟ ‪.‬‬
       ‫سسس‬                                   ‫ل‬   ‫‪.‬ل‬      ‫لے ل‬   ‫تست ت‬       ‫س‬     ‫س‬   ‫ِِ‬



                        ‫‪.‬‬   ‫‪ - ۴‬بهر دومعنی درتهران ‪68۱۱‬‬                 ‫‪.‬‬       ‫م‪:‬دن‬
                                                                                   ‫چارك‬
                                                                                      ‫‪۱‬‬
             ‫*شاعر گوید ‪:‬‬   ‫د‬
                            ‫و)‬‫بثور‬
                                 ‫اسدی گوید ‪« :‬چانه »سخن منش (ظ‪ .‬سخن من‬                     ‫‪۴‬‬
                 ‫گاه چامه سرود و که چانه ‪.‬‬             ‫مشبكانروز اندر آن خانه‬
       ‫«لغت فری‪٩. ۸۰۵‬‏‬
                            ‫وچاته زدن بمعنی گفتگو با فروشنده دربار؛ بای چیزی‌است‪.‬‬
   ‫‪« ۴‬چاو» لفتی‌است چینی(درچینی‪ [03"6‬رك‪. 065 :‬ص‪[acinarI_oniS,refuaL.‬‏‬
   ‫و ازآنجا درزمان سلطنت گیخانوخان پادشاه مفولی ابران ( ‪ ) . ۰۹۹-۹۱‬بابران وارد شد‬
  ‫شخصی‌بنام عزالدین‌محمد بن‌مظفرین‌عمید که از‬      ‫د‪.‬‬
                                                    ‫یالی‬
                                                       ‫دت خ‬
                                                          ‫رملک‬
                                                             ‫گان‌ه‬
                                                                 ‫چه در زمان این‌یادشاءه خز‬
  ‫اوضاع چين و ممالك قاآلی اطلاعاتی داشت خود را صدر حپان زنجانی ( وزير ) نزديك کرد‬
=== size ===
4339896 BQT_v2_pages.txt
2247721 BQT_v1_pages.txt
6587617 total
```


## [2026-09-06T15:44:58.185Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for w in چپ چفته چمیدن چنبر خم; do echo \"== $w\"; awk -v W=\"$w\" 'BEGIN{RS=\"\\f\"}{n++; if (index($0,W)) printf \"leaf %d\\n\", n}' BQT_v2_pages.txt | head -8; done"
}
```


### [2026-09-06T15:45:01.538Z] TOOL RESULT

```
== چپ
leaf 4
leaf 6
leaf 23
leaf 31
leaf 32
leaf 34
leaf 39
leaf 40
== چفته
leaf 37
leaf 106
leaf 262
leaf 407
== چمیدن
leaf 116
leaf 117
leaf 118
leaf 119
leaf 120
== چنبر
leaf 121
leaf 199
leaf 229
leaf 261
leaf 330
leaf 373
== خم
leaf 12
leaf 13
leaf 18
leaf 22
leaf 24
leaf 26
leaf 31
leaf 36
```


## [2026-09-06T15:45:07.819Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for L in 75 80 85 90 116 121; do echo \"=== leaf $L ===\"; awk -v L=$L 'BEGIN{RS=\"\\f\"} NR==L' BQT_v2_pages.txt | head -6; done"
}
```


### [2026-09-06T15:45:09.903Z] TOOL RESULT

```
=== leaf 75 ===
   ‫‪۱‬‬                                                                                           ‫چامن‬



‫‌ای بود هربع و طولانی که مکی‬
                           ‫انرکاهغذ‬
=== leaf 80 ===
 ‫یه‬                                                                                     ‫‪14‬‬


‫با کسی خود را یکی‬         ‫بچسبانشد ‪-‬‬     ‫بچیزی‬    ‫چیدار = با زای هوز بروزن مقراض »‬
                                                  ‫سر موزه راگوبند » وکآفنشی باشدکه مردم‬
                                                  ‫ماوراء النهر از بالای موزه پوشنده ؛ و با رای‬
=== leaf 85 ===
                                           ‫بیان هشتم‬
           ‫جیم فارسی با رایقرشت مشتمل بر نود لغت و کنایت‬                            ‫در‬

                                                      ‫چر = بضماول وسکون‌ثانی» تآلنتاسلرا‬
                        ‫وبعربی مشکوة خوانند ‪.‬‬
  ‫جر احور = با واو معدوله بر وزن‬                    ‫کویند‪ - ۱‬وبفتح اول‌نفمه وغناباشد چه چر کر‬
=== leaf 90 ===
   ‫رده‬                                                                                                           ‫‪- ۳۱‬‬
           ‫وآنچه زان بدان ریسمان رسند ‪۷‬‬                          ‫وزن ومعنی‌چرخست باشد وآن چرخی وحوضی‬
                                                             ‫باشد که انگور درآن ریزند و بمالند تاشیرءآن‬
                                                                                                                      ‫بر ید ‪٠‬‏‬
                ‫‪۰‬‬       ‫وفلك اولخسوا‬       ‫باشد نوفا ‌‬

=== leaf 116 ===
                                                                                              ‫‪۳‬ی‬
                                                                                               ‫—~ ‪۷‬‬


‫کفته‌اند ‪ -‬و کنایه ار زلف ممشوق حم هت ‪.‬‬            ‫براهمه و نود ازطلاا و نقره و امثال آن سازد‬

=== leaf 121 ===
          ‫که‬                                                                               ‫چنائبن‬

 ‫جنیر مینا ک=نابه ازآسمانات ‪. ۱‬‬                      ‫چنا نھن ‪ -‬بفتح اول وئانی بالف کشیده‬
‫جنيك ‪ .‬بضم اول بروزن اردك » خیز‬                      ‫و بنون زده وهای مفتوح ولون دیگر ساکن ‪۰‬‬
‫کردن و جتن را گوبند ‪ - ۷‬و بمعتی سنگه‬                 ‫ابن (‪)١‬کلمة‏ تحین‌است بمعنیآفرمنوباركاهد‪,‬‬
 ‫و بدودالی مقناطیس‬      ‫آهن ربا هم آمده است‬           ‫که همه لیکیها درضمن آن هت بعنی وصف‬
```


## [2026-09-06T15:45:22.639Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for L in 76 77 78; do echo \"=== leaf $L ===\"; awk -v L=$L 'BEGIN{RS=\"\\f\"} NR==L' BQT_v2_pages.txt | head -25; done"
}
```


### [2026-09-06T15:45:24.418Z] TOOL RESULT

```
=== leaf 76 ===
  ‫چاه‬                                                                                                ‫سلا‬
                      ‫‪۰ 1‬‬    ‫وناهموار نیزآمده است‬                                         ‫‪١‬‏‬   ‫واول اصح است‬


 ‫چاو لی ته بسکون ثالث بروزن‌کاولی »‬                         ‫چاو چاو ‪ = .‬با جيم فارسی بورزن‬
‫چیزی باشد پهن که ازنی بوربا و امتالآن بافند‬                ‫کاوکاو » شور وغوغا وصدا ‪ -‬و بانگ كنجعك را‬
            ‫‪۰‬‬   ‫تاباك شود‬    ‫سقشانند‬   ‫وغله را بدان‬        ‫روده باشد‬
                                                                   ‫کا‬‫گویند وقتکه جانوری‌فصد گرفتنع‬

 ‫= بروزن پایوش؛ قب‬               ‫جاووش‬
                                                           ‫کی وس شان او که که مه او را‬
                            ‫لشکر وفافله را گویند ‪۳‬‬
                                                                                               ‫برآورد ‪۶. ۴‬‬
                                                                                               ‫چاوك‬
 ‫چاو يدن * = بروزن‌کاودن» قرباد‬                            ‫دروزن تاو گ‪«.‬خفف جکاو ك‬   ‫گ‬


‫کردن کذجشک باشد وقتبکه دست برآشدانة او‬                      ‫است وآن مرغی باشد برابر بگنجشک و بعربی‬
‫و بطرىق استماره بانك کردن سار "‬          ‫وراز کنند _‬   ‫‪۱‬‬                                        ‫قبره خوانند ‪.‬‬
                                                       ‫‪۱‬‬

                      ‫حوانات و انانرا گوند ‪.‬‬
                                         ‫جاه‬
                                                       ‫ی ولام » نکالمی‌باشد ‪۱‬‬                         ‫‪5‬‬
        ‫ا‬        ‫ام‬
=== leaf 77 ===
 ‫‏‪ ٩‬مس‬                                                                                                            ‫چاءآبی کنود‬
 ‫کنابه از دنا باشد =‬                 ‫چاه دلو د‬                             ‫وجریی بشرخوانند ‪٩‬‏ ‪ -‬وکوی زنخدان خوبانرا‬
‫کونابه از برح دلوهم هت که یکی از دوازده‬                                                              ‫نیزجطریق استماره گفتماند ‪-‬‬
                                       ‫‪۹‬‬   ‫فلکی است‬          ‫ردج‬
                                                                           ‫‪ - ۴‬بااف و ون ‪.‬‬                 ‫وید‬
                                                                                                             ‫نی‬‫که]‬
                                                                                                                 ‫جا‬
‫جاه ظلما نی ‌ کنابه ازدلیا وقالب‬
                                                                           ‫چامی است در طرابلی که ھر کس آب از آن‬
                                                  ‫‪۰‬‬   ‫آدمی ات‬
                                                                          ‫چاه بغورداحمق کردد » واين مثل است ؛ وآ یی‬
‫چاهی‌است که ابن‌مفنع‬                 ‫جاه هعنع‬                              ‫کبود حم بنظر آمده است که بجای نون بای‬

‫بعلم سحرازآ نجاماهی برمیآورد که چهارفرسخ‬                                                                               ‫ایسد باشد‪.‬‬
                                                                           ‫چاه يست = برکاك وفتح‌بای‌فارسی»‬
‫= بفتح ثالث ‪ ,‬گوی عمیق چاه‬                  ‫جاهه‪۱‬‬
                                                                                                  ‫کتابه ادزتا باشد ‪-‬‬
                                           ‫م‌انند را گونشت ‪۰‬‬
                                                                           ‫با بای فارسی بروزن خام‬           ‫چاه پور ‪۴‬‬
‫در‬       ‫و آن‬    ‫اس‬   ‫جاه ہو سف ‪ -‬مشپور‬


                                                                          ‫اقتد برآرند ؛ و بجای بای قارسی بای حطی نیز‬
                                                            ‫باشثد ‪.‬‬

=== leaf 78 ===
                                         ‫بیان دوم‬

                ‫ایرمسی با بای ابجد مشتمل برشش لغت‬
                                                ‫دفر ج‬
 ‫چبلوس» با لام بر رزن افوس ‪۰‬‬                    ‫چیشی = بر وزن رفتن » انبانجه را‬
‫مخفف چاپلوی امت که چرب زبان و فربنده‬            ‫کوند ؛ وبجای ای قرش تت بای حطی همآمده‬
                                    ‫باشد ‪. ۴‬‬                                              ‫امت ‪١‬‏ ‪.‬‬
 ‫جبیر ‪ = 6۵‬بر وزن کبیره » بمعنی جمم‬             ‫چبعت » بفتح اول وسکون انی و ضم‬
 ‫وجمعیت‌سپاء ومردم‌باشد‪ -‬وجمم گردیده وساخته‬      ‫‪-‬‬   ‫» نهالی و لحاف‬     ‫وفوقانی ساکن‬   ‫غین نقطه دار‬


                          ‫شده را نگیوزبند ‪.‬‬     ‫وسوزنی ‪ -‬وجامه ‪ -‬و هرچیز پنبه دارکهکهنه‬
                                                                ‫واز هم داشیده باشد ‪۴‬‬   ‫ومندرس شده‬
‫چیین " » بفتح اول توشدید ثالی بر‬
‫وزن شب ین » طبقی را کویند کهاز چوب ید‬            ‫چبغوت ‪ -‬بورزن مبیوت » بععنی‬
 ‫بافته باشند؛ وباین معنی بطم اول هم مده است؛‬    ‫و کپنه لحاف باره باره‬      ‫است که جامه _‬      ‫چبغت‬

                 ‫و بابای فارسی نیز کفته‌اند ‪.‬‬                                             ‫باشد ‪. ۴‬‬




   ‫‪ ۴‬رك چ‪:‬بغوت » جبغوت‪..‬‬              ‫مصحف چسن («‪.‬م‪ ).‬رك‪ :‬چپین و جدئین ‪.‬‬               ‫ظ؛‬
   ‫ب ‪ -‬طبری ‪Îpac‬‏ (سہد)(بز ر که‬           ‫رك‪ :‬چایلوس‪.‬‬   ‫‪-‬‬   ‫ی‬      ‫‪ - ۴‬رك ‪ :‬چفت »حدغوت‪.‬‬
```


## [2026-09-06T15:45:34.408Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"}{n++; if(n>=60 && n<=130){ line=\"\"; split($0,a,\"\\n\"); for(i=1;i<=6;i++){ if(a[i] ~ /[۰-۹]{3}/) {print n\": \"a[i]} } }}' BQT_v2_pages.txt | head -40"
}
```


### [2026-09-06T15:45:36.552Z] TOOL RESULT

```
60:                                                                                  ‫‪۱‬‬    ‫ات‬    ‫گنستك‬
61: ‫هورك از سنگهای نفسه همچو المای وباقوت‬                    ‫‪ = ۱‬بفتح اول وسکون ثانی‬         ‫جومت‬
61: ‫ولمل وامثال آن‌باشد ‪ -‬وموح چوب واستخوانرا‬                 ‫ومیم صکور بین بی‌نقطه وتای قرشت‌زده (‪)۱‬‬
61:  ‫ونابه از مردم زشید وصاحب‬
62:               ‫جیم ابجد با های هوز مشتمل بر پانزده لغت و کنات‬                          ‫در‬
62: ‫جود داز‬           ‫جهان !رای ا‬                        ‫= بکر اول و سکون انی »‬            ‫جه‬
62:                                                      ‫بلغت زند پوازند (‪ » )۱‬زئن فاحشه و بدکاره را‬
62: ‫‪-‬‬     ‫وکنابه ازفرزند هم حت‬    ‫عین خوانند ‪- ۴‬‬          ‫جهاد اصغر ‪ - ۴‬کنابه امقزابله‬
63:  ‫و میم مفتوح برای بی‌نقطه و زای نقطه دارزده‪.‬‬      ‫»‬     ‫واف‬
64:                                           ‫بیان پیستم‬
64:                ‫درجیم ابجد بابای حطی مشتمل برهجده (‪ )۱‬لغت‬
64: ‫چیر ه د بر وزن زیره » روزباله باشد‪,‬‬                     ‫جی = بکسر اول وسکون ثانی » ولات‬
64: ‫وآن چیزی بود ازکندم وآرد و نان وامثال آن‬               ‫صفاهان را گویند عموما ‪ -‬وبلوکی از بلوکات‬
64:           ‫که بجپت غلام و لوکرمقرر کنند ‪.‬‬                ‫آنرا خصوصا ‪ - ۱‬ویفتح اول دهی است ازولات‬
64: ‫جیز جنگ ‪ _ .‬باجیم وزای‌هوزبروزن‬                        ‫بز‪-‬بان زد وپازند(‪ )۲‬بمعنی پاكویاکیزه‬
65:                                                                                      ‫جیغوت‬
65: ‫وبعربی زیبق خوانند ‪ . ۵‬طبیمت آن گرم باشد‬                    ‫جیقوت بسر وزن فرتوت ت»وبره‬
65: ‫و پسنی گوند سرد و تر است در دویم » شیش‬
65:                                                               ‫و سبدیرا کوبند که ازلیف خرما بافند ‪. ۱‬‬
66:                                   ‫گفتار ششم‬
66:      ‫تبجی‬            ‫رب‬
66:                    ‫واف‬   ‫از کاب پرهان قاطع درحرف جیم فار‬
66:                        ‫حسی‬
66:         ‫هبتتی بربيست و دو بیان و محتوی بر ششصد و سیزده‬
67:                                                                                                                 ‫چاپلوی‬
67:  ‫جداگردیده را بکیوزبند ‪ ۵‬و آنرا بعریی صبره‬        ‫را یز کون دکه اکر‬                   ‫اسب رهواری‬               ‫و‬   ‫باشد =‬
67:                       ‫خوالند بضم صاد بی‌نقطه ‪.‬‬               ‫را غلط نکند ‪# ۱‬‬                     ‫راه‬
67:                                                                                                    ‫ننهن پدراو‬
68:  ‫چار تاره‬                                                                                 ‫—‬        ‫س‬
69:     ‫سس‬                                                                                             ‫چار تکبیرزدن‬
69: ‫چار دیو ار صمرذات؟ ‪ -‬وکنابه‬                                                                        ‫‪١‬‏ ‪.‬‬       ‫هم هت‬
69:                     ‫‪. °‬‬    ‫از چهار حد دنا هم هت‬             ‫کنایه از ترك‬            ‫چار تکبیرردن ‏‬
69: ‫جار دیو‌ار نف« کنانه از دلبا ‪-‬‬                             ‫کلی کردنوتبرای مطلق ازماوی نمودن‌باشد ‪.۴‬‬
69:                           ‫وقالب وجد ادمی باشد ‪.‬‬            ‫و کناه از نماز جذازه هم هت که بعد از آن‬
70:  ‫چاره‬                                                                                                                         ‫‪۱۱‬ات‬
70:                                            ‫است ‪. 4‬‬          ‫دورهند‪ .‬راوتی گوبند ‪ - ۷‬و خیمة مطبخ رالیز‬
70:                                                                     ‫و کنابه از عناصر ارعه باشد ‪۰‬‬                             ‫کفته‌اید ‪۴‬‬
70: ‫چار مبخ = معروف است» و آن‌چنان‬
70: ‫باشد که شخصی را خواهند شکذجه کنند بریشت‬                         ‫جنم رای بی نقطه وسکون‬              ‫‪» ۳‬‬               ‫چارع‬
71:   ‫=“‬                                                                                                        ‫چاريك‬
```


## [2026-09-06T15:45:47.655Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for L in 79 117 120; do echo \"=== leaf $L (p.$((L+541))) ===\"; awk -v L=$L 'BEGIN{RS=\"\\f\"} NR==L' BQT_v2_pages.txt | head -35; done"
}
```


### [2026-09-06T15:45:49.255Z] TOOL RESULT

```
=== leaf 79 (p.620) ===
                                                          ‫بیان سوم‬
             ‫ونات‬
                ‫در جیم فارسی با بای فارسی مشتمل بر بیست و دو لغت ک‬
 ‫چپا نی ‪ = ۴‬بروژن ادانی (‪ » )۱‬مردم‬                                  ‫بقتح‌اول وسکون‌انی» هعر وف‬   ‫‪ ۱‬س‬       ‫چپ‬

‫بی‌سرویا کوهنه پوش راکوبند ؛ وباتشدید ثائی‬
                                      ‫‪2‬‬    ‫همآمده اس‬                                ‫وویندگی را نز کویند ‪#.‬‬
                                                                                                         ‫گ‬
 ‫‪ °‬ه باجیم فارسی بروزن‬                 ‫حیچاپ‬                        ‫چیات ‪ -‬بفتح‌اول بروزن تبات طیانچهرا‬
‫دوسه را‬      ‫و‬   ‫برسه راگوبند‪.‬‬   ‫واواز‬     ‫صدا‬   ‫کشکاب»‬                     ‫گوبند ؛ و با تشد‪.‬د انی همکفته‌اند ‪.‬‬

                                 ‫بعربی فبله خوانند ‪.‬‬               ‫چیا تی بروزن‌نبانی » مخفف چاپانی‬
‫چیجله ‏ بروزن مرحله ز»مین پر(‪)۷‬‬                                    ‫بشدرکرهوی تابه‬
                                                                                ‫است که نان تشک فطبر با‬
‫آب و کلرا گوبند که پای‌مردم وحیوانات دیگر‬
‫در آن بلغزد ‪ -‬وکوه پارژ نرمی را گوبن دکه‬                            ‫چیار ‏ بر وزن قطار ‪ .‬حرچیز دورنگ‬
      ‫نزد‬
        ‫نن‬‫وخشك‬
             ‫گا ل‬
                ‫و آنر‬                ‫زند‬
                                       ‫طفلان بلرغآن‬                  ‫باشد عموها ‪ -‬و کبوتری سبز که خالهای ساه ‪-‬‬
‫ویمائی را لیز‬
            ‫وبعربی زحلوفه (‪ )۳‬کوبند ‪ -‬ر‬                             ‫و اسبی که نقطه ها و کلهای سیاه باغدر رنگف‬
 ‫کفته‌اند که درایام عید و نوروز وجشنها ازجابی‬                       ‫خودش بر بدن داشته باشد خصوصاً ‪ ۰‬و بعربی‬
‫بباویزند و زنان و دختران برآن نشته در هوا‬                                                       ‫ابرش خواتند ‪-‬‬
 ‫آبند و روند ؛ وباین معتی بجای بای قارسی‌لون‬
                                                                    ‫جاع ؟ ‪ -‬بکسر اول بروزن چراغ »‬
                                     ‫نند ات‬      ‫م طن‬
                                                                    ‫نوعی از ماهی باشد ؛ و بقتح اول هم أمده‬
 ‫= کنابه از فرب ودغا‬             ‫دادن‬       ‫چپ‬                                                                  ‫است ‪.‬‬
 ‫دادن باشد ‪ -‬وترك نمودن و واگذاشتن و طرح‬                           ‫جیان ‪ - ۴‬بروزن کتان ‪ .‬لباس کهنة‬
                                                                    ‫«تدری را گوبند ؛ و باتشدید انی هم هست ‪.‬‬
                                                                                   ‫‌ اوانی‪.‬‬   ‫خم ‪۳‬‬   ‫)‪۱‬‬

                                                                   ‫(‪ )۳‬خم ‪ ۳‬ز‪:‬حلوته ‪ .‬چش‪ :‬زحلوقه ‪.‬‬
=== leaf 117 (p.658) ===
      ‫‪5‬‬
      ‫ی ی‬


 ‫رفتن بناز و خرامسدن بزیبابی کروابند ® یعتی‬                ‫و ضم اول بمعتی لاف زدن و تفاغر کردن باشد‪.‬‬
‫اله‬    ‫و‬     ‫در وقت راه رفتن بهرطرف مبل کند ‪-‬‬               ‫وحیوان را نیز کوند که مطلق جاندار است ‪٩‬‏ ۔‬
                               ‫شراب را نیزگویند ‪.‬‬           ‫وثفل انگوری بداشکه شبرة آبراگرفته باشندب‬
                                                           ‫وسرمای سخت را نکیفزته‌اند ‪ -‬دوانه‌ای باشد‬
‫وسکون نون و جيم بتحتالی رسیده » کوز‪ :‬سر‬                     ‫سياه وشفاف کهدر دارو های چشم بکار پرند ‪-‬‬
                                                            ‫ون چیزی‬  ‫ولزغ راگوبند » آ‬   ‫وبکر اول ج‬
                                                            ‫آبهای ابتاده‬    ‫باشد سز مانند ابرشم که درروی‬
‫جماند ‪۷۲‬س بر وزن رساند * می در‬
                                                                                                            ‫بهمرسد؟ ‪.‬‬
                               ‫‪*#‬‬   ‫‪.‬‬   ‫سر وخرامآورد‬

                                                            ‫چماچم ‪ -‬بفتح اولو جیم فارسی ‪.‬‬
                                                           ‫بر وزن دمادم پشاتیرا گونند و بعربی لاصیه‬
‫و صف کدوی نقاش یکرده را‬             ‫شراب را کویند ‪-‬‬

 ‫گنفیتزه‌اند کهبدان‌شراب خورند ‪ - ۸‬وبضم اول‬                     ‫خوانند ؛ و چم اول و رابع هم آمده است ‪.‬‬
‫بر وزن فلانه ‪ ¢‬بمعنی مطلق حیوان باشد که‬                     ‫چماق ‪ ۲‬س پم اول بروزن براق» گرز‬
                                        ‫حاندار است ‪٩‬‏ ‪۰‬‬     ‫آهنین شش‌بره راگویند‪ .‬ودراین زمان‌چویدست‬
                                                                                         ‫‪2‬‬    ‫ه دار را گوبند ‪۴‬‬     ‫صر‬
 ‫خرامان‬     ‫روائی »‬   ‫پر ورن‬    ‫‪۳‬‬       ‫جمانی‬

                          ‫و صاقی رائیز کوند ‪#*.‬‬            ‫چمان = بقح اول مر وزن روان » راه‬


                    ‫‪ - ۴‬ویز بمعنی تمیز »رک ‪ :‬جم ‪.‬‬           ‫‪ :‬چمانه ‪.‬‬  ‫رک‬  ‫‪۱‬‬

     ‫‪ " ۷۱‬جمقدار؟‪.‬‬     ‫صی‪۲‬ح‪۱‬‬‫کرز ‪« .‬جفتابی ‪« ۹۹۲‬دز‬    ‫یعن‬
                                                       ‫‪ ۴‬از ترکی «چوماق» بم‬
   ‫‪« - ۴‬قتلغ را بگرفتند و یار بزدند " داگاه چماقی برسر اوآمد و کشته شد‪«».‬تجارب‬
   ‫‪ - ۵‬نفتاعلی از چمیدن‌است‬           ‫اللف هندوشاه‪ .‬مصحح اقبال ‪ .‬تهران ‪ ۳۱۳۱‬ص ‪۲۲‬؟‪.‬‬
                                                                              ‫‪:‬‬              ‫نوده‬
=== leaf 120 (p.661) ===
                                                                                                   ‫‪~N‬‬


‫و غمزه و خرام و تکبر براه رفته باشد ‪ -‬و خم‬        ‫چمیلن ‪ = ۱‬بر وزن رسیدن ؛ بمعنی‬
                          ‫شده را نیز گویند ‪.‬‬       ‫خرامان براه رفتن باشد ‪ -‬و بمعنی میل کردن‪-‬‬
                                                       ‫هآممده‬         ‫دن‬
                                                                       ‫رخم‬
                                                                         ‫وو‬‫خپیچ‬
                                                                              ‫و ب رکشتن ‪ -‬و‬
 ‫چهین = بکرومزنن‪.‬مخف‌چامین ‪۲‬‬                                                                            ‫است‬
  ‫است که شاش و بول و غابط را نیز گویند ‪.‬‬           ‫‪3‬‬            ‫‪۳‬‬           ‫‪۳‬‬         ‫‪۲‬‬
                                                   ‫"‪ -‬بروزن رسبده» از روی از‬                ‫چمیكه‬


                                     ‫بیان نور دهم‬
               ‫بر بنجاه لفت و كنات‬              ‫جیم فارسی با نون مشتمل‬                    ‫در‬

  ‫ویای احزنا‬    ‫است ‪ -‬و آنجه زان بر دست‬                ‫چتاب = بروزن‌طتاب ‪,‬کلیچخیمه(‪)۱‬‬
                                 ‫می‌دگار ند ‪۰‬‬       ‫کروابنده وآن نخته‌ای باشد سوراخ‌دارکه‌ستون‬
                                                    ‫و نام رودخانه‌است‬      ‫خنمه رابرآن (‪ )۲‬گذارند ت‬
 ‫جناع د بفتح اول بورزن اباغ * لوعی‬
                               ‫ازماهی باشد ‏‬                               ‫مشهور درولابت پنجاب ‪. ۴‬‬
 ‫چنال بروزن کمال "بمعنی چناراست‬                    ‫جناجن ‪ -‬بقتح اول وجیم فارسی بر‬
                                                            ‫‪۳‬‬                   ‫‪۳۳۹‬‬   ‫[‪)-‬‬          ‫‪۰‬‬




          ‫وآن درختی باشد عظیم وجوهردار ‪۷‬‬            ‫وزن فلاخن ‪۰‬و|از وصدای تبر باشد که بی‌دریی‬
‫چنان‪ -‬بنتح اول بورزن مکان ‪ .‬نام‬                                                                    ‫بندازند ‪.‬‬

 ‫موضعی است ‪ - ۸‬و بمعنی کوشیدن هم هست ‪-‬‬
         ‫وضم اول مخفف چون‌آن وچونان ‪.‬‬
                                                    ‫باشد مشهور ‪ - ۱‬و بمعنی حلقه هم آمده‬
                                  ‫‪ :‬بدان‪.‬‬     ‫)‪ (۱‬چش‬                ‫(‪ )۱‬خم ‪ : ۳‬کلیم خیمه ‪.‬‬
```


## [2026-09-06T15:46:09.172Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"}{n++; if(index($0,\"خمیدن\")) print \"leaf\",n, \"p.\"(n+541)}' BQT_v2_pages.txt | head; echo \"=== leaf 227 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==227' BQT_v2_pages.txt | head -30"
}
```


### [2026-09-06T15:46:11.235Z] TOOL RESULT

```
leaf 227 p.768
leaf 229 p.770
leaf 262 p.803
leaf 342 p.883
=== leaf 227 ===
 ‫~~‬


 ‫وتاحنیتانی‬
          ‫خلیش ‏‪ - ١‬بفتح اول ب‬                         ‫خلس ) = بروزن نفس ‪ ۰‬دوچیز درهم‬
‫رسیده و مشن نقطه دار زده ‪.‬گل و لای درهم‬                ‫آمیخته راگوبند عموماھىجولىل ومروارید(‪)۱‬‬

 ‫آمیختةچبنده راگویند که پای انجزاآبدشواری‬               ‫ومیوة تر وخشك وماش ویرنج وامثال آن ‪ -‬ورش‬
‫جدا شود ‪ - ۴‬وبمعنی دور وآشوب ومشغله هم‬                                    ‫‪۰‬‬    ‫را کوند خصوصا‬       ‫دوموی‬
                                        ‫آففن است‬




                                              ‫بیان شدانهزم‬
               ‫در خای نقطه‌دار بامیم مشتمل برسی و پنج لغت و کنایت‬
‫» نام‬        ‫ورم‬
               ‫عتلغی‬
                   ‫مر ک‬
                      ‫و واو وح‬        ‫‌انیقطه‬
                                            ‫یر‬‫بو‬
                                               ‫"‬         ‫ض‬ ‫ی»‬
                                                            ‫قثانی‬‫نون‬
                                                                   ‫حم ‪ -‬بفتح اول و سک‬
                         ‫نوابی است از موسیقی ‪. ۷‬‬       ‫راست است که کج باشد؟ ‪ -‬وکجی و جفتگی‬
‫خمار = بصم اول بروزن دوچار » نام‬                        ‫چیزها رائیز گونند ‪ ۴‬همچو خریشته‌وطاق ابوان‬
‫بخوه‌روبان‪-‬‬        ‫وختن‌سوب‬    ‫از ملك خا‬    ‫شهر ست‬     ‫ومانند آن ‪ -‬وبه‌عنی جستن و یگخرتن هم مده‬
‫و کلفتی باشد که معد‬        ‫عرربی ملالت و کدورت‬   ‫ودر‬
```


## [2026-09-06T15:46:19.533Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==227' BQT_v2_pages.txt | tail -20; echo \"=== leaf 79 tail (chap footnotes) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==79' BQT_v2_pages.txt | tail -12"
}
```


### [2026-09-06T15:46:21.272Z] TOOL RESULT

```
   ‫از‪:‬‬       ‫راظ‬     ‫‪۴‬‬     ‫‪« _ ۴‬خلش‪ .‬گگنلدیده» «لفت فرس ‪۰ ۹۲۷۰‬‬                ‫‪:‬خلاش‪.‬‬   ‫رك‬     ‫‪۱‬‬


  ‫‪.‬‬       ‫‪.‬یارسی بامتان ‪_ap)n(ak‬‏ ‪« #‬اسقا‪۲ :۱‬م‪۰٦۰‬‏ وخمیدن ازهمن کمه‌ساخته شده‬                 ‫خنب ‪00181‬‬
          ‫‪x‬‏‪nux)kabnu‬‬
                    ‫‪:‬نب « خەب یپلوی ‪ka(b‬‬
                                       ‫‪ ۵9‬از خ‬                         ‫‪ 2 ۴‬خن («م)‪.‬‬
             ‫«اسفا‪۱:۲‬ص ‪۹۵‬و‪ ۷۰‬در اوراق مانوی (پارتی) ‪( ۵/۸0۳5‬کوزه» سبو)‪. ‎‬‬                   ‫‪mu‬‬
                                                                                             ‫اومتا‪abX ‎‬‬
  ‫‪(Henning,‬‬              ‫‪A list of Middle Persian..., BSOS,‬‬            ‫)‪1,۱,۵. 89.‬‬
                                                                         ‫خیم ‪۰‬‬    ‫رك‪:‬‬         ‫‪۹‬‬

            ‫ببانگ شیشم‪ .‬بابانگك افسرسگزی‬                  ‫‪ - ۷‬بگیربادة نوشن ونوش کن بصواب‬
             ‫بلحن مويهة زال و قصيدة لعبزی‪.‬‬
                                                           ‫بلفط پارسی و چینی و خماخسرو‬
      ‫‪.‬‬    ‫دامغانی ‪۲۱۱‬‬    ‫د منوچپری‬

         ‫ور کوه را ز عثبر درسرخمار باشد‪.‬‬                ‫‪- ۸‬کرسرو را ز کوهر برسرشمار باشد‬
      ‫د منوچهری دامفالی ‪.» ۱۲‬‬

=== leaf 79 tail (chap footnotes) ===
                 ‫‪ « 080026 ۰ 0206 - ۴‬افا ‪۲ : ۱‬ص ‪.۵۷۰۹۷‬‬                                           ‫وایاخ ‪.‬‬
                                                                                                       ‫‪ ۰۷‬چ‬
  ‫‪.‬‬     ‫‪ 020۳20‬د«اسفا! ‪ :‬ص‪۱۷‬‬                ‫=یجپ‬
                                               ‫‪ ۵‬چ‬                     ‫به «چیان» («‪.‬م‪۰ ).‬‬     ‫ه‌توب‬
                                                                                                  ‫‪ ۳‬ب‬

  ‫ت چپا ‏ بفتح اول » طرف‌چپ‪ .‬ضد « راستا» بمعنی طرف راست ‪ .‬رك ‪ :‬طبقات ناصری‬
                                          ‫ح ‪۰. ۲‬‬      ‫‪۶‬‬     ‫* تاریخ هقی مصحح د کتر فیاش ص‬            ‫و ‪۱۱‬‬   ‫‪۶۱‬‬    ‫ص‬

  ‫ت چواول ‪ -‬بفتح اول وضم چپارم » ازتر کی «چپاول»( ‏ چاپاوقی)بمعنی کبکه بسوی‬
                                                      ‫‪4‬‬         ‫‪ ,‬عارت» چایار‪« .‬جفتابی ‪۱۷‬‬   ‫میراند ‪ .‬هجوم‬   ‫دشمن‬
```


## [2026-09-06T15:46:30.683Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 600 python3 tools/ref_page.py BQT:1439 2>&1 | head -40"
}
```


### [2026-09-06T15:46:38.579Z] TOOL RESULT

```
REF: BQT:1439  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 232  OCR-lang: fas

-۱:۳۹- هه
قتالیدن ۱ « بفتم‌اول پروزن‌طراویدن, قتردن ۷ « بنتح اول بروزن نکردن»
بمعنی ربختن_ودربدن وشکافتن_وپریشان‌وپر کنده | بمعنی دربدن وپاره کردن ۸ باشد .
کردن ۲ - و کندن‌وازهم جدا کردن ‏ وکستن ۳ فترید ‎٩‏ » بر وزن طلبید . بمعنی
باشد ؛ وبکس اول هم کفته‌اند . درید و دریدن هر دو گفته‌اند که ماشی و مصدر
فتح باب ۴ » کنایه از در باز کردن | باشد -
و گشادکارهاباشد - وابتدای فضل بارندکی‌وایتدای فتریدن *۱ -(۳) بروزن‌طلییدن,بممتی
بارندکی‌رانیز کوبند - وبمعنی بارن دکی‌هم‌هت. | دربدن‌وشکافتن-وپر بشان‌وپرا کنده کردن- وکندن
- ونظر دوک و کب را نیز کفته‌اندباهم که‌خانهای باشد ؛ وبکر اول هم درمت امست.
اشان مقابل باشد همچو عطارد که خانهٌ او جوزا فتلیدن ۱ بالام بروزن ومعنی‌فتریدن
است نار باشد با مشتر ی که خانةٌ او قوس‌است. | و فتاریدن و فتالیدن است که ربختن- وشکافتن
فتراكد بکسراول بروزن (۱) ادراك. | - وکندن وغیره باشد .
تمه و دوالی باشد که از پی وپیش زین اسب تن - بفتح اول بر وزن چمن » بعمتی
آويزند وآنرا ترکی قنجوقه کوبند 6 . شکل وشمایل باشد-ونام ملکی استدرهندوستان
قترد ۲ - بفتم اول و ثانی و اسکون را - و بکس اول درعربی جمع فتنه‌است که فتنه‌ها
و دال بی نقطه ( ۲ ) » هاضی فتردن امت بعنی وآشوبها باشد ‏
چیزیرا ازهم درید وپاره کرد - وبمعنی فاعل که فتنه - بادر اول وافتح آخر که نون
درنده ومقمول که دریده شده - ومصدر که‌وریدن | باشد . نام کنیزك بهرام کور امت و او چنگه را
باشد , هم گفته اند. بغفایت خوب مینواخت . حکایت او و هر وغضب
(۱) چك : بوزن . () چك : - بی نقطه .
(۳) چك : + بفتح اول .
۱ از : فتال (و.م.) + بدن (پسوند مصدری) < فتاریدن (ه.م.) * فترردن * فتردن -
۴ - وبرافتاندن زر وسیم وگل ومانندآن :
باد برآمد بعاخج سیب شکفته بر سر می خواره بر که کل بفتالید .
عماره مروزی «لخت فرس۳۱۱*.
۴ - ای ملك این ملك‌را تو دانی معنیش مال بگیر و سر خوارج بفتال .
۰ منوچهری دامغانی ۱۳۷ >
۴ (ص) کشودن در .
8 - زفتراك بگشاد خم کمند در آورد نا که میاش ببند .
فردوسی طوسی . شاهنامةٌ بخ اج ۳ص ۸۹۵
۹ - رك : فتردن . ۷ - مخفف فتاردن * فتاریدن(ه.م.) * فتالیدن (ه.م.)
۸ - خود برآورد و باز وبران کرد خود طرازید و باز خود بفترد .
خروی « لغت فری ۹۶ *.
‎٩‏ -رد: رشن . ۰ << فتردن (ه.م.) مخقف فتاریدن(ه.م.) ۳ فتالیدن(ه.م.)
۱ مخقف فتالیدن (ه.م.)
```


## [2026-09-06T15:46:50.628Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(d['PLA'].get('page_offset'), '|', d['PLA'].get('lookup_hint'))\"; echo ===; grep -n \"qabbān\\|qabban\\|Qabbān\\|kapān\\|kappān\\|Schnellwaage\\|Waage\" data/verification/sources/refs/incoming/PLA/PLA_pages.txt | head -20"
}
```


### [2026-09-06T15:46:52.870Z] TOOL RESULT

```
Exit code 1
301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276). | HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
(eval):3: == not found
```


## [2026-09-06T15:46:55.434Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA; awk 'BEGIN{RS=\"\\f\"} NR==231' PLA_pages.txt | head -60"
}
```


### [2026-09-06T15:46:57.529Z] TOOL RESULT

```
qubäd                                                                             216                                                         garastün


ls -        qubäd:              "ein           iranischer              König"          Io      pers.         „L; qubäd T               mp. yarıa kavät        5
                  aw.         kaväta               "der     Gründer          v.    Kavi       Dynastie".


>15- gibgär = kibär q. v.
     -                  -                                                                      4         _      3

oLs - qibbän:                       "Schnellwaage"                     pers.             oyly kapän                 ”, syr.       bis       ?.

&-         gabaß:             "Rebhuhn'                         pers.            kapk mp.                3013       kupk      4


gl         - garätig:                     Pl.       v..3b5           gartaq       q.    v.


lb-         garäf:             Pl.         v.        ss garf.


822 9.200 garbädin:                                "Zusammensetzung                    verschiedener                 Medikamente"
          pers.         >     ?.

om                                                                              v4
> - qurbuz:                         "Betrug"               pers.             2, kirbuz             6 ?.


o*»,3-           garbüs:              "Sattelbogen"                    pers.                 ui,    har-puSt               — mp.           xar     "Esel"
          cc      aw.         Xara         +    MP.       Kol        PuSt     "Rücken"         am.              parSta,           mand.     garbasaia
          (p.oxr>)                  7 möglicherweise                         aus       pers.       up harpüs.


2, -       gard:            "Hals"             <        pers.        o,/”gardan         8 m.                 we gardan            9,


 abs             - gardamäni:                        "Panzer,          Helmklappe"             pers.          ne           pers.       „5° gurd "Held"
          cc      mp.         „pp     gurd           11    + män        "ähnlich"            mit    der      Bed.       "einem         Held       passend".

  tt.
Den,         _    garastün:                     "Schnellwaage"                         pers.       5              garstün         12      mand.     garastum



1.       al-Mu’arrab                  s.       v.
2.       Nyberg         Bd.         II     s.       v.
3.       Muhit     s.         v.,         Wahrmund              s.    v.,    Addai        Scher        s.    v.
4.       ebda,     Hosrow                 Qobädan           n.       Chista       Bd.     9 s.      v.
5. Muhit
      s. v.
6.       al-Mu°arrab                  s.       v.,        Muhit       s.    v.
7.       Macuch         Ss.     v.
8.       Addai     Scher              s.       v.
9.       Mackenzie              s.        v.
10.       al-MuCarrab                     s.    v.
11.       Mackenzie                 Ss.    v.
12.       logat     al-foros                       n.     BQ.    s.    v.
```


## [2026-09-06T15:47:08.523Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== LKT campana/qabban ===\"; grep -n -i \"qabban\\|kabbân\\|campana\\|kampanos\\|καμπανός\" LKT.txt | head -20; echo \"=== AFM قبان ===\"; grep -n \"قبان\\|كبان\\|قپان\" AFM.txt | head -10; echo \"=== TAD ===\"; grep -n \"قبان\" TAD.txt | head -10"
}
```


### [2026-09-06T15:47:08.610Z] TOOL RESULT

```
=== LKT campana/qabban ===
=== AFM قبان ===
4306:* (الشّولة ) كوكبان نيران ينزلما القمر فارسيتة سُوَله 
=== TAD ===
2239:قبان - فارسي « كيان » وهو ميزان للاحمال الثقيلة و سةطده في الاسبانية
```


## [2026-09-06T15:47:17.062Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"}{n++; if(index($0,\"قبان - فارسي\")) print \"TAD leaf\",n}' TAD_pages.txt; echo \"=== LEW campus ===\"; grep -n \"campus\" LEW_1910.txt | head -8; echo \"=== LEW camera/camur ===\"; grep -n \"camurus\\|camera,\" LEW_1910.txt | head -8"
}
```


## [2026-09-06T15:47:18.539Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== LAT campus ===\"; grep -n \"campus\\|caminus\\|camera\" LAT.txt | head -12; echo \"=== IEC kamer ===\"; grep -n \"kamer\\|kamara\\|kampos\\|kamp-\" IEC.txt | head -12"
}
```


### [2026-09-06T15:47:19.003Z] TOOL RESULT

```
=== LEW campus ===
=== LEW camera/camur ===
```


### [2026-09-06T15:47:19.069Z] TOOL RESULT

```
=== LAT campus ===
2021:dans des sens derives, cf. campus). M.L., 376.
8971:de camera.
8991:camera, -ae f.(camara, cf. Char., GLK I 58,33, camara dicitur, ut
8992:Verrius Flaccus adfirmat, non camera per e; Funaioli, p.515,6): toiturecampagus
8995:tortum, unde et camerae tecta in curuitatem formata ; P.F., 38,14, camera
8999:voute; cf. M. 1546, et concamero, -rat io (Vite. Pline); camerarius-, et
9000:dans Gr 4 g.de Tours, substantive camerarius, - i: camerier, M.L.154*7;
9001:camerarium: courge en berceau (Plin. 19,70).
9012:caminus, -1 m.: four. Emprunt au gr.xoquvog, correspondant au lat.
9038:tardif que Lydus, de Mag. 1,17 fait d 4 river de campus, sans doute par
9040:v 4 s ou compos 4 s de campus (v. ce mot). Peut-^tre a rapprocher de gr.
9056:campus, -i m.: plaine, terrain piat, gr. 7te8i,0V; par opposition a
=== IEC kamer ===
6706:kamoros (kamur-) “bent; arched; bend, arch’. WP I, 349 Av. kamarà “belt, vault, arch’; kamar-, v. ‘be bent, arched’; Iran. LW in Tk. kemer ‘arch’; Gk. kamára ‘vault, chamber": LW in Arm. ka- mar, id.; Arm. cf. kamur£, gs. kamré£i, Let "bridge'. Cf. SEM: AIE $ 147 2; Lat. camarus, camurus 'crooked, w. crumpled horn'. (Iso- phonic Hitt. kamaras (queried) ‘vapour, smoke’ or ‘darkness’). See Supt.
6719:kampos, à 'crooked, bent; crook, bend, angle, leg’. WP I, 350. Cf. kampo Hindi kampà ‘bent stick for catching birds’; Arm. kam ‘bent’; Gk. kampé ‘bend’; kámpe *canker-worm'; Lat. campus (plain, field’, se- mantics of E bent ‘heath’, Li. lafikas: lankà); Olr. camb. Mir camm, Ir. cam ‘crooked’; s. ‘deceit’; Gaul. cambo- ‘bent’; Br. kamm, id. (also ‘bend’; f. ‘pace, track); OBr. kam(m), adj. id.; W cam, adj. id. also m. ‘wrong, in- jury; step, pace’; Cor. cam, adj. as W (s. ‘pace’); Go. hamfs, ‘maimed’; OS haf ‘lame’; G Hamme ‘haunch, ham; scythe-handle”: OHG hamma ‘ham’; Du. ham, id.; Fris. hamme, id.; Icel. hóm, pl. hamir, f. ‘haunch’; OE hamm ‘ham, haunch; paddock, pasture’; Li. kañpas, m. ‘corner, edge’; kampa ‘arc, bow, crosspiece on sleď’. Substrate element in Rumansch chamma ‘leg’; Alb. (LW) kâmbë, këmbë (but Gallo-Latin gamba, whence It. & Fr.), 1d.; Finn. LW kampur-, cpds. ‘crooked’ beside kampi ‘crank, handle’
6720:kamptos ‘bent, crooked’. Cf. kanthos. WP I, 350-1 Gk. kamptós; OBr. camhed ('felloe', fr. *kam- pita) beside Mod. Br. cammed, f. (/pace, step; felloe’, whence Lat. gambita > Fr. jante & E jaunt); Gaul. cambutta (err. for *cambitta (?) *shepherd's crook’); Arm. kant, s. “holder, handle’. (The provenience of Gk. kanthós and LLat cantus is apparently Celtic in view of Br. W. cant ‘circumference’, but both the seman- tics and the line of evolution are obscure). Cf. kampos, kampóo
7597:komoros (?) (a plant). Cf. WP I, 390 Skt. kamalah ‘lotus’; Gk. kómaros ‘arbutus’. (Isophone: Latv. kamara “crust, rind’)
10042:longos “lame, bent, crooked; meadow, low- land”. (Semantics of Gk. kampé: Lat. campus, see kamp-, and of Li. lañkas “bend, bow? and lankà *watermeadow', see lonquos) Skt. langah ‘lame’; Per. lang, id.; Mod. Gk. lóggos, m. (*wood, grove’. A SI. LW for An- drioti); OCS logü, m., id.; Blg. lág ‘copse, meadow’; Cz. luh ‘meadow, heath’; Pol. lag, teg, m. “lowland, marsh’. (For G Lanke ‘waist, hip, haunch’; Ge-lenk, etc. see Supt: klong-, kleng-)
15452:skam- (1) ‘shameful; shame’. Cf. skamp-. (Arm. ambig.) Oss. Kàm, s. (3) ‘shame’; Dig. kämä, id. (and *pudenda?); Arm. (ambig.) xam, adj. ‘boorish’; MHG scham, adj. ‘shameful’; sf. and -e, wm. & f. ‘shame’; OE scamu, f. ‘shame; privy parts’; ON skamm-, cpds. 'shame-'; OFris. cf. skamel, OHG skamal, adj. "poor"
15465:skamp- (skampið, skampos, skampto-) ‘shorten, constrict; defective, short; lack, want’ Verbal types” Ir. scamaim, scamhaim, v. ‘drain, strip, exhaust, reduce, bare, milk dry'; ON skemma, v. ‘truncate’; Sw. fór-skümma, v. ‘ruin’ beside skämma, v. “fall ill, sicken, pine, turn bad’; mod. Icel. skemma ‘damage’; OCS skọpljọ, skọpiti, v. ‘constrain, contract’; Cz. skoupiti se, v. refl. "be miserly’. Adjectival types: ON skammr, adj. ‘short; MHG scham, adj. ‘disgraced, ashamed’; EME sham ‘coun- terfeit; pretence’; cf. also OE scom-lic, adj. “short? (for *scom- = *sceam?); OCS (and com. Slav) skopü ‘miserly’; Blg. skáp ‘dear’; (LW in) Rum. scump ‘dear’; Latv. skops ‘miserly’. . Further (type *skamptos) Ir. scamtha ‘milked dry’ beside scamhtha ‘stripped, bare); MHG schamede, schemde, schande, f. 'disgrace, shame”; OE scand, f. id. beside E scant (fr. neuter form of skammr); (MHG fr. *skam- pita). Cf. skam- (1)
```


## [2026-09-06T15:47:27.249Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '8991,9015p' LAT.txt; echo \"==== campus ====\"; sed -n '9056,9075p' LAT.txt"
}
```


### [2026-09-06T15:47:27.319Z] TOOL RESULT

```
camera, -ae f.(camara, cf. Char., GLK I 58,33, camara dicitur, ut
Verrius Flaccus adfirmat, non camera per e; Funaioli, p.515,6): toiturecampagus
-161-
vontee, voute; pont de'navire, barque pont 4 e. Non.3°>7, canerun: ob¬
tortum, unde et camerae tecta in curuitatem formata ; P.F., 38,14, camera
et camuri boues a curvatione ex Graeco dicuntur. Emprunt latinis 4 au
gr. xajjopcc. Classique, usuel. M.L.1545; gera.: v.h.a. c(hjamara "Kammer",
d'ol finn .kamari; celt.: iri. camra. De 14 . camero,-as: construire en
voute; cf. M. 1546, et concamero, -rat io (Vite. Pline); camerarius-, et
dans Gr 4 g.de Tours, substantive camerarius, - i: camerier, M.L.154*7;
camerarium: courge en berceau (Plin. 19,70).
camillus, -I a.; camilla, -ae f.: ancien terae du rituel designant
des enfants de naissance libre et noble (cf. P.F.38,8, camillus proprie
appellatur puer ingenuus) qui servaient dans les sacrifices, et accora-
pagnaient sp 4 cialement les flaaines (Serv. auct.Ae.11,543; P.F.83,18).
Rapproche par Varron, L.L.7,34, du grec 3 <aap.irXoe (xa6p,tXoc)> qu'on
retronve a Samothrace; cf. les r 4 f 4 rences de 1 •ed. Goetz-Schoell ad 1 .
D'aprfes Servius, Ae.11,588, le mot s'employait en 4 trusque: ministros
enim et ministras impuberes camillos et camillas in sacris uocabant,
unde et Mercurius Etrusca lingua Camillus dicitur, quasi minister
deorum-, cf. Macr. 3,8,6. Pent-etre a rapprocher de Camenae. V. cumera.
caminus, -1 m.: four. Emprunt au gr.xoquvog, correspondant au lat.
fornax. Terme technique, fr 4 quent surtout dans la langue de l'£glise,
et dans les langues de m 4 tiers (potier, forgeron) . De 11 : camino,-as
d 4 riv 4 sans doute de camlnStus (Plin.). M.L.1548-1549. Sans rapport
==== campus ====
campus, -i m.: plaine, terrain piat, gr. 7te8i,0V; par opposition a
mons (cf. les derivis bas latins campdneus, -nius, dans les Gromat.
331,30, in montanioso loco, ...in campaneis; camposus dans 1'Itala en
couple avec montuosus). D'ou "terrain d’exercice on de bataille (champ
de -)", campus Martius, sens auquel se rattachent 1 'emprunt germanique
kampf, et le derive attesti par les gloses campio, -onis m. "pugnax",
cf. fr. Champion, it. -esp. campione-, ou "carrikre" (ouvrir nn champ A) au
sens physique et moral, - La culture se faisant le plus souvent dans
la plaine, campus a aussi le sens de "champ", dijA dans Caton, Agr.
1,7, campus frumentarius-, Ov. Anui, 3,9, renouatur campus aratris. Campus
ayant tendu A se specialiser dans ce sens, c'est plana qui a pris le
sens de"plaine". Campus s'oppose igalement A urbs, comme la campagne A
la ville, e.g. Tac.,H.3,i7, quantum inter Padum Alpesque camporum et
urbium armis Vitellii... tenebatur. - Ancien, usuel. Panroman. M.L.
1563. Iri. cam, britt. camp. Germ. : m.h.a .kamp, ali .Kampf.
Derives: campestris (-ter), -e(formi d'aprfes terrestris-, cf. siluestris)
"de la plaine, du champ (de Mars)" M.L.1560; substantivi au n. campestre :
caleijon, pagne (pour 1 'exercice au champ de Mars), avec un doublet
populaire campestrumy d'ou campestratus "porteur du cale^on". Campester
est 1 1 adj . de la langue littiraire; A cote figurent: campdnus (forme
```


## [2026-09-06T15:47:34.947Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; grep -n \"kamarā\\|kamara\\|kamurus\\|kam-p\\|kamp-\" WLD_Bd1_pages.txt | head -20"
}
```


### [2026-09-06T15:47:34.997Z] TOOL RESULT

```
32998:*qap na ,Raupe") und die iihnliche Doppelheit (s)kamp- qab- „kriimmen“.
```


## [2026-09-06T15:47:38.030Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; sed -n '32960,33040p' WLD_Bd1_pages.txt; echo \"=== which pdf page ===\"; awk 'NR<=32998 && /\\[pdf page/ {p=$0} END{print p}' WLD_Bd1_pages.txt"
}
```


### [2026-09-06T15:47:39.976Z] TOOL RESULT

```
kumpis „Schweineschinken“, lett. hitmpt „krumm, buckelig werden", apr.
etkumps Adv. „wiederum“ (s. Trautmann Apr. 332, der wie Fick I 4 380,
III 4 93 f. nicht wahrscheinlicher an Nasalbildungen neben gr. y.vpog usw.
denkt ; dazu wohl lit. hitmste „Faust" als *kiimp-ste „die Zusammenkriim-
mung der Finger" (s. u. pijsti-);
   dasselbe u in ai. humpa- (unbelegt) „lahm an der Hand"; in gleicher
Bed.             got. hamfs „verstummelt“ (vgl. dt. einen krummen Fu6,
        vielleicht
Arm liaben), as. haf, ahd. hamf „verstiimmelt, gelahmt" (s. u.); vielleicht
poln. he pa „Busch, Biischel, mit Buschwerk bewachsene Fluliinsel", aksl.
hqpina „i) ftmog, rubus", russ. kupind „Gebiisch, StrauG, Garbe" (Stokes
IF. 2, 173. Berneker GUO); besonders unsicher ai. hapata- n. „Betrug, Hinter-
list"   (ware *qmp-; Uhlenbeck Ai. Wb. 42).
                                          Ygl. Fick II 3 52, I 4 377, 387,
III 4 74,Zupitza Gutt. 108, Solmsen Beitr. 210 Anm. 1, Yf. LEWb. 2 u.
cumpus, Feist Got. Wb. 128. Idg. qamp- ist moglicherweise eine Erw. von
*qam- „biegen, wolben" (s. auch die ahniiche Wz. (s)qamb- von gr. ay.a/u-
jiog,  gall. Cambo-dunum usw.)    doch vgl. auch die nasallose gleichbed.
                                                  ;


Sippe von ai. cCipa- m. n. „Bogen“, capala- ,.unstet, schwankeud", np. cap
„link", d. i. ,*krumur‘ (Horn Np. Et. 97, Fick I 4 aaO., Uhlenbeck Ai. Wb.
                  2
88, 90, Prellwitz 221    Endzelin KZ. 44, 03 crinnert fiir *capala- auch an
                                         ;


lett. hupamdUes „zappeln“, h'cpardt „zappeln, sich muhsam forthelfen", lit.

hdpanotis „liegend durch Bewegung aller GliedmaGen sich aufzuhelfen
suchen" oder „miihsam gehn, durch verschneiten Weg", Scheftelowitz IF.
33, 142 an russ. capah „schaukeln“, sja „hin und her schwanken". pocabits
„sieh neigen" (doch s. dazu auch Berneker 135 f.); allenfalls (wenn nicht
eher zu sqep- „mit einem scharfen Werkzeug hantieren" s. d.), ahd. happa,       ;


luilba, heppa „Hippe"', happa „Sichel, Hippe" (Fick III 4 74; siehe noch
*qap na ,Raupe") und die iihnliche Doppelheit (s)kamp- qab- „kriimmen“.
            ;                                                                       :
                                      qan           qantho-                                   351

     Fur got. usw. hamfs steht „Yerkriimmt“ als Gdbed. nicht sicher; Schroder
Abl. 16f. stellt es beachtenswert als „verstiimmelt, abgestumpft" zu nd.
hummel           stumpfes Messer", nhd. hummel „Rindvieh ohne Horner",
             „altes,
hummelbock „Widder ohne Horner", ahd. hmnhal „Hummel“ (urspriinglich
„Drohne, xrj(ptjv“, ags. liyf „Bienenstock“ („*bohler Baumstrunk", docb
dies sicher zu lat. ctlpa usw., Wz. qeu-p-) usw. (germ. Basis *hanaf-).


qan- „singen, klingen, auck von anderen Gerauschen".
  Gr. xavd(aaco), Aor. xavdtgm ..mit Gerausch flieBen oder schiitten", xavayrj
„Geton, Gerausch", xavayeco, xavayJCw „schalle, tone" (vgl. azEvdyco, azovayrj
:otevol>), tj'C-xavog „Hahn“ (, in der Morgenfriihe krahend"; unannehmbar

Ehrlich BPhW. 1911, 1574: fj-fix-avog zu lit. vista „Henne“);
      kaumaber xovafiog „Gerauseh“, xovajUoj „raBle“ (Hirt Abl. 92 setzt
ibretwillen  die Basis als *qono- an; mindestens hinsichtlicli des ersten
Yokals gewiB mit Unrecht; es lage Abtonung vor, doch w ohl vielmehr                 7



eine verschiedene; Ficks I 4 382 Vgl. m. lett. kuhkstet „stohnen, schluch-
zen" ist triigerisch, das unbelegte ai. kuhjati „larmt" gehort zu kujati
,.knurrt, brummt, murmelt", z. B. Boisacq u. xovaftog); lat. cano-, -ere
„singen, erklingen, erklingen lassen", cunorus „wohlklingend (vgl. sonorus),
carmen „Gesang“ ( *canmen s. Yf. LEWb. 2 s. v., Boisacq 1114), umbr. ka-
                                  ,


neta „canito", procanurent „praecinnerint", ar-kani „*accinium, cantus fla-
minis; sehr wahrscheinlich auch lat. eic 7 nia „Storch“ (daraus wohl synkopiert
praen. conia, s. Yf. LEWb. 2 s. v.; vgl. zur Yokalstufe ahd. liuon, russ. kdnjn)\
air. canhn „ich singe", cvmr. canu      bret. eana „singen“ (usw., s. Pedersen
                                               ,


KG. II 479 f.), mir. cetal n., cymr. cathl f. ,.Gesang", bret. kentrt f. „le§on“
(*kan-tlo-m, erst brit. zum Fem. geworden, s Pedersen KG. II 6G gegen                     ;

=== which pdf page ===
```


## [2026-09-06T15:47:49.089Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; grep -n \"qamer\\|qam-er\\|qamer-\\|kmarati\\|xa/idpa\\|Gürtel\" WLD_Bd1_pages.txt | head -20; echo ===; sed -n '32880,32925p' WLD_Bd1_pages.txt"
}
```


### [2026-09-06T15:47:49.147Z] TOOL RESULT

```
Exit code 1
32881:       kmarati (nur Dliatup.) „ist krumm“, gr. x/it/.eDoov „Stubendecke,
32938:  Wenn himins , cumera (und y.dplvog) ausscheiden, kann idg. *qamer- oder
(eval):1: == not found
```


## [2026-09-06T15:47:51.436Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; sed -n '32870,32950p' WLD_Bd1_pages.txt"
}
```


### [2026-09-06T15:47:51.493Z] TOOL RESULT

```
  Ai. Kubera- (aus *kabera-, vgl. das Patronymicum Kaberakd-) „ein Geist
der Tiet‘e“ = gr. xd^stgog „ein chthonischer Gott“. Wackernagel KZ. 41, 314.
Beziehung zu gob- „sich gut fiigen“ kann trotz der stark ins Gebiet des
Aberglaubens heruberscbwankenden Bed. von slav. Icobb wohl nicht sach-
lich begriindet werden, und hatte fiir gr. y.dfteiQog auch die Yoraussetzung
illyr. Lautgebung (a = idg. o
                              ) notig.



qam- (qem-?) „wolben, biegen“, vielleicht nur mit r-Formans: gamer-.
       kmarati (nur Dliatup.) „ist krumm“, gr. x/it/.eDoov „Stubendecke,
     Ai.
Tlach, Haus“ (wohl diss. aus *y.pege§gov, Grammont Diss. 43); av. Icamarn
„Giirtel“ (und „*Gewolbe“, s. Fick KZ. 43, 137, wo auch iiber iran. Lehn-
formen im gr. Kulturkreis; dab samtliche zu nennenden gr. und lat. Formen
dieser Quelle entstammen sollen, ist wenigstens fur lat. camur camcrus
kaum glaublich.                    —
                     Fern bleibt av. ka-moroba- „Kopf“, siebe Bartbolomae
                                                                                                         ,




IF. 5, 224, Airan. Wb. 440); gr. xa/uaga „Gewolbe, Himmelbett; bedeckter
Wagen“ (zu Solmsens BPbW. 1906, 852 f. Annabme karischer Iierkunft,
xd/xaga Xeyerai tu aoipalg, s. Boisacq 402 Anm. lat. Lw. camera camara      ;                                ,


,,gewolbte Decke, Zimmerwolbung) ; allenfalls xaplvog „Ofen“ (freilich
Kulturwort, das gew'andert sein konnte; Beziehung zu slav. kamy ,,Stein“,
s. *ak- „scbarf    Hirt Abl. 137, Falk-Torp u. kamin, ist erwixgenswert,
                          l<
                               ,


docb wohl nur als Entlehnung aus einem nordliehen oder ostlichen *kamcno;
   lat. camur
                                                                  1
                -a, -tun „gewolbt, gekriimmt
                      ,
                                                 (dial., s. die Stellen bei Er-
                                                                      '



nout El. dial. lat. 34 f., echt lat. camcrus „obtortus“ bei Non. 30, 7); sebr
                                   1



fraglicli wegen der Gdbed. „geflochtener Korb“, lat. cumcra „Behaltnis zur
Getreideaufbewahrung“ (.        quae fiunt palmeae vcl sparteae
                                              .   .
                                                                       Paul, ex              .   .   .




Fest. 43 L.; s. zuletzt Reichelt KZ. 46, 342; Gdf. ware *komeru; nicht zu
dt. Hamster, woruber s. Berneker 395, Falk-Torp u. hamster), aimer us
350                                                        qamp-


„Kastchen mit den Utensilien der Braut"; got. Minins usw. „Himmel"
braucht nicht als „Gewolbe“ benannt zu sein, sondern kann als Weeken-
der"    (vgl.   lit.   dangiis       „Himmel“         :   dengti „decken“) zu hem- „bedecken,   ein-
kiillen" gehoren,          s.   d.
  Wenn himins , cumera (und y.dplvog) ausscheiden, kann idg. *qamer- oder
*qt mer- angesetzt werden (womit *qt mer- „Tier mit Panzer" wohl identisch).
  Ygl. Curtius 5 140 f Fick I 4 23, 383, Bersu Gutt. 170, Zupitza Gutt. 182,
                                     ,


und zur Scbeidung von hem- „bedecken, einhiillen", Vf. LEWb. 2 u. canm-
rus, Fick III 4 73f,, Falk-Torp u. liam, Meringer WSB. 181, Y S2f.
   An. hamuli „verstiimmelt“ usw. (sei „gekriimmt"; Fick III 4 73, Falk-Torp
u. hammelhoni) bleibt fern (s. she/)- „schneiden“).  DaG *qam-p- „biegen"
und qan-tho- „Eeke“ Erw. von qam- seien, vermutet Yf. LEWb. 2 u. cam-
pus, Boisacq u. y.ajusu], xav&og.
```


## [2026-09-06T15:48:07.527Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,40p' tools/fetch_source.py"
}
```


### [2026-09-06T15:48:07.566Z] TOOL RESULT

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


## [2026-09-06T15:48:11.457Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \"https://en.wiktionary.org/wiki/کمر\" \"https://en.wiktionary.org/wiki/چپ\" \"https://en.wiktionary.org/wiki/قپان\" \"https://www.etymonline.com/word/cabaret\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/hibin\"; do timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 237, root Kam 2/Kamer/Kamp, checking the Persian and Germanic nodes\" 2>&1 | tail -2; done"
}
```


### [2026-09-06T15:48:18.090Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/d831a3de0b9951fe.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/37acf239895f599d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4fd93f9d915cc0c3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a9259455bce7775a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/809ba7f9ada7a367.txt
```


## [2026-09-06T15:48:20.535Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo \"=== kamar ===\"; grep -n -A12 -i \"^Persian\" d831a3de0b9951fe.txt | head -60"
}
```


### [2026-09-06T15:48:20.586Z] TOOL RESULT

```
=== kamar ===
```


## [2026-09-06T15:48:23.379Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; wc -c d831a3de0b9951fe.txt 37acf239895f599d.txt 4fd93f9d915cc0c3.txt a9259455bce7775a.txt 809ba7f9ada7a367.txt; echo ===; grep -n -i \"etymology\" d831a3de0b9951fe.txt | head"
}
```


### [2026-09-06T15:48:23.428Z] TOOL RESULT

```
Exit code 1
 8660 d831a3de0b9951fe.txt
 7283 37acf239895f599d.txt
 8299 4fd93f9d915cc0c3.txt
 6592 a9259455bce7775a.txt
  161 809ba7f9ada7a367.txt
30995 total
(eval):1: == not found
```


## [2026-09-06T15:48:25.358Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; head -40 d831a3de0b9951fe.txt"
}
```


### [2026-09-06T15:48:25.404Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/کمر
FETCHED: 2026-09-06T15:48:14Z
STATUS: 200
TITLE: کمر - Wiktionary, the free dictionary

کمر - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community portal 
 Requested entries 
 Recent changes 
 Random entry 
 Help 
 Glossary 
 Contact us 
 Special pages 

 Search 

 Search 

 Appearance 

 Donations 

 Create account 

 Log in
```


## [2026-09-06T15:48:28.246Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; sed -n '40,200p' d831a3de0b9951fe.txt"
}
```


### [2026-09-06T15:48:28.293Z] TOOL RESULT

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
 Khalaj 

 Toggle Khalaj subsection 

 1.1 
 Noun 

 1.1.1 
 Declension 

 2 
 Persian 

 Toggle Persian subsection 

 2.1 
 Etymology 

 2.2 
 Pronunciation 

 2.3 
 Noun 

 2.3.1 
 Derived terms 

 2.3.2 
 Descendants 

 2.4 
 References 

 2.5 
 Further reading 

 3 
 Urdu 

 Toggle Urdu subsection 

 3.1 
 Etymology 

 3.2 
 Pronunciation 

 3.3 
 Noun 

 3.3.1 
 Declension 

 3.4 
 References 

 3.5 
 Further reading 

 Toggle the table of contents 

 کمر 

 13 languages 

 العربية 
 বাংলা 
 Ελληνικά 
 فارسی 
 Na Vosa Vakaviti 
 Français 
 Bahasa Indonesia 
 Kurdî 
 Malagasy 
 Polski 
 سرائیکی 
 Тоҷикӣ 
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

 Khalaj
 [ edit ] 

 Noun
 [ edit ] 

 کَمَر ( kamar, kəmər ) ( definite accusative کَمَری or کَمَرؽ , plural کَمَرلَر or کَمَرلار ) 

 Arabic spelling of kamar , kəmər ( “ hillside , boulder ” ) 

 Declension
 [ edit ]
```


## [2026-09-06T15:48:30.170Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; sed -n '200,320p' d831a3de0b9951fe.txt"
}
```


### [2026-09-06T15:48:30.243Z] TOOL RESULT

```
 Declension of کمر 

 singular

 plural

 nominative

 کمر 

 کمرلار 

 genitive

 کمرݧ 

 کمرلارؽݧ 

 dative

 کمرقا 

 کمرلارقا 

 definite accusative

 کمرݧ 

 کمرلارؽ 

 locative

 کمرچا 

 کمرلارچا 

 ablative

 کمردا 

 کمرلاردا 

 instrumental

 کمرلا 

 کمرلارلا 

 equative

 کمرواره 

 کمرلارواره 

 Declension of کمر 

 singular

 plural

 nominative

 کمر 

 کمرلر 

 genitive

 کمرݧ 

 کمرلریݧ 

 dative

 کمرکه 

 کمرلرکه 

 definite accusative

 کمرݧ 

 کمرلری 

 locative

 کمرچه 

 کمرلرچه 

 ablative

 کمرده 

 کمرلرده 

 instrumental

 کمرله 

 کمرلرله 

 equative

 کمرواره 

 کمرلرواره 

 Persian
 [ edit ] 

 Etymology
 [ edit ] 

 From Middle Persian [script needed] ( kml /⁠kamar⁠/ , “ waist, belt, girdle ” ) , 𐫞𐫖𐫡 ( qmr /⁠kamar⁠/ , “ vault ” ) from Old Persian , from Proto-Iranian *kamarā- ( “ something curved ” ) , from *kamárati , from Proto-Indo-Iranian *kmárati , from Proto-Indo-European *kh₂m-ér-e-ti , from *kh₂em- ( “ to bend, curve ” ) (see there for further cognates). Doublet of کمرا ( kamrâ ) . [ 1 ] 

 Pronunciation
 [ edit ] 

 Audio ( Iran ) : ( file )
```


## [2026-09-06T15:48:34.853Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; sed -n '320,420p' d831a3de0b9951fe.txt"
}
```


### [2026-09-06T15:48:34.906Z] TOOL RESULT

```
 Audio ( Iran ) : ( file ) 

 Dari

 کمر 

 Iranian Persian

 Tajik

 камар 

 IPA ( key ) : [kʲæmæɾ] 

 Noun
 [ edit ] 

 کمر • ( kamar ) 

 waist 

 girdle , belt 

 the middle of a mountain

 the flank of an army

 arch , cupola , dome , arched bridge 

 Derived terms
 [ edit ] 

 کمربند ( kamar-band ) 

 Descendants
 [ edit ] 

 → Armenian: քամար ( kʻamar ) 

 → Azerbaijani: kəmər 

 → Middle Bengali: কমর ( komor ) 
 Bengali: কোমর ( kōmor ) 

 → Georgian: ქამარი ( kamari ) → Bats: ქამარ ( kamar ) 

 → Gujarati: કમર ( kamar ) 

 → Hindustani: 
 Hindi: कमर ( kamar ) 
 Urdu: کمر ( kamar ) 

 → Kashmiri: کَمَر ( kamar ) 

 → Khalaj: kamar 

 → Malay: kamar 

 → Marathi: कंबर ( kambar ) 

 → Punjabi: ਕਮਰ ( kamar ) 

 → Ottoman Turkish: كمر ( kemer ) Turkish: kemer 
 → Albanian: qemer 
 → Armenian: քէմէր ( kʻēmēr ) , ք յ ա̈մա̈ր ( kʻ y ämär ) 
 → Bulgarian: кеме́р ( kemér ) 
 → Greek: κεμέρι ( keméri ) 
 → Romanian: chimír , chimér 

 References
 [ edit ] 

 ^ Edelʹman, D. I. ( 2011 ), Etimologičeskij slovarʹ iranskix jazykov [ Etymological Dictionary of Iranian Languages ] (in Russian), volume 4, Moscow: Vostochnaya Literatura, page 191 

 Further reading
 [ edit ] 

 Steingass, Francis Joseph ( 1892 ), “ کمر ”, in A Comprehensive Persian–English dictionary (overall work in English), London: Routledge & K. Paul, page 1049 

 Urdu
 [ edit ] 

 Urdu Wikipedia has an article on: کمر 

 Wikipedia ur 

 Etymology
 [ edit ] 

 Borrowed from Classical Persian کَمَر ( kamar ) . [ 1 ] First attested in c. 1635 as Middle Hindi کمر ( kmr /⁠kamar⁠/ ) . [ 2 ] Displaced Middle Hindi لنک ( lãk , “ waist ” ) .

 Pronunciation
 [ edit ] 

 ( Standard Urdu ) IPA ( key ) : /kə.məɾ/ 

 Audio ( Pakistan ) : ( file ) 

 Rhymes: -əɾ 

 Hyphenation: کَ‧مَر
```


## [2026-09-06T15:48:39.621Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; grep -n -A20 \"Persian\" 37acf239895f599d.txt | grep -n -A20 \"Etymology\" | head -50; echo \"=== raw tail ===\"; sed -n '/^ Persian$/,/^ Urdu$/p' 37acf239895f599d.txt | head -60"
}
```


### [2026-09-06T15:48:41.264Z] TOOL RESULT

```
6:73- Etymology 1 
7-74-
8-75- 2.1.1 
9-76- Pronunciation 
10-77-
11-78- 2.1.2 
12-79- Adjective 
13-80-
14-81- 2.1.2.1 
15-82- Derived terms 
16-83-
17-84- 2.1.2.2 
18-85- Related terms 
19-86-
20-87- 2.2 
21:88- Etymology 2 
22-89-
23-90- 2.2.1 
24---
25-226: Persian
26-227- [ edit ] 
27-228-
28:229- Etymology 1
29-230- [ edit ] 
30-231-
31-232- From Proto-Indo-European *kep- ( “ to bend, curve ” ) , a possibly dialectal combination of Proto-Indo-European *kh₂emp- ( “ to bend, curve ” ) + *(s)kamb- ( “ crooked ” ) (compare Latin cambiō ( “ to exchange ” ) , whence English change ), the latter ( *(s)kamb- ) which may be of the same origin as the former ( *kh₂emp- ). Cognate with Sanskrit चाप ( cāpa , “ bow, arc ” ) , Sanskrit चपल ( capala , “ trembling, unsteady, wavering ” ) . [ 1 ] 
32-233-
33-234- Pronunciation
34-235- [ edit ] 
35-236-
36-237: ( Classical Persian ) IPA ( key ) : /ˈt͡ʃap/ 
37-238-
38-239- ( Dari, formal ) IPA ( key ) : [t͡ʃʰäp] 
39-240-
40-241- ( Dari, formal ) IPA ( key ) : [t͡ʃʰäp] 
41-242- ( Kabuli ) IPA ( key ) : [t͡ʃʰäp] 
42-243-
43-244- ( Hazaragi ) IPA ( key ) : [t͡ʃʰäp] 
44-245-
45-246- ( Iran, formal ) IPA ( key ) : [t͡ʃʰæpʰ] 
46-247-
47-248- ( Tajik, formal ) IPA ( key ) : [t͡ʃʰäp] 
48-249-
=== raw tail ===
 Persian
 [ edit ] 

 Etymology 1
 [ edit ] 

 From Proto-Indo-European *kep- ( “ to bend, curve ” ) , a possibly dialectal combination of Proto-Indo-European *kh₂emp- ( “ to bend, curve ” ) + *(s)kamb- ( “ crooked ” ) (compare Latin cambiō ( “ to exchange ” ) , whence English change ), the latter ( *(s)kamb- ) which may be of the same origin as the former ( *kh₂emp- ). Cognate with Sanskrit चाप ( cāpa , “ bow, arc ” ) , Sanskrit चपल ( capala , “ trembling, unsteady, wavering ” ) . [ 1 ] 

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈt͡ʃap/ 

 ( Dari, formal ) IPA ( key ) : [t͡ʃʰäp] 

 ( Dari, formal ) IPA ( key ) : [t͡ʃʰäp] 
 ( Kabuli ) IPA ( key ) : [t͡ʃʰäp] 

 ( Hazaragi ) IPA ( key ) : [t͡ʃʰäp] 

 ( Iran, formal ) IPA ( key ) : [t͡ʃʰæpʰ] 

 ( Tajik, formal ) IPA ( key ) : [t͡ʃʰäp] 

 Rhymes: -ap 

 Readings

 Classical reading ? 

 čap

 Dari reading ? 

 čap

 Iranian reading ? 

 čap

 Tajik reading ? 

 čap

 Adjective
 [ edit ] 

 Dari

 چپ 

 Iranian Persian

 Tajik

 чап 

 چپ • ( čap ) 

 left
```


## [2026-09-06T15:48:47.019Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; sed -n '/^ Persian$/,$p' 4fd93f9d915cc0c3.txt | head -50; echo \"=== etymonline cabaret ===\"; grep -n -i -A6 \"cabaret (n\" a9259455bce7775a.txt | head -30"
}
```


### [2026-09-06T15:48:48.754Z] TOOL RESULT

```
 Persian
 [ edit ] 

 Alternative forms
 [ edit ] 

 کپان ( kapân ) 

 قپون ( qapun ) ( colloquial Teherani ) 

 Etymology
 [ edit ] 

 Borrowed from Byzantine Greek κάμπανος ( kámpanos ) , γάμπανος ( gámpanos ) , from Latin campāna .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /qa.ˈpaːn/ 

 ( Dari, formal ) IPA ( key ) : [qä.pʰɑ́ːn] 

 ( Dari, formal ) IPA ( key ) : [qä.pʰɑ́ːn] 
 ( Kabuli ) IPA ( key ) : [qä.pʰɑ́ːn] 

 ( Hazaragi ) IPA ( key ) : [qä.pʰɔ́ːn] 

 ( Iran, formal ) IPA ( key ) : [qæ.pʰɒ́ːn] 

 ( Iran, formal ) IPA ( key ) : [qæ.pʰɒ́ːn] 
 ( Tehrani ) IPA ( key ) : [qæ.pʰúːn] 

 ( Tajik, formal ) IPA ( key ) : [qä.pʰɔ́n] 

 Rhymes: -aːn 

 Readings

 Classical reading ? 

 qapān

 Dari reading ? 

 qapān

 Iranian reading ? 

 ġapân

=== etymonline cabaret ===
23: cabaret (n.) 
24-
25- 1650s, "tavern, bar, little inn," from French cabaret , originally "tavern" (13c.), which is of uncertain origin, perhaps from Middle Dutch cambret , from Old French (Picard dialect) camberete , diminutive of cambre "chamber" (see chamber (n.)). The word was "somewhat naturalized" in this sense [OED, 1989]. It was borrowed again from French with a meaning "a restaurant/night club" in 1912; the extension of meaning to "entertainment, floor show" is by 1918.
26- also from 1650s 
27-
28- Entries linking to cabaret 
29-
```


## [2026-09-06T15:49:00.522Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 120 python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/himinaz\" --note \"page 237, node 12 Germanic himin/hibin 'vault of heaven' - checking the root\" 2>&1 | tail -2"
}
```


## [2026-09-06T15:49:01.986Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; for w in کمر چپ خم کپان; do echo \"== $w\"; awk -v W=\"$w\" 'BEGIN{RS=\"\\f\"}{n++; if (index($0,W)) printf \"leaf %d\\n\", n}' ARY_pages.txt | head -4; done"
}
```


### [2026-09-06T15:49:03.412Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/108586e3718551f5.txt
```


### [2026-09-06T15:49:05.672Z] TOOL RESULT

```
== کمر
leaf 408
leaf 545
== چپ
leaf 10
leaf 205
leaf 298
leaf 414
== خم
leaf 12
leaf 13
leaf 37
leaf 46
== کپان
```


## [2026-09-06T15:49:08.497Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; awk 'BEGIN{RS=\"\\f\"} NR==408' ARY_pages.txt | head -30; echo \"=== chap leaf 205 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==205' ARY_pages.txt | grep -n \"چپ\" -A4 -B2 | head -20"
}
```


### [2026-09-06T15:49:11.687Z] TOOL RESULT

```
[pdf page 408]
ککه که که ککا(به چم *سرگین* "برازه *گه) | ۳۰۹
بادداشت:
چم این واژه در اوستایی و اوستی و کردی: کمربند» تسمه,
چم این واژه در سأنسکریت: خمیده» قوسدار,
چم این واژه در زبان‌های پونانی و رومانس: هرچیز دارای سرپوش با تاق قوسدار» تاق ضربی» اقاقق,
سانسکریت (54(/877077): ۲۸۹۸۲۸۹ کش ۸77
ارمنی (470/2(7490): 3 لهستانی (0[./877): هلف
برنانی 0قق0): ۰ فلقفا راکش . روسی (854(0ا0: ما
لانین (7120ها): زد ۱ ۵ اد واه صربی (/(58814): ۰ ۸6111 ,[7ه۸ا
فرانسه (ل۳82۸): 3 دا ی برهمی (/80/75//140): را
آسپانیایی (5۳۸(71923): 3 ابرلندی میانه (۳28514(4 ۰4/005 :
اینالپایی (/(ت74/): ای ۸۲۸
رومانی ربمه ۲ آفعه) ,۲2۶۸ ولزی (78.877): ۱ ۹:۱
پرنغالي (۳0/77017882): ۸۸ بر تونی (/8670۸): 1
ایسلندی کهن (5(070۸/27 صا۵):
ه۸ پسگشت‌ها 5
آلمانی (400ا2/9: ۰ 6366۸ ,1۸086 ق2۶00
انگلیسی کهن (3لا2(/0 0ا0): 62 (071187) :۵/۸72 ا5ط
: 07 ۸6 25 ناه
هو انگلپسي (ب3۸/08)(محلی) دا 52/0 ه2 070 5۳70875 ۷81۷ 778 ۱
دانمارکی شمش ۳ هه ۱ 314 :(۵/07[/0ظ
هلندی (بلع۵7: ۹" ده 32 مان
اسلاوی کهن (7۴ها5 2770807 ص0): برهان قاطع : ۱۳۶۵ ْ
۱

=== chap leaf 205 ===
20-روسی (۷ل۸ا59/): 1116 ,71 وتا[ برهان قاطع : ۵7۶
21-یادداشت:
22:۱ چم اين واژه در زبان لاتین: چپاندن» پرکردن 8
23-چم این واژه در زبان ایسلندی کهن و ایرلندی کهن و ولزی: تپه» بلندی اعتلا. :
24-چم این واژه در زبان انگلیسی کهن: شاخ و برگ» برگ دادن,
25-چم اين واژه در زبان‌های اسلاوی و زبان لیترانی: چاق» چاق شدن
26-.۰ ۲ واژه‌ی انگلیمی 13 (انگلیسی کهن:3738073 ب5113) آلمانی کهن:01018 فریزی کهن:3055 71
```


## [2026-09-06T15:49:20.554Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; sed -n '/^ Etymology$/,/^ Noun$/p' 108586e3718551f5.txt | head -30"
}
```


### [2026-09-06T15:49:22.555Z] TOOL RESULT

```
 Etymology
 [ edit ] 

 Unclear, but possibly descending from Proto-Indo-European *h₂éḱmō ( “ stone ” ) with heavy remodelling, including apparent metathesis similar to Proto-Slavic *kamy . The difference in meaning seems to be bridged by Ancient Greek ἄκμων ( ákmōn ) , meaning among other things “meteorite”. Kroonen suggests “heavenly vault” as the original meaning. Compare also Iranian cognates such as Persian آسمان ( âsemân, âsmân , “ sky, heaven ” ) .

 Kroonen proposes descent primarily from the genitive *h₂ḱm̥nós , yielding first in Germanic a paradigm with nominative *hemô , genitive *hemnaz , dative *hemeni , later levelled further to give two parallel stems *hemina- and *hemna- . [ 1 ] 

 Another proposal, by Hjalmar Frisk and Friedrich Kluge, suggests the root Proto-Indo-European *kem- ( “ to cover ” ) (most likely with the form *kem-eno-s ( “ the "covered" thing, the shroud ” ) ) as the source, due to the more straightforward phonology (the meaning could be derived from how the sky figuratively "covers" the earth from space or the divine). This would become *heminaz , with the modern form of coming from e > i raising before nasals (such as -n- , found in this word) and the close front vocalics i and j (of which this word contains the former), which is standard in Germanic.

 A further suggestion, linking it to Proto-Indo-European *ḱey- ( “ to settle ” ) (via a form expanded with -m- , such as *ḱi-m-inos ), having the sky the "abode of the gods", is discussed by Kroonen and Orel, though this is much more niche and was less popular than the former.

 The "cover" proposal eventually stopped being the dominant hypothesis of derivation in favor of *h₂éḱmō , due to the idea of the sky being a stony or metallic thing being found across the Indo-European languages, most notably in Vedic Sanskrit अश्मन् ( aśman ) , which the Rigveda uses to refer both to stone and the sky. Some scholars also link this to Proto-Germanic *hamaraz ( “ hammer ” ) , which were formerly made of stone, basing this proposal on a connection between the sky and the hammer of Thor (further lending support to the *h₂éḱmō hypothesis). The more abstract and culturally bland semantics of the other two proposals, as well as their unclear morphological derivation, despite their more straightforward phonology, are why they are now rejected by most.

 Pronunciation
 [ edit ] 

 IPA ( key ) : /ˈxi.mi.nɑz/ 

 Rhymes: -i.mi.nɑz 

 Noun
```


## [2026-09-06T15:49:30.037Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for w in \"heaven\" \"chamber\" \"chimney\" \"camp,\" \"champion\" \"camera\"; do echo \"== SKT $w\"; grep -n -m2 -i \"^$w\\|; $w\" SKT.txt | head -3; done"
}
```


### [2026-09-06T15:49:31.836Z] TOOL RESULT

```
== SKT heaven
== SKT chamber
3634:chamber,  room  up  in  the  raficw.
== SKT chimney
3346:CHIMNEY.
3385:Chimney.  (F.-U-Gk.)  F.  cktm *  a  chimney  ;*    Cot.  *  Low  L. provided  with  a  ckimort ;  hcooe,  at »L.  rtfOTMM/.  a  &r<  |ilaoc;«*< oyttL,  fire  plsM.
== SKT camp,
== SKT champion
== SKT camera
22899:camera — chamber.
```


## [2026-09-06T15:49:34.436Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i -m3 \"Heaven\\.  (E\" SKT.txt; grep -n -m3 \"Camp\\.  \\|Chamber\\.  \\|Champion\\.  \\|Cabaret\" SKT.txt | head"
}
```


### [2026-09-06T15:49:34.490Z] TOOL RESULT

```
2692:camlet,    a    «tuft.     ^Arah )      Formerly fdm^^/.supposedto  be  named  from  coittAin- iiiK  iitmel's  nair.    Really  iVoro  Arab,  kham^ /at,  khamalat,  camlet;  Kicb-  Diet  p.  c'ljs. Camellia.    (Personal   name.)     A   plant named  after  Geo.  Jos.  Kamcl,  a  Moravian Jesuit,   who    dt'&cjibed   the    plants    Ui   the ishuid  of  Liuon. Camelopard :  see  CameL Cameo.  (Ital.)     Ital.  cammeo,  a  cameo, piecious  stune  carved  ic  relief.     Origin  tin* known. Camera.  (L.)     L.  camera,,  a  chamber; hence  camera  odsatra.  a  dork  chamber,  box for  photography  ;  see  Chamber. Camlet ;  see  CameL Camomile ;  .%ec  Chamomile. Camp.  (L.)     We  find  F.  camp  (Cot.)  ; bnt  the  E.  word   was  prob.  taken  directly from  L.  eamfus.  a  field,  ground  held  by  an army.  +  Gk.  w^»o»,  a  garden.
```


## [2026-09-06T15:49:39.838Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -o \"Heaven\\.[^|]\\{0,320\\}\" SKT.txt | head -3; echo \"=== FSD/WEB camera ===\"; grep -n -o \"cummerbund[^|]\\{0,200\\}\" FSD_vol1.txt WEB_vol1.txt 2>/dev/null | head -4"
}
```


### [2026-09-06T15:49:41.923Z] TOOL RESULT

```
=== FSD/WEB camera ===
WEB_vol1.txt:104393:cummerbund. ;
```


## [2026-09-06T15:49:44.843Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -o \"Heaven[^|]\\{0,250\\}\" SKT.txt | head -5; echo \"=== WEB cummerbund ctx ===\"; sed -n '104388,104398p' WEB_vol1.txt"
}
```


### [2026-09-06T15:49:48.741Z] TOOL RESULT

```
=== WEB cummerbund ctx ===
etc. ků’miss, 7. [G., Russ. kumis, from Tatar kumiz.] A :
1. mare's or camel's milk fermented (or dis- tilled) and used as a drink by Tatar nomads of Asia. ;
2. a similar drink made from cow's milk, used in certain special diets.
Also spelled koumis, koumiss, koumyss.
kiim/mel (kim/1; G. kim/el), n. [G.] a liqueur flavored with caraway seeds, anise, cumin, etc.
kum/mér-bund, n. same as cummerbund. ;
kum’quät, z. [from dial. pronun. of Chin. chin-chü, lit., golden orange.) __
1. an orange-colored, oval fruit about the size of a small plum, with a sour pulp and a sweet rind, used in preserves and confections.
2. the tree that it grows on.
Also spelled cumquat.
, bull, brite, tirn, up; ery, myth; cat, machine, ace, church, chord; gem, añger, (Fr.) bon, Bee
```


## [2026-09-06T15:49:52.093Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -o \"cum.mer.bund[^|]\\{0,220\\}\" WEB_vol1.txt | head -4; echo \"=== FSD cummerbund ===\"; grep -rn -o \"cummerbund[^|]\\{0,200\\}\" FSD_vol1.txt | head -3"
}
```


### [2026-09-06T15:49:53.945Z] TOOL RESULT

```
=== FSD cummerbund ===
```


## [2026-09-06T15:50:14.388Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; wc -l KNT.txt; grep -n -c \"kan\" KNT.txt; grep -n -o \"kan[a-z]*\" KNT.txt | sort -u -t: -k3 | head -20; echo \"=== c- entries ===\"; grep -n -o \"^ *[cč]a[a-z]*-\" KNT.txt | head -20"
}
```


### [2026-09-06T15:50:16.052Z] TOOL RESULT

```
5868 KNT.txt
57
101:kanes
=== c- entries ===
2063:case-
5378:canah-
```


## [2026-09-06T15:50:20.975Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"kan-\\|kam-\\|kāma\\|kamna\" KNT.txt | head -20"
}
```


### [2026-09-06T15:50:21.065Z] TOOL RESULT

```
614:Gaubaruva = barv-, on the evidence of Elam. kam-bar-ma, or -barw- on the added evidence of Akk. gu-ba-ru-’, Gk. Гов pins.
638:of the prior character is a pronounced vowel: айа = adadá, im"m* = imam. Any long con- sonants which had developed by assimilation had been shortened in Iranian; even the doubles that came from enclisis were graphically reduced to singles: брт DB 1.95 = äpiš-šim, laumanisaiy DNb 25f = taumanis-Saiy, [n"yāikama Аа 4 = niydkam-maiy (852.1). An error in cutting the characters, or in the drafting of the model
1265:For OP x from £ before consonants, see $102 and $108. Corresponding to Skt. khdnati ‘he digs’ we have OP akantya ‘it was dug’, Av. kan- ‘dig’, and Av. xà ‘well’, with unexplained variation between aspirate and non-aspirate.
1315:Perhaps in OP amaxmatà (see Lex. s.v. amara- mata), where the relation to other forms from the root kam- (if this etymology be correct) prevented the further change of xm to hm. ПІ. Other examples of earlier Е before con-
1379:enclitics: kamnam, jiyamnam, acc. nākam, adam- : q | kim, avakaram-ca-maiy, parwam-ciy. On [n*yà]- ; kama = |kam-ma, see $130. On pIE m, see $67; ^
1389:Ka™bijiya ‘Cambyses’, Elam. kan-bu-si-ja, АКК. kam-bu-2t~{a.
1401:root, kan- ‘dig’ + pass. -ya-, in akaniya ‘was dug’. *duS- ll’ + *yür- ‘year’, in dušiyãram ‘famine’. wamarsiyus nsm. ‘by self-death’, Skt. mriyú-š
1611:maniíaiy = taumanis-Saiy, I'yü)kama = -kam-
1811:П. Secondary -па-, forming adjectives: para- na-, perhaps here kam-na; as mase. sb., drauja- па-, as nt. abstract pariy-ana-; forming hypo- coristic personal name, Aci-na-; perhaps Mardu- na- in Mardun-tya-; forming place names, with lengthening of preceding vowel, Varkàna- to varka-, Ha"-gmalàna- to ha?-gmala-; with -na- of uncertain origin, h*zdna- (see Lex. s.v.).
2044:Inst. Pl. asabára:b$, martiyaibiš, hamigtyaibis, bagaibi, vibaibiš, kamnarbis; Мааа, Sakai- b, Pardavaibis, Mārgavaibiš, Üvjiyaibis; nt. ünaraibiš,
2047:Nt. Nom. Sg. zsacam, dusiyaram, ardatam, darant- yam, aruvastam, dàtam, Sakatam, kartam, visam, kamnam; aec. xsagam, stánam, daraniyam, aru- vastam, kartam, visam, uvdipasiyam, uvaspam, probably casam.
2497:pIE *dher- ‘hold firm’: pAr. *йАатата- in Skt. dhárdyati; OP darayamzy, darayatty, pl. déraya"- tiy, imf. 3d sg. addraya‘, mid. lst sg. kam- adárayaty, 3d sg. ada(rayatla.
2531:$220. Tue Passive-Votce Present STEM of pIE was formed by the addition of the suffix pIE -je-/-4o-, which is accented in Sanskrit; in OP the root regularly has the normal grade, with -a-: imf. 3d sg. and pl. abariya abariya", to root bar-; ayadiya ayadiya", to yad-; akaniya, to root kan- ‘dig’; afahya and afahiya, to Ваћ-; avaniya, to van-; ajantya, to jan-; akariya akariya"la, to kar-; pres. ist pl. &ahyàmahy, to dah-; opt. 3d sg. kariyaiš to kar-, frabiyats to frað-, 3d pl. yadiyaiša” to yad-.
2544:navinaiy, 3d sg. kunavatazy. var-, pres. varnay(a)-: varnavátauy. xsnav-, pres. zinav(a)-: ü-z5navàhy. kan-, pres. kan(a)-: vi-kandhy (and -àh*-di$). jan-, pres. jan(a)-: perhaps (restored) 3d pl. vi-
2570:II. The secondary ending is -t, which is not written in OP final after & (840); before - the thematic vowel is -e-: pIK *ebheuet, Skt. dbhavat, OP abava; pIE *ebheret, Gk. &фєре, Skt. dbharat, OP abara; Skt. ddruhyat, OP adurujiya; Skt. ddhd- rayat, OP adáraya; viyamarda; unaugmented ava- harida]; etc. Injunctive @adaya. Remodeled non- thematic, dha‘ ‘was’. Passive, abariya, adariya, etc. (§220). Non-thematic: adānā' to z5nà-, adada to 'dá-, айта to *di-, viy-aka" to kan-, avàja" to ava-jan-; in the last two, radical n as well as end- ing é is not represented in the OP orthography. Strong aorist: pIE *edhél, Skt. ddhat, OP ada. Optatives: Skt. gamydi, OP a-jamiya; OP avā- janiyà, Муй, pert. caxriyd.
2608:$238. THe INFINITIVE occurs in OP only in the present active, with the suffix -tanazy, the ancestor of the NPers, infinitive ending -tän or -ddn: carta- naiy ‘to do’, to kar-; ka*tanaty ‘to dig’, to kan-, cf. NPers. kdndén; bartanaiy ‘to bear’, to bar-; тїраї {апаш ‘to engrave’, to nt-paid-. The c- of cartanaty is evidence for the -e- ablaut-grade in this formation ($98); NPers. kárdün ‘to do’ has k- gen- eralized from the rest of the paradigm.-In form,
2769:may be used as predicate to any subject:! DB 2.18f кага Parsa шй Майа hya ира mam аһа haw kamnam dha ‘the Persian and Median army which was with me—this was a small thing’; во also DB 1.47 uvaipa saam (referring to Parsam utà Madam ша aniyà dahyàva), DNa 39 ctyakaram aha ava dahyava, DNb 6f avakaram amiy, ОХЬ 27f avā- karam-ca-maiy usiy wa framand, DNb 50 ciyükaram amiy ciyükaram-ca-maiy tonaré. A neu- ter subject may have a masculine substantive as predicate: DNb 11f tya rdstam ava тат kama ‘what is right, that is my desire’.
2804:I. The definite article, properly speaking, is lacking in OP, despite the uses given in the pre- ceding section (ef. Lg. 20.6-8); for kya hyd tya as article function only to attach modifiers to another substantive, or to indicate generic value. Thus we find Ката Parsa utä Мада hya ира mam àha haw kamnam aha ‘the Persian and Median army which was with me, this was a small thing’ (DB 2.181); adam Déarayavaus xidyatiya vazraka ‘I (am) Darius the Great King’ (DB 1.1). It is noticeable
3499:56 máhyà : X : raucabis : 6akatà : dha : ауаба : adam : hada : kamnaibis : martiyaibi
3586:Техт or DB, Сошмх П: 1 :98ty : Dárayavaus : xSayafiya : paeüva : Naditabaira : ha 2 dà : kamnaibis : asabaraibis : amufa : Bübirum : ašiya 3 va: pasàva : adam : Babirum : ašiyavam : vasnd : Auramazdiha : uta : Ba 4 birum : agarbiyam : uta : avam : Naditabairam : agarbüyam : pasáva : ava 5 m : Naditabairam : adam : Babirauv : avüjanam —— :0ütüy : Dārayavauš : x 6 Sdyabiya : yātā : adam : Bübirauv : àham : ima : dahydva : tyà : hacàma : ha 7 migiyà : abava : Рагва : Üvja : Mada : Aðurā : Mudráya : Parfava : Margus : Өз 8 tagui:Saka : абу : Dārayavauš : x8dyabiya : I martiya : Martiya : nā Q ma : Cicixrais : puca : Kuganakà : пата : vardanam : Pársaty : avada : adaraya : 10 hauv : udapatatà : Uvjaiy : Кагаһуй : avaðā : afaha : adam : Imanis : amiy : 0 11 vjeiy :xSdyafiya —— : @atiy : Darayavaus : zsayattya : adakaiy : adam : asna 12 iy : àham : abiy : Üvjam : pasáva : hac&ma : alarsa : Üvjiy& : avam : Marti 13 yam :agarbaya : hyašām : mafista : dha : шат : avàjana — : 00у: D 14 árayavaus : xSiyafiya : І martiya : Fravartiá : пата : Мада : hauv : udapatat 15 à : Madaiy : Катаһуй : ауаба : абала : adam : XSa6rita : amìy : Uvaxdtrah 16 уй : taumàyá : pasáva : kāra : Mada : hya : v'àpaliy : haw : hacáma : hamiciya : a 17 bava : abiy : avam : Fravartim : aSiyava : hauv : тёйуайтуа : abava : Madaiy 18 9àtry : Dárayavaus : xšāyaðiya : kara : Parsa : ша : Мада : bya : ира : mim : 4 19 ha : hauv : kamnam : aha : раѕауа : adam : kdram : fraiSayam : Vidarna : пата : Pársa : man 7 20 à : badaka : avam&àm : mafistam : akunavam : avataSaám : afaham : parait : avam : К 2] dram : tyam : Madam : jatà : hya : mand : пау : gaubataiy : pasiva : hauv : Vidarna : ha 22 dà : kara : айуауа : yafà : Madam : parárasa : Māruš : пата : vardanam : Ma 23 дау : ауада : hamaranam : akunaus : hada : Мада : һуа : Màdaisuvà 24 :ma(iSta : dha : hauv : adakaiy : пау : avadà : аһа : Auramazdimary : u 25 раѕійт : арага : vasnà : Auramazdáha : kāra : hya : тара : avam : kàram : t 26 yam : hamiciyam : aja : vasiy : Animakahya : mähyä : XXVII : raueabis : fakat 27 à : аһа : avatüsám : hamaranam : kartam : pasáva : hauv : Ката : һуа : manā : Карада : пат 28 à : dahydus : Mádaiy : avadà : mam : amánaiya : y8tà : adam : arasam : Mada ' 20m : 08у : Dàrayavaus : xšāyaðiya : адаг х : nàma : Arminiya : man 30 à : badaka : avam : adam : frāišayam : Árminam : avafasazy : aaham : paraidiy : ka 31 ra : һуа : hamigiya : mană : naiy : gaubataiy : avam : jadiy : pasiva : Dadarsi 32 š : aSiyava : yafà : Arminam : parárasa : pasáva : hamigiya : hagmatà : paral 33 tà : patiš : Dādaršim : hamaranam : cartanaiy : Züzahya : пата : àvahanam : А 34 rmíniyaiy : avadà : hamaranam : akunava : Auramazdimaiy : upastàm : a 35 bara : vasnà : Auramazdàha : kāra : һуа : manā : avam : küram : {уаш : hamigiyam : 36 aja : vasiy : Oüravaharahya : máhya : VIII : raucabis : 09akatà : dha : ava 87 à$üm : hamaranam :kartam : бабу : Dárayavaus : z3àyaffya : patiy : duv 38 itiyam : hamigiyà : hagmatà : paraitd : patiš : Dàdar&im : hamaranam : carta 3€ nay : Tigra : пата : didà : Arm‘niyavy : avadà : hamaranam : akunava : А 40 uramazdàmaiy : upastàm : арага : vašnā : Ашатагдаћа : kāra : һуа : тапа :a 41 vam : káram : tyam : hamigiyam : aja : vasiy : G9üravüharahya : mihya : ХҮШ 42 :raueabiá : бакаќа : аһа : ауабадат : hamaranam : kartam —— : 00у : Daraya 43 vaus : xšāyaðiya : patiy : citiyam : hamictyd : hagmatà : paraita : pat 44 iš : Dádar&im : hamaranam : cartanaiy : Uyama : nama : didi : Arm'myaty :a 45 vadā : hamaranam : akunava : Auramazdimaiy : upastam : арага : vaSnà : Aurama 46 zdàha : kāra : һуа : manā : avam : küram : tyam : ham?giyam : aja : vasiy : Oàigarea 7 d :mábyà : IX : raucabis : Nakata : dha : ауада ат : hamaranam : kartam : pasava 48 : Dadarsis : citā : mim : amánaya : Arm/niyaiy : yiti : adam : arasam : Ма
```


## [2026-09-06T15:50:32.924Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls site/pages/237.jpg 2>/dev/null; pdftoppm -f 237 -l 237 -r 150 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg237 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T15:50:35.086Z] TOOL RESULT

```
site/pages/237.jpg
total 6768
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 11:50 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     902 Sep  6 11:50 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   92182 Sep  6 10:55 bqt1854.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66580 Sep  6 10:57 bqt2023.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69965 Sep  6 11:25 bqt2242crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   28189 Sep  6 11:25 bqt2417crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  431133 Sep  6 11:16 bqt2420_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9548 Sep  6 11:25 bqt2meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb   81018 Sep  6 11:16 build213.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67391 Sep  6 11:49 build225.py
-rw-rw-r-- 1 sfmqrb sfmqrb   71757 Sep  6 11:47 build232.py
-rw-rw-r-- 1 sfmqrb sfmqrb    6504 Sep  6 11:13 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3402 Sep  6 11:22 c224_n10.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4812 Sep  6 11:28 c224_n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4744 Sep  6 11:22 c224_n1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3203 Sep  6 11:28 c224_n7.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12820 Sep  6 11:27 c229_bibua.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5308 Sep  6 11:27 c229_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5313 Sep  6 11:27 c229_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7793 Sep  6 11:13 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4371 Sep  6 11:13 c_gacele.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3485 Sep  6 11:16 c_harmathan.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12347 Sep  6 11:20 c_hdr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9147 Sep  6 11:16 c_herman2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3841 Sep  6 11:16 c_herman.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12691 Sep  6 11:20 c_ieuo.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2071 Sep  6 11:26 c_ijlak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14654 Sep  6 11:20 c_ijlak.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12239 Sep  6 11:20 c_latis.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6280 Sep  6 11:13 c_mag.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6971 Sep  6 11:03 crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    8619 Sep  6 11:03 crop2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5240 Sep  6 11:03 crop3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12820 Sep  6 11:05 crop_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3408 Sep  6 11:05 crop_guthjo.png
-rw-rw-r-- 1 sfmqrb sfmqrb  111118 Sep  6 11:19 crop_habl.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9001 Sep  6 11:05 crop_node12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5564 Sep  6 11:05 crop_node1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5286 Sep  6 11:05 crop_varathra.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11652 Sep  6 11:13 c_xzn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83691 Sep  6 11:19 gen215.py
-rw-rw-r-- 1 sfmqrb sfmqrb    2303 Sep  6 11:25 j.json
-rw-rw-r-- 1 sfmqrb sfmqrb     228 Sep  6 11:06 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb   37376 Sep  6 11:09 mk201.py
-rw-rw-r-- 1 sfmqrb sfmqrb   77132 Sep  6 11:11 mk207.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61121 Sep  6 11:11 mk208.py
-rw-rw-r-- 1 sfmqrb sfmqrb   80041 Sep  6 11:14 mk214.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67513 Sep  6 11:27 mk217.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74459 Sep  6 11:33 mk218b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   17605 Sep  6 11:25 mk218.py
-rw-rw-r-- 1 sfmqrb sfmqrb   50138 Sep  6 11:24 mk222.py
-rw-rw-r-- 1 sfmqrb sfmqrb   78297 Sep  6 11:32 mk223.py
-rw-rw-r-- 1 sfmqrb sfmqrb   47928 Sep  6 11:38 mk224.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53093 Sep  6 11:40 mk226.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51303 Sep  6 11:39 mk228.py
-rw-rw-r-- 1 sfmqrb sfmqrb   29152 Sep  6 11:37 mk229.py
-rw-rw-r-- 1 sfmqrb sfmqrb   47535 Sep  6 11:47 mk230.py
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:44 p216
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:49 p233
-rw-rw-r-- 1 sfmqrb sfmqrb   17907 Sep  6 11:25 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb   54688 Sep  6 10:58 pg201.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70083 Sep  6 10:52 pg204.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77858 Sep  6 10:52 pg206.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67371 Sep  6 10:53 pg207.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59146 Sep  6 10:53 pg208.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53054 Sep  6 11:00 pg209.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74515 Sep  6 11:02 pg211.png
-rw-rw-r-- 1 sfmqrb sfmqrb  141781 Sep  6 11:03 pg212hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75961 Sep  6 11:02 pg212.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83761 Sep  6 11:03 pg213.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83752 Sep  6 11:01 pg214.png
-rw-rw-r-- 1 sfmqrb sfmqrb  194102 Sep  6 11:05 pg215hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  117034 Sep  6 10:54 pg215.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76564 Sep  6 11:13 pg216.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82798 Sep  6 11:16 pg217.png
-rw-rw-r-- 1 sfmqrb sfmqrb  147278 Sep  6 11:13 pg218hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82099 Sep  6 11:13 pg218.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71937 Sep  6 11:19 pg219.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63280 Sep  6 11:18 pg220.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71497 Sep  6 11:18 pg221.png
-rw-rw-r-- 1 sfmqrb sfmqrb  118895 Sep  6 11:16 pg222hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84108 Sep  6 11:16 pg222.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79615 Sep  6 11:18 pg223.png
-rw-rw-r-- 1 sfmqrb sfmqrb   90848 Sep  6 11:22 pg224hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   55412 Sep  6 11:15 pg224.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80963 Sep  6 11:32 pg225.png
-rw-rw-r-- 1 sfmqrb sfmqrb  161218 Sep  6 11:26 pg226hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74322 Sep  6 11:19 pg226.png
-rw-rw-r-- 1 sfmqrb sfmqrb   54381 Sep  6 11:31 pg227.png
-rw-rw-r-- 1 sfmqrb sfmqrb   52519 Sep  6 11:25 pg228.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78760 Sep  6 11:27 pg229hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   42112 Sep  6 11:26 pg229.png
-rw-rw-r-- 1 sfmqrb sfmqrb   65310 Sep  6 11:32 pg230.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69894 Sep  6 11:34 pg231.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67111 Sep  6 11:35 pg233.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82071 Sep  6 11:44 pg234.png
-rw-rw-r-- 1 sfmqrb sfmqrb   47149 Sep  6 11:44 pg236.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67972 Sep  6 11:50 pg237.png
-rw-rw-r-- 1 sfmqrb sfmqrb   97613 Sep  6 11:49 pg242.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1209522 Sep  6 11:39 sin_goog.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  147680 Sep  6 11:20 sns167.jpg
```


## [2026-09-06T15:50:37.960Z] TOOL CALL #74: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg237.png"
}
```


### [2026-09-06T15:50:37.985Z] TOOL RESULT

```

```


## [2026-09-06T15:50:54.366Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; pdftoppm -f 237 -l 237 -r 400 -png -singlefile EtymologicalDictionary-persian-english.pdf $S/pg237hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('$S/pg237hi.png'); w,h=im.size; print(w,h)\nim.crop((int(w*0.55),int(h*0.26),int(w*0.80),int(h*0.30))).save('$S/c237_n3.png')\nim.crop((int(w*0.38),int(h*0.72),int(w*0.80),int(h*0.78))).save('$S/c237_n18.png')\n\""
}
```


### [2026-09-06T15:50:58.504Z] TOOL RESULT

```
3400 4400
```


## [2026-09-06T15:51:00.788Z] TOOL CALL #76: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c237_n3.png"
}
```


### [2026-09-06T15:51:00.806Z] TOOL RESULT

```

```


## [2026-09-06T15:51:05.007Z] TOOL CALL #77: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c237_n18.png"
}
```


### [2026-09-06T15:51:05.022Z] TOOL RESULT

```

```


## [2026-09-06T15:51:49.965Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HRN kamar ===\"; grep -n -i \"kamar\" HRN.txt | head -10; echo \"=== HUB kamar ===\"; grep -n -i \"kamar\" HUB.txt | head -10; echo \"=== BRT Gürtel ===\"; grep -n \"Gürtel\" BRT.txt | head -10"
}
```


### [2026-09-06T15:51:50.049Z] TOOL RESULT

```
=== HRN kamar ===
7537:aw. kamara- 'Gürtel*; phlv. kamar,
7538:LW. kurd. kemer 'Gürtel*, af/. kamar; oss. LW. d.
16212:I kamar 866.
19830:kamar 866.
=== HUB kamar ===
3111:867. Das Verhaitniss von np. kamar 'altitude, collis, tumu-
3112:lus, saxum* = afgh. LW. kamar 'the middle of a moun-
3115:ys. 56, 12, 4 (Sp.) sowie zu arm. kamar '6ew5lbe,
3130:1 m ae) katnal gelesen werden und entsprSche dann einem ap. ^kamarda-
10520:kamar 88.
=== BRT Gürtel ===
3980:•  j.  'aiiwyästay-  f.  'Anlegen  des  Gürtels, der  Gürtelschnur':  {ytzt)  *'maynqm  *ianßm 'stqm'^  "irlrl^  ndit  anatwyäsH  astrmii "wenn  sie  dem  nackten  Leib  beim  (sva. durch)  Anlegen  des  Gürtels  Schaden  zu- fügen würden,  so  begehen  sie  durch  Nicht- anlegen  des  Gürtels  keine  Sünde"  N.55;
3987:■  j.  aiwylnhana-  n.  i)  'Gürtel,  Gürtel- schnur'*>:  'n^m  r3  aiwya»hayamnS  'mm bO/ayarnnS  (sd.)  Yti.iT,  —  /rä  i! mazdä  harat  ..  'n^m  ..  vanuhim  daSnqm mäzdayasnlm  "dir  (dem  Haoma)  brachte M.  einen  Gürtel  . .,  (näml.)  die  gute mazday.  Religion"  Y.9. 26'*;  —  yat  alle yö  mazdayasnS  ap^rmäyBks  avi  hs  hapta ■na  /rajasäiti . .  °nö "'  paitis  h!  maiayai bU)yamanS  avi  hlnara pascaili  tamauhmti 'wenn  dem  jungen  Masday.  sieben  Jahre vergangen  sind,  soll  man  ihm  den  Gürtel um  die  Hüften  legen,  worauf  ihn  die Männer  (als  ihresgleichen)  achten"  Vd, 18;  20'; — jairyö  °nö  ißjyamanff  "vieitem legt  man  (dem  Toten)  die  Gürtelschnur um"  Vd. /23),  a)  von  der  Schnur,  mit der  die  Barvsmanzvreigt  in  Bündel  zusam- mengebunden werden"":  a^a  'na  N. ioS(?).  2)  'Gewand,  Kleid';  ^5  iama *°«o"  aiitryia^qyanii  "wenn  zwei  gleiche Kleider  anziehen"  N.p4(?);  — yaii  tarasca 'na  aipi.vancainii'^.gs^); — bilyS  ant?ma 'nH  "zweitens  (soll  man  dem  Toten  mit- geben) das  Untergewand"  Vd./i>3'.
3988:*)  Mit  dei  ersten  Anlegung  der  Gürtelschnur (heute  iiuti)  volliieht  sich  die  Aufnahme  des jungen  Ma^ayasHa  in  die  Religionsgemeinde. Sie  geschieht  jetzt  nach  dem  7.,  früher  nach dem   15.  Jahr,  vgl.  Yt.  S.   13    (unter  ayav-)    und
3990:Komp.:  anvi-^'ySvAana-,  zum  V.  >^Ö^..  —  Vgl. np.  ffrähani)  'Hemd',  hamyä»^')  'Gürtel'.  — Pü. ;  aiiByäAami,  'AanilniiTi,  erl.:  hisdt.  — »  Vgl.  zu  diesem  Bild  V.  iS,  1,  lU  aiianayästa-.
4309:•  j.  an-aiwyästa-Adj.  'nicht  mitderGürtel-
4314:—  >)  Die  niazdayaimscht  Religion  als  Gürtel
4316:•  ].  'an-aiwyästay-  f.  'Nichtanlegen  des Gürtels,  der  Gürtelschnur':  yat  tui  .  . /rapataiti  (sd.)  'ta  (LS.)  vä  anabdäts  vä "wenn  ein  Mann . .,  ohne  den  Gürtel  oder das  Hemd  angelegt  zu  haben"  "  V. /ä  54**; —  nöit  'H  (IS.)  astrmti  N._()5,  ^jj^'';  — a  'ti  sir:nti  H.(}6,  +95  3>,
4882:•  j.  ayav-  Adj.  'alt,  in  einem  gewissen Alter  stehend':  nars  kthrpa  pattca.dasar»}iS .  .  taia  yaos  yäia  paoirJm  vTrim  avi  ya bavaiti  ".  .  eines  fünfzehnjährigen  Manns .  .  eines  so  alten,  wie  wann  dem  Mann zum  ersten  Mal  der  Gürtel  angelegt  wird" Yt.Äi4;  14'.
15236:Ableit.  aus  'fianni.dasa.  —  ai.  fancadaiä- Adj.  (fem.  •//■).  —  Pö. ;  pänjdahum.  —  1)  Auch ohne  Trennung  geschr.  —  ')  D.  i.  nach  An- legung des  Gürtels,  Tgl.  Yt.  8.  \%i.
16545:i)  '(den  Gürtel)  lösen  sva.  ablegen': yasca  . .  aiwyänhantvt  vä  aiwyäahayamnö aiwyatfhatum  vd  ds/ayamn^  "..deaGüi- telan-  oder.. ablegend"  Yt  7,17.  a)'be- freien,  retten':  vä^ yäi ^^S^mat(Sp.Bg8  o.) särvm  bunjainti  Yt.  7^46;  —  masyS  an- ÄJM  (sd.)  yat  u^tänim  bunjayäi  ", .  dass  sie ihre  Lebenskraft  rette"  V,  7. 7 1 .  a)  Vor  — ' (haca  mit  Akk. !):  tä  büjat  . .  narsm  haca nasüm  Yt  4.  3.  a)  'sich  retten  vor  — '
```


## [2026-09-06T15:51:50.672Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD; awk 'BEGIN{RS=\"\\f\"} NR==54' FFD_pages.txt | head -40"
}
```


### [2026-09-06T15:51:52.628Z] TOOL RESULT

```
[pdf page 54]
ماده‌های ماضی و مضارع فارسی دری ‏ سا ی ۴۹
پهلوی اشکانی و ایرانی باستان» «دویدن» معنی می‌دهد.

از 2۵۳47422 فارسی میانه در فارسی دری «چندش» آمده است.

0 فارسی میانه مادةٌ ماضی جعلی است. از مادهٌ مضارع ساخته شده
است.< 2224 ایرانی باستان ۵۵4-۵ت*. برای 2 > آرای. ريشةٌ ۸4 به معنی
«هیجان‌داشتن» و 2۵۵414۵8 به معنی «لرزیدنْ» است.

چیدن

چید < فارسی میانه 67 < ایرانی باستان ۵۲-1۵*. برای 18 > آراست. ۲ صورت

ضعیف ريشةٌ ۵7و آن ريشه به معنی «گُزیدن» است. «گُزیدن) هم از اغ آمده است ->
گزیدن.

چین < فارسی میانه 278 < ایرانی باستان ۴۵۲-۵ 3 نشانه‌ای که برای ساختن
مادهٌ مضارع از ريشه به کار می‌رفته است.

خاستن

خاست < فارسی میانه 3391 < ایرانی باستان ۴۸315-12۵ برای 12 -> آراست. 232
صورت اصلی 5ل88 است» 2 پیش از 1به 5 بدل شده است. 1312 صورت بالاندةٌ 822 و آن
به معنی «خاستن» است.

خیز + فارسی میانه 82 < ایرانی باستان 8۵12-2*. برای 2 > آرای.

خاییدن
«خایید» مادهٌ ماضی جعلی است. از مادهٌ مضارع ساخته شده است.
خای چ ایرانی باستان 304-2 برای 3 > آرای. ريشةٌ 40 به معنی «جویدنُ» است.
```


## [2026-09-06T15:52:01.104Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD; awk 'BEGIN{RS=\"\\f\"} NR==53' FFD_pages.txt | head -40"
}
```


## [2026-09-06T15:52:02.261Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '7530,7545p' HRN.txt; echo \"=== leaf of that line ===\"; awk 'NR<=7537{c+=gsub(/\\f/,\"\")} END{print \"leaf\",c+1, \"printed p.\",c+1-21}' HRN.txt; echo \"=== HUB ctx ===\"; sed -n '3105,3132p' HUB.txt"
}
```


### [2026-09-06T15:52:03.095Z] TOOL RESULT

```
[pdf page 53]
ال فعلهای فارسی دری
جوی < ایرانی باستان 7۵00-2*. برای 2 -> آرای.
«جور؛»» دیگر ماد مضارع «جستن»» جدید است > شستن.
از 12040 در پهلوی اشکانی 7047 به معنی «نبرد کردن» آمده است. از ایرانی باستان
۱ 1-82 12 نشانه‌ای بوده که برای ساختن مادهٌ مضارع از ريشه به کار می‌رفته است.
جستر
جست < فارسی میانه 281[. 29122[ در فارسی میانه به معنی «اتفاق‌افتادن» است و
اسم مصدرش 28150[ «بخت) معنی می‌دهد. «جهشیار»» نام خاص, در فارسی میانه
7- 20158[ است به معنی «بختیار).
ججه « فارسی میانه ۵0[.
جویدن
جوید ماده ماضی جعلی و از ماده مضارع ساخته شده است. در قارسی میانه 00[
آمده است» از ایرانی باستان 8-12[*. برای 1۵ -> آراست. ربشةٌ 5[ء که صورت دیگرش
0[ است» «جویدن) معنی می‌دهد.
جو < فارسی میانه 27[ < ایرانی باستان 8۷-۵[ < 928-2[*. برای 2 > آرای. 2[ و
7۷ به ترتیب صورتهای افزودةٌ تا[ و لا[ هستند. :
چریدن
چرید مادهٌ ماضی جعلی است واز مادهٌ مضارع ساخته شده است.
چر < فارسی میانه 6۵7 + ایرانی باستان 23-۵" برای 2 -> آرای. ريشةٌ 27 به معنی
«حرکت کردن» است.
چمیدن
«چمید» مادهٌ ماضی جعلی است. از مادهٌ مضارع ساخته شده است.
چم < پهلوی اشکانی 278 « ایرانی باستان 6۵۵*. برای 2 > آرای. ۵78 در
```


### [2026-09-06T15:52:04.932Z] TOOL RESULT

```
LW. kurd. kirn; afy. bei. (125) kanij n. ßam.
Die Grundform ist ^kanibhua- bezw. *kipbhna'
(Hübschmann, ZDMG. 44, 559, Bartholomae,
Studien H, 101). Kurd. kirn und phlv. kim^ welches
bisweilen vorkommt (z. B. vd. 19 (9)), werden auf den
Comparativ *kamni/ao zurückgehen («-Epenthese).
866. {\)kemer 'Gürtel', kemra^),
aw. kamara- 'Gürtel*; phlv. kamar,
LW. kurd. kemer 'Gürtel*, af/. kamar; oss. LW. d.
kamdri Trauengürtel'.
867. (2)kemer 'Höhe, Berg* etc. (IDD Is. 2, 10).
aw. kamere^a- 'Kopf*; phlv. kamal (wie Bartho-
lomae zu lesen vorschlägt, der kamer eda- als aus
Vermischung der Wörter ai. kakühh-, kakud-, skr.
kapdla-^ lat. caput und ai. mürdhän- entstanden an-
sieht).
=== leaf of that line ===
leaf 215 printed p. 194
=== HUB ctx ===
hat also mit gr. ytaXv^rj nichts zu thun.
865. Die drei Steigerungsstufen lauteten im Altpersischen:
kamna-, ^kanbiyah--, *kanbista- (= zd. kambiSta-), vgl.
zd. taxma--, tc^yah-, tandista^. Also Horn's *kamnyao
eine wuste Bildung! Vgl. Fr. Muller, WZKM.
7, 368.
867. Das Verhaitniss von np. kamar 'altitude, collis, tumu-
lus, saxum* = afgh. LW. kamar 'the middle of a moun-
tain, precipice, cliff, the high bank of a river' zu zd.
kamereda" 'Kopf der Devas u. s. w. = phi. kamdr^)
ys. 56, 12, 4 (Sp.) sowie zu arm. kamar '6ew5lbe,
Bogen, Kuppel, Halle* = gr. Kajudga (xa^idgtj schon
bei Hero dot) *Gewolbe' = lat. camera, np. LW.
kamra 'Gewolbe, Stalf (N 6 1 d e k e , Pers. Stud. H, p. 40)
ist mir unklar.
868. Np. kund *stumpf = bal. kunt *stumpf, grob, einfaltig*
(Geiger) = skr. (prakr.) kunthar- 'stumpf. Davon
kund Vir strenuus* zu trennen, vgl. kunda^ kundavar,
869. Horn bemerkt mit Recht, dass auf paz. xandan
(= kandan) nichts zu geben ist. Das angefiihrte
phi. xantak (wo vorkommend?) kann nur das falsch
ins Pehlevi umschriebene arab. pers. xandaq = arm.
xandak (bei Steph. Asol. und Spateren!) sein, dessen
regulare np. Form kanda^) ist. Afgh. kanql (im Praes.
')>Kdnnte, obwohl nicht mit I geschrieben, doch (naoh Bartho-
1 m ae) katnal gelesen werden und entsprSche dann einem ap. ^kamarda-
= zd. ^hamareSa-,
') Die Nebenform xati' zu Jean 'graben' stUtzt sich im Iranischen
```


## [2026-09-06T15:52:29.787Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD; awk 'BEGIN{RS=\"\\f\"}{n++; if(index($0,\"خمیدن\")) print \"pdf page\",n}' FFD_pages.txt | head; echo; awk 'BEGIN{RS=\"\\f\"}{n++; if(index($0,\"خمیدن\")) print $0}' FFD_pages.txt | grep -A4 \"خمیدن\" | head -20"
}
```


### [2026-09-06T15:52:31.496Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T15:52:36.938Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -m3 \"^کمر:\" MON_part2.txt | head; grep -n -m3 \"کمر: \" MON_part2.txt | head -3; echo \"=== chap ===\"; grep -n -m2 \"چپ: \" MON_part1.txt MON_part2.txt | head -4; echo \"=== xam ===\"; grep -n -m2 \"خم: \" MON_part1.txt | head -3"
}
```


### [2026-09-06T15:52:37.046Z] TOOL RESULT

```
12216:کمر: (پز.) گونه‌ای بلادر؛ بلادر مغربی. 
26348:کمر: ۲ () (بز.) ناحیه‌ای تنه که از بالا 
12216:کمر: (پز.) گونه‌ای بلادر؛ بلادر مغربی. 
26348:کمر: ۲ () (بز.) ناحیه‌ای تنه که از بالا 
40458:کردن و به زور کشیدن. لنگ کمر: (کشتی) 
=== chap ===
MON_part1.txt:24468:وسیله یک زده می‌شود. بکك چپ: از افراد 
MON_part1.txt:68155:نگاهبان. پاسبان. موکل. رقیب دست چپ: 
MON_part2.txt:15850:نازل. قولون چپ: (پز.) قولون نازل. قولون 
MON_part2.txt:86110:چپ: وزیسر دوم (پس از صدراعسظم). 
=== xam ===
8744:اخم: [- اخمه] (.) چین و شکنج که بر 
11646:استخوان لای زخم: (کد.) کار ناتمام» امر
```


## [2026-09-06T15:52:39.408Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '26344,26360p' MON_part2.txt"
}
```


### [2026-09-06T15:52:39.504Z] TOOL RESULT

```
کمدین: 0 (ص.) هنر بیشه‌ای که 
در نماشنامه‌های کمدی. بازی کند. 

کمر: ۲ () (بز.) ناحیه‌ای تنه که از بالا 
محدود به نی ات 5 کر 
تا نی دوازدهمین زوج دنده‌ها قفسه سته 
می‌گذرد و از پایین محدود به سطحی افقی 
می‌شود که از تاج خاصره‌یی مرور می‌کند. 
ناحيةٌ کمری که معمو لا بنام کمر خوانده 
می شو ده در قسمت جلو محدود به سطح 
داخلی تنه‌های مهره‌یی کمری است که در 
پشت امعاء و احشاء در ناحیٌ شکم قرار 
دارند و از قسمت خارج یا خلف عضلهة 
خاجی کمری و پوست بدن در این قسمت 
آن را محدود کر ده است. کمر آفتاب: خطی 
که بر مرکز آفتاب گذرد همچو محور. کمر
```


## [2026-09-06T15:52:56.336Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"kamsr\\|kamar[aä]\\|kamr\\|kamere\" BRT.txt | head -8; echo \"---\"; grep -n -o \"kam[a-zäöü]\\{2,8\\}\" BRT.txt | sort -u -t: -k2 | head -20"
}
```


### [2026-09-06T15:52:58.061Z] TOOL RESULT

```
5034:•  p.  ava'dä  {'da')  '\  j.  ava'8a  Adv.  i)  'dort, da':  \ patigrabanä  näma"  vardanam  . .  "da kamaranam  akunaus  Bh,  j.  ij  7,  9,  10, 2.6— 11^  16; — imaiy  martiyä  tyaiy  *ada- kly(sA.)  'da  aha''ta  Bh.4. 18;  j.  18',  2.  3, 6,J.4, 11,5.4;  —  didä  ..  'dasim  aväjanam Bh,  /.  13;  5. 1,  J.8'';  II  —  kva  .  .  °äa  bä  , . asne  hamsrihät  "wo  .  .  ?  .  .  dort  . ."  H.  2. 20,  *Vyt.54;  Yt6'.47>  Jp- 93>  N./5,  2^'; —  ''ha  agtaha  altahe  syao%nahe  ,  .  V.  4. 50.  a)  II  halä  avadas<^'''>  'von  da  aus': kami  udapatalä  bäbirauv  dubälJ"  namä" dahyäu/  halä  av  hauv  udapatata  Bh._j. 13;  J,  11;  —  hauv  . .  aÜyavaf"  paisiya- ^uvSdiim  haiä  av'  käram  *äyasatä  hyä''- param  *aif..  Bh.j.7  I ,  a)  'dorthin,  da- hin': U  raxa  rtSma!'  vardanam . .  'da  hauv .  .  *ä//Bh._y.6;  1. 19,  2.13;  — fravaSayS
10961:•  j.  x$va$.aSi-  Adj.  'mit  sechs  Augen': ailm  äahskim  ..  "hrikamsr^im  'sXm  Y.g.8.
13692:äsnaila  zbayantsi  'ratca  Yt.  77.  * ;  ■ — ■  nara . .  ya  nasaum  avaJiUta  'ire  asahi  rasan- hqm  (sd.)  V.Ä'.g?;  YX.i4.^l\  —  Wp^r- sahyü  .  .  ari'tii  'raiy'''  paragmatä  "des Persers  Speer  ist  fernhin  gekommen"  D. ff.  4;  —  mit  Abi:  agibyS  'in  voha  as mand  (sd.)  Y.J4.  8.  a)  |  in  Verbindung mit  apiy  (sd.):  ahyäyä  bümiya  'raiapiy  D. 6.3;  X.I.3  (wo  'raiy  apty): —  mit  Aacä und  Abi.:  pSrs<^  marliytr  *'rayapiy''> hacä  pärsS^  kamaram  paliyajatä  D.  6. 4.  2)  Abis,  'von   fem;  fem;    femhin,
14582:■  j.  (hi-kamsrvJa-  Adj.  'imt  drei  Köpfen': azTm  daAahm  . .  'hm'^  'x^a/jtitrn  (sd.) Y.  5.  8.
16336:der  (behaarten)  Haut  sva.  soweit  die  (be- haarte) Haut  (des  Kopfes)  geht'":/"  hl iam^n^pm  vtnä^ayen  (sd.)  "sie  sollen  ihm den  Kopf  schinden,  soweit  das  Haar  geht" V.J.  zo;  —  yaäia  yal  Ag P'  kamsri^sm hiirpnuyäHSp.452  u.)  "als  ob  er  sich  (selber) den  Kopf  schindele,  soweit  das  Haar  gehl" V. /<?.  10.
19395:—  matyd^  mam  xsnasatiy  Bh.  1. 13.  zu a):  hauv  ai?<^  hadä  kara  patil  mäm kamaranam  cartanaiy  Bh.i.  19;  2.12;  — fravartil    agarbayala    Uta    anayata    abiy
21175:ist  hypothetisch,  soll  aber  als  möglich  hin- gestellt werden  'als  ob':  tuHi  vaT?hS  ahmai fyao%mm  Vimyäti  y  y  hf  pqstsjra%a- tah^m  (sd.)  kamsr^m  kinnuyät  V.  18. io;  N.<^.  b)  die  Aussage  stellt  eine Folge  als  möglich  hin  'so  dass . .  könnte': astiia  ahmi  , .  avavat  kavaem  afannS  y y  i^  anairya  daAhus  hakat  usca  us.' fravayHt  (sd.)  Yt  ig.  6  8.  c)  ohne  Verb, wie  3  a:  avavata  aejanha  y  y  patUa narSV.  15.10  PliZ.  Wertlos:  Vyt.,^5, 13,  20,  25, 34, 37 >  46,  52 ,  Vd.  p.  [Y.
24771:Aar»  vimixiet  pa  kamret;  s.  No.  5,  6.  —  9)  Pü. ;
---
4718:kamahe
5487:kamahya
23778:kamahyä
29637:kamäi
10028:kamäia
27595:kamaica
28164:kamaistär
3884:kamäk
15507:kamaklum
21301:kamakys
16337:kamal
19816:kaman
14276:kamän
29090:kamara
29432:kamaraita
13692:kamaram
5034:kamaranam
13477:kamarg
24994:kamaspahmal
5454:kamaspfiima
```


## [2026-09-06T15:53:38.112Z] AGENT

Now let me copy the page image for the audit trail and write the verification file.


## [2026-09-06T15:53:40.815Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg237.png data/verification/sources/refs/ocr/BOOK/237.png && ls -la data/verification/sources/refs/ocr/BOOK/ | tail -3"
}
```


### [2026-09-06T15:53:42.485Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-06T16:01:59.247Z] TOOL CALL #87: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk237.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_KAMAR = \"https://en.wiktionary.org/wiki/%DA%A9%D9%85%D8%B1\"\nW_CAP   = \"https://en.wiktionary.org/wiki/%DA%86%D9%BE\"\nW_QAPAN = \"https://en.wiktionary.org/wiki/%D9%82%D9%BE%D8%A7%D9%86\"\nE_CAB   = \"https://www.etymonline.com/word/cabaret\"\nW_HIM   = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/himinaz\"\n\ndoc = {\n \"pdf_page\": 237,\n \"book_page\": 207,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [{\n  \"entry\": 0,\n  \"root\": \"Kam 2, Kamer, Kamp, Qam, Qem\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *kam-er- / *kh2em-er- 'to bend, curve; vaulted' (Pokorny 524-525) with the nasal extension *kam-p- 'to bend' (Pokorny 525); Walde-Pokorny set it up as *qam- (qem-?) 'wölben, biegen', 'perhaps only with the r-formant: qamer-'\",\n  \"note\": \"Every one of Nourai's five root labels is a real reconstruction taken from his own sources. Pokorny p.524-525 has 'kam-er-: to bend, curve, vaulted' (material: Skt. kmarati, Av. kamarā, Gk. kamára, Lat. camur(us)) and p.525 'kam-p-: to bend' (Skt. kampate, Gk. kampē, Lat. campus, Goth. hamfs, Lith. kampas), with Pokorny's own remark that 'kamp- is possibly an extension from *kam- \\\"bend, curve\\\"'. The variants 'Qam, Qem' are Klein's notation for the same base (Klein s.v. camera: 'fr. I.-E. base *qam-, *qem-, \\\"to bend, vault\\\"'), and Walde-Pokorny I 349 heads the article 'qam- (qem-?) \\\"wölben, biegen\\\"'. Language label ('Indo-European') and gloss ('to bend, also a cavity, vault') are therefore both correct. The cross-reference to 'Gěu 1: to bend' is Nourai's own; Pokorny keeps geu- 'bend, curve' (p.393 ff.) apart from kam-, and no modern source merges them. The weak links on this chart are not the root but three of its branches: Old Persian (#4), Germanic heaven (#12) and, to a lesser degree, Latin campus (#14).\",\n  \"note_fa\": \"ریشهٔ بازسازی‌شدهٔ نورایی درست است: پوکورنی در صفحه‌های ۵۲۴–۵۲۵ ریشهٔ هندواروپایی آغازین *kam-er- «خمیدن، قوس‌دار» را با گواه‌های سنسکریت kmarati، اوستایی kamarā، یونانی kamára و لاتینی camurus می‌آورد و در ص ۵۲۵ گونهٔ خیشومی‌شدهٔ *kam-p- «خمیدن» را، و خود او یادآور می‌شود که kamp- احتمالاً گسترش *kam- است. گونه‌های «Qam, Qem» نویسهٔ کلاین برای همین ریشه است (کلاین ذیل camera: از پایهٔ هندواروپایی *qam-, *qem-)، و والده‌ـ‌پوکورنی هم مدخل را «qam- (qem-؟) wölben, biegen» نامیده است. بنابراین نام ریشه، برچسب زبانی و معنای «خمیدن، حفره، طاق» هر سه درست است؛ ولی ارجاع نورایی به «Gěu 1» تأییدی در منابع امروزی ندارد.\",\n  \"sources\": [],\n  \"ref_check\": [\n   {\"ref\": \"POK:524\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt l.43424: 'Root / lemma: kam-er- | Meaning: to bend, curve, vaulted | Material: Old Indic kmarati ... Avestan kamarai. [= kamarā-] \\\"belt, girdle\\\" (and \\\"*dome\\\") ... gr. Kopiapa [kamára] \\\"dome ...\\\" (Latin loanword camera, camara \\\"a vault\\\") ... Latin camur(us) \\\"arched, writhed, crooked\\\" ... References: WP. I 349 f. ... Page(s): 524-525.'\"},\n   {\"ref\": \"POK:525\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt l.43443: 'Root / lemma: kam-p- | Meaning: to bend | Material: Old Indic kapana ..., kampate ...; gr. kampē \\\"bend\\\", kamptō \\\"curve, bend\\\", kampylos ...; Latin campus \\\"field\\\" (originally \\\"bend, indentation, lowland, depression\\\") ...; Gothic hamfs \\\"mutilated\\\" ...; Lithuanian kampas \\\"point, edge, angle\\\" ... Indo Germanic kamp- is possibly an extension from *kam- \\\"bend, curve\\\" ... Page(s): 525.'\"}\n  ],\n  \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I 349-350 (WLD_Bd1_pages.txt l.32878-32950)\", \"stance\": \"supports\",\n    \"note\": \"'qam- (qem-?) \\\"wölben, biegen\\\", vielleicht nur mit r-Formans: qamer-. Ai. kmarati ... av. kamara \\\"Gürtel\\\" (und \\\"*Gewölbe\\\") ... gr. kamára \\\"Gewölbe, Himmelbett\\\" ... lat. Lw. camera ... lat. camur -a -um \\\"gewölbt, gekrümmt\\\"'; and p.350 'Idg. qamp- ist möglicherweise eine Erw. von *qam- \\\"biegen, wölben\\\"'. This is exactly Nourai's Kam/Kamer/Kamp/Qam/Qem set.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. kamer- and kamp- (AHD_watkins1985.txt l.578-581)\", \"stance\": \"supports\",\n    \"note\": \"'kamer-. To bend; a vault. 1. Greek kamara, a vault: (CABARET), CAMARILLA, (CAMERA), CHAMBER, (COMRADE) ... 2. Persian kamar, waist, girdle, or something arched: CUMMERBUND. [Pok. kam-er- 524.]' and 'kamp-. To bend. 1. ... Greek kampē ... [Pok. kam-p- 525.]'\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, cols. under kamoros and kampos (IEC.txt l.6706, 6719)\", \"stance\": \"supports\",\n    \"note\": \"'kamoros (kamur-) \\\"bent; arched; bend, arch\\\". WP I, 349. Av. kamarā \\\"belt, vault, arch\\\" ... Gk. kamára \\\"vault, chamber\\\" ... Lat. camarus, camurus'; 'kampos \\\"crooked, bent\\\" ... Lat. campus \\\"plain, field\\\" ... Go. hamfs \\\"maimed\\\" ... Li. kampas \\\"corner\\\"'.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. camera (KLN_1966.txt l.6279)\", \"stance\": \"supports\",\n    \"note\": \"'camera, n. — L. \\\"vault, arched roof, arch\\\", fr. Gk. kamára, which is rel. to kaminos (whence L. caminus) \\\"furnace\\\", and cogn. with L. camur, camurus \\\"curved\\\", fr. I.-E. base *qam-, *qem-, \\\"to bend, vault\\\".' — the source of Nourai's 'Qam, Qem'.\"}\n  ],\n  \"nodes\": []\n }]\n}\n\nN = doc[\"entries\"][0][\"nodes\"]\n\nN.append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"kamarâ\", \"verdict\": \"confirmed\",\n \"derivation\": \"Avestan kamarā- f. 'belt, girdle' (Yasna/Vendidad usage; the girdle later ritualised as the kustīg) is the standard Iranian witness for PIE *kam-er- 'to bend, vault': a *kam- 'bend' + -er- stem, semantically 'the thing that goes round / the encircling band', with the secondary sense '*vault' inferred by Fick and repeated by Pokorny and Walde-Pokorny. Nourai's gloss 'waist, belt, also a vault' reproduces Pokorny's 'belt, girdle (and \\\"*dome\\\")' word for word. Not to be confused with the homophonous Av. kamarəδa- 'head (of daevic beings)', which Bartholomae (Airan. Wb. 440) and Hübschmann keep separate; Nourai correctly does not import it.\",\n \"derivation_fa\": \"واژهٔ اوستایی kamarā- «کمربند، شال کمر» (همان بندی که بعدها در آیین زردشتی «کُستی» شد) گواه اصلی ایرانیِ ریشهٔ هندواروپایی *kam-er- «خمیدن، طاق‌زدن» است: ستاک *kam- به‌همراه پسوند -er-، با معنای آغازینِ «آنچه گرداگرد چیزی می‌پیچد». معنای دومِ «طاق، گنبد» را فیک بازسازی کرده و پوکورنی و والده‌ـ‌پوکورنی همان را آورده‌اند؛ پس شرحِ نورایی «کمر، کمربند و نیز طاق» درست است. این واژه را نباید با kamarəδa- اوستایی به معنی «سرِ دیوان» یکی گرفت؛ بارتولومه و هوبشمان آن دو را جدا می‌دانند و نورایی نیز آن را نیاورده است.\",\n \"sources\": [W_KAMAR],\n \"ref_check\": [{\"ref\": \"POK:524\", \"status\": \"supports\",\n   \"note\": \"POK_full.txt l.43429: under 'kam-er-' — 'Avestan kamarai. [OCR for kamarā-] \\\"belt, girdle\\\" (and \\\"*dome\\\")'. Exactly the node's claim.\"}],\n \"consulted\": [\n  {\"src\": \"HRN\", \"where\": \"no. 866, p.194 (HRN.txt leaf 215)\", \"stance\": \"supports\",\n   \"note\": \"'866. (1) kemer \\\"Gürtel\\\", kemra; aw. kamara- \\\"Gürtel\\\"; phlv. kamar, LW. kurd. kemer \\\"Gürtel\\\", afγ. kamar; oss. LW. d. kamări \\\"Frauengürtel\\\".' Horn puts the Avestan word at the head of the Persian entry.\"},\n  {\"src\": \"BRT\", \"where\": \"Altiranisches Wb. col. 439-440\", \"stance\": \"not_found\",\n   \"note\": \"grep 'kamar' / 'kamere' in BRT.txt returns only OCR-mangled Old Persian hamaranam and Av. kamərəδa- ('Kopf', e.g. l.14582 'θri-kamərəδa- Adj. \\\"mit drei Köpfen\\\"'); the kamarā- 'Gürtel' entry itself could not be located in this OCR. WLD I 349 cites Bartholomae Airan. Wb. 440 for the separate kamarəδa-.\"},\n  {\"src\": \"IEC\", \"where\": \"Mann, s.v. kamoros (IEC.txt l.6706)\", \"stance\": \"supports\",\n   \"note\": \"'Av. kamarā \\\"belt, vault, arch\\\"; kamar-, v. \\\"be bent, arched\\\"; Iran. LW in Tk. kemer \\\"arch\\\"'.\"},\n  {\"src\": \"ARY\", \"where\": \"Aryanpur, pdf p.408 (ARY_pages.txt leaf 408)\", \"stance\": \"supports\",\n   \"note\": \"note under the کمر entry: 'چم این واژه در اوستایی و اوستی و کردی: کمربند، تسمه؛ چم این واژه در سانسکریت: خمیده، قوس‌دار؛ چم این واژه در زبان‌های یونانی و رومانس: هرچیز دارای سرپوش یا طاق قوس‌دار'.\"}\n ]\n})\n\nN.append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"kamar «کمر»; kamrâ «کمرا»\", \"verdict\": \"plausible\",\n \"derivation\": \"kamar «کمر» 'waist, belt' is the regular continuant: Av. kamarā- > Old Iranian *kamarā- > Middle Persian kamar (MacKenzie, Concise Pahlavi Dict. p.50: 'kamar [kml | N ~] waist; belt, girdle. ~-band [-bnd] belt') > NP kamar, with the compound کمربند kamar-band already Middle Persian. Wiktionary (after Edelman, ESIJa IV 191) gives exactly this chain and adds Manichaean MP qmr /kamar/ 'vault', so that the Persian word carries the 'arch, cupola, arched bridge' sense too — which is why the Persian entry can also mean 'the middle of a mountain'. kamrâ «کمرا» 'high-ceilinged room, stable' is weaker: Hübschmann, Pers. Stud. no.867 (p.88) calls np. kamra 'Gewölbe, Stall' a LOANWORD ('np. LW. kamra', after Nöldeke) beside Arm. kamar 'Gewölbe' = Gk. kamára = Lat. camera, and says the relation of all this to np. kamar is 'mir unklar'; Mo'in's footnote 9 to Borhan p.1694 says the same — Manichaean Pahlavi kmr' 'طاق، گنبد', Armenian and Persian kamara 'از آرامی' — while adding that the Aramaic is itself from Persian kamar. So kamrā is at best a doublet re-imported through Aramaic/Greek, not a straight descendant of Av. kamarā-, and the single arrow of the chart flattens that.\",\n \"derivation_fa\": \"«کمر» دنبالهٔ منظمِ اوستایی kamarā- است: ایرانی باستان *kamarā- ← فارسی میانه kamar (مکنزی ص ۵۰: kamar «کمر، کمربند»، kamar-band) ← فارسی نو کمر؛ ترکیب «کمربند» نیز از دورهٔ میانه به‌جا مانده است. در فارسی میانهٔ مانوی صورت qmr به معنی «طاق» هم آمده، و از همین‌روست که «کمر» معنای «طاق، گنبد، میانهٔ کوه» هم دارد. اما دربارهٔ «کمرا» (اتاق بلند، طویله) هوبشمان در «مطالعات فارسی» بند ۸۶۷ آن را وام‌واژه می‌داند (کنار ارمنی kamar، یونانی kamára، لاتینی camera) و پیوندش را با «کمر» ناروشن می‌خواند؛ حاشیهٔ معین بر برهان قاطع ص ۱۶۹۴ (پانوشت ۹) نیز آن را «از آرامی» می‌داند، هرچند می‌افزاید که آرامی خود از «کمرِ» فارسی گرفته است. پس «کمرا» بیشتر دوگانه‌ای است که از راه آرامی/یونانی بازگشته، نه بازماندهٔ مستقیم اوستایی؛ ادعای نورایی دربارهٔ «کمر» درست و دربارهٔ «کمرا» با احتیاط پذیرفتنی است.\",\n \"sources\": [W_KAMAR],\n \"ref_check\": [\n  {\"ref\": \"BQT:1694\", \"status\": \"supports\",\n   \"note\": \"Borhan-e Qate' vol.3 printed p.1694 (pdf p.487, cached at sources/refs/ocr/BQT/1694.txt): headwords «کمر» ('معروف است که میان باشد ... و آنچه را یک دور بر میان بندند از ابریشم و زر و نقره مانند حلقه و طوقی ... و میانهٔ کوه را نیز گویند') and «کمرا» ('محوطه‌ای را گویند که شب‌ها چهارپایان و ستوران را در آن کنند ... و طاق بلند را نیز گویند'), with Mo'in's footnote 6 'پهلوی kamar (کمربند)، اوستا kamarā (کمربند)، کردی kemer، افغانی kamar' and footnote 8 quoting the very verse of Aʿmaq Boxārāʾī printed in the chart ('چو گرگ ظلم را کشتی بزور بازوی عدلت / ز انبوهی شده صحرای اقلیم تو چون کمرا').\"},\n  {\"ref\": \"MON:3068\", \"status\": \"not_checked\",\n   \"note\": \"The 6-volume Mo'in is not digitised; the page cannot be opened. The alphabetical position is consistent (کاباره 2777 < کپان 2896 < کمر 3068). The 2-volume Adena abridgement (MON_part2.txt l.26348) has کمر but only with an anatomical definition and no etymological tag.\"}\n ],\n \"consulted\": [\n  {\"src\": \"PHD\", \"where\": \"MacKenzie p.50 s.v. kamar (PHD.txt l.424)\", \"stance\": \"supports\",\n   \"note\": \"'kamar [kml | N —] waist; belt, girdle. ~-band [-bnd | N ~] belt.' The Middle Persian link Nourai leaves implicit.\"},\n  {\"src\": \"HRN\", \"where\": \"Horn no. 866, p.194\", \"stance\": \"supports\",\n   \"note\": \"'(1) kemer \\\"Gürtel\\\", kemra; aw. kamara- \\\"Gürtel\\\"; phlv. kamar' — Horn keeps kamar and kamrā in one entry, i.e. supports the node as drawn.\"},\n  {\"src\": \"HUB\", \"where\": \"Hübschmann, Pers. Studien no. 867, p.88 (HUB.txt l.3111-3117)\", \"stance\": \"partial\",\n   \"note\": \"'Das Verhältnis von np. kamar \\\"altitude, collis, tumulus, saxum\\\" ... zu arm. kamar \\\"Gewölbe, Bogen, Kuppel, Halle\\\" = gr. kamára ... = lat. camera, np. LW. kamra \\\"Gewölbe, Stall\\\" (Nöldeke, Pers. Stud. II, p.40) ist mir unklar.' — kamrā explicitly marked a loanword.\"},\n  {\"src\": \"MON\", \"where\": \"2-vol. abridgement, s.v. کمر (MON_part2.txt l.26348)\", \"stance\": \"silent\",\n   \"note\": \"Only the anatomical sense, no origin tag; the abridgement drops Mo'in's etymologies.\"}\n ]\n})\n\nN.append({\n \"id\": 3, \"lang\": \"English\", \"words\": \"cummerbund, kummerbund\", \"verdict\": \"confirmed\",\n \"derivation\": \"Not a direct loan from Persian into English but the classic Anglo-Indian route: Persian کمربند kamar-band 'loin-band' passed into Hindustani/Urdu کمر بند (Urdu kamar first attested c.1635), and British residents in India picked it up in the 17th c. — first recorded in English 1616 as 'combarbands'. Hobson-Jobson s.v.: 'CUMMERBUND, s. A girdle. H. from P. kamar-band, i.e. \\\"loin-band\\\". Such an article of dress is habitually worn by domestic servants, peons, and irregular troops.' The variant kummerbund is only a different transliteration of the same Urdu word (Klein: 'kummerbund, n. — See cummerbund'). AHD's appendix files it under kamer- (waist) and bhendh- (band), which is precisely the two halves of the compound.\",\n \"derivation_fa\": \"«کمربند» فارسی از راه هندوستان به انگلیسی رفته است، نه مستقیم: kamar-band فارسی نخست به اردو/هندی راه یافت و سپس انگلیسیان هند در سدهٔ ۱۷م آن را گرفتند (نخستین ضبط انگلیسی ۱۶۱۶م به‌صورت combarbands). یول و برنل در «هابسن‌ـ‌جابسن» می‌نویسند: «CUMMERBUND، کمربند؛ از هندی، برگرفته از فارسی kamar-band یعنی بندِ میان». گونهٔ kummerbund تنها آوانگاری دیگری از همان واژه است. فرهنگ AHD نیز آن را زیر دو ریشهٔ kamer- (کمر) و bhendh- (بستن) می‌آورد که همان دو جزء ترکیب است. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\",\n   \"note\": \"Watkins 1985 s.v. kamer- (l.578): '2. Persian kamar, waist, girdle, or something arched: CUMMERBUND'; and s.v. bhendh- (l.332): '5. Persian band ...: BUND; CUMMERBUND'; index l.1402 'CUMMERBUND bhendh-, kamer-'.\"}],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"s.v. cummerbund (KLN_1966.txt l.9914)\", \"stance\": \"supports\",\n   \"note\": \"'cummerbund, n., waistband (Anglo-Ind.) — Hind.-Pers. kamar-band, fr. Pers. kamar, \\\"waist, loins\\\", and band, \\\"band, bandage\\\".'\"},\n  {\"src\": \"HJB\", \"where\": \"Hobson-Jobson s.v. CUMMERBUND (HJB.txt l.7958)\", \"stance\": \"supports\",\n   \"note\": \"'CUMMERBUND, s. A girdle. H. from P. kamar-band, i.e. \\\"loin-band\\\".'\"},\n  {\"src\": \"WEB\", \"where\": \"Webster's New 20th Cent. vol.1 (WEB_vol1.txt l.104393)\", \"stance\": \"supports\",\n   \"note\": \"'kum/mer-bund, n. same as cummerbund' — confirms the doublet spelling printed in the chart.\"}\n ]\n})\n\nN.append({\n \"id\": 4, \"lang\": \"Old Persian\", \"words\": \"kanpa; čam\", \"verdict\": \"disputed\",\n \"derivation\": \"Neither form is attested Old Persian. Kent's Old Persian lexicon has kamna- 'few', kāma- 'desire', kan- 'to dig' — no kanpa and no čam (grep of KNT.txt); the Achaemenid corpus simply does not contain them. 'kanpa' is Nourai's own back-formation from the nasal-infix family Pokorny lists under kam-p- (Skt. kampate, Gk. kampē, Lith. kampas), i.e. a Proto-Indo-European/Proto-Iranian *kamp-, not an Old Persian word; Cheung's Iranian verb dictionary does set up a root *kamp 'to bend' but its witnesses are Parthian nkmb- 'to bend', Sogdian nk'np-, Chorasmian m|'kfs-, never Old Persian. 'čam' is likewise a Proto-Iranian root, attested in Parthian čm- 'to walk, move to' (Cheung *čam 'to walk'), and Abolghasemi (FFD p.48) derives NP چمیدن from 'پهلوی اشکانی čam < ایرانی باستان *čam' — Old Iranian, i.e. the common ancestor, not Old Persian. Its meaning in the sources is 'to walk/move', not 'to bend'. The node's NOTE comparing Av. xumba 'bent' is separate: Bartholomae's xumba- is a jar/pot word, and Mo'in's footnote to Borhan p.768 links it to خنب/خمب, not to kam-.\",\n \"derivation_fa\": \"هیچ‌یک از این دو صورت در پارسی باستان گواهی نشده است. در واژه‌نامهٔ کنت تنها kamna- «اندک»، kāma- «کام» و kan- «کندن» هست و نه kanpa و نه čam. صورت *kanp- بازسازی خودِ نورایی از خانوادهٔ خیشومی‌شدهٔ *kam-p- پوکورنی است (سنسکریت kampate، یونانی kampē، لیتوانیایی kampas)؛ چونگ نیز ریشهٔ ایرانیِ *kamp «خمیدن» را می‌پذیرد ولی گواهانش پارتی nkmb-، سغدی nk'np- و خوارزمی است، نه پارسی باستان. čam هم ریشه‌ای ایرانی باستان است که در پارتی čam- «رفتن، حرکت کردن» دیده می‌شود؛ ابوالقاسمی (ص ۴۸) «چمیدن» را از «پهلوی اشکانی čam ← ایرانی باستان *čam» می‌گیرد و معنای آن را «رفتن/دویدن» می‌داند نه «خمیدن». بنابراین برچسبِ «پارسی باستان» و نیز معنای «خمیدن» برای čam نادرست است؛ درست آن است که این دو را «ایرانی باستان (بازسازی‌شده)» بنامیم.\",\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"POK:524,525\", \"status\": \"partial\",\n   \"note\": \"Pokorny 524-525 gives kam-er- and kam-p- with Indic, Greek, Latin, Germanic and Baltic material and (under kam-p-) 'npers. čap \\\"left\\\"', but has no Old Persian forms at all and no kanpa or čam. The pages support the root, not the language label of this node.\"}],\n \"consulted\": [\n  {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon (KNT.txt, grep 'kan-|kam-|kamna')\", \"stance\": \"contradicts\",\n   \"note\": \"Only kan- 'dig' (akaniya 'was dug', kantanaiy 'to dig'), kamna- 'few' (kamnam, kamnaibiš), kāma- 'desire'; no kanpa, no čam anywhere in the Old Persian lexicon.\"},\n  {\"src\": \"CHEUNG\", \"where\": \"s.vv. *kamp 'to bend' and *čam 'to walk' (CHEUNG.txt l.15380 ff., l.3278 ff.)\", \"stance\": \"partial\",\n   \"note\": \"'*kamp \\\"to bend\\\" — PARTHIAN (+ *ni-) nkmb- \\\"to bend\\\"; SOGDIAN ...; NWIR (?) NP čamidan \\\"to twist, bend\\\", NP čaftah \\\"curved, bent, a vaulted roof\\\"' [PIE? LIV 342 | Pok. 525]; and separately '*čam ? \\\"to walk\\\" — PARTHIAN čm- \\\"to walk, move to\\\"; NP čamidan \\\"to walk proudly\\\" ... This sparingly attested root does not have an IE origin'. Iranian, but Parthian/Sogdian, never Old Persian.\"},\n  {\"src\": \"FFD\", \"where\": \"Abolghasemi p.48 (FFD_pages.txt pdf p.53)\", \"stance\": \"partial\",\n   \"note\": \"'چمیدن ... چم < پهلوی اشکانی čam < ایرانی باستان *čam ... در پهلوی اشکانی و ایرانی باستان «دویدن» معنی می‌دهد' — Old Iranian *čam, glossed 'to run/walk', not 'to bend', and not Old Persian.\"}\n ]\n})\n\nN.append({\n \"id\": 5, \"lang\": \"Persian\",\n \"words\": \"čapeh «چپه»; čap «چپ»; čafteh «چفته»; čamîdan 1 «چمیدن»; xam «خم ۲»\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Four of the five words belong here; one does not. (a) čap «چپ» 'left' is the textbook case: Walde-Pokorny I 350 and Pokorny 525 cite it under kam-p- itself — 'die nasallose gleichbedeutende Sippe von ai. cāpa- \\\"Bogen\\\", capala- \\\"unstet\\\", np. čap \\\"link\\\", d.i. \\\"*krumm\\\"' — and Wiktionary (2026) derives it from PIE *kep- 'to bend', 'a possibly dialectal combination of *kh2emp- + *(s)kamb-', cognate with Skt. cāpa- 'bow', capala-. (b) čapeh «چپه» 'turned over' is the same stem with the adjectival -a(h). (c) čafteh «چفته» 'bent, vaulted' is listed by Cheung under his Iranian root *kamp 'to bend' ('NP čaftah \\\"curved, bent, a vaulted roof\\\"'), and Borhan (p.620 ff.) treats چفت/چفته in the same family. (d) xam «خم» 'a curve' with خمیدن/خماندن: Horn, Grundriss no.446 (p.99) puts it explicitly in this root — 'Zu derselben Wurzel wird übrigens auch np. xam, xamm (*xamp) ... \\\"krumm, gebogen\\\", xamīdan etc. gehören' — beside čap (no.435) and Gk. kamptō, kampylos; the x- for expected k- is what makes the word irregular and is why Horn reconstructs *xamp. Borhan p.768 defines خم as 'ضد راست است که کج باشد ... و کجی و چفتگی چیزها را نیز گویند'. (e) čamīdan 1 «چمیدن» glossed 'walk flauntily' is the disputed one: Cheung splits the material, giving 'NP čamidan \\\"to twist, bend\\\"' to *kamp but 'NP čamidan \\\"to walk proudly\\\"' (with Parthian čm-, Bal. čamit) to a separate root *čam 'to walk' which 'does not have an IE origin and may be a blend of *čar(H) and *gam', and Abolghasemi p.48 derives چمیدن from Parth. čam < Old Iranian *čam 'to run/walk'. Borhan p.661 does give چمیدن both senses ('خرامان راه رفتن ... و بپیچیدن و خم شدن هم آمده است'), which is how Nourai (and Horn's tradition) came to file the 'walk' verb here; but on the modern view the strutting verb and the bending verb are homonyms from different roots. The extras چمبر/چنبر 'hoop' are supported: Horn no.446 derives čanbar (phlv. čambar 'head-fillet') from the same root as čap.\",\n \"derivation_fa\": \"از پنج واژهٔ این خانه چهارتا در جای خود است و یکی نه. «چپ» را والده‌ـ‌پوکورنی (ج۱ ص ۳۵۰) و پوکورنی (ص ۵۲۵) خودشان زیر همین ریشه آورده‌اند: «خانوادهٔ بی‌خیشومِ هم‌معنا: سنسکریت cāpa- «کمان»، capala- «ناپایدار»، فارسی نو čap «چپ» یعنی «کج»»؛ ویکی‌واژه نیز آن را از *kep- «خمیدن»، آمیزه‌ای از *kh₂emp- و *(s)kamb-، می‌گیرد. «چپه» همان ستاک با پسوند صفتی است. «چفته» را چونگ زیر ریشهٔ ایرانی *kamp می‌آورد («NP čaftah: خمیده، طاق ضربی»). «خم» و «خمیدن/خماندن» را هرن در بند ۴۴۶ (ص ۹۹) صریحاً به همین ریشه می‌بندد: «np. xam، xamm (*xamp) «کج، خمیده» و xamīdan نیز به همین ریشه تعلق دارند»، در کنار čap (بند ۴۳۵) و یونانی kamptō؛ «خ» به‌جای «ک» بی‌قاعده است و برای همین هرن *xamp بازسازی می‌کند. برهان قاطع ص ۷۶۸ نیز خم را «ضد راست ... کجی و چفتگی چیزها» می‌داند. اما «چمیدن ۱» به معنی «خرامیدن» جای بحث دارد: چونگ آن را از ریشهٔ جداگانهٔ *čam «راه رفتن» (پارتی čm-) می‌گیرد که ریشهٔ هندواروپایی ندارد، و ابوالقاسمی هم آن را از «پهلوی اشکانی čam» می‌داند؛ هرچند برهان قاطع (ص ۶۶۱) برای چمیدن هم «خرامان راه رفتن» و هم «بپیچیدن و خم شدن» را آورده و همین سبب اشتباه شده است. پس ریشه‌شناسی امروزی «چمیدنِ خرامیدن» را از این ریشه جدا می‌کند.\",\n \"sources\": [W_CAP],\n \"ref_check\": [\n  {\"ref\": \"POK:525\", \"status\": \"supports\",\n   \"note\": \"POK_full.txt l.43480 under kam-p-: 'compare also the nasalized equal meaning family of Old Indic capa- \\\"bow\\\", capala- \\\"restless, fluctuating\\\", npers. čap \\\"left\\\", i.e. \\\"*crooked\\\"'.\"},\n  {\"ref\": \"BQT:620\", \"status\": \"supports\",\n   \"note\": \"Borhan vol.2 printed p.620 (BQT_v2_pages.txt leaf 79) = 'بیان سوم: در جیم فارسی با بای فارسی', headword «چپ»: 'بفتح اول و سکون ثانی، معروف است ... و رونده‌گی را نیز گویند'; the same page carries چپات، چپاول، چپه.\"},\n  {\"ref\": \"BQT:658\", \"status\": \"supports\",\n   \"note\": \"Borhan vol.2 p.658 (leaf 117): «چمان» 'بفتح اول بر وزن روان، راه رفتن به ناز و خرامیدن به زیبایی' and «چماند»/«چماندن», footnote 5 'مشتق از چمیدن است' — the two extras چماندن، چمان of the chart.\"},\n  {\"ref\": \"BQT:661\", \"status\": \"supports\",\n   \"note\": \"Borhan vol.2 p.661 (leaf 120): «چمیدن» 'بر وزن رسیدن، بمعنی خرامان براه رفتن باشد ـ و بمعنی میل کردن ـ و برگشتن ـ و بپیچیدن و خم شدن هم آمده است'; the same leaf begins 'بیان نوزدهم ... جیم فارسی با نون' with چنبر.\"},\n  {\"ref\": \"BQT:768\", \"status\": \"supports\",\n   \"note\": \"Borhan vol.2 p.768 (leaf 227) = 'بیان شانزدهم: در خای نقطه‌دار با میم', headword «خم»: '[ضد] راست است که کج باشد ـ و کجی و چفتگی چیزها را نیز گویند همچو خمیده و طاق ایوان'.\"},\n  {\"ref\": \"BQT:1439\", \"status\": \"not_found\",\n   \"note\": \"Borhan vol.3 printed p.1439 (pdf p.232, cached at sources/refs/ocr/BQT/1439.txt) is the ف section — فتالیدن، فتریدن، فتراک، فتن، فتنه. Nothing on this page relates to چپ/چفته/چمیدن/خم. The other four BQT pages of this node matched exactly, so the pagination is right and 1439 is a stray citation.\"},\n  {\"ref\": \"HRN:99\", \"status\": \"supports\",\n   \"note\": \"Horn, Grundriss no.446 (printed p.99, HRN.txt leaf 121): 'čanbar ... Zu np. čap \\\"links\\\" (No. 435), gr. kamptō \\\"biege\\\", kampylos (Nöldeke). Fick setzt als Wurzel für ai. capa- und gr. kamptō \\\"qep\\\" an. Zu derselben Wurzel wird übrigens auch np. xam, xamm (*xamp) ... \\\"krumm, gebogen\\\", xamīdan etc. gehören.' Covers čap, čanbar and xam/xamīdan in one breath.\"},\n  {\"ref\": \"FFD:48\", \"status\": \"partial\",\n   \"note\": \"Abolghasemi p.48 (pdf p.53) s.v. چمیدن: 'چم < پهلوی اشکانی čam < ایرانی باستان *čam' with the note (top of p.49) that in Parthian and Old Iranian it means 'دویدن'. It supports a root for چمیدن, but a *čam- 'to walk/run', not the bend-root of this chart.\"}\n ],\n \"consulted\": [\n  {\"src\": \"WLD\", \"where\": \"Bd. I 350 (WLD_Bd1_pages.txt l.32983)\", \"stance\": \"supports\",\n   \"note\": \"under qamp-: 'doch vgl. auch die nasallose gleichbed. Sippe von ai. cāpa- m. n. \\\"Bogen\\\", capala- \\\"unstet, schwankend\\\", np. čap \\\"link\\\", d. i. \\\"*krumm\\\" (Horn Np. Et. 97 ...)'.\"},\n  {\"src\": \"CHEUNG\", \"where\": \"s.vv. *kamp and *čam (CHEUNG.txt l.15395, l.3278)\", \"stance\": \"partial\",\n   \"note\": \"*kamp 'to bend' claims 'NP čamidan \\\"to twist, bend\\\", NP čaftah \\\"curved, bent, a vaulted roof\\\"' — supports čafteh; but the strutting verb 'NP čamidan \\\"to walk proudly\\\"' is put under a different root *čam 'to walk' with no IE origin.\"},\n  {\"src\": \"PHD\", \"where\": \"MacKenzie (PHD.txt, grep 'xam', 'čam')\", \"stance\": \"silent\",\n   \"note\": \"No Middle Persian xam or čam verb in the Concise Pahlavi Dictionary's headword list (kaman 'bow', kamar 'waist' are there); the Persian words are first documented in New Persian.\"},\n  {\"src\": \"ARY\", \"where\": \"Aryanpur (ARY_pages.txt, leaves 205, 298, 414 for چپ)\", \"stance\": \"silent\",\n   \"note\": \"The چپ material found in ARY belongs to unrelated entries (Latin 'to stuff', Old Icelandic 'hill'); no entry connecting چپ to *kamp was located in this OCR.\"}\n ]\n})\n\nN.append({\n \"id\": 6, \"lang\": \"Greek\", \"words\": \"kamara; kaminos\", \"verdict\": \"plausible\",\n \"derivation\": \"kamára 'vaulted chamber, covered wagon, four-poster' is the Greek member of kam-er- and is beyond dispute (Pokorny 524, WP I 349, Mann kamoros, Klein s.v. camera); Herodotus already has kamárē. Two caveats. (i) Fick and others suspected the Greek word of being an Iranian culture-loan (WP I 349: 'wo auch über iran. Lehnformen im gr. Kulturkreis'), and Solmsen proposed a Carian origin — both mentioned and both rejected by Pokorny/WP for the Latin forms at least, so 'inherited cognate' remains the majority view. (ii) kaminos is much weaker: it means 'oven, furnace, kiln', NOT 'fire' as the chart glosses it, and Pokorny admits it only with reservation ('at most kaminos \\\"oven\\\"; certainly this could have derived from a culture word'), while WP I 349 adds that a connection with Slavic kamy 'stone' (i.e. the *ak-/kem- 'stone' root) is 'erwägenswert'. Watkins's AHD entry kamer-, which is the reference cited here, lists kamára only and no kaminos. Klein, however, does state that kamára 'is rel. to kaminos (whence L. caminus)'.\",\n \"derivation_fa\": \"kamára یونانی «طاق، اتاق طاق‌دار، ارابهٔ سرپوشیده» عضو بی‌چون‌وچرای این ریشه است (پوکورنی ۵۲۴، والده‌ـ‌پوکورنی ج۱ ص ۳۴۹، مان، کلاین)؛ هرودوت صورت kamárē را دارد. دو نکته: نخست آنکه فیک این واژه را وام‌واژهٔ ایرانی در حوزهٔ فرهنگی یونان می‌دانست و زولمزن ریشهٔ کاریایی برایش پیشنهاد کرده بود، ولی رأی غالب همان هم‌ریشگی است. دوم آنکه kaminos معنایش «تنور، کوره» است نه «آتش»، و پوکورنی آن را «دست‌بالا» به این ریشه می‌بندد و می‌افزاید که ممکن است واژه‌ای فرهنگی و مهاجر باشد؛ والده‌ـ‌پوکورنی پیوند آن را با kamy اسلاوی «سنگ» شایستهٔ درنگ می‌داند و واتکینز در AHD (همان مأخذی که نورایی گواه گرفته) زیر kamer- تنها kamára را آورده است. پس این خانه با احتیاط پذیرفتنی است و معنای «آتش» برای kaminos نادرست است.\",\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"partial\",\n   \"note\": \"Watkins 1985 s.v. kamer- (l.578): '1. Greek kamara, a vault: (CABARET), CAMARILLA, (CAMERA), CHAMBER ...' — kamára yes, kaminos not mentioned under this root anywhere in the appendix.\"}],\n \"consulted\": [\n  {\"src\": \"POK\", \"where\": \"p.524-525 s.v. kam-er- (POK_full.txt l.43432-43438)\", \"stance\": \"partial\",\n   \"note\": \"'gr. kamára \\\"dome, four-poster bed; covered cart\\\" ... (Latin loanword camera ...); at most kaminos \\\"oven\\\" (certainly this could have derived from a culture word)'.\"},\n  {\"src\": \"WLD\", \"where\": \"Bd. I 349\", \"stance\": \"partial\",\n   \"note\": \"'allenfalls kaminos \\\"Ofen\\\" (freilich Kulturwort, das gewandert sein könnte; Beziehung zu slav. kamy \\\"Stein\\\" ... ist erwägenswert)'.\"},\n  {\"src\": \"KLN\", \"where\": \"s.v. camera (KLN_1966.txt l.6279)\", \"stance\": \"supports\",\n   \"note\": \"'L. \\\"vault, arched roof\\\", fr. Gk. kamára, which is rel. to kaminos (whence L. caminus), \\\"furnace\\\"' — Klein does join the two, but glosses kaminos 'furnace', not 'fire'.\"},\n  {\"src\": \"IEC\", \"where\": \"Mann s.v. kamoros (IEC.txt l.6706)\", \"stance\": \"supports\",\n   \"note\": \"'Gk. kamára \\\"vault, chamber\\\": LW in Arm. kamar'.\"}\n ]\n})\n\nN.append({\n \"id\": 7, \"lang\": \"Latin\", \"words\": \"camera; caminus\", \"verdict\": \"confirmed\",\n \"derivation\": \"Both Latin words are straightforward borrowings from Greek, as the chart draws them. Ernout-Meillet: 'camera, -ae f. (camara ...): toiture voûtée, voûte ... Emprunt latinisé au gr. kamára. Classique, usuel'; and 'caminus, -i m.: four. Emprunt au gr. kaminos, correspondant au lat. fornax. Terme technique, fréquent surtout dans la langue de l'Église et dans les langues de métiers (potier, forgeron)'. Latin camera then feeds the whole Romance family (It./Sp./Cat. camera/cámara, Fr. chambre, OHG chamara, OCS komora, Lith. kamara, OIr. camra — Klein). Pokorny notes that beside the loan Latin also has an inherited cognate camur(us) 'arched, crooked', which is why the borrowing did not feel foreign. Nourai's gloss of caminus as 'hearth' is right for the classical use (Vergil's caminus = forge/hearth).\",\n \"derivation_fa\": \"هر دو واژهٔ لاتینی وام‌واژهٔ یونانی‌اند، درست همان‌گونه که نمودار نشان می‌دهد. ارنو و مه‌یه می‌نویسند: «camera: سقف طاق‌دار، طاق ... وام‌واژهٔ لاتینی‌شده از یونانی kamára» و «caminus: کوره؛ وام‌واژه از یونانی kaminos، هم‌ارز fornax لاتینی، اصطلاحی فنی و بسیار پرکاربرد در زبان کلیسا و پیشه‌ها (سفالگر، آهنگر)». camera لاتینی سپس سرچشمهٔ همهٔ خانوادهٔ رومی است: ایتالیایی/اسپانیایی camera–cámara، فرانسوی chambre، آلمانی علیای کهن chamara، اسلاوی کهن komora. پوکورنی یادآور می‌شود که لاتین در کنار این وام‌واژه صورت موروثی camurus «خمیده» را هم داشته است. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\",\n   \"note\": \"Watkins 1985 s.v. kamer-: Greek kamara gives (CAMERA), CHAMBER, CAMARILLA, (CABARET), (COMRADE) — i.e. the Latin/Romance chain of this node.\"}],\n \"consulted\": [\n  {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.vv. camera, caminus (LAT.txt l.8991, l.9012)\", \"stance\": \"supports\",\n   \"note\": \"'camera ... Emprunt latinisé au gr. kamára. Classique, usuel. M.L.1545'; 'caminus, -i m.: four. Emprunt au gr. kaminos, correspondant au lat. fornax.'\"},\n  {\"src\": \"KLN\", \"where\": \"s.v. camera (KLN_1966.txt l.6279-6280)\", \"stance\": \"supports\",\n   \"note\": \"'Cp. It., OProveng., Catal. camera, Sp. camara, Port. camara, F. chambre, OHG. chamara, OS. camara, OSlav. komora, Lith. kamara, OIr. camra, which all derive fr. L. camera.'\"},\n  {\"src\": \"POK\", \"where\": \"p.524-525\", \"stance\": \"supports\",\n   \"note\": \"'Latin loanword camera, camara \\\"a vault, an arched roof, an arch\\\"' beside genuine Latin camur(us)/camerus.\"}\n ]\n})\n\nN.append({\n \"id\": 8, \"lang\": \"French\", \"words\": \"cabaret; chambre\", \"verdict\": \"plausible\",\n \"derivation\": \"chambre is impeccable: Latin camera > Vulgar Latin *camra > Old French chambre (with the regular Gallo-Romance ca- > cha- palatalisation and the intrusive -b- in the -mr- cluster), attested since the 11th c. cabaret is the loose link: it is not a French continuation of camera at all but a re-import — French cabaret 'tavern' (13th c.) was borrowed from Middle Dutch cabret, itself denasalised from cambret / Old Picard camberete, a diminutive of Picard cambre (= chambre), so 'little room'. Klein: 'cabaret, n. — F., a loan word fr. MDu. cabret, denasalized fr. cambret, camret, fr. OPicard cambrete, dimin. of cambre, \\\"chamber, room\\\"'; Etymonline is more cautious ('of uncertain origin, perhaps from Middle Dutch cambret ...'). So the ultimate source is indeed Latin camera, but the arrow Latin > French hides a Picard-Dutch detour and a diminutive suffix.\",\n \"derivation_fa\": \"«chambre» بی‌عیب است: camera لاتینی ← لاتینی عامیانهٔ *camra ← فرانسوی کهن chambre، با دگرگونی منظمِ ca- به cha- در گالوـ‌رومی و افزودن «b» میان m و r. اما «cabaret» پیوند سست این خانه است: این واژه دنبالهٔ مستقیم camera در فرانسه نیست بلکه واژه‌ای بازگشته است؛ فرانسوی cabaret «میکده» (سدهٔ ۱۳م) از هلندی میانهٔ cabret گرفته شده که خود از cambret و آن از پیکاردی کهن camberete، مصغّرِ cambre (= chambre) یعنی «اتاقک» است. کلاین همین را می‌گوید و اتیمولوجی‌آنلاین محتاطانه‌تر «ریشهٔ نامطمئن، شاید از هلندی میانه» می‌نویسد. پس سرچشمهٔ نهایی همان camera لاتینی است، ولی پیکانِ «لاتین ← فرانسه» یک چرخش پیکاردی‌ـ‌هلندی و یک پسوند تصغیر را پنهان کرده است.\",\n \"sources\": [E_CAB],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\",\n   \"note\": \"Watkins 1985 s.v. kamer- lists (CABARET) and CHAMBER among the descendants of Greek kamara via Latin camera; index l.1328 'CABARET kamer-', l.1342 'CHAMBER kamer-'.\"}],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"s.vv. cabaret and chamber (KLN_1966.txt l.6007, l.7149)\", \"stance\": \"partial\",\n   \"note\": \"'cabaret, n. — F., a loan word fr. MDu. cabret, denasalized fr. cambret, camret, fr. OPicard cambrete, dimin. of cambre \\\"chamber, room\\\", which is rel. to F. chambre'; 'chamber, n. — ME., fr. OF. (= F.) chambre, fr. L. camera.'\"},\n  {\"src\": \"etymonline\", \"where\": \"etymonline.com/word/cabaret\", \"stance\": \"partial\",\n   \"note\": \"'1650s, \\\"tavern, bar, little inn,\\\" from French cabaret, originally \\\"tavern\\\" (13c.), which is of uncertain origin, perhaps from Middle Dutch cambret, from Old French (Picard dialect) camberete, diminutive of cambre \\\"chamber\\\".'\"}\n ]\n})\n\nN.append({\n \"id\": 9, \"lang\": \"Persian\", \"words\": \"kâbâreh «کاباره»\", \"verdict\": \"confirmed\",\n \"derivation\": \"A 20th-century French loan, taken in with the other Parisian entertainment vocabulary (رستوران، بوفه، شامپاین) during and after the Qajar-era contact with France; the ending -eh renders French final -et as pronounced [ɛ], exactly as in بوفه/کاباره/کروکه. Mo'in's dictionary registers it, and the 2-volume abridgement glosses it 'کاباره: میکده، میخانه، مشروب‌فروشی'. Nothing Iranian about the word itself — it is the far end of a loop that started with Greek kamára, so the chart's placement is correct.\",\n \"derivation_fa\": \"«کاباره» وام‌واژه‌ای فرانسوی از سدهٔ بیستم است که همراه دیگر واژه‌های سرگرمی و خوراک پاریسی (رستوران، بوفه، شامپاین) به فارسی راه یافت؛ پایانهٔ «ـه» برابرنهادِ -et فرانسوی است که [ɛ] تلفظ می‌شود، درست مانند «بوفه». معین آن را ثبت کرده و در ویرایش دوجلدی چنین آمده است: «کاباره: میکده، میخانه، مشروب‌فروشی». این واژه هیچ پیشینهٔ ایرانی ندارد و تنها سرِ دیگرِ حلقه‌ای است که از kamára یونانی آغاز شده؛ پس جای‌گذاری نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"MON:2777\", \"status\": \"partial\",\n   \"note\": \"The 6-vol. Mo'in cannot be opened, but the 2-vol. Adena abridgement (MON_part2.txt l.16802) has the entry: 'کاباره: (اِ.) میکده، میخانه، مشروب‌فروشی' — the word and sense the chart cites. The page number 2777 fits the alphabetical run کاباره 2777 < کپان 2896 < کمر 3068.\"}],\n \"consulted\": [\n  {\"src\": \"MON\", \"where\": \"2-vol. abridgement s.v. کاباره (MON_part2.txt l.16802)\", \"stance\": \"supports\",\n   \"note\": \"'کاباره: میکده، میخانه، مشروب‌فروشی' (the abridgement drops the [فر.] origin tag that the 6-vol. print carries).\"},\n  {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' (17th c.)\", \"stance\": \"silent\",\n   \"note\": \"Not in Borhan, as expected of a 20th-century Europeanism; the word cannot predate the French contact.\"}\n ]\n})\n\nN.append({\n \"id\": 10, \"lang\": \"English\", \"words\": \"cabaret, chamber\", \"verdict\": \"confirmed\",\n \"derivation\": \"chamber: Middle English chambre (c.1200) straight from Old French chambre, Latin camera — Klein s.v. chamber. cabaret entered English twice from French: 1650s in the original sense 'tavern, bar, little inn', then again in 1912 in the sense 'restaurant with a floor show', whence 'entertainment, floor show' by 1918 (Etymonline). Both are ordinary French > English borrowings and the chart's French > English arrow is exactly right.\",\n \"derivation_fa\": \"«chamber» از انگلیسی میانهٔ chambre (حدود ۱۲۰۰م) مستقیماً از فرانسوی کهن chambre و آن از camera لاتینی است. «cabaret» دو بار از فرانسه به انگلیسی رفته است: نخست در دههٔ ۱۶۵۰م به معنای «میخانه، مهمانخانهٔ کوچک» و بار دیگر در ۱۹۱۲م به معنای «رستورانِ برنامه‌دار»، و از ۱۹۱۸م به معنی «برنامهٔ نمایشی». هر دو وام‌گیری معمولی فرانسوی به انگلیسی‌اند و پیکانِ «فرانسه ← انگلیسی» درست است.\",\n \"sources\": [E_CAB],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\",\n   \"note\": \"Watkins 1985 index l.1328 'CABARET kamer-' and l.1342 'CHAMBER kamer-'; the kamer- article lists both as descendants of Greek kamara.\"}],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"s.vv. chamber, cabaret (KLN_1966.txt l.7149, l.6007)\", \"stance\": \"supports\",\n   \"note\": \"'chamber, n. — ME., fr. OF. (= F.) chambre ... fr. L. camera'; 'cabaret, n. — F., a loan word fr. MDu. cabret ...'\"},\n  {\"src\": \"etymonline\", \"where\": \"etymonline.com/word/cabaret\", \"stance\": \"supports\",\n   \"note\": \"'It was borrowed again from French with a meaning \\\"a restaurant/night club\\\" in 1912; the extension of meaning to \\\"entertainment, floor show\\\" is by 1918.'\"}\n ]\n})\n\nN.append({\n \"id\": 11, \"lang\": \"English\", \"words\": \"camera, chimney\", \"verdict\": \"confirmed\",\n \"derivation\": \"camera was taken directly from Latin, first as an architectural/legal term and then in 1708+ as camera obscura, the darkened box of the optical experiment, from which the photographic 'camera' (1840s) is an abbreviation — Skeat: 'Camera. (L.) L. camera, a chamber; hence camera obscura, a dark chamber, box for photography; see Chamber.' chimney reaches English through French: Latin caminus 'hearth, forge' > Late Latin (camera) caminata 'room provided with a fireplace' > Old French cheminee > Middle English chimenee > chimney (Klein s.v. chimney; Skeat s.v. Chimney). The chart's single Latin > English arrow therefore telescopes an Old French stage for chimney, but the Latin source is correct for both words.\",\n \"derivation_fa\": \"«camera» را انگلیسی مستقیماً از لاتین گرفته است: نخست اصطلاحی معماری و حقوقی، سپس از ۱۷۰۸م به‌صورت camera obscura «اتاق تاریک»، و دوربین عکاسی (دههٔ ۱۸۴۰م) کوتاه‌شدهٔ همان است؛ اسکیت می‌نویسد: «Camera از لاتینی camera «اتاق»، و از آن camera obscura، اتاق تاریک، جعبهٔ عکاسی». اما «chimney» از راه فرانسه آمده است: caminus لاتینی «کوره، اجاق» ← لاتینی متأخر caminata «اتاقِ اجاق‌دار» ← فرانسوی کهن cheminée ← انگلیسی میانهٔ chimenee ← chimney. پس پیکانِ یگانهٔ «لاتین ← انگلیسی» برای chimney یک مرحلهٔ فرانسوی را نادیده گرفته، ولی سرچشمهٔ لاتینی هر دو واژه درست است.\",\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\",\n   \"note\": \"Watkins 1985 index l.1332 'CAMERA kamer-'; the kamer- article derives the Latin/English camera from Greek kamara.\"}],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"s.v. chimney (KLN_1966.txt l.7416)\", \"stance\": \"supports\",\n   \"note\": \"'chimney, n. — ME. chimenee, fr. OF. cheminee (F. cheminée), fr. Late L. (camera) caminata, \\\"(a room) provided with a chimney\\\", fr. L. caminus, \\\"forge, hearth\\\", fr. Gk. kaminos ... See camera.'\"},\n  {\"src\": \"SKT\", \"where\": \"Skeat s.vv. Camera and Chimney (SKT.txt l.2692, l.3385)\", \"stance\": \"supports\",\n   \"note\": \"'Camera. (L.) L. camera, a chamber; hence camera obscura, a dark chamber, box for photography; see Chamber.'; 'Chimney. (F.-L.-Gk.) F. cheminée ... L. caminus ...'\"}\n ]\n})\n\nN.append({\n \"id\": 12, \"lang\": \"Germanic\", \"words\": \"himin, hibin\", \"verdict\": \"disputed\",\n \"derivation\": \"The forms are real — Proto-Germanic *himinaz / dissimilated *hibin- 'heaven' (Goth. himins, ON himinn, OS/OHG himil, OE heofon) — and the gloss 'the vault (of heaven)' is a fair paraphrase; but no modern authority derives them from kam-er-, and Nourai's own reference contradicts him. Watkins/AHD, which is the reference cited on this node, puts *himin-, *hibin- under the root ak- 'sharp': 'suffixed form *ak-men, stone, sharp stone used as a tool, with metathetic variant *ka-men ... b. *ke-men- (probable variant) in Germanic *himin-, in dissimilated form *hibin-, \\\"the stony vault of heaven\\\", in Old English heofon: HEAVEN. [Pok. 2. ak- 18, 3. kem- 556.]' — i.e. the two forms the chart quotes are lifted from the ak- article and reattached to the wrong root. Walde-Pokorny I 350 explicitly warns against this node: 'got. himins usw. \\\"Himmel\\\" braucht nicht als \\\"Gewölbe\\\" benannt zu sein, sondern kann als \\\"*Deckender\\\" ... zu kem- \\\"bedecken, einhüllen\\\" gehören', and adds that *qamer- can only be set up 'wenn himins, cumera (und kaminos) ausscheiden'. Klein s.v. heaven likewise: 'These words prob. derive fr. Teut. base *hama(n)-, fr. I.-E. base *kem-, *kam-, \\\"to cover\\\"' — his 'to cover' base, not the *qam-/*qem- 'to bend, vault' base of his camera article. The current consensus (Kroonen, followed by Wiktionary) derives *himinaz from PIE *h2eḱmō 'stone (sky as a stone vault)', gen. *h2ḱmnós, cf. Skt. aśman, Gk. akmōn; the *ḱem- 'cover' proposal of Frisk and Kluge is the runner-up. Nourai was probably misled by Klein's bare cross-reference 'Cp. also heaven' at the end of the camera entry.\",\n \"derivation_fa\": \"خودِ صورت‌ها درست‌اند — ژرمنی آغازین *himinaz و گونهٔ ناهمگون‌شدهٔ *hibin- «آسمان» (گوتی himins، نورسی کهن himinn، آلمانی علیای کهن himil، انگلیسی کهن heofon) — و معنای «طاقِ آسمان» هم بیراه نیست؛ اما هیچ منبع امروزی آن‌ها را از *kam-er- نمی‌گیرد، و مأخذِ خودِ نورایی خلاف او را می‌گوید. واتکینز در AHD این دو صورت را زیر ریشهٔ ak- «تیز، سنگ» می‌آورد: «*ak-men «سنگ» با گونهٔ قلب‌شدهٔ *ka-men ... و *ke-men- در ژرمنی *himin-، به‌صورت ناهمگون‌شدهٔ *hibin-، «طاق سنگی آسمان»» — یعنی نورایی همین دو صورت را از مقالهٔ ak- برداشته و به ریشهٔ نادرست بسته است. والده‌ـ‌پوکورنی (ج۱ ص ۳۵۰) صریحاً هشدار می‌دهد که himins گوتی لازم نیست «طاق» نامیده شده باشد و می‌تواند «پوشاننده» و از ریشهٔ kem- «پوشاندن» باشد، و می‌افزاید که *qamer- تنها آنگاه بازسازی‌کردنی است که himins و kaminos کنار گذاشته شوند. کلاین هم ذیل heaven آن را از پایهٔ *kem-، *kam- «پوشاندن» می‌گیرد. رأی امروزی (کرونن و ویکی‌واژه) *himinaz را از *h₂éḱmō «سنگ» می‌داند (سنسکریت aśman، یونانی ákmōn). پژوهش امروزی این پیکان را رد می‌کند.\",\n \"sources\": [W_HIM],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"contradicts\",\n   \"note\": \"Watkins 1985 s.v. ak- (AHD_watkins1985.txt l.275): '3. Suffixed form *ak-men, stone ... with metathetic variant *ka-men ... b. *ke-men- (probable variant) in Germanic *himin-, in dissimilated form *hibin-, \\\"the stony vault of heaven,\\\" in Old English heofon, hefn, heaven: HEAVEN. [Pok. 2. ak- 18, 3. kem- 556.]'; index l.1582 'HEAVEN ak-'. Nourai's own cited authority files these forms under a different root.\"}],\n \"consulted\": [\n  {\"src\": \"WLD\", \"where\": \"Bd. I 350 (WLD_Bd1_pages.txt l.32936-32940)\", \"stance\": \"contradicts\",\n   \"note\": \"'got. himins usw. \\\"Himmel\\\" braucht nicht als \\\"Gewölbe\\\" benannt zu sein, sondern kann als \\\"*Deckender\\\" ... zu kem- \\\"bedecken, einhüllen\\\" gehören ... Wenn himins, cumera (und kaminos) ausscheiden, kann idg. *qamer- ... angesetzt werden.'\"},\n  {\"src\": \"KLN\", \"where\": \"s.v. heaven (KLN_1966.txt l.17369)\", \"stance\": \"contradicts\",\n   \"note\": \"'heaven, n. — ME. heovene ... fr. OE. heofon, hefon, rel. to ... Goth. himins, OS., OHG. himil ... These words prob. derive fr. Teut. base *hama(n)-, fr. I.-E. base *kem-, *kam-, \\\"to cover\\\". See chemise.' — a different base from the *qam-, *qem- 'to bend, vault' of his camera entry.\"},\n  {\"src\": \"POK\", \"where\": \"p.524-525 s.v. kam-er-\", \"stance\": \"silent\",\n   \"note\": \"Pokorny's material for kam-er- lists Indic, Avestan, Greek and Latin only; no Germanic word at all.\"}\n ]\n})\n\nN.append({\n \"id\": 13, \"lang\": \"English\", \"words\": \"heaven\", \"verdict\": \"confirmed\",\n \"derivation\": \"Within its own branch this arrow is right: Old English heofon, hefn 'sky, heaven' < Proto-Germanic *himinaz with the West Germanic dissimilation *-m-n- > *-b-n- (whence OE heofon, OS heban beside Goth. himins, OHG himil), > ME heovene, hevene > heaven. What is wrong is only the attachment of the Germanic node itself to kam-er- (see #12): heaven does descend from *himin-/*hibin-, but that word's own origin is PIE *h2eḱmō 'stone' (Kroonen) or *ḱem- 'to cover' (Klein, Kluge), not 'to bend, vault'.\",\n \"derivation_fa\": \"در درون شاخهٔ ژرمنی این پیکان درست است: انگلیسی کهن heofon/hefn «آسمان» از ژرمنی آغازین *himinaz، با ناهمگونیِ غرب‌ژرمنیِ ‑mn‑ به ‑bn‑ (از این‌روست heofon انگلیسی کهن و heban ساکسونی کهن در برابر himins گوتی و himil آلمانی علیای کهن)، سپس انگلیسی میانهٔ heovene/hevene و سرانجام heaven. آنچه نادرست است تنها بستنِ خودِ خانهٔ ژرمنی به ریشهٔ *kam-er- است (بنگرید به شمارهٔ ۱۲): heaven به‌درستی از *himin-/*hibin- می‌آید، ولی ریشهٔ آن واژه *h₂éḱmō «سنگ» یا *ḱem- «پوشاندن» است، نه «خمیدن و طاق‌زدن».\",\n \"sources\": [W_HIM],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\",\n   \"note\": \"The node carries no reference in the book; checked against Klein, Watkins and Wiktionary instead.\"}],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"s.v. heaven (KLN_1966.txt l.17369)\", \"stance\": \"supports\",\n   \"note\": \"'ME. heovene, hevene, heven, fr. OE. heofon, hefon, rel. to OS. hebān, LG. heben, ON. himinn, Goth. himins, OS., OHG. himil ... G. Himmel, \\\"heaven, sky\\\".' — the Germanic > English step as drawn.\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ak- (l.275)\", \"stance\": \"supports\",\n   \"note\": \"'Germanic *himin-, in dissimilated form *hibin- ... in Old English heofon, hefn, heaven: HEAVEN' — same Germanic-to-English step, different ultimate root.\"}\n ]\n})\n\nN.append({\n \"id\": 14, \"lang\": \"Latin\", \"words\": \"campus; Campania\", \"verdict\": \"plausible\",\n \"derivation\": \"campus 'level ground, field' does belong to kam-p- for Pokorny, who explains the semantics himself: 'Latin campus \\\"field\\\" (originally \\\"bend, indentation, lowland, depression\\\", as Lithuanian lankà \\\"valley, meadow\\\" to lenkti \\\"bend\\\")' — the same figure as Mann's 'Lat. campus \\\"plain, field\\\", semantics of E bent \\\"heath\\\"' and Klein's 'camp ... fr. L. campus ... fr. I.-E. base *qamp-, \\\"to bend\\\"'. Two reservations keep this from 'confirmed': Watkins's AHD appendix, one of the two references cited here, restricts kamp- to the Greek forms (kampē, kampylos) and does not list campus at all; and Ernout-Meillet give campus a full article with no Indo-European etymology whatever, treating it purely as a Latin-Romance item. Campania is the regular adjectival derivative (campanius/campaneus 'of the open country' > Late Latin campania 'plain'), the name of the plain around Naples — Klein s.v. campaign: 'L. Campania, name of a province of Italy about Naples, lit. \\\"the plain or level country\\\"'. The chart's gloss 'famous for its scales' points at the Campanian steelyard (Latin campana 'balance', ML statera campana), the link that node #18 needs.\",\n \"derivation_fa\": \"campus «زمین هموار، دشت» را پوکورنی به ریشهٔ *kam-p- می‌بندد و خودِ او دگرگونی معنایی را توضیح می‌دهد: «campus لاتینی «دشت» در اصل «خمیدگی، گودی، زمین پست»، همچون lankà لیتوانیایی «دره، مرغزار» از lenkti «خم کردن»»؛ مان و کلاین نیز همین را می‌گویند («camp از campus لاتینی، از پایهٔ *qamp- «خمیدن»»). دو نکته مانع از «تأییدِ کامل» است: نخست آنکه پیوستِ AHD (یکی از دو مأخذِ همین خانه) ریشهٔ kamp- را تنها به صورت‌های یونانی محدود کرده و campus را اصلاً نیاورده است؛ دوم آنکه ارنو و مه‌یه برای campus هیچ ریشه‌شناسی هندواروپایی نمی‌آورند. Campania نیز صفتِ منظمِ همان است (campanius «متعلق به دشت» ← لاتینی متأخر campania «دشت») و نام جلگهٔ پیرامون ناپل؛ اشارهٔ نمودار به «شهرتش در ترازو» به «ترازوی کامپانیایی» (campana لاتینی) برمی‌گردد که خانهٔ شمارهٔ ۱۸ به آن نیاز دارد. پس این خانه با احتیاط پذیرفتنی است.\",\n \"sources\": [],\n \"ref_check\": [\n  {\"ref\": \"POK:525\", \"status\": \"supports\",\n   \"note\": \"POK_full.txt l.43466 under kam-p-: 'Latin campus \\\"field\\\" (originally \\\"bend, indentation, lowland, depression\\\", as Lithuanian lanka \\\"valley, meadow\\\" to lenkti \\\"bend\\\")'.\"},\n  {\"ref\": \"AHD:193\", \"status\": \"not_checked\",\n   \"note\": \"AHD:193 is a page of the 1975 New College main dictionary (the 'camp/campus' page), which is not available; but the Watkins appendix in AHD_watkins1985.txt s.v. kamp- (l.579) lists only Greek kampē and kampylos and does NOT include Latin campus, so the appendix does not back this arrow.\"}\n ],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"s.vv. camp, campaign (KLN_1966.txt l.6289, l.6292)\", \"stance\": \"supports\",\n   \"note\": \"'camp, n. — F., fr. It. campo, fr. L. campus, \\\"flat space, plain field\\\" ... fr. I.-E. base *qamp-, \\\"to bend\\\", whence also Gk. kampē ... Goth. hamfs \\\"mutilated\\\" ...'; 'Cp. L. Campania, name of a province of Italy about Naples, lit. \\\"the plain or level country\\\".'\"},\n  {\"src\": \"IEC\", \"where\": \"Mann s.v. kampos (IEC.txt l.6719)\", \"stance\": \"supports\",\n   \"note\": \"'kampos \\\"crooked, bent; crook, bend, angle, leg\\\" ... Lat. campus \\\"plain, field\\\" (semantics of E bent \\\"heath\\\", Li. lankas: lanka)'.\"},\n  {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. campus (LAT.txt l.9056 ff.)\", \"stance\": \"silent\",\n   \"note\": \"A long article on the Latin and Romance history ('plaine, terrain plat ... Ancien, usuel. Panroman. M.L. 1563. Germ.: mhd. kamp, all. Kampf') with no Indo-European etymology offered at all.\"},\n  {\"src\": \"WLD\", \"where\": \"Bd. I 350-351\", \"stance\": \"supports\",\n   \"note\": \"The qamp- article (which is 'Idg. qamp- ist möglicherweise eine Erw. von *qam-') is headed by Latin campus among Goth. hamfs, Lith. kampas, gr. kampē.\"}\n ]\n})\n\nN.append({\n \"id\": 15, \"lang\": \"French\", \"words\": \"champaigne\", \"verdict\": \"plausible\",\n \"derivation\": \"Old French champaigne 'open country, plain' < Late Latin campania (the neuter plural campanea 'level country' reanalysed as a feminine), with the regular Gallo-Romance ca- > cha-; it gives English champaign and, through Italian campagna, English campaign. That much is exactly Klein, KLN p.266-267. The second half of the chart's gloss conflates two words: the French province and the wine are Champagne (Klein: 'champagne, n. — F., abbreviation of vin de Champagne, \\\"wine made in the province of Champagne\\\", a name derived fr. Late L. campania'), which is the same Late Latin etymon but a proper name with its own spelling; the common noun champaigne 'open country' has nothing to do with wine. Nourai has fused the two entries of his own source into one box.\",\n \"derivation_fa\": \"فرانسوی کهن champaigne «دشت، سرزمین باز» از campania لاتینی متأخر است (جمعِ خنثای campanea که مؤنث بازتحلیل شد)، با همان دگرگونی منظمِ ca- به cha- در گالوـ‌رومی؛ از آن champaign انگلیسی و از راه campagna ایتالیایی واژهٔ campaign پدید آمده است. تا اینجا دقیقاً گفتهٔ کلاین (ص ۲۶۶–۲۶۷) است. اما نیمهٔ دوم توضیحِ نمودار دو واژه را یکی گرفته: نام ایالت و شرابِ آن Champagne است — کلاین: «champagne کوتاه‌شدهٔ vin de Champagne، شرابِ ساخته‌شده در ایالت شامپاین، نامی برگرفته از campania لاتینی متأخر» — که هرچند از همان ریشه است، اسم خاصی با املای دیگر است، حال آنکه champaigne به معنی «دشت» ربطی به شراب ندارد. نورایی دو مدخلِ مأخذ خود را در یک خانه آمیخته است.\",\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"KLN:266\", \"status\": \"supports\",\n   \"note\": \"Klein 1966 leaf 152 (printed pp.266-267, the page numbers 266/267 are visible on that leaf): 'champaign, n., open country, plain. — OF. champaigne, fr. L. campania. See campagna, campaign, and cp. champion, scamp.' The neighbouring entry on the same leaf is 'champagne, n. — F., abbreviation of vin de Champagne ... fr. Late L. campania', which is the wine sense the chart tacks on.\"}],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"s.vv. campaign, champagne, champaign (KLN_1966.txt l.6292, l.7158-7159)\", \"stance\": \"partial\",\n   \"note\": \"Klein keeps three separate entries: campaign (F. campagne < It. campagna < LL Campania), champagne (the wine, from the province), champaign (the common noun 'open country'). The chart merges the last two.\"},\n  {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. campus, derivatives (LAT.txt l.9057-9075)\", \"stance\": \"supports\",\n   \"note\": \"'les dérivés bas latins campaneus, -nius, dans les Gromat. 331,30, in montanioso loco, ... in campaneis' — the Late Latin adjective behind campania/champaigne.\"}\n ]\n})\n\nN.append({\n \"id\": 16, \"lang\": \"Persian\", \"words\": \"šâmpâyn «شامپاین»\", \"verdict\": \"plausible\",\n \"derivation\": \"A modern French loan into Persian: French champagne [ʃɑ̃paɲ] > Persian شامپاین, the -ayn spelling reflecting the word as it reached Persian through the international (rather than strictly French) pronunciation of the wine name; Mo'in's dictionary also carries the older, closer transcription شامپانی, defined 'نوعی شراب سفید کف‌دار گرانبها که آن را اصلاً در «شامپانی» (فرانسه) از بهترین اقسام انگور تهیه کنند' — i.e. Mo'in himself derives the Persian word from the French province. Two qualifications: the immediate source is the proper name Champagne / vin de Champagne, not the common noun champaigne 'open country' drawn as the parent; and Nourai's English gloss 'Champaign' is the wrong word for the wine (English champagne).\",\n \"derivation_fa\": \"«شامپاین» وام‌واژه‌ای نو از فرانسه است: champagne فرانسوی ← شامپاین فارسی؛ املای «ـاین» بازتاب تلفظ بین‌المللی نام آن شراب است، و معین صورت نزدیک‌تر «شامپانی» را هم ثبت کرده و چنین تعریف می‌کند: «نوعی شراب سفید کف‌دار گرانبها که آن را اصلاً در «شامپانی» (فرانسه) از بهترین اقسام انگور تهیه کنند» — یعنی خودِ معین این واژه را از نام ایالت فرانسه می‌گیرد. دو نکته: سرچشمهٔ مستقیم، نامِ خاصِ Champagne (و ترکیب vin de Champagne) است نه واژهٔ عام champaigne «دشت» که در نمودار پدرِ آن نشان داده شده؛ و برابرنهادِ انگلیسیِ نورایی («Champaign») برای این شراب نادرست است و باید champagne باشد.\",\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"MON:2001\", \"status\": \"partial\",\n   \"note\": \"The 6-vol. Mo'in is not digitised. The 2-vol. Adena abridgement (MON_part1.txt l.83153) has 'شامپانی: (اِ.) نوعی شراب سفید کف‌دار گرانبها که آن را اصلا در «شامپانی» (فرانسه) از بهترین اقسام انگور تهیه کنند' — the same word and the same French-province etymology, but spelt شامپانی; شامپاین was not found in the abridgement.\"}],\n \"consulted\": [\n  {\"src\": \"MON\", \"where\": \"2-vol. abridgement s.v. شامپانی (MON_part1.txt l.83153)\", \"stance\": \"supports\",\n   \"note\": \"Derives the Persian word from the French district of Champagne, as the chart does.\"},\n  {\"src\": \"KLN\", \"where\": \"s.v. champagne (KLN_1966.txt l.7158)\", \"stance\": \"partial\",\n   \"note\": \"'champagne, n. — F., abbreviation of vin de Champagne, \\\"wine made in the province of Champagne\\\", a name derived fr. Late L. campania.' The parent is the province name, not OF champaigne 'open country'.\"}\n ]\n})\n\nN.append({\n \"id\": 17, \"lang\": \"English\", \"words\": \"Champaign, champion, camp\", \"verdict\": \"confirmed\",\n \"derivation\": \"All three go back to Latin campus, as drawn, though by three different roads. champaign 'open country' is straight from Old French champaigne (Klein p.266). champion is Middle English from Old French champion < Late Latin campiō, -ōnem 'fighter', literally 'one who takes the field' — the Frankish-Latin term for a judicial duellist in the campus (Klein: 'champion, n. — ME., fr. OF. champion, fr. Late L. campionem, acc. of campio, \\\"fighter\\\", lit. \\\"one who takes the field\\\", fr. L. campus, \\\"field\\\"'). camp is the odd one out: it did not come through Old French but was taken in the 16th c. from Italian campo / French camp (military sense), and Skeat thinks it may even be direct from Latin — 'Camp. (L.) We find F. camp (Cot.); but the E. word was prob. taken directly from L. campus, a field, ground held by an army.' Note that Klein's own camp article stands on p.226, not on p.266 as cited, though he cross-refers to champaign from there.\",\n \"derivation_fa\": \"هر سه واژه به campus لاتینی می‌رسند، اما از سه راه. champaign «دشت» مستقیماً از فرانسوی کهن champaigne است. champion از انگلیسی میانه، از فرانسوی کهن champion، از لاتینی متأخر campiō «جنگاور»، تحت‌اللفظ «آنکه به میدان می‌آید» — اصطلاحِ لاتینیِ فرانکی برای جنگجوی دوئل قضایی در «میدان» (کلاین). اما camp استثناست: از راه فرانسوی کهن نیامده بلکه در سدهٔ ۱۶م از ایتالیایی campo و فرانسوی camp (به معنای نظامی) گرفته شده و اسکیت حتی آن را وام مستقیم از لاتین می‌داند: «Camp (لاتینی): در فرانسوی camp هست، ولی واژهٔ انگلیسی احتمالاً یکراست از campus لاتینی «دشت، زمینی که سپاه در آن اردو زند» گرفته شده است». یادآوری: مدخلِ camp در کلاین در ص ۲۲۶ است نه ص ۲۶۶ که نورایی ارجاع داده، هرچند کلاین از همان‌جا به champaign ارجاع می‌دهد.\",\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"KLN:266\", \"status\": \"partial\",\n   \"note\": \"Klein leaf 152 (pp.266-267) carries champaign and champion, exactly as cited: 'champion, n. — ME., fr. OF. champion, fr. Late L. campionem ... fr. L. campus, \\\"field\\\". See camp and cp. champaign.' But camp itself is on Klein leaf 132 (~p.226): 'camp, n. — F., fr. It. campo, fr. L. campus'.\"}],\n \"consulted\": [\n  {\"src\": \"SKT\", \"where\": \"Skeat s.v. Camp (SKT.txt l.2692)\", \"stance\": \"supports\",\n   \"note\": \"'Camp. (L.) We find F. camp (Cot.); but the E. word was prob. taken directly from L. campus, a field, ground held by an army.'\"},\n  {\"src\": \"KLN\", \"where\": \"s.v. camp (KLN_1966.txt l.6289)\", \"stance\": \"supports\",\n   \"note\": \"'camp, n. — F., fr. It. campo, \\\"camp\\\", fr. L. campus ... Cp. campaign ... champaign, champignon, champion, decamp, encamp ...'\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 index (AHD_watkins1985.txt l.1332)\", \"stance\": \"silent\",\n   \"note\": \"Only 'CAMPYLOTROPOUS kamp-' appears in the index for this root; CAMP, CHAMPION and CHAMPAIGN are not assigned to kamp- (or to any root) in the appendix.\"}\n ]\n})\n\nN.append({\n \"id\": 18, \"lang\": \"Persian\", \"words\": \"capân «کپان»\", \"verdict\": \"transcription_suspect\",\n \"error_in\": \"book\",\n \"book_prints\": \"capân\",\n \"correct_form\": \"kapân\",\n \"derivation\": \"Two things to separate. (1) The transliteration: the printed page (pdf p.237, image saved as sources/refs/ocr/BOOK/237.png) really does read 'capân' for «کپان» — a bare c that Nourai's own system never uses for ک (he writes kamar, kâbâreh, and marks the affricate as č in čap, čamîdan). The extraction is faithful; the misprint is the book's, and the form should read kapân (variants قپان qapân, قبان qabbân, colloquial Tehrani قپون qapun). (2) The etymology is essentially right but the route is compressed. Persian کپان/قپان is a steelyard, a one-pan balance; Wiktionary derives it 'from Byzantine Greek κάμπανος (kámpanos), γάμπανος, from Latin campāna' — the campana, the balance named after Campania, the very link the chart's node #14 supplies ('name of an area in Italy famous for its scales'). What the chart's direct Latin > Persian arrow hides is the Byzantine Greek stage and the Syriac/Arabic transmission: Asbaghi (PLA p.216) lists Arabic قبان qibbān 'Schnellwaage' with 'pers. کپان kapān' and a Syriac form beside it, and Tobia al-Unaysi has 'قبان ـ فارسي «كپان» وهو ميزان للأحمال الثقيلة'; Mo'in's entries کپان and قبان cross-refer to each other as mo'arrab/original. Persian and Arabic lexicography therefore treat کپان as the source of Arabic qabbān, whereas the Greco-Latin origin makes the Persian word itself a borrowing — probably through Aramaic/Syriac qanpānā. The Ferdowsi verse of the chart ('به کپان درم سختن آغاز کرد') shows the word already in Persian by the 10th c.\",\n \"derivation_fa\": \"دو چیز را باید جدا کرد. نخست آوانگاری: در صفحهٔ چاپی (تصویر در sources/refs/ocr/BOOK/237.png) به‌روشنی «capân» آمده است، حال آنکه نورایی خودش «ک» فارسی را همه‌جا k می‌نویسد (kamar، kâbâreh) و «چ» را č؛ پس این خطای چاپی کتاب است نه خطای خوانشِ اسکن، و صورت درست kapân است (گونه‌ها: قپان، قبان، و در گفتار تهرانی قپون). دوم ریشه‌شناسی که در اصل درست ولی فشرده است: «کپان/قپان» ترازوی یک‌کفه‌ای است و ویکی‌واژه آن را از یونانی بیزانسی kámpanos و آن را از campāna لاتینی می‌گیرد — همان «ترازوی کامپانیایی» که خانهٔ شمارهٔ ۱۴ نمودار به شهرتِ کامپانیا در ترازو اشاره می‌کند. آنچه پیکانِ مستقیمِ «لاتین ← فارسی» پنهان می‌کند مرحلهٔ یونانی بیزانسی و انتقال سریانی/عربی است: اصباغی (ص ۲۱۶) عربی «قبّان» را «Schnellwaage» می‌داند و آن را از «فارسی کپان» می‌گیرد و در کنارش صورت سریانی می‌آورد؛ طوبیا العنیسی نیز می‌نویسد «قبان ـ فارسي «كپان» وهو ميزان للأحمال الثقيلة»؛ و معین در دو مدخل «کپان» و «قبان» آن‌ها را معرّب یکدیگر می‌خواند. یعنی فرهنگ‌نویسی فارسی و عربی کپان را سرچشمهٔ «قبّان» عربی می‌دانند، حال آنکه خاستگاه یونانی‌ـ‌لاتینی نشان می‌دهد خودِ واژهٔ فارسی هم وام‌واژه است، احتمالاً از راه آرامی/سریانی qanpānā. بیت فردوسی («به کپان درم سختن آغاز کرد») نشان می‌دهد واژه در سدهٔ چهارم هجری در فارسی جا افتاده بوده است.\",\n \"sources\": [W_QAPAN],\n \"ref_check\": [\n  {\"ref\": \"MON:2896\", \"status\": \"partial\",\n   \"note\": \"6-vol. Mo'in not available; the 2-vol. abridgement has both entries — 'کپان: [- معر. قبان - قپان] ترازویی که یک پله دارد و بجای پله دیگر سنگ از شاهین آن آویزند؛ قپان' (MON_part2.txt l.20406) and 'قبان: [معر. کپان - قپان] ترازویی که دارای یک پله باشد؛ قپان' (l.11135). Sense and cross-reference match the chart; the page number is consistent with the alphabetical run.\"},\n  {\"ref\": \"ARK:222\", \"status\": \"not_checked\",\n   \"note\": \"Rokn-zadeh Adamiyyat, Arkan-e Sokhan, is not digitised anywhere (refs_online.json: 'Not found ... nothing digitised on any permitted platform').\"},\n  {\"ref\": \"PLA:216\", \"status\": \"supports\",\n   \"note\": \"Asbaghi, Persische Lehnwörter im Arabischen, printed p.216 (PLA_pages.txt leaf 231, running heads 'qubād ... 216 ... ġarastūn'): 'qibbān: \\\"Schnellwaage\\\" pers. کپان kapān, syr. ...' with footnote 3 (Muḥīṭ, Wahrmund, Addai Scher). Asbaghi supports a Persian kapān behind Arabic qabbān/qibbān — i.e. the Persian word and its Arabic double, though not the Latin ancestry.\"}\n ],\n \"consulted\": [\n  {\"src\": \"TAD\", \"where\": \"Tobia al-Unaysi s.v. قبان (TAD.txt l.2239)\", \"stance\": \"supports\",\n   \"note\": \"'قبان ـ فارسي «كپان» وهو ميزان للاحمال الثقيلة و ...' — Arabic qabbān from Persian kapān, a balance for heavy loads.\"},\n  {\"src\": \"MON\", \"where\": \"2-vol. abridgement s.vv. کپان, قبان\", \"stance\": \"supports\",\n   \"note\": \"Both entries define the one-pan steelyard and tag each other as the mo'arrab form.\"},\n  {\"src\": \"AFM\", \"where\": \"Addi Shir (AFM.txt, grep 'قبان')\", \"stance\": \"silent\",\n   \"note\": \"No entry for قبان found in this OCR of the Alfāẓ al-fārisiyya al-muʿarraba (only كوكبان in an unrelated line).\"},\n  {\"src\": \"LKT\", \"where\": \"Lokotsch (LKT.txt, grep 'qabban|campana|kampanos')\", \"stance\": \"silent\",\n   \"note\": \"No entry located for this word in the OCR of Lokotsch's dictionary of European orientalisms.\"}\n ]\n})\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-237.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"nodes:\", len(N))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk237.py && python3 -m json.tool data/verification/page-237.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 237"
}
```


### [2026-09-06T16:02:02.058Z] TOOL RESULT

```
nodes: 18
JSON OK
nodes verified: 18/18
node verdicts: {'confirmed': 8, 'plausible': 6, 'disputed': 3, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 16, 'not_checked': 4, 'partial': 7, 'not_found': 1, 'contradicts': 1}
books consulted: {'supports': 30, 'not_found': 1, 'partial': 10, 'silent': 9, 'contradicts': 3} | by book: {'KLN': 12, 'MON': 4, 'WLD': 4, 'IEC': 3, 'POK': 3, 'LAT': 3, 'HRN': 2, 'ARY': 2, 'PHD': 2, 'CHEUNG': 2, 'etymonline': 2, 'SKT': 2, 'AHD': 2, 'BRT': 1, 'HUB': 1, 'HJB': 1, 'WEB': 1, 'KNT': 1, 'FFD': 1, 'BQT': 1, 'TAD': 1, 'AFM': 1, 'LKT': 1}
```


## [2026-09-06T16:02:23.414Z] AGENT

Verification of PDF page 237 (book p. 207) is written to `/home/sfmqrb/git/rishe/data/verification/page-237.json`; `verify_check.py 237` reports 18/18 nodes and **0 PROBLEM lines**.

**Root `Kam 2, Kamer, Kamp, Qam, Qem` — confirmed.** POK 524-525 (kam-er-, kam-p-), WLD I 349 ("qam- (qem-?) wölben, biegen … qamer-") and Klein's `*qam-, *qem-` account for all five labels.

**Verdicts:** root confirmed; nodes 8 confirmed / 6 plausible / 3 disputed / 1 transcription_suspect. Ref checks: 16 supports, 7 partial, 1 contradicts, 1 not_found, 4 not_checked.

Flagged items:
- **#12 Germanic `himin, hibin`** — *disputed*. Nourai's own cited source contradicts him: Watkins/AHD files `*himin-, *hibin- "the stony vault of heaven"` under root **ak-** (Pok. 2. ak- 18), WLD I 350 says himins may belong to `kem-` "cover", Klein s.v. heaven derives it from `*kem-/*kam-` "to cover", and Kroonen/Wiktionary from `*h₂éḱmō` "stone". Likely misled by Klein's bare "Cp. also heaven" at *camera*.
- **#4 Old Persian `kanpa`, `čam`** — *disputed*. Neither is attested Old Persian (Kent has only kan-, kamna-, kāma-). `*kanp-` is a reconstruction; `čam` is Old Iranian/Parthian (Cheung, Abolghasemi p.48) and means "walk/run", not "bend".
- **#5 Persian `čapeh, čap, čafteh, čamīdan 1, xam`** — *disputed* only because of `čamīdan 1` "walk flauntily": Cheung splits it off to a separate non-IE root `*čam` "to walk". The other four are well supported (POK 525 and WP I 350 cite np. čap; Horn no. 446 p.99 covers čap, čanbar and xam/xamīdan; Cheung's `*kamp` has čaftah).
- **#18 Persian `capân` «کپان»** — *transcription_suspect*, `error_in: "book"`. The printed page really reads `capân`; Nourai never uses bare `c` for ک. Correct form `kapân`. Etymology itself sound (Byz. Gk. kámpanos ← Lat. campāna; PLA:216 and al-Unaysi confirm the Persian/Arabic pair).

**No extraction errors** — the JSON matches the printed page everywhere I checked (page image saved to `data/verification/sources/refs/ocr/BOOK/237.png`).

Other notable finds: BQT:620/658/661/768 all match exactly, but **BQT:1439 is a stray citation** (that page is فتالیدن/فتریدن/فتن, nothing related). Gk. `kaminos` means "oven/furnace", not "fire". Node #15 conflates OF *champaigne* "open country" with the province *Champagne*.
