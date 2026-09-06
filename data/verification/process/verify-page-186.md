# Verification process log — verify-page-186


## [2026-09-06T02:13:11.303Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 186 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-186.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-186.json. Write /home/sfmqrb/git/rishe/data/verification/page-186.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 186` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T02:13:13.095Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-06T02:13:13.761Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T02:13:13.778Z] TOOL RESULT

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


## [2026-09-06T02:13:14.188Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-186.txt"
}
```


### [2026-09-06T02:13:14.204Z] TOOL RESULT

```
1	=== PDF page 186 (book page 156) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ghel : to shine, also a bright yellow color  (refs POK:429)  PART 2
4	#1 (parent #0) [Greek] refs=AHD:236 | xlôros : greenish yellow color ; xlôros-phullon : green leaf (chlorophyll) ☞Bhel
5	  #2 (parent #1) [French] refs=None | 
6	    #3 (parent #2) [Persian] refs=MON | kolor «کلر» : chlorine | extra: کلروفیل ، کلروفرم
7	  #4 (parent #1) [English] refs=None | chlorine, chlorophyll
8	#5 (parent #0) [Greek] refs=AHD:817 | xolĕ : bile ; melan-xolia : black bile, a disease ☞Mel 1
9	  #6 (parent #5) [Latin] refs=None | melancholia
10	    #7 (parent #6) [Persian] refs=BQT:795,1947 | mâlîxŭlîâ «مالیخولیا» : melancholy | extra: خولیا
11	      #8 (parent #7) [Arabic] refs=AFM:59; FVF:223 | xîyâl : imagination | NOTE: Arabic "xîyâl" is a distorted form of Persian "xŭlîa:imagination".
12	        #9 (parent #8) [Persian] refs=MON:1466 | xîyâl «خیال» : imagination | extra: تخیّل
13	    #10 (parent #6) [French] refs=None | 
14	      #11 (parent #10) [English] refs=None | melancholy
15	#12 (parent #0) [Germanic] refs=None | 
16	  #13 (parent #12) [English] refs=AHD | gold, yellow, glass, gloss, glow, glad
17	    #14 (parent #13) [Persian] refs=MON:3513 | gîlâs «گیلاس ۱» : a glass drinking cup
18	--- entry 1 ---
19	ROOT [Indo-European] Gheled : ice, hail  (refs POK:435)
20	#1 (parent #0) [Sanskrit] refs=POK:435 | jada : hail, also cold and dry
21	  #2 (parent #1) [Persian] refs=BQT:1057; MON:1775; FSF:216 | žâleh «ژاله» : hail, dew
22	#3 (parent #0) [Greek] refs=AHD | xalaza : hail stone, also any lump sum object, tumor
23	  #4 (parent #3) [English] refs=None | chalazion : an eyelid tumor
24	
```


## [2026-09-06T02:13:17.319Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-186.json",
 "description": "Read source JSON page 186"
}
```


### [2026-09-06T02:13:17.365Z] TOOL RESULT

```
{
  "pdf_page": 186,
  "book_page": 156,
  "entries": [
    {
      "root": {
        "name": "Ghel",
        "lang": "Indo-European",
        "refs": "POK:429",
        "gloss": "to shine, also a bright yellow color"
      },
      "part": 2,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD:236",
          "words": [
            {"translit": "xlôros", "gloss": "greenish yellow color", "script": null},
            {"translit": "xlôros-phullon", "gloss": "green leaf (chlorophyll)", "script": null, "see": ["Bhel"]}
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
          "refs": "MON",
          "words": [
            {"translit": "kolor", "gloss": "chlorine", "script": "کلر"}
          ],
          "script_extra": "کلروفیل ، کلروفرم",
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "chlorine, chlorophyll", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD:817",
          "words": [
            {"translit": "xolĕ", "gloss": "bile", "script": null},
            {"translit": "melan-xolia", "gloss": "black bile, a disease", "script": null, "see": ["Mel 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Latin",
          "refs": null,
          "words": [
            {"translit": "melancholia", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "BQT:795,1947",
          "words": [
            {"translit": "mâlîxŭlîâ", "gloss": "melancholy", "script": "مالیخولیا"}
          ],
          "script_extra": "خولیا",
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Arabic",
          "refs": "AFM:59; FVF:223",
          "words": [
            {"translit": "xîyâl", "gloss": "imagination", "script": null}
          ],
          "note": "Arabic \"xîyâl\" is a distorted form of Persian \"xŭlîa:imagination\".",
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "MON:1466",
          "words": [
            {"translit": "xîyâl", "gloss": "imagination", "script": "خیال"}
          ],
          "script_extra": "تخیّل",
          "note": null,
          "quote": {
            "text": "بر خیالی صلحشان و جنگشان - وز خیالی فخرشان و ننگشان",
            "poet": "Molavî"
          }
        },
        {
          "id": 10,
          "parent": 6,
          "lang": "French",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "melancholy", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Germanic",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "gold, yellow, glass, gloss, glow, glad", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "Persian",
          "refs": "MON:3513",
          "words": [
            {"translit": "gîlâs", "gloss": "a glass drinking cup", "script": "گیلاس ۱"}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Gheled",
        "lang": "Indo-European",
        "refs": "POK:435",
        "gloss": "ice, hail"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:435",
          "words": [
            {"translit": "jada", "gloss": "hail, also cold and dry", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1057; MON:1775; FSF:216",
          "words": [
            {"translit": "žâleh", "gloss": "hail, dew", "script": "ژاله"}
          ],
          "note": null,
          "quote": {
            "text": "تو گفتی هوا ژاله بارد همی - به سنگ اندرون لاله کارد همی",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "xalaza", "gloss": "hail stone, also any lump sum object, tumor", "script": null}
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
            {"translit": "chalazion", "gloss": "an eyelid tumor", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-06T02:13:19.613Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','MON','BQT','AFM','FVF','FVQ','FSF','WLD','KLN','HRN','HUB','PHD','NYB','IEC','SYN','SKT','WEB','FSD','PLA','ARY']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:400])\n\"",
 "description": "Inspect refs_online keys"
}
```


### [2026-09-06T02:14:19.652Z] TOOL RESULT

```
claude-sonnet-5[1m] is temporarily unavailable (timed out), so auto mode cannot determine the safety of Bash right now. Wait a moment and then try this action again. If it keeps failing, continue with other tasks that don't require this action and come back to it later. Note: reading files, searching code, and other read-only operations do not require the classifier and can still be used.
```


## [2026-09-06T02:14:24.040Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','MON','BQT','AFM','FVF','FVQ','FSF','WLD','KLN','HRN','HUB','PHD','NYB','IEC','SYN','SKT','WEB','FSD','PLA','ARY','LKT','MAY']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:400])\n\"",
 "description": "Inspect refs_online keys"
}
```


### [2026-09-06T02:14:25.654Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
FVF {"title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968", "kind": "website", "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)", "lookup_hint": "Alphabeti
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushi
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
MAY null
```


## [2026-09-06T02:14:28.874Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/sources/refs/ && echo ---- && sed -n '1,120p' data/verification/sources/SOURCE_MATRIX.md",
 "description": "List local reference files and matrix"
}
```


### [2026-09-06T02:14:28.926Z] TOOL RESULT

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
----
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
```


## [2026-09-06T02:14:31.299Z] TOOL CALL #7: Bash

```json
{
 "command": "sed -n '1,200p' tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-06T02:14:31.347Z] TOOL RESULT

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


## [2026-09-06T02:15:08.913Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK ghel glänzen ===\"; grep -n \"ĝhel-\" POK_full.txt | head -40\necho \"=== POK chalaza ===\"; grep -n -i \"χάλαζα\\|chalaza\\|Hagel\" POK_full.txt | head -40",
 "description": "Grep Pokorny for ghel and hail"
}
```


### [2026-09-06T02:15:08.997Z] TOOL RESULT

```
=== POK ghel glänzen ===
=== POK chalaza ===
34638:compare Modern High German Hagel.^x. KaxAr)^ pebble ', etc.
```


## [2026-09-06T02:15:12.664Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nwc -l POK_full.txt POK_01.txt POK_02.txt POK_03.txt\necho \"=== head ===\"; head -30 POK_full.txt\necho \"=== grep ghel ===\"; grep -n \"ghel-2\\|ghel-1\\|ĝhel\" POK_full.txt | head -20\necho \"=== grep Page 429 ===\"; grep -n \"Page(s): 429\\|Page(s): 435\" POK_full.txt | head -20",
 "description": "Inspect Pokorny files"
}
```


### [2026-09-06T02:15:12.780Z] TOOL RESULT

```
  93771 POK_full.txt
   5151 POK_01.txt
   6715 POK_02.txt
   5974 POK_03.txt
 111611 total
=== head ===
List of language abbreviations in tlie lED 



Abbreviation Language name 


Aeq. 




Aequian 


Akk. 




Akkadian 


Alan. 




Alanian (=Old Ossetic) 

=== grep ghel ===
20282:From Root / lemma: ghel-1 (and ghel-1), also as /-, u-or /7-stenn; ghela- : ghle- ghlo- : 
20320:From Root / lemma: ghel-1 (and ghel-1), also as /-, ^-or /7-stem; ghela- : ghle-, ghlo- : 
20345:From Root / lemma: ghel-1 (and ghel-1), also as /-, ^-or /7-stem; ghela- : ghle-, ghlo- : 
36328:From Root / lemma: ghel-1 (and ghel-1), also as /-, u-or /7-stem; ghela- : ghle-, ghlo- : 
36633:Root / lemma: ghel-2 
=== grep Page 429 ===
32677:Page(s): 435 
32690:Page(s): 435 
32712:Page(s): 435 
32730:Page(s): 435 
32746:Page(s): 435 
36631:Page(s): 429-434
```


## [2026-09-06T02:15:14.722Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '36590,36700p' POK_full.txt",
 "description": "Read Pokorny ghel entry region"
}
```


### [2026-09-06T02:15:14.781Z] TOOL RESULT

```
gh/eu- and gh/ou-: gh/u- perhaps in gr. xA6(F)o(;, x^ouq " greenish-yellow or light green 
colour: hence, pallor ', xA6r| " the first green shoot of plants in spring, young green corn or 
grass ', xAo(F)£p6q "green, fresh, strong'; 

further in Irish gluair{*ghleu-ri-) "clear, bright, pure, clean'; cymr. ^/c»"coar, corn, glow. 
Middle Breton glou, abret. g/aou{see Pedersen KGr. I 63). 

Gothic g/aggwo' clear ', g/aggwaba' carefully ', Old Icelandic g/gggr, g/0ggr'c\ear, 
bright, distinct, painstaking, stingy'. Old English gleaw. Old Saxon glau. Old High German 
ndd. glau^ clear-eyed, hawk-eyed, smart'. Old \ce\av\d\c gluggi^ light opening, window'. 

(To arrangement of these words with Lithuanian zvelgiu, zi/eTg//" glance, look' compare 
Trautmann 374.) 

ghl6u-\v\ Old Icelandic g/da'g\o\N, gleam, shine'. Old English g/owan' fulminate ', Old 
Icelandic himinglseva " daughter of Agirs and Ran ' (impersonating the surge); -glo- f. "sun', 
-gloai. "moon'; s. also above S. 430 under ghlo- 

^^/J-; Norwegian dial, glyma^ dim, lookthreatening or sneaky ', Old Swedish gluna^ 
look askance ', East Frisian glumen^ see and lurk hidden and secretly after something '; 
Old Icelandic ^/J/77/'m. "bear'. 



In addition 5-(s#-)extensions: 

Irish gluss {*ghlustu-) "light, brightness'; 

Old Icelandic glys^ radiance, frippery', nisi, glosa^ shine'. Middle High German glosen, 
g/osten 'g\o\N, gleam', g/oste'b\aze, glow'. Middle Low German g/uren'\urk', engl. to 
glower^ look dim, scowl ', steir. gloren^ stare ', Norwegian dial, glyra^ look sideways, 
squint, blink'. Old Icelandic ^/>r/7af. 'eye', Norwegian g/dr6s. 

ghlud-: Middle English glouten, engl. to glouV stare, look grievingly or sullenly ', to 
gloat {< *glotian) " feel or express triumphant and malicious satisfaction at another's 
misfortune, exult, look, gaze malicious ', Old Icelandic ^/c»//a" grin ', Middle High German 
Modern High German glotzen. 

References: WP. I 623 f., 624 ff., WH. I 473 f., 514, 578 f., 600, 607 f., 639, 654, 868, 
Trautmann 83 f., 88, 364 f., 368, 372, Persson Beitr. 170 f., 790 ff., 876 f. 
Page(s): 429-434 

Root / lemma: ghel-2 
Meaning: to cut 

Material: Old Indie hala- m. n. 'plough' (originally 'bough, twig, branch'?); hudu-, huda-xx\. 
'aries, ram' {*gh!du-)\ 

Armenian yb/ 'picket, pole, stick' etc.,y/e/77' groove, plow'; 

gr. yaAAoc; 'priest of Cybele, the castrator ' (from Phrygian, whence also Hittite iskalla-^ 
shred, tear', Iskallis name of Attis?), out of it Latin gallus ds.; 

acymr. gylym, mcymr. geleu, ^e/yf' knife, dagger' (Vendryes Et. celt. 4, 60) from *ghel- 
mo-= Old English gielm; 

Gothic gill=>ai. 'sickle'; Old English gielm m. ' fascicle, sheaf '; Old Icelandic ggltr, gaiti 
'boar', gylr, gylta^sow, axe'. Old English g/elteyoung sow'. Middle Low German gelte' a 
castrated mother's pig ', Old High German galza, gelzat ' castrated swine'; Old High 
German Middle High German gait, Old English g/elde, Old Norse geldr, Old Swedish 
galder^ giving no milk, barren, infertile ', Old Icelandic gelda^ castrate '; Swiss galta\so 
'not giving milk ', galdvee= ' Jungvieh '. 

Lithuanian zuolis^ piece of wood, tree trunk ' {gholi-). 



the above equation always doubtful. 

References: WP. I 626 f., Petersson Heterokl. 155 f., nVH. I 581. 
Page(s): 434 

Root / lemma: ghengh- 

Meaning: to march, step 

Material: Old Indie 75/77/735-11. " footstep, flapping 'Jarjgha^ shank, leg, shin bone ', 

Avestan za/7^a/77 'ankle of the foot', -zangra-{\n compounds) ds., zero grade Old Indie 

jaghana-m. n. "buttock, pubic region ' : gr. Koxwvn " place between thighs' (assim. from 

*Kaxu)va); 

Old English -g/hf gait ', Middle High German g/ht' gait, journey' (proto Germanic 
*g/nxtf- from gheng-ti-), with gradation o.' Gothic gaggu.. Old Icelandic gangr. Old English 
Old High German gang^ gait ' and Germanic *gangjan \ter. (Gothic preterit gagg/da' 
walked ', Old English gengan. Middle High German gengen, gancte^ leave; wade in') and 
thereafter also *gangan, Gothic gaggan 'go' = Old Icelandic ganga {gekk). Old Saxon 
gangan {geng). Old High German gangan {giang). Old English gongan6s., wherefore Old 
High German gengi. Old English genge. Old Icelandic gengr^ feasible, able to be carried 
out', Gothic framgahts' advance'. Old Icelandic gatV incision in doorposts', gaettT door 
frame '; zero grade Old Frisian gunga 'go', Danish gynge, older gunge 'swing'; 

Lithuanian zengiu, zengti^ march, step, stride, strut ', prazanga' contravention, violation 
', zingsnis ' footstep '. 

A duplicate Aniaut (through dissimilation?) perhaps in Old Irish cingim ' march, step, 
stride, strut' (3. PI. cengait, Perf. cechaing), cymr. rhy-gyngu^ going pass ', Old Irish cing. 
Gen. cinged^\Narr\or\ gall. Cingeto-rTx, zero grade proto Celtic *kngsmn\n Old Irish ceimm 
{* kenksmen), cymr. corn, cam, bret. camm^ footstep ' {*kanksman). 

An other variant *ghenk-\s (under d/r^-s 'quick, fast') for Old High German ^5/7/ "rash, 
hasty, sudden' take into consideration. 

References: WP. I 588, WH. I 217, Trautmann 370. 
Page(s): 438-439 

Root/ lemma: ^^e/d^-and ghei^^-
```


## [2026-09-06T02:15:19.814Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^Root / lemma: ghel-1\\|Root/ lemma: ghel-1\" POK_full.txt | head\necho ---\nawk 'NR>=36200 && NR<=36360' POK_full.txt | grep -n \"Meaning\\|Root / lemma\" | head",
 "description": "Locate ghel-1 lemma"
}
```


### [2026-09-06T02:15:21.480Z] TOOL RESULT

```
---
20:n. year' prove that Root / lemma: en-2\ year' : Root/ lemma: at-, *atno- : "to go; year' : 
75:Root / lemma: ghe/-1 {and ghe/-7), also as A, u-or /7-stem; ghela-: ghle-, ghlo-. ghla- 
79:Meaning: to shine; green, gold, blue, yellow, moon 
83:Root / lemma: ghe/-1 {and ghe/-7), also as /-, u- or /7-stem; ghela- : ghle-, ghlo- : ghle- : to 
129:From Root / lemma: ghel-1 (and ghel-1), also as /-, u-or /7-stem; ghela- : ghle-, ghlo- :
```


## [2026-09-06T02:15:25.262Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '36274,36330p' POK_full.txt\necho \"=====  chloros/khole search =====\"\ngrep -n \"xoAn\\|xoAr\\|xAcopo\\|xAoipo\\|MzAac; xoAn\\|melancholy\" POK_full.txt | sed -n '1,20p'",
 "description": "Read ghel-1 header and search khole"
}
```


### [2026-09-06T02:15:25.363Z] TOOL RESULT

```
Root / lemma: ghe/-1 {and ghe/-7), also as A, u-or /7-stem; ghela-: ghle-, ghlo-. ghla- 

{*ghwet-) 

Meaning: to shine; green, gold, blue, yellow, moon 

Note: 

Root / lemma: ghe/-1 {and ghe/-7), also as /-, u- or /7-stem; ghela- : ghle-, ghlo- : ghle- : to 

shine; green, gold, blue, *sun; derived from Root/ lemma: gel-, gela-, gle-, (also *gelel-.) 

g(e)lal-\ light, to shine; to be joyful. 

Material: In view of the frequent cases, where Indo Germanic palatals in Balto-Slavic are 

represented by velar, instead of through a concurrence of gel-, ghel- and ghel- agreeable 

with Persson (Beitr. 790) and Kretschmer (Gl. 21 , 115) the Balto-Slavic *gel- is defined 

through borrowing from a Centum language (Venetic-lllyrian?). 

Note: 

The enxtended root {*ghwel-)-nta, -na, -/aformants follow the model of lllyrian - Anatolian 

attribute nouns, adjectives, (see alb. numbers). 

Old Indie har'h "blond, yellow, golden, green yellow, pale', harina-h^ gazelle ', harit- " 
dun-colored, light grayish brown ', harita- ^yeWow, green', hfranya-n. "gold, medium of 
trade', hiranyaya-^ Qo\den'; about hataka-n. "gold' s. Kuiper Proto-Munda 30; in addition 
being based on velar root Old Indie gbofa-'horse' as originally "fox'? (Sommer IF. 31 , 364 
under A. 3); 



the normal development in Latin helvus^ honey-yellow, golden ' {*gheluos) = gallo- Latin 
g/7vus'\\g\r\t yellow' (with dial, /from gall. *gelvos)\ 

in addition Latin {h)olus, -e/75(from *holos, *heleris) n., dial, folus, old helus, helusa^ 
herbage, vegetables, cabbage '; 

Note: 

Common Old Indie : Latin gh-> h-. 

Avestan zari- 'yellow, yellowish, golden ', zaMa- "yellow, paled-yellow ', zaranya-. Old 
pers. daraniya-u. 'gold', zaranaena Irom gold, golden', zara- m. 'gall' (= gr. xoAn), named 
after the color as gr. xoAoc;, Latin fe/, [common Latin ghw- > ph- > A], Old Norse ga// ust; 
with velar root aniaut gsrado-karata-^ cutting out the gall '? (see Bartholomae Altiran. Wb. 
523 with Lithuanian); 

Note: 

From Root / lemma: ghel-1 (and ghel-1), also as /-, u-or /7-stem; ghela- : ghle-, ghlo- : 
ghla-\ 'to shine; green, gold, blue, *sun' derived Root/ lemma: d^e/-/, d^o/o-: 'curve; 
hollow'. Root/ lemma: 6^61-2: 'light, shining'. Root/ lemma: 6}^el-3\ 'to tremble' [common 
=====  chloros/khole search =====
36321:pers. daraniya-u. 'gold', zaranaena Irom gold, golden', zara- m. 'gall' (= gr. xoAn), named 
36344:gr. xbkoQ, 'gall, rage, fury', xoAr) 'gall, rage, fury', xoA-£pa ' stomach disease ', xAwpoq '
```


## [2026-09-06T02:15:28.137Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '36335,36400p' POK_full.txt",
 "description": "Read Greek section of ghel-1"
}
```


### [2026-09-06T02:15:28.217Z] TOOL RESULT

```
alb. dhelpere, dhelpne, dhelbun(e) 'fox', actually 'the yellow one' (see Jokl Linguist, 
kulturhist. Stud. 297 ff.); 

Wrong etymology: 

Alb. alb. dhelpere, dhelpne, dh e l buna 'fox' derived from the transposition of Griko 
Salentino li pun eddha; ali puna 'fox', from earlier Greek Greek aAgnou 'fox'. 

gr. xbkoQ, 'gall, rage, fury', xoAr) 'gall, rage, fury', xoA-£pa ' stomach disease ', xAwpoq ' 
pale green, green yellow, fresh, strong' (:Old Icelandic ^/oa' radiance '); 

Latin fel, fellis{*fel-n-is) n. 'gall' (older /7-stem as Old High German galla), /probably 
dialect; WH. I 474, EM2 342 would be placed to /e/and Lithuanian gelfas 'yeWow' etc. (see 
below) a root *g"'hel- {77); 

Note: 



Latin fel, fellis {*fe/-n-/s) n. 'gall' derived from root *del because of common Latin d- > f-. 

here also Latin ga/bus' xanthous bird', galbinus " green yellow ', whether Celtic or 
lllyrian loanword {*ghe/-b^o-or *gho/-b^o-, further to Lithuanian gulbissee below); 

Maybe alb. {*gelben) gjelber' green ' < Rom. galben^ green ' < galbinus^ green yellow '. 

Old Irish ^©/"luminous, white', nir. gealachi. 'moon'; cymr. ge//'ye\\o\N', bret. ge// 
'brown' {*ghel-no)\ 

in addition *ghl9-\v\ Irish cymr. corn. bret. g/an 'pure, clean', Celtic FIN Glanis, Glana, 
Irish glain 'glass, crystal' ( *ghlani-), cymr. glain 'gemstone, jewel' ( *ghlanio-); 

also in isl. glana' clear up ', glan' radiance ', Norwegian dial. ^/aA7a "shimmer, gleam, 
shine, clear up ', Swedish dial. glana's\\\v\e weakly, stare, peek', asach. FIN (S/a/7a (further 
see below den s-extensions). 

Old Icelandic gallu. 'gall, poison ' ( *galldn-, Indo Germanic *ghol-n-). Old English gealla 
m.. Old Saxon galla, intense f.. Old High German galla, weakf. 'gall'; 

zero grade Old Icelandic gu/r'yeWow', besides full grade Old English geolo. Old Saxon 
Old High German gelo. Gen. gelwesAs. (< *gelua-)\ 

Gothic gult^u.. Old Icelandic gull, gollu.. Old English Old Frisian Old Saxon Old High 
German goldu. 'gold'; 

Ablaut grade *ghle- in Old Icelandic glamr' moon', glamsynr optic deception, illusion ', 
Swedish glamlg' gray-yellow in the face, with sunken eyes ', Old Icelandic ^/^/"'bright' 
{*glela= Lithuanian z/eya under). 

*gh/d-{as in gr. xAwp6<;) appears in Old English glom' twilight, dawn, dusk' (yet o 
before m\s ambiguous). Old Saxon glolan. Old High German gluoen'burv\\ gluhen'shme 
', Old Icelandic ^/od 'blaze, glow, glowing coal'. Old English gisedt 'blaze, glow, flame, 
glowing coal, coal'. Old Frisian gled'b\aze, glow'. Old High German gluot'b\aze, glow, 
glowing coals'; Old Icelandic -^/oAn. ' radiance ' (: xAwp6(;), Old Icelandic ^/d/a 'sparkle, 
glitter'; s. also under S. 433 ghlou-, 

Lithuanian zeliu, zeliau, zeiti, Latvian zelu, zelt'be green'; ablaut. Lithuanian zailas, 
Latvian zal's. Old Prussian sallgan' green', Lithuanian zole, Latvian zaiei. 'grass, herb'. 
Old Prussian sal/nAkk. 'herb', Lithuanian zaias'red' (from cattle); Lithuanian z/las'gray', 
Latvian z//s'blue', Lithuanian zelvas' greenish ', Latvian ze//5 (previous Neutr.) 'gold'. 



East Lithuanian ze7tas'go\6en'; Litliuanian z/eja' twiiiglit, liaif darkness, dusl< ' {*gh/e/a), 
Trautmann Bsl. Wb. 364 f., 368, 372; Lithuanian /^/z/s"gall', through Metath. from *zu/t/s,
```


## [2026-09-06T02:15:33.474Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '32600,32760p' POK_full.txt",
 "description": "Read Pokorny page 435 region"
}
```


### [2026-09-06T02:15:33.537Z] TOOL RESULT

```
Gothic faihu-geigan'\\is\., crave', ga-geigan^ gain ', nasalized Old High German gingen 
"after etwas verlangen', ^//7^c»"das Verlangen'; after Wissmann Nom. postverb. 41 though 
to ghei-gh; above S. 421. 

Lithuanian apmaudqgiezti^ hold a grudge, nurse a grievance ', gieziuos' long, want 
violently ', pagiezti' ask for revenge ', pagieza^ thirst for revenge '; whether Lithuanian 
giezti, pa-giezti\x\\x. " im Halse kratzen ' would be with it. 

References: WP. I 552; different Feist 136 f. 
Page(s): 427 

Root / lemma: gheis- and gheiz-d- 



Meaning: confused, shocked 

Note: original resemblance with ghei-, ghe/-s-\n Old Indie h/not/ etc. is very probably 

Material: Avestan zaesa-' gruesome' 

Note: 

Reduplicated laryngeal in -h2™ahre- > Avestan -ae- 

zoisnu-^ frightening, shuddering, shaking together (before frost)', zoizdisto^ of the 

ghastliest, most hideous ones ' (Superl. to a verb *zdizda- ' make shudder '; see below 

gheiz-d-)\ 

Gothic us-geisnan^ erschrecken (intr.), au(ler£assung geraten ', Kaus. us-gaisjan^ 
erschrecken (tr.), aufter Fassung bringen ' (but Old Icelandic ^e/isa ' hervordringen, 
heranstijrmen ' from *ga-eisa)\ 

Old Icelandic geiskiu. " fear, horror '. 

root form gheiz-6^-:0\6 Indie hed- 'be angry with' {ahedant-, ahedamana-h, Perf. jihTda), 
heda-h rw., hedahu. "anger' (here also helate' is improvident ', helayati^ deride ', see 
be\o\N ghe/-' yawn '), hTdati^ excited, aroused, aggrieved ', Med. 'is excited, aroused, 
angry '; Avestan zoizdista- {see above); 

Old High German geist{= Old Indie heda-li) m.. Old Saxon gest. Old English gast 
{gsestj m. 'ghost (in contrast to the body); uberirdisches gespenstiges Wesen ' (so esp. 
engl. ^/7c»s/' ghost'). Old English gsestan {*gaistjan) 'frighten' (tr.), engl. aghasf agitated, 
angry, irate', ghastly^ grisly, terrible, dreadful'. 

That in the meaning exact attuning Old Church Slavic za5/7(?// "frighten (intr.). stupefied ', 
zas/// "frighten' (tr.), uzast 'fright' from *g(h)ds- aWuues in vowel and not in guttural. 

References: WP. I 553 f.. Feist 531 f. 
Page(s): 427 

Root / lemma: ghel(e)gh- 

Meaning: a kind of metal 

Material: Old Church Slavic *zelezo\x\ zelez(b)n-b ' iron', Serbo-Croatian zeljezo, russ. 

ze/&zc» 'iron'; 

Lithuanian ge/ez/'san6 zem. ^e/z/5 (therefrom gelezinis, gelzinis^ iron'), Latvian dzeizs. 
East Latvian dzelezs. Old Prussian gelsot 'iron'; 



Whether in connection with gr. xc(Ak6(;, Cretan Kauxot; " copper, bronze '? That k from 
XQAkoc; standing comparison not in the way, because Kouxoq in *xaAx6(; points as common 
primary grade. The word probably derives from a a foreign cultural circle; also the unique 
gradation of the 2nd syllable in Balto Slavic would be based on different substitution in the 
in the borrowed; xciAk6(; (£pu9p6(; llias I 365) as ' red metal ' perhaps to xaAKP), xaAxn. 
KaAxn ' murex, snail emitting purple dye ', which is likewise borrowed; in Balto Slavic the 
name would be figuratively transferred from bronze to the iron. 

References: WP. I 629, Specht Dekl. 27, Trautmann 83. 
Page(s): 435 

Root / lemma: gheled- 
Meaning: ice 

Material: Npers. zala{*zalda) "hail, hoarfrost'; 

gr. hom. xaAa^a 'hail'; 

Old Church Slavic z/e d/ca Irozen rain', sloven. z/ed^g\azed frost, ice', kir. ozeleda^ rain 
with snow, ice on trees ', poln. ziodz^ sleet, smooth ice '. 

References: WP. I 629 f., Specht Dekl. 17. 
Page(s): 435 

Root / lemma: ghelgh- 

Meaning: gland 

Note: 

Root/ lemma: gheigh-: "gland' derived from an extended Root/ lemma: gel-1\ "to curl; 

round, *gland, growth, ball'. 

Material: Armenian geij-kh " glands ' (the obvious aniaut can be explained through 

dissimilation, s. Meillet MSL. 13, 244f., Liden Arm. Stud. 71 under A. 1. 2); 

East Lithuanian gelezuones, gelezaunes, gelezunes " glands, craw '; 

Slavic *zelza\v\ Church Slavic zleza, russ. zeleza, sloven, zleza, acech. zleza, 
nowadays zlaza^ gland ' (about Czech hlfza^ abscess ' s. Meillet aaO.), poln. zo/zads. 

References: WP. I 612, 632, Trautmann 84. 
Page(s): 435 



Root / lemma: ghel-ond- ghol-ijd- 

Meaning: stomach; bowels 

Note: (A supposition about the old paradigm by Petersson Heteroklisie 228'') 

Material: Gr. xoAa5£(;f. PI. ' intestines, entrails, Gedarm', x6AiK£(;ds.; 

Maybe abbreviated alb. zorra " intestine, entrail ' common alb. gh- > d-, z-\ l/rs. 

Old Church Slavic *zelgd'bk-b " stomach ', russ. -Church Slavic zeludtk-b, Serbo-Croatian 
zeludac, Czech zaiudek, poln. zo/^o'e/rds. 

References: WP. I 631 f., Trautmann 82. 
Page(s): 435 

Root / lemma: ghel-ou-, ghelu- 

Meaning: tortoise 

Material: Gr. x^Kxic, 'turtle, tortoise. Lyre', xsAcbvp ds., Aeolic xsAuvva, x£A£U(; KiGapa Hes. 

(Kuiper Notes 48); 

Slavic zelu-i. 'turtle, tortoise' in: 

Church Slavic zeli^vb, russ. -Church Slavic zelva, Serbo-Croatian zelva, Czech zelva, 
russ. zolvbi., poln. zd/tv. 

References: WP. I 631, Trautmann 84, Specht Indo Germanic Dekl. 120. 
Page(s): 435 

Root/ lemma: p'^eA/i? (Germanic) and p'^eZ-d'^d (Slavic) 
Meaning: to cost, pay 

Material: Gothic fra-gildan^ repay, compensate ', us-gildan^ repay'. Old Icelandic gjalda^ 
defray, pay, repay, be worth ', Old English gieldan. Old High German geltan ' defray, 
repay, serve, sacrifice' (proto Germanic *je/dd), Old Swedish gja//a ds. {*je//=>d); Gothic 
g/7dn. 'tax, interest'. Old Icelandic 5/5/0'' payment, earnings, punishment'. Old English 
gield^ payment, tribute, tax, sacrifice, oblation, brotherhood ', Old Icelandic ^/M' 
membership ', Old English glide v\. ds., glldam. ' Gildenbruder ' (out of it Middle Irish gllda 
' squire '), Middle Low German glide, out of it Modern High German Glide; Old High 
German gelt^ payment, repayment, sacrifice, oblation etc.'. Modern High German Geld, 
QoVc\\c gllstru. 'tax'. Old High German gelstar{*geld-tra-) 'sacrifice, oblation, tax'; from 
ndd. gellen =gelfen derWes Lithuanian gelluotrbe valid';
```


