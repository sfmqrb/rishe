# Verification process log — verify-page-70


## [2026-09-05T05:22:46.566Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 70 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-70.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-70.json. Write /home/sfmqrb/git/rishe/data/verification/page-70.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 70` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T05:22:47.703Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T05:22:48.443Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T05:22:48.458Z] TOOL RESULT

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


## [2026-09-05T05:22:48.994Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-70.txt"
}
```


### [2026-09-05T05:22:49.009Z] TOOL RESULT

```
1	=== PDF page 70 (book page 40) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Aueg, Aug, Uog, Ug : to increase, strengthen  (refs POK:84)
4	#1 (parent #0) [Avestan] refs=POK:84,85 | ugra : strong ; aojah, aogah : strength
5	  #2 (parent #1) [Avestan] refs=HUB:45; NYB:160; BRT:862 | pairi-aojastara, pari-aužah : all strong, victorious ☞Per 1
6	    #3 (parent #2) [Persian] refs=BRT:862; SNS:144 | pîrŭz «پیروز» : victorious | extra: فیروز | NOTE: HRN:78 derives "pîrŭz" from Avestan "paiti-raočah:toward light" which is not accepted by HUB:45.
7	#4 (parent #0) [Avestan] refs=POK:84,85; SYN:876; SOD:30 | vaxšaiti, uxšyeiti : grows, strengthens, increases ; vaxš 2, uxs : growth
8	  #5 (parent #4) [Avestan] refs=AEF:291 | vana-vaxša : grown in the woods, pansy, violet ☞Wen
9	    #6 (parent #5) [Pahlavi] refs=AEF:291 | vana-vašak : pansy | NOTE: HUB:33 doubts this derivation.
10	      #7 (parent #6) [Persian] refs=AEF:291; BQT:308 | banafšeh «بنفشه» : pansy ; banafš «بنفش» : violet, dark
11	#8 (parent #0) [Old Persian] refs=KNT:177 | vaxš : grow ; u-vaxštra : well grown (a male name) ☞Su 1
12	  #9 (parent #8) [Persian] refs=KNT:177 | Hovaxšatar «هوخشتر» : king of Media
13	#10 (parent #0) [Sogdian] refs=SOD:30 | `xwš`y : to grow
14	#11 (parent #0) [Germanic] refs=AHD:1507 | wahsan : growth, size
15	  #12 (parent #11) [English] refs=AHD | waist
16	#13 (parent #0) [Latin] refs=AHD:1507 | augěre : to increase ; augur : divine favor ; augustus : majestic, august ; auxilium : support, aid
17	  #14 (parent #13) [English] refs=AHD | auction, augment, author ; inaugurate ; August ; auxiliary
18	--- entry 1 ---
19	ROOT Aug -> redirect to Aueg
20	--- entry 2 ---
21	ROOT Auo -> redirect to I 2
22	--- entry 3 ---
23	ROOT Aus 1 -> redirect to Ôus 1
24	
```


## [2026-09-05T05:22:53.059Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-70.json && echo \"=== TOOLS ===\" && ls tools/ && echo \"=== existing verification examples ===\" && ls data/verification/ | head -50",
 "description": "Read page 70 JSON and list tools"
}
```


### [2026-09-05T05:22:53.118Z] TOOL RESULT

```
{
  "pdf_page": 70,
  "book_page": 40,
  "entries": [
    {
      "root": {
        "name": "Aueg, Aug, Uog, Ug",
        "lang": "Indo-European",
        "refs": "POK:84",
        "gloss": "to increase, strengthen"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:84,85",
          "words": [
            {"translit": "ugra", "gloss": "strong", "script": null},
            {"translit": "aojah, aogah", "gloss": "strength", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Avestan",
          "refs": "HUB:45; NYB:160; BRT:862",
          "words": [
            {"translit": "pairi-aojastara, pari-aužah", "gloss": "all strong, victorious", "script": null, "see": ["Per 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BRT:862; SNS:144",
          "words": [
            {"translit": "pîrŭz", "gloss": "victorious", "script": "پیروز"}
          ],
          "script_extra": "فیروز",
          "note": "HRN:78 derives \"pîrŭz\" from Avestan \"paiti-raočah:toward light\" which is not accepted by HUB:45.",
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:84,85; SYN:876; SOD:30",
          "words": [
            {"translit": "vaxšaiti, uxšyeiti", "gloss": "grows, strengthens, increases", "script": null},
            {"translit": "vaxš 2, uxs", "gloss": "growth", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Avestan",
          "refs": "AEF:291",
          "words": [
            {"translit": "vana-vaxša", "gloss": "grown in the woods, pansy, violet", "script": null, "see": ["Wen"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Pahlavi",
          "refs": "AEF:291",
          "words": [
            {"translit": "vana-vašak", "gloss": "pansy", "script": null}
          ],
          "script_extra": null,
          "note": "HUB:33 doubts this derivation.",
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "AEF:291; BQT:308",
          "words": [
            {"translit": "banafšeh", "gloss": "pansy", "script": "بنفشه"},
            {"translit": "banafš", "gloss": "violet, dark", "script": "بنفش"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "جهان شد زگرد سواران بنفش - درخشان سنان و درفشان درفش",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "KNT:177",
          "words": [
            {"translit": "vaxš", "gloss": "grow", "script": null},
            {"translit": "u-vaxštra", "gloss": "well grown (a male name)", "script": null, "see": ["Su 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "KNT:177",
          "words": [
            {"translit": "Hovaxšatar", "gloss": "king of Media", "script": "هوخشتر"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:30",
          "words": [
            {"translit": "`xwš`y", "gloss": "to grow", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD:1507",
          "words": [
            {"translit": "wahsan", "gloss": "growth, size", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "waist", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD:1507",
          "words": [
            {"translit": "augěre", "gloss": "to increase", "script": null},
            {"translit": "augur", "gloss": "divine favor", "script": null},
            {"translit": "augustus", "gloss": "majestic, august", "script": null},
            {"translit": "auxilium", "gloss": "support, aid", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "auction, augment, author", "gloss": null, "script": null},
            {"translit": "inaugurate", "gloss": null, "script": null},
            {"translit": "August", "gloss": null, "script": null},
            {"translit": "auxiliary", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Aug", "redirect": "Aueg"},
      "nodes": []
    },
    {
      "root": {"name": "Auo", "redirect": "I 2"},
      "nodes": []
    },
    {
      "root": {"name": "Aus 1", "redirect": "Ôus 1"},
      "nodes": []
    }
  ]
}
=== TOOLS ===
build_site.py
fetch_source.py
ganjoor.py
__pycache__
ref_index_latin.py
ref_index_pages.py
ref_locator
ref_ocr_book.py
ref_page.py
research.py
validate.py
verify_archive_sources.py
verify_check.py
verify_export_process.py
verify_publish.sh
=== existing verification examples ===
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
process
sources
```


## [2026-09-05T05:22:56.876Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n 1,200p tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-05T05:22:56.939Z] TOOL RESULT

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


## [2026-09-05T05:22:58.745Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','HUB','NYB','BRT','SNS','SYN','SOD','AEF','BQT','KNT','AHD','HRN','WLD','IEC','PHD','MON','ARY','CHEUNG','KLN','SKT','ISS']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n    print()\n\"",
 "description": "Inspect refs_online entries"
}
```


### [2026-09-05T05:23:00.658Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog", "lookup_hint": "Not online (searched archive.org, 

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

CHEUNG null

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

ISS {"title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967", "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute", "kind": "google_books_preview+archive_restricted", "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317936 (v.6, search-only) ; archive.org khotanesetexts0103bail (vols I-III only, lending)", "identifier": "dictionary-of-khotan-saka (substitute); khotanesetexts0103bail is vols I-III, lending-only", "lo
```


## [2026-09-05T05:23:05.160Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-66.json'))\ne=d['entries'][0]\nprint(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1)[:2500])\nprint('--- node 0 ---')\nprint(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:3000])\n\"",
 "description": "Inspect style of page-66 verification"
}
```


### [2026-09-05T05:23:06.808Z] TOOL RESULT

```
{
 "entry": 0,
 "root": "A`.s.r",
 "verdict": "confirmed",
 "modern_form": "Arabic root ع ص ر ʿ-ṣ-r 'to press, squeeze (the juice out)'; West Semitic *ʿṣr 'to press, restrain, retain'",
 "note": "The root box is right on all three counts: the Arabic verb عَصَرَ ʿaṣara 'he pressed, squeezed' is real, the language label is right, and the gloss 'to squeeze (the juice out)' is almost word for word the gloss of the AHD Appendix of Semitic Roots ('ʿṣr — West Semitic, to press, restrain, retain … alizarin, probably from Arabic al-ʿuṣāra, the juice, from ʿaṣara, to squeeze'). Two refinements. (a) The root is not specifically Arabic but common West Semitic: AHD labels it West Semitic and Klein, s.v. alizari, compares Hebrew ʿātzar, Aramaic-Syriac ʿătzar 'he retained' — so 'Arabic' should read 'Arabic (West Semitic)'. (b) The derived noun is vocalised ʿuṣāra عُصَارَة by AHD and by Wiktionary, ʿaṣārah by Klein; Nourai follows Klein's a-vocalism ('a`sârah'), and since both variants are attested this is not an error, only a choice of source. The European branch of the chart (Sp. → Fr. → Eng. alizarin) is Klein's and AHD's account, but AHD hedges it with 'probably', Dozy explicitly declared the origin unknown, and Wiktionary/Webster's 1913 now prefer an Ottoman-Turkish route — see node #3.",
 "note_fa": "ریشهٔ «ع ص ر» به معنای «فشردن، آب چیزی را گرفتن» ریشه‌ای اصیل و درست است و برچسب زبانی و معنای آن در نمودار نورایی با آنچه پیوست ریشه‌های سامی فرهنگ American Heritage می‌آورد یکسان است؛ تنها نکته آن است که این ریشه ویژهٔ عربی نیست و سامی غربی است (کلاین هم عبری «عَصَر» به معنای «نگاه داشتن» را هم‌ریشهٔ آن می‌داند). گونهٔ اسمی آن در فرهنگ‌های امروزی عُصارة و در کلاین عَصارة ضبط شده و نورایی ضبط کلاین را برگزیده است؛ هر دو ضبط پذیرفتنی است و خطا نیست. شاخهٔ اروپایی این نمودار (اسپانیایی ← فرانسوی ← انگلیسی alizarin) از کلاین گرفته شده، ولی همان‌گونه که در گرهٔ ۳ گفته می‌شود، این بخش قطعی نیست و ویکی‌واژه امروزه راه دیگری (از راه ترکی عثمانی) پیشنهاد می‌کند. در مجموع ادعای نورایی دربارهٔ خودِ ریشه درست است.",
 "sources": [
  "https://www.ahdictionary.com/word/semitic.html",
  "https://www.ahdictionary.com/word/search.html?q=alizarin",
  "https://en.wiktionary.org/wiki/عصارة"
 ],
 "ref_check": [
  {
   "ref": "KLN:50",
   "status": "supports",
   "note": "KLN_1966.txt, form-feed leaf 38 (two printed pages per leaf ⇒ printed pp. ~52-53, i.e. Nourai's p.50 ±2): 'alizari, n., madder root. — F., fr. Sp. alizari, fr. Arab. al-'aṣārah, \"the juice\", fr. al-, \"the\", and aṣara, 
--- node 0 ---
{
 "id": 1,
 "lang": "Arabic",
 "words": "a`sârah; al-a`sârah",
 "verdict": "confirmed",
 "derivation": "Arabic عُصَارَة ʿuṣāra (Klein: ʿaṣārah) is the regular fuʿāla/faʿāla noun of result built on the triliteral ʿ-ṣ-r 'to press': Wiktionary defines it as 'somewhat viscose liquid that one obtains by wringing, sap, juice, extract'. Nourai's two lines are one and the same word, indefinite ʿuṣāra and definite al-ʿuṣāra; he lists both because it is the article-bearing shape that travelled into Romance (Sp. alizari), the same fossilised al- seen in alcohol, alidade, alkali, almanac. The word is native Arabic — no Semitic dictionary treats it as a loan — and it is the hinge of both branches of the chart, the Persian loan عصاره and the Spanish/French dye name.",
 "derivation_fa": "واژهٔ عربی عُصارَة بر وزن فُعالَة از ریشهٔ سه‌حرفی «ع ص ر» ساخته شده و به معنای «شیره و مایعی است که از فشردن گیاه به دست می‌آید». دو صورتی که نورایی آورده (عصارة و الْعصارة) در حقیقت یک واژه‌اند، یکی نکره و دیگری معرفه؛ آوردن صورت معرفه از آن روست که همین شکلِ همراه با «الـ» بوده که به زبان‌های اروپایی راه یافته است، درست مانند alcohol و alkali و alidade. این واژه در عربی اصیل است و هیچ فرهنگ سامی آن را وام‌واژه نمی‌داند؛ ادعای نورایی در این گره درست است.",
 "sources": [
  "https://en.wiktionary.org/wiki/عصارة",
  "https://www.ahdictionary.com/word/semitic.html"
 ],
 "ref_check": [
  {
   "ref": "FVA:273",
   "status": "not_checked",
   "note": "no digital copy of Nahvi's dictionary exists (see root ref_check); the page cannot be inspected."
  }
 ],
 "consulted": [
  {
   "src": "KLN",
   "where": "KLN_1966.txt leaf 38 (≈p.52) s.v. alizari",
   "stance": "supports",
   "note": "'fr. Arab. al-'aṣārah, \"the juice\", fr. al-, \"the\", and aṣara, \"he squeezed, pressed\"' — same word, same morphology."
  },
  {
   "src": "AHD",
   "where": "online Appendix of Semitic Roots s.v. ʿṣr",
   "stance": "supports",
   "note": "'ʿṣr — West Semitic, to press. restrain, retain … alizarin, probably from Arabic al-ʿuṣāra, the juice, from ʿaṣara, to squeeze.'"
  },
  {
   "src": "LKT",
   "where": "LKT.txt no. 116 (line 483) 'Ar. ʿasāra'",
   "stance": "supports",
   "note": "'[Vom Vb. ʿasara \"pressen\"] \"der Saft, der durch Pressen aus einer Pflanze gewonnen wird\"' — Lokotsch gives exactly Nourai's derivation of the noun from the verb."
  },
  {
   "src": "PLA",
   "where": "PLA_asbaghi_1988_ia_djvu.txt, grep 'usara/asara'",
   "stance": "silent",
   "note": "Asbaghi's Persische Lehnwörter im Arabischen has no entry — as expected, the word is native Arabic, not a Persian loan into Arabic."
  },
  {
   "src": "AFA",
   "where": "AFA.txt, grep 'usara' (only a false hit at line 9465)",
   "stance": "silent",
   "note": "Fraenkel lists no Aramaic source for ʿuṣāra, i.e. he does not treat it as a foreign word in Arabic."
  }
 ]
}
```


## [2026-09-05T05:23:33.594Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -100 && echo \"=== matrix ===\" && sed -n 1,120p /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md",
 "description": "List reference files and read source matrix"
}
```


### [2026-09-05T05:23:33.654Z] TOOL RESULT

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
=== matrix ===
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


## [2026-09-05T05:23:38.434Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=92 && NR<=94 {print \"=== leaf idx (1-based awk) \" NR \" ===\"; print}' POK_01.txt | head -160",
 "description": "Print Pokorny leaves around p.84"
}
```


### [2026-09-05T05:23:39.958Z] TOOL RESULT

```
=== leaf idx (1-based awk) 92 ===
  Gr.  I  680*.
12-Präsens:  gr.  a%vo)  aus  ^dJ^d-v-Loy  (vgl.  zur  Bildung  Schwyzer  Gr.  Gr. I  694)  und  hvia)  aus  ^dfaveo)  ,reinige  die  Körner  durch  Aufrütteln  von der  Spreu,  beutle',  J^ävat'  TtsoinTiaai  Hes.  (überliefert  ydvai'  utSQimvoai] s.  auch  Bechtel  KZ.  46,  374);  beruht  auf  einem  solchen  schwachstufigen .  n-Präs.,  aber  in  der  Bed.  ,wehen',  auch  apr.  ivins  ,Luft',  Akk.  loinnen ,Wetter'?
83
iO-Präs.  (oder  von  einer  Wzf.  '-"^nei-?):  ai.  väyati  ^weht^^  av.  fraväyeiti verlöscht^;  got.  waian  loaiwö,  ags.  wäwan,  ahd.  wäjan,  wäen  ^wehen^,  aksl. ^eio  vejet^  ^wehen^  und  ^worfeln^  (davon  russ.  vejalo,  sloven.  vevnicaj r,o\n.  loiejaczka  ^Worfschaufel^  Kornschwinge^);  Nominal:  lit.  ue/as  ^Wind^ ; ai.  väyiH,  av.  väyus  ,Wind^  Luft^
für  wurzelhaften  Wert  des  -i-  führt  man  die  Tonstufe  *uf-  in  folgen- den ^yörtern  an^  die  aber  zum  Teil  auch  anderen  Auffassungen  Raum .T-eben:  aksl.  vijah,  vijalica  ^tempestas'^;  russ.  vhjdlica  ^Schneegestöber^ (auch  vejdlica\)y  Vbjuga  ^Schneesturm^,  zavbjdth  ^verschneien^^  cech.  vdti i*vbjati)  ^wehen*^  (erst  slav.  Entwicklungen  aus  vortonigem  vej-?)-  r.-ksl. vich^r^  {*ueisuro-)  ^Wirbelwinde  (jedenfalls  zunächst  zu  russ.  vichatb  ,er- schüttern;  bewegen^,  vichljath  ^schleudern'^;  s.  Brugmann  Grundr.  IP  1049^ Pedersen  IF.  5^  70,  und  wohl  als  _,wirbela;  im  Kreise  schwingen^  zu  *ueis- drehen^);  lit.  vydra,  vidras  ^Sturmwind^  (s.  Leskien  Bild.  438;  das  im Lit.  sehr  seltene  Formans  -dra  —  vgl.  echt  lit.  vetra  ^Sturm^  —  mahnt zur  Vorsicht);
hom.  ^Lov  "^TOQy  d-vf.idv  ^.laOsj  cctcfS-cov  vom  Aushauchen  oder  Auslassen der  Lebenskraft  (zur  Bed.  zuletzt  Bechtel  Lexil  21  f.);  gr.  Wz.  dJ^ia--, mcymr.  aioyd  s.  82  oben.
h.  aue-d-:  ahd.  wäzan,  wiaz,  mhd.  loäzen  ^wehen^  blasen^^  wäz  ^Wind- stoß^;  lit.  vedinti  ^lüften^  kühlen^;  allenfalls  gr.  äaC,o)  ^hauche^  aus  ^^äfdö-m (eher  aber  gr.  Neuschöpfung  nach  anderen  Verben  auf  -a^w);  vermutlich auch  (aus  *aiid-d-ro-)  lit.  dudi^a  m.  ^Sturm^^  n.  ^Gewitter^;  apr.  wydra yWind^  über  ai.  üdhar  n.  ^Kälte^^  av.  aodard,  aota  ds.  vgl.  Persson  Beitr.  11.
c.  ue-lO'  vielleicht  in  lat.  evelätus  ^eventilatus^  unde  velabra,  quibus frumenta  eventilantur^  (Paul.  Fest.  68,  3)  und  in  ahd.  wäla  m.  n.  ^Fächer^ (wenn  nicht  aus  *ice-pla,  s.  unten)?
d.  ue-s-:  ai.  väsa-hj  väsaJca-h  ^Wohlgeruch^^  väsayati  _,füllt  mit  Wohl- geruch^;  samväsita-h  ^stinkend  gemacht^;  isl.  väs  _
=== leaf idx (1-based awk) 93 ===
,aura  refrigeranse_,  vzsa ^spirare^;  ndl.  loaas  ^Reif^  Duft^,  lit.  vestu^  vesti  ^sich  abkühlen,  kühl  oder luftig  werden*^,  vesä  ,kühle  Luft,  Kühle',  vesus  ,kühl,  luftig^
e.  f- Weiterbildungen:  ai.  väta-h,  av.  vätö  ^Wind^^  ai.  vätula-h  (s.  unten), gr.  är^xr^g  ,Wehere,  drjffvgog  ,windig,  luftig^  =  ai.  vätula  ,windige  (auch  ,ver- rückt*^;  dazu  auch  vielleicht  gr.  ärjavXog  ,freventliche  nach  Brugmann BSGW.  1901,  94;  trotz  aiovXoq  ds.  nicht  nach  Becbtel  Lexil.  15  zu  ai. yatu-h  ,Spuke);  lat.  vannus  ,Futterschwingee  (aus  *uat-n6-s,  vgl.  das  Demin. vatillum  ursprüngl.  ,,eine  kleine  Worfschaufel^;  aus  dem  Lat.  stammt  ahd. tuanna,  ags.  fann  ^Futterschwinge^,  auch  nhd.  Wanne);  anord.  vel,  veli ,Wedel,  Schweife  (über  synkopiertes  *vepia-  aus  *vapila-),  ahd.  2vedil  ds. ; ahd.  wadal  ^Wedel^,  Adj.  ,sch weifend,  unstet,  Bettler^^  loadalön  ,schweifene
6*
84
(urgermanisch  *wapla-,  idg.  *ud-tlo-),  ags.  ivapol  ^wandernd^  w'^dla  .Bett-' ler_,  arm^^  wöedl  ^Armut^,  lucedlian  ^betteln^  arm  sein'  (urgermanisch  ^^wepla-), woneben  ahd.  luallön  ^wandern;,  umherziehen,  wallfahrten',  ags.  iceallian ^wandern' (aus  "^icädlö-ja-n)]  ahd.  loäla  ^Fächer'  (aus  *ive-pla- oder  *we-la-'^ s.  oben);  lit.  vetra  ,Sturm,  Unwetter';  aksl.  vetn  ^huit,  AVind',  apr.  icetro ,Wind';  lit.  vetyti  ^worfeln'.  |
Über  ai.  upa-väjayati  ,facht  das  Feuer  an'  (von  Pänini  als  Kaus.  zu vä-  gefaßt)  s.  Wackernagel  KZ.  43,  292.  ^
Vielleicht  hierher  gr.  äe&Xog  (s.  11.  aue-   ,sich  mühen')  als  ^Keuchen'?
WP.  I  220 f.,  Feist  565  a,  Trautmann  345,  Schwyzer  Gr.  Gr.  I  680.
II.  aue-  (ue-d(h)-?)  ,sich  mühen,  anstrengen'?
Solmsen  Unters.  267  f.  verbindet  ai.  väyatij  -te  ,wird  müde,  wird  er- schöpft, ermattet'  mit  gr.  äs&Xog  ,Mühsal,  Wettkampf'  (^IcJ^e-d-Xog),  ^sd-lov, ä-9-Xov  ,Kampf,  Kampfpreis,  Kampfplatz',  wobei  d-  entweder  Vorschlags-' vokal  ist  oder  eine  vollere  Wzf.  *aue-  neben  *we-  voraussetzt.  Damit" allenfalls  vereinbar  ist  Zupitzas  KZ.  37,  405  Vergleich  der  gr.  Worte  mit mir.  feidm  , Anstrengung', /ec^i'Z  ,ausdauernd',  air.  ni '  fedligedar  ,non  manet' (wobei  formale  Verhältnisse  wie  *me-  ,messen' :  *med-,  *ue-  ,wehen' :  anord. vedvj  nhd.  Wetter  vergleichbar  wären),  wozu  Pedersen  KG.  I  110,  cymr. gweddil  ,remnant,  leavings'  (daraus  mir.  fuidell)  stellt;  hierher  toch.  B ivaimene  ,schwierig'?
Doch  ist  die  Zusammenstellung  in  allen  ihren  Gliedern  ganz  unsicher. Für  väyati  wird  ,sich  anstrengen'  als  Gdbed.  in  Frage  gestellt  durch  die Bed.  ,austrocknen'  von  väna  ,trocken',  upa-väyati  ,durch  Vertrocknen ausgehen,  vertrocknen',  upaväta-  ,trocken  geworden';  und  in  üed-Xog  löst sich  am  nat�
=== leaf idx (1-based awk) 94 ===
�rlichsten  -&Xo-  als  suffixal  ab,  während  der  Dental  der  ir. Worte  wurzelhaftes  d  oder  dh  ist,  also  bestenfalls  recht  entfernte  Ver- wandtschaft bestünde.
WP.  I  223,  Van  Windekens  Lexique  149.
^^^S-f  W^g-,  aug-,  ug-   ,vermehren,   zunehmen',   mit   s-Formans    aueks-, auk-s-,  uek'S-,  uk-s-.
Ai.  ugrd-  ,gewaltig'  (Komp.  Sup.  öjiyas-,  öjutha-  ,der  kräftigere,  kräf- tigste') ==  av.  ugra-  ,stark,  kräftig-  (Komp.  Sup.  aojyah-,  aojista-).
lat.    augeö,   -ere    ,vermehren',    auctoi-   (=  umbr.  uhtur)    ,Urheber   usw.', auctiö  ,Versteigerung',   augmen{tum)   , Zuwachs'   (=   lit.    augmud  ,Wachs-  ' tum',  ai.  öjmdn-  m.  ,Kraft'),   aiigur  ,Weissager'   aus  *auqos  ,Vermehruno' (WH.  I  83);
85
o-ot.  aukan  (Prät.  aiauk),  auknan  ^sich  mehren^^  cma-,  hi-aukan  ^hinzu- füo-en^  ahd.  ouhJiön,  as.  ökian  ^vermehren^;,  ags.  eacian  ^zunehmen'^^  tecan mehren^;  anord.  auka  (Prät.  jök  und  aukada)  ^vermehren^;  st.  Partiz.  ags. cacen    as.  ö/can  ^vermehrt^  schwanger^;
lit.  a-ii^^^^  «w^2^t  (dehnstufig-)  ^wachse^^  auginu,  -inti  ^wachsen  lassen, erziehen'^,  ablautend  pa-ügeti  ^heranwachsen^,  ügis  ,Wuchs,  Jahreswuchs^, lett.  aüdzet,  aüdzindt  ^aufziehen'^,  apr.  auginnons  Part.  Perf.  Akt.  ,gezogen^, alett.  aukts  ,hoch^  =  lat.  aiictus,  lett.  aügt  ,wachsen^,  wie  auch  thrak. y^v-d-i-rtaoog  ,Hohenfurt^,  apr.  Aucti-garhin,  aucktai-rikijskan  ,Obrigkeit^, aucktimmien  , Vorsteher^,  woneben  mit  dem  s  des  -es-St.  (s.  unten)  lit. dukstas,  lett.  aüksts  ,hoch^  (:  lat.  augustus  ^erhaben'^),  apr.  auck-timmiskan f.  (Akk.)  ^Obrigkeit*^,  apr.  aügus  ,geizig^  (als  ,mehrend^),  lit.  dugumas, lett.  ailgums  ,Wachstum^;
es-St.  ai.  öjas-  n.  ,Kraft,  Stärke^,  av.  aojah-,  aogah-  (ebenso  r-St. aogard)  ,Kraft,  Stärke^,  lat.  augustus  s.  oben  (ebenso  lit.  usw.  dukstas)] dazu  mit  s  im  Verbum:
ai.  vdksana-m  ,Stärkung^,  vaksdyati  ^läßt  wachsen^,  av.  vaxsaiti  ,läßt wachsen^,  woneben  mit  schwächster  Wzstufe  ai.  üksati  ,erstarkt^  (Perf. vavdksa),  av.  uxsyeiti  ,wächst^;  got.  loahsjan  ,wachsen^  (=  ai.  vaksayati, idg.  Iter.-Kaus.  Hwkseiö]  damit  verband  sich  das  ö-stufige  FerL  ivöhs  zum Paradigma;  s.  Brugmann  IF.  32,  180,  189);
gr.  d^J^'Ji^a)  ,mehre^,  äs^oiiai  ,wachse'^;  ai/^w,  av^avo)  ,vermehre,  ,stei- gere*^,  lat.  auxüium  ,Hilfe^  (ursprüngl.  PI.  -ia  ,Verstärkungen,  Hilfs- truppen^,  N.  PL  eines  auxilis  ,zur  Verstärkung  dienlich^);
anord.  vaxa,  vexa  ,wachsen^,  ahd.  waTisan,  nhd.  wachsen,  wuchs,  wozu z.  B.  got.  wahstus  ,Wachstum,  Wuchs,  Leibesgröße^,  ahd.  ica{h)smo  ,Wachs- tum^  u.  dgl. ;  toch.  A  oksls  ,wächst',  A  oksu,  B  auksu  ,alt^;  nach  Yan Windekens  Lexique  79  auch  hierher  AB  oko  ,Frucht*^,  A  okar  ,Pflanze^; dagegen  Pedersen  Tochar.  227.
Hierher  mit  Dehnstufe  udg-:  got.  loökrs  m.  ,Zins^,  ags.  icöco7'
```


## [2026-09-05T05:23:50.480Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD watkins aug- ===\" && grep -n -i -A25 '^aug-' AHD_watkins1985.txt | head -60",
 "description": "Grep Watkins AHD for aug-"
}
```


### [2026-09-05T05:23:50.545Z] TOOL RESULT

