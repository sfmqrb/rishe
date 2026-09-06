# Verification process log — verify-page-250


## [2026-09-06T16:02:46.303Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 250 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-250.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-250.json. Write /home/sfmqrb/git/rishe/data/verification/page-250.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 250` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T16:02:47.542Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T16:02:48.293Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T16:02:48.308Z] TOOL RESULT

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


## [2026-09-06T16:02:48.726Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-250.txt"
}
```


### [2026-09-06T16:02:48.748Z] TOOL RESULT

```
1	=== PDF page 250 (book page 220) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Kel 1 : cold, also warm, warm season, a year  (refs POK:551; SYN:1078)
4	#1 (parent #0) [Avestan] refs=POK:551; SYN:1078 | sareta : cold ; saretha : bringing cold
5	  #2 (parent #1) [Pahlavi] refs=HRN:23 | sart : cold (adj.) ; sarmâk : cold (noun) ; awsartan : to become cold, to lose hope.
6	    #3 (parent #2) [Persian] refs=POK:551; SYN:1078; BQT:149; | sard «سرد ( سرما )» : cold ; afsordan «افسردن» : to lose hope
7	  #4 (parent #1) [Sogdian] refs=SOD:362 | srt : cold
8	#5 (parent #0) [Avestan] refs=POK:551; SYN:1012 | sarez, sareda : a warm season, a year
9	  #6 (parent #5) [Pahlavi] refs=HRN:153 | sâlak, sâl : year
10	    #7 (parent #6) [Persian] refs=POK:551; SYN:1012 | sâl «سال» : year ; gŭsâleh «گوساله» : calf (one year old) ☞Gwou
11	#8 (parent #0) [Old Persian] refs=SYN:1012; KNT:188; BQT:7 | thard, sard : year ; upa-sard : toward the year, beginning of the year, spring
12	  #9 (parent #8) [Persian] refs=BQT:7 | âbsâl «آبسال ( آبسالان )» : spring
13	#10 (parent #0) [Latin] refs=AHD | calor : heat ; calere : to be warm ; calefâre : to warm up
14	  #11 (parent #10) [French] refs=AHD | calorie, chauffeur, chauffage
15	    #12 (parent #11) [Persian] refs=MON:2090,2860 |  | extra: کالری ، شوفر ، شوفاژ
16	    #13 (parent #11) [English] refs=AHD | calorie, chauffeur
17	#14 (parent #0) [Sogdian] refs=SOD:361 | srd : year
18	--- entry 1 ---
19	ROOT [Indo-European] Kel 2 : to cover  (refs POK:553)
20	#1 (parent #0) [Pahlavi] refs=HRN:192,193; HUB:88 | kulâf : cover, hat ; kurpak : shelter, hut
21	  #2 (parent #1) [Persian] refs=BQT:1671,1673; PLA:233 | kolâh «کلاه» : hat ; kolbeh «کلبه ( کلبک )» : hut
22	#3 (parent #0) [Greek] refs=AHD; SYN:460 | kaluptein : to cover ; kolba : shelter, hut
23	  #4 (parent #3) [Latin] refs=AHD | eu-caliptus : a plant with "well covered" flowers ☞Su 1
24	    #5 (parent #4) [Persian] refs=MON:404 | okâlîptûs «اکالیپتوس» : eucalyptus
25	    #6 (parent #4) [English] refs=None | eucalyptus
26	#7 (parent #0) [Germanic] refs=AHD | hallô : covered place ; helmaz : head cover
27	  #8 (parent #7) [English] refs=None | hall, hell, hole, hollow ; helmet
28	#9 (parent #0) [Latin] refs=AHD | color : that which covers ; cĕlâre : to hide
29	  #10 (parent #9) [English] refs=None | color, conceal
30	
```


## [2026-09-06T16:02:52.381Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-250.json",
 "description": "Read source JSON page 250"
}
```


### [2026-09-06T16:02:52.417Z] TOOL RESULT

```
{
  "pdf_page": 250,
  "book_page": 220,
  "entries": [
    {
      "root": {
        "name": "Kel 1",
        "lang": "Indo-European",
        "refs": "POK:551; SYN:1078",
        "gloss": "cold, also warm, warm season, a year",
        "note": "This root has two opposing meanings"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:551; SYN:1078",
          "words": [
            {
              "translit": "sareta",
              "gloss": "cold",
              "script": null
            },
            {
              "translit": "saretha",
              "gloss": "bringing cold",
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
          "lang": "Pahlavi",
          "refs": "HRN:23",
          "words": [
            {
              "translit": "sart",
              "gloss": "cold (adj.)",
              "script": null
            },
            {
              "translit": "sarmâk",
              "gloss": "cold (noun)",
              "script": null
            },
            {
              "translit": "awsartan",
              "gloss": "to become cold, to lose hope.",
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
          "refs": "POK:551; SYN:1078; BQT:149;",
          "words": [
            {
              "translit": "sard",
              "gloss": "cold",
              "script": "سرد ( سرما )"
            },
            {
              "translit": "afsordan",
              "gloss": "to lose hope",
              "script": "افسردن"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "SOD:362",
          "words": [
            {
              "translit": "srt",
              "gloss": "cold",
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
          "lang": "Avestan",
          "refs": "POK:551; SYN:1012",
          "words": [
            {
              "translit": "sarez, sareda",
              "gloss": "a warm season, a year",
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
          "lang": "Pahlavi",
          "refs": "HRN:153",
          "words": [
            {
              "translit": "sâlak, sâl",
              "gloss": "year",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "POK:551; SYN:1012",
          "words": [
            {
              "translit": "sâl",
              "gloss": "year",
              "script": "سال"
            },
            {
              "translit": "gŭsâleh",
              "gloss": "calf (one year old)",
              "script": "گوساله",
              "see": [
                "Gwou"
              ]
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "SYN:1012; KNT:188; BQT:7",
          "words": [
            {
              "translit": "thard, sard",
              "gloss": "year",
              "script": null
            },
            {
              "translit": "upa-sard",
              "gloss": "toward the year, beginning of the year, spring",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "BQT:7",
          "words": [
            {
              "translit": "âbsâl",
              "gloss": "spring",
              "script": "آبسال ( آبسالان )"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "همان شیپور با صد راه نالان - بسان بلبل اندر آبسالان",
            "poet": "Vîs-o-Râmîn"
          }
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {
              "translit": "calor",
              "gloss": "heat",
              "script": null
            },
            {
              "translit": "calere",
              "gloss": "to be warm",
              "script": null
            },
            {
              "translit": "calefâre",
              "gloss": "to warm up",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "French",
          "refs": "AHD",
          "words": [
            {
              "translit": "calorie, chauffeur, chauffage",
              "gloss": null,
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
          "lang": "Persian",
          "refs": "MON:2090,2860",
          "words": [],
          "script_extra": "کالری ، شوفر ، شوفاژ",
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 11,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {
              "translit": "calorie, chauffeur",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:361",
          "words": [
            {
              "translit": "srd",
              "gloss": "year",
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
        "name": "Kel 2",
        "lang": "Indo-European",
        "refs": "POK:553",
        "gloss": "to cover"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "HRN:192,193; HUB:88",
          "words": [
            {
              "translit": "kulâf",
              "gloss": "cover, hat",
              "script": null
            },
            {
              "translit": "kurpak",
              "gloss": "shelter, hut",
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
          "refs": "BQT:1671,1673; PLA:233",
          "words": [
            {
              "translit": "kolâh",
              "gloss": "hat",
              "script": "کلاه"
            },
            {
              "translit": "kolbeh",
              "gloss": "hut",
              "script": "کلبه ( کلبک )"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD; SYN:460",
          "words": [
            {
              "translit": "kaluptein",
              "gloss": "to cover",
              "script": null
            },
            {
              "translit": "kolba",
              "gloss": "shelter, hut",
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
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {
              "translit": "eu-caliptus",
              "gloss": "a plant with \"well covered\" flowers",
              "script": null,
              "see": [
                "Su 1"
              ]
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
          "refs": "MON:404",
          "words": [
            {
              "translit": "okâlîptûs",
              "gloss": "eucalyptus",
              "script": "اکالیپتوس"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 4,
          "lang": "English",
          "refs": null,
          "words": [
            {
              "translit": "eucalyptus",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {
              "translit": "hallô",
              "gloss": "covered place",
              "script": null
            },
            {
              "translit": "helmaz",
              "gloss": "head cover",
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
          "lang": "English",
          "refs": null,
          "words": [
            {
              "translit": "hall, hell, hole, hollow",
              "gloss": null,
              "script": null
            },
            {
              "translit": "helmet",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {
              "translit": "color",
              "gloss": "that which covers",
              "script": null
            },
            {
              "translit": "cĕlâre",
              "gloss": "to hide",
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
              "translit": "color, conceal",
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


## [2026-09-06T16:02:53.004Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T16:02:53.039Z] TOOL RESULT

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


## [2026-09-06T16:03:40.141Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','SYN','HRN','KNT','BQT','SOD','MON','HUB','PLA','AHD','BRT','PHD','NYB','CHEUNG','ARY','WLD','IEC','KLN','SKT','LEW','LAT']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:600])\n    print()\n\""
}
```


## [2026-09-06T16:03:40.220Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -40 && echo --- && head -60 data/verification/page-205.json"
}
```


### [2026-09-06T16:03:42.150Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

CHEUNG null

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos
```


### [2026-09-06T16:03:42.191Z] TOOL RESULT

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
---
{
  "pdf_page": 205,
  "book_page": 175,
  "verified_by": "claude-opus-5",
  "verified_on": "2026-09-05",
  "entries": [
    {
      "entry": 0,
      "root": "Gwei",
      "verdict": "confirmed",
      "modern_form": "PIE *gʷeyh₃- (Pokorny 'gʷei-3, gʷeiə-, gʷii̯ē-, gʷi̯ō-, gʷī-, frequent, often with -u̯- extended') 'to live'",
      "note": "The root box is right on all three counts. Pokorny's lemma reads 'Root/lemma: gʷei-3 and gʷeiə-: gʷii̯ē-: gʷi̯ō-: gʷī-, frequent, often with -u̯- extended. Meaning: to live', with 'Page(s): 467-469', so Nourai's 'Gwei : to live' with POK:467 reproduces Pokorny's own heading and page; Watkins in the AHD appendix has 'gʷei-. Also gʷeiə-. To live ... [Pok. 3. gʷei- 467]'; Wiktionary reconstructs *gʷeyh₃- 'to live' (alternative *gʷyeh₃-); Cheung, for the Iranian verb, writes '*jaiH2 ... «PIE *gʷeiH₃-, *gʷieH₃-/*gʷih₃- \"to live\" © LIV: 215 f. | Pok.: 467 f.'. What is striking about this chart is how much of it is simply Pokorny's own article rearranged: pages 467-469 contain, in order, Avestan gaya- and gaēθā-/Old Persian gaiθā, Avestan jīti- and jīra-, Old Persian jīva-/Avestan jva-, Greek bios, zōḗ, zōion and hygiḗs, Latin vīvus/vīvō/vīta, and Old English cwicu / OHG queh — that is, every branch of the page except the modern coinages. Klein's article 'quick' (p.1288, Nourai's own citation on node 1) carries the same set in one paragraph. Three things need qualifying rather than correcting: the Avestan citation forms in node 1 ('jîta', 'merezu-jîta' for jīti-, mərəzu-jīti-/-jva-); the gloss 'to exist' given to the noun gaēθā- in node 8; and the presence of two 19th/20th-century neologisms ('mikro-bios' in the Greek box, 'vitamine' in the French box) among inherited words. Everything on the Iranian side — zīwistan/zīwandag → زیستن/زنده/ژیوه, the Arabic round trip زیبق, gayō.marətan- → کیومرث, gaēθanąm → gēhān → گیتی/کیهان/جهان, jīra- → زیرک/آژیر — checks out against Horn, Hübschmann, MacKenzie, Nyberg, Bartholomae, Asbaghi and Moʿin's footnotes on the very Borhān pages Nourai cites.",
      "note_fa": "جعبهٔ ریشه از هر سه جهت درست است: پوکورنی مادّهٔ «gʷei-3 و gʷeiə-…» را با معنای «زیستن» در صفحات ۴۶۷–۴۶۹ آورده، پس هم صورت و هم برچسبِ زبان و هم معنا و هم شمارهٔ صفحه‌ای که نورایی داده دقیق است؛ واتکینز نیز همین را می‌گوید و ویکی‌واژه آن را *gʷeyh₃- بازسازی می‌کند و چونگ در فرهنگِ فعلِ ایرانی ذیل *jaiH₂ همین ریشه را می‌آورد. نکتهٔ چشمگیر این است که بیشترِ نمودار در واقع بازچینشِ همان مقالهٔ پوکورنی است: اوستایی gaya- و gaēθā-، پارسی باستان gaiθā، jīti- و jīra-، jīva-/jva-، یونانی bios و zōḗ و hygiḗs، لاتین vīvus و vīta، و انگلیسی کهن cwicu همه در همان سه صفحه‌اند. سه نکته باید روشن شود، نه اصلاح: صورت‌های اوستاییِ گرهٔ ۱ («jîta» به‌جای jīti-)، معنای نادرستِ «to exist» برای اسمِ gaēθā- در گرهٔ ۸، و حضورِ دو نوواژهٔ سدهٔ نوزدهم و بیستم (mikro-bios و vitamine) در کنارِ واژه‌های موروثی. تمامِ بخشِ ایرانیِ نمودار — از zīwistan تا «زیستن» و «زنده» و «ژیوه»، چرخهٔ «زیبق»، gayō.marətan- تا «کیومرث»، gaēθanąm تا «گیهان/گیتی/کیهان/جهان»، و jīra- تا «زیرک/آژیر» — با هرن، هوبشمان، مکنزی، نیبرگ، بارتولمه، اصباغی و حواشیِ معین بر همان صفحاتِ برهانِ قاطع که نورایی ارجاع داده می‌خواند.",
      "sources": [
        "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7eyh%E2%82%83-"
      ],
      "ref_check": [
        {
          "ref": "POK:467",
          "status": "supports",
          "note": "POK_full.txt lines 38677-38790: 'Root / lemma: gʷei-3 and gʷeiə-: gʷii̯ē-: gʷi̯ō-: gʷī-, frequent, often with -u̯- extended || Meaning: to live || Material: A. from *gʷei-: Old Indic jīvatu-ḥ \"life\", gaya-ḥ \"house, courtyard\" ... Avestan gaēθā, Old pers. gaiθā \"entity, house and courtyard\" ... References: WP. I 668 ff. ... Page(s): 467-469.' Exactly the root box as drawn."
        }
      ],
      "consulted": [
        {
          "src": "AHD",
          "where": "Watkins 1985, IE roots appendix s.v. gʷei- (AHD_watkins1985.txt line 540)",
          "stance": "supports",
          "note": "'gʷei-. Also gʷeiə-. To live. I. Suffixed zero-grade form *gʷi-wo-, *gʷī-wo- ... [Pok. 3. gʷei- 467.]' — the same root, gloss and Pokorny page."
        },
        {
          "src": "WLD",
          "where": "Walde-Pokorny I 668-669 (WLD_Bd1_pages.txt leaves 676-677, running head 'gʷei(ə)-')",
          "stance": "supports",
          "note": "the source article that Pokorny 467 abridges, with the Germanic and Greek material set out at length ('mhd. verquīnen ... ags. cwīnan ... got. qistjan')."
        },
        {
          "src": "KLN",
          "where": "Klein 1966 p.1288 s.v. quick",
          "stance": "supports",
          "note": "'fr. I.-E. *gwigwos, fr. base *gwei-, \"to live\", whence Goth. *qius ... OI. jivah ... Avestic jvaiti ... OPers. jiva- ... Gk. bios ... zōē ... L. vivus ... vita ... OIr. bith, W. byd, \"world\" ... Cp. also zodiac, zoetic, zoo-.'"
        },
        {
          "src": "CHEUNG",
          "where": "Etymological Dictionary of the Iranian Verb, *jaiH2, p.223",
          "stance": "supports",
          "note": "'«PIE *gʷeiH₃-, *gʷieH₃-/*gʷih₃- \"to live\" © LIV: 215 f. | Pok.: 467 f. *IE COGNATES: Lat. vivo, OCS živǫ, Lith. gyju, Latv. dzīvu \"I live\", Toch. śaw- \"to live\"'."
        },
        {
          "src": "SYN",
          "where": "Buck, Dictionary of Selected Synonyms",
          "stance": "silent",
          "note": "grep of SYN.txt for the root shapes produced no clean hit (the OCR mangles the labiovelar notation); Buck's chapter 4.74 'live' was not located in the text file."
        }
      ],
      "nodes": [
        {
          "id": 1,
          "lang": "Avestan / Old Persian",
          "words": "jiva, jîta, jva; merezu-jîta; hu-jyâti",
```


## [2026-09-06T16:03:46.146Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 551\" POK_full.txt | head -20; echo \"=== 553 ===\"; grep -n \"Page(s): 553\" POK_full.txt | head -20"
}
```


### [2026-09-06T16:03:46.209Z] TOOL RESULT

```
45111:Page(s): 551 
47171:Page(s): 551 
49867:Page(s): 551-552 
=== 553 ===
50001:Page(s): 553-554
```


## [2026-09-06T16:03:46.543Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^Root / lemma: kel\" POK_full.txt | head -30"
}
```


### [2026-09-06T16:03:46.589Z] TOOL RESULT

```
44616:Root / lemma: kelg- 
44630:Root / lemma: kel-1, kela- 
44697:Root / lemma: kel-2 
44745:Root / lemma: kel-3, kela-, A/a- extended klad- 
44927:Root / lemma: kel-5 
44963:Root / lemma: kel-6, k(e)le-, k(e)la-or 1(1-1 
45077:Root / lemma: kel-7{kol-, kj^ 
45105:Root / lemma: kel-7 
45113:Root / lemma: kelp-, l^lp- 
47147:Root / lemma: kel-, kol-, kal- 
93753:Root / lemma: keleu-
```


## [2026-09-06T16:03:49.233Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '45070,45120p' POK_full.txt; echo \"======47140\"; sed -n '47140,47180p' POK_full.txt; echo \"======49840\"; sed -n '49840,49875p' POK_full.txt"
}
```


### [2026-09-06T16:03:49.326Z] TOOL RESULT

```
(influence of kuojv?) could belong together directly from Celtic *koligno-, Lithuanian kale, 
alb. kelush. 

References: WP. I 443 ff., WH. I 141 f., 227, 228, 258, Specht KZ. 59, 85 ff.; 
See also: probably identical with kel-5. 
Page(s): 548-550 

Root / lemma: kel-7{kol-, kj^ 

Meaning: goblet 

Note: with ^-suffix 

Material: Old Indie kalasa-hxn. "pot, pan, crock, pitcher, bowl' {*koleko-, -oko-); 

gr. KuAi^, -iKoq "goblet' {*keli-k); 

= Latin callx, -Iclsm. "deep bowl, goblet, calix' (from callx6emes Old High German 
chellh. Modern High German Kelch " calix '), wherefore perhaps with moveable s Umbrian 
skalge-ta, scalse-to lormer \ow bowl, flattened dish, saucer, libation-saucer', scalsle"\n a 



low bowl, flattened dish, saucer, libation-saucer '; Latin culigna^ small calix' from gr. 
KuAixvP) (*KuAiK-ava) ds.; 

There s- also in Modern High German Schale^ shell ' (that to {s)kel- "cut, clip') and in gr. 
GKoAAiov, aKaAi(; ds. Hes.,. 

In addition gr. kqAu^, -ukoc; f. " fruit cup, grain cup ' and perhaps Old Indie kalika\. "bud' 
(different in gutturals of suffixes from kalasa-h). 

References: WP. I 442, WH. 1138 f. 
Page(s): 550-551 

Root / lemma: kel-7 

Meaning: " chop, cut '; " be at fault, be to blame, be wrong; " parch, dry '; " bend ' 

See also: see below (s)kel- 

Page(s): 551 

Root / lemma: kelp-, l^lp- 

Meaning: jar, cauldron 

Material: Gr. kqAhk;, -i5oc;, KaATrn f. "crock, pitcher; cinerary urn '; 

Latin calpar, -aris " wine cask ' ( *calp-ali-, probably Latin further formations of gr. 
KoAna); 
======47140
grade formation as Old Indie cyautna-, but with reduced u, is probably here suitable 
awTpov ' wooden felloe of the wheel ', EniaawTpov ' wheel rim, the metal hoop round the 
felloe '. 

References: WP. I 361 ff., WH. I 213 f., Schwyzer Gr. Gr. I 679, 686, 745. 
Page(s): 538-539 

Root / lemma: kel-, kol-, kal- 

Meaning: to deceive, enthrall, etc.. 

Material: Gr. Attic khAeu) (proto gr. n) " enchant, beguile, bewitch ', Kr|Ar|0M6<; ' enthrallment 

', KriAr|56v£(; PI. f. ' enchanting creature '; 

Latin calvor, -/"and calvid, -Tre ' devise tricks, use artifice, attack one with artifice, to 
intrigue against, to deceive ', calumniala\se accusation, deceit, slander, trickery, artifice, 
chicanery, cunning ' {*calvomnia), very probably also cavilla {*calvilla) ' badinage, mocking 
', cavillor, -a/7 to jeer, mock, criticise, satirize, jest '; -v- is unclear; 

Gothic holon, afhd/dn's\ander', Old Norse ho/n. ' laudation, boastfulness ', M/a' 
praise, brag, boast'. Old English ho/n. ' slander', /7d//a/7 'slander', holunga, holinga^ in 
vain, groundless ', /7e/a/7 'slander'. Old High German huo/en ' cheat, deceive'. 



Should probably Perssons (Beitr. 148) citation of gr. KoAa^ " adulator ' apply to (?), it 
would be assumed the root as short vocal, hence gr. Kr\k- and Germanic ho/- lengthened 
grade, Latin ca/- reduced grade. 

References: WP. I 446, WH. I 143, 187; Wissmann Nom. postverb. 125. 
Page(s): 551 

Root / lemma: ket- kot- 

Meaning: dwelling space 

Note: 

Root/ lemma: ket-, kot-\ dwelling space, derived from Root/ lemma: kat-1\ to link or 

======49840

2. Old Indie sar^o'-f'autumn', with numeral, word that represents a number 'year', 
Avestan sara5-\. 'year' (see also Solmsen KZ. 34, 78 to Lydian aap5ic; 'year'), osset. sard 
'summer', npers. saryeaf ('autumn' as ' warm time ', also Lithuanian s//i/s 'August', more 
properly silius); 

Latin caleo, -ere 'warm, be hot, glow', caMus 'warm, hot', ca/or' warmth, heat'; 

cymr. c/ycf{ *RI-to-) 'warm, warming' (: Lithuanian s/Itas); in addition perhaps from an e/- 
extension cymr. claear' lukewarm ', bret. klouar6s.l 

Old Saxon ha/o/an 'burn'; in Germanic became an extension *Rleu-: Old High German 
lao, fleet, /a M^e/"' lukewarm, warm'. Old Icelandic hlserAs., oi weather {*h/ew/a-), hIana'rwM 
become'. Bavarian /aunen' thaw'. Old Icelandic hiaka' thaw': Old Icelandic /?///' 'lukewarm', 
hlyr\. ' warmth ', Old English /7/eoM/e 'lukewarm'. Old Icelandic hle{*hlewa-) n. ' protection, 
lee, side protected from the wind'. Old Saxon hleo m' protection before the weather ', Old 
Frisian hIT, Old English hleo, hleowr\. 'hideout, cover, protection' (compare also Middle 
High German liewe, lie\. 'bower, network of branches, shaded place', Swiss /e 'sheltered 
position, sunny side', Swedish lya'caNe of animals '); Norwegian Danish lum, lummer 
'mild, lukewarm', Swedish //um6s., Swiss /J/77 'mild, of weather' , ndd. /uk, holl. /euk 
'lukewarm'. 

Lithuanian sy/u, silau, s/'/t/'warm become'; s/Itas'warm' (: cymr. c/ycf). 



References: WP. I 429 f., WH. I 137, Trautmann 297 f., 304 f. 
Page(s): 551-552 

Root / lemma: Rel-2 

Meaning: to incline 

Material: The base of tlie root form developed much more Rlei- 'lean' (see below) and very 

probably in consecutive words to recognize:
```


## [2026-09-06T16:03:53.346Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '49810,49845p' POK_full.txt"
}
```


### [2026-09-06T16:03:53.399Z] TOOL RESULT

```
Material: Gothic hilpan. Old Icelandic hjalpa. Old Saxon Old English helpan. Old High 

German helfan, he/phan^\r\e\p'; 

Lithuanian selpili, selpti. Old Lithuanian se/b/nos'\r\e\p, aid '; unclear is the relationship 
to gelbeti^\\e\p\ 

References: WP. I 447 f., Trautmann 302, Feist 255 f. 
Page(s): 554 



Root / lemma: Rel-1 

Meaning: cold; warm 

Material: 1. Old Indie s/s/ra-'coo\, cold', m. " cool time, coldness', Avestan sarata- 'cold', 

npers. sarc/ds., osset. sa/o' 'coldness', Avestan sara-6a-' bringing coldness '; 

Old Icelandic he/a' hoarfrost {hi-hlon-, compare Old Indie si-sira-)\ Dutch halu. 'frozen 
bottom', with lengthened grade eOld High German /7a//" slippery, smooth ', Modern High 
German Bavarian hal, Swiss ha/6s., Old English hselig' changeable ', Old Icelandic hair 
smooth, cunning'; 

Lithuanian s^lu, saiti' freeze ' (Latvian salt}, sa/tas'co\6' (Latvian 537/5), sa/na' 
hoarfrost (Latvian salna), pasa/as Irozen earth' = Old Prussian passa//s IrosV , Lithuanian 
pasolys ' night frost, frost in the earth'; 

Old Bulgarian slana' hoarfrost '. 

2. Old Indie sar^o'-f'autumn', with numeral, word that represents a number 'year', 
Avestan sara5-\. 'year' (see also Solmsen KZ. 34, 78 to Lydian aap5ic; 'year'), osset. sard 
'summer', npers. saryeaf ('autumn' as ' warm time ', also Lithuanian s//i/s 'August', more 
properly silius);
```


## [2026-09-06T16:03:53.882Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '49940,50010p' POK_full.txt"
}
```


### [2026-09-06T16:03:53.936Z] TOOL RESULT

```
enclosure, hedge ', 5a//775- "verlegen' (*hidden, concealed); very doubtful Old Indie sata-m., 

satTi. "kerchief, cloth, bandage'; 

gr. KaATa: "cottage, barn, nest'; K6Au9po(; m. "sack, bag, pouch '; hom. koAsov, stretched 
metrically kouAeov, Attic koKzoc, "vagina' (*koA£F6(;; unclear Latin c^//e^s "leather sack', 
from which russ. kulb, poln. /ri//"sack, bag', out of it again Lithuanian ku//s6s., kulikas. Old 
Prussian ku//ks'bag '); with labial extension KaAunru) " wrap, hide', KoAupn "hideout, 
cottage', KsAucpoc; n. "bowl, husk'; labial shows also probably cognate Middle High German 
hu/ft' quiver ' (see below); 

Maybe alb. /r^/e "hernia'. 

Latin *celd{= Old Irish celim. Old High German helan) in occulo, -e/ie "conceal'; color, - 
0/7S "paint, color' (arch, colds, actually "sleeve, wrapping, external side '); lengthened 
grade celo, -are' hide, conceal', nominal ce//a "storeroom, chamber, cell ' (probably with 
consonant increase for *cela= Old Indie sala); zero grade clam' clandestine ' (Akk. a 
*cla), clandestFnus ' secret ' from *clam-de; also Oscan kafia' a place of concealment, 
store-room, cell, granary ' {*kalja); 

clllum (from Plinius) "eyelid, esp. the low' and the older superclllum " upper eyelid' 
probably from * super-keliom "the upper cover'; 



Old Irish ce//m'W\de\ cymr. ce/c/ 'conceal', Old Irish c^//e "cellar, warehouse ' and ' 
kitchen ' (not from Latin culTna, but influenced in the meaning therefrom). Middle Irish luid 
arcer obiit ', actually ' fuhrzur Holle '; Middle Irish cur protection', cu/a/d's\eeye, 
wrapping ' {*colu-), probably also colum, Dat. PI. co/omna/t>' skin, hide' and cuilche 
"mantle' {*kolikia)\ Middle Irish clitharru. " protection' {*RI-tu-ro-)\ 

Old High German Old Saxon Old English /7e/5/7 "conceal', next to which from an present 
Aorist -hulan, Gothic hulundii. "cave' {*RQlntr the rescuing '), Gothic huljan. Old Norse 
hyija. Old High German hullen' veil, cover', whereof with Germanic Suff. -stra-, Gothic 
hulistru. "sleeve, cover'. Old Norse hulstr^ sheath '; in an old -es-stem (see Latin color) 
based on whereas probably Middle High German hulsti. "cover, sleeve ' and Middle Low 
German hulse. Old High German hulsa, hulis^husV! (Old English helustr, heo/stor's\ee\/e, 
hiding place, nook, bolt-hole, darkness' with Germanic suffix vowel gradation or at most 
with Indo Germanic *Relu-)\ compare in similar meaning Old English hului. "bowl, husk'. 
Old High German helawa, helwa^ oat chaff ', Swedish dial, hjelmvn. ds.. Old High German 
/7a/a "cover, bowl'; Gothic hilms. Old High German Old Saxon Old English /7e//77 "helmet'. 
Old Norse hjalmr6s.. Old English he/ma\so " protector' (: Old Indie sarman-, word has 
shifted in this Slavic in Baltic: Lithuanian 5a//775S 'helmet' etc.); Gothic haija. Old High 
German hella. Old Saxon hellia. Old English helli. " underworld, hell ', Old Norse her 
death goddess ' from *halja-, Indo Germanic *RolJo-, compare Finnish-ugr. Koljo^ 
underworld demon '; 

after Szadrowsky (PBrB. 72, 221 ff.) soil Germanic *halj6^ the concealing, the kingdom of 
the dead ' have merged already early with *halljd(n) "flagstone ' (to Gothic hallus "rock'); s. 
also under (s)kel-^S'^\\\!\ Old High German Old Saxon halla. Old English heair hall ', Old 
Norse hglli. "big house' {*Rolna)\ Norwegian /7^/0'e/' (participle Pass. f. *hult^J), hulda^ 
forest elf. Modern High German Frau Holle^heW; 

lengthened grade Old High German hala^ the concealment ', Middle High German h^le 
" concealment ', Old Norse haeliu. " hideout ', Old High German hali^ concealing, hidden '. 

With labial extension: Middle High German hulft, holfte, hulfe, hulft " quiver ', Middle 
Low German hu/ffe ds. (: KaAunTOj); compare also R/ep- 

References: WP. I 432 f., WH. I 195 ff., 214 f., 226 f.; J. Loth RC. 42, 88 f. 
See also: s. also under /r/e/?- "conceal'. 
Page(s): 553-554 

Root / lemma: Rem/9/-4 



Meaning: to be tired 

Material: Old Indie samnTte, samati, samyati. Imp. samJ-sva' exert themselves, slave, 
work, prepare, concoct', samita- " prepares ', samitar- "worker for preparing of pressure
```


## [2026-09-06T16:04:06.817Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '49915,49942p' POK_full.txt"
}
```


### [2026-09-06T16:04:06.869Z] TOOL RESULT

```
gr. Kf|Aov "arrow, projectile'; 

Middle Irish ca/7'spear, javelin', celtairi. "spear, spearhead'; 

Old Norse haliru. " apex of a shaft, tail '; 

Old Prussian ke//an 'spear, javelin' with West Indo Germanic /rfor /c, Lithuanian s/'/as' 
moor, heath, moorland ' (after the rigid stalks). 

References: WP. I 431 f., WH. I 304. 
Page(s): 552-553 

Root / lemma: Re/-4 

Meaning: to conceal 

Material: Old Indie sarana- "sheltering', n. " shelter, protective roof, cottage', sarman- n. " 

shelter, protective roof, cover, guarding' (: Modern High German Helm), lengthened grade 

(as Latin celo, cella. Old High German hali) sa/at "cottage, house, chamber', sa/a- m. " 

enclosure, hedge ', 5a//775- "verlegen' (*hidden, concealed); very doubtful Old Indie sata-m., 

satTi. "kerchief, cloth, bandage';
```


## [2026-09-06T16:04:07.450Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==207' POK_02.txt | head -80"
}
```


### [2026-09-06T16:04:09.373Z] TOOL RESULT

```
cpelt]  ävvöoog  y,at  xeiiiSQivt}  '^^leqa'  y,al  cc|§^ fJTLg  ytarä  rd  ^hwrtov  aiqixsLOv  e%si  xvlosLÖeg  Hes. ;
lat.  cälidus,  calUdus  (Gl.)  ,weißstirni^  *(von  Pferden)'  =  umbr.  kalef-uf (huf)  ,calIidos  (boves)^;  lat.  caligo  f.  ,Nebel,  Finsternis^;
air.  caile,  mir.  gaile  ,Fleck';
lit.  kalyhasj  kalyvas  ^weißhalsig^ ;
aksi.  kah  jTtrjlögj  Kot*^  mit  den  Bedeutungen  ^Sumpf,  Morast,  mit  Kot beschmutzen^ ;  dazu  (nach  der  Farbe)  russ.  kalina  ,Viburnum  opulus^,  wie auch  sloven.  kalina  ,Pfütze^   und  russ.  kalü-ga  ^Morast^,  kalu-za  ,Lache'.
WP.  I  440ff.,  WH.  I  139 f.,  249,  Specht  Idg.  Dekl.  118,  140,  143==, Trautmann  113  f.,  Petersson  Heterokl.  146  f.
5.  kel-  ,treiben,  zu  schneller  Bewegung  antreibend
Ai.  kUldyati  ,treibt,  trägt,  nimmt  wahr,  hält' ;
alb.  geg.  qilj  sizil.  qel  ,bringe,  trage^,  shqütse  ,Lab,  d.  i.  co-agulum^, wohl  auch  kal  ,stifte,  stelle  an^  (Jokl  IF,  30,  198);
gr.  xsXXü)  ,treibe  (das  Schiff  ans  Land);  lande^  (Präs.  nur  bei  Gramm, und  in  d-^sXX(jü  trans.  ,treibe  das  Schiff  ans  Land;  strande,  scheitere^; sonst  nur  Aor.  Fut.  ey^XacXj  -/.eXact)),  y-iXrjgj  -rjTog  ,Renner  (Pferd);  schnell- segelndes Schiff' ;  y,X6vog  ,heftige  Bewegung',  'AXoveo)  ,vor  sich  her  treiben' (vgl.  d^Q-övog,  %Q-6vog ;  Boisacq  s.  v.  m.  Lit.) ;  vielleicht  (Persson  Beitr.  179) y.oXbiv'  iX&stv  und  xoAior,  xoXia  ,Art  Tanz'  Hes.;
lat.  celer  , schnell,  rasch^  (wie  y,eXrjg)y  celeber,  -bris,  -bre  ,betrieben,  be- fahren (via),  "belebt  {locus,  oppidum),  häufig,  gefeiert'  (*kele-dhlo-,  -dhli-)]
als  ^Präs.  got.  haldan  ,Vieh  weiden^  (zum  a-Vok.  s.  Brugmann  IF.  32, 181),  ahd.  haltan  ,hüten,  halten',  as.  haldan,  ags.  healdan,  aisl.  halda, aschwed.  halla  (*halpan)  ,halten',  mnd.  hilde,  kille  ,rasch,  eifrig'^.
WP.  I  442f.,  WH.  I'l94f.;  wohl  identisch  mit  6.  kel--,  s.  auch  keleu- ,wandern^.
6,  kel-,  k(c)le-,  k{e)l^-  oder  kl-7  ,rufen,  schreien,  lärmen,  klingend
Ai.  usä-kala-  m.  ,Hahn'  (j^t-xaydg'),  kalädhika-,  kalävika-  ds~kala- vitdka-  ,Sperling',  kala-  ,leise  tönend,  undeutlich  vernehmbar',  kalakala- m.  ,verworrenes  Geschrei,  Geräusch';
gr.  %aXs(a  (statt  *xaAw)  ,rufe,  nenne,  rufe  herbei^  (äol.  ycdXrjfML),  Futur. xaXeaü)^  att.  naXw,  Perf.  xixXjjTtay  ycXrjTÖg;  inUXriaig  ,BeinameS  vXfiaig ,Ruf,  Einladung,  Vorladung',  ^XriTrig,  yi(a)Xrjru}Q  ,Rufer',  df^oxXrj  ,Zuruf' (zum  1.  Glied  s.  unter  om9-);   Tuydrjaxü)  (oder  xixAi^'crxw)  ,rufe  an,  flehe^.
549
yclrjt^oi,  xlfj^ü)  ;,nemie^  (*xA?;-/«-g-£^co ?) ;  hochstufig-  x5A(a)-  in  yielofuai  ^treibe an  (durch  Zurufy,
```


## [2026-09-06T16:04:16.597Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=209 && NR<=211' POK_02.txt | grep -n \"\" | sed -n '1,200p' | grep -i -n -E \"sarad|sarat|kalt|warm|sard|caleo|calor|551|552|553\" | head -40"
}
```


### [2026-09-06T16:04:18.272Z] TOOL RESULT

```
16:16:551
27:27:I.  kel-  1.  ,frieren,  kalt^,  2.  ,warm^  (Bedeutungvermittlungs  wohl  ,brennend^).
28:28:1.  Ai.  sisira-  ,kühl,  kalt^,  m.  ,kühle  Zeit,  Kälte^,  av.  sardta-  ,kalt^, npers.  sard  ds.,  osset.  sald  ,Kälte^,  av.  sard-öä-  ,Kälte  bringend^;
30:30:lit,  sqliij  sdlti  ,frieren^  (lett.  salt)y  sdltas  ,kalt^  (lett.  salts),  salnä  ,Reif^ (lett.  salna),  päSalas  ,gefrorene  Erde^  =  apr.  passalis  ,Frost^,  lit.  pasolys ,Nachtfrost,  Frost  in  der  Erde';
32:32:2.  Ai.  sardd-  f.  ,Herbst',  mit  Zahlwörtern  ,Jahr',  av.  sardd-  f.  ,Jahr' (s.  auch  Solmsen  KZ.  34,  78  zu  1yd.  aaqdig  ,Jahr'),  osset.  särd  , Sommer', npers.  säl  ,Jahr'  (,Herbst'  als  ,warme  Ze
34:34:lat.  caleö,  -ere  ,warm,  heiß  sein,  glühen',  calidus  ,warm,  heiß',  calor , Wärme,  Hitze';
35:35:cymr.  clyd  (*Jcl-to-)  ,warm,  wärmend'  ( :  lit.  siltas) ;  dazu  vielleicht  von einer  ei*-Erweiterung  cjmr.  claear  ,lauwarm',  bret.  hlouar  ds.?/
36:36:552
38:38:lit.  sylüj  silau,  silti  ,warm  werden^;  siltas  ,warm^  (:  cymr.  clyd),
```


## [2026-09-06T16:04:42.316Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN leaf 1102 (p.1078) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==1103' SYN.txt | head -60"
}
```


## [2026-09-06T16:04:42.644Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN p.1012 -> leaf 1036 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==1037' SYN.txt | head -60"
}
```


### [2026-09-06T16:04:43.922Z] TOOL RESULT

```
=== SYN leaf 1102 (p.1078) ===
ication of smells analogous to that of tastes (as ‘sweet, bitter’, etc.), and the
situation is the same today. There is still neither an accepted scientific class! fication nor a popular classification re flected in common speech, that is truly distinctive of the sense of smell.
The only widespread popular distinction 18
that of pleasant and unpleasant mall good and bad smells, to use the briefes
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
= wa 2s = |
ee
this is linguistically more a than any similar distinction, E od and bad, in the case of Otherwise, we have ms belonging primarily to ame vegpeciallY taste (the actual pie of smell and taste, the fact eect ‘tastes’ really depend upon ae hardly a factor in this, it is too le. known), 2S sweel, acrid, pungent (orig. of touch, ‘pricking ), ete. Or else we describe the smell by naming the object which emits it, as the smell of a rose. Similar expressions are, of course, used of other senses, the taste of an apple, the sound of a bell, etc., but we are less dependent upon them, since there are at least some generic terms. The Hindus enumerated nine kinds of smell, the Skt. terms (quoted in BR, s.v.
The majority of the words for ‘fra- ea are derived from words for ‘smell’ an 1-24), either with an adv. prefix a . Sweet’, or more often resting on a Xialization of ‘smell’ to ‘good smell’. c Tk. eds, cpd. of eb- ‘well? and Toot of dtw ‘smell’. Hupwdaros, deri i, ‘smell’ ee 7 eriv. of pupword ‘smell OF, “a Sragrans (> It. fragrante, of ae Fragrant, Sp. fragante); pple. ¢ emit a (good) smell’.
and ‘gr
SENSE PERCEPTION
Digitized by Arya Samaj Foundation Chennai and eGangotri
1025
gandha-) meaning ‘desirable, undesir- able, sweet, sharp, diffusive, compressed, smooth, rough, soft’, none of them pri- marily distinctive of smell.
It has been argued by some that the lack of classification is due to the lack of distinctive linguistic terms. Quite the opposite is true. Such terms would have arisen had there been any obvious basis of grouping. The lack of them reflects the inherent difficulty of classification, which even modern science has not over- come. Cf. also Kretschmer, Glotta 19.209 f., in review of Weisgerber, Der Geruchsinn in unseren Sprachen, IF 46.121 ff.
To illustrate the words referring to good or bad smells the adjs. are chosen. The corresponding sbs. and vbs. are in most cases cognate with them.
15.25 GOOD SMELLING, FRAGRANT
Grk.  ebdbins Goth. (dauns wopi, sb.) Lith. kvapus, kvapingas NG —pvpwSaros ON vel fefadr, vel ilmadr, Lett.  smarSains, smardigs Int.  fragrans, odorifer pefgoor ChSl. blagovoninis (sudvis) Dan. _vellugtende, duftende SCr. _- mirisav It, olezzante, fragrante, Sw. villuktande, doftande Boh.  vonny odorifero OE wel-, swotstincende Pol. wonny Fr. odoriférant ME wel, swote stinkinge Russ. duSistyj, blagovonnyj Sp. _oloroso, fragante NE fragrant Skt.  sugandhi- Rum. mirositor Du.  welriekend, geurig Av. hubaosi- . boladmar, cumra OHG _— suozo stinkentt ro eel MHG  wol riechend
```


### [2026-09-06T16:04:45.403Z] TOOL RESULT

```
=== SYN p.1012 -> leaf 1036 ===
NIE early, beside comp. in OE @r, ME er(e) (often with positive force) : Goth. airis, OHG ér ‘before, earlier’, all perh. as ‘early in the morn- ing’: Grk. #épios ‘of the morning’, jpt ‘in the morning’, Av. ayara ‘day’, root connection dub. Walde-P. 1.3. Falk- Torp 8. Feist 24 f.
ON snemma, snimma, in epds. snemm- etym. dub. Falk-Torp 1097, 1550. Walde-P. 2.696.
: di dj. tidig) fr. «lig, 8° tidigt (a pan. i a anksti : OPruss. angstainat, b ne rly in the morning’, possibly _ *onkt- beside *nokt- in _ nahts, Lat. noctis, Walde-P. 2.339. Other- n 9, etc.) : Skt. afijas denly’, Goth. anaks ‘at
fearly : : ee savic (but Boh. rdno sb. ‘morning,
TIME
Digitized by Arya Samaj Foundation Chennai and eGangotri
961
hence adj. rannj ‘early’, adv. ranné), prob. as ‘(sun)rise’ fr. *wrddh-no- : Grk. 3p9pos ‘dawn’, adj. épOpus ‘at dawn, early in the morning’, etc., fr. the root in Skt. urdh- ‘rise, grow’; cf. Bulg. razda se ‘(the sun) rises’. Walde-P. !1.290. Von- drak 1.528.
ChSl. za utra (renders Grk. zpwt), lit. ‘in the morning’ (utro, 14.44).
Boh. éasné, Pol. wezesnie (adjs. éasny, wezesny), fr. Boh. éas, Pol. czas ‘time’ (14.11). Briickner 73.
7. Beside Skt. pratar ‘early in the morning’ (above, 1), there seem to be no generic words for ‘early’. The nearest approach would be expressions for ‘at the beginning, before, formerly’, like agre (cf. above, 5), purvam, prak.
14.17 LATE (adv.)
Grk. bye Goth. seipus (adj.) Lith. vélaz NG dpya ON sid, seint aes as Lat, séro Dan. _ sent hSl. pozdé It.  tardi Sw. sent SCr.  kasno, pozno, dockan Fr tard OE sip, late Boh.  pozdé §p. tarde ME late Pol.  pdzno Rum. firziu NE late Russ. pozdno I. mall (adj.) Du. laat Skt. vilambena, vilambat Nr. déidheannach, deire- OHG - spdato Av. a annach (adj.) MHG spate + hwyr, diweddar (adj.) NHG spat
Br diwezat
Words for ‘late’ rest on such notions as ao" ‘behind, after’, or ‘end’. : ee for a few adj. forms marked as ; eo are listed in the adv. forms. ae Tk, oye (NG only in amdye ‘this ae and yés ‘list evening’ and ‘yes- aH ), prob., as orig. ‘afterward’, bt on an *oy, that is *dr-s (cf. ay ad Ward’ beside aaé ‘away from’) be- © Omifey “hah; ye lat, oie ev behind’, ériow ‘backward’ : Bde ob i, In o(p)s-tendere, etc., be- (aha a 8, ab), Ose. op ‘apud’, Grk.
t 0) Waldo. : i Skt. api- ‘to, by’, ete. No, 122f. Boisacg 736.
a Py, adv. to adj. dpyés, ‘slow’
(14.22) and ‘late’. Cf. It. tardi, etc., be- low, and Grk. Bpadis ‘slow’, whence NG Bpadtve ‘be late’ and Bpadv ‘evening’.
2. Lat. saro (sérus adj. > W. hwyr also ‘evening’) : Ir. str ‘long (of time)’, W. hir ‘long’, fr. a root *sé(z)- (cf. comp. Ir. sia, W. hwy fr. *sg-is) seen also in Lat. sétius ‘less’, early ‘later’, Goth. seipus, etc. (below, 4), Skt. sdya- ‘eve- ning’, but orig. meaning of root dub. Walde-P. 2.462. Ernout-M. 933. Falk- Torp 962. Feist 415 tie
It. tardi, Fr. tard, Sp. tarde, fr. Lat. tarde ‘slo
```


## [2026-09-06T16:04:54.353Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 1088 1089 1154 1155; do echo \"### NR=$n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' SYN.txt | head -30; done"
}
```


### [2026-09-06T16:04:56.121Z] TOOL RESULT

```
### NR=1088
oh. and Pol., and a few others of common words applied to different months (e.g. listopad, lit. ‘leaf-falling’, in SCr. ‘October’, Boh., Pol. ‘November’; Boh. kvéten ‘May’ = Pol. kwiecier ‘April’, orig. ‘flower- month’), but, on the whole, great diver- sity.
In general, the month-names are based upon religious festivals (so most of the Grk. and some of the Celtic and Gmc.) or upon some characteristic fea- ture of the weather, vegetation, har- vest, etc.
The enumeration and discussion of these so diverse month-names (even if one chose for the Greek only the Attic or for OHG only those prescribed by Charlemagne) would require so much space that it seems best here to consider only the Lat. names and their spread.
The Lat. names were adj. forms with ménsis ‘month’ understood. Since the Roman year orig. began with March, the numeral derivs. which served is July-December, were Quinctilis ‘fifth for July, Sextilis ‘sixth’ for August (these later replaced by Idlius and Augustus 0 honor of Julius Caesar and Augustus),
aay oR eS Ae et ee ae
i a hen
October, November, December novem-ri-s, *decem-ri-s, f medial mr to mbr,
order beginning with Janu- Fe er eidesoon naisly the names of gods or g dTa RABE. Janus, Mars, Mava, an nel neces arius, the last month of the o ca en ar, yas the ‘month of PUAN NOH, fr. februdre ‘cleanse, purify (Ernout-M. 34], Walde-H. 1.472). Aprilis, prob. f, an Btruscan name based on a short form of Grk. Adpodirn. Benveniste BSL 32.70 ff. Cortsen, Glotia 27.270 ff.
The Roman names have persisted in all the Romance languages. But most of the Rum. forms go back, partly through Slavic, to the later Grk. bor- rowed forms. And elsewhere there are various formal peculiarities, e.g. for tinudrius VLat. cenudrius (> It. gen- naio, Sp. enero); for augustus VLat.
in the new
Digitized by Arya Samaj Foundation Chennai and eGangotri
TIME
1011
agustus (> It., Sp. agosto, Fr. aott); OFr. juignet ‘June’ fr. dim. form, and, by analogy to this, Fr. juillet July’ for OFr. juil, ete.
The Romance names appear in Greece in authors and papyri of the early Ro- man period and eventually prevailed. Hence the NG lit. tavovapios, deSpova- ptos, etc., beside pop. yevapns, odeBapns, etc.
In Celtic, all the Old Irish names were of Lat. origin. In modern Irish those for January, February, March, April, July, and in part June, persist, while the others have been replaced, in part al- ready in Middle Irish, by native terms. In Welsh and Breton the Lat. names are retained for January, February, March, April, May, and August, the others hav- ing native names.
The whole Lat. series is used in all the living Gmc. languages, likewise in Lett. (the older native names being obs.; cf. Miihl.-Endz. 2.616) and Russ.
14.73 YEAR Grk, gros, buavrds Goth. jér, abn, alapbni Lith. metaz NG 0500s, ros ON @ Lett. gads lat. annus Dan. ar ChSl.  léto : pO Sw. dr SCr. godina coal OE géar Boh. rok Ru eg ME ~ yeer Pol. rok ie Pe NE year Russ. god Nir Dliadain Du. jaar Skt. vatsara-, varsa-, ha- V . bliadhain OHG jar yana- Br, lwyddyn MHG jar Ay. yar-, sarad-, aeons NHG jahr OPers. @ard-
There are three groups of cognates,
rig hich is represented by words riches cy least two widely separated e ( the IE family. It is the first
the best ar the order below) that has Word foe tit
### NR=1089
 to reflect a distinctive IE Widespread far. The second is more Various us oe formal group, but with Period it °S Suggesting that in the IE Was more generic, ‘passing
time, period of time’, whence later spe- cialization to ‘year’, ‘season’, ‘spring’, or ‘hour’.
Most of the other words for ‘year’ are also cognate with words for ‘time’ or ‘fixed period of time’, including terms for various seasons of the year and for ‘day’ or ‘hour’.
1. TE *wet-, *wetes-. Walde-P. 1.251.
Grk. éros, fr. widely attested féros;
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
’
—_
Digitized by Arya Samaj Foundation Chennai and eGangotri
1012 SELECTED INDO-EUROPEAN SYNONYMS
Skt. vatsa- (only tri-vatsa- ‘three years old’, otherwise ‘calf’ = ‘yearling’), usu- ally vatsara-; Alb. vjet. Here prob. Lat. vetus ‘old’, ete. (14.15).
2. IE *yé-ro-, *yd-ro-, prob. fr. *ye-, *yo- beside *ya- in Skt. yd- ‘go’, Lith. jott ‘ride’, extension of *ei- ‘go’. Walde- P. 1.105. Falk-Torp 6 f.
Goth. jér, ON ar, OE géar, etc., gen- eral Gmce.; Av. yar- (nom. sg. yara); Grk. wpa ‘period of time’ (14.11), ‘hour’; Boh. jaro, etc. ‘spring’ (14.75).
3. IE *at-no-, perh. fr. *at- in Skt. atait “goes, wanders’ (cf. above, 2). Walde-P. 1.41 f. Ernout-M. 55. Walde- H. 1.51.
Lat. annus (> Romance words); Goth. apn (? only dat. pl. abnam) and at-apbni (only gen. sg. atabnjis) both for évaurés. Here also (with in > kn) Osc. akenet ‘in anno’, Umbr. acnu ‘annos’.
4. Grk. eénavrés, orig. ‘anniversary’ as in Hom. and early inscriptions (Cre- tan law-code, etc.), but also (Hom.-+) simply ‘year’, etym. disputed. Hither fr. phrase él at76 ‘in the same (time)’, for which cf. Boh. tyden, etc. ‘week’, fr. ‘this day’ (14.61); or perh. as orig. ‘sol- stice, resting place of the sun’, deriv. of evabw ‘rest, sleep in’, cpd. of latw ‘rest, sleep, pass the night’. Walde-P. 1.20. Brugmann IF 15.87 ff., 17.319.
Grk. xpévos ‘time’ (14.11) is in pop. NG ‘year’, with new pl. xpév.a and new fem. coll. xpoud ‘space of a year’ (Fr. année). But lit. gros is also generally familiar.
5. Ir. bliadain, NIr. bliadhain, W. blwyddyn, OCorn. blidhenn, Br. dial, blizenn, all fem., fr. the shorter form
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
ee ne
seen in Br. bloaz ‘year’, W. blwydd yen
; r of age’, etym. dub.; perh. orig. mytho- logical conception. Pedersen 1.113 Morris Jones 212 (fantastic; cf, Loth, RC 36.401). Stokes 188.
6. Lith. metai, pl. of metas ‘time’ (14.11), ane
Lett. gads, fr. Russ, god (below), Mihl.-Endz. 1.582.
7. ChSI. léto (= eros, évaurés, xXpbvos, katpés, Gospels, Supr.; also Bépos Pg, Sin.), modern Slavic ‘summer’, rarely also ‘year’ : Sw. dial. lading ‘spring’, Ir. laithe ‘day’. Walde-P. 2.427. Ber- neker 713 f.
SCr. godina (rarely also ‘hour’) = ChSl. godina, Boh. hodina, Pol. godzina ‘hour’ (14.51), fr. ChSI. god%
### NR=1154
tural association between ‘lift? and ‘heavy’ is sufficient). NED s.v. heavy. :
5. Lith. sunkus : sunkti ‘grow heey older Lith. sunkinga ‘pregnant’, fr. *sunk- beside *swenk- in OE aie ‘heavy of movement, slow, sluggis?)
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
eg ye Se ee ar Na aay EL ae
Set er ee
7T Cr
Digitized by Arya Samaj Foundation Chennai and eGangotri
SENSE PERCEPTION
yaG sohwanger ‘pregnant’. Walde-P.
250. sags: Lith. dial. smagus : to carry or pull’, Grk. ndyos ‘toil’,
as ‘Jaborious’, etc. Walde-P. 2.692. po
\ahl.-Endz. 3.928.
1073
6. ChSl. tgztkii, general Slavic (but
Russ. tjazkij in physical sense mostly re- placed by new formation fjazelyj) : ChSI. tegnqti ‘pull’, ON pungr ‘heavy’, etc.
(above, 4). 7. Skt. guru-, Av. gouru-, above, 1.
15.82 LIGHT (in Weight)
rAagpbs (KoDpos) Goth. _ lethts oe Reiss ON lair Lat, levis ; Dan. let it.  leggiero (lieve) Sw. latt rr Léger OE leoht Sp. _legero (leve) ME light Rum. wusor NE light Ir &romm Du. Licht Nir.  éadlrom OHG lihti VW.  ysgafn MHG_ liht(e) Br. skaziv NHG leicht Words for ‘light’ in weight are com-
monly used also for ‘light, nimble’ in movement, and in one case the latter sense is clearly the earlier. But the great majority belong to an inherited group used in both senses.
1. IE *legvh- and *leng’h- in words for ‘light in weight’ and ‘light, quick in movement’. Walde-P. 2.426. Ernout- M. 542 (assuming two orig. different groups, but this not called for). Walde- H. 1.788 f, Falk-Torp 637.
Grk. éhagpds, NG pop. also ddadpés, thagpts; Lat. levis (> It. lieve, Sp. leve; oe ae old tugor with suffix -gor, cf. er 1844; VLat. *levidrius > Fr. 5003-4). a leggiero, Sp. legero. REW sae % oth. lethis, OE léoht, etc.,
me.; Lith. lengvas; ChSI.
Lith. lengvas Lett.  viegls ChSl. Ligitkit SCr. lak Boh. lehky Pol. = lekki Russ. legkij Skt. _—_ laghu- Av. auetee
liguku, etc., general Slavic; Skt. raghu-, laghu- (Av. ragu- ‘quick’); Alb. lehté; here also with different meaning Grk. éehaxts ‘little, paltry’, Ir. laigiu, MW Ulez ‘less’, OHG lungar ‘quick’, etc.
2. Grk. xoidos (rarely of weight, most- ly ‘light, nimble, vain, etc.’), etym.? Boisaecq 504.
3. Ir. &romm, NIr. éadirom, neg. of tromm ‘heavy’ (15.81).
W. ysgafn, Br. skafv, skant : Ir. sca- man ‘lung’ (cf. NE lights ‘lungs’ and the related lung), etym. dub. Walde-P. 2.601. Pedersen 1.76. Stokes 308.
4, Lett. viegls : Lith. viglas or vigrus ‘quick, lively’, Slov. vegati ‘waver’, Skt. vij- ‘gush, heave, be agitated’, etc. Miihl.-Endz. 4.654. Walde-P. 1.234.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
### NR=1155
aSnys Rum. ud, wmed OHG naz, fihti Skt. drdra- oreete Ir. Sliuch MHG naz, viuhte Av. napta- Nir. fliuch NHG _zass, feucht W. guwlyb, lazth
Br. gleb, leiz
It is impossible to draw a sharp line between ‘wet’ and ‘damp’. The dis- tinction according to the degree of wet- ness, a8 in the current use of NE wet and damp, holds also in the main for the Gme. and Balto-Slavic words. But elsewhere this is ignored, and where sev- eral words are in use, as in Latin and the Romance languages, the choice depends on the kind of object described, the ground, a rag, etc., whether naturally wet or made wet, etc., all too diverse and complicated to be noted here.
Apart from the inherited group, the words are connected with others for ‘water’, ‘bathe’, ‘leak’, ‘melt’, ‘vapor’, ‘soften’, ‘mire, filth’(?).
1. TE *weg-. Walde-P. 1.248. Er- nout-M. 1123. REW 4233, 9030.
Grk. iypés; Lat. amidus, and (by as- sociation with humus ‘earth’) hiimidus (> It. umido, Rum. umed, Fr. humide, Sp. himedo), and tvidus, whence tidus (> Rum. ud); ON vokr.
2. Grk. (Hom.) véris, Att. vorepés, beside vorts ‘moisture’, vé7os ‘south wind’ (= ‘damp’), prob. : Arm. nay ‘wet, liquid’, Lat. natare ‘swim’, fr. an extension of the root *(s)na- in Grk. vaxw, Lat. nare (cf. Umbr. veskla snata ‘vessels for liquids’), Skt. sna- ‘swim’, etc. Walde-P. 2.692 f.
NG Speyuévos, pple. of Bpexw ‘wet, moisten’, intr. ‘rain’, class. Grk. ‘wet,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
steep’, pass. ‘get wet, be rained on): Bpoxy ‘rain’, Lett. mdarga ‘gentle rain’, etc. Walde P. 1.280.
3. Lat. madidus, fr. madére ‘be Wet, drip with’ : Grk. padéw ‘be moist, fall off (of hair)’, Ir. maidim ‘break out, go to pieces’, etc. Walde-P. 2.231. Ernout- M. 579. Walde-H. 2.6 f.
It. bagnato, pple. of bagnare ‘bathe, wet, moisten’ (VLat. balneare fr. balnea, earlier balineum ‘bath’, fr. Grk. Bada- vetoy). Trnout-M. 101. REW 913.
Fr. mouillé, Sp. mojado, pple. of Fr. mouiller, Sp. mojar ‘wet, moisten’, fr. a VLat. *mollidre, fr. mollis ‘soft’. REW 5646.
Fr. moite, OF r. moiste (> ME moyste,
NE moist), prob. fr. “muscidus for Lat. miucidus ‘moldy’ blended with musteus ‘musty’. REW 5711. Gamillscheg 618. Bloch 2.71. _ 4. In. fliuch, W. gwlyb, MBr. gloeb, Br. gleb, perh. : Lat. liquidus ‘liquid’, etc., root *wleik-(?). Walde-P. 2.397. Pe- dersen 1.60. Stokes 285. Walde-H. 1.812. ;
W. Ilaith, Br. leiz: W. dad-laith ‘thaw’, Ir. legaim ‘dissolve, melt’, ON leka ‘leak’, OF leccan ‘moisten, wet’, ete. Walde-P. 2.422 f.
```


## [2026-09-06T16:05:04.057Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"COLD\" SYN.txt | head; echo ===; grep -n \"sarad-\\|sar\\^ta\\|sarata\" SYN.txt | head -20"
}
```


### [2026-09-06T16:05:04.111Z] TOOL RESULT

```
Exit code 1
27293:COLD
(eval):1: == not found
```


## [2026-09-06T16:05:06.247Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '27270,27400p' SYN.txt"
}
```


### [2026-09-06T16:05:06.315Z] TOOL RESULT

```
Ir. t@, pl. téit (pple. *tepent-), NIr. te; W. twym, Br. tomm, OCorn. toim (*tepes- mo-); ChSl. toplit, SCr. topao, Boh. teply, Pol. ciepty, Russ. teplyj; Skt., Av. tapta- (pple. of tap- ‘be hot, warm’); Lat. tepi- dus ‘lukewarm, tepid’, tepére ‘be tepid’, etc. Here also W. cynnes fr. *cyn-tes, epd. of tes, Ir. tess ‘heat’ (*teps-tu). Morris Jones 63.
3. IE *el-, prob. the same ultimately as in words for ‘cold’, Lith. Saltas, etc. Walde-P. 1.429. Ernout-M. 134. Walde- H. 1137.
Lat. calidus (> borrowed Sp. cdlido), caldus (>It. caldo, Fr. chaud, Rum. cald), with vb. calére ‘be warm’ (> OSp. caler, deriv. caliente ‘hot’); Lith. Siltas, Lett. silis, with vb. Lith. Silti, Lett. silt ‘grow warm’; fr. an extended form of the root prob. ON Aly ‘warmth’, hler ‘warm, mild’ (of weather), OE hleowe ‘comfort- able, sheltered’, OHG lao, NHG lau ‘tepid’, etc,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
1078 SELECTED INDO-EUROPEAN SYNONYMS
4, NG feorés, in class. Grk. ‘boiled, boiling hot’, fr. ¢éw ‘boil’ (10.31).
5. Ir. té, W. twym, Br. tomm, W. cyn- nes, above, 2.
W. brwd: berwi, Ir. berbaim, etc. ‘boil’. Walde-P. 2.168.
W. poeth = Br. poaz ‘cooked, burn- ing’, Lat. coctus ‘cooked’, pples. of W. pobi, Lat. coquere ‘cook’, etc. Walde-P. 217.
6. ON heitr, OF hat, OHG heiz, etc., general Gmc., fr. *kai-d-, beside *kaz-t- in Lith. katsti, Lett. kaist ‘become hot’,
15.86 Grk. oxpds Goth. kalds NG Kptos ON kaldr Lat.  frigidus, gelidus Dan. _ kold It. freddo Sw. kall Fr. froid OE ceald Sp. Jrio ME cold Rum. rece, friguros NE cold Ir. tar Du. koud Nir. = fuar OHG alt W. oer MHG kalt Br. yen NHG kalt
A distinction similar to that of ‘hot’ and ‘warm’ is partially observed, but here ignored in the list. That is, be- side the generic words for ‘cold’, there are others for ‘moderately cold’, ‘cool’, usually with the feeling of pleasant con- trast to excessive heat. These may be cognate with those for ‘cold’, as NE cool, NHG kihl, etc., or they may be words which mean literally ‘fresh’, as It. fresco, Fr. frais, etc., similarly NG Spocepés in class. Grk. ‘dewy, fresh’ : dpdcos, NG dpoora ‘dew’. Again, NE chilly, also cognate with cold, is ‘moderately but dis- agreeably cold’, and NG Wuxpés (in class. Grk. ‘cold’) is now used in just this sense, or else figuratively.
Apart from inherited groups, there are other words connected with those for ‘ice, frost’, ‘stiffness’ (?), ‘blow’.
1. IE *fel-, prob. the same root as in
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
etc., and *kai- in OHG hei, gehei Walde-P. 1.326 f. Falk-Torp 388
7. Lith. kargtas, Lett. karsts, besid Lett. karst ‘become hot’, fr. the root si Lith. kurtt, Lett. kurt ‘heat’, Ch}, kurit; se ‘smoke’, Goth. hauri ‘coals’, ON ; ‘fire’. Walde-P. 1.418.
8. SCr. vrué, and vreo : vreti, Choy viréti ‘boil’, Lith. virti ‘bubble up, boil’ etc, Walde-P. 1.269. Miklosich 381, ”
9. Skt. usna-, fr. ws- ‘burn’ : Grk. ebeo ‘singe’, Lat. drere ‘burn’. Walde-P. ible
‘heat,
.
hyrr
COLD
Lith.  Saltas
Lett. auksts, salts
ChSl.  studenii
SCr. _hladan, studen Boh.  studeny
Pol. zimny
Russ. cholodnyj (studenyj) Skt. ¢ila-, cigira-, hima- Av. aota-, sarata-
words for ‘hot’, Lat. calidus, etc. See 15.85.
Lith. galtas, Lett. salts (with vbs. Lith. galli, Lett. salt ‘freeze’); Skt. (with re- duplication) ¢gigira-, Av. sarata-, N Pers. sard, also in Av. sara-6d- ‘bringing cold’; Osset. sald sb. ‘cold’.
2. IE *gel-. Walde-P. 1.622, Er nout-M. 412. Walde-H. 1.585 f. Falk- Torp 560 f.
Lat. gelidus (with sb. gelu ‘cold, frost’, vb. gelare ‘freeze’); Goth. kalds, Or ceald, etc., general Gme. (orig. pple. wy ON kala ‘freeze’, OE calan ‘become cold’, whence also sbs. ON kuldi, OB ceald, OHG calit, etc.), here also sb. OE cele, ciele (> NE chill, whence adj. chilly), with ablaut OE col, NE cool, OHG kuoli, NHG kil ‘cool’.
3. Grk. yoxpss (NG ‘chilly’ or fig.), with sb. ydxos ‘cold, coolness’ : ¥ox#
eS ae 5 aad > bel bl ot Pe
1 off’, yuxa W refresh, C00 , pester Per” Boisaca 1079.
SENSE PERCEPTION
Digitized by Arya Samaj Foundation Chennai and eGangotri
1079
Br. yen : W. iaen ‘sheet of ice, gla- cier’, ia, Ir. aig ‘ice’, ON jaki ‘piece of
ipreath, SP fr, sb. Kpbos ‘cold’ (xaver | ice’, etc. Walde-P. 1.206. NG wine) in class. Grk. ‘icy cold, 6. Gme. words, above, 2. aad Gee, crust’, OE 7. Lith. Salias, Lett. salts, above, 1.
h)roso : Oe sacl Lett. kruvesis o]
‘ogen dung in the road’, etc. ralde-P- 1.479. Boisacq 522. Hat. fragidus (> Sp. frto), Viet. “indus (> It. freddo, Fr. froid), ed frigus ‘cold’ (> Rum. frig); ae ite frigorosus (> Rum. friguros, ote,), vb. frigere ‘be cold, freeze : Grk. sos frost’, prvéw ‘shiver (with cold), der. Walde-P. 2.705. Ernout-M. 390, Walde-H. 1.547. REW 3512, 3514. Rum, rece, fr. Lat. recéns ‘fresh, re- ent, young’, with development fr. ‘fresh’ through ‘cool’. REW 7109. 5, Ir. war, NIr. fuar, W. oer, OCorn. oir, cf. Gall. Ogron name of a month (toug-ro-), beside sb. Ir. dacht (*oug-to-) : Am, oie ‘cold’, ucanam ‘grow cold’, all prob, fr. an extension of a root *ew- seen also in Lett. auksts ‘cold’, Lith. aust ‘grow cool’, and in Av. aota- ‘cold’, sb. aogar-, Skt. tidhar- ‘cold’, further root connections (as with Grk. anus, Skt. vd- ‘blow’, etc. ; cf. above, Grk. pixos : Poxw) more doubtful. Walde-P. 1.222. Pers- a 10f. Pedersen 1.103. Lé- » Wort. u. Sach. 11.54.
Lett. auksts, above, 5.
8. ChSl. student, SCr. studen, Boh. studeny, Russ. studenyj, with sb. studi ‘cold’, vb. stynati ‘become cooler’, fr. *steu-d-, beside *steu-g- in Grk. ortyes ‘chill, frost’, oriyos ‘abomination’, orv- yew ‘abhor’, etc., fr. *steu- in Skt. ghrta- stavas ‘drops of melted butter’. The pri- mary meaning of the root was perh. ‘con- geal, become stiff’. Walde-P. 2.620.
SCr. hladan, Russ. cholodnyj (Boh. chladny, Pol. chtodny ‘cool’), with sbs. Russ. cholod ‘cold’, ChSl. chladi% ‘cool- ness’, etc.,etym. dub. Berneker 393.
Pol. zimny beside sb. zimno, fr. zima ‘winter’ (14.74). Cf. Boh. zima, used also as ‘cold’ sb., and so ChSl. zima in Gospels, Jn. 18.18; likewise Skt. hima- as ‘cold’ sb. and adj.
9. Skt. gita-, ¢itila-: gyd- ‘freeze, congeal’, outside connections dub. Uh- lenbeck 318.
Skt. cicira-, Av. sarata-, above, 1.
Skt. hima-, see under Pol. zimny, above, 8.
Av. aota-, see under Ir. war, above, 5.
s 15.87 CLEAN kabapd XBaphs Goth. hrains Lith. Svarus, Gystas mundus Aas ON hreinn Lett. firs, glits Bulilo, netio Dan. ren ChSl.  Sistit Propre, net Sw. ren SCr. ist limpig OE cl@ne Boh. Gisty curat ME lene Pol. czysty glan NE clean Russ. éistyj glan Du. rein, zuiver Skt.  cuddha- glan OHG  reini, subar Av. ‘ ue MHG reine, siiber
NHG rein, sauber
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
———
Digitized by Arya Samaj Foundation Chennai and eGangotri
1080 SELECTED INDO-EUROPEAN SYNONYMS
Words for ‘clean’ and ‘dirty’, though these notions are by no means exclusive- ly distinguished by the sense of touch (more often by smell or sight), are con- veniently introduced here. Many of the words for ‘clean’ are the same that are used for ‘pure, unmixed’, and in sey- eral of these this is clearly the earlier notion. Others are of too diverse or doubtful origin for summary.
1. Grk. xadapés, etym.? Walde-P. 1.868. Boisacq 389.
NG pop. zaorpixds, with mdaorpa ‘cleanliness’, macrpebw ‘cleanse’, Byz. omacTpikos, omaoTpa, omactpetw, etym. dub., perh. first ordorpa fr. craw ‘draw, carry off’. Otherwise (fr. oraprov ‘Spanish broom’, the plant) Koraes, “Araxra 1.288 f., Hatzidakis, Mec. 1.327.
2. Lat. mundus (> It. mondo ‘peeled, cleaned’, Sp. mondo ‘neat, pure’), perh. as orig. ‘washed’ fr. *mudnos : Ch&l. myti ‘wash’, MLG maiiten ‘wash the face’, OHG muzzan ‘clean, adorn’, Grk. pbdos ‘dampness’, etc. Walde-P. 2.250 f.
Lat. purus : Skt. pu- ‘cleanse, purify’, OHG fowen ‘sift, clean grain’, etc., root *peu-. Walde-P. 2.18. Ernout-M. 826.
It. pulito, pple. of pulire ‘cleanse’, fr. Lat. polire ‘smooth, polish’.
It. netto, Fr. net (OF r. neit, net > ME neate, nete ‘clean, pure, bright’, NE neat), fr. Lat. nitidus ‘bright, shining, polished’ (15.57). REW 5929.
Fr. propre, in sense ‘clean’ from perh. 16th cent., earlier ‘correctly arranged’ fr. ‘having necessary qualities, proper’, fr. Lat. proprius ‘own, special, proper’. Bloch 2.188.
Sp. limpio, fr. Lat. limpidus ‘clear, transparent’ also late ‘pure, clean’ (1. panis, Cael. Aur.). REW 5056.
Rum. curat, fr. Lat. cdlatus, pple. of célare ‘filter, purify’. REW 2035a. Puseariu 454.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
3. In, W. glan : Ir. gel ‘whi (15.64). Walde-P. 1.624.
Br. net, neat, fr. Fr. net.
4. Goth. hrains, ON hreinn, Dan Sw. ren, OHG (h)reini, MHG a NHG, Du. rein; in Rhine Frank, and in Swiss ‘finely ground or sifted’; hence perh. fr. the root of Grk. kptvw ‘choose decide, judge’, xpiuvov ‘coarse barley meal’, Lat. cernere ‘separate, sift, dis- tinguish’, cribrum, OE hridder ‘sieve’, etc. Walde-P. 2.585. Falk-Torp 89, Kuge-G. 477.
OE cléne, ME clene, NE clean (OHG kleint ‘shining, fine’, etc., NHG klein ‘small’) prob.:Grk. -yAjvea ‘bright things, trinkets, stars’, yyy ‘pupil of the eye’, etc. (cf. 12.56), with develop- ment of ‘bright’ to ‘clean’ as in Fr. net, etc. (above, 2). Walde-P. 1.623.
OHG sitbar, subiri, MHG saber, si- ver, NHG sauber, OS stbar, Du. zuiver (OE sifre ‘sober, temperate, pure’), fr. Lat. sdbrius ‘sober, moderate, temper- ate’. Weigand-H. 2.655. Franck-v. W. 829.
5. Lith. varus, and vb. svarintt ‘cleanse’, etym.? Walde 1.462.
Lith. éystas (formerly the usual word but now being discarded in favor of §varus; NSB s.v.), fr. Slavic (below, 6).
Lett. tirs : Lith. tyrus, tyras ‘pure, wn- mixed’, further connection dub. (Mihl.- Endz. 4.204: Lith. tyras, tyré ‘pap, pulp’, Lett. drelis ‘swamp’, etc., but se- mantically difficult.)
Lett. glits, perh. : glits ‘slippery, soft, Lith. glitus ‘viscous’, Lett. glist ‘get slimy’, etc. Walde-P. 1.620. Muhl- Endz. 1.627. ;
6. ChSl. distt, ete., general Slavic with vb. distiti ‘cleanse’ : OPruss. a tan (ace.) ‘clean’, skistint ‘cleanse’, Lit skystas ‘liquid, fluid’, Lett. sk’asts thin (of liquids), also ‘clean, chaste root of ChSl. céditi ‘strain, filter
te’, ete,
” fr, the ? (ete,
Bh be ES geen
\ 1th. skiesti ‘adulterate, al eee ee OHG heitar ‘bright, pe ‘brightness (of the i ‘light, shape, form’, etc. (Dis Berneker 157 f.
sky, Walde
lous, loudour
Words for ‘dirty, soiled’ are mostly connected with sbs. for ‘dirt, filth’, ‘mud’, ‘excrement’, ‘snot’, ‘stench’, etc. Several are from ‘dark-colored, black’. Some are neg. cpds. of those for ‘clean’. The majority of these lastare used mainly with reference to moral or ritualistic un- cleanliness. This is the only use occur- ting in the Gospels, where axé@apros is tendered by Lat. immundus, Goth. un- hrains, OE uncl&éne, OHG unreini (Otfr.), unsabiri (Tat.), ChSl. nedisti. However, these words are entered in the list, and some of them are also used in a less restricted sense, as frequently Lat. aed Sometimes ME unclene, NE aa (NED s.v. 4), and esp. the i Ae Including NIcel. dhreinn. Chs}, i purapés, fr. birros filth, dirt? : bilein pu ‘wound’ (in modern Slavic Titian, ad epeb, crust, etc.’), root con- NG ee ‘flow’?).- Walde-P. ios a ye: ies ‘soil’, pple. Aepw- St ’ a4 class. Grk. ddepds ‘tur-
é 7 ©\cpov" BopBop&des, rerapary- deriv. of : 6és ‘ink
» but formed after or
SENSE PERCEPTION
Digitized by Arya Samaj Foundation Chennai and eGangotri
1081
7. Skt. cuddha-, pple. of gudh- ‘purify,
cleanse’, fr. *ku-dh- beside *fu-bh- in cubh- ‘shine’?). Walde-P. 1.368.
‘adorn, beautify’ (root *keu-
15.88 DIRTY, SOILED ¥ Goth. wnhrains Lith. purvinas, suterstas Grk. purapsy ee age ON saurigr, uhreinn Lett. netirs, melns NG depbsy Dra ur, us Dan.  smudsig, snavset, uren ChSl. netistic Game squalidus, Sw. smutsig, oren SCr. — prijav [at 80" ae immundus OE fal, horig, uncl@ne — Boh.  Spinavy Ne sudicio ME unclene, foul, hori, Pol. brudny ; ET SS UntOr A filthi — Russ. grjaznyj bey a NE dirty, soiled Skt.  malina-, etc. ; ae Du. vuil, smerig Av. ahita- Rum. eh OHG  unreini, unstibar Nir salach MHG unreine, unsiber, hor- * bdr, brwnt Wee: re NHG = schmutzig, schmierig
influenced by the more common @ode- pos ‘muddy, turbid’, esp. of water, etc.. but also ‘dirty’ (cf. téare vite Porepav adivbov, Theocr. 16.62), deriv. of 86dos ‘mud, dirt’.
NG 8Bpwptxos, properly ‘stinking’ (15.26), used also for ‘dirty’ (the laun- dress used to come for ré Bpwpixa).
NG dacrpos, neg. : racrpixds ‘clean’ (15.87).
2. Lat. sordidus, with sordére ‘be dirty’, sordés ‘dirt, filth’ : Goth. swarts ‘black’, etc. (15.65). Walde-P. 2.585. Ernout-M. 958.
Lat. squalidus, and rare (Enn.) squa- lus, with sbs. squalés, squalor ‘filth’, vb. squalére ‘be filthy’, properly of dirt and filth consisting of stiff or rough incrusta- tions, scales, etc., etym.? Walde-P. 1.441. Ernout-M. 970.
Lat. spurcus (> It. sporco), etym. dub. (cf. spurius ‘bastard’?). Ernout-M. 969 f.
Lat. immundus, neg. cpd. of mundus ‘clean’ (15.87).
It. sudicio, Sp. sucio, fr. Lat. sticidus ‘sappy, juicy’. REW 8414.
Fr. sale, fr. OHG salo, MHG sal
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
1082 SELECTED INDO-EUROPEAN SYNONYMS
‘dark-colored, turbid, dirty’: OF salu ‘dark-colored’ (cf. Ir. salach ‘dirty’, etc., below). REW 7547.
Fr. malpropre (esp. of persons ‘habit- ually dirty’), epd. of mal ‘bad’ with neg. force and propre ‘clean’ (15.87).
Rum. murdar, fr. Turk. murdar ‘dirty’, this fr. Pers. murdar ‘corpse’ (: murdan ‘die’, Av. mar-, etc.). Titkin 1022. Lokotsch 1516. Horn 973.
3. Ir. salach, fr. sal ‘dirt, filth’ : OHG salo ‘dark-colored, turbid, dirty’, OE salu ‘dark-colored’ (NE sallow), etc. Walde-P. 2.453.
W. budr, with vb. budro ‘soil’, MIr. buaidrim ‘roil up, confuse’, prob. : OF cewead, OHG quat, NHG kot ‘dung, filth’, etc. (4.66). Walde-P. 1.696.
W. brwni, etym.?
Br. lows, same word as louz, MBr. louge ‘badger’, fr. (or conversely) Fr. dial. louse ‘badger’ and ‘trickery’, etc., hence orig. an opprobrious term. Er- nault, RC 14.287, Glossaire 377.
Br. loudour, cf. W. lludedic ‘muddy’ : Ir. loth ‘dirt’, Lat. lutwm ‘mud’, Grk. \dua ‘washings, filth’, ete. Walde-P. 2.406. Stokes 250.
4. Goth. unhrains, ON whreinn, Dan. uren, Sw. oren, OHG un(h)reini, MHG unreine (NHG unrein), likewise OB un- cléne, ME unclene (NE unclean), and OHG unsibar, unsibiri, MHG unsiber (NHG unsauber), neg. epds. of words for ‘clean’ (on use see above), and common today in the physical sense only in Scandinavian.
ON saurigr, saurugr, also saurligr, fr. saurr ‘mud, dirt, excrements’, this prob. : ON sdrr, OE siir, etc. ‘sour’ (15.38). Walde-P. 1.469, 518. Falk-Torp 1236.
Dan. snavset, and vb. snavse, fr. snavs ‘dirt, muck’, Sw. dial. snafs, with vb. snaffsa ‘spill’, perh. = snaffsa ‘snap,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
bite’. Orig. meaning of snavs food, waste’. Falk-Torp 1091,
OE ful, ME foul (NE foul a to NED not now used in this se out admixture of the notion ‘putrid stinking’), Du. vuil (the usual term for ‘dirty’), orig. ‘putrid, stinking’ (15.26) Hence sb. OE fylp ‘rottenness, filth’. with adj. ME filthi (NE jilthy, in earlier use without the present strong connota- tion, ef. NED s.v.).
OE horig, ME hori (NE dial. howry), OHG horawig(?), MHG horwec, fr. horu, OHG horo ‘dirt, filth’ = ON horr ‘snot? root connection dub. NED gy. hory, horry. Falk-Torp 936. Walde-P. 1.409,
NE dirty, fr. dirt, older and ME drit ‘filth, excrement’ (4.66). Cf. ON shi- linn, with Dan. skiden, and NIcel. skitu- gur pop. terms for ‘dirty’, fr. the well- known Gmc. word for ‘excrement’,
NE soiled, but in ME (Ancr. R. sui- lede) mostly ‘defiled’, fr. vb. soil, ME suile(n) ‘defile, pollute’, OF r. suzllier, NFr. sowiller ‘stain, befoul’, fr. VLat. *suculdre, deriv. of suculus, dim. of sts ‘hog’. REW 8418. Bloch 2.287. NED S.v.
Du. smerig, NHG schmierig, properly ‘sreasy’, fr. Du. smeer, NHG schmiere ‘grease’. Franck-v. W. 625. Weigand- H. 751.
NHG schmutzig, sb. schmutz (> Dan. smudsig, Sw. smutsig, sbs. Dan. smuds, Sw. smuts), MHG smuz = NE smut, etc., prob. : Ir. smiid ‘smoke, steam’, root connection dub. Walde-P. 2.251. Falk-Torp 1083.
5. Lith. purvinas, fr. purvas ‘mud, filth’ (1.214). ee Lith. suterStas, fr. (su)terstt soil, befoul’, prob. : Lat. stercus ‘dung, a crement’, W. troeth ‘lye, urine’, troelht ‘urinate’, etc. Walde-P. 2.641.
‘refuse of
ccording nse with-
—_oeo—
Lett. melns ‘black’ 2 Of, NEB and
```


## [2026-09-06T16:05:15.740Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"arad-\\|Oard\\|@ard\\|Gard-\" SYN.txt | head -20"
}
```


### [2026-09-06T16:05:15.792Z] TOOL RESULT

```
6471:Skt. hrd-, hrdaya- Av. zarad-
6472:ChSl. sridice, etc., general Slavic; Arm. sirt; here also Skt. Ard-, hrdaya-, Av. zarad-, but with init. as if fr. IE gh, due to a blend with some other word; Hitt. kartis (Sturtevant, Hitt. Gram. 106).
6999:Nir. _ broimnighim OHG ferzan Ay. parad-
12307:Skt. urvarad- : Av. urvara- ‘plant’, under Grk. apoupa, above, 2.
22404:(= Increase in Size) Grk.  abkdvopat Goth. wahsjan Lith.  augti NG Heyaddvw, attavw ON vaza Lett.  augt Lat. _créscere, augéscere Dan.  vokse ChSl.  rasti It. crescere Sw. vdxa SCr. —_rasti Fr. crottre OE weazan Boh. riisti Sp. crecer ME _waze, growe Pol. rosnqé Rum. cresle NE grow Russ. rasti Ir. Gsaim, forbiur Du. —_groeien, wassen Skt.  urdh-, rudh-, uks- Nir. fasaim OHG wahsan Ay. varad-, rud-, uxs- W. tyfu MHG wahsen Br. kreski NHG  wachsen
22419:7. Skt. vrdh- act. and caus. ‘make grow or thrive, elevate’, mid. ‘grow, thrive’, Av. varad- act. (and mid.) ‘make grow or thrive, increase’, mid. and pass. ‘grow, thrive’ : ardhva- ‘up- ward, upright, raised, elevated’, Grk. dps ‘upright, straight’, Slavic roditi ‘bear’. Walde-P. 1.289.
22873:Grk. 6p66s (fopfo-, *ropO¢o-), orig. and in actual use mostly ‘upright, ver- tically straight’ : Skt. ardhva- ‘upright, raised’, urdh- ‘increase’, mid. ‘grow’, Av. varad- ‘increase’, etc. Walde-P. 1.289. Boisacq 711.
24923:Grk.  apxopat; dpxy Goth. duginnan, ana-, du- Lith. pradéti; pradzia NG épxlifw, apxwd; dpxn slodjan; anasto- Lett. (ée)sakt; (ie)sakums Lat.  incipere, coepere; ini- deins, frumisti ChSl. — naceti; nagelo, natelii- lium, principium ON hefja (upp), byrja; kit It. incominciare, princi- upphaf SCr. poteti; potetak ptare; principio Dan.  begynde; begyndelse Boh. zaéiti, potiti; zaédtek Fr. commencer; com- Sw. bérja, begynna; bér- potdtek Z mencement, début jan, begynnelse Pol. zaczq¢, wszczq¢; poc- Sp. empezar, comenzar; OE onginnan; angin, zqlek principio r fruma, frymp Russ. naéat’; natalo Rum. ‘ncepe; inceput ME (a-, be-)ginne, com- Skt. Grabh-; Grambha- Tr. doinscanna; tossach, mence; beginnunge, Av. aiwigarad-; fratauru- tuus commencement na-, aiwigali- Nir. tosnuighim; tosach NE begin, commence; be- (tits) ginning commence- W. dechreu; dechreuad ment Br. deraoui, derou Du. beginnen, aanvangen; aanvang, begin OHG biginnan, anafahan; anagin, anafang MHG beginnen, anvahen; anvanc, begin, ane- gin NHG anfangen, beginnen;
24951:Av. aiwigarad-, lit. ‘go toward’, esp. ‘begin’ a hymn or some part of the ritu-
24954:978 al, epd. of garad- : Lat. gradi ‘step, go’, | etc. Cf. Lat. ingredt ‘enter upon’ and
25709:14.73 YEAR Grk, gros, buavrds Goth. jér, abn, alapbni Lith. metaz NG 0500s, ros ON @ Lett. gads lat. annus Dan. ar ChSl.  léto : pO Sw. dr SCr. godina coal OE géar Boh. rok Ru eg ME ~ yeer Pol. rok ie Pe NE year Russ. god Nir Dliadain Du. jaar Skt. vatsara-, varsa-, ha- V . bliadhain OHG jar yana- Br, lwyddyn MHG jar Ay. yar-, sarad-, aeons NHG jahr OPers. @ard-
25743:Av. sarad-, OPers. @ard- (certainly ‘year’, not ‘manner’ as Barth. 1566), NPers. sal ‘year’, Osset. sdrd ‘summer" : Skt. carad- ‘autumn’, also ‘year’ in RY, etc., perh. as orig. ‘warm season’ f Lith. Silius ‘August’, silti ‘grow warm’, Lat. calére ‘be warm’, etc. Wood, AJPh, 21.182. Walde-P. 1.429. Walde- H. 1.137.
25750:1013 14.76 14.77 SUMMER AUTUMN Oépos POtvérwpov xadoxalpt P0tvorwpo aestas aulumnus estate aulunno été automne verano, estio otono vara toamnd sam, samrad fog(a)mar samhradh foghmhar haf hydref (cynhaeaf) haziv diskar-amzer, dilost-hanv asans Re sumar haust sommer efteraar (h¢st) sommar hést sumor herfest sumer hervest, autum(p)ne summer autumn, fall zomer herfst sumar herbist sumer herb(e)st sommer herbst vasara ruduo vasara rudens Zetva, léto jesent ljeto jesen. leto podzim, jesen lato jester leto osen’ grisma-, nidagha- ¢arad- ham-
25826:7. Skt. garad- (also ‘year’, RV, etc.) = Av. sarad-, OPers. @ard- ‘year’ (14.78).
29407:Av. aradra-, perh. : arad-, arad- « mote, advance, make thrive’, Sk¢ ‘thrive, prosper’, radh-
```


## [2026-09-06T16:05:25.085Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"sar\\?ta\\|sarəta\\|sarota\\|sarata\" BRT.txt | head -20; echo \"=== 1566 area\"; grep -n \"1566\\|1565\\|1567\" BRT.txt | head -20"
}
```


### [2026-09-06T16:05:25.150Z] TOOL RESULT

```
2466:jiaiti  oAmli  avasata  .  .  zaraiusirö  V.it).   aHbyo  .  .  Y.j2. i  f.;   —  yaHiyascd  tsi  ä ";  —  vTvaahä  mqm  paoirys  ■  .\yalcä    asiijiö    a  (sd.)    aah?n    Y.jp, i;  —
2483:—  para  ahtnSi  .  .  cinasti  ya%a  ^aitavS x'aitäifm  (sA)  Y.20.  i,  3)  auf  ein Relativum  als  dessen  Korrelat;  a)  adjek- tivisch: ahmili  naemäi  uzjasäitt  mtiro  .. yahtnai  naimanqm  mOiröJruxl  nai-ia  .  . paiti.päiti  Yt  /0. 1 9 ;  —  aÄ  . .  alsam  narqm yöi  kacahi  Yt/7.6;  —  mffirpm  ahyä *madahyä  (sd.)  yä  .  .  uräpayHntl  (sd.)  Y. Jt^.io;  —  Svat  A3  nü  ankuyaite  .  .  cvat ahmäi  naire  m^tm  aahat  yÖ  .  .  frama- r,UU\.4-4t;  Y.62. 1,  Yt.  10.137;  —  "^^ dussar^hahe  . .  manö  3at  ahe  .  .  mane  yö ml  dussatahö  hutaite  Y./0.12  (s.b);  — ipas  vloaSa  .  ./rS  *aAhe  vXsaiti  mt>rö ..
2768:mit  paiti  i)  'streben  nach  — ,  begeh- ren': a)  mit  Akk,:  tafca  yä  kasu.xratul ,  masyöjcrdkwqm  (sd.)  nöit  paitiSaiti  V.  7, I  59.  b)  mit  Gen.:  s.  AbsoL  a)  'sich befleissigen,  betätigen',  mit  Akk.'>:  paiti- sata  (2P.)  mazdayasna  sraoiahe  a/yeke '  yasmm  Y.  37. 13;  —  staota  yesnya  yaza- maide  .  .  dadräna  paitHäna  paitiima- .  r^mna  Y.  55. 6 ;  —  six/anlfm  sa/ayaitt^m paitisant^m  Vyt52,  *P- /?  (wo  °Ä«- ,ljm)'i^.  3)  'erfahren,  erleben':  iaia lUli  (sd.)  *paitUäma  '*>  frya  paiti  tanvi ,  Yt.  i7, 10.  a)  bes. 'zur  Vergeltung,  zum Dank  erfahren,  empfangen':  kä>:ä..kä%3 .  (sd.)  saidyäi  yS  I  paitisift  Y.44.2 ; — ya^a ahmya  amtsa  spmta  sraoläoa  aiyäoa paitisqn  . .  yasnqsca  vahmqsca  Y.  öb.6.
3292:•  j.  'aSätAdv.  i)  zeithch  'darauf,  dann'; a)  an  der  Spitze  des  Satz(teil)es:  a'j-  uit't /rarasata  asi/Yt.iy.21;  18,  14.S4,  '0-A^y 47i  49t  F-7;  —  "''"  anyaäqm  ra'i-wqm /•aiti.ä'jaydil(sii.)N.  <^^;  Yt.  1. 30.  a)  im Nachsatz:  y^  . .  jainti  . .  yaw  tat . .  para.- baraiti  dasa  isd,)  a-i"  paili  a/sjlid.)  tiia- yat  V.  (_j.io.  b)  enkliL  hinter  dem ersten  Wort  (bez.  Hochton)  des  SaU(teil)es: vacö  paoirTm  mi'ir^m  k>r3ttaoiti   *sasiB.-
3294:mazd  ao'  /ramar?zaiti  *saste.mazö  a<i° antan  urvaitya  (sd.)  fradd^aiti  V.  4.3; 3f.*,  N.  7/,  Vd.  20;  —  caiwlrö  «6°  ahu- tum  vairim  fiasrsvayäit  V.i8.i,y,  —  us paili  an'  histaiti  . .  iistryd  . .  us  ao'  ÄtstJt satavaesö  Yt  1^.32;  23;  —  *uzdän»m  hl .  rto"    ktrinaot  V.  6.50;  /J.30.  2)    an-
4273:•  j.  anapyüxSa-  Adj.  (fem.  '"oä-)  'wobei kein  Hineinsprechen,  Einschieben  von Worten  stattfindet':  gil'ianqm  'oanqm anapisatanqmsrävayamnanqm"\oaGi^ils, die  ohne  Einschicbung  und  Versetzung von  Worten  hergesagt  werden"  Y.  7(j.  5; 13.3;  —  tisrB  paoiryS  .  .  'o5  anapUütS Vr.  13.  I,  3;  —  Hsra  paoirya  ,  .  'oa anapisäia  YT.13.2,  3;  3.
5368:"ka''  ski^  avam  *''ufrasatam  aparsam  Bh. /.8;  —  pasavJ'  karJ'  'ka"  abavJ'  Bh. /.  10.
5737:•  j.  asah-  n.  'Ort,  Stätte,  Platz,  Raum': y8  anyeAe  *'saAya  (LS.)  bansma  */ra- stff^ie^.ioi; — äaire  "saAi  razaaiam(sd.) V.Ä97;  —  atfffi  daoam  °s/f  rämsMäitTm (sd.)  ndil  kuäalJäiim'V.i.i;  iPUZ.,  Vyt. 2'j(?);  —  xrüma  'sl6rs{3is  Subj.)  frasinia danunam  YL  13.  ^S;  —yatca  aakat  %wyqs- brnalrva  'sauham  V.2.23;  —  yäi^a  °sS mai^animca  atmisilSe  äaiära  (sd.)  Yt.  13. 67.  a)  sonst  neben  sSihra-.  paoirlm •sanham^a  Sstiranamca  vakishm  frii' "iwtnspm  .  .  airyatDtn  vaSjB  "als  die  erst- beste der  Stätten  undWohnplätze.."  V.  I.a; Y.  /.  lÖ;  —  hpnti  atiyäscii  °s3sca  sSi^rSsca irirasla..  V.J.  20;  Y.  3.16,  S.  7.28,  2.28; —  äat . .  vazaite  väiS . .  avi  'sä  avi  /gi'irS ai-i  karh'ä  yäis  hapta  Yt  Ä  3  3 ;  —  para  nU ahntät  h<üa  'sarihal^a  ^t^räatca  axslat .,  iia/a  äzätliscaY.g.^y,  —  Adoa..  aktnai •saaAalia  sUrbraläi  paiti.jasata  iii V.  ß.  5  4 ;  55,  57;  —  tä  yai'.yeinti  p>sanahu kavc  'tahi  säi^rafai  Yt.  IJ.  27.
6071:'sa  (ab  Subj.)^  naptyoisä  . .  türaAya  uxjSn  a  a:  aevö  panlä  yS  'sähe  Y,  72.  1 1 ;  — (sd.)  Y.  4Ö.  1 3 ;  —  y7  xidknm  .  .  'iä .  ratus  . .  'sähe  *dasayat  paniqta  Vyt  42 ; /radähai  (sd.)  aspp/fsata  Y.ji.  161  — 1 — 'sähe  faiti  pantqm  ti/ahi  päi/i  mq^rynt %wahmät  äkras^a  manaahascä  yayä  syao- !  V.  ^  43  (s.  ob.) ;  —  sva.  'Stätte,  wo  das %anaU  °hm  %raosiä  (sd)  \.46.J;  — ,  j^sa  heittüxh  ist' :  haoa  nJ  ß-aounauayät/i vanh^us  :^aasus  i^aaatä  (sd.)  vaahius  'sähe  paiti  panlqm  drujg  vaiim^la  asmi- •/fli/J..  Y.J5.  5.  a)  GS.  mit /«ä- 'der  nqm  (sd.)  "waim  wird  uns  (die  Rinder) Pfad  des  ASa,  der  Wahrheit,  des  beUigen  !  zurUckführcn  zum  Pfad  des  Asa  . ."  Yt Rechts'   (s.  I  3  b  a):    dr^gvafö  .  .    *"Ji/j  70. 86.  ß)  GS.  mit  bir^  (sd.):  hnja
6193:AaSmnä  W.öo.^;  —  Aaomanam  •A»7  .  . eistsis  basidsa  haHmnanqm  Vr.  p.  i ;  — yamäüa  .  .  yat  /aymasyS  'Ms  .  .  ratu/ri- tsi/Vr.g.S.  a)  sonst  mit  vauhav-  Adj.: 'silvanuhi  srTra  xssi'kni ..  kainins  kfhrpa srTrayä  Yt  13.  107;  —  'stm  vaauklm x^Bii-nXm  bsrfsaitlm  .  .  dv/oarym  ahurahe mazdi  li'aKhanm  aimsanqm  spmli Yt77.i  f.;  3',  18.2,;  —  kubaotiäl  baohaite timäfum  yetihe  nmänt  °Hi  vamthi  süra paha  nida^aite  \t.17.6;  —  upa-staota yasatanqm  .  .  patH-stayata  rai^ya  'sif" vanuki  yi  b^rxaitiMX.i'j.i'};  21,  26,  54, 57.  58,  59,  ro.68,  7Ä4;  —  ava£  ayapUm dasäi  MI  'sis  (als  VS.)  vanuhi  y3  btr^saiti YL  77.  25;  6,  7;  —  vaauhim  .  .  ädqm vaauhtm  -hm  aca  mla  mrümaide  Y.  '68. ai;  Vr.  ^i;  —  mihnm  .  .  yim  kalaite 'Tis  vanuhi  parmdica  Yt/0.66;  Ä38,  Y. 13.  I,  Vyt.  8;  —  'ssis  vanhuyh  eistsis tmnkuyä  Y. /.14,  V. /p.39,  Yt. //.  16;  — sraoss . .  •«/  vatfuhi  iha  milbnatu  . .  upa imai  nmilTum  Y,  10.  i;  i,  57.  3,  Vr.  7,  i, 7/.  16;  —  ■■//«  vatmklm  .  .  ^ar»nJ..  sofS mazdaoähm  Y.  2. 14,  8.2.25;  Y. /(».ö;  — :x?ahr3Jisyeie  (sd)  paiti  '/si/ck  vanAuyä dar3i?m  haxma  Y,  60,  7,  a)  'söis  va- ti/iuyj.  (näml,  ayan')  heisst  der  25.  Monats- tag: °Ms  vanhuyh  BstSis  .  ,  ^tp^J  .  . pärMdyä  S.J.2S;  vgl.  2.25,  \.  16.6. •«/  FrD.  7  (?).        [V.  4- 45-  lies  asWa
6745:•  j.  ahax§ta-fna-  n.  im  Plur.  '100  000 Schläge' :  patuasaynsi  sataynäisca . .  balva-
7365:ayasata    °ta    xiaira  vairya  V.  20,3(?)"
7582:—  von  VtStäspa:  vTstalpaAe  .  .  °yehe  Yt '3-99>  ^^'ö;  —  sonst , von  Göttern:  atn^- iiinqm  sp?ntanqm  .  .  'yaiiqm  Y.  26.3;  — sraosaAe  asyehe  .  .  "yehe  .  .  yasataAe  V, _j.  20 ;  4. 23,  V.  18. 1 4,  S.  1. 1 7-  A)  Plur. ntr.  'die  öÄwHschen  Räume,  die  Räume,
8203:•  j.  Utavant-  Adj.  — ?— :  satavata  satJ.rita 'vata  uts.vita  ..  Yt2. 14.     Wertlos.
8204:•  j.  utS.vita-  Adj.  —  ?  — ;  satavata  sati.iita utai'oia  °ta  ..  Yt2. 14.     Wertlos.
8209:Verben  des  Sprechens  und  Denkens;  a)  auf die  folgende  direkte  Rede  verweisend:  °A' aojanö  (uifyae/anS,  °ti  vacsbts  aojanS)  Yt. /0.53  usw.";  —  °tX  mravat  Y.^j.a;  — aiiasca  °ti  V.  4-Ali  N. J7;  —  °ii  fravasata Yt /4-54t '7'i8,  ai;  —  'li  davata  \.sg.i, 44,  Yt/7.19;  *i9.47",  FrW.io.41;  —  Ui maiikäns  YL/iJ.47.  b)  iD  die  direkte Rede  eingeschoben:  ulla  ahinai  .  .  —  'ti tiiraof  ahurS  mazdü  —  ..yahinäi..'^X.io.\yi; 79.53,  V./A'.i,  VyL //(?),  43.  2)  'so',
8565:td^w^m  frasnat!e{sd.)  ürisataüw^m  upa- srt'We  ayiyqm  (sd.)  paiti  'snäitimV.S.qZ.
8568:•  j.  usmä'nar-  m.  EN.  eines  Gläubigen: -narahe'''* paisatake  a?aons  "des  U.,  Sohns des  P.  . ."  YtiJ.97;  120.
9983:mit  «f  i)  '(eine  Waffe)  niederschlagen, -schmettern  auf—'  {paiti  mit  Lok.):  ks (näml.  mi'hro)..gmqm(%A^  nijainti  aspaSta paiti  vTraii'a  Yt.  10.101,  3)  'nieder-, zu  Boden  schlagen,  er-,  entzweischlagen': yatcit  tdastaire  hindvd  (sd.)  ^ifgiurvayaiti yatcit  daosataire  niyne  (3SPM.)  Y.  57. 29;  —  %wqmca  drupmca  «»'/«« (iSPM,?) Yt.  4-5!  —  yalba  azim  nijanäni  dva 'irisva  .  .  daez'anqm  Yt  5.  22;  9.  22, 31^,  15.  3;  —  yat  niE  avavat  daljia- yasiianqm  nijattm  ya%a  ..  Yt^.  77; —  para  akmät  yat  .  .  aiimaoyB  . . *'ka%ra.jatö  nijanSite'^  V.5.  56;  y.  55;  — yö  .  .  stija  nijainti  kam^rT^l . .  na2',a.cim ymqm  sadayeiti  yavata  alm  nijainti  m>r>- zuca..  Yt,/o.7ij — yat  *n5  nsit  ni/anüt'^ ars'a  ..  Yt/5.  32;—  nij'ann'ctiS.)  buye vTspe  dusmainyü  K.i.\\;  —  yai:a  aspm aom  spähm  nijanäni  yö  .  .  Yt.  14.  58;  5. 54,  58;  —  mit  Dat  incomm. :  kahmäi  .. fraiaintim  kdi:ra.jata  (sd.)  nijanäni  Yt. 10. 110.  a)  sva.  'zerstören,  zu  Grunde richten';    l0   vispe   v^rfioinqm    vanat  nl
10035:mit  (I  (äiä)  'heraE-,  herzukommen'; 1)  ohne  Zielangabe,  von  Personen  und Zeiten:  n?ma^ka  aoara  dlta  3jasilm  Yt 10. 118;  118;  —  yai  ajasäi  *k3r>sas<a *gadstüs<a  Yt.  Ji.  6;  —  ''ustrAdyäi  i^A.) par,l  hyal  mSi  a.Jimat  ssrao^ö  Y.  43- 1 2 ; —  (J  hstqm  anhusqmca  .  .  i<ia  jasjniu /rarasäyS  Y,  65.6 ;  — /rä  mä  *nar»  *gära- yHsi&A.)  yat  ralus  yritsU  ^ajasäi^*''  N. II); —  *oim  .  .  ayarv  äjasaiti  .  .  asva  vä xsafa  Aog.  5/.  2)  mit  Zielangabe, von  Personen  und  Geschehnissen:  a)  mit J  und  Akk.  des  Ziels:  ka',a  nö  (sd.) i'ia  asiium  agat3  (näml.  akt)  i^ye/an- hatat  haea  aahaoi  ai^yajanhim  ahüni 3  V.  7(),  3 1 ,  b)  mit  Akk.  oder  Dat  der Pers.  'kommen  zu  — ,  sich  einstellen  bei  — ': a)  mit  Akk.:  ksng  ä  vanhsus  fimat  ma- iiauhd  cij(ir(sä.)  Y.4''^.ii.  ß)  mitDat.: ahmili  paoiryS  äjasät  vazfmtiö  j'^riiraytiö YL/4.  a;  7,  9,  13,  15,  17,  21,  23,  25;  — yaiiä  nS  a  vohu  jimat  mananhä  "damit der  gute  Sinn  sich  bei  uns  einstelle"  Y. 44- 1.  P?)  mit  Dat.  der  Pers.  und  Inf.: il  airyJnuj  (sd.)  .  .  rafnrai  jantü  n^n- byai(ä..  V.54,1;  —  S  möi  rafHomi  lavSng (sA)  jasata  Y.  SÄ  3;  —  a'a  nd  Jamyal avanhe  Y,  57.  3;  68.  %  Yt.  /O.  5',  77, 78.  c)  mit  Akk.  der  Sache  'gelangen iu  -,  teilhaftig  werden';  ka  mJ  urvä  voha *urväxiat*äg»inat.ti(^Vx^ys>  "wie  wird meine  Seele  des  beglückenden  Guts  teil- haftig werden?"  Y.44.Z;  benutzt:  a  vehü *un'ax/at  *äg^mat.tii  '^'>  Y.  70.  g.
=== 1566 area
26065:1565  sara-
26073:1566
```


## [2026-09-06T16:05:28.637Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '26060,26130p' BRT.txt"
}
```


### [2026-09-06T16:05:28.681Z] TOOL RESULT

```
KompE.  —  Zum  V.  sar-.  —  iBed.  vgl.  Bthl, AF.  3.  184,  IF.  j.  364,  Gdn-  KZ.  28.  195, Bn.  Stud.  /.  354,  JN.  A  hymn  55 ;  faUch neuerdings  Gdn.  VSt  2.  iH.  Enischeidend sind;  Y.  40.  z  mit  haximä  gegenüber  tarim in  Y.  4r.  6;  Y.  4g.  3,  wo  sich  vaohiui  sari maiiaiihö  und  dngvatS  haxming,  und  Y.  4g,  9, wo  sich  sarim  ärtgvati  and  asä  yuxtä  g^en- Qberstehen.  —  Pü.;  sardätih,  (lu  V.  75);  siya 'er  liegt"  I).  —  ')  Vgl.  V.  40.  2.  —  »)  Vgl. zu  saröi.  —  3)  Dualrerbindung ;  BB.  /o,  269. —    4)    Wie  Y.  32.  5;    vgL  liayö  No.  1,    —
5)  Nach  der  Variante  laeri,  vgl,  läy-  und  zu %sar-  No.  3.
•  j.  3sar-  f.,  Du.  'die  beiden  festen  Be- standteile des  menschlichen  und  tierischen Körpers,  d.  i.  Haut  (mit  Fleisch  usw.)  und
!  Knochen  sva.  Leib,  Leichnam':  kva  bitim \  aiiiAä  12ms  a/äiibm  (sd.)  /  . .  yat  iä  patü
dby  Google
1565  sara-
frasltim  sairi  nikanle  spänasla  irista naraSca  irista  ".  .  wo  man  am  meisten Leichen  vergräbt  -  tote  Hunde  und  tote Menschen-"  V.J.S;  iz;  —  cvanfym dräjB  trvatum  sairi  mai^a  triste  ztmi nikante  kavatsimS  bavainti  "in  welcher Frist  wird  ein  Leichnam  —  tote  Menschen der  in  die  Erde  eingegraben  ist,  (selber) so  gut  wie  Erde?"  V.  7.  47;  45.
ai,  särJra-  n.  'fester  Bestandteil  des  Körpe Leib'');  s.  lEt.  Gdn.  3Yt.  133  und  S  /#i'). Pü.:  iäyil  *er  liegt' J).  —  ■)  VIL  iarM^Ti?fi —  ')  Doch  ist  sat-  wegen  hai/al.nmö  besser als  fem.  lu  nelimen.  —  i)  Nach  der  Variante laFre,  vgl,  uy-  und  lu  'sar-  No.  5,
•  j.  sara-  m.:  -?-.
KompE.    —    El.?    —    Nor  AS.  hinter  Zahl- wörtern, im  Sinn  unsres  'mal'.    —    Pü.;    iu-
•  j.  saray-  m.  'Bruchstück,  Scherbe': yavat  ahmai  yamanqm  paitinqm  'airinqm aitaval  .  .  "soviel  es  ihm  von  den  Glas- gefässen  einzelne  Scherben  gibt,  (als  ob) er  so  viel  . ."  V.Ä85.
Znm    ai.  V.  ifnhi,    vgl.  lu  asarila:   —    PO.: undeutlich.
lar^Sa-
1566
J-  ■
'.  8:  lie.
•  j.  Sarah-  n.  'Kopf:  karitacii  .  .  yfi ttiyraire  'raAu  masyakanqm  Yt.  10.  40.
ai.  Mrai-  n.,  np.  sar.  —  Vgl.  lära:
•  g.  sarä  Inf.  'sich  zu  vereinigen,  ver- binden mit  — ,  sich  anzuschliesscn  an  — ' (Gen.)'':  13  vanAsuI  s'  *isyä  mananhs "drum  verlange  ich,  dass  man  sich  an ViW.''>  anschliesse"  Y.  4g.  3.
Zum  V.  sar..  —  Vgl.  'lar-,  —  Pü.;  sardlrTA. —  ')  Der  Gen.  statt  des  Instr.  ist  autftllig; wohl  eine  Altraklionserscheinung ;  vgl.  lu  Y. jr.  15  unter  Aanari,  Der.  AiS.  88,  Wh.  Gr.» S  9S3  a,  gSs  b.
•  j.  saire.hya-  n.  'Vorrichtung  zum  Dörren von  Mist"',  Mistdarre':  yff  ätr^m  °hyai haca  däitim  gätutn  avi  ava.iaraiti  V. Ä83.
Statt  'ryaiy'  geschr.,  S iffJ. 32 >).  —  Komp.: taJrya-+*aAya.  ($  36S.  3  b)  n.  'Darre';  vgl, nhd.  esu,  BTHt-  ZDW.  4.  25a.  —  Pü,:  älai  i ddraddpo,  wohl  sar  {sva.  sar,^iri)  äsöc.  — >)  Um  ihn  darnach  als  Brennmaterial  zu  ge- braachen.  —  •)  Trennung  wie  bei  larahe.hii.
•  g.  sarÖi  Inf.  'sich  zu  vereinigen,  ver- binden (mit  -)':  r  bBsdyai  {sA.)  haurvätä am>r3tätä  . .  yJ  räh»ms  (sd.)   «/j/   ia/ä
Zum  V.  sar:  —  Vgl.  'sar-.  —  Pfl.i  sardar.  — ■>  Vgl.  Y.  j/,  11.
•  j.  sairima-  Adj.  (fem.  'mS-),  bezeichnet ein  Volk  'sairimisch'*^:  aityanqm  . .  teirya- nqm  . .  'manqm  dahyunqm  narqm  asaonqm . .  'manqm  äaßyunqm  näirinam  aiaoninqm .  .  *sainunqm  . ,  dshinqm    dahyunqm   Vt.
*)  Nach  Marqi'akt  Eransahr  155  die  Sauro- maten.  Im  Mp.  heisst  das  Land  Sakman ,  das auch  Aröm  (das  oströmisclie  Reich)  genannt und  als  Quellland  des  Tigris  bezeichnet  wird ; s.  Bd.  15.  19,  20.  12,  Dk.  8.  13,  15.  S.  dazu Makquart  a.  O.;  vgl.  femer  Ggr.  OK.  199,
•  j.  "sairimanan^m  bax^lrai"  (sd.) Vyt  52.
•  g.  saragan-  m.  'Helfer':  ahmai  asä nSil  -rija  advalls  gavSi  paitJ.mravai  "ihm antwortete  Asa:  'Es  gibt  fiir  das  Rind keinen  leidlosen  Helfer""»  Y.  2p.  3.
Zu  einer  idg.  Basis  *salg-  [,  wozu  gol.  hilpan wie  ksl.  Trrügq  zu  goL  ■aiairpaii)*'^.  —  Pü.:  an i  gdspasuiän  /an  lardäriA  ni  pa  abesitärlh,  Sü. : na  svämini  aduhkhaiartflayi  gBpaiünäm.  — —  ')  D.i.  keinen,  der  ihm  alles  Leid  fern- halten könnte.  —  '>  Gdk.s  Andeutung  KZ. 30.  333  ist  mir  unverständlich,  ebenso  die von  JN.  JAOS.  2t.  171  No.  2.
•  j.  sar9ta-  Adj.  "katt':  dva  (näml.  manhs) hqmina  iaica  h^nti  'ia  äps  'ta  z»mS  'ta urvarayä  "(es  sind  dort)  nur  zwei  Sommer- monate und  auch  die  sind  (zu)  kalt  für . ."
V.7.3.
np.  sard,  lit.  siaUas,  aL  vgl.  Hüra-  Adj.  — S.  auch  lariiä-  und  sstastay-,  —  mp.  sarl,
p.  S-ard-,  j.  'sar?d-  f.  'Art,  Gattung': •dam  Bh.  5.  i  (?).  a)  hamahyayä  'dJ' (GS.)  "in  jeder  Weise':  imc^  tys*  adam akunavam  hamahyayä  'dc^  vaSna  J'urJ'-
isdahc^    akunavam    Bh.  ^.  i  z ;  6,  2,  9  ^
yd^a  im^  hasiyam  naiy  duruxtam  {sÄ.} akunavam  hamahyayä  'da/'  Bh.4,7.
KompL.  ~  Vgl.  sarAa:
j.  'sarad-  f.  'Jahr":  cfargha  vä  duyta va  . .  pasea  pancaJasjm  'r^m  V.14-  i  S ; iS.  54;  —  pasca  pan?asat>m  'rp^qm  V. 7.  48 ;  —  x^as  märyhs  sBnff  %ra^nm  (sd.) hapta  •r>oa{h?.)  apprm3yahaAe'V.iS-4S', Vd.  iS;  —  ym  narü  paniadasaahn  °r^B irTrai^yäi  Vd.  17.
Ablcit.  —  ooss.  sätd  'Sommer',  ap.sjl  'Jahr';
ai.  vgl.  iaräd-  f.  'Herbst;  Jahr';  »Et  g.  WooD
AJPh.  3f.  182.  —  Pü.:  sä/.
•  j.  'sanSa'  n.  'Art,  Gattung':  Aa'^ra vlspanqm  gJus  'tanqm  taoxma  upa.bara V,  2.  2  7 ;  41 ;  —  ^pam  *vlra  yä  stS  °tanqm vahiäa  Yty.  12;  —  äiiti  h?nti  urvara-
dby  Google
"567
'aaraSti-
sazdyäi
1568
nam  'la  V.5, 19  PüZ.;  —  j'OvaAe  -ht F.  4  g.
Komptl   —   Vgl,  *ijand..  —  «p,   (Pa.)  »gl.
•  j.  "sardSa-  m.  Name  der  Gottheiten der  Jahre:  *Za  a/ai/ana  aiake  ratavü  Y. 2.  9,  Vr.  2.  6,  S.  2.  6;  —  -SasVi^ö  asahe ratubys  Y./.9,  Vr./.4,  S.I.6;  —  rähwqm
. .  yäiryanqmca  '\anqmca  y.  i.  ly;  '— ratavö  .  .  y3irya  'la  Y.  2. 1 7.
ALleit.  aas  'tond-,  eig.  Adj.  'auf  das  Jahr  be-
lüglicll'.    —   PÜ,;   läl.
•  g.  saradanl-  C  'Verachtung,  Verhöhnung", Piur.  konkr.  'Verächter,  Schänder":  *Ui inidyai  *a$j'ni  sitigAaAyä  maj  läts'vis/ai ySi  . .  "so  will  ich  mich  aufinachen  zum Angriff  gegen  die  Sghander  der  (deiner) Lehre  zusammen  mit  all  denen,  die  . ." Y.4^.  14.
Zum  ai.  V.  iärdhati').  —  Pü.:  saräir  i  Jänii, Sü,:  ivämL  —  ■>  UDvereinbare  Ansichten  über dessen  Grundbedeatung  bei  Gdk.  KZ  30.  333 und  riscHEL  VSt.  3.  ba.
•  j.  sar«-i)ä-  'gelidus,  Kälte  bringend' maioydirim (söl)  °Mm'>  Vr.2.a;  —  matöyäh yehe  'la/te^^  Vr./.  sj  —  'lahe'^  mhM FrW.  8. 1  (?).
*iar-  t  'Kälte,  Frost';  vgl.  sanla-.    —    Bed. nach  Pü.  —  Pü. :  iorlik,  er). :  pa  sarl  iavll. <)  Tben.
•  g.  *3araidya-  Adj.  'gregalis;  Genosse">: al  töi  mazdä  t)m  mainyüm  aiaoxsayaiüä 'yayi  s^a^ra  mag^a  (sd.)  maya  vahiUä iarfta  manavAa  "deinen  Geist,  o  Af., sammt  dem  Wohlbehagen  der  beiden Genossen,  die  das  Asa  erhöhen,  soll  . ."
Ableil.  aus  *sar>da-  in.  'giei';  ai.  iärdha-  m. —  Vgl  oiasatAa-.  —  Pü.!  mtdätth  dakün, erl:  pääxiäkiA;  Siu:  niänütvam  dili,  erl.: pirlhaiatuaat.  —  1)  Vgl,  iBed.  i[;DN.  BB.  /j. 257'  —  *'  Da*  lind  Haarvaläi  und  Aanrilatäi, die  ja  unmitlelbar  zuvor  genannt  werden.  Was hier  als  x'iAnm  des  11.  und  A.  beieichnel wird,   heisst   in    der  folgenden  Strophe  hiijl-
•  j.  saraiya-  Adj.  -?-:  masdaoxttm va^S  '\p  vaxs  mq%rS  spmti  FrW.p.  i.
•  j.  sairya-  n.  "Dünger,  Mist'*>:  ava  hl gätüm  äärayjn  atryehe  (sd.  t  va  'yehe  vä V.&8.
•>  Und  iwsr  trockener,  etwa  Kamelmist.  Die Leiche  soll  auf  Asche  oder  Mist  ruhen,  die  be- ■linmit  sind,  die  aus  dem  Leichnam  sickernden
FlüMigkeilen  aofiusangen  und  so  lu  verhindern, dais  der  Erdboden  verunreinigt  wird.
KompA.  (s.  sairc.').  -  Vgl,  mp.  (Pö.)  :arg^, Ttf.targm  'Mist,  Dünger';  t.  noch  unter  lairt  -
iya:
•  j.  saurva-  m.  Name  eines  Dafia^*-. indrym  .  .  'rum  .  .  näaAai>lm  daium  V. /O.  9;  —  darvanam  daii-B  indrS  .  .  **ru" (statt  NS.)  .  .  n^nfiaih»m')  Y.in  a,
•)  Bd.  2S.  9:  "The  business  of  Ihe  demon  S that  IS  a  leader  of  ihe  demons,  is  thi«,  Ihat  U misgoyemmeiit,oppressireanarchy.inddrunken- ness  j  femer  West  SBE.  j/.  182  \o.  2,  wo weitere  Litt.  Bei  der  AuferstehnnR  kimp'fl  er mll  XIa%raVairya,  Bd.  30.  zq.  Weiteres  bei JN.  GIrPh.  1.  656,  6j8  No.  9.
ai.  sarvä.  m.  Name  eines  Gott«.  —  Versuch
einer    Etymologie    bei    Bloowield   BB.  31.
109.    -    O  NA.  .a™.     Hd*.  so   und  ^i«4.
saaum.  —  »)  S.  fialay-  No.  2
j.  «sasta-  n.  'Vollendung-,  in  eschato- logischcm  Smn;  nur  LS.;  at  matdä  tatbys xsa^rtm  vokB  manatthj  *vSmdaitJ  ae,iys Ulysi  aiai  dadin  taslayS  *drujim  "dann, o  M.,  wffd  VM.  bei  der  Vollendung  das Reich  von  dir  her  denen  verschaffen, o  AA.,  die  dem  A.  die  Dr.  in  die  Hände lieferten"  Y.jo.8;  —  at  is  voliü  hsm aiblMötst  tnananhs  atibyS  rafi'.rai  matda 'tl  ahur3  "dann  wird  sie  VM.  zulassen {in  das  Reich),  ihnen  wird  Unterstüuung gewähren  MAh.  bei  der  Vollendung"  Y 46. 1  a.
```


## [2026-09-06T16:05:49.096Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### HRN leaf for p.23 = 23+21=44 (1-based 45)\"; awk 'BEGIN{RS=\"\\f\"} NR==45' HRN.txt | head -60"
}
```


## [2026-09-06T16:05:49.678Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### HRN p.153 -> NR=175\"; awk 'BEGIN{RS=\"\\f\"} NR==175' HRN.txt | head -60"
}
```


### [2026-09-06T16:05:50.706Z] TOOL RESULT

```
### HRN leaf for p.23 = 23+21=44 (1-based 45)
OQ
94. efrö^/ten anzünden, erleuchten', Praes. efröz-em^
ewrö/fen [heme-werözT AM. 239 Zeile 1 v. u.), jn5n5N,
furö/ten, furözis^ furöy etc.
aw. aiwi + [^ruc- 'anzünden*; phlv. afröxtan,
a/röcmn, afröcimtan ; skr. abhi + [/'ruc- 'leuchten'.
kurd. vergl. ci]rüstin 'leuchten', dici\rüsi (3. Sg.).
95. ef%är 'Werkzeug', ewzar 'Organ' (AM.).
phlv. afzär 'Werkzeug, "ITZN (Talmud).
Zu ai. 1 V^hur-, Nöldeke, ZDMG. 32, 408.
96. efzuden 'zunehmen, vermehren*, Praes. efzdy-ew,
eirzäden (AM. ; hah-wezäi, 235 Zeile 2), fuzüden, efzün^
fuzün^ efzayis etc.
aw. "^aiwi + \/ snv-, sävaijät 'er wird nützen';
phlv. afzütan^ ofzün^ afzüntk^ afzäyltan, afzäyimtan,
afzäy(i)sn,
97. efsär 'Zügel, Zaum', ßsar.
aw. ^aiwisdra-; phlv. afsdr (Bund.),
syr. talmüd. LW. 1DCN.
98. efsän 'Wetzstein', eusän,^) fesän, vergl. sün,
phlv. afsän (Säy. Näääy. 10, 28); skr. gäna-^) 'Wetz-
stein* + abhi; vergl. B.rm. yesan (H. No. 211).
wa;f. sar. pasän ^Wetzstein'.
99. efser 'Krone'.
aw. ^aiwisara-; phlv. afsar 'Krone' (6ö§t-T Fr.)^).
100. efsurden 'frieren', gefrieren, fusurden^ ßsurden
(Sahn. I, 78 Vers 211).
phlv. afsartan, afsar(i)smh (vd. 19, 12), vergl. arm.
surf, 'Kälte'.
Siehe np. serd (No. 731).
101. efsös 'Spott, Scherz', fisös,
phlv. afsös 'Spott, Scherz'.
Darmesteter's Erklärung, Et. ir. II, 131 aus aw.
*aiwisaoca' ist unhaltbar, da aw. d im Np. nicht zu s
werden kann.
*) ewsün (Vullers).
*) Zu dem n vergl. Joh. Schmidt, KZ. 32, 385.
*J West*, S. 175: awüar; ZPGl. 24, 10; awavBar.
```


### [2026-09-06T16:05:52.423Z] TOOL RESULT

```
### HRN p.153 -> NR=175
— 153 —
bei. LW. sazag (237). Np. nüxte, säz sind vielfach
entlehnt, vergl. auch np. sä^t lieitzeug in arm. sa/teal
gesattelt*, ansa/t *ungesattelt' (Noldeke bei Hübsch -
mann, ZDMG. 35, 132 No. 37).
np. sd/ten ist eine Causativbildung zum Stamme sac-
(np. seztden).
689. {i)8är ^Schmerz, Leid*.
aw. sddra- 'Wehe, Leid*.
690. (2)-ÄÄr 'Kopf in nigün]sar^ sebuk]sar etc.
aw. sära-, särah- *Kopf*; phlv. vergl. sar[var 'Helm\
Vergl. No. 726.
691. 8äl 'Jahr*.
aw. sare^a- 'Jahr*; phlv. sal, sälak *alt\ arm. LW.
nava]8ard, graecisirt (nicht lydisch, vergl. G. Meyer,
Indog. Forsch. I, 326) i'for adodiv (Job. Lydus), chald.
LW. "»TlDli (de Lagarde, Öemitica I, 65), ;K''ärezm.
nau^arjT (Nöldeke, Pers. Stud. I, 34); skr. gardd-
'Herbst, Jahr (mit Zahlen)'.
oss. d. särdä, t. särd 'Sommer* (223).
Allg. entlehnt: kurd. af/. bei. (235) säl; wa/. sdl,
sar. säL
692. sälär 'Anführer'.
aw. *särö,dära' ; phlv. sälar, \idQa(jTaöa()av\öaXdvrji^
(Procop. Pers. I, 7, 11 u. ö.), arm. LW. s(dar, spajsalar,
np. serdär (phlv. sardär) ist eine junge Bildung, da
man sonst seryär erwarten müsste.
Vergl. No. 726.
693. sämän 'Ordnung, Grenze; Hausgerät etc.'.
phlv. sämän, bezw. sahmän (z. B. AV. 'boundary-
mark'), arm. LW. sahman o()ocj oQ^o/ndc^ -nQoacayua (de
Lagarde, No. 1934).
Zu ai. [/'gad' etc. (Fr. Müller, WZKM. 5, 262).
(\)8än 'Wetzstein.
Siehe efsan (No. 98) 0.
*) Nachträglich sei hier noch np. sumhäde (goschr. sunb"), Käs.
K. sunbötä, arab. LW. sunbäSaj^ sunhäSat (Bibl.' geogr. arab. IV, 277)
'"Wetzstein* erwähnt
■}\*m^t!/*m.^i
```


## [2026-09-06T16:06:06.554Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 214 215; do echo \"### NR=$n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' HRN.txt | head -70; done"
}
```


## [2026-09-06T16:06:06.926Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"731\\. \\|serd \" HRN.txt | head -20"
}
```


### [2026-09-06T16:06:08.463Z] TOOL RESULT

```
### NR=214
800. kef \Schaiiin'.
aw. kafa- *SchaunV; phlv. kaf (AV., nicht kef)\ skr.
kapha- 'Schleim'.
kurd. kaf Schaum'; oss. d. /äfä, t. /äf Hotz,
Schleim' (299); bei. kap^) (188); wa/. ;^w/, sar. /^/.
861. kul *krnmm, gekrümmt'-).
Nach Nöldeke (mündliche Mitteilung) zu gv. y.vkhig
*krumm'. Dann vergl. auch gr. xt;(}rog gekrümmt', aw.
skarena- 'rund'. — Fortunatow stellt (BB. 6, 216)
gr. y.vXXog zu skr. kuni- *lahm am Arm' (aus "^kulni-),
862. keläy, kulüy liabe', ixiD (Is. 34, 11, etwa statt ixiD?).
aw. «;ära;72rt- (?) ; phlv. varäy^ varäk.
Das np. k könnte dann eben so wenig ursprünglich
sein wie in kiisüden statt gusciden. Anderenfalls würde
die Zusammenstellung unstatthaft sein. Nöldeke will
daher (mündliche Mitteilung) gr. v.ogai, etc. vergleichen
und auch phlv. rardy, varOk ganz aus dem Spiele
lassen; jüd.-pers. JIXID sei in jNHp zu emendiren, wie
auch das Gazophylacium schreibe (D und p seien
in hebräischen Handschriften oft nicht von einander
zu unterscheiden)-^). Diese Erklärung ist gewiss vor-
zuziehen, zumal die Bedeutung *Rabe' für das Avesta-
wort gar nicht passt (sie beruht zudem nur auf einer
Vermutung Destür Daräb's) *).
863. Ualäh \VIütze'; Helm (aus Stahl, Sahn. I, 100 Vers
711)', kidä, hdeli.
') Vergl. g. kaj).
^) Durch einen Vers des vorfirdusischen Dichters Abu Öekür
belegt.
^) Im Neupersischen wird das Wort aber nie mit q^ sondern stets
mit k geschrieben. Es müsste also ein Schnitzer im Gazophylacium
und in der jüd.-pers. Schreibung vorliegen.
*) Nachträglich sehe ich Hübsch mann's Bemerkungen in
KZ. 26, 607 folg., der auch aw. väi^ayun- nicht als *Rabe* gelten lassen
will und bei. f/nräy *crow\ köh-f/uräy Vaven' (Damea, S. 104) heran-
zieht ( Corrokturnoto ).
### NR=215
— 193 —
Zu ahd. hulja, hulla 'Kopfbedeckung, also zu got.
htdjan Verhüllen, bedecken, lat. celärCj occulere
(Hörn, KZ. 32, 582 No. 10).
Das Suffix ist spezifisch iranisch (vergl. kurd. ktdäw,
serkuläw, arm. LW. sarßiday 'cucullo dei dottori
Armeni'). Calautica und Verwandtes (siehe de
Lagarde, Mitteilungen II, 4 ffolg.) /gehören nicht
hierher.
864. kulbe, kurbe *Bude', arab. LW. ktirbaj, kurhaq^ kidhat,
N ö 1 d e k e (mündliche Mitteilung) vergleicht ^r.
xaXvßrj *Hütte, Laube. Dies zu yiaXvnro) (6. Meyor,
Griech. Grammatik-, § 197a).
865. kern 'wenig, gering, klein', kemJn,
ap. kamna- Venig*; aw. katmia-; phlv. kaw^ kam(i).^f,
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
kenär s. keran (No. 846).
868. kund 'stumpf; tapfer*.
skr. (bezw. präkr.) kunfha- 'stumpf.
Vergl. Rückert, ZDMG. 8, 280.
np. ktmdaver hat nach Nöldeke (mündliche Mit-
teilung) im Öähnäme immer die Bedeutung 'stolz'.
»J Nöldeke, Pars. Studien II, 40.
U r n , QrundriHB d. noup. Ktyniolog-ie. ] 3
```


### [2026-09-06T16:06:08.516Z] TOOL RESULT

```
1286:Siehe np. serd (No. 731).
6383:731. serd 'kalt', sermä 'Kälte'.
13581:serd 100, 731.
```


## [2026-09-06T16:06:22.723Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6383,6400p' HRN.txt; echo \"### HUB p.88 -> NR=99\"; awk 'BEGIN{RS=\"\\f\"} NR==99' HUB.txt | head -70"
}
```


### [2026-09-06T16:06:24.296Z] TOOL RESULT

```
731. serd 'kalt', sermä 'Kälte'.
g. sart,
aw. sareta- 'kalt'; phlv. sarty sarmäk (Bund.); skr.
vergl. gigira- 'Kälte'; arm. sarn 'Eis*, sahium., sarcim
'gefrieren, erfrieren' (H. No. 245) ; lit. szdlfas 'kalt'.
kurd. sür; afy. sör; oss. t. sald 'Kälte' (219); bei.
.sa/d, n. särf (336) ; wa;^. sür, süri.
np. sei'ma erklärt Nöldeke (mündliche Mitteilung)
überzeugend als Analogiebildung nach germä 'Wärme' ').
*j Lit. szarmä kann ihm also nicht gleichgeaetzt werdon
(Bezzonberger, Beitr. z. Gesch. der lit. Sprache, Ol).
II r II , (jiunUriüM tl. iioup. Ktyiuologpie. 11— 162 -
732. siristen 'niisclien, vermengen; schaffen, bilden, sirls
{*sires)j siriäem 'Leim* *).
aw. l^sraes- , sraesyeiti 'sich an etwas hängen ;
phlv. sristan^ sresct (PPGh); ai. skr. [/^rres-^ (^les-^
rlisyatl Verbinden, zusammenfügen'.
sar. xlr/'am ^vermischen, mengen etc.'
### HUB p.88 -> NR=99
- 88 —
863. Die Etymologie ist unsicher, weil ein Suffix -fl&
(= ap. aAa, a^a, ada, of a?) im Neupersischen nicht
vorliegt. Kurd, kiddw verhalt sich wohl zu np. kulah
wie kurd. dew *Mund* zu ap. dahan, setzt also ein
phi. *kulaf voraus, aus dem np. kulah entstand wie
np. koh aus phi, kof 'Berg*.
864. Np. kulba = kurba *Bude' aus phi. "^kurpak = arm.
krpak 'Werkstatt, Laden, Schenke', Apg. 28, 15 u. s. w.,
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
eigentlich nur auf dieses arabisch-pers. xandaq, da die etym. Erkl&rungen
von xana^ xd,n und xanl (Nr. 465, 466) doch nicht als durchaua sic her
gelten konnen.
```


## [2026-09-06T16:06:38.603Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### PHD\"; grep -n \"sard\\|sarmāg\\|sarmag\\|afsard\\|sālag\\|salag\\|kulāf\\|kulaf\" PHD.txt | head -40"
}
```


### [2026-09-06T16:06:38.654Z] TOOL RESULT

```
### PHD
172:a-dàd [471], a-dādestān [?- DYNA, -dtst^n'] illegal, unjust. ih: injustice, illegality. a-dahm P@?hm] uninitiated. -ādan [- m! | P dn, N ~] suffix forming secondary infinitives. a-dàn [??п! | M din ignorant. ~ih: ignorance. «адап [??!] wealthy, solvent; wealth. “Аһ: wealth. a-dard [Pdlt'] painless. áüdaróg [wk], ātaxš 1 ~ : the simplest kind of sacred fire. adehig (’dhyk'] indigenous, domestic. adén [?tyn! | М dun) entry. *adén- ['dyn- | = M] bring, lead. ādišt Ptyst'] fire-stand. : ae. D i ‚ (ed уд ádüg Ptwk! | M "?dwg] capable. adur twr! | Mdwr, N ādar] fire; the god ‘Fire’; cal. gth month; oth day. adurestar [twrystl] ashes. ~én [-yx!] ashen. adur- gah [twrg’s] fire altar. ЖЕСЕ, āfrāh PSPs | М ??р?Л] teaching, doctrine. alva 2 KM N facaz\ ‘ace Luch >a-frasāwand [' Bl? wnd] imperishable. afridan, àfrin- / āfur- Pžlytn', ?Blyn-, *pwl- | M 'p(w)ryd, "po -— P >f+yn-, N āfarīdan, afarin-] praise, bless; create. áfrin ['pryn! | M?pryn, N áfarin] praise, blessing. 9544. "tien ~agan [-k”n!] Afrinagan prayers. аїгӧёар [ēlwšk! | N ~ a] a sweetmeat made of flour, butter, and honey. ‚ *afsálàn Pfs'Px!' | (N ābsālān)] springtime. afsān (?psn! | (M ?р?ле), N afsāna] story, fable. afsardan, afsar- ['psi-tn'] cool down. afsārdan, afsar- Pfs?/-tn'] cool, freeze, extinguish. „išn: cooling. afsáy-, v. afsūdan. afsénistan, afsén- [*5syx-stn!, v. abesihén-idan] destroy. --i$n : destruction. afsin [swn | N afsün] spell, incantation. M psan afsös [psws | N ~] scorn, mockery. ~gar [-g/] mocker. afsūdan, afsāy- ['pswtn!, *ps*d-] enchant, protect by spell. afšāndan, afšān- [5Zz?n-tn! | N ~] spread, scatter, sow. afSardan ['5?Its! | N ~] = afšurdan. af$urdan, afšār- 'Pfwltn!,?pP?l- | N ~] press, compress, crush. āfurīdan, afur- ?fwl-ytn', v. Afridan] create. ~išn: creation. -ag [-À! | M -g, N -a] suffix forming (i) adjectives, from nouns and verbal stems, (ii) nouns, from adjectives and present stems.
256:bayaspānļīh: mission, embassy. ~ig [-yk'] post-(horse). Бах [Pc | N ~] hawk, falcon. bāzā [b’c’y | (N bāzū)] arm. ~banag [-p'nk'] arm-guard, brassard. bazaģ [bck' | М beg, N ~a] sin, evil. —ih: = bazag. bazakkar [bckkl | M bzkr] sinful, sinner. bāzā-zanišnīh [by znfnyh = Av. bázu.jata-] a degree of sin. bazišn [dcšn'] division, part. bazm [bzm | — M, N —] meal, feast. ~-awurd [-zolt! | N ~] a sort of canapé. 1bë [BRA < A br | MP] but; out; ~... (enya), except. ~...enya...né: except... (otherwise)... not. ~ az: without. m 2be [BRA | M P, N bi-] particle with verbs, with 6, of indefinable function. -bed [-pt' | M -byd, N -balilud] suffix, -lord, -master. bēdom [bytwm | M bydwm] furthermost. béganag [byk’nk' | N ~a] strange; stranger. bégar [byk”/ | N ~] corvée, forced labour. béh [byh | N bih] quince. bel [by] | (M. Бу), N ~] spade. bélür [bylwl | M bylwr, N bilür] crystal. bérón [bylwn' | M byrwn, N bérün] outside. bëš [bys] pain, sorrow; harm, hostility. — burdan: bear hostility. bēš-, —i&n, v. bištan. bēšāz [byš(*)z] healing, medicinal. bēšāz(ēn)- [by?z(yn)-, byf?)c(yn)- | M byP?z-] heal, cure. —išnih: healing. bēš-burdār [byšbwlť’[] hostile. bëšidan [bysytn'] = bištan, bēšūmand [byš?*wmnd] sorrowful. béwar [Буш | M bywr, N ~] myriad, ten thousand. P bid [руй | P byd] again. bidaxš [byths] viceroy. *bifagàn [bch'n!] medicinal. bim [bym | = M, N ~] fear, terror. ~gén [-kn'] fearful, terrible. ~génih: fearfulness. --6mand [-'wmnd] fearful. *bistag [bstk! | N busta] hazelnut. biš [byf | N —] aconite. bištan, bé&- [bys-in' | M by$t, bys-] hurt, torment. ~išn: harm, torment. bize&k [dešk! | M bzyšk, N pizišk] doctor, physician.
392:hamēstār, —ih [hmyst!l, -yh] = hamēmāl, ~ih. hamésag [hmyfk! | M hmyšg, N —a] always. ^h : eternity. ~-86z [-swe] ever-burning. hamē-wahār [hmy whl | N haméfa-bahar] marigold. ham-éwénag [Am'dwynk!'] of the same kind, homogeneous. ham-góhr (hmgwhl! | M hmgwhr] of the same substance or nature, consubstantial. ham-ginag [hmgwnk! | M hmgwng] likewise, so. P hāmharz [A())mAlc | P I? mhyrz] adjutant, attendant. hāmīn [A*myn! |= M] summer. ~ig [-yk'] (of) summer. hāmist [KHDE, v. hammis ; )”mst!] all. ham-kār [hmk’l | N ~] collaborator. 7h : collaboration. hāmkišwar [mkyfwl | M. -wr] universe. hammis [KH DE < A k-hdh), ат... ~: together with. hammist [hmyst'] stagnant, peaceful. ~(ag)an [-(kYn'] limbo, the neutral station between heaven and : hell. vl hammóxtan, hammoz- [ALPWN-tn! < A У "Ip: hmwhtn', hmwc-, Ki hmsoz- | M hmwxtn, N āmēxtan, ámóz-] teach; learn. -išn: teaching. hammdxtar [Amwht?!] learner. ~th: learning. hammóz- , ~i8n, v. hammóxtan. —@йг [kmwcek?l | N āmēzgār] teacher. ham-nibardih [hmnpityh] (single) combat. hamēūģ [/tmwg] equal, like. hámón [k mwn' | N kāmūn] level, flat. hámoyén [/?mwdyn!] all. ham-pursag [hmpwrsk!] consulting, taking counsel. ^h : consultation. ham- |-ránih [Am nyh] battle, combat. ~-samiain [-s"m?n!] contiguous. ~-sardag [-sltk'] of the same kind, like. ~-sayag [-sdk! | N hamsáya) neighbour. ~-tag [-t*k! | N hamid] equal, peer. «tan [-tn'] of the same stature, build. ~=-tihmag [-twhmk'] relative, relation. hamwar [hmwl | N hamwār] level, abreast. hámwiür(ag) [%()mw?/, -k! | N hamwdara] always. ham-zamān [hm ODNA | N —] instantly, immediately. handām [And*m | = P, N andàm] member, limb. handarz [hndle | N andarz] advice, injunction, testament. handarzénidan, handarzén- [hndleyn-ytn!] advise.
430:kē(x)šīdan, kū(x)š- [kz(4)$-ytn! | M htos-ydn, N kēšīdan) strive, struggle, endeavour. ~iSn: strife, combat. ~iSnig : energetic. Кбу [kwd | N ~] street, lane. ki [AYK < A’yk | M kw, N kū, hi] where; that; than, ~ Буар [N лија] where. ~ tā: so that. kūč(ak) [Awe(k!) | N kūčak] small. kak [kwk'] small, short. kulāčag [kwľck' | N kulīča] small, round bun. kulāf [kwl”5 | N kuláh] cap, bonnet. ~ak [-k!] | N ~hak] little cap; calyx. kulang [Ring | N ~] crane. kullag [kwlk'] locust. kumig [Awmyk'] stomach. kun-, -išn, v. kardan, kunišn. кар [STE < A *st-h; kwn! | N ~] rump, buttocks, anus. kundāģ [knd^k! | M qnd’-, N kunda] magician, soothsayer. ~ih: magic, astrology. kundur [kwndl | N ~] frankincense. kunišn [kwnsn' | M kwnyšn] action, deed. ~gar LA | M -gr] doer, performer. kunjid [ŠM% < А пг; kwnc(y)t! | N ~] sesame. kün-marz [Rzonmlc] sodomite; sodomy. kurkum [kwlkwm] saffron. kurrag [kwlk' | N ~a] foal, colt. 1kust [Ruwst!] side, direction; district. kust [kwst' | Ar. qust] costus. kustag [kwstk! | M Rwstg] = !kust. ~bed [-pt'] district-commander. kustig [kwstyk! | N ~i] sacred girdle. kuštan, kuš- [NK SWN-tn! < А V nks; kwi-tn! | M kwšt, kws-, N ~] kill.
551:pillagan [plk’n' | M pylg, N ~] steps, ladder. pim [pym] pain, pang, sorrow. ~gén [-kyn'] sorrowful. pir [руі | N ~] old, aged, ancient. ~ih: age. piring [pling | M pryng, (N pirind)] monochrome damask, pist [pst! | N ~] browned flour. pistag [pstk! | IN pista] pistachio nut. pišīz [pšyc | N ~] small copper coin, ‘farthing’. pēhišn [pwhsn'] corruption, decay. pēlāwad [pwPft! | М pwl'wd, N pēlād] steel. ~ën [-yn!] (made of) steel. pondik [pndk' | Ar. b/fundug] hazel-nut. por [pwl | N —] francolin. pēryētkēš [pwlyw(k)kyf = Av. paoiryē.tkaēša-| (one of) the first teachers of the Mazdean religion. ~ЛЬ : the primal doctrine of the Mazdean religion. pēst [pwst! | = M, N ~] skin, hide; bark, shell. mēn [-yn! | N ~in] (made of) skin. pēšīdan, pēš- [pws-yin' | N <] cover, put on, wear. ~išn: covering. potk [pwtk' | N ~] sledge-hammer. poxtan, paz- [APPWN-tn' < А V?ph; pwhtn', pc- | M pwxtn, N ~] cook, bake. рӧу- [pwd- | (P pwd-), N ~] run. ~iSnig : running. p6z(ag) [pwc(k!) | N pēz(a)] snout, muzzle. püdag [pwtk! | N pūda) foul, rotten. —ih: rottenness. 1puhl [pwhl | N pul] bridge. *puhl [pwhl] expiation, atonement; punishment. puhlénidan [ pwhlynytn'] cause to atone. purnāy [pwln’d] adult. purr (MALE < A mlh; pul | M pur, N ~} full. =-ģāh [-g’s] at the fullness of time, about to die. ~-тюаһ [-mh] full moon. —-rawišnih [-lwbsnyh] fullness. ~-sardag [-sltk'] of all kinds. --xwarrah [-G DE] full of glory. pursidan, purs- [pwrs-ytn' | M pwrs-ydn, N ~] ask. Vu re: Е ~iSn: question. — ~i$nig : responsible. pus [BRE < A br-h; pws | = M, N =] son. ~ar [BREI, pwsl | M pwsr, N ~] son. —yàn [pwsd?n! | M pwsy’n] womb. pušt [52001 | = M, N ~] back; support, protection.
564:sang [KYPA < A kyp’; CCA (in error); sng | (P?sng), N ~] stone, rock. -~sar [-s?1] stony place. sanj-, v. saxtan. sanwar [snwl = Av. 0anwar-] bow. sar [LOYŠE < A r'šh; sl | M sr, N ~] head; top, summit; end, begin- ning. | sarāsar [s?s] | N ~] from end to end. sard [s/t! | M srd, N ~] cold. ^Àh: coldness. sardag [sltk' = Av. sarada- | (M s’rg), J srdg] sort, kind. sardsér [s/tsyl | N ~] cold region, uplands. sārēnīdan, sárén- [s’/yn-ytn'] provoke. sargen [slgyn' | N sargin] dung, manure. sarmāģ [s/m?k! | N затта] coldness. sarw [slw(b)' | M srw, N ~] cypress. sas [ss | N ~] bug. sāstār [s”st”7 | P s?s?r] commander; tyrant. ~ih: tyranny. Sawah [sw’h = Av. sawahi-] the western continent of the earth. saxt [sQ)At! | N ~] strong, hard, severe(ly); very. “Аһ: strength, severity. saxtag [shtk! | (N saxtiyán)] morocco leather. saxtan, ѕапј- [s’htn', snc- | N ~] weigh. sāxtan, sáz- [s*htm!, ?c- | (P s?*c-), N ~] make, prepare; tolerate. sāxtārīh [Pht yh] toleration, forbearance. saxwan [МРУА < А mly’; shwn' | М sxwn, N suxan] word, speech. say-, v. südan. sayag [sg dk! | M ғур, N sáya] shade, shadow. lsaz- [sc- | M sz-, N ~] be fitting, proper, worthy. --i$n(ih): fitness, worthiness. 26а2-, —išn, v. sazistan, saz-, v, sáxtan. sazāģ [sk | N sazá] fitting, worthy. ~th: fitness, worthiness. ~ ~war [-w/ | N sazāwār] = затар. sazistan, *saz- [sc-stn'] pass. ~išn: passing, transience. ~iSnig : transient, perishable, mortal. sé [3; TLTA < А tl? | M sh, N si] three. sëb [syf | N ~] apple. sēj [sye = Av. 'Gyejah- | N ~) danger, trouble. --ómand [-”zvmnd | N —mand] dangerous. sel [si | N —] spear, javelin. sém [sym | N —] — asém. !sén(ag) [syn(k)! | N sina] breast, chest. *sén murw [synmzlw | (N simury)] a fabulous bird.
752:age dad, -sālagīh; old -- pīrīh, zarman(ih), zarwan. aged pir.
1044:bonnet kulāf.
1071:brassard bāzābānag.
1142:calyx kulāfak.
1151:cap kulaf(ak).
1266:cold sard; ~ region sardsēr.
1267:coldness sardih, sarmāg.
1387:cool down afsardan.
1856:extinguish afsardan.
2525:kind (n.) gón(ag), sàn, sardag, šēn; of the same ~ haméwénag.
2624:like (a.) ēwsān, hamóg, hamsardag, hawand, manag.
3743:sort gón(ag), sardag.
4172:upland sardsér.
4369:year sāl; -years-old -salag. yellow zard.
4540:salag! škaf- škāftan nibay-! nibastant ških- šken(n)- šken(n)išn škēbāgīh škēbāg škeftīh škeft 1*$kķēh &kohih škūf- škūfag škoft škuftan hur!, šakar škarw- škarwīdan škarag škastan škaft
4704:purrmāh Ku purrsardag 15 Qa» yes dahint roe to pusyān V 10 pusar ND 10 póstén V yen 10) póst we» 105 рап}, poz So panjah ay S ya) panjag, pēzag 13619 pos- = 74010 pūšīdan Wres“O ve pēšišn VUV puštībānīh «U ye) 43 «650105 pustiban т^” оу S ANA pušt VOU 199 puštag 1100010) püdagih ^t 5120
4776:sardsér Na sisimbar ` yrtasass sīsīmbar S yeun»
4782:gáy- gādanī wattart wattarīh! srawēn- srawēnīdan srūwēn ` sarw, sraw, srü srūwar sarw bar-! burdan! srub srubén Srūš srūšīg srūd srūdan sarmāg srub srešk srištan sardīh sard, srat
4783:sardag
4818:sárcn- sārēnīdan sālwār sālagīh sālag
5023:kulāf kulāčag, kulāfak kordil kullag, kurrag kurkum kumm kustig
```


## [2026-09-06T16:06:39.228Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### NYB\"; grep -n -i \"sart\\b\\|sarmak\\|sartak\\|salak\\|afsartan\\|afsart\" NYB_vol2_glossary.txt | head -30"
}
```


### [2026-09-06T16:06:39.287Z] TOOL RESULT

```
### NYB
476:apäc [L'WEIL ; ’p’c] 1. adv. back, back- ward (opp. frāc 25?-*), again: hac 7-salak ~ for seven years 16?5; hac én and (q.v.) sal ~ 1674; — prev. with vbs. of motion, e. g. dmatan, šutan, vastan, ete., and many others, e.g. guftan, gumeatan, etc. — 2. prep. with (= apäk) 42%. — 1. < *apācā instr. adv. from Olr adj. *apdnk-, weak st. apük- and apác, derived from Av. (72) apa, OP apa, cf Skr apdfic- ‘situated be- hind’; MPrth °b’c; Paz. awāž; NP baz. — 2. < *upācā, instr. adv. from Olr adj. *wpünk- derived from Av. (388 sq.) upa, OP upä ‘under, with’; J-Prs ?b?z ‘with’ (common); v. further apäk.
528:apa-sartan ['ps'ltn'] to quench, to ex- tinguish (fire) 116’. — Properly ‘to cool down’: MPrs ?ps?rysn ‘cooling, freezing’ (Sogd 2112-18. 22); cf Paz. awasard ‘frozen’ (SGV); NP afsurdan ‘to congeal’; MPrth wysr- ‘to cool’, List 89, Ghilain 74. V. also sart.
1427:46 Py; HN?], old ev [yw], particle de- noting the opt. 1. ev: ~ HNHTWN. HajB:13 (v. nihätan); ču ŠDYTN ibd. 14 (v. vistan); ev ‘BYDWN F:5 (v. kartan); év göbet 128? (v. guftan). — 2. € Dy]: frāc & yazēt 539; ē nikecet 60%; han ē bavēt 1095. — 3. HN’: bē ē raset 604. — 4. encl. and written HWHw-yd = (h)e 61: āyēnd ~ they would cover (a distance of ...), ef the yäy-i Sart and the yày-i tamannā in early NP. — Av. (22) aēvā; Paz. č (SGV).
3201:. raftan to keep company with, to communicate with 702-8; — apar én zamik ravét he moves on this earth 3333; apar zanišn raft hend they went to slay (him) 4515-16. — hac from 62. 569.809; — 6 to 3726, 385-9 etc. passim ; — pat gehän *hamāi raft hom I roamed the world all about 318-9 (kame would not suit the context; cf 952° s, v. hamäk); — with prev.: andar ~ : ka srav ... 0$ (prep.) mart (+...) andar rajt ēstāt when the report had reached that man (who ...) 4424-26; došar"% ... andar 6 [KN] ravét will move, roam freely in Hell 347-8; — apar ~ : 6 õi ket apar raft hénd they went off to the sooth- sayer 379; 3811-15, 415, ete. — be ~ : fra- tom 6 änöd apar raft, avdom be raft (he was the first to step in there) and the last to step out 496-?-20; 5714-15; pas patvand hac oisan be raft then offspring proceeded from them 941°; very often bē only indicates the aspect: ētēn sart bē raft i-š ... went ahead so vehemently that 3315; bē rav! 6019; adak ēišān bē raft hend 5712; — frac ~ : frac raft Pourusäsp
3403:sart [slt'] cold 8614. — Av. (1566) sarota- ;
3433:sih-salak
5330:sarota-: sart
6124:sr’y-: srütan srd’g: sart srwbr: söbär srwd: sröt
6791:sard: sart
7378:sapēd: spēt sarāy: srād sard: sart
```


## [2026-09-06T16:07:02.408Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### PHD gosalag/sal\"; grep -n -o \"gōsāl[a-zāēīōū]*\\|gosal[a-z]*\\|sāl \\[[^]]*\\][^.]*\\.\\|sālag \\[[^]]*\\][^.]*\\.\" PHD.txt | head -20; echo; echo \"### AHD kel\"; grep -n -A25 \"^kel-1\\|^kel-1\\.\" AHD_watkins1985.txt | head -60"
}
```


### [2026-09-06T16:07:02.485Z] TOOL RESULT

```
### PHD gosalag/sal

### AHD kel
602:kel-1, To strike, cut. Hypothetical base of derivatives referring to something broken or cut off; twig, piece of wood. I. Basic form *kel- in suffixed o-grade form *kol-o- in Greek kolos, docked, kolobos, maimed: COLOBOMA. II. Extended form *keld-. 1.Germanic *helt- in Old English hilt: HILT. 2. Zero-grade extended form *kid- in a. Germanic *hulta- in Old English holt, wood: HOLT; b. Greek klados, branch, shoot: CLADOCERAN, CLADODE, CLADOGENESIS, CLADOPHYLL, PHYLLOCLADE. 3. Variant Celtic zero-grade extended form *klad- in: a. suffixed form *klad-yo-, Celtic source of Latin gladius, sword: GLADIATE, GLADIATOR, GLAIVE; b. suffixed form *klad- ibo- in Gaelic claidheamh, sword: CLAYMORE. 4. O-grade extended form *kold- in: a. Germanic *haltaz, “with a broken leg,” in Old English compound lemphealt, limp- ing, halting (lemp-, hanging loosely; see leb-'), probable source of obsolete limphalt, lame: LIMP; b. Germanic derivative verb *haltén in Old English healtian, to limp: HALT’, III. Extended form *keb-. 1. Zero-grade form *klo- in: a. Greek kia- in (i) Greek klan, to break: CLAST, CLASTIC; CLASMATOCYTE, OSTEOCLAST, PLAGIOCLASE (ii) Greek klén (< *kla-6n), twig: CLONE; b. suffixed form *klo-ro- in Greek kléros, lot, allotment (< “that which is cut off”): CLERK; C. suffixed form *kb-mn in Greek kléma, twig: CLEMATIS; d. suffixed form *kb-mo- in Latin calamitds, injury, damage, loss: CALAMITY. 2. O-grade form *kob- in suffixed form *kols-bho- in Greek kolaphos, a blow: coPE!, coup. See extension kleg-. [Pok. 3 kel- 545.]
603-kel-2. To cover, conceal, save. I. O-grade form *kol-. 1. Germanic *haljé, the underworld (< ‘concealed place’), in: a. Old English ell, hell: HELL; b. Old Norse Hel, the underworld, goddess of death: HEL. 2. Germanic *halld, covered place, hall, ini a. Old English heal, hall: HALL; b. Old Norse Adil, hall: VALHALLA. 3. Suffixed form *kol-eyo- in Greek koleon, koleos, sheath: COLEUS; COLEOPTERA, COLEOPTERAN, COLEOPTILE, COLEORHIZA. II. Zero-grade form *k/-. 1.Germanic *hul- in: a. Old English Aulu, husk, pod (< “that which covers”): HULL; b. Old English hol, a hollow: HOLE; c. Old English holh, hole, hollow: HOLLOW; d. Old English healh, secret place,
604-28
605-kele-?
606-small hollow: HAUGH; e. Dutch holster, holster, (< “that which covers”): HOLSTER. 2. Suffixed Germanic form *hulfti- in Medieval Latin hultia, protective covering: HOUSING?. 3. Suffixed form *kl-to- in Latin occultus (see III. 5. below). 4. Extended form *kld (< *kl-) in Latin clam, in secret: CLANDESTINE. 5. Suffixed variant form *kal-up-yo- in Greek kaluptein, to cover, conceal: Ca- LYPSO, CALYPTRA; APOCALYPSE, EUCALYPTUS. III. Full-grade form *kel-. 1. Germanic *helmaz, “‘protec- tive covering,” in: a. Old English helm, protection, cover- ing: HELM?; b. Frankish *helm, helmet, akin to the source of Middle English helmet, helmet: HELMET. 2. Latin occulere (part participle occultus; see Il. 4. above), to cover over (ob-, over; see epi): OCCULT. 3. Suf- fixed form *kel-os- in Latin color, color, hue (< “that which covers”): COLOR. 4. Suffixed form *kel-nd in Latin cella, storeroom, chamber: CELL, CELLA, CELLAR, CELLARER; (RATHSKELLER). 5. Suffixed form *kel-yo- in Latin cilium, lower eyelid: CILIUM, SEEL; SUPERCILIOUS, (SUPERCILIUM). IV. Lengthened-grade form *kél-d- in Latin céldre, to hide: CONCEAL. See extension klep-. [Pok. 4. kel- 553.] kel-3. To drive, set in swift motion. Hypothetical base of various loosely connected derivatives. 1. Extended form *kelt- or *keldh- possibly in Germanic *haldan, to drive flocks, keep or pasture cattle, in: a. Old English healdan, to hold, retain: HOLD!; b. Old High German haltan, to stop, hold back: HALT!; c. Middle Dutch houden, to hold: AVAST. 2. Suffixed form*kel-es- in: a. Latin celer, swift: CELERITY; ACCELERATE; b. possibly further suffixed form *keles-ri- in Latin celeber, (of a place) much fre- quented, hence famous: CELEBRATE, CELEBRITY. 3. Suf- fixed zero-grade form *kl-on- in Greek klonos, turmoil, agitation: CLONUS. [Pok. 5. kel- 548.] kel-4. To lean, tilt. Germanic *halthjan in Old English hieldan, to tilt: HEEL2. [Pok. 2. kel- 552.] kel-5. Gray, black, dark. Suffixed form *kel-omb(h)- in Latin columba, dove, pigeon: COLUMBA, COLUMBARIUM, COLUMBINE, CULVER. [Pok. 4. kel- 547.] kel-*, To be prominent; hill. 1. Zero-grade form *k/- in: a. suffixed Germanic form hul-ni- in Old English hyll, hill: HILL; b. suffixed Germanic form *hul-ma- in Old Norse holmr, islet in a bay, meadow: HOLM. 2. Suffixed form *kel-d- in Latin excellere, to raise up, elevate, also to be eminent (ex-, up out of; see eghs): EXCEL. 3. O-grade form *kol- in: a. Greek kolophén, summit: COLOPHON; b. suffixed form *kol(u)men- in Latin culmen, top, summit: CULMINATE; C. extended and suffixed form *kolumna in Latin columna, a projecting object, column: COLONEL, COLONNADE, COLUMN. [Pok. 1. kel- 544.] kel-7. To prick. Germanic *hulin- in Old English holen, holly (from its spiny leaves): HOLLY. [Pok. 2. kel- 545.] kel-®. To deceive, trick. Extended form *kelu-, variant *kalu-, in: a. Latin calvi, to deceive, trick: CALUMNY, CHALLENGE; b. Latin cavilla (< *calvilla), a jeering: CAVIL. [Pok. Rél- 551.] kelb-. To help. Germanic *helpan in Old English helpan, to help: HELP. [Pok. kelb- 554.] kele-1. Warm. Variant *klé-, contracted from *kleo-. 1. Suffixed variant form *k/é-wo- in Germanic *hléwaz in Old English hléo, hléow, covering, protection (as from cold): LEE. 2. Suffixed zero-grade form *kip-é- in: a. Lat- in calére, to be warm: CALENTURE, CHAFE; DECALES- CENCE, NONCHALANT, RECALESCENCE; Db. Latin derivative adjective calidus, warm (> French chaud, warm): CALDRON, CAUDLE, (CHOWDER); CHAUDFROID, SCALD'. 3, Suffixed zero-grade form *fl-os- in Latin calor, heat: CALORIC, CALORIE; CALORECEPTOR, CALO- RIFIC, CALORIMETER, CALORIMETRY. [Pok. 1. kel- 551.] kele-2. To shout. I. Variant form *kld- (< *klaa-). 1. Ger- manic Aljé- in Old English hléwan, to roar, low: Low?. 2. Suffixed form *k/d-mé- in Latin clamare, to call, cry out: CLAIM, CLAMANT, CLAMOR; ACCLAIM, DECLAIM, EXCLAIM, PROCLAIM, RECLAIM. II. O-grade form *kob-.
607-kelp-
608-Germanic *hal6n, to call, in: a. Dutch halen, to haul, pull (2? < “to call together, summon”): KEELHAUL; b. Old French haler, to haul: HALE?, HAUL. ITI. Zero-grade form *klo- (> *kal-). 1. Suffixed form *kal-yo- in Latin conct- lium, a meeting, gathering (< “a calling together”; con-, together; see kom): CONCILIATE, COUNCIL. 2. Suffixed form *kal-énd- in Latin kalendae, the calends, the first day of the month, when it was publicly announced on which days the nones and ides of that month would fall: CALENDAR, CALENDS. 3. Suffixed form *kal-e- in Greek kalein (variant klé-), to call: ECcLESIA, PARACLETE. 4. Suffixed form *kal-d- in Latin caldre, to call, call out: INTERCALATE, NOMENCLATOR. 5. Suffixed form *klp-ro- or suffixed variant form *klaa-ro- contracted to *kld-ro- in Latin clarus, bright, clear: CLEAR, GLAIR; CHIARO- SCURO, CLAIRVOYANCE, DECLARE, ECLAIR, ECLAIRISSE- MENT. IV. Possibly extended zero-grade form *kid-, becoming *klad- in suffixed form *klad-ti- in Latin classis, summons, division of citizens for military draft, hence army, fleet, also class in general: cLAss. [Pok. 6. kel- 548.] kelp-. To hold, grasp. O-grade form *kolp- in Germanic *halb- in: a. Old English hielfe, handle: HELVE; b. suf- fixed form *halb-ma- in (i) Old English helma, rudder, tiller: HELM! (ii) Middle High German helm, handle: HALBERD; C. suffixed form *half-tra- in Old English helftre, halter: HALTER}. [In Pok. 1. (s)kel- 923.] kem-1, Hornless. 1. Germanic *skamm- in Old Norse skammr, “hornless,” short: SCANT. 2. Suffixed form *kem-tydé in Germanic *hinthj6 in Old English hind, doe: HIND?, [Pok. 2. kem- 556.] kem-?. To compress. Germanic *hamjam, a compressing, hence a doubling, in Old English hem/(m), a doubling over, a hem: HEMI, [Pok. 1. kem- 555.] kem-3. To hum. Germanic *hum- in Middle English hummen, to hum: HUM. [Pok. 2. kem- 556.] keme-. To be tired, to tire. Suffixed lengthened o-grade form *kém-n proposed by some as the preform of Greek k6ma, deep sleep, which is more likely of obscure origin: coma}. [Pok. 4. kem(g)- 557.] ken-'. To be active. 1. Suffixed o-grade form *kon-o- in Greek diakonos, servant, attendant (dia-, thoroughly): DEACON. 2. Lengthened o-grade form *kdén-d- in Latin condari, to endeavor: CONATION. [Pok. 4. ken- 564.] ken-2. Hypothetical base of a number of loosely related Germanic words referring to pinching, closing the eyes, and other obscurely associated notions. 1. Old English hnappian, to doze, nap: NAP!. 2. Old English népfléd, neap tide (fléd, tide; see pleu-): NEAP TIDE. 3. Middle Dutch nipen, to bite: n1P!. 4. Old Norse hnéggr, miserly, akin to the Scandinavian source of Middle English nigard, miser: NIGGARD. 5. Middle Dutch noppe, pile: NAP?. 6. Low German nibbein, to nibble: NIBBLE. 7. Mid- dle High German notten, to nod, perhaps akin to Middle English nodden, to nod: Nop. [Pok. 2. ken- 559.] ken-3, Fresh, new, young. 1. Suffixed form *ken-t- in Latin recens, young, fresh, new (re-, again; see re-): RECENT. 2. Suffixed zero-grade form kn-yo- in Greek kainos, new, fresh (> kainotés, newness): -CENE; CAINO- TOPHOBIA, CENOGENESIS, CENOZOIC, KAINITE. [Pok. 3. ken- 563.] ken-4, Empty. Suffixed form *ken-wo- in Greek kenos (< *kenwos), empty: KENOSIS; CENOTAPH. [Pok. ken- 564.] ken-5, Hypothetical base of several roots associated with the notions “to compress,” “something compressed.” 1. Germanic root *hnekk-, “neck” (a narrow or com- pressed part), in: a. Old English hnecca, neck: NECK; b. Old Norse hnakkur, saddle, and Old Norse hnakki, back of the neck, perhaps akin to the source of KNACKER. 2. Root *knu-, nut (< “small hard object”), in: a. extend- ed form *knud- in Old English hnutu, nut: NUT; b. ex- tended form *knuk- in Latin nux, nut: NEWEL, NOUGAT, NUCELLUS, NUCLEUS. 3. Germanic root *hnukk-, sharp projection, tip, in: a. Middle Dutch nocke, tip of a bow,
609-29
610-ker-?
611-perhaps akin to the source of Middle English nokke, nock: NOCK; b. Norwegian (dialectal) nok, projection, hook, akin to the Scandinavian source of Middle English nok, corner, nook: NooK. [Pok. 1. ken- 558.]
612-k(e)nako-. Yellow, golden. Germanic *hunagam in Old English hunig, honey: HONEY. [Pok. k(e)nako- 564.] keni-. Dust, ashes. 1. Latin cinis, ashes: CINERARIUM, CINEREOUS; INCINERATE. 2. O-grade form *koni- in Greek konis, konia, dust: CONIOSIS; CONIDIUM. [Pok. 2. ken- 559.]
613-kenk-1. To gird, bind. Variant form *keng- in Latin cingere, to gird: CINCH, CINCTURE, CINGULUM; EN- CEINTE2, PRECINCT, SHINGLES, SUCCINCT. [Pok. 1. kenk- 565.]
614-kenk-2. To suffer from hunger or thirst. Suffixed zero-grade form *knk-ru- in Germanic *hungruz in Old English hungor, hungur, hunger: HUNGER. [Pok. 2. kenk- 565.]
615-kenk-’. Heel, bend of the knee. 1. Germanic *hanhaz in Old English héh, heel: HocK!. 2. Germanic *hanhilén- in Old English héla, heel: HEEL!. [Pok. 3. kenk- 566.] kens-. To proclaim, speak solemnly. Form *kens-é- in Latin cénsére, to judge, assess, estimate, tax: CENSOR, CENSUS; RECENSION. [Pok. kens- 566.]
616-kent-. To prick, jab. 1. Greek kentein, to prick (> ken- tron, point): CENTER, CENTESIS; AMNIOCENTESIS, DICEN- TRA, ECCENTRIC. 2. Suffixed form *kent-to- in Greek Restos, belt, girdle: cEstus!. [Pok. kent- 567.]
617-kentho- Also kento-. Cloth, rag. Latin centéd, cento, patchwork: CENTO. [Pok. kenth(o)- 567.]
618-ker-1. Horn, head; with derivatives referring to horned animals, horn-shaped objects, and projecting parts. I. Zero-grade form *kr-. 1. Suffixed form *kr-n- in: a. Ger- manic *Aurnaz in (i) Old English horn, horn: HORN, (HORNBEAM) (ii) German Horn, horn: ALPENHORN, ALT- HORN, FLUGELHORN, HORNBLENDE; Db. Latin cornd, horn: CORN2, CORNEA, CORNEOUS, CORNER, CORNET, CORNICULATE, CORNU; BICORN, CADUCICORN, CAPRI- CORN, CLAVICORN, CORNIFICATION, LAMELLICORN, LON- GICORN, TRICORN, UNICORN. 2. Suffixed and extended form *krs-n- in Germanic *hurznuta in Old English hyrnet, hornet: HORNET. 3. Suffixed form *kr-ei- in: a. Germanic *hraina- in Old Norse hreinn, reindeer: REINDEER; b. Germanic *hrinda- in Old High German hrind, ox (> German Rinder, cattle): RINDERPEST. 4. Suffixed extended form *kros-no- in Greek kranion, skull, upper part of the head: CRANIUM; MIGRAINE, OLECRANON. 5. Suffixed form *kr-a- in: a. Greek karé, kara, head: CHARIVARI; CHEER; b. Greek karoun, to stupefy, be stupefied (< “to feel heavy-headed”): ca- ROTID; c. Greek kardton, carrot (from its hornlike shape): CARROT. 6. Possibly extended form *kri- in Greek krios, ram: CRIOSPHINX. II. Suffixed form *ker-wo-. 1. Latin cervus, deer: CERVINE, SERVAL. 2. Latin cervix, neck: CERVIX. III. Extended and suffixed form *keru-do- in Germanic *herutaz in: a. Old English heorot, hart, stag: HART; b. Dutch hart, deer, hart: HARTEBEEST. IV. Extended form *keras-. 1. Greek keras, horn: CARAT, CERASTES, KERATO-; CERATODUS, (CERATOID), CHELIC- ERA, CLADOCERAN, KERATIN, RHINOCEROS, TRICERA- Tops. 2. Persian sar, head: SIRDAR. 3. Suffixed form *keras-ro- in Latin cerebrum, brain: CEREBELLUM, CERE- BRUM, SAVELOY. V. Extended o-grade form *koru-. 1. Greek Rorumbos, uppermost point (< “head”): CoR- yMB. 2. Greek koruphé, head: CORYPHAEUS. 3. Suffixed form *koru-do- in Greek korudos, crested lark: coRY- DALIS. 4. Suffixed form *koru-ndé in Greek koruné, club, mace: CORYNEBACTERIUM. [Pok. 1. ker- 574.]
619-ker-2, Echoic root, base of various derivatives indicating loud noises or birds. I. Zero-grade form *kr-, becoming Germanic *hr-. 1. Germanic *hring- in Old English hringan, to resound, clink: RING. 2. Germanic *hraik- in Old English hré&can, to clear the throat: RETCH. 3. Ger- manic *hrdkaz, “croaking bird,” crow, in Old English
620-ker-*
621-hréc, rook: RooK!. 4. Germanic *hraban, *hrabnaz, raven, in Old English hrefn, raven: RAVEN}. 5. Extended form *krep- in Latin crepdre, to crack, burst, creak: CREPITATE, CREVICE; DECREPIT, DECREPITATE, QUEBRA- cHo. 6. Extended form *kri- in Germanic *krik- in Old French criquer, to creak, click: CRICKET!. II. Variant form *skr-. 1.Germanic *skrik- in Old English scric, thrush: SHRIKE. 2. Germanic *skrékjan- in Old Norse skrekja, to shriek: SCREAK, SCREECH. 3. Germanic *skrainjan, to shout, shriek, in Old Norse screma, to scream, perhaps akin to the possible Scandinavian source of Middle English scremen, to scream: SCREAM. III. O-grade form *kor-. 1. Latin corvus, raven: CORBEL, CORBINA, CORMORANT, CORVINE, Corvus. 2. Greek ko- rax, raven (> korakias, chough): CORACIIFORM, CORA- com. [Pok. 1. ker- 567.] ker-3. To grow. 1. Suffixed form *ker-es- in Latin Cerés, goddess of agriculture, especially the growth of grain: CEREAL, CERES. 2. Extended form *kré- (< *krea-) in: a. suffixed form *kré-yd- in Latin credre, to bring forth, create, produce (< “to cause to grow”): CREATE, CREOLE; PROCREATE; b. suffixed form *kré-sko- in Latin créscere, to grow, increase: CRESCENDO, CRESCENT, CREW!; AC- CRUE, CONCRESCENCE, CONCRETE, DECREASE, EXCRES- CENCE, INCREASE, RECRUIT. 3. Suffixed o-grade form *kor-wo-, “growing,” adolescent, in Greek kouros, koros, boy, son: DIOSCURI, HYPOCORISM. 4. Compound *sm-kéro-, “of one growth” (*sm-, same, one; see sem-'), in Latin sincérus, pure, clean: SINCERE. [Pok. 2. ker- 577.) ker-4, Heat, fire. 1. Suffixed form *ker-té in Germanic *herthé in Old English heorth, hearth: HEARTH. 2. Zero-grade form *kr- in: a. Latin carbé, charcoal, ember: CARBON, CARBUNCLE; b. extended form *krem- in Latin cremdre, to burn: CREMATE. 3. Possibly suffixed and extended form *kera-mo- in Greek keramos, potter’s clay, earthenware: CERAMIC. 4. Possibly variant ex- tended form *krds- in Russian krasa, beauty (< “bril- liance of fire”): CRASH?. [Pok. 3. ker(a)- 571.] ker-5. Also kere-. To injure. Suffixed zero-grade form *kro-yé- in Latin cariés, decay, caries: CARIES. [Pok. 4. her- 578.] ker-8. A kind of cherry. 1. Suffixed zero-grade form *kr-no- in Latin cornus, cornel tree: CORNEL. 2. Full- grade form *ker- probably in Greek kerasos, cherry: CHERRY. [Pok. 4. ker- 572.] kerd-', Heart. 1. Suffixed form *kerd-en- in Germanic *hertén- in Old English heorte, heart: HEART. 2. Zero-grade form *krd- in: a. Latin cor (stem cord-), heart: CORDATE, CORDIAL, COURAGE, QUARRY!; ACCORD, CONCORD, CORDIFORM, DISCORD, MISERICORD, RECORD; b. suffixed form *krd-yd- in Greek kardia, heart, stom- ach, orifice: CARDIA, CARDIAC, CARDIO-; DIPLOCARDIAC, ENDOCARDIUM, EPICARDIUM, MEGALOCARDIA, MYOCAR- DIUM, PERICARDIUM. 3. Possibly *kred-dha-, “‘to place trust” (an old religious term; *dho-, to do, place; see dhé-'), in Latin crédere, to believe: CREDENCE, CREDI- BLE, CREDIT, CREDO, CREDULOUS, GRANT; MISCREANT, RECREANT. [Pok. kered- 579.] kerd-2. Craft. Suffixed form *kerd-d in Old Irish cerd, art, artist: CAIRD. [Pok. 2. kerd- 579.] kerdh-. Row, herd. Suffixed form *kerdh-d@ in Germanic *herdo in Old English heord, herd: HERD. [Pok. kerdho- 579.] kere-. To mix, confuse, cook. 1. Variant form *kra- (< *kraa-) in Germanic *hrdr- in: a. possibly Old English hrér, lightly boiled, half-cooked: RARE?; b. Middle Dutch roer, motion: UPROAR. 2. Zero-grade form “krp- in: a. suffixed form *kro-ti- in Greek krasis, a mixing: IDIOSYNCRACY; b. suffixed form *kro-ter- in Greek kra- ter, mixing vessel: CRATER. [Pok. hero- 582.] kerp-. To gather, pluck, harvest. Variant karp-. 1. Ger- manic *harbistaz in Old English herfest, harvest: HAR- VEST. 2. Latin carpere, to pluck: CARPET; EXCERPT,
622-keu-?
623-(SCARCE). 3. Greek karpos, fruit: -cARP, CARPEL, CARPO-, -CARPOUS. [In Pok. 4. sker- 938.] kers-'. Dark, dirty. 1. Suffixed form *ker(s)-no- in Rus- sian chérnyi (feminine chérnaya), black: CHERNOZEM. 2. Suffixed zero-grade form *krs-no- in Sanskrit krsna-), black, dark: KrisHNa. [Pok. kers- 583.] kers-2. To run. Zero-grade form *krs-. 1. Latin currere (past participle cursus), to run: CORRIDOR, (CORSAIR), COURANTE, COURIER, COURSE, CURRENT, CURSIVE, CUR- SOR, CURULE; CONCOURSE, CONCUR, DECURRENT, DIS- COURSE, EXCURSION, HUSSAR, INCUR, INTERCOURSE, OCCUR, PERCURRENT, PRECURSOR, RECOURSE, RECUR, succor. 2. Suffixed form *krs-o- in Gaulish carros, a wagon, cart, in: a. Latin carrus, a two-wheeled wagon: CAR, CAREER, CARGO, CARICATURE, CARIOLE, CAROCHE, (CARRY), CHARGE, CHARIOT; b. Latin carpentum, a two- wheeled carriage: CARPENTER. [Pok. 2. fers- 583.] kert-. To turn, entwine. I. Zero-grade form *krt-. 1. Suf- fixed form *krt-i- in Germanic *hurdiz, wickerwork frame, hurdle, in: a. Old English hyrdel, hurdle, frame: HURDLE; b. Old French hourd, fence, hurdle, scaffold: HOARDING. 2. Suffixed form “*krt-sti- in Germanic *hur- sti- in Old High German hurst, thicket: Horst. II. Per- haps suffixed variant form *krot-i- in Latin crdatis, wickerwork hurdle: CRATE, GRATE?, (GRID), GRIDDLE; (GRIDIRON). [Pok. kert- 584.] kes-'. To scratch. 1. Germanic *hezd6 in Old English heordan, coarse parts of flax: HARDS. 2. Extended form *kseu- in Greek xuein, to scrape: XYSTER. 3. Nasalized form *ks-n-eu- in: a. Germanic *snaww- in Old Norse snéggr, “close-cropped,” perhaps akin to the source of snuG!: b. Latin novdcula, razor: NOVACULITE. [Pok. kes- 585.] kes-2. To cut. Variant kas-. 1. Suffixed form *kas-tro- in: a. Latin castrare, to castrate: CASTRATE; b. Latin cas- trum, fortified place, camp (perhaps “separated place”): CASTLE. 2. Suffixed form *kas-to- in Latin castus, chaste, pure (< “cut off from, free of, faults”): CASTE, CHASTE; CASTIGATE, INCEST. 3. Suffixed (stative) form *kas-é- in Latin carére, “to be cut off from,” lack: CARET. 4. Ex- tended geminated form *kasso- in Latin cassus, empty, void: (CASHIER), QUASH. [Pok. hes- 586.] kes-°. To order. Suffixed 0-grade form *kos-mo- in Greek kosmos, order: COSMOS; MACROCOSM, MICROCOSM. keu-' Also ekeu-. To perceive, see, hear. O-grade form *akou-. 1. Extended form *kous- in: a. Germanic *haus- Jan in (i) Old English hieran, to hear: HEAR (ii) Old English he(o)rcnian, to harken: HEARKEN; b. suffixed form *9-kous-yo- in Greek akouein, to hear: ACOUSTIC. 2. Variant *skou- in: a. Germanic *skauwon in (i) Old English scéawian, to look at: SHOW (ii) Flemish scauwen, to look at: SCAVENGER; b. Germanic *skaunjaz in Mid- dle Dutch schoon, beautiful, bright (< “conspicuous, attractive”): SCONE; Cc. Germanic *skauniz in Old Eng- lish sciene, bright, sheen: SHEEN. [Pok. 1. keu- 587.] keu-?. Base of various loosely related derivatives with assumed basic meaning “to bend,” whence “a round or hollow object.” I. Extended forms *keub-, *keup-. 1. Ger- manic *haup- in: a. Old English héap, heap: HEAP; b. Dutch hoop, heap, troop: FORLORN HOPE. 2. Germanic *hupp-, to leap (by first bending the legs), in Old English hoppian, to hop: HoP!. 3. Germanic *Aupiz in Old Eng- lish hype, hip: H1P!. 4. Zero-grade form *kup-, vessel, in: a. suffixed form *kup-s- in Greek kupselé, chest, hollow vessel: CYPSELA; b. long-vowel form *kip- in (i) Ger- manic *Aifi- in Old English hyf, hive: HIVE (ii) suffixed form *kip-a in Latin cupa, tub, vat: CUPOLA, CUPULE; c. expressive form *kupp- in Late Latin cuppa, drinking vessel: cup. 5. Zero-grade form *kub- in: a. Greek kubos, cube: CUBE; b. suffixed form *kub-@- in (i) Latin cubdre, to lie down on (< “to bend down, prostrate”): COUVADE, COVEY, CUBICLE; CONCUBINE, INCUBATE, SUCCUBUS (ii) Latin cubitum, elbow: CUBIT; Cc. nasalized form *ku-m-b- in (i) Latin -cumbere, to lie down, recline: ACCUMBENT,
624-kéu- 31
625-DECUMBENT, INCUMBENT, PROCUMBENT, RECUMBENT, SUCCUMB (ii) Greek kumbé, boat, bowl: (CEMBALO), (CHIME!), CYMBAL, CYMBIDIUM; d. aspirated long-vowel form *kiibh- in Greek Ruphos, bent: KYPHOSIS. II. Ex- tended o-grade form *kouk-. 1. Suffixed form *kouk-o- in: a. Germanic *hauhaz, “arched,” high, in Old English héah, high: HIGH; b. Germanic *hauhitho in Old English héhthu, héahthu, height: HEIGHT. 2. Germanic *huk- in: a. Middle Low German héken, to bend, squat, bear on the back, peddle: HAWKER; b. Old Norse hokra, to crouch, akin to the Scandinavian source of HUNKER; c. Middle Dutch hokester, “one who squats,” peddler, perhaps akin to the source of Middle English hukster, peddler: HUCKSTER. III. Reduplicated form *ka-ku-bh- in Latin caciimen, summit, point (< “arch, vault’): CACUMINAL. [Pok. 2. keu- 588.]
626-kéu-. To burn, Zero-grade form *kau- becoming *kaw- in suffixed form *kaw-yo- in Greek kaiein, to burn: CALM, CAUSTIC, CAUTERY; ENCAUSTIC, HOLOCAUST, (INK). [Pok. 2, kéu- 595.]
627-keub-. Thorn. Germanic *heup- in Old English héope, brier, seed vessel of the wild rose: HIP’. [Pok. keub- 595.] keue-!. To pay attention, perceive (preternaturally). 1. Suffixed o-grade form *kous-o- becoming *kaw- in denominative (stative) Latin cavére, to beware, watch, guard against: CAUTION, CAVEAT; PRECAUTION. 2. Suf- fixed zero-grade form *ki-dos (< *kua-dos) in Greek kudos, magical glory: kuDos. [In Pok. 1. keu- 587.] keue-2. To swell; vault, hole. I. O-grade form *kouo-. 1. Basic form *kous- becoming *kaw- in Latin cavus, hollow, and cavea, a hollow: CAGE, CAVE, CAVERN, CA- VETTO, GABION, JAIL; CONCAVE, DECOY, EXCAVATE. 2. Suffixed form *kow-ilo- in Greek koilos, hollow: (-CELE2), -CELIAC, -COEL, COELOM. 3. Suffixed lengthened-grade form *kéw-o- in Greek kdos, hollow place, cavity (> kddeia, poppy head): CODEINE. II. Zero-grade form *ki- (< *kua-). 1. Suffixed shortened form *ku-m-olo- in Latin cumulus, heap, mass: CUMU- LATE, CUMULUS; ACCUMULATE. 2. Basic form *kd- in: a. suffixed form *ki-ro-, “swollen,” strong, powerful, in Greek kurios (vocative kurie), master, lord: CHURCH, (KIRK), KYRIE; b. suffixed form *kuw-eyo- in Greek kuein, to swell, and derivative kiima (< *ki-mn), “a swelling,” wave: CYMA. [Pok. 1. feu- 592.]
```


## [2026-09-06T16:07:20.169Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"θard\\|Oard\\|tharda\\|θarda\\|upa-sard\\|upasard\" KNT.txt | head -20; echo \"### leaf try\"; for n in 203 204 205; do echo \"--NR=$n--\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' KNT.txt | head -25; done"
}
```


### [2026-09-06T16:07:21.808Z] TOOL RESULT

```
3839:45 xtam : adam : akunavam : hamahyáyà :Oarda. : 08tiy : Dürayavaus : xsàya
### leaf try
--NR=203--
om ã + kart- ‘cut’; but see Kent, Lg. 18.81-2).
акша aor. mid. ($66.1, §218.11, §235.11) CMb 4; DB 1.47.
akunavayalà imf. pass. (§220, $235.IT) DB 1.20, 24.
akariya imf. pass. (585.1, §99, $220) DSf 37; XPh 42.
akarzya^tà За pl. imf. pass. (§35.1, $66.IT, $220, 8236.11) DB. 3.92. !
[c]àzr[;yatà]| or cazr{iyatd] perf. pass. ($219, $220) DB 4.90 (Kent, JAOS 62.267-8, for KT's „ада... after König, Klotho 446).
kunavahy 2d sg. sub). (8222. TIT) DB 4.75, 79.
kunavánazy lst sg. subj. mid. (§66.1, $222. III, $233.IV) DSI 4 (Bv. BSLP 30.1.65; not act. -nty, with Wb. AfOF 7.39).
kunavdtaiy subj. mid. (5222.11) DNb 56.
caxriya perf. opt. ($99, $1081, $122, $219, 6228.1, $228.II) DB 1.50.
kariyaiš opt. pass. (585.1, $220, $223.IT, $228.- Ш) DNb 9, 11 (not desiderative future, as taken by Hz. Apl 228).
kunautuy imv. (§210.1, 5237.П) DB 4.76.
kušuvā 2d sg. aor. imv. mid. (5218.1, $237.11) DNb 50.
eartanaiy inf. (581, $99, $122, 5238) DB 1.94; 2.33, 381, 44, 53, 58, 67; 3.36, 431, 60, 651; DSf 20°; DSn 1°.
karta nsm. past pte. pass. (Av. karata-, NPers. hard, Skt. kid-; $30, 506, 8122, 242.1) DPe; ЮР; DSf 38, 40, 43; XPi*; AM,
kartā nsf. A?Pa 28. kartā npf. ($119) DSi 46.
kartam nsn. DB 1.27; 2.27, 37, 42, 47, 57, 62, 02, 08; 3.8f, 10, 19, 21, 40, 47, 53, 64, 69, 76; 4.2, 42, 46f, 49, 511, 52, 54; "Ма 48f; DNb 29, 48, 56°; DSe 44; DS} 5f°; DSn 2; DSs 7; XPa 14, 15f, 19, 20; XPb 23f, 25, 30; ХРе 13, 14; XPd 19; XPf 38, 461, 47; XSc 5°; XV 27°; XH; A'Pa 24°. kartā (for nsn., $56:V) А?Ра 26. kartam asn. DNa 51; XPf 40; XPg 10; XPh 46; A’Sd 4.
kara- sb. ‘doer, maker’, as 2d element of cpd.: deriv. of kar- ($82, §143.1); found in avükara-, ciyükara-, düraniyakara-, zürakara-,  hakara-, hamaranakara-, and with passive meaning, 'thing made’, in patikara- (cf. Bv. Gr. $289).
küra- sb. ‘people, army’: Lith. káras ‘war’, dialectal ‘army’, Gt. harjis ‘army’, NGm. Heer (8143. III); ef. König, КИР 66. See also ukdra-.
180
Ката nsm. DB 1.33, 40, 79, 85; 2.16, 18, 25, 27, 301, 35, 40, 46, 50, 55, 60, 751, 87, 90, 94; 3.3, 17, 26, 32, 38, 45, 59, 62, 67, 81; 4.92; DPe 22; DSi 29,32. Ката-йт DB 1.50. káram asm. DB 1.51, 52, 66, 78, 86, 88, 95; 2.19, 20f, 25, 35, 41, 46, 55, 61, 68, 72, 81, 83f, 87, 97; 3.1f, 4, 7, 15, 17, 29, 38, 42, 46, 55, 58, 62, 67, 84, 85; 4.34; 5.7; DPe 21. kárahyà gsm. DB 1.31f, 38, 64, 75; 2.10, 15, 80; 3.24, 70, 80; 4.54, 55, 58. kárá ism. DB 1.93; 2.22, 67, 85, 95; 3.15f, 33, 36, 73, 861; 5.9, 21, 24; DPe 8f. |
Karka- adj. ‘Carian’; pl., also a province of the Persian Empire: Elam. kur-qa-ap, Akk. kar-sa, Gk. Kapes, Карко{ (§31, §106); cf. Eilers, OLZ 38.201-13, with lit. Karka пет. А?Р 30. Karka npm. DNa 30; DSe 30°; DSf 33; XPh 28.
karnuvaka- sb. ‘stonemason’: from root kart- ‘cut’, Av. pres. karanv-, Skt. kyi-, pIE *gert-, + suffix -aka- (§30, $146.D), ef. JAOS 51.210. There are also forms of this root without -i- (JAOS 53.20), such as Gk. керө (cf. Boisaca, Dict. étym. de la langue greeque, s.v.). See also Bv. BSLP 30.1.06; Hz. AMI 3.78; Kónig, Burgbau 69-70; Wb. AfOF 7.48. — karnuvakà npm. DSf 47.
Karmüna- sb. ‘Carmania’, a district of South- ern Iran ($166.I): NPers. Kirmān, Gk. Kapyavia. Karmánà absm. DSf 35.
karSa- sb. ‘weight, (unit by) weight’ (like Lt. pondo, Lg. 19.227-9), = 83.33 gr. or slightly less than 3 oz. avoirdupois (Gray, JAOS 20.55; Sehmidt, Treasury of Persepolis 62): Skt. karga- ‘pull, unit by weight’ (§29.n2, $80, $1431, VI). The OP kar$a- was one-sixth of the Babylonian mana ‘mina’ (weight; not unit of value). Elam. transcribes kur-Sa-wm, = kršam, which may mark the word as netter, since Elam. transcriptions commonly represent the nom. sg. of the foreign word; but the other evidence is rather for the masc. karšā ism. (§252D; Lg. 19.227-9; not ndm.) Wal. karíayá lsm. (§251C; Lg. 19.227-9; not npm.) We 1; Wd 1.
--NR=204--
ted by the OP writing. регу. of Iran. root *kas- (89.V, §87, $126, §146.II), = Skt. kaś- ‘be visible, appear, shine’ (so König, Burgbau 61; not to Skt. Ёйс@- ‘crystal, quartz’, despite Bv. BSLP 30.1.61); for meaning, cf. NEng.
OLD PERSIAN
brilliant. Cf. also Scheil 21.29; Wb. МОЕ 7.49. Hz. AMI 3.65, ApI 230-3; Bv. Gr. $273. See algo :
kasakaina-. Казака пзш. DSf 37, 39.
kasakaina- adj. ‘of semi-precious stone’, | | namely, of lapis lazuli: adj. to preceding ($147. ;
III).  kásakaina nsm. DPi; XPi.
Kuganakü- sb. ‘Kuganaka’, a town in |
Persia: Elam. ku-ug-gan-na-qa-an, Akk. ku-gu-ne- ak-ka. — Kuganaká nsf. DB 2.9.
Ku'duru- sb. ‘Kunduru’, а town in Media: Elam. ku-un-tar-ru-i$, АКК. ku-un-du-ur. Кид“. ти$ (§22) nsm. DB 2.65.
Küru- sb. ‘Cyrus’, founder of the Persian Empire: Elam. ku-rag, АКК. ku-ra-a$, Gk. Коро; (§164.V). Küru$ пэт. CMa 1; CMb 1; CMe.
Kürau$ gsm. DB 1.28, 39, 53; 3.25; 4.9, 27f; DBb
5f; DBh 6f.
Kūša- sb. ‘Ethiopia’, a province of the Per- sian Empire: Elam. ku-ša-a-ia, АКК. ku-ú-šu, Heb. kik. See also KüSiya-. Kā- absm. DPh 6; DSf 48; DH 5.
Kūšiya- adj. ‘Ethiopian’; pl., a province of the Persian Empire: adj. to preceding (5144.11). Kūšāya (sic!) пзш. A?P 28. Kasydé npm. DNa 30; DSe 30°; XPh 28 (written Kūšiya, $51; ef. Lg. 13.298).
zaudü- sb. ‘hat, cap’ ($100, $143.IV): Av. таоба-, Oss. хойй, NPers. тоб, Arm. (borrowed) zoir ‘headband’ (cf. Duchesne-Guillemin, BSOS 9.865, for further connections). See also tigra- zauda-. [zaudāäļm asf. DB 5.22.
Xarsadasya (or Xarsaisya), word of doubtful Meaning, Se; apparently gsm. of owner’s name. Justi, INB 173, reads lines 1-3-2, and gets Xišyāršā, approximately the АКК. form of the name of Xerxes ($163. VII); against this, see Wb. KIA 181.
tradu- sb. ‘wisdom’, meaning given by АКК. equivalent {ётё bissatum ‘word or message of wisdom’: Av. zralav- zrabw- ‘geistiges Wollen und Können’ (Bthl. AiW 535), Skt. krdtu- ‘power’, Gk. kparüs ‘strong’ (§33, 581, 5108.1, §153.III, §179.- n2); cf. Hz. RHRel. 113.27-9, Ар! 285-7. xradum asm. DNb 3.
X Sabrita- sb, ‘Khshathrita’, name assumed by the Median rebel Phraortes ($9.11, 578): Elam.
-
m
LEXICON
Éa-at-tar-ri-da, Akk. ha-5a-at-ri-it-t; shortening of compound name ($145, $164.TIT) such as *X saéra- dára- (foundin Phl., cf. Justi, INB 176). Хата nsm. DB 2.15; 4.19; DBe 6.
тќас̧а- sb. ‘kingship, kingdom’: Av. zšaðra-, NPers. šähr ‘city’, Skt. ksatrd-, pIE *gpetro-, deriv. of root in OP aSay- (§78, §148.III). See also Artazšaça-, XSafrita-, xXagapávan-. — r$acam nsn. DB 1.44, 45; DPh 4; DH 3. z3agam asn. DB 1.12, 25 bis, 26, 41, 42f, 50, 60, 61, 80f; DPd 3; DSf 10f; DSm 3°; DSp 2°; DZe 3f; XPa 19; XPb 291; XPd 19; XPf 46; XPg 14; XSe 5; XV 27°; A'Pa 24^; Ас 18, 19f. zšaçam-šim DB 1.59.
z5acapüvan- sb. ‘satrap’: Gk. сатраттв; x3aqa- + root pä- ‘protect? + suffix -van- (§155.IV, 6160.19). =ёас̧араәа nsm. (§124.5, §187) DB 3.14, 56.
z3an- vb., see axsata-.
--NR=205--
, 66, 70f, 78f, 80, 91, 92; 3.1, 9, 11, 20, 21,
181
28, 29, 40f, 49f, 53, 54, 64, 69, 75, 76f, 83, 83f; 4.1, 3, 5, 11, 17, 21f, 25, 31, 33, 36f, 37, 40, 43f, 45f, 50, 53, 57, 59, 62, 67 bis, 70, 72, 7161, 80, 86f, 87, 88; 5.1, 3f, 14f, 18, 20f, 301, 34; DBa 1, If, 2, 21, 5, 9, 14; DBb 6; DBc 6f; DBd6f; DBe 9; DBF 5f; DBg 6f; DBh 8f; DBi 9f; DB) 4f; DPa 1, 2, 3; DPd 5, 6, 19; DPe 1, 2, 3, 6, 19; DNa 8, 9, 10, 11, 15, 31, 34, 40, 48; DNb 5f, 59; DSb 2, 3f, 5f, 7; DSI lf; D8m 6°; DE 12f, 13, 14f, 16f; XPa 6, 7 bis, 8, 11, 18; XPb 12, 13, 14f, 16, 22; XPd 9 bis, 10, 11, 15; XPe 1, 2; XPf 8f, 9, 10, 11f, 16, 25f, 28, 35, 36, 44; ХРе 2, 6; XPh 7, 7f, 8, 9, 14, 15, 29, 29f, 56f; X82 1, 2; XSc 1°, 1, 1f°, 8°, 3f°; XE 121, 13f, 14f, 16; XV 10 bis, 11, 12f, 17, 17f; A!Pa 9°, 10°, 11°, 12°, 171, 20; Ае 2, 2°, 3, 4; A*Pa 5f ($2478), 9 bis, 10, 11, 21f, 24; Wa 3f; Wb If, 2f, 4f, 5f; We 2f, 3f, 5f, 6f; Wd 3, 4, 5f, 6f; AVsb-d.
z5dyaüiyam asm. AsH 7f; DPd 2f; DNa 5, 6f, 391; DNb 4f; DSm 4; DSt 5f°; DE 7f, 9; XPa 4, 5; ХРЬ 7f, 9f; XPd 5f, 7; XPf 5, 6f, 281; XPh 4f, 5f; XE 8, 10; XV 6, 7f; А!Ра 6°, 7°; MPa 7.
asdyahiyahya gsm. AmH 3; AsH 3f; CMb 2; DB 3.59; DPd 10f; DNe 2; DNd 1f; XPa 10; XPb 19f; XPd 13f; XPe 3f; XPf 14; XPh 11; XSc 2; XE 191; XV 15; А!Ра 15°, z5iyatiya as gsm. ($818.П) АзРа 121, 14, 15, 16, 17f.
хїйуабтуб npm. DB 1.8 (or nsf. adj. ?), 10, 10; 4.51; DBa 13, 16, 17f.
тїйуабёшй apm. DB 4.7, 32.
asayahiyandm gpm. AmH 2; AsH 2; DB 1.11; DBa 2; DPa 2f; DPe 2f; DNa 9; D8b 4f; DE 14; XPa 7; XPb 13f; XPd 10; XPe 2f; XPf 9; XPh 8; XSc 1; XE 14; XV 11; A!Pa 10f°; Wb 3f; We 4f; Wd 4f. zíayatiyanám (552.11) А? 2f; A’Pa 10. On the title "king of kings', see von Wesen- donk, Or. Stud. Pavry 488-90.
XŠ пз. (842) DPb; DPh 1 ter, 4; DSa 1 bis, 2, 3; DSc bis; рва 1 bis, 1° bis, 3°; DSe 8°, 8, 9°, 10°, 14°, 31°, 42, 50°; DSf 6 quater, 8, 55°; DSg 1° quater, 3°; DSi 1, I? ter, 3; DSj 1 bis, 1°, 2°, 5; DSk 1 bis, 2, 4; DSm 1° bis, 2°, 3°; Обр 1°; DSo 3°; DSt 7°, 10°; DSy 1 bis, 2 bis; DZb 1, 2 bis, 3°; DZe 5 ter, 5°, 7; DH 1 ter, 3; ХРе 6 ter, 7, 10, 11; ХР} quinquies; АЧ ter; D’Sa 2°; D’Sb 1° ter, 1, 8°; А?8а 1 quater; A’Sb ter; A?Sd 1 quater, 2; A*Ha 1 bis, 1° bis; A?Hb; A?He 7, 8 ter, 16 bis; SDa; SXa 2; SXb 2; SXc 1; XVs; AVsa.
Хт asm. DSe 5, 6; ХРе 4, 5; D'Sa 3; А?Не 5, 6. XSyam DSf 4, 4f, 10, 15; 17; DSi 8°; DSn 2; DSp 2; DZe 3.
182
Xšyā gsm. DZc 3; A!He 10, 11, 12,13. X Shyà DPe; DPi; ХРе 9, 14; XP^; XPk; XH; АЧ bis; D'Sb 2°; A’Sa 1, 2 bis, 3; A'Sb; Ае 0; A?Ha 2, 3, 3°, 4. XSahyi (853) А84 2. XSyahya XP}; XSyahiya (827) XPjv. XS as gsm. (8313.1) A!Hb.
XSanam gpm. XPc6. XSyánàm Га 11; DSc; DSd 1; DSe 8f; DSf 6; DSg 1°; DSi 1°; DS} 1; DSk 1f; DSm 1°; DSy 1; DZb 2; Рӯе 5; ХР}; АЧ; D'Sb 1°; A’Sa 1; A'8d 1; A?Ha 1°; A’He 8. XSyanam (§52.11]) DPh 1; DH 1. XSyana (§52.V) A?Sb.
X SaydrSan- sb. ‘Xerxes’: Elam. ik-Se-ir-28-Sa, АКК. hi-&-"-ar-áa, Gk. ép£ns: from хќауа- ‘king’, Ау, z&aya-, to root z$ay-, + arsan- ‘male’ ($181): ‘Hero among Kings’, cf. Skt. rdja-rsabha- (Bthl. AiW 550; but Hz. AMI 1.121n, Bv. Gr. §290, take second part to be arša- ‘just’, on which cf. §162.n1, $187.n2; ef. also Hz. AMI 7.82-137, esp. 135-6, on which see Henning, BSOS 10.502-3). Decl., 6187.
Хїауйгёй пэт. XPa 6, 11, 17; XPb 116, 21, XPc 6, 9; XPd 8f, 15; XPe 1; XPf 8, 15, 27, 44; XPg 1; XPh 7, 18, 28f, 56; XP} bis; XPk; XSa 1; XSe 1°, 3°; ХЕ 12; XV 9, 16; А!Ра 19f; A?Pa 16, 16f (both as gen., $313.ITI); Ха 1; SXb 1f; SXe 1; XVs.
XSayarsam asm. XPa 4; XPb 7; ХРе 4; XPd 5; XPf 5; XPh 4; XE 7f; XV 6.
X Saya[rsiha] gsm. XPi; [XfayárMüha XH. X Saydrsahyd ($57) А!Ра 14f; АЛ bis; A?Ha 3, 3f. Xéayárcahyü (849b) A’Sa 2 bis. Xšayāršähyā А?Не 12, (as nom., $818.1) 12f. Xarsada&yà, q.v.
тёпа- vb. "learn, come to know, know’: Av. xind-, Skt. jñā-, Gk. yeyrwoxw, Lt. gnóscó, NEng. know, pIE *gné- (806, $110, 8212). See also zínav-, dan-. | adünà imf. (NPers. dánàm, 568, $210) DB 1.51; DSq 3. x&ndsahy 2d
```


## [2026-09-06T16:07:28.990Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 211 212 213; do echo \"--NR=$n--\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' KNT.txt | grep -n -i -E \"ard-|year|sarad|manner|18[6-9]|19[01]\" | head -20; done"
}
```


### [2026-09-06T16:07:30.725Z] TOOL RESULT

```
--NR=211--
15:187
--NR=212--
4:188
6:bard- sb. ‘year’: Av. sarad- ‘year’, NPers. säl, Skt. Sardd- ‘autumn’ (§31, 587, $142). For the chronology of the rebellions against Darius, see Hist. App. IV. &ardam asf. DB 5.3. barda gsf. DB 4.4f, 41, 45, 52, 60.
17:kvpos ‘valid’, pIE *hiro- (887), + vàáhara- ‘spring time’, Skt. vdsard- ‘bright’, NPers. bahar ‘spring’, Lith. vásara ‘summer’ (§1181, $126, $148, 5148.1, §154.1; ef. Bv. Origines 16): ‘(Month) of Strong Spring’ ($161.ITa, §165). Guravüharahya gsm. DB 2.36, 41, 61; 3.39. .
--NR=213--
13:dauStar- sb. ‘friend’: NPers. dost, Skt. jostdr- ‘loving’; agent-noun ($154.IT) to root daus-, Av. zaos- ‘enjoy’, Skt. jus-, Lt. gustat ‘tastes’, NEng. choose, pIE *ĝeus- (S88). daustà nsm. (§124.5, 6186.1) DB 4.56, 69, 74; DNb 7,8, 12; DS} 4.
23:189
```


## [2026-09-06T16:07:40.789Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"srδ\\|srδyh\\|srt\\b\" SOD_pages.txt | head -30"
}
```


### [2026-09-06T16:07:40.849Z] TOOL RESULT

```
6889:      ansartc *=»srt
8615:          1671 >srt(y) C                                                         xnt, }nt2=>>stny
20794:     niyosne ©pres. part.; voc. nYwsrt\ pi. -nYwsnyt                 Frag. Len. 44.1
24447: prsrt-
29591:srt
29594:8963 srt - B                                    *j+        8974 sry'ws       B                  ^Ja^u* i<j&\ «ojy- ~&*>
29617:     srosarat-payi (srwsrt Py) ©Av. sraosa-asya-
29625:8967 srwsrt pY ** srws*rt pyy                                      AVS 98
29688:                                                                9005 stw-'srt M                                  ^l^j-u.
```


## [2026-09-06T16:07:43.112Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '29560,29640p' SOD_pages.txt"
}
```


### [2026-09-06T16:07:43.165Z] TOOL RESULT

```
                                                                    Saragh, Lo-yang(a town in Ancient China)
        GMS 526; Anc. Lett. 2.6, 21, 31, 32, 35, 51, 62,            Anc. Lett. 2.11, 13, 37; Hen. BSOAS 12, 603, 608
         3b; MD; STii 1.18, 81, 9.13, 14; BSTi 196; BSTii:
                                                               8957 srgc C =» sryc>nch
        C2, 1R10, 94R13, 68V13-, Sund. AoFiii 1975,
        66.16, 67.1; Man. Lett. 310.9; CII 1990 Dl             8958 sryc'nch B                          £^ (^ -o ^j~^>)
                                                                    saryc(anc) (srgc)
8946 sr5»k     B                                    <JU<JU          (<9/)Saragh
      sar5ak    ^sptsrS'k                                           BSTBL, Intox. 34; GMS 1023; Pelliot TP. 1931,
                                                                      458; STii 330 p546 n 3
       year 14; GMS 1156; STii 9.15; Hen. Tales. 467.32;
      SCE                                                      8959 srywyc B                                          >j>^
        sr&kw, VJ 347; sr&w                                         sar-xwec =^srxwyc
8947 srS>k     B, S =» sr5»k                                        headache
                                                                    TSP 7.6
8948 srfi'nk B, M, S        * J3j^iS^^tJi^^i^Aj
     sarOang ©pi. -/ =^sr8ng, sr5nng                           8960 srm'n S                                          ? ^\j
     commander, chief, lord                                         sarman ?
      TSP 13 ii 6; Notesiv 499; -w, BBB p78, 64 1;                  monk ?
        Sogdica. 34; Frag. Len. 31.4, 80.7; Sund. MHC               MDiipl67.11
        p27.8, 36, 10V8                                        8961 srsn^ B                        <^y^)>ti-i<fL>.
8949 srS>t B                                          UJU           sar-snam
     sarSat (sr5yt, srdt) ©pi. =^sr5                                b&lhihead-bath)
                                                                    SCE 518
      years2.523; GMS 070; Hen. AM 1952, 203.4; Sund.
      TSP                                                      8962 srsp(,) B                             J^-^l^J^
        AoFiii 67.1
                                                                    sarsapa ©<Skt. sarsapa =»sywsp8n, sp>nty 8>ny
8950 sr8S M                                               JU        mustard seed
     sarS =*sr5                                                     TSP 14.5; BSTBL, Padm. 54; Hen. AION 6, 1965,
                                                                                                                   362
srt

        29-47                                                    BSTii 843.56; S W, C2 p84, 40R10, 68V25, 111V6
8963 srt - B                                    *j+        8974 sry'ws       B                  ^Ja^u* i<j&\ «ojy- ~&*>
          w                                                     saryos
     sart ©<Avsar9ta\ Yaghn. sort ©nom. ob. -y,
                                                                 disturbed
      cold                                                       SCE 318; GMS 551
     GMS 526; TSP 2.420 3, 259, 265; VJ 533, 961;
                        ,                                  8975 srypt}m B                              ^<£j
       SCE 291; Frag. Len. 65.9, *srttw, SCE 386                sarepdam ? (sr'yptta, sryPtm) ©ob. -y
8964 srBng C                                     S^^            pain, suffering
      sar9ang ©pi. -/; ob. pi. -/y ^srS'nk, srSnng              GMS 1094; VJ 1493; TSP p271; BSTBL; SCE 466
      chief
                                                           8976 srypt'mync B                              ^T^^jb^j
      BSTii 851.8, 881.5: C2, 12V8, 13R18; Sund.                sarepdamenc
        AoFviii 1981, 30R 9
                                                                 painful, tormented
8965 srwq M                               j^M^j^t^f              BSTBL, Dhy. 397
     srok ©<*sruka\ Skt. sloka     =*ptsrwm-
                                                           8977 sryptm =» sryPt>m
     speech, hymn
     Sogdica. 45.7; GMS 978                                8978 sryt => sr-
                                                           8979 sryy M =» sry
8966 srwsVt pyy M          dsy^ oLJ-^ Jf ^i)jy oy^
                                                           8980 st- M, C                                   j*S&
     srosarat-payi (srwsrt Py) ©Av. sraosa-asya-
                                                                sat (stt-) ©Yaghn. sat; Khot. sata\ Parth. sad-
     Sroosh-RatU Manichean god)
     BBB pl35; Hen. BSOAS 11, 216 n8; Gersh. AHM                   ©pt. st. =*sn-, syn-, sty2
        194n; KG 2350; Sund. AoFvi 1979, 101; W-Lii              (to)risc
                                                                 KG 541; GMS 864 A, 780, BSTi 113, 121; C2
        504, 566.11; S W, ANP2, 157-8
                                                                   gloss. p225; Sund. Man. Lett. 310.17, 18, 20;
8967 srwsrt pY ** srws*rt pyy                                      AVS 98
8968 srwsy M                     jy_^ <J>j?(*J t^^^j
     srose                                                 8981 st-2             (jop o^^ff^ oo uy> >^~- j-0-^
                                                                sat ©mostly in compds. abl. inst. st\ nom.; ace.
     obedient, dutiful
                                                                  stw -*stw, stp^k
      Sogdica. 64.8 n p65; BBB 687 p82; GMS 1156                hundred
                                                                 stay
8969 srwsyft M                           c^Jsl ^>^U>            GMS 1667, 1316, STi 43.9, 12
     srosift ©<Parth.
     obedience                                             8982 stnY/x       B             (^:J^*)*jJoj*<r&
     BBB 687 f75
                                                                 childless
8970 srxwc S (M)                           (Jj^^jj*             SCE 27; GMS 1108A
     sar-xuc                                               8983 sV C
     salute
```


## [2026-09-06T16:07:54.246Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"89[23][0-9] sr\" SOD_pages.txt | head -20; echo ---; sed -n '29480,29562p' SOD_pages.txt"
}
```


### [2026-09-06T16:07:54.317Z] TOOL RESULT

```
29450:                                                             8927 sr-                                  (u>>>^j^
29465:                                                             8928 sr}k B, M
29471:     perfection, completion                                  8929 sr'kh S
29478:     (to)serve                                               8930 sr>k(w)      B
29486:     STi 37.1; Benv. JA 1955, 322, 1959, 121                 8931 srNv-      C                                 o^jj^^o^y-
29492:     iron, chain, iron fetter                                8932 srVj'ky M                                         Ullo^
29498:     spinawe ? ^spyn                                         8933 sr'ws rwc        M, S       '-^j^)*^ {*•>** jjj*j3 j J* jj^
29506:     horse racing                                    'ArV    8934 sr'wty* C
29511:     (ro)serve, (ro)pay respect                              8935 sr'y B
29518:                                                             8937 srpVk   B =» sflr'ck*
29520:                                                             8938 srpy MD =* s'rpwy
29521:8926 spyy    C =» sp-                                        8939 sre'y B => srey
---
                                                                   sare ©in compd. =*sr>y
       C2 p99 n29; perf. spxsd}r-, STi 27.19                       head, having head of
8920 spxs(w) C                                 c^j^i^L*
     spaxs(u)                                                      srykw, TSP 3.153 etc.; sr())yy TSP 13.9 etc.; TSP
                                                                     3.124, 136                               J~*
     service
     STi 37.1; Benv. JA 1955, 322, 1959, 121                 8931 srNv-      C                                 o^jj^^o^y-
                                                                   sraw
                                                                   Go)sing
8921 spyn- C                                 _*?rj<j*i
     spen, span, span ©<*aspanya ©pi. spynt*                       BSTii 890.54, 55: C2, 60V22, 23
       ^spn'yn'k, spnync()), spnyq
     iron, chain, iron fetter                                8932 srVj'ky M                                         Ullo^
                                                                  sar-uzak(c) ?
     BSTii 843.18, 846.24: C2, 68R18, 69R22; S W, C2
                                                                   letter of alphabet
         pl48                                                      Sogdica. 27.13; GMS 991
8922 spyn'wy M                                   f^r«>^
     spinawe ? ^spyn                                         8933 sr'ws rwc        M, S       '-^j^)*^ {*•>** jjj*j3 j J* jj^
     sin
                                                                   sros-roc
     BBB f 8, abl. spin>w\ GMS 1082, 1255
                                                                   seventeenth (fay of the month
8923 spy swd'mnty C                              ^Ijp^-J            song JRAS 1945; Fasts. 151.9; MD
                                                                   Hen.                                            Jj l ^j^
     (a)spe-soSamande ©ace. -tw
     horse racing                                    'ArV    8934 sr'wty* C
                                                                  srutya ©f. n. ob. pi. srwtyty
     BSTii 892.21: C2, 31R21
8924 spys-     M, C                            j^l                 BSTii 829.30: C2, 102R30 n pl77
     spes (spys-) ^sp'ys-, spxs-, sps-
     (ro)serve, (ro)pay respect                              8935 sr'y B
     GMS 752; BSTii 897.86: C2, 55R26, 57R3; AVS                  sare ©in compd. ^sr>k(w), sry
       128                                                         head
                                                                   TSP 3.135
8925 spyty     C
     spete Osp'ytk) =*spty2, ^p'yt'k.                        8936 si^ypt'm     B =* sryPt>m
     white
                                                             8937 srpVk   B =» sflr'ck*
     STi 16.9; Sund. AoFiii 77
                                                             8938 srpy MD =* s'rpwy
8926 spyy    C =» sp-                                        8939 sre'y B => srey
                                                                                                                         c>>

361


8940 src'yk     B                        c^^^JjUo-^
     sarcik     (srcyq)                                             GMS
                                                                     happy970; Hen. AM    1952, 203.1
      chief, first, superior                                   8951 srSnVn B
      SCE 199; TSP 15.7; GMS 1014; BSTii 887.6: C2,                  year
                                                                    sarSman ©pi. -t
                                                                                                                 Jbx— _^5»-
        91R6, Sund. 1988, 184
8941 srcmyk   M                              ^J^c^j;^               VJ 113, 1044; TSP 11.27, 14.37; -r, TSP 2, 693;
     sarcmlk ?                                                        STii 8.7

      highest rank                                             8952 srSm}nyt(w)     S
      W-Li 568                                                      sar8manet

8942 srcy B                                      j^^lc^             happiness                                    ^Jbtiy-
     sarci (src^y)                                                  Anc. Lett. 5.16, 1.10; GMS 1073

      first, formost                                           8953 sr8nng    M                             tj^jiS^^
      GMS 1006, 1332; SCE 420, 539; TSP 2.739, 741,                 sarOang   ©pi. -r; ob. pi. -ty =*sr8ng, sr8>nk
                                                                    chief
         5.45; BSTBL, Vim. 55, 87, 165, 58
                                                                    GMS 292, 810; BBB p91 b8; Hen. JRAS 1945,
8943 srcyq C =» src}yk
8944 srd C =* sr5                                                     154.12; pi. -t(y), GMS 1225, 1228; Sund. Man.
                                                                      Lett. 305-311
8945 sr5 B, M, S                    (o>> >^- >>)JU
     sar5 (srd) ©A v. sar?da\ OP Oard-, Khwar. srS             8954 srdt   C =» sr8>t
        ©nom. -y; ob. -c>>y, -yh; pi. -HlytJ-t   ^srS't        8955 sr5yt M =» sr8>t
                                                               8956 sry S       iSa^ z^ja j-^- j.> ^^        ^-u^ f^)\^
       year 526; VJ 265, 1408, 1409; TSP p271; SCE 13,
      GMS
         377, 383; BSTBL, Padm. 27, 45, 46; Intox. 34,              sary, saray
         35; Hen. JRAS 1945, 149.15; KG 353, 2372;
                                                                    Saragh, Lo-yang(a town in Ancient China)
        GMS 526; Anc. Lett. 2.6, 21, 31, 32, 35, 51, 62,            Anc. Lett. 2.11, 13, 37; Hen. BSOAS 12, 603, 608
         3b; MD; STii 1.18, 81, 9.13, 14; BSTi 196; BSTii:
```


## [2026-09-06T16:08:07.515Z] TOOL CALL #36: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['MON'],ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-06T16:08:10.200Z] TOOL RESULT

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
```


## [2026-09-06T16:08:13.813Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"آبسال\" BQT_v1_pages.txt | head -20"
}
```


### [2026-09-06T16:08:13.869Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T16:08:16.927Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\nfor i,p in enumerate(pages):\n    if 'بسال' in p or 'آبسا' in p:\n        print('LEAF',i, p[:60].replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T16:08:18.626Z] TOOL RESULT

```
777
LEAF 7 ۱ ی ۱ برهان قاطم متعلق بکتابغان؛ ملی نپران (خم ۱) مورخ بسال 
LEAF 22 م . معین سس ب - دیگرز بانهای ایرانی بجز زبانهایی که در مقالا
LEAF 35 بیست وهفت زبانهای ایرانی کنم» کند» کنیم» کنید» زمان‌ماضی: کر
LEAF 64 مقدمه شحاه وشش |ماهیچکد|م از خودنیر سید ندا گردساتدرست‌است چ
LEAF 79 هفتاد ويك فرهنگپای پارسی ابر اهیم قوام الدین فاروقیست که در۸
LEAF 83 ۱- فر هنك محمدین قیس . ۷۲- فر هنشکت «حمدهندوشاه ۱ . ۳- فر هت
LEAF 90 مقدمه هناد ودو رجال معروف هندوستان وملقب بعضدا لدو له است وش
LEAF 121 صد وسیژده اقتباس وقلید وترجمه و رد برهان برهان قاطم : نمید ف
LEAF 122 مقد مه صد وچپارده موّلف بال ۱۲۸۱قمری» و آن درسال۱۲۸۳قمری درم
LEAF 123 صد وپانزده اقتباس وقلید وترجبه و ردبرهان مجموعه در ۱۲۸۳ قمری
LEAF 124 مقد مه صد وشانزده اغلاط [نر| اصلاح کرد ومقداری لفت بر آن افز
LEAF 129 صد و یست و .ك نسخ خطی برهان قاطع شمارء اوران ۰.۳۵۷ صفحه‌ایی"
LEAF 132 معنمه صد و بیست وچپار ۲-نخه بنشانی ۸۸00.26,130 شمار صفحات ۰۷
LEAF 134 مقد مه صد و بیست وشش و مقابلهً کتاب و جمم لفات نتمه الی الآن
LEAF 135 ِِ کاب عاضر 1- متن ۹ کتاب حاضراز روی نسخ چایی وخطی‌ذیل مقابل
LEAF 170 تالیف کتاب دیباجة موف ۱ ۳ فرجام‌رسانیدموخا تمصحیفة انبیا وفا
LEAF 295 کت آیرویز نحتانی مجهول و واو » بسعنی آبی باشد و آن ا ییون « 
LEAF 526 تدامیر ۱ ۱ ی دوافروش ٩‏ - و کرانقروش را ی زکویند - ونم بنشر 
LEAF 699 آحت‌سر اج بنتح سین. بی ضله ورای قرشت بالف کشیده بجیم زده , ن
```


## [2026-09-06T16:08:24.268Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (215,216,217,218):\n    print('==== LEAF',i)\n    print(t[i][:2200])\nEOF"
}
```


### [2026-09-06T16:08:25.951Z] TOOL RESULT

```
==== LEAF 215
ساختن ناشد .
" .ریز - بر وزن خاه ریز . ادبخانه
و مستراح را گویند - و بمعنی دلو آب کشی
هم آمده است - و ظرفی را نیز کفته‌اددکه در
وقت غل کردن بدانآب‌برسرریزند - و کودالی
باش که از برای آپهای مستعمل همچو آب‌حمام
و آب مطبخ و امثال آن‌کنده باشند .
آ بر یزان - روز سیز دهم تبر ماه
باشد ٩‏ . گویند در زمان مکی از ملوك عج‌چند
سال باران نباوبد . دربن روز حکما و بزرکان
و خواصوعوام در جائی جمعیت نموده دعا کردند
همان لحظه باران‌شد , بدان سبب‌مردم شادی‌وشاط
کرده آب بربکدیگر ربختند. و ان «وز این
رسي برجاست .
؟ بر یز گان » با کاف فارسی » نام
ی تس نی اس
آب زدن ه بفتح زای هوز ودالابجد
و سکون نون . کنابه از فرو نشاندن و تسکین
دادن باشد ۴ .
اب ژر فت ه عنم رابع ورای قرشت
باشد که خریزه و حندوانه و هر موه که درون
آن ضایم و ترش  )۱(‏ وکنده شده باشد .
زک » بر وزن بادزن ءظرفی را گونشد
از مس و امثال آن بىقدار قامت آدمی با کمشس
آب مالان
ازآن . باس‌پوشی سوراخ دار که اطبا بیماران‌ر!
در آن خواباند بسا بتشانشد ؛ و سر بیمار را از
آن سوراخ بیرون آرند » و آب کرم با ادوبة
جوشانیده درآن کنند - و بمعنی حو ضکوچك
هم هست - و کنابه از آرام و تسکین دهنده
باشد » یمنی شخصی که مردم را بزبان خوش
تسلی کند - و امر باين معنی نیز آمده است
یمنی شسلی کن و تسکین بده (۷) *
| بر ۵ » بسکون ثالث وکس رابموظهور
های هوز » پمعنی زهاب باشد » بمنی آب ی که از
چشمةٌ کنار تالاب و رودخانه تراوش کند .
آب ژهره - بکر ثاك و سکود
باشد - و ثابش و شفق بعد از صبح؟ را یز
تفن
آب یر گاه - کی را گوبندکه
خود را ظاهر خوب وا نماید و در باطن حفتن
و فتنه‌انگیز باشد - و کنایه از خوبی و نیکی
مخفی - و رواج و دونق خس پوش هم حست
باّب که خوبی ولیکی وقابلیت و کمال‌واستمداد
و رواج و روفش مخفی و پزشیده است . "
آ س « جختح تالث بر وزن فاکس , نم
شهری و مدینه ایست نامملوم .
آب سالان - بالام بر وزن آب پاشان,
بممنی باغ باشد و بعربی حدیقه گوبشد ۴ .
2[ ددر پشتو
(قی : ۰ بهاران) ۰
==== LEAF 216
" ]یست - بنتح ثاك و سکون رابم
و فوقالی . کرشت ترنج را گویند , و آن را
میه بالشکه نیز خواشد . ممده را ژبان دارد -
و یکر تاك مخفف آبستن باشد ۱ . #
۲ فستان ه بی وزن تاستان » بسنی
آبتن بود یمنی هر حیوالی که بچه در شکم
داشته‌باشد ۱ - و بمعنی پنهان‌داشتن هم گفته اند.
] بسقی - بر وزن داستن نهفته و پنهان
را کوبند و هر حیوال ی که بچه در شکم‌داشته
باشد ؟ .
آ بستن قریاك » بکی نون » کنابه
از پربط است ۰ و آن سازی باشد که حطربان
نوازند . *
] بسته « پفتح ثالث بر وزن وارسته »
زمینی را گویند که بجهت زراعت کردن مهیا
کرده باشند - وبمعنی جاسوس‌هم آمده اس تکه
خبر گیرنده باشد - و عردم چاپلوس را لیز
کویند م ویکسر ثالث بمعنی‌آیتن باشد ۷ -
و زهدان را حم کنته‌اند.(۱) که بعربی رحم
خواند . *
] بسگوت ه بکر اك و سکونرابع
و شم کاف فارسی * و واو و نون ساکن » تلم
جزیره با قربه‌است از قرای طبرستان نزديك
باستراباا . و میان آن و جرجان سه روزه رأه
است - و نام دربای آنجا نیز هست . ووجه‌تسميةً
آن به آب سکون آن است که رودخانهای که
آترا آبگون خوانند از خوارزم آعده بدربای
خز رکه آ نرا آسکون (۲) میکوبند داغل‌میشود
و چون ترديك بدوبا میرسد بآهستگی و سکون
تمام میرود » بدان سبب آب سکون خوانند -
و بسی محل پیوستن آن رودخانه را با دربا
آبسکون (۳) می‌نامند - و جزیره ای فیز بوده
است تزديك بدانجا » آتر! آب سکون‌میکنته‌اند.
کویند وقتی که سلطان محمد. خوارزمشاهازلشکی
تاتار گریشت بان جزیره آمد(4) » دوز عمرش
بآخر رسد و الحال آن جزیره را آب گرفته
ات ۲ -
آب سواد ان - سواران‌آب است 6 ؛
و آن شیشه ماتندی باشد که یشتر برقت باریدن
باران در روی آب بهم رسدو بمربی‌حیاب گویند.
آب سیاه - یکی تالث ورایع : کنابه
از شراب انگوری باشد .- و ماد علتی (ه)رانیز
گونند که بدیب آن چثم نایینا گردد - وآب
طوفان لوح را هم میگویند .
ب سیر ه بفتح رابع و سکون الث
و تحتانی و دای قرشت + کنابه از چاروای («)
خوش رفتار و خوش راه باشد .
(ه) خم ۳ : وعلتی (+) چش : چاریای .
و آستی‌حم مت ۳
(برهان قاطع )٩‏
==== LEAF 217
"آب سیه « یکی اك , مخخف آب
سیاء انت که شراب انگوری - و علت کوری
و غیره باشد . ۸ ۱
[ بشت - بنتح تالك و سکون شین و ای
قرشت » هفته و پنهان را گوبند ٩‏ .
۲ بشتگاه ه خلونشانه - و جای هفتن
و محل پنهان شدن باشد » چه گاه بمعنی جا
و مقامبهم آهده است - و ادیخانه و مستراح را
یی زگویند .
] اشتگه - مخفف آبشتگاه است که
محل نهفتن و ستالخلا باشك  .‏ .
۲ بشتن - بفتح ثاك » بر وزن‌وارستن .
بمعنی نهفته وپوشیده داشتن باشد . ویکسر ثاكث
عم کنته اند .
محل نهفتن (۱) - و خلوتانه و متوضا (۲)باشد.
جای بنهان شدن - و لهارنخانه باشد .
| بشود - با خای نقطه‌دار و راو
معدوله بر وژن دانشور ؛ بمعنی اصیب و ق-ستم
باشد - و سررچشمه و کنار دجله و رودخانهو:الاب
و استخر (۳) و امثال آنرا نیز کون که مردمان
و جانوران از آنجا آب خورند » و آنجاراپعریی
منپل و عطن خوانند - و ظرف آبخوربرا حم
کفته اد - و بمعنی توقف نمودن و مقام کردن
آپ شیب
هم هست ۴ .
آب شلن - بمعنی کداختن باشد -
و کنابه از شرمنده شدن - و رفتن :رت ءآبرو
و برطرف شدن رولق و رواج هم هت .
۲ پش دوشن است « نی عزت
و آبرو -و رواج و رونق و طراوت دارد . *
آب شناس - کنابه از حقیق‌هنلی-
و فاعده دان - وصاحب مهارت درعلوم باشد (4)-
و تخصی را لیز کویند که بر بالای تیر کشتی
برآمده ا صلاح و فاد دربا خبر دعدب وشخصی
که آب کاریز و چاه رامیشناسد بعنی میداندکه
کدام جای از زمین آب دارد وکدام جاندارد ؛
و آب شناسان جمم آب‌شنای است نی قاعه ‏
دانان .
آ بشنگ. ختح رابع بر وزن آبرنگه
بىعنی اول آپزن است و آن ظرفی باشد از می
و امثال آن بمقدار قامت آدمی که طبیبان مار
را در آن خوابانند و ادویهٌ جوشاننه در آن
بت سم
اب شنگر ی » بک ات .کنابه
۲۳۶۱
اب شیت بت یک رابع و سکون‌انی
و تحتالی وبای ابجد , راهگنر آب را گونن دکه
از بالا بزیر آورده باشند .
(4) خم ۳ : - باشد .
مقام کردن :
ببهرام داد ان زمان دخترش
۵ آبشی - رك : آوشن .
۴ - پمعنی منزل و مقام وموطن است ؛ نه
۳ ۰
==== LEAF 218
آب صفت بودن - کنابه از یار
بفم و فایده رسانیدن باشد - و بالقواضم بودن‌را
نیز گویند.
آب طبرستان - بکسر ثاك »
چشمه‌است روان در کوهی که اکر بانگه , برآن
ود ند و چون فربادکنند پنهان خودوچون
طلب نمایند روان گزدد ؛ و این حنال هر هر
سای از آن چشمه مکرد بفعل میآید .
چشمه‌ایت که مدت هفت سال بیوستهروان‌باشد
و هفت سال دیگر خشك نود .
شراب انگوری باشد .
۲ ب‌عشر ت - بکس الك و عبن می
شمه » بىمنی آب طربست که شراب انگوری
باشد
! شت س بفتح ثالث بر وزن وارفت »
حخفف آبافت است که بارچه گنده و سطبر
باشد ۷ .-
آب سر ۵۵ - بکس تاك , کنایه‌از
-شنشی ی وخنجر باشد و شیشه و پلور و آبگینه
را نیز کویند .
] ها هد بت تالث بر وزن اوك ۰ مکی
از نلبهای سیماب است و آنرا آب و آیق
سس ۰ ۷..--
و ابوالارواح و اصل و االاجاد و پرنده و ده
و تیر وناقة (۱) وجوهر وجیوه و حل‌النهب(۷)
وحی‌الماء و روح و روحانی و رجراج و زارق(۳)
و ژموم (4) و ژبوه و ستاره و سحاب و نور (۵)
و سیماپ و طبار و عبد و عطارد و عین الحیوان
و غبیط وغیان وفرار و گریزنده ولین ولجلاح(»)
9 را نیز خوان که طفلان
پر هیآ ورند و صم ثالث هرچیز پر آیوآبکی
وا میگویشد .
یکااه - بسکون ثالث بر وزن آیبار ,
پمعنی سقا باشد - و شراب‌خوار (۷) و شراب
فروش - و حکاك - و نگین‌ساز را نیز کویند(۸)-
و بکسر ثاك » کنابه از رونق و رواج و آبرو
بلشد : #
۲ یکاهه - بر وزن کارامه . نان‌خورشی
است ممروف که در صقلعان (4) ازماست وشیر
و نم سپند و خمیر خشكث شده و سر که سازند
و آنرا جربی مری خوانند .
۲ یکافه - با بلی فارسی بر وزن تابشانه, "
بجه آدمی با حیوان دیگر که نارسیده از شکم
مادر سفئد .
۲ بگاه - بر وزن خوابگاه . تهیگاه
ظي هست ۰
خم ۳ : اسطخر .
۵ ]بکاری - سل آبکار, سقایت .
( ازافادات علامه فزوننی )
```


## [2026-09-06T16:08:51.535Z] TOOL CALL #40: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-06T16:08:51.542Z] TOOL RESULT

```


```


## [2026-09-06T16:08:53.145Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'سالان' in p:\n        print('LEAF',i)\n        import re\n        for m in re.finditer('سالان',p):\n            print('   ...',p[max(0,m.start()-200):m.start()+200].replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T16:08:54.861Z] TOOL RESULT

```
LEAF 215
   ...  کنایه از خوبی و نیکی مخفی - و رواج و دونق خس پوش هم حست باّب که خوبی ولیکی وقابلیت و کمال‌واستمداد و رواج و روفش مخفی و پزشیده است . " آ س « جختح تالث بر وزن فاکس , نم شهری و مدینه ایست نامملوم . آب سالان - بالام بر وزن آب پاشان, بممنی باغ باشد و بعربی حدیقه گوبشد ۴ . 2[ ددر پشتو (قی : ۰ بهاران) ۰
```


## [2026-09-06T16:09:08.421Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D8%B1%D8%AF",
 "prompt": "Give the full Persian etymology section for سرد (sard) 'cold' — Middle Persian, Old Iranian, Proto-Indo-European forms and any cited references. Also any Persian سرما entry."
}
```


## [2026-09-06T16:09:09.427Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D8%A7%D9%84",
 "prompt": "Give the full Persian etymology section for سال (sāl) 'year' — Middle Persian, Old Iranian, Avestan, PIE forms and cited references."
}
```


### [2026-09-06T16:09:15.182Z] TOOL RESULT

```
# Persian Etymology for سرد (sard) 'cold'

Based on the Wiktionary entry provided, here is the available etymological information:

## Documented Etymology

The Persian section states: "From Middle Persian _slt'_ (/⁠sard⁠/, 'cold')."

This represents the full etymological chain presented in the source material. The entry does not extend the etymology beyond Middle Persian to Old Iranian or Proto-Indo-European forms, nor does it cite specific references for the Middle Persian derivation.

## Related Entry

The page lists a derived term سردی (sardi), though this appears to be a nominal derivative rather than an etymologically distinct entry.

**Notable limitation:** The provided content contains no entry for سرما (sarmā), which is often cited as a related Persian word for "cold" in other lexicographic sources. The Wiktionary entry focuses exclusively on the documented Middle Persian ancestry of سرد without extending to deeper historical linguistic layers.
```


### [2026-09-06T16:09:19.104Z] TOOL RESULT

```
# Persian Etymology of سال (sāl) 'year'

## Etymology Tree

The documented lineage traces back through:

**Proto-Indo-European**: *ḱelh₁-* (uncertain reconstruction)

**Proto-Indo-Iranian**: *ćarHáts*

**Proto-Iranian**: *carHdáh*

**Old Persian**: 𐎰𐎼𐎭 (θ-r-d /⁠θard⁠/)

**Middle Persian**: 𐭱𐭭𐭲 (sāl)

**Persian**: سال (sāl / sâl)

## Direct Source Information

According to Wiktionary, the term derives "from Middle Persian 𐭱𐭭𐭲 (sāl), from Old Persian 𐎰𐎼𐎭 (θ-r-d /⁠θard⁠/), from Proto-Iranian *carHdáh, from Proto-Indo-Iranian *ćarHáts."

## Cited References

- MacKenzie, D. N. (1971), *A concise Pahlavi dictionary*, Oxford University Press
- Nourai, Ali (2011), *An Etymological Dictionary of Persian, English and other Indo-European Languages*, page 220
```


## [2026-09-06T16:09:29.538Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1elh%E2%82%81-",
 "prompt": "Give the reconstruction page content: the root *ḱelh₁-, its meaning, and all listed descendants (Indo-Iranian, Latin, Baltic, Germanic). Also note whether it is glossed 'warm' or 'cold' and any note about a homonymous root."
}
```


## [2026-09-06T16:09:30.708Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%AF%D9%88%D8%B3%D8%A7%D9%84%D9%87",
 "prompt": "Give the Persian etymology of گوساله (gūsāla) 'calf' — components, Middle Persian form, and any references."
}
```


### [2026-09-06T16:09:31.553Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T16:09:35.586Z] TOOL RESULT

```
# Persian Etymology of گوساله (gusâle)

Based on the Wiktionary entry provided, the specific etymological components and Middle Persian form are **not documented** in this source material.

The page shows that گوساله means "calf" in Persian and lists descendants in other languages (Chagatai, Gujarati, Khalaj, Ottoman Turkish), but it does not provide:

- Component breakdown
- Middle Persian antecedent form
- Historical etymology or linguistic references

The entry appears to be missing the etymological section that would typically explain the word's origin, development, and linguistic relationships across time periods.
```


## [2026-09-06T16:09:40.292Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/carHd%C3%A1h",
 "prompt": "Give the reconstruction page for Proto-Iranian *carHdáh: meaning, PIE ancestor, and all descendants (Avestan, Old Persian, Middle Persian, Sogdian, Ossetian, Khwarezmian etc.), and references cited."
}
```


## [2026-09-06T16:09:41.783Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B3%D8%B1%D8%AF%D9%86",
 "prompt": "Give the full Persian etymology of افسردن (afsordan) — Middle Persian form, prefix, root, meaning development, and any references (Cheung, MacKenzie, Hasandust)."
}
```


### [2026-09-06T16:09:47.838Z] TOOL RESULT

```
# Proto-Iranian *carHdáh

## Meaning
The reconstructed term means "autumn," "summer," or "year" (feminine noun).

## PIE Ancestor
Possibly derived from Proto-Indo-European *ḱelh₁- ("to warm up, to be hot"), with cognates including Latin *caleō* ("to be warm").

## Etymology
The word descends from Proto-Indo-Iranian *ćarHáts.

## Major Descendants

**Central Iranian:**
- Avestan: sarəδa ("year")

**Southwestern Iranian:**
- Old Persian: θ-r-d (θardaʰ, "year")
- Middle Persian: sāl
- Classical Persian: سال (sāl)
- Tajik: сол (sol)

**Northwestern Iranian:**
- Kurdish: sal
- Baluchi: sál

**Northeastern Iranian:**
- Ossetian: særd/særdæ ("summer")
- Khotanese: salä

**Other branches:**
- Sogdian, Parthian, Khwarezmian, and numerous other Iranian languages preserve cognate forms

## References
1. Mayrhofer, M. (1992–2001). "śarád-" in *Etymologisches Wörterbuch des Altindoarischen*
2. Wodtko, Dagmar S., et al. (2008). *Nomina im indogermanischen Lexikon*
```


### [2026-09-06T16:09:47.970Z] TOOL RESULT

```
Based on the Wiktionary content provided, here's the Persian etymology of افسردن:

**Middle Persian Origin:**
The word derives from Middle Persian *ʾpsltn'* (absardan), meaning "to cool down." The Wiktionary entry states: "From Middle Persian _ʾpsltn'_ (absardan, 'to cool down')."

**Root Connection:**
A related Middle Persian term is *slt'* ("cold"), suggesting a semantic connection within the proto-root family dealing with temperature reduction.

**Meaning Development:**
The archaic Persian verb افسردن carries the sense of "to cool down; freeze," representing a direct semantic inheritance from its Middle Persian predecessor.

**Limitations:**
The provided source material does not include detailed prefix analysis, references to scholarly works (Cheung, MacKenzie, or Hasandust), or deeper etymological reconstruction beyond the Middle Persian form. A comprehensive etymological study would require consulting specialized historical linguistics resources beyond this dictionary entry.
```


## [2026-09-06T16:09:55.057Z] TOOL CALL #48: WebSearch

```json
{
 "query": "Wiktionary Reconstruction Proto-Indo-European ḱelH- cold šaltas śiśira sarəta"
}
```


## [2026-09-06T16:09:56.507Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D9%84%D8%A7%D9%87",
 "prompt": "Give the full Persian etymology of کلاه (kolāh) 'hat' — Middle Persian form, any Proto-Iranian/PIE reconstruction, and references cited (Hasandust, MacKenzie, Horn, Hübschmann)."
}
```


### [2026-09-06T16:10:01.865Z] TOOL RESULT

```
Web search results for query: "Wiktionary Reconstruction Proto-Indo-European ḱelH- cold šaltas śiśira sarəta"

Links: [{"title":"Reconstruction:Proto-Slavic/xoldъ - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Slavic/xold%D1%8A"},{"title":"Reconstruction:Proto-Indo-European/(s)kelH- - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)kelH-"},{"title":"Reconstruction:Proto-Indo-European/ḱe - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1e"},{"title":"Reconstruction:Proto-Indo-European/ḱel- - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1el-"},{"title":"Reconstruction:Proto-Indo-European/ǵn̥h₃sḱéti - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5n%CC%A5h%E2%82%83s%E1%B8%B1%C3%A9ti"},{"title":"Reconstruction:Proto-Indo-European/h₂eḱ- - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82e%E1%B8%B1-"},{"title":"Proto-Indo-European desiderative","url":"https://en.wikipedia.org/wiki/Proto-Indo-European_desiderative"},{"title":"Proto-Indo-Iranian language","url":"https://en.wikipedia.org/wiki/Proto-Indo-Iranian_language"},{"title":"Proto-Indo-Aryan language","url":"https://en.wikipedia.org/wiki/Proto-Indo-Aryan_language"},{"title":"Proto-Indo-European language","url":"https://en.wikipedia.org/wiki/Proto-Indo-European_language"}]

I found relevant search results for your query. The Proto-Indo-European root *ḱelH- is cognate with Lithuanian šáltas ("cold"), Avestan sarəta, Persian sard, and Ossetian sald. This information comes from the Wiktionary article on Proto-Slavic *xoldъ, which discusses the etymological connections between these language forms and their proposed Proto-Indo-European origin.

The search results show that this PIE root is documented in Wiktionary's reconstruction articles, illustrating how this ancient word root for "cold" is reflected across various Indo-European language branches, including Baltic (Lithuanian), Iranian (Avestan and Persian), and Caucasian (Ossetian) languages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-06T16:10:03.798Z] TOOL RESULT

```
# Persian Etymology of کلاه (kolāh)

Based on the Wiktionary entry provided, here is the available etymological information:

**Middle Persian Form:**
The word derives from Middle Persian *kwlʾp̄* /kulāf/, meaning "cap" or "bonnet."

**Comparative Evidence:**
The entry notes cognates in Middle Armenian *sakʻulay* and Northern Luri *kelö*, suggesting a broader regional linguistic pattern.

**References Cited:**
The page explicitly references:
- MacKenzie, D. N. (1971), "kulāf" entry in *A concise Pahlavi dictionary* (Oxford University Press), page 52
- Dehkhoda Dictionary Institute materials

**Limitations:**
The Wiktionary article itself acknowledges gaps: "This etymology is missing or incomplete." It specifically notes uncertainty about potential connections to Persian *kal* (کل, "bald") and states that relevant Edelman scholarship isn't currently cited.

**Proto-Iranian/PIE Reconstruction:**
The provided content contains no Proto-Iranian or Proto-Indo-European reconstructions. Such deeper historical layers are not addressed in this particular Wiktionary entry.
```


## [2026-09-06T16:10:12.257Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1el-",
 "prompt": "List the distinct PIE roots spelled *ḱel- on this page: their meanings and main descendants. In particular, is there a root *ḱel- 'to cover/conceal' (Latin cēlāre, occulō, Greek kalúptō, Germanic hall/hell/helm) and a root *ḱel- 'cold' (Avestan sarəta, Lithuanian šáltas)?"
}
```


## [2026-09-06T16:10:13.673Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%83%D9%84%D8%A8%D8%A9",
 "prompt": "Is there an Arabic entry كلبة meaning hut/shed, and what does it say about Persian کلبه? Report any etymology given."
}
```


### [2026-09-06T16:10:20.436Z] TOOL RESULT

```
Based on the Wiktionary page provided, there is **no entry for كلبة meaning "hut/shed"**. The page only documents the Arabic noun كَلْبَة (kalba), which means "bitch" (female dog) — the female equivalent of كَلْب (kalb).

The page contains **no information about Persian کلبه or any etymology linking to Persian**. The "See also" section mentions only كَلْبَتَان (tongs/pincers), which is unrelated to a hut or shed.

To find information about كلبة as a hut/shed or its Persian cognate, you would need to consult a different source.
```


### [2026-09-06T16:10:20.601Z] TOOL RESULT

```
# Proto-Indo-European *ḱel- Roots

Based on the Wiktionary article, there are **two distinct homonymic roots** spelled *ḱel-:

## Root 1: "to cover"
This root means **"to cover"** and produces numerous descendants including:
- Germanic terms: *huljaną (to conceal), *helmô (helmet), *hallō (hall)
- Latin: *cella* (room/chamber)
- Greek: *kalúptō* (to cover)
- Sanskrit: *śárman* (shelter/protection)

## Root 2: "to incline"
This root means **"to incline"** with different reflexes:
- Germanic: *halþaz*, *hulþaz* (inclined, favorable)
- Baltic: Lithuanian *šalis* (side), Latvian *salis*
- Latin: *auscultō* (to listen)

The article does not address a separate "cold" root or discuss whether terms like Lithuanian *šáltas* connect to these roots. The two *ḱel-* entries shown represent distinct semantic categories, indicating these are homonymic roots rather than semantic variants of a single root.
```


## [2026-09-06T16:10:26.799Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA && grep -n -i \"kulba\\|kolba\\|qulba\\|kurba\\|kulbe\" PLA_pages.txt | head -20; echo \"=== page 233 ===\"; python3 - <<'EOF'\nt=open('PLA_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor i,p in enumerate(t):\n    if '233' in p[:200]:\n        pass\nEOF"
}
```


## [2026-09-06T16:10:28.025Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D9%84%D8%A8%D9%87",
 "prompt": "Give the Persian etymology of کلبه (kolbe) 'hut' — any Middle Persian, Greek, Arabic connection, and references."
}
```


### [2026-09-06T16:10:28.559Z] TOOL RESULT

```
12776:a             -       kurbaß:             "Laden,                 Schenkbude"                       pers.       ak           kulbe       3 mp.          ode kurpak           4
12779:&’-                   kurbag             = kurbaß                 q.     v.    5,
13081:—Lb_-           kulbak:              "Hütte,               Zelle,         Keller" <           pers. ab
=== page 233 ===
302
```


### [2026-09-06T16:10:36.294Z] TOOL RESULT

```
# Persian Etymology of کلبه (kolbe) 'Hut'

## Middle Persian Origin
The word derives from Middle Persian *kwrbg* (kurbag), meaning "humble dwelling, hut." The root carries the basic sense of "formed, shaped," connecting to Middle Persian *klp* (kirb, "body, form").

## Proto-Language Ancestry
The term traces back through Proto-Iranian *kŕ̥pš* and Proto-Indo-Iranian *kŕ̥ps*, ultimately deriving from Proto-Indo-European *krep-* meaning "body."

## Related Language Connections

**Ancient Greek**: The entry explicitly states this word is "unrelated to Ancient Greek καλύβη (kalúbē)" despite apparent similarity.

**Arabic**: Cognate forms exist in Arabic: كُرْبَق (kurbaq), قُرْبَق (qurbaq), and كُرْبَج (kurbaj).

**Avestan**: Related through Avestan 𐬵𐬎𐬐𐬆𐬭𐬆𐬞𐬙𐬀 (hukərəpta, "well-formed").

**Other Iranian borrowings** appear in Old Armenian, Old Georgian, and Georgian languages.

## References
The entry cites Dehkhoda Dictionary Institute and Christian Bartholomae's *Altiranisches Wörterbuch* (1904) as authoritative sources.
```


## [2026-09-06T16:10:45.440Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA && sed -n '12750,12800p' PLA_pages.txt; echo \"=== find page tag ===\"; awk 'NR<=12790 && /\\[pdf page/ {l=$0; n=NR} END{}' PLA_pages.txt; grep -n \"\\[pdf page\" PLA_pages.txt | awk -F: '$1<12790' | tail -3; grep -n \"\\[pdf page\" PLA_pages.txt | awk -F: '$1>13070' | head -3"
}
```


### [2026-09-06T16:10:47.126Z] TOOL RESULT

```
ol» - karäwän:                        Pl.       v.glyj karwän                          q. v.

           B4        _                                                 v4
Go!          - karäwin:                   Pl.     v. O)z)               karwän               q. v.


zu“             kirbäf:              "Reitpeitsche"                         pers.            32,


oLsl es
     kirbäs:                         "feine        weiße               Leinwand"                  pers.       a m.Ds   karbas
                                                                                                                       Zarbas   5, syr.
           Ks ‘pP, hebr. 097» ®,

1. Muhit          s.        v.
2.       Fraenkel           s.       v.
3.       Muhit    s.        v.
4A. al-MuCarrab                      s.     v.,    Ellenbogen                         s.     v.
5.       Mackenzie              s.    v.
6.       Ellenbogen              S.       v.
kirbäl                                                                                     228                                                           kurdistän

              _                                                                                2
ÖL,               - kirbäl:                   "Sieb"                     pers.          JL’garbäl            ı           syr.       Sn

         »-/                                                                                                         >
a             -       kurbaß:             "Laden,                 Schenkbude"                       pers.       ak           kulbe       3 mp.          ode kurpak           4

   2
&’-                   kurbag             = kurbaß                 q.     v.    5,

 w_/                                                                                                  /                  6
-                 kurraf:                "eine              Spielart"                    pers.o}          kore               .
              Karussell:                      "sich              im Kreis           drehende          Rundfläche                   mit        Reit-    od.    Fahr-
              sitzen            "frz.                       carrousel                    it.       carosello                 zu   ar.     kurradsch          zu   pers.
              kurrak             "Füllen"                    7,

     AG
&-                kurraß’            s    "Füllen"                    pers.             Srkurre mp.                          dı4 kurrag          8,

 Pa >                 4
ol,                   -        karhäna:             "Fabrik"              pers.                al» W kärbäne                      mp          Ls kar    ap.           kara
              + mp.             4m        Xanak              "Haus",

         >
2 - kard:                        "Hals"                 <        pers.        ©,        garden        Ic         mp.              ırO> gardan          10,

         Pr
24-               kurd:          "Kurde"                    ı1 <—T mp. „819                    kurtik       12,

os                        kirdär:             "Tat"              pers.        12          mp.       kardär        am.                   kar    14,
=== find page tag ===
```


## [2026-09-06T16:10:53.197Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA && sed -n '13060,13110p' PLA_pages.txt; echo \"=== grep kulah ===\"; grep -n -i \"kulah\\|kuläh\\|kolah\" PLA_pages.txt | head"
}
```


### [2026-09-06T16:10:53.262Z] TOOL RESULT

```
  .                  z                                                                       .£              PR
GEST            kaönl:           "hungrig                   sein"!          7 pers.               gurusne,
                                                                                                         as) goSne mp.                             EIAN
           gursnag                >rur guänag                     1

                                                                                          I _                                               BP}
A 7          kack:          "Biskuit,                  Torte"           <      pers.     JYkäk 2 ‚ syr.                    K&%o (pers. SIE)               3,
           dtsch.           Kuchen             /Keks,             engl.        cake    pers.           käk           4,

       ._/                                                                                                   .
Aa) - kufta:                     "Fleischbällchen,                             Kloß"          pers.     Ci                küftan    "schlagen,
           klopfen,              hacken"               Kg mp.Naı9 koftan,                      kob     ®,

                            u                                                                                    7
a2 - kafkag:                         "Ranunculus,                     Ranunkel;          Hahnenfuß"                  ‘.

       /
ae -              safikaf = kafkaf a. v.

Je                    kul-käsni:                      s.        käsnl     ®.
       _                                                                                                         / kolbe <Tmp. 983 kurpak,
—Lb_-           kulbak:              "Hütte,               Zelle,         Keller" <           pers. ab
           s.    qarbaq,              karbag               u.     karbaq.         9,


_AZb"-
      d, 7              x
                 kol5ikar:                  "Rosenzucker"                      pers.
                                                                                         10 eg pers.                      Yan
                                                                                                                           ygol "Blume,     Rose
                                                                                                                                                   n
           mp. Ip gul <T aw.varada.-                                      aram.        Lw.   wrd”     1,             pers._& Sikar s.              Sikar
           ar.     sukkar.


                kalafs           = karafs                  q. v.

       _
OJE”-            kulkün:              "wie            die        Rose"      pers.            ©,       gulgün s.               gul    in kolsikar          u.
           gün     in       asmänfün.                  12,


ri         kalam            =   karam            q.        v.




 1.    Mackenzie                 s.       v.
 2.    Wahrmund                 s.    v.,        TaCalibi                figqh    al-luga      s.     v.,        al-MuCarrab           s.   v.
 3.    Brockelmann                    Ss.      v.
4.     Littmann                 s.    v.
=== grep kulah ===
12351:ab.           gqulla:       "Spitze"          pers.        AK    kuläh       "Mütze"    9
```


## [2026-09-06T16:11:00.094Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA && awk 'NR>=13020 && NR<=13140' PLA_pages.txt | grep -n -E \"^[a-zA-Z].*[0-9]{3}\" | head; echo \"---explicit page numbers---\"; awk 'NR>=12980 && NR<=13140 {if ($0 ~ /23[0-9]/) print NR\": \"$0}' PLA_pages.txt | head"
}
```


### [2026-09-06T16:11:02.043Z] TOOL RESULT

```
---explicit page numbers---
12999: kasrawi                                                                      232                                                      ka$an
13059: kaSni                                                                             233                                                            kalam_
13119: kamäßa                                                                           234                                                              kinnär
```


## [2026-09-06T16:11:10.304Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in اکالیپتوس کالری شوفر شوفاژ; do echo \"=== $w ===\"; grep -o -m3 \".\\{0,180\\}$w.\\{0,180\\}\" MON_part1.txt MON_part2.txt 2>/dev/null | head -4; done"
}
```


### [2026-09-06T16:11:23.576Z] TOOL RESULT

```
=== اکالیپتوس ===
=== کالری ===
=== شوفر ===
=== شوفاژ ===
```


## [2026-09-06T16:11:26.706Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in کالیپتوس کالر شوفا اکالی; do echo \"=== $w ===\"; grep -o -m3 \".\\{0,120\\}$w.\\{0,120\\}\" MON_part1.txt MON_part2.txt 2>/dev/null | head -4; done; echo \"### file sizes\"; ls -la MON_part*.txt"
}
```


### [2026-09-06T16:11:39.825Z] TOOL RESULT

```
=== کالیپتوس ===
=== کالر ===
=== شوفا ===
=== اکالی ===
### file sizes
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
```


## [2026-09-06T16:11:46.659Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/eucalyptus",
 "prompt": "Give the full etymology of eucalyptus: who coined it, when, from what Greek elements, and why (the flower cover / operculum)."
}
```


## [2026-09-06T16:11:47.963Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/chauffeur",
 "prompt": "Give the full etymology of chauffeur and of chauffer/chauffage: French, Vulgar Latin *calefare, Latin calefacere, calere. Also give the etymology of calorie if mentioned."
}
```


### [2026-09-06T16:11:51.887Z] TOOL RESULT

```
# Etymology of Eucalyptus

**Coiner and Date:** French botanist Charles Louis L'héritier de Brutelle coined the term in 1788, with documented use appearing in 1789.

**Greek Components:** The word combines two Greek elements:
- *eu* meaning "well"
- *kalyptos* meaning "covered"

**Etymological Path:** Both elements trace to Proto-Indo-European roots: *eu* derives from *(e)su-* ("good"), while *kalyptos* comes from the PIE root *kel-* ("to cover, conceal, save").

**Botanical Motivation:** The botanist selected this name because it refers to "the covering on the bud." The eucalyptus flower features a distinctive operculum—a cap-like structure that covers the flower before it blooms, which inspired the descriptive nomenclature.
```


### [2026-09-06T16:11:54.256Z] TOOL RESULT

```
# Etymology of Chauffeur and Related Terms

## Chauffeur
The word "chauffeur" comes from French, originally meaning "stoker" or steam engine operator. It derives from French *chauffer* "to heat," which traces back through Old French *chaufer* to Vulgar Latin *calefare*, ultimately from Latin *calefacere* "to make hot, make warm," composed of *calere* "be warm" plus *facere* "to make, do."

As the entry notes: "literally 'stoker,' operator of a steam engine, French nickname for early motorists, from *chauffer* 'to heat.'" The term entered English in 1896 as a reference to motorists, with the professional driver sense developing by 1902.

## Chauffer/Chauffage
These related French terms share the same root. *Chauffer* means "to heat, warm up; to become hot," while *chauffage* would refer to heating (though not explicitly detailed in this source).

## Calorie
**Not mentioned** in the provided content. The etymology traces only back to Latin *calere* ("be warm"), but the specific term "calorie" and its etymology are not discussed in this article.
```


## [2026-09-06T16:11:59.697Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN calorie ===\"; grep -o -m2 \".\\{0,80\\}calorie.\\{0,400\\}\" KLN_1966.txt | head -3; echo \"=== KLN eucalyptus ===\"; grep -o -m2 \".\\{0,60\\}[Ee]ucalyptus.\\{0,400\\}\" KLN_1966.txt | head -3"
}
```


## [2026-09-06T16:12:02.529Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT hall ===\"; grep -o -m2 \"hall, a large room.\\{0,300\\}\\|HALL.\\{0,300\\}\" SKT.txt | head -3; echo \"=== SKT hell ===\"; grep -o -m2 \".\\{0,20\\}Hell, the place.\\{0,300\\}\\|hell, the abode.\\{0,300\\}\" SKT.txt | head -3; echo \"=== SKT conceal ===\"; grep -o -m2 \"Conceal.\\{0,300\\}\" SKT.txt | head -3; echo \"=== SKT color ===\"; grep -o -m2 \"Colour.\\{0,300\\}\\|Color,.\\{0,300\\}\" SKT.txt | head -3"
}
```


### [2026-09-06T16:12:06.642Z] TOOL RESULT

```
=== KLN calorie ===
ugrep: error: error at position 84
xbf][\x80-\xbf]*){0,400}
                        \___exceeds complexity limits


=== KLN eucalyptus ===
ugrep: error: error at position 90
\x80-\xbf][\x80-\xbf]*){0,400}
 exceeds complexity limits___/
```


### [2026-09-06T16:12:09.191Z] TOOL RESULT

```
=== SKT hall ===
HALLOW.
=== SKT hell ===
=== SKT conceal ===
Conceal ;  sec  Cell.
=== SKT color ===
```


## [2026-09-06T16:12:12.974Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nfor w in ['calorie','eucalyptus','Eucalyptus','chauffeur']:\n    print('==== ',w)\n    for m in list(re.finditer(w,t))[:2]:\n        print(t[max(0,m.start()-100):m.start()+420].replace('\\n',' '))\n        print('---')\nEOF"
}
```


### [2026-09-06T16:12:14.786Z] TOOL RESULT

```
====  calorie
  —  F.  calorique, fr.  L.  color,  ‘heat’.  See  calori-  and  -ic. Derivative:  caloric-ity,  n. calorie,  also  calory,  n.,  unit  of  heat.  —  See  calori-. calorifacient,  adj.,  heat-producing.  —  Com¬ pounded  of  calori-  and  -facient. Derivative:  calorifacient,  n. calorific,  adj.,  heat-producing.  —  F.  calorifique , fr.  L.  calorificus.  See  calori-  and  -fic. Derivative:  caiorific-ation,  n. calorifics,  n.,  the  science  of  heat.  —  See  prec. word  and  -ics. calorimeter,  n.,  an  app
---
subst.  suff.  -ite. langley,  n.,  a  unit  of  solar  radiation,  correspond¬ ing  to  one  gram  calorie  per  square  centimeter per  unit  of  time.  —  Named  after  the  American astronomer  Samuel  Pierpont  Langley  (1834- 1906). Langobard,  n.,  Lombard.  —  L.  Langobardi  (pi.), name  of  a  people  of  Northern  Germany.  See Lombard. langrage,  n.,  a  kind  of  shot.  —  Formed  on  anal¬ ogy  of  cartridge  fr.  earlier  langrel,  a  word  of unknown  origin. Derivative:  langrag-ed ,  adj. langsyne
---
====  eucalyptus
====  Eucalyptus
anary’,  celdre,  ‘to  hide, keep  secret'.  See  cell  and  cp.  caliology,  Calypso, apocalypse,  Eucalyptus,  kelyphite. calyx,  n.,  the  outer  whorl  of  leaves  (bot.)  —  L., fr.  Gk.  xoXu4,  ‘the  cup  or  calyx  of  a  flower’, which  stands  in  gradational  relationship  to x’iXiC,  ‘cup,  drinking  cup’,  and  is  cogn.  with  L. calix,  ‘cup,  goblet,  drinking  vessel’,  Umbr. skaice-ta,  scalse-to,  ‘out  of  the  dish  or  saucer’, OI.  kaldsah,  ‘pot,  cup’,  kalika,  ‘bud’.  OE.  celic, ctelic, 
---
  Paludicella. Cp.  also  caliology,  calyptra,  cilia,  clandestine, color,  conceal,  dharmsala,  Eucalyptus,  hall,  hell, helmet,  holster,  hull,  kalidium,  kelyphite,  kil-, occult,  superciliary,  Valhalla. Derivatives;  cell,  tr.  and  intr.  v.,  cell-ed,  adj. cella,  n.,  the  inner  part  of  a  temple  in  ancient Greece  or  Rome  (arch it.)  L.  See  prec.  word, cellar,  n.  —  ME.  celler,  fr.  OF.  celier  (E.  cellier), fr.  L.  cedarium,  ‘a  receptacle  for  food,  pantry’, prop.  neut.  of 
---
====  chauffeur
cicnt,  ca¬ lenture,  calescence,  callant,  calorescencc,  calo¬ ric,  caudle,  chafe,  chaldron,  chauffeur,  chawdron, chowder,  rechauffe,  scald,  nonchalant.  For  prob. 223 derivatives  of  base  *kleu-,  enlargement  of  base *kel-,  ‘warm’,  see  lee. Caleb,  n.,  masculine  PN.;  in  the  Bible,  one  of  the twelve  men  sent  by  Moses  to  spy  out  the  land of  Canaan.  —  Heb.  Kalebh,  prop,  ‘like  a  dog’, fr.  kelebh,  ‘dog’.  Cp.  Noldeke  in  ZDMG.,  40, p.164,  Note  1.  Cp.  Aram,  kalbi,  U
---
’. See  caldron  and  fact  and  cp.  calefacient,  calo¬ rific.  Cp.  also  chaff,  ‘to  banter’,  chauffeur,  re¬ chauffe. Derivatives:  chafe,  n.,  chafer  (q.v.) chafer,  n.,  a  vessel  for  heating.  —  Formed  fr. chafe  with  agential  suff.  -er.  Cp.  chauffer, chafer,  n.,  a  beetle.  —  ME.,  fr.  OE.  ceafor,  rel. to  OS.  kevera,  Du.  kever,  OHG.  chevar,  MHG. kever,  G.  Kdfer,  lit.  ‘gnawer’.  Cp.  MHG.  kiven, Du.  keveren,  ‘to  gnaw’,  OE.  ceafl,  ME.  chavel, G.  Kiefer,  ‘jaw’,  and  se
---
```


## [2026-09-06T16:12:26.020Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nimport re\nt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\n# find leaf containing 'sarəta' style or 'kel-' cold\nfor i,p in enumerate(t):\n    if 'sarəta' in p or 'sarata' in p or ('sarə' in p and 'kalt' in p):\n        print('HIT leaf',i, p[:120].replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T16:12:28.016Z] TOOL RESULT

```
leaves 895
HIT leaf 611 ghrSvi „Eber   gr. yoigog tritt Hellquist SvEO. 202 bei s. aber auch Persson
```


## [2026-09-06T16:12:32.313Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nimport re\nt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if re.search(r'\\b429\\b',p) and i>400:\n        print('leaf',i,'has 429')\nfor i,p in enumerate(t):\n    if 'sisira' in p or 'sisira' in p or 'saltas' in p or 'sdltas' in p:\n        print('CAND leaf',i,p[:150].replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T16:12:34.371Z] TOOL RESULT

```
leaf 419 has 429
leaf 437 has 429
leaf 444 has 429
leaf 512 has 429
leaf 517 has 429
leaf 518 has 429
leaf 573 has 429
leaf 595 has 429
leaf 793 has 429
leaf 794 has 429
leaf 824 has 429
leaf 832 has 429
CAND leaf 437                                                                     qers-   — kel-
```


## [2026-09-06T16:12:36.853Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[437][:3500])\nEOF"
}
```


### [2026-09-06T16:12:38.776Z] TOOL RESULT

```
                                                                    qers-   — kel-                                                                              429

mhd. hurmen siehe aber unter kormno- „atzende Fliissigkeit"), np. cardeh
„schwarzlich“,kari, karah „Schmutz“,                                                 pehl.                karic                „Mist“;                ai.    kalkd-h
„Kot,  Dreck, Ohrenschmalz   Siinde“,                         ;
                                                                                     ir.               corcach   „Sumpf*, arm. kork
„Schmutz, Mist“ (? wegen k- statt £-),                                               lit.              k'irnos ,.Sumpf, Morast“; vgl.
iihnliches unter ker-.
      Erw. konnen                   sein:„RuB“; ags. hriirn ds., y.aovvat
                                                     as. hrot,      ahd.    ruo-x,
                                                                                                                                                                     •




ftv£ai (Schleim) Hes., xagofivov fieXav Hes. (Fick KZ. 43, 139, Persson
Beitr. 750; der Ausgang von xaQvfivov ist zwar auffallig, aber Peterssons
aaO. Deutung aus *xaojh’o- trotzdem sehr unsicher, s. auch u. kerbero-,
qerbero „scheckig“, das wohl eine 6-Erw. unserer Wz. ist.


2. qers-             (und einfacher qer-) „Furchen ziehen“.
      Av.    kcLrayeiti „furcht ein, zieht“, afgh. karal „ackern, pfliigen";                                                                                  mit -s-
ai.       kariati „zieht Furchen *, krsdti „pfliigt‘, karsu-h                                                                 f.    ,Furche,                Graben“,
av. karsaiti           ,
                           furcht ein“, karsa- m. n. ,,Furche, Furchstrich,                                                                      -streifen (auf
dem Erdboden)" karsu- f. jjAckerland''; mit dieser ar Sippe (z. B. Fick I 4
187, Bartholomae Airan. Wb. 449, 457 f.) verkniipft Berneker 136 west-
slav. *cara in eech. car a ,.Linie“, coral i „Linien ziehen", osorb. tiara-
„Furche; Strich, Linie; Durchhau, Wildbahn im Walde* woneben mit -s-                                                                -

                                                                                                                                        ,


cech. alt. crcha mdartl. mahr. cert-ha ,Linie“; trotz der Beschrankung auf
das Westslav., die zunachst an Entlehnung denken laBt, ansprechend wegen
des ar und slav. Parallelismus zwischen s-losen dehnstufigen Formen und
schwacherstufigen mit -s.
   karsati usw nicht besser zu r eloov (Prellwitz 2 und Boisacq s. v. sowie
u. *</M „drehen“j.                           —
                      Eine Grdbed. , kratzen* und Gleicbsetzung mit qars-
„kratzen" ist zwar denkbar, aber solange fur letztere nicht e-Vokalismus
einigermaBen wahrscheinlich gemacht wird, nicht annehmbar.


1.        kel-   1.   „frieren, kalt“, 2. „warm“.
      1.    Ai. gicira- „kiihl,                        kalt“,      m. „Vorfruhling, kiihle                                         Zeit, Kalte, Frost“,
                                                                                                                      £
av. sardta-            ,,kalt“,               np. sard ds.,           osset. said                      „Kalte ‘, av. sara-ba- „Kalte
bringend“;             lit.
```


## [2026-09-06T16:12:45.710Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[437][3400:6500])\nprint(\"======== leaf 438 (p.430)\")\nprint(t[438][:1500])\nEOF"
}
```


### [2026-09-06T16:12:47.604Z] TOOL RESULT

```
     osset. said                      „Kalte ‘, av. sara-ba- „Kalte
bringend“;             lit.         sqlu,        >
                                                     sdlti   „frieren“        (lett.       salt),           sdltas                 „kalt“             (left,   salts),

salna „Reif“               pamlas „gefrorene Erde“
                           (lett.            sahvt),     apr. passalis „Frost“,                                      =
lit paszolys „Nachtfrost, Frost in der Erde
                                                                                           £
      .                                       abg. slana „Reif‘‘ (aber iiber                       ;

                                                                                                             £
abg. slota „naBkaltes Wetter“ s. u. him- „spiilen'      gegen Anreihung von                                      ;

abg. chinch ,,Kiihle“ s Berneker 393); aisl. lie I a „Reif    Jn-hlOn -, vgl. ai.
                                                                                                                                   £
                                                                                                                                            (.


ci-cira-)  Bezzenberger BB. 7, 76, Bugge Arkfnf. 2, 354 f.); ndl. hal n. ,.ge-
                 ;


frorener Boden                     ££
                   mit Dehnstufe P ahd. kali „schlupfrig, glatt
                                        ,
                                                                     nhd. bair.                                                                  ££
                                                                                                                                                      ,

                                                                                                                 ££
ha! ds., ags. hcelig ,,unzuverlassig“,                                      aisl. hall                 ,,glatt                (aber ags. halstan , an-
geblich „Kristall“ bleibt nach Holthausen Anglia Beibl. 15, 319 fern).
  Ygl. Fick I 4 44, 208, Zupitza Gutt. 181.  Eine daneben angenommene                          —
Wz. ker- „frieren,                            kalt“      scheint sich          in      urspriingliche Farbbezeichnungen
des weiBgrauen Reifs aufzuldsen,                                       s.    u. kero-                  .,Farbbezeichnung“.
                                                                                                                          £
      2.    Ai. carad-                  f.   ,.Herbst“,  av. sar./d- f. „Jahr“
                                                                  mit Zahlwiirtern „Jahr ,
(s. auch Solmsen KZ. 34, 78 zu 1yd. oagbiz ,,Jahr"), oosset. sard ,.Sommer“,
                           £
np. sal „Jahr („Herbst“ als ,,warme Zeit'
                               '
                                             Wood AlPh. 21, 182, ebenso                    £

                         
======== leaf 438 (p.430)
                            l        )                                            :     ;        -)




430                                                                kel-



sylii, silaii, silti            „warm werden"; lat. caleo, -ere „warm, heifi sein, gliihen",
calidus „warm, heiB", calrlor               „Warme, Hitze"; mir. clithe „aprieis", cymr.
clyd „calens, caloriticus"  Fick II 4 331; dazu vielleicht von einer e/-Erw.
                                            :




cymr. cl (tear „lauwarm, kiihl"? Persson Beitr. 793); as. haloian „brennen"
(Fick III 4 83f.). Im Germ, wurde eine Erw. *kleu fruchtbar (s. bes. Fick
III 4 109,  van Wijk IF. 24, 32 ff., Falk-Torp u. lunrner, lunlcen, ly Ice):                                          ,


abd. liio, fleet, haver „lau“, aisl. hlcer ds., vom Wetter (* Mnvia -), hi ana
„mild werden", bair. Juumn „tauen", aisl. hi aka „Tauwetter": aisl. hlyr
„lau“, My n. „Warme“, ags hleoive „lau‘       schwed. dan. norw. ly „warmer,
                                                                           ,


vor dem Wetter geschiitzter Ort", aisl. hie (* Jih-wa n. „Schutz, Leeseite",
as. hleo m. ,.Schutz vor dem Wetter", afries. hit, ags. hleo hleow n. ,0b-                                .


dach, Decke, Schutz" (vgl. auch mbd. liewe, lie f. „Laube“, schweiz. le
,,geschiitzte Lage, Son-nenseite", schwed lya „H6hle von Tieren"; diese

Worte    fiir „Schutz“ nicht besser nach Noreen Ltl. 32 an klei- „lehnen"

oder nach Zupitza Gutt. 1
```


## [2026-09-06T16:12:54.389Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (440,441):\n    print('==== leaf',i)\n    print(t[i][:2200])\nEOF"
}
```


### [2026-09-06T16:12:56.380Z] TOOL RESULT

```
==== leaf 440
432                                                          kel-



     Ygl. Curtius 5 148, Zupitza Gutt. 182,                               BB. 25, 90;             nicht iiberzeugendes
bei Prellwitz 2 220.                     *kohmo-s „Halm, Rohr", s. d. nicht
                             Yielleicht hierher                                                                        ;


in    der Bed. zu vereinigen wiiBte ich ai. galka- m. n. „Span, Abschnitzel,
Fischschuppe".


4. kel- „bergen, verhiillen".

     Ai. gams- n. „die Haut auf gekochter Milch, Rahm“, garand- „schirmend“,
n.    „Scbirm, Schutzdach. Hiitte", gar-man-                                 n.       „Schirm, Schutzdach, Decke,
Obhut" (: dt. Helm), dehnstufig (wie lat. celo cella ahd. hall) gala „Hutte,      ,           ,


Haus, Gemach" (aber kulayam „Geflecht, Neat, Gehause"           FickI 3 527,                                       —
nicht mehrl 4 386; II 4 83, Brugmann 1 2 456, 578, KVG. § 202 — ist im
Gutt. und in der ganz abweichenden Gdbed. unvereinbar, Curtius 140,
Persson Beitr. 727; verfehlte Gruppierungen bei Scheftelowitz ZdMG. 59,
707, s. Yf. LEWb. 2 u. cella)-, sehr unsieber ai. g&ta- m., g dtl „Tuch, Binde"
(Petersson St. zu Fortunatovs Regel 83).

   Gr. xaXrd „Hiitte, Scheune, Nest“ (aber arm. kal „Tenne“ bleibt fern,
a. Pedersen KZ. 38, 2(>3; 39, 380); hom. y.oXeov, metrisch gedehnt xovXeov,
att. xoXeog „Scheide" (*xoXefog, Solmsen Unt. 78     daraus lat. culleus mit              ;


ll als Ausdruck   des hellen gr. X, Boisacq u. xoXeog Nachtrag; aus dem
Lat. stammt rusa. huh, poln. kul „Sack“, daraus wieder lit. lulls ds., ku-
Vikas, apr. kuliks ,.Beutel“; s. Solmsen aaO. Yf. LEWb. 2 u. culleus    Ber-                                           ,


neker 642); mit Labialerw. y.aXvjiim „umhiille, verberge“, xaXv^rj „Obdach,
IIiitte“ (reimt mit xqvjitcd, doch scheint die Neuerung eher aufSeite des

letzteren zu liegen), xeXvcpog n. „Schale, Iliilse" (das v der 2. Silbe vielleicht
im Ablaut zu *xoXep-og                ,
                                            Bechtel Lexil. 197, der zw. auch germ, helu- in
ags     helush-     vergleicht,           s. auch u. mir. cm/; Labial 
==== leaf 441
            ;                                                                                                             :




                                                         qel-                                                           433

  Air. celim „verberge“, cymr. celu ,.verbergen“ (Formenbestand s. bei
Pedersen KG. II 482 ff.), air. cuile „Keller, Magazin' und „Kuche‘ (auch
in letzterer Bed. formell nicht aus lat. culina herleitbar nach Pedersen
KG. II 111; aber doch wohl in der Bed. da von beeinflufit), mir. had ar
cel „obiit‘, eigentlich „zur Holle fahren“ (vgl. as. usw. he.lliu .JJnterwelt",
schwed. sla i hjall „totscblagen“, nicht besserzu gr. zelog Ende‘ B bei Fick                        ,       ,


II 4 83 zw.); mir. cul „Schutz‘, culaid „Hulle‘' (Stokes BB. 19, 63; scheint
*colu- zu sein. s. o.), wohl auch cohim, Dat. PI. colomnaib .,skin, hide                                                  -1



(Stokes KZ. 41, 383) und cuilche „Hantel t: ( *kolikia Stokes IvZ. 40, 247).            ,


     Ahd.   as.    ags. „verbergen“, woneben von einem Aoristpraesens
                          helan
*hulan, got. hulundi ,,Hohle“ (,die bergende*; aber ahd. usw. hoi „hohI                                                       ,



got. ushulon ,,aushohlen“ vielmehr zu *qaid- „hohl, HohlstengeU     Yer-                                           ;



bindung mit cclare z. B. bei Zupitza Gutt. 185, Uhlenbeck Got. Wb. s. v.,
zw Fick III 4 80 f., Falk-Torp u. hid .,hohl“;                                   s.   dagegen L. Meyer                 GGN.
1906, 187),        got. huljan,        anord. hylja , ahd. hullcn ,,verhullen‘,                                 wovon mit
germ. Suff. -stra-, got. hulistr n. ,Hiille, Decke“; auf einem alten -es-St.
(s. lat. color ) beruhen hingegen wohl mhd. hidst f.     Decke, Hiille'‘ (aber              ,




nd. holster mit si fur ft zu mhd. hidfter     s. u. und Falk-Torp
                                                                ,  u. hylster)
und sicher mnd.            lndse,      ahd.      hidsa   ,
                                                             hulls          „IIiilse“           (ags.   helust ,   he
```


## [2026-09-06T16:13:07.632Z] TOOL CALL #69: Bash

```json
{
 "command": "ls site/pages/250.jpg 2>/dev/null; pdftoppm -f 250 -l 250 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg250 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T16:13:10.469Z] TOOL RESULT

```
site/pages/250.jpg
total 10588
drwx------ 7 sfmqrb sfmqrb    4096 Sep  6 12:13 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    1144 Sep  6 12:09 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  180887 Sep  6 11:56 bqt1637_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   50592 Sep  6 11:56 bqt1637_kaz.png
-rw-rw-r-- 1 sfmqrb sfmqrb  181961 Sep  6 12:11 bqt1688_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb  340758 Sep  6 12:11 bqt1709_fn2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  280452 Sep  6 12:11 bqt1709_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   92182 Sep  6 10:55 bqt1854.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66580 Sep  6 10:57 bqt2023.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69965 Sep  6 11:25 bqt2242crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   28189 Sep  6 11:25 bqt2417crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  431133 Sep  6 11:16 bqt2420_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9548 Sep  6 11:25 bqt2meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb   81018 Sep  6 11:16 build213.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67391 Sep  6 11:49 build225.py
-rw-rw-r-- 1 sfmqrb sfmqrb   71757 Sep  6 11:47 build232.py
-rw-rw-r-- 1 sfmqrb sfmqrb   49952 Sep  6 11:57 build234b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   32265 Sep  6 11:51 build234.py
-rw-rw-r-- 1 sfmqrb sfmqrb   24770 Sep  6 12:01 build243.py
-rw-rw-r-- 1 sfmqrb sfmqrb    6504 Sep  6 11:13 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3402 Sep  6 11:22 c224_n10.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4812 Sep  6 11:28 c224_n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4744 Sep  6 11:22 c224_n1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3203 Sep  6 11:28 c224_n7.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12820 Sep  6 11:27 c229_bibua.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5308 Sep  6 11:27 c229_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5313 Sep  6 11:27 c229_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9059 Sep  6 11:50 c237_n18.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2389 Sep  6 11:50 c237_n3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4987 Sep  6 11:52 c239_kandid2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4734 Sep  6 11:52 c239_kandid.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12852 Sep  6 11:52 c239_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4087 Sep  6 11:52 c239_sandarus.png
-rw-rw-r-- 1 sfmqrb sfmqrb   15240 Sep  6 11:54 c246_caiique.png
-rw-rw-r-- 1 sfmqrb sfmqrb   36354 Sep  6 12:02 c246_casaque.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84366 Sep  6 11:54 c246_n2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   51690 Sep  6 11:54 c246_n6.png
-rw-rw-r-- 1 sfmqrb sfmqrb   13719 Sep  6 12:02 c248_p3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   30759 Sep  6 12:02 c248_p4.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2750 Sep  6 12:02 c248_persian2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3046 Sep  6 12:02 c248_persian.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb  169482 Sep  6 11:58 crop_1648b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   45260 Sep  6 11:57 crop_1648.png
-rw-rw-r-- 1 sfmqrb sfmqrb  305924 Sep  6 11:57 crop_1731.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb     724 Sep  6 12:11 drive.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb   64267 Sep  6 11:59 mk235.py
-rw-rw-r-- 1 sfmqrb sfmqrb   73422 Sep  6 12:02 mk237.py
-rw-rw-r-- 1 sfmqrb sfmqrb   81037 Sep  6 12:03 mk240.py
-rw-rw-r-- 1 sfmqrb sfmqrb   80347 Sep  6 12:08 mk242.py
-rw-rw-r-- 1 sfmqrb sfmqrb   58802 Sep  6 12:07 mk244.py
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:44 p216
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:52 p233
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 12:12 p245
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 12:12 p249
-rw-rw-r-- 1 sfmqrb sfmqrb   33321 Sep  6 11:51 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb   30335 Sep  6 12:07 part2.py
-rw-rw-r-- 1 sfmqrb sfmqrb   38036 Sep  6 12:11 part3.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb  125593 Sep  6 11:50 pg237hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67972 Sep  6 11:50 pg237.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168221 Sep  6 11:52 pg239hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81026 Sep  6 12:03 pg239.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83594 Sep  6 12:03 pg239_small.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81131 Sep  6 11:51 pg240.png
-rw-rw-r-- 1 sfmqrb sfmqrb   97613 Sep  6 11:49 pg242.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80947 Sep  6 11:59 pg244.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80632 Sep  6 11:55 pg245.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79253 Sep  6 11:54 pg246.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64208 Sep  6 12:04 pg247.png
-rw-rw-r-- 1 sfmqrb sfmqrb  142780 Sep  6 12:02 pg248hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   49887 Sep  6 12:02 pg248.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82530 Sep  6 12:05 pg249.png
-rw-rw-r-- 1 sfmqrb sfmqrb   89076 Sep  6 12:13 pg250.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75263 Sep  6 12:04 pg251.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74772 Sep  6 12:13 pg252.png
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 12:12 __pycache__
-rw-rw-r-- 1 sfmqrb sfmqrb 1209522 Sep  6 11:39 sin_goog.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  147680 Sep  6 11:20 sns167.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   53545 Sep  6 12:03 w241.py
```


## [2026-09-06T16:13:13.676Z] TOOL CALL #70: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg250.png"
}
```


### [2026-09-06T16:13:14.159Z] TOOL RESULT

```

```


## [2026-09-06T16:13:14.157Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T16:13:30.932Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 250 -l 250 -r 400 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg250hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg250hi.png'); print(im.size)\nw,h=im.size\nim.crop((int(0.20*w),int(0.24*h),int(0.42*w),int(0.30*h))).save('c250_sarez.png')\nim.crop((int(0.20*w),int(0.58*h),int(0.55*w),int(0.66*h))).save('c250_kolba.png')\nim.crop((int(0.20*w),int(0.70*h),int(0.42*w),int(0.76*h))).save('c250_celare.png')\n\""
}
```


### [2026-09-06T16:13:34.345Z] TOOL RESULT

```
(3400, 4400)
```


## [2026-09-06T16:13:36.753Z] TOOL CALL #72: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c250_sarez.png"
}
```


### [2026-09-06T16:13:36.766Z] TOOL RESULT

```

```


## [2026-09-06T16:13:37.704Z] TOOL CALL #73: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c250_kolba.png"
}
```


### [2026-09-06T16:13:37.724Z] TOOL RESULT

```

```


## [2026-09-06T16:13:44.680Z] TOOL CALL #74: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg250.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/250.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -3"
}
```


### [2026-09-06T16:13:44.749Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-06T16:13:46.061Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(533,540):\n    p=t[i]\n    import re\n    if re.search(r'\\b45[89]\\b|\\b46[01]\\b',p):\n        print('LEAF',i,'---')\n        print(p[:2500])\n        break\nEOF"
}
```


### [2026-09-06T16:13:47.716Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T16:13:52.022Z] TOOL CALL #76: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/250.png; cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"καλύβη\\|kalube\\|kalybe\\|xaAvBn\\|HUT\\b\" SYN.txt | head -10"
}
```


### [2026-09-06T16:13:52.075Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/250.png
11562:460 SELECTED INDO-EUROPEAN SYNONYMS 7.13 HUT
21642:12.25 SHUT, CLOSE (vb.)
```


## [2026-09-06T16:13:54.079Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11555,11600p' SYN.txt"
}
```


### [2026-09-06T16:13:54.123Z] TOOL RESULT

```
From other languages the following may be mentioned as approximating ‘home’ and not listed under ‘house’.
Words for ‘fireplace, hearth’ (7.31) as symbolic of the ‘home’ (cf. NE fight for their firesides). So often Grk. éovia, Rum. cdémin, etc.
NIr. baile ‘town, village’ (19.16), also ‘home’, as in ag baile ‘at home’.
W. cartref ‘home’, gartref ‘at home’, epd. of MW gar beside ger, ker ‘at’ and tref ‘home, town’ (: Ir. trebaim ‘inhabit, cultivate’, 7.11).
ketuar ete.
Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
460 SELECTED INDO-EUROPEAN SYNONYMS 7.13 HUT
K xadla, xrol: Goth. ove Lith. bakuze, grytia ce ce xadtBn 5 ON kofi, kot Lett bida Lat. casa, tugurium Dan.  hylte Ghsizae . It. casupola, tugurio, Sw. hydda SCr. koliba
capanna OE cot Boh.  chatré, chalupa
Tr. hutle, cabane ME cot, hutte Pol. —chalupa, chata, buda Sp. huta, cabaiia, choza NE hut Russ. chiZina, latuga Rum. colibd, bordeiu Du. hut Skt. kuti-, cala- Ir. both, bothan OHG hulta Av. irae oe NIr. both, bothan MHG hiilte W. bwth, cwt NHG hiille
Br. log, logell
Words for ‘hut’ are from those denot- ing ‘cover’, ‘rounded or hollow shape’, or some special manner or material of con- struction. Some are diminutives of those for ‘house’.
1. Grk. xadvBy fr. the stem of xadirrw ‘cover’, also xadia and Skt. cala- ‘house, stall, hut’ fr. the same root, IE *éel- ‘cover, hide’ in Lat. occulere, célare, Ir. celim, OE helan, etc. (12.26, 12.27). Walde-P. 1.482 ff.
NG xadtBa is, through Turk., the source of SCr. koliba, Rum. colibd, etc. Berneker 546.
Grk. wAicla, Hom. xdtcin (‘hut’, also ‘couch’) : kXtvw ‘incline, recline’, xAivn ‘couch’, Goth. hleibra ‘tent? (7.14), etc., IE *flei-. Walde-P. 1.490. Boisacq 470 f.
2, Lat. casa, etym. dub., perh. as orig. ‘wickerwork’, fr. *kat- in Lat. caténa ‘chain’, cassis ‘net’, etc. Walde- P. 1.338. Walde-H. 1.175 f.
It. casupola, dim. of casa, after it had become ‘house’, REW 1752.
Lat. tugurium (> It. tugurio), teguri- um, fr. tegere ‘cover’ (12.26). Ernout-M. 10.20.
Late Lat. capanna (Isid. 15.12.2 tugu- rium casula est... . hunc rustici capan- nam vocant), orig. dub., perh. fr. cannaba ‘booth’ with form influenced by capere. Hence It. capanna, Sp. cabafia, NE cabin, ete. Ernout-M. 146. Walde-H. 1.156. REW 1624.
Fr. hutte, Sp. huta, fr. Gmc. (below, 4).
Sp. choza, chozo, fr. Lat. pluteum ‘shed’. REW 6619. Otherwise (fr, Arab. huss ‘straw hut’) Lokotsch 887.
OFr. borde ‘booth, hut’, bordel ‘hovel, brothel’ (> ME bordel, It. bordello ‘brothel’) fr. Gme. bord ‘board’. Here also prob. (but through Bulg. bordej) Rum. bordeiu ‘mud hut’? REW 1216.
3. Ir., NIr. both, bothan: W. bod ‘dwelling’, ON bad ‘dwelling’, ME bape, bothe ‘hut, tent’, NIE booth (> W. bwth), NUHG bude ‘booth’ (> Pol., Russ. buda ‘booth, hut’ > Lith. bada ‘booth, tent’, Lett. bida ‘hut’), Lith. butas ‘house’, Goth. bauan ‘dwell’, etc. (7.11). Walde- P. 2.142. Pedersen 1.35.
W. cwt, fr. OF, ME cot (below, 4).
Br. log, logell, fr. Fr. loge (OFr. ‘arbor, bower’, also ‘hut’, cf. Godefroy), this fr. Gme. laubja (NHG laube). Loth, Mots lat. 182. REW 4936.
4. ON kofi : OF cofa ‘a room’ (also ‘hollow in the rock’, later ‘recess on the coast’, NE cove), MHG kobe ‘stall, cage’, Grk. yz ‘hole, cave, hut’ (Hesych.), fr. an extension of IE *geu-, as in the fol- lowing. Walde-P. 1.561. Falk-Torp 570, 1500.
ON kot (ODan. kod ‘hovel’), OF, ME cot (also cote, NE dovecote, etc.), MLG kot, kote (NHG kot, kote ‘hovel’, Du. kot ‘hovel, sty, kennel’; fr. Gme., OFT. cotage > NE cottage), fr. an extension of IE *geu- in words denoting hollow
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
DWELLI
Walde-P. 1.555 ff., 560. NUG hiitte (> Fr. ONE hut, Sp. huta; also ODan. hudde, Ik. Kevdw, OE hiydan ly connected 12). Walde-
all : Gr C an 0) ultimate bn jias ‘house’ ete. (7.
» Alminauskis 28.
grincia, shortened form ‘servants hall’, ‘smoke- Russ. *gridnica. Berneker
6 Boh. chairé beside dial. chat’ = Pol., Russ dial. chata, loanword fr. Iran., Av.
NG, HOUSE, FURNITURE
igitized by Arya Samaj Foundation Chennai and eGangotri
461
kata- ‘chamber, storeroom’, NPers. kad ‘house’. Berneker 385 f.
Boh. chalupa, Pol. chatupa, orig. dub. Berneker 383. Brickner 175 f.
Russ. chizina, dim. of chiza : Ukr. chyza ‘hut’, ChSl. chyzt ‘house’, Bulg. hiza ‘hut’, etc., early loanword fr. Gmc., OHG his, ete. (7.12). Berneker 414. Stender-Petersen 240 ff.
Russ. laéuga, older alaéuga, fr. Turk. alaéuk ‘hut of cloth or bark’. Berneker 682. Lokotsch 49.
7. Skt. kuti-, kult- fr. *krti- : Skt. krt- ‘twist’, Grk. xaprados ‘basket’, Lat. cratis ‘wickerwork’, ete. Walde-P. 1.421.
Skt. cald-, above, 1.
7.14 TENT
amy Goth. Aleipbra, hlija Lith. palapine, Selra ‘oe ON tjald Lett. telis _ ;
```


## [2026-09-06T16:14:03.822Z] TOOL CALL #78: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A7%DA%A9%D8%A7%D9%84%DB%8C%D9%BE%D8%AA%D9%88%D8%B3/",
 "prompt": "Report what فرهنگ معین (Mo'in) and other dictionaries on this page say for اکالیپتوس — the definition and the origin tag (e.g. [فر.] French, [يو.] Greek)."
}
```


## [2026-09-06T16:14:05.489Z] TOOL CALL #79: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B4%D9%88%D9%81%D8%A7%DA%98/",
 "prompt": "Report what فرهنگ معین (Mo'in) says for شوفاژ — the definition and the origin tag (e.g. [فر.] French chauffage). Also anything for شوفر."
}
```


### [2026-09-06T16:14:10.391Z] TOOL RESULT

```
# فرهنگ معین Definition of اکالیپتوس

**Definition:**
According to فرهنگ معین, اکالیپتوس is described as "درختی از تیرة موردی ها، همیشه سبز با برگ های دراز و نوک تیز مانند بید" (an evergreen tree from the Myrtaceae family with long, pointed leaves resembling willow). The entry notes that decoctions of fresh or dried leaves are beneficial for respiratory conditions, flu, and other ailments.

**Origin Tag:**
The entry includes the notation **(اُ) [لا.] (اِ.)**, indicating:
- **(اُ)** — Persian pronunciation marker
- **[لا.]** — Latin origin
- **(اِ.)** — Indicates borrowed/foreign word

The term derives from Latin/Greek roots and entered Persian as a borrowed scientific term in botanical nomenclature.
```


### [2026-09-06T16:14:10.710Z] TOOL RESULT

```
# فرهنگ معین Definition of شوفاژ

According to Farhang-e Mo'in, شوفاژ is defined as:

**Origin:** "[فر.]" (French origin)

**Definitions:**
1. "گرمایش" (heating/warmth)
2. "هر یک از رادیاتورهای سیستم حرارت مرکزی" (each radiator in a central heating system)

---

## Note on شوفر

The provided content does not contain any dictionary entry or definition for **شوفر** (chauffeur). Only شوفاژ (chauffage/heating system) is documented in the materials shown.
```


## [2026-09-06T16:14:21.486Z] TOOL CALL #80: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A2%D8%A8%D8%B3%D8%A7%D9%84/",
 "prompt": "Report what Dehkhoda and other dictionaries say for آبسال and آبسالان: meanings ('spring'? 'garden'?), the Vis-o-Ramin or other verse quotations, and any etymology or reference to Borhan-e Qate'/Mo'in."
}
```


### [2026-09-06T16:14:24.782Z] TOOL RESULT

```
The server returned HTTP 400 Bad Request.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-06T16:14:27.959Z] TOOL CALL #81: WebFetch

```json
{
 "url": "https://vajehyab.com/dehkhoda/%D8%A2%D8%A8%D8%B3%D8%A7%D9%84",
 "prompt": "Report the Dehkhoda entry for آبسال (and آبسالان): meanings, verse quotations (e.g. from Vis-o-Ramin or Asadi), and any etymological note."
}
```


### [2026-09-06T16:14:32.918Z] TOOL RESULT

```
# Dehkhoda Entry for آبسال

Based on the webpage content provided:

**Meaning:** According to Dehkhoda's dictionary, آبسال is a compound word (اِ مرکب) meaning "garden" or "orchard" (باغ، حدیقه).

**Verse Quotation:** The entry includes a poetic example from Nasir Khosrow:
> "همی تابد ز چرخ سبز عیوق / چو آتش بر صحیفه ی ْ آبسالی"

This verse illustrates the word's usage in classical Persian poetry, showing how the term was employed to describe a garden-like setting within a literary context.

**Etymology:** No explicit etymological note is provided in this particular Dehkhoda entry excerpt.

The entry demonstrates that آبسال functioned as a poetic term for garden spaces in medieval Persian literature.
```


## [2026-09-06T16:14:51.074Z] TOOL CALL #82: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/%D8%B3%D8%B1%D8%AF' \\\n 'https://en.wiktionary.org/wiki/%D8%B3%D8%A7%D9%84' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/carHd%C3%A1h' \\\n 'https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B3%D8%B1%D8%AF%D9%86' \\\n 'https://en.wiktionary.org/wiki/%DA%A9%D9%84%D8%A7%D9%87' \\\n 'https://en.wiktionary.org/wiki/%DA%A9%D9%84%D8%A8%D9%87' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1el-' \\\n 'https://www.etymonline.com/word/eucalyptus' \\\n 'https://www.etymonline.com/word/chauffeur' \\\n 'https://abadis.ir/fatofa/%D8%A7%DA%A9%D8%A7%D9%84%DB%8C%D9%BE%D8%AA%D9%88%D8%B3/' \\\n 'https://abadis.ir/fatofa/%D8%B4%D9%88%D9%81%D8%A7%DA%98/' \\\n 'https://vajehyab.com/dehkhoda/%D8%A2%D8%A8%D8%B3%D8%A7%D9%84' ; do\n python3 tools/fetch_source.py \"$u\" --note 'pdf page 250 (book 220), roots Kel 1 / Kel 2 verification' 2>&1 | tail -2\ndone"
}
```


### [2026-09-06T16:14:59.039Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/74baa7997e3fc27b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f0574db3bcc6edf4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9c48fdf2d09edbd8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/205db3294280a2bd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3b969fa08921be27.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d74225474a7c0c80.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d75b2693ecaac0a8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/14d9f6da68b94717.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e73c16a507a869c0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6ed87b4118a6f9da.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b06f78c60713ad53.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6bf3f04e55d9124e.txt
```


## [2026-09-06T16:15:09.500Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i,p in enumerate(t):\n    if 'افسرد' in p:\n        print('LEAF',i)\n        for m in re.finditer('افسرد',p):\n            print('  ...',p[max(0,m.start()-250):m.start()+250].replace('\\n',' '))\n        print()\nEOF"
}
```


### [2026-09-06T16:15:12.346Z] TOOL RESULT

```
LEAF 56
  ...  قول خطاست ۰ وموّ لف مجبل التواریخ و القصص رد : چون جبرئیل علیه السلام کیش بیاورد وابراهیم قر بان کرد...» موّلف «موّ بدا لفضلاء > گوید ۷ :«استوده» بالضم با واو فارسی استه؛ نيك آوردن و نيك آمده.وماندگی گر فته. > وجای دیگی گویها : < استوه» مانده شده‌و افسرده و تنگ آمده وملول.» و بدیهی است که « استوده > بجای «استوه» غلط است. و هم او آرد :۰ستور» دستور بعنی‌صاحب دست ومسند؛ 4 مولف فرهنگ انندراج در لت 2 ید خت > آورده : «ستاره زهر هرا و وظن مولف آنست که آن نیز هیدخت بوده مانند بیدخ تصحیف خوانی شده چه دخ

LEAF 624
  ... زن ی رکاله ؛ بععنی حصه وبهرء ولخت وپاره باشداز هرچیز - وپاره و وسلهرا تیز گوبند که برجامه دوزند ودر عربی رقعه خوانتد ؟ . فر ۵ - بفتح اول و سکون ثانی و هیم . ببعنی کوه باشد که بعربی جبل خوانند. وبکسر اول حم آخفة 0 ۳ مان ۴ « بکسراول بروزن کرمان» بممنی افسرده و بی رونق و غمن‌الث و مخمور واندوهگن باشد ۵ , وباینمعئی بفتح اول وضم اول هردو آمده است - ویضم اول بمعنی‌خواهض واوژه هم کفثداند ۰ لژ ما4 متح اود بر وزن عمسایه . کاوی که فربدون راشیر میداد وبکسر اول هم آنفد است ۹ 4 بر هر ده مکش اول وضم میم بروزن
```


## [2026-09-06T16:15:17.734Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(357,363):\n    print('==== LEAF',i)\n    print(t[i][:900])\nEOF"
}
```


### [2026-09-06T16:15:19.650Z] TOOL RESULT

```
==== LEAF 357
_ٍِِ
اشکو خیدن . مصدر اشکوخ است
که لفزیدن دبسردرآمدن وافتادن‌باشد , چها کر
کی را پایش از یش بدد رود و یفئد گویند
اشکوخیه .
اشکو 4 ه بن اول , بسنی شکوفه
و بهار درخت باشد - و فی و استفراغ را لبز
گویشد ۱.
اشکوه « بنم اول والث وسکون تانی
و واو و ها ء بمعنی شآن و شوکت و شکوه
وعنلمت باشد ۴ .
اشکیل؟ بکراول وثاكك وسکون‌الی
وئحتانی ولام » بمعنی اک ات وان اسبی‌بود
که دست راست وپایچپ او سفید باشد - ومکر
وحبله وفریب را نیز کویند .
اشکیل چشم - اشکیل مملوم و نتح
جیم فارسی وشم شین قرشت وسکون‌ميم. دوایی
است که آیرا عوسج کوبند جاگ بر کف ای را
بکوبند و آب آنرا بگیرند و هفت دوز درچشم
چکانند مفیدی چشم کد هم رسیده باشد زایل
گنت -
اشکیوة » بنتح اول و سکون انی
وثالث وبای حطی بواو رسیده وبدال زده» مر کب
را گوبند که درمة بل‌مفرد است ؟ .
اشمو‌سا - بفتح اول و سن بی نفطه
بالف کشیده بر وزن محمودا ۰ بلفت بونانی نوعی
از مرو باشد که آنرا بشیرازی مرورشك خوانند
و بوی‌آن کمتر از مرو خوش‌باشد .
۵ و _
6 رك . آشنا . 1
فرهنگه
==== LEAF 358
اشو ی
که کمانگران بر باژوی از جابدر رفته ‏ بندند
واشق معربآشت .
اشتاف مامثا بنتح اول و کسرفاه
یعنی عصاره مامثا ومامیئا بلغت سربانی‌نام رستنی
باشد که آنر! درفااضات بکاربرند وآنرا زهبانالی
که درئواحی موصل میباشند سازند . درد چشم
و ناقم افننت. ‏
اشیهه - بفتح اول وکسر‌انی بتحانی.
رسیده و های مقتوح » آواز هو شيهه اسب را
قز بر 9
هم حست خوشبوی که آنرا دواله میگوینه
وبعربی شبیه‌السجوز ومكك‌القرود خوانند» مانند
عثقه ولبلاب بردرخت یچد و اکر بسایند و ور
چشم کشند چشم‌را جلادهد. *#
اشو۱ بفتح‌اول وضم‌ثانی بواو رسیده,
بلخت زند ویازند (۱) بمعنی بهشتی باشد که در
حقایل دوزخی است ۷
اه ۳ ی یی
شوع < بضم اول بروزن دروغ» شخص
عجپول‌النسب وء‌فقودالیلد را گوند؟ ۰
اشه ه تسم اول وفتح ئالی , گساهی‌است
بیان پانز دهم _
در همزه باصاد بی‌تقطه مشتمل بر نه لغت
اصابع فرعقن - سنگی است مانند
انگشت آدمی و آنرا از بحرحجاز آورند و بعربی
امالالخراح گونند .
شهربت مثهور در عراق و نام اصلی او این
است؟ - ونام عقامی است از جملهةٌ دوا
==== LEAF 359
۳و
معتی امتضر است که قلمةٌ فاری باشد و آن
که داراین داراب‌استت هاگن وتالابرا لس
گویند .
اصطر خ" س بروزن ومعنی استخراست
که فلمة فارس ناشدب وتالابو آبگررا نز گووند.
سمفی است سرخ بسیاهی حابل و بسنی گویند
صمغ درخت زیتون است . نزله را نافم است .
اصطر لاب - ممروف است و آن
آلتی باشد ازیرنج وتال ساخته که منجمان‌بدان
ارتفاع آفتاب و کواکب معلوم کنند و این لفت
بونالی است بمعنی نرازوی آفتاب چه اصطرترازو
اطماط
ولاب نام آفتاب است؟ - و بعضی کویند نام پس
ادریس علیه‌الملام(۱) است که واضم اصطرلاب
ت ۱
اصطقی بفتح اول وثالث وفا ونحتالی
اکن » بلغت بونانی صمتی است که ماشد عود
بوزد و جریی میم سائله گوبند و بسل لبن
اشتهار دارد .
اصطفیی - بفتح اول و الث بر ون
درکزین» بلفت بونانی بممنی زردك است و آنرا
زر نیز کویندله .
اصول فاخته - ام اسولی باشد از
هنده بحر اصول موسیقی وآنرا فاختةٌ ضرب هم
خوانند ونام صوتی هم هست .
اطا ه بفتم ازد و انی بالف کشیده ,
درخت یدم است که بس‌بی غرب خوانند و آنرا
زخمی بیای آن ترنند و نشکافند
==== LEAF 360
وشطهای سیله دارد . ۱ نوعی ازبوی مادران باتد . گویند کترانیدن‌آن
اطموط ‏ بنتم اول بر وزن مضوط , | درخانه گزندکان موذی را بکربزاند وآنرابعربی
بمعنی اطماط است که بندق حندی باشد  .‏ ۰ | قیصوم خوانند .
اطمسا ه بفتح ال و ثالت بتحتانی ابو ط ‏ پابای حطیء بروزن و معنی
رسیده وسین بی‌نقطه بالف کشیده . بلغت بودابی | اطموط است که بندق خندی باشد .
درهمزه باغین نقطه دار مشتمل برهیجده لغت
سعقص ساکن, باغت رومی وبسنی گویندیونانی؟
نوعی ازحرشفاس تکه بفارسی‌بید گیا و کزماز که
خوانند » وبعبی ثمرالطرفا گوبند .
اغره » بنم اول بروزن نقره ۰ رشی
باشد که در شکم و کردن مردم بهم میرسدوآترا
بعرمی تکفه میگوبند - وبفتح‌اول مجمح‌سلاطین
وحکام واشراف باشد - وبمعنی باد گیروجاب ی که
.باد سیار بود هم وت لته .:
اغریا ‏ بر وزن اصفیا » بلفت یونانی؟
کوه را گویند وحربی جیل‌خوانشد .
آغر یر ث؟ - بکس اول واك بتحتالی
رسیده ورای بی‌نقطه مفتوح بثای مثلهٌ زده » فام
برادر اقراسیاب‌بن پشنگه‌ین ورین آفرربدون‌است
که‌بجپت موافقت ابرانبان بردس
==== LEAF 361
فیاصر# روم ؛ او را ازآن جپت قصر گفتندکه
مادرش بوفت ولادت عمرد 7 شکمش را بشکافتند
و او را برآوردند و پزبان رومی اینچنین شخصی
را قیسرخوانند٩‏ . و گویند عیسی علیه‌السلام در
زمان او بوجود آمد . وبقوط سین اول بروزن
فربوی هم بنظر امده است -
اغشته با اول وئانی مفتوح و سکون
شین فرشت وفتح فوقانی ‏ بمعنیآمیخته وآلوده
وتر کرده باشد؟ .
لام ؛ جایی‌باشد که در کوه وسحرا بجهت‌خوابیدن
کومفندان ساژند؟ .
اغلیسون » با سن بی قطه بر وزن
افربدون ۰ قوس قرح را خوانند .
افتدستا
اغلیقی ‌ َنح اول,قلف سحتا سدكهه
بلفت بونانی؟ ترکیبی است کهآ نرا بغارسی پخته
جوشانیده‌اند ومیفختج همان است » وبکسر اول
نیز آعده شتگن «
اغول ه بر وزن ملول » از روی خشم
وفهر بگوث؛ چشم نگریستن باشد .
اغیرس < بنتح اولوثانی‌بتحتانی رسیده
و کسر رای قرشت و سکون سین سعفص ؛ جوز
رومی است و آن بار درختی باشد که صمغ آن
کهرباست ؛ و بعضی گویند چوب آن درخت
کهرباست .
اغیسی ‏ بروزن نفیس , نخمی اس ت که
آنرا بشیرازی تخم دلاشوب کونند » و ری
افتاد جنم اول بروزن
==== LEAF 362
اتمون
حمف خدایتمالی هم هست! -
/ لتیهاون » بعتح‌اول. دوابی‌است‌ممروف
وآن شَكوفةٌ نبانی باشد که بسعتر می‌ماند و سر
شاخپای آن بارمك است ۰ وطبع آن کرموخشاثه
کوفت صرع را نافع است ۰ و آنرا بعربی سبع
الثمرا خوانئد , وی کوبند زیر رومی است
وتیزطعم میباشد .
اقچ4 - بن اول بروزن بقچه , علامتی
است که در غله زار ها و کشت و زراعت بجهت
رمیدن مرغان ساژند . وبفتح اولعم گفته‌اند .
اقد فتح ارل و رای وسکون دال
ابچد » بممنی افتد است که شگفت
روا ماه تور گر ۳
وآن سورخ و:
و عجب
افدد » بر وزن صقذر ؛ برادر در را
وخواهرزاده تبزامده ات ۰
اقدستا » با تای قرخت بروزن‌مجلهاء
جمعتی افتدستاست که ستایش عجب و نبکو نرین
متایش - و حمد خدای عز وجل باشد بزبابن
پهلوی ۴‏
اقد‌یدن » بروزن فهمیدن . شگفتی
کردن وتعجب نمودن باشد ۴ .
اقر) - بر وزن صفرا ۰ بمعنی آفرین
ونحسین پاشه .
ار احت ‏ بر وزن پرداخت » یعنی
برداشت وبلند ساخت .
. رک : اد وافدستا‎ ٩
ب 30۸
اقفر اختن - بر وزن برداختن 4 بمعنی
برداشتن وبلشد ساختن باشد .
افر احته بر وزن بردا
```


## [2026-09-06T16:15:35.509Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i in range(363,368):\n    print('==== LEAF',i, ' first 300:')\n    print(t[i][:300].replace('\\n',' '))\n    for m in re.finditer('فسرد|فسرد|سرده',t[i]):\n        print('   HIT:',t[i][max(0,m.start()-200):m.start()+220].replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T16:15:37.653Z] TOOL RESULT

```
==== LEAF 363  first 300:
افر اشتن بروزن ومعنی‌برداشتن: بلند ساختن باشد . افر اشته بروزث ومعنی برداشته‌و بطند ماخته و بالارده )۱( باشد ۰ ۱ فر دون - بفتح اول رانی‌وسکون‌نالث و کربای ابجد وبای حطی بواو رسیده و بنون زده , دوایی اس تکه آنرا قرفیون کوبند . ا کر کزند کی جانوران را نانع است . که آنرا بشیرازی بالنگوی خوورو (۲گوبند .
==== LEAF 364  first 300:
آفری کشوث و نخم آنرا بذرالکشوث خوانند . فواق را تافع است . افری فتح اول وثانی بروزن سفری » مخفف آفرین است که دد مقام تصی نگوند . و بسکون انی هم درست است . افر یدون ‏ - فربدونباشد. واویادشاهی بوده. ءشهوره ویستی گویند افربدون نوح علیه ب اللام است ۰ و بعضی ذوالقرنین اعظم او را صسدانند ۰ اقفر پسموسش_ » 
==== LEAF 365  first 300:
ات وافرا یمرن الیل خوالند . اسر ۵لن؟ « بر وزن افشردن » بمعنی سردشدن ویخ بستن ومنجمد کردیدن باشد - واز چیزی ‏ وکسی‌دل سرد شدن هم هست - آقتاب عالمتاب است . افسرسگزی « بکس مین بی شله و سکون کاف فارسی و زای نقطه دار بتحتانی رسیده ۰ نام سازی باشد که نوازند - ونام تصنیفی وقولی است ازصنیفات بارید . افسر شد
==== LEAF 366  first 300:
بدان غلهٌ کوفته شده را برباد دهند تاکاه از آن 9 اقشه - بروزن کفچه, بمعنی باغورباشد وآن ظه‌ایست که درآسیا خرد کنند و بشکنند افغات» باین نقطه‌دار بروزن‌سنان , بممنی‌فرباد وزاری باشد- ونام فسلهاست مشهور چنانکه آرد نشود . افشین ۱ ‌‌ مروزن کم 0 نام شخصی بوده افی زد دفام - کنابه از قلمواسطی ومعروف وجمعش‌آ
==== LEAF 367  first 300:
افگنده(۱)سم کنابه ازعجز وزاری بسیارباشد . ومعرب افلاطون‌است . راو حکیمی بوده مشهور و معروف در زمان کف واستاد ارسطو است» وساز ارغنون مخترع اوست . افالا گبان- بک رکف . کنامه ازئوابت و سیارات است - وطایفه ای باششد از می دینان ویدمذهبان . افندبدن بت ور وزن ستدیدن ِ جنگ وخصوحت کردن باشد ب افیلون « بالام
```


## [2026-09-06T16:15:49.155Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nimport re\nt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor i,p in enumerate(t):\n    m=re.search(r'\\[pdf page (\\d+)\\]',p)\n    n=int(m.group(1)) if m else None\n    if n and 462<=n<=472:\n        print('=== pdf',n)\n        print(p[:700].replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T16:15:51.492Z] TOOL RESULT

```
leaves 721
=== pdf 462
[pdf page 462] -۱114- کلافه لام جایی ومقامی است.  کلاغ = بفتم اول. ممر‌واست وآنرا  کالاش ه بر وزن لواش : عشکبوت را | زاغ‌دشتی‌هممیگویند۷ ‎SaaS‏ - وصاحب ‎Waddle fa‏  ‎ay‏ کلاغ بالشم و بات کر باش د که آنرا کرد بر کرد قبور بزرکان میدارند وآن از ‎Ke‏ وچوب نیز یود . # ‎bd FEW‏ - کنابه از استهرا وتسخر و ربشخند کردن باشدکسیرا - ‎OWT‏ ۵ - بر وزن و ممنی کلابه باشد و آن ‎Glos‏ است خام که ازدوكبرچرخه  ‏کلاش خانه۲ = ‎get‏ ویافتضکبوت راکویند و ‎lige‏ ایکا کیا خوانند ۴ - ‎bie,‏ ‏عنکبوت را هم کفته‌اند که درآن تخم نهد وبچه برآرد . کلاشك ۴ = بفتح اول ورابع وسکون ‎GE‏ » بمعنی کلاسنگ است که فلاخن باشد. کالاشکن * - بنتح اول ‎ing GS,‏ ‎gals‏ نام یکی از حلواها باشد . کلاشکه ۱ ‎che‏ اول ‎ele‏ وکاف: قلاییرا گوبند ک
=== pdf 463
[pdf page 463] aw  ‎on - SY‏ اول بروزن علاك » دشت و صحرائیر| کوبند که مطلفاً درآن زرات ‎ot‏ ‏باشد ۱ و بلای پیثالیرا هم کفته‌اند که ‎ay‏ ‏سر باشد وآن از رستنگاه موی سراست ا میان س ۴ ؛ و باین ‎gine‏ بجای‌کاف لام هم‌آمده است - ویضم اول بععنی تهی وخالی باشد ۴ - وموج  ‏بز رکه را نیز کوبند ۴ - ‎Sy‏ اول‌چوب ‎She‏ ‏سر کجی باشد که کل ومیوه که دست ‎WT‏ رسد ‎Pate oly‏ .  ‎SU‏ موش - ‎eth‏ اول ۰ موش صحرائی و دشتی ‎atl‏ چه ‎cats SIT‏ وصحرارا کوش ‎٩‏ .  ‎pie = Ju‏ اول بروزن جمال » تاره  ‏سرا ست که مان فرق یی اد ۷ - ود ‎lel Sul ve‏ و خیره شدن چشم - و در  ‎—\we-  ‎ware‏ شراب‌فروش ‎ITU‏ و نم اول, کوزب کر ‎Seb,‏ را مبکویند نی ‎ES pot‏ ‎Ming JFL,‏ میسازد وبعربی فشا ر گوبند(۱)- و ‎gale Oly‏ حندوستان هم کوزه گر ر
=== pdf 464
[pdf page 464] AWA  ۲ ‏خوانند‎ Ul owe ‏اول‎ Gy - Va ‏بست وبند درهای باغ و طوبله و امثال آن‎ oT, . ‏باشد‎ ‎oye ‏دوضه - کنابه از‎ OW ‏است.‎ IT, ade ‏محمدی صلوات ال‎ oly ‏رسالت‎ ‏کلاو ۲ » پفتح اول و سکون آخر که‎ 5 ‏راگوبند‎ Jey ‏واو باشد », وزق‎  کلاور ۷ © بروزن تکاور ؛ بمعن یکلاو است که وزق باشد .  لوف = بروزن ترازو . توعی ازموش صحرالی ‎Ol‏  کلاوه » با واو » بروزن و معن یکلافه است که رسمان خام برچرخه پیچیده بائند ‎٩‏ ‏= و پمعتی ‎dele‏ وس کشته عم‌آمده است۷ - و غوك و وزق را نز گویند ۸ .  ‎Cr sr‏ ۷ پیشی_کمربند چرخ باشد که عربان منطقه خوانند - و کنابه از  ‏کلام بضم اول وسکون‌ها,معروفشت یعنی چیزی که ازپوست و پارچة زریفت وفیره دوزند و بر سر گذارند - و تاج پادشاهانرا لیز  ‎Cee) ‏مبدل «کلال»‎ - ٩ © ‏ب
=== pdf 465
[pdf page 465] و آن کلامی است که از ‎oT‏ زنگله و دم ‎aby‏ ‏بیاری آوبخته ‎ah‏ و متسین بر سورد کم فروش ‎ate‏ ودر بازاریگردانند .  کلاه شکستی = کنابه‌ازیر کردانیدن  ‎WLS‏ باشد ۱ - وکج گذاشتن هشن کلاء را لیز.  ‎- ‏بر اس‎ rg  ‎a ‏است‎  ‏کلاه نهادن - کنایه ازتواضع وعبز و ‎ath ys‏ - و کنابه از سجده کردن و می برزمین لهادن هم گفته‌اند .  ‎Py‏ ؟ » با ها بروزن ترازو,نوعی از آهوی بی شاخ باشد.  ‏کلاهود - بروزن بلادور ام ‎aide‏ ‏بوده مازندرالی ۳ .  ‏کلاهلوت ۴ - بر ‎oy‏ فلاطون . دم پهلوانی و بهادری بوده .  ‎a  ‏کلاه ملك - بخ میم ۰ کنابه‌از بادشاه  ‎«Jae ‏خم۱:‎ )0(  ‎Vw  ‏کلب ‎cae‏ اول و ثالی وسکون بای ایجد »کرد بر کرد دهان راکوبنب ۵ - و متقار ‎Lye‏ بیز کفته‌اند(۱) ۱ ؛ و ‎nh‏ معنی با بای فارسی هم آمده است -
=== pdf 466
[pdf page 466] —\wve—  هفت من ‎pS‏ داردکه بستحق بدهند ‎AN)‏  ‎oll‏ ۱ -بکر ثالث بر وزن  ‏نی ‎Se‏ ‏باه و آن ‎JT‏ است که کلبتان  ‏آهنگران وامتال ابشان راکه آهن ‎cis‏ را بدان ‎Alt Sa‏ هم میکوید :  ‏کلیتره ‎che‏ اول و بای فارسی ورای قرشت و سکون انی و فوفانی ۰ سخنان بیپوده وزبون و یمعنی راگویند ۴ - و ‎hy‏ رباییرا 55 میگفته‌اند ۱  ‏کلیس ۳ - با سین‌بی‌نقطه بروزنلبلبوه بمعتی چلیاسه است که وزغه باشد .  ‎Jaga = fos‏ و فتح الت‌وسکون ثانی وکاف + ‎oe‏ باشد که برروی خرمن سازند  ‏تا باران ضابع تکند - وخانة کوچکیرانیز کوبند.  ‏(۱) چش : - تواپ ... پدهند - (۳) خم۱: سر .  ‏)0( چك : و از کار باز آعده ‎tet‏ :  ‏که دشت ‎Hh‏ وفالیزبامان (۳) در فالیز وخرمن سازند ؛ و باین ممثی با کاف فارسی هم‌پنظ آمده است (4) وصاحب م
=== pdf 467
[pdf page 467] ~\wi- us ‏کلجان . بروزن مرجان » مزبله را‎ ‏کویند و آن (۱) جابی‌باشد که خاکروبه‌وپلیدیها‎ . ‏درآن ریزند‎ st ap ~  کلچنگ ۱۳- بن اول‌وفتح تانی‌وجيم فارسی وسکون نون وکاف فارسی » خرچنگه را کوبند وآنرا عربان سرطان خوانند.  کلجیجه - بفتح اول بروزن‌زدگیچه,  مشتف ۱۴ ‎ag CIS‏ است که ‎ine‏ غلفلیچه ‎Wat‏ وآن کف‌پای خاربدن وجنبانیدن‌انگشتان باشد در زیر بغل مردم تا بخنده افتند ؛ و یکی اول هم آمده است .  کح - ‎SG‏ اول و سکون ثانی وحای ۳ نفطه « نوعی از صمغ است که آنرا بارزد و بیرزد ‎٩۵‏ هر دوگوبند و عربان قنه خوانند.  شبیه است بمسطکی .  و دام و فیره ‎٩‏ - و هر چیز ناقص و کوتاه ۳" ‎Cory‏ و حقیر واندك و تافرتپ ودم بریده راهم کفته‌اند ۴ - و شخصیرا نیز کویند که زباش ‎colar‏ جاری نباشد و حرفها را 
=== pdf 468
[pdf page 468] و۱9۷ کلفت ‎OF‏ بنم اول و سکون ثانی و خای کلیس = یک اول با سین ی قطه . نقطه‌دار » نوعی از گیاه ورستنی باشد ۱۷ . بروزن و معنی‌کلز است ‎٩‏ که مفاث هندی‌باشد کلخچ ؟ = بنتح اول و انی و سکون - وبعربیآهگرا گوشد۷ - و بضماولینبقحلاجی ‎GE‏ نقطه دار و جیم فارسی ۰ چرکیر! گوبند | کرده باشد . که بر دست و پا و اندام نشیند و بعربی وسج ‎gin = Heald‏ اول وعین بی نقطه.لفظی خوانند . ۱ 0 ‎ell‏ که ‎sew‏ تاهموار و بانراشده وضم ‎ss‏ 5 م ست بجهت مردم لاهموار و اتراشیده دص ‎oe‏ بفتح اول و دال ابجد دسکدن | کرو, اند وامرد قوی هیکل را نیز کوشد - و مزدم هرزهکوی و پوج کوی را هم گفته‌اند. ‎AT‏ ۸ - با غین نقطه‌داربروزن‌زرکر, پشم بسیار ترم را گویند - ونوعی ازهیزم وهيمةً ‎OAT‏ بفتح اول و نانی و سکون فا  وفوفانی
=== pdf 469
[pdf page 469] io eS Sod Kee ‏و مشکی چند را پر بادکرده بر آن نصب کنند‎ - 9 ‏بگذرند‎ gue ‏شته از آبپای‎ oT ‏و بر‎ ‏و نام موضعی است از مضافات دامغان که درآ نجا‎ ‏میشود ۷ - و انجمن وعجمع‎ dele ‏.گندم خوب‎ ‏مردم را نیز گفته‌اند (۱) - و بمعنی درد سر هم‎ ۷ ‏آمده است - و تصفیر کل باشد که کچل است‎ ‏وشوم ونامبارك را نیز کویند ۸ ؛ وباین سبب‎ - ‏با ثانی‎ gow ‏کوف وبوم راکلك خوانند٩ ؛ و‎ ‏نارسیده*۱‎ pt ‏مک‌وریممنی بوم گفته‌اند - و‎ ‏وکاومیش‎  - ‏وغوز؛ پنبه که هنوزنش‌کفته باشد‎ - ‏و سم (۲) اول‎ -٩۱ ‏جوانرا هم میگوبند‎ Ly ۱۴ ‏وسکون ثانی؛ هم بممنی بغل وآغوش باشد‎ ‏پثم نرمی باشد که از بن موی‌بز‎ isn ‏-وهم‎  . ٩ ‏درشت و ناهموار را خوانند‎ gly  ‎ga ef aly”‏ اول و شالت وسکون ثانی وخای نقطه دار که رایع باشدونون
=== pdf 470
[pdf page 470] aus ۲ —\wy- ‏آن‌بافند‎ Jed IE ‏با ثانه برآورند ۱ و ازآن‎ ‏وتکیه و نمد وکلاه وکينك و ماتندآن ماللد‎ ‏و بکر اول و ثالی » انگشت کوچك وا گویند‎ ‏و یعربی خنص خوانند ۴ - و بمعنی لوچ وکاچ‎ ‏و بکر اولوسکون‎ - Feat wel oe ‏احول‎ ۳ ‏ثانی».هرلی میان‌خالیرا گوبندعموعاً ونی‌قلم کتایت‎ gle ‏کردنرا خموساً ۴ - وهرچهار دندان نیز‎ - 9 ‏بعربی ناب خوانند‎ LT, ‏را هم میگوبند‎ ‏و نام صمفی است درنهایت تلخی وآنرا ازدرخت‎ ٩ ‏جپودانه برمیآورند وعربان منزروت‌میگوند‎  - رضم اول ‎iy‏ بیعتی احول و کاج باشد ۷ - و درد شکم را یز گوبند ۸ .  کل کل . بفتح هر دو ‎GE‏ و سکون هر دولام » بمعنی هرژه گوبی کردن و کاوکاو نمودن باشد ‎٩‏ - ونام داروبی‌است که آنرا عربی مقل گویند ۴ ؛ وباین معنی‌بکسر ‎Ju!‏ وضم اول‌هر دوآمده 
=== pdf 471
[pdf page 471] کلکنك ۱ -رلو-  و میم » بمعنی منجئیق باشد ‎٩‏ - و بفتح اول . و دزم برسن دستار و کلاء زنند و آنرا ‎pr see‏  . ۵ ‏هم بایئممنی وهم بمعتی کافتن گفته اند- | میگویند‎ Sb,  ‎te‏ قوی وقرح ۴ نیز پنظرآمده است. | کلیم ۷ - ‎pth‏ اول وثانی کون کلکنلگ - بکر اول و فتح ‎Seb‏ از ‎Le‏ حویجی ‎wom So)‏ 8  ‏نون ‎ath‏ بروزن اشکلك , تخم خرفه را گویند آشها کنند ‎OTs‏ دونوع‌میباشد:  ‏و بعربی ‎a‏ خوانند ؛ وبروزن دلتنگهم | رومی وغیره» بهترین آن رومی  ‏بنظر آمده است است ‎oT,‏ بدستار عربان‌وعمامة کلکی یر پری باشد زهد فروشان ماند . که در بزم و رزم بر سر زنند و بترکی جیفه ‎GIST‏ ۲ بروزن ‎LS‏ ‏خوانند۳ . بلفت زندوپازند درخت ‎SGI‏ راکوبند ‏ کلم کلکینه - ‎oe‏ اول‌بروزن مرغینه؛مخمن کلماسنگ ۸ ه باسن بی‌نقطه بروزن 
=== pdf 472
[pdf page 472] {Awa  پرنمیباشد ۱  کلموژ ه بازای فارسی بروزن‌خر کوشء چلیاسه و وزغه را کویند ۴ (۱).  کلن - بت اول و فتح ثانی و سکون نون ‎IIMs‏ و کرهی ‎Toth‏ از کردن و اعنای مردم برمیآید؟ ؛ وباغره ‎)٩(‏ را نیز گوبند وآن علتی باشد (۳) که ببب زحمت ‎as‏ بهم رسد و چون زحمت اول بر طرف شود آنهم بر طرف کردد - و زحمتیرا نیز گویند که پایآدمی‌برابر ‎ob‏ میشود وعربان داءالفیل خوانند - و پنبفزده را تیز ‎SaaS‏ ازبرای رشتن کلوله کرده باشند - و در عریی نیز ‎AMT Le‏ کرده را کلن خوانند ۴ .  کلنبه = بنم اود و ثانی و سکون نون و فتح بای ایجد . کلیچه‌ای که درون آنرا از حلوا و مغز بادام پرساخته باشند ۵ - و بمعنی  (۱) خم۱: وزغه باشد .  آدمی شود وعربان داءالفیل خوانند و زحمتی را نیز گنته‌اند .  ‎in, ۲‏ کلمرغ بزیر همای
```


## [2026-09-06T16:16:07.763Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nimport re\nt=open('BQT_v3_pages_faseng.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor p in t:\n    m=re.search(r'\\[pdf page (\\d+)\\]',p)\n    if m and int(m.group(1)) in (464,466):\n        print('=== pdf',m.group(1))\n        # print lines with latin letters\n        for ln in p.split('\\n'):\n            if re.search(r'[A-Za-z]{3,}',ln) and 'pdf page' not in ln:\n                print('  ',ln.strip()[:200])\nEOF"
}
```


### [2026-09-06T16:16:09.760Z] TOOL RESULT

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'BQT_v3_pages_faseng.txt'
```


## [2026-09-06T16:16:11.951Z] TOOL CALL #88: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1671 --image 2>&1 | tail -30"
}
```


### [2026-09-06T16:16:19.333Z] TOOL RESULT

```
است که وزق باشد . :
سود دادن باشد .
1 ود > بروزن ترازو » نوعی آزموش کلاه چرخ - بکر ها بطریق‌اضافه.
3 ۱ | بمعنی آسان باشد پعنی کلاه ی که‌آن چرخ است
8 » با واو » بروزن و معنی کلافه - وآفتایرا نیز گوبند .
است که رسمان خا خه محده باشند ‎٩‏ رن
8 ۱ ْ کی 7 1 کلاه دادی - بممنی‌پادشاهی‌وساطنت
- و بمعنی سراسیمه وس هم‌آمده است کلاه دا
- و غوك و وزق را نیز کوبند ۸ . باشد ۱۳چه مر پادشاء را کویند.
کلاوة چرخ ‎٩‏ - بسن کمربند کلاه مین - بنتح زای نقطه دار
چرخ باشد که عربان منطقه خوانند - و کنابه از | کنابه ازآسمان است - وکنایه ازآفاب سوماه
کرش چرخ هم هست. هم هست - و رستنیی را نیز میگوبند که از
کلاه*۱- نم اول وسکون‌ها.معروفت | زمینهای 2 و دیوارهای حمام برمياید وآترا
بعنی چیزی که ازپوست و پارچهٌ زریفت وغیره سماروغ خو ی ۹
دوزند و بر سر گذارند - و تاج پادشاهانر| نیز کلاه ر له ۴ بخته کلامرا گوبند
۱- مبدل «کلال» (هم.) . ۲ - قزوبنی 601878 ۸« دییرسیاقی > » تهرانی
5000 » بروجردی [ ۱۱۹۵۱۱۱۱۱ 2 شهیدی ی ۳ < کلااو (.م.) ۶ کلاوه (.م.).
۴ -_ظ. مصحف«کللااو» < کلاو . ‎٩9‏ _قس: کلادموش. ‎٩‏ * کلابه * کلافه(هم.) .
۷ - در زبا ن کنونی کوبند : کلافه شدم (کیج وس رگشته شدم ) .
۸ -قس :کلاو ؛کلااو . ‎٩‏ -رك : کلاوه ( معنی اول ) ۰
۶ وجه اختفاقی آن درست معلوم یت . قس : کردی ۱13۲۷ظ ۰ پهلوی وان اه
« هوبشمان ‎۸٩۳‏ > و رك : اسشق ‎۸٩۳‏ » ورك : ژابا ص ۳۳۹ . اورامانی 8312۷ * 4. اورامان
۳ گیلکی ۴۷128 ۰ فریزدی 1312 ۰ برنی 8012 » نطنزی 8018 4 .۲۹۱۱ ۰4
سمنانی ۱2 سنگری اد . لامگردی و شپمبرزادی 1 « ۲.4 ص ۰*۱۹ طبری
42 * واژه‌نامه ۵۸۹ > ۹ اکنون گوبند: کلاهش را بهوا ( بآسمان ) انداخت .
۴ نه هر که طرف کله کج‌نهاد وتند اشت کلاه داری و آبین سروری داند .
« حافظ شیرازی مصحح قروینی*2۱۷ - ۴۳ کلاه زنگوله « فرهنکه نظام » :
مباد محتسب طبع بهر رسوایی کلاه زنگلهٌ هجو بر نهد برت »
حکم شرف‌الدین شفائی « بهار عجم >.
```


## [2026-09-06T16:16:25.454Z] TOOL CALL #89: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1673 --image 2>&1 | tail -35"
}
```


### [2026-09-06T16:16:32.631Z] TOOL RESULT

```
هت هن کندم دار د که بستحق بدهند ‎.)٩(‏ که دشت بانان وفالیز بانان (۳) در قالیز وخرمن
کلبتان ۱ - بکسر ثنالت بر وزن | سازند ؛ و باین معنی با کاف قارسی هم‌بنظرآمده
زرفعان (۲) ۰ است (4) وصاحب موْبدالفتلاء میگوید چیزست
بسنی کلیتن ‏ نس 6 | که بدان خرمن اسازند الط اعطم .
باشد و آن کلبه * - بنم اول وافتح ثالك , خانه
آلتی اس ت که کبتان كوچك تنگه و تاريك را کوبند - و حجره -
آهنگران وامثال آیشان را که آهن فته را بدان و دکانرا نیز گفته‌اند - و بمعن ی کنج وکوشههم
برگیرند وآترا انبر هم میگوبند . بنظرآمده است .
کلپتره - بفتح اول و بای فارسی ورای کلتان ‎٩‏ - با تای فرشت پروزن‌دربان,
قرشت و سکون ثانی و فوقانی » سخنان بیپوده | از جملهٌ چپارچوب درآن دوچوب را گوبند که
وزبون و بیمعنی راکویند ۴ - و بويك ربابیرا | در پهلوهای در خانه باشد .
نیزمیگفته‌اند . کلتبان ۷ بروزن ومعنی غلتباناست
کلیسق * - با سین‌بی‌نقطه بروزن‌لبلبوه | که مردم بی حمیت و دیوث باشد و معرب آن
بمعنی چلیاسه است که وزغه باشد . فلطبان وقرطبان است ۸ .
کاب * - بنم‌اول و فتح ثالث‌دسکون کلقه - بفتح اول و ثالث و سکون ثانی,
انی وکاف » نالاری باشد که برروی خرمن سازند | حیوان پیر سال خورده و ازکار بلزمانده (0) واز
تا باران ضایع نکند - وخانه کوچکیرانیز کویند ۲ کار افتاده راکوبند از هرقم که باشد اعم ازدد
(۱) چش : - ثواب ... پدهند . (۲) خم۱: زرشان .
(۳) خم۱: سر . (4) چش :- است .
(ه) چك : و از کار بلز آمده ؛چش : - از کار باز مانده .
۱ - (ع) «کلبتان بالفتحء آنبور آهنگران > « متتهی‌الارب > -
۴ - او تراک ی گفت‌کاین کلپتره ها را جمم ان
تا ترا لازم شود چندین شکایت کستری .
انوری آییوردی «رشیدی» «فرهنگه نظام».
۴ - رك : کلباسو :
همچو عقرب که کلیو بیند قبل از ایذ! همی رود از خود .
آذری طوسی ۶ رشیدی» « فرهنکه‌نظام .
۴ كليك « بهار عجم > قی :کلبه .
ه <* کربه . از پهلوی 80۲۳02 8 > ارمنی ۲۲۳2 ( کارخانه » دکان » میشانه)
« هوبشمان ۸۹۶ ۰ ععرب آن کربق ۰ قربق ( 0.73 , ۳۲۵۳۵۷۷0۳۸6۳ ,814410 ) ونیز
کریج » کلبة « اسشق ۸۹۶ > قس :كليك . در عربی «كلية بالضم , دکان‌می‌فروش*«منتهی الارب».
‎٩‏ -ظ . مسحف «کلان » (هم.) . ۷ - رك : قرتبان , قلتبان .
۸ - خود کلتبان هم در عربي آمده : « کلتبان بالفتح وقتح الفوفية قبل‌الباه » دیوث و
زن جلب » ۶ منتهي‌الارب ‏ ۰«
```


## [2026-09-06T16:16:44.256Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG sard ===\"; grep -n -A12 \"^\\*sard\\|\\*sard  \\|sard-\" CHEUNG.txt | head -40"
}
```


### [2026-09-06T16:16:44.302Z] TOOL RESULT

```
=== CHEUNG sard ===
22020:*sard ‘to smear, rub’ 
22021-
22022-*PARTHIAN: (+ *aua-) ? wsrd ‘poured ?, Ausgeburt ?’ (Andreas — Henning 1934: 880 
22023-f.) = DMMPP: 347 
22024-
22025-*KHOTANESE: (+ *4-) e-saly- ‘to besmear’ || (+ *aua-) ? avasalaka- ‘mark by 
22026-smearing’ (LW ?) || (+ *pati-) *pasal-, LKh. pisal- ‘to besmear [tr.] = SGS: 12, 78 
22027-*NWIR: Kurd. sirin, Awrom. asariáy/-sar- ‘to wipe’ 
22028-
22029-*NEIR: (+ *ui-) Oss. I. saerdyn/szerst, D. iszerdun/isarst ‘to smear, grease’ 
22030-
22031-*SANSKRIT: (?) chard ‘to pour out, spit out, vomit" (VS, TA+), also sardh’ ‘to fart, 
22032-blow to’ (AVP) = EWAia I: 557; II: 620 
--
57659:*sard, *sauH!, Sort" 
57660-*Hais, *Hraz (s.v.), *xsaH 
57661-*dau', *dram, *drau’, *duar, 
57662-*gaHz, *paud, *saij, *tac’, 
57663-*yaiH 
57664-
57665-*xsaub 
57666-
57667-*band (s.v.) 
57668-
57669-*iaz, *uai 
57670-
57671-*spaH
```


## [2026-09-06T16:16:47.711Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"afsurdan\\|afsardan\\|to be cold\\|to become cold\\|to freeze\" CHEUNG.txt | head -20"
}
```


### [2026-09-06T16:16:47.760Z] TOOL RESULT

```
2542:*NWIR: ? NP bastah ‘curdled’ (< *‘bound’ ?), Bal. bast, badit/bad- ‘to freeze (of 
3684:*ЧаН?/&Н ‘to freeze" 
3686:*CHORESMIAN: т/су- ‘to freeze’ = Samadi: 55 
3688:*NWIR: NP ca(hjidan/cay-, Zaz. čī- ‘to become cold’, Sang. ёеу- ‘to freeze’, Maz. ca 
3691:*NEIR: Yghn. si-, Yi. Ciy-/Cuy- (Zarubin) ‘to freeze’ || (+ *us- ?) Sh. (Baj.) Xici(y)-/ 
3693:Xicud, Yzgh. Siy-/Sed ‘to freeze’ || (+ *pati-) Yi. pcio 'frostbitten' 
6991:Inf.: BMP ’ps’Itn /afsardan/ 
7752:«PIE ? *gel- ‘to freeze’ = LIV: 185 | Pok.: 365 f. 
7754:ЈЕ COGNATES: ON kala ‘to become cold, freeze’, Lat. gelü ’freezing’, (denomin.) 
7755:Lat. gelare ‘to freeze’, OE cealer, calwer (m.) ‘fatty milk’, NHG (Alem.) challen ‘to 
15191:~ *zaiH ‘to perish; to destroy’ and *&iaH’/&iH ~ *saiH/siH ‘to freeze’, but both cases 
21578:*saiH/siH ‘to freeze’ 
21580:*NEIR: Oss. I. syjyn/syd, D. sujun/sud ‘to freeze’, ? Yghn. si- (rather *Чан? N), 
21581:Yzgh. Sed/Siy- ‘to freeze’, Sh. Sito, Sariq. S(1)tu ‘cold, ice’. Ф The initial š- of Yzgh. 
21585:*SANSKRIT: sya ‘to freeze, coagulate, become rigid’ (Käth+), sitä- (ppp.) ‘cold’ 
22051:pres. IND. 3sg. BMP /afsarénéd/; Inf.: BMP "psitn /afsardan/ 
22069:*CHORESMIAN: srY- ‘to become cold, freeze’, s’ry- (caus.) || (+ *apa-) ps’ry- ‘to cool 
22072:*NWIR: NP sard, Bal. sart, Kurd. sar ‘cold’ || (+ *apa-) NP afsurdan/afsär- ‘to 
22075:*NEIR: Oss. I. salyn/sald, D. s&lun/sald ‘to freeze’, Pash. sor, sara, Sariq. sort 
22082:«PIE *KelH- ‘to freeze’. © The accent in the Baltic forms indicates the presence of a
```


## [2026-09-06T16:16:50.662Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '22040,22095p' CHEUNG.txt"
}
```


### [2026-09-06T16:16:50.711Z] TOOL RESULT

```
*sarH! ‘to cool, become cold' 

*AVESTAN: Y Av. sarota- ‘cold’ (V 1.3) 

*MIDDLE PERSIAN: MMP srd'g ‘cold(ness)’, BMP sit /sard/ ‘cold’ || (+ *apa-) BMP 
"psl- /afsar-/ ‘to cool down’, BMP pel /afsar-/ (caus.), BMP /afsarén-/ (sec. caus.) 
‘to cool off, extinguish (fire)’, MMP ’ps’rysn ‘cooling? = DMMPP: 308b f., 50b 

(+ *apa-) Pres.: IND. 3р1. BMP ’pslynd /afsarend/; Partic.: perf. pass. BMP pelt caus. BMP pelt Caus.: 
pres. IND. 3sg. BMP /afsarénéd/; Inf.: BMP "psitn /afsardan/ 


*PARTHIAN: srd ‘cold’ || (+ *ui-) wys’r- ‘to cool off (Sundermann 1997: 76, 169) 


= Ghilain: 74 | DMMPP: 308b, 356b 
Pres.: IND. 3sg. wys’ryd 


*sarH2 337 


*KHOTANESE: säda- ‘cold’ 

*SOGDIAN: BSogd. srt, srty ‘cold’ || (+ *apa-) MSogd. “psyr’mndyy ‘cooling, 
freezing’ || (+ *ham-) BSogd. ’ns’rty ‘cold, cooled’ 

*CHORESMIAN: srY- ‘to become cold, freeze’, s’ry- (caus.) || (+ *apa-) ps’ry- ‘to cool 
off [tr.” © Samadi: 186, 178, 161 

*NWIR: NP sard, Bal. sart, Kurd. sar ‘cold’ || (+ *apa-) NP afsurdan/afsär- ‘to 
congeal’ 

*NEIR: Oss. I. salyn/sald, D. s&lun/sald ‘to freeze’, Pash. sor, sara, Sariq. sort 
‘frozen, stiff from cold’, Wa. ѕыг ‘cold’ || (+ *a- ?) Yghn. ósir-/ósér-/ósirta ‘to 
freeze, chill’ || (+ *pati-) Sang, pacor-, paci-/pacug, pacüg ‘to cool, become cold’ || 
(+ *ui-) ? Oss. I. ser(d)yn/serst, D. iserdun/isard (isarst) ‘to harden, steel; to weld’, 
Yghn. oser- ‘to cool’, Wa. wasar-/wasart- ‘to fade, wither [of apricot blossoms]’ 
*SANSKRIT: ? sisira- (m.) ‘the cool season’ (AV+) > EWAia II: 641 

«PIE *KelH- ‘to freeze’. © The accent in the Baltic forms indicates the presence of a 
laryngeal. = LIV: 323 | Pok.: 551f. 


*IE COGNATES: Lith. šálti ‘to freeze, cool (off), become cool’, Latv. salt ‘to freeze’ 
*REFERENCES: EVP: 70; IFL П: 540b, 549b; Andreev — PeSéereva: 299b Ё; Fraenkel II: 960b Ё; EVS: 
75b, 52b; Abaev, Slovar’ III: 64; DKS: 424a; Steblin-Kamenskij 1999: 325, 399; NEVP: 76; Korn 2005: 
189, 381 (passim) 


*sarH? “to mix, unite with’ 

*AVESTAN: OAv. sar- ‘to mix, unite with’ — Liste: 61
```


## [2026-09-06T16:16:57.518Z] TOOL CALL #93: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f in ['LEW_1910.txt','LAT.txt']:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    print('====',f)\n    for m in list(re.finditer(r'caleo|caleō',t))[:2]:\n        print(t[max(0,m.start()-150):m.start()+700].replace('\\n',' '))\n        print('---')\nEOF"
}
```


### [2026-09-06T16:16:59.271Z] TOOL RESULT

```
==== LEW_1910.txt
==== LAT.txt
x, et noame d'aprbs sa couleur? La finale rappelle 'arista/aresta. calceus: v. calx. calculus, -i, calculo, - 5 re: v. calx. calendae: v. colo,-os 1. caleo, - 5 s, -ul, -Iturus, -ere: etre cbaud (sene physique et moral), etre 4 chauff 4 ; etre ardent, etc. Ancien, usuel. M.L.1510. Inchoatif: calesco, -is, M.L.1511 (d'ou concalesco marquant l' 4 chauffement soudain (aspect d^termine) M.L.3110, incalescd, M.L. 4339 , avec le pr 4 fixe marquant le passage d'un 4 tat a un autre; excalesco 9948). Compos 4 transitif: cal(e)facio,-is,-ere et ses derivas; M.L.1507; *excale- faciS, 3947; calefacto, -os (Pl.). Formes nominales et d 4 riv 4 s: calor, -oris m.: chaleur (sens physique et moral). Le neutre qu'on lit dans Plaute, Mer. 870, nec calor nec frigas metuo, semble a*en 4 par le voisinage de frigus. M.L.1536. calidus ( caldus avec absorption de
---
pacum., frigida Tempe (Vg.); au sens noral "froideur". Le double sens, phjrsique et aoral, se retrouve dans frlgeB, frigidus qui souvent s'opposent A caleo, calidus, cf. ad Herenn., 4,x5,3x, in re frigidissima cales, in feruentissima friges, Cf. pour le sens 1 |/UX 0 S, yvyjpoi. - Anci en, usnel. D^riv^s et conpos^s: frigeB,-es,-xl (-ul) (les graanairiens enseignent que le pft. est frixi, qu'on lit dans Ldv; Andr., Od.17, ...Ulixi frixit prae pauore/cor; frigui est rdcent. Dans la plupart des cas, il est iapossible de decider si l'on a affaire au pft. de frigeo ou de fri¬ gesco)'. etre froid. M.1.3509; frlgescB,-is et ses coapos 4 s dB-, in-, inter-, per-, refrigesco M.l.^isya, dont le parfait est perfrixi, refrixi', frigero,-dp: rare (Catul., Cael. Anr.), aais le coaposd refrigero est frequent et classique; le subst. refrigerium, dans le
---
```


## [2026-09-06T16:17:16.480Z] TOOL CALL #94: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('PHD.txt',encoding='utf-8',errors='replace').read()\nfor w in ['gōsāl','gosāl','sālag','sāl ','ābsāl','afsālān']:\n    print('===',w)\n    for m in list(re.finditer(re.escape(w),t))[:3]:\n        print('  ',t[max(0,m.start()-160):m.start()+160].replace('\\n',' '))\nEOF"
}
```


## [2026-09-06T16:17:18.163Z] TOOL CALL #95: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nfor w in ['Hall,','Hell,','Hole,','Hollow','Helmet','Colour','Conceal','Cell,']:\n    print('===',w)\n    for m in list(re.finditer(re.escape(w),t))[:1]:\n        print('  ',t[m.start():m.start()+330].replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T16:17:18.234Z] TOOL RESULT

```
=== gōsāl
=== gosāl
=== sālag
   ion grāmīgīh. afraid, be ~ tarsidan. after fraz az, pas az, pay i. afterwards pas. again abaz, did, P bid. against padirag. karm, hambāy, (spiritual) age dad, -sālagīh; old -- pīrīh, zarman(ih), zarwan. aged pir. ageless azarman. aggression hénih. aggressive mustabarmand. agile čābuk. agility čābukīh. agitate ayārdēnīd
    haftād* darr-t PAHLAVI KEY — AA Sri 33 süxtarih saxtih saxt saxtan, saxtan süg, sak say- sahigih sahig, sivag sas зап saxwan sahóg sak sárcn- sārēnīdan sālwār sālagīh sālag sahm sāmānūmand sūmān sahmgēn Y $6) PAHLAVI KEY [140] mastog 19112256 mehtar Vess mastarg > e26 mizagūmand 2061” 406 mizagdārīh AAS 3G mizag 1.5 
    darr-t PAHLAVI KEY — AA Sri 33 süxtarih saxtih saxt saxtan, saxtan süg, sak say- sahigih sahig, sivag sas зап saxwan sahóg sak sárcn- sārēnīdan sālwār sālagīh sālag sahm sāmānūmand sūmān sahmgēn Y $6) PAHLAVI KEY [140] mastog 19112256 mehtar Vess mastarg > e26 mizagūmand 2061” 406 mizagdārīh AAS 3G mizag 1.5 0G rūynī
=== sāl 
=== ābsāl
   praise, blessing. 9544. "tien ~agan [-k”n!] Afrinagan prayers. аїгӧёар [ēlwšk! | N ~ a] a sweetmeat made of flour, butter, and honey. ‚ *afsálàn Pfs'Px!' | (N ābsālān)] springtime. afsān (?psn! | (M ?р?ле), N afsāna] story, fable. afsardan, afsar- ['psi-tn'] cool down. afsārdan, afsar- Pfs?/-tn'] cool, freeze, extingu
=== afsālān
   l wimuštan, wināhīdan. spoilt ānāst(ag), mūdag, tabāh, winastag. spoon kafčag. spotted parš. spread atšāndan, wistardan. spring, v. source. spring(time) wahār, afsālān, mēdyē- zarm; (a.) wahārīg. sprinkle paššinjīdan. sprinkling paššinjišn. sprout spīg. stable āxwarr, stērgāh. stagger škarwīdan. stagnant hammist. stain
```


### [2026-09-06T16:17:20.430Z] TOOL RESULT

```
=== Hall,
=== Hell,
=== Hole,
=== Hollow
   Hollow ;  &ee  Hole. Holly.  ^E.)  M  £.  hoHn ;  ao  that  an  n has  been  dropped.  A.  S.  koUn^  koUgn, holly.  +  W  celyn.  Com.  ctlin.  Bret.  keUn^ Gael.  €uilionH,  \n^  cmliann,  holly.  CC also  Dtt.  huUt,  G.  huhc,  holly,  0.  H.  G. AmVii  (whence  F.  hou-r). holm-oak,  the  evergreen  oak.  (E.) Here  holm  i
=== Helmet
=== Colour
=== Conceal
   Conceal ;  sec  Cell. Concede;  sec  Cede. Conceit;  see  Capaoiot Conceive^   Conoeptloti? oioua. Conoentro ;  tee  Oeatrs^ CONCERN. nix:  in  Ute  Lat^  to  belong >-  (AMV),  Wttb  ;    Uld   £^' dccrre,  observe.  4*  ^jl^- e,  decide;  Skt  kxi,  to K.) .-L.)  M.  E.<fa-fw.-O.F. 'ntf».«i.*L.  dunitis,  pp.  of decTc*,  lit.
=== Cell,
```


## [2026-09-06T16:17:27.270Z] TOOL CALL #96: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN gusale ===\"; grep -n -B2 -A8 \"gusale\\|güsäle\\|gusäle\\|gôsâle\" HRN.txt | head -30; echo \"=== NYB sal ===\"; grep -n \"^sal \\[\\|sal \\[sl\\|s'l\\]\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-06T16:17:27.340Z] TOOL RESULT

```
=== HRN gusale ===
=== NYB sal ===
```


## [2026-09-06T16:17:30.427Z] TOOL CALL #97: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"sale.*Kalb\\|Kalb'\" HRN.txt | head -10; echo \"=== NYB ===\"; grep -n -i \"'Jahr'\\|year\" NYB_vol2_glossary.txt | grep -i \"sal\" | head -10"
}
```


### [2026-09-06T16:17:30.492Z] TOOL RESULT

```
2017:kurd. vacdhä *Familie' (H.-Sch.); oss. d. mss 'Kalb'
2018:(79); bei. gvask *Kalb' (142); wa/. vmk^ sar. visk *Kalb'.
7717:888. f/äv llind', gö, gög 'Kalb' {^gavaka-)'''), göban 'Hirte'.
8171:941. gösäle 'Kalb'.
10229:Für die Bedeutung 'dreijähriges Kalb' werden im
=== NYB ===
420:an-aibigatīk ['nybgtyk] adj. belonging to the period of non-atbigat (q. v.), i.e. the period when the Evil Power had not yet invaded the creation of Ohurmazd: ~ sar the end of this period (v. sar) 38%; ~ 330 sal 330 years before the Onslaught took place 3926, — Cf azbigat, aibigatik.
439:and [’nd] so much, so many: én ~ this much 64°; all this, all these 351. 623. 6572.24; hac én ~ sal apāc since so many years 1674; han ~ dušman all these ene- mies (sg. as with numerals) 249; 10426, 11923; — ~ cand as much (big, large, high, etc.) as: 3119-15, 935. (935 without ~); ~ cand yašt-ē (as much as =) at least some ceremonies 659; — hän <... cand as much (many, long, ete.) as 92°. 997. 10027, 10324-25; 2 ~ dranäi pahnāi cand han i nn hast twice the length (and) breadth of it as it is now 10024-25; 7000 han ~ cand
476:apäc [L'WEIL ; ’p’c] 1. adv. back, back- ward (opp. frāc 25?-*), again: hac 7-salak ~ for seven years 16?5; hac én and (q.v.) sal ~ 1674; — prev. with vbs. of motion, e. g. dmatan, šutan, vastan, ete., and many others, e.g. guftan, gumeatan, etc. — 2. prep. with (= apäk) 42%. — 1. < *apācā instr. adv. from Olr adj. *apdnk-, weak st. apük- and apác, derived from Av. (72) apa, OP apa, cf Skr apdfic- ‘situated be- hind’; MPrth °b’c; Paz. awāž; NP baz. — 2. < *upācā, instr. adv. from Olr adj. *wpünk- derived from Av. (388 sq.) upa, OP upä ‘under, with’; J-Prs ?b?z ‘with’ (common); v. further apäk.
507:(cf 41?" and 89%); ~ fravartak in the letter 1822; — combined with another prep.: ~ 6 pad estat 28%. 1189. 11917 (cf above 1871); ~ 6 ax“ i astomand 401; m andar äyiyänak 409; ~ tdi sdxdn 401; ~ pat óstak 48% (ete.). — b) temporal: ~ sal 2 mazdesn bag’ Šāhpuhr” in the year 2 of the Mazdayasnian Divine Sh. Pl:l; ~ sal "68 in the year 68 P2:1; ~ pat han jamān ka at the time when 41%, adak ~ pat jamän at that time 619; 4214; 3 sap td three nights ago 512-3, — c) figurative: on, about (esp. in headings and book titles), concerning; (reigning) over, (merciful) to, (hostile) to- wards; (means) for; ete.; — with an inf. or a v.n.: in order to 3714-15, 4515; 1185 (continued by inf. + rād, l. 6). - ~ does not govern encl. pronouns; single excep- tion apar-aš 54° (late passage). — Av. (394 sq.) upati, OP upariy; MPrthPrs br; Paz. awar; NP bar. Cf aper. — On MDM 43" v. hàreftan.
554:apäyistan ['p'dstn'], apāyītan [’p’dytn'] apäy-, 3d p. sg. apāyēt [’p’dt', ^p'dyt'], 3d p. pl. apäyend ['p'dynd], pret. 3d p. sg. apāyist 1. to please a p. (pat) 83%; cigon mēnēyān apäyist as it had pleased (was predestinated by) the heavenly gods 405, v. below. — 2. impers. it is desirable: -m apāyēt 6 han ciš I desire, try to obtain, this 562%, — 3. to be needed 1211-2 also pat. kär. apāyet 14%. 375, andar apāyēnd 105%. — 4. to be proper, seemly 4015 (bē ~). — 5. impers. apäyet auxiliary vb.: must, ought to, shall, should, has to, is bound to, ete. with the p. as indir. obj. (virtual dat.), a) governing an inf., which is as a rule placed after: u api-t xvatāyēh i Ērān šahr vas sal apäyet kartan and thou shalt exercise dominion over Iran for many years 629-31; 918-19, ]014 ete.; in this case preverbs to the inf. are drawn to apäyet; bé — pursitan 1319; ba ~ hištan 1313; kār-ē i apar nē ~ kartan 104%; apārīk 6 [KN] ~ xtartan 94??; less often the inf. is placed before: ēzatan nē ~ 1017-19; pit u mat frazand i xueš rād En and kär u kirpak ... bē üámóxtan ~ the parents shall teach 6522-23; 6519-20; 9113; the inf. sometimes has to be supplied: -
763:ütur ['twr'; inser. ’twry] fire, referring to the old Iranian fire cult: ~ yazét god Ātur 25?; ~ farröbäg, gušnasp u burzen mihr the names of the three sacred fires connected with the three classes of the old Iranian society 118, explained 27-9; ~ farröbäg, i -bag 974. 9511; ~ gusnasp 955; ~burzén mihr 95%; ~-dn šāh the head of the sacred fires 1222-23, 131; — sal 58, āturv i Artaxšahr säl 40, āturv Šahpuhr i āturān šāh sal 24 SPrs:1-3 = sar 58, ātarē Artaxéahr sar 40, ātarē Šāhēpuhr ātarūn xšāh sār 24 SPrth:1-3: ‘... of the year 58 (viz.) the year 40 (of =) after the (enthronement) fire of Artax- Sahr, the year 24 (of =) after the (en- thronement) fire of Sahpuhr, the head of the fires’, which means the year 266 A.D., v. Christensen apud Ghirshman, Rev. des arts asiatiques X, 1936, 127—128 (the year 40 reckoned from the coronation of A. in the year 226, the year 24 reckoned from the coronation of S. in the year 242, and the year 58 reckoned from what must have been the epochal year of Sassanid time-reckoning, viz. 208 A. D.). — [~ the name of the 9th day of the month, also of the 9th month of the year; dade (q.v.) pat — the name of the 8th day of the month: FrP 28.] — Av. v.s. v. ätaxs; Prth ätarö (g. v.); MPrthPrs ’dwr; Paz. ädur; NP āčar, ādar. As to the three sacred fires v. Christensen, Sass. 164— 167; cf also de Menasee, Feux (1964); Mary Boyce, BSOAS XXXI, 1968, 52- 68, 270-289.
1426:3.8 [the figure l; -’y, -y, -yh] the enel. indef. art.: tigr-é [-1] 339; duxt-ē [BRTH- ^y] 14%; gad-ē [gt'-”y] one stroke with the mace 312°, 4 ēvak-ē [HD-wk!-y] one fourth 998; vāt-ē [-1] 4 hubod 73°; hec ctš-ē [-l] nö 16%; har kas-ē PYS-1] 10018; and cand yašt-ē [-1] 651°; pat har 40 sal hac zan-ē u mart-é frazand-é [al -ē's spelt -1] zāyēt every forthieth year a child is born of a woman and a man (= of one couple) 8622-23; 6 artestäreh for 6 artēštār-ē 4517. — Identical with ?e; MPrs ‘yw placed after its subst.; Paz. -é, NP -é. — The spelling [-1] is sometimes erroneously used for other suffixes -é: mēd4-1 = mode cas. obl. 72??; har marg- arzanik+-1 = -aržānīkē for the abstr. -arzanikéh 10199.
1927:har [KR^; hl 27/9] every, each, all; to- gether with the indef. art. each: ~ gām-ē at each step 3217; 87?5. 949; ~ &vak each one 1045-6, 11318; ~ 2 both, passim; ~ kas, ~ kasē everyone, ~ ciš everything; ~ ke, — ce, v. these ws.; pat ~ 40 sal each fortieth year 86??; in neg. sentence: any 619. 1001%; whatever 821%. — = Paz. NP; MPrthPrs hrw — harv; Av. (1790) haurva-, OP haruva. V. also harvén, har- visp, harvist, harvistén.
3381:sal, Prth sar [ŠNT] year; in dating: apar ~ 2 mazdésn bag" Šāhpuh<r)Y in the year 2
3384:of His Mazdayasnian Majesty Sh. P I: 1; apar — 68 [this seems to be the correct reading] inthe year 68 [of the reign of King Shapur II] P2:1; ~ 58, àtur* + Artaxšer ~ 40 etec., v.s. v. tur; — ~ pat ~ year by year 191; pat har 40 m every 40th year 86**; pat 3 ~, pat 6 ~, pat 9 — in three, six, nine years 9319-21; 10621-22; pat 3000 ~ 4 menos āstišnēh within the 3000 years of heavenly exis- tence 3820-21; 393; ka 30000 ~ gētē āstišnēh (but), anaibigatik 330 ~ apäc but when it was the 3000 years’ (period) of material existence, and 330 years of the unassailed period still remained 3926-27; — hac én and — apäc so many years ago 1674. — Av. (1566) sarad-, OP Gard-; MPrthPrs sr; Paz. NP sal.
```


## [2026-09-06T16:17:37.401Z] TOOL CALL #98: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8171,8186p' HRN.txt; echo \"--- which leaf?\"; python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\ni=t.find(\"941. gösäle\")\nprint('leafindex',t[:i].count('\\f'))\nEOF"
}
```


### [2026-09-06T16:17:39.675Z] TOOL RESULT

```
941. gösäle 'Kalb'.
ai. vatsd' 'Kalb, Jährling*.
käfir. vatsala, si^n. botsöri 'Jährling' (Tomaschek,
S. 765).
Das ö in gösäle stammt von go 'Kuh' (No. 888).
942. göspendj gösfend 'Kleinvieh, Schaaf, Widder, Ziege'.
aw. gaospenta- (vd. 21, 1); phlv. göspaud.
943. gas 'Ohr*.
ap. gausa- 'Ohr'; aw. gaosa- 'Ohr*; phlv. gös; ai.
ghoSa- 'Lärm, Getön .
kurd. güh; afy. yvay; oss. d. yos, t. qüs (94); bei.
gös (125); wa/. yws, yis etc.
np. gösvär^ ^öst^äre 'Ohrgehänge*: aw. frä.[gaosävara-,
mat,[gaosävare; phlv. gösvär,
944. gast 'Fleisch*.
aw. gäv, Nom. gän§ 'Fleisch' ; phlv. göst^ göstm (GFr.).
--- which leaf?
leafindex 231
```


## [2026-09-06T16:17:47.679Z] TOOL CALL #99: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && python3 - <<'EOF'\nimport re\nt=open('ARY_pages.txt',encoding='utf-8',errors='replace').read()\nfor w in ['سرد','سال','کلاه','گوساله']:\n    print('===',w)\n    hits=[m for m in re.finditer(w,t)]\n    print(' count',len(hits))\n    for m in hits[:2]:\n        print('   ',t[max(0,m.start()-200):m.start()+300].replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T16:17:49.973Z] TOOL RESULT

```
=== سرد
 count 20
     و «گرگث» و دقازه و «راش» (882614) و «غان» (81071) و «ماهی آزان (5۸14۸/1030) و «ییده (/۷11-1-07) و «بلوط» (0۸74) و «زنبور؛ (81312) و «اردکث» (01700) نشان می‌دهد که خاستگاه این مردم در یک ناحیه نسبتاً سردسیر بود. چون اگر مثلاً  پپی ..خاستگاه آنها در ناحیه‌ی گرسیر با استوایی بود واژه‌های همریشه‌ی آنها وابسته بهگیاهان و جانوران گزمسیری می‌بود در حالیکه تفریباً همه‌ی واژه‌های گرمسیری و استوایی از ریشه‌ی هند و اروپایی نبوده و در چند سده‌ی اخیر وارد زبانهای هند و اروپایی شده‌اند. البته واژه‌های هند و 
    ی برمی‌خورند يا نام محلی را می‌پذپرفتند» یا نام جدیدی را نوآوری می‌کردند و يا نام هند و اروپایی قدیمی را برای آن بکار می‌بردند. این فرآیند امروز اهر صادق است. واژه‌ی «یخچالء (چاله‌ی یخ) را برای ابزار سرد ساز برقی بکار می‌پریم. واژه‌ی «سپر» را ۰۹ 48۶ که مدتها عملاً کاربرد روزمره نداشت برای بخشی از اتومبیل بگار می‌بریم, اصولاً ردیابی واژگانی بیشتر روی همریشگی تاکید دارد نه هم چمی.  ضمناً همه‌ی واژه‌های همريشه (۲0011۸7) در تعیین خاستگاه هند و اروپائیان رهنمون نیستند. مثلاً ریشه‌ی هند و اروپابی --۳0
=== سال
 count 53
     ۵. دیباچه «هند و اروپایی» نامی است که به خانواده‌ی بزرگی از زبانها داده می‌شود. این خانواده شامل تفریباً همه‌ی زبانهای اروپا و فلات ایران و بخش شمالی شبیه قاروی هند می‌شود. کوچگری آروپائیان در پانصد سال گذشته دامنه‌ی زبانهای هند و اروپایی را در سرتاسر آمریکای شمالی و جنوبی و مرکزی و همچنین در استرالیاگبترش داده است. ضمناً در گذشته زبان مردم آذرپایجان و آسپای صغیر و آسپای مرکزی و چین باختری (ایالت سین کیانگ) نیز هند و اروپایی بوده ولی هجوم تبایل ترکك زبان (از حدود سده‌ی پنج میلادی به بعد) موجب ا
    ر» برخي از دانشمندان (به ویژه دانشمندان روسی: .۰ "(۷۰1۷۸۵۵ 0۸2/6811022 3۰) چنین فرض کرده‌اند که گهواره‌ی مردمان هند و اروپایی کردستان و سرزمین‌های اطراف آن است چون در اين نواحی بود که در حدود ده هزار سال پیش کشاورزی و اهل‌سازی دام‌ها نو آوری شد و این نوآوری‌ها شهرزیستی و ازدیاد جمعیت و ایجاد ارتش و فناوری وگسترش از راه کوچگری را میسر نمود. بنابراین دیدمان (17733083) مردمان این سرزمین کم‌کم از یک سو به فلات ایران و شمال هندوستان و از سوی دیگر به آسیای صغیر و از آنجا به اروپاً اکوج کردند. نکات زیر
=== کلاه
 count 12
    0): فریزی کهن (۷نها5ل۶۸ ص0): 3 نا ار  ۸ م۸لا۸ آلمانی کهن (۵07/ل057 ۲/04 طا0):  پهلری (۲1اتله): ۷ ,وال۲۸ رال ای اوستی (0838716): لاله ,۸۷0۸ آلمانی (4۸ق058): وال۲۱ کردی (0732134): 0۷ ,۸5 انگلیسی کهن (بزکلاهل8 صا۵): 07358 سانسکریت (52077/ه5): انگلیسی (بالاه8۸): 0  ,۸۷۷۸8 ,ش۲7۸8لم۸ م۸ دانمارکی (0۸271874): ۸ یونانی (7)0677 لاد | سرئدی (81780[157): ۸۳۸ لانین (/710مل): 1 نروژی (/۸/0737801۸): ۸ گرنبکه (007112): 3 هلندی (1[ج017): و ادزرن ۹  ابسلند یگهن (10۸1۸۸7 یه صاه): اسلاوی کهن (314۲76 بل #نال) صان): 
    #لفاکلا۶ صا0): 8878۳ 2 (187338 ها) ههام25 آلمانی کهن ((027/۸ 104لز صا0): 1516 اه 0 880۸ 8 (ل8۸37) :0102/5 آلمانی (0570/۸04): دزی ان ] 7 (5۸33۲) +3 انگلیسی کهن (بژکلا80/0 صا۵م): 803718 55 0 انگلیسی (للکلاه/(8): ای ۱ برهان قاطع + ۹۸ دانمارکی (0۸(]84): 1.02 یادداشت: : ۱ واژه‌های "رد" و "ارت" و "ارنا" در ارستایی به معنی "پاکی" و "تقدس " و "جای مقدس" نیز به کار فه‌اند. ۲ 863۸7 ,001078 واجریشه‌های هند و آروپایی و هند و ایرانی این واژه را نمی‌دهند. 4 ۱ ۱ | توانگلیسی سروازی نارسا ۷۵8 اوستایی (4787۸4): ۸
=== گوساله
 count 1
    1 (87583) +7 دماری رفسطلا ‏ 708 بو برهان قاطع + ۱۲ سوئدی (90207517): ب#لا[] لغت‌نامه دهخدا : ۱۳۳۷۲ پادداشت: چم اين واژه در سانسکریت: قری و سترگك. چم این واژه در زبان‌های ژرمنی و رومانس و سلتی:گاو نره گوساله‌ی نر, [pdf page 349] ۵۰ ) ستوسه شنوسه اشنوسه؛ سنرسه (به چم "عطسه") فارسی (۳8۸۹۸/۷): استوسه, شنوسه, اشنوسه, سنوسه (به چم عطسه:) | چم‌انگلیسی سرواژی فارسن 0 ور ۱88828 پهلری (7اتله۸): ان بایان سوئدی (5178:201377): ۷۷8۸ سانسکریت (5۸/5717): ردنا نروژی (/081850142/: انیا ارمتی (47482/1۸7): اد انشا
```


## [2026-09-06T16:17:56.683Z] TOOL CALL #100: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-06T16:17:56.726Z] TOOL RESULT

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


## [2026-09-06T16:18:56.736Z] AGENT

Now I'll write the verification file.


## [2026-09-06T16:29:40.322Z] TOOL CALL #101: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk250.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\nE0_NODES = [\n dict(id=1, lang=\"Avestan\", words=\"sareta; saretha\",\n  verdict=\"confirmed\",\n  derivation=\"Both words are Bartholomae's. AiW col. 1565-66 has 'j. sarəta- Adj. \\\"kalt\\\"' (attested Vd. 7.3 'dva hąmina māh(a) … sarəta āpō, sarəta zəmō, sarəta urvarayā', of the two summer months that are still too cold), with the note 'np. sard, lit. šáltas … mp. sart'; and col. 1568 'j. sarə-δā- \\\"gelidus, Kälte bringend\\\"' (Vr. 2.2, of the mid-winter feast maiδyāirya-), built on a noun *sar- 'Kälte, Frost'. Nourai's 'saretha' is his transliteration of sarəδā-, in which he renders the Avestan spirant δ by ⟨th⟩ (the same digraph he uses for θ in 'thard' below); the form itself, and the gloss 'bringing cold', are exactly Bartholomae's. Phonetically Av. sarəta- is the verbal adjective *ḱl̥H-to- of the root, i.e. zero grade + *-ta-, matching Skt. śiśira- 'cool' (reduplicated) and Lith. šáltas 'cold'; the Avestan ə is the regular anaptyctic vowel of Iranian *r̥ before a dental.\",\n  derivation_fa=\"اوستایی sarəta- «سرد» (وندیداد ۷٫۳) و sarəδā- «سرمازا، سرماآور» (ویسپرد ۲٫۲) هر دو در فرهنگ ایرانی باستانِ بارتولومه (ستون‌های ۱۵۶۵–۱۵۶۸) آمده‌اند و بارتولومه خودْ فارسی «سرد» و پهلوی sart را ذیل همین مدخل یاد کرده است. صورت sarəta- صفتِ فعلیِ ریشه است (هندواروپاییِ آغازین *ḱl̥H-to-)، هم‌ریشه با سنسکریت śiśira- «خنک» و لیتوانیایی šáltas «سرد»؛ حرفِ ə در آن واکهٔ میانجیِ ایرانیِ *r̥ است. آنچه نورایی «saretha» نوشته همان sarəδā- است و او δ اوستایی را ⟨th⟩ آوانگاری کرده است. ادعای نورایی در این گره درست است.\",\n  sources=[W+\"Reconstruction:Proto-Iranian/carHd%C3%A1h\"],\n  ref_check=[\n   dict(ref=\"POK:551\", status=\"supports\", note=\"POK_02.txt leaf for printed p.551 (awk RS=\\\"\\\\f\\\" NR==209..211): '1. ḱel- 1. \\\"frieren, kalt\\\", 2. \\\"warm\\\" … 1. Ai. śiśira- \\\"kühl, kalt\\\", m. \\\"kühle Zeit, Kälte\\\", av. sarəta- \\\"kalt\\\", npers. sard ds., osset. sald \\\"Kälte\\\", av. sarə-δā- \\\"Kälte bringend\\\"' — Nourai's two Avestan words in Pokorny's own order.\"),\n   dict(ref=\"SYN:1078\", status=\"supports\", note=\"Buck §15.86 COLD, printed p.1078 (SYN.txt line 27293 ff.): 'Lith. šaltas, Lett. salts …; Skt. (with reduplication) śiśira-, Av. sarəta-, N Pers. sard, also in Av. sarə-δā- \\\"bringing cold\\\"; Osset. sald sb. \\\"cold\\\".'\")],\n  consulted=[\n   dict(src=\"BRT\", where=\"Altiranisches Wörterbuch cols. 1565-66 and 1568 (BRT.txt lines 26100-26140)\", stance=\"supports\", note=\"'j. sarəta- Adj. \\\"kalt\\\": dva (näml. māŋhō) hąmina taēca həṇti … V.7.3. np. sard, lit. šáltas … mp. sart' and 'j. sarə-δā- \\\"gelidus, Kälte bringend\\\" … *sar- f. \\\"Kälte, Frost\\\"; vgl. sarəta-'.\"),\n   dict(src=\"CHEUNG\", where=\"Etymological Dictionary of the Iranian Verb s.v. *sarH1 (CHEUNG.txt lines 22040-22085)\", stance=\"supports\", note=\"'*sarH1 \\\"to cool, become cold\\\" • AVESTAN: Y Av. sarəta- \\\"cold\\\" (V 1.3) … «PIE *ḱelH- \\\"to freeze\\\" … LIV: 323 | Pok.: 551f.'\"),\n   dict(src=\"WLD\", where=\"Walde-Pokorny I 429 (WLD_Bd1_pages.txt leaf 437)\", stance=\"supports\", note=\"'1. ḱel- 1. „frieren, kalt“, 2. „warm“. 1. Ai. śiśira- „kühl, kalt“ …, av. sarəta- „kalt“, np. sard ds., osset. sald „Kälte“, av. sarə-δā- „Kälte bringend“.'\")],\n ),\n dict(id=2, lang=\"Pahlavi\", words=\"sart; sarmâk; awsartan\",\n  verdict=\"confirmed\",\n  derivation=\"All three are attested Book-Pahlavi words. MacKenzie's Concise Pahlavi Dictionary gives 'sard [slt' | M srd, N ~] cold. ~īh: coldness', 'sarmāg [slm'k' | N sarmā] coldness' and 'afsardan, afsar- ['psltn'] cool down; afsārdan, afsār- ['ps'ltn'] cool, freeze, extinguish'; Nyberg's glossary has 'sart [slt'] cold 86-14. — Av. (1566) sarəta-' and 'apa-sartan ['ps'ltn'] to quench, to extinguish (fire) … properly \\\"to cool down\\\" … NP afsurdan \\\"to congeal\\\"'. Nourai's spelling 'awsartan' reflects the Aramaeographic-looking heterogram ʾp- read as aw-/af- (Middle Persian abe-/af- < Old Iranian *apa-), so the verb is *apa-sarta- 'to cool off'; sarmāk is sard + the abstract suffix -māg (cf. NP garmā : sarmā, where Nöldeke, in Horn no. 731, explains sarmā as analogical to garmā). Old Iranian intervocalic -t- after r stays as -t/-d in Middle Persian, so *ḱl̥H-to- > sart is regular. The only inaccuracy is the gloss 'to lose hope' attached to awsartan: in Middle Persian the verb is only physical ('to cool, freeze, extinguish'); the figurative sense belongs to the New Persian stage.\",\n  derivation_fa=\"هر سه واژه در پهلویِ کتابی گواهی شده‌اند: مکنزی sard «سرد»، sarmāg «سرما» و afsardan/afsārdan «سرد شدن، یخ بستن، خاموش کردن» را می‌آورد و نیبرگ در واژه‌نامهٔ خود sart را با ارجاع به اوستایی sarəta- و apa-sartan را «خاموش کردن (آتش)، در اصل سرد کردن» ثبت کرده است. آنچه نورایی «awsartan» نوشته همان صورتِ نوشتاریِ ʾp-sltn است، یعنی *apa-sarta- از پیشوندِ ایرانیِ باستانِ *apa- «باز، فرو». sarmāg از sard با پسوندِ -māg ساخته شده و به گفتهٔ نُلدکه (نزد هرن، شمارهٔ ۷۳۱) «سرما» بر قیاسِ «گرما» ساخته شده است. تنها نکتهٔ نادرست، معنیِ «امید باختن» است که برای فعلِ پهلوی داده شده؛ این معنیِ مجازی از دورهٔ فارسی نو پدید آمده است.\",\n  sources=[W+\"%D8%A7%D9%81%D8%B3%D8%B1%D8%AF%D9%86\"],\n  ref_check=[dict(ref=\"HRN:23\", status=\"supports\", note=\"Horn, Grundriss p.23 no. 100 (HRN.txt leaf 45): 'efsurden \\\"frieren, gefrieren\\\", fusurden, fisurden (Šāhn. I, 78 Vers 211). phlv. afsartan, afsar(i)šnīh (vd. 19,12), vergl. arm. surb \\\"Kälte\\\". Siehe np. serd (No. 731).' — exactly Nourai's Pahlavi verb and its link to sard.\")],\n  consulted=[\n   dict(src=\"PHD\", where=\"MacKenzie, Concise Pahlavi Dictionary s.vv. sard, sarmāg, afsardan (PHD.txt lines 172, 564)\", stance=\"supports\", note=\"'sard [slt' | M srd, N ~] cold. ~īh: coldness'; 'sarmāg [slm'k' | N sarmā] coldness'; 'afsardan, afsar- ['psltn'] cool down. afsārdan, afsār- ['ps'ltn'] cool, freeze, extinguish.'\"),\n   dict(src=\"NYB\", where=\"Nyberg, Manual of Pahlavi II s.vv. sart and apa-sartan (NYB_vol2_glossary.txt lines 3403, 528)\", stance=\"supports\", note=\"'sart [slt'] cold 86-14. — Av. (1566) sarəta-'; 'apa-sartan ['ps'ltn'] to quench, to extinguish (fire) 116-7. — Properly \\\"to cool down\\\" … cf Paz. awasard \\\"frozen\\\" (SGV); NP afsurdan \\\"to congeal\\\"; MPrth wysr- \\\"to cool\\\".'\"),\n   dict(src=\"CHEUNG\", where=\"s.v. *sarH1, Middle Persian section\", stance=\"supports\", note=\"'MMP srd'g \\\"cold(ness)\\\", BMP slt /sard/ \\\"cold\\\" || (+ *apa-) BMP 'psl- /afsar-/ \\\"to cool down\\\" … Inf.: BMP 'psltn /afsardan/.'\")],\n ),\n dict(id=3, lang=\"Persian\", words=\"sard «سرد ( سرما )»; afsordan «افسردن»\",\n  verdict=\"confirmed\",\n  derivation=\"NP سرد sard continues MP sard [slt'] without change; سرما sarmā continues MP sarmāg with the regular New Persian loss of final -g (MP -āg > NP -ā, cf. MP wistāg > NP گواه? rather MP dānāg > NP دانا). افسردن afsordan continues MP afsardan/*apa-sartan 'to cool down, freeze'; the New Persian present stem is afsar- (افسر-), and the past stem shows the usual raising a > o before the cluster in the Classical orthography (afsurdan in Horn, afsordan today). Semantically the physical sense 'to freeze, to wither' is the older one — Borhān-e Qāṭeʿ, on the very page Nourai cites, defines it 'بمعنی سرد شدن و یخ بستن و منجمد گردیدن باشد' and only then adds 'و از چیزی و کسی دل سرد شدن هم هست', i.e. the figurative 'to become disheartened' that Nourai gives as the gloss ('to lose hope'). Cheung reconstructs the whole set under Proto-Iranian *sarH1 'to cool, become cold' < PIE *ḱelH-.\",\n  derivation_fa=\"«سرد» بی‌هیچ دگرگونی از فارسی میانهٔ sard آمده و «سرما» از sarmāg پهلوی است با افتادنِ -گ پایانی که قاعدهٔ گذر از فارسی میانه به فارسی نو است. «افسردن» دنبالهٔ afsardan پهلوی (*apa-sarta-) است با ستاکِ حالِ «افسر-». معنیِ نخستینِ آن مادّی است: برهانِ قاطع در همان صفحه‌ای که نورایی ارجاع داده می‌نویسد «بمعنی سرد شدن و یخ بستن و منجمد گردیدن باشد» و سپس می‌افزاید «و از چیزی و کسی دل سرد شدن هم هست» — یعنی همان معنیِ مجازیِ «دل‌سرد شدن/امید باختن» که نورایی آورده است. چونگ همهٔ این صورت‌ها را زیرِ ریشهٔ ایرانیِ *sarH¹ «سرد شدن» از هندواروپاییِ *ḱelH- می‌آورد. ادعای نورایی درست است.\",\n  sources=[W+\"%D8%B3%D8%B1%D8%AF\", W+\"%D8%A7%D9%81%D8%B3%D8%B1%D8%AF%D9%86\"],\n  ref_check=[\n   dict(ref=\"POK:551\", status=\"supports\", note=\"Pokorny p.551 lists 'npers. sard' directly among the reflexes of ḱel-1 'kalt' (POK_02.txt, printed p.551).\"),\n   dict(ref=\"SYN:1078\", status=\"supports\", note=\"Buck §15.86: '… Av. sarəta-, N Pers. sard …'\"),\n   dict(ref=\"BQT:149\", status=\"partial\", note=\"BQT_v1_pages.txt leaf 365 (printed ≈ p.150-155 with the volume's drifting leaf offset, so within a few pages of Nourai's 149) carries the افسردن entry: 'افسردن، بر وزن افشردن، بمعنی سرد شدن و یخ بستن و منجمد گردیدن باشد - و از چیزی و کسی دل سرد شدن هم هست' — both of Nourai's senses, but the Borhān entry itself carries no etymological footnote here, and the headword سرد is in vol. 2, not at p.149.\")],\n  consulted=[\n   dict(src=\"HRN\", where=\"Horn, Grundriss no. 731, p.161 (HRN.txt line 6383)\", stance=\"supports\", note=\"'731. serd \\\"kalt\\\", sermā \\\"Kälte\\\". g. sart, aw. sarəta- \\\"kalt\\\"; phlv. sart, sarmāk (Bund.); skr. vergl. śiśira- \\\"Kälte\\\"; arm. saṙn \\\"Eis\\\" …; lit. száltas \\\"kalt\\\". … np. sermā erklärt Nöldeke … als Analogiebildung nach germā \\\"Wärme\\\".'\"),\n   dict(src=\"CHEUNG\", where=\"s.v. *sarH1, NWIR section\", stance=\"supports\", note=\"'NP sard, Bal. sart, Kurd. sar \\\"cold\\\" || (+ *apa-) NP afsurdan/afsār- \\\"to congeal\\\".'\"),\n   dict(src=\"BQT\", where=\"Borhān-e Qāṭeʿ ed. Moʿin, vol. 1, the افسردن entry (leaf 365)\", stance=\"supports\", note=\"quoted above; Borhān's own second sense 'دل سرد شدن' is Nourai's 'to lose hope'.\")],\n ),\n dict(id=4, lang=\"Sogdian\", words=\"srt\",\n  verdict=\"confirmed\",\n  derivation=\"Gharib's Sogdian Dictionary, entry 8963: 'srt- B, sart ©<Av. sarəta-, Yaghn. sort ©nom. ob. -y, cold', with citations from the Vessantara Jātaka (VJ 533, 961) and the Sūtra of the Causes and Effects (SCE 291). The Buddhist-Sogdian spelling srt renders /sart/, the same *ḱl̥H-to- adjective as Avestan sarəta- and Middle Persian sard; Sogdian, like Middle Persian, keeps the cluster -rt-. Yaghnobi sort continues it today. Nourai's page number is one off: the entry stands on printed p.363 of Gharib (the running head 'srt' begins that page), not 362 — a one-page offset that recurs in his next Sogdian citation.\",\n  derivation_fa=\"در فرهنگ سغدیِ بدرالزمان قریب، مدخل ۸۹۶۳: «srt- (B) sart، از اوستایی sarəta-، یغنابی sort، به معنی سرد» با شاهدهایی از وسنتره‌جاتکه و سوترهٔ علت و معلول. املای srt در سغدیِ بودایی همان صفتِ *ḱl̥H-to- است که در اوستایی sarəta- و در فارسی میانه sard شده؛ سغدی نیز مانند فارسی میانه خوشهٔ -rt- را نگه می‌دارد و یغنابیِ امروز sort دنبالهٔ آن است. تنها نکته آنکه شمارهٔ صفحه یک واحد جابه‌جاست: این مدخل در صفحهٔ ۳۶۳ چاپیِ قریب است نه ۳۶۲.\",\n  sources=[],\n  ref_check=[dict(ref=\"SOD:362\", status=\"partial\", note=\"SOD_pages.txt line 29594: '8963 srt - B … sart ©<Av sarəta-, Yaghn. sort ©nom. ob. -y, cold. GMS 526; TSP 2.420, 3, 259, 265; VJ 533, 961; SCE 291.' The content is exactly Nourai's, but the page-number marker '362' in the scan falls before entry 8963, so the entry is on p.363.\")],\n  consulted=[\n   dict(src=\"SOD\", where=\"Gharib, Sogdian Dictionary, entry 8963 (p.363)\", stance=\"supports\", note=\"quoted above; Gharib himself derives it from Av. sarəta-.\"),\n   dict(src=\"CHEUNG\", where=\"s.v. *sarH1, Sogdian section\", stance=\"supports\", note=\"'SOGDIAN: BSogd. srt, srty \\\"cold\\\" || (+ *apa-) MSogd. 'psyr'mndyy \\\"cooling, freezing\\\" || (+ *ham-) BSogd. 'ns'rty \\\"cold, cooled\\\".'\")],\n ),\n dict(id=5, lang=\"Avestan\", words=\"sarez, sareda\",\n  verdict=\"transcription_suspect\",\n  error_in=\"book\", book_prints=\"sarez, sareda\", correct_form=\"sarəd- (with the derivative sarəδa-)\",\n  derivation=\"The second form is right, the first is not. Avestan has sarəd- f. 'year' (Bartholomae AiW 1566: 'j. sarəd- f. \\\"Jahr\\\": … pasca pancasatəm sarəδəm V.14.15 … — osset. särd \\\"Sommer\\\", np. sāl \\\"Jahr\\\"; ai. vgl. śarád- f. \\\"Herbst; Jahr\\\" … Pü.: sāl') and beside it the adjective/derivative sarəδa- m., 'Name der Gottheiten der Jahre … Ableitung aus sarəd-, eig. Adj. \\\"auf das Jahr bezüglich\\\"'. Nourai's 'sareda' is that sarəδa-; his 'sarez' answers to nothing in the Avestan lexicon — there is no *sarəz-, and the sequence would be phonetically impossible for this stem, whose final consonant is the voiced dental spirant δ. The printed page (pdf 250) really does read 'sarez, sareda', so the extraction is faithful and the slip is the author's, almost certainly a keying error for 'sared' (= sarəd-). The gloss 'a warm season, a year' is Buck's and Pokorny's explanation ('\\\"Herbst\\\" als \\\"warme Zeit\\\"'), so the semantics of the box are sound.\",\n  derivation_fa=\"صورتِ دوم درست است و صورتِ نخست نادرست. در اوستایی sarəd- (مادینه) «سال» هست — بارتولومه ستون ۱۵۶۶: «j. sarəd- f. \\\"Jahr\\\" … اوستی särd \\\"تابستان\\\"، فارسی نو sāl، سنسکریت śarád- \\\"پاییز؛ سال\\\"، پهلوی sāl» — و در کنارِ آن sarəδa- که خودْ برساختهٔ همان است. آنچه نورایی «sareda» نوشته همان sarəδa- است، اما «sarez» در واژگانِ اوستایی هیچ مابه‌ازایی ندارد؛ *sarəz- نه گواهی شده و نه از دیدِ آوایی ممکن است، چون همخوانِ پایانیِ این ستاک سایشیِ واکدارِ دندانیِ δ است. تصویرِ صفحهٔ چاپی نشان می‌دهد که کتاب خودْ «sarez, sareda» چاپ کرده است؛ پس خطای خوانشِ اسکن نیست، خطای چاپیِ کتاب است و به‌احتمالِ زیاد «sared» باید می‌بود. معنیِ «فصلِ گرم، سال» همان توضیحِ باک و پوکورنی است («پاییز» به معنیِ «هنگامِ گرم») و درست است.\",\n  sources=[W+\"Reconstruction:Proto-Iranian/carHd%C3%A1h\"],\n  ref_check=[\n   dict(ref=\"POK:551\", status=\"supports\", note=\"Pokorny p.551 §2: 'Ai. śarád- f. \\\"Herbst\\\", mit Zahlwörtern \\\"Jahr\\\", av. sarəd- f. \\\"Jahr\\\" … osset. särd \\\"Sommer\\\", np. sāl \\\"Jahr\\\" (\\\"Herbst\\\" als \\\"warme Zeit\\\") …' — the source of Nourai's gloss, but with the form sarəd-, not sarez.\"),\n   dict(ref=\"SYN:1012\", status=\"supports\", note=\"Buck §14.73 YEAR, p.1012 (SYN.txt line 25743): 'Av. sarəd-, OPers. θard- (certainly \\\"year\\\", not \\\"manner\\\" as Barth. 1566), NPers. sāl \\\"year\\\", Osset. särd \\\"summer\\\" : Skt. śarad- \\\"autumn\\\", also \\\"year\\\" in RV, etc., perh. as orig. \\\"warm season\\\" fr. … Lith. sìlius \\\"August\\\", šìlti \\\"grow warm\\\", Lat. calēre \\\"be warm\\\".'\")],\n  consulted=[\n   dict(src=\"BRT\", where=\"AiW cols. 1566-67 (BRT.txt lines 26118-26135)\", stance=\"partial\", note=\"'j. sarəd- f. \\\"Jahr\\\" … Pü.: sāl' and 'j. sarəδa- m. Name der Gottheiten der Jahre … Ableit. aus sarəd-, eig. Adj. \\\"auf das Jahr bezüglich\\\"'. No form sarəz- exists; Bartholomae also has a homonym 'p. θard-, j. sarəd- f. \\\"Art, Gattung\\\"' which Buck (p.1012) rejects for Old Persian.\"),\n   dict(src=\"WLD\", where=\"Walde-Pokorny I 429 §2 (leaf 437)\", stance=\"supports\", note=\"'2. Ai. śarád- f. \\\"Herbst\\\", mit Zahlwörtern \\\"Jahr\\\", av. sarəd- f. \\\"Jahr\\\" …, np. sāl \\\"Jahr\\\".'\")],\n ),\n dict(id=6, lang=\"Pahlavi\", words=\"sâlak, sâl\",\n  verdict=\"plausible\",\n  derivation=\"MP sāl 'year' is right and its ancestry is right in substance, but two details need correcting. (a) The Middle Persian word descends from the South-West Iranian form, i.e. Old Persian θard-, not from the Avestan (Central/East Iranian) sarəd-: the diagnostic is the change *-rd- > -l-, which is a South-West Persian development (*sarda- > sāl, with compensatory lengthening); an inherited Avestan sarəd- would have given MP *sard, as the homonymous word for 'kind' in fact did (MacKenzie 'sardag [sltk' = Av. sarada-] sort, kind'). Nyberg states the pedigree plainly: 'sāl, Prth sar [ŠNT] year … — Av. (1566) sarəd-, OP θard-; MPrthPrs sr; Paz. NP sāl.' (b) sālag is not a word for 'year'. MacKenzie's English index reads 'year sāl; -years-old -sālag', and Nyberg cites 'hac 7-sālak apāc \\\"for seven years\\\"'; Horn no.691 likewise glosses 'phlv. sāl, sālak \\\"alt\\\"'. It is the suffixed adjective *sāla-ka- '-year-old', the element that gives NP گوساله its second half.\",\n  derivation_fa=\"«سال» پهلوی درست است و تبارِ آن نیز در اصل درست، اما دو نکته باید اصلاح شود. نخست آنکه صورتِ فارسیِ میانه از شاخهٔ جنوب‌غربی، یعنی از پارسیِ باستانِ θard-، آمده است نه از اوستاییِ sarəd-؛ نشانهٔ آن دگرگونیِ آواییِ *-rd- ← -l- است که ویژهٔ فارسیِ جنوب‌غربی است (*sarda- ← sāl با کشیدگیِ جبرانی)؛ اگر صورتِ اوستایی موروثی می‌بود، در پهلوی *sard می‌شد، چنان‌که همان واژه به معنیِ «گونه، نوع» در پهلوی sardag شده است. نیبرگ می‌نویسد: «sāl، پارتی sar، سال — اوستایی (۱۵۶۶) sarəd-، پارسی باستان θard-». دوم آنکه sālag به‌تنهایی «سال» نیست: مکنزی آن را «-ساله، به سنِ … سال» می‌داند و هرن (شمارهٔ ۶۹۱) آن را «کهن‌سال» معنی می‌کند؛ همین جزء است که نیمهٔ دومِ «گوساله» را می‌سازد. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n  sources=[W+\"%D8%B3%D8%A7%D9%84\"],\n  ref_check=[dict(ref=\"HRN:153\", status=\"supports\", note=\"Horn, Grundriss p.153 no. 691 (HRN.txt leaf 175): '691. sāl \\\"Jahr\\\". aw. sarəδa- \\\"Jahr\\\"; phlv. sāl, sālak \\\"alt\\\"; arm. LW. nava-sard …; skr. śarád- \\\"Herbst, Jahr (mit Zahlen)\\\". oss. d. särdä, t. särd \\\"Sommer\\\".' — Nourai's Pahlavi box in full, but with 'alt' for sālak.\")],\n  consulted=[\n   dict(src=\"PHD\", where=\"MacKenzie, Concise Pahlavi Dictionary, English index (PHD.txt lines 752, 4369)\", stance=\"partial\", note=\"'year sāl; -years-old -sālag'; 'age dad, -sālagīh' — sālag is the '-year-old' formant, not a noun 'year'.\"),\n   dict(src=\"NYB\", where=\"Nyberg, Manual of Pahlavi II s.v. sāl (NYB_vol2_glossary.txt line 3381)\", stance=\"supports\", note=\"'sāl, Prth sar [ŠNT] year; in dating: apar sāl 2 mazdēsn bay Šāhpuhr … — Av. (1566) sarəd-, OP θard-; MPrthPrs sr; Paz. NP sāl.'\"),\n   dict(src=\"BRT\", where=\"AiW col. 1566\", stance=\"supports\", note=\"the Pahlavi gloss of Av. sarəd- is given as 'Pü.: sāl'.\")],\n ),\n dict(id=7, lang=\"Persian\", words=\"sâl «سال»; gŭsâleh «گوساله»\",\n  verdict=\"confirmed\",\n  derivation=\"سال sāl is MP sāl unchanged, from *sarda- with the South-West Iranian *rd > l; Wiktionary's chain 'Persian سال < Middle Persian sāl < Old Persian θard < Proto-Iranian *carHdáh < Proto-Indo-Iranian *ćarHáts' is the standard one (though the entry cites Nourai's own p.220 among its references, so it is not fully independent for this page). گوساله gūsāla is a transparent compound: gāw/gō 'cow, ox' + sāl(ag) '-year-old' + the nominal -a, i.e. 'yearling (of the cow)'. Horn analyses it exactly so at no. 941 — 'gōsāle \\\"Kalb\\\" … Das ō in gōsāle stammt von gō \\\"Kuh\\\" (No. 888)' — and compares Skt. vatsá- 'calf, yearling', which is the same metaphor built on the other IE word for 'year' (*wet-). Nourai's cross-reference ☞Gwou (PIE *gʷōw- 'cow') for the first element is correct.\",\n  derivation_fa=\"«سال» بی‌دگرگونی از sāl فارسی میانه است، و آن از *sarda- با تبدیلِ ویژهٔ جنوب‌غربیِ rd ← l. زنجیرهٔ ویکی‌واژه — فارسی «سال» ← فارسی میانهٔ sāl ← پارسی باستانِ θard ← ایرانیِ آغازینِ *carHdáh — همان زنجیرهٔ پذیرفته‌شده است (هرچند همان مدخل خودْ به کتابِ نورایی، ص ۲۲۰، ارجاع داده و از این رو برای این صفحه گواهِ کاملاً مستقلی نیست). «گوساله» ترکیبی روشن است: «گو/گاو» + «سال(ه)» یعنی «یک‌سالهٔ گاو»؛ هرن در شمارهٔ ۹۴۱ همین تحلیل را دارد و آن را با سنسکریت vatsá- «گوساله، یک‌ساله» می‌سنجد که همان استعاره است اما بر پایهٔ واژهٔ دیگرِ هندواروپایی برای «سال» (*wet-). ارجاعِ نورایی به ریشهٔ Gwou برای جزءِ نخست نیز درست است. ادعای نورایی درست است.\",\n  sources=[W+\"%D8%B3%D8%A7%D9%84\", W+\"%DA%AF%D9%88%D8%B3%D8%A7%D9%84%D9%87\"],\n  ref_check=[\n   dict(ref=\"POK:551\", status=\"supports\", note=\"Pokorny p.551 §2 gives 'np. sāl \\\"Jahr\\\"' as the New Persian reflex.\"),\n   dict(ref=\"SYN:1012\", status=\"supports\", note=\"Buck §14.73: 'Av. sarəd-, OPers. θard- …, NPers. sāl \\\"year\\\", Osset. särd \\\"summer\\\" : Skt. śarad- \\\"autumn\\\", also \\\"year\\\" …'\")],\n  consulted=[\n   dict(src=\"HRN\", where=\"Horn, Grundriss no. 941, p.210 (HRN.txt line 8171)\", stance=\"supports\", note=\"'941. gōsāle \\\"Kalb\\\". ai. vatsá- \\\"Kalb, Jährling\\\". … Das ō in gōsāle stammt von gō \\\"Kuh\\\" (No. 888).'\"),\n   dict(src=\"PHD\", where=\"MacKenzie, English index s.v. year\", stance=\"supports\", note=\"'year sāl; -years-old -sālag' — the two elements of gō-sālag.\"),\n   dict(src=\"ARY\", where=\"Aryanpur, Farhang-e Rishe-hā (ARY_pages.txt, entry near pdf p.349)\", stance=\"silent\", note=\"the گوساله entry exists but the Latin-script etyma in the OCR are unreadable ('چم این واژه در زبان‌های ژرمنی و رومانس و سلتی: گاو نره، گوسالهٔ نر'); nothing quotable on the root.\")],\n ),\n dict(id=8, lang=\"Old Persian\", words=\"thard, sard; upa-sard\",\n  verdict=\"plausible\",\n  derivation=\"θard- is genuine and exactly as Kent gives it: 'θard- sb. \\\"year\\\": Av. sarəd- \\\"year\\\", NPers. sāl, Skt. śarád- \\\"autumn\\\"', attested in the Behistun inscription (θardam DB 5.3, θarda gen. DB 4.4, 41, 45, 52, 60, in the recurring formula hamahyāyā θarda 'in one and the same year'). Buck adds that the meaning is 'certainly \\\"year\\\", not \\\"manner\\\" as Barth. 1566'. Two qualifications: (a) 'sard' is not an Old Persian form — Old Iranian *ć gives OP θ but Median/Avestan s, so sard is the Median/Avestan shape (and the source of the borrowed vocabulary of Middle Persian), not an OP variant; (b) 'upa-sard' is not attested in Old Persian. It is a reconstruction, and a good one: MacKenzie's Pahlavi dictionary records '*afsālān ['fs'l'n' | (N ābsālān)] springtime' and lists 'spring(time) wahār, afsālān, mēdyē-zarm', which presupposes exactly *upa-sarda- 'towards the year, at the turn of the year' > MP *af-sāl. So the box is right in substance but presents a reconstruction as an attested Old Persian word.\",\n  derivation_fa=\"θard- گواهی‌شده است و دقیقاً همان است که کنت آورده: «θard- اسم «سال»: اوستایی sarəd-، فارسی نو sāl، سنسکریت śarád- \\\"پاییز\\\"»، با شاهدهایی از سنگ‌نبشتهٔ بیستون (θardam، DB ۵٫۳؛ θarda در DB ۴٫۴ و ۴۱ و ۴۵ و …) در ترکیبِ hamahyāyā θarda «در یک سال». باک نیز می‌افزاید که معنیِ آن «به‌یقین سال است، نه گونه چنان‌که بارتولومه در ستون ۱۵۶۶ پنداشته». دو نکته: نخست، «sard» صورتِ پارسیِ باستان نیست؛ *ć ایرانیِ باستان در پارسیِ باستان θ می‌شود و در مادی/اوستایی s، پس sard صورتِ مادی است. دوم، «upa-sard» در پارسیِ باستان گواهی نشده و بازسازی است — اما بازسازیِ خوبی است، چون مکنزی در فرهنگِ پهلوی *afsālān را با معنیِ «بهار» ثبت کرده که درست بر همین *upa-sarda- استوار است. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n  sources=[],\n  ref_check=[\n   dict(ref=\"KNT:188\", status=\"supports\", note=\"Kent, Old Persian, Lexicon p.188 (KNT.txt leaf 212): 'θard- sb. \\\"year\\\": Av. sarəd- \\\"year\\\", NPers. sāl, Skt. śarád- \\\"autumn\\\" (§31, §87, §142). … θardam asf. DB 5.3. θarda gsf. DB 4.4f, 41, 45, 52, 60.' No entry upa-sard-.\"),\n   dict(ref=\"SYN:1012\", status=\"supports\", note=\"Buck §14.73 p.1012: 'Av. sarəd-, OPers. θard- (certainly \\\"year\\\", not \\\"manner\\\" as Barth. 1566), NPers. sāl \\\"year\\\" …'\"),\n   dict(ref=\"BQT:7\", status=\"partial\", note=\"BQT_v1_pages.txt leaf 215 (≈ printed p.5-7) has the entry 'آب سالان - بالام بر وزن آب پاشان، بمعنی باغ باشد و بعربی حدیقه گویند' with a Moʿin footnote referring the reader to بهاران; the Persian word is there, but the page carries nothing on Old Persian upa-sard.\")],\n  consulted=[\n   dict(src=\"KNT\", where=\"Kent p.188\", stance=\"partial\", note=\"supports θard-, silent on upa-sard-.\"),\n   dict(src=\"BRT\", where=\"AiW col. 1566\", stance=\"partial\", note=\"Bartholomae files 'p. θard-, j. sarəd- f.' under the meaning 'Art, Gattung' (with the Behistun passages hamahyāyā θardā 'in jeder Weise'), separating it from 'j. sarəd- f. \\\"Jahr\\\"'; Buck and Kent reject that and read 'year', which is the modern consensus and Nourai's reading.\"),\n   dict(src=\"PHD\", where=\"MacKenzie s.v. *afsālān and English index s.v. spring(time)\", stance=\"supports\", note=\"'*afsālān ['fs'l'n' | (N ābsālān)] springtime'; 'spring(time) wahār, afsālān, mēdyē-zarm' — the Middle Persian reflex that presupposes *upa-sarda-.\")],\n ),\n dict(id=9, lang=\"Persian\", words=\"âbsâl «آبسال ( آبسالان )»\",\n  verdict=\"plausible\",\n  derivation=\"The derivation is sound but the gloss is contested. MacKenzie records Middle Persian '*afsālān ['fs'l'n'] springtime', explicitly equating it with New Persian ābsālān; the Pahlavi spelling ʾfsʾlʾn shows af- (< Old Iranian *apa-/*upa-) + sāl 'year' + the plural/temporal -ān, i.e. Nourai's *upa-sarda- 'at the turn of the year'. In New Persian the opaque af- was re-analysed as آب āb 'water' — a textbook folk etymology, helped by the abundance of آب- compounds — giving آبسال / آبسالان. The lexicographers then followed the re-analysis: Borhān-e Qāṭeʿ (the page Nourai cites) defines 'آب سالان … بمعنی باغ باشد و بعربی حدیقه گویند' and Dehkhodā likewise gives 'باغ، حدیقه' with a line of Nāṣer-e Khosrow, not 'spring'. So the etymology 'spring, turn of the year' is right at the Middle Persian stage, and Moʿin's own footnote on that Borhān page points the reader to بهاران; but the classical Persian dictionaries know آبسالان chiefly as 'garden'. Nourai's Vīs-o-Rāmīn verse ('همان شیپور با صد راه نالان / بسان بلبل اندر آبسالان') reads naturally with either sense.\",\n  derivation_fa=\"ریشه‌یابی درست است اما معنایی که نورایی داده جای گفت‌وگو دارد. مکنزی در فرهنگِ پهلوی *afsālān را با نویسهٔ ʾfsʾlʾn و معنیِ «بهار» ثبت کرده و آن را صریحاً برابرِ «آبسالان» فارسی نو دانسته است؛ ساختِ آن af- (از *apa-/*upa- ایرانیِ باستان) + sāl «سال» + پسوندِ -ān است، یعنی همان *upa-sarda-ی نورایی «به‌سوی سال، سرِ سال». در فارسی نو جزءِ ناشناختهٔ af- به «آب» بدل شد — نمونه‌ای آشکار از ریشه‌شناسیِ عامیانه که فراوانیِ ترکیب‌های «آب-» به آن یاری رسانده — و «آبسال/آبسالان» پدید آمد. فرهنگ‌نویسان نیز همین بازتحلیل را پی گرفتند: برهانِ قاطع در همان صفحه‌ای که نورایی ارجاع داده می‌نویسد «آب سالان … بمعنی باغ باشد و بعربی حدیقه گویند» و دهخدا نیز «باغ، حدیقه» آورده با بیتی از ناصرخسرو، نه «بهار». پس معنیِ «بهار» در مرتبهٔ فارسی میانه درست است ولی در فارسیِ کلاسیک معنیِ رایج «باغ» بوده است.\",\n  sources=[\"https://vajehyab.com/dehkhoda/%D8%A2%D8%A8%D8%B3%D8%A7%D9%84\"],\n  ref_check=[dict(ref=\"BQT:7\", status=\"partial\", note=\"BQT_v1_pages.txt leaf 215: 'آب سالان - بالام بر وزن آب پاشان، بمعنی باغ باشد و بعربی حدیقه گویند ۴' — the word is on the page Nourai cites, but Borhān glosses it 'garden', not 'spring'; Moʿin's footnote there is a cross-reference (قس: بهاران).\")],\n  consulted=[\n   dict(src=\"PHD\", where=\"MacKenzie, Concise Pahlavi Dictionary s.v. *afsālān (PHD.txt line 172) and English index s.v. spring(time)\", stance=\"supports\", note=\"'*afsālān ['fs'l'n' | (N ābsālān)] springtime' — the decisive evidence for *upa-sarda- and for the sense 'spring'.\"),\n   dict(src=\"BQT\", where=\"Borhān-e Qāṭeʿ vol. 1, آب سالان\", stance=\"partial\", note=\"gives 'باغ / حدیقه'.\"),\n   dict(src=\"MON\", where=\"Dehkhodā (which quotes Borhān and Moʿin) s.v. آبسال, via vajehyab\", stance=\"partial\", note=\"'اِ مرکب: باغ، حدیقه' with Nāṣer-e Khosrow's 'همی تابد ز چرخ سبز عیوق / چو آتش بر صحیفهٔ آبسالی'; no sense 'spring' and no etymological note.\")],\n ),\n dict(id=10, lang=\"Latin\", words=\"calor; calere; calefâre\",\n  verdict=\"confirmed\",\n  derivation=\"Latin caleō, calēre 'to be warm, be hot, glow' and its -os-stem derivative calor, calōris 'warmth, heat' are the standard Italic reflexes of the 'warm' half of the root: Watkins sets them under 'kelə-1. Warm … 2. Suffixed zero-grade form *kl̥ə-ē- in a. Latin calēre … 3. Suffixed zero-grade form *kl̥-os- in Latin calor, heat [Pok. 1. kel- 551]', and Pokorny prints 'lat. caleō, -ēre \\\"warm, heiß sein, glühen\\\", calidus \\\"warm, heiß\\\", calor \\\"Wärme, Hitze\\\"' in the same article as Avestan sarəta- and Persian sard. 'calefâre' is a small inexactness: classical Latin has the compound calefaciō, calefacere 'to make hot' (calēre + facere); *calefāre is the Vulgar Latin contraction reconstructed from the Romance forms (It. scaldare, Fr. chauffer), and it is that Vulgar Latin verb, not the classical one, that Nourai actually needs for the French box below.\",\n  derivation_fa=\"فعلِ لاتینِ caleō/calēre «گرم بودن، سوختن» و اسمِ برساختهٔ آن calor «گرما» بازتابِ ایتالیکِ نیمهٔ «گرم»ِ این ریشه‌اند: واتکینز آن‌ها را ذیلِ «kelə-1 گرم» می‌آورد و پوکورنی نیز در همان مقاله‌ای که اوستایی sarəta- و فارسیِ «سرد» را دارد می‌نویسد «lat. caleō, -ēre \\\"warm, heiß sein\\\", calidus, calor». صورتِ «calefâre» اندکی نادقیق است: لاتینِ کلاسیک calefacere دارد (calēre + facere «کردن»)، و *calefāre صورتِ بازسازی‌شدهٔ لاتینِ عامیانه است که از روی صورت‌های رومیایی (ایتالیایی scaldare، فرانسوی chauffer) بازسازی شده — و درست همین صورتِ عامیانه است که جعبهٔ فرانسویِ بعدی به آن نیاز دارد. ادعای نورایی درست است.\",\n  sources=[\"https://www.etymonline.com/word/chauffeur\"],\n  ref_check=[dict(ref=\"AHD\", status=\"supports\", note=\"Watkins 1985 (AHD_watkins1985.txt line 606): 'kelə-1. Warm. Variant *klē-, contracted from *kleə-. … 2. Suffixed zero-grade form *kl̥ə-ē- in: a. Latin calēre, to be warm: CALENTURE, CHAFE; … b. Latin derivative adjective calidus, warm (> French chaud) … 3. Suffixed zero-grade form *kl̥-os- in Latin calor, heat: CALORIC, CALORIE … [Pok. 1. kel- 551.]'\")],\n  consulted=[\n   dict(src=\"POK\", where=\"Pokorny p.551 (POK_full.txt line 49855)\", stance=\"supports\", note=\"'Latin caleo, -ere \\\"warm, be hot, glow\\\", calidus \\\"warm, hot\\\", calor \\\"warmth, heat\\\"' inside the article ḱel-1 'cold; warm'.\"),\n   dict(src=\"LAT\", where=\"Ernout-Meillet, Dictionnaire étymologique de la langue latine s.v. caleō\", stance=\"supports\", note=\"'caleo, -es, -ui, -iturus, -ere: être chaud (sens physique et moral) … Composé transitif: cal(e)facio, -is, -ere et ses dérivés … Formes nominales et dérivés: calor, -oris m.: chaleur.'\"),\n   dict(src=\"KLN\", where=\"Klein, Comprehensive Etymological Dictionary s.v. caldron/calid- (KLN_1966.txt, p.223 area)\", stance=\"supports\", note=\"the family 'calefacient, calenture, calescence, calorescence, caloric, caudle, chafe, chaldron, chauffeur, chowder, rechauffé, scald, nonchalant … base *kel-, \\\"warm\\\"'.\"),\n   dict(src=\"SYN\", where=\"Buck §15.85 WARM, p.1077-78\", stance=\"supports\", note=\"'3. IE *ḱel-, prob. the same ultimately as in words for \\\"cold\\\" … Lat. calidus …, with vb. calēre \\\"be warm\\\".'\")],\n ),\n dict(id=11, lang=\"French\", words=\"calorie, chauffeur, chauffage\",\n  verdict=\"confirmed\",\n  derivation=\"All three are French, and all three go back to Latin calēre, but by two different routes. calorie is a learned nineteenth-century coinage (Nicolas Clément's lectures, 1824-25, popularised from 1842) formed on Latin calor with the suffix -ie. chauffer 'to heat' is the inherited word: Vulgar Latin *calefāre (contracted from calefacere) > Old French chaufer > modern chauffer, with the regular Gallo-Romance ca- > cha- and intervocalic -f- from the -f- of facere; from it are formed chauffage 'heating' (with -age < Latin -āticum) and chauffeur, literally 'stoker', the man who fires a steam engine, which in the 1890s became the French nickname for the driver of an automobile.\",\n  derivation_fa=\"هر سه واژه فرانسوی‌اند و هر سه به فعلِ لاتینِ calēre بازمی‌گردند، اما از دو راه. calorie نوواژه‌ای دانشورانه از سدهٔ نوزدهم است (درس‌های نیکلا کلمان، ۱۸۲۴–۱۸۲۵) که از calor لاتین با پسوندِ -ie ساخته شده. اما chauffer «گرم کردن» واژه‌ای موروثی است: از لاتینِ عامیانهٔ *calefāre (کوتاه‌شدهٔ calefacere) به فرانسویِ کهنِ chaufer و سپس chauffer، با تحولِ منظمِ ca- ← cha- در گالو-رومی. از همین فعل chauffage «گرمایش» (با پسوندِ -age از -āticum لاتین) و chauffeur ساخته شده که در اصل «آتش‌کار، تون‌تابِ ماشینِ بخار» بوده و در دههٔ ۱۸۹۰ در زبانِ عامیانهٔ فرانسوی لقبِ رانندگانِ نخستین خودروها شد. ادعای نورایی درست است.\",\n  sources=[\"https://www.etymonline.com/word/chauffeur\"],\n  ref_check=[dict(ref=\"AHD\", status=\"supports\", note=\"Watkins s.v. kelə-1 lists French chaud under calidus and CHAFE (< OFr. chaufer) under calēre; the Latin > French link is Watkins's own.\")],\n  consulted=[\n   dict(src=\"KLN\", where=\"Klein s.vv. chafe, chauffeur\", stance=\"supports\", note=\"chafe 'fr. OF. chaufer … fr. VL. *calefare, fr. L. calefacere'; the same article cross-refers 'chauffeur, rechauffé'.\"),\n   dict(src=\"AHD\", where=\"Watkins 1985 s.v. kelə-1\", stance=\"supports\", note=\"'CALORIC, CALORIE' listed under *kl̥-os- > Latin calor.\")],\n ),\n dict(id=12, lang=\"Persian\", words=\"کالری ، شوفر ، شوفاژ\",\n  verdict=\"confirmed\",\n  derivation=\"Three twentieth-century French loanwords in Persian, taken directly from spoken French rather than through English: کالری kālrī = calorie, شوفر šufer = chauffeur, شوفاژ šufāž = chauffage (the -اژ spelling for French -age, as in گاراژ, ماساژ, is the standard Persian rendering and is itself proof of French, not English, mediation — English would have given *چافیج). Moʿin's Farhang tags شوفاژ '[فر.]' (French) and defines it 'گرمایش؛ هر یک از رادیاتورهای سیستم حرارت مرکزی', i.e. the sense has narrowed in Persian from 'heating' to 'radiator/central-heating unit'.\",\n  derivation_fa=\"سه وام‌واژهٔ فرانسویِ سدهٔ بیستم در فارسی که یکسره از فرانسویِ گفتاری گرفته شده‌اند نه از راهِ انگلیسی: «کالری» = calorie، «شوفر» = chauffeur، «شوفاژ» = chauffage. نگارشِ «-اژ» برای -age فرانسوی (مانندِ گاراژ و ماساژ) خودْ گواهِ میانجیگریِ فرانسه است، چون اگر از انگلیسی می‌آمد صورتی مانندِ *چافیج می‌داشت. معین «شوفاژ» را با نشانِ [فر.] آورده و «گرمایش؛ هر یک از رادیاتورهای سیستم حرارت مرکزی» معنی کرده است؛ یعنی معنا در فارسی از «گرمایش» به «شوفاژ/رادیاتور» تنگ‌تر شده است. ادعای نورایی درست است.\",\n  sources=[\"https://abadis.ir/fatofa/%D8%B4%D9%88%D9%81%D8%A7%DA%98/\"],\n  ref_check=[dict(ref=\"MON:2090,2860\", status=\"partial\", note=\"The six-volume Farhang-e Fārsi is not available as a scan; the entry text is online, and Moʿin's شوفاژ reads '[فر.] (اِ.) ۱- گرمایش. ۲- هر یک از رادیاتورهای سیستم حرارت مرکزی', i.e. the French origin tag Nourai relies on. The page numbers themselves could not be checked.\")],\n  consulted=[\n   dict(src=\"MON\", where=\"Farhang-e Moʿin s.v. شوفاژ, via abadis.ir\", stance=\"supports\", note=\"'[فر.] گرمایش؛ هر یک از رادیاتورهای سیستم حرارت مرکزی.'\"),\n   dict(src=\"ARY\", where=\"Aryanpur, Farhang-e Rishe-hā\", stance=\"silent\", note=\"grep of ARY_pages.txt for کالری / شوفر / شوفاژ returns nothing; the book treats inherited Indo-European vocabulary, not modern European loans.\")],\n ),\n dict(id=13, lang=\"English\", words=\"calorie, chauffeur\",\n  verdict=\"confirmed\",\n  derivation=\"Both are borrowings of the French words of the previous box, not independent formations. calorie entered English about 1866 as the physical unit, and the dietary 'large calorie' from about 1900; chauffeur is attested in English from 1896, first of the driver of a motor car (the sense 'stoker' never came over). Neither shows any English sound change: they are cited by Watkins in the same list as the Latin etyma ('CALORIC, CALORIE' under Latin calor).\",\n  derivation_fa=\"هر دو وام‌واژه از فرانسویِ جعبهٔ پیشین‌اند نه ساختِ انگلیسی. calorie نزدیکِ سالِ ۱۸۶۶ به‌عنوانِ یکایِ فیزیکی و «کالریِ بزرگِ» خوراکی از حدودِ ۱۹۰۰ وارد انگلیسی شد؛ chauffeur از ۱۸۹۶ در انگلیسی گواهی شده، از همان آغاز به معنیِ رانندهٔ خودرو (معنیِ «آتش‌کار» به انگلیسی نرسید). هیچ دگرگونیِ آواییِ انگلیسی در آن‌ها دیده نمی‌شود و واتکینز نیز آن‌ها را در همان فهرستِ برآمده از calor لاتین می‌آورد. ادعای نورایی درست است.\",\n  sources=[\"https://www.etymonline.com/word/chauffeur\"],\n  ref_check=[dict(ref=\"AHD\", status=\"supports\", note=\"Watkins s.v. kelə-1: '3. Suffixed zero-grade form *kl̥-os- in Latin calor, heat: CALORIC, CALORIE; CALORECEPTOR, CALORIFIC, CALORIMETER, CALORIMETRY.'\")],\n  consulted=[\n   dict(src=\"KLN\", where=\"Klein s.v. calorie (KLN_1966.txt)\", stance=\"supports\", note=\"'calorie, also calory, n., unit of heat. — See calori-' and 'caloric — F. calorique, fr. L. calor, \\\"heat\\\"'.\"),\n   dict(src=\"AHD\", where=\"Watkins 1985 s.v. kelə-1\", stance=\"supports\", note=\"as quoted.\")],\n ),\n dict(id=14, lang=\"Sogdian\", words=\"srd\",\n  verdict=\"confirmed\",\n  derivation=\"Gharib's entry 8945: 'srδ B, M, S — sarδ (srd) ©Av. sarəδa-, OP θard-, Khwar. srδ ©nom. -y; ob. -c''y, -yh; pl. -t … year', with citations from the Vessantara Jātaka, the Ancient Letters and the Christian texts; the derivatives srδ'k 'year', srδ't 'years' and srδm'n follow. Sogdian, being North-East Iranian, keeps the -rd- cluster (written -rδ-) exactly where South-West Persian gives -l- (sāl), so Sogdian srδ and Persian sāl are the same word by two different sound laws. Again Nourai's page number is one off: the entry stands on printed p.362 (the marker '361' falls just before entry 8940), not 361.\",\n  derivation_fa=\"مدخلِ ۸۹۴۵ در فرهنگِ قریب: «srδ (B, M, S)، sarδ، از اوستایی sarəδa-، پارسی باستان θard-، خوارزمی srδ … به معنیِ سال»، با شاهدهایی از وسنتره‌جاتکه و نامه‌های باستانی و متونِ مسیحی، و برساخته‌هایی چون srδ'k و srδ't. سغدی از شاخهٔ شمال‌شرقی است و خوشهٔ -rd- را نگه می‌دارد، درست همان‌جا که فارسیِ جنوب‌غربی -l- می‌دهد؛ پس srδ سغدی و «سال» فارسی یک واژه‌اند با دو قانونِ آواییِ متفاوت. شمارهٔ صفحه در اینجا نیز یک واحد جابه‌جاست: این مدخل در صفحهٔ ۳۶۲ چاپی است نه ۳۶۱. ادعای نورایی درست است.\",\n  sources=[],\n  ref_check=[dict(ref=\"SOD:361\", status=\"partial\", note=\"SOD_pages.txt line ~29545: '8945 srδ B, M, S — sarδ (srd) ©Av. sarəδa-, OP θard-, Khwar. srδ … year. GMS 526; VJ 265, 1408, 1409; TSP p271; SCE 13, 377, 383; … Anc. Lett. 2.6, 21 …' — the content is exactly Nourai's, but the entry falls on printed p.362, not 361.\")],\n  consulted=[\n   dict(src=\"SOD\", where=\"Gharib, Sogdian Dictionary, entry 8945 (p.362)\", stance=\"supports\", note=\"quoted above; Gharib derives it from Av. sarəδa- and OP θard-.\"),\n   dict(src=\"SYN\", where=\"Buck §14.73 YEAR, p.1012\", stance=\"partial\", note=\"Buck lists the Iranian family (Av. sarəd-, OP θard-, NPers. sāl, Osset. särd) but no Sogdian form.\")],\n ),\n]\n\nE1_NODES = [\n dict(id=1, lang=\"Pahlavi\", words=\"kulâf; kurpak\",\n  verdict=\"disputed\",\n  derivation=\"Two words with two very different standings. kulāf is a real, attested Book-Pahlavi word — MacKenzie p.52: 'kulāf [kwl'f | N kulāh] cap, bonnet. ~ak: little cap; calyx' — and its connection with New Persian kolāh was established by Hübschmann (Persische Studien p.88, on Horn no.863): 'Kurd. kulāw verhält sich wohl zu np. kulāh wie kurd. dew \\\"Mund\\\" zu ap. dahan, setzt also ein phl. *kulāf voraus, aus dem np. kulāh entstand wie np. kōh aus phl. kōf \\\"Berg\\\"'. The attachment of that word to PIE *ḱel- 'cover' is Horn's own suggestion (Horn no.863, referring to his KZ 32.582 no.10: 'zu ahd. hulja, hulla \\\"Kopfbedeckung\\\", also zu got. huljan \\\"verhüllen, bedecken\\\", lat. cēlāre, occulere'), and it is plausible but not established — Moʿin's footnote on Borhān p.1671 says flatly 'وجه اشتقاقی آن درست معلوم نیست' ('its etymology is not properly known'), and the Wiktionary entry, citing MacKenzie, gives no Proto-Iranian or PIE ancestor at all. kurpak, by contrast, is a starred form taken from the same page of Hübschmann — but from the sentence in which Hübschmann DENIES the connection Nourai is drawing: 'Np. kulba = kurba \\\"Bude\\\" aus phl. *kurpak = arm. kʿrpak \\\"Werkstatt, Laden, Schenke\\\" …, hat also mit gr. καλύβη nichts zu thun' ('so it has nothing to do with Greek kalúbē'). Nourai has combined Horn's Greek comparison (Horn no.864) with Hübschmann's Pahlavi reconstruction, although the second was expressly framed to refute the first.\",\n  derivation_fa=\"دو واژه با دو سرنوشتِ کاملاً متفاوت. kulāf واژه‌ای گواهی‌شده در پهلویِ کتابی است — مکنزی، ص ۵۲: «kulāf، فارسی نو کلاه، کلاه و عرقچین» — و پیوندِ آن با «کلاه» را هوبشمان در «پژوهش‌های فارسی»، ص ۸۸، استوار کرده است: «کردیِ kulāw نسبت به کلاهِ فارسی همان است که kurd. dew نسبت به dahan پارسی باستان دارد؛ پس پهلویِ *kulāf را پیش‌فرض می‌گیرد که np. kulāh از آن پدید آمده، چنان‌که کوه از kōf پهلوی». اما پیوند دادنِ این واژه به ریشهٔ هندواروپاییِ *ḱel- «پوشاندن» پیشنهادِ خودِ هرن است و پذیرفتنی ولی نااستوار؛ معین در حاشیهٔ برهانِ قاطع، ص ۱۶۷۱، صریح می‌نویسد «وجه اشتقاقی آن درست معلوم نیست». در برابر، kurpak صورتی ستاره‌دار است که نورایی از همان صفحهٔ هوبشمان گرفته، اما دقیقاً از جمله‌ای که هوبشمان در آن همین پیوند را رد می‌کند: «کلبه/کربهٔ فارسی از پهلویِ *kurpak است، برابرِ ارمنیِ kʿrpak، پس با καλύβη یونانی هیچ ربطی ندارد». نورایی سنجشِ یونانیِ هرن را با بازسازیِ پهلویِ هوبشمان درآمیخته، حال آنکه دومی برای ردِّ نخستی نوشته شده بود.\",\n  sources=[W+\"%DA%A9%D9%84%D8%A7%D9%87\", W+\"%DA%A9%D9%84%D8%A8%D9%87\"],\n  ref_check=[\n   dict(ref=\"HRN:192,193\", status=\"partial\", note=\"Horn p.192 no.863: 'kulāh \\\"Mütze\\\"; Helm … Zu ahd. hulja, hulla \\\"Kopfbedeckung\\\", also zu got. huljan \\\"verhüllen, bedecken\\\", lat. cēlāre, occulere (Horn, KZ. 32, 582 No. 10). Das Suffix ist spezifisch iranisch (vergl. kurd. kulāw …)' — supports the root link for kolāh. Horn p.193 no.864: 'kulbe, kurbe \\\"Bude\\\", arab. LW. kurbaǧ, kurbaq, kulbat. Nöldeke (mündliche Mitteilung) vergleicht gr. καλύβη \\\"Hütte, Laube\\\". Dies zu καλύπτω' — this is where Nourai's Greek 'kolba' comes from, but Horn has no Pahlavi *kurpak here.\"),\n   dict(ref=\"HUB:88\", status=\"contradicts\", note=\"Hübschmann, Persische Studien p.88 (HUB.txt leaf 99), ad Horn 864: 'Np. kulba = kurba \\\"Bude\\\" aus phl. *kurpak = arm. kʿrpak \\\"Werkstatt, Laden, Schenke\\\", Apg. 28, 15 u. s. w., hat also mit gr. καλύβη nichts zu thun.' The source of Nourai's *kurpak explicitly denies the connection Nourai draws. On the same page, ad Horn 863, Hübschmann does supply the *kulāf that Nourai's first word rests on.\")],\n  consulted=[\n   dict(src=\"PHD\", where=\"MacKenzie, Concise Pahlavi Dictionary p.52 s.v. kulāf (PHD.txt line 430)\", stance=\"supports\", note=\"'kulāf [kwl'f | N kulāh] cap, bonnet. ~ak [-k'] | N ~hak] little cap; calyx.' No entry *kurpak (MacKenzie has the New Persian side only).\"),\n   dict(src=\"HUB\", where=\"Persische Studien p.88\", stance=\"partial\", note=\"supplies *kulāf (supports word 1) and refutes the Greek connection of *kurpak (contradicts word 2).\"),\n   dict(src=\"BQT\", where=\"Borhān-e Qāṭeʿ ed. Moʿin p.1673, footnote 5 on کلبه\", stance=\"supports\", note=\"'* کربه. از پهلوی kurpak > ارمنی kʿrpak (کارخانه، دکان، میخانه) «هوبشمان ۸۹۴»، معرّب آن کربق، قربق … و نیز کربج، کلبة' — Moʿin accepts the Pahlavi *kurpak, but as an Armenian-linked word, with no Greek or Indo-European root.\")],\n ),\n dict(id=2, lang=\"Persian\", words=\"kolâh «کلاه»; kolbeh «کلبه ( کلبک )»\",\n  verdict=\"disputed\",\n  derivation=\"کلاه kolāh from Middle Persian kulāf is uncontroversial as a sound change — Old/Middle Persian final -f becomes New Persian -h exactly as in MP kōf > NP کوه kōh 'mountain' (Hübschmann's own parallel) — and Wiktionary, citing MacKenzie, gives just that. Its further attachment to *ḱel- 'to cover' is Horn's conjecture; Moʿin (Borhān p.1671 n.10) says the etymology is unknown and only compares Kurdish kulāw and Pahlavi kulāf, and Wiktionary offers no Proto-Iranian form. کلبه kolbeh, however, does not belong here at all in the modern view. Its Middle Persian ancestor is kurbag 'humble dwelling, hut', a derivative of MP kirb 'body, form' (Avestan kəhrp-, hu-kərəpta- 'well-formed', Proto-Iranian *kr̥p-, PIE *krep- 'body'); Wiktionary, citing Bartholomae, states expressly that it is 'unrelated to Ancient Greek καλύβη (kalúbē)'. The Arabic forms كُرْبَق kurbaq / قُرْبَق qurbaq / كُرْبَج kurbaj, and the Armenian kʿrpak that Hübschmann and Moʿin adduce, all point to a -p- in the second syllable, which καλύβη cannot supply. So the first word is plausible and the second is misassigned; the node takes the worse verdict.\",\n  derivation_fa=\"«کلاه» از kulāf فارسی میانه از نظرِ آوایی بی‌چون‌وچراست: -f پایانی در فارسی نو به -ه بدل می‌شود، درست همان‌گونه که kōf پهلوی «کوه» شده است (همین سنجش را هوبشمان آورده). اما پیوند دادنِ آن به ریشهٔ *ḱel- «پوشاندن» گمانهٔ هرن است؛ معین در حاشیهٔ برهان، ص ۱۶۷۱، می‌نویسد وجهِ اشتقاقی‌اش روشن نیست و تنها کردیِ kulāw و پهلویِ kulāf را می‌سنجد، و ویکی‌واژه نیز هیچ صورتِ ایرانیِ آغازین برای آن نمی‌دهد. اما «کلبه» از دیدِ پژوهشِ امروزی اصلاً به این ریشه تعلق ندارد: نیای فارسیِ میانهٔ آن kurbag «خانهٔ محقر، کلبه» است، برساختهٔ kirb «تن، پیکر» (اوستایی kəhrp-، hu-kərəpta- «خوش‌پیکر»، ایرانیِ آغازینِ *kr̥p-، هندواروپاییِ *krep- «تن»)؛ ویکی‌واژه به‌استنادِ بارتولومه صریح می‌گوید که «با καλύβη یونانی بی‌ارتباط است». صورت‌های عربیِ کُربَق و قُربَق و کُربَج و ارمنیِ kʿrpak همه بر -پ- در هجای دوم گواهی می‌دهند که καλύβη نمی‌تواند آن را توضیح دهد. پس واژهٔ نخست با احتیاط پذیرفتنی است و واژهٔ دوم نادرست جای گرفته؛ داوریِ گره همان داوریِ بدتر است.\",\n  sources=[W+\"%DA%A9%D9%84%D8%A8%D9%87\", W+\"%DA%A9%D9%84%D8%A7%D9%87\"],\n  ref_check=[\n   dict(ref=\"BQT:1671,1673\", status=\"partial\", note=\"Borhān-e Qāṭeʿ ed. Moʿin p.1671 (کلاه) with footnote 10: 'وجه اشتقاقی آن درست معلوم نیست. قس: کردی kulāw، پهلوی kulāf «هوبشمان ۸۹۳»' — the Pahlavi form yes, the Indo-European root no. p.1673 (کلبه) footnote 5: '* کربه. از پهلوی kurpak > ارمنی kʿrpak … معرّب آن کربق، قربق … و نیز کربج، کلبة' — Pahlavi kurpak yes, but no root. Both page numbers are exact (verified by rendering the pages with tools/ref_page.py).\"),\n   dict(ref=\"PLA:233\", status=\"supports\", note=\"Asbaghi, Persische Lehnwörter im Arabischen p.233 (PLA_pages.txt line 13081, running head 'kāsnī … 233 … kalam'): 'kulbak: \\\"Hütte, Zelle, Keller\\\" < pers. kolbe < mp. kurpak; s. qarbaq, karbag u. karbaq.' Supports the Pahlavi kurpak > Persian kolbe > Arabic kulbak chain; for kolāh Asbaghi's entry (Ar. qulla < pers. kulāh 'Mütze') is on p.~226, not 233.\")],\n  consulted=[\n   dict(src=\"BQT\", where=\"Borhān ed. Moʿin pp.1671, 1673 (pages rendered with tools/ref_page.py)\", stance=\"partial\", note=\"as quoted; Moʿin supports both Middle Persian antecedents and denies any settled deeper etymology for kolāh.\"),\n   dict(src=\"PLA\", where=\"Asbaghi p.233\", stance=\"supports\", note=\"'kulbak … < pers. kolbe < mp. kurpak'.\"),\n   dict(src=\"HRN\", where=\"Horn nos. 863, 864 (pp.192-193)\", stance=\"partial\", note=\"Horn is the only source that attaches kolāh to the *ḱel- family (via Gothic huljan, Latin cēlāre) and that compares kolbe with Greek καλύβη; Hübschmann rejected the latter a year later.\"),\n   dict(src=\"HUB\", where=\"Persische Studien p.88\", stance=\"contradicts\", note=\"'hat also mit gr. καλύβη nichts zu thun'.\")],\n ),\n dict(id=3, lang=\"Greek\", words=\"kaluptein; kolba\",\n  verdict=\"transcription_suspect\",\n  error_in=\"book\", book_prints=\"kolba : shelter, hut\", correct_form=\"kaluba (καλύβη kalúbē)\",\n  derivation=\"καλύπτω / infinitive καλύπτειν 'to cover, conceal' is exactly right: it is the labial extension *ḱel-up- of the root (Pokorny 553 'mit Labialerweiterung καλύπτω \\\"umhülle, verberge\\\"'; Watkins 'Suffixed variant form *kal-up-yo- in Greek kaluptein, to cover, conceal: CALYPSO, CALYPTRA; APOCALYPSE, EUCALYPTUS'). The second word, printed 'kolba', is not a Greek word. What Nourai means is καλύβη kalúbē 'hut, cabin, arbour', the noun built on the same *kal-up- extension — and this is certain, because Buck's page 460, which Nourai cites in this very box, opens §7.13 HUT with 'Grk. καλύβη fr. the stem of καλύπτω \\\"cover\\\", also καλιά and Skt. śālā- \\\"house, stall, hut\\\" fr. the same root, IE *ḱel- \\\"cover, hide\\\" in Lat. occulere, cēlāre, Ir. celim, OE helan'. The high-resolution scan of the printed page (pdf 250) shows 'kolba : shelter, hut', so the extraction is faithful and the corruption is the book's: -o- for -a-, -b- for -β-, and the loss of the ending have left the word unrecognisable.\",\n  derivation_fa=\"καλύπτω / مصدرِ καλύπτειν «پوشاندن، پنهان کردن» کاملاً درست است: گسترشِ لبیِ ریشه است (*ḱel-up-)، چنان‌که پوکورنی در ص ۵۵۳ می‌نویسد «با گسترشِ لبی καλύπτω \\\"می‌پوشانم، پنهان می‌کنم\\\"» و واتکینز نیز آن را با apocalypse و eucalyptus یک‌جا می‌آورد. اما واژهٔ دوم، که «kolba» چاپ شده، واژه‌ای یونانی نیست. مقصودِ نورایی καλύβη «کلبه، آلاچیق» است، اسمی از همان ستاکِ *kal-up-؛ و این را با یقین می‌توان گفت، چون صفحهٔ ۴۶۰ باک — که نورایی خودْ در همین جعبه به آن ارجاع داده — بندِ ۷٫۱۳ «کلبه» را چنین می‌آغازد: «یونانی καλύβη از ستاکِ καλύπτω \\\"پوشاندن\\\"، و نیز καλιά و سنسکریت śālā- … از همان ریشه، هندواروپاییِ *ḱel- \\\"پوشاندن، پنهان کردن\\\"». تصویرِ پرحجمِ صفحهٔ چاپی نشان می‌دهد که کتاب خودْ «kolba» چاپ کرده است؛ پس خطای چاپیِ کتاب است نه خطای خوانشِ اسکن: ـُ به‌جای ـَ، b به‌جای β، و افتادنِ پایانه واژه را ناشناختنی کرده است.\",\n  sources=[W+\"Reconstruction:Proto-Indo-European/%E1%B8%B1el-\"],\n  ref_check=[\n   dict(ref=\"AHD\", status=\"partial\", note=\"Watkins s.v. kel-2 'To cover, conceal, save' (AHD_watkins1985.txt line 603): '5. Suffixed variant form *kal-up-yo- in Greek kaluptein, to cover, conceal: CALYPSO, CALYPTRA; APOCALYPSE, EUCALYPTUS.' Supports kaluptein; Watkins has no καλύβη.\"),\n   dict(ref=\"SYN:460\", status=\"supports\", note=\"Buck §7.13 HUT, p.460 (SYN.txt line 11562 ff.): '1. Grk. καλύβη fr. the stem of καλύπτω \\\"cover\\\", also καλιά and Skt. śālā- \\\"house, stall, hut\\\" fr. the same root, IE *ḱel- \\\"cover, hide\\\" in Lat. occulere, cēlāre, Ir. celim, OE helan, etc. Walde-P. 1.432 ff. NG καλύβα is, through Turk., the source of SCr. koliba, Rum. colibă.' — Nourai's own reference gives the correct form of the word he misprints.\")],\n  consulted=[\n   dict(src=\"POK\", where=\"Pokorny 553-554 s.v. ḱel-4 'to conceal' (POK_full.txt line 49947)\", stance=\"supports\", note=\"'gr. καλιά \\\"cottage, barn, nest\\\" … with labial extension καλύπτω \\\"wrap, hide\\\", καλύβη \\\"hideout, cottage\\\", κέλυφος n. \\\"bowl, husk\\\".'\"),\n   dict(src=\"WLD\", where=\"Walde-Pokorny I 432 (WLD_Bd1_pages.txt leaf 440)\", stance=\"supports\", note=\"'mit Labialerw. καλύπτω „umhülle, verberge“, καλύβη „Obdach, Hütte“ (reimt mit κρύπτω …)'.\"),\n   dict(src=\"SYN\", where=\"Buck p.460\", stance=\"supports\", note=\"as quoted; the misprinted word is καλύβη.\")],\n ),\n dict(id=4, lang=\"Latin\", words=\"eu-caliptus\",\n  verdict=\"plausible\",\n  derivation=\"The word is right in substance but is not a Latin word of antiquity and is not spelt as printed. Eucalyptus is a New Latin (botanical) genus name coined in 1788 by the French botanist Charles Louis L'Héritier de Brutelle from Greek εὖ eu 'well' + καλυπτός kalyptós 'covered' (verbal adjective of καλύπτειν), because the flower bud of the tree is capped by an operculum — a lid that covers the whole flower until it is shed at anthesis. So Nourai's gloss 'a plant with \\\"well covered\\\" flowers' and his cross-reference ☞Su 1 for the first element (PIE *h₁su- 'good, well') are both correct, and the box's position under kaluptein is correct. What is wrong is the form: the printed page has 'eu-caliptus', with i for y; the botanical name has always been Eucalyptus. And a New Latin coinage of 1788 is not a descendant of Greek in the way the arrow suggests — it is a deliberate modern compound made from Greek elements.\",\n  derivation_fa=\"مضمونِ جعبه درست است، اما این واژه نه لاتینِ باستان است و نه به این املا. Eucalyptus نامِ سرده‌ای است در لاتینِ نو (لاتینِ گیاه‌شناسی) که در سالِ ۱۷۸۸ شارل لویی لِریتیه دو بروتل، گیاه‌شناسِ فرانسوی، از یونانیِ εὖ «خوب» و καλυπτός «پوشیده» (صفتِ مفعولیِ καλύπτειν) ساخت، زیرا غنچهٔ این درخت را سرپوشی (operculum) می‌پوشاند که تا هنگامِ شکفتن نمی‌افتد. پس هم معنایی که نورایی داده («گیاهی با گل‌های خوب‌پوشیده») و هم ارجاعِ او به ریشهٔ Su 1 برای جزءِ نخست درست است و جای جعبه نیز زیرِ kaluptein درست است. آنچه نادرست است صورتِ واژه است: صفحهٔ چاپی «eu-caliptus» دارد با i به‌جای y، حال آنکه نامِ گیاه‌شناختی همواره Eucalyptus بوده است. افزون بر این، برساخته‌ای از سالِ ۱۷۸۸ به آن معنا فرزندِ یونانی نیست که پیکان می‌نمایاند، بلکه ترکیبی است آگاهانه و نوساخته از عناصرِ یونانی.\",\n  sources=[\"https://www.etymonline.com/word/eucalyptus\"],\n  ref_check=[dict(ref=\"AHD\", status=\"supports\", note=\"Watkins s.v. kel-2, under '*kal-up-yo- in Greek kaluptein', lists 'EUCALYPTUS' among the English words derived from it.\")],\n  consulted=[\n   dict(src=\"KLN\", where=\"Klein, Comprehensive Etymological Dictionary s.v. cell (KLN_1966.txt)\", stance=\"supports\", note=\"'Cp. also caliology, calyptra, cilia, clandestine, color, conceal, dharmsala, Eucalyptus, hall, hell, helmet, holster, hull, kalidium, kelyphite, kil-, occult, superciliary, Valhalla' — Klein's own list under Latin cella/cēlāre is almost exactly the set of words on this chart.\"),\n   dict(src=\"WEB\", where=\"Etymonline s.v. eucalyptus (standing in for the English dictionaries)\", stance=\"supports\", note=\"'coined 1788 by French botanist Charles Louis L'héritier de Brutelle from Greek eu \\\"well\\\" + kalyptos \\\"covered\\\", in reference to the covering on the bud.'\")],\n ),\n dict(id=5, lang=\"Persian\", words=\"okâlîptûs «اکالیپتوس»\",\n  verdict=\"confirmed\",\n  derivation=\"اکالیپتوس okālīptūs is the scientific name taken into Persian in the twentieth century together with the tree, which was introduced into Iran as a plantation and avenue species. The Persian shape shows the French/Latin pronunciation with -tūs, not the English -tus [-təs], and prosthesis is not needed because Persian tolerates initial vowel + consonant here; the Persian rendering of the Greek υ as ی reflects the modern European value [i]. Moʿin's Farhang tags it '[لا.]' — Latin — and defines it 'درختی از تیرهٔ موردیها، همیشه سبز با برگهای دراز و نوک تیز مانند بید', which is exactly the transmission Nourai draws (New Latin > Persian).\",\n  derivation_fa=\"«اکالیپتوس» نامِ علمیِ گیاه است که در سدهٔ بیستم همراهِ خودِ درخت — که برای جنگل‌کاری و درخت‌کاریِ خیابانی به ایران آورده شد — وارد فارسی شده است. صورتِ فارسی تلفظِ فرانسوی/لاتینی را نشان می‌دهد (پایانهٔ -توس، نه -تِس انگلیسی) و υ یونانی در آن به «ی» بدل شده که ارزشِ اروپاییِ امروزیِ آن است. معین آن را با نشانِ [لا.] یعنی لاتینی آورده و چنین معنی کرده است: «درختی از تیرهٔ موردیها، همیشه سبز با برگهای دراز و نوک تیز مانند بید» — یعنی درست همان راهی که نورایی ترسیم کرده است. ادعای نورایی درست است.\",\n  sources=[\"https://abadis.ir/fatofa/%D8%A7%DA%A9%D8%A7%D9%84%DB%8C%D9%BE%D8%AA%D9%88%D8%B3/\"],\n  ref_check=[dict(ref=\"MON:404\", status=\"partial\", note=\"The six-volume Farhang-e Fārsi is not available as a scan, so the page number could not be verified; the entry text is online and reads '(اُ) [لا.] (اِ.) درختی از تیرهٔ موردیها، همیشه سبز با برگهای دراز و نوک تیز مانند بید …', i.e. Moʿin does tag the word Latin as Nourai's arrow requires.\")],\n  consulted=[\n   dict(src=\"MON\", where=\"Farhang-e Moʿin s.v. اکالیپتوس, via abadis.ir\", stance=\"supports\", note=\"'[لا.]' origin tag.\"),\n   dict(src=\"WEB\", where=\"Etymonline s.v. eucalyptus\", stance=\"supports\", note=\"gives the 1788 New Latin coinage from which the Persian, like every other modern language's form, is taken.\")],\n ),\n dict(id=6, lang=\"English\", words=\"eucalyptus\",\n  verdict=\"confirmed\",\n  derivation=\"English eucalyptus is simply the New Latin genus name used as a common noun; it is recorded in English from 1809, a generation after L'Héritier's coinage of 1788, and keeps the Latin spelling and the Latin plural eucalypti beside the English eucalyptuses. Klein files it, with hall, hell, helmet, color and conceal, among the English words that go back to the root of Latin cella and cēlāre, and Watkins lists EUCALYPTUS under Greek kaluptein in kel-2 — precisely the position Nourai gives it.\",\n  derivation_fa=\"واژهٔ انگلیسیِ eucalyptus همان نامِ سردهٔ لاتینِ نو است که به‌عنوانِ اسمِ عام به کار رفته؛ از سالِ ۱۸۰۹ در انگلیسی گواهی شده، یعنی یک نسل پس از برساختِ لِریتیه در ۱۷۸۸، و املا و حتی جمعِ لاتینیِ eucalypti را در کنارِ جمعِ انگلیسی نگه داشته است. کلاین آن را در کنارِ hall و hell و helmet و color و conceal در شمارِ واژه‌های انگلیسیِ برآمده از ریشهٔ cella و cēlāre لاتین می‌آورد، و واتکینز نیز EUCALYPTUS را ذیلِ kaluptein یونانی در ریشهٔ kel-2 فهرست کرده است — درست همان جایی که نورایی به آن داده است. ادعای نورایی درست است.\",\n  sources=[\"https://www.etymonline.com/word/eucalyptus\"],\n  ref_check=[dict(ref=\"None\", status=\"not_checked\", note=\"Nourai gives no reference for this box.\")],\n  consulted=[\n   dict(src=\"KLN\", where=\"Klein s.v. cell\", stance=\"supports\", note=\"'Cp. also … Eucalyptus, hall, hell, helmet, holster, hull, … occult, superciliary, Valhalla.'\"),\n   dict(src=\"AHD\", where=\"Watkins 1985 s.v. kel-2\", stance=\"supports\", note=\"'APOCALYPSE, EUCALYPTUS' under Greek kaluptein.\"),\n   dict(src=\"WEB\", where=\"Etymonline s.v. eucalyptus\", stance=\"supports\", note=\"the 1788 coinage and the reason for the name.\")],\n ),\n dict(id=7, lang=\"Germanic\", words=\"hallô; helmaz\",\n  verdict=\"confirmed\",\n  derivation=\"Both are standard Proto-Germanic reconstructions and both are in Watkins's article under this root: '*hallō, covered place, hall, in a. Old English heall, hall: HALL; b. Old Norse höll, hall: VALHALLA' (from the o-grade *ḱol-nā-, with the Germanic assimilation -ln- > -ll-), and '*helmaz, \\\"protective covering\\\", in a. Old English helm, protection, covering: HELM; b. Frankish *helm, helmet' (full grade *ḱel-mo-, the exact match of Sanskrit śárman- 'shelter, protective roof, cover', as Pokorny notes: 'śarman- n. \\\"shelter, protective roof, cover, guarding\\\" (: Modern High German Helm)'). Nourai's glosses 'covered place' and 'head cover' are Watkins's own wording.\",\n  derivation_fa=\"هر دو صورت بازسازی‌های استانداردِ ژرمنیِ آغازین‌اند و هر دو در مقالهٔ واتکینز ذیلِ همین ریشه آمده‌اند: «*hallō \\\"جای پوشیده، تالار\\\"، در انگلیسیِ کهن heall و نُرسیِ کهن höll (والهالا)» — از درجهٔ o یعنی *ḱol-nā- با همگونیِ ژرمنیِ -ln- ← -ll- — و «*helmaz \\\"پوششِ نگهدارنده\\\"، در انگلیسیِ کهن helm و فرانکیِ *helm \\\"کلاهخود\\\"» از *ḱel-mo- که برابرِ دقیقِ سنسکریت śárman- «سرپناه، پوشش» است، چنان‌که پوکورنی خودْ آن را با Helm آلمانی می‌سنجد. حتی معناهایی که نورایی نوشته («جای پوشیده»، «پوششِ سر») عینِ عبارتِ واتکینز است. ادعای نورایی درست است.\",\n  sources=[W+\"Reconstruction:Proto-Indo-European/%E1%B8%B1el-\"],\n  ref_check=[dict(ref=\"AHD\", status=\"supports\", note=\"Watkins s.v. kel-2: 'I. O-grade form *kol-. … 2. Germanic *hallō, covered place, hall, in: a. Old English heall, hall: HALL; b. Old Norse höll, hall: VALHALLA. … III. Full-grade form *kel-. 1. Germanic *helmaz, \\\"protective covering\\\", in: a. Old English helm …: HELM; b. Frankish *helm, helmet … HELMET.'\")],\n  consulted=[\n   dict(src=\"POK\", where=\"Pokorny 553-554\", stance=\"supports\", note=\"'Old High German Old Saxon halla, Old English heall \\\"hall\\\", Old Norse höll f. \\\"big house\\\" (*ḱolnā)'; 'Gothic hilms, Old High German Old Saxon Old English helm \\\"helmet\\\" … (: Old Indic śarman-)'.\"),\n   dict(src=\"WLD\", where=\"Walde-Pokorny I 432-433 (leaf 440-441)\", stance=\"supports\", note=\"'śarman- n. „Schirm, Schutzdach, Decke, Obhut“ (: dt. Helm)'.\"),\n   dict(src=\"KLN\", where=\"Klein s.v. cell\", stance=\"supports\", note=\"lists hall, hell, helmet among the cognates.\")],\n ),\n dict(id=8, lang=\"English\", words=\"hall, hell, hole, hollow; helmet\",\n  verdict=\"confirmed\",\n  derivation=\"All five words descend from this root, but by three different Germanic preforms, only two of which the chart's Germanic box names. hall is OE heall < *hallō (o-grade *ḱol-nā-). hell is OE hell < Proto-Germanic *haljō 'the concealed place' (o-grade *ḱol-yā-), the same word as Old Norse Hel, the death-goddess. hole and hollow are OE hol 'a hollow' and holh 'hole, hollow' < the zero-grade *hul- (*ḱl̥-), the group that also gives OE hulu 'husk' > hull. helmet is not native English but Middle English helmet borrowed from Old French helmet, a diminutive of Frankish *helm, itself the Germanic *helmaz of the previous box — so the English word comes back into English from Germanic by way of French. Klein's article on cell lists 'color, conceal, dharmsala, Eucalyptus, hall, hell, helmet, holster, hull' together, and Watkins has all of them under kel-2, so the box is right; only the intermediate Germanic box is abridged.\",\n  derivation_fa=\"هر پنج واژه از این ریشه‌اند، اما از سه صورتِ ژرمنیِ متفاوت که جعبهٔ ژرمنیِ نمودار تنها دوتای آن‌ها را نام برده است. hall از انگلیسیِ کهنِ heall و آن از *hallō (درجهٔ o، *ḱol-nā-). hell از انگلیسیِ کهنِ hell و آن از ژرمنیِ *haljō «جای پنهان» (*ḱol-yā-)، همان واژه‌ای که در نُرسیِ کهن نامِ ایزدبانوی مرگ Hel است. hole و hollow از انگلیسیِ کهنِ hol و holh و آن‌ها از درجهٔ صفرِ *hul- (*ḱl̥-) که hull «پوست، غلاف» نیز از آن است. اما helmet واژه‌ای موروثی نیست: انگلیسیِ میانه آن را از فرانسویِ کهنِ helmet وام گرفته که خودْ مصغرِ فرانکیِ *helm است، یعنی همان *helmaz جعبهٔ پیشین — پس این واژه از راهِ فرانسه به انگلیسی بازگشته است. کلاین در مقالهٔ cell همهٔ این‌ها را یک‌جا می‌آورد و واتکینز نیز همه را ذیلِ kel-2 دارد؛ پس جعبه درست است و تنها جعبهٔ میانیِ ژرمنی کوتاه‌شده است. ادعای نورایی درست است.\",\n  sources=[W+\"Reconstruction:Proto-Indo-European/%E1%B8%B1el-\"],\n  ref_check=[dict(ref=\"None\", status=\"not_checked\", note=\"Nourai gives no reference for this box; the parent Germanic box cites AHD, which covers all five words.\")],\n  consulted=[\n   dict(src=\"AHD\", where=\"Watkins 1985 s.v. kel-2 (AHD_watkins1985.txt lines 603-606)\", stance=\"supports\", note=\"'Germanic *haljō, the underworld (< \\\"concealed place\\\"), in: a. Old English hell, hell: HELL … 2. Germanic *hallō … HALL … II. Zero-grade form *kl̥-. 1. Germanic *hul- in: a. Old English hulu, husk, pod: HULL; b. Old English hol, a hollow: HOLE; c. Old English holh, hole, hollow: HOLLOW … b. Frankish *helm, helmet, akin to the source of Middle English helmet: HELMET.'\"),\n   dict(src=\"KLN\", where=\"Klein s.v. cell\", stance=\"supports\", note=\"'Cp. also … hall, hell, helmet, holster, hull …'\"),\n   dict(src=\"SKT\", where=\"Skeat, Concise Etymological Dictionary (SKT.txt)\", stance=\"partial\", note=\"the OCR is badly damaged, but the surviving cross-references 'Conceal; see Cell.' and 'Hollow; see Hole.' show Skeat grouping the same family.\")],\n ),\n dict(id=9, lang=\"Latin\", words=\"color; cĕlâre\",\n  verdict=\"confirmed\",\n  derivation=\"Latin color, colōris 'colour, hue' is an old -os-/-es- stem, *ḱel-os- 'a covering', archaic colōs, and the semantic step is exactly the one Nourai gives: 'that which covers' (the outward appearance, the surface) > 'colour'; Pokorny writes 'color, -ōris \\\"paint, colour\\\" (arch. colōs, actually \\\"sleeve, wrapping, external side\\\")'. cēlāre 'to hide' is the lengthened-grade denominative *ḱēl-ā- beside *celō (= Old Irish celim, Old High German helan); it survives in Latin occulō, occultus and in the borrowed English conceal. The one small blemish is the printed diacritic: the book prints 'cĕlâre' with a breve, but the vowel is long, cēlāre — precisely the lengthened grade on which the whole formation depends (Watkins: 'IV. Lengthened-grade form *kēl-ā- in Latin cēlāre, to hide: CONCEAL').\",\n  derivation_fa=\"color لاتینی از ستاکِ کهنِ -os/-es است، یعنی *ḱel-os- «پوشش»، با صورتِ کهنِ colōs؛ و گذارِ معنایی دقیقاً همان است که نورایی نوشته: «آنچه می‌پوشاند» (نمایِ بیرونی، رویه) ← «رنگ». پوکورنی می‌نویسد «color, -ōris \\\"رنگ\\\" (کهن colōs، در اصل \\\"پوشش، رویهٔ بیرونی\\\")». cēlāre «پنهان کردن» فعلی است بر پایهٔ درجهٔ کشیدهٔ *ḱēl-ā- در کنارِ *celō (برابرِ ایرلندیِ کهن celim و آلمانیِ علیای کهن helan) و در occulō و occultus لاتین و در conceal انگلیسی بازمانده است. تنها لغزشِ کوچک نشانهٔ روی واکه است: کتاب «cĕlâre» با نشانهٔ کوتاهی چاپ کرده، حال آنکه واکه کشیده است (cēlāre) و همین کشیدگی است که کلِّ ساخت بر آن استوار است — واتکینز: «صورتِ درجهٔ کشیدهٔ *kēl-ā- در cēlāre لاتین». ادعای نورایی درست است.\",\n  sources=[W+\"Reconstruction:Proto-Indo-European/%E1%B8%B1el-\"],\n  ref_check=[dict(ref=\"AHD\", status=\"supports\", note=\"Watkins s.v. kel-2: 'III. Full-grade form *kel-. … 3. Suffixed form *kel-os- in Latin color, color, hue (< \\\"that which covers\\\"): COLOR. … IV. Lengthened-grade form *kēl-ā- in Latin cēlāre, to hide: CONCEAL.'\")],\n  consulted=[\n   dict(src=\"POK\", where=\"Pokorny 553 (POK_full.txt line 49952)\", stance=\"supports\", note=\"'Latin *celō (= Old Irish celim, Old High German helan) in occulo, -ere \\\"conceal\\\"; color, -ōris \\\"paint, color\\\" (arch. colōs, actually \\\"sleeve, wrapping, external side\\\"); lengthened grade cēlō, -āre \\\"hide, conceal\\\", nominal cella \\\"storeroom, chamber, cell\\\".'\"),\n   dict(src=\"WLD\", where=\"Walde-Pokorny I 433 (leaf 441)\", stance=\"supports\", note=\"'auf einem alten -es-St. (s. lat. color) beruhen hingegen wohl mhd. hulst f. „Decke, Hülle“ …'\"),\n   dict(src=\"KLN\", where=\"Klein s.v. cell\", stance=\"supports\", note=\"'L. cella … cēlāre, \\\"to hide, keep secret\\\" … Cp. also … color, conceal …'\")],\n ),\n dict(id=10, lang=\"English\", words=\"color, conceal\",\n  verdict=\"confirmed\",\n  derivation=\"Neither is a native English word: both were taken from French in the Middle English period. color/colour is Middle English colour from Anglo-French colur, Old French color/colur, from Latin colōrem (accusative of color); the American spelling color restores the Latin form. conceal is Middle English concelen from Old French conceler, from Latin concēlāre 'to hide completely' (com- intensive + cēlāre). Skeat's dictionary still handles the second by a bare cross-reference — 'Conceal; see Cell' — putting it in the same article as cella and cēlāre, and Klein and Watkins do the same, so the box is exactly where the reference works put these words.\",\n  derivation_fa=\"هیچ‌یک از این دو واژه انگلیسیِ موروثی نیست؛ هر دو در دورهٔ انگلیسیِ میانه از فرانسه وام گرفته شده‌اند. colour/color از انگلیسیِ میانهٔ colour، از انگلونورمنِ colur و فرانسویِ کهنِ color، از حالتِ مفعولیِ لاتینِ colōrem؛ املای آمریکاییِ color صورتِ لاتینی را بازگردانده است. conceal از انگلیسیِ میانهٔ concelen، از فرانسویِ کهنِ conceler، از لاتینِ concēlāre «یکسره پنهان کردن» (پیشوندِ تأکیدیِ com- + cēlāre). اسکیت هنوز واژهٔ دوم را تنها با ارجاعِ «Conceal؛ نگاه کنید به Cell» می‌گذراند، یعنی آن را در همان مقالهٔ cella و cēlāre می‌نهد، و کلاین و واتکینز نیز چنین می‌کنند. پس جای این جعبه دقیقاً همان است که فرهنگ‌های مرجع به آن داده‌اند. ادعای نورایی درست است.\",\n  sources=[W+\"Reconstruction:Proto-Indo-European/%E1%B8%B1el-\"],\n  ref_check=[dict(ref=\"None\", status=\"not_checked\", note=\"Nourai gives no reference for this box; the parent Latin box cites AHD, which covers both words (COLOR, CONCEAL).\")],\n  consulted=[\n   dict(src=\"AHD\", where=\"Watkins 1985 s.v. kel-2\", stance=\"supports\", note=\"'*kel-os- in Latin color … : COLOR' and '*kēl-ā- in Latin cēlāre, to hide: CONCEAL.'\"),\n   dict(src=\"SKT\", where=\"Skeat, Concise Etymological Dictionary s.v. Conceal (SKT.txt)\", stance=\"supports\", note=\"'Conceal; see Cell.'\"),\n   dict(src=\"KLN\", where=\"Klein s.v. cell\", stance=\"supports\", note=\"'Cp. also … color, conceal …'\")],\n ),\n]\n\ndoc = dict(\n pdf_page=250, book_page=220,\n verified_by=\"claude-opus-5\", verified_on=\"2026-09-06\",\n entries=[\n  dict(entry=0, root=\"Kel 1\", verdict=\"confirmed\",\n   modern_form=\"PIE *ḱel- / *ḱelH- (Pokorny 'ḱel-1: 1. \\\"frieren, kalt\\\", 2. \\\"warm\\\"', pp. 551-552); modern handbooks split it into *ḱelH- 'to freeze' (LIV 323, Cheung *sarH1) and *ḱelh₁- 'to warm', the latter yielding Proto-Iranian *carHdáh 'autumn, year'\",\n   note=\"The root box is right in every particular, and it is right because it reproduces Pokorny. Pokorny's article on p.551 is headed '1. ḱel- 1. \\\"frieren, kalt\\\", 2. \\\"warm\\\" (Bedeutungsvermittlung wohl \\\"brennend\\\")' — so Nourai's gloss 'cold, also warm, warm season, a year' and his note 'This root has two opposing meanings' are Pokorny's own heading and Pokorny's own remark that the bridge between the two senses is probably 'burning'. Section 1 of that article contains Av. sarəta-, np. sard, av. sarə-δā-; section 2 contains Skt. śarád- 'autumn, (with numerals) year', av. sarəd- f. 'Jahr', osset. särd 'Sommer', np. sāl 'Jahr' ('\\\"Herbst\\\" als \\\"warme Zeit\\\"'), and then Lat. caleō, calidus, calor. Every branch of this chart except the Sogdian forms and the modern French/Persian/English loans stands in those two columns of Pokorny, and Buck's two articles §15.86 COLD (p.1078) and §14.73 YEAR (p.1012) — Nourai's other two citations — supply the same material with the same explanation ('perh. as orig. \\\"warm season\\\"'). Modern scholarship has separated what Pokorny joined: LIV and Cheung set up *ḱelH- 'to freeze' for the 'cold' family (Cheung's *sarH1, with Av. sarəta-, MP sard, Sogd. srt, NP sard, afsurdan), while Wiktionary and NIL derive the 'year' family from *ḱelh₁- 'to warm up' via Proto-Indo-Iranian *ćarHáts, and Watkins keeps only 'kelə-1. Warm' at Pok. 551, with no 'cold' entry at all. So Nourai's single box with 'two opposing meanings' is a faithful report of the 1959 standard rather than of the present one — which is worth saying, because the chart's real claim, that Persian سرد and Persian سال are ultimately the same root, is exactly the claim that the modern split calls into question. Within the chart, three boxes need qualifying: the Avestan 'sarez' of node 5 (a misprint), the Pahlavi 'sālak' of node 6 (which means '-year-old', not 'year'), and the unattested Old Persian 'upa-sard' of node 8.\",\n   note_fa=\"جعبهٔ ریشه از هر جهت درست است، و درست است چون عیناً بازتابِ پوکورنی است. مقالهٔ پوکورنی در صفحهٔ ۵۵۱ چنین عنوان دارد: «۱. ḱel- ۱. \\\"یخ زدن، سرد\\\"، ۲. \\\"گرم\\\" (پیوندِ معنایی گویا از راهِ \\\"سوزان\\\")» — پس هم معنایی که نورایی داده («سرد، و نیز گرم، فصلِ گرم، سال») و هم یادداشتِ او («این ریشه دو معنیِ متضاد دارد») همان عنوان و همان تبصرهٔ پوکورنی است. بندِ نخستِ آن مقاله اوستایی sarəta- و فارسی «سرد» و اوستایی sarə-δā- را دارد و بندِ دوم سنسکریت śarád- «پاییز، (با شمار) سال»، اوستایی sarəd- «سال»، اوستیِ särd «تابستان»، فارسی «سال» («پاییز» به معنیِ «هنگامِ گرم») و سپس لاتینِ caleō و calidus و calor را. جز صورت‌های سغدی و وام‌واژه‌های نوِ فرانسوی و فارسی و انگلیسی، هر شاخهٔ این نمودار در همان دو ستونِ پوکورنی ایستاده است، و دو مقالهٔ باک — بندِ ۱۵٫۸۶ «سرد» در ص ۱۰۷۸ و بندِ ۱۴٫۷۳ «سال» در ص ۱۰۱۲، یعنی دو ارجاعِ دیگرِ نورایی — همان مواد را با همان توضیح می‌آورند. اما پژوهشِ امروزی آنچه را پوکورنی یکی کرده بود جدا کرده است: LIV و چونگ برای خانوادهٔ «سرد» ریشهٔ *ḱelH- «یخ بستن» را می‌نهند (چونگ: *sarH¹) و ویکی‌واژه و NIL خانوادهٔ «سال» را از *ḱelh₁- «گرم شدن» از راهِ هندوایرانیِ *ćarHáts می‌گیرند، و واتکینز اصلاً مدخلی برای «سرد» ندارد و تنها «kelə-1 گرم» را با ارجاع به پوکورنیِ ۵۵۱ می‌آورد. پس جعبهٔ یگانهٔ نورایی با «دو معنیِ متضاد» گزارشی وفادار از معیارِ سالِ ۱۹۵۹ است نه از معیارِ امروز — و این نکته اهمیت دارد، چون ادعای اصلیِ نمودار، یعنی هم‌ریشه بودنِ «سرد» و «سال» فارسی، همان چیزی است که این جدایی‌سازیِ نو در آن تردید می‌افکند. درونِ نمودار سه جعبه نیازمندِ توضیح است: «sarez» اوستاییِ گرهٔ ۵ (خطای چاپیِ کتاب)، «sālak» پهلویِ گرهٔ ۶ (که «-ساله» است نه «سال»)، و «upa-sard» گواهی‌نشدهٔ گرهٔ ۸.\",\n   sources=[W+\"Reconstruction:Proto-Iranian/carHd%C3%A1h\"],\n   ref_check=[\n    dict(ref=\"POK:551\", status=\"supports\", note=\"POK_02.txt, printed p.551: '1. ḱel- 1. „frieren, kalt“, 2. „warm“ (Bedeutungsvermittlung wohl „brennend“). 1. Ai. śiśira- „kühl, kalt“ …, av. sarəta- „kalt“, npers. sard ds., osset. sald „Kälte“, av. sarə-δā- „Kälte bringend“; lit. šálti … 2. Ai. śarád- f. „Herbst“, mit Zahlwörtern „Jahr“, av. sarəd- f. „Jahr“ …, npers. sāl „Jahr“ … lat. caleō, -ēre „warm, heiß sein, glühen“, calidus, calor.' The whole chart in one article.\"),\n    dict(ref=\"SYN:1078\", status=\"supports\", note=\"Buck §15.86 COLD, p.1078: '1. IE *ḱel-, prob. the same root as in words for \\\"hot\\\", Lat. calidus, etc. See 15.85. … Skt. śiśira-, Av. sarəta-, N Pers. sard, also in Av. sarə-δā- \\\"bringing cold\\\"; Osset. sald.' — including Buck's own statement that the 'cold' and 'hot' words are probably one root, which is Nourai's note.\")],\n   consulted=[\n    dict(src=\"WLD\", where=\"Walde-Pokorny I 429-430 (WLD_Bd1_pages.txt leaves 437-438)\", stance=\"supports\", note=\"the fuller article Pokorny abridges: '1. ḱel- 1. „frieren, kalt“, 2. „warm“ … lat. caleō, -ēre „warm, heiß sein, glühen“, calidus „warm, heiß“, calor „Wärme, Hitze“ … lit. šylu, šilau, šilti „warm werden“.'\"),\n    dict(src=\"AHD\", where=\"Watkins 1985, IE roots appendix s.v. kelə-1 (AHD_watkins1985.txt line 606)\", stance=\"partial\", note=\"'kelə-1. Warm. … [Pok. 1. kel- 551.]' — Watkins keeps only the 'warm' half at Pokorny's page 551 and has no entry for a root *ḱel- 'cold'; the 'cold' words are simply absent from his appendix, so the American Heritage list already implies the split that LIV later made explicit.\"),\n    dict(src=\"SYN\", where=\"Buck §14.73 YEAR, p.1012 (SYN.txt line 25743)\", stance=\"supports\", note=\"'Av. sarəd-, OPers. θard- (certainly \\\"year\\\", not \\\"manner\\\" as Barth. 1566), NPers. sāl \\\"year\\\", Osset. särd \\\"summer\\\" : Skt. śarad- \\\"autumn\\\", also \\\"year\\\" in RV, etc., perh. as orig. \\\"warm season\\\" fr. … Lat. calēre \\\"be warm\\\", etc.'\"),\n    dict(src=\"CHEUNG\", where=\"Etymological Dictionary of the Iranian Verb s.v. *sarH1 (CHEUNG.txt line 22040 ff.)\", stance=\"partial\", note=\"'*sarH1 \\\"to cool, become cold\\\" … «PIE *ḱelH- \\\"to freeze\\\". … LIV: 323 | Pok.: 551f. *IE COGNATES: Lith. šálti \\\"to freeze, cool (off)\\\", Latv. salt.' Cheung reconstructs a laryngeal-final root meaning only 'freeze' and does not join the 'warm/year' material to it.\")],\n   nodes=E0_NODES),\n  dict(entry=1, root=\"Kel 2\", verdict=\"confirmed\",\n   modern_form=\"PIE *ḱel- 'to cover, conceal' (Pokorny 'ḱel-4: to conceal', pp. 553-554; Watkins 'kel-2. To cover, conceal, save')\",\n   note=\"Root, language label, gloss and page reference are all exact. Pokorny's fourth ḱel- is headed 'to conceal' and runs from p.553 to p.554, and its material is, box for box, the material of this chart: Greek καλιά, καλύπτω, καλύβη; Latin *celō (occulō), color, cēlāre, cella, clam; Germanic *haljō (hell), *hallō (hall), hulundi 'cave', huljan, helms 'helmet'; Sanskrit śárman- 'shelter, cover'. Watkins's kel-2 'To cover, conceal, save' is the same article in English, and even the derived English words Nourai lists — hall, hell, hole, hollow, helmet, color, conceal, eucalyptus — are Watkins's own list of English derivatives, as is Klein's parallel list under cell. The chart is therefore an accurate rendering of the standard account for everything west of Iran. The problem is on the Iranian side: the two Persian words hung on this root, کلاه and کلبه, rest on Horn's 1893 suggestions, and Hübschmann demolished the second of them in 1895 on the very page (Persische Studien 88) that Nourai cites as his authority for the Pahlavi form. Moʿin, in the footnotes to the two Borhān pages cited, accepts the Middle Persian antecedents kulāf and kurpak but attaches neither to any Indo-European root, and says of kolāh outright that its etymology is not properly known.\",\n   note_fa=\"ریشه و برچسبِ زبان و معنا و شمارهٔ صفحه هر چهار دقیق‌اند. چهارمین ḱel- پوکورنی با معنیِ «پنهان کردن» از صفحهٔ ۵۵۳ تا ۵۵۴ کشیده شده و موادِ آن جعبه‌به‌جعبه همان موادِ این نمودار است: یونانی καλιά و καλύπτω و καλύβη؛ لاتین *celō (occulō) و color و cēlāre و cella و clam؛ ژرمنی *haljō (hell) و *hallō (hall) و hulundi «غار» و huljan و helms؛ سنسکریت śárman- «سرپناه، پوشش». مقالهٔ kel-2 واتکینز («پوشاندن، پنهان کردن، نگاه داشتن») همان مقاله به انگلیسی است، و حتی فهرستِ واژه‌های انگلیسی که نورایی آورده — hall، hell، hole، hollow، helmet، color، conceal، eucalyptus — همان فهرستِ واتکینز و همانندِ فهرستِ کلاین ذیلِ cell است. پس نمودار برای هر چه غربِ ایران است گزارشی درست از معیارِ پذیرفته‌شده است. دشواری در سویِ ایرانی است: دو واژهٔ فارسیِ آویخته به این ریشه، «کلاه» و «کلبه»، بر پیشنهادهای هرن (۱۸۹۳) استوارند، و هوبشمان دومی را در سالِ ۱۸۹۵ درست در همان صفحه‌ای (پژوهش‌های فارسی، ص ۸۸) که نورایی برای صورتِ پهلوی به آن ارجاع داده، رد کرده است. معین نیز در حواشیِ همان دو صفحهٔ برهانِ قاطع صورت‌های فارسیِ میانهٔ kulāf و kurpak را می‌پذیرد اما هیچ‌یک را به ریشه‌ای هندواروپایی نمی‌بندد و دربارهٔ «کلاه» صریح می‌گوید که وجهِ اشتقاقی‌اش درست معلوم نیست.\",\n   sources=[W+\"Reconstruction:Proto-Indo-European/%E1%B8%B1el-\"],\n   ref_check=[dict(ref=\"POK:553\", status=\"supports\", note=\"POK_full.txt lines 49924-50001: 'Root / lemma: ḱel-4 || Meaning: to conceal || Material: Old Indic śaraṇa- \\\"sheltering\\\" … śarman- n. \\\"shelter, protective roof, cover\\\" (: Modern High German Helm) … gr. καλιά \\\"cottage, barn, nest\\\" … with labial extension καλύπτω \\\"wrap, hide\\\", καλύβη \\\"hideout, cottage\\\" … Latin *celō … in occulo \\\"conceal\\\"; color, -oris \\\"paint, color\\\" … lengthened grade cēlō, -āre \\\"hide, conceal\\\" … Gothic hulundi \\\"cave\\\" … Gothic hilms, Old High German Old Saxon Old English helm \\\"helmet\\\" … Gothic halja, Old High German hella … Old High German Old Saxon halla, Old English heall \\\"hall\\\" … References: WP. I 432 f. … Page(s): 553-554.'\")],\n   consulted=[\n    dict(src=\"AHD\", where=\"Watkins 1985 s.v. kel-2 (AHD_watkins1985.txt line 603)\", stance=\"supports\", note=\"'kel-2. To cover, conceal, save. … [Pok. 4. kel- 553.]' with HELL, HALL, VALHALLA, HULL, HOLE, HOLLOW, HOLSTER, CLANDESTINE, CALYPSO, CALYPTRA, APOCALYPSE, EUCALYPTUS, HELM, HELMET, OCCULT, COLOR, CELL, CILIUM, CONCEAL — Nourai's whole second chart.\"),\n    dict(src=\"WLD\", where=\"Walde-Pokorny I 432-433 (WLD_Bd1_pages.txt leaves 440-441)\", stance=\"supports\", note=\"'4. ḱel- „bergen, verhüllen“. Ai. śaraṇa- „schirmend“ … śarman- n. „Schirm, Schutzdach, Decke, Obhut“ (: dt. Helm) … Gr. καλιά „Hütte, Scheune, Nest“ … mit Labialerw. καλύπτω „umhülle, verberge“, καλύβη „Obdach, Hütte“ … got. huljan, anord. hylja, ahd. hullen „verhüllen“.'\"),\n    dict(src=\"KLN\", where=\"Klein, Comprehensive Etymological Dictionary s.v. cell\", stance=\"supports\", note=\"'L. cella … cēlāre, \\\"to hide, keep secret\\\". See cell and cp. caliology, Calypso, apocalypse, Eucalyptus, kelyphite … Cp. also caliology, calyptra, cilia, clandestine, color, conceal, dharmsala, Eucalyptus, hall, hell, helmet, holster, hull, kalidium, kelyphite, kil-, occult, superciliary, Valhalla.'\"),\n    dict(src=\"SYN\", where=\"Buck §7.13 HUT, p.460\", stance=\"supports\", note=\"'IE *ḱel- \\\"cover, hide\\\" in Lat. occulere, cēlāre, Ir. celim, OE helan, etc.'\")],\n   nodes=E1_NODES),\n ])\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-250.json','w',encoding='utf-8') as f:\n    json.dump(doc,f,ensure_ascii=False,indent=2)\nprint('ok')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk250.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-250.json > /dev/null && echo JSON_OK && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 250"
}
```


### [2026-09-06T16:29:44.175Z] TOOL RESULT

```
ok
JSON_OK
nodes verified: 24/24
node verdicts: {'confirmed': 16, 'transcription_suspect': 2, 'plausible': 4, 'disputed': 2}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 20, 'partial': 10, 'contradicts': 1, 'not_checked': 3}
books consulted: {'supports': 52, 'partial': 11, 'silent': 2, 'contradicts': 1} | by book: {'KLN': 9, 'PHD': 6, 'WLD': 5, 'AHD': 5, 'BRT': 4, 'CHEUNG': 4, 'BQT': 4, 'POK': 4, 'HRN': 3, 'MON': 3, 'SYN': 3, 'WEB': 3, 'NYB': 2, 'SOD': 2, 'ARY': 2, 'HUB': 2, 'SKT': 2, 'KNT': 1, 'LAT': 1, 'PLA': 1}
```


## [2026-09-06T16:30:18.462Z] AGENT

Done — `data/verification/page-250.json` written, `verify_check.py 250` reports **24/24 nodes, 0 PROBLEM lines**.

**Page 250 (book p.220) — roots `Kel 1` (cold/warm/year) and `Kel 2` (to cover)**

Verdicts: roots 2 confirmed. Nodes: 16 confirmed, 4 plausible, 2 disputed, 2 transcription_suspect.
Ref checks: 20 supports, 10 partial, 1 contradicts, 3 not_checked. 66 `consulted` entries across 20 books.

Flagged items:
- **transcription_suspect — Kel 1 #5 Avestan "sarez"**: no such Avestan form; the word is `sarəd-` f. "year" (Bartholomae 1566). The 400-dpi scan shows the book itself prints "sarez, sareda" → author's misprint, extraction faithful.
- **transcription_suspect — Kel 2 #3 Greek "kolba"**: a corruption of καλύβη *kalúbē* "hut" — proved by Nourai's own citation SYN:460, where Buck §7.13 opens "Grk. καλύβη fr. the stem of καλύπτω". Book prints "kolba"; extraction faithful.
- **disputed — Kel 2 #1/#2 (Pahlavi kurpak → Persian کلبه)**: Nourai's `HUB:88` is the page where Hübschmann *refutes* him — "Np. kulba … aus phl. *kurpak = arm. kʿrpak …, hat also mit gr. καλύβη nichts zu thun." Modern view (Wiktionary citing Bartholomae): کلبه < MP *kurbag* < *kirb* "body, form" < PIE *\*krep-*, "unrelated to καλύβη". کلاه itself is only *plausible*: the *ḱel- link is Horn's guess and Moʿin (BQT:1671 n.10) says "وجه اشتقاقی آن درست معلوم نیست".
- **plausible — Kel 1 #6** Pahlavi *sālak* is "-year-old", not "year" (MacKenzie, Horn, Nyberg); and MP *sāl* descends from OP *θard-* (SW *rd*>*l*), not from Avestan *sarəd-*.
- **plausible — Kel 1 #8** OP *upa-sard* is unattested (absent from Kent 188), though well supported by MacKenzie's MP `*afsālān` "springtime".
- **plausible — Kel 1 #9** آبسال: MacKenzie's `*afsālān` "springtime" confirms the *upa-sarda-* etymology, but Borhān (the cited p.7) and Dehkhodā gloss آبسالان "باغ، حدیقه", not "spring" — the *āb-* is folk-etymology for *af-*.

No extraction errors: every questioned form was checked against the 400-dpi render of pdf p.250 and the JSON matches the printed page exactly. Page image archived to `data/verification/sources/refs/ocr/BOOK/250.png`; 12 web pages archived via `fetch_source.py`.

Notable positive findings: Pokorny p.551 heads the article "1. ḱel- 1. 'frieren, kalt', 2. 'warm'" — Nourai's root gloss *and* his note "two opposing meanings" are Pokorny verbatim; Cheung's `*sarH1` covers nodes 1–4 in one entry; both Borhān page numbers (1671, 1673) are exact; both Sogdian citations are one page low (srδ is on p.362, srt on p.363).