## [2026-09-06T02:15:57.358Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD watkins ghel ===\"; grep -n \"ghel-\" AHD_watkins1985.txt | head -40",
 "description": "Grep Watkins for ghel"
}
```


### [2026-09-06T02:15:57.414Z] TOOL RESULT

```
=== AHD watkins ghel ===
153:Internal organs were also named in Indo- European times, including the womb (g“elbh-), gall (ghel-?), brain (mregh-mno-, confined to Low German and Greek), spleen (spelgh-), and liver (yekr). The male sexual organs, pes- and ergh-, are common patri- mony, as is ors-, “backside.”
172:The Indo-Europeans knew metal and met- allurgy, to judge from the presence of the word ayes- in Sanskrit, Germanic, and Latin. The term designated copper and perhaps bronze. Iron is a latecomer, technologically, and the terms for it vary from dialect to dialect. Latin has ferrum, while the Ger- manic and Celtic term was *isarno-, properly “holy (metal),” doubtless so called because the first iron was derived from small meteor- ites. Gold was known from ancient times, though the names for it vary; ghel-2, prob- ably “yellow (metal),” and aurum (*aus-, Latin aurum), are widespread. Silver was arg-, with various suffixes, doubtless mean- ing “white (metal).”
510:*ghait-d in Greek khaité, long hair: CHAETA; (CHAETOG- NATH). [Pok. ghait-d- 410.] ghalgh-. Branch, rod. Germanic *galgon- in: a. Old English g(e)alga, cross, gallows: GALLOWS; b. Old North French gauge, gauge: GAUGE. [Pok. ghalgh- 411.] ghans-. Goose. 1. Germanic *gans- (nominative plural *gansiz) in: a. Old English gds (nominative plural gés), goose: GOOSE!; (GOSHAWK); b. Old Norse gas, goose, diminutive geslingr, gosling: GOSLING. 2. Germanic *ganr- in Old English ganra, gandra, gander: GANDER. 3. Germanic *gandton- in Old English ganot, gannet: GANNET. 4, Suffixed form *ghans-er- in Latin dnser (< *hanser), goose: ANSERINE; MERGANSER. 5. Basic form *ghans- in Greek khén, goose: CHENOPOD. [Pok. ghans- 412.) ghasto-. Rod, staff. 1. Variant form *ghazdh- in Ger- manic *gazdaz in: a. Old English gierd, gerd, staff, twig, measuring rod: YARD}; b. Old Norse gaddr, rod, goad, spike: GAD?. 2. Form “ghast-d- in Latin hasta, spear: HASLET, HASTATE. [Pok. 1. ghasto- 412.] ghé-. To release, let go; (in the middle voice) to be released, go. Contracted from *ghea-. 1. Germanic vari- ant form *gaian in Old English gdn, to go: GO; AGO, FOREGO!, FoRGO. 2. Suffixed form *ghé-ro- in Latin hérés, heir (? < “orphan” < “bereft”):; HEIR, HEREDITA- MENT, HEREDITY, HERITAGE; INHERIT. 3. Suffixed o-grade form *ghé-ro-, “empty space,” possibly in: a. Greek khéros, place, country, particular spot: CHO- ROGRAPHY; b. Greek denominative khorein, to move, go, spread about, make room for: -CHORE; ANCHORITE. 4. Perhaps suffixed zero-grade form *gha-l- in Greek khalan, to slacken, let down (but this is more likely of unknown origin): CALANDO, CHALONE; ACHALASIA. 5. Suffixed zero-grade form *gho-t(w)d- in Germanic *gatwon-, a going, in Old Norse gata, path, street: GAIT. [Pok. ghé- 418.] ghebh-el-. Head. 1. Germanic *gablaz, top of a pitched roof, in Old Norse gafl, gable: GABLE. 2. Dissimilated form *khephel- in Greek kephalé, head: CEPHALIC, CEPH- ALO-, -CEPHALOUS; ENCEPHALO-, ENKEPHALIN, HYDRO- CEPHALUS. [Pok. ghebh-el- 423.] ghedh-. To unite, join, fit. 1. Lengthened o-grade form *ghédh- in Germanic *gédaz, “fitting, suitable,” in Old English géd, good: GooD. 2. Germanic *gaduri, “in a body,” in Old English tégezdere (t6, to; see de-), together: TOGETHER. 3. Germanic “gadurén, “to come or bring together,” in Old English gad(e)rian, to gather: GATHER. [Pok. ghedh- 423.] ghei-'. To propel, prick. 1. Suffixed and extended o-grade form *ghoidh-d in Germanic *gaidé, goad, spear, in Old English gdd, goad: GOAD. 2. Suffixed form *ghei-s- per- haps in nasalized zero-grade form *ghi-n-s- in Sanskrit himsati, he injures: AHIMSA. [Pok. 1. ghei- 424.] ghei-2. Theoretical base of *ghyem-, *ghiem-, winter. 1. Form *ghiem- in Latin hiems, winter: HIEMAL. 2. Suf- fixed variant form *gheim-ri-no- in Latin hibernus, pertaining to winter: HIBERNACULUM, HIBERNATE. 3. Suffixed zero-grade form *ghim-ar-ya, “female animal one year (winter) old,” in Greek khimaira, she-goat: CHIMERA. [Pok. 2. ghei- 425.] gheis-. Used of the emotion of fear or amazement (origi- nal part of speech uncertain). Suffixed o-grade form *ghois-do- in Germanic *gaistaz, a ghost, in: a. Old English gdst, ghost: GHOST; AGHAST; b. Old High Ger- man geist, ghost: POLTERGEIST; Cc. Germanic denomina- tive *gaistjan in Old English g&stan, to scare: GAST. [Pok. gheis- 427.] ghel-'. To call. 1. Germanic “gel-, *gal-, in: a. Old Eng- lish gellan, giellan, to sound, shout: YELL; b. Old English gielpan, to boast, exult: YELP; c. Old English galan, to sing: NIGHTINGALE. 2. Reduplicated form *ghi-ghl- in Greek kikhilé, thrush, later also the name for a kind of wrasse (a sea fish that has bright colors and jagged waving fins, reminiscent of the plumage of a bird):
512:CICHLID. 3. Greek khelidw6n, khelidén, the swallow: CELANDINE. [Pok. ghel- 428.] ghel-2. To shine; with derivatives referring to colors, bright materials (probably “yellow metal”), and bile or gall. I. Words denoting colors. 1. Suffixed form *ghel-wo- in Germanic *gelwaz in Old English gealu, yellow: YELLOW. 2. Suffixed variant form *ghlé-ro- in Greek khioros, green, greenish yellow: CHLORO-; CHLORITE!. 3. Suffixed variant form *ghlo-wo- in Greek khloos (< *khlo-wo-s), green color: CHLOASMA. 4, O-grade form *ghol- in Russian zola, ashes (from their color): PODZOL. II. Words denoting gold. 1. Suffixed zero-grade form *ghl-to- in Germanic *gultham, gold, in: a. Old English gold, gold: GOLD; b. denominative verb *gulthjan in Old English gyldan, to gild: GILD!; c. Middle Dutch gulden, golden: GUILDER, GULDEN; d. Old Norse gulinn, golden, akin to the possible source of Middle English gollan, yellow flower: GOWAN. 2. Suffixed o-grade form *ghol-to- in Polish zloto, gold: zLoTy. 3. Suffixed full-grade form *ghel-i- in the unknown Iranian source of Syriac zarnikd, orpiment: ARSENIC. III. Words denoting bile. 1. Suffixed o-grade form “ghol-no- in Germanic *gallon-, bile, in Old English gealla, gall: GALL!. 2. Suffixed o-grade form *ghol-& in Greek kholé, bile: CHOLE-, CHOLER, (CHOL- ERA); ACHOLIA, MELANCHOLY. 3. Suffixed full-grade form *ghel-n- in Latin fel, bile: FELON?. IV. A range of Germanic words (where no preforms are given, the words are late creations). 1. Germanic *glaimiz in Old English glém, bright light, gleam: GLEAM. 2. Middle High Ger- man glimsen, to gleam, akin to the source of Middle English glimsen, to glimpse: GLIMPSE. 3. Swedish dialec- tal glinta, to shine, akin to the source of Middle English glent, a glint: GLINT. 4. Swedish glimra, akin to the source of Middle English glimeren, to glimmer: GLIM- MER. 5. Old Norse glitra, to shine: GLITTER. 6. Old English glisnian, to shine: GLISTEN. 7. Middle Dutch glisteren, to shine: GLISTER. 8. Germanic *glasam, glass, in Old English gles, glass: GLASS, GLAZE. 9. Germanic *glaz- in Middle Low German glaren, to glisten, akin to the source of Middle English glaren, to glitter, stare: GLARE!. 10. Icelandic glossi, a spark, perhaps akin to the source of GLoss!. 11. Old High German glanz, bright: GLANCE2. 12. Old Norse gléggr, clear-sighted: GLEG. 13. Germanic *gladaz in Old English gled, shining, joyful: GLAD. 14. Germanic *gleujam in Old English gléo, sport, merriment: GLEE. 15. Old English gléd, ember: GLEED. 16. Germanic *gié- in: a. Old English gléwan, to glow: GLow; b. Norwegian dialectal glora, to gleam, stare, akin to the probable source of Middle English gloren, to gleam, stare: GLOWER; C. Old Norse glotta, to smile (scornfully), perhaps akin to the source of GLOAT. 17. Germanic *glé-m- in Old English glém, twilight: GLOAMING. 18. Possibly distantly related is Germanic *glidan, to glide, in: a. Old English glidan, to slip, glide: GLIDE; b. Old French glier, to glide: GLISSADE; c. Old High German glitan, to glide: GLITCH; d. derivative Germanic “glidén- in Old English glida, kite (< “gliding, hovering bird”): GLEDE. 19. Middle Low German glibbe- rich, slippery, possibly akin to the source of GLrB. [Pok. 1. &hel- 429.] ghel-. To cut. 1. Germanic “galdjan, to castrate, in Old Norse gelda, to castrate, and geldingr, a castrated ani- mal: GELD!, (GELDING). 2. Germanic *gulti- in Old Norse gyltr, a sow (< “castrated pig”): GiLT?. [Pok. 2. ghel- 434.] gheldh-. To pay. Only in Germanic and Slavic. 1. Ger- manic *geldam, payment, in: a. Old English geld, gield, payment, service: GELD?; DANEGELD, WERGELD; b. Old High German gelt, payment, reward: GELT!. 2. Germanic *geldan, to pay, in Old English gieldan, to pay, yield: YIELD. 3. Germanic *geldjam, payment, contribution, hence an association founded on contributions, a crafts- men’s guild, in Old Norse gildi, guild: GuILD. [Pok. ghel-t6 436.] ghelegh-. A metal. Possible root of Greek khalkos,
516:gheli-. Tortoise. Suffixed form “ghel-dnd in Greek khe- l6né, tortoise: CHELONIAN. [Pok. ghel-du- 435.] ghel-una. Jaw. 1. Germanic *geliz in Old Norse *gil, gill of a fish, akin to the Scandinavian source of Middle English gile, gill: GILL!. 2. Suffixed variant form *ghel-wo- in Greek kheilos, lip: CHEILOSIS, CHILOPOD. [Pok. ghelunda 436.]
1209:ACHE ag-es- ACHENE ghai- ACHERON eghero- ACHOLIA ghel-2 ACHROMATIC ghréu- ACICULA ak- ACID ak-
1260:ARMADILLO = ar- ARMATURE ar- ARMIGER gerere ARMILLARY SPHERE al- ARMISTICE sta- ARMOIRE ar- ARMY ar- ARPENT pert ARRAIGN  ar- ARRANGE sker-3 ARRAY reidh- ARREARS re- ARREST sta- ARRIERE-BAN koro- ARRIVE rei-1 ARROGATE reg-1 ARROW arku- ARSENIC ghel-2 ARSIS wer-2 ARSON as-
1339:CEDE ked- CELANDINE ghel-1 -CELE? keue-2 CELEBRATE kel-3 CELEBRITY kel-3 CELERITY kel-3 -CELIAC keue-2 CELL kel-2
1348:CHASM ghai- CHASSIS kap- CHASTE kes-2 CHAUDFROID kele-1 CHEAP caupd CHECK tké- CHECKMATE tké- CHEER ker-! CHEESE? kWo- CHEETAH kWeij-2, skai- CHEILOSIS ghel-una CHELICERA ker-1 CHELONIAN gheli- CHEMOTROPHY threph- CHENILLE kwon- CHENOPOD ghans- CHERISH ka- CHERNOZEM kers-1 CHERRY ker-6 CHERSONESE ghers-, sna- CHESS’ kap-
1350:CHIEF kaput CHIEFTAIN kaput CHILIAD gheslo- CHILL gel-3 CHILOPOD ghel-una CHIME! keu-2
1356:CHIRO- ghesor- CHIRURGEON ghesor- CHISEL kaa-id- CHITTERLINGS ku- CHLOASMA ghel-2 CHLORITE! ghel-2 CHLORO- ghel-2 CHOANA gheu- CHOANOCYTE gheu- CHOICE geus- CHOIR gher-1
1357:CHOLE- ghel-2 CHOLER ghel-2 CHOLERA ghel-2 CHOLESTEROL ster-1 CHOLINERGIC werg- CHOLLA g(e)u-lo- CHONDRO- ghrendh- CHONDROMALACIA mel-1 CHOOSE geus- CHORAGUS_§ ag-, gher-1 CHORAL gher-1 CHORALE gher-1 CHORD? ghere- -CHORE ghé- CHORIC gher-1 CHORION ghere- CHORISTER gher-! CHOROGRAPHY ghé- CHORUS gher-1 CHOWDER kele-1 CHRESARD gher-5 CHRESTOMATHY gher-5, mendh-1 CHRISM ghréi- Curist ghréi- CHRISTEN ghréi- CHRISTIAN ghréi- CuRIsTMas ghréi- CHROMA ghréu- CHROMATIC ghréu- CHROMATO- ghréu- -CHROME ghréu- CHROMIUM ghréu- CHROMO- ghréu- CHROMONEMA (s)né- CHRONAXY ag- CHRYSANTHEMUM § andh- CHTHONIC dhghem- CHUFA swei-! CHUKAR kau-! CHUKKER kwel-1 CHURCH keue-? CHURL karlaz CHUTE kad-
1358:CHYLE gheu- CHYLOMICRON smé- CHYME gheu- CICHLID ghel-1
1505:FEIGN dheigh- FEINT dheigh- FEIST pezd- FELDSPAR pele-2 FELICIFIC dhé(i)- FELICITATE dhé(i)- FELICITY dhé(i)- FELL! p(h)ol- FELL? pel-4 FELLATIO dhé(i)- FELLOW legh-, peku- FELO-DE-SE s(w)e- FELON2 ghel-2 FELT! pel-6 FEMALE dh@(i)- FEMININE dhé(i)- FEMTO- penkwe FEN pen-
1551:GAGE! wadh-1 GAIN! wei-2 GAINLY gagina GAINSAY gagina GAIT ghé- GALACTIC melg- GALACTO- melg- GALAXY melg- GALL! ghel-2 GALLIARD gal-3 GALLINACEOUS = gal-2 GALLINULE gal-2 GALLOP klou-, wel-2 GALLOWGLASS yeu- GALLOWS ghalgh- GALORE lau-
1557:GAST gheis- GASTRIC gras- GASTRO- gras- GASTRULA gras- GATHER ghedh- GAUCHE weng- GAUD gau- GAUDY! gau- GauDY? gau- GAUGE ghalgh- GAUNTLET? klou- GAUR gWou- GAVEL? ghabh- GAWK ghow-é- GAYAL gWou- _ GEANTICLINE gé GEAR garwian GEGENSCHEIN gagina, skeei- GELANDESPRUNG lendh-2, spergh- GELATIN gel-3 GELATION gel-3 GELD! ghel-3 GELD2 gheldh- GELDING ghel-3 GELID  gel-3 GELIGNITE egni- GELT! gheldh- GEM gembh- GEMINATE yem- GEMINI yem- GEMMA gembh- GEMMATE gembh- GEMMULE gembh- GEMOT mdéd- GEMSBOK bhugo- GEMUTLICH mé-1 GEMUTLICHKEIT mé-1 -GEN gene- GENDARME gene- GENDER gene- GENEALOGY genoe- GENERAL gene- GENERATE genoe- GENERATION geno- GENERIC gene- GENEROUS gene- GENESIS gene- -GENESIS gene- GENIAL! gene- GENIAL? genu-2 GENICULATE genu-1 GENITAL gene- GENITIVE gene- GENITOR gene- GENIUS gene- GENOCIDE gene- GENOTYPE gene- GENRE gene- GENS gene- GENT! gene- GENTEEL gene-
1560:GEODE gé GEODESY da- GEOMETRY mé-2 GEOPONIC (s)pen- GEORGIC gé, werg- GERANIUM gera-2 GERENT gerere GERIATRICS gera-1 GERM gene- GERMAN? gena- GERMANDER deru, dhghem- GERMANE gene- GERMINAL gene- GERMINATE gene- GERONTO- gera-1 GERUND gerere GEST gerere GESTALT stel- GESTATION gerere GESTICULATE gerere GESTURE gerere GET ghend- GEYSER gheu- GHAT gher-4 GHOST gheis- GIDDY gheu(e)- Girt ghabh- GILD! ghel-2 GILL! ghel-una GILLS ghai- GILLYFLOWER bhel-3, kar-1 GILT2 ghel-3 GIMMAL yem- GINGERLY gene- GIRASOL sawel- GIRD gher-1 GIRDLE gher-1 GIRTH gher-1 GIST yé-
1561:GIVE ghabh- GLABELLA gladh- GLABROUS gladh- GLACE gel-3 GLACIAL gel-3 GLACIATE gel-3 GLACIER gel-3 GLACIS § gel-3 GLAD ghel-2 GLADIATE kel-1 GLADIATOR kel-1 GLAIR kele-2 GLAIVE kel-1 GLANCE? ghel-2 GLAND gWele-2 GLANDERS gWele-2 GLANDULAR gWel@-2 GLANS gWela-2 GLARE! ghel-2 GLAss ghel-2 GLAZE ghel-2 GLEAM ghel-2 GLEBE gel-1 GLEDE ghel-2 GLEE ghel-2 GLEED ghel-2 GLEET gel-! GLEG ghel-2 GLEY gel-! GLIADIN  gel-1 GLIB_ ghel-2 GLIDE ghel-2 GLIMMER ghel-2 GLIMPSE ghel-2 GLINT ghel-2 GLISSADE ghel-2 GLISTEN ghel-2 GLISTER ghel-2 GLITCH ghel-2 GLITTER ghel-2 GLOAMING ghel-2 GLOAT ghel-2 GLOBE gel-1 GLOBULE gel-1 GLOCHIDIUM glégh- GLOMERATE §el-1 GLOMERULE gel-1 GLoss! ghel-2 Gloss? glégh- GLOSSARY gldgh- GLOSSOLALIA glégh-, la- GLOTTIs glégh- GLOVE lep-2 GLOW ghel-2
1563:GLOWER ghel-2 GLUCAGON ag- GLUCOSE dlk-u- GLUE gel-1 GLUME gleubh- GLUT gWel-3 GLUTEN gel-! GLUTEUS gel-1 GLUTINOUS  gel-1 GLUTTON gWel-3 GLYCERIN dik-u- GLYPH gleubh- GLYPTIC gleubh- GNAT ghen- GNATHIC genu-2 -GNATHOUS genu-2 GNAW ghen- GNOCCHI gen- GNOME? gno- GNOMON gno- GNOSIS gnd-
1565:GOAD ghei-1 GOAT ghaido- GOD gheu(e)- GODSEND sent- GOFFER webh- GOLD ghel-2 GOLIARD gWel-3 GOMPHOSIS gembh- -GON genu-! GONAD gene- GONFALON gWhen-1 GONIOMETER genu-1 GONIOMETRY genu-! GONION genu-! GONO- gena- coop ghedh- GOOSE! ghans- GORE! ghaiso- GORE? ghaiso- GORGE gWere-4 GORGET gWera-4 GORSE ghers- GOSHAWK ghans- GOSLING ghans- GOSPEL spel-3 GOSSIP s(w)e- GOUACHE akWa- GOWAN ghel-2 GRAB! ghrebh-1 GRABEN ghrebh-2 GRACE gWera-3 GRACKLE gera-2 GRADE ghredh- GRAFFITO gerbh- GRAIN gre-no- GRAM! § gerbh- GRAM? gre-no- -GRAM gerbh- GRAMA gras- GRAMINEOUS_ gras- GRAMMAR gerbh- GRAMPUS_peisk- GRANADILLA gfe-no- GRANARY gre-no- GRANDILOQUENCE tolkw- GRANGE gre-no- GRANITE gr@-no- GRANT kerd-1 GRANULE gre-no- GRAPE ger-2 GRAPH gerbh- -GRAPH gerbh- -GRAPHER gerbh- GRAPHIC gerbh- GRAPHITE gerbh- -GRAPHY gerbh- GRAPNEL ger-2 GRAPPA ger-2 GRAPPLE ger-2 GRASP ghrebh-1 GRAss_ ghré- GRATE! grat- GRATE? kert- GRATEFUL gWere-3 GRATIFY gWere-3 GRATIS gWera-3 GRATITUDE gWero-3 GRATUITY gWera-3 GRAUPEL kreup- GRAVE! ghrebh-2 GRAVE? gwWera-2 GRAVES ghrebh-2 GRAVEL ghréu- GRAVID gWera-2 GRAVURE ghrebh-2 GRAY gher-3 GRAYWACKE wegh-
1571:Grus_ gere-2 GUARANTY wer-5 GUARD wer-4 GUERDON lau-, wi- GUERRILLA wers-1 GUESS ghend- GUEST ghos-ti- GUIDE weid- GUILD gheldh- GUILDER ghel-2 GUILE weik-2 GUIPURE weip- GUISE weid- GULAR gWel-3 GULDEN ghel-2 GULES gwWel-3 GULF kwelp- GULLET gWel-3 Gum? ghéu-
1845:MEGALO- meg- MEGALOCARDIA kerd-1 MEGALOPOLIS_ pele-3 MEIOSIS mel-2 MEISTERSINGER sengh- MELANCHOLY ghel-2, mel-2 MELANGE meik- MELANO- mel-2 MELD! meldh- MELILOT melit- MELINITE mélon MELIORATE mel-4 MELIORISM mel-4 MELISMA mel-3 MELLIFEROUS melit- MELLIFLUOUS bhieu-, melit- MELODRAMA mel-3 MELODY mel-3, wed-2
1914:NIBBLE ken-2 NICE ne, skei- NICHE nizdo- NICKNAME aug-? NICTITATE kneigh- NIDDERING nei- NIDE_ nizdo- NIDIFY dhé-1, nizdo- NIDUS nizdo- NIECE nepot- NIELLO negW-ro- NIFLHEIM nebh-, tkei- NIGGARD_ ken-2 NIGH néhw-iz NIGHT nekw-t- NIGHTINGALE ghel-1 NIGHTMARE mer-2 NIGRESCENCE neg¥-ro- NIGRITUDE neg¥-ro- NIGROSINE negW-ro- NIHILISM ne NIHILITY ne
2108:POCO pau- POCOCURANTE ciira -POD ped-1 PODAGRA ag-, ped-1 PODESTA poti- PODIATRY ped-! PODITE ped-! PODIUM ped-1 PODOPHYLLIN bhel-3, ped-1 PODZOL ghel-2, ped-1 POEM kWej-2
```


## [2026-09-06T02:16:09.283Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== watkins chalaza ===\"; grep -n -i \"chalaza\\|ghelad\\|gheled\" AHD_watkins1985.txt | head -20\necho \"=== KLN chalaza ===\"; grep -n -i \"chalaza\" KLN_1966.txt | head -20\necho \"=== KLN chlorine ===\"; grep -n -i \"^chlorine\\|chlorine,\" KLN_1966.txt | head -10\necho \"=== KLN melancholy ===\"; grep -n -i \"melancholy\" KLN_1966.txt | head -10",
 "description": "Grep Watkins/Klein for chalaza etc"
}
```


### [2026-09-06T02:16:09.400Z] TOOL RESULT