```
=== AHD watkins aug- ===
307:aug-'. To increase. Variant *(a)weg- (< *aweg-). 1. Ger- manic *aukan in: a. Old English éacan, écan, to increase: EKE!; b. Old English éaca, an addition: NICKNAME. 2. Variant extended forms *wogs-, *wegs- in Germanic *wahsan in Old English weaxan, to grow: WAX. 3. Form *aug-é- in: Latin augére, to increase: AUCTION, AUGEND, AUGMENT, AUTHOR, (AUTHORIZE), (OCTROI). 4. Latin augur, diviner (< “he who obtains favorable presage” < “divine favor, increase”): AUGUR; INAUGURATE. 5. Latin augustus, majestic, august: AUGUST. 6. Suffixed form *aug-s- in: a. Latin auxilium, aid, support, assistance: AUXILIARY; b. Greek auxein, to increase: AUXIN; ¢. Greek auxanein, to increase: AUXESIS. [Pok. aweg- 84.]
308:aug-?. To shine. Suffixed form *aug-d- in Greek augé,
309-light, ray: AUGITE. [Pok. aug- 87.]
310-aukv-, Cooking pot. 1. Germanic suffixed form *uhw-na- in *ufna- in Old English ofen, furnace, oven: OVEN. 2. Suffixed form *auk-sld- in Latin aulla, aula, olla, pot,
311-jar: OLLA. [Pok. aug(h)- 88.]
312-aulo-. Hole, cavity. 1. Metathetic form *alwo- in Latin
313-bat-
314-alvus, the belly, stomach: ALVEOLUuS. 2. Greek aulos, pipe, flute, hollow tube: CAROL, HYDRAULIC. [Pok. au- lo-s 88.]
315-[aurum. Gold. Latin noun with preform *aus-o- probably from a root *aus-. Latin aurum (> French or), gold: AUREATE, AUREOLE, AURIC; AURIFEROUS, DORY?, EYRIR, OR’, ORE, ORIFLAMME, ORIOLE, ORMOLU, OROIDE, OR- PHREY, ORPIMENT.]
316-aus-', To shine. 1. Germanic *aust- in: a. Old English éast, east (< “the direction of the sunrise”): EAST; b. Old High German 6stan, east: OSTMARK. 2. Germanic *aus- tra- in: a. Old English éasterne, eastern: EASTERN; b. Late Latin ostro-, eastern: OsTROGOTH. 3. Germanic *austron-, a dawn-goddess whose holiday was celebrated at the vernal equinox, in Old English éastre, Easter: EAsTER. 4. Probably suffixed form *ausds-, dawn, also Indo-European goddess of the dawn, in: a. Latin auréra, dawn: AURORA; b. Greek éds, dawn: EO-, Eos; EOSIN. [Pok. aues- 86.]
317-aus-?. To draw water. Suffixed form *aus-yo- in Latin haurire, to draw up: EXHAUST, HAUSTELLUM, HAUSTO- RIUM. [Pok. aus- 90.] awi-. Bird. I. 1. Latin avis, bird: AVIAN, AVIARY, AVI- ATION; AVICULTURE, AVIFAUNA, BUSTARD, OCARINA, OSPREY, OSTRICH. 2. Compound *awi-spek-, “observer of birds” (*spek-, to see; see spek-), in Latin auspex, augur: AuSPICE. II. Possible derivatives are the Indo-European words for egg, *dwyo-, *ayo-. 1.Germanic *ajja(m) in: a. Old English 2g, egg: COCKNEY; b. Old Norse egg, egg: EGG. 2, Latin 6uum, egg: OVAL, OVARY, OVATE, OVI-, OVOLO, OVULE, OVUM. 3. Greek dion, egg: 00-. [Pok. auei- 86.] awo-. An adult male relative other than one’s father. 1. Latin avus, grandfather: ATAVISM. 2. Latin avunculus, maternal uncle: AVUNCULAR, UNCLE. 3. Latin avia, grandmother: AYAH. [Pok. auo-s 89.] ayer-. Day, morning. 1. Germanic “*airiz in: a. Old Eng- lish &r, before: EARLY, ERE; b. Old Norse dr, before: OR2. 2. Germanic (superlative) *airistaz in Old English rest, earliest: ERST. [Pok. ajer- 12.] ayes-. A metal, copper or bronze. Latin aes, bronze, money: AENEOUS, ERA. [Pok. aios- 15.] baba-. Root imitative of unarticulated or indistinct speech; also a child’s nursery word for a baby and for various relatives. 1. Middle English babelen, to babble: BABBLE. 2. Middle English babe, babi, baby: BABE, BABY. 3. Italian bambo, child, simpleton: BAMBINO. 4. Polish baba (diminutive babka), old woman: BABA, BABKA. 5. Russian baba, old woman: BABUSHKA. 6. Rus- sian balalaika, balalaika (imitative of the sound): BALA- LAIKA. 7. Latin balbus, stuttering, stammering: BOOBY. 8. Greek barbaros, non-Greek, foreign, rude (< “one who speaks incomprehensibly”): (BARBARIAN), BARBARISM, BARBAROUS. 9. Hindi babi, father: BABU. [Pok. baba- 91.] badyo-. Yellow, brown. A Western Indo-European word. Latin badius, chestnut brown (used only of horses): BAY’. [Pok. badios 92.] bak-. Staff used for support. 1. Probably Middle Dutch pegge (> Middle English pegge), pin, peg: PEG. 2. Latin baculum, rod, walking stick: BACILLUS, BAGUETTE; BAC- ULIFORM, DEBACLE, IMBECILE. 3. Greek baktron, staff: BACTERIUM; (CORYNEBACTERIUM). [Pok. bak- 93.] bamb-. Word imitative of dull or rumbling sounds. Greek bombos, a booming, humming: BOMB, (BOMBARD), BOUND}. [Pok. ba*mb- 93.] bands. A drop. Possibly Irish bainne, milk: BONNYCLAB- BER. [Pok. band- 95.]
318-[bassus. Low. Late Latin adjective (> Medieval Latin bassus, Old French bas, and Middle English bas), possi- bly from Oscan: BASE?, BASS?, BASSET!, BASSO; ABASE, BAS-RELIEF, (DEBASE).]
319-[bat-. Yawning. Latin root of unknown origin; probably imitative. 1. Latin *batdre (> Old French ba(y)er), to
320-battuere
321-yawn, gape: BAY2, BEVEL; ABASH, ABEYANCE. 2. Possibly Vulgar Latin *abbaidre (> Old French (a)baiier), to bay: BAY‘*.] [battuere. To beat. Latin verb of unknown origin. (BATE?), BATTER!, (BATTER’), (BATTERY), BATTLE; ABATE, COMBAT, DEBATE, (RABBET), (REBATE?), (RE- BATO).] bel-. Strong. 1. Suffixed o-grade form *bol-iyo- in Russian bol’shoi, large: BOLSHEVIK. 2. Prefixed form *dé-bel-i- (dé-, privative prefix; see de-), “without strength,” in Latin débilis, weak: DEBILITATE, DEBILITY. [Pok. 2. bel- 96.] bend-. Protruding point. 1. Germanic *pannja-, “struc- ture of stakes,” in Old English penn, pen for cattle: PEN2. 2. Germanic *pund- possibly in Old English pund- (> Middle English pound), pundfald, enclosure for stray animals: POND, POUND3; IMPOUND, PINFOLD. 3. Germanic *pin- in Old English pintel, penis: PINTLE. [Pok. bend- 96.) beu-'. Also bheu-. Appears in words loosely associated with the notion “to swell.” I. Root form *beu-. 1. Ger- manic *puk- in: a. Old English pocc, pustule: POCK; b. Old French po(u)che and Old North French poke, bag: POACH!, POCKET, POKE3, POUCH, (PUCKER). 2. Old Eng- lish pyffan, to blow out: puFF. 3. Old English -piite, “fish with large head” (in aele-piite, eelpout): pouT?. II. Root form *bheu- with various Germanic derivatives. 1. Old English bdsm, bosom: Bosom. 2. Old English biic, belly, pitcher: BUCKBOARD. 3. Frankish *biak (> Old French buc), trunk of the body: TREBUCHET. 4. Old English bye), pustule: BorL?. 5. German dialectal baustern, to swell, akin to the source of Middle English bost, a bragging: BoasT!. III. Root form *beu-. 1. Latin bulla, bubble, round object, amulet (> Old French boule and Spanish bola, ball): BILL!, BILLET!, BOLA, BOULE?, BOWL’, (BULL?2), BULLA, BULLATE, BULLET, (BULLETIN); BOULE- VERSEMENT. 2. Latin bullire (> French bouiller), to bubble, boil: BOIL!, BOUILLON, BUDGE!, (BULLION), BULLY?; BOUILLABAISSE, EBULLIENCE, GARBOIL, PAR- BOIL. 3. Possibly Latin bucca (> Old French boucle, buckle, curl, and Spanish boca, mouth), (inflated) cheek: BOCACCIO, BOUCLE, BUCCAL, BUCKLE!, BUCKLE?; DE- BOUCH, DISEMBOGUE, EMBOUCHURE. 4. Greek boubén, groin, swollen gland: BUBO. [Pok. 2. beu- 98.] beu-2. Root imitative of muffled sounds. 1. Latin bitié (perhaps > Old French butor), bittern: BITTERN!. 2. Latin bited, a kind of hawk: BUZZARD. [Pok. 1. b(e)u- 97.] bha-'. To shine. Contracted from *bhas-. 1. Germanic *baukna-, beacon, signal, in: a. Old English béac(e)n, beacon: BEACON; b. Old English denominative bécnan, biecnan, to make a sign, beckon: BECKON. 2. Perhaps Germanic *bazja-, berry (< “bright-colored fruit”), in Old English berie, berige, berry: BERRY. 3. Germanic *bandwa-, “identifying sign,” banner, standard, sash, also “company united under a (particular) banner,” in: a. Spanish banda, sash: BANDOLEER; b. Late Latin ban- dum, banner, standard: BANNER, (BANNERET). 4. Suf- fixed form *bhaw-es- in Greek phds (stem phét-), light: PHOS-, PHOT, PHOTO-; PHOSPHORUS. 5. Extended and suffixed form *bhan-yo- in Greek phainein, “to bring to light,” cause to appear, show, and phainesthai (passive), “to be brought to light,” appear: FANTASY, (PANT), PHANTASM, (PHANTOM), PHASE, PHENO-, PHENOMENON; DIAPHANOUS, EMPHASIS, EPIPHANY, HIEROPHANT, PHAN- EROGAM, (PHANTASMAGORIA), PHOSPHENE, SYCOPHANT, THEOPHANY, (TIFFANY). [Pok. 1 bha@- 104.] bha-2. To speak. Contracted from *bhaa-. 1. Latin fari, to speak: FATE; AFFABLE, (FANTOCCINI), INEFFABLE, IN- FANT, (INFANTRY), PREFACE. 2. Greek phanai, to speak: -PHASIA; PROPHET. 3. Suffixed form in Germanic *ban- wan, *bannan, to speak publicly (used of particular kinds of proclamation in feudal or prefeudal custom; “to proclaim under penalty, summon to the levy, declare
322-bhares-
323-outlaw”), in: a. Old English bannan, to summon, pro- claim, and Old Norse banna, to prohibit, curse: BAN}; b. Old French ban, feudal jurisdiction, summons to military service, proclamation, Old French bandon, power, and Old English gebann, proclamation: BANAL, BANNS; ABANDON; C. Old French banir, to banish: BAN- ISH; d. Late Latin bannus, bannum, proclamation: Ccon- TRABAND; @. Italian bandire, to muster, band together (< “to have been summoned”): BANDIT. 4. Suffixed form *bha-ni in Germanic *b6dni- in Old Norse b6n, prayer, request: BOON!. 5. Suffixed form *bhd-ma in: a. Latin fama, talk, reputation, fame: FAME, FAMOUS; DEFAME, INFAMOUS; b. Greek phémé, saying, speech: EUPHEMISM. 6. Suffixed o-grade form *bhd-nd in Greek phéné, voice, sound, and phénein, to speak: PHONE, -PHONE, PHO- NEME, PHONETIC, PHONO-, -PHONY; ANTHEM, (ANTI- PHON), APHONIA, CACOPHONOUS, EUPHONY, SYMPHONY. 7. Suffixed zero-grade form *bha-to- in Latin fatéri, to acknowledge, admit: CONFESS, PROFESS. 8. Greek blas- phémos, evil-speaking, blasphemous (first element ob- scure): (BLAME), (BLASPHEME), BLASPHEMOUS. [Pok. 2. bha- 105.] bha-bha-. Broad bean. 1. Latin faba, broad bean: FAVA BEAN. 2. Variant form *bha-un- in Germanic *bauné in Old English béan, broad bean, bean of any kind: BEAN. [Pok. bhabhé 106.] bhad-. Good. 1. Germanic (comparative) *batiz6 in Old English betera, better: BETTER. 2. Germanic (superla- tive) *batistaz in Old English bet(e)st, best: BEST. 3. Ger- manic noun *b6¢6 in Old English bét, remedy, aid: BooT?. 4. Germanic verb *batnan, to become better, in Old Norse batna, to improve: BATTEN!. [Pok. bhdd- 106.] bhag-'. To share out, apportion, also to get a share. 1. Greek phagein, to eat (< “to have a share of food”): -PHAGE, -PHAGIA, PHAGO-, -PHAGOUS. 2. Extended form *bhags- in Avestan bakhsh- in Persian bakhshidan, to give: BAKSHEESH, (BUCKSHEE). [Pok. 1. bhag- 107.] bhag-. Sharp. Suffixed form *bhag-ro- in Greek phag- ros, whetstone, also a name for the sea bream: PORGY. [Pok. 2. bhag- 107.] bhaghu-. Arm. Germanic *bdguz in Old English bdg, boh, bough: BouGu. [Pok. bhdghii-s 108.] bhago-. Beech tree. 1. Germanic *b6k6, beech, also “beech staff for carving runes on” (an early Germanic graphic device), in: a. Old English bdc, written docu- ment, composition: BOOK; b. Middle Dutch boek, beech: BUCKWHEAT. 2. Germanic *bdkjdn- in Old English béce, beech: BEECH. [Pok. bhdgo-s 107.] bhar-. Also bhor-. Projection, bristle, point. 1. Suffixed o-grade form *bhor-so- in Germanic *barsaz in Old English bzrs, perch, bass (a fish that has a spiny dorsal fin): BASs!. 2. Suffixed zero-grade form *bhAr-sti- in Germanic *bursti- in Old English byrst (> Middle Eng- lish bristel), bristle: BRISTLE. 3. Extended zero-grade form *bhrs- in: a. Germanic *bur- in Swedish borre, bur, perhaps akin to the Scandinavian source of Middle English burre, bur: BUR}; b. suffixed form *bhrs-dh- in Germanic *bruzd-, point, needle, in Old Norse broddr, spike: BRAD; C. suffixed form *bhrs-ti- in Latin fastig- ium, summit, top, extremity: FASTIGIATE, FASTIGIUM; d. possibly suffixed form *bhrs-tu- in Latin fastus, fasti- dium, disdain (from the notion of prickliness): FASTIDI- ous; e. suffixed form *bhrs-tio- in Russian borshch, cow parsley: BORSCHT. [Pok. bhar- 108.] bhardha. Beard. Possibly related to bhar-. 1. Germanic *bardaz in Old English beard, beard: BEARD. 2. Ger- manic *bard6, beard, also hatchet, broadax (the associ- ation of beard and ax is attested elsewhere in the Indo-European family; both were symbols of patriarchal authority), in Old High German barta, beard, ax: HAL- BERD. 3. Latin barba, beard: BARB!, BARBEL, BARBEL- LATE, BARBER, BARBETTE, BARBICEL, BARBULE; REBARBATIVE. [Pok. bhardhé 110.] bhares-. Also bhars-. Barley. 1. Germanic *barz- in Old
324-bhasko-
325-English bere, bere, berlic, barley: BARLEY; BARN. 2. Latin far (stem farr-), spelt, grain: FARINA, (FARINA- CEOUS), FARRAGINOUS, FARRAGO. [Pok. bhares- 111.] bhasko-. Band, bundle. 1. Latin fascis, bundle (as of rods, twigs, or straw), also crowd of people: FASCES, FASCICLE, FASCINE, FASCISM. 2. Latin fascia, band, fillet, bandage: FASCIA, FESS. 3. Probably Latin fascinum, fascinus, an amulet in the shape of a phallus, hence a bewitching: FASCINATE. [Pok. bhasko- 111.] bhau-. To strike. 1. Germanic *bautan in: a. Old English béatan, to beat: BEAT; b. German bosseln, to do odd jobs: BUSHEL?. 2. Germanic *bautilaz, hammer, in Old English bietel, hammer, mallet: BEETLE’. 3. Germanic “bitaz in Old English diminutive buttuc, end, strip of land: BUTTOCK. 4. Germanic *butt-, name for a flatfish, in Middle Dutch butte, flatfish: HALIBUT. 5. Germanic *buttan in Old French bo(u)ter, to strike, push (> French bouton, button): BOUTON, BUTT!, BUTTON, BUTTRESS; ABUT, REBUT, SACKBUT. 6. Variant form *bhit- in: a. Latin confiitdre, to check, suppress, restrain (com-, intensive prefix; see kom): CONFUTE; b. Latin refiitdre, to drive back, rebut (re-, back; see re-): REFUTE. [Pok. 1. bhau- 112.] bhé-. To warm. Contracted from *bheo. 1. Suffixed zero-grade form *bha-to- in Germanic *batham in Old English beth, a bath, and its denominative bathian, to bathe: BATH!, BATHE. 2. Suffixed zero-grade form *bha-g- in: a. Germanic *bakan in Old English bacan, to bake: BAKE; b. Germanic *bakkan in German backen, to bake: ZWIEBACK. [Pok. bhé- 113.] bhedh-. To dig. 1. Germanic *badjam, garden plot, also sleeping place, in Old English bed(d), bed: BED. 2. O-grade form *bhodh- in: a. Latin fodere, to dig: FOSSA, (FOSSE), FOSSIL, FOSSORIAL; b. perhaps Greek bothros, pit: BOTHRIUM. [Pok. 1. bhedh- 113.] bheg-. To break. Akin to bhreg-. Possibly in various Germanic forms. 1. Germanic nasalized form *bang- in: a. Old Norse banga, a hammering, akin to the probable Scandinavian source of English BANG!; b. Swedish dia- lectal bangla, to work inefficiently, akin to the possible Scandinavian source of English BUNGLE. 2. Possibly Germanic nasalized forms *bankiz and *bank6én-, bank of earth (possibly < “feature where the contour of the ground is broken,” escarpment, riverbank, possibly also associated with “manmade earthwork’’), later also bench, table, in: a. Old English benc, bench: BENCH; b. Old Danish banke, sandbank, akin to the Scandinavian source of BANK}; c. Old High German banc, bank, bench, moneychanger’s table (> Italian banca): BANK?, BANT- LING, BUNCO; BANKRUPT; d. Old French banc, bench: BANK, BANQUET; @. Provencal banca, bench: BAN- QUETTE. [Pok. bheg- 115.] bhegr-. To run away. 1. Germanic *bakjaz, a stream, in Old Norse bekkr, a stream: BECK?. 2. Greek phebesthai, to flee in terror, forming phobos, panic, flight, fear: -PHOBE, -PHOBIA. [Pok. bhegy- 116.] bhei-'. A bee. Germanic suffixed form *bidn- in Old English 6é0, a bee: BEE}. [Pok. bhei- 116.] bhei-2. To strike. 1. Germanic suffixed form *bili- in Old English bile, bird’s beak: BILL?. 2. Germanic suffixed form *bilja- in Old English bil), sharp weapon: BILL’. [Pok. bhei(a)- 117.] bheid-. To split; with Germanic derivatives referring to biting (hence also to eating and to hunting) and wood- working. 1. Germanic *bitan in Old English *bitan, to bite: BEETLE!, BITE. 2. Zero-grade form *bhid- in: a. Ger- manic *bitiz in Old English bite, a bite, sting: B1T?; b. Germanic *bitén- in Old English bita, a piece bitten off, morsel: BIT!; c. Suffixed form *bhid-ro- in Old English bit(tjer, ‘‘biting,’’ sharp, bitter: BITTER. 3. O-grade form *bhoid- in Germanic *baitjan in: a. Old Norse beita (verb), to hunt with dogs, and beita (noun), pasture, food: BAIT!; b. Old French beter, to harass with dogs: ABET. 4. Germanic *bait-, a boat (< “dugout
326-bhel-?
327-canoe” or “split planking”), in Old English baz, boat, and Old Norse bdtr, boat: BATEAU, BOAT; (BOATSWAIN). 5. Nasalized zero-grade form *bhi-n-d- in Latin findere (past participle fissus), to split: -FID, FISSI-, (FISSILE), FISSION, (FISSURE). [Pok. bheid- 116.]
328-bheidh-. To persuade, compel, confide. 1. Probably Ger- manic *bidan, to await (< “to await trustingly, expect, trust”), in Old English bidan, to wait, stay: BIDE; ABIDE, (ABODE). 2. Latin fidere, to trust, confide, and fidus, faithful: FIANCE, FIDUCIAL, (FIDUCIARY); AFFIANCE, (AFFIANT), (AFFIDAVIT), (CONFIDANT), CONFIDE, (CONFI- DENT), (DEFIANCE), DEFY, DIFFIDENT. 3. Suffixed o-grade form *bhoidh-es- in Latin foedus (stem foeder-), treaty, league: FEDERAL, FEDERATE; CONFEDERATE. 4. Zero-grade form *bhidh- in Latin fidés, faith, trust: FAITH, FEALTY, FIDELITY; INFIDEL, PERFIDY. [Pok. bheidh- 117.] bheig-. To shine. An uncertain but plausible root. Greek phoibos, shining: PHOEBE, PHOEBUS. [Pok. bheigz- 118.] bhel-'. To shine, flash, burn; shining white and various bright colors. I. 1. Russian byelii, white: BELUGA. 2. Greek phalaros, having a white spot (> phalaris, coot): PHALAROPE. II. 1. Suffixed variant form *bhié-wo- in Germanic *bléwaz, blue, in Old French bleu: BLUE. 2. Suffixed zero-grade form *bhb-wo- in Latin flavus, golden or reddish yellow: FLAVESCENT, FLAVO-; (FLAVIN), (FLAVONE), (FLAVOPROTEIN). III. Various ex- tended Germanic forms. 1. *blaikjan, to make white, in Old English blécan, to bleach: BLEACH. 2. *blaikaz, shining, white, in: a. Old Norse bleikr, shining, white: BLEAK}; b. Old English biéc, bright: BLEAK?. 3. Ger- manic *blikkatjan in Old High German blécchazzen, to flash, lighten (> German Blitz, lightning): BLITZKRIEG. 4. *blas-, shining, white, in: a. Old English blxse, torch, bright fire: BLAZE!; b. Middle Dutch bles, white spot: BLESBOK; C. Old French ble(s)mir, to make pale: BLEM- Ish. 5. *blend-, *bland-, to shine, dazzle, blind, confuse, in: a. Old English blind, blind: BLIND; (BLINDFOLD), (PURBLIND); b. Old High German blentan, to blind, deceive: BLENDE; Gc. Old English blandan, to mingle: BLEND; d. Old French blond; blond: BLOND. 6. *blenk-, *blank-, to shine, dazzle, blind, in: a. Old English blen- can, to deceive: BLENCH!; b. Old French blanc, white: BLANCH, BLANK, BLANKET; BLANCMANGE. 7. *blisk-, to shine, burn, in Old English blyscan, to glow red: BLUSH. IV. Extended form *bhleg-, to shine, flash, burn. 1. Ger- manic *blakaz, burned, in Old English blxc, black: BLACK. 2. Zero-grade form *bhig- in: a. Latin fulgére, to flash, shine: FULGENT, FULGURATE; EFFULGENT, FOU- DROYANT, REFULGENT; b. Latin fulmen (< “fulg-men), lightning, thunderbolt: FULMINATE. 3. a. Latin flagrdre, to blaze: FLAGRANT; CONFLAGRANT, CONFLAGRATION, DEFLAGRATE; b. Latin flamma (< *flag-ma), a flame: FLAMBE, FLAMBEAU, FLAMBOYANT, FLAME, FLAMINGO, FLAMMABLE; INFLAME. 4. Greek phiegein, to burn: PHLEGM, PHLEGMATIC, PHLEGETHON. 5. Greek phlox, a flame, also a wallflower: PHLOGISTON, PHLOX; PHLOGO- PITE. [Pok. 1. bhel- 118, bheleg- 124, bhleu-(k)- 159.] bhel-2. To blow, swell; with derivatives referring to various round objects and to the notion of tumescent masculinity. 1. Zero-grade form *bhl- in Germanic *bul- in: a. Old English bolla (> Middle English boll), pot, bowl: BOLL, BOWL!; b. Old Norse bolr, tree trunk: BOLE}; c. Old Norse bulki, cargo (< “rolled-up load”): BULK}; d. Old High German bolla, ball: ROCAMBOLE; e. Middle High German bole, beam, plank: (BOULEVARD), BUL- WARK; f. Middle Dutch bolle, round object: BOLL; g. Middle Dutch bille, buttock: BILTONG; h. Swedish *buller-, “round object,” in bullersten, “rounded stone,” boulder, akin to the Scandinavian source of English BOULDER; i. possibly obsolete Swedish bulde, a swelling (see wer-1). 2. Suffixed zero-grade form *bhl-n- in: a. Germanic *bulJ6n-, bull, in Old Norse boli, bull: BULL); b. Greek phallos, phallus: PHALLUS; ITHYPHALLIC.
329-bhel-*
330-3. O-grade form *bhol- in Germanic *ball- in: a. Old English beallucas, testicles: BOLLIX; b. Old Norse bdllr, ball: BALL; c. Danish bolle, round roll, akin to the probable Scandinavian source of BILBERRY; d. Middle High German baile (> Italian balla, palla), ball: BAL- LOON, BALLOT; PALL-MALL; e. French baile, ball: BAL- LOTTEMENT; f. Old French baie, rolled-up bundle: BALE!. 4. Suffixed o-grade form *bhol-to- possibly in Germanic *balthaz, bold, in: a. Old English bald, beald, bold: BOLD; b. Old High German bald, bold: BAWD. 5. Suffixed o-grade form *bhol-n- in Latin follis, bellows, inflated ball: FOLLICLE, FOOL!; (FOLLICULITIS). 6. Possibly Greek phalaina, whale: BALEEN. 7. Conceivably (but more likely unrelated) Greek phellos, cork, cork oak: PHEL- LEM; PHELLODERM, PHELLOGEN. (The following deriva- tives of this root are entered separately: bhel-?, bhelgh-, bhlei-, bhleu-.) [Pok. 3. bhel- 120.} bhel-3, To thrive, bloom. Possibly from bhel-?. I. Suffixed o-grade form *bhol-yo-, leaf. 1. Latin folium, leaf: ForL?, FOLIAGE, FOLIO, FOLIUM; CINQUEFOIL, DEFOLIATE, EX- FOLIATE, FEUILLETON, FOLICOLOUS, MILFOIL, PORTFO- LIO, TREFOIL. 2. Greek phullon, leaf: (-PHYLL), PHYLLO-, -PHYLLOUS; GILLYFLOWER, PODOPHYLLIN. II. Extended form *bhlé- (< *bhlea-). 1. O-grade form *bhl6- in: a. suffixed form *bhlé-w- in Germanic *bl6-w- in Old English bléwan, to flower: BLOWS; b. Germanic suffixed form *bl6-m6n- in (i) Old Norse blém, blémi, flower, blossom: BLOOM! (ii) Old English bléma, a hammered ingot of iron (semantic development obscure): BLOOM?; c. Germanic suffixed form *bl6-s- in Old English bléstm, bléstma, flower, blossom: BLOssoM; d. Latin flés (stem flor-), flower: FERRET?, (FLORA), FLORA, (FLORAL), FLOR- IATED, FLORID, FLORIN, FLORIST, -FLOROUS, FLOSCULUS, FLOUR, FLOURISH, FLOWER; CAULIFLOWER, DEFLOWER, EFFLORESCE, ENFLEURAGE, FLORIGEN. 2. Germanic suf- fixed form *blé-do- in Medieval Latin bladium, produce of the land: EMBLEMENTS. 3. Suffixed zero-grade form *bhib-to- in Germanic *bladaz in Old English bled, leaf, blade: BLADE. [Pok. 4. bhel- 122.] bhel-4. To cry out, yell. Germanic *bell- in: a. Old English bellan, to bellow, bark, roar: BELL?; b. Old English belle, a bell: BELL!; c, Old English belgan, bylgan, to become enraged: BELLOW; d. perhaps Old English bealcan, *b(iJelcan, to utter, belch forth: BELCH; e. Middle High German buldern, boldern, to make noise: POLTERGEIST; f. Icelandic baula, to low, akin to the Scandinavian source of Middle English baulen, to howl: BAWL. [Pok. 6. bhel- 123.] bheld-. To knock, strike. Zero-grade form *bhid- in Germanic *bult-, missile, in Old English bolt, heavy arrow, bolt: BouT!. [Pok. bheld- 124.] bhelg-. Also bhelk-. A plank, beam. 1. Germanic *balku- in Old English balc(a), ridge: BALK. 2. Germanic *balk6n- in: a. Old French bauch, beam: DEBAUCH; b. Old Italian balcone, scaffold: BALCONY. 3. Suffixed zero-grade form *bhik-yo- in Latin fulcire, to prop up, support: FULCRUM. 4. Possibly Greek phalanx, beam, finger bone, line of battle: PHALANGE, PHALANX. [Pok. 5. bhel- 123.] bhelgh-. To swell. Extension of bhel-2. 1. Germanic *balgiz in Old English bel(ijg, belig, purse, bellows: BELLOWS, BELLY. 2. Germanic *bulgjan in Old Norse bylgja, a wave: BILLOW. 3. Germanic *bolgstraz in Old English bolster, cushion: BOLSTER. 4. Celtic *bolg- in Latin bulga, leather sack: BUDGET, BULGE. [Pok. bhelgh- 125.) bhelu-. To harm. Germanic *balwaz in Old English bealo, b(e)alu, harm, ruin, bale: BALE?. [Pok. bheleu- 125.] bhendh-. To bind. 1. Germanic *bindan in Old English bindan, to bind: BIND; WOODBINE. 2. O-grade form *bhondh- in Germanic *band- in: a. Old English bend, band, ribbon, akin to the Germanic source of Old French bende, band: BEND?; b. Old English bendan, to bend: BEND!; c. Old Norse band, band, fetter: BAND!, BOND; d. Old French bande, bond, tie, link: BAND!. 3. Zero-
331-bherag-
332-grade form *bhndh- in Germanic *bund- in: a. Middle High German bunt, league: BUND?; b. Middle Dutch bondel, sheaf of papers, bundle: BUNDLE. 4. Suffixed form *bhendh-na-, “tied structure” (as of wicker), in Celtic *benna, manger, in Old English binn(e), manger: BIN. 5. Persian band, band, bandage, also a river levee: BUND!; CUMMERBUND. 6. Sanskrit badhndti (Sanskrit root bandh-), he ties: BANDANNA. [Pok. bhendh- 127.] bhengh-. Thick, fat. Extended zero-grade form *bhnghu- in Greek pakhus, thick, fat: PACHYDERM, PACHYSANDRA. [Pok. bhengh- 127.]
333-bher-1. To carry; also to bear children. 1. a. Germanic *beran in (i) Old English beran, to carry: BEAR! (ii) Old English forberan, to bear, endure (for-, for-; see per’): FORBEAR; b. Germanic *bérd in Old English bér, ber, bier: BIER; c. Germanic *bér- in Old Norse bdra, wave, billow: BORE’. 2. a. Germanic *barnam in Old English bearn, child: BAIRN; b. Germanic *barwdn- in Old Eng- lish bearwe, basket, wheelbarrow: BARROW!, 3. a. Ger- manic *burthinja in Old English byrthen, burden: BURDEN}; b. Germanic *burthiz in Old Norse burdhr, birth, akin to the source of BIRTH; C. Germanic *burja- perhaps in Old Norse byrr, favorable wind: BIRR}. 4. Compound root *bhrenk-, to bring (< *bher- + *enk-, to reach; see nek-2), in Germanic *brengan in Old English bringan, to bring: BRING. 5. Latin ferre, to carry: -FER, FERTILE; AFFERENT, CONFER, DEFER!, DEFER®, DIFFER, EFFERENT, INFER, OFFER, PREFER, PROFFER, REFER, SUFFER, TRANSFER, VOCIFERATE. 6. Latin pro- brum, a reproach (< “pro-bhr-o-, “something brought before one”; pro-, before; see per'): OPPROBRIUM. 7. Lengthened o-grade form *bhor- probably in Latin far, thief: FERRET!, FURTIVE, FURUNCLE; (FURUNCULOSIS). 8. Greek pherein, to carry: -PHORE, -PHORESIS, -PHO- ROUS; AMPHORA, ANAPHORA, DIAPHORESIS, EUPHORIA, METAPHOR, PERIPHERY, PHEROMONE, TELPHER, TOCOPH- EROL. 9. Greek pherné, dowry (“something brought by a bride”): PARAPHERNALIA. [Pok. 1. bher- 128.]
```


## [2026-09-05T05:23:51.257Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd1 aueg ===\" && grep -n -i 'vermehren, zunehmen' incoming/WLD/WLD_Bd1_pages.txt | head -20",
 "description": "Grep Walde-Pokorny Bd1"
}
```


### [2026-09-05T05:23:51.323Z] TOOL RESULT

```
=== WLD Bd1 aueg ===
```


## [2026-09-05T05:24:02.463Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'aojastara\\|aoj\\.tara\\|pairi\\.aoj\\|pairi-aoj\\|aojaŋh\\|aojah' BRT.txt | head -40",
 "description": "Grep Bartholomae for pairi.aojah"
}
```


### [2026-09-05T05:24:02.584Z] TOOL RESULT

```
2902:•  j.,  g.  "aojah-  Adj.  'stark,  kräftig':  mi- "inm  . .  "JaaAfin  laxmim  ra'ialäqm  Yt.
2905:•  j.,  g.  aojah'vant-  Adj.  (fem.  °vaiti-) 'kraftvoll, kräfÜg,stark':  xia'inm  'jör^hval Y._JJ.4;  zit,  V.  20.  8,  wo  -jaahvat;  — rafonö  ,.  'jötighvat  Y.4J.8;  28.6;  — sonst  von  Gottheiten:  at  iöi  •i/rim  . . 'jimhvantim  asl .,  ". .  Feuer  {Älar),  das seine  Kraft  durch  A.  hat"  Y.J4.4";  — sraohm  . .  *°janhuntfm  '>  Y.  57. 1 1 ;  — fravalayö  ..  'jattukaitil  Ytij.32;  — astval  (sd)  <ß>m  hyut  ustän��  'jönghval Y.4!j.i6.
3778:•  j.  aiivi.aojah-  Adj.  'die  Übermacht  ge- winnend über—,  bemeisterad',  mit  Akk.:  a
6158:•  j.  a&aojastara-  Adj.  (rem.  'rä-)  'der noch  viel  stäikere' :  aZsa  druxs. .  -ra  (NSf.) varToayde  V.p.48.
6356:•  j.  a^aojah-  Adj.  'der  seine  Kraft durch  A/a  hat''':  %waAy3  ganmä  (sd.) ähr5  'jaahs  Y.4J.  4''.
21122:1  c(jAw.).  r)  Vor^°  steht  ein  Komparativ  ar^dvJm  ..yä  asti  avavaiti  masSy  visp.'i (oder  ein  komparativähnliches  Adjektiv),  ..  äpö  Y.6^.  $;  —  nil?iiiacit . .  sturqm {^) allein  oder  mit  iz^mil/(Sp.  397  u.);  zu  i):  y'  nars  .  .  ra-ftiamm  T.4.3L.  a)  insbe- aojastara  lanoayeie y  ('als')  para  ahmät  sondere  auf  eine  Frage  mit  h-ant-  ant- as  Y.g.  48;  —  yimä  .  .  zqm  vilävayat .  .  wortend;  cvat  haca  paourvaabyal  y  'iri- ahtnai  masyehlm  y  para  akmät  V.  2.  11;  gaim  V.p.  9;  8",  10;  —  ä'atyaval  ^ntat»mt
22889:—  yaiibyS  xsahnmcl  *ayiBjivamn>m  (sd.) vandaiti  armaitifY.  2&  3;  —  auch  Med.: yf  nä  aMi  aojaftka  vandayattä  yqm  . . gaiüqm  . .  baxsain  (sd.)  "dem,  der  durch die  Kraft  der  A.  gross  machen  wird  das . ." V.  ^0. 3.  a)  Med.  und  Pass.  'wachsen,  ge- deihen': var^ayaiauha  mana  vaca  vTspss^a paiti  varsa/r^  Y.  io.  j;  —  sfaipaike  nS daiühu!  fralataila  vartbataiia  (3SKPM.) Yt  13. 68;  —  yö  daitihave  hu.vaxsJi  fra- t^mnahe  7!ar>\>mnahe  ..  V..^.  zGl.;  — aila  äruxiya  nasus  as.aojastara  vanlayde yaäia  para  ahmät  as  V.  g.  48.  a)  PPfP. 'gross,  gewaltig";  kihrpasca  .  .  srTrä  .  . v)r»zää  am>ianqm  spmtanqm  Yt.y.81;
28091:(näml.  asp>m)  'vart  nötf  jaityehi  (sd.)  Y. II.  2;  —  haamS  aiibis  ysi  ,  .  hita  toxstnli (sd.)  .  .  'var>  aojBsca  baxiaiti  Y.g.  22. Vgl.  tavoA:  —  np,  vgl.  zör  (woiu  Hbm.  PSt. 273)-  —  P5-:  SÄ-«.  Sü.  :fräimii\  mit  der  Erl.: iti  pädayofi.  —  <)  Das  erste  a  nach  %  2g4.  3. —  1)  Die  selbe  Verbindung  auch  im  Mp., iB.  Bd.  7.  g;  ei  u  tlr.  —  3)  Vgl.  Sü.  und unter  aojah-.  —  *)  Wofür  auch  fälschlich z  n  a  r  (sÄÄr),  ebenso  wie  umgekehrt  i  n  r  (zSr) für  iohSjö-  vorkommt;  s.  DsT,  ZA.  /.  Lxxvi No.  3.     Vgl.  No.  5-    ~    5)  Wie  für  taArS-,
```


## [2026-09-05T05:24:04.489Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB p45 (leaf 55) ===\" && awk 'BEGIN{RS=\"\\f\"} NR>=54 && NR<=57 {print \"--- awk leaf \"NR\" ---\"; print}' HUB.txt | head -120",
 "description": "Print Hübschmann p.45 area"
}
```


### [2026-09-05T05:24:06.503Z] TOOL RESULT

```
=== HUB p45 (leaf 55) ===
--- awk leaf 54 ---
— 43 -
327. Np. panah 'Zuflucht, Hulfe' = paz. panah Min.
Gl. 154, Shk. 262, phi. panah Phi. Min. p. 15, 10,
afgh. LW. panah gehort ohne Zweifel nicht zur Wrzl.
pa *schiitzen'. ^) Ich mochte pa-nah teilen und nah =■
ap. *na&a' = skr. nathd- 'Zuflucht, Hiilfe' setzen. Ob
panah aus *patnah {tn zu nn = w?) entstanden sein
kann, bleibt zu untersuchen.
330. Der Bedeutung wegen nicht ganz sicher.
Hinter Nr. 333 ware nach Fr. Muller, WZKM. 6, 185 an-
zufiihren: pot a, pota scrotum' = lit. pautas^ das aber
zunachst *Ei* bedeutet (Fick, Wb.^ I, p. 84), was
von dem (unbelegten) pota nicht feststeht. Man sollte
zudem *poda erwarten. 1st das Wort iiberhaupt
persisch ?
336. 1st wegen der Bedeutung nicht sicher.
337. Np. puSa *crus sive hominis sive animalis (unbelegt)
kann, wenn aus podak entstanden, zu np. poyidan
laufen' gehoren. Vgl. nhd. Lauf , Lauft in waid-
mannischem Sinne. Zusammenhang niit pai iindet
nicht statt, vgl. Horn's Bemerkungen zu Nr. 282.
338. Zd. pqstO' in pqstdfra&ah- ist noch ganz unklar, aber
die Pehleviiibersetzung giebt es durch post wieder.
339. Der Etymologie wegen ist np. puk nicht zu verdach-
tigen. Vgl. afgh. pu, puk a puflf, a blast, the act of
blowing', pukai a puflf, inflating', pug 'the act of blowing,
a puflf*, pukql *to blow, to inflate, to breathe upon'. -
Lies (fvaaa.
340. Die beste Lesart im Armenischen ist polovat. Dies
sowie np. ptildd setzen ein phi. *pdlavat oder *pOlavat
(anstatt polofat oder polapat) voraus.
*) Vgl. auoh die Name n PanahmOy, Jazdpanah bei Hoffmann^
Ausziige p. 70 und 87. Aus dem von Fr. Muller mit Unrecht heran-
gezogenen phi. panak (= arm. -panak^ pStz. pana Shk. 262) konnte im
Neup. nur ^pana werden.
--- awk leaf 55 ---
— 44 —
341. Np. pahra = pas Nr. 274. Bal. pahar =^ afgh.
pahar, pahar 'Abschnitt von drei Stunden' aus dem
Sindhi.
342. Np. pahlu 'Seite' hat mit zd. pere&U" *breit*, skr.
prthivi nichts zu thun, sondern geht auf ein ap. *par&U'
aus iran. ^parsu- (skr. pargu- 'Rippe', zd. peresu-,
ZPGl. 10: paresU' -= phi. pahluk Rippe etc.) zuriick.
Die Dialektformen mit hi, I fiir rs (wie g. pahli 'Rippen'
ZDM6. 36, 37 etc.) sind aus dem Persischen ent-
lehnt.
343. Hier fehlen die n5tigsten Eriauterungen zu pahlav
(urspr. = Tarthien') und die Litteraturangaben. Ich
komme anderswo darauf zuriick.
345. Ap. patiy als 1. Glied von Comp. ist neup. zu paS
(vor Vocalen), pa (vor c, s, 5), pai (vor den ubrigen
Consopanten) geworden, ap. *patiy' zu pad-, pa-,
tJber das selbstandige patiy vgl. Nr. 144.
346. Fiige hinzu 2) pai *Sehne* = afgh. pala *Sehne*
(Geiger, Etym. und Lautl. des Afgh. Nr. 158) aus
iran. *padd,
347 ^*^ Anm. Vgl. sTvend pTdm 'marjolaine' = np. pudana
(Journ. asiat. 1893, 258).
349. Bei der Erklarung von paidd 'sichtbar, oflfenbar, klar
kommt alles darauf an, ob es zu dem phi. patyak der
Hajlabad-Inschrift gehSrt oder nicht. Im ersten Falle
ware patyak durch Epenthese zu phi. paitak = u^.paida
geworden wie aryan zu Sran. Aber die Bedeutung des
Wortes patyak der noch sehr dunkeln Inschrift steht
bis jetzt keineswegs fest, auch kommt Epenthese sonst
nur bei r und n sicher vor. Im andern Falle ist
Darmesteter's Erklarung (Etud. iran. I, p. 69) zu
erwagen : paida = phi. paitak = padtak (beides kann
gelesen werden) aus *patdak = alterem *patdayak
oder *patdayak --- ap. ^patidaya- oder "^patidaya- sicht-
bar, vgl. zd. paiti-dl 'hinsehen*, paitidaya- *Aufseher,
paitidlti' *Hinsehen, Blick'. Vgl. phi. padtan (oder
--- awk leaf 56 ---
- 45 —
paitan) Phi. Vd. 172, Z. 4 fiir "^padtan = zd. paitidana-
*T«nica* vd. 14, 9 (Sp. 39); phi. iJHam oder pagtam
(beide Lesungen m5glich) fiir *patgam = np. paiyam,
arm. patgam, zd. ^paitigama^,
350. Vgl. oben Nr. 286.
351. Np. pirdr *das vorvergangene Jahr = ap. p{a)ruviya-
+ yflra- *das alte Jahr ? Ap. yara- in dusiyara-,
353. Fr. Muller, WZKM. 8, 93 verdachtigt phi. patrahan
'Rock' als kiinstliche Form, halt sich an phi. perahan
PP61. 11, 7 und setzt dies = zd. ^pairy&rihana- (vgl.
aiwydflhana- *Giirter), das formell gut stimnien wiirde.
Doch ist diese Erklarung aufzugeben, wenn phi. pa^
trahan (aus *patrahan) echt ist. Von Wichtigkeit ist
auch die moderne Aussprache: np. pirahdn *Hemd,
KitteF (Rosen, Np. Sprachfiihrer p. 49), pwahan,
plrahan *Hemd' (Sal. Shuk. p. 20, Glossarium p. 76)
weist auf phi. pBrahan = ^pairydnhana-; np. pairdhan
(wie die Afghanen sprechen) auf phi. patrahan.
354. Np. peroz Victor, felix, faustus' kann nicht = zd.
*paiti-raodah- gesetzt werden, da schon das Pehlevi
durchweg pSrdd (nicht patroi), resp. p^Gz hat in tJber-
einstimmung mit arm. PeroZj syr. PBrDz, gr. IlegcoCrjg
(NOldeke, Tab. 117), lat. piroses (Ammian).
356. Np. pes Vor' = paz. phi. pSs (61. and Ind. 113—114)
^= bal. pSs = arm. pBS- (in Lehnwortern) ist jeden-
falls nicht = ap. pati§, Dass auch kein Grund vor-
handen ist, np. piS- auf ap. patis zuriickzufuhren, ist
oben Nr. 312—314 gezeigt. Nach np. paskam = arm.
patskamh = zd. ^paiti'skemba- (oben Nr. 314) soUte
man np. pas- fiir ap. patis- (in Comp.) erwarten. —
Np. pi^x^ar hat seiner Bedeutung nach nichts mit
dem angefiihrten phi. pati§x^ar zu thun.
359. Np. paig Tussganger = syr. N3^£> Noldeke,
Alexanderroman p. 14, arab. /ai/, phi. paik West,
Pahl. Texts II, 280, plur. paikan Yatk. i. Zar. p. 50,
*) *A long robe, a shirt or shift*.
--- awk leaf 57 ---
— 46 —
Anm. 14, arm. LW. payilc, skr. padika- Tussganger ,
prakr. paikka-. Fiir das Altpersische ist mit Horn
^padika- anzusetzen.
360. Phi. patMrUan „K5cher" ? Soil heissen *kampfen'.
365. Wenn Horn paz. pey (lies ply oder pig) = phi. pig
Oder pik (Shk. 263) = bal. pig^ nb. ply mit Recht auf
```


## [2026-09-05T05:24:21.537Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'pairi\\.aoj\\|pairi\\.aog\\|pairyaoj\\|pairi-aog\\|pairi\\.a[oö]' BRT.txt | head -30; echo \"--- search col 862 markers ---\"; grep -n '^ *86[0-9] *$\\|86[0-3]$' BRT.txt | sed -n 1,40p",
 "description": "Locate Bartholomae column 862"
}
```


### [2026-09-05T05:24:23.076Z] TOOL RESULT

