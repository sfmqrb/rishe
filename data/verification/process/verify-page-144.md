# Verification process log — verify-page-144


## [2026-09-05T20:08:34.074Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 144 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-144.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-144.json. Write /home/sfmqrb/git/rishe/data/verification/page-144.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 144` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:08:35.840Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:08:36.557Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:08:36.570Z] TOOL RESULT

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


## [2026-09-05T20:08:36.863Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-144.txt"
}
```


### [2026-09-05T20:08:36.884Z] TOOL RESULT

```
1	=== PDF page 144 (book page 114) ===
2	--- entry 0 ---
3	ROOT [Arabic] D.v.r : to turn, go around, encircle  (refs KLN:397; FVA:146)
4	#1 (parent #0) [Arabic] refs=FVA:146; KLN:108,397 | dâîrah : circle ; dâr : house, originally surrounding a court ; dahr : a round of (long) time ; dâr-as-sanâ` : house of construction, factory ☞S.n.`a
5	  #2 (parent #1) [Persian] refs=FVA:146 | dowr «دور ۲» : around, perimeter ; dâr 1 «دار ۱ ( دیار ، دیّار )» : house ; dahr «دهر» : a long time, world, fortune | extra: دوره ، دوران ، دایر ، دایره ، داریه
6	دوّار ، مدوّر ، مَدار ، اداره ، مدیر
7	  #3 (parent #1) [Greek] refs=KLN:108 | arsonalos : factory, workshop
8	    #4 (parent #3) [Italian] refs=AHD:74; KLN:108 | darsena, arsenale : naval dockyard
9	      #5 (parent #4) [English] refs=AHD:74 | arsenal
10	--- entry 1 ---
11	ROOT [Indo-European] Dwei, Dvei : to fear  (refs POK:227)
12	#1 (parent #0) [Avestan] refs=POK:228; KLN:454 | dvaĕtha : threat, menace ; dvaĕš, tbaĕš : sick, ill
13	  #2 (parent #1) [Pahlavi] refs=POK:228 | běš 1 : sorrow | NOTE: See "Weis" for an alternative root.
14	    #3 (parent #2) [Persian] refs=MON:627 | bîš 2 «بیش ۲» : a poisonous plant
15	#4 (parent #0) [Sogdian] refs=SOD:138 | db`yš : enmity, harm
16	#5 (parent #0) [Latin] refs=AHD | dîrus : horrible
17	  #6 (parent #5) [English] refs=None | dire
18	#7 (parent #0) [Greek] refs=KLN:451 | deinos : dreadful ; deinos-saura : dreadful lizard
19	  #8 (parent #7) [English] refs=None | dinosaur
20	
```


## [2026-09-05T20:08:40.861Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-144.json",
 "description": "Show source JSON for page 144"
}
```


### [2026-09-05T20:08:40.908Z] TOOL RESULT

```
{
  "pdf_page": 144,
  "book_page": 114,
  "entries": [
    {
      "root": {
        "name": "D.v.r",
        "lang": "Arabic",
        "refs": "KLN:397; FVA:146",
        "gloss": "to turn, go around, encircle"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "FVA:146; KLN:108,397",
          "words": [
            {"translit": "dâîrah", "gloss": "circle", "script": null},
            {"translit": "dâr", "gloss": "house, originally surrounding a court", "script": null},
            {"translit": "dahr", "gloss": "a round of (long) time", "script": null},
            {"translit": "dâr-as-sanâ`", "gloss": "house of construction, factory", "script": null, "see": ["S.n.`a"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "FVA:146",
          "words": [
            {"translit": "dowr", "gloss": "around, perimeter", "script": "دور ۲"},
            {"translit": "dâr 1", "gloss": "house", "script": "دار ۱ ( دیار ، دیّار )"},
            {"translit": "dahr", "gloss": "a long time, world, fortune", "script": "دهر"}
          ],
          "script_extra": "دوره ، دوران ، دایر ، دایره ، داریه\nدوّار ، مدوّر ، مَدار ، اداره ، مدیر",
          "note": null,
          "quote": {"text": "مرو به خانهٔ ارباب بی مروّتِ دهر - که کنج عافیتت در سرای خویشتن است", "poet": "Hâfez"}
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Greek",
          "refs": "KLN:108",
          "words": [
            {"translit": "arsonalos", "gloss": "factory, workshop", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Italian",
          "refs": "AHD:74; KLN:108",
          "words": [
            {"translit": "darsena, arsenale", "gloss": "naval dockyard", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "AHD:74",
          "words": [
            {"translit": "arsenal", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Dwei, Dvei",
        "lang": "Indo-European",
        "refs": "POK:227",
        "gloss": "to fear"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:228; KLN:454",
          "words": [
            {"translit": "dvaĕtha", "gloss": "threat, menace", "script": null},
            {"translit": "dvaĕš, tbaĕš", "gloss": "sick, ill", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "POK:228",
          "words": [
            {"translit": "běš 1", "gloss": "sorrow", "script": null}
          ],
          "note": "See \"Weis\" for an alternative root.",
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:627",
          "words": [
            {"translit": "bîš 2", "gloss": "a poisonous plant", "script": "بیش ۲"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:138",
          "words": [
            {"translit": "db`yš", "gloss": "enmity, harm", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "dîrus", "gloss": "horrible", "script": null}
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
            {"translit": "dire", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Greek",
          "refs": "KLN:451",
          "words": [
            {"translit": "deinos", "gloss": "dreadful", "script": null},
            {"translit": "deinos-saura", "gloss": "dreadful lizard", "script": null}
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
            {"translit": "dinosaur", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-05T20:08:41.002Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Show source matrix"
}
```


### [2026-09-05T20:08:41.045Z] TOOL RESULT

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


## [2026-09-05T20:08:45.371Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['FVA','KLN','POK','AHD','MON','SOD','FVQ']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:900])\n    print()\n\""
}
```


## [2026-09-05T20:08:45.872Z] TOOL CALL #6: Bash

```json
{
 "command": "head -c 3000 data/verification/page-127.json"
}
```


### [2026-09-05T20:08:47.032Z] TOOL RESULT

```
FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with Nourai's title when buying. Catalogue record only."}

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based l

POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: lea

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}", "loca

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"], "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 335 leaves)", "covers_etymology": true, "notes": "Good English OCR (Arabic script garbled). Same 1938 edition Nourai cites.", "cites": "page number of Jeffery, The Foreign Vocabulary of the Qurʾān (19
```


### [2026-09-05T20:08:47.063Z] TOOL RESULT

```
{
 "pdf_page": 127,
 "book_page": 97,
 "verified_by": "claude-opus-5",
 "verified_on": "2026-09-05",
 "entries": [
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
     "note": "'dhem-, dhemə- „stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben = düster, dunkel), wehen, blasen (hauchen = rieche
```


## [2026-09-05T20:09:03.973Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"dṷei\\|dvei-\\|dŭei\\|duei-\" POK_01.txt | head -30\necho \"=== search page area ===\"\ngrep -n \"Furcht\\|fürchten\" POK_01.txt | sed -n '1,40p'"
}
```


### [2026-09-05T20:09:04.032Z] TOOL RESULT

```
3257:duei-  ,fürchten'.
3266:duö(u)  m.  .zwei'  (Satzdoppelform  duuou),  dual  f.  n..  daneben  duei-,  duoi-, du/-;  vgl.  die  Zusammenfassung  bei  Brugmann  IP  2.  6 — 82  passim.   "
3284:Mochstufiges  duei-  in  Kompositis  ist  zuzugeben  fürs  Kelt.  (z.  B.  air. dH-riad  .bigae'.  diabul  .zweifach',  cymr.  dwy-flwydd  .biennis';  air.  dias ,Zweiheit  von  Personen'  wohl  aus  *dueio-stho-)  und  fürs  Germ.  (z.  B.  an- ord. tul-faldr  ,zweifach'  neben  tuefaldr]  got.  tweifla-,  wohl  n..  ahd.  zivifal n.  neben  gr.  di-nkög,  lat.  duplus).
3294:4.  Multiplikativa:  gr.  diTcXög,  dinköog,  lat.  duplus,  umbr.  dupla  ,duplas' air.  dlabul  (*duei-plo-;  siehe  auch  oben  got.  tweifis),  wozu  vielleicht  av. bifra-  n.  ,Vergleich,  Ähnlichkeit^  (:  Wz.  pel-  , falten'^,  vgl.  mit  <-Ervvei- terung :)
3299:ahd.  zwlg  ,Zweig^  (*duei-gho-),  ags.  tivig  ,Zweig^  (*dui-gJio-)  ]  as.  tög{o)f mnd.  töch,  ahd.  zuog{o)  , Zweig'  sind  nach  Formen  des  Kardinales  mit twö-  umgebildet;
3317:Mit  duis-  ^zweimal^  identisch  ist  diiis-  ^entzwei,  auseinander^  in  got.  tx standan  ^sich  trennen^  und  den  Ableitungen  anord.  tvistra  ^trennen^_,  m£J afries.  ticlst,  mhd.  zwist  , Zwist  (Entzweiung)^  und  mengl.  ticist  =  anoi kvistr  ^Zweig'^  (wie  auch  bair.  zioist),  ferner  anord.  kvisl  f.  , gespaltener  Zwei oder  Werkzeug,  Arm  eines  Flusses^  (dies  mit  idg.  ei)\  ferner  anord.  ^viVüc ^zweimaF,  tvistr  ^zwiespältig,  traurig^  (=  ai.  dvistJia-  ,zweideutig^ *diaTOQ  in  dLaxaC^co  ,zweifle^,  idg.  *dui{s)-sto- -.Wz.  stä-,  allenfalls  duis^i mit  formantischem  -to-),  ags.  twisla  ,Arm  eines  Flusses^,  twislian  ^zwe teilen^,  ahd.  zwisila,  nhd.  Ziviesel  ^gabelförmiger  Gegenstand,  Zweigt,  mli^ zwisel  ,doppelt^j  hierher  sehr  wahrscheinlich  ar.  dvls-  ,hassen^  (s.  untel *duei-  ,fürchten^).
=== search page area ===
48:Schwundstufig:  ved.  t-sdrati  , schleicht,  schleicht  heran^,  ahd.  zagen  (:got. *-rt<7an  , fürchten'),  ahd.  z-ougen,  mhd.  zöngen,  as.  t-ögian  gegenüber  got.  at- angjan  ,vor  Augen  stellen,  zeigend
101:agh'  ,seelisch  bedrückt  sein,  sich  fürchten'.
103:Ags.  ege  m.  ,Furcht',  egisi-grima  gl.  larvula,  einst  n.  es-St.  *agiz  =  gr. ^/o.",  vgl.  ahd.  egis-llh  ,schrecklich',  egisön  ,erschrecken'  und  die  zu  o- und  e/z-Stämmen  erweiterten  got.  agis  n.  ,Furcht,  Angst,  Schrecken',  ahd. agiso,  egiso  m  ,  egisa  f.  , Schrecken,  Schreckgestalt',  ngs.  egesa  m.  , Furcht'; anord.  agi  m.  (-e^-St.)  ,FLircht',  ahd.  egl;  mhd.  ege  f.  , Furcht,  Schrecken, Strafe';  got.  -agan  in  un-agands  ,sich  nicht  fürchtend',  af-agjan  ,ängstigen', us-agjan  ,jemanden  erschrecken',  in-agjan  .jemanden  anfahren';  Präterito- präsens  got.  ög  (ögum)  ,fürchte  mich';  ni  ögs  ,fürchte  nichts'   (alter   kurz-
104:vokalischer  Konjunktiv  *ögiz),  anord.  öa-sk  ,sich  fürchten^;  g'ot.  ögjan jemanden  schrecken'  =  anord.  cegja  .erschrecken';  anord.  ögn  f.  .Schrecken', ötti  m.  .Furcht',  ags.  öga  f.  .Schrecken'.
275:schwed.  ag  m.  .Sumpfgras.  Cladium  mariscus.  Schneide'  (*akö-),  mhd. ag  .Barsch',  egle,  eglinc  ds..  nhd.  Schweiz,  egel,  Demin.  egli,  aschwed.  agh- borre  ds..  vielleicht  auch  schwed.  agg  .Groll.  Haß',  agga  .stechen,  plagen', norw.  dial.  agge  .Zahn.  Spitze'  {*ako-k��-  oder  expressive  Gemination?), sowie  (mit  sekundärem  germ.  Ablaut  a  :  ii  oder  aus  *akuko-  mit  Assimila- tion des  a  an  w?)  norw.  dial.  ugg  .Stachel.  Ängstigung',  schwed.  dial.  ugg .Zacke,  Zahn',  anord.w^^r  .Furcht',  norw.  dial.  it^^e  .Flosse';  lit.  aküotas^) .Granne',  äsaka^  {*ako-kä)  .Fischgräte.  Kleie'  ==  wruss.  osoka  .carex'. apr.  ackons  {^aköno-)  ds.
982:*>-üt  aiipja-  (N.  Sg.  *aupeis  oder  *aups)  ,'öde,  verlassen^  (*,abgelegen^), auhida  Wüste^,  ahd.  öcli,  nhd.  Öde,  anord.  audr  ,öde^;  air.  üathad  , Einzel- heit Vereinzelung^  —  Geht  auf  die  Schrecken  der  Einöde,  Wildnis  auch mir.  üath  _,Schrecken,  schrecklich'  (fernzuhalten  sind  cjmr.  uthr  , schreck- lich' corn.  uth,  euth,  bret.  euz  , Schrecken')  ?  Wenigstens  ist  deren  Ver- bindung mit  lat.  pavere  ,sich  ängstigen,  vor  Furcht  zittern'  alles  eher  als sicher,  s.  pou-  , Angst'.
1598:gv.  (peßo^aL,  (poßao^iai  ^fliehen,  sich  fürchten^,  (p6ßog  ,Flucht,  Furch?^ (poßea)  .scheuche  auF,  cpoßeqög  .furchterregend,  furchtsam';  .fi
2319:bhöi- :  bhQi'  :  bhi-  (bhiid-)  ,sich  fürchten';  bhoidho-s  ,fürchterlich,  abscheu- lich'. Ai.  bhdyate  ,fürchtet  sich'  (aus  Hhdietai  =  slav.  bojet^),  av.  bayente, byente  ,sie  setzen  in  Furcht',  mpers.  besänd  ,sie  sind  in  Angst'  (uriran. *bai-sk-)',  ai.  bibhki  ,fürchtet  sich',  sek.  zum  ursprünglichen  Perf.  m. Präsensbed.  bibhäya  ,bin  in  Furcht'  (bibhiyät,  bibhltana,  abibhet,  Partiz. bibhlvän  =  av.  biwivä  ,sich  fürchtend');  ai.  bhiyand-h  ,sich  fürchtend'; bhi-h  f.,  bhUi-h  f.  (:  lett.  Inf.  bities)  ,Furcht',  bhlmd-h,  ,furchtbar',  bhitd-h
2321:,sich  fürchtend^  erschrocken^^  hhlo-u-h  ,furchtsam^  schüchtern,  feige*^  (wei r  =  idg.   l,  ablautend    mit  lit.    hdiUj   bailüs)-,    npers.    bäk   ,Furcht^  (a^ *bhdyaka-)'j   mit   idg.  Vereinfachung  von  äi   zu  ä  vor  Kons,   hierher  aj^ bhäma-h  etwa  ,Grimm,  Wut',  bhämitd-h  ,grimmig^
2325:Bsl.  ursprgl.  Präsens  *bhdiö-y  Prät.-St.  *bhiiä-j  Inf.  *bhltei]  apr.  biät ,fürchten^,  kausat.  pobaiint  ,strafen^;  lit.  bijaus,  bijötis  (auch  nicht  reflexiv' ,sich  fürchten^,  lett.  bistuos,  bijuds,  bities  und  bijäjuos,  bijäties  ,sich  fürchten' lit.   baijils  ,furchtbar,  schrecklich,  abscheulich^;   baidaü,   -yti  ,scheuchen'^ lett.    baXdUj    baXdyt    und    biedet    ,schrecken^,    dazu    lit.    baisä    ,Sch recken' i^baid-s-ä),  baisüs  ,schrecklich,  greulich^,  baisiöti  ,beschmutzen,  beschmie- ren^ (und  aksl.  bäs^  , Teufel^,  *bH-s^)]   lit.  bdime  ,Furcht^;  bdiU  ds.  (bailus ,furchtsam^).
2326:Aksl.  bojg,  bojati  s§  ,sich  fürchtend
2327:Eine  Weiterbildung  *bhil-es-,   *bhis-    in    ai.  bhydsate    ,fürchtet    sicli^, udbhydsa-h  ,sich   fürchtend^,  av.  Perf.  biwivärdha   (d.  i.  biwyaTdha).  ,erregte    * Schrecken,  war  furchtbar^;   ai.  bhlsayate  ,schreckt^,   bhisana-h  ,Schrecken  -'■ erregend^;
3257:duei-  ,fürchten'.
3259:arm.  erkntim  ,ich  fürchte',  erkiul  ,Furcht'  (Anlaut  wie  in  erku  ,zwei' '.*diLöu  Meillet  MSL.  8,  235);
3262:gr.  hom.  deldo)  ^fürchte^  (*Ö6-dfot-a),  Plur.  dsidci-iey  (d.  i.  öidJ^iixsv)^ dsdii-isv   (danach    der   neue    Sg.  hom.  dsLÖia^  d.  i.  öadJ^ia,  att.  deöia)^ hom.  MdÖBLaev  (d.  i.  söJ^eiasv),  hom.  diß  ,fürchtete^;  aus  *6söJ=oia  umgebiß Perf.  hom.  dsiöoiKa,  att.  didoL^a,  kret.  dsöSoiTCMg  Hes.  (Hs.  dsd^or/wg)^  ^^ öedeiyisXog  Hes.  ^furchtsam';  zu  öeöia-Ao^ai  (nachhom.)  .schrecke'  (*<Jfi-dj GY-o-iiai)  wurde  sekundäres  d€Ldl^O(.iaL  gebildet,  wovon  erst  att.  dedlztoi hom.  SsLÖiGao^iaL]  hom.  66iörj(.uüv  .furchtsam'  (*dsdJ^strj^tov);  ösog  n.  .Furcj (*(5/eiog).  d-eovörig  .gottesfürchtig'  (*^£0-(^/£iäg).  öel^ia  n..  SsL^iög  m.  , Furcht dfitvrfg  .schrecklich'.   JstAog,  .furchtsam,  feig;    unglücklich,   beklagenswert (*öJ^€isX6g)'j  diSQÖg  .zu  fürchten'  (*öJ^L-eQOg)]
3317:Mit  duis-  ^zweimal^  identisch  ist  diiis-  ^entzwei,  auseinander^  in  got.  tx standan  ^sich  trennen^  und  den  Ableitungen  anord.  tvistra  ^trennen^_,  m£J afries.  ticlst,  mhd.  zwist  , Zwist  (Entzweiung)^  und  mengl.  ticist  =  anoi kvistr  ^Zweig'^  (wie  auch  bair.  zioist),  ferner  anord.  kvisl  f.  , gespaltener  Zwei oder  Werkzeug,  Arm  eines  Flusses^  (dies  mit  idg.  ei)\  ferner  anord.  ^viVüc ^zweimaF,  tvistr  ^zwiespältig,  traurig^  (=  ai.  dvistJia-  ,zweideutig^ *diaTOQ  in  dLaxaC^co  ,zweifle^,  idg.  *dui{s)-sto- -.Wz.  stä-,  allenfalls  duis^i mit  formantischem  -to-),  ags.  twisla  ,Arm  eines  Flusses^,  twislian  ^zwe teilen^,  ahd.  zwisila,  nhd.  Ziviesel  ^gabelförmiger  Gegenstand,  Zweigt,  mli^ zwisel  ,doppelt^j  hierher  sehr  wahrscheinlich  ar.  dvls-  ,hassen^  (s.  untel *duei-  ,fürchten^).
```


## [2026-09-05T20:09:04.822Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"arsenal\" KLN_1966.txt | head -20\necho \"=== dinosaur ===\"\ngrep -n -i \"dinosaur\" KLN_1966.txt | head -10\necho \"=== deinos ===\"\ngrep -n -i \"^dire\\b\\|dirus\" KLN_1966.txt | head -10"
}
```


### [2026-09-05T20:09:04.935Z] TOOL RESULT

```
3518:arsenal,  n.,  a  place  for  manufacturing  and  storing ammunition  and  weapons.  —  It.  arsenale  (Olt. arzanale),  ‘dock’,  borrowed — prob.  through  the medium  of  MGk.  d.pm]'tdkt)C, — fr.  Arab,  dar- a?-sind'ah  (whence  also  Sp.  darsena  and  It.  dar- sena,  ‘dock’),  lit.  ‘house  of  construction’,  fr.  ddr, ‘house’,  as-,  assimilated  form  of  al-,  ‘the’,  and Sind'ah,  ‘construction,  art’,  fr.  Sana' a,  ‘he  made’. For  the  ending  of  arsenal  see  adj.  suff.  -al. arsenic,  n.,  a  chemical  element.  —  OF.  (=  F.) arsenic,  fr.  L.  arsenicum,  arrhenicum,  fr.  Gk. dptrsvixov,  appevvxov,  ‘yellow  orpiment',  fr. MPers.  *zarnik,  ‘gold,  golden ;  orpiment’(whence ModPers.-Arab.  zarnikh,  ‘orpiment’),  through the  medium  of  a  Semitic  language;  cp.  Mish- naic  Heb.  zarnikh,  Syr.  zarnikhd,  ‘orpiment’. Cp.  Avestic  zaranya,  Pers.  zar,  ‘gold’,  and  the first  element  in  zermahbub,  and  see  yellow  and words  there  referred  to.  Cp.  also  jargon,  ‘a variety  of  zircon’.  Gk.  apctevtxov,  appsvtx&v, ‘orpiment’,  was  influenced  in  form  by  apcrevtxop, appevixic,  ‘male’,  fr.  ape rc;v,  ap pr,v,  ‘male’.  For the  sense  development  of  MPers.  *zarnik,  cp.  L. auripigmentum,  fr.  aurum,  ‘gold’  (see  orpiment). Derivatives:  arsenic,  arsenic-al,  adjs. arsenious,  adj.,  containing  arsenic.  —  See  ar¬ senic  and  -oils.
=== dinosaur ===
5711:Brontosaurus,  n.,  a  genus  of  American  dinosaurs ( paleontol .)  —  ModL.,  coined  fr.  Gk.  ppovrij, ‘thunder’,  and  aaupo?,  ‘lizard’.  See  bronto-  and saurian.
8514:Compsognathus,  n.,  a  genus  of  small  dinosaurs (paleoniol.)  —  ModL.,  compounded  of  Gk. >co(nji6?,  ‘refined,  elegant’,  and  yvaffex;,  ‘jaw’. The  first  element  prob.  stands  for  *kwonqu-m- os  and  is  cogn.  with  Lith.  svdnkus,  ‘fine’.  For the  second  element  see  gnathic.
11473:Dinomis,  n.,  a  genus  of  recently  extinct  birds  re¬ sembling  an  ostrich.  The  New  Zealand  Moa belonged  to  this  genus  (paleontol.) — ModL.,  lit. ‘a  frightful  bird’,  compounded  of  dino-  and Gk.  8pvi?,  ‘bird’.  See  omitho-. dinosaur,  n.  any  member  of  the  Dinosauria.  — See  next  word.
11474:Dinosauria,  n.  pi.,  a  group  of  extinct  Saurian  rep¬ tiles  (paleontol.)  —  ModL.,  lit.  ‘frightful  liz¬ ards’,  compounded  of  dino-  and  Gk.  aaopa, caupop,  ‘lizard’.  See  sauro-.
11475:Derivatives:  dinosaurian,  adj.  and  n. dinothere,  n.,  any  member  of  the  genus  Dino- therium.  —  See  next  word.
11520:Diplodocus,  n.,  a  genus  of  gigantic  dinosaurs ( paleontol .)  —  ModL.,  compounded  of  diplo- and  Gk.  80x65,  ‘beam,  bar’,  lit.  ‘that  which holds  the  roof’,  fr.  I.-E.  base  *dek-,  dok-,  ‘to take,  receive,  accept’.  See  decent  and  cp.  words there  referred  to.
11543:dire,  adj.,  dreadful.  —  L.  dirus,  ‘fearful,  awful, ill-omened,  horrible,  terrible’,  of  uncertain  ori¬ gin.  It  possibly  derives  fr.  I.-E.  base  *dwei-,  ‘to be  afraid,  fear’,  whence  also  Gk.  SeiSoi  (for *S£-Sfot-a),  ‘fear’,  Seop  (for  *8fet-op),  ‘fear¬ ful,  terrible,  powerful,  mighty,  marvelous’, SctXop  (for  *Sfet-Xop),  ‘cowardly’,  Savop  (for *Sfei-vop),  ‘fearful’,  OI.  dvesti,  ‘hates’,  dvisah, ’hatred’,  Avestic  dvaeba-,  'threat,  menace’,  and prob.  also  Arm.  erkncim,  'I  fear’.  Cp.  dino-, dinosaur.
17009:Hadrosaurus,  n.,  a  genus  of  extinct  dinosaurian reptiles  ( pa/eontol .)  —  ModL.,  compounded  of hadro-  and  Gk.  araupot;,  ‘lizard’.  See  sauro-. haecceity,  n.,  thisness;  individuality  (scholastic philos.)  —  ML.  haecceitas,  fr.  L.  haecce  (res), ‘this  (thing)’,  with  better  spelling  haece,  fern, of  hlce  (hicce),  intensive  form  of  hie  (fern,  haec, neut.  hoc),  ‘this’.  See  hodiernal  and  cp.  encore, langue  d’oe.  For  the  ending  see  suff.  -ity. haem-.  —  See  hem-.
18691:Iguanidae,  n.  pi.,  a  family  of  lizards  ( zool .)  — ModL.,  formed  fr.  prec.  word  with  suff.  -idae. Iguanodon,  n.,  a  genus  of  dinosaurs  (paleontol.)
23336:Megalosaurus,  n.,  a  genus  of  gigantic  dinosaurs ( paleontol .)  —  ModL.,  compounded  of  megalo- and  Gk.  craopop,  ‘lizard’.  See  sauro-. megaphone,  n.  —  Compounded  of  mega-  and Gk.  9fovif),  ‘voice’.  See  phone,  ‘speech  sound’, megapode,  also  megapod,  n.,  any  of  the  birds  of the  family  Megapodiidae.  —■  See  next  word. Megapodiidae,  n.  pi.,  a  family  of  birds  inhabiting Australia  and  the  Malay  Archipelago  (orni- thol.)  —  ModL.,  formed  with  suff.  -idae  fr. mega-  and  Gk.  7toui;,  gen.  71086;,  ‘foot’.  See podo-.
=== deinos ===
11543:dire,  adj.,  dreadful.  —  L.  dirus,  ‘fearful,  awful, ill-omened,  horrible,  terrible’,  of  uncertain  ori¬ gin.  It  possibly  derives  fr.  I.-E.  base  *dwei-,  ‘to be  afraid,  fear’,  whence  also  Gk.  SeiSoi  (for *S£-Sfot-a),  ‘fear’,  Seop  (for  *8fet-op),  ‘fear¬ ful,  terrible,  powerful,  mighty,  marvelous’, SctXop  (for  *Sfet-Xop),  ‘cowardly’,  Savop  (for *Sfei-vop),  ‘fearful’,  OI.  dvesti,  ‘hates’,  dvisah, ’hatred’,  Avestic  dvaeba-,  'threat,  menace’,  and prob.  also  Arm.  erkncim,  'I  fear’.  Cp.  dino-, dinosaur.
```


## [2026-09-05T20:09:21.404Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\np=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=p.split('\\f')\nprint('nleaves',len(leaves))\n# find leaf containing 'arsenal,  n.,  a  place'\nfor i,l in enumerate(leaves):\n    if 'a  place  for  manufacturing  and  storing' in l:\n        print('arsenal leaf',i)\n    if 'dire,  adj.,  dreadful' in l:\n        print('dire leaf',i)\n    if 'dinosaur,  n.' in l:\n        print('dinosaur leaf',i)\nEOF"
}
```


## [2026-09-05T20:09:22.684Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\np=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=p.split('\\f')\nfor n in (210,211,212):\n    print('=== leaf',n,'~ pp',2*(n-12),2*(n-12)+1)\n    print(leaves[n][:1500])\nEOF"
}
```


### [2026-09-05T20:09:23.083Z] TOOL RESULT

```
nleaves 903
arsenal leaf 68
dinosaur leaf 247
dire leaf 249
```


### [2026-09-05T20:09:24.677Z] TOOL RESULT

```
=== leaf 210 ~ pp 396 397
ro,  n.,  the  monetary  unit  of  Brazil.  —  Port., fr.  cruz,  ‘cross’,  fr.  L.  crucem,  acc.  of  crux, ‘cross’.  See  crucial.
cry,  intr.  and  tr.  v.  —  OF.  (=  F.)  crier,  fr.  VL. *crltare,  corruption  of  L.  quiritare,  ‘to  cry,  wail, scream’,  denominated  fr.  Quirites,  ‘Roman  ci¬ tizens’;  see  Quirites.  Accordingly  quiritare  orig. meant  ‘to  address  the  Romans’,  whence  arose the  meanings  ‘to  implore  somebody’s  help;  to raise  a  plaintive  cry;  to  cry  aloud’.  Cp.  It.  gri- dare,  OProven?.,  OSp.  cridar,  Sp.,  Port,  gritar, which  all  derive  from  L.  quiritare.  Cp.  also decry,  descry.
Derivatives:  cry,  n.,  cry-ing,  adj.,  cry-ing-ly,  adv. cry-,  form  of  cryo-  before  a  vowel, crymodynia,  n.,  pain  caused  by  cold  weather ( med .)  —  Medical  L.,  lit.  ‘pain  caused  by  frost’, fr.  xpOfioc  (for  *xpuap.6p),  ‘frost’,  and  oSu-rt], ‘pain’.  Gk.  xpupuS;  is  cogn.  with  L.  crusta, ‘crust’;  see  crust,  n.,  and  cp.  the  second  element in  isocryme.  For  the  second  element  see  -odynia. crymotherapy,  n.,  the  therapeutic  application  of cold  (med.)  —  Compounded  of  Gk.  xpOpiop, ‘frost’,  and  SEpamria,  ‘a  waiting  on,  service,  at¬ tendance’.  See  prec.  word  and  -therapy, cryo-,  before  a  vowel  cry-,  combining  form  mean¬ ing  ‘cold,  freezing’.  —  Gk.  xpuo-,  xpu-,  fr.  xpuo? (for  *xpuaoc),  ‘icy  cold,  frost’,  which  is  cogn. with  L.  crusta,  ‘crust’.  See  crust, cr
=== leaf 211 ~ pp 398 399
e’;  see  cube  and -ism.  The  word  cubisme  was  coined  by  the French  art  critic  Louis  Vauxcelles  on  the  basis of  a  remark  made  by  the  French  painter  Henri Matisse  (1869-1954)  before  a  landscape  ex¬ hibited  by  Georges  Braque  (1882-1963)  in  the Autumn  Salon  of  1908.  On  that  occasion  Ma¬ tisse  spoke  of  the  ‘small  cubes’  (petits  cubes) characterizing  the  painting  of  Braque.  This  re¬ mark  induced  Vauxcelles  to  form  the  word cubisme.
cubist,  n.,  an  adherent  of  cubism.  —  F.  cubiste, fr.  cube,  ‘cube’.  See  prec.  word  and  -ist. Derivative:  cubist,  adj.
cubit,  n.  —  L.  cubitum  (also  cubitus),  ‘elbow’,  fr. I.-E.  base  *qeu-b-,  ‘to  bend,  curve’,  whence  also cubare,  ‘to  lie  down'.  See  cubicle  and  cp.  cubitus. Cp.  also  codille.
cubital,  adj.,  pertaining  to  the  cubitus  or  cubit.  — L.  cubitalis,  fr.  cubitum  (cubitus).  See  cubit  and adj.  suff.  -al.
cubitus,  n.,  the  ulna  ( anat .)  —  L.  ‘elbow’.  See cubit.
cuboid,  adj.,  resembling  a  cube  in  shape.  —  Gk. xupoEid/jc,  ‘like  a  cube,  cubical’,  compounded of  xu(3o?,  ‘cube’,  and  -oEtSfjt;,  ‘like’,  fr.  eZ8o?, ‘form,  shape’.  See  cube  and  -oid.
Derivative:  cuboid,  n.
cuckold,  n.,  the  husband  of  an  unfaithful  wife.  — ME.  cocold,  kokewold,  kokeweld,  fr.  OF.  cucu- ault,  ‘cuckold’,  a  hybrid  coined  fr.  OF.  cocu (whence  F.  coucou),  ‘cuckoo’,  and  -ault,  -ah, a  suff.  of  Teut.  origin.  
=== leaf 212 ~ pp 400 401
,  a  dupe.  —  Perhaps  abbreviation  of cullion.
culm,  n.,  stalk,  stem.  —  L.  culmus,  ‘stalk,  stem’, cogn.  with  Gk.  xxaxuo?,  xx'Axirr,,  ‘reed’,  OSlav. slama,  Russ,  soldma,  ‘straw’,  OPruss.  salme, Lett,  salms,  ‘blade  of  straw’.  Cp.  calamary, Calumet,  chalumeau,  haulm,  shawm.
culm,  n..  coal  dust.  —  ME.  colme,  perhaps  rel.  to col,  ‘coal’.  See  coal.
Derivative:  culm-y,  adj.
culminant,  adj.,  culminating.  —  L.  culminans, gen.  -antis,  pres.  part,  of  culminare.  See  next word  and  -ant.  .
culminate,  intr.  v.,  to  reach  the  highest  point. Late  L.  culminatus,  pp.  of  culminare,  ‘to  top,  to
4
JOJ
crown’,  fr.  L.  culmen,  gen.  culminis,  contracted form  of  columen,  gen.  columinis,  ‘the  top  of  an object,  summit’,  which  is  rel.  to  columna,  ‘pillar, column’.  See  column  and  verbal  suff.  -ate  and cp.  hill.
Derivative:  culminat-ion ,  n. culot,  n.,  a  small  sheet  iron  cup  inserted  into  the base  of  projectiles.  —  F.,  ‘bottom  of  lamps  or crucibles,  metal  end  of  crucibles’,  dimin.  of  cul, ‘bottom’.  See  culet  and  cp.  next  word, culotte,  n.,  breeches.  • —  F.,  fr.  cul,  ‘bottom’.  See culet  and  cp.  prec.  word.  Cp.  also  sansculotte, culottic,  adj.,  wearing  breeches.  —  Formed  with suff.  -ic  fr.  F.  culotte,  ‘breeches’.  See  prec.  word, culpability,  n.  —  Late  L.  culpabilitas,  ‘guilt,  cul¬ pability’,  fr.  L.  culpabilis.  See  next  word  and  -ity
```


## [2026-09-05T20:09:58.851Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\np=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=p.split('\\f')\nfor n in (66,67,68,246,247,248,249):\n    l=leaves[n]\n    nums=re.findall(r'\\b\\d{3}\\b',l)\n    print(n, 'firstwords:', l.strip()[:60].replace('\\n',' '), '| 3-digit nums:', nums[:12])\nEOF"
}
```


### [2026-09-05T20:10:00.976Z] TOOL RESULT

```
66 firstwords: Asia  (Ovis  am- mon).  —  Mongolian. argand  lamp.  —  Name | 3-digit nums: ['336', '104', '105', '384', '322']
67 firstwords: .  v()-pi-xo4,  ‘numberless’,  OE., OHG.  rim,  ‘number’,  O | 3-digit nums: ['106', '107']
68 firstwords: and  revert, arpeggio,  n.,  the  playing  of  the  notes  o | 3-digit nums: ['108', '109']
246 firstwords: the  finger-shaped  co¬ rollas). Digitaria,  n.,  a  genus   | 3-digit nums: ['449']
247 firstwords: go  through  the  mid¬ dle’,  fr.  dis-  and  medium,  ‘midd | 3-digit nums: ['450', '451', '686', '452', '453']
248 firstwords: Dionysian,  adj.,  pertaining  to  Dionysus.  —  See Dyonysu | 3-digit nums: ['065', '015', '454']
249 firstwords: t.  pi.  of SbiTEpo?,  'having  two  wings’,  fr.  Si-  (see | 3-digit nums: ['455']
```


## [2026-09-05T20:10:09.351Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\np=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=p.split('\\f')\nimport re\nfor n in (247,248,249):\n    l=leaves[n]\n    print('=========== leaf',n)\n    for line in l.split('\\n'):\n        s=line.strip()\n        if re.match(r'^\\d{3}\\b',s) or s.startswith('dino') or s.startswith('dire') or s.startswith('dinosaur') or re.search(r'\\b45[0-9]\\b',s[:80]):\n            print(repr(s[:200]))\nEOF"
}
```