```
=== watkins chalaza ===
513:ghelad-
515:gheled-. Hail. Zero-grade form *ghled- in Greek khalaza (< *khalad-ya), a hailstone, hard lump, also a small cyst: CHALAZA, CHALAZION. [Pok. ghelsd- 435.]
1342:CENTROBARIC gWere-2 CENTUM dekm CENTURY dekm CEPHALIC ghebh-el- CEPHALO- ghebh-el- -CEPHALOUS ghebh-el- CERAMIC ker-4 CERASTES ker-! CERATODUS dent-, ker-1 CERATOID ker-! CEREAL ker-3 CEREBELLUM ker-1 CEREBRUM ker-1 CERES ker-3 CERTAIN krei- CERVINE ker-1 CERVIX ker-1 CESSION ked- CESSPOOL spirare cEsTus! kent- CEsTUS? kae-id- CHAETA ghait- CHAETOGNATH genu-2, ghait- CHAFE dhé-1, kele-1 CHAFER gep(h)- CHAFF! gep(h)- CHAIR sed-1 CHALAZA gheled- CHALAZION gheled- CHALCID ghelegh- CHALCOCITE ghelegh- CHALCOPYRITE ghelegh- CHALCOsIS ghelegh- CHALICE kal-1 CHALLENGE kel-8 CHALONE ghé- CHAMAEPHYTE dhghem- CHAMBER kamer- CHAMELEON dhghem- CHAMFER bhreg- CHAMFRON kaput CHAMOMILE dhghem-, mélon CHANCE kad- CHANCEL carcer CHANCELLOR carcer CHANCRE kar-1 CHANGE skamb- CHANT kan-
=== KLN chalaza ===
7100:cetin,  n.,  a  crystalline  fat  forming  the  chief  com¬ ponent  in  spermaceti  ( chem .)  —  Formed  with chem.  suff.  -in  fr.  L.  cetus,  ‘whale’.  See  Cetacea, cetology,  n.,  that  part  of  zoology  which  deals with  the  whales.  —  Compounded  of  Gk.  yfcoc, ‘whale’  (see  ceto-),  and  -Xovia,  fr.  -Xoyo ���one who  speaks  (in  a  certain  manner) ;  one  who  deals (with  a  certain  topic)’.  See  -logy, cetyl,  n.,  a  univalent  radical,  C16H33,  occurring in  spermaceti,  beeswax  {chem.)  —  Formed  with suff.  -yl  fr.  L.  cetus,  ‘whale’.  See  Cetacea, chabazite,  chabasite,  n.,  a  hydrous  silicate  (mi¬ neral.)  —  Formed  with  subst.  suff.  -ite  fr.  Gk. yaPa^is:  (occurring  in  the  poem  Hep!,  XESiwv ascribed  to  Orpheus),  an  erroneous  reading  for yaXa^is,  vocative  of  yaXa^iop,  name  of  a  pre¬ cious  stone,  lit.  ‘resembling  hailstone’,  fr.  yaXa^a, ‘hail,  hailstone’.  See  chalaza. chablis,  n.,  light,  white  Burgundy  wine.  —  Named from  Chablis,  a  town  in  the  Department  of Yonne  in  France.
7123:chalana,  n.,  a  kind  of  barge.  —  Sp.,  fr.  VL.  che- landium,  fr.  Late  Gk.  yeXavSiov. chalaza,  n.,  1)  the  part  of  an  ovule  where  the  in¬ teguments  are  united  to  the  nucellus  (bot.); 2)  one  of  the  two  spiral  albuminous  chords  in the  white  of  an  egg  (zool.)  —  ModL.,  fr.  Gk. yaXcc^a,  ‘hail,  hailstone,  lump’,  which  stands  for *yxXaS-ia  and  is  cogn.  with  OSlav.  zledica, ‘frozen  rain’.  Cp.  next  word.  Cp.  also  chabazite. chalazion,  n.,  a  small  tumor  in  the  eyelid  (med.)
7124:—  Medical  L.,  fr.  Gk.  yaXa^iov,  dimin.  of XaXoryx,  ‘hail;  pimple,  small  tubercle’.  See chalaza.
=== KLN chlorine ===
7474:chlorine,  n.,  name  of  a  nonmetallic  element  be¬
7507:choledocho-,  combining  form  meaning  ‘contain¬ ing  bile’.  —  See  prec.  word, choler,  n.  —  ME.  coler,  colere,  fr.  OF.  colere  (F. colire),  ‘choler,  anger',  fr.  L.  cholera,  fr.  Gk. yoXepa,  'bilious  diarrhea,  cholera’,  fr.  yolrh  also y6Xo c,  ‘gall,  bile’,  which  is  rel.  to  y'k'joc,  ‘greenish- yellow  color’,  yko^eiv,  ‘to  be  green’,  yluicib', ‘greenish-yellow,  pale  green,  green,  fresh’,  and cogn.  with  Avestic  zara-,  ‘gall,  bile’,  L.  fel, OSlav.  zluci,  Russ,  zelc.’,  Lith.  tulzis  (metathesis for  *zultis ),  Lett,  zults,  OE.  gealla,  galla,  ‘gall, bile’,  fr.  I.-E.  base  *ghel-,  *ghel-,  ‘to  shine;  yel¬ low,  yellowish  green,  green’.  See  yellow  and  cp. gall,  ‘bile’.  Cp.  also  next  word,  Chloe,  Chlorella, chlorine,  Chloris,  and  the  second  element  in melancholy,  Chrysochloris,  Echinochloa.  Cp.  also the  second  element  in  bezoar. cholera,  n.  —  L.  cholera,  fr.  Gk.  xoXepa,  ‘bilious diarrhea’,  fr.  yoTcq,  ‘gall,  bile'.  See  prec.  word, choleraic,  adj.,  related  to,  or  resembling,  cholera. —  Formed  from  prec.  word  with  suff.  -ic. choleric,  adj.  —  MF.  (=  F.)  choleriqtie,  fr.  L. cholericus,  fr.  Gk.  yokepixo^,  fr.  ydkipdi,  (see choler  and  -ic) :  first  used  by  Chaucer. Derivatives:  choieric-ly,  adv.,  choieric-ness,  n. cholesterine,  n.,  cholesterol.  —  See  next  word and  chem.  suff.  -ine.
7614:Chrysemys,  n.,  a  genus  of  American  turtles  (zool.) —  ModL.,  compounded  of  chrys-  and  Gk.  cpu;, ‘fresh  water  turtle’.  See  Emys. chryso-,  before  a  vowel  chrys-,  combining  form meaning  ‘gold,  golden,  golden  yellow’.  —  Gk. Xpono-,  xpu or-,  fr. /putt6;,  ‘gold’.  See  chrysalis, cbrysoberyl,  n.,  a  semi-precious  stone  (mineral.) — •  L.  chrysoberyllus,  fr.  Gk.  / poco  |3  f] poXXo ; , which  is  compounded  of  /poao ;,  ‘gold’,  and pfjpuXXo;,  ‘beryl’.  See  chrysalis  and  beryl. Chrysochloris,  n.,  a  genus  of  moles  (zool.) ModL.,  lit.  ‘golden  yellow’,  compounded  ofGk. Z_pu <r6;,  ‘gold’,  and  /Xiopo;,  ‘greenish  yellow  , See  chrysalis  and  chlorine, chrysolite,  n.,  a  magnesium  iron  silicate.  —  ME. crisolite  (F.  chrysolithe),  fr.  L.  chrysolithus ,  fr. Gk.  /pucAXiffo;,  which  is  compounded  of Xpucjo;,  ‘gold’,  and  Xifloc,  ‘stone’.  See  chrysalis and  -lite.
17111:halogen,  n.,  any  of  the  four  chemical  elements chlorine,  bromine,  iodine,  fluorine.  —  Lit.  ‘salt- producer’,  coined  by  the  Swedish  chemist  Baron Jons  Jakob  Berzelius  (1779-1848)  fr.  Gk.  dike,, gen.  aXo?  (masc.),  ‘salt’,  and  yEvvav,  ‘to  pro¬ duce’.  See  halo-  and  -gen.
19251:-ine,  also  -in,  suff.  used  in  chemistry  to  form t)  names  of  alkaloids  and  bases  (as  cocaine, aniline,  etc.);  2)  names  of  elements  (as  bromine, chlorine,  etc.)  —  F.  -ine,  fr.  Latin  adj.  suff.  -ina, fem.  of  -inus.  See  1st  adj.  suff.  -ine.
=== KLN melancholy ===
3869:atrabiliary,  adj.,  melancholy,  hypochondriac.  — Medical  L.  atrabiliarius,  ‘suffering  from  black bile’,  fr.  L.  atra  bilis,  ‘black  bile,  melancholy’, loan  translation  of  Gk.  piXctivoc  yoXf)  (see  me¬ lancholy).  Atra  is  fem.  of  ater,  ‘black,  dark’,  rel. to  Umbr.  atru,  adro  (neut.  pi.),  ‘black’,  and prob.  cogn.  with  OI.  atharvan-,  Avestic  a&ra- van-,  ‘fire  priest',  dtarsh,  ‘fire’,  atrya-,  ‘ashes’. Arm.  airem,  ‘I  light  up,  kindle’.  Cp.  atrocious. Cp.  also  Atharvan.  For  the  etymology  of  L.  bilis see  bile.  For  the  ending  of  atrabiliary  see  adj. suff.  -ary.
6224:calo-,  combining  form  meaning  ‘beautiful’.  — Gk.  xotXo-,  fr.  x«Xbp,  ‘beautiful’,  which  is  cogn. with  OI.  kalyah,  ‘healthy’.  Cp.  calisthenics,  Ca¬ lista,  Callicarpa,  Callicebus,  calligraphy,  Cal¬ listo,  Calluna,  calomel,  caloyer,  Hemerocallis, Hymenocallis,  kaleidophone,  kaleidoscope, calomel,  n.,  mercurous  chloride,  HgCl  (chem.)  — F.,  prop,  ‘beautiful  (i.e.  white)  substance  de¬ rived  from  black',  fr.  Gk.  xaXop,  ‘beautiful,  fair  , and  puXx S,  ‘black’.  See  calo-  and  melancholy. Calonyction,  n.,  a  genus  of  plants  of  the  morning- glory  family  (bot.)  —  ModL.,  compounded  of calo-  and  Gk.  vuxtio;,  ‘nightly’,  fr.  gen. vuxtop,  ‘night’.  See  night  and  cp.  nycti-. Calophyllum,  n.,  a  genus  of  plants  of  the  balsam- tree  family  (bot.)  —  ModL.,  compounded  of calo-  and  Gk.  <pvXXov,  ‘leaf’.  See  phyllo-. calorescence,  n.,  transference  of  heat  rays  into light  rays  ( phys.)  - —  Coined  by  the  British  physi¬ cist  John  Tyndall  (1820-93).  The  word  is  in¬ correctly  formed.  The  correct  form  would  be calescence,  fr.  L.  calescens,  pres.  part,  of  cale- scere,  ‘to  grow  hot’,  inchoative  of  calere,  ‘to  be hot’.  See  caldron  and  -escence  and  cp.  cales¬ cence  and  calori-.
7507:choledocho-,  combining  form  meaning  ‘contain¬ ing  bile’.  —  See  prec.  word, choler,  n.  —  ME.  coler,  colere,  fr.  OF.  colere  (F. colire),  ‘choler,  anger',  fr.  L.  cholera,  fr.  Gk. yoXepa,  'bilious  diarrhea,  cholera’,  fr.  yolrh  also y6Xo c,  ‘gall,  bile’,  which  is  rel.  to  y'k'joc,  ‘greenish- yellow  color’,  yko^eiv,  ‘to  be  green’,  yluicib', ‘greenish-yellow,  pale  green,  green,  fresh’,  and cogn.  with  Avestic  zara-,  ‘gall,  bile’,  L.  fel, OSlav.  zluci,  Russ,  zelc.’,  Lith.  tulzis  (metathesis for  *zultis ),  Lett,  zults,  OE.  gealla,  galla,  ‘gall, bile’,  fr.  I.-E.  base  *ghel-,  *ghel-,  ‘to  shine;  yel¬ low,  yellowish  green,  green’.  See  yellow  and  cp. gall,  ‘bile’.  Cp.  also  next  word,  Chloe,  Chlorella, chlorine,  Chloris,  and  the  second  element  in melancholy,  Chrysochloris,  Echinochloa.  Cp.  also the  second  element  in  bezoar. cholera,  n.  —  L.  cholera,  fr.  Gk.  xoXepa,  ‘bilious diarrhea’,  fr.  yoTcq,  ‘gall,  bile'.  See  prec.  word, choleraic,  adj.,  related  to,  or  resembling,  cholera. —  Formed  from  prec.  word  with  suff.  -ic. choleric,  adj.  —  MF.  (=  F.)  choleriqtie,  fr.  L. cholericus,  fr.  Gk.  yokepixo^,  fr.  ydkipdi,  (see choler  and  -ic) :  first  used  by  Chaucer. Derivatives:  choieric-ly,  adv.,  choieric-ness,  n. cholesterine,  n.,  cholesterol.  —  See  next  word and  chem.  suff.  -ine.
12417:Derivatives:  dump,  n.,  dump-er,  n.,  dump-ing,  n. dump,  n.,  sadness,  melancholy.  —  Rel.  to  G. Dampf,  ‘steam,  vapor’,  dumpf  ‘hollow,  gloomy, musty’,  Dan.  dump,  ‘dull’,  and  to  E.  damp  (q.v.) Derivatives:  dump-ish,  adj.,  dump-ish-ly,  adv., dump-ish-ness,  n.
17829:hip,  n.,  melancholy.  —  For  hyp,  which  is  short  for
17837:hipped,  adj.,  depressed.  —  Formed  with  suff.  -ed fr.  hip,  ‘melancholy*.
17838:hippish,  adj.,  somewhat  depressed  ( colloq .)  — Formed  with  suff.  -ish  fr.  hip,  ‘melancholy*, hippo-,  before  a  vowel  hipp-,  combining  form meaning  ‘horse*.  —  Gk.  fonro-,  bnr-,  fr.  (777704, ‘horse’,  rel.  to  dial.  Gk.  (xxo4,  for  I.-E.  *ekwos, whence  also  OI.  asvah,  L.  equus,  ‘horse*.  See equine  and  cp.  the  second  element  in  Eohippus, ephippium,  Philip,  Xanthippe, hippo,  n.  —  Short  for  hippopotamus. Hippoboscidae,  n.  pi.,  a  family  of  parasitic  blood¬ sucking  flies  ( entomol .)  —  ModL.,  formed  with suff.  -idae  fr.  hippo-  and  Gk.  (36<rxetv,  ‘to  feed*. See  botany.
18497:hypochondria,  n.,  morbid  depression  of  spirits, melancholy  (med.)  — -  L.  hypochondria,  gen. -drum,  ‘the  soft  part  of  the  body  from  the  ribs to  the  groin,  the  abdomen’,  fr.  Gk.  6xoy6v§pia, of  s.m.,  prop.  neut.  pi.  of  the  adjective  6x0- x6v8pio< ;,  ‘that  which  is  below  the  cartilage  (of the  breastbone)’,  formed  fr.  6x6  (see  hypo-)  and x6v8poc,  ‘granule,  gristle,  cartilage’.  See  grind.
23350:Melampyrum,  n.,  a  genus  of  plants,  the  cow- wheat  (bot.)  —  ModL.,  fr.  Gk.  fieXafr-rrOpov, ‘black  wheat’,  fr.  piXa?,  gen.  pteXavo?,  ‘black’, and  r.op/jc,  ‘wheat’.  See  melano-  and  pyrene, melan-,  form  of  melano-  before  a  vowel, melancholia,  n.  —  Late  L.  See  melancholy, melancholiac,  n.,  one  who  suffers  from  melan¬ cholia.  —  Formed  fr.  melancholia  with  suff.  -ac. melancholic,  adj.,  pertaining  to,  or  characterized by,  melancholy.  —  ME.  melancolik,  fr.  MF. (=  f.)  mdlancolique,  fr.  Late  L.  meiancholicus, fr.  Gk.  (ieXayyoXixAp,  fr.  (reXxyyo/ix.  See  next word  and  -ic.
23351:Derivative;  melancholic-al-ty,  adv. melancholy,  n.  —  ME.  melancolie,  fr.  OF.  melan- colie  (F.  mtlancotie),  fr.  Late  L.  melancholia,  fr. Gk.  pLEXotyxoXla,  ‘atrabiliousness’,  lit.  ‘black bile’,  fr.  piXS?,  gen.  piXavoc,  ‘black’,  and ‘bile’.  See  melano-  and  choler.
```


## [2026-09-06T02:16:15.076Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '7474,7476p' KLN_1966.txt\necho \"=== KLN glass ===\"; grep -n \"glass,  n\\.\" KLN_1966.txt | head -5\necho \"=== SKT chalaza/melancholy ===\"; grep -n -i \"melancholy\\|chalaza\" SKT.txt | head -10",
 "description": "Klein chlorine + Skeat"
}
```


### [2026-09-06T02:16:15.268Z] TOOL RESULT

```
chlorine,  n.,  name  of  a  nonmetallic  element  be¬
longing  to  the  halogen  family  (chem.)  —  Coined by  the  English  chemist  Sir  Humphrey  Davy (1778-1829)  fr.  Gk.  yXcopos,  ‘greenish  yellow, pale  green,  green,  fresh’.  See  Chloe.  For  the ending  see  chem.  suff.  -ine  and  cp.  brom-ine, fluor-ine,  iod-ine.  Derivative:  chlor in-ous,  adj.
Chloris,  n.,  name  of  the  goddess  of  flowers  in Greek  mythology;  later  identified  with  the Roman  goddess  Flora  (Greek  mythol.)  —  L.,  fr. Gk.  XXoipu;,  lit.  ‘greenness,  freshness’,  which  is rel.  to  yXoipoc.  See  prec.  word.
=== KLN glass ===
15724:2)  French.  —  Fr.  L.  Gallus,  ‘a  Gaul’.  Cp.  Gallic, galloglass,  gallowglass,  n.,  a  heavily  armed  re¬ tainer  of  an  Irish  chief.  —  Ir.  galldglach,  lit.  ‘a foreign  soldier’,  fr.  gall,  ‘foreigner’,  and  oglach, ‘servant,  soldier’,  fr.  OIr.  oclach,  ‘youth’,  which derives  fr.  OIr.  dac,  ‘young’.  See  young, gallon,  n.,  a  measure  equal  to  4  quarts.  —  ME. galoun,  fr.  AF.  galon,  corresponding  to  OF. jalon,  ‘a  liquid  measure’,  and  rel.  to  OF.  jale,  ‘a bowl’,  which  is  of  uncertain  origin.  F.  gallon, ‘gallon’,  is  an  English  loan  word, galloon,  n.,  a  braid  used  for  trimming.  —  F. galon,  fr.  galonner,  ‘to  lace,  braid  the  hair’, which  is  prob.  rel.  to  F.  gala,  ‘festivity’.  See  gala and  cp.  gallant.
16226:glass,  n.  —  ME.  glas,  gles,  fr.  OF.  glees,  rel.  to OS.  glas,  gles,  ON.  gler,  Dan.  glar,  MDu.,  Du. glas,  ‘glass’,  OHG.,  MHG.  glas,  ‘amber,  glass’, G.  Glas,  ‘glass’,  OE ,-glier,  ‘amber’,  and  cogn. with  L.  glaesum,  glesum,  ‘amber’,  OIr.  glass, ■green,  blue,  gray’,  W.  glas ,  ‘blue’,  Mir.  glaisin, ‘woad’,  fr.  I.-E.  base  *ghles-,  *ghles-,  ‘to  shine, glitter’,  which  is  an  enlargement  of  base  *ghel-, *ghel-,  *ghle-,  ‘to  gleam,  glimmer;  to  be  green or  yellow’.  Cp.  glare,  glaze,  glow.  Cp.  also  gleam and  words  there  referred  to.  Cp.  also  yellow. Derivatives:  glass,  tr.  v.,  glass-ful,  adj.,  glass-y, adj.,  gtass-i-ly,  adv.,  glass-i-ness,  n.
19964:isinglass,  n.,  a  gelatinous  substance  prepared from  the  airbladders  of  certain  fishes.  —  Cor¬ ruption  of  obsol.  Du.  huizenblas,  fr.  MDu.  huus- blase,  fr.  huus,  ‘sturgeon’,  which  is  rel.  to  OHG. huso,  of  s.m.,  and  blase  (=  Du.  blaas),  ‘blad¬ der’,  which  is  rel.  to  OHG.  bldsa,  of  s.m., blasan,  ‘to  blow’.  For  the  first  element  see  huso, for  the  second  see  blast  and  cp.  bladder.
=== SKT chalaza/melancholy ===
3285:Chagrin.  (K.-Turk?)  F.  ehapin, melancholy.  Diet  identifies  it  with  F. chagritt,  shagreen,  a  rough  stuff  taken  ai the  type  of  corroding  care  ;  see  Shac'e^ii*
5565:Dumps,    melancholy.    (Scand.) dial,    duifipin.    mclanchol)',    orig difftba.  to  sleom,  reek ;  Dan.  durn^ low.  +  Du.  domp,  damp,  hazy,  G damp.     Allied   to   Damp^   ct   *lo one's  spiiits.'
8961:humour,  orig.  moisture,  (F.  — L.)  See Trench,  Select  Glossary,  and  Study  of Words.  The  four  kumoun,  acconling  to Galen,  caused  the  four  temperaments  of miud,  viz.  choleric,  melancholy,  phlegmatic, and  sanguine.- O.  F.  kt4mor  {i .  Aumeur).
11355:Melanoholy.  sadoeta.  (F.-L Supposed  to  be  doe  to  an  excess  of bile/  M.  E.  meianchoHe.^O.  F. cholif.^h.  melan£h^lia  —  Gk.  ^txa melancholy.  — Gk.  n^X^yxoX^t,  jau —  Gk.  iii\a¥',  stem  of  liiXct,  black bile,  gall.  Cf.  Skt.  mala,  dirty, black ',  and  see  O&IL
```


## [2026-09-06T02:16:19.664Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in مالیخولیا خولیا ژاله گیلاس کلر خیال; do echo \"=== $w ===\"; grep -c \"$w\" MON_part1.txt MON_part2.txt 2>/dev/null; done",
 "description": "Count Persian headwords in MON"
}
```


### [2026-09-06T02:16:21.437Z] TOOL RESULT

```
=== مالیخولیا ===
MON_part2.txt:4
MON_part1.txt:2
=== خولیا ===
MON_part2.txt:6
MON_part1.txt:2
=== ژاله ===
MON_part2.txt:0
MON_part1.txt:13
=== گیلاس ===
MON_part2.txt:17
MON_part1.txt:4
=== کلر ===
MON_part2.txt:50
MON_part1.txt:27
=== خیال ===
MON_part2.txt:38
MON_part1.txt:32
```


## [2026-09-06T02:16:24.147Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON مالیخولیا ===\"; grep -n -m6 \"مالیخولیا\" MON_part1.txt MON_part2.txt | cut -c1-600\necho; echo \"=== MON ژاله ===\"; grep -n -m8 \"ژاله\" MON_part1.txt | cut -c1-500",
 "description": "Grep Mo'in entries"
}
```


### [2026-09-06T02:16:24.237Z] TOOL RESULT

```
=== MON مالیخولیا ===
MON_part1.txt:80978:مالیخولیایی. دیو انه» مجنون. عاشق. 
MON_part1.txt:88718:مالیخولیا. 
MON_part2.txt:43025:مالیخولیا: ]21 [مصحف. مالنخو لا» 
MON_part2.txt:43059:مالیخولیا؛ ماخولیا» ملتخولیا؛ مالیخ؛ مالنخ ۲ 
MON_part2.txt:52320:پردة صفاق. (بز. قد.) نوعی مالیخولیا که آن 
MON_part2.txt:54762:گرم و مرطوب. ۳ -مزاج مالیخولیایی 

=== MON ژاله ===
1060:آ کم بلور. بح. . ژاله» شبنم. تگرگک. 
1216:ایستاده» ژاله. برف. تک رگ. یخ. مسبشه » 
6648:اپشک : ۸05۵1 [- بشکک ] (ا.) شبنم» ژاله. 
15109:منم ژاله. 
32089:سبزی نشیند؟ شبنم» ژاله» بژ» صقیم» ایشک» 
32184:پشسنگک: -021272 (ا.مسصف.) ژاله. 
46750:جاله: (ه-):121 [- ژاله] (.) قطعاتی از چوب 
48248:جلید: 1:14 (ع.] (ا.) بخ. شبنم» ژاله.
```


## [2026-09-06T02:16:28.331Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '43015,43065p' MON_part2.txt | cut -c1-300",
 "description": "Read Mo'in malikhulya region"
}
```


### [2026-09-06T02:16:28.397Z] TOOL RESULT

```
خراج» ارتفاغ. ضح.- (حق. مال.) مالیات 
برمی‌دارد تا بتواند مخارج مملکتی را که نفع 
بیردازد (قوانین ادا ۳۷ مالبات غبر 
مستقیم: : مالیاتی رز مالبات دهنده بطور 
غیر مستقیم می‌پردازد» کر 
ار رویط در ضمن 
خررند جنس پرداخته می‌شود. ۳ 
مالیاتی که 9 از مالبات دهنده کر فته 
می‌شو د. مانند مالبات الا کک مرروعی» 
اراضصی بابر» مستفلات و مالبات بردر آمد. 
مالیخولیا: ]21 [مصحف. مالنخو لا» 
تره جات ۱ رز ) (پز.) گونه‌ای مرض 
دماعی همراه منیا دنبالة فلج 
عمومی با تحت شکنجةً شدید روحی و 


مالیدن 


فرهنگ فار سی معین 


۱ ۵ ۹٩ 


سس تسس سب 


می‌دهند) و یا بر اثر مرض صرع یا در 
اشخاص هیستریک و یا بطور مادرزادی 
پدید آید. مبتلایان به این مرض گاه از 
خوردن و آشامیدن خودداری می‌نمایند به 
نحوی که به حالت مرگ می‌رسند و 
کٌاهی خو دکشی می‌کنند. برای معالجه این 
سماران استراحت کامل و مسافرت به نقاط 
خوش آب و هوا و جدا بودن از افراد دیگر 
و از حوادث لازم است. این معالجه باید با 
تجو بز داروهای مقوی قوای دماغی همراه 
باشد؛ مالثخولیا؛ خبط دماغ» صبارا» صباره. 
(روان.) یکی از عواطف مرکب است و آن 
از تذکر حالات مطبوع مفقود و از اندوه 
فعلی که آنها را احاطه کرده است و غیره 
ترکیب شده (دکتر سیاسی. روانشاسی تربیتی 
ص ۳۳۳). ضصح. «مالنخولیا» بصورت‌های: 
مالیخولیا؛ ماخولیا» ملتخولیا؛ مالیخ؛ مالنخ ۲ 
غیر ه در امده. 

مالیدن: 2121-07 (جماع کردن» ساییدن» 
مالبدن ] (مالید» مالد؛ خواهد مالید. بمال» 
مالنده» مالیده» مالش» ماله). (مص م.) دست 
کشیدن روی چیزی» چیزی را در دست
```


## [2026-09-06T02:16:38.414Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['MON'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['FSF'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['AFM'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['FVF'],ensure_ascii=False,indent=1))\n\"",
 "description": "Show ref details for BQT/MON/FSF/AFM/FVF"
}
```


### [2026-09-06T02:16:40.006Z] TOOL RESULT

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
 "notes": "Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Provenance caveat: picofile is a general file host, the uploads are not from a library; treat as a grey copy (the book is in copyright in Iran). | vol 4 (م–ی) OCR text, tesseract fas+eng, pages tagged [pdf page N], printed = pdf+1917 | vol 5 (ta'liqat) OCR text, printed = pdf-5 | vol 3 (ش–ل) OCR text (689/721 pages), printed ≈ pdf+1203..1209 | BQT_v2_pages.txt: printed page = leaf + 540 (verified by catch-lines at pp. 838-855, 869, 904); earlier estimate +543 was 3 pages off.",
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
 "title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/20220809_20220809_1444",
 "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"
 ],
 "page_offset": "484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking",
 "covers_etymology": false,
 "notes": "Persian OCR fair (readable prose). Mostly glosses; some Pahlavi/Avestan notes. Edition may differ from the 1363 Donya print Nourai used."
}
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
{
 "title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968",
 "kind": "website",
 "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)",
 "lookup_hint": "Alphabetical by Persian headword; noorlib page number N is the scan page — browser needed to read. Not on archive.org.",
 "local_file": null,
 "page_offset": null,
 "covers_etymology": true,
 "notes": "PDF exists on several Iranian sites (ketabnak/parsianjoman) but could not be fetched here (login/JS)."
}
```


## [2026-09-06T02:16:46.296Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v2 leaf 255 (printed 795) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==256' BQT_v2_pages.txt | head -60 | cut -c1-200",
 "description": "Print BQT vol2 leaf 255"
}
```


### [2026-09-06T02:16:47.832Z] TOOL RESULT

```
=== BQT v2 leaf 255 (printed 795) ===
 ‫روانند که سپاهیان‬
                 ‫ویفتح اول‌قندیل و تیردان گ‬       ‫تالف لوام مان كف رازا سرا زا‬
                          ‫از گردنآویز ند ‪.۴‬‬                                              ‫گونند ‪.‬‬
‫خولبا = بورزن توتیا »چیزیرا گوند‬                   ‫خو لنجان ‪ -‬بروزن سورنجان ‪ ۰‬ينی‬
‫کرس خواهد‬
        ‫که مالعتصرف دداشته‌باشد بمنی ه‬            ‫است دوایی ‪ ۰ ۱‬وآنرا درآشیان بازبابند و بغیر‬
                          ‫آرا تصرف کند ‪.۴‬‬          ‫اشزبآان بازجایی دیگربهم نمیرسد » چه گویند‬
  ‫عربی‬
     ‫ویوف‬
        ‫‌معر‬
           ‫تون»‬
              ‫س‌ن‬
                ‫اوزن‬
                   ‫حون = بر‬                        ‫داروهمان‬      ‫رو‬
                                                                  ‫سو‬‫خزد‬
                                                                      ‫که آن از زمین ‪:‬ونان خی‬
                                                   ‫است وآنرا ریزه رمزه کردهآورند وآنرا برتکی‬
‫دگموبند ‪ -‬و بمعنی کشتن همهت ‪ ۱‬چنانکه‬
‫گوبند « فلانی خون کرده است >“ بکعنسیی را‬           ‫فره‌فاف خوانند ‪ .‬کرم وخشك‌است دردویم وسیم‪.‬‬

 ‫کشته است ‪ -‬ومردم خونی (‪ )۱‬قتال وسفاکهزا‬          ‫کویند درهردیگ وکاه که قدری ازآن باشد‬
‫نیزگوبند ‪ -‬وبمعنی خودی ‪ -‬وخود بیثی وتکبر‬                                    ‫کردآن نگردد ‪.‬‬    ‫مگ‬

‫هم بنظر آمده است ‪ -‬و باثانی مجهول‪ .‬بمعنی‬           ‫حو له = بصم اول وئانی مجهول پروزن‬
                                                   ‫لوله » بمعنی خالی باشد که قیض پر است ؟ ‪-‬‬

                                                                ‫و ‪.‬‬   ‫(‪ )۱‬چك“ چش ‪+:‬‬

                    ‫‪ » Galanga‬لك ‪ ۲‬ص ‪۱٩‬‏ » و رك ‪ :‬تحغة حکیم ممن ‪.‬‬                 ‫‪۱‬‏ =‬
  ‫«خوله‪ .‬تبرداای‬     ‫‪۴‬‬         ‫‪ - ۴‬در کیلکی ‪ ×410‬بممنی سوراخ است ‪ .‬رك ‪ :‬خل ‪.‬‬
   ‫‪ - ۴‬خولادرکلمة مر کب «مالبخولا»(ه‪.‬م‪).‬و«مالنخولا»‬           ‫بکهو‌دغازبان‌دارند» «لغت‌فری ‪. ۵844‬�
   ‫® ‪ -‬پهلوی ‪ « 201‬تا ‪888۳۵8۵02, ۳05,» ۹۳۱‬‬                      ‫ازیونانی ‪ 610‬است بممنی صفرا ‪.‬‬
    ‫(خون‌دار) » کردی ‪ ,08‬افغانی ‪. 601۷‬بلوچی ع ‪nûh‬‏ ‪, .nêh‬وخی ‪naxuv‬‏ ‪ .‬شقنی ‪81۷‬‬
   ‫سربکلی ‪. 1102۷‬مسنکلیچی ‪« 012۷‬اسشق ‪ ۱۱۵‬و رك ‪ :‬اسفا‪ ۱:۲‬ص ‪۸۹۲۱ ۰۹۲۰ ۹۹۰ ۷۰‬‬
   ‫؛ کیلکی‬    ‫ءاشکاشمی ‪nêw‬‏ ‪ ۶‬گربرمن ‪۰۰۱‬‬       ‫سیوندی ‪« 011‬هو بشمان ‪۱۱۵‬‬        ‫‪۷۸۳۰ A‬‬       
 ‫؛ ماده‌ای قرمز رنك وسیال که در رگهای بدن(وربدها وشربانها)جربان دارد و هر کب است ‪۰‬‬            ‫×‬
   ‫داوزقسمت ‪ -۱ :‬لول های کوچکی بنام « کلبول قرمز» و «گلبول سفید» ‪ ۲ .‬م‪-‬اد سیالی‬
        ‫در بدن دارد ‪.‬‬    ‫وهمی‬
                            ‫هع‬‫فدهد‬
                                 ‫ظلیمی‬
                                     ‫وکی‬
                                       ‫» که قسمت اعظم خون را تش‬                   ‫ما‬
                                                                                   ‫س‪:‬‬‫لمابه‬
                                                                                         ‫پسو‬
                                                                                           ‫مو‬
       ‫که هیچ چیز لهییئی حلال جزخوش ‪.‬‬               ‫‪ - ۱‬بگرد درهمه باب ملك هستی او‬
   ‫«کلتان ‪.»۲۸۷‬‬
                                                ‫؛ رك ‪ :‬خن › خانه ‪.‬‬     ‫‪ - ۷‬نهرانی ‪8005‬‬

                                                                               ‫قته از صفحهٌ ‪6۹۷‬‬
  ‫الست که بابد پرنده ای‌بسبار کوچك باشد ‪ « :‬خولی بکفم بهز‬
                                                        ‫‪- ۲‬پازییندمث‬
                                                                                  ‫کلنگی بپوا » ‪:‬‬
             ‫از درختی بدرختی‌شود و کوبد ‪:‬آ‪!۰‬‬          ‫خول‌طنبوره توگوبی زند ولاسکوی‬
   ‫«منوچپری داهفانی ‪۲۵۱٩‬‏ ‪.‬‬

    ‫‪( -۸‬عر) هخول‪ ,‬آن چیزبتکه داده است خداترا از چارپابان و بند گان وکنیزان‬
   ‫( عر ) «خال‪ .‬سی پرستاری کرد و مصدرآن خول‬           ‫‪-‬‬                ‫وخدمتکاران»«شرح قلموس؟ ‪.‬‬
   ‫‪ ۰‬ص=‪uicyL‬‏ لك س ‪Yo‬‏‬                         ‫بفتح اول وخیال بروزن کتابست ‪« ».‬شرح فاه‌وی؟ ‪.‬‬
                                                                       ‫ورگ ‪ :‬تحفة حكيم موّمن ‪.‬‬