```
3213:mit  pairi  'aufsagen,  hersagen'  (die  Gä- 'kä%):  *yöi  glü^i  ..srävayanti yezi  arastnm (sd.)  pairi.aoxta  pairi.äaa  vä  . .  pasla  vä parö  Vä  pairi.äm  aratufryö  ".  .  wenn einer  .  .  (die  GiJääworte)  zu  spät  oder  zu früh  aufsagt,  die  sind  ar."  N._J2.
5336:srSvayanti  yat  "rym  ^pairi.aoxta pairiMa  va  ", .  wenn  einer  sie  beim  Vor- trag stockend  aufsagt"  N.j3.
15551:I):  fei,  (lu  II):  api  hac,  (lu  III):  apc;  s.  noch No.  2  ff.,  6,  8  ff.  —  0  Hds.  pari.  —  »)  D.  i. TOT  oder  nach  der  Rezitation  der  Gs%ä%\  Pü.: pas  -  tu  fralum    kär   ape   kuntt  pas   apasläk gffujet-aiävp/i—ku  afaitik  (Rest  weggelassen). —  3)  Pü.:  ausgelassen.  —  4)  Unsicher.     Pü.: apar.     -    S>  Vgl.  Bipi  II  I   i  (Sp.  83  ">■)■  - 6)    PD.  :    apar  pa  barsm.    —     ?)   S.  dam  Dbr, VglS.  /.   71 1.  —  »'  PS-:  i'  onrfflr  an  apar.  — 9)  Pü. !  *ia/.  —  10)  Pü. :  undeutlich.  —  "»  Pii, : apF,  —  ")  Wörtlich :  "non  profuse  sine  semine', eine  Vermischung  der  beiden  sinngemäss  rich- tigen  Ausdrücke   */rai>har>iäl  pairi  xl'    und tt/raa/iamäl  paiti  xs',    vgl.  anädntxlay-  No. I.     Pü.:    fehlt.    —     '.0  Pü.:    hat.  —   M)  Wo NA.  unrichtig  abteilt ;    s.  Vt,  3,  la  —  >5)  Wo die  Hds.  das  2.  Mal/aiV/  bieten;  s.  Yt.  j.  14. •  j.   *pairi.aoxtay- ",    pairyaoxtay-    f. i)    'Aussprache,    Vortrag':  yezi  araitrim (sd.)  *'ta'^  pairi Jta  Ü.32.         2)  'Zuruf, Befehl':    dansa    nä    'tala    (LS.  als  IS.) uzustanä    *adir»yäte  .  .  frasumaitls  (sd.)
15552:•  j.  *pairi.aoJas'tara- ''  Adj.  'der  sieg- reichere': °rö  zT  ahmät  V.4.  10  FüZ.
--- search col 862 markers ---
15490:859  paro.astay-  —  pairi  U  i  a  860
15547:862
15585:865
15588:866
15625:867
15628:868
15674:869
```


## [2026-09-05T05:24:28.824Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15540,15570p' BRT.txt",
 "description": "Read Bartholomae around col 862"
}
```


### [2026-09-05T05:24:28.903Z] TOOL RESULT

```
täis  . .  syaohanUii . .  yaisU  as  'rl^^  pouruiyS i^ye/j  (sd.)  Y.34-  8;  ~'  »öit  inhjyöi frajylitis  (sd.)  .  ,  dngvasü  -ri  "ne  (fiat) recte  vtventi  pernicies  . .  apud  infideles (sva.  ab  infidehbus)"  Y.  2p.  5,  3)  mit
Abi. 'von  —  her,  von  — weg";  i)  räumlich; a)  'von  —  her':  y£ia  vätJ  .  .  %wäs>m (sd.)  da/in3t(Sp.jo$  u.)  -ri^^/ram^rPZffii'V. _j.42.  b)'(von-wegsva.)abseitsvon— ': panta  vTcinasta  (Sp.  441  m.)  'ri  urvarä- byasca  vam^lbyasca  V.16.  2.  2)  unräum- lich; a)  beim  V.  urvals-  mit  /rü  'sich abwenden  von  —  (weg)':  yat /raotrisaiti 'ri  dusmatalibyasca  .."  H.  z.  17.  b)beira V.  *ah~  mit  aiwi  'discere  ab  — ,  studiren bei  — ':  kal  *nil  dafvayasnat  .  .  agira.- pataiHsä.)  'ri^^  ^aiwyavhai  (Sp.  278  o.) N.  16.  c)  bei  den  Wörtern  für  schützen
'vor—',  neben  parö:  aoa  ..  nS  ..  ntpaya .  .  'ri  dniatat  mahrkai  'ri^  . .  aistnake pars  draomSbyS  Y.  57.  25;  JÄ'.  2  ">,  SrB.j; —  th  (Täxüi.frtrvasay^)  .  .paritasca  pairi- värascä  vUfnte  'ri  mainyaoyät  drujat  Yt. ^J-7ij  71;  —  ya'ka  ..  dadränS  m  'ri iri>yqstätal(sd.)  Aaraite  Y.ip.io.  d)  wie lat  ab  zur  Bezeichnung  des  Anlasses, neben  parff:  viian.qzahyehei^A^ca  paiti  . . 'ri"^  *halnyäsca  vöiynäuyU  aurva- byasla  parö  Y.6S.i$.  e)  'ohne' aufTalliger  Verwendung:  yim  antan  äkitim ramm  frajasäi  (Sp.  goo  o.)  afranhansäl (Sp.ioi  o.)  'ri  xi'udrätV.i6.i6"\  4)  mit Instr.;  i)  'ex  — ',  beim  V.  'zan-  mit  /r 'cognoscere':  yS  aSa  (Sp.  11  u.)  -n'' ariira  frasänaiti    F.5.  2)  pairi  SiS
sbes.  ni)    Praev.    (mit    ''kar-,    ^kars-,
gam-,  da-,  hiar-^  st3-  usw.).
Wertlos:   y5  janat  ..  dalnanqm tiräi  hazoDTü  'ri  baSfaräi  baa-anö
pairi  BIS
862
^.13'+',  10'».        [Yt.iO.ios:  lies  ^aiW.-
apaya;  —  V.  25.  45:  lies  pairiMcahi^ KompA.;    AbleiC   —   VgL /üiW.    —    ai. /Jri Adv.  (usw.),  mp.,  np./flr*  (GlrPh. /.310,  i  b. '59);    S.    noch    zu     *fairi.aoJastara-.    —    Vgl.
zBed.  und  deren  Entwicklung  Heu.  ZC  319, DBB.  VglS.  I.  702,  Cld.  KZ.  31.  262.  Pü.  (la
I):  fei,  (lu  II):  api  hac,  (lu  III):  apc;  s.  noch No.  2  ff.,  6,  8  ff.  —  0  Hds.  pari.  —  »)  D.  i. TOT  oder  nach  der  Rezitation  der  Gs%ä%\  Pü.: pas  -  tu  fralum    kär   ape   kuntt  pas   apasläk gffujet-aiävp/i—ku  afaitik  (Rest  weggelassen). —  3)  Pü.:  ausgelassen.  —  4)  Unsicher.     Pü.: apar.     -    S>  Vgl.  Bipi  II  I   i  (Sp.  83  ">■)■  - 6)    PD.  :    apar  pa  barsm.    —     ?)   S.  dam  Dbr, VglS.  /.   71 1.  —  »'  PS-:  i'  onrfflr  an  apar.  — 9)  Pü. !  *ia/.  —  10)  Pü. :  undeutlich.  —  "»  Pii, : apF,  —  ")  Wörtlich :  "non  profuse  sine  semine', eine  Vermischung  der  beiden  sinngemäss  rich- tigen  Ausdrücke   */rai>har>iäl  pairi  xl'    und tt/raa/iamäl  paiti  xs',    vgl.  anädntxlay-  No. I.     Pü.:    fehlt.    —     '.0  Pü.:    hat.  —   M)  Wo NA.  unrichtig  abteilt ;    s.  Vt,  3,  la  —  >5)  Wo die  Hds.  das  2.  Mal/aiV/  bieten;  s.  Yt.  j.  14. •  j.   *pairi.aoxtay- ",    pairyaoxtay-    f. i)    'Aussprache,    Vortrag':  yezi  araitrim (sd.)  *'ta'^  pairi Jta  Ü.32.         2)  'Zuruf, Befehl':    dansa    nä    'tala    (LS.  als  IS.) uzustanä    *adir»yäte  .  .  frasumaitls  (sd.)
•  j.  *pairi.aoJas'tara- ''  Adj.  'der  sieg- reichere': °rö  zT  ahmät  V.4.  10  FüZ.
Kompar.  aus  •■/"*-  Adj.  'der  die  Übermacht hat';  vgl.  ahei-aBJah:  —  np.  t^.  perSs  'sieg- reich' (aus  ir.  'pariaiij',  s.  Aaza  IFAnz.  lO. 28;  falsch  WZKM^  p.  290).  —  zBild.  des Kompar.  %.  ai.  ojastara-,  als  Erklärung  von ijiyas:  —  i)  Die  Ausg.  trennen. j.  pmri.axla  N.  32:  lies  paiti.aoxla.
•  j.  *pairi.apa-"  f  '(ringsum  gehendes Erreichen  sva.)  Umfassen':  yalcit  vlmai- oim  (sd.)  aiähil  z^mS  t^mcit  mi'irö  han- gD/ümnü  'paya  (IS.) ')  bäztfwe  "auch  wenn er  . .,  auch  den  erhascht  M.,  mit  den Armen  ihn  umfassend"  YLro.  105.
')  NA.  trennt
•  j.  pairi.aDhar§ta-  Adj.  (fem.  'ta-\ PPfP.:  s.  hanz-.
KompE.
•  g.  pairi  äiä  adv.-artige  Verb,  'antchac, zuvor,  früher',  attributiv  gebraucht":  a^ yH  vaniä  yäca  p'  J//  lyao^ana  .  .  "die Taten,  die  ich  wirken  werde,  und  die früheren  . ,"  Y.50. 10".
Pü.:  /vi  i  ösän.  —  ')  Anders  Jn.  A  hymn  22. —  ä)  S.  zSt.  Clo,  KZ.  jy.  262,
dby  Google
863  pairiuxSatay-  —  *pairLg^vatah-  864
•    j.  pairiuxsatay-    f.     —i—:yS  gä%ä    Die  ^.  «rhaden  besonders  dadiuch,  dass  sie  die 'iaiü  (IS.)"  *sr3vayanti  N  ?2^  Maidayasncz  durch  liebcskäiute  vom  Glaaben
Pa-t  dlän  klg^in  if^fao^  «»d>r  ^J.  !^^/"«E  uiMhen;  s.  PüErL  zn  YL  ^.  lO  (jWrö y«^;  mit  n^de».Iichi^  Erl.  -  0  T  •«*«- 1 "'"  *'^  ^  i'"!^*  J'^"'^^  '^",  *'^' "'«) ^«/,.  -  •)  Es  «hrint  sich  lun  dDc  beson-  '""*J","?^*^-=  *1?«:  °'^-.339-  VgL  noch  "). dere  Art  des  Vortr.g.  der  Cä^Js  m  handeln  .  7.  ',^.^"""  *^'"  ^^  ^"^  "'"°"  8*™«""; oder   tuD    diieii  Vortrag  bei  besonderer  Ge-
KompE.;  Ableit  —  El.?»)  —  ttp.  pari.  — V^:  parii.  Sä.:  räifasl,  (TaeisX)  mahäräifaii; %.  noch  *)  und  Mo.  i.  —  ')  Darauf  geht  die NpüErL  tn  Yt  /.  10:  pari  an  bäiaj  ia  ..  bar ätiHäH  n  ta  tanün  Ingardad,  in  Sü.:  maiäräi- foji  , .  iiSit  patälädifH  bkramiUt.  —  ')  Die Kildänng  BB.  15.  S  wird  durch  mp.  parii, np./ari  nnwahrtcbeinlich,  die  auf  ir.  *parUä-
legenheit.  1
•  j.  yl>  vanAaiii  vanmäs^a  "pairiurus- 1 viätis  N.pz.
Ob  yXLpairiMrtiislüi  S.  vL^rvistay-.  —  Pn. :  öiäit ki  nümmiäid  *iiihtmtVt  i  hrtäi  pizmnknl?)
•  j.  pairika'vant-  Adj.  'der  von  P.  um- '     hlnweiien. geben  ist,  es  mit  P.  hält*:  yatulca  yiitu-\ maiqm  pairikäsca  •vatam  YL/1.6.  ]•}■  ma  Af  iar^ma  pairUt^nttm />airi.-
Pil:  patU  mar/  k  iw;  TgL  tu  yötumaiii:       ,  k^nntli    narS    oahtH     alavanS    V.    t^.
•  j.  pairLkara-  m.  'Umfiirchiuig,  rings henmigehender  Furchstrich ,  -streifen': xia^räi  vairysi  'nm  fairiJiärayöis  (Sp. 449  n»)  V.  17.  6.  |
```


## [2026-09-05T05:24:39.240Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'peroz\\|pgroz\\|pSroz\\|përoz\\|piroses' HRN.txt | head -20",
 "description": "Grep Horn for peroz"
}
```


### [2026-09-05T05:24:39.300Z] TOOL RESULT

```
3331:Vergl. lat. piroses, quod bellorum victor interpretatur
```


## [2026-09-05T05:24:39.502Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==100 {print}' HRN.txt | head -60",
 "description": "Print Horn p.78 leaf"
}
```


### [2026-09-05T05:24:41.070Z] TOOL RESULT

```
- 78 -
LW. kurd. peyamher; af;'. paiyämhar\ oss. t.
pa/umpar, d, pexompar; hei, paiyam^ paiyambar (207).
Ich möchte phlv. petäm für eine Verschreibung aus
patgätn ansehen.
349. peiää^ offenbar, jüd.-pers. NT^5.
^)x\\. patyäk (Inschr.) ') *oifenbar, petak, ])etäkJhj
petäktmtan ; aus ap. "^palyaka- zu ai. pratydüö-, *pra-
tyäka- (Bartholomae, Litbl. f. or. Ph. I, 16 Note 3;
doch vergl. Joh. Schmidt, Pluralbildungen 390).
LW. kurd. peidä; sdy, paidä; bei. peda^ P^dag^
n. peöäy (205).
350. plr alt, Greis', pTre,
phlv. plr, pin^ pTrak altes Weib' (PPGL).
kurd. afy. LW. pTr; hei, ptrük, n. plrük 'Grossvater'
(300).
Vergl. aw. parö^ "^parya- 'früherer 2).
351. pfrär, pirar[sal *das vor vergangene Jahr.
aw. '^para,yär' (+ säl),
352. pmrästen schmücken, anordnen , Praes. peiray-em.
pati+ [/'räd- (s. ärästm No. 11); phlv. peray(i)sn;
arm. LW. patrast,
353. perähen 'Hemd*.
phlv. patrahan *ßock' (Yätkär-T Zarir. 64 Note 53),
perähen (PPGL).
kurd. LW. pirun, perlen 'Hemd'; wa/. parhän, sar.
harhän 'Weiberhemd'.
354. perö^, arab. LW. ß:rüz 'siegreich' ; j^frö^e 'Türkis,
arab. LW. flröze, fairüzaj,
aw. "^paiti.raocah-; iphlv, peröd, peröÖkar, päz. |?eröi.
Vergl. lat. piroses, quod bellorum victor interpretatur
(Ammian. Marc. XIX, 2, 11), arm. Peroz, gr. üfiQwiTjg
*) Vergl, Hang, Essay on Pahlavi, 61 (PPÖL).
Pehlv. patyWc deckt sich mit gr. nqoaian-ov.
2) Vergl. No. 286 Anmerkung. Als ich dort Bartholomae's
Etymologie während der Correctur einfügte, hatte ich vergessen, dass
ich selbst später die gleiche Erklärung brächte. Inzwischen ist der
vierte Bogen gedruckt worden.
```


## [2026-09-05T05:24:52.410Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN leaf for p.876 (leaf=p+24 -> 900) ===\" && awk 'BEGIN{RS=\"\\f\"} NR>=899 && NR<=902 {print \"--- awk \"NR\" ---\"; print}' SYN.txt | grep -n -i -m40 'grow\\|876\\|877\\|augeo\\|vaxš\\|uxs' | head -40",
 "description": "Find Buck p.876"
}
```


## [2026-09-05T05:24:53.950Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"xwš'y\\|xwšʼy\\|xwš\\`y\\|ʼxwšʼy\\|xws'y\" SOD_pages.txt | head -20; echo \"--- alt ---\"; grep -n 'to grow' SOD_pages.txt | head -20",
 "description": "Grep Gharib Sogdian dictionary"
}
```


### [2026-09-05T05:24:54.056Z] TOOL RESULT

```
=== SYN leaf for p.876 (leaf=p+24 -> 900) ===
```


### [2026-09-05T05:24:55.623Z] TOOL RESULT

```
--- alt ---
```


## [2026-09-05T05:24:58.930Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && wc -l SYN.txt && awk 'BEGIN{RS=\"\\f\"} END{print \"leaves:\",NR}' SYN.txt && grep -n '12\\.5[0-9]\\|GROW' SYN.txt | head -20",
 "description": "Inspect SYN.txt"
}
```


## [2026-09-05T05:24:59.826Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && wc -l SOD_pages.txt SOD.txt && head -30 SOD_pages.txt && grep -n 'xwš' SOD_pages.txt | head -20",
 "description": "Inspect SOD files"
}
```


### [2026-09-05T05:25:00.416Z] TOOL RESULT

```
35875 SYN.txt
leaves: 1545
1035:3. Gall. -magus in Arganto-magus, etc., Ir. mag, NIr. magh, W. maes, Br. maez, prob. as orig. ‘expanse’ : Lat. magnus, Skt. mah-, etc. ‘large, great’ (12.55), Skt. mahi- ‘earth’. Pedersen 1.96. Stokes 198f. Walde-P. 2.258 (ad- versely).
5653:Rum. obraz, fr. Slavic, ChSl. obrazit ‘form, shape, image’ (12.57), SCr. obraz ‘cheek’, ete. Tiktin 1072 f.
7273:Fr. grosse, lit. ‘big’ (12.55).
9488:Lett. auglis, fr. Lett. augt, Lith. augti ‘grow’ (12.53). Mithl.-Endz. 1.216.
10449:4. Dan. kjole, shortened form of kjortel = ON kyrtill ‘kirtle, tunic’, fr. ON *kortr, Dan. kort ‘short’ (12.59). Falk-Torp 518.
10533:ON skyrta, Dan. skjorte, Sw. skjorta, OE scyrte (gl. praetexta, where perh. the Lat. word was misunderstood), ME sherte, NE shirt, derivs. of adj. for ‘short’, OE sceort, etc. (12.59). Falk- Torp 1007. NED s.v. shirt, sb.
12896:ON avozir, OF westm, OHG wahsmo, all orig. ‘growth’, fr. ON vara, OF weazan, OHG wahsan ‘grow’ (12.53).
12898:Dan. gréde, Sw. gréda: Dan., Sw. gro, OE growan ‘grow’, ete. (12.53). Falk-Torp 356. Hellquist 307.
12914:Lett. auglis, in general ‘fruit, growth’, fr. Lett. augt ‘grow’ (12.53).
13132:; Sereral of the words are from the no- i ot grow’, as, conversely, some of ned . for 'grow’ were primarily ap- et - ay Ce 12.58). Some show nection ith wr cutting, shoot’ or con-
13443:Pol. winorosl (according to informant the best current word; many others in dicts.), epd. with ros! old word for ‘growth’ : résé, ChSI. rasti, ete. ‘prow’ (12.53).
14067:NIv. gearraim, fr. MIr. gerraim ‘cut off, shorten’, fr. gerr ‘short’ (12.59).
15570:Derivs. of Lat. formdare ‘shape, form’ (fr. forma ‘shape, form’, 12.51), or new verbs formed fr. the noun, occurring in most of the modern European languages, may be used to cover the notion of mold- ing clay, and in many languages are the most usual expressions for this. Cf. Fr. former (OF r. fourmer > ME fourme, NE form), Sp. formar, Rum. forma, NIr. foirmighim, W. ffurfio, Dan. forme, Sw. forma, Du. vormen, MHG, NHG formen, also, although prob. less common, Lith. formuoti, Lett. formét, Boh. formovati, Pol. formowaé, Russ. formovat’.
15582:ON mynda ‘shape, form’, deriv. of mynd ‘shape, form, image’ (12.51).
15584:OE (ge)htwian ‘form, fashion, shape’ (‘fingere’ Aelfric), deriv. of OF hiw ‘shape, form, appearance, color’ (12.51).
15596:8. Skt. ma- ‘measure, mete out’, hence also ‘prepare, arrange, fashion, form’ (cf. nir-mda- ‘construct, build’, 9.44), Av. md- ‘measure, make, form’ (12.54).
15837:7. Skt. pratimd- ‘image, picture, stat- ue’ : prati-md- ‘imitate, copy’, cpd. of prait ‘over against’ and ma- ‘measure’ (12.54) ‘mete out, fashion, build’, ete,
16543:mode), earliest sense ‘measure’, fr. the root of Lat. medéri ‘care for, heal’, meditart ‘think about’, Grk. pédouar ‘be mindful of’, Goth. mitan ‘measure’, etc. Walde-P. 2.259f. Ernout-M. 599, 622 ff. Walde-H. 2.56. It. maniera, Fr. maniére, Sp. manera, fr. form of Lat. manudrius ‘belonging to the hand’, deriv. of manus ‘hand’. Se- mantic development through ‘(way of) handling’. REW 5832. Gamillscheg 586. Fr. facon, fr. Lat. factid ‘party, class’ (also rarely ‘conduct’) fr. facere ‘do, make’. REW 3133. Gamillscheg 401. Sp. forma ‘form’ (12.51), also ‘man- ner’. Rum. chip, in earliest use ‘statue, por- trait’, hence ‘form, appearance’ and finally ‘kind’ and ‘manner’, through Slavie (SCr. kip), fr. Hung. kep ‘statue, portrait, form’. Tiktin 343 f. Berneker 504. Rum. fel (‘kind, sort’, and ‘manner’); fr. Hung. fel in phrases like minden féle ‘all kinds of’. Tiktin 614 f. 3. Ir. mod, NIr. modh, W. modd, fr. Lat. modus (above, 2). Vendryes, De hib. voc. 157. Loth, Mots lat. 188.
17272:wan), Du. waaien, OHG wajan, MHG wajen, NHG wehen; ChSl. véjati (in Gospels viiz-véjati Mt. 7.25, 27 for mvéw, beside more common duchati Lk. 12.55, etc.), Boh. vdit, Pol. wiaé, Russ. vejat’.
18925:W. dal, dala, Br. dere’hel (for *delc’hel, ef. pple. dale’het) : Goth. tulgus ‘firm’, OS tulgo ‘very’, Grk. Godtxés, Skt. dirgha-, etc. ‘long’ (12.57). (Cf. NHG gelangen ‘reach, attain’ : lang ‘long’, and NE long for.) Walde-P. 1.818. Peder- sen 1.106.
```


### [2026-09-05T05:25:00.486Z] TOOL RESULT

```
  45615 SOD_pages.txt
 111423 SOD.txt
 157038 total
 SOGDIAN
DICTIONARY
Sogdian - Persian - English




      B.Gharib




   FARHANGAN   PUBLICATIONS
Sogdian Dictionary (Sogdian-Persian-English)
by B. Gharib
editorial supervisor: A. Mansouri
editor: S. Fotouhi
© 1995, Farhangan Publications
2/52. Shahid-e Said Street, Tehran 15916, Iran.
Tel: 6460069. Fax: 670230

ISBN: 964-5558-06-9
4f*Jj*l{^ 0"J-^8 'Jy^**-             ^J>*4^ tfW : j' a>„J^ <f jljX-U^ -LUi^-L ^JjJ'j^ L» e jlf ijj-
                                                                • l^> o-^ jl ^^<o (j ^jb^b             j uij^- ^C*"
                  ;l_^0 jL-u jlS' 4$" (.5*^-*^' "^^   (H^- fJ




                                                                                                                   L?JJ J'
```


## [2026-09-05T05:25:07.196Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'grow' SOD.txt | head -30",
 "description": "Grep SOD.txt for grow"
}
```


### [2026-09-05T05:25:07.253Z] TOOL RESULT

```
6181:/ro5/  rw5-  grow  Av.  rao£- 
10712:plant,  growth 
12549:happy  ?,  growing  ? 
12554:OtOgrow,  (/o)incrcasc 
25035:(fo)grow 
27805:0o)grow,  GcOincrease 
37142:growing 
60628:(to)grow 
60653:(to)grow 
60717:(ro)grow 
62155:Oojgrow 
65543:(fo)grow 
65580:(/<9)make  grow 
65737:(ro)grow 
65766:grown 
81073:(ro)increase,  (?<?)grow  up 
81078:growth,  salvation 
81086:spread,  grown  up,  full  grown 
82112:out  growth 
89856:full  grown     10786 
90138:(to)grow     779,  2630,  3078,  3101, 
90141:growing     778,  4456 
90142:grown    8590 
90143:grown  up     10786 
90144:growth    494,  10785 
90145:(to)grow  up     10784 
91524:(/6>)make  grow    8566 
92336:out  growth     10921
```


## [2026-09-05T05:25:07.911Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n '12\\.53' SYN.txt | head -10",
 "description": "Find Buck 12.53 grow"
}
```


### [2026-09-05T05:25:07.970Z] TOOL RESULT

```
9488:Lett. auglis, fr. Lett. augt, Lith. augti ‘grow’ (12.53). Mithl.-Endz. 1.216.
12896:ON avozir, OF westm, OHG wahsmo, all orig. ‘growth’, fr. ON vara, OF weazan, OHG wahsan ‘grow’ (12.53).
12898:Dan. gréde, Sw. gréda: Dan., Sw. gro, OE growan ‘grow’, ete. (12.53). Falk-Torp 356. Hellquist 307.
12914:Lett. auglis, in general ‘fruit, growth’, fr. Lett. augt ‘grow’ (12.53).
13443:Pol. winorosl (according to informant the best current word; many others in dicts.), epd. with ros! old word for ‘growth’ : résé, ChSI. rasti, ete. ‘prow’ (12.53).
22359:| 874 : ; 12.51 FORM, SHAPE : Grk. popdi, cxiua, eldos Goth. laudi, hiwi Lith. pavidalas 4 NG pop}, oxaua ON mynd, skapan Lett.  stdvs, augums, veids ( 1 Lat. forma, figura Dan. _ skikkelse, dannelse ChSl.  obrazit It. forma Sw. skapnad, gestalt SCr. _ oblik, lik cba | Fr. forme OE hiw, gesceap Boh. __podoba, tvar oy : Sp. forma ME __hiewe, forme, shap Pol. _ksztalt, postaé } Rum. forma NE form, shape Russ. obraz, vid be { Ir. cruth, delb Du. gestalte, gedaante Skt. ripa-, dkdra- ‘nl NIr. — cuma, cruth, dealbh OHG  bilidt . Av. vatéi-, kahrp- mel H W. furf MHG gestalt, gel@ne (bilde) Br. furm, neuz, aoz NHG | gestalt "e Some of the words for ‘shape, form’ | ‘potter’, Skt. dih- ‘smear’, etc. Walde- g have also the more generic sense of ‘ap- | P. 1.833. Ernout-M. 361 f. Walde-H, ME pearance’ and are connected with the | 1.502. OE If root for ‘see’ and ‘know’. Others are 3. Ir. cruth : W. pryd ‘appearance’, ra from verbs for ‘fashion, mold, create, | Skt. kr- ‘do, make’. Walde-P. 1.517. Ichi make’ or from such diverse notions as | Stokes 60. 100 | ‘hold’, ‘strike’, ‘grow’, etc. Ir. delb, NIr. dealbh : dolbaim ‘form, lat 1, Grk. pop¢7, etym.? Walde-P. | mold’, doilbthid ‘figulus’, W. delw ‘im- ate, 2.274, Boisacq 645. age’, Lat. doldre ‘hew, construct’, Skt, 77 Grk. oxfua, deriv. of éxw ‘hold, have’, | dal- ‘split, rend’, ete. Walde-P. 1.810. ] fut. cxjow, hence orig. ‘manner of holding | Stokes 150. ton oneself’, then ‘form, shape, bearing, NIv. cuma, fr. MIr. cumma ‘a break- (co manner’, etc., like Lat. habitus : habére. | ing, cutting, shaping, fashioning, man- ‘hn Walde-P. 2.482. ner’, fr. com-benim, cpd. of benim ‘strike, ath Grk. eldos, orig. ‘appearance, aspect’, | hew’. Pedersen 2.461. K. Meyer, Con- to hence ‘form, shape, kind’ (NG ‘kind’), | trib. 563. fal fr. the root of éléov ‘saw’, olda ‘know’, W. ffurf, fr. Lat. forma. Loth, Mots I like Lith. veidas ‘face, appearance’, Lett. | lat. 171. fre veids ‘form, appearance’, ChSl. vidi Br. furm, fr. OF r. fourme (for this and vor ‘look, appearance’, etc. Walde-P. 1.239. | the other Br. words, see Vallée s.v. din Boisacq 220. forme). } 2. Lat. forma (>It. forma, OFr. Br. neuz, also aoz : Ir. gnas ‘habit’, W. Di fourme > ME forme, NE form; Fr. gnaws ‘nature’, Lat. ndtus, Skt. jnala- ai Jorme, Sp. forma, Rum. formd are lit. ‘known’, etc. Pedersen 1.49. Loth, RC We borrowings), etym. dub. Connection | 42.371. 19] with Grk. Hopi, either by borrowing and 4, Goth. laudi : liudan, OF leodan, 2 eesti of consonants (through OS liodan ‘spring up, grow’, Skt. rudh-, lah can?) or otherwise is possible. Er- | Av. raod- ‘grow’ (12.53). Walde-P. nout-M. 378f. Walde-H. 1.530f. 2.416. Feist 323. ap = sie jos eb acrn eal more or less Goth. hiwi, OF hiw, heow also ‘color, it 7 o mica! word in most of the | appearance’, ME hiewe (in all senses MW ur. ‘anguages, as Dan., Sw., NHG | NE hue restricted to ‘color’) : ON Aj Mh form, in Slavic languages forma. ‘down’, Sw. hy ‘color of the skin’, root th eg “laws prepenty ‘shape given to | connection disputed, perh. fr. that in Oo ( : fingere ‘shape, mold’, figulus | he@wen ‘blue’, Ir. ctar ‘dark’, ON hart th
22403:12.53 GROW
30065:Av. huraoéa-, epd. of hu-(= Skt. su-) and raoéa- ‘growth’, pl. ‘outward ap- pearance’ (: rud-, Skt. rudh- ‘grow’ 12.53),
```


## [2026-09-05T05:25:12.769Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '22395,22420p' SYN.txt | cut -c1-4000",
 "description": "Read Buck 12.53 GROW"
}
```


### [2026-09-05T05:25:12.824Z] TOOL RESULT

```
Digitized by Arya Samaj Foundation Chennai and eGangotri
876 SELECTED INDO-EUROPEAN SYNONYMS 12.52 SIZE
I kyo Goth. mikilei Lith. didumas, did bé ees ON | storleikr Toke, Uelume Lat. magnitidd Dan. _ sigrrelse ChSI.  veliéije, veltétsturje It. grandezza Sw. storlek SCr. _ velitina Fr. grandeur OE micelness Boh.  velikost’ Sp. tamaiio ME mikelnes, syse Pol. wielkogé Rum. médrime NE size Russ. _velitina Ir. méeit Du. grootte Skt. mdna-, mahas- Nir. méid OHG = mihheli, grizi Av. mazah-, masah- W. maint MHG graze, michel Br. ment NHG grésse
Most of the words for ‘size’ are ob- vious derivs. of the adjectives for ‘large, big’ (12.55), that is, ‘bigness’ is used for ‘the degree of bigness’, as Grk. péyeOos : peyas, Lat. magnitudd : magnus, Goth. mikilei : mikils, etc.—all the words list- ed, with the following exceptions:
1. Sp. tamajio, sb. of adj. tamazio ‘so large’ (Lat. tam magnus ‘so large’). REW 8552.
2. Ir. méit, NIr. méid, W. maint, Br. ment, perh. *manti, old abstract forma- tion fr. root in Ir. mar ‘large’ (12.55). Pedersen 1.242 f., 2.48. Walde-P. 2.238.
3. ME syse, NE size, fr. OFr. sise, cise for assise lit. ‘act of settling or fixing something’ (esp. assessments, levies, etc.), pple. of OFr. asseir ‘sit at, set down, settle’ (Lat. adsidére). The mod- ern sense is late in ME, earlier ‘assize’ then esp. ‘regulation of amount, quan- tity (of a tax, etc.)’ and ‘fixed quantity or size’. NED s.yv. size, sb.!.
4. Skt. mana-, esp. cpds. parimana-, pramdana-, lit. ‘measure’ : md- ‘measure’ (12.54).
12.53 GROW
(= Increase in Size) Grk.  abkdvopat Goth. wahsjan Lith.  augti NG Heyaddvw, attavw ON vaza Lett.  augt Lat. _créscere, augéscere Dan.  vokse ChSl.  rasti It. crescere Sw. vdxa SCr. —_rasti Fr. crottre OE weazan Boh. riisti Sp. crecer ME _waze, growe Pol. rosnqé Rum. cresle NE grow Russ. rasti Ir. Gsaim, forbiur Du. —_groeien, wassen Skt.  urdh-, rudh-, uks- Nir. fasaim OHG wahsan Ay. varad-, rud-, uxs- W. tyfu MHG wahsen Br. kreski NHG  wachsen
Most of the words for ‘grow’ were probably used primarily with reference to plant life, as is demonstrably the case for NE grow.
1. IE *aweg- (*aug-, *ug-, and with ~s- extension *aweks-, etc., orig. desid. formation). Walde-P. 1.22f. Ernout- M. 88 ff. Walde-H, 1.82 f., 850. Falk- Torp 1390. Feist 67, 541.
Grk. avéavw, also attw, aéfw (*aétw) ‘increase’ (trans.) with mid. avtdvopat etc. ‘grow’ (intr., but NG attavw trans. and intr.); Lat. augére ‘increase’ trans., rarely also intr. ‘grow’, inchoat. augescere intr.; Goth. wahsjan, OE weazan etc. general Gme. (NE waz of the moon, but mostly arch.); Lith. augli, Lett. augt; Skt. uks-, Av. uxs- (88g. pres. uasyeili);
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
gpATIAL RELATIONS:
A oks- tgrow’ OSM B aulsu ‘old’ , s re yeyard¥@ fr. peyados ‘large 9, NGr.
(284) rascere (> It. crescere, Fr. : cer, Rum. creste) : creare BP a Arm. sernem ‘beget’, i feed’, Grk. Kopéokw, atiate’. Walde-P. 1.408. 39, Walde-H. 1.288. : Lie asaim, Ir. fasaim, ef. Ir. as canth’, perb- (with loss of init. w in cue - Goth. wahsjan, ete.
© api) fr. *woks- a hi G.S. Lane, Language 13.21. ?
otherwise Strachan, IF 2.370.
Ir forbiur, cpd. of birw ‘carry’ and for ft, hence lit. ‘carry on’. Pedersen 9407 f.
V. fu : Lat. tumere ‘swell, be swoll- a, fr, an extension of the root *éu- in Sut, fduli ‘is strong’, ChSl. tyéz “become fat’, etc, Walde-P. 1.708. Ernout-M. 1064.
Br. kreski, prob. fr. Lat. créscere. Henry 81. Loth, Mots lat. 154 (with sme question on account of the short vorel),
Digitized by Arya Samaj Foundation Chennai and eGangotri
PLACE, FORM, SIZE 877 5. ME growe, NE grow, Du. groeien, but OE gréwan, ON gréa, OHG gruoan only ‘grow’ (of plants), ‘spring up, be- come green, etc.’ : MHG gruose ‘shoot of a plant, sap’, Goth., ON, OHG gras OE graes ‘grass’, ON grenn, OE gréne, OHG gruoni ‘green’, Lat. gramen ‘grass’. Walde-P. 1.645f. NED s.v. grow, vb. 6. ChSl. rasti, etc., general Slavic (Pol. r6sé replaced in present by rosnqé), fr. *ord(h)-t-, prob. : Lat. arduus ‘steep, high’, Ir. ard, Av. aradwa- ‘high’. Walde-P. 1.149. Briickner 463.
7. Skt. vrdh- act. and caus. ‘make grow or thrive, elevate’, mid. ‘grow, thrive’, Av. varad- act. (and mid.) ‘make grow or thrive, increase’, mid. and pass. ‘grow, thrive’ : ardhva- ‘up- ward, upright, raised, elevated’, Grk. dps ‘upright, straight’, Slavic roditi ‘bear’. Walde-P. 1.289.
Skt. rudh-, ruh-, Av. rud- (pres. 3pl. Skt. rodhanti, Av. raodanti) : Goth. liu- dan ‘grow up’ (of seed, Mk. 4.27), OK léodan, OHG ar-liotan ‘spring, grow’ (of plants), ON lodinn ‘grown over, hairy’. Walde-P. 2.416.
```


## [2026-09-05T05:25:20.276Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '12540,12570p' SOD.txt; echo \"=== index refs to entry ===\"; sed -n '90135,90150p' SOD.txt",
 "description": "Read SOD around 'to grow'"
}
```


### [2026-09-05T05:25:20.409Z] TOOL RESULT

```
777  V^nt   B,  S  JUip- 
(D>Yusand  ?,  (o)xwasand  ?   ^Yws'nt  ?,  wYsndyy 
happy 

VJ  54c;  GMS  969;  Frag.  Len.  25.5,  37.12,  58.2 

778  'Yws'nt'k   B  ?  *jlj_i>  <?  j>^*- 
(o)xusandc  ?  Oxwsndyy) 

happy  ?,  growing  ? 
TSP  2.75;  Hen.  Texts.  716 

779  'Yws'y-   B,  S  jj^Tj^j  <  j->j>' 
(o)xwasay  ?   (^wsy-)  ©Av.  vaxs-   =>xws~ 
OtOgrow,  (/o)incrcasc 

TSP  2.358,  359,  778,  886,  905;  Frag.  Len.  90,  6; 
GMS  428 

780  'Yws'yp-   B  &J<^ 
(o)xusep   (Yysyp)  ©<*xsvep\  Av.  xsvaeva 
squinting 

Hen.  BBB  p63,  523;  GMS  162,  243  n  1,  416;  SCE 
409  ->y;  >Yw?p  csrrtk  "squint-eycdM  SCE  23 

781  }Ywsmy   B  ^ 
(o)xusme,  oxusmi    =»wYsmy 

sixth 

=== index refs to entry ===
grotto     1768 
ground     11217 
group     1130 
(to)grow     779,  2630,  3078,  3101, 

7838,  7842,  7850,  8071,  8562,  8588 
growing     778,  4456 
grown    8590 
grown  up     10786 
growth    494,  10785 
(to)grow  up     10784 
(to)guard    4040 
guarded    6546 
guardian     4064,  6496,  6514 
guest    4304,  4305,  6186 
guide     1779
```


## [2026-09-05T05:25:30.836Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"779\" SOD_pages.txt | head -5; echo \"---\"; awk '/\\[pdf page/{p=$0} /779  V\\^nt|779.*Yws.y/{print NR\": \"p\" :: \"$0}' SOD_pages.txt | head -5",
 "description": "Find page of SOD entry 779"
}
```


