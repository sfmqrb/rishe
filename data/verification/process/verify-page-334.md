# Verification process log — verify-page-334


## [2026-09-07T16:13:01.230Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 334 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-334.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-334.json. Write /home/sfmqrb/git/rishe/data/verification/page-334.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 334` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T16:13:03.334Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T16:13:04.049Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T16:13:04.063Z] TOOL RESULT

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


## [2026-09-07T16:13:04.681Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-334.txt"
}
```


### [2026-09-07T16:13:04.712Z] TOOL RESULT

```
1	=== PDF page 334 (book page 304) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Menth : mouth, to chew  (refs POK:732)
4	#1 (parent #0) [Greek] refs=POK:732; AHD:1529 | math-ya : to chew ; mustax : upper lip ; mastax : mouth ; mastixan : to grind the teeth ; mastixĕ : chewing gum
5	  #2 (parent #1) [Arabic] refs=TAD:69 | mastakî : a resinous plant and its resin used for chewing
6	    #3 (parent #2) [Persian] refs=MON:4173 | mastakî «مصطکی» : a resinous plant and its chewable resin
7	  #4 (parent #1) [English] refs=AHD | mustache
8	#5 (parent #0) [Germanic] refs=AHD | muntha : mouth
9	  #6 (parent #5) [English] refs=AHD | mouth
10	--- entry 1 ---
11	ROOT [Indo-European] Menth, Meth : to turn, stir  (refs POK:732)
12	#1 (parent #0) [Avestan] refs=POK:732; BQT:2040; FSF:311 | mant 1 : to stir, turn ; mant 2, vant : in control, owner | NOTE: The link of "mant 2: owner" and "mant 1: stir" is unclear unless "stir" means "to be in control".
13	  #2 (parent #1) [Pahlavi] refs=BQT:2040 | mand, omand : owner, with, like
14	    #3 (parent #2) [Persian] refs=BQT:2040; FSF:311 | mand «ـمند» : (suffix) owner of, with | extra: ارجمند ، دانشمند ، هنرمند ، نیازمند
15	دانشومند ، برومند ، خردومند ، نیازومند
16	#4 (parent #0) [Latin] refs=POK:732 | manphur, manfur : lathe, a lathed object
17	  #5 (parent #4) [French] refs=AHD:793 | mandrin : lathe
18	    #6 (parent #5) [English] refs=AHD:793 | mandrel, mandril
19	--- entry 2 ---
20	ROOT [Indo-European] Mer 1, Smer : to remember, be anxious about  (refs POK:969)
21	#1 (parent #0) [Avestan] refs=MON; KLN:961; FFD:64 | mar 1, smer : to remember ; mar-aiti, hiš-mar-aiti : counted for ; â-mar : (count) to remember ; vi-mar : designate (off) ☞Wi
22	  #2 (parent #1) [Persian] refs=HUB:95; HRN:208; BQT:1834,1978 | mar «مَر» : account, count, number ; âmâr «آمار» : census ; šemordan «شمردن ( شمار ، شمارش ، شماره )» : to count ; gomârdan «گماردن ( گماشتن ، گماشته )» : designate
23	#3 (parent #0) [Sogdian] refs=SOD:69 | `šm`r` : thought, imagination
24	#4 (parent #0) [Latin] refs=AHD | me-mor : mindful
25	  #5 (parent #4) [English] refs=AHD | memory, remember
26	#6 (parent #0) [Different Languages] refs=AHD; KLN:943 | 
27	  #7 (parent #6) [English] refs=None | martyr, mourn
28	
```


## [2026-09-07T16:13:07.107Z] AGENT

I'll start by reading the source JSON and reference infrastructure.


## [2026-09-07T16:13:08.540Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-334.json | head -200",
 "description": "Read page 334 source JSON"
}
```


## [2026-09-07T16:13:09.016Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-07T16:13:09.956Z] TOOL RESULT

```
{
    "pdf_page": 334,
    "book_page": 304,
    "entries": [
        {
            "root": {
                "name": "Menth",
                "lang": "Indo-European",
                "refs": "POK:732",
                "gloss": "mouth, to chew"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Greek",
                    "refs": "POK:732; AHD:1529",
                    "words": [
                        {
                            "translit": "math-ya",
                            "gloss": "to chew",
                            "script": null
                        },
                        {
                            "translit": "mustax",
                            "gloss": "upper lip",
                            "script": null
                        },
                        {
                            "translit": "mastax",
                            "gloss": "mouth",
                            "script": null
                        },
                        {
                            "translit": "mastixan",
                            "gloss": "to grind the teeth",
                            "script": null
                        },
                        {
                            "translit": "mastix\u0115",
                            "gloss": "chewing gum",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 1,
                    "lang": "Arabic",
                    "refs": "TAD:69",
                    "words": [
                        {
                            "translit": "mastak\u00ee",
                            "gloss": "a resinous plant and its resin used for chewing",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 2,
                    "lang": "Persian",
                    "refs": "MON:4173",
                    "words": [
                        {
                            "translit": "mastak\u00ee",
                            "gloss": "a resinous plant and its chewable resin",
                            "script": "\u0645\u0635\u0637\u06a9\u06cc"
                        }
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
                        {
                            "translit": "mustache",
                            "gloss": null,
                            "script": null
                        }
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
                        {
                            "translit": "muntha",
                            "gloss": "mouth",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 6,
                    "parent": 5,
                    "lang": "English",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "mouth",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                }
            ]
        },
        {
            "root": {
                "name": "Menth, Meth",
                "lang": "Indo-European",
                "refs": "POK:732",
                "gloss": "to turn, stir"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Avestan",
                    "refs": "POK:732; BQT:2040; FSF:311",
                    "words": [
                        {
                            "translit": "mant 1",
                            "gloss": "to stir, turn",
                            "script": null
                        },
                        {
                            "translit": "mant 2, vant",
                            "gloss": "in control, owner",
                            "script": null
                        }
                    ],
                    "note": "The link of \"mant 2: owner\" and \"mant 1: stir\" is unclear unless \"stir\" means \"to be in control\".",
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 1,
                    "lang": "Pahlavi",
                    "refs": "BQT:2040",
                    "words": [
                        {
                            "translit": "mand, omand",
                            "gloss": "owner, with, like",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 2,
                    "lang": "Persian",
                    "refs": "BQT:2040; FSF:311",
                    "words": [
                        {
                            "translit": "mand",
                            "gloss": "(suffix) owner of, with",
                            "script": "\u0640\u0645\u0646\u062f"
                        }
                    ],
                    "script_extra": "\u0627\u0631\u062c\u0645\u0646\u062f \u060c \u062f\u0627\u0646\u0634\u0645\u0646\u062f \u060c \u0647\u0646\u0631\u0645\u0646\u062f \u060c \u0646\u06cc\u0627\u0632\u0645\u0646\u062f\n\u062f\u0627\u0646\u0634\u0648\u0645\u0646\u062f \u060c \u0628\u0631\u0648\u0645\u0646\u062f \u060c \u062e\u0631\u062f\u0648\u0645\u0646\u062f \u060c \u0646\u06cc\u0627\u0632\u0648\u0645\u0646\u062f",
                    "note": null,
                    "quote": {
                        "text": "\u0645\u0646 \u0646\u06cc\u0627\u0632\u0648\u0645\u0646\u062f \u062a\u0648\u06af\u0634\u062a\u0645 \u0648 \u0647\u0631\u06a9\u0648 \u0634\u062f \u0686\u0646\u06cc\u0646 - \u0639\u0627\u0634\u0642 \u0646\u0627\u0632 \u062a\u0648\u060c \u0645\u06cc \u0632\u06cc\u0628\u062f\u0634 \u0647\u0631 \u06af\u0648\u0646\u0647 \u0646\u06cc\u0627\u0632",
                        "poet": "Man\u00fbchehr\u00ee"
                    }
                },
                {
                    "id": 4,
                    "parent": 0,
                    "lang": "Latin",
                    "refs": "POK:732",
                    "words": [
                        {
                            "translit": "manphur, manfur",
                            "gloss": "lathe, a lathed object",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
```


### [2026-09-07T16:13:09.987Z] TOOL RESULT

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


## [2026-09-07T16:13:17.329Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-334.json | sed -n '200,400p'",
 "description": "Rest of source JSON"
}
```


### [2026-09-07T16:13:18.642Z] TOOL RESULT

```
                    "quote": null
                },
                {
                    "id": 5,
                    "parent": 4,
                    "lang": "French",
                    "refs": "AHD:793",
                    "words": [
                        {
                            "translit": "mandrin",
                            "gloss": "lathe",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 6,
                    "parent": 5,
                    "lang": "English",
                    "refs": "AHD:793",
                    "words": [
                        {
                            "translit": "mandrel, mandril",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                }
            ]
        },
        {
            "root": {
                "name": "Mer 1, Smer",
                "lang": "Indo-European",
                "refs": "POK:969",
                "gloss": "to remember, be anxious about"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Avestan",
                    "refs": "MON; KLN:961; FFD:64",
                    "words": [
                        {
                            "translit": "mar 1, smer",
                            "gloss": "to remember",
                            "script": null
                        },
                        {
                            "translit": "mar-aiti, hi\u0161-mar-aiti",
                            "gloss": "counted for",
                            "script": null
                        },
                        {
                            "translit": "\u00e2-mar",
                            "gloss": "(count) to remember",
                            "script": null
                        },
                        {
                            "translit": "vi-mar",
                            "gloss": "designate (off)",
                            "script": null,
                            "see": [
                                "Wi"
                            ]
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 1,
                    "lang": "Persian",
                    "refs": "HUB:95; HRN:208; BQT:1834,1978",
                    "words": [
                        {
                            "translit": "mar",
                            "gloss": "account, count, number",
                            "script": "\u0645\u064e\u0631"
                        },
                        {
                            "translit": "\u00e2m\u00e2r",
                            "gloss": "census",
                            "script": "\u0622\u0645\u0627\u0631"
                        },
                        {
                            "translit": "\u0161emordan",
                            "gloss": "to count",
                            "script": "\u0634\u0645\u0631\u062f\u0646 ( \u0634\u0645\u0627\u0631 \u060c \u0634\u0645\u0627\u0631\u0634 \u060c \u0634\u0645\u0627\u0631\u0647 )"
                        },
                        {
                            "translit": "gom\u00e2rdan",
                            "gloss": "designate",
                            "script": "\u06af\u0645\u0627\u0631\u062f\u0646 ( \u06af\u0645\u0627\u0634\u062a\u0646 \u060c \u06af\u0645\u0627\u0634\u062a\u0647 )"
                        }
                    ],
                    "note": null,
                    "quote": {
                        "text": "\u0627\u06af\u0631 \u0686\u0646\u062f \u0628\u0627 \u0645\u0627 \u0628\u0633\u06cc \u0644\u0634\u06a9\u0631 \u0627\u0633\u062a - \u0627\u0632\u06cc\u0646 \u0632\u0627\u0648\u0644\u06cc \u0631\u0646\u062c \u0645\u0627 \u0628\u06cc \u0645\u0631 \u0627\u0633\u062a",
                        "poet": "Asad\u00ee"
                    }
                },
                {
                    "id": 3,
                    "parent": 0,
                    "lang": "Sogdian",
                    "refs": "SOD:69",
                    "words": [
                        {
                            "translit": "`\u0161m`r`",
                            "gloss": "thought, imagination",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 4,
                    "parent": 0,
                    "lang": "Latin",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "me-mor",
                            "gloss": "mindful",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 5,
                    "parent": 4,
                    "lang": "English",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "memory, remember",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 6,
                    "parent": 0,
                    "lang": "Different Languages",
                    "refs": "AHD; KLN:943",
                    "words": [],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 7,
                    "parent": 6,
                    "lang": "English",
                    "refs": null,
                    "words": [
                        {
                            "translit": "martyr, mourn",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                }
            ]
        }
    ]
}
```


## [2026-09-07T16:13:19.733Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','TAD','MON','BQT','FSF','KLN','HUB','HRN','SOD','FFD','WLD','IEC','SYN','BRT','PHD','NYB','ARY','CHEUNG','LEW','LAT','SKT','PLA','AFM','FVQ','LKT']:\n    if k in d: print(k, json.dumps(d[k], ensure_ascii=False)[:600]); print()\n\"",
 "description": "Ref lookup info"
}
```


### [2026-09-07T16:13:21.186Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; insi

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offs

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries:
```


## [2026-09-07T16:13:27.834Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(d['POK']['page_offset']); print(d['POK'].get('lookup_hint'))\nprint('---AHD---'); print(d['AHD'].get('page_offset')); print(d['AHD'].get('lookup_hint'))\nprint('---TAD---'); print(d['TAD'].get('page_offset')); print(d['TAD'].get('lookup_hint'))\nprint('---MON---'); print(d['MON'].get('page_offset')); print(d['MON'].get('lookup_hint'))\nprint('---BQT---'); print(d['BQT'].get('page_offset')); print(d['BQT'].get('lookup_hint'))\nprint('---FSF---'); print(d['FSF'].get('page_offset'))\nprint('---FFD---'); print(d['FFD'].get('page_offset'))\nprint('---SOD---'); print(d['SOD'].get('page_offset'))\n\"",
 "description": "Page offsets detail"
}
```


### [2026-09-07T16:13:29.148Z] TOOL RESULT

```
POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
---AHD---
1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).
---TAD---
86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image
Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.
---MON---
None
Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).
---BQT---
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
---FSF---
484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking
---FFD---
115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X).
---SOD---
printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes)
```


## [2026-09-07T16:13:33.686Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'lemma: menth\\|lemma: meth\\|lemma: (s)mer\\|lemma: smer\\|lemma: mer-' POK_full.txt | head -40",
 "description": "Grep Pokorny full for lemmas"
}
```


### [2026-09-07T16:13:33.730Z] TOOL RESULT

```
40298:It seems that from Root / lemma: g^hder- : to run, flow, derived Root / lemma: mer-5, 
58134:< kw\; alb. proves that from Root / lemma: mer-2, *extended mer-ek-\ "to shimmer, shine' 
60116:Root / lemma: mer-4, mera- 
60176:Root / lemma: mer-5, mera- 
60183:Root / lemma: mer-5, mera-\ to rub, wipe; to pack, rob, derived from extended Root/ 
60285:It seems that from Root / lemma: g^hder- : to run, flow, derived Root / lemma: mer-5, 
60313:Root / lemma: mer-6, mer-s- 
78543:Root / lemma: smerd-, smord- 
78564:Root / lemma: smeru- 
78586:Root / lemma: (s)mer-
```


## [2026-09-07T16:13:34.571Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==388||NR==389' POK_02.txt | head -80",
 "description": "Pokorny p732 leaf"
}
```


### [2026-09-07T16:13:35.889Z] TOOL RESULT

```
mnti-)]  mentum  ,Kinn,  Gebäudevorsprung',  mit  cymr.  mar\i ,Kinnlade,  Mund'  als  *mnto-  gleichsetzbar  (daraus  mir.  mant  ,die  Stelle eines  ausgefallenen  Zahnes,  Zahnfleisch');  abret. -monit^,  umgelautet  cymr. mynydd,  corn.  meneth,  bret.  menez  ,Berg'  (*moniio-),  cymr.  gor-fynydd , Aufstieg*  (formell  ==  air.  formna  , Schulter');  s.  auch  unter  2.  menth--
aisl.  menir  , Dachfirst'  (dehnstufig  neben  kelt.  *möniio-),  möna  , empor, ragen' ;
verwandt  ist  wahrscheinlich  *mono-  , Nacken,  Hals'.
WP.  II  263,  WH.  II  73  f,  90,  108  f.
2.  znen-  ,treten,  zertreten,  zusammendrücken'.  .  J
Ai.  carma-mnäs  Nom.  PL  , Gerber';  äol.  y^ccreiaai  , tretende'  (V^^^'Jf^t), (,iaTSi'  TtaieX  Hes.,  Denom.  von  einem  mn-tös  , getreten';  cymr.  mathru ,mit  Füßen  treten',  bret.  mantra  ds.  {*-mntr-),  gall.  -mantalon  (^gestampfter) ,Weg'  in  Petro-mantalon  , vierfache  Straße'  (=  Petru-),  Mantalo-magu$ , Straßenfeld',  phryg.  ON  MavraXog;  auch  mir.  men  f.  ,Mehl,  Staub';  lit. minii,  mznti  , treten,  Flachs  brechen,  Felle  gerben',  lett.  min?^,  mit  , treten, gerben';  abg.  *m'bng,  meti  , zusammendrücken',  russ.  mnu,  mjatb  , brechen (Flachs  oder  Hanf),  kneten,  treten  (Lehm),  zerknittern,  zerknüllen';
gr.  (^vLOv  jMoos,  Meergras'  ((xvLagög,  ^viösig  , moosig'),  uvöog,  (xvovg (*(.ivöfog)  , weicher  Flaum',  (j.volov'  (.lalaycöv  Hes.,  lit.  mmiava  , Flachs- seide, Filzgras'.
WP.  II  263,  Vendryes  BSL  38,  113f.,  Trautmann  185.
3.  men-  , denken,  geistig  erregt  sein' ;   erweitert  meng-  :  mnä-  und  mne-,
nienei-  :  nieni-]  Nominalbildungen:  men-raen-  n.,  znenos-  n.,  men-ti-^ men-tu-,  nioni-,  znn-ti-,  mn-to-  ,Sinn,  Gedanke',  men-ter-  , Denker'. Ai.  mdnyate  , denkt',  av.  mainyeite  ds.,  ap.  mainyähay  (idg.  *men-i-0', =  gr.  {.laivofxai  ,rase',  air.  -muiniur,  slav.  mhnjq  , meine,'  s.  unten),  ai.  Perf. ma-mne,  mene^  manäy-ati  ,ist  eifrig',  manä-yu-  , eifrig,  fromm',  manl-sä ,Weisheit,  Verstand ;  Andacht,  Gebet'  (*m^nei-  :  m^ni-) ;  ai.  mannte  , denkt'; mdnati  , erwähnt'  (=  lit.  menü,  poln.  -mione,  öech.  -menu);  0.1.  mandyati  ,ehrt , ( :  lit.  is-monis  , Verstand'),  av.  manaydn  ,man  könnte  glauben' ;  Supin.  ai.
727
„idntum,   Partiz.  Perf.  matd-  ,gedacht'  (=  gr.  aiTÖ-^arog,   lat.  commentus, lit.  mifitas,  air.  dermat)]
von  der  ä-Basis  (=  gr.  uva-):  ai.  mnätd-  ,erwähnt';  mnäydte  ,wird  er- wähnt* ;
ai.  mdnas-,  av.  manah-  n.  ,Sinii'  (=  gr.  (.isvog);  ai.  durmands  {=  öva^e- vrjg)]  3,p.  Ha
xä-manU  'Ayaiuivr^g  ,von  Freundessinn  beseelt';  ai.  mdnman- ,Sinn,  Gedanke'  (=  air.  menme);  mantdr-  ,Denker'  (=  gr.  Msvtwq,  lat. commentor);  müni-  ra.  begeisterter,  Seher  (vgl.  nccvrig),  Asket';  mdntra- m.  , religiöse  Formel',  av.  mq-d-rö  ds.;
ai.  su-mnd-  n.  , Wohlwollen' ;  äi.  ma^z-,  maa*-,  av.  -maiti-  ,Sinn,  Gedanke, Meinung'  (=  lit.  mintis,  abg.  pa-mgit,  got.  ga-munds,  lat.  wem),  woneben auch  ai.  manti-  , denken'  (=  got.  ana-minds) •  mdntu-  ds.;  abhi-mäti-  f. ^Nachstellung'  (*-'»ini-i-) ;
arm.  i-manam  , verstehe'  {*menä-mi,  vgl.  unten  ahd.  manön)] gr.  (xsfxova  {ix6f.iai.isv]  f^sfiäcbg,  mit  metr.  Dehnung  (xe^iäcog)  ,gedenke, habe  Lust,  verlange'  (Präteritopräs.  wie  lat.  meviini,  unredupl.  got.  man), Imper.  Perf.  !.ie(.i(XTü)  (=  lat.  mementö) ;  avTÖ-(.iaTog  ,aus  sich  selber  heraus- denkend und  handelnd' ;  fi(xivo(.Lai  ,bin  verzückt,  rase'  (=  mänyate  usw.), 1  Aor.  if.i7]vcc(j.r]v,  ifiavrjv,  Perf.  (j,6{.ir]va]  vgl.  fiavla  ,Raserei',  (lavTig  , Seher', fiaivdgj  -ddog  ,die  Verzückte',  (.laivölTjg,  -oXig  , rasend' ;
von  der  Basis  auf  ä-:  Perf.  (.i6(j,vrjfiaL  (dor.  -ä-)  ,bin  eingedenk',  Präs. jiL(Xvfj(Ty.ü}  (äol.  y,LfivaioY,(jü)  , erinnere',  Med.  , erinnere  mich',  Fut.  i.ivr^oo}] ^vdofiai  ,erinnere  mich'  in  hom.  (xvcoöfisvog,  (.nwovro ;  fxvrjaig  f.  , Erinnerung', fivrjfj,a)v  , eingedenk',  fi^rjua,  dor.  (xväfia  , Erinnerungszeichen,  Grabmal'; (ih'og  n.  (=  ai.  mdnas-)  ,Mut,  Zorn';  (xsvoLvda)  ,habe  im  Sinn,  habe  vor', pLSvoLvrj  , Wunsch',  auf  Grund  eines  Subst.  *{.i6rd)(i)  (vgl.  den  Frauen- namen MsvcüL,  Msvü)  und  die  Ableitung  Mevolrrjg,  MevoixLog) ;  ^fjvLg,  dor. fxävig  , Groll'  (*uvävLg?)]  vgl.  oben  S.  693: alb.  mund,  mend  ,kann'  (*mn-dh-)',
lat.  meminl  , erinnere  mich,  bin  eingedenk'  (:  gr.  ixe^iova]  vgl.  osk.  mem- nim  ,monumentum,  memoriam') ;  von  der  Basis  auf  -l  ( :  -ei)  minlscitur  ds., comminlscor  , erinnere  mich';  mens, -tis  , Sinnesart,  Gemüt,  Denkvermögen, Vernunft'  (aus  *mnti-,  s.  oben  ai.  mati-  usw.),  mentiö  , Erwähnung'  (=  air. air-mitiu),  Denom.  mentior,  -Iri  , lügen'  (vgl.  apr.  mentimai  ,wir  lügen', d.  i.  ,Ersonnenes  vorbringen',  vgl.  z.  Bed.  noch  commentum  , Erdichtung, Plan',  zum  Partiz.  commentus  , ersonnen',  und  lit.  pra-manytas  , erdichtet, falsch');  Kaus.  moneö  , mahne'  (=  lit.  is-manyti,  dehnstufig  ai.  mändyati), monitor  m.  , Mahner',  monumentum  , Erinnerungszeichen',  mönstrum
```


## [2026-09-07T16:13:40.440Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'menth' POK_full.txt | head -40",
 "description": "Grep POK_full for menth"
}
```


### [2026-09-07T16:13:40.485Z] TOOL RESULT

```
21951:compare also v. Blumenthal IF. 49, 172 to 5ua|jaivai BoKxai; sxGuaan SKnvsuan Hes.; but 
26538:thrak. £V£a (v. Blumenthal IF. 51, 115); 
32196:172 ff., V. Blumenthal, Iguv. Taf. 662; 
33496:s. V. Blumenthal Gl. 20, 288. 
55871:indulgence, luxury, debauchery ', luxuria; probably luma^ mint, mentha, plant of the genus 
55872:mentha, a thorn (?)' from *lug(s)ma; 
59781:e-grade iJEGiaKa Tr|v peijaaniJevrivTpocpnv Hes. ( *menth-to-)\ 
59783:Latin mando, -ere, -i, mansum " to chew, masticate ' ( *menthd)\ 
59785:nir. meadarbeWy, intestines ' {*menth-la ox *mnth-la)\
```


## [2026-09-07T16:13:43.260Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '59740,59840p' POK_full.txt",
 "description": "Read POK_full menth entries"
}
```


### [2026-09-07T16:13:43.310Z] TOOL RESULT

```
gr. iJoGoq m. ' SchlachtgetiJmmel ', [JoGoupa (*|Jo9opFa) f. ' haft of Ruders', Doric 
|j60u)v m. ' Metokenkind '; Attic Trechling', lak. [joGa^ ds.; 



Latin (Oscan) mamphur, better manfur^ ein Stuck der Drehbank '; 



Old Icelandic mgndullm. " Drehholz an der HandmiJhle ', Modern High German Mandel, 
Mandelholz^ Rollholz, walzenformiges Holz '; 

Lithuanian menturis, -i/zie (Latvian mieturis) 'verticil, whorl, group of parts (leaves, 
flowers, etc.) arranged in a circle, mashing stick, twirling stick ', menciu, /77^s//"stir 
(meal, flour)', Lithuanian mente^ spatula ', mentei. " shoulder-blade, shoulder, chuck, 
blade, palm, vane, fan, paddle, turner, trowel, float, shovel '; Old Bulgarian m§tg, 
mgstr TapaTT£iv, to make an uproar, move confusedly, be in disorder'. Iter. mQtiti, 
*sh-m eta na {russ. smetana etc.) "cream, milk cream, milk skimmings ', dissimil. from 
* sh-m^fana; 

Old Bulgarian motat/s^' to set in violent motion, drive onward, move, impel, urge ', 
russ. motatb " wind up, roll up, shake; waste ', etc. 

References: WP. II 269, WH. II 22 f., Specht KZ 64, 13; 66, 49, Trautmann 181 f. 
Page(s): 732 

Root / lemma: mehnth-2 
Meaning: to chew, mouth 
Material: Old Indie math-^ devour ': 



gr. ijaQuiai yvaGoi Hes. (compare (januvri maked. "meat dish '), paaaopai " chew, bite' 
(from *pa9ia-, Indo Germanic *mnth-ia), fjaara^u) " chew ', piaara^f. "mouth' and " 
mouthful ', paaTixauj "knirsche with den Zahnen', [jooguveiv jjaaaaGai ppaSswc; Hes. 
(probably with o from a before u, from *[jaa(a)uv£iv " assumed from Attic MaauvTia(;, 
TTapaMaauvTr|<; m. " a female parasite '); 

e-grade iJEGiaKa Tr|v peijaaniJevrivTpocpnv Hes. ( *menth-to-)\ 

Latin mando, -ere, -i, mansum " to chew, masticate ' ( *menthd)\ 

nir. meadarbeWy, intestines ' {*menth-la ox *mnth-la)\ 

Old High German mindil, gamindelu. " set of teeth in the bridle ', Old English mld/ds., 
Old Icelandic mel{*mint^I), Old Swedish /77/7ds.; Old Icelandic m/nna-sk' kiss'; (under the 
influence of common Celtic -ns-, -nt- > -nn-), zero grade Gothic munt^s. Old Icelandic 
mudr, munne. Old English mud. Old High German /77^/7o'" mouth'; or to cymr. mant, see 
above mehn-1. 

References: WP. II 270, WH. II 24; Specht Indo Germanic Dekl. 253 f. 
Page(s): 732-733 

Root / lemma: mehrehgh- 

Meaning: to soak, drizzle 

Material: Gr. ppsxw ' wet, rain, flood ', ppoxn, Ppox£t6(; "rain'; Latvian /77e/ig^d/ 'gentle 

rain', m^rga, marga^ soft rain'; Czech mrholiti^6uzz\e\ mrhu/kal\ne rain', russ. morgatb' 

become cloudy ' ( *mbrgafb), moroch, morozga "fine rain' ( *morgh-s-), morositb " fine rain'. 

References: WP. II 280, Trautmann 182. 

Page(s): 738 

Root / lemma: mehrehg- 
Meaning: edge, border 

Material: Npers. marz^ portion of land, region '; Latin margo, -/n/s' an edge, brink, border, 
margin ' ( *merg-dn-, -en-); Old Irish mruig. Middle Irish bruig {*mrogi-) " portion of land, 
region ', cymr. corn. bret. bro^ district, region, area ', brogaeQa\\\ agrum dicunt (Schol. to 
Juvenal VIM 234), gall. PN Brogi-maros, VN Allobroges {= urnord. alJa-markiR^ foreigner ') 
; Gothic markat "limit, boundary'. Old High German marcfbja '\\fr\\t, boundary, border land 
', Old English mearcds.. Old Icelandic mgrkt " border land, wood, forest' (*morga). Old 
Icelandic /anda-markn., Old English gemearcn. "limit, boundary, border line, abuttal, 
border' {*morgom), probably also Old Norse marku. " token, sign, mark ', Middle High 



German marc(h)v\. " brand, mark, sign ', Modern High German merken {a\so mark as 
currency, actually probably ' Merkstrich am Gewicht '). 
References: WP. II 283 f., WH. II 39 f. 
Page(s): 738 

Root / lemma: mehrsM^-, mraM^- 

Meaning: to boil; to jolt, shake 

Material: Gr. ppaaau), Attic ppaiToo (*pipa6-i(jo), Aor. sppaaa, Ionian sK-ppnaaoo 'simmer, 

seethe, roar, flare up; foam, bubble, effervesce, winnow ', ^pao[}6(; " the boiling '; Latvian 

murdef to bubble up ', murd/" mineral water ', Lithuanian murdau, -yti^ hineinstoflend 

versenken '.
```


## [2026-09-07T16:13:50.806Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '59700,59745p' POK_full.txt",
 "description": "POK menth-1 start"
}
```


### [2026-09-07T16:13:50.855Z] TOOL RESULT

```
With Ar-formants: Old Indie manak^ a little, a bit '; Old High German mengen {*mangjan) 
and mango/on '{r\\ss', Modern High German mangein. Middle High German manc{-g-) 
'lack, disability '; Lithuanian /77e/7/r5S "small, insignificant ', menke^ codfish, cod-like 
predatory fish ', etc.; 

Tocharian B menkT small '; Hittite ma-ni-in-ku-wa-an-te-esHom. PI. "short'. 

References: WP. II 266 f., WH. II 93. 
Page(s): 728-729 

Root / lemma: mehn-5 

Meaning: to stay, stand still 

Note: (= /77e/7/7- "think'?) 

Material: Old Indie man- {parimamandhi, amaman) "hesitate, stand idle ', Avestan ap. man- 

" abide, remain, wait, hold on', Avestan fra-man-' persist, stand firm '; Armenian mnam^ 



stay, expect ' ( *mena-); gr. |j£vco, (jifjvu) (|j£p£vr|Ka) " stay ', povn f. ' staying ', p6vipo(; " 
persisting ', fj£|jvu)v " donkey ' ("persistent '); Latin maneo, -e/ie (compare fj£|j£vr|-Ka) " to 
stay, remain, abide, tarry ' ( *meneid), Denomin. mantare " to stay, remain, wait '; Old Irish 
ainmne, cymr. amynedd, mcymr. anmynedd^ patience ' {*an-menia)\ 

Tocharian A B mask- " be, exist '; Hittite mH'm-ma-/" reiuse'. 

References: WP. II 267, WH. II 26, Pedersen Hittite 121. 
Page(s): 729 aaypa 

Root / lemma: mehnth-1, mehth- 

Meaning: to mix up, stir 

Material: Old Indie manthati, mathnati^ swirls, mixes, stirs, shakes ', mantha-m. " gyration, 

mixing spoon ', Avestan mant- " bestir '; 



gr. iJoGoq m. ' SchlachtgetiJmmel ', [JoGoupa (*|Jo9opFa) f. ' haft of Ruders', Doric 
|j60u)v m. ' Metokenkind '; Attic Trechling', lak. [joGa^ ds.;
```


## [2026-09-07T16:14:17.159Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '78586,78660p' POK_full.txt",
 "description": "POK (s)mer- entry"
}
```


### [2026-09-07T16:14:17.210Z] TOOL RESULT

```
Root / lemma: (s)mer- 

Meaning: to remember; to care for 

Material: 1. Old Indie smarati^ reminds sich, gedenkt', smarana-n., smrt/-' memory, 

recollection, Gedachtnis', Avestan maraiti, h/smara/t/ ' {be)merkt' , m/mara- ^e'\ngedenk'; 

Armenian /77c»/777c»/r"Bedauern, Miftvergnijgen, distress, affliction'(with formants -o/r'from 

a *mor-m[or]o-W\Vc\ fractured reduplication); gr. \xt^\xz^oc, 'was viel Sinnen, Sorgen 

required '; jJEppaipu), pspunP'^w 'care, sinne, hesitate '; [jsppripa f. ' care, Sinnen', 

Mspipvau) 'care, bin bedacht, grijble', post-verbal pspipiva f. ' care, anxiety '; also paprut;, - 

poq, hom. fjapTupoc;, Cretan paiTup- ' witness, testifier '? different above S. 735; 

Latin /77e/77c»/''eingedenk' (compare Avestan mimara-6s.. Old English ge-mimor6s.), 
/77e/77c>/7a 'Gedachtnis'; A^o/fa'eine Parze'; 

Old Irish airm(m)ert\. 'forbid', cymr. ar/77e/f/7 'Vorbereitung' {*smert-). Middle Irish 
/77e/'/5/io''richtet ein', bret. merzout^ become aware', Vannes 5/777e/'/7e//7'einrichten'; gall. 
PN Smerius, Smertullus, GN Smertrios, Ro-smerta'6\e Voraussehende'; abrit. VN 
Ipsprai. 



Old Icelandic MTmir'a giant '; Old English mimorian ^s\c\\ remind', ge-m/mor' kno\Nn' , 
mamr/an 'uberetwas sinnen', Dutch m/jmeren'deep nachsinnen'; Gothic maurnan. Old 
English murnan. Old High German mornen'care for, worry, anxiously worry about'; 

Old Lithuanian meref/^care for, worry', lengthened grade serb. mar/f/^s\c\r\ kijmmern 
um', etc. {*mdr-)\ 

2. as "sinnen, sinnend dastehen' = 'hesitate' probably die group Latin morat "Verzug, 
delay'. Old Irish mar{a)/m' stay '; corn. bret. mar'6oubt'; 

3. here as "jemanden wherewith consider, versorgen; Zugedachtes' also gr. pEipopai 
{*o[iZQ\o[ia\) 'erhalte allotment ', poTpa ' allotment, fate, destiny' {*sm-, compare hom. Kara 
MpoTpav), Perf. hom. eppops "hatAnteil', ei'papTai (*o£-apapTai) "es is durchs lot, fate 
zugeteilt', sipapiJEvr) "fate, destiny', [^tpoq n., [j£pi(;f. " allotment, part', pspi^u) "divide', 
M6po(; m. "lot, fate, fate, destiny, person's lot in life', Kaapopo(; 5uaTr|vo(; Hes. 
{*Kaio[}opoq; Koppopo^Od. is newer formation), hom. appopoc; "unteilhaftig', nijopic; 
za^zpr\[^tvr\ Hes., lak. popa "dividing off, partitioning off of spartanischen Heeres', [jopiov 
"part'; probably also afjapravu) "verfehle' due to eines *a-/7ijapT0(; "unteilhaftig'; Latin 
mereo, -ereav\6 mereor, -erf earn, acquire ' (i.e. "erhalte allotment ', "erwerbe mir meinen 
allotment '), merenda "Vesperbrot, Mahlzeit the animal' ("*wherewith person and animal to 
consider is'). 

References: WP. II 689 f., WH. II 67 f., 110, W. Oehl IF. 57, 2 ff.; Vendryes Et. Celt 2, 133 
f., DuvalEt Celt 6,219 ff. 
Page(s): 969-970 

Root / lemma: (s)meukh-, (s)meug- (s)meugh- 

Meaning: to smoke, smoke n. 

Material: Armenian mux. Gen. /77A'c>y "smoke'; gr. apuxw (x = kh or gfr, sopuynv from the g- 

form) "allow verschwelen; in langsamem fire consume'; Irish /77i7c/7 "smoke', cymr. mwg 

(with alternation 0: u), corn. mok6s., bret. moug, mogl\re', moged'smoke' {-kh- or -k-); 

with -g. gr. opuynvai; Armenian murk. Gen. /77/'/roy"sengend' {*smugro-); 

Old English smeocan ^ smoke' , mnl. sm/eken and smu/ken 'smoke'; Kaus. Old English 
sm/iecan' smoke, fume ', Middle Low German s/77d/re/7"schmauchen, fume, through Rauch 
choke'; Old English smTecm. "smoke'. Middle High German s/77c»£/c/7 "smoke, haze, mist'; 
Old English smocam. 'smoke', s/77c»c/a/7 "smoke, fume '; 



Lithuanian smaugiu, smaugtr choke; suppress, crush (originally through smoke), 
strangulate '; perhaps russ. smuglyj, kir. smuhfyj^ brownish black ' ("smoke-color '); Balto
```


## [2026-09-07T16:14:31.240Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD menth ===\"; grep -n -i '^menth\\|^ment-\\|^mendh\\|^smer\\|^mer-\\|^men-' AHD_watkins1985.txt | head -30",
 "description": "Grep AHD Watkins roots"
}
```


### [2026-09-07T16:14:31.289Z] TOOL RESULT

```
=== AHD menth ===
217:men-1, I. Zero-grade form *mn-...
745:men-!, To think; with derivatives referring to various qualities and states of mind and thought. I. Zero-grade form *mn-. 1. Suffixed form *mmy-ti- in: a. Germanic “ga-mundi- (*ga-, intensive prefix; see kom), in Old English gemynd, memory, mind: MIND; b. Latin méns (stem ment-), mind: MENTAL; AMENT?, DEMENT; c. Latin mentid, remembrance, mention: MENTION. 2. Suffixed form *mn-to- in Greek -matos, “willing”: AUTOMATIC. 3. Suffixed form *mn-yo- in: a. Greek mainesthai, to be
749:men-2. To project. 1. Suffixed zero-grade form *mn-to- in a western Indo-European word for a projecting body part, variously “chin, jaw, mouth,” in Germanic *mun- thaz in Old English mith mouth: mouTu. 2. Latin mi- nae, projecting points, threats (> mindri, to threaten): MENACE, MINACIOUS; AMENABLE, DEMEAN!, PROME- NADE. 3. Latin -minére, to project, jut, threaten: EMI- NENT, IMMINENT, PROMINENT. 4. Suffixed o-grade form *mon-ti- in Latin méns (stem mont-), mountain: MONS, (MONTAGNARD), MONTANE, MONTE, MONTICULE, MOUNT!, MOUNT?, MOUNTAIN; AMOUNT, ULTRAMONTANE. [Pok. 1. men- 726, 2. menth- 732.] men-3, To remain. Variant suffixed (stative) form *man-é- in Latin manére, to remain: MANOR, MANSE, MANSION, (MENAGE); IMMANENT, PERMANENT, REMAIN. [Pok. 5. men- 729.] men-‘. Small, isolated. 1. Greek manos, rare, sparse: MANOMETER. 2. Suffixed o-grade form *mon-wo- in Greek monos, alone, only, single, sole: MONAD, MONAS- TERY, MONK, MONO-; PSEUDOMONAD. 3. Possibly also suffixed form *men-i-, a small fish, in Old English myne, mynwe, minnow, perhaps the source of Middle English meneu, a small fish: MINNOW. [Pok. 4. men- 728, meni- 731.] mend-. Physical defect, fault. 1. Latin mendum, menda, defect, fault: MENDICANT; AMEND, EMEND, (MEND). 2. Latin mendax, lying, liar: MENDACIOUS. [Pok. mend(a) 729.) mendh-'. To learn. Zero-grade form *mndh- in Greek manthanein (aorist stem math-), to learn: MATHEMAT- ICAL, (MATHEMATICS); CHRESTOMATHY, POLYMATH. [Pok. mendh- 730.] mendh-?. To chew. 1. Latin mandere, to chew: MANDI- BLE, (MANGE), MANGER. 2. Zero-grade form *mndh- in: a. Greek masasthai (< *math-ya-), to chew: MASSETER; b. Greek mastax, mouth, the model for expressive Greek (Doric) mustax, upper lip, mustache: (MOSTACCIOLI), MUSTACHE; Cc. Greek mastikhan, to grind the teeth: MASTICATE. [Pok. 2. menth- 732.] menegh-. Copious. Germanic *managa- in Old English manig, menig, many: MANY. [Pok. men(e)gh- 730.] meng-. To furbish. 1. Latin mango, furbisher, gem pol- isher, swindler: MONGER. 2. Greek manganon, magic
750:mer-'
752:mer-'. To flicker; with derivatives referring to dim states of illumination. 1. Suffixed form *mer-o- in Latin merus, pure, unadulterated (< “unmixed wine” < “clear liq- uid”): MERE!, 2. Extended form *merk- in Germanic *murgana- in: a. Old English morgen, morning: MORN, MORNING, MORROW; b. Middle Dutch morghen, morn- ing: MORGEN; Cc. Old High German morgan, morning: MORGANATIC. 3. Possibly extended root *merg~- in Ger- manic *merkwia-, twilight, in Old English mirce, dark- ness: MURK. [Pok. 2. mer- 733.]
753:mer-2, To rub away, harm. I. 1. Germanic *marén-, goblin, in Old English mare, mere, goblin, incubus: NIGHTMARE. 2. Greek marainein, to waste away, wither: MARASMUS; AMARANTH. 3. Probably suffixed zero-grade form *mr-to-, “ground down,” in Latin mortdrium, mor- tar: MORTAR. 4. Possibly extended root *merd- in Latin mordére (past participle morsus), to bite: MORDACIOUS, MORDANT, MORDENT, MORSEL; PREMORSE, REMORSE. 5. Possibly suffixed form *mor-bho- in Latin morbus, disease (but more likely of unknown origin): MORBID. II. Possibly the same root, but more likely distinct, is *mer-, “to die,” with derivatives referring to death and to human beings as subject to death. 1. Zero-grade form *mr- in: a. suffixed form *mr-tro- in Germanic suffixed form *mur-thra- in Old English morthor, murder: MUR- DER; b. suffixed form *mr-ti- in Latin mors (stem mort-), death: MORT!, MORTAL, MORTUARY; AMORTIZE, (IMMOR-
755:mer-3. To tie. Possibly in: a. Middle Dutch marren, to tie: MARLINE; b. Middle Low German méren, to tie: MooOR!. [Pok. 1. mer- 733.]
```


## [2026-09-07T16:14:32.945Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN mar/amar ===\"; grep -n -i 'āmār\\|amär\\|āmar\\|Zählung\\|šmurdan\\|shumārdan\\|gumārdan\\|gumāštan' HRN.txt | head -40",
 "description": "Grep Horn"
}
```


### [2026-09-07T16:14:32.998Z] TOOL RESULT

```
=== HRN mar/amar ===
833:aw. a + 2 l^mar- 'sich erinnern'; phlv. amär 1) 'Zahl'
1460:aw. hanlcärat/emi j hankere&a-, hankereti- 'Zählung'
5117:schichte, Erzählung .
5589:^) von Staokelberg, Fünf ossetische Erzählungen, 83 ver-
```


## [2026-09-07T16:14:50.077Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '833,860p' HRN.txt; echo \"=== leaf of line 833 ===\"; awk 'NR<=833{n+=gsub(/\\f/,\"\")} END{print n}' HRN.txt",
 "description": "Horn amar entry"
}
```


### [2026-09-07T16:14:51.320Z] TOOL RESULT

```
aw. a + 2 l^mar- 'sich erinnern'; phlv. amär 1) 'Zahl'
2) 'zähle, rechne* (das Verbum ämartan ist nicht belegt) ;
skr. a + V^smaV" (nicht belegt).
48. ätneden 'kommen*, Praes. äy-em (s. No. 60).
ap. ä+ [/^gam-, äjannya 'er käme*; aw. ci+ [/'(/am-,
ägemat; phlv. nrntan, ämatan (PPGl.) ').
Mit Mahjalvokal (FJ.).
^) FR hat einen Beleg aus Siräj eddin:
(Metr. Xeftf)
tie/s^ cun ser^ gesf bestezed
tevsen-äsä beher süy älezed.
*) Beiläufig bemerkt, findet sich bure als Imperativ *komm* ausser
im Kurdischen (Houtum-Schindler) und bei Shukovski dialektisch
auch bei Bäbä Tähir *Uryän aus Rei (Huart, Journ. asiat, Si^me s^rie,
vol. VI, 519).12 -
49. äniurzlden Verzeihen', ämarzis^ amurzlst (Qiss. Dan.).
aw. ä+i/'marz', ämarezen; iphlw, ümurzUan, ämurz(i)sn,
ämurzltär Verzeihen' ; ai. ä -j- [/'marj- Vegwischen .
Vergl. wa/. namurzg, sar. namüzg 'Rechen, Besen.
Im Awesta und Altindischen wird die Bedeutung
gnädig sein, verzeihen' durch das Wurzeldeterminativ
d aus der [/^merg- ^abwischen' gewonnen, vergl. aw.
merezdätä, meresdika-, ai. m^ddti (Bartholomae BB. 13,
87, während Brugmann, Indog. Forsch. I, 171 auch
an ai. mfsyate Vergisst*, lit. mifsztl Vergessen denkt).
50. iimö^ten lehren, lernen*, Praes. ämöz-em, amözis,
phlv. ämö/tan lehren', ämöc-am, amöc(i)sn^ ämöölmtan ;
lit. mokinü „wohl auch faktisch 'lehren*, eigentlich zum
=== leaf of line 833 ===
32
```


## [2026-09-07T16:14:51.905Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== TAD مصطك ===\"; grep -n 'مصطك\\|مصطكى\\|مصطكا' TAD_pages.txt | head; echo \"=== HUB ===\"; grep -n -i 'āmār\\|amär\\|hišmar\\|hishmar\\|smar' HUB.txt | head -20",
 "description": "Grep TAD and HUB"
}
```


### [2026-09-07T16:14:51.969Z] TOOL RESULT

```
=== TAD مصطك ===
2655:    ‫مصطكي ‪ -‬ونانى ‪8‬وعناموه هو عصارة شجرة نشبه الفستق واليطم تمد‬
=== HUB ===
2826:§merql *to count', kurd. izmar 'Zahl' = hiSmar Socin,
2828:hismarento^ aiwi-smareW^ paiti-smaremna^ aber SumuV"
2829:dan geht nicht auf zd. aiwi^smar zuriick, trotz phi.
2841:sumar auf smar (Nr. 791), sanj auf sific (Nr. 323) etc.
3335:falls mit ap. *m-inar = skr. vi-smar nichts zu thun.
3728:(Nr. 47). Wrzl. skr. smar-, vgl. sam-smar *sich er-
3729:innern, gedenken , sq^smarana" *das Gedenken, sqs-
5117:sumaram (vgl. skr. smarayati), supurdan: pr. sipciram ist
6107:sufnCLr *Zahr, Sumurdan 'zahlen', phi. mmurtan, ap. -smar^
9227:zd. mar = skr. smar (oben p. 105) ; am
```


## [2026-09-07T16:14:58.623Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--- HRN leaf 229 (p208) ---\"; awk 'BEGIN{RS=\"\\f\"} NR==230' HRN.txt | head -40",
 "description": "Horn p208"
}
```


## [2026-09-07T16:15:00.570Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--- HUB leaf of line 2826 ---\"; awk 'NR<=2826{n+=gsub(/\\f/,\"\")} END{print n}' HUB.txt; sed -n '2815,2845p' HUB.txt; echo; echo \"--- HUB line 6107 leaf ---\"; awk 'NR<=6107{n+=gsub(/\\f/,\"\")} END{print n}' HUB.txt; sed -n '6100,6115p' HUB.txt",
 "description": "Hubschmann entries"
}
```


### [2026-09-07T16:15:00.894Z] TOOL RESULT

```
--- HRN leaf 229 (p208) ---
— 208 —
indog. Deminutivsuffix -/o- vergl. Brugmann, Grund-
riss II, 186 folg.
930. gile 'Klage .
aw. gerezü" 'Klage', vergl. [/^gar2-, gerezaiti 'klagen';
plilv. garzTtan j garz{i)s7i, gilak (Men.); ai. l^garh-,
garhate 'klagen, anklagen' ^).
kurd. gilt 'Klage', gire 'Streit'; oss. d. yärziin, t.
gärzin stöhnen* (89).
931. f/ii^ii«/Sfeii/an vertrauen, übergeben', Praes. gumär-em.
ap. *»/ -r V^mar- mit Bedeutungswechsel, vergl. skr.
vi- r smav' 'vergessen' ; phlv. gumästan, gumür.
Unsicher.
932. gtitnän 'Zweifel; Meinung'.
aw. '^vwianah' 'Zweifel', vergl. mmiwöhya-; phlv.
gnmän,
LW. kurd. afy. gumän 'Zweifel*; bei. gtarän (121).
933. f/unäh 'Sünde'.
g. venall.
skr. vinäga- 'das Verlorengehen, Vernichtung, Unter-
gang (m + iXwa^r-) ; phlv. v{i)ncLskary v{i)na8karth, arm.
LW. vnas, vnasakar,
LW. kurd. gmiäh 'Sünde*; bei. gunas (119).
934. yend 'Gestank', gmda stinkend', gendah 'Pfuhl*, gend-
egl, gende, gendamden (AM. 45 Zeile 1; 78 Zeile 3
V. u.).
*) Lautlich stünde der Heranziehung von skr. \y^gorj-^ garjati
*brüllen, brummen, toben, brausen, tosen* nichts entgegen; denn sowohl
e/i wie g^h setzen ein ap. d voraus. Doch stimmt die Bedeutung von
garh^ besser als die von garj- (s. auch Bartholoma e, ZDMG. 44, 552).
notirt : hüzle *junge Ziege', desle 'Händchen', yellele 'Bischen, Stückchen*,
kuzowle 'Wasserkrüglein', kulaile *Köter* (eigentlich Demin. von kulai
'Hofhund'j, nazule 'Kätzchen*, perdele 'Häutchen', segle 'Hündchen*,
/unele 'Häuschen'.
Dasselbe Suffix erkenne ich nunmehr in np. ähle 'Bläschen' (AM.
50, 14; 153, 11), auch abile^ äwile^ vergl. äbek (änek^ VuUers No. 2 s. v.
ist verschrieben). Gewiss wird es sich im Np. noch häufiger finden.
Auch kurd. gtirdale (s. oben No. 905) wird hierher gehören (Correctur-
note).
```


### [2026-09-07T16:15:02.388Z] TOOL RESULT

```
--- HUB leaf of line 2826 ---
90
Praesens SiUdfam ist als iranische Wurzel skaf =
arisch skaph anzusetzen. Caus. sigdfdmdan JRAS.
1894, 474.
788. Ich habe ZDMG. 38, 424—426 als iranische Wurzel
skand^ scand^) angesetzt: was ist der Vorzug des
Horn-Bartholomae'schen Ansatzes sdand?
789. Wenn Sal =■- gr. OxsXog ist, miisste es fiir sal (von
Wrzl. sk^el) stehen. Soweit stimme ich Fr. Miiller,
WZKM. 7, 377 bei.
790. Lies arm. /er.
791. Dazu afgh. LW. sumar 'counting, numbering, number',
§merql *to count', kurd. izmar 'Zahl' = hiSmar Socin,
kurd. Samml. II, 281. Wegen des anlaut. s fiir s vgl. zd.
hismarento^ aiwi-smareW^ paiti-smaremna^ aber SumuV"
dan geht nicht auf zd. aiwi^smar zuriick, trotz phi.
osmurtan (Gl. and Ind. 53), das usmurtan gelesen werden
kann, da die Pehlevischrift u und o im Anlaut nicht
unterscheidet , vgl. urvar *Baum', geschrieben drv(a)r
Oder aurv(a)r etc.
») Vgl. jud. tat. coyol (Miller p. 88).
*) Die schwachste Form ist shad = idg. sknd*— 81 —
792. Gehort Hna, sinoh, aSna, Osnah 'Schwimmen' (Nr. 34, 2)
zu osset. axsnun^ axsjnn waschen, ptc. axsnadt, axsdd ?
Osset. nam entspricht lautgesetzlich dem zd. sno-,
da anl. sn- im Iranischen (ausser dem Zend) zu n
wird. Doch kann Una etc. auf snd zuriickgehen wie
sumar auf smar (Nr. 791), sanj auf sific (Nr. 323) etc.
793. Das Verbum danistan ist, wie oben unter Nr. 534
bemerkt ist, aus dem Praesensstamm dan- (np. ddnam
= ap. *danamiy = skr. janami) gebildet, so dass unter
seinen Formen Ableitungen der durch skr. jtW, lat.

--- HUB line 6107 leaf ---
183
siparam) 'iibergeben', Wrzl. spar; supdr 'Pflug', afgh. spdra
fem. 'Pflugschar; supurz 'Milz* = zd. spereza; supus, supus- 173 —
*Laus' (auch sipis u. s. w.) = zd. spis; supoxtan [sip^xtan)
'heraustreiben = paz. spuxtan, arm. spuzel : sutudan (sitdyam)
'loben*, zd. stw, sutor ^Ross' = zd. staora-; siitun Saiile*
= zd. stuna-; sunudan (sinavam) *horen' (auch sinldan, as^
nudan etc. Sal. Shuk. p. 52); suma'ihr\ gd. xsmaka- 'euer ;
sufnCLr *Zahr, Sumurdan 'zahlen', phi. mmurtan, ap. -smar^
u. s. w.
In der Kegel also wird l vorgeschlagen oder einge-
schoben, wenn der folgende Vokal a, ? oder e war, dagegen
u vor folgendem u oder 6 und zwischen s-w. Urspriinglich
also durUdan, aber pr diravam, sunndan, aber simdan, pr.
sinavam etc.
vi^ 62. Da sonach die Anlautsgruppe: Vokal 4 Doppel-
konsonant (z. B. ispSd, istahr) haiifig mit der Anlautsgruppe:
```


## [2026-09-07T16:15:11.571Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==106' HUB.txt | head -50",
 "description": "HUB p95"
}
```


### [2026-09-07T16:15:12.849Z] TOOL RESULT

```
— 95 —
ksl. glava 'Kopf ', arm. glux 'Kopf etc. Zu merdle vgl.
Vullers, Grammatica linguae persicae p. 235, wo die
Formen auf le als Formen des Tat-Dialectes bezeichnet
sind. Darauf verweist auch Mann, ZDMG. 47, 705.
931. Np. gumaStan = pfiz. gumdrdan = phi. gumdrtan
'einsetzen, bestimmen, beauftragen, betrauen' Min. Gl.
93, Bdh. Gl. 225, afgh. gumdrql to consign*, arm.
LW. gumar-el 1) sammeln*, 2) 'schicken, iibergeben,
einsetzen* zeigt nirgends den Anlaut t?- und hat jeden-
falls mit ap. *m-inar = skr. vi-smar nichts zu thun.
932. Np. guman = ap. ^mmOna^ (statt zd. *vfmanah'),
Vgl. unten Nr. 965.
934. Vgl. KZ. 33, 165. Dazu nun auch afgh. yand^ql *Ekel
empfinden, nicht leiden, nicht mOgen' (Geiger). Afgh.
ganda 'stinkend' finde ich nicht bei Raverty.
935. Skr. gddhUma^ wird volksetymologische Anlehnung
von ^gandhUma- an die Composita mit gd- *Kuh* sein
{go-dhuma- gleichsam *Kuhrauch'; vgl. unsern Pflanzen-
namen Erdrauch, gr. xanvog^ mnvioc).
936. Dazu arm. LW. gund 'Kugel', gndak *Kugel, Ball,
KnoUen'. Ich halte die Etymologic fiir richtig.
937. Hochst unsicher.
938. Unsicher.
Hierher nach Fr. Miiller, WZKM. 8, 189 guvdrtdan ver-
dauen' = phi. gukar-Uan zu skr. vi-kar umwandeln .
940. Arm. vkay gehdrt nicht zu np. guvdh, vgl. meine
Abhandlung *Arisches und Armenisches*, Idg. Forsch. 4,
p. 119.
941. Ich fasse gosdla *Kalb* als Compos, von go- = np.
gav, gav *Kuh' und sdla *Jahrling (von sal *Jahr ab-
geleitet wie in den Zusammensetzungen mit Zahl-
wortern -sdla = jahrig' ist), also = 'Kuh-jahrling,
vgl. unser 'Jahrlingskalb'. Kurd. LW. gilsile ZDMG.
38, 85.
^4. Np. gost 'Fleisch' = ap. *gausta-?
946. Arm. goin ist Lehnwort, aber aus anderen Griinden.
Ebenso arm. gunak =n np. guna* Afgh. yuna f. 'Haare
[
```


## [2026-09-07T16:15:21.840Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG mar ===\"; grep -n 'gumār\\|gumar\\|hišmar\\|hismar\\|šmar\\|smar-\\|\\*mar' CHEUNG.txt | head -40",
 "description": "Grep Cheung"
}
```


### [2026-09-07T16:15:21.886Z] TOOL RESULT

```
=== CHEUNG mar ===
9715:paitismaromna- (Y 55.6, Yt 5.11, Yt 5.123, Yt 10.86), red. ҮАУ. aipi hismarant- (Yt 10.45), perf. pass. 
9748:*CHORESMIAN: ’/mr- ‘to count; consider’ (*hismara-) = Samadi: 111 
9755:(impv.) wer-usmor, Gz. ösmär-/ösmärt, ismärt, Khuns. (t)ismar-, Smar-/1smurt, Mah. 
12404:exist. The attested form malstä can be interpreted differently, from *maré, on which 
17446:difficult: the connection with the root *mar(H) is unlikely, particularly because the 
17452:root *mar(H) is continued by Khot. murr- (q.v.). The inclusion of YAv. “man- is 
17512:*maré (mark) 265 
17569:*maré (*mark) ‘to destroy, damage’ 
17574:266 *mard 
17589:ВМР gwmlc'k /gumarzag/ ‘the pernicious’ (Gershevitch 1977: 66) = DMMPP: 
17613:*MISC: Par. mat (supplet. of mör-, *mar') ‘killed’, Orm. mak (ppp.) ‘withered, faded’ 
17623:*mard ‘to despise, disparage (?); to neglect, abandon (?)’ 
17641:*marHl 267 
17664:*marH! ‘to rub; crush’ 
17671:contain *marH', rather than *maz ‘to break’: all the attested forms have , /r/ without 
17695:268 *marH2 
17711:*marH ‘to block, hinder 
17716:Pres.: IND. 3sg. MMP "gwm'ryd, IMPV. 2sg. BMP gwm’! /gumar/; Partic.: perf. pass. MMP gwm’rd, 
17717:BMP gwm’Itk /gumardag/; Inf.: BMP gwm’Itn /gumardan/ 
17746:*marš ‘to forget’ 
17750:*mars (on account of the Pahlavi and Manichaean forms), for which he quotes 
17787:*marZd ‘to have pity, forgive’ 
17809:© The Пг. root *marzd has no IE correspondences. On the possible interpretations of 
17983:*marH!, which is preferable: all the attested forms have , /r/ without the diacritic dot 
18042:*mar (*mar2) ‘to moan, complain’ 
35169:gwm'l- /gumar-/, 268 
35171:gwmlc 'k /gumarzag/, 
44311:(t)išmar-, Smär-/iSmurt, 
55097:*mard, *raic, *raz (S.V.), 
55769:*Hranj (s.v.), *mard (s.v.), 
55774:*marzd (s.v.), *suan 
55778:*Hram (s.v.), *marH’, *raud, 
56134:*mar 
56178:*marH' , *pais, *uraiH, 
56278:*maiH, *maréc, *ras 
56311:*mard 
56314:*kan! (s.v.), *marc, *Hrais 
56321:*mar', *frait/9 (s.v.), *rai9! 
56337:*mard 
56628:*mars
```


## [2026-09-07T16:15:24.696Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD ===\"; grep -n -i 'āmār\\|amar\\|hmār\\|ōšmurdan\\|ušmurdan\\|gumārdan\\|gumārtan\\|hmurdan' PHD.txt | head -30; echo \"=== NYB ===\"; grep -n -i 'āmār\\|ōšmurdan\\|ušmurtan\\|gumārtan\\|hmar' NYB_vol2_glossary.txt | head -30",
 "description": "Grep MacKenzie and Nyberg"
}
```


### [2026-09-07T16:15:24.760Z] TOOL RESULT

```
=== PHD ===
189:áhüg [TYBA < A ру; ”hwk! | MQyhwg, N āhū] gazelle. ahunawar [hnw!] the holiest prayer, beginning Yadā ahū wairyē. a-hunsand [Phwnsnd] dissatisfied. ^h : dissatisfaction. ahy [KZ Y < А k-zy | М hy] soon(est), first. ajģahān [>20/?л! | М ieikin, N azgahan] lazy, indolent. “АҺ: laziness, indolence. ak P! | N dk] evil, harm. -ak LIN ~] diminutive suffix. a-kámagómand [k mk’ wmnd] unwilling. a-kanārag ['kr?]k! | M ?qn’rg] unlimited, boundless. ~ih: boundlessness. a-kard Pārt! | (M °gyrd)] not done, undone. Akoman ['kwmn! | М ?qwmn] Evil Thought, an arch-demon, akómand ["£wmnd] evil, harmful. alā [Py] oh! alas! Аар [STLA, STRA < A £t ;?lk! | (М rel side. alálag PPH! | N lala] anemone. ālāy-, v. ālūdan. Aleksandar Piksndl | M *Ixsyndr, N Iskandar] Alexander (of Macedon). almās(t) Pim?s(t') | (M ?rm?s), N almas] steel; diamond. аадар [?/wtk'] defiled, polluted. АҺ: defilement. ālūdan, ālāy- Photn!, *Pd- | (M ?rwd), N ~] defile, pollute. Aluh Plwh | M "If, N ~] eagle. Xum [lum] millet. N~ amā [LNE < A l-nh | М ?*°h, N má] we, us. Amadan, āy- [Y ATWN-tn! < А y twn, V*th | M?mdn,?y-, N ~] come. amahraspand [?mhrsbnd | M (?)mhr’spnd] a Holy Immortal, a-mar [ml] countless, innumerable. amar [ml | N ~] reckoning, consideration. āmār- [?m?1-] reckon, calculate. ~išn: reckoning. a-marag [mlk') countless. amaraģān [?mlk’n'] generality, commonalty. ~ig [-yk'] general. ~iha [-yh’] in general, generally. a-marg [mig] deathless, undying. ~ih: deathlessness, immortality. ámárgar [?m’lgl | N ~] reckoner. amāwand [?m'wnd] powerful, strong.
380:gawazn [gw’sn' | N ~] deer. gawdar [0011 | N ~] calf. ģāw-dumb [g'bdwmb | N —dum] horn, trumpet. ģāw-mēš [TWR Amyš | N gā(w)mēš] buffalo. £áy-, v. ģādan. Gayómart [g”ywkmlt! = Av. gayó marata | (M gyhmwrd), N ~] the First Man. gaz [gc | N ~] tamarisk. gaz-, —išn, v. gazidan. gazag [gc’k'] biting. ģāzar [g'cl | N gázur] fuller, washerman. £azdum [gcdwm | N každum!] scorpion; astr. Scorpio. £azidag [ezytk! | N gazid] poll-tax. gazidan, gaz- [gc-, gz-ytn! | N ~] bite, sting. ~išn: biting. gëg [gdk' | M gyyg] thief. gēhān [gy)?>n! | = M, N gihān, jahān] world. ~ig [-yk'] worldly, mortal. -ģēn [-k(y)n! | M -gyn, N -gin] suffix forming adjectives of quality. gês [гуз | (M gyswg, N gēsū)] curls, locks. £étig [gytyk, gytydy | M gytyg, N géti] 1. the material world; 2. worldly. ~ig [-yk'] worldly. gil [ТУМА < A tym; gl | N ~] clay. gilag [g(y)lk! | N gila] complaint, lamentation. —-Obàr [wp] swallowing complaint, suffering in silence. ģilēn [T YN Ayn! | N gilin] (made of) clay. gilistag [g/ystk!] home, dwelling of demons. gir-, ~iSnig, v. griftan. gird [git! | M gyrd, N ~] round, circular; gathered. (9) — āmadan: gather, collect (intr.). — kardan: gather, collect (tr.). ~ih: roundness. girdag [gitk' | N ~a] disk, round. gisnag [gink' | P gyfng] short, small. ģišnīz [ginyc | N —] coriander. giyā(h) [gy^h, gy^h | (M gy'w), N ~] grass. ~izag [-yck'] a straw, blade of grass. gizistag [gcystk' | J w/Bzsth] accursed, hateful. gogird [оо | M gwgyrd, N ~] sulphur. ~ӧтапа [-’wmnd] sulphurous. gohr [gwhl | M gwhr, N gauhar] substance, essence, nature; jewel; stock, lineage. goóhrag [gwhlk'] = göhr. ~-danag [-d^m k!] physicist. 1g6hrig [gwhlyk'] natural, essential. *ģūhrīg [gw(’)hlyk'] equivalent, substitute, indemnity,
424:kaman [kin’n' | = M, N ~] bow. 5; 7 ~dar [-d'] | N ~] archer, bowman. ha er mae 4 ba kamar [kml | N —] waist; belt, girdle. ~-band [-bnd | N ~] belt. kāmģār [Emil | P k?*mg?*r, N ~] powerful, absolute. kamist [Amyst'] least. —jh: pad ~ih, at least. kāmistan, kām- [YCBEN-stn' < A ysbh, V shh; k*m-(y)stnt M k*m-yst] want, desire. kám|-rawág [km izvb*k! | N ~rawa] successful. ~-Z1(w)isn [-zywsn'] free, independent. kam-zór [kmzwl | N ~] weak. ~ih: weakness. kan-, v. kandan, kanar [kwl | N ~] side, edge; embrace. ~ag [-k' | M kr?rg, N ~a] edge, limit, boundary. --agómand [-k’wmnd | M -gwmnd] limited, finite. kandan, kan- [HPLWN-tn! < А V hpr; kn-dn', -tn! | M knd, N ~] dig; raze, destroy. kanig [knyk! | M knyg] girl, maid. kanizag [knyck! | M knycg, N kaniz(ak)] — kanig. kantigr [kntgl] quiver. kāpūr [ро | Ar. kāfūr] camphor. kar-, v. kardan. 1Kar [21 | M Pr, N ~] work, deed, affair. ~ framüdan: put to use. 2kàr [%'7], pl. —àn: (other) people. зкаг [%'/] butter. kār-, v. kištan. karafs [klips | N ~] celery. kār-āgāh [РА | N ~] skilled, experienced. ~ih: skill, experience. karak [krk! | N ~] quail. karan [kľn' | P bein, N ~] side, edge, end, limit. kārawān [%?/zv?x! | P k*rw'n, N kārwān] caravan, military column. ~ig [-yk! | N ~7] caravaneer, traveller. karb [klp] priest hostile to Zoroaster. karbāš [5/0 | N karbas, etc.] lizard. karbunag [k/pnk!, klbnk'] lizard. kard [krt! | M kyrd, N ~] action; matter, affair. кага [SK YN A < A skyn’; Kit! | N ~] knife. ikardag [kltk!] division, section, portion. *kardag [krtk!, kltk! | N karda] action. kārdāg [k'/d?k'] traveller, wanderer, migrant. kardaģān [Art-, Rlt&?n! | M kyrdg”n) action. kardagàár [Artk?l | M kyrdg’r, № ~] mighty. C 6084 E
816:appoint fraz griftan, gumārdan,hištan.
976:belt kamar(-band).
1136:calculate āmār-; v. reckon.
1295:commonalty amaragān, pāyram.
1352:consideration amar,  hangārišn,
1417:countless amar(ag), anēšmār, авар.
1503:deathless ahūš, amarg; v. immortal.
1504:deathlessness amargīh; v. immortality.
1782:entrust abespurdan, gumārdan.
2086:general (a.) amaraganig.
2088:generally, in general amaragānīhā.
2089:generality amaragan.
2102:girdle kamar; sacred ~ ēbyānghan, kustig.
2383:immortal ahēš, amarg, anēš(ag).
2384:immortality ahēšīh, amargih, anēša- gih.
2446:innumerable amar, anēšmār, азар.
3344:reckoner āmārgar.
3345:reckoning āmār(išn), hangārag, mar, óámárag, ūšmārišn.
3933:tamarisk gaz.
4129:undying amarg; v. immortal.
4247:waist kamar.
4987:kardagān 1%kardāg kam kamāndār kamān kamāl kamālīg kamistīh ‘kamist kamzor kamzorih kamar kamarband maygt arz! kastār kastärīh kchtar kaf
=== NYB ===
384:amar [?m?’l] account; the Reckoning which the individual soul has to go through after death, and mankind at the Resurrection 6411.27, 7923, 8418; scour- ge 4222; kunišn x it is the act that counts (on which the Reckoning after death is based) 6427, — Paz. NP ämär. From Av. (1142 sq.) ?mar-, originally hmar-, cf ošmurtan; Arm. lw. hamar; Targ. Talm. ^"mrkr ‘cashier’. Bailey, BSOS VI, 1930, 65 sg.; Telegdi 227.
2847:čošmurtan ["wšmwltn'] ēšmur- (ēšmār-) to reckon, to calculate, to account for, to enumerate: 4674. 105?'; to count among (apäk) 10917; — v. n. ošmurišn pred.: one must calculate (deliberate) 381%; for an inf.: (den) pat ēšmurišn ravēt he will come here to give an account of the Religion 597. — < *avis-hmár-, *avis-hmr-, from aviš + Av. (1142) ?mar-, orig. *hmar-, Skr smar-; MPrs act. 'šm?r-, pass. ‘$myr- ‘to reckon’; Paz. x“asmur- dan, xuašmaridan (for xoš-, with secon- dary aspiration); NP šumurdan šumār.
3789:togčh [twgyh] account: ~ dahét 6 dévan he will settle an account with the devs 4619-11, _ FrP 30, Cod. K has (not recog- nized by Junker) twg. hwl. šm’l, Paz. tug. hmär. $mär, that is in BP: tog: hmar,
3790:šmār, the lemma signifying: ‘tog = ac- count, reckoning’. Paz. hmar represents the NW form of SW āmār, g. v.; Arm. lw. toiž < *tauža- ‘fine, penalty’, tugan < *taugana- id., v. further s. v. tērtan and ham-tožik. — Coincides in spelling with tangēh, but 4619-3! must refer to the Last Judgement, thus to the last settle- ment of aecounts.
4221:tviščk [wSyk] distressed, to be read in this way 1912 instead of my *ny’dk'; distressful, tormenting, or the like: ni- part <i> tvišek 1079, thus to be read in- stead of nplt' w g'dk' (West: dahik). — This w. has not been recognized by Ind- ian text editors though it is found in the MSS; cf andar bimeh hac āmār u tars ~ in fright of the Reckoning and tor- menting fear DD ch. 27? (p. 49), where Anklesaria has *wyhyk' in the text, but quotes in the critical apparatus wšyk from Cod. K 35 and still another MS. This form is now confirmed beyond
```


## [2026-09-07T16:15:37.633Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9690,9780p' CHEUNG.txt",
 "description": "Cheung *(H)mar entry"
}
```


### [2026-09-07T16:15:37.683Z] TOOL RESULT

```
9 The initial š- found in several Iranian forms is because of ruki (after prev. *ni-, 
*abi-, etc.). 

«PIE *sjeuH)- ‘to sew’ = LIV: 545 | Pok.: 915 f. 

*IE COGNATES: Hitt. /sum(m)anza(n)-/ ‘string, rope’, Lat. suere, Russ. sit’, SCr. Siti, 


Lith. siüti, Latv. süt, Goth. siujan ‘to sew’, Engl. to sew, etc. 
*REFERENCES: IFL II: 279a; DKS: 483a f.; Abaev, Slovar’ IV: 258; Werba 1997: 382; Steblin-Kamenskij 
1999: 335; Shahbakhsh: s.v. gusad- 


*hmar ‘to remember, recall; to count’ 

*AVESTAN: (S)mar- ‘to remember, recall’ || (+ *abi-) ‘to curse (in thought)’ || (+ 
*upa-) ‘to recite; to have an oral agreement’ || (+ *pati-) ‘to recall; long for’ || (+ 
*fra-) ‘to recite’ = Liste: 43 

Pres. them.: IND. 3sg. YAv. fra.maraiti (N 23, N 38, N 42), 3pl. OAv. maronti (Y 43.14), YAv. 
fra.maranti (N 52), YAv. paitismaronti (Y 23.3, Y 67.3), med. YAv. paitismaronte (Yt 8.5, Yt 8.41, Yt 
8.48), SUBJ. 3sg. YAv. marat (Y 19.6), med. 3sg. ? YAv. framaräite (A 4.5, A 4.7), 3pl. YAv. “maranti 
(FrW 4.1), OPT. med. 3sg. ҮАУ. upa maraeta (V 4.45); Aor. athem.: OPT. 3sg. YAv. mairiiat (V 3.33); 
Partic.: pres. marant- (Y 31.1, P 12), med. YAv. maramna- (Y 55.6, Yt 5.86, Yt 16.17), med. YAv. 
paitismaromna- (Y 55.6, Yt 5.11, Yt 5.123, Yt 10.86), red. ҮАУ. aipi hismarant- (Yt 10.45), perf. pass. 
Y Av. aiBi.smarata- (Yt 14.34), Y Av. upa.morota- (V 4.48); Caus.: pres. IND. 3sg. YAv. (“)märaiieiti (Yt 
14.29, Yt 16.7) 

*MIDDLE PERSIAN: MMP ‘Smyr- ‘to be reckoned, accounted’, MMP ’sm’r- ‘to count, 
reckon’, BMP ml /mar/ ‘calculation, number, account’, BMP milk /marag/ || (+ *abi-) 
ВМР ’wsm’I- /ösmär/, ВМР "wsmwl- /ösmur-/ (caus.) ‘to (ac)count, reckon’ || (+ 
*а-) ВМР ”m'l”- /ämär-/ ‘to reckon, calculate’ || (+ *pari-) MMP prysm’r ‘account’ 
c DMMPP: 93b, 57b, 283a 

Partic.: pres. MMP 'smyr'n ‘being counted, calculated [of autumn, spring] || (+ *abi-) Pres.: IND. 3pl. 


BMP ’wsmwlynd /osmurend/; Partic.: perf. pass. BMP "wsmwltk /osmurdag/, BMP "wsmwit /osmurd/, 
ВМР ’wsm’lt /osmard/; Inf.: BMP ’wsm’lynytn /6smarénidan/ || (+ *а-) Pres.: IND. 3р1. BMP /amarend/ 
*PARTHIAN: ‘Sm’r ‘number, counting’ || (+ *a-) IPth. "hmr-kr ‘accountant, économe’ 
c DMMPP: 93a 

*KHOTANESE: sumär- (sa’mar-) ‘to count’ || (+ *pati-) patámar- (pammar-) ‘to report’ 
= SGS: 128, 67 


138 *(h)maué ? 


*SOGDIAN: SSogd. ’sm’r, BSogd. sm’r, CSogd. sm’r ‘to think, consider’ || (+ *pati-) 
SSogd. ptšmr- ‘to count’, CSogd. pcmr- ‘to reckon, consider’, MSogd. ptsmr- ‘to 
think, count’, BSogd. ptšmyr-, MSogd. ptsmyr- (pass.) ‘to be counted, reckoned’ 
Widely attested: Pres.: IND. 1sg. BSogd. 'm'r'm, dur. CSogd. *Sm’rmsq, 3sg. BSogd. sm’rt, CSogd. 
sm’rt, BSogd. $m "rt, etc. || (+ *pati-) Pres.: OPT. 3sg. CSogd. pemry, 2р1. SSogd. ptšmryóy; Pass.: pres. 
IND. 3sg. BSogd. ptsmyrt, BSogd. ptsmyrty, SSogd. ptsmyrty, MSogd. "ptsmyrty; Partic.: perf. pass. (pl.) 
SSogd. ptsmrt’yt, Inf.: pret. MSogd. ptsmrt 

*CHORESMIAN: ’/mr- ‘to count; consider’ (*hismara-) = Samadi: 111 

*BACTRIAN: (+ *4-) avpapo ‘account, settlement’ || (+ *ham-) vopapo ‘account, 
total’ > S-W, Bact.: 183b f., 228a 

*NWIR: (with pref. ?) NP Sumurdan/Sumar-, Kurd. Zmärtin, Zmärdin/Zmör- ‘to count, 
account for’ || (+ *abi- or diff./without pref. ?) Abyan. özmardan, Anar. -iSumort/ 
(impv.) wer-usmor, Gz. ösmär-/ösmärt, ismärt, Khuns. (t)ismar-, Smar-/1smurt, Mah. 
-ismärd ‘to count, reckon’ || (+ *à-) Zaz. ämordis/ämoren-, (Kor.) ämärt-/ämär- ‘to 
count’, NP amar ‘numeration, calculation’, Kurd. aZmar (f.) ‘number; account’ (a-: 
"prothetic" ?) || (+ *ham-) NP hamar ‘number, quantity; measure’ 

*NEIR: Yi. imar-/imur, M. yumar-, Pash. $mörol ‘to count’ (LW ?), Oss. I. mært 
‘measure of dry substances, chiefly of grain’, Pash. dö-mra ‘so much’, cö-mra ‘how 
much’ || (+ *pati-) Oss. D. fzesmarun/£esmard ‘to know, be known; to find out; to 
recall’, Yzgh. pamar- ‘to wait for’ || (+ *ni-) Oss. I. nymzr, D. (med)nimer ‘on 
account of 

*MISC: (+ *à-) Orm. amar-ök, amar-ék ‘to hear’ = amar-/amarók, mar-/marök || (+ 
*ham-?) Arm. (LW) hamar ‘number, account’ 

*SANSKRIT: smar ‘to remember, to become aware, to be mindful of? (RV+) 
= EWAia II: 780 

9 The wide range of meanings which can be assigned to this root is odd: it may 
indicate the convergence of two IE roots ? Cf. LIV: Le. 

*PIE *(s)mer- ‘to observe, consider, think of || *smer- ‘to earn, get a share’ => LIV: 
569 f. | Pok.: 969 

ТЕ COGNATES: Gr. ї1ңєїрө ‘I desire, long’, Goth. *maurnan, OHG mornén, OE 
murnan, Engl. to mourn || Gr. реїіророл ‘I get a share’, (perf.) ëuuope ‘has a share’,
```


## [2026-09-07T16:15:46.357Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '17705,17750p' CHEUNG.txt",
 "description": "Cheung *marH block/hinder gumardan"
}
```


### [2026-09-07T16:15:46.413Z] TOOL RESULT

```
KPF II: 204; Christensen, Contributions I: 166 £, 261; Abrahamian 1936: 115; Bailey 1936: 341; 
Lambton 1938: 72a, 78a, 42a; MacKenzie 1966: 102; EVS: 45a; Abaev, Slovar’ II: 27 f.; DKS: 335b f., 
375b, 460b, 87a; WIM I: 69; Werba 1997: 312 f.; Cabolov 2001: 644; Lecoq 2002: 128, 130, 133, 135 
(passim); Kiefer 2003: 201 


*marH ‘to block, hinder 

*MIDDLE PERSIAN: (+ *ui-) MMP gwm’r- ‘to appoint’, ВМР gwm'l- /gumär-/ ‘to 
appoint, entrust, commission’? > DMMPP: 167a 

Pres.: IND. 3sg. MMP "gwm'ryd, IMPV. 2sg. BMP gwm’! /gumar/; Partic.: perf. pass. MMP gwm’rd, 
BMP gwm’Itk /gumardag/; Inf.: BMP gwm’Itn /gumardan/ 


*NWIR: (+ *ui-) NP gumästan/gumär- ‘to put someone to work, appoint; to send; to 
send back; to employ; to let alone; to give permission, authorize; to deliver, set free; 
to entrust, rely on’. 

9 Cf. Dehkhoda: 16995b f.: 

||... os £ Sa ||... oS) Ale ||... gous ||... oS vi, GT ol 2 b || 
ge ушш уй. ||... 535 ls oasis; ||... gale a, э Ы ||... AUS Ka. || As for the 
semantics, cf. Pth. hyrz- ‘to let, leave, abandon; to establish, appoint’. The meaning 
of the Pers. verb was probably originally *‘unblock’ (with negative/reversive *ui-): 
> *'to let go, allow’, etc. 

*NEIR: (+ *ni- ?) Yzgh. némar-/némard ‘to stop’ || (+ *nis-) Sh. (Baj.) 
niymar-/niymart ‘to be obstinate’ 

*SANSKRIT: mar ‘to hinder’ (RV) > EWAia II: 321 

«PIE *merH- ‘to hinder, block = LIV: — | Pok.: 970 

*IE COGNATES: Lat. mora (f.) ‘delay, obstacle’, Olrish mar(a)im ‘I stay’, Bret. mar 


‘doubt’ 
*REFERENCES: EVS: 49b, 48b; Werba 1997: 313 


*marš ‘to forget’ 

*MIDDLE PERSIAN: (+ *fra-à-) MMP fr’mws-, ВМР pl’mws- /framos-/ ‘to forget’. © 
Henning 1933: 185 is sceptical about the connection of the Persian forms with 
*mars (on account of the Pahlavi and Manichaean forms), for which he quotes
```


## [2026-09-07T16:16:02.332Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT mant- ===\"; grep -n 'mant-\\|mantay\\|^mant\\|maṇt' BRT.txt | head -20; echo; echo \"=== BRT -vant ===\"; grep -n 'Suffix.*vant\\|-vant-' BRT.txt | head -10",
 "description": "Grep Bartholomae mant"
}
```


### [2026-09-07T16:16:02.391Z] TOOL RESULT

```
=== BRT mant- ===
2443:manttve  könnten  sich  der  Bildung  nach  genau
4065:•  j,  a-fraäi'mant-  Adj.  'sich  nicht  vor- wärts, weiter  bewegend':  strqtn  m&nhs hür5  .  .  ysi  para  a/tmät  käme  gätvB dar)y?tit  hUtinia  -manlS  Vt  y.  S7-
5494:•  j.  ara^a'mant-  Adj.  sva.  'an^a-z rasnvö  'mal  (ASn.)'*  bairilta  (sd.) , .  tlyüm nijaynUia  Yti2.7.
6773:3  83  'ahu-  —  'ahumant-  284
6796:g,  6,  2 1 ;  —  'ns  vairy3  fraoxts  H.  7. 4 ;  —  '  J-  'ahuimant-  Adj.  'der  emen  Aha  be- tam  paoiryd  zara>ustra 'npfn  vatrlm  fra-'^'^^'  stets  neben  ra/»;«^;,/.  (sd):  *"».a/'> irävayJvTb>r^>wa>,tfm{%^),lxtairJm{sA.)  ratumai  vaktnmi  vaocata  wzs  tin%n  Aha apar?tn  xraozdyehya  (sd.)  frasräiti  V.o.  "°°  ^"^"^  *""  '  "^^  "^°°'^t  das  beste" i4;V.in.2,YtiQ.8i;—panra  'na  vairya  P-'^'?)i  —  'mais  raiumatö  alaonö  asahe JrasravaySisW.n.z;    77.6,   7Ä43,  70.  zi;   '•■^^Sa-J  Vr.7.5J>;  —   'm^^m  rafummism
6800:•  j  'ahu'mant-  .'Vdj.  'das  Wort  aha  ent- haltend': aita^  vacS  . .  yat  'mat  yat  raiu- mal  "der  Spruch,  der  die  Worte  aha  und
9826:•  j.  'gaomant-  m.  EN.  eines  Gläubigen : 'matS  zavanS  (sd.)  .  .  a!aonö  Yt  13.  1 2  5.
10503:•  j.  gramant-  Adj.,  PPA.:  s.  gram-.
10625:•  j.  xratu'mant-  Adj.  'einsichts-,  weisheits- voll': xitvS  yal  ahmi  xralu^  hapta'hd  °ma yt.l.j;  ¥.6.
16284:•  j.  pouru.'mant-  Adj.  '(viele  enthaltend sva.)  zahlreich  besucht":  •maiti  hanjamame Y.  iu  2.
17088:•  j.  bänu'mant-  Adj,  (fem.  °maitf-)  'strah- lend, glänzend':  xsa%raheäi  paiti  'mats Vt  JJ.  13s;  —  aH  srxre  . .  'maiti  (VSf.) Yt.  ij.  6.
18053:•  j.  frasu'mant-  Adj.  (fem.'maifl-)  'sich vorwärts  bewegend,  beweglich' :  dansa  na pairyaoxlaca  taus/a/iä  *äd)rfydte  nyäe a^tanavaitls  vlspä  'maitls  (APf.  statt  n.) "durch  Blick  und  Zuruf  Überwacht  man (alle)  leblose,  leitet  man  alle  lebende  be- wegliche Habe"  P.5*'>.
18382:Zum  V.ßav.  —  l-a.  (lu  S.  i):  ßSnisnSt,  erl.: awsäyiin,  NpO,  (m  YL  3.  8);  aßäym!där  i lamäm  rama,  (lU  S.  l):  ßavihUtl  rama,  erl.: ayädat  kutmnda  rama  iyaäia  i  yatd&n  htnan- liagän.  —  i)  Dvandva,  bei  dem  jedes  Glied mil  einem  Adjektiv  verbunden  i*t;  falsch  BB. lO.  268.  —  »)  Doch  wohl  *va.  'die  Üppigkeit der  Heerden'  oder  'die  üppigen  Heerden'.  — J)  Vgl.  tßau-  No.4.  —  *)  S.ßumant-  No.  3.
18397:Hai  an  i  a/ünermii.  —  4)  Lies/iwiSuin?  S. za  ßaonay-  anA /sümant-.  —  S)  So  Päs.  Eine Veralüramelung  von  -üäitryö fiuy^;  V.  /Ä  ai steht  n  a  ddt  r  dn  p  dah.
18408:•  j.  fsü'mant-  Adj.  'der  sich  Vieh  hält': *mS  asti  aiava  virTirajä  vahi^S  ßois /ar3k>r»nahl . .  hscä  nä  °mä  nisan/taraiu "wer  sich  Vieh  hält,  hat  das  Anrecht (Sp.  3  53  0.),  ist  siegreich,  der  frommendste; den  Viehbesitzer  rühmen  wir  . .  und  der Mann,  der  sich  Vieh  hält,  soll  .  ."  Y. 58. 4  *';  —  unter  den  Namen  AhM.^\  -m& tiama  aAmi  */säiS  ma%ra  nama  ahmt YLM3.
18577:I04I  naohuämant-  -
18579:•  j.  naehui'mant-  m,  Name  eines  Bergs
19852:•  j.  mant-  V,  'rtihren';  nur  mit  Praev. Piaes.  12  b  manä-'^i  j-Aor.  i  mqi-.
21544:•  j.  *yäta'mant-  Adj,  'reich  an  Besitz, vermögend':  maiyänam..  •maiam  V.20. i.
21547:yätumant-

=== BRT -vant ===
24262:Eig.  Bed.?  —  ■)  So  Kl. I«  j.  vi-vant-  Adj.  (fem.  •väitl-),  V?.\.: s.  pa(>)-'>. O  Mit  No.  3.
```


## [2026-09-07T16:16:04.845Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD -ōmand ===\"; grep -n -- '\\-ōmand\\|-6mand\\|ōmand \\[' PHD.txt | head -10; echo \"=== PHD grep omand ===\"; grep -n 'wmnd\\]' PHD.txt | head -5; echo \"=== NYB omand ===\"; grep -n 'omand\\|ómand\\|-mand' NYB_vol2_glossary.txt | head -10",
 "description": "Grep MacKenzie/Nyberg -omand"
}
```


### [2026-09-07T16:16:04.912Z] TOOL RESULT

```
=== PHD -ōmand ===
256:bayaspānļīh: mission, embassy. ~ig [-yk'] post-(horse). Бах [Pc | N ~] hawk, falcon. bāzā [b’c’y | (N bāzū)] arm. ~banag [-p'nk'] arm-guard, brassard. bazaģ [bck' | М beg, N ~a] sin, evil. —ih: = bazag. bazakkar [bckkl | M bzkr] sinful, sinner. bāzā-zanišnīh [by znfnyh = Av. bázu.jata-] a degree of sin. bazišn [dcšn'] division, part. bazm [bzm | — M, N —] meal, feast. ~-awurd [-zolt! | N ~] a sort of canapé. 1bë [BRA < A br | MP] but; out; ~... (enya), except. ~...enya...né: except... (otherwise)... not. ~ az: without. m 2be [BRA | M P, N bi-] particle with verbs, with 6, of indefinable function. -bed [-pt' | M -byd, N -balilud] suffix, -lord, -master. bēdom [bytwm | M bydwm] furthermost. béganag [byk’nk' | N ~a] strange; stranger. bégar [byk”/ | N ~] corvée, forced labour. béh [byh | N bih] quince. bel [by] | (M. Бу), N ~] spade. bélür [bylwl | M bylwr, N bilür] crystal. bérón [bylwn' | M byrwn, N bérün] outside. bëš [bys] pain, sorrow; harm, hostility. — burdan: bear hostility. bēš-, —i&n, v. bištan. bēšāz [byš(*)z] healing, medicinal. bēšāz(ēn)- [by?z(yn)-, byf?)c(yn)- | M byP?z-] heal, cure. —išnih: healing. bēš-burdār [byšbwlť’[] hostile. bëšidan [bysytn'] = bištan, bēšūmand [byš?*wmnd] sorrowful. béwar [Буш | M bywr, N ~] myriad, ten thousand. P bid [руй | P byd] again. bidaxš [byths] viceroy. *bifagàn [bch'n!] medicinal. bim [bym | = M, N ~] fear, terror. ~gén [-kn'] fearful, terrible. ~génih: fearfulness. --6mand [-'wmnd] fearful. *bistag [bstk! | N busta] hazelnut. biš [byf | N —] aconite. bištan, bé&- [bys-in' | M by$t, bys-] hurt, torment. ~išn: harm, torment. bize&k [dešk! | M bzyšk, N pizišk] doctor, physician.
680:žzēn [zyn! | N zin] saddle. zēn-abzār [zyn'pe!l | N zinafzár] horse-armour. zēnāwand [zy>zond] alert, vigilant. zēndān [zynd?n! | = M, N zindān] prison. «bān [-p?*x! | N -ban] jailer. ~ig [-yk! | N -i] prisoner. zënënidan, zënën- [zynyn-ytn!] look after, preserve. zēnhār [zyn)?] | N zinhàr] protection. zénig [zynyk!] armed. *zibāl [zb | N zībāl] swift (horse, etc.). zih [zyh | N zih] bow-string. zindag [zy(w)ndk! | M zyndg, N zinda] alive, living. ~th: life. zindakkar [zywndkkl | M zyndkr] vivifier, reviver. zinénidan, zinén- [zynyn-ytn'] damage, harm. zirak [zylk' | M zyr, N ~] wise, clever. zistan, v. ziwistan. zišt [zyst! | = P, N ~] hateful, ugly. ziwénidan, ziwén- [zywyn-ytn! | M zywyn-] vivify, revive. zi(wi)stan, zi(w)- [zyz-stn! | M zywystn, zyw-, N zistan] live. zi(w)išn [zywšn! | M zyysn] life; livelihood. ~ih: life, living. --6mand [-”xmnd] living, alive. ziyānaģ [zyd?nk'] young woman. zīyišn, v. zī(w)išn. zofāy [zwp'd | M zwp’y] deep; depth. *~ih: depth. ` zofr [zwpl | M zwwpr, J zwrf, (N žarf)) deep. —šy [2d] depth. ~-payag [-p'dyk'] deep. zóhr [zwhl | M zwhr] libation, offering. zor [z())wl | M zwr, N ~] power, strength. Bay ge J ~ig, ~dmand [-yk!, -wmnd | M -mnd, N —mand] powerful, strong. d z^ 201 [zwt! = Av. zaotar-] first officiating priest. ~ih: office of 201. Zraw-, v. zruftan. !zréh [zlyh | P zryh] sea, lake. *zréh [ziyh | N zirih] armour. zruftan, zraw- [zlwp-tn'] = azruftan. zūd [zwt! | M zwd, N ~] quick(ly). ^h : speed. zür [zwl | M z*wr] false, deceitful.
=== PHD grep omand ===
170:abilag 5/4! | N ~a] blister. a-bim [bym] fearless. āb-kāmag [5A mk! | N ~a] a thick, sour soup. abnüs Pžēnws | (N ābnūs)] ebony. a-biy Pbwd] senseless. ~ih: senselessness. à abr РЫ, Séi | N ~] cloud. M bel abrang [ing | N aurang] glory, splendour. abrastan, abraz- [AP stn',SPc- | М ?br?st, N (afráttan), afrdz-] lift, raise. abraz [Pe | N afrāz] acclivity. abrēšom Pflyš(u)m | M? bryfwm, N ~} silk. ~én [-yn!] silken. abróxtan, abróz- ['piwhtn', ?phoc- | M brwxt, ?)brwc-, N afróxtan, afróz-] light, kindle, illuminate, polish. ~i$n(ih): illumination. āb-tazan Pftcn!] watercourse. a-bun [*dwx!] baseless, bottomless. a-burd-framān ['bwltplm^n'] disobedient. ~th: disobedience. aburnāy f(w)lnd, v. purnāy | N burnā] under age, child. ^h : childhood. aburnáyag [?A(w)/n’(d)yk'] child. abus [pws] (woman) having just given birth. “АҺ: childbirth. арив, -tan Pws, -tn! | M ’bwws, v. ábestan] pregnant. „il: pregnancy. abydxtan, abyóz- Phywhtn', ?bywc-] join, mix. āb-zan zn! | N ~] bath. labzar [el pel] M *6c*7, N afzār] instrument, means; spice. *abzar [6271 | M bail skill, power; powerful. „ūmand [-wmnd] skilled, able. abzāy-, —išn, у. abztidan, abzón [?pzwn! | M, J ”*bzwn, N afzün] increase, growth. ~ig [-yk!] increasing, expansive, bountiful. ~igih: bountifulness. abzüdan, abzáy- ['pzwtn!,^?pzd- | M ?bz'y-, N afzüdan, afzāy-] in- crease, grow. ~i$n: increase, growth. a-čār [cI] inevitable, Jee ~ag [-k'] compelled.
189:áhüg [TYBA < A ру; ”hwk! | MQyhwg, N āhū] gazelle. ahunawar [hnw!] the holiest prayer, beginning Yadā ahū wairyē. a-hunsand [Phwnsnd] dissatisfied. ^h : dissatisfaction. ahy [KZ Y < А k-zy | М hy] soon(est), first. ajģahān [>20/?л! | М ieikin, N azgahan] lazy, indolent. “АҺ: laziness, indolence. ak P! | N dk] evil, harm. -ak LIN ~] diminutive suffix. a-kámagómand [k mk’ wmnd] unwilling. a-kanārag ['kr?]k! | M ?qn’rg] unlimited, boundless. ~ih: boundlessness. a-kard Pārt! | (M °gyrd)] not done, undone. Akoman ['kwmn! | М ?qwmn] Evil Thought, an arch-demon, akómand ["£wmnd] evil, harmful. alā [Py] oh! alas! Аар [STLA, STRA < A £t ;?lk! | (М rel side. alálag PPH! | N lala] anemone. ālāy-, v. ālūdan. Aleksandar Piksndl | M *Ixsyndr, N Iskandar] Alexander (of Macedon). almās(t) Pim?s(t') | (M ?rm?s), N almas] steel; diamond. аадар [?/wtk'] defiled, polluted. АҺ: defilement. ālūdan, ālāy- Photn!, *Pd- | (M ?rwd), N ~] defile, pollute. Aluh Plwh | M "If, N ~] eagle. Xum [lum] millet. N~ amā [LNE < A l-nh | М ?*°h, N má] we, us. Amadan, āy- [Y ATWN-tn! < А y twn, V*th | M?mdn,?y-, N ~] come. amahraspand [?mhrsbnd | M (?)mhr’spnd] a Holy Immortal, a-mar [ml] countless, innumerable. amar [ml | N ~] reckoning, consideration. āmār- [?m?1-] reckon, calculate. ~išn: reckoning. a-marag [mlk') countless. amaraģān [?mlk’n'] generality, commonalty. ~ig [-yk'] general. ~iha [-yh’] in general, generally. a-marg [mig] deathless, undying. ~ih: deathlessness, immortality. ámárgar [?m’lgl | N ~] reckoner. amāwand [?m'wnd] powerful, strong.
219:āsn [?sn'], ~ xrad: innate wisdom. ásnidag [snytk'] = āsnūdaģ. asnüd(ag) [^snwt(k)'] cleansed, purified; pure, noble. a-sohisn [Pswhšn') unfeeling. Я asp [SW.SY A < A swsy’; sb | N ~] horse; (chess) knight. Ha 5Р7 aspánür [sp nwl] tomb. a-spās [’sp’s] ungrateful. aspast ["spst! | N ~] clover, lucerne. NM aspinj [^spnc | P “рулу, N sipanj] hospitality; inn. ШУ "Sy Me asprés [?splys | N ~] race-course. asré Pslwk! = Av. Gbrawa] priest. ~th : priestly office. Asré-kerpa [slzv(k)!klpk = Av. ādrē kahrp-] the form of fire. asrón Pslwn! = Av. āfrawan-) priest. last [AY T! < A?yty | M °st, N <] is, exists. ~ih : existence. *ast(ag) [*st(k)! | M ’st(g), N hasta] bone; (fruit) stone. astānaģ [s??nk!] need, misfortune. ~Smand [-wmnd] needy. āstār [s] | M ?sbr] sin. āstārēnīdan, āstārēn- (^s? ]yn-ytn!] cause to sin. āstawān [*stwb'n', ?stwp^n! | M ”stw?n] confessing, professing. ~th: confession, belief. astódàn [?stw(k)d’n' | M ?stwd^?n] sepulchre, ossuary. astómand [?st?zomnd] corporeal, material. ~th: corporeality. astux4n [sth(w)’n' | N ustux"án] bone. astwand ['stwnd | — M] — astómand. Astwihād [?stwyd’t'] the demon of death. āsūdan, āsāy- [*swtn!, ^? d- | N ~} rest, repose. —išn: rest, peace.
256:bayaspānļīh: mission, embassy. ~ig [-yk'] post-(horse). Бах [Pc | N ~] hawk, falcon. bāzā [b’c’y | (N bāzū)] arm. ~banag [-p'nk'] arm-guard, brassard. bazaģ [bck' | М beg, N ~a] sin, evil. —ih: = bazag. bazakkar [bckkl | M bzkr] sinful, sinner. bāzā-zanišnīh [by znfnyh = Av. bázu.jata-] a degree of sin. bazišn [dcšn'] division, part. bazm [bzm | — M, N —] meal, feast. ~-awurd [-zolt! | N ~] a sort of canapé. 1bë [BRA < A br | MP] but; out; ~... (enya), except. ~...enya...né: except... (otherwise)... not. ~ az: without. m 2be [BRA | M P, N bi-] particle with verbs, with 6, of indefinable function. -bed [-pt' | M -byd, N -balilud] suffix, -lord, -master. bēdom [bytwm | M bydwm] furthermost. béganag [byk’nk' | N ~a] strange; stranger. bégar [byk”/ | N ~] corvée, forced labour. béh [byh | N bih] quince. bel [by] | (M. Бу), N ~] spade. bélür [bylwl | M bylwr, N bilür] crystal. bérón [bylwn' | M byrwn, N bérün] outside. bëš [bys] pain, sorrow; harm, hostility. — burdan: bear hostility. bēš-, —i&n, v. bištan. bēšāz [byš(*)z] healing, medicinal. bēšāz(ēn)- [by?z(yn)-, byf?)c(yn)- | M byP?z-] heal, cure. —išnih: healing. bēš-burdār [byšbwlť’[] hostile. bëšidan [bysytn'] = bištan, bēšūmand [byš?*wmnd] sorrowful. béwar [Буш | M bywr, N ~] myriad, ten thousand. P bid [руй | P byd] again. bidaxš [byths] viceroy. *bifagàn [bch'n!] medicinal. bim [bym | = M, N ~] fear, terror. ~gén [-kn'] fearful, terrible. ~génih: fearfulness. --6mand [-'wmnd] fearful. *bistag [bstk! | N busta] hazelnut. biš [byf | N —] aconite. bištan, bé&- [bys-in' | M by$t, bys-] hurt, torment. ~išn: harm, torment. bize&k [dešk! | M bzyšk, N pizišk] doctor, physician.
292:*brinj [binc | (M bryng), N birinj] bronze, brass. ~én [-yx!] bronze, brazen. brinómand [blyn’wmnd] delimited. brištan, bréz- [blystn', blyc- | M bryz-, N biristan] roast. brüg [blwk' | M brwg, N abrü] (eye)brow. büdan, b(aw)- [YHWWN-tn! < A yhwwn, У hwh; bwtn', b- | M bwdn, bw-, N büdan] be, become. bawišn: becoming, genesis. büf [bwp | N <), *büg [bwk'] owl. buland [bwind | = M, N ~] high. būm [bwm | N ~] land, earth, country. ~-€andag [-cndk'] earthquake. Ibun [bwn' | = M, N ~] base, foundation, bottom. *bun [bwn! | N ~] = wan. bunag [bznk! | N ~a] baggage; abode, camp. — daštan: dwell, settle. bun-dahišn(īh) [bzundhšn!, -yh] primal creation. bunih [bwnyh] beginning. buništ [bwnyst! | = M] foundation. ~ag [-k'] principle. bun-kadaģ [bwnktk'] original house, home. bun-xān [bwnh?n'] source. bur-, —išn, v. buridan. burāģ [bzoP RU] cutting, sharp. burām-, v. bram-. burd [bwit! | M bwrd] patient. ~ih: patience. burdan, bar- [Y BLWN-tn! < А У ybl; bwltn', bl- | M Бата, br-, N <] carry, bear, take, endure. ~išn: bearing, behaviour. burdār [bwit!]] bearer; womb. ~ih: patience. burd-ešnēhr [bwit! fnwhl | P bwrdyfnwhr] grateful, thankful. burg [bwig | (Ar. burj)] tower. buridan, bur- [bwl-ytn! | M bwr-, N ~] = bridan. —j$n: cutting. Burz [bwic] the god of agriculture. Burzénmihr [bwlcynmtr!] the third major Fire of Sasanian Eran, that of husbandmen. burzidan, burz- [bwlc-ytn'] praise, honour. ~i$n: praise, honour. —iŠnié : praiseworthy. buš [ро | N ~] mane. būšāsp [bwPsp | M bwsy'sp, N ~] sleep, sloth; dream. * but [bwt! | = M, N ~] Buddha; idol. buz [AZ < A ‘z; Бос | N ~] goat.
=== NYB omand ===
364:akómandihà [>k'wmndyh"] in an evil man- ner, pitilessly, mercilessly 75°. Paz. sub- stitutes for it anačmediha ‘hopelessly’. — From akömand ‘belonging to (the world of) Evil’, aka; v. ak-deneh.
507:(cf 41?" and 89%); ~ fravartak in the letter 1822; — combined with another prep.: ~ 6 pad estat 28%. 1189. 11917 (cf above 1871); ~ 6 ax“ i astomand 401; m andar äyiyänak 409; ~ tdi sdxdn 401; ~ pat óstak 48% (ete.). — b) temporal: ~ sal 2 mazdesn bag’ Šāhpuhr” in the year 2 of the Mazdayasnian Divine Sh. Pl:l; ~ sal "68 in the year 68 P2:1; ~ pat han jamān ka at the time when 41%, adak ~ pat jamän at that time 619; 4214; 3 sap td three nights ago 512-3, — c) figurative: on, about (esp. in headings and book titles), concerning; (reigning) over, (merciful) to, (hostile) to- wards; (means) for; ete.; — with an inf. or a v.n.: in order to 3714-15, 4515; 1185 (continued by inf. + rād, l. 6). - ~ does not govern encl. pronouns; single excep- tion apar-aš 54° (late passage). — Av. (394 sq.) upati, OP upariy; MPrthPrs br; Paz. awar; NP bar. Cf aper. — On MDM 43" v. hàreftan.
559:apazaromand [~-’wmnd] endowed with spiritual forces, pl. cas. obl. ~-dn 1074. apa-zāyišn ['pz'd$n'] increase, further- ance, promotion 879-11, — Paz. aw(a)zàisn.
671:aržānīkēnītan [~-ynytn'] to consider a p. worthy, governing a subordinated clause without an introducing particle, 5318 in a very complicated passage 5317-21, which only seems possible to understand on the following suppositions: a) kū-t bahr hac man bé burt l. 19 is not a gloss, as I have marked it, but is governed by anak tč bavat l. 17 ‘it shall be unhappy for thee that thou hast bereft ...'; b) the clause kē ... aržānīkēnīt hom 1.17-19 is loosely attached to tē l.17; c) for MNW-t L<y> (MS very clearly MNWtl) read MNW kw) LY» = kē tē man, to man being the exact counterpart of LK ^NH = tč an (v. žan) 1. 19 and both signifying ‘thou and I’; d) YBLWN-m l. 18 and 20, and HWH'-m 1. 19, are the Ist. p. pl. coinciding with the Ist p. sg.; e) there is a wordplay between *š = dé ‘food’ l. 18 and ’$ = as (demonic) eye’ 1. 20 (as burtan 'to have a vision', v. 'aš; bahr ‘ministry’, v. this w.). Text: anàk tč bavat, marak, ke t(0» man fratom hac ax" i astomand andar Rdg u Notar hac bahr barišneh āš barom frac aržānīkēnīt hom, kū-t bakr hac man bē burt. niin-ip tē an pat apar-barišneh aš barom u et bavēt kū-t dušcašmiha al zänak nikēram i-t nest ‘unhappy shall it be for thee, little scoundrel, (that thou) — as thou and I first of all men in the material world between Räg and Notar have been found worthy of earning food by perfor- mance of ministry — that thou hast bereft me of the ministry. Now thou and I shall be enraptured in an ecstatic vision, and then it will happen that I shall see thee evil-minded in another house that is not thine’. The passage is the immediate continuation of the incident related in 537-15, Zsprm XII, 7 epitomizes 5316-21 as follows: dwlyslwb BR’ L zltwšt gwpt' "VK cygwnt pltwm HWH'-m b’hl wlweyk BR’ ’pknd HWH'-m ZK tw "NH KR?
674:aržomand [’le’wmnd] worthy, dignified 311. 4715; precious, excellent, comp. —-tar 879. — Paz. arzmand (Mx), arzamand (SGV); NP arjmand.
706:ast ['st' the bones 50!. 10012; +ast- dahišnan corporeal creatures 5571. — Av. (211 sq.) ast-; MPrs ?st, stg. V. astómand.
718:astómand [’st’wmnd] corporeal, material: Qa" i =, v. axt; hic mw né...no corporeal being 1057; pl. ~-dn 59? (cas. obl.). 10513 (cas. rect.) corporeal, material, earthly beings; ~-dn gehän (cas. obl.) 3911-13; ~-an martömän 10519. — From ast; Paz. astimand, Skr. v. srstimant (SGV); cf MPrs 'stwnd, ”stwnd (A-H I) Av. (215 sg.) astvant-.
727:2aš [^5] the independent form of the cas. obl. 3d p. sg. = enel. -$ (g. v.); always preceding the w. to which it belongs; used 1. anaphorically in the interior of a sentence after a part of the sentence which has been placed first for emphasis: andar han Zartuxst | aš hac miyān Gp i hömikän burt || u pat uléh Zartuxšt | aš han i dašn paitištān hac Osan rote burt 5615-1? (Markwart's reading, Cat. 114 n. 1, is a failure); õi (pron.) mar | aš 6 pasčh gàv apāc rānēnīt 485; — not anaphorically: Ot (prep.) fravahr + Zartuxst | aš (viz. the snake) zafar frac zat 4012-13; purr-x"arrahéh i ax" à astómand | aš hac tan xYarrah from his (viz. Zartuxšt's) bodily splendour 377-8; — taking up an encl. -§ at the beginning of the sentence, after a part of the sen- tence which carries a lengthy attribute: api-š hamäk damik i-š apar rāh bit | aš *perävanihit kart 3316-17; — after an ad- verbial phrase beginning the sentence: adak apar pat jamän | aš hanjamanénit mūtak :61° (where aš anticipates mūtak, cf. s. v. -š). — 2. to introduce the apo- dosis (as api-$, adak-i8): after kakar 31?! ; after ka 327. 3319. 341. 565. 5717. 924. after a relative clause 3219, 9824, 100?7— 101?. — Probably identical with MPrthPrs š, written as an independent w. with two dots above (another explanation of this § v. A-H III, Gloss s. v.; ? in a fragmentary context [S] is obscure). Cf am, at, atün, asän.
826:ax" ['hw] existence, life: ~ ti astomand the material, terrestrian world 378. 40! etc., passim. — Av. (106 sqq.) ahu-, anhu-; FrP, Cod. P fol. 7a with the Paz. reading axti and the NP gl. dunyā. Paz. common- ly óx. — Another ax“ v. patvast-axteh.
897:bahrómandeh [—-"wmndyh] the state of being prosperous, prosperity 877.
```


## [2026-09-07T16:16:16.822Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSF mand ===\"; grep -n 'مند' FSF_pages.txt | head -20; echo \"=== FSF leaf for 311 ===\"; grep -n '^\\s*—\\s*311\\|٣١١' FSF_pages.txt | head",
 "description": "Grep FSF for -mand"
}
```


### [2026-09-07T16:16:16.885Z] TOOL RESULT

```
=== FSF mand ===
54:                   ‫نمونه‌خوانی و بازنگری‪ :‬شهاب‌الدین ارجمندی‬
93:‫اسماعیل مهرتاش و باهمکاری هنرمندانی چون‪ :‬بانوچهرآزاد رفیع حالتی‪ .‬ملوک‬
138:  ‫دانشمندانة زنده‌یاد عبدالحسین نوشین است‪ .‬یادآور می‌شویم کهعظمت شاهنامة‬
238: ‫کس از مشک ز آنسان نپیچد کمند‬               ‫کمندی گشاد او ز سرو بلند‬          ‫‪۷‬‬
255:‫گفتار زال را شنود و گیسویش را بهجای کمند بهپایینافکند ت زاال بالابیاید‪.‬اما‬
358: ‫سخنورانی که دیوانشان به‌وسیلهة دانشمندان وارسی و تصحیح شده است‬
686:    ‫مرکب از آرد ‪+‬الف آرزومندی و دعا‪:‬‬                 ‫و شهرها را بیارایند (نسخۀ دیگر)‪ :‬قبه‬
1393:               ‫آفریند ‪+‬الف آرزومندی د‬           ‫از گفخررگانی (رویاسموین ‪:)۲۴۴-۳۰۵‬‬
1605:                              ‫بکار می‌برد‪.‬‬                  ‫پسند تو آمد؟ خردمند هست؟‬
1774:‫دل هوشمند و آهنگ شیر‬                            ‫او ماربودو مار چو آهنگ او کنی‬
1919:               ‫بینداخت رستم کیانی کمند‬                ‫انش خون‬
2098:                                  ‫فار‬                         ‫گه ارمنده‌ای و گه ارغنده‌ای‬
2680:             ‫کنون ای خردمند وصف خحرد‬                    ‫یک پایک او راز بن اندر بشکسته‬
2994:  ‫فرستید بازی منش ارجمند‬                       ‫ووللرس و دکتر معین همه در اشتباهند‪.‬‬
3054:‫‪ ۲۲‬به‬      ‫‪۱‬ص‬    ‫خر دمند‪( .‬یورداود‪ .‬یشت‌هاج‬
3345:‫آرزومندی و‬           ‫ف‬
3400:              ‫«بیفایده و ناسودمند» (برهان)‪:‬‬     ‫پورتغال‪ .‬سخنوران رنگ زرد چهره را به‬
3586:                                                                                    ‫مند‬
3589: ‫ادگزردی کنیدزردباری‬                                               ‫میوه‌دار‪:‬‬   ‫ورمند‪.‬‬
3977:                ‫گاریدونک یزدان بود پارمند‬                ‫اکر پادشاه دیده خواهد زمن‬
=== FSF leaf for 311 ===
```


## [2026-09-07T16:16:18.311Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== v4 pdf 123 (p2040) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==124' incoming/BQT/BQT_v4_pages.txt | head -40",
 "description": "BQT p2040"
}
```


### [2026-09-07T16:16:19.914Z] TOOL RESULT

```
=== v4 pdf 123 (p2040) ===
[pdf page 124]
-4۱< مندیش
اش
و ی گوبند مندل شهریست در زمین هند که | مندبور اس ت که مفلوك وساحب ادبار وسیظه بخت
در آنجا عود بسیار است و عود مندلی پیب آن | وبی دولت باشد - و بمعنی کرفته و خسیس وبی
کوبند؛ و بی‌دیگرمیگویند که عود نه درزمین | بهره از عمت خدا هم هت - وبمعنی غمناد‌یز
مندل میروید بلکه در جزیره ای میروید ووای | آمده است ؛ وبا يك واو هم تویسند همچوطاوی
خط استوا وآبآنرا بمندلمی‌آورد۱ - ودایرهای | او داود وامثال آن » اما می‌باید درست لباشد چه
را نیز کفته‌اند که عزایم‌خوانان پردور خودکشند | دربنجا واو اول بجای بای ابجد واقع شدم است
و درمیان‌آن نشینند. و دعا و عزایم خوانند ۲ - | بنایر قاعده کلیي که بای ابجد و واو بهم تبدایل
وبزبان هندی نوعی از دهل باشد. ‏ می‌بایند .
مندله ؟ - بنتح اول و ناك و لام » منده « بفتح اول بروزن خنده » بمعنی
پمستی مندل است که عود خام و دابرة عزایم مندك است کهکادی و اروایی بلزار و اباب
خوانان باشد - وبکرالت . وعی ازقانی بای | ومتاع باشد ‎٩‏ - وکوزه وسبوی بی‌دسته وکرون
که از آن خیمه وسایبان سازند ۴ .۹# شکسته را هم میگویند ۷ - و حین وفائی
۱ ۹ بمعنی‌نان هم‌آورده اس ت که بعرپی‌خبز کوبنده .
مناءق - بفتح ارل و سکون ثانی وئثالك مد اگم اد مغفف مندت است نما
او کشیده , نام شهری است در هتدوستان ی ۹
بواو کشیده , ام شهری است در هندوستان. 3 اندیشه مکن وغم مخور٩‏ - ونام قلمه‌ای هم‌هست
مندوور ‎٩‏ * با واو » بروزن و معنی | در خراسان *۹.
۱ -« مندل بفتح ( اول وسوم ) » شهربست بهند که از آن عود لیکو خیزد که آنرا
« مندلی > کوبند .» « معجم‌البلدان » ورك : دزی ج ۲ ص ۹۱۸ : متدلی +
۲ «مندله (ه.م.) ۶ مندل , خط عزیمت بو د که معزمان کشند . رود کی( سمرقندی)
گوید : ندید تنبل اوی وبدید مندل اوی دگرنماید و دیگن بود بان سراپ .>
« لفت فری ص ۳۲۲ ۰
در تکلم خراسان مندل ( بکسر میم ) بمعنی پرگار است « فرهنکه نظام >.
ی «<مندل (همم.) ۴ - رك : سروری , جهانگیری » رشیدی .
<مندور (ه.م.) ۳ مندیور (ه.م.) ‎٩‏ - رك : مند که (۱)
۷ -«منده . سبو وکوزه دسته شکته بود ... فرالاوی گوید :
روا نبودکه با این فل و داش بود شریم همی دالم ز هنده. »
« لفت فری ص 4۷۵ ۰.۹
رشیدی این بیت را به (غمس) فغری دبت کرده است. ۸ - باین ممتی مصحف « میده >
(.م.) است . ‎٩‏ - مضفف میندیش( نهی از الدشیدن ) .
۴ نام ولایتی بوده در غور » دارای قلعه‌ای . از قسه‌ا ی که منهاج سراج دروجه تميةٌ
این محل نفل میکند ( طبقات ناسری س ۳۳-۳۲ ) ا<تمال میرود که بفتح میم باشد . میگوید:
دوفراری از نهاوند بغور آمدند و درین ناحیه مقام کردند و گفتند : « زومندیش » آن موضع را
مندریش نام شد .» « تاریخ بیهقی‌چاپ دکترفیاضش س ۷۰ ح؟ * ( البته وجه نميةٌ مزبوریزاساسی
نیت ) و رك : فهرست اعلام تاریخ بیهقی چاپ مذکور -
0 مندلی - بفتح اول وسوم » منسوب به « مندل » (ه.م.) ؛ عود منسوب به مندل .
2 مندور - رك : مندوور » هندپور :
```


## [2026-09-07T16:16:28.172Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==123' incoming/BQT/BQT_v4_pages.txt | head -50",
 "description": "BQT v4 pdf 123"
}
```


### [2026-09-07T16:16:29.367Z] TOOL RESULT

```
[pdf page 123]
منجوق را سر
ی هکنندوسنگه وخاك وآتش‌درآ نکرده بطرف | است بمعنی صاحب درد وغمناك ۴ - و لام نوعی
دشمن(۱) اندازند . از عبر هم هت و آن سیاه و سنگین و کران
نحو 3 ۱- ح منباشد۴ .
.۰ ی
بروژن صندوق, ماهچه ور مند‌آور * - بفتح اول و واو بر وزن
علم راکویند وبمعنی ۱۱ کنجاور ؛ نام ولایتی است غیر معلوم.
چترهم آمده است وآن ره متد بو ر؟ - بابای ابجدیروزن‌لندهود,
چیزی باندکه بجهت | بمنی سیاء بخت ومفلوه و بیدولت وصاحب ادبار
محافظت آفتاب بربالای ۹ . ۹
سوم < ۹ سس
اه دارند - ۵ ۳ ۰
کت او مندعوده ۷ - بنم اول و سکون‌نانی
را یز ۰ و
هل « بروزن سا کال : و فتح ثالث و عبن بی نقطه بوا و کشیده و رای پی
8 9 3 نقطهٌ مفتوح ء بلغت خم لقاح بری است
هد بش ماس با ۹ | و
خداوند باشد وه 7 : ولفاح میوء مردمگیاه است. اگردرشراب بشورد
وخداوند باشد وییشس کی دهتد ش گر 5
در آخر کلمات آید لك ۹ هون اردد
همچو دوت مند پعثی تخنیق (منجنيك) مندالگ « بنتح اول بروزن اند بممنی
صاحب دولت و ارجمند بعنی صاحبپ و خداوند [] کادی وناروایی اسباب وکالا باشد ۸ ۰
قدر و قیمت وحاجتمند» و دردمند هم آزین قبیل مندل » بروزن صندل » عود خام است؛
(۷) خم۱ : خم .
۹ - کانلم قدری در فرهنکه مضصل ترکی خود این کلمه را « قارسی > دالسته » درعربی
یز بهمین صورت « منجوق > و بمعتی قمی علم وارد شده « دزی اج ص ۲:۹۱۷.
۲ - چوزلف بتان جعد منجوق باد گهی بر نوشت وکهی بر کشاد -
آسدی طوسی « رشیدی » .
۴ - در پهلوی 32220 - و بیز 012820 - , اوستایی 12281 - » پموند دارایی و
تصاحب واصاف : هترمند » سودمند » ارجمند » آزمند , داشمند . ورك: ص لد ازدیباچهٌ مولف.
‎٩‏ - جهانگیری باین معتی آورده » ولي درکتب طب بافته شد. و مراج اللغات کوید :
« و بحی بمعنی نوعی ازعنبر شیاه وکران قیمت نیز نوشته‌اند , و ظاهراً به «مید» بیای مجهول
که نوعی ازططربات امت و از گریهٌ زیاد حاصل میشود , اشتباه کردماند و حال آنکه بدین معنی
هم هندی است له فارسی » « فرهنگه نظام > . -ظ. با «مناور» (ه.م.) تمحیف شده .
‎٩‏ <منده‌بور « رشیدی » قس : مندور » ور : جهانگیری . کردیع 126046017 ۰
7 ( ورشکته » بی‌چیز ) « ژایا ص 4*۹ > » معرب از فارسی « مندبور» (بفتح‌اول)
بسست ی کدا « دزی ج ۲ ص ۹۱۸ ۷ - مسحف « متدغورة » ۳ منداغورس « تحفةً حکیم
مومن » . ازیونانی ۸]820۳2806785 * 3280738076 (ض) ۶ دزی ج؟ ص۹۱۸ رکه:
مردم گیاه » استرنگه . ۸ - جهانگیری و رشیدی این بیت مولوی را شاهد آورده‌اند :
رستم و حمزه و مخنث يك پدی علم و حکمت باطل ومندك غدی.
« متنوی چاپ لیکلسن دفتر ششم س ۳۷۳ > « چاپ علاء الدوله س 0۹4 » ومند که ( بشم و3
وتشدید‌آخر (عر) اسم فاعل آزاند؟ا که است بمعنی براپر وهموا رگردیدن ( مکان ) روبران شدن
( از افادات علامه دهدا ) و رك : فرهنگه نظام ‏
```


## [2026-09-07T16:16:44.210Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== TAD leaf ===\"; awk 'NR<=2655{n+=gsub(/\\f/,\"\")} END{print n}' TAD_pages.txt; sed -n '2648,2668p' TAD_pages.txt; echo \"=== pdf page tag ===\"; awk 'BEGIN{RS=\"\\f\"} NR==65{print substr($0,1,80)}' TAD_pages.txt",
 "description": "TAD mastaki context"
}
```


### [2026-09-07T16:16:45.544Z] TOOL RESULT

```
=== TAD leaf ===
72
                   ‫‪ 50261000012‬معناه وحيد القرن وهو الىكدن‬                                  ‫نسا‪-‬نى‬
                                                                                                 ‫ومي‬
                                                                                                   ‫مر‬

                                           ‫معناه رأب" الخردل‬                  ‫مسترده ‪ -‬ايطالى ‪9‬‬

          ‫مسطرة ‪ -‬أيطالي ‪ 801502‬معناه عر"ض البضاعة وغيرها مرادفه مثال‬
    ‫مصطكي ‪ -‬ونانى ‪8‬وعناموه هو عصارة شجرة نشبه الفستق واليطم تمد‬
                                                                         ‫فتتعقد صمعا بعلك مرادفه السك‬

    ‫مكروب ‪ -‬وثانى منحوت من "‪ 804116‬أي صغير و ‪ 5101015‬أي جى وهو‬

                             ‫أن حي يا رغ بالوعن امجردة بعش فى الماء والدم والطواء‬
  ‫و‪ 060‬راقب‬
          ‫وونانى مركب من معازم أي صغير ‪0‬‬                             ‫كرس كونة‬
                                                               ‫ورصد مرادفه مجهر‬
‫النسكاج على الأشيبه ويقال له‬                          ‫‪0 5‬‬
 ‫‪:6‬ن التي فى الاصل معناها سفينة صغيرة ‪ .‬فتوضع‬
                                            ‫‪8‬ية‬
                                              ‫‪6‬فرانس‬
                                                   ‫بالفارسية مُوم وب‪8‬الا‬
=== pdf page tag ===
                               ‫‪ 2-0‬ل‬


                ‫فونا�
```


## [2026-09-07T16:16:45.790Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON مصطکی ===\"; grep -n 'مصطکی\\|مصطكي\\|مصطكى' MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -10",
 "description": "Grep Moin for mastaki"
}
```


### [2026-09-07T16:16:45.852Z] TOOL RESULT

```
=== MON مصطکی ===
incoming/MON/MON_2vol_Adena_v1_djvu.txt:93529:بلد مصطکی» طین جزیرةٌ مسطکی» طین 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:93548:مصطکی: (زم.) طین اقریطس. طین جزيرة 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:93549:مصطکی: (زم.) طین اقفرس. طین جلود: 
MON_part1.txt:93529:بلد مصطکی» طین جزیرةٌ مسطکی» طین 
MON_part1.txt:93548:مصطکی: (زم.) طین اقریطس. طین جزيرة 
MON_part1.txt:93549:مصطکی: (زم.) طین اقفرس. طین جلود: 
MON_part2.txt:27053:رومی: (گیا.) مصطکی. کندر هندی: ( گیا.) 
MON_part2.txt:38762:آن گشنیز خشک و زیرةٌ کوییده و مصطکی 
MON_part2.txt:58754:ساقه و شاخه‌های درختچه مصطکی خارج 
MON_part2.txt:58757:شدةٌ مصطکی به درشتی نخودی کوچک و
```


## [2026-09-07T16:16:53.883Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '58740,58770p' MON_part2.txt",
 "description": "Moin mastaki entry"
}
```


### [2026-09-07T16:16:53.930Z] TOOL RESULT

```
و مرتضوی و مصطفوی به زبادت واو خطا 
باشد چنانکه به اکثر در کلام خواص و عوام 
واقع است. مگر چون در تصانیف ثقات 
سبار آمده است؛ لهذا چندان محل 
نیست. از جاربردی و دیگر کتب و رسائل 
(قیاس. فر نظا.) 

مصطفی: 001017 [ع.] (امف.) صاف گرد 
شده. برگزیده. ضح.- نسبت بدان مصطفوی 
است؛. 

مصطعی: ۱25۱۳ [معر ره معر . 
- مصطکاء معر.) (.) (گیا.) گونه‌ای سقز که 
نطو رت ی هآ ات انتساد شکات از 
ساقه و شاخه‌های درختچه مصطکی خارج 
می‌شود و بصورت قطرات کوچکی در 
محل شکاف منعقد می‌گردد. قطرات سخت 
شدةٌ مصطکی به درشتی نخودی کوچک و 
رنگش زرد بریده و کمی شفاف است و بو 
و طعم آن ملایم و مطبوعغ می‌باشد. . در 
گرمای ۸ درجه ذوب می‌شود و بر اثر 
جویدن به سهولت در زیر دندان نرم 
می‌گردد. مصطکی کمی از آب سنگین تر 
است و در اتر و کلروفرم و اسانس تربانتین و 
به مقدار کم در الکل حل می‌شود. گاهی 
مصطکی بجای آنکه بر روی شاخه‌ها و ساقة 
درخت اقی بماند» در پای درخت بر روی 
و ی و وی 
درمی اید. این قسم نوغ خالص مصطکی را 
تشکیل می‌دهد. نوع اخیر رنگ قهوه‌یی 
دارد و وا دارای ماسه و ناخالصی‌های
```


## [2026-09-07T16:17:03.512Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD smar ===\"; grep -n \"šm'r\\|sm'r\\|smʾr\\|šmʾr\\|thought, imagination\" SOD_pages.txt | head -20",
 "description": "Grep Gharib Sogdian"
}
```


### [2026-09-07T16:17:03.591Z] TOOL RESULT

```
=== SOD smar ===
7595:      (a ^psm'r
8827:1745 >skr- =* 'sk'r-, skr-                                         1760 'sm'r- B, S              jiJ^ioJ^^id}J'jj~&
8845:     (o)skarte ©pp.                                                1763 'sm'r't- S                          b*j+^ ijjL-^jul
25150:7444 psm'r B                         faJL* ^y)<! ^                   pasuyd Opswyt-) ©pt. st.
25151:     (o)p(a)smar ? -^'psm'r                                          OcOpurify, (fo)clean up
26577:        54V18pl06 "be diffused"                            7937 ptsm'r- B, S, C          j^J'^L^- ij^J'J^ io>^
26586:                                                                   ^ptsm'r-, ptsmyrt-
27255:8152 pw'sm'r'kh B                                             8163 pwSpys M
27378:8198 pw ptsm'r             C, B
29151:     (a)skesar ^skys'r                                        8819 sm'rknSc    S                                  ^^~
30406:     (o)sku ©<Av. hisku      ^'skw, swk1, skwy(y)            9256 sn^rn'k/y      B =» sm'rn'y
30424:         yFrag. Len. pl09; kT, Frag. Len. 44.9, 83a4                smarne   (sm*rn}k/y) ^sm'ry^k
30427:                                                                     BSTBL, Dhy. 60, 331, sm>rn% Dhy. 303; sm'rrty,
30428:9261 sm'r-         (oj^j^jJ)o*j~Ztlo*£&"jj>.lo*J'£*
30431:        symfr ^sm'r-
30436:                                                               9274 sm'ry C =* sm»ryy
30437:9262 sm'r" B                                4£*x\iJ*           9275 sm'ryck03 B                         ^jx^^^JJs
30438:     smara (sm'r*, snVrO ©f. n. ^)sm,r', smVkh                      smarick (smVyckO
30442:                                                               9276 sm'ryq C                                  a^j^iJjc^
30447:                                                               9277 sm'rykyn      M                     J* ^ ^LLjjuI
```


## [2026-09-07T16:17:05.727Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN martyr ===\"; grep -n 'martyr, n\\.\\|^martyr\\|martyr,' KLN_1966.txt | head -10; echo \"=== KLN memory ===\"; grep -n '^memory\\|memory, n' KLN_1966.txt | head -5; echo \"=== KLN mastic ===\"; grep -n '^mastic\\|mastic, n\\|mustache\\|moustache' KLN_1966.txt | head -10",
 "description": "Grep Klein"
}
```


### [2026-09-07T16:17:05.818Z] TOOL RESULT

```
=== KLN martyr ===
23022:martyr,  n.  —  ME.  martir ,  fr.  OE.  martyr ,  fr. Eccles.  L.  martyr,  fr.  Gk.  papru?,  Aeol.  and Dor.  pip  Tup,  ‘witness;  martyr’,  which  prob. stands  for  I.-E.  *mptu-  and  is  rel.  to  Gk.  p£- pijxva,  ‘care,  solicitude,  thought’,  pippnjpa  (poet¬ ic),  ‘care,  trouble’,  peppepop,  ‘causing  anxiety, baneful’,  and  cogn.  with  Ol.  smarati,  ‘remem¬ bers’,  L.  memor,  ‘mindful’.  See  memory  and  cp. words  there  referred  to.
23023:Derivatives:  martyr,  tr.  v.,  the  hybrid  noun martyr-dom,  martyrize  (q.v.),  martyry  (q.v.) martyrize,  tr.  v.  —  ME.  martirizen,  fr.  Eccles.  L. martyrizare,  fr.  martyr.  See  martyr  and  -ize. Derivative:  martyriz-ation,  n. martyrology,  n.,  a  study  of  martyrs;  a  history  of martyrs.  —  Eccles  L.  martyrologium,  fr.  Eccles. Gk.  papTopoXo-fiov,  which  is  compounded  of Gk.  pap-ru?  (see  martyr),  and  Xoyop,  ‘word, speech,  discourse,  account’.  See  logos.
23025:martyry,  n.  —  Eccles.  L.  martyrium,  fr.  Gk.  pap-
23432:Derivative:  memoriz-ation,  n. memory,  n.  —  ME.  memorie,  fr.  OF.  memorie  (F. memoire),  fr.  L.  memoria,  ‘memor}'’,  fr.  memor, ‘mindful’,  which  stands  for  *me-mor  and  de¬ rives  fr.  I.-E.  *mer-{s)mer-,  reduplication  of base  *(s)mer-,  ‘to  care  for,  be  anxious  about, think,  consider,  remember’.  From  the  redupli¬ cated  base  derive  also  Avestic  mimara-,  ‘mind¬ ful’,  OE.  gemimor,  ‘known’,  mamrian,  ‘to  plot, design’,  Du.  mijmeren,  ‘to  ponder’.  Cp. — with full  reduplication  of  base  *mer- — Gk.  pcppEpoc, ‘causing  anxiety,  mischievous,  baneful’,  pip- prjpa  (poet.),  ‘care,  trouble’,  peppatpEtv,  pep- pTjpi^eiv,  ‘to  be  anxious,  to  ponder’.  Arm.  mor- mok ‘  (for  *mermero-  or  * mormoro -),  ‘regret, grief’.  The  simple  base  *{s)mer-  appears  in  OI. smarati,  Avestic  maraiti,  ‘remembers’,  Gk.  pipi- llvx,  ‘care,  thought’,  pEpipviv,  ‘to  care  for,  be anxious’,  Serbo-Croat  mariti,  ‘to  care  for’, Goth,  maurnan,  OE.  murnan,  ‘to  be  anxious for',  W.  marth,  ‘sadness,  anxiety',  and  possibly also  in  L.  mora,  ‘hesitation,  delay’,  OIr.  maraim, ‘I  remain’.  Cp.  memoir,  commemorate,  remem¬ ber.  Cp.  also  martyr,  mourn,  smriti.  Cp.  also moratory.
30684:protoma,  protome,  n.,  the  bust  of  an  animal.  — Gk.  TupoTopr),  ‘head  of  a  decapitated  animal’, lit.  ‘something  cut  off’,  from  the  stem  of  7tpo- TEpvetv,  ‘to  cut  off  in  front',  fr.  it po  (see  2nd  pro-) and  TEjivEiv,  ‘to  cut’.  See  tome, protomartyr,  n.,  the  first  martyr.  —  Compounded of  proto-  and  martyr.
=== KLN memory ===
=== KLN mastic ===
2179:Algernon,  masc.  PN.  —  Lit.  ‘with  mustaches  ,  fr. OF.  als  gernons.  OF.  als  (F.  aux)  stands  for  a les,  lit.  ‘to  the’  (pi.),  fr.  L.  ad-  (see  ad-)  and  the plural  of  the  article  le,  fr.  L.  ille,  ‘that  one  ; see  ille  and  cp.  words  there  referred  to.  OF.  ger- non  is  a  collateral  form  of  grenon,  ‘mustache  , fr.  VL.  *grandnem,  acc.  of  *grand,  a  word  of Teut.  origin.  Cp.  OHG.  grana,  OE.  granu ,  mus¬ tache’,  G.  Granne,  ‘awn,  beard’,  fr.  I.-E.  base *gher-,  ‘to  stick  out’,  whence  also  OSlav.  grani, ‘point,  edge’,  W.  gran,  ‘eyelid’,  MIr.  grend, ‘whiskers’.
4971:Bignoniaceae,  n.pl.,  the  Bignonia  family  (bot.)  — ModL.,  formed  fr.  prec.  word  with  suff.  -aceae. bignoniaceous,  adj.  —  See  prec.  word  and  -aceous. bigot,  n.  —  F.  bigot,  ‘over-devout’,  of  uncertain origin.  It  possibly  derives  fr.  Sp.  hombre  de  bi- gotes,  ‘a  man  wearing  mustaches’,  whence  ‘a man  of  a  serious,  solemn  cast  of  mind’. Derivatives:  bigot-ed,  adj.,  bigot-ry,  n. bijou,  n.  —  F.,  ‘jewel,  gem’,  fr.  Bret,  bizou,  ‘finger ring’,  fr.  biz,  ‘finger’.
20587:—  ME.  kempe,  fr.  Scand.  Cp.  ON.  kampr, ‘mustache’,  which  is  rel.  to  OE.  cenep,  OFris. kanep,  of  s.m.
23041:masticate
23085:mastic,  n.,  resin  obtained  from  certain  trees.  — ME.  mastik,  fr.  OF.  mastic,  fr.  VL.  mastichum, fr.  Gk.  \ita~Ay;r\,  ‘mastic’.  See  masticate  and  cp. almaciga.
23088:mastication
23094:mastication,  n.  —  Late  L.  masticatio,  gen.  -dnis, ‘chewing,  mastication’,  fr.  masticatus,  pp.  of masticare.  See  masticate  and  -ion. mastiff,  n.  —  ME.  mastif,  fr.  OF.  muslin  (whence F.  matin),  fr.  VL.  *md(n)suetinus,  ‘tamed’,  fr. L.  mansuetus,  of  s.m.,  pp.  of  mansuescere,  ‘to tame’ ;  see  mansuete.  The  ending  of  E.  mastiff  is due  to  a  confusion  with  OF.  mestif,  ‘mongrel’, mastitis,  n.,  inflammation  of  a  breast  ( med .)  — Medical  L.,  coined  by  Konig  fr.  Gk.  aaoxo;, "breast’,  and  suff.  -tTiq.  See  masto-  and  -itis. masto-,  before  a  vowel  mast-,  combining  form meaning  ‘breast’.  — -  Gk.  p.a paaT-,  fr. [x'/.n-ric,  ‘breast’,  which  prob.  stands  for  *trccS- toi;  and  derives  from  the  stem  of  paSav,  ‘to  be wet,  to  flow’,  fr.  I.-E.  base  *mad-,  ‘wet,  moist, dripping’.  See  mast,  ‘fruit  of  the  beech’,  and  cp. prec.  word,  mastoid,  mazo-,  ‘breast’,  amastia, bimastism.
24535:Derivatives:  mouse,  intr.  and  tr.  v.,  mous-er,  n., mouse-let,  n.,  mouse-ling, n.,  mous-ing,  n.  and  adj. mousquetaire,  n.,  musketeer.  —  See  musketeer, mousse,  n.,  a  dish  made  from  whipped  cream, white  of  egg,  etc.  —  F.,  ‘foam’,  fr.  Late  L.  mttlsa, ‘hydromel’.  See  mulse. mousseline,  n.,  muslin.  —  See  muslin, moustache,  n.  —  A  var.  spelling  of  mustache. Mousterian,  adj.,  designating,  or  pertaining  to, the  late  paleolithic  culture  (geol.)  —  So  called from  Le  Moustier  in  southern  France,  where  re¬ mains  of  this  type  were  found, mouth,  n.  —  ME.  mouth,  mouthe,  fr.  OE.  mild, rel.  to  OS.,  OFris.  miith,  ON.  munnr,  mttdr,  Dan. mund,  Swed.  mun,  MDu.  mont,  mond,  Du.  mond, OHG.  mund,  MHG.  munt,  G.  Mund,  Goth. 7 nunps,  ‘mouth’,  OE.  midi,  ON.  met,  OHG. mindil,  ‘horse’s  bit’,  ON.  minnask,  ‘to  kiss’;  fr. I.-E.  base  *menth-,  ‘to  chew’,  whence  prob.  also Gk.  pd-fluioa  (Hesychius),  ‘jaw’,  paciopxt  (for ♦palHdcopat.),  ‘I  chew,  bite’,  pxaxa^w,  ‘I  chew’, paaxai;,  ‘mouth,  jaws’  (lit.  ‘that  with  which  one chews’),  L.  mandere,  ‘to  chew’,  Ir.  meadal, ‘orifice  of  the  stomach’.  Cp.  malar,  mandible, manducate,  mange,  manger,  masseter,  mastic, masticate,  maxilla,  mustache.
24758:‘drunk,  intoxicated’,  pp.  of  mddati,  ‘boils,  bub¬ bles,  gets  drunk’,  fr.  I.-E.  base  *mad-,  ‘wet,  to drip’.  See  meat  and  cp.  words  there  referred  to. must,  n.,  new  wine.  —  ME.,  fr.  OE.  must,  fr.  L. mustum,  ‘new  wine’,  shortened  fr.  mustum  vi- num,  fr.  mustus,  ‘fresh,  new’,  which  possibly standsfor  *mus-tos, ‘wet, moist',  fr.  l.-E.*meu-s-. See  moss  and  words  there  referred  to  and  cp. esp.  mustard.  F.  mout,  It.  mosto.  OSlav.  mustu, ‘new  wine’,  also  derive  fr.  L.  mustum. mustache,  moustache,  n.  —  MF.  (=  F.)  mous¬ tache,  fr.  It.  mostaccio,  a  collateral  form  of  mo- stacchio,  fr.  MGk.  pcioTcoa,  fr.  Gk.  (auotx;, ‘upper  lip,  mustache',  which  is  rel.  to  y-dtatxi,, ‘mouth,  jaws’,  lit.  ’that  with  which  one  chews’, patCTTt/xoj,  ‘I  gnash  the  teeth',  (Axaxouoa  (for ♦pxfftxouxt ),  ‘I  chew,  bite’,  fr.  I.-E.  base *menth,  to  chew’.  See  mouth  and  cp.  mastic, masticate.
24759:Derivatives:  mustach-ed,  moustach-ed,  adj., mustach-ial,  moustach-ial,  adj. mustachio,  mustache,  n.  —  A  blend  of  Sp.  mos- tacho  and  It.  mostaccio.  See  mustache. Derivative:  mustachio-ed ,  adj. mustang,  n.,  the  small,  half-wild  horse  of  the American  prairies.  —  Mexican  Sp.  mesteho, mestengo,  ‘ownerless  animal,  stray  ,  fr.  Sp. mesteho,  mestengo,  ‘belonging  to  graziers  ,  fr. mesta,  ‘company  of  graziers’,  fr.  L.  mixta,  fem. pp.  of  miscere ,  ‘to  mix'  (see  mix);  influenced  in
```


## [2026-09-07T16:17:23.628Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 23022 23085 23432 24535 24758; do echo -n \"line $L -> leaf \"; awk -v L=$L 'NR<=L{n+=gsub(/\\f/,\"\")} END{print n}' KLN_1966.txt; done; echo \"--- page markers near ---\"; grep -n '^[0-9]\\{3\\}$' KLN_1966.txt | awk -F: '$1>22900 && $1<24900' | head -20",
 "description": "Klein page markers"
}
```


### [2026-09-07T16:17:24.919Z] TOOL RESULT

```
line 23022 -> leaf 506
line 23085 -> leaf 507
line 23432 -> leaf 516
line 24535 -> leaf 541
line 24758 -> leaf 546
--- page markers near ---
22901:939
22961:940
22968:941
22996:942
22997:943
23042:944
23043:945
23090:946
23091:947
23142:948
23155:949
23169:950
23233:953
23300:957
23340:958
23546:966
23568:967
23599:968
23669:970
23670:971
```


## [2026-09-07T16:17:38.927Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"'sm'r\\|'šm'r\\|smara\\|thought, imagination\\|imagination\" SOD_pages.txt | head -20; echo \"=== leaf of 8827 ===\"; awk 'NR<=8827{n+=gsub(/\\f/,\"\")} END{print n}' SOD_pages.txt",
 "description": "Gharib smar entries"
}
```


### [2026-09-07T16:17:40.264Z] TOOL RESULT

```
7593:     (a)pismar ?, (o)p3smar ? ©<*Skt. apasmara                     1336 >ps>nk B                                          <l;<,f
8827:1745 >skr- =* 'sk'r-, skr-                                         1760 'sm'r- B, S              jiJ^ioJ^^id}J'jj~&
8835:                                                                        (o)smara         ©Av. hismar     ©f. n. =^sm}r*
8842:                                                                        (o)smara(k) ^)sm>r,) smVkh
8845:     (o)skarte ©pp.                                                1763 'sm'r't- S                          b*j+^ ijjL-^jul
15812:      yarfi-smarak                                                      4254 yrftyct M, C                             U>>- J^
26568:                                                                patsmar ©<*pati- smara\ Khwar. pcm}r ©ob.
26578:7923 ptsk'f    M =» ptsk}p-                                     patsmar (ptsmr-) ©<Av. patismara- «*pcmr-
27255:8152 pw'sm'r'kh B                                             8163 pwSpys M
27257:     pu-ssmarak                                                    pu-6Pes =*8Pys
30438:     smara (sm'r*, snVrO ©f. n. ^)sm,r', smVkh                      smarick (smVyckO
30454:     smara(k) (sm»r>kh) ©f. n. ^smV, ^mVkGO                         smarene ©pi. -r ^sn^ryn'k
30466:     smaran                                                         sa(m)mase ©<Syr. sammasa ©pi. -t
30470:     smarat ©pp.                                                    smax     ^sm'xCw), fn, ^nVyw
=== leaf of 8827 ===
134
```


## [2026-09-07T16:17:45.701Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==135' SOD_pages.txt | sed -n '1,60p'",
 "description": "SOD leaf 134 full"
}
```


### [2026-09-07T16:17:47.040Z] TOOL RESULT

```
                                                                                                                             'smVt-

 69

       world                                                              BSTBL, Dhy. 200
       TSP 8.189-, >sk}np\ TSP 2.1150; Wnpvv, VJ n p91,             1751 >skrwp B                   (J>jJlt.)j^\^iKjF^
                                                                             dry
         101 etc. >nkynpw, VJ 38b; GMS 366, *skamb-,                     (a)skaruP, askruf ? ©<*skarf
         "to support"                                                    trouble
 1739 'sk'r- B, M, S      (jjjLi:^*)^*^^^^                               SCE 21 n p34;GMS 366,482
      oskar Oskr-) ©<*skar- ©impf. sykr =*sk'r-,                    1752 >skw     B, M

             r-d, (fo)pursue, (fo)chase
          skca
       OcOl                                                              (o)sku    ©<*hisku      =*skw, swk1
       GMS 366, 492; VJ; TSP 2; BSTBL, Padm. 28; SCE
                                                                         GMS 93; Sogdica. 64.13; BBB 486
         251, 394; Frag. Len. 8 R7; Anc. Lett. 3.11; inf.
                                                                   1753 >skw>c     M(S)
         -Wy.TSP        13.2, 12.5                                                                                     lS^JJ>- c<>SJl3>-
                                                                         (o)skuca(+z}y) ©f. adj.
 1740 >skJrt -» sk'rt-
 1741 »gkVt-      B, M,S                                Cp/JU            dry land
                                                                         Sogdica. 64.13; S W, C2 n pl50.26
      oskart      (skrt-, 'skrt-) ©pt; St. \ftfcrttfV-; trans.
                                                                   1754 >skwch       B                                       d~<£
         prct. st. -^sk'r-                                                                                                    */*#
                                                                         (o)skuc ®<*skuth Khot. skat a
       GcOIcad, GcOpursue
                                                                         throat
       GMS 486, 879; SCE 456, 3sg. pot.; AVS 103
                                                                         TSP 6.88; GMS 147 A
 1742 'sk'wrS B                          jr^«o3~
                                                                   1755 'skwch-'ptr'ywstk
      oskorO (sqwrG) ©<*skau0i; MP iskoh
        =»sk}wr5, skwrS                                                  (o)skuc-(o)patrxusk ?
      difficult                                                          having an obstructed throat
                                                                         SCE 390; Gersh. Sogd. Cpds. TSP 1945, 147;
      GMS 361, 366; VJ 259; SCE 288; STii 9.1, 6;                          JRAS 1942, 9
        BSTBL, Vim. 150; TSP 2, 269, >skwr6\ BBB f28
                                                                   1756 >skwr5       B, M =» »sk»wr8, skwr5
1743 ^skVrSy* B, S                                       ^
     oskorGya (sqwr8y\ 'skwrSyO ©f.             =>skwr5yJh,        1757 >skwr5y>         S ^ >sk,wr5y>
       sk'wrSy*                                                    1758 'sm^h => 'sm'yw
     difficulty
                                                                   1759 'sm'yw B, S                            us.
      BSTBL, Vim. 152; Frag. Len. 57.11; MDii pl68.4                    osmaxu, smax Osm'yh) ©<*smdxam\ Yaghn.
1744 >sk)yr- B                        jj^^O-^JL^                           sumax      =^sm}Yw, 'sm'xfw)
     oskir (sqyr-) ©pass. st. =*sk'yr-
                                                                         GMS 157, 1380; TSP 2.672, 827, 1143, 21i 4; Hen.
     (fo)be pursued
      GMS 540-, TSP 2.551                                                  Tales. 478.22; >$m% TSP 2.827
1745 >skr- =* 'sk'r-, skr-                                         1760 'sm'r- B, S              jiJ^ioJ^^id}J'jj~&
1746 >sqr- =» 'nsk'r-                                                   (o)smar ©<*hisman fsmar- =>smJr-
                                                                             you (reconsider, (^)count
                                                                        GcOthink,
1747 'skr'yn*      B                                      i-JLjj
                                                   ^<.                  BSTBL, Dhy.; TSP; MDii; BBB
      oskarene      ^sk^yn'k
      follower                                                     1761 'smV      M                            J^ i<L*x>\ i jyat i £k
```


## [2026-09-07T16:17:51.640Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==135' SOD_pages.txt | sed -n '55,90p'",
 "description": "SOD leaf 135 rest"
}
```


### [2026-09-07T16:17:53.044Z] TOOL RESULT

```
                                                                             you (reconsider, (^)count
                                                                        GcOthink,
1747 'skr'yn*      B                                      i-JLjj
                                                   ^<.                  BSTBL, Dhy.; TSP; MDii; BBB
      oskarene      ^sk^yn'k
      follower                                                     1761 'smV      M                            J^ i<L*x>\ i jyat i £k
                                                                        (o)smara         ©Av. hismar     ©f. n. =^sm}r*
      TSP 2.890, pres. part. pi. >skrWtt, TSP 2.629                     thought
1748 >skrcy B, S                                    j^^
     oskarce/i                                                          Sogdica. 64.9; GMS 93
      pursuit, chase                                               1762 )sm)r1k(h)       B, S   £jj fljal j^J^-)^^        tJ^s i/^as
      TSP 13, Rust, ii, 11; Hen. Tales. 478, 14; GMS
        1008
                                                                        (o)smara(k) ^)sm>r,) smVkh
1749 >skrt- B, M =» >sk>rt-                                             thought, meditation
1750 >skrt}y B                                                          BSTBL, Vaj. 4, 5; TSP 2.756; KG 362
     (o)skarte ©pp.                                                1763 'sm'r't- S                          b*j+^ ijjL-^jul
      pursued, chased                                                   asmar-at         (smr*t-) ©pt. st. =*sm}rt-
```


## [2026-09-07T16:18:03.010Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD mandrel ===\"; grep -n -i 'mandrel\\|mandril' AHD_watkins1985.txt | head; echo \"=== LEW mamphur ===\"; grep -n -i 'mamphur\\|manphur\\|manfur' LEW_1910.txt LAT.txt POK_01.txt POK_02.txt POK_03.txt WLD_band3.txt 2>/dev/null | head; echo \"=== WLD Bd2 mamphur ===\"; grep -n -i 'mamphur\\|manfur\\|menth' incoming/WLD/WLD_Bd2_pages.txt | head -20",
 "description": "Grep for mamphur"
}
```


### [2026-09-07T16:18:03.085Z] TOOL RESULT

```
=== AHD mandrel ===
=== LEW mamphur ===
POK_02.txt:6248:lat.  (osk.)  mamphur,  besser  manfur  ,ein  Stück  der  Drehbank' ;
LAT.txt:36041:mamphur?: - appellatur loro circumuolutum mediocris longitudinis
=== WLD Bd2 mamphur ===
17684:                                             menth-                                     269
17697:lat. (osk.) mamphur „ein Stuck der Drehbank“, nach Meyer-Liibke Phil.
17701:voraussetzen (a und Dental wie bei mando „kaue“ zu menth „kauen“);
17725:   Ehrlich aaO. setzt mit unserer Wz. auch menth- ,,kauen'‘ gleich(?), so-
17744:270                                       menth-   — mendh-
17746:menth- „kauen; GebiS, Muad'^
17760:lich)    e-stufig fieoTaxa  Ti]v f^isjuaorjjuevrjv TQO(pr]v Hes i^menth-to -')
17766:dar^ osk. manfar zu menth- „quirlen“;        ein      ist kein Platz), Vanicek
17769:LEWb.^ 207, Frohde BB. 7, 330;           meadal „Magenoffnung“ {^menth-lo~
17797:  Ehrlich aaO. halt menth- „kauen“ fiir ursprgl. dasselbe wie menth- „quirlen“
17847: ahd. mendl, mendan zu "^menth- ^schiitteln, quirlen''— „geistig erregt sein“);
```


## [2026-09-07T16:18:08.987Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '17684,17700p;17744,17800p' incoming/WLD/WLD_Bd2_pages.txt",
 "description": "Walde-Pokorny menth entries"
}
```


### [2026-09-07T16:18:09.033Z] TOOL RESULT

```
                                             menth-                                     269

  DaU Tinsere Wz. eigen tlich eine -/i(e)Jnfixbildung zu mcgQij- „grofi“ sei
(Fick   104, 508, Bnigmann aaO., Pedersen KZ. 38, 354), wird durch die
Bed. und durch den Gutt.          — Med. asp. gegeniiber got. miMls^ und zwar ve-
lare; gegeniiber     dem Palatal you meyQi)           —
                                         widerlegt; daS beide Gruppen
etwa aus       „gro6'' durch versch. Gutturalformanten erweitert seien,
ware eine ganz luftige Konstruktion.

meiitli- „quirlei], drehend bewegen“; meth-.
   Ai. manihaii, mdihati, matJindti „quirlt, riihrt, schiittelt^*, manthd- m.
^Drehung, RuhrlofFel", av. mant- „ruhren^‘ (s. Bartholomae Airan. Wb. 1 135);
lat. (osk.) mamphur „ein Stuck der Drehbank“, nach Meyer-Liibke Phil.

Abhdlgn. Schweizensidler gewidmet 24 ff., EWb. 383 vielmehr manfar nach
Ausweis der heutigen Dialekte, die daneben auch ein echt lat. ^mandar
270                                       menth-   — mendh-

menth- „kauen; GebiS, Muad'^
  Gr. jLiddviat   *   yvd&oi Hes., /aaodojuai ,.kaue, bei6e“                         (juad- j^dojuai;   unan-
nehmbar Sommer IF. 1 1   266), /uaotd^a) „kaue'', judora^ „Mund“ und „ Atzung“,
                                ,



juaouxdco jjknirsche mit den Zahnen“, juooovvsiv juaodo'&at ^gadecog Hes.*



(wohl mit o aus a vor v, Ygl. ^juaovvetv vorausgesetzt von att. Maovvilag^
TiagajLiaovvTrjg „parasita“;        da6 neben *iuao{o)vvetv aus                             altes fjiOG{o)v-
V 81 V aus *iuov'&iv- gelegen sei, Ehrlich KZ, 41, 288 f., ist nicht wahrschein-
lich)    e-stufig fieoTaxa  Ti]v f^isjuaorjjuevrjv TQO(pr]v Hes i^menth-to -')
                            *
      ;


    lat. mando^ -ere,      mansum „kauen“ (mit lat. a parallel dem yon ^man-
dar^ osk. manfar zu menth- „quirlen“;        ein      ist kein Platz), Vanicek
                                                          fiir

LEWb.^ 207, Frohde BB. 7, 330;           meadal „Magenoffnung“ {^menth-lo~
                                                   nir.

Oder ^mnih-lo-^ Marstrander ZfcPh. 7. 363 f.).
  Ahd. mindil^ gamindel „Gebi6 am Zaum'S ags. midl ds., aisl.         aschwed.
mil ds. (Liden Uppsalastudier 79, doch unter Verb, mit lat. menhm j.Kinn",
cymr.         die wohl zu men- „bervorragen‘', Ehrlich KZ. 41, 287 f.; das
ags. und uord. Wort nicht nach Wood Men. 21, 40 zu fjitxog,                aisl*

minnask ,.kussen“ (wie oscidarl os; s. Koch Ark. f. nord. fil. 4, 170, Liden
                                              :



aaO.; nicht zu nhd. Minne                 —
                                 s. men- „denken‘^                           —
                                                           da dieses eine aus-   ,


schlieBlich deutsche Bed.-Entwicklung ist) schwundstufig got. mimps^ aisl.
                                                                 :




miidr^ ags. mud ahd. mund „Mund“ (s. Falk-Torp u. mund) Yerzeichnis
alterer Deutungen bei Liden aaO., Yf. LEWb.^ u. mentum),
   Gber dt. Made s. u. mat- „bei6endes Gewiirm^.
  Ehrlich aaO. halt menth- „kauen“ fiir ursprgl. dasselbe wie menth- „quirlen“
(„drehende Kaubewegung^)              ;
                                          fraglich.
```


## [2026-09-07T16:18:09.713Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '36035,36055p' LAT.txt; echo \"=== leaf ===\"; awk 'NR<=36041{n+=gsub(/\\f/,\"\")} END{print n}' LAT.txt",
 "description": "Ernout-Meillet mamphur"
}
```


### [2026-09-07T16:18:11.582Z] TOOL RESULT

```
3°de mamilla: manillStus, -nus (Plin. m. ficus); mamillaris; d'ou
mamillare n.: soutien-gorge.
mamphula, -ae f.: panis Syriaci genus quod, ut ait Verrius, in
clibano antequam percoquatur, decidit in carbones cineremque, F.136,11.
Un ex. Ae Lucilius, Sat.1350. Sans doute pour *mampula d'une racine
mpl "tomber" attest^e en hebreu et en aram^en.
mamphur?: - appellatur loro circumuolutum mediocris longitudinis
lignum rotundum, quod circumagunt fabri in operibus tornandis, P.F.
i 1 7 , 3 S« Terme technique, sans doute dialectal, auquel devait cor-
respondre une forme latine *mandar que supposent certains derives
romans. Hanphur lui-meme est peut-etre une corruption d'une forme
osque *mamphar, *manfar, cf.Ernout fI 4 m.dial., et M.L.5378; Jud, Arch.
f. d. Stud. d. neueren Spr. 134,403; et Thes. s.u.
Mana: r. nanis, mdnus.
manceps, -lpls m.: terme technique du droit; proprement "celui
qui prend en main" (quelque chose p'our en devenir l'acqudreur ou en
revendiquer la possession), cf. P.F.137,13, manceps dicitur qui quid
a populo emit conducitue, quia manu sublata significat se auctorem
emptionis esse. De la: mancipium, -t n.: mancipation, fait de prendre
en main (pour 1 'acquereur d'un objet, cf. Gaius Inst. 1, npsq., May-
Becker, Prdcis, p.ii7sqq.) d'ou le sens concret de "chose acquise
=== leaf ===
697
```


## [2026-09-07T16:18:23.792Z] TOOL CALL #42: Bash

```json
{
 "command": "pdftoppm -f 334 -l 334 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf \"$SCRATCH/pg334\" 2>&1; ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/ 2>/dev/null | head",
 "description": "Render page 334"
}
```


### [2026-09-07T16:18:25.517Z] TOOL RESULT

```
Could not write image to /pg334.png; exiting
total 15676
drwx------ 2 sfmqrb sfmqrb     4096 Sep  7 12:18 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  7 11:48 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     8635 Sep  7 12:07 318-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   101267 Sep  7 12:07 318-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb      449 Sep  7 12:17 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    14937 Sep  7 11:56 arrows.png
-rw-rw-r-- 1 sfmqrb sfmqrb    85949 Sep  7 11:57 bqt2002_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72256 Sep  7 11:58 bqt2002_f1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   161214 Sep  7 11:57 bqt2002_foot.png
```


## [2026-09-07T16:18:29.840Z] TOOL CALL #43: Bash

```json
{
 "command": "S=/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 334 -l 334 -r 220 -png -singlefile EtymologicalDictionary-persian-english.pdf \"$S/pg334\" && python3 -c \"\nfrom PIL import Image\nim=Image.open('$S/pg334.png'); print(im.size)\nw,h=im.size\nim.crop((0,0,w,h//2)).save('$S/pg334_top.png')\nim.crop((0,h//2,w,h)).save('$S/pg334_bot.png')\n\"",
 "description": "Render and split page 334"
}
```


### [2026-09-07T16:18:31.991Z] TOOL RESULT

```
(1870, 2420)
```


## [2026-09-07T16:18:34.677Z] TOOL CALL #44: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg334_top.png"
}
```


### [2026-09-07T16:18:34.706Z] TOOL RESULT

```

```


## [2026-09-07T16:18:42.805Z] TOOL CALL #45: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg334_bot.png"
}
```


### [2026-09-07T16:18:42.830Z] TOOL RESULT

```

```


## [2026-09-07T16:18:52.776Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FFD pdf 69 (p64) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==70' incoming/FFD/FFD_pages.txt | head -40",
 "description": "FFD p64"
}
```


## [2026-09-07T16:18:53.710Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v4 pdf 61 (p1978) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==62' incoming/BQT/BQT_v4_pages.txt | head -45",
 "description": "BQT p1978"
}
```


### [2026-09-07T16:18:54.281Z] TOOL RESULT

```
=== FFD pdf 69 (p64) ===
[pdf page 70]
ماده‌های ماضی و مضارع قارسی دری سس ۶۵
ی یف ۰
شیفت + ایرانی باستان 33۳۵-۲1۵*. برای 1۵ -> آراست. 0ه7537 صورت اصلی
آنه5۷* است. 0 پیش از 1 بدل به آ شده است. ريشهٌ 8۷۵10*به معنی «جنبیدن) است.
شیب < فارسی میانه 580 + ایرانی باستان 35۷/۵10-۵*. برای 2 > آرای.
«شیفته» صفت فاعلی گذشته از «شیفتن» است و در بیت زیر از گرشاسبنامةٌ اسدی
«(مشیب) به معنی («ناراحت مشو) به کار رفته است:
شکیب آور از درد و بر من مشیب که از مهر بسیار بهتر شکیب
فراموشیدن, فرموشیدن
فراموشید. فرموشید + فارسی میانه 1 ماد ماضی جعلی است. از ماده
مضارع ساخته شده است. در فارسی دری «فرامشت» بازماندة 11371۵31 فارسی میانه
است. 1۳30۵1 بازمانده 112-3-7108-1۵* ایرانی باستان است. برای 2 > آراست. 3و 5۵
هر دو پیشوند فعلی هستند. ريشةٌ کار" ظاهراً به معنی «فراموش‌کردن» است.
فراموش, فرموش < فارسی میانه 137۵5 < ایرانی باستان 172۵-3-۳۵5-۵*. برای 2
> آرای. 13۵05 صورت افزودةٌ ریشهٌ 05 است.
فرجامیدن
«فرجامید» مادهٌ ماضی جعلی است. از مادهٌ مضارع ساخته شده است.
فرجام + فارسی میانه 17[300 < ایرانی باستان 370-2[-17۵*. برای ۵ -> آرای. 370[/ظ
صورت بالاندهٌ ريشةٌ 8/[278 است. 8/1270 به معنی «حرکت کردن» است. صورت بالاندةٌ
آن با پیشوند فعلی ۵ به معنی «به پایان‌رساندن» است. در فارسی میانه ماد ماضی :
به صورت 178[31۲ آمده است» از ایرانی باستان 17[348*, با آمدن 31[ به‌جای
«آمدن) و «انجامیدن» هم از 8/۵7 آمده‌اند -> «آمدن) و «انجامیدن).
فرستادن
فرستاد + فارسی میانه 1۲68130 1138110 هر دو ماده ماضی جعلی هستند. از 11
```


### [2026-09-07T16:18:55.561Z] TOOL RESULT

```
=== BQT v4 pdf 61 (p1978) ===
[pdf page 62]
-۱۹۷۹- مراش
وبسی گویند هرمری پنجاه است چه صد رادومی مراد - پکر اول بر وزن فاد دم
و صد وینجاه را سه مر خوانند ۱ - و از جملةٌ | اسنگی باشد بسیار عجیب و از حرکت آقتاب
کلمات زایده هم هست که از برای حسن کلام | الوان مختلفه درو ظاهر میگردد یمنی هر سامت
آورند چنانکه « من او را گفتیم » و« من اورا | برتگی مینماید و آترا بلغفت سر‌بانی سروطالیس
دیدیم» پمنی با وگفتیم واورا دیدیم ۴ - وکاهی | میگویند بمنی سنگه پرنده زیرا که در هوا از
افادة معنی‌حصرهم میکند چنانکه کفته‌اند: مر | بغار لطیف متولد شود وباد آبرا ازجعتی بجهتی
او را رسد کیربا ومنی > یعنی دیگریرا نمیرسد | افکند . کوبند مادام که آفتاب فوق‌الارض باشد
و با تقدید ثانی در عربی بمعتی مرور کردن | هرکه‌آن سنکه را باخود دارد شیاطین تابع وی
وگذشتن برچیزی وازجاییباشد۴ - وبمعنی‌شمار | میشوند - وجنم اول, درعربی‌بمعنی خواسته شده
هم هست . باشد ۴ .

مراحل فشهن -کنایه از هر يك از هراد * « بفتح اول بروزن هزاره نوعی
کوا کب سبعهٌ سیاره باشد که قمر است و عطارد | از باد آورد و شکاعی باشد که بمربی ش وکةالبینا
و زهره وشمس ومریخ ومعتری وزحل -ومافر | خوانند و آن هم بوتة خاری است سفید که در
را نیز کوبند ؛ و مراحل نشینان مجموع هفت خاصیت کار بادآورد میکند .
کوکب - و مافران . همراش - یکی اول بر وزن خراش ,
‎٩‏ مر ما مرامن حاب الممر چون به ینجه رسد حاب » «مر» است.
« خاقانی شروانی ص ۹۷ .۰
مر بود پنجاه وچون‌آمد دو مر ابیات‌آن در صفا و محکمی شای دک ه کویم مر مراست ‏
جامی « جهانگیری » .
سراج‌آرد : «فوسی کوید که این حابی‌است که جولاهان در شمردن تارهای کربای کنند و گوبند
که این کریای چند « هر » است واین اقوی است چرا که محاسبان عقوداعداد مقر رکرده محتاج

باسطلاح دیگرنیستند مگراینکه مراد ازمحاسبان غیر از اهل علم حاب باشند . » (سراح‌اللفه)

بنقل فرهنگه نظام >. ۴ مر 87 اداتی ( 087110116 ) که پیش از مفعول درآید :
عرآن زخم گرزش که بارد چشید ؟ ( فردوسی ‎ )‏ مراو را رسد - ولیز ممکن است با مسندالیه

(با فاعل) استهمال شود : مراو هت پروردة کرد کاره دارمستتر . تتبغات اج ۱ص ۴۱۳۷ » ولیز :

بدل گفت اکر جنگجوی ی کنم به پیکار او سرخروبی کنم
بگربند هر دوده و هیهتم که بی‌سربه‌بینند خسته تنم
عنصری بلخی « لفت فری ص ۰۳۹۰

و رل:: مقدمة کتاب حاضر مس لد. ۴ - رك : منتهی‌الارب . اقرب‌الموارد .

۴ - اسم مفعول از آرادة . ۵ - 2/1076 ۰ 8 (فر) « دزی‌ج

۷ ی ۷۷ » مرار چم اول و تشدید ثالی » اسم عربی خاریست که در آخر بهار میرسد و در
مص «مر‌بر» و ۶ دردریه * نامند . برکش مانند بر که چفندر و مابل بسیاهی وملاسق زمین ودر
تابستان مانند درخت شعبه‌ها از يك بیخ میروید وگلش زرد و درآخرخاردار و شبیه بشکاعی‌میشود
و دران تخمی مانند تخم کافشه وبسیار تلخ وقوتش تا چهار سال بای است» و ساق او را پوست باز
کرده میخورند ومنیتش‌میان زراعات وجای دمناك (است) > «تحفةٌ حکیم موّمن» ورك: ابن‌البیطار.
```


## [2026-09-07T16:19:06.654Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'گماردن\\|گماشتن\\|گماشته' incoming/BQT/BQT_v3_pages.txt | head -10; echo \"--- shomordan ---\"; grep -n 'شمردن\\|شمار' incoming/BQT/BQT_v3_pages.txt | head -5",
 "description": "BQT v3 gomardan"
}
```


### [2026-09-07T16:19:06.723Z] TOOL RESULT

```
46492:‏» گماردن , کماریدی , گماختی - بت اول و فتح ماقبل آخر ( در هرسه ), پهلوی
--- shomordan ---
47:اول و دوم و طبع بخشی از مجلد سوم دربافت که شمارةٌ صفحه‌های مجلد اخیر از هزار متجاوز
110:‎-f‏ اضاقه ‎cae anes‏ بخش نضت . شمار۳2 ازسل له انتشارات « طرح دستور
125:باهتمام و صحیح دکتور ماکس مابرهوف . قاهره ۱۹4۰( عقار ) [ شماره‌هایی که پس ازآنها
424:۲ رك: ‎Sys‏ ۱۵ همن ماده . ۸ رك: شمارژ۱ همین ماده - ونیز «شاج»
2041:‏هرن چوپان و ‎Olt‏ را از ‎eh‏ ربشه میداند ولی هوبشمان آنرا جدا میشمارد « اسشق - هوبدمان
```


## [2026-09-07T16:19:11.112Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk -v L=46492 'NR<=L{n+=gsub(/\\f/,\"\")} END{print \"leaf(pdf-1)=\"n}' incoming/BQT/BQT_v3_pages.txt; awk 'BEGIN{RS=\"\\f\"} NR==631' incoming/BQT/BQT_v3_pages.txt | head -5; sed -n '46485,46510p' incoming/BQT/BQT_v3_pages.txt",
 "description": "BQT gomardan entry"
}
```


### [2026-09-07T16:19:12.392Z] TOOL RESULT

```
leaf(pdf-1)=630
[pdf page 631]
بیان پانزدهم

در ‎GE‏ فارسی با میم مشتمل بر هفت لغت و کنایت

HEV ‏لت فرس ص‎ «

‏رك : چست , ورگ : الجماهرص ۰۷۸ ۹۵ ۰ ۰۱۹6 ‎NAR‏

‏0 گم بنم اول ‎BUND SLT.‏ ؛ مفقود . غایب » تاپدید , آراره , سرکشته(بابودن
و شدن و کردن و گشتن ‎Sse‏ شود ).

‏» گماردن , کماریدی , گماختی - بت اول و فتح ماقبل آخر ( در هرسه ), پهلوی
0 ( از : کمار ‎gt ot (go)‏ ( پسوند مصدری ) راد : تیب رکه ص ‎۸٩‏ ؛ پازدد
‎gumaral ysl. gumardan‏ ( وا گذار کردن ‎(os Spd‏ » ارمنی ع ‎gumar_el‏
‏( جمع کردن - فرستادن » نیم کردن ) « هوبشمان ‎٩۳۱‏ » و رل : استق ابضاً ؛ فصب کردن-
فرستادن - اجازه ورخصت دادن - سفارش کردن ۰

‎ga - ole? ©‏ اول, اوستا - ‎(ouS) ovimanah‏ فس‌اوستایی: - ۷18۵8062
پهلوی ‎SUMAN‏ ء کردی ¢ افانی ع 80۳080 , بلوچی ع 800۷0 « اسشق ‎٩۳۷‏ ».پارسی
باستان - 0۷180808 «هوبشمان ۲ ؛ ‎a‏ احتمال - شك , شبهه - رای » الدیشه-

‏فر » تصور .
» گمالیدی - نم اول و فتح ششم ‎fe SOLS:‏ اندیشیدن . رك : کمان .
کماند که ازتیغ او در جهان بارزید ‎GS‏ کهان و مهان .

‏فردوسی طوسی « رشیدی *.
( برهای فاطع ‎Cree‏
[pdf page 632]
۳۵ -
```


## [2026-09-07T16:19:29.428Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN mourn ===\"; grep -n 'mourn,  intr\\|^mourn\\|mourn, ' KLN_1966.txt | head -5; echo; grep -n 'mourn' KLN_1966.txt | head -5; echo \"=== page of mouth/mustache ===\"; grep -n '^[0-9]\\{3,4\\}$' KLN_1966.txt | awk -F: '$1>24400 && $1<24800'|head -20",
 "description": "Klein mourn"
}
```


### [2026-09-07T16:19:30.785Z] TOOL RESULT

```
=== KLN mourn ===
12251:drear,  adj.  (poet.)  —  Shortened  fr.  dreary, dreary,  adj.  —  ME.  dreri,  dreori,  fr.  OE.  dreorig, ‘bloodstained,  gory;  sad,  sorrowful’,  fr.  dreor , ‘gore,  blood’ ;  rel.  to  OHG.  trurac,  MHG.  trurec, G.  traurig,  ‘sad,  sorrowful’,  OHG.  truren ,  ‘to lower  the  eyes;  to  mourn,  lament;  MHG.  tru¬ ren,  G.  trauern,  ‘to  mourn,  lament’,  and  to  OE. dreosan,  ‘to  fall,  sink,  become  slow,  become  in¬ active’,  OS.  driosan,  Goth,  driusan,  ‘to  fall’, MHG.  tror,  ‘dew,  rain’.  Cp.  drowse,  drizzle. Derivatives:  drear-i-ly,  adv.,  drear-i-ness,  n. dredge,  n.,  a  dragnet.  —  From  the  stem  of  OE. dragan,  ‘to  draw’.  See  draw.
22277:lugubriosity,  n.  —  See  lugubrious  and  -ity. lugubrious,  adj.,  mournful.  —  Formed  with  suff. -ous  fr.  L.  lugubris,  ‘pertaining  to  mourning, mournful,  painful',  fr.  tugere,  ‘to  mourn,  lament, bewail';  which  is  cogn.  with  OI.  rujdti,  ‘breaks, torments’,  rugnah,  ‘broken",  rSgah,  ‘frailty,  dis¬ ease’,  Avestic  uruxti-.  ‘a  breaking,  tearing’,  Gk. XeuYtxXeo;,  Xuypo;,  'mournful,  sad,  dismal’, Xovuoc  (Hesychius),  ‘a  loud  cry’,  Lith.  hiiti,  ’to break’  (intr.),  lauzyti,  ‘to  break'  (tr.),  Lett,  lauzit, ‘to  break  the  heart’,  Lith.  luzis,  Iduzis,  ‘breach’. All  these  words  derive  fr.  I.-E.  base  *leug-  (Bal¬ tic),  *leug-,  ‘to  break;  to  cause  pain’;  see  lock, ‘contrivance  for  closing  doors’.  For  the  sense development  of  this  base  cp.  OI.  lumpati.
23238:milho,  ‘millet’,  fr.  L.  milium,  ‘millet’.  See  millet. mean,  tr.  v.,  to  have  in  mind.  —  ME.  menen,  fr. OE.  mxnan,  ‘to  mean,  signify,  intend;  to  speak of;  to  complain,  mourn,  moan’,  rel.  to  OS. me, nan,  ‘to  have  in  mind,  intend,  signify’, OFris,  mena,  MDu.  menen,  Du.  menen ,  OHG. meinan,  meinen,  MHG.,  G.  meinen,  to  think, suppose,  be  of  opinion',  fr.  I.-E.  base  *mam-, *mein-,  ‘to  be  of  opinion,  think  ,  whence  also OSlav.  mdniti,  ‘to  think,  have  an  opinion’,  OIr. mian,  ‘wish,  desire’,  Ir.  mian,  ‘intention’,  W. mwyn,  ‘enjoyment’.  Cp.  moan.
23432:Derivative:  memoriz-ation,  n. memory,  n.  —  ME.  memorie,  fr.  OF.  memorie  (F. memoire),  fr.  L.  memoria,  ‘memor}'’,  fr.  memor, ‘mindful’,  which  stands  for  *me-mor  and  de¬ rives  fr.  I.-E.  *mer-{s)mer-,  reduplication  of base  *(s)mer-,  ‘to  care  for,  be  anxious  about, think,  consider,  remember’.  From  the  redupli¬ cated  base  derive  also  Avestic  mimara-,  ‘mind¬ ful’,  OE.  gemimor,  ‘known’,  mamrian,  ‘to  plot, design’,  Du.  mijmeren,  ‘to  ponder’.  Cp. — with full  reduplication  of  base  *mer- — Gk.  pcppEpoc, ‘causing  anxiety,  mischievous,  baneful’,  pip- prjpa  (poet.),  ‘care,  trouble’,  peppatpEtv,  pep- pTjpi^eiv,  ‘to  be  anxious,  to  ponder’.  Arm.  mor- mok ‘  (for  *mermero-  or  * mormoro -),  ‘regret, grief’.  The  simple  base  *{s)mer-  appears  in  OI. smarati,  Avestic  maraiti,  ‘remembers’,  Gk.  pipi- llvx,  ‘care,  thought’,  pEpipviv,  ‘to  care  for,  be anxious’,  Serbo-Croat  mariti,  ‘to  care  for’, Goth,  maurnan,  OE.  murnan,  ‘to  be  anxious for',  W.  marth,  ‘sadness,  anxiety',  and  possibly also  in  L.  mora,  ‘hesitation,  delay’,  OIr.  maraim, ‘I  remain’.  Cp.  memoir,  commemorate,  remem¬ ber.  Cp.  also  martyr,  mourn,  smriti.  Cp.  also moratory.
24109:Moabite,  n.  —  Late  L.  Moabites,  fr.  Gk.  Mua- PiT7)i;,  ‘inhabitant  of  Moab’,  fr.  MtoafS,  ‘Moab, land  of  Moab’,  fr.  Heb.  Md’abh,  which  is  perh. a  derivative  of  Heb.  abh,  ‘father’;  see  Gen. 19:37.  See  abbot  and  subst.  suff.  -ite. Derivatives:  Moabite,  adj.,  Moabit-ish,  adj. moan,  n.  —  ME.  mone,  mane,  from  the  stem  of OE.  msenan,  ‘to  complain,  mourn,  moan’.  See mean,  ‘to  have  in  mind’.

8329:comely,  adj.  —  ME.  cumelich,  cumlich,  comeliche, comlich,  fr.  OE.  cymlie,  formed  with  suff.  -lie (see  like,  adj.),  fr.  cyme,  ‘fine,  beautiful,  splen¬ did’,  orig.  ‘frail,  delicate,  tender’,  which  is  rel. to  ME.  kime,  ‘weak,  delicate’,  OHG.  chumo, kiimd,  MHG.  kume,  ‘with  difficulty’,  OHG. chumig,  kumig,  ‘weak,  delicate’,  G.  kaum, ‘hardly,  scarcely’.  The  original  meaning  of  ME. kime  and  OHG.  chumig  was  ‘lamentable,  piti¬ able’;  cp.  OHG.  chuma,  ‘sorrow’,  OHG.  chu- mon,  ‘to  mourn’,  OS.  kumian,  ‘to  lament,  de¬ plore’.  All  these  words  are  derivatives  of  the I.-E.  imitative  base  *gou-,  *gow-,  ‘to  shout,  cry’ whence  also  OE.  ciegan  (for  orig.  *kaujan ),  ‘to call’,  cyta,  ‘kite’,  Ol.gavate,  ‘sounds,  resounds’, Gk.  yoav,  ‘to  wail,  groan,  weep’,  MLG.  kitten, ‘to  chatter,  babble,  prate’,  Lith.  gaudziii,  gausti, ‘to  howl’,  gaudas,  ‘lamentation’,  OSIav.  govoriti, ‘to  make  a  noise’,  Russ,  govorit',  Serb,  and Croat  ian^ovoWh,  Czech  hovoriti,  Slovak  hovorit’, ‘to  speak’,  OIr.  guth,  ‘voice’.  Cp.  kite.  The  word comely  was  influenced  in  meaning  by  an  as¬ sociation  with  come.
11995:dole,  n.,  grief  ( archaic  and  poet.)  —  ME.,  fr.  OF. dol,  doel,  deol  (F.  deuil),  ‘sorrow,  grief,  mourn¬ ing’,  fr.  Late  L.  dolus,  ‘sorrow  (whence  also  It. duolo,  OProven?.  dol,  ‘sorrow,  grief’,  Sp.  duelo, ‘sorrow,  grief;  mourning’),  fr.  L.  doiere,  ‘to suffer  pain,  grieve,  be  afflicted,  deplore,  lament’, fr.  I.-E.  base  *del-,  *dol-,  ‘to  split,  cut,  carve’, whence  also  OI.  dalati,  splits,  bursts’,  dalayati, causes  to  burst’,  daiam,  ‘part,  piece’,  Arm.  tal, impression,  sign’,  Gk.  SaiSaXo?,  ‘cunningly made’,  SatSaXXetv,  ‘to  work  cunningly  or  skill¬ fully’,  L.  dolium,  ‘a  very  large  jar,  vessel’,  dolare, ‘to  hew  with  an  ax',  Russ,  dolja,  ‘part’,  Lith.  dalis, ‘part,  destiny’,  Lith.  daliju,  dalyti,  Lett,  dalit, ‘to  divide’,  ON.  tal,  OE.  talu,  ‘number’  (prop. ‘incision  in  the  tally’),  OIr.  delb,  ‘figure,  form’, Toch.  A  tab,  B  tallawo ,  ‘miserable,  wretched’. The  original  meaning  of  L.  doiere  was  ‘to  be torn’.  For  sense  development  cp.  E.  heart¬ rending.  Cp.  condole,  dolabriform,  dole,  ‘guile’.
12023:dolor,  dolour,  n.,  grief,  mourning.  —  OF.  dolor, dolur ,  dolour  (F.  douleur ),  fr,  L.  dolorem,  acc.  of dolor,  ‘pain,  distress,  grief,  affliction’,  fr.  doiere, ‘to  suffer  pain’.  See  dole,  ‘grief’, doloroso,  adj.,  sorrowful  ( musical  direction).  — It.,  fr.  L.  dolbrosus.  See  dolorous.
12251:drear,  adj.  (poet.)  —  Shortened  fr.  dreary, dreary,  adj.  —  ME.  dreri,  dreori,  fr.  OE.  dreorig, ‘bloodstained,  gory;  sad,  sorrowful’,  fr.  dreor , ‘gore,  blood’ ;  rel.  to  OHG.  trurac,  MHG.  trurec, G.  traurig,  ‘sad,  sorrowful’,  OHG.  truren ,  ‘to lower  the  eyes;  to  mourn,  lament;  MHG.  tru¬ ren,  G.  trauern,  ‘to  mourn,  lament’,  and  to  OE. dreosan,  ‘to  fall,  sink,  become  slow,  become  in¬ active’,  OS.  driosan,  Goth,  driusan,  ‘to  fall’, MHG.  tror,  ‘dew,  rain’.  Cp.  drowse,  drizzle. Derivatives:  drear-i-ly,  adv.,  drear-i-ness,  n. dredge,  n.,  a  dragnet.  —  From  the  stem  of  OE. dragan,  ‘to  draw’.  See  draw.
12802:elegancy,  n.  —  See  prec.  word  and  -cy. elegant,  adj.  —  F.  elegant,  fr.  L.  elegantem,  acc. of  elegans,  ‘choice,  tasteful,  elegant’,  a  collateral form  of  ehgens,  pres.  part,  of  eligere,  ‘to  choose, pick  out’.  See  elect,  v.,  and  -ant. elegiac,  adj.,  1)  pertaining  to  the  elegiac  meter; 2)  used  for  elegies ;  3)  mournful.  —  Late  L.  ele- giacus,  fr.  Gk.  IXe ysiotxop,  ‘elegiac’,  fr.  IXeyeix. See  elegy.
=== page of mouth/mustache ===
24419:1004
24420:1005
24467:1006
24468:1007
24495:1008
24496:1009
24538:1010
24566:1011
24595:1012
24659:1015
24689:1016
24690:1017
24786:1021
```


## [2026-09-07T16:19:36.625Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>24500 && NR<24560' KLN_1966.txt | grep -n 'mourn' ; echo \"---\"; sed -n '24528,24534p' KLN_1966.txt",
 "description": "Klein mourn headword"
}
```


### [2026-09-07T16:19:37.864Z] TOOL RESULT

```
33:mourn,  intr.  and  tr.  v.  —  ME.  mournen ,  monten, fr.  OE.  murnan,  ‘to  care  for,  be  anxious  about ; to  lament  over’,  rel.  to  OS.  mornian,  OHG. mornen,  Goth,  matirnan,  ‘to  mourn’,  ON.  morna ‘to  pine  away’,  fr.  I.-E.  base  *(s)mer-,  ‘to  care for,  be  anxious  about,  think,  consider,  remem¬ ber’,  whence — with  reduplication  of  the  base — L.  memor,  ‘mindful’,  memoria,  ‘memory’.  See memory  and  cp.  words  there  referred  to. Derivatives:  mourn-er,  n.,  mourn-ful,  adj., mourn-ful-ly,  adv.,  mourn-ful-ness,  n.,  mourn¬ ing,  n.
---
Derivatives:  mountain-eer,  n.,  mountain-eer-ing, n.,  mountainous  (q.v.),  mountain-y,  adj. mountainous,  adj.  —  F.  montagneux  (fem.  mon- tagneuse),  fr.  VL.  *montaneosus,  fr.  L.  montanus.
See  mountain  and  -ous.
Derivatives:  mountain-ous-ly,  adv.,  mountain- ous-ness,  n.
mountebank,  n.,  a  quack,  charlatan.  —  It.  mon- tambanco,  contraction  of  monta-in-banco,  lit.
‘mount  on  bench’,  with  reference  to  the  bench from  which  quacks  and  buffoons  used  to  address the  crowd  gathered  around  them.  It.  monta  is theimper.  of  montare,  ‘to  mount’,  fr.  VL.  *  mon- tare;  see  mount,  v.  For  the  etymology  of  It. banco,  ‘bench’,  see  banco.  For  sense  develop¬ ment  cp.  saltimbanco.
mourn,  intr.  and  tr.  v.  —  ME.  mournen ,  monten, fr.  OE.  murnan,  ‘to  care  for,  be  anxious  about ; to  lament  over’,  rel.  to  OS.  mornian,  OHG. mornen,  Goth,  matirnan,  ‘to  mourn’,  ON.  morna ‘to  pine  away’,  fr.  I.-E.  base  *(s)mer-,  ‘to  care for,  be  anxious  about,  think,  consider,  remem¬ ber’,  whence — with  reduplication  of  the  base — L.  memor,  ‘mindful’,  memoria,  ‘memory’.  See memory  and  cp.  words  there  referred  to. Derivatives:  mourn-er,  n.,  mourn-ful,  adj., mourn-ful-ly,  adv.,  mourn-ful-ness,  n.,  mourn¬ ing,  n.
mouse,  n.  —  ME.  mous,  fr.  OE.  mils,  rel.  to  OS., ON.,  OFris.,  MLG.,  MDu.,  Dan.,  Swed.  mus, Du.  muis,  ‘mouse’,  OHG.,  MHG.  mus,  G. Maus,  ‘mouse;  muscle’,  and  cogn.  with  OI. muf-,  ‘mouse,  rat’,  muskdh,  ‘scrotum,  testicle’, lit.  ‘a  little  mouse',  OPers.  mush,  ‘mouse’,  Arm. mukn  (gen.  mkan),  Gk.  p<3?  (gen.  pooq), ‘mouse;  muscle',  L.  mils  (gen.  muris ),  Alb.  mi, Lith.  muse,  OPrus.  muso,  ‘mouse’,  OSlav.  my  si, ‘mouse’,  mysica,  ‘arm’.  Cp.  dormouse,  flitter- mouse.  Cp.  also  murex,  Muridae,  murine,  Mus, muscatel,  muscle,  muscular,  musk,  musteline, marmot.  Cp.  also  Mya,  myelo-,  myo-,  amyous, perimysium.
```


## [2026-09-07T16:19:47.521Z] TOOL CALL #52: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-07T16:19:47.529Z] TOOL RESULT

```


```


## [2026-09-07T16:19:52.121Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mend%CA%B0-",
 "prompt": "Give the full reconstruction, meaning, and the list of descendants/derived terms for this PIE root, especially Greek mastax/mystax/mastichē, Latin mandere, and any Germanic 'mouth' forms."
}
```


## [2026-09-07T16:19:53.503Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/mun%C3%BEaz",
 "prompt": "What PIE root does Proto-Germanic *munþaz 'mouth' come from? Quote the etymology section and any cognates (Latin mentum, Welsh mant) and note any dispute about *menth- 'to chew' vs *ment- 'to chew/project'."
}
```


### [2026-09-07T16:19:53.543Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T16:19:58.724Z] TOOL RESULT

```
# Proto-Germanic *munþaz Etymology

The word derives from Proto-Indo-European **\*mn̥-tó-s** ("mouth, jaw"), combining the root **\*men-** ("chin") with the suffix **\*-tós**.

## Cognates

The text lists several related words:
- Latin *mentum* ("chin")
- Welsh *mant* ("mandible, gums")
- Hittite *mēni-* ("face, cheek")

## Disputed Etymology

There's speculation about a possible connection to PIE **\*stemn-** ("mouth, muzzle"), which would relate to Ancient Greek *stóma* ("mouth"). The source notes "some details are disputed" regarding connections to Ancient Greek *masáomai* ("to chew, bite") and Latin *mandō* ("to chew"), suggesting uncertainty about these semantic parallels.
```


## [2026-09-07T16:20:06.459Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%BC%CE%AC%CF%83%CF%84%CE%B1%CE%BE",
 "prompt": "Give the etymology of Ancient Greek μάσταξ, the related verb μασάομαι, the Doric μύσταξ, and μαστίχη. What PIE root are they assigned to?"
}
```


## [2026-09-07T16:20:07.129Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/mandrel",
 "prompt": "Give the full etymology entry for mandrel (and mandril), including French mandrin and any Latin mamphur connection."
}
```


### [2026-09-07T16:20:12.094Z] TOOL RESULT

```
# Etymology of Mandrel

Based on the provided content, here's the etymology entry:

**mandrel (n.)** - The word appears from the 1510s onward, initially referring to a "miner's pick." The Online Etymology Dictionary notes its "origin [is] unknown," though it "perhaps borrowed from French _mandrin_, itself of unknown origin."

From the 17th century onward, the term expanded to describe "a bar or spindle, used chiefly to hold articles in place, on a lathe or a circular saw."

**Important limitation:** The webpage content provided does not include information about a "mandril" variant or any connection to Latin "mamphur." The dictionary entry focuses only on the uncertain French borrowing from _mandrin_ and acknowledges the fundamental obscurity of the word's ultimate origins.
```


### [2026-09-07T16:20:13.029Z] TOOL RESULT

```
# Etymology of μάσταξ and Related Terms

Based on the Wiktionary article provided, here's what can be determined:

## Etymology

According to the source, μάσταξ is "related to μασάομαι (masáomai, 'to chew') and μαστάζω (mastázō, 'to chew'), both terms [Beekes] suspects to be of Pre-Greek origin."

## PIE Root Assignment

**The article does not assign these words to any Proto-Indo-European root.** Instead, it explicitly identifies them as having a **Pre-Greek substrate origin**, meaning they likely predate the arrival of Indo-European speakers in Greece and may represent an ancient Mediterranean language layer.

## Related Terms

The source lists μαστίχη (mastíkhē) as a related term, but provides no etymological explanation for it or information about the Doric variant μύσταξ beyond what appears in the main entry.

The article's approach reflects scholarly uncertainty about the ultimate origin of this word family, attributing it to substrate languages rather than reconstructed Indo-European ancestry.
```


## [2026-09-07T16:20:22.669Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/mando",
 "prompt": "For the Latin verb mandō 'to chew', give the etymology section verbatim — which PIE root, what de Vaan says, and any note that it is disputed or of unclear origin."
}
```


## [2026-09-07T16:20:23.253Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/mustache",
 "prompt": "Give the full etymology of mustache, including the Italian, Medieval Greek and Doric Greek forms and dates."
}
```


### [2026-09-07T16:20:27.718Z] TOOL RESULT

```
# Etymology of Latin mandō (to chew)

The etymology is uncertain but probably derives from Proto-Italic *mandnō, ultimately from Proto-Indo-European *meth₂-.

**De Vaan's interpretation:** He suggests the PIE root *menth₂- meaning "to stir, whirl" → "chew," citing cognates like Sanskrit mánthati ("to whirl, rub, shake").

**Alternative view:** Other scholars (WH, IEW, LIV, Meiser) refer it to PIE *menth₂- meaning "tear away," with different cognate evidence.

**Status:** The documentation explicitly notes: "The semantic development is disputed," indicating scholarly disagreement about which sense best explains the Latin verb's meaning.
```


### [2026-09-07T16:20:29.272Z] TOOL RESULT

```
# Etymology of Mustache

The word mustache traces back through multiple Romance and Greek languages:

**English (1580s):** "the hair that grows upon the upper lip of men"

**French (15c.):** *moustache*

**Italian (origin point):** *mostaccio*

**Medieval Greek:** *moustakion* (a diminutive form)

**Doric Greek:** *mystax* (genitive *mystakos*), meaning "upper lip, mustache"

An earlier English borrowing occurred in the 1550s as *mostacchi*, derived from Italian or Spanish *mostacho*. The Greek root *mystax* connects to *mastax* meaning "jaws, mouth," literally "that with which one chews," possibly from an Indo-European root *\*mendh-* meaning "to chew." However, scholars suggest the entire Greek word group may have Pre-Greek origins.

The plural form *mustachios* persisted in English usage, reflecting the historical treatment of mustaches as paired features on either side of the upper lip.
```


## [2026-09-07T16:20:38.187Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%B5%D8%B7%D9%83%D9%89",
 "prompt": "Give the Arabic entry مصطكى / مصطكاء: etymology (from Ancient Greek?), meaning (mastic resin), and any Persian entry مصطکی on this page."
}
```


## [2026-09-07T16:20:39.664Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/-%D9%85%D9%86%D8%AF",
 "prompt": "Give the Persian suffix -مند (-mand) entry: etymology (Middle Persian, Old Iranian/Avestan forms), meaning, and examples. Quote the etymology exactly."
}
```


### [2026-09-07T16:20:41.213Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T16:20:44.553Z] TOOL RESULT

```
# مصطكى (Mastic) - Dictionary Entry Summary

**Etymology:** The word مصطكى derives from Ancient Greek μαστίχη (mastíkhē), borrowed through Aramaic מצטכי (mūṣṭəḵē). The entry states: "Borrowed from Aramaic..., borrowed from Ancient Greek."

**Meaning:** This Arabic noun refers to "mastic, the gum-resin of Pistacia lentiscus." It's a feminine noun pronounced /musˤ.tˤa.kaː/.

**Persian Entry:** The page lists a Persian descendant: مصطکی (mastaki), indicating the term migrated into Persian from Arabic, though no separate Persian dictionary entry content is provided on this page.

**Note:** The entry also documents alternative Arabic forms (مُصْطَكَاء, مُصْطَكِيّ) and dialectal variants (مِسْتَكَة, مَسْتِيك), along with related terms in Egyptian Arabic, Turkish, Spanish, and Portuguese.
```


## [2026-09-07T16:20:50.694Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D9%86%D8%AF",
 "prompt": "Find the Persian suffix -مند (mand) section: give its etymology (Middle Persian -ōmand, Proto-Iranian, Avestan -mant-/-vant-), meaning and examples. Quote exactly."
}
```


## [2026-09-07T16:20:52.192Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D9%85%D8%A7%D8%B1",
 "prompt": "Give the Persian entry آمار (āmār): etymology (Middle Persian, Avestan forms) and meaning. Quote the etymology exactly."
}
```


### [2026-09-07T16:20:53.983Z] TOOL RESULT

```
I cannot provide the Persian suffix section as requested. The webpage content shown is from the **Urdu** entry for مند, not the Persian entry. While the page mentions that Persian and Malagasy versions exist via links, the actual Persian section content is not included in the provided material.

To find the Persian suffix -مند with its full etymology, meaning, and examples, you would need to visit the Persian Wiktionary directly at the link indicated: https://fa.wiktionary.org/wiki/مند
```


### [2026-09-07T16:20:56.813Z] TOOL RESULT

```
# Persian Entry: آمار (āmār)

## Etymology
The word is inherited from Middle Persian āmār meaning "reckoning, consideration," which derives from Old Persian. According to the entry: "Inherited from Middle Persian [Book Pahlavi needed] (ʾmʾl /⁠āmār⁠/, "reckoning, consideration"), from Old Persian."

## Meaning
**آمار** (āmār) has two definitions:

1. **Statistics** (current usage)
2. **Calculation, enumeration** (obsolete, original sense)

The entry notes a derived term: **آمارگر** (âmârgar), meaning "statistician."
```


## [2026-09-07T16:21:05.688Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AVG vant/mant suffix ===\"; grep -n -i 'vaṇt\\|vant-\\|mant-\\|-mant\\b' AVG.txt | head -25",
 "description": "Jackson Avesta Grammar suffix"
}
```


### [2026-09-07T16:21:05.738Z] TOOL RESULT

```
=== AVG vant/mant suffix ===
564:be  explained  GAv.  drygvant-  'wicked'  (=  *drugva*it-  to  Av. druj~) ;  GAv.  bazvant-  'advantageous'  (=  *buzva?it-  to  Skt. Vbhuj-}\  GAv.  u$9uru-  'zeal'  (?)  see  Ys.  34.7,  cf.  usuruye Ys.  32.16;  GAv.  Aufj'tt-  'well-being' ;  GAv.  ina^ti-  Ys.  30.1 1 ; GAv.  dsk^ti-  Ys.  44.17.
721:Av.  zaranim  'golden'  (ace.)  =  Skt.  hiran-ya-m  ;  Av. u%$tn  'they  increased'  (for  *ufy<;-ya.-ri)\  Av.  mainimna 'thinking'  (fern.)  =  Skt.  mdn-ya-mdna;  Av.  p&pimnd 'possessing'  =  Skt.  pdt-ya-mdnas  ;  Av.  iripiqti  'they die'  (for  irip-ya-titt).  —  GAv.  asruzdiim  'ye  were  heard of  Ys.  32.3  =  Skt.  dsrd$h-va-m;  Av.  daeum  'demon' =  Skt.  de-vd-m;  A.v.Jri$um  'third'  (for  pri$-va-ni)  ;  Av. mourum  'Merv'  (for  *mar-va-m)\  —  Av.  tamawhuiitam 'dark'  =  Skt.  tdmasvant-  ;  Av.  Jvar'navhufitsm  'glorious' beside  hrar'nawuhaiit0  for  hrar'navh-va-titam.
1028:(-vh-t  -vhv-) — GYAv.  vavuhim  'good'  (fern.),  Pers.  MSS.  vavhim  = Skt. vdsvim;  YAv.  pafdyavuha  'set  foot,  abide'  =  Skt.  pddyasva;  YAv. hunavuha  'press  haoma-juice",  cf.  Skt.  sunufvd; — YAv.  aojavuhant-, GAv.  aojorighvatit-,  aojovAvatft-  'strong'  =  Skt.  ojasvant-.—YA.v. vavhvqm  'of  good  things',  beside  vohunqm;  YAv.  kar'navhvanta 'glorious',  cf.  Yt.  15.56,  beside  Jvar'navuharittm  ;  YAv.  var'cavhutitim 'brilliant'  Yt.  X2.I  =  Skt.  *varcasvantam.
1774:§  290.  •  As  to  stem-gradation,  (i)  the  adjective  ant- stems  generally  show  at  in  the  weak  (=  Skt.  weak)  cases, (2)  the  participial  (thematic)  #;^-stems  show  ant  in  almost all  forms.  (3)  The  mant-,  z/rt^-stems  agree  with  the  ad- jective stems  in  showing  at  in  the  weak  cases.  A  number of  interchanges,  however,  between  all  three  occur — these  interchanges  are  found  chiefly  in  YAv.  e.  g.  dat.  du. ber'zanbya  (from  str.  st.)  Ys.  i.li;  3.13.
2190:amavant-  'strong',  amavastara-?  amavastama-
2638:§  435.  Here  may  be  enumerated  as  connected  with the  personal  pronoun,  the  following  possessive  (and  re- flexive) forms:  —  Av.  ma-  'meus',  pwa-  'tuus',  hva-,  ha-, hava-  (reflexive)  'suus',  ahmaka-  'our',  yu$mdka-,  tysmdka- 'your'.  —  mavant-  'like  me',  pwdva^t-  'like  thee',  yii$mavaiit-, t-  'like  you'.  —  Ivaepaipya-  'own'.
2655:Note  2.  The  possessives  ahmaka-  'our',  JnvSvant-  'like  thee'  etc. follow  the  noun-inflection.
4638:Av.  a*rvanj-  adj.  and   noun  'swift,    courser*  =  SkL  drvant-;
4640:vivaahvan.t-    m.    nomen    propr.  =  Skt.   vivdsvant-;   Av.  stfr'frwan.t-
4756:24.  Av.  -matit  =  Skt.  -mant  (Whitney,  §   1235). §  851.    The  secondary  suffix  -matit,  like  -vant  below, is  used  in  making  a  number  of  possessive  adjectives  from noun-stems.    The  noun-stems  with  which  it  is  used,  as  in Skt.,  are  chiefly  «-stems.     Examples  are:
4757:Av.  Jiratumatit-  'having  wisdom'  =  Skt.  krdlumant- ; Av.  gaomatit-  'having  milk,  flesh'  =  Skt.  gomant-; Av.  madumatit-  'rich  in  sweets'  =  Skt.  mddhumant- ; — Av.  ar'pamatit-  'right,  true  to  fact'  (from  tf-stem) ; — Av.  afra$lmaiit-  'not  progressing'  (fr.  z'-stem).
4777:From  tf-stem:  Av.  amavatit-  adj.  'strong'  =  Skt. dmavant-;  Av.  pupravan_t-  'having  a  son'  =  Skt.  /«• travdnt-;  Av.  haomavan^t-  'having  haoma'  =  Skt.  soma- vant~.  —  From  /-stem:  Kv .  fraza^tivarit-  'having  off- spring' ;  Av.  ndirivarit-  'having  a  wife' ;  Av.  raevant- 'radiant'  =  Skt.  revdnt-.  —  From  consonant  stem:  Av. aojavhvan.t-}  aojdvhvatit-  'mighty'  Ys.  57.11,  Ys.  31.4 =  Skt.  djasvant-;  Av.  tomavhvant-  'dark'  =  Skt.  td- masvant-;  Av.  paemavant-  'with  milk'  (paeman-);  Av. ar$navan.t-  'possessing  a  stallion'
4780:Note  2.  A  few  words,  chiefly  pronominal  derivatives  in  -vatjt,  have the  meaning  'like  to',  'resembling',  cf.  Whitney,  Skt.  Grain.  §  1233  f. Examples  are:  Av.  mavat^t-  'like  me' =  Skt.  mdvant-;  Av.  pw&vaiit-  'like thee,  your  Grace'  =  Skt.  tv&vant-.  So  also  Av.  visa'tivant-  'twenty-fold' ; Av.  satavaijl-  'hundred-fold',  §  376.
5441:p-wavant-  435-
```


## [2026-09-07T16:21:07.328Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D8%AC%D9%85%D9%86%D8%AF",
 "prompt": "Give the Persian entry ارجمند (arjmand): etymology, and how the suffix -mand is explained (Middle Persian -ōmand, Avestan -mant/-vant)."
}
```


### [2026-09-07T16:21:12.354Z] TOOL RESULT

```
# Persian Entry: ارجمند (arjmand)

## Etymology

According to the Wiktionary entry, this term is "Related to _ارزیدن_ (arzidan, 'to cost, be of value'). Ultimately from Proto-Indo-European _*h₂elgʷʰ-_ ('to cost, have value')."

## Suffix -mand Explanation

The provided Wiktionary content does **not** explain the suffix -mand or its historical development through Middle Persian -ōmand or Avestan -mant/-vant forms. The entry focuses on the root etymology tracing back to Proto-Indo-European but does not analyze the morphological composition or suffixal components of the word itself.

To obtain information about the -mand suffix derivation from Middle Persian and Avestan, you would need to consult additional linguistic sources beyond what appears on this particular Wiktionary page.
```


## [2026-09-07T16:21:23.410Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%BC%CE%AC%CF%81%CF%84%CF%85%CF%82",
 "prompt": "Give the etymology of Ancient Greek μάρτυς 'witness': which PIE root, does it come from *(s)mer- 'to remember'? What does Beekes say? Quote."
}
```


## [2026-09-07T16:21:24.828Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/smer-",
 "prompt": "Give the reconstruction, meaning and descendants of this PIE root (Sanskrit smarati, Avestan mar-, Latin memor, Germanic murnan, Greek)."
}
```


### [2026-09-07T16:21:26.394Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T16:21:27.041Z] TOOL RESULT

```
# Etymology of Ancient Greek μάρτυς

## PIE Root Origin

The word typically derives from Proto-Indo-European ***(s)mer-*** meaning "to fall into thinking, remember, care for." However, this attribution is disputed.

## Beekes's Position

Beekes acknowledges the standard PIE derivation but finds it unconvincing. He instead proposes: "derives it from Pre-Greek based on the ending of the word." His alternative theory emphasizes pre-Greek substrate influence rather than Indo-European ancestry.
```


## [2026-09-07T16:21:32.916Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'smer-\\|smer\\b' AHD_watkins1985.txt | head -10",
 "description": "Watkins smer root"
}
```


### [2026-09-07T16:21:32.963Z] TOOL RESULT

```
955:5. Suffixed form *lag-no- in Greek lagnos, lustful, lasciv- ious (> lagneia, lust, lasciviousness): ALGOLAGNIA. 6. Variant form */ég- in Greek légein, to leave off: CATALECTIC. [Pok. (s)lég- 959.] sleidh-. To slip, slide. 1. Germanic *s/idan, to slip, slide, in Old English s/idan, to slide: SLIDE. 2. Germanic *slid- in: a. Middle Low German sledde, a sled, sledge: SLED; b. Middle Dutch s/éde, a sled: SLEIGH; C. Middle Dutch sleedse, sleigh: SLEDGE. sleng”h-. To slide, make slide, sling, throw. 1. Germanic strong verb *slingwan and derived suffixed noun form *slingw-6- in Old Frisian slinge, sling, akin to the possi- ble source of Middle English sling, sling: SLING}; (SLING- SHOT). 2. Germanic variant strong verb *slinkan in Old English slincan, to creep: SLINK. 3. Suffixed o-grade form *slongh-ri-ko- in Latin lumbricus, intestinal worm, earthworm: LUMBRICOID. [In Pok. (sjleidh- 960, slenk- 961.] sleu-. Hypothetical base of a group of distantly related Germanic derivatives with various suffixes. 1. Germanic *slii-m- in Old English slima, sleep: SLUMBER. 2. Prob- ably Germanic *slautjan- in Old English “s/léte, sleet: SLEET. 3. Germanic *slus- in Norwegian slusk, sloppy weather, probably akin to the possible Scandinavian source of SLUSH. 4. Germanic *sleura- in Middle High German slier, mud, slime: SCHLIEREN. 5. Extended form *sleug- in Germanic ‘*sluk-, *slug- in: a. Norwegian dialectal slugg and Swedish dialectal slagga, slow-mov- ing animal or person, probably akin to the source of Middle English slugge, a sluggard, and sluggen, to be idle: SLUG?, SLUGGARD; b. Dutch /og, lazy, slack: LOGY. [Pok. (s)leu- 962.] sleubh-. To slide, slip. I. Basic form *sleubh-. 1. Ger- manic *slewb- in Old English s/éf, siif, slief, sleeve (into which the arm slips): SLEEVE. 2. Suffixed form *sleubh- ro- in Latin Jibricus, slippery: LUBRICATE, LUBRICITY, LUBRICIOUS. II. Variant Germanic form *sleup-. 1. Ger- manic *slup- in: a. Old English slypa, slyppe, slipa, slime, slimy substance: SLIP’; COWSLIP, OXLIP; b. Old English *sloppe, liquid food (perhaps > Middle English sloppe, a muddy place): sLoP!; c. Old English (ofer)slop, surplice (perhaps > Middle English sloppe, a kind of garment): SLOP?. 2. Germanic *s/aup- in Dutch sloep, sloop (< “gliding boat”): sLoop. [Pok. sleub(h)- 963.] sli-. Bluish. Contracted from *s/is-. 1. O-grade form *sloi- in Germanic *slaihw6n in Old English s/ah, sla, sloe (< “bluish fruit”): SLOE. 2. Suffixed form *sli-wo- in Latin livére, to be bluish: Livip. 3. Suffixed form *s/i-wd- in Serbo-Croatian sijiva, plum: sLivovitz. [Pok. (s)li- 965.] sloug-. Help, service. Celtic and Balto-Slavic. Suffixed form *sloug-o- in Old Irish slag, slog, army, host, whence Gaelic sluagh, army, host: SLEW!, SLOGAN. [Pok. slougo- 965.] smé-. To smear. Contracted from *smeo-. 1. Extended root *smeid- (< *smea-id-) in Germanic *smitan in Old English smitan, to daub, smear, pollute: SMITE. (2. At- tributed by some to this root, but more likely to be of unknown origin, is the Germanic root *mas-, spot, speck, in: a. Middle Dutch masel, pustule, spot, akin to the source of Middle English masel, measles-spot: MEASLES; b. Old French masere, mazre, knot in wood: MAZER.) 3. Attributed by some to this root, but perhaps distinct, is root *smik-, small, in: a. Latin mica, crumb, small piece, grain: MICA; b. Greek (s)mikros, small: MICRO-, MICRON; CHYLOMICRON, OMICRON. [Pok. smé- 966.] smeg-. To taste. Germanic *smak- in: a. Old English smzxc, flavor, taste: SMACK?; b. Middle Dutch and Mid- dle Low German smacken, to taste, make a sound with the lips while tasting food, akin to the source of SMACK!. [Pok. smeg(h)- 967.] smei-. To laugh, smile. 1. Germanic reshaped forms *smer-, *smar- in Old English smercian (with -k- forma- tive), to smile: SMIRK. 2. Germanic extended form *smil- in Swedish smila, to smile, probably akin to the Scandi-
961:(s)mer-3. Grease, fat. 1. Suffixed form *smer-wo- in Germanic *smerwa-, grease, fat, in Old High German smero, fat (> German Schmiere, grease): SCHMEER. 2. Germanic denominative verb *smerwjan, to spread grease on, in: a. Old English smierwan, smerian, to smear: SMEAR; b. Old High German smirwen, smerian (> German schmieren), to apply salve, smear: SMEAR- CASE. 3. Latin medulla (perhaps < *merulla, influenced by medius, middle), marrow: MEDULLA. [Pok. smeru- 970.
```


## [2026-09-07T16:21:38.313Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '956,962p' AHD_watkins1985.txt | grep -o '(s)mer-[12][^[]*\\[Pok[^]]*\\]' | head -5; echo \"---\"; sed -n '956,962p' AHD_watkins1985.txt | tr '.' '\\n' | grep -n -i 'mer-1\\|mer-2\\|memor\\|mourn\\|martyr' | head -20",
 "description": "Watkins (s)mer roots"
}
```


### [2026-09-07T16:21:38.384Z] TOOL RESULT

```
---
20: Suffixed zero-grade form *mr-no- in Germanic *murnan, to remember sorrowfully, in Old English murnan, to mourn: MOURN
24: Latin memor, mindful: MEMORABLE, (MEMO- RANDUM), MEMORY; COMMEMORATE, REMEMBER
28:(s)mer-2
```


## [2026-09-07T16:21:41.943Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=956 && NR<=962' AHD_watkins1985.txt | tr '\\n' ' ' | grep -o '(s)mer-1\\..\\{0,900\\}' | head -1",
 "description": "Watkins (s)mer-1 full"
}
```


### [2026-09-07T16:21:43.234Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T16:21:47.574Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=956 && NR<=962' AHD_watkins1985.txt | tr '\\n' ' ' | python3 -c \"\nimport sys,re\nt=sys.stdin.read()\ni=t.find('mer-')\nwhile i!=-1 and i<len(t):\n    seg=t[i-4:i+800]\n    if 'MOURN' in seg or 'MEMORY' in seg:\n        print(seg); break\n    i=t.find('mer-',i+1)\n\"",
 "description": "Extract Watkins smer-1"
}
```


### [2026-09-07T16:21:48.816Z] TOOL RESULT

```
 (s)mer-'. To remember. 1. Suffixed zero-grade form *mr-no- in Germanic *murnan, to remember sorrowfully, in Old English murnan, to mourn: MOURN. 2. Redupli- cated form “me-mor- in: a. Germanic *mi-mer- in Old Norse Mimir, a giant who guards the well of wisdom: Mimir; b. Latin memor, mindful: MEMORABLE, (MEMO- RANDUM), MEMORY; COMMEMORATE, REMEMBER. [Pok. (s)mer- 969.] (s)mer-2. To get a share of something. 1. Suffixed (sta- tive) form *mer-é- in Latin merére, meréri, to receive a share, deserve, serve: MERETRICIOUS, MERIT; EMERITUS. 2. Suffixed form *mer-o- in Greek meros (feminine meris), a part, division: -MERE, MERISTEM, MERO-, -MER- OUS; (ALLOMERISM), (DIMER), (ISOMER), (MONOMER), TRIMER. [In Pok. (s)mer- 969.] (s)mer-3. Grease, fat. 1. Suffixed form *smer-wo- in Germanic *smerwa-, greas
```


## [2026-09-07T16:22:02.809Z] TOOL CALL #71: Bash

```json
{
 "command": "for U in \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/mun%C3%BEaz' \\\n 'https://en.wiktionary.org/wiki/%CE%BC%CE%AC%CF%83%CF%84%CE%B1%CE%BE' \\\n 'https://www.etymonline.com/word/mandrel' \\\n 'https://en.wiktionary.org/wiki/mando' \\\n 'https://www.etymonline.com/word/mustache' \\\n 'https://en.wiktionary.org/wiki/%D9%85%D8%B5%D8%B7%D9%83%D9%89' \\\n 'https://en.wiktionary.org/wiki/%D8%A2%D9%85%D8%A7%D8%B1' \\\n 'https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D8%AC%D9%85%D9%86%D8%AF' \\\n 'https://en.wiktionary.org/wiki/%CE%BC%CE%AC%CF%81%CF%84%CF%85%CF%82' ; do\n  python3 tools/fetch_source.py \"$U\" --note 'pdf page 334: Menth/Mer1 verification' 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-07T16:22:07.367Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/029635a46c0f9b81.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/da08ae88272a4014.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cf555aff0d2f034f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a4324142dbe4b35b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c4590e5fac4e5d4e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/70913c033528d1e3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cca24013da227b08.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6f2b54e8f9ab39bb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0e5383bedc954781.txt
```


## [2026-09-07T16:22:12.030Z] TOOL CALL #72: Bash

```json
{
 "command": "S=/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && mkdir -p data/verification/sources/refs/ocr/BOOK && cp \"$S/pg334.png\" data/verification/sources/refs/ocr/BOOK/334.png && ls -la data/verification/sources/refs/ocr/BOOK/334.png",
 "description": "Copy page PNG for audit"
}
```


### [2026-09-07T16:22:12.095Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 97297 Sep  7 12:22 data/verification/sources/refs/ocr/BOOK/334.png
```


## [2026-09-07T16:22:15.913Z] TOOL CALL #73: Bash

```json
{
 "command": "sed -n '1,80p' tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-07T16:22:15.967Z] TOOL RESULT

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


## [2026-09-07T16:22:19.041Z] TOOL CALL #74: Bash

```json
{
 "command": "sed -n '80,140p' tools/verify_check.py",
 "description": "Rest of verify_check"
}
```


### [2026-09-07T16:22:19.084Z] TOOL RESULT

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


## [2026-09-07T16:23:06.460Z] AGENT

Now I'll write the verification file.


## [2026-09-07T16:34:02.992Z] TOOL CALL #75: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk334.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_MUNTH = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/mun%C3%BEaz\"\nW_MASTAX = \"https://en.wiktionary.org/wiki/%CE%BC%CE%AC%CF%83%CF%84%CE%B1%CE%BE\"\nE_MANDREL = \"https://www.etymonline.com/word/mandrel\"\nW_MANDO = \"https://en.wiktionary.org/wiki/mando\"\nE_MUSTACHE = \"https://www.etymonline.com/word/mustache\"\nW_MASTAKI = \"https://en.wiktionary.org/wiki/%D9%85%D8%B5%D8%B7%D9%83%D9%89\"\nW_AMAR = \"https://en.wiktionary.org/wiki/%D8%A2%D9%85%D8%A7%D8%B1\"\nW_ARJMAND = \"https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D8%AC%D9%85%D9%86%D8%AF\"\nW_MARTYS = \"https://en.wiktionary.org/wiki/%CE%BC%CE%AC%CF%81%CF%84%CF%85%CF%82\"\n\nPOK_MENTH2 = (\"POK_full.txt 'Root / lemma: menth-2 | Meaning: to chew, mouth ... Page(s): 732-733': \"\n  \"'Old Indic math- devour; gr. masaomai chew, bite (from *maθ-ia, IE *mnth-ia), mastazo chew, \"\n  \"mastax mouth and mouthful, mastichao knirsche mit den Zaehnen ... Latin mando to chew (*menthd) ... \"\n  \"zero grade Gothic munths, OIcel. mudr, munnr, OE mud, OHG mund mouth; or to cymr. mant, see above menth-1'\")\nPOK_MENTH1 = (\"POK_full.txt 'Root / lemma: menth-1, meth- | Meaning: to mix up, stir ... Page(s): 732': \"\n  \"'Old Indic manthati, mathnati swirls, mixes, stirs, shakes, mantha- m. gyration, mixing spoon, \"\n  \"Avestan mant- bestir; ... Latin (Oscan) mamphur, better manfur ein Stueck der Drehbank'\")\nPOK_SMER = (\"POK_full.txt 'Root / lemma: (s)mer- | Meaning: to remember; to care for ... Page(s): 969-970': \"\n  \"'Old Indic smarati reminds sich, gedenkt ... Avestan maraiti, hismaraiti (be)merkt, mimara- eingedenk ... \"\n  \"Latin memor eingedenk ... Gothic maurnan, OE murnan, OHG mornen care for, worry'\")\n\nout = {\n \"pdf_page\": 334,\n \"book_page\": 304,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-07\",\n \"entries\": []\n}\n\n# ---------------- ENTRY 0 ----------------\ne0 = {\n \"entry\": 0,\n \"root\": \"Menth\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"PIE *mendʰ- / *menth- 'to chew' (Pokorny 2. menth- 732-733; Watkins mendh-2 'to chew')\",\n \"note\": (\"Pokorny 732-733 really does have a root 2. menth- glossed 'to chew, mouth', and Watkins/AHD \"\n   \"prints it as mendh-2 'To chew' with the same members (Lat. mandere, Gk. masasthai, mastax, mystax, \"\n   \"mastikhan) — so Nourai's root box, language label and gloss are faithful to his sources (POK:732 = the \"\n   \"right page; AHD:1529 = the 1976 appendix page for mendh-). Two caveats make it only 'plausible' today. \"\n   \"(a) The aspiration: AHD/Watkins and Wiktionary write *mendʰ-, Pokorny *menth-; that is a notational \"\n   \"difference, not a real disagreement. (b) The membership is now doubted at both ends: Beekes (EDG) treats \"\n   \"the whole Greek group masáomai / mastázō / mástax as Pre-Greek substrate, and Kroonen/Wiktionary derive \"\n   \"PGmc *munþaz 'mouth' not from 'chew' but from *men- 'chin' (Lat. mentum, Welsh mant, Hitt. mēni-) — a \"\n   \"route Pokorny himself offers as an alternative ('oder zu cymr. mant, s. oben men-1') and which Watkins \"\n   \"actually adopts (mouth stands under his men-2 'To project', not under mendh-2). De Vaan meanwhile \"\n   \"derives Lat. mandō from *menth₂- 'to stir, whirl' — i.e. he merges this root with Nourai's next entry.\"),\n \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *mendʰ-/*menth- «جویدن» در فرهنگ پوکورنی (ص ۷۳۲–۷۳۳، شمارهٔ ۲) و در \"\n   \"پیوستِ ریشه‌های واتکینز (AHD) با همان مصادیق (mandō لاتین، masáomai و mástax و mýstax یونانی) آمده است؛ \"\n   \"پس نامِ ریشه و برچسبِ زبان و معنایی که نورایی آورده با مآخذ خودش می‌خواند. اما پژوهش امروزی دو جای آن را \"\n   \"سست می‌داند: بیکس واژگانِ یونانی این خانواده را پیش‌یونانی (زیرلایه‌ای) می‌شمارد، و کرونن و ویکی‌واژه واژهٔ \"\n   \"«دهان» ژرمنی را نه از این ریشه بلکه از *men- «چانه» (mentum لاتین، mant ولزی) می‌گیرند — راهی که خودِ \"\n   \"پوکورنی هم به‌عنوان گزینهٔ دوم یاد کرده و واتکینز پذیرفته است. از این رو: ادعای نورایی با احتیاط پذیرفتنی است.\"),\n \"sources\": [W_MASTAX, W_MUNTH, E_MUSTACHE, W_MANDO],\n \"ref_check\": [\n   {\"ref\": \"POK:732\", \"status\": \"supports\", \"note\": POK_MENTH2},\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. mendh-2 (AHD_watkins1985.txt line 749)\", \"stance\": \"supports\",\n    \"note\": \"'mendh-2. To chew. 1. Latin mandere, to chew ... 2. Zero-grade form *mndh- in: a. Greek masasthai (< *math-ya-), to chew; b. Greek mastax, mouth, the model for expressive Greek (Doric) mustax, upper lip, mustache; c. Greek mastikhan, to grind the teeth: MASTICATE. [Pok. 2. menth- 732.]' — the same five Greek forms Nourai lists.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II p. 270 (WLD_Bd2_pages.txt line 17746)\", \"stance\": \"supports\",\n    \"note\": \"'menth- \\\"kauen; Gebiß, Mund\\\"' with μάθυιαι, μασάομαι, μαστάζω, μάσταξ, μαστιχάω, lat. mando, got. munþs, ags. mud, ahd. mund; and the footnote 'Ehrlich aaO. hält menth- \\\"kauen\\\" für ursprgl. dasselbe wie menth- \\\"quirlen\\\" (\\\"drehende Kaubewegung\\\"); fraglich.'\"},\n   {\"src\": \"KLN\", \"where\": \"p. 1009 s.v. mouth (KLN_1966.txt line 24535)\", \"stance\": \"supports\",\n    \"note\": \"'fr. I.-E. base *menth-, \\\"to chew\\\", whence prob. also Gk. μάθυιαι \\\"jaw\\\", μασάομαι \\\"I chew, bite\\\", μαστάζω, μάσταξ \\\"mouth, jaws\\\" (lit. \\\"that with which one chews\\\"), L. mandere, \\\"to chew\\\" ... Cp. mastic, masticate, maxilla, mustache.'\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, grep 'menth' in IEC.txt\", \"stance\": \"silent\",\n    \"note\": \"grep -n -i 'menth' IEC.txt returned no headword for this root in the OCR of Mann's comparative dictionary.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck, grep 'mastax|masaomai' in SYN.txt\", \"stance\": \"silent\",\n    \"note\": \"no hit for the Greek chewing group under Buck's 'chew'/'mouth' articles in this OCR.\"},\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Greek\",\n \"words\": \"math-ya; mustax; mastax; mastixan; mastixĕ\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"All five forms are real Greek and all five stand in Nourai's own two references. *math-ya \"\n   \"is not an attested word but the reconstruction behind Attic μασάομαι 'I chew, bite' (Pokorny: 'μασάομαι \"\n   \"chew, bite (from *maθ-ia, Indo-European *mnth-ia)'; Watkins: 'Greek masasthai (< *math-ya-)'): zero-grade \"\n   \"*mn̥dʰ- + the -yo- present suffix, with *dʰy > Attic σσ / Ionic-Attic σ. μάσταξ, -ακος f. 'jaws, mouth; \"\n   \"mouthful' is a -k- stem on the same base, literally 'that with which one chews' (Klein). μύσταξ is the \"\n   \"Doric/Laconian variant of μάσταξ with expressive u-vocalism, specialised to 'upper lip, moustache' — \"\n   \"Watkins calls it 'the model for expressive Greek (Doric) mustax'. μαστιχάω / inf. μαστιχᾶν 'to gnash, \"\n   \"grind the teeth' is a -ιχ- iterative (Nourai's 'mastixan' is the infinitive). μαστίχη 'mastic' is the \"\n   \"same stem used for the Chian resin that was chewed as a gum — hence Nourai's gloss 'chewing gum', which \"\n   \"is literally right (Klein s.v. mastic). The derivation from the IE root is what Pokorny, Walde-Pokorny, \"\n   \"Klein and Watkins all print; it is 'plausible' rather than 'confirmed' only because Beekes (EDG) judges \"\n   \"μάσταξ, μασάομαι and μαστάζω to be Pre-Greek substrate words and gives them no IE root at all.\"),\n \"derivation_fa\": (\"هر پنج صورت یونانی واقعی‌اند و در هر دو مأخذی که نورایی می‌آورد (پوکورنی و واتکینز) هم \"\n   \"دیده می‌شوند. math-ya واژهٔ ضبط‌شده نیست، بلکه صورت بازسازیِ پشتِ masáomai «جویدن» است: پایهٔ صفرگونهٔ \"\n   \"*mn̥dʰ- به‌همراه پسوند حالِ ‑yo‑ که در آتیک به σσ/σ بدل شده. mástax «آرواره، دهان» با پسوندِ ‑k بر همان \"\n   \"پایه ساخته شده، و mýstax گونهٔ دوری/لاکونیایی آن با واکهٔ u است که معنایش به «لبِ بالا، سبیل» محدود شده. \"\n   \"mastikháō (مصدر mastikhân) «دندان بر هم ساییدن» فعلِ تکراری با ‑ikh‑ است، و mastíkhē «سقز، مصطکی» همان \"\n   \"ستاک است که برای صمغِ جویدنیِ جزیرهٔ خیوس به کار رفته؛ پس ترجمهٔ نورایی («آدامس») تحت‌اللفظ درست است. \"\n   \"پیوند این خانواده با ریشهٔ هندواروپایی همان است که پوکورنی، والده‑پوکورنی، کلاین و واتکینز نوشته‌اند؛ تنها \"\n   \"از آن رو «با احتیاط پذیرفتنی» است که بیکس این واژه‌ها را پیش‌یونانی می‌داند.\"),\n \"sources\": [W_MASTAX, E_MUSTACHE],\n \"ref_check\": [\n   {\"ref\": \"POK:732\", \"status\": \"supports\", \"note\": POK_MENTH2 + \" — covers math-ya (*mnth-ia), mastax, mastazo, mastichao.\"},\n   {\"ref\": \"AHD:1529\", \"status\": \"supports\", \"note\": \"Nourai's page is in the 1976 New College appendix (not open online); the identical root article in the 1985 Watkins standalone (AHD_watkins1985.txt line 749) reads 'mendh-2. To chew ... Greek masasthai (< *math-ya-) ... Greek mastax, mouth, the model for expressive Greek (Doric) mustax, upper lip, mustache ... Greek mastikhan, to grind the teeth', so the citation is sound.\"},\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II p. 270 (line 17746 ff.)\", \"stance\": \"supports\",\n    \"note\": \"'Gr. μάθυιαι· γνάθοι Hes., μασάομαι \\\"kaue, beiße\\\" (μαθ- ...), μαστάζω \\\"kaue\\\", μάσταξ \\\"Mund\\\" und \\\"Atzung\\\", μασυχάω/μαστιχάω \\\"knirsche mit den Zähnen\\\"' — the whole Greek set, s.v. menth- 'kauen'.\"},\n   {\"src\": \"KLN\", \"where\": \"pp. 1009 (mouth), ~1019 (mustache), 1015 (mastic)\", \"stance\": \"supports\",\n    \"note\": \"s.v. mustache: 'fr. Gk. μύσταξ, \\\"upper lip, mustache\\\", which is rel. to μάσταξ, \\\"mouth, jaws\\\", lit. \\\"that with which one chews\\\", μαστίχαω, \\\"I gnash the teeth\\\", μασάομαι, \\\"I chew, bite\\\", fr. I.-E. base *menth, \\\"to chew\\\"'; s.v. mastic: 'fr. VL. mastichum, fr. Gk. μαστίχη, \\\"mastic\\\"'.\"},\n   {\"src\": \"Wiktionary/Beekes\", \"where\": W_MASTAX, \"stance\": \"contradicts\",\n    \"note\": \"μάσταξ 'related to μασάομαι (\\\"to chew\\\") and μαστάζω (\\\"to chew\\\"), both terms [Beekes] suspects to be of Pre-Greek origin' — no PIE root is assigned.\"},\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Arabic\",\n \"words\": \"mastakî\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Arabic مُصْطَكَى / مُصْطَكَاء / مُصْطَكِيّ 'mastic, the gum-resin of Pistacia lentiscus' is \"\n   \"indeed the Greek word μαστίχη, but the transmission was not direct from Greek to Arabic: Wiktionary \"\n   \"(with the Semitic literature) has it borrowed from Aramaic מצטכי mūṣṭəḵē, itself from Ancient Greek \"\n   \"μαστίχη — the Aramaic pharyngealised ṣ/ṭ for Greek σ/τ is exactly the shape the Arabic form shows \"\n   \"(mastíkhē > mūṣṭəḵē > muṣṭakā), a pattern typical of Greek plant- and drug-names entering Arabic through \"\n   \"Syriac medical translation in the 8th-9th c. Semantically nothing shifted: it stays the chewable resin of \"\n   \"the lentisk. So Nourai's arrow Greek → Arabic is right in substance; only the Aramaic/Syriac relay is \"\n   \"left out of the chart.\"),\n \"derivation_fa\": (\"«مُصْطَکَی / مصطکاء» عربی همان mastíkhē یونانی است، اما وام‌گیری مستقیم نبوده: بر پایهٔ \"\n   \"ویکی‌واژه و پژوهش‌های سامی، عربی آن را از آرامی מצטכי (mūṣṭəḵē) گرفته و آرامی از یونانی. همین واسطه است که \"\n   \"س و ت یونانی را به ص و ط (واک‌های حلقی‌شدهٔ سامی) بدل کرده — الگویی آشنا در نام‌های گیاهی و داروییِ یونانی \"\n   \"که در سدهٔ دوم و سوم هجری از راه ترجمه‌های سریانی به عربی رسیده‌اند. معنا دگرگون نشده و همان صمغِ درختِ \"\n   \"پستهٔ وحشی است. پس جهتِ پیکانِ نورایی (یونانی ← عربی) درست است و تنها حلقهٔ آرامی/سریانی از نمودار افتاده.\"),\n \"sources\": [W_MASTAKI],\n \"ref_check\": [\n   {\"ref\": \"TAD:69\", \"status\": \"supports\", \"note\": \"al-Unaysi, Tafsir al-alfaz al-dakhila, TAD_pages.txt leaf 72 (printed numeral on the page ≈ 68-69), line 2655: 'مصطكي - ونانى [يونانى] ... معناه هو عصارة شجرة تشبه الفستق واليطم تمد فتتعقد صمغا يعلك مرادفه السك' — 'mastakī: Greek; it is the sap of a tree resembling the pistachio and the terebinth, which flows and congeals into a gum that is chewed'. Explicitly labels the word Greek and explicitly mentions chewing, i.e. exactly Nourai's arrow and gloss.\"},\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 1015 s.v. mastic (KLN_1966.txt line 23085)\", \"stance\": \"supports\",\n    \"note\": \"'mastic, n., resin obtained from certain trees. — ME. mastik, fr. OF. mastic, fr. VL. mastichum, fr. Gk. μαστίχη, \\\"mastic\\\". See masticate and cp. almaciga.' — Klein's cross-reference 'almaciga' is the Spanish Arabism al-maṣṭakā, i.e. he knows the Arabic link.\"},\n   {\"src\": \"AFM\", \"where\": \"Addi Shir, grep 'مصطك' in AFM.txt / AFM_pages.txt\", \"stance\": \"silent\",\n    \"note\": \"no hit — expected, since Addi Shir collects Persian (not Greek) loans in Arabic, and mastic is not Persian.\"},\n   {\"src\": \"Wiktionary\", \"where\": W_MASTAKI, \"stance\": \"partial\",\n    \"note\": \"'Borrowed from Aramaic מצטכי (mūṣṭəḵē), borrowed from Ancient Greek μαστίχη' — same origin, one intermediate more than the chart shows. Persian مصطکی is listed there as a descendant of the Arabic.\"},\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Persian\",\n \"words\": \"mastakî\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"New Persian مصطکی mastakī 'mastic; the chewable resin of Pistacia lentiscus / P. atlantica' \"\n   \"is a straight Arabic loan (an Arabicised Greek word coming back into Persian through the Arabic medical \"\n   \"vocabulary of the 4th-5th c. AH), and Moʿīn marks it as such: his entry مصطکی opens with the origin tag \"\n   \"[معر.] 'Arabicised', names the by-form مصطکاء (also معرّب), and describes the resin oozing from the \"\n   \"branches of the mastic shrub and softening 'بر اثر جویدن' — under chewing. The Persian keeps the Arabic \"\n   \"spelling with ص and ط although Persian has no pharyngealised consonants, which is itself the fingerprint \"\n   \"of the Arabic relay. Nourai's arrow Arabic → Persian and his gloss are both right.\"),\n \"derivation_fa\": (\"«مصطکی» در فارسی نو وام‌واژه‌ای از عربی است — یعنی واژه‌ای یونانی که نخست معرّب شده و سپس \"\n   \"از راه واژگانِ پزشکیِ عربیِ سده‌های چهارم و پنجم هجری به فارسی بازگشته است. معین در «فرهنگ فارسی» ذیل \"\n   \"«مصطکی» همین را می‌گوید: نشانهٔ ریشه‌ای [معر.] را می‌آورد، گونهٔ «مصطکاء» را هم معرّب می‌خواند و صمغی را \"\n   \"وصف می‌کند که «از ساقه و شاخه‌های درختچهٔ مصطکی خارج می‌شود» و «بر اثر جویدن به سهولت در زیر دندان نرم \"\n   \"می‌گردد». نگه‌داشتنِ ص و ط در املای فارسی — با آنکه فارسی واکِ حلقی‌شده ندارد — خود گواهِ واسطهٔ عربی است. \"\n   \"ادعای نورایی درست است.\"),\n \"sources\": [W_MASTAKI],\n \"ref_check\": [\n   {\"ref\": \"MON:4173\", \"status\": \"partial\", \"note\": \"The 6-vol Amir Kabir pagination cannot be mapped online and is not in the local scans, so the page number itself is unchecked; the entry text is in the local OCR of Moʿīn (MON_part2.txt line 58747 ff.): 'مصطکی: [معر. ... مصطکاء معر.] (اِ.) (گیا.) گونه‌ای سقز که ... از ساقه و شاخه‌های درختچه مصطکی خارج می‌شود ... و بر اثر جویدن به سهولت در زیر دندان نرم می‌گردد.' Content supports Nourai fully (loan tag + chewable resin); status 'partial' only because the cited page could not be verified.\"},\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"MON_part2.txt line 58747 ff. s.v. مصطکی\", \"stance\": \"supports\",\n    \"note\": \"origin tag [معر.] and the description of the chewable resin, quoted above.\"},\n   {\"src\": \"BQT\", \"where\": \"grep 'مصطک' in BQT_v1/v2/v3/v4_pages.txt\", \"stance\": \"silent\",\n    \"note\": \"Borhān-e Qāṭeʿ has no مصطکی article in the OCR of these volumes (it is a drug-name of the Arabic medical lexicon rather than a Persian dari word).\"},\n   {\"src\": \"Wiktionary\", \"where\": W_MASTAKI, \"stance\": \"supports\",\n    \"note\": \"Persian مصطکی (mastaki) is listed on the Arabic page as a descendant of Arabic مصطكى.\"},\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 4, \"lang\": \"English\",\n \"words\": \"mustache\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"English mustache (first attested 1580s) does go back to Doric Greek μύσταξ, but through four \"\n   \"intermediate stages that the chart's single arrow compresses: Doric μύσταξ, gen. μύστακος 'upper lip, \"\n   \"moustache' → Medieval Greek μουστάκιον (diminutive) → Italian mostaccio / mostacchio → French (15th c.) \"\n   \"moustache → English. An earlier and separate English borrowing, mostacchi (1550s), came from Italian or \"\n   \"Spanish mostacho and survives in the plural mustachios. Semantically the shift is 'upper lip' → 'the hair \"\n   \"on the upper lip'. Etymonline and Klein give the identical chain; Watkins prints 'Greek mastax, mouth, the \"\n   \"model for expressive Greek (Doric) mustax, upper lip, mustache: MUSTACHE', which is precisely Nourai's \"\n   \"arrow from the Greek box, so his AHD citation is exact.\"),\n \"derivation_fa\": (\"واژهٔ انگلیسیِ mustache (نخستین کاربرد در دههٔ ۱۵۸۰) به mýstax دوری بازمی‌گردد، اما از چهار \"\n   \"حلقهٔ میانی می‌گذرد که پیکانِ یگانهٔ نمودار آن‌ها را در خود فشرده است: mýstax دوری «لبِ بالا، سبیل» ← \"\n   \"moustákion در یونانیِ میانه (صورتِ تصغیر) ← mostaccio/mostacchio ایتالیایی ← moustache فرانسویِ سدهٔ \"\n   \"پانزدهم ← انگلیسی. وام‌گیریِ جداگانه و کهن‌ترِ mostacchi (دههٔ ۱۵۵۰) از ایتالیایی یا اسپانیایی mostacho \"\n   \"آمده و در جمعِ mustachios بازمانده است. تحولِ معنایی از «لبِ بالا» به «مویِ لبِ بالا» است. ریشه‌شناسی \"\n   \"آنلاین و کلاین همین زنجیره را می‌دهند و واتکینز نیز آشکارا mustax را «الگویِ» MUSTACHE می‌خواند؛ پس \"\n   \"ارجاعِ نورایی به AHD دقیق است و ادعایش درست.\"),\n \"sources\": [E_MUSTACHE, W_MASTAX],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. mendh-2 (AHD_watkins1985.txt line 749): 'b. Greek mastax, mouth, the model for expressive Greek (Doric) mustax, upper lip, mustache: (MOSTACCIOLI), MUSTACHE'.\"},\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. ~1019 s.v. mustache (KLN_1966.txt line 24758)\", \"stance\": \"supports\",\n    \"note\": \"'mustache, moustache, n. — MF. (= F.) moustache, fr. It. mostaccio, a collateral form of mostacchio, fr. MGk. μουστάκι(ον), fr. Gk. μύσταξ, \\\"upper lip, mustache\\\" ... fr. I.-E. base *menth, \\\"to chew\\\"'; and 'mustachio, mustache, n. — A blend of Sp. mostacho and It. mostaccio.'\"},\n   {\"src\": \"Etymonline\", \"where\": E_MUSTACHE, \"stance\": \"supports\",\n    \"note\": \"'1580s ... from French (15c.) moustache, from Italian mostaccio, from Medieval Greek moustakion, from Doric Greek mystax (gen. mystakos) \\\"upper lip, mustache\\\" ... possibly from PIE root *mendh- \\\"to chew\\\"; but the whole Greek group may be Pre-Greek.'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, grep 'mustache|moustache' in SKT.txt\", \"stance\": \"partial\",\n    \"note\": \"grep returns no separate headword in this OCR of the Concise; no independent statement recorded.\"},\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 5, \"lang\": \"Germanic\",\n \"words\": \"muntha\",\n \"verdict\": \"disputed\",\n \"derivation\": (\"The form is right: Proto-Germanic *munþaz m. 'mouth' (Gothic munþs, ON munnr/múðr, OE mūð, \"\n   \"OHG mund), which Nourai transliterates 'muntha'. What is disputed is the parent. Pokorny does list it \"\n   \"under menth-2 'to chew' — 'zero grade Gothic munþs, OIcel. mudr, munne, OE mud, OHG mund \\\"mouth\\\"' — but \"\n   \"in the same sentence he offers the alternative 'or to cymr. mant, see above men-1', and Walde-Pokorny II \"\n   \"270 already notes Ehrlich's objection that the Germanic and OE/ON bit-words belong with Latin mentum \"\n   \"'chin' and Welsh mant, i.e. with *men- 'to project'. Modern handbooks take that second road: Watkins — \"\n   \"the very authority Nourai cites here — puts 'Germanic *munthaz in Old English mūth, mouth: MOUTH' under \"\n   \"men-2 'To project ... a western Indo-European word for a projecting body part, variously \\\"chin, jaw, \"\n   \"mouth\\\"', and Wiktionary/Kroonen reconstruct *mn̥-tó-s 'mouth, jaw' from *men- 'chin', cognate with Lat. \"\n   \"mentum, Welsh mant, Hitt. mēni- 'face, cheek'. Phonologically both work (*mn̥dʰ-tó- or *mn̥-tó- > *munþa- \"\n   \"by the nasal-plus-dental development); it is the root that is contested, and the modern preference is \"\n   \"against the chart. Klein (p. 1009) is the one modern-ish dictionary that still sides with Nourai.\"),\n \"derivation_fa\": (\"صورتِ واژه درست است: ژرمنیِ آغازین *munþaz «دهان» (گوتیک munþs، نورس باستان munnr/múðr، \"\n   \"انگلیسی باستان mūð، آلمانی علیای باستان mund) که نورایی آن را muntha آورده. آنچه محلِ اختلاف است پدرِ این \"\n   \"واژه است. پوکورنی آن را ذیلِ menth- «جویدن» می‌آورد، اما در همان جمله گزینهٔ دیگری هم می‌نهد: «یا به mant \"\n   \"ولزی، نگاه کنید به men-1». والده‑پوکورنی (ج ۲ ص ۲۷۰) نیز ایرادِ ارلیش را نقل می‌کند که این واژه با mentum \"\n   \"لاتین «چانه» و mant ولزی، یعنی با ریشهٔ *men- «برآمدن»، هم‌خانواده است. کتاب‌های امروزی همین راهِ دوم را \"\n   \"برگزیده‌اند: واتکینز — همان مرجعی که نورایی در این گره به آن ارجاع می‌دهد — «دهان» را ذیلِ men-2 «برآمدن» \"\n   \"می‌آورد، و ویکی‌واژه و کرونن آن را از *mn̥-tó-s «دهان، آرواره» از ریشهٔ *men- «چانه» می‌گیرند. پس: پژوهش \"\n   \"امروزی ادعای نورایی را رد می‌کند و به‌جای «جویدن» ریشهٔ «چانه/برآمدگی» را می‌نشاند؛ تنها کلاین همچنان با \"\n   \"نورایی هم‌رأی است.\"),\n \"sources\": [W_MUNTH],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"contradicts\", \"note\": \"Watkins 1985 (AHD_watkins1985.txt line 749) puts mouth NOT under mendh-2 'to chew' but under 'men-2. To project. 1. Suffixed zero-grade form *mn-to- in a western Indo-European word for a projecting body part, variously \\\"chin, jaw, mouth,\\\" in Germanic *munthaz in Old English muth, mouth: MOUTH ... [Pok. 1. men- 726, 2. menth- 732.]' — so Nourai's own reference assigns this node to a different root.\"},\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"p. 732-733 s.v. menth-2\", \"stance\": \"partial\",\n    \"note\": \"'zero grade Gothic munth-s, Old Icelandic mudr, munne, Old English mud, Old High German mund \\\"mouth\\\"; or to cymr. mant, see above menth-1 [read: men-1]' — Pokorny lists it here but explicitly leaves the other root open.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II p. 270 (line 17769 ff.)\", \"stance\": \"partial\",\n    \"note\": \"'Ahd. mindil, gamindel \\\"Gebiß am Zaum\\\", ags. midl ds. ... doch unter Verb. mit lat. mentum \\\"Kinn\\\", cymr. mant, die wohl zu men- \\\"hervorragen\\\", Ehrlich KZ. 41, 287 f.' — and 'schwundstufig got. munþs, aisl. mudr, ags. mud, ahd. mund \\\"Mund\\\"' with a list of older interpretations.\"},\n   {\"src\": \"KLN\", \"where\": \"p. 1009 s.v. mouth\", \"stance\": \"supports\",\n    \"note\": \"'ME. mouth, fr. OE. mūð, rel. to OS., OFris. mūth, ON. munnr, múdr ... Goth. munþs, \\\"mouth\\\" ... fr. I.-E. base *menth-, \\\"to chew\\\"'.\"},\n   {\"src\": \"Wiktionary\", \"where\": W_MUNTH, \"stance\": \"contradicts\",\n    \"note\": \"'From Proto-Indo-European *mn̥-tó-s (\\\"mouth, jaw\\\"), from the root *men- (\\\"chin\\\") with the suffix *-tós'; cognates Latin mentum 'chin', Welsh mant, Hittite mēni- 'face, cheek'.\"},\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 6, \"lang\": \"English\",\n \"words\": \"mouth\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"This last step is uncontroversial whichever root the Germanic word belongs to: Proto-Germanic \"\n   \"*munþaz > Old English mūð (with the regular West Germanic loss of the nasal before þ and compensatory \"\n   \"lengthening of the vowel, the same change as in OE tōð 'tooth' < *tanþuz and gōs 'goose' < *gans-) > \"\n   \"Middle English mouth (spelling ou for /uː/ after the Norman scribal convention) > Modern English mouth \"\n   \"with the Great Vowel Shift diphthongisation /uː/ > /aʊ/. Gothic munþs and OHG mund keep the nasal, so the \"\n   \"English form is the innovating one. Klein and Watkins both give this chain verbatim.\"),\n \"derivation_fa\": (\"این پله، هر ریشه‌ای هم که واژهٔ ژرمنی داشته باشد، بی‌اختلاف است: از *munþaz ژرمنیِ آغازین \"\n   \"به mūð انگلیسیِ باستان — با حذفِ قاعده‌مندِ خیشومی پیش از þ در ژرمنیِ باختری و کشیدگیِ جبرانیِ واکه، همان \"\n   \"دگرگونی که در tōð «دندان» (از *tanþuz) و gōs «غاز» (از *gans-) دیده می‌شود — سپس mouth در انگلیسیِ میانه \"\n   \"(نگارشِ ou برای /uː/ به رسمِ کاتبانِ نورمن) و در پایان mouth امروزی با دوواکه‌شدنِ /uː/ به /aʊ/ در «جابه‌جاییِ \"\n   \"بزرگِ واکه‌ها». گوتیک munþs و آلمانی علیای باستان mund خیشومی را نگه داشته‌اند، پس صورتِ انگلیسی نوآور است. \"\n   \"ادعای نورایی درست است.\"),\n \"sources\": [W_MUNTH],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins 1985 has 'Germanic *munthaz in Old English muth, mouth: MOUTH' — the Germanic→English step exactly as drawn; but the article it stands in is men-2 'To project', not mendh-2 'To chew' (see node #5).\"},\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 1009 s.v. mouth\", \"stance\": \"supports\",\n    \"note\": \"'mouth, n. — ME. mouth, mouthe, fr. OE. mūð, rel. to OS., OFris. mūth, ON. munnr, múdr, Dan. mund, Swed. mun, MDu. mont, mond, Du. mond, OHG. mund, MHG. munt, G. Mund, Goth. munþs, \\\"mouth\\\".'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, s.v. mouth (grep in SKT.txt)\", \"stance\": \"silent\",\n    \"note\": \"no headword line recovered from this OCR; nothing recorded either way.\"},\n   {\"src\": \"Wiktionary\", \"where\": W_MUNTH, \"stance\": \"supports\",\n    \"note\": \"OE mūð is listed among the descendants of *munþaz.\"},\n ]\n})\n\nout[\"entries\"].append(e0)\n\n# ---------------- ENTRY 1 ----------------\ne1 = {\n \"entry\": 1,\n \"root\": \"Menth, Meth\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *menth₂- 'to stir, whirl' (Pokorny 1. menth-, meth- 732; LIV *menth₂-)\",\n \"note\": (\"The root box is exactly right, down to the second variant: Pokorny p. 732 has 'Root / lemma: \"\n   \"menth-1, meth- | Meaning: to mix up, stir', with Old Indic manthati/mathnāti 'swirls, mixes, stirs, \"\n   \"shakes', mantha- 'gyration, mixing spoon' and Avestan mant- 'bestir'. Nourai's 'Menth, Meth' reproduces \"\n   \"Pokorny's double lemma and 'to turn, stir' his gloss; the language label 'Indo-European' is correct. \"\n   \"Modern reconstruction writes it *menth₂- (LIV, de Vaan), and de Vaan in fact derives Latin mandere \"\n   \"'to chew' from THIS root ('to stir, whirl' → 'chew'), i.e. he merges it with Nourai's previous entry; \"\n   \"Walde-Pokorny II 270 already reports Ehrlich's same proposal, calling it 'fraglich'. The problem with \"\n   \"this entry is not the root but the first branch: the Persian -mand suffix hung under it belongs to the \"\n   \"Avestan possessive suffix -mant-/-vant- (PIE *-ment-/*-uent-), which has nothing to do with the verb \"\n   \"'to stir' — see node #1.\"),\n \"note_fa\": (\"جعبهٔ ریشه کاملاً درست است، حتی در آوردنِ گونهٔ دوم: پوکورنی در ص ۷۳۲ ریشهٔ «menth-1, meth-» را با \"\n   \"معنای «آمیختن، هم زدن» ثبت کرده و برای آن سنسکریت manthati/mathnāti «هم می‌زند، می‌آمیزد، می‌جنباند» و \"\n   \"mantha- «چرخش، ملاقهٔ هم‌زن» و اوستایی mant- «جنباندن» را می‌آورد؛ پس «Menth, Meth: چرخاندن، هم زدن» \"\n   \"بازنویسیِ درستِ همان مدخل است. بازسازیِ امروزی آن را *menth₂- می‌نویسد و دخاون فعلِ mandere «جویدن» لاتین \"\n   \"را هم از همین ریشه می‌گیرد، یعنی این ریشه را با ریشهٔ مدخلِ پیشین یکی می‌داند — همان پیشنهادی که ارلیش \"\n   \"پیش‌تر داده و والده‑پوکورنی آن را «مشکوک» خوانده بود. اشکالِ این مدخل نه در ریشه است بلکه در شاخهٔ نخستِ \"\n   \"آن: پسوندِ «ـمند» فارسی به پسوندِ دارندگیِ اوستاییِ ‑mant-/‑vant- (از *-ment-/*-uent- هندواروپایی) \"\n   \"برمی‌گردد و با فعلِ «هم زدن» پیوندی ندارد.\"),\n \"sources\": [W_MANDO],\n \"ref_check\": [\n   {\"ref\": \"POK:732\", \"status\": \"supports\", \"note\": POK_MENTH1},\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II p. 269 (WLD_Bd2_pages.txt line 17690 ff.)\", \"stance\": \"supports\",\n    \"note\": \"'menth- \\\"quirlen, drehend bewegen\\\"; meth-. Ai. manthati, mathati, mathnāti \\\"quirlt, rührt, schüttelt\\\", mantha- m. \\\"Drehung, Rührlöffel\\\", av. mant- \\\"rühren\\\" (s. Bartholomae Airan. Wb. 1135); lat. (osk.) mamphur \\\"ein Stück der Drehbank\\\" ...'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, grep 'menth' / 'mandrel'\", \"stance\": \"silent\",\n    \"note\": \"Watkins has no root article for menth-1 'to stir' (his mendh-2 covers only 'to chew'), and no root entry mentioning mandrel; grep -n -i 'mandrel|mandril' AHD_watkins1985.txt returns nothing. Nourai's AHD:793 must therefore be the main-dictionary page for the word mandrel, not an appendix root.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, grep 'menth' in IEC.txt\", \"stance\": \"silent\", \"note\": \"no headword found in this OCR.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet leaf 697 s.v. mamphur\", \"stance\": \"partial\",\n    \"note\": \"They give the word and the Oscan hypothesis but attach it to no IE root: 'Terme technique, sans doute dialectal ... Mamphur lui-même est peut-être une corruption d'une forme osque *mamphar, *manfar' (see node #4).\"},\n ],\n \"nodes\": []\n}\n\ne1[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan\",\n \"words\": \"mant 1; mant 2, vant\",\n \"verdict\": \"disputed\",\n \"derivation\": (\"The two words in this box have to be judged separately. (a) 'mant 1: to stir, turn' is \"\n   \"confirmed: Bartholomae's Altiranisches Wörterbuch has 'j. mant- V. \\\"rühren\\\"; nur mit Praev. Praes. 12b \"\n   \"manā-; j-Aor. 1 maṇt-', i.e. a Young Avestan verb 'to stir', attested only with preverbs — exactly the \"\n   \"form Pokorny cites on p. 732 ('Avestan mant- \\\"bestir\\\"') and the Iranian match of Skt. manthati. \"\n   \"(b) 'mant 2, vant: in control, owner' is disputed, and this is the substantive error of the entry. \"\n   \"Avestan -mant- / -vant- is not a verb at all but the inherited SECONDARY POSSESSIVE SUFFIX: Jackson's \"\n   \"Avesta Grammar §851 'Av. -mant = Skt. -mant ... The secondary suffix -mant, like -vant below, is used in \"\n   \"making a number of possessive adjectives from noun-stems', with xratu-maṇt- 'having wisdom' = Skt. \"\n   \"kratumant-, gao-maṇt- 'having milk' = Skt. gomant-, ama-vaṇt- 'strong' = Skt. ámavant-. Its ancestor is \"\n   \"PIE *-ment-/*-uent- (the -mant- allomorph appearing after u- and labial stems), which is a suffix of \"\n   \"possession, not a reflex of the verbal root *menth₂- 'to stir'. Nourai's own NOTE in the box concedes \"\n   \"that the link is 'unclear unless \\\"stir\\\" means \\\"to be in control\\\"' — and modern scholarship takes the \"\n   \"other side: there is no link, and the whole -mand branch is filed under the wrong root.\"),\n \"derivation_fa\": (\"دو واژهٔ این جعبه را باید جدا سنجید. الف) «mant 1: هم زدن، چرخاندن» تأیید می‌شود: \"\n   \"بارتولومه در «فرهنگ ایرانی باستان» می‌آورد «j. mant- ریشهٔ فعلی «جنباندن»؛ تنها با پیشوند؛ حالِ manā-؛ \"\n   \"ماضیِ سادهٔ maṇt-»، یعنی همان صورتی که پوکورنی در ص ۷۳۲ نقل کرده و برابرِ ایرانیِ manthati سنسکریت است. \"\n   \"ب) «mant 2, vant: دارنده، صاحب» پذیرفتنی نیست و همین خطای اصلیِ این مدخل است. ‑mant-/‑vant- در اوستایی \"\n   \"به‌هیچ‌روی فعل نیست، بلکه پسوندِ دارندگیِ ثانویِ موروثی است: جکسون در «دستور اوستا» بندِ ۸۵۱ می‌نویسد که \"\n   \"«‑maṇt اوستایی همان ‑mant سنسکریت است ... این پسوندِ ثانوی، مانندِ ‑vant، برای ساختنِ صفاتِ دارندگی از \"\n   \"ستاکِ اسمی به کار می‌رود» و نمونه‌هایی چون xratu-maṇt- «خردمند» = kratumant- و ama-vaṇt- «نیرومند» = \"\n   \"ámavant- می‌آورد. نیایِ آن *-ment-/*-uent- هندواروپایی است، پسوندی برای دارندگی، نه بازماندهٔ ریشهٔ فعلیِ \"\n   \"*menth₂- «هم زدن». خودِ نورایی هم در یادداشتِ جعبه پذیرفته که این پیوند «روشن نیست»؛ پژوهش امروزی پاسخ \"\n   \"می‌دهد که پیوندی در کار نیست و کلِ شاخهٔ «ـمند» زیرِ ریشهٔ نادرست نشسته است.\"),\n \"sources\": [W_ARJMAND],\n \"ref_check\": [\n   {\"ref\": \"POK:732\", \"status\": \"partial\", \"note\": \"Pokorny p. 732 (POK_full.txt, lemma menth-1) supports only 'Avestan mant- \\\"bestir\\\"' — i.e. Nourai's mant 1. Pokorny says nothing about a mant/vant 'owner', which is a suffix and not in his root article at all.\"},\n   {\"ref\": \"BQT:2040\", \"status\": \"partial\", \"note\": \"Borhān-e Qāṭeʿ ed. Moʿīn vol. 4 pdf p. 123 (= printed 2040), s.v. «مند»; Moʿīn's footnote 4 reads (OCR of the Latin garbled): 'در پهلوی -ōmand و نیز -mand، اوستایی -mant، پسوند دارایی و تصاحب و اصاف: هنرمند، سودمند، ارجمند، آزمند، دانشمند.' So Moʿīn does give Av. -mant- as the ancestor of -mand — but explicitly as a POSSESSIVE SUFFIX (پسوند دارایی و تصاحب), never as the verb 'to stir'. It supports Nourai's forms while contradicting his root attachment.\"},\n   {\"ref\": \"FSF:311\", \"status\": \"not_found\", \"note\": \"Noushin's Vāzhe-nāmak: grep 'مند' in FSF_pages.txt finds only compounds in running text (کمند، خردمند، ارجمند، سودمند...) and no suffix article; the scan's printing/offset could not be pinned down, so printed p. 311 could not be located.\"},\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Bartholomae, Altiranisches Wörterbuch col. 1135 (BRT.txt line 19852)\", \"stance\": \"supports\",\n    \"note\": \"'j. mant- V. \\\"rühren\\\"; nur mit Praev. Praes. 12b manā-; j-Aor. 1 maṇt-.' — confirms the verb mant- 'to stir' (Nourai's mant 1), and confirms Walde-Pokorny's citation 'av. mant- \\\"rühren\\\" (s. Bartholomae Airan. Wb. 1135)'.\"},\n   {\"src\": \"AVG\", \"where\": \"Jackson, Avesta Grammar §851 and §852 (AVG.txt lines 4756-4780)\", \"stance\": \"contradicts\",\n    \"note\": \"'24. Av. -maṇt = Skt. -mant (Whitney, §1235). §851. The secondary suffix -maṇt, like -vant below, is used in making a number of possessive adjectives from noun-stems ... Av. xratu-maṇt- \\\"having wisdom\\\" = Skt. kratumant-; Av. gao-maṇt- \\\"having milk, flesh\\\" = Skt. gomant- ... Av. ama-vaṇt- adj. \\\"strong\\\" = Skt. ámavant-'. This is a derivational suffix, not the verb mant- 'to stir'.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II s.v. astōmand (NYB_vol2_glossary.txt line 718)\", \"stance\": \"contradicts\",\n    \"note\": \"'astōmand [ʾstʾwmnd] corporeal, material ... From ast; Paz. astūmand ... cf MPrs ʾstwnd, ʾstwnd (A-H I) Av. (215 sq.) astvant-.' — the MP -ōmand of astōmand is equated with Av. -vant-, not with any verb 'stir'.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary s.v. zōr (PHD.txt leaf 680)\", \"stance\": \"partial\",\n    \"note\": \"'zōr ... ~ig, ~ōmand [-yk!, -wmnd | M -mnd, N -mand] powerful, strong' — records the MP suffix pair -ōmand / -mand continued by NP -mand, with no etymology given.\"},\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Pahlavi\",\n \"words\": \"mand, omand\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"The Pahlavi forms are exactly right and the step from Avestan is regular. Middle Persian has \"\n   \"the pair -mand / -ōmand (Book Pahlavi -mnd, -ʾwmnd; Manichaean -mnd), MacKenzie s.v. zōr: 'zōr ... ~ig, \"\n   \"~ōmand [-yk!, -wmnd | M -mnd, N -mand] powerful, strong'; likewise bīm-ōmand 'fearful', astō-mand \"\n   \"'corporeal', arž-ōmand 'worthy', bahr-ōmand 'prosperous'. The longer -ōmand arose where Old Iranian \"\n   \"*-a-vant- attached to a stem in a consonant or in -ah-: intervocalic *-v- was lost and the resulting \"\n   \"*-a-ant- contracted to -ōmand (Nyberg equates MP astōmand directly with Av. astvant-); the shorter -mand \"\n   \"generalised from u- and labial stems where Avestan already had the -mant- allomorph (xratu-maṇt-). \"\n   \"Nourai's gloss 'owner, with, like' is also accurate — the suffix is possessive, and Jackson §852 note 2 \"\n   \"records the 'like to, resembling' use (Av. ma-vaṇt- 'like me'). The verdict is 'plausible' rather than \"\n   \"'confirmed' only because the arrow inherits the wrong ancestry from node #1: the true parent is the \"\n   \"possessive suffix -mant-/-vant-, not the verb mant- 'to stir'.\"),\n \"derivation_fa\": (\"صورت‌های پهلوی درست‌اند و گذارِ آن‌ها از اوستایی قاعده‌مند است. فارسیِ میانه جفتِ \"\n   \"‑mand/‑ōmand را دارد (پهلویِ کتابی ‑mnd و ‑ʾwmnd، مانویِ ‑mnd)؛ مکنزی ذیلِ zōr می‌آورد: «zōr ... ‑ōmand، \"\n   \"نیرومند»، و همچنین bīm-ōmand «ترسناک»، astō-mand «مادی، جسمانی»، arž-ōmand «ارجمند»، bahr-ōmand \"\n   \"«بهره‌مند». صورتِ بلندترِ ‑ōmand آنجا پدید آمده که *-a-vant- ایرانیِ باستان به ستاکی مختوم به همخوان یا به \"\n   \"‑ah- می‌پیوست: v میان‌واکه‌ای افتاده و *-a-ant- در هم فشرده شده و ‑ōmand داده است (نیبرگ astōmand پهلوی را \"\n   \"بی‌واسطه برابرِ astvant- اوستایی می‌نهد)؛ صورتِ کوتاهِ ‑mand نیز از ستاک‌های مختوم به u و لبی — که در \"\n   \"اوستایی هم گونهٔ ‑mant- داشتند، مانندِ xratu-maṇt- — تعمیم یافته است. معنایی هم که نورایی می‌دهد («دارنده، \"\n   \"با، مانندِ») درست است، چون جکسون در بندِ ۸۵۲ کاربردِ «مانندِ» را هم ثبت کرده (ma-vaṇt- «مانندِ من»). حکم \"\n   \"«با احتیاط پذیرفتنی» است، زیرا خودِ این پیکان درست است ولی نیایِ نادرستِ گرهِ پیشین را به ارث می‌برد.\"),\n \"sources\": [W_ARJMAND],\n \"ref_check\": [\n   {\"ref\": \"BQT:2040\", \"status\": \"supports\", \"note\": \"Borhān-e Qāṭeʿ ed. Moʿīn vol. 4 pdf p. 123 (= printed 2040), footnote 4 to «مند»: 'در پهلوی [‑ōmand] و نیز [‑mand]، اوستایی [‑mant]، پسوند دارایی و تصاحب و اصاف: هنرمند، سودمند، ارجمند، آزمند، دانشمند' — gives precisely the Pahlavi pair -ōmand / -mand that Nourai's box shows, with Avestan -mant- as their source.\"},\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, s.v. zōr, bīm, astōmand, abzār, brinōmand (PHD.txt leaves 170, 219, 256, 292, 680)\", \"stance\": \"supports\",\n    \"note\": \"'zōr ... ~ōmand [-wmnd | M -mnd, N -mand] powerful, strong'; 'bim ... --ōmand [-ʾwmnd] fearful'; 'astōmand [ʾstʾwmnd] corporeal, material'; 'abzār ... ūmand [-wmnd] skilled, able'; 'brinōmand [blynʾwmnd] delimited' — the suffix in both shapes, with NP -mand named as its continuation.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. aržōmand, astōmand, akōmandīhā, bahrōmandēh (NYB_vol2_glossary.txt lines 364, 559, 674, 718, 897)\", \"stance\": \"supports\",\n    \"note\": \"'aržōmand [ʾrǰʾwmnd] worthy, dignified ... Paz. arzmand (Mx), arzamand (SGV); NP arjmand'; 'astōmand ... Av. (215 sq.) astvant-'; 'apazarōmand [~-ʾwmnd] endowed with spiritual forces'. Nyberg both documents the MP suffix and anchors it in Av. -vant-.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, grep '-mand|omand' in HRN.txt\", \"stance\": \"silent\",\n    \"note\": \"Horn's Grundriss is arranged by lexical headwords and has no article for the suffix; nothing recorded.\"},\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Persian\",\n \"words\": \"mand\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"The Pahlavi → New Persian step and the description of the suffix are both correct. MP -mand / \"\n   \"-ōmand > NP ـمند -mand, a fully productive denominal suffix of possession: ارجمند arjmand 'of worth', \"\n   \"دانشمند dānešmand 'possessed of knowledge, scholar', هنرمند honarmand 'possessed of art, artist', \"\n   \"نیازمند niyāzmand 'in need'. The older -ōmand survives in the classical doublets Nourai prints on the \"\n   \"second line — دانشومند، برومند، خردومند، نیازومند — which are the direct continuations of MP dānišn-ōmand, \"\n   \"bar-ōmand, xrad-ōmand, niyāz-ōmand, and are still metrically required in early poetry, as in his \"\n   \"Manūčehrī line 'من نیازومند تو گشتم و هرکو شد چنین...'; the shorter -mand then generalised, with the \"\n   \"unstressed ō of the older form lost. Borhān-e Qāṭeʿ describes the suffix in these very terms ('خداوند \"\n   \"باشد و چون در آخر کلمات آید ... همچو دولتمند یعنی صاحب دولت'). Nourai's gloss '(suffix) owner of, with' \"\n   \"is thus exact. (The branch as a whole is nevertheless filed under the wrong PIE root: see node #1.)\"),\n \"derivation_fa\": (\"گذارِ پهلوی به فارسیِ نو و توصیفی که نورایی از این پسوند می‌دهد هر دو درست است: ‑mand و \"\n   \"‑ōmand فارسیِ میانه به «ـمند» فارسیِ نو رسیده است، پسوندی زایا برای ساختِ صفتِ دارندگی از اسم: ارجمند، \"\n   \"دانشمند، هنرمند، نیازمند. صورتِ کهن‌ترِ ‑ōmand در دوگانه‌های کلاسیکی که نورایی در سطر دومِ جعبه آورده \"\n   \"(دانشومند، برومند، خردومند، نیازومند) بازمانده است؛ این‌ها ادامهٔ مستقیمِ dānišn-ōmand و bar-ōmand و \"\n   \"xrad-ōmand و niyāz-ōmand پهلوی‌اند و در شعرِ کهن هنوز وزن آن‌ها را می‌طلبد، چنانکه در بیتِ منوچهریِ خودِ \"\n   \"کتاب: «من نیازومند تو گشتم و هرکو شد چنین...». سپس صورتِ کوتاهِ ‑mand با افتادنِ ōِ بی‌تکیه تعمیم یافته \"\n   \"است. برهانِ قاطع همین را می‌گوید: «خداوند باشد و چون در آخر کلمات آید ... همچو دولتمند یعنی صاحب دولت». \"\n   \"پس ادعای نورایی در این گره درست است — هرچند کلِ این شاخه، چنانکه در گرهِ ۱ گفته شد، زیر ریشهٔ نادرست \"\n   \"نشسته است.\"),\n \"sources\": [W_ARJMAND],\n \"ref_check\": [\n   {\"ref\": \"BQT:2040\", \"status\": \"supports\", \"note\": \"Vol. 4 pdf p. 123 (= printed 2040), headword «مند»: '... خداوند باشد و چون در آخر کلمات آید ... همچو دولتمند یعنی صاحب دولت و ارجمند یعنی صاحب قدر و قیمت و حاجتمند و دردمند هم ازین قبیل است بمعنی صاحب درد و غمناک' — i.e. exactly Nourai's '(suffix) owner of, with'; footnote 4 adds Pahlavi -ōmand/-mand, Avestan -mant- and the examples هنرمند، سودمند، ارجمند، آزمند، دانشمند, four of which are in Nourai's own list.\"},\n   {\"ref\": \"FSF:311\", \"status\": \"not_found\", \"note\": \"Noushin's Vāzhe-nāmak: grep 'مند' in FSF_pages.txt yields no suffix article (only compounds in running text, e.g. line 3586 «مند» inside a column of a Shahnameh gloss); the scan's page offset could not be established, so printed p. 311 was not located.\"},\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"vol. 4 printed p. 2040 s.v. «مند» + footnote 4\", \"stance\": \"supports\", \"note\": \"quoted above.\"},\n   {\"src\": \"MON\", \"where\": \"Moʿīn / grep 'ارجمند|هنرمند|نیازومند' in MON_part1-2.txt\", \"stance\": \"partial\",\n    \"note\": \"the abridged 2-vol OCR carries the compounds but not a suffix article; no independent etymological statement recorded.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II line 674 s.v. aržōmand\", \"stance\": \"supports\",\n    \"note\": \"'aržōmand [ʾrǰʾwmnd] worthy, dignified 3111, 4715; precious, excellent, comp. ~-tar 879. — Paz. arzmand (Mx), arzamand (SGV); NP arjmand.' — the MP → NP step for one of Nourai's own examples, and the -ōmand ~ -mand doublet.\"},\n   {\"src\": \"GPL\", \"where\": \"Platts & Ranking, Grammar of the Persian Language (grep '-mand' in GPL.txt)\", \"stance\": \"silent\",\n    \"note\": \"no line recovered from this OCR for the suffix; nothing recorded.\"},\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Latin\",\n \"words\": \"manphur, manfur\",\n \"verdict\": \"transcription_suspect\",\n \"derivation\": (\"The word exists but its first spelling does not. The Latin gloss-word is mamphur, preserved \"\n   \"by Paulus-Festus 117,3: 'mamphur appellatur loro circumuolutum mediocris longitudinis lignum rotundum, \"\n   \"quod circumagunt fabri in operibus tornandis' — 'a round piece of wood of moderate length, wrapped with \"\n   \"a strap, which craftsmen spin round in lathe-work', i.e. precisely Nourai's 'lathe, a lathed object'. \"\n   \"Pokorny p. 732 cites it as 'lat. (osk.) mamphur, besser manfur \\\"ein Stück der Drehbank\\\"' and \"\n   \"Walde-Pokorny II 269 the same, with Meyer-Lübke's view that manfur is the better form 'nach Ausweis der \"\n   \"heutigen Dialekte'. So Nourai's second form manfur is right, but the first should be mamphur with -m-; \"\n   \"the printed page (pdf 334, book 304) really does read 'manphur, manfur', so this is the author's own \"\n   \"misprint (an assimilated *manphur for mamphur) and the JSON extraction is faithful. A second, \"\n   \"independent caveat: Ernout-Meillet attach the word to no IE root at all, calling it 'terme technique, \"\n   \"sans doute dialectal' and 'peut-être une corruption d'une forme osque *mamphar, *manfar' — so the arrow \"\n   \"from *menth₂- is Pokorny's opinion, not a consensus.\"),\n \"derivation_fa\": (\"واژه هست، اما املای نخستِ آن نیست. واژهٔ لاتین mamphur است که پاؤلوس‑فستوس (۱۱۷٬۳) نگه \"\n   \"داشته: «mamphur آن چوبِ گردِ میان‌اندازه‌ای را گویند که با چرمی پیچیده شده و صنعتگران در کارِ خراطی آن را \"\n   \"می‌گردانند» — یعنی درست همان «چرخِ خراطی و شیءِ خراطی‌شده»ای که نورایی معنا کرده. پوکورنی در ص ۷۳۲ آن را \"\n   \"«lat. (osk.) mamphur, besser manfur» می‌آورد و والده‑پوکورنی نیز همان، با نقلِ رأیِ مایر‑لوبکه که manfur \"\n   \"بر پایهٔ گویش‌های امروزی صورتِ بهتری است. پس صورتِ دومِ نورایی درست است ولی صورتِ نخست باید mamphur با م \"\n   \"باشد. تصویرِ صفحهٔ چاپی (صفحهٔ ۳۳۴ پی‌دی‌اف، ۳۰۴ کتاب) به‌روشنی «manphur, manfur» دارد؛ پس این خطای چاپیِ \"\n   \"خودِ کتاب است (همگونیِ mamphur به manphur) و خوانشِ اسکن درست بوده. نکتهٔ دومِ مستقل: ارنو و مییه این واژه \"\n   \"را به هیچ ریشهٔ هندواروپایی نمی‌بندند و آن را «اصطلاحی فنی و به‌احتمال گویشی» و «شاید تحریفِ صورتی اسکی» \"\n   \"می‌خوانند؛ پس پیکانِ آمده از *menth₂- رأیِ پوکورنی است، نه اجماع.\"),\n \"error_in\": \"book\",\n \"book_prints\": \"manphur, manfur\",\n \"correct_form\": \"mamphur, manfur\",\n \"sources\": [W_MANDO],\n \"ref_check\": [\n   {\"ref\": \"POK:732\", \"status\": \"partial\", \"note\": \"POK_full.txt s.v. menth-1 (p. 732): 'Latin (Oscan) mamphur, better manfur \\\"ein Stuck der Drehbank\\\"'. Supports the derivation and the second form, but spells the first mamphur, not manphur.\"},\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II p. 269 (WLD_Bd2_pages.txt lines 17697-17701)\", \"stance\": \"partial\",\n    \"note\": \"'lat. (osk.) mamphur \\\"ein Stück der Drehbank\\\", nach Meyer-Lübke Phil. Abhdlgn. Schweizer-Sidler gewidmet 24 ff., EWb. 383 vielmehr manfar nach Ausweis der heutigen Dialekte, die daneben auch ein echt lat. *mandar voraussetzen (a und Dental wie bei mando \\\"kaue\\\" zu menth \\\"kauen\\\")' — mamphur again, and the Romance-based *mandar that node #5 needs.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, leaf 697 s.v. mamphur (LAT.txt line 36041)\", \"stance\": \"partial\",\n    \"note\": \"'mamphur: appellatur loro circumuolutum mediocris longitudinis lignum rotundum, quod circumagunt fabri in operibus tornandis, P.F. 117,3. Terme technique, sans doute dialectal, auquel devait correspondre une forme latine *mandar que supposent certains dérivés romans. Mamphur lui-même est peut-être une corruption d'une forme osque *mamphar, *manfar, cf. Ernout, m. dial., et M.L. 5378.' — confirms the meaning exactly, confirms the spelling mamphur, and gives no IE root.\"},\n   {\"src\": \"LEW\", \"where\": \"Walde 1910, grep 'mamphur|manfur' in LEW_1910.txt\", \"stance\": \"silent\",\n    \"note\": \"no hit in this OCR of the 2nd edition.\"},\n   {\"src\": \"BOOK\", \"where\": \"printed page image data/verification/sources/refs/ocr/BOOK/334.png (pdftoppm of pdf p. 334)\", \"stance\": \"partial\",\n    \"note\": \"the Latin box on the printed page reads verbatim 'manphur, manfur : lathe, a lathed object' — so the extraction is faithful and the odd form is Nourai's.\"},\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 5, \"lang\": \"French\",\n \"words\": \"mandrin\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"French mandrin 'mandrel, the spindle or chuck of a lathe' is a real word with the right \"\n   \"meaning, and the arrow from the Latin gloss-word is a real scholarly proposal — Meyer-Lübke's (REW 5378), \"\n   \"which Ernout-Meillet report: the modern Romance forms presuppose not mamphur itself but a Latin *mandar, \"\n   \"and mamphur is taken to be a corruption of an Oscan *mamphar/*manfar. AHD's 1976 word-entry (Nourai's \"\n   \"AHD:793) followed exactly that reconstruction. But it is only a hypothesis: Etymonline reports French \"\n   \"mandrin as 'itself of unknown origin', and no reflex of mamphur is attested between Paulus-Festus and \"\n   \"16th-century French. Hence 'plausible' — the etymology is Nourai's source's, not a modern consensus.\"),\n \"derivation_fa\": (\"mandrin فرانسوی «مغزی/سه‌نظامِ ماشینِ تراش» واژه‌ای واقعی با همان معناست، و پیکانی که \"\n   \"نورایی از واژهٔ لاتین به آن می‌کشد پیشنهادی پژوهشی است — رأیِ مایر‑لوبکه (REW ۵۳۷۸) که ارنو و مییه نقل \"\n   \"می‌کنند: صورت‌های رومانسِ امروزی نه خودِ mamphur بلکه صورتی لاتین *mandar را پیش‌فرض می‌گیرند و mamphur \"\n   \"خود تحریفِ *mamphar/*manfarِ اسکی دانسته شده است. مدخلِ واژه‌نامهٔ AHD (۱۹۷۶) که نورایی به آن ارجاع \"\n   \"می‌دهد (ص ۷۹۳) همین بازسازی را آورده بود. اما این تنها فرض است: «ریشه‌شناسی آنلاین» mandrin فرانسوی را \"\n   \"«خود ناشناخته‌ریشه» می‌خواند و میانِ پاؤلوس‑فستوس و فرانسویِ سدهٔ شانزدهم هیچ بازماندهٔ ضبط‌شده‌ای از \"\n   \"mamphur نیست. پس: با احتیاط پذیرفتنی است.\"),\n \"sources\": [E_MANDREL],\n \"ref_check\": [\n   {\"ref\": \"AHD:793\", \"status\": \"not_checked\", \"note\": \"Nourai's page 793 belongs to the main A-Z text of the 1975/76 New College Edition (the IE appendix is pp. 1505-1550), and that edition is lending-only on archive.org; the 1985 Watkins root book has no article for this word at all (grep -n -i 'mandrel|mandril' AHD_watkins1985.txt → nothing). The etymology AHD gave in that era (French mandrin < Latin mamphur 'bow-drill') is the one reproduced by Nourai and is the Meyer-Lübke reconstruction reported by Ernout-Meillet.\"},\n ],\n \"consulted\": [\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet leaf 697 s.v. mamphur\", \"stance\": \"partial\",\n    \"note\": \"'... auquel devait correspondre une forme latine *mandar que supposent certains dérivés romans ... cf. M.L. 5378' — i.e. Meyer-Lübke's Romance etymology, the basis of the French link, but through *mandar rather than mamphur directly.\"},\n   {\"src\": \"Etymonline\", \"where\": E_MANDREL, \"stance\": \"contradicts\",\n    \"note\": \"'perhaps borrowed from French mandrin, itself of unknown origin' — Etymonline declines the Latin connection.\"},\n   {\"src\": \"PHN\", \"where\": \"Pihan, grep 'mandrin' in PHN.txt\", \"stance\": \"silent\",\n    \"note\": \"no hit — Pihan covers French words of Arabic/Persian/Turkish origin, and mandrin is not claimed to be one.\"},\n   {\"src\": \"DEV\", \"where\": \"Devic, grep 'mandrin' in DEV.txt\", \"stance\": \"silent\", \"note\": \"no hit.\"},\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 6, \"lang\": \"English\",\n \"words\": \"mandrel, mandril\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"English mandrel (also spelt mandril) is first recorded in the 1510s in the quite different \"\n   \"sense 'miner's pick', and only from the 1680s in the sense drawn here, 'a bar or spindle used chiefly to \"\n   \"hold articles in place, on a lathe or a circular saw'. The French source is probable but not proven: \"\n   \"Etymonline gives 'origin unknown ... perhaps borrowed from French mandrin, itself of unknown origin', the \"\n   \"-in > -el ending being reshaped on the English agent/instrument pattern (cf. barrel, kernel). The spelling \"\n   \"mandril, which Nourai lists as a variant, is a genuine 18th-19th-c. by-form (not to be confused with the \"\n   \"monkey mandrill). So the last step of the chart is right in outline, and 'plausible' because both this \"\n   \"step and the previous one rest on a probability rather than an attested series.\"),\n \"derivation_fa\": (\"mandrel انگلیسی (با گونهٔ نگارشیِ mandril) نخست در دههٔ ۱۵۱۰ و در معنایی دیگر — «کلنگِ \"\n   \"معدنچی» — ثبت شده و تنها از دههٔ ۱۶۸۰ به معنایی که در این نمودار آمده، یعنی «میله یا مغزی که کار را بر \"\n   \"ماشینِ تراش یا ارهٔ گرد نگه می‌دارد»، به کار رفته است. خاستگاهِ فرانسوی محتمل است اما اثبات‌شده نیست: \"\n   \"«ریشه‌شناسی آنلاین» می‌نویسد «ریشه ناشناخته ... شاید وام از mandrin فرانسوی که خود ناشناخته‌ریشه است». \"\n   \"پایانهٔ ‑in به ‑el بر قیاسِ واژه‌های ابزارِ انگلیسی (مانند barrel و kernel) بازساخته شده است. گونهٔ mandril \"\n   \"که نورایی می‌آورد صورتی راستین از سدهٔ هجدهم و نوزدهم است (و نباید با نامِ میمونِ mandrill اشتباه شود). پس \"\n   \"پلهٔ پایانیِ نمودار در کلیات درست است و حکم «با احتیاط پذیرفتنی» است، زیرا این پله و پلهٔ پیش از آن هر دو \"\n   \"بر احتمال تکیه دارند نه بر زنجیرهٔ ضبط‌شده.\"),\n \"sources\": [E_MANDREL],\n \"ref_check\": [\n   {\"ref\": \"AHD:793\", \"status\": \"not_checked\", \"note\": \"Same as node #5: p. 793 of the 1975/76 New College Edition is not openly available and the 1985 Watkins root book has no mandrel article; the citation could not be read.\"},\n ],\n \"consulted\": [\n   {\"src\": \"Etymonline\", \"where\": E_MANDREL, \"stance\": \"partial\",\n    \"note\": \"'mandrel (n.) — 1510s, \\\"miner's pick\\\", of unknown origin, perhaps borrowed from French mandrin, itself of unknown origin. From 17c. of \\\"a bar or spindle, used chiefly to hold articles in place, on a lathe or a circular saw.\\\"'\"},\n   {\"src\": \"KLN\", \"where\": \"Klein, grep 'mandrel|mandril' in KLN_1966.txt\", \"stance\": \"silent\",\n    \"note\": \"no headword recovered from this OCR.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, grep 'mandrel|mandril' in SKT.txt\", \"stance\": \"silent\", \"note\": \"no hit.\"},\n ]\n})\n\nout[\"entries\"].append(e1)\n\n# ---------------- ENTRY 2 ----------------\ne2 = {\n \"entry\": 2,\n \"root\": \"Mer 1, Smer\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *(s)mer- 'to remember, care for' (Pokorny (s)mer- 969-970; Watkins (s)mer-1 'To remember')\",\n \"note\": (\"Root, page and gloss all check out. Pokorny pp. 969-970 has 'Root / lemma: (s)mer- | Meaning: to \"\n   \"remember; to care for', opening with 'Old Indic smarati \\\"reminds sich, gedenkt\\\" ... Avestan maraiti, \"\n   \"hišmaraiti \\\"(be)merkt\\\", mimara- \\\"eingedenk\\\" ... Latin memor \\\"eingedenk\\\" ... Gothic maurnan, Old \"\n   \"English murnan, Old High German mornen \\\"care for, worry, anxiously worry about\\\"'. Watkins prints \"\n   \"'(s)mer-1. To remember. [Pok. (s)mer- 969.]' Nourai's double lemma 'Mer 1, Smer' renders Pokorny's \"\n   \"s-mobile notation, and his gloss 'to remember, be anxious about' is Klein's wording almost verbatim \"\n   \"('*(s)mer-, \\\"to care for, be anxious about, think, consider, remember\\\"', KLN p. 961 s.v. memory) — the \"\n   \"very page Nourai cites. Cheung (2007) likewise sets up Proto-Iranian *hmar 'to remember, recall; to \"\n   \"count' from 'PIE *(s)mer- ... Pok.: 969'. The two weak points on this chart are inside nodes #1/#2 \"\n   \"(vi-mar → gomārdan) and #7 (martyr), not in the root.\"),\n \"note_fa\": (\"ریشه و شمارهٔ صفحه و معنا، هر سه درست است. پوکورنی در صص ۹۶۹–۹۷۰ ریشهٔ «(s)mer-» را با معنای \"\n   \"«یاد آوردن؛ پروا داشتن» ثبت کرده و با سنسکریت smarati «به یاد می‌آورد»، اوستایی maraiti و hišmaraiti، \"\n   \"mimara- «یادآور»، لاتین memor، و گوتیک maurnan و انگلیسیِ باستان murnan آغاز می‌کند. واتکینز نیز «(s)mer-1: \"\n   \"یاد آوردن [پوکورنی ۹۶۹]» دارد. صورتِ دوگانهٔ «Mer 1, Smer» در کتابِ نورایی همان نشانه‌گذاریِ s متحرک \"\n   \"پوکورنی است، و معنایی که می‌دهد («یاد آوردن، نگران بودن») تقریباً واژه‌به‌واژه عبارتِ کلاین در ص ۹۶۱ ذیل \"\n   \"memory است — همان صفحه‌ای که نورایی به آن ارجاع می‌دهد. چونگ (۲۰۰۷) هم ریشهٔ ایرانیِ آغازینِ *hmar «یاد \"\n   \"آوردن؛ شمردن» را از همین «*(s)mer- هندواروپایی، پوکورنی ۹۶۹» می‌گیرد. دو نقطهٔ سستِ این نمودار در گره‌های \"\n   \"۱ و ۲ (vi-mar و «گماردن») و در گرهِ ۷ (martyr) است، نه در ریشه. ادعای نورایی در سطحِ ریشه درست است.\"),\n \"sources\": [W_MARTYS, W_AMAR],\n \"ref_check\": [\n   {\"ref\": \"POK:969\", \"status\": \"supports\", \"note\": POK_SMER},\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. (s)mer-1 (AHD_watkins1985.txt line ~961)\", \"stance\": \"supports\",\n    \"note\": \"'(s)mer-1. To remember. 1. Suffixed zero-grade form *mr-no- in Germanic *murnan, to remember sorrowfully, in Old English murnan, to mourn: MOURN. 2. Reduplicated form *me-mor- in: a. Germanic *mi-mer- in Old Norse Mimir ...; b. Latin memor, mindful: MEMORABLE, MEMORANDUM, MEMORY; COMMEMORATE, REMEMBER. [Pok. (s)mer- 969.]'\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 689 f. (cited by Pokorny as 'WP. II 689 f.' at the end of the (s)mer- article)\", \"stance\": \"supports\",\n    \"note\": \"Pokorny's own reference line for this root is 'WP. II 689 f., WH. II 67 f., 110', i.e. Walde-Pokorny treat the root at Bd. II pp. 689-690; the local WLD_Bd2 OCR breaks off before that range, so the cross-reference is recorded from Pokorny.\"},\n   {\"src\": \"KLN\", \"where\": \"p. 961 s.v. memory (KLN_1966.txt line 23432)\", \"stance\": \"supports\",\n    \"note\": \"'L. memoria ... fr. memor, \\\"mindful\\\", which stands for *me-mor and derives fr. I.-E. *mer-(s)mer-, reduplication of base *(s)mer-, \\\"to care for, be anxious about, think, consider, remember\\\". From the reduplicated base derive also Avestic mimara-, \\\"mindful\\\" ... The simple base *(s)mer- appears in OI. smarati, Avestic maraiti, \\\"remembers\\\" ... Goth. maurnan, OE. murnan, \\\"to be anxious for\\\" ... Cp. also martyr, mourn, smriti.'\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007, Etym. Dict. of the Iranian Verb, s.v. *hmar (CHEUNG.txt line 9698 ff.)\", \"stance\": \"supports\",\n    \"note\": \"'*hmar \\\"to remember, recall; to count\\\" ... PIE *(s)mer- \\\"to observe, consider, think of\\\" || *smer- \\\"to earn, get a share\\\" => LIV: 569 f. | Pok.: 969'; IE cognates listed include 'Gr. ἱμείρω \\\"I desire, long\\\", Goth. *maurnan, OHG mornēn, OE murnan, Engl. to mourn'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, grep 'smer' in IEC.txt\", \"stance\": \"silent\", \"note\": \"no headword recovered from this OCR.\"},\n ],\n \"nodes\": []\n}\n\ne2[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan\",\n \"words\": \"mar 1, smer; mar-aiti, hiš-mar-aiti; â-mar; vi-mar\",\n \"verdict\": \"disputed\",\n \"derivation\": (\"Three of the four items are solid, the fourth is not. (a) mar- 'to remember' with the present \"\n   \"maraiti and the reduplicated aipi-hišmarant- are attested and are Pokorny's own evidence on p. 969 \"\n   \"('Avestan maraiti, hišmaraiti \\\"(be)merkt\\\"'); Cheung s.v. *hmar lists YAv. fra.maraiti, \"\n   \"paitismaraiti/-smaromna-, aipi hismarant-, aiβi.smarata-. The initial š of hiš-mar- is the ruki-product \"\n   \"of *s after the preverb *abi-/*ni-/*pati-, so hiš-mar- and smar- are the same stem; Nourai's 'smer' next \"\n   \"to 'mar 1' is not a separate Avestan word but the PIE s-mobile shape (Skt. smarati) — harmless as \"\n   \"notation. (b) ā-mar- '(to count) to remember' is right: Nyberg derives MP amar/āmār- 'From Av. (1142 sq.) \"\n   \"ā-mar-, originally ā-hmar-'. (c) vi-mar 'designate (off)' is where the chart goes wrong. No Avestan \"\n   \"vi-mar- with that sense is attested; the form is a reconstructed Old Persian *vi-mar- invented to explain \"\n   \"NP gumārdan, and Horn, who proposed it (Grundriss no. 931, p. 208), already labelled it 'Unsicher'. \"\n   \"Hübschmann rejected it outright (p. 95, no. 931: gumāštan/gumārdan/gumārtan 'zeigt nirgends den Anlaut v- \"\n   \"und hat jedenfalls mit ap. *vi-mar = skr. vi-smar nichts zu thun'), and Cheung 2007 assigns MP gumār-/NP \"\n   \"gumāštan to a different root altogether, *ui- + *marH 'to block, hinder' (PIE *merH-, Pok. 970), with the \"\n   \"original sense *'to unblock' > 'to let go, allow, appoint'. Because of that item the node as a whole is \"\n   \"disputed.\"),\n \"derivation_fa\": (\"سه قلم از چهار قلمِ این جعبه استوار است و چهارمی نه. الف) ریشهٔ mar- «یاد آوردن» با حالِ \"\n   \"maraiti و صورتِ مضاعفِ aipi-hišmarant- ضبط شده و همان گواهی است که پوکورنی در ص ۹۶۹ می‌آورد؛ چونگ نیز ذیل \"\n   \"*hmar صورت‌های fra.maraiti و paiti-smaromna- و aiβi.smarata- را فهرست می‌کند. šِ آغازینِ hiš-mar- زادهٔ \"\n   \"قاعدهٔ «روکی» است، یعنی s پس از پیشوندِ *abi-/*ni-/*pati- به š بدل شده؛ پس hiš-mar- و smar- یک ستاک‌اند و \"\n   \"«smer»ی که نورایی کنارِ «mar 1» نهاده واژهٔ جداگانهٔ اوستایی نیست، بلکه صورتِ sِ متحرکِ هندواروپایی است \"\n   \"(همانندِ smarati سنسکریت) — که به‌عنوان نشانه‌گذاری بی‌اشکال است. ب) ā-mar- «شمردن/به یاد آوردن» درست \"\n   \"است؛ نیبرگ amar/āmār- پهلوی را «از اوستایی ā-mar-، در اصل ā-hmar-» می‌گیرد. پ) اما «vi-mar: گماشتن» جای \"\n   \"خطاست. هیچ vi-mar- اوستایی با این معنا ضبط نشده؛ این صورت *vi-mar-ی بازسازی‌شده در پارسیِ باستان است که \"\n   \"برای توضیحِ «گماردن» ساخته‌اند، و خودِ هرن که آن را پیش نهاد (شمارهٔ ۹۳۱، ص ۲۰۸) آن را «نامطمئن» خواند. \"\n   \"هوبشمان یکسره ردش کرد (ص ۹۵، شمارهٔ ۹۳۱: «هیچ‌جا vِ آغازین نشان نمی‌دهد و به‌هرحال با *vi-mar پارسی باستان \"\n   \"= vi-smar سنسکریت هیچ ربطی ندارد») و چونگ (۲۰۰۷) gumār- پهلوی و «گماشتن» فارسی را به ریشهٔ دیگری می‌بندد: \"\n   \"*ui- + *marH «بستن، بازداشتن» با معنای آغازینِ «باز کردن» ← «رها کردن، اجازه دادن، گماشتن». به سببِ همین \"\n   \"قلم، حکمِ کلِ گره «رد‌شده» است.\"),\n \"sources\": [W_AMAR],\n \"ref_check\": [\n   {\"ref\": \"MON\", \"status\": \"not_checked\", \"note\": \"Cited without a page number; Moʿīn's 6-vol pagination cannot be mapped online and the local OCR is of the 2-vol abridgement, so no specific place could be checked for the Avestan forms.\"},\n   {\"ref\": \"KLN:961\", \"status\": \"supports\", \"note\": \"Klein p. 961 s.v. memory (KLN_1966.txt line 23432, between the printed page markers 958 and 966): 'The simple base *(s)mer- appears in OI. smarati, Avestic maraiti, \\\"remembers\\\" ...' and 'From the reduplicated base derive also Avestic mimara-, \\\"mindful\\\"'. Supports mar- / maraiti; says nothing about vi-mar.\"},\n   {\"ref\": \"FFD:64\", \"status\": \"not_found\", \"note\": \"Abolghasemi, Feʿl-hā-ye Fārsi-ye Dari: FFD_pages.txt pdf p. 70 (= printed 64-65 by the recorded offset) contains the articles شیفتن، فراموشیدن، فرجامیدن، فرستادن — no mar-/āmār article. The verbs شمردن and گماردن are elsewhere in the book (alphabetically under ش and گ), so this page number does not correspond to the claim.\"},\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Bartholomae, Altiranisches Wörterbuch cols. 1142 f. (referenced by Nyberg s.v. amar and ōšmurtan)\", \"stance\": \"supports\",\n    \"note\": \"Nyberg cites 'Av. (1142 sq.) ā-mar-, originally ā-hmar-' and 'aviš + Av. (1142) ?mar-, orig. *hmar-, Skr smar-' — i.e. Bartholomae's article for the root stands at AiW 1142 f. and gives ā-mar- and hmar-. Bartholomae has no vi-mar-.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 s.v. *hmar (CHEUNG.txt line 9698 ff.) and s.v. *marH 'to block, hinder' (line 17711 ff.)\", \"stance\": \"partial\",\n    \"note\": \"s.v. *hmar: 'AVESTAN: (š)mar- \\\"to remember, recall\\\" ... red. YAv. aipi hismarant- (Yt 10.45), perf. pass. YAv. aiβi.smarata- (Yt 14.34)'. But s.v. *marH: '(+ *ui-) MMP gwmʾr- \\\"to appoint\\\", BMP gwmʾl- /gumār-/ \\\"to appoint, entrust, commission\\\" ... NP gumāštan/gumār- ... PIE *merH- \\\"to hinder, block\\\" | Pok.: 970' — so Cheung supports mar-/hišmar- and contradicts vi-mar → gumārdan.\"},\n   {\"src\": \"AVG\", \"where\": \"Jackson, Avesta Grammar (grep 'mar-' / 'smar')\", \"stance\": \"silent\",\n    \"note\": \"Jackson's grammar cites no form of this root in the passages recovered; nothing recorded either way.\"},\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien no. 791, printed p. 80-81 (HUB.txt leaf 90)\", \"stance\": \"supports\",\n    \"note\": \"'791. Dazu afgh. LW. sumar \\\"counting, numbering, number\\\", šmerǝl \\\"to count\\\", kurd. ižmar \\\"Zahl\\\" = hišmar ... Wegen des anlaut. š für s vgl. zd. hišmarǝntō, aiwi-smarǝtǝm, paiti-smarǝmna' — confirms the Avestan hiš-mar-/aiwi-smar- forms Nourai lists.\"},\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\",\n \"words\": \"mar; âmâr; šemordan; gomârdan\",\n \"verdict\": \"disputed\",\n \"derivation\": (\"Three of the four Persian words descend from this root; the fourth almost certainly does not. \"\n   \"(1) مَر mar 'count, number, reckoning' — Borhān-e Qāṭeʿ printed p. 1978 s.v. «مر»: 'و بمعنی شمار هم هست', \"\n   \"with Jāmī's 'مر بود پنجاه و چون آمد دو مر' and a footnote explaining it as the weavers' counting unit. It \"\n   \"continues MP mar (BMP ml /mar/ 'calculation, number, account', Cheung; MacKenzie 'amar [ml] reckoning, \"\n   \"consideration'), from *(h)mar-. (2) آمار āmār 'reckoning; (modern) statistics' < MP āmār- 'to reckon, \"\n   \"calculate' (MacKenzie 'āmār- [ʾmʾl-] reckon, calculate; ~išn reckoning; āmārgar reckoner'), Nyberg: \"\n   \"'amar ... Paz. NP āmār. From Av. ā-mar-, originally ā-hmar-; Arm. lw. hamar' — a pure Old Iranian \"\n   \"compound ā- + *hmar-. (3) شمردن šomordan/šemordan 'to count' (with شمار، شمارش، شماره) < MP ōšmurdan / \"\n   \"ōšmār- (BMP ʾwsmwl-, ʾwsmʾl-) < *aviš-hmar- (Nyberg, s.v. ōšmurtan); the initial š- is the ruki reflex of \"\n   \"*s after the preverb, so Persian š-, not the s of smar-. Note that Hübschmann p. 80 f. denies specifically \"\n   \"that šumurdan goes back to Av. aiwi-smar-, but Cheung lists 'NP šumurdan/šumār-' under *hmar (with prefix) \"\n   \"— the root is not in doubt, only the exact preverb. (4) گماردن gomārdan (گماشتن، گماشته) 'to appoint, \"\n   \"designate' does NOT belong here. Hübschmann p. 95 — the very page Nourai cites — says the opposite: 'Np. \"\n   \"gumāštan = pāz. gumārdan = phl. gumārtan \\\"einsetzen, bestimmen, beauftragen, betrauen\\\" ... zeigt \"\n   \"nirgends den Anlaut v- und hat jedenfalls mit ap. *vi-mar = skr. vi-smar nichts zu thun.' Cheung 2007 \"\n   \"assigns it to *ui- + *marH 'to block, hinder' (Skt. mar- 'to hinder', Lat. mora 'delay'), original sense \"\n   \"*'unblock' > 'let go, allow, entrust, appoint'. Moʿīn's own footnote in Borhān (printed p. ~1834, vol. 3 \"\n   \"pdf p. 631) gives only 'پهلوی gumārtan (از: گمار + پسوند مصدری) ... ارمنی gumar-el' and refers to \"\n   \"Hübschmann §931, i.e. to the rejection. The node therefore counts as disputed.\"),\n \"derivation_fa\": (\"سه واژه از چهار واژهٔ این جعبه به‌راستی از این ریشه‌اند و چهارمی به‌احتمالِ نزدیک به یقین \"\n   \"نه. ۱) «مَر» به معنای شمار و عدد: برهانِ قاطع در ص ۱۹۷۸ ذیلِ «مر» می‌آورد «و بمعنی شمار هم هست» و بیتِ \"\n   \"جامی «مر بود پنجاه و چون آمد دو مر» را گواه می‌گیرد و در حاشیه آن را واحدِ شمارشِ جولاهان می‌خواند؛ این \"\n   \"واژه ادامهٔ mar فارسیِ میانه است (چونگ: BMP ml «شمار، حساب»؛ مکنزی: amar «شمار، ملاحظه») از *(h)mar-. \"\n   \"۲) «آمار» از āmār- فارسیِ میانه «شمردن، حساب کردن» (مکنزی: āmār-، āmārišn، āmārgar)؛ نیبرگ می‌نویسد \"\n   \"«amar ... در پازند و فارسیِ نو āmār؛ از اوستایی ā-mar- که در اصل ā-hmar- بوده؛ وام‌واژهٔ ارمنی hamar» — \"\n   \"یعنی ترکیبی سراسر ایرانیِ باستان از پیشوندِ ā- و ریشهٔ *hmar-. ۳) «شمردن» (با شمار، شمارش، شماره) از \"\n   \"ōšmurdan/ōšmār- فارسیِ میانه از *aviš-hmar-؛ šِ آغازین بازتابِ قاعدهٔ «روکی» است، یعنی s پس از پیشوند به \"\n   \"š بدل شده. هوبشمان (ص ۸۰ به بعد) می‌گوید «شمردن» به aiwi-smar اوستایی برنمی‌گردد، اما چونگ آن را با پیشوند \"\n   \"ذیلِ همان *hmar می‌آورد؛ پس ریشه محلِ تردید نیست، تنها پیشوندِ دقیق. ۴) «گماردن/گماشتن/گماشته» به این \"\n   \"خانواده تعلق ندارد. هوبشمان در همان ص ۹۵ که نورایی به آن ارجاع می‌دهد خلافِ او را می‌گوید: «gumāštan \"\n   \"فارسی نو = gumārdan پازند = gumārtan پهلوی «گماشتن، معین کردن، سپردن» ... هیچ‌جا vِ آغازین نشان نمی‌دهد و \"\n   \"به‌هرحال با *vi-mar پارسیِ باستان هیچ ربطی ندارد». چونگ آن را از *ui- + *marH «بستن، بازداشتن» می‌گیرد \"\n   \"(سنسکریت mar- «مانع شدن»، لاتین mora «درنگ») با معنای آغازینِ «گشودن» ← «رها کردن، سپردن، گماشتن». حاشیهٔ \"\n   \"خودِ معین در برهان (ص ۱۸۳۴، ج ۳) نیز تنها «پهلوی gumārtan (از: گمار + پسوند مصدری) ... ارمنی gumar-el» \"\n   \"می‌دهد و به هوبشمان ۹۳۱ ارجاع می‌دهد، یعنی به همان ردّیه. پس: پژوهش امروزی این گره را در بخشِ «گماردن» \"\n   \"رد می‌کند.\"),\n \"sources\": [W_AMAR],\n \"ref_check\": [\n   {\"ref\": \"HUB:95\", \"status\": \"contradicts\", \"note\": \"Hübschmann, Persische Studien, printed p. 95 (HUB.txt leaf 106, the leaf opening '— 95 —'), note 931: 'Np. gumāštan = pāz. gumārdan = phl. gumārtan \\\"einsetzen, bestimmen, beauftragen, betrauen\\\" Min. Gl. 93, Bdh. Gl. 225, afgh. gumārǝl \\\"to consign\\\", arm. LW. gumar-el 1) \\\"sammeln\\\", 2) \\\"schicken, übergeben, einsetzen\\\" zeigt nirgends den Anlaut v- und hat jedenfalls mit ap. *vi-mar = skr. vi-smar nichts zu thun.' The cited page explicitly rejects the derivation the arrow draws.\"},\n   {\"ref\": \"HRN:208\", \"status\": \"partial\", \"note\": \"Horn, Grundriss der neupersischen Etymologie, printed p. 208 (HRN.txt leaf 230, headed '— 208 —'), no. 931: 'gumāštan/gumārdan \\\"vertrauen, übergeben\\\", Praes. gumār-em. ap. *vi + √mar- mit Bedeutungswechsel, vergl. skr. vi-smar- \\\"vergessen\\\"; phlv. gumāstan, gumār. Unsicher.' — this IS Nourai's source for vi-mar → gomārdan, but Horn himself closes the entry with 'Unsicher' and reconstructs Old Persian, not Avestan.\"},\n   {\"ref\": \"BQT:1834\", \"status\": \"partial\", \"note\": \"Borhān-e Qāṭeʿ ed. Moʿīn vol. 3, pdf p. 631 (= printed ≈1834 by the recorded offset), s.v. «گماردن، گماریدن، گماشتن»: Moʿīn's footnote gives 'پهلوی gumārtan (از: گمار + [پسوند] پسوند مصدری) ... پازند gumardan, gumaral (واگذار کردن) ... ارمنی gumar_el (جمع کردن - فرستادن - نصب کردن) «هوبشمان ۹۳۱»' plus the senses 'نصب کردن - فرستادن - اجازه و رخصت دادن - سفارش کردن'. It documents the Pahlavi form but offers no Avestan mar- link and points to the Hübschmann note that denies one.\"},\n   {\"ref\": \"BQT:1978\", \"status\": \"supports\", \"note\": \"Vol. 4 pdf p. 61 (= printed 1978), s.v. «مر»: '... و با تشدید ثانی در عربی بمعنی مرور کردن و گذشتن بر چیزی و از جایی باشد - و بمعنی شمار هم هست', with 'مر بود پنجاه و چون آمد دو مر' (Jāmī) and the footnote 'این حسابی است که جولاهان در شمردن تارهای کرباس کنند'. Supports Nourai's mar 'account, count, number' precisely.\"},\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary s.v. amar, āmār-, āmārgar (PHD.txt leaf 189) and the English index (leaves 816, 1136, 1782, 3345)\", \"stance\": \"supports\",\n    \"note\": \"'a-mar [ml] countless, innumerable. amar [ml | N ~] reckoning, consideration. āmār- [ʾmʾl-] reckon, calculate. ~išn: reckoning ... āmārgar [ʾmʾlgl | N ~] reckoner'; index: 'reckoning āmār(išn), hangārag, mar, ōšmārag, ūšmārišn'; 'appoint frāz griftan, gumārdan, hištan'; 'entrust abespurdan, gumārdan'. Confirms mar, āmār, ōšmār- and gumārdan as MP words (with no etymologies).\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II s.v. amar (line 384) and ōšmurtan (line 2847)\", \"stance\": \"supports\",\n    \"note\": \"'amar [ʾmʾl] account; the Reckoning ... Paz. NP āmār. From Av. (1142 sq.) ā-mar-, originally ā-hmar-, cf ōšmurtan; Arm. lw. hamar; Targ. Talm. ʾmrkr \\\"cashier\\\". Bailey, BSOS VI, 1930, 65 sq.'; 'ōšmurtan [ʾwšmwltn] ēšmur- (ēšmār-) to reckon, to calculate ... < *aviš-hmár-, from aviš + Av. (1142) mar-, orig. *hmar-, Skr smar-; MPrs act. ʾšmʾr-, pass. ʾšmyr- \\\"to reckon\\\"; Paz. xuašmurdan; NP šumurdan šumār.' — the exact intermediate forms for āmār and šomordan.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 s.v. *hmar and s.v. *marH\", \"stance\": \"partial\",\n    \"note\": \"s.v. *hmar, NWIR section: 'NP šumurdan/šumār-, Kurd. žmārtin ... \\\"to count\\\" || (+ *ā-) ... NP āmār \\\"numeration, calculation\\\", Kurd. ažmār ... || (+ *ham-) NP hamār \\\"number, quantity\\\"'. But NP gumāštan/gumār- appears only s.v. *marH 'to block, hinder', with the note 'The meaning of the Pers. verb was probably originally *\\\"unblock\\\" (with negative/reversive *ui-): > *\\\"to let go, allow\\\"' — supporting mar/āmār/šomordan and contradicting gomārdan.\"},\n   {\"src\": \"HUB\", \"where\": \"Hübschmann no. 791 (printed p. 80 f., HUB.txt leaf 90) and §61 (printed p. 173, leaf 183)\", \"stance\": \"partial\",\n    \"note\": \"no. 791: 'aber šumurdan geht nicht auf zd. aiwi-smar zurück, trotz phl. ōsmurtan (Gl. and Ind. 53), das ušmurtan gelesen werden kann'; §61: 'šumār \\\"Zahl\\\", šumurdan \\\"zählen\\\", phl. ušmurtan, ap. -smar- u. s. w.' with the rule that a prothetic u appears before a following u/ō. Confirms the Persian forms and the root while quarrelling about the preverb.\"},\n   {\"src\": \"Wiktionary\", \"where\": W_AMAR, \"stance\": \"supports\",\n    \"note\": \"آمار: 'Inherited from Middle Persian (ʾmʾl /āmār/, \\\"reckoning, consideration\\\"), from Old Persian'; senses '1. statistics; 2. (obsolete) calculation, enumeration'; derived آمارگر.\"},\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Sogdian\",\n \"words\": \"`šm`r`\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Nourai's backtick notation renders the aleph, so ʾšmʾrʾ, and Gharib's Sogdian dictionary has \"\n   \"it on exactly the cited page: SOD printed p. 69 (SOD_pages.txt leaf 135, which carries the printed \"\n   \"numeral 69), entries 1760-1762 — 'ʾsmʾr- B, S: (ə)smār < *hismara-, Av. hišmar; to think, consider, \"\n   \"count'; '1761 ʾsmʾrʾ M: (ə)smāra, Av. hišmar, f. n., thought'; '1762 ʾsmʾrʾk(h) B, S: (ə)smārā(k), \"\n   \"thought, meditation'. Formally this is the Old Iranian preverb-form *(a)biš-mara- / *hiš-mara- with the \"\n   \"ruki š, made into an ā-stem feminine abstract; Gharib herself glosses the etymology 'Av. hišmar', which \"\n   \"is precisely Nourai's arrow from the Avestan root. Cheung confirms the verb across the Sogdian corpora \"\n   \"('SSogd. ʾsmʾr, BSogd. smʾr, CSogd. šmʾr \\\"to think, consider\\\"'). Nourai's gloss 'thought, imagination' \"\n   \"matches Gharib's 'thought, meditation'.\"),\n \"derivation_fa\": (\"نشانهٔ ` در کتابِ نورایی همان الف است، پس واژه ʾšmʾrʾ خوانده می‌شود، و فرهنگِ سغدیِ بدرالزمان \"\n   \"قریب آن را درست در همان صفحه‌ای دارد که نورایی نشانی داده: صفحهٔ چاپیِ ۶۹، مدخل‌های ۱۷۶۰ تا ۱۷۶۲ — \"\n   \"«ʾsmʾr-: (ə)smār از *hismara-، اوستایی hišmar؛ اندیشیدن، در نظر گرفتن، شمردن»؛ «۱۷۶۱ ʾsmʾrʾ: (ə)smāra، \"\n   \"اوستایی hišmar، اسمِ مادینه، اندیشه»؛ «۱۷۶۲ ʾsmʾrʾk(h): اندیشه، تأمل». از نظرِ ساخت، این همان صورتِ \"\n   \"پیشوندیِ ایرانیِ باستان *hiš-mara- با šِ روکی است که به اسمِ معنای مادینهٔ ā-ستاک بدل شده؛ خودِ قریب \"\n   \"ریشه‌اش را «اوستایی hišmar» می‌نویسد، یعنی همان پیکانی که نورایی از جعبهٔ اوستایی کشیده است. چونگ هم این \"\n   \"فعل را در سه گونهٔ سغدی تأیید می‌کند. معنایی که نورایی می‌دهد («اندیشه، خیال») با «اندیشه، تأمل»ِ قریب \"\n   \"می‌خواند. ادعای نورایی درست است.\"),\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"SOD:69\", \"status\": \"supports\", \"note\": \"Gharib, Sogdian Dictionary, printed p. 69 = SOD_pages.txt leaf 135 (the leaf begins with the printed numeral '69'): '1760 ʾsmʾr- B, S — (ə)smar ©<*hismar- =>šmʾr- : think, (re)consider, count'; '1761 ʾsmʾrʾ M — (ə)smara ©Av. hišmar ©f. n. : thought'; '1762 ʾsmʾrʾk(h) B, S — (ə)smara(k) : thought, meditation'; '1763 ʾsmʾrʾt- S'. Exactly Nourai's word, gloss and derivation from Avestan.\"},\n ],\n \"consulted\": [\n   {\"src\": \"SOD\", \"where\": \"SOD_pages.txt leaf 135 = printed p. 69, entries 1760-1763\", \"stance\": \"supports\", \"note\": \"quoted above; also entries 7937 ptsmʾr- and 8198 pw ptsmʾr elsewhere in the dictionary for the pati- compound.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 s.v. *hmar, SOGDIAN section (CHEUNG.txt line ~9757)\", \"stance\": \"supports\",\n    \"note\": \"'SOGDIAN: SSogd. ʾsmʾr, BSogd. smʾr, CSogd. šmʾr \\\"to think, consider\\\" || (+ *pati-) SSogd. ptšmr- \\\"to count\\\", CSogd. pcmr- \\\"to reckon, consider\\\", MSogd. ptsmr- \\\"to think, count\\\" ...' with the parent 'PIE *(s)mer- ... Pok.: 969'.\"},\n   {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, Dictionary of Khotan Saka (grep 'sumar' / 'hismar')\", \"stance\": \"silent\",\n    \"note\": \"no line recovered from this OCR; Cheung nevertheless cites Khotanese sumār- (saʾmar-) 'to count' from SGS: 128 for the same root.\"},\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Latin\",\n \"words\": \"me-mor\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Latin memor, -oris 'mindful, remembering' is the reduplicated formation of the root, and \"\n   \"Nourai's hyphenation me-mor states the analysis correctly: *me-mor- < *me-mor-/*mi-mer-, a broken \"\n   \"reduplication of *(s)mer-, exactly parallel to Avestan mimara- 'mindful' and Old English ge-mimor \"\n   \"'known' (both cited by Pokorny p. 969 and by Klein s.v. memory: 'L. memoria ... fr. memor, \\\"mindful\\\", \"\n   \"which stands for *me-mor'). Watkins: '2. Reduplicated form *me-mor- in ... b. Latin memor, mindful: \"\n   \"MEMORABLE, MEMORY; COMMEMORATE, REMEMBER.' The initial s- of the s-mobile is absent in Latin, as in Greek \"\n   \"μέριμνα and Germanic murnan; only Sanskrit smarati keeps it. From memor Latin built memoria 'memory' and \"\n   \"the verb memorāre.\"),\n \"derivation_fa\": (\"memor لاتین «یادآور، به‌یاددارنده» صورتِ مضاعفِ همین ریشه است و خط‌تیره‌ای که نورایی گذاشته \"\n   \"(me-mor) تحلیل را درست نشان می‌دهد: *me-mor- از تکرارِ ناقصِ *(s)mer-، هم‌ساختِ mimara- اوستایی «یادآور» و \"\n   \"ge-mimor انگلیسیِ باستان «شناخته» — که پوکورنی در ص ۹۶۹ و کلاین ذیلِ memory هر دو را می‌آورند: «memoria \"\n   \"لاتین ... از memor «یادآور» که صورتِ *me-mor است». واتکینز نیز می‌نویسد: «صورتِ مضاعفِ *me-mor- ... \"\n   \"memor لاتین: MEMORY، REMEMBER». sِ متحرکِ آغازین در لاتین — مانندِ μέριμνα یونانی و murnan ژرمنی — افتاده \"\n   \"است و تنها سنسکریت smarati آن را نگه داشته. از memor واژهٔ memoria و فعلِ memorāre ساخته شده. ادعای \"\n   \"نورایی درست است.\"),\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. (s)mer-1: '2. Reduplicated form *me-mor- in: a. Germanic *mi-mer- in Old Norse Mimir ...; b. Latin memor, mindful: MEMORABLE, (MEMORANDUM), MEMORY; COMMEMORATE, REMEMBER. [Pok. (s)mer- 969.]'\"},\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"p. 969 s.v. (s)mer-\", \"stance\": \"supports\",\n    \"note\": \"'Latin memor \\\"eingedenk\\\" (compare Avestan mimara- ds., Old English ge-mimor ds.), memoria \\\"Gedächtnis\\\"; Moera \\\"eine Parze\\\".'\"},\n   {\"src\": \"KLN\", \"where\": \"p. 961 s.v. memory (KLN_1966.txt line 23432)\", \"stance\": \"supports\",\n    \"note\": \"'fr. L. memoria, \\\"memory\\\", fr. memor, \\\"mindful\\\", which stands for *me-mor and derives fr. I.-E. *mer-(s)mer-, reduplication of base *(s)mer-, \\\"to care for, be anxious about, think, consider, remember\\\".'\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, grep 'memor' in LAT.txt\", \"stance\": \"silent\",\n    \"note\": \"the relevant leaf was not recovered from this OCR; nothing quoted.\"},\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 5, \"lang\": \"English\",\n \"words\": \"memory, remember\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Both English words come from Latin memor through French, and the chain is completely \"\n   \"uncontroversial. memory: Latin memoria > Old French memorie / memoire > Middle English memorie > memory \"\n   \"(Klein: 'ME. memorie, fr. OF. memorie (F. memoire), fr. L. memoria'). remember: Late Latin rememorārī \"\n   \"'to call to mind' (re- + memor) > Old French remembrer > Middle English remembren; the Latin verb is a \"\n   \"post-classical re-formation on memor, which is why English has -member and not -memorate (the learned \"\n   \"doublet commemorate keeps the classical shape). Watkins lists both English words in the same root \"\n   \"article: 'Latin memor, mindful: MEMORABLE, (MEMORANDUM), MEMORY; COMMEMORATE, REMEMBER.'\"),\n \"derivation_fa\": (\"هر دو واژهٔ انگلیسی از memor لاتین و از راهِ فرانسوی آمده‌اند و زنجیره یکسر بی‌اختلاف است. \"\n   \"memory: memoria لاتین ← memorie/memoire در فرانسویِ باستان ← memorie در انگلیسیِ میانه ← memory. \"\n   \"remember: rememorārī در لاتینِ متأخر «به یاد آوردن» (از re- و memor) ← remembrer فرانسویِ باستان ← \"\n   \"remembren انگلیسیِ میانه؛ فعلِ لاتین ساختی پس‌کلاسیک بر memor است و همین است که انگلیسی ‑member دارد نه \"\n   \"‑memorate — دوگانهٔ عالمانه‌اش commemorate صورتِ کلاسیک را نگه داشته است. واتکینز هر دو واژه را در همین \"\n   \"مدخلِ ریشه می‌آورد. ادعای نورایی درست است.\"),\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. (s)mer-1 lists MEMORY and REMEMBER among the derivatives of Latin memor, exactly as the chart draws Latin → English.\"},\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 961 s.v. memory (KLN_1966.txt line 23432)\", \"stance\": \"supports\",\n    \"note\": \"'memory, n. — ME. memorie, fr. OF. memorie (F. memoire), fr. L. memoria, \\\"memory\\\", fr. memor, \\\"mindful\\\" ... Cp. memoir, commemorate, remember.'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, grep 'remember' in SKT.txt\", \"stance\": \"silent\", \"note\": \"no headword line recovered from this OCR.\"},\n   {\"src\": \"POK\", \"where\": \"p. 969\", \"stance\": \"supports\", \"note\": \"'Latin memor \\\"eingedenk\\\" ... memoria \\\"Gedächtnis\\\"' — the Latin base of both English words.\"},\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 6, \"lang\": \"Different Languages\",\n \"words\": \"\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"An empty pass-through box: Nourai uses 'Different Languages' whenever the English words below \"\n   \"reach the root by more than one route, so that no single intermediate language can be named on the box. \"\n   \"Here it stands for two distinct paths — Greek (μάρτυς → Ecclesiastical Latin martyr → Old English martyr) \"\n   \"for martyr, and Germanic (*murnan → OE murnan) for mourn. The box is legitimate bookkeeping, and its two \"\n   \"references half-support it: Klein p. 943 s.v. martyr and p. 1009 s.v. mourn do bring both words to \"\n   \"*(s)mer-, whereas Watkins's (s)mer-1 article lists only MOURN and has no martyr at all. Hence 'plausible' \"\n   \"rather than 'confirmed'.\"),\n \"derivation_fa\": (\"این جعبه‌ای گذری و تهی است: نورایی هر جا واژه‌های انگلیسیِ زیرِ جعبه از بیش از یک راه به \"\n   \"ریشه می‌رسند، برچسبِ «زبان‌های مختلف» می‌گذارد، چون نمی‌توان یک زبانِ میانی را بر جعبه نوشت. اینجا این \"\n   \"برچسب نمایندهٔ دو راهِ جداگانه است: راهِ یونانی (μάρτυς ← martyr لاتینِ کلیسایی ← martyr انگلیسیِ باستان) \"\n   \"برای martyr، و راهِ ژرمنی (*murnan ← murnan انگلیسیِ باستان) برای mourn. این شیوهٔ نمودارکشی پذیرفتنی است \"\n   \"و از دو مأخذی که آورده، یکی پشتیبانی می‌کند: کلاین در ص ۹۴۳ ذیلِ martyr و ص ۱۰۰۹ ذیلِ mourn هر دو واژه را \"\n   \"به *(s)mer- می‌بندد، اما مدخلِ (s)mer-1 واتکینز تنها MOURN را می‌آورد و از martyr نامی نمی‌برد. پس حکم \"\n   \"«با احتیاط پذیرفتنی» است.\"),\n \"sources\": [W_MARTYS],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins 1985 s.v. (s)mer-1 'To remember' lists MOURN (via Germanic *murnan) and MEMORY/REMEMBER (via Latin memor) but no MARTYR; the Greek path the box needs for martyr is absent from Watkins.\"},\n   {\"ref\": \"KLN:943\", \"status\": \"supports\", \"note\": \"Klein p. 943 (the printed page marker '943' stands at KLN_1966.txt line 22997, immediately before the martyr article at line 23022): 'martyr, n. — ME. martir, fr. OE. martyr, fr. Eccles. L. martyr, fr. Gk. μάρτυς, Aeol. and Dor. μάρτυρ, \\\"witness; martyr\\\", which prob. stands for I.-E. *mrtu- and is rel. to Gk. μέριμνα ... and cogn. with OI. smarati, \\\"remembers\\\", L. memor, \\\"mindful\\\". See memory.' The cited page is exactly the martyr entry and it does route the word to this root.\"},\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"pp. 943 (martyr) and 1009 (mourn)\", \"stance\": \"supports\",\n    \"note\": \"both entries end with 'See memory and cp. words there referred to', i.e. Klein groups martyr and mourn under the same base — the two 'different languages' of the box.\"},\n   {\"src\": \"POK\", \"where\": \"p. 969 s.v. (s)mer-\", \"stance\": \"partial\",\n    \"note\": \"Pokorny includes the Germanic mourn-words ('Gothic maurnan, Old English murnan, Old High German mornen') but flags the Greek witness-words: 'also μάρτυς, -υρος, hom. μάρτυρος, Cretan μαῖτυρ- \\\"witness, testifier\\\"? different above S. 735' — a question mark and a cross-reference to a different root.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. (s)mer-1\", \"stance\": \"partial\", \"note\": \"MOURN only; no martyr.\"},\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 7, \"lang\": \"English\",\n \"words\": \"martyr, mourn\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"mourn is confirmed; martyr is doubtful. mourn < Middle English mournen < Old English murnan \"\n   \"'to care for, be anxious about; to lament over' < Proto-Germanic *murnan (Gothic maurnan, OS mornian, OHG \"\n   \"mornēn, ON morna 'to pine away') < zero-grade *mr̥-n- of *(s)mer-; Watkins prints it word for word \"\n   \"('Suffixed zero-grade form *mr-no- in Germanic *murnan, to remember sorrowfully, in Old English murnan, \"\n   \"to mourn: MOURN'), Pokorny p. 969 lists the same Germanic set, and Klein's OE gloss 'to care for, be \"\n   \"anxious about' is literally Nourai's root gloss. martyr < Old English martyr < Ecclesiastical Latin \"\n   \"martyr < Greek μάρτυς, gen. μάρτυρος (Doric μάρτυρ) 'witness', which took on the Christian sense 'one who \"\n   \"witnesses by dying' in 2nd-c. Greek and reached English with Christianity. The traditional etymology \"\n   \"connects μάρτυς to *(s)mer- ('one who bears in mind', *mr̥-tu-), which is what Klein p. 943 prints; but \"\n   \"Pokorny himself queries it ('also μάρτυς ... \\\"witness, testifier\\\"? different above S. 735'), Watkins \"\n   \"omits it, and Beekes (EDG) rejects the IE derivation on the strength of the word's ending and calls it \"\n   \"Pre-Greek. So one of the two words is certain and the other is contested.\"),\n \"derivation_fa\": (\"mourn تأییدشده است و martyr مشکوک. mourn از mournen انگلیسیِ میانه از murnan انگلیسیِ \"\n   \"باستان «پروا داشتن، نگران بودن؛ سوگ گفتن» از *murnan ژرمنیِ آغازین (گوتیک maurnan، ساکسونِ باستان \"\n   \"mornian، آلمانی علیای باستان mornēn، نورس morna «پژمردن») از گونهٔ صفرگونهٔ *mr̥-n- همین ریشه؛ واتکینز \"\n   \"واژه‌به‌واژه همین را می‌نویسد، پوکورنی در ص ۹۶۹ همان مجموعهٔ ژرمنی را می‌آورد، و معنایی که کلاین برای \"\n   \"murnan می‌دهد («پروا داشتن، نگران بودن») عیناً همان معنایی است که نورایی برای ریشه نوشته. اما martyr از \"\n   \"martyr انگلیسیِ باستان از martyr لاتینِ کلیسایی از μάρτυς (اضافیِ μάρτυρος، دوریِ μάρτυρ) «گواه» آمده که \"\n   \"در یونانیِ سدهٔ دومِ میلادی معنایِ مسیحیِ «گواهی‌دهنده به بهای جان» گرفت و با مسیحیت به انگلیسی رسید. \"\n   \"ریشه‌شناسیِ سنتی μάρτυς را به *(s)mer- می‌بندد («آن‌که در یاد دارد»، *mr̥-tu-) و کلاین در ص ۹۴۳ همین را \"\n   \"می‌آورد؛ اما خودِ پوکورنی با علامتِ پرسش از آن می‌گذرد و به صفحهٔ دیگری ارجاع می‌دهد، واتکینز آن را نمی‌آورد، \"\n   \"و بیکس بر پایهٔ پایانهٔ واژه ریشهٔ هندواروپایی را رد می‌کند و آن را پیش‌یونانی می‌خواند. پس یکی از دو واژهٔ \"\n   \"این جعبه قطعی و دیگری محلِ اختلاف است.\"),\n \"sources\": [W_MARTYS],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"This node carries no refs= of its own in the chart; the references stand on the parent box #6 (AHD; KLN:943), which were checked there.\"},\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 1009 s.v. mourn (KLN_1966.txt line ~24533) and p. 943 s.v. martyr\", \"stance\": \"supports\",\n    \"note\": \"'mourn, intr. and tr. v. — ME. mournen, mornen, fr. OE. murnan, \\\"to care for, be anxious about; to lament over\\\", rel. to OS. mornian, OHG. mornen, Goth. maurnan, \\\"to mourn\\\", ON. morna \\\"to pine away\\\", fr. I.-E. base *(s)mer-, \\\"to care for, be anxious about, think, consider, remember\\\"'; and s.v. martyr: 'fr. Gk. μάρτυς ... which prob. stands for I.-E. *mrtu- and is rel. to ... OI. smarati, \\\"remembers\\\", L. memor'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. (s)mer-1\", \"stance\": \"partial\",\n    \"note\": \"'1. Suffixed zero-grade form *mr-no- in Germanic *murnan, to remember sorrowfully, in Old English murnan, to mourn: MOURN' — mourn yes, martyr not listed.\"},\n   {\"src\": \"POK\", \"where\": \"pp. 969-970\", \"stance\": \"partial\",\n    \"note\": \"Germanic mourn-words listed ('Old English mimorian, ge-mimor; Gothic maurnan, Old English murnan, Old High German mornen \\\"care for, worry, anxiously worry about\\\"'); the Greek witness-group carries a question mark and a cross-reference: 'also μάρτυς, -υρος, hom. μάρτυρος, Cretan μαῖτυρ- \\\"witness, testifier\\\"? different above S. 735'.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 s.v. *hmar, IE COGNATES\", \"stance\": \"supports\",\n    \"note\": \"'IE COGNATES: Gr. ἱμείρω \\\"I desire, long\\\", Goth. *maurnan, OHG mornēn, OE murnan, Engl. to mourn' — mourn given as an IE cognate of the Iranian root, and no martyr.\"},\n   {\"src\": \"Wiktionary/Beekes\", \"where\": W_MARTYS, \"stance\": \"contradicts\",\n    \"note\": \"μάρτυς: 'typically derived from PIE *(s)mer- \\\"to fall into thinking, remember, care for\\\"' but 'Beekes ... derives it from Pre-Greek based on the ending of the word'.\"},\n ]\n})\n\nout[\"entries\"].append(e2)\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-334.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk334.py && python3 -m json.tool data/verification/page-334.json > /dev/null && echo \"JSON valid\" && python3 tools/verify_check.py 334",
 "description": "Write and validate page-334.json"
}
```


### [2026-09-07T16:34:04.755Z] TOOL RESULT

```
ok
JSON valid
nodes verified: 19/19
node verdicts: {'plausible': 6, 'confirmed': 8, 'disputed': 4, 'transcription_suspect': 1}
root verdicts: {'plausible': 1, 'confirmed': 2}
ref checks: {'supports': 12, 'partial': 8, 'contradicts': 2, 'not_found': 3, 'not_checked': 4}
books consulted: {'supports': 29, 'contradicts': 6, 'silent': 14, 'partial': 18} | by book: {'KLN': 10, 'Wiktionary': 5, 'POK': 5, 'SKT': 4, 'NYB': 4, 'CHEUNG': 4, 'WLD': 3, 'Etymonline': 3, 'PHD': 3, 'LAT': 3, 'Wiktionary/Beekes': 2, 'MON': 2, 'BQT': 2, 'BRT': 2, 'AVG': 2, 'HUB': 2, 'AHD': 2, 'AFM': 1, 'HRN': 1, 'GPL': 1, 'LEW': 1, 'BOOK': 1, 'PHN': 1, 'DEV': 1, 'SOD': 1, 'ISS_alt_DKS': 1}
```


## [2026-09-07T16:34:28.637Z] AGENT

Done. `python3 tools/verify_check.py 334` reports 19/19 nodes, 0 PROBLEM lines.

**Page 334 (book p. 304) — 3 entries, 19 nodes**

Verdicts: nodes — 8 confirmed, 6 plausible, 4 disputed, 1 transcription_suspect. Roots — 2 confirmed (Menth/Meth "stir" = POK 732 menth-1; Mer 1/Smer = POK 969 (s)mer-), 1 plausible (Menth "mouth, to chew" = POK 732 menth-2 / Watkins mendh-2; Beekes treats the Greek group as Pre-Greek).

Disputed / flagged:
- **Menth #5 Germanic `muntha` "mouth"** — Watkins (Nourai's own cited ref) puts *munþaz under **men-2 "to project"**, and Wiktionary/Kroonen under *men- "chin" (Lat. mentum, Welsh mant); Pokorny lists it here but himself offers the men- alternative.
- **Menth/Meth #1 Avestan `mant 2, vant` "in control, owner"** — not a verb: Jackson, *Avesta Grammar* §851 shows -maṇt-/-vaṇt- is the inherited **possessive suffix** (= Skt -mant-/-vant-, PIE *-ment-/*-uent-), unrelated to mant- "to stir". Nourai's own box-NOTE flags the puzzle; modern scholarship answers that the whole -mand branch is filed under the wrong root. (mant 1 "to stir" itself is confirmed: BRT AiW 1135 "j. mant- V. 'rühren'".)
- **Mer 1 #1 Avestan `vi-mar` "designate (off)"** — no such Avestan form; it is Horn's reconstructed OP *vi-mar (HRN:208, which itself ends "Unsicher"). Cheung 2007 puts gumār- under *ui- + **\*marH "to block, hinder"** (Pok. 970).
- **Mer 1 #2 Persian `gomârdan`** — same problem, and **HUB:95, the page Nourai cites, says the opposite**: "…zeigt nirgends den Anlaut v- und hat jedenfalls mit ap. *vi-mar = skr. vi-smar nichts zu thun." (mar, âmâr, šemordan all confirmed via BQT:1978, Nyberg, MacKenzie, Cheung.)

Transcription_suspect (error_in = **book**, extraction faithful):
- **Menth/Meth #4 Latin `manphur`** — printed page really reads "manphur, manfur" (PNG saved to `data/verification/sources/refs/ocr/BOOK/334.png`); Pokorny 732, Walde-Pokorny II 269 and Ernout-Meillet all have **mamphur** (Paulus-Festus 117,3). Nourai's misprint; `manfur` is fine. Correct form: "mamphur, manfur".

No extraction errors found — the JSON matches the printed chart everywhere (checked against the rendered page image).

Other notable ref findings: TAD:69 confirmed verbatim ("مصطكي – يونانى… صمغا يعلك"); BQT:2040 located (vol. 4 pdf p. 123) and Moʿīn's footnote there gives Pahlavi -ōmand/-mand ← Avestan -mant- as a **possessive suffix**; SOD:69 confirmed exactly (Gharib entries 1760-1762, ʾsmʾrʾ "thought", "Av. hišmar"); **FFD:64 not_found** (that page has شیفتن/فراموشیدن/فرجامیدن, no mar-), **FSF:311 not_found** (no suffix article; scan offset unestablished), AHD:793 not_checked (1975/76 main-text page, lending-only). Nine web pages archived via `fetch_source.py`.