```


## [2026-09-06T02:16:55.345Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\ngrep -n \"pdf page 30\\]\" BQT_v4_pages.txt | head\necho \"---\"; awk 'BEGIN{RS=\"\\f\"} /\\[pdf page 30\\]/' BQT_v4_pages.txt | cut -c1-200 | head -70",
 "description": "BQT vol4 pdf page 30"
}
```


### [2026-09-06T02:16:56.944Z] TOOL RESULT

```
1063:[pdf page 30]
---
[pdf page 30]
۱۹۵۷ مالخولا
کلوبندء را (۱) گوبند و آن غلامی باشد که | مالش ومالندگی‌هم هت ‎٩‏ -
رتیه بزرگی رسیده باشد چه کلو (۲) بمعنی مالی - بر وزن خالی . بممتی بیار
بز رکه است - و شکم پرست و جوعیرا نیز | و فراوان باشد ۷ - و بلغت بودانی انکیین دا
کفته‌اند . کویند که عبل باعد ۸ - ودرملك دکن باغبانت
هالّه ۱ - بروزن‌خاله. تخته‌ای راکوبند | را مالی میگویند .
که برزیگران بر زمین (۳) شیارکرده بکشند مالیا < بروزن بالیا . «رختی‌است بلريك
ا کلوخهای آنرا نرم کند و زمین را همواد | و درا زکه از چوب آن درخت نیزه و تیور سلزند
سازد ۴ - و افزاری که کلکاران بدان کاهگل | - و بلفت بوتانی بممنی میاء باشد. که در برایر
وکج (4) وآحك ۳ سفید ات ‎٩‏ +
بردیوار مالند۴ مه مالیخ *۱- بائاك بتحتا ی کشیده ویتای
و افزاری که ماله نقطه دار زده ۰ بممتی مالیخولیاست که کوقت
جولاهگان از خی بمانند جاروب و لیف‌سازین | و اخلل دماغی و سودا و خیال خام پلشد -
ربا آن تانه را آهار دهند ۴ - و بمعتی‌مالامال مالیخو لیا ۱۱- بممنی مالیخ اس ت که
هم آمده اس ت که پر و لبربز باشد 8 - وبممنی | کوفت و خلل دمانغی وسودا و خیال خلم باشد -
(۱) چك : کلوبنده را . (۷) چك :کلو . (۳) چش : بزمین .
(4) چش : کچ .
از : مال ( مالیدن )۸ ( پسوند اسم آلت ) » معرب آن «مالق» « تقی > -
۴ - بر زگر دفت و نان و دوغ ببرد ماله و جفت و دای وبوغ ببرد .
سنائی غزتوی « رشیدی >
۴ <معرب « مألج » « المنجد > . ۴ - ... دیشی دارد چوماله آلوده بهیت -
عمارة مروزی « لفت فری چاپ هرن ص ۸۰ > و رك : فرهنگه نظام ‏
8 - سیکیی ده بخانه وام شدست پنج ازآن خوله پنج ازآن ماله .
سوزلی سمرقندی « رشیدی * -
‎٩‏ - از : مال (مالیدن) ۸۰7 (پسوند اس مصدر). ۷ -اين بیت را شاهدآوردماند :
هر که سرمايةٌ.ماهی زتو دارد حاصل آفتابش ز دل ستکه برآید مالی-
سیف اسفرنگه « رشیدی > -
مولف فرهنگه نظا کوید : « شاید در شمر مذ کور « حالی > تصحیف خوانی شده .> ور4: ماله.
مالامال ۰ ۸ - بونانی 5261 ( عل ) « آشتینگای > .۰
‎٩‏ - یونانی 336185 ( سیاء ) « اختینگای ». ۰ رد : مالیخولیا +
۱- مسحف مالنخولیا » لانینی 3361810112 از بودانی 126188870112 « حزی
چ ۷ س ۵۹۵ ۶ اشتینگای : مالنخولیا >۰ مر کب از 33618008 ( سیاء ) و 1018 (خلط
صفرا) جمماً بدمنی خلط سیاء , چون مرش مذ کور سوداوی است لپذا باین اسم‌خوادماند , وآن
نوعی از جنونست که در فکر فاد بهم وسد ولی صاحب آن بکسی ایذا نرساند « غیاث > . این
لفت بسور ماخولبا » ملنخولیا , مالیخ » مالنخ و غیره در آمده است .
```


## [2026-09-06T02:17:07.687Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==518' BQT_v2_pages.txt | cut -c1-200 | head -60",
 "description": "BQT vol2 leaf 517 (printed 1057)"
}
```


### [2026-09-06T02:17:09.456Z] TOOL RESULT

```
  ‫زين‬                                                                                              ‫‪۵‬‬
                                                                                                   ‫ت‬ ‫یی‬
                                                                                                      ‫ا‬


                             ‫بر روی خمیر نان پاشند‪.‬‬      ‫زنهار ‪ ۴‬است که بناه‬         ‫ربنهار ‪۳‬‬
‫رلو ار » با نالی مجهولبروزن دیوار ‪.‬‬                         ‫ویمان‬
                                                                ‫جستن و امان خواستن باشد ‪ -‬و عهد پ‬
       ‫معنی سوبت وماوی بودن وبرابری باشد‪.‬‬                   ‫‪ -‬و تری‌وبيم ‪ -‬و شکایت را لکیوزیند ‪-‬وبمعنی‬
 ‫هه‬              ‫بگر‬     ‫ی‬         ‫‪۷‬‬        ‫ی‬                 ‫هآی‬ ‫او‬‫گعجل‬
                                                                       ‫افوس و حسرت ‪ -‬وامات ‪ -‬وت‬
‫بمعنی(ژ شت‬            ‫' = بروزن ده‬     ‫لو‬
                                        ‫زر‬
                                                                                          ‫لیزآمده است ؟ ‪.‬‬
‫و آرایش باشد ‪ -‬و آنچه بدان زبنت و آرایش‬
                                                            ‫ر بنهاری = یناه آورنده ‪ -‬ویناه داده‬

‫لرین = بفتح اول بورزن زمین ؛ بلغت‬                           ‫‪-‬در عوهادمان کی در‬
                                                                             ‫شده ‪ -‬وعهد بسته ‪ ۴‬و‬
                                                                                      ‫‪.‬‬   ‫آمدن را گو شد ‪۵‬‬
‫زد وپازند (‪ )۱‬بمعنی دراز وبلند باشد که‌نقیض‬
        ‫وور کا‬                                   ‫کا‬         ‫ز)نیان ‪ - ۱‬بابای‌حطی بروزن‌میهمان‪,‬‬
                                                         ‫زینان امت که الخواه باشد‪ .‬وآن نخمی‌است که‬




                                                                        ‫(‪ )۱‬چك ‪ :‬ژند وپاژند ‪.‬‬
 ‫‪۳1,‬‬       ‫‪ - ۱‬بهلوى ‪( 41112‬امن‪.‬امان)» ‪-‬قدی ‪( 11/2‬بناه‪.‬امان) رك‪ :‬مقالهةٌ ‪6/7۲۳‬‬
      ‫ص‪.۵ ۵۸‬‬     ‫‪ 2‬شمارء ‏‬       ‫چاپ ماساچوست‌ح ‪۷‬‬       ‫درمعر فی تارمخ عرب تالف هتی ‪»,mulucepS‬‏‬

      ‫‪ 590‬آرامر کب‌از‪0128 ۲201 :‬میداند‪ .‬بعنی‌ازین پر هرز ‪ ۲۳. ۲611(1)۷۱.‬آنراعاوستابی‬
      ‫(سلاح‌حامی )میداند هوبشمان گوی که وجه‌اخیر بنظرمن بهتراست «هویشمان‬                   ‫‪60622 .3‬‬
  ‫‪ - ۴‬در بت ذبل لختن بمعنی‬                        ‫‪.‬‬   ‫ار‬
                                                       ‫ه‪:‬‬‫زنرك‬
                                                            ‫‪۳‬‬                    ‫‪ :‬احق ‪. ۷۲۰‬‬       ‫‪ ۷‬ور‬
                                                ‫و دوم‌یمعنی ”یناه ‪ ۰‬حمایت؟ است ‪:‬‬      ‫‪ ۵‬بپرهیز ‪ ۰‬حذرکن؟‬

                ‫حان مرا «دین فلك ز هار خوار‪.‬‬                    ‫مگذار ز‪:.‬هار چو در زهار تت‬
  ‫‪.‬‬     ‫‪ °‬ھچ‬    ‫سعد‬   ‫معود‬   ‫‪۶‬‬

               ‫® _ از‪ :‬زبنهار‪-۳‬ی (حاصل مصدر) ‪.‬‬                 ‫نزه‪:‬ار(‪-‬ی ( ست ) ‪.‬‬
                                                                                ‫زی ا‬
                                                                                   ‫‪۴‬‬
                                   ‫_ سفدی ‪. ۲۷۷72‬‬       ‫‪۲‬‬           ‫‪.‬‬   ‫‪٠‬‏ زان‬    ‫رك ‪ :‬زان‬     ‫‪۹‬‬

             ‫‪Henning, Sogdian loan - words..., 505,2۰۰‬‬
           ‫زه ‪ , 22/8100 ۰ 2298280 ۰‬ىولېپ ‪ » 01200‬دنلپ ‪‎‬ركىوب« ‪. ۰ ۱۰۸‬‬                         ‫‪۸‬‬
```


## [2026-09-06T02:17:15.842Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"ژاله\" BQT_v2_pages.txt | head -20\necho \"--- leaf numbers ---\"\nawk 'BEGIN{RS=\"\\f\"} /ژاله/ {print \"LEAF \" NR-1}' BQT_v2_pages.txt",
 "description": "Find ژاله in BQT vol2"
}
```


### [2026-09-06T02:17:17.553Z] TOOL RESULT

```
30918:                   ‫پشت بندند ژاله گویشد‪.‬‬
30935:  ‫در سانسکریت‪( [802 ..‬سرد» خشك وبیح رکت) «اسشق‪ »4۸۱‬هوبشمان‌ژالهرا از‬                           ‫‪۴‬‬
30937:                  ‫چون غوره بخامی اسرون محکم ‪.‬‬               ‫چون ژاله بسردی اسرون موصوف‬             ‫‏*‬
30942:               ‫کرده براو حواله » فواص دردربا‪.‬‬             ‫ژاله‬   ‫اکلهه‬
30948:      ‫« کوحله» ‪« ۳‬حیاب» اقرب دالته‌اند نا مع؛ی قخيڭ ماد الدردمیدم» ‪ .‬رك‪:‬‬          ‫دو» کلمةٌ ژاله را نمی‬
--- leaf numbers ---
LEAF 519
```


## [2026-09-06T02:17:20.256Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==520' BQT_v2_pages.txt | cut -c1-220 | head -70",
 "description": "Print BQT leaf 519 (žāla)"
}
```


### [2026-09-06T02:17:22.030Z] TOOL RESULT

```
                                                                                               ‫وی ‪— ۵‬‬

‫و سیب آن چنان است که چون بشار بهوا رود‬                   ‫بأکله‌البعیریمنی علفی است که آنرا شتر خورد‬
‫وسرما درو اثرکند غلیظ شود وقطر‪ :‬بارانکردد‬                ‫‪-‬نوانه‬
                                                              ‫ورزن حرس خوالند ک‬
                                                                              ‫ویعربی غلیص ب‬
‫‌ در محل فرود آمدن فعل برودت زیاده درو‬                  ‫هرزه و یاوه و بی مزه و هذبان هم‬             ‫اسزخنان‬
‫تأثیر کند اورا بفشرد وبخ بندد ® ‪ -‬و شینم را‬                                                        ‫همست ‪. ۱‬‬

‫ایز گوبند و سبب آن چنان باشد که شدت‌سرما‬
                                                         ‫راو مك ‪ -‬بثالك بواورسیدہ و میم‬
  ‫یزن‬‫ززدموا‬
          ‫هوای صافی را غلیظ کند وبخار سا‬                 ‫مفتوح بکاف‌زده ‪ ۰‬لوببارا گویند‪,‬وآن تخمی‌است‬


‫اند کی بلند شود و بربر کهای ببانات شیند واز‬                             ‫که بعربی لیا خوانند بکسر لام ‪.‬‬
‫آن قطرها پدید کردد ‪٩‬‏ ‪ -‬و باران تساتراحم‬
                                                            ‫‪ll‬‬                            ‫‪۲‬‬    ‫‪‎ 4‬ا‬
                                                         ‫' = با زای قارسی بروزن تازه »‬              ‫‪2‬‬
‫کفته‌اند ‪ -‬وجاله را نیز گوبند؛ وآن‌چیزی‌باشد‬             ‫بمعنی زار است که علف‌بی‌مزه ‪ -‬کوذابه‌ازسخنان‬
‫که ازچوب وعلف سازند‪ .‬ومش‌کهلی پرباد برآن‬                                                      ‫باشف ‪۰‬‬    ‫هرزه‬


  ‫بوسی‬‫بندند وبرآن شته از آب گذرند ‪ ۷‬؛‬                    ‫ڪر ‪= ۴‬و بررنزن لااعغررا‪ .‬چچےینه‌دان‌مرغان‬
                                                                                                 ‫ژاغر‬
‫آن مشکهای برباد را و مشکی که شناوران بر‬                                 ‫را گوبند و بعربی حوصله خوالنف‪.‬‬
                   ‫پشت بندند ژاله گویشد‪.‬‬
‫او ب=كون واو » خالس وخلاصة هر‬
       ‫‪۰‬‬                                      ‫ھ‬
                                                         ‫کیاهی است دوابی شبیه‌بانگشتان چلیاسه وزفن‪.‬‬
                                     ‫‪۰‬‬   ‫چیز را گوند‬    ‫رال ‪ » ۴‬بروزن لاله‪ .‬تگرك رااگوند‬




             ‫که چرب کوبان آ بجا شود کند زبان ‪.‬‬             ‫‏‪ ٩‬کیکه ژاژ درابد بدرکیش نشود‬
  ‫‪۰‬‬        ‫(‪FA‬‏‬   ‫فری‬   ‫«لت‬   ‫فرخی‌سستالی‪.‬‬



  ‫‪ = ۴‬زاغر (ه‪.‬م‪ ).‬عنصری باخی درخطاب بساپزید بزاغگوبد ‪:‬‬                           ‫رك‪ :‬ژاز ‪.‬‬    ‫؟‏‬
                                          ‫خورند از آنچه بماند زمن ملوك زمین (جهان ‪ .‬ن‪.‬ل‪).‬‬
  ‫‪.‬‬        ‫«لفت امه‬           ‫نو از پلیدی ومردار پر کنی ژاغر ‪.‬‬
  ‫در سانسکریت‪( [802 ..‬سرد» خشك وبیح رکت) «اسشق‪ »4۸۱‬هوبشمان‌ژالهرا از‬                           ‫‪۴‬‬
                                         ‫‪ #‬مأخوذميداند‪ .‬افغانى ‪ « 210۳2‬هویشمان ‪4۸٩‬‏ ‪.‬‬                 ‫‪6‬‬
                  ‫چون غوره بخامی اسرون محکم ‪.‬‬               ‫چون ژاله بسردی اسرون موصوف‬             ‫‏*‬
   ‫‪.‬‬        ‫‪۲4‬‬
             ‫‪4‬رس‬
               ‫‪۹‬ت ف‬
                  ‫منك لرمذی‪ « .‬لف‬
               ‫کرده براو حواله » فواص دردربا‪.‬‬             ‫ژاله‬   ‫اکلهه‬
                                                                     ‫لیر‬
                                                                       ‫‪ ۱‬بافوت وار لاله ‪ .‬بر‬
       ‫کایی‌مروزی‪« .‬لت فرس ‪۲44۹.۰‬‬
  ‫‪-‬رای امن معنی دوشاهد از بك قصیدة فرخی کشرلده‌اند و استاد دهخدا درآن‬
                                                                    ‫‪ ۷‬ب‬
      ‫« کوحله» ‪« ۳‬حیاب» اقرب دالته‌اند نا مع؛ی قخيڭ ماد الدردمیدم» ‪ .‬رك‪:‬‬          ‫دو» کلمةٌ ژاله را نمی‬

                                                                                   ‫لت نامه؛ ورك‪ :‬حاله‪.‬‬
```


## [2026-09-06T02:17:35.343Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN zala/žāla ===\"; grep -n -i \"zâla\\|zala\\|žāla\\|zâle\\|Hagel\" HRN.txt | head -20\necho \"=== HUB ===\"; grep -n -i \"zala\\|Hagel\" HUB.txt | head -20",
 "description": "Grep Horn and Hübschmann for žāla"
}
```


### [2026-09-06T02:17:35.433Z] TOOL RESULT

```
=== HRN zala/žāla ===
6032:684. £äle 'Hagel, Keif.
6033:Ri.hrädünl' 'Hagel'; gr. ;faAa^a; hdt, (jranclo; ksl.
6402:aw. sraska- 'Hagel' (Justi); für srasc- nimmt
9723:\ii26. i/^x *Eis' i/e/ce *Hagel\
9727:kurd. aty. LW. ye/; oss. d. ye/, t. Jx Eis, Hagel'
=== HUB ===
2518:entstanden, miisste sowohl afgh. zdla 'Hagel' wie ^alai
4619:Mia *Hagel, Reif* aus *iardak (vgl. Horn Nr. 684)?, nol
8186:c) ^= np. z: zala 'Hagel* (aus ^zardak = arisch
9315:phi. -marz, zd. marez; iola 'Hagel, Reif* aus *kirdak H. 684;
```


## [2026-09-06T02:17:38.424Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN 684 ===\"; sed -n '6028,6042p' HRN.txt\necho; echo \"=== HUB 2510-2525 ===\"; sed -n '2508,2528p' HUB.txt\necho; echo \"=== HUB 4612-4625 ===\"; sed -n '4612,4625p' HUB.txt",
 "description": "Read Horn 684 and Hübschmann context"
}
```


### [2026-09-06T02:17:38.539Z] TOOL RESULT

```
=== HRN 684 ===
*J West vergleicht hierzu das np. funbelcgto) irmäit 'llcue*.
^) Skr. Jivaha- 'lebündijj, lebhaft*; LW. arab. zifjoq , syr. 'VTi
kurd. zive^ arm. ztpak 'Quecksilber*.- 152 —
z.
684. £äle 'Hagel, Keif.
Ri.hrädünl' 'Hagel'; gr. ;faAa^a; hdt, (jranclo; ksl.
fjradü.
Nöldeke (mündliche Mitteilung). Neupersische
Grundform *zrade^ *zärde.
Diese Etymologie verdient vor der meinigen (KZ.
32, 588 No. 23) aus skr. Jada- 'kalt, starr, regungs-
los den Vorzug.
685. Serf 'tief*, PJniT (Is. 29, 15 ^), zerfi;.
aw. jfafra- 'tief; phlv. zufar^ zafr.
kurd. ziör, zaza /ör; afy. zavar; bei. juhl, n. jahl

=== HUB 2510-2525 ===
a lute, the treble in music*.
681. Zu zirak 'scharfsinnig, schlau = phi. zTrak (oder Strak)— 72 -
Ganj. 61. p. 10 gehSren als LW. kurd. zlr^ zlrek ge-
schickt, klug' ZDM6. 38, 72, afgh. zlrak acute, saga-
cious, intelligent*.
683. Arm. zipak (spat belegt) wird moderne Schreibweise fiir
iihak = arab. zlbaq, np. ^wa, jlva sein.
684. tJber die Zusammenstellung von skr. hraduni- mit ksl.
gradu vgl. jetzt Tick, Wb.* I, p. 56 und 417.
1st np. Sdla aus *mrdak (wie ich ansetzen wiirde)
entstanden, miisste sowohl afgh. zdla 'Hagel' wie ^alai
{^alai) *Hager pers. LW. sein.
687. Die Zusammenstellung scheint mir richtig trotz der
lautlichen Differenz zwischen zd. dusaka- und np. ^£a
=r phi. ^U^ak (wie ich lese) einerseits und kurd. SUzi,
g. jUjflk (ZDM6. 36, 63) andrerseits. Zd. dusaka- ist
der Schimpf- oder vulgare Name des Igels, der eigent-
lich vanhapara- heisst, vgl. Darmesteter, Zend-
Avesta II, p. 194.
691. Np. scU-a = phi. scU-ak (geschrieben snUak) ist
jahr-ig* in Compositis, deren erstes Glied ein Zahlwort

=== HUB 4612-4625 ===
ap. ^bardah" = zd. barezah^^) *H5he', phi. sup. balist, zd.
bareziSta- *h5chst*; phi. sup. a;^flto-) *am schmackhaftesten*,
zd. x^areziSta-, vgl. np. x^aUdan schmecken' (Horn Nr.500)?;
balis *Kissen, phi. balisn Gl. and Ind. 76, zd. barezis; phi.
balln *a summit, the crown of the head* Gl. and Ind. 76,
zd. baresnu- *H5he, Gipfel' (aus *6ar2?«w-, vgl. zd. bqSnu-
*Tiefe* zu bqjsah-); mOlfdan reiben', phi. -^tnarz, zd. marez-;
Mia *Hagel, Reif* aus *iardak (vgl. Horn Nr. 684)?, nol
*Rohr , skr. nada- *Schilfrohr , gr. vdgdog ? ; naltdan *klagen',
skr. nard (oben p. 103).
Vgl. Milad aus Mihrdat § 3.
Ausnahme: paz. hala verriickt', phi. halak = zd.
haredus,
b) Fiir zd. oder skr. a erscheint in einigen Fallen
```


## [2026-09-06T02:18:05.119Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\nfor w in ژاله گیلاس مالیخولیا کلر; do echo \"=== $w ===\"; grep -n \"$w\" ARY_pages.txt | head -6 | cut -c1-250; done",
 "description": "Grep Aryanpur for these words"
}
```


### [2026-09-06T02:18:06.798Z] TOOL RESULT

```
=== ژاله ===
7820:چم این واژه در زبان‌های ژرمنی: ژاله» شینم.
8562:چم اين واژه در زبان‌های ژرمنی نوین: ژاله,
=== گیلاس ===
=== مالیخولیا ===
=== کلر ===
```