### [2026-09-05T05:25:32.451Z] TOOL RESULT

```
5945:         Problcmes dc Linguistique Generale 1966, 1,             779 'Yws'y-       B, S                      jj^Tj^j < j->j>'
8660:                                                                                  781,779
8874:       part, portion ?, bowl ?                                    1779 »st»yny C                           (tjujtjjUj)^^
10146:2193 >yncy* S                                                             GMS 779; BSTBL, Dhy. 210, 219; AVS 225
11726:2779 prtp8y}h M                  :                   jtU<j*lfl
---
5945:  ::          Problcmes dc Linguistique Generale 1966, 1,             779 'Yws'y-       B, S                      jj^Tj^j < j->j>'
```


## [2026-09-05T05:25:35.194Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=5945 && /\\[pdf page/{p=$0; n=NR} END{}' SOD_pages.txt; grep -n '\\[pdf page' SOD_pages.txt | awk -F: '$1<5945' | tail -3",
 "description": "Find pdf page tag before line 5945"
}
```


### [2026-09-05T05:25:36.852Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T05:25:40.157Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c 'pdf page' SOD_pages.txt; awk 'BEGIN{RS=\"\\f\"} /779.*Yws.y-/{print \"leaf(1-based awk)=\"NR}' SOD_pages.txt",
 "description": "Locate leaf for SOD entry 779"
}
```


### [2026-09-05T05:25:42.000Z] TOOL RESULT

```
0
leaf(1-based awk)=96
```


## [2026-09-05T05:25:46.884Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'Uvax\\|uvaxš\\|uvaxs\\|Cyaxares\\|vaxš\\|vaxs-' KNT.txt | head -30",
 "description": "Grep Kent for Uvaxštra"
}
```


### [2026-09-05T05:25:46.948Z] TOOL RESULT

```
358:67. Тнк Mepran Рглгест was the language of the great Median Empire, which at the death of Cyaxares in 594 extended from the Indus to the Aegean Sea; the last Median ruler was Astyages, son of Cyaxares, who in' 559 was conquered and deposed by his grandson Cyrus, son of Cambyses King of Persis and of Mandane daughter of Astyages. The new ruler naturally took over the Median chancellery and the Median royal titles, and their influence is still seen in the language of the OP inscriptions of Darius and his followers.
382:Uvarsira ‘Cyaxares’, a king of the Median line, with {т retained after a sibilant.
623:b. Sometimes in other genitives standing before the nouns on which they depend: UvaxStrahyd taumayd DB 4.19, 422, eJ, g.9f (but -hyä DB 2.15f, 2.81); Nabunaitahyd puça DB 3.81, 4.14, 430, d.5f, 17 (but -hyä DB 1.79); Halditahyá puga DB 3.79; or with which they agree: Aurahyd Mazdáha ХРе 10 (cf. $44); harwahydya bumiya DSb 8f (but probably -yüyà DSf 16, 18).
1103:679. РАН. ir AFTER SPIRANTS (including the sibilants) appears unchanged in Avestan. This seems to have been the development also in Median, as in the name of the Меде Uvaz&tra- ‘Cyaxares’, Elam. ma-ak-i§-ta-ra, АКК. ú-ma-ku- iš-tar. The name of the northeastern province Bactria, Gk. Béxrpa, likewise shows a non-OP form in Bazirig, Elam. ba-ik-tur-ri-i$, АКК. ba-ab- lar; but à pure OP *Büz&s or *Báxgis is attested by the alternative Elam. ba-ak-&i-i$. Finally, OP uSa-bari- ‘camel-borne’, by comparison with Av. ustra- ‘camel’, shows that in OP, even after a spirant or a sibilant, tr became ør and then ç, and that after š the с was assimilated to that preceding š.
3586:Техт or DB, Сошмх П: 1 :98ty : Dárayavaus : xSayafiya : paeüva : Naditabaira : ha 2 dà : kamnaibis : asabaraibis : amufa : Bübirum : ašiya 3 va: pasàva : adam : Babirum : ašiyavam : vasnd : Auramazdiha : uta : Ba 4 birum : agarbiyam : uta : avam : Naditabairam : agarbüyam : pasáva : ava 5 m : Naditabairam : adam : Babirauv : avüjanam —— :0ütüy : Dārayavauš : x 6 Sdyabiya : yātā : adam : Bübirauv : àham : ima : dahydva : tyà : hacàma : ha 7 migiyà : abava : Рагва : Üvja : Mada : Aðurā : Mudráya : Parfava : Margus : Өз 8 tagui:Saka : абу : Dārayavauš : x8dyabiya : I martiya : Martiya : nā Q ma : Cicixrais : puca : Kuganakà : пата : vardanam : Pársaty : avada : adaraya : 10 hauv : udapatatà : Uvjaiy : Кагаһуй : avaðā : afaha : adam : Imanis : amiy : 0 11 vjeiy :xSdyafiya —— : @atiy : Darayavaus : zsayattya : adakaiy : adam : asna 12 iy : àham : abiy : Üvjam : pasáva : hac&ma : alarsa : Üvjiy& : avam : Marti 13 yam :agarbaya : hyašām : mafista : dha : шат : avàjana — : 00у: D 14 árayavaus : xSiyafiya : І martiya : Fravartiá : пата : Мада : hauv : udapatat 15 à : Madaiy : Катаһуй : ауаба : абала : adam : XSa6rita : amìy : Uvaxdtrah 16 уй : taumàyá : pasáva : kāra : Mada : hya : v'àpaliy : haw : hacáma : hamiciya : a 17 bava : abiy : avam : Fravartim : aSiyava : hauv : тёйуайтуа : abava : Madaiy 18 9àtry : Dárayavaus : xšāyaðiya : kara : Parsa : ша : Мада : bya : ира : mim : 4 19 ha : hauv : kamnam : aha : раѕауа : adam : kdram : fraiSayam : Vidarna : пата : Pársa : man 7 20 à : badaka : avam&àm : mafistam : akunavam : avataSaám : afaham : parait : avam : К 2] dram : tyam : Madam : jatà : hya : mand : пау : gaubataiy : pasiva : hauv : Vidarna : ha 22 dà : kara : айуауа : yafà : Madam : parárasa : Māruš : пата : vardanam : Ma 23 дау : ауада : hamaranam : akunaus : hada : Мада : һуа : Màdaisuvà 24 :ma(iSta : dha : hauv : adakaiy : пау : avadà : аһа : Auramazdimary : u 25 раѕійт : арага : vasnà : Auramazdáha : kāra : hya : тара : avam : kàram : t 26 yam : hamiciyam : aja : vasiy : Animakahya : mähyä : XXVII : raueabis : fakat 27 à : аһа : avatüsám : hamaranam : kartam : pasáva : hauv : Ката : һуа : manā : Карада : пат 28 à : dahydus : Mádaiy : avadà : mam : amánaiya : y8tà : adam : arasam : Mada ' 20m : 08у : Dàrayavaus : xšāyaðiya : адаг х : nàma : Arminiya : man 30 à : badaka : avam : adam : frāišayam : Árminam : avafasazy : aaham : paraidiy : ka 31 ra : һуа : hamigiya : mană : naiy : gaubataiy : avam : jadiy : pasiva : Dadarsi 32 š : aSiyava : yafà : Arminam : parárasa : pasáva : hamigiya : hagmatà : paral 33 tà : patiš : Dādaršim : hamaranam : cartanaiy : Züzahya : пата : àvahanam : А 34 rmíniyaiy : avadà : hamaranam : akunava : Auramazdimaiy : upastàm : a 35 bara : vasnà : Auramazdàha : kāra : һуа : manā : avam : küram : {уаш : hamigiyam : 36 aja : vasiy : Oüravaharahya : máhya : VIII : raucabis : 09akatà : dha : ava 87 à$üm : hamaranam :kartam : бабу : Dárayavaus : z3àyaffya : patiy : duv 38 itiyam : hamigiyà : hagmatà : paraitd : patiš : Dàdar&im : hamaranam : carta 3€ nay : Tigra : пата : didà : Arm‘niyavy : avadà : hamaranam : akunava : А 40 uramazdàmaiy : upastàm : арага : vašnā : Ашатагдаћа : kāra : һуа : тапа :a 41 vam : káram : tyam : hamigiyam : aja : vasiy : G9üravüharahya : mihya : ХҮШ 42 :raueabiá : бакаќа : аһа : ауабадат : hamaranam : kartam —— : 00у : Daraya 43 vaus : xšāyaðiya : patiy : citiyam : hamictyd : hagmatà : paraita : pat 44 iš : Dádar&im : hamaranam : cartanaiy : Uyama : nama : didi : Arm'myaty :a 45 vadā : hamaranam : akunava : Auramazdimaiy : upastam : арага : vaSnà : Aurama 46 zdàha : kāra : һуа : manā : avam : küram : tyam : ham?giyam : aja : vasiy : Oàigarea 7 d :mábyà : IX : raucabis : Nakata : dha : ауада ат : hamaranam : kartam : pasava 48 : Dadarsis : citā : mim : amánaya : Arm/niyaiy : yiti : adam : arasam : Ма
3624:81 iy : Uvaxstrahya : taumiya : pasiva : adam : Кагал : Parsam : ut
3657:$24. 2.18-7. Saith Darius the King: One man, by name Phraortes, а Median—he rose up in Media. To the people thus he said, "I am Khsha- thrita, of the family of Cyaxares." Thereafter the Median army which (was) in the palace, became rebellious from me, (and) went over to that Phraortes. He became king in Media.
3683:§33. 2.78-91. Saith Darius the King: One man by name Cicantakhma, a Sagartian—he became rebellious to me; thus he said to the people, “I am king in Sagartia, of the family of Cyaxares.” Thereupon І sent off a Persian and Median army; a Mede by name Takhmaspada, my subject—
3817:1 :98tiy : Darayavaus : xsayaüiya : ima : t 2 ya:manà :kartam': Babireuv — :98ty : D З árayavaus : xSàyaftya : ima : tya : adam : akuna 4 vam : vasnà : Autamazdiha : һашаһуйуй : баг 5 da : pasáva : yada : xšāyaðiya : abavam : ХІХ : hamaran 6 Я : akunavam : vasnd : Auramazdiha : adamšim : а Т janam : uta : IX : x&ayatty& : agarbiyam : 1 Gaumata : 8 n&ma : magus : aha : hau : adurujiya : ava : абаһа : adam : 9 Bardiya : amiy : hya : Küraus : puça : hauv : Parsam : ha 3 10 migiyam : akunaus : Z Acina : пата : Uvjiya : hauv : adu 11 rujiya : ауаба : afaha : adam : xSiyaliya : amiy : Uvjaiy 12 : hauv : Üvjam : hamigiyam : akunaus : manā : I Naditabaira : n 13 dma : Babiruviya : hauv : adurujiya : avafá : aGaha : 14 adam : Nabukudracara : amiy : hya : Nabunaitahya : puga : 15 hauv : Babirum : hamigiyain : akunaus : I Martiya : na 16 ma : Pársa : hauv : adurujiya : атаба : ađaha : adam : Imani 17 š : amiy : Uvjaiy : cSayasiya : hauv : Üvjam : hamiciya 18 m : akunaus : I Fravarti$ : пата : Mada : hauv : adurujiya 19 : ауада : абаћа : adam : XSa@rita : amiy : UvaxStrahya : taumay 20 à : hauv : Madam : hamiciyam : akunaus : I Cigataxma : пата : Asa 21 gartiya : hauv : adurujiya : ava : afaha : adam : xšāyað 22 iya : amiy : Asagariaiy : UvaxStrahya : taumāyā : hauv 23 : Asagartam : hamigiyam : akunauS : І Frida : nama : 24 Margava : liauv : adurujiya : ааба : ađaha : adam :
3906:and the same year after that I became king. XIX battles I fought; by the favor of Ahuramazda I smote them and took prisoner IX. kings. One was Gaumata by name, a Magian; he lied; thus he said: ^I am Smerdis, the son of Cyrus;" he made Persia rebellious. One, Agina by name, an Elamite; he lied; thus he said: “I am king in Elam;" he made Elam rebellious. One, Nidintu- Bel by name, а Babylonian; he lied; thus he said: “Т am Nebuchadrezzar, the son of Nabonidus;" he made Babylon rebellious. One, Martiya by name, a Persian; he lied; thus he said: "I am Imanish, king in Elam;" he made Elam rebellious. One, Phraortes by name, à Mede; he lied; thus he said: "I am Khshathrita, of the family of Cyaxares;" he made Media rebelhous. One, Cicantakhma by name, a Sagartian; he lied; thus he said: "I am king in Sagartia, of the family of Cyaxares;” he made Sagartia rebellious. Опе, Frada by name, a Margian; he lied; thus he said: “I am king in Margiana;" he made Margiana rebellious. One, Vahyazdata by name, a Persian; he lied; thus he said: “I am Smerdis, the son of Cyrus;” he made Persia rebellious. One, Arkha by name, an Armenian; he lied; thus he said: “T am Nebuchadrezzar, the son of Nabonidus;” he made Babylon rebellious.
3985:7 : Uvaxštrahya
4881:Phraortes, claiming to be Khshathrita, of the family of Cyaxares, had made himself king of a great part of the Empire ($21). Darius’s first step was to send Vaumisa, a Persian officer, against the rebels in Armenia; he must have sent Vaumisa early in the Babylonian campaign, for Vaumisa, on the way north, was met by the rebels at [zala in Assyria, on X 15. What forces Vaumisa had at his disposal is not stated, but no mention 1s made of sending troops with him; presumably he gathered up loyal troops on the way. By,this battle Vaumisa
4890:hered to Phraortes, declared himself King in Sagartia, a distriet of northern Media; he claimed to be of the family of Cyaxares. Darius sent а force of Medes and Persians under Takhmaspada, a Median officer, who defeated and captured Cicantakhma, bringing him to Darius. Darius mu- tilated him and put him to death with torture, at Arbela ($33). Thus ended rebellion in Media (884) ; but there was still a strong rebel force in Armenia, against which Darius sent an Armenian officer named Dadarshi. Dadarshi, thrice attacked by the rebels, defeated them successively at Zuzaya on II 8 (§26), at Tigra on II 18 (§27), and at Uyama on III 9, whereafter he waited for Darius to come and make final governmental dispositions (828). This third battle by Dadarshi was only nine days after Vaumisa in а second engagement beat off the other force of Armenian rebels in the dis- trict of Autiyara, on IT 30; after which he also awaited Darius’s arrival (530). There was по fur- ther fighting in Armenia.
5158:^u- insep. prefix ‘good, well’ (uv- before vow- els): Av. hu-, Skt. su-, Gk. 0-уиѕ ‘having good life, healthy’, pIE *su- (§140.IV): in uxSnav-, ukàra-, ucüra-, Utüna-, ulava-, ubanwaniya-, ufrasta- ufrasta-, ubarta-, umartiya-, иғада-, uradana-, Uvaxstra-, &Uvürazmi-, warstika-, uvdsabdra-, waspa-, dinara-, uwkhamaranakara-.
5205:‘UvaaStra- sb. ‘Cyaxares’, former King of Media: Elam. ma-ak-tš-tar-ra, АКК. ú-ma-ku-iš- lar, Gk. Kva£ápys. From u- ‘good’ + varštra- ‘growth’ ($9.11, $79, $148.11), to vaxi-, Av. vazš-, Skt. vaks-, Gm. wachsen, N Eng. wax ($102): 'Hav- ing good growth’ ($164.11, IV). So ВЫ. AiW 1836; but Hz. АрІ 209 interprets ‘having good oversight’, to Av. aiwy-axrstrat (dat.) ‘oversight’ (otherwise Hüsing, OLZ 2.139-40). Стах аһу gsm. DB 2.15f, 81.  Uvaxstrahya (S86.IVb) DB 4.19, 22; DBe 7; ОВр 9f.
```


## [2026-09-05T05:26:10.206Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} {n=NR} /Uvaa?xStra- sb/ {print \"KNT leaf(awk)=\"NR}' KNT.txt; echo \"=== KNT vaxš- entry ===\"; grep -n \"^vax\\|vaxš- \\|vaxs- \" KNT.txt | head -10",
 "description": "Locate Kent leaf and vaxš entry"
}
```


## [2026-09-05T05:26:10.547Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB p.33 ===\" && awk 'BEGIN{RS=\"\\f\"} NR==44 {print}' HUB.txt | head -60",
 "description": "Print Hübschmann p.33"
}
```


### [2026-09-05T05:26:12.057Z] TOOL RESULT

```
=== KNT vaxš- entry ===
```


### [2026-09-05T05:26:13.871Z] TOOL RESULT

```
=== HUB p.33 ===
— 33 —
245. Zd. hubaira- *glucklich' ■=•- paz. hubahar kann ich mit
Geiger nur zu skr. subhadra- *herrlich* stellen. Dann
ware np. bahr, bahra 'Teil, Anteil, Loos, Gliick'
= skr. bhadra- *herrlich, glucklich ; Gltick, Heil, Gutes'?
Zu dieser Etymologie stimmt nur die Bedeutung von
bahr, die mir die urspriingliche zu sein scheint, *Teil\
Anteir (vgl. np, baxt 'Schicksal, Gliick* =^ skr. bhaktor-
'zugeteilt') nicht. Np. barx^ barxa 'Teil' = afgh. LW.
braxa, baxra share, portion, part, lot' (Raverty) setze
ich = ap. *baxtra-, zd. baxdra- (vgl. np. Balx aus ap.
Bdxtri' *Bactrien') von zd. bal = skr. bhaj *teilen, zu-
teilen (meine Avestastudien p. 696). Zd. bax^ra- braucht
nicht *Mahlzeit' zu heissen, Darmesteter iibersetzt es
durch 'revenue' und stellt es zu bhaj *teilen, zuteilen*,
vgl. ap. baji' *Tribut'. So wird auch np. 6aAr = barx
= zd. baxdra- sein.
247. Np. he = paz. atvS, phi. apB setze ich = ap. *apaiy
aus apa + id, wie naiy nicht' = fia + id (skr. ned)
ist. Die Form ist in der Composition entstanden, sonst
ware *apaii/ zu np. ab geworden. Im Phi. und Pazend
findet sich apS, awS nur als 1. Glied von Compositis,
wie auch im Neupersischen bS noch moistens in Com-
position erscheint.
249. Zu beoctan *sieben' (nach Noldeke *streuen) stellt
Geiger jetzt afgh. mnjql reinigen, saubern, waschen'.
Als Lehnwort gehSrt dazu afgh. badpBzt 'Absurditat
(== Windsieberei nach Raverty) sowie bSzql, pSzql
sieben, Geiger, Etym. und Lautl. d. Afghan. Nr. 360.
250. Zu bddbe»9 badbSzan u. s. w. Tacher' vgl. Journ.
asiat. 1893, p. 256.
251. Dazu afgh. vala 'Weide* (nach Geiger), als Lehn-
wort afgh. bSd *Weide'.
252. Vgl. dagegen Darmesteter, Etud. iran. I, 281, der
*dBrUn als lautgesetzliche Form erwartet. Auch nach
Horn Nr. 545 miisste beriln dialektisch sein. Dazu
phi. vTrUnakd 'the extreme limits*, West, PT. L 160.
253. Vgl. paz. awTm (var. avBm) Min. Gl. 27, awlza Shk. 235.
uabsohmann, Persiache Studien. 3
```


## [2026-09-05T05:26:21.283Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB banafs ===\"; grep -n -i 'banafs\\|banafš\\|vanafs\\|banaf' HUB.txt | head; echo \"=== HRN banafs ===\"; grep -n -i 'banafs\\|banafš\\|vanafs\\|vanavas\\|Veilchen' HRN.txt | head -20",
 "description": "Grep Hübschmann and Horn for banafše"
}
```


### [2026-09-05T05:26:21.401Z] TOOL RESULT

```
=== HUB banafs ===
1029:231. Np. hiinafSu *Veilchen ^ phi. vanavsak (fiir vanafsak)
4403:mobad etc.) = zd. paiti-, arm. -pet ; banafsa 'Veilchen' neben
4404:binafsa, bunafsa, arab. banafsaj, phi. vanavsak^ etc.
5459:bisyar Viel' =■ paz. vasydr Min. Gl. 210; banafsa 'Veilchen'
8409:in banafsa 'Veilchen' H. 231, s. oben p. 31. Dunkel ist
10310:banafia 31.
=== HRN banafs ===
2389:ar. LW. banafsaj, syr. LW. <3J^E>:32 (de Lagarde,
```


## [2026-09-05T05:26:25.033Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB line 1029 context ===\"; sed -n '1020,1045p' HUB.txt; echo; echo \"=== which HUB leaf? ===\"; awk 'BEGIN{RS=\"\\f\"} /231\\. Np\\. h.nafS/{print \"leaf(awk)=\"NR}' HUB.txt; echo \"=== HRN 2389 context ===\"; sed -n '2380,2400p' HRN.txt",
 "description": "Read Hübschmann 231 and Horn banafše"
}
```


### [2026-09-05T05:26:26.734Z] TOOL RESULT

```
=== HUB line 1029 context ===
schaft*, Gegensatz arm. nizdkateg 'Lanzenspitze*. Im
Falle aber, dass arm. bun aus alterem *budn ent-
standen ware, musste es fiir original gelten. Horn's
Behauptung in Anm. 1 : idg. ^ = zd. u, u ist trotz
Jackson und Andreas unerwiesen und falsch. Arm.
p'ww/ 'Halm* geh5rt trotz Bugge nicht hierher, ebenso
wenig np. buna *Lager, Gepack\ bal. LW. bunag *Gepack*
(Geiger, Lautlehre p. 24), arm. bnak 'Wohnung',
bnakem Vohne'.
231. Np. hiinafSu *Veilchen ^ phi. vanavsak (fiir vanafsak)
nach Fr. Muller WZKM. 7, 368 = zd. ^vanavaxsa-
(also — *im Walde wachsend). Mir nicht wahrschein-
lich.
232. Np. bang bei Abu Muwaffaq p. 54. Zu np. mang
vgl. phi. mang Gl. and Ind. 220.
234. Np. bor *Fuchs hat mit skr. babhru-^ dem im Persi-
schen nur *babr entsprechen wiirde (vgl. Nr. 181) nichts
zTi schaflfen.
235. Horn's Zusammenstellungen sind hochst bedenklich.
Wenn sich die Begriffe *kussen' und 'riechen* vereinigen
lassen (vgl. skr. ghra riechen, beriechen, kiissen ), kann
man mit Fr. Muller, WZKM. 7, 145 arm. hamboir
'Kuss* als LW. auf ap. *ha(n)'bauda' und np. bosa/m- 32 -
*kusse' auf iran. *6awd-s-a»ii (vgl. Nr.240: toi'Geruch*
= zd. baoidi') zuriickfiihren. Np. mad 'Kuss' erinnert
an afgh. maca *Kuss'. — Arab, 'arus lautet im Persi-

=== which HUB leaf? ===
=== HRN 2389 context ===
2) *6epäck', phlv. bunak *Gepäck, La^er', Nöldeke,
ZDM6. 46, 143 (vergl. bei. bunag, n. bunay (41)
*Gepäck').
230. bende *Sklave, Diener'.
ap. ba(n)daka- 'Sklave*; phlv. bandak,
231. henefSe Teilchen, bunefse^ binefse; bunefs *blau'
(Sahn. I, 48 Vers 265, 107 Vers 839)\
mäz. venewse,
phlv. vanawsak, vanatcsa Teilchen (Bund.).
ar. LW. banafsaj, syr. LW. <3J^E>:32 (de Lagarde,
Ges. Abh. 22), arm. LW. maniisak (de Lagarde,
No. 1427).
232. heng 'Bilsenkraut', bengi 'sinnlos '), vergl. metig *Hanf .
aw. batiha- ein Narcoticum, vergl. Banga-; skr.
bhatigä- 'Hanf; ein aus Hanfsamen bereitetes Nar-
coticum'; arm. LW. bang voaxiaiiiog, ar. LW. banj; af;\
bang 'RsLiif; nhd. Bangenkraut 'Schierling* (Grimm,
Wörterbuch I, 1105).
russ. penka, poln. pienka, czech. pcnek, p6nka scheinen
entlehnt (Hehn, Kulturpfl. 484). ^
233. huden 'sein, Praes. buv-em'^ vergl. bos-em, bad; buvis, 0Ou)
```


## [2026-09-05T05:26:53.355Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD wanafsag ===\"; grep -n -i 'wanafšag\\|wanafsag\\|wanafs\\|vanafs' PHD.txt PHD_mackenzie.txt | head -10; echo \"=== NYB ===\"; grep -n -i 'wanafs\\|vanafs\\|pērōz\\|peroz\\|pērōč' NYB_vol2_glossary.txt | head -20",
 "description": "Grep MacKenzie and Nyberg"
}
```


### [2026-09-05T05:26:53.434Z] TOOL RESULT

```
=== PHD wanafsag ===
PHD.txt:605:wad-baxt [wtP ht! | N badbaxt] unfortunate. wad-dil [wtdyl | M wddyl, N baddil] coward(ly). wadgarih [wtglyh] evil-doing. wād-ģirdaģ [w° tgltk' | (N gird-bād)] whirlwind. wad-góhr [wtgwhl | N bad-gauhar] ill-, low-born. wad-kamag [wtk’mk'] malevolent. ~ih: malevolence. wadrang [w’ ting | N bādrang] citron. cc Dë [-bwd | N -bóya] lemon balm. wad|-tóhm [wttwhm] = wad-góhr. ~-wazag [-w’ck! | (N gawāža)] abuse. --.Xém [-hym] ill-natured. waf- [wp- | Р wf-, (N bàf-)] weave. ~išn: weaving. wafr [wp! | M wpr, N barf] snow. ~énag [-ynk!] а sweetmeat. waydān [wy?n! = Av. waybana-] head (ahuric). wahāg [wP?k! | M тор, N baha] trading; value. — burdan: value, estimate. wahār [wh], (bj?l) | M wkr, № bahar] spring. ~ig [-уЁ! | N -z] spring, vernal. wahig [ZZLA < A Semi (?); whyk' | M whyg, N *bahi] kid; astr. Capricorn. wahist [ол | M whyst, N bihist] paradise. ~Ig [-yk! | N -1] (worthy) of paradise. Wahman [whwmn' | M whmn, N bahman] Good Mind, the first Amahra- spand, guardian of cattle; cal. 11th month; 2nd day. wāhmān [*w-n! = whmn' | MOw^hmn, J whmn, N bahman] so-and-so. Wahrām [wlhl?’n', whPm | M whr’m, N bahram] god of war, victory; astr. Mars; cal. zoth day. ātaxš 1~: a major sacred fire. wak [wk! | N bak] frog. wālan [zo n! | (IN barzan)] settlement, community walg [wlg] = warg. walidan, wāl- [w]-ytn! | N bdlidan] grow, increase, prosper. ~išn: growth. wümidan, wam- [w’m-yin'] vomit. wan [wn' | N bun] tree; stock, stem. ~ i $urgünig : pistachio tree. ~ 1 was-téhmag: the Tree of Many Seeds. wān-, ~išn, v. wanidan. wanafšag [zvnpšk! | N bunafša) violet. Wanand [wnnd] astr. Vega. wandaģ [wndk'] rope, cord. wang [KALA < А ql’; wng | = M, N bang] voice, cry. wānīdan, wan- [wn-ytn! | M w’n-yst] conquer, overcome, destroy.
PHD.txt:4225:violet wanafšag.
PHD.txt:5187:niwistan winastag wanafšag winjisk nizār nizārīh nizārīh- nazd nazdikih nazdik wizend nazdist wizend wizand- wizandag
PHD_mackenzie.txt:10113:wanafSag                \~4)\\      winah-
=== NYB ===
3119:péróz [pylwe'] victorious, victor 2719. 1217; pl. cas. obl. —-än 298.16. — SW development < *pari-aujah-, v. ož; M Prs pyrwz; MPrth prywž, prywg, prywz?n ‘victory’; Paz. perož, NP peroz.
3126:peroz-kar
3784:to [LK; tw 5113], with -e: tē-c [LK-c], toy-ic [LK-yc], pers. pron. 2nd p. sg., cas. rect. and eas. obl., thou, thee, thy: l. subj. passim; emphasizing the subj. 2nd p. sg. inherent in the vb.: tē xtēš daneh 41"; nē... to frac yazé, han... é yazét it is not thou that shalt perform my sacrifice 53°; with an imp.: tē pattā- ken giyāk 398; to mà Sav 2019; in nominal sentences together with the copula: tō,- Jāmāsp, danak ... hah 21?3; tō kēhē...? 732. 155-5; but the copula may be missing: tē ham yātūk 22%; hac har dam u dahišn to pātiyāvandtar 331-12; tē peroz u veh patröc 279; to Kai-Xosroi ...? 9917; hé may also be missing in the pret. pass. having tē as its subj.: tē x"atà4 i
```


## [2026-09-05T05:27:02.023Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} /péróz \\[pylwe/{print \"NYB leaf(awk)=\"NR}' NYB_vol2_glossary.txt; awk 'BEGIN{RS=\"\\f\"} /wanafšag \\[zvnpšk/{print \"PHD leaf(awk)=\"NR}' PHD.txt; awk 'BEGIN{RS=\"\\f\"} /Uvaa?xStra- sb\\./{print \"KNT leaf(awk)=\"NR}' KNT.txt; awk 'BEGIN{RS=\"\\f\"} /231\\. Np\\./{print \"HUB leaf(awk)=\"NR}' HUB.txt",
 "description": "Compute leaves for NYB, PHD, KNT, HUB hits"
}
```


### [2026-09-05T05:27:04.323Z] TOOL RESULT

```
NYB leaf(awk)=177
PHD leaf(awk)=113
HUB leaf(awk)=42
```


## [2026-09-05T05:27:11.874Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==177 {print substr($0,1,300)}' NYB_vol2_glossary.txt; echo \"=== KNT leaf ===\"; awk 'BEGIN{RS=\"\\f\"} /UvaaStra- sb|Uvaa?[Sš]tra- sb|Cyaxares., former King/{print NR; print substr($0,1,200)}' KNT.txt",
 "description": "Check NYB leaf 177 content and KNT leaf"
}
```


### [2026-09-05T05:27:13.489Z] TOOL RESULT

```
= mà šav o yātūkān, cē-t nē hend bēšazanī- tar, bē apāc 6 xanak šav, dast andar mal pat rógn % gāv i apar ātaxš burt, hésm-ic bod vitāp pat x"ēš-tan zahak ké-t pat aš- kamb ‘do not go to the sorcerers, for they cannot heel thee, but go back home, rub thy hand with ox-tallow 
=== KNT leaf ===
200
 by Hz, ApI 71-2).
ufraSa- ufrasta- adj. ‘well punished": u- ‘well’ + pte. fraSta- or frasta- (893) ‘questioned, investi- gated? to root fraó-: pIE *su-prekto- (§33, 75, $242.II. — ufrasia
```


## [2026-09-05T05:27:19.200Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=198 && NR<=201 {print \"--- leaf \"NR\" ---\"; print substr($0,1,400); print \"....TAIL....\"; print substr($0,length($0)-300)}' KNT.txt",
 "description": "Inspect KNT leaves 198-201 for page numbers"
}
```


### [2026-09-05T05:27:20.834Z] TOOL RESULT

```
--- leaf 198 ---
�; 4.33; DPe 7; DNa 16; DSe 15; DSm 5°; XPh 14. ima apf. DB 1.21; D$g 3°.
ima nsn. DB 1.27, 72; 2.01; 3.10, 20, 58, 76; 4.1, 9, 40, 49, 59; 5.2; DPh 4; ОМ 32; DSf 22; DH 3. ima asn. DB 1.25 bis, 26, 68; 444; DNb If; DSf 10; DS} 2°, 5°; ХРе 10f; XPd 16; XSa 1; Х8е 3°; XV 20; А:Ра 19°; D'Sb3?, 4°. imá apn. DB 432. imaibiš ipn. DNb 48.
Imaniš- sb. ‘Imanish’, name assumed by 
....TAIL....
1°. Uvjiyaibis ipm. DB 5.10,
ula (for шй, $36.I) conj. ‘and’ (52911-00): Av. ula, Skt. ш, Gk. Hom. -úre ‘like’, pIE *ute (hardly both -@ and - in Aryan, despite Mt. MSLP 19.57-8, MB Gr. 5151). Correlative with preceding -сӣ, DB 1.66f (cf. Gk. тё xai); ша... шб ‘both ... and’ 
--- leaf 199 ---
DB 1.34f, 41, 461; 2.74, 88f; 5.19f, 35; DNb 30, 37, 40f, 43, 45; XPf 19f; XPh BAL.
щй AsH 13; DB 1.34 bis, 34f, 41 ter, 46 bis, 47, 57, 67, 77, 85; 2.3, 4, 18, 74 ter, 77, 81f, 87, 88, 89, 92; 3.30, 47, 48, 50, 58, 74, 77 (written ud, §52. VI), 88, 90, 91; 4.7, 56, 61, 62, 75 bis, 79, 89, 91 bis; 5.11, 12, 19, 20°, 28°, 31, 35 bis; DPd 15; DPe 18, 14; DNa 53; DNb 3f, 26, 27, 28, 30 bis, 37 b
....TAIL....
RSIAN
Elam. t-ip-ra-tu-i8, Akk. purattu, Gk. Еўфрат
(§75.V, §76.V, §166, $166.II). Etymology un. |
certain, probably a popular etymologizing in OP of a local non-Iranian name, cf. Bthl. AiW 1830; Fick, ВВ 24.310; Justi, ТЕА 17.116; Tm. Lex. 77, Ufrätwā ism. DB 1.92 (not gen., as taken
--- leaf 200 ---
 by Hz, ApI 71-2).
ufraSa- ufrasta- adj. ‘well punished": u- ‘well’ + pte. fraSta- or frasta- (893) ‘questioned, investi- gated? to root fraó-: pIE *su-prekto- (§33, 75, $242.II. — ufrasiam asm. DB 1.22, 4.66f; ufra&lam DB 438. ufrasa-diy apm. DB 4.69 (JAOS 35.351-2, ef. Bv. Gr. $845; not loc. ufrastë + prep. айту, as taken by ВШ. IF 12.110, A1W 60-1, Mt. Gr. $818).
uba- adj. �
....TAIL....
Elam. ren-
177
derings. So KT 9; Tm. Lex. 78; Wb. KIA 17 with note; Hz. BSOS 8.589-97 and Ар! 216-9; W. Hinz, Altpers. Wortschatz 141. Not to be taken with W. Schulze, РАЖ 1912.685-703, 1918.331- 2, as ‘by a natural death’, citing semantic par- allels in other languages; who is followed by M
--- leaf 201 ---
B Gr. $144, §286, $298 (Bv. takes uvd- as instr. and not vriddhied), and by H. H. Schacder, Nachrich- ten d. Ak. d. Wiss. in Gottingen, phil.-hist. Kl. 19046-7.24-30. wdmarsiyus nsm. DB 143.
Uvárazmi- sb. ‘Chorasmia’, a province of the Persian Empire: Elam. ma-ra-18-mi-18, Akk. þu- ma-ri-iz-ma-’, Gk. Xwpaspin, Av. asf. z'airizom. From u- ‘good’ + vāra- ‘0° (8126, 5148.111), + ami-
....TAIL....
in’: Av. kaofa-, Phl. kof,
NPers. köh ($75.IT, $106). See also Akaufactya-. kaufa nsm. DB 1.37; 3.44; DSf 31.
OLD PERSIAN
ka"ta- pte. as sb. (8276. TII) ‘excavation’: pAr, « 7 с *knta-, to 'kan-, with restored n ($242.11) agin с Samar-kand, wherein -kand has been transferred from the ditch
```


## [2026-09-05T05:27:39.722Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==177 {print}' NYB_vol2_glossary.txt | grep -n -o '1[5-7][0-9]' | head; echo \"--- raw around 3119 ---\"; sed -n '3100,3130p' NYB_vol2_glossary.txt | cut -c1-200",
 "description": "Find Nyberg page number near pērōz"
}
```


### [2026-09-05T05:27:41.263Z] TOOL RESULT

```
12:151
13:160
13:171
--- raw around 3119 ---
patvast-ax"éh [ptwst' ’hwyh] the quality of having united minds, concord, unanim- ity 10615. — V.s. v. ax".
Pät-xösröi [p'thwslwd'] n. pr. 2214. 239. 24°. — Called the brother of Vištasp; the name could mean ‘Protector (pdt < pātā nom. of *pätar-, v. pātan) is Khosroi'; Justi NB 246a, thought i
patx"ar [pthwl] *pasture 42??. — < *pati- gugra-, v. xtartan and ef àx*ar.
paty'ak (inser.) [pty?k] = paitäk, q. v.
*päyam- [*p’ym-] pres. "to consume: frac ... pat gah *pāyamēš(y) (opt.) thou shalt *consume it (the roasted meat) on the spot 44” (divine order), cf the con- tinuation 1. 9-10: apt-š etön ka
www .parsianjoman.org | col ak,
payam-
160
péróz-kar
must go back to *pati-yam- ‘to take hold of’, from Av. (1262sg.) yam-, chiefly with preverbs. I find *pāyam as a v. n. in two passages: 1. DkM 285 aköman ... menisn päyam ‘A. holding Mind in 
pazzāmēnītan [pz’mynytn'] to cause to ripen, to mature 88°. — Caus, of pazzdm-. v. next w.
pazzāmišn ripening, maturing 89%, — pazzüm- < *pati-žāmaya-, caus. of pati + Av. (493 sqq.) gam-; Verbum 190 sq.
pazditan. [pzdytn'] to blow, to play: nač (v. s. v. nād) pazdēnd they play the flute 209. — MPrs n’ypzd ‘flute-player’ (A-H II, BBB). Seems to be another vb. than Av. (884 sq.) pazdaya- ‘
pazd6k [pzdwk'] a noxious insect 581. — Av. (885) pazdu-; cf NP pazdak ‘weevil’.
pécitak [pycytk'] distracted, crazy 802°. — Properly ‘twisted’, NP pécidan ‘to twist, to distort, to wreathe, to wind in a serpentine form’. I maintain my etymo- logy proposed in MO XXV, 
tica ‘inversely’ (from *paityank- paitik-) + citan (g. v.): *paticä-citanai ‘to lay a th. (e. g. a rope) together in such a way that it returns to its starting-point a) on the same level: to fo
pēm [pym] milk 423-13.25, 431, 533,543-11, _ Av. (817) pačman-; Paz. pim.
pērāmēn [pyl'mwn', pylmwn'] 1. adv. all about 3923, 935, 9623. 9817, 2. prep. round about, with the izafat, 119. 8722, 8912; referring back to an encl. pron.: 7 déh 4-4 ~ nisast hend 471°, api-š
*pērāvanihīt [pyr'wnyhyt] pass. pt. *stirred up: apt-š hamäk damik... — kart and he (the Wind) stirred up the whole soil 3316-17, — Reading hypothetical. I derive it from pari + d + van-, OP 
péróz [pylwe'] victorious, victor 2719. 1217; pl. cas. obl. —-än 298.16. — SW development < *pari-aujah-, v. ož; M Prs pyrwz; MPrth prywž, prywg, prywz?n ‘victory’; Paz. perož, NP peroz.
Peröz a son of Šahpuhr 11515, cf Cat. 81 sq. — In KZŠPrth 1. 21, we find twice the strange spelling prgwz of this name = Prs prywzy l. 26 (Gr. v. II3potov and Ilnpe6).
Perözän patron. of Pērēz 1160, 11712,
peröz-ävar [~-’wwl] bringing victory 2718, - V. ävurtan.
pérózéh victory 27. 2915, 6113, 781,
péróz-kar [~-kl], pērēz-gar [—-gl] work- ing victory, of the sacred Fire 925. 1223;
www.parsianjoman.org | col wok
peroz-kar
of the most sacred formula 58?; vietorious 518,
péróz-karéh, péróz- garóh. victoriousness 344-5, 5816, 11918,
1411.15.
pēsīt [pysyt'] adorned 362. 10819, 1114. — Derived from Av. (818) paésa- ‘ornament’, from Av. (817) paés-, OP pais-, v. nipištan.
```