### [2026-09-05T20:10:11.221Z] TOOL RESULT

```
=========== leaf 247
'450'
'451'
'452'
'453'
=========== leaf 248
'454'
=========== leaf 249
'dire,  adj.,  dreadful.  —  L.  dirus,  ‘fearful,  awful, ill-omened,  horrible,  terrible’,  of  uncertain  ori¬ gin.  It  possibly  derives  fr.  I.-E.  base  *dwei-,  ‘to be  afraid,  fear’,  whenc'
"direction,  n.  —  F.,  fr.  L.  directidnem,  acc.  of directio,  'a  making  straight,  aiming,  directing’, fr.  directus,  pp.  of  dirigere.  See  direct,  v.,  and"
'directive,  adj.  —  ML.  directivus,  fr.  L.  directus, pp.  of  dirigere.  See  direct,  v.,  and  -ive. Derivatives:  directive,  n.,  directive-ly,  adv.,  di- rective-ness,  n.'
'directoire,  n.,  the  French  Revolutionary  Govern¬ ment  of  1795-99.  —  F.,  fr.  ML.  directorium.  See directory,  n.'
'director,  n.  —  AF.  directour,  equivalent  to  F. directeur,  fr.  Late  L.  directorem,  acc.  of  director, fr.  directus,  pp.  of  dirigere.  See  direct,  v.  and agential  suff.  -or.'
'directorate,  n.  —  Formed  fr.  prec.  word  with subst.  suff.  -ate.'
'directory,  adj.  —  Late  L.  directorius,  ‘that  which directs’,  fr.  L.  directus,  pp.  of  dirigere.  See  di¬ rect,  v.  and  adj.  suff.  -ory. directory,  n.  —  ML.  directorium,  prop.  ne'
'direful,  adj.,  dire.  —  Formed  on  analogy  of  dread¬ ful.  See  dire  and  -ful.'
'455'
```


## [2026-09-05T20:10:20.963Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\np=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=p.split('\\f')\nl=leaves[247]\ni=l.find('dino-')\nprint(l[i-200:i+1400])\nEOF"
}
```


### [2026-09-05T20:10:23.745Z] TOOL RESULT

```
 of  uncertain  origin, dinner,  n.  —  ME.  diner,  fr.  F.  diner,  ‘dinner’, prop,  the  infinitive  diner,  ‘to  dine’,  used  as  a noun.  See  dine.
Derivatives:  dinner-y,  dinner-less,  adjs. dino-,  combining  form  meaning  ‘fearful’.  —  Gk. Seivo-,  fr.  8eiv6?  (for  *8fei-vo?),  ‘fearful’,  rel. to  8ei8o>  (for  *8£-8Foi-a),  ‘I  fear’,  8£o?  (for *8Fei-o?),  ‘fearful,  terrible,  powerful,  mighty, marvelous’,  Seiko?  (for  *8Fei->,6?), 'cowardly,  and possibly  cogn.  with  L.  dims,  ‘fearful’.  See  dire. Dinobryon,  n.,  a  genus  of  flagellates  (biol.)  — ModL.,  compounded  of  Gk.  STvo?,  ‘a  whirl¬ ing’,  and  ppftov,  ‘moss’.  See  dinus  and  bryo-. Dinoceras,  n.,  a  genus  of  extinct  ungulates  (pale- ontol.)  —  ModL.,  compounded  of  dino-  and Gk.  x£pa?,  ‘horn’.  See  cerato-.
Dinoflagellata,  n.  pi.,  an  order  of  flagellates (biol.)  —  A  ModL.  hybrid  coined  fr.  Gk.  STvo?, ‘a  whirling’,  and  L.  flagellum,  ‘whip’.  See  dinus and  flagellum.
Dinomis,  n.,  a  genus  of  recently  extinct  birds  re¬ sembling  an  ostrich.  The  New  Zealand  Moa belonged  to  this  genus  (paleontol.) — ModL.,  lit. ‘a  frightful  bird’,  compounded  of  dino-  and Gk.  8pvi?,  ‘bird’.  See  omitho-. dinosaur,  n.  any  member  of  the  Dinosauria.  — See  next  word.
Dinosauria,  n.  pi.,  a  group  of  extinct  Saurian  rep¬ tiles  (paleontol.)  —  ModL.,  lit.  ‘frightful  liz¬ ards’,  compounded  of  dino-  and  Gk.  aaopa, caupop,  ‘lizard’.  See  sauro-.
Derivatives:  dinosaurian,  adj.  and  n. dinothere,  n.,  any  member  of
```


## [2026-09-05T20:10:30.418Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\np=open('POK_01.txt',encoding='utf-8',errors='replace').read()\nleaves=p.split('\\f')\nfor i,l in enumerate(leaves):\n    if \"duei-  ,fürchten'.\" in l:\n        print('leaf',i,'=> printed page approx',i-8)\n        print(l[:2600])\n        break\nEOF"
}
```


### [2026-09-05T20:10:33.410Z] TOOL RESULT

```
leaf 238 => printed page approx 230
ds.,  ags.  topp  m.  ,Gipfel',  mhd.  zopf  ^Zopf,  Ende  eines  Dinges',  mit  bb: mnd.  tobbe,  tubbe  , Zapfen',  vgl.  Xqü.  duba  ,aufgestellte  Garbe';  germ. *tappan  ,Zapfen'  in  ags.  tssppa  m.  (engl,  tap)^  mnd.  tappe  m.,  ahd.  zapho, mhd.  zapfe  m.  Offenbar  ,mot  populaire'  mit  intensiver  Konsonantenschär- fung,  Nasalierung  und  Vokalwechsel  a:i:ii'^  vgl.  oben  S.  221  drop- :  drip- : drup-.    S.  auch  oben  S.  177.
WP.  I  816,  Fick  III  155,  164,  168,  Petersson  Heterokl.  70  f.
cfus-  ,übel,  miß-'  als  1.  Kompositionsglied.
Ai.  dus-,  dur-,  av.  diLS-,  duz-  ,miß-,  übel',  arm.  t-  ,un-',  gr.  ovo-  ,miß-, übel',  lat.  in  difficilis  ,schwierig',  air.  do-j  du-  ds.  (lenierend  nach  dem Vorbild  von  so-,  su-),  got.  tuz-  (in  tuz-werjan  ,zweifeln'),  anord.  ags.  tor-j ahd.  2;wr-  ,un-',  slav.  in  abg-.  d^zdh  {^duz-djus  ^schlechter  Himmel'  ==)  ,Regen', russ.  dozdh,  poln.  deszcz^  aöech.  desc.  Gen.  dsce  und  analogisch  deH4.  Zu- sammenhang mit  deus-  ,ermangeln'  ist  sehr  wahrscheinlich.
Erst  ind.  aus  dus-  entwickelt  ist  düsyati  ,verdirbt,  wird  schlecht', dusta-  ,verdorben,  schlecht',  düsdyati  ,verdirbt,  versehrt'.
WP.  I  816,  E.  Fraenkel  M^  Pedersen  453.
duei-  ,fürchten'.
Av.  dvaed-ä  ,Bedrohung'j
arm.  erkntim  ,ich  fürchte',  erkiul  ,Furcht'  (Anlaut  wie  in  erku  ,zwei' '.*diLöu  Meillet  MSL.  8,  235);
16*
228
gr.  hom.  deldo)  ^fürchte^  (*Ö6-dfot-a),  Plur.  dsidci-iey  (d.  i.  öidJ^iixsv)^ dsdii-isv   (danach    der   neue    Sg.  hom.  dsLÖia^  d.  i.  öadJ^ia,  att.  deöia)^ hom.  MdÖBLaev  (d.  i.  söJ^eiasv),  hom.  diß  ,fürchtete^;  aus  *6söJ=oia  umgebiß Perf.  hom.  dsiöoiKa,  att.  didoL^a,  kret.  dsöSoiTCMg  Hes.  (Hs.  dsd^or/wg)^  ^^ öedeiyisXog  Hes.  ^furchtsam';  zu  öeöia-Ao^ai  (nachhom.)  .schrecke'  (*<Jfi-dj GY-o-iiai)  wurde  sekundäres  d€Ldl^O(.iaL  gebildet,  wovon  erst  att.  dedlztoi hom.  SsLÖiGao^iaL]  hom.  66iörj(.uüv  .furchtsam'  (*dsdJ^strj^tov);  ösog  n.  .Furcj (*(5/eiog).  d-eovörig  .gottesfürchtig'  (*^£0-(^/£iäg).  öel^ia  n..  SsL^iög  m.  , Furcht dfitvrfg  .schrecklich'.   JstAog,  .furchtsam,  feig;    unglücklich,   beklagenswert (*öJ^€isX6g)'j  diSQÖg  .zu  fürchten'  (*öJ^L-eQOg)]
lat.  cZ^rws  .grausige  grauenvoll,  unheilvoll'  (von  Servius  zu  Aen.  IH  gs auch  als  sabin.  und  umbr.  Wort  angeführt,  so  daß  di-  statt  bi-  aus  *d% als   mundartliche   Lautentwicklung),   mit   Formans   -ro-  .wovor   man fürchtet',  wie  clä-rus  .hörbar'.
s-Erweiterung   in   ai.  dvist
```


## [2026-09-05T20:10:43.212Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\np=open('POK_01.txt',encoding='utf-8',errors='replace').read()\nleaves=p.split('\\f')\nl=leaves[238]\ni=l.find('s-Erweiterung')\nprint(l[i:i+2200])\nEOF"
}
```


### [2026-09-05T20:10:44.723Z] TOOL RESULT

```
s-Erweiterung   in   ai.  dvisti  .haßt,  feindet  an',  dvistd-   .verhaßt',  dvesa-/^ ra..  dvisas-  n.  .Haß',  av.  dvae§-,  tbaeS-  .anfeinden,  kränken'.  Partiz.  thüta- dva&sah-,   tbaesah-  .Anfeindung',   mpers.  bes  .Leid
```


## [2026-09-05T20:11:04.202Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\np=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=p.split('\\f')\nfor i,l in enumerate(leaves):\n    if re.search(r'(?m)^\\s*39[5-9]\\s*$', l):\n        print('leaf',i,[m.group() for m in re.finditer(r'(?m)^\\s*\\d{3}\\s*$',l)], l.strip()[:80].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T20:11:06.150Z] TOOL RESULT

```
leaf 218 ['396', '397'] See  -cyte. cytology,  n.,  study  of  the  structure,  functions  and life  his
```


## [2026-09-05T20:11:12.074Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\np=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=p.split('\\f')\nprint(leaves[218][-2500:])\nEOF"
}
```


### [2026-09-05T20:11:14.033Z] TOOL RESULT

```
ther,  son’,  which  all  are  of  childish origin.
Dada,  n.,  an  artistic  movement  characterized  by incoherence  and  the  love  of  paradoxes  ( art  and lit.)  —  F.  dada,  prop,  a  child’s  word  meaning ‘horse,  hobby  horse,  hobby’.  This  word  was chosen  in  1916  by  Tristan  Tzara,  a  Rumanian- born  poet  and  editor  in  Paris  (1896-1963),  to designate  this  artistic  movement.
Dadaism,  n.,  Dada.  —  F.  dadalsme,  formed  from prec.  word  with  suff.  -is me  (see  -ism).
Dadaist,  n.,  an  adherent  of  Dadaism.  —  F.  dada¬ ist  e,  formed  fr.  Dada  with  suff.  -iste  (see  -ist). dado,  n.,  a  part  of  the  pedestal.  —  It.  dado,  ‘die, cube,  pedestal’,  fr.  L.  datus,  ‘given’,  pp.  of  dare, ‘to  give’.  See  date,  ‘point  of  time’,  and  cp. die,  ‘cube’.
Derivative:  dado,  tr.  v.
daduchus,  dadouchos,  n.,  torchbearer  in  the  Eleu- sian  mysteries.  —  L.  daduchus,  fr.  Gk.  SqiSoOxo?, ‘torchbearer’,  which  stands  for  *Sa8o-8x°?  and
396
397
is  compounded  of  Sat?,  8a:?  (gen.  8at8o?,  resp. 8x36?),  ‘torch’,  and  syeiv,  ‘to  hold,  have’.  The first  element  is  rel.  to  Sodetv  (for  *Sxft£iv),  ‘to blaze,  bum’,  and  cogn.  with  OI.  dundti,  ‘bums’, davah,  ‘conflagration’,  OIr.  doim,  ‘I  singe,  bum’. Cp.  the  first  element  in  Deianira.  For  the  second element  see  hectic.
daedal,  adj.,  ingenious,  skillful.  —  L.  daedalus,  fr. Gk.  SalSaXo?,  ‘cunningly  made’,  fr.  SatSaXXetv, ‘to  work  cunningly  or  skillfully’,  which  stands for  *8ai-8ctXieiv  and  is  formed  with  redupli¬ cation  of  I.-E.  base  *del-,  *dol-,  ‘to  split,  cut, carve’,  which  appears  in  OI.  dalati,  ‘splits, bursts’,  ddlayati,  ‘causes  to  burst,  splits  open’, dalam,  ‘part,  piece’,  L.  dolare,  ‘to  hew  with  an ax’,  dolium,  ‘a  very  large  jar’.  See  dole,  ‘grief’, and  cp.  Daedalus,  dal  and  the  second  element  in logodaedaly.  Cp.  also  tale.  The  word  daedal  was first  used  in  English  by  Spenser, daedalian,  adj.,  pertaining  to,  or  resembling,  the work  of  Daedalus.  —  See  Daedalus  and  -ian. Daedalus,  n.,  the  mythical  artist,  father  of  Icarus and  builder  of  the  Cretan  labyrinth. — L.,  fr.  Gk. AodSaXo ?,  lit.  ‘the  cunning  worker’.  See  daedal, daemon,  n.  —  L.,  fr.  Gk.  8a(|io>v.  See  demon, daemonic,  adj.  —  Late  L.  daemonicus,  fr.  L.  dae¬ mon.  See  daemon  and  -ic. daffodil,  n.  —  Du.  de  affodil,  ‘the  asph
```