## [2026-09-06T02:18:10.802Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\nsed -n '7805,7830p' ARY_pages.txt | cut -c1-250\necho \"-----\"\nsed -n '8550,8572p' ARY_pages.txt | cut -c1-250\necho \"=== pdf page tags near ===\"\nawk 'NR<=8562 && /\\[pdf page/ {p=$0} END{}' ARY_pages.txt\ngrep -n \"\\[pdf page\" ARY_pages.txt | awk -F: '$1<8562' | tail -2\ngrep -n \"\\[pdf page\" ARY_pages.txt | awk -F: '$1<7820' | tail -2",
 "description": "Read Aryanpur žāleh contexts"
}
```


### [2026-09-06T02:18:13.200Z] TOOL RESULT

```
لاتین (/710ل): 8 8008 انگلیسی کهن (5۸/073[4 010)(شاید)
فرانسه (۳8۸۸۲۷): ۰ ۲0۱۲۳۸۹۸۲۳ ,808773 7۷ ,ت05
اسپانیایی (52۸((15[7): وید اد انگلیسی (5[7ا5۸/0)(شاید) درد
ابتالبابی (744/۷): ۴0۲۲۳۸۸۸ ,۲0۲۲75 دانمارکی (2۸4۸۷/54)(شاید) انا
رومانی (/(8۷-۸4۸2/4): انا ۱ سوئدی (57782154)(شاید) 26
پرتغالی (۳0717012858): 07 ملندی (/[0076): 24۸17
[pdf page 265]
۶ | دایه
پسگشت‌ها 55 (ق۸2۲2۲ +57
۲ 0 20 16 080 ,فد هن ۱
مک این 01 8( هنم
3 (08) ,404 (۲00۲۸1) آفت‌نامه دهغدا: ۱۴۴۱۳ رین
3 (089) :01005
یادداشت: :
چم این واژه در زبان لاتین و زبان‌های ناشی از آن (زبان‌های رومانس): فواره» چشمه,
چم این واژه در زبان‌های ژرمنی: ژاله» شینم.
هند و اروپایی (1۸/00-821078۸): + ,ترآ 013* ۴0۲180130۰ ,۴015۸۵ ,038+
اوستایی (4/88374/۷): -0۸3۸۷10 ,-0۸1380 20
پهلری (4۲7الا۳۸): 6 بل۸ 029 لیترانی (72۸(4/): 00
اوستی (0558716): ,09 لتونی (لتی) (7۷1407ل): 0837
کردی (6080158): 0256 ,225 ,1020 پروسی کهن (الفاک5ن۲7 ص۵): 02۸2۸
بلوچی (الللالهه): 02 ولزی (لاقا78): 20
افغانی (پشتو) (/۸7011۸۸). 3 بر ترنی (870670۸): 20
سانسکریت (7ل54۸/58): 0112781 013۸۰ آلبانی (المامقلم: نا ۱۱
آرمنی (/۸۷۵42(1۸): 0۸۸
پرنانی (07250): پسگشت‌ها 5
-----
آرمنی (434/8(/42): 0/۸ پسگشت‌ها شک تیا
بونانی 07280): 0 ۶000
0 ,7351 ,730 3 (0) 7
ایسلندی کهن (/(52270104/4 010)(شاید) 253 موم
6 131 (8۲۱) 0/275
نررس کهن (۸0788 012)(شاید) 694 دی
00606 3 (08) :0(0(5
آلمانی کهن ((087244 777077 010)(شاید) 7 (05) 547
۹ ت70 010 :043 ۸ 07لا
.ار آلمانی (0880/40)(شاید) 7۸7 برهان قاطع + .۹
است بادداشت.
چم این واژه در زبان‌مالهنر و اروپایی کهن: دویدن» جاری شدن. :
چم اين واژه در زبان‌های ژرمنی نوین: ژاله,
اوستایی (/4(8974): ۰ 0۸3181 ,0۸301 پارسی باستان (۶37807 0ا0):
[pdf page 291]
۸11۸ ,نت0۸ انگلیسی (تکلاه/۵: 10۷۳ ,00۷۲۷
پهلری (1/لالمه): 0 هلندی (070ان 71
کردی (4ل03). 0۸ اسلاوی کهن (ع4ذل5 نان صامم:
بلرچی (ات‌ناستمه: 5 ,ت05 متططاضی
افغانی (پشتو) (۸۳0[7۸21). 13 روسی (/42ا5کتا): 03
تخاری ۸ (۸ ۸(۷ل70727۸7). اد رنه با لیتوانی (۸2(هناب 7 رم).
تخاری 8(8 #۸ 7027۸). اد ادن ره با 56 ما0
سغدی ((56007014): روهار ایرلندی کهن (للكل#ا ضان):
=== pdf page tags near ===
8505:[pdf page 289]
8535:[pdf page 290]
7783:[pdf page 264]
7811:[pdf page 265]
```


## [2026-09-06T02:18:20.634Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON ژاله headword ===\"; grep -n \"ژاله:\" MON_part1.txt | head -5 | cut -c1-300\necho; echo \"=== MON گیلاس ===\"; grep -n \"گیلاس\" MON_part2.txt | head -12 | cut -c1-300",
 "description": "Grep Mo'in for žāleh and gilās"
}
```


### [2026-09-06T02:18:20.726Z] TOOL RESULT

```
=== MON ژاله headword ===
73044:ژاله: (»)225 [سرد و خشکث] (ا.) قطرة 
73048:ژاله: (ع-)«221 (- جاله] (.) چند قطعه چوب 

=== MON گیلاس ===
133:گلوسیدی ترشح می‌کند. برگ غار گیلاس 
148:گیلاس در پزشکی آب مقطر لوریه سریز 
150:طرز تهیةٌ آب غار گیلاس بدین طریق است 
154:مقطر غار گیلاس دارای خاصیت ضد تشنج 
161:کرزی. غار گیلاسی. 
13269:و با نورد چوبی پهن کنند و با گیلاس 
34065:دارنسد مانند گل آذین گلابی و گیلاس. 
37475:گیلاس: 2و (ا.) ( گی.) درختی است از 
37484:آن می‌ریزند. گیلاس کلیه شبیه قیفی است 
37489:سنگ‌های کلیوی معمولاً در داخل گیلاس 
37494:کلیه. گیلاس وحشی: (گیا.) گونه‌ای گیلاس 
37501:گیلاس: 5۰اآه (.) ظرفی بلوری به اشکال
```


## [2026-09-06T02:18:23.631Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '73042,73052p' MON_part1.txt | cut -c1-300\necho \"=== gilas 2 ===\"\nsed -n '37473,37508p' MON_part2.txt | cut -c1-300",
 "description": "Read Mo'in entries žāleh and gilās"
}
```


### [2026-09-06T02:18:23.717Z] TOOL RESULT

```
مسهل فوی استعمال می‌شود. 

ژاله: (»)225 [سرد و خشکث] (ا.) قطرة 
-_ِ که روی بر گل و گیاه نشیند؛ شینم. 
تک رک. باران. 

ژاله: (ع-)«221 (- جاله] (.) چند قطعه چوب 
و تخته که به خیکک‌های باد کرده بندند و در 
آب اندازند و روی آن نشینند و از آب 
گذر کنند؛ جاله. 

=== gilas 2 ===
مشغول کردن مردان و رقص و فنون دیگر را 
فرا گیرد و مجالس بزم ه مردان را گرم کند 
گیلاس: 2و (ا.) ( گی.) درختی است از 
تیه گل‌سرخیان و از دستة بادامی‌ها که 
دارای گسونه‌های مسختلف است. سمبوه‌اش 
شفت و خوشمزه و سطبوع است. معمولا 


برای تهية گونه‌های مرغوب این گیاه را 
موی زر کیلاشسن که (بز) لکنه؛ 
کلیه را گویند که ترشحات رأس پاپی‌ها در 
آن می‌ریزند. گیلاس کلیه شبیه قیفی است 
که رأس آن در پایین است و دنباله‌اش حالب 
را بو جود می آورد. دهانه این قیف در مقابل 
سنوس کلیوی است. عرض یلاس کلیه ۲ 
تاش وا خفاعن. ۴ سباتمن استا 
سنگ‌های کلیوی معمولاً در داخل گیلاس 
کلیه جای‌گیر می‌شوند و گاهی یکی از اين 
سنگریزه‌های کلیوی از حالب عبور می‌کند 
و چون اد ار در دصیس جهر ۱ اجب 
تولید قولنج کلیوی می‌نماید؛ لگنچه؛ لنچ 
کلیه. گیلاس وحشی: (گیا.) گونه‌ای گیلاس 
که بطور خودرو در اکنر جنگل‌های نواحی 
بحر الرومی و مراکز اروپا و شمال ایران 
می‌روید؛ آلوککك؛ الو ککك» هلی ککك؛ 
سیاه‌هلی» هلار» الیکا کث» گیله‌بند؛ هلدانه, 
آلبالوی جنگلی. 

گیلاس: 5۰اآه (.) ظرفی بلوری به اشکال 
مختلف که جهت نوشیدن آب یا انواع 
مشروبات بکار رود؛ لیوان. خالی کردن 
گیلاس: به سر کشیدن و تهی کردن مشروبی 
که در گبلاس است. 

گکیلک: »اه (ص.) گیلی» گیلانی. 
روستایی؛ رعیت.
```


## [2026-09-06T02:18:40.547Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFM خيال ===\"; grep -n \"الخيال\\|( خيال\\|خيال )\" AFM_pages.txt | head -10 | cut -c1-300\necho \"=== AFM خوليا ===\"; grep -n \"خوليا\\|ماليخوليا\" AFM_pages.txt | head -10 | cut -c1-300",
 "description": "Grep Addi Shir for khayal"
}
```


### [2026-09-06T02:18:40.625Z] TOOL RESULT

```
=== AFM خيال ===
=== AFM خوليا ===
4575:خوليا ܘ
```


## [2026-09-06T02:18:44.104Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '4560,4600p' AFM_pages.txt | cut -c1-300\necho \"=== page tags ===\"; grep -n \"\\[pdf page\" AFM_pages.txt | head -3\nawk 'BEGIN{RS=\"\\f\"} /خوليا/ {print \"LEAF \" NR-1}' AFM_pages.txt",
 "description": "Read Addi Shir khulya context"
}
```


### [2026-09-06T02:18:45.717Z] TOOL RESULT

```
ܥܕ مه
حوار حر ©
حوان مه
ܥܕ[ »^ مه
حو بله ܙ ܘ ْ
حور ©
خوردادى ܨܘ
خوردى مره
09 ܢܘ
حوره ܨܘ
خوش ܢܘ
خوشاب وه
خوشس أسورم 5
ܡܕܬ وه
ܥܕ ܐܫܝ باه
خوليا ܘ
حون بد لاه
حون ܚܝܨܢ لاه
حون بس لاه
خون ثاب لاه
حوه هلمستوى .هه
ܥܕ ܙ )ܘ
خيار مه
ܫ ܐܝ ܥ 8ه
خيتالى ܙ ܘ
<يربوا ܘ
ܥܡ ܟܘ
خبزران .ܘ
خش ܘ
حدشفوج ̈ܘ
ܝ ܘ ܕ ܘ
خينا كى 0
+1 د جد
داب ܘ
داج "٠‏
دادا وه
دادى 8د
دارجينى +5
دار ششفان ٠د‏
دار فافل 54
داشن < ܪ¡
=== page tags ===
LEAF 168
```


## [2026-09-06T02:18:52.061Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"خوليا\" AFM.txt | head -10 | cut -c1-400\necho \"=== leaves with خوليا in AFM_pages ===\"\nawk 'BEGIN{RS=\"\\f\"} /خولي/ {print \"LEAF \" NR-1}' AFM_pages.txt\necho \"=== leaf 67 (approx p59) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==68' AFM_pages.txt | cut -c1-300 | head -50",
 "description": "Find Addi Shir khulya entry"
}
```


### [2026-09-06T02:18:53.707Z] TOOL RESULT

```
7182:خوليا ܘ 
=== leaves with خوليا in AFM_pages ===
LEAF 168
=== leaf 67 (approx p59) ===
اي قلب :43 م اي أعوج
6 ܨ به مشل دول معنى وقريب منهُ © والظاهر 37 0 من
ܝܨ !ܐܝ اللغات وهو ܕܘܠܐ بالسريانّة ܕܟ 1 ܙܪ
بالتركة ودول بالكردنة و 5161112 بالروسة ْ ; ري $10111 مأخوذ العرلي 1:6
3 السَجل 5 الدلو فأخوذ من ܥܨ 1 ( فرتكل : 277 )
الداحانة ) زجاجة كيايرة واسعة اللوف ܟܩ العنق قبل فارسسّة ونم أجدها
01 0 وَالدمازة) الهلاك ٠‏ ܘܐܬ 4 1065 وهو ܨܝ 2 دم اي
± < والنفس ومن آز ومعناه ` ويطلق ® على - الرماق
30 وقالت فيه العرب د مر ود مر الى غير ذلك
(الداموق) اللار 9 9 0 وكزر .)ܕ ومنة مأخرة
6 1 وهو كور اماد
(الدمق ) ريح وثلج تعريب دمه
(الدمقس 9 والدقّس) مسر بالابريم وقيل £ الدبياج او ¬
او ܐܐ ܨ الا مض ܡܩܡ ܢܝ د مسه:ومعتاة اطرييره الافض اوه تيون الل محلية
دمشق (021225661115 21111115م) وهو 20:07 با 0 (عاموس ”*: ¥ | ) ٠‏ واليوم
0 الدِمقس منسوب الى دمشق في كثير من اللغات وهو 0145125 3977 0
وع001735[1 بالاتكايزنة و0ع0317235 بالايطا ® وغ1001125 باكرماسة ( راجع
القاموس العبرالي تاليف جاسلئلموس )
(الدمل) ܨ وهو غراى قالله يال قاريق وحمي 6 ܨ الله .
قلت وهو معرب عن دمل الذي ܬܝܐܘ
0( 003 الأهد (005002 10 اي نفس ومن كير ܦ ماسك
( الداناج » تعريب 18 وهو العالم ٠ومن‏ الداناج مأخوذ د نج ' اي ܒܨܐ
0ل فارسي محض وهو ܣ الصيني المعروف بحب ܐܝܐ | ܨ
السلاطين
5 والدّانآق) سدس < تعريب دانك وهو بمعنى اللبّة مطاقاً ومن
ܠܨ ܪ ܓ الفاس فتعريت :23نب او 501115 او
```


## [2026-09-06T02:19:00.949Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"الخول\\|الخيال\\|خيال\" AFM_pages.txt | head -20 | cut -c1-300\necho \"=== find leaf with 'الخوان' or خوش ===\"\nawk 'BEGIN{RS=\"\\f\"} /خوشاب/ {print \"LEAF \" NR-1}' AFM_pages.txt",
 "description": "Search Addi Shir kh- section"
}
```


### [2026-09-06T02:19:02.968Z] TOOL RESULT

```
=== find leaf with 'الخوان' or خوش ===
LEAF 168
LEAF 180
LEAF 183
```


## [2026-09-06T02:19:06.165Z] TOOL CALL #37: Bash

```json
{
 "command": "python3 tools/ref_page.py AFM:59 2>&1 | head -60",
 "description": "Fetch Addi Shir page 59"
}
```


### [2026-09-06T02:19:08.324Z] TOOL RESULT

```
no scan of AFM covers printed page 59 (see 'scans' in refs_online.json)
```


## [2026-09-06T02:19:10.798Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"خول\" AFM_alt.txt | head -20 | cut -c1-300\necho \"=== AFM_alt خيال ===\"; grep -n \"خيال\" AFM_alt.txt | head -10 | cut -c1-300",
 "description": "Search AFM_alt"
}
```


### [2026-09-06T02:19:10.892Z] TOOL RESULT

```
494:الدخول على الاوك وهو م رک من بار اي جمل ورخصة ومن نامه ای رسال 
775:# (التراء ) الحناء في الظلهر او اشراف في وط الظلهر او خوج الصدر ودخول 
821:ا والأشجار ال2 يل تفع من الاليخوليا والذام وتسكی باضراس 
2265:+ ( الال ) الظن والوهم مثل خولا لفظاً ومعنى 
4014:(الشاقول) معرب الفارسى شا خول او شاقّل وهو ميزان البناء ( عيط الحبط ) 
7060:خولنجان oY‏ 
7061:خولنا ٥۹٩‏ 
7567:شاخول شافول ٠۰١‏ 
=== AFM_alt خيال ===
```


## [2026-09-06T02:19:18.609Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '2255,2275p' AFM_alt.txt | cut -c1-300\necho \"=== index lines 7055-7065 ===\"; sed -n '7050,7070p' AFM_alt.txt | cut -c1-200",
 "description": "Read AFM_alt khayal entry"
}
```


### [2026-09-06T02:19:18.679Z] TOOL RESULT

```
( ری ) دات وهو النثور الا صفر تعريتب رخارو 

e )‏ < . صغار كالقاقة فارسیتة حارو 

( الخارصيني ) ضرب من العادن تعریب خارجینی وهو مرگ من خار اي 
و ومن حن اي اص 

3 ا ( ا عض رهي کک ف لس<ھ | ا وخ و طا غلاظ من 
آل 

+ ( الال ) الظن والوهم مثل خولا لفظاً ومعنى 

# (النال) شامة في البدن والبعير الضخم فارستتها خال وهي الشامة وتطاق 
على المل الاسود ايضا 

( اام ) الفحل واللد م يدغ واتکرباس م يتل فارساتة خام ٠‏ ومن خاء 
بالأركة والكرد هة والسر يانة الدارجة 

ا تعریب خي ای الطلسعة. ٠‏ واصل خي بالفأرسہة خوی E‏ خم 
بالکرد به ای السا 

=== index lines 7055-7065 ===

خوردادی o‏ 
حخوردی ۳ه 
ا O‏ 
حوره oY‏ 

خوس 3 
خوشاب ٥ه‏ 
خوس اسپرم ٥ه‏ 
حوشه ٥ه‏ 
خولنجان oY‏ 
خولنا ٥۹٩‏ 

حون بد ۷ه 
حون دش oY‏ 
حون پاس ۷ه 
حون تاب ۷ه 
حوه ۸٩‏ 


وی 0۹
```


## [2026-09-06T02:19:34.106Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls incoming/PLA/ 2>/dev/null\necho \"=== search خيال in Arabic-loan books ===\"\nfor f in FVQ_pages.txt AFA.txt DOZ.txt LKT.txt ARB_mo3rb.txt ARB_abdulraheem.txt; do echo \"--- $f\"; grep -c \"خيال\" $f 2>/dev/null; done",
 "description": "Check PLA files and search khayal"
}
```


### [2026-09-06T02:19:35.818Z] TOOL RESULT

```
Exit code 1
PLA_asbaghi_1988_ia_djvu.txt
PLA_asbaghi_1988_ia.pdf
PLA_pages.txt
=== search خيال in Arabic-loan books ===
--- FVQ_pages.txt
0
--- AFA.txt
0
--- DOZ.txt
0
--- LKT.txt
0
--- ARB_mo3rb.txt
3
--- ARB_abdulraheem.txt
0
```


## [2026-09-06T02:19:40.125Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PLA خيال / haly ===\"; grep -n \"خيال\\|hayāl\\|ḫayāl\" incoming/PLA/PLA_pages.txt | head -10 | cut -c1-300\necho \"=== PLA مالنخوليا ===\"; grep -n \"مالنخوليا\\|ماليخوليا\\|Melancholie\" incoming/PLA/PLA_pages.txt | head | cut -c1-300\necho \"=== ARB_mo3rb خيال ===\"; grep -n \"خيال\" ARB_mo3rb.txt | head -5 | cut -c1-300",
 "description": "Search Asbaghi and mo3rb"
}
```


### [2026-09-06T02:19:40.212Z] TOOL RESULT

```
=== PLA خيال / haly ===
=== PLA مالنخوليا ===
=== ARB_mo3rb خيال ===
9569:جافا ٠‏ وق هذا الشعر خخيال تحب »و إن كان فى معنى تيف ٠‏ (5) حرف «فى» لم يذكر قح ٠‏ 
10795:تت سر سأ بور مقها * 150 ور 2 خيالك 8 معسالنع 
15540:عندى بعرن جع ©" هم 69 بصم الشين المفجمة ف ونسيما ُ اللسان عن الخيالى »6 وقال 7
```


## [2026-09-06T02:19:44.894Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -c \"خ\" incoming/PLA/PLA_pages.txt; echo \"---\"; grep -n \"ḫayāl\\|hayal\\|Phantasie\\|Einbildung\" incoming/PLA/PLA_pages.txt | head -5 | cut -c1-200\necho \"=== sample ===\"; sed -n '2000,2020p' incoming/PLA/PLA_pages.txt | cut -c1-200",
 "description": "Check Asbaghi text usability"
}
```


### [2026-09-06T02:19:44.995Z] TOOL RESULT

```
0
---
=== sample ===
8.    LD.        s.   v.
9.    al-Marßa®               s.       v.,        Muhit              s.     v.
10.        ebda.
11.        al-Mar&a°              S.       V.,        Wahrmund               s.    v.,     Mu°$am       al-Wasit       Ss.   Vv.
12.        Nyberg        Bd.       II        s.       v.
’ antirawän                                                                                          29                                                             ’awära
              ..73
olyazı                     -    ”anüfirawän:                                "ein     sassanidischer                  König"              pers.     1 — mp       mo      ir
             ano$ak-ruwän                               MP.                 „or     anofak           "unsterblich"                 am.            an-aoSa     + mp. yrp>
             ruwän             2,

              >
 ar!                  -    ”ahurmazdä:                              "Ormuzd,             Gott"        pers.     3 aus              dem    pers. _;,e hormoz           mp.
              wu pyp ohurmazd                                     ap.             ahuramazdäh               4 s._>ı               ahür    .

         “        3
(Se                        ”ahriman:                           "Widersacher                    Gottes,        Teufel"              aus    pers.      (st!      ahriman       5,
                          mp.            u          ahriman                 ap.               angra       mainyu         5


zuel - ”’ahlilaf = halilak                                                         s. nalllaß.
```


## [2026-09-06T02:19:50.584Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"ayäl\\|ayal:\\|hayal\" incoming/PLA/PLA_pages.txt | head -10 | cut -c1-250\necho \"=== m section malin ===\"; grep -n -i \"mälin\\|malin\\|mälih\\|malib\" incoming/PLA/PLA_pages.txt | head -10 | cut -c1-250",
 "description": "Search Asbaghi transliterations"
}
```


### [2026-09-06T02:19:50.663Z] TOOL RESULT

```
11313:ol           - tayälis:                           Pl.    v.gu.s,        tailasan             q. v.
11316:lb               -       tayälisi:                  "derjenige,              der    den       tailasan       macht".
=== m section malin ===
```


## [2026-09-06T02:19:56.397Z] TOOL CALL #44: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T02:19:56.404Z] TOOL RESULT

```


```


## [2026-09-06T02:19:59.704Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%DB%8C%D8%A7%D9%84",
 "prompt": "Give the Arabic and Persian etymology sections for خیال / خيال: what root and origin are given for Arabic khayāl, and how did Persian خیال get the word?"
}
```


## [2026-09-06T02:20:00.591Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/melancholy",
 "prompt": "Full etymology chain for melancholy: Greek, Latin, Old French, Middle English, dates."
}
```


### [2026-09-06T02:20:06.747Z] TOOL RESULT

```
# Etymology of خیال (Khayāl)

## Arabic Root
The webpage does not provide explicit information about the Arabic root or origin for خَيَال (ḵayāl). It only mentions that the word exists in Arabic with the meaning "imagination," but offers no details about its etymological derivation or the specific root from which it developed.

## Persian Etymology
According to the document, Persian خَیال acquired the word through borrowing: "Borrowed from Arabic خَيال (ḵayāl)." The entry explicitly states that "Persian خیال" came directly from the Arabic term, establishing a straightforward loanword relationship rather than an independent development.
```


### [2026-09-06T02:20:07.643Z] TOOL RESULT

```
# Etymology of Melancholy

The word **melancholy** traces back through multiple linguistic layers:

**Greek Origin**: The term derives from Greek *melankholia*, literally meaning "(excess of) "black bile"—combining *melas* ("black") and *khole* ("bile").

**Latin Transmission**: It passed through Late Latin *melancholia* before entering Old French as *melancolie*.

**Medieval English**: The word arrived in Middle English around 1300 as *melancolie* or *malencolie*, initially describing "mental disorder characterized by sullenness, gloom, irritability" based on humoral theory.

**Historical Context**: Old medicine attributed depression to excessive "black bile," one of the body's four humors. A 1623 dictionary defined it as "The grossest of the foure corporall humours, which if it abound too much, causeth heavinesse and sadnes of minde."

**Evolution**: As medical humoral theory faded in the 18th century, the word retained its psychological meaning, referring to habitual or prolonged gloominess rather than a physiological condition.

**Related Languages**: The etymology influenced Spanish *melancolia*, Italian *melancolia*, German *Melancholie*, and Danish *melankoli*.
```


## [2026-09-06T02:20:12.196Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D9%8A%D8%A7%D9%84",
 "prompt": "Arabic entry خيال (khayāl): what is the etymology, the triliteral root, related verb خال/تخيل, and meanings? Quote the etymology text."
}
```


## [2026-09-06T02:20:13.229Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%98%D8%A7%D9%84%D9%87",
 "prompt": "Persian ژاله: etymology, Middle Persian/Proto-Iranian forms, cognates, meaning. Quote the etymology text."
}
```


### [2026-09-06T02:20:19.037Z] TOOL RESULT

```
# Etymology of Persian ژاله (žâle)

## Origin and Cognates

The word ژاله derives from Proto-Indo-European roots meaning "ice." According to the Wiktionary entry, it comes from "*gʰelh₂d-" and shares linguistic ancestry with Ancient Greek χάλαζα (khálaza), which refers to hail.

## Etymology Quote

"From Proto-Indo-European *gʰelh₂d- ("ice"). Cognate with Ancient Greek χάλαζα (khálaza)."

## Meanings

The Persian term carries multiple related meanings depending on regional usage:
- Hoarfrost (the crystalline ice coating)
- Dew
- Hail (particularly in Dari Persian)

The word has spawned descendants across multiple languages including Azerbaijani, Turkish, Gujarati, Hindi, and Urdu, demonstrating its historical linguistic significance across Asia.
```


### [2026-09-06T02:20:19.643Z] TOOL RESULT

```
# Arabic Entry خيال (khayāl)

## Etymology
The document does not explicitly state the etymology of this term beyond identifying its Semitic root.

## Triliteral Root
The root is **خ ي ل** (ḵ y l), with 9 related terms belonging to this root family.

## Meanings
According to the Wiktionary entry, خيال has three primary definitions:

1. **Imagination**
2. **Shadow**
3. **Fiction** (in literature contexts)

## Related Verb Forms
The document lists one derived term:
- **خيالي** (khiyālī) — meaning "imaginary" (adjective form)

However, the specific verbs خال or تخيل are not mentioned in this entry, so I cannot provide information about their relationship based solely on the provided content.

## Note on Etymology Text
The page does not include a dedicated etymology section for the Arabic entry itself, only documenting the root classification and its descendants across other languages.
```


## [2026-09-06T02:20:25.330Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%AF%DB%8C%D9%84%D8%A7%D8%B3",
 "prompt": "Persian گیلاس: list all etymologies given (both the 'cherry' word and the 'drinking glass' word). Quote the etymology texts, including any borrowing from English glass or Russian/French."
}
```


## [2026-09-06T02:20:27.192Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%A7%D9%84%DB%8C%D8%AE%D9%88%D9%84%DB%8C%D8%A7",
 "prompt": "Persian مالیخولیا: etymology — from Arabic? from Greek melankholia? Quote the etymology text."
}
```


### [2026-09-06T02:20:29.982Z] TOOL RESULT

```
# Persian گیلاس - Both Etymologies

**Etymology 1 (Cherry):**
The text states: "From Greek _κεράσι_ (kerási, 'cherry')." This word originated from the ancient Greek term for the fruit.

**Etymology 2 (Drinking Glass):**
According to the source: "Borrowed from Urdu _گلاس_, from English _glass_." This meaning came through Urdu as an intermediary language, ultimately deriving from the English word for the transparent drinking vessel.

The entry documents two distinct etymological paths for this Persian term, reflecting both a natural fruit and a borrowed term for glassware.
```


### [2026-09-06T02:20:32.902Z] TOOL RESULT

```
# Etymology of Persian مالیخولیا

According to the Wiktionary entry, the Persian term's origin traces back to Ancient Greek through a somewhat convoluted path.

**Direct Etymology:**
The word is described as a "Misspelling of earlier _مالنخولیا_ (mâlenxuliyâ), from Ancient Greek _μελαγχολία_."

**Key Point:**
The etymology does not attribute the word directly to Arabic. Rather, it indicates the Persian form came from Ancient Greek *melankholía*, with the current spelling representing an error from an earlier Persian variant. The word entered Persian and subsequently other languages like Urdu through this Greek-to-Persian transmission, not through Arabic as an intermediary source in the direct lineage, though Arabic may have played a role in historical transmission routes of the term across the broader Islamic world.
```


## [2026-09-06T02:20:43.801Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/chlorophyll",
 "prompt": "Etymology of chlorophyll and chlorine: who coined them, in which language and year, from which Greek words?"
}
```


## [2026-09-06T02:20:44.411Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/chalaza",
 "prompt": "Etymology of chalaza and chalazion: Greek khalaza, PIE root, meanings."
}
```


### [2026-09-06T02:20:48.506Z] TOOL RESULT

```
# Etymology of Chlorophyll and Chlorine

**Chlorophyll:**
- **Coiners:** French chemists Pierre-Joseph Pelletier and Joseph Bienaimé Caventou
- **Year:** 1818 (French version: *chlorophyle*)
- **Language:** French
- **Greek roots:** "chloro-" from Greek *khlōros* ("pale green, greenish-yellow") + *phyllon* ("a leaf")

**Chlorine:**
The webpage does not provide specific information about who coined chlorine, in which year, or the original language. It only appears as a linked entry in lists of related words.

The document notes that chlorophyll entered English in 1819 from the French coinage of the previous year, combining Greek elements meaning "green" and "leaf."
```


### [2026-09-06T02:20:49.434Z] TOOL RESULT

```
I appreciate your request, but I need to be transparent: the web page content provided doesn't actually contain etymological information about "chalaza" or "chalazion." 

The page appears to be a header/footer template from Etymonline.com showing navigation, branding, and support options, but it lacks the actual dictionary entries or etymological data you're asking about.

To provide accurate information about these words' origins (both relating to Greek "khalaza"), I would need the actual entry content from the Etymonline database, which isn't included in the material you've shared.

If you can provide the specific entry pages for these terms, I'd be happy to summarize their etymological information following your guidelines.
```


## [2026-09-06T02:20:56.430Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC gheled/gheld ===\"; grep -n \"ghelad\\|gheled\\|gheld-\\|khalaza\\|xalaza\" IEC.txt | head -10 | cut -c1-300\necho \"=== IEC ghelos/ghel- shine ===\"; grep -n \"ghelos\\|ghelwos\\|ghlōros\" IEC.txt | head -10 | cut -c1-300\necho \"=== SYN hail ===\"; grep -n -i \"Hail\" SYN.txt | head -10 | cut -c1-250",
 "description": "Grep Mann and Buck"
}
```


### [2026-09-06T02:20:56.568Z] TOOL RESULT

```
=== IEC gheled/gheld ===
=== IEC ghelos/ghel- shine ===
4465:gughelos, à “lump, ball’. Cf. gugh-, gughaà MHG kugele ‘ball’; G Kugel ‘bullet; OE cycgel ‘cudgel’; Du. kogel ‘bullet’; Li. güZulas (bundle, sheaf ambig., cf. güigos)
5968:$hel- (ghelos, -es-, &helis) ‘green; greenery, vegetable; gold, golden’. WP I, 625. See fol- lowing entries, and cf. ghel- w. extns. Skt. harih ‘yellow, tawny’; Per. zar ‘gold’; -zar, cpds. *plant-bed'; Av. zairis, adj. ‘yellow’; Dac. cf. -zelion (in asio- ?, equated w. asifoliu
11993:oghelos (oghoeros; oghlos, oghros) (intense, difficult, tough). Cf. aghoelos, ogh- (1). (Skt. Gk. & Gmc. ambig. For Gk. cf. uoghol-) Skt. aghalah ‘evil’; Arm. cf. ogorem, -im, v. ‘fight’; Gk. (initial ambig.) ókhlos, m. ‘tumult, bother; okhléo ‘stir up, trouble’; Ir. ogal, adj.
16630:soghlos, soghelos (sogh-) “hold, holder Hitt. saklais (for *saglis), s. law, custom’; W hoel, pl. ion, f. ‘nail’
=== SYN hail ===
1764:4. Goth. peihwd, prob. fr. *tenkwa- : ChSl. tqéa ‘shower’, Russ. tuca ‘dark cloud’, SCr. tuéa ‘hail’, Lith. tankus ‘thick’. Development through ‘thick cloud’, ‘thundercloud’ to ‘thunder’. Walde-P. 1.726 (with doubt)
2437:NIr. buachaill ‘boy, servant, cow- herd’, fr. MIr. buachaill ‘cowherd’, like W. bugail ‘cowherd’, Corn. bugel ‘herds- man, shepherd’, Br. bugel ‘child’: Grk. Bouxédos ‘cowherd’. Walde-P. 1.696. Pedersen 1.54. Henry 47.
2509:Br. bugel ‘child’ also ‘cowherd’ : W. bugail ‘cowherd’, Ir. buacchail ‘cowherd, boy’ (2.25).
3985:Nir. buachaillighim (a); MHG weiden, weidenen (a,
3997:Nir. buchaillighim, W. bugeilio, fr. NIv. buachaill, W. bugail ‘herdsman’ (3.18), like Grk. rouatvw fr. rouphy.
4036:a Fecha agatre MHG hirt(e), herter Russ. pastuch ae buachaill, aodhaire NHG shirt yee gopa-, pacupa-, etc. W. bugail v. vastar- Br. bugel
4047:3. Ir. buachaill, W. bugail, Br. bugel, all orig. ‘cowherd’, but not so restricted (cf. NIx. bwachaill bo ‘cowherd’), epds. of words for ‘ox, cow’, and prob. the same root as in Grk. Bovkédos, etc. (above, 1). Pedersen 1.127.
6070:Ir. scérn in cpds. (scdrn-chailbhe ‘epiglottis’, etc.), NIr. scérnach, etym.?
7694:300 4.83 WELL; HEALTH Grk. is} bylea Goth. hails ; Lith sveikas; sveikaig NG oe yepos; byela ON heill; hetlsa Lett. —_vesels, Sveiks; veseliba Lat. sdnus, etc.; sdnilas, Dan. ask, sund; helbred, ChSl. stidravit, célii; stidra. ete. sundhed vi
7708:thealth’), am yagh : a fs hee nt’, Grk. axos ‘cure’, fet ean Pe alde-P. 1.195. Peder- axe sen sa pails, ON heill (> ME hail),
```


## [2026-09-06T02:21:04.751Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"‘hail\" IEC.txt | head -20 | cut -c1-350\necho \"=== WLD Bd1 ghel ===\"; grep -n \"Hagel\" incoming/WLD/WLD_Bd1_pages.txt | head -10 | cut -c1-250",
 "description": "Search Mann and Walde-Pokorny"
}
```


### [2026-09-06T02:21:04.831Z] TOOL RESULT

```
4954:ghródos, io “ice, hail, crust:. Cf. ghrud- Vedic Skt. cf. hrádunih “hail'; OCS gradü, graZda, id.; Srb. grád; OCz. hrad, id.; R cf. gra- dobitie ‘hailstorm’; Li. grüodas *hardfrozen ice; scaly-foot in horses’; gruodis ‘December’
5743:Per. cf. Zale “hail; dew" (?); Alb. zallé ‘pebble, shingle’; OHG kisil, MHG kisel, OE ceosel, ceosol, id.; G Kiesel "flint, silica, hail; kisseln, v. ‘hail’; Icel. kísill ‘silica’; OCS žali “shore? Srb. žal, id.
7086:kestis, os, io ‘spike, spear, pole’. Cf. Kestros, ksest- Arm. šešt, Let (sharp; stiletto’: $ by double induction from i-inflection); Gk. (ambig.) kestós embroidered" beside késtra *pole-axe'; Mir oss ‘edge’; Ir. ceis ‘spear’; W ces, pl. i *dividing-point'; Li. kestis, ës keste, keSCia ‘pole’. (Gaulish cissium *two-wheele
7941:krisolos, krislos, à ‘residue, fragment(s), speck, smut'. Cf. krisd- Arm. (?) koriy, i, av ‘grain, stone’; MHG risel ‘hail; residue; drizzle, snowflake’; G Riesel, f. *rubble-heap; freckle; measles’; Li. krislas, m. ‘crumb, speck, smut, mule on skin’;
8030:kruksos, à (kruKs-) ‘crushed grains, powder, granules’. (Sl. evidence ambig. Cf. krüsos). Cf. WP I, 479 *LLat. in It. crusca ‘bran, refuse, dregs’; OCS krüxa “fragment? beside krüso, iti ‘shatter’; R kroxà ‘crumb, grain’; Li. krušà ‘hail’ beside krušùs ‘friable’; kruns$u & krüstu, inf. krusti “crush, pound
=== WLD Bd1 ghel ===
31987:kaghlo- ,,kleiner runder Stein. Kiesel"; germ.                                         ,,Hagel".
31989:hagol, hcegel m. anord. liugl n. ..Hagel”. Z. B. Zupitza Gutt. 207 Boisacq s. v.
32116:   mir. casar „Hagel; Blitz", cymr. cesair „SchloBen“, corn, keser, bret.
32117:kazarch „Hagel" (Fick II 4 74; nicht entscheidend dagegen Loth Rc. IS,
32222:auch lat. calamitas „Schaden“ (urspriinglieh landwirtschaftlich „Hagelschlag,
33235:„rauh, hart" (auch karaka- m. „Hagel“? Uhlenbeck Ai. Wb. 44); vermut-
34004:ausl. Tenuis air. cith „Regenschauer“ ? ? apr. Iceytaro „Hagel“?? (eher zu
45260:„Hagel“, bei Nesselmann auch ,,Eisscholle'‘, lett. krttsa ,,llagel ", Schmidt
45398:           krimti ) „stampfen, zerstoBen", krusd „Hagel“ (bei Xesselmann
45399:auch „Eisscholle“), lett. krusa „Hagel“, lit. krustine „Graupe“, lit. kriau-
```


## [2026-09-06T02:21:13.297Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '5740,5746p' IEC.txt | cut -c1-400\necho \"=== WLD zledica/gheled ===\"; grep -n \"zledica\\|žl.dica\\|gheled\\|ghel.d-\" incoming/WLD/WLD_Bd1_pages.txt | head -10 | cut -c1-250\necho \"=== WLD zala ===\"; grep -n \"npers. zala\\|zala „Hagel\\|zala ,,Hagel\" incoming/WLD/WLD_Bd1_pages.txt | head | cut -c1-250",
 "description": "Mann lemma + Walde-Pokorny gheled"
}
```


### [2026-09-06T02:21:13.389Z] TOOL RESULT

```
ilos, a, is “growth, stem, sprout’
Arm. ciy 'stem, blade of plant’; cil “bud, shoot panicle’; Thracian zila- “vine? beside Dacian -zila, -dila (in plant-names: a-zila, beside a- dila, proce-dila, tani-dila, doc-tila (sic), and dio-dela (sic) of uncertain composition, cf. porKos, tn-, tāk-, diu-); Ir. giol (2) “early grass”; MHG kil (2) ‘leek’; cf. Rum. (? substrate) zir- nå, f. ‘woody nightshade’. (Per. zire �
gislos, is (gisol-) ‘pebble, shingle’
Per. cf. Zale “hail; dew" (?); Alb. zallé ‘pebble, shingle’; OHG kisil, MHG kisel, OE ceosel, ceosol, id.; G Kiesel "flint, silica, hail; kisseln, v. ‘hail’; Icel. kísill ‘silica’; OCS žali “shore? Srb. žal, id.
(&it-, variant of ĝid-, gidh-, q.v. WP I, 527. Cf. W gid, giten ‘kid’. Isophonic are MHG kit, gs kides; kide ‘sprout’; OE cip *mote")
£ieua, see Seu
&leibh- (variant of gleibh-, glibh-, q.v. "ad.
=== WLD zledica/gheled ===
59262:„Glatteis“ iiberzeugend zu *goh „nackt, bloB“; fiber aksl. zledica „ge-
59845:                                         ghel-   — ghelad-                                        629
59904:ghelad- „Eis“.
59905:  Horn, /alalia „Hagel“; aksl. zledica „gefrorener Regen", sloven, zled
=== WLD zala ===
```


## [2026-09-06T02:21:15.496Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '59898,59925p' incoming/WLD/WLD_Bd1_pages.txt | cut -c1-250",
 "description": "Read Walde-Pokorny ghelad- entry"
}
```


### [2026-09-06T02:21:15.551Z] TOOL RESULT

```
     Nicht einleuchtend will Persson Beitr. 31               A 2, 792 A 2 %a/.xog, xal/rj als
echt idg. Wort zu ghel- „griin, gelb“               (lit.                    vom Rind-
                                                            zalas freilich „rot ‘,
vieh) stellen,        wobei   fur   den bsl. Yelar auf lit. geltas, gelsvas ,,gelb“ usw.
zu verweisen ware.

ghelad- „Eis“.
  Horn, /alalia „Hagel“; aksl. zledica „gefrorener Regen", sloven, zled
„Glatteis", klr. ozeleda„Regen mit Schnee, Eis auf Baumen", poln. zlodz
„Schneeregen, Glatteis". Solmsen AfslPh. 24, 579.
                                                                                     41 *
630                                                 gelebh-   —   geli-, gli-



  Ai. hlddate „kuhlt sich ab, erfrischt sich", pra-hlada- m. „Erfrischung,
Erquickung“, wozu hrada- m. „Teich, See“ (Uhlenbeck Ai. Wb. 363) sind
im Gutt. (gh-), Yokalismus (ai. 3 Dehnstufe zu Hochstufe a) und in der
Bed. unvereinbar; unsichere Erwagungen dariiber bei Berneker 393; mit
gr. yayXdQm „klatsche, platschere', y.tyXaba (Pind.) „rausche, brause'
                                                                                                              -
                                                                                                                  (Fick I*
56, 438)       sind sie   kaum zusammenzubringen                                (s.   Boisacq 423 m. Lit. auch
xiber     anklingende Worte).

gelebh-        ,,schaben",       u.           zw.    teils    ..sehabend aushohlen",                teils     „schabend
          glatten,   hobeln" (..geglattete Stange, Balken").
     Gr. yXayor „hohle aus, scharre aus, haue aus, schnitze aus", yXaq>v
```


## [2026-09-06T02:21:26.901Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON کلر headword ===\"; grep -n \"کلر:\" MON_part2.txt | head -5 | cut -c1-300\necho \"=== MON کلروفیل ===\"; grep -n \"کلروفیل\\|کلروفرم\" MON_part2.txt | head -5 | cut -c1-300\necho \"=== MON خیال headword ===\"; grep -n \"خیال:\" MON_part1.txt | head -5 | cut -c1-300",
 "description": "Mo'in entries for kolor and khiyāl"
}
```


### [2026-09-06T02:21:27.003Z] TOOL RESULT

```
=== MON کلر headword ===
=== MON کلروفیل ===
10139:کلروفیل هستند و نمی‌توانند از انیدریک 
16744:کلروفرم یا در بتزین حل می‌کنند و چون 
25084:کلروفرم: (-0۳۳9۸)۲6]-۱۵۱۵۲۵ (۱.) (یز. شننم. ) 
34513:ذرات کلروفیل ۳ بت را تبدیل به مواد 
37193:کلروفیل در برابر خورشید انجام می‌شود. 
=== MON خیال headword ===
20120:خیال: 
26830:بسی خیال: اقرندآن آن. ع.] (ص‌مر.) 
58473:خیال: (تند. 2۸۵۷۵۱۷۵1 [ع.] (.( کمان؛
```


## [2026-09-06T02:21:30.594Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '58470,58490p' MON_part1.txt | cut -c1-300\necho \"=== 20118 ===\"; sed -n '20116,20130p' MON_part1.txt | cut -c1-300\necho \"=== کلروفرم entry ===\"; sed -n '25082,25090p' MON_part2.txt | cut -c1-300\necho \"=== کلر standalone ===\"; grep -n \"^کلر\\| کلر \" MON_part2.txt | head -8 | cut -c1-200",
 "description": "Read Mo'in khiyāl and kolorofurm"
}
```


### [2026-09-06T02:21:30.730Z] TOOL RESULT

```
خیاطت: ۷2 (ع. خياطة | (اسص.) 
دوزندگی. خیاطی. 

خیال: (تند. 2۸۵۷۵۱۷۵1 [ع.] (.( کمان؛ 


وهم. صورتی که در خواب دیده شود. هر 
صورتی که از ماده مجرد باشد مانند شیْ در 
آینه. (فا. قد.) قوه‌ای است که در موخر 
تجویف اول دماغ گذارده شده و صوری را 
که حس مشت رک ادراکك کرده است نگاه 
می‌دارد و مانند خزانه‌ای است سرای حس 
مشترکك و بدین قوه آن کسی که در زمانی 
دیده شده سیس غاب گردیده؛ حاضر و 
شناخته می‌شود. ضح.- (رواد.) ه رگاه اشیاء با 
حواس مواجه باشند» صورتی که از آنها در 
ده مس شوه اتاتوبا دز ک مستی 
خوانده می‌شود؛ هرگاه با حواس مواجه 
نباشند» صورت ذهنی آنها «خیال, يا «تصور 
جز ثی» نام دار د؛ ج. اخبله» خبالات. خبال 
مجرد: (تص.) آن بود که خواطر نفسانی بر 
=== 20118 ===
سر نهنك. 

پاریر ؛ ۰27027 (افا. امر.) کسی که بار را بر 
پشت و دوش خود حمل کند: باربرنده» 
خیال: 

بارپیج: 05-16 (امر.) آنچه که بار را بدان 
پیچند مانند نوار» رسمان و غیره. 
بارجامه: (6-)02-12702 (امر.) کیسه‌ای 
بزرگ و ستبر که بر پشت چارپایان بارکش 
افکنند و در آن خاکك» شن؛ آهک و جز 
آن ریزند؛ جوال. 

بارح: 02۳2۳ ([ع.] )۱( باد گرم تاستان. باد 
تند کردنا کك» باد شدیدی که غبار برانگیز د) 
=== کلروفرم entry ===
مصرف می‌شود. 

کلروفرم: (-0۳۳9۸)۲6]-۱۵۱۵۲۵ (۱.) (یز. شننم. ) 
مایعی است بی‌رنگ و بیهوش کننده به 
فرمول ,م1101 که از اثر استخلاف سه انم 
یدروژن متان به وسیلة سه اتم کلر بدست 
می آید. این ماده در پزشکی به عنوان داروی 
بیهوشی مصرف می‌شود. 

=== کلر standalone ===
3706:اکسیژن و ازت و کلر و برخی چون گوکرد» 
10139:کلروفیل هستند و نمی‌توانند از انیدریک 
13414:کلرال نیز مفید است و نیز تزریق محلول 
16744:کلروفرم یا در بتزین حل می‌کنند و چون 
19741:مانند زاج و اسید تری کلر استبکك. 
20932:کلرات‌دو پتاسیم و کلر بدرات‌دوک وکائین 3 
21767:کلرج: لته [- - کرج] () گوی گریبان. 
25021:می‌کند. کلر را می‌توان در حرارت ۱۵
```


## [2026-09-06T02:21:35.375Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '25005,25030p' MON_part2.txt | cut -c1-300",
 "description": "Read Mo'in kolor entry"
}
```


### [2026-09-06T02:21:35.431Z] TOOL RESULT

```
کلچ: 5 (.) پوشش بشمینه که ساقاً از 
کشمیر و پیت هی | وو نك 

کلخج: آجداها [- کلخچ؛ قس. کلچ] ۲.1 
چ رک وسح. 

کك: ۲ (.) (شیم.) شبه فلز ی است زرد 
مایل به سبزء در شرایط متعارفی گازی شکل 
ابوی خفه کننده و کمی سبکث‌تر از هواو به 
همین جهت بصورت گٌاز خفه کنند در 
جنگ اول جهانی بکار رفته. تکاثف نسبی 
این گاز نسبت به هوا سل (معادل ۲/۴۹) 
از هوا تقریباً دو و نیم مرتبه 
سنگین تر است. یک لیتر آب در ۸ درجه 
حرارت ۳/۰۴ لیتر آن را در خود حل 
می‌کند. کلر را می‌توان در حرارت ۱۵ 
درجه حرارت با فشار ٩‏ جو مایم کرد و در 
بطری چدنی سیفون‌دار به بازارا عرضه نمود. 
کلر اول دفعه در سال ۱۷۴۷ م. وسیلةٌ شیل 
از اثر جوهرنمکک بر بی| کسید منگنز بدست 
آد مسطابق فرمول زیر: 
۲۵0 +0۱۲ ۲ م۴011 +100۲ ون 
فرمول فوق در برابر گرما باید صورت گیر ده 
لذا اگر وسیلةً گرم کردن نباشد پرمنگنات 
پتاسیم متبلور را در ظرف ریخته و قطره
```


## [2026-09-06T02:21:48.025Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%9C%E0%A4%A1",
 "prompt": "Sanskrit जड (jaḍa): etymology and meanings. Is it linked to any PIE root, or called of uncertain/non-Indo-Aryan origin? Quote the etymology."
}
```


## [2026-09-06T02:21:49.848Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B0elh%E2%82%82d-",
 "prompt": "What descendants and meaning are given for this PIE root? Does it include Persian žāla and Greek khalaza? Any Sanskrit forms?"
}
```


### [2026-09-06T02:21:51.720Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T02:21:54.397Z] TOOL RESULT

```
# Sanskrit जड (jaḍa): Etymology

The etymology of this word is **uncertain**, with competing theories:

**Substrate Origin Theory:**
According to Turner, the word is "probably of substrate origin" — meaning it may derive from non-Indo-European languages absorbed into Sanskrit.

**Proto-Indo-European Theory:**
Proponents of Fortunatov's law propose a PIE connection: "inherited from Proto-Indo-European *gel-d-os via Proto-Indo-Aryan *ȷ́alḍas." Under this theory, it relates to English "cold" and Latin "gelidus."

The page explicitly states the etymology is "Uncertain," acknowledging scholarly disagreement about whether this word has Indo-European roots or comes from substrate languages.
```


## [2026-09-06T02:22:06.942Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/خیال' --note 'page 186, root Ghel entry 0 node 9: Persian خیال borrowed from Arabic خيال' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/خيال' --note 'page 186, root Ghel node 8: Arabic خيال, root خ-ي-ل, no Persian/Greek origin given' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/melancholy' --note 'page 186, root Ghel nodes 5-6-10-11: Greek melankholia > LL melancholia > OF melancolie > ME melancolie c.1300' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/ژاله' --note 'page 186, root Gheled node 2: Persian ژاله from PIE *gʰelh2d- ice, cognate Gk khalaza' 2>&1 | tail -3",
 "description": "Archive web sources batch 1"
}
```


### [2026-09-06T02:22:09.894Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/b8bf343bf74fd8a3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/50720724cd744067.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c7bf246f7dfa7ced.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/16c6ce3960ac94b3.txt
```


## [2026-09-06T02:22:15.494Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/گیلاس' --note 'page 186, root Ghel node 14: Persian گیلاس drinking glass borrowed from Urdu گلاس from English glass' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/مالیخولیا' --note 'page 186, root Ghel node 7: Persian مالیخولیا misspelling of مالنخولیا from Gk melankholia' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/chlorophyll' --note 'page 186, root Ghel nodes 1-4: chlorophyll coined French 1818 Pelletier/Caventou from Gk khloros + phyllon' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/जड' --note 'page 186, root Gheled node 1: Sanskrit jaḍa uncertain/substrate (Turner) or PIE *gel-d- cold, not *gheled-' 2>&1 | tail -2",
 "description": "Archive web sources batch 2"
}
```


### [2026-09-06T02:22:18.518Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/94cf6c1d366f028b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/836bfa332b9f4ef0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8650ebc03002c6ad.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f1ad3f725c886c02.txt
```


## [2026-09-06T02:22:24.672Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FSF ژاله ===\"; grep -n \"ژاله\" FSF_pages.txt | head -5 | cut -c1-300\nawk 'BEGIN{RS=\"\\f\"} /ژاله/ {print \"LEAF \" NR-1}' FSF_pages.txt",
 "description": "Grep Noushin for žāleh"
}
```


### [2026-09-06T02:22:26.177Z] TOOL RESULT

```
=== FSF ژاله ===
14366:‫به‌چشم اندرون آب چون ژالهگشت‬                                               ‫یافه» (صحاح)‪:‬‬
14382:          ‫گرازه سر نخمه گیوگان‬                                                          ‫ژاله‬
14384:‫(‪)۴-۹۲-۲۲۲‬‬                                                 ‫توگفتی هوا ژاله بارد همی‬
LEAF 288
```


## [2026-09-06T02:22:28.747Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==289' FSF_pages.txt | cut -c1-200 | sed -n '1,45p'",
 "description": "Read Noushin page with žāleh"
}
```


### [2026-09-06T02:22:30.840Z] TOOL RESULT

```
                                ‫‪-۲‬شبنم‪:‬‬

     ‫شهر پر زاری و ناله گشت‬        ‫همه‬       ‫«هذیان‬    ‫(لغت فرس)‬       ‫(سخن بیهوده)‬


‫به‌چشم اندرون آب چون ژالهگشت‬                                               ‫یافه» (صحاح)‪:‬‬
‫‏)‪(YTVA-۱0۵-F‬‬                                          ‫چو برسم بدید اندر امد به واژ‬
                              ‫ژرف‌بین‬        ‫نه‌گاه سخن بود و گفتار ژاژ‬

‫از ژرف [بهمعنی گود‪ .‬عمیق] ب‪+‬ین [اسم‬          ‫(‪۹‬شیرویه ‪)۹۴۴‬‬
             ‫فاعل مرخم از دیدن =بیننده]‪:‬‬     ‫از ناصرخسرو‪ :‬ژاژ و ژاژیدن به‌معنی سخن بیهوده‬
                  ‫زرف بیننده‪ :‬دوراندیش‪:‬‬                               ‫گفتن (‪)۴۲ ۳۱۲-۲۲‬‬

           ‫یکی چاره آورد از دل به جای‬               ‫نادان تو را‬     ‫خحوار کنا صحبت‬

‫که بد ژرف‌بین و فزاینده رای‬                   ‫همچو فرومایه تن‌خوار خویش‬
‫‪۱۸۰-۷۰۲-۷۸۰۱‬‬
                                      ‫ژگان‬    ‫رنجه به ژاژیدن بسیار خویش‬
‫قید از ژگیدن (ژگیدن به معنی لندلند‬                ‫کد زار ونت نا مسر‬                  ‫ی‬
    ‫کردن از ناخرسندی زیر لب نالیدن)‪:‬‬          ‫معدهة ناهار خویش‬       ‫کند‬     ‫سیر‬

          ‫گرازه سر نخمه گیوگان‬                                                          ‫ژاله‬
                                                                               ‫‪-۱‬تگرگ‪:‬‬
‫(‪)۴-۹۲-۲۲۲‬‬                                                 ‫توگفتی هوا ژاله بارد همی‬


                                             ‫(‪۲-۰۳۱-۲‬ع‪)6‬‬
```


## [2026-09-06T02:22:55.861Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HJB glass/gilas ===\"; grep -n -i \"GILASS\\|gilas\\b\\|glass, s\\.\" HJB.txt | head -8 | cut -c1-250\necho \"=== SKT gold/yellow/glass ===\"; grep -n -i \"^Gold\\|Gold, \\|Yellow\\|Glass,\" SKT.txt | head -8 | cut -c1-250\necho \"=== LAT melancholia ===\"; grep -n -i \"melancholia\\|melancholicus\" LAT.txt LEW_1910.txt | head -5 | cut -c1-250",
 "description": "Grep Hobson-Jobson, Skeat, Latin dicts"
}
```


### [2026-09-06T02:22:55.950Z] TOOL RESULT

```
=== HJB glass/gilas ===
16331:pAlagilAss,
=== SKT gold/yellow/glass ===
515:yellow.  —  O,  F.  aufwtnr,  aIl>otfu,  blond (Godcfroy);  re^larly  formed  from  Low L.a/lmrnus,  whitish,  light  coloured.  Florio explains  Itnl.  aiburno  by  '  that  whitish colour  of  women's  hair  called  an  aibttrn or  aburn  col
1938:Blond.    (F.)    A  late  word- m.   blenJ4,  fem.   Might  yellow fcrred  by  Diez  to  Iccl.  A cf.  A.S.  blimtUn-foax^  having gled  coloDr.  gray-haired.     See  B!
6301:Fallow  (3),  used  with  reference  lo colour.  (E.1  A.h.  feaiu^/eala^  pale  red, yellowish.  +  Dtt-  two/,  lorL  ffir,  t»a)c G.  fahl,  pale,  also  /alb.  L.  failidmj.  Gk. iroAtur,  g^,  Skt  f*alita,  gray.     Sea  Fal«.
6726:(Untr  X«-ll)  The  sense  of t  ucmi  to  havf  been  adapted Mcr  tense  of  '  hue '  or  '  appear L,.JIfnior,  golden  coin,  yellow- X^JUtMS,  yellow,  gold-coloured. r:  Me  VIaIw.
7415:—  O.  ¥.  gariofu//.  Cf.  Span,  ^tnrmt Ital.ghir/oMifa  1  whence  mod.  F.gMtrian a  garland.  Prob,  formed,  witb  suffix  -4 from  M.  H.G.  wiertUn*,  a  suppeaed., quentative  of  ttiVrvr.  to  adorn,  from  0,G wiara^  M.  H.  G-  v
7779:Gold.  (E.)  A.  S.  gold.  +  Dn.  gvud  (for fp/*/),  Icel.  guff,  Swed.  Dan.  guid,  G.  gold, Gotli  gulfh,  UiiBS.  c/a/tf,  Gk.  xpiwoj,  Z-tod tanxftu.  .Skt  hitana.  (V  CHAR.)  Allied to  Yellow.     Der.  mari-gold.
7780:erild,  to  overlay  with  gold.  (E.)  M.  E. gildtn.  A.S.  gyldan,  to  gild  (Etlmlillcr)  ; d.  K.^. gyldfn,  golden.  Formed  (by  regular change  fioni  o  lojf)  from  gold,  gold.
9433:JargoneUe.  a  kind  of  pessr* Pcrs.?)     V.jargfffitiU,  a  atwJi itony   (UltrtE);    formed    (acC" fiom  F.  jargatt,  a  yellow  diomaodt stune.  —  Itai.  gio*-"^     * diamond.   Perhai'-.
=== LAT melancholia ===
```


## [2026-09-06T02:23:05.606Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WEB chalazion ===\"; grep -n -i \"chalazion\\|chalaza\" WEB_vol1.txt | head -4 | cut -c1-300\necho \"=== FSD chalazion ===\"; grep -n -i \"chalazion\" FSD_vol1.txt | head -3 | cut -c1-300\necho \"=== SKT glass ===\"; grep -n -i \"^Glass\" SKT.txt | head -3 | cut -c1-250\necho \"=== SKT chlorine ===\"; grep -n -i \"Chlorine\\|Chloro\" SKT.txt | head -3 | cut -c1-250",
 "description": "Webster/Funk&Wagnalls/Skeat checks"
}
```


### [2026-09-06T02:23:05.709Z] TOOL RESULT

```
=== WEB chalazion ===
30427:chab/a-zite, chab/a:site, n. (Fr. chabazie, missp. of Gr. chalazie, vocative of chalaza, hailstone.] a mineral classed with the zeolites, occurring in oblique, glassy crystals (rhombo-
30531:chalaza
30570:=  chalazal
30571:cha-la’zal, a. of a chalaza; as, the chalazal end
=== FSD chalazion ===
62150:See  illu3.  under  egg.  2.  Bot.  The  part  of  an  ovule  cnal-ci  tes,  1   kal-sai'tlz;  2   c3I-?i'teg,  n.  A   decomposi- where  the  coats  are  united  to  each  other  and  to  the  *ion  product  of  either  iron  or  copper  pyrites,  hence nucleus.  3.  See  chalazion.  [<  Gr. 
62155:especially  one  on  the  eyelid;  a   sty.  [<  Gr.  chalazion, dim.  of  chalaza,  pimple.]
85592:—   dentigerous  cyst,  a   dcrmatold  cyst  containing  teeth.  . piliferous  c.t>— Meibomian  c.,  same  as  chalazion. cj'st-ad"c-no'raa,  n.  Pathol.  An  adenoma  having  cysts.  * cys"to-ad"e-no'mat.—  cys-taPgl-a,  n.  Neuralgia  of  the bladder.— cys-tat'ro-phy,  n.  Pathol.  A
=== SKT glass ===
=== SKT chlorine ===
3409:Chlorine,    a    pale    green    gas. Nnmed  from  its  colour, green.     (V^HAR.)
3411:chloroform.  (L.  anJ  Gk.)  The  latlci clrment  rtlates  to  formic  acid,  an  acid formerly  ob.ained  from  red  aBts.»L.  /i»r- mittt.  an  ant,
10820:pale  yellow,  wan.     Perhaps  allied  to  Gk. xA*^,  green;  see  Chlorine. Ziurk.  to  lia  in  wait    (Scand.)     !£.£.
```


## [2026-09-06T02:23:54.755Z] AGENT

Now I'll write the verification file.


## [2026-09-06T02:30:35.933Z] TOOL CALL #68: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build186.py",
 "content": "# -*- coding: utf-8 -*-\nimport json\n\nW_KHIYAL_FA = \"https://en.wiktionary.org/wiki/خیال\"\nW_KHIYAL_AR = \"https://en.wiktionary.org/wiki/خيال\"\nE_MELAN = \"https://www.etymonline.com/word/melancholy\"\nW_ZALEH = \"https://en.wiktionary.org/wiki/ژاله\"\nW_GILAS = \"https://en.wiktionary.org/wiki/گیلاس\"\nW_MALIKH = \"https://en.wiktionary.org/wiki/مالیخولیا\"\nE_CHLPH = \"https://www.etymonline.com/word/chlorophyll\"\nW_JADA = \"https://en.wiktionary.org/wiki/जड\"\n\nPOK429 = (\"POK_full.txt, lemma 'ghel-1 (and ĝhel-1) … ghela- : ghle-, ghlo-', Meaning 'to shine; green, gold, blue, \"\n          \"yellow, moon', Page(s) 429-434: 'gr. χόλος \\\"gall, rage\\\", χολή \\\"gall\\\", χλωρός \\\"pale green, green yellow, \"\n          \"fresh\\\"'; 'Gothic gulþ, Old Icelandic gull, goll, Old English … gold \\\"gold\\\"'; 'Old English geolo … \"\n          \"\\\"yellow\\\"'; Avestan zari- 'yellow', zara- 'gall'.\")\nWAT_GHEL2 = (\"AHD_watkins1985.txt line 512: 'ghel-2. To shine; with derivatives referring to colors, bright materials \"\n             \"(probably \\\"yellow metal\\\"), and bile or gall … *ghlē-ro- in Greek khlōros, green, greenish yellow: \"\n             \"CHLORO- … *ghol-ā in Greek kholē, bile: CHOLE-, CHOLER, (CHOLERA); ACHOLIA, MELANCHOLY … Germanic \"\n             \"*gultham, gold … Old English gealu, yellow: YELLOW … Germanic *glasam, glass … GLAD … GLOW. \"\n             \"[Pok. 1. ĝhel- 429.]'\")\nWAT_GHELED = (\"AHD_watkins1985.txt line 515: 'gheled-. Hail. Zero-grade form *ghlēd- in Greek khalaza (< *khalad-ya), \"\n              \"a hailstone, hard lump, also a small cyst: CHALAZA, CHALAZION. [Pok. ghelǝd- 435.]'\")\nPOK435 = (\"POK_full.txt: 'Root / lemma: gheled- / Meaning: ice / Material: Npers. žala (*zalda) \\\"hail, hoarfrost\\\"; \"\n          \"gr. hom. χάλαζα \\\"hail\\\"; Old Church Slavic žlědica \\\"frozen rain\\\" … References: WP. I 629 f. Page(s): 435' \"\n          \"— no Sanskrit form is cited.\")\nWLD_GHELAD = (\"incoming/WLD/WLD_Bd1_pages.txt p.629: 'ghelad- „Eis“. Horn, [ž]āla „Hagel“; aksl. žledica „gefrorener \"\n              \"Regen“, sloven. zled „Glatteis“, klr. ozeleda …' — Persian žāla is entered directly, with a reference to \"\n              \"Horn, and no Sanskrit intermediary.\")\n\ndata = {\n  \"pdf_page\": 186,\n  \"book_page\": 156,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Ghel\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *ǵʰel- (Pokorny ĝhel-1, Watkins ghel-2) 'to shine; green, yellow, gold; gall, bile'\",\n      \"note\": (\"Pokorny 429-434 (ĝhel-1 'glänzen, schimmern; gelb, grün, grau, blau') and Watkins ghel-2 'to shine, with \"\n               \"derivatives referring to colors, bright materials (probably \\\"yellow metal\\\"), and bile or gall' are exactly \"\n               \"Nourai's root, gloss and page. This is PART 2 of the chart; the whole page hangs together well. The two \"\n               \"problem points on the page are not in the root but in two arrows: the Latin→Persian step for مالیخولیا \"\n               \"(the word came through Greek/Syriac/Arabic, not Latin) and, above all, Nourai's claim that Arabic خيال is \"\n               \"a mangled Persian خولیا, which he takes over from Addi Shir and which modern Arabic lexicography rejects.\"),\n      \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *ǵʰel- «درخشیدن؛ سبز، زرد، زرّین» است که پوکورنی آن را در صفحهٔ ۴۲۹ زیر ĝhel-1 و \"\n                  \"واتکینز زیر ghel-2 آورده‌اند؛ نام ریشه، برچسب زبانی و معنایی که نورایی داده است هر سه درست‌اند. \"\n                  \"شاخهٔ «صفرا» (یونانی χολή) و شاخهٔ «زرد/زرّین» (ژرمنی gold، yellow) هر دو در همان مدخل پوکورنی گرد آمده‌اند. \"\n                  \"دو حلقه از این نمودار پذیرفتنی نیست: راه ورود «مالیخولیا» به فارسی از لاتینی نبوده، و ادعای برگرفتگی \"\n                  \"«خیال» عربی از «خولیا» تنها نظر ادّی شیر است و ریشه‌شناسی امروزی آن را رد می‌کند.\"),\n      \"sources\": [E_MELAN, E_CHLPH],\n      \"ref_check\": [\n        {\"ref\": \"POK:429\", \"status\": \"supports\", \"note\": POK429}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"pp. 429-434, lemma ĝhel-1\", \"stance\": \"supports\", \"note\": POK429},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. ghel-2\", \"stance\": \"supports\", \"note\": WAT_GHEL2},\n        {\"src\": \"IEC\", \"where\": \"IEC.txt line 5968\", \"stance\": \"supports\",\n         \"note\": \"Mann: 'ǵhel- (ghelos, -es-, ǵhelis) \\\"green; greenery, vegetable; gold, golden\\\". WP I, 625. … Skt. hariḥ \\\"yellow, tawny\\\"; Per. zar \\\"gold\\\"; Av. zairiš, adj. \\\"yellow\\\"'\"},\n        {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. 'choler'\", \"stance\": \"supports\",\n         \"note\": \"Klein: 'χολή also χόλος \\\"gall, bile\\\", which is rel. to χλόος \\\"greenish-yellow colour\\\" … and cogn. with Avestic zara- \\\"gall, bile\\\", L. fel, OSlav. žlŭčĭ … OE. gealla \\\"gall\\\", fr. I.-E. base *ghel-, *ĝhel-, \\\"to shine; yellow, yellowish green, green\\\". See yellow.'\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Greek\",\n          \"words\": \"xlôros; xlôros-phullon\",\n          \"verdict\": \"plausible\",\n          \"derivation\": (\"Gk. χλωρός (khlōros) 'pale green, greenish-yellow, fresh' is the regular *ǵʰl̥h₃-ro-/*ǵʰlō-ro- \"\n                         \"formation of the root: zero/lengthened grade *ghlō- + the adjectival suffix -ro-, exactly parallel to \"\n                         \"Old Icelandic glóa 'to shine' and Old English glōm 'twilight' (Pokorny 429ff.). Watkins files it as \"\n                         \"'*ghlē-ro- in Greek khlōros, green, greenish yellow: CHLORO-'. The second item, however, is not an \"\n                         \"ancient Greek word: there is no attested Gk. *χλωρόφυλλον. 'Chlorophylle' was coined in French in \"\n                         \"1818 by Pelletier and Caventou out of khlōros + φύλλον phullon 'leaf' (PIE *bhel- 'to thrive, bloom', \"\n                         \"hence Nourai's cross-reference ☞Bhel); English chlorophyll follows in 1819. So the node is right about \"\n                         \"the Greek material but presents a 19th-century neoclassical compound as if it were Greek.\"),\n          \"derivation_fa\": (\"یونانی χλωρός (khlōros) «سبزِ زردفام، تر و تازه» صورت -ro دار ریشهٔ *ǵʰel- است و با gold و glow \"\n                            \"ژرمنی هم‌ریشه است (پوکورنی، ص ۴۲۹ به بعد؛ واتکینز، ghel-2). امّا ترکیب «xlôros-phullon» واژه‌ای \"\n                            \"یونانی باستان نیست: chlorophylle را در سال ۱۸۱۸ م. دو شیمی‌دان فرانسوی، پلتیه و کاوانتو، از \"\n                            \"khlōros «سبز» و phullon «برگ» ساختند. پس ادعای نورایی دربارهٔ خودِ khlōros درست است، ولی \"\n                            \"ترکیب یادشده ساختهٔ سدهٔ نوزدهم است، نه واژه‌ای بازمانده از یونانی.\"),\n          \"sources\": [E_CHLPH],\n          \"ref_check\": [\n            {\"ref\": \"AHD:236\", \"status\": \"partial\",\n             \"note\": (\"AHD:236 is a body page of the 1975 New College edition (the 'chlor-' entries), which is not on disk; \"\n                      \"the accessible edition of the same work, Watkins 1985, supports the derivation at ghel-2: \" + WAT_GHEL2)}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 429ff., lemma ĝhel-1\", \"stance\": \"supports\",\n             \"note\": \"'gr. χόλος \\\"gall, rage\\\", χολή \\\"gall\\\", χλωρός \\\"pale green, green yellow, fresh, strong\\\" (: Old Icelandic glóa \\\"radiance\\\")'\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. 'chlorine' / 'Chloris'\", \"stance\": \"supports\",\n             \"note\": \"Klein s.v. Chloris: 'Gk. Χλωρίς, lit. \\\"greenness, freshness\\\", which is rel. to χλωρός'; s.v. chlorine: 'fr. Gk. χλωρός, \\\"greenish yellow, pale green, green, fresh\\\"'\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt line 3409\", \"stance\": \"supports\",\n             \"note\": \"Skeat: 'Chlorine, a pale green gas. Named from its colour … [Gk.] χλωρός, green.'\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": (\"Empty pass-through node for the French chemical vocabulary built on khlōros: chlore (the French \"\n                         \"renaming of Davy's 1810 'chlorine'), chlorophylle (Pelletier & Caventou 1818), chloroforme \"\n                         \"(named by Dumas 1834). French is the correct intermediary for the Persian forms below, because \"\n                         \"Persian scientific terminology of the late Qajar and early Pahlavi period was taken from French, \"\n                         \"not English — which is why Persian has کلر (not *کلراین) and کلروفرم (not *کلروفورم).\"),\n          \"derivation_fa\": (\"گرهٔ واسطهٔ تهی برای واژگان شیمیایی فرانسه که بر پایهٔ khlōros ساخته شده‌اند: chlore، \"\n                            \"chlorophylle (۱۸۱۸ م.) و chloroforme (۱۸۳۴ م.). فرانسه حلقهٔ درست میانی است، زیرا اصطلاحات \"\n                            \"علمی فارسی در اواخر دورهٔ قاجار و آغاز پهلوی از راه فرانسه وارد شده‌اند؛ گواهِ آن صورت «کلر» \"\n                            \"(نه *کلراین انگلیسی) است.\"),\n          \"sources\": [E_CHLPH],\n          \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the chart gives no reference for this pass-through node\"}],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. 'chlorine'\", \"stance\": \"supports\",\n             \"note\": \"'Coined by the English chemist Sir Humphrey Davy (1778-1829) fr. Gk. χλωρός' — French chlore is the calque of this coinage\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt line 3411\", \"stance\": \"supports\",\n             \"note\": \"Skeat s.v. chloroform: '(L. and Gk.) The latter element relates to formic acid … L. formica, an ant' — the compound is modern, made on Greek chlor-\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"kolor «کلر»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": (\"Persian کلر kolr/kolor 'chlorine' is a straight borrowing of French chlore, with the French \"\n                         \"final -e dropped and the cluster kl- kept (Persian has no initial cluster, so the word is read \"\n                         \"kolr with an epenthetic vowel). The chart's extras follow the same route: کلروفیل ← chlorophylle, \"\n                         \"کلروفرم ← chloroforme. Mo'in's Farhang has the entry کلر with the chemical definition 'شبه‌فلزی است \"\n                         \"زرد مایل به سبز … بوی خفه‌کننده' and کلروفرم tagged with the French form chloroforme.\"),\n          \"derivation_fa\": (\"«کلر» وام‌واژه‌ای است از فرانسهٔ chlore؛ ‑e پایانی فرانسه افتاده و خوشهٔ آغازین kl- با واکهٔ \"\n                            \"میانجی خوانده می‌شود. «کلروفیل» از chlorophylle و «کلروفرم» از chloroforme نیز از همین راه \"\n                            \"آمده‌اند. معین در فرهنگ فارسی هر سه را با صورت فرانسوی آورده است. ادعای نورایی درست است.\"),\n          \"sources\": [E_CHLPH],\n          \"ref_check\": [\n            {\"ref\": \"MON\", \"status\": \"supports\",\n             \"note\": (\"MON_part2.txt line ~25009: headword «کلر» '(شیم.) شبه فلزی است زرد مایل به سبز، در شرایط متعارفی گازی شکل، \"\n                      \"بوی خفه کننده …'; line 25084 «کلروفرم: chloroforme (ا.) (پز. شیمی) مایعی است بی‌رنگ و بیهوش کننده به فرمول CHCl₃'. \"\n                      \"Nourai cites MON without a page; the entries exist and match.\")}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part2.txt (2-vol Adena condensation), s.vv. کلر, کلروفرم, کلروفیل\", \"stance\": \"supports\",\n             \"note\": \"«کلروفرم: chloroforme … مایعی است بی‌رنگ و بیهوش کننده»; «کلروفیل» used in the plant entries — all with the French form\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' (17th c. text, Mo'in's ed.)\", \"stance\": \"silent\",\n             \"note\": \"grep of BQT_v1/v2_pages.txt for کلر gives no dictionary entry; as expected, a 19th-20th c. European chemical term is absent from Borhan\"},\n            {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_pages.txt\", \"stance\": \"silent\",\n             \"note\": \"grep 'کلر' returns no headword; Aryanpur lists only inherited Indo-European Persian vocabulary, not modern chemical loans\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"chlorine, chlorophyll\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": (\"Both are neoclassical coinages on Greek khlōros. 'Chlorine' was named in 1810 by Humphry Davy, \"\n                         \"who had shown that Scheele's 'dephlogisticated marine acid air' was an element, and called it from \"\n                         \"its yellow-green colour, with the chemical suffix -ine (as in bromine, iodine, fluorine). \"\n                         \"'Chlorophyll' entered English in 1819 from French chlorophylle (1818). Neither passed through Latin \"\n                         \"or French phonology in any interesting way; they are learned formations.\"),\n          \"derivation_fa\": (\"هر دو واژه ساختهٔ نوکلاسیک بر پایهٔ khlōros یونانی‌اند: chlorine را در ۱۸۱۰ م. همفری دیوی به سبب \"\n                            \"رنگ سبز-زردِ این گاز با پسوند شیمیایی ‑ine ساخت، و chlorophyll در ۱۸۱۹ م. از فرانسهٔ \"\n                            \"chlorophylle به انگلیسی رفت. ادعای نورایی دربارهٔ این گره درست است.\"),\n          \"sources\": [E_CHLPH],\n          \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the chart gives no reference for this node\"}],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. 'chlorine'\", \"stance\": \"supports\",\n             \"note\": \"'Coined by the English chemist Sir Humphrey Davy (1778-1829) fr. Gk. χλωρός … For the ending see chem. suff. -ine and cp. brom-ine, fluor-ine, iod-ine.'\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt line 3409\", \"stance\": \"supports\",\n             \"note\": \"'Chlorine, a pale green gas. Named from its colour … green.'\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985, index and s.v. ghel-2\", \"stance\": \"supports\",\n             \"note\": \"index line 1356: 'CHLOASMA ghel-2 CHLORITE¹ ghel-2 CHLORO- ghel-2'\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Greek\",\n          \"words\": \"xolĕ; melan-xolia\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": (\"Gk. χολή kholē (and masc. χόλος kholos) 'gall, bile' continues the o-grade *ǵʰol-eh₂ of the same \"\n                         \"root: bile was named from its yellow-green colour, exactly as Avestan zara- 'gall' beside zari- \"\n                         \"'yellow', Latin fel, Old English gealla (Pokorny 429ff.). μελαγχολία melankholia 'black bile' is a \"\n                         \"compound of μέλας melas, gen. μέλανος (PIE *mel- 'dark, dirty' — Nourai's ☞Mel 1) and kholē; in \"\n                         \"Hippocratic-Galenic humoral medicine the excess of black bile causes the disease μελαγχολία, so \"\n                         \"the gloss 'black bile, a disease' is precisely right.\"),\n          \"derivation_fa\": (\"یونانی χολή (kholē) «صفرا، زَهره» از درجهٔ o همان ریشه (*ǵʰol-) است: صفرا را به سبب رنگ زرد-سبزش \"\n                            \"چنین نامیده‌اند، درست همان‌گونه که در اوستایی zara- «زهره» کنار zari- «زرد» می‌آید (پوکورنی ۴۲۹). \"\n                            \"μελαγχολία ترکیبی است از μέλας «سیاه» و χολή «صفرا»، یعنی «سودا / صفرای سیاه»؛ در طب اخلاطی \"\n                            \"بقراطی-جالینوسی فزونی این خلط بیماری سودا را پدید می‌آورد. ادعای نورایی درست است.\"),\n          \"sources\": [E_MELAN],\n          \"ref_check\": [\n            {\"ref\": \"AHD:817\", \"status\": \"partial\",\n             \"note\": (\"AHD:817 is a body page of the 1975 New College edition ('melancholy'), not on disk; the same work's \"\n                      \"root appendix in the accessible 1985 Watkins edition supports it: '*ghol-ā in Greek kholē, bile: \"\n                      \"CHOLE-, CHOLER, (CHOLERA); ACHOLIA, MELANCHOLY' (AHD_watkins1985.txt line 512), and the index line \"\n                      \"1845 reads 'MELANCHOLY ghel-2, mel-2'.\")}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 429ff.\", \"stance\": \"supports\",\n             \"note\": \"'gr. χόλος \\\"gall, rage, fury\\\", χολή \\\"gall, rage, fury\\\", χολ-έρα \\\"stomach disease\\\"'\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.vv. 'choler', 'melancholy'\", \"stance\": \"supports\",\n             \"note\": \"'melancholy, n. — … fr. Gk. μελαγχολία, \\\"atrabiliousness\\\", lit. \\\"black bile\\\", fr. μέλας, gen. μέλανος, \\\"black\\\", and χολή \\\"bile\\\". See melano- and choler.'\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt line 11355\", \"stance\": \"supports\",\n             \"note\": \"Skeat s.v. Melancholy: 'Supposed to be due to an excess of bile … Gk. μελαγχολία … μέλαν-, stem of μέλας, black; χολή, bile, gall.'\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Latin\",\n          \"words\": \"melancholia\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": (\"Late Latin melancholia is a straight transliteration of Gk. μελαγχολία, taken over with the whole \"\n                         \"Galenic humoral vocabulary by the Latin medical writers (Caelius Aurelianus, and later the \"\n                         \"Salernitan and scholastic tradition); Greek χ was rendered ch, ‑ία became ‑ia. Classical Latin had \"\n                         \"the calque atra bilis 'black bile' beside it (Klein s.v. atrabiliary: 'loan translation of Gk. \"\n                         \"μέλαινα χολή').\"),\n          \"derivation_fa\": (\"لاتینی متأخر melancholia آوانویسی مستقیم μελαγχολία یونانی است که همراه با کل دستگاه طب اخلاطی \"\n                            \"جالینوسی به لاتینی راه یافت؛ χ یونانی به ch و ‑ία به ‑ia بدل شد. لاتینی کلاسیک در کنار آن \"\n                            \"گَردهٔ atra bilis «صفرای سیاه» را نیز داشت. این حلقه درست است.\"),\n          \"sources\": [E_MELAN],\n          \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the chart gives no reference for this node\"}],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.vv. 'melancholia', 'atrabiliary'\", \"stance\": \"supports\",\n             \"note\": \"'melancholia, n. — Late L. See melancholy.'; 'atrabiliarius, \\\"suffering from black bile\\\", fr. L. atra bilis … loan translation of Gk. μέλαινα χολή'\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet (LAT.txt) and Walde-Hofmann (LEW_1910.txt)\", \"stance\": \"silent\",\n             \"note\": \"grep 'melancholia|melancholicus' returns nothing: neither Latin etymological dictionary treats it, as expected of a transparent Greek medical loan\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Persian\",\n          \"words\": \"mâlîxŭlîâ «مالیخولیا»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": (\"The Persian word is genuinely Gk. μελαγχολία, and its Persian shape proves the route. The older and \"\n                         \"correct Persian/Arabic form is مالنخولیا mālanḵūliyā, which still shows Greek melan-; مالیخولیا is a \"\n                         \"later scribal corruption (مصحف) of it, with n > y. The transmission was Greek → Syriac → Arabic in the \"\n                         \"9th-century Baghdad translation movement (Hunayn ibn Ishaq's versions of Galen and of Rufus of \"\n                         \"Ephesus' book on melancholy; Ishaq ibn Imran's Maqala fi l-malinḵūliya), and from that Arabic medical \"\n                         \"vocabulary into Persian — not from Latin, which had no contact channel with Persian in that period. \"\n                         \"Mo'in's own footnote at Borhan p.1947 names the Latin form ('لاتینی melancholia از یونانی \"\n                         \"melancholia'), which is presumably where Nourai took his Latin box from, but Mo'in is giving the \"\n                         \"European form of the word, not the route into Persian. The extra خولیا is the second element by \"\n                         \"itself: Mo'in at Borhan p.795 s.v. خولیا says it 'is from Greek χολή, meaning bile'. Verdict: right \"\n                         \"root and right ultimate source, wrong intermediary.\"),\n          \"derivation_fa\": (\"«مالیخولیا» در اصل همان μελαγχολία یونانی است و صورت کهن‌تر و درست‌ترِ آن در فارسی و عربی \"\n                            \"«مالنخولیا» است که هنوز melan- یونانی را نگاه داشته؛ «مالیخولیا» مصحّفِ آن است (ابدال ن به ی). \"\n                            \"راه ورود آن یونانی ← سریانی ← عربی بوده است، در نهضت ترجمهٔ سدهٔ سوم هجری (ترجمه‌های حنین بن اسحاق \"\n                            \"از جالینوس و روفس، و «مقاله فی المالنخولیا»ی اسحاق بن عمران)، و از همان واژگان طبی عربی به فارسی \"\n                            \"رسیده است؛ نه از لاتینی، که در آن روزگار هیچ مجرای تماسی با فارسی نداشت. معین در حاشیهٔ برهان \"\n                            \"(ص ۱۹۴۷) صورت لاتینی melancholia را یاد کرده و گویا نورایی خانهٔ «لاتینی» را از همان‌جا گرفته است، \"\n                            \"ولی معین صورت اروپایی واژه را می‌آورد نه مسیر ورودش به فارسی. «خولیا» نیز به تصریح معین در برهان \"\n                            \"(ص ۷۹۵) «از یونانی χολή است بمعنی صفرا». پس: ریشه درست، واسطه نادرست — با احتیاط پذیرفتنی.\"),\n          \"sources\": [W_MALIKH, E_MELAN],\n          \"ref_check\": [\n            {\"ref\": \"BQT:795\", \"status\": \"supports\",\n             \"note\": (\"BQT_v2_pages.txt leaf 255 (printed p.795), headword «خولیا», Mo'in's footnote: «خولا در کلمهٔ مرکب \"\n                      \"\\\"مالیخولا\\\" (ه.م) و \\\"مالنخولا\\\" … از یونانی χολή است بمعنی صفرا.» — supports the Greek kholē source of \"\n                      \"the second element exactly as the chart draws it.\")},\n            {\"ref\": \"BQT:1947\", \"status\": \"partial\",\n             \"note\": (\"incoming/BQT/BQT_v4_pages.txt [pdf page 30] = printed p.1947, s.v. «مالیخولیا», Mo'in's footnote 10: \"\n                      \"«مصحف مالنخولیا، لاتینی melancholia از یونانی melancholia … مرکب از melan (سیاه) و kholē (خلط صفرا) \"\n                      \"جمعاً بمعنی خلط سیاه … این لغت بصور ماخولیا، ملنخولیا، مالیخ، مالنخ و غیره در آمده است.» Mo'in does name \"\n                      \"the Latin form, which is what Nourai's Latin box rests on, but he calls the Persian word a corruption of \"\n                      \"مالنخولیا and derives it from Greek, not from Latin.\")}\n          ],\n          \"consulted\": [\n            {\"src\": \"BQT\", \"where\": \"BQT_v4_pages.txt pdf p.30 (printed 1947) and BQT_v2_pages.txt leaf 255 (printed 795)\", \"stance\": \"partial\",\n             \"note\": \"«مصحف مالنخولیا … از یونانی melancholia»; «خولا … از یونانی χολή است بمعنی صفرا»\"},\n            {\"src\": \"MON\", \"where\": \"MON_part2.txt line 43025 s.v. مالیخولیا\", \"stance\": \"partial\",\n             \"note\": \"Mo'in's Farhang: «مالیخولیا: [مصحف. مالنخولیا] (پز.) گونه‌ای مرض دماغی …» and «صح. \\\"مالنخولیا\\\" بصورت‌های: مالیخولیا، ماخولیا، ملنخولیا، مالیخ، مالنخ و غیره در آمده» — Greek origin, corrupted Persian form; no Latin route\"},\n            {\"src\": \"PLA\", \"where\": \"incoming/PLA/PLA_pages.txt (Asbaghi 1988)\", \"stance\": \"silent\",\n             \"note\": \"no entry mālinḵūliyā; Asbaghi lists only Persian loans in Arabic, and the word is Greek in Arabic, so its absence is expected and consistent\"},\n            {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_pages.txt\", \"stance\": \"silent\",\n             \"note\": \"grep 'مالیخولیا' finds nothing — Aryanpur covers only inherited Indo-European Persian words\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Arabic\",\n          \"words\": \"xîyâl\",\n          \"verdict\": \"disputed\",\n          \"derivation\": (\"Nourai's NOTE — 'Arabic xîyâl is a distorted form of Persian xŭlîa: imagination' — comes verbatim from \"\n                         \"his cited source: Addi Shir, al-Alfaz al-farisiyya al-mu'arraba p.59, s.v. الخيال: «الظن والوهم مثل \"\n                         \"خوليا لفظاً ومعنى» ('supposition and fancy, like khūliyā in form and meaning'). Modern Arabic \"\n                         \"lexicography does not accept it. خَيال belongs to the fully productive Semitic root خ-ي-ل: خالَ \"\n                         \"يَخالُ/يَخِيلُ 'to suppose, imagine, seem', تَخَيَّلَ 'to imagine', مُخَيِّلة 'imaginative faculty', \"\n                         \"أخْيَل 'green woodpecker', خُيَلاء 'conceit' — and طَيْف الخَيال, 'the phantom of the beloved that visits \"\n                         \"at night', is a stock motif of pre-Islamic poetry, i.e. the word is in use long before any Greek \"\n                         \"medical text was translated into Arabic. Semantically the two words are far apart as well: خولیا in \"\n                         \"Arabic/Persian means 'bile' (the humour), never 'imagination'; the 'imagination' sense is Nourai's own \"\n                         \"back-formation from مالیخولیا. Asbaghi's Persische Lehnwörter im Arabischen (1988), the standard \"\n                         \"modern inventory of Persian loans in Arabic, has no ḫayāl. Verdict: disputed — a chance resemblance \"\n                         \"(خ-ول / خ-ي-ل) that Addi Shir, an enthusiastic collector of supposed Persian loans, took for a \"\n                         \"borrowing.\"),\n          \"derivation_fa\": (\"یادداشت نورایی که «خیالِ عربی صورت دگرگون‌شدهٔ خولیای فارسی است» عیناً از مأخذ خودش گرفته شده: \"\n                            \"ادّی شیر در «الألفاظ الفارسیة المعرّبة» ص ۵۹ ذیل «الخیال» می‌نویسد: «الظن والوهم مثل خولیا لفظاً \"\n                            \"ومعنی». ریشه‌شناسی امروزی این را نمی‌پذیرد. «خیال» از ریشهٔ زایای سامی خ-ی-ل است: خالَ یَخالُ \"\n                            \"«پنداشتن»، تَخَیَّلَ، مُخَیِّلة، خُیَلاء، أخْیَل؛ و «طیف الخیال» از بن‌مایه‌های شعر جاهلی است، یعنی \"\n                            \"واژه سده‌ها پیش از نهضت ترجمهٔ متون یونانی در عربی به کار می‌رفته. از سوی معنایی نیز «خولیا» در \"\n                            \"عربی و فارسی «صفرا»ست نه «پندار». اصباغی نیز در «وام‌واژه‌های فارسی در عربی» (۱۹۸۸) آن را در \"\n                            \"شمار وام‌واژه‌های فارسی نیاورده است. پس این حلقه، شباهت آوایی تصادفی است و پژوهش امروزی آن را رد \"\n                            \"می‌کند.\"),\n          \"sources\": [W_KHIYAL_AR],\n          \"ref_check\": [\n            {\"ref\": \"AFM:59\", \"status\": \"supports\",\n             \"note\": (\"AFM_alt.txt line 2265 (Addi Shir, خ section; the index at line 7061 gives خولیا p.59): «( الخيال ) الظن \"\n                      \"والوهم مثل خوليا لفظاً ومعنى» — the reference does say exactly what Nourai's NOTE says; it is Nourai's \"\n                      \"source. It is the claim itself, not the citation, that is wrong.\")},\n            {\"ref\": \"FVF:223\", \"status\": \"not_checked\",\n             \"note\": \"Emam Shushtari, Farhang-e vazheha-ye farsi dar zaban-e arabi: no local copy and no fetchable online text (noorlib/ketabnak need a login); refs_online.json marks it kind=website with local_file null\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AFM\", \"where\": \"Addi Shir p.59 s.v. الخيال (AFM_alt.txt line 2265)\", \"stance\": \"supports\",\n             \"note\": \"«الظن والوهم مثل خوليا لفظاً ومعنى»\"},\n            {\"src\": \"PLA\", \"where\": \"incoming/PLA/PLA_pages.txt (Asbaghi, Persische Lehnwörter im Arabischen 1988)\", \"stance\": \"contradicts\",\n             \"note\": \"no entry for ḫayāl anywhere in the book (greps for 'ayäl', 'hayal' return only ṭayālis); the standard modern inventory of Persian loans in Arabic does not count خيال among them\"},\n            {\"src\": \"FVQ\", \"where\": \"FVQ_pages.txt (Jeffery, Foreign Vocabulary of the Qur'an)\", \"stance\": \"silent\",\n             \"note\": \"no entry — Jeffery does not treat خيال as a foreign word\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt\", \"stance\": \"silent\",\n             \"note\": \"Klein has no Arabic ḵayāl entry (the word did not enter European languages), so no independent Western check from this book\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Persian\",\n          \"words\": \"xîyâl «خیال»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": (\"Taken on its own, this arrow is right: New Persian خیال ḵiyāl 'imagination, fancy, image, phantom' \"\n                         \"is a straightforward Arabic loan (Mo'in tags the entry «[ع.]»), together with the rest of the root's \"\n                         \"family that Persian borrowed — تخیّل taḵayyol, متخیّله, خیالی, خیال‌پرداز; Nourai's extra تخیّل is the \"\n                         \"Arabic form V verbal noun. It arrives with the philosophical vocabulary of Avicenna's Persian and \"\n                         \"Arabic works, where خیال is the technical faculty that stores the forms received by the sensus \"\n                         \"communis — exactly the definition Mo'in reproduces. What is wrong is the step above it: since node #8 \"\n                         \"is not a Persian word to begin with, this is a plain Arabic loan into Persian, not the Persian → \"\n                         \"Arabic → Persian round trip the chart draws.\"),\n          \"derivation_fa\": (\"خودِ این حلقه درست است: «خیال» در فارسی نو وام‌واژه‌ای است از عربی، و معین نیز آن را با نشانهٔ \"\n                            \"«[ع.]» آورده است؛ همراه با دیگر مشتقات همان ریشه که فارسی وام گرفته: تخیّل، متخیّله، خیالی، \"\n                            \"خیال‌پرداز. این واژه با واژگان فلسفی ابن‌سینا وارد فارسی شده، در معنای قوّه‌ای که صورت‌های \"\n                            \"دریافتهٔ حسّ مشترک را نگاه می‌دارد — همان تعریفی که معین نقل می‌کند. آنچه نادرست است حلقهٔ بالاتر \"\n                            \"است: چون گرهٔ ۸ اصلاً واژه‌ای فارسی نیست، اینجا وام‌گیری سادهٔ عربی به فارسی داریم، نه رفت‌وبرگشتِ \"\n                            \"فارسی ← عربی ← فارسی که نمودار نشان می‌دهد.\"),\n          \"sources\": [W_KHIYAL_FA],\n          \"ref_check\": [\n            {\"ref\": \"MON:1466\", \"status\": \"supports\",\n             \"note\": (\"MON_part1.txt line 58473 (2-vol condensation of the same Farhang): «خیال: [ع.] (اِ.) گمان؛ وهم. صورتی که \"\n                      \"در خواب دیده شود … (فل. قد.) قوه‌ای است که در موخر تجویف اول دماغ گذارده شده و صوری را که حس مشترک ادراک \"\n                      \"کرده است نگاه می‌دارد …؛ ج. اخیله، خیالات.» The «[ع.]» tag is Mo'in's mark for an Arabic loan — exactly \"\n                      \"the arrow drawn. Page 1466 of the 6-vol edition could not be verified (only the 2-vol condensation is on \"\n                      \"disk), but the entry is there.\")}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt line 58473 s.v. خیال\", \"stance\": \"supports\",\n             \"note\": \"«خیال: [ع.] (اِ.) گمان؛ وهم …» — Arabic-loan tag\"},\n            {\"src\": \"BQT\", \"where\": \"BQT_v2_pages.txt leaf 255 (printed p.795)\", \"stance\": \"partial\",\n             \"note\": \"the Borhan page has «(عر) خال، بمعنی پرستاری کرد و مصدر آن خول … و خیال بر وزن کتاب است، \\\"شرح قاموس\\\"» — i.e. Borhan/its commentators also treat خیال as Arabic, quoting the Qamus\"},\n            {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_pages.txt\", \"stance\": \"silent\",\n             \"note\": \"grep finds no headword خیال — Aryanpur's Indo-European root dictionary excludes Arabic loans, which is itself consistent with the word being Arabic\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": (\"Empty pass-through node: Old French melancolie (also malencolie by folk-association with mal 'ill'), \"\n                         \"attested from the 12th century, is the popular French continuation of Late Latin melancholia, with \"\n                         \"loss of the -h-, ch > k and the learned ending -ia > -ie. Modern French mélancolie.\"),\n          \"derivation_fa\": (\"گرهٔ واسطهٔ تهی: فرانسهٔ کهن melancolie (و گونهٔ malencolie به قیاسِ mal «بد») از سدهٔ دوازدهم \"\n                            \"میلادی، دنبالهٔ عامیانهٔ melancholia لاتینی متأخر است؛ ‑h‑ افتاده و پایانهٔ عالمانهٔ ‑ia به ‑ie بدل \"\n                            \"شده است. این حلقه درست است.\"),\n          \"sources\": [E_MELAN],\n          \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the chart gives no reference for this pass-through node\"}],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. 'melancholy'\", \"stance\": \"supports\",\n             \"note\": \"'ME. melancolie, fr. OF. melancolie (F. mélancolie), fr. Late L. melancholia'\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt line 11355\", \"stance\": \"supports\",\n             \"note\": \"Skeat: 'M.E. melancholie — O.F. melancolie — L. melancholia — Gk. μελαγχολία'\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"English\",\n          \"words\": \"melancholy\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": (\"Middle English melancolie / malencolie, from about 1300, borrowed from Old French; the modern \"\n                         \"spelling with -ch- is a Renaissance re-latinisation. The sense history runs from the humour itself \"\n                         \"('the grossest of the foure corporall humours', Cockeram 1623) through 'mental disorder marked by \"\n                         \"gloom and irritability' to the modern 'habitual sadness' once humoral medicine was abandoned in the \"\n                         \"18th century.\"),\n          \"derivation_fa\": (\"انگلیسی میانه melancolie / malencolie از حدود ۱۳۰۰ م.، وام‌گرفته از فرانسهٔ کهن؛ املای امروزی با \"\n                            \"‑ch‑ لاتینی‌سازی دوبارهٔ دورهٔ رنسانس است. تحول معنایی از خودِ خلط سودا، به «اختلال دماغی همراه \"\n                            \"افسردگی و تندخویی» و سرانجام پس از کنار رفتن طب اخلاطی در سدهٔ هجدهم به «اندوه دیرپا» رسیده است. \"\n                            \"این حلقه درست است.\"),\n          \"sources\": [E_MELAN],\n          \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the chart gives no reference for this node\"}],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. 'melancholy'\", \"stance\": \"supports\",\n             \"note\": \"'melancholy, n. — ME. melancolie, fr. OF. melancolie …'\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt line 11355\", \"stance\": \"supports\",\n             \"note\": \"'Melancholy, sadness. (F.-L.-Gk.) … M.E. melancholie.'\"}\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"Germanic\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": (\"Empty pass-through node for Proto-Germanic. Grimm's law turns PIE *ǵʰ- into Gmc *g-, so the root \"\n                         \"appears as *gel-/*gul-/*glō-: *gelwaz 'yellow' (< *ǵʰel-wo-), *gulþa- 'gold' (< *ǵʰl̥-to-), \"\n                         \"*gallōn- 'gall' (< *ǵʰol-n-), *glasa- 'glass' and a whole nest of late *gl- formations for shining \"\n                         \"(*glōan, *glitrōn, *gladaz). Pokorny and Watkins list all of these under the same root.\"),\n          \"derivation_fa\": (\"گرهٔ واسطهٔ تهی برای ژرمنی آغازین. بر پایهٔ قانون گریم، *ǵʰ هندواروپایی در ژرمنی به *g بدل می‌شود \"\n                            \"و ریشه به صورت‌های *gel-/*gul-/*glō- درمی‌آید: *gelwaz «زرد»، *gulþa- «زر»، *gallōn- «زهره»، \"\n                            \"*glasa- «شیشه» و انبوهی ساخت *gl- به معنی درخشیدن. پوکورنی و واتکینز همهٔ اینها را زیر همین \"\n                            \"ریشه آورده‌اند.\"),\n          \"sources\": [],\n          \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the chart gives no reference for this pass-through node\"}],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"pp. 429-434\", \"stance\": \"supports\",\n             \"note\": \"'Gothic gulþ, Old Icelandic gull, goll, Old English Old Frisian Old Saxon Old High German gold \\\"gold\\\"'; 'zero grade Old Icelandic gulr \\\"yellow\\\", besides full grade Old English geolo'\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ghel-2 §IV\", \"stance\": \"supports\",\n             \"note\": \"'IV. A range of Germanic words … Germanic *glasam, glass, in Old English glæs … Germanic *gladaz in Old English glæd, shining, joyful: GLAD … Germanic *glō- in Old English glōwan, to glow'\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. 'glass'\", \"stance\": \"supports\",\n             \"note\": \"'rel. to OS. glas, gles, ON. gler … fr. I.-E. base *ghles-, *ĝhles-, \\\"to shine, glitter\\\", which is an enlargement of base *ghel-, *ĝhel-, *ghlē-'\"}\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"English\",\n          \"words\": \"gold, yellow, glass, gloss, glow, glad\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": (\"All six are Watkins' ghel-2. gold < OE gold < Gmc *gulþam < *ǵʰl̥-to- 'the yellow (metal)', cf. OCS \"\n                         \"zlato, Skt. hiraṇya-, Av. zaranya-. yellow < OE geolu < Gmc *gelwaz < *ǵʰel-wo-, cf. Lat. helvus \"\n                         \"'honey-yellow', Lith. geltas. glass < OE glæs < Gmc *glasa-, from the s-extension *ǵʰles- 'to shine' \"\n                         \"(same word as Lat. glaesum 'amber'). glow < OE glōwan < Gmc *glō- (: Gk. khlōros). glad < OE glæd \"\n                         \"'shining, bright, joyful' < Gmc *gladaz — the 'bright' sense is the older one, 'joyful' the \"\n                         \"development. gloss 'lustre' is the weakest member: Watkins gives it as 'Icelandic glossi, a spark, \"\n                         \"perhaps akin to the source of GLOSS¹', i.e. a Scandinavian word of the same *gl- nest but without a \"\n                         \"secure preform (and it must be kept apart from gloss 'marginal note' < Gk. glōssa, a different \"\n                         \"root).\"),\n          \"derivation_fa\": (\"هر شش واژه زیر ghel-2 واتکینز جای می‌گیرند: gold از انگلیسی کهن gold و ژرمنی *gulþam < \"\n                            \"*ǵʰl̥-to- «فلز زرد»، هم‌ریشه با zaranya- اوستایی و «زر» فارسی؛ yellow از geolu و *gelwaz؛ \"\n                            \"glass از *glasa- که گسترش s-دار ریشه (*ǵʰles- «درخشیدن») است؛ glow از *glō- (هم‌ریشه با khlōros \"\n                            \"یونانی)؛ glad از glæd به معنی نخستین «درخشان»، سپس «شادمان». تنها gloss «جلا» سست‌تر است: \"\n                            \"واتکینز آن را با تردید به glossi ایسلندی «جرقّه» می‌بندد، و باید آن را از gloss «حاشیه، تفسیر» \"\n                            \"که از glōssa یونانی است جدا داشت. در مجموع ادعای نورایی درست است.\"),\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\",\n             \"note\": (\"AHD_watkins1985.txt line 512 s.v. ghel-2 lists YELLOW, CHLORO-, GOLD, GILD, GLASS, GLAZE, GLAD, GLEE, \"\n                      \"GLOW, GLOWER and 'Icelandic glossi, a spark, perhaps akin to the source of GLOSS¹'; the reverse index \"\n                      \"(lines 1561-1565) confirms 'GLAD ghel-2 … GLASS ghel-2 … GLOSS¹ ghel-2 … GLOW ghel-2 … GOLD ghel-2'.\")}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ghel-2 and index\", \"stance\": \"supports\",\n             \"note\": \"'GLAD ghel-2 … GLASS ghel-2 … GLOSS¹ ghel-2 … GLOW ghel-2'; 'GOLD ghel-2' (index line 1565)\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt line 7779\", \"stance\": \"supports\",\n             \"note\": \"Skeat: 'Gold. (E.) A.S. gold. + Du. goud, Icel. gull, Swed. Dan. guld, G. gold, Goth. gulth, Russ. zlato, Gk. χρυσός(?), Zend zaranya, Skt. hiraṇya. Allied to Yellow.'\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. 'glass'\", \"stance\": \"supports\",\n             \"note\": \"'fr. I.-E. base *ghles-, *ĝhles-, \\\"to shine, glitter\\\", which is an enlargement of base *ghel- … Cp. glare, glaze, glow … Cp. also yellow.'\"}\n          ]\n        },\n        {\n          \"id\": 14,\n          \"lang\": \"Persian\",\n          \"words\": \"gîlâs «گیلاس ۱»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": (\"Persian گیلاس gilās 'tumbler, drinking glass' is a modern loan of English glass, taken in through the \"\n                         \"Indian route: Urdu/Hindi گلاس گِلاس gilās (an Anglo-Indian usage) → Persian گیلاس, with the \"\n                         \"prothetic/epenthetic i breaking up the initial gl- cluster that Persian phonotactics does not allow. \"\n                         \"Mo'in's entry glosses it «ظرفی بلوری به اشکال مختلف که جهت نوشیدن آب یا انواع مشروبات بکار رود؛ \"\n                         \"لیوان» and gives the Latin-script etymon glass. It is a homonym of the inherited-looking گیلاس ۲ \"\n                         \"'cherry', which is a quite separate word from Greek κεράσι(ον) via Byzantine/Anatolian contact, and \"\n                         \"Nourai correctly cites Mo'in's numbered entry to keep the two apart.\"),\n          \"derivation_fa\": (\"«گیلاس» به معنی لیوان، وام‌واژه‌ای نو از انگلیسی glass است که از راه هند وارد شده: اردو/هندی \"\n                            \"«گلاس» gilās (کاربرد انگلیسی-هندی) ← فارسی «گیلاس»، با واکهٔ میانجی i که خوشهٔ آغازین gl- را \"\n                            \"می‌شکند، زیرا ساخت هجایی فارسی چنین خوشه‌ای را برنمی‌تابد. معین آن را چنین تعریف می‌کند: «ظرفی \"\n                            \"بلوری … جهت نوشیدن آب یا انواع مشروبات بکار رود؛ لیوان» و صورت glass را در برابرش می‌آورد. این \"\n                            \"واژه هم‌آوای «گیلاس ۲» (میوه) است که واژه‌ای جداگانه از یونانی κεράσι است، و نورایی به‌درستی با \"\n                            \"شمارهٔ مدخل معین آن دو را از هم جدا کرده است. ادعای نورایی درست است.\"),\n          \"sources\": [W_GILAS],\n          \"ref_check\": [\n            {\"ref\": \"MON:3513\", \"status\": \"supports\",\n             \"note\": (\"MON_part2.txt line 37501 (2-vol condensation of Mo'in's Farhang): «گیلاس: glass (اِ.) ظرفی بلوری به اشکال \"\n                      \"مختلف که جهت نوشیدن آب یا انواع مشروبات بکار رود؛ لیوان. خالی کردن گیلاس: به سر کشیدن …» — the entry \"\n                      \"carries the English etymon, exactly Nourai's arrow. Page 3513 belongs to the 6-vol edition, which is not \"\n                      \"on disk, so the page number itself could not be checked.\")}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part2.txt line 37501 s.v. گیلاس (the vessel)\", \"stance\": \"supports\",\n             \"note\": \"«گیلاس: glass (اِ.) ظرفی بلوری … لیوان»\"},\n            {\"src\": \"HJB\", \"where\": \"HJB.txt (Hobson-Jobson)\", \"stance\": \"silent\",\n             \"note\": \"no 'glass/gilas' headword found (only the string 'palagilass'); Yule & Burnell do not treat the word, though the Anglo-Indian usage it presupposes is well known\"},\n            {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_pages.txt\", \"stance\": \"silent\",\n             \"note\": \"grep 'گیلاس' returns nothing — Aryanpur's dictionary of inherited Indo-European Persian words has no entry, consistent with a recent European loan\"},\n            {\"src\": \"HRN\", \"where\": \"HRN.txt (Horn 1893)\", \"stance\": \"silent\",\n             \"note\": \"no گیلاس/gilās entry — expected, since the borrowing postdates Horn's Grundriss\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Gheled\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *ǵʰelh₂d- / *ǵʰeled- 'ice, hail' (Pokorny gheled- 435; Watkins gheled-)\",\n      \"note\": (\"Root, language label, gloss and page are all right: Pokorny p.435 has 'Root/lemma: gheled- / Meaning: ice', \"\n               \"and Watkins 'gheled-. Hail.' What Pokorny actually puts under it is New Persian žāla, Homeric Greek χάλαζα and \"\n               \"Old Church Slavic žlědica — i.e. the Persian word hangs directly on the root, not on a Sanskrit intermediary. \"\n               \"The one bad arrow on this chart is Sanskrit jaḍa → Persian žāleh, an etymology that Horn himself published in \"\n               \"KZ 32 and then explicitly withdrew in the Grundriss (no. 684); Mo'in kept it in his footnote to Borhan and in \"\n               \"the Farhang, and that is where Nourai got it.\"),\n      \"note_fa\": (\"ریشه، برچسب زبانی، معنا و شمارهٔ صفحه همه درست‌اند: پوکورنی در ص ۴۳۵ مدخل «gheled-، معنی: یخ» را دارد و \"\n                  \"واتکینز نیز «gheled-. تگرگ». آنچه پوکورنی زیر این ریشه می‌آورد عبارت است از فارسی نو žāla، یونانی هومری \"\n                  \"χάλαζα و اسلاوی کلیسایی کهن žlědica — یعنی واژهٔ فارسی مستقیماً به ریشه می‌پیوندد، نه از راه سنسکریت. \"\n                  \"تنها حلقهٔ نادرست این نمودار پیکان «سنسکریت jaḍa ← فارسی ژاله» است؛ هرن خود این ریشه‌شناسی را نخست در \"\n                  \"KZ ۳۲ آورده و سپس در «گروندریس» (شمارهٔ ۶۸۴) صریحاً پس گرفته است، ولی معین آن را در حاشیهٔ برهان و در \"\n                  \"فرهنگ فارسی نگاه داشته و نورایی از همان‌جا گرفته است.\"),\n      \"sources\": [W_ZALEH],\n      \"ref_check\": [\n        {\"ref\": \"POK:435\", \"status\": \"supports\", \"note\": POK435}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"p. 435, lemma gheled-\", \"stance\": \"supports\", \"note\": POK435},\n        {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. I p. 629f. (incoming/WLD/WLD_Bd1_pages.txt)\", \"stance\": \"supports\", \"note\": WLD_GHELAD},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gheled-\", \"stance\": \"supports\", \"note\": WAT_GHELED},\n        {\"src\": \"IEC\", \"where\": \"IEC.txt lines 4954, 5743\", \"stance\": \"partial\",\n         \"note\": \"Mann has no *gheled- lemma; he files Gk khalaza's semantic field under 'ghrōdos, io \\\"ice, hail, crust\\\"' (Skt. hrāduniḥ, OCS gradŭ, Lith. grúodas) and lists 'Per. cf. žale \\\"hail; dew\\\" (?)' with a question mark under 'gislos, is \\\"pebble, shingle\\\"' — a minority view that separates the Persian word from the Greek one\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"jada\",\n          \"verdict\": \"disputed\",\n          \"derivation\": (\"Sanskrit जड jaḍa is real, but it does not mean 'hail' and it is not from this root. Its senses are \"\n                         \"'cold, frigid; stiff, motionless, benumbed; dull, stupid' (whence Persian/Urdu usage and the \"\n                         \"philosophical term jaḍa 'inert matter'); the gloss 'hail' in the chart is imported from the root box, \"\n                         \"not from any Sanskrit lexicon. Pokorny's gheled- entry on p.435 cites only Npers. žala, Gk. χάλαζα \"\n                         \"and OCS žlědica — no Indic form at all; nor does Walde-Pokorny I 629f., nor Watkins. Modern opinion \"\n                         \"on jaḍa: Turner (CDIAL) calls it 'probably of substrate origin'; the only Indo-European proposal on \"\n                         \"offer connects it, via Fortunatov's law (*-ld- > -ḍ-), with PIE *gel-d- 'cold' (Pokorny 365f., \"\n                         \"Lat. gelidus, Eng. cold) — a plain velar *g-, therefore a different root from palatal *ǵʰel-h₂d-. \"\n                         \"Decisively, Horn (Grundriss no. 684) had himself derived žāla from 'skr. jaḍa- \\\"kalt, starr, \"\n                         \"regungslos\\\"' in KZ 32.588 and then wrote that Nöldeke's etymology 'verdient vor der meinigen … den \"\n                         \"Vorzug'. Nourai is repeating, at second hand through Mo'in, an etymology its own author abandoned in \"\n                         \"1893.\"),\n          \"derivation_fa\": (\"واژهٔ سنسکریت जड jaḍa وجود دارد، امّا نه معنای «تگرگ» می‌دهد و نه از این ریشه است. معنای آن «سرد؛ \"\n                            \"خشک و بی‌حرکت؛ کودن» است (و در فلسفه «مادّهٔ بی‌جان»)؛ معنی «تگرگ» در نمودار از خانهٔ ریشه به این \"\n                            \"گره سرایت کرده است. پوکورنی در ص ۴۳۵ زیر gheled- تنها فارسی نو žāla، یونانی χάλαζα و اسلاوی \"\n                            \"žlědica را می‌آورد و هیچ صورت هندی‌ای در کار نیست؛ والده-پوکورنی و واتکینز نیز همین‌گونه‌اند. \"\n                            \"دربارهٔ خودِ jaḍa: ترنر آن را «احتمالاً برگرفته از زیرلایهٔ غیرهندواروپایی» می‌داند و تنها پیشنهاد \"\n                            \"هندواروپایی، پیوند آن با *gel-d- «سرد» (لاتینی gelidus، انگلیسی cold) از راه قانون فورتوناتوف \"\n                            \"است — که ریشه‌ای دیگر با g کامی‌نشده است. از همه مهم‌تر: هرن خود در KZ ۳۲ ژاله را از jaḍa گرفته \"\n                            \"بود و سپس در «گروندریس» (شمارهٔ ۶۸۴) نوشت که ریشه‌شناسی نولدکه «بر ریشه‌شناسی من برتری دارد». پس \"\n                            \"این حلقه را پژوهش امروزی رد می‌کند.\"),\n          \"sources\": [W_JADA],\n          \"ref_check\": [\n            {\"ref\": \"POK:435\", \"status\": \"not_found\",\n             \"note\": (\"checked the full lemma on POK_full.txt: 'Root / lemma: gheled- / Meaning: ice / Material: Npers. žala \"\n                      \"(*zalda) \\\"hail, hoarfrost\\\"; gr. hom. χάλαζα \\\"hail\\\"; Old Church Slavic žlědica … Page(s): 435'. There \"\n                      \"is no Sanskrit jaḍa (or any Indic word) in Pokorny's entry, so the citation does not support the node.\")}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 435 s.v. gheled-\", \"stance\": \"contradicts\",\n             \"note\": \"the entry's whole material is 'Npers. žala (*zalda); gr. hom. χάλαζα; OCS žlědica' — no Indic reflex\"},\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. I p. 629 s.v. ghelad- „Eis“\", \"stance\": \"contradicts\",\n             \"note\": \"'ghelad- „Eis“. Horn, [ž]āla „Hagel“; aksl. žledica „gefrorener Regen“ …' — again no Sanskrit; and on the same page WP explicitly reject Skt. hlādate/hrada- as 'im Gutt. (gh-), Vokalismus … und in der Bed. unvereinbar'\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gheled-\", \"stance\": \"contradicts\",\n             \"note\": \"'gheled-. Hail. Zero-grade form *ghlēd- in Greek khalaza … CHALAZA, CHALAZION' — Greek only\"},\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 684, p. 152 (HRN.txt line 6032)\", \"stance\": \"contradicts\",\n             \"note\": \"'Diese Etymologie verdient vor der meinigen (KZ. 32, 588 No. 23) aus skr. jaḍa- \\\"kalt, starr, regungslos\\\" den Vorzug' — Horn withdraws the jaḍa etymology\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"žâleh «ژاله»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": (\"The word and its root assignment are right; only the drawn parent is wrong. NPers. ژاله žāla 'hail, \"\n                         \"hoarfrost, dew' is an inherited Iranian word, not a Sanskrit borrowing — Persian does not take \"\n                         \"everyday weather vocabulary from Sanskrit. Pokorny sets it up as *zalda- (i.e. Ir. *žalda- < \"\n                         \"*ǵʰl̥h₂d-o-), Horn as a New Persian ground-form *žrade / *žārde, Hübschmann as *žardak (with the \"\n                         \"regular Middle Persian -ak > NP -a and Persian ž- from earlier *ž/*žr-); the Afghan/Pashto žāla is \"\n                         \"either the cognate or a Persian loan (Hübschmann no. 684). Its exact Greek match is χάλαζα, and OCS \"\n                         \"žlědica outside Iranian. Nourai's own source chain is transparent: Mo'in's footnote to Borhan p.1057 \"\n                         \"reads 'در سانسکریت jaḍa (سرد، خشک و بی‌حرکت) … هوبشمان ژاله را از *žardak مأخوذ می‌داند', and the \"\n                         \"Farhang entry is tagged with the same Sanskrit gloss 'سرد و خشک'. So the chart is drawing an \"\n                         \"abandoned 19th-century etymology as if it were the route. Verdict: plausible — right root, wrong \"\n                         \"intermediate step.\"),\n          \"derivation_fa\": (\"خود واژه و انتساب آن به این ریشه درست است؛ تنها پیکانِ ورودی نادرست است. «ژاله» واژه‌ای است \"\n                            \"ایرانی و ارثی، نه وام‌واژه‌ای از سنسکریت — فارسی واژگان روزمرهٔ هواشناسی را از سنسکریت وام \"\n                            \"نمی‌گیرد. پوکورنی صورت پایه را *zalda- (ایرانی *žalda- از *ǵʰl̥h₂d-o-) می‌داند، هرن صورت آغازین \"\n                            \"فارسی نو را *žrade/*žārde می‌گیرد و هوبشمان *žardak را پیشنهاد می‌کند (با تبدیل معمول ‑ak فارسی \"\n                            \"میانه به ‑ه در فارسی نو). هم‌ارز دقیق آن در یونانی χάλαζα و بیرون از ایرانی، žlědica اسلاوی کهن \"\n                            \"است. سرچشمهٔ ادعای نورایی روشن است: حاشیهٔ معین بر برهان (ص ۱۰۵۷) می‌نویسد «در سانسکریت jaḍa \"\n                            \"(سرد، خشک و بی‌حرکت) … هوبشمان ژاله را از *žardak مأخوذ می‌داند» و مدخل فرهنگ فارسی نیز همان \"\n                            \"معنی «سرد و خشک» را در قلاب دارد. پس نمودار ریشه‌شناسی‌ای متروک از سدهٔ نوزدهم را بازمی‌گوید: \"\n                            \"ریشه درست، واسطه نادرست — با احتیاط پذیرفتنی.\"),\n          \"sources\": [W_ZALEH],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1057\", \"status\": \"supports\",\n             \"note\": (\"BQT_v2_pages.txt leaf 519 (printed p. ≈1057-1059), headword «ژاله = بروزن لاله. تگرگ را گویند … و شبنم \"\n                      \"را نیز گویند», with Mo'in's footnote 4: «در سانسکریت jaḍa (سرد، خشک و بی‌حرکت) … هوبشمان ژاله را از \"\n                      \"*žardak مأخوذ می‌داند. افغانی žāla \\\"هوبشمان\\\"». The reference does carry Nourai's Sanskrit claim (and, \"\n                      \"next to it, Hübschmann's Iranian one).\")},\n            {\"ref\": \"MON:1775\", \"status\": \"supports\",\n             \"note\": (\"MON_part1.txt line 73044 (2-vol condensation): «ژاله: [سرد و خشک] (اِ.) قطرهٔ … که روی برگ و گیاه نشیند؛ \"\n                      \"شبنم، تگرگ، باران» — the bracketed «سرد و خشک» is Mo'in's gloss of the Sanskrit etymon jaḍa, i.e. exactly \"\n                      \"Nourai's node-1 gloss. Page 1775 belongs to the 6-vol edition, not on disk.\")},\n            {\"ref\": \"FSF:216\", \"status\": \"supports\",\n             \"note\": (\"FSF_pages.txt leaf 288 (Noushin, Vazhe-namak): «ژاله ۱- تگرگ: تو گفتی هوا ژاله بارد همی …؛ ۲- شبنم: \"\n                      \"به چشم اندرون آب چون ژاله گشت» — confirms both glosses and the Ferdowsi shāhed the chart quotes. The \"\n                      \"printed page number is not legible in the OCR of this scan, so 216 itself is unverified.\")}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 435 s.v. gheled-\", \"stance\": \"supports\",\n             \"note\": \"'Npers. žala (*zalda) \\\"hail, hoarfrost\\\"' — entered directly under the root, with no Sanskrit link\"},\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 684, p. 152\", \"stance\": \"partial\",\n             \"note\": \"'žāla \\\"Hagel, Reif\\\". [Skr.] hrāduni- \\\"Hagel\\\"; gr. χάλαζα; lat. grando; ksl. gradŭ. Nöldeke (mündliche Mitteilung). Neupersische Grundform *žrade, *žārde. Diese Etymologie verdient vor der meinigen … aus skr. jaḍa- … den Vorzug.'\"},\n            {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien no. 684 (HUB.txt line 2518) and p. ~119 (line 4619)\", \"stance\": \"partial\",\n             \"note\": \"'Ist np. žāla aus *žrdak (wie ich ansetzen würde) entstanden, müsste sowohl afgh. žāla \\\"Hagel\\\" wie žalai pers. LW. sein'; 'žāla \\\"Hagel, Reif\\\" aus *žardak (vgl. Horn Nr. 684)?'\"},\n            {\"src\": \"BQT\", \"where\": \"BQT_v2_pages.txt leaf 519 (printed ≈1057)\", \"stance\": \"partial\",\n             \"note\": \"Mo'in's footnote gives both the Sanskrit jaḍa comparison and Hübschmann's *žardak\"},\n            {\"src\": \"FSF\", \"where\": \"FSF_pages.txt leaf 288\", \"stance\": \"supports\",\n             \"note\": \"«ژاله ۱- تگرگ … ۲- شبنم» with the Ferdowsi verse — gloss only, no etymology\"},\n            {\"src\": \"IEC\", \"where\": \"IEC.txt line 5743\", \"stance\": \"contradicts\",\n             \"note\": \"Mann puts 'Per. cf. žale \\\"hail; dew\\\" (?)' under 'gislos … pebble, shingle' beside OHG kisil, i.e. away from khalaza — a minority view, and even he flags it with '(?)'\"},\n            {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_pages.txt\", \"stance\": \"silent\",\n             \"note\": \"no ژاله headword; the two hits are 'ژاله' used as a Persian gloss inside other entries\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Greek\",\n          \"words\": \"xalaza\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": (\"Homeric Gk. χάλαζα khalaza 'hailstone' goes back to *khalad-ya, the zero-grade *ǵʰl̥h₂d- of the root \"\n                         \"plus the feminine -ya suffix, with the regular Greek treatment -dy- > -ζ-. The extended senses the \"\n                         \"chart records are Greek medical usage: from 'hailstone' to any hard round lump, hence a small tubercle \"\n                         \"or cyst (Hippocratic and later medical writers), which is what makes the diminutive available for the \"\n                         \"eyelid cyst. Klein: 'Gk. χάλαζα, \\\"hail, hailstone, lump\\\", which stands for *χαλαδ-ya and is cogn. \"\n                         \"with OSlav. žlědica, \\\"frozen rain\\\"'.\"),\n          \"derivation_fa\": (\"یونانی هومری χάλαζα «دانهٔ تگرگ» از *khalad-ya است، یعنی درجهٔ صفر ریشه (*ǵʰl̥h₂d-) به‌علاوهٔ \"\n                            \"پسوند مؤنث ‑ya، با تحول آوایی همیشگی یونانی ‑dy‑ > ‑ζ‑. معناهای گسترده‌ای که نمودار می‌آورد \"\n                            \"(هر تودهٔ گِرد و سفت، و از آنجا کیست و غدّه) کاربرد پزشکی یونانی است و همان است که ساخت مصغّر آن \"\n                            \"را برای کیست پلک ممکن کرده است. کلاین: «χάλαζα از *χαλαδ-ya و هم‌ریشه با žlědica اسلاوی کهن». \"\n                            \"ادعای نورایی درست است.\"),\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": WAT_GHELED}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gheled-\", \"stance\": \"supports\", \"note\": WAT_GHELED},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 7123 s.v. 'chalaza'\", \"stance\": \"supports\",\n             \"note\": \"'ModL., fr. Gk. χάλαζα, \\\"hail, hailstone, lump\\\", which stands for *χαλαδ-ya and is cogn. with OSlav. žlědica, \\\"frozen rain\\\". Cp. next word. Cp. also chabazite.'\"},\n            {\"src\": \"POK\", \"where\": \"p. 435 s.v. gheled-\", \"stance\": \"supports\",\n             \"note\": \"'gr. hom. χάλαζα \\\"hail\\\"'\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"chalazion : an eyelid tumor\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": (\"chalazion is Medical Latin, borrowed from Gk. χαλάζιον khalazion, the diminutive of χάλαζα — \"\n                         \"literally 'little hailstone', a very exact description of the small firm nodule left in the eyelid by \"\n                         \"a blocked meibomian gland. English took it from the medical Latin of the anatomical tradition; the \"\n                         \"plural chalazia is still the Greek one. The sibling term chalaza (the albuminous cord in an egg, and \"\n                         \"the ovule scar in botany) is the simplex of the same word.\"),\n          \"derivation_fa\": (\"chalazion از لاتینی پزشکی است و آن نیز از یونانی χαλάζιον، مصغّر χάλαζα، یعنی «تگرگِ کوچک» — \"\n                            \"توصیفی بسیار دقیق از گرهک سفتی که بر اثر گرفتگی غدّهٔ میبومینِ پلک پدید می‌آید. انگلیسی آن را از \"\n                            \"لاتینی پزشکیِ سنّت تشریح گرفته و جمع یونانی chalazia هنوز به کار می‌رود. ادعای نورایی درست است.\"),\n          \"sources\": [],\n          \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the chart gives no reference for this node\"}],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 7124 s.v. 'chalazion'\", \"stance\": \"supports\",\n             \"note\": \"'chalazion, n., a small tumor in the eyelid (med.) — Medical L., fr. Gk. χαλάζιον, dimin. of χάλαζα, \\\"hail; pimple, small tubercle\\\". See chalaza.'\"},\n            {\"src\": \"FSD\", \"where\": \"FSD_vol1.txt line 62155 (Funk & Wagnalls)\", \"stance\": \"supports\",\n             \"note\": \"'especially one on the eyelid; a sty. [< Gr. chalazion, dim. of chalaza, pimple.]'\"},\n            {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt lines 30427, 30531ff.\", \"stance\": \"supports\",\n             \"note\": \"Webster has chalaza and its derivatives, and s.v. chabazite: '[Fr. chabazie, missp. of Gr. chalazie … chalaza, hailstone]'\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n\nwith open('/home/sfmqrb/git/rishe/data/verification/page-186.json', 'w', encoding='utf-8') as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\n"
}
```


### [2026-09-06T02:30:36.170Z] TOOL RESULT

```
The file /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build186.py has been updated successfully. (file state is current in your context — no need to Read it back)
```


## [2026-09-06T02:30:40.662Z] TOOL CALL #69: Bash

```json
{
 "command": "python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build186.py && python3 -m json.tool data/verification/page-186.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 186",
 "description": "Build and validate page-186.json"
}
```


### [2026-09-06T02:30:46.283Z] TOOL RESULT

```
written
JSON OK
nodes verified: 18/18
node verdicts: {'plausible': 3, 'confirmed': 13, 'disputed': 2}
root verdicts: {'confirmed': 2}
ref checks: {'partial': 3, 'not_checked': 8, 'supports': 10, 'not_found': 1}
books consulted: {'supports': 34, 'silent': 12, 'partial': 6, 'contradicts': 6} | by book: {'KLN': 12, 'SKT': 7, 'POK': 6, 'ARY': 5, 'AHD': 5, 'MON': 4, 'BQT': 4, 'HRN': 3, 'PLA': 2, 'LAT': 1, 'AFM': 1, 'FVQ': 1, 'HJB': 1, 'WLD': 1, 'HUB': 1, 'FSF': 1, 'IEC': 1, 'FSD': 1, 'WEB': 1}
```


## [2026-09-06T02:31:07.444Z] AGENT

Done. `data/verification/page-186.json` written; `verify_check.py 186` reports 18/18 nodes, 0 PROBLEM lines.

**Page 186 (book p. 156) — 2 entries, 18 nodes**
- Roots: 2 confirmed (Ghel = Pokorny 429 ĝhel-1 / Watkins ghel-2; Gheled = Pokorny 435 "ice", Watkins "hail").
- Nodes: 13 confirmed, 3 plausible, 2 disputed, 0 unverified, 0 transcription_suspect.
- Ref checks: 10 supports, 3 partial, 1 not_found, 8 not_checked (all of the latter are nodes the chart gives no reference for, plus FVF:223 which has no accessible copy).

**Disputed**
- *Ghel #8, Arabic xîyâl* — Nourai's NOTE ("Arabic خيال is a distorted Persian خولیا") is taken verbatim from Addi Shir p.59 ("الظن والوهم مثل خوليا لفظاً ومعنى"), but خيال is built on the productive Semitic root خ-ي-ل (خال/تخيّل/خُيَلاء, and طيف الخيال in pre-Islamic poetry); Asbaghi's *Persische Lehnwörter im Arabischen* does not list it. Chance resemblance.
- *Gheled #1, Sanskrit jada* — jaḍa means "cold, stiff, dull", not "hail"; absent from Pokorny 435, Walde-Pokorny I 629 and Watkins. Turner: probably substrate; the only IE proposal links it to *gel-d- "cold" (a different root). Horn himself withdrew the jaḍa etymology of ژاله in Grundriss no. 684.

**Plausible (route errors, right ultimate origin)**
- *#1 Greek xlôros-phullon* — khlōros is genuine, but *χλωρόφυλλον is not an ancient Greek word; chlorophylle was coined in French in 1818.
- *#7 Persian مالیخولیا* — Greek μελαγχολία is right, but the transmission was Greek → Syriac → Arabic مالنخوليا → Persian, not via Latin (Mo'in, BQT p.1947, calls the Persian form a مصحّف of مالنخولیا; BQT p.795 s.v. خولیا: "از یونانی χολή است بمعنی صفرا").
- *Gheled #2 Persian ژاله* — the word does belong to the root (Pokorny 435 lists Npers. žāla directly), but as inherited Iranian *žalda-/*žardak, not as a Sanskrit loan.

**Extraction errors:** none found — the JSON matches the chart text at every node, so no page image was rendered.

Eight web pages archived via `fetch_source.py` (Wiktionary خیال/خيال/ژاله/گیلاس/مالیخولیا/जड, Etymonline melancholy/chlorophyll).