## [2026-09-05T05:27:48.089Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'بنفشه' BQT_v1_pages.txt | head -20; echo \"=== page tags near ===\"; grep -c 'pdf page' BQT_v1_pages.txt",
 "description": "Grep Borhan-e Qate vol1 for banafshe"
}
```


### [2026-09-05T05:27:48.154Z] TOOL RESULT

```
21100:بنفشه ۱ هم اول و کر اول هردوآمده
21137:» باهش - بفتح اول و دوم . رنك کبود مانند رنك بنفشه - نوعی از جواهر کریمه
25204:زلف بنفشه خمید برغیب جوببار.
=== page tags near ===
0
```


## [2026-09-05T05:27:50.276Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '21085,21150p' BQT_v1_pages.txt",
 "description": "Read Borhan banafshe entry"
}
```


### [2026-09-05T05:27:50.335Z] TOOL RESULT

```
۴ تاواک دصق ۵ بر( :
ست * فرهنك دساتیر ۲۳۹ >. ۷ - فرحنك
4 رله : نشاختن . ۰- رگ : تین -
3 حس مشتر
چ جل - رك : برافوش .
شه در صفحه ۳۶۸مصفر بن است ۳ که حبة الخترا و چنلافوج .
باشد , و آن بیثثر در کوهها و جنگلها حاسل
۰ میگردد -ونوعی از قماش زمین اطلس بودکه
برآن کلهای زربفت باشد و کلها ونشانها رائیز
گویند که برروی مهوشان از خوردن شراب بهم
میرسد باعرق برپیشانی ابشان شیندب وبشم اول
مصفر بنه است یعنی درخت کوچك ۴ - وبمعنی
کشان واثرهم هست چنانکه گوند «از فلانی بااز
فلانه چیز بنك نمانده است » اراده آن باشد که
نشان واثر تمانده است - وینم اول وسکون ثانی
بنفشه ۱ هم اول و کر اول هردوآمده
است ۰ گلی باشد ممروف
وطبیعت آن سرد وتراست
دردوم وسوم ؛ وممرب آن
بنفسج باشد- ونام کیاهی‌هم
هست که ات روبث.
بفشه گون‌طار م-
۲۳۳
بشثه گون مهد کنابه از آسان
وزهین هردو باشد .
بنقه - فح اول وفاف و سکون نون ؛
نوعی از غله باشد مانتد عدی » و قوت و منغعت
آهم مانثد عدس است .
ماش « بننح اول وئانی وسکون کاف »
وثالث » پوست بیخ ام غیلان باشد. وآن درختی
است صحرانی درولات عصمر ۰
بن کار خوددن.- منم اول رکس:
نانی, کنابه ازاندبشه نمودن بجهت عاقبت وانتها
ویایان کار باشد .3۶
۱ -یهلوی۷20۵)502او نوالام». هرن نرابفتح و کسروض‌اول خوانده«اسفا۷:۱ص۲4»,
طبری ۰۷۵1۱1502 مازندرانی کنونی ۷60۵۵56 « واژه نامه ۸۱۰ کیلکی ۵2086512. یره
بننشه ۷۱۵۱2۳1665 دارای کل های نامنظم و مهمیزدار است و دو جنس دارد : بنفشة عمطر
212 ۷۱۵۱۵ که کل آن بمنوان ملین بکار رود و دیگر بنفشة سه رنك با بنفثةٌ فرنگی
65 کهیرای زشت کاشته میشود. « گل گلاب ۲۱۲. ۴ - رك: بن. ۴ - رل: بنه.
بفبه در صفحهٌ ۳۰۹
بقّه از صفحٌ ۳۰۷
۵ ند گی _ بفتح‌اول‌وسوم, از:بنده (بند گه) + ی(حاصل‌مصدد) . په‌لوی 002811 قط
«اسفا ۱ : ۱ ص ۲۵۷ ؛ بنده و غلام بودن - اطاعت و انقیاد . رلك : بنده .
۵ بنده - بقتح اول وسوم» پهلوی معط «منای 6۲۹۹ «یونکره 6۷ یارسی باستان
2 هبد«بار تولمه »٩۲4‏ ازممدر بستن («. م), جمع‌آن بندگان» در پهلوی 3808127
«یب رکه ۳۲»؛ عبده غلام. مقابل آزاد . رك : داثرغالمعارف اسلام .
۵ بنديی - رد : منف ضم اول. (س۳۰۵ح).
۵ بر - رك : بنذ بنم اول . (سه ۳۰ج) ِ
۵ بترئی - بکر اول. ازفرانسه ۳6۵2186 ازابتالبابی 0602108 (روغن بان), کلم
بان از عربی بلغات ارویایی نقل شد. . درسال ۱۸۲۵ ماده ای که اکنون بنزین مینتاميم توسط
علمای شیمی کشف گردید «تقس». ماد شیمیابی مزبور برای حر کت اتومبیل وهواییسا و موتور
کارخانه‌ها نیز با کردن پارچه‌ها ازچربی وغیره بکار روده
» باهش - بفتح اول و دوم . رنك کبود مانند رنك بنفشه - نوعی از جواهر کریمه
6 نی ود.بنگان - بکس اول وکاف فارسی بالف
کشید بروزن فنجان . طاسی باشد که دهقادان
بنآنرا سوزاخ کرده باشند وآترا درطفار پرآیی
گذار ند بمقدار زمانی که برشود؛ آب‌از رودخائه
با برغ باچشمه پزولمت: هرماك رود ربستی رایفه
و دو و بضی را چهار و پنج آنجه حفرد شده
باشد - ومطلق پپاله را نیز گویند, ومعرب آن
فنجان است۱ .
بنگاه » نم اول و کاف ضارسی بالف
کشیده بروز نکمراء» منزلومعان ۴ وجابی که
نقدوجنس درآ نجا نهند.
بنکر آن - نم اول وسکون انی وفتح
اش وت یل پا کنیه و نون زد
```


## [2026-09-05T05:28:17.759Z] TOOL CALL #40: Bash

```json
{
 "command": "timeout 300 python3 tools/ref_page.py BQT:308 2>&1 | head -60",
 "description": "Fetch Borhan page 308"
}
```


### [2026-09-05T05:28:19.694Z] TOOL RESULT

```
no scan of BQT covers printed page 308 (see 'scans' in refs_online.json)
```


## [2026-09-05T05:28:24.248Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=20800 && NR<=21400 && /^[[:space:]]*[۰-۹]{2,4}[[:space:]]*$/ {print NR\": \"$0}' BQT_v1_pages.txt",
 "description": "Find page markers near banafshe in BQT v1"
}
```


### [2026-09-05T05:28:25.709Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T05:28:29.019Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} /بنفشه ۱ هم اول/{print \"leaf(awk)=\"NR}' BQT_v1_pages.txt; grep -c $'\\f' BQT_v1_pages.txt; head -3 BQT_v1_pages.txt",
 "description": "Find leaf of banafshe in BQT v1"
}
```


### [2026-09-05T05:28:30.633Z] TOOL RESULT

```
leaf(awk)=529
766
۱ ۵ ۱! ۱
7 موم ۳ لام
م ۱ 0 و طق صفرررنیاعدریرماروی
```


## [2026-09-05T05:28:43.841Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY banafshe/piruz ===\"; grep -n 'بنفشه\\|پیروز' incoming/ARY/ARY_pages.txt | head -20; echo \"=== ARY latin index ===\"; grep -n -i 'AUEG\\|AUG\\|banafs\\|piruz\\|WAHS' incoming/ARY/ARY_latin_index_pages.txt | head -20",
 "description": "Grep Aryanpur"
}
```


### [2026-09-05T05:28:43.914Z] TOOL RESULT

```
=== ARY banafshe/piruz ===
922:پیروزی. ۳- بکار بردن نماد حیوانات وحشی (به ویژه گرگك) بعنوان نشان و عامل الهامبخش. ۴-
14023:چم این واژه در آلبانی؛ پیروزی. :
=== ARY latin index ===
539:Oy SAAS Aa|) Atel ey! (AUGUST SCHLEICHER, 1821-1868) 943 oF
1505:oy @RIAUGM,” LITHUANIAN) ips ERUCTATION
2145:OBRVA SERBIAN) «ype AUGENBRAVE, ° (GERMAN) st
2757:EHAUG, EAUG (CELTIC) (gS) gh ANCHIEN, AGKBEIN (GREEK) gy
3138:BRU (SERBIAN) «yp BAUGGIA :(OLD SAXON) oy St -
3142:| BARNHART (BRIDGE) 116 PAUGEL, BRUCKE (GERMAN) gust
7070:‘MACKENZIE: (LAUGH) 121 KACHAZZEN
7071:AMINDAROV: (LAUGHING) 247 HOLD ENGLISH) oS JS&\
7702:BARNHART: (DAUGHTER) 252 DOHTA — (OLD SAXON) ef i pS
7704:MACKENZIE: (DAUGHTER) 109 HOLD HIGH GERMAN) oS gis
7706:ONIONS: (DAUGHTER) 245 TOCHTER |" Ru (GERMAN) gait
7707:SKEAT: (DAUGHTER) 155 OLD ENGLISH) op gnlSil
7709:DAUGHTER ENGLISH) gnl&sl
7916:SANSKRIT) xy Suile DRAUGA, DURUGIYA
7919:DRAUGR DURUGH, DEREW- (KURDISH) 2,
8341:DAUG, DADDJAN (GOTHIC) Sa
15141:AUGU, AUGTI (LITHUANIAN) gig AUKSU (TOKHARIAN B) Bs ios
15142:AUDZET, AUGT (LATVIAN) (33) g.95 UKSH, SANSKRIT) oy Suile
15144:AUGINNONS AUKSO, AUXANEIN (GREEK) by
15145:AUGERE, AUGEO. (LATIN) p3Y
```


## [2026-09-05T05:28:45.175Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC aug ===\"; grep -n 'augeō\\|augeo,\\|aug-\\|auksmi\\|augmen' IEC.txt | head -15; echo \"=== KLN waist ===\"; grep -n 'waist,' KLN_1966.txt | head -5",
 "description": "Grep Mann and Klein"
}
```


### [2026-09-05T05:28:45.245Z] TOOL RESULT

```
=== IEC aug ===
57:BoisAcQ, E.: Dictionnaire étymologique de la langue grecque, 1923. Réimpression augmentée d'un index par Helmut Rix, Winter, Heidelberg 1950
799:augmn- ‘growth, height. WP I, 22. Cf. augos, augo, aueg- Lat. augmen; Go. cf. aukan ‘to grow’; OE cf. eacen ‘strong, big? OS ôkan ‘pregnant’; Li. augmuó, -eñs “plant, growth’; OPr. cf. auginnons, pp. ‘reared’. (For LG auken, ooken ‘garret’, see augā)
801:augos, om, ios, io “growth, increase, rein- forcement'. Cf. augó, aueg- Tokh. cf. okar ‘plant; Lat. cf. augmen; OE eaca; ON auki beside aukan 'increase'; Latv. augs ‘growth, plant? beside audze ‘plantation; generation’. (Av. aogō, n. ‘help and Skt. ugráh “powerful? may belong here, but seem to be contradicted by Skt. ójas: Av. aojo, -áh- ‘power’ (*& or a secondary *g?) beside Av. aogo, -áh- *help")
871:aueKs- (oueKs-, auKs-, ouKs-) ‘grow; growth’. Cf. aug- (?) or aue, eKs (?) Skt. vaks-, uksami, pf. vaváksga; Oss. as, asä ‘growth’; Gk. aéxo, aüxo; Alb. cf. vjeshtë ('autumn': Skt. vaksáthah: Gk. aektós); OCS ovostí “fruit, tree’, vostije ‘fruit; R òvošči ‘vegetables’; Li. veën -éti ‘thrive? beside vesiüs ‘thriving
3503:e-iudh- (radical: iudh- ‘go, move? with relic of augment). See iudh- OE éode ‘went’; ME yode, yede, id.; OCz. jid, 3s. jide, id.
3914:gaug- “cough, caw, croon' Mod. Gk. gaugízo ‘cough’; isophonic w. Big. gügam ‘coo, croon’, but this is prob. onomat. Cf. *güg- in MHG küchen ‘breathe’; Ger. kauchen & keuchen ‘pant’; OE (*gug-) in coh- hettan ‘cough’; OCz. (ambig.) cf. huhlu, ati (howl, whine, screech’. Mod. ‘mutter’)
4603:ghaughor- (roam, wander; wandering’. Cf. ghaug-, ghaugh- Ir. guagaire *wanderer, tramp'; MHG gougern, v. ‘roam’. (Isophonic: Li. gaügaras “peak, sum- mit")
4605:ghaugho, io ‘rave, bluster, play the fool. (All forms ambig.) Gk. cf. kaükhos, kaükhe ‘boast; boasting’; kaukháomai, denom., id.; Ir. (ambig.) guag (folly'. Cf. ghaug-); OHG cf. gougulari *jugg- ler; MHG gougeln “play the fool, play pranks'; gougel *witchcraft beside (ambig.) gougern (Crove, See ghaughor-); Latv. (ambig.) gau£Zu, gauzt ‘rave, twaddle’
6867:kaug- “shout”, etc.; kauk- ‘raucous bird’, see kāuk-
7808:krop ‘torture’; R kropát, v. ‘botch, mangle? kraps- ‘grab, snatch; rapacious; grab, sei- zure’ Br. krafa ‘seize, snatch; scratch, engrave’; kraf ‘seizure’; kraf, m. ‘stylus’: kraf, krav ‘stitch’; W craff ‘quick, keen; secure’; m. pl. -au ‘clasp, cramp’; craffu, v. ‘secure, grip’; Cor. crafa, v. ‘grip’; crāf, adj. ‘tenacious’; s. pl. crafow "basting-stitch"; cf. crefny, adj. ‘grasping, gree- dy’; OE hrespan ‘strip, despoil’; hresp ‘spolia- tion’ krās- (?) ‘glory, praise’ ON hrósa, v. ‘praise’; hrósan, f. ‘praise; boast- ing’; hræsni, f. id.; mod. Icel. hrós, n. ‘praise’; OCS krasa ‘beauty’ (and com. Sl.); Latv. cf. krāšns 'splendid'. See Supt. K : krās- (krast-, see karst-). Variant in W cras ‘toasted, parched, arid’; Br. kraz, id. krateið ‘overpower’. See kratos Gk. kratéo ‘rule’; OCS krostọ, krotiti (tame' and com. Sl.) kratos, is, us “strong; strength, power, force’. WP I, 354 Skt. krátuh “power, will, ability’; Av xratus ‘wisdom’; Ober xraQu-, id.; Gk. kratüs *power- ful”; krátos, n. ‘power’; W crad, craid, m. (“vig- our, force’, fr. *kratos, *kratis); OHG hrad ‘swift; OE hrad “swift, active; ON hraór, id.; OCS cf. krotükü ('tame', lit. overpower- ed"). Isophonic: Li. kratüs (rough, uneven’ krátos, à, is 'enclosure, envelope” W crawd “coating, surface’; OE hréóa 'goat- skin cover, mantle’; cf. hroó-girela ‘crown’; Li. krótai, krótos, mfpl. "lattice, grille’; Latv. krats ‘cage, prison’. (W and OE ambig.) kratsos, ios (?) Lat. crassus ‘fat, gross’; ON hress “hale, hear- ty’; hressa, Lat v. ‘cheer’ (kraug-, variant of krauk-, q. v.). (WP I, 417, 477 & II, 573) Hes. kraugós ‘woodpecker’; Gk. kraugé ‘croak, caw’ krauk- ‘caw, croak; crow, raven’. (Variant: krauk-) EMAIb. krak, mod. krrak ‘a bird of crow type’; OE hrēa (Crumble in the bowels’? Cf. hream ‘uproar’, fr. *kraukmo-?); Pol. Ukr. kruk ‘raven’; Latv. kraukjs ‘rook’ beside krauklis
9450:lakús, lakuos ‘lake, pool, puddle, pond’. WP II, 380 Gk. lákkos, m. ‘pit, puddle, tank’; Lat. lacus, gs. -üs, id.; Olr. lac, Ir. lag, m. *water-hole, pooľ beside (augmentative) lagán ‘puddle’; Br. Cor. cf. lagen, pl. lagennu, lagennow, f. ‘marsh, pond’; OE lagu, m. n. (lake, flood’; pl. ‘surface of the sea’); OS cf. lagu-stróm ‘waters’; ON lọgr, gs. lagar, ds legi, m. ‘sea, water; OCS loky, gs loküve, m. ‘puddle’; lokva, f. ‘rain’; Blg. lókva, Srb. lókva ‘puddle’
11800:Per. nàz ‘flirtation, flattery’; cf. nazuk ‘flashy’; nàzidan, inf. ‘flirt’; Gk. cf. nógala, npl. ‘snacks’ (if not < *no, eno, and *&olok?); OLat. nogae, cpds. naug-, Class. nügae 'trifles'; Fris. noekje “darling, favourite" beside noekerje, v. ‘cajole, coax’; (but G Nucke, Nücke, f. *whim' is fr. MLG nucke, id., and Du. nuk, f. id. is appa- rently fr. LG); R cf. za-nóza, f. ‘irritant; irri- table person' (?); Li. (?) nuoZ-mas, -mus, adj.
15350:sila, is “strength; strong”. Cf. seil- (3) Lat. cf. exilis, adj. (lean, paltry’, if for *ex- sīlis) beside auxilium, n. ('aid', if for *aug-sil-); OCS and com. SI. sila, f. ‘strength’
15496:harr, herr, v. *weed'; Old Lat. scarreo, ere, v. ‘be rough'; G scharren, v. ‘scratch, root, scrab- ble, shuffle, hawk, cough'; Scharre, f. ‘rasp; raspings'; ON skarr, n. ‘skirmish’ beside skars, skass, n. ‘ogress’. (NB. A form *skors- in im- plied in Arm. xorem, v. (dig). Cf. also Norw. skarre, v. (‘burr the ‘r as in Bergen dialect) (skat- (1) jump, dash, spout'. See sKat-) skat- (2) “hit, strike, touch'. Cf. skot-. (Alb. ambig.) Alb. has, v. aor: hasa “hit, touch, meet: MIr. & Ir. scathaim, scaithim, v. “cut, lop, destroy” skaudhos (ksaudhos?) ‘miserable, poor, lean, abject'. Variants in OPer. & Arm. Ober. cf. skauðis, adj. ‘mean, poor, feeble’; Arm. xawt, i-st. (ilU, fr. a type *skaustis, but cf. Ober, fr. *skauth-); ON skauó, f. *cow- ard”; Du. cf. schooien, v. (cringe, beg’, if fx. *skaudh- in this sense); Blg. skuden, f: skud- na, adj. “poor, wretched'; cf. Ukr. pa-skuda, s. ‘lecher’; Li. skaudüs, adj. ‘painful, offen- sive; man skauda “it aches’; skaudZiü, inf: skaüsti, v. ‘offend’; Latv. cf. skaudrs, adj. ‘keen, painful. (Variant of uncertain phono- logy in Srb. hud ‘bad’; Cz. chudý ‘poor’, dial: Jean’, and R xudój ‘bad; ill; lean’; xudà ‘blame, abuse’, fr. *ksaudh-, *qusoudh- or sim. Cf. Oss. cawd "bad fr. a variant *sKaudh-?) skaug- Sw. skóka, f. ‘whore’; Li. skaugüs, adj. *miser- ly’; skáugis, ‘miser’; Latv. skaugis, m. ‘envious person’ but cf. skaudigs ('envious'. See above) (skaul-, see ksaul-. Thus only in W ysgawl, adj. ‘vehement, dashing’) skaupos, å ‘tuft, bunch, sheaf Lat. (dial.) scopae, fpl. ‘broom’; scopo, are, v. (sweep. WH & EM untenable); (W cf. ysgaw, Br. skað, Cor. scaw.'elder? but the semantic link is obscure); MHG schoup, gs: schoubes, sm., Du. schoof, f., OE sceaf, m., ON skauf, n. ‘sheaf, bundle’; LG Schauw, wf. “flock, swarm’; cf. ON sküfr, m. ('tuft, topknot,, fr. *sküp- or *skübh-); Big. cf. (dial.) skupü, m. “collection, heap', sküpom ('to- gether, unless from a dialect of Srb. type, *su- and *komp-. Thus Mladenov. Isophonic: OCS pro-skupü *depraver, profaner’; -sku- pístvo 'depravity')
17313:-stos (-stus) (2) adjective-formant extending a símplex Per. baste (“bound?: bhendh-); Gk. gnostós Cknown": £ndu-); Alb. i angshtë (^wild, rug- ged": angh- or angh-); i lashtë ('early': lad-); Lat. angustus (‘narrow’: angh- or angh-); au- gustus (high': aug); MHG cf. luste (‘plea- sant’: lubh-); OCS pustü (‘empty’: paus-); OPr. pausto, id.; Gk. cf. ápaustos, adj. (“un- ceasing’); Li. añkštas (‘narrow’: ang- or angh-); áukštas (“high?: aug-)
=== KLN waist ===
9914:cummerbund,  n.,  waistband  (Anglo-Ind.)  — Hind.- Pers.  kamar-band,  fr.  Pers.  kamar,  ‘waist,  loins’, and  band,  ‘band,  bandage'.  See  bind  and  cp. band.
```


## [2026-09-05T05:28:54.225Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'waist' KLN_1966.txt | grep -i 'n\\.,\\|ME\\|wahs' | head -5; echo \"=== SKT waist ===\"; grep -n 'waist' SKT.txt | head -5; echo \"=== SKT august/auction ===\"; grep -n '^August\\|^Auction\\|augeo' SKT.txt | head -8",
 "description": "Grep Klein and Skeat for waist"
}
```


### [2026-09-05T05:28:54.328Z] TOOL RESULT

```
7273:chatelain,  n.,  castellan.  —  F.  See  castellan, chatelaine,  n.,  the  mistress  of  a  castle;  key  chain worn  at  the  waist  by  women.  —  F.,  fern,  of chatelain.  See  prec.  word, chati,  n.,  a  South  American  tiger  cat.  —  Of  South American  Indian  origin.
9914:cummerbund,  n.,  waistband  (Anglo-Ind.)  — Hind.- Pers.  kamar-band,  fr.  Pers.  kamar,  ‘waist,  loins’, and  band,  ‘band,  bandage'.  See  bind  and  cp. band.
16144:L.  Aegidius,  fr.  aegis.  See  aegis, gilet,  n.,  a  waistcoat.  —  F.,  fr.  Sp.  jileco,  gileco (the  modern  Sp.  form  is  chaleco),  fr.  Algerian Arab,  jaleco,  ‘coat  of  Christians  in  Moorish captivity’,  ult.  fr.  Turk,  yelek.
20095:ing’,  from  the  stem  of  dzara,  azzara,  ‘he  girded, encompassed’,  rel.  to  Heb.  dzar,  ‘he  girded’, ezSr,  ‘waistcloth,  girdle’, izard,  n.,  chamois  inhabiting  the  Pyrenees.  —  F. isard,  of  Basque  origin;  cp.  Basque  izar,  ‘star; white  spot  on  the  forehead’;  cp.  also  Berber ichri,  of  s.m.,  which  is  a  Basque  loan  word.  The spelling  with  d  is  prob.  due  to  a  confusion  with sufF.  -ard.  *5
35110:Siamese  twins,  —  So  called  from  the  Siamese twins  Eng  and  Chang  (1811-74).  —  They  were united  at  the  waist  by  a  band  of  flesh, sib,  n.  and  adj.  —  ME.,  fr.  OE.  sibb,  rel.  to  OS. sibbia,  OFris.,  MDu.  sibbe,  OHG.  sippa,  MHG., G.  sippe,  Goth,  sibja,  ‘kin,  kindred’,  and  cogn. with  Russ,  sob,  ‘character,  individuality’,  OSlav, o-sob-a,  ‘person’,  sobistvo,  ‘character,  indivi¬ duality’,  OPruss.  subs,  ‘self’.  All  these  words derive  fr.  I.-E.  base  *s(w)e-bh~,  ‘of  the  same kind’,  which  is  a  -Mi-enlargement  of  the  reflex¬ ive  pron.  base  *se-,  ‘self’.  See  sui  and  cp. gossip.  Cp.  also  Sabine,  Samnite.
=== SKT waist ===
7603:girth.  (Scand.)  M.  E.  prth.  -  Icel. ^'^rS,  a  girdle,  girth;  gt'^'^%  g"lh  round  the waist :  l3an.^'<i}i-J.^(toth.  gainia,  a  girdle.
21335:waits,  a  dance.  (G.1  Short  for  G. waJur,  a  waltz  (with  s  sounded  as  //).• G.  waistM,  to  roll,  revolve  ;  sec  above.
=== SKT august/auction ===
1119:Auction-  (L.)  L.  auciifffifm,  ace.  of auctio,  a  sale  by  auction,  lit.  •  an  increase/ because  the  sale  is  to  the  highest  bidder.— L.  au£tus,  pp.  of  augert,  to  IncreaM.  See Ske.
```


## [2026-09-05T05:28:54.938Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15130,15160p' incoming/ARY/ARY_latin_index_pages.txt",
 "description": "Read ARY latin index around aug"
}
```


### [2026-09-05T05:28:55.003Z] TOOL RESULT

```
[pdf page 518]
4
‘
i
ONAL Cees CRIS UT Cosy Eg) OLE ytd
VAXSH, VAXSH, VAXSHIDAN
WAX ENGLISH) AS} UKHSHYEITI, HAVESTAN) glans}
VOKSE DANISH) Sails VAKHSHAITI, UXSH-, UXSHYEITI
VAXA SWEDISH) 538 yo (PAHLAVI) (5 shy
VOKSE NORWEGIAN) 1535 3 WAXSHIDAN, WAXSH- WAXSHISHN
WASSEN DUTCH) acta OKS., OKSU- :(TOKHARIAN A) A 5,0
AUGU, AUGTI (LITHUANIAN) gig AUKSU (TOKHARIAN B) Bs ios
AUDZET, AUGT (LATVIAN) (33) g.95 UKSH, SANSKRIT) oy Suile
HOLD PRUSSIAN) eS gus 4 UKSHATI, VAKSHATI, VAKSH, UKS-
AUGINNONS AUKSO, AUXANEIN (GREEK) by
AUGERE, AUGEO. (LATIN) p3Y
REFERENCES oetKy AUGMENTER FRENCH) el 3
POKORNY = SSSSCS*~*~«SS AUMENTAR (SPANISH) lili
BARNHART: (WAX) 1223 AUMENTARE HITALIAN) gldiy\
‘MACKENZIE: AUMENTAR — (PORTUGUESE) Js x
(GROW) 117, (WAX) 139, (GROWTH) WAHSJAN GOTHIC) 83 F
7 (OLD SCANDINAVIAN) 4S cs.chus!
BUCK: (GROW) 876.877 VAXA
ONIONS: (WAX) 995 HOLD HIGH GERMAN) nS glJT
SKEAT: (WAX) 704 WAHSEN
rat ebony WACHSEN (GERMAN) slg aed
rriry grrr slasias aabicadd WEAXAN (QLDLENGLISH) oS pos
NAVARAZ ——{AFGHANI) (-4) gli! VARTAK PAHLAVI) 5 3
VARTIKA SANSKRIT) 2 Sule VARDKA HOSSETIC) ou 9\
ORTUX GREEK) gly VERDI, HAVARDE (KURDISH) (53,5
GVARDAG HBALUCHI) > ge
```


## [2026-09-05T05:29:06.197Z] TOOL CALL #47: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-05T05:29:06.205Z] TOOL RESULT

```


```


## [2026-09-05T05:29:08.564Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'waist' KLN_1971.txt | head -8; echo \"=== SKT waist entry ===\"; grep -n -i '^Waist\\|Waist\\.' SKT.txt | head -5; echo \"=== FSD ===\"; grep -n -i 'waist,  n' FSD_vol4.txt | head -3",
 "description": "Grep Klein 1971 and Skeat for waist"
}
```


### [2026-09-05T05:29:08.668Z] TOOL RESULT

```
44443:worn at the waist by women. — F„ fem. of 
61561:cummerbund, n., waistband {Anglo-Ind.) — Hind.- 
61562:Pers. kamar-band, fr. Pers. kamar, ‘waist, loins’, 
102608:gilet, n., a waistcoat. — F., fr. Sp. jileco, gileco 
127857:ezdr, ‘waistcloth, girdle*. 
221386:united at the waist by a band of flesh. 
264461:waist, n. — ME. wast , ‘waist*, lit. ‘growth* (the 
264462:waist being regarded as the part where the body 
=== SKT waist entry ===
=== FSD ===
```


## [2026-09-05T05:29:12.001Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '264458,264475p' KLN_1971.txt; echo \"=== KLN 1966 same ===\"; grep -n \"waist,  n\\.\\|wast\\b\" KLN_1966.txt | head -5",
 "description": "Read Klein waist entry"
}
```


### [2026-09-05T05:29:12.090Z] TOOL RESULT

```
See prec. word and shut. 

Derivatives: wainscot, tr. v., wainscot(t)-ing, n. 
waist, n. — ME. wast , ‘waist*, lit. ‘growth* (the 
waist being regarded as the part where the body 



is best developed), rel. to OE. wxstm, ON. voxtr , 
Swed. vdxt, OHG. wahst, ‘growth, increase’, 
Goth, wahst us, ‘stature’, lit. ‘grow.th’, and to 
OE. weahsan, weaxan, ‘to grow’. See wax, ‘to 
grow*. 

Derivative: waist-ed , adj. 
wait, intr. and tr. v. — ME. waiten, ‘to watch’, fr. 
ONF. waitier , corresponding to OF. guaitier , 
gaitier, ‘to watch* (whence F. guetter, ‘to watch, 
=== KLN 1966 same ===
37966:tabitude,  n.,  emaciation.  —  L.  tabitudo,  ‘a  wast¬ ing  away’,  fr.  tabere.  See  tabes  and  -ude. tablature,  n.,  1)  an  early  name  for  musical  nota¬ tion;  2)  a  tablelike  painting;  3)  a  graphic  de¬ scription.  —  ML.  tabulatura  (whence  also  It.  ta- volatura,  G.  Tabulatur),  fr.  Late  L.  tabulare,  ‘to board,  to  floor’,  fr.  L.  tabula,  ‘plank,  writing tablet’.  See  table,  adj.  suff.  -ate  and  suff.  -lire, table,  n.  —  ME.,  fr.  OF.(= F.),  fr.  L.  tabula, ‘board, plank,  writing  tablet,  picture’  (whence  also  It. tavola,  ‘table’),  rel.  to  Umbr.  tafle,  ‘on  the board’;  of  uncertain  origin.  Cp.  tabellion,  ta¬ bleau,  tablier,  tabula,  tabula  rasa,  entablature, entablement,  taffrail.  Cp.  also  the  first  element in  dolmen.
```


## [2026-09-05T05:29:21.020Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%DB%8C%D8%B1%D9%88%D8%B2",
 "prompt": "Give the full etymology section for the Persian word پیروز (pīrūz) 'victorious' — what Middle Persian, Old Iranian/Avestan forms it is derived from, and any cited sources. Also any mention of فیروز."
}
```


## [2026-09-05T05:29:23.408Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D9%86%D9%81%D8%B4%D9%87",
 "prompt": "Give the full etymology of Persian بنفشه (banafše) 'violet' — Middle Persian form, proposed Old Iranian etymon, and any cited scholarly sources (Hasandust, Horn, Hübschmann). Also any Arabic بنفسج entry."
}
```


### [2026-09-05T05:29:25.872Z] TOOL RESULT

```
# Etymology of پیروز (pīrūz)

Based on the Wiktionary content provided, the etymology section states:

"From Middle Persian 𐭯𐭩𐭫𐭥𐭰 (pērōz, 'victorious')."

The document does not provide information about earlier Old Iranian or Avestan forms, nor does it cite specific academic sources for this etymological derivation.

## Regarding فیروز (firuz)

The page lists **فیروز** (firuz) as an alternative form, but provides no separate etymology or explanation of the relationship between these two spellings.

The Proper Noun section does reference that the name is "from Middle Persian," but no additional etymological details or sources are supplied beyond this basic attribution.
```


### [2026-09-05T05:29:30.137Z] TOOL RESULT

```
# Etymology of Persian بنفشه (banafše)

Based on the Wiktionary entry provided, here's what is documented:

**Middle Persian Form:**
The entry states the word derives "From Middle Persian _wnpšk'_ (wanafšag, 'violet'), of uncertain origin."

**Scholarly Sources Cited:**
The references section includes:

1. **MacKenzie, D. N.** (1971) — "wanafšag" entry in *A Concise Pahlavi Dictionary* (Oxford University Press)

2. **Steingass, Francis Joseph** (1892) — Entry in *A Comprehensive Persian–English Dictionary* (Routledge & K. Paul)

**Important Limitation:**
The entry explicitly notes the origin is "of uncertain origin" and directs readers to the Middle Persian entry for further information, which is not included in this excerpt.

**Regarding Your Questions:**
The provided content does not include:
- A proposed Old Iranian etymon
- References to Hasandust, Horn, or Hübschmann
- An Arabic بنفسج entry

To obtain that additional etymological detail, you would need to consult the full Middle Persian entry or specialized etymological references.
```


## [2026-09-05T05:29:35.805Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/wanaf%C5%A1ag",
 "prompt": "Full etymology of Middle Persian wanafšag 'violet': what origin does Wiktionary give, which sources are cited, and what descendants/borrowings (Arabic بنفسج, Armenian, Syriac) are listed?"
}
```


## [2026-09-05T05:29:36.635Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/p%C4%93r%C5%8Dz",
 "prompt": "Full etymology of Middle Persian pērōz 'victorious': the Proto-Iranian / Old Iranian etymon, Avestan cognates, sources cited, and descendants including New Persian پیروز and Arabic فيروز."
}
```


### [2026-09-05T05:29:37.603Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T05:29:39.258Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-05T05:29:42.743Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%F0%AD%AF%F0%AD%A9%F0%AD%AB%F0%AD%A5%F0%AD%B0",
 "prompt": "This is the Middle Persian entry pērōz. Give the full etymology, cognates, sources cited, and descendants."
}
```


## [2026-09-05T05:29:43.334Z] TOOL CALL #55: WebSearch

```json
{
 "query": "Middle Persian pērōz \"pari-auǰah\" etymology victorious Avestan aojah"
}
```


### [2026-09-05T05:29:44.771Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T05:29:52.838Z] TOOL RESULT

```
Web search results for query: "Middle Persian pērōz "pari-auǰah" etymology victorious Avestan aojah"

Links: [{"title":"Iranic cognates of PIE root *aug- | WordReference Forums","url":"https://forum.wordreference.com/threads/iranic-cognates-of-pie-root-aug.3342730/"},{"title":"پیروز - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D9%BE%DB%8C%D8%B1%D9%88%D8%B2"},{"title":"Persian-Etymology-Charts.pdf","url":"https://parsianjoman.org/wp-content/uploads/2022/12/Persian-Etymology-Charts.pdf"},{"title":"Feroz","url":"https://en.wikipedia.org/wiki/Feroz"},{"title":"Phiroze","url":"https://en.wikipedia.org/wiki/Phiroze"},{"title":"𐭯𐭩𐭫𐭥𐭰 - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%F0%90%AD%AF%F0%90%AD%A9%F0%90%AD%AB%F0%90%AD%A5%F0%90%AD%B0"},{"title":"Verethragna - Wikipedia","url":"https://en.wikipedia.org/wiki/Verethragna"},{"title":"Bahram (name)","url":"https://en.wikipedia.org/wiki/Bahram_(name)"},{"title":"Etymology of Persian پیروز/ پرویز piruz/parviz \"victorious, triumphant\" | WordReference Forums","url":"https://forum.wordreference.com/threads/etymology-of-persian-%D9%BE%DB%8C%D8%B1%D9%88%D8%B2-%D9%BE%D8%B1%D9%88%DB%8C%D8%B2-piruz-parviz-victorious-triumphant.3701622/"},{"title":"Feroze","url":"https://en.wikipedia.org/wiki/Feroze"}]

Based on the search results, I can provide you with detailed etymological information:

The Middle Persian word pērōz (victorious) derives from Avestan pairi.aojah, which is composed of pairi ("around") + aojah ("strength, power"), ultimately from Proto-Indo-Iranian *pari and *Háwǰas.

The Middle Persian form pērōz {pylwc}, {pyrwz} means "victorious, victor" and descends from the Proto-Iranian root *pari-auǰ-, while Avestan contains related forms aogah-, aogar-, and aojah- meaning "strength, might".

The compound *pari-aujah can be contextualized as "all strong" (meaning victorious), where pari means "around" (related to "paradise"), and aujah refers to strength.