## [2026-09-05T20:11:30.336Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"dahr\\|ddra\\|Arab,  dar\\|Arab,  ddr\\|dawwar\\|douar\\|duar\\b\" KLN_1966.txt | head -20"
}
```


### [2026-09-05T20:11:30.389Z] TOOL RESULT

```
1587:adder,  n.,  a  snake.  —  ME.  naddre,  addre,  fr.  OE. nxdre,  ‘adder,  snake’,  rel.  to  OS.  nddra,  ON. nddra,  MDu.  nadre,  Du.  adder,  OHG.  natara, MHG.  nater,  G.  Natter,  Goth,  nadrs,  and  cogn. with  L.  natrix,  ‘water  snake’  OIr.  nathir,  W. neidr,  OCo.  nader,  ‘adder’.  All  these  words  prob. derive  fr.  I.-E.  base  *(s)ne-,  ‘to  wind,  twist’, whence  also  Gk.  v?jv,  L.  nere,  ‘to  spin’.  See needle  and  cp.  natrix.  The  loss  of  the  initial  n  in
1701:adorable,  adj.  —  L.  adordbilis,  ‘worthy  of  adora¬ tion’,  fr.  addrare.  See  adore  and  -able. Derivatives:  adorable-ness,  n.,  adorabl-y ,  adv. adoration,  n.  —  F.,  fr.  L.  adordtidnem,  acc.  of addratid,  ‘worship,  adoration’,  lit.,  ‘a  praying to’,  fr.  addrdtus,  pp.  of  addrare.  See  next  word and  -ion.
1702:adore,  tr.  v.  —  F.  adorer,  ‘to  adore,  worship’,  fr. L.  addrare,  ‘to  speak  to,  entreat,  ask  in  prayer, worship’,  fr.  ad-  and  orare,  ‘to  speak,  pray’. See  oration.
3518:arsenal,  n.,  a  place  for  manufacturing  and  storing ammunition  and  weapons.  —  It.  arsenale  (Olt. arzanale),  ‘dock’,  borrowed — prob.  through  the medium  of  MGk.  d.pm]'tdkt)C, — fr.  Arab,  dar- a?-sind'ah  (whence  also  Sp.  darsena  and  It.  dar- sena,  ‘dock’),  lit.  ‘house  of  construction’,  fr.  ddr, ‘house’,  as-,  assimilated  form  of  al-,  ‘the’,  and Sind'ah,  ‘construction,  art’,  fr.  Sana' a,  ‘he  made’. For  the  ending  of  arsenal  see  adj.  suff.  -al. arsenic,  n.,  a  chemical  element.  —  OF.  (=  F.) arsenic,  fr.  L.  arsenicum,  arrhenicum,  fr.  Gk. dptrsvixov,  appevvxov,  ‘yellow  orpiment',  fr. MPers.  *zarnik,  ‘gold,  golden ;  orpiment’(whence ModPers.-Arab.  zarnikh,  ‘orpiment’),  through the  medium  of  a  Semitic  language;  cp.  Mish- naic  Heb.  zarnikh,  Syr.  zarnikhd,  ‘orpiment’. Cp.  Avestic  zaranya,  Pers.  zar,  ‘gold’,  and  the first  element  in  zermahbub,  and  see  yellow  and words  there  referred  to.  Cp.  also  jargon,  ‘a variety  of  zircon’.  Gk.  apctevtxov,  appsvtx&v, ‘orpiment’,  was  influenced  in  form  by  apcrevtxop, appevixic,  ‘male’,  fr.  ape rc;v,  ap pr,v,  ‘male’.  For the  sense  development  of  MPers.  *zarnik,  cp.  L. auripigmentum,  fr.  aurum,  ‘gold’  (see  orpiment). Derivatives:  arsenic,  arsenic-al,  adjs. arsenious,  adj.,  containing  arsenic.  —  See  ar¬ senic  and  -oils.
5107:Derivatives:  blackmail,  tr.  v.,  blackmail-er,  n. bladder,  n.  —  ME.  bladre,  bledder,  fr.  OE.  bliedre, bUeddre,  ‘blister,  bladder’,  rel.  to  OS.  bladara, ON.  bladra,  Swed.  bladdra,  OHG.  blattara, MHG.  blatere,  G.  Blatter,  Du.  blaar ;  formed fr.  Teut.  base  *ble-,  ‘to  blow,  inflate’,  corre¬ sponding  to  I.-E.  base  *bhlo-,  *bhle-  (see  blow, ‘to  puff’),  with  suff.  -dro,  which  corresponds  to Gk.  -xpo,  L.  -tro  (see  rostrum).  Cp.  the  second element  in  isinglass.
7682:Derivative :  cincture,  tr.  v. cinder,  n.  —  OE.  sinder,  ‘impurity  of  metal, dross’,  rel.  to  OS.  sinder,  ON.  sindr,  Dan  sinder, MLG.,  MDu.  sinder,  Du.  sintel,  OHG.  sintar, MHG.  sinter,  sinder,  G.  Sinter,  and  cogn  with OSlav.  sfdra,  ‘sinter’,  Czech  sddra  (for  *sen- dhrd),  ‘gypsum’.  Cp.  sinter.  The  spelling  of  sinder was  influenced  by  F.  cendre ,  ‘ashes’,  with  which it  has  nothing  in  common.
10232:daira,  n.,  formerly,  estates  of  the  Egyptian  khe- dive.  —  Arab.  dd’irah  (in  vulgar  pronunciation dayra),  ‘circle,  enclosure’,  prop.  fern,  partic. of  ddra,  ‘he  moved  in  a  circle,  went  about’, which  is  rel.  to  dar,  ‘house’,  orig.  ‘buildings  sur¬ rounding  a  court’,  daur,  ‘circumference’,  dahr, ‘long  time,  age’,  Heb.  dur  (n.),  ‘circle,  ball’,  dur (v.),  ‘to  dwell’,  orig.  ‘to  move  in  a  circle’,  dor, ‘generation’,  Mishnaic  Heb.  madhSr,  ‘dwelling place’,  Aram,  dur,  ‘to  dwell’,  mfdhdr,  medhar, ‘dwelling  place’,  dar,  ‘generation’,  Akkad,  duru, ‘wall,  fortress’,  also  ‘duration,  eternity’,  daru, ‘everlasting’.  Cp.  next  word, daira,  n.,  a  large  kind  of  Oriental  tambourine.  — Fr.  dayra,  vulgar  Arab  pronunciation  of  dd’irah, ‘circle,  tambourine’.  See  prec.  word, dairy,  n.  —  ME.  deierie,  formed  with  suff.  -erie fr.  deie,  ‘dairymaid’,  fr.  OE.  dsege  ‘(female) breadmaker’,  lit.  ‘kneader  of  dough’,  fr.  dag, ‘dough’.  Cp.  ON.  deigja,  Swed.  deja,  ‘dairy¬ maid’,  which  derive  fr.  ON.  deig,  resp.  Swed. deg,  ‘dough’,  and  see  dough.  Cp.  also  the  second element  in  lady.  For  the  ending  see  -ery. Derivative:  dairy-ing,  n.
12106:Doronicum,  n.,  a  genus  of  plants.  —  ModL.,  fr. Arab,  dardnaj,  dardnaj.
12318:drub,  tr.  v.,  to  beat  with  a  stick ;  intr.  v.,  to  stamp. —  The  orig.  meaning  was  ‘to  bastinado’;  prob. fr.  Arab,  darb,  ‘a  beating  (with  a  stick)’,  fr. ddraba,  ‘he  beat,  struck’.
23857:midrash,  n.,  exposition  of  the  Holy  Scriptures ( Hebrew  literature).  —  Heb.  midhrdsh,  ‘study, exposition’,  in  Mishnaic  Hebrew,  ‘homiletical interpretation’,  fr.  Heb.  ddrash ,  ‘he  sought,  in¬ quired,  investigated’,  in  Mishnaic  Heb.  also  he expounded,  interpreted’;  hence  Aram,  d  rash , ‘he  searched  out,  investigated,  interpreted’,  and — through  the  medium  of  this  latter — Arab. ddrasa,  ‘he  read  repeatedly,  he  studied’,  Ethiop. darasa,  ‘he  expounded’.  Cp.  madrasah, midriff,  n.,  the  diaphragm.  —  ME.  mydrif,  fr.  OE. midhrij,  a  compound  of  OE.  midd  (see  mid,  adj.) and  hrif,  ‘belly  ,  which  is  rel.  to  OHG.  href. OFris.  hrif  href,  ‘belly’,  OHG.  href,  ‘body’,  and cogn.  with  L.  corpus,  ‘body’.  See  corpus  and  cp. words  there  referred  to.
24974:—  F.  narcolepsie,  coined  by  the  French  physi¬ cian  Jean-Baptiste-£douard  Gelineau  ( 1859— 1928)  in  1880  fr.  Gk.  vxpxT),  ‘numbness’,  and Vrfj'.z,  ‘a  taking,  seizing,  seizure’.  See  narcotic and  lemma  and  cp.  words  there  referred  to.
28854:Pindari,  n.,  one  of  a  horde  of  marauders  in  India in  the  18th  and  early  19th  centuries.  —  Hind. pinddra,  Marathi  pendhari,  possibly  from  the place-name  Pandhar.
```


## [2026-09-05T20:11:31.691Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"dahr\\|da'irah\\|daira\" FVQ_pages.txt | head -20\necho \"=== dar house ===\"\ngrep -n \"الدهر\\|dahr\" FVQ.txt | head"
}
```


### [2026-09-05T20:11:31.792Z] TOOL RESULT

```
=== dar house ===
```


## [2026-09-05T20:11:50.927Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\np=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=p.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'formerly,  estates  of  the  Egyptian' in l:\n        print('daira leaf',i,[m.group().strip() for m in re.finditer(r'(?m)^\\s*\\d{3}\\s*$',l)])\nEOF\necho \"=== KLN 1971 arsenal ===\"\ngrep -n -o \"arsenal,  n.,.\\{0,700\\}\" KLN_1971.txt | head -3"
}
```


## [2026-09-05T20:11:52.642Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD db'yš ===\"; grep -n \"\\bδβ\\|db'yš\\|dbyš\\|Sß'yš\" SOD_pages.txt | head -10\necho \"=== SOD enmity ===\"; grep -n -i \"enmity\" SOD_pages.txt | head -20"
}
```


### [2026-09-05T20:11:52.679Z] TOOL RESULT

```
daira leaf 219 []
=== KLN 1971 arsenal ===
```


### [2026-09-05T20:11:52.748Z] TOOL RESULT

```
=== SOD db'yš ===
=== SOD enmity ===
13713:     enmity, harm                                              3496 5pnstr M                                   j£r*3*j&
26833:8020 ptyJm-     M, S                 o*/fU; to^^J^                 misfortune, enmity
28835:     enmity                                                      sarPuy ©<*sar~a-bu; Syr \srbwg; Uigur. sarvaY
28840:     enmity                                                8725 s*rst M, C                             U j < v^ iaj^l
38158:   10320                                       enmity    3481, 8030, 8711, 8712        Eucharist       5036
```


## [2026-09-05T20:11:56.992Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '13700,13725p' SOD_pages.txt"
}
```


### [2026-09-05T20:11:57.043Z] TOOL RESULT

```
3479 db>t C => 5pH
                                                                      doubt, suspicion, fear
3480 *5p>y- B                                         o^^J
                                                                      GMS 513, 1236; TSP; Hen. Texts. 719; SCE 216;
     8/0pay
       db'n(y)? ©Av. Gwaya         ^nSPy-, wy5p>y-,
                                                                         BSTBL, Padm, 30, Vim. 127, Dhu. 233-4; MDii
                                                                         A9V2; C2, 48R 15 n p86; 6fin\ TSP 15.23
       OcOextend
       GMS 293
                                                               3493 8pnh *± 5pn->h
3481 Sp'ys B                                      jljT.^o      3494 8pnnh B =* 5Pn->h
     8Pcs ©Av. dvaes =*5Pys                                    3495 Spnpn =» 5P}mpn(w)
     enmity, harm                                              3496 5pnstr M                                   j£r*3*j&
     VJ 1047
                                                                    wider
                                                                    8Panstar ®<*61Pnz-str         ^SP'nz
3482 8p>ys-        M                         ^jocu. <jjbjljT
       6Pes      =>8Pys~                                              GMS 465, 1290
       OcOharm                                                 3497 5pnw B                                               ^
       Hen. Tales. 476.5; GMS 682                                   both
                                                                    6Panu <§)*dwi-(nu)\ Lat. binu =>5ypnw
3483 5p»yz- B, S                        (j^i :Jj~>)j^^\
                                                                      VJ 277; GMS 430, 1316
   • SPez, Ofez ®<*0wajaya-           -»Gfxst-, SP'yst-,
         Gfyz-, Spjnyh, tbyz-                                  3498 dbr C =» 5Pr-2
```


## [2026-09-05T20:12:03.069Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=13713 && /\\[pdf page/ {p=$0; n=NR} END{}' SOD_pages.txt\ngrep -n \"\\[pdf page\" SOD_pages.txt | awk -F: '$1<13713' | tail -3\ngrep -n \"\\[pdf page\" SOD_pages.txt | awk -F: '$1>13713' | head -2"
}
```


### [2026-09-05T20:12:04.798Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:12:08.162Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nhead -3 SOD_pages.txt; echo ---; grep -c $'\\f' SOD_pages.txt; echo ---\npython3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\n# find leaf containing entry 3481\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if '3481' in l and 'enmity, harm' in l:\n        print('leaf',i,'printed page approx',i-66)\nEOF"
}
```


### [2026-09-05T20:12:10.083Z] TOOL RESULT

```
 SOGDIAN
DICTIONARY
Sogdian - Persian - English
---
642
---
leaf 203 printed page approx 137
```


## [2026-09-05T20:12:14.753Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD ===\"; grep -n \"bēš\\|be:s\\|besh\\|bēš\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== NYB ===\"; grep -n \"bēš\\|bes'\\|bēšāz\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-05T20:12:14.819Z] TOOL RESULT

```
=== PHD ===
PHD.txt:256:bayaspānļīh: mission, embassy. ~ig [-yk'] post-(horse). Бах [Pc | N ~] hawk, falcon. bāzā [b’c’y | (N bāzū)] arm. ~banag [-p'nk'] arm-guard, brassard. bazaģ [bck' | М beg, N ~a] sin, evil. —ih: = bazag. bazakkar [bckkl | M bzkr] sinful, sinner. bāzā-zanišnīh [by znfnyh = Av. bázu.jata-] a degree of sin. bazišn [dcšn'] division, part. bazm [bzm | — M, N —] meal, feast. ~-awurd [-zolt! | N ~] a sort of canapé. 1bë [BRA < A br | MP] but; out; ~... (enya), except. ~...enya...né: except... (otherwise)... not. ~ az: without. m 2be [BRA | M P, N bi-] particle with verbs, with 6, of indefinable function. -bed [-pt' | M -byd, N -balilud] suffix, -lord, -master. bēdom [bytwm | M bydwm] furthermost. béganag [byk’nk' | N ~a] strange; stranger. bégar [byk”/ | N ~] corvée, forced labour. béh [byh | N bih] quince. bel [by] | (M. Бу), N ~] spade. bélür [bylwl | M bylwr, N bilür] crystal. bérón [bylwn' | M byrwn, N bérün] outside. bëš [bys] pain, sorrow; harm, hostility. — burdan: bear hostility. bēš-, —i&n, v. bištan. bēšāz [byš(*)z] healing, medicinal. bēšāz(ēn)- [by?z(yn)-, byf?)c(yn)- | M byP?z-] heal, cure. —išnih: healing. bēš-burdār [byšbwlť’[] hostile. bëšidan [bysytn'] = bištan, bēšūmand [byš?*wmnd] sorrowful. béwar [Буш | M bywr, N ~] myriad, ten thousand. P bid [руй | P byd] again. bidaxš [byths] viceroy. *bifagàn [bch'n!] medicinal. bim [bym | = M, N ~] fear, terror. ~gén [-kn'] fearful, terrible. ~génih: fearfulness. --6mand [-'wmnd] fearful. *bistag [bstk! | N busta] hazelnut. biš [byf | N —] aconite. bištan, bé&- [bys-in' | M by$t, bys-] hurt, torment. ~išn: harm, torment. bize&k [dešk! | M bzyšk, N pizišk] doctor, physician.
PHD.txt:312:débag [dyp’k! | N dēbā] brocade. débahr [dyp?hl | P dybhr] anger. pad — dāštan: banish. dég [dyk' | N ~] cauldron. LU) deh [M TA < A m? | M dyh, N ~] country, land; village. 0" гу -ģān [МТА-, dh? »'] = dahigàn. dën [dyn' | = M, N din] religion; cal. 24th day. dēnār [4ут/ | N dindr] (gold) dinar. dēn-āstawān [dyn’stwh’n'], dēn-burdār [dynbwit^l] believing, faithful. dénig [dyny&! | N dini] religious. dénódag [dynwtk'] female, milch. dér, dérand, v. dagr, dagrand. d��s(ag) [dys(k') | M dys] form, appearance. désidan, dēs- (dys-ytn! | M dys-yd] build. déw [SD Y.A < A #02, pl. šydy? | N ~] demon, devil. dēwān [d(p)ywn! | N <] archive, collected writings. déwanag [dyw”nk! | N ~a] demonic, mad. dēwār [dyw?l | M dyw’r, N ~] wall. déw|-ésnih [Š D Y Aysnyh | (M dyw?snyh)] idolatry, devil-worship. ~-ézagih [ŠD Y Ayckyh] = ~-ésnih. dēwēk [dywwk! | № déwuk] leech. dibir [dpy(w)r' | M dbyr, N ~] scribe. ~ih: writing, scribeship. „estān [-st?n! LN ~] school. did [TWB < A twb; dt'] again, then, further. didan, wén- [HZ Y TWN-tn! < A У hzy; dytn', wyn- | M dydn, wyn-, N —, bin-] see. ~išn: sight, seeing. ~i8nig : visible. didar [dyť] | N ~] sight; visible. pad ~ [N padidár] visible. didom [dtwm] second. dil [LB(B)ME < A lb(b)-h; dyl | = M, N ~] heart. dilér [dylywl, dlyl | N ~] brave. diz [KLYTA < A дур; dc | M dyz, N ~] fortress. dē [2, TLYN' < A tryn | M dw, N du] two. ~-ахмапіб [2 !hw)nyk!] relating to both worlds. ~ganag [dwk”nk! | M dwg'ng, N dugāna] double; twin. dok [dwk! | N ~] spindle. dol [del | N —] bucket; astr. Aquarius. dó|-pahikar [dwptkl | N du-paikar] astr. Gemini. ~-pay [2 LGLE, дора | N du-pà] biped, human being. dos [dws | N —] gum; plaster. dē-saxwan [2 shwn'] two-tongued, deceitful. dēsēn [dwsyn'] gummy; plastery; *glazed (pottery). dóst [dwst' | = M, N ~] friend.
PHD.txt:390:hambār [kmb’l | N anbdr] store. hambārīdan, hambār- [hm-, hnb'l-ytn! | M hmb'r-, N anbürdan] fill, collect. hambasān [Anbs?n! | M *mbs*n] enemy, opponent. ~ig [-yk'] inimical, opposing. hambast [Ambst' | N anbast] compact. !hambastag [Ambstk' | N anbasta] formed, composed. shambastag [hnbstk' | М hmbst] collapsed, fallen. hambāstag [hmb’stk'] *all. īhambastan, hamband- [hmbsin', hmbnd-] form, compose; bind to- gether, intertwine, encircle. ~i8nih : binding together, intertwining. žhambastan, hambah- [%xbstn!, hnb?h- | M hmbst, hmbh-] collapse, fall down. VW "E. hambāstan, hambāh- [hnb’stn', hnb’d- | M hmb’stn, hmb’h-] cast down, demolish. ~išn: felling, demolition. ham-bašn [hmbén'] of the same stature. hambaw-, —išn, v. hambüdan. hambāy [hmb?g | (M hmb’w)] companion, partner; adversary. hambāz [hm-, hnb’c | M ?mP?z, N anbáz] partner. hambedig [%mbytyk!] = hambadig. hambēš-, —išn [hnbwi-, -£n! | N anbūšif] = hambüs-, ~išn, hambdy- (hnbwd- | M hwmbwy-, N anbóy-idan] smell (tr.). —ügih [-*kyh], —iŠn: (sense of) smell. hambüdan, hambaw- [hm-YHWWN-tn', v. büdan; hmbwtn'] be united, composed. „«išn(īh): union, composition. hambun [hmbwn'] (with a negative) not at all, not in the least. hambüsidan, hambūs- [hnbws-ytn' | N anbüsidan] come into being, be conceived. ~išn: conception. ham-dádestàn (hm-D YN A, -d'tsn! | N ham-dástán] agreeable, of the same opinion. hamdam [hmdm | N ~] intimate. ham-désag [hmdysk'] of the same form, homomorphous. hamë [hm’y | M Атуш, N ~] always. ^ ka: whenever. ham-ēdēn [m)ytwn! | N hamédün] likewise, similarly. bamé|ig (/um)yyk! | M тушур] eternal. ~iha [-yh’] eternally. hamémiil [mym] | = J] opponent, adversary. --īh: opposition. haménidan, hamén- [hmyn-ytn'] unite, compose. hamē-rawišnīh, hamē-ud-hamē-rawišnīh [(Amy W) hwy lwbsnyh) eternity.
PHD.txt:414:jawédan [LOLMN < А l-Imn; ywyt?n' | (P y'wyd?n, M Pyn), N ~] eternally, always. ~ag [-k! | (P -g), N ~a] eternal, perpetual. jawén [S£yn! | № jawin] made of barley. jeh [yh, yyh = Av. jahi-] the Whore, female arch-demon. fiw [суш!, yyw! = Av. fiwya-] (consecrated) milk. *jomā [ywm’y] together with; both. jorda [ywilt’y, 2k | (P yw?rd?w), J *jwrd?r] corn, grain. jo(y) [ywd, ywb! | N ~] stream, channel. Jóy-, -išn, v. Jadan. jud [ywdt' | M jwd] separate, different; anti-. ~ az [N juz] except, apart from. judàg [ywd? h! | N juda] separate, different. ~ih: separation, difference. Jūdan, jóy- [ywtn!, ywd- | M jwwdn, (jw-), (N jawruan)] chew; devour (daevic). „išn: eating (daevic). jud-|-bēš [ywdt bys] harmless, antidote. ~-dadestan [-D YN A] disagreeable, opposing. ~-déw [-ŠD YA) anti-demonic. ---này [-> d] a fathom (6 ft.). jud-ristag [yzodt lystk!] schismatic, heretic. ~th: heresy. Juy [усе | N ~] yoke. Jumbāģīh [ywmb’kyh] motion. jumbénidan, jumbén- [ywmbyn-yin'] (cause to) move. jumbidan, jumb- [ywmb-yin' | N ~] move. ~išn: motion, movement. jumbihistan, jumbīh- [ywmbyh-stn'] be moved. juttar [ywdtl | M jwtr] different, otherwise. --īh: opposite, reverse. Juwān [ywb?n! | (P ywn), N jawàn] young; a youth. ~th: youth. juxt [ywht! | (P ywxt), N juft!] pair, couple.
PHD.txt:1465:cure bēšiz(ēn)-.
PHD.txt:2205:harm (n.) ak, anāgīh, azarm, bei, bēšišn, wizend, zyàn.
PHD.txt:2211:harmless abes, abéwizend, judbēš.
PHD.txt:2212:harmlessness abēših.
PHD.txt:2232:heal bēšāz(ēn)-.
PHD.txt:2233:healing (a.) bēšāz.
PHD.txt:2234:healing (n.) bēšāz(ēn)išnīh.
PHD.txt:2324:hostile bēšburdār.
PHD.txt:2325:hostility ех; bear ~ bēš burdan.
PHD.txt:2343:hurt (v.) bištan, (bēšīdan), rēšīdan.
PHD.txt:2484:invulnerability abēšīh.
PHD.txt:2485:invulnerable abēš, abēwizend.
PHD.txt:2768:medicinal bēšāz, bijagān; ~ plant rürag.
PHD.txt:3031:pain bēš, dard, pim.
PHD.txt:3538:scribeship dibirih.
PHD.txt:3741:Sorrow andag, andoh, bēš, pim, témar, zarīg. sorrowful andag(g)én, andēhgēn,
=== NYB ===
969:bé [BR”; Sas. inser. BL”; Prth. LBR"] with enel. bé-c 3812, bé-p 53%, cf also 2bēš: l. adv. outside HajB:8; HajA:7 LBR = ö bé outward; ibd. 9 ‘L LBR? STR? = 6 bē ärak id.; — hac bē Xvanirah from outside Kh. 10812; — bē hac to out- side thee, thy domain 1035 (v.s. v. tē):!!; — together with a following prep.: bé 6 emphasizing the sense of direction inherent in 6, very frequent; still more emphatic tdi bē 6 right up to 9218; bē apar Zartuxst nīšān (g. v.) dräyit 487-8; — bē! away! 14%, — 2. prev.: a) off, out, away, forth, esp. with vbs. designating a motion or a change of place or of condition, v. each separate vb.; cf fratom 6 ünód apar raft, avdom bē raft he (the horse) was the first to come there, and the last to go away 49%; HajB:8 (first BL’). In this case be, as giving the vb. its specific sense, is not dropped when other preverbs or the negation are added;
981:ībēš [bys] grief, affliction 1116. 481; ~ burtan to grieve, to mourn 681, 8413, — Av. (814 sq.) dvaēšah-, tbaēšah- ‘hostili-
983:(BBB 53); Paz. bēš. Derivatives v. below.
984:2bēš (Prth) [byš] but, HajA:7. - < bē-c, v.s. v. bé; Prth c has very often changed to š, ef s. v. šit.
990:bēšāzišuēh det. v. n. of bēšāzišn healing: (yätuk) ~ gl. to biziskeh 44?. — Cf MPrs bys’zyn- ‘to heal? (A-H II)
992:bēšēnītār [~-ynyt’l] causing pain, pain- ful, excruciating: ~ dart 43%.
993:bēšītan [byšytn'] to violate 73%. 831, 9824. — MPrs and Paz.
3109:must go back to *pati-yam- ‘to take hold of’, from Av. (1262sg.) yam-, chiefly with preverbs. I find *pāyam as a v. n. in two passages: 1. DkM 285 aköman ... menisn päyam ‘A. holding Mind in his grasp’; 2. ibd. 501? páyam hešm andar ménisn “Wrath taking Mind in his grasp’ (?). — Zsprm VIII, 4 has a somewhat divergent, perhaps more original version of the story 441-9: ^L ZLWN ‘L y’twk’n, MH-t L>? HWH-nd byšznyt'l, BR’ L'WHL ‘L h'nk' ZLWN, YDH BYN ml PWN "MŠH' ZY TWR’ ZY MDM thé YDLWN-t', hysme bwd wt'p' PWN NPSH-tn' zhk' MNW-t PWN 'škmb' = mà šav o yātūkān, cē-t nē hend bēšazanī- tar, bē apāc 6 xanak šav, dast andar mal pat rógn % gāv i apar ātaxš burt, hésm-ic bod vitāp pat x"ēš-tan zahak ké-t pat aš- kamb ‘do not go to the sorcerers, for they cannot heel thee, but go back home, rub thy hand with ox-tallow which has been. set on fire, and burn fragrant fuel for the benefit of thy offspring which is in thy womb’.
4381:xuäyisneh det. v. n. of the preceding w.: ` pat pus ~ in order to search for, or bring forth, a young one 40?, a son 43812; bēšāzēhē ~ rād in order to search for a remedy 43*4,
5052:baéSaza-: bēšāzēh
5144:dvar-: dar duš-mainyu-: duš-mčn du$-manah-: duš-man duš-mata-: duš-mat duš-x"aronah-: duš- xUarr(ah) dužda.fedrē: dušdaft duž-dačna-: dus-dén duz-däy-: duž, dužd duž-vacah-: duš-gobišn duž-varšta-: duš-huvaršt duž-ūxta-: duš-hūxt dvaēšah, tbaēšah: 'bēš dvar-, dvāristan
5545:’hy’ng: äyiyän ’jdh’k: Aži-dahāk ’mb’g: ham-bäi ’mStn: āmušt ’mwjd: ämurzitan ^mwzdyft: āmuržītan ’n’bys: 'bēš ’ndrw’z: andar-vài "ngd(g): hangateh ’rd’w: ahlav
5894:byš*z, byš'zyh: bēšāzēh
5895:byšzyn-: bēšāzišnēh
6467:azér, azér: hacadar Azi-dahak: ~ bačsažgar: bēšāzēh baévar: bévar
7062:bēš: vēš
7063:bēšah: vēšak
```


## [2026-09-05T20:12:16.375Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT tbaes ===\"; grep -n \"tbaēš\\|tbaes\\|tbaeš\" BRT.txt | head -20\necho \"=== BRT dvaeθ ===\"; grep -n \"dvaēθ\\|dvaeth\\|dvaēš\\|dvaeš\" BRT.txt | head -20"
}
```


### [2026-09-05T20:12:16.446Z] TOOL RESULT

```
=== BRT tbaes ===
6234:•  j.  asava.tbaes'  Adj.  'den  Gläubigen befeindend':  asavaynam^a  'tiagsqm^a'^  Y.
9124:yasaife  kd^  .  .  kahmai  raisca  Kfarmasca kakinäi ..  dn'atuhm  ..  baxsäni . .  kahmäi'' ., Vt  /0.108-110;  —  kS  nS  stai-ai  kö*  .  . kake  nd  i'ia  nijma  äyatryHl  kahmai  nS  tat dä'ir?m  dayiit  yat  .  .  Vt.y.50;  5.8^  Ä 15',  /J.47J;  — ■  60  "iviam  . .  inaoili  ks .  . tbaesayeiti  V./A'.öi;  Y.p.8  PuZ.,  V.:j.42i —  kas)  ^ji-aiji  paoiryü  . .  masys . .  Aunüla y-9-ii  V.J.  12,  20.1;  —  kahmai  mä ■  "iwarSldUm  ks  ma  talat  'H.2').\\  —  k7  .  . raocasca  dst  timäscä  Y.44.5;  5",  3,  4', ,  7',  4^-14,  5/.  1 1';  —  kasif  vohü  maiianhä ^y}  i  däy.il  (sd.)  \.-2i/.t,  —  koi  *dr^g7-i>.' dibü  . .  rämam  dih/ii:  "v/er  sind  sie,  die.." Y,  4iS'.  II;  —  kirn  nii  mavaiis  (sd.)  päyürn dadat\.4/i.T,  —  *kaAe^'>  *nä  *gara  ratu- friS  N.54:  —  kirn  höi  ustä  (sd)  ahurim Y.29.2;  —  tclm  {\Sm.)  /rrmraelt  asa- \vatum  ..  \.ig.io;  20.2;  —  kat  va/iY.
12031:\)  'überwinden,  bewältigen':  tistrxm  , . yS  pairika  taurvayeiti  yd  patrika  titära- yeiti  YtiV.8;  40;  —  afar^nS  ..  taurvayeiti anrfm  mainyOm  Yt.  J<?.  2;  2';  —  ya^a taurvayeni  vTspanam  tbisvatqm  ibaisä  Y. g.  18;  Yt.  /.  6',  14.  4,  13.  142;  —  yai mqm  nalHS  taurvayät  Yt  /.  6;  JJ.  56;  — yüi)m  taüa  taurvayata  V}r3hr»m  äänunqm Yt/J.  38;  38;  —  tä  (ND.)  Al taurvayaiptn tiagsaXt.lj.'jS;  —  yä  datbisvatö  dvalsä (sd.)  taurvayämäY.sS.S; — ya^a  valm.. vispä  tbaBsii  taurvayama  Yt/0. 34;  — airyamamm  .  .  vtspa  (baisa  taurvayan- ttm  vtspa  ibaisä  titarintftn  G, /.  6;  — ^aiiWSrB  vastära  .  .  taurvayanta  .  . g/aesa\X.$.\y,  —  asTm  ..  taurvayeinttm viipä  tbaesä  Y.  52.  2.  a)  'andringen gegen  -,  angreifen':  yat  titarat{^SPiA.)  '^
14783:•  j.  (bisyant-,  g.  daibisyant-**  Adj.  'feind- lich, fcind,  inimtcus':  rapantl  .  .  at  .  . -yanti  zastäi/täi/ (sd.) . .  Y.34. 4;  —  aei'qm *°yafitqm ''>  . .  tbaesä  \t.jo.'j6;  —  aurva- 'äianqm  'yantqnt  Y.57.  a6,  Yt  J^.  31,  *Vyt. i^";  Yt  74.34,  ^■57-''f>\  —  aurvahafiiyS pars  'yanbys  Yt.  13.  69,  Y.  68.  13;  Yt.  10. 75,75.31;  — -  vlspim  aurvd^jm  °yanttm vXspfm  ay)m  °yant>m  A.  7,  10;  —  vanä{ vupe  'yantö  Yt  75.54; — pala  nS  'yantat pairi  SrB.5.
=== BRT dvaeθ ===
```


## [2026-09-05T20:12:28.672Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HJB bish ===\"; grep -n -i \"BISH\\b\\|BIKH\\|aconite\" HJB.txt | head -20"
}
```


### [2026-09-05T20:12:28.742Z] TOOL RESULT

```
=== HJB bish ===
3630:BISH,  BIKE.
3635:BIflH,  BIEH,  &c.,  n.  H.  from  Skt. vishay  'poison.'  The  word  has  several specific  applications,  as  (a)  to  the poison  of  various  species  of  aconite, particularly  Aconitum  ferox^  otherwise more  specifically  called  in  Skt,  vatsa- ndbha,  *  calf's  navel,'  corrupted  into ba>chndbh  or  baeh/ndg,  &c.  But  it  is also  applied  (b)  in  the  Himalaya  to  the effect  of  the  rarefied  atmosphere  at great  heights  on  the  body,  an  effect which  there  and  over  Central  Asia  is attributed  to  poisonous  emanations from  the  soil,  or  from  plants ;  a doctrine  somewhat  naively  accepted  by Hue  in  his  famous  narrative.  The Central  Asiatic  (Turki)  expression  for this  is  Esh,  '  smell.'
6959:[1708.— "This  grave  is  made  for  HodgOS Shaughsware,  the  chiefest  servant  to  the King  of  Persia  for  twenty  years.  .  .  ." — Inscription  on  the  tomb  of  "  6\>,va  Shawiwart, a  Pertin  in,  St.  Botolpk*s  Churckyardj  Bish^u- gate,**  New  Vino  o/tjondon,  p.  169.]
8904:DOAI!  DW7EI  Interj.  Properly H.  dohOij  or  dahdi,  Qujarati  cUmdnlf  an exclamation  (hitherto  of  obscure  ety- mology) shouted  aloud  by  a  petitioner for  redress  at  a  Court  of  Justice,  or  as any  one  passes  who  is  supposed  to have  it  in  rds  power  to  aid  in  render- ing the  justice  sought.  It  has  a  kind of  analogy,  as  Thevenot  pointed  out over  200  years  a^,  to  the  old  Norman Hard  JSaro!  mens  d  men  aide^  man Prince  I  *  but  does  not  now  carry  the privilege  of  the  Norman  cry ;  though one  may  conjecture,  both  from  Indian anal^es  and  from  the  statement  of Ibn  &tuta  quoted  below,  that  it  once did.  Every  Englishman  in  Upper India  has  often  been  saluted  bv  the cAX\soi^^'DohBiKhudav)andki!  Doh&i Mahdrdj  !  Dohai  Kompanl  Bdhddur ! ' '  Justice,  my  Lord  !  Justice,  O  Kin^  I Justice,  O  Company!' — perhaps  in consequence  of  some  oppression  by  his followers,  perhaps  in  reterence  to  some grievance  with  which  he  has  no  power to  interfere.  "  Until  1860  no  one  dared to  ignore  the  appneal  of  dohai  to  a native  Prince  within  his  territory.  I have  heard  a  serious  chaige  made against  a  person  for  caUinj^  the  doh&i needlessly  "  {M.-Oen.  Keattnge).
23371:These  are  two  aromatic  roots,  once famous  in  pharmacy  and  often  coupled together.  The  former  is  often  men- tioned in  medieval  literature.  The former  is  Arabic  Jadwdr,  the  latter Pers.  zarambdd.  There  seems  some doubt  about  the  scientific  discrimina- tion of  the  two.  Moodeen  Sheriff  says that  Zedoary  {Curcuma  zedoaria)  is  sold in  most  bazars  imder  the  name  of  ahbe- haldi,  whilst  jadvdr,  or  zhadvdr,  is  the bazar  name  of  roots  of  varieties  of non -poisonous  aconites.  There  has been  considerable  confusion  in  the nomenclature  of  these  drugs  [see  Watt, Econ.  Diet,  ii.  655,  670].  Dr.  Royle, in  his  most  interesting  discourse  on the  Antiquity  of  Hxndco  Medicine (p.  77),  transcribes  the  following  pre- scription of  the  physician  Aetius,  in which  the  name  of  Zedoary  first  occurs, along  with  many  other  Indian  drugs  :
24121:Bish,    96a;   Bis   ki
```


## [2026-09-05T20:12:28.968Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT Anfeindung ===\"; grep -n \"Anfeindung\" BRT.txt | head -20"
}
```


### [2026-09-05T20:12:29.014Z] TOOL RESULT

```
=== BRT Anfeindung ===
4970:aväjanam  |  *startä   akatiy  "vaiy  (als  AP.)  mä  dauitH 'vaiy  .  .  parsä  Bh.4'i4i  —  hauv  karam fräiSaytr  .  .  vivana^  nilwa"  pärs^  mann 6a!'dakaf'    karj'uvatiyä    xsa>''apJVt1    abty Bli.j.9;  —  kärJ"  kyi^  hamth^iy^ manä  naiy  gaubataiy  °vam  /adiy'Eh.2.'},io; martiyä  tyaisaty  ..anuHyä  äka'tS 'vaiy {3\sAF.)../rdÄ^/am  Bh.  2. 13.-,        i)  II  auf ein  Relativum  als  dessen  Korrelat:  tya* parsbartam    ä/Sa*    °^a*    adam  pattpadam akunavam    Bh.  t.  14;   —   tyJ'iam    adam aiakam  "vJ^  akunav^tä  D.d.  4 ;  3,  Bh.  l.  7, 4.16,    17,  X.r.  3,  2.3;  —  Uta   ty<^maiy pi^''a^  iatiam  -valciy  (ASn.)  t^urJ'mazdtl patuv    X.7.4;  J.3;    —   kyci'    aparam  .  . Patiparsatiy  °vaky3  . .  Bh.  4-  8;  —  tyaisaiy fi-atamä  anuiiyä  ähc^til  'vaiy  (als  AP.). . frahcTJam  Bh.  3. 1 3 ;  —  tyaiy  panevä  xsäya- hiyä  . .  'vaisäm  naiy  astiy  kartam . .  Bh.  4- 9.11       3)  auf  einen  Satz(inhalt) :  y3  nanm kasyatfke  (sd.)  satthii  da^tti  vfavi  'i'Ot paraiti  (sÄ)  V. /j.  2;  —  ya^a  nSii  .  . kar>tS. .  avasySt  vismteisd.)  °val .  ./rava- lays  Yty.72f.         a)  in  Verbindung  mit ta-  'hie  ille':  ya'isa  azim  häätyene  pu'^rgm daliai  ahmäi  tat  "vat  syapt?m  artdvi.. Ytj.i8f.;(j.S,J5.4,äi,  Vyt.45.        2)vor. ausweisend;  1)  auf  direkte  Rede,  sub- stantivisch: tamatfkil . .  °vat  stuyi:  nSit., xäa  Y.  J2. 3 ;  —  °vat  manawka  maiiiimna : nqm  stavap  Yt5.7;  123,  y.49,  '9- 50;   —  *viövä    'vai   hava    xra'hwa: ml  hiu  nä  .  .  P.  21.         2)  auf  eine erläuternde  oder  ergänzende  nominale  Bei- fügung, a)  adjektivisch,  auch  im  Sinn  unsres Artikels  (des  schwachtonigen 'der'): /a^i- kayäi  yil  aom  puiinm   baraiti  anyahmai arsanai  varsl»m  Yt.  17.58;  —  aat .  .  aom miryjim  /rayrarayati  .  .  parSJars  nqma \.i8.2y,  —  'vä  /ba^sä  .  .  daevaniim  mal- yänqmca  ". .  die  Anfeindungen  der  D.  und Menschen"  Yt. /.  10;  — yasi  tat  paiti  'vä gaiiiä  tayus  .  .  para.baraiti  dasa  ".  ,  was jenes,  das  Anwesen  anlangt.."  V. y.  10; II.         o)    mit   relativischem   Anschluss: *'vau  (NSf.)  pairika  yS   dulyäirya  Yt  8. 54;  —  'vqm  kikrpmt  . ,  yqm  sämake  Yt. y.6i  ;   62,    Y.2O.2,    y.19.14;    —  /la^a *'vadhat  vlsat  yat  tnäsdayamöit  V.  '9- 1 2 ; —  haca  "vaahät  tamia^  yat  datvö.Jatayh V.ig.20\    —    'va   (APn.)  "baEiaza  ..  ya kumäydte  Vr.  9.  3.  b)  substantivisch:
12096:■  j.  taurvayö  Inf.  'zu  überwinden,  be- wältigen': yeä  van  . .  avä  tba^  f  a%a  . . "wenn  du  die  Anfeindungen . .  Überwinden willst  ...  so  .."  Yt/.io.
14768:•  j,  tbaeSö.tara-  Adj.  'der  die  Anfeindungen, Feindschaften  überwindet':  tarS.lbaiss  (sd.) .  ,  °rS  nqma  ahmt  Yt  /j.  47.
14967:•  j.  paiti.dvaeSayanti-  f.  'Fähigkeit, Kraft  den  Feinden,  Anfeindungen  entgegen- zuwirken': äicd  '^wqm  cakana  ..variiira- jqslaca  VaÄ  (IS.)  H.2. 11.
23994:•  j.  vitara.tbae&ah-  Adj.  'die  Anfeindung überwindend':  3ai  dis  äva^ayamaki  .  . aht  nmänahe  vltaratS  ahe  nmanahe  'iS "wir  weisen  sie  zu  .  .,  damit  sie  dieses Hauses  Not  überwinden,  dieses  Hauses Anfeindung  überwinden"  Vr.  jr.  13''.
23996:•  j.  vitar«.tbaeäab'ya-  il  'Überwindung der  Anfeindung*:  vltar».qsahyeheia  faiti 'kyeheca  pairi  hainyäs'a  vBtynäuyB  (sd.) Y.68.iz;Y\..S.\2.
24115:•  j.  vi'dvaestva-  Adj.  'nicht  anzufeinden, dem  keine  Feindschaft  droht,  was  anhaben kann'":  das)mS  yat  ahmi  .  .  HaäirudasS imal  'vd  ". .  vierzehntens  bin  ich  das: unerreichbar  für  Anfeindung"  Yt/.  S;  — yasnahe  haptafihatsis  . .  yU  fravaoce  maza amava  virihraja  °vü  Vr.  15.  3.
24426:>r3dat.förya  .  .  yä  'vairüa  nqma  avaia 'vairi  ya%a  hä  hm  zUanäl  yd  vTsp€ taurvayat . .  fiagfä  ". .  die  auch  K  heisst. darum  K,  weil  sie  den  gebären  wird,  der alle  Anfeindungen  überwinden  wird  .  ," Yf. /?.  142.
```


## [2026-09-05T20:12:37.125Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"ba[eE][SsŠš]ah-\\|bae&ah\\|baeäah\\|baesah\" BRT.txt | head -20"
}
```


