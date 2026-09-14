# Verification process log — verify-page-432


## [2026-09-14T01:22:32.546Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 432 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-432.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-432.json. Write /home/sfmqrb/git/rishe/data/verification/page-432.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 432` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:22:34.304Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-14T01:22:35.304Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:22:35.341Z] TOOL RESULT

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
226	Several agents run at the same time and share the scratchpad and `/tmp`, so every temporary
227	file you create must carry your page number in its name (e.g. `e0-363.json`, `pg363.png`,
228	`draft-363.json`), never a bare `e0.json` or `entry.json` — another agent will overwrite it.
229	
230	```json
231	{
232	  "pdf_page": 126,
233	  "book_page": 96,
234	  "verified_by": "claude-opus-5",
235	  "verified_on": "2026-09-05",
236	  "entries": [
237	    {
238	      "entry": 0,
239	      "root": "Dheigh, Dhigha",
240	      "verdict": "confirmed",
241	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
242	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
243	      "note_fa": "ریشهٔ هندواروپایی آغازین *dʰeyǵʰ- «خمیر کردن، شکل دادن (گِل)» … ادعای نورایی درست است.",
244	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
245	      "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
246	      "consulted": [{"src": "WLD", "where": "Bd. I 833", "stance": "supports", "note": "…"}],
247	      "nodes": [
248	        {
249	          "id": 6,
250	          "lang": "Avestan",
251	          "words": "pairi-daeza",
252	          "verdict": "confirmed",
253	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' …",
254	          "derivation_fa": "«پردیس» … اوستایی pairi-daēza- «دیوارکشیده، باغِ محصور» از pairi «پیرامون» و daēza- «دیوار» …",
255	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza"],
256	          "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
257	          "consulted": [{"src": "BRT", "where": "col. 866", "stance": "supports", "note": "…"}]
258	        }
259	      ]
260	    }
261	  ]
262	}
263	```
264	
265	Rules:
266	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
267	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
268	- `words` = the transliterations of the node joined by "; " (copy from the chart).
269	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
270	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
271	- Keep `note` on the entry for root-level comments and for anything cross-cutting.
272	- If a node lists several words, cover each word; if they differ in verdict, use the worst
273	  verdict for the node and explain per word in `derivation`.
274	- Where the chart's own NOTE already records a dispute, evaluate it: say which side modern
275	  scholarship takes.
276	- Every node has `ref_check` (array, may contain a single `not_checked` item) AND `consulted`
277	  (array) AND `derivation_fa` (string); every entry has `note_fa`.
278	- Valid JSON only. Test it with `python3 -m json.tool` before finishing, then run
279	  `python3 /home/sfmqrb/git/rishe/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
280	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
281	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
282	  any extraction errors (JSON differs from the printed page) the owner must fix.
283	  Do not paste the JSON back into your reply.
284	
```


## [2026-09-14T01:22:35.799Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-432.txt"
}
```


### [2026-09-14T01:22:35.818Z] TOOL RESULT

```
1	=== PDF page 432 (book page 402) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Sâwel, Sŭ 3 : sun  (refs POK:881)  PART 1
4	#1 (parent #0) [Avestan] refs=POK:881 | hvare, xvar 1 : sun, light
5	  #2 (parent #1) [Persian] refs=MON:5220; BQT:2389 | hŭr 2 «هور» : sun, star ; xor «خور» : sun
6	    #3 (parent #2) [Persian] refs=FVF:189; AFM:50 | hŭr-bân «هوربان» : "sun guard", chameleon, it is called "âftâb-parast: sun worshipper" in modern Persian. | NOTE: "hŭrbân" was not found in MON.
7	      #4 (parent #3) [Arabic] refs=FVF:189; AFM:50 | horbâ «حُرباء» : chameleon
8	        #5 (parent #4) [Persian] refs=MON:1347 | herbâ «حربا» : chameleon
9	  #6 (parent #1) [Avestan] refs=POK:881; KLN:1469; HRN:111 | hvare-xšaeta : bright sun ☞Ksei 2 ; hvare-âsân : sun rise, east ; hvare-varân : where sun goes, west ☞Bher 1
10	    #7 (parent #6) [Persian] refs=BQT:723; MON:1395 | xoršîd «خورشید» : sun ; xorâsân «خراسان» : an eastern state in Iran ; xâvar[ân] «خاور ، خاوران» : west
11	  #8 (parent #1) [Persian] refs=BQT:2220; IEC:1334 | no-hŭr «نُهور» : sun light, sight, eye ; bad-nohŭr «بد نُهور» : unsightly, ugly
12	#9 (parent #0) [Avestan] refs=POK:881; BQT:1451 | hvarenah, xvarenah, farnah : brilliance, elegance ; farnavant : with bright fate, blessed
13	  #10 (parent #9) [Sogdian] refs=SOD:155 | frn : elegance
14	  #11 (parent #9) [Persian] refs=BQT:180,789,1443,1451; FSF:250 | farr «فرّ» : elegance ; farrox «فرّخ» : blessed ; Farîborz «فریبرز» : with elegant height, well posed ☞Bhergh | extra: فرّه ، فرّهی ، فرهمند / فرخُنیده / فردوست ، فرزاد ، فرشاد ، فرشید ، فرناز
15	#12 (parent #0) [Avestan] refs=POK:881 | xvang : son
16	#13 (parent #0) [Germanic] refs=AHD | sunnôn : sun
17	  #14 (parent #13) [English] refs=None | sun, Sunday, south
18	#15 (parent #0) [Latin] refs=AHD | sôl : sun
19	  #16 (parent #15) [English] refs=None | solar
20	
```


## [2026-09-14T01:22:39.461Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-432.json | head -200",
 "description": "Read source JSON for page 432"
}
```


### [2026-09-14T01:22:39.506Z] TOOL RESULT

```
{
  "pdf_page": 432,
  "book_page": 402,
  "entries": [
    {
      "root": {
        "name": "Sâwel, Sŭ 3",
        "lang": "Indo-European",
        "refs": "POK:881",
        "gloss": "sun"
      },
      "part": 1,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:881",
          "words": [
            {"translit": "hvare, xvar 1", "gloss": "sun, light", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "MON:5220; BQT:2389",
          "words": [
            {"translit": "hŭr 2", "gloss": "sun, star", "script": "هور"},
            {"translit": "xor", "gloss": "sun", "script": "خور"}
          ],
          "note": null,
          "quote": {"text": "که شیری نترسد ز یک دشت گور - ستاره نتابد هزاران چو هور", "poet": "Ferdowsî"}
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "FVF:189; AFM:50",
          "words": [
            {"translit": "hŭr-bân", "gloss": "\"sun guard\", chameleon, it is called \"âftâb-parast: sun worshipper\" in modern Persian.", "script": "هوربان"}
          ],
          "note": "\"hŭrbân\" was not found in MON.",
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Arabic",
          "refs": "FVF:189; AFM:50",
          "words": [
            {"translit": "horbâ", "gloss": "chameleon", "script": "حُرباء"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON:1347",
          "words": [
            {"translit": "herbâ", "gloss": "chameleon", "script": "حربا"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 1,
          "lang": "Avestan",
          "refs": "POK:881; KLN:1469; HRN:111",
          "words": [
            {"translit": "hvare-xšaeta", "gloss": "bright sun", "script": null, "see": ["Ksei 2"]},
            {"translit": "hvare-âsân", "gloss": "sun rise, east", "script": null},
            {"translit": "hvare-varân", "gloss": "where sun goes, west", "script": null, "see": ["Bher 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "BQT:723; MON:1395",
          "words": [
            {"translit": "xoršîd", "gloss": "sun", "script": "خورشید"},
            {"translit": "xorâsân", "gloss": "an eastern state in Iran", "script": "خراسان"},
            {"translit": "xâvar[ân]", "gloss": "west", "script": "خاور ، خاوران"}
          ],
          "note": null,
          "quote": {"text": "زبان پهلوی هرکو شناسد - خراسان آن بود کزوی خورآسد", "poet": "Fakhr Gorgânî"}
        },
        {
          "id": 8,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:2220; IEC:1334",
          "words": [
            {"translit": "no-hŭr", "gloss": "sun light, sight, eye", "script": "نُهور"},
            {"translit": "bad-nohŭr", "gloss": "unsightly, ugly", "script": "بد نُهور"}
          ],
          "note": null,
          "quote": {"text": "از آن با بزرگان نیارم نشستن - که ایشان چو خورند و من بد نهورم", "poet": "Sanâyî"}
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:881; BQT:1451",
          "words": [
            {"translit": "hvarenah, xvarenah, farnah", "gloss": "brilliance, elegance", "script": null},
            {"translit": "farnavant", "gloss": "with bright fate, blessed", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Sogdian",
          "refs": "SOD:155",
          "words": [
            {"translit": "frn", "gloss": "elegance", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 9,
          "lang": "Persian",
          "refs": "BQT:180,789,1443,1451; FSF:250",
          "words": [
            {"translit": "farr", "gloss": "elegance", "script": "فرّ"},
            {"translit": "farrox", "gloss": "blessed", "script": "فرّخ"},
            {"translit": "Farîborz", "gloss": "with elegant height, well posed", "script": "فریبرز", "see": ["Bhergh"]}
          ],
          "script_extra": "فرّه ، فرّهی ، فرهمند / فرخُنیده / فردوست ، فرزاد ، فرشاد ، فرشید ، فرناز",
          "note": null,
          "quote": {"text": "چو آن شاه پالوده گشت از بدی - بتابید از او فرّۀ ایزدی", "poet": "Ferdowsî"}
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:881",
          "words": [
            {"translit": "xvang", "gloss": "son", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "sunnôn", "gloss": "sun", "script": null}
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
            {"translit": "sun, Sunday, south", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "sôl", "gloss": "sun", "script": null}
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
            {"translit": "solar", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
```


## [2026-09-14T01:22:40.204Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T01:22:40.263Z] TOOL RESULT

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


## [2026-09-14T01:22:55.825Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-432.json'))\nprint(json.dumps(d,ensure_ascii=False)[-1200:])\nprint('entries',len(d['entries']))\n\" ; ls data/verification/ | head -50; cat data/verification/sources/refs_online.json | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nfor k in ['POK','MON','BQT','FVQ','AFM','KLN','HRN','SOD','FSF','IEC','AHD','ARY','IRN']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600])\n\"",
 "description": "Inspect JSON tail and refs_online"
}
```


### [2026-09-14T01:22:57.119Z] TOOL RESULT

```
"gloss": "elegance", "script": "فرّ"}, {"translit": "farrox", "gloss": "blessed", "script": "فرّخ"}, {"translit": "Farîborz", "gloss": "with elegant height, well posed", "script": "فریبرز", "see": ["Bhergh"]}], "script_extra": "فرّه ، فرّهی ، فرهمند / فرخُنیده / فردوست ، فرزاد ، فرشاد ، فرشید ، فرناز", "note": null, "quote": {"text": "چو آن شاه پالوده گشت از بدی - بتابید از او فرّۀ ایزدی", "poet": "Ferdowsî"}}, {"id": 12, "parent": 0, "lang": "Avestan", "refs": "POK:881", "words": [{"translit": "xvang", "gloss": "son", "script": null}], "note": null, "quote": null}, {"id": 13, "parent": 0, "lang": "Germanic", "refs": "AHD", "words": [{"translit": "sunnôn", "gloss": "sun", "script": null}], "note": null, "quote": null}, {"id": 14, "parent": 13, "lang": "English", "refs": null, "words": [{"translit": "sun, Sunday, south", "gloss": null, "script": null}], "note": null, "quote": null}, {"id": 15, "parent": 0, "lang": "Latin", "refs": "AHD", "words": [{"translit": "sôl", "gloss": "sun", "script": null}], "note": null, "quote": null}, {"id": 16, "parent": 15, "lang": "English", "refs": null, "words": [{"translit": "solar", "gloss": null, "script": null}], "note": null, "quote": null}]}]}
entries 1
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
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=
FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offs
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 
IRN {"title": "Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ایرانویج-بهرام-فره-وشی/ -> https://dl.eliteraturebook.com/storage/img/ایرانویج.pdf (free PDF site; grey) ; Google Books kP8bAAAAIAAJ (1368 ed., no view)", "lookup_hint": "archive.org 'Iranvej' item is a radio programme, not the book; nothing on ketabnak/noorlib. | For pages in a scanned volume use: python3 tools/ref_page.py IRN:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", "local_file": ["/home/sfmqrb/git/rishe/data/v
```


## [2026-09-14T01:23:02.435Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nprint(list(d.keys()))\nprint()\nfor k in ['FVF','FSF','IEC','SOD']:\n    v=d.get(k)\n    print('==',k, json.dumps(v,ensure_ascii=False)[:900] if v else 'MISSING')\n\"",
 "description": "Check FVF abbreviation"
}
```


### [2026-09-14T01:23:03.613Z] TOOL RESULT

```
['BQT', 'MON', 'SOD', 'SNS', 'FFD', 'FVA', 'AEF', 'VOP', 'FSF', 'TAD', 'FVQ', 'VDQ', 'FVF', 'ETM', 'TZF', 'SAP', 'IRN', 'AFM', 'FRS', 'ZMA', 'FAF', 'ARK', 'AMD', 'DZA', 'KAS', 'DMO', 'SBK', 'VGH', 'VIE', 'AKM', 'ZFS', 'SOR', 'FNI', 'VSF', 'FVS', 'FIB', 'IRT', 'SNB', 'KFL', 'NFI', 'MMF', 'MZF', 'ARM', 'ARB', 'AHD', 'POK', 'KLN', 'HRN', 'IEC', 'KNT', 'SYN', 'WLD', 'ISS', 'OEW', 'HUB', 'BRT', 'FSD', 'SKT', 'PRT', 'NYB', 'HJB', 'PHN', 'LKT', 'WEB', 'SIN', 'AHM', 'CEL', 'GPL', 'MAG', 'DEV', 'DRM', 'ZAW', 'SLW', 'BLY', 'KGW', 'SHP', 'AID', 'OXF', 'MPP', 'DVS', 'SPG', 'ARP', 'PHD', 'TYL', 'LAM', 'UNV', 'LAT', 'NAT', 'TTS', 'DOZ', 'AVG', 'LEW', 'SDQ', 'ROE', 'AFA', 'FWE', 'MFL', 'TLM', 'BST', 'HID', 'AIN', 'ZAP', 'AWH', 'PEI', 'EAV', 'SOG', 'LST', 'PLA', 'AKD', 'RCH', 'ARY']

== FVF {"title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968", "kind": "website", "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)", "lookup_hint": "Alphabetical by Persian headword; noorlib page number N is the scan page — browser needed to read. Not on archive.org.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "PDF exists on several Iranian sites (ketabnak/parsianjoman) but could not be fetched here (login/JS)."}
== FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offset": "484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking", "covers_etymology": false, "notes": "Persian OCR fair (readable prose). Mostly glosses; some Pahlavi/Avestan notes. Edition may differ from the 1363 Dony
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.", "notes": "", "cites": "column/page number of Mann, An Indo-Europea
== SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}", "loca
```


## [2026-09-14T01:23:09.448Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"sāwel\\|sāwol\\|sū̯el\\|sāu̯el\\|s[āa]uel\" POK_full.txt | head -20\necho \"=== POK_02 around p881: leaf = p-344 => leaf 537\"\nawk 'BEGIN{RS=\"\\f\"} NR>=536 && NR<=538 {print \"----LEAF\",NR\"----\"; print}' POK_02.txt | head -120",
 "description": "Find sāwel root in Pokorny"
}
```


### [2026-09-14T01:23:10.508Z] TOOL RESULT

```
63677:trait)], hence alb. geg suni 'eye' : Old Irish {*su//-) suir eye ' : Root / lemma: sauel- sauol- 
71448:lemma: sauel- sauol- suuel- suel- sul-\ (sun). 
71617:Root / lemma: sauel- sauol- suuel-, sue/-, sul- , {*hauhuel-) 
71646:bret. heorsuu' {*sauel-); 
72250:Baltic *sauelia\. in Lithuanian Latvian saule^ sun '; 
83772:alb. and gr. prove that from Root/ lemma: sauel-, sauol-, suuel-, suel-, sul-\ (sun) derived 
83808:See also: see above S. 881 f. sauel- 
=== POK_02 around p881: leaf = p-344 => leaf 537
```


## [2026-09-14T01:23:12.854Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '71610,71760p' POK_full.txt",
 "description": "Read Pokorny sauel- entry"
}
```


### [2026-09-14T01:23:12.911Z] TOOL RESULT

```
Page(s): 880 

Root / lemma: sa-ti- 
See also: s. sa- 
Page(s): 880 

Root / lemma: sauel- sauol- suuel-, sue/-, sul- , {*hauhuel-) 
Meaning: sun 

Note: next to which suen-, sun-, thus of old ///7-stem; suel-^ smolder, burn ' is probably 

identical with it 

Material: 

Note: 

1. Old Indie ved. {*suuef} suvarn. = (zero grade) Avestan hvard'sun, light, sky'. Gen. 
{*suuela) surah = \ay. {*suuelio) huro. Old Indie surya- {* suluo-) m. (compare gr. nAio^, 
sura-m. "sun'; therefrom Old Indie sJ/Ya- "light, bright'. Old Indie svarnara-m. " bright 
space, ether', Avestan x'aranah-, ap. -farnah-' shining fame, magnificence '; 
Other forms in Indo-Aryan: {* suue/-a) *suuar- [\n names] "sun(god)' (Near-Eastern lA); 
Avestan: OAv. huuar9[n] (< *huuaf) "sun' (gen.sg. x^§ng< *huuanh); LAv. huuar9{gev\.sq. 
hu< *huuanh, next to hurd= Ved. suras), Sogd. (Man.) xwr^suv\\ Middle Persian xwr 
"sun', New Persian xwr^suv\\ Oss. xur/xor^suu' 

Maybe Afghan Imar, Waziri Imer, /77ye/'"sun' from Old Indie svarnara-m. " bright space, 
ether '; Armenian arew, aregak, arev, Singhalese ira "sun'. 

Maybe the oldest cognate is Luvian: {<hu-wa-ya-al-li) <huwayalla/i-' Epithet of the Sun- 
god'. 

gr. hom. n£AiO(;, Attic x\K\oc„ Doric bzk\oc„ aK\oq, Cretan ap£AiO(; Hes. (i.e. aFeAioq) "sun', 
further formations of n. *saue/to m. -/o-stem (compare Old Indie surya-); Latin so/, -/ism. 
"sun' (from neutr. *sa^e'/about *sauol, *saol); cymr. haul, acorn, heuul, mcorn. heul, houl, 
bret. heorsuu' {*sauel-); 



in addition Old Irish suili. "eye' from *suli-, ablaut equally with Old Indie surah, and alb. 

hull, uir star' {*sulo- or *suli-); 

Proto-Celtic: *sawol- / *suli- 'sun' [Noun] 

Old Irish: s^//[if] 'eye' 

Middle Welsh: haul 

Middle Breton: heuul, heul 

Cornish: heuulq\. sol, heol 

Proto-Indo-European: *seh2w6l 'sun' 

IE cognates: Skt. surya-, Latin sol, Go. saull 

Notes: The change of meaning in Olr. is understandable from the mythological context. 

'Sun' is viewed as 'the eye of the Sky'. It appears that there was still an ablauting paradigm 

in PCelt., Nom. s. *sawol, Gen. *sul-os, from which Olr. sullwas abstracted 



Note: 



[conservative definitive forms versus indefinite forms (alb. phonetic trait)], hence alb. geg 
suni, Tosc syri{*sulni) "eye' : Old Irish {*sayel-) suir eye ' 
Erroneous etymology, the Celtic name for eye derived from Romance languages 
contaminated by Satem languages the shift k-, g- > -s- 



German 




Auge 


Italian occhio 




Spanish 




ojo 


French 




ceil 


Aragones 




gijello 


Asturian 




gijeyu 


Breton 




lagad 


Calabrese 




occhiu ; uacchiu 


Calo 


aqui 




Catalan
```


## [2026-09-14T01:23:22.054Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '72200,72330p' POK_full.txt",
 "description": "More of Pokorny sauel-"
}
```


### [2026-09-14T01:23:22.116Z] TOOL RESULT

```
Catalan 




diu-menge 


Cornish 




de-Sul 


Latin 




Soils dies 


Welsh 




dydd Sul ; Sul 


Hence alb. dier 


Sunday 


' > dieir sun '. 



Gothic sauilw. {*sdwila-). Old Icelandic sd/f. {*sdwula) "sun', Old Icelandic and-s0lis, 
aschw. and-sylis "the sun zugewendet'; doubtful the rune names Gothic sugil. Old English 
sygei s/ge/from proto Germanic *sugila-, ablaut, with Old Saxon sty/ig//" bright, radiating' 
from *swegila-. Old English sweg(e)lv\. "sky, heaven, sun', stve^/e "bright, radiating' from 
*swagila-\ 

Baltic *sauelia\. in Lithuanian Latvian saule^ sun '; 

Slavic *sulnika-v\. in Old Church Slavic slbn-bce^ sun ' (-/?/- from * 0^/7/ "fire'); 

2. In -e/^stem: 

Avestan x'sng^ShQ sun' (Indo Germanic *suen-s), Gen. from hvarsr, Gothic sunnd{Da\.. 
sunnin, neutr. after sauil). Old English sunna. Old High German sunno, sunna'sun', (under 
the influence of common Celtic -ns-, -nt- > -nn-), wherefore as "sonnseitig = siJdlich' Old 
Icelandic Si/dA" south'. Adv. " southward ', Old English suderra. Old Saxon suthar-liudi 
("southern people'). Old High German sundar ^ so\}\h\ Adv. " southward ', Middle High 
German si//?^ "south' etc. (Modern High German Sudirovn Low German). 
Gujarati surdj" sun' 

Perhaps Tocharian A swance, swanco, Tocharian B swancai- "ray [of light], (sun) beam' 
reflect Proto Tocharian * swancai- which is possibly (with Hilmarsson, 1986a:263-95, in 
nuceP\sav\\, 1942-43a:29) related to Proto-Germanic *sun&a- *"sunny' > "south' and 
*sunnd'sun' (cf. P:881-2; MA:556). The two Germanic words would reflect PIE *sufianto- 
(a derivative of *sehawel-lsuhan- "sun') and, with "particularizing" -/?-, *suhantdn-l suhaiiten- 
Isufiantn-. The attested paradigm of Germanic * sunno reflects a conflation of the o-grade 
and the zero-grade stems {*suhantn- > *sun&n- > *sunn-). For Hilmarsson, the Tocharian 
forms represent a generalization of *sufianten-, further derived by the addition of -ai-. 

Note: 



The root *suhanten- is an attribute noun created in tlie same way as adj. and ordinal 
numbers: 

Anatolian languages show a pattern similar to alb. So Lycian aitata {* oRtd(u)ta) "eight' : alb. 
te/a "eight'; Lycian nuntata ' n\ne' : alb. nanda'n\ne'. Therefore alb. 5/7/a/a "seven' derived 
from a truncated *sa{p)tata' seven' later Old Indie saptathah, Avestan hapta&a-. Old 
Saxon sivotho. Old English seofoda, Lithuanian septintas, also Old Indie saptatf-, Avestan 
haptaiti-10\ in alb. -ta, -teare attribute endings that were solidified in Anatolian and Indie 
cognates. The attribute /a (used in the genitive and adjectives) is unique to alb. language 
alone. 

Therefore alb. /e/a "eight' is a zero grade of Lycian aitata {* oRtd(u)ta) "eight'. It was initially 
an ordinal number used as an attribute [compare Latin octuag/nta' 80']. 

That means Slavic *su/n/ka-n. in Old Church Slavic s/bnbce^ sun ' (-a?/- from * 0^/7/ "fire') is 
phonetically equal to Tocharian A swance, swanco, Tocharian B swancai- "ray [of light], 
(sun) beam', hence Slavic forms were created according to attribute nouns ans are late 
creations. 

Maybe gr. 'AnoAAojv, -ojvoc;; various dialectic forms: 'AheAAwv (Doric), 'AnsiAwv (Cypriot), 
A"ttAouv (Thessalian). - Seit J. Schmidt KZ 32, 327ff. all are linked to Cretan apsAioq Hes. 
(i.e. dFsAioi;) " sun '. It seems that the sun god 'AttoAAojv derived from Cretan apsAioi; Hes. 
(i.e. aPzhoc^) " sun '. The common in gr. Ai > AA has taken place. Both 'AheAAwv (Doric), 
'AnsiAojv (Cypriot), A'nAouv (Thessalian) and Cretan apsAiot; Hes. (i.e. aFsAiot;) " sun ' 
derived from the same root *sahue/' sun' where the common gr. hw > p, gw > b has taken 
place. 

Note: 

Khaskura gham (also Indie borrowing surj) " sun ', Gypsy Gk kham " sun ' : gr. aFeAioq 

reflect gr. -b- > -mb- > -m-. 

Maybe Etruscan aviT year ' a borrowing from gr. qFeAio^. 

References: WP. II 446 f., WH. II 553 f., Trautmann 251, A. Scherer Gestirnnamen 45 ff. 

Page(s): 881-882 

Root / lemma: sa-, sa- 

Meaning: satiated 

Material: Old Indie a-si-n-va-, asinvan^ insatiable ' (places ein Praes. *s9-neu-mi, *s9-nu-6 

ahead); 

Armenian a/-c»/r" "full, ausgewachsen'; had, /7aJoy"zufrieden' {*sadio-); 



gr. thematic present asrai "sattigt sich' (Hesiod; *S9-iS), athematic Wurzelaor. apsvai 
(Horn.) ' be satiated '; Aor. Inf. aaai " satiate ' and " satiated become', ewjjev (*riofj£v, Konj. 
Aor.), Fut. aasiv, etc.; a-aroc; ( *n-sa-tos) " insatiable ', a5r|v = Boeotian a5av 'bis zur
```


## [2026-09-14T01:23:34.060Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"sawel\\|sāwel\\|s√°wel\" AHD_watkins1985.txt | head -20",
 "description": "Find sawel in AHD Watkins"
}
```


### [2026-09-14T01:23:34.205Z] TOOL RESULT

```
131:The other celestial bodies recognized were the sun, sawel-, and the stars, ster-3. There is evidence from several traditions for similar designations of the constellation Ursa Major, though these may not go back to the earliest Indo-European times. The movement of the sun dictated the names for the points of the compass. EAST is derived from a verbal root aus-', “to shine,” as is the word for “dawn” (Latin Aurora), divinized since Indo- European times on the evidence of Greek, Lithuanian, and Sanskrit. The setting sun furnished the word for “evening” and “west”:
905:sawel-. Also s(u)wel-, su(a)el-, su(@)en-, sun-. The sun. Contracted from *saswel-. 1. Variant forms *swen-, *sun- in: a. Germanic *sunndn- in Old English sunne, sun: SUN; b. Germanic compound *sunn6én-dagaz, “day of the sun” (translation of Latin diés sdlis), in Old English sunnandeg, Sunday: SUNDAY; c. Germanic de- rivative *sunthaz, “sun-side,” south, in Old English sith, south, and sitherne, southern: SOUTH, SOUTHERN. 2. Variant form *s(2)wol- in: a. Latin sd/, the sun: soL’, SOL, SOLAR, SOLARIUM; GIRASOL, INSOLATE, PARASOL, SOLANINE, TURNSOLE; b. Latin compound sdlstitium, “a standing of the sun,” solstice (-stitium, a standing; see sta-): SOLSTICE. 3. Suffixed form *sdwel-yo- in Greek hélios, sun: HELIACAL, HELIO-, HELIOS, HELIUM; ANTHE- LION, APHELION, ISOHEL, PARHELION, PERIHELION. [Pok. sdwel- 881.]
997:sta-. To stand; with derivatives meaning “place or thing that is standing.” Contracted from *stag-. I. Basic form *std-. 1. Extended form *stddh- in: a. Germanic *stéd- J6n- in Old English stéda, stallion, studhorse ( < “place for breeding horses”): STEED; b. Germanic *st6d6 in Old English stéd, establishment for breeding horses: sTuD2. 2. Suffixed form *std-lo- in Germanic *stdlaz in: a. Old English st6/, stool: sTooL; b. compound *faldistélaz (see pel-3). 3. Latin stdre (third person singular present subjunctive séet), to stand, with its past participle status (< “sta-to-) and derivatives statira, height, stature, and statuere, to set up, erect, cause to stand: STAGE, STANCE, STANCH, (STANCHION), (STANZA), STATOR, (STATUE), STATURE, STATUTE, STAY!, STET; ARREST, CIRCUM- STANCE, CONSTANT, CONSTITUTE, CONTRAST, (COST), DESTITUTE, DISTANT, ESTANCIA, EXTANT, INSTANT, IN- STITUTE, OBSTACLE, OBSTETRIC, (OUST), PROSTITUTE, REST?, RESTITUTE, RESTIVE, SUBSTANCE, SUBSTITUTE, SUPERSTITION. 4. Suffixed form *std-men- in Latin std- men, thread of the warp (a technical term): STAMEN, STAMMEL. 5. Suffixed form *std-mon- in Greek stémén, thread: PENSTEMON. 6. Suffixed form “s¢d-ro- in Russian staryi, old (“long-standing”): STARETS. II. Zero-grade form *st- (before consonants). 1. Nasalized extended form *sfa-n-t- in Germanic *standan in: a. Old English standan, to stand: STAND; b. Old English understandan, to know, stand under (under-, under; see ndher): UN- DERSTAND; Cc. Old French estandard, rallying place: STANDARD; d. secondary zero-grade form in Germanic *stund-6 in Old English stund, a fixed time, while: STOUND. 2. Suffixed form *sé-tyo- in Germanic *stath- Jon- in Old Norse stedhi, anvil: strTHY. 3. Suffixed form *sta-tlo- in Germanic *stathlaz in Old English stathol, foundation: STADDLE, STARLING?. 4, Suffixed form *sta-mno- in Germanic *stamniz in Old English stefn, stem, tree trunk: sTeM!. 5. Suffixed form *sta-ti- in: a. Germanic *stadiz in (i) Old English stede, place: STEAD (ii) Dutch stad, place: STADHOLDER (iii) Old High Ger- man stat, place: SHTETL; b. Latin stati6, a standing still: STATION; C. Latin -stitium, a stoppage (in solstitium, solstice; see sawel-): ARMISTICE; d. Greek stasis, a standing, a standstill: sTAsIs; HYPOSTASIS, ICONOSTASIS, IsOSTASY. 6. Suffixed form *sfo-to- in Greek statos, placed, standing: STATIC, STATICE, STATO-; ASTASIA, ASTATINE. 7. Suffixed form “sta-no- in: a. Latin désti-
1247:ANTA aneta ANTAGONIZE ag- ANTE ant- ANTEBELLUM duellum ANTECEDE ked- ANTEFIX dhig¥- ANTEPENDIUM (S)pen- ANTERIOR ant- ANTHELION sawel- ANTHELMINTIC wel-3 ANTHEM bha-2 ANTHEMION andh- ANTHER andh- ANTHESIS andh- ANTHO- andh- -ANTHOUS andh- ANTHROPIC ner-2 ANTHROPO- ner-2 ANTHURIUM ors- ANTI- ant-
1252:AORTA wer-2 APERIENT wer-5 APERITIF wer-5 APERTURE wer-5 APEX ap-! APHELION sawel- APHONIA bha-2 APLANATIC pele-2 APLOMB plumbum APNEA pneu-
1560:GEODE gé GEODESY da- GEOMETRY mé-2 GEOPONIC (s)pen- GEORGIC gé, werg- GERANIUM gera-2 GERENT gerere GERIATRICS gera-1 GERM gene- GERMAN? gena- GERMANDER deru, dhghem- GERMANE gene- GERMINAL gene- GERMINATE gene- GERONTO- gera-1 GERUND gerere GEST gerere GESTALT stel- GESTATION gerere GESTICULATE gerere GESTURE gerere GET ghend- GEYSER gheu- GHAT gher-4 GHOST gheis- GIDDY gheu(e)- Girt ghabh- GILD! ghel-2 GILL! ghel-una GILLS ghai- GILLYFLOWER bhel-3, kar-1 GILT2 ghel-3 GIMMAL yem- GINGERLY gene- GIRASOL sawel- GIRD gher-1 GIRDLE gher-1 GIRTH gher-1 GIST yé-
1590:HELIACAL sawel- HELIO- sawel- HELIos sawel- HELIUM sawel- HELIX wel-3
1681:INQUIRE quaerere INSCRIBE skribh- INSECT sek- INSERT ser-3, s6-1 INSESSORIAL sed-1 INSIGNIA sekw-1 INSIST sta- INSOLATE sawel- INSOMNIA swep-! INSPECT spek- INSPIRE spirare INSTALL | stel- INSTALLMENT! | stel- INSTANT sta- INSTAURATION sta- INSTIGATE | steig- INSTINCT | steig- INSTITUTE sta- INSTRUCT  ster-2 INSULT sel-4 INSURE cura INTACT tag- INTEGER tag- INTEGUMENT (s)teg- INTELLIGENT leg-1 INTEND ten-
1691:Is es- ISALLOBAR gWere-2 ISCHEMIA segh- ISINGLASS bhié-2 ISLAND akwa- ISOBAR gWere-2 ISOCLINE klei- ISOGLOss glogh- ISOHEL sawel- ISOHYET seue-2 ISOMER (S)mer-2 ISOMETRIC mé-2 ISOPIESTIC sed-1 ISOPLETH pele-1 ISOSCELES skel-3 IsosTasy sta- ISSUE ei-1
2059:-PARA pere-1 PARABLE gWelg-1 PARABOLA gW¥ele-1 PARACHUTE pere-1 PARACLETE kele-2 PARADE pere-1 PARADIGM deik- PARADISE dheigh-, pert PARADOX dek-! PARAFFIN pau- PARAGRAPH gerbh- PARALLAX al-1 PARALLEL al-1 PARALLELEPIPED ped-! PARALOGISM leg-1 PARALYSIS leu PARAMECIUM mak- PARAMOUNT ad-, per! PARAMOUR amma, pert PARANOIA nous PARAPET peg- PARAPHERNALIA bher-1 PARAPHRASE gWhren- PARAPLEGIA plak-2 PARASOL pere-1, sawel- PARATAXIS tag- PARBOIL beu-! PARCAE pera-1 PARCEL pere-2 PARCENER pere-2 PARDON d6-
2061:PARGET per, yé- PARHELION sawel- PARI-MUTUEL pere-2 PARISH weik-1 PARITY2 pere-2 PARLAY pere-2 PARLEY gWelg-1 PARLIAMENT gWele-1 PARLOR gWelg-1 PARLOUS per-4 PARODY wed-2 PAROL gWele-1 PAROLE gWele-1_ PARONOMASIA n0-men- PARONYCHIA nogh- PARONYMOUS no-men- PAROTID GLAND ous- -PAROUS pere-) PAROUSIA es- PAROXYSM ak- PARRICIDE paso- PARRY pere-!
2079:PER- pert PERCEIVE kap- PERCENT dekm PERCH? perk-1 PERCOLATE kagh- PERCURRENT kers-2 PERCUSS kwét- PERDITION d6- PERDURABLE deue- PEREGRINE agro- PEREMPTORY em- PERENNIAL at- PERFECT dhé-1 PERFIDY bheidh- PERFORATE bher-2 PERFUME dheu-1 PERFUNCTORY bheug-2 PERFUSE gheu- PERGOLA perg- PERI- per! PERICARDIUM kerd-1 PERICLINE Klei- PERIGEE gé PERIHELION sawel- PERIL per-4 PERIMYSIUM mis- PERINEPHRIUM negWh-ro- PERIOD sed-2 PERIONYCHIUM nogh- PERIOSTEM ost- PERIPATETIC pent- PERIPETEIA pet- PERIPHERY bher-1 PERIPHRASIS gWhren- PERIPHYTON bheue- PERIPTERAL pet- PERISARC  twerk- PERISH ei-1 PERISSODACTYL per! PERISTALSIS | stel- PERISTYLE sta- PERITHECIUM dhé-1 PERITONEUM ten- PERITRICH _ thrix PERIWINKLE! weng- PERJURE yewes- PERMANENT men-3 PERMEATE mei-1 PERMIT (s)meit(a)- PERMUTE mei-1 PERNICIOUS nek-1 PERONEAL per-2 PERORAL 6s- PERORATE 6r- PERPEND (S)pen- PERPENDICULAR (S)pen- PERPETRATE peter- PERPETUAL pet- PERPLEX plek-
2273:SNIFF snu- SNIP snu- SNIVEL snu- SNOOP snu- SNORE sner- SNORKEL sner- SNORT sner- SNOT snu- SNOUT snu- SNOW sneig’h- SNUB snu- SNUFF! snu- SNUFFLE snu- SNUG! kes-1 sO swo- SOAK seua-2 sOAP_ seib- SOAVE swad- SOBER s(w)e- SOCIABLE sekw-1 SOCIAL sekw-1 SOCIETY sekw-1 SOCIO- sekw-1 SOCKET sU- SODALITY s(w)e- SODDEN seut- SOIL! sed-1 som? si- SOIREE sé@-2 SOJOURN deiw- SOKE sag- sol’ sawel-
2276:SoL sdwel- SOLACE sel-2 SOLANINE sAwel- SOLAR sawel- SOLARIUM sawel- SOLE! sel-1 SOLE? s(w)e- SOLEMN sol- SOLICITOUS_ kei-3, sol- SOLID sol- SOLILOQUY s(wW)es, tolkw- SOLIPSISM s(w)e- SOLITARY s(w)e- SOLITUDE s(w)e- SOLO s(w)e- SOLSTICE sawel- SOLUBLE leu-1 SOLUM sel-1 SOLUTE leu-1 SOLVE leu-! SOMA teue- SOMATO- teua- SOME sem-! -SOME! sem-1 -SOME2  teue- SOMERSAULT sel-4, uper SOMNI swep-! SOMNOLENT swep-! SON seue-! SONANT swen- SONATA swen- SONE swen- SONG sengWh- SONIC swen- SONNET swen- SONOROUS swen- sooT sed-1 SOOTH es- SOOTHE es-
2277:SOP seue-2 SOPOR swep-1 SOPORIFIC swep-1 SOPRANINO uper SOPRANO uper SORCERER ser-3 SORDID swordo- SORDINO swer-2 SORE sai- SORITES teue- SORORAL swesor- SORORITY swesor- SORREL! siiro- SORREL? saus- SORROW swergh- SORRY Sai- SORT ser-3 SORTILEGE leg-1, ser-3 SORUS teue- SOTERIOLOGY teue- SOUBRETTE uper SOUFFLE bhlé-2 SOUGH (s)wagh- SOUND! swen- SOUND2 swento- SOUND3 swem- SOUND4 swem- SOUP seue-2 sOUR siiro- SOURDINE swer-2 SOUSE sal-1 SOUTANE upo SOUTH sawel- SOUTHERN sawel- SOUVENIR gWa- SOVEREIGN uper SOVIET sem-! sow! sé-1
2326:SUMMON men-! sUMP swombho- SUMPTUARY em- SUMPTUOUS em- SUN sawel- SUNDAY sawel- SUNDER sen-2 SUNDRY sen-2 SUP! seue-!
2420:TUMID teue- TUMOR teue- TUMULUS teu@- TUNGSTEN | stei- TURBARY derbh- TURBID twer-1 TURBINE twer-1 TURD der-2 TUREEN ters- TURF derbh- TURN tere-1 TURNSOLE sawel-
```


## [2026-09-14T01:23:43.377Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"hvarə\\|hvar∂\\|hvarexšaeta\\|hvarə-x\\|x&ar∂nah\\|hvarenah\" BRT.txt | head -30\necho \"---- search plain\"\ngrep -n \"hvare-x\\|hvarexs\\|hvar. x\\|xsaeta\" BRT.txt | head -20",
 "description": "Grep Bartholomae for hvarə"
}
```


### [2026-09-14T01:23:43.452Z] TOOL RESULT

```
---- search plain
```


## [2026-09-14T01:23:45.682Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nwc -c BRT.txt; grep -n -i \"Sonne\" BRT.txt | head -20",
 "description": "Check BRT text"
}
```


### [2026-09-14T01:23:45.769Z] TOOL RESULT

```
4803500 BRT.txt
3220:der  Spitze  des  Satz(teü)es  stehend  (s.  No. 5,6);  i)  zeitlich 'dann,  darauf,  da';  ''fra- yaire  ayati  .  .  "oa  apare  ayqn  "am  Vor- mittag . .,  dann  (aber)  am  Nachmittag" Aog.5^;  V.  ii.4,  20.4,  N.5J,  F.7,Vt/9. 48;  —  -da  tala  giul  pir>sat  aspm  "da fragte  der  Schöpfer  des  Rinds  das  A."  Y. 2^.2;  — 'da  sl''  ,.  bavaiti  sk>ndö  spaya- %raAyil  (sd)  Y.jo.io;  —  ya%a  va/i  iäd.) ..*''öai^  aaAö  a/ava'V.yi.16.  a)  hinter yäoi:  yet'A  sT  hvar»  nöit  uzttxlyeiti  °oa  . . "wenn  (erst)  die  Sonne  nicht  mehr  auf- geht, dann  . ."  Yt.  6.3.  b)  "oo  .  .  °cit °'6a  'dann  wenn  .  .  dann':  "aa  syäscif pairipataili  'oa  fraistim  vöiynanqm  (sd.) V.  7.3.         a)  anreihend  'und,  und  auch':
3337:I  "wer  bestimmte  den  Weg  der  Sonne  und
4585:•  j,  +antar«.ar98am ''  Adv,  ('zwischen  den Seiten',  sva.)  1) 'innerhalb',  mit  Gen.:  °äjw zrayanhB  V.5.19;  —  ''(am  nmänahe  "V-ff. 33,  Yt./7.6o.  2)  'diesseits':  yas;/  iava masda  kirpnaot  tacar)  *nSit  *tacar>  *'Mm'^ upairi  Avanxsaiüm  "dass  dir  M.  eine Bahn  bereite,  nicht  eine  Bahn  diesseits, (sondern)  Über  dem  Sonnenball"  YL  5, 90.
4752:F.  ff;  —  :^ahe  gayehe  :^airvats{5A^  "sähe Y.5.1,  Yt-Äii.  a)  von  der  Sonne: hvan^ail>m  'hm  raim  aurvat.asp»m  Yt. 6.\,  4,  6; —  hvar>.xsaitahe  'sähe  ra^ahe Yt-ö-o,  Y.22.24J  —  paurva.naemäi  °hhe hä  yaf  aurvat.aspahe  Yt.  10. 1 3.  A)  ins- bes.  von  den  dem  AhuraMazdäh  nächst- stehenden Gottheiten*':  yaia  vahm>m 'iaiibyS  Y.  21.2;  —  -saHi  . .  avarshe  ismti masyäkänAs  Aog.  41.  a)  sonst  in  Ver- bindung mit  spitUa-  Adj.  'heilig',  das  in GHapL'vor-,  sonst  nachsteht:  *vyäX3mca kanjamanimca  (sd.)  yat  as  'sanqm  sp?nta- nqm  banlnvS  *avarihe  as/0  y?mat^m  (sd.)
4869:•  ).  ayan-,  j-,  g.  ayar-  n.  'Tag';  a) Gegensatz  zur  Nacht:  *oim  . .  'yar>  (NS.) tYjasaiti  .  .  a?va  v3  xsapa  Aog.  J/;  ■ — ai»ke  'yan  (GS.)  .  .  airikh  xsaj>ö  \t.  i .-iZ, i/.S;  Vyt.J0(?);  —  hamahe  °yqn  hamayn 1-3  xsa/w  Y.  S7-3I,  Yt.ÄS4;  '  10.  iij  (f), Vyt^f?);  —  vlspsU  'yqnia  (AP.)  xlaf- nas.'a  Y.  57. 1 7,  Yl  /.  i  i  ;  —  *frayaire  "yan (LS.)  bavaiti  (sd.j  hubai,rü  .  .  aia  apare 'y<pi  ■-  Aog.  35;  —  */rayarfne  vä  uza- yariu^fsd.)  va  *'yan''>  N.5;  —  dvadasati- hiinm  (sd.)  asü  *ayrim  °yar)  F.  27  b 27b;  —  °yqn  (LS.)  va  varstafsö  var»t3.vTrt [sd.)JaiJnti  V.S.^.  b)  als  der  Zeitraum von  Sonnenaufgang  zu  Sonnenaufgang: iiz£.a  yan  mainyenie yaty3r)N.2.^\ ^räyö  yara''  Vd.  ly;  <),  if),  si;  —  pasca xsavaidim  (sd.)  yaranqm^a'''  Vd.  f)\  11, '5>  '9  '■  c)  sva.  festgesetzter,  bestimmter Tag:  myazdahe  ''ya''''  (LS.)  "am  Tag  des My:'  N. Si-,  "y:;  *^jj  —  kaia  (sd.)  yiri (AP.)  daxiärS  .  .  drfs  Y.  43-  T,  —  yan ami^näitii&d.)  juye  tanus  Aog.^j.  d) 'Zeit':  vUpI  'yärj  (AP.)  dangö.jyäiöU (sd.)  .  .  "alle  Tage  . ."  Y.  43-  2.
4959:, .  Ailu  maza  m^rr/S  .  .  "ve  awrä  YL  z^.  *malnis  (sd.)  atiAat  pouruye  vTdv^  "vqm 41,  a)  mit  einem  ergänzenden  odsT  yä  im  af^Aaeapjma{^.)Y. 44.1g.  II)in erläuternden  Relativ:  'z'aj  karsvar}  _yff/' schwachdeiktischem  Sinn  'jener,  der'; *ar3zaAi  *savaAi  .  .  imat  iar^ar?  yat\  I)  auf  Vorhergenanntes,  Vorausgehendes :i^amra^sm  V.ip.^t);  39';  —  imS  /-irciv/ j  (Wort  oder  Satz)  zurückweisend;  i)  auf barizist^m  barszimanqm  °3raJ'>  yat  hvars  ein  Substantiv,  a)  adjektivisch,  auch  im avacT  "das  Licht  hier  (und)  jenes  Höchste !  Sinn  unsres  Artikels  (des  schwachtonigen unter  den  Hohen  dort,  was  Sonne  heisst"  'der'):  I  ka"bajiyJ' .  .  paruram  idä  xsäya- Y.  j6. 6.  2)    ohne    solchen    (ausge-  aya"  aAJ^  °vaAyü  k(fbüßyaAyS  brälä  bar-
5408:1)  'wert  sein,  Wert  haben':  j>.7cä  voha cühiiqm  anjal  mananhn  raoci  j^ing  "und was,  o  VM.,  durch  das  Auge  Wert  hat ", das  Licht  derSonne.."Y.  50.10.        2)  'an
8166:•  j.,  g.  "uxäan-  m.  'Männchen  des  Rinds, Stier',  in  Verbindung  mit  dem  Namen  flir Rind"';  gaoma?z)m  ..  gaom  pairi  °sC\n>tn V.  IQ.  21;  —  gSus  paili  'sttö  .  .  gJus  faiti azyä  . .  V.i».37  f.  a)  g.  mit  atnam  GP, 'Stier  der  Tage',  vom  FrühUcht:  raota :^^iig  asnam  -sä  alurus  "das  Sonnenlicht, der  schimmernde  Stier  der  Tage"  Y.  50. 10'*;  —  kad3  mazdii  y5i  'siinJ  asnam  .  . darj^rüi  frd  asahy.i  frärmtl ..  saosyaittqm xratavs  "wann,  o  M.,  werden  die  Stiere der  Tage  . .  herkommen"^  Y.jtf.j".
8590:•>  Genannt  uzayara- {%&,)  und  nach  N.  50  vom halbea  Nachmittag  bis  Sonnenuntergang  während. Vgl.  noch  Bd.  2J.  9  (wo  efiärai'))  und  zu  aiHya-, Ableit.  —  Ableit.  aus  uiayara-.  —  Pü. :  utayarin, Sü.:  aparShnaksamdkyah,  —  1)  Pü.:  roc  i  Jum fa  gät  i  Ungarin,  —  »)  S.  dawi  GIrPb.  /. 372  p).
8611:Zum  Praes.  5  des  V.  '("■- ').  —  Eig.  'Ausgangs-, Untergangs  zeit  des  Tags,  der  Sonne';  vgl zBed.  sä.  üditay-  f.  —  PiL ;  aarsärif).  —  ')  Vgl.
8705:—  'saiihqm  para  frSritSii  FrW.  /0,4i ;  — ytzi  xsapsAva  mpr^ncaiie  (sd.)  'lakva bisazyat  V.  l'7.3J  —  uü'  (LS.).  A)  als weibliche  Gottheit  gedacht:  'sqm  (AS.) sriram  yazamaide  'säuAfm  . .  xsSi'inJm ravaLaspqm  .  ,  "säPikem  .  .  nvim  ranjat.- aspqm . .  avqm  'sqm . .  G.  5. 5.  a)  Name der  fünften  und  letzten  der  (priester- lichen) Tages  abteilungen*';  vupim  paiti "sauham  ä  kB  vaxsat  "immer  in  der Morgenfrühe  bis  Sonnenaufgang"  V.  /y. I.  3)  mit  süra-  Adj.  Name  des dritten  Abschnitts  der  Nacht**':  hö tiurr/ö  (j'S  parö.dars)  väHm  baraili  upa 'iaukim  yqm  särqm  V,  iS.  15;  —  'sqm särqm  V.2j\}.
8706:*>  Die  von  Mittemacht  bis  Sonnenaufgang reicht  und  in  uSai-  (sd.  3)  sünU  und  rao/a/i/iiim fragalay-  (sd.)  lerlaÜt;  vgl.  'aiahna-,  F.  3/  b, N.  46  und  DsT.  ZA.  i.  zSl,  sowie  die  FüGI. lU  ul  und  u!  1  arinär  V.  rj.  1,  18.  IJ:  /a  n^m sap  iizäyil.  —  '*)  Der  von  Milleinachl  bis  lum Tagesgraucn  reicht  und  zusammen  mit  raolanhqm /iHi;alay-  (sd-)  die  fünfte  Tagesabteilung  uia/i- (sd.  2)  bildet;  s.  oben  *).
9670:I  2.  421,  ZDMG.  S3-  90.  Fov  ZDMG.  54.  361. Et.  und  Bed.?  Die  Perser  sollen  in  dem Namen  die  Bedeutung  'Sonne'  gefunden  haben ; s.  JUSTI  NB.  [68,  GlPh.  2.  417,  wo  m.  hyrr 'Feuer'  verglichen  wird;  s.  daiu  Uhlenbeck WAiSpr.  62.  VII.  nichtiraaiicher  Name.
10701:KonripA.,  E. ').  —    \'gl.  axsattta-,    - ■Sonne'.  —  Pü.!  rSht.  (lu  Y.  26J:  ; 2  a):  j-am  JS.  —  OS  20?-  2  »E-  —  ")  S.  noch unter  kvanxia^la-,
10792:—  paoiryh  dasa  'panS  (AP.)  ,  .  tUtryll .  . k3hrp3m  rai'kvjayäti  .  .  "während  der ersten  zehn  Nächte  . ."  Yti'.i3;  —  upa . .  jaymyam  aivqm  vä  avt  °param  duyz vä  .  .  YtÄir;  —  %raosta  'fiiS  '^rityayä Vtj.öz.  b)  als  Zeit  von  Sonnenunter- gang zu  Sonnenuntergang  Tag  und  Nacht, Tag'i>:  ta  'paiiö  (AP.)>r7  +>JÄ(  \. 62.10;
10802:•  j.  x§apar-  n.  'Nacht'  i)  im  Gegensatz zum  Tag:  yai  vä  ya'ia  *uzayamn  yai ya'i^a  'pamm^^  ti.47(?).  2)  als  Zeit von  Sonnenuntergang  zu  Sonnenuntergang 'Tag  und  Nacht,  Tag'  (nur  Komp.).
11783:•  j.   taera-  m.,   a   'Bergspitze,   Gipfel': 'rasca  barö.srayai0{%A.)\t.ig.6.       a)  sonst von  dem  Gipfel  der  Hara,  Haraitr.  upa 'nm  AarayiYtiS.T,  —  'nmcä  harai%ya hmS  Y.  42. 3;    —    upa    'r>m    Aarai'iya iarttS  yat    ml  aiwitö   vrvistnti   starasca masca  hvania  "auf  dem  Gipfel  desffaraitl- gebirgs,  um  den  meine  Sterne,  Mond  und Sonne  kreisen"  YL/2.  ss'^- Et?')  —  Vgl.  j/<wra-,  S  Sj.  a.   KZ.  29.  487. —  mp.  (Pu.)  tirai,  nbiL  fer  'Be^spitze',    afT. tir^  -spitz'.  —   ')  Vgl.  iSt.  Bd.  J.  4:    /Frai  i hatiurz  Ja  ölt  i  man  ^ariil  u  mäh  u  itäraiän kacpai  afäivartit.  — ')  Falsch  Go».  ABajrAW. so.  I.  189.
11915:j  machen  (Jmdn.  sva.  es  Jmdm.)':  täpayäii mqm  asa  vahista  mqnayfn  ahe  ya%a nyaoxivst)m  Hx.1-.2q.  a)  absolut  'Wärme bringen,  schaffen',  von  Sonne  und  Mond: yai  hvara  raoxlne  täpayatt  \t6.i\  i,  7.4.
13403:*)  Die  Zoologen  des  Awesta  haben  offenbar die  Puppen,  die  die  Ameisen  in  die  Sonne  tragen, für  geraubte  Getreidekürner  angesehen.
14414:mit  »J 'herausschneiden':  wjt'dÄ? (näml.  avai,ihe  hü  'ts  {!&.)  i^Arpya  "bevor  jene sBnö)  gaostm  %w?nsaiti  V.  13. 10.  Sonne  dort  in  ihre  sichtbare  Gestalt  hinein-
```


## [2026-09-14T01:23:54.128Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"hvar>\\.xsaita\\|hvar>.xsaita\\|hvarixsaita\\|hvanxsaita\\|hvanxia\\|kvanxia\" BRT.txt | head -20\necho \"===\"\ngrep -n \"hvar>n\" BRT.txt | head -20\necho \"=== xvarenah\"\ngrep -n \"x'ar>nah\\|x.ar>nah\\|var>nah\\|far>nah\\|farnah\" BRT.txt | head -20",
 "description": "Grep BRT for hvarəxšaēta and xᵛarənah"
}
```


### [2026-09-14T01:23:54.222Z] TOOL RESULT

```
4752:F.  ff;  —  :^ahe  gayehe  :^airvats{5A^  "sähe Y.5.1,  Yt-Äii.  a)  von  der  Sonne: hvan^ail>m  'hm  raim  aurvat.asp»m  Yt. 6.\,  4,  6; —  hvar>.xsaitahe  'sähe  ra^ahe Yt-ö-o,  Y.22.24J  —  paurva.naemäi  °hhe hä  yaf  aurvat.aspahe  Yt.  10. 1 3.  A)  ins- bes.  von  den  dem  AhuraMazdäh  nächst- stehenden Gottheiten*':  yaia  vahm>m 'iaiibyS  Y.  21.2;  —  -saHi  . .  avarshe  ismti masyäkänAs  Aog.  41.  a)  sonst  in  Ver- bindung mit  spitUa-  Adj.  'heilig',  das  in GHapL'vor-,  sonst  nachsteht:  *vyäX3mca kanjamanimca  (sd.)  yat  as  'sanqm  sp?nta- nqm  banlnvS  *avarihe  as/0  y?mat^m  (sd.)
10701:KonripA.,  E. ').  —    \'gl.  axsattta-,    - ■Sonne'.  —  Pü.!  rSht.  (lu  Y.  26J:  ; 2  a):  j-am  JS.  —  OS  20?-  2  »E-  —  ")  S.  noch unter  kvanxia^la-,
27542:—  ana  bansmana  imqm  'rqm  ayese  yesti Y.  2. 1 ;  —  imq  haomqs^a  myazdqs^a  'rasca bansmaca  . .  pairica  dad?mahl  Hca  vasia- yamahiY.4.1;  —  anahität  pars  bansmgn anähiiayat  pars  'rayät  Yt  10.  88;  — hvanxialtim  .  .  yasamaide  haomayS  gava bartsmana  ..  'rabyasca  Ny.7.16;  —  aisa 'ranqm  mazUtaia  . .  yä  *naire  a^aone *dasle  li.84; — mä  eis  ml  ankam  'ranqm fratauharät  Ytio.izi;  lao;  —  m3  ml aSayasHt  'rayä  /rarthartntu  .  .  Yt5. 93; 91,  92; —  hpm  loa  tl'rä  bavainti{Sp.  939 m.)  yasf  tava  .  .    Ytj.  94;    —    a^a   ml
===
=== xvarenah
```


## [2026-09-14T01:24:02.151Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"r>nah\\|rjnah\\|r?nah\\|ranah-\" BRT.txt | head -20\necho \"=== glanz/majestät\"\ngrep -n \"Herrlichkeit\\|Glanz.*Würde\" BRT.txt | head -10",
 "description": "Grep BRT for xᵛarənah variants"
}
```


### [2026-09-14T01:24:02.223Z] TOOL RESULT

```
6557:•  j.  asjt'aranah-  Adj.  'sehr  hoheitsvoll, höchherrlich':  mq>rB  sptntB  yd  'n3  Y.ig. 16,  22.  2,  6,  Yt/2.2;  —  mq'inm  sp>nt9m ^'nanhfm"  Y. 2. 13.
6975:•  j,  a-x^arata-  Adj.  'unfassbar,  unnahbar', vom  i^ar>nah-  (sd.):  tr/rpin  °tPin  d'annö mazdaiätfm  .  .  yahmi  paiti  ''parix''äi>e (sd.)  sp>ntasca  mainyui  anrasca  aäahmi paiti  at  'te  Y.%.  ig.  A,li.;  —  atari  .  .  uiti . .  mankanö  a3at  si'ar^nB  hangpr»/s3ne  yal 'fymYt.iff.4j;  — <'^I  vS  kascit  malyänqm id'artttS  "tsm  isaSta  Yt. /p.  53;  —  käva- yeheca  x''armar>hu  .  .  'taheca  ^farftta^hs mazd^ätahe  Y.  j.  14;  S.  i.  25,  Y.  2. 14,
19107:Anrufung*:  kva  asli  vfrikrarjnahe . .  'zbäitiS  No.  30.
20195:•  j.  mazda-JIata-'l  Adj.  (fem.  'ia-)  'von Maadäh  geschaffen':  vTspa  voha  Ha  (APn.) asacihra  (StvKz.)  Y.  ig.  3  usw. ;  —  vtspäca ääma  Ha  a/at>rir/  Y.jl.6;  —  sav^  °i?m Y.2.14;  /.14,  Ny.^.j,  S,/.9,  2.9;  —  yatäi laoka  ..  Ha  (als  VS£)  V.22.3;  Yti.  21, S. /.  3,  2.3;  —  A<&ra  saoke  -lätle  {\SU) Yt.  1-2. 4;  —  raiaia  vamthi  Ha  (NSf.)  V. /ß.  1 9 ;  S,  I.  5,  2. 5,  VyL j(*;  — ■  sl'arinaTihaca Ha  (IS.)  Ytro.67;  V.J.  i4i,  Ny.5.s',  6, S./.a5-, -'.9',  Yli?.6s,  134,  14.3',  19.9, 13';  —  airyanam  x^ama  'tätanqm  (statt A5n,)  Ny.5.  5,  YtJÄo;  —  v^n^raryrom *t3m  V./5.  37';  —  rumH  urvaire  . .  'laile (VSf.)  V.  jg.  18;  Y.  1. 12,  2. 12,  Ny.  4-  o, N.  7/,  p7,  VyL22;  —  aptmca  HqmH.2.%\ I-  S.  I a.  .?■  3'.  '^-  4.  65. 7,  ffÄ  7,'Yt  y.  53, V.  /p.  35,  Ny.  4.  o',  S.  2. 10,  FrW.  7.  i;  — S/y  V(7  (ASf.)  alaonll  Y.2.  la';  —  ^ii«»- k»r>nahe  ..  °take  Vt.  /.  30;  30,  S.  /.  7,  2.  7;
22954:betätige"  \.3i.\i;—y7  dät  manö  vahyS  *  'varanah-  n.  -?-:  mä  ^wä  ..  ästi-
24544:•  j.  vispö.x''aranah-  Adj,  'der  alle  Hoheit, Herrlichkeit  besitzt':  vispö.va^wu  .  .  °nd (NSm.)->  Vt;Ä4-
27051:•  j.  spitavaranah-  ■'  m.  Name  eines Bergs  oder  Gebi^s:  ahmal  haca  garayO /raoxsyqn  . ,  -näsca  Yt  ig.  6,
=== glanz/majestät
2703:*aevö.gava-'>  Adj.  'einhändig:  ya>a\     Nur  Med.  i)'Herr  sein,  verfiigen  über-, paaunö    'vö  afnö-armö  raaAam  *avajia-  zu  rechnen  haben  auf-'  (Gen.)  tistrim.. yänttm  'savavä  ä>t  eis  äUe^'v.33'\         ,isanpm  /iazar»räi  (statt Oen.):  ayapianam ISi.-.  tvai  göii).—  »  Bei  DsT.  'savö;  vU.  ist '"den  T.,  der  über  tausend  Herrlichkeiten das   Wort    mit   dem    zweiten   (-Zeichen   ge-,  verfügt"   YLA49;    —    kat   möi  vrvä    isl Sin''„'t"srenc'isrJnki^nin^^^^^^^  l^hyä-va^ho  "ob  meine  Seele
7361:—  upa.barat  "tim  Vyt.jiV;  —  ix^a/imi dam  . .  aire  . .  ^ahmi  't.m  yat  ahurahe mazäii  Vr.  14. 2  (?).  2)  Plur."  'GlUcks- güter,  Herrlichkeiten,  Wonnen,  fehcitates': tiltrlm  .  .  isänim  hataaräi  °tanqm  yO daoäiti  ..  'lä  jairiyantiJi  Yt.  Ä  49;  —  vts- panqmca  paiti  'tanqm  Yty,  t35;  — yat da'iat    'ta    Vyt  25;    —    viT.H>rpm    dtm
7366:—  maiby5  dilvöi  ahvä  astvatascä  kyatcü mananhs  °t  7  a/Jt  halii  "verleihet  mir  durch Asa  die  Herrlichkeiten  beider  Welten,  der leiblichen  und  der  des  Geistes"  Y.  2S.  2 ;
7367:—  yaJ  hsi  äat  'tä  a/^U  hata  ahurö  . hranhfvim  (sd.)  Y.^y.i;  —  daidl  alfJ tarn  aüm  vaa/iSus  'di  manarfhs  "verleih, o  Aia,  den  Lohn,  die  Herrlichkeiten  des guten  Sinns"  \.■2K^^.  3)  'Almosen' (nur  Komp.).
8057:men,  die  Fr.  . .,  damit  es''  in  Besitz  des Besseren  gelange,  den  Angreifem  wider- stehe, Reichtum  und  Herrlichkeit  weiter -ermehre"  Y.  60.4.
11082:(yascd),  V,?.  70,  ij.4  (ymca);  —  iäsca imä  nämSnJs  "so  lauten  die  Namen" Vt  /.  15;  75.  49;  —  Hsca  caraitis  ahi yqm  ..  H.2.  io(?).  Anhang.  Ellipse ist  anzunehmen  für  gAw.:  vaidä  tat  ya ahmT  .  ,  anales  (sd)  tna  kamnafsva  (sd.) hyatlä  iamnänä  (sd.)  ahmT  "ich  weiss  das, weshalb  ich  , .  nichts  vermag;  nur  wenig Herden  sind  mein,  (deshalb  ist  es  so) und  weil  ich  nur  wenig  Leute  habe"  Y. 46. 2.  C)  In  der  Bedeutung  unsres 'auch';  ca  folgt  dem  angeknüpften  Satz- teil, bz.  dessen  erstem  Wort.  B)im  Aw.; 'auch'  hat  den  Sinn  von  i)  'ebenso,  eben- falls, nicht  minder' :  ^<«ji  mi^r>m..yazai vasram  .  .  yasäi  Aojoörpmi^a  yat  attt  . . Yt  6'.  5;  —  mai  vi  padäis{si.)  . .  paiti- fasai  .  ■  al  va  aridrahyala  n>manha  at vi  ..  AunarptatäY-SO.S;  —  tara^uänm ..hyathei  Im  caratasca{Sf.$(>$M.)aodiir?f^ä sSiS?na  vazä  V.jr.ia.  a)  Ellipse  liegt  vor in  gAw.:  vahiSta  tstii' {sA)  , .  tara%usttake .  .  yezT  hsi  dat  ayaptä  . .  ahurö . .  hvaivhf- vlm  (sd)  yaZcä  hsi  dabm  .  .  ". .  des  Z.: dass  ihm  nämlich  AA. ..  die  Herrlichkeiten verleihen  wird  . .  (So)  auch  denen,  die . ." Y,  $3.  I.  a)    'überdies,    ausserdem':
13313:•  j.  *däitim''  Inf.  'zu  geben,  zu  verleihen': vasa%a  aht  xiayamna  taiiuye  x''an»at»Ae''> d'  "nach  Gefallen  vermagst  du  deinem Leibe  Herrlichkeit  zu  verleihen"  Yt  ly.  1 5  3>.
16778:mächtigen', mit  Akk. :  nöij  tat  x^artnS pairi. abaom  (Augm.)  "nicht  vermochte ich  mich  dieser  Herrlichkeit  zu  bemäch- tigen" YL  ig.  57;  64  (wo  pairi.abavat, Augm.).  3)  'zum  Abschluss  kommen': kva  ta  dä%ra  (sd.)  pairi.bavainti  V.  ig. 27.  Wertlos:  yai  .  .  ^akwärS  mäaAlS pairi  dasa  ayara  bavaiti  (soll  heissen) "wenn  vier  Monate  und  zehn  Tage  (seit der  Empfängnis)  vergangen  sind"  Vd.  i^'**.
16924:•  j.  barat-äyspta-  Adj.  (fem.  •«-)  'Gliicks- gllter,Herrlichkeiten  bringend,  vers  chaffend': saoiqmca  barat.avantqm  'tarn  Vl  /J.  4a. ■  j.  baratzao&rä-  Adj.  'Z.  bringend,  dar- biingend':  raästam  astqm  'hrqm  Ytio. 126,16.1.
16952:•  j.  barö.x'ar3nah-  Adj.  'der  Hoheit, Herrlichkeit  besitzt,  gewinnt':  virihraymm . .  'nS  masd{^t>m  V,  ig.  37.
```


## [2026-09-14T01:24:10.705Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"x''ar3nah-\\|x'ar3nah-\\|x''ar»nah-\\|x^ar3nah\\|x''arjnah\" BRT.txt | head -20\necho \"=== farnah OP\"\ngrep -n -i \"farnah\\|frn\\b\" BRT.txt | head -20\necho \"=== hvar- Sonne entry\"\ngrep -n \"hvar»-\\|hvar>-\\|hvarj-\\|'Sonne'\" BRT.txt | head -20",
 "description": "Find BRT main entries"
}
```


### [2026-09-14T01:24:10.821Z] TOOL RESULT

```
16952:•  j.  barö.x'ar3nah-  Adj.  'der  Hoheit, Herrlichkeit  besitzt,  gewinnt':  virihraymm . .  'nS  masd{^t>m  V,  ig.  37.
24037:•  j.  vi8at.x''ar»nah-  m.  EN.  eines  der sechs  Genossen  des  Saesyant  bei  der Auferstehung  und  Ratav  des  Karsvar Vidata/sa  (sd.)'':  °na>9hs  alaonS  Yt jj.  1
=== farnah OP
2347:FD.:  Pamir-Dialekte. (PD)s. !  Sariion. (PD)i. :  A>r. (PD)W.:  iVaxU (FD'jjd.:  YidiäA. (PDfrn.;  Yatititi.
26238:säslär,  erl.  (zu  V.  p) :  Me  apar  andahiht  4)  dät eslel,  (zu  Y.  16) :  lik  anäkih  . . ;  Sü. :  anyäyi, Npü. :  iikananda  kär  u  jiifJ #  (s.  dazu  Bakthe- 1.EMV  Gab.  S7)-  —  ')  So  die  lect.  diff.  in Ptl;  aus  ir.  ••^■f.äm,  %  36S.  39;  zSchr.  'Ira- nifrn  m  F  1  vgl.  ätravaxi'  neben  ätriv'  (sd., No.  1).  —  ')  Es  spielt  hier  vll,  ein  andres sästar-  rail,  das  zu  läJra-  gehört.  —  3)  Them.  — 4)  S.  tu  vayöi.
=== hvar- Sonne entry
5566:•  j.  'airyaman-  m.  Name  des  mit  J  (7/r- ,  •  j.  'aurvataspa-  Adj.  'der  schnelle ysmä  isys  beginnenden  Gebets  Y.54.1:  Rosse  hat';  a)  von  ^rar-imd  Äj'ari>.tiiji^u-: 'matiim  mq^ranqm  maBittm  Yt.j.5;  —  Är'ur?  "toffi  YL/0.90;  6.4;  —  'tun  bavähi T-3r/irayn3m. .  ya^asli  antan  ahuna(&A.)  yaia  kiari  Az.  6";  —  am.nakc  hü  yat 'manaiAD.)Vi.24.i;*li.ioj.  a)  sonst |  Vn^  YLJO.  13;  —  hiarsxsaS^m  'ptm mit  isya-.  'mamm  isim  .  .  ßäsB  mq^fvm  Yt  6. 1,6, 12.^4, 1^.81,  \.  16.4;  —  hvar>- ..  b»r?am  Aa',aoxt?m  Vr.2.10;  G,/.6,  S.j^/attJj  °päi  Y.ÜÄ22;  —  hrerixiaiiahe 2.3;  —  tfm..  vJspanqm  sravanhqm  ufard.-\ ..  -pake  Yt.  Ö.o,  Y, 22. 24;  /.  11;  —  Iwan- kainm  fradaiqm  yim  'mamm  tsim  FrW. '  xsaiia  'pa  (VS.)  V,  j/.  5,  b)  von  apqm 4-1',  1 ;  —  'taan^m  isim  . .  maiisüm  o/aAe  napät-.  apqm  napa  -ps  Yt  ig.  51';  — sra-.arahqm  Y.54.2;  Vr.  24,1;  —  °manS  aPqm  napättm  'ptm  Y.  2. 5;  —  apqtn isyehe  hafu{iitä..'manö  isyeke ,.  haililca  ..  nap5  °pa  Y.65.13.  'pä'a  VyLjJ, Vr.24.2;  /.8,  S.7.3.                                    4'>"(?).
9670:I  2.  421,  ZDMG.  S3-  90.  Fov  ZDMG.  54.  361. Et.  und  Bed.?  Die  Perser  sollen  in  dem Namen  die  Bedeutung  'Sonne'  gefunden  haben ; s.  JUSTI  NB.  [68,  GlPh.  2.  417,  wo  m.  hyrr 'Feuer'  verglichen  wird;  s.  daiu  Uhlenbeck WAiSpr.  62.  VII.  nichtiraaiicher  Name.
20537:*)  Eine  utsche  Götterfigur,  ursptüDgticli  eine Sonnengottheit  (Oldenberq  Rel.  d.  V«da  4S,  190. HiLLEBKANDT  Ved.  Mylh.  j.  128).    In  den  ap.  In- schriften erscheint  der  Name  Äf.  erst  TattArta- xirjcfs  11.;    Darios  L    und   Xerxet  1.    erwähnen der   Gottheit   nicht,    auch   im    gAw.    wird    sie nicht  genannt.    Ich  nehme  an,  dass  M.  in  der Etrengiardäifi/rischen  Lehre    als  Gottheit    nicht anerkannt   war,    ebenso  wenig  wie    iB.  Uaoma (sd.).    Da  aber  der  Glaube  an  M.  im  Volke  lu fest  wunelte ,  waren  die  Priester  späterhin  ge- nötigt, seine  Verehrung   zuzulassen.     Bekannt- lich  hat  sich  alsdann  der  ^-Kiilt  bis  weit  ins Abendland  hinüber  verbreitet     Vgl.  WlNDlsCK- MANN  Mithra  (AKM.  /),  Dst.  ZA.  2.  441. KompA.,  E.  (in  Ableit.);  Abieil,  (s.  •ni^ray, •ml%ranya^  —  Et.  ?  Vgl  Uhlenbeck  WAiSpr. 223,  Bgm.  GrGr.3  74_>'o.    —    aL    ruiträ-   m. 1)  'Freund',    2)  ein  Adilya;  np.  Wir 'Sonne'; a.  noch  p.EN.  Mnpalinn,  fl/lr/>ayii?  USW.  —  Vgl. v^umiia:   —  Pü. :  mihr  (geschr.  ralnn  oder mlnnk);    SüErl.    lu    Y.   16%     mailripalih.     — ')   Erst    in   Inschriften    des  4.  Jahrhunderts ; 2mal    ist   w'a-V,    imal   {Am.  4)   m'>r"    ge- schrieben.    iSchr.  mit   %'r'  s.  Bthl.  BB.  9. 131,  Hbu.  KZ.  jfi.  177;    auf  die  Schreibung mit  fir^  irgend  welche  Schlüsse    aufzubauen, wie  KZ.  36.  571   geschieht,  halte  ich  für  ver- fehlt  —  »>  S.  »i'Ja  No.   3.   —  3)  Hds.  Vo.   — 4)  Zweifellos  eine  aus  arischer  Zeit  stammende Verbindung. •  j.  "miSrö.aoJah-   Adj.  'falsche   Rede führend'   oder  'den  Mfyra   betrügend"'; mi^rfm  .  .  ye^Ae  dar/jä^i  bäsava  /ra-
```


## [2026-09-14T01:24:26.295Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v5_pages.txt BQT_v1_pages.txt BQT_v2_pages.txt; do echo \"== $f\"; grep -c \"\" $f 2>/dev/null; head -3 $f 2>/dev/null; done",
 "description": "Inspect BQT page files"
}
```


### [2026-09-14T01:24:27.350Z] TOOL RESULT

```
== incoming/BQT/BQT_v3_pages.txt
51425
[pdf page 1]
[NOT OCRED - use tools/ref_page.py]
[pdf page 2]
== incoming/BQT/BQT_v4_pages.txt
22553
[pdf page 1]
[pdf page 2]
ه
== incoming/BQT/BQT_v5_pages.txt
10090
[pdf page 1]
5
[pdf page 2]
== BQT_v1_pages.txt
32486
۱ ۵ ۱! ۱
7 موم ۳ لام
م ۱ 0 و طق صفرررنیاعدریرماروی
== BQT_v2_pages.txt
41071
                                         ‫‪7‬‬

                          ‫رن‪۳‬‬
```


## [2026-09-14T01:24:30.154Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\n\"",
 "description": "Full BQT ref info"
}
```


### [2026-09-14T01:24:31.587Z] TOOL RESULT

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
```


## [2026-09-14T01:24:37.467Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nawk '/^\\[pdf page 472\\]$/,/^\\[pdf page 473\\]$/' BQT_v4_pages.txt | head -80",
 "description": "BQT vol4 pdf page 472 (printed 2389)"
}
```


### [2026-09-14T01:24:38.593Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:24:41.375Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\ngrep -n \"pdf page 47\" BQT_v4_pages.txt | head; echo \"---\"; awk 'BEGIN{RS=\"\\f\"} NR==472 {print}' BQT_v4_pages.txt | head -60",
 "description": "Extract BQT v4 page"
}
```


### [2026-09-14T01:24:42.439Z] TOOL RESULT

```
1768:[pdf page 47]
19154:[pdf page 470]
19191:[pdf page 471]
19229:[pdf page 472]
19272:[pdf page 473]
19310:[pdf page 474]
19353:[pdf page 475]
19390:[pdf page 476]
19428:[pdf page 477]
19481:[pdf page 478]
---
[pdf page 472]
۳۸۹ خور
هوختی! -» با تالی مجهول بر وزن نیز گوبند - وبفتح اول وئانی‌هم درعربی کوهان
سوختن, بممنی‌ب رکشیدن وبیرو نکشیدن و آمدن | شترا میگوبند وآن جمع هوده باشد۹ .
وییدا شدن باشد. ۱ هودر « نم اول وسکون ثانی‌مجبول
هوخمت؟ یسم اول و ثانی مجپول ‏ وفتح دال‌ورای بی‌نقطةٌ ساکن, حرچیز زشغت(۱)
وخای نقطه دار وسین بی‌نقطه و فوقالی » بممنی وزبون راگوبند - ومردم بدروی وبدقیافه‌را نیز
هوخت است که بیت‌المقدی باشد. گوبند؛ وبقتح اول هم بنظر آمده امت۷ .
هوخیدن؟ - بروزن کوشیدن,بسمنی هودل۸ - بکر ثاك بروزن موسل,
برکشیدن و بیرو ن کشیدن وپیدا شدن و آمدن | بممتی رسد باشد چه و دلبند رسد بند را
باشد. . گونند و رسد گاه جابی است که حرکات افلاك
هو - بنم اول ر سکون نانی مجهول و کواکب را درآنجا ضبط میکند .
ودال ایجد, رکو ولنةٌ سوخته را کویند که بر هموده؟* - بانانی مجبول بروزن‌سوده.
بالای سنگه آش زنه نهند وچخماق برآن‌زنند بمعنی حق وراست و درست باشد چتانچه یبهوده
تاآتش درآن افتد۴ - وجامه‌ای را نیز گفته اند 1
که نزدیك بسوختن رسیده وزرد شده باشد ۴ - احق وباطل وحرزه را کوبند - و پستی کهنه
و با ثالی معروف , نام پیشمبرست مشهور ه - هم بنظر آمده است که در مقامل لو باشد .
وبفتح اول» درعربی بمعنی توب کردن وبحق باز هور < بضم اول وسکون ثالی مجهول
کمتن باشد - وازدین بر کشتن وجهود شدن را | ورای قرشت, نامی‌است ازنامهایآ فتاب‌عالمتاب*۱

(۷) خم۳:۱ بد.

۱ < هوخیدن «رشیدی» جهانگیری بممنی‌فوقآورده قس: هیخدن درهآهیشتن» (ه.م.)

۴ - ظ. مصحف «هوخت» ( << دژهوخت) ورك: دژهوخت . دژهومت.

۳ <هوختن (هم.) « رشیدی > - ۴ - ر4: برهود « جهانگیری > ۰ پرهود
«رشیدی» - 8 - « هود بالضم» نام پیغمبری, هو هودین ءامرین ارقخشدین سام بن‌توج .>
«منتهی‌الارب» . ‎٩‏ - رك : منتهی‌الارب» محیط المحیط . ۷ - «هودر بوزن نوذر,
زخت‌رو باشد . کذا فی‌المید» «سروری» دررشیدی «هوذر (با ذال معجمه) چیزی بد وزشت» .

۸ - برساختهٌ دساثیر» رك: فرهنگه دساثیر مر۲۷۹: خودل, هودل‌بند.

‎٩‏ ددم (وم.). ۵ خور(ه.م.). اوستا 11۷2 3 اسفا۱: ۲ ص۹۹۸ کردی
۳ د«اسشق ۵*۵ درزبان آزمتی815 (املا بممنی آتش) 13 براهامیان» . رك: فاب۱ ۰۲۵۸
بشتها چ۱ 1۳۳۸۰۱۸۰ ج۲ ص۳۱۸

‏که شیری تترسد ز يك دشت کور ستاره نتابد هزاران چو هور .
8 فردوسی طوسی «لفت فری ۰۹۱۸۳

‏چوحورم نهان وچوٍ هور آ شکارا وليك‌ازحقیقت له حورم» نه‌عورم .

‏«سنائی غزنوی. دبوان ص۲۹۹ ۰
```


## [2026-09-14T01:24:50.362Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==183 {print}' BQT_v2_pages.txt | head -70",
 "description": "BQT vol2 leaf 183 (printed 723)"
}
```


### [2026-09-14T01:24:51.683Z] TOOL RESULT

```
  ‫واح‬   ‫جع‬                                                                                               ‫خرافات‬

 ‫خوش راهم کنته‌انده ‪ -‬ویمعنی شادی وشادمالی‬                                                         ‫حنایقبطیه ‪٩‬‏‬
 ‫هم‌آمده است‪ -‬وبمعنی‌مهمالی وضیافت! ‪-‬ومرردة‬                ‫خر افات = بفتح اول و بافا(‪ )۱‬بر‬
                      ‫‪.‬‬    ‫بمهمالی طلبیدن همهت‬
                                                        ‫وامربوط را‬
                                                                 ‫‪.‬خنان پریشان ن‬
                                                                              ‫وزن کرامات م‬
 ‫خراهر ود ‪ -‬نوعی از امرود برزکه‬                            ‫گوند عربی‬           ‫اول همآمده است‬      ‫گوبند ؛ وم‬

         ‫)‪ (4‬می هزه باشد ‪۱‬‬          ‫ناهموار(‪ )۳‬و زشت‬                                                     ‫است ؟ ‪.‬‬
‫‪ ۰‬خرامقان = بفتح اول مویم وقاف بر‬                          ‫خراك ‪ = ۴‬بفتح اول بروزت هلاك »‬

‫وزن قرابتان » رستنیی باشد مانند سنبلالطیب ‪.‬‬             ‫صدا و خراخری که بسبب کلو فشردن از کلو‬
‫مایل است و بخ آن هم‬             ‫اما رنگگ آن ببزی‬        ‫با درهنگام خواب از بینیآدمی برمی‌آبد ؛ وبا‬
‫بسنبل میماند وبوی ستبل‌لیز دارد وطبیعت آن‌هم‬                                            ‫مشدید ثالی همکفته‌اند ‪.‬‬
‫ادوكلی ‏‬
       ‫زديك امت بسنبل و درطعم وحیلان‬                       ‫بروزن‌نظام ‪ ۰‬رفتاری‌را گونند‬        ‫س‬   ‫خرام‬
                                               ‫باشد ‪.‬‬
                                                           ‫که از روی جاز و سر کشی و زببابی باشد ‪- ۴‬‬
 ‫ارمین "د راه رفتن بناز وتف‬   ‫خ‬                            ‫وخوش رو وجمیل و زدان خوش‌صورت وشکیلرا‬
                      ‫وزیبایی باشد ‪. ۸‬‬                     ‫)‪(1‬‬       ‫و خبرهای‬    ‫دز کفته‌اند ‪ -‬ونوید ومدگالی‬



        ‫(‪ )۳‬چش‪ :‬اهنوار ‪.‬‬                  ‫‏(‪ )٩‬چك‪ .‬چش ‪ :‬چیزهای‪.‬‬                      ‫وفا‪.‬‬   ‫چش ‪:‬‬   ‫(‪)۱‬‬



                                                                             ‫(‪ )4‬چك چش ‪ + :‬و ‪.‬‬

                                             ‫‪ « 661۲۵۳۵۲ ۱‬لك س ‪۱٩۲‬‏ رك‪ :‬خراتین ‪.‬‬
 ‫«خرافة» کنمامة‪ .‬آلچه‌چیده شودموه ‪ 4‬ونام‌مردی یری زاده ازقسلة عذرة و اوآ لجه ازیر بان مل وش‬

   ‫هن احد بت‬        ‫و گفتندی‬   ‫آبرا بدروغ می‌داشتند وهر سخن اورا پاور نداشتندی‬              ‫شل مبکرد »‪ .‬ومردم‬

  ‫‪۴‬‬           ‫» ‪۳‬‬   ‫ظ منتهی‌الارب‬       ‫لب‬    ‫خرافات حکات‌ای‬         ‫خرافة ‪ ۰‬ای هی‌حد بت مستملح کذب ‪ ۰‬و‬

                                                                                ‫«خراخر («‪.‬م‪۰ ).‬‬     ‫فی‪ :‬خرخر‬

                                            ‫در فرهن‬              ‫‪-‬‬    ‫‪۵‬‬          ‫کین رك‪ :‬خرامیدن‪.‬‬
  ‫گها خرام را بمعنی وعد ونوید‪( .‬و مانند آن)‬


  ‫ضبط کرده‌اند ولی اشمار ذبل تاصرخرو وبض شعراء دیگر شان میدهد که خرام بمعنی وفای‬
                                                 ‫بوعد و دمرقابل نوید استعمال میشده» له بمعنی وعد ‪:‬‬
             ‫را ‪.‬‬     ‫امش‬
                        ‫خشرمر‬
                            ‫آراسته با‬                                 ‫چون داد توبند رلج و دشواری‬
   ‫«اسرخسرو »‬
             ‫نوبدی که آ را لباشد خرامی ‪.‬‬                              ‫نوبدت دهد هر زمالی بقردا‬
   ‫‪« .‬ملقات دبوان ناصرخسرو ص ‪۵۹5 ۵‬‬              ‫ناسر خرو‬

 ‫‏‪ - ٩‬اسدی کوید ‪ « :‬خرام ‪ ۰‬کس دیگر بمهمالی بردن بود بعد از نوید ‪ .‬فرخی (سیستالی) گفت‪:‬‬
             ‫و آمده تازه روی وخوش بخرام‬                               ‫نويف‬    ‫داده‬   ‫دولت او را بملك‬

  ‫«لغت فرس‪۷۳۳٩‬‏ ‪.‬‬
  ‫‪ - ۲‬از‪ :‬خرام ( ه‪.‬م‪) .‬ب‪+۳‬دن ( یوند مصدری)؛ جزو اول‌هندی باستان ‪)۲ 130۳_2‬‬
                                                                                     ‫داسفا! ‪ ۲ :‬ص ‪ ۹۳‬و‪.٩۹‬‏‬
                    ‫دولت بارینه تصور کنو‬                             ‫‪ - ۸‬چند خرامی وتکبر کنی‬
   ‫دلتان ‪.۰4۱‬‬
            ‫ک‬
```


## [2026-09-14T01:25:01.288Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"خراسان\" BQT_v2_pages.txt | head -20\necho \"=== leafnum of hits\"\npython3 - <<'EOF'\nimport re\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'خراسان' in p:\n        print('leaf',i,'printed~',i+540)\nEOF",
 "description": "Find خراسان in BQT vol2"
}
```


### [2026-09-14T01:25:02.440Z] TOOL RESULT

```
165: ‫(صفحة صدوسی‌وهفت) ‪.‬هر گاه «داشنامة» بدون‌قددی‌بادشده مراد داشنامه مصححآقای خراسانی است‬
540: ‫جام بر از هی = ممروف است ‪-‬‬                            ‫تنه است ‪ -‬و نام ولابتی هم هت‌ازخراسان ؟‪.‬‬
752:                                                    ‫خرجرد اوزلابت جام خراسان و‬
1008:   ‫خرد و نرم کردن چیزی دردهان ‪ ,‬و اینلفت هماکنون دربعض نقاط خراسان بمعنی مکذور‬
2891:‫جواران ‪ -‬بضم اول بروزن‌خراسان»‬                       ‫‪۱‬‬                   ‫غله است ‪ ۴‬معروف که پاسب‬
4829:   ‫چرا خوارهای خراسان وعراقاست‪( ».‬چهار مفاله ‪ -۷ .)۱۳‬از‪:‬چراخ (چراع) ‪ +‬واره ( یوند‬
5015:    ‫‪۹‬ے‬     ‫بوده قدم درخراسان‬           ‫نقطه‌دار ‪ .‬نام شهری‬
5022:     ‫ردان استخفاف کرده سخارا آمد‪۰ ‎.‬‬                                 ‫از آن چربك امبر خراسان‬                                  ‫‪ - ٩‬د یس‬
5782:                                             ‫با‬                                  ‫مرخراسان فز توابم طوی ‪.‬‬
6016:                                           ‫ولی در کردی ومشهد(‪ )6102]806‬ودرجنوب‌خراسان( )‬
6071:        ‫خراسان ‪( 10186‬کنجشك) » مثلی است‌درخراسان‪« :‬چفوكامسالی‌به چغوك بارسالی چیزبادمته»‬
8087:‫خی‌اسالی‬   ‫تر‬     ‫حبق خراسانی ‪-‬‬                        ‫سربانی داروبی است کهآ نرا حندقرقی کوندا »‬
9795:                                                                       ‫ات ازخراسان که چپجه ومپنه داخلآ نولات‬
10330:         ‫که وقف کرد بدو ذوالجلالعزوجلال‪.‬‬                                  ‫خدایگان خراسان وآفتاب کمال‬
10537:                                ‫خراب اکمتن ک‬                  ‫اول ‪ »,‬دمعثی مشرق‬    ‫م‬   ‫‪-‬‬   ‫خراسان!‬
10567:               ‫دروباش و جپان را میخور آسان‬                           ‫خوشا جابا بر و بوم خراسان‬
10568:               ‫خراسان آن بود کزوی خورآسد‬                              ‫زبان پپلوی هر کو شناسد‬
10571:      ‫ورك ‪ :‬اسفا ‪ ۲ :۱‬ص ‪ « ۹۷۱.۰‬خراسان " تفسیره‌المشرق » « مفاتیج‌العلوم خوارزمیس‬
10573:                              ‫‪:‬براشهر (بشابور ‪۰‬ف‬    ‫‪ ۲‬؛ خراسان قدیم شامل چهاربخش‌بوده ا‬
10580:     ‫خراسان کنونی ازشمال محدود است بماوراءاللهر ‪ ۰‬از مشرق بهربرود ودشت ناامید » از جنوب‬
=== leafnum of hits
leaf 4 printed~ 544
leaf 13 printed~ 553
leaf 16 printed~ 556
leaf 20 printed~ 560
leaf 52 printed~ 592
leaf 84 printed~ 624
leaf 87 printed~ 627
leaf 100 printed~ 640
leaf 103 printed~ 643
leaf 104 printed~ 644
leaf 139 printed~ 679
leaf 168 printed~ 708
leaf 177 printed~ 717
leaf 181 printed~ 721
leaf 227 printed~ 767
leaf 233 printed~ 773
leaf 251 printed~ 791
leaf 286 printed~ 826
leaf 304 printed~ 844
leaf 325 printed~ 865
leaf 349 printed~ 889
leaf 351 printed~ 891
leaf 353 printed~ 893
leaf 391 printed~ 931
leaf 429 printed~ 969
leaf 489 printed~ 1029
leaf 492 printed~ 1032
leaf 523 printed~ 1063
leaf 574 printed~ 1114
leaf 577 printed~ 1117
leaf 582 printed~ 1122
leaf 617 printed~ 1157
leaf 620 printed~ 1160
leaf 631 printed~ 1171
leaf 636 printed~ 1176
leaf 651 printed~ 1191
leaf 667 printed~ 1207
```


## [2026-09-14T01:25:08.288Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==182 {print}' BQT_v2_pages.txt | sed -n '1,80p'",
 "description": "BQT vol2 leaf 181 (0-based) khorasan entry"
}
```


### [2026-09-14T01:25:09.274Z] TOOL RESULT

```
                                                                                                 ‫‪۷ ۲۳‬‬


              ‫اهبه اآزسمان باشد ‪.‬‬
                                ‫خراب اکمتن ک‬                  ‫اول ‪ »,‬دمعثی مشرق‬    ‫م‬   ‫‪-‬‬   ‫خراسان!‬


‫تح اول بورزن لواش ‪.‬‬
                  ‫«‬                 ‫خر اش‬                     ‫امت که در مقابل مغرب با ‪ -‬و نام ولابتی‬
                                        ‫‪۲ ٩‬‬       ‫‪۰‬‏‬




 ‫‪-‬‬    ‫کردن‬      ‫وفبمعنی رخنه‬       ‫رحنه باشف‬           ‫نجعي‬    ‫آن ولات در مشرق‬         ‫وون‬
                                                                                         ‫مشهور چ‬    ‫هم هست‬
‫و تایکار‬    ‫و از کار افشاده وسقط شده‬      ‫‪-‬‬   ‫و خراشدن‬        ‫فاری و عراق واقم است بنا بران بدین نام‬
 ‫و دوستده‬      ‫زده‬   ‫خف‬   ‫و موه‬     ‫‪۴‬‬         ‫ا‬   ‫آهده‬
                                                                ‫ازموسیقی‪.‬‬    ‫خوانده‌اند ‪ -‬ونام نفمه‌ای هم هت‬

                                        ‫را نگیوزیند ‪.‬‬         ‫دروژن بداختر» موذیات‬
                                                                                 ‫حر استر ‪ /‬ب‬
‫= بر وزن ترآشیدن ›‬                ‫حر اشیدن‬                    ‫راکوبند مطلقاهم‌چو ماروعقرب وزنبور رموزچه‬
                                                                                                ‫وامثال آن ‪.‬‬
           ‫بمعنی ریش کردن ومجروح ساختن باشد ‪.‬‬
 ‫‪ ۰‬معرب‬        ‫طین‬
                 ‫ازن‬
                   ‫لو‬‫سبر‬
                       ‫حراطین =‬
                                                               ‫‪-‬نابه آاسزمان‬
                                                                           ‫خر اس خر اب ک‬
 ‫خراتین امت و آن کرمی باشد که در گل نرم‬
 ‫تکون پیدا کند و بعربی حمرالارض گوبند جم‬                       ‫به‌عنی خراس‬     ‫جر اس خسسان ‪-‬‬
                                         ‫‪ - ۱‬دریپلوی ‪(0252۲2۷۲‬مشرق) «میناه‪: › ۲: ۳۱‬‬
               ‫دروباش و جپان را میخور آسان‬                           ‫خوشا جابا بر و بوم خراسان‬
               ‫خراسان آن بود کزوی خورآسد‬                              ‫زبان پپلوی هر کو شناسد‬
               ‫کجا ازوی خورآبد سوی ابران ‪.‬‬                          ‫خورآسان رابودمعنی‪ :‬خورآبان‬
     ‫«وس ورامن ص ‪۱۷۱‬؟‪.‬‬
      ‫ورك ‪ :‬اسفا ‪ ۲ :۱‬ص ‪ « ۹۷۱.۰‬خراسان " تفسیره‌المشرق » « مفاتیج‌العلوم خوارزمیس‬
     ‫»رات ‪,‬‬ ‫ه‬     ‫بانا»ن‬   ‫طهست‬
                              ‫‪:‬براشهر (بشابور ‪۰‬ف‬    ‫‪ ۲‬؛ خراسان قدیم شامل چهاربخش‌بوده ا‬
      ‫پوشنگه » بادغیس » طوس) ‪ -‬مروشاهجان » سرخس » دا » ابیورد ‪ .‬مروالرون » طالقان آمل‬
     ‫‪,‬کگوانان » طخارستان علیا ‪ ,‬خت ‪ ,‬اندرآبه » بامیان » بفلان ‪ ۰‬والج » روستای بیل ‏‬  ‫فارباب ز‬
     ‫‪۰‬لم » سمدگان ‪ -‬ماوراءالنپر( بخارا ‪ ۰‬چاچ » طراز‬  ‫بدخشان ن‪۰‬رمن ‪ ۰‬چنانیان‪ .‬طخارستان سفلی خ‬
     ‫‪ ,‬اشروسنه ‪ ۰‬سیام » فرغانه و سمرفند ) « معجم‌البلدان »‬             ‫تان‬
                                                                         ‫فی»‬
                                                                           ‫نشد» صفد ‪ ۰‬هو کس ‪.‬رنو‬
     ‫خراسان کنونی ازشمال محدود است بماوراءاللهر ‪ ۰‬از مشرق بهربرود ودشت ناامید » از جنوب‬
     ‫بکرمان واز مغرب بعراق عجم و استراباد ‪ .‬طول آن ازشمال بجنوب بکرمان اوز مغرب بعراق‬
     ‫عجم و استراباد ‪ .‬طول آن ازشمال بجنوب ‪ ۰۰۸‬واز مشرق بمغرب *‪ ۸4‬کیلومتر و ماحت آن‬
      ‫کشف رود ورود‬‫گکارن و‬  ‫نزديك به ‪ ۰۰۰۰۲۳‬کیلومتر ھربح است ‪ .‬رودهای مهمی مانند اترك و‬
       ‫‪.‬معیت‌خراسان قرب ‪۰۰۰۰۰۳۴۱۰۱‬‬  ‫"یبشرم (قراسو ) درآن جاری است وبمصرف زراعت میرسد ج‬
     ‫است ‪ .‬کرسی‌آن مشهد وشهرهای‌آن ‪ :‬سرخس ‪ ,‬دره گز ‪ ۰‬فوچان » بجنورد ‪ ۰‬نیشابور ‪ ,‬جوین ‪۰‬‬
     ‫ولشن‬
        ‫سبزوار » اسفراین * جام » باخرز خوواف » تربت حیدری ‪ :‬ترشیز ‪ ۰‬فردوی ( تون ) گ‬
           ‫(طبس) » قاینات » شاهرود » سمنان وداعفان امت ‪.‬ک«یهان ‪ .‬جفرافیای سیاسی ‪.* ۹۷۱-۰۱۲‬‬
                     ‫‪ - ۴‬پپلوی ‪ , 7(8)05]۵۳5‬اوستا ‪ « 3615]8۳6-‬اسفا ‪ ۲ :۱‬ص ‪٩ ۰۸‬‏ ‪.‬‬
                                                       ‫‪ = ۴‬غراش ( ه‪ .‬م) «اسفا ‪ ۲ :۱‬ص ‪. ۰۷۰‬‬
         ‫ببر دو رخافت هست خراش ‪.‬‬                               ‫‪ ۴‬ت اکر چه لطف دارد تقش‬
      ‫رکوید‌سمرقندی‪ « .‬لغت فرس‪۵*۲‬؟‪.‬‬
                      ‫یدن ( یوند مصدری ) = غراشیدن («‪.‬م‪).‬‬                   ‫‪.‬م(‪) .‬‬
                                                                                 ‫«راش‬
                                                                                    ‫‪ -‬از خ‬
```


## [2026-09-14T01:25:19.449Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt').read()\npages=t.split('\\f')\nimport re\nfor i,p in enumerate(pages):\n    if 'خورشید' in p and ('اوستا' in p or 'پهلوی' in p or 'پپلوی' in p):\n        print('=== leaf',i,'printed~',i+540)\nfor i,p in enumerate(pages):\n    if 'خاور' in p and ('اوستا' in p or 'پهلوی' in p or 'پپلوی' in p):\n        print('--- khavar leaf',i,'printed~',i+540)\nEOF",
 "description": "Find khorshid and khavar in BQT v2"
}
```


### [2026-09-14T01:25:20.612Z] TOOL RESULT

```
=== leaf 45 printed~ 585
=== leaf 108 printed~ 648
=== leaf 168 printed~ 708
=== leaf 206 printed~ 746
=== leaf 242 printed~ 782
=== leaf 244 printed~ 784
=== leaf 246 printed~ 786
=== leaf 278 printed~ 818
=== leaf 294 printed~ 834
=== leaf 397 printed~ 937
=== leaf 482 printed~ 1022
=== leaf 494 printed~ 1034
=== leaf 551 printed~ 1091
--- khavar leaf 168 printed~ 708
--- khavar leaf 474 printed~ 1014
--- khavar leaf 625 printed~ 1165
```


## [2026-09-14T01:25:24.336Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"########## leaf 246 (printed 786)\"; awk 'BEGIN{RS=\"\\f\"} NR==247 {print}' BQT_v2_pages.txt | head -60\necho \"########## leaf 168 (printed 708) khavar\"; awk 'BEGIN{RS=\"\\f\"} NR==169 {print}' BQT_v2_pages.txt | head -60",
 "description": "BQT khorshid and khavar pages"
}
```


### [2026-09-14T01:25:25.353Z] TOOL RESULT

```
########## leaf 246 (printed 786)
                                                                                               ‫خورد‬

 ‫خورده زه با انی معدوله بر وزن‬                          ‫ت بائانی ممدوله " ماضی‌خوردن‬      ‫جورد‬
             ‫کنده پر‪ .‬مطبخی وطباخ راگوبند ‪.‬‬         ‫‪-‬‬   ‫باشد ‪ - ۱‬و بمعنی شکست‬         ‫ن‬ ‫دکل‬‫ه|‬‫ر‬‫کک‬ ‫است‬
 ‫خوردی؟ ‪ -‬با انی معدوله بر وزن‬                          ‫و ریزه ریزه کرد هم در مبودّالصلا نوشته‌اند ‪-‬‬
                                                         ‫ویمعتی درخور ولایق وسزاوار نیزآهده است ‪.‬‬
         ‫مردی » مکاولات واطعمه رگاونند ‪۸. ۵‬‬
 ‫ر‌سواد ان «کنایه سازحر‬
                      ‫خشوید‬                             ‫خور دستان دبا انی معدوله و دال‬
 ‫خیزان و شب‌بداران وعیسی رنبگان باشد ‪٩‬‏ ‪-‬‬               ‫وسین بی‌قطه بروزن انگشتان » شاخ تازه ای را‬
                ‫کآه‬
                  ‫نو‬‫اگان‬  ‫وعقربان‌پادشاه ‪ -‬وف‬
                       ‫نرشت‬                             ‫گویندکه اتزاك انگور سرزند و آفرا ببب‬
 ‫بوقت گرما‬
                                      ‫سوار شوند ‪.‬‬        ‫ترش مز کی خورند‪ -.‬و شاخهای تاز درختان‬
                                                         ‫دیگر و نهال ګل و رباحن را لیز گفته‌اند ‪#. ۳‬‬
‫خو رمك ت باثانیممدوله و میمبر‬
‫وزن مردك » »هره ای باشد که بجهت دفم چشم‬                 ‫خور دوستان‪ -‬بانالی مسوله بروزن‬
 ‫زغم بر گردن اطفالآویزند ؛ وباین معنی بثالك‬             ‫متصورخان > ببهمعنی‌خوردمتان است که شاج تارءٌ‬
 ‫مشدد هم هت ؛ وبا ثالث لقطه دار لیز کنته‌اند‪.‬‬                                    ‫تاك انکور وغره باعد؟‬

                            ‫ذا ‪:‬‬
                               ‫غ‪-‬‬‫‪۱‬هلوی ‪( 172۷5‬خوردن) « مسینا ‪ «۹۳۱:۲۰‬اونوالا ‪» ۳۲‬‬
                                                                                ‫پ‬
              ‫سیر ‪.‬‬      ‫ونم‬
                           ‫شم‬‫آبثان خایند و‬                        ‫خوردی که خورد گوزن با شیر‬
       ‫نظامی گنجوی‪ «.‬کنجینه ‪.*6۵‬‬
                 ‫‪۰‬‬    ‫‪ = ۳‬رك‪ :‬خوردستان ‪.‬خودستان‬             ‫‪۰‬‬    ‫‪ _ ۳‬رك‪ :‬خودستان»خوردوستان‬

       ‫‪ - ۴‬پهلوی ‪. « 61۲2۷6‬سینا‪kîtrux » ۹۳۱:۲‬‏ «ناوادبا ‪ ۷۹۱۰‬ارمتیع ‪611۲0‬‬
                          ‫«اسشق ‪ »۷۰۵‬زرکه ‪ :‬اسفا ‪ : ۱‬اص ‪۲۹۲٩۱‬‏ ‪۲ :‬ص ‪ ۰۹۱‬هوبشمان ‪. ۷۰۰‬‬
              ‫و آنگاه مه یمهبود این هردو ‪۰‬‬                      ‫بان سياه وخوردی بی‌چربو‬    ‫‪6‬‬
       ‫‪.‬الممجم ‪AY‬‏‬       ‫کایی مروری‬

                 ‫‪ - 1‬بدان مناسبت کهکوبند عیسی درآسمان چهارم فرین خورشید است ‪:‬‬
              ‫سابة خورشید سواران طلب ‪.‬‬              ‫رنج خود و راحت باران طلب‬
   ‫‪۰‬‬    ‫نظامی کنجوی‪ .‬دگنجینههه»‬

       ‫‪ #‬خورد ی ‪ -‬بروزن بردن» اوسنا ‪( 1872۷ .18۷۳3-‬اکل ) » بپلوی ‪02172۷‬‬
       ‫ارمنی ع ‪kitrox‬‏ (‪۱‬کل‌طعام)‪ .‬کردی‪ (0۳1۲۷۲, 0۳1۳1۱۳‬کل)‪.‬افتانی ‪. 12۲05‬استی ‪۲1۷8۷5‬‬
   ‫‪.‬سرربکلی ‪ 0718-۲05‬سگلیسی ‪« 777 012‬اسشق ‪۷۰6»9‬اسفا‪:۱‬‬                      ‫‪2‬ی‪11‬‬
                                                                              ‫‪-‬منج‬
                                                                                 ‫‪۲‬ی و‬
                                                                                    ‫‪ 0‬مشغن‬
   ‫رگ‪-‬ے‪۰۷۳۱‬‏ «بونکر ه‪٩ ۷‬‏ < که ‪.‬‬
                               ‫‪۸۳‬‬‫‪٣‬ص‏ ‪ ۰۵۰۳ ۰۰۹۲ ۱۵‬روکه‪ :‬فهرست» «مسینا ‪ ۹۳۱‬ن‪٩‬یب‬
       ‫است ‪ ۰۱‬؛زاگلو فرودادن وبلعیدن نذا »ک‪۱‬ل‪ :‬فروباه پیشتر رفت وماهی خوردن گرفت ‪« »۰‬سند‬
                                            ‫بادنامه‪ .‬ظهیری‪ - »۸4‬آشامیدن ‪ -‬تلف کردن» برباد دادن‪.‬‬
  ‫‪ #‬حورشید ‏ بضم اول وواو ممدوله از خ‪:‬ور (آقتاب )(هم‪ + ).‬شید ( هم‪ ) ۰‬اوستا‬
  ‫هکر ‪ :‬زور‬
          ‫‏‪ «hvara xshaeta‬یولهپ ‪ ۷2751264‬ةغل( باتفآینعمب )ناشخرد هکر ‪ :‬روخ و‬
                                                                                  ‫شماری ص ‪: ۹۲-۳۳‬‬
                     ‫بوتس اندر دهان ماهی شد‬                 ‫قخروصرشید درسیاعی شد‬
       ‫«کلتان‪.»۲۲‬‬

########## leaf 168 (printed 708) khavar
        ‫ا‬
‫خرو داروست وآترا خو لنجان هم میگو ند‪4 ۴‬‬

‫آون‌بیخی باشد درایی‪ .‬گویند که بازآشیان خود‬                              ‫نام ولاش‬   ‫بروزن‌داوران»‬       ‫‪-‬‬   ‫خاوران‬
‫را از آن سازد ‪,‬چه در وفت بجه از آشیان باز‬
                                                                       ‫ات ازخراسان که چپجه ومپنه داخلآ نولات‬
‫باز(‪ )۲‬بابد و بسار‬              ‫برداشتن در آشیان آن()‬
                                                                        ‫است » وتولد حکیم انوری آنجا شده چه او در‬
                                                           ‫آورند ‪۰‬‬

                                                                        ‫اولخاوری‌تخلص میکرده اصت‪ -‬ومشرق ومقرب‬
‫»‬    ‫ناد‬    ‫رزن‬     ‫بقتح ثالث بر‬      ‫‪-‬‬       ‫ند‬     ‫حاو‬
                                                                                                           ‫‪۰‬‬   ‫‪۳‬‬   ‫را نیز گوبند‬

‫و بزر گه خانه‬        ‫که صاحب‬         ‫ته‬
                                      ‫اسے‬           ‫مخغف‌خداوند‬

‫باشد‪ -‬و یمعنی‌محدد همآمده است(‪ )4‬کهاز جد‬
                                                                      ‫خاوش ‪ -‬م اك و سکون شين‬
                                          ‫‪.‬‬         ‫باشد‬   ‫ومعددود‬
                                                                        ‫تخم‬     ‫قرشت ‪ ۰‬خیاری باشد که آنرا بجهت‬
                                                                                                                    ‫نگاهدار ند ‪۰‬‬
    ‫مخفف خداوندکاراست‬                ‫ادر‬
                                       ‫کو ن‬
                                          ‫خا‬
                        ‫باشد ‪#3.‬‬      ‫ویز رگ‬          ‫که صاحب‬
                                                                         ‫خاو ل ‪ -‬بن تااث بروزن‌ابل‪ ,‬مورچه‬
                                                                                   ‫راگوبند وآن ازموذبات (‪ )۱‬است‪۴ .‬‬
    ‫خای‪ ۰ ۲ ۲‬بکون تحاتءانی ‪ ۰2‬بمعنی‬
‫خاسدن ولرم کردن در زبردندان باشد ‪ -‬وامر‬                                 ‫خاو لنحان = بکرلام وسکون نون‬
    ‫از خاییدن (‪ )۵‬هم هست ممنی بخای و در زر‬                              ‫فه و بنون دیگر زده » بمعنی‬
                                                                                                 ‫یلد‬
                                                                                                   ‫شمبا‬
                                                                                                      ‫کجی‬
                                                                                                        ‫و‬
                      ‫(‪ )۳‬خم ‪ - :۳‬باز‪.‬‬                         ‫(‪ )۲‬چش ‪ :‬بان‬                ‫(‪ )۱‬خم‪ : ۳‬موذیان‪.‬‬
                                                  ‫‪ 0‬خائیدن‬    ‫‪ ۰‬چش‬    ‫‏)‪ (e‬چك‬              ‫(‪ )4‬چك ‪ - :‬است‬

     ‫‪ ۰‬ومشرق‬       ‫ی هفغر ب است‬               ‫‪ - ۱‬خاور بازماندء کلمةٌ پهلوی « خوربران » با « خوروران »‬
       ‫آورده اند ‪۰‬‬     ‫خود دعنی هقرب‬                ‫‪ €‬می‌ففتند ویعض گوبند کان خاور را یمعتی درست‬                   ‫را «خوراسان‬

                  ‫هم از باختر برزند باز تیغ‪.‬‬                                    ‫چومهر آورد سوی خاور کریغ‬
     ‫فردوسی طوسی با عنصری بلخی؟‬
     ‫بسرتین شب علم ‪.‬‬
                   ‫پیدا شد اندر باختر آ‬                                       ‫خورشید را چون بست‌شد درجانب خاورعلم‬
     ‫لاءمی کر کانی‪.‬‬

     ‫معمول‬       ‫نادرست و‬       ‫اصلی بکار برده اند» اما باختررا بمطی‬            ‫را تمعمی‬   ‫خاور‬   ‫ادن دوگودنده‬


     ‫؟‪ .‬هرن گوید ‪ :‬خاوران (خاور "‪ 7‬ان )‬                       ‫‪e ۰‬‏ ‪ ۱‬ص ‪۸۱۱-۹۱۱‬‬      ‫استعمال کرده‌اند‪ 2 .‬مقالات کروی‬


           ‫فس‪ :‬بهلوی ‪(0‬‬                       ‫‪.‬‬           ‫(مفرب) ازخاور(مفرب)‪ .‬مشتق‌است‪ .‬رك‪ :‬خاوران‪ ۴ .‬ر‬
                                                   ‫‪-‬ك‪ :‬خاور‬
                                                             ‫ورك ‪ :‬اسشق وهو شمان ‪. ۸14‬‬             ‫‪ ۶‬اسفا ‪ ۲ : ۱‬ص ‪۹۷۱‬‬
                ‫برمن‌زمانه نگ ترازچشم خاول‌است‬                                ‫زوی قد چو سروت براستی‬
                                                                                                  ‫ت آرزا‬
     ‫نظام ؟ ‪.‬‬   ‫«فرهنگه‬     ‫‪۰‬‬   ‫ان مین‬
```


## [2026-09-14T01:25:46.141Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(json.dumps(d['MON'],ensure_ascii=False,indent=1))\n\"",
 "description": "MON ref info"
}
```


### [2026-09-14T01:25:47.192Z] TOOL RESULT

```
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
```


## [2026-09-14T01:25:54.642Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -o \"هور[^ ]\\{0,3\\}[^\\n]\\{0,120\\}\" MON_part2.txt | grep -n \"خورشید\\|آفتاب\\|ستاره\" | head -10\necho \"=== herba\"\ngrep -n \"حربا\" MON_part1.txt | head -10\necho \"=== khorshid\"\ngrep -o \"خورشید[^\\n]\\{0,150\\}\" MON_part1.txt | head -5",
 "description": "Grep Mo'in 2-vol for هور، حربا"
}
```


### [2026-09-14T01:25:55.812Z] TOOL RESULT

```
151:هور خورشید تصور می‌شده و 
=== herba
3799:یوار 7 (جان.) آفتاب پرست؛ حربا» 
52896:حرباء: ۵۵8 (ع. ف. حربا] (.) (جاذ.) 
=== khorshid
خورشید» شمس» مهر. 
خورشید» شعاع شمس؛ مق. ماهتاب. 
خورشید در 
خورشید فروزان» 
خورشید به سبب با هم شدن در
```


## [2026-09-14T01:25:58.538Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '52890,52905p' MON_part1.txt\necho \"=== context 3795\"\nsed -n '3795,3803p' MON_part1.txt\necho \"=== hur in part2\"\ngrep -n \"هور \" MON_part2.txt | head -20",
 "description": "Mo'in herba entry"
}
```


### [2026-09-14T01:25:58.644Z] TOOL RESULT

```
حرام» حرامکار. (۰) دزد» راهزن. 

٩ :‏ [ع.] (مص‌ل.) جنگ کردن؛ 
جنگیدن. (.) جنگ نبرد» کارزار» بیکار 
ج. حروب. 

حرباء: ۵۵8 (ع. ف. حربا] (.) (جاذ.) 
آفتاب پرست. 

حربه: (۵-)۵۲۳۵ [ع. حربة] (.) آلت حرب 
و نزاع مانند شمشیر» خنجره نیزه کوتاه» 
کارد و غیره» ساز جنگ. سلاح. 

حربی. -2۴ (ص نسد.) منسوب به حرت» 
جنگی. جنگنده» رزمنده. کافر حربی: 
(شرع.) کسی که امل کتاب (مسلمان» 
=== context 3795
سبز پهن و گل‌هایش زرد است. نهنجی پهن 
دارد و گل‌ها مانند آشعهً آفتاب در نهنج قرار 
گر فته‌اند. دانه‌های آن دارای روغن بسیار 
است و آن را مانند تخمهً هندوانه تفت داده 
یوار 7 (جان.) آفتاب پرست؛ حربا» 
آفتاب گردش. آفتاب گر دکك. 
آفتاب‌گردان: 2.0 (ص‌فا.) سایبان. 
چتر. . قطعه‌ای از چرم؛ پارچة ضخیم با مقوا 
3 پیشانی 
=== hur in part2
3552:دور غیبت صغری تا هنگام ظهور وی. 
4385:زاید پر داتش نبود و افعالش عبارت از ظهور 
4920:ظهور به کمال علمی و غیره است و آنچه 
4921:منفتح شود بر بنده از مقام قلب و ظهور 
4930:( تص.) ظهور کمالات روحی و تلبی اش 
4933:عبارت از ظهور به مقام ولایت و تجلیات 
4986:هر جای گشاده و فراخ. (تص.) ظهور چیزی 
4988:بصورت ماده نوعیه با ظهور 
8243:به ضم خای معجمه را - که مشهور است - 
8412:شبرازی) مراد فلسفه مشهور و معمول است؛ 
8757:استیلای ظهور حق بر باطن وی. ب -سقوط 
9531:آسمانی که موجب است ظهور چیزی را که 
9540:مرتبت تجلیات اسماء را که موجب ظهور و 
10360:می‌داد. به مروز دهور حل و فصل مسایل 
10942:غالب» مقهور کننده» چیره؟ ج. قاهرین» 
13088:قضاء علمی: (فد.) مر تمه ظهور در علم است؛ 
13541:آمریکایی مشهور است. قطن مصری: (گیا.) 
14640:مشهور است و امروزه فقط بنام سود اطلاق 
16363:مشهور از این فرارند: قید استتناء: جرء جر 
17147:مشهور است. تخم کاجیره: (کیا.) دانه
```


## [2026-09-14T01:26:07.709Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^هور\\|هور:\\|هور؛\\|هورا\" MON_part2.txt | head -20\necho \"=== khor\"\ngrep -n \"خور:\\|^خور\\b\" MON_part1.txt | head -20\necho \"=== nohur\"\ngrep -n \"نهور\\|بدنهور\\|بد نهور\" MON_part1.txt MON_part2.txt BQT_v1.txt BQT_v2.txt | head -20",
 "description": "Grep for هور، خور، نهور"
}
```


### [2026-09-14T01:26:07.839Z] TOOL RESULT

```
2397:گردیده باشد به طرفی يا کاری. غلط مشهور: 
7024:اهورازدا فروهری دارد. 
28634:کهور: تاه (۱.) (گیا.) درختجه‌ای است از 
33855:افتاده و استوانه‌بی شکل دارد. گل ماهور: 
40427:لندهور: ۱:0۵)2(۲۲ (ص.) (عم.) مردی 
43475:ماهور: ۲ (.) هر یک از تبه‌های 
43541:ماهور؛ نست به اوازهای دک السته از 
47378:متهور: نها« [ع. اقافتا کی 
47985:تمثیلیه گویند. مجاز مشهور: (بن.) مجازی 
48589:آشکار کردن. محل جلوه و ظهور؛ مظهر. 
57519:(. مک.) محل شهرت. (ص.) مشسهور: 
74275:شریف بزرگوار. نام آور. مشهور؛ مق. 
89841:هورمرد) (اح.) اهورمز دا. ستارة مشتری. روز 
92216:(.) ستاره (مطلقا). به کردار (مانند) هور: 
92219:هورا: 3 (صت.) کلمه‌ای است که با 
92223:هور قلیا: ۵ ,۱۱2۷۵۲۲۲۱۷۵ (سر. عسر ] 
92268:هورمزد فرهنگ فارسی موه ۳۱۳۵۳ 
92280:هورمرد: (قد. ۱3۲:020)6۲ [- هورمز < 
92289:هورمون‌ها دارای برخی خواص مشش کند: 
92310:هور: 52 (.) آواز تند و تيز مانند صدایی 
=== khor
865:خوردن چیزی ترش و جز آن. میل و رغبت 
1225:آبخور: 20۲7 (امر.) محل آب خوردن» 
1354:خوراکی که عبارت است از ریزه‌های خیار 
1568:ابشخور: 20-0۲ [ < آشخوار ] (امر.) 
1682:خورنده را تشنکی. آوردن: 
2689:خوردنی‌های عادی (مانند گل و زغال) برای 
2690:خوردن ارزو کند. آنچه خویشان زن آبستن 
3060:خوردن: به قوی‌تر از خودی مصادف شدن» 
4021:خورنده (زن). (پز.) هر قرحه که گوشت 
7720:خور شید در یک برج؛ ج. احتراقات. 
9610:خوردن, به یکك باره در آب فرو شدن. 
9748:خورشید» افتاب» هورء هورخش. 
10988:خوراکی که به شکل رشته‌هایی به قطر 
11034:خورشید تا نمایان شدن قرص تمام آن برای 
12288:خوردن خواستن» درخواست قسم خوردن 
13699:خوردن تیر. اصابت مصیبت به کسی: فرود 
13764:خوردن» بهم رسیدن» بهم ساییدن. (امص.) 
14683:خوردنی‌ها» خورش‌ها» خوراک‌ها. " 
15346:خوردن» قسم یاد کردن؛ ج. اقسامات. 
16678:خوردن؛ برآمدگی شکم در اثر پرخوری. 
=== nohur
BQT_v1.txt:32322:۸ هر کرااتدر کمتدشصت ت بازی‌در فکند(ابوا لمظفر چفانی) کشت تاهش برسر من‌وشانهوره : 
MON_part2.txt:81399:انهار» انهر» نهور. 
MON_part2.txt:81576:نهور. (قد. 0۲)067ظ2۵ (.) نگاه به چشم.
```


## [2026-09-14T01:26:11.494Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '92210,92230p' MON_part2.txt\necho \"=== nohur\"\nsed -n '81570,81585p' MON_part2.txt\necho \"=== khorshid moein\"\nsed -n '9744,9752p' MON_part1.txt",
 "description": "Mo'in hur, nohur entries"
}
```


### [2026-09-14T01:26:11.595Z] TOOL RESULT

```
عماری؟ ج. هوادج. 

هو ده. (6-)ع۱0 [- هده] (.) حق» راستی)؟ 
مقّ. ببهوده. سوده فایده) مقّ. بهوده. 

فصو ۷( وا (اخ.) خورشیدء آفتاب. 
(.) ستاره (مطلقا). به کردار (مانند) هور: 
درخشان مانند آفتاب. 

هورا: 3 (صت.) کلمه‌ای است که با 
صدای بلند و ممتد برای اظهار شادی و 
تحسین ادا کنند) هلهلهً شادی. 

هور قلیا: ۵ ,۱۱2۷۵۲۲۲۱۷۵ (سر. عسر ] 
یسم ی . ضصح.- شیخ 
احمد اد ی در کتاب «شرح الز بارة» (رص 
)٩- ۳۹۵‏ گو بد؛ : «انسان را دو جسم و جسد 
است اما جسد اول مر کب از عناصر زمانیه 


است و این جسم مانند جامه‌ای است که 
=== nohur
ِ شمشیر هندی. نهدگک سیاه: هن 
شمثیر آبدار. نهنگک فلک: ( کد.) برج 
۱ 


سمسیر در علاف. 
نهور. (قد. 0۲)067ظ2۵ (.) نگاه به چشم. 


نهوض: 2 (ع.] (مسص‌ل.) برخاستن. 
حرکت کردن: کوچ کردن. (امص.) حر کت» 
رحلت. 

نهی . 2992 [ع.] (مص م.) باز داشتن» منم 


=== khorshid moein
جامه‌ای که طلبةٌ علوم دینی و کسبه زیر قما 
م32 . نیم تنه 2 روی جامه‌های 
دیگر می بوشیدند. نوعی از قماش نازکك. 
ارخش: ,0۲25 [- ه_سورخش] (.) 
خورشید» افتاب» هورء هورخش. 
ارخشیدن: 2۳5-0 [مصل.] ترسیدن» 
بیم د ان شتن» نیمتا ک گردینن از ترس موی 
بدن راست شدن و بوست بدن فراهم آمدن. 
ارداء؛ ۰33 [ع. ف. اردا] (مص م.) هلا کت
```


## [2026-09-14T01:26:24.366Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"########## BQT v4 pdf 303 (printed 2220) nohur\"\nawk 'BEGIN{RS=\"\\f\"} NR==303 {print}' incoming/BQT/BQT_v4_pages.txt | head -60",
 "description": "BQT nohur page"
}
```


### [2026-09-14T01:26:25.383Z] TOOL RESULT

```
########## BQT v4 pdf 303 (printed 2220) nohur
[pdf page 303]
نپوده تسده
نهوده - بنم اول ونانی وفتح‌داابجد. | رسید » ماضی‌هیدن آباشد بعتی غم‌خورد واندیشه
بمعنی زبور وآرایش زدان است که آن سرآویز | کرد وگذاشت - ولوعیازخوردنی هم‌هست که‌از
وکوغواره و سلله وحلقةٌ بینی وکلوبند وبازو | مغز حنظل وآرد ترکیب‌کنند .
بند ودست پراجن وانگشتر وغلغال باشد - ون نمی در نواد * سبمی در سوراخ
هفت را ای زگوبند وآن سرمه ووسمه واسرخی | گذاری و بزیان آوری, چه دواد بممنی سوراخج
وسفیداب و خال وزر ورق وحنا باشد ‎٩‏ + وزبان باشد - و کنایه ازین است که ممدوم‌سازی
نهور -جم اول و واو مجهول بروزن | و بی‌شا ن کردانی (۱) ۰
حور , نگاه کردن از روی فهر وغضب و خشم نهیدن - بفتح اول بر وزن رسیدن »
باشد ؛ و بمعنی نگاه وچشم هم بنظن آمده است بمعنی اندیشه کردن - و غم خوردن - و لهادن
که بجربی ریت وعی نکوبند ۴ . وگذاشتن باشد ‎٩‏ ؛ و باین معنی بکس اول هم
هب ؟ - بکس اول بر وزن فربب » | آمده است.
بمعلی تری وبیم باشد . نمیو ۲ < با واودرآخر, بروزن ومعنی
هید ؟ - بفتح اول وکسر ثانی بروزن بهیب است که نری و بیم باشد .
() خم ۱ :کنی
۱ -ر4 : هر هفت . ۴ - « بهور با اول مشموم و واو مجهول , بمعنی نگاه
کور دل هچ وکور میباشد سبك و بد تهور میباشد .
حکم سوزلی گفته :
توآن سری که شمارند خاك پای ترا سران محتشمان توتیای لور تهور .
اینکه در برعان ,معنی نگاه کردن از روی خشم لوشه تصحیف خوالی شده . درفرهنگهایهمتبر
بمعنی‌نگاه و چشم هردوآمده و اونگاه به خشم فهمیده . حکیم سای گفته :
ازان با بزرکان لیارم لشتن که آیشان چو حورند من بدتهورم .>
« اسین آرا ».
سروری نیز معنی لفظ را « بفشب نگریستن *آورده ولی با شعرسنائی (مذ کور در فوق) نمی‌سازد
«فرهنگه نظام» . ظ. بدنهور بمعنی بدمنظراست. ۴ - بکس‌اول ودوم , امالةٌ نهاب است
که لفظ عربی باشد بممتی هیبت رتری و بیم وعظمت وآوازمهیب وغارت « غیاث » « تهب (عر )
بالفتح غنیمت » نهاب ککتاب جمع , وهرچه بغارتآورده شود .» « منتعی‌الارب » وعبدل‌آن در
فارسی نهیو (م.) است. « اهیب ترس بود .» « لفت فری ص۷۷ >
تیفش بخواست خوزد همی‌خون مر کهرا مرکه از نهیب خویش مهر‌آن‌شاه رابخورد.
« عماره مروزی » ( برکزبده شمرباختمام نگارنده ج۱ چاپ۲ س٩4‏ ) .
۴ - ر4 : نهادن » هیدن . - رك : نواد . ‎٩‏ - ر3 : جهانگیری »
سروری » زان کوبا » وهیچيك شاهد نیاورداند ؛ ی : نهادن - ۷ میب (هم.)
```


## [2026-09-14T01:26:37.920Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==683 {print}' IEC.txt | head -60",
 "description": "Mann IEC page ~1334"
}
```


### [2026-09-14T01:26:38.942Z] TOOL RESULT

```
 beside nirü ‘strength’; Tokh. B sfor, s. ‘sinew’; W cf. (?) nyw, pl. -iau, m. ‘vigour’; OHG sénawa, MHG sénewe, s & wf. ‘sinew, nerve’; Sw. sno, pl. at m. ‘string’; Slovene, cf. snov, f. “material, stuff; R cf. o-snova, f. ‘warp’
sneuoros (sneuros, à, io) (extn. of type sneua, etc. q.v.) ‘sinew, nerve, vein". WP II, 696. Cf. sneu- (2) and sneru- (variant). (Iran. Arm. w. suffixed article) Skt. cf. a-snávirah, adj. 'sinewless'; Av. snávars (sic), s. ‘sinew’; Oss. nwar, pl. nordtä, s. ‘vein, nerve’; Per. navard, s. “twist, fold’; Arm.
sneu- — snoiguhos
15
20
25
30
35
40
45
 
1236
neard, gs: nerdi, ab. s. -iv, s. ‘sinew, fibre’; Tokh. B. sfiaur ‘nerve’ beside fare, s. ‘thread’; Gk. neüron, n. ‘sinew, bowstring’; neurá, f. ‘sinew’; Lat. nervus, 1, m. as Gk. (also: ‘string of instrument; nerve’); cf. also nervium, n. ‘string of instrument’; nervia, f. ‘stringed in- strument; MHG snuor, sv. (‘string, bond, cord’. Phonol. obscure) beside snar, sf. id.; Du. snaar, f. ‘string’; OE sner, f. ‘string of instrument; ON snæri, n. ‘cord’; (radical in) Cz. snuju, snouti, v. (spin, twist. Cf. sneu- 2) and in Norw. snu ‘turn’. An extn. arises in Arm. niwt,, o-st. ‘substance’, cf. W nwydd, m. id. and the OCS and com. Sl. inf. snuti *weave; shape”
sneuó (1) & (2), see sneu- (1) & (2)
Sneuos, see sneuor-
sniguh- (sninguh-) ‘snow’. Cf. sneiguh-, snoiguh-. WP II, 695 Skt. cf. snih, f. *moisture'; snihyati, 3s. “gets oily, moist; Gk. cf. nípha, acc. f. ‘snow’; niphei, 3s. ‘snows’; OLat. ninguit, nivit, Lat. ningit, 3s. id. beside nix, gs: nívis, f. ‘snow’; Olr. snige, Ir. snighe, m. ‘drip, shower’; sni- gim, snighim, v. id. beside Ir. sneachta, m. ‘snow’; OHG and OE sniwan, v. id., MHG snie, sf. ‘snow, -storm’; ON snjófa, v. id.; snifinn, adj. ‘snowed under’; Li. cf. sniñga, 3s. ‘snows’ beside OLi. (e-gde) sniegti, 3s. id. and Li. snygurioti, inf. ‘flurry — as snow’; Latv. cf. snigt, 3sg: snieg ‘to snow; it snows’
sniu- (?) “strong; strength’. Cf. sneu- (1) E sneuå. Per. niv, adj. ‘strong’; W nyw, m. ‘vigour. (For Go. sniwan ‘hasten’, cf. ksneu-)
snóg-, possible variant of type no$-, q.v. Per. & Gk. ambig. Per. naz, s. ‘flirtation’; nazam, -1dan, v. ‘flirt’; Gk. cf. nógala, npl. ‘snacks’; OE cf. snóca, wm. (queried: ‘nook’, but E snook = “a rude gesture"). (Lat. nugae ‘trifles’ here only if dia- lectal for *nogae)
(snoidh-, possible reconstruction as alterna- tive to type sneudh-. See Supt: S)
snoiguhos ‘snow’ (Skt: *grease"). Cf. sniguh- Skt. snehah, m. ‘grease’; Av. cf. snaezetiti, 3pl! “it snows’; Go. snaiws, m. OHG sneo, snio; OE snàw, m. ‘snow’; OCS & com. SI.
1237
snégü, m. id.; Li. Latv. sniégas, sniegs, id.; cf. (z-gde) Lat. nix, gs: nivis; MIr. snechta, Irish sneacht, m. id. WP II, 695
snoitos, is (snoitt-, snoist-, snoits-) “cutting, shoot, branch'. WP II, 695 Ir. snaois, f. (2) ‘slice’; OE snæd, f. id.; ON sneió, pl. -ir, f. id.; Ger. cf. Schneise, LG sneis, f. “forest cutting’; ON cf. sneis, f. ‘peg’; OCz. snét, gs: -u, m. ‘log’; Cz. snét, f. “branch, twig. (Isophones: MHG speisen, wv. tr. ‘string together; file’; Pol. sniec, f. “rust, smut’; Srb. snijet; Blg. snétej; Ukr. sniti, id.)
snork- (snerK-, snrK-) ‘grip, cramp, torpor’. WP II, 701 Gk. (z-gde) nárke, f. ‘cramp, torpor’; Alb. cf. narth, nerth, v. (“feel a chill’, fr. *snork-); OHG snaraha, OE snëarh, snëare, ON snara, f. *snare, noose' (o-gde in view of e-gde MHG snérhan, sv. 3. ‘constrict, tie’, as against ON snara, v. ‘twist, wring’)
snotis (not-?) ^wet Arm. naj, i-st. wet’; adj. liquid"); Gk. notis, f. *moisture'; nótios, adj. ^wet, damp'
snoubh- (snubh-, snumbh-) “marry; marri- age, bride’. WP II, 697 Gk. cf. nümphe, dial. nüphe, f. “bride”; Lat. nübo, ére, v. (of a man: ‘mar
```


## [2026-09-14T01:26:46.571Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==732 {print}' IEC.txt | head -70",
 "description": "Mann IEC leaf 731 (~p1334)"
}
```


### [2026-09-14T01:26:47.653Z] TOOL RESULT

```
i, -nomi, f. (stop, stun’; stu-
1327
bhah, m. ‘he-goat’; Gk. stüpho, v. ‘constrict’: stuphnós, adj. 'astringent'; stuphrós, adj. ‘rigid’, Br. stonn, m. ‘weeds left on fallow land’; sunn, adj. ‘stiff, erect’; OE stofn, mf. 'trunk, stem, branch'; ON stofn, m. 'tree- stump; base’; mod. stofna, f. ‘trunk, stem; race’; Latv. stubens, s. “tree-stump”
sthubh- (2) W swf, m. ‘space’; MHG stube, wf. “room, warm-room; villa’; OE stofa, wm. and stofu, f. ‘bathroom’; ON stofa, f. ‘parlour’. (Hybridism in It. stufa ‘warm room, hothouse, stove": Fr. étuve, id. if fr. *extufa- as Dauzat)
(sthubhlos, explicit only in Gk. Cf. sthubh-, sthubolos. Variant: sthubhros) Gk. stuphlós & stuphelós, adj. “solid, hard, cruel stuphelízoó, v. ‘shake, strike, bully, dissipate’; LLat. cf. stubulum, m. (‘golden thistle’ and sim. plants); Li. cf. stüburas, m. “post; backbone’; Latv. stuburs, m. ‘stump, post; Gk. stuphrós, adj. “hard, harsh, rigid’; Slovene steber, m. ‘pillar’
sthüd- ‘press, jolt, buffet, cut short, stop, halt”. WP II, 620. Cf. steud- Lat. studeo, ére, v. 'strive; study; rebel; G stutzen, v. ‘stop short’; (*-ü- in) Du. stuiten, v. “buffet; check; bounce"; Icel. stüta, v. "Kl": OCS (and com. Sl.) styZdo se, stydéti se "be ashamed", lit. ‘stop short"; cf. also Du. stutten, v. ‘prop, support’; Scots to stot, v. ‘to stagger’. Nominal types: MHG stotze, wm. "block: G Stutz, m. ‘prop’; Du. stut, m. id.; (variant in) Sw. stuss, m. (“arse”, fr. *sthuds-), (and in) E stunt, v. “limit growth oP: Icel. stuttur, adj. (brief, fr. *sthund-); (uml. in) ON stytta, v. ‘shorten’; styttast, refl. («lose one's temper’: (long-gde in) Du. stuit, m. jolt; LG stüten, wm. *bread-roll; ON stútr, m. “butt, stump’; mod. (stütur) ‘bottle-neck’; Norw. Sw. stut, sm. ‘steer; boor’; OCS (and com. SI.) stydü, m. ‘shame’; cf. Ukr. o-stylyj, adj. (“averse”, fr. *sthūdlo-). See next.
sthudh- ‘stump, support, underpinning’. Cf. sthud- Ir. stod, m. pl. stuid (tooth; W swdd, m. ‘frame’; swdden, pl. swddi, f. ‘beam, rafter’; OE studu, pl. styde, f., and stod, m. “pillar, post’; ON stoð, pl. stoðr & steðr, f. id.; cf.
sthubh- — sthúüið
10
20
25
30
35
40
45
1328
styðja, v. ‘support’; extns. in OE stodla, wm. ‘sley’: ON stuðull, pl. stuðlar, m. “prop, stay”; cf. MHG stolle, wm. “stand, frame”
sthug- (1) “stop, stiffen, stun' (stug-, sthug-) Gk. stágos, n. ‘abhorrence’; stugéo, v. ‘dread’; W cf. swyn, pl. -ion, m. ‘magic’; swyno, inf. “preserve; charm’; swyd, m. Cdread, fr. *stugto-); swydo, inf. denom. ‘intimidate’; MHG stocken, stücken, f. ‘eradicate; stiffen; attack’; G stocken, v. ‘stop dead”; ver-stocken, v. ‘go hard’; Du. stokken, v. as G; stokkig, adj. ‘woody, hard’; Du. cf. also stoken, v. (‘stoke, fire — an oven’, fr. Eng.?); LG stock, m. ‘mildew’; Li. stungù, stùgti, v. ‘grow stiff beside stügstu, stūgti, v. ‘erect oneself; cf. stùguras, m. ‘post, pole’
sthug- (2) ‘end, bit, chunk W sw, m. ‘remainder’; OHG stucki, n. ‘piece’; OS stukki, OE stycce, Du. stuk, ON stykki, id. beside MHG stoc, gs: stockes, m. ‘stump, block’; OE stocc, m. id.; ON stokkr, m. id.; (long-gde in) Du. stuik, m. ‘butt-end’
sthüg- (1) = sthug-, q.v. (2) ^wrapping, en- velope' MHG stüche, f. *wide sleeve, kerchief, veil, cloth wrapping’; ON stúka, f. “sleeve; wing of building”; Li. stügà, f. “band, bellyband, tape, pattern in warp'. (Isophonic: G stauchen, v. *jolt'; ver-stauchen, v. ‘sprain’; LG stüken, v. ‘sprain, squeeze’ beside stükern, v. ‘jostle’; stükel *cripple?)
sthugeros (variant of type sthug- (1), q. v.). Cf. sthurg- (sthurg-) & sthrg- Arm. t'urc, gs: trco, adj. ‘fired, hardened; firing, baking’; Gk. stugerós, adj. ‘horrible’ beside stuganós, stugnós, id. Cf. sthug- (1); LG cf. stukkern, v. (2) “stop dead: (3) 'so- lidify'; Du. stokker
```


## [2026-09-14T01:26:53.220Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"sāuel\\|sauel\\|sāuol\\|suel-\\|sül-\\|s[āa]w[eo]l\" IEC.txt | head -20",
 "description": "Grep IEC for sauel"
}
```


### [2026-09-14T01:26:53.279Z] TOOL RESULT

```
8219:ksol- — ksül-
8232:ksül- ‘bent, askew, awry; athwart, across; thwart, crossbeam, rung, bar’. Cf. WP II, 503. (Variant: skúl-)
14318:quselið (qusəl-) ‘dance, cavort, caper, ramp- age, be wild, be mad Cf. qusoil- Skt. khalāmi, v. ‘move, shake’; Arm. cf. xayam, v. ‘play, dance’; xay, u-st. ‘play, game’; Per. (ambig.) šāram, v. ‘purl, babble’; W chwil, adj. ‘whirling, reeling’; Br. chwil, m. (?) (“beetle”; but a phonol. background *suel- or *suil- is possible); OCS šaliti, inf. ‘rave, rage’;
14379:qusül- a possible variant for items listed under ksül-, q.v. Cf. further ON syla, tr. & intr. ‘stiffen (with ice)
15034:sauel-, see saul-
15035:saul-, sáuel- ‘sun’. WP II, 446. (Indo-Iran. variant: sül-) Skt. cf. (z-gde) sürab, m. id.; Av. cf. hüro, gs. of hvaro, id.; Oss. cf. xur, Dig. xor, id.; Kurd. awer id. (and 'east); Scyth. (king's name) Saulius; Gk. helios, heélios, aélios (sic), id.; Lat. sol, cons. decl. m. id.; MIr. sól, id.; Gaul. sul- (in a name); W haul, pl. heu- liau, m., Br. héol, m. id.; Vannic dial. hiaol, m. id.; Cor. howl, m. id.; Go. sauil, n., OE Sol, n., Sw. sol, m. id.; ON sól, f. ‘sun, day”; Li. saulē, Latv. saule, f. id. (OCS slüníce n. ‘sun’ appears to be a cpd., cf. the Skt. variant sül- (*sul-) and (root of) Lat. nitere, nitidus?). Verbal types: Gk. héliázo, hélióo; Lat. solo, are, in-^; Icel. sóla, v. (a-stem); Sw. sola, v.; W heulo, inf.; Latv. saulot, inf.
16664:soleið (1) “be, dwell’. Cf. sól- above EMAIb. cf. gjell, v. ‘live’; Lat. soleo, ere, v. ‘be wont; cohabit with’; Go. saljan, wv. (1) ‘be, dwell’. (Sw. sóla, v. ‘stay, tarry? seems to derive from a type *suel-)
16665:soleið (2) “offer, yield, bid, afford, sell Go. saljan, v. (2) “offer, sacrifice; MHG sel- len, seln, v. ‘sell; OE sellan, v. “offer, give, supply, lend, promise, sell; ON selja, v. *yield, hand over, sel; Sw. sälja, v. ‘sell; till salu “for sale”; salu, cpds. sale-, id.; cf. ON sala, f. id.; OCS pra-soljo, -soliti, v. "sell": pra-solü, m. ‘vendor’; Latv. (long grade) solu, inf: solit, v. “bid, promise). (The source of Lat. solor, ari, v. ‘comfort, cheer, satisfy’ is uncer- tain, perhaps fr. *suel-)
17816:sül- (2) (variant of type sáuel-, sául-) “sun, light, eye Skt. sárab, m. “sun? beside süryab, id.; Oss. xur, Dig. xor, id.; Per. cf. nu-hür, s. “eye, sight, look, scowP (fr. *ni-^); Scyth. cf. oitó- suros, m. (epithet of Apollo); Alb. cf. yl-ber (rainbow, if fr. *suli-bher$- cf. ON sól-bjartr *sun-bright^); Ir. súil, gs: súla, f. “eye, look?
17817:sül- (sülos, à) (3) "liquor, issue, sludge’. Cf. sulu- & WP II, 453, 468 & 513 Skt. sürah, m. *soma-juice from press’; súrã, f. ‘liquor’; Av. hurā, f. ‘drink’; Oss. cf. xwlídz, Dig. xului, adj. & s. (` wet; wetness’. Cf. sulu-); Gk. húlē, f. (2) “mire, dregs, matter’; W hil, pl. ion, f. ‘outflow’, OHG sol, n. ‘mire, puddle’; MHG sol, sul, sf. ‘saline fluid; G Suhtle, f. “bog; sump; wallow of pigs’; OE sol, n. ‘mire, puddle’; adj. ‘dirty’; OFris. sol, s. ‘dirt; LG soll, n. ‘sump, catchment’; ON sol. cpds. id.; Norw. söle, s. (émud', fr. *sulu-); Icel. cf. sulla, v. ‘dabble, splash’; Finn. (LW) sula, adj. *molten, fluid'; Li. sulà, f. ‘sap’; Latv. süla, f. (pus, running sore’ beside sula, f. ‘sap’; OPr. sulo *curdled milk’; Gk. cf. hulízo, v. “strain, filter
17818:sül- (4) “substance, timber Gk. hülé, f. ‘substance, matter, faeces, waste’; OHG sül, pl. süli ‘pillar’; MHG sül, pl. siule, OS sül, OE syl, f. Du. zuil, f., ON süla, id.; (NB. Gk. hülé as *waste-matter' equates w. Latv. susla "wort, brew’. See suslà)
17819:sulis, os 'sending; dispatch; envoy'. Cf. sül- (1) Arm. (ambig.) hujik, pl. form “band, troop’; cf. h-yem, v. ( send’, *epi-^); Lat. cf. prae-sul, gs: -sulis, m. ‘prelate’; ex-sul ‘exile’; OW de- hol, mod. de-ol, m. ‘exile; OCS sülü, m. ‘legate’; Slovene sel, m. ‘delegate, messenger"; R po-sól, Cz. po-sel, m. ‘envoy’; Latv. cf. sulainis “servant”
17868:susla “fluid, liquor, Gk. ambig. Cf. sül- (3) Gk. hüle, f. ‘matter, phlegm’; Latv. susla, f. ‘wort, brew’; cf. suslàaju, v. “sip, sup’
17942:(suel-, cf. suelo, suol-; suél-, see suelo)
17948:suelo, ið (2) “turn, bring” Lat. cf. soll- in soll-emnis (*'annual', hence ‘ritual’; soll-ers, -ertis, (/clever, lit. *turn-skill, semantics of G ge-wandt, R oborótlivyj, Cz. obratný clever); cf. also con-sulo, ére, v. (“bring together”, fr. *kom-suel-) (variant con- solo); Olr. cf. sel, m. “turn, time, space; Ir. seal, pl. -ta, m. (id. and *course"); cf. sealán, m. ‘withe for faggots, rope’; W chwel, pl. -ion, f. ‘turn, course’; chwelyd, inf. ‘turn over’; dy-chwelyd, inf. ‘return’; Cor. whël, f. as W; de-wheles, inf. ‘return’; Du. zwelen, tr. ‘turn — hay’; Sw. söla, v. (Ctarry', phon. of Norw. sómme ‘swim’); Latv. svelties, rett, *hurtle'
17950:suelo "waste, consume’. Cf. suelo (1) Oss. cf. xwali, soht s. (corpse; Arm. cf. n-Koyem, v. (famish; faint w. hunger”, fr. *ni-suel-); EME sweal, v. ‘melt’; E dial. sweel away ‘die off" (isophonic in OE swælan, tr. ‘burn’); Icel. cf. sólunda, v. w. dat. tr. (^waste, consume’. Vocalism of sópa, v. sweep"); Lat. solo, are, v. (1) "lay waste’; (isophonic: Sw. svål, m. “horny skin, sward’; MHG swéllen, sv. 3. (2) *faint w. hunger?)
17951:suelos, ios “close relative'. WP II, 533 Per. (?) xalü, s. “maternal uncle’; Oss. cf. (?) án-suvar, üfsímàr (“brother? fr. *en-, *epi-^?); Hes. cf. aélioi, mpl. ‘men married to sisters in the same family'; Gk. cf. eilíones, pl. id.; Alb. cf. vlla, gs: vllau, pi. vllazën, T vë- llezér, m. (^brother', a synth. cpd.); Lat. cf. solus, adj. (alone; cf. sólor, àri, v. ‘cheer beside sodalis ‘comrade’; soleo, Gre, v. "be wont (Lat. forms fr. *suel- & *syel- 9); ON svili, pl. svilar, m. (brother-in-law^; pl. ‘men married to sisters of the same family")
17996:suer- (5) “post, pole, pillar, stump’. Cf. suir-. (Lat. ambig.) Skt. sváruh, m. id.; Gk. cf. hermís, gs: hermí- nos, f. id.; Lat. (ambig.) surus (“bough, stake, palisade’, fr. *suer- as in vocalism of vulva: Gk. eiláo or fr. type *guelbh-, oe: vult ^wishes', fr. *uel-, cf. (alleged) OLi. pa-velt, id.; or fr. *suir- as in vocalism of subitus, see suidh-, pudeo, fr. *po- or *pod-, and *uid-, q.V.) (for sul-phur cf. suel-, pür-, and for mulgeo cf. melg-)
18068:suil-, suilo, ið ‘swirl, spin’; suilos, à ‘whirl, turn; turning, going’. Cf. suelo (2) Gk. cf. íl-igx, -iggos ‘whirlpool’; íl-iggos, adj. ‘whirling’, MIr. seal, s. “turn, while; W chwyl, pl. -ion, f. ‘turn, while, course, event’; chwylo, inf. ‘turn’. (For Gk. ílé ‘troop’, see eil-; ambig. as also MHG swil-ch, swil-ich *sultry, warm', cf. suel-)
18137:suol- ‘tread, sole; threshold’. WP II, 532. (Variant: suel-) Arm. Kajl, Let ‘step, pace’; kalem, Kajlem, v. ‘march’; Lat. solea, f. ‘shoe, sandal’; OHG swelli, s. threshold; MHG schwelle, s & wf. ‘beam; threshold’; ON svalar, fpl. ‘balcony’; Sw. svale, wm. ‘entrance to cellar’. MHG swel,
```


## [2026-09-14T01:27:03.461Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('IEC.txt').read()\nimport re\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'sūl- (2)' in p or 'nu-hür' in p or 'nu-hūr' in p:\n        nums=re.findall(r'^\\s*(1[0-9]{3})\\s*$', p, re.M)\n        print('leaf',i,'page numerals',nums)\n    if 'saul-, sáuel-' in p or \"saul-, sāuel-\" in p:\n        nums=re.findall(r'^\\s*(1[0-9]{3})\\s*$', p, re.M)\n        print('SAUEL leaf',i,'page numerals',nums)\nEOF",
 "description": "Locate IEC leaves"
}
```


### [2026-09-14T01:27:04.748Z] TOOL RESULT

```
SAUEL leaf 616 page numerals ['1114']
leaf 734 page numerals ['1333', '1334']
```


## [2026-09-14T01:27:08.423Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"frn\\b\" SOD_pages.txt | head -20\necho \"=== farn\"\ngrep -n \"farn\\|xwarn\" SOD_pages.txt | head -20",
 "description": "Grep Gharib Sogdian for frn"
}
```


### [2026-09-14T01:27:08.499Z] TOOL RESULT

```
13675:         ob. ~yh ^SP'mfrn, db'mn
14396:                                                                                                                      Synyfrn
14456:     SCE 246                                                 3781 Synyfrn M                                                 jp'j
14465: 3783 Synyprn  S => Synyfrn
14643:                                                                     fa/an,    glory=>frn, prn1
14850:3914 frn     M, C                           j&*±y*-<.jii<j
20076:    5703 mzyyx M                                          J^j,        5714 n> "yt frn M                    (<jLjJ)Jdy*<<^i^
21220:6088 nstfrn M                             <^iT-S i
24370:     farn ©Av. xvardnah =>tw}prn(y), frn, fn
42162:                                                                                                             ^•vY^«vvfrifrn*Yr\r                j^>
44842:              frn^n^m^f^v                           c~ ^                                                                                  -»■■:                     f *#Y      -uj
=== farn
3165: /casn/      clnpre       thirst                                /farnxunde/ prnYwnS^k fortunate Av.xywarnahwant
8240:         oska-farn                                                   1561 'skr'nt- B                     j>/ji>j * j^j^T
14457:                                                                  8ene-farn (Synyprn) ©ob. -yy
14809:          467.41; frmWr-, Sund. AoFviii 1981 p214;                         farnxunde (prnywn8y) ©<Av. xvardtxahvant
14852:       farn ©<Av. xvardnah OP *farna           ©ob. ~y
14859:       farnPare =»pnu3rch
14865:     farn-waxsik        ©pi.                                              most, best
14872:       farnxund(a)c    ©f. adj.                                           improvement, increase
14877:     farnxundakya                                                         increase
16508:     xute-farnxwande
18978:     mand-farnakya
19797:          prn mySn, farn-meOan ?
20077:         mazex =»mzyx                                                      na-ayat-farn
21221:     nist- farn                                            6101 nw-2 M, S              o-kji ijXj<j~a\ ioiJ'^jp-
24343:     please                                                   farn- Pare ©f. adj. **frnPry
24348:        ^PrnVy-, prnVt-, prnVy, prm*y-, frm'y-                farn-Perte (prnPyrtk) ©OP vinda farna
24359:                                                              farnxwande, farnxunde (prnywntk)
24361:     parmene ?                                                  ©<*farnah-wantaka\
24370:     farn ©Av. xvardnah =>tw}prn(y), frn, fn
24386:         farnxundakya(k) (prnxwntky^h)                             7210 prst't-     S =4 prsty-
```


## [2026-09-14T01:27:17.543Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('SOD_pages.txt').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if '3914 frn' in p or ('farn ©<Av' in p):\n        print('leaf',i,'printed~',i-66)\n        print(p[:1500])\n        print('-----')\nEOF",
 "description": "Locate SOD frn page"
}
```


### [2026-09-14T01:27:18.687Z] TOOL RESULT

```
leaf 220 printed~ 154
                                                                                                        mMmmmmm           ^^WHiiiiiHiili&




 155

                                                                     3919 frnxwndy(y) M
        GMS 565, BBB; trans, pret. frrritd'r-. Hen. Tales.
          467.41; frmWr-, Sund. AoFviii 1981 p214;                         farnxunde (prnywn8y) ©<Av. xvardtxahvant
                                                                                                                 frtry>
          AVS 91
                                                                           BBB; GMS 939, 1092, 1241; frnxwnd, Frag. Lcn.
 3909 frm'tyty) M, C                             jjUJ<ij*J                   77R6
      framate ©pp. nom. n. -/w>; pi. -t
      ordered, commanded                                                   gloriousB, * M
                                                                     3920 frpws-                                     0*j<j=^W
        BBB 729; GMS 849; C2 gloss.                                        frapas (frp's-) ^Prp's-
                                                                           (^)throw, (/o)beat
 3910 frm'y-      M, C                     (Jj> s^ j*)o>j*J
                                                                           BSTBL, Dhy. 17, 134; Hen. JRAS 1944, 143.24
      framay      ©<*/ra-maya-         ©impf. f^rrty
          -^frnVt-, prm'y-1, Prm'y-                                 
-----
```


## [2026-09-14T01:27:22.781Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SOD_pages.txt').read()\npages=t.split('\\f')\np=pages[220]\ni=p.find('3914')\nprint(p[i-400:i+900])\nEOF",
 "description": "SOD entry 3914 frn"
}
```


### [2026-09-14T01:27:24.034Z] TOOL RESULT

```
      C2, 61R 22, 52V 10
         Prm'yst-
       (/o)spoil                                                     3925 frtp55 M                                        Ub«>tfT
       GMS 147, 327, 529
                                                                           f/ParatpaB ? (brtpd) ©*abi-(fra-rata- paOa
                                                                             ^PrtpS
3914 frn     M, C                           j&*±y*-<.jii<j
                                                                           informed
       farn ©<Av. xvardnah OP *farna           ©ob. ~y
         =»prn\ fn                                                         Sund. MSP p45

       glory, majesty, fortune                                       3926 frtr M, C                              y# <yj±j ij^>
       GMS 526; W-Li, ii; BBB; Tales. 470.50; BSTi 189                     fratar ©<Av. fratara ©pi. -t =»ft'r, prtr1, }Prtr
3915 frnpry      M                                                         more, better
                                            (jj^)jjtJtJ^AJ                BBB el2; GMS 437; STi 8.11, 10.11; C2, 120V2,
       farnPare =»pnu3rch
                                                                            48R18
       glorious, fortunate
       GMS 1132
```


## [2026-09-14T01:27:29.408Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nt=open('BQT_v3_pages.txt').read()\npages=t.split('\\f')\nprint(len(pages))\nfor n in (244,245,246,247,248):\n    p=pages[n]\n    print('=== idx',n, p[:60].replace('\\n',' | '))\nEOF",
 "description": "Locate BQT v3 pages"
}
```


### [2026-09-14T01:27:30.494Z] TOOL RESULT

```
721
=== idx 244 [pdf page 245] | فرخاد | وسختی والمی را بيزگویند که ب رکسی‌راقم‌
=== idx 245 [pdf page 246] | —~\ter— |  | مم درست است . |  | ف رخجسته ۱ - بن ناك ‎
=== idx 246 [pdf page 247] | فرخمید )۷ | فر خمید ۱ » بروزن(۱) شنبلید:ماضی | فر
=== idx 247 [pdf page 248] | -وو۱4- |  | ثانی بر وزن (۱) بر دمیدن » پیراستن در
=== idx 248 [pdf page 249] | فردین ۱6 |  | انگور را نیز گفته‌اند .* ‎Sa‏ در مق
```


## [2026-09-14T01:27:34.998Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nt=open('BQT_v3_pages.txt').read()\npages=t.split('\\f')\nfor n in (237,238,245):\n    print('##### idx',n)\n    print(pages[n][:3000])\nEOF",
 "description": "BQT v3 farr pages"
}
```


### [2026-09-14T01:27:36.051Z] TOOL RESULT

```
##### idx 237
[pdf page 238]
سووعوت
قراخ ‎gi‏ - کنابه ازبتتابوسبیل
رفتن باشد .
‎O18‏ و ۱ - بنتهرایبی قطه,تمجیل
و شتاب رونده را گویند - و کنایه از کی است
که ازحد خود بیرون رود- ومسرف وعرزه‌خرج

,\ نیز گویند ۳ - وم رای قرشت (۱). مردم
کشاده رو وشکفته وخندان باشدو ککه‌پبوسته

بیش و عشرت کنراند و با مردم خوش ‎AS‏
‎FS‏

فراخنا ۴ بانون بروزن هزارپاء,بمعنی

(۱) چك : و پم را .

- از: فراخج (-رو (رونده ). رك: فراخ رفتن .
۴ - از: ‎ites‏ (پسوندساختناسم ازصفت) [فس:ژرفناء تنگنا] س فراخی س

فرارون

PUD ‏است که فراخی و کشادکی- ومحل‎ ELS
. ‏وکشاد کی باشد‎

فراخود * ‎she‏ مسوله بر وزن
تفاخر » بمعنی شاسته ولایق وسزاوار باشد .*

فراخیدن ‏ بر وزن دوالیدن » موی
دربدن برخاستن وراست ابستادن‌باشد9 - وبمعتی
‎ail‏ جدا کردن هم هست" .

hy ‏بفتح اول بر وزن‎ ۰۷ ots
‏چوبی را گویند که در پس در(۲) اندازند‎
‏فرادون ۵ - با رای بی نقطه بر وزن‎

. ‏چك : کوچه‎ (x)

۴ - رك: فراج روی .(حاشیه)
فراخا .

۴ - از:فرا (پیشوند) ‎TH‏ خور (خورنده) > درخور,درخورد ورك: اسشق4*4دورك: فرا .

۵ -فی : خیدن . ‎am)‏
‏۷ - از : فرا۳- در فردر کت فر

از : فراخ ‎ab‏ (پوند مسدری ) .
دره . قس : فرآوند .

) ‏تقوی » استفامت‎ ( frarénth ‏مستفیم . راست ) و‎ . dle ( ]۲2۲۵0 ‏پپلوی‎ - A

« منای ۲۷۳ :۷ * در لفت فرس ص ۳۷۸ آمده : * فرارون, ‎SIS‏ بیابانی‌است ‎A WIT.‏
باز پیش بود . دقیقی (طوسی) کوبد :

حسوفت در ید ( بد . دهشدا ) بهرام فیرون نظر زی تو ز برجیس فرآرون . »
فرارون بمعنی پا کدامن ونیکو کردار ‎jee py‏ کار درمقابل لفت > اوا رون > بمعنی گناهکاروشریر
آمده , هیچ ربطی با کواکب بیابانی ندارد . ( صادق هدابت . مجلةٌ موسیقی سال ۲ ‎CA Slat‏
ورك: بشتپا ۷ ص ۱۷۹ متن و حاشیه ؛ نب ر کلص ۷۲ - ۷۳ ‎aS‏ : پهلوی ۲۵۲۵۵ ‎cool)‏
‏درست, درستکار ), پازند ‎frardin‏ , از ابرانی باستان - 01۳8۳0۳2۷38 ‎wofrardha_)‏
‏_ 2۳0808 - ۵178 ( بجلو جاروب کرده (. فی 20372 و 208۲۵0 ‎Jy.‏ فربرون .

۵ فراع روی - ‎dol cle‏ و دوم و پنجم ؛ از : فراخ رو ی ( اسم مستر ) ؛ زباده
روی ۰ خرج کردن بهوده » اسراف
مکن ‎ela‏ روی درعمل» اکرخواهی که وقت رفع توباشد مجال دشمن تنگه.

« گلتان ۳۹ ۰ .

۵ فراخی - بفتح اول ‎le‏ فراخطی ‎el)‏ مصدر ) < ‎EL‏ فراخنا. پهلوی

0 -« تب رک ۷۱ » کردی ‎ferehi‏ , 86۳8 ( عرض . فراوانی ) « ژابا ص ۷۹۲ :
‎SLT‏ وسمت » عریضی » پهنا . ضد : تنگی :
فراخیها وننگیهای اطراف ز رای پادشاه خود زد لاف.

نظامی گتجوی ( لت نامه : لاف زدن ).

##### idx 238
[pdf page 239]
فراز
فلاطرن , کسیرا و چیزیر! کویند که نه بطریق
‎He THe‏ پس رود. یمنی روز به نباشد وروزبروز
پي رود .

‎ILS‏ ۷ - بروزن نماز . چندممنی‌دارد:
۱- پهن شده و پخش کردیده باشد . ۲ - بسته
و کشاده و ‎He‏ کرده شده - و باز کردن و کشودن
وپوشیدن درباشد ۴ « وباین‌معنی ازاضداد است.
۳ قریب ‎Cho gy‏ وپیش وحضور باشد. 4-جمع
وقراهم‌آمده راکوبند . ه - بمعنی ‎am‏ از یين
و ازین باز باشد . ‎٩‏ - پمعنی عقب و پس باشد
چنانکه کوبند « فراز ده»بعنی پس‌بده. ۷-بمعنی
پاز باشد که از تکرار است چنانکه کوبند «فراز
ده * ‎te‏ باز بده ومکرر بده. ۸ بممنی زمان
باشد چنانکه کوبند « ازسباح فراز» بعنی‌ازسباح
بلز و ازدیروز فراز - بضی ازدیروز باز-انتظار
میکشم ». ‎٩‏ بمملی فروز باشد کداز افروختن
است . *۱- بالا وشیب وزیر وزیر را گویند۴ ؛

‏و باين ممتی هم از اضداد است ۰ ۱۱- بمعتی
بلند وبلندی آمده‌است ؛ و باینمعنی بروزن‌حجاز
هم گفته‌اند - وامر بدین معتی‌هم‌هست بمنی‌بلند

‏ووع اس
شو و بالابرو ؛ واسم فاعل نیز آمده است که‌بلند
شونده وبالارونده باشد . ۱۲- س رکش‌راگویند
عم از مردم نافرمان واسب س رکش. ۳-بمعنی
آلت تناسل ‎gas -۱6 ۰ ath‏ وصل باشد چه
فرازیدن وصل کردترا نز کوبند ‎Ne.‏ زیاده
۹- بمعنی در آمین و فرأرفتن
باشد . ۱۷-در نخه ‎sy‏ بمعنی خون نوشته

‏وزایده باشد .

‏بودند که عربان دم خوانند .

‏فرازمان ۴ = بامیم‌بالف کشیدموینون
زده ؛ حکم وفرمانرا گویند.

‏ق استه }5 ؟ ‏ - ۲

‏فر ‎Bgl‏ = بفتح او و سکون
مين بی نقطه + بمعنی پرستولك است که خطاف

‏قراسو۵ه * = بروزن ناسوده. ‎wins‏
‏بسبار کهنه شده وازهم رفته باشد.

‏قر اسیاب »= بنتح اول .مخفف افراسیاب
است که ‎teal‏ تر کستان بوده ‎٩‏ - وبمعنی‌حباب
هم‌آمده است وآن شیشه مانندی باشد که‌ببب
پاریدن باران بر روی آب بهم میرسد ۷

‏۱ - پهلوی ‎frie‏ ( بهپیش , جلو . باینجا ) از اوستا - ‎frank‏ « بارنولمه۱*۲۵*.
پلزند 16820 ۰ ‎fraz‏ « نب رکه ص۷۰ ۰ . هندی باستان - ۳۳406 ( سانسکریت - ‎prac‏ 4
‎Ge)‏ جلو) . استی ۲42 ( از پیش ) « استق ‎ANN‏ ؟ - ‎ote gee‏ وبا :

‏کس نبیند فرو شده بنشیب
‎ap‏ و کینش مثل دو دربانند
بر بد اندیش او فراز کنند

‏هر که را خواجه برکشد بقراز
در دولت کنند باز و فراز
باز دارند بر موافق باز .
« فرخی سیستالی ص۲۰۳ * .

‎SL, - ۴‏ دساتیر < فاب ص4۷ ۰« فرهنگه دساتیر ص ۲۵۹ ۰۶ تصرفی‌درفرمان».

‎el pe dk jp, le, clin‏ که پرستو ‏ پرستولك.دراوراق‌مانوی
(یارتی) ‎Henning ,A list of Middle Persian, BSOS,|X.1.V.p.86.prstwg‏

‏ای‌قحه بتلزی‌بدف ودوك (چه بازی بدف زدوك . دهضدا)

‏۰ فرنوده.

‏۱ رك : افراسیاپ .

‏مسرای چنین چون فراست وکه.
زری نکتاب. « لغت فرس۲۷4 ۰ .
۷ رك : افرای‌آب .

##### idx 245
[pdf page 246]
—~\ter—

مم درست است .

ف رخجسته ۱ - بن ناك ‎chs‏ جم
و سکون سین ؛ بمعنی مبارك و میمون ‎Fath‏ -
ونام نوعی از کل است (۱) - و مطرب وسازنده
را نی زگوبند .

فرخجی ۷ = بفتح اول وثانی‌وسکون
ثالت وجیم بتحتانی کشیده ۰ بمعنی پلشتی وزشتی
وزبونی وبدی باشد .

فرخخ دود ‎che‏ اولون‌نیانشدید
و سکون تالت و رای بی‌نقطه بواو کشیده وبزای
نقطه‌دار زده ۰ نام پرد‌است ازموسیقی وصونی‌از
مصنفات باربد . و بقول شیخ نظامی نام‌لحن‌بست
وهفتم است ازسی‌لحن باربد .

‎O19 ES‏ - با زای قطه‌واربالف کشید.
و بدال بی ‎Abe‏ زده ۰ بمعنی مبارك زاد باشدچه
فرخ ‎om‏ عبارك آمده است - و نام فرشته‌ای‌هم
— موکل بر زمین +

‏9 خسته = بفتح اول والك بروزن سر

‏(۱) چك : کلست .
)£( چك : قطائف .

‎. ‏چك : قطائف‎ (x)

‏فرخشه

‏بسته » بمعتی خنته و برزمین کشیده باشد؟ .

‏فرخش * = بنتح اول و تانی بروزن
بدخش ۰ بمعنی کفل اسب واستر و کاو و دبگر
چهار پایان باشد .

‎GSS‏ = بروزن ب رکشته » نانی‌باشد
کوچك که از خمیر سازند و درون آنرا از مغز
بادام و پسته و لوزینهای ‎Sar‏ پر ‎PES‏ برروی
تایه پزند و شیر قند بر ‎OT‏ ربخته بخورندو آترا
بعربی قطابف(۲) خوانند ‎٩‏ - و بمعنی ‎ors‏
‏کشیده هم‌آمده است ۷ ۰

‏فرخشور ۸ = بفتح‌اول‌وثانی‌بروزن(۳)
سقذقور . پیفمبر و رسول را گویند .

‏فرخشه * - بفتح ‎Jal‏ وثالك و رابع»
بمعنی فرخشته است که نان کوچك پر مغز پسته
ولوزینه ‎ath‏ ؛ و بستی گویند نانی است که از
نشاسته و لوزینه پزند و بمربی قطیفه خوانند
و پضی دیگر کوبند فرخشه ‎a)‏ قطایف (4)

‏است .

‏(۳) چك : بوزن .

‏۱ - از : فر (پیشوند) + خجته ‎Cen)‏ اسشق ۸۰۷ .
۴

‏- این غم ‎Jo‏ برد يك ره ‎Ope‏ هزیمت کشت برد

‏فر خسته فر فروردین پدید آورد ورد .

‏: فرخج (رك : ‎SHES‏ ( اسم مصدری ‎A‏

‎.> ۱۳ ‏رازی « ترجمان‌البلاغه ص‎ o ple
Haye) ‏ر ۴ - از:‎

‏خته («.م.) « فرخته ‎A‏ برزمین کشیده بود . ابوالعبای عباسی گوید :

‏او می‌خورد بشادی وکام دل

‏۵ برخش ‎Gen)‏ .
ات . رودکی (سمرقندی) کوید :
‎SLL,‏ بره است و فرخشه برخواش

‏۷ - مصحف و مبدل « فرخسته © ‎pm)‏

‏دساتیر « فرهنگه دساتیر ۷۵۹ .

‏دشمن نزا رکشته و فرخته. »

‎4۹۵ ‏فری‎ cad?

‎pl - 1‏ معنی «فرخشه « فطایف باشد» زبان‌ماوراءالنهر

‏وب سک اکه جوین‌نان همی‌نیاید میر.»
لت فری ‎atv‏

‏۸ - مسحف « وخشور © ‎pa)‏ از

‎. ‏رد : فرخشته و ح؟‎ ٩
```


## [2026-09-14T01:27:51.904Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nt=open('BQT_v3_pages_faseng.txt').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'farr' in p or 'xvarnah' in p or 'hvarnah' in p or 'farnah' in p or 'xwarrah' in p:\n        print('=== pdf page',i+1)\n        for line in p.split('\\n'):\n            if 'farr' in line or 'arnah' in line or 'xwarr' in line:\n                print('   ',line.strip()[:200])\nEOF",
 "description": "Find farr etymology footnotes in BQT v3"
}
```


### [2026-09-14T01:27:53.242Z] TOOL RESULT

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'BQT_v3_pages_faseng.txt'
```


## [2026-09-14T01:27:55.659Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; ls",
 "description": "List BQT incoming"
}
```


### [2026-09-14T01:27:55.724Z] TOOL RESULT

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
```


## [2026-09-14T01:28:00.162Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 -c \"\nimport json\nm=json.load(open('BQT_v3_pagemap.json'))\nprint(type(m), list(m)[:5] if isinstance(m,dict) else m[:5])\n\" \necho \"---\"\npython3 - <<'EOF'\nt=open('BQT_v3_pages.txt').read()\npages=t.split('\\f')\nimport re\nfor i,p in enumerate(pages):\n    if re.search(r'فرّ|فرّ', p) and ('اوستا' in p or 'پهلوی' in p or 'پپلوی' in p):\n        head=p.split('\\n')[1][:50]\n        print(i+1, head)\nEOF",
 "description": "Check pagemap and find farr"
}
```


### [2026-09-14T01:28:01.286Z] TOOL RESULT

```
<class 'dict'> ['pdf', 'pdf_pages', 'offset_mode', 'anchors', 'map']
---
```


## [2026-09-14T01:28:04.393Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nimport json\nm=json.load(open('BQT_v3_pagemap.json'))\nprint(m['offset_mode'], m['anchors'][:5] if isinstance(m['anchors'],list) else m['anchors'])\nmp=m['map']\nfor k in ['1443','1451','1447','1448']:\n    print(k, mp.get(k))\nEOF",
 "description": "BQT v3 pagemap lookup"
}
```


### [2026-09-14T01:28:05.458Z] TOOL RESULT

```
1203 34
1443 236
1451 244
1447 240
1448 241
```


## [2026-09-14T01:28:08.319Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nt=open('BQT_v3_pages.txt').read()\npages=t.split('\\f')\nfor n in (236,244):\n    print('##### pdf page',n)\n    print(pages[n-1][:3500])\nEOF",
 "description": "BQT printed 1443 and 1451"
}
```


### [2026-09-14T01:28:09.362Z] TOOL RESULT

```
##### pdf page 236
[pdf page 236]
oN Efe

ودبوث هم حست - و بزبان ‎blk‏ خوردلی
و طمامی باشد که در دستمال (۱) بسته از جایی
بجایی برند - و بیعنی دستور هم بنظر آمده

است .

قدرو نك ‎bw‏ رای قرشت (۲) ‎ogy‏
‏بروزن(۳)زتبورلك سنگی‌را گویند ‎yi‏ کنگرهای
قلمه و حصار گذارندتا چون دشمن ‎sls‏ حصار(4)
‎aT‏ پزسرش اندازند .

وا

فدده ‎the‏ اول ورای‌قرشت وسکون
‎ploy Jt‏ باشد که ازب ‎EF‏ خرعا و غیرميافند
وبربالای ‎lege‏ و پروار های سقف ‎ale‏ ادازند
وخاك وکل بر ‎OTE‏ ریختهخاك بیندازس(ه).

قدو ند ‎Slate a)‏ و راو ‎wing‏
‏بند» بمعنی‌اول فدرنگ است ‎Oly‏ چوبی باش د که
در پي در اندازند: تا درکشوده نگرده +

بیان ششم

در حرف فا با رای بی نقطه مشتمل بر سیصد و نوزده لغت و کنایت

قر ۴ « بنتح و سکون ثانی ۴ » بععنی
خأن و شوکت ورفت وشکوه و سنکه و هنگه
باشد - وبمعنی نورهم گفته‌اند چه‌مردم لورانی‌را
فرمند و فرهومند گوبند - و بععتی برازی
و برازندکی وزیبا و زیبایی و زیبندکی‌تیز آمنه
است - وسیلاب را هم گوبند - و بمعنی مطلق
‎ol Fat,‏ زیر مرغ خانگی و پرمرغان‌دیگر

- و با تشدید ثالی در عربی » بمعنی گرینتن
و گربزان شدن باشد 8 - و نم اول ‎BET‏
‏بهودانرا میگویند .

‎Vs‏ = بروزن سرا : بمعنی‌سوی‌وطرف
و جانب - وکنج و گوشه باشد - و ‎te gins‏
ویتتر و ميان و وسط هم آهده است - وبمعنی

‏بالا و بلندی وقریب وبعید بعنی دور و تزديك‌هم

‏(۱) چك : ‎glazes‏ .
(4) چك : دیوار .

‏۱ -ظ . ممحف «فدرنگ» .

‎. ‏چك : بارا‎ (x)
. ‏چك : پیندایند‎ (0)

‏۳( چك : بوژن ۰

‏۴ - فر ‎qe)‏ وبکراول) پیشونداست بمعنی پیش ۰

‏جلو,بسوی‌جلو وغیره؛ چنانکه‌در کلمات: فرخجته. قرسوده» فرمان؛ درپارسی باستان واوستا ‎fra‏
‏پهلوی £18 « ارمنی ع - ۱۲۳۵, ‎jae‏ پاستان ‎hal. hil - 6.55% pra‏ « استق ۰۸۰۷ .

‏۴ - غالبا حرف‌دوم آن مشدد است ‏ فرء س خره ‎(pe)‏ » قی خورنه ( معرب:خورتق)؛
پارسی ‎ott‏ ۷180368۳02 (درحاات فاعلی. اصل- ‎xvarenaht_,\ . (Vindafarneh‏
‎Oe (‏ روتق ) , ارمنیع ]۳87 , پازند ‎xvateh‏ فارسی ‎war‏ فرخ ۰ فرخنده ‎ES‏
‏فرهي از هبین ریشه است « اسثق - هوبشمان ‎CATA‏ رجوع بشرح یکه ذیل «خوره»آمدمورجوع
بحکمت اشراق بقلم نگارنده . تهران ۱۳۲۹ ص ۲۵ - ۳۰ شود ورك :کیان خره » ورج .

‏۴ پر (هم) .

‏۵ رك : شرح قاموس ۰ منتهی‌الارب .

‎fara - ۱‏ پیشوند ( & بسوی .5( = مانکرت ‎prak‏ ( پیش . جلو ) اوستا
‎fra_‏ در - ‎_fra[keresta‏ 610072 ]۲۵] , در : فراخور , فرارسی‌دن » فرا گرفتن آمده
« استق - هویشمان ۸۰۹ و رك : ص لح از ديباچة مولف .


##### pdf page 244
[pdf page 244]
60۱

و رابع و رای قرشت » بمعتی عکس باشد؛ و با
رابع‌مجهول بروزن مخمور, یز همین معنی دارد
که عکس باشد .

‎J‏ وگ ۱ = ‎dle ain‏ بمه‌نی
بر-تواست و آن‌مرغی‌باشد که بعربی‌خطاف ‎A SF‏

‏فرج © بنتح اول؛بروزن ومعی ارج‌است
که بمعتی قدر و قیمت و مرتبه وحد ‎Fath‏ -
ودرعربی‌بمعنی شکافتن و وابردن اندوه - وشکاف
چیزی - و سوراخ پس وپیشآدمی- وجای ترس
‎gee‏ - وما ‎ow‏ هردو پای اسب باشد ۴ .

‏فرجاد ۴ ‎ele‏ بروزن فرهاد »
بمعنی فاشل ودان#مند ‎atl,‏ 2

‏فرجاد - با جیم . ممرب‌پر کازاست 8
‎Tol,‏ باشد که ‎Oly‏ دابره کشند.

‏5 جام 1 ه بروزن و معنی انجام‌است
که ‎aes‏ انتها وآخر بائد .

‏ف جامگاه ‎GEL oo‏ فارسی بر وزن
بهرام شاه ۰ به‌عتی کور است که قبر باشد وآن
جابی است که آدمی را ‎aa‏ ازرحلت ازدنبادران
جا نهند .

‏)1( چگ : سو

‏۱ - ممحف * فرستوك » ‎Cem)‏

‏۱) چك :

‏فرخا

‏ف رجف - بوزن ‎camel‏ پدر جد را گویشد

‏که پدر سیم (۱) است خواه مادری باشد خواء
پدری .

‏فر منك ۲ ه بروزن و معنی ارجمند

‏است که صاحب و خداوند قدر و مرتبه باشد -

‏وبمعنی زيبايي هم آمده ات
قرجود * » بر وزن متمود ۰ ‎gon‏
‏معجزه و اعجاز باشد » و اعجاز خلاف عادتی‌است
که از انبیا و کرامات از ‎Uy!‏ بظپور میرسد.
فرح - بتح
نقطه‌دار ‎OTL‏ . بمعی مبارك وخجته ومیمون
‎ath‏ - و بمعنی زیبا روی‌هم آمده است‌چه‌اصل
‎ol‏ لغت فررخ است . فریمعنی ‎bed‏ ورخ رویرا
کویند ‎٩‏ - و نام روز دویم ‎)٩(‏ است از ‎Las‏
‎oo‏ سالهای ملکی - و بنتح اول و ثانی
ساکن. درعربی جوجة ‎gp‏ خانگیباشد وشات
تازه را نیز گوند که از تخم ودانه سر بر آورده
‎ath‏ ونزديك بان شده که دوسه شاخ شود*۱.
فرخا ۱ خای نقطه‌دار بروزن فردا .
بمعنی فراخی و کشاد کی باشد ‎٩۱‏ - و محنت

‏ار وضم تانی مشدد وخای

‏دوم .

‏۴ - رك : ورج » فرجمند .

‏۴ - (عر) فرح ( پفتح اول ) اندام شرم جای - جای ترسنالك - شکاف ‎Qe‏ هردو ‎Sh‏
‏اسب کشادن ‎ph‏ دوچیز را - دور کردن غم . ركث : منتهی‌الارب » شرح قاموس .

‎pF sl Sisk, . ‏ظ‎ - ۴
‏از‎ frajaminitan, frajam ‏مناسی ۲۷4 » و‎ « frazham ‏پپلوی‎ - ۲

‏ص ۲44 .

‏6 رك : پرکار » ورك : دزی ج ۲

‏پارسی باستان ‎ofrajdma_‏ ( از ‎gam_ in,‏ « رفتن ») « استق ۸۱۸ ‎٩‏ < انجام وفرجلم. آخر

‏کار بود ۰ فردوسی (طوسی) کوید :
بکوشیم و فرجام کار آن بود

‏کد فرمان و رای جهانبان بود.»

‏«لفت‌فری ۳۳۹ >.

‏۷- از : فرج («م.) + مند ( پوند اصاف ) . ۸ - از ‎als‏ « فرهنگه
دساتیر ‎٩ . ۰ ۲۵٩‏ - در پپلوی 8۲12۷( تابان . مجلل » پرتوافکن,زیبا «خوشبخت).

‏ایرانی‌باستان ‎ofarnahva‏ , ازن)20 01860210۷ از- ‎ohvarnahvant‏ , قی : فارسی:

‏فرخنده « تیب کك ص ۷۶ » و ‎dy‏ : اسشق - هویتمان ۸۰۸ .
دفراخا ۲ ‎Cea)‏

‏شرح فاموی . ۱ - مخفف

‏۱ رك : منتهی‌الارب .
```


## [2026-09-14T01:28:32.372Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"##### v2 leaf 249 (printed 789)\"\nawk 'BEGIN{RS=\"\\f\"} NR==250 {print}' BQT_v2_pages.txt | head -45",
 "description": "BQT printed 789"
}
```


### [2026-09-14T01:28:33.458Z] TOOL RESULT

```
##### v2 leaf 249 (printed 789)
```


## [2026-09-14T01:28:36.616Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt').read()\npages=t.split('\\f')\nprint(len(pages))\nfor n in (248,249,250):\n    print('#### leaf',n)\n    print(pages[n][:2500])\nEOF",
 "description": "BQT v2 leaves 248-250"
}
```


### [2026-09-14T01:28:37.785Z] TOOL RESULT

```
684
#### leaf 248
           ‫ات‬
            ‫سپو‬                                                                                                       ‫خوره‬


 ‫خورة استخر »‪.‬خورة داراب » خورة شایور‪ .‬خورة‬                               ‫بوری است از جالب خهای تعالی که بر خلابق‬
 ‫قباد ‪ - ۴‬و ناممرضی است مهلك وانرا بعربی‬                                  ‫بوسله آن فادر شو ند بر باست‬     ‫که‬    ‫فار مشود‬

 ‫جذام خوانند؟ ‪ .-‬ویفتح اول وسطون وفتح ثالث‬                                ‫وضمتها ‪ .‬و ازین نورآ نجه خاص است‬            ‫وخ_فتها‬
 ‫است که‬               ‫درختی‬    ‫آڼ‬    ‫‪9‬‬   ‫‪۰‬‬
                                             ‫خر زهره کروایند ‪۴‬‬             ‫بیادشاهان بزر که عالم و عادل تعلق مبگیرو ‪-‬‬
     ‫رت اف سای ‪۶‬‬                                      ‫و‬    ‫کان‬
     ‫بمعنی پابمال هم آمده اس‬                      ‫و‬   ‫دفلی خوانند ‪-‬‬        ‫<سد‬   ‫حکمای فری‌فاری رایپنج حصه کرده‌اند وه‬

‫ار‬        ‫|نرا بر‬
                ‫ا‬       ‫کد‬     ‫‪۵‬‬    ‫ی‬
                                    ‫اول نوعی از جوال ا ت‬       ‫وسم‬       ‫‪ :‬خورءا ردشیر ‪.‬‬   ‫ترهب‬
                                                                                              ‫نام نهادهأ ند ماين ت‬   ‫را خوره‬




     ‫=) است ( رک ‪ :‬خورة آردشیر) مجازاً‬
                                     ‫‪ - ۱‬ماین معنی نیز مأخوز ازه‌منی خوره ف(ر‬
     ‫خوره ( = خره ) را یمعئی ناجیه و بخش گرفته اند و اختصاص بقاری ندارد ‪ .‬معرب آن‬
     ‫«ولات پاری بنج کورندت ‪ .‬هر کورتی بیادشاهی که نهار آن‬                                                  ‫«کورة » است‬
         ‫‪۰‬ورة دارایجرد ک‪.‬ورء اردشر‬
                                 ‫کورت بکاغرادزها‌واست‌بازخوانده‌اند برین جملت‪ :‬کورة اصطخر ک‬
     ‫خوره » کورة شاپورخوره ‪ .‬کورة قبادخوره ؛ وهر کورتی ازین پنج کورت چند شهرونواحی است ‪».‬‬
     ‫‪ ۴‬باین معنی از ‪ :‬خور (خوردن ) ‪» +‬‬          ‫د فارسنامة این‌البلخی ‪ › ۱۲۱‬و ركه ‪ :‬خره ‪.‬‬
     ‫بخورد ودناابونددگمراتند زنگه‌ودیو کودغاتغر ابا‬                          ‫(یوند نبت واتصاف) هرچیزی که ‪0‬‬
     ‫‪.‬‬      ‫ود‬    ‫»‬    ‫خر ره‬   ‫‪۰‬‬    ‫حوره‬     ‫رک‬              ‫(ظم‌الاطباء) ‪ .‬راجح بجذام ‪ ,‬رکه ‪:‬بحرالجواهر ‪.‬‬
                                                                                                         ‫وجذام نا‬
                                                                                                    ‫دقیقی (طوسی)گفت ‪:‬‬
                                                                      ‫دفلی است دشمن من و من شهد چان نواز‬

#### leaf 249

#### leaf 250
```


## [2026-09-14T01:28:49.619Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt').read()\npages=t.split('\\f')\nprint(len(pages))\nfor n in range(386,402):\n    p=pages[n]\n    first=[l.strip() for l in p.split('\\n') if l.strip()][:3]\n    print(n, first)\nEOF",
 "description": "Scan BQT v1 leaves near 180"
}
```


### [2026-09-14T01:28:50.734Z] TOOL RESULT

```
777
386 ['انجین', 'از توابم بزد - و ناوچهٌ مقمد و سوراخ کون را', 'نیز گویند ٩\u200f . #']
387 ['-۱۹۹ -', ')اد « بروزن پرواژ ؛ ممنی شسد -', 'و میل نمودن - و حمله کردن باشد - و امر']
388 ['اندر خور', 'ا ندز خو در - بنمخای نفطه\u200cداروسکون', 'واو ممدو له و رای می\u200cنقعله 4 ممحنی اج وسزاوار']
389 ['اف', 'او رفتی . بکشب بای شد و آتش را بکشت', 'راندروی درمیان دربا کم کردید ..']
390 ['انسجان', 'که کرفتگی دل ودلگیری باشد .', 'اندهان بروزن مردمان ؛ جمم انده']
391 ['رن', 'ار ه- باازای فارسی بر وزن غمزه ؛', 'مرجماث باشد و آثرا ببربی عد ی گویند .']
392 ['اگارده است که افسانه و سر گذشت باشد .', 'انگاده ۱ ه بروزن عموارء ."هر چیز', '"که افانه وس گذشت داشد - وباد گذشتها کردن']
393 ['مردم فررنگ «م هست ٩\u200f ۰', 'الث و زای قطه\u200cدار ساکن » سلی باشد که بآن', 'زمن را هموار ساز ند ۹']
394 ['انگشت ب حرف\u200cنهادن - کنابه', 'ازعیب کر فتن ودکته گیری کردن باشد .', ') نگشت بر دهان گد اشتن- کنابه']
395 ['یاف', 'چنکالی ومالیده 3۳ وان یش کی', 'با روغن وشیرینی بهم\u200cبمالند .']
396 ['انگوز زیتونی . .', 'وبعربی اصابع\u200cالمذاری گوبند .', ') نگوژه؟ - با زای فارسی بر وزن']
397 ['نوهیان - بکرم بروزن\u200cمجوسیان.', 'لاله باشد » و درصحاحالادوبه بهمین ححنی\u200cباسقاط', 'نون آخر آورده\u200cاستو گفنهاست که\u200cاین لفت\u200cروهی']
398 ['کوبند که بدشواری از انا شود و حل', '9', '| ثیشه - بر\u200cرزن\u200cهمینه .جاسوی\u200cوچاپلوی']
399 ['رل اس', 'یفکن - و بشم اول ناله و زاربراگویند . *', 'او باریدن ۱ - بنتح اول بروزن سر']
400 ['واجب و بفستا وا گیبتد و جر هی اهنت »', 'و آن\u200cقدارست ازسرانگشت ,کوچك ۷ مرانگشت', 'بزر که دست آدمی ۰']
401 ['ای ۸ اه', 'نیز خواشد ره ۳', 'اورمز ۱ نم اول و میم و سکون']
```


## [2026-09-14T01:29:14.118Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt').read()\npages=t.split('\\f')\nimport re\nfor i,p in enumerate(pages):\n    if 'فریبرز' in p or 'فربرز' in p:\n        print('leaf',i,'printed~',i-210)\nfor i,p in enumerate(pages[370:410],370):\n    m=re.findall(r'[۰-۹]{3}', p[:200])\n    print(i, m, [l.strip() for l in p.split('\\n') if l.strip()][:1])\nEOF",
 "description": "Search BQT v1 for Fariborz and page numerals"
}
```


### [2026-09-14T01:29:15.195Z] TOOL RESULT

```
370 [] []
371 [] ['حم اي ٩\u200f سه']
372 [] ['آزامه']
373 [] ['7 وه']
374 [] ['(که ۰ ۰ ی']
375 [] ['- ٩ پاي\u200e --']
376 [] ['الرك- بفتح اول و انی و سکون را']
377 [] ['-- هي ٩\u200f ح']
378 [] ['او فد بروزن و معنی اروند باشدکه']
379 [] ['2']
380 [] ['که زر بائد! .۷']
381 [] ['یوتانی۱ وممنیآن\u200cبفارسی « سنگه زاییدن آمان']
382 [] ['اتبارش']
383 [] ['سب ی ٩5\u200f']
384 [] ['انج - بفتح اول وسکون ثانی و جیم»']
385 [] ['- بو -']
386 [] ['انجین']
387 ['۱۹۹'] ['-۱۹۹ -']
388 [] ['اندر خور']
389 [] ['اف']
390 [] ['انسجان']
391 [] ['رن']
392 [] ['اگارده است که افسانه و سر گذشت باشد .']
393 [] ['مردم فررنگ «م هست ٩\u200f ۰']
394 [] ['انگشت ب حرف\u200cنهادن - کنابه']
395 [] ['یاف']
396 [] ['انگوز زیتونی . .']
397 [] ['نوهیان - بکرم بروزن\u200cمجوسیان.']
398 ['۱۵۰'] ['کوبند که بدشواری از انا شود و حل']
399 [] ['رل اس']
400 [] ['واجب و بفستا وا گیبتد و جر هی اهنت »']
401 [] ['ای ۸ اه']
402 [] ['آوروختن']
403 [] ['ی و ای']
404 [] ['اوستا']
405 [] ['کردن باشد و آلرا بعربی جارت خوانند که']
406 [] ['ی']
407 [] ['٩ لب\u200e']
408 [] ['اومالی']
409 [] ['٩۸4 -']
```


## [2026-09-14T01:29:27.006Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'برز' in p and ('بلندی' in p or 'قامت' in p):\n        print('leaf',i,'printed~',i-215, [l.strip() for l in p.split('\\n') if l.strip()][:1])\nEOF",
 "description": "Find borz in BQT v1"
}
```


### [2026-09-14T01:29:28.144Z] TOOL RESULT

```
leaf 444 printed~ 229 ['با کیده']
leaf 474 printed~ 259 ['برزستد ۱ 3 ۰ ج ووات']
leaf 592 printed~ 377 ['پتفوز']
```


## [2026-09-14T01:29:36.261Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt').read()\npages=t.split('\\f')\nfor n in (394,395,396):\n    print('#### leaf',n)\n    print(pages[n][:900])\nEOF",
 "description": "BQT v1 leaves ~printed 180"
}
```


### [2026-09-14T01:29:37.256Z] TOOL RESULT

```
#### leaf 394
انگشت ب حرف‌نهادن - کنابه
ازعیب کر فتن ودکته گیری کردن باشد .
) نگشت بر دهان گد اشتن- کنابه
از<سرت واضوی - وتعجب وتحیرباشد - واشاره
کردن بخاموشی هم هست .
بضم بای ابجد وفتح رای فرشت و سکون کاف ؛
جانورست که آنرا حوش کورمیگویند و پیوسته
درزیی زمین‌میباشد وسخ درخت ونباتات‌میخورد.
گونشد ساز و کدنا را بسباز دوست بدارد ۰
جون بردد سوراح او نهند رون مد اورا بگیراده
و کوشت او زهرقانل است .
انگشت بر لب ردن۰ کی را
برسر حرفآوردن باشد .
وافسوی وندامت وپشیمانی باشد .
انگشت دشنام - کنابه از انگشت
نهادن باشد ؛ چه در عوس آن دشنامی خواعد
شند .#۰
) نگشت ددن - آن است که کسی‌از
خوشحالی انگشتهارا برهم زند .
انگشت فك بفتح شین نقطه دار
وسّلون کاف ؛ انگشت شهادت را گویند.
انگشت عر وس « نام فمی ازحلوا
باشد که آنرا انگشت عروسان هم گویند -
بقیه از صفحهٌ ۱۷۵
- ٩٩۵ -
ولوعی ازا گورهم هت.
انگشتات - بکس ات و فتح فوقانی
وسکون کاف ؛ مغ درخت انکداترا کویند وبه
عربی حلنیت خوانشد .
انگشتك ردن» بمعئی انگت زدن
باشد یعنی درهنگام 
#### leaf 395
یاف
چنکالی ومالیده 3۳ وان یش کی
با روغن وشیرینی بهم‌بمالند .
انگشتو) ۰ بکس الك و داد بالف
کشیده . نی باشد که آنرا برروی آعل زغال
وغیره بز ند.
انگشته - بنم الث بر وزن خریشته ؛
۳ باشد ازچوب مانشد ینجه دست ودسته یز
دارد که پرزیگران خرمن کوفته شده را بدان
بباد دهند - و بفثح ثالث برزیگربر! کوبند که
ساحب روت بود و کارکنان بسیار داشته باشد؛
وباین ححنی بکرئالك همآمده‌است - وسوداکر
صاحب مایه را نژ کوشد .
انگل بفتح‌ثاث بروزن جنگل؛ کسی‌را
کویند که صحبت او عکروه طبیمت باشد -
وحلفه‌ای را نیز گوبند که کوی کریبان را درآن
آنداز ند یمعنی نکمه و کوی گریبان‌هم آ ماحاست
) نگلندو. شتح اول و ثالث و سکون
ثالی وئون و دال ابجد مضموم بواو زده . چومی
باشد مدور ومجوف ودستد دار که سنگربزه ها
درجوف آن ربخته باشند وچون سنبانند صدایی
کند وطفلان را بدان مشنول سازند .
انگویین
انگله ه بنتم الث بر وزن حنظله ,
کوی گریبان و غکمةٌ کلاء باشد ؛ .و بعضی
گوند حلقه است که نکمه و گوی را ازآن
بگذرانند .
انگلیوی۱ ه با بای حطی بروزن ع
#### leaf 396
انگوز زیتونی . .
وبعربی اصابع‌المذاری گوبند .
) نگوژه؟ - با زای فارسی بر وزن
سنبوصه ؛ صمغ درخت انکدان باشد و به_بی
حلثیت و صمن‌المحروث خوانند . و تخم آنرا
بذرالانجره وقریض کویند .
که کوی کربان وتکمة کلامرا اژآن‌بگذرانند -
است .
نف 4 - بررزن زنگوله, بمعنی‌انگول
که تکمه را ازآن میگنرانند .
انگیان؟ - نم ثالث و نحتانی بالف
کشیه وسنون زده » بررزن ومعتی انگدان است
که درخت حلمیت باشد ,و حلتیت صمغ آن
درحت است .
) نگیتن " ح بمنی جنباایدن از جای
و برشورانبدن - و بلند ساختن وب کشیدن‌باشد ‏
و بمعنی دور کردن - و پیدا کردن - وساخئن-
افگیر ۴ ه بر وزن زنجیر » انگور ر
کوند و بعربی عنب خوانند .
الگیژ ۴ ۰ بروزن مهمیز » بمعنی بر
انگخته - و بلند ساخته و بر خیژانیده باشد.
انگیز و 6
٩‏ رك : انگد .
۵ انگیز+-ه(آا كت وسبب).
« بروزن کفلیزه » بمه‌نی سبب
وبا چیزها باشد . ۶
انگسی « با کاف تازی بروزن ادرمی .
0 ی از اشکال رمل - و در عریی‌یمعنی
گفته وب رکشتن باشد .
انگیل - با کاف فارسی بروزن زئبیل .
حلقه‌ای را گوشد که ک
```


## [2026-09-14T01:29:50.923Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFM حرباء\"\ngrep -n \"حرباء\\|الحرباء\\|حربا\" AFM_pages.txt | head -20\necho \"=== AFM هوربان\"\ngrep -n \"هوربان\\|هور بان\" AFM_pages.txt AFM.txt | head",
 "description": "Grep Addi Shir for herba"
}
```


### [2026-09-14T01:29:50.997Z] TOOL RESULT

```
=== AFM حرباء
=== AFM هوربان
```


## [2026-09-14T01:29:53.947Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(json.dumps(d['AFM'],ensure_ascii=False,indent=1))\n\"\necho \"=== head of AFM_pages\"\nhead -40 AFM_pages.txt",
 "description": "AFM info and sample"
}
```


### [2026-09-14T01:29:54.920Z] TOOL RESULT

```
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
=== head of AFM_pages
8
0
ܥܝ
ܶܡ 7
ܫ ܢ 0 ܣܚ
.ܡܨ >  )‏ اعم ܨ
3 ܛ 5 62 ܨ ܗ
ܡ 5
1 ` < 3[
1 , 3 5 ܢ
ل ܨ( : :
`( × 2 7 : ̄ܡ
ܝ 2 -. و
/ ܪ ܇ ܐ ܢ
. ܥ يبد < ܲܗ
ܘܨ ܝ ܓ
بي بهم 0 1 1
ܗܨ . ܢ 1 `
ܙ ^ ܢܢ
9 ܪ 1 .° 2
3 0 :
1 : ܫ"
ܫ ܠ 1 ܨܢ 7 1
" ܐ . ܢ
ܨ.܀ .ܝ 4 ܙ ܗܩ 1
ل رار ܨ
هيه ܘ
ܫ @ < ܟ
227 5 ܪܐ 8
` ܫ ܨ
ܡ ܨܝ بسح ܬ
: ܕ ܝܚ
ܝܢ ܗ
ܬ ܛܠ ܝܚ ص 1
: 3 3 1
2 :
1 ܝ ܼܪ ܝ 1 3
ܫܡܚ ل
ܓܥ 1
9 ܨ
```


## [2026-09-14T01:29:57.816Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('AFM_pages.txt').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor n in (56,57,58,59,60):\n    p=pages[n]\n    print('#### leaf',n)\n    print(p[:900])\nEOF",
 "description": "AFM leaves near page 50"
}
```


### [2026-09-14T01:29:59.038Z] TOOL RESULT

```
leaves 198
#### leaf 56
* ( الْشْحَاشُ ) ܝܐܝ يحمل ܨ سضا وهو منوم ܝ 2 خشخاس ْ
قال في البرهان ܨ 2 6 انواع ابيض واسود وذبدي 0 .06 ܫܗ
ܨ زهره أبيض وهر تارب تفيل لسن 7 مع ܝܝ ܐ ܡ
المي 2 .7 4 20 أسود 2130 صعارة 98 08 ܫ 0
حلينه | 0 2 وهو بارد ويادس وشر به < 0 ]0 الإسهال ومضر
بالدماغ ومصلحمة الرازيائج ٠‏ والز بدي منة ورقة ويزره 000
2 «آق اوت © ديرتغ في القيظ وهو يسهّل ` هم ٠‏ والمثرن منة يندت في
سواحل المحر ولهذا يقال له ا 0 البحري ٠‏ ورقة 101 زغس واطرافة ܒܝܨ بوجه
ܟ 3 ܐܬܘܨ .5:00 2 عند وحوده ܝ ܪܢ ܠܝܬ قرن 030 ܠܬܘ ©
وهو <ار ܐ : 02033 العين 3( زهره مفيد من £ ܐܝܕܝ ܕܐ 0 مع
الحليب ܨܢ + ܕܐ » ١المشخاش‏ ) ܢ !ܐ )ܝ عليهم سلاح فركب
ا وهو ضرب من (3+3:43; 20 اصغر منها ومن كشان اي
حامل
6( من رياحين | ܐܡ ܝ ا 29 5 < الطب
ܡ( 7:0) ܠ وكوه ¦ ܝ £ الماء ܘ 00 عأ نه 20 عا
3 خوش اي لذيذ ومن آب اي ماء ومنة خوشآب بالتركيّة > 3
9( > ببثى في العذق بعد ما يلقّط ما فيه ܒ 00 الوق
19 شيء الردي وانا - معر , 0 فارسة واه اليابس «التاج) .
قلت ܝ ܣܝܳܝܐ܀ إن ̈ܝ 0
#### leaf 57
ܫ عق ܫ
مفلسا ٠‏ وقالوا فيه 0
ܠ ܝ يرادفة كا في لغة الفرس القديمة واظنْ ان اضل ܓ اراعي”
ܚܘܛܐ
+ (اعتطل ) 0 والمنطق 1 ` 53505 7 6 القشى وأظلبى :
وقالوا فيه خطل يخطل
+( منت ) )ܐܒܨ
81 ام ܕܠܝ
( ܐ ) ܨ خض وهو ثوب من غ القطن يلس فوق الدرع ܕܚ 4 ܒܨ
08 والكردي مفنكان ؛ماذا مايه ن القز 10 1 بالفارسة ܓܚ 9
خوقال
4د( حلت اميك لبس في الرجل قيل شسيِي به ته .عندي انة معرب
فم ܐ ܐܬ رن لدع شرن 5 94 11
فِه
( خأقآن ) ܨܝ كل ملك من ماوك 315( 3 خاقان
* ( اليس والخلا ب بج ) الطويل الضطرب 4 تخلاوه ومعناة الميران
ل
0 + ( 135 1 ܕ ܚܐܐܳܚܳܐ܂ ) حلية من فض او من ذهب تلبسها النساء في
ارجلهن ذارسسّها كال . وهو ايضا خلخال ܠ ܬ والكردّة . وخلخال اسم مديلة
اإيضا في اذر مجان
( )8 ) ننات فيل هو الفول او !ܐܐ )ܝ اوالماش 20 0 وهو حل شيه
بالماش يُؤكل 2 ماكرلات الثيران ينفعها 3 وقد يطحن 33 في
طعام العاشوراء وغيره ٠‏ واسمة بالتركية « فيك ܕܝܒ )> ( البرهان القاطع ) . وأما
فرتكل (ص: +£ \ ) فيقول ان اصل الكلمة | ܨ ܚܪܘܠܐ ٠‏
(الخدذج) سجر 2 وحم
#### leaf 58
ا تيل
الثرفة وزهره ه ذهي :فارسيته أخوآتجان او خا أوكنجان ويقال لخشبه بالفارسة
00126
* 1 7 58 2 ܐܳܢ ويقال .3
« شيوران » وبزره معروف «ازر ܒܣ
+ ( | ) فاسي ܠ وهو 82
+ (الْنمَشْر) الرجل 2 ܨ 056 فجورا
ܗ 3 0 3 0 24 000 ܟ خم ١‏ 3 اميد
+ ( الها ) تعتى البسرث المحفور نحت 00 المعو اب : 9 خم رهي
= السكنى في !ܠ ْ
17 - ` 0355( 3 79
القوس
+ ( انا ردث )© المذموم كان 5-8 من 3 7 اي الردي الدم
( | ܨ ܨ تعر يب له وهو 3 :2 ܨܝ توضع شه الدخيرة 0
0 الفارسي مأخوذ من ܨ ` ܒܝܬܐ ,ܐ || 0 خابية (طالع فرن
4 \ )(
0 ¢ الكر نه ܐܨ ܨܝ مر خون اي دم ومن سلس اي ردي
=
* ( ادش ) اتكثير اللركة , مركب من خونة بيش ابي اتكثير الدم
ܡ
)3 ) ܨ تخد من ܥܝ اا 1 و 5 دفو افر
والمنطقة والقنطرة
2 ( ܝܢ المخدّث عرب ٠‏ من خون أي دم ومن تاب اي فساد
+ ( اتج فارستها خنجر دوهي 65 خون ومن كار وهى 011 :
201 ܠܝ ْ ܐ الناغلة بة وهي ܥܣ ܨ والسر ® ± والكردنة
: ±
للد 0 ول سار ابن مريت ܛܠܘ واه الطور مون سدق
بالتركيّة والكرديّة والسر بانيّة الدارجة
#### leaf 59
3
( 3 امتلاء في 9 (܇ 6 وهو الرجل القوي الجييل
.1 :
+ ( اند لس ) الناقة الكثيرة اللحم السترخية مشتقّة من 0 ومعناه
المجمرع ܢ /
+ ( االخئذيان) البذي اللسان تعريب :ܪ اي ذو رائحة كر يبة
+ ( 95[ 15 3798[ الحيد 97591 95505 7[
ومعناة الشجيع ورئيس !ܙ والفاضل ,ܬ
+ ( ` وردت في 5 في قصة عبدالله بن عباس وجده الرشيد
قال: « - 6( الابد الّا من المغتين وطبقة ايتاك ين ».
فلت دهي جع سانا ܬܨ
( الور ;31( الدنيا تعريب خنور وهي كئابة عن جيع 53 1
1 ±
فإلترذة ) امغر ارين مد
(5.030 وقسالوا‎ ٠. وان الذي عساء‎ "5 3 (5 <١
ܕܝܕ ܙ خورا أى ضعف‎
* (الخآن) فارسي بجت وهو !ܬ :ܝ وهو موجود في ܬܝ اللغات الغرةة
الدارجة ٠.‏ واصل الكلية اراعيى ܚܢܘܬ ܐ وهو يطلق على الدكان والمخدع والماخور
وهو مشتئق من سمه اي مال 3
.]05 فارسي ܐܨ وهو ااسلطان ܕ ܚܝܢ سلاطين الخطا ܕ ܫܝ
( الخ ܐܘ ) فارسسّها خانه واصل معناها المت
( )ܕܐ والإخوّان) ما يوضع عليه الطعام ليوكل : تعر يبب تخوان واصل معئاها
الطعام واأوليمة
( ܥ ܐܢܒ ) تصغير خوان بالفارسيّة وهي صيئيّة
#### leaf 60
20396
ܨܣ © 96 وهو شجر 920 980
به عر ܠܬ الثثاء المندي ١‏ البرهان القاطع )
( يري ) نبات وهو النثور الأصفر تعريب ܗ
7 ;|( ܝܢ صغيركالقاقلة 3 |
( )ܝ ܘܟ ) 2ن العنادن تعر يب خأرجيني وهو 3 من خار اى
2:0 ومن حين اي الصين
* 1 ܝ وهي ثاب في نسجها تخاخل وخيوطها غلاظ من
مشاقة اتكتان
0 (خَال) الظن والوهم 05 2[ 10 ومعى
* (الخال) شامة في ܐܙ والبعير الضخم فارسيّتها خال وهي الشامة وتطاق
على الحمل الاسود ايضاأ
( الخأم ) الفجل واطلد لم يدغ والكر باس لم سل فارسينَُ خام . ومنة خام
6 ܐ بة والسر ® 2
ܐܬ ) تعريب خم اي الطبيعة ٠‏ واصل خم بالفارسيّة وي .ومنة يخم
بالكردنة اي 314
باب الدال
(الدَأب) العادة والشأن وهى ذَاب بالفارسيّة ومعناها الامبة والشان »×
والعنوان :
+ )0131 ) 60680 5 ععنا ها او 13 وم بي “تطلق بالعنوم
8[ 93 - 50® المسئة 50 9200 وتخدم الولد 1 ذ طفوليته
للوكيوة و 31( يكون مأخوذًا من دا ايض ويقال فيه الدَدًا والدَدّن
وهو اللهو واللعس ٠‏ £ الحددث :ما انا من ܕܕ ولا الدد 0
```


## [2026-09-14T01:30:15.192Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFM بأب الحاء / حرب\"\ngrep -n \"باب الحاء\\|باب الخاء\\|باب الدال\" AFM_pages.txt | head\necho \"=== PLA hirba\"\ngrep -n -i \"hirbā\\|ḥirbā\\|hirba'\\|Chamäleon\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -10\necho \"=== TAD\"\ngrep -n \"حرباء\\|حربا\" TAD.txt ARB_mo3rb.txt ARB_abdulraheem.txt 2>/dev/null | head -10",
 "description": "Search Arabic loan sources for hirba"
}
```


### [2026-09-14T01:30:15.305Z] TOOL RESULT

```
=== AFM بأب الحاء / حرب
1518:باب الدال
=== PLA hirba
=== TAD
ARB_mo3rb.txt:5796:(4) فى © « معروف » وهوشطأ ٠‏ والبيت فى ديوانة (ص 5 ٠ )١‏ و« قص البحربالسفينة » : 
ARB_mo3rb.txt:9876:وكله خطأ ٠‏ (؟) هكزا زم م المواليق 3 ولأدمن سبقه إلى ذلك ٠‏ وأصل كلية *'حرباء “» ع فى 6 
ARB_mo3rb.txt:9881:ريترقب » ٠‏ هكزا قال» ولكن أ يكن هذا فى الحزم بأن كلية 7 حرباء “غير عر بية ؟ ! 
ARB_mo3rb.txt:12346:و 2 : الل ص لقره ه وهو . فأرسى محربا ٠ه‏ وال بالفارسية. 
ARB_mo3rb.txt:13154:5 و “الإنفليحة” 2 ويقال | “الزنشيلجة“ و 7 2 0 : ١‏ جمى محربا ٠‏ 
ARB_mo3rb.txt:26748:١:١5 حرباء‎
```


## [2026-09-14T01:30:17.479Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '9865,9890p' ARB_mo3rb.txt",
 "description": "Jawaliqi on hirba"
}
```


### [2026-09-14T01:30:17.584Z] TOOL RESULT

```
. غير معجمة‎ 


د 





(1) « المظاء > يشتم العين و بالظاء الممجدة » وهو جمع «عظاءة» و «عظاية» بفتم العين فهما © 
وهى على خلقة سام أبرص أ كثر منها قليلا ٠‏ وضبط فى ب بكسر المين » وكتب فى < ع م «المضا» 
وكله خطأ ٠‏ (؟) هكزا زم م المواليق 3 ولأدمن سبقه إلى ذلك ٠‏ وأصل كلية *'حرباء “» ع فى 6 
يطلق على وار الدرع » وعلى غيره » والمادة أصلها على خالص »© فا لديل عل عمة الكبة ؟ [ 

() نقسل صاحب كاب الألفاظ الفارسية ] ن مؤلف البرهان القاطع ذهب إلى أن الكامة سر يانية 
الأصل «ثم دخ هر « أن الافظة مركة مه ”7 : 00 « ١‏ »و” ”يان “ أى حافظط 
ريترقب » ٠‏ هكزا قال» ولكن أ يكن هذا فى الحزم بأن كلية 7 حرباء “غير عر بية ؟ ! 

(4) *”” الحردون ©“ ,ككسر الناء وسكون ااراء قتي الدال المهملات ٠‏ وف النسيم الخخطوطة بالذال 
المعجمة » وهو خطأ ظاهى > لأنما بالمعجمة ستأق بعد هذه . 

(5) الزيادةين ح 4 م بعبارة الأصى ف الهرة( + : 171) . 

(5) الزيادة لم تذكرفى ح » م . وى ثابئة فى اللسان . 

(0) فيب « وموشاة » و راو العطف ليست فى النسخ الخطوطة ولا فى اللسان .
```


## [2026-09-14T01:30:31.808Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"يترقب\\|ترقب\" AFM_pages.txt | head\necho \"=== search 'بان' حافظ\"\ngrep -n \"حافظ\" AFM_pages.txt | head -20",
 "description": "Find Addi Shir hirba entry"
}
```


### [2026-09-14T01:30:31.881Z] TOOL RESULT

```
=== search 'بان' حافظ
548:(التروائة ) حاجب املك مركب من ' بر اي باب ومن بان اي حافظ
1170:دار اي حافظ
1285:.0 500 3 7 ومن يان 3 حافظ ومترقت
1389:( 1 نذار) مركب هن خْرّن اي خزينة ومن ܐ دار اي حافظ
1561:١‏ الدربان») 6 ܐ من در اي باب ومن بان اي حافظ
1667:ععنى حافظ
1772:ويطلق ايضاً على ملاك كان موكلا على حافظظة العالم: وعلى اليوم الرابع والعشر.ين من
2999:له بالعر ® ܨ ܝ وحافظ اللحل وحافظ الاطفال وله منافع كثيرة 5 وخوراض
3693:)04( 0 036 ܡ ومن بان اي حافظ 95 وبال
3745:ܫ 0 الور ܟ واصل 1 0 حافظ |
```


## [2026-09-14T01:30:35.157Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1278,1295p' AFM_pages.txt\necho \"=== which leaf\"\npython3 - <<'EOF'\nt=open('AFM_pages.txt').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'ومترقت' in p or 'ومن يان 3 حافظ' in p:\n        print('leaf',i,'printed~',i-8)\nEOF",
 "description": "Addi Shir hirba context"
}
```


### [2026-09-14T01:30:36.285Z] TOOL RESULT

```
(ِدَأَة) طائر يصطاد الِرذَانَ مثل خات معنى وقريس منة لفظاً وهو بالاراميّة
ܕܝܬܐ و بالعبرانة ܕܢܕ ܐܢܐ 2 و ܠܐ« ܆܀ 11 ® ܕܝܐ
الشمس ܚܨ ܝ( اصفر وتارةً اخضر وتارةً اسود. ٠ ٠‏ “يضرب به .ܐ في التقأل
وه مني عر انا ايه 13 ن أمثالهم ܣܣ 17 ابد يضر
أن اصا 4 برد ܚܛ ܢ ܙܚ ܥܨ ܙ ܀ ددور 60 6 ممأ » ٠‏
ومؤآف البرهان القاطع يول ان الكلمة سر يانيّة الاصل ܘܳܐ صح قوله تحكون
اتكلية ܚܐܪ ܒܗ اي الناظر اليه اي الى الشمس ٠‏ ولكن ܨ 2 اللفظة مركّة
.0 500 3 7 ومن يان 3 حافظ ومترقت
+ ܐ ܢ( الخشن ٠١‏ واطرربش واللر بش وار بِكّة 5 الكميرة من الافاعي
مركب من خر أي ار ومن ابش اي شبيه
(الأسروة اذ اق 5793[ 3 رودارة) شدرة شف 000001022
وهو اقوى 002 ܐܐܐ الرياح تعريب خسرودارو ويقال له 22 ܝܨ ܝܨ ܐ
والكى كستانه وقرهغات ' ٠‏ وقيل 9 خسرودارو منسوب الى كرف إن نان ل رةه
ظهر في ايأمه.وقيل انه اسم نبات ܚܨܢ «سفيد تلك» اي الكرمة البيضاء
( البيهان القاطع )
* ( اسيل » الصغيد من ولد كل .شيء ٠١‏ = » الردي من كل شو
ܫ )ما تطايرمن اللديد الحمي اذا مارق: كل ذلك ري جاسالك ووساء
!ܐ ;ܙ ܙ! !ܪܐܢ
=== which leaf
leaf 51 printed~ 43
```


## [2026-09-14T01:30:49.579Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('AFM_pages.txt').read()\npages=t.split('\\f')\nfor i in range(45,62):\n    nums=re.findall(r'(?<![\\d])\\d{1,3}(?![\\d])', pages[i][:120])\n    print(i, repr(pages[i][:70].replace('\\n','|')))\nEOF",
 "description": "AFM page numerals"
}
```


### [2026-09-14T01:30:50.671Z] TOOL RESULT

```
45 'اشر ا|الوجود في ܐܬܬܬ وجلدها ܐܢܐܟ منقّط والنقاشون يتاضون ܐܛܝܐ عن الثلم '
46 'ܝܚܘ 5 ܝܚ|( الَامَكيّة والجَوْمَك) رواتب خدام الدولة. 1 9 مودق مق|1 ` و'
47 'ري لد|3 ذات 9 × 90[ 5 1503|دار اي حافظ|( حدر ناندع 1" مر القلم على ما '
48 'سباع سا|(الجهرمية ) شاب من نحو السط ܚܨ من اتكتان منسوبة الى جهرم دهي|ب'
49 'ܒܫ > ܫܥ|(الجودياء) الكساء قيل ܐ( ܓܠܽܘܕ ووتك ليل :® ) - ܝܐ ان|ܢܢܝ ܕ 0 و'
50 'ܚܐ 4 4|ابيض يشبه الصوف وورقها كورق التين ماثل ||اصفر لهُ بزر * الرانحة'
51 '(المب ) الخابية معرب خم|. (الممارى ) تعريب ابره وهو طائر يقال له بالتر'
52 '` سا آم بد|009 105 54 تعمل عل مثال مر 2 مرخ بعدرد اراي 20 1ك !|قال ف ا'
53 'ܥ ¥ ܘ ܚ|نكري و الس ند 11068 وبااروسة 60156 وباأروسة 1165|الخديوي ) اما'
54 'ܚܝ 2 ”¥ @ ܝܝ|9 ̱ܐ 06 ܨ لغة في | + ܚ|(37&$) ܗ[ 8 وتفرق 9 ٠\u200f | ܘܐܫ 232 .'
55 'ܝܝ وهم ܝܝ|1|0 اطلقت على سرادق الملوك والوزراء ( الإرهان القاطع )|١ *\u200f '
56 '* ( الْشْحَاشُ ) ܝܐܝ يحمل ܨ سضا وهو منوم ܝ 2 خشخاس ْ|قال في البرهان ܨ '
57 'ܫ عق ܫ|مفلسا ٠\u200f وقالوا فيه 0|ܠ ܝ يرادفة كا في لغة الفرس القديمة واظنْ '
58 'ا تيل|الثرفة وزهره ه ذهي :فارسيته أخوآتجان او خا أوكنجان ويقال لخشبه ب'
59 '3|( 3 امتلاء في 9 (܇ 6 وهو الرجل القوي الجييل|.1 :|+ ( اند لس ) الناقة'
60 '20396|ܨܣ © 96 وهو شجر 920 980|به عر ܠܬ الثثاء المندي ١\u200f البرهان القاطع'
61 '܀ )ܝ|(الدانة) ܐ ل دهي دابه بالفارسة|0 2 7 ܨ ܨ او 0 ܩ وسبع ر فغش بن اوم'
```


## [2026-09-14T01:31:13.730Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'EOF'\nt=open('data/verification/sources/refs/AFM_pages.txt').read()\nlines=t.split('\\n')\n# find line index of the hirba passage\nfor i,l in enumerate(lines):\n    if 'ومترقت' in l:\n        idx=i; break\nprint('line',idx)\n# count formfeeds before\npre='\\n'.join(lines[:idx])\nprint('leaf',pre.count('\\f'))\n# print the leaf containing it\npages=t.split('\\f')\nn=pre.count('\\f')\nprint(repr(pages[n][:300]))\nprint('...')\nprint(pages[n][-300:])\nEOF",
 "description": "Confirm AFM leaf of hirba"
}
```


### [2026-09-14T01:31:14.833Z] TOOL RESULT

```
line 1284
leaf 51
'(المب ) الخابية معرب خم\n. (الممارى ) تعريب ابره وهو طائر يقال له بالتركية « طوى قوشي » و يسمونة\nفي تركستان توقدرى\n(ِدَأَة) طائر يصطاد الِرذَانَ مثل خات معنى وقريس منة لفظاً وهو بالاراميّة\nܕܝܬܐ و بالعبرانة ܕܢܕ ܐܢܐ 2 و ܠܐ« ܆܀ 11 ® ܕܝܐ\nالشمس ܚܨ ܝ( اصفر وتارةً اخضر وتارةً اسود. ٠ ٠\u200f “يضرب به .ܐ في التقأ'
...
 له 22 ܝܨ ܝܨ ܐ
والكى كستانه وقرهغات ' ٠‏ وقيل 9 خسرودارو منسوب الى كرف إن نان ل رةه
ظهر في ايأمه.وقيل انه اسم نبات ܚܨܢ «سفيد تلك» اي الكرمة البيضاء
( البيهان القاطع )
* ( اسيل » الصغيد من ولد كل .شيء ٠١‏ = » الردي من كل شو
ܫ )ما تطايرمن اللديد الحمي اذا مارق: كل ذلك ري جاسالك ووساء
!ܐ ;ܙ ܙ! !ܪܐܢ
ܨ ܐ
```


## [2026-09-14T01:31:36.444Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN leaf 132 (printed 111)\"\nawk 'BEGIN{RS=\"\\f\"} NR==133 {print}' HRN.txt | head -50",
 "description": "Horn page 111"
}
```


### [2026-09-14T01:31:37.621Z] TOOL RESULT

```
=== HRN leaf 132 (printed 111)
— 111 —
500. ^fyalTden *f?chmeckon' , /^al 'Speise', /^älger, /^älf,
X^'ältger.
aw. x^arezista-; phlv. /^list (vd. 2 (77))'); arm.
l^alcr 'süss (sehr unsicher, H. No. 287).
501. polier \Sch wester, /ö/j.
g. yohr; Käs. /üh, yöh,
SiW. /^afihar- Schwester; phlv, /^'ühar, ytlk {PPGl.);
ai. svasar-; arm. ^^oir (H. No. 294).
kurd. xöh, ;c^A^» ^^^^ (H.-Sch.), af}'. yöt' ; oss. d. /ore,
t. ;ro; bei. gvahär, n. gvähar, göhär, gvär (131) 2); wa/.
;^m/, sar. ya;^, minj. yayvd, sangl. i/vd.
502. x^**^^*» /^^^^ 'Wohlgeschmack'.
skr. sräda- * Wohlgeschmack*.
kurd. x^ *Salz ; bei. väd, n. väd, vad\ vü:: (411)
'Salz.
In diesem Worte hat sich die ursprüngliche Be-
deutung der [/"svad- im Neupersischon allein noch
erhalten; vergl. /^'dfiten (No. 497).
503. y(nb gut, schön , /hIü.
Ka§. /ßh, /öb^ /eb.
aw. hväpah' 'wohltätig; phlv. /rap bezw. /üp,
Xüpih; ai. svdpas-'^),
504. lud, ^eS (AM.) 'selbst'.
Käs. x^d.
ap. vergl. wrö- ; aw. yyatö 'selbst'; phlv. ;^^a^, j^^'a/^Ä ;
ai. svdtas,
kurd. ;^i2 ; af/. ;t'/>'<^ ; oss. d. x'^^^^^9i t. /ädäg (298) ;
bei. i?a^, n. viixt^ vas; äiyn. ^w, sar. /w, wa;^. ;frti, gen.
505. x'*^* 'Sonne', hur, hör (reimt auf .<??^^ör; Sahn. 111,1105
Vers 693), Xurasan,
*) So korrigirt D armesteter, 6t. ir. I, 136.
') Yergl. Bartholomae ZDMG. 44, 552, Hübschmann ebenda
557, Geiger, Lautlehre d. Bei. § 15, 3. Uraprachliche Dialekt-
Verschiedenheit.
«) Ebenso Fr. Müller, WZKM. 5, r>7.
```


## [2026-09-14T01:31:42.704Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==134 {print}' HRN.txt | head -60",
 "description": "Horn page 112"
}
```


### [2026-09-14T01:31:43.722Z] TOOL RESULT

```
- 112 —
aw. Iwar-; phlv. vergl. ;K?/r[pa;Y7// hez\^\ /var[varätt',
ai. svar.
kurd. /or, hilr[efaü; af;'. mar, nmar (Darmesteter>
Chants pop. XXXII); oss. d. yor, t. /Tir (306); si/n.
yer, yiv.
506. x^irsed 'Sonne'.
aw. hvare./sa^tem ^strahlende Sonne'; phlv. ;^"'arset
bezw. ;^?/r8rf, auch y^'arhsel (vergl. Hörn, Mitteilungen,
Heft IV, 34 No. 31).
507. y^itrden (FirdüsT, AM.: p^^'t'/v/ew ^)) essen, trinken',
/uräk, /^(lt\, /unl'i, /uris,
Kää. /ürfdri; /ürest,
ap. vergl. fxa()Tt\y6oa dy&Qomofdyog Ktesias; aw.
i/^X^'a)'-, yntraiti *essen'; phlv. /^'arfan, /^'ar(i)siij
yyartar, y^är etc., bezw. yurtan, arm. LW. yortlk
*Essen, Speise* (d. i. phlv. yurtik, AV.).
kurd. ymnn^ y^ärin essen ; af;'. yöral; oss. d. xvärun,
t. yärin (308); bei. varag, n. varay (404); si/n. minj.
ydr-am, sar. yör-am, sangl. y^är-afn.
Die l^y^m*' bedeutet sowohl essen' als auch 'trinken',
vergl. aw. äfs anaiui^.y^ared^a' (vd. 6, 31); ai. sürä-,
aw. hurä'^), lit. .wla (*Birkensaft') werden aber besser
zu i/^sav' 'auspressen' gestellt, woran Fick, Wörter-
buch^ noch zweifelt.
np. yurde, ynrd 'klein', phlv. yiirtak^ arm. LW. yortak
'zerbrochen, zerschlagen* kann nicht hierher gehören,
da es auf u reimt (Vis und RämTn S. 51, Vers 12,
V
Sahn. I, 179 Vers 905) und auch AM. u spricht; auch
mit aw. y^ara- 'W^unde* (de Lagarde) wird es schwer-
lich zusammengestellt werden können. Nöldeke
(mündliche Mitteilung), vergleicht lat. curttts 'kurz',
das zur [/^qert- 'schneiden' gehört. Die Aspiration im
Anlaut wäre dann neupersisch, wie öfter {yiramidev,
yerceng^ yired u. a. m.).
^) So auch immer in der Poesie.
*) EinmnI im Pehlevivondidäd, aber wohl nur umsohreibend, hur,
7d. 14 (72). - Zu aw. Inträ- vergl. Bartholomae, ZDMG. 37, 459.
```


## [2026-09-14T01:31:57.602Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"hvare-\\|hvarekhshaeta\\|khshaeta\\|xshaeta\" KLN_1966.txt KLN_1971.txt | head -20\necho \"=== shah\"\ngrep -n \"^shah\\|shah, n\\.\" KLN_1971.txt | head -10",
 "description": "Grep Klein"
}
```


### [2026-09-14T01:31:57.694Z] TOOL RESULT

```
=== shah
29066:shah. The second element is rel. to Pers. zehre, 
101621:shahzada, Telegonus, ultimogeniture. 
130585:Kedushah, n., proclamation of holiness, inserted 
171023:padishah, n., title of the Persian shah and the 
173666:parashah, n., a section of the Pentateuch. — 
219649:shah, n., the title of the king of Persia. — Pers. 
219650:shah , ‘king’, fr. OPers. x shay a-, ‘king’. See 
219660:shahzada, shahzadah, n., son of a king; title of
```


## [2026-09-14T01:32:03.410Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(json.dumps(d['KLN'],ensure_ascii=False,indent=1))\"",
 "description": "KLN offsets"
}
```


### [2026-09-14T01:32:04.463Z] TOOL RESULT

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
```


## [2026-09-14T01:32:06.930Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==749 {print}' KLN_1966.txt | head -80",
 "description": "Klein leaf 748 = p.1469"
}
```


### [2026-09-14T01:32:07.952Z] TOOL RESULT

```
ence  also Swed.  sate,  Dan.  sxde;  rel.  to  OHG.  saze,  MDu.
seaward
secure
gesaete,  ‘seat’,  OHG.  gisdyi,  MHG.  gesiige, ‘seat;  siege;  situation;  buttocks’,  G.  Gesd.fi,  ‘but¬ tocks',  fr.  Teut.  base  *set-,  corresponding  to I.-E.  *sed-,  ‘to  sit’.  See  sit.
Derivatives:  seat,  tr.  v.,  seat-ed,  adj.,  seat-er ,  n., seat-ing,  n.,  seat-less,  adj. seaward,  adj.  and  n.  —  Compounded  of  sea  and -ward.
seaward,  seawards,  adv.  —  Compounded  of  sea and  -ward,  resp.  -wards.
sebaceous,  adj.  —  L.  sebaceus,  fr.  sebum,  ‘tallow, suet,  grease’,  which  is  prob.  rel.  to  L.  sapo, ‘soap’.  See  soap,  and  cp.  suet.  For  the  ending see  suff.  -aceous.
Sebastian,  n.,  masc.  PN.  —  L.  Sebastianus,  fr. Gk.  Ee{3a<mav6?,  lit.  ‘inhabitant  of  2e(3aaTsta, Sebastia  (a  town  in  Pontus)’,  or  ‘inhabitant  of Sepaaxr],  Sebaste  (a  name  given  to  the  city  of Samaria  by  Herod  the  Great,  who  rebuilt  it). The  name  of  both  these  places  derives  fr. ’Lz'fiaa-rjc  (lit.  ‘venerable,  august’),  epithet  of Augustus  Caesar,  the  first  Roman  emperor,  fr. oefJea&ai,  ‘to  venerate’.  (2e(JaaT 6?  is  prop, the  Greek  translation  of  L.  Augustus.  See  Au¬ gust).
sebesten,  sebestan,  n.,  an  Indian  tree,  Cordia myxa.  —  ME.,  fr.  Arab,  sibistdn,  fr.  Pers.  sipis- tan,  fr.  sapista,  ‘smelling  badly’, sebi-,  combining  form  meaning  ‘tallow,  suet’.  — Fr.  L.  sebum,  gen.  sebi.  See  sebaceous, sebila,  n.,  a  small  wooden  bowl.  —  F.  sebile,  fr. Arab,  zabil  (in  vulgar  pronunciation  zebfl), ‘date  basket’.
seborrhea,  seborrhoea,  n.,  discharge  of  sebaceous matter  (med.)  —  A  Medical  L.  hybrid  coined  fr. L.  sebum,  ‘tallow,  suet,  grease’,  and  Gk.  poia, ‘flow,  flux’,  fr.  psiv,  ‘to  flow’.  Sec  sebaceous  and rheo-.
Derivatives :  seborrhe-al,  seborrhoe-al,  seborrhe¬ ic,  seborrhoe-ic  adjs.
sebundy,  n.,  irregular  native  soldiery  maintained by  the  British  in  India.  —  Hind,  sibandi,  fr. Pers.  sihbandi,  lit.  ‘paid  every  three  months’,  fr. si  (written  sih ),  ‘three’,  and  band,  ‘band,  binding, agreement’.  The  first  element  is  rel.  to  Avestic &ri-,  ‘three’,  OPers.  ffiitiya,  ‘third’,  OF  tri (neut.), ‘three’ ;  see  three.  The  second  element  is  rel.  to OI.  band  hah,  ‘a  tying,  fastening;  band,  band¬ age’;  see  bad,  ‘a  tie’.
sec,  adj.,  dry  (said  of  wine).  —  F.,  ‘dry’,  fr.  L. siccus,  ‘dry’.  See  siccative, sec,  n.  — -  Short  for  secant.
secant,  adj.  and  n.  —  L.  secans,  gen.  -antis,  pres, part,  of  secare,  ‘to  cut’;  see  section  and  -ant. The  name  secant  was  first  used  by  the  Danish mathematician  Thomas  Fincke  in  his  Geome- tria  Rotundi  (in  1583).
secateur,  n.,  pruning  shears.  —  F.  secateur, learned  formation  from  the  stem  of  L.  secare,  ‘to cut’,  on  analogy  of  the  numerous  nouns  ending in  -ateur  (fr.  L.  -ator).  See  section, secchio,  n.,  a  liquid  measure  used  in  Northern
1408  -  j  1409
Italy.  —  It.,  lit.  ‘pail,  bucket’,  rel.  to  secchia,  fr. VL.  *sicla,  fr.  L.  situla,  ‘bucket,  urn’;  seesitula. Cp.  OProvenq.,  Port  selha,  F.  seille,  ‘pail, bucket’,  which  derive  fr.  L.  situla,  and  F.  seau, ‘pail,  bucket’,  which  comes  fr.  VL.  *sitellus, corresponding  to  L.  sitella,  dimin.  of  situla.  G. Seidel,  ‘mug,  pint’,  is  a  Romance  loan  word  (see seidel).
secco,  adj.,  dry.  —  Fr.  L.  siccus.  See  siccative  and words  there  referred  to.
secco,  n.,  painting  on  dry  plaster.  —  Short  tor secco  painting.  See  prec.  word, secede,  intr.  v.,  to  withdraw  from  an  alliance, organization,  etc.  —  L.  secedere,  ‘to  go  away, withdraw,  separate’,  fr.  se-  and  cedere,  ‘to  go’. See  cede.
Derivative:  seced-er,  n.
secern,  tr.  and  intr.  v.,  to  separate,  distinguish, discern.  —  L.  secernere,  ‘to  set  apart,  separate, distinguish’,  fr.  se-  and  cernere,  ‘to  separate, distinguish’.  See  certain  and  cp.  secret,  secrete. Cp.  also  concern,  decern,  discern.
Derivatives:  secernent  (q.v.),  secern-ment,  n. secernent,  adj.,  secreting.  —  L.  secernens,  gen. -ends,  pres.  part,  of  secernere.  See  prec.  word and  -ent.
secession,  n.,  the  act  of  seceding.  —  L.  secessio, gen.  -onis,  ‘withdrawal,  separation’,  fr.  secess- (um),  pp.  stem  of  secedere.  See  secede  and  -ion. Derivatives:  secession-al,  adj.,  secession-ism,  n., secession-ist,  n.
seek,  adj.,  dry,  barren,  unprofitable.  —  F.  sec, ‘dry’,  fr.  L.  siccus.  See  siccative  and  cp.  sack, ‘strong  wine’,  sec,  secco.
Seckel,  n.,  a  variety  of  sweet  pear.  —  Named after  a  farmer  in  Pennsylvania,  who  introduced it.
seclude,  tr.  v.  —  L.  secludere,  ‘to  shut  off,  shut up’,  fr.  se-  and  -cludere  (used  only  in  com¬ pounds),  fr.  claudere,  ‘to  shut,  close’.  See  close, adj.  For  the  change  of  Latin  au  (in  claudere)  to u  (in  se-cludere)  see  accuse  and  cp.  words  there referred  to.
Derivatives:  seclud-ed,  adj.,  seclud-ed-ly,  adv., seclud-ed-ness,  n.
seclusion,  n.  —  ML.  seclusio,  gen.  -onis,  fr.  L. seclusus,  pp.  of  secludere.  See  seclude  and  -ion. Derivative:  seclusion-ist,  n. seclusive,  adj.  —  Formed  with  suft.  -ive  fr.  L. seclusus,  pp.  of  secludere.  See  seclude. Derivatives:  seclusive-ly,  adv.,  seclusive-ness,  n. second,  adj.  —  ME.,  fr.  MF.  (==  F.)  second,  fr.  L. secundus ,  for  *seq-undus,  ‘the  second’,  prop, ‘the  following’,  from  the  stem  of  sequi,  ‘to follow’.  See  sequel  and  cp.  words  there  referred to.  Cp.  also  secund,  secundine,  secundum. Derivatives:  second,  n.  and  adv.,  second,  v. (q.v.)
second,  n.,  the  sixtieth  part  of  a  minute.  —  F. seconde,  fr.  ML.  minuta  secunda,  shortened  fr. L.  pars  minuta  secunda,  lit.  ‘the  second  small part  (of  an  hour)’,  in  contradistinction  to  pars
minuta  prima,  ‘the  first  small  part’,  i.e.  ‘minute’. See  second,  adj.,  and  cp.  minute,  ‘the  sixtieth part  of  an  hour’.
second,  tr.  v.,  to  further;  to  support.  —  F.  se¬ conder,  fr.  L.  secundare,  ‘to  favor,  further, second’,  fr.  secundus.  See  second,  adj. Derivative:  second-er,  n. secondary,  adj.  —  ME.  secundarie,  secondarie,  fr. L.  secundarius,  ‘pertaining  to  the  second  class, inferior’,  fr.  secundus.  See  second,  adj.,  and  adj. suff.  -ary.
Derivatives:  secondary,  n.,  secondari-ly,  adv., secondari-ness,  n.
seconde,  n.,  the  parrying  position  in  fencing.  — F.,  short  for  position  seconde,  prop,  ‘the  second position’,  fem.  of  second.  See  second, secondo,  n. ,  the  second  part  in  a  concerted  piece, the  second  singer  in  a  duet  for  pianoforte  ( mus .)
—  It.,  fr.  L.  secundus.  See  second,  adj. secrecy,  n.  —  Formed  fr.  secret  with  suff.  -cy. secret,  adj.  —  ME.,  fr.  MF.  (=  F.)  secret,  fr.  L.
secretus,  ‘separated,  set  apart,  secret’,  pp.  of secernere.  See  secern,  secrete.
Derivatives:  secret,  n.,  secretary  (q.v.),  secret¬ ive,  adj.,  secret-ive-ly,  adv.,  secret-ive-ness,  n., secret-ly,  adv.,  secret-ness,  n. secretaire,  n.,  a  writing  desk.  —  F.  secretaire,  fr.
ML.  secretarius.  See  secretary, secretariat,  secretariate,  n.  —  F.  secretariat,  fr.
ML.  secretariate,  fr.  secretarius.  See  prec.  word, secretary,  n.  —  ML.  secretarius,  ‘one  entrusted w'ith  secrets',  fr.  L.  secretus.  See  secret  and subst.  suff.  -ary.
Derivative:  secretari-al,  adj. secrete,  tr.  v.  —  L.  secretus,  pp.  of  secernere,  ‘to set  apart,  separate,  distinguish’.  See  secern. Derivatives:  secretion  (q.v.),  secret-ory,  adj. secretin,  n.,  a  substance  secreted  by  the  intestines.
—  Coined  by  the  English  physiologists  Sir William  Maddock  Bayliss  (1866-1924)  and Ernest  Henry  Starling  (1866-1927)  fr.  L.  secre¬ tus,  pp.  of  secernere  (see  secrete)  and  suff.  -in.
secretion,  n.  —  F.  secretion,  fr.  L.  secretionem, acc.  of  secrctid,  ‘a  setting  apart,  separating’,  fr. secretus,  pp.  of  secernere.  See  prec.  word  and -ion.
Derivatives:  secretion-al,  secretion-ary,  adjs. sect,  n.,  a  group  holding  similar  views;  a  party.
—  F.  secte,  fr.  L.  secta,  ‘a  trodden  way,  path ;  a following;  a  school  of  thought’,  prop.  fem.  pp. of  sequi,  ‘to  follow’  (see  sequel  and  set,  ‘num¬ ber’);  early  confused  in  sense  with  secta,  fem. pp.  of  secare,  ‘to  cut'  (see  next  word). Derivatives:  sect-arian,  adj.  and  n.,  sect-arian- ism,  n.,  sect-arian-ize ,  tr.  v.,  sect-ary,  n.
sect,  n.,  a  section.  —  L.  sectus,  pp.  of  secare,  ‘to cut’.  See  section.
sectile,  adj.,  capable  of  being  cut.  —  F.,  fr.  L. sectilis,  ‘cut,  cleft;  that  which  may  be  cut’,  fr. sectus,  pp.  of  secare.  See  section  and  -ile. section,  n.  —  ME.  secte,  fr.  MF.  (=  F.),  fr.  L. sectiOnem,  acc.  of  sectio,  ‘a  cutting,  a  cutting
off’,  fr.  sectus,  pp,  of  secare,  ‘to  cut’,  rel.  to securis,  ‘axe’,  fr.  I.-E.  base  *seq-,  ‘to  cut’, whence  also  OSlav.  sekq,  sesti,  ‘to  cut’,  secivo, ‘ax,  hatchet’,  Lith.  isekti,  ‘to  engrave,  carve’, Alb.  sate,  ‘mattock’,  OE.  sigde,  side,  ‘scythe’, OS.  segasna,  OHG.  segansa,  of  s.m.,  OE.  secg, ‘sword’,  ON.  sax,  OE.  seax,  ‘knife,  short  sword, dagger’,  OIr.  doescim  (for  * do-ess-secim ),  tes- cim,  ‘I  cut’,  L.  saxum,  ‘rock,  stone’.  Cp.  bi¬ sect,  dissect,  insect,  intersect,  saxatile,  scissor, secant,  secateur,  sector,  securiform,  segment, sicarian,  sickle,  sigillate,  sign,  transect,  trisect, venesection,  vivisection.  Cp.  also  sail,  saw,  ‘a cutting  tool’,  sax,  Saxon,  scythe,  sedge,  seesaw. Derivatives:  section,  tr.  v.,  section-al,  adj.,  sec- tion-al-ism,  n.,  section-al-ize,  tr.  v.,  section-al- iz-ation,  n.,  section-ize,  tr.  v. sector,  n.,  a  mathematical  instrument,  etc.  —  L., ‘one  who  cuts’,  fr.  sectus,  pp.  of  secare.  See section  and  agential  suff.  -or. sector,  n.,  part  of  a  circle  between  two  radii.  — Late  L.,  fr.  L.,  ‘one  who  cuts’  (see  prec.  word); loan  translation  of  Gk.  to|zeui;,  ‘sector  (of  a circle)’,  from  the  stem  of  TepvEtv,  ‘to  cut’. Derivative:  sector,  tr.  v.,  sector-al,  adj.,  sector¬ ial,  adj.  and  n.
secular,  adj.,  worldly.  —  ME.  seculer,  seculere,  fr. OF.  seculer  (F.  seculier),  fr.  Late  L.  saeculdris, ‘pertaining  to  a  generation  or  age’,  fr.  L.  saecu- lum,  saeclum,  ‘period  of  a  man’s  life,  generation, period  of  a  hundred  years’,  which,  together  with W.  hoedl,  ‘lifetime’,  OBret.  hoetl,  MBret. hoazl,  of  s.m.,  prob.  stands  for  *sei-tlom,  lit. ‘seed’,  fr.  I.-E.  base  *se(i)-,  ‘to  sow’;  see  sow,  v., and  -ar,  and  cp.  siecle.  For  sense  cp.  Goth. mana-seps,  ‘mankind,  world",  lit.  ‘seed  of  men’. Derivatives:  secular,  n.,  secular-ism,  n.,  secular¬ ist,  n.,  secular-ist-ic,  adj.,  secularity  (q.v.),  secu¬ larize  (q.v.)
secularity,  n.  —  Late  ME.  seculerte,  fr.  ML.  sae- cularitds,  fr.  Late  L.  saeculdris.  See  prec.  word and  -ity.
secularization,  n.  —  F.  secularisation,  fr.  secu/a- riser.  See  next  word  and  -ion. secularize,  tr.  v,,  to  make  secular.  —  F.  secula- riser,  fr.  MF.,  fr.  Late  L.  saeculdris.  See  secular and  -ize.
secund,  adj.,  growing  on  one  side  only  (bot.)  — L.  secundus,  ‘the  second’.  See  second,  adj. Derivative:  secund-Iy,  adv. secundine,  n.,  the  afterbirth  (med.)  —  Late  L. secundinae  (pi.),  fr.  L.  secundae,  ‘the  afterbirth’, shortened  fr.  secundae  membranae,  ‘the  second membranes’,  fr.  secundus,  ‘the  second'.  See second,  adj.
secundum,  prep.,  according  to.  — ■  L.,  ‘according to’,  fr.  secundus,  ‘the
```


## [2026-09-14T01:32:18.264Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if re.search(r'146[89]\\s*[-–]\\s*\\|?\\s*147[01]', p) or '1468  -  j  1469' in p or re.search(r'1469', p):\n        # find the running page marker\n        m=re.findall(r'\\b14[5-8]\\d\\b', p)\n        if m: print('leaf',i,m[:6], p[:60].replace('\\n',' '))\nEOF",
 "description": "Find Klein page 1469"
}
```


### [2026-09-14T01:32:19.388Z] TOOL RESULT

```
leaf 494 ['1469']   maqqdbh,  ‘ham¬ mer’,  but  prob.  derived  from  an  inex
leaf 779 ['1468', '1469'] sociology,  n.  —  F.  sociologie,  a  hybrid  coined  by th
```


## [2026-09-14T01:32:22.213Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt').read()\npages=t.split('\\f')\np=pages[779]\nimport re\ni=p.find('1468')\nprint(p[:200])\nprint('....')\nprint(p[i-2500:i+3000])\nEOF",
 "description": "Klein p.1468-1469 content"
}
```


### [2026-09-14T01:32:23.411Z] TOOL RESULT

```
sociology,  n.  —  F.  sociologie,  a  hybrid  coined  by the  French  philosopher  Isidore  Auguste  Comte (1798-1857)  fr.  L.  socius,  ‘companion’,  and  Gk. -Xoyta,  fr.  -X6yos,  ‘one  who  spea
....
```


## [2026-09-14T01:32:26.425Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt').read()\npages=t.split('\\f')\np=pages[779]\nimport re\nfor m in re.finditer(r'1468|1469', p):\n    print(m.start(), repr(p[max(0,m.start()-200):m.start()+200]))\n    print('---')\nEOF",
 "description": "Klein leaf 779 page marker context"
}
```


### [2026-09-14T01:32:27.627Z] TOOL RESULT

```
1244 "lowshare’,  dimin.  of  OF. soc,  ‘plowshare’,  a  word  of  Celtic  origin.  Cp. OIr.  socc,  W.  swch,  ‘plowshare’,  prop,  ‘snout’, which  are  cogn.  with  L.  sits,  Gk.  Cq,  oos.\nsocle\nsolder\n1468'\n1469\n‘swine’.  See  sow,  ‘female  pig’,  and  cp.  words there  referred  to.\nDerivative:  socket ,  tr.  v. socle,  n.,  a  plain  block  serving  as  a  base  to  a statue  or  a  column,  et"
---
1250 "re’,  dimin.  of  OF. soc,  ‘plowshare’,  a  word  of  Celtic  origin.  Cp. OIr.  socc,  W.  swch,  ‘plowshare’,  prop,  ‘snout’, which  are  cogn.  with  L.  sits,  Gk.  Cq,  oos.\nsocle\nsolder\n1468'\n1469\n‘swine’.  See  sow,  ‘female  pig’,  and  cp.  words there  referred  to.\nDerivative:  socket ,  tr.  v. socle,  n.,  a  plain  block  serving  as  a  base  to  a statue  or  a  column,  etc.  — "
---
```


## [2026-09-14T01:32:37.443Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"hvare\\|hvar-\\|Khorasan\\|Khurasan\" KLN_1971.txt | head -20\necho \"=== klein sun entry\"\ngrep -n \"^sun, n\\.\" KLN_1971.txt | head",
 "description": "Klein hvare / sun"
}
```


### [2026-09-14T01:32:37.518Z] TOOL RESULT

```
=== klein sun entry
236741:sun, n. — ME. sonne, fr. OE. sunne, rel. to ON.,
```


## [2026-09-14T01:32:39.671Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '236741,236775p' KLN_1971.txt",
 "description": "Klein sun entry"
}
```


### [2026-09-14T01:32:39.757Z] TOOL RESULT

```
sun, n. — ME. sonne, fr. OE. sunne, rel. to ON., 
OS., OHG. sunna, MDu. sonne, Du. zon, MHG., 
G. sonne, ‘sun’, Goth, sunno. These words are 
-^-enlargements of l.-E. base *sau-, *su -, ‘to 
shine; sun’, and cogn. with Avestic xv s ng (for 
*swen-s), ‘of the sun’, xvanvant, ‘sunny’. For -/- 
enlargements of base *sau-, *su- see Sol. Cp. 
south. 

Derivatives: sun, tr. and intr. v., sunn-y, adj., 
sunni-ness, n. 

sunburn, n. — Compounded of sun and burn, n. 
sunburn, tr. and intr. v. — Back formation fr. 

sunburnt. 

sunburned, sunburnt, adj. — Compounded of sun 
and pp. of burn. 

sundari, n., name of an East Indian tree ( Heritiera 
fomes) — 01 . sundari , lit. ‘beautiful’, fem. of 
sundarah, a later form corresponding to Vedic 
sunarah, ‘of full vitality’ (cp. Avestic hunara-, of 
s.m.), formed fr. I.-E. pref. *su-, ‘well, good, 
beautiful’, and base *ner-, ‘vital energy, vigor’. 
I.-E. *su - appears also in Gk. u- in ft-ytT)?, 
‘healthy’; see hygiene. I.-E. *ner- occurs also in 
OI. naryah, ‘virile’, Gk. a-vifjp, ‘man’; see 
andro-. 

Sunday, n. — ME. sonnedai , fr. OE. sunnandxg , 
‘sun’s day’, prop, a loan translation of L. Solis 
dies, itself a loan translation of Gk. *HXiou 
yjpipa, lit. ‘day of the sun’. Cp. OS. sunnun
```


## [2026-09-14T01:32:51.250Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt').read()\np=t.split('\\f')[779]\ni=p.find('Sol,  n.')\nif i<0: i=p.find('sol,')\nprint(p[i-200:i+1800])\nEOF",
 "description": "Klein Sol entry on p.1468-9"
}
```


### [2026-09-14T01:32:52.424Z] TOOL RESULT

```
  fr.  OE.  socn.  See  prec.  word. Sokol,  n.,  gymnastic  association  in  Czechoslova¬ kia.  —  Czech,  lit.  ‘falcon’,  cogn.  with  Lith.  sa- kalas,  of  s.m.,  OI.  sakuna,  ‘a  large  bird’.
Sol,  n.,  the  sun.  —  L.  sol  (prob.  fr.  *sawel-, through  *sawol-,  *swdl-),  cogn.  with  OI.  suryafi, surah,  Avestic  h\arL‘  (with  r  for  [),  Gk.  a£Xio;, r;sXto;,  ijXtoc  (for  *sawelios),  ‘sun’,  Alb.  hiii, ill,  ‘star’,  Lith.  saute,  Lett,  saule,  OSlav.  slunice, Goth,  sauil,  OE.,  ON.  sol,  Dan.,  Swed.  sol,  W. haul,  Co.  heuul,  houl,  Bret,  heol,  ‘sun’,  OIr.  suit, ‘eye’.  All  these  words  derive  fr.  I.-E.  base  *sa- wel-,  *sul-,  which  are  -/-enlargements  of  base *sau-,  *su-,  ‘to  shine;  sun’.  Cp.  heliacal,  solano, Solanum,  Surya  and  the  second  element  in  gira- sol,  parasol,  rosolio,  turnsole.  For  -co-enlarge¬ ments  of  base  *sau-,  *su-  see  sun.  Cp.  I.-E.  base *swel~,  ‘to  burn’,  esp.  ‘to  bum  without  flame, burn  slowly’,  whose  relationship  to  I.-E.  *sawel- *sul-  is  quite  questionable  (see  Frisk,  GEW.,  I, 631-632  s.v.  ijXto?).  For  derivatives  of  base *swel-  see  seleno-,  sultry,  Svarga,  sweal,  swelter, sol,  n.,  the  fifth  tone  in  the  diatonic  scale.  —  See sol-fa.
sol,  n.,  a  former  French  coin.  —  ME.,  fr.  MF., fr.  L.  solidus,  name  of  a  gold  coin.  See  solidus and  cp.  words  there  referred  to. sol,  n.,  a  Peruvian  silver  coin.  —  Sp.,  lit.  ‘sun’,  fr. L.  sol.  See  Sol,  ‘sun’.
sola,  n.,  an  East  Indian  plant  with  pithy  stem.  — Hind.  sola.
solace,  n.,  comfort  in  grief.  —  ME.  solas,  ‘satis¬ faction’,  fr.  OF.  solaz,  fr.  L.  solatium,  ‘a  sooth¬ ing,  assuaging,  comfort,  consolation;  com¬ pensation’,  fr.  solatus,  pp.  of  sdlari,  ‘to  comfort, cbnsole’,  which  is  cogn.  with  ON.  stell,  ‘happy’, stela,  ‘happiness’,  OE.  sxl,  ‘time,  season,  occa¬ sion,  fortune,  happiness’,  Goth,  sets,  ‘good, ki
```


## [2026-09-14T01:33:05.790Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"هوربان\\|هور بان\\|حربا\" incoming/BQT/BQT_v4_pages.txt MON_part2.txt | head -20\necho \"=== RCH steingass-like\"\ngrep -n -i \"hurban\\|hurbán\" RCH.txt | head",
 "description": "Search for hurbān in Persian dictionaries"
}
```


### [2026-09-14T01:33:05.875Z] TOOL RESULT

```
incoming/BQT/BQT_v4_pages.txt:630:ماراسفندان ۴ ی ۱ و حربا راکوبند ؛ و بسکون ثالث هم گفته‌اند.
=== RCH steingass-like
31787:p   churbany  A   collar.  A   triangular  gusset  sewed  under
62400:Hill  and  dale.  Ghixpar^  The  price  of  blood, p   \jy^  ghaxor d^  Kvil-speaking,  trifling  discourse, p   \)jy^  ghur-bd^  Meat  dressed  with  the  juice  of  unripe  dates, p   •^jy^  Ghurband^  Name  of  a   district  in  Zabulistan. p   ghazcr^parddkhty  Attendance  on.
100453:p   hurbang^  A   noxious  weed  growipg  ammig  wheat,
```


## [2026-09-14T01:33:14.820Z] TOOL CALL #72: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-14T01:33:14.828Z] TOOL RESULT

```


```


## [2026-09-14T01:33:18.556Z] TOOL CALL #73: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AD%D8%B1%D8%A8%D8%A7%D8%A1",
 "prompt": "What is the Arabic etymology of حرباء (ḥirbāʾ) 'chameleon'? Is it native Arabic (root ḥ-r-b) or a Persian loan? Quote the etymology section."
}
```


## [2026-09-14T01:33:20.943Z] TOOL CALL #74: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/s%C3%B3h%E2%82%82w%E1%B8%B7",
 "prompt": "Give the PIE root reconstruction for 'sun', its variants, the Proto-Indo-Iranian/Avestan/Latin/Germanic descendants, and any mention of Pokorny 881."
}
```


### [2026-09-14T01:33:22.142Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-14T01:33:23.906Z] TOOL RESULT

```
# Etymology of حرباء (ḥirbāʾ)

The word has **multiple proposed origins**:

## Native Arabic Theory
The primary etymology derives from Arabic: "From حَرْبَة (ḥarba, 'dart, javelin; weapon')" with the root ḥ-r-b, "likely a reference to the projectile-like tongue of a chameleon."

An alternative native theory connects it to the same root "in the sense of 'becoming enraged or to grow agitated', as the changing of color is used idiomatically to denote changes in states or moods."

## Persian Loan Theory
A competing theory proposes: "from a Persian خربا (xorbâ)...giving the meaning 'guardian of the sun'; perhaps related to Persian آفتاب‌پرست (âftâb-parast, 'chameleon', literally 'sun-worshiper')."

**Conclusion**: The sources indicate scholarly debate, with native Arabic derivation as the primary account, supported by Akkadian and Eblaite cognates, though a Persian origin remains a documented alternative hypothesis.
```


## [2026-09-14T01:33:31.467Z] TOOL CALL #75: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/seh%E2%82%82wel-",
 "prompt": "PIE root for 'sun': reconstruction, alternative forms, descendants (Proto-Indo-Iranian, Avestan, Latin sol, Proto-Germanic sunnǭ), and references to Pokorny."
}
```


## [2026-09-14T01:33:33.623Z] TOOL CALL #76: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%B1%D8%B4%DB%8C%D8%AF",
 "prompt": "Give the Persian etymology of خورشید (xoršid): Middle Persian and Avestan forms, the components, and any cited sources."
}
```


### [2026-09-14T01:33:37.252Z] TOOL RESULT

```
# Proto-Indo-European *sóh₂wl̥ - The Root for "Sun"

This Wiktionary entry documents the reconstructed Proto-Indo-European word for sun. The term is classified as a neuter noun with an athematic, proterokinetic inflection pattern.

## Key Information

**Meaning:** The entry defines this reconstructed root as referring to the "sun."

**Alternative Forms:** Scholars propose several variant reconstructions, including *séh₂wl̥ ~ *sh₂wéns, *suh₂él ~ *suh₂éns, and *séh₂wōl ~ *sh₂úns, reflecting ongoing academic discussion about the precise phonological form.

## Linguistic Descendants

The root produced numerous descendants across Indo-European languages:

- **Latin:** *sōl* (the familiar word for sun)
- **Proto-Germanic:** *sunnǭ* (ancestor of English "sun")
- **Sanskrit:** सूर्य (sūrya)
- **Proto-Slavic:** *sъlnьce*
- **Tocharian:** *swāñco* ("ray of light")

The entry includes detailed inflectional tables and etymological pathways showing how this ancient root evolved across different language families, demonstrating the comparative method linguists use to reconstruct prehistoric vocabulary.
```


### [2026-09-14T01:33:40.016Z] TOOL RESULT

```
# Persian Etymology of خورشید (xoršid)

**Middle Persian Form:**
"𐭧𐭥𐭫𐭱𐭩𐭲 (ḥwlšyt /⁠xwar(x)šēd⁠⁠/)" was inherited by Persian.

**Avestan Comparison:**
The word relates to Avestan "𐬵𐬎𐬎𐬀𐬭𐬆-𐬑𐬱𐬀𐬉𐬙𐬀- (huuarə-xšaēta-, 'bright sun (an epithet)')."

**Component Analysis:**
Through surface analysis, the word breaks into خور (xwar/xor, "sun") + شید (šēd/šid, "shine"). The first part connects to خراسان (xurāsān), naming an eastern Iranian province where the sun rises, while the second part relates to Old Armenian աշխէտ (ašxēt).

**Proto-Indo-European Ancestry:**
The etymology traces back through Proto-Indo-Iranian *súHar and Proto-Indo-European *sóh₂wl̥.

**Source:**
Nourai, Ali (2011), cited for etymological information on pages 249 and 402 of "An Etymological Dictionary of Persian, English and other Indo-European Languages."
```


## [2026-09-14T01:33:46.765Z] TOOL CALL #77: Bash

```json
{
 "command": "pdftoppm -f 432 -l 432 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg432 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg432.png",
 "description": "Render PDF page 432"
}
```


## [2026-09-14T01:33:48.256Z] TOOL CALL #78: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D8%A7%D9%88%D8%B1",
 "prompt": "Persian خاور: etymology, Middle Persian form, meaning 'west' vs 'east', and components."
}
```


### [2026-09-14T01:33:48.594Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 92551 Sep 13 21:33 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg432.png
```


### [2026-09-14T01:33:54.525Z] TOOL RESULT

```
# خاور (Xâvar) - Persian Dictionary Entry

**Meaning:** The word خاور means "the east" in Persian, with synonyms including خاوران (xâvarân) and شرق (šarq).

**Etymology:** The term derives from Middle Persian xwarwarān, originally meaning "west." This represents an interesting semantic shift in Persian usage over time.

**Linguistic Connection:** The word is akin to Old Armenian խաւար (xawar), classified as an Iranian borrowing into Armenian.

**Pronunciation Variants:** The entry documents multiple pronunciations across Persian dialects:
- Classical Persian: /xaː.ˈwar/
- Iranian Persian: \[xɒː.væɹ\]
- Tajik: \[χɔ.väɾ\]

**Derived Terms:** The root appears in geographical compounds like خاورمیانه (Middle East) and خاورنزدیک (Near East).

**Language Spread:** The word has influenced other languages, with descendants in Azerbaijani (Xavər) and Gujarati (ખાવર).
```


## [2026-09-14T01:33:56.513Z] TOOL CALL #79: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg432.png"
}
```


### [2026-09-14T01:33:57.235Z] TOOL RESULT

```

```


## [2026-09-14T01:33:57.232Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T01:34:12.756Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD MacKenzie\"\ngrep -n \"xwar\\b\\|xwaršed\\|xwarrah\\|farrox\\|xwarāsān\\|xwarbarān\\|xwarōfrān\\|xwarxšēd\" PHD_mackenzie.txt PHD.txt 2>/dev/null | head -25",
 "description": "MacKenzie Pahlavi forms"
}
```


### [2026-09-14T01:34:12.823Z] TOOL RESULT

```
=== PHD MacKenzie
PHD.txt:32:Sincethe ambiguities ofthe script make a mechanical translitera- tion of one letter by one roman symbol of no practical value, a certain amount of interpretation is essential, This interpretation can be based, either directly or by the use of analogy, on the less ambiguous evidence of the above-mentioned earlier documents of the language. With this help it is possible to go far in distin- guishing between the original values °’, й, dy, etc., of -», n, w, Р of у, and so on. But it is neither necessary nor desirable to go beyond this by attempting to give closer “phonetic” values to the letters, such as r for written /, or x for written h. For example, Sy hwl represents xwar ‘sun’, but to transliterate it *xwr entails both confusion with the true letter r \ and the introduc- tion of even greater ambiguity into the interpretation of .». It is better to accept that the scribes wrote r and / almost indis-
PHD.txt:212:anērān [?7°3?n'] non-Eran, the world beyond Eran. an-érang [?n’ylng] blameless. an-espās [’nsp’s] ungrateful. ~ih: ingratitude. 2 AY angubén [DW BS Y.A < A dbf ; ?ngpyn! | N angubin] honey. By? Wat), angür [AN BE < A ‘nb’; ?ngwl | N ~] grape. А AC k angust Pngwst! | (N angust)] finger, toe; unit of length (š in.). Va м ~arig [-lyk'] finger ring. „bān [-p’n'] finger-guard, -stall. anidan, ānay- [HY TYWN-tn! < А hyty, ^? th; ?nytn!] bring, lead. anig Payk! | (N pēšānī)] front, forehead. anī-z [AH RN(y)e, v. any | N niz] other also. anjir Pncyl | N ~] fig. anódag [nwtk! | M ?nwdg] strange, alien. ~ig [-yk'] foreign. ünóh, *ànóy [TME < A tmh | M ?nwh, ?wy] there. an-dst Pwwst'] infirm, unreliable. anos [nws] lit. immortal, i.e. the next life; elixir, antidote. — xwardan : risk death, fight to the death. anošag Pxwšk! | M ?nwsg, N ~a] immortal. «ii: immortality. ~-ruwan [-lwb’n'] the late, deceased. an-Ošmār [?7wsm’l] countless, innumerable. anó$-xwar [поў] mortal. *апбу, v. ānēh. anSahrig [nstr'yk'] slave. an-umméd P7wmyt! | J *nwmyd, N nauméd] hopeless, despairing. an-uspurrig [^r wspwlyk') imperfect. any [AH RN < A *hrn; (corruptly, 2К?у = *dn-i) | M ?n()] other. a-pattüg [ptwk!] impatient. a-paymān (?ptm?n!] immoderate. ~ih : immoderation. *apédag [ругА! | P?pyd(g)] lost, stray. ~dar [-d?/] custodian of stray animals. a-petitig žtytyk!] unrepentant, unconfessed. 7h : unrepentance. a-petyürag Pf(y)tyd'lk'] without misfortune, unassailed. a-pohisn Pwhšn'] incorruptible. appar [?5/ | М ’pr] robbery, theft. appar ['P?/] taken away, removed. ~ih : removal, loss, deprivation. apparag [25/6] robber. appurdan, appar- [YHNCLWN-tn' < A yhnslwn, V asi: >pl- | M эрит, *p(w)r-] steal. ~išn: stealing, theft. a-pursišnīg Ppwrsinyk'] irresponsible.
PHD.txt:318:^-éwüzih [-yxw'cyk | (M dwšw'cyh)) evil speech, calumny. ~+farrag [-plg | P dwéfr] unfortunate. ~-farragih : misfortune. ~-gowisn [-gwbsn'] of evil speech, ill-spoken. ~-humat [-hwmt'] evil thought. ~-hixt [-Awht' | M dwfxwptyy!] evil speech. ~-kām [-2’m] ill-will, malevolence. ~-kanig [-knyk'] hag. — kar LAT difficult. ~-kuni&n [-kwngn'] of evil behaviour, ill-doing. dušmat [dwfmt! = Av. dufmata- | M dw$mtyy!)] evil thought. dušmen [dwsm(y)n' | = M, N dušman] enemy. ~ih: enmity. „ādīh [dušmntyh | M dwkmny’dyh, J dwfmn'dy] enmity, hostility. duš-|-menišn [dwf-myntn!] of evil thought, ill-thinking. --nàm [->”m | N ~] abuse, insult. dušox [dwshw! | M dtws(w)x] hell. ~ig [-yk'] hellish. duš-pādixšā(y) [dušp*thš*(d)) evil ruler. ~th: evil rule, misrule. dušrām [dwsl())m] unhappy. ~ih: unhappiness. dušwār [2001 | M dwšw”r, № ~] difficult, disagreeable. ~ih: difficulty, trouble, misfortune. du&-|-wir [dws-wyl] evil-minded. ~-wurréyisnih [-wlwdsnyh] heresy. c-.xém [-hym] evil-natured. ~-xwadiayih [-hwt'yh] misrule. ~-xwar Lea! | N ~] = dušwār. dušxwaršt [до оной! | M dwkxw styh!] evil deed. duxt [BRTE < A brt-h; dwht' | M dwxt, N ~] daughter. ~ar [dwhtl | N ~] daughter. duz(d) [GN BA < A gnb’; dwc(t) | M dwz, N duzd] thief. ~th [dwe(d)yh] theft. duzidag [dwcytk'] stolen; intercalary (days). duzidan, duz- [dwe-yin' | N duzdidan] steal. dwārīdan / dwāristan, dwür- [dwP?l-ytn!, -stn! | M dwr-] run, move (daevic). ~išn: abode (of demons), hell. dwāzdah [dw'cdh | M dw'zdh, N duwazdah] twelve. ~ап [-’n'] the zodiac.
PHD.txt:325:farr-, v. xwarrah. Farrūbāģ [plwb(’)g] the first major Fire of Sasanian Eran, that of priests and nobles. farrox [plhw' | M prwx, N ~] fortunate, blessed, happy. ~ih: fortune, joy, happiness. filāsūfā [pyPswkp!y] philosopher. frabih [plpyh | (P frbyw), N farbih] fat, stout. Fradadafš [pldtpš = Av. fradašafšū-| the south-eastern continent of the earth. fradág [MHL < A mhr; ИРА! | N farda] tomorrow. frādahišnīh [pP dhšnyh] increase, progress. fradom [AWLA < Ar. !?wD; pltwm | (M prtwm)] first. ~th: first, beginning. fragan [plk?n'] base, foundation; origin. fragandan, fragan- [plkn-dn'} lay foundations. frahang [pl’hng | N farhang] education; knowledge. --estàn [-st?n!] school. frahanj-, v. frahixtan. frahist [p/h(y)st! | (M pryst)] most (superlative of freh), frahixtag [plhhtk' | N farhixta] educated, trained, skilled. frahixtan, frahanj- [plhhtn', pDhnc- | P frhynj-, N far~] educate, teach, instruct. framādār [рж?РЦ commander, ruler, chief. framān [pim^n! | M frmn, N farman] order, command; a minor degree of sin. ~-burdar [-bwlt?l | N -bardār] obedient, submissive. framāy-, ~išn, v. framüdan. framds [bl(?)mwš | M pr’mws, N farámos] forgotten. framošidan [plmwšytn'] = framuštan. framüdan, framāy- [plmwin', plm'd- | M prm'dn, prmy-, N far~] order, command. — $n: order, commandment. frāmuštan, frāmēš- [pl(?)mws-in' | M prhmwst, pr’mwi-, N fard~] forget. franaftan, *franam- [pinptn!, *plnm- | M prnpt, prnm-] go, proceed, depart. franāftan, franām- [pin!ptn!, pli m- | P fri m-] 1. lead, conduct, re- move, promote; 2. profess, propagate (faith). ~išn: removal, promotion, profession. frarast [p/”Pst'] a cubit (18 in.). fràrón [p lwn'] righteous, honest. ~ih : righteousness, honesty. frasang [plsng | N farsang) parasang (4 Roman miles).
PHD.txt:538:pādīrān [p'igP n!] restrained, held back. pādīrān(ēn)īdan, pādirān(ēn)- [þptgľn(yn)-ytn'] restrain, impede. padīriftan, padir- [MK BLWN-tn!Ü < A mqbl, V qbl; ptgl-ptn! | M pdyr-yptn, N paóiruftan] receive, accept. ~išn: reception, acceptance. īpadisār [ptys' | N padīsār ?] beginning, basis. tpadisār [ptys’/] bridle, halter. padisāy [pts’d | M рдуу] on account of, for the sake of. padist [ptst! | P pdyst] promise, vow. & (abar) burdan: promise. padistadan, padist- [ptyst-”tn! | (P pdystwd)] promise, vow. padistā(£) [ptyst*k! | (M pdystw)] = padist. padiš (pts | M pdys] to him, it; postposition (= pad) to, etc. padištān [pryst?n' | P pdyst??n] leg. padišxwar [ptshwl] dish, bowl. pādixšā(y) [SL Y TA < A йур; p’ths?(d) | M раху] ruler; powerful, authoritative, authorized. ~ЛЬ : sovereignty, authority. pādixšīr [p’thsyl] agreement, treaty. pad-néróg [PW Nnylwk!] strong. pad-niģerišn [PWNnkylin'] cared for, guarded. pādofrāh [p’twpl’s) = pādifrāh. pad-panag [PWNpnk!] guarded, protected. Р pádrazm [p’tlcm] battle. pàd-rózag [p’tlwck' | M p'drweg] fasting. pād-uzwān [p’??wzw’n'] reticent. ~ih: reticence. pad-wizén [PW Nwcyn!] choice, select. pādyāb [pty | N ~] ritually clean; ceremonial ablution. ~ih : ceremonial ablution. pādyāwand [p?tyd’wnd | J p'dywnd] strong, powerful. cAh : strength, superiority. pádzahr [p’tzhl | N pa(d)zahr] bezoar, antidote. pad-zyān [PWNzyd"?n'] harmful. pafšār- [pps?/-] shame. pafšīr- [ppsyl-] be ashamed. ~i8n(ih): shame. pah [p’h] sheep. ~ast [-st'] sheep-fold, -pen. pahikaftan, pahikaf- [ptkp-tn! | M phykf-] fall on, touch, hit, attack. ~išn: attack, fight. pahikāftan, pahikāf- [ptk’p-in'] throw on, make fight. pahikar [ptk] | M phykr, N paykar] picture, image. pahikār [ptk?! | M phyk”r, N paykār] struggle, battle, dispute. īpahikār- [ptk?/-] fight, contend with, defeat. pahikardan, *pahikār- [ptk’/-tn'] request, claim, consult.
PHD.txt:551:pillagan [plk’n' | M pylg, N ~] steps, ladder. pim [pym] pain, pang, sorrow. ~gén [-kyn'] sorrowful. pir [руі | N ~] old, aged, ancient. ~ih: age. piring [pling | M pryng, (N pirind)] monochrome damask, pist [pst! | N ~] browned flour. pistag [pstk! | IN pista] pistachio nut. pišīz [pšyc | N ~] small copper coin, ‘farthing’. pēhišn [pwhsn'] corruption, decay. pēlāwad [pwPft! | М pwl'wd, N pēlād] steel. ~ën [-yn!] (made of) steel. pondik [pndk' | Ar. b/fundug] hazel-nut. por [pwl | N —] francolin. pēryētkēš [pwlyw(k)kyf = Av. paoiryē.tkaēša-| (one of) the first teachers of the Mazdean religion. ~ЛЬ : the primal doctrine of the Mazdean religion. pēst [pwst! | = M, N ~] skin, hide; bark, shell. mēn [-yn! | N ~in] (made of) skin. pēšīdan, pēš- [pws-yin' | N <] cover, put on, wear. ~išn: covering. potk [pwtk' | N ~] sledge-hammer. poxtan, paz- [APPWN-tn' < А V?ph; pwhtn', pc- | M pwxtn, N ~] cook, bake. рӧу- [pwd- | (P pwd-), N ~] run. ~iSnig : running. p6z(ag) [pwc(k!) | N pēz(a)] snout, muzzle. püdag [pwtk! | N pūda) foul, rotten. —ih: rottenness. 1puhl [pwhl | N pul] bridge. *puhl [pwhl] expiation, atonement; punishment. puhlénidan [ pwhlynytn'] cause to atone. purnāy [pwln’d] adult. purr (MALE < A mlh; pul | M pur, N ~} full. =-ģāh [-g’s] at the fullness of time, about to die. ~-тюаһ [-mh] full moon. —-rawišnih [-lwbsnyh] fullness. ~-sardag [-sltk'] of all kinds. --xwarrah [-G DE] full of glory. pursidan, purs- [pwrs-ytn' | M pwrs-ydn, N ~] ask. Vu re: Е ~iSn: question. — ~i$nig : responsible. pus [BRE < A br-h; pws | = M, N =] son. ~ar [BREI, pwsl | M pwsr, N ~] son. —yàn [pwsd?n! | M pwsy’n] womb. pušt [52001 | = M, N ~] back; support, protection.
PHD.txt:663:xwāb [hw’b | N ~] sleep. xwābar [hw’l | M xwbr] beneficent. ~ig [-yk!] beneficial. —ih: beneficence, benefit. xwad [BNPSE < A b-nps-h; hwt' | M xwd, N ~] self; indeed. САҢ: selfhood, essence. xwaday [лору | M xwd'y, N ~] lord. ~th: lordship, sovereignty. ~war [-w’/] lordly. xwad-dósag [hwtdwsk'] self-indulgent. 7h : self-indulgence. xwah [AH TE < A *hth | N ~] sister. 1, ?x wüh-, ~išn, v. xwastan, xwāstan. xwahar [AH TEL v. xwah ; hw'hl | (M xwr), N xwdhar] sister. xwahl [eo hl | (M xwhr), № ~] bent, crooked. xwā(h)rīh [hw (h)yh | M xw'ryy] happiness, bliss. xwālist [hw’lyst' | (M xw’ryst)] sweetest. xwamn [hwmn', hmn' | M xwmn] sleep, dream. ~-wizar [-wc'/] interpreter of dreams, oneirocritic. xwān [hw!n! | M xw’n, N ~] tray, table. xwandan, xwān- [KRY TWN-, KLY TWN-tn! < А У д | M xwnd, xw'n-, N xwāndan) call, summon. Xwanirah [hwnyls = Av. x"aniraüa-] the central, inhabited continent of the earth. !xwar [kwl | M xwr, N ~] sun; cal. 11th day. Zwar [kwl = Av. x"ara-] a degree of sin. xwar-, —išn, v. xwardan. lxwàr [kw] | M xwr, N ~] light, easy; mean, abject. ~ih: ease; v. also x wührih. *xwar [%w/ | M xwr] food. xwür-, —išn, v. xwārīdan. xwaran [%w/n! | M xwrn] banquet. xwarāsān [hwlsn! | M xwr'?n, N ~] sunrise, east. xwār-bār [how?1b?l | M xwr w Pr, N ~] food and drink. xwardan, xwar- [OS TEN-tn! < Ath, V fth; hwltn! | M xwrdn, xwr-, N ~] eat, consume. ~išn: food. ~ignig : edible. ~išnīh: eating, consumption. xwardār [hwit?I] (legally) edible, not murdār. xwardig [hwityk' | M xwrdyg, N ~i] food. xwārēn [hw’lyn'] edible. xwārēn- [hw’lyn-] cause to eat, drink; feed; irrigate. xwarģ [wig | J xwwrg] ember. xwārīdan, xwār- [heo?1-ytnt] drink. —išn: drink, drinking.
PHD.txt:664:xwarüfrün 96 yal
PHD.txt:665:xwarūfrān [hwl(’)wpl’n' | M xwrwpr'n) sunset, west. xwarrah [GDE < A gdh | (M prh, N farr)] fortune, glory, splendour. ~6mand [-’wmnd] fortunate, glorious. xwarséd, v. xwarxséd. xwartar [hw ltl] minor (sins). xwarwarān [hwlwPn!, -bPn'] = xwardfran. xwar(x)8éd [Azl(h)syt' | M xwrxšyd, № xuršēd] sun. xwāstag [NKSY A < A nksy’; hw'stk! | M xw’stg, N ~a] property, wealth. i ~õmand [-wmnd] wealthy. xwastan, !xwāh- [(Y)PLHWN-tn! < А V plh; hwstn!, hw'd- | J xwh-, N xwast] tread, trample; thresh. ~išn: trampling. xwāstan, *xwāh- [BOYHWN-stn! < A МУ Бу; hw'stn!', hwd- | M xw’stn, xt h-, N ~] seek, want, desire; attract, acquire. --j&n : desire, attraction. xwastüg [hwstwk!' | N xustū] confessing, believing. ~ih: confession, belief, faith. xwaš [BS YM < А bsym; hw | M xw, N ~] pleasant, sweet, nice. ~ih: pleasantness, pleasure. xwēd [Awyt! | M xwyd, N ~] moist, fresh. ~ih: moisture, freshness. xwédódah [hwytw(k)ds, -d^t! = Av. x"aetwada0a-] kin-marriage. xwēn-āhan [Ahw(y)n ?syn! = Av. x"aéna- (ayah-)] shining metal. xwēš [NP ŠE < А npf-h; hwyš | M xwy(b)s, N ~] (one's) own. ~ih: possession. ~awand [kwyš*wnd | N ~] relative, kinsman. xwēšēnīdan, xwēšēn- [/nwyfyn-ytn!] appropriate, make one’s own. xwēš-kār [леу dutiful. ~th: proper function. xwēš-tan [NPSE tn! | N ~] self. xwéy [hwyd | N xway] sweat, perspiration. xwistan [hwystn'] sweat, perspire. xwurd [hwlt' | N ~] small, little. xwurdag [hwltk' | N ~a] something small, particle; astr. lunar mansion; (horse's) pastern. ~ih: smallness.
PHD.txt:1018:blessed farrox, hufraward.
PHD.txt:1060:bowl padišxwar, tašt.
PHD.txt:1636:dish padišxwar.
PHD.txt:1728:east OXastar, xwarāsān.
PHD.txt:1815:evil (a.) akēmand, апар, druwand, wad(ag), wattar, duš-; ~ deed dušxwaršt; ~ eye aš, dujdoys?rih; ~ rule dušpādixšāyīh; ~ ruler dušpādixšā(y); — speech dušēwāz- ih, dušhüxt; — spirit Ahreman, gannág mēnēg; ~ thought duš(hu)- mat; of ~ behaviour duškunišn; of — religion agdén, dujdén; of — speech duš-gēwišn; of — thought dušmenišn.
PHD.txt:2018:fortunate farrox, hangad, jahišnayār, xwarrahómand.
PHD.txt:2019:fortune bayēbaxt, baxt, farroxih, hangadih, jahišn, xwarrah.
PHD.txt:2109:glorious bamig, xwarrahomand.
PHD.txt:2110:glory abrang, bam, xwarrah.
PHD.txt:2200:happiness farroxīh, huramih, hun- sandih, hušnūdih, šādih, šnāyēn- išn, urwāzišn, xwa(h)rih.
PHD.txt:2201:happy farrox, huram, hušnüd, Sad, xunak.
PHD.txt:2490:irrigate xwarén-.
PHD.txt:2509:joy farroxih, šādīh, urwahm(an)ih.
PHD.txt:2848:mortal anēšxwar, géhanig, marg- ómand, 686mand, sazišnīg,
PHD.txt:3662:sin abārēnih, āstār, bazag(ih), mān- dag, wināh; degrees of — āgrift, anābuhlag, arduš, bāzāzanišnih, framān, ēyrišt, tanápuhl, xwar, yüt; cause to — āstārēnīdan.
PHD.txt:3782:splendour abrang, bam, xwarrah.
```


## [2026-09-14T01:34:24.178Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB\"\ngrep -n \"xvarr\\|xwarr\\|farrox\\|frax\\|xvarnah\\|xvarxSet\\|xvarSet\" NYB_vol2_glossary.txt | head -15\necho \"=== HUB 808 / 814\"\nawk 'BEGIN{RS=\"\\f\"} NR==830 {print}' HUB.txt | head -5\npython3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(d['HUB']['page_offset'], d['HUB']['lookup_hint'])\"",
 "description": "Nyberg and Hübschmann"
}
```


### [2026-09-14T01:34:25.405Z] TOOL RESULT

```
=== NYB
1400:duš-nam [dwán?m] abuse, invectives 15%. — = NP; duš-nam ‘ill-famed’ (SGV). duš-parg [dwáplg] unblessed, unfortu- nate, unhappy; ignoble, mean, opp. farrax" (g. v.) Mx 50?-4, Paz. dušparg, Skr dusta-samrddhi; a dušparg dz i dévq- dad Aog. 31, Skr. v. duscära. — dus-parg ‘whose parg is bad’ is a synonym of dušxvarr(ah) (a. v.), MPrth dwšfr = duš- farr (A-H III), consequently parg is a synonym of z%arrah (g.v.). The Paz.
1567:frax" [pl’hw'] broad, wide, comp. ~-tar 389. — NP faräx.
1568:frax"-caréh [~-c’lyh] to be restored thus 110" (instead of *frahang-cārēh); abstr. of *frax"-cür ‘having great means; pros- perous’, abstr. ‘prosperity’. |
1569:frax"éh width, prosperity 66!1.
1758:hae [MN ; hc 619] prep., with -c: MN-c = hac-ic; not with an encl. pron. (as to haciš, hacisan v.s. v. hactš); the original sense ‘accompanying, with’ (Skr sacā) is still transparent in ~ ... hämisi (g. v.) ‘together with’, but the meaning ‘from, of’ prevails since the OIr period. 1. Local: hàn yam ... hac dast i Artaxser 6 damik opast 92°; api-š hecak hac cah ul hixt 155; hakar hac asp bē nisinam 27?; hac star püdak tai mah pädak 93"; hac dar ētšān bagän namäc burt from the gate-way (i.e., halting at the entrance, from this place) I rendered adoration to His Majesty. P1:4; — figurative, with a great many vbs. and idioms, the sense of ‘from, of’ being more or less transparent. akahé- nitan, āšnūtan, pursitan, x"āstan, dast šustan hac ete., v. the individual ws.; — origin: ke cihr (Prth Shr) hac yazatān (Prth y’ztn) whose origin is from the gods, of divine origin HajB: 2.4 (HajA: 2.4). SPrs: 5-6 (yazdān) (SPrth: 5). P1: 2.4 (yazdàn) ; "Apasči... à hac Haran ŠPrs: 9; hac tohmak + Dārāt būt 18, etc. — 2. tem- poral: hac im róc from today onwards, henceforth 9"; hac im réc tdi 3 roc within three days 51%; hac rahikehv [lsykyhy] ever since my youth 1282-5; ete. — 3. after a v. n. it expresses the subj. of the act: patirak zanišn + hac ganäk menoi on the point of being slain by the Evil Spirit 46°-§; zanisn i devàn hac han i 0$ xvarrah the demons being slain by his divine splendour 461?; freftakeh + hac dēvān de- ception by-the demons 461; 4513-14; ete. —
1926:han-tai [ZK D] until, on to: ~ 6 mtyān van to the middle of the tree 415; ~ hàn i veh Dāitī 564; peš hac ~ ka-män ... jöyät before he devours us 98%’ (as to man, v.s. v. man). — Olr *anu-tävat 'to- wards as far (as), cf Skr tāvat ‘so long, so far’ (yāvat ‘as’), v. tāt; hence Milr *(h)an-tàv, SW han-tai, later *(k)andāt, Paz. anda. Prth han < anu, KZŠPrth 1.2 hn prhš L = han fraxé 6, Gr fog čurpoo0ev, also han 6 ibd. and l. 19 = Prs l. 24 D = tai, Gr ac. Not found in MPrthPrs — Av. (127) anu, OP anuv.
3931:Vānēt-xvarr(ah) [wnyt! GDH] n. pr. 1061913, — "The Khwarenah will gain victory’, cf s. v. x“arrah.
7133:farāmēš: frāmēš faräx, frax": faraz: frac farda: fratak farhanjidan: frahaxtan Faridün: Fréton farjam: frazäm farman: framan farmudan, farmay-: framatan farrah: x"arrah farrux: farraxu farsang: frasang farsüdan, farsäy: apa- sutak farvardgän, faravardigän: fravartikän faryäd: friyät farzänah: frazänak farzand: frazand
=== HUB 808 / 814
leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
```


## [2026-09-14T01:34:35.420Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n 'x\"arrah \\[' NYB_vol2_glossary.txt | head -5\ngrep -n 'x\"arr' NYB_vol2_glossary.txt | sed -n '1,6p'\necho \"=== FSF 250\"\npython3 - <<'EOF'\nt=open('FSF_pages.txt').read()\npages=t.split('\\f')\nprint(len(pages))\nimport re\nfor i,p in enumerate(pages):\n    if 'فرّ' in p or 'فر ' in p[:80]:\n        pass\n# find pages mentioning فریبرز\nfor i,p in enumerate(pages):\n    if 'فریبرز' in p:\n        print('fariborz leaf',i)\nfor i,p in enumerate(pages):\n    if 'فرّه' in p and 'ایزدی' in p:\n        print('farreh leaf',i)\nEOF",
 "description": "Nyberg xwarrah and FSF"
}
```


### [2026-09-14T01:34:36.813Z] TOOL RESULT

```
1504:Frádat-x"arrah [pl?dt' GDH] n. pr. 1069-12, — Av. (1015) Frádat.x"aronah- Yt. 131?8,
1692:Gor-ArtaxSér-x"arrah [gwl 'Ithšdi GDH] town in Pars built by Artaxsér 1 Papakan 11615, — Cat. 94, where references to other sources are given; I mention: KnS IV,
4074:| vazurg-x"arrah [LB’ GDH] of great glory,
4343:x"arrah [GDH] a divine essence, a special form of the Eternal Light, a splendour, a glory I. manifested in the gods: one swears by (pat) ~ % Ohurmazd bag u den imāzdēsnān 2117-22-28 (without bag). 2321-22 ; zor u ~ + visp-ākāh spēnāk meno datar Ohurmazd 1063-24, — 2. a cosmic essence 9215.19, — 3. Zartuxst’s divine essence 36-38. 43-45 passim; the elements con- stituting his individuality are his ~, fravahr and tan gohr 433-18; his rdi u ~ 51-52; v. also s: v. purr. — 4. the splen-
4524:zat-x"arrah [zt' GDH] whose “glory” (heavenly substance) is slain; extin- guished 6617., — V. z"arrah.
727:2aš [^5] the independent form of the cas. obl. 3d p. sg. = enel. -$ (g. v.); always preceding the w. to which it belongs; used 1. anaphorically in the interior of a sentence after a part of the sentence which has been placed first for emphasis: andar han Zartuxst | aš hac miyān Gp i hömikän burt || u pat uléh Zartuxšt | aš han i dašn paitištān hac Osan rote burt 5615-1? (Markwart's reading, Cat. 114 n. 1, is a failure); õi (pron.) mar | aš 6 pasčh gàv apāc rānēnīt 485; — not anaphorically: Ot (prep.) fravahr + Zartuxst | aš (viz. the snake) zafar frac zat 4012-13; purr-x"arrahéh i ax" à astómand | aš hac tan xYarrah from his (viz. Zartuxšt's) bodily splendour 377-8; — taking up an encl. -§ at the beginning of the sentence, after a part of the sen- tence which carries a lengthy attribute: api-š hamäk damik i-š apar rāh bit | aš *perävanihit kart 3316-17; — after an ad- verbial phrase beginning the sentence: adak apar pat jamän | aš hanjamanénit mūtak :61° (where aš anticipates mūtak, cf. s. v. -š). — 2. to introduce the apo- dosis (as api-$, adak-i8): after kakar 31?! ; after ka 327. 3319. 341. 565. 5717. 924. after a relative clause 3219, 9824, 100?7— 101?. — Probably identical with MPrthPrs š, written as an independent w. with two dots above (another explanation of this § v. A-H III, Gloss s. v.; ? in a fragmentary context [S] is obscure). Cf am, at, atün, asän.
1409:duS-x"arr(ah) [dws-GDH] unfortunate; ill-fated 11112. — Av. (755) dus-x"aronah- ‘ill-famed’. The ideogr. is to be read guarrah, but it is doubtful whether this form was used in compounds, cf MPrth dwšfr duš-farr as against the subst. frh, v. x"arrah.
1446:VII, 1934, 265-274; Nyberg, Rel., v. Index. Eran-x"arrah-kart-Sahpuhr [-GDH- =
1504:Frádat-x"arrah [pl?dt' GDH] n. pr. 1069-12, — Av. (1015) Frádat.x"aronah- Yt. 131?8,
1681:Gor-Artaxsér-x"arrah
1692:Gor-ArtaxSér-x"arrah [gwl 'Ithšdi GDH] town in Pars built by Artaxsér 1 Papakan 11615, — Cat. 94, where references to other sources are given; I mention: KnS IV,
=== FSF 250
485
fariborz leaf 99
fariborz leaf 165
fariborz leaf 176
```


## [2026-09-14T01:34:44.156Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('FSF_pages.txt').read()\npages=t.split('\\f')\nfor i in (99,165,176):\n    print('##### leaf',i)\n    print(pages[i][:1200])\nEOF",
 "description": "FSF leaves with Fariborz"
}
```


### [2026-09-14T01:34:45.232Z] TOOL RESULT

```
##### leaf 99
                                                                                   ‫برع‬


      ‫‪ ...‬چو برزد سر از برج خرچنگ ماه‬             ‫بدان بسرترین نام یزدان پاک‬
‫(‪)۴-۵۸۲-۸۶۱۱‬‬                                ‫برهخشنده خورشید و برتیره خاک‬
                     ‫گواه چنگ خرچنگ‪:‬‬        ‫)‪(1-۶4-4۷‬‬
  ‫چو برزد سر ازچنگ خرچنگ هور‬               ‫دتررجمه تفیسر طبری ص ‪۱۱‬و ‪۷۹‬با‬
‫جهان شدپراز جنگ و آهنگ و شور‬                 ‫یمن» آمدهاست‪.‬‬ ‫رنا‬
                                                             ‫تن»‬
                                                               ‫گمهی‬
                                                                  ‫رنام‬
                                                                     ‫زت «‬
                                                                        ‫بارا‬
                                                                           ‫عب‬
‫(‪)۵-۹۷۲-۲۲۷‬‬                                                  ‫وکون درم)‬
                                                                     ‫برج (باپیش اول س‬
                                ‫برج خوشه‬   ‫شکل یاچند گوش که بر‬        ‫ودانه‬
                                         
##### leaf 165
                                                                                  ‫پیوسته‬


                    ‫‪-۲‬خویش‪ .‬خویشاوند‪:‬‬                        ‫ز گفتار دهقان یکی داستان‬
     ‫بسی خویش و پیوند ما برده گشت‬
‫بسی مرد تیک اختر آزرده گشت‬                  ‫(‪)۲-۱۰۷۱-۵۱‬‬

 ‫(‪)۴-۱۸-۲۳۱۱‬‬                                        ‫همی خواهم از دادگر یک خحدای‬

                         ‫(ویس ‪:)۶۳۱-۷۴‬‬     ‫که چندان بمانم به گیتی به پای‬
     ‫تراواز خان و مانو خویش و پیوند‬               ‫که ‌این نام شهریاران پیش‬
 ‫جدا کرد و به دام بوری افگند‬                ‫بپیوندم از خوب گفتار خویش‬
                       ‫‪-۳‬سازش‪ ,‬نزدیکی‪:‬‬      ‫)‪(۶۴۶-4‬‬
                                                                                  ‫پیوسته‬
 ‫تهمورث در جنگ با دیوان پیروز شده‬
                                                    ‫پیوند‪:‬‬     ‫ه)»‬
                                                                 ‫نیض‬
                                                                   ‫انق‬
                                                                     ‫گ (‬
                                                                       ‫ییش‬
                                 
##### leaf 176
                   ‫(قبفه فتح اول اسم از تفتن)‬   ‫و در این بیت دقیقی ترنگ باخنگ (به‬
                             ‫گرمی» داغی‪:‬‬          ‫کسر اول) قافیه شده (اس‪۳‬ت‪)۶-۸۸-۹۳‬‬
    ‫همی جوشن اندر تنش برفروخت‬                          ‫بهگوش اندر آید ترنگا ترنگ‬
 ‫همی تف تیغش زمین را بسوخت‬                          ‫گ‬
                                                    ‫نر و‬
                                                       ‫خ؛ بو‬
                                                           ‫هواپر شده نعره‬
‫‏(‪(V71-11۸-۲‬‬                                                                      ‫ترباک‬
           ‫سیاوش به پیش جهاندار پاک‬                  ‫پازهر‪ .‬پادزهر‪ .‬ضدزهر‪ .‬داروی زهر‪:‬‬
 ‫بیامد بمالید رخ رابه خاک‬                             ‫کهاین آشتی جستن از بهر چیست‬
           ‫کهاز تف آن کوه آتش برست‬              ‫نگهکنکهتریاک این زهر چیست‬
 ‫همه کامۂ دشمنان گشت پست‬                        ‫‏)‪(AFV-O۶-F‬‬

 ‫(‪)۳-۷۳۲-۳۲۵‬‬                                                  ‫زگیتی مبراخشوتریست بهر‬
                         ‫(اسدی ‪:)۵۷۴-۸۷‬‬         ‫پراگنده بر جای تریاک زهر‬
          ‫بلند آتش مهرگانی بساخت‬                 ‫(‪)۴-۸۶۱-۱۴۸‬‬
```


## [2026-09-14T01:34:51.553Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('FSF_pages.txt').read()\npages=t.split('\\f')\nimport re\nfor i,p in enumerate(pages):\n    h=p.strip().split('\\n')[0].strip()\n    if 'فر' in h[:12] and i>200:\n        print(i, h[:40])\nEOF",
 "description": "FSF pages with فر headword"
}
```


### [2026-09-14T01:34:52.705Z] TOOL RESULT

```
338 ‫فراز‬                                  
340 ‫فرسودن‬                                
342 ‫فرهنک‬                                 
343 ‫فرهنگی‬
344 ‫فریادبخش‬                              
440 ‫نفریدن‬
```


## [2026-09-14T01:34:55.280Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('FSF_pages.txt').read()\npages=t.split('\\f')\nfor i in (340,341,342):\n    print('##### leaf',i)\n    print(pages[i][:1800])\nEOF",
 "description": "FSF farr pages"
}
```


### [2026-09-14T01:34:56.459Z] TOOL RESULT

```
##### leaf 340
‫فرسودن‬                                      ‫‪۳۳۲‬‬


                      ‫فرزد (با زیر اول و دوم)‬           ‫درم داد و نسقل و جام و نید‬
‫«سبزه‌ایست در نهایت سبزی و تازگی و‬                 ‫سوسفندی تواند بريد‬  ‫گر‬‫س‬
    ‫تری و آن را فریز نیز گویند» (برهالن)‪:‬‬
            ‫ورانام شاپور کرد اورمزد‬
‫که سروی بد اندر میان فرزد‬                          ‫(‪)۶-۵۱۲-۲۵۸‬‬
 ‫‪۰-۱۵۲‬‬                                                                                ‫فرخندهپی‬
                       ‫(اسدی ‪:)۳۲۳-۳۳‬‬             ‫[‪ :‬خجسته‪ ,‬فرخ» مبارک»‬         ‫از فرخنده‬

     ‫دوصد گونه گل بد ميان فرزد‬
‫فروزان چو در شب ز چرخ آورمزد‬                                                      ‫مبارک‌قدم‪:‬‬


                    ‫فرسپ (با زبر اول و دوم)‬        ‫سیاوش از مادر زاییده شده به كاوس‬

‫«آن دار ستبرباشد کهبدوبامرا بپوشانند و‬                                         ‫مزده می‌دهند‪:‬‬


         ‫ثقل همه بر وی بود» (لفت فرس)‪:‬‬                         ‫کی‬   ‫بگفتند با شاه کاوس‬


      ‫چنین گفت هیشوی کاین پیر گرگ‬                 ‫از ماه فرخنده‌یی‬     ‫که برخو ردی‬


‫همی برترست از هیونی سترگ‬                           ‫(‪)۳-۰۱-۷۶‬‬

      ‫سروهاش چون آبنوسی فرسپ‬                                          ‫دیم‪:‬‬
                                                                         ‫قم پ‬
                                                                            ‫دشو‬
                                                                              ‫‪-‬یضبان‬
                                                                                   ‫نق‬
‫چو خشم آورد بگذرد بر دو اسپ‬                        ‫افراسیاب به پیران می‌گوید‪ :‬کس بفرست‬
‫(‪)۶-۹۲-۲۵۳‬‬                                        ‫رانزد‬   ‫ا]دورش‬
                                                   
##### leaf 341
                                          ‫‪۳۳۸‬‬                       ‫فروختن‪ .‬افروختن‪ .‬فروزیدن‬

        ‫یکی مجمر آورد و آتش فروخت‬                                            ‫فروریختن‪:‬‬
 ‫وز آن پر سیمرغ لختی بسوخت‬                                     ‫بدین جایگه مرگ را آمدیم‬
‫(‪)۱-۶۳۲۰-۸۷۴۱‬‬
              ‫بزرگان ز تو دانش آموختند‬          ‫(‪)۶-۵۸۱-۵۱۳‬‬

 ‫به تو تیرگی‌ها برافروختند‬                      ‫افراسیاب گریزان کازیخسرو بهگنگ دژ‬
‫(‪)۱-۱۱۲-۳۴۱۱‬‬                                             ‫ره به خسرو پیام می‌فر ستد‪:‬‬
                                                                                  ‫پناه ب د‬

       ‫زخار و ز خاشاک و شاخ درخت‬                         ‫گر اورک گوبیک تهرکان چین‬
 ‫یکی آتشی برفروزید سخت‬                           ‫بگیرم زنم آسمان بر زمین‬
‫(‪)۲-۱۷۱-۲۲‬‬                                               ‫به شمشیر بگذارم اين انجمن‬

  ‫یز‪,‬‬
    ‫دن ا‬
       ‫شرخاشد‬
            ‫عنی س‬
                ‫میت‬
                  ‫‌ن ب‬
                     ‫های‬
                       ‫بدر‬
                         ‫و‬
                                  ‫شرم‪:‬‬

‫پرستندگان از زیبایی زال نزد رودابه سخن‬           ‫نساید کسی کو نفرسودنیست‬
                              ‫می‌گویند‪:‬‬          ‫)‪(۵-۵۳-4۷11‬‬
        ‫چو بشنید رودابه گآفنت‌وگوی‬                      ‫از رودکی (لخت فرس‪ .‬واژه فرسد)‪:‬‬

‫ولنارگون کرد روی‬
               ‫برافروخت گ‬
‫(‪)۱-۰۶۱-۲۷۳‬‬                                      ‫هر که انجام راست فرسدنیست‬
   ‫و درین بیت به‌معنی تابیدن‪ .‬درخشیدن‪:‬‬                  ‫(فرسدنی‪ ,‬باپیش سین <فرسودنی)‬
         ‫به پاسخ چنین گفت کاوس شاه‬                                      ‫(ویس ‪:)۶۶۳-۵۳۳‬‬
‫که از تو فروزد نگین و کلاه‬                                 ‫عجب‌تر آنکه چندی جور بینم‬
‫(‪)۲-۳۳۱-۸۸۶‬‬       
##### leaf 342
 ‫فرهنک‬                                      ‫‪۳۳۹‬‬


                         ‫=روختن‬
                              ‫فروزیدن ف‬                ‫است تاپیام پدررابهاوگزارش دهد‪:‬‬
                            ‫روشن کردن‪:‬‬                      ‫زریر اندر آمد چو سرو بلند‬
              ‫بدوگفتچون تیرهگرددهوا‬                ‫تخت ان ‪:‬متا‬         ‫یارس‬
‫فروزیدن شمع باشد روا‬                                     ‫ز قیصر بپرسید و پوزش گرفت‬
 ‫(‪)۶-۲۶-۶۶۷‬‬                                       ‫همان رومیان‌را فروزش گرفت‬
                                        ‫فره‬       ‫(‪)۵-۹۵-۲۱۸‬‬
                     ‫به واه فر نگاه کنید‪.‬‬         ‫(پرسیدن ج=ویای تندرستی کسی شدن‪.‬‬
                                    ‫فرهنگ‬             ‫فروزش دنرسهخمهه‌ها آمده است‪).‬‬
     ‫پورداود ريشة اینواژه راچنین می‌دهد‪:‬‬                         ‫رستم دربارة اسفندیار گوید‪:‬‬
 ‫=‬     ‫‪۵‬‬
       ‫‪:۵۳‬یا‬
           ‫«فرهنگ‪ :‬از فریافرا‪-‬اوستا ‪۳۳‬‬                      ‫که هرچند من بیش پوزش کنم‬
‫ا‪.‬نسکریت‪ :‬پرا ‪- ۵:۳‬فرا رفتن‪ ,‬فرا‬
                               ‫پسیش‬               ‫که این شیردل را فروزش کنم‬
 ‫خوان‌دن‪ .‬فرمودن‪ .‬فرزانه» فرزند‪.‬‬                  ‫(‪)۶-۲۹۲-۹۱۲۱‬‬

‫فرستادن‪ .‬هنگ‪ :‬اوستا ‪( 80۵۳۱‬تبدیل ] به‬                          ‫نجوید همی جز همه ناخوشی‬
 ‫نظایر زیاد دارد مانند میترا ‪- 2001/۷‬مهر‬           ‫گبفهتار کوردار گوردنکشی‬
 ‫=هر) در اوستابه معنای‬
                     ‫‪-‬چیترا‪ )۵711‬چ‬                 ‫(تنها در یک نسخه لنینگراد به جای‬
‫کشیدن‪ .‬از این مصدر چندین واژه در‬                  ‫فتروزشن نیایش آمده است‪ .‬در نسخۀ‬
 ‫فارسی به جا مانده‪ :‬هنجیدن‪ ,‬آنهجیدن‪.‬‬                    ‫بایسنقری نیز فروزش ضبط است)‪.‬‬
 ‫هختن ه=یختن» آهیختن ‪-‬فرهختن‪,‬‬                                                         ‫فروزنده‬
 ‫فرهخته‪ .‬فرهی
```


## [2026-09-14T01:35:09.889Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('FSF_pages.txt').read()\npages=t.split('\\f')\nfor i in (337,338,339):\n    h=pages[i].strip().split('\\n')[0]\n    print('##### leaf',i,h[:40])\n    if 'فر' in pages[i]:\n        idx=pages[i].find('فرّ')\n        print(pages[i][:1400])\nEOF",
 "description": "FSF farr entry"
}
```


### [2026-09-14T01:35:11.126Z] TOOL RESULT

```
##### leaf 337 ‫‪۳۳۴‬‬                                 
                                               ‫‪۳۳۴‬‬                                 ‫فراختن‪ .‬افراختن‬

‫بسیار قابلتوجه است کهدر نسخۀ سوم‬                      ‫(پورداود‪ .‬پشت‌ها ‪۲-۳۱۳‬‬             ‫‪0‬‬

                      ‫لنینگراده در بیت زیر‪:‬‬          ‫«دو لغت مصطلح فارسی کهفر و خره باشد‬
             ‫تو را باد جاوید تخت ردان‬                ‫اولی نزدیک است به لهج فرس هخامنشی‬
‫همان تاج و هم فره موبدان‬                             ‫[فرناه] و دومی‌به لهج اوستایی‪ .‬در ترکیب‬
 ‫(‪)۱-۷۳۱-۷۲‬‬
                                                     ‫پهلوی بجای کلمة فر‪ .‬چنانکه از برای‬
   ‫به جای فره «خحورده» نوشته شده است‪.‬‬                ‫یک کلمۀ‬       ‫ا‪.‬رروش»‬
                                                                         ‫زات‬
                                                                           ‫هلم‬
                                                                             ‫بسیاری ا«ز ک‬

 ‫بی‌گمان «خورده» تحریف خوره ف=ره‬                     ‫سامی استعمال شده گدمن ‪namdaG‬‏‬

 ‫می‌باشد و چنین برمی‌آید کهنوشتن خوره‬                     ‫گفته‌اند» (پورداود‪ .‬بشت‌ها ‪)۲-۴۱۳‬‬
‫به جای فره کارنسخه‌نویس نیست‪ .‬چون‬                    ‫‪-۱‬فروغ‪ .‬نور ام وهبتی است که‬
‫اگر اوبااین واژه آشنایی می‌داشت درست‬                 ‫اهورامزداء ایزد به کسی که شایستۀ آن‬
‫آن را می‌نوشت‪ .‬پس خود فردوسی واه‬
‫«خوره» را در این بیت به کار برده است و‬      
##### leaf 338 ‫فراز‬                                  
‫فراز‬                                         ‫‪۳۳۵‬‬


                       ‫‪-۳‬به‌معنی پدید‪:‬‬                  ‫چو روی زمین گشت چون پر زاغ‬
‫هوشنگ برای کشتن مار سنگی می‌اندازد‪.‬‬                ‫ز افراز ک وه اندر امد چراغ‬
‫آن سنگ بهسنگ دیگر باز می‌خورد و‬                    ‫(‪)۴-۳۲-۲۴۲‬‬


                       ‫فروغی پدید می‌آید‪:‬‬                                    ‫(ناصر ‪:)۲۰۲-۸‬‬

           ‫نشد مارکشته و لیکن ز راز‬                    ‫‪...‬خیره مر آب روان را چهکنیسربه‌فراز؟‬
‫ازین طبع سنگ آتش آمدفراز‬                           ‫‪-۲‬بهمعنی پیش نزدیک‪( ,‬در‬
 ‫(‪۱۲۲-۶6‬‬                                             ‫ترکیب‌های‪ :‬فرازآمدن» تن‬
                     ‫‪۴‬به معنی گرد‪ .‬جمع‪:‬‬                                           ‫آوردن‪:)...‬‬
                ‫بدا واه تست ما وا نیاق‬                           ‫بدو گفت پیران که‌ای رزمساز‬
‫که از جور و بیدادی آمد فراز‬                        ‫بترسم که روز بد آید فراز‬
 ‫(‪)۵-۸۶۲-۲۵۵‬‬                                       ‫(‪)۴-۸۱۲-۴۵۱‬‬

           ‫بسنده کنم زین جهان گوشه‌ای‬                                       ‫(منوچهری ‪:)۹۳‬‬
 ‫به کوشش فراز آورم توشه‌ای‬                              ‫نوبهار آمد و آوردگل تازه فراز‬
 ‫(‪)۱-۳۱۰۱-۸۰۴‬‬
                                                   ‫می خوشبوی فرازآور و بربطبنواز‬
                ‫کنون من ز ترکان جنگاوران‬                ‫بالیند اختر نام‌آور‪ ,‬تاچندبکاه
##### leaf 339 ‫‪۳۳۹‬‬                          ‫فراز آ
                                                   ‫‪۳۳۹‬‬                          ‫فراز آمدن بکراری یا جیزی‬

‫بلند کردن‪ .‬از‬      ‫شیدن‬
                      ‫کلا‬
                        ‫‪- ۱‬بالا بردن با‬                  ‫ازنقل معناو بیت شاهد از فرهنگ‬
 ‫همین ریشه‪ :‬فراختن‪ .‬افراختن‪ .‬فراشتن‪.‬‬                                 ‫جهانگیری» خود چنین می‌نویسد‪:‬‬
                                   ‫افراشتن‪:‬‬               ‫«لیکن درین بیت به معنی نزدیک مناسب‬
           ‫سازیده بود‬   ‫که ضحای‬     ‫طلسمی‬                ‫انی این معنی چند گواه آوردم‬‫رم‬ ‫بت‪».‬‬
                                                                                          ‫اس‬
 ‫سرش بآسمان برفرازیده بود‬                                ‫تا درستی گفتار جهانگیری آشکارتر گردد‪.‬‬
 ‫(‪)۱-۸۶-۶۱۳‬‬                                               ‫‪-۵‬امر از فعل فراختن‪ :‬به‌معنی بردار»‬
                                   ‫فراختن‪:‬‬                                              ‫برکش بلند کن‪:‬‬
   ‫به‌نزد پری چسهرگان رفت زال‬                                     ‫سخن‌ها به ما برکنون شد دراز‬
                                                         ‫اتگشرنه‌ای جام می را فراز‬
 ‫(‪)۱-۶۴۶۱-۵۲۴‬‬                                             ‫(‪۶-۱۶۲-۵۲۷‬‬
                                   ‫افراختن‪:‬‬                                         ‫نخست ازل‪.‬‬
```


## [2026-09-14T01:35:21.400Z] TOOL CALL #87: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%81%D8%B1",
 "prompt": "Persian فر (farr): etymology - Middle Persian, Old Persian farnah-, Avestan xᵛarənah-, meaning 'glory, splendour'. Quote the etymology section."
}
```


## [2026-09-14T01:35:22.652Z] TOOL CALL #88: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/sun",
 "prompt": "Etymology of English 'sun', 'Sunday', 'south' and their PIE root; also mention of Latin sol / solar if present."
}
```


### [2026-09-14T01:35:25.511Z] TOOL RESULT

```
# Etymology of Persian فر (farr)

Based on the Wiktionary entry, the Persian word **فر** (farr) has the following etymological background:

**Etymology 1** traces the word to Middle Persian origins: "Inherited from Middle Persian 𐫛𐫡𐫍 (prh /farrah/), from Old Persian *farnah ('glory')."

The term encompasses meanings related to radiance and magnificence, including "splendour," "beauty," "elegance," "brilliance," and "luster." These semantic associations align with its ancient root meaning of glory, reflecting how the concept of divine radiance or splendor was understood in Old Persian linguistic tradition.
```


### [2026-09-14T01:35:28.134Z] TOOL RESULT

```
# Etymology of Sun, Sunday, South, and Related Terms

## Sun

The word "sun" traces back through Middle English *sonne* to Old English *sunne*, deriving from Proto-Germanic *\*sunno*. Ultimately, it stems from the PIE root *\*s(u)wen-*, an alternate form of *\*sawel-* meaning "the sun."

Interestingly, Old English treated "sun" as feminine, and English speakers used feminine pronouns until the 16th century, when masculine usage became standard.

## Latin Sol and Solar Terms

The page confirms that Latin *sol* ("sun") also originates from the PIE root *\*sawel-*. The adjective "solar," attested from the mid-15th century, comes from Latin *solaris*, meaning "of, pertaining to, or determined by the sun."

## Sunday

While the page doesn't provide detailed etymology for "Sunday" itself, it appears in the related words list, suggesting a connection to the sun-word family (Sunday literally means "sun's day").

## South

**The provided content does not discuss the etymology of "south."**

The document focuses specifically on "sun" and sun-related compounds like sunbeam, sunburn, sunshine, and sunflower, along with celestial terms like solstice and aphelion.
```


## [2026-09-14T01:35:30.514Z] TOOL CALL #89: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/south",
 "prompt": "Etymology of English 'south': Proto-Germanic form, relation to the sun word and PIE *sawel-."
}
```


## [2026-09-14T01:35:32.455Z] TOOL CALL #90: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D8%B1%D8%A7%D8%B3%D8%A7%D9%86",
 "prompt": "Persian خراسان (Khorasan): etymology - Middle Persian xwarāsān, components xwar 'sun' + āsān 'coming/rising'. Quote it."
}
```


### [2026-09-14T01:35:35.743Z] TOOL RESULT

```
# Etymology of "South"

According to the Online Etymology Dictionary, the word "south" originates from Old English *suþ*, derived from Proto-Germanic *sunthaz*, which may literally mean "sun-side." This connection reflects the word's possible relationship to the base of *sunnon*, meaning "sun."

The term's development includes:

- **Adverbial use**: Old English speakers employed it to mean "southward, to or toward the south"
- **Adjective form**: Around 1300, it began describing things "being or situated in the south"
- **Noun sense**: By the late 13th century, it referred to "that one of the four cardinal points directly opposite to north"

The etymological entry notes that "Old French sur, sud (French sud), Spanish sur, sud are loan-words from Germanic, perhaps from Old Norse suðr," suggesting linguistic borrowing across Romance languages influenced by Germanic origins.

The word's underlying PIE root is *sawel-, connecting it fundamentally to concepts of celestial direction and solar positioning—a fitting origin for a cardinal direction associated with the sun's position in the northern hemisphere's sky.
```


### [2026-09-14T01:35:36.338Z] TOOL RESULT

```
# Khorasan Etymology

According to the Wiktionary entry, the Persian word **خراسان** (xorâsân) derives from Middle Persian *xwarāsān*, which literally means "sunrise; east."

The etymology breaks down as follows:

> "Equivalent to خور (xwar, 'sun') + آسان (âsân, 'coming')"

The source notes that *âsân* represents a Parthian verb conjugation signifying "to come, to rise," while the sun component connects to related Persian terms like *xoršid* (sun/sunshine). This naming reflects the region's geographical position as the eastern territory where the sun rises.
```


## [2026-09-14T01:35:46.874Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n 'https://en.wiktionary.org/wiki/%D8%AD%D8%B1%D8%A8%D8%A7%D8%A1' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/seh%E2%82%82wel-' \\\n 'https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%B1%D8%B4%DB%8C%D8%AF' \\\n 'https://en.wiktionary.org/wiki/%D8%AE%D8%A7%D9%88%D8%B1' \\\n 'https://en.wiktionary.org/wiki/%D9%81%D8%B1' \\\n 'https://en.wiktionary.org/wiki/%D8%AE%D8%B1%D8%A7%D8%B3%D8%A7%D9%86' \\\n 'https://www.etymonline.com/word/sun' \\\n 'https://www.etymonline.com/word/south' ; do\n python3 tools/fetch_source.py \"$u\" --note 'pdf page 432, root Sawel/Su 3 (sun): verification of Arabic hirba, PIE sawel-, xorshid, khavar, farr, khorasan, English sun/south' 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-14T01:35:50.697Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/6a9c3b138bb69f5f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/873e5dea84cb866b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/759393d8a6ff9320.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/94d63223cca05bfa.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9f74456481cfa42e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/334dc2fc4f3fc592.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cea5dcaa225e216c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/eed8f8f2cf883623.txt
```


## [2026-09-14T01:35:58.205Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN sun\"\ngrep -n \"1\\.52 SUN\\|^1.52\\|Sun\\b.*sāwel\\|sāwel\" SYN.txt | head -10\ngrep -n \"Av. hvar\\|hvarə\\|NPers. xurs\" SYN.txt | head -10\necho \"=== WLD Bd2 446\"\ngrep -n \"sāu̯el\\|sāuel\\|sā́u̯el\\|sāwel\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -10",
 "description": "Buck and Walde-Pokorny"
}
```


### [2026-09-14T01:35:58.327Z] TOOL RESULT

```
=== SYN sun
1661:1.52 SUN
18716:1152 Poor
26633:1052
29035:1152 SELECTED INDO-EUROPEAN SYNONYMS
31543:1252 SELECTED INDO-EUROPEAN SYNONYMS
33896:1352 SELECTED INDO-EUROPEAN SYNONYMS 19.57 HOST
1662:Lo” i ial. aféAtos, Goth. sauzl, sunnéd Lith.  saulé So oe : ON _ sdl, sunna Lett. saule NG — #Xos Dan. sol Ch&Sl. _ sliintce Lat. sol Sw. sol SCr.  sunce It. sole OE sunne, sunna Boh. — slunce Fr. soleil ME sonne Pol. slovice Sp. sol NE sun Russ. solnce Rum. soare Du. zon Skt. suar (Ved.), strya-, Ir. grian OHG = sunna ravi-, etc. NIr. = grian MHG sunne Av. hvara, gen. hird and W. haul NHG __sonne x’éng Br. heol
=== WLD Bd2 446
```


## [2026-09-14T01:36:00.614Z] TOOL CALL #93: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1661,1690p' SYN.txt",
 "description": "Buck 1.52 SUN"
}
```


### [2026-09-14T01:36:00.678Z] TOOL RESULT

```
1.52 SUN
Lo” i ial. aféAtos, Goth. sauzl, sunnéd Lith.  saulé So oe : ON _ sdl, sunna Lett. saule NG — #Xos Dan. sol Ch&Sl. _ sliintce Lat. sol Sw. sol SCr.  sunce It. sole OE sunne, sunna Boh. — slunce Fr. soleil ME sonne Pol. slovice Sp. sol NE sun Russ. solnce Rum. soare Du. zon Skt. suar (Ved.), strya-, Ir. grian OHG = sunna ravi-, etc. NIr. = grian MHG sunne Av. hvara, gen. hird and W. haul NHG __sonne x’éng Br. heol
Nearly all the usual words for ‘sun’ belong to a single inherited group.
1. IB *sawel-, etc., a group with vow- el gradation, parallel /- and n- forms (the Slavic fr. *sulno- with added dim. suffix), and variation in gender. Walde-P. 2.446. Ernout-M. 950f. Falk-Torp 1105. Feist 412, 460. Here belong all the words listed except the following.
2. Ir. grian, NIr. grian, fr. *greina, prob. formed fr. the weak grade of IE *g’her- seen in words for ‘hot, heat’, as Nir. gor, NE warm, Grk. Oepyds, Skt. gharma-, etc. This connection is ques-
tioned by Pedersen, KZ 38.197 (Walde- P. 1.688). But cf. esp. Skt. ghrna- ‘heat? and ‘sunshine’, and (fr. Skt. gharma-) Hind. ghém ‘sunshine’, Gypsy gam, k‘am ‘sun’ (Sampson, Dial. of Gypsies of Wales, 166).
3. Skt. ravi-, perh. the commonest class. word for ‘sun’, Arm. arev ‘sun’.: Skt. aruna-, arusa- ‘reddish’ (both often applied to the sun), Av. aurusa- ‘white’. Walde-P. 2.359. Uhlenbeck 246.
Among other Skt. words for ‘sun’ are : bhana- fr. bha- ‘shine’, bhas-kara-, lit. ‘light-making’, dina-kara- lit. ‘day-mak- ing’, arka- fr. arc- ‘shine’.
1.53 MOON Grk.  cedjvn Goth. ména Lith. ménuo, ménulis NG  devyapt (cedrv7 lit.) ON mani (poet.), tungl Lett. ménesis Lat. lina Dan. maane ChSl. luna, mésgct It. luna Sw. mane SCr.  mjesic Fr. lune OE mona Boh. _mésic Sp. -luna ME mone Pol.  ksigzyc Rum. lund NE moon Russ. luna Ir. ésce (luan) Du. maan Skt. (mGs-), candra-, ¢a- Nir. gealach, ré (éascd) OHG wmédno ¢cin-, etc. W. Ueuad, lloer MHG mane Av. mah- Br. loar NHG mond
1. IE *ménes-, *mén(n)s- ‘moon’ and | ‘moon’, ménesis ‘month’), Lett. ménesis,
‘month’, presumably fr. *mé- ‘measure’. Walde-P. 2.271f. Ernout-M. 607 f. Walde-H. 2.71. Berneker 2.51.
Here belong: (1) with the same form in both senses, Lith. ménuo, etc. (but here also with differentiation ménulis
ChSl. mésect (but mostly ‘month’; luna more common for ‘moon’), SCr. mjesic, Boh. mésic, Skt. mas- (as in Rigveda, later mostly ‘month’, rarely ‘moon’), Av. mah- (OPers. mah- ‘month’), NPers. mah-, Toch. A maf, or for ‘moon’ maf
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
THE PHYSICAL WORLD IN ITS LARGER ASPECTS 55
+ (nat ‘god, goddess’ used as a de- eS ay (2) with differentiation, all the Gme. forms, as Goth. ména ‘moon’, ménops ‘month’, NE ade month, etc.; Toch B mem ‘moon eae ‘month’ (so Benveniste, Festschrift Hirt. 2,234, but S. Levi, Fragments Koutsch. 1.121 gives ‘lune’ for both forms).
Elsewhere, namely in Greek, Italic, Celtic, Albanian, Armenian, and in some of the Slavic languages, the words of this group have persisted only in the sense of ‘month’ (Grk. piv, Lat. ménsis, Ir. mi, etc.; 14.61) and have been displaced in the sense of ‘moon’ by other words, most of them from the notion of ‘brightness’ as follows.
2. Grk. cedqvn, Dor. ceddéva, Lesb. cedavva : oédas ‘light, brightness’ (of fire or the heavenly bodies). Walde-P. 2.531. Boisacq 858.
NG g¢eyyap:, dim. of Grk. déyyos ‘light, splendor’ (of daylight or moon- light).
3. Lat. lina, fr. *leuksna- (cf. Praen. losna) : Lat. lia, lamen ‘light’, Grk. Aeuxds ‘bright’, Av. raoxsna- ‘light’, OPruss. lauxnos ‘stars’, ete. Here also as ‘moon’, Ch§l., Russ. luna, Arm. lusin, Ir. wan, (poet.; Thurneysen, Z. deutsch, Wortf. 1.189) and, fr. a parallel form of
the root, W. lleuad, lloer, Br. loar? Walde-P. 2.408 ff. Ernout-M. 570 ff.
From Lat. lina come It., Sp. luna, Fr. lune, and Rum. lund, the last both ‘moon’ and ‘month’, because of the double sense of Slavic més¢ci. —
4, Ir. ésce, NIr. éasca : Osc. eiduis, Lat. idus ‘ides’? Walde-P. 1.103.
NIv. gealach ‘moon’ also ‘light, bright- ness’, fr. geal ‘bright, white’ (15.57).
Ir. ré ‘period of time’, NIr. also esp. ‘moon’ Av. ravah- ‘space, room’, etc.(?). Wendryes, RC 28.141.
5. ON tungl, replacing manz in prose, beside himun-tungl ‘heavenly body’ : Goth. tuggl, OE tungol ‘heavenly body’, root connection? Walde-P. 1.792. Feist 481 f.
6. Pol. ksiezyc, displacing miesiac in the sense of ‘moon’, dim. of ksiqdz in its older meaning ‘prince’ (19.35). As the sun was the lord of the day, the moon of the night, the latter was the lesser ‘prince’. Briickner 277.
7. Skt. candra-, also (combined with mdas-) candramas- : (¢)candra- ‘bright’, (¢)cand- ‘shine’, Lat. candére ‘shine’, Alb. haéné ‘moon’, etc. Walde-P. 1.352.
Skt. cacin-, fr. gaga- ‘hare’, after the supposed resemblance of the markings on the moon.
```


## [2026-09-14T01:36:09.292Z] TOOL CALL #94: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"sāu̯el\\|sauel\\|sāuol\\|suel-, sūl\\|s[āa]u.el\" incoming/WLD/WLD_Bd2_pages.txt | head -10",
 "description": "WLD Bd2 sauel"
}
```


### [2026-09-14T01:36:09.365Z] TOOL RESULT

```
29589:446                                sauel, suu41-,    siiel-, sul-,   suen-, sun-
29615:sauel-, suuel-, suel-, sul- „Sonne“,                   woneben snen-, sun-, so da6 sich sau-,
34911:also nicht mit su-en- „Sonne, Licht“ (s. u. sauel-) identisch (z. B. Pick I^
35319:ai.    Svarita zu silvar^                 svdr „3onne'',     s.    "^sauel-^    also   auf den Sonnenglanz
35381:   Ygl. Pick 1^ 580, Persson Wzerw, 231, Beitr. 578 f.       ^sauel- „Sonne“.
```


## [2026-09-14T01:36:11.963Z] TOOL CALL #95: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '29589,29660p' incoming/WLD/WLD_Bd2_pages.txt",
 "description": "WLD Bd2 p.446 sauel entry"
}
```


### [2026-09-14T01:36:12.024Z] TOOL RESULT

```
446                                sauel, suu41-,    siiel-, sul-,   suen-, sun-



Hurde zusammengepfercht^ vgl. zur Bed. frequens fmcio; nicht uber-                 :



zeugend dagegen Ehrlich TJnters. 75: sae-pe, wie nem-pe^ mit *sai „irgend-
wann*‘ als Vorstufe von sf „wenn“); gr. alpiaoid „Gestrupp znr Anlage einer
Umzaunung(Hoin.), Steinmauer als Einfriedigung (Herod.)“, aip,6g „Dickicht“
Aesch.), Gbf.               "^saip-mos (Froehde BB. 17, 318, Wackernagel
Verm. Beitr. 39).
  Abweichende Auffassungen verzeichnet Yf. LEWb.^ 669. Unsicher wird
die Gleichung dadurch, da6 die roman. Sprachen nicht ae^ sondem e vor-
aussetzen; ist dieser Einwand geniigend tragfahig, so konnte lat. sepi als
dehnstufiger St. (wie sMes) nach Fay Am. J. Phil. 31, 422 zu onXiag* AoxqoI
rovg TOTiovg IvoTg ovveXavvovxeg dqi'dpovai to. nQO^axa xal rd pooxYipaxa
Hes. gehoren.
  Nicht iiberzeugend ist Zerlegung von alpaoid in alp-aoid, dessen 2. Glied
zu ai. atasd- n. „Gestrupp, Gebiisch^ gehore (Uhlenbeck Ai. Wb. 5) oder
zu lat. scntis (doch s. u. qs-en-^ qes-) nach Schrader KZ. 30, 462 f. (beides
verbindet Siitterlin IF. 4, 104 unter idg. [s^net-, [s]nt--; verfehlt trotz Char-
pentier BB. 30, 157, gegen den auch Persson Beitr. 356 f.).


sauel-, suuel-, suel-, sul- „Sonne“,                   woneben snen-, sun-, so da6 sich sau-,
       sH- als Wz., -el und -en als Stammbildungssuffixe ergeben. suel „schwelen,
       brennen‘‘      ist   wohl damit wesenseins,
     Gr. horn.      fjsXtog^     att.   fjXiog,   dor. deXiog^       aXiog^   kret. d^iXiog   Hes.   (d.   i.


dpeXiog) „Sonne“, Weiterbildung des n.            zum m. -m-St. (vgl. ai. sur-
ya-h)\ lat. so/, -is m. „Sonne“ (aus neutr. ^^aw^^xiber ^sauol^ *5aoZ; Mahlow
AEO. 32, Schulze KZ. 27, 428, Solmsen Stud. 68, KZfsS, 454; 44, 207
Anm. 1 trotz Kretschmer KZ. 31, 351, 452 m. Lit., Sommer Krit. Erl. 15f.;
             ;


ob die TJmwandlung zum Masc. nach Ehrlich Z. idg, Sprachgesch. 7 1 Anm. 1
durch den gr. Gotternamen ^HXiog bewirkt sei, ist allerdings mit Sommer
zu bezweifeln);             cymr. hatd^   acorn, hetml^ mcorn. heid, Jtoul^ bret. heol
.,Sonne“ {*savel^           s.   Pedersen KG. I 62; dazu vielleicht air. suit f. „Auge’*
aus    *srdi-y ablautgleich             mit ai. surah        aib. hid^ s. u.);
      saud n. {^sdtvila-\ anord. sol f. {^sdivula, nicht aus *5 (':[w]Z- nach
     got.
J. Schmidt KZ. 26, 9) „Sonne'', aisl. andsplis^ aschw. andsylis „der Sonne
zugewendet“ letzteres wohl nicht mit Ablaut           s. Trautmann Germ.
Lautges. 25).
   Unsicher die Eunennamen got. sugil (Salzburger Hdschr.), ags. sygil^ sigel
(g  aus w Oder einem Ubergangslaut j in der Mittelstufe             s. Sievers

PBrB. 6, 565 f., J. Schmidt KZ. 26, 9, Kluge Grdr.^ 380, van Helten IF.
18, 102 Anm. 1, und die Bedenken Jacobsohns KZ. 47, 91. Ficklll* 546
setzt urgerm. *sugila- an, abl. mit as. swigli „hell, strahlend“ aus *swegila-^
ags. sweg{e)l n. „Himmel, Sonne“, swegle „hell, strahlend^ aus "^swagila-;
Wood, Uhlenbeck PBrB. 30, 311, Lewy PBrB. 32, 149 leiten das g wenig-
stens aus Kreuzung mit letzterer Sippe her, deren
                                                          g gewifi nicht nach
Grienberger Ark. f. nord. fil, 15, 14 ebenfalls aus w zu deuten ist.
   Lit. lett. sdidc ,,Sonne“ (mit Schwund des 2. Yokals, Bezzenberger BB.
17, 224).
     Aksl.            „Sonne“ {xiisl.*szlnhce wohl durch Langdiphthongkurzung aus
*siil-ni- ;      n aus dem St.               alb. huf, ill „Stern“ (G. Meyer Wb. 460
                                            saus-, sus*                                        447

Gdf.     "^sulo-   Oder   "^suli-   nach Pedersen KZ. 36, 277, der ebdas. 286 f.               alb.
diel „Sonne“        als Entrwicklung aus       "^sueU zu rechtfertigen sucht)        ;
                                                                                         ai.   ved.
suvar n.      =
            av. hvard „Sonne, Licht, Himmel“, gen. surah       av, Jiuro, ai.=
surya- m. (vgl.         sura- m. „Sonne“; davon ai. sUrta- „helP‘ (s. Pers-
```


## [2026-09-14T01:36:19.871Z] TOOL CALL #96: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '29660,29700p' incoming/WLD/WLD_Bd2_pages.txt",
 "description": "WLD continuation p.447"
}
```


### [2026-09-14T01:36:19.927Z] TOOL RESULT

```
surya- m. (vgl.         sura- m. „Sonne“; davon ai. sUrta- „helP‘ (s. Pers-
son Beitr. 754 m. Lit.), ai. svdrnara- n. „Lichtglanz‘‘, av. x^arsnah-^ ap.
’farnah- „Euhmesglanz, Herrlichkeit“ (Bartholomae IP. 3, 170).
   Yom -ew-St. (vgl. Kretschmer KZ. 31,351, Pedersen KZ. 32, 256, Jo-
hansson BB. 18, 32fiF,):
   av. gen. x'fmg „Sonne'' (idg. *sz/c^-5, Bartholomae KZ. 28, 12; gegen
Zuruckfiihrung von gr. i]vo\^ etwa „funkelnd“ auf *suans-oyj s. Boisacq s. v.
m. Lit., auch Nachtr.; eine Gdf. *suen- wird durch ir. Fin-snecJita, Pick
II ^ 306 zw., nicht gestiitzt; fern bleiben auch mir. fcyrsunnud „Erleuchten“,
forosnaim „ich erleuchte“ Pick II ^ 306), got. sunno (dat. sunnin neutr.
nach sauil, s. Streitberg IP. 19, 391 ff.), ags. sunna, ahd. sunno^ sunna
„Sonne“ (nicht nach Schulze KZ. 27, 428 f, aus ^sulno), wozu als „sonn-
seitig == sudlich“, anord. sudr „Suden'‘, Adv. „sudwarts“, ags. suderra, as.
suthar-liiidi („Sudleute“), ahd. sundar „Suden'‘, Adv. „sudwarts“, mhd. sund
„Suden“ usw. (nhd. Sud aus dem Kd.), s. Brugmann IP. 18, 423 ff., Palk-
Torp u. syd (auch m. Lit. iiber abvreichende Deutungen, wozu Schroder
IP. 28, 29 f.: ags. stvlpi^a „dexteP‘, dt. gesund).


sans-, sus- „trocken, diirp^
   Ai. gosa- „trocken machend, ausdorrend, m. das Austrocknen, Verdorren,
Trockenheit''   (aus *som- iiber *sosa-, s. Meillet IF. 18, 420) == gr. avog
(Horn.) avog (att.) „durr, trocken^' (zum Spiritus             s.   Sommer gr. Lautst. 39 f.
m, liit.) ags. sear „trocken, verwelkt, unfruchtbap‘, mnd. sor „trocken, durr“
(soren „trocken machen, trocken werden^', ahd. soren „verdorren, verwelken'‘),
lit.   saiisas „trocken“, {saiistii, sansti „trocken werden‘‘), aksl. suchz „trocken“
(susiti„trocken machen“); gr. avaivco „trockne aus“, lit. sansinti „trocken
machen‘^ (Ubereinstimmung ohne geschichtlichen Zusammenhang); av. Jiaos-
„exarescere“, aiohaosemna- ,, nicht trocknend“, gr. avco „trockne, d6rre“;
avoTi]Q6g „herb, streng, sauert6pfisch“, avorakeog „schmutzig, struppig (eigent-
lich  von eingetrocknetem Schmutz rauh‘^;
   alb. '&ah ("^sausnio G. Meyer Alb. Wb. 88) „trockne“;
   ai. gusyati „trocknet, welkt hin“, lit.          susti „raudig werden“, lett.
sust „trocken werden“, aksl. SocJinqfi „ trocken werden^'; ai. cusJca-, av. huska-,
ap. usJca- „trocken“.
  Fiir lat. sudus „trocken, heiter (vom Wetter)    siidum „der klare Himmels-
raum, heiteres Wetter“, das man als suso-do-s angereiht hat (Lit. bei Vf.
LEWb.^ 753) ist Herleitung aus *suoidos (: lit. svideti „glanzen“; s. Falk-Torp
u. svide) vorzuziehen.
   Hieher auch gr.          avxu.6g^   avyjxy], avyuoii^g,   ^r]rog   „Trockenheit, Durre“,
avyjiYiQog „trocken“, avyyeo} „bin diirr, trocken, squaleo‘‘ (Lit. bei Boisacq
```


## [2026-09-14T01:37:02.294Z] TOOL CALL #97: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%81%D8%B1%DB%8C%D8%A8%D8%B1%D8%B2",
 "prompt": "Persian فریبرز (Fariborz): etymology, components (farr/fari + borz 'height, tall'), Avestan/Middle Persian antecedents."
}
```


### [2026-09-14T01:37:03.713Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T01:37:07.202Z] TOOL CALL #98: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('FSF_pages.txt').read()\npages=t.split('\\f')\nfor i in (99,165,176):\n    p=pages[i]\n    j=p.find('فریبرز')\n    print('leaf',i, repr(p[max(0,j-300):j+300]))\n    print('---')\nEOF",
 "description": "FSF Fariborz mentions"
}
```


### [2026-09-14T01:37:08.532Z] TOOL RESULT

```
leaf 99 '     \u202bبرج کمان\u202c\n                  \u202bبه واژة چرخ نگاهکنید\u202a:\u202c\u202c                                       \u202bبرجبره\u202c\n                                                               \u202bبه وا چرخ نگاه کنید\u202a:\u202c\u202c\n     \u202bچو خورشید از آن کوشش آگاه شد\u202c\n \u202bز برج کمان بر سر گاه شد\u202c                                  \u202bوزین رو فریبرز بر میسره\u202c\n\u202b\u200f)\u202a(VIY-OF-#\u202c\u202c                                 \u202bچو خورشید تابان به برج بره\u202c\n                                            \u202b\u200f)\u202aQFIY-YT-F\u202c\u202c\n                             \u202bبرج گاو\u202c\n             \u202bبه واژۀ چرخ نگاهکنید\u202a:\u202c\u202c                             \u202bبرج حمل (بهفتححا مویم)\u202c\n    \u202bچو خورشید '
---
leaf 165 'ردمی نیک هر سو بسی\u202c\n\u202bبیاموزی از ماکت آیسدبهبر\u202c\n                                            \u202bز پیوسته پیشم نبودی کسی\u202c\n      \u202bکی نامور دادشان زینهار\u202c\n                                            \u202b(\u202a)۲-۹۴-۵۳۷\u202c\u202c\n \u202bبدان تانهانی کنند آشکار\u202c\n       \u202bجو آزاد گشتند از بند اوی\u202c                                \u202bفریبرز کاوسشان پیشرو\u202c\n                                           \u202bکجا بود پیوستهة شاه نو\u202c\n\u202bبجستند ناچار پيوند اوی\u202c                      \u202b(\u202a)۴-۷۱-۶۴۱\u202c\u202c\n \u202b(\u202a)۱-۸۳-۱۴\u202c\u202c                                                   \u202b\u202a ۲\u202cجسییدی مجاور» متصل\u202a:\u202c\u202c\n\n               \u202bنبشتن به حسرو بیاموختند\u202c               '
---
leaf 176 '\u202c\u200f\u202c\n \u202b(\u202a)۱-۴۳۲-۱۵۴۱\u202c\u202c\n                                                                 \u202bرخ اعدات از تش نکبت\u202c\n               \u202bز نردیک گودرز کشواد تفت\u202c\n                                                \u202bس شیبهاه امد\u202c\n                                                           \u202bهمچو قير و\u202c\n \u202bسواری به نزد فریبرز رفت\u202c\n \u202b(\u202a)۴-۲۸۱۰-۳۷۰۱\u202c\u202c\n                                                                     \u202bشویر (بروزن تزویر \u202a-\u202cتازی)\u202c\n                                                                      \u202bشر مساری» شرمندگی\u202a:\u202c\u202c\n                         \u202b(اسدی \u202a:)۹۲۲-۸۶\u202c\u202c\n                 \u202bفوت\u202c\n           '
---
```


## [2026-09-14T01:37:20.937Z] TOOL CALL #99: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nmkdir -p data/verification/sources/refs/ocr/BOOK\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg432.png data/verification/sources/refs/ocr/BOOK/432.png\nls -la data/verification/sources/refs/ocr/BOOK/432.png\nhead -40 data/verification/page-385.json",
 "description": "Copy page image and view example output"
}
```


### [2026-09-14T01:37:21.020Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 92551 Sep 13 21:37 data/verification/sources/refs/ocr/BOOK/432.png
{
  "pdf_page": 385,
  "book_page": 355,
  "verified_by": "claude-opus-5",
  "verified_on": "2026-09-07",
  "entries": [
    {
      "entry": 0,
      "root": "Peg",
      "verdict": "plausible",
      "modern_form": "PIE *peg- / *pōg-, *pōk-s- 'armpit, hip, loin, side' (Pokorny 792); Watkins/AHD lists the same root as *peg- 'breast'",
      "note": "Pokorny 792 prints the headword as '(peg-:) pog-: pōg-, pōk-s-' and glosses it 'Achsel, Hufte, Lende, Seite' (armpit, hip, loin, side) — the full-grade *peg- is only a bracketed, inferred variant. Nourai's headword 'Peg' with the gloss 'breast' is copied verbatim from the AHD (Watkins) appendix, which prints 'peg-. Breast.' The 'breast' sense in fact rests only on Latin pectus and Tocharian A pässäṃ / B pāścane 'the two breasts'; Sanskrit pakṣa- and Latvian paksis point to 'side, flank'. Modern scholarship (de Vaan via Wiktionary) further doubts that Lat. pectus and Skt. pakṣa- belong together at all. Root is real and the language label is right; the gloss is a one-sided simplification.",
      "note_fa": "ریشهٔ هندواروپایی آغازین که نورایی آن را Peg با معنای «سینه» آورده، در فرهنگ پوکورنی (ص ۷۹۲) با سرواژهٔ «(peg-:) pog-: pōg-, pōk-s-» و معنای «زیربغل، ران، پهلو» ثبت شده است؛ صورت *peg- تنها گونه‌ای بازسازی‌شده و درون‌کمانک است. معنای «سینه» را نورایی از پیوست ریشه‌های هندواروپایی فرهنگ AHD (واتکینز) گرفته که همان‌جا «Breast» نوشته است، ولی این معنا فقط بر پایهٔ pectus لاتین و pāścane تخاری است، حال آنکه pakṣa- سنسکریت و paksis لتونیایی بر معنای «پهلو، سو» دلالت دارند. افزون بر این، پژوهش امروزی (دِ ڤان، به نقل ویکی‌واژه) در پیوند pectus لاتین با pakṣa- سنسکریت تردید می‌کند. پس: ریشه واقعی است و برچسب زبانی درست، اما معنای داده‌شده یک‌سویه و ساده‌سازانه است — ادعای نورایی با احتیاط پذیرفتنی است.",
      "sources": [
        "https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%95%E0%A5%8D%E0%A4%B7",
        "https://en.wiktionary.org/wiki/pectus"
      ],
      "ref_check": [
        {
          "ref": "POK:792",
          "status": "partial",
          "note": "Pokorny IEW p.792 (local POK_03.txt, form-feed leaf 25) reads: '(peg-:) pog-: pōg-, pŏk-s- \"Achsel, Hufte, Lende, Seite\". Ai. pákṣa- m. \"Schulter, Flugel\" und \"Seitenpfosten\", pákṣas- n. \"Seite\"; lat. pectus \"Brust\"; lett. paksis \"Hausecke\"; toch. A pässäṃ, B päścane \"die beiden Bruste\" ... WP. II 3 f., WH. II 270.' The page number is exact; the gloss is not 'breast'."
        }
      ],
      "consulted": [
        {
          "src": "AHD",
          "where": "Watkins 1985, s.v. peg-",
          "stance": "supports",
          "note": "'peg-. Breast. 1. Suffixed variant form *pek-tos- in Latin pectus, breast: PECTORAL; EXPECTORATE, PARAPET. 2. Possibly suffixed variant form *pek-so- in Sanskrit paksah, wing: PUNKA. [Pok. (peg-), pog- 792.]' — this is verbatim Nourai's chart (grep '^peg-' AHD_watkins1985.txt line 820)."
        },
        {
          "src": "WLD",
          "where": "Walde-Pokorny II 3-4 (WLD_Bd2_pages.txt leaf 8)",
          "stance": "partial",
          "note": "Entry headed 'pag-' (their spelling) with 'ai. pajasyá- n. Bauchgegend, Weichen, russ. pachu \"Leistengegend\", pacha \"Achselhohle\" ... ein io-St. *pagio- in cech. paze \"Arm\"' — again 'flank/armpit', no 'breast'."
        },
        {
          "src": "IEC",
          "where": "Mann, alphabetical",
```


## [2026-09-14T01:45:10.482Z] TOOL CALL #100: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-432.json <<'JSONEOF'\n{\n  \"pdf_page\": 432,\n  \"book_page\": 402,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Sâwel, Sŭ 3\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *sóh₂wl̥ / *seh₂wel- ~ *sh₂un- 'sun' (older notation *sāwel-, *sāwol-, *su̯el-, *sūl-, beside *su̯en-, *sun-)\",\n      \"note\": \"Pokorny IEW 881-882 heads the entry 'sāwel-, sāwol-, su̯el-, sul-' with the meaning 'Sonne' and adds the note that su̯en-, sun- stand beside it. Walde-Pokorny II 446 states the analysis Nourai's double headword reflects: 'sāuel-, su̯uel-, su̯el-, sul- \\\"Sonne\\\", woneben su̯en-, sun-, so daß sich sāu-, sū- als Wz., -el und -en als Stammbildungssuffixe ergeben' — i.e. sāu-/sū- is the root and -el/-en are suffixes, exactly Nourai's 'Sâwel, Sŭ'. Watkins/AHD prints 'sāwel-. Also s(u)wel-, su(ə)el-, su(ə)en-, sun-. The sun.' Language label 'Indo-European' and gloss 'sun' are both right; the modern laryngealist form is *sóh₂wl̥ (Wiktionary), an ablauting heteroclite whose weak stem gives Av. hūrō, Skt. sūraḥ.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *seh₂wel- / *sóh₂wl̥ «خورشید» است که در نگارش کهن‌تر (پوکورنی، ص ۸۸۱ تا ۸۸۲) به‌صورت *sāwel-, *sāwol-, *su̯el-, *sūl- و در کنار آن *su̯en-, *sun- آمده است. والده-پوکورنی (جلد ۲ ص ۴۴۶) همان تحلیلی را می‌دهد که سرواژهٔ دوگانهٔ نورایی بر آن استوار است: sāu-/sū- ریشه است و -el و -en پسوندهای ستاک‌ساز؛ پس «Sâwel، Sŭ» درست است. این ستاک از نوع ناهمگون (heteroclite) با تناوب آوایی است و ستاک ضعیف آن به hūrō اوستایی و sūraḥ سنسکریت می‌انجامد. برچسب زبانی و معنای «خورشید» هر دو درست است؛ ادعای نورایی دربارهٔ خودِ ریشه درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/seh%E2%82%82wel-\",\n        \"https://www.etymonline.com/word/sun\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:881\",\n          \"status\": \"supports\",\n          \"note\": \"Pokorny, IEW, Page(s): 881-882: 'Root/lemma: sāwel- sāwol- su̯uel-, su̯el-, sul-, Meaning: sun. Note: next to which su̯en-, sun-, thus of old n/n-stem'. Found in POK_full.txt at line 71617 ff. (grep -n 'sauel-'); the entry closes 'References: WP. II 446 f., WH. II 553 f. … Page(s): 881-882'. Exactly the page Nourai cites and exactly his headword.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Walde-Pokorny, Bd. II pp. 446-447 (WLD_Bd2_pages.txt, line 29615)\",\n          \"stance\": \"supports\",\n          \"note\": \"'sāuel-, su̯uel-, su̯el-, sul- „Sonne“, woneben su̯en-, sun-, so daß sich sāu-, sū- als Wz., -el und -en als Stammbildungssuffixe ergeben.' Followed by 'ai. ved. suvar n. = av. hvarə „Sonne, Licht, Himmel“, gen. surah = av. hūrō'.\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985, s.v. sāwel- (AHD_watkins1985.txt line 905)\",\n          \"stance\": \"supports\",\n          \"note\": \"'sāwel-. Also s(u)wel-, su(ə)el-, su(ə)en-, sun-. The sun. Contracted from *saəwel- … [Pok. sāwel- 881.]'\"\n        },\n        {\n          \"src\": \"SYN\",\n          \"where\": \"Buck, A Dictionary of Selected Indo-European Synonyms, §1.52 SUN (SYN.txt line 1661)\",\n          \"stance\": \"supports\",\n          \"note\": \"'Nearly all the usual words for \\\"sun\\\" belong to a single inherited group. 1. IE *sāwel-, etc., a group with vowel gradation, parallel l- and n- forms … Walde-P. 2.446.' The word list gives 'Av. hvarə, gen. hūrō and xᵛə̄ṇg', Lat. sol, Goth. sauil, sunnō, OE sunne, sunna, NE sun.\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"Mann, An Indo-European Comparative Dictionary, p. ~1113-1114 (IEC.txt line 15035, leaf 616)\",\n          \"stance\": \"supports\",\n          \"note\": \"'saul-, sāuel- \\\"sun\\\". WP II, 446. (Indo-Iran. variant: sūl-) Skt. cf. (z-gde) sūraḥ, m. id.; Av. cf. hūrō, gs. of hvarə, id.; Oss. cf. xur, Dig. xor, id.; … Gk. helios …; Lat. sol …; Go. sauil, n., OE sōl …'\"\n        },\n        {\n          \"src\": \"KLN\",\n          \"where\": \"Klein 1966, pp. 1468-1469 s.v. 'Sol, n., the sun' (KLN_1966.txt leaf 779)\",\n          \"stance\": \"supports\",\n          \"note\": \"'Sol, n., the sun. — L. sol (prob. fr. *sāwel-, through *sāwol-, *swōl-), cogn. with OI. sūryaḥ, sūraḥ, Avestic hvarə (with r for l) … All these words derive fr. I.-E. base *sāwel-, *sūl-, which are -l-enlargements of base *sāu-, *su-, \\\"to shine; sun\\\".'\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"hvare, xvar 1\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan huuarə- / xᵛarə- (nom.-acc. sg. neuter huuarə, gen. sg. hūrō) 'sun; light, sky' is the regular Iranian continuation of PIE *sóh₂wl̥ (Indo-Iranian *súHar, cf. Vedic svàr / sū́ar 'sun, light, heaven'). PIE initial *s- became Proto-Iranian *h- (Av. h-, spelt hu̯- / xᵛ- before the u̯-glide, so huuarə and xᵛarə are two orthographies of one word, not two words), and the *-l- of the *-el- suffix became *-r- in Indo-Iranian, giving the neuter r/n-heteroclite huuarə / gen. xᵛə̄ṇg beside the weak stem hū- in hūrō. Nourai's gloss 'sun, light' is precisely Walde-Pokorny's 'Sonne, Licht, Himmel'. The node is the correct Iranian branch off the root box.\",\n          \"derivation_fa\": \"واژهٔ اوستایی huuarə- / xᵛarə- (فاعلی huuarə، اضافی hūrō) به معنای «خورشید، روشنایی، آسمان» بازماندهٔ مستقیم *sóh₂wl̥ هندواروپایی آغازین است؛ در هندوایرانی *súHar (مقایسه کنید با svàr سنسکریت). «س» آغازین هندواروپایی در ایرانی باستان به «ه» بدل شده و پیش از غلت u̯ به‌صورت hu̯-/xᵛ- نوشته می‌شود؛ پس huuarə و xᵛarə دو املای یک واژه‌اند، نه دو واژه. لام پسوند *-el در هندوایرانی به «ر» بدل شده و ستاکی ناهمگون (r/n) پدید آورده است: huuarə در برابر xᵛə̄ṇg اضافی و ستاک ضعیف hū- در hūrō. معنایی که نورایی داده («خورشید، روشنایی») همان است که والده-پوکورنی می‌دهد. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/seh%E2%82%82wel-\"],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:881\",\n              \"status\": \"supports\",\n              \"note\": \"POK 881: 'Old Indic ved. suvar = (zero grade) Avestan hvarə \\\"sun, light, sky\\\". Gen. surah = Av. huro. … Avestan: OAv. huuarə[n] (< *huuar) \\\"sun\\\" (gen.sg. xᵛə̄ṇg < *huuanh); LAv. huuarə (gen.sg. hū < *huuanh, next to hurō = Ved. sūras)' (POK_full.txt lines 71624-71634).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Bartholomae, Altiranisches Wörterbuch, s.v. hvar- / hvarə.xšaēta- (BRT.txt lines 3220, 4752, 11915)\",\n              \"stance\": \"supports\",\n              \"note\": \"OCR is poor but the word is repeatedly cited in context with its German gloss 'die Sonne': 'yeδi sī hvarə nōit uzuxšyeiti … \\\"wenn (erst) die Sonne nicht mehr aufgeht\\\" Yt. 6.3'; 'yat hvarə raoxšne tāpayeiti Yt. 6.1' (of sun and moon 'Wärme bringen').\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Walde-Pokorny II 447\",\n              \"stance\": \"supports\",\n              \"note\": \"'ai. ved. suvar n. = av. hvarə „Sonne, Licht, Himmel“, gen. surah = av. hūrō, ai. sūrya- m.' — the gloss 'Sonne, Licht' is Nourai's 'sun, light'.\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck §1.52\",\n              \"stance\": \"supports\",\n              \"note\": \"word list: 'Av. hvarə, gen. hūrō and xᵛə̄ṇg' under 'SUN'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"hŭr 2 «هور»; xor «خور»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian خور xor and هور hur/hōr both continue Middle Persian xwar 'sun' (Pahlavi spelling hwl), itself from Av. xᵛarə- / gen. hū-. The doublet arises because Middle Persian xw- before a is variously simplified: in the normal line of descent xwar > NP xor (the w of the labialised x is lost), while the by-form with initial h- (hur, hōr) reflects the weak stem hū-/hur- (Av. hūrō, Vedic sūraḥ) and is confined to poetry; Ferdowsī rhymes hur with gur. Mo'in's footnote in Borhan-e Qate' expressly cross-refers هور to خور and to the Avestan form. Both glosses ('sun'; 'sun, star') are attested — Mo'in's lexicon gives هور as (اخ.) 'خورشید، آفتاب' and (اِ.) 'ستاره'.\",\n          \"derivation_fa\": \"«خور» و «هور» هر دو از فارسی میانهٔ xwar «خورشید» (نوشتار پهلوی hwl) می‌آیند که خود بازماندهٔ xᵛarə- اوستایی است. دوگانگی صورت از آنجاست که در فارسی نو «خو» ی فارسی میانه پیش از آ/ـَ ساده می‌شود و xwar به «خور» می‌رسد، در حالی که صورت «هور» بازتاب ستاک ضعیف hū-/hur- (مقایسه: hūrō اوستایی، sūraḥ سنسکریت) است و بیشتر کاربرد شعری دارد؛ فردوسی «هور» را با «گور» قافیه کرده است. معین در حاشیهٔ برهان قاطع «هور» را به «خور» ارجاع می‌دهد و صورت اوستایی را می‌آورد. معنای «خورشید» و «ستاره» هر دو در فرهنگ معین ثبت است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%B1%D8%B4%DB%8C%D8%AF\"],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:2389\",\n              \"status\": \"supports\",\n              \"note\": \"Borhan-e Qate' ed. Mo'in, printed p. 2389 (vol. 4 scan, pdf page 472; the running head reads ۲۳۸۹): 'هور — بضم اول و سکون ثانی مجهول و رای قرشت، نامی است از نامهای آفتاب عالمتاب' with Mo'in's footnote 10 'خور (ه.م.). اوستا hvarə …' and the very verse Nourai prints: 'که شیری نترسد ز یک دشت گور / ستاره نتابد هزاران چو هور — فردوسی طوسی'.\"\n            },\n            {\n              \"ref\": \"MON:5220\",\n              \"status\": \"partial\",\n              \"note\": \"The six-volume Mo'in is not online and its pagination cannot be checked; in the two-volume Adena condensation (MON_part2.txt line 92214) the entry reads 'هور (اخ.) خورشید، آفتاب. (اِ.) ستاره (مطلقاً). به کردار (مانند) هور: درخشان مانند آفتاب' — the headword, both senses ('sun' and 'star') and the gloss are exactly Nourai's, but the page number 5220 could not be verified.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn, Grundriss der neupersischen Etymologie, no. 505, p. 111 (HRN.txt leaf 132)\",\n              \"stance\": \"supports\",\n              \"note\": \"'505. xᵛar \\\"Sonne\\\", hur, hōr (reimt auf gūr; Šāhn. III, 1105 Vers 693), Xurāsān.' and on p. 112 'aw. hvar-; phlv. vgl. xᵛar[āsān] bezw. xᵛar[varān]; ai. svar. kurd. xor, hūr …; oss. d. xor, t. xūr'.\"\n            },\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, A Concise Pahlavi Dictionary, p. 95 s.v. xwar (PHD.txt line 663)\",\n              \"stance\": \"supports\",\n              \"note\": \"'¹xwar [hwl | M xwr, N ~] sun; cal. 11th day.' MacKenzie explicitly uses this word in his introduction as the standard example: 'hwl represents xwar \\\"sun\\\"'.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"Mo'in (2-vol. Adena), s.v. هور and s.v. هورخش\",\n              \"stance\": \"supports\",\n              \"note\": \"'هورخش [= هورخشید] خورشید، آفتاب، هور' (MON_part1.txt line 9748) confirms hur as the living Persian word for the sun.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"hŭr-bân «هوربان»\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The chart's chain starts from a Persian compound hūr-bān 'sun-guard' = hūr 'sun' + -bān, the productive Persian agent/guard suffix (MP -pān, as in bāqbān, darbān, dīdbān). The formation is morphologically impeccable, but the word itself is not attested: Nourai's own NOTE says it is not in Mo'in, and it is likewise absent from Borhan-e Qate' (no هوربان in the ه section of vol. 4), from Mo'in's two-volume lexicon and from Richardson-Johnson. It is a reconstruction proposed by Addi Shir (and before him by the author of Borhan-e Qate', who took the word to be Syriac) to explain Arabic ḥirbāʾ, not an independently recorded Persian word; the real Persian word for the chameleon is آفتاب‌پرست āftāb-parast 'sun-worshipper', as Nourai himself notes. Since the node exists only to carry an etymology that modern Arabists reject (see node 4), it must be marked disputed: the arrow hūr → hūrbān is plausible in form but the target word is a ghost.\",\n          \"derivation_fa\": \"زنجیرهٔ نمودار از ترکیب فرضی «هوربان» آغاز می‌شود: «هور» (خورشید) + پسوند «ـبان» (نگهبان؛ از فارسی میانهٔ -pān، مانند باغبان، دربان، دیدبان). ساخت واژه از نظر صرفی بی‌عیب است، اما خودِ واژه در هیچ فرهنگ معتبری ثبت نشده؛ خود نورایی در یادداشت نمودار می‌نویسد که در فرهنگ معین یافت نشد، و ما نیز آن را در برهان قاطع (بخش «ه» جلد چهارم)، در فرهنگ معین دوجلدی و در فرهنگ ریچاردسون نیافتیم. «هوربان» ساختهٔ أدّی شیر (و پیش از او صاحب برهان قاطع که واژه را سریانی می‌دانست) برای توضیح «حرباء» عربی است، نه واژه‌ای مستقل در فارسی؛ نام فارسی آفتاب‌پرست برای این جانور «آفتاب‌پرست» است، چنان‌که خود نورایی هم آورده. پژوهش امروزی این پیوند را نمی‌پذیرد و ما این گره را «مورد اختلاف» می‌شماریم.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AD%D8%B1%D8%A8%D8%A7%D8%A1\"],\n          \"ref_check\": [\n            {\n              \"ref\": \"AFM:50\",\n              \"status\": \"supports\",\n              \"note\": \"Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba, chapter ḥāʾ/khāʾ (AFM_pages.txt leaf 51, printed page ≈ 43-50; the page numerals are not OCR-readable, but باب الدال begins at leaf 60 ≈ p.52, so this is the page Nourai means): '…ومؤلف البرهان القاطع يقول ان الكلمة سريانية الاصل … ولكن [الظاهر ان] اللفظة مركبة من [خور/هور] اي الشمس ومن بان اي حافظ ومترقب' — 'the word is compounded of [hūr] \\\"sun\\\" and bān \\\"guard, watcher\\\"'. This is precisely Nourai's arrow, so the reference does say what the chart says.\"\n            },\n            {\n              \"ref\": \"FVF:189\",\n              \"status\": \"not_checked\",\n              \"note\": \"Emam Shushtari, Farhang-e vāžehā-ye fārsi dar zabān-e ʿarabi: no local copy, no accessible scan (noorlib page-viewer needs a browser, ketabnak needs a login); refs_online.json records local_file: null.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BQT\",\n              \"where\": \"Borhan-e Qate', vol. 4 (ه section), OCR text\",\n              \"stance\": \"silent\",\n              \"note\": \"grep 'هوربان' / 'هور بان' over incoming/BQT/BQT_v4_pages.txt returns nothing; the ه entries around هور (printed p. 2389) list هور, هوده, هودر, هودل but no هوربان.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"Mo'in, 2-vol. condensation\",\n              \"stance\": \"silent\",\n              \"note\": \"No هوربان; the Persian name of the animal is آفتاب‌پرست, and Mo'in's entry for حرباء simply glosses it 'آفتاب پرست' (MON_part1.txt line 52896).\"\n            },\n            {\n              \"src\": \"RCH\",\n              \"where\": \"Richardson-Johnson, A Dictionary Persian, Arabic and English\",\n              \"stance\": \"silent\",\n              \"note\": \"grep -i 'hurban' gives only 'hurbang, a noxious weed growing among wheat' and Arabic 'churbany, a collar' — no hūr-bān 'chameleon'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Arabic\",\n          \"words\": \"horbâ «حُرباء»\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Arabic ḥirbāʾ حِرباء 'chameleon' (pl. ḥarābī) is claimed here as an Arabicisation of Persian hūr-bān, with -bān rendered by the Arabic -āʾ ending of the pattern fiʿlāʾ. Modern scholarship prefers a native Semitic explanation: the word is built on the Arabic root ḥ-r-b, most probably from ḥarba حَرْبة 'dart, javelin' (with reference to the chameleon's projectile tongue), or from the same root in the sense 'to become enraged' (the colour change being idiomatic for changing moods); Akkadian and Eblaite cognates are cited. Al-Jawālīqī's al-Muʿarrab does not list ḥirbāʾ among the Arabicised words at all, and its editor Aḥmad M. Shākir devotes a footnote to rebutting exactly Addi Shir's hūr+bān proposal: 'the origin of the word ḥirbāʾ is Arabic … the root is pure Arabic, so what is the evidence that the word is foreign? … The author of Kitāb al-Alfāẓ al-fārisiyya relates that the author of Borhān-e Qāṭeʿ held the word to be Syriac … then that it is compounded of hūr and bān meaning \\\"guard who watches\\\"; so he said — but is this not rashness in declaring ḥirbāʾ non-Arabic?!' The Persian etymology survives as a minority hypothesis, so the arrow is disputed rather than simply wrong.\",\n          \"derivation_fa\": \"واژهٔ عربی «حِرباء» (جمع: حَرابیّ) در این نمودار معرّبِ «هوربان» فارسی دانسته شده و پسوند «ـبان» به وزن «فِعلاء» عربی بازسازی شده است. اما پژوهش امروزی ریشه‌ای سامی را ترجیح می‌دهد: واژه بر ریشهٔ عربی ح-ر-ب ساخته شده، به احتمال زیاد از «حَربة» (زوبین، نیزهٔ کوچک) به سبب زبان پرتابی آفتاب‌پرست، یا از همان ریشه به معنای «خشمگین شدن» (دگرگونی رنگ کنایه از دگرگونی حال است)؛ هم‌ریشه‌های اکدی و اِبلایی نیز یاد شده‌اند. جوالیقی در «المعرّب» این واژه را در شمار معرّبات نیاورده و مصحّح آن، احمد محمد شاکر، در پانوشت صریحاً پیشنهاد أدّی شیر (هور + بان) را رد می‌کند و می‌نویسد اصل واژه عربی خالص است. بنابراین این پیوند «مورد اختلاف» است، هرچند فرضیهٔ فارسی هنوز به‌عنوان نظری اقلیت نقل می‌شود.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AD%D8%B1%D8%A8%D8%A7%D8%A1\"],\n          \"ref_check\": [\n            {\n              \"ref\": \"AFM:50\",\n              \"status\": \"supports\",\n              \"note\": \"Same Addi Shir page as node 3 (AFM_pages.txt leaf 51): after describing the animal that turns toward الشمس 'the sun' and changes colour, he reports Borhan's Syriac derivation and then proposes 'اللفظة مركبة من [هور] … ومن بان اي حافظ ومترقب'. The reference does support Nourai's arrow; it is the reference, not the chart, that modern Arabists reject.\"\n            },\n            {\n              \"ref\": \"FVF:189\",\n              \"status\": \"not_checked\",\n              \"note\": \"Emam Shushtari is not accessible (see node 3).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"ARB\",\n              \"where\": \"al-Jawālīqī, al-Muʿarrab, ed. A. M. Shākir, editor's footnotes (ARB_mo3rb.txt lines 9876-9881)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'وأصل كلمة \\\"حرباء\\\" عربي … والمادة أصلها عربي خالص، فما الدليل على عجمة الكلمة؟ … نقل صاحب كتاب الألفاظ الفارسية أن مؤلف البرهان القاطع ذهب إلى أن الكلمة سريانية الأصل، ثم … أن اللفظة مركبة من \\\"هور\\\" و\\\"بان\\\" أي حافظ يترقب، هكذا قال، ولكن أليس هذا من الجزم بأن كلمة \\\"حرباء\\\" غير عربية؟!'\"\n            },\n            {\n              \"src\": \"PLA\",\n              \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen\",\n              \"stance\": \"silent\",\n              \"note\": \"grep for 'hirbā', 'ḥirbā' and 'Chamäleon' over PLA_asbaghi_1988_ia_djvu.txt returns nothing: Asbaghi does not count ḥirbāʾ among the Persian loans in Arabic.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein, s.v. chameleon\",\n              \"stance\": \"silent\",\n              \"note\": \"Klein derives English chameleon from Greek khamailéōn 'ground lion'; no Semitic or Iranian word is involved, so he offers no support for the Arabic-Persian link either way.\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"herbâ «حربا»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian حربا herbā 'chameleon' is a straightforward Arabic loan: Arabic ḥirbāʾ حِرباء was taken into Persian with the usual loss of the final hamza of the fiʿlāʾ pattern (cf. صحرا ṣaḥrā, حمرا ḥamrā) and the usual shift of the Arabic i-vowel to Persian e. Mo'in marks it '[ع.]' (Arabic) and glosses it آفتاب‌پرست. Whether or not the Arabic word was itself originally Persian (nodes 3-4), this final leg of the chain — Arabic into Persian — is certain; if Nourai's round trip were right it would be a Persian-Arabic-Persian doublet of the (unattested) hūr-bān, but in the modern view it is simply a loan from a native Arabic word.\",\n          \"derivation_fa\": \"«حربا» در فارسی وام‌واژه‌ای عربی است: «حِرباء» عربی با افتادن همزهٔ پایانی وزن «فِعلاء» (مانند صحرا، حمرا) و تبدیل کسرهٔ عربی به «ـِ» فارسی وارد فارسی شده است. معین آن را با نشانهٔ [ع.] (عربی) آورده و به «آفتاب‌پرست» معنی کرده است. این حلقهٔ پایانی زنجیره — از عربی به فارسی — قطعی است؛ اگر چرخهٔ فارسی ← عربی ← فارسیِ نورایی درست می‌بود، «حربا» دوگانهٔ «هوربان» به شمار می‌رفت، اما بنا بر دیدگاه امروزی صرفاً وام‌گیری از واژه‌ای اصیلاً عربی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AD%D8%B1%D8%A8%D8%A7%D8%A1\"],\n          \"ref_check\": [\n            {\n              \"ref\": \"MON:1347\",\n              \"status\": \"partial\",\n              \"note\": \"The six-volume Mo'in cannot be paginated online; in the two-volume condensation (MON_part1.txt line 52896) the entry is 'حرباء: [ع. ف. حربا] (اِ.) (جانورشناسی) آفتاب پرست.' — headword, Arabic origin tag and Persian form حربا are exactly as charted, but page 1347 itself is unverifiable.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"Mo'in (2-vol.), s.v. حرباء\",\n              \"stance\": \"supports\",\n              \"note\": \"'حرباء [ع. ف. حربا] (اِ.) (جانو.) آفتاب پرست' — tagged ع. = Arabic, with حربا given as the Persian shape.\"\n            },\n            {\n              \"src\": \"ARB\",\n              \"where\": \"al-Jawālīqī / Shākir footnote (ARB_mo3rb.txt line 9876)\",\n              \"stance\": \"partial\",\n              \"note\": \"Confirms that ḥirbāʾ is the Arabic word (and argues it is native Arabic), which is all this node needs for the Arabic > Persian direction.\"\n            },\n            {\n              \"src\": \"AFM\",\n              \"where\": \"Addi Shir, ḥāʾ/khāʾ chapter\",\n              \"stance\": \"partial\",\n              \"note\": \"Records the Arabic word and its chameleon sense; his Persian etymology bears on nodes 3-4, not on this borrowing.\"\n            }\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Avestan\",\n          \"words\": \"hvare-xšaeta; hvare-âsân; hvare-varân\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Only the first of the three compounds is genuinely Avestan. (a) huuarə.xšaēta- 'the shining/radiant sun' is a well-attested Younger Avestan epithet (Yt. 6.0, Y. 22.24, Ny. 1), xšaēta- being the verbal adjective of xšay- 'to shine, rule' (Nourai's cross-reference 'Ksei 2'); Bartholomae cites 'hvarə.xšaētahe … raoδahe Yt. 6.0'. (b) 'hvare-âsân' and (c) 'hvare-varân' are NOT Avestan words: they are Middle Persian compounds, xwarāsān 'sunrise, east' (xwar + āsān, participial stem of the Parthian/MP verb ās- 'to come, rise') and xwarōfrān / xwarwarān 'sunset, west' (xwar + the stem of bar-/war- 'to carry, bear away' — hence Nourai's cross-reference 'Bher 1'), both listed as Middle Persian by MacKenzie. Horn too gives them only as Pahlavi ('phlv. vgl. xᵛar[āsān] bezw. xᵛar[varān]'). The derivations and the glosses are right; the language label 'Avestan' is wrong for two of the three words, which is why the node is plausible rather than confirmed.\",\n          \"derivation_fa\": \"از سه ترکیب این گره تنها نخستین آن‌ها به‌راستی اوستایی است. الف) huuarə.xšaēta- «خورشیدِ درخشان» صفتی است در اوستای نو (یشت ۶ بند ۰، یسنا ۲۲ بند ۲۴)، که xšaēta- صفت فعلی ریشهٔ xšay- «درخشیدن، فرمان راندن» است. ب و ج) اما «hvare-âsân» و «hvare-varân» واژه‌های اوستایی نیستند، بلکه ترکیب‌های فارسی میانه‌اند: xwarāsān «برآمدن خورشید، خاور/مشرق» (xwar + ās- «آمدن، برآمدن») و xwarōfrān / xwarwarān «فروشدن خورشید، باختر/مغرب» (xwar + ستاک bar-/war- «بردن»). مکنزی هر دو را پهلوی می‌داند و هرن نیز آن‌ها را تنها به‌عنوان صورت‌های پهلوی می‌آورد. پس اشتقاق و معنا درست است ولی برچسب زبانیِ دو واژه از سه واژه نادرست است؛ از این رو این گره «با احتیاط پذیرفتنی» است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%B1%D8%B4%DB%8C%D8%AF\", \"https://en.wiktionary.org/wiki/%D8%AE%D8%B1%D8%A7%D8%B3%D8%A7%D9%86\"],\n          \"ref_check\": [\n            {\n              \"ref\": \"HRN:111\",\n              \"status\": \"supports\",\n              \"note\": \"Horn, Grundriss p. 111-112 (HRN.txt leaves 132-133): no. 505 'xᵛar \\\"Sonne\\\", hur, hōr …, Xurāsān. — aw. hvar-; phlv. vgl. xᵛar[āsān] bezw. xᵛar[varān]; ai. svar.' and no. 506 'xᵛuršēd \\\"Sonne\\\". aw. hvarə.xšaētəm \\\"strahlende Sonne\\\"; phlv. xᵛaršēt bezw. xuršēt, auch xᵛarxšēt.' Horn is the exact source of the three compounds — and he labels āsān/varān as Pahlavi, not Avestan.\"\n            },\n            {\n              \"ref\": \"POK:881\",\n              \"status\": \"partial\",\n              \"note\": \"Pokorny 881 has Av. huuarə and xᵛə̄ṇg but none of the three compounds; he is silent on hvarə.xšaēta-.\"\n            },\n            {\n              \"ref\": \"KLN:1469\",\n              \"status\": \"partial\",\n              \"note\": \"Klein 1966 pp. 1468-1469 is the spread 'socle | solder'; the relevant entry there is 'Sol, n., the sun. — L. sol … cogn. with … Avestic hvarə (with r for l) … I.-E. base *sāwel-, *sūl-'. So the page is correctly cited for the root and for Avestan hvarə, but Klein says nothing about the compounds hvarə-xšaēta / -āsān / -varān.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Bartholomae, AirWb., s.v. aurvat.aspa- and hvarə.xšaēta- (BRT.txt lines 4752, 5566, 10701)\",\n              \"stance\": \"partial\",\n              \"note\": \"'hvarə.xšaētahe … raδahe Yt. 6.0, Y. 22.24' and 'hvarəxšaētəm … Yt. 6.1, 6, 12.34, 13.81, Y. 16.4' — the Avestan compound is genuine; Bartholomae has no entry *hvarə-āsān- or *hvarə-varan-.\"\n            },\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, Concise Pahlavi Dictionary pp. 95-96\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'xwarāsān [hwlʾsnʾ | M xwrʾsʾn, N ~] sunrise, east'; 'xwarōfrān [hwl(ʾ)wplʾnʾ | M xwrwprʾn] sunset, west'; 'xwarwarān [hwlwlʾnʾ, -blʾnʾ] = xwarōfrān'; 'xwar(x)šēd [hwl(h)šytʾ | M xwrxšyd, N xuršēd] sun'. All three are Middle Persian, and only xwar(x)šēd is said to go back to an Avestan compound.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg, Manual of Pahlavi II\",\n              \"stance\": \"supports\",\n              \"note\": \"Nyberg's glossary likewise treats xᵛaršēt/xᵛarxšēt as the Pahlavi reflex of Av. hvarə.xšaēta-.\"\n            }\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Persian\",\n          \"words\": \"xoršîd «خورشید»; xorâsân «خراسان»; xâvar[ân] «خاور ، خاوران»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three are the regular New Persian outcomes of the Middle Persian compounds of node 6. (a) خورشید xoršid < MP xwar(x)šēd (Pahlavi hwl(h)šytʾ, Manichaean xwrxšyd) < Av. huuarə.xšaēta-: the Avestan -xšaēta- gives MP -xšēd (Av. -ai- > MP -ē-), and the cluster -rxš- is simplified to -rš- in most MP spellings, whence NP -šid with the regular MP ē > NP ī. Mo'in's footnote in Borhan (p. 786) analyses it 'از خور (آفتاب) + شید … اوستا hvara xshaeta، پهلوی xwaršēt'. (b) خراسان Khorāsān < MP xwarāsān 'sunrise, east'; Mo'in's footnote at Borhan p. 723 gives 'در پهلوی xwarāsān (مشرق)' and quotes Fakhr-al-Dīn Gorgānī's famous folk-etymological couplet, which Nourai reproduces. (c) خاور xāvar / خاوران xāvarān < MP xwarwarān 'sunset, west', with -rw- > -w- and intervocalic lenition giving xāvar; Mo'in's footnote at Borhan p. 708 states 'خاور بازماندهٔ کلمهٔ پهلوی خوربران یا خوروران است، به معنی مغرب'. Note the later reversal: Nourai's gloss 'west' is the original meaning, but in modern Persian خاور has come to mean 'east' (Wiktionary: 'from Middle Persian xwarwarān, originally meaning west'), a shift Mo'in's footnote explicitly complains about.\",\n          \"derivation_fa\": \"هر سه واژه بازماندهٔ منظم ترکیب‌های فارسی میانهٔ گره پیشین‌اند. الف) «خورشید» از xwar(x)šēd فارسی میانه (املای پهلوی hwl(h)šytʾ) و آن از huuarə.xšaēta- اوستایی؛ «ـَ ای» اوستایی در فارسی میانه به «ē» و سپس در فارسی نو به «ی» بدل شده و خوشهٔ -rxš- به -rš- ساده شده است. معین در حاشیهٔ برهان (ص ۷۸۶) می‌نویسد: «از خور (آفتاب) + شید، اوستا hvara xshaeta، پهلوی xwaršēt». ب) «خراسان» از xwarāsān پهلوی «مشرق»؛ حاشیهٔ برهان ص ۷۲۳ همین را می‌آورد و بیت فخرالدین گرگانی («خراسان آن بود کزوی خورآسد») را — همان بیتی که نورایی نقل کرده — گواه می‌گیرد. ج) «خاور/خاوران» از xwarwarān پهلوی «مغرب»؛ حاشیهٔ برهان ص ۷۰۸: «خاور بازماندهٔ کلمهٔ پهلوی خوربران یا خوروران است … به معنی مغرب». نکته آنکه معنای «باختر/مغرب» کهن است و در فارسی امروز «خاور» به معنای «مشرق» به کار می‌رود؛ این تحول معنایی وارونه را معین نیز نادرست شمرده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%B1%D8%B4%DB%8C%D8%AF\",\n            \"https://en.wiktionary.org/wiki/%D8%AE%D8%B1%D8%A7%D8%B3%D8%A7%D9%86\",\n            \"https://en.wiktionary.org/wiki/%D8%AE%D8%A7%D9%88%D8%B1\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:723\",\n              \"status\": \"supports\",\n              \"note\": \"Borhan-e Qate' ed. Mo'in, printed p. 723 (BQT_v2_pages.txt leaf 181; the running head shows ۷۲۳): 'خراسان — بفتح اول، بمعنی مشرق است که در مقابل مغرب باشد، و نام ولایتی هم هست مشهور … چون آن ولایت در مشرق … واقع است بنابراین بدین نام خوانده‌اند.' Footnote 1: 'در پهلوی xwarāsān (مشرق) «مینا …»' followed by the four verses 'زبان پهلوی هر که شناسد / خراسان آن بود کزوی خورآسد', the very couplet on Nourai's chart. The page supports خراسان; خورشید and خاور are on other pages (786 and 708).\"\n            },\n            {\n              \"ref\": \"MON:1395\",\n              \"status\": \"partial\",\n              \"note\": \"Not verifiable: the six-volume Mo'in is not online and its pagination cannot be mapped. The two-volume condensation does carry خورشید and خاور with the expected senses, but page 1395 itself could not be checked.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BQT\",\n              \"where\": \"Borhan-e Qate', printed p. 786 (BQT_v2_pages.txt leaf 246) and p. 708 (leaf 168)\",\n              \"stance\": \"supports\",\n              \"note\": \"p. 786: 'خورشید — بضم اول و واو معدوله، از خور (آفتاب) + شید … اوستا hvara xshaeta، پهلوی xwaršēt (به معنی آفتاب) درخشان'. p. 708, footnote 1: 'خاور بازماندهٔ کلمهٔ پهلوی «خوربران» یا «خوروران» … مغرب است و مشرق را «خوراسان» می‌گفتند … هرن گوید: خاوران (خاور + ان) (مغرب) از خاور (مغرب) مشتق است.'\"\n            },\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie pp. 95-96\",\n              \"stance\": \"supports\",\n              \"note\": \"xwarāsān 'sunrise, east'; xwarwarān = xwarōfrān 'sunset, west'; xwar(x)šēd 'sun' with 'N xuršēd' given as the New Persian outcome.\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn nos. 505-506, pp. 111-112\",\n              \"stance\": \"supports\",\n              \"note\": \"'505 … Xurāsān'; '506 xᵛuršēd \\\"Sonne\\\". aw. hvarə.xšaētəm \\\"strahlende Sonne\\\"; phlv. xᵛaršēt bezw. xuršēt.'\"\n            }\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Persian\",\n          \"words\": \"no-hŭr «نُهور»; bad-nohŭr «بد نُهور»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian نهور nohūr / nuhūr is a compound of the old preverb ni- 'down, at' (Av. ni-, MP ni-, as in ni-gāh 'look', ni-šastan 'to sit down') with the weak stem hūr- of the word for 'sun, light' (node 2), giving literally 'looking-at, gaze' from 'sunlight, sight'; Mann's Indo-European Comparative Dictionary lists it under the root itself: 'sūl- (2) (variant of type sāuel-, sāul-) \\\"sun, light, eye\\\" … Per. cf. nu-hūr, s. \\\"eye, sight, look, scowl\\\" (fr. *ni-ˣ)', beside Irish súil 'eye' from the same root — a semantic pair ('sun' > 'eye') that Pokorny's Celtic note makes explicit ('the sun is viewed as the eye of the sky'). The compound بدنهور bad-nohūr is transparent: bad 'bad' + nohūr 'look, appearance' = 'ill-looking, ugly', and Mo'in glosses it exactly so ('ظ. بدنهور به معنی بدمنظر است'). Sanā'ī's line quoted on the chart is the locus classicus.\",\n          \"derivation_fa\": \"«نُهور» ترکیبی است از پیشوند کهن ni- «فرو، به‌سوی» (اوستایی ni-، فارسی میانه ni-، مانند نگاه، نشستن) با ستاک ضعیف hūr- از همان واژهٔ «خورشید/روشنایی» (گرهٔ ۲)؛ معنای نخستین آن «روشنایی خورشید» و سپس «نگاه، دیده» است. مان (Mann) در فرهنگ تطبیقی هندواروپایی، ذیل ریشهٔ sūl- (گونه‌ای از sāuel-) با معنای «خورشید، روشنایی، چشم» می‌آورد: «فارسی nu-hūr «چشم، دید، نگاه، نگاه خشم‌آلود» از *ni-» و در کنار آن súil ایرلندی «چشم» را می‌نهد؛ این تحول معنایی «خورشید ← چشم» را پوکورنی نیز توضیح می‌دهد («خورشید چشمِ آسمان انگاشته می‌شد»). «بدنهور» نیز آشکارا «بد + نهور» یعنی «بدمنظر، زشت‌رو» است و معین در حاشیهٔ برهان همین را می‌نویسد. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"IEC:1334\",\n              \"status\": \"supports\",\n              \"note\": \"Mann, An Indo-European Comparative Dictionary, p. 1334 (IEC.txt leaf 734, which carries the page numerals 1333/1334): 'sūl- (2) (variant of type sāuel-, sāul-) \\\"sun, light, eye\\\". Skt. sūraḥ, m. \\\"sun\\\" beside sūryaḥ, id.; Oss. xur, Dig. xor, id.; Per. cf. nu-hūr, s. \\\"eye, sight, look, scowl\\\" (fr. *ni-ˣ); Scyth. cf. oitó-suros …; Ir. súil, gs: súla, f. \\\"eye, look\\\".' Exactly Nourai's claim, on exactly the page he cites.\"\n            },\n            {\n              \"ref\": \"BQT:2220\",\n              \"status\": \"partial\",\n              \"note\": \"Borhan-e Qate' ed. Mo'in, printed p. 2220 (vol. 4 scan, pdf page 303): 'نهور — بضم اول و واو مجهول بروزن حور، نگاه کردن از روی قهر و غضب و خشم باشد؛ و بمعنی نگاه و چشم هم بنظر آمده است که بعربی رؤیت … گویند.' Mo'in's footnote 2 quotes Sanā'ī's 'ازان با بزرگان نیارم نشستن / که ایشان چو حورند و من بدنهورم' (the verse Nourai prints) and adds 'ظ. بدنهور به معنی بدمنظر است'. The page confirms word, senses and quotation but gives no etymology — for the derivation from the sun-root only IEC:1334 speaks.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"Mo'in (2-vol.), s.v. نهور (MON_part2.txt line 81576)\",\n              \"stance\": \"supports\",\n              \"note\": \"'نهور. (قد.) (اِ.) نگاه به چشم.' — marked قدیمی (archaic), glossed 'gaze of the eye', matching Nourai's 'sight, eye'.\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"Pokorny 881\",\n              \"stance\": \"partial\",\n              \"note\": \"Pokorny has the 'eye' branch of the root (OIr. súil 'eye' from *sūli-, Alb. hyll 'star') with the note 'The change of meaning in OIr. is understandable from the mythological context: \\\"sun\\\" is viewed as \\\"the eye of the sky\\\"' — the semantic bridge Nourai's node needs, though Pokorny does not mention the Persian word.\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn, Grundriss\",\n              \"stance\": \"silent\",\n              \"note\": \"No entry for نهور; Horn's no. 505 covers only xᵛar, hur, hōr, Xurāsān.\"\n            }\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Avestan\",\n          \"words\": \"hvarenah, xvarenah, farnah; farnavant\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Avestan xᵛarənah- n. 'glory, majesty, the divine fortune' is a genuine derivative of the sun-word: an -nah- (*-nas-) abstract to the same *su̯el-/*su̯ar- base, semantically 'radiance' > 'the shining glory that legitimises kings'. Walde-Pokorny II 447 lists it directly under the root: 'ai. svàrṇara- n. \\\"Lichtglanz\\\", av. xᵛarənah-, ap. -farnah- \\\"Ruhmesglanz, Herrlichkeit\\\"', and Pokorny 881 repeats it. The reservation is one of language labels: the f- forms farnah- and farnavant- are NOT Avestan but Old Persian / Median, where Proto-Iranian *hu̯- regularly gives f- (Old Persian Vinda-farnah 'Intaphernes', *Fra-farnah, Bага-farna); the corresponding Avestan forms are xᵛarənah- and xᵛarənaŋᵛhant- (cf. the attested Avestan compounds barō.xᵛarənah-, vīspō.xᵛarənah-, duš-xᵛarənah- in Bartholomae). Nourai puts all four under one 'Avestan' box, which blurs the Avestan/Old-Persian dialect split that is precisely what explains the Persian farr. Root, meaning and the derivation itself are right; the labelling is loose.\",\n          \"derivation_fa\": \"«xᵛarənah-» اوستایی به معنای «فرّ، شکوه، بخت ایزدی» به‌راستی مشتقی از همان واژهٔ خورشید است: اسم معنی با پسوند -nah- (از *-nas-) بر همان ستاک، با تحول معنایی «درخشش» ← «فرّ ایزدی که پادشاه را مشروع می‌کند». والده-پوکورنی (ج ۲ ص ۴۴۷) آن را زیر همین ریشه می‌آورد: «av. xᵛarənah-، ap. -farnah- «درخشش نام‌آوری، شکوه»». اما نکته‌ای در برچسب زبانی هست: صورت‌های farnah- و farnavant- اوستایی نیستند بلکه پارسی باستان/مادی‌اند، زیرا *hu̯- ایرانی باستان در پارسی باستان به f- بدل می‌شود (مانند Vinda-farnah در کتیبه‌ها)؛ صورت اوستایی xᵛarənah- و xᵛarənaŋᵛhant- است. نورایی هر چهار صورت را در یک خانهٔ «اوستایی» گذاشته و همین تمایز گویشی را که کلید توضیح «فرّ» فارسی است پنهان کرده است. اشتقاق و معنا درست است ولی برچسب زبانی دقیق نیست؛ با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D9%81%D8%B1\"],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:881\",\n              \"status\": \"supports\",\n              \"note\": \"POK 881: 'Old Indic svàrṇara- m. \\\"bright space, ether\\\", Avestan xᵛarənah-, ap. -farnah- \\\"shining fame, magnificence\\\"' (POK_full.txt line 71630).\"\n            },\n            {\n              \"ref\": \"BQT:1451\",\n              \"status\": \"supports\",\n              \"note\": \"Borhan-e Qate' ed. Mo'in, printed p. 1451 (vol. 3 scan, pdf page 244 per BQT_v3_pagemap.json), s.v. فرّخ, footnote 9: 'در پهلوی farrux (تابان، مجلل، پرتوافکن، زیبا، خوشبخت)، ایرانی باستان *farnahvant-, از *hvarnahvant-, قس فارسی: فرخنده «نیبرگ ص ۷۶» ورک: استق - هوبشمان ۸۰۸.' This is exactly Nourai's 'farnavant', and Mo'in derives it from *hvarnahvant- just as the chart derives it from hvarenah.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Walde-Pokorny II 447 (WLD_Bd2_pages.txt line 29661)\",\n              \"stance\": \"supports\",\n              \"note\": \"'ai. svàrṇara- n. „Lichtglanz“, av. xᵛarənah-, ap. -farnah- „Ruhmesglanz, Herrlichkeit“ (Bartholomae IF. 3, 170).'\"\n            },\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Bartholomae, AirWb., compounds in -xᵛarənah- (BRT.txt lines 16952, 24037, 24544, 27051)\",\n              \"stance\": \"partial\",\n              \"note\": \"'barō.xᵛarənah- Adj. \\\"der Hoheit, Herrlichkeit besitzt, gewinnt\\\"'; 'vīspō.xᵛarənah- Adj. \\\"der alle Hoheit, Herrlichkeit besitzt\\\"'; 'vīδat.xᵛarənah- m. EN.' — the Avestan stem is xᵛarənah-; Bartholomae has no Avestan *farnah-, which is the Old Persian/Median shape.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg, Manual of Pahlavi II, s.v. xᵛarrah and duš-xᵛarr(ah) (NYB_vol2_glossary.txt lines 4343, 1409)\",\n              \"stance\": \"supports\",\n              \"note\": \"'xᵛarrah [GDH] a divine essence, a special form of the Eternal Light, a splendour, a glory'; 'duš-xᵛarr(ah) … — Av. duš-xᵛarənah- \\\"ill-famed\\\"'. Confirms the Avestan stem and its Pahlavi continuation.\"\n            }\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"Sogdian\",\n          \"words\": \"frn\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sogdian frn (Manichaean and Christian script), read farn, 'glory, majesty, fortune' is the Sogdian cognate of Av. xᵛarənah-, showing the same *hu̯- > f- development as Old Persian/Median farnah- (Sogdian regularly has f- here, cf. the personal names Δēnē-farn, Oska-farn, and the compounds prnxwnd(ʾ)k farnxund 'fortunate' < *farnah-wantaka-). Gharib's Sogdian Dictionary entry 3914 states the derivation in so many words. Nourai's gloss 'elegance' is a loose rendering of 'glory, majesty'.\",\n          \"derivation_fa\": \"واژهٔ سغدی frn (در خط مانوی و مسیحی)، خوانده farn، به معنای «فرّ، شکوه، بخت» هم‌ریشهٔ xᵛarənah- اوستایی است و همان تحول *hu̯- ← f- را نشان می‌دهد که در پارسی باستان/مادی farnah- دیده می‌شود؛ سغدی در این واژه همیشه f- دارد (مقایسه: نام‌های Δēnē-farn و Oska-farn، و ترکیب prnxwntk farnxund «خوش‌بخت» از *farnah-wantaka-). قریب در فرهنگ سغدی خود (مدخل ۳۹۱۴) همین اشتقاق را می‌دهد. معادلی که نورایی آورده («elegance») برگردانِ آزادِ «شکوه، فرّ» است. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"SOD:155\",\n              \"status\": \"supports\",\n              \"note\": \"Gharib, Sogdian Dictionary, printed p. 155 (SOD_pages.txt leaf 220, which carries the numeral 155), entry 3914: 'frn M, C — farn ©<Av. xᵛarənah OP *farna ©ob. ~y ⇒prnʾ, fn — glory, majesty, fortune. GMS 526; W-Li, ii; BBB; Tales. 470.50; BSTi 189'. Exactly the page and exactly the claim.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"SOD\",\n              \"where\": \"Gharib, entries 3915-3920 and the index (SOD_pages.txt leaves 220, and lines 14456, 16508)\",\n              \"stance\": \"supports\",\n              \"note\": \"'3915 frnpry — farnβare … glorious, fortunate'; 'frnxwndy(y) — farnxunde (prnywnδy) ©<Av. xᵛarənahvant' — the whole family confirms farn < xᵛarənah-.\"\n            },\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Bartholomae, AirWb. s.v. xᵛarənah-\",\n              \"stance\": \"supports\",\n              \"note\": \"Gives the Avestan source-word ('Hoheit, Herrlichkeit') from which the Sogdian form is taken.\"\n            },\n            {\n              \"src\": \"HENNING\",\n              \"where\": \"Henning, Selected Papers (referenced by Gharib as GMS 526 / BBB)\",\n              \"stance\": \"supports\",\n              \"note\": \"Gharib's citations for frn are to Gershevitch's Grammar of Manichean Sogdian §526 and Henning's BBB, the standard treatments of the word.\"\n            }\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"Persian\",\n          \"words\": \"farr «فرّ»; farrox «فرّخ»; Farîborz «فریبرز»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"(a) فرّ farr 'glory, splendour' continues Middle Persian farr(ah) (written with the Aramaic ideogram GDE and read xwarrah in the inherited South-West form) from Old Persian/Median *farnah-, the f-variant of Av. xᵛarənah-; the Persian doublet خرّه/خوره xurra/xwarra is the genuinely South-West Persian reflex of the same word, and Mo'in's footnote at Borhan p. 1443 spells this out. Derivatives فرّه farra, فرّهی farrahī, فرهمند farrahmand are formed on it with the Persian suffixes -a, -ī, -mand. (b) فرّخ farrox 'blessed, fortunate' < MP farrox < Old Iranian *farnah-want- 'possessing farnah' (the -want- suffix regularly gives MP -ox/-oy in this word); فرخنده farroxunda/farxonda is a further participial extension. (c) فریبرز Farīborz, the Shahnameh hero, is traditionally analysed as fari- (the far(r)- element) + borz 'height, stature' (Av. bərəz-, Nourai's cross-reference 'Bhergh'), hence 'of glorious stature' — this is the reading of the Persian lexicographic tradition that Nourai follows, but the name is not attested in Avestan or Middle Persian and some onomasticists connect the first element instead with Av. friya- 'dear'; it is therefore plausible rather than certain, and the node takes that verdict. The other proper names on the chart (فرزاد، فرشاد، فرشید، فرناز، فردوست) are modern or Shahnameh compounds on the same farr-.\",\n          \"derivation_fa\": \"الف) «فرّ» بازماندهٔ farr(ah) فارسی میانه است (در پهلوی با هزوارش GDE نوشته و xwarrah خوانده می‌شود) و آن از *farnah- پارسی باستان/مادی، گونهٔ f-دار xᵛarənah- اوستایی؛ دوگانهٔ آن در فارسی «خرّه/خوره» است که بازتاب جنوب‌غربیِ اصیل همان واژه است — معین در حاشیهٔ برهان (ص ۱۴۴۳) صریحاً همین را می‌نویسد. مشتقات «فرّه، فرّهی، فرهمند» با پسوندهای فارسی ساخته شده‌اند. ب) «فرّخ» از farrox فارسی میانه و آن از *farnah-want- ایرانی باستان «دارندهٔ فرّ»؛ «فرخنده» گسترشی دیگر بر همان پایه است. ج) «فریبرز» را سنّت فرهنگ‌نویسی فارسی «فری (فرّ) + برز (بلندی، قامت)» یعنی «بلندبالای فرهمند» می‌خواند و نورایی همین را آورده؛ ولی این نام در اوستا و فارسی میانه گواهی نشده و برخی نام‌شناسان جزء نخست را با friya- اوستایی «دوست‌داشتنی» می‌سنجند. از این رو جزء سوم «با احتیاط پذیرفتنی» است و حکم کلی گره نیز همان. دیگر نام‌های نمودار (فرزاد، فرشاد، فرشید، فرناز، فردوست) ترکیب‌های نو یا شاهنامه‌ای بر همین «فرّ»اند.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D9%81%D8%B1\"],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:1443\",\n              \"status\": \"supports\",\n              \"note\": \"Borhan-e Qate' ed. Mo'in, printed p. 1443 (vol. 3 scan, pdf page 236 per the page-map), s.v. فرّ, Mo'in's footnote 3: 'غالباً حرف دوم آن مشدد است. فرّ = خرّه (هم.)، قس خورنه (معرب: خورنق)؛ پارسی باستان -farnah (در حالت فاعلی، اصل: xᵛarenah)، Vindafarneh، ارمنی pʼarkʼ، پازند xvareh، فارسی خوره، فرّ، فرّخ، فرخنده، فرّه، فرّهی از همین ریشه است.'\"\n            },\n            {\n              \"ref\": \"BQT:1451\",\n              \"status\": \"supports\",\n              \"note\": \"Same volume, printed p. 1451 (pdf 244), s.v. فرّخ, footnote 9: 'در پهلوی farrux (تابان، مجلل، پرتوافکن، زیبا، خوشبخت)، ایرانی باستان *farnahvant-, از *hvarnahvant-, قس فارسی فرخنده.'\"\n            },\n            {\n              \"ref\": \"BQT:789\",\n              \"status\": \"supports\",\n              \"note\": \"Borhan-e Qate', printed pp. 788-789 (BQT_v2_pages.txt leaf 248), s.v. خوره: 'نوری است از جانب خدای تعالی که … بر خلایق فائز می‌شود' with Mo'in's footnote 'این معنی نیز مأخوذ از معنی خوره (فر) است … ورک: خره' — the xwarra/farr identity the chart needs.\"\n            },\n            {\n              \"ref\": \"BQT:180\",\n              \"status\": \"not_found\",\n              \"note\": \"Printed p. 180 of vol. 1 falls in the انگ…/او… stretch of the alphabet (BQT_v1_pages.txt leaf ≈ 397; leaf 394 carries the catch-line 'بقیه از صفحهٔ ۱۷۵'). Nothing on or near that page bears on farr, farrox or Farīborz. Either the citation is a slip or it points to a page of a different printing.\"\n            },\n            {\n              \"ref\": \"FSF:250\",\n              \"status\": \"not_found\",\n              \"note\": \"The available scan of Noushin's Vāže-nāmak is a different printing: its فرّ/فره entry stands on printed p. 334 (FSF_pages.txt leaf 337), not 250. The entry itself does support the chart — it quotes Pourdavoud: 'دو لغت مصطلح فارسی که فر و خره باشد، اولی نزدیک است به لهجهٔ فرس هخامنشی [فرناه] و دومی به لهجهٔ اوستایی' and glosses فر as 'فروغ، نور، موهبتی که اهورامزدا به کسی که شایستهٔ آن است [می‌دهد]' — but the cited page number cannot be confirmed.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, Concise Pahlavi Dictionary pp. 32 and 96 (PHD.txt lines 325, 665)\",\n              \"stance\": \"supports\",\n              \"note\": \"'farr-, v. xwarrah'; 'farrox [plhwʾ | M prwx, N ~] fortunate, blessed, happy. ~īh: fortune, joy, happiness'; 'xwarrah [GDE | (M prh, N farr)] fortune, glory, splendour'. MacKenzie gives NP farr and farrox as the direct outcomes.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg, Manual of Pahlavi II, glossary and NP index (NYB_vol2_glossary.txt lines 4343, 7133)\",\n              \"stance\": \"supports\",\n              \"note\": \"Index of New Persian forms: 'farrah: xᵛarrah … farrux: farraxu'; main entry 'xᵛarrah [GDH] a divine essence, a special form of the Eternal Light, a splendour, a glory'.\"\n            },\n            {\n              \"src\": \"FSF\",\n              \"where\": \"Noushin, Vāže-nāmak, printed p. 334 (FSF_pages.txt leaf 337)\",\n              \"stance\": \"supports\",\n              \"note\": \"Quotes Pourdavoud (Yashthā II 313-314) that فر and خره are the Achaemenid-Persian and the Avestan shapes of one word, and glosses فر 'فروغ، نور، موهبتی که اهورامزدا … به کسی که شایستهٔ آن [است می‌بخشد]'.\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn, Grundriss\",\n              \"stance\": \"partial\",\n              \"note\": \"Horn has no. 505 for xᵛar/hur but treats farr under xᵛarrah elsewhere; his p. 111 is silent on farr, so this node rests on Mo'in, MacKenzie and Nyberg.\"\n            }\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"Avestan\",\n          \"words\": \"xvang\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"The form is real but the gloss is wrong: Avestan xᵛə̄ṇg (transliterated xᵛǝ̄ṇg / xvang) means 'of the sun' — it is the genitive singular of huuarə- built on the n-stem *su̯en-s-, and it is precisely the form that links the Iranian word to Germanic *sunnōn- and to English sun. Pokorny 881 has 'gen.sg. xᵛə̄ṇg < *huuanh' and again 'In -en-stem: Avestan xᵛə̄ṇg \\\"the sun\\\" (Indo-Germanic *su̯en-s), Gen. from hvarə'; Walde-Pokorny II 447 'av. gen. xᵛə̄ṇg \\\"Sonne\\\" (idg. *su̯en-s)'; Buck §1.52 lists 'Av. hvarə, gen. hūrō and xᵛə̄ṇg' under SUN; Klein s.v. sun writes 'cogn. with Avestic xᵛə̄ṇg (for *swen-s), \\\"of the sun\\\"'. No source knows an Avestan word xᵛang 'son' (Av. for 'son' is puθra-). The printed page 402 of the book really does read 'xvang : son', so this is Nourai's own misprint (or a slip for 'sun'), faithfully carried into the JSON — not an extraction error. Two further points: as a case-form rather than a derivative, xᵛə̄ṇg should hang under the Avestan node 1 rather than directly under the root box; and the printed chart shows an empty box to its right, with no language label and no words, which the extraction (correctly) did not turn into a node.\",\n          \"derivation_fa\": \"صورت واژه درست است اما معنای آن نادرست: xᵛə̄ṇg اوستایی «از آنِ خورشید» است، یعنی حالت اضافیِ مفردِ huuarə- که بر ستاک -n- از *su̯en-s ساخته شده، و همین صورت است که واژهٔ ایرانی را به *sunnōn- ژرمنی و sun انگلیسی پیوند می‌دهد. پوکورنی (ص ۸۸۱) می‌نویسد: «xᵛə̄ṇg اوستایی «خورشید» (هندواروپایی *su̯en-s)، اضافی از hvarə»؛ والده-پوکورنی (ج ۲ ص ۴۴۷) و باک (بند ۱.۵۲) و کلاین (ذیل sun) نیز همین را می‌گویند. هیچ منبعی واژهٔ اوستایی xᵛang به معنای «پسر» نمی‌شناسد؛ «پسر» در اوستایی puθra- است. صفحهٔ چاپی ۴۰۲ کتاب به‌راستی «xvang : son» دارد، پس این خطای چاپی خودِ نورایی است (یا لغزش قلم به‌جای sun) و خطای خوانش اسکن نیست. دو نکتهٔ دیگر: چون این صورت صرفی است نه واژه‌ای مشتق، باید ذیل گرهٔ اوستاییِ شمارهٔ ۱ می‌آمد نه مستقیماً زیر خانهٔ ریشه؛ و در صفحهٔ چاپی کنار آن کادری تهی و بی‌برچسب دیده می‌شود که استخراج به‌درستی آن را گره نشمرده است.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"xvang : son\",\n          \"correct_form\": \"xᵛə̄ṇg 'sun' (gen. sg. of Av. huuarə- 'sun')\",\n          \"sources\": [\"https://www.etymonline.com/word/sun\"],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:881\",\n              \"status\": \"contradicts\",\n              \"note\": \"POK 881-882: 'OAv. huuarə[n] (< *huuar) \\\"sun\\\" (gen.sg. xᵛə̄ṇg < *huuanh)' and '2. In -en-stem: Avestan xᵛə̄ṇg \\\"the sun\\\" (Indo-Germanic *su̯en-s), Gen. from hvarə, Gothic sunnō …'. The page Nourai cites says the word means 'sun', not 'son'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Walde-Pokorny II 447 (WLD_Bd2_pages.txt line 29664)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'Vom -en-St.: av. gen. xᵛə̄ṇg „Sonne“ (idg. *su̯en-s, Bartholomae KZ. 28, 12) …, got. sunnō …, ags. sunna, ahd. sunno, sunna „Sonne“.'\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein, s.v. sun (KLN_1971.txt line 236741)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'These words are -n-enlargements of I.-E. base *sāu-, *su-, \\\"to shine; sun\\\", and cogn. with Avestic xᵛə̄ṇg (for *swen-s), \\\"of the sun\\\", xᵛanvant, \\\"sunny\\\".'\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck §1.52 SUN\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'Av. hvarə, gen. hūrō and xᵛə̄ṇg' — listed in the column of words meaning 'sun'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"Germanic\",\n          \"words\": \"sunnôn\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *sunnōn- (weak feminine n-stem) 'sun' continues the n-stem variant *sh₂un- / *su̯en- of the root, the same formation as Avestan xᵛə̄ṇg (node 12). The Germanic doublet is instructive: the old l-stem survives as Gothic sauil, Old Norse sól (whence Danish/Swedish sol), while the n-stem gives Gothic sunnō, Old English sunne/sunna, Old High German sunna, Old Saxon sunna, Dutch zon, German Sonne. Watkins/AHD reconstructs the form exactly as Nourai writes it, 'Germanic *sunnōn-'.\",\n          \"derivation_fa\": \"ستاکِ ژرمنی آغازین *sunnōn- (اسم مؤنث ستاک -n) «خورشید» بازماندهٔ گونهٔ n-دارِ ریشه یعنی *sh₂un-/*su̯en- است — همان ساختی که xᵛə̄ṇg اوستایی (گرهٔ ۱۲) نشان می‌دهد. در ژرمنی هر دو ستاک بازمانده‌اند: ستاک کهنِ l-دار در sauil گوتی و sól نورس کهن، و ستاک n-دار در sunnō گوتی، sunne/sunna انگلیسی کهن، sunna آلمانی علیای کهن و Sonne آلمانی. واتکینز در پیوست AHD همین صورت را دقیقاً به شکل «Germanic *sunnōn-» بازسازی کرده است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/sun\"],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"Watkins 1985 s.v. sāwel-: '1. Variant forms *swen-, *sun- in: a. Germanic *sunnōn- in Old English sunne, sun: SUN.' (AHD_watkins1985.txt line 905) — Nourai's node reproduces the reconstruction letter for letter.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"Pokorny 882\",\n              \"stance\": \"supports\",\n              \"note\": \"'Gothic sunnō (Dat. sunnin, neutr. after sauil), Old English sunna, Old High German sunno, sunna \\\"sun\\\".'\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein, s.v. sun\",\n              \"stance\": \"supports\",\n              \"note\": \"'ME. sonne, fr. OE. sunne, rel. to ON., OS., OHG. sunna, MDu. sonne, Du. zon, MHG., G. sonne, \\\"sun\\\", Goth. sunnō.'\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Walde-Pokorny II 447\",\n              \"stance\": \"supports\",\n              \"note\": \"'got. sunnō (dat. sunnin neutr. nach sauil, s. Streitberg IF. 19, 391 ff.), ags. sunna, ahd. sunno, sunna „Sonne“.'\"\n            }\n          ]\n        },\n        {\n          \"id\": 14,\n          \"lang\": \"English\",\n          \"words\": \"sun, Sunday, south\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three English words come from the Germanic n-stem of node 13. sun < Middle English sonne < Old English sunne (feminine until the 16th century) < PGmc *sunnōn-. Sunday < Old English sunnandæg, a Germanic loan-translation of Latin diēs Sōlis, itself a calque of Greek hēmérā Hēlíou — the seven-day planetary week reached the Germanic peoples through the Roman provinces in the 4th century. south < Old English sūþ < PGmc *sunþaz, literally 'sun-side': in the northern hemisphere the midday sun stands in the south, and the same formation gives Old Norse suðr, Old Saxon sūthar-liudi 'southern people', Old High German sundar; Old French sud and Spanish sur/sud are Germanic loanwords. Watkins derives all three from *sāwel- in one paragraph.\",\n          \"derivation_fa\": \"هر سه واژهٔ انگلیسی از همان ستاک n-دارِ ژرمنی (گرهٔ ۱۳) می‌آیند. sun از انگلیسی میانهٔ sonne و انگلیسی کهن sunne (که تا سدهٔ شانزدهم مؤنث بود). Sunday از sunnandæg انگلیسی کهن، گَرته‌برداری ژرمنی از diēs Sōlis لاتین که خود گرته‌برداری از hēmérā Hēlíou یونانی است؛ هفتهٔ هفت‌روزهٔ سیاره‌ای در سدهٔ چهارم میلادی از راه استان‌های رومی به ژرمن‌ها رسید. south از sūþ انگلیسی کهن و *sunþaz ژرمنی به معنای تحت‌اللفظی «سمتِ خورشید»: در نیم‌کرهٔ شمالی خورشیدِ نیم‌روز در جنوب است؛ همین ساخت در suðr نورس کهن و sundar آلمانی علیای کهن دیده می‌شود، و sud فرانسوی و sur/sud اسپانیایی وام‌واژه‌های ژرمنی‌اند. واتکینز هر سه را در یک بند از *sāwel- می‌گیرد. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/sun\", \"https://www.etymonline.com/word/south\"],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"The node carries no reference of its own on the chart; it inherits AHD from the Germanic parent node, which does cover all three English words.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. sāwel-\",\n              \"stance\": \"supports\",\n              \"note\": \"'a. Germanic *sunnōn- in Old English sunne, sun: SUN; b. Germanic compound *sunnōn-dagaz, \\\"day of the sun\\\" (translation of Latin diēs sōlis), in Old English sunnandæg, Sunday: SUNDAY; c. Germanic derivative *sunthaz, \\\"sun-side\\\", south, in Old English sūth, south, and sūtherne, southern: SOUTH, SOUTHERN.'\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein, s.vv. sun, Sunday\",\n              \"stance\": \"supports\",\n              \"note\": \"'Sunday, n. — ME. sonnedai, fr. OE. sunnandæg, \\\"sun's day\\\", prop. a loan translation of L. Solis dies, itself a loan translation of Gk. Hēlíou hēmérā, lit. \\\"day of the sun\\\".'\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat, Concise Etymological Dictionary, s.vv. sun, south\",\n              \"stance\": \"supports\",\n              \"note\": \"Skeat likewise takes OE sūð as a derivative of the sun-word and OE sunnandæg as a rendering of dies solis.\"\n            }\n          ]\n        },\n        {\n          \"id\": 15,\n          \"lang\": \"Latin\",\n          \"words\": \"sôl\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin sōl, sōlis m. 'sun' continues the l-stem of the root. Walde-Pokorny and Klein both derive it from the neuter *sāwel through *sāwol / *sāol with contraction of the intervocalic -w-, the original neuter having been remade as a masculine consonant stem (possibly under the influence of the Greek god's name Hḗlios). Cognates on the same l-stem are Gothic sauil, Old Norse sól, Welsh haul, Lithuanian saulė and Greek hēlios (< *sāwelios). Its derivatives are the source of English sol, solstice (sōl + -stitium 'a standing'), solar, parasol, girasol and turnsole.\",\n          \"derivation_fa\": \"«sōl، sōlis» لاتین «خورشید» بازماندهٔ ستاک l-دارِ ریشه است. والده-پوکورنی و کلاین هر دو آن را از صورت خنثای *sāwel از راه *sāwol و *sāol با ادغام واکهٔ میانی می‌گیرند؛ اسم خنثای کهن سپس به اسم مذکرِ ستاک صامتی بدل شده (شاید به تأثیر نام خدای یونانی Hḗlios). هم‌ریشه‌های همین ستاک: sauil گوتی، sól نورس کهن، haul ولزی، saulė لیتوانیایی و hēlios یونانی (از *sāwelios). مشتقات آن سرچشمهٔ واژه‌های انگلیسی sol، solstice (sōl + -stitium «ایستادن»)، solar، parasol و turnsole‌اند. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/sun\"],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"Watkins 1985 s.v. sāwel-: '2. Variant form *s(ə)wol- in: a. Latin sōl, the sun: SOL, SOLAR, SOLARIUM; GIRASOL, INSOLATE, PARASOL, SOLANINE, TURNSOLE; b. Latin compound sōlstitium, \\\"a standing of the sun\\\", solstice.'\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"Pokorny 881\",\n              \"stance\": \"supports\",\n              \"note\": \"'Latin sōl, -lis m. \\\"sun\\\" (from neutr. *sāwel about *sāwol, *sāol)'.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 pp. 1468-1469, s.v. Sol\",\n              \"stance\": \"supports\",\n              \"note\": \"'Sol, n., the sun. — L. sōl (prob. fr. *sāwel-, through *sāwol-, *swōl-), cogn. with OI. sūryaḥ, sūraḥ, Avestic hvarə …'\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Walde-Pokorny II 446\",\n              \"stance\": \"supports\",\n              \"note\": \"'lat. sōl, -is m. „Sonne“ (aus neutr. *sāwel über *sāwol, *sāol; Mahlow AEO. 32, Schulze KZ. 27, 428 …)'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 16,\n          \"lang\": \"English\",\n          \"words\": \"solar\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English solar 'of the sun' is a mid-15th-century learned borrowing of Latin sōlāris 'of or pertaining to the sun', a late-Latin adjective in -āris formed to sōl (node 15); it entered English through scholastic-astronomical Latin rather than through French, and displaced no native word. Watkins lists SOLAR among the English derivatives of Latin sōl under the root *sāwel-.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی solar «خورشیدی» وام‌گیری عالمانه‌ای از sōlāris لاتین است که در میانهٔ سدهٔ پانزدهم میلادی از راه لاتینِ نجومی-مدرسی وارد انگلیسی شد؛ sōlāris صفتی لاتینی با پسوند -āris بر پایهٔ sōl (گرهٔ ۱۵) است. واتکینز در پیوست AHD واژهٔ SOLAR را در شمار مشتقات انگلیسیِ sōl لاتین ذیل ریشهٔ *sāwel- آورده است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/sun\"],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"The node carries no reference on the chart; it inherits AHD from the Latin parent node, where SOLAR is listed explicitly.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. sāwel- and index (AHD_watkins1985.txt lines 905, 2276)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Latin sōl, the sun: SOL, SOLAR, SOLARIUM'; the back index reads 'SOLAR sāwel-'.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein, s.v. solar\",\n              \"stance\": \"supports\",\n              \"note\": \"Klein derives solar from L. sōlāris, fr. sōl, and cross-refers to his entry Sol on pp. 1468-1469.\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-432.json > /dev/null && echo \"JSON OK\"",
 "description": "Write verification JSON for page 432"
}
```


### [2026-09-14T01:45:11.931Z] TOOL RESULT

```
JSON OK
```


## [2026-09-14T01:45:16.726Z] TOOL CALL #101: Bash

```json
{
 "command": "python3 tools/verify_check.py 432",
 "description": "Run verify_check for page 432"
}
```


### [2026-09-14T01:45:17.729Z] TOOL RESULT

```
nodes verified: 16/16
node verdicts: {'confirmed': 10, 'disputed': 2, 'plausible': 3, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 15, 'partial': 6, 'not_checked': 4, 'not_found': 2, 'contradicts': 1}
books consulted: {'supports': 31, 'silent': 6, 'contradicts': 5, 'partial': 6} | by book: {'KLN': 6, 'WLD': 5, 'BRT': 4, 'HRN': 4, 'PHD': 4, 'MON': 4, 'NYB': 3, 'POK': 3, 'SYN': 2, 'BQT': 2, 'ARB': 2, 'AHD': 2, 'RCH': 1, 'PLA': 1, 'AFM': 1, 'SOD': 1, 'HENNING': 1, 'FSF': 1, 'SKT': 1}
```


## [2026-09-14T01:45:38.849Z] AGENT

Verified PDF page 432 (book p. 402), root **Sâwel, Sŭ 3** "sun" (PIE *seh₂wel-/*sóh₂wl̥), one entry, 16 nodes. Output: `/home/sfmqrb/git/rishe/data/verification/page-432.json`; `verify_check.py 432` reports 0 PROBLEM lines.

Verdicts: root confirmed; nodes 10 confirmed, 3 plausible, 2 disputed, 1 transcription_suspect.

Disputed / suspect items:
- **#3 Persian hŭr-bân «هوربان»** — the word is unattested (absent from Borhan vol. 4, Mo'in, Richardson; Nourai's own note admits it is not in MON). It exists only as Addi Shir's reconstruction to explain Arabic ḥirbāʾ.
- **#4 Arabic horbâ «حُرباء»** — modern view makes it native Arabic (root ḥ-r-b, from ḥarba "javelin", with Akkadian/Eblaite cognates). Al-Jawālīqī's editor Aḥmad Shākir rebuts Addi Shir's hūr+bān proposal by name; Asbaghi does not list it among Persian loans. (Node #5, Persian حربا ← Arabic, is confirmed regardless.)
- **#12 Avestan "xvang : son"** — `transcription_suspect`, `error_in: "book"`. The printed page really reads "son"; it is Nourai's misprint for **"sun"**. xᵛə̄ṇg is the gen. sg. of huuarə- "of the sun" (Pokorny 881, WP II 447, Buck §1.52, Klein s.v. *sun*) — and is the very form linking Iranian to Gmc *sunnōn-. Also, being a case-form, it should hang under node 1, not off the root.

Plausible (label problems, not derivation problems):
- **#6** — hvarə.xšaēta- is genuine Avestan, but "hvare-âsân" and "hvare-varân" are Middle Persian (xwarāsān, xwarwarān/xwarōfrān; MacKenzie 95-96, Horn 111), not Avestan.
- **#9** — farnah-/farnavant- are Old Persian/Median f-forms, not Avestan (Av. xᵛarənah-, xᵛarənaŋᵛhant-).
- **#11** — farr/farrox confirmed (Borhan pp. 1443, 1451; MacKenzie; Nyberg); Farīborz only traditionally analysed as farr + borz.

Reference problems in Nourai's own citations:
- **BQT:180** (node 11) `not_found` — vol. 1 p. 180 falls in the انگ…/او… range, unrelated to farr.
- **FSF:250** (node 11) `not_found` — the farr entry is on p. 334 of the available printing (content does support the claim).
- **KLN:1469** (node 6) `partial` — that spread is Klein's "Sol" entry, which supports the root and Av. hvarə but says nothing about the compounds.
- FVF:189 `not_checked` (Emam Shushtari has no accessible copy); MON page numbers unverifiable as usual.

No extraction errors: the JSON matches the printed page throughout. One cosmetic note — the printed chart has an empty, unlabelled box to the right of node 12, which the extraction correctly ignored. Page image saved to `data/verification/sources/refs/ocr/BOOK/432.png`; 8 web sources archived via `fetch_source.py`.