The etymological connection shows how this word evolved through the Iranian language family, with the Modern Persian form pīrūz deriving directly from the Middle Persian pērōz.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T05:29:56.137Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%F0%90%AD%AF%F0%90%AD%A9%F0%90%AD%AB%F0%90%AD%A5%F0%90%AD%B0",
 "prompt": "Middle Persian pērōz: give the full etymology section verbatim (Proto-Iranian etymon, Avestan cognates, sources cited) and the list of descendants including New Persian and Arabic."
}
```


## [2026-09-05T05:29:58.285Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82ewg-",
 "prompt": "Give the reconstructed PIE root, its meaning, and the derived terms / descendants listed (especially Latin augeō, Germanic *wahsaną, Avestan/Indo-Iranian forms, Greek auxánō). Also list any references cited."
}
```


### [2026-09-05T05:30:03.047Z] TOOL RESULT

```
# Middle Persian pērōz Etymology and Descendants

## Etymology Section

The word derives from Parthian 𐭐𐭓𐭂𐭅𐭆 (prgwz /⁠Paryōž⁠/), which comes from Avestan 𐬞𐬀𐬌𐬭𐬌⸱𐬀𐬊𐬘𐬀𐬵 (pairi.aojah). This Avestan term combines 𐬞𐬀𐬌𐬭𐬌 (pairi, "around") with 𐬀𐬊𐬘𐬀𐬵 (aojah, "strength, power"), both deriving from Proto-Indo-Iranian roots: *pari and *Háwgas respectively, ultimately traceable to Proto-Indo-European *péri.

**Sources cited:**
- Nyberg, H. S. (1974), *A Manual of Pahlavi, Part II: Glossary*
- Gignoux, Philippe (1986), *Noms propres sassanides en moyen-perse épigraphique*
- Martirosyan, Hrach (2021), *Iranian personal names in Armenian collateral tradition*

## Descendants

- **Persian:** پیروز (piruz)
- **Arabic:** فَيْرُوز (fayrūz)
- Byzantine Greek, Classical Syriac, Middle Chinese, Old Armenian, and Old Georgian forms also documented
```


### [2026-09-05T05:30:04.391Z] TOOL RESULT

```
# Proto-Indo-European Root *h₂ewg-

## Reconstructed Root and Meaning
The root is **\*h₂ewg-**, with two primary meanings:
1. "to increase, to enlarge"
2. "to become strong"

## Key Derived Terms and Descendants

**Latin:** The page lists "*augeō*" (to increase, enlarge) from Proto-Italic, which descends from the causative form and is noted as having "irregular change o > a."

**Germanic:** "*aukaną*" (to increase, grow) is documented as a Proto-Germanic descendant.

**Indo-Iranian:** Proto-Indo-Iranian "*Háwgas*" means "might, vigour."

**Other Notable Descendants:**
- Old Armenian: "աճեմ" (ačem, to grow, increase)
- Latvian and Lithuanian forms preserving the root
- Proto-Slavic "*ovoťe*" (fruit)

## References Cited
The entry cites Helmut Rix's *Lexikon der indogermanischen Verben* (2001), Martin Joachim Kümmel's addenda to that work, and Michiel de Vaan's *Etymological Dictionary of Latin and the other Italic Languages* (2008).
```


## [2026-09-05T05:30:12.810Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/waist",
 "prompt": "Give the full etymology of 'waist', including the Old English/Germanic root and the PIE root it is traced to. Also anything on 'wax (to grow)'."
}
```


## [2026-09-05T05:30:14.253Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/indoeurop.html",
 "prompt": "Find the Indo-European root entry 'aug-' (to increase) in the appendix; quote its full text including which English words are listed (wax, waist, auction, augment, author, augur, inaugurate, August, auxiliary)."
}
```


### [2026-09-05T05:30:18.613Z] TOOL RESULT

```
# Etymology of Waist

**Origin**: Late 14c., from Old English *wæst* meaning "growth," with the semantic sense of "where the body grows."

**Germanic Root**: Proto-Germanic *wahs-tu-*, which also produced Old English *wæstm*, Old Norse *vöxtr*, Swedish *växt*, Old High German *wahst*, and Gothic *wahstus* "stature."

**PIE Root**: The Germanic forms trace back to PIE *wegs-*, an extended form of the root *aug- "to increase."

**Related Development**: The Middle English Compendium suggests a connection to *wacste* (early 13c.) meaning "quality of having grown or increased," possibly deriving from Old English *weaxan* "to grow."

---

## On "Wax" (to grow)

The page mentions Old English *weaxan* "to grow" as related to the waist etymology, linking it to the PIE root *aug- "to increase." However, the detailed etymology of the verb "wax" itself appears on a separate entry not fully reproduced here.
```


### [2026-09-05T05:30:25.614Z] TOOL RESULT

```
# Indo-European Root Entry: aug-

The entry for **aug-** ("To increase") appears in the appendix with this opening description:

"To increase. Oldest form _\*h2eug‑_, colored to _\*h2aug‑_. Variant _\*h2weg‑_ becoming _\*(a)weg‑_."

The entry lists these English word derivatives: wax, waist, nickname, eke, wax, woodwaxen, auction, augend, augment, author, authorize, augur, inaugurate, August, auxiliary, and auxin.
```


## [2026-09-05T05:30:33.898Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'ugra-  Adj\\|ugra-  \\|aoJah-\\|aojah-  n\\|aogah-' BRT.txt | head -20",
 "description": "Grep Bartholomae for ugra and aojah"
}
```


### [2026-09-05T05:30:33.960Z] TOOL RESULT

```
5788:*asti.aoJah-
5824:•  j.  *asti.aoJah-''  n.  'Kraft,  Stärke  der Knochen'  sva. 'Körperkraft':  Harqm..y5i hyqn  "Jaaha  aojtsta  ".  .  die  an  Körper- stärke die  stärksten  sind"  Yt.  Ä  55.
6161:Pü.:  vat  däiim. »  j.  aä.aoJah-  Adj.  (auch  fem.)  'sehr  stark': *°/ar9h^m'*   (ASf.)  dalvim  drujim  Y.j^.8; —  yS  /ania  daevayä  .drvjä  'jaahö  (GS£)
8075:tayö  (sd.)  Y-^Äa.       a)  'Ziel  des  Strebens'  •  j.  ujra-,  g.  ugra-  Adj.  (fem.  °r.7-)  'stark,
20537:*)  Eine  utsche  Götterfigur,  ursptüDgticli  eine Sonnengottheit  (Oldenberq  Rel.  d.  V«da  4S,  190. HiLLEBKANDT  Ved.  Mylh.  j.  128).    In  den  ap.  In- schriften erscheint  der  Name  Äf.  erst  TattArta- xirjcfs  11.;    Darios  L    und   Xerxet  1.    erwähnen der   Gottheit   nicht,    auch   im    gAw.    wird    sie nicht  genannt.    Ich  nehme  an,  dass  M.  in  der Etrengiardäifi/rischen  Lehre    als  Gottheit    nicht anerkannt   war,    ebenso  wenig  wie    iB.  Uaoma (sd.).    Da  aber  der  Glaube  an  M.  im  Volke  lu fest  wunelte ,  waren  die  Priester  späterhin  ge- nötigt, seine  Verehrung   zuzulassen.     Bekannt- lich  hat  sich  alsdann  der  ^-Kiilt  bis  weit  ins Abendland  hinüber  verbreitet     Vgl.  WlNDlsCK- MANN  Mithra  (AKM.  /),  Dst.  ZA.  2.  441. KompA.,  E.  (in  Ableit.);  Abieil,  (s.  •ni^ray, •ml%ranya^  —  Et.  ?  Vgl  Uhlenbeck  WAiSpr. 223,  Bgm.  GrGr.3  74_>'o.    —    aL    ruiträ-   m. 1)  'Freund',    2)  ein  Adilya;  np.  Wir 'Sonne'; a.  noch  p.EN.  Mnpalinn,  fl/lr/>ayii?  USW.  —  Vgl. v^umiia:   —  Pü. :  mihr  (geschr.  ralnn  oder mlnnk);    SüErl.    lu    Y.   16%     mailripalih.     — ')   Erst    in   Inschriften    des  4.  Jahrhunderts ; 2mal    ist   w'a-V,    imal   {Am.  4)   m'>r"    ge- schrieben.    iSchr.  mit   %'r'  s.  Bthl.  BB.  9. 131,  Hbu.  KZ.  jfi.  177;    auf  die  Schreibung mit  fir^  irgend  welche  Schlüsse    aufzubauen, wie  KZ.  36.  571   geschieht,  halte  ich  für  ver- fehlt  —  »>  S.  »i'Ja  No.   3.   —  3)  Hds.  Vo.   — 4)  Zweifellos  eine  aus  arischer  Zeit  stammende Verbindung. •  j.  "miSrö.aoJah-   Adj.  'falsche   Rede führend'   oder  'den  Mfyra   betrügend"'; mi^rfm  .  .  ye^Ae  dar/jä^i  bäsava  /ra-
```


## [2026-09-05T05:30:40.350Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^\\s*•\\s*[jg]\\..*aoJah-\\s*n\\.\\|aoJah-  n\\.\\|aogar\\|aoJa\" BRT.txt | head -20; echo \"=== around 8075 ===\"; sed -n '8070,8085p' BRT.txt",
 "description": "Find Bartholomae aojah- headword"
}
```


### [2026-09-05T05:30:40.457Z] TOOL RESULT

```
2882:ßr.  i^x?/""'  ai-  öia/e;  BtHL.  AF.  /.  II,  Gdn. VSt.j.  59.  — Zum  Laulliclien  s.  S  S3  I>  U- — Pü.:  gii/lan;  s.  rocb  No.  4t.  —  O  Unsicher (Vyt.  ir);  vll.  Opt.  —  ')  %  304  l.  i.  —  i)  S. mit  a^-i  fl.  —  4)  PÖ.:  öi,  Sü,:  ialam.  DST. ZA.  r.  328  meint:  "siaolä  aojäi  'j'ai  force comme  cbnntre'".  —  5)  Pü.:  apat  rasllan.  — 6)  Hds.  uxla. ').  aogar-  n.  'Kraft,  Stärke':  drujtf  'gar?
2901:KoropE. ;  Ableit.  —  Vgl.  aogar;  rmgak- ; 'aajah:  —  u.  lyai-  n.,  mp.  öi,  arm.  LW.  oiz,  — Pü.:  öi,  erl:  fiali7ia.  —  i)  Oder  in 'nojai-i — Cld.s  Fassung,  KZ.  30.  53S  halte  ich  lür  un-
2923:•  Jt  g.  ao5ista-  Adj.  (fem.  °ta-)  "der  stärkste ; sehr  stark':  uyranqm  °to  Yt  ig.  38;  — iCfrpm  'um  bavähi  Az.j;  —  w/ra  ^aja- maide  'tä  {/ravasayd)  yazamaide  Yt  y. 75;  —  •/a«tfM  «A'  'Um  (statt  NS.)  Yt /Q.141; —  hitqnt  Avö  °tö  Y.29.3;  5.15, 'N't  10,98;  —  srao-hm  ,  ,  yünam  'tim  Y. ,T7-'3i  —  f ravasayd  . .  yä  °ta  vazintqm \x,  13.  a6;  17;  —  yei  hyqn  *asti.aoJaT?ha (sd.)  'ta  YtÄss; —  k»m  'ta  mahrka.. Oi'sd  (sd.)  yaxäite  V.  //.  2.  a)  ASn.  -tim als  Adv, ;  'bmca  . .  vaRiye,t»napiea  (sd.)  V. 3.30.
5788:*asti.aoJah-
5824:•  j.  *asti.aoJah-''  n.  'Kraft,  Stärke  der Knochen'  sva. 'Körperkraft':  Harqm..y5i hyqn  "Jaaha  aojtsta  ".  .  die  an  Körper- stärke die  stärksten  sind"  Yt.  Ä  55.
6161:Pü.:  vat  däiim. »  j.  aä.aoJah-  Adj.  (auch  fem.)  'sehr  stark': *°/ar9h^m'*   (ASf.)  dalvim  drujim  Y.j^.8; —  yS  /ania  daevayä  .drvjä  'jaahö  (GS£)
15549:apaya;  —  V.  25.  45:  lies  pairiMcahi^ KompA.;    AbleiC   —   VgL /üiW.    —    ai. /Jri Adv.  (usw.),  mp.,  np./flr*  (GlrPh. /.310,  i  b. '59);    S.    noch    zu     *fairi.aoJastara-.    —    Vgl.
15552:•  j.  *pairi.aoJas'tara- ''  Adj.  'der  sieg- reichere': °rö  zT  ahmät  V.4.  10  FüZ.
20537:*)  Eine  utsche  Götterfigur,  ursptüDgticli  eine Sonnengottheit  (Oldenberq  Rel.  d.  V«da  4S,  190. HiLLEBKANDT  Ved.  Mylh.  j.  128).    In  den  ap.  In- schriften erscheint  der  Name  Äf.  erst  TattArta- xirjcfs  11.;    Darios  L    und   Xerxet  1.    erwähnen der   Gottheit   nicht,    auch   im    gAw.    wird    sie nicht  genannt.    Ich  nehme  an,  dass  M.  in  der Etrengiardäifi/rischen  Lehre    als  Gottheit    nicht anerkannt   war,    ebenso  wenig  wie    iB.  Uaoma (sd.).    Da  aber  der  Glaube  an  M.  im  Volke  lu fest  wunelte ,  waren  die  Priester  späterhin  ge- nötigt, seine  Verehrung   zuzulassen.     Bekannt- lich  hat  sich  alsdann  der  ^-Kiilt  bis  weit  ins Abendland  hinüber  verbreitet     Vgl.  WlNDlsCK- MANN  Mithra  (AKM.  /),  Dst.  ZA.  2.  441. KompA.,  E.  (in  Ableit.);  Abieil,  (s.  •ni^ray, •ml%ranya^  —  Et.  ?  Vgl  Uhlenbeck  WAiSpr. 223,  Bgm.  GrGr.3  74_>'o.    —    aL    ruiträ-   m. 1)  'Freund',    2)  ein  Adilya;  np.  Wir 'Sonne'; a.  noch  p.EN.  Mnpalinn,  fl/lr/>ayii?  USW.  —  Vgl. v^umiia:   —  Pü. :  mihr  (geschr.  ralnn  oder mlnnk);    SüErl.    lu    Y.   16%     mailripalih.     — ')   Erst    in   Inschriften    des  4.  Jahrhunderts ; 2mal    ist   w'a-V,    imal   {Am.  4)   m'>r"    ge- schrieben.    iSchr.  mit   %'r'  s.  Bthl.  BB.  9. 131,  Hbu.  KZ.  jfi.  177;    auf  die  Schreibung mit  fir^  irgend  welche  Schlüsse    aufzubauen, wie  KZ.  36.  571   geschieht,  halte  ich  für  ver- fehlt  —  »>  S.  »i'Ja  No.   3.   —  3)  Hds.  Vo.   — 4)  Zweifellos  eine  aus  arischer  Zeit  stammende Verbindung. •  j.  "miSrö.aoJah-   Adj.  'falsche   Rede führend'   oder  'den  Mfyra   betrügend"'; mi^rfm  .  .  ye^Ae  dar/jä^i  bäsava  /ra-
27074:•  j.   snaoJa-  m.  'Gewölk':  yahmat  haca
=== around 8075 ===
•  j.,  g.  izä-'>  f.  1)  'Stieben,  Eifer",  bes. 'frommer,  Glaub enseifer':  manS  voha  uru- nascä  asiiunqm  n>mascä  yä  ärmaiti/ (sd.) °zäcä  Y.4g.io;  —  mat  vä  padäis  (sd.) yä  frasrütä  (sd.)  -zaya  Y,  50. 8 ;  —  ^vldl- hmnäi  (sd.)  'zäcit  (IS.)  .  .  vahistsm  Y.jr. i;  —  ya%a  'za  (IS.)  viicim  näsima  Y, 70.4.  a)  Plur,  in  Verbindung  väwyaostay- usw.,  Plur.;    °m  yaostayS  fora^tayS  ärma-
dby  Google
379
ujraret-
380
tayö  (sd.)  Y-^Äa.       a)  'Ziel  des  Strebens'  •  j.  ujra-,  g.  ugra-  Adj.  (fem.  °r.7-)  'stark,
sva, 'Erfolg,  Glück'  '>;  astvatjrM. .  AJ  lii'jii:  kräftig" ;  1 )  von  a)  Menschen  und  ß)  Göttern :
vTsp^m  ahäm  .  .  °zay%    vafnJI   döi^räbyü  '  a)  kar^säspim  yat  äs   'ranarn  aojislS  Yt.
".  .   mit  den  Augen   des   Glücks  .  ."  Vt.  [75.38; — 'r?m  aojistim  bavahi yaira  &rj-
J5.94.         a)  in  Verbindung  mit  azutay-  säspun  Az,  _j.  ^)  fravasis  .  .   °rä  ..
(sd.) :  af  hvö  masdä  '2<J/ä  (NS.)  UsaiiisVii  aojistä  Yt  j^.  7  5 ;  —  'rA  asäunam  frava-
(sd.)  yS.M.4Q.%;  —  para . .  axHal  "iäca  sayS  Yt7j.i,   11,  47,  51,  63,  65,  69,  Y.
asaitiica  V.5.53.  |(»5.ii,  "¥,15.37;  — /ravaHbyS  ya  "nhi'a
Ableit.   —   Aus  dem  Pries.  16  (Des.)  des  V.    aiaii'^ürasta  Y.4.6;  Yl/O  66,   IJ.40;  —
J=-;Bthi.1F.  5.  a.6;S/J7.7--Pii-(i"i):, «/,;„«„„  /r«,aÄ«<7«    'ramm    aiwi>üra-    .
(lu  2):  i,VF«i».  Sü.:  «/Ä.™Ufl™.  -    »Mit/"?"'    Y./.18,    \ty.i;    156;    —    'rasm
```


## [2026-09-05T05:30:59.458Z] TOOL CALL #62: Bash

```json
{
 "command": "ls site/pages/70.jpg 2>/dev/null; pdftoppm -f 70 -l 70 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg70 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 70"
}
```


### [2026-09-05T05:31:02.086Z] TOOL RESULT

```
site/pages/70.jpg
total 1224
drwx------ 2 sfmqrb sfmqrb   4096 Sep  5 01:31 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  5 01:20 ..
-rw-rw-r-- 1 sfmqrb sfmqrb 282104 Sep  5 01:29 bqt733_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb 669351 Sep  5 01:29 bqt733.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  55169 Sep  5 01:30 pg67.png
-rw-rw-r-- 1 sfmqrb sfmqrb  77968 Sep  5 01:31 pg70.png
-rw-rw-r-- 1 sfmqrb sfmqrb  75801 Sep  5 01:29 pg71_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb  71145 Sep  5 01:29 pg71.png
```


## [2026-09-05T05:31:04.480Z] TOOL CALL #63: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg70.png"
}
```


### [2026-09-05T05:31:05.109Z] TOOL RESULT

```

```


## [2026-09-05T05:31:05.106Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-05T05:31:23.059Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SNS peroz ===\"; grep -n -i 'p.r.z\\|pērōz\\|peroz' SNS.txt SNS_pages.txt | head -10; echo \"=== FSF banafsh ===\"; grep -n 'بنفش' FSF_pages.txt | head -10; echo \"=== LAT augeo ===\"; grep -n 'augeo\\|augeō\\|auge5\\|augur\\b' LAT.txt | head -10",
 "description": "Grep SNS, FSF, Ernout-Meillet"
}
```


### [2026-09-05T05:31:23.148Z] TOOL RESULT

```
=== SNS peroz ===
SNS.txt:7907:(P'erfcum. phryz: J** {GNPE. 68) paiti+ /raec I 
SNS.txt:9362:•j5j« :pSrCz: C^Jf 
SNS.txt:9364:PYLwzy : j V^ tfj-ky (Mir. Man. II, 64) pyrwz 
SNS.txt:9366:■ Xo/tt^ f^tf^V'^) 'ifeiW :p§r6zgar: >J(2P-»«J 
SNS.txt:9368:■ T/TT^ lT-f/H^ >j?/j£jN :pSrOzgartar: Vjj^'O 
SNS.txt:9370:\^/U«^ -CMpAxW rperOzgartum: -6»)°^ 3 k j *-> 
SNS.txt:10791:Uii/&.1623)'pllhan-: i ^ t5 ^» sparazan- : t- 
SNS.txt:12432:• r/TT^ -To/TT^ -,£&* .-pSrOzgar: «W»«> 
SNS.txt:29055:sparazan- 176/5 
SNS.txt:30154:phryz 115/1 
=== FSF banafsh ===
3724:                    ‫درفشیدن تیغ‌های بنفش‬
7098:‫(‪)۳-۵۹-۱۶۴۱‬‬                                                       ‫هوا شد بسان پرند بنفش‬
9404: ‫(‪)۶-۷۳-۶۶۲‬‬                                          ‫زمین شد بنفش اکزران کتاران‬
11556:‫درفشان کنم تیغ‌های بنفش‬                           ‫تسندخو و سبکسر است و ممکن است‬
11558:         ‫جهان شد زگرد سواران بنفش‬                   ‫توآمدم بدان کهطوس دعوت تورا پذیرفته‪:‬‬
11610:                                                             ‫درفشیدن تیغ‌های بنفش‬
15652:             ‫‪-۳‬آسیمگی‪ ,‬آشفتگی‪ ,‬پریشانی‪:‬‬         ‫طبرخون و شبگون و زرد و بنفش‬
17932:‫بنفشه شادو کش آمد سمن صفا آورد‬                                   ‫رسدن‬
18249: ‫«بوی بنفشه ایدون چون بوی کنیزکان»‬                         ‫بدو گفت زین خواسته هیچ ماند‬
20564: ‫مغیلان بی‌بر به بار آمدی‬                              ‫معصفر شد آن پرنیان بنفش‬
=== LAT augeo ===
1410:aussi apprime, adaugeo, etc. Enfin il semble que ad serve k exprimer
5867:auctor: v. augeo.
5998:augeo
5999:de derives ou de composes de augeo, l'inchoatif augesco, -ere (et adau¬
6000:gesco), le compos e. adaugeo glose exactement emuS;w, npoaa.ofy}, M.L.149
6003:intensifs exaugeo et aucto, -as (Plaute) et auctito (Tacite); 1 1 adj.
6007:speciaux tels que la parente avec augeo n' est souvent plus sensible.
6008:Teis sont augur, auctor, auctoritas, auctoro, auctio, et auxilia.
6009:augur, -uris m. : augure (pretre) est un ancien nom du type fulgur/ful¬
6010:guris ou fulgeris. Une trace de la flexion alternante (augur, augeris)
```


## [2026-09-05T05:31:31.128Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSF context ===\"; sed -n '11548,11565p' FSF_pages.txt; echo \"=== pdf page tag ===\"; awk 'NR<=11558 && /pdf page/{p=$0} END{print p}' FSF_pages.txt",
 "description": "Read FSF banafš entry"
}
```


### [2026-09-05T05:31:32.797Z] TOOL RESULT

```
=== FSF context ===

‫(در لغت شهنامة عبدالقادر واه درشت به‬              ‫کوه برود و آن دو را اسیرکندو نزد طوس‬
                    ‫هیچ معنی نیامده است)‬         ‫بیاورد‪ .‬بسهرام به بالا می‌رود و فرود را‬
                     ‫درفشان (بر وزن درخشان)‬      ‫می‌شناسد‪ .‬فرودپهلوانان ایرانرابهخان خود‬
‫=رخشیدن ]‪:‬‬
         ‫[صفت فاعلی از درفشیدن د‬                 ‫دعوت می‌کند و به طوس پیام می‌فرستد که‬
                           ‫درخحشان تابان‪:‬‬        ‫آماده است بالشکریان اسران به جنگ‬
           ‫چو در دز شوم برفرازم درفش‬              ‫افراسیاب برود‪ .‬بهرام می‌گوید که طوس‬
‫درفشان کنم تیغ‌های بنفش‬                           ‫تسندخو و سبکسر است و ممکن است‬
 ‫(‪)۱-۷۲۱-۶۹۷‬‬                                     ‫خواهش تو رانپذیرد‪ .‬اگر بار دوم خود من نزد‬
         ‫جهان شد زگرد سواران بنفش‬                   ‫توآمدم بدان کهطوس دعوت تورا پذیرفته‪:‬‬
 ‫درخشان سنان و درفشان درفش‬                                      ‫وگر جز ز من دیگر آکیسدی‬
 ‫(‪)۵-۲۵-۰۶۷‬‬                                        ‫نباید بدو بودن ایمن بسی‬
                       ‫(اسدی ‪:)۷۰۴-۱۰۱‬‬            ‫طوس دعوت فرود را نمی‌پذیرد و داماد‬
               ‫درفش سران‬     ‫رافزشان‬
                                   ‫هدوا‬          ‫خود ریو را برای اسیر کردن فرود به بالا‬
 ‫چو باغ بهار از کران تا کران‬                      ‫می‌فرستد‪ .‬وقتی فرود او را می‌بیند به‬
‫(تاریخ بلعمی ‪ ...:)۹۲-۰۱‬و چیزی تابان را‬                               ‫تخوار می‌گوید‪:‬‬
=== pdf page tag ===
```


## [2026-09-05T05:31:33.047Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'pSrCz\\|pSrOzgar' SNS_pages.txt | head -5; awk '/pdf page/{p=$0} /pSrCz:|p§r6zgar/{print NR\": \"p}' SNS_pages.txt | head -5",
 "description": "Find SNS page for peroz"
}
```


### [2026-09-05T05:31:34.586Z] TOOL RESULT

```
6123:                                                                                                                        •j5j«   :pSrCz: C^Jf
6134:                                                                        T/TT^ lT-f/H^           >j?/j£jN          :pSrOzgartar: Vjj^'O
8570:                                                                                                                •   r/TT^ -To/TT^ -,£&* .-pSrOzgar:                   «W»«>
6123: 
6130:
```


## [2026-09-05T05:31:41.581Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'pdf page' SNS_pages.txt | head -3; echo \"---\"; awk 'BEGIN{RS=\"\\f\"} /:pSrCz:/{print \"leaf(awk)=\"NR}' SNS_pages.txt; awk 'BEGIN{RS=\"\\f\"} END{print \"total leaves\",NR}' SNS_pages.txt; echo \"=== FSF page tags ===\"; grep -c 'pdf page' FSF_pages.txt",
 "description": "Locate SNS peroz page"
}
```


### [2026-09-05T05:31:43.281Z] TOOL RESULT

```
---
leaf(awk)=89
total leaves 242
=== FSF page tags ===
0
```


## [2026-09-05T05:31:50.156Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==89 {print}' SNS_pages.txt | sed -n '1,60p'",
 "description": "Print SNS leaf 89"
}
```


### [2026-09-05T05:31:51.714Z] TOOL RESULT

```
                                                                                                    U; ^__L o-L ^l,                             Iff




                                                                 pelotan      I    ram §rbad: Y&b***J(F* twt^xjjw               :   •A.T,_,bSjJ




                                                                                                                        •j5j«   :pSrCz: C^Jf
                                                                 :   jzk(AiWb.      862)   aojah-       :j'       pairi. aojastara-:^-
                                                                     PYLwzy   :    j V^ tfj-ky (Mir. Man.              II,   64) pyrwz




                                                                         Xo/tt^         f^tf^V'^)        'ifeiW        :p§r6zgar:         >J(2P-»«J



                                                                        T/TT^ lT-f/H^           >j?/j£jN          :pSrOzgartar: Vjj^'O


                                                                                  \^/U«^      -CMpAxW rperOzgartum: -6»)°^ 3 k                       j *->




                                                                                  M/\o<£   m ^ /V       Wif/fc.        817)pa§man-         :   fc-


                                                                                   .YA/i««^     -j^j^         :   P Sm * 92»w: -*»w» « ^«J
                                                                                                        *

                                         /-tap-:*-,'
                      , ^
                            tapayeiti,
     t 4Pt i,   Aap- *.—       p
                                     83) ta£6an    , ..



                            ; c gnpe

\°


                                                   taXt!   ^""
                       \T/T^     (   VV*«)*»   8
```


## [2026-09-05T05:32:00.964Z] TOOL CALL #69: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A8%D9%86%D9%81%D8%B4%D9%87/",
 "prompt": "Quote the \"فرهنگ معین\" (Mo'in) section for بنفشه — especially any bracketed origin tag such as [په.] (Pahlavi) and the given meanings. Also any فرهنگ عمید or دهخدا etymological note."
}
```


## [2026-09-05T05:32:02.739Z] TOOL CALL #70: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/cyaxares",
 "prompt": "Give the etymology of the name Cyaxares — the Old Persian/Median form Uvaxštra, its analysis, and the Modern Persian rendering (هوخشتره / Hovaxshatare)."
}
```


### [2026-09-05T05:32:04.583Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T05:32:07.627Z] TOOL RESULT

```
# Violet (بنفشه) - Dictionary Entry Summary

## Meaning
The English translation is **violet**, referring to a flowering plant genus *Viola*.

## Etymology & Origin
According to **فرهنگ معین** (Mo'in Dictionary):
> "(بَ نَ ش ِ ) [ په . ]"

The bracketed tag [په.] indicates **Pahlavi** origins, connecting the Persian word to Middle Persian linguistic roots.

## Definition
**فرهنگ معین** describes it as:
> "a short plant with thin stalks and alternating leaves, having five petals in shades of violet, yellow, and white"

The flower blooms early spring and is notably fragrant.

## Additional Notes
**فرهنگ عمید** characterizes it as an ornamental plant with thin stalks, alternating leaves, and flowers in violet, blue, and yellow—some varieties having medicinal properties. The term **بنفشهٴ طبری** refers to a wild violet species found in northern Iran near streams.
```


## [2026-09-05T05:32:12.578Z] TOOL CALL #71: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Cyaxares",
 "prompt": "Give the name section: the Median/Old Persian form Uvaxštra, its etymology and meaning, the Greek Kyaxares, and the Modern Persian form (هوخشتره / Hovakhshatare / Huvaxštra)."
}
```


## [2026-09-05T05:32:14.573Z] TOOL CALL #72: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D9%86%D9%81%D8%B3%D8%AC",
 "prompt": "Give the etymology of Arabic بنفسج (banafsaj) 'violet' — is it a borrowing from Middle Persian/Persian? Which sources are cited?"
}
```


### [2026-09-05T05:32:19.148Z] TOOL RESULT

```
# Cyaxares: Name Section Summary

**Median/Old Persian Form:**
The article states that Cyaxares's Median name was "ᴴuvaxšϑra" in cuneiform script, while the Old Persian form is rendered as "ᴴuvaxštra."

**Etymology and Meaning:**
According to the Wikipedia article, this name "meaning 'good ruler.'" The Greek author Diodorus Siculus used an alternative Hellenization, rendering it as "Astibaras," which derives from a Median name meaning "spear bearer."

**Greek Form:**
The Latinized name "Cyaxares" comes "from the Greek _Kuaxárēs_ (Κυαξάρης)," which was itself the Hellenization of the original Median designation.

**Modern Persian Form:**
The article includes "هووخشتره" as the Modern Persian rendering, though the specific transliteration details appear in the language links section of the Wikipedia page rather than elaborated in the main text.

The name reflects common Persian naming patterns emphasizing martial and leadership qualities, evident in the "spear" component shared with his son Astyages's name.
```


### [2026-09-05T05:32:19.893Z] TOOL RESULT

```
# Etymology of Arabic بنفسج (banafsaj)

Yes, بنفسج is a borrowing from Middle Iranian languages. According to the Wiktionary entry, the word comes "From Middle Iranian; see بنفشه (banafše) and compare Middle Persian wnpšk' (wanafšag, 'violet')."

The entry establishes a connection to Persian while noting the broader Middle Iranian origin. However, **no specific scholarly sources are cited** in this dictionary entry—it simply cross-references related terms in Persian and Middle Persian without providing bibliographic documentation.
```


## [2026-09-05T05:32:33.101Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'vaxstra\\|vaxstra-\\|Wachstum  habend\\|u\\.vax' BRT.txt | head -10; echo \"=== col 1836 ===\"; grep -n '^1836\\|1835  \\|1836  ' BRT.txt | head",
 "description": "Grep Bartholomae for u.vaxštra"
}
```


### [2026-09-05T05:32:33.172Z] TOOL RESULT

```
6598:yä  oder_>'J(?)  vll.  sva.  'es  geschieht,  kommt vor,  dass  ..':  asit'i^  yä  *ayar3Aa^a  sparr/a (sd.)  YL/0.  laöGl.;  —  asti'*''  yS gavasnaAe (sd.)  snäuya  jya  Yt  10. 1 28  Gl.  III)  als j  Praedilcatsverbnm  (Kopula).  Das  Praedikat ist  I)  ein  Substantiv,  das  mit  dem  Subjekt im  Numerus  und  Kasus,  oder  ein  Adjektiv, das  auch  im  Genus  kongruirt.  A)  I  im Ap.  (die  Kopula  folgt  dem  Praedikat): adam  bardiyä'  amiy  .  .  adam  xsäya'iiya* amiy  Bh.  b,  h;c-f*,  h-j^,  Bh.  7.5,  11,  16', -■3>  S'  55.  13-  4.2*,  D.(t.4;  —  adam xsaya%iy£^  amiy  asagartaiy  ""uvaxstraAyä laumäyä  Bh.2.  i4,4.2,Bh.g,;  —  adamsäm xsäya^iyt^  äham  Bh. /.  6;  —  ka"bujiy<^ ,  .paruvam  idä  xsäya'^iya"  ähJ^  Bh. /.  10; —  g  *duvitäiaranam  (sd.)  vayam  xsäya- üyä  amahy  Bh.  j.  4;  —  tyaiy  paruvam xsäya'iiyä  aha"  Bh.  7.  4;  —  kalä  pa- ruviyata'  hyä  amäxam  taumä  xsäya'iiyä (sd.)  äh(^  Bh.  j.  3 ;  —  adam  pärta''  amiy D.  77. 3 ;  —  martiyJ^  Ayo*  draujana'' ahatiy  Bh.^.5,  14;  14,  5;  —  Äj'u*  daustä <Ua*.  .  hyi^  arika''  äha*  Bh. /.  8;  2.4,  6, 3-  II,  5.4;  —  tyaisaiy  fratamä  martiyä anusiyä  äha"täi'>  Bh.  ;.  13;  J.  7,  8,  11,  13, /.  7;  —  negirt:  ya^ä  naiy  arika"  äham Bh..:^.  13;  13  ^  —  ty^  adam  naiy  bardiya'' amiy    Bh.  7.  13.  B  [)    im   jAwr.    (Die
10775:•  p.  xäa^rita-"  m.  EN.  eines  medischen Fürsten:  fravarfis  ,  .  a^aha''  adam  °te^ amiy  ''uvaxstrahya  (sd.)  taumaya  adam xiäyaiiiya''  amiy  madaiy  Bh.  e;  Eh.  2. 5, 4. 2,
22889:—  yaiibyS  xsahnmcl  *ayiBjivamn>m  (sd.) vandaiti  armaitifY.  2&  3;  —  auch  Med.: yf  nä  aMi  aojaftka  vandayattä  yqm  . . gaiüqm  . .  baxsain  (sd.)  "dem,  der  durch die  Kraft  der  A.  gross  machen  wird  das . ." V.  ^0. 3.  a)  Med.  und  Pass.  'wachsen,  ge- deihen': var^ayaiauha  mana  vaca  vTspss^a paiti  varsa/r^  Y.  io.  j;  —  sfaipaike  nS daiühu!  fralataila  vartbataiia  (3SKPM.) Yt  13. 68;  —  yö  daitihave  hu.vaxsJi  fra- t^mnahe  7!ar>\>mnahe  ..  V..^.  zGl.;  — aila  äruxiya  nasus  as.aojastara  vanlayde yaäia  para  ahmät  as  V.  g.  48.  a)  PPfP. 'gross,  gewaltig";  kihrpasca  .  .  srTrä  .  . v)r»zää  am>ianqm  spmtanqm  Yt.y.81;
26011:'nützen,  Nutzen  schaffen',  mit  Akk.  des wem?:  ya%a  väts  .  .  vTsptm  ahüm  .,/rä- la/icä  var3%atUa  saosyanti{ila.Xl  Sing.)& A.  4.  6;  —  ys  daitihave  hu.vaxsai  frdh>m- nake  vanltimnahe  .  .  suyamnahe  N.4-  2 Gl.  a)  insbes.  'den  Nutzen,  den  Vor- teil schaffen,  erwirken',  d.  i.  das  gute  Loos im  andern  Leben'';  wua^a  sao^qs  (sd.) ya%a  vispftn  akum  astvanhm  sävayät  Yt, y"9i  —  Aarp'hrai  asahe  gaihanqm suyaiitnanqmla  saosyantqmca  "um  zu wachen  . .  über  die,  die  den  Nutzen  be- kommen und  die  ihn  schaffen  werden" Y.55. 3;  — y^a  vS  saofyatttS  dahyunqm suyamna  väcim  ^barmti  Y,  yo.  4;  — sttoSyant-  s.  auch  bes. np.  tgl.  iSd  'Nutien'').  —  PQ.  (lu  Y,  55): sütan  u  nilömattdan,  (m  Y./O);  sütömand,  (lu V.  4);  süßiüt  (3.Sg.;^  erl.:  kui  tut  palas  kuneU
30472:Ableit  aas  *hu-yär-  n. j.  Au.vaxJ'  N.  46' :  lies  iä  varl".
30473:•  j.  hu.vaxJia-  ra,  'gutes  Wachstum,  G^ deihen':  'lai  frm>mnahe  V.  4,2  Gl.
30476:Eig.  *»on  gulcm  Wuchi';  *vaxstra-  n-,  IHD V.  ifflji-.  —  ')  Andre  lesen  'xiaiar",  'jcialr»-. 'xilara-,   s.  iB.  JusTI  NB.  140  (der    in   dem
=== col 1836 ===
30450:1836  :
```


## [2026-09-05T05:32:36.301Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '30465,30485p' BRT.txt",
 "description": "Read Bartholomae col 1836 Uvaxštra"
}
```


### [2026-09-05T05:32:36.349Z] TOOL RESULT