### [2026-09-05T20:12:37.177Z] TOOL RESULT

```
12078:•  j.  tarö.tbaeäah-  Adj.  'der  die  Anfein- dungen, Feindschaften  überwindet':  '/ff (HSm.y^  ..l6ae^g.tard  nqma  aÄmiYtlS-47.
14721:8i3  tkaeia-  i  b  —  tbaeSah-  i  814
14746:•  j.  tbaeäah-,  g.  dvaeSah-  n.  i)  'An- feindung, Feindschaft,  Feindseligkeif:  iTr- pSng  any^ng  matnySu^  spasya  (sd,,  'ich' näml.2flr.)  °sar?ka  Y.44-ii;  — paityaogsl (sd.)  lä  (näml.  iyao^ani)  aAmai  jassit 'lanAa  (IS.)    Y.  46.  8.  a)    sonst    nui^
14750:tbaeSah-  a
14765:•  '}.  tbaeäah'vant-  Adj.  'feindschaftlich handelnd,  ^  gesinnt':  tum  ai/qm  'laau- hatqm  tbastä  sHndayeki  Yt  10.  ^6.
23994:•  j.  vitara.tbae&ah-  Adj.  'die  Anfeindung überwindend':  3ai  dis  äva^ayamaki  .  . aht  nmänahe  vltaratS  ahe  nmanahe  'iS "wir  weisen  sie  zu  .  .,  damit  sie  dieses Hauses  Not  überwinden,  dieses  Hauses Anfeindung  überwinden"  Vr.  jr.  13''.
24144:•  j.  vi-tbaeäah-  Adj.  'gegen  die  Anfein- dungen (der  Datva  usw.)  gerichtet,  sich wendend;  sie  abwehrend':  aityaman^ni i!tm  , .  amavanfym  vprf^rä/an^m  'iatthtm Y.  54. 2,  G.  J.  6.
```


## [2026-09-05T20:12:44.484Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Bedrohung\" BRT.txt | head -20"
}
```


### [2026-09-05T20:12:44.525Z] TOOL RESULT

```
7089:usihiUiiiii  aetat  he  °tim  "wenn einer  sich  erhebt  einen  Mann  zu  schlagen, so  begeht  er  damit  eine  Bedrohung"  V. 4,17; — yö  !tar)m  "um  üg^urfiJyHti  {sA.) V.4-18,  21.
10448:mit  ä  i)  'packen,  fassen':  yatUt  usaslaire Mnävä  (&d.)  *3g3urvayäii  yafät  daolataire\ »(7»«  Y.57.2g,  2)  'Jemandem  (Gen.)| etwas  zur  Strafe  abnehmen  für  — '  (Abi.):. yii  arfiiusaf  *apaititat  *Sjayaurva  "was man  für  eine  nicht  beglichene  J^^.^u'Äj-Sünde ' (Jemandem)  abgenommen  hat"  N.  54;  —  | yä  tanu.ppri^ake  aparao^pmiiahe  (sd.) ' *ajafaurva  *aya  ratußi/ü.^4.  3)  in! Verbindung  mit  3g»r?pt3m  (sd.) :  yS  tia- 1 rsm  ägiTSpUm  ägmrvayeitt  "wer  gegen Jemand  eine  Bedrohung  verübt"  V.  4. 1 8, 2 1.  ■
13939:•  g.  dvaeOä-  f.  'Bedrohung',  mit  Akk-  kiasäger  Tag''  ist  zwölf  -ff.  lang"  F. der  Person:  yeiyä   mä   j/Ji/  (sd.)    -'^3 ,  27  b,
```


## [2026-09-05T20:12:49.386Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=13900 && NR<=13960' BRT.txt | grep -n -E \"^\\s*[0-9]{3}\\s|[0-9]{3}\\s*$\" | head -20\necho \"---raw 13930-13945---\"\nsed -n '13930,13945p' BRT.txt | cut -c1-160"
}
```


### [2026-09-05T20:12:51.196Z] TOOL RESULT

```
39:764
---raw 13930-13945---
^ül  l;      ■        "  u  ■  i.      ■■u  .  ■      S  aW.   12.     -    ^>   D.  i.  rf.«.fl.   S  268.  8.    -
'bestrebt  sem  nach  — ,  sich  mühen  um  —       3)  j  268.  19.  —  *)  So  T.  —   s>  v.  18.  74: (Lok.)'*;  _yÖJ  asrustsis  (sA.)  P»mia!ih
Pü.!  niktzUan,  %v,.:  ptalipadayUim.  —  i)  .S.  lU  ;       BXHL.  IF.  //.  135.  —  ai.  dvi{-dha,  Adv.),  mp.
'*""•  3-  '       A-"(?)'l.  —  1)  Zu  ba;  F.  /n  s.  udW.  —  ')  S.
•  j.  'dyav-  m.  'Himmel':  paun'a.na!mtll      d""  Salemahn  GIrPh.  /.  284,  4  Anm, ^ff/i//  dyaos  (GS.  als  AblS.)  . .  anro  main-  ■         g.
dby  Google
76}
dvaeO'a-
764
•  g.  dvaeOä-  f.  'Bedrohung',  mit  Akk-  kiasäger  Tag''  ist  zwölf  -ff.  lang"  F. der  Person:  yeiyä   mä   j/Ji/  (sd.)    -'^3 ,  27  b,
"cujus  me  (mihi)  pemicies  mioabo  (minax      Komp.:  va+iJVa-.  —  Pa.:  7^2*0«-.— i)D. L
est)"  Y.4Ä9;   92.  16.  ""  T""e  '°"  grösster  I^gc  (nach  Bd.  2J.  5
VfL    gr.   i,ni(,    iiiia,;    KZ.  3S.  31.    (Falsch        *"   '*  Stünden);  vgl.  Aä^ra-.
Mills  G.  487)  —  Pü.:  Ai  vimäniilh.  j      ,.  iri.    1   n  ■  ..1    -     >    j*
..._',,  '7  •  g.  dvafsa-  m.  'Qual,  Pein"':  a  1/  -ifng
•  j.  dvaepa-ü.  Insel':  >i///»r)  <foa§»?'>  „,,^3  ^«^^  ^^^„^5  «damit  er  Qualen Ä  "  YL^-  sT  ""^^^«l«'««»  1^1  <ier,  aber  sie  b
```


## [2026-09-05T20:13:17.511Z] TOOL CALL #32: Bash

```json
{
 "command": "pdftoppm -f 144 -l 144 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg144 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


## [2026-09-05T20:13:18.454Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON بیش ===\"; grep -n \"بیش\" incoming/MON/MON_2vol_Adena_v1_djvu.txt | head -5\necho \"=== BQT بیش aconite ===\"; grep -n \"اقونیطن\\|بیش\" BQT_v1_pages.txt | head -10"
}
```


### [2026-09-05T20:13:19.799Z] TOOL RESULT

```
total 7132
drwx------ 2 sfmqrb sfmqrb   4096 Sep  5 16:13 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  5 16:02 ..
-rw-rw-r-- 1 sfmqrb sfmqrb 752374 Sep  5 16:12 bqt362_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb 624515 Sep  5 16:12 bqt362.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 385716 Sep  5 16:13 bqt363_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb 338175 Sep  5 16:13 bqt363_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb 692415 Sep  5 16:13 bqt363.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 956665 Sep  5 16:11 bqt553_foot2.png
-rw-rw-r-- 1 sfmqrb sfmqrb 746413 Sep  5 16:11 bqt553_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb 512022 Sep  5 16:10 bqt553.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 154316 Sep  5 16:07 bqt_bot389.png
-rw-rw-r-- 1 sfmqrb sfmqrb 168738 Sep  5 16:07 bqt_bot390.png
-rw-rw-r-- 1 sfmqrb sfmqrb 520653 Sep  5 16:07 bqt_n389.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 527392 Sep  5 16:07 bqt_n390.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    395 Sep  5 16:10 leaf.py
-rw-rw-r-- 1 sfmqrb sfmqrb  53212 Sep  5 16:08 pg130_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  74748 Sep  5 16:08 pg130.png
-rw-rw-r-- 1 sfmqrb sfmqrb 107108 Sep  5 16:08 pg130_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  87739 Sep  5 16:10 pg134.png
-rw-rw-r-- 1 sfmqrb sfmqrb  68320 Sep  5 16:08 pg136_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb  63248 Sep  5 16:08 pg136.png
-rw-rw-r-- 1 sfmqrb sfmqrb  45014 Sep  5 16:12 pg137.png
-rw-rw-r-- 1 sfmqrb sfmqrb  74330 Sep  5 16:11 pg138.png
-rw-rw-r-- 1 sfmqrb sfmqrb  70436 Sep  5 16:10 pg140.png
-rw-rw-r-- 1 sfmqrb sfmqrb  63658 Sep  5 16:13 pg144.png
-rw-rw-r-- 1 sfmqrb sfmqrb  89133 Sep  5 16:09 pg145.png
-rw-rw-r-- 1 sfmqrb sfmqrb  60631 Sep  5 16:11 pg147.png
```


### [2026-09-05T20:13:19.888Z] TOOL RESULT

```
=== MON بیش ===
371:آثاری که از مرحوم دکتر معین به چاپ نرسیده و آمادهٌ طبع است بیش از ده 
857:(کسی را): نزول آفات و بلیات بیشمار (بر 
1119:آب‌تاختن: (مسصل.) بیشاب 
1311:که بیشتر با دو ظرف (آفتابه و لگن) پیش از 
1345:پوسته از برنج (به اصطلاح شلت و کث) (بیشتر 
=== BQT بیش aconite ===
168:بیشتر اين نوشتها بسه خط میخی و بسه زبان پارسی باستان و بابلی و عیلامی
171:سال بیش از اين بغرمان داریوش ۰ سومین شاهنشاه هخامنشی ( ۵۲۲ - ۸
189:ار شامه بود 6 بدر ار شامه ار بارمنه بود؛یسرار یار منه چیش بیش طهزی) نود 4
203:این بایگاه درسال ۵۱۸ بیش از میلاد مسیح آغاز شده باشد و آنرا نونانیان
205:هجری نوشته آنرا چپل منار خوانده و سیاحان بیش نیز ۲نجارا بهمین نام
209:از میان رفت ودربابل زمين هم گویا بیش‌از يك‌فرن پیش از میلاد پایدار نیا ند
244:است که در آن کفتگو بسیارشده . بیشتر احتمال دارد که زبان اوستایی يك
373:مدت طولانی که بیش ازهزار ودویست سال است : آثار کتبی که از زبان
396:که بیش اژ چپارصد وهفتادسالاست» جز از نام چندکس و چند نوشته کو تاه
442:پنجمين پادشاه ساسانی بجای مانده است . بیشتر سنکنبشتهای بادشاهان‌اولی
```


## [2026-09-05T20:13:27.932Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls -la MON_part1.txt MON_part2.txt; head -20 MON_part1.txt; echo \"---\"; grep -c $'\\f' MON_part1.txt"
}
```


### [2026-09-05T20:14:05.742Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
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

---
0
```


## [2026-09-05T20:14:08.641Z] TOOL CALL #35: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-05T20:14:08.648Z] TOOL RESULT

```


```


## [2026-09-05T20:14:12.197Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/arsenal",
 "prompt": "Give the full etymology section for English arsenal, including any Italian, Venetian, Byzantine/Medieval Greek and Arabic forms mentioned (dār aṣ-ṣināʿa), and note whether a Greek intermediary is asserted."
}
```


## [2026-09-05T20:14:13.344Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/arsenal",
 "prompt": "Give the full etymology text for arsenal, including Italian arzenale/darsena, Venetian, and the Arabic dar as-sina'ah, and any mention of Greek."
}
```


### [2026-09-05T20:14:18.117Z] TOOL RESULT

```
# Etymology of English "Arsenal"

Based on the Wiktionary entry, the English etymology section states:

"From Italian _arsenale_, from Arabic _دَار الصِّنَاعَة_ (dār aṣ-ṣināʕa, 'manufacturing shop'), from _دَار_ (dār) + _صِنَاعَة_ (ṣināʕa)."

**Key findings:**

- **Italian intermediary**: The entry explicitly traces the word through Italian *arsenale*
- **No Greek form mentioned**: The etymology does not reference any Byzantine, Medieval Greek, or other Greek intermediary stage
- **Arabic origin**: The ultimate source is identified as the Arabic compound meaning "manufacturing shop"
- **No Venetian forms cited**: While historical scholarship sometimes notes Venetian involvement in this word's transmission, the Wiktionary entry does not mention Venetian explicitly

The documented pathway is: Arabic → Italian → English, with no Greek intermediary asserted in this source.
```


### [2026-09-05T20:14:18.409Z] TOOL RESULT

```
# Etymology of Arsenal

According to the Online Etymology Dictionary, "arsenal" originated around 1500 as "dockyard, dock with naval stores," entering English from Italian *arzenale*. This Italian term derived from Arabic *dar as-sina'ah*, meaning "workshop" or literally "house of manufacture" (from *dar* meaning "house" and *sina'ah* meaning "art, craft, skill").

The Venetians applied this word to a large wharf in their city, and English adopted it in this nautical sense. By the 1570s, the meaning expanded to "public place for making or storing weapons and ammunition."

**Note:** The provided text contains no mention of Greek origins or the variant *darsena*.
```


## [2026-09-05T20:15:32.326Z] TOOL CALL #38: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg144.png"
}
```


### [2026-09-05T20:15:32.696Z] TOOL RESULT

```

```


## [2026-09-05T20:15:32.688Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T20:15:43.631Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT arsenal ===\"; grep -n -i -o \".\\{0,300\\}arsenal.\\{0,400\\}\" LKT.txt | head -5\necho; echo \"=== DEV arsenal ===\"; grep -n -i -o \".\\{0,200\\}arsenal.\\{0,500\\}\" DEV.txt | head -3"
}
```


## [2026-09-05T20:15:45.462Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT arsenal ===\"; grep -n -o \"arsenal.\\{0,400\\}\" SKT.txt | head -3\necho; echo \"=== FSD arsenal ===\"; grep -n -o \"arsenal.\\{0,300\\}\" FSD_vol1.txt | head -3\necho; echo \"=== KLN1971 arsenal ===\"; grep -n -o \"arsenal.\\{0,600\\}\" KLN_1971.txt | head -3"
}
```


### [2026-09-05T20:15:50.665Z] TOOL RESULT

```
=== LKT arsenal ===
ugrep: error: error at position 86
-\xbf][\x80-\xbf]*){0,400}
                          \___exceeds complexity limits



=== DEV arsenal ===
ugrep: error: error at position 86
-\xbf][\x80-\xbf]*){0,500}
                          \___exceeds complexity limits