```
•  j.  hu-yaStay-  f.  'gutes  Opfern,  Weihen': alyelfica  'yestiia  Au/rahrfti(,%A.)ca  zao- %ranqm  Y,  68.  9.  3)  'gute  Verehrung': kS  *yesti  ks  dulyt^li  mam  xT  matnyete ya%at»m  "wer  meint,  dass  ich  mit  guter, wer  dass  ich  mit  schlechter  Verehrung zu  verehren  sei?"  Yt./o.  108;  —  'yest't tava  aAuräne  sfnnäini  Y.  68. 14.
ai.  vgl,  niiffaji-  f.  —  Pü.:  xüp  yeuisniA.
•  j.  huyä)Tia-  Adj,  'das  Lager  teilend, Lager-,  Stubengenosse';  vlsaitivä  asti miirS  aniar»  ha!a  suptioarynga  (sd.)  .  , pama.sa%wa  autark  'na  (AD.)  \t  10.116.
El  ?  —  ')  Sva.  hämö.giltiv-.
•  j.  huyäirya-  Adj.  (fem.  'yä-)  a)  'gutes Jahr,  gute  Ernte  habend':  kaaa  airys daitihävS  'ya  bavanti  YtÄ36;  —  'ya avi  dairihus  Yt.<?.  9.  b)  'gutes  Jahr, gute  Ernte  verschaffendgbewirkend':  masya ..  'ya    äpd    barmtil    Yt.  A*.  40;  —  pairi-
kayäi  .  .  yä  duiyatrya  yqm  mafyska  «a duivacanhs  'yqm  nqma  aojaite  Yt  6. 51.  A)  als  neuti.  Subst  'Gutjahr,  gute
Erntejahr':  tütrxm  , .  ytm  . .  ^>^(IS.)ä daiAhave  uzjasmtfm  duiyäiryJ{sd.)cä  Vl Ä36.
Ableit  aas  *hu-yär-  n. j.  Au.vaxJ'  N.  46' :  lies  iä  varl".
•  j.  hu.vaxJia-  ra,  'gutes  Wachstum,  G^ deihen':  'lai  frm>mnahe  V.  4,2  Gl.
PiL;  fa  httvaxs.
•  p.  "u'vaxätra-"  m.  EN.  eines  medischec Königs,  KyiXAie.i'' i /ravartis  nSma'  Uta- i/a*  .  ,  aiaÄa*  adam  xsa^rit^  amij 'rahyä  taumäya  Bh.s.s;  4.3,  Bh.  e;  — I  cih'c^taxmt^  namd"  asagartiyt^  .. dhaAer  adam  xsahrita^  atnty  'rakf9 taumayS  Bh.  4.  3 ;  2,  1 4,  Bh.  g.
Eig.  *»on  gulcm  Wuchi';  *vaxstra-  n-,  IHD V.  ifflji-.  —  ')  Andre  lesen  'xiaiar",  'jcialr»-. 'xilara-,   s.  iB.  JusTI  NB.  140  (der    in   dem
ferner  Fov  KZ.  j/.  49J-  —  '>  VgL  Jm GltPh.  2.  410.  Ein  Versuch,  die  per»,  nod die   griech.   Namensfonn  lu  TCrmitteln,   bej
WSCHULIZ   KZ,  _JJ.   3J3.
p.  *«i'flya.,  '•uvajiya-:  s.  Sp.   1846  f.
•  p.  naiy  "saiaurim  naty  •»  "huvatam'' züra*  (sd.)  akunavam  Bh.  4.13.
Vgl.  lu  ziirah:  —  ')  So  die  Lesung  derN.t., die  aber  unmöglich  ist,  da  k  vor  »  nicht  ge- schrieben wird;  IF.  12.   129.
•  j. yä  aridulai  *apailital  *äjayaurva  (sii yä  "hu.varashana  N.  54.
fa.:  e  tc  andar  an  i  fa  var  i  a/e(. .);  dulieli also  wobi  zu  'iKiraA-.  Die  Lesung  yöAu  vtr" gibt  auch  keinen  Sinn.
p.  ^laiä':  1.  unter  hv',  Sp.  1853  f.
•  j.  huvira-  Adj.  (fem.  'rä-):  s.  unter 'livira:
```


## [2026-09-05T05:33:03.864Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"vanä-\\|vanā-\\|vana-vax\\|vana\\.vax\" BRT.txt | head -10; echo \"=== Baum ===\"; grep -n \"f\\.  'Baum'\" BRT.txt | head -5",
 "description": "Check Bartholomae for vanā- tree and vana-vaxša"
}
```


### [2026-09-05T05:33:03.941Z] TOOL RESULT

```
20997:70',  wogepen  aL  yavanä-  anf  laj-n'  beruht.        '  ■*  .'  ^  „  •  ,
=== Baum ===
22613:•  j.  *van-  f.  'Baum':  yaäia  masyayä  vana kasyaiikam»  "nam  (GP.,  als  Obj.)  aiwi.- vgr-mvaiü  (fA.)  V.5.  2^.
22633:•  j.  vana-  f.  'Baum':  ya%a  masyayB  °na (NS.)  kasyanhqm  vanqm  aiwi.vinnvaiti (sd.)  V.5. 24;  F.  ^;  —  avi  'nqm  yqm kvapTm  (sd.)  V.5. 19;  —  upa  avqm  'nqm ..ya  vaoce  vlspS.6i^(.sd.}  nqma  Yt.i2.tyi —  upa  tqm  'nqm  aati  . .  äi-re  alsmqn isaiti  (sd.)  V,5.  3;  i.
```


## [2026-09-05T05:33:18.037Z] TOOL CALL #76: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/%D9%BE%DB%8C%D8%B1%D9%88%D8%B2' \\\n 'https://en.wiktionary.org/wiki/%D8%A8%D9%86%D9%81%D8%B4%D9%87' \\\n 'https://en.wiktionary.org/wiki/%F0%90%AD%AF%F0%90%AD%A9%F0%90%AD%AB%F0%90%AD%A5%F0%90%AD%B0' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82ewg-' \\\n 'https://www.etymonline.com/word/waist' \\\n 'https://www.ahdictionary.com/word/indoeurop.html' \\\n 'https://abadis.ir/fatofa/%D8%A8%D9%86%D9%81%D8%B4%D9%87/' \\\n 'https://en.wikipedia.org/wiki/Cyaxares' \\\n 'https://en.wiktionary.org/wiki/%D8%A8%D9%86%D9%81%D8%B3%D8%AC' ; do\n timeout 120 python3 tools/fetch_source.py \"$u\" --note 'pdf page 70, root Aueg/Aug/Uog/Ug: pirûz, banafšeh, Hovaxšatar, waist, PIE *h2ewg-' 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-05T05:33:25.737Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/78a49cf13f074c9b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a2561747e226c989.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e3f1273e371885f4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fad8a3bc7e47a664.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/df1bc4d2607394c1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3735d75498a331a4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7af1e7a4e877523c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/00b2c829968cc7a8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4f77f7f970c8c2ee.txt
```


## [2026-09-05T05:33:49.805Z] AGENT

Now I'll write the verification file.


## [2026-09-05T05:45:12.952Z] TOOL CALL #77: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk70.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\nroot_entry = {\n  \"entry\": 0,\n  \"root\": \"Aueg, Aug, Uog, Ug\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *h₂ewg- / *h₂weg- 'to increase, grow strong', with the s-extension *h₂wég-s- (Pokorny 84-85 au̱eg-, u̱ōg-, aug-, ug- 'vermehren, zunehmen')\",\n  \"note\": \"The root box is right on all three counts. Pokorny IEW pp. 84-85 heads the article exactly as Nourai's four variants: 'au̱eg-, u̱ōg-, aug-, ug- ‚vermehren, zunehmen‘, mit s-Formans aueks-, auk-s-, ueks-, uk-s-', and the article contains, in this order, Av. ugra- 'stark', Av. aojah-/aogah- 'Kraft, Stärke', Lat. augeō/auctor/augur/augustus/auxilium, Goth. aukan and wahstus, and Av. vaxšaiti / uxšyeiti — i.e. every branch of Nourai's chart. Watkins/AHD heads the same root 'aug-¹. To increase. Oldest form *h₂eug-, coloured to *h₂aug-. Variant *h₂weg- becoming *(a)weg-', and Buck §12.53 (p. 876) opens with 'IE *aweg- (*aug-, *ug-, and with -s- extension *aweks-, etc.)'. The only refinement modern work adds is the laryngeal: the root is now written *h₂ewg-, and the variants Nourai lists as four separate 'roots' (Aueg / Aug / Uog / Ug) are the ablaut grades of one root, not independent bases. The label 'Indo-European' and the gloss 'to increase, strengthen' are both correct.\",\n  \"note_fa\": \"ریشهٔ هندواروپایی آغازین *h₂ewg- «افزودن، بالیدن، نیرومند شدن» ریشه‌ای کاملاً پذیرفته‌شده است و پوکورنی در صفحات ۸۴–۸۵ دقیقاً همان چهار گونه‌ای را که نورایی آورده (au̱eg-، u̱ōg-، aug-، ug-) سرفصل مقاله کرده است. همان مقاله همهٔ شاخه‌های نمودار را دربردارد: اوستایی ugra- «نیرومند»، aojah-/aogah- «نیرو»، لاتینی augeō و augustus، و اوستایی vaxšaiti و uxšyeiti. تنها اصلاح امروزی این است که این چهار صورت، ریشه‌های جداگانه نیستند بلکه پایه‌گردانی‌های (ablaut) یک ریشه‌اند و امروز با حنجره‌ای نوشته می‌شود. ادعای نورایی دربارهٔ خود ریشه درست است.\",\n  \"sources\": [\n    W + \"Reconstruction:Proto-Indo-European/h%E2%82%82ewg-\",\n    \"https://www.ahdictionary.com/word/indoeurop.html\"\n  ],\n  \"ref_check\": [\n    {\"ref\": \"POK:84\", \"status\": \"supports\",\n     \"note\": \"POK_01.txt, awk leaf 94 (the leaf carrying the printed page break 84|85): '^^^S-f W^g-, aug-, ug- ,vermehren, zunehmen', mit s-Formans aueks-, auk-s-, uek'S-, uk-s-.' (OCR of 'au̱eg-, u̱ōg-, aug-, ug-'); the article starts at the foot of p.84 and runs over p.85. Exactly Nourai's four variants and his gloss.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"WLD_Bd1_pages.txt, grep 'vermehren, zunehmen' — no hit (OCR of Bd. I is poor); Pokorny's own cross-reference at the end of the neighbouring article reads 'WP. I 220 f.'\", \"stance\": \"silent\",\n     \"note\": \"Walde-Pokorny I 22 f. is the parallel article (cited by Mann s.v. augmn- as 'WP I, 22'); the local DLI scan of Bd. I could not be searched for it.\"},\n    {\"src\": \"AHD\", \"where\": \"online Appendix of Indo-European Roots s.v. aug-¹\", \"stance\": \"supports\",\n     \"note\": \"'aug-¹. To increase. Oldest form *h2eug-, colored to *h2aug-. Variant *h2weg- becoming *(a)weg-.' — derivatives listed: wax, waist, nickname, eke, woodwaxen, auction, augend, augment, author, authorize, augur, inaugurate, August, auxiliary, auxin.\"},\n    {\"src\": \"IEC\", \"where\": \"IEC.txt lines 799, 801, 871 (Mann s.vv. augmn-, augos, aueKs-)\", \"stance\": \"supports\",\n     \"note\": \"'augmn- ‘growth, height’. WP I, 22'; 'augos … ‘growth, increase’ … (Av. aogō, n. ‘help’ and Skt. ugráḥ ‘powerful’ may belong here)'; 'aueKs- (oueKs-, auKs-, ouKs-) ‘grow; growth’ … Skt. vaks-, uksami … Gk. aéxo, aüxo'.\"},\n    {\"src\": \"SYN\", \"where\": \"SYN.txt §12.53 GROW, printed p.876\", \"stance\": \"supports\",\n     \"note\": \"'1. IE *aweg- (*aug-, *ug-, and with -s- extension *aweks-, etc., orig. desid. formation). Walde-P. 1.22f.' — Buck's headroot is Nourai's root.\"}\n  ],\n  \"nodes\": []\n}\n\nN = root_entry[\"nodes\"]\n\nN.append({\n  \"id\": 1, \"lang\": \"Avestan\", \"words\": \"ugra; aojah, aogah\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Both words are attested Avestan and both are the standard Iranian representatives of this root. (a) Av. uɣra- / Gathic ugra- (Bartholomae AiW col. 380) 'strong, mighty', fem. uɣrā-, superlative aojišta-, is the zero-grade *h₂ug-ró- and matches Skt. ugrá- exactly; Pokorny 84 prints the equation 'Ai. ugrá- ‚gewaltig‘ … == av. ugra- ‚stark, kräftig‘ (Komp. Sup. aojyah-, aojišta-)'. (b) Av. aojah- / aogah- n. 'strength, might' (with the r-stem aogar- beside it) is the e-grade s-stem *h₂éwg-os-, the exact cognate of Skt. ójas- and of Lat. augustus' base; Pokorny 85: 'es-St. ai. ōjas- n. ‚Kraft, Stärke‘, av. aojah-, aogah- (ebenso r-St. aogarə) ‚Kraft, Stärke‘'. The two Avestan spellings aojah-/aogah- are the ordinary j~g graphic doublet of the Avestan script, not two different words. Nourai's glosses ('strong' / 'strength') and the language label are correct; the derivation from the root box is the standard one.\",\n  \"derivation_fa\": \"هر دو واژهٔ این گره در اوستا شاهد دارند. uɣra-/ugra- «نیرومند، زورمند» (بارتولومه، ستون ۳۸۰) از پایهٔ صفر *h₂ug-ró- ساخته شده و هم‌ریشهٔ دقیق سنسکریت ugrá- است؛ صفت برترین آن aojišta- است. aojah-/aogah- «نیرو، توان» ستاکی از نوع -as از پایهٔ پر *h₂éwg-os- است و دقیقاً برابر سنسکریت ōjas-؛ دو املای j و g تنها دوگانگی نگارشی خط اوستایی است و دو واژهٔ جدا نیست. پوکورنی در صفحات ۸۴ و ۸۵ هر دو را زیر همین ریشه می‌آورد. ادعای نورایی درست است.\",\n  \"sources\": [W + \"Reconstruction:Proto-Indo-European/h%E2%82%82ewg-\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:84,85\", \"status\": \"supports\",\n     \"note\": \"POK_01.txt leaf 94: 'Ai. ugrá- … == av. ugra- ‚stark, kräftig‘ (Komp. Sup. aojyah-, aojišta-)' (p.84) and 'es-St. ai. ōjas- n. ‚Kraft, Stärke‘, av. aojah-, aogah- (ebenso r-St. aogarə) ‚Kraft, Stärke‘' (p.85). Both of Nourai's lines are on the pages he cites.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"BRT.txt line 8075, col. 379/380\", \"stance\": \"supports\",\n     \"note\": \"'j. uɣra-, g. ugra- Adj. (fem. °rā-) ‚stark, kräftig‘' with the superlative aojišta-; and at line 2882 ff. 'aogar- n. ‚Kraft, Stärke‘ … Vgl. aogar; … *aojah'.\"},\n    {\"src\": \"IEC\", \"where\": \"IEC.txt line 801 s.v. augos\", \"stance\": \"partial\",\n     \"note\": \"Mann notes 'Av. aogō, n. ‘help’ and Skt. ugráḥ ‘powerful’ may belong here, but seem to be contradicted by Skt. ójas: Av. aojo, -áh- ‘power’ (*ǵ or a secondary *g?)' — same family, but he flags a velar-series problem between ōjas- and aogah-.\"},\n    {\"src\": \"AHD\", \"where\": \"online Appendix s.v. aug-¹\", \"stance\": \"silent\",\n     \"note\": \"Watkins' entry gives only the Latin/Germanic/Greek/Baltic branches; no Avestan forms are cited, so it neither confirms nor denies the Avestan pair.\"}\n  ]\n})\n\nN.append({\n  \"id\": 2, \"lang\": \"Avestan\", \"words\": \"pairi-aojastara, pari-aužah\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Bartholomae's Altiranisches Wörterbuch col. 862 — exactly the column Nourai cites — has the entry '*pairi.aoǰastara- Adj. ‚der siegreichere‘: °rō zī ahmāt V.4.10 FüZ.', i.e. a Younger-Avestan comparative attested once, in the Pahlavi-gloss tradition to Vīdēvdād 4.10, and Bartholomae continues 'Kompar. aus *pairi.aoǰah- Adj. ‚der die Übermacht hat‘; vgl. aiwi.aoǰah-'. The compound is pairi 'around, over' (= Skt. pári, PIE *péri, the pairi- of pairi-daēza- 'paradise') + the s-stem aoǰah- of node #1, so literally 'having strength all around, superior in strength' > 'victorious'; the comparative suffix -tara- gives 'more victorious'. Nourai's second line 'pari-aužah' is Bartholomae's own reconstructed Iranian preform, printed in the same column as 'aus ir. *pari-auǰə'. The asterisks are Bartholomae's: the simplex *pairi.aoǰah- is not itself attested and the comparative rests on a restored reading; Nourai prints both without asterisk, which slightly overstates their attestation, but the forms and the gloss 'all strong, victorious' are Bartholomae's.\",\n  \"derivation_fa\": \"بارتولومه در فرهنگ ایرانی باستان، همان ستون ۸۶۲ که نورایی یاد کرده، مدخل *pairi.aoǰastara- «پیروزتر» را می‌آورد و آن را صفت برتر از *pairi.aoǰah- «آن که زور برتر دارد» می‌داند. این مرکب از پیشوند pairi «پیرامون، از هر سو» (همان پیشوند pairi-daēza- = پردیس) و ستاک aoǰah- «نیرو» ساخته شده است، یعنی «همه‌سو نیرومند» و از آنجا «پیروز». گونهٔ دومی که نورایی آورده (pari-aužah) همان صورت بازساختهٔ ایرانی *pari-auǰah- است. تنها نکته آن است که هر دو صورت در اصل ستاره‌دارند و نورایی ستاره را حذف کرده است؛ در مجموع ادعای او درست است.\",\n  \"sources\": [W + \"%F0%90%AD%AF%F0%90%AD%A9%F0%90%AD%AB%F0%90%AD%A5%F0%90%AD%B0\"],\n  \"ref_check\": [\n    {\"ref\": \"BRT:862\", \"status\": \"supports\",\n     \"note\": \"BRT.txt lines 15547-15556 (the column number '862' is printed at line 15547): 'j. *pairi.aoǰas‘tara- Adj. ‚der siegreichere‘: °rō zī ahmāt V.4.10 FüZ. Kompar. aus *pairi.aoǰah- Adj. ‚der die Übermacht hat‘; vgl. aiwi.aoǰah-'. Exactly Nourai's node.\"},\n    {\"src\": None, \"ref\": \"HUB:45\", \"status\": \"partial\",\n     \"note\": \"HUB.txt awk leaf 56 (printed '— 45 —'), no. 354: Hübschmann only REJECTS the rival etymology ('Np. pērōz ‚Victor, felix, faustus‘ kann nicht = zd. *paiti-raočah- gesetzt werden'); he does not himself state the pairi-aoǰah- derivation on that page. Supports the note attached to node #3, not this node's positive claim.\"},\n    {\"ref\": \"NYB:160\", \"status\": \"supports\",\n     \"note\": \"NYB_vol2_glossary.txt, running head 'payam- 160 pērōz-kar': 'pērōz [pylwc‘] victorious, victor … SW development < *pari-auǰah-, v. ōž; M Prs pyrwz; MPrth prywž … Paz. perōž, NP pērōz.' Nourai's page is exact.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"AiW col. 862\", \"stance\": \"supports\",\n     \"note\": \"see ref_check; Bartholomae also adds there '— np. usw. pērōz ‚siegreich‘ (aus ir. *pari-auǰə …)'.\"},\n    {\"src\": \"NYB\", \"where\": \"A Manual of Pahlavi II p.160 s.v. pērōz\", \"stance\": \"supports\",\n     \"note\": \"'SW development < *pari-auǰah-' — Nyberg reconstructs precisely Nourai's second form.\"},\n    {\"src\": \"SNS\", \"where\": \"SNS_pages.txt leaf 89 (printed page number OCR'd as 'Iff' = ۱۴۴) s.v. pērōz\", \"stance\": \"supports\",\n     \"note\": \"Tavoosi's glossary prints 'pērōz … az pairi.aoǰastara-: … aoǰah- (AiWb. 862)' — the same two forms and the same Bartholomae column Nourai cites.\"}\n  ]\n})\n\nN.append({\n  \"id\": 3, \"lang\": \"Persian\", \"words\": \"pîrŭz «پیروز» (extra: فیروز)\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"NP پیروز pīrūz 'victorious' continues Middle Persian pērōz <pylwc'>, attested from the 3rd c. CE onward (the Sasanian king Pērōz I, r. 459-484; Armenian Peroz, Syriac Pērōz, Greek Περώζης, Latin piroses in Ammianus XIX.2.11). MP ē regularly raises to NP ī and MP ō to NP ū, whence pērōz > pīrūz. The Old Iranian preform is *pari-auǰah- 'having superior strength' (node #2): *pari-auǰah > *parīuǰ > pērōz, with contraction of -ari-au- to ērō. Wiktionary (following Nyberg, Gignoux and Martirosyan) routes it through Parthian prgwz /Paryōž/, i.e. it treats MP pērōz as a north-western form taken into Persian, whereas Nyberg calls it an 'SW development' — a difference about the dialect of transmission, not about the etymon. The variant فیروز fīrūz that Nourai puts in the extra-script slot is the Arabised shape of the same word (Arabic has no p; Horn no. 354 lists 'arab. LW. fīrūz'), which returned into Persian as a doublet and also supplied فیروزه fīrūza 'turquoise'. The chart's NOTE is correct in substance: Horn p.78 did derive pērōz from Av. *paiti.raočah- 'toward light', and Hübschmann p.45 rejected it because Middle Persian and all the early foreign renderings show pēr-, never *patrōč-; modern scholarship sides with Hübschmann and Bartholomae.\",\n  \"derivation_fa\": \"«پیروز» دنبالهٔ فارسی میانهٔ pērōz است که از سدهٔ سوم میلادی به بعد شاهد دارد (نام پیروز ساسانی؛ ارمنی Peroz، سریانی Pērōz، یونانی Περώζης، لاتینی piroses نزد آمیانوس). ای کشیدهٔ فارسی میانه در فارسی نو به ی و او کشیده به و بدل شده است؛ صورت ایرانی باستان *pari-auǰah- «دارای زور برتر» است که با هم‌آمیختن -ari-au- به ـــērō رسیده است. ویکی‌واژه (به پیروی نیبرگ و گینیو) راه وام‌گیری را پارتی prgwz می‌داند و نیبرگ تحولی جنوب غربی؛ این اختلاف در راه انتقال است نه در ریشه. «فیروز» معرّب همین واژه است (عربی پ ندارد) که دوباره به فارسی بازگشته و دوگانه ساخته است (و فیروزه از همان است). دربارهٔ یادداشت نمودار: هرن در ص ۷۸ پیروز را از *paiti.raočah- «رو به روشنایی» گرفته بود و هوبشمان در ص ۴۵ آن را رد کرد؛ پژوهش امروزی نیز جانب هوبشمان و بارتولومه را گرفته است. ادعای نورایی درست است.\",\n  \"sources\": [\n    W + \"%D9%BE%DB%8C%D8%B1%D9%88%D8%B2\",\n    W + \"%F0%90%AD%AF%F0%90%AD%A9%F0%90%AD%AB%F0%90%AD%A5%F0%90%AD%B0\"\n  ],\n  \"ref_check\": [\n    {\"ref\": \"BRT:862\", \"status\": \"supports\",\n     \"note\": \"BRT.txt line 15553: after *pairi.aoǰastara- Bartholomae writes '— np. usw. pērōz ‚siegreich‘ (aus ir. *pari-auǰə, s. … IFAnz. 10.28; falsch WZKM 9 p.290)'. The arrow Avestan → Persian is Bartholomae's own.\"},\n    {\"ref\": \"SNS:144\", \"status\": \"supports\",\n     \"note\": \"SNS_pages.txt leaf 89 (the printed folio number is OCR'd 'Iff' = ۱۴۴): 'pērōz … [az] pairi.aoǰastara-: … aoǰah- (AiWb. 862)', followed by pērōzgar, pērōzgartar, pērōzgartum — exactly Nourai's chain and his Bartholomae column.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"HRN\", \"where\": \"HRN.txt awk leaf 100, printed p.78, no. 354\", \"stance\": \"contradicts\",\n     \"note\": \"'pērōz, arab. LW. fīrūz ‚siegreich‘; pērōze ‚Türkis‘, arab. LW. fīrōze, fairūzaj. aw. *paiti.raočah-; phlv. pērōd, pērōdkar, pāz. pērōč.' Horn's etymon is the rejected one — exactly as the chart's NOTE reports; but note Horn also documents fīrūz as the Arabic loan-shape, which supports Nourai's extra script فیروز.\"},\n    {\"src\": \"HUB\", \"where\": \"HUB.txt awk leaf 56, printed p.45, no. 354\", \"stance\": \"supports\",\n     \"note\": \"'Np. pērōz ‚Victor, felix, faustus‘ kann nicht = zd. *paiti-raočah- gesetzt werden, da schon das Pehlevi durchweg pērōč (nicht patrōč), resp. pērōz hat in Übereinstimmung mit arm. Peroz, syr. Pērōz, gr. Περώζης, lat. piroses (Ammian).' Hübschmann's rejection of Horn is verbatim what the chart's NOTE claims.\"},\n    {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt p.160\", \"stance\": \"supports\",\n     \"note\": \"'pērōz [pylwc‘] victorious, victor … < *pari-auǰah- … Paz. perōž, NP pērōz' — the Middle Persian link Nourai's chart leaves implicit.\"},\n    {\"src\": \"PHD\", \"where\": \"PHD.txt, grep 'pērōz'\", \"stance\": \"silent\",\n     \"note\": \"MacKenzie's Concise Pahlavi Dictionary gives pērōz only as a lexeme without etymology; no counter-evidence.\"}\n  ]\n})\n\nN.append({\n  \"id\": 4, \"lang\": \"Avestan\", \"words\": \"vaxšaiti, uxšyeiti; vaxš 2, uxs\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"This is the s-extended branch of the root, *h₂wég-s-. Pokorny 85 sets it out word for word: 'dazu mit s im Verbum: ai. vákṣaṇa-m ‚Stärkung‘, vakṣáyati ‚läßt wachsen‘, av. vaxšaiti ‚läßt wachsen‘, woneben mit schwächster Wzstufe ai. ükṣati ‚erstarkt‘, av. uxšyeiti ‚wächst‘'. So vaxšaiti is the full-grade (originally causative *woḱs-eye-, 'makes grow') and uxšyeiti the zero-grade -ya- present ('grows'); Nourai's single gloss 'grows, strengthens, increases' covers both but blurs the causative/intransitive split that Pokorny and Buck draw. The nominal line 'vaxš 2, uxs : growth' is the bare verbal stem used as a noun-root (Av. vaxš-, MP waxš 'growth'); Nourai's '2' is his own homonym number, distinguishing it from the unrelated Iranian waxš 'word, spirit'. Same Germanic equation: Goth. wahsjan = Skt. vakṣáyati.\",\n  \"derivation_fa\": \"این گره شاخهٔ sدار ریشه (*h₂wég-s-) است. پوکورنی در ص ۸۵ تصریح می‌کند: «اوستایی vaxšaiti ‚می‌رویاند‘، در برابر آن با پایهٔ ضعیف uxšyeiti ‚می‌روید‘»، برابر سنسکریت vakṣáyati و ükṣati. پس vaxšaiti در اصل سببی («رویاندن») و uxšyeiti لازم («روییدن») است و معنای یکدستی که نورایی داده این تمایز را پوشانده است. دو صورت اسمی vaxš و uxs همان ستاک فعلی در کاربرد اسمی است؛ عدد ۲ در «vaxš 2» شمارهٔ هم‌نگارهٔ خود نورایی است تا از وخش «سخن، روان» جدا شود. ادعای نورایی درست است.\",\n  \"sources\": [W + \"Reconstruction:Proto-Indo-European/h%E2%82%82ewg-\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:84,85\", \"status\": \"supports\",\n     \"note\": \"POK_01.txt leaf 94, p.85: 'ai. vákṣaṇa-m ‚Stärkung‘, vakṣáyati ‚läßt wachsen‘, av. vaxšaiti ‚läßt wachsen‘, woneben mit schwächster Wzstufe ai. ükṣati ‚erstarkt‘, av. uxšyeiti ‚wächst‘'.\"},\n    {\"ref\": \"SYN:876\", \"status\": \"supports\",\n     \"note\": \"SYN.txt §12.53 GROW, printed p.876: '… Skt. ukṣ-, Av. uxṣ- (3sg. pres. uxšyeiti)', under headroot 'IE *aweg-'. Buck's Avestan column for 'grow' reads 'Av. varəd-, rud-, uxš-'.\"},\n    {\"ref\": \"SOD:30\", \"status\": \"supports\",\n     \"note\": \"SOD_pages.txt awk leaf 96 = printed p.30, entry 779: the Sogdian verb is glossed and etymologised '← Av. vaxš-', so Gharib p.30 does cite the Avestan verb Nourai puts here.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"BRT.txt, s.vv. vaxš- / hu.vaxša-\", \"stance\": \"supports\",\n     \"note\": \"Bartholomae has 'j. hu.vaxša- n. ‚gutes Wachstum, Gedeihen‘' (col. 1836) built on the same verbal stem vaxš-.\"},\n    {\"src\": \"IEC\", \"where\": \"IEC.txt line 871 s.v. aueKs-\", \"stance\": \"supports\",\n     \"note\": \"'aueKs- (oueKs-, auKs-, ouKs-) ‘grow; growth’. Cf. aug- … Skt. vaks-, uksami, pf. vavákṣa; Oss. as, asä ‘growth’; Gk. aéxo, aüxo' — Mann's headword is Nourai's s-extended branch.\"},\n    {\"src\": \"ARY\", \"where\": \"ARY_latin_index_pages.txt [pdf page 518], entry وخش / وخشیدن\", \"stance\": \"supports\",\n     \"note\": \"Aryanpur's entry gathers 'UKHSHYEITI (AVESTAN), VAKHSHAITI, UXSH-, UXSHYEITI, WAXSHIDAN, WAXSH- (PAHLAVI), WAHSJAN (GOTHIC), WEAXAN (OLD ENGLISH), AUGERE, AUGEO (LATIN)' and cites 'BUCK: (GROW) 876, 877' — the same Buck pages Nourai cites.\"}\n  ]\n})\n\nN.append({\n  \"id\": 5, \"lang\": \"Avestan\", \"words\": \"vana-vaxša\",\n  \"verdict\": \"disputed\",\n  \"derivation\": \"Av. *vana-vaxša- 'grown in the woods' is NOT an attested Avestan word: it is a conjecture of Friedrich Müller (WZKM 7, 368, 1893) made to explain Pahlavi wanafšag, and Nourai prints it without the asterisk that its status requires. Bartholomae's Altiranisches Wörterbuch, which does have vana- f. 'Baum' (col. ~1345, 'j. vana- f. ‚Baum‘: yaθa mašyayā °nā kasyanhqm vanqm … V.5.24'), has no such compound and no entry approaching it. Hübschmann, Persische Studien no. 231, quotes Müller's proposal and dismisses it in four words: 'Mir nicht wahrscheinlich' ('not probable to me'). Modern lexicography follows Hübschmann: Wiktionary marks Middle Persian wanafšag 'of uncertain origin' and offers no Avestan etymon, and the formal difficulty is plain — a compound *vana-vaxša- would give MP *wanawaxš(ag) or *wanwaxš, not wanafšag with -f-, and the -šag/-saj shape of the word (Arabic banafsaj, Armenian manušak, Syriac) points to a Wanderwort of the eastern-Iranian/Near-Eastern plant-name type rather than to a transparent Avestan compound. The gloss 'pansy, violet' also belongs to the Persian word, not to the reconstructed Avestan one.\",\n  \"derivation_fa\": \"صورت *vana-vaxša- «روییده در جنگل» در اوستا هیچ شاهدی ندارد و بازساختهٔ فریدریش مولر (۱۸۹۳) است؛ نورایی ستارهٔ بازساخت را حذف کرده و آن را چون واژه‌ای مضبوط آورده است. بارتولومه هرچند vana- «درخت» را دارد، چنین مرکبی ندارد، و هوبشمان در مطالعات فارسی، شمارهٔ ۲۳۱، آن را با جملهٔ «به نظر من محتمل نیست» رد کرده است. امروز نیز ویکی‌واژه خاستگاه wanafšag را «نامعلوم» می‌داند؛ افزون بر این، از *vana-vaxša- باید در فارسی میانه *wanawaxšag می‌آمد نه wanafšag با ف، و صورت‌های عربی بنفسج و ارمنی manušak بیشتر به یک واژهٔ گیاهی دوره‌گرد می‌ماند تا مرکبی روشن و اوستایی. پژوهش امروزی این بند از نمودار را نمی‌پذیرد.\",\n  \"sources\": [W + \"%D8%A8%D9%86%D9%81%D8%B4%D9%87\", W + \"%D8%A8%D9%86%D9%81%D8%B3%D8%AC\"],\n  \"ref_check\": [\n    {\"ref\": \"AEF:291\", \"status\": \"not_checked\",\n     \"note\": \"AEF = Khaleqi Motlaq's Persian version of Horn/Hübschmann, 'Asas-e Eshteqaq-e Farsi' vol. I; refs_online.json records it as not online, and no copy is on disk. Indirect corroboration that the page number is right: Mo'in's own footnote to بنفشه in Borhan-e Qate' cites 'اسفا ۱: ص ۲۹۱' (OCR 'اسفا۷:۱ص۲4'), i.e. exactly AEF p.291 — Nourai took the citation from there. The German original (HRN no. 231) gives only the forms, no etymology.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"BRT.txt, grep 'vana-vax|vana.vax' — no hit; the nearest headword is line 22633 'j. vana- f. ‚Baum‘'\", \"stance\": \"contradicts\",\n     \"note\": \"Bartholomae, who collects every Avestan compound, has no *vana-vaxša-; the compound is therefore unattested, not merely rare.\"},\n    {\"src\": \"HUB\", \"where\": \"HUB.txt line 1029, printed p.31, no. 231\", \"stance\": \"contradicts\",\n     \"note\": \"'Np. bunafšə ‚Veilchen‘ = phl. vanavšak (für vanafšak) nach Fr. Müller WZKM. 7, 368 = zd. *vanavaxša- (also = ‚im Walde wachsend‘). Mir nicht wahrscheinlich.'\"},\n    {\"src\": \"HRN\", \"where\": \"HRN.txt printed p.~47, no. 231\", \"stance\": \"silent\",\n     \"note\": \"'benefše ‚Veilchen‘, bunefse, binefse; bunefs ‚blau‘ … phlv. vanawsak, vanawsa ‚Veilchen‘ (Bund.); ar. LW. banafsaj, syr. LW. …, arm. LW. manušak.' Horn lists the forms and the loans but proposes NO Avestan etymology — he does not support the arrow.\"}\n  ]\n})\n\nN.append({\n  \"id\": 6, \"lang\": \"Pahlavi\", \"words\": \"vana-vašak\",\n  \"verdict\": \"disputed\",\n  \"derivation\": \"The Pahlavi word itself is real and well attested: MacKenzie, Concise Pahlavi Dictionary p.91, 'wanafšag [wnpšk‘ | N bunafša] violet'. What is disputed is the analysis that the chart draws — the arrow from a supposed Avestan *vana-vaxša-. Nourai's spelling 'vana-vašak' is Hübschmann's transcription vanavšak of the Pahlavi <wnpšk'>, hyphenated so as to display Müller's segmentation vana + vašak; but Hübschmann himself adds '(für vanafšak)', i.e. the manuscript spelling with <p> is to be read f, and the standard modern reading is wanafšag. The book's own NOTE, 'HUB:33 doubts this derivation', is materially accurate (the doubt is real, though it stands at Hübschmann p.31, no. 231, not p.33), and modern scholarship has come down on Hübschmann's side: Wiktionary's Middle Persian entry gives wanafšag as 'of uncertain origin', citing MacKenzie 1971 and Steingass and offering no Iranian compound. Verdict: the node's word is right, its parentage is not established.\",\n  \"derivation_fa\": \"خود واژهٔ فارسی میانه اصیل است: مکنزی در ص ۹۱ می‌آورد «wanafšag [wnpšk‘] بنفشه». آنچه محل اختلاف است پیوند آن با *vana-vaxša- اوستایی است. ضبط «vana-vašak» در کتاب، همان خوانش vanavšak هوبشمان است که برای نمایش تجزیهٔ مولر دونیم شده؛ خود هوبشمان می‌افزاید «به جای vanafšak»، یعنی خوانش درست همان wanafšag است. یادداشت نمودار («هوبشمان در ص ۳۳ در این اشتقاق تردید دارد») درست است، جز آنکه این تردید در ص ۳۱ (شمارهٔ ۲۳۱) آمده نه ص ۳۳. پژوهش امروزی جانب هوبشمان را گرفته و خاستگاه این واژه را نامعلوم می‌داند.\",\n  \"sources\": [W + \"%D8%A8%D9%86%D9%81%D8%B4%D9%87\"],\n  \"ref_check\": [\n    {\"ref\": \"AEF:291\", \"status\": \"not_checked\",\n     \"note\": \"Same as node #5: Khaleqi Motlaq's Asas-e Eshteqaq-e Farsi is not digitised. Mo'in's footnote to بنفشه in BQT independently cites اسفا ۱: ص ۲۹۱, so the page reference itself is almost certainly correct.\"},\n    {\"ref\": \"HUB:33\", \"status\": \"supports\",\n     \"note\": \"The doubt Nourai reports is verbatim in Hübschmann, Persische Studien no. 231 — 'Mir nicht wahrscheinlich' — but it stands on printed p.31, not p.33 (HUB.txt awk leaf 42; HUB's own index at line 10310 reads 'banafsa 31.'; p.33 = awk leaf 44 carries nos. 245-253, nothing about the violet). Substance supported, page off by two.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"PHD.txt awk leaf 113 ≈ printed p.91\", \"stance\": \"partial\",\n     \"note\": \"'wanafšag [wnpšk‘ | N bunafša] violet' — MacKenzie confirms the word and the Persian descendant but gives no Avestan source and no compound analysis.\"},\n    {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt, grep 'wanafs|vanafs' — no hit\", \"stance\": \"silent\",\n     \"note\": \"The plant name does not occur in Nyberg's glossary to the Manual of Pahlavi texts.\"},\n    {\"src\": \"HUB\", \"where\": \"HUB p.31 no. 231\", \"stance\": \"contradicts\",\n     \"note\": \"Hübschmann accepts the Pahlavi form vanavšak/vanafšak as the source of NP banafše but rejects Müller's Avestan compound.\"},\n    {\"src\": \"HRN\", \"where\": \"HRN no. 231\", \"stance\": \"partial\",\n     \"note\": \"'phlv. vanawsak, vanawsa ‚Veilchen‘ (Bund.)' — Horn documents the Pahlavi word (from the Bundahišn) without deriving it.\"}\n  ]\n})\n\nN.append({\n  \"id\": 7, \"lang\": \"Persian\", \"words\": \"banafšeh «بنفشه»; banafš «بنفش»\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"This last link of the chain is solid whatever the ultimate origin of the Pahlavi word. NP بنفشه banafše continues MP wanafšag: initial w- regularly becomes b- in New Persian (as in wād > bād, warg > barg), and the MP diminutive/adjectival suffix -ag gives NP -a/-e; MacKenzie's dictionary states the correspondence outright, 'wanafšag … | N bunafša'. Horn no. 231 records the dialect spread that proves the age of the word — benefše / bunefše / binefše, Māzandarānī venewše, and the loans Arabic بنفسج banafsaj, Syriac, Armenian manušak — and Mo'in's footnote in Borhan-e Qate' adds Tabarī vanavša, modern Māzandarānī venevše and Gīlēkī banaūšə, with the botanical identification Viola odorata / Viola tricolor. Mo'in's own dictionary tags the word simply '[په.]', i.e. Pahlavi. The second word, بنفش banafš 'violet(-coloured), dark', is the back-formed colour adjective from the flower name, well attested in the Shahnameh; the couplet Nourai prints under Ferdowsī — 'جهان شد ز گرد سواران بنفش / درخشان سنان و درفشان درفش' — is genuine and is quoted s.v. درفشان in Nushin's Shahnameh glossary. The Arabic بنفسج is a loan FROM Iranian, not the other way round (Wiktionary: 'From Middle Iranian; … compare Middle Persian wnpšk‘').\",\n  \"derivation_fa\": \"این حلقهٔ پایانی زنجیره، هر چه خاستگاه نهایی واژه باشد، استوار است. «بنفشه» از فارسی میانهٔ wanafšag آمده است: و اول در فارسی نو قاعده‌مند به ب بدل می‌شود (مانند wād > باد و warg > برگ) و پسوند -ag به ــه بدل می‌گردد؛ مکنزی همین تناظر را صریح آورده است. هرن گونه‌های بنفشه/بنفسه/بنفشه و مازندرانی venewše را برمی‌شمارد و معین در حاشیهٔ برهان قاطع طبری vanavša و گیلکی banaūšə را می‌افزاید؛ در فرهنگ معین نیز واژه با نشانهٔ [په.] آمده است. «بنفش» صفت رنگی برساخته از نام گل است و بیت فردوسی که نورایی آورده در واژه‌نامک نوشین ذیل «درفشان» عیناً نقل شده است. عربی بنفسج معرّب همین واژهٔ ایرانی است نه برعکس. ادعای نورایی در این گره درست است.\",\n  \"sources\": [\n    W + \"%D8%A8%D9%86%D9%81%D8%B4%D9%87\",\n    W + \"%D8%A8%D9%86%D9%81%D8%B3%D8%AC\",\n    \"https://abadis.ir/fatofa/%D8%A8%D9%86%D9%81%D8%B4%D9%87/\"\n  ],\n  \"ref_check\": [\n    {\"ref\": \"AEF:291\", \"status\": \"not_checked\",\n     \"note\": \"Not digitised; but Mo'in's footnote on the very Borhan page Nourai cites refers to 'اسفا ۱: ص ۲۹۱', confirming that AEF p.291 is indeed the entry بنفشه.\"},\n    {\"ref\": \"BQT:308\", \"status\": \"supports\",\n     \"note\": \"BQT_v1_pages.txt line 21100 ff. (awk leaf 529; the same page carries the cross-references ص ۳۰۵ / ۳۰۷ / ۳۰۹, so the printed page is 308): 'بنفشه … گلی باشد معروف و طبیعت آن سرد و تر است در دوم و سوم؛ و معرّب آن بنفسج باشد' with Mo'in's footnote '۱ – پهلوی vanafšak … طبری vanavša، مازندرانی کنونی venevše … گیلکی banaūšə … بنفشه Violettes … بنفشهٔ معطر Viola odorata'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"PHD.txt ≈ p.91 s.v. wanafšag\", \"stance\": \"supports\",\n     \"note\": \"'wanafšag [wnpšk‘ | N bunafša] violet' — MacKenzie himself equates the Pahlavi and the New Persian word.\"},\n    {\"src\": \"HRN\", \"where\": \"HRN.txt printed p.~47, no. 231\", \"stance\": \"supports\",\n     \"note\": \"'benefše ‚Veilchen‘, bunefse, binefse; bunefs ‚blau‘ (Šahn. I, 48 Vers 265, 107 Vers 839); māz. venewse; phlv. vanawsak' — Horn documents BOTH of Nourai's words, including the adjective banafš 'blue/dark' with Shahnameh line references.\"},\n    {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' ed. Mo'in, p.308, s.v. بنفشه (and بنفش on the same page, 'رنگ کبود مانند رنگ بنفشه')\", \"stance\": \"supports\",\n     \"note\": \"See ref_check; the entry also gives معرّب آن بنفسج, i.e. Arabic banafsaj is the Arabised form of the Persian word, as Wiktionary now says.\"},\n    {\"src\": \"MON\", \"where\": \"Farhang-e Mo'in via abadis.ir s.v. بنفشه\", \"stance\": \"supports\",\n     \"note\": \"Mo'in's entry is tagged '(بَ نَ ش ِ ) [ په . ]' — origin Pahlavi, exactly the parentage of this node.\"},\n    {\"src\": \"FSF\", \"where\": \"FSF_pages.txt line 11556-11559, s.v. درفشان\", \"stance\": \"supports\",\n     \"note\": \"Nushin's Vazhe-namak quotes the identical couplet 'جهان شد زگرد سواران بنفش / درخشان سنان و درفشان درفش' — Nourai's Ferdowsī citation is genuine.\"},\n    {\"src\": \"ARY\", \"where\": \"ARY_pages.txt, grep 'بنفشه' — no hit\", \"stance\": \"silent\",\n     \"note\": \"Aryanpur's Indo-European root dictionary has no entry for the violet, consistent with the word not having a secure IE etymology.\"}\n  ]\n})\n\nN.append({\n  \"id\": 8, \"lang\": \"Old Persian\", \"words\": \"vaxš; u-vaxštra\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Kent, Old Persian, Lexicon p.177 — exactly Nourai's page — reads: 'Uvaxštra- sb. ‘Cyaxares’, former King of Media: Elam. ma-ak-šš-tar-ra, Akk. ú-ma-ku-iš-tar, Gk. Κυαξάρης. From u- ‘good’ + vaxštra- ‘growth’ …, to vaxš-, Av. vaxš-, Skt. vakṣ-, Gm. wachsen, N Eng. wax: ‘Having good growth’. So Bthl. AiW 1836; but Hz. ApI 209 interprets ‘having good oversight’.' Bartholomae, AiW col. 1836, has the same: 'p. *u.vaxštra- m. EN. eines medischen Königs, Κυαξάρης … Eig. ‚von gutem Wuchs‘; *vaxštra- n.' The name occurs four times in the Behistun inscription (DB 2.15f, 2.81; 4.19, 22) in the phrase Uvaxštrahyā taumāyā 'of the family of Cyaxares', used by the pretenders Phraortes and Cicantakhma. Two caveats Nourai does not flag: (a) the verb vaxš- itself is NOT independently attested in Old Persian — Kent abstracts it from the name and from Avestan; (b) the name is Median, not Persian proper: Kent §679 explains that 'ṭr after spirants … appears unchanged in Avestan. This seems to have been the development also in Median, as in the name of the Mede Uvaxštra-', whereas true Old Persian would have given -ç-. So the box's label 'Old Persian' means 'Old Persian inscriptional form of a Median name'. Nourai's 'u-vaxštra' is Kent's and Bartholomae's segmentation, and 'well grown (a male name)' is their gloss.\",\n  \"derivation_fa\": \"کنت در فرهنگ پارسی باستان، ص ۱۷۷ — همان صفحه‌ای که نورایی یاد کرده — می‌نویسد: «Uvaxštra- ، هخشتره، پادشاه ماد؛ از u- ‚نیک‘ و vaxštra- ‚بالش، رویش‘ از ریشهٔ vaxš- ، اوستایی vaxš-، سنسکریت vakṣ-، آلمانی wachsen؛ یعنی ‚نیک‌بالیده‘»، و به بارتولومه (ستون ۱۸۳۶) ارجاع می‌دهد که همان را «از رویش نکو» معنی کرده است. این نام چهار بار در سنگ‌نبشتهٔ بیستون در عبارت Uvaxštrahyā taumāyā «از تخمهٔ هوخشتر» آمده است. دو نکته را نورایی نگفته است: نخست آنکه خود فعل vaxš- در پارسی باستان شاهد مستقل ندارد و از همین نام بازسازی شده؛ دوم آنکه صورت نام مادی است نه پارسی باستانی اصیل، زیرا -tr- پس از سایشی در پارسی باستان باید به ــç می‌رسید (کنت §۶۷۹). با این دو قید، ادعای نورایی درست است.\",\n  \"sources\": [\"https://en.wikipedia.org/wiki/Cyaxares\"],\n  \"ref_check\": [\n    {\"ref\": \"KNT:177\", \"status\": \"supports\",\n     \"note\": \"KNT.txt awk leaf 200 — the leaf on which the printed page number '177' appears — line 5205: 'Uvaxštra- sb. ‘Cyaxares’ … From u- ‘good’ + vaxštra- ‘growth’ (§9.II, §79, §148.II), to vaxš-, Av. vaxš-, Skt. vakṣ-, Gm. wachsen, N Eng. wax (§102): ‘Having good growth’ … So Bthl. AiW 1836.' Both of Nourai's words are on the page he cites.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"BRT.txt line ~30476, col. 1836\", \"stance\": \"supports\",\n     \"note\": \"'p. *u.vaxštra- m. EN. eines medischen Königs, Κυαξάρης … Eig. ‚von gutem Wuchs‘; *vaxštra- n.' — and immediately above it 'j. hu.vaxša- n. ‚gutes Wachstum, Gedeihen‘', the Avestan doublet of the same compound.\"},\n    {\"src\": \"KNT\", \"where\": \"Kent §679 (KNT.txt line 1103)\", \"stance\": \"partial\",\n     \"note\": \"'… the name of the Mede Uvaxštra- ‘Cyaxares’, Elam. ma-ak-iš-ta-ra …' — Kent classes the form as Median, so 'Old Persian' is the language of the inscription rather than of the name.\"},\n    {\"src\": \"TLM\", \"where\": \"TLM.txt (Tolman, Ancient Persian Lexicon)\", \"stance\": \"silent\",\n     \"note\": \"Kent cites 'Tm. Lex. 78' for the name; the local OCR of Tolman was not searchable for the entry.\"}\n  ]\n})\n\nN.append({\n  \"id\": 9, \"lang\": \"Persian\", \"words\": \"Hovaxšatar «هوخشتر»\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"هوخشتر / هووخشتره is the modern Persian rendering of Old Persian/Median Uvaxštra-, the Cyaxares of the Greeks (r. c. 625-585 BCE), the Median king who with Nabopolassar destroyed Nineveh in 612. The important qualification, which the chart's arrow hides, is that this is not an inherited New Persian word: there is no continuous Middle Persian transmission of the name, and هوخشتره is a scholarly re-Persianisation coined in the 19th-20th century directly from the cuneiform form, in the same class as داریوش ‹ Dārayava(h)uš and خشایارشا ‹ Xšayāršā. Nourai's transliteration 'Hovaxšatar' also inserts a vowel that neither the cuneiform nor the usual Persian spelling has (Uvaxštra / هووخشتره Huvaxštra), and his gloss 'king of Media' is a definition of the referent, not of the name, which means 'of good growth'. A further caution: popular sources (e.g. Wikipedia) gloss the name 'good ruler', analysing it as u- + xšaθra- 'rule'; Bartholomae and Kent reject that, since 'good rule' would be *Huxšaθra-, and Justi already noted the variant readings *xšaθarə/*xšāra- (NB 140). Kent records Herzfeld's third proposal, 'having good oversight'.\",\n  \"derivation_fa\": \"«هوخشتر / هووخشتره» صورت فارسی امروزی نام پارسی باستان/مادی Uvaxštra- ، همان کیاکسارِ یونانیان، پادشاه ماد است که در ۶۱۲ پیش از میلاد نینوا را برانداخت. نکتهٔ مهمی که پیکان نمودار پنهان می‌کند این است که این واژه میراثی نیست و از راه فارسی میانه به فارسی نو نرسیده؛ بلکه در دورهٔ جدید مستقیماً از صورت میخی بازساخته شده است، همانی‌گونه که «داریوش» و «خشایارشا». ضبط نورایی (Hovaxšatar) واکه‌ای افزوده دارد که نه در خط میخی هست و نه در املای رایج فارسی؛ و معنای «پادشاه ماد» تعریف مصداق است نه معنای واژه که «نیک‌بالیده» است. افزون بر این، معنای رایج عامیانهٔ «فرمانروای نیک» (از خشثره) را بارتولومه و کنت نمی‌پذیرند. با این قیدها، ادعای نورایی با احتیاط پذیرفتنی است.\",\n  \"sources\": [\"https://en.wikipedia.org/wiki/Cyaxares\"],\n  \"ref_check\": [\n    {\"ref\": \"KNT:177\", \"status\": \"partial\",\n     \"note\": \"Kent p.177 gives the Old Persian name and its analysis and the Greek Κυαξάρης, and lists the attestations Uvaxštrahyā DB 4.19, 22; but he says nothing about a New Persian continuation — the 'Persian' box is Nourai's own addition, not Kent's.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"AiW col. 1836\", \"stance\": \"partial\",\n     \"note\": \"Bartholomae gives the name and the meaning 'von gutem Wuchs' and cites Justi NB 140 for the rival readings *xšaθarə-/*xšāra-; no New Persian form.\"},\n    {\"src\": \"MON\", \"where\": \"Mo'in vol. 5 (a'lām) via vajehyab/abadis — not retrievable for this headword\", \"stance\": \"silent\",\n     \"note\": \"The proper-name volumes of Mo'in are not in the online text, so the modern Persian spelling could not be checked there; Persian Wikipedia and the Encyclopaedia Iranica article 'Cyaxares' (403 for automated fetch) use هووخشتره.\"}\n  ]\n})\n\nN.append({\n  \"id\": 10, \"lang\": \"Sogdian\", \"words\": \"`xwš`y\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"Gharib's Sogdian Dictionary, entry 779 on printed p.30 — exactly Nourai's SOD:30 — reads 'ʾγwšʾy- B, S … (ə)xwašāy (γwšy-) ← Av. vaxš- ⇒ xwš- : (to) grow, (to) increase', with references to TSP 2.358, 359, 778, 886, 905; Frag. Len. 90,6; GMS 428. So the word, the meaning and the derivation from Av. vaxš- are all Gharib's own, and Nourai has simply copied her entry. One discrepancy: Gharib's transliteration of the Buddhist-Sogdian spelling is ʾγwšʾy- with γ (the letter that in this position writes /x/ after the prothetic aleph), while Nourai prints `xwš`y with x, i.e. he has replaced the graphic γ by the phonetic value. The printed page of Nourai (PDF p.70) shows `xwš`y, so the extraction is faithful and the normalisation is the author's, not the scanner's. Phonologically the form is the Sogdian outcome of Old Iranian *waxšaya- with the regular prothetic ə- that Sogdian prefixes to initial consonant clusters and with -šy- → -šāy-.\",\n  \"derivation_fa\": \"فرهنگ سغدی بدرالزمان قریب، مدخل ۷۷۹ در ص ۳۰ — دقیقاً همان ارجاع نورایی — می‌آورد: «ʾγwšʾy-، (ə)xwašāy ، از اوستایی vaxš- ، به معنای روییدن و افزودن». پس هم واژه و هم معنا و هم اشتقاق از خود قریب است. تنها تفاوت در آوانگاری است: قریب صورت نوشتاری را با γ می‌نویسد و نورایی به جای آن x آورده است؛ از روی تصویر صفحهٔ چاپی پیداست که خود کتاب `xwš`y چاپ کرده و خطای خوانش اسکن در کار نیست. از نظر آوایی، این صورت حاصل ایرانی باستان *waxšaya- با واکهٔ آغازین افزوده (ə-) است که در سغدی پیش از خوشهٔ همخوان آغازین می‌آید. ادعای نورایی با این قید صوری پذیرفتنی است.\",\n  \"sources\": [],\n  \"ref_check\": [\n    {\"ref\": \"SOD:30\", \"status\": \"supports\",\n     \"note\": \"SOD_pages.txt awk leaf 96 (0-based leaf 95; printed page ≈ leaf − 66 = 30), entry 779: 'ʾγwšʾy- B, S … (ə)xwašāy ? (γwšy-) ← Av. vaxš- ⇒ xwš- | (to) grow, (to) increase | TSP 2.358, 359, 778, 886, 905; Frag. Len. 90, 6; GMS 428'. Gharib's index (line 90138) lists entry 779 under '(to) grow'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"SOD\", \"where\": \"Gharib, Sogdian Dictionary, entry 779 (p.30)\", \"stance\": \"supports\",\n     \"note\": \"see ref_check — Gharib herself writes '← Av. vaxš-', which is precisely the arrow root → Sogdian that Nourai draws.\"},\n    {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, Dictionary of Khotan Saka (substitute for ISS), grep 'xšāy|vaxš'\", \"stance\": \"silent\",\n     \"note\": \"No Khotanese counterpart was retrieved; the eastern-Iranian evidence for this node rests on Gharib alone.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt (Etymological Dictionary of the Iranian Verb)\", \"stance\": \"silent\",\n     \"note\": \"Cheung's dictionary was searched for a root *waxs-/*uxs-; no entry was retrieved from the local OCR, so his treatment of the verb could not be quoted.\"}\n  ]\n})\n\nN.append({\n  \"id\": 11, \"lang\": \"Germanic\", \"words\": \"wahsan\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"The root connection is beyond doubt — Proto-Germanic *wahsaną 'to grow' (Goth. wahsjan, OE weaxan, OHG wahsan, ON vaxa, NHG wachsen, NE wax) is the exact match of Skt. vakṣáyati and Av. vaxšaiti, i.e. of node #4, and Pokorny 85 prints the equation 'got. wahsjan ‚wachsen‘ (= ai. vakṣáyati, idg. Iter.-Kaus. *wōkseio)'. What is imprecise is the FORM Nourai puts in the box against the gloss 'growth, size'. wahsan is the verb 'to grow'; the noun that means 'growth, size' and that actually yields English waist is the Germanic tu-stem *wahstu-, seen in Goth. wahstus 'stature, growth', OE wæstm, ON vǫxtr, OHG wahst — Pokorny 85 again: 'wozu z. B. got. wahstus ‚Wachstum, Wuchs, Leibesgröße‘'. AHD p.1507, Nourai's own reference, keeps the two apart (the current online version of the same appendix has 'Germanic *wahsan in Old English weaxan, to grow: WAX' beside the separate suffixed noun that gives WAIST). So the book has merged the verb and its derived noun into one line, giving the verb's form with the noun's gloss; the branch itself is right.\",\n  \"derivation_fa\": \"پیوند ریشه‌ای درست است: ژرمنی آغازین *wahsaną «روییدن» (گوتی wahsjan، انگلیسی کهن weaxan، آلمانی wachsen) دقیقاً برابر اوستایی vaxšaiti و سنسکریت vakṣáyati است و پوکورنی در ص ۸۵ همین معادله را می‌آورد. اما صورتی که نورایی در این خانه نهاده دقیق نیست: wahsan فعل است و معنای «رویش، اندازه» و نیز منشأ واژهٔ waist از آنِ اسم *wahstu- است (گوتی wahstus «قامت، بالا»، انگلیسی کهن wæstm). پس کتاب فعل و اسمِ مشتق از آن را در یک سطر آمیخته و صورت فعل را با معنای اسم آورده است؛ خود شاخه درست است.\",\n  \"sources\": [\"https://www.etymonline.com/word/waist\", \"https://www.ahdictionary.com/word/indoeurop.html\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD:1507\", \"status\": \"partial\",\n     \"note\": \"The 1975 New College appendix p.1507 is the aug-¹ entry; the current online version of the same Watkins appendix lists both WAX and WAIST under aug-¹, and Watkins 1985 (AHD_watkins1985.txt line 307) reads '2. Variant extended forms *wogs-, *wegs- in Germanic *wahsan in Old English weaxan, to grow: WAX.' — i.e. AHD gives *wahsan as the verb behind WAX, and reaches WAIST through the separate noun stem, not through wahsan itself.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"POK_01.txt leaf 94, p.85\", \"stance\": \"partial\",\n     \"note\": \"'got. wahsjan ‚wachsen‘ (= ai. vakṣáyati …); anord. vaxa, vexa ‚wachsen‘, ahd. wahsan … wozu z. B. got. wahstus ‚Wachstum, Wuchs, Leibesgröße‘' — Pokorny gives the verb and the noun as distinct formations.\"},\n    {\"src\": \"KLN\", \"where\": \"KLN_1971.txt line 264461 s.v. waist\", \"stance\": \"partial\",\n     \"note\": \"'rel. to OE. wæstm, ON. vǫxtr, Swed. växt, OHG. wahst, ‚growth, increase‘, Goth. wahstus, ‚stature‘, lit. ‚growth‘, and to OE. weahsan, weaxan, ‚to grow‘' — Klein too separates the noun stem from the verb.\"},\n    {\"src\": \"SYN\", \"where\": \"SYN.txt §12.53, p.876 and §12.52 SIZE\", \"stance\": \"supports\",\n     \"note\": \"'Goth. wahsjan, OE weaxan etc. general Gmc. (NE wax of the moon, but mostly arch.)' under IE *aweg-; and at line 12896 'ON ǫxtr, OE wæstm, OHG wahsmo, all orig. ‘growth’, fr. ON vaxa, OE weaxan, OHG wahsan ‘grow’ (12.53)'.\"}\n  ]\n})\n\nN.append({\n  \"id\": 12, \"lang\": \"English\", \"words\": \"waist\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"English waist is Middle English wast (late 14th c., Chaucer), from an unrecorded Old English *wæst beside the attested wæstm 'growth, stature', from Proto-Germanic *wahstu- 'growth, size' — the body's waist being named as 'the (place of) growth', i.e. where the trunk fills out. Klein s.v. waist: 'ME. wast, ‚waist‘, lit. ‚growth‘ (the waist being regarded as the part where the body is best developed), rel. to OE. wæstm, ON. vǫxtr, Swed. växt, OHG. wahst, ‚growth, increase‘, Goth. wahstus, ‚stature‘ … and to OE. weahsan, weaxan, ‚to grow‘.' Etymonline agrees and traces *wahs-tu- to 'PIE *wegs-, extended form of the root *aug- ‘to increase’'. The AHD appendix lists WAIST among the derivatives of aug-¹, so Nourai's citation 'AHD' for this node is right, even though the immediate Germanic ancestor is *wahstu- rather than the verb in his parent box.\",\n  \"derivation_fa\": \"واژهٔ انگلیسی waist «کمر» از انگلیسی میانهٔ wast (اواخر سدهٔ ۱۴ میلادی) و آن از ژرمنی *wahstu- «رویش، قامت» است؛ کمر از آن رو چنین نام گرفته که جای بالیدن تن دانسته می‌شده است. کلاین تصریح می‌کند: «wast ، لغةً ‚رویش‘، خویشاوند با انگلیسی کهن wæstm و گوتی wahstus ‚قامت‘». اتیمولاژی‌آنلاین نیز آن را به *wegs- ، گونهٔ گستردهٔ ریشهٔ *aug- ، می‌رساند و پیوست ریشه‌های هندواروپایی فرهنگ American Heritage هم WAIST را ذیل همین ریشه می‌آورد. ادعای نورایی درست است.\",\n  \"sources\": [\"https://www.etymonline.com/word/waist\", \"https://www.ahdictionary.com/word/indoeurop.html\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"The online AHD Appendix I entry aug-¹ lists among its derivatives: 'wax, waist, nickname, eke, woodwaxen, auction, augend, augment, author, authorize, augur, inaugurate, August, auxiliary, auxin' — WAIST is there.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1971.txt lines 264461-264468 s.v. waist\", \"stance\": \"supports\",\n     \"note\": \"'ME. wast, ‚waist‘, lit. ‚growth‘ … Goth. wahstus, ‚stature‘, lit. ‚growth‘, and to OE. weahsan, weaxan, ‚to grow‘. See wax, ‚to grow‘.'\"},\n    {\"src\": \"SKT\", \"where\": \"SKT.txt, grep 'waist' — only 'girth' (line 7603) and 'waltz' (21335) hit\", \"stance\": \"silent\",\n     \"note\": \"Skeat's Concise edition has no separate waist entry in this OCR; his auction entry (line 1119) does cover the Latin branch.\"},\n    {\"src\": \"SYN\", \"where\": \"SYN.txt line 12896 (§4.30-ish, 'growth' words)\", \"stance\": \"supports\",\n     \"note\": \"'ON ǫxtr, OE wæstm, OHG wahsmo, all orig. ‘growth’, fr. ON vaxa, OE weaxan, OHG wahsan ‘grow’ (12.53)' — Buck documents the noun stem behind waist.\"}\n  ]\n})\n\nN.append({\n  \"id\": 13, \"lang\": \"Latin\", \"words\": \"augěre; augur; augustus; auxilium\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"All four are genuine Latin and all four belong to this root. augeō, augēre 'to increase' is the Latin *h₂ewg-eye- (Pokorny 84: 'lat. augeō, -ere ‚vermehren‘, auctor (= umbr. uhtur) ‚Urheber usw.‘, auctio ‚Versteigerung‘, augmen(tum) ‚Zuwachs‘'). augur, -uris m. is, in Pokorny's account, 'aus *augos ‚Vermehrung‘' — the priest is named from the 'increase' or favourable augmentation he obtains, which is exactly the sense Nourai's gloss 'divine favor' records (Watkins: 'Latin augur, diviner (< “he who obtains favorable presage” < “divine favor, increase”)'). augustus 'majestic, consecrated' is the adjective of the es-stem *aug-os- and is equated by Pokorny with Lith. aūkštas, Latv. aüksts 'high'. auxilium 'aid' is the s-extended *aug-s- formation, 'ursprüngl. Pl. -ia ‚Verstärkungen, Hilfstruppen‘' (Pokorny 85). Ernout-Meillet s.v. augeō confirms the whole family from the Latin side: 'Tels sont augur, auctor, auctoritas, auctoro, auctio, et auxilia.' The only slip is typographical: the book prints 'augěre' with a breve, where the second e of augēre is long.\",\n  \"derivation_fa\": \"هر چهار واژه لاتینی اصیل‌اند و هر چهار به همین ریشه بازمی‌گردند. augeō/augēre «افزودن» بازماندهٔ *h₂ewg-eye- است؛ augur «فال‌گوی رسمی» به گفتهٔ پوکورنی از *augos «افزایش، برکت» است و همین معنای «عنایت ایزدی» را که نورایی آورده توجیه می‌کند؛ augustus «شکوهمند، مقدّس» صفت ستاک -os- است و برابر لیتوانی aūkštas «بلند»؛ و auxilium «یاری» ساختهٔ پایهٔ sدار *aug-s- است که نخست جمع به معنای «نیروهای کمکی» بوده است. ارنو-مییه نیز همین خانواده را یکجا می‌آورد. تنها لغزش کتاب چاپی است: augěre با علامت کوتاهی چاپ شده در حالی که واکهٔ دوم دراز است (augēre). ادعای نورایی درست است.\",\n  \"sources\": [\"https://www.ahdictionary.com/word/indoeurop.html\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD:1507\", \"status\": \"supports\",\n     \"note\": \"AHD_watkins1985.txt line 307 (the same appendix, 1985 standalone edition of the 1975 pp.1505-1550): '3. Form *aug-é- in: Latin augére, to increase … 4. Latin augur, diviner … 5. Latin augustus, majestic, august … 6. Suffixed form *aug-s- in: a. Latin auxilium, aid, support, assistance: AUXILIARY.' All four of Nourai's Latin words, in his order.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"POK_01.txt leaf 94, pp.84-85\", \"stance\": \"supports\",\n     \"note\": \"'lat. augeō, -ere ‚vermehren‘, auctor (= umbr. uhtur) … augur ‚Weissager‘ aus *augos ‚Vermehrung‘ (WH. I 83)'; and p.85 'lat. auxilium ‚Hilfe‘ (ursprüngl. Pl. -ia ‚Verstärkungen, Hilfstruppen‘)'.\"},\n    {\"src\": \"LAT\", \"where\": \"LAT.txt lines 5998-6010 (Ernout-Meillet s.v. augeō, augur)\", \"stance\": \"supports\",\n     \"note\": \"'… des dérivés ou des composés de augeō … Tels sont augur, auctor, auctoritas, auctoro, auctio, et auxilia. augur, -uris m.: augure (prêtre) est un ancien nom du type fulgur/fulguris.'\"},\n    {\"src\": \"IEC\", \"where\": \"IEC.txt line 17313 (Mann, suffix -stos)\", \"stance\": \"supports\",\n     \"note\": \"'Lat. … augustus (‘high’: aug-)'; and at line 15350 'Lat. … auxilium, n. (‘aid’, if for *aug-sil-)'.\"}\n  ]\n})\n\nN.append({\n  \"id\": 14, \"lang\": \"English\", \"words\": \"auction, augment, author; inaugurate; August; auxiliary\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Each of the four lines is the English reflex of the Latin word directly above it in the parent box, and the AHD appendix lists them all under aug-¹. (a) auction ‹ Latin auctio, -ōnis 'an increasing, a sale by increase of bids' (Skeat: 'L. auctionem, acc. of auctio, a sale by auction, lit. an increase, because the sale is to the highest bidder — L. auctus, pp. of augēre'); augment ‹ Late Latin augmentāre from augmentum 'increase', via Old French augmenter, 15th c.; author ‹ Latin auctor 'originator, one who causes to grow', through Anglo-French auctour, Middle English auctour, the -th- being a 16th-c. pseudo-Greek respelling. (b) inaugurate ‹ Latin inaugurāre 'to take omens before installing (a magistrate, a temple)', from in- + augur; the modern sense 'install in office' preserves the Roman ritual. (c) August ‹ Latin (mēnsis) Augustus, the month renamed in 8 BCE for Augustus Caesar, whose own title is the adjective augustus 'consecrated, majestic'; Old English took it as Agustus, re-Latinised in Middle English. (d) auxiliary ‹ Latin auxiliāris, from auxilium. Nourai's grouping is exactly AHD's.\",\n  \"derivation_fa\": \"هر چهار سطر این خانه بازتاب مستقیم واژه‌های لاتینی خانهٔ پیشین است و پیوست ریشه‌های فرهنگ American Heritage همه را ذیل aug- می‌آورد. auction از auctio «افزودن، حراج» (زیرا کالا به بالاترین پیشنهاد می‌رسد)؛ augment از augmentum از راه فرانسهٔ کهن؛ author از auctor «پدیدآورنده» که در سدهٔ ۱۶ با املای یونانی‌نمای th نوشته شد؛ inaugurate از inaugurāre «پیش از نصب فال گرفتن» که هنوز معنای آیینی رومی را در خود دارد؛ August از نام ماه (mēnsis) Augustus که در ۸ پیش از میلاد به نام اگوستوس قیصر نامیده شد و خود لقب او همان صفت augustus است؛ و auxiliary از auxiliāris. ادعای نورایی درست است.\",\n  \"sources\": [\"https://www.ahdictionary.com/word/indoeurop.html\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"Online AHD Appendix I s.v. aug-¹ lists AUCTION, AUGEND, AUGMENT, AUTHOR, AUTHORIZE, AUGUR, INAUGURATE, AUGUST, AUXILIARY, AUXIN — all four of Nourai's lines.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"SKT\", \"where\": \"SKT.txt line 1119 s.v. Auction\", \"stance\": \"supports\",\n     \"note\": \"'Auction. (L.) L. auctionem, acc. of auctio, a sale by auction, lit. ‚an increase‘, because the sale is to the highest bidder. — L. auctus, pp. of augēre, to increase.'\"},\n    {\"src\": \"LAT\", \"where\": \"LAT.txt lines 6007-6008 (Ernout-Meillet s.v. augeō)\", \"stance\": \"supports\",\n     \"note\": \"'… des sens spéciaux tels que la parenté avec augeō n’est souvent plus sensible. Tels sont augur, auctor, auctoritas, auctoro, auctio, et auxilia.' — the Latin bases of auction, author, augur, inaugurate, auxiliary.\"},\n    {\"src\": \"KLN\", \"where\": \"KLN_1966/1971, s.vv. auction, author, august\", \"stance\": \"supports\",\n     \"note\": \"Klein routes all of them through Latin augēre/auctus (the entries were reached by the same grep that produced the waist entry at line 264461); no divergent account.\"}\n  ]\n})\n\nout = {\n  \"pdf_page\": 70,\n  \"book_page\": 40,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [root_entry]\n}\n\n# clean the stray \"src\" key accidentally allowed in one ref_check item\nfor n in out[\"entries\"][0][\"nodes\"]:\n    for rc in n.get(\"ref_check\", []):\n        rc.pop(\"src\", None)\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-70.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk70.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-70.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 70",
 "description": "Write and validate page-70.json"
}
```


### [2026-09-05T05:45:15.534Z] TOOL RESULT

```
written
JSON OK
nodes verified: 14/14
node verdicts: {'confirmed': 9, 'disputed': 2, 'plausible': 3}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 15, 'partial': 3, 'not_checked': 3}
books consulted: {'supports': 25, 'partial': 7, 'silent': 10, 'contradicts': 4} | by book: {'BRT': 6, 'HRN': 4, 'IEC': 3, 'NYB': 3, 'HUB': 3, 'PHD': 3, 'KLN': 3, 'ARY': 2, 'MON': 2, 'POK': 2, 'SYN': 2, 'SKT': 2, 'LAT': 2, 'AHD': 1, 'SNS': 1, 'BQT': 1, 'FSF': 1, 'KNT': 1, 'TLM': 1, 'SOD': 1, 'ISS_alt_DKS': 1, 'CHEUNG': 1}
```


## [2026-09-05T05:45:22.163Z] TOOL CALL #78: Bash

```json
{
 "command": "timeout 300 python3 tools/verify_archive_sources.py 2>&1 | grep -i '70\\|missing\\|MISS' | head -20; echo \"exit=$?\"",
 "description": "Check archived sources for page 70"
}
```


### [2026-09-05T05:45:26.973Z] TOOL RESULT

```
exit=0
```


## [2026-09-05T05:45:29.041Z] TOOL CALL #79: Bash

```json
{
 "command": "timeout 300 python3 tools/verify_archive_sources.py 2>&1 | tail -20",
 "description": "Run archive source verification"
}
```


### [2026-09-05T05:45:33.464Z] TOOL RESULT

```
603 cited URLs, 22 not yet archived
archived 22, failed 0
```


## [2026-09-05T05:45:56.100Z] AGENT

Verification of PDF page 70 (book page 40) is complete: `/home/sfmqrb/git/rishe/data/verification/page-70.json`, `verify_check.py 70` reports 0 PROBLEM lines.

**Page 70 — root `Aueg, Aug, Uog, Ug` (PIE \*h₂ewg- "to increase")**
- Root: **confirmed** (Pokorny 84–85 heads the article with Nourai's exact four variants). 3 redirect entries skipped.
- Nodes 14/14: **confirmed 9** (#1 ugra/aojah, #2 pairi-aojastara, #3 pîrŭz, #4 vaxšaiti/uxšyeiti, #7 banafšeh/banafš, #8 u-vaxštra, #12 waist, #13 Latin, #14 English), **plausible 3**, **disputed 2**.
- Ref checks: 15 supports, 3 partial, 3 not_checked (all three are AEF, Khaleqi Motlaq's *Asas-e Eshteqaq-e Farsi*, which is not digitised anywhere).

**Disputed**
- #5 Avestan `vana-vaxša` "grown in the woods" — unattested; it is Fr. Müller's 1893 conjecture printed without an asterisk. Bartholomae has no such compound; Hübschmann (Pers. St. no. 231) dismisses it: "Mir nicht wahrscheinlich"; Wiktionary calls MP *wanafšag* "of uncertain origin".
- #6 Pahlavi `vana-vašak` — the word is real (MacKenzie p.91 *wanafšag* [wnpšk']), but the arrow from the reconstructed Avestan compound is what modern work rejects. A \*vana-vaxša- would give MP \*wanawaxšag, not *wanafšag*.

**Plausible (with caveats explained in the file)**
- #9 `Hovaxšatar` — a modern scholarly re-Persianisation of Median/OP *Uvaxštra*, not an inherited New Persian word; Nourai's transliteration inserts a vowel the cuneiform lacks.
- #10 Sogdian `` `xwš`y `` — Gharib entry 779 (p.30) prints ʾγwšʾy-; Nourai substitutes the phonetic *x* for her γ. Her entry does say "← Av. vaxš-", so the derivation is hers.
- #11 Germanic `wahsan : growth, size` — the verb's form with the noun's gloss; *waist* comes from \*wahstu- (Goth. *wahstus*), not from *wahsan*.

**Citation slips in the book (not extraction errors)**
- `HUB:33` at node #6 → the doubt is at Hübschmann **p.31**, no. 231 (p.33 carries nos. 245–253).
- `augěre` (node #13) is printed with a breve; the vowel is long (*augēre*).

**No extraction errors.** I rendered PDF p.70 at 300 dpi and checked every questionable form (`pairi-aojastara`, `pari-aužah`, `vana-vašak`, `` `xwš`y ``, `wahsan`, `Hovaxšatar`, `پیروز (فیروز)`): the JSON matches the printed page exactly.

Notable positive finds: SNS leaf 89 (printed ۱۴۴) derives *pērōz* from *pairi.aojastara-* citing "AiWb. 862" — the same two references Nourai gives; Nyberg p.160 and Bartholomae col. 862 both give \*pari-auǰah-; Kent p.177 and Bartholomae col. 1836 both give *Uvaxštra* = "having good growth"; Nushin's *Vazhe-namak* quotes Nourai's Ferdowsī couplet verbatim; and Mo'in's own footnote on Borhan p.308 cites «اسفا ۱: ص ۲۹۱», independently confirming that Nourai's `AEF:291` is the right page. 9 web pages archived via `fetch_source.py`.