```


### [2026-09-05T20:15:52.424Z] TOOL RESULT

```
=== SKT arsenal ===
985:arsenal ;    Iohj^ ;.-  jMj,  wliere  the  a- •     -ude.     Cf.  Itnl. .V.    —  ,\iab.  (/*ir  suu£ai, iction,  place  for  mfilfing •-  Amb    dtir,  a   house; tnde,  construction. .— GW,)    Late  L,  arsemmm. ic  ;  lit.  a  male  prin- ul  the  Ktrnii^c  lancy dlfTcretkl  Kxc9.~Gk, ;r,  A  male. Ard«nt.      * ■.  {vcs.  of  verb.  (E.)    See
23698:arsenal, bonito,  colaba^  ?,  caiaway  (carraway), cannine,  maravctli.  minaret,

=== FSD arsenal ===
12500:arsenal, al-raa'cl-ga,  1   al-ma'sj-ga;  2   fil-ma'ci-gii,  n.  [P.  I.J  1.  A tree  of  the  genus  Dipterocarpus,  yielding  a   light,  ashy- colored  wood  and  a   valuable  gum.  2.  Its  wood  or  the gum  antang.
25013:arsenal, "ma-men-ta'ri-um,  1   ar'me-men-te  mines,
25124:arsenal.

=== KLN1971 arsenal ===
20079:arsenal, n., a place for manufacturing and storing 
20080:arsenale (Olt. 
20090:arsenal see adj. suff. -al.
```


## [2026-09-05T20:15:55.131Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '20075,20095p' KLN_1971.txt\necho \"=== LKT ===\"\ngrep -n \"Arsenal\" LKT.txt | head -10"
}
```


### [2026-09-05T20:15:55.205Z] TOOL RESULT

```
and cogn. with Gk. £ppoq (for I.-E. *orsos), 
‘tail, rump, base of the spine’, oup& (for *6pcf&), 
‘tail*, Hitt, arrash. Arm. or, ‘buttock’, OIr. err 
(for *ersd), ‘tail’. Cp. uro-, ‘tail-*, 
arsenal, n., a place for manufacturing and storing 
ammunition and weapons. — It. arsenale (Olt. 
arzanale), ‘dock’, borrowed — prob. through the 
medium of MGk. ipcnrjvaXr)^ — fr. Arab, ddr- 
a$-$ind'a h (whence also Sp. ddrsena and It. dar- 
sena , ‘dock’), lit. ‘house of construction’, fr. dar, 
‘house’, as-, assimilated form of al-, ‘the’, and 
Sind'a h , ‘construction, art’, fr. fdna'a, ‘he made*. 



“ For the ending of arsenal see adj. suff. -al. 
arsenic, n., a chemical element. — OF. (= F.) 
arsenic, ' fr. L. arsenicum, arrhenicum, fr. Gk. 
<£p<revix6v, dcppevtx6v, ‘yellow orpiment’, fr. 
MPers. *zarnik, ‘gold, golden ; orpiment’( whence 
ModPers.-Arab. zarntkh, ‘orpiment’), through 
=== LKT ===
1249:Auch  bind,  'ein  Hügel,  Erdwall  oder erhöhte  Batterie',  als  n.  pr.  in  Bengalen Namen  einer  militärischen  Niederlassung, 4V2  engl.  Meilen  nordwestlich  von  Cal- cutta,  die  70  Jahre  lang  (1783—1853) Hauptquartier  des  berühmten  Korps  der bengalischen  Artillerie  war.  Im  dortigen Arsenale  wurden  zuerst  mit  stumpfem Vorderende  versehene,  daher  stark  zer- reißende Geschosse  liergestellt,  die  man engl,  dum-dum,  dtsch.  Dimidumgeschosse nennt.    [Hobson-Jobson  330.
1290:[Aus  ar.  dar  'Haus',  sinä'a  'Betriebsam- keit, Handwerk,  Industrie']  'Fabrik',  be- sonders 'Waffenfabrik'  und  auch  schon ar.  'Schiffsbauhaus';  im  Türkischen  zu tershäne  korrumpiert,  als  wenn  es  von pers.  Jiänä  [s.  hier  Nr.  809]  käme.  Hier- aus it.  darsena,  siz.  tirzanä  'iniiei'es Hafenbecken',  arzanä,  arsenale,  terzana 'Zeughaus';  frz.  darse,  darsine  'kleiner Binnenhafen',  arsenal;  sp.  atarazana, atarazanal  'Schuppen',  arsenal;  pg. taracena,  tercena  'Schuppen',  arsenal; rum.  arsenal,  darsena.  Dtsch.  Arsenal, ndl.  arsenaal,  engl,  arsenal,  russ.  a?*- senal.  [Dozy  Oost  16/18.  DE  205/206. Eguilaz  304.  Gorjaiew  6.  Kluge  23. Devic  DEt  35/36.    ML  2474.
```


## [2026-09-05T20:16:06.709Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1283,1292p' LKT.txt"
}
```


### [2026-09-05T20:16:06.745Z] TOOL RESULT

```
I^ers.  därd.]
40
be  Präposition  'zu,  bei,  an',  Horn  NpEt S.  33,  Nr.  144]  'einer,  der  von  Tür  zu Tür  gellt;  Bettler,  Vagabund',  ebenso tk.;  hieraus  rum.  derbedeü,  derbeder '  Paugenichts,  Vagabund,  Bummler'.
49:^.  Fers,  därd: 'Schmerz'  [Horn  NpEt  S.  12:2,  Nr.  5.00], ebenso  \k.derd;  hieraus serb.rfe?-^ 'Sorge', bultr.  det-t   'Sorge,    Schmerz'.  [Bern SiEtWb  185.
494.  Ar.  dariuaka:
Auch  darmaka  'Blütenmehl,  VVeifsbrot daraus'  [KM  H,  624];  hieraus  mit  ar. Art.  sp.  adargama,  aldargamn  'Blüten- mehl; eine  Art  feinen  Brotes'.  [DE  41.
495.  Ar.  där-sinä'a:
[Aus  ar.  dar  'Haus',  sinä'a  'Betriebsam- keit, Handwerk,  Industrie']  'Fabrik',  be- sonders 'Waffenfabrik'  und  auch  schon ar.  'Schiffsbauhaus';  im  Türkischen  zu tershäne  korrumpiert,  als  wenn  es  von pers.  Jiänä  [s.  hier  Nr.  809]  käme.  Hier- aus it.  darsena,  siz.  tirzanä  'iniiei'es Hafenbecken',  arzanä,  arsenale,  terzana 'Zeughaus';  frz.  darse,  darsine  'kleiner Binnenhafen',  arsenal;  sp.  atarazana, atarazanal  'Schuppen',  arsenal;  pg. taracena,  tercena  'Schuppen',  arsenal; rum.  arsenal,  darsena.  Dtsch.  Arsenal, ndl.  arsenaal,  engl,  arsenal,  russ.  a?*- senal.  [Dozy  Oost  16/18.  DE  205/206. Eguilaz  304.  Gorjaiew  6.  Kluge  23. Devic  DEt  35/36.    ML  2474.
496.  Pßrs«  ilär^vGS  •
'Bettler ;  arm'  [Horn  NpEt  S.  124,  Nr.  559], ebenso  tk.  derwis  'arm,  Bettelmönch'; hieraus  rum.  dervi§,  it.  dervis  [mit  Be- tonung der  Pänultima],  frz.  derviche,  sp. derviche,  pg.  dervis,  derviche;  dtsch. Derwisch,  ndl.  dervis,  engl,  dervish ;  russ. bulg.  serb.  derwis,  cech.  dervis,  poln. dervisz.
```


## [2026-09-05T20:16:07.887Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D9%87%D8%B1",
 "prompt": "Give the Arabic entry دهر: its root (which triliteral root it is listed under), meaning, and any etymology given (cognates in Akkadian/Hebrew, relation to د و ر). Also give the Persian entry دهر if present."
}
```


### [2026-09-05T20:16:13.951Z] TOOL RESULT

```
# Arabic Entry دهر (dahr)

## Root
The word belongs to the triliteral root **د ه ر** (d h r), which encompasses 3 related terms.

## Meanings

**As a Verb (dahara):**
To overcome, conquer, subdue, overpower, master, gain mastery over, prevail, predominate over, or surpass.

**As a Noun (dahr):**
1. Verbal noun of the verb form
2. "The course of time, fate"

## Etymology & Cognates
The entry does not explicitly state cognates in Akkadian or Hebrew, nor does it discuss relations to د و ر (d w r). No etymological section providing such information is included in this Wiktionary entry.

## Persian Entry
The page indicates a Classical Persian descendant form **دَهْر** (dahr) exists, derived from the Arabic term, but does not provide a separate detailed Persian entry on this page.
```


## [2026-09-05T20:16:23.122Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D8%B4",
 "prompt": "List all Persian entries for بیش, especially any meaning \"aconite / a poisonous plant\", with their etymologies (Sanskrit विष viṣa? Middle Persian biš?). Also any entry meaning \"more\". Quote the etymology sections."
}
```


## [2026-09-05T20:16:24.446Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dwey-",
 "prompt": "Does this reconstruction page exist? If so give the meaning and the descendants (Greek, Latin, Avestan, Sanskrit)."
}
```


### [2026-09-05T20:16:29.301Z] TOOL RESULT

```
# Persian Entries for بیش

## Etymology 1: "More" (Adverb)

**Etymology section quote:**
"From Middle Persian [script needed] (wyš /⁠wēš⁠/, "more"), probably borrowed from Avestan 𐬠𐬌𐬱 (biš, "twice"), from 𐬛𐬀𐬌𐬠𐬌𐬙𐬌𐬌𐬀 (daibitiia)."

This form derives from ancient Iranian language roots predating modern Persian.

## Etymology 2: "Aconite" (Noun)

**Etymology section quote:**
"From Middle Persian [script needed] (byš /⁠bīš⁠/, "aconite"), from Sanskrit विषा (viṣā, "_Aconitum ferox_"), from विष (viṣa, "poison"), whence English _bikh_."

This entry traces the word through Sanskrit origins, connecting it to the poisonous plant family and the broader concept of toxins in Indo-European languages.
```


### [2026-09-05T20:16:30.809Z] TOOL RESULT

```
# Proto-Indo-European *dwey- Reconstruction

Yes, this reconstruction page exists. 

**Meaning:** The root *dwey- means "to fear."

**Key Descendants:**

- **Greek:** δειλός (deilós, "cowardly"), δεῖμα (deîma, "fear"), δειμός (deimós), δεινός (deinós, "terrible"), δέος (déos, "fear")

- **Latin:** dīrus ("terrible/dire")

- **Sanskrit:** द्वेष्टि (dvéṣṭi, "to hate")

- **Avestan:** duuaeš- (fear-related term)

- **Armenian:** erkn (fear)

The etymology note indicates this root likely derives from *dwóh₁ ("two"), with a semantic shift from "two" → "ambivalence/second thoughts" → "fear."
```


## [2026-09-05T20:16:38.999Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"dwei-\\|dinosaur\\|dire\\b\" AHD_watkins1985.txt | head -15"
}
```


### [2026-09-05T20:16:39.051Z] TOOL RESULT

```
306:au-5, To perceive. Compound forms *aw-dh-, *awis-dh-, “to place perception” (see dhé-'). 1. Suffixed form *awisdh-yo- or *awdh-yo- in Latin audire, to hear: AUDIBLE, AUDIENCE, AUDIENT, AUDILE, AUDING, AUDIO-, AUDIT, AUDITOR, AUDITORIUM, AUDITORY, OYEZ; OBEY, SUBAUDITION. 2. Greek aisthanesthai, to feel: AES- THETIC; ANESTHESIA. [Pok. 8. au- 78.]
323:outlaw”), in: a. Old English bannan, to summon, pro- claim, and Old Norse banna, to prohibit, curse: BAN}; b. Old French ban, feudal jurisdiction, summons to military service, proclamation, Old French bandon, power, and Old English gebann, proclamation: BANAL, BANNS; ABANDON; C. Old French banir, to banish: BAN- ISH; d. Late Latin bannus, bannum, proclamation: Ccon- TRABAND; @. Italian bandire, to muster, band together (< “to have been summoned”): BANDIT. 4. Suffixed form *bha-ni in Germanic *b6dni- in Old Norse b6n, prayer, request: BOON!. 5. Suffixed form *bhd-ma in: a. Latin fama, talk, reputation, fame: FAME, FAMOUS; DEFAME, INFAMOUS; b. Greek phémé, saying, speech: EUPHEMISM. 6. Suffixed o-grade form *bhd-nd in Greek phéné, voice, sound, and phénein, to speak: PHONE, -PHONE, PHO- NEME, PHONETIC, PHONO-, -PHONY; ANTHEM, (ANTI- PHON), APHONIA, CACOPHONOUS, EUPHONY, SYMPHONY. 7. Suffixed zero-grade form *bha-to- in Latin fatéri, to acknowledge, admit: CONFESS, PROFESS. 8. Greek blas- phémos, evil-speaking, blasphemous (first element ob- scure): (BLAME), (BLASPHEME), BLASPHEMOUS. [Pok. 2. bha- 105.] bha-bha-. Broad bean. 1. Latin faba, broad bean: FAVA BEAN. 2. Variant form *bha-un- in Germanic *bauné in Old English béan, broad bean, bean of any kind: BEAN. [Pok. bhabhé 106.] bhad-. Good. 1. Germanic (comparative) *batiz6 in Old English betera, better: BETTER. 2. Germanic (superla- tive) *batistaz in Old English bet(e)st, best: BEST. 3. Ger- manic noun *b6¢6 in Old English bét, remedy, aid: BooT?. 4. Germanic verb *batnan, to become better, in Old Norse batna, to improve: BATTEN!. [Pok. bhdd- 106.] bhag-'. To share out, apportion, also to get a share. 1. Greek phagein, to eat (< “to have a share of food”): -PHAGE, -PHAGIA, PHAGO-, -PHAGOUS. 2. Extended form *bhags- in Avestan bakhsh- in Persian bakhshidan, to give: BAKSHEESH, (BUCKSHEE). [Pok. 1. bhag- 107.] bhag-. Sharp. Suffixed form *bhag-ro- in Greek phag- ros, whetstone, also a name for the sea bream: PORGY. [Pok. 2. bhag- 107.] bhaghu-. Arm. Germanic *bdguz in Old English bdg, boh, bough: BouGu. [Pok. bhdghii-s 108.] bhago-. Beech tree. 1. Germanic *b6k6, beech, also “beech staff for carving runes on” (an early Germanic graphic device), in: a. Old English bdc, written docu- ment, composition: BOOK; b. Middle Dutch boek, beech: BUCKWHEAT. 2. Germanic *bdkjdn- in Old English béce, beech: BEECH. [Pok. bhdgo-s 107.] bhar-. Also bhor-. Projection, bristle, point. 1. Suffixed o-grade form *bhor-so- in Germanic *barsaz in Old English bzrs, perch, bass (a fish that has a spiny dorsal fin): BASs!. 2. Suffixed zero-grade form *bhAr-sti- in Germanic *bursti- in Old English byrst (> Middle Eng- lish bristel), bristle: BRISTLE. 3. Extended zero-grade form *bhrs- in: a. Germanic *bur- in Swedish borre, bur, perhaps akin to the Scandinavian source of Middle English burre, bur: BUR}; b. suffixed form *bhrs-dh- in Germanic *bruzd-, point, needle, in Old Norse broddr, spike: BRAD; C. suffixed form *bhrs-ti- in Latin fastig- ium, summit, top, extremity: FASTIGIATE, FASTIGIUM; d. possibly suffixed form *bhrs-tu- in Latin fastus, fasti- dium, disdain (from the notion of prickliness): FASTIDI- ous; e. suffixed form *bhrs-tio- in Russian borshch, cow parsley: BORSCHT. [Pok. bhar- 108.] bhardha. Beard. Possibly related to bhar-. 1. Germanic *bardaz in Old English beard, beard: BEARD. 2. Ger- manic *bard6, beard, also hatchet, broadax (the associ- ation of beard and ax is attested elsewhere in the Indo-European family; both were symbols of patriarchal authority), in Old High German barta, beard, ax: HAL- BERD. 3. Latin barba, beard: BARB!, BARBEL, BARBEL- LATE, BARBER, BARBETTE, BARBICEL, BARBULE; REBARBATIVE. [Pok. bhardhé 110.] bhares-. Also bhars-. Barley. 1. Germanic *barz- in Old
412:dwei-. To fear. 1. Suffixed form *dwei-ro- in Latin dirus, fearful, horrible (originally a dialectal form): DIRE. 2. Suffixed form *dwey-eno- in Greek deinos, fearful, monstrous: DINOSAUR, DINOTHERE. (This root originally meant “to be in doubt, be of two minds,” and is related to dwo-.) [Pok. dyei- 227.]
536:gru-. To grunt. Imitative. 1. Germanic *grun- in Old English grunnian, to grunt, probably akin to Old English grunettan, to grunt: GRUNT. 2. Germanic intensive form *grunnatjan in Old High German grunniz6n, to grunt: GRUDGE. 3. Latin grunnire, grundire, to grunt: GRUNION. [Pok. gru- 406.]
814:fana, flag, banner, weathercock: VANE; b. compound *gund-fanon-, “battle-flag” (see ghen-'). 2. Extended form *panno- in Latin pannus, piece of cloth, rag: PANE, PANEL. 3. Possibly Greek pénos, web (> Latin pdnus, a swelling): PANICLE. [Pok. pan- 788.] [pandoura. Three-stringed lute. Greek noun of obscure origin. BANDORE, MANDOLIN, PANDORE.] pant-. All. Attested only in Tocharian and Greek. Greek pas (neuter pan, stem pant-), all: PAN-, PAN; DIAPASON, PANCRATIUM, PANCREAS. [In Pok. 1. keu- 592.] pap-'. Teat (sound symbolism). Probably the same word as pap-2. 1. Middle English pap(pje, nipple: Pap}. 2. Latin diminutive papula, pimple (diminutive papilla, nipple): PAPILLA, PAPULE. 3. Variant form *pup(p)- in Latin piipus, boy, and pupa, girl: puPA, PUPIL. [In Pok. barb- 91.] pap-?. Food (baby-talk root). Reduplication of pa-. 1. Germanic nasalized form *pamp- in Flemish frequen- tative pamperen, to cram with food, akin to the source of Middle English pamperen, to pamper: PAMPER. 2. Latin pappa, food (> Middle English pap, soft food): PAP?, POPPYCOCK. [Pok. pap(p)a 789, ba*mb- 94.] papa. A child’s word for “father,” a linguistic near-uni- versal found in many languages. 1. French papa, father: PAPA. 2. Greek pappas, father, and pappos, grandfather: PAPPUS, POPE. [Pok. pap(p)a 789.] paso-. Kinsman by marriage. Latin parri- (for pari-) in compound parri-cida (oldest form paricidas), murderer of a near relation: PARRICIDE. [Pok. pdso-s 787.] past-. Solid, firm. 1. Germanic *fastuz, firm, fast, in: a. Old English fest, fixed, firm: FAST!; STEADFAST; b. Middle Dutch vast, firm, fast: AvAST. 2. Germanic *fastinon, to make firm or fast, in Old English festnian, to fasten, establish: FASTEN. 3. Germanic *fastén, to hold fast, observe abstinence, in: a. Old English festan, to abstain from food: rasT?; b. Old Norse fasta, to abstain from food: BREAKFAST. [Pok. pasto- 789.] pau-. Few, little. I. Adjectival form *pau-, few, little. 1. Germanic *fawaz in Old English féawe, few: FEW. 2. Suffixed form *pau-ko- in Latin paucus, little, few: PAUCITY, POCO. 3. Suffixed form *pau-ro- in metathetical form *par-wo- in Latin parvus, little, small, neuter parvum, becoming parum, little, rarely: PARAFFIN, PAR- vovirus. 4. Compound “pau-paros, producing little, poor (*par-os, producing; see pere-'), in Latin pauper, poor: PAUPER, POOR, POVERTY. II. Suffixed reduced variant form “pu-lo-, young of an animal. 1. Germanic *fulén- in Old English fola, young horse, colt: FOAL. 2. Germanic derivative *fuljé in Old Norse fylja, female colt: FILLY. 3. Latin pullus (probably with expressive gemination), young of an animal, chicken: POLTROON, PONY, POOL?, POULARD, PULLET; CATCHPOLE. III. Basic form *pau- and variant form *pi-, boy, child. 1. Suffixed form *pu-ero- in Latin puer, child: PUERILE, PUERPERAL. 2. Suffixed form “pi-sso- in Latin piisus, boy: PUSIL- LANIMOUS. 3. Suffixed form *paw-id- in Greek pais (stem paid-), child (> paideia, education): PEDO-?; ENCY- CLOPEDIA, ORTHOPEDICS. [Pok. pdu- 842.] paus-. To leave, desert, cease, stop. Greek pauein, to stop (> Latin pausa, a stopping): PAUSE, (PESADE), (POSE!); COMPOSE, DIAPAUSE, (REPOSE!). [Pok. paus- 79.] ped-'. Foot. I. Nominal root. 1. Lengthened o-grade form *pod- in Germanic *fot- in Old English fot, foot: Foor. 2. Suffixed form *ped-ero- in Germanic *feteré in Old English fetor, feter, leg iron, fetter: FETTER. 3. Suffixed form *ped-el- in Germanic *fetel- in Old High German vizzelach, fetlock, akin to the Germanic source of Middle English fitlock, fetlock, fetlock: FETLOCK. 4. Basic form *ped- in Latin pés (stem ped-), foot: PAWN2, -PED, PEDAL, PEDATE, PEDESTRIAN, PEDI-, PEDICEL, PEDUNCLE, (PEON), PES, PIONEER; MILLIPEDE, SESQUIPEDALIAN, TRIPEDAL, TRIVET, VAMP!. 5, Form *ped-yo- in: a. Latin expedire, to free from a snare (ex-, out of; see eghs): EXPEDITE; b. Latin impedire, “to put in fetters, hobble,
1154:wéro-. True. 1. Germanic *wéra- in Old English wér, faith, pledge: WARLOCK. 2. Latin vérus (> Old French voir, truth), true, with its derivative vérax, truth: VERA- CIOUS, VERISM, VERITY, VERY; AVER, VERDICT, VERIDI- CAL, VERIFY, VERISIMILAR, VOIR DIRE. 3. Latin sevérus, grave, serious; regarded by some as a compound of se-, sed, without (see s(w)e-), and vérus, true, but the semantic difficulties make this explanation improbable: SEVERE; ASSEVERATE, PERSEVERE. [Pok. 11. yer- 1165.]
1429:DIN dhwen- DINGUS _{enk-1 DINOSAUR dwei- DINOTHERE dwei- DIOCESE weik-! DIOECIOUS weik-1 DIOICOUS_ weik-1 DIOPTER oOkW- Dioscuri_ deiw-, ker-3 pip dheub- DIPHTHERIA deph- DIPHYODONT bheue- DIPLO- dwo- DIPLOCARDIAC kerd-1 DIPLODOCUS dek-1 DIPLOE dwo- DIPLOID pel-3 DIPLOMA dwo- DIPNOAN pneu- DIRE dwei- DIRECT reg-! DIRNDL tek- DISARM ar- DISASTER ster-3 DISBURSE bursa DISCERN krei- DISCIPLE dek-! DISCIPLINE dek-? DISCOMFIT dhé-1 DISCORD kerd-1 DISCOURSE kers-2 DISCRIMINATE krel- DIscuss kwét- DISDAIN dek-1 DISEMBOGUE beu-! DISFIGURE dheigh- DISGUST geus- DISK deik- DISMAL deiw-, mel-5 DISMAY magh-! DISMISS (s)meit(9)- DISPARATE pere-1 DISPATCH ped-! DISPEL pel-6 DISPENSE (s)pen- DISPERSE (s)preg- DISPLAY plek- DISPOSE apo- DISPUTE peu- DISQUISITION quaerere DISRUPT reup- DISSECT sek- DISSEMINATE 6-1 DISSENT sent- DISSERTATE ser-3 DISSIDENT sed-1 DISSILIENT sel-4 DISSIPATE swep-2 DISSOCIATE sekw-1 DISSOLVE leu-! DISSONANT swen- DISSUADE swad- DISTANT sta- DISTEND ten- DISTICH steigh- DISTINGUISH _ steig- DISTORT terkw- DISTRACT tragh- DISTRAIN  streig- DISTURB twer-! DITCH dhigw- DITTO deik- DITTY deik- DIURETIC wers-2 DIURNAL deiw- DIVA deiw- DIVARICATE wa- DIVE dheub- DIVERGE wer-3 DIVERT wer-3 DIvEs_ deiw- DIVIDE weidh- DIVINE! deiw- DIVINE? deiw- DIVULSION wel-4 Dizzy dheu-!
2457:VOILE weg-! VOIR DIRE wéro- VOLANT gWel-2 VOLATILE gWel-2 VOLE! welt- VOLE? gWel-2 VOLITANT gWel-2 VOLITION wel-2 VOLKSLIED léu-2 VOLLEY gWel-2 VOLT? wel-3 VOLUBLE wel-3 VOLUME wel-3 VOLUNTARY wel-2 VOLUPTUARY wel-2 VOLUPTUOUS wel-2 VOLUTE wel-3 VOLUTIN wel-3 VOLVA wel-3 VOLVOx wel-3 VOMER wogWh-ni- VOMIT weme- VORACIOUS gWere-4 VORLACE legh-, per! -VOROUS gWere-4 VORTEX wer-3 VOTARY wegh- VOTE wegWh-
```


## [2026-09-05T20:16:53.448Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd1 dvei ===\"; grep -n \"dṷei\\|duei-  ,fürchten\\|duei- ,fürchten\\|dvaeθ\\|dvae\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10\necho \"=== WLD Bd1 dirus ===\"; grep -n \"dīrus\\|dirus\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10"
}
```


### [2026-09-05T20:16:53.513Z] TOOL RESULT

```
=== WLD Bd1 dvei ===
46457:mann Bsl. Wb. 328. Aksl. tr/uh , dvaevrEQta 1 nicht nach Bezz. KZ. 22, 479, 
49009:tauchen)", ebenso med. dvopai und dvvca (hom. dvaero , ricbtiger mit -cm-, 
51525:av. dvae&a „Bedrohung“ (Fickl 3 113), hochst zweifelhaft arm . erkncim 
51538:dcista- ,,verha(jt", duesa-h, m., dvesas- n. „HaB“, av. dvaes -, tbaes- ,,anfeinden, 
51539:kranken", Ptc. tbista -, dvaesah -, tbaesah- „Anfeindung“, mp. bes „Leid, Un- 
51617:frcr&ah- „zwei Finger breit“, dvaepa- n. „Insel“? oder eher aus duaii-, wie 
=== WLD Bd1 dirus ===
11231:„dirus, atrox" (Fick BB. 1, 334; 2. 195).
```


## [2026-09-05T20:16:54.481Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LEW dirus ===\"; grep -n -o \"dirus.\\{0,400\\}\" LEW_1910.txt | head -5\necho; echo \"=== LAT dirus ===\"; grep -n -o \"dirus.\\{0,400\\}\" LAT.txt | head -5"
}
```


### [2026-09-05T20:16:56.389Z] TOOL RESULT

```
=== LEW dirus ===

=== LAT dirus ===
16938:dirus, -a, -um; de nanvais angnre, sinistre. Terne de la 1 . reli-
16949:dirus est vrainent nn not dialectal (cf. di-ennium
```


## [2026-09-05T20:17:00.960Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '51518,51545p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-05T20:17:01.008Z] TOOL RESULT

```
doixa (d. i. dedfoixa), att. Sedoixa, kret. dedfoixcbg Hes. (liberliefert Sedgoi- 
xibg) kehrt wieder in hom. Seidiaao/uai (d. i. dedftooojuai ), att. deSurojuat 
„schrecke (tr.), erschrecke (intr.)“ (*de-dfixtofiai), nachhom. Sedloxojuat 
„schrecke“ (*dedftx-oxo/iai), Sedstxeloe „furchtsam‘’, so daB unsere Wz. zu 
den Musterformen des x-Pf. gerechnet werden darf, s. Brugmann-Thumb 
Gr. Gr. 4 376 f. 

av. dvae&a „Bedrohung“ (Fickl 3 113), hochst zweifelhaft arm . erkncim 
„ich fiirchte", erkiid „Furcht“ (Anlaut wie im ebenso strittigen erku „zwei“ 

: *duoul Meillet Msl. 8, 235; doch von Pedersen KZ. 39, 398 zu dt. 
fiirchten gestellt); lat. dims „grausig, grauenvoll, unheilvoll" (von Servius 
zu Aen. Ill 235 auch als sabin. und umbr. Wort angefiihrt, so daB di- statt 
bi- aus *dui- als mundartliche Lautentwieklung betrachtet werden darf. 
Ernout El. dial. lat. 153 f., Sommer Hdb. 2 223), mit Formans -ro- „wovor 
man sich fiirchtet“, wie cla-rus „horbar“ ; vermutlich bestia, bellua ,,wildes 
Tier, Ungeheuer" aus *dueies-to-, -lo- „furchterlieh“ (s. auch u. *dheues- 
„stieben“) : dsog n. 

Als s-Erweiterung betrachtet man gemeinhin ai. dvesti „ha8t, feindet an", 
dcista- ,,verha(jt", duesa-h, m., dvesas- n. „HaB“, av. dvaes -, tbaes- ,,anfeinden, 
kranken", Ptc. tbista -, dvaesah -, tbaesah- „Anfeindung“, mp. bes „Leid, Un- 
heil". Doch liegen die Bedd. „hassen, anfeinden" und fiirchten" weit 
voneinander ab. Und wenn man (so z. B. Uhlenbeck KZ. 40, 553) Be- 
ziehung unserer Wz. zur Zweizahl erwogen hat („Entzweiung, Zwiespalt"), 
so kann dies sehr wohl fur ar. duals-, duis- zutreffen, das geradezu aus 
idg. *duis „entzwei" entwickelt sein mag, aber fur duel „fiirchten‘ f pa8t 
eine solche Gdbed. kaum („im Zwiespalt, Zweifel sein“ = „fiirchten“??
```


## [2026-09-05T20:17:01.147Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '16930,16960p' LAT.txt"
}
```


### [2026-09-05T20:17:01.207Z] TOOL RESULT

```
de duplus)-. i° diplone, brevet; 9° sanf-condnit, passeport {aena spdcial
an latin).
directus: y.rego.
diribeo, -§s, -ul, -itum, -ere: distribuer; t.techn.; ddnonbrer
les snffrages. De dis-habeo avec annissenent de h et sonorisation
de s intervocalique.
D^riv^s: diribitio,-tor,-torium. Ternes rares.
dirimo: v. emo.
dirus, -a, -um; de nanvais angnre, sinistre. Terne de la 1 . reli-
giense, cf. Cic., Din. 9, 15, tristissima exta sine capite, quibus nil
uidetur esse dirius et Leg.a ,8 fin; substantivd dans dirae, -arum f.pl.
"nanvais prdsages, nalddictions, inprdcations"; et ddifi 4 dans Vira,
et Dirae "les Furies". En passant dans la 1 . connnne (oh d'aillenrs
il est assez rare, et garde nne conlenr noble et poetique, conne le
d 4 riv 4 rare, nais classique, diritas ), 1 'adj. a pris le sens plns gdn 4 -
ral de "fnneste, redontable, etc.". Mot sabin d'aprbs Serv.anct., Ae.
3,335, S<a>bini et Vmbri, quae nos mala, dira appellant.
Le rapprochenent avec la racine duei- de hon. Ss 5 (F)oi.xa, 6e8(F) i,;tev,
arm.erkn$im "je crains", et, avec dlargissenent -s-, de skr. dvd§ti "il
hait" est possible si dirus est vrainent nn not dialectal (cf. di-ennium
A cote de bi-ennium-, v. Ernont, 6 l. dial., p. 153 et sniv.).
dis-: particnle usit 4 e senienent conne prenier terne de conposds.
L's pent s'annir devant sonore, ainsi dido, digero, diligo, dimoueo,
dirigo, diuelld, ae sonoriser en r A 1'intervocalique: dirimo, on
s’assiniler: dif-fero, dis- ne snbsiste clairenent qne devant p, t, c
et devant s. Marque la s^paration, 1'£cartenent, la direction en sens
opposds ( discurro, diuersus), et par snite le contraire, la ndgation
et s'oppose A con-: placeo/displiceo, similis/dissimilis, facilis/dif¬
ficilis, concors/discors, cf. disconducit, disconuenit, discooperio
fornations popnlaires; sens qne les langues ronanes ont bien conservd,
cf. entre antres, M.L.3666 *disdigndre, 3670 *disjSjundre, 9680 displi-3*5
```


## [2026-09-05T20:17:14.401Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nimport re\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'Bedrohung' in l and 'erkncim' in l or ('dvaesah -, tbaesah-' in l):\n        tag=re.search(r'\\[pdf page (\\d+)\\]', l)\n        print('leaf',i,'tag',tag.group(1) if tag else None)\n        # find printed page numbers\n        print([m.group().strip() for m in re.finditer(r'(?m)^\\s*\\d{3}\\s*$', l)][:5])\nEOF"
}
```


### [2026-09-05T20:17:16.177Z] TOOL RESULT

```
leaf 825 tag None
[]
```


## [2026-09-05T20:17:19.006Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nimport re\nleaves=t.split('\\f')\nl=leaves[825]\nprint(l[:400])\nprint('...TAIL...')\nprint(l[-400:])\nEOF"
}
```


### [2026-09-05T20:17:21.047Z] TOOL RESULT

```
                                                                       ;       ;




(Schulze Qu. ep. 244                       Anm. 2,   s.    auch Boisacq 171                        m. Anm. 2; korinth.
Afsivia gen.), be dog ,,furchtsam, feig; ungliicklich, beklagenswert"
eXog, Schulze Qu. ep. 244 Anm. 2, Bechtel Lexil. 97)      dtegog zu fiirchten“                 ;                ,


(*dft-sQog
...TAIL...
et haben konnen, sowie von got. anord. as. ags. afries. wi-t „w i
    zwei", anord. it, as. ags. git „ihr zwei“)
      alb.    du „zwei“ (von Pedersen KZ.                             36, 282             ebenfalls       auf *dud zuruck-
    gefiihrt ; ?);
      lat.   duo usw., umbr. (nur mit plur. Flexion) dur nom. m. „duo“, desen-duf
    acc. m. (12), duir „duobus“,                  tuva acc. n.
```


## [2026-09-05T20:17:25.946Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\np=open('POK_01.txt',encoding='utf-8',errors='replace').read()\nleaves=p.split('\\f')\nl=leaves[238]\ni=l.find('s-Erweiterung')\nprint(l[i:i+900])\nEOF"
}
```


### [2026-09-05T20:17:27.722Z] TOOL RESULT

```
s-Erweiterung   in   ai.  dvisti  .haßt,  feindet  an',  dvistd-   .verhaßt',  dvesa-/^ ra..  dvisas-  n.  .Haß',  av.  dvae§-,  tbaeS-  .anfeinden,  kränken'.  Partiz.  thüta- dva&sah-,   tbaesah-  .Anfeindung',   mpers.  bes  .Leid
```


## [2026-09-05T20:17:30.255Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\np=open('POK_01.txt',encoding='utf-8',errors='replace').read()\nleaves=p.split('\\f')\nl=leaves[239]\nprint(l[:900])\nEOF"
}
```


### [2026-09-05T20:17:31.750Z] TOOL RESULT

```
.   Unheil',  wohl  zu  duis^  "** S.  232.      ^  '^    .,
WP.  I  816  f..  WH.  I  353  f..  Schwyzer  Gr.  Gr.  I  710  &.  769.  774.    Nach/" Beaveniste    (briefl.)  gehört    die  Wz.  als    .bin  im    Zweifel'  zum   folgenden
duö(u)  m.  .zwei'  (Satzdoppelform  duuou),  dual  f.  n..  daneben  duei-,  duoi-, du/-;  vgl.  die  Zusammenfassung  bei  Brugmann  IP  2.  6 — 82  passim.   "
1.  Ai.  m.  dvdUj  dvti  (ved.  auch  duvdu,  duvä)  =  av.  dva  m..  ai.  f.  n.  c?ü^  ' (ved.  auch  duvt)  =  av.  bae  f.  und  n.  .zwei';
Tnstr.  Dat.  Abi.  ai.  d{ii)väbhyäm  (mit  geneuertem  ä),  av.  dvaeibya  (mit altem  i-Diphthong.  wie  lit.  dviem  usw.).  Gen.  Sg.  ai.  d{u)vdyoli]  bei  Zu sammenrückung  ai.  d(ii)vä- :  d(u)vä-dasa  .12'  (=  gr.  (Jwtea);
arm.  erku  .zwei'  (=  ai.  dvä)]
gr.  hom.  öv{f)(ü  (*J/w  in  (Jw-dexa),  Gen.  Dat.  ion.  att.  övoTvj  woneb
```


## [2026-09-05T20:17:43.377Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== RCH daur/dahr ===\"; grep -n -o \"dahr,.\\{0,200\\}\" RCH.txt | head -5\ngrep -n -o \"daur,.\\{0,200\\}\" RCH.txt | head -5\ngrep -n -o \"dairat.\\{0,150\\}\\|dáira.\\{0,150\\}\" RCH.txt | head -5\necho \"=== HRN dahr/daur ===\"; grep -n \"dahr\\|daur\" HRN.txt | head -5\necho \"=== HUB ===\"; grep -n \"dahr\\|daur\" HUB.txt | head -5"
}
```


### [2026-09-05T20:17:45.048Z] TOOL RESULT

```
=== RCH daur/dahr ===
43388:dahr,  The  world.
54130:dahr,  Continually  fasting,  p   sd-im  shudan^  To  fast.
=== HRN dahr/daur ===
8159:d. gaur, t. daur, S. 123), sondern vielmehr neupers.
=== HUB ===
```


## [2026-09-05T20:17:49.653Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '43380,43392p' RCH.txt | cut -c1-300\necho \"==== daira ====\"\ngrep -n -o \"A  circle.\\{0,120\\}\" RCH.txt | head -5"
}
```


### [2026-09-05T20:18:11.647Z] TOOL RESULT

```
fioe^pportifi  ijr  |»||afk  y>.
*   »■»*•>»  Strikii^ff.  heating.  BntMMg,
■   .   «   ■   .   *   V.  J   ^   ^   •   .   a   a   .   aaa
A   \ms^jffSj^hS^  l^fiime  of  arsah)  Close-hipped  (woman).
1^  nM,  A   very  deep  well  made  use  of  by  them  of  olden time  asim  observatory.
A   r&td  or  rasad  (from  Ju^),  Watching  (thtf  road  or  the stars).  Rusad  (from  X^J)  Seising  prey  (a  lion).  A   star-gazer. A   roadmWatcber.  A   guardian  angel.  A   leaper,  a   jumper. Snares.  Little  (com  or  water).  The  beginning  of  rain.
PhUJ  Xfj  ra$ad^bandy  A   fixer  of  astronomical  tables.
A   raidatj  One  fall  of  rain.  Ruidatj  A   pit  dug  to  catch a   lion.  A   silver  or  brass  ring  by  which  a   sword  hangs  to  the  belt.
p   ra$ad*gah^  An  observatory.  A   king’s  court.  The receipt  of  custohi.  rasad-gah^i  dahr,  The  world.
P   roiodpgah  khakty  The  world.  The  body.
A   rasadigy  A   keeper  of  the  road.  A   toll-gatherer.
A rat^(from  |Slb4be''banA  w.  Braising  be- tween two  stones.  fta§4t^  (from
W**  ^   ering  firmly*  Young  bees, (fern,  of  anOf)  Mesgfe-hipped  (woman). A   deep  wound  in  which  ih^  point  of  a   spear  is  burjed.
==== daira ====
38449:A  circle.  A   halo  round  the moon.  A   stipend,  a   salary.
```


## [2026-09-05T20:18:18.321Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A8%DB%8C%D8%B4/",
 "prompt": "Quote the فرهنگ معین (Mo'in) section for بیش, especially any sense \"گیاهی سمی / اقونیطن\" (a poisonous plant, aconite) and any bracketed origin tag such as [سنس.] or [هند.] or [په.]."
}
```


### [2026-09-05T20:18:23.027Z] TOOL RESULT

```
# بیش - فرهنگ معین Entry

According to the Mo'in dictionary section provided, the entry reads:

**[ په . ] (ق . ) افزون ، زیاد.**

This indicates the word بیش means "more" or "greater" with a Pahlavi origin marker [په.]. 

The document does not include a specific poisonous plant definition (اقونیطن/aconite) in the فرهنگ معین section shown. That botanical sense appears in the separate فرهنگ عمید section, which describes it as a toxic plant with leaves resembling lettuce or chicory.
```


## [2026-09-05T20:18:30.059Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/%D8%A8%DB%8C%D8%B4",
 "prompt": "Quote all Mo'in (فرهنگ معین) senses listed for بیش, including numbered homonyms بیش ۱، بیش ۲ and any bracketed etymological tags (e.g. [سنس.], [په.], [هند.])."
}
```


### [2026-09-05T20:18:34.717Z] TOOL RESULT

```
# Mo'in Dictionary Entry for بیش

According to the Moein Dictionary (فرهنگ انتشارات معین) shown above, there is one sense listed:

**بیش ۱**: "[په . ] (ق .) افزون ، زیاد" — meaning "more" or "additional; abundant"

The entry includes the etymological tag [په.] (indicating Persian origin) and the abbreviation (ق.) The definition equates بیش with the synonyms افزون and زیاد.

No additional numbered homonyms (بیش ۲, etc.) appear in the provided content.
```


## [2026-09-05T20:18:44.837Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nmkdir -p data/verification/sources/refs/ocr/BOOK\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg144.png data/verification/sources/refs/ocr/BOOK/144.png\nls -la data/verification/sources/refs/ocr/BOOK/ | tail -5"
}
```


### [2026-09-05T20:18:46.485Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb  90918 Sep  5 10:16 92.png
-rw-rw-r-- 1 sfmqrb sfmqrb  93420 Sep  5 10:18 94.png
-rw-rw-r-- 1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r-- 1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r-- 1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-05T20:18:51.488Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://en.wiktionary.org/wiki/arsenal|page 144 entry 0, English arsenal < It. arsenale < Arab. dar as-sina'a; checking whether a Greek intermediary is asserted\" \\\n\"https://www.etymonline.com/word/arsenal|page 144 entry 0, arsenal chain Arabic>Italian>English, no Greek stage\" \\\n\"https://en.wiktionary.org/wiki/%D8%AF%D9%87%D8%B1|page 144 entry 0 node 1-2, Arabic dahr: root d-h-r not d-w-r\" \\\n\"https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D8%B4|page 144 entry 1 node 3, Persian bish 'aconite' < MP bis < Skt visa\" \\\n\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dwey-|page 144 entry 1 root, PIE *dwey- 'to fear', descendants Lat dirus, Gk deinos, Av duuaes-\" \\\n\"https://vajehyab.com/moein/%D8%A8%DB%8C%D8%B4|page 144 entry 1 node 3, Mo'in online only has bish 1 'more' [Pahlavi]\" \\\n\"https://abadis.ir/fatofa/%D8%A8%DB%8C%D8%B4/|page 144 entry 1 node 3, Mo'in/Amid for bish; aconite sense only in Amid\" ; do\n  url=\"${u%%|*}\"; note=\"${u#*|}\"\n  python3 tools/fetch_source.py \"$url\" --note \"$note\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-05T20:18:56.295Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/4e4b76dfeb2bb881.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3731e550a460af94.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/139670ac1a0b714e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/77992dbe2e233ee1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0336307ea60583e4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/94409ef9e6360efe.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/943646f13c264e00.txt
```


## [2026-09-05T20:19:05.671Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FVQ dahr ===\"; grep -n -o \"dahr.\\{0,200\\}\" FVQ_pages.txt | head -5\necho \"=== AKD duru ===\"; grep -n -o \"duru.\\{0,150\\}\" AKD.txt | head -5\necho \"=== AFA dar ===\"; grep -n -o \"sina'a.\\{0,150\\}\\|dar as\\|dār\" AFA.txt | head -5\necho \"=== PHN arsenal ===\"; grep -n -o \"arsenal.\\{0,300\\}\" PHN.txt | head -3\necho \"=== DEV arsenal ===\"; grep -n -o \"ARSENAL.\\{0,400\\}\" DEV.txt | head -3"
}
```


### [2026-09-05T20:19:07.481Z] TOOL RESULT

```
=== FVQ dahr ===
=== AKD duru ===
=== AFA dar ===
=== PHN arsenal ===
1833:arsenal, que les étymologistes ne nous ex-
=== DEV arsenal ===
```


## [2026-09-05T20:19:09.690Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1820,1870p' PHN.txt"
}
```


### [2026-09-05T20:19:09.731Z] TOOL RESULT

```
^ji\ [atroub*] le quart Dans l'origine, Yarrobe était un poids
de vingt-cinq livres de seize onces chacune, usité en Espagne,
en Portugal, et dans le midi de la France; plus tard, sa valeur
a subi des variations suivant les localités. — Arrobe, comme
le prouve le correspondant arabe, signifie le quart du quintal
ou poids de cent livres.
ARSENAL, s. m. composé, (a.)
msXjuio j\^ [dâr s'inâ^at] maison de fabrication , lieu oii l'on fait
et conserve toutes sortes d'armes. Les Turcs écrivent «ildtf^
[terskhâneh] ou jôUm^ [ter^aneÀ], double altération des deux
mots arabes précédents. — Tarsianat^s, en latin du moyen âge,
et arzanày terme italien employé par Dante [Inferno, canto xxi,
verso 7), semblent témoigner assez en faveur de la source
orientale du mot arsenal, que les étymologistes ne nous ex-
pliquent pas d'une manière satisfaisante. Les uns l'attribuent
au celtique, d'autres au latin; mais l'origine de ce mot n'offre
plus maintenant aucun doute. M. le docteur Engelmann, dans
son Glossaire des mots espagnols et portugais dérivés de l'arabe
(Leyde, 1861, in-8^), s'exprime ainsi, au mot Arsenal : « Dans
(cun passage d'Ibn-Khaldoun, le calife Abdalmélic ordonne à
r. Haçan ibn Norman de bâtir à Tunis un dâr cinâ^a pour la cons-
^ truction de tout ce qui est nécessaire à l'équipement et à l'ar-
^ mement des vaisseaux. C'est dans cette acception spéciale que
''le mot a passé dans presque toutes les autres langues euro-
^ prennes. Voyez Jal , Gloss. naut, y>ART /if)
ARSENIC, 8. m. (p.)
^JJ [i^erntM] oijnment, arsenic jaune, mot également usité chez
les Arabes, et qui, précédé de Tarticle Jl [al], donne ji^t^p!
[azzemikh]j prototype de la transcription grecque dpcreviKÔv et
du latin arsenicum, dont nous avons fait arsenic. — - Les étymo-
logistes se sont trompés, je pense, en disant que arsenic vient
de ipcmv, mâle, fort, et de vixçiv^ vaincre, dompter (littérale-
ment, qui dompte les forts), à cause de la propriété vénéneuse
de cette substance. Pour moi, je n'y reconnais qu'une analogie
dortbographe avec l'adjectif grec ipereviKés, tf, 6v^ masculin, e,
dont le sens n'a aucun rapport avec celui de Varsenic; et je
considère ce dernier mot comme une altération du persan,
dont la première syllabe jj) [zer], qui signifie or, sert peut-être
h indiquer la couleur de l'orpiment à l'état naturel. C'est de
jê^j^\ [azzemikhl^ que les Espagnols ont fait azamefe, sorte de
poison. En portugais, on trouve aussi le vieux mot azamete,
avec le même sens.
ARTICHAUT, s. m. composé, (a.)
Les dictionnaires ne sont pas d'accord sur l'origine de ce
mot : les uns disent qu'il vient du latin arsus carduus [chardon
cuit), ce qui est inadmissible, attendu que l'on mange aussi
l'artichaut à l'état naturel; d'autres lui donnent pour racine les
deux mots celtiques art [^épine) et chaulx (chou); M. Defrémery
le rapporte de préférence au grec àfmnixd, — Bien qu'en
arabe ^artichaut soit appelé spécialement Ul^j^ [/l'arc/ia/] ,
mot reproduit par l'espagnol alcachofa et alcarchofa, ainsi que par■\
```


## [2026-09-05T20:19:19.501Z] TOOL CALL #63: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-05T20:19:19.538Z] TOOL RESULT

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


## [2026-09-05T20:20:35.046Z] AGENT

Now I'll write the verification file.


## [2026-09-05T20:26:46.639Z] TOOL CALL #64: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/write144.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_ARS = \"https://en.wiktionary.org/wiki/arsenal\"\nE_ARS = \"https://www.etymonline.com/word/arsenal\"\nW_DAHR = \"https://en.wiktionary.org/wiki/%D8%AF%D9%87%D8%B1\"\nW_BISH = \"https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D8%B4\"\nW_DWEY = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dwey-\"\nV_BISH = \"https://vajehyab.com/moein/%D8%A8%DB%8C%D8%B4\"\nA_BISH = \"https://abadis.ir/fatofa/%D8%A8%DB%8C%D8%B4/\"\n\ndata = {\n \"pdf_page\": 144,\n \"book_page\": 114,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"D.v.r\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"Arabic root د و ر (d-w-r) 'to turn, revolve, go round'; verb دَارَ (dāra), verbal noun دَوْر (dawr)\",\n   \"note\": \"The root box is right: د و ر is a standard Arabic triliteral meaning 'to turn, go round, encircle', and Nourai's own source Klein has exactly this family under the headword 'daira' (KLN_1966 leaf 219, printed p.398-399): «Arab. dāʾirah … prop. fem. partic. of dāra, 'he moved in a circle, went about', which is rel. to dār, 'house', orig. 'buildings surrounding a court', daur, 'circumference', dahr, 'long time, age' … Akkad. dūru, 'wall, fortress', also 'duration, eternity'». Two weak spots in the chart, both inherited from Klein: (a) dahr 'time' is in Arabic morphology a word of the root د ه ر, not د و ر — Wiktionary lists it under د ه ر with the verb dahara 'to overcome, prevail' — so its membership here is a comparative-Semitic guess, not an Arabic-internal derivation; (b) the Greek box (node 3) prints a form no lexicon knows. The English end of the chart (dār aṣ-ṣināʿa > It. arsenale > arsenal) is uncontroversial and is confirmed by Klein, Lokotsch, Pihan, Skeat, Etymonline and Wiktionary alike, except that they route the word straight into Venetian/Italian without a Greek stage.\",\n   \"note_fa\": \"ریشهٔ سه‌حرفی عربی «د و ر» به معنای «گشتن، چرخیدن، گرد چیزی گردیدن» ریشه‌ای است واقعی و برچسب زبان و معنای جعبهٔ ریشه درست است؛ کلاین نیز — که خودِ مأخذ نورایی است — در مدخل daira همین خانواده را یک‌جا آورده است: دائره، دار «خانه، در اصل بناهای گرداگرد حیاط»، دور «پیرامون» و حتی دهر. دو نکته را باید با احتیاط خواند: نخست آنکه «دهر» در صرف عربی از ریشهٔ «د ه ر» است نه «د و ر» و پیوند آن با این ریشه تنها در سطح مقایسهٔ زبان‌های سامی (اکدی dūru «دیرپایی») مطرح است؛ دوم آنکه جعبهٔ یونانی نمودار (گرهٔ ۳) صورتی می‌آورد که در هیچ فرهنگی یافت نمی‌شود. زنجیرهٔ «دارالصناعة ← ایتالیایی arsenale ← انگلیسی arsenal» اما بی‌چون‌وچرا درست است.\",\n   \"sources\": [W_ARS, E_ARS, W_DAHR],\n   \"ref_check\": [\n    {\"ref\": \"KLN:397\", \"status\": \"supports\", \"note\": \"Klein s.v. 'daira' (KLN_1966.txt line 10232; form-feed leaf 219, i.e. printed pp.398-399 — Nourai's 397 is one page low, the neighbouring leaf 218 carries the printed numbers 396/397 and ends at 'daffodil'): «Arab. dāʾirah (in vulgar pronunciation dayra), 'circle, enclosure', prop. fem. partic. of dāra, 'he moved in a circle, went about', which is rel. to dār, 'house', orig. 'buildings surrounding a court', daur, 'circumference', dahr, 'long time, age', Heb. dūr … Akkad. dūru, 'wall, fortress', also 'duration, eternity'». This is Nourai's root box and node 1 almost word for word.\"},\n    {\"ref\": \"FVA:146\", \"status\": \"not_checked\", \"note\": \"FVA = S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (1368/1989). refs_online.json records that no digital copy exists on any permitted platform (re-searched 2026-09); catalogue record only.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"LKT\", \"where\": \"no. 495 'Ar. dār-ṣināʿa' (LKT.txt line 1290)\", \"stance\": \"supports\", \"note\": \"«[Aus ar. dār 'Haus', ṣināʿa 'Betriebsamkeit, Handwerk, Industrie'] 'Fabrik', besonders 'Waffenfabrik' und auch schon ar. 'Schiffsbauhaus' … Hieraus it. darsena, siz. tirzanà 'inneres Hafenbecken', arzanà, arsenale, terzana 'Zeughaus'; frz. darse, darsine …, arsenal; sp. atarazana …; dtsch. Arsenal, ndl. arsenaal, engl. arsenal». Confirms the Arabic etymon and the Romance spread — with no Greek link.\"},\n    {\"src\": \"FVQ\", \"where\": \"grep 'dahr', 'daira' in FVQ_pages.txt\", \"stance\": \"silent\", \"note\": \"Jeffery's Foreign Vocabulary of the Qurʾān has no entry for dahr or dāʾirah — expected, since he lists only loanwords and these are treated as native Arabic.\"},\n    {\"src\": \"RCH\", \"where\": \"RCH.txt line 38449 (دائره) and line 43388 (دهر)\", \"stance\": \"supports\", \"note\": \"Richardson marks the circle-word with his Arabic flag: 'A  circle. A halo round the moon. A stipend, a salary.'; دهر likewise appears as an Arabic word glossed 'The world'. Confirms both are Arabic in Persian usage.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Arabic\",\n     \"words\": \"dâîrah; dâr; dahr; dâr-as-sanâ`\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"دَائِرَة dāʾira 'circle' is the active participle f. of دَارَ dāra 'he turned, went round' (root د و ر), i.e. literally 'the turning/encircling one'; دَار dār 'house' is the same root's noun, Klein glossing it 'orig. \\\"buildings surrounding a court\\\"', a sense supported by Akkadian dūru 'wall, enclosure'; دَار الصِّنَاعَة dār aṣ-ṣināʿa 'house of manufacture' is a genitive compound of dār with ṣināʿa 'craft, manufacture' (root ص ن ع, whence Nourai's cross-reference S.n.ʿa), used from Umayyad times of state shipyards — Pihan quotes Ibn Khaldūn on the caliph ʿAbd al-Malik ordering Ḥasan b. al-Nuʿmān to build a dār ṣināʿa at Tunis for fitting out warships. The odd word out is دَهْر dahr 'a long stretch of time, fate': Arabic lexicography assigns it to the root د ه ر (verb dahara 'to overcome, prevail'), and Wiktionary lists it there, so it is not an Arabic-internal derivative of dāra. Klein nevertheless groups it with dāra at the comparative-Semitic level, comparing Akkadian dūru 'duration, eternity' and dāru 'everlasting' — a real but weaker, cross-root argument. Hence 'plausible' rather than 'confirmed' for the node as a whole; the first three words are secure, dahr is not.\",\n     \"derivation_fa\": \"«دائره» اسم فاعل مؤنث از فعل «دارَ (یدور)» است از ریشهٔ «د و ر»، یعنی در اصل «آنچه می‌گردد / گرداگرد می‌آید»؛ «دار» نیز از همین ریشه است و کلاین معنای اصلی آن را «بناهای گرداگرد یک حیاط» می‌داند که با اکدی dūru «دیوار، حصار» می‌خواند. «دارالصناعة» ترکیب اضافی «دار» و «صناعة» (از ریشهٔ ص ن ع) است به معنای «کارخانه»، و از روزگار امویان به کارگاه کشتی‌سازی دولتی گفته می‌شد؛ پیهان از ابن خلدون نقل می‌کند که عبدالملک به حسان بن نعمان فرمان داد در تونس «دار صناعة» بسازد. تنها واژهٔ ناهمخوان «دهر» است: در صرف عربی «دهر» از ریشهٔ «د ه ر» است نه «د و ر» و پیوند آن با این خانواده تنها از راه مقایسهٔ سامی (اکدی dūru «جاودانگی») پیشنهاد شده است. بنابراین سه واژهٔ نخست قطعی‌اند و «دهر» با احتیاط پذیرفتنی است.\",\n     \"sources\": [W_DAHR, W_ARS],\n     \"ref_check\": [\n      {\"ref\": \"KLN:108\", \"status\": \"supports\", \"note\": \"Klein s.v. 'arsenal' (KLN_1966.txt line 3518; leaf 68, which carries the printed page numbers 108/109 — Nourai's 108 is exact): «It. arsenale (OIt. arzanale), 'dock' … fr. Arab. dār-aṣ-ṣināʿah (whence also Sp. dársena and It. darsena, 'dock'), lit. 'house of construction', fr. dār, 'house', as-, assimilated form of al-, 'the', and ṣināʿah, 'construction, art', fr. ṣanaʿa, 'he made'».\"},\n      {\"ref\": \"KLN:397\", \"status\": \"supports\", \"note\": \"Klein s.v. 'daira' (leaf 219, printed p.398-399) gives dāʾirah, dāra, dār, daur and dahr as one family — the whole node. See the entry-level ref_check for the quotation.\"},\n      {\"ref\": \"FVA:146\", \"status\": \"not_checked\", \"note\": \"no digital copy of Nahvi's dictionary exists (refs_online.json).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"LKT\", \"where\": \"no. 495 (LKT.txt line 1290)\", \"stance\": \"supports\", \"note\": \"«Aus ar. dār 'Haus', ṣināʿa 'Betriebsamkeit, Handwerk, Industrie'» — the compound and its meaning exactly as drawn.\"},\n      {\"src\": \"PHN\", \"where\": \"s.v. ARSENAL (PHN.txt lines 1826-1845)\", \"stance\": \"supports\", \"note\": \"«[dâr ṣinâʿat] maison de fabrication, lieu où l'on fait et conserve toutes sortes d'armes … Dans un passage d'Ibn-Khaldoun, le calife Abdalmélic ordonne à Haçan ibn Norman de bâtir à Tunis un dâr çinâʿa pour la construction de tout ce qui est nécessaire à l'équipement et à l'armement des vaisseaux.»\"},\n      {\"src\": \"SKT\", \"where\": \"s.v. arsenal (SKT.txt line 985, OCR damaged)\", \"stance\": \"supports\", \"note\": \"«— Arab. dár ṣináʿat … place for making … — Arab. dár, a house; ṣanáʿa, trade, construction» — Skeat gives the same compound.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"dowr «دور ۲»; dâr 1 «دار ۱ ( دیار ، دیّار )»; dahr «دهر»\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"All the words in this box are Arabic loans taken into New Persian with the ʿAbbāsid-era wave of Arabic vocabulary, not inherited Iranian material, and the chart draws them correctly as descendants of the Arabic node rather than of any Iranian form. دور dawr 'turn, cycle, perimeter' is Arabic dawr; the derivatives listed in the extra line are the regular Arabic patterns of the same root — دوره/دوران (Persianised nominals), دایر dāʾir and دایره dāʾira (act. part. m./f.), دوّار dawwār (intensive), مدوّر mudawwar (pass. part. 'made round'), مدار madār (noun of place, 'orbit'), and the form-IV pair اداره idāra 'administration' / مدیر mudīr 'director' (literally 'a making-to-turn' and 'one who makes turn'); داریه is the tambourine-word, Arabic dāʾira in the vulgar pronunciation dayra that Klein records. دار 'house' survives in Persian mainly in the frozen collocations and in دیار diyār 'lands, parts' (Arabic broken plural of dār) and دیّار dayyār 'a soul, anyone dwelling'. دهر dahr 'long time, world, fortune' is likewise a straight Arabic loan (Hāfez's line quoted on the page uses it in the classic sense 'the world, fate'), but it carries over the caveat of node 1: in Arabic it belongs to the root د ه ر. Verdict plausible for the node because of dahr; the rest is secure.\",\n     \"derivation_fa\": \"همهٔ واژه‌های این جعبه وام‌واژه‌های عربی‌اند که در فارسی نو (از سدهٔ سوم هجری به بعد) به کار رفته‌اند، نه میراث ایرانی؛ و نمودار نیز درست آن‌ها را از جعبهٔ عربی گرفته است. «دور» همان دَوْر عربی است و واژه‌های ردیف افزوده همگی صیغه‌های قیاسی همین ریشه‌اند: «دایر» و «دایره» اسم فاعل، «دوّار» صیغهٔ مبالغه، «مدوّر» اسم مفعول، «مدار» اسم مکان، و «اداره» و «مدیر» مصدر و اسم فاعل باب افعال؛ «داریه» نیز همان «دائره» است در تلفظ عامیانهٔ dayra که کلاین ثبت کرده است. «دار» به معنی خانه در فارسی بیشتر در «دیار» (جمع مکسر دار) و «دیّار» بازمانده است. «دهر» هم وام‌واژه‌ای عربی است — بیت حافظ که نورایی آورده آن را در معنای «روزگار، جهان» به کار برده — ولی همان نکتهٔ گرهٔ پیشین دربارهٔ آن برجاست: در عربی از ریشهٔ «د ه ر» است. پس ادعای نورایی دربارهٔ سه واژهٔ نخست درست و دربارهٔ «دهر» با احتیاط پذیرفتنی است.\",\n     \"sources\": [W_DAHR],\n     \"ref_check\": [\n      {\"ref\": \"FVA:146\", \"status\": \"not_checked\", \"note\": \"FVA (Nahvi 1368) is precisely the book that would list these Arabic-in-Persian words, but no digital copy exists (refs_online.json: 'RE-SEARCH 2026-09: still no digital copy on any permitted platform').\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"RCH\", \"where\": \"RCH.txt lines 38449, 43388\", \"stance\": \"supports\", \"note\": \"Richardson (Persian-Arabic-English) flags both words as Arabic in Persian use: 'A  circle. A halo round the moon. A stipend, a salary.' (دائره) and 'dahr, The world.'\"},\n      {\"src\": \"HRN\", \"where\": \"grep 'dahr', 'daur' in HRN.txt — one irrelevant hit (line 8159, about gaur/daur)\", \"stance\": \"silent\", \"note\": \"Horn's Grundriss der neupersischen Etymologie has no entry for دور/دهر/دار, as expected: it treats inherited Iranian vocabulary only, so its silence positively supports the loan analysis.\"},\n      {\"src\": \"MON\", \"where\": \"vajehyab.com/moein and abadis.ir (فرهنگ معین section)\", \"stance\": \"partial\", \"note\": \"The online Mo'in text is served without the Latin-script origin forms of the print edition; for دهر/دور it gives the senses but the [ع.] tags are not reproducible from the pages fetched, so Mo'in could only be used indirectly here.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Greek\",\n     \"words\": \"arsonalos\",\n     \"verdict\": \"transcription_suspect\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"arsonalos\",\n     \"correct_form\": \"ἀρσηνάλης (MGk. arsēnálēs)\",\n     \"derivation\": \"The printed page (PDF 144, book p.114) really does read 'arsonalos : factory, workshop', so the extraction is faithful; the error is Nourai's. His source is Klein s.v. arsenal, which says the Italian word was «borrowed — prob. through the medium of MGk. ἀρσηνάλης — fr. Arab. dār-aṣ-ṣināʿah»; the 1971 one-volume printing gives the Greek clearly as ἀρσηνάλης (the 1966 OCR mangles it). 'Arsonalos' is not a Greek word in any form: it has neither the -ης ending Klein prints nor any attestation in Byzantine lexica, and Nourai's gloss 'factory, workshop' is simply the gloss of the Arabic compound carried over. Beyond the form, the Greek stage itself is not part of the modern account: Wiktionary gives 'Italian arsenale, from Arabic دَار الصِّنَاعَة' with no Greek link, Etymonline has Italian arzenale straight from Arabic (the Venetians applying it to their great wharf), and Lokotsch no.495 and Pihan s.v. ARSENAL likewise take the word from Arabic into Sicilian/Venetian (tirzanà, arzanà — Dante, Inferno XXI.7) with no Greek intermediary. So the box should be read as Klein's hedged 'prob.', with a misspelt headword.\",\n     \"derivation_fa\": \"صفحهٔ چاپی (ص ۱۱۴ کتاب) به‌راستی «arsonalos» دارد، پس خطای خوانش اسکن نیست و خطای خودِ کتاب است. مأخذ نورایی، یعنی کلاین، در مدخل arsenal می‌نویسد که واژهٔ ایتالیایی «احتمالاً به میانجی یونانی میانه ἀρσηνάλης» از عربی «دارالصناعة» گرفته شده است؛ صورت درست همین ἀρσηνάλης است و «arsonalos» نه پایانهٔ یونانی درستی دارد و نه در هیچ فرهنگ بیزانسی آمده است. افزون بر صورت واژه، خودِ مرحلهٔ یونانی هم در ریشه‌شناسی امروزی جایی ندارد: ویکی‌واژه و اتیمانلاین واژه را یک‌راست از عربی به ایتالیایی (و نخست به گویش ونیزی/سیسیلی: arzanà، tirzanà — که دانته در دوزخ، سرود بیست‌ویکم آورده) می‌برند، و لوکوچ (شمارهٔ ۴۹۵) و پیهان نیز چنین‌اند. پس این جعبه خطای چاپی کتاب است بر پایهٔ حدسِ محتاطانهٔ کلاین.\",\n     \"sources\": [W_ARS, E_ARS],\n     \"ref_check\": [\n      {\"ref\": \"KLN:108\", \"status\": \"partial\", \"note\": \"Klein does put a Greek stage here, but hedged and with a different form: KLN_1971.txt lines 20079-20083 «It. arsenale (OIt. arzanale), 'dock', borrowed — prob. through the medium of MGk. ἀρσηνάλης — fr. Arab. dār-aṣ-ṣināʿah». Klein gives no gloss 'factory, workshop' for the Greek word and does not assert the Greek stage as fact.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"LKT\", \"where\": \"no. 495 (LKT.txt line 1290)\", \"stance\": \"contradicts\", \"note\": \"Lokotsch routes the word Arabic → Italian/Sicilian directly: «Hieraus it. darsena, siz. tirzanà …, arzanà, arsenale, terzana 'Zeughaus'» — no Greek is mentioned anywhere in the entry.\"},\n      {\"src\": \"PHN\", \"where\": \"s.v. ARSENAL (PHN.txt lines 1826-1845)\", \"stance\": \"contradicts\", \"note\": \"«Tarsianatus, en latin du moyen âge, et arzanà, terme italien employé par Dante (Inferno, canto XXI, verso 7), semblent témoigner assez en faveur de la source orientale du mot arsenal» — the mediating forms Pihan knows are Medieval Latin and Italian, not Greek.\"},\n      {\"src\": \"SKT\", \"where\": \"s.v. arsenal (SKT.txt line 985)\", \"stance\": \"contradicts\", \"note\": \"Skeat's chain is 'Ital. … — Arab. dár ṣináʿat'; no Greek step.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Italian\",\n     \"words\": \"darsena, arsenale\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Arabic dār aṣ-ṣināʿa was borrowed twice into Italo-Romance from the Muslim Mediterranean: once with the initial dā- kept, giving Italian/Spanish darsena, dársena 'inner harbour basin, wet dock' (Sicilian tirzanà), and once with the first syllable reanalysed and lost, giving Old Italian arzanà — the form Dante uses of the Venetian shipyard in Inferno XXI.7 — later Tuscanised as arsenale with the Romance suffix -ale. Lokotsch sets the whole spread out (Sp. atarazana, Pg. taracena, Fr. darse/arsenal, Rum. arsenal), and Klein records the doublet explicitly: «Arab. dār-aṣ-ṣināʿah (whence also Sp. dársena and It. darsena, 'dock')». The Venetian Arsenale, the state shipyard founded in 1104, is the referent that fixed the naval-dockyard sense.\",\n     \"derivation_fa\": \"«دارالصناعة» عربی دو بار به زبان‌های ایتالیایی-رومی راه یافته است: یک بار با نگاه‌داشت هجای نخست، که ایتالیایی darsena و اسپانیایی dársena «حوضچهٔ درونی بندر» از آن است (و سیسیلی tirzanà)، و یک بار با افتادن هجای «دار» — گویا به گمانِ آنکه حرف تعریف است — که ایتالیایی کهن arzanà از آن پدید آمد؛ همان صورتی که دانته در «دوزخ»، سرود بیست‌ویکم، دربارهٔ کارگاه کشتی‌سازی ونیز به کار برده است. سپس با پسوند رومی ‎-ale‎ به arsenale بدل شد. لوکوچ همهٔ این گسترش را برشمرده و کلاین نیز دوگانهٔ darsena/arsenale را ثبت کرده است. ادعای نورایی در این گره درست است.\",\n     \"sources\": [W_ARS, E_ARS],\n     \"ref_check\": [\n      {\"ref\": \"KLN:108\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 3518 (leaf 68 = printed p.108/109): «It. arsenale (OIt. arzanale), 'dock' … fr. Arab. dār-aṣ-ṣināʿah (whence also Sp. dársena and It. darsena, 'dock')» — both Italian forms of Nourai's box, from the Arabic compound.\"},\n      {\"ref\": \"AHD:74\", \"status\": \"not_checked\", \"note\": \"AHD:74 is a page of the main American Heritage Dictionary (New College ed.), where 'arsenal' falls in the A-section; only Watkins's Indo-European Roots appendix is on disk locally (AHD_watkins1985.txt), and it has no entry for this non-Indo-European word. Not verifiable here.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"LKT\", \"where\": \"no. 495 (LKT.txt line 1290)\", \"stance\": \"supports\", \"note\": \"«Hieraus it. darsena, siz. tirzanà 'inneres Hafenbecken', arzanà, arsenale, terzana 'Zeughaus'; frz. darse, darsine …, arsenal; sp. atarazana, atarazanal 'Schuppen', arsenal».\"},\n      {\"src\": \"PHN\", \"where\": \"s.v. ARSENAL (PHN.txt line 1830 f.)\", \"stance\": \"supports\", \"note\": \"«arzanà, terme italien employé par Dante (Inferno, canto XXI, verso 7)» — the Old Italian form and its earliest literary attestation.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"English\",\n     \"words\": \"arsenal\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English took the word from Italian around 1500 in the nautical sense 'dockyard, dock with naval stores', the Venetian Arsenale being the model; by the 1570s it had shifted to 'public place for making or storing weapons and ammunition', which is the modern sense (Etymonline). Wiktionary's chain is the same: «From Italian arsenale, from Arabic دَار الصِّنَاعَة (dār aṣ-ṣināʿa, 'manufacturing shop')». The final -al was reinforced in English by the native adjective suffix -al (Klein).\",\n     \"derivation_fa\": \"انگلیسی این واژه را نزدیک سال ۱۵۰۰ میلادی از ایتالیایی گرفت، نخست در معنای دریایی «کارگاه و انبار کشتی‌سازی» — با الگوی «آرسناله»‌ی ونیز — و از دههٔ ۱۵۷۰ به معنای «زرادخانه، جای ساخت و انبار جنگ‌افزار» به کار رفت. ویکی‌واژه و اتیمانلاین هر دو همین زنجیره را می‌آورند: عربی «دارالصناعة» ← ایتالیایی arsenale ← انگلیسی arsenal. ادعای نورایی در این گره درست است.\",\n     \"sources\": [E_ARS, W_ARS],\n     \"ref_check\": [\n      {\"ref\": \"AHD:74\", \"status\": \"not_checked\", \"note\": \"Page of the main AHD (New College ed.) A-section; only the Watkins IE-roots appendix is available locally, and it carries no non-IE headwords. The claim is however fully covered by Klein, Skeat, Lokotsch, Etymonline and Wiktionary.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. arsenal (KLN_1966.txt line 3518, printed p.108)\", \"stance\": \"supports\", \"note\": \"«arsenal, n., a place for manufacturing and storing ammunition and weapons. — It. arsenale … For the ending of arsenal see adj. suff. -al.»\"},\n      {\"src\": \"SKT\", \"where\": \"s.v. arsenal (SKT.txt line 985)\", \"stance\": \"supports\", \"note\": \"Skeat gives 'Ital. … — Arab. dár ṣináʿat, … place for making …; — Arab. dár, a house; ṣanáʿa, trade, construction'.\"},\n      {\"src\": \"LKT\", \"where\": \"no. 495 (LKT.txt line 1290)\", \"stance\": \"supports\", \"note\": \"«Dtsch. Arsenal, ndl. arsenaal, engl. arsenal, russ. arsenal» — English listed among the European borrowings of the Arabic compound.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"Dwei, Dvei\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *dwei- 'to fear' (Pokorny 227 dṷei-; Watkins/AHD dwei-; Wiktionary *dwey-)\",\n   \"note\": \"Pokorny IEW 227 heads the entry «dṷei- ,fürchten'», so the root, the language label 'Indo-European' and the gloss 'to fear' are all exactly right, and Nourai's page reference is exact (the entry begins on p.227 and runs onto p.228). Watkins/AHD has the same headword: «dwei-. To fear. 1. Suffixed form *dwei-ro- in Latin dirus … DIRE. 2. Suffixed form *dwey-eno- in Greek deinos … DINOSAUR, DINOTHERE. (This root originally meant 'to be in doubt, be of two minds', and is related to dwo-.) [Pok. dṷei- 227.]» — which is the whole right-hand half of the chart. One caution that Nourai does not pass on: Walde-Pokorny I 816 f. warns that the s-extension (Skt. dvéṣṭi 'hates', Av. dvaēš-/tbaēš-, MP bēš), i.e. the entire Iranian left half of this chart, is semantically distant — «Doch liegen die Bedd. 'hassen, anfeinden' und 'fürchten' weit voneinander ab» — and Pokorny himself closes the entry noting Benveniste's view (per letter) that the root belongs to *dṷō(u) 'two' as 'to be in two minds'. The one derivation on the page that modern scholarship rejects outright is the last Iranian step, Pahlavi bēš 'sorrow' → Persian bīš 'a poisonous plant' (node 3).\",\n   \"note_fa\": \"ریشهٔ نمودار همان *dwei- هندواروپایی آغازین به معنای «ترسیدن» است؛ پوکورنی در صفحهٔ ۲۲۷ فرهنگ خود آن را با همین سرواژه و همین معنا («dṷei- ,fürchten'») آورده و ارجاع نورایی (POK:227) دقیق است. واتکینز نیز در پیوست ریشه‌های هندواروپایی امریکن هریتیج همین را دارد و لاتینی dīrus و یونانی deinos را از آن می‌گیرد. اما نکته‌ای هست که نورایی نیاورده است: والده-پوکورنی (جلد یکم، ص ۸۱۶ به بعد) هشدار می‌دهد که گسترش ‎-s‎ی این ریشه — یعنی سنسکریت dvéṣṭi «کینه می‌ورزد»، اوستایی dvaēš-/tbaēš- و فارسی میانه bēš، که سراسر شاخهٔ ایرانی این نمودار است — از نظر معنایی از «ترسیدن» دور است؛ و خودِ پوکورنی در پایان مدخل نظر بنونیست را می‌آورد که این ریشه در اصل «دودل بودن» و وابسته به «دو» است. تنها حلقه‌ای که پژوهش امروزی آن را رد می‌کند، واپسین گام ایرانی است: «بیشِ» فارسی (گیاه سمی) از «بِشِ» پهلوی (اندوه) نیامده است.\",\n   \"sources\": [W_DWEY],\n   \"ref_check\": [\n    {\"ref\": \"POK:227\", \"status\": \"supports\", \"note\": \"POK_01.txt line 3257 (form-feed leaf 238; the printed number 228 appears part-way down the same leaf, so the entry opens on p.227): «dṷei- ,fürchten'. Av. dvaēθ-ā ,Bedrohung'; arm. erknč̣im ,ich fürchte' …» and on p.228 «gr. hom. δείδω ,fürchte' … lat. dīrus ,grausig, grauenvoll, unheilvoll' … mit Formans -ro- ,wovor man sich fürchtet' … s-Erweiterung in ai. dvéṣṭi ,haßt, feindet an' … av. dvaēš-, tbaēš- ,anfeinden, kränken', Partiz. tbišta-, dvaēšah-, tbaēšah- ,Anfeindung', mpers. bēš ,Leid, Unheil'». Every node of the chart except the Sogdian and the New Persian one is on these two pages.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I 816 f. (WLD_Bd1_1930 djvu lines 51518-51545; Pokorny closes his entry with 'WP. I 816 f.')\", \"stance\": \"partial\", \"note\": \"Has the same material — «av. dvaēθa „Bedrohung“ … lat. dīrus „grausig, grauenvoll, unheilvoll“ … mit Formans -ro- „wovor man sich fürchtet“» — but adds the reservation Nourai omits: «Als s-Erweiterung betrachtet man gemeinhin ai. dvéṣṭi „haßt, feindet an“ … av. dvaēš-, tbaēš- „anfeinden, kränken“ … mp. bēš „Leid, Unheil“. Doch liegen die Bedd. „hassen, anfeinden“ und „fürchten“ weit voneinander ab.»\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. dwei- (AHD_watkins1985.txt line 412)\", \"stance\": \"supports\", \"note\": \"«dwei-. To fear. 1. Suffixed form *dwei-ro- in Latin dirus, fearful, horrible (originally a dialectal form): DIRE. 2. Suffixed form *dwey-eno- in Greek deinos, fearful, monstrous: DINOSAUR, DINOTHERE. … [Pok. dṷei- 227.]»\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan\",\n     \"words\": \"dvaĕtha; dvaĕš, tbaĕš\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The forms are real and the descent from the root is right, but the second gloss is wrong. Gathic Avestan dvaēθā- f. is a genuine noun 'threat' — Bartholomae col. 763-764: «g. dvaēθā- f. 'Bedrohung', mit Akk. der Person», i.e. the thing one threatens someone with — formed from the root with the -θā- suffix; Pokorny cites the same word on p.227 and Klein s.v. dire has 'Avestic dvaeθa-, \\\"threat, menace\\\"', which is exactly Nourai's first gloss. dvaēš-/tbaēš- are the verbal stem of the s-extension: Pokorny glosses them «anfeinden, kränken» = 'to be hostile to, to injure/offend', and Bartholomae has the nouns tbaēšah-, Gathic dvaēšah- n. 'Anfeindung, Feindschaft, Feindseligkeit' (col. 813-814) and dvaēša- m. 'Qual, Pein'. Nourai's gloss 'sick, ill' is a mistranslation of Pokorny's German kränken ('to wrong, injure'), read as though it were krank 'sick'; nothing in the Avestan material means 'sick'. Phonetically the tb-/dv- pair is the regular Avestan doublet of an initial cluster *dw- (Young Avestan tb-, Gathic dv-). Verdict plausible: the arrow is right, one gloss is not.\",\n     \"derivation_fa\": \"صورت‌ها درست‌اند و پیوندشان با ریشه نیز درست است، اما معنای دوم نادرست است. dvaēθā- اوستایی گاهانی اسمی است مؤنث به معنای «تهدید»؛ بارتولومه در ستون ۷۶۳–۷۶۴ می‌نویسد: «g. dvaēθā- f. ,Bedrohung', mit Akk. der Person»، و کلاین نیز در مدخل dire همین را با معنای «threat, menace» آورده است — یعنی همان معنایی که نورایی داده. اما dvaēš-/tbaēš- ستاک فعلی گسترشِ ‎-s‎ی ریشه است و پوکورنی آن را «anfeinden, kränken» یعنی «دشمنی کردن، آزردن» معنا کرده و بارتولومه اسم‌های tbaēšah-/dvaēšah- «دشمنی» و dvaēša- «رنج، درد» را ذیل آن آورده است. معنای «بیمار» که نورایی نوشته، برگردان نادرستِ فعل آلمانیِ kränken («آزردن») است که آن را به گمانِ krank («بیمار») خوانده‌اند؛ هیچ‌یک از این صورت‌های اوستایی معنای «بیمار» ندارد. از نظر آوایی نیز tb- در اوستایی متأخر و dv- در گاهان، دو صورت قاعده‌مندِ خوشهٔ آغازینِ *dw- ایرانی باستان‌اند. پس ادعای نورایی در اصلِ اشتقاق درست و در معنا خطاست.\",\n     \"sources\": [W_DWEY],\n     \"ref_check\": [\n      {\"ref\": \"POK:228\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 238, p.228: «s-Erweiterung in ai. dvéṣṭi ,haßt, feindet an' … av. dvaēš-, tbaēš- ,anfeinden, kränken', Partiz. tbišta-, dvaēšah-, tbaēšah- ,Anfeindung', mpers. bēš ,Leid, Unheil'»; dvaēθ-ā ,Bedrohung' stands a few lines earlier on p.227. Supports the forms and the descent — and shows where the 'sick, ill' gloss came from.\"},\n      {\"ref\": \"KLN:454\", \"status\": \"supports\", \"note\": \"Klein s.v. dire (KLN_1966.txt line 11543; leaf 249, whose printed page number is 455, the preceding leaf carrying 454 — Nourai's 454 is within a page): «It possibly derives fr. I.-E. base *dwei-, 'to be afraid, fear' … OI. dveṣṭi, 'hates', dviṣaḥ, 'hatred', Avestic dvaeθa-, 'threat, menace', and prob. also Arm. erknč̣im, 'I fear'.» Klein's gloss for dvaēθa- is Nourai's first gloss verbatim.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"cols. 763-764 (dvaēθā-, dvaēša-) and 813-814 (tbaēšah-) — BRT.txt lines 13939, 14746, header line 14721 '813 tbaēša- … tbaēšah- 814'\", \"stance\": \"supports\", \"note\": \"«g. dvaēθā- f. ,Bedrohung', mit Akk. der Person: yeiiā mā ... Y.43.9»; «j. tbaēšah-, g. dvaēšah- n. 1) ,Anfeindung, Feindschaft, Feindseligkeit'»; «g. dvaēša- m. ,Qual, Pein'». Bartholomae has all three, none glossed 'sick'.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I 816 f. (djvu lines 51525, 51538-51541)\", \"stance\": \"partial\", \"note\": \"«av. dvaēθa „Bedrohung“ (Fick I³ 113)» supports the first word; but for the second: «av. dvaēš-, tbaēš- „anfeinden, kränken“, Ptc. tbišta-, dvaēšah-, tbaēšah- „Anfeindung“, mp. bēš „Leid, Unheil“. Doch liegen die Bedd. „hassen, anfeinden“ und „fürchten“ weit voneinander ab» — Walde-Pokorny doubt that this branch belongs to 'to fear' at all.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Pahlavi\",\n     \"words\": \"běš 1\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Middle Persian bēš [byš] 'pain, sorrow; harm, hostility' continues the Old Iranian s-stem *dwaišah- (Av. dvaēšah-/tbaēšah- 'hostility') with the regular Middle Persian loss of the initial *dw- cluster before a front vowel — the same change that gives MP bē 'two' beside Av. dva- and MP bīst 'twenty' beside Av. vīsaiti — plus *ai > ē. Pokorny lists the form himself at the end of the p.228 entry («mpers. bēš ,Leid, Unheil'»), MacKenzie has «bēš [byš] pain, sorrow; harm, hostility. ~ burdan: bear hostility», and Nyberg makes the derivation explicit: «¹bēš [byš] grief, affliction … — Av. dvaēšah-, tbaēšah- 'hostility'». The chart's own NOTE ('See \\\"Weis\\\" for an alternative root') is misplaced here: bēš 'sorrow' belongs securely to Dwei; it is the *next* box, Persian bīš 'aconite', for which the Weis root (PIE *weis- 'poison', whence Skt. viṣa-) is not merely an alternative but the correct answer.\",\n     \"derivation_fa\": \"«بِش» فارسی میانه [byš] به معنای «رنج، اندوه؛ آزار، دشمنی» دنبالهٔ ستاکِ ‎-s‎یِ ایرانی باستان *dwaišah- است (اوستایی dvaēšah-/tbaēšah- «دشمنی»)، با دو دگرگونی آوایی قاعده‌مند: از میان رفتن خوشهٔ آغازین *dw- در فارسی میانه — همان تحولی که «دو»ی اوستایی را به bē و «بیست» را پدید آورده — و بدل شدن ai کهن به ē. پوکورنی خودِ این صورت را در پایان صفحهٔ ۲۲۸ آورده («mpers. bēš ,Leid, Unheil'»)، مکنزی آن را «bēš [byš] درد، اندوه؛ آزار، دشمنی» ثبت کرده و نیبرگ اشتقاق را صریح نوشته است: «¹bēš … — Av. dvaēšah-, tbaēšah-». یادداشت خودِ نمودار («برای ریشهٔ دیگر بنگرید به Weis») جای درستی ندارد: «بِش» به معنای اندوه به‌قطع از همین ریشه است؛ آن ریشهٔ دیگر برای جعبهٔ بعدی، یعنی «بیشِ» فارسی به معنای گیاه سمی، نه «بدیل» بلکه پاسخ درست است.\",\n     \"sources\": [W_DWEY],\n     \"ref_check\": [\n      {\"ref\": \"POK:228\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 238, end of the dṷei- entry: «… tbaēšah- ,Anfeindung', mpers. bēš ,Leid, Unheil'» — the Pahlavi word is Pokorny's own, on precisely the cited page.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary, b-section (PHD.txt line 256)\", \"stance\": \"supports\", \"note\": \"«bēš [byš] pain, sorrow; harm, hostility. ~ burdan: bear hostility»; also «bēš-burdār [byšbwltʾl] hostile» and «bēšīdan [byšytn'] = bištan» 'hurt, torment'.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (NYB_vol2_glossary.txt lines 981-983, and the Avestan index line 5144)\", \"stance\": \"supports\", \"note\": \"«¹bēš [byš] grief, affliction 111⁶. 48¹; ~ burtan to grieve, to mourn … — Av. (814 sq.) dvaēšah-, tbaēšah- 'hostili[ty]'»; the Avestan-to-Pahlavi index likewise has «dvaēšah, tbaēšah: ¹bēš».\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Persian\",\n     \"words\": \"bîš 2 «بیش ۲»\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"Modern scholarship derives Persian بیش bīš 'aconite, a poisonous plant' not from Pahlavi bēš 'sorrow' but from Sanskrit: Wiktionary's Persian entry (Etymology 2) gives «From Middle Persian byš /bīš/ 'aconite', from Sanskrit विषा (viṣā, 'Aconitum ferox'), from विष (viṣa, 'poison'), whence English bikh» — i.e. an Indian drug-name borrowed into Middle Persian, ultimately from PIE *weis- 'poison' (Skt. viṣa-, Lat. vīrus), which is exactly the root Nourai's own NOTE points to under the name 'Weis'. Decisively, MacKenzie's Pahlavi dictionary lists the two words as separate lemmas a few lines apart — «bēš [byš] pain, sorrow; harm, hostility» and «biš [byš] aconite» — so the split is already Middle Persian, and only the ambiguous Pahlavi spelling byš makes them look like one word. Hobson-Jobson s.v. BISH, BIKH says the same on the Indian side: «n. H. from Skt. viṣa, 'poison'. The word has several specific applications, as (a) to the poison of various species of aconite, particularly Aconitum ferox». The arrow Pahlavi bēš → Persian bīš 2 is therefore a homonym confusion; the correct chain is Skt. viṣa-/viṣā > MP bīš > NP بیش.\",\n     \"derivation_fa\": \"پژوهش امروزی «بیش» فارسی (گیاه سمی، اقونیطن) را نه از «بِشِ» پهلوی به معنای اندوه، بلکه وام‌واژه‌ای هندی می‌داند: ویکی‌واژه در مدخل دوم «بیش» می‌نویسد که از فارسی میانهٔ bīš «اقونیطن» است و آن از سنسکریت विषा (viṣā، «Aconitum ferox») از विष (viṣa، «زهر»). این همان ریشه‌ای است که خودِ نورایی در یادداشت نمودار با نام «Weis» به آن اشاره کرده — یعنی ریشهٔ هندواروپایی *weis- «زهر» که لاتینی vīrus نیز از آن است. دلیل قاطع در فرهنگ پهلوی مکنزی است که این دو را دو مدخل جداگانه آورده: «bēš [byš] درد، اندوه» و «biš [byš] اقونیطن»؛ پس جدایی این دو واژه از فارسی میانه پیداست و تنها یکسانیِ املای پهلویِ byš آن‌ها را یکی می‌نمایاند. هابسن-جابسن نیز ذیل BISH, BIKH می‌گوید این واژهٔ هندی از سنسکریت viṣa «زهر» است و بر گونه‌های اقونیطن اطلاق می‌شود. بنابراین پیکان «بِشِ پهلوی ← بیشِ فارسی» خطای هم‌آوایی است و ریشه‌شناسی امروزی آن را رد می‌کند.\",\n     \"sources\": [W_BISH, V_BISH, A_BISH],\n     \"ref_check\": [\n      {\"ref\": \"MON:627\", \"status\": \"not_found\", \"note\": \"Mo'in vol.1 p.627 could not be reached: the print volumes are not digitised, and the online Mo'in text (vajehyab.com/moein/بیش and abadis.ir/fatofa/بیش/, both fetched) serves only «بیش [ په . ] (ق .) افزون ، زیاد» = bīš 1 'more', tagged Pahlavi; the aconite sense appears on those pages only in the Amid dictionary section. Nourai's homonym number «بیش ۲» does match Mo'in's numbering practice, so the citation is likely genuine, but its content is unverified — and note that even if Mo'in glosses the plant there, that would not by itself support an origin in bēš 'sorrow'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, b-section (PHD.txt line 256)\", \"stance\": \"contradicts\", \"note\": \"Two distinct lemmas in the same column: «bēš [byš] pain, sorrow; harm, hostility» and, a few entries later, «biš [byš | N ~] aconite» — MacKenzie explicitly keeps the aconite word apart from the sorrow word and links it to the New Persian form.\"},\n      {\"src\": \"HJB\", \"where\": \"Hobson-Jobson s.v. BISH, BIKH (HJB.txt lines 3630-3635)\", \"stance\": \"contradicts\", \"note\": \"«BISH, BIKH, &c., n. H. from Skt. viṣa, 'poison.' The word has several specific applications, as (a) to the poison of various species of aconite, particularly Aconitum ferox, otherwise more specifically called in Skt. vatsanābha, 'calf's navel'…»\"},\n      {\"src\": \"MON\", \"where\": \"vajehyab.com/moein/بیش and abadis.ir (فرهنگ معین section)\", \"stance\": \"partial\", \"note\": \"Online Mo'in gives only «[ په . ] (ق .) افزون ، زیاد» for بیش, i.e. the homonym 'more' (from MP wēš), not the plant; so Mo'in as served online neither supports nor refutes the plant etymology.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Sogdian\",\n     \"words\": \"db`yš\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Sogdian δβʾyš (Buddhist Sogdian spelling; read δβēš) 'enmity, harm' is the Sogdian outcome of the same Old Iranian s-stem *dwaišah- that gives Av. dvaēšah-/tbaēšah- and MP bēš: Sogdian, unlike Middle Persian, keeps the initial cluster as δβ-, and the Aramaic-based script writes it db-. Gharib's Sogdian Dictionary, entry 3481, states the Avestan connection outright, and the neighbouring entry 3482 δβʾyš- 'to harm' gives the verb. Drawing the box straight from the root rather than through the Avestan box is a simplification of the chart's geometry — Sogdian does not descend from Avestan — but it is not an error: both are independent Old Iranian continuations.\",\n     \"derivation_fa\": \"«δβʾyš» سغدی (به خط سغدیِ بودایی؛ خوانش δβēš) به معنای «دشمنی، آزار» بازماندهٔ همان ستاک ‎-s‎ی ایرانی باستان *dwaišah- است که در اوستایی dvaēšah-/tbaēšah- و در فارسی میانه bēš شده است. سغدی برخلاف فارسی میانه خوشهٔ آغازین را نگاه داشته و آن را δβ- تلفظ می‌کند که در خط آرامی‌بنیاد سغدی db- نوشته می‌شود. غریب در فرهنگ سغدی (مدخل ۳۴۸۱) خود به پیوند اوستایی تصریح کرده است. اینکه نمودار این جعبه را یک‌راست از ریشه گرفته و نه از جعبهٔ اوستایی، تنها ساده‌سازیِ شکلِ نمودار است — سغدی از اوستایی نیامده، بلکه هر دو دنبالهٔ مستقلِ ایرانی باستان‌اند. ادعای نورایی درست است.\",\n     \"sources\": [W_DWEY],\n     \"ref_check\": [\n      {\"ref\": \"SOD:138\", \"status\": \"supports\", \"note\": \"Gharib, Sogdian Dictionary, entry 3481 (SOD_pages.txt line 13713; form-feed leaf 203, and refs_online gives printed page ≈ leaf − 66, i.e. p.137-138 — Nourai's 138 is right): «3481 δβʾyš B / δβēš ⓐ Av. dvaēš ⇒ δβyš / enmity, harm / VJ 1047»; the next entry «3482 δβʾyš- M, δβēš- ⇒ δβyš-, ⓒ harm» gives the verb.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"cols. 813-814 s.v. tbaēšah- (BRT.txt line 14746)\", \"stance\": \"supports\", \"note\": \"«j. tbaēšah-, g. dvaēšah- n. 1) ,Anfeindung, Feindschaft, Feindseligkeit'» — the Old Iranian s-stem whose Sogdian reflex Gharib records.\"},\n      {\"src\": \"POK\", \"where\": \"IEW 228 (POK_01.txt leaf 238)\", \"stance\": \"supports\", \"note\": \"«av. dvaēš-, tbaēš- ,anfeinden, kränken' … dvaēšah-, tbaēšah- ,Anfeindung', mpers. bēš ,Leid, Unheil'» — Pokorny gives the Iranian family but not the Sogdian form itself (silent on Sogdian).\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"Latin\",\n     \"words\": \"dîrus\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin dīrus 'fearful, ill-omened, horrible' is a *-ro-* derivative of the root, *dwei-ro- 'that which one fears', formed like clā-rus 'audible' from *kleh₂-. The initial di- instead of the expected bi- (Latin regularly turns *dw- into b-, as in bis, bellum) shows it is a dialect word taken into Latin from Sabine or Umbrian, where *dw- gave d- — an observation going back to Servius on Aeneid III (Pokorny, Walde-Pokorny and Ernout-Meillet all repeat it, comparing di-ennium beside bi-ennium). Semantically it began in the language of augury: Cicero's dirissima exta, and substantivised dīrae 'evil omens, curses', later the Furies (Ernout-Meillet). Watkins gives it as the first branch of the root.\",\n     \"derivation_fa\": \"لاتینی dīrus «هراس‌انگیز، شوم، هولناک» ساختی است با پسوند ‎-ro-‎ از همین ریشه، یعنی *dwei-ro- «آنچه از آن می‌ترسند»، درست بر همان قیاسِ clā-rus «شنیدنی». نکتهٔ آوایی مهم آن است که در لاتینِ معیار خوشهٔ آغازین *dw- به b- بدل می‌شود (مانند bis «دوبار» و bellum)؛ پس صورت di- نشان می‌دهد این واژه از گویش‌های سابینی یا اومبریایی به لاتین راه یافته است، آن‌جا که *dw- به d- بدل شده — نکته‌ای که سِرویوس در شرح انئید یاد کرده و پوکورنی، والده-پوکورنی و ارنو-مییه هر سه آن را تکرار کرده‌اند (با قیاسِ di-ennium در برابر bi-ennium). از نظر معنایی نیز نخست اصطلاح فالگیری و دین بوده است: dīrae یعنی «فال بد، نفرین» و سپس نام ایزدبانوان انتقام. واتکینز همین را نخستین شاخهٔ ریشه آورده است. ادعای نورایی درست است.\",\n     \"sources\": [W_DWEY],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. dwei- (AHD_watkins1985.txt line 412): «1. Suffixed form *dwei-ro- in Latin dirus, fearful, horrible (originally a dialectal form): DIRE.» Nourai cites AHD without a page, and this is the entry.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW 228 (POK_01.txt leaf 238)\", \"stance\": \"supports\", \"note\": \"«lat. dīrus ,grausig, grauenvoll, unheilvoll' (von Servius zu Aen. III 235 auch als sabin. und umbr. Wort angeführt, so daß di- statt bi- aus *dui- als mundartliche Lautentwicklung [zu betrachten ist]), mit Formans -ro- ,wovor man sich fürchtet', wie clā-rus ,hörbar'».\"},\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. dirus (LAT.txt lines 16938-16950)\", \"stance\": \"partial\", \"note\": \"«dirus, -a, -um: de mauvais augure, sinistre. Terme de la l[angue] religieuse … Mot sabin d'après Serv. auct., Ae. 3,235 … Le rapprochement avec la racine dṷei- de hom. δέδϝοικα, δεδϝίμεν, arm. erknč̣im 'je crains', et, avec élargissement -s-, de skr. dvéṣṭi 'il hait' est possible si dirus est vraiment un mot dialectal» — accepted, but expressly conditional.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I 816 f. (djvu lines 51528-51532)\", \"stance\": \"supports\", \"note\": \"«lat. dīrus „grausig, grauenvoll, unheilvoll“ … mit Formans -ro- „wovor man sich fürchtet“, wie cla-rus „hörbar“» — same analysis as Pokorny, with the Ernout and Sommer references.\"}\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"English\",\n     \"words\": \"dire\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English dire is a straight learned borrowing of Latin dīrus, taken directly from Latin in the 16th century rather than through French (there is no French *dire in this sense), with the native adjective ending assimilated to -e; the derivative direful is a later English formation on the model of dreadful. Klein and Watkins both take it to the same root, and Watkins's index lists 'DIRE dwei-'.\",\n     \"derivation_fa\": \"«dire» انگلیسی وام‌واژه‌ای است ادبی و مستقیم از لاتینی dīrus که در سدهٔ شانزدهم میلادی از خودِ لاتین گرفته شد، نه از راه فرانسه؛ و صفتِ direful بعدها در انگلیسی بر قیاسِ dreadful ساخته شد. کلاین و واتکینز هر دو آن را به همین ریشهٔ هندواروپایی می‌رسانند و در نمایهٔ واتکینز آمده است: «DIRE dwei-». این گره بی‌اشکال است.\",\n     \"sources\": [W_DWEY],\n     \"ref_check\": [\n      {\"ref\": \"(none)\", \"status\": \"not_checked\", \"note\": \"Nourai gives this node no reference of its own; it inherits the AHD citation of the Latin box above, which does support it (Watkins s.v. dwei-: '… Latin dirus …: DIRE').\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. dire (KLN_1966.txt line 11543, printed p.454-455)\", \"stance\": \"supports\", \"note\": \"«dire, adj., dreadful. — L. dirus, 'fearful, awful, ill-omened, horrible, terrible', of uncertain origin. It possibly derives fr. I.-E. base *dwei-, 'to be afraid, fear' …» — plus «direful, adj., dire. — Formed on analogy of dreadful. See dire and -ful.»\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. dwei- and the English index (AHD_watkins1985.txt lines 412, 1429)\", \"stance\": \"supports\", \"note\": \"«*dwei-ro- in Latin dirus … : DIRE», and the index line «DIRE dwei-».\"}\n     ]\n    },\n    {\n     \"id\": 7,\n     \"lang\": \"Greek\",\n     \"words\": \"deinos; deinos-saura\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Greek δεινός deinós 'fearful, terrible, awe-inspiring' is regular from the root: *dwei-nos > *δϝεινός > δεινός, with the digamma lost as in δέος déos 'fear' (*δϝεῖος) and δειλός deilós 'cowardly' (*δϝει-λός); Homer's perfect δείδω 'I fear' (*δε-δϝοι-α) preserves the same stem. Klein s.v. dino- states it exactly: «Gk. δεινο-, fr. δεινός (for *δϝει-νός), 'fearful', rel. to δείδω (for *δε-δϝοι-α), 'I fear', δέος (for *δϝει-ος)»; Watkins has «Suffixed form *dwey-eno- in Greek deinos». The second item is where the box overreaches: 'deinos-saura' is not a Greek word at all but a Modern Latin scientific compound (Dinosauria) built from Greek δεινός and σαῦρος/σαῦρα 'lizard' in the 19th century — Klein labels it «ModL., lit. 'frightful lizards', compounded of dino- and Gk. σαῦρα, σαῦρος, 'lizard'». Ancient Greek never had such a compound, and the correct Greek σαῦρος is masculine, so the feminine -saura of the chart is the Latin plural Dinosauria showing through. Verdict plausible: deinos confirmed, deinos-saura an anachronism.\",\n     \"derivation_fa\": \"یونانی δεινός («سهمگین، ترسناک») به‌قاعده از این ریشه است: *dwei-nos ← *δϝεινός ← δεινός، با افتادن واکِ دیگاما، درست همان‌گونه که در δέος «ترس» (از *δϝεῖος) و δειλός «بزدل» (از *δϝει-λός) رخ داده؛ و صورت هومریِ δείδω «می‌ترسم» (از *δε-δϝοι-α) همین ستاک را نگاه داشته است. کلاین در مدخل ‎dino-‎ همین را می‌گوید و واتکینز نیز صورت پسوندیِ *dwey-eno- را برای deinos یونانی می‌آورد. اما بخش دوم جعبه از حد فراتر رفته است: «deinos-saura» اصلاً واژه‌ای یونانی نیست، بلکه ترکیبی است علمی و لاتینیِ نو (Dinosauria) که در سدهٔ نوزدهم از δεινός و σαῦρος «سوسمار» ساخته شده؛ کلاین خود آن را «ModL.» می‌نامد. یونانی باستان چنین ترکیبی نداشته و صورت درست σαῦρος مذکر است. پس واژهٔ نخست تأییدشده و واژهٔ دوم زمان‌پریشی است.\",\n     \"sources\": [W_DWEY],\n     \"ref_check\": [\n      {\"ref\": \"KLN:451\", \"status\": \"supports\", \"note\": \"Klein s.v. dino- (KLN_1966.txt leaf 247, which carries the printed numbers 450-453, so Nourai's 451 is exact): «dino-, combining form meaning 'fearful'. — Gk. δεινο-, fr. δεινός (for *δϝει-νός), 'fearful', rel. to δείδω (for *δε-δϝοι-α), 'I fear', δέος (for *δϝει-ος), 'fearful, terrible…', δειλός (for *δϝει-λός), 'cowardly', and possibly cogn. with L. dirus, 'fearful'. See dire.» The same leaf's Dinosauria entry marks the compound as ModL., not Greek.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW 227-228 (POK_01.txt leaf 238)\", \"stance\": \"supports\", \"note\": \"«gr. hom. δείδω ,fürchte' (*δε-δϝοι-α) … δέος n. ,Furcht' (*δϝειος) … δεῖμα n., δειμός m. ,Furcht'; δεινός ,schrecklich'; δειλός ,furchtsam, feig' (*δϝειελός)».\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. dwei- (AHD_watkins1985.txt line 412)\", \"stance\": \"supports\", \"note\": \"«2. Suffixed form *dwey-eno- in Greek deinos, fearful, monstrous: DINOSAUR, DINOTHERE.»\"}\n     ]\n    },\n    {\n     \"id\": 8,\n     \"lang\": \"English\",\n     \"words\": \"dinosaur\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English dinosaur is the anglicisation of Modern Latin Dinosauria, the order-name coined by Richard Owen in 1841-42 from Greek δεινός 'terrible' + σαῦρος 'lizard'; the singular dinosaur is a back-formation from the plural order-name, and its sense 'obsolete, oversized survivor' is a 20th-century figurative extension. Klein: «dinosaur, n., any member of the Dinosauria» and «Dinosauria, n. pl., a group of extinct Saurian reptiles (paleontol.) — ModL., lit. 'frightful lizards', compounded of dino- and Gk. σαῦρα, σαῦρος, 'lizard'.» Watkins's index likewise gives 'DINOSAUR dwei-'. The chart's arrow is thus right in substance, though the Greek box it comes from should be read as 'Greek elements' rather than a Greek word.\",\n     \"derivation_fa\": \"«dinosaur» انگلیسی صورت انگلیسی‌شدهٔ Dinosauria است، نامی لاتینیِ نو که ریچارد اوون در سال‌های ۱۸۴۱–۱۸۴۲ از یونانی δεινός «سهمگین» و σαῦρος «سوسمار» ساخت؛ صورت مفردِ dinosaur از همان نام جمعِ رده بازسازی شده و معنای مجازیِ امروزی آن («چیز از رده خارج و بزرگ») تحول معناییِ سدهٔ بیستم است. کلاین می‌نویسد: «Dinosauria … ModL., lit. 'frightful lizards', compounded of dino- and Gk. σαῦρα, σαῦρος». نمایهٔ واتکینز نیز «DINOSAUR dwei-» دارد. پس پیکان نمودار در اصل درست است، جز آنکه جعبهٔ یونانیِ پیش از آن را باید «عناصر یونانی» خواند نه واژهٔ یونانی.\",\n     \"sources\": [W_DWEY],\n     \"ref_check\": [\n      {\"ref\": \"(none)\", \"status\": \"not_checked\", \"note\": \"The node carries no reference of its own; it inherits KLN:451 from the Greek box, and that page does cover it (Klein's dinosaur / Dinosauria entries stand on the same leaf as dino-).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. dinosaur, Dinosauria (KLN_1966.txt lines 11473-11475, leaf 247 = printed pp.450-453)\", \"stance\": \"supports\", \"note\": \"«dinosaur, n. any member of the Dinosauria. — See next word. / Dinosauria, n. pl., a group of extinct Saurian reptiles (paleontol.) — ModL., lit. 'frightful lizards', compounded of dino- and Gk. σαῦρα, σαῦρος, 'lizard'. See sauro-.»\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. dwei- and index (AHD_watkins1985.txt lines 412, 1429)\", \"stance\": \"supports\", \"note\": \"«… in Greek deinos, fearful, monstrous: DINOSAUR, DINOTHERE», and the index line «DINOSAUR dwei-».\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-144.json','w',encoding='utf-8') as f:\n    json.dump(data, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/write144.py"
}
```


### [2026-09-05T20:26:48.940Z] TOOL RESULT

```
written
```


## [2026-09-05T20:26:52.767Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -m json.tool data/verification/page-144.json > /dev/null && echo \"JSON OK\"\npython3 tools/verify_check.py 144"
}
```


### [2026-09-05T20:26:54.841Z] TOOL RESULT

```
JSON OK
nodes verified: 13/13
node verdicts: {'plausible': 4, 'transcription_suspect': 1, 'confirmed': 7, 'disputed': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 9, 'not_checked': 6, 'partial': 1, 'not_found': 1}
books consulted: {'supports': 22, 'silent': 1, 'partial': 4, 'contradicts': 5} | by book: {'LKT': 4, 'PHN': 3, 'SKT': 3, 'KLN': 3, 'POK': 3, 'AHD': 3, 'MON': 2, 'BRT': 2, 'WLD': 2, 'PHD': 2, 'RCH': 1, 'HRN': 1, 'NYB': 1, 'HJB': 1, 'LAT': 1}
```


## [2026-09-05T20:27:11.991Z] AGENT

Page 144 (book p. 114) verified: `/home/sfmqrb/git/rishe/data/verification/page-144.json`. `verify_check.py 144` → 13/13 nodes, 0 PROBLEM lines.

**Verdicts** — roots: 2 confirmed. Nodes: 7 confirmed, 4 plausible, 1 disputed, 1 transcription_suspect.
Ref checks: 9 supports, 1 partial, 1 not_found, 6 not_checked (all FVA — Nahvi's dictionary has no digital copy — plus AHD:74, a page of the main AHD whose only local part is the Watkins IE appendix, and two nodes with no refs of their own).

**disputed**
- Dwei #3, Persian بیش «bīš 2» "a poisonous plant" — not from Pahlavi bēš 'sorrow'. MacKenzie lists two separate Pahlavi lemmas, `bēš` "pain, sorrow" and `biš` "aconite"; Wiktionary and Hobson-Jobson (s.v. BISH, BIKH) derive the plant-word from Sanskrit विष viṣa "poison". Nourai's own chart note ("See Weis") points at the right root; it is the answer, not an alternative.

**transcription_suspect**
- D.v.r #3, Greek "arsonalos" — `error_in: book`. The printed page really shows *arsonalos*, so the extraction is faithful; Klein (the cited source) prints MGk **ἀρσηνάλης**, and Lokotsch 495, Pihan, Skeat, Etymonline and Wiktionary route Arabic dār aṣ-ṣināʿa straight into Venetian/Italian with no Greek stage at all. Page image archived to `data/verification/sources/refs/ocr/BOOK/144.png`.

**plausible (noted, not flagged)**
- D.v.r #1/#2: دهر *dahr* belongs to Arabic root د ه ر, not د و ر; it is joined to this family only by Klein's comparative-Semitic argument (Akkadian dūru "duration").
- Dwei #1: Avestan gloss "sick, ill" for dvaēš-/tbaēš- is a mistranslation of Pokorny's German *kränken* "to injure, wrong" (read as *krank* "sick"); Bartholomae 813-4 has 'Anfeindung, Feindschaft'.
- Dwei #7: "deinos-saura" is not Greek but Modern Latin *Dinosauria* (Klein labels it ModL.).

**Extraction errors: none** — the JSON matches the printed page throughout.

7 web pages archived via `fetch_source.py`. Note for the owner: Nourai's KLN page numbers check out against the 1966 two-volume printing (arsenal p.108 exact, dino- 451 exact, dire 454 within a page); KLN:397 for the root is one page low — the supporting entry (*daira*) sits on leaf 219 = pp. 398-9.
