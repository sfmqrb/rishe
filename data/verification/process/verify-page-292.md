# Verification process log — verify-page-292


## [2026-09-06T22:11:09.773Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 292 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-292.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-292.json. Write /home/sfmqrb/git/rishe/data/verification/page-292.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 292` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T22:11:11.482Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T22:11:12.223Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T22:11:12.240Z] TOOL RESULT

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


## [2026-09-06T22:11:12.976Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-292.txt"
}
```


## [2026-09-06T22:11:12.983Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/extracted/batch/page-292.json"
}
```


### [2026-09-06T22:11:12.998Z] TOOL RESULT

```
1	=== PDF page 292 (book page 262) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Kwen 2 : sip, swallow  (refs POK:640)
4	#1 (parent #0) [Old Iranian] refs=AHM:184 | čam : to sip, drink
5	  #2 (parent #1) [Persian] refs=POK:640; AHM:184 | čamîdan 2 «چَمیدن ۲ ( چَم )» : to sip, drink (obsolete)
6	  #3 (parent #1) [Persian] refs=POK:640 | kâm 2 «کام ۲» : palate
7	#4 (parent #0) [Sanskrit] refs=POK:640 | čamati, camati : to sip
8	--- entry 1 ---
9	ROOT Kwěp -> redirect to Kŭp 2
10	--- entry 2 ---
11	ROOT [Indo-European] Kwer, Qwer : to make, form  (refs POK:641)  PART 1
12	#1 (parent #0) [Avestan / Old Persian] refs=NYB:157; HRN:80; ZAW:38; SYN:628 | kar 1, kara 1 : to work ; kara-manah : wise at work, manager ☞Men 1 ; paiti-kâra : work against, fight ☞Per 3 ; paiti-kara : form against (like) something ☞Per 3 ; aiwiš-kar : chase (animals) away, hunt ☞Ambhi ; wi-kâr : to digest ☞Wi
13	  #2 (parent #1) [Persian] refs=BQT:1549,1617,1779 | kârîdan 2 «کاریدن ۲ ( کردن ، کار ۱ )» : to do ; gar 2 «گر ۲» : a suffix meaning worker ; kahr-mân «کهرمان ، قهرمان» : wise at work, hero | extra: آهنگر ، کوزه گر ، زرگر
14	  #3 (parent #1) [Persian] refs=DMO:115; MON:2057,3426; FFD:68,75 | paykâr «پیکار» : fight ; paykar «پیکر» : body, statue ; šekâr «شکار ( شِکَردن ، شِکَر ۲ )» : hunt ; govârdan «گواردن ( گوارا ، گوارش )» : digest
15	#4 (parent #0) [Avestan / Old Persian] refs=HRN:201; ZAW:38 | krta : creation, city ; yazato-karteta : God's creation ☞Yag
16	  #5 (parent #4) [Persian] refs=BQT:1787,2432; DMO:115 | -vard, -gard, -jerd «ـ ورد ، ـ گرد ، ـ جرد» : town, installations ; Yazdgerd «یزدگرد» : "God's creation", a male name ☞Yag ; Lâjvard «لاجورد» : "home of Turkish Lâj(in) tribe" ☞Lâjîn | extra: ابیورد ، بروجرد ، سوسنگرد ، دستگرد
17	#6 (parent #0) [Avestan] refs=BQT:173; ZAW:38,242; HRN:28,232; HUB:39 | han-kar : to do (consider) all, imagine ☞Sem 1 ; han-kareyemi, han-keretha : consider ; haša-kerta : one who pays attention and follows, a student ☞Sekw ; pairi-kara : go (draw) around, a compass ☞Per 1
18	  #7 (parent #6) [Persian] refs=BQT:173,2157,2164; ZAW:38,242 | engârdan «انگاردن ( انگاشتن ، انگار )» : imagine ; šâgerd «شاگرد» : student, follower ; pargâr «پرگار» : compass, necklace, fortune | extra: نگاریدن ، نگاشتن ، نگار ، نگریستن
19	نگاردن ، نگارش ، نگریدن ، نگرستن | NOTE: HUB:39 is not sure about the derivation of "pargâr"
20	
```


### [2026-09-06T22:11:13.000Z] TOOL RESULT

```
1	{
2	  "pdf_page": 292,
3	  "book_page": 262,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Kwen 2",
8	        "lang": "Indo-European",
9	        "refs": "POK:640",
10	        "gloss": "sip, swallow"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Old Iranian",
17	          "refs": "AHM:184",
18	          "words": [
19	            {"translit": "čam", "gloss": "to sip, drink", "script": null}
20	          ],
21	          "script_extra": null,
22	          "note": null,
23	          "quote": null
24	        },
25	        {
26	          "id": 2,
27	          "parent": 1,
28	          "lang": "Persian",
29	          "refs": "POK:640; AHM:184",
30	          "words": [
31	            {"translit": "čamîdan 2", "gloss": "to sip, drink (obsolete)", "script": "چَمیدن ۲ ( چَم )"}
32	          ],
33	          "script_extra": null,
34	          "note": null,
35	          "quote": null
36	        },
37	        {
38	          "id": 3,
39	          "parent": 1,
40	          "lang": "Persian",
41	          "refs": "POK:640",
42	          "words": [
43	            {"translit": "kâm 2", "gloss": "palate", "script": "کام ۲"}
44	          ],
45	          "script_extra": null,
46	          "note": null,
47	          "quote": null
48	        },
49	        {
50	          "id": 4,
51	          "parent": 0,
52	          "lang": "Sanskrit",
53	          "refs": "POK:640",
54	          "words": [
55	            {"translit": "čamati, camati", "gloss": "to sip", "script": null}
56	          ],
57	          "script_extra": null,
58	          "note": null,
59	          "quote": null
60	        }
61	      ]
62	    },
63	    {
64	      "root": {
65	        "name": "Kwěp",
66	        "redirect": "Kŭp 2"
67	      },
68	      "nodes": []
69	    },
70	    {
71	      "root": {
72	        "name": "Kwer, Qwer",
73	        "lang": "Indo-European",
74	        "refs": "POK:641",
75	        "gloss": "to make, form"
76	      },
77	      "part": 1,
78	      "nodes": [
79	        {
80	          "id": 1,
81	          "parent": 0,
82	          "lang": "Avestan / Old Persian",
83	          "refs": "NYB:157; HRN:80; ZAW:38; SYN:628",
84	          "words": [
85	            {"translit": "kar 1, kara 1", "gloss": "to work", "script": null},
86	            {"translit": "kara-manah", "gloss": "wise at work, manager", "script": null, "see": ["Men 1"]},
87	            {"translit": "paiti-kâra", "gloss": "work against, fight", "script": null, "see": ["Per 3"]},
88	            {"translit": "paiti-kara", "gloss": "form against (like) something", "script": null, "see": ["Per 3"]},
89	            {"translit": "aiwiš-kar", "gloss": "chase (animals) away, hunt", "script": null, "see": ["Ambhi"]},
90	            {"translit": "wi-kâr", "gloss": "to digest", "script": null, "see": ["Wi"]}
91	          ],
92	          "script_extra": null,
93	          "note": null,
94	          "quote": null
95	        },
96	        {
97	          "id": 2,
98	          "parent": 1,
99	          "lang": "Persian",
100	          "refs": "BQT:1549,1617,1779",
101	          "words": [
102	            {"translit": "kârîdan 2", "gloss": "to do", "script": "کاریدن ۲ ( کردن ، کار ۱ )"},
103	            {"translit": "gar 2", "gloss": "a suffix meaning worker", "script": "گر ۲"},
104	            {"translit": "kahr-mân", "gloss": "wise at work, hero", "script": "کهرمان ، قهرمان"}
105	          ],
106	          "script_extra": "آهنگر ، کوزه گر ، زرگر",
107	          "note": null,
108	          "quote": null
109	        },
110	        {
111	          "id": 3,
112	          "parent": 1,
113	          "lang": "Persian",
114	          "refs": "DMO:115; MON:2057,3426; FFD:68,75",
115	          "words": [
116	            {"translit": "paykâr", "gloss": "fight", "script": "پیکار"},
117	            {"translit": "paykar", "gloss": "body, statue", "script": "پیکر"},
118	            {"translit": "šekâr", "gloss": "hunt", "script": "شکار ( شِکَردن ، شِکَر ۲ )"},
119	            {"translit": "govârdan", "gloss": "digest", "script": "گواردن ( گوارا ، گوارش )"}
120	          ],
121	          "script_extra": null,
122	          "note": null,
123	          "quote": null
124	        },
125	        {
126	          "id": 4,
127	          "parent": 0,
128	          "lang": "Avestan / Old Persian",
129	          "refs": "HRN:201; ZAW:38",
130	          "words": [
131	            {"translit": "krta", "gloss": "creation, city", "script": null},
132	            {"translit": "yazato-karteta", "gloss": "God's creation", "script": null, "see": ["Yag"]}
133	          ],
134	          "script_extra": null,
135	          "note": null,
136	          "quote": null
137	        },
138	        {
139	          "id": 5,
140	          "parent": 4,
141	          "lang": "Persian",
142	          "refs": "BQT:1787,2432; DMO:115",
143	          "words": [
144	            {"translit": "-vard, -gard, -jerd", "gloss": "town, installations", "script": "ـ ورد ، ـ گرد ، ـ جرد"},
145	            {"translit": "Yazdgerd", "gloss": "\"God's creation\", a male name", "script": "یزدگرد", "see": ["Yag"]},
146	            {"translit": "Lâjvard", "gloss": "\"home of Turkish Lâj(in) tribe\"", "script": "لاجورد", "see": ["Lâjîn"]}
147	          ],
148	          "script_extra": "ابیورد ، بروجرد ، سوسنگرد ، دستگرد",
149	          "note": null,
150	          "quote": null
151	        },
152	        {
153	          "id": 6,
154	          "parent": 0,
155	          "lang": "Avestan",
156	          "refs": "BQT:173; ZAW:38,242; HRN:28,232; HUB:39",
157	          "words": [
158	            {"translit": "han-kar", "gloss": "to do (consider) all, imagine", "script": null, "see": ["Sem 1"]},
159	            {"translit": "han-kareyemi, han-keretha", "gloss": "consider", "script": null},
160	            {"translit": "haša-kerta", "gloss": "one who pays attention and follows, a student", "script": null, "see": ["Sekw"]},
161	            {"translit": "pairi-kara", "gloss": "go (draw) around, a compass", "script": null, "see": ["Per 1"]}
162	          ],
163	          "script_extra": null,
164	          "note": null,
165	          "quote": null
166	        },
167	        {
168	          "id": 7,
169	          "parent": 6,
170	          "lang": "Persian",
171	          "refs": "BQT:173,2157,2164; ZAW:38,242",
172	          "words": [
173	            {"translit": "engârdan", "gloss": "imagine", "script": "انگاردن ( انگاشتن ، انگار )"},
174	            {"translit": "šâgerd", "gloss": "student, follower", "script": "شاگرد"},
175	            {"translit": "pargâr", "gloss": "compass, necklace, fortune", "script": "پرگار"}
176	          ],
177	          "script_extra": "نگاریدن ، نگاشتن ، نگار ، نگریستن\nنگاردن ، نگارش ، نگریدن ، نگرستن",
178	          "note": "HUB:39 is not sure about the derivation of \"pargâr\"",
179	          "quote": {
180	            "text": "همانا که برگشت پرگار ما - غنوده شد آن بخت بیدار ما",
181	            "poet": "Ferdowsî"
182	          }
183	        }
184	      ]
185	    }
186	  ]
187	}
188	
```


## [2026-09-06T22:11:14.750Z] AGENT

I'll gather the reference infrastructure info first.


## [2026-09-06T22:11:18.462Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHM','NYB','HRN','ZAW','SYN','BQT','DMO','MON','FFD','HUB','WLD','AHD','BRT','KNT','PHD','CHEUNG','ARY','KLN','SKT','IEC']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:400] if v else 'MISSING')\n\"",
 "description": "Inspect refs_online.json entries"
}
```


## [2026-09-06T22:11:18.967Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n '1,200p' data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T22:11:20.198Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
AHM {"title": "I. Gershevitch, The Avestan Hymn to Mithra, Cambridge 1959", "edition_found": "1959", "kind": "archive_djvu", "url": "https://archive.org/details/gershevitch-ilya-the-avestan-hymn-to-mithra-cambridge-university", "identifier": "gershevitch-ilya-the-avestan-hymn-to-mithra-cambridge-university", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHM.txt", "page_offset": 
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
ZAW {"title": "C. Bartholomae, Zum altiranischen Wörterbuch: Nacharbeiten und Vorarbeiten (Beiheft zu IF XIX), Strassburg 1906", "edition_found": "1906 - Google Books record only", "kind": "google_books", "url": "https://books.google.com/books?id=agDP0HdEssEC (full view; PDF downloaded) ; also 8q0zAQAAMAAJ (full view) ; HathiTrust coo.31924026891675 (pdus)", "identifier": "agDP0HdEssEC", "local_file":
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
DMO {"title": "Sa'id Nafisi, Dar Maktab-e Ostad, Zohreh 1344/1965", "kind": "website", "url": "https://www.ketabnak.com/book/55983 (283 pp. PDF, login)", "lookup_hint": "Not on archive.org.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "PDF page exists; not fetched."}
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/downloa
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
CHEUNG MISSING
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
```


### [2026-09-06T22:11:20.236Z] TOOL RESULT

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
```


## [2026-09-06T22:11:24.263Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-06T22:11:24.300Z] TOOL RESULT

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


## [2026-09-06T22:11:25.034Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/page-259.json'))\nprint(json.dumps(d['entries'][0], ensure_ascii=False, indent=1)[:3000])\n\""
}
```


### [2026-09-06T22:11:26.822Z] TOOL RESULT

```
{
 "entry": 0,
 "root": "Kerd 1, Kred",
 "verdict": "confirmed",
 "modern_form": "PIE *ḱḗr, oblique stem *ḱr̥d- (root *ḱerd-) 'heart'; with the compound *ḱred-dʰeh₁- 'to place one's heart, trust'",
 "note": "Pokorny p.579 bottom–580 heads the entry exactly '(kered-:) kerd-, kērd-, kr̥d-, kred- ‘Herz’', so Nourai's headword 'Kerd 1, Kred', the language label 'Indo-European' and the gloss 'heart' all reproduce his source correctly; AHD (Watkins) has 'kerd-1. Heart. [Pok. kered- 579.]'. The one substantive caveat concerns the 'kred-' half: Pokorny himself (p.580) says the kred-dhē- 'believe' group is 'nicht hierher' (not to be connected with 'heart'), and Buck 17.15, Klein s.v. heart and Ernout–Meillet s.v. cor agree; modern standard works (Watkins/AHD, de Vaan 2008 s.v. crēdō, Wiktionary) do connect it, analysing *ḱred-dʰeh₁- as 'to place one's heart'. Nourai therefore follows the newer, now dominant, view — but not the page of Pokorny he cites. The Iranian branch has a further complication that the chart passes over: Indo-Iranian shows a voiced aspirate initial (Skt. hṛd-, Av. zərəd-, PII *ȷ́ʰā́rd) where *ḱ- is expected, 'unexplained voiced aspiration' (Wiktionary), 'mit init. as if fr. IE gh, due to a blend with some other word' (Buck 251).",
 "note_fa": "ریشهٔ هندواروپایی آغازین *ḱḗr (ستاک غیرفاعلی *ḱr̥d-، ریشهٔ *ḱerd-) به معنی «دل، قلب» است و پوکورنی در ص ۵۷۹–۵۸۰ سرواژه را دقیقاً «kerd-, kērd-, kr̥d-, kred-: Herz» آورده؛ پس نام ریشه، برچسب زبانی و معنایی که نورایی داده درست است. تنها نکتهٔ محل بحث بخش kred- است: خودِ پوکورنی در ص ۵۸۰ پیوند kred-dhē- «باور داشتن» را با «دل» رد می‌کند و باک و کلاین و ارنو–مه‌یه نیز همین نظر را دارند، اما واتکینز (AHD)، دِ وان و ویکی‌واژه آن را می‌پذیرند و *ḱred-dʰeh₁- را «دل نهادن» می‌دانند؛ یعنی نورایی از دیدگاه نو پیروی کرده است نه از صفحه‌ای که به آن ارجاع داده. نکتهٔ دیگر آنکه در هندوایرانی به جای *ḱ- انسدادی واکدارِ دمیده دیده می‌شود (سنسکریت hṛd-، اوستایی zərəd-) که هنوز توضیح قطعی ندارد.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1%E1%B8%97r",
  "https://en.wiktionary.org/wiki/credo%23Latin",
  "https://www.etymonline.com/word/heart"
 ],
 "ref_check": [
  {
   "ref": "POK:579",
   "status": "supports",
   "note": "Pokorny IEW p.579 (bottom) – 580, read in POK_02.txt leaf 239–240 (awk 'BEGIN{RS=\"\\f\"} NR==239'): '(kered-:) kerd-, kērd-, kr̥d-, kred- ‘Herz’. Arm. sirt … gr. καρδία (att.), κραδίη (hom.) … lat. cor (aus *cord) … got. hairto, ahd. herza, ags. heorte, anord. hjarta n. ‘Herz’ (*ḱērd-on-)'. Exactly Nourai's root name and gloss."
  },
  {
   "ref": "SYN:251",
   "status": "supports",
   "note": "Buck, Selected Synonyms p.251 = §4.44 HEART (SYN.txt leaf 289, page number '251' printed in the running head above '4.44 HEART'): 'Most of the words for ‘heart’ belong to an inherited group … 1. IE *ḱerd-, etc., with gradation. Walde-P. 1.423 ff. Ernout-M. 219 f.'"
  }
 ],
 "consulted": [
  {
   "src": "AHD",
   "where": "Watkins 1985, s.v. kerd-1 (AHD_wat
```


## [2026-09-06T22:11:33.413Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la POK*.txt && head -c 600 POK_02.txt && echo \"---\" && grep -c $'\\f' POK_01.txt POK_02.txt POK_03.txt POK_full.txt"
}
```


## [2026-09-06T22:11:34.182Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"camati\\|čamati\\|cámati\" POK_*.txt | head -40"
}
```


### [2026-09-06T22:11:35.201Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb  981836 Sep  4 14:06 POK_01.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1137861 Sep  4 14:06 POK_02.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1170809 Sep  4 14:06 POK_03.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 3971883 Sep  4 14:06 POK_full.txt
H
^-)e7
G,  O.
^äb-  ,schauen^  ausschauen  nach9? ergäbe  sich,  wenn  man  mit  Zupitza  Gutt.  194  aisl.  köpa  (j)p)  ^starren,  gaffen^, ao-s.  ccepan  ^beobachten,  ausschauen  nach,  sorgen  für,  schützen^,  ablautend ags.  capian  up  ,aufblicken^,  asächs.  upcapen  ,eminere^;  mnd.  kapen  ,gaffen, schauen',  mhd.  kaffen  ds.,  ahd.  (mit  Intensivgemination)  kapfen  ,schauen, spähen'  (daraus  rückgebildet  ahd.  kapf  ,Ort,  von  dem  man  ausschaut, Gipfel')  und  ahd.  üfkepfen  ,aufschauen'  zu  russ.  zahota  ,Sorge',  zabotith  ^a ,sich  sorgen  machen,  sich ---
POK_01.txt:352
POK_02.txt:420
POK_03.txt:415
POK_full.txt:0
```


### [2026-09-06T22:11:35.244Z] TOOL RESULT

```
POK_02.txt:4755:Ai.  cämati  und  camati  .schlürft'.  Partiz.  äcänta-j  camasd-  m.  .Trink- schale. Becher',  camü-  m.  .Schüssel';  npers.  cam  .das  Essen',  camiöan .trinken',  osset.  cumun  , schlürfen' ;
POK_full.txt:45212:presumably also Slavic *cbma\v\ serb. cama^ boredom, weariness ', camati^ wait with 
POK_full.txt:52830:nisi, hvoma {iroxw *hvama, Indo Germanic *k"emd= Old Indie camati) " swallow, devour,
```


## [2026-09-06T22:11:39.052Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4735,4790p' POK_02.txt"
}
```


### [2026-09-06T22:11:39.104Z] TOOL RESULT

```
colus,  -üs  f.  m,  oder  -l  f.  ,Spinnrocken'  (^k'^elos  ,Spindel'),  collus,  -l  m. (alat.),  Collum,  -l  n.  ,Hals,  Bergjoch'  {^kV^ol-so-,  got.  hals)]
air.  cul  ,Wagen'  (Dual.  *k'^olö) ;  mir.  coli  ,Haupt'  =
640  /
got.  aisl.  asächs.  hals  m.,  ags.  heals,  nhd.  ,HaU  ]  aisl.  hvel  n.,  Rad'
apr.  kelan  ,Rad',  lett.  f.  PL  du-celes  .zweirädriger  Wagen' ;
aksl.  kolo  n.,  Gen.  kolese  ,Rad',  PL  kola  ,Wagen'  (Mischung  von  k^ol m.  und  k^eles-  n.);
bsL  '^kelia-  .Knie'  in  lit.  kelys,  ostlit.  kelias  .Knie',  fett,  celis  ds.;  Ü^ ÄreZenas  m.  .Knie',  ablaut.  aksL  koUno  n.  .Knie.  Stamm.  Geschlecht',  vielleicht weiter  zu  slav.  *celm  m..  sloven.  clm  .Gelenk.  Glied',   klr.  iSeUn  .Glied*»!
toch.  A  källä^  »bringt',  Prät.  sei,  PL  kalar  (Pedersen  Tochar.  183).
k^ek^lo-,  k^ok^lo-{^)  .Rad'  in:
ai.  cakrd-  m.  n.  (Akzent  sekundär)  .Wagenrad.  Scheibe.  Kreis',  av. caxra-  m.  .Rad',  gr.  'AvyCkoq  .Kreis^.  PL  -/.vuloi  und  xvxAa  .Räder',  aisl. hjöl,  hvel  {*k'^ek'^elon-,  germ.  *Mveh(iv)ula-)  n..  ags.  hweol  (engl.  wheeJ)^ daneben  hweowol,  hiveogol  (germ.  *hweg{w)uld-),  mnd.  wel  .Rad';  auch fries.  fial  ist  wohl  eine  Dissimil.-Form  für  ^hweiola-]  vgl.  auch  phryg. xiyiXrjv  .der  große  Bär'  (.Wagen'),  lit.  käklas,  lett.  kokls  .Hals'  als  .Dreher'; toch.  A  kukäl,  B  kokale  .Wagen'.
Dehnstufig  vielleicht  (als  .gedreht,  rund')  aisl.  hväll  und  höll  m.  (letz- teres aus  dem  Dat.  PL  hölum  aus  hvälum)  .rundlicher  Hügeln
WP.  I  514  f..  WH.  I  45.  245  ff..  250.  846,  Trautmann  125.
2.  k^el-  .fern  (örtlich  und  zeitlich)'  in:
ai.   caramd-   .der  letzte,  äußerste',   cirds   ,lang  (zeitlich)',   gr.  TfjXe,  äol. TtrjXvL  .ferU;  weit'  (rr^lö-d-ev,  -^t.  -crs).  ftdXccv  .längst'  (/raAcctog  .alt'.  TtaXai-  t- TBQoq,  -TaTOQ),  cymr.  corn.  bret.  pell  .fern'  (*Ä;oeZ-s-o-?).  cymr.  pellaf  .der  _ äußerste'.  ^,
WP.  I  517.  ^
j.  kHei-  .Schwärm.  Schar.  Sippe'?
Ai.  küla-m  n.  .Herde.  Menge;  Geschlecht';  kj-sti-  f.  .Leute.  Menschen'; gr.  rsXog  n.  .Schar';
aksl.  celjadh  f.  .Gesinde'.  Kollektiv  zu  dem  in  celovSkT,  .Mensch'  vor- liegenden celo-,
WP.  I  517.  Berneker  141  f..  Meillet  BSL.  22. 18  f.,  Kuiper  Proto-Munda  55.
k^em-  .schlürfen,  schlucken'.
Ai.  cämati  und  camati  .schlürft'.  Partiz.  äcänta-j  camasd-  m.  .Trink- schale. Becher',  camü-  m.  .Schüssel';  npers.  cam  .das  Essen',  camiöan .trinken',  osset.  cumun  , schlürfen' ;
arm.  kim-k  PL  .faux,  guttur'  (*Ä;%emä-);  mit  Ablautstufe  ö:  npers.  kam .Gaumen',  afghan.  kümai  ds. ;  zweifelhaft  ist  gr.  ezef-iev'  ^jfxsXysv  und ri^vowa  [wohl  rs^ovra]'  äfisXyovra  Hes..  wobei  äfxsXysiv  in  der  spätem Bed.  .Flüssiges  aussaugen,  auspressen'  zu  fassen  wäre;
641
nisl.  hvöma  (aus  ^hväma,  idg.  "^k^emö  =  ai.  cdmati)  .verschlucken,  ver- ■!:      schlingen';  hvöma  f.  .Speiseröhre.  Schlund^. WP.  I  Ö14.
^ugae,  Partikel  der  Verallgemeinerung  und  Unbestimmtheit.
Ai.  cana,  av.  <^inä  .irgend^;  oft  negativ,  z.  B.  ai.  nd  Bka§  cana  .keiner^;
germ.  -%in  in  aisl.  hver-gin  .keineswegs^,  ags.  asächs.  ahd.  hiver-gin .irgendwo^  (aus  htvar  .wo'  +  -gin)  aus  ahd.;  io-wergin,  mhd.  iergen,  nhd. irgend.
WP.  I  399  f..  Wackernagel-Debrunner  III  562.
y^üQnth-  .leiden,  duldend
Gr.  Tcevd-og  n.  .Leid.  Trauer.  Unglück';  nachhom.  nad^og  n.  .Leid.  Un- glück, Leidenschaft',  ndoxo)  (*k^nth-s7cö),  Fut.  itslaoiiai,  Aor.  errad-ov, perf.  TCSTtovd^a  ,leide.  erdulde'  (tts-  für  le-  nach  den  Formen  mit  na-,  Tto-) ;
lit.  kenciü,  kgsti  .aushalten,  leiden',  pakantä  f.  .Geduld',  kanciä  .heftiger körperlicher  Schmerz',  itiem-kintis  .den  Winter  über  aushaltend',  lett.  aiehi cust  .leiden,  dulden',  ziem-ciesis  {^kentsia-)  .Wintergrün';
air.  cess{a)im  .ich  leide'  (*k^enth-tö  oder  *k^Aenth-s-ö),  cessad  .passiö'.
Pedersen  KG.  II  486  vermutet  einen  nasallosen  VerAvandten  in  air. ar-cessi  (*k'!^et-si-)  .schont,  erbarmt  sich'  (Bed.  wäre  wie  in  lit.  pakenteti .mit  jemandem  Geduld  haben'),  cymr.  arhedu  (*Ä:^e^)  .schonen',  bret. erhedi  .empfehlen*  (älter  auch  .schonen'),  acorn.  henbidiat  ,parcus'.
WP.  I  513.  Trautmann  126 f..  Schwyzer  Gr.  Gr.  1.  708.
I.  k"er-  .machen,   gestalten'.  Adelleicht  ursprünglich   von  irgendeiner  nicht mehr  bestimmbaren  Handwerkstätigkeit.
Ai.  karöti  (Imper.  kuru),  krnöti  .macht,  vollbringt'.  Partiz.  kftd-]  kard- .tuend.  machend',  m.  .Hand.  Elefantenrüssel',  kära-  .machend',  m.  .Tat'. kdrman-  n.  .Handlung.  Werk',  karmära-h  .Schmied';  k2'ti-  .Tat';  sam-krt .einmal';  daneben  mit  s-  pari-skar-  und  sam-skar-]
av.  kdrdnaoiti  .macht,  vollführt,  tut',  kdrdtay-  .Tat'.  Infin.  kdrdtde,  apers. akunavarrij  karta-]  av.  cärä  .Mittel.  Hilfsmittel',  np.  cär  , Mittel',  cära .Mittel.  Hilfe.  List'  (=  sl.  cara  .Zauber',  s.  unten);
osk.  petiro-pert  .viermal'  (:  ai.  sam-krt);
cymr.  paraf  .bewirke,  verschaffe',  Verbaln.  peri,  wozu  redupL  (aus einem  redupl.  Präs.?)  wohl  cymr.  pyhyr  .tatkräftig';
air.  cruth  .Gestalt',  cymr.  pryd  (*k'^rtu-)  .Gestalt.  Zeit';  dazu  vielleicht air.  Cru(i)thinj  mcymr.  Prydyn  .Pikten';  cymr.  Prydain  .Britannien'  hat die  Endung  von  Rhufain  (ßömanl)  bezogen;  acorn.  prit,  mcorn.  prys, bret.  pred  .Zeit';  mir.  creth  .Dichtung'  (*Ä;?^f^o-).  cymr.  prydu  ,dichten'. prydydd  .Dichter';
41
642
I
lit.    kuriü,    kürti;!, errichten,   bauen,   machen^,    daraus   vielleicht  ,Feuer anmachen,  heizen';  lett.  kurt  ^anfeuern,  heizen',  apr.  küra  ^erbaute';  anders* oben  S.  572.
Hierher  mit  der  Bed.  ,63  jemandem  antun,  verhexen',  auch  ai.  k^ty^ (,Handlung-,  Tat'  und  :)  ,Behexung,  Zauber'  u.  dgl.,  gr.  zigag  n.  ,Wunder- zeichen',  fceXwQ  n.  ,Ungetüm,  Ungeheuer',  rsXwQiog'  ^eyag,  TteXcogiog  Hes.; das  TT-  ist  Äolismus;  tvsXcjüq,  rsXwQ  aus  *7T€qo)q,  Hsqwq  dissimiliert;  Ht. keriü,  kerUi  ,jemanden  bezaubern,  in  der  Gesundheit  schädigen',  kero^ , Zauber',  slav.  6ara  f.  ,Zauber'_in  abg.  carodSjh  ,Zauberer',  cari  f.  pj^ , Zauber,  Reiz'  usw.;
vielleicht  mit  anlaut.  s-  (vgl.  ai.  sam-skar-)  ai.  ä-icarya-  ,seltsam,  wun- derbar', n.  ,Wunder',  aisl.  skars  n.  ,ein  Ungeheuer;  Riesin',  skersa  f. ,Riesin',  skyrse  m.  ,(übles)  Vorzeichen,  Phantom'  (welche  die  suffixale Schwundstufe  des  es-St.  rigag  enthielten).
WP.  I  517  f.,  WH.  I  165,  273,  Trautmann  127.
2,  k^er-  in  Worten,  die  etwas  Schüssel-,  Schalenartiges  bedeuten.
Ai.  carü-  ,Kessel,  Topf,  wozu  wohl  karkarl  ,Wasserkrug',  karaidka- ,  Schädel';
air.  co{i)re  (jedoch  nicht  aus  *kV^erijo-,  sondern  aus  *k'^crijo-),  cymr.  pair, corn.  per  , Kessel';
altn.  hverr' m.  ,Kessel',  ags.  hwerj  ahd.  {h)wer  ds.
w-Erweiterung  liegt  vor  in:  mir.  cern  f.  , Schüssel',  nisl.  hvörn  ,Knochen im  Fischkopf',  norw.  dial.  hvann  ds. ;  got.  Ivairnei  f.  ,Schädel',  aisl.  hverna f.  ,Kochgeschirr'.
WP.  I  518.
k"eru-  , kauen;  zermalmen,  mahlen  (Mehl  und  daraus  Bereitetes)'?
Ai.  cdrvati  , zerkaut,  zermalmt',  Partiz.  cürna-s,  m.  , feiner  Staub,  Mehl' (im  -ü-  wirkt  der  zweite  Vokal  der  Basis  k^eru-  nach?);  anders  über cdrvati  oben  S.  576,  582 ;
gr.  tOQvvrj'  (TLTCüösg  le  Hes,  (assimil.  aus  *TeQvvG),  fcoQvvav  fxaylda Hes.  (entw.  aus  ablautendem  *knorunä  oder  äol.  Form  von  tOQvvr]), nvQvov  n.,  PI.  nvQva  (Hom.)  , Weizenbrot'  {-v-  in  noch  zu  untersuchendem Zusammenhang  mit  dem  zweiten  Vokal  von  ^k^eru-).
```


## [2026-09-06T22:11:39.767Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} /cämati/{print NR}' POK_02.txt"
}
```


### [2026-09-06T22:11:41.698Z] TOOL RESULT

```
301
```


## [2026-09-06T22:12:26.362Z] AGENT

Now let me check the printed page for the root name, and start local reference greps.


## [2026-09-06T22:12:29.195Z] TOOL CALL #12: Bash

```json
{
 "command": "ls site/pages/292.jpg 2>/dev/null; pdftoppm -f 292 -l 292 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg292 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


## [2026-09-06T22:12:30.004Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHM around 184 ===\" && grep -n \"cam\\|čam\\|kām\\|Gaumen\" AHM.txt | head -30"
}
```


### [2026-09-06T22:12:31.992Z] TOOL RESULT

```
site/pages/292.jpg
total 117560
drwx------ 3 sfmqrb sfmqrb     4096 Sep  6 18:12 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   533122 Sep  6 17:21 afm41_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb   508509 Sep  6 17:21 afm41_b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   969829 Sep  6 17:21 afm41.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1322100 Sep  6 17:20 afm46.png
-rw-rw-r-- 1 sfmqrb sfmqrb   416305 Sep  6 17:20 afm46_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb      704 Sep  6 18:11 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  5157031 Sep  6 18:05 aiw.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    76489 Sep  6 17:24 bqt1237_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   362419 Sep  6 17:50 bqt1583_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   456331 Sep  6 16:54 bqt1594_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2824 Sep  6 16:59 bqt83_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   703015 Sep  6 17:50 bqt_fn4.png
-rw-rw-r-- 1 sfmqrb sfmqrb   299015 Sep  6 17:50 bqt_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   325427 Sep  6 17:50 bqt_n552.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   315487 Sep  6 17:50 bqt_n553.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   330101 Sep  6 17:50 bqt_n554.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   560485 Sep  6 17:53 bqtv2_650_s.png
-rw-rw-r-- 1 sfmqrb sfmqrb   541712 Sep  6 17:53 bqtv2_651_s.png
-rw-rw-r-- 1 sfmqrb sfmqrb   729454 Sep  6 17:53 bqtv2_n650.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   702551 Sep  6 17:53 bqtv2_n651.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   100817 Sep  6 17:36 bqt_v3_111.png
-rw-rw-r-- 1 sfmqrb sfmqrb   110820 Sep  6 17:36 bqt_v3_112.png
-rw-rw-r-- 1 sfmqrb sfmqrb    91526 Sep  6 16:59 bqt_v3_83.png
-rw-rw-r-- 1 sfmqrb sfmqrb   137595 Sep  6 18:10 buck2.txt
-rw-rw-r-- 1 sfmqrb sfmqrb      146 Sep  6 18:10 buck3.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    64531 Sep  6 16:53 build261.py
-rw-rw-r-- 1 sfmqrb sfmqrb    60498 Sep  6 17:11 build269.py
-rw-rw-r-- 1 sfmqrb sfmqrb    97300 Sep  6 17:16 build270.py
-rw-rw-r-- 1 sfmqrb sfmqrb    52615 Sep  6 17:36 build275.py
-rw-rw-r-- 1 sfmqrb sfmqrb    74145 Sep  6 17:43 build278.py
-rw-rw-r-- 1 sfmqrb sfmqrb    72342 Sep  6 17:58 build283.py
-rw-rw-r-- 1 sfmqrb sfmqrb     5043 Sep  6 17:05 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3501 Sep  6 17:05 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56424 Sep  6 17:05 c3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78058 Sep  6 17:05 c4.png
-rw-rw-r-- 1 sfmqrb sfmqrb 60831599 Sep  6 18:01 cad_k.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  2530822 Sep  6 18:01 cad_k.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    37980 Sep  6 17:16 c_av.png
-rw-rw-r-- 1 sfmqrb sfmqrb    29703 Sep  6 17:16 c_cros.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1174 Sep  6 17:16 c_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb    95615 Sep  6 16:39 coord_pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb  8373934 Sep  6 18:09 cpd.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb   378445 Sep  6 18:09 cpd.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     4560 Sep  6 16:39 crop_ak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4014 Sep  6 16:39 crop_ak.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25373 Sep  6 16:42 crop_alk.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24852 Sep  6 17:04 crop_fr269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    43238 Sep  6 16:55 crop_germ269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    51654 Sep  6 17:04 crop_gk269.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2585 Sep  6 17:05 crop_gk271.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64142 Sep  6 17:02 crop_gr267.png
-rw-rw-r-- 1 sfmqrb sfmqrb     6411 Sep  6 16:39 crop_gr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    23559 Sep  6 16:42 crop_kohul.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59386 Sep  6 16:39 crop_lat2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    51357 Sep  6 16:55 crop_latin269.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4761 Sep  6 16:39 crop_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3974 Sep  6 16:37 crop_me2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3300 Sep  6 16:37 crop_me.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10236 Sep  6 16:39 crop_op2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4935 Sep  6 16:37 crop_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5599 Sep  6 16:37 crop_pers.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22007 Sep  6 17:10 crop_sak.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5110 Sep  6 17:10 crop_sax.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4854 Sep  6 17:10 crop_shekar.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1249 Sep  6 17:05 crop_sirish.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30419 Sep  6 17:02 crop_skt267.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10043 Sep  6 16:58 crop_slav.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24463 Sep  6 16:58 crop_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  2144625 Sep  6 17:55 dmmpp.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    31044 Sep  6 17:50 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17126 Sep  6 17:54 e1.json
-rw-rw-r-- 1 sfmqrb sfmqrb    18004 Sep  6 17:56 e2.json
-rw-rw-r-- 1 sfmqrb sfmqrb  5301166 Sep  6 17:01 ediv.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  1773345 Sep  6 17:01 ediv.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1845041 Sep  6 18:04 gharib.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  3698758 Sep  6 17:50 IEC_full_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb      228 Sep  6 16:34 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb     4265 Sep  6 17:53 kapi_script.png
-rw-rw-r-- 1 sfmqrb sfmqrb   944060 Sep  6 18:06 kent_full.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   288525 Sep  6 18:07 kent_n222.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   285652 Sep  6 18:07 kent_n223.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   282304 Sep  6 18:07 kent_n224.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   268920 Sep  6 18:07 kent_n225.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb     1433 Sep  6 16:45 merge262.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63035 Sep  6 16:56 mk265.py
-rw-rw-r-- 1 sfmqrb sfmqrb    73111 Sep  6 17:13 mk267.py
-rw-rw-r-- 1 sfmqrb sfmqrb    71564 Sep  6 17:08 mk268.py
-rw-rw-r-- 1 sfmqrb sfmqrb    41609 Sep  6 17:31 mk274.py
-rw-rw-r-- 1 sfmqrb sfmqrb    51778 Sep  6 17:32 mk276.py
-rw-rw-r-- 1 sfmqrb sfmqrb    46494 Sep  6 17:52 mk279.py
-rw-rw-r-- 1 sfmqrb sfmqrb    16605 Sep  6 17:54 mk280b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    17667 Sep  6 17:56 mk280c.py
-rw-rw-r-- 1 sfmqrb sfmqrb    43177 Sep  6 17:50 mk280.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58322 Sep  6 17:51 mk282.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63940 Sep  6 18:05 mk285.py
-rw-rw-r-- 1 sfmqrb sfmqrb    67974 Sep  6 18:09 mk286.py
-rw-rw-r-- 1 sfmqrb sfmqrb    60646 Sep  6 18:11 mk287.py
-rw-rw-r-- 1 sfmqrb sfmqrb  8373934 Sep  6 17:00 mk.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb   378445 Sep  6 17:00 mk.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    11601 Sep  6 16:42 p262-g01.json
-rw-rw-r-- 1 sfmqrb sfmqrb    10625 Sep  6 16:43 p262-g02.json
-rw-rw-r-- 1 sfmqrb sfmqrb    19393 Sep  6 16:46 p262-g03.json
-rw-rw-r-- 1 sfmqrb sfmqrb    19959 Sep  6 16:44 p262-g04.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12063 Sep  6 16:43 p262-g05.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12051 Sep  6 16:44 p262-g06.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12737 Sep  6 16:44 p262-g07.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17259 Sep  6 16:46 p262-g08.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17820 Sep  6 16:53 p262-g09.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17855 Sep  6 16:45 p262-g10.json
-rw-rw-r-- 1 sfmqrb sfmqrb    14983 Sep  6 16:44 p262-g11.json
-rw-rw-r-- 1 sfmqrb sfmqrb    25352 Sep  6 16:46 p262-g12.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17745 Sep  6 16:44 p262-g13.json
-rw-rw-r-- 1 sfmqrb sfmqrb   105748 Sep  6 16:39 p263hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5565 Sep  6 17:22 p275_krei_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53703 Sep  6 17:22 p275_pahlavi.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7106 Sep  6 17:34 p279_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb    12970 Sep  6 17:34 p279_word.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3647 Sep  6 17:34 p279_xsaeta.png
-rw-rw-r-- 1 sfmqrb sfmqrb   130651 Sep  6 17:48 p283_arrow.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:02 p284
-rw-rw-r-- 1 sfmqrb sfmqrb    43108 Sep  6 17:51 p284_e0_fa.png
-rw-rw-r-- 1 sfmqrb sfmqrb    89734 Sep  6 17:51 p284_e0.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59639 Sep  6 17:48 p284_e2b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   106502 Sep  6 17:48 p284_e2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    54419 Sep  6 18:05 p289_labibi.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1476 Sep  6 18:11 p291_esfand.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31043 Sep  6 18:11 p291_root.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66777 Sep  6 16:42 pg261.png
-rw-rw-r-- 1 sfmqrb sfmqrb    84660 Sep  6 16:39 pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71156 Sep  6 16:38 pg263.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92930 Sep  6 16:37 pg264hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57862 Sep  6 16:35 pg264.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13324 Sep  6 16:57 pg265_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86370 Sep  6 16:57 pg265.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79922 Sep  6 16:42 pg266.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70622 Sep  6 16:56 pg267.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69592 Sep  6 16:52 pg268.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71754 Sep  6 16:55 pg269.png
-rw-rw-r-- 1 sfmqrb sfmqrb   122626 Sep  6 16:58 pg270hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    87489 Sep  6 16:55 pg270.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115300 Sep  6 17:05 pg271hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66696 Sep  6 17:04 pg271.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68566 Sep  6 16:58 pg272.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66829 Sep  6 17:28 pg273_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   157304 Sep  6 17:10 pg273hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70615 Sep  6 17:27 pg273.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65586 Sep  6 17:18 pg274.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80338 Sep  6 17:21 pg275.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76740 Sep  6 17:15 pg276.png
-rw-rw-r-- 1 sfmqrb sfmqrb    44171 Sep  6 17:16 pg277.png
-rw-rw-r-- 1 sfmqrb sfmqrb    89267 Sep  6 17:26 pg278.png
-rw-rw-r-- 1 sfmqrb sfmqrb   168655 Sep  6 17:34 pg279hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75777 Sep  6 17:34 pg279.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82065 Sep  6 17:34 pg280.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61535 Sep  6 17:39 pg281.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70575 Sep  6 17:34 pg282.png
-rw-rw-r-- 1 sfmqrb sfmqrb    74784 Sep  6 17:47 pg283.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81024 Sep  6 17:50 pg284hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81024 Sep  6 17:51 pg284.png
-rw-rw-r-- 1 sfmqrb sfmqrb   144566 Sep  6 17:49 pg284_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    84487 Sep  6 17:53 pg285.png
-rw-rw-r-- 1 sfmqrb sfmqrb   106264 Sep  6 17:53 pg286hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76099 Sep  6 18:10 pg286.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72442 Sep  6 17:59 pg287.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53847 Sep  6 17:58 pg288.png
-rw-rw-r-- 1 sfmqrb sfmqrb    90831 Sep  6 18:04 pg289.png
-rw-rw-r-- 1 sfmqrb sfmqrb   105586 Sep  6 18:11 pg291hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70592 Sep  6 18:10 pg291.png
-rw-rw-r-- 1 sfmqrb sfmqrb   103438 Sep  6 18:12 pg292.png
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1548.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1549.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1550.jpg
```


### [2026-09-06T22:12:32.034Z] TOOL RESULT

```
=== AHM around 184 ===
232:Liiders’ clear-sighted insistence an what had previously Seen understood only perfunctorily, the dominant role of Truth in Indo-Iranian religion, has enadled him to present Varuna in a new and immediately convincing perspective. Because transcendental Truth is situated in a primordial spring inside the highest heaven, water everywhere is the ‘womb of Truth’ (pp. 25 sq.). This is why also Varuna, the guardian of Truth, is to be found in the waters. Accordingly the ancient Indo-Aryans swore their aaths by water, invoking Varuna, who was present in the water to guard Truth and witness the validity of the oath (pp. 28, 30 sq.}. Thus Liiders was able to penetrate to the essential definition of Varuna as the god of oath (Hidgatt), which provides the clue to his character of an avenger of falsehood, and to the spies and thousand eyes by which he detects the infringers of Truth. In addition, as Varuna had his seat in the waters, where Truth is situated, he was bound to take charge of them; in the naturalistic interpretation of the Vedic pantheon he thus Secame a water-gad.
292:Let us try to imagine how Darius might have acquired what notions he seems to have had of ZarathuStra’s religion. Brought up far from Aryana Vaéjah,} very likely unfamiliar with the Gathic language, surrounded by Magian priests who would oppose any religious reform, Darius, one would think, obtained his Zara- thuStrian initiation from a second-hand source. As this must have been one he particularly trusted, we may avail ourselves of informa- tion given by Herodotus (1, 299 sgq.), which has not hitherto deen used in this connection: when in his fatal campaign against the Massagetae Cyrus had crossed the Araxes, the suspicion arose in him that Darius, who deing scarcely twenty years old had been left behind in Persis, was plotting against his crown; Cyrus revealed his suspicion ta Hystaspes, who at once recrossed the Araxes and returned to Persis to keep watch on his son; shortly afterwards Cyrus fell in battle.
322:The history of early Zoroastrianism can now de seen as a give- and-take game played Sy the Zarathustrian priesthood of Aryana Vaéjah on the one hand and the Magi on the other. The original Zarathustrian doctrine was introduced by Darius into Western Iran as Mazdahism. The Magi, perhas grudgingly, accorded it an important place beside their traditional cults. ‘Their eclectic stand- point gradually prevailed, and weakened the loyalty ta Mazdah of the royal house. Eventually Artaxerxes I, or at the latest Artaxerxes I], officially came down on the side of the Magi. The reaction of the ZarathuStrian priests was resourceful in the extreme. They adopted the eclectic standpoint, and by intensive literary activity converted it into a system purporting to be ZarathuStra’s. The logical weakness of the system was no a¥stacle to its success; . its compilation was not a case of thinking out what would persuade, but merely of reproducing what everybody Selieved or was ready to believe, and giving it a semlance of unity. Thus the Magi were defeated at their own game. What they had exported as a plurality of cults and Seliefs came back to them as Zoroastrianism: the same religious situation, in the one case a juxtaposition of loose ends and bits, with at most the description ‘Iranian’ toa hold it together, in the other, a ‘system’ exploiting to the full the propagandistic value of ZarathuStra’s authority, whose fame was growing the more he receded into legendary antiquity.
323:There was only one remedy the Magi could adopt, short of committing suicide; by resorting ta it they in the long run despoiled the Zarathustrian priests of the fruits of their toils, and turned defeat into victory: they declared Zarathustra to have been a Magus, and claimed ta be the true heirs and custodians of his doctrine. This was most likely the occasion when the legend was invented, reported in Pahlavi and some classical sources, that Zoroaster’s native place was in Media, the homeland of the Magi (cf. Jackson, Zoroaster, 139 sqq.). Once adopted in self-defence by the Magi as their chief credential, Zoroaster’s name became
326:famous throughout Western Asia, and soon penetrated to the Greeks, If we array our facts and theory around the year 441 as the date when the religious mixture was so prominently advertised as to induce the ZarathuStrian priests to provide it with a scripture, we may expect that by the end of the fifth century the Magi will have been driven to acknowledging Zoroaster as their prophet. This dating squares well with the familiarity of fourth-century Greeks with Zoroaster’s name, and Herodotus’ failure to mention it.} To Persian Mazdayasnians, of course, the prophet’s name was well known long before the Magi usurped it, as the use of the name Spitamas in the time of Artaxerxes I shows (see Henning, Zor. 28, n. I). But foreign odservers could not be expected to penetrate to the remote origins of what was merely one of the numerous Persian cults, To them the Persian religion quite rightly consisted in what the Magi did and said, and they became aware of Zoroaster’s importance only after the Magi cared to assure them of it.
411:+ Thus A. Pagliars, Oriental Studies... Pavry, p. 381, according ta whom the liberation of the cows accomplished in the Rigveda by Indra after the slaying of Vitra ‘is attributed in the Avesta to Mithras (Yaat x 85-6)’. In fact nothing in sts. 35 sg. suggests Indra’s mythicized, symbolical liberation of rain-cloud cows: solid, terrestrial cows, proasaically captured by ‘awners of Falsehood’ who, false to the treaty, had abducted them, as in st. 33, implore Mithra to came to their rescue. If he did listen to their call, all he had to do was to knack down the
479:With Mithra, as with every complicated problem, discrimination is the essential condition of progress. This chapter may therefore fittingly end with a belated triute to the discrimination of Antoine Meillet, who saw through the maze of conflicting data, and with unerring precision estalished that Mithra’s original campetence was the contract, and nothing else (FAs. 1997, 1, 143 sqq7.). What delayed acceptance of Meillet’s unanswerable case must have been his mild insistence on etymological considerations. In matters of religious history linguistic arguments are so distrusted that they
514:Accordingly, one dasic difference between Zarathuatrians and the supporters of the ancient pantheon came to consist in this, that the former worshipped as only 9d Ahura Mazdah, whereas for the latter Ahura, not entirely Mazdah, was one 20d among many they cherished. Thus we understand why the famous dvandva became midva ahura, and not *mi3ra mazda. Thus we also understand the distinction which occupied Benveniste (see below, p. 169, n. f), between the Avestan epithets mazdadaia- ‘created by Mazdah’, and ahuraSata- ‘created by Ahura’, of which the latter is only applied to varadrayna- ‘victoriousness’ (and its hypostasis, the god Vorodrayna), and zam- ‘earth’. The compound ahuradata-, like the compound mi3ra ahura, contains a fossilized reference to the dis- carded Iranian *Vouruna, who was evidently regarded as having created both Vorodrayna and the earth.
515:As time went by, and Mazdah gained in venerability through becoming older and ever more widely accepted, even the pan- theistic sects probably came to believe that their god Ahura was Mazdah, and the difference outlined above was reduced to one between monotheistic and pantheistic Mazdahians. Thus in Aryana Vaéjah there developed a religious situation similar to the one we have assumed for Persis (cf. above, p. 19), except with regard to the priests in charge of it. In Persis the same priests officiated for all sects, thereby giving the sects the superficial appearance of belong- ing to a single religion, whereas in Aryana Vaéjah the Zarathu8trian priests remained loyal to monotheistic Mazdahism until under the impact of developments in Western Iran they translated the exist- ing religious situation into terms of a ‘Zorgastrian’ church and scripture, which included also pantheistic Mazdahtsm.
526:It is worth dwelling for a moment 9n the initial statement of the Yast that Mazdah created Mithra and made him as great as himself, Mazdah’s creation of Mithra is a belief which, if we substitute Varuna for Mazdah, may well go 4ack to the prehistory of the two gods; for it agrees with the Rigvedic position that although the two gods are, as Liiders put it, “homogeneous’ (see above, p. 7), yet Mithra is inferior to Varuna. On the other hand the homogeneity of the two gods, and Mithra’s precedence in the dvandva midra ahura, may have Seen the reasons why in some respects Mithra came to surpass Ahura Mazdah, It is true that the description of Mithra as mazisto yazato in st. 142 is ndt an unequivocal indication of the god’s supremacy; for although most translators render it by ‘the greatest god’, Lommel’s interpretation of it as meaning ‘the very great god’ provides a plausible contrast with the formula mazists yazatangm ‘the greatest of the gods’, which in Yz 17.6 is applied to Ahura Mazdah. But absolute supremacy is accorded ta Mithra in matters of insight, endowment of fortune, and sheer physical prowess. On his insight see p. 43 above. Of fortune he has or gives more than any other supernatural god; he both grants (sts. 16, 198) and diverts it (st. 27). As regards physical qualities he is the mightiest, strongest, most mobile, fastest, and most
531:On the other hand it should be noted that while Ahura Mazdah is in Yt 17.6 not only maazzsta ‘the greatest’, but also vahisia yaszatangm ‘the best of the gods’, Mithra, as we saw (p. 39), is ‘both wicked and very good’ (ak vahistasca) to countries and men (st. 29), Perhaps we may say that compared with Ahura Mazdah, who is just but preponderantly good, in the sense that he does not personally seek out the wicked for punishment, rather letting them run to their self-appointed doom, Mithra is preponderantly just, and carries out justice himself. Some two or more centuries before aur Yast was composed, we may suppose that Mithraand *Vouruna shared the judgeship (ahii-ratu-shig) of the world, as mentioned above, p. 47. In the Zoroastrian system, however, this judgeship is either shared between Ahura Mazdah and Zarathu&tra, or con- templated only in respect of the empirical world, with Mithra as judge (see st. 92 and note 92°), If one takes into consideration Mithra’s Sogdian title S@mext ‘Judge of the world (or creation)’ (see note 927), as well as his Pahlavi title dataBar ‘judge’ and possibly the Avestan epithet rasnu- (see note 791, (2)), it would seem that, ‘except in secondary partnership with Zarathustra, Ahura’s share of the judgeship, viz. that of the supernatural world, was in time allowed to lapse. A possible reason may have been that in supernature there is little scope for a judge, so that Mithra, the fully employed judge of the empirical world, came eventually to be thought of as the divine judge par excellence. In this capacity not anly is the Avestan Mithra accompanied by the hypastasis of Justice (Arstat, see note 139"), but has himself the necessary insight (xratu-) to pass equitable judgement, and the physical skill to execute it. Though ‘wicked’ when necessary, Mithra is not always inexorable; he is merciful (st. 149), and joins his worshippers ‘for
560:Mainyu. Thus Sgenta Mainyu’s original name became a rarely used epithet of his.
563:Qnce it is agreed that the first element of the dvandva payii 9worastara is Mithra, the relative sentence ya vispa Iwarasatd daman ‘the two who fashioned all creatures’ (Y 57.2, see above, p. 54) acquires special significance, as it seems to foreshadow the later, Persian conception of Mithra as a Snpeovpyds (see above, >. 41). The Vedic Mitra, through forming the intimate association with Varuna of which the dvandva mitrdvarund is the label, came to have a share in Varuna’s control of the waters (cf. above, p. 39, and Liiders, 9). cit. 51, n. 19). Similarly Mithra the payu-, through his dvandva association with the ‘fashioner’, of whom alone it could truly Se said that ‘he fashioned all creatures’, came to have a share in Spanta Mainyu’s creative activity. Understandably enough the Syproupyds side of Mithra does not appear in the Mithra Ya&t or in any other of the Avestan references ta the god which derive fram genuine Mithra worship. To genuine Mithra worshippers, that is, pantheistic Mazdahians, the thought af combining Mithra with Sponta Mainyu instead of Ahura would seem an unattractive
604:We have also scen that Mithras’ role of a life-giver is anticipated by three Avestan cpithets 9f Mithra (see above, pp. 32 5q.). These, however, same scholars will consider insufficient explanation of the behaviour of the Roman Mithras, whose life-giving function is most forcefully expressed in the central scene of mast Mithraic reliefs: as Mithras kills the (primordial?) bull, sperm is emitted by the dying animal (Cumont, 1, 299, No. 25, cf. 1, 190), and ears of corn sprout from its tail (Cumont, 1, 186 sq.). Let us first state our view on how this legend came to be connected with Mithras. It is basically Cumant’s view that the legend is a Mithraic version of Ahriman's murder of the primordial bull. Cumont, however, did not commit himself as to which of the two versions was the original one, no doudt because he had not realized the implication of the three Avestan epithets we have quoted.
628:The above theory on the clever camsuilage of Mithra perpetrated by the authors of the Avesta is part and parcel of the madern trend in Iranian religious studies always to suspect that the Avesta either conceals the truth or tells the untruth, and that it is so artificial a scripture, so little based on the realities of the religious life of ardinary men and women, that its authors could permit themselves whatever arbitrary combination, distortion, or suppression crossed their fancy. It must be said in fairness that Lommel, who by his book Die Religion Zarathustras, and his careful translation of the Yats, has contriyuted more than any other living author to a balanced and sound understanding of the Zoroastrian religion, does not otherwise take such a sceptical view of the truthfulness of the scripture of the religion of Truth. It is an irony that little else Dut this theory, out of a book which is packed with pene- trating and sober observations on the Zoroastrian religion, has caught the imagination of presemt-day religious historians; the greater part of that thoughtful book seems to have passed unnoticed.
1097:37. Then grass-land magnate Mithra cames to the assist- ance of that (invoker) by whom he has been propitiated; Sut of him who has antagonized grass-land magnate Mithra he destroys (respectively [¢f. 83 sg.]) the house, the clan, the tribe, the country, and the empire (dit. command of countries)! (Here repeat 4-4.)
1174:natural Mithra speaks ga0d words; there is no material man in existence who cammits evil deeds to (so) great an extent as supernatural Mithra performs good deeds;
1202:113. may he therefore came to our assistance, O exalted Mithra and Ahura! When loudly resound the whip and the neighing? of horses, when the whips are tossing,? the bow-strings twanging(?), the sharp arrows‘ darting, then the evil sons of those who have offered viscid (Zt. heavy) libations (=libations of Slood), having been struck, will go down writhing.® .
1341:The somewhat uncouth translation ‘grass-land magnate’ has een chosen mainly because of its comparative brevity. That the unusual length and heaviness of this constant epithet of Mithra became in time inconvenient even to ardent devotees of the gad can be inferred from the epithet Cautes of the Roman Mithras, which in my opinion is the result of a haplological reduction of Olr. *gauyauti- to *zauyti, with sudsequent disappearance of y, and with initial & as in Gr. xavvdxn(s) beside yauvaxys < Olr. *zaunaka- (cf. Liiders, APAW, 1936, No. 3, 7 59¢.).
1399:Much ingenuity has been spent in trying to clarify the relation between the first component of vara9va-yna- (etc.) and the simple !varadra-, for both of which the Pahl. translators used the same word érazkarih ‘victory’. But the difficulties remain. Bth, had to attribute to 1varaIra- the meaning ‘attack’ in order ta be able to analyse varaIrayna- as ‘smashing the attack’, and for the sake of one passage (Y? 13.38, quoted in note 38? below); in the other passages, however, he used for !osra9ra- ‘victorious attack, victory’. He did not attempt ta explain how the ‘attack’, permanently beaten in vara9rayna-, came to be ‘victorious’, Benv. assumed that ‘vara9ra- meant ‘defence, resistance’, yet he also admitted a derivative meaning, that of ‘hostility’ (9. c##. 10 sq.), Again the semantic development arouses misgivings: one does not see why the ancient Iranians should have considered the defence against an aggressor, rather than the latter’s attack, an act of hostility.
1429:A word must de added on the (5) sentence of Yt 13.46, which M. Benv. is scarcely right in connecting closely with what precedes. This sentence to my mind introduces a new trend of thought, which is developed in Yt 13.47, where the sudject yatara refers to the warriors of each of two countries (as can be seen from the parallel st. g of the Mithra Ya8t, and from the reference to ‘countries’ at the deginning of Yt 13.43): warriors normally propitiate the Fravaiis before engaging in cam}at; if, however, they belong to two countries at war with each other, then the Fravaiis lend their su99rt to that side which is first in performing the propitiatian.
1471:If now we inquire how it came to pass that the zender of the term amasa spanta is masculine, when none of the six Entities of the graup Selongs ta this gender, the obvious answer ts that the YAv. reference to the group as ‘the seven incremental Immortals’ (hapta amasd spanta) represents the original state of affairs; seside the three neuter and three fem. Entities the graup must have 9riginally included one masc, Entity, and since this Entity determined the gender of the collective name
1541:Afonz, as defined by my Digor friend, indicates a definite time, in contrast with raste#g, which refers ta time in general. Examples: restxg min yes ‘I have time’ (not *afonz min yes), znafani ma zrbaco ‘do not came at the improper time’ (not *znzxrzstxgi); di afone’y ‘what is the time?’; & restzgey ‘what time is now (summer or wiater)?’; znzlisag serdtan afoni nimedzez ‘British Summer Time’; x afone ku zrqerttzy (Tamamuuru, I, 10.21)= Iron yx afon ka ’reidi (Narti Kadzdsitz 53.3) ‘when its time§ arrived’ ; Iran zrtz afon ‘three times’ (colloquial, = ‘for a long time’), Iron Adszemon Sfzldistad 46.17; Iron zmzx nz dalconzn erceun afon kung ma i ‘it is not yet time for our traveller ta come back’, V. Miller, Ocemunenue amrodvi, I, 22.17.|| This definition of afon(x) supports the praposed etymological connection with afzdsz/afzy ‘year’, viz. a definite span of time, and is in harmony with the Av. epithet fratwarstsm ‘aypainted, exactly defined’, which qualifies afontam in the formula quoted above.§
1615:(3) the adj. paiti.sinda- in Y 33.5: apasé% va...avaacama vahista srabitd ava v3 vanuhif ratai} darayd. bazdus naka paiti.vyada paiti.sinda ‘Und euch, Wasser, .. die... besten (und) schdnsten, herad rufen wir, ihr guten, mittelst der langarmigen Opferspende, (die thr) im Ungliick (nasa) Vergeltung iibend (paiti.vyada) Abhilfe schaift (paitt.sindd)’ (Wo.). The ‘calamities’ (nas, loc. pl.) are uncalled for at this juncture, the gen. ratais darayd. bazaus is left hanging in the air, and vyadz- else- where means ‘reward, thanks’. Tie difficulties disappear if we interpret paiti.vyadd as ‘grateful’, and nasa as belonging not to Mwas- ‘to perish’ but ta 2xas- ‘to attain’, hence ‘what is attained, obtained, =share’, cf. Ved. diinasa ‘unattainadle’; ratais will then depend on nasa. Translate: ‘we call you down...(ta be =show yourself) grateful for, and pleased with, the (=your) shares ¢ of the long-armed sacrificial offering’.
1616:25%. tanumaira- according to Bth. (and Duch., Comp. 155) has tanu- virtually in the loc., ‘having the ma@ra- in his Sody (person), with whose body (person) the m. is connected, who has adsorbed it, has became one with it’. If this lengthy explanation were correct, one might reasonably expect to find the epithet applied to Ahura Mazdah, since the m@@ra- is — Mazdah’s ‘soul’ according to Yt 13.381, Vend. 19.14. Yet tanumatra- is only found as epithet of Mithra and Srao$a, and of men. Moreover, its counterpart tanu.drug- (drvant3 tanu.druji, Vend. 15.18) is equally unlikely to contain a virtual loc.: the ‘Drug inthe body’ would suggest the demon of putrefaction (cf. W3. 78o.2-11}, rather than the demon Falsehood who bedevils the ‘owners of Falsehaad’.
1619:t Wn., 11, 1, 27% top, translates ‘whose hair are trees’, but defines like Macdonell: it is the second member of the campound which provides the figurative term of the identification. Such dahuvrihis are for Wn. adjectivized tatpurusas of the type mukha-candra ‘a mouth which is like the moan, a moan- mouth’. tanu.drug- and tanu.ma@ra- are similarly understandable as displaying attributive usage of determinative compaunds meaning ‘a drug- person (body)’, ‘a ma9ra- person (Sody)’, respectively.
1649:Vorrat’ (Lo.), The assumed base of mane is thus either Aay- ‘to heap up’, or kay- ‘to repay'. Benv., Znf. 50, without himself pronouncing on the base, rejects 3th.’s interpretation of the form as an infinitive, and Pasits a nominal stem. ciman-, with long d@ as in pudrane (on which see above, note 24°), This stem I would analyse as an -an- extension (cf. uxine, Benv., 09. cit. 51) of the Olr. base *éam- ‘to sip, drink’, cf. Skt. camatz, NPers, éant, camidan: Mithra collects the libations in his chariot (see st. 136) and takes them ta his abode in Paradise (see note 501), where he consumes them at leisure. [See Addenda.]
1663:345. It is generally held that the Aavi-s of the present formula and the kavi-s collectively branded by Zarathu8tra in his Gathas were princes or rulers (see A. Christensen, Les Kayanides, 9 5q.).¢ This assumption implies three distinct meanings of the ward Aav-, or an unproven development in three stages: (1) OInd. kav, a wise composer of hymns;{ (2) Av. Ravi-, members of a class of rulers badly spoken of, because they protected religions, or a religion, opposed to Zarathustra’s preaching; and (3) Av. Ravi-, title of a dynasty well spoken of, because Vi8taspa, the last holder of the title, adapted ZarathuStra’s religion. The situation gains in plausibility if we eliminate the second link in this chain. In the Gathic kavi-s, mentioned on a par with Aarapan-s and usig-s, who are agreed to have been respective members of two priestly classes, we may as well recognize the Iranian counterparts of the Vedic Aavi-s: camposers af hymns to various gods, who in additioz had perhags assumed certain priestly functions; they would incur ZarathuStra’s disapproval because of their insistence on the traditional Indo-Iranian ritual. One particular family of kavi-s, whose home was in Sistdn, rase to temporal power and came to rule over the Chorasmian state or part of it; this family used the professional description Aavi as personal dynastic surname. Zarathustra, in addressing his protector as Kavi Vist#sa2, would not associate the king’s dynastic name with the class-name of the priestly hymn-writers
1668:(‘hymn-mongers’ to him) who were Sent an frustrating his religious reform, any more than we are apt to think of parsons when addressing Mr John Parson. One is reminded of the 3armecide family, which, as H. W. Bailey has shown (BSOAS, x1, 2), was named after the head of a vihara, sramukha.t In later times, when the Kavis had taken their place in the remote legendary history of Iran, their title assumed a wider meaning, cf. Christensen, 99. cit. 61, In Zoraastrian Middle Persian literature kavis are associated with heroes, cf. Rayan u yalan, Gt. Bd. 177.10, cf, Da., ZA, I, 319, 0. 132, and Gt. Bd. 75.15 (reference kindly supplied by H. W. Bailey, who suggests viran as a possible alternative to the reading yalan) ; in Manicheism the kavis became ‘giants’, see Henning, BSOAS, x1, 53 sq.; Chr. Sogd. pr qwy’g, Hansen, AAWL, 1954, 843.37, 375.16, translates Syriac gandava'i) ‘fortiter’, lit. ‘in a manly way, heroically’, thus indicating that the abstract gwy’g ‘Kavi-ism’ means ‘heroism’. Cf. also the draff-i kavyan, Christensen, L’ ran sous les Sassanides, 562, 0. 5.
1696:As regards «riima- already Lo. queryingly compared Av. paxruma- (Die Yast's, 115, n. 4), which I suggested in RAS, 1942, 101, should be connected with Sogd. xrwm, xwrm ‘earth, sail’, cf, also Bailey, TPS, 1945, 34 This suggestion was taken up by Hef, P- 429, and extended to wrimd and xriimim in the present stanza. xrama was for Hf. ‘loc, or instr. of the noun’, and xrimrya- ‘earthy in the sense of sandy or stony’; hence he translated lines 5 sg. ‘the cattle, ..is driven the stony way. of captivity’. One may hazard the opinion that xrima-,} as a derivative of the base *kreu- ‘to collayse, break up’ (Pokorny, IEW, 522 sq.), means ‘crumbling’; substantivized as a neuter, ‘the crumbling (substance)’ Kar’ e€oyjv came to mean ‘soil, earth, dust’; from this noun a further adj. sxriimya- was derived, see nate 38+,
```


## [2026-09-06T22:12:37.517Z] TOOL CALL #14: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/292.jpg"
}
```


### [2026-09-06T22:12:37.537Z] TOOL RESULT

```

```


## [2026-09-06T22:12:38.137Z] TOOL CALL #15: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(json.dumps(d['AHM'],ensure_ascii=False,indent=1))\""
}
```


### [2026-09-06T22:12:39.696Z] TOOL RESULT

```
{
 "title": "I. Gershevitch, The Avestan Hymn to Mithra, Cambridge 1959",
 "edition_found": "1959",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/gershevitch-ilya-the-avestan-hymn-to-mithra-cambridge-university",
 "identifier": "gershevitch-ilya-the-avestan-hymn-to-mithra-cambridge-university",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHM.txt",
 "page_offset": "leaf = printed + 14 (e.g. leaf 18 = p.4). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Commentary is by stanza/note number; the Glossary (end of book) lists Avestan words. grep the Avestan word in transliteration.",
 "notes": ""
}
```


## [2026-09-06T22:12:55.877Z] TOOL CALL #16: Bash

```json
{
 "command": "grep -rl '\"Kwen\\|\"Kwem' data/extracted/batch/*.json | head; echo \"---roots---\"; python3 - <<'EOF'\nimport glob,json\nfor f in sorted(glob.glob('data/extracted/batch/page-*.json')):\n    d=json.load(open(f))\n    for e in d['entries']:\n        n=e['root'].get('name','')\n        if n.lower().startswith('kwe') or n.lower().startswith('kwer') or n.lower().startswith('qwer'):\n            print(f.split('/')[-1], n, e['root'].get('gloss'), e['root'].get('refs'), e['root'].get('redirect'), 'part',e.get('part'))\nEOF"
}
```


## [2026-09-06T22:12:57.592Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndata=open('AHM.txt',encoding='utf-8',errors='replace').read()\npages=data.split('\\f')\nfor i,p in enumerate(pages):\n    if \"to sip, drink\" in p or \"camidan\" in p or \"camatz\" in p:\n        print(\"leaf\",i,\"printed\",i-14)\n        print(p[:200].replace('\\n',' | '))\n        print('...')\nEOF"
}
```


### [2026-09-06T22:12:57.800Z] TOOL RESULT

```
data/extracted/batch/page-139.json
data/extracted/batch/page-227.json
data/extracted/batch/page-217.json
data/extracted/batch/page-291.json
data/extracted/batch/page-292.json
---roots---
page-288.json Kwe, Qwe, Kue, Que, Kwi 2 and POK:635 None part None
page-289.json Kwei 1, Qwei, Qwi to pay back, revenge, punish POK:637 None part None
page-289.json Kwei 2, Kwoi to pile up, build, make POK:637 None part None
page-290.json Kweit None None Kuei part None
page-290.json Kwek, Qwek to appear, see, show POK:638 None part None
page-290.json Kwel, Qwel to move around, dwell POK:640 None part 1
page-291.json Kwel, Qwel to, move around, dwell POK:640 None part 2
page-291.json Kwen 1 holy POK:630 None part None
page-292.json Kwen 2 sip, swallow POK:640 None part None
page-292.json Kwer, Qwer to make, form POK:641 None part 1
page-293.json Kwer, Qwer to make, form POK:641 None part 2
page-293.json Kwermi None None Wer 2 part None
page-294.json Kwes to pant, to breathe fast POK:631; CEL6:284 None part None
page-295.json Kwetwer, Qwetwor four POK:642 None part None
page-296.json Kweye, Qweye quiet, comfortable KLN:1740; POK:638 None part None
page-413.json Qwer None None Kwer part None
```


### [2026-09-06T22:13:00.632Z] TOOL RESULT

```
leaf 200 printed 186
t, Lit. ‘.. .(of him [see above, 9. 151, n.f]) who (being a) Truth- owning (man) worships you with prayer in which (your) name is men- tioned with regular utterance, offering libations’. This is the f
...
```


## [2026-09-06T22:13:07.049Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\npages=open('AHM.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (196,197,198,199,200,201):\n    p=pages[i]\n    print(\"=== leaf\",i,\"printed\",i-14,\"len\",len(p))\n    print(p[:400].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-06T22:13:08.926Z] TOOL RESULT

```
=== leaf 196 printed 182 len 3099
naka paiti.vyada paiti.sinda ‘Und euch, Wasser, .. die... besten (und) schdnsten, herad rufen wir, ihr guten, mittelst der langarmigen Opferspende, (die thr) im Ungliick (nasa) Vergeltung iibend (paiti.vyada) Abhilfe schaift (paitt.sindd)’ (Wo.). The ‘calamities’ (nas, loc. pl.) are uncalled for at this juncture, the gen. ratais darayd. bazaus is left hanging in the air, and vyadz- else- where mea
=== leaf 197 printed 183 len 2868
iently ambiguous for Vyé. 1 to carry the late gloss Aahrpa x*sus ‘(your = Vistasza’s) own shape’, x°3us {thus L 5; Pahl. transl. ‘xs, cf. W4%. s.v. xaysus) being the Pazand form which corresponds to Man. MPers. xwy3! (x°23(a)s). | 25°. 5azus.aojah-. Of the four possidle explanations mentioned by Duch., Comp. 15 sq., I prefer the last, ‘graphie d’un b@zaud?, Gen. S2.’, without, however, accepting the
=== leaf 198 printed 184 len 2780
 734.621). For the Sogd. present stem two explanations seem possible: either rx#- (raxn-) is a metathesis of Or. *ranx(a)- (=Av. *rgx(a)-) <LE *lrenk*h-; or rxn- has preserved the 7@/n formative and represents Olr. *raxn(z)-, with *rax- from cither LE *Z/rn*- or *Lfrnkeh-.t [Add.] | 27", paiti...varayeiti, Wi. ‘arevents’; Gdn. ‘obscures’; Lo. ‘con- ceals’; Bth. ‘destroys’; Da. ‘removes’; Bailey ‘kee
=== leaf 199 printed 185 len 2737
th Skt. lakuta ‘club’ (supggasedly < *lakrta) and Tat. lacertus (cf. Walde -Ilofmann, LEW, s.v.) should happen to be correct, one may assume an 7/n alternation *leky-to~ (> Ind. *lakyta-):*leky-to- (> Tyan. | *lzkata-). The Tranian adj, suffix -ata- mentioned by Bailey, 3SOAS, x11, 933, does not belong hete. [Sec Addenda.] | 132 | COMMENTARY [39.1-32.1 | attempted, of Av. sravant-, uda.srvant-, with Pahl.
=== leaf 200 printed 186 len 3121
t, Lit. ‘.. .(of him [see above, 9. 151, n.f]) who (being a) Truth- owning (man) worships you with prayer in which (your) name is men- tioned with regular utterance, offering libations’. This is the full definition af what later on is concisely referred to as midrahe vaxs ‘the utterance of Mithra’, see note 1373, | 32". ham his cimane daranuha ‘trage sie hin zum Sammel-Orte (Cinvat)’ (Wi.); ‘zur Fre
=== leaf 201 printed 187 len 3115
note 925). Other sugzestions for pazti.parsti- are ‘Erfragung’ (Bth.), ‘Erforschen’ (Lo.), ‘Révélation’ (Da.}, ‘Gegen- frage’ (Htl.), ‘Unterricht’ (Wi.). | t vratiyaiy could alternatively be a denominative of vrata-, cf. Bth., GIP, 1, p. 35, §1s2, a, 2. | $I do not see why, to quote Benv., Noms d'agent, 22, patti. fraxétar- ‘doit signifier “qui informe gudliquement” (paralléle & staotar-)’. | 184 | COMMEN
```


## [2026-09-06T22:13:27.167Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1640,1660p' AHM.txt | cut -c1-1500"
}
```


### [2026-09-06T22:13:27.211Z] TOOL RESULT

```
132
COMMENTARY [39.1-32.1
attempted, of Av. sravant-, uda.srvant-, with Pahl. asap, apar astap kar, which respectively translate the Av. words. For asta, Arm. stap, ‘haste, hurry’ (cf. 3th., ZW, 236, n. 3, Henning, ZIJ, 1x, 190; 224) stand ta astap Rar (cf. Pahl. Ps. ’wét’pyaly ‘appressor’) as ‘pressing’ (cf. French presse, Ital. premura, ‘haste, urgency’) to ‘oppressing’, If ‘to press’ is the basic meaning of Soth *stas- and Av. *sru-, we can understand sravatd in F.12 as ‘hurrying’, and zamd...upa.srvatd in Vend. 7.27 as ‘oppres- sive winter’; vekrkdehd sravanhavd, Vend, 13.45, of which the Pahl. transl. is still obscure, can then be taken to mean ‘im ortunate, insistent, harassing, wolves’, cf. Freach pressant. For suggestions on the possible meaning of *srav3-, srava-, we must again turn to French pressant (this time in the sense of ‘urgent’)}, as well as to Ital. premurasoa ‘solicitous’ and Arm. stad ‘diligence, haste, pramptitude, urgency’: srazyana- ‘having bustling, fussing, solicitous, women’; sraara9a- ‘where cars are hurrying (=fast), ar prompt (at the owner’s command)’; srastanii- ‘whose body is impetuous, prompt, of quick motion’; sravassmua- ‘whose thrusts are pressing, impetuous, véhement’, °Ssna- having arisen from compound- thematization (cf. Duch., Comp, 37) of °Samnah- ‘thrust’ (suffix as in rafnah-, tafnah-), cf. anman- ‘thrust’, adove, note 243. Bth.’s etymo- logical connectian of sr(a)vant- with D
30°. mistaratd .spaya-. Since Av. *fraspat- very likely means ‘rug’ (see Henning, BSOAS, x11, 315), the same can Se assumed for the etymo- logically related saaya-. Both wards may belong to Olr. *span- (cf. Av. saya-, 2ita-, to zan-) <IE *(s)pen- (QHG sdinnan, spannan, Arm, henum, etc., cf. Walde-Hofmann, LEW, u, 279 39.). Bth.’s *span- ‘spider’ (postulated for the sake of the gen. sg. and nom. pl, s#na), which would have provided asuitable alternative root for spaya- and °spat- (IE *Ayen-), was eliminated by S. H. Tagizadeh, BSOS, 1x, 321 sqq. A different base is seen in upairi.spat-, see below, note 1255.
30°. nda. barazista-, lit. ‘where cushion-heaps have been deposited (= piled up, cf. “throwing”: “erecting” in OPers., Asia Major (N.S.), 11, 135 sg.)’. I take barazista- as a compound of darasif- ‘cushion’ and sta(y)- ‘heap’, whose only attested form séaii(¢z) als» shows thematic inflection,
gat, Lit. ‘.. .(of him [see above, 9. 151, n.f]) who (being a) Truth- owning (man) worships you with prayer in which (your) name is men- tioned with regular utterance, offering libations’. This is the full definition af what later on is concisely referred to as midrahe vaxs ‘the utterance of Mithra’, see note 1373,
32". ham his cimane daranuha ‘trage sie hin zum Sammel-Orte (Cinvat)’ (Wi.); ‘zur Freude’ (Sai. doudtfully); ‘schreibe sie uns auf rechnunz’ (Gdn.); ‘ramasse-les ensem Ie’ (Da.); ‘sammle sie auf zur Bu3zahlung’ (Bth., followed by Htl.); ‘bring zie zusammen zum
133
32.1-33.2] COMMENTARY
Vorrat’ (Lo.), The assumed base of mane is thus either Aay- ‘to heap up’, or kay- ‘to repay'. Benv., Znf. 50, without himself pronouncing on the base, rejects 3th.’s interpretation of the form as an infinitive, and Pasits a nominal stem. ciman-, with long d@ as in pudrane (on which see above, note 24°), This stem I would analyse as an -an- extension (cf. uxine, Benv., 09. cit. 51) of the Olr. base *éam- ‘to sip, drink’, cf. Skt. camatz, NPers, éant, camidan: Mithra collects the libations in his chariot (see st. 136) and takes them ta his abode in Paradise (see note 501), where he consumes them at leisure. [See Addenda.]
331. urvaiti ddtanam sravanham ‘im Festhaiten an den gegebenen Spriichen’ (Wo.); ‘um des Bundes der gegebenen Verhei3ungen willen’ (Lo.); ‘treu dem gegebenen warte’ (Gdn.). In A 3.3 a layman who has failed in his religious duty is declared a-va¢cd.urvatti- ‘ disqualified from entering a stigulation by mere verbal promise’, cf. vacd.urvati-, Wo. 1343. In our passage the speakers are not so disqualified and consider, accordingly, that the god of Contract is bound to assist them by virtue of the vow they have made to honour him.
urvaiti~ ‘ foedus, fides’, which is etymologically related to Av. urvata-, Ved. wratd ‘vow’, may be of help in the understanding of the OPers. expression aurmzdahd“gm "v'rtryty in Beh, 1v, 44 (as briefly indicated in Olr, Lit. §11). Benv. has recognized that these two words constitute a form of oath: ‘I swear by Ahuramazdah’, BSL, 1951, 35 sqq.; 50. That he was right in treating the long word as a compound ‘ Ahuramazdahian oath’ (better ‘praclamation’), is shown by the El. version, which, as Weissach pointed out (Die Keilinschriften der Achdmeniden, $3, n.), has ‘Ahuramazdahian’, not ‘Ahuramazd3h’. However, the spelling "o'rtiyiy does not favour the reading vartatyazy (which should have been written *Ty'rtyzy) adopted Sy Benv., and the meaning of vart- ‘to turn’ docs nat suit the context. Until proaf to the contrary we may assume that the Indo-Iranian initial group yra- survived unchanged in OPers.; by reading vratiyaty we obtain a dcnominative present stem vrati-ya-, in which vrati- corresponds to Av. urvaiti.t The meaning will then be: ‘I vow, state my (good) faith by, a proclamation (made in the aame) of Ahuramazdah.’
33°. paitd. parsti- ‘interpretation’; cf. OPers. patiprsa-‘ro read’, Man. MPers. phypurs-, Parth. pdowrs-, Sogd. atfs-, Khot. pug- (Bailey, BSOAS, xi, 128), and Av. paiti.fraxstar- ‘interpreter’ (Yi 13.92, quoted below, note 925). Other sugzestions for pazti.parsti- are ‘Erfragung’ (Bth.), ‘Erforschen’ (Lo.), ‘Révélation’ (Da.}, ‘Gegen- frage’ (Htl.), ‘Unterricht’ (Wi.).
t vratiyaiy could alternatively be a denominative of vrata-, cf. Bth., GIP, 1, p. 35, §1s2, a, 2.
$I do not see why, to quote Benv., Noms d'agent, 22, patti. fraxétar- ‘doit signifier “qui informe gudliquement” (paralléle & staotar-)’.
184
COMMENTARY _ §34.1-34.5
34°. framanah-, cf. OInd. pramédnas ‘cheerful’, MPers. prmyn- ‘ta be happy, cheerful’, prvyn adj., Parth. frmnywe ‘hope’, see Mary Boyce, MHC?, 187.
34°. hara93, corrected by Caland to hamara93.
34°. Lines 9-10 must either de read
vandma (vispa thassa vispa thatsa taurvayama,
```


## [2026-09-06T22:13:39.988Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ndef page(f,pr,off):\n    pages=open(f,encoding='utf-8',errors='replace').read().split('\\f')\n    i=pr+off\n    return i,pages[i] if i<len(pages) else 'OOR'\nfor pr in (80,201,28,232):\n    i,t=page('HRN.txt',pr,21)\n    print(\"##### HRN printed\",pr,\"leaf\",i)\n    print(t[:2600])\nEOF"
}
```


### [2026-09-06T22:13:41.571Z] TOOL RESULT

```
##### HRN printed 80 leaf 101
— 80 -
357. 2^^'*^^ ^Handwerk, Gewerbe'.
aw. vergl. pistro- 'Gewerbe*; phlv. pesak.
358. peiyäre 'Tadel' (Sahn. III, 1763, V. 95; 1803, V. 383)^).
aw. "^paiti + 2 [/"gar' (ai. praii + gar- bedeutet auch
nur 'anrufen, begrüssen, antworten).
Spiegel, Ar. Periode, 229.
Bartholomae meint, man könne auch an Ableitung
von ai. prati + [^har- denken (vergl. pratihdrana- und
die Bedeutung von lat. ohjicere), Ai. h entspricht ja
sowohl indogermanischem gji wie g2h,
peiyäni s. peyäm (No. 348).
359. peig (peik) Tussgänger, Häscher, Bote', arab. faij,
aw. "^padika-,
de Lagarde, Ges. Abh. 74; Nöldeke, Tabari-
Übers. 448, Note 2, vergl. auch Denkschr. WAW.
Band 38, 14.
360. peikär, peigär *Kampf'.
aw. *paitikära' vergl. paiti.akerenaot (vd. 2, 6);
phlv. patkär 'Kampf (z. B. vd. 5 (33) GL), patkäritan
'Köcher, (z. B. vd. 4 (137)), patkärok (AV.).
arm. LW. payUar *Kampf' .
361. peiker *Bild'.
Sii^. patikara- 'Bild'; iphlv, patkar (Bund.), arm. LW.
pafker.
362. peikän 'Pfeilspitze, Pfeil'.
aw. paiti -\- [/kan- (?); arm. LW. paikan\daran
de Lagarde, No. 1834.
vergl. serb. LW. pHk 'Pfeilzeichen der fahrenden
Leute (Miklosich, Denkschr. WAW. Band 38, 11);
während peik 'Bote, Laufbursche' (ib. Band 35, 144
und 38, 11) zu np. peik (No. 359) gehört.
363. pei/imiden'mQ^^Gn\ zeigen', Prsies. peimäy-emj peimäny
peimäne^).
*) An der letzten Stelle wie auch sonst (z. B. IIT, 1642, Vers 2,
Calc, 1708, V. 3765) ist in der VuUers-Landauer'schen Ausgabe
h^ in p^ zu ändern.
«) Eine *Masft' (HohlmassJ, z. B. Jnnn ZKM. V, 302.
##### HRN printed 201 leaf 222
— 201 —
Dialektisch (K*ä§än, Q.) bedeutet (jurd, gurdl *hoch,
Höhe'.
900. {lygird (Endung von Ortsnamen).
ap. *-fcf^a-. (Hübschmann, KZ. 27, 112)^); phlv.
^kart, vergl. Därähkart.
Die Ableitung von ap. vardana- (vergl. Mordtmann,
ZDMG. 32, 724) ist unmöglich, da ap. rd im Np. zu
l geworden sein müsste. Np. -verd dagegen in Ablverd
u. a. m. kann nur auf ap. *varta- zurückgehen ; vergl.
-varta^) in indischen Städtenamen (PW. s. v. und
PäninT ed. Böhtlingk-, IV, 2, 126)? Material-
zusanimenstellung bei Blau, ZDMG. 31, 495 flf.; vergl.
dann auch Nöldeke, ZDMG. 33, 144 ff.
901. {2)ffird rund; rings herum (begirdf , girde rundes
Brot* (arab. LW. jardaqat), girdü *Wallnuss'.
ai. vfttä^ gedreht, rund'; phlv. vurtak 'runder Kuchen'
(Papyrus, unsicher; Hörn, ZDMG. 43, 51), gart (vd.
19 (15) für aw. skarena-; Men.).
902. (/ertl *Staub* (ursprünglich 'wirbelnd, sich drehend).
ai. i/'^vart", vdrtatB 'sich drehen .
wa/. LW. gard, minj. y(fräi.
903. ff er den 'Nacken, Hals', gerdene 'Gebirgspass'^).
ap. *vartana', etwa 'Wirbel', zu [/^vart-; phlv. gartan
(vd. 19 (94) Gl.).
LW. kurd. gerdan *Hals'; af^'. bei. (71) gardan
'Nacken, Hals'; wa;^. §iyn. gardan, sar. gardan,
904. gerdün ^Firmament; Wagen.
ai. vartani^ 'Radkreis, Radfelge'.
kurd. LW. gerdün 'Wagen ; oss. värdon * Wagen' (258).
Np. gerdün steht für *gerdan (dasselbe gilt für oss.
>)Hüb8chinann steUt a. a. 0. auch zweifelnd np. sägird *Schüler*
(arm. LW. asakert^ phlv. asökart) hierher, doch geben die Lexikographen
auch vird als 'Schüler' an. Wenn diese Form irgend welchen Wert hat,
80 ist die Etymologie Fr. Müller's, WZKM. 5, 66 unmöglich.
Zu np gird gehört vielleicht auch oss. kärt *Hof* (von Stackel-
berg, Fünf osset. Erz. 82).
*j Oder viti" 'Einzäunung' (?j
') VuUers s. v. g erden (gerdengäfi).
##### HRN printed 28 leaf 49
- 28 -
Die Etymologie stammt von Nöldeke (mündliche
Mitteilung).
121. enderyiur, der^ur (früher: ender /^r) ^passend, an-
gemessen, ender/iird, der/urd, ender/urden ^) (Sahn.
I, 79 Vers 318).
Nöldeke schlägt vor (mündliche Mitteilung), die
Worte an [/^svar- *glänzen anzuschliessen.
122. endöyiteu 'sammeln, erwerben', Praes. endöz-em,
endö/is'^),
phlv. andö/tan, andöcet sammeln, erwerben* (Men.,
AV.).
Siehe unter np. tö/ten (No. 462).
123. euffärden ^glauben, wähnen*, engüsten, Praes. enrjär-
em, engäris^ engäre 'Rechnungsbuch'.
Käs. engöstdn sprechen' (s. v. herf zeden),
aw. hanlcärat/emi j hankere&a-, hankereti- 'Zählung'
(Geldner, KZ. 27. 239 Note 1); phlv. angärtan,
angärttan glauben, zählen' (Men., AV.); ai. 2 i^kar-
gedenken' (?).
oss. d. analuHj aüyalim ^meinen, glauben', t. änqül-
dän *ich vermute* (25); af/. angeral 'denken, sich
einbilden'; kurd. LW. angerin; arm. LW. angarem
'halten für; georg. und Thusch LW. angarisi bezw.
angris 'Rechenschaft' (Hüb seh mann, Osset. Etym.
No. 25)3).
^) Impersonalo.
*) Nur aus einem Verse des fragwürdigen AbuM Ma*änl belegt,
was im Grunde nicht yiel sagen will. Eine andere solche *ünform* ist
phlv. ämöxt(i)sn (aw. äxsö^ y. 45, 2).
^) Über das gr. LW. ayyaoo; ist schon so viel Falsches geschrieben
worden (erst ganz kürzlich hat noch 8. Bugge, BB. 14, 62, ausser
ai. ähgira-, dugiras- und gr. nyyfXo? sogar lat. amhuläre dazu gestellt und
Ceci, Appunti Glottologi, No. 8, vergl. Indog. Forsch. I, Anzeiger 2,
158, ist ihm darin gefolgt), dass es am Platze sein dürfte, hier kurz
auf das Wort einzugehen. Als Grundbedeutung giebt Hesych fQyartjg,
vntjQFTtjZt ax^oifooot; an; arjfjL<xCvfi Sf. xai rov: fx SiwJo^f]'^ ßaaiXixovg yQa/u-
juaTofpogov^. Suidas hat nur die letzte Bedeutung mit dem Hinzufügen
ol (Vf nvToi xai aaiaV^Ti« (lies aaydvdai); vergl. auch Herod. VIII, 98
Tovro To SQuat^jua twv InntJoy xaXh'ovai U^^nai ayyixQiliov, Dazu ayya()fvu)
##### HRN printed 232 leaf 253
— 232 -
1034*>*» niseni *Nest* (Sahn. I, 137 Vers 146), nisemen i).
Doch wohl auch zu np. nisesten (No. 1033), wenn-
schon die Erklärung der Formen schwierig ist. Ge-
hört dazu etwa auch äsyäne *Nest' (No. 35)?
skr. LW. niglmana" (PärasTpr. ed. Weber, No. 433).
1035. neft ^Naphta .
aw. napta- *feucht' ; ai. l/^nabh-, ndbhatB 'spalten,
platzen; hervorquellen*.
LW. ar. naft; kurd. nefte; bei. n. napt 'Donnerkeil,
Blitzstrahl, Kanone' (No. 177) gehört aber wohl nicht
hierher.
Arische Doppelformen naph- und nabh-, vergl.
Hörn, KZ. 32, 584 No. 16.
1036. fUgasten malen', Praes. nigär-em, nigarld^n^ nigär
*Bild*, nigdristdn (Häfiz 16, 5).
Causativum zu nigertdeny nigeristen (No. 1038),
wörtlich *ansehbar, sichtbar machen'; phlv. '^n(i)kar
etc., vergl. arm. LW, nkar 'Bild', nkaren, tikarem,
1037. nigäh 'Anblick, Aufmerksamkeit*.
aw. *nikasa- (vergl. ägäh, No. 40); phlv. n(i)käs.
LW. kurd. nekä; bei. nikäh (263).
Kä§. V. hat sogar als Verbum [/^kos- *sehen' noch
erhalten, nämlich in Praes. bitkesün, Impt. bikes, Inf.
bikasdn u. s. w. (s. v. nigäh kerden).
1038. nigertden 'betrachten', nigeristen.
Käs. Q. vergl. angastän^ batangastdn (s. v. nigc^
kerden),
Wohl zu derselben Wurzel wie aw. hankäray§mi,
siehe np. engärden (No. 123); phlv. n(i)karitan,
n(i)kar(i)sn,
kurd. nirin, nihirin 'betrachten.
1039. nem 'feucht; Feuchtigkeit'.
aw. napta- 'feucht' {[/^nab-, namb- d. i. nabh-,
nambh'); phlv. namb^ nam.
^)In SpiegeTs Chrestomathie, S. 97, 5, durch einen Vers
Väqänl's belegt.
```


## [2026-09-06T22:13:59.893Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\npages=open('HUB.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor pr in (39,):\n    for i in (pr+10, pr+9, pr+11):\n        print(\"##### HUB leaf\",i)\n        print(pages[i][:2500])\nEOF"
}
```


## [2026-09-06T22:14:00.598Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pargar\\|pargār\\|parkār\\|pargâr\\|Zirkel\" HUB.txt | head -20"
}
```


### [2026-09-06T22:14:02.025Z] TOOL RESULT

```
##### HUB leaf 49
— 39 —
proceeding', parddz ^finishing, completing ) stimmt nicht
zu Horn's Etymologie: zA. para + tacay- Veglaufen
lassen . Phi. pardaxt verbraucht' Arta-Vlraf Cap. 89,
6 ist unsicher.
298. Bei der vorgeschlagenen Etymologie: skr. pari -f
sthci 'umstehen' erwartet man ein praes. *paristam
aiis *paristam (fur parastatn)^ inf. *paristadan (fiir
parastidan). Vgl. estadan und firistadan,
299. Np. pursam = ap. prsamiy (nicht parsamiy). Die
Wurzel war ap. und iran. fras (auf der mittleren
Stufe), prs (auf der NuUstufe).
301. Die Bedeutung von zd. parsuy&o ist unsicher; Geld-
ner erschliesst sie aus np. pars *Bach*, das Horn
wieder fiir unsicher halt. Auch sollte np. *pas- einera
zd. pars- entsprechen.
Np. pargdl = pargOr 'Zirkel' (afgh. parr/dr 'Zirkel')
stellt de Lagarde (Btrg. zur bactr. Lexic. p. 54) nebst
pargar 'Halskette' zu zd. pairikara- vd. 17, 6 = Turche'
(phi. pBramUn-karisnlh) und vergleicht skr. jmrikara-
'Giirtel'. Unsicher.
302. Np. pargana 'terra vel provincia vectigalis; an in-
ferior division of a country nearly equalling a barony',
afgh. LW. pargana dt. gehort sicher nicht zur Wurzel
kan *graben'.
303. Slvend. para Vorgestern' (Journ. asiat. 1893, 294)
hierher oder zu Nr. 311 oder 270.
304. Zd. pairivara- heisst yt. 1, 19; 13, 71 bestimmt
'Schutzwehr'(*Abwehr Geld ner,*Wehr* Bart hole mae,
'cuirasse par devant' Darmesteter) und wird also
vd. 2, 26 ohne Not nicht anders zu iibersetzen sein.^)
Es gehort also nicht zu np. parvdr 1) 'Mastvieh*,
2) *Nahrung*, 3) 'Ort, wo man Vieh mastet', das doch
sicher zu parv(lra^ parvdrl gemastet, fett*, parvardan
'ernahren, futtern, erziehen' etc. zu stellen ist. Be-
deutung und Etymologie von hebr. parbdr, parvdrtm
*) Dazu nach Fr. Miiller aram. parvara ^Vorstadt, Vorhof*
(aus Levi's neuhebr. Wb.)
##### HUB leaf 48
— 38 —
286 Anm. Np. p%r alt' aus ^p^rvya- = ap. p(a)rumya-
(haca parumyata Von Alters her') ? Vgl. mirad *stirbt*
aus *infyatai.
287. Np. pid/ram erfreut' wird aus ^paiti-raman- erklart.
Warum dann nicht *pairam*i^
289. Streiche die Worte: „al80 aw. ^upadtti-'' und vgl.
oben Nr. 144. Das Wort padid sichtbar ist erst im
Mittelpers. componirt aus pa und dU == 'in Sicht'
wie padrud aus pa und drut (Horn, Nr. 288).
291. Np. padtra 'entgegen = paz. padtra Min. Gl. 151,
Shk. 261, phi. patlrak Gl. and Ind. 95 etc. lasst sich,
da phi. paVSrak fest steht, nicht auf ein phi. "^patglrak
zuriickfiihren und mit Nr. 290 : padlruftan ( entgegen-
nehraen, annehmen = phi. patgrafian (ap. patiy H-
grh) vermitteln. Ich glaube, dass die beiden Worter
wurzelhaft verschieden *) sind und nur die Praep. pad-
= ap. patiy gemein haben, dass aber phi. patgraftan,
pr. *patg%ram 'entgegennehmen' friih von patlrak *ent-
gegen* lautlich beeinflusst worden ist. Sonst sind auch
die Lautverhaltnisse von padlruftan unerklarbar. Denn
warum heisst es nicht: *paigriftan, *paigiram?
295. Np. pardgandan zerstreuen', phi. pargandak 'scat-
tered* (61. and Ind. 103) passt jedenfalls nicht zur
Wrzl. kan graben'. Es gab ja wohl auch noch andere
Wurzeln kan oder gan. Vgl. Nr. 41 : agandan VoU-
stopfen'.
296. Np. partav 'Licht, Strahl* (auch afgh. LW.) mit auf-
falligem t fiir d, Anlehnung an tab, taftan etc.?
297. Np. pardaxtan hat bei Vullers 12 Bedeutungen,
es ist schwer zu entscheiden, auf welche man die
Etymologie bauen soil. Die gewohnliche Bedeutung:
VoUenden, beendigen, sich mit etwas beschaftigen'
(vgl. afgh. LW. pardaxt performance, relinquishment,
*) paSira = phi. patirdh gehort zu zd. paiti + ar^ wovon pat-
tyUra' 'Opposition', paiti-ereiti- 'Widerstand, Hinderniss*, apaitiereta-
'ohne Widerstand, ungehemmt'. Ich setze paSira = ap. ^pati-jrya-.
##### HUB leaf 50
— 40 —
ist unsicher; de Lagarde, Btrg. z. bactr. Lex. p. 55
ist schwerlich im Recht.
307. Fr. Muller WZKM. 6, 352 bemerkt mit Recht, dass
man fiir paz. awarvez Shk. 233 = arm. AprUSz (= Aprv^)
im Neupersischen *barvez anstatt parvez Victor, felix,
fortunatus' erwarten miisste. Ist es beeinflusst durch
p^rdz Victor, felix, faustus ?
308. Ich kann die ihrem Sinne nach zusammengehorigen
Worter (ZDMG. 44, 560) lautgesetzlich nicht ver-
einigen. Darmesteter liest mit Westergaard
paoirySnyaS' (von paoiry^i- aus *pdrvydni-^ vgl. afgh.
pSrune, Geiger, Etym. Nr. 170), das er mit ahuranfs
(von ahurani' ahurisch*) vergleicht und durch *die
(Wasser) des Paoirya (Zend-Avesta II, p. 418) iiber-
setzt. Aber Geldner liest paoirya^iny as- von paoirya^i-
= ap. *paruviyaini' = np. parvm?
309. Np. parhe» 'Enthaltsamkeit, Fasten', parMxtan *sich
enthalten' = paz. pahrez Min. GL 154, phi. pahrSd
'abstinence* GI. and Ind. 88, *Vorsicht* Yatk. i. Zar.
p. 62, Anm. 48, pClhredSnd *sie hiiten, pflegen ebenda
p. 51, Anm. 16. Von dieser Pehleviform fiihrt kein
Weg zu Fr. Muller' s (WZKM. 6, 185) zd. ^paiti-ra^d-
Verlassen*", dem doch nur np. *pairextan entsprechen
wiirde. — Arm. pahrez 'Fasten' ist einmal im 14. Jhd.
belegt.
310. Zd. pairika- schlechtweg durch *Hure' zu iibersetzen,
ist falsch. Die Pairika s sind Teufelinnen, die die
Frommen zu verfuhren und vom rechten Glauben ab-
wendig zu machen suchen; phi. parlk bose Fee'
Bdh. Gl. 108, arm. parik ein Fabelwesen' (Eznik 97, 98),
np. pari 'Fee, EngeF.
312. Die Form piSman u. s. w. ist verkiirzt aus paslman, das
auch ins Afgh. {pa§Tmcin Veuig') iibergegangen ist. Vgl.
paz. poSetnan repentant', paSSmam 'penitence' Shk. 263,
Min. Gl. 157, phi. paSSmdnlh 'Reue* Phi. Min. p. 5, Z. X5,
```


### [2026-09-06T22:14:02.071Z] TOOL RESULT

```
871:204. Vgl. phi. apargar (fiir aparkar) = paz. awargar a
1318:Np. pargdl = pargOr 'Zirkel' (afgh. parr/dr 'Zirkel')
1320:pargar 'Halskette' zu zd. pairikara- vd. 17, 6 = Turche'
```


## [2026-09-06T22:14:11.427Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('SYN.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\n# find page whose text contains '628'\nfor i,p in enumerate(pages):\n    if re.search(r'\\b628\\b', p[:200]) or re.search(r'^\\s*628', p):\n        print('cand leaf',i)\nprint('total',len(pages))\nEOF\ngrep -n \"9.11\\|DO, MAKE\" SYN.txt | head -20"
}
```


## [2026-09-06T22:14:13.175Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls NYB*; python3 - <<'EOF'\npages=open('NYB_vol2_glossary.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('pages',len(pages))\nimport re\nfor i,p in enumerate(pages):\n    if re.search(r'kartan|kardan|kar-|kirdan', p[:300]):\n        pass\nfor i,p in enumerate(pages[:5]):\n    print('---',i,p[:200])\nEOF"
}
```


### [2026-09-06T22:14:13.244Z] TOOL RESULT

```
total 1545
804:e. A definite portion of the earth’s surface, from the land of an individual to a whole country (19.11).
4809:SCr., raca (> Rum. ratd), Alb. rosé, etc., like NHG dial. rdtsche, of imitative orig. G. Meyer, Alb. Etym. Wtb. 368. Rohlfs, Z. frz. Spr. 49.111 f.
5676:Boh. tvd?, Pol. twarz (the common words for ‘face’), fr. the root of ChSl. tvoriti, etc. ‘do, make’ (9.11), hence orig. ‘creation, form, kind’ (attested for older Boh. and Pol.; cf. also ChSl. tvari ‘crea- tion, work, deed’, SCr. tvar ‘material’, stvar ‘thing’, Boh. tvar ‘form, shape’, Russ. tvar’ ‘creature’), with further se- mantic development like that in Lat. facies (above, 2). Briickner 586.
9581:s(t. zejtin, REW 9611. Lokotsch
10254:W. gwnio, Br. gwriat (for n > r in Br, cf. Pedersen 1.155), Specialized fy. ‘make’ : Ir. do-gniu ‘do, make’ (9.11), Pedersen 1.60.
10850:OE scohwyrhta, MHG schuochwiirhte, epds. of words for ‘shoe’ and agent- nouns of OE wyrcan, OHG wurchen ‘make’ (9.11).
12227:NE pea (OF. paisant > Ountry’ (19.11) ae ae of pays
13490:9.11 9.12 9.13 9.14 9.15 9.16 9.17 9.18 9.19 9.192 9.21 9.22 9.23 9.24. 9.25 9.26 9.27
13545:(as Artist) 9.943 Firrine, SurraBLe PAINTER E 966 PAINTING, icru® 9.95 Can, May 987 (sb.) , 9.96 Hasy nT : (@ 988 Fe (vb. ‘Paint 6 House’) 9.97 Dirricuir 989 Tans 9.98 Try! (Make Trial of, Test) v BE 9.99 Try? (Attempt, Endeavor) Me pecow® 9.992 Way, MANNER a NzED, ‘im 9.993 HarrEn T, UST 9,94 QuGH ? 911 DO, MAKE ; Goth. taujan, waurkjan Lith. (pra)daryti, veikti
13633:1. From IE *werg- in Grk. épiw, pétw ‘do’, Av. varaz- ‘work, do’, etc. (9.11). Walde-P. 1.290 ff. Feist 555, 556.
13678:ChSI. délo (renders épyov), ete., gen- eral Slavic for concrete ‘work’ : déti ‘put’, etc. (9.11, 12.18). Hence vb. ChSI. (st-)délati in Gospels reg. for Epya- touat, later for xovéw, Boh. délati ‘do, make’ and ‘work’ (Pol., Russ. ‘do’, 9.11).
13686:8.:Skt. karman- ‘act, activity’ and ‘work’ (cf. karma-kara- ‘workman’) : kr- ‘do’ (9.11).
13689:P. 2.426, 498. Skt. ¢am- : Grk. kauvw, above, 2, Av. vorazya- : varaz- ‘do, work’, Grk épyor, etc. (above, 1). . For ‘work’ concr. mostly Skt, krta- Av. karota-, OPers. karta- : Skt, kr- ‘do, make’ (9.11). ¢
13890:Du. touw = MHG tou(we) ‘tool, equipment’ esp. of a ship, hence ‘cable, rope’ (NHG taw fr. LG) : Goth. taujan ‘do, make’ (9.11). Walde-P. 1.779. Falk-Torp 1267.
14810:4. ON iol (pl.), OE tol, ME tole, NE tool, fr. the root of OE tawian ‘prepare’, Goth. taujan ‘do, make’ (9.11). NED s.v. fool, sb.
14818:‘iti ‘do, make’ (9.11).
14823:7. Skt. karana- (neut.), mostly act of ‘doing, making’, fr. kr- ‘do, make’ (9.11),
14850:Br. ober gant, lit. ‘do with’ (ober ‘do’, 9.11; gant ‘with’).
14927:ON g¢rva ‘do, make’ (9.11) and in phrases like gérva his, skip, etc., the most common expression for ‘build’.
15184:Fr. macgon (> ME machun, NE ma- son), MLat. macio, machio, matio ‘ma- son’, prob. a Latinized form of a Gmc. *mako : OF macian ‘make’, OHG mah- hon ‘accomplish, make, construct’, etc., reflecting an assumed earlier meaning of the Gme. verb, namely ‘build with clay’ (see 9.11). REW 5208. Meyer-Liibke, Wort. u. Sach. 9.67f. Sofer, Isidorus 142. Walde-H. 2.4.
```


### [2026-09-06T22:14:15.101Z] TOOL RESULT

```
NYB.txt
NYB_vol1.txt
NYB_vol2_glossary.txt
pages 295
--- 0 www.parsianjoman.org IN n

--- 1 A MANUAL OF PAHLAVI
by HENRIK SAMUEL NYBERG
II
Ideograms, Glossary, Abbreviations, Index,
Grammatical Survey, Corrigenda to Part I
www.parsianjoman.org | oe zl ejt

--- 2 (C) Otto Harrassowitz, Wiesbaden 1974 Alle Rechte vorbehalten
Photographische und photomechanische Wiedergabe nur mit ausdrücklicher Genehmigung des Verlages
Satz: Layout-Satz Dr. Tetzner GmbH, Mainz 
--- 3 2
HENRIK SAMUEL NYBERG A MANUAL OF PAHLAVI
II
www.parsianjoman.org |e Job P J 8 luga)
--- 4 ?
www.parsianjoman.org sel
```


## [2026-09-06T22:14:22.750Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('SYN.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\n# find leaf index of line containing '911 DO, MAKE'\nimport re\npages=txt.split('\\f')\nfor i,p in enumerate(pages):\n    if 'DO, MAKE' in p and 'Goth. taujan' in p:\n        print('leaf',i)\n        print(p[:1500])\nEOF"
}
```


### [2026-09-06T22:14:24.382Z] TOOL RESULT

```
leaf 588
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
Words for ‘do’ and ‘make’ are treated together because these most generic no- tions of action are so commonly ex- pressed by the same word; and where there are pairs of words, roughly dis- tinguished by the feeling for the action itself or the implication of result respec- lively, the idiomatic differentiation is never quite the same for different lan- Guages and periods, not even in the case of such closely allied pairs as NE do, ees tun, mach
```


## [2026-09-06T22:14:29.527Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('SYN.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nimport re\n# find leaf where printed page 628 appears\nfor i,p in enumerate(pages):\n    if re.search(r'\\b628\\b',p):\n        print('leaf',i, p[:160].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-06T22:14:31.394Z] TOOL RESULT

```
leaf 49 acq 128 f. | 2. Lat. mons, montis (> It. monte, etc.), W. mynydd, Corn. meneth, Br. menez ‘mountain’, Av. mati- ‘mountain top’, fr. the root seen in Lat. é-, pré-
leaf 59 e Grk. Tapadla Boh. po-mofi ‘coast’. ey a wens (or stab neut.) OHG Geetads Se ere stade, gestat, NHG | » beside Goth. stass, OE step OHG stat, etc. ‘place’ ? grou
leaf 67 rsson, Beitrige 15. Franck-v. W. 25. | Du. golf, form influenced by golf ‘gulf, bay’, but fr. MDu. ghelve (also golve), MLG gelve ‘wave’ : ON gjalfr ‘noise of the
leaf 127 fr. hus-fru, epd. of hus ‘house’ and fru ‘mistress’, like NHG hausfrau, Du. huisvroww. | Sw. make, fem. maka, ME make prop- erly ‘mate’ : OE gemecca ‘mate’ gem- O
leaf 143 ��s daughter’ (mic gen. of mac), | NIr. mac inghine ‘daughter’s son’, inghean inghine ‘daughter’s daughter’, | NIr. garmhac ‘grandson’, fr. MIr, gormac ‘foster-son,
leaf 371 rd originally denoting some special kind of food comes to be | FOO. | d whe special of If *ed- ‘eat’ (5.11). My Hom. ¢ldap; Lat. ésca; HG, MHG az; Lett. ? of food’)
leaf 392 e., fr. Lat. urceus (above, 2) or fr. the same source. Miklosich, Lex. Palaeoslov. s.yv. | Russ. kuvsin beside kovg ‘scoop, ladle’ : Lith. kKausas ‘ladle’, Lett. 
leaf 403 ngri Collection, Haridwar | Digitized by Arya Samaj Foundation Chennai and eGangotri | 358 | and laib, cf. Kretschmer, Wortgeogr. 150 ff. | 5. Lith. duona (Lett. duona 
leaf 494 - ve the d e. ' ‘adornment’ (6.71). 4 |. ram é, Pol. poh. ram 6.75 NECKLACE = ON men, halsgjord Lith. kaklarysis, karieliat Grk. pH arpentés, TEPt Dan. halsbaan
leaf 545 labor ‘labor, toil’ (9.12). REW 4810. | 3. Ir. airim ‘plow’ (8.21), also in wider sense ‘cultivate’. Hessen s.v. | NI. oibrighim ‘work’ (8.13) and ‘cul- tivate.’ | Ni
leaf 683 ne ‘statue’, which became its established use : ayan- ho ‘adorn’ and ‘glorify’, &ydads, ‘bright, splendid’, ete. Walde-P. 1.623. Boi- Sacq 5, oer aig orig. ‘ima
leaf 714 f ell- ‘go, set in motion’ (10.47). Pe- dersen 2.511. | NIr, tabhraim (or tugaim) iarracht ar, lit. ‘give effort to’, phrase with iarracht ‘attempt, effort’ : iar
leaf 829 tick of wood’), with semantic development through ‘hunt for fire- wood’. REW 1420. Wartburg 1.650. | Rum. cduta fr. VLat. *cavitadre, iter. formation to Lat. cavé
leaf 903 E *fei-. Walde-P. 1.358 ff. Grk. keluat, 38g. xetrac = Skt. cele, Av. saéte. Byz., NG xetrouat (so, not xolrouac as if fr. sb. orn) with shift to thematic type 
leaf 1106 hutnati, miti chut’ chut’ chut’ (okus) Re kosztowaé smakowaé smak smak : i vkusit’, olvedat! imel’ vkus vkus vkus ti. suad-, ras- svad-, ras- rasendriya- (?) ra
leaf 1198 ide, Sw. lida, NEG; sbs. Dan. lidelse, Sw. lidande), =e oul but OHG ir-lidan ‘endure, ine Bey then ‘experience (go ts Ge a (cf. phrases like NE what is eae ), t
leaf 1211 ��wrinkle the nose’ : Lith. Septis ‘grin’, Sypsotis ‘smile’ (12.25). Walde-P. 1.364. Stokes 75. | NIr. goilim, cf. MIr. gol ‘weeping’, prob. as orig. ‘cry out’ : 
leaf 1341 . Walde-P. 1.252. Boisacq 15. | NG rpayovsd, fr. class. Grk. rpayedée ‘act, chant a tragedy’, late ‘chant, re- eee Tpaywoia ‘tragedy’, cpd. be- | g to preceding Bro
leaf 1375 . 1135. | Grk. xou7éw (also ‘ring, clash’), xouwatw, with sb. xduzos ‘din, clash, boast’, etym.? Boisacq 489 f. | Grk. xavxéouat, prob. of imitative orig. (cf. Lith
leaf 1444 n), Sp. compafio, now de- riv. compafiero, fr. MLat. compdnio, -onis, epd. of com- ‘together’, and panis ‘bread’, orig. a military term modeled on the Gmc., ef.
leaf 1536 to’, as legal term, ‘sue’. | Dan. klager, fr. MLG (below). | Sw. kdrande, fr. kdra ‘bring suit, prose- cute’ = ON kera ‘accuse’ (21.31). | OE ftéond, pres. pple. of t
```


## [2026-09-06T22:14:38.898Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('SYN.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nfor i in range(676,690):\n    p=pages[i]\n    import re\n    m=re.findall(r'\\b(5\\d\\d|6\\d\\d)\\b',p[:400])\n    print('=== leaf',i,'nums',m)\n    print(p[:300].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-06T22:14:40.867Z] TOOL RESULT

```
=== leaf 676 nums ['626', '624']
as OF gler and a part OHG glas) : Ir. glass ‘green, gray blue’, W. glas ‘blue’, Br. glaz ‘green’, ON glesa ‘make shine, adorn’, ME, MLG glaren ‘gleam’, all prob. fr. an s-extension of I *ghel- in color names (cf. above, 3). Walde-P. 1.626. Falk-Torp 325. | 5. Lith. stiklas, Lett. stikls, OPruss, sticl
=== leaf 677 nums []
 to representing a generic term for the product, though the words are used mostly for various more specific products, is the following: | Grk. xapra(A)Aos ‘a kind of basket’, xvptn ‘fish-basket’, xuptia ‘wickerwork shield’ (all rare words), Lat. cratis (esp. pl. cratés) ‘wickerwork, hurdle, harrow’, O
=== leaf 678 nums []
N brja ‘sparkle, shine’, braga ‘flame, burn’, ete, (for such relations cf. the uses of NE flash). Walde-P. 2.169. Falk-Torp 56, | NE plait, plat (in scuthern US. one plats hair), deriv. of plait ‘a fold, crease’, fr. OFr. pleit, Lat. plicitum : plicare ‘fold’, plectere (above, 1). NED sv. | 5. Lith. pin
=== leaf 679 nums ['623']
 PHYSICAL ACTS, ETC. 623 | Grk. apprxos (Ion. a&porxos), orig. dub. Walde-P. 2.374. | Grk. capyavy (in NT, 2 Cor, 11.33 clearly a ‘rope-basket’; cf. the Goth. rendering 8n67j6; so prob. in the papyri, where the word is frequent beside kopuvos), Att. tapyavn (Hesych., EM), etym.? Walde-P. 1.751. Boisacq 
=== leaf 680 nums []
 in NED S.V., but cf. Weekley s.v. | CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar | OHG corb, etc., above, 2 corbis. aie: Lat. | MHG krebe : OHG krippa, OB cribb ‘crib, manger’, MLG kerve ‘fish-basket net’, ON kjarf ‘bundle’; OHG cratto, krezzo, MHG krezze : OE creat ‘wagon. basket’, OHG kr
=== leaf 681 nums ['595']
ce con- oie : MSS and introduction of in sie culptor, Sculptura, in our texts Ol scalpere, scalptor, scalptura, im ‘knife, chisel’, dim. scal- | 1), prob. fr. an extension of ‘scrape, hoe’, skilja ‘separate, -P. 2.595. Ernout- | Tema: eC root Se | P 13) Lith, - | alde | CC-0. In Public Domain. Guru | sculpter, 
=== leaf 682 nums []
, | It. scultore Sw. bildhuggare SCr. — kipar, vajar Fr. sculpleur OE (grafere) Boh.  sochar, Fezbd¥ Sp. escullor ME (graver), kerver Pol. rzezbiarz Rum. — sculplor NE sculptor Russ. vajatel’, skul'ptor Ir. acre Du. beeldhouwer Skt. iene | Nir. — snoigheaddir OHG (grabart) Av. | W. cerflunydd MHG (grabare
=== leaf 683 nums ['623']
ne ‘statue’, which became its established use : ayan- ho ‘adorn’ and ‘glorify’, &ydads, ‘bright, splendid’, ete. Walde-P. 1.623. Boi- Sacq 5, oer aig orig. ‘image of a Gh Giien ae ied to statues of men gods (as aad rarely to those of the of Apollo at oe of an archaic statue ‘nan’, 8), deriv. of avip
=== leaf 684 nums []
qg ‘cord of wood’, this as orig. a measure (cf, sqzen, ChS]. sezint ‘fathom’, i.e. ‘the distance to which the arms can be stretched’) : Ch§]. segnati ‘stretch out (the arm)’, Pol. Siegaé ‘reach, stretch’. Briickner 483. | Russ. izvajanie ‘piece of scl statue’ : (iz)vajat! ‘carve’ (9.81). | 7. Skt. prati
=== leaf 685 nums []
E chisel Russ. doloto Ir. tee Du. beitel Skt. wees Nir. _ siséal : OHG = meizil Av. | W. cyn, gaing MHG maizzel | Br. kizell NHG  meissel | Words for ‘chisel’ (sculptor’s or car- penter’s) are from verbs for ‘cut, hew, carve’, ‘split’, or ‘hollow out’. The Welsh words denoted originally ‘wedge’, whence ‘c
=== leaf 686 nums ['629']
�� (9.23). | igitized by Arya Samaj Foundation Chennai and eGangotri | 629 | ME chisel, NE chisel, above, 2. | Du. beitel (MLG > Dan. bejtel), fr. the root of bijten, Goth. beitan, etc. ‘bite’, orig. ‘split’, Lat. jindere, Skt. bhid- ‘split’ (9.27). Franck-y. W. 44. | 5. Lith. kaltas, Lett. kalts, fr. vbs. Li
=== leaf 687 nums ['691']
sign’, these prob. fr. the root seen in Skt. malina- ‘dirty, dark’, Grk. hédas, Lett. melns ‘black’, ete. But the immediate development in German is fr, ‘make a mark’ to ‘draw’, hence also ‘paint’, and has no direct connection with a color notion. Walde-P. 2.293. Falk-Torp 691. | Du. schilderen (cf. N
=== leaf 688 nums []
ojums NG = fwypagid, rlvaxas Dan.  maleri, billede ChSl.  obrazii (elxova) Sw. mdlning, tavla, bild SCr.  slika { Lat. pictiira, tabula OE méting, tifrung Boh. _malba; obraz / It, pillura, quadro ME peyntyng, peyniure, Pol. malowidlo; obraz Ry, Peinlure, tableau pycture Russ. Zivopis', kartina Sp. P
=== leaf 689 nums ['537']
etc. (9.85). | Russ. kartina, deriv. of karta ‘card map’, this fr. Lat. charta ‘paper’. Ber neker 491. | 7. Skt. citra- ‘bright, clear’ (: OHG heitar id., Walde-P. 2.537), neut. sb. ‘ornament’ and ‘picture’, likewise cttra- karman-, epd. with karman- ‘work’. | 9.88 PAINT (sb.) | Grk. xpapa Goth. Lith. dazai
```


## [2026-09-06T22:14:49.640Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('SYN.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nfor i in (683,684,685):\n    print('===== leaf',i)\n    print(pages[i])\nEOF"
}
```


### [2026-09-06T22:14:51.213Z] TOOL RESULT

```
===== leaf 683
ne ‘statue’, which became its established use : ayan- ho ‘adorn’ and ‘glorify’, &ydads, ‘bright, splendid’, ete. Walde-P. 1.623. Boi- Sacq 5, oer aig orig. ‘image of a Gh Giien ae ied to statues of men gods (as aad rarely to those of the of Apollo at oe of an archaic statue ‘nan’, 8), deriv. of avip, avipds
» Statua, usually of men : sia- use to Stand, set up’, fr. stare
statue, NHG statue, Lett. statuja, Pol. statua, Russ. statuja.
Lat. signum ‘mark, sign’ (12.94), hence also ‘military standard’ and ‘image, statue’ (usually of a god). Hr- nout-M. 939.
3. Ir. delb ‘form, image’, NIr. dealbh, W. delw ‘form, image, statue’ (also W. cerfddelw ‘carved image’, cf. cerfio ‘carve’, 9.81), Br. delowenn (so Vallée for ‘statue’, not in Ernault):Ir. dolbaim ‘form, mold’ (9.72), Lat. doldre ‘hew’, etc. (9.45). Walde-P. 1.810. Pedersen 1.64.
NIt. iomdigh ‘image, statue’, fr. Lat. imago ‘image, representation’. Ven- dryes, De hib. voc. 146 f.
W. cerflun ‘piece of sculpture, carv- ing, statue’, epd. of cerf ‘carving, sculp- ture’ (: cerfio ‘carve’, 9.81) and Ilun ‘form, picture’ (9.87).
Br. skeudenn ‘image, statue’ (Er- nault), deriv. of skeud ‘shadow’ (1.63).
4. Goth. man(n)leika ‘image’ (in the only occurrence renders eixav, the image on a coin), ON mannlikan ‘human im- age, idol’, OF man(n)lica ‘human image, statue’, OHG manaliho, etc. (Graff 2.118), epds. of words for ‘man’ and those for ‘like’, Goth. (ga)leiks, etc., whence also ON Itkneski, ME licness ‘likeness, image, statue’.
Dan. billedsigtte, Sw. bildstod, epds. of Dan. billede ‘image, picture’, Sw. bild ‘picture, representation, statue’ (9.87) and Dan. sigite, Sw. stod ‘pillar’.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar -~<
628 SELECTED INDO-EUROPEAN SYNONYMS
Du. standbeeld, cpd. of stand : staan ‘stand’ and beeld ‘image, picture’.
OHG sul, MHG sil, sitel ‘post, pillar’ hence also ‘statue’, NHG bildsdule ‘statue’ (cf. bild ‘image, picture’, 9.87) : ON sil, sila, OE sgl, Goth. sauls ‘pil- lar, column’. Falk-Torp 1233. Walde- P. 2.503.
5. Lith. sfatula (mow preferred to stovyla, fr. Wh. Russ., formerly in com- mon use), fr. weak grade of IE *sta- ‘stand’, as in siatymas ‘building’, etc. Cf. OE stafol ‘foundation, support’. Buga, Kalba ir Senové 172 f.
Lett. téls ‘form, image, statue’, prob. fr. ORuss. télo ‘image, idol, statue’ (be- low, 6). Miihl.~Endz. 4.171.
6. ChSI. télo ‘body, form’ (9.11), hence later ‘image, statue’ as also ORuss. télo, ete.
SCr. kip ‘form, image, statue’, fr. Hung. kép ‘appearance, form, picture, image’. Berneker 504.
Boh. socha ‘handle, pole, pillar’ hence
also ‘statue’ : ChSI. (late) socha ‘club cudgel’, Russ. socha ‘wooden plow’, et ‘ (8.55). Walde-P. 1.335, ee
Pol. posqg ‘statue’, orig. ‘Wooden pillar’, fr. s
===== leaf 684
qg ‘cord of wood’, this as orig. a measure (cf, sqzen, ChS]. sezint ‘fathom’, i.e. ‘the distance to which the arms can be stretched’) : Ch§]. segnati ‘stretch out (the arm)’, Pol. Siegaé ‘reach, stretch’. Briickner 483.
Russ. izvajanie ‘piece of scl statue’ : (iz)vajat! ‘carve’ (9.81).
7. Skt. pratimd- ‘image, picture, stat- ue’ : prati-md- ‘imitate, copy’, cpd. of prait ‘over against’ and ma- ‘measure’ (12.54) ‘mete out, fashion, build’, ete,
Skt. ddivata- ‘statue of a god, idol’ (so freq. in Manu, etc.), deriv, of deva- ‘god’.
OPers. patikara- used of the figures sculptured in relief (NPers. paikar ‘face, form, portrait’), cpd. of pati- ‘over against’ and kar- ‘make’, hence lit, ‘something made in likeness’,
pture,
9.84 CHISEL (sb.)
Grk.  cpthy Goth. .... Lith. kaltas NG opldrn, oprrAdpr ON meitill Lett. kalis Lat. — scalprum Dan. mejsel, bejtel ChSl.  dlato It. scalpello, cesello Sw. mejsel SCr.  dlijeto Fr. ciscau OE grafsex Boh.  dldto Sp. escoplo ME _chisell Pol. dléto Rum. daltd N
===== leaf 685
E chisel Russ. doloto Ir. tee Du. beitel Skt. wees Nir. _ siséal : OHG = meizil Av.
W. cyn, gaing MHG maizzel
Br. kizell NHG  meissel
Words for ‘chisel’ (sculptor’s or car- penter’s) are from verbs for ‘cut, hew, carve’, ‘split’, or ‘hollow out’. The Welsh words denoted originally ‘wedge’, whence ‘chisel’ from the similar shape.
1. Grk. cutdy, NG also ourape : OF smtp ‘smith’, ete. and prob. Goth. mai- tan ‘cut, hew’, OHG meizil ‘chisel’, etc. Walde-P. 2.686.
2. Lat. scalprum (> Fr. échoppe, Sp.
escoplo; dim. scalpellum > It. scalpello), fr. scalpere ‘carve’ (9.81). Ernout-M. 901. REW 7642, 7645.
It. cesello, OF r. cisel (> Br. kizell), chisel (> ME chisell, NEE chisel > NIt. siséal), Fr. ciseau, fr. late Lat. *caesel- lum, cisellum, deriv. through *cisum (cf . cisdrium ‘cutting tool’) of caedere ‘cut. REW 1474. Wartburg 2.40. NEDs.v. chisel sb.}.
Digitized by Arya Samaj Foundation Chennai and eGangotri 7
}
MISCELLANEOUS PHYSICAL ACTS, ETC.
fr, Slavic (below, 6).
Iso and orig. ‘wedge’, fr.
ge’. Loth, Mots lat.
: ig Jones 91.
‘ a and orig. ‘wedge’ = Ir.
gen ‘wedge’: ON gandr root connection dub.
Stokes 110. TFalk-
m. dalla,
tesa meitill, OHG meizil, MHG “vl NHG meissel (> Dan., Sw. mej- a the root of Goth. maztan, OHG
fr. os etc. ‘cut’ (9.22). Walde-P.
9, Weigand-H. 2.162. 48 grafsex, fr. grafan ‘carve (9.81) and seax, sex ‘knife�
```


## [2026-09-06T22:15:00.831Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\npages=open('NYB_vol2_glossary.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(pages))\nfor i,p in enumerate(pages):\n    m=re.search(r'^\\s*(\\d{2,3})\\b', p.strip()[:8])\n    if m: pass\n# search for kartan entries\nfor i,p in enumerate(pages):\n    if re.search(r'\\bkartan\\b|\\bkart\\b.*\\bmade\\b|kirrēnīdan', p):\n        print('leaf',i, p[:120].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-06T22:15:02.385Z] TOOL RESULT

```
295
leaf 18  anything to do with adarvär BdJ 3511, 5710 = adarvārak BdA p. 103°. 120? ‘lower jaw’, also:the rendering of Av. (1767) 
leaf 21 nah ‘Friday’, for Islamic (yaumu-)l-jum'a, cannot be etymologically connected with ātvēnak, as Markwart has it (v. above
leaf 22 antly written in Prs. in- scriptions and in the Ps.; this is wanting in Prth (quite exeptionally written in site, vitava
leaf 27 ation from cand, q. v. | andar [BYN] in: 1. adv. a) referring to a preceding encl. pron. (ef apäk, apar, avis, haciš, pati
leaf 34 Ind. vb. šā- means ‘to sharpen, to whet’ ($ita- ‘sharp’) a sense also attested in Ir: NP afsän, ausän ‘whetstone’; MPrs 
leaf 46 yberg, Da- nielsson Vol., 1932, 237-261; Ghilain 47. Cf örandar, öristar. | *āvartāk [’wlt’k] *procuring one's wealth from
leaf 47 � havand bavet shall listen bene- volently (to the man confessing his sin), and he shall not disgrace him, nor divulge h
leaf 49 t together, to compose 1192-21; to fetch down 40?!; to inflict (a punishment) 9°; to acquire (a name, renown) 27%; — and
leaf 51 21°. 5615. 6112, — 2. dyuxtan inf. of dydz- (g. v.). — 1. ā- 4- Av. (1228 sq.) yaog-. Cf ap?-yuat. | ayyaritan [’dyb’lytn'
leaf 57 be Zartuxšt | tat ... kas-ic ne nobody but Z. alone 9313-14; — hac ... be: nipekihä i hac den bé writings outside (= not c
leaf 60 his power to upper Meso- potamia. | | Bratoroš [bbtwlwš] n. pr. 11716. — An- other form of Brātar-vaxš, v. Brataroreš; Byt
leaf 63 s bwatn, pres. MPrth bwy-, bwas-, MPrs bwz-; Arm. lw. bužem; Paz. boxtan, buxtan, bož-. — V. božišn. | buxtarčh [bwht’lyh]
leaf 68 ated beings, the created world 31?! and passim ; ~ u dahišn, v. dahišn; — pl. cas. obl. ~-ãn 7319. 7624. 7716, 7917. 801
leaf 71 9725, 984, | dat [dt'] wild animal 9725, 984, — Av. (678) daitika-; NP dad(ah). | dat [d?t'] 1. law 6413-19, 6916, 8623, 981
leaf 77  renders Av. (966) bi- zangra-. | drafš [dlpš] banner 2722. 298-16, — Av, (771 sq.) drafša-; MPrth drjš (A-H III, cf MHC 1
leaf 82 10018; and cand yašt-ē [-1] 651°; pat har 40 sal hac zan-ē u mart-é frazand-é [al -ē's spelt -1] zāyēt every forthieth y
leaf 84  with 6 to set out on, to go into 19. 139. 10012; — apar pad ~ 18?!, apar 6 pad ~ 2513, bē 6(i) pad ~ 3424.27, 352, frāc
leaf 85 wl; 3% incorrectly y bl] adj. true [duat ~, with the gl. kū ke mat zat a true daughter, i.e. whom the mother has born PR
leaf 87 . — Paz. fargard. | framän [plm'n'] order, command 12). 11310 ete.; ~ būt hac... + inf. it was ordained, decreed by ... th
leaf 88 is vazurg ~ F: | 1-2. — Arm. lw. vzruk hramatar; Talm hrmdr. V. Christensen, Sass. 114 sqq., 518 sqq. | trimoš [plmwš, plmwš
leaf 93 nterpretation, which restores the Paz. reading and respects the tradition, is due to Bailey (l.c.; ZP 20-21) I now give 
leaf 94 ; MPrs g^w (A-H I); Paz. NP gäv. | gavakéh [gwb’kyh] increase, growth 109. — From Av. (504) !gav-, v. s. v. apazütan; Bail
leaf 95 v. gartišn. | www.parsianjoman.org | ool wok | girtak | girtak: ~ pērāmēn all around 92!9, | girzitan [gyleytn'] to complain, to
leaf 96 īrūz- äbäd. | göspand [gwspnd; KYN?] cattle in gen- eral, but esp. small cattle, sheep and goats, as distinguished from ho
leaf 98 -, Sogd we’w ‘witness’ cannot be compared). Henning, Weller Vol. p. 297, combines Av. vikaya- with Sogd. wcw, deriving t
leaf 105 or ?c ... hmys (S), < OP *hamica- (hamiciya- ‘rebellious, rebel’), NW *hami@ra-, *-riya-, whence MPrth (BBB) hmyr < *ham
leaf 107 t he 7615-16, | handarz-pat [hndlept'] chancellor, chief judge, head of the treasury of a province or a corporation, admin
leaf 108 2-23, 172, — 2. to calculate, to determine 91’. — 3. to consider, to bear in mind 413. 725. — Paz. angārdan; MPrs hng?r-
leaf 112 > or asyndeton] zor u z"arrah i .., spēnāk menoi 10628-24; pat name u nerök u ~ 1 dätär Ohurmazà 113?; 01? v. s. v. jāyt
leaf 114 20 passim; pat cim + kārēcār ~ kart constructed it to represent the - conditions of a battle 1198; — about: kötak 7-säla
leaf 115 the different classes of the community 5027, according to the gl.: ku kar i aparik veh dānēt kartan ‘that is: it knows h
leaf 116  underly- -ing this passage: hordca [read aordca] paräca tarasca, Phl örön u parón u tarist: hutarest [Paz.] pas hac ham
leaf 124 ith the gl. cigön mēnēyān apäyist, v. apāytstan; purr--~ i o ahläyeh whole-hearted devotion to Righteousness 55? (purr-k
leaf 125 I, 249; Ver- bum 172. MPrs and NP ‘to dig’, Paz. cadan, xan- with an initial x- confirmed by the Arab. lw. randag ‘trenc
leaf 126 nker, ZII II, 243, translates 'lizard?, com- paring NP words which seem to be rather distant; wrongly BSOAS XVII, 1955, 
leaf 127 rér kartak bit be 6 Bastvar dahet this horse, since for Z. a legally valid declaration was made (that it should be owned
leaf 128 yenend u ‘BY DWN-x, man and woman will fall in love, become engaged (v. räyenitan) and contract marriage 1044-25; zan ka
leaf 130 7%, 5525. - From Av. (442 sq.) kavi-, v. kat. | 116 kë | kā(y)ēn [k’yn'] the old capital of Köh- istān 11412, v. Cat. 53; Ar
leaf 131  from which men derive pleasure 10020-21 (haciš for hac referring to ke through the intermedium of the encl. -š in ke-$)
leaf 132 rmān [klm’n'] Kirman 81%. 1161, — Arab Karman or Kirmän, Yāgūt 4, 262sgg.; Cat. 90. | kirpak [krpk'] virtue, pious duty (d
leaf 134  the like: göbet ku, api-$ guft ku he says, he said that, passim; very often intro- ducing direct speech, and serving as
leaf 143 r funda- mentals, basic principles, etc.": 1. docu- ment; original and authentic, canonical text 1101; in titles: book, 
leaf 148 v. also mihr-druž. — Cf mihrän kartan to form an alliance KnS VI, 2. — Paz. mihiran-dru£. | mihràn-druZéh breach of faith,
leaf 149 čeak [mwlwyck'] chicken 92%. — Demin. of !murv. | murv-niš [mwlwnyš] soothsayer fore- telling the future by the flight or 
leaf 152 r ~ from above 4326-27, 5819; hac rapitfaktar (g.v.) ~ 56°; hac peš ~ in front, as opposed to hac pasčh 5774; či peš ~ s
leaf 153 2) ničate-. Paz. niha, NP nihan. | nihanik concealed 903. | nihitak [HNHTWN-tk'] the method of placing, arrangement 120%. Su
leaf 154 óhr  x"arrah be ~ seems to mean: he projected, threw forth, (from his own essence) its (= the earth’s) substance-light, 
leaf 155  Hell] 5324-26, cf s. v. aržan- tkénitan. — Paz. nigerīdan, nigaridan ; NP ntgarīdan, -istan. The spelling nkdl is attes
leaf 156 tan what nisast is to nisastan. | nipastan(npstn '] to fall down, tolie, lay one- self down: ul nipast hénd they laid them
leaf 157 24-25, 2522, 6817-18, — Av. (1754) ni-šad- < ni-had- = OP (caus. ni-Sädaya-); Ps. nšstny nšyd- (for nišiy-); MPrth. nšst
leaf 163 pa0ana-; NP pahn "wide, large’ ; v. also pahnāt. | päh-ast [p'hst'] sheepfold 9411-14, — < päh + ast < Av. (212) asta- ‘ho
leaf 164 pati + Av. (1520) räd- ‘to get ready’ (Skr rddh-). The prev. pat-, generally preserved in the archaistic BP orthogra- ph
leaf 168  the other | www.parsianjoman.org | oe zl wb | passand | side: though according to law a daughter only inherits half as much a
leaf 169 jB: 6-7. (12-13), Prth NGRYN pty ZK wym HQ’YMW-t HajA: 6—7. (11-12); PWN ZK Psy ZY ... = pat hàn rah" 1... on the road t
leaf 173 2d"n'] mart i zan ~ a married man 10026-27; — adj. domi- nating, sup. pätixsä-tar 85, 8612. — 2. em- powered, authorized
leaf 177 2, 392, 493, 652°, with a v. n. or an inf. instead of a temporal clause 4618, 5423; ~ ki 81. 1317, ~ hac han-tčit [ZK *D
leaf 178  "pišt, from "piš-, Skr pinasti ‘to grind’, Av. (907) pt. pišant-. | pistàn [pst’n'] female breast: ~-pān breast bodice, v
leaf 179 f cattle’. | purr-kamakčh [pwl k’mkyh] the quality of being purr-kämak having his will wholly directed to (6) 555. — V. kā
leaf 184 ��to seduce into apostasy’. As for rahiyét cf s.v. apasthistan. | rastar one who escapes: ~ kartan to bring about an escap
leaf 190 re (if a pl., in the cas. obl. —-än): axtarmärän — the chief of the astrologers, the chief astrol- oger 5°. 73-6; artest
leaf 197 āyēm [st’dym] 642°; 2nd p. sg. stāyē [st’yd] 59%; 3d p. sg. stäyet [st>dt'] 9927. 1007; 2nd p. pl. stāyēt [st’dyt'] 601;
leaf 202 te sense is probably found in Av. (1080) ni-xšata adv. ‘below’, pointing to *xšata- ‘lowered’. | šašom [ššwm] the sixth 83
leaf 205 an that they may go and come safely 8723; ka han damistan Sut when this winter has gone 972; hac man šavdi thou shalt go
leaf 207 262°; as long as, as far as, with a nominal clause: ~ yazdän hayydr as long as the gods are helpers F:7; — en- larged by
leaf 208 77. 934. 104%. — Av. (633 sqq.) tanū-; common Ir. | -tàn [t'n'; Ps. -tn] encl. pron. of the pers. | pron. 2nd p. pl. you, yo
leaf 211 2. 895, — Paz. tišnaī; MPrth čšyndyft (MHC). | Tištr [tyštl] a constellation, generally identified with Sirius 875-7. — Av
leaf 214 s [tws] 1. a mythical hero 100*-?. 1066. 1147-9-25, — 2. the town founded by him (now Mašhad) 114*— Av. (657) Tusa-; Tūs
leaf 216 ' =) kašak: ul sräyisn, with the explanation & ki pat aškem [sic = aškamb] dvārēt, cf Skr udara- ‘belly’. All the noxiou
leaf 218  — Pass. of *uz-vädaya- ‘to carry away’, v. Ghilain 71. — Vd. 195 uzvaēdayat is rendered in Phl by uzväst with the gl. | v
leaf 220 Andiyok-Šahpuhr *bet- ter than Antiochos Sahpuhr (built) KZS Prth 1. 26 = Prs 1. 32 init.; Gr. v. Tove Avrıoy LaBwe; Ara
leaf 226 ��clergy’]. | včeišn [wycšn'] decision 1141, v. Wwextan. — Cf 459-14, the OP passage DNa 43-47, and al-Biruni, Chron. 220.
leaf 231 �li kartan ‘to ex- change, to barter’. | "vikastan [wkstn'] "to disappear: *vikast she *disappeared 58°. — Uncertain. It c
leaf 236  [wtyst'] a linear measure, a span = 12 finger-breadth 93°. — Av. (1440) vitasti- | viturt [wtwlt'] v. vitartan. | viyak [wy
leaf 238 which is also the spelling in three of the cities mention- ed 1141? sqq., certainly to be pronounced Xūsrūv = Arm Xosrov
leaf 243 n inf.: the act of searching, research 11217; request 11719, — < guidišn (the SW form with -d- < -z-, V.S. V. x”ästan) w
leaf 245 ] one of the primeval heroes, son of Vivanghan, 3918, 4425, 455, 478. 781, 9012, 1014. 11315, 1147; ~ i šēt = NP Jamšed 
leaf 247 zd?n'] Prth yazatān [y?ztn] HajA:3.4. SPrth 5.7.12, god: Atur ~ 252; Gosurvan ~ 3476-27; Nerösang ~ 60°; Mihr ~ 961; hin
leaf 249  A fine example is the Prth. n. pr. z’hyn KZŠ Prth 1. 24 = Prs 1. 30 y’dyn, Gr. v. Atenv (du- for j-). Cf next w. | zaman 
leaf 253  man hac mātar nē zat hom 2111-12. Artaxsér haciš zāt 27°; haciš pus . . . zāt 1075; — the pres. is act. or pass. : tài 
leaf 269 -: bastan bandaka-: bandak bratar-: brat bümi: bam | -ca, -cà: [-c], -ci cišciy: ciš ciy: -c, -ci | dahyu-: deh | daiva-: dev | 
leaf 272 m Gandarewa: Gandarv ganti-: gandakēh Gao-cidra: Göcihr lgaona-: gönak lgaona-: cigön gaosponta-: Göspand gaoyaoti-: gäv
leaf 278 yšn: bastišn dyn: den dyrdn, d’r-: daštan dyštn, dys-: dištan dyz: diz | fr'e: frac frhynj-: frahaxtan frm’n: framàn | frm’d
leaf 283  girt | gytyg: getik | hn: han | h’myn: hamén | h'wnd, h'wynd: havand | hgryc: hakarc | hm?g, h’m’g: hamäk | hmb’w: ham-bài | hmgwhr: ha
leaf 287 fraron | fraš(ē)gard S | a \ : fraškart | frašn: » | fravaš: fravahr | frazand: ~ | Frazušag: Frazišak | fraž: frac | fréftan, frév-: | fr
leaf 291 tär | giristan, giry-: gristan | göhar: göhr | göspand, gösfand: göspand | gošah: hangösitak | göy: göd | gudäxtan, gudäz-: vitäx- t
```


## [2026-09-06T22:15:12.599Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\npages=open('NYB_vol2_glossary.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (170,171,172):\n    print('===== leaf',i,'printed ~',i-14)\n    print(pages[i][:2200])\nEOF"
}
```


### [2026-09-06T22:15:14.339Z] TOOL RESULT

```
===== leaf 170 printed ~ 156
e prep.: pat... rād (g. v.). — ll. in composition with a subst., forming adjectives with the sense of ‘provided, connected with’: yam i pat-göhr set with jewels 6°; (murvdn i) pat-àp aquatic 93°; zan i pat-göhr a woman of good birth 69%; cigon andar hindükän pat-vicin but high of station 11819-11; — enlarged with the adj. ending -ömand: ka krisäsp pat-tanómand u (pat-)janomand ne bit hah if K. had not been endowed with body (pat-tan) and life (pat-jān) 342. — B. adv. (rare): in addition, moreover 96%; u pat-ic and furthermore 904. The proper adv. be- longing to pat is patiš (g. v.). - OIr *patt (Skr prati), Av. (822 sqq.) pasti, OP patiy; MPrthPrs pd, pt; Paz. pa. In all prob- ability this pa was since old in common use alongside of pač as its sandhi form (cf passaxt, passand etc.), and on it the spelling of the prep. was based by analogy with the Semitic prepositions b-, k-, l-. As however, contrary to the Sem. ws., it maintained its character of an independ- ent w., and independent ona-consonantic
(418, v. božišn), belief (virröyistan pat), | monosyllables are unknown in the Aram. www.parsianjoman.org | perl wb
pat
orthography the Iranians took over, it was necessary to mark it in some way as a word unit. For this purpose the ending -WN, very common in Aram. verb ideograms, was chosen. The form PWN thus created is consequently a spurious ideogr. and has no root in Aram, as I formerly assumed. The transliteration p'', adopted by de Menasce, is an attempt to visualize the spelling (but the real sign of abbreviation in BP is -g, originally probably -k: H-g, Š-g, P-g, FrP 4). - In compounds pat is regularly written pho- netically, only in special cases PWN, cf above A II, ll and some of the following ws. In compounds the genuine SW form pai- is sometimes reflected in the orthography. v. pairdstak, pairāyak, pairök.
patacanbyö [Av.] 6512, not found in the existent Av. texts; probably, through haplology, < *patt-tacanbyē, dat.-instr. pl. of *pati-tacant-, pt. pres. of pati + tac- (v. tacitan and iāxtan), thus ‘in an uninterrupted succession of generations’.
pätan [NTLWN-tn'] päy- [NTLWN., p'dt' = päyet 2512] 1. to guard, to protect, to watch: tan + x“éS be pāyēt: me
===== leaf 171 printed ~ 157
��s care and tenderness. — Cf pat- frazämenit. pātdāšin  [p'td'án' pādāšin [*p’d’än'
5913.25] retribution, reward 38. 5913.25, 719-8 (opp. ävenisn). 808-1? (opp. patifras). 9510-18, 103?5, — < pāt- = pat- (as to the lengthening of -ā- cf Verbum 229 sg.) + dašin (g.v.): MPrs. p’d’syn; Paz. pä- daišn, pädäs(a)n (Mx), NP pädäsan; Talm. lw. prdšn? ‚prdysn’ ‘gift on parting, a farewell present’ Cf Bailey, BSOS VI, 1930-31, 600; Telegdi 250 sq.
patéx"éh [ptyhwyh] welfare, prosperity, well-being 68%. 877. — Abstr. of patéx ‘thriving, prosperous, well-to-do’, render- ing Av. (805 sq.) Orqfada-; < *pati-ax"a-, from Av. (106 sgg.) ahu- ‘life, existence’, v.s. v. pat A II, 11; Paz. patixvi.
patéx"énitan [ptyhwynytn'] to nourish, to cause to prosper 8115.
pätez [p'tyz] autumn 887. — MPrs p'd(y)z (A-H I), Paz. pādēz, NP payiz. V. Bailey, TPhS 1945, 13.
pat-fracéh [PWN pPcyh] appearance 40% (read: api-sän ētēn-aš ~ 6 ham ārāst *,.. his appearance’). 4019, cf 39??, — pat fraceh 52? are two distinct ws., v. frācēk.
pat-fražāmēnīt [PWN ple’mynyt'] pt. = pret. pass. 3d p. sg., was finished 1169-12, — A den. of the expression pat frazdm, v. frazam and cf pat-apakénit.
pätifräs [[p'tpl's], Ps. pätufräs [p’tw- pPsy] punishment 93. 12°. 76H. 808-13, 10112-15, 10218-17.26, 10322, 1288, -NW w.: MPrth p’dyfr’s (MHC), Arm. Iw. patuhas, but SW pätifräh: MPrs p'dypr? h (S); Paz.
| pädafräh. The -u- in pätu-, also found in
www.parsianjoman.org | ool wok
patifras
the books, is due to the influence of the following labial.
patigriftan [ptglptn', MKBLWN-], pati- gruftan [ptglwptn'] pačir- [MKBLWN-, ptyl-], pt. = pret. pass. 3d p. sg. patigrift [ptglpt'; MKBLWN.t, MKBLWN-x, 2876, 299. 611; -x, 21, 18%] patigruft [ptglwpt'] 5811. 6015: to receive, to ac- cept, to take up, often with the prev. frac: 1. Bastvar (PLK”) pat dast fräc patigrift B. caught *the battle-axe (just swung by the attacking enemy) with his hand 2875-26; barak xvēš pat dast frac patirét he himself takes command of the steed (by grasping the reins) with his hand 299. — 2. en den i mäzdesnän hac Ohurmazd patigrift he received the Maz- dayasnian religion from O. 18%2?sq. 1919, ete.; hàn 4 Evak frāc patigrift u apārīk hac dastavar
===== leaf 172 printed ~ 158
w-; MPrs pdyryfin pdyr-, v. Verbum 205, Ghilain 89; Paz. padiraftan padir-, NP pačiruftan pačir-.
patigriftaréh [ptglpt'lyh] reception 731. Tola;.,
patirak [ptylk'] a meeting: bam-é i hac ~ + (a light produced by the meeting of...) a light reflected from, a reflexion of 11218; — mostly combined with a vb. of motion: 0 ~ āmatan to meet 84. 731-2! ete. ;
156
patiš
as an adj. ~ bütan to meet 85; či peš nemak Vahuman ~ āyuxt V. driving in from in front met him 5617-18; — as a prep.: ~ zanišn + hac Ganak Menoi im- mediately before being slain by the Evil Spirit 405-5, — From pati + ar- ‘to move’, Av. (183) patti-lar- ‘to advance against, to be hostile to’, cf (74) a-pattt.srota- *un- checked’; MPrs pdyrg ‘against’; Paz. padira; NP paóirah; ci paitiyärak.
*Patiritaräsp [ptylytPsp'] the paternal grandfather of Zartuxst 3726, 3841.15.16, 4625, — Various spellings: BdA p. 234!5 p'ytlsp, 235? pyltl’sp', 23615 pylt’sp; Zsprm VII, 1 pltPsp'. In my opinion it goes back to *patorstara-aspa-, in which *pateratara- is haplology < *patorota- tara-, comp. of Av. (821 sg.) patarota- (for *patorsta-) ‘flying’: ‘whose horses are almost flying’ (?).
patīsār [ptys']] unbroken succession: throughout, from the first to the last
- 120%. — Paz. paösär (Skr v. prakdra,
SGV XV, 50); NP padisdr ‘taking up and finishing any business which has already been begun’ (possibly a learned w.).— < *pattš-sār < *patisa-sära- ("head onward'') ‘continuous forward move- ment’.
patiš [pts] adv. 1. before (= pēš), with hac: ~ hac zāyišn i ... before the birth of ... 365. — 2. used instead of pat if it refers back to an encl. pron. in the be- ginning of the sentence: cē-m anākēh vas ~ kunēnd (BYDWN-x;) for they will do much harm to me 954; i ka-t anākēh ~ kuném for we shall do. harm to thee 76°; api-š dēvān apasós ~ kunénd and the devs sneer at him 7576-2"; api-ščin ~ nē virroyam and I do not believe in them 64%; cigan ka-šān Sir i garm ~ andar dösend as if warm milk were milked upon them 10121-22; 4228; 8024-26; 9825-26, . 3, as a substitute for the prep. pat + the encl. pron. of the 3d p. sg. -$: on, to, at (etc.) him, her, it 4?6. 3212, 4726, 559.16, 6311.16, 6420.24 6614, 801, 8615.
www .parsianjoman.or
```


## [2026-09-06T22:15:21.624Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"patkar\\|patkār\\|patkāl\\|paikar\" NYB_vol2_glossary.txt | head -20; echo \"=== leaf173-174\"; python3 - <<'EOF'\npages=open('NYB_vol2_glossary.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (173,174):\n    print('===== leaf',i); print(pages[i][:2000])\nEOF"
}
```


### [2026-09-06T22:15:23.462Z] TOOL RESULT

```
2241:äyet do ye proclaim that every man shall come to King V.’s court 205-6; Dahäk hàn and zaman ‘BYDWN-x, cand ... to D. as long a time will be assigned as (to allow him to...) 997; ristäxez etón kind ka he will determine the Resurrection at the time when ... 3422; atän hàn 4 kart axtäyisneh (q. v.) dahet he will create un- willingness with regard to what is in- stituted by you 451; of the marriage contract: mart u zan évak apäk dit kämak bavēt, räyenend u ‘BY DWN-x, man and woman will fall in love, become engaged (v. räyenitan) and contract marriage 1044-25; zan kartan u patvand i geteh rayénitan to marry a woman and settle his family ties in this world 631%; PLK?... pat čip $ banjak kart éstat the axe was enchanted (dedicated to Hell) by means of banjak (q. v.)-water 2516-17, 284; Sah- puhr ... āpān xānak kart Sh. founded (instituted) a temple for the Waters 10914-15; the same meaning undoubtedly also in the expression šahristčin kart 113— 116; šahristan ... pat Sapistan kart was declared a harem-city 116?4-?5, — Av. (448) 2kar- ‘to recollect, to mention, to com- mend’ [from which in all probability ham + the caus. in the set phrase nivaé- čayemi hankčirayemi ‘I consecrate, I de- dicate’ (not from !kar- as Bthl. has 1t)]. First proposed by Pagliaro, RSO XXIII, 1948, 67-68 (v.s. v. ?kartak); followed up by A. Périkhanian, REA, N.S. V, 1968, 22, VI, 1969, 8, quoting the Arm. lw. &ar [< *éarna-] ‘festival oration, ho- mily’. Of course in BP as we now have it BYDWN- has always been read as kun-, but the original pres. must have been kar-, as the NW pres. of kartan ‘to make'.— V .?kartak, kartäreh (1), hangartan, nikerdi, nikeritan, patkārītan, uskärtan.
3053:patkaritan
3059:patkar [ptkly, Prth ptkr]image ŠPrs: 3. 14. Prth:4. — OP pati-kara-; MPrs phykr; Arm. lw. patker ; Syr. Talm. lw. ptakrä ‘an idol’, Mand. lw. patikrä; NP paikar.
3060:patkär [ptk?l], pitkär [pytk'l] quarrel, controversy, dispute 4519-12 [pit-]. 70". 1081. — MPrs phyk?r (A-H II; meaning: quite clear); Paz. patkür; NP patkār; v. ?kartan and uskartan.
3062:patkarit [—-yt'] altercation, quarrel 572. patkäritan [~-ytn'] to dispute, to dis-
4919:pati-kara: patkar
5674:pdk’r: patkaritan
6073:phyk"r: patkar
6075:phykr: patkar
7302:paigàr: patkar
7306:paikar: patkar
=== leaf173-174
===== leaf 173
2d"n'] mart i zan ~ a married man 10026-27; — adj. domi- nating, sup. pätixsä-tar 85, 8612. — 2. em- powered, authorized; as an impers. vb. in a neg. sentence: né ~ bé ka it is not authorized, lawful except when = it is necessary that: nē — bē ka šavēt it is not lawful except when he goes = he is compelled to go, he must needs go, cf
Bthl, ZsR I, 29, n. 2; né ~ bē ka kunihet ©
(it is not lawful except when it [i. e., the sum of the religious duties] is fulfilled =) the chief religious duties must absolutely
157
patkaritan
be fulfilled 65?! (cancel the rel. pron. <i> at the beginning of l. 21 and join the preceding clause bē kē karr aivāp gung ēnyā, 1. 20, to 1. 21: "With the exception of the deaf and dumb, the religious duties must be fulfilled by everyone’). — Ps. p’ths’dy; Paz. pidišah, NP pādšā(h), cf next w.; ef MPrth vb. pdyx$h- ‘to rule’; from pati + Av. (551 sqq.) zšay- = OP; v. Verbum 229 sq., BBB 95 sq.; Bailey, BSOAS XII, 1948, 328 sq.
pātixšāyēh [p'thi?^dyh] domination, do- minion, power, supremacy, kingdom 25.1. 517.26, 5916 etc. — Paz. pādišāhī; MPrs pdyxsny (A-H I -’dy, but corrected in A-H III to -ny = BBB); MPrth pds nyft.
pátixíayómand [p’ths’d’wmnd] possess- ing power: katīk ~ the master of the house 95”.
pätiyävand [p’tyd’wnd] mighty, power- ful, dominant, comp. ~-tar with hac prevailing upon 321°, 3312-13, 8018, — Paz. pädyävand. |
patkaitan [ptk’ptn'] patkaf- to let fall, to let loose, to shoot off (an arrow) 1005-? (patkäfom). — Caus. of *pati-kaf-, ci MPrs phykf- ‘to fall down’, Verbum 173; Ps. phk’pty ‘spread out, founded’. Cf kahvan.
patkar [ptkly, Prth ptkr]image ŠPrs: 3. 14. Prth:4. — OP pati-kara-; MPrs phykr; Arm. lw. patker ; Syr. Talm. lw. ptakrä ‘an idol’, Mand. lw. patikrä; NP paikar.
patkär [ptk?l], pitkär [pytk'l] quarrel, controversy, dispute 4519-12 [pit-]. 70". 1081. — MPrs phyk?r (A-H II; meaning: quite clear); Paz. patkür; NP patkār; v. ?kartan and uskartan.
patküri$n [---šn'] discussion, disputation 1095, |
patkarit [—-yt'] a
===== leaf 174
guess is only proposed faute de mieux.
patmin [ptm’n'] measure 915; contract 778; moderation, modesty 7019-21, 8517; maturity 225 (opp. araséh). — MPrth pdm'n; MPrs pym?n; Paz. pačma(n); NP paimän; from pati + Av. (1165 sq.) mäy- ‘to measure’ = OP.
patmanak dimension 931, patmänik moderate, restrained 6919. 7027.
patmänikihä proportionally, in due pro- portion 89?9, — Paz. pačmanihi.
patmöcan [ptmwen'] garment 2!?. 171, — Arm. lw. patmucan; MPrth pdmwen; M Prs pymwen; v. next w.
patmóxtan [ptmwhtn'] patmöc- to dress oneself, to put on one's clothes 218. 8515, — Cf Av. (837 sq.) pasti.Smuxta- ‘shoed’; MPrth pdmwatn pdmwe/j- (MHC); MPrs. pymwatn pymwc-; Paz. padmöztan pad- mož-; NP paimostan paimoz-.
tpatnäsik [tptn’syk] 41? an abortive emendation, restore pt’syk = pattahik.
patpursitan [ptpwrsytn'] to read: api-m framät? patpursēt and I ordered (Someone) to read it = I ordered it to be read P 2: 4. — OP pati-prs- (Kent s. v. fra0-); M Prth pdbwrs-; MPrs pahypwrs-, phybwrs- ; Verbum 196. 228. V. pursitan.
patran [ptl’n'] resistant, refractory, of the boar 262°. — Corresponds to the Av. (828) epithet of the boar pattt.srona- (var. paiti.rana-, paitirena-) which has been remodelled under the influence of ran ‘side’ (q. v.).
pätrazm [p’tlem] counterattack 2719, v. razm. — Arm. lw. paterazm ‘war, battle’.
patrče [p’tlwe] *splendour: veh ~ of good splendour 271°. — Ps. ptlwk renders Syr zīwā Ps 96%; Av. (1487) pazti-raok- caus. ‘to make flame up’.
pat-säxt [PWN s*ht']: v. passdat.
pat-sén [PWN syn'] breast bodice 5718, — DkM 63514-15: apar-ic 6 tē, Zartuxst, druž bē dvārēt mätak-karp, zarren-patsen (ku pistin-pin dārēt), v. pistan. — FrP 31 sénak, NP sinah ‘bosom, breast’.
pattahik [pt’syk: this reading is to be restored 417] in consecutive order, one after the other. — FrP, S, XIV, 5; patisär (g. v.) glossed by NP paččihi = Phl patahik; pattāh alternating with pattāt (v. the next w.) according to the common SW phonetic rule; -s- inverse spelling of -h- asin ls = rah, g's
```


## [2026-09-06T22:15:48.360Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"===PHD===\" && grep -n \"patkār\\|patkar\\|angārdan\\|angārd\\|hangārdan\\|škār\\|wigārdan\\|wigār\\|kirrog\\|kardan\\|kirrēn\\|hāwišt\\|ašāgird\\|hašāgird\\|dastgird\\|-gird\\|pargār\" PHD_mackenzie.txt | head -40"
}
```


### [2026-09-06T22:15:48.404Z] TOOL RESULT

```
===PHD===
734: ,.., kardan: open .
735: ..... kardan az: disengage from, wean.
1372:   - kardan: remember.
1406: ,... guftan, ,... hangirdan, - kardan, pad ..... distan: thank, give
1911:dast(a)~ird [YDE-, dst-krt l I M dstygyrd, N dastgird] estate.
2521: ...... kardan: gather, collect (tr.).
3197:kar-, v. kardan.
3227:kardan                            SO                          kehtar
3228:kardan, kun-, (P kar-) [OBYDWN-ln' < A ..,j<bd; krtll', kum-, (kl-) I
3304:kirih- [OBYDWNyh-, V. kardan, klyh- I M k,,,ryh-] be done,
3309:kirrog [k(y)lwk I M qrwg] artisan, craftsman; skilled.
3352:kun-, ,...,isn, v. kardan, kunisn.
3740: -- kardan: look.
3834: - ham kardan: gather (tr.).
3917:padiran                           63                       pahikardan
3973: pahikardan, 2pahikar- [ptk)l-tn ] request, claim, consult.
4377:raz·kirrog [l'e kylwk l I M r'z qrwg] architect, builder.
4885:    - kardan abar, 0: attack.
4923: ,ow    kardan, -- menidan: abuse, despise.
5070:uskardan, uskar- ['wsk'l-tn I J ......, (N sigal-)] think, consider, discuss.
5125:wad-girdag [w'tgltk ' I (N gird-bad)] whirlwind.
5209: ...... kardan: learn by heart, memorize.
5418: ...... kardan: send, despatch.
5876:a e(w).                                   act (v.) kardan, warzidan.
5896:abuse (v.) tar kardan / menidan.          advocate Jiidag-go(w).
5945:amber kahruba(y).                         architect raz-kirrog.
5971:artisan hutuxs, kirrog.                  authorized padixSii(y).
5973:arts kirrogih.                           average mayiinag.
6007:attack (v.) pahikaftan, tag kardan       base bun, fragan, payag.
6106:boy, v. lad, page, son.                builder raz-kirrog.
6194:claim pahikardan.                        commission gumardan.
6260:  osmurdan, uskardan.                        corner gosag.
6270:consult pahikardan.                          corvee begar.
6298:craftsman kirrog.                          daevic creature wisudag; v. noxious.
6299:craftsmanship kirrogih.                    dagger ceHin. dasnag.
6357:    niiydag.                                despise tar kardan I menidan.
6405:dip ogra.                               do kardan.
6422:disengage from abaz kardan az.          double doganag.
6671:gather (vt.) cidan, gird kardan, 0 ham           hupiidixsayih; ,..., ruler hupadix-
6672:    kardan, harrob-, P amwastan.                 sii(y); ,..., speech hiixt; ,..., spirit
```


## [2026-09-06T22:15:49.835Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"===CHEUNG kar===\" && grep -n \"^\\*kar\\|\\*kar-\\|hankar\\|han-kar\\|angār\\|\\*wi-kar\\|škār\\|patkār\" CHEUNG.txt | head -40"
}
```


### [2026-09-06T22:15:49.898Z] TOOL RESULT

```
===CHEUNG kar===
9355:also be lurking in Sogd. wn- (next to kwn-, s.v. *kar-), Khot. yan- (s.v. *kar-) ‘to do, 
15502:*kar8/*xrah. 
15768:*kar ‘to do, make’ 
15819:*kar 237 
15919:*karé ? ‘to strike’ 
15927:*karH2 239 
15939:*kard ? ‘to stick, keep down ?’ 
15960:*karH! ‘to celebrate, praise’ 
15984:*karH ‘to spread out, scatter (esp. seed), sow; to make furrows, plough’ 
15989:*karaja- ~ *krsta- (i.e. root *kars-/*xrah-) in Pir. cf. Emmerick 1966: 612; Sims- 
16012:(SGS: 50) derives LKh. naskirr- from a root *kar- ‘to cut’, PIE *(s)ker-, which is not 
16048:*kars/*xrah 241 
16074:*karp ? ‘to lament, moan, mumble’ 
16092:*kars/*xrah ‘to draw, plough’ 
16172:*kartl 243 
16180:*kars-/xrah- and *karH’- either show mutual influence, cf. Sh. kiräx(t), etc., or are 
16196:*kart! ‘to cut’ 
16271:*kart? ‘to twist, turn’ 
16305:*karz ? ‘to cheat, deceive’ 
55117:*kard (s.v.), *tund 
55142:*kar (s.v.), *pas (s.v.), *sam 
55321:*kar (s.v.), *sac’, *tary (s.v.), 
56193:*kart', *saH, *tas, *9uars, 
56353:*kar, *uarz 
56434:*kar (s.v.) 
57096:*kar, *tas 
57106:*karH? 
57242:*karp 
57363:*kar (s.v.) 
57374:*karH’, *karš/*xrah 
57384:*karH'! , *stau 
57679:*karH’, *9ràs, *yap' 
57949:*karH°, *tau 
58076:*karc, *namH, *sna9H, *xad 
58145:*kar (s.v.), *man, *paH' 
58247:*karť , *naj, *tarc, *uar, 
58250:*kart’, апе, *tap
```


## [2026-09-06T22:15:52.339Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15768,15830p' CHEUNG.txt"
}
```


### [2026-09-06T22:15:52.385Z] TOOL RESULT

```
*kar ‘to do, make’ 

*AVESTAN: kar- ‘to do, make’ || (+ *fra-) ‘perficere’ || (+ *ham-) ‘to perform a Yasna 
for someone’ = Liste: 14f. 

Pres. nu-: IND. 1sg. YAv. kerenaomi (V 21.6, V 21.10, V 21.14, Vyt 49), 25р. (?) YAv. kərənüši (Y 
10.13), 3sg. Y Av. koronaoiti (V 13.41, V 13.51, V 19.43, etc.), 3pl. YAv. "koronuuainti (Yt 13.26), impf. 
lsg. YAv. akoronom (V 22.1, V 22.8, V 22.14), impf. 2sg. Y Av. akoron(a)uuo (Y 9.15), impf. 3sg. (?) 
Y Av. frakoronaot (X3 V 22.2), INJ. 3sg. YAv. koronaot (V 2.32 f., V 2.36, V 2.38, etc.), SUBJ. 1sg. 
YAv. keronauuani (Yt 15.16, Yt 15.20, Yt 17.57, etc.), 3pl. OAv. koronaon (Y 30.9), 3pl. YAv. 
koronauuan (Yt 19.11), OPT. 3sg. YAv. kerenuiiat (V 14.17, V 18.10, VdPZ 18.51 f., Мр 14), YAv. 
koronoit (FrK 73), Y Av. frakoronoit (ViD 15), IMPV. 2sg. Y Av. koronüiói (Y 9.28), Y Av. koronauua (V 
2.25, V 2.28, У 2.30), impf. IND. 3sg. (?) YAv. frakoronaot (V 22.2); Aor. athem.: INJ. 3sg. OAv. cörot 
(Y 44.7, ? Y 45.9), SUBJ. 1sg. OAv. carani (Y 44.17), 3sg. OAv. caraiti (Y 51.1), OAv. carat (Y 46.4), 
OPT. 3sg. ? OAv. coirit (Y 45.9, Kellens — Pirart 1991: 193), IMPV. med. 250. OAv. korosuua (Y 40.1); 
Perf.: IND. 3pl. YAv. *caxrara (V 4.46); Partic.: pres. YAv. koronuuant- (Fr.), perf. pass. YAv. ?korota- 
(Y 26.9, Yt 10.128, V13.23, V 19.30), etc.; Pass.: pres. IND. 3sg. Y Av. kiriieiti (Yt 10.111), 3pl. ҮАУ. 
kiriieinti (V 3.9). © The form YAv. koronüsi can also interpreted as (emend.) med. 2sg. "koronüse, 
Hoffmann - Forssman 1996: 215. 

*OLD PERSIAN: kar- ‘to do, make, build’ — Kent: 179a 

Pres. nu- IND. 3sg. kunautiy <ku-u-n-u-ti-y> (DNb 24), <ku-u-n-u-[t]-[iJ-[y]> (DSs 3), 
<[ku]-[u]-[n]-u-t-i-y> (055 4), impf. lsg. akunavam <a-ku-u-n-v-m> (A’Sd 3), akunäm 
<[a]-[ku]-[n]-a-m> (XSc 3, ? A?Ha 5), ? akuvanasäsa <a-ku-v-n-8-a-8> (A’Sde 3), 3sg. akunaus 
<a-ku-u-n-u-8> (D'Sb 3), akunas <a-[ku]-u-n-8> (A’Sa 3 f), 3pl. akunava", med. 3pl. akunava"tà 
<a-ku-u-n-v-t-a> (DB 3.12, DSf 48), <a-[ku]-[u]-[n]-[v]-t-a> (DB 5.6), SUBJ. lsg. kunavanaiy 
<ku-u-n-v-a-n-i-y> (081 4), 2sg. kunavahy <ku-u-n-v-a-h-y> (DB 4.75, DB 4.79), med. 3sg. kunavätaiy 
<ku-u-n-..-v-a-t-i-y> (DNb 56), IMPV. 3sg. kunautuv <ku-u-n-u-tu-u-v> (DB 4.76); Aor. athem.: IND. 
med. 3sg. akuta <a-ku-u-t-a> (DB 1.47, CMb 4), I pl. akumä <a-ku-u-m-a-> (DB 1.90), IMPV. med. 2sg. 
kuSuva <ku-u-8-u-v-a> (DNb 50); Perf.: OPT. 35р. caxriyä <с-х-г-і-у-а> (DB 1.50); Partic.: perf. pass. 
karta-; Inf.: cartanaiy <c-r-t-n-i-y> (DB 1.94, DB 2.33, DB 2.44, etc.), <c-r-t-n-i-y> (2.38), <c-r-t-n-i-y> 
(DB 3.43, DB 3.65); Pass.: impf. IND. 3sg. akunavayatä <a-ku-u-n-v-y-t-a> (DB 1.20, DB 1.24, akariya 
<a-k-r-i-y> (DSf 37, XPh 42), 3р1. акагіуа"іа <a-k-r-i-y-t-a> (DB 3.92), OPT. 3sg. kariyais <k-r-i-y-i-8> 
(DNb 9, DNb 11) 

*MIDDLE PERSIAN: MMP kwn-, qwn-, BMP kwn- (‘BYDWN-) /kun-/ ‘to make, do’ || 
(+ *us-) BMP ’wsk’l- /uskar-/ (caus.) ‘to think, consider, discuss’ || (+ *pati-) BMP 
ptk’1/pahikar-/ (caus.) ‘to request, claim, consult, MMP phykr, BMP ptkl /pahikar/ 
‘picture, image’, MMP phyk’r, BMP рік? /pahikar/ ‘battle, struggle’ || (+ *ni-) 
MMP ng’r- (caus.) ‘to paint, draw’, MMP ner ‘picture’ || (+ *ui-) MMP w(y)c’r- 
(caus.) ‘to separate, divide, spread, interpret, decide....; perform, accomplish’ || (+ 
*ham-) MMP hng’r- (orig. caus.) ‘to (ac)count, reckon’, BMP hng’l- /hangär-/ ‘to 
perform, offer (thanks); calculate, determine; consider > DMMPP: 213b f., 275a, 
240b, 351b, 181a 

Widely attested: Pres.: IND. 1sg. MMP qwnym, "kwnym, 3sg. MMP kwnyd, etc.; Partic.: pres. MMP 
kwn'n, perf. pass. MMP qyrdg, MMP kyrd, дуга, Pass.: pres. IND. 3sg. MMP kyryhyd, 3р1. MMP 
qyryhynd, SUBJ. 3sg. MMP qyryh'd || (+ *us-) Caus.: pres. IND. 3pl. BMP ’wsk’lynd /uskarénd/, 


*kar 237 


sk’lynynd /skarénénd/; Partic.: perf. pass. caus. BMP ’wsk’lt /uskard/ || (+ *pati-) Caus.: pres. IND. 3pl. 
BMP ptk’lynd /pahikarend/ || (+ *ni-) Pres.: IND. 3sg. MMP ng’ryd, 3р1. MMP ng rynd; Partic.: perf. 
pass. MMP ng’rd || (+ *ui-) Pres.: IND. 3sg. MMP we’ryd, IMPV. 2sg. MMP we’r, Partic.: perf. pass. 
MMP wyc’rd || (+ *ham-) Caus.: pres. IND. 35р. BMP hng’lyt /hangaréd/, 3р1. MMP hng’rynd, BMP 
hng’lynd /hangarénd/; Pass.: pres. IND. 3pl. MMP hng’ryhynd (M7983 I Vii,11); Partic.: perf. pass. BMP 
hng’It /hangard/ 

*PARTHIAN: kr- ‘to do, make’ || (+ *pati-) pdk’r- ‘to contend, strive’, pdkr ‘picture’ || 
+ *fra-) ? ‘frg’r- ‘to be dejected’ || (+ *ni-) ng’r- ‘to paint, draw’, ng’rgr ‘painter’ ||
```


## [2026-09-06T22:15:58.320Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15830,15925p' CHEUNG.txt"
}
```


### [2026-09-06T22:15:58.371Z] TOOL RESULT

```
+ *fra-) ? ‘frg’r- ‘to be dejected’ || (+ *ni-) ng’r- ‘to paint, draw’, ng’rgr ‘painter’ || 
(+ *ui-) wyc’r- ‘fulfil, perform’ = Ghilain: 57, 73 f. | DMMPP: 207 f., 269b, 85b, 
351b 

Pres.: IND. Isg. kr’m, 25р. qryh, 35р. kryd, qryd, 1р1. “kr’m, 2р1. Куа, 3р1. krynd, qrynd, SUBJ. 1sg. 
kr’n, 25р. kr’h, 3sg. kr’h, OPT. 25р. qryndyh, IMPV. 2sg. kr, 2pl. kryd; Partic.: perf. pass. kyrd; Inf.: 
kyrdn, qyrdn || (+ *pati-) Pres.: IND. 3pl. pdk’rynd || (+ *fra-) Pres.: IND. 1pl. ‘frg’r’m || (+ *ni-) Pres.: 
IND. 3sg. ng ryd || (+ *ui-) Pres.: IND. 25р. wyc ryy, 3sg. we’ryd, wyc’ryd 

*KHOTANESE: yan- “о do, make’ || (+ ui-) LKh. güjsar- ‘to harm, injure? = SGS: 
110 £, 29 

*SOGDIAN: SSogd. (k)wn-, BSogd. (k)wn-, CSogd. wn- ‘to do, make, perform, 
cause’, SSogd. (”)krt- (pass.) ‘to happen, occur; to become, be situated’ || (+ *pati-) 
BSogd. ptkr'k, ptkr'kw, ptkr'y, CSogd. ptq'ry (m.) ‘image’ || (+ *ui-) ? CSogd. 
wycyr’mnty (m.) ‘explanation’ (< Wir. ?), Sogd. w(y)c( rt ‘exactly’ 

Widely attested: Pres.: IND. 1sg. MSogd. kwn’m, 2sg. BSogd. wn’y, CSogd. "um, 3sg. SSogd. kwnty, 
BSogd. kwnty, MSogd. kwndyy, MSogd. qwndyy, etc. 

*CHORESMIAN: m/k- ‘to make, do’, (+ d") to say’ || (+ *abi-) ? m/’Bk’ry- ‘to look up’ 
|| (+ *pati-) pckr- (denomin. ?) ‘to set, put up (spear)’ || (+ *fra-) sk’ry- (caus.) ‘to 
colour, paint’ || (+ *ham-, *ni-) m/nk’ry- ‘to settle (a score) with someone; to say 
goodbye ?’. © The forms of m/k- with frequent diacritic tasdid | ] in Arabic script 
apparently point to assimilation of the consonant group *kn- (without *-r- !): > -kk-. 
|| Althought it is not entirely clear whether m/’Bk’ry- does contain the root *kar, the 
relation to Yi. uZér-/uZur, M. uZar-/uZir is surely undeniable, in view of the meaning. 
= Samadi: 94, 1, 141, 192, 128 

*BACTRIAN: к1р- ‘to do, act, make, etc.’ || (+ *pati-ham-) midayynp- ‘to agree, settle’ 
|| (+ *ui-) owonp- ‘to argue, quibble’ || (+ *ham-) ? ayyapyo, ayyapyo, ayyapayo 
‘property (in land), estate’. 0 Sims-Williams compares о1стр- with MMP w(y)c’r-, 
Sogd. w(y)c()rt. > S-W, Bact.: 199a, 177a, 217b, 213, 218a 

*NWIR: Widely attested: NP kardan/kun-, Bal. kan-/ku(r)t-, Kurd. (Kurm.) kirin/ki-, 
(Sor.) kirdin/ka-, Zaz. kerdis/ken-, Awrom. kardáy/kar-, Abyan. kardan/e-kar-, Anar. 
-ike/eker-, Ard. käd/ker-, Fariz. kärdän/-kär-, Yar. kärdän/-kor-, -kär-, Gz. ker-/ke-, 
kart, Gil. (Rsht.) kudoen/kun-, Gur. (Kand kärd-/-kär-, Ham. Кагійп/Кег-, Isfah. 
Кагійп/Кег-, Jow. bam-Ka/a-Ker-, Meim. bem-Ka/a-Ker-, Khuns. kir-/kirt, Khr. 
hi-kerd/hi-ker-, Mah. kir-/kär-d, Nn. kärtin/kir-, Natan. -kärd-/kor- (1sg.), kär-, 


| 


238 *karé ? 


Qohr. Ка(гаа)/Кег-, Semn. -kärd-, -kürc-/-kür-, Sang. hä-kärt-/hä-kän-, (subj.) 
hä-kär-, Shamerz. ha-kordan/ha-kon-, Siv. k(y)ar-, k(y)er-, kir-/k(y)erd, kird, Soi 
kärd-/kir-, Sorkh. ha-kärdan/hä-koen-, Lasg. hä-kärd-/hä-kän- ‘to do, make’, Kurd. 
(Kurm.) kärin/kär-, kanin/kan- (caus.) ‘to be able’, Awrom. kıriay/kıria- (pass.) ‘to 
be done’ || (+ *us-) NP sigälidan/sigäl- ‘to think, meditate (mischief)’ || (+ *pati-) NP 
paykar ‘picture, statue’ || (+ *ni-) NP nigastan/nigar- ‘to paint’ || (+ *ham-) NP 
ingastan/ingar- ‘to suppose; consider, believe’, angaridan/ angär- ‘to think, imagine, 
estimate; to paint, figure’, Yar. -hängäst/-hängar-, Jow. angor-/ (supplet. bam-vot < 
*yat), Meim. bem-henga:ft/a-heger-, Khuns. éngar-/engast, Nn. -Engäst/engar-, 
Natan. -hängäst ‘to talk, speak’, NP angärah ‘revenue-book, cash-account’ 

*NEIR: Oss. I. kenyn/kond, Купа, D. kanun/kond, kind, Pash. kawol, kral, Sh. (Baj.) 
kin-/Cüd, Rosh. kin-/ctig, Sariq. kan-/Cewg, Yzgh. k"on-/keg, Ishk. ken-/kül-, Yi. 
ken-/kor-, M. kan/ker- ‘to do’, Yghn. kün-/ikta, Wa. car-/kort ‘to do, make’, 
(redupl.) Wa. korc(o)r-, koc(o)r-/ke(r)kayn-, ko(r)cart- ‘can, to be able’ || (+ *abi, 
*aua- or *ui-) ? Yi. uZér-/uZur, M. uZar-/uZir ‘to perceive, look’ || (+ *ham-) ? Oss. I. 
enk’aryn/enk’ard (pref. sec. ?), D. ank’arun/enk’ard ‘to feel, comprehend’ (< NP 
?), Pash. angur ‘agreement’ 

*MISC: Par. kan-, kur-, kör, Orm. k-/dak ‘to do, make’ (< Pash. ?) = k-/däk, Orm. 
kin-/kinok, kin-/kwulak ‘to copulate’ (euphem.) = kan-/kanók 

*SANSKRIT: kar ‘to do, to make, to act’ (RV+) = EWAia I: 307 

© The rather generic ‘to do, make’ has apparently developed into more specific 
activities, ranging from “painting, depicting’ to ‘arguing, fighting’. 

*PIE *k”er- ‘to do, make, construct’? = LIV: 391 | Pok.: 641 

*IE COGNATES: Hitt. /kuer-/ ‘to cut’, Welsh paraf ‘to process’, Olrish cruth ‘form’, 
Lith. kung (kürti) ‘I found, build’, etc. 

*REFERENCES: KPF I: 82b, 143b f., 207b f., 247b f.; Ivanow 1926: 420, 426; EVP: 34; KPF II: 207 f.; 
IIFL 1. 266a f., 398a f.; Christensen, Contributions I: 71, 168 f., 261; Christensen, Contributions II: 60 f., 
116 f., 161; Abrahamian 1936: 116, 130; IIFL II: 196, 217b; Lambton 1938: 42b, 78a; Abaev, Slovar’ I: 
579; Andreev — PeSéereva: 275b ff.; MacKenzie 1966: 100; EVS: 40b; Lecoq 1974: 58; WIM I: 70; WIM 
H/1: 78; WIM Ш: 110 £; Werba 1997: 168 f.; Paul 1998: 303; Steblin-Kamenskij 1999: 112, 218; 
Cabolov 2001: 518, 514 f.; Lecoq 2002: 108 f., 138 ff. (passim); Kiefer 2003: 199; Korn 2005: 314, 393 
(passim) 


*karé ? ‘to strike’ 

*PARTHIAN: (+ *ni-) ? ngwrc- ‘[pejorative] to baptize’ (-c- < ?). Ф According to 
Sundermann 1981: 90, n. 1 the meaning is from ‘niederschlagen’ [‘to strike down’], 
ie. “gewaltsam niederbeugen und untertauchen (?) [Чо push under by force’]. 
c DMMPP: 241a
```


## [2026-09-06T22:16:15.928Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG skar/škār ===\" && grep -n \"škār\\|skar-\\|\\*skar\\|sikär\\|Sikär\\|hunt\" CHEUNG.txt | head -30; echo \"=== PHD wigardan/škār ===\"; grep -n \"wig'r\\|wigār\\|wig&r\\|Skar\\|Sk'r\\|škar\" PHD_mackenzie.txt | head -20"
}
```


### [2026-09-06T22:16:15.986Z] TOOL RESULT

```
=== CHEUNG skar/škār ===
1443:*NEIR: Yzgh. veZ ‘partner (in hunting, sharing the bag made)’ (< *bajia-), Wanji wej 
6560:Pres. them.: IND. med. 3pl. YAv. fiiaghuntae? (Yt 5.120); Partic.: pres. YAv. fiiaghuuant- (Yt 16.10). 0 
7600:*IE COGNATES: Gr. gó vog ‘murder’, Arm. gan ‘strike’, Russ. gon ‘hunt’ 
9469:*IE COGNATES: Hitt. /salk-/ ‘to knead, to mingle’, Olrish selg (f.) ‘hunting’, MHG 
13757:belong here, v. *yaiH ‘to hunt’. 
14745:‘to drive, hunt’ (Pokorny: 512; LIV: 315 f.). 
15805:(+ *us-) BMP ’wsk’l- /uskar-/ (caus.) ‘to think, consider, discuss’ || (+ *pati-) BMP 
18422:*NEIR: (+ *ati-) Wa. tan(a)y-/tanat- ‘to drive, chase (cattle) into the stable; to hunt, 
20043:*PARTHIAN: pzd- ‘to scare, frighten’, pzdgr ‘chaser, hunter? = Ghilain: 53 | 
21597:*AVESTAN: (+ *fra-) ? Y Av. frasiiazj- ‘to hunt, chase after’ — Liste: 62 
22149:*saru ? ‘to hunt’ 
22153:*KHOTANESE: (+ *fra-) hasura-, hasura- ‘quarry, hunted beast’ 
22155:*NEIR: Oss. I. suryn/syrd, D. sorun/surd, Yzgh. sard/sar- ‘to track, hunt’ 
22157:*MISC: Toch. (LW) A saru, B serwe ‘hunter’ 
22567:*skar 345 
22594:*skar ‘to pursue, drive, look for (the cattle)’ 
22596:*AVESTAN: ? Y Av. skar- ‘to pursue (?)'. 0 The meaning of the Av. compound YAv. 
22605:“hunting-ground, wilderness’ 
22607:*PARTHIAN: ‘Skr- ‘to hunt, chase’ = Ghilain: 58 | DMMPP: 92a 
22627:346 *skard 
22630:*NWIR: NP 3ikar ‘hunt’ (LW ?, < Sogd. ?) || (+ *ui-) NP bisgar(d) ‘hunter, fowler; 
22631:place for hunting; chase; game’ 
22638:Skör-/skär-, M. skör-/skar- ‘to send (a thing)’, ? Pash. skärol ‘to incite (against) || (+ 
22650:*skard ‘to pierce (through)’ 
22670:© The evidence for Ir. *skard is (mainly) confined to Khot. and Sogd. 
22681:*skarf ‘to stumble’ 
24359:tazn-/tazna ‘to drive, hunt’, Natan. -tázáná/táz- || (+ *para-) NP pardäxtan/pardäz- ‘to 
26264:*AVESTAN: ? OAv. vad- ‘to break through, hunt’, YAv. vada- (m.) ‘wedge’ (V 14.7), 
26684:*uaiH ‘to hunt, chase; to run’ 
26685:*AVESTAN: ҮАУ. vaii- (vae-, vi-) ‘to hunt, chase’ || (+ *apa-) ‘to chase away’ 
=== PHD wigardan/škār ===
```


## [2026-09-06T22:16:17.285Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\np=open('incoming/FFD/FFD_pages.txt',encoding='utf-8',errors='replace').read()\npages=re.split(r'\\[pdf page (\\d+)\\]', p)\nprint(len(pages))\nprint(p[:600])\nEOF"
}
```


### [2026-09-06T22:16:19.000Z] TOOL RESULT

```
231
[pdf page 1]
4و اک ۵ 0
۲ ی
ی
۵ > ره
مرگ
0
/ 0 4 ۰
6( : ز (
مر رک ۳ ص شمل هار /
ور 0
۳ 7 ۹ ۹۱ /
۱
۸ 5 2۱+ و 9 ۱
۵
7
ی
ات
ِ یت
هو و اس
مس لوالا ی
1 ۰
: 4 3 ماس
[pdf page 2]
نچد کي و۱
رح اس
15 ۳/48 8 (7
مکی ( از
۹ ۹ ۸ ۸
۹
!همم
مویکو
7
0
کم
یه
5 ۷ سر
: ۵
موم
7
چا
ن ی
ی 0
۳ ک
فا : 3 6
هم
2 1
3)
اگم له
ی یی بر با
8 9
یی ۲۶ 0۳
۹
4
۹۵-33117025 258۷ ا ِ ا
۳ ا ۰ ۰ قتومان
رش ٍ
۱
[pdf page 3]
أ 1
لو
۹
زد
۸
9
.۱
۶
1
کم
[pdf page 4]
۱ ماده‌های
فعلهای ثارسی دری
۱ دکتر محسن ابوالقاسمی
تهوان, ۱۳۷۳
[pdf page 5]
1
۳۹:۱۵ سرشناسه: ابوالقاسمی» محسن 0۳۱۱
عنوان و پدیدآور: ماده‌های فعل‌های فارسی دری / محسن ابوالقا
```


## [2026-09-06T22:16:25.438Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '22594,22650p' CHEUNG.txt"
}
```


### [2026-09-06T22:16:25.481Z] TOOL RESULT

```
*skar ‘to pursue, drive, look for (the cattle)’ 

*AVESTAN: ? Y Av. skar- ‘to pursue (?)'. 0 The meaning of the Av. compound YAv. 
skärailat.radahe (Yt 13.108), which seems to be a personal name, is unclear. Szeme- 
rényi 1970: 513 translates it as “he who speeds his chariot’. Alternatively, it can also 
be translated as ‘qui fait rouler son char’ (Kellens 1984: 144), which would have no 
further (DIr. correspondences. = Liste: 63 

Partic.: pres. caus. Y Av. skaraiiat- ‘pursuing ?’ (Yt 13.108) 

*MIDDLE PERSIAN: ВМР SkIk /Skarag/ ‘(bird of) prey’ || (+ *ui-) ВМР wskl /wiskar/ 
“hunting-ground, wilderness’ 

*PARTHIAN: ‘Skr- ‘to hunt, chase’ = Ghilain: 58 | DMMPP: 92a 

Pres.: IND. 3sg. * ‘Skryd, 3pl. ‘Skrynd; Partic.: perf. pass. “га 

*SOGDIAN: SSogd. (")skr-, BSogd. ’sk’r-, BSogd. sk’r-, CSogd. Sqr-, MSogd. škr- ‘to 
lead, take; pursue, persecute’ || (+ *apa- or *upa- or *pati-) BSogd. "pskr- ‘to chase’, 
(pass.) MSogd. pskyr- ‘to be chased’, CSogd. psk’r (m.) ‘persecution’ (C2 68V.13) || 
(+ *fra-) BSogd. ’Bskr-, CSogd. fSqr-, MSogd. fSkr- ‘to expel, drive out’ || (+ *ham-) 
BSogd. ’nskr- ‘to collect, gather’ 

Widely attested: Pres.: IND. 1sg. dur. BSogd. "Skr^m ’skwn, 2sg. BSogd. ’skr’y, 3sg. SSogd. ’Sk’rt, etc. || 
(+ *apa- or *upa- or *pati-) Pres.: IND. 3р1. BSogd. ’pskr’nt, ОРТ. 3sg. CSogd. pSqry; Partic.: perf. pass. 
CSogd. psqrtyt (pl.) ‘persecuted’; Pass.: pres. IND. 35р. MSogd. “pskyrtyy || (+ *fra-) Pres.: IND. 3sg. 
BSogd. ’Bskrt, Impf.: IND. 3р1. CSogd. fSqrnt || (+ *ham-) Pret.: intr. IND. 3sg. BSogd. ’nsk’rt, Partic.: 
perf. pass. BSogd. ’nskrtk, BSogd. ’nskrt’y, BSogd. ’nskrt, Inf.: BSogd. рг... ’nskr’y, Pass.: pperf. intr. 
IND. 3sg. BSogd. ’nskrt’y wm’t ‘had been collected’ 

*BACTRIAN: ор(о)кор-, ғркор- ‘to pursue, chase (off)! = S-W, Bact.: 184b 


346 *skard 


*NWIR: NP 3ikar ‘hunt’ (LW ?, < Sogd. ?) || (+ *ui-) NP bisgar(d) ‘hunter, fowler; 
place for hunting; chase; game’ 

*NEIR: Oss. I. sk’zryr/sk’zrd, D. (&)sk’zrun/(&)sk’ard ‘to chase (animals)’, (caus.) 
І. skaryn/skerst, D. skarun/skarst ‘to explore, look around, seek; to grope one’s 
way’, Sh. (Baj.) Xikar-/Xiküd, Rosh. Xikar-/Xiküg, Sariq. Xiker-/Xikawg, Yzgh. 
Xokor-/Xokord ‘to seek, search for’ (< LW ?, cf. EVS: 102a), Ishk. skarr-/skul ‘to 
seek’, Wa. Skar-/Skard- ‘to mate [of animals]’, Wa. Skur(g)-/Skurd ‘to seek’, Yi. 
Skör-/skär-, M. skör-/skar- ‘to send (a thing)’, ? Pash. skärol ‘to incite (against) || (+ 
*upa-) ? Sh. bixsar-/bixcud ‘to ladle, scoop up (grain, fluid)’ || (+ *pati-) (?) Sariq. 
paxéor-/paxcig, paxcug ‘to fill with water, grain (into receptacles from a store)’ 

9 This root is exclusively Ir.; no reliable IE cognates can be cited. 


*PIE— > LIV: – | Pok.: 
*REFERENCES: IIFL II: 251, 413; CDIAL, no. 13645; MacKenzie, Pahlavi: 80, 92; EVS: 21b, 64b, 102a; 
Abaev, Slovar’ III: 117 f., 122; Steblin-Kamenskij 1999: 344 f. 


*skard ‘to pierce (through)’
```


## [2026-09-06T22:16:36.733Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"aiwiskar\\|aiwi.škar\\|aiwiš.kar\\|aiwi-škar\\|škar\\|skar-\" BRT.txt | head -20; echo \"=== hankarayemi ===\"; grep -n \"hankār\\|hankar\\|han.kar\\|hąkar\" BRT.txt | head -20"
}
```


### [2026-09-06T22:16:36.798Z] TOOL RESULT

```
=== hankarayemi ===
25320:•  j,  ^räiti.hankaraS'a-''  Adj.  'dessen  Voll- ziehung durch  Dienstwilligkeit  ( 'raiay-)  oder
29577:•  j,  har-  V.  'Acht  haben  auf  -'.  Praes. 3  hara-,  20  haurva-;  Perf.  i  hankar-.  — Inf.  har>tayat-ca,  Aankmi.
```


## [2026-09-06T22:16:37.444Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -c 500 incoming/ZAW/ZAW_pages.txt; echo; grep -n \"\\[pdf page\" incoming/ZAW/ZAW_pages.txt | head -5; grep -c \"\" incoming/ZAW/ZAW_pages.txt"
}
```


### [2026-09-06T22:16:37.499Z] TOOL RESULT

```
This is a reproduction of a library book that was digitized
by Google as part of an ongoing effort to preserve the
information in books and make it universally accessible.




https://books.google.com
Über dieses Buch

Dies ist ein digitales Exemplar eines Buches, das seit Generationen in den Regalen der Bibliotheken aufbewahrt wurde, bevor es von Google im
Rahmen eines Projekts, mit dem die Bücher dieser Welt online verfügbar gemacht werden sollen, sorgfältig gescannt wurde.
Das Buch hat d
14890
```


## [2026-09-06T22:16:45.248Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pdf page\" incoming/ZAW/ZAW_pages.txt | head -3; echo \"--- form feeds:\"; python3 -c \"\nd=open('incoming/ZAW/ZAW_pages.txt',encoding='utf-8',errors='replace').read()\nprint(d.count(chr(12)))\npages=d.split(chr(12))\nfor i in (40,45,50):\n    print('== leaf',i); print(pages[i][:300])\n\""
}
```


## [2026-09-06T22:16:47.016Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"paiti.kara\\|paitikara\\|paiti\\.kāra\\|patikara\" BRT.txt | head -20; echo \"=== kar- entry ===\"; grep -n \"^.\\{0,10\\}kar-  V\\|kar-  V\\.\" BRT.txt | head"
}
```


### [2026-09-06T22:16:47.246Z] TOOL RESULT

```
--- form feeds:
318
== leaf 40
                         Zum AirWb . 1.   Vorbemerkungen.                 17



 sisches Lautgepräge trägt, einfach für medisch erklärt ; dann
 verliert aber die Bezeichnung medisch' jede Prägnanz. JUSTI
hätte sich doch mit GEIGERS Bemerkungen, GIrPh. 1 b. 413 f.
 auseinandersetzen sollen, die ja ge
== leaf 45
    22
           Ch. Bartholomae, Zum AirWb . 1.   Vorbemerkungen.

    durch aus und zu auseinandergehalten. So steht Sp. 1647 unter
A
    srīrō.tara- Kompar. aus srira-', aber Sp. 1639 unter srayah-
    Kompar. zu srira-'. Ebenso scheide ich genau zwischen ety-
    mologisch gleichen und nur mehr
== leaf 50
                             Zum AirWb . 1.     Exkurs § 1-4.                     27



             'adûr 'Feuer' 16 u. ö.; daneben 'atar 98, 99 ; also ādur
      ) 11(     ‫ آذر‬dar ;
           'arâm 'Ruhe' 50 ; daneben árám 50, 52 ; also ārām, np.
      ‫ آرام‬aram
                         ‫د‬
```


### [2026-09-06T22:16:49.613Z] TOOL RESULT

```
12384:matum  .  .:  interfeci  et  (eos)  qui .  .  erant" Bh.  i.  13;  —  patikaram  didiy  'yaiy  manä ga'äium  ii7rB"(!(j'"simuIacruni3pecta{eorum) qui  . .  portant"  D.  6.  4.  11)  2ur   An-
12782:—  ya/iiy  imSm  dipim  vainlhy  imaivä patikara  naiydi!  (fi^n.)  vikanäky  utämaiy yava  taumä  aAatiy paritarahidii'Sii.4-f^',
12783:—  yadiy  imäm  dipim  imaiva  patikara vaimiAy  vikanahidtl  utamaiy  yävä  taumä  ; akatiy  naiydis  parikaräky  '^.4.\T,  — ■ paiikaram  dldiy  tyaiy  inanä  gä'isum  bari^- tiy    ava'äiä  xinäsähidii^'^  (APm.)   D.  ö.  4;
13260:i)  'sehen,  hinsehen  auf  — ,  beschauen': patikaram  didiy  (2SIA-)'*  tyaty  mani gj'ium  bar^tiy  D.  6.  4;  —  spasö  .  .  are aipi  (sd.)  dai'Aantö  (NP.)''  .  .  ydi  .  .  Yt. ro.  45;  —  lakrpa-  avavatam  sraya  yaia dilayatam  (GP.)"  sao'sö  (sd.)  YL  /;. 1 1,  z)  'im  .\uge  behalten,  beobachten': tarn  dastqm  yä  hatqm  (Sp.  268  o.)  rahistti .  .  irrrimKi/  ux'nlis  ^aoianil  >rM  datdyat {■^YtK^'''^  mahyh  i:7rft'//(sd.)"dieReligion.T werden  sie  sie  mit  den  Worten  und  dem Tun  der  Frommei^ebenheit  richtig  be- obachten .  ."  Y.44.10.  3)  'Jemandes Acht  haben,  sich  kümmern  um— '(Gen.): mit  ?r3s.vaca  sarim  (GP.;  sd.)  didqs(^%^
21108:•  p.  ya'diy,  j.  ye8i'>,  yei8i'>  Konjn. I)  II  zeitlich 'zu  der  Zeit  als' ;  viyaxnakya\  3.-ai\i\\X, mähyn  14  raucabii  'kakaiä  äka'  y  uda- patatä  Bh./.  II.  II)  bedingend  'wenn, sofern';  i)  mit  (fiitur.)  Konj.,  a)  vor  dem Hauptsatz:  II  y  kürj'  pärsj'  patc^  aha- tty ..  siyätis  .  .  nirasstiy  .  ■  D.  5. 3;  — y  av(^a  *maniyähay  .  .  imam  pärsatn käram  pädiy  D.  5. 3;  —  y  imäm  dipim vainaAy  . .  uta  parikarähidil  J'urJ'mazda %uv3m  daufta  blyä^Bh. 4.  16;  17,10,11;! —  *(^(  sL.aSe  vacS  ustime  urvaese  gayehe /ramrai'3i{aS.)  pairt  te  tanava . .  urvamm . . Y.  7/.  ig;  —  im  Nachsatz  steht  «Sa:  °i%i zT  kvari  nUii  uzuxsyeiti  aha  datva  vTsph minnänta  "wenn  (einmal)  die  Sonne  nicht aufgehen  wird,  dann  werden  die  D.  alles zu  nichte  machen"  Yt  6.  3.  a)  ||  mit ^•^«/(^(sd.)  'wenn  etwa':  ^yadipatiy  *'ma- niyähay:  ciyJ'karam  (sd.)  .  .  patikaram dldiy  D.  6.  4.  b)  U  hinter  dem  Haupt- satz: martiy^  ky(^  draujaitJ'  ahatiy  avam *^u/iasata>n    pars3    y     avada    *mam-
=== kar- entry ===
9139:•  j.,  g.,  p.  'kar-  V.  'machen'.  I'raes.  1  i'ar-: i-jTj-,  iu-'>,  loa  i)r.'naT-,  iunai--'^: kjr.iii7',  10a +34  *iufMi'aya-''''l,  27  (Pass.) iirya-i',  kariy.i-,  30  (Iter.)  hiiaya-;  Perf. I     i'axr-,     -2    nixr-.  PPfP.     kjrjta-*\
9180:•  j.  'kar-  V.  'gedenken'.  Praes.  7  ean- kirs-,  30  (Kaus.)  küraya-.        Inf.  'kar^ta.
9201:•  j.  'kar-  V.  'einfurchen'.  Praes.  30  (Iter.)  wandeln':  panca.dasa  /ra/arSii^iiDPiiS..) kSraya'.  ^ptta  puiras'a  raor,aSh'a  kalarasät  Y. p. 5  ;
```


## [2026-09-06T22:17:04.306Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9139,9210p' BRT.txt"
}
```


### [2026-09-06T22:17:04.351Z] TOOL RESULT

```
•  j.,  g.,  p.  'kar-  V.  'machen'.  I'raes.  1  i'ar-: i-jTj-,  iu-'>,  loa  i)r.'naT-,  iunai--'^: kjr.iii7',  10a +34  *iufMi'aya-''''l,  27  (Pass.) iirya-i',  kariy.i-,  30  (Iter.)  hiiaya-;  Perf. I     i'axr-,     -2    nixr-.  PPfP.     kjrjta-*\
karta-<>;  PFP,  iairya-;  Inf.  cartariaiy, kirjtSe.         |S,  noch  "karsta-^
I) 'etwas  (Akk.)  machen"  in  allgemeinster Verwendung ;  'ausfuhren,  /u  Stande  bringen, vollziehen,  schaffen,  zeugen,  bereiten,  tun': •hit  yimii  var}m  hr^naol  V.  L*.  33';  39,  38, /;.  so,  -.  ig  PüZ.;  —  ääl  Om  var^m  i.n-i- fiiwa  (Imp.)*'  V.  L'.  25';  30;  —  ku>a  tl az?m  varjm  k}rmav,~ine  V.  2.  3 1 ;  —  II  /wa* hadis  driraya''-,-a''us  akiinam"'^  X.  ?.  3; 4-  3-  D.  /.  I,  Am.  /  (wo  "akunasf'^;  — "imam  usf.isan,i/»  . .  u/.i  niiim  kaitri""^ Ao.  7.  3;  —  ardastlna" .  .  däray(^'faham .  .  j/^Mvf  kartii^  D-.;- 1;  —  ■"'"*  iy" kartam  av<^  visam  7'<uti:r  a^ara^maz- däha!'  akunavam  D.6'.5;  13;  —  im(^  Iva'' adiim  akuna-.am  7 ■ahm  a'um''iiiazdaßia'' akuna7Hjm  Bh. ./.  6, 12;/.  14, 15,4.  2,  7,> I,  6, 4.  19,  Am.  4  (wo  "aiun.l'");  —  iiiut'' Iva''  mann  kartam  m-idaty  l!h.  L',  I5;_J. 2,4,  12,^.  I, /.  10,  j.  6,  8,  10;  — -  '"utiimaiy aniyauiy    vasiy    astiy    kartam   Bh,  4.  S;
—  Uta  ty<^  manu  kartam  utä  tya"  maiy pi^'ii*  kartam  X.  /.  4;  y.  3;  —  fy.i'' manu  kartam  id-i  utä  tya^maiy  kartam apataram  ava''  Hsam  7'ahiä  a''ura''mas- d,thJ'  akimavam  X.2.3;  3,^.3;  —  avaisäm iiaiy  astiy  kartam  ya>ä  manä  .,  kartam Bh. .,'.  9;  —  Uta  tye^  "mäm  kart,l'"" Ao,  /.  4;  —  Aai(7' .  .  vasiv  tya^  naibam akimau;'"  X.  7.  3;  —  'tyJ'  kunavaky ava''taiy  a"urtrmazd,i  mkwtm'  (sd.)  Rh. 4.  17;  16;  —  a''uri^mazd<lmaiy  upastäm abitra    yätä  kartam  akunavam  D.  6.  5;
—  imam  duTariim  ,  .  adam  akunai-am, \vasiy  aniytiiay   naibam  kartam..  tya''
adam  akunavam  iitamaiy  tya""  piiä I  akiiriaui'^^,  tya'paliy  kartam  7'ainatair \mubam  (sd.)  ara"  visam  vasna  af'ura''- mazdä/ia''  akumilX.i.y, — lyi^'iam  hacüma'' a'^ahya"  ava  akunai'o"  D.  6".  3;  Bh.  ;.  7 (wo  *akunai'ara"t,iy\  D.6.4  (wo  akuna- Td'tä)  II  ;  —  yat  b.i  paiti  frac'tjm daxnia    uzdaeza   (sd.)    kiryänte^^    V._j.  9;
dby  Google
445
'kar-  I  a
'kar-  S  a
446
—  vupim  ä  ahiHilt  '^rä^r^m  k}r?navat yal  .  .  V.  jj.  15;  —  yai  tum  atnim arain^is  sao:a\a/a  kinnav  antem^>\ H.  2.  13;  13,  Vyt.  _J9  (wo  hrmvö'*;\ aSPrA.?;;  — .iaÄ-y  k?r.maoiti  yat  avSstrim  1 V.  j;.  51;  —  I  ..  ^■akata  aiii^  avairä\ hantaranain  akuma  Uli.  X.  18,  ig',  i'.  iz;l 1  z ;  —  avadä  hamaranam  aktmaus  hadä  ' hamtk''iyaibii  Bh._j.i;  3,  2.6,  14,  5.1;  — -j avadii  hamaranam  akunava"  Bh.j.6,7,9,1 10,  2.  7  — 11,16;  —  avaiäsäm  hamaranam  , kar  tarn  Bh.  2.  6-1 1,  i6,_y.  1,3, 6, 7, 9, 10;  l
—  adain  it)  /lamaranS  aku/ia7-am'iih.4.6  ;  j
—  afrin>in  ifmiavät  Az,  2;  Vyt.  J  (wo k^rjnofilAi);  —  va!s  paoirlm  miirsm k^rmaoiti  V.J.3;  —  iian  (sd.)  hä  iiisläta iiryatii>  Yt.  10.  109;  —  ^fö  0ng  /rS.ga pa^mSng  hucistöis  (sd.)  *carat  (Konj.)9> ; \.4li.a,\  —  k(ii:a..  zarjm  (sd.)  (ar,l»r'>' kaca  xsmal  Y.  44. 1 7.  a)  mit  Adv,  statt Akk.:  II  ya^äsäm  hacärnJ"  d^ahyJ'  ara^^J *aJh/riavaya"li '^  Bh.  j.  S;  —  <iai  yimd ara'ia  k^rjfiaat ya'>a..'V.-J.$2.  h)  mit Inf.  als  Obj.:  yaf  kirsnaot..  c^airyqn  (sd.) 3far?i>m  ajyamnum  Y.'y.4; 75,16  {k}rma-\ rJni).  S- S.  2a)  mit  sksfuiem  'etwas' (Akk.)  zerbrechen,  zerstören';  shnd?m  (sd.) sl  mauö  k^nnüi'A  Y.  i/.  28.  b)  ;  mit züre^  'Jemandem  (Akk.)  Unrecht  tun': naiy  "sakurim  .  .  zür,^  (sd.)  akunavam Bh,4. 13.  c)  mit  ntazdam  Med.  'sich etwas  (Akk.)  ins  Gedächtnis  rufen,  recor- dari':  inasdqmcä  büirüä  (s.  bei  5)  ktrshul ,  .  xrapaitl  (sd.)  hyat  ahmat  aibi  Y. 40.  1 .  3a)  'Jemanden,  etwas  (Akk)  iiin- schaffea  zu  -,  verbringen,  versetzen  in  -'; a)  mit  Lok.  des  Ziels:  II  pasäva^dis a''ura^mazd<l  maiiä  dastayi  (sd.)  akunaus Bh,  4. 4,  1-)  mit  Lok.  eines  Nom.  act. zur  Umschreibung  des  Verbs:  vispqm  .  . taiiüm  ayao^dsta  (sd.)  k)rJiiaoiti  V.<V,4o;
—  yai  nurm  yas'/ö  kprj/iam/ii  Yt  /j. 56  (?)""  ^)  I  mit  pa/iy  und  Lok.:  afa- dasis  usmayiipatiy  (sd.)  akuiui7<am  Bh. 3-  8;  2.  13,  14;  —  uzmayäpatiy  (sd.) *akariy,^tii"^  Bh._J.141.  7)  mit  äi  und Akk.:  yat  .  .  an.lpm  (sd,)  äi  sp3m\ kpr^naoiti  V.  j.  4;  4,  b)  'Jemanden, (AkL)  wegschaffen,  wegbringen,  losbringen  | von  — ',  mit  kaca  und  Abi.:  ku^a  hiS\ az?m  kfr?naväni  hala  avatihät  drujal V. /p.  la.  4)  'Jemandem  (Dat,  Gea, Lolc)  etwas  machen,  schaffen,  verschaffen
(usw.)':    daitim    ahmHicit  harJkir»m    kjr?-
nuy.it  V.  /4. 1 7 ;  —  y3  tiS  usSn  (sd.)  (ör?t  "'> spsncä  aspSii^ä  Y.  45.  9;  —  ya'ia  spä vahrkaht  (sd.)  k:>nnaoiti  V.  13.  41;  —  yas) tai'ü  mazdh  k>rJiiaot  ta:ar?  (sd.)  Yt^.go;
—  raoxiium  kirjiiaxTihi  dämakva  V.  2/.  5 ;
—  yat  {mafiatum')  kjnniiun^^^  amtSa. spiiita  (ahc)yti ..  YLiO.  51;  —  hqmJaptibyS aiwyö  cäxrare'*'  (3PPfM.)  nfnbyö  "mit heissem  Wasser  stellen  sie  es  (das  Ordal) an  den  Männern  an"  V..;.  46.  5)  'Je- manden, etwas  (Akk.)  machen  zu  -' (Akk.):  II  hy^  durayaf'Ti^um  xsäya^iyam akunau/  D.  6.  i;  4,X. /.  i,  6".  i,Ao. ;.  i;  — uiHsäm  I  martiyam  maHislam  akunau^''\iaA er  machte  einen  Mann  zu  ihrem  Obersten" Bh.  j.  9;  2.  6, 14,  J.  6, 14, 5.  i;  —  aniyam (sd.)    ''uslrabärim    akunavam    Bh.j.iSi;
—  ks  UKtmSm  (sd.)  cBrM"^  . ,  pu'^nm pure  Y.  44. 7 ;  —  kjrmaomi  "iwam  hacat.- pu^rqm  V.2^.6;  — yat  k^rmaot..  *amar- /an/a  fasu  vira  V.p.  4;  Yt5.  30,  /j.  16 [k^rmavani);  —  matdqmcä  (s,  i  c)  büiricä kjrpsvä  .  .  xrapaitl  (sd.)  Ayat  ahmat  aibi Y.  4n.  I ;  —  yi  umm  pinmm  k?rpnaoiti  . . bantjm.'a  drum  k^rmaoUi  V.  22.5;  uj.^%, Y.  10,13;  —  \hatm  parsam  hami'i''iyam akunaus  Bh.  4.2;  2%  3;  —  ya'ia  asym amasyq  (sd.)  kmnaväni  .  .  karh'qn  Yt. 5.30;  —  ts  k>rmava  mdwaire  ajyamnem V.2.z8;  36  {kirnittol);  — yat  amm  patti.- irist»m  /rä.nastirii  kjnnaaiti  V.  r/,  42;  — armadsth  atiyh  äps  k^nnaoi  Yt.5,78;— >J( Im  firasJmisA.)  *k3rjnaon'^^  ahsm  Y.30.9; Yt.iil.ii  (k^rMavqn),  89  {k»rma7,;li) ;  — yezi  iidit . .  mazdayasna  . .  kahrpsm  kvars.- dar^slm  (sd.)  k:>rmavqn  V.5,14;  13  (wo k^r»nai)t,  statt  Plur,);  —  raeko  (sd.)  mS haca  aühij  s»mat  vatihö  k^rjnaoiii  Yt. iy.2o;  10.2S;  —  ya  *a/r3.ur7'isval  (sd.) hrmavainti  irmi  Yt  13.  z6;  —  I  av<^taiy (^urJ'mazdä  ^mazänam  (sd.)  kunautiro Bh.  4.'6;   —  ava'^  adam  patipadam{%iL)
Bh./.i4,;  —  "pouru.narftn  tum .  {aet^m)  yas3  tl  .  .  Y, /o.  13; srJra  k?r)ta  (NSf,)  V.  if). a)  Medium  in  reflex.  Sinn: '^istam  rtX-««(ji'rt''Ai  "den machten zu  ihrem  Obersten"  Bh.j.3;  ^5.1;  —
I  fiwrj;« (sd.)  k^rJuaväneYl.  j>).4$;  43;
II  utä  pitrsam  .  ,  util  aniyl  dakyäv^ I  hauv  ^äyasatä  " uväipasiyam  (sd,)  akufä l(3SPrM.)    Bh.y.ii.  a)   mit  Adv,    statt
akunava  II kjrmfisi   ,
30  m'«.
ob,Google
447
'kar-  S  Anhang
»kar-
448
Akk.;  I^yaäa  paruvamciy  avaiia  adam\ (flftf*)  akunavam  Bh. /.  14;  —  kui:a  Ais' az3m  hrmaväni  sva,  "was  soll  ich  mit  | ihnen  machen?"  YL77. 57;  —  \ava%iidis\ akunavam  Bh.  5.  a ;  4. 4.  II  Anhang  zu  S. Mit  Akk.  der  Person  oder  Sache  und  Akk. des  PFfP.  'machen  (usw.),  dass  Jemand, etwas  . .  wird' ;  naiy  äha''  . .  kasciy  hya'' .  .  gauniätam  .  .  xsa'i''am  dllam  caxriyä" "es  war  keiner,  der  es  fertig  gebracht hätte,  dass  G.  der  Herrschaft  beraubt wurde"  Bh.  /.  13;  —  yanaiy  (sd.)  dipim naiy  ttiptstäm  akunaus  X.  7. 3.  6)  mit
(blossem)  Opt,  'machen,  bewirken,  dass . .': yö  kirsnavat  yim  yazaite  mi^nm , .  xsttBlä albHtS  hyät  "der  bewirkt,  dass  M.,  den er  verehrt,  zufrieden,  ungekränkt  ist"  Vt. lo.iao.  Unklar:    ksr^take  Vyt.47;  —
kirinaoiti  Vd.  ig,  kfrmaväni  Vd.  <^,  k^ri- nuyäi  Vd.  14-
mit  antarS  'durch  Vermittlung  etwas (Akk.)  Jemandem  (Dat)  erwirken,  ver- schaffen': veAa  xsa^rf/zi  vatrim  biigjm aibl-bairistitn  *vTdlhmnai  (sd.)  .  .  Oiä anlar).caraiil  {i^Y^k.yT'  Y.5/.1.
mit  ä,  mit  dopp.  Akk.  dnwS.  5:  tum stmargüzd  *ilipr^ni-J  (iSPtA.)  vispe  daeua Y.f).T^.         [Bh.2. 14  lies:  aiariya"/,!.]"*
mit  paiii  —  ?— :  mosit  tat paiii  ak»r)naoi (Augm.)  V.  ■•.  5  PüZ.'9l
mit  /rS  'perficere':  frakaire  (sd.)  fra- kyr^naoi\.ig.4i  Gl.  a)  Med.  in  reflex. Sinn;  *astjm  (sd.)  i^ra  Jra^armta^"^  pas- vasca  .  .  V.  2.  II.  Wertlos:  frak}r.ma-
vintam  Vd.  g ;  —  frak/nnöit  Vd.  75.
mit  kam  'für  Jemanden  (Dat.,  Gen.)  es (näml  den  Yasna)  vollziehen':  niva&a- yemi{sd.)  Aankärayemt"^ ..  ahurake  mazdä ..  vauhaTe  mananke  Y. /.  if.)  äff.,  Vr. j.ifT.,  F.  34.
ai.  äkar,  äifla,  karati.  fytvä;  kj-ip'li,  kfifuhi; kriyäle,  kätayäli  (Kaas.)j  cäkrh,  ii-läh;  np. iunad.iaidaH,  PDw-  xölk  'gemacht'.  -  Pü.: iar/an;  s.  noch  No.  9,  12,  16,  17,  20.  21.  — ')  Zum  ap.  u  (für  ar.  r<  S  ^<^^)  s-  noch  Hbu. PSt.  147,  tot  KZ.  J5.  35.  i/.  541.  BtlM.  Grdr. /».  454,460,  HoRN  GIrPh, /b.  ji,  FrMOller WZKM.  //.  »57,  KoRTUNATOV  KZ.  36.  14 (d«r  fälschlich  ap.  kiin'  ansetit  und  dies vom  np.  i'iM'getrenm  wissen\sill>  —  J)S/J5■ KZ.  jj.4;  NA.  hat  akiinrny'.—  3)  Tjf'.6.— *)  Ui^ide  gleich  ai.  kf/ä-,  während  das  mp. tarl,  n^.  tarda  auf  Ausgleich  mit  dem  Infinitiv beruht;  s.  Bthl,  IF.  4.  128  No.  (,  wis  der Schreiber  von  WZKM.  //.  257  olTenbar  ebenso- wenig gelesen  hat  als  S  ^90,   worauf  GliPh,
/.  206  zu  aiulä  verwiesen  ist)").  —  i)  Tbem. —  6)  Zuletit  iF.  Fov  KZ.  ^7.  540,  —  7)  Ortho- grapbiscb  verunglückte  Wörter.  Anders  FüV KZ  35.  56  f.  Ich  halte  das  troti  IF.  /^.  I73 für  unrichtig.  Man  wollte  noch  nach  den Vorbildern  schreiben,  ä\K DariM  J.anAXtrxn I. gegeben  hatten,  aber  die  Sprache  hatte  lich BeieilE  verändert.  —  B)  Aus  dem  Vollstamm, gegenüber  ai.  kj-rivänl:  —  9)  Pü.;  kunisn; karlärih.  —  i")  Man  verlangte  die  1.  Sing. iiriHOvähi.  —  ")  NA.  äiariytftäm ,  Imp. Dagegen  spricht  1)  dass  sonst  in  dieser  Wen- dung das  Simplex  gebraucht  vurde,  2j  dss^ bei  Rl.  die  leine  Zeile  der  Inschrift  deutlich mit  a  abscbliesst.  —  ")  S  ?9*.  3  b.  Vgl.  da^u fbar-  No.  9.  Pü.:  kart.  ~  'J)  S  JÖ?.  — '■>  S  'i'  f-  -  -5»  Pi  4.  J  i.  K  5-  NA.  -»äu«, s.  No.  13,  —  -6)  Pö.:  an  i  nnoak  pa  dilan hukart.  —  '7)  Pii,;  andari  iunend,  Sü.;  aitla- räle  katomi.  —  '*)  S.  No.  11.  —  •9)  Kann auch  zu  iarfl'  gehören.  HORN  GlTPh./b.6l stellt  es  lu  mp.  faliär  'KampP.  —  •")  Nach Fü. : /rä/ ra/l  if tid  ta  ikar-;  vg).  la 'at/a-. — ")  Pü. !  hangartenem  (vgl.  np.  angärdan),  erl.; yaniht  sar  kuti/ni;  Sü.;  latnfürnayämi ,  erl.: ijifni  lamfärnatH  iammi ;  Tgl.  'tiaed-  So.  18. S.  daiu  DST.  ZA.  i.  5.  Anders  HbM,  AGr. /.  gS.  —  "»  Das  np,  -ghd  am  Ende  von  Orts- namen, mp.  •kort,  im  arm.  LW.  'kfti  (I.itl. GIrPh.  rh,  190)  bedeutet  schwerlich 'gemacht'. Ich  sehe  darin  ein  Nom.  von  der  Bedeutung 'Aufenthalt,  Heim',  das  lu  ^iar-,  gr.  irr}.tiiai,
•  j.  'kar-  V.  'gedenken'.  Praes.  7  ean- kirs-,  30  (Kaus.)  küraya-.        Inf.  'kar^ta.
i)  'Jemands  (Gen.)  rühmend  gedenken, ihn  rühmen':  fsümn  (sd.)  asti  asava  .  . ßüsi  carik^rjmakl  V.  $S.  4.  2)  Kaus.
'dem  Gedächtnis  einprägen"';  vahists ahurö  uiazd-l  ahun^m  rairtm  Jrilmraoi vahistö  häind  karayat  "der  beste  AhM. hat  den  AhunaVairya  kund  getan,  der selbe  beste  hat  ihn  dem  (unserm  ?j  Gedächt- nis eingeprägt"  \.ig.\t,; — a'ia  tkalhm kärayäti  "in  dieser  Weise  prägt  er  (uns) ein    Dogma    ein"   Y.  :;o.  1.  a)    in    der
exegetischen  Litteratiir  'das  Augenmerk lenken,  hinweisen  auf-' (.\kk.):  manai^hö iiltavailya  im  israyeiii  ivao'^.man/im  ioa a/iüm  kürayeiti  "'manauAä':  damit  weist er  auf  ihn  hin;  syu«^. man/im  weist  auf  den (ihn  als)  A/iä  hin"  V. //j.  13.
mit  *aipi  'eingedenk  sein',  mit  Gen.: s.  Inf.
ai.  ^a,kr/,i/.  —  Vgl.  /atjkj,f:i,a..  —  PÜ.  (lU I,  füryj"  raiJi'):  fiüi  kartät  i  nri.-akii,  (tu 2|;  A.TiH'OrtlkrA  (Sü.:  iamkiip'aH)  iülaii,  erl.: sar  (ap,')  Imlan.  —  ")  Vgl.  iBed.  Bn.  Stud.  /. 306.  Anders  H*l'0  SBayrAW.  /*/?.  13I, DsT.  ZA.  I.  173  ('resumer';
dby  Google
449
^kar-
ikar-  Noten
45°
•  j,  ^kar- V. 'ausschütten',  Praes.3o(Iter.)i  besuchen',  mit  Akk.:  yasi  tarn  daÄyHm käraya-.  ^3caraiH  Yt. /O.  iia;  —  viips  vairiS  (,hS.)
i)  '(S^™c°)  ausschiitien,  ausstreuen  auf  acaraiti  Yt.^.46;  8.  2}  'wohin  (Akk.)
—  hin' (Akk.):  mäia  ..  tarn  sam  ^rJ/-iyj« ;  kommen  zu  Jemandem'  (Dat):  räst>m rnä  ilpü  k>r»iay?n  yat  ahmi  . .  "nicht  sollen  1  ahmäi  naire  .  .  mi%rS  mal'ianim  (sd.) sie    auf   das    Land    Samen    werfen    noch  ^JÄira/ft"  Yt.  iO.  137.
Wasser  darüber  hssen,  wo  .  ."  V.o.  2;:  mit /arfl  'vorbei-,  vorübergehen':  vis- 2,  3.  3)  'durch  Aussäen  anbauen':  yat\panqm para.car?ntqm  illars  sasta  ääioaya
bä  paiti  fraSst?m  kürayäli  .  .  yavanamca   (sd.)  Y.  62,8.
vOstrajiqm'a  urvaranamca  ifars>S.bair-\  1  mit /a^iy 'pflegen,  Sorge  tragen  für —' yanqm  V.j,4;  —  yj  yaom  kärayeili  ÄJ'(Akk.):  imäm  dipim  ..  imaivä  patiiarä alim  k.lrayeiti  "wer  Getreide  durch  Aus- '  mätyj"  vikanühy  ylvä  (sd.)  *taum!l  ahatiy säen  anbaut,  der  baut  das  Asa  an"  '^.*svä  avaiy  parikarä  ". .  solang  pflege J.31.  isie"   Bh..^  15;    —  yadiy  .  .   utämaiy  .  .
ai.   vgl.   kiräti;    np.  iii-orf   'er   sät,    pRa.mi\' parikamAUis    "wenn   du  ..   und    sie   mir
"T.f"'^'"  '"''p?'''i";  '"^'--VeI-  ■J'""^'^-   pflegst"  Bh.4.16;   17.
und  'iars-.  —  Pu.;  iislan.  1  '      °.     ,       ,  ;  ,    /  ..      ,     ■   i_     i
I     mit  /rJ  'sich  (vorwärts)  einn  erbe  wegen,
•  j.  'kar-  V.  'einfurchen'.  Praes.  30  (Iter.)  wandeln':  panca.dasa  /ra/arSii^iiDPiiS..) kSraya'.  ^ptta  puiras'a  raor,aSh'a  kalarasät  Y. p. 5  ;
'einfurchen,  (Furchenstriche,  -streifen) '.  —  yaia  gaz'ishva  (sd.)  vasS.xsahrS ziehen":  karsaim  (sd.)  kirayeiti  Yt.4.4.     ,/racarane  Y.g.iT,  —  aat  hva  pasu  vTra
mit  pairi  'ringsum  einfurchen' :  xsa^räi  ■  vasü.xiair5  fracaraite  (3DPM.)  "und  seine vairyii  pairi.ianm  pairi-kSrayiis  "mit ;  (des  Landes)  Tiere  und  Menschen  be- einem  Metallstiick  sollst  du  einen  ringsum  wegen  sich  frei  einher"  Yt  io.  112-,  — gehenden  Furchstreifen  ziehen"  V. /j.  6.     \yeAhe    nmJne    asis    vaiiuhi  . .  fracaraäa
mit /rJ  'durch  Einfurchen  herstellen':  (sSPrM.)  Vt.ij.  107;  —  aü?..  fr  acaraiti karsasiit  (sd.)  frakirayjis  tiyra  xi'a'ira  \*antan.ar/6}m  nm3nahe  Yt.  iS.  4;  3;  — *vairya  V.^,  10;  11',  F. 5;  —  nava  karsa.vasS.xsa^rS  (näml.  jran//')  *fracaraite  aoi frakJrayat  "neun  Furchstreifen  zog  er"  ^y^m  ..  gas%qm  ¥.57.34;  —ya'i:a..anJzarvtä \.22.ao; — yS  ZJinS  tisrS  kari^a/rak3ra-\.  .  yahm  (näml.  fravasayS)  fra^ara'imie yHH  N.;o/;  YL4.63.  (2PPM-)  ¥1/^.34.         2)  mit  Akk.  'hinzu
afj.  kÄral  'ackern,  pflüfen',    PDs.   . baue  das  Feld';  vgl,  GlrPh.  /,b.  299,  - carjna-  und  ikari-.   —  Pii. :  kutan.
•  j'i  g->  P-  *kar-  'sich  einherbewegen'. Praes.  3  cara-,  iara-'\  24  caraya-  [,  »5 cara^a\  —  Inf.  *(aire.
i)  'sich  einherbewegen,  versari':  nsil ml  apqm  J^rai'a  . ,  daifihava  carät  "nicht soll  sich  fernerhin  ein  A.  . .  m  meinem Lande    aufhalten"   Y,  ().  24.  2)    mit
Adj,  'dauernd  einer  (durch  das  Adj.  be- zeichneten) Tätigkeit  obliegen' :  ySi  djitya.-
gehen  zu— ':  äat  *aile  yji  fra'arpnti  kjtv- sqs^a  gaaSitii^a(s^)  N.  55,  [/ra.^arf/i/a V.  2. 1 1 :  s.   'iar-.]
mit  vT  i)  'sich  hin  und  her  bewegen,  auf und  ab  gehen':  *anaiwi^nlvS.gälu  (sd.) aSa  äb>r3ta  *'sraosävar3za  vüarayatim N,  79.  2)    'sich    ergehen':   fravasayJ
```


## [2026-09-06T22:17:32.455Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\npages=open('incoming/ZAW/ZAW_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor pr in (38,242):\n    for d in (0,):\n        i=pr+23+d\n        print('===== printed',pr,'leaf',i)\n        print(pages[i][:3000])\nEOF"
}
```


### [2026-09-06T22:17:34.094Z] TOOL RESULT

```
===== printed 38 leaf 61
38                             Ch . Bartholomae,

 lebendig' 35, 48, 65, bavandag 'vollkommen', savgand 'Eid'
81, 312, pand 'Rat' 24, 52, 'abgand 'hingeworfen 81 ; 39, 77,
'andar innerhalb 16 u. ö., u. a. m., endlich die 3. Plur. parî-
stand 86, padîrand 86, ' êstand 1079, 'istâyand 69 ; s . S. 37
No. 3, unter 3.
       § 16. 2) vor rd :
                      C



      kêrd, qêrd gemacht 12 u. ö.¹), kêrdan machen' 85, 91,
kêrdag, qêrdag 'Tat' 862 u. ö., frašêgêrdîy, gêrdîg 49 ff.2) ; man
vergleiche zur Wurzelsilbe des bp. 11515 kartan, Paz. ‫وو‬         ‫وس‬
kardan, np. ‫ کردن‬kardan BARTHOLOMAE IF. 8. 253, SALEMANN
GIrPh. 1. 274 und zu deren Aussprache das entlehnte arm.
կերտ kert gemacht am Ende von Zusammensetzungen ; s.
HÜBSCHMANN AGr. 1. 168 ;
       yazdêgêrd ' Götterstadt' 75, SM.; vgl. dazu voNSTACKELBERG
Oss . Erzähl. 82, MUNCKASI Revue orient. 1904. 318, BARTHOLOMAE
AirWb . 448 ;
     hašâgêrd (MÜLLER gîrd) 'discipulus' 30, 32; vgl. zur Aus-
sprache die Pazandwiedergabe von bp. 119          oder ‫س دام‬
durch_
     ‫دسمو‬            sowie das entlehnte arm. muhtpır ašakert ; aber
im Np. wird ‫ شاگرد‬sagird gesprochen. In der Annahme, daß
dash der mpT. Wortformen etymologisch berechtigt ist, nicht
sekundär, setze ich uriran. * hašākarta- an, d. i. eigentlich der
mit der Wartung, dem Dienst des Priesterkollegen oder Priester-
kollegiums zu tun hat', eine Zusammensetzung aus *haxai- (jAw.
                                                                    von
unter einmal nach y, s. § 65, zweimal am Zeilenende, s. oben S. 26
den Handschriften im Dialekt sehe ich dabei allerdings ab -, sodann daß
neben -ênd auch -êênd vorkommt, s . nâzêênd neben nâzênd 69, hamnihêênd 19
    beide freilich am Zeilenende , s. oben S. 26 mit Note -, endlich daß in der
3. Sing. neben zahlreichen Formen auf -êd der Ausgang -ad nur in qûnad
11 , 12, kunad 100      hier am Zeilenende, s . S. 26 ; darum ist auch der Vokal
der ersten Silbe nicht geschrieben —, 'abrasad (?) 1081 , sowie in patâyad 33,
nimâyad 93, 1078    in beiden Fällen hinter y ; s. dazu § 65             belegt ist,
ē und nicht e zugewiesen werden muß .
            4. zîndag lebendig' 47, 55 u. ö., das aus zīvand (s . zîvandag 35 u. ö.)
zusammengezogen ist.
       1) kard oder qard ist überhaupt nicht bezeugt, daher MÜLLERS Er-
gänzung 21 Z. 5 nicht ganz richtig.          Statt padašqîrd 16 ist padišqêrd zu
schreiben, s . MÜLLER 110.
       2) Bd. S. 46 Z. 4 der WESTERGAARD SChen Ausgabe steht ‫لاسود ودامه‬
fraškirt.

===== printed 242 leaf 265
242                         Ch . Bartholomae,

      ‫ دود‬hakirč oder die hakure sind mir nicht deutlich. Man
   verlangte hkyrj statt ḥkryj ; allein die Zeichen sind
   ganz deutlich auf dem Faksimile zu erkennen.

     Sp. 1744, Z. 33 und 43 ff. füge in den Noten zu jaw.
haxay- Freund' und zu ap. haxāmaniš- EN. hinzu : Vgl. mpT.
hašâgêrd, np. šāgird 'Schüler'.
         S. oben S. 38 f., 158 f. und 226. Man beachte das auch
      zu Sp. 238 m.

        Sp. 1754, Z. 41 f. füge in den Noten zum airan. Verbum
had- 'sitzen' hinzu : mpT. nišîyând 'sie werden sich setzen' M. 21 .
      Das Wort zeigt die selbe Präsensbildung wie das jAw.
   nišhidaiti oder auch wie das ai. níşīdati, indem es ar. * ni
      šīdānti fortsetzt ; s . a. O. No. 3.

        Sp. 1756, Z. 15 füge in den Noten zu ap. hadā zusammen
mit' hinzu : mpT. 'ad.
         Das mpT . Wort findet sich bei MÜLLER 16, 23, 352, 42,
   54, 66, 68, 83, 1082 an zum Teil undeutlichen Stellen. Not-
   wendig ist die Zusammenstellung mit dem ap. hadā nicht.
   Vielmehr spricht d eher für iran. t, und diesem Ansatz steht
      auch oss. äd nicht entgegen. Dann ließen sich mpT. 'ad,
   oss. äd mit griech. μετά verbinden; vgl. μέχρι und ἄχρι bei
   FICK BB. 5. 168, BRUGMANN GrGr.3 548.1)
        Sp. 1759, Z. 40 f. füge in den Noten zu jaw. hadō.zāta-
'leiblich' hinzu : arm. LW . harazat leiblicher Bruder'.

     Sp. 1765, Z. 13 ff. füge in Note 1 zum ap. Präsensstamm
hapariya- hinzu : Vgl. ferner JusTI IFAnz. 17. 106 mit meinen
Bemerkungen dazu, oben S. 104.
      Sp. 1771, Z. 21 ff. füge in den Noten zum gaw. Verbum
1hant- hinzu : Zu den gAw. Wörtern nišąsyā Y. 50. 2 und
hīšasat Y. 32. 15 S. SCHEFTELOWITZ ZDMG . 59. 693, 711 .
         Meine Übersetzung von Y. 32. 15 a ist nach ScH. sinnlos' .
   S. noch a. O. 714 Note .

       1) JSCHMIDTS Einwand dagegen, auf den PRELLWITZ WbGrSpr.2 292
verweist, Sonantentheorie 152, gilt mir nicht für stichhaltig .
```


## [2026-09-06T22:17:55.002Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in BQT_v1_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt; do echo \"### $f\"; grep -o \"\\[pdf page [0-9]*\\]\" $f | head -3; grep -o \"\\[pdf page [0-9]*\\]\" $f | tail -3; done"
}
```


## [2026-09-06T22:17:55.469Z] TOOL CALL #46: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py"
}
```


### [2026-09-06T22:17:57.141Z] TOOL RESULT

```
### BQT_v1_pages.txt
### incoming/BQT/BQT_v3_pages.txt
[pdf page 1]
[pdf page 2]
[pdf page 3]
[pdf page 719]
[pdf page 720]
[pdf page 721]
### incoming/BQT/BQT_v4_pages.txt
[pdf page 1]
[pdf page 2]
[pdf page 3]
[pdf page 551]
[pdf page 552]
[pdf page 553]
```


### [2026-09-06T22:17:57.176Z] TOOL RESULT

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


## [2026-09-06T22:18:07.197Z] TOOL CALL #47: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\""
}
```


### [2026-09-06T22:18:09.130Z] TOOL RESULT

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


## [2026-09-06T22:18:23.367Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nimport re\ndef getpage(f, pdfp):\n    d=open(f,encoding='utf-8',errors='replace').read()\n    parts=re.split(r'\\[pdf page (\\d+)\\]', d)\n    m={}\n    for i in range(1,len(parts),2):\n        m[int(parts[i])]=parts[i+1]\n    return m\nv3=getpage('BQT_v3_pages_faseng.txt',0)\nv4=getpage('BQT_v4_pages_faseng.txt',0)\nimport json\npm=json.load(open('BQT_v3_pagemap.json'))['map']\nfor pr in (1549,1617,1779,1787):\n    p=pm.get(str(pr))\n    print('#### BQT printed',pr,'pdf',p)\n    t=v3.get(p if isinstance(p,int) else int(p or 0),'MISSING')\n    print(t[:1400])\nEOF"
}
```


### [2026-09-06T22:18:25.428Z] TOOL RESULT

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 9, in <module>
  File "<stdin>", line 3, in getpage
FileNotFoundError: [Errno 2] No such file or directory: 'BQT_v3_pages_faseng.txt'
```


## [2026-09-06T22:18:28.454Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && ls; python3 -c \"\nimport json;pm=json.load(open('BQT_v3_pagemap.json'));print(type(pm), list(pm)[:5] if isinstance(pm,dict) else '')\nm=pm.get('map',pm)\nfor k in ['1549','1617','1779','1787']: print(k, m.get(k))\n\""
}
```


### [2026-09-06T22:18:30.161Z] TOOL RESULT

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
<class 'dict'> ['pdf', 'pdf_pages', 'offset_mode', 'anchors', 'map']
1549 342
1617 410
1779 576
1787 584
```


## [2026-09-06T22:18:34.253Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nimport re,json\ndef getpages(f):\n    d=open(f,encoding='utf-8',errors='replace').read()\n    parts=re.split(r'\\[pdf page (\\d+)\\]', d)\n    m={}\n    for i in range(1,len(parts),2):\n        m[int(parts[i])]=parts[i+1]\n    return m\nv3=getpages('BQT_v3_pages.txt')\nm=json.load(open('BQT_v3_pagemap.json'))['map']\nfor pr in (1549,1617,1779,1787):\n    p=m[str(pr)]\n    print('#### BQT printed',pr,'-> pdf',p)\n    print((v3.get(p,'MISSING'))[:1600])\n    print()\nEOF"
}
```


### [2026-09-06T22:18:35.935Z] TOOL RESULT

```
#### BQT printed 1549 -> pdf 342

—N\eta—

‎ogee gs‏ ۰ با اول بثانی رسیده
و میم پالف کشیده وکسر رای فرشت ونای‌مثلثه
‎oly‏ رسیده و پنون زده ؛ بلفت ‎gy‏ رازبانة
صحرایی را گویندکه بادبان دشتی است.

‏قوم فیل ه اارهباصعاب‌الفیلاست؟ .

‏قومنی ۴ ۰ با اول بثانی رسیده و کر
میم و نون بتحتانی کشیده » شرابی است که آنرا
از آرد جو وآرد ارزن و غیره سازند وآنرابوزه
کویند. خوردنش مستی آورد .

‏و فا - با تون بر وزن ‎Lag‏ بلفت

‎aig

‎. ‏را گویند‎ 256 by

‏لن = با بای حطی ولون وح رکت‌غیر
معلوم, مرضی است کهآنرا بفارسی کهنکووبعربی
عرقالنسا خوانشد .

‏قوینطن ۴ = با اول پثانی رسیدموفتح
تحتانی و سکون نون وطای حطی مفتوح ‎Ose‏
‏زده ؛ بلفت رومی گیاهی است که آنرا بعربی
خانقالنمر کوبند و ‎OT‏ نوعی از ماذربون است.
چون‌پلنکه وبوز بخورندخناق بهمرسانندوبمیرند
و بدین سیب قاتل‌اللمر خوانند .

‏بیان هیچدهم

‏درقاف با ها مشتمل‌برسه لفت

‏قهرمان * = با میم بر وزن پهلوان .
کارفرما را گویند .
قهستان - مرب کیتان ‎٩‏ است.وآن

‎ay,‏ است در خراسان ۷ و بتعربب اشتهار

‏دارد .
‎Wd‏ » بنتح اول و سکون ثالی و قاف
مفتوح وها . خندة بآواز بلند ‎Aas SL‏ - ونام

‎. ٩ ‏است در ولابت طوی‎ ole

‎٩‏ - بونانی ‎fennel = Marathon‏ ( انگه ) « فرهنگه بونانی انگلسی‌وودهوس».

‏۴ - رك: تفاسیرق رآن‌زیل . سورة ۱۰۵ (الفیل) و تواریخ عرب جاهلیت .

‏۴ - دزی گوید ( ‎(LTA HYG‏ « قومی ‎KOME guy)‏ ) چنانکه ‎Sontheimer,,‏
‏الف . قومینی؛ ب , قومنی دیده مود . 188080808 ۶ . ۴ - مصحف‌قوبیطن‌بوتانی
‎Sze!» Aconitum = dkéniton‏ > © -(عی) « قهرمان » جمم « قهارمة »
« دزی ج۲ص۱6: ‎ley:‏ « کپرمان » ‎kubruman‏ که بمعنی کاراندیش ‎col‏ ازمصدر ‎Kar‏
‏)= کردن) + مان (منش) « فاباس ۲۷۲۳ ؛کردی ع ‎qahtiman‏ > ژابا س ۱۳۱۹ :

‏اکر اشتر و اسب و استر نباشد کجا قبرمانی بود قهرمان را ؟

‎. ۰ ۵ ‏خرو باخی س‎ pel

#### BQT printed 1617 -> pdf 410

-۱1۱۷--
بر وزن امتیاز , ‎WS gem‏ است که نم
خدایتمالی - و داسته و ‎ath fur‏ در فرهنگه

جهانگیری .
کر ذهنك ۱ ه بروزن ‎np‏ بمعنی
جلد وتند وتیز و تمجیل و شتاب و سخت باشد.

یعنی بسیار جلد و نند ویز ‎AV)‏

کرد نگ ۲ « بروزن ‎pK‏
‏و ابله و بی‌اندام ‎wath‏

eh ‏کاف‎ ae [SoS
‏وسکون لام ۰ بمعتی کردنگگ است کهدبوث وابله‎
.)۴( ‏و بی‌اندام راگونند‎

کرو ۴ ۰ بر وزن بدخو » شاخی را
گوبند که از درخت بربده باشند .

کر ده کار = بر وزن هرزه‌کار + مردم
جلد و کاردان و کار آزبوده (4) و تجربه کار را
گوبند ۴ و « ‎Ha‏ » درمقابل این است

کردیلن -: بقتح اول و الث ‎ln‏

(۱) چش : تیزوتند.
(4) چش : وآزموده و کاردان .

(0) چش :کرد نکل.
‎gd -: ote thy (0)‏ .

رسیده ولاممکوربنون 1095 نوعی ازاننعدان‌است
وآ براانجدان‌روم ی کوبند وچارپایانرا خوردن‌آن
باعث ‎ols‏ تاج کردد یمن بچه بسیار آورند .

کرر ه = بضم اول و ‎gt OS‏ وزای
قطمدار + زمیتی را گوبند که بجهت سبزی‌کاشتن
و زراعت دیگر هموار کرده و کثارهایآنرا بلند
ساخته باشند .

کرذمان ۱ = ‎pa‏ اول و ‎alta‏
‏و میم بالف کشیدء بر وزن ‎hie‏ » آسان را
‎a‏ مطلقاً - و ‎cones‏ عرش ‎quel‏ هم کفته‌اند
که آسمان ‎par‏ باشد ؛ و باين معتی بفتح اول
‎tly‏ هم آمده است که بروزن نمکدان باشد.

‎os‏ © بروزن کردن. نیم تاج‌مرصعی
بوده است که ‎Ip‏ پیشین از بالای سرخودیجبت
یمن وتبر ‎Led‏ ویخته‌اند و گاهی‌لیز(۵) پرسر(ج)
مینهاده اند ۷ - و تاجی را نیز گوبندکه از
دیبا دوخته باشند ؛ وباکاف فارسی هم آمده‌است
- و در عربی میان سر و فرق سررا خوانند ۸

‏(۳) چك».چش: بی‌اندامباشد.
(«)چك. چش: + یز

‏- از :کرد (کردن) ۳ مند ( پوند اصاف ) ۰ قس :کرد کار .

‏۴ - رد : کردنگل ورك : رشیدی

‎ist) kardu _ xala Cus: 5 ۴

‏دراز ‎Sa» Ay‏ برای کشبدن دلوآب وآفنابه از چاه بکار رود) ‎Ay‏ : کرد - در فرهشگه‌نظام
آمده : «کرد

#### BQT printed 1779 -> pdf 576

بیان نهم
در ‎GB‏ فارسی با رای بی‌نقطه مشتمل بر دوست و سی ‎Chey‏ لغت و کنایت
گر بفتح اول وسکون ثالی»,مخففا کر
باشد که کلمةٌ شرطیه است٩‏ - ونام جوششی‌است

مشهو رکه بعربی جرب گوبند ۴ - وبمعنی مراد
وه‌قصود باشد ۴ - و بمه‌تیکننده و سازنده هم

و آهنی ‎op‏ باشد دسته دار و در دو طرف ‎OT‏
‏ریسمان بندند یکی ‎dey‏ آنرا بگیرد و دیگری
‎aS Il,‏ نا زمین شیار کرد ناهموار را
بدان هموار کنند وآنرابعربی مسلفه‌وسواط(۱)

هت ۴ همچوکوزه کر وکاسه گر ‎geal,‏ آن . | خوانند ۸ .
ومرادف کارباشد همچو آموز کار وآموز کر که گر اد بکر اول بروزن ‎Ute ald‏
ازهر دومعنی فاعلیت مفهوم میگردد وقتی که با ]| کهنه راکوبند .

کلمادیگی تر کیپ‌شود - وبضم‌اول نام رووخاله -
‎cul‏ در سرحد ملك غزان » وباین معنی باکاف

گرادون ‏ با رای قرشت بر وزن
فلاطون » نام جوشتی است کهآ نرا داد خوانند
ویعربی قوبا کویند ‎٩‏ -

گر از بطم اول بروز نگداز ‎oes‏
‎Sys‏ نرباشد که جفت خول ماده است*٩-وخرام‏
ورفتاری که از روی تاز وتکبر وتبختر ‎Mask‏
‏و ی گویند بممنی خرام و رفتار از روی ناژ

تازی مشهور است ۵ .
گرا - بفتح اول‌وثانی مشددبالف کشیده»
پمعتی بنده باشد که در مقابل آزاد است ۲ -
وحجام وسرتراش ‎Boy‏ را نیز گوبند۷ »و کاهی
اين ‎bid‏ را بطریق ‎ches‏ هم بزبان آورند -
)1( خم ‎aie:‏ ومشواط -

۱ )4: اگر؛ کردی8067 (اکر) ‎Up‏ صس .»۳۵۷‏ ۴ - مرشی‌است کهدادهها يکوچك
بربدن انان‌وجانوران پدید آرد وخارش کند ومریض راه ک رکین» (مخفف آن : ک رگن) کوند.
اوستا - ‎garenu‏ (جرب)؛ کردی ‎(Oe) BIT‏ بلوچی 88۲ (یسی » جرب) « اسشق ‎۸٩0‏ »
و رك : هوبشمان » ایضاً ؛ پهلوی ‎Bal‏ (جرب) « دارستتر , تبمات ج ۱ ص 6۹۵ .
۴ رل :کر . ۴ اوستا - 64۲8 - (ساخته) » یپلوی ‎aie. gar. - kat‏
‎kara - ott‏ - ۶ اسشق ‎ker coo Xe cant‏ - (وبرانکر [وبران کنتده]) « ژابا س٩4۳‏ >-
ه‌ رگ :کر ۰
‎LS plea

#### BQT printed 1787 -> pdf 584

- ۱۷۸۷ کردان
بالف کشیده وبسین بی قطئزده , ستمگر وظالم
‎ua SI,‏ ۸ ؛ وبا شین قطه دار هم آمدماست .

گرث ‎e WUT‏ بنتح‌اول و کسرناكث,
‎ols‏ را گویندو آن غباری باشد که درپرتوآ فتاب
کهازروزنه برجابی‌افتدظاهر کردد وبعبی‌سمراره
خوانند .

گردا گرد بغتح‌اول بروزن‌تنها گرده
بمعنی پی‌درپی وهمیشهدر گردش‌باشد ‎٩‏ سوبکس
ارل ‎GE,‏ فارسی, اطراف وجواب را گویند*۱.

گر ‎STS‏ » معروفاس تکمعرچیز
‎Le‏ آلود باشد - و کنابه از شخصی که اسباب
واموال دیوی را حامل است .

گرد ‎oo ST‏ سازد © ‎lal ie‏
واموال دییوی دهد پکسی .

گر ‎Noles‏ بر وزن ‎ob)‏ بوعی از
کباب است. وآن‌چنان باشد که کوشت مرغ با
شت کوسفند در ‎OT‏ بجوخاند و بمد از آن

یکی اول ‎yam‏ مدور ودوری باشدا - ودور
وحوالی واطراف را ‎js‏ کفتهاند ۴ - وافادثجمع
هم میکند که کرد آمده و جمع شده باشد -
‎teers‏ شهر و مدیثه هم هست ۴ حمچو داراب
کرد وسیاوش کرد که مراد از ‎OT‏ شهر داراب
وشهر سیاوش است - و بمعنی خ رگاه لیز بنطر
آمده است ۴ - ‎Gy‏ اول و قتح ثانی» مخفف
کیرد © باشد .

گر دا © بفتح اول بروزن فردا؛مخفف
کردان است ۷ - و بادبر را ‎gt‏ کویند و آن
چوبی باشد مضروط ی که طفلان ‎glen‏ بر ‎OT‏
‏پیچند. و از دست رها کنند تا در زمبن گردان
شود۷ - ویک اول پمعنی حجت باشد .

Bram! ‏بکسر اولوبای‎ » blo FP
‏کشیده وبدال زده ؛ نام شهر مداین است وآلرا‎
Uy ‏پیشدادبان است‎ ae ‏دیوبند که از‎ Sayegh
. ‏کرده وجمشید باتمام وسالید‎

گرداس پم اول وسکون ثاتی‌ودال

۱ - پهلوی 801(74 . ركه: حوبدمان - ‎۰٩۰۱ Gel‏ ویزپهلوی ‎Birt‏ (مدور)ءارمنیع
( کرد ‎(ob‏ . از ‎girtak‏ ۵ دیب رکه ص ‎eva‏ «استق ۰۸۰۱ .
۴ -«کرد» ودبگرد» ( اطراف » دور ) از ‎Ley‏ ۷۵۲۶ (گردیدن) . رك : دارستتر .
‎obs‏ ج ۱ص ۲۸۳ . ۴ - پارسی باستان - 6۳08 - ۵ 6 پپلوی ‎Kart‏ - ( قس :
1 ) .)4 : اسشق - عوبشمان ۹۰۰ استی ‎NA. 2 < 807864
```


## [2026-09-06T22:19:07.373Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nimport re,json\ndef getpages(f):\n    d=open(f,encoding='utf-8',errors='replace').read()\n    parts=re.split(r'\\[pdf page (\\d+)\\]', d)\n    return {int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}\nv4=getpages('BQT_v4_pages.txt')\nfor pr in (2157,2164,2432):\n    p=pr-1917\n    print('#### BQT printed',pr,'-> pdf',p)\n    print((v4.get(p,'MISSING'))[:1500]); print()\nEOF"
}
```


## [2026-09-06T22:19:08.677Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && grep -n \"کاریدن\" BQT_v3_pages.txt | head; echo \"---gvardan---\"; grep -n \"گواردن\\|گوارش\" BQT_v3_pages.txt BQT_v4_pages.txt | head"
}
```


### [2026-09-06T22:19:09.470Z] TOOL RESULT

```
#### BQT printed 2157 -> pdf 240

-۱۷- ره
کربا راگوبند ۱ - و بمعتی فریاد همست ۲ | تختانی » حکم وفرمانی باش که سلاطین وحکام
- وعربان گریز راگویند که از کربختن‌است ۴. | بجهت جمع شدن و کرد آمدن سپاء ار لشکر

نغیر نامه - بفتح اول و کسرنانی‌وسکون | می نوسند (۱).
بیان شانزدهم
درنون با قاف مشتمل برسی وسه لغت و کنایت
نقاب خصرا - کنتابه از آسمان | بهردومعثی آمده است 8 .
است ۴ . نقد شش روزه * - کنایه ازدیا
نقاب ثیلی - کنایه از مب است که و مافیها امت ۴ .
بمربی لیل کوبند ۴ . فقد گیر ان ‎٩‏ «کنایه ازمردمانی باشد
نقد جان - کنایه از جان است که | که رشوت میگیرند ورشوت میخوراد - وطالبان
روح باشد - وزر وسیم سره رایج را نیز گفته‌اند. دیا را ی ز کوبند ۴ .
نقد روآن - بسمنی‌نند جان است که فقره « بنم اول, معروف است که بعریی
کنایه از جان - و زر وسیم رایج باشد چه روان | فنه‌کوبند ۷ - وکنایه ازهرچیز سفید هم‌هت
(۱) چش : لوسند . َ
۱ - شکل قدیمترآن « بیور» .کردی 3811۳8 (شیپور) « ژابا ص 4۲۲ > » معرب نقیر
« دزی ج ۲ ص ۷۶۰ >. مجازاً قضمی ازکرباکه بیشترفلندران دارند وبآن « شاخ نقیر» و «بوق
اغیر» هم کویند « فرهنگه نظام ».- درموسیقی نام آوازست ازدستگاه همایون «فرهنگه نظام».
۴ - نه من کردم از دست جورت لفیر که خلفی ز خلفی یکی کشته کیی :
5 سمدی 2 فرهنگه نظام > .۰

و رك : تذکرةالاولیاه چاپ اروپا ج ۱ ص۲۱۱ یه ۴ - (عر) « نفیرکامیر » گروه هردم

ازسه تا ده - وفومی که بکاری‌پیش روند وبا کسی کریزند پاازهم گربزند درجنگه.*«متتهی‌الارب».

۴ - رك : رشیدی - * - ر4 : روان . ‎٩‏ - جمع « نقدکیر» ( از: تقد

(عر) + کیرل کیرنده] ).

۷ - درسندی 87۴۲۸ (سیم) رل : 60۳82۵176 46 89921 ,3.860۷601816

5 .۱929,0 و۲ ۰ عناندم عس 2 5808416006۰ وآن مر کیت از*8 (۱ه نا) مد

(کرده

#### BQT printed 2164 -> pdf 247

نگزرد ۲۱۹
نگریدن ۱ بروزن درویدن » بمعنی نگزیرد * - بمنی‌چاره‌ای تباشدوعلاج
نگرش باشد که دیدن و نگاه کردن است . نبود . :
نگریحتن ؟ « بکون سین بی نقطه نگل ۱ - بفتح ارل وسکون تانی ولام»
و فتح فوقانی » بسمنی نگربدن است که نگا, | آنکه خطش تام ندمیده باشد پعتی پسری که
کردن و دیدن باشد . مزلف شده باشد .
نگزده ۴ « بفتح‌اول وثانی‌وسکون زای تگندن - یکسر اول بروژن فکندن ّ
فارسی و دال مفتوح , کوزه ومشربهٌ ‎)٩(‏ سفالین بسستی آچیده کردن جامه وا بخیه کردن سوزلی
راگویند . ند
َ : ده « بروزن فکنده » بخیه‌وآجیدهة
نگزرد ؟ - بح اول و سکون ثالی جامه وسوزنی راکوت ۸ - و بمعنی دفینه هم
وکس زای نفطه‌دار و رای بي‌قطةٌ مفتوح بدال | کفته‌اند پمنی آنچه درزمین و غیره پنهان کنند
بی‌نقطةٌ زده » مخفف نگزبرد است یمتی چاره‌ای | و درخ دیگر دفتینه نوشته بودند وآن‌افزاری
لباغد وعلاجی لیست. . است جولاهگانرا ‎٩‏ -

() چش : مشروبه ."

۱ از : نگر ( ریعه )۳ یدن ( پسوند مصدری )۳ انگرستن ۳ نگریستن . پهلوی
]3181۲6 (نگرید) * پارسی باستان 81۷۴12811 8 ‎«٩‏ هوشمان ۱۶۳۸ ريشة
این کامه در اوستابی ۸28082۳861 » فارسی نگاردن, دیده میشود « اسشق ۰۱۳۸ از : -
7 ( بغاطر آوردن » ذکر کردن ) «بارتولمه ۸۸۸ «* نیب کاس ۰۰۱۵۹ کردی ۰31۳1
(دیدن, ملاحظه کردن) «ژابا ۰4.۲۷ قسی: کیلکی: 52-708۳258187 ( وانگرستن,
نگریتن ). ۴ * نگرستن . رك : ح ‎٩‏ صفحهٌ قبل.

۴ << بکرده « فولری ]1 ۹۶ بعضی بکاف تازی آورده‌اند « جهانگیری » «رشیدی»
و بعی بزاء تازی گفته‌اند « رشیدی >. ۴ - ر: گزردن. -رك :گزیر گزردن .

. ‏مصحف «تگل » « لفت فرس اس ۳۲۱ وار4 :اس ۵*۷ ح۳ همان کتاب‎ - ٩

۷ -رك : گنده . ۸« اللذان ‏ رشتةٌ نکنده» «الامی فی‌الاسامی ص 4۳>.

‎٩‏ - در جهانگیری ورشیدی بم

#### BQT printed 2432 -> pdf 515

پزدان ۲۳۲-۳
آن ربزندء وبسنیبزدادی کوفته را گوبند که در | یزدگرد است که پدر بپرام گور باشد و او را
درون آن‌تخم مرغ پخته‌باشند وآنرا یزد‌آدین | بزدجردالائیم میگفتند . بغایت ظالم بود. روزی
هم میگوبند که بمد ازبای حخطی در آخر نون | درکنارچشمهٌ کلست که ازاعمال طوس است اسپی
باشد . اورا لکد زد وکشت - ونام پسرزادة انوشیروان

یزدان! » بنتم اول وسکون ثانی‌ودال | هم «ست که آخرملوك عجم باشد. گوبند. درشهن
بالف کشیده وبنون‌زده. بکی‌ازنامهای‌خدای‌تعالی نیشابور بردست ملازمان خود با آسیابانیکشته
امت جل جلاله - و نام فرشته‌ای هم هست که | شد. 4
فاعل خیراست وه کز ازوشرپیاید. وطابقة‌تنویه یز ك؟ « بفتح اول وئانی وسکون کاف»
ی خیررا بزدان وآفربنش مرو هدن | چیمی قلیل ومردم کمی را کوین د که در مقدمه
ند وهمچنینآ فربنندء‌نورر! بزدان‌وآ فربننده ی
ظلمت را اعرمن, و فتها خدای باطل راو شعرا و پیشا پیش لشکر براه روند و بترکی قراول
خدای حق را خواند (۱) .۰ خواننده - وپای‌وپاسیادالرانیز گفته‌اس ویمعنی
پزدان‌بخش؟۲ < نام وزیر هرمزین - جاسوی هم آمده است .
انوشیروان بوده است - رف - پروزن وزنه. خوهر خواهر را
پزدجرد؟ - بکر جیم» ممرب | کویند .
() چك» چش: کوبند .
۱ - ارستا ۰7828180870 پهلوی ۰2218 7824]8[8 ۰ 282420 ۰ قی :

ایزد «اسشق ۶۱۱۲۷ یزدان دراسل جمع «یزه» (* ایزد [ه م.]. 8284 ازاوستایی 782818)

امت دریهلوی. ر: لیب رکه صس۱۶۹؛ کر بتنن. ساسان ص۲۹۰ - درفارسی بمعثی «فرد بکاررقته

امت: «منووان که «وگویند: یکی پزدان ودیگر اهرمن ...> «ناصرخرو بلشی. جامع الحکمتین

۳۱ ۲ - درفهرست شاهنامة ولف‌نيامده. (تر کیب اسم عفعولی بمعنی «یزدان,خشیده»

ازقبیل«شاهنواز») (ازیادداشتهای علامه محمدقزوینی) ۴ - معرب یز دکرت+9824687

(248) ۰ سرب
```


### [2026-09-06T22:19:09.533Z] TOOL RESULT

```
---gvardan---
BQT_v3_pages.txt:47514:گوارش ‎-f‏ بضم آول‌بروزنگذارش»
```


## [2026-09-06T22:19:33.962Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nimport re\ndef getpages(f):\n    d=open(f,encoding='utf-8',errors='replace').read()\n    parts=re.split(r'\\[pdf page (\\d+)\\]', d)\n    return {int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}\nv4=getpages('BQT_v4_pages.txt')\nfor p in (244,245,246):\n    t=v4.get(p,'')\n    if 'نگار' in t or 'نگاردن' in t:\n        print('#### pdf',p,'printed',p+1917)\n        print(t[:1800]); print()\nEOF"
}
```


## [2026-09-06T22:19:35.791Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nprint(len(pages))\nimport re\nfor i,p in enumerate(pages):\n    if 'انگاردن' in p or 'انگاشتن' in p:\n        print('leaf',i,'~printed',i-220)\n        print(p[:1200]);print('---')\nEOF"
}
```


### [2026-09-06T22:19:35.813Z] TOOL RESULT

```
#### pdf 245 printed 2162

بیان هیجدهم
در نون با کاف فارسی «شتمل بر بیست و دو لغت وکنایت
نگ ۱ - بفتح اول وسکون نانی؛ کام را | امعنی هم‌هست پعنی بنگار ونقش کن۷ -وکنایه
گوبند که سقف دهانت . از محبوب و معشوق وشخصی است که اورا بیار
نگمار؟ - بروزن شکار . بممنی بت‌باشد | دوست دازند ۸ .
که بعربی صنم گویند ۴ - وبمعنی نقش‌ومرادف نار خانه ‎٩‏ , خان‌ای را کوین دکه
نش هم هست ۴ همچو نقش‌ونگار ونقشی که از | بنقش وانگار آراسته باشد بعنی انقاشی کرده
حنا بر دست وپای محبوب کنند * - و انگارنده | باشند .4
و تقش‌کننده (۱] را از کوبند۹ -و امر باین
۹ -کنابادی 881 (دندان)3262883 886 (دندان میزند ) «گناپادی» » قس: نك :
و۰4 ۴ - اسم از نگاشتن (۸.م.) + وق : نگربدن » نگریستن ۰ ۴ - ره : جهانگیری,
رشیدی » فرهنگه نظام ‏ ۴ -کردی 8162۲ ( نقاعی » نوشته ) « ژابا س 4۷۳ :
از ی ونگار در و دیوار شکته آثار پدید است صنادید عجم را .
عرفی شیرازی « اءثال و حکم دهغدا >
8 - رشیدی آرد : ۶ نفشی چند که از حنا بردست وپا در روز عید وجد نکشند و آهك
ولوشادر سیاه کنند ۰ واين معنی‌زديك بممنی‌فش است . اظامی( کاجوی) کوید :
دخ آراسته دستها در انگار پشادی دوبدندی ازه رکنار .>
۹ - اسم فاعل مرخم ( < نگارنده ) : صورت نگار » روزنامه نگار - و لیز اسم مفمول
مرخم (* نگاریده < نگاشته ) : زرنگار . ۷ -ر4 : نگاشختن .
۸ - دیر آمدی ای نگار عرمت زودت ندهیم دامن از دست .
۶ کلتان س ۰۱۳۷
‎٩‏ - از :انگار (و.م ) +خانه- نگارخانه چین ( * چینی) ۳ نگارستان (وم.) :
کرالتنات خداوندیش ( کلتان را ) بیاراید نگارخانهٌ چینی ونقش ارتنگی است.
* کلتان سمدی مس ۱۷ *.
7 نگارستان - بکر اول وچهارم . از : انگار (۸.م.) ۳ ستان ( پوند مکان ) ؛ جای
نش ونگار . محل پرنقش وتصویر » کاخ متقوش و مصور :
این نگارستان وین مجلس آراسته را صورت از چشم دل وچشم درها نشود .

* منوچهری دامغانی ص ۱۲ ( در وصف قسر ممود غزنوی )»
- « نگارستان > و «نگارستان چین » را در داستانها موضعی در چین پنداشته‌اند پراز تصاویر طرفه
وق ونگار بدیع » وهماست که بنام «نگارخانه» خوانده‌اند . در داستان « دژ هوش ربا >(باهتمام
سبحی مهتدی .

#### pdf 246 printed 2163

۱۹۳-۳ تکرش
* نگاشت!۱ « بکون شبن ونای‌قرشت, نگران ۹ < یکر اول بروزن پران,
ماضی نگاشتن است بعنی لوشت والقش کرد | بممنی منتظ و بیتنده و تأمل کننده باشد.
وساخت . نگرستن ۱ - بکر اول وفتح ناني,
نگاشتی ؟ » بکراول بروزن‌فراشتن, | مغفف نگریتن است که بنمنی آنگاء کردن
بمعنی لوشتن - و نقش وانگار وفقاشی کردن | ودیدن باشد .
باشد ۴ . نگرش ۲ - بکر اول و سکون آخر
نگاشته ؟۴ - پسمتی نش کرده شده - که شین ققطه‌دار باشد » بمعنی‌نگرستن اس ت که
ولوشته - وساخته شده باشد .4 بمعنی نگاه کردن و دیدن باشد .
۹ ر4 : نگاشتن . ۴ * نگاریدن . متمدی « نگریدن > (۸ .م۰ ) و
, نگریتن 3 (هم.) » پپلوی 47( وغیره » قس : ارمنی 7 (ضویر ‎ )‏ 26۶۲8۵8 ۰
اسشق ۰۲۱۳۳۹ ۴ - آن صورتها که ستا رکان را بدو نگارند . « التفهیم‌س
۸۹ ۴ - اسم مقعول از «نگاشتن» (هم.) 8 - از : لگر (نگرستن,نگربدن)
+ان ( یوند صفت فاعلی ):
ارغوان جام عقیفی بسمن خواهد داد چشم در کس‌بشقایق نگران خواهد شد.
حافظ شیرازی ص ۰۱۱۱
‎-٩‏ از :دگر (ریشه) +ستن ( پوند مصدری ) * نگریتن :
منگر در ( اسر ) بتان که آخرکار لگرستن کرستن آرد بار .
ضیاء الدین فارسی «فرهتگه نظام» ورك : امثال وحکم دهغد! .
۷ - پهلوی 181۲198 «اونوالا836121868:*۹۶؛ پاز و 1عوزم. صط5ع هو اه
«عوبشمان ۱۰۳۸ » از : الگر( نگرستن ۰ نگربدن) اش ( پوند اسم مصدر) : « پن دبدمن
از واسطةٌ دیدن او ازمن دیده پردوخت ولگرش باصل‌کار و وت خویش درآموخت .» « نذ کرة
الاولیاء چاپ لیدن ج۱ ص ۱۷۲ ۰
5 قاه - بکر اول . اوستا - 816882 5 (قی :آگاه) » پپلوی 8)1(628 »کردی
2 م2 » بلوچی ع 5 رلد: اسشق ۱۰۳۷ ؛ ريشهٌ آن 88ظ ( دیدن » نگریتن ) است
« پارتولمه 40۹ » ؛ گیلکی (رشت ) 8183 , کیلکی ( لنگرود ولاهیجان ) 28 ؛ نظردیدار-
نگاه کردن » دیدن ». نظر کردن .- نگاه داشتن » حفظ کردن » مخفی کردن : «مردمآزاری ۰
سنگی برسرصالحی زد. درویش... سنکه را نگاه همی‌داشت نا وقتی که سلطان را برآن لشکری
خشم آمد #«گلستان ص ۰.۴۵۳
بقیه ازحاشيهٌ صفحةٌ قبل
5 #ارش - بکر اول و چهارم » از : نگار (ه.م.) +ش ( پوند اسم مصدر ) ؛ نش
کردن- تحریر» نوشتن . ادارة نگارش , ادار
```


### [2026-09-06T22:19:37.484Z] TOOL RESULT

```
777
leaf 391 ~printed 171
رن
ار ه- باازای فارسی بر وزن غمزه ؛
مرجماث باشد و آثرا ببربی عد ی گویند .
انسته - بفتم اول و کسرثانی و سکون
سین بی‌قطه و فتح فوفالی 4 مقصورآ دته است»
وان بیخ کیاهی باشد خوشبوی که بعربی سعد
" گو بکف .
۰ ۰
انشانا - بفتم اول و سکون الی وشن
فرشت ونئای مثلته هردو مالف کشیفه » بسربالی
دوابی‌است که آنرا بغارسی مویزكك وبعربی زسبت
الجبل خوانند .
اتطلیون « با ای حطی ولام وتحتانی
بروزن عنبر گون , بلغت بونانی۱ فوی قزح را
کون دک هکمان شرطان باشد .
| نطی فیا۳ - بروزن‌افلونیا. بلفت‌ونانی
کاسنی شامی را گویند وآن سرد وتراست ودجگر
گرم را نافم باشد .9
اقاق »یک اول و سکون تانی وفای
بالف کشیده و بقاف زده ۰ روغن زءتون تازه را
گویند .
ات - بر وزن رحست  )۱(‏ همان
وخارت وزبانرا کویند که سمعنی غبن‌باشد - ودر
عربی بمعنی ننک و عار آمده است ۰
] نقست « بروزن , بدمست » پرده وتنیده
عنکبوت وا گوشد .
افقر دیا - بختح اول و فاف و سکون
ثانی و را و دال بی نقطه و تحتانی بالف کشیده »
لغتی است رومی و بعضی کوبند بونالی ۴ وممنی
آن مانند دل‌باشد وان چیزس تکهبلاد ر گوشد.
)۱( چاثه : زحمت.
۱ - بیونانی 50461105. «افتشنگای».
انگارده
بهترین وی آست که سیاه و فربه باشد و چون
بشکنند پر شیره بود . و آن گرم و خشك است
در چهارم» فوت حافظه دهد وذهن را تب زکند ,
و بعربی‌ثمرقالبلادر خوانند وبهندی بلاو مگویند.
قلیا - بکر اول و قاف و سکون‌ثان
---
leaf 392 ~printed 172
اگارده است که افسانه و سر گذشت باشد .
انگاده ۱ ه بروزن عموارء ."هر چیز
"که افانه وس گذشت داشد - وباد گذشتها کردن
رانیز کوبند - و ازسر گرفتن سر گذشت وافانه
را عم گفته اند بطریق کنابه چنانکه ا گر کسی
بسیارومکرراز گذشته بگوید گویشدهانگاره‌میکند»
یعنی باز از سر هیگیرد - و پس پی خزنده از
شرم و حیا را نیز کوبند - وبمعتي دفتر وحساب
و نامه اعمال هم نوشتهاند .
انگادیدن ۱ » بر وزن ترسانیدن »
بمعنی هو رکردن وینداشتن ‏ و گمان بودن‌باشد .
اناد » با زای‌هوزبروزن پرواز .افزار
آن اووات است .
انگاشتی ۱ -بر وزن برداشتن. بمعنی
صور کردن و نداشتن و کمان بردن باشه. .-
انگام ۴ » بروزن و معنی‌هتگام است
که موسم و وفت باشد .
انگاهه ۲ - بر وزن و معنی هنک‌امه
۱ راد : انگاردن ۰
۳ ت ازمادهٌ اذیدمن» رژد انجمن.
ات
است که مجمع و انجمن بازیگران و قصهخوانان
ا لگیین ۴ - با بای‌ابجد بروزن‌عنبرین,
سل و شهد را گوبند .
انگیینه - بروزن شنبلیله , نام حلوامی
است و ان قلن باشد که نيك بقوام آورده‌باشند
و برطبقی ریزند تا سخت‌شود و دندان کیر گردد .
انگدان ه بنم نالك ودال بالف کشیده
بروزن مردمان , شنای را گوبند یمنی دمومردم؛
و آن جانوری باشد وحشی شبیه بادمی ؛ و در
جاوتری میگوبند واه اعلم - و نام درختی حم
نقطهدار هم آمذه است - و نام قربه‌است‌ازفرای
کاشان که بانگوان اشتهار دارد.
انگرده ۳ بشم ثالث بروزن‌افرده. دانةً
انگور که از خوش
---
leaf 490 ~printed 270
و کار بهوده و بیفایده کردن باشد . #
پر ود قلكك - کنابه ازماه است که‌قمر
باشد - و ژحل را نی زگفته‌اند 3
بر لژزن - بکر اول و تحتانی مجهول
بروزن شیمن » پرویزن باشد که بعربی غرپال
و علپال کوبند ۴ -و بممئی ترشی بالا هم آمده
لت - و ابه‌ای را نز گویند که از کل ساخته
باشند و بربالای آن‌نان پزند » و بقتح اول‌بمعنی
بر لژ ۵ » بکسر اول وئالث مجهولبروزن
سفیده . صمفی است دوایی شبیه بمسطکی وآن
سبك و خشك و بدبوی‌میباشد » و حمربان‌باززد
ریانما۰ با حای بی شطذ ولام
مشدد بالف کشیده , بربان باتره و پودنه وترخان
و نان و ییاز اون ۰
بریحی ۱ با چیم بر وزن رسیدن »
تنوری باش د که در آ نکماج و نان سنکك پزند ۰
و جربی فرن گوبند بضم فا .
بریخ زدن- بنتجبای حطی, کنایه از
خاطر محو نمودن و تلم نبردن و فرأمو شکردن
سونایدیدساختن‌ومعد وم گردانیدن- وهیچ‌انگاشتن
باشد -
بر بخ و شتن » کنابه‌از هیچ‌انگاشتن
- وکارییمدار و بی‌اثر کردن وضایم ساختن کاری
۱ - رك : برزن و پریزن . ۴ - رك : پرویزن . ۴ ٩‏ بریجن » پهلوی .
0 , ابرانی‌باستان [0۲21 * (یختن » برشتن) «اسفا ۱ : ۲ س ۷۱ *.
ری - بفتح‌اول . ظاهراً اسل آن‌از کلملانینی ۷5۲۵۸/105 کرفته شده بمعتی‌چاریای
چاپار و اب چایار وسپس بمعنی مك . سد ها باداره و دستگاه چاپار و عاقبت برمنزلی که بچندو .
حو.کز چاپار است اطلاق کردید و این منزل در بلاد ايران دو فرسنگه سه‌میلی و در ممالكشریی
اسلامی 
---
leaf 648 ~printed 428
کوند وآن دا گربه نز خوانند .
نج هر لم» کیهی باشد خوشبوی
باندام پنج انگشت - کویند مریم مادر عیسی
علیه السلام در هنگام وضع حمل بر آن کیاء
چسسلده بود*
بنج یو ۱۵۵ - با تحنانی و واو مجهور
و دال بر وزن نج روزه : ینعی ضف عشر
است چه ده بوده ۴ عثر را گویندکه ده يك
باشد .
نك بفتح او وسکون ثانی ودال ابجد,
آنت که بعربی صیحت کوبند ۴ - و بممنی
زغن و غلواج هم‌احده است - وم اول كلولهةٌ
نبة حلاجی کرده‌باشد وبااول مکورزه نشتکاهرا
گوشد و مری مفعد خوانند 5
پند ار - بکسر اول بر وزن بیار »
تکیر و ععحب را گویشب وامر بدشمعتی هم‌هست-
(۱) چك: ژند ویاژند.
در اد
ویممنی فکر وخیال و تصور - و خود را بز رکه
پتداشتن ثیز آهده است.
بدنی آخر یندار است که فکر و خیال و تخل
پنداشتن ٩‏ - مک اول اش بزنن
مگذاشتن » بمعتی گمان بردن و ور کردن
باشد و بمعنی عجب و نکیر نمودن هم آمده
است . 4
ندش منم اول و فتح الث بروزن
کس کش کلولة ثبةٌ حلاجی کرده را کوشد.
باشك .
بلفت زند و بازند ۱ .
قنك ۵ ع بکس اول و سکون انی و فتح
. ظ , ینجوبه . رگ: الفهرست سص ۳۳۸ ۱۹ ۶« ششویبه» بجای «ینجوبه»‎ - ٩
۳ - رنده‌بوده. و ۳ پهلروی۳21001.]برانیباستان 2۸ (راء) «بارتولمه ۸۷ بارسی
باستان! 311 (راء), سااسکربت 4)1980, ارمنی10119, استی1300 (میلء آرزر) <ا-عق۰۳۳۰
«نیب رک ٩۲۹یس‏ اصللا پندیممنی راء است و مجازاً پنددادن بمعثی نشان دادن راه و دوش اینتی
4 وراوستا بمعن
---
```


## [2026-09-06T22:19:56.463Z] TOOL CALL #55: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-06T22:19:56.469Z] TOOL RESULT

```


```


## [2026-09-06T22:19:58.761Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD watkins kwer ===\"; grep -n \"kwer-\\|kʷer\\|k[ʷw]er-\" AHD_watkins1985.txt | head -20; echo \"=== IEC ===\"; grep -n \"kʷer\\|k^wer\\|qṷer\" IEC.txt | head -10"
}
```


### [2026-09-06T22:19:58.830Z] TOOL RESULT

```
=== AHD watkins kwer ===
652:kwelek-. Bundle. Proposed by some as the root of Latin culcita, mattress, sack, which is more likely of unknown origin: QUILT. [Pok. kuelak- 630.] kwelp-. To arch. 1. Germanic *hwalbjan in Old English *hwelfan, hwylfan, with parallel form *hwelman (> Middle English whelman), to turn over: WHELM. 2. Suf- fixed o-grade form *kwolp-o- in Greek kolpos, bosom, womb, vagina: GULF; COLPITIS, COLPOSCOPE, COLPOS- copy. [Pok. 2. kuelp- 630.] kwen-. Holy. Suffixed zero-grade form *kwn-s-lo- in Germanic *hunslam in Old English hisl, hiisel, Eucha- rist: HOUSEL. [Pok. kuen- 630.] kwent(h)-. To suffer. 1. Suffixed form *kventh-es- in Greek penthos, grief: NEPENTHE. 2. Zero-grade form *kenth- in: a. Greek pathos, suffering, passion, emotion, feelings: PATHETIC, PATHO-, PATHOS, -PATHY; PATHOGNO- MONIC, SYMPATHY; b. suffixed form *k“nth-sko- in Greek paskhein, to feel, suffer: PROTOPATHIC. [Pok. kventh- 641.] kwép-. To smoke, cook, move violently, be agitated emotionally. Hypothetical base of possibly related words. 1. Suffixed variant form *kup-yo- in Latin cupere, to desire: COVET, CUPID, CUPIDITY; CONCUPISCENCE. 2. Zero-grade form *kwap-, becoming *kwap- possibly in: a. Latin vapor, steam, vapor: VAPOR; EVAPORATE; b. Latin vapidus, that has emitted steam or lost its vapor, flat, poor: VAPID; c. Greek kapnos, smoke: ACAP- niA. [Pok. kuép- 596.] kver-1, To make. 1. Sanskrit karoti, he makes: SANSKRIT. 2. Suffixed form *kver-6r with dissimilated form *kel-6r in Greek pelér, monster (perhaps “that which does harm”): PELORIA. 3. Suffixed form *ker-as- in Greek teras, monster: TERATOCARCINOMA, TERATOGEN, TERA- TOID, TERATOMA. 4, Suffixed form *ker-mn in Sanskrit karma, act, deed: KARMA. [Pok. 1. kver- 641.] kwer-2. Something shaped like a dish or shell. Suffixed variant form *k”ar-yo- in Scottish Gaelic coire, cauldron, hollow, whirlpool: corrt&. [Pok. 2. kver- 642.] kwerp-. To turn oneself. 1. Germanic *hwarb- in Old English hwearf, wharf (< “place where people move about”): WHARF. 2. Germanic *hwerban in: a. Old Norse hverfa, to turn: VARVE; b. Old Norse *hvirfa, to whirl, perhaps assimilated to Danish hvirre, to whir, akin to the Scandinavian source of Middle English whirren, to whir: WHIR; C. Old Norse hAvirfla, to whirl: WHIRL; d. Old North French werble, a warbling: WARBLE!. 3. Possibly suffixed zero-grade form *kwrp-o- in Greek karpos, wrist: CARPAL, CARPUS. [Pok. kuerp- 631.] kwes-. To pant, wheeze. 1. Germanic *hwésjan in Old Norse huzsa, to hiss: WHEEZE. 2. Latin queri, to com- plain: QUARREL!, QUERULOUS. 3. Suffixed zero-grade form *kus-ti- in Greek kustis, bladder, bag (< “bellows”): cyst, cysTo-. [Pok. kues- 631.] kwé6t-. To shake. Zero-grade form *kwet-, becoming *kwat- in Latin quatere (past participle quassus, in composition -cussus), to shake, strike: CASCARA, KVETCH, SCUTCH, SQUASH?; CONCUSS, DISCUSS, PERCUSS, RESCUE, succussIoNn. [Pok. kuét- 632.] kvetwer-. Four. I. O-grade form *ketwor-. 1. Probably Germanic *fe(d)wor- in: a. Old English féower, four: Four; b. Old English féowertig, forty: FORTY; c. Old English féowerténe, fourteen: FOURTEEN. 2. Latin quat- tuor (> Italian quattro), four: CAHIER, CARNET, QUATRAIN; CATER-CORNERED, QUATTROCENTO. IT. Mul- tiplicatives *kveturs, kvetrus, and combining forms *kvetur-, *kvetru-. 1. Latin quater, four times: (CARIL- LON), QUATERNARY, QUATERNION, QUIRE’. 2. Latin gua- drus, four-sided thing, square: CADRE, QUADRATE, QUARREL?, QUARRY?; SQUAD, SQUARE, TROCAR. 3. Latin quadri-, four: QUADRI-. 4. Latin quadra, square: QUA- DRILLE!. 5, Latin quadrdns, a fourth part: QUADRANT. 6. Latin quadrdagintd, forty (-gintd, ten times; see dekm): QUARANTINE. 7. Variant form *ket(w)r- in: a. Greek tetra-, four: TETRA-; b. Greek tessares, tettares,
2071:PEG bak- PEGMATITE pag- PEJORATION ped-1 PELAGE pilo- PELAGIC plak-1 PELARGONIUM pel-2 PELECYPOD ped-1 PELISSE pel-4 PELLAGRA ag-, pel-4 PELLICLE pel-4 PELL-MELL meik- PELLUCID leuk- PELOPS okw-, pel-2 PELORIA kwer-1 PELT! pel-4 PELTATE pel-4 PELTRY pel-4 PELVIS pel-7 PEN! pet-
=== IEC ===
```


## [2026-09-06T22:20:09.219Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%DA%A9%D8%A7%D8%B1",
 "prompt": "Give the full Persian etymology section for شکار (šekâr) \"hunt\": Middle Persian form, Proto-Iranian reconstruction, any mention of *kar- \"to do\" or a separate root, and cited sources (Hasandust, Cheung, MacKenzie)."
}
```


## [2026-09-06T22:20:11.775Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%82%D9%87%D8%B1%D9%85%D8%A7%D9%86",
 "prompt": "Give the etymology of Persian/Arabic قهرمان (qahramān): what Middle Persian form is it derived from (kārframān? kāhramān?), the meaning \"steward/majordomo\", and any cited sources."
}
```


### [2026-09-06T22:20:17.254Z] TOOL RESULT

```
# Persian Etymology of شکار (šekâr)

Based on the Wiktionary entry, here's what's documented:

## Etymology Chain
The word traces to **Proto-Iranian *skar-** ("to pursue, to look for [cattle]"), which has no secure non-Iranian cognates.

## Middle Persian Forms
The entry notes that while شکار is "not attested in Middle Persian," related forms exist:
- A term meaning "bird of prey" 
- Another meaning "hunting ground"

## Sogdian Connection
The word is "perhaps a loanword from Sogdian" 𐽁𐼸𐼰𐽀 (škʾr, "to pursue, to drive"), which itself derives from the same Proto-Iranian root.

## Sources Cited
The entry cites **Cheung, Johnny (2007)**, *Etymological Dictionary of the Iranian Verb*, noting the Proto-Iranian *skar-* reconstruction on page 345.

**Note:** The provided content does not mention Hasandust, MacKenzie, or any separate *kar-* root etymology. The documented etymology focuses exclusively on the *skar-* root.
```


### [2026-09-06T22:20:18.338Z] TOOL RESULT

```
# Etymology of قهرمان (qahramān)

## Middle Persian Origin

The word derives from Middle Persian **kārframān** (also spelled kʾlplmʾn in Book Pahlavi), meaning "manager" or "overseer." The Wiktionary entry states: "from [script needed] (kār, 'work, affair') + [script needed] (framān, 'command, order')."

A dialectal variant **kāhramān** is also referenced as a possible intermediate form.

## Ultimate Source

The term traces back to Old Median **\*karhramāna-**, representing an ancient Iranian administrative designation that predates both Persian and Arabic usage.

## Semantic Development

The original sense of "steward" or "majordomo" (an administrative official) evolved in Persian and Arabic into the meanings of "champion" and "hero." The entry notes that Arabic قَهْرَمَان (qahramān) meaning "superintendent, majordomo" was borrowed through Aramaic from this Iranian root, explaining the initial *q-* sound rather than derivation from the Arabic root قَهْر (qahr, "force, wrath").

This semantic shift from bureaucratic to heroic connotations occurred within the Persian tradition itself.
```


## [2026-09-06T22:20:30.136Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%84%D8%A7%D8%AC%D9%88%D8%B1%D8%AF",
 "prompt": "Give the etymology of Persian لاجورد (lājvard) \"lapis lazuli, azure\": Middle Persian form, the place-name origin (Lājvard/Lazhward mine in Badakhshan), and any connection to -gird/-kird \"town\". Also list the descendants (Arabic لازورد, Latin lazurium, English azure)."
}
```


## [2026-09-06T22:20:32.052Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%DB%8C%DA%A9%D8%B1",
 "prompt": "Give the etymology of Persian پیکر (peykar) \"body, figure, statue\" and also anything on پیکار (peykār) \"battle\": Middle Persian forms, Old Persian patikara-, and Proto-Iranian reconstruction."
}
```


### [2026-09-06T22:20:37.060Z] TOOL RESULT

```
# Etymology of Persian لاجورد (lājvard)

## Origin and Place-Name Connection

The word derives from the place name **Lāžvard** in Badakhshan where the stone was mined. The etymology breaks into two components:

**First component** (_لاژ_): Traced to Proto-Indo-European *ǵʰelh₃- ("green"), cognate with Old Irish _glas_.

**Second component**: According to Bailey, derives from Proto-Iranian *varta- ("stone"), with cognates including Wakhi _wurt_, Northern Kurdish _ber_, and Central Kurdish _بەرد_ (berd), ultimately from Proto-Indo-European *wel- ("to press together").

## Key Descendants

The word spread widely through trade routes:

- **Arabic**: لازورد (lāzaward)
- **Latin**: _lazulum, lazurium, azura_
- **English**: "azure" (via Old French _azur_)
- **Romance languages**: Italian _azzurro_, Spanish _azul_, Portuguese _azul_
- **Germanic**: German _Lazur_, Czech/Polish _lazur_
- **Slavic**: Russian лазурь (lazúrʹ)

The document does not mention a direct connection between the etymological components and "-gird/-kird" (town), nor does it reference a specific Middle Persian form preceding the Classical Persian attestation.
```


### [2026-09-06T22:20:37.902Z] TOOL RESULT

```
# Etymology of Persian پیکر (peykar)

Based on the Wiktionary entry, here's the etymological information:

## پیکر (peykar) - "body, figure, statue"

The word derives from **Middle Persian** _patkar, pahikar_ ("picture, image"), which came from **Old Persian** _patikarā_, ultimately from **Proto-Iranian** _*patikárah_.

The entry notes: "From Middle Persian 𐭯𐭲𐭪𐭫 (ptkl /⁠patkar, pahikar⁠/, 'picture, image'), from Old Persian 𐎱𐎫𐎡𐎣𐎼 (p-t-i-k-r /⁠patikarā⁠/), from Proto-Iranian _*patikárah_."

A cognate appears in **Armenian** _patker_ ("picture, likeness"), which represents an Iranian borrowing.

## Note on پیکار (peykār)

The provided document does not contain etymological information for پیکار (peykār) meaning "battle." The Wiktionary entry focuses exclusively on پیکر (peykar) in its various meanings across Chagatai and Persian languages.
```


## [2026-09-06T22:20:45.483Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%DB%8C%DA%A9%D8%A7%D8%B1",
 "prompt": "Give the etymology of Persian پیکار (peykār) \"battle, fight, combat\": Middle Persian form, Proto-Iranian reconstruction, and whether it is derived from *pati- + *kar- \"to do\"."
}
```


## [2026-09-06T22:20:48.025Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%D8%A7%DA%AF%D8%B1%D8%AF",
 "prompt": "Give the etymology of Persian شاگرد (šāgerd) \"student, apprentice\": Middle Persian form (hašāgird / ašāgird), the reconstruction *haxā-kṛta- or *hašā-karta-, and cited sources."
}
```


### [2026-09-06T22:20:51.078Z] TOOL RESULT

```
# Etymology of Persian پیکار (peykār)

**Middle Persian Form:**
The word derives from Middle Persian _ptkʾl_ meaning "struggle, battle, dispute."

**Proto-Iranian Reconstruction:**
The term breaks into two components:
- Preverb from Proto-Iranian *pati- ("towards, to, against")
- Root from Proto-Iranian *kar- ("to do, make")

**Derivation from *pati- + *kar-:**
Yes, this word is indeed composed of these elements. As the source states, "the preverb is from Old Persian...itself from Proto-Iranian *pati-...and the root is from Proto-Iranian *kar-...ultimately a derivative of Proto-Indo-European *kʷer- ('to do, make, construct')."

The term ultimately traces to Proto-Indo-European *próti and *kʷer-, demonstrating how this Persian word for battle/struggle semantically connects "acting against" something through the combination of these ancient linguistic roots.
```


### [2026-09-06T22:20:54.622Z] TOOL RESULT

```
# Etymology of Persian شاگرد (šāgerd)

## Middle Persian Form
The word derives from Middle Persian *hšʾklt'* (/hašāgird/), meaning "disciple, pupil."

## Proto-Iranian Reconstruction
According to the sources, the etymological ancestor is Proto-Iranian *hašā-kr̥táh-*. This compound consists of two components:

1. **First element**: Proto-Iranian *hu-šāk-*, ultimately from Proto-Indo-Iranian *Hsu-* ("good") plus Proto-Indo-European *sekʷ-* ("to follow")

2. **Second element**: Proto-Indo-Iranian *kr̥tás* ("done, made")

## Cited Sources
The entry cites etymological work by Rastorgujeva and Edelʹman's 2007 *Etymological Dictionary of Iranian Languages*, which provides detailed analysis of the Proto-Iranian roots and their Indo-European origins. A reference to Keith Hitchins and colleagues' "Georgia v. Linguistic Contacts with Iranian Languages" in the *Encyclopedia Iranica* is also included.

The word shows cognates in Old Armenian *ašakert* and Aghwan, supporting its ancient Iranian heritage.
```


## [2026-09-06T22:21:02.249Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%AF%D9%88%D8%A7%D8%B1%DB%8C%D8%AF%D9%86",
 "prompt": "Give the etymology of Persian گواریدن / گواردن (govāridan/govārdan) \"to digest\" and گوارش (govāreš) \"digestion\": Middle Persian form (wigārdan / wiyārdan?), the preverb *wi- and root *kar-, and cited sources."
}
```


## [2026-09-06T22:21:04.033Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D8%A7%D9%85",
 "prompt": "Give the Persian etymology sections for کام: (a) کام \"palate, roof of the mouth\" — what root/Proto-Iranian form and any link to Proto-Indo-European *kʷem- \"to swallow, sip\"; (b) any other کام entries. Quote the reconstructions."
}
```


### [2026-09-06T22:21:06.530Z] TOOL RESULT

```
# Persian گواریدن Etymology

I cannot provide the etymology you've requested based on the webpage content supplied. The Wiktionary entry only states that **گواریدن (govâridan)** is an "alternative form of گواشتن, to digest"—it offers no etymological information about Middle Persian origins, the preverb *wi-*, the root *kar-*, or related terms like گوارش (govāreš).

To obtain etymological details including historical forms and linguistic sources, you would need to consult:
- Comprehensive Persian etymological dictionaries
- Specialized resources on Middle Persian linguistics
- Academic works on Persian verb formation and historical phonology

The current Wiktionary entry lacks this scholarly apparatus.
```


### [2026-09-06T22:21:10.865Z] TOOL RESULT

```
# Persian Etymology for کام

## (a) "Palate, roof of the mouth"

The Wiktionary entry for this sense notes: "(This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium.)"

No Proto-Iranian reconstruction or Proto-Indo-European connection is provided for this anatomical meaning. The document does not link it to PIE *kʷem- "to swallow, sip."

## (b) Other کام entries

The primary Persian entry traces to Proto-Indo-European origins:

**Etymology 1** (desire, wish, intention):
- Middle Persian: "𐭠‎𐭬‎𐭪 (kʾm)"
- Old Persian: "𐎣𐎠𐎶 (k-a-m /⁠kāmaʰ⁠⁠/)"
- "Proto-Iranian *káHmah"
- "Proto-Indo-Iranian *káHmas"
- "Proto-Indo-European *kóh₂mos, from Proto-Indo-European *keh₂- ('to desire, wish')"

This meaning (desire/intention) has clear attestation through ancient language stages, unlike the anatomical sense.
```


## [2026-09-06T22:21:22.910Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN guvar ===\"; grep -n \"guvär\\|guvar\\|güvar\\|gvär\\|verdauen\" HRN.txt | head -10; echo \"=== HRN camiden ===\"; grep -n \"camlden\\|camiden\\|cam-\\|schlürf\" HRN.txt | head -10; echo \"=== PHD wg ===\"; grep -n \"wigārdan\\|wigar\\|wiyār\\|w[iy]g'r\" PHD_mackenzie.txt | head -10"
}
```


### [2026-09-06T22:21:23.003Z] TOOL RESULT

```
=== HRN guvar ===
1774:Vegnen'; oss. d. warun^ t. vdrin (73); bei. gväris^
4534:t. ;ro; bei. gvahär, n. gvähar, göhär, gvär (131) 2); wa/.
=== HRN camiden ===
4101:ai. l/^(faw-, cämati (skr. camajiti) 'schlürfen',
4102:oss. cimin, ba\dimin 'schlürfen* (320).
9504:saufen, Suff, ahd. süfan 'schlürfen, trinken ver-
18144:cam- 160 änni.
=== PHD wg ===
```


## [2026-09-06T22:21:25.082Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%86%D9%85%DB%8C%D8%AF%D9%86",
 "prompt": "Give all etymologies for Persian چمیدن (čamidan): the sense \"to walk gracefully / strut\" and any sense \"to sip, drink, eat\". What roots are given (Proto-Iranian *čam-)?"
}
```


### [2026-09-06T22:21:31.247Z] TOOL RESULT

```
# Etymology of Persian چمیدن (čamidan)

Based on the Wiktionary entry, there is **only one etymology provided** for this word, relating to the sense "to strut, walk proudly" and "to flaunt."

## Root Origin

The entry states the word derives from "Proto-Iranian *čam- ('to walk'), perhaps a blend of Proto-Iranian *čarH- ('to come and go, wander') and *gam- ('to come')."

These proto-roots ultimately trace back to Proto-Indo-Iranian *čálH- ("to move, wander") and Proto-Indo-European *gʷem- ("to step, come").

## Additional Senses

**No sense meaning "to sip, drink, or eat" appears in this dictionary entry.** The entry only documents two related meanings: walking with pride and displaying something ostentatiously.

The entry does provide cognates in related languages like Baluchi čamag ("to shake, dance"), suggesting the root's connection to physical movement across Indo-European languages.
```


## [2026-09-06T22:21:39.254Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4090,4110p' HRN.txt; echo \"=== which leaf/page ===\"; python3 -c \"\nd=open('HRN.txt',encoding='utf-8',errors='replace').read()\npages=d.split(chr(12))\nfor i,p in enumerate(pages):\n    if 'cämati' in p or 'camati' in p:\n        print('leaf',i,'printed',i-21); print(p[:900])\n\""
}
```


### [2026-09-06T22:21:40.787Z] TOOL RESULT

```
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
=== which leaf/page ===
leaf 120 printed 99
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
446. cernber (geschrieben cenber) 'Kreis, R
```


## [2026-09-06T22:21:52.474Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && python3 - <<'EOF'\nimport re\nd=open('ARY_pages.txt',encoding='utf-8',errors='replace').read()\nparts=re.split(r'\\[pdf page (\\d+)\\]', d)\npages={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}\nfor w in ['گوارش','گواردن','پیکار','پیکر','شکار','انگاشتن','انگاردن','شاگرد','پرگار','چمیدن','لاجورد','قهرمان','یزدگرد','کام']:\n    hits=[p for p,t in pages.items() if w in t]\n    print(w, hits[:6])\nEOF"
}
```


### [2026-09-06T22:21:54.312Z] TOOL RESULT

```
گوارش []
گواردن [444]
پیکار []
پیکر []
شکار [2, 8, 12, 13, 39, 49]
انگاشتن []
انگاردن []
شاگرد []
پرگار []
چمیدن []
لاجورد []
قهرمان [36, 39, 99, 495, 524]
یزدگرد []
کام [5, 7, 20, 22, 24, 27]
```


## [2026-09-06T22:21:54.403Z] TOOL CALL #69: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D8%B1%DA%AF%D8%A7%D8%B1",
 "prompt": "Give the etymology of Persian پرگار (pargār) \"(pair of) compasses\": Middle Persian form, the preverb *pari- and root *kar-, and any cited sources."
}
```


### [2026-09-06T22:22:00.604Z] TOOL RESULT

```
# Etymology of Persian پرگار (pargār)

Based on the Wiktionary entry, the word derives from Proto-Iranian and Proto-Indo-Iranian origins. The source states: "From Proto-Iranian, from Proto-Indo-Iranian. Cognate with Sogdian...Northern Kurdish _pergal_...Sanskrit _प्रकार_ (prakāra)."

**Structural breakdown:**

The first element comes from Proto-Iranian *pari- meaning "around," which traces back to Proto-Indo-European *per- ("before, front").

The second element relates to the root *kar- (evident in the Sanskrit cognate prakāra and Kurdish pergal), which carries meanings of "sort, kind, form, manner."

**Note on Middle Persian:**

The entry does not explicitly cite a Middle Persian intermediary form, only Proto-Iranian as the direct ancestor. The word's appearance in an 11th-century Persian text by Abū Saʿīd Abī-l-Khayr demonstrates its established use in Classical Persian, but the etymological documentation skips directly from Proto-Indo-Iranian to Persian.
```


## [2026-09-06T22:22:10.351Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && python3 - <<'EOF'\nimport re\nd=open('ARY_pages.txt',encoding='utf-8',errors='replace').read()\nparts=re.split(r'\\[pdf page (\\d+)\\]', d)\npages={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}\nfor p in (444,):\n    t=pages[p]\n    i=t.find('گواردن')\n    print('== ARY pdf',p,'printed',p+1)\n    print(t[max(0,i-700):i+700])\nEOF"
}
```


## [2026-09-06T22:22:11.278Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nfor i,p in enumerate(pages):\n    if 'پرگار' in p:\n        print('leaf',i,'~printed',i-220)\n        j=p.find('پرگار'); print(p[max(0,j-400):j+900]); print('---')\nEOF"
}
```


### [2026-09-06T22:22:12.256Z] TOOL RESULT

```
== ARY pdf 444 printed 445

ا
أ
گواریدن گواردن / ۴۴۵
۱
لهستانی (۳0/34): 00۸ پسگلتهل ۶2۳3۵۷۵۵5 : ۱
روسی (8314(7/): هتاختاه 19497 ۸002 أ
لینوانی (/(1777114(74.)): این ان 3 (لت۸ه8) رد هس :
90908 ناه ۱
برهان قاطع : ۶ و ۱۸۶۴ ۱
یادداشت: ۲
چم این واژه در زبان یونانی: فرورفتگی؛ گودی :
چم این واژه در زبان لاتین:کیسه‌ی چرمی ۱
1
ِ
اوستایی (4/88727): 3171 روسی (۲/5514/۷): 1
پهلوی (/۸۷ا۳۸): ,۸ انا چکه (28077)): زد ۷۸:۱
606330۸ لینرانی (۷(فسابز ).03830 ,6883
سانسکریت (8478617): ال
ارمتی (/47۸48(14): ود ده پسگشت‌ها ند دنت
برنانی 022/0): ۰ 81871108162100 ,803 زر ار 1 را
لاتین (7100مل): 0 ,۷۵۵05 8 وی
فرانسه (۳8۵۸04): ۷۵۸ 2 ۷۵8۸۳۵ :
اسپانیایی (82۸(/37): ۷0۸2 9 (۷۸83ه) 1
ایتالیابی ((74/14): " اد ۵( 0 (016557) :0/2[5ت) لا
پرتغای (82ق070010: ۷۶ 6 (5ت۷
```


### [2026-09-06T22:22:13.972Z] TOOL RESULT

```
leaf 489 ~printed 269
است درحضرموت. کویت. درآنجا چاهی امت که
ارواح کفار و عنافین آنجا جمم شوند .
بر هو 3 - با واومجهول بروزن محموده
چیزیرا کوبند که ترديك بوختن رسیدموحرارت
آشس رن آ ثرا کردانیده و زرد کرده باشد .
بر هون -» بفتح اول بر رزن مجنون ؛
هر چیز مان خالی ۳ مانئد حالهٌ ماه
1
و دایره‌ای که از پرگار کشند - و چوب بندی
و خاربست- وحصار- و در خانه ومحوطه_ وغانة
کوچك را نیز کفته‌اد - وآریش و زیت رائیز
رازبانج است ۱ .کویند از دوزبکه آقاب‌ببرج
حمل میرود ح رکه هر روز ز يك درهم نخم‌راز بانه
با يك درهم فند سفید سفوف کند و تا سه ماه‌در
خوردن آن مداومت نمابد در نمام سال مریض
نشود ؛ و جمیم گزندکان تخم رازبانه خورند
بجهت روشنایی چشم . و افمی چشم‌خود راببهت
روشنابی و نقوت برآن مالد . #
برههی ؟ » بتح اول و ثالی و حیم
بروزن قلمزن» بمعنی بت‌پرست و زناربند باشد
و حکما و دانثه‌ندان و پیر و مرشد بت‌پرستان
و هندوان و آته تش‌پرستانرا هم میگوند -واصیل
و نجیب هنود را نز برهم نگویند » و بفتح‌اول گویند - و بمعنی کمر گاه و کم رکوه هم بنظر
و سکون انی بوزن کر کدن هم آمده است . آمده است ؛ و بنم اول لبز درستست .
دل ۲ ۰ ۳ . ۱
بر همنك * - بروزن سمرفند ۰ بمعنی بر هو ه » بروزن‌انبوه . صابونراکویند
برهمن است ت که پیر ومرشد - وحکیم ودانشمند
و اصیل و جیب هنود باشد .
بر همه 9 بر وزن طبقجه » مخغف
برهمن است که اصیل و 
---
```


## [2026-09-06T22:22:25.000Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nd=open('incoming/FFD/FFD_pages.txt',encoding='utf-8',errors='replace').read()\nparts=re.split(r'\\[pdf page (\\d+)\\]', d)\npages={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}\nfor w in ['گوار','پیکار','شکار','کردن']:\n    hits=[p for p,t in pages.items() if w in t]\n    print(w, hits[:12])\nfor p in (78,79,80,85,86,87):\n    print('=== pdf',p); print(pages.get(p,'')[:900])\nEOF"
}
```


### [2026-09-06T22:22:26.538Z] TOOL RESULT

```
گوار [80]
پیکار []
شکار []
کردن [14, 15, 16, 17, 19, 20, 25, 26, 29, 30, 31, 32]
=== pdf 78

ماده‌های ماضی و مضارع قارسی دری ۷۳
است. «گله» فارسی دری از 81188 فارسی میانه آمده است و 8128 از 874-42* فارسی
باستان. 874 صورت ضعیف ريش 8۵74 / 8720 است. 218 پسوند بوده است.
۱ گزاردن
گزارد + فارسی میانه ۷12274 < ایرانی باستان 3۳-1۵.-۷*. برای ۵ -> آراست. ۷:۱
پیشوند فعلی است. لَن صورت بالاندةٌ ريشهٌ 27 به معنی «حرکت کردن» است.
«(چریدن) از ریشهٌ 47 آمده است > چریدن.
گزار < فارسی میانه ۷1237 < ایرانی باستان 2۲-۵.-۷۷*. برای 2 > آرای.
گُزیدن
گُزید ج فارسی میانه ۷127۵ < ایرانی باستان ۶۷-6۲-1۵ برای ۵ > آراست. ۷
پیشوند فعلی است. آت صورت ضعیف ریشةٌ له به معنی «گزیدن» است.
گزین ج فارسی میانه ۷۵217 < ایرانی باستان ۹1-61-۵*. 120 نشانه‌ای بوده که برای
ساختن ماده مضارع از ريشه به کار می‌رفته است.
گزیدن
۰ کِ شت.+
گستردن
گسترد < فارسی میانه ۷181۵74 < ایرانی باستان ۴۷۷1-81۵۳-12. برای ۵ -> آراست. ۷1
پیشوند فعلی است. ريشهٌ 5187 به معنی «پاشیدن» است.
گستر < فارسی میانه ۷۷۶17 < ایرانی باستان ۷1-۹1۵۳-۵*. برای 
=== pdf 79

4۳ نفعلهای فارسی دری
شده است. 814 صورت ضعیف ريشهٌ ۶210 است.

«گسل» در فارسی دری مادهٌ مضارع «گسستن) است. در فارسی میانه مادةٌ مضارع

: اقا ملع آمده است و آن از ۷۷۹-۹18۵* ایرانی باستان آمده است. ۶104 از ادخال 8

پیش از آخرین صامت ريشه برای ساختن مادهٌ مضارع از ريشه به کار رفته است.

در فارسی دری «گسیخت» به جای «گسست» به کار رفته است.

گشادن, گشودن

گشاد < فارسی میانه ۴834 < ایرانی باستان ۷1-33-1۵*. برای 1۵ > آراست. ۷۷
پیشوند فعلی است. ۳3 صورت اصلی 3 است» « پس از ابه 5 بدل شده است. ريشة ۲3
به معنی «بستن» است. «گشود» در فارسی دری به قباس با «سرود»» «سرای» به وجود
آمده است.

گشای + فارسی میانه 152 < ایرانی باستان ۳-52-78*. # برای ساختن ماده از
ريشه به کار می‌رفته است.

گید(

گشت < فارسی میانه ۷251 < ایرانی باستان ۹279-12*. برای 1۵ -> آراست. ۷۷۸۲۲
صورت اصلی ۷۷279 است. 1 پیش از ۲ به 8بدل شده است. ‏ -

گرد + فارسی میانه ۷۷۵۲ < ایرانی باستان ۳:۵۳-۵*. برای 2 -> آرای,

گاشت. مادةٌ ماضی گاشتن» از 
=== pdf 80

ماده‌های ماضی و مضارع فارسی دری وی

گفت < فارسی میانه +801 < ایرانی باستان 80-42 *. برای 12 -> آراست. 6۵0 صورت
اصلی ۶باع است» ۳ پیش از 1 به ؟ بدل شده است. 90ع صورت ضعیف ريشهٌ 8200 به
معنی «گفتن» است.

گوی + فارسی میانه 83۷ < ایرانی باستان 8200-2*. برای ۵ > آرای.

گماردن. گماشتن

گمارد < فارسی میانه ۰8070370 (گماشت) در فارسی دری به قیاس با «کاشت».
«کار» به وجود آمده است.

گمار + فارسی میانه ۰801037

گواردن

گوار + فارسی میانه 6۳837 < ایرانی باستان ۷1-127-۵*. برای 2-> آرای. 137 صورت
بالاندةٌ ريشهٌ ۴۵۲ به معنی «کردنْ» است. ۷۷1 پیشوند فُعلی است.

مادهٌ ماضی در فارسی میانه 8083770 بوده که جعلی است. «گوارد» فارسی دری
بازماندة ۹1-137-1۵* ایرانی باستان است. برای 1۵ -> آراست.

گوالیدن (:بالیدن)

گوال < ایرانی باستان ۷3۲4-2-/۷*. برای ۵ -> آرای. ۷ پیشوند فعلی است. ۷۷374
صورت بالاندةٌ ۷۵7۵ به معنی «بالیدن» است و خود («بالیدن» هم از ۷۵7۵ آمده است >
بالیدن.

لرزیدن
لرزید < فارسی میانه 1272۵» مادةٌ ما
=== pdf 85

ار فعلهای فارسی دری
نوْشتن,» نوردیدن
نوشت « ایرانی باستان 21-۵7۶-1۵*. برای 1۵ > آراست. 8 پیشوند فعلی است.
: 4 صورت اصلی ۷87۶ است» 1 پیش از ۲ به 5 بدل شده است. ۷87۲ به معنی «گشتن»)
است و خود «گشتن» هم از این.ریشه آمده است. نوردید ماده ماضی جعلی است که از
مادةٌ مضارع با «ید» ساخته شده است.
نورد + ایرانی باستان ۴81-۷۵۲۲۵ برای 2-> آرای.
نهادن
نهاد « فارسی میانه 224 < ایرانی باستان 143-1۵:*. برای 1۵ > آراست. 7
پیشوند فعلی است. ريشهٌ 13 به معنی «گذاشتن» است.
نه « فارسی میانه 7 + ایرانی باستان 21-42-۵*. برای 2 -> آرای.
نهفت ۰
نهفت « فارسی میانه 218011 + فارسی باستان 00-1۵ -ط* + ایرانی باستان
2 برای 12 > آراست. 1 پیشوند فعلی است. 800 صورت اصلی ۶۶ است. 0
پیش از 1به ۶ بدل شده است. ريشهٌ ۶0 به معنی «آراستن» است.
نهنب < فارسی میانه 200000 < فارسی باستان 21-0020 < ایرانی باستان
۶21-۶ 2 پیش از 0 برای ساختن مادهٌ مضارع از ريشه آورده شده است.
(سفتن) هم از ريشهٌ 9 آمده است > سفتن.
نیوشیدن
نیوشید < فارسی
=== pdf 86

ماده‌های ماضی و مضارع قارسی دری شش ۸۱
ویراستن
> پیراستن
۱ هراسیدن

«هراسید» مادةٌ ماضی جملی است: از ماده مضارع ساخته شده است.

هراس + پهلوی اشکانی 21739 < ایرانی باستان ۵:392* + ۵73-9-8*. برای 2۵ >
آرای. ۶ برای ساختن مادهٌ آغازی به کار می‌رفته است. 073۳ صورت بالاندةٌ ریشه 17۳
است, با ابدال 1 به ۰0 ريشهٌ 1۳8 به معنی «ترسیدن» است» ۰28739 که از صورت بالاندهٌ
ريشةٌ 12 آمده به معنی «ترساندن» است. «ترسیدن) هم از 15 آمده است > ترسیدن.

هستن, استن

«هستن» و «استن» مصدرهایی هستند که برای «هستم»» «هستی) ... و (استم)»
«استی) ... فرض شده‌اند. این فرضی است نادرست» چون (>۵» از مادهٌ ماضی مصدر
می‌سازد. «هست» و «است» فعل مضارع سوم شخص مفرد هستند. از «بودن» -> بودن.

اگر قرار باشد برای «هستم»» (هستی» ... و (استم»» (أستی» ... مصدری فرض شودء
باید آن‌را به صورتهای «هستیدن) و («استیدنٌ) فرض کردء یعنی «هست» و (است» را
مادهٌ مضارع فرض کنیم و از آنها با «ید» مادهٌ ماضی بسازیم و به آن ماده‌های ماضی
«>0) را بیفز
=== pdf 87

فعلهای فارسی دری
یافتن
یافت < فارسی میانه 27311 < ایرانی باستان ۵1-3۳4۵*. برای 12 > آراست. 21
: پیشوند فعلی است. ريشةٌ 22 به معنی «به دس تآوردن» است.
یاب < فارسی میانه 2730 < ایرانی باستان ۵01-30-8*. برای 2 -> آرای.
بشترد
پشت + فارسی میانه 181 < ایرانی باستان 9۵3-12*. برای 12 -» آراست. 7صورت
اصلی 28 است. * پیش از ۲ به 5 بدل شده است. ريشهٌ 727 به معنی «ستودن» است,
«یشتن» از واژه‌های «زند و پازند» است. مادةٌ مضارع آن در فارسی میانه 22 است»
از ایرانی باستان 922-8. برای 2 + آرای,
```


## [2026-09-06T22:22:38.774Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nd=open('incoming/FFD/FFD_pages.txt',encoding='utf-8',errors='replace').read()\nparts=re.split(r'\\[pdf page (\\d+)\\]', d)\npages={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}\nfor p in (72,73,74):\n    print('=== pdf',p,'printed',p-5); print(pages.get(p,'')[:1500]); print()\nEOF"
}
```


### [2026-09-06T22:22:40.417Z] TOOL RESULT

```
=== pdf 72 printed 67

ماده‌های ماضی و مضارع قاری دری سس ۶۷
۴1۳-4۵ برای 1۵ > آراست. 2۵ پیشوند فعلی است. ۹38 صورت اصلی 83 است. 8
پیش از 1به #بدل شده است. ۹88 صورت ضعیف ريشةٌ ۹228 است. «برای ضعیف کردن
ريشه حذف شده است. 5288 به معنی «کشیدن» است.
فرهنج ج فارسی میانه [112822 < فارسی باستان 8-[0۵0 -8۵* < ایرانی باستان
2-[172-8۵2*. برای 2 - آرای. [به جای 8 آمده است. + آهختن.
«آهنگ» و «فرهنگ» هم از ريشةٌ 988 گرفته شده‌اندء به شرح زبر:
آهنگ + فارسی میانه 30228 < فارسی باستان 0208-8 -3* < ایرانی باستان
۶3-8288-2. 3 پیشوند و 2 پسوند است.
فرهنگ < فارسی میانه 13022 < فارسی باستان 0۵88-8 -8۸* < ایرانی باستان
۳۵-۵28۵
۱ فریفتن
فریفت < فارسی میانه 17211 < ایرانی باستان ۳2۵-427-1۵]*. برای 18 > آراست. 18
پیشوند فعلی است. 420 صورت اصلی ريشه است. پیش از 1 به ؟ بدل شده است. ريشهٌ
0 به معنی «فریفتن) است.
فریپ < فارسی میانه 1۳80 < ایرانی باستان 18-420-2*. برای ۵ -> آرای.
کاستن
کاست < ایرانی باستان 1:39-12*. برای ۵) -> آراست. 139 صورت بالاندةٌ ريشه 1۵5
است به معنی «کوچک بودن». صورت بالانده در معنی واداری به کار رفته است» به معنی
«ک و چککردن».
کاه « فارسی میانه 13 < ایرانی باستان 139-۵*. برای 2 - آرای.
کاشتن
کاشت < ایرانی باستان 37-5-12 *. برای 1۵ -> آراست. 837 صورت بالاندةٌ ريشة 1۵7
به معنی «زراعت کردن» است. 5 برای ساختن ريشهٌ جدید از ريشه به کار می‌رفته است.


=== pdf 73 printed 68

0 فارسی درق
کار + فارسی میانه 3 < ایرانی باستان ۸37-۵*. برای 2 -> آرای.
«کشت» مادةٌ ماضی دیگر است برای «کار» از فارسی میانةٌ 151 < ایرانی باستان
۵ا-65ا*. 1 صورت ضعیف ريشةٌ 1۵7 است.
کافتن
کافت + فارسی میانه 1311 + ایرانی باستان ۸3-1۵*. برای 18 -> آراست. 131 صورت
بالاندهٌ ریش 81 به معنی «شکاقتن» است.
کاو +کاف < فارسی میانه 13۶ < ایرانی باستان ۴32*. برای 2 -> آرای.
« کفت»» که مادهٌ مضارع آن «کف» است. از ريشةٌ ۵ به معنی «شکافتن» آمده است.
به شرح زیر
کفت « ایرانی باستان 1۵1-1۵* کف « ایرانی باستان 1۵1-8*.
«کفتن»در فارسی دری هم لازم و هم متعدی به‌کار رفته‌است. در شاهنامه آمده است:
نیامد جز احستتشان بهره‌ام
بکفت اندر احسنتشان زهره‌ام
کامستن
کامست < فارسی میانه 1300191 1370181 مادةٌ ماضی جعلی است. از مادهٌ مضارع
ساخته شده است.
کام « فارسی میانه 2/0 « ایرانی باستان 28*. 8308* در ایرانی باستان اسم
است که به عنوان مادهٌ مضارع به کار رفته است.
کردن :
کرد (به کسر و فتح اول) + فارسی میانه 876 و ۴۵۲۵ < ایرانی باستان 7-1۵* و
۵۶-۵*. برای 4۵ آراست. 7 صورت ضعیف ريشهٌ ۵7 به معنی «کردن» است.
کن + فارسی میانه 18 < فارسی باستان ۴۵۵ < ایرانی باستان ۴17-۵۷ 7 به ۵
بدل شده است. 24۷ برای ساختن ماده از ريشه به کار می‌رفته است.


=== pdf 74 printed 69

ماده‌های ماضی و مضارع فارسی دری شش و۶۱
اک کت
+کاشتن
کف
کشت + فارسی میانه 1934 + ایرانی باستان ۴*10۵5-12. برای 18 > آراست.
کش < فارسی میاته 1005 < ایرانی باستان 10۵3-۵*. برای 2- آرای. ریشهٌ 63 به معنی
«نبرد کردن» است. «کوشیدن» هم از ریشةٌ 05 آمده است.
کشفت.
کشفت < فارسی میانه ۷1811 < ایرانی باستان ۷807-1۵" برای 18 ->آراست. ۷:1
پیشوند فعلی است. 00ا75صورت اصلی ريشةٌ ۶ا3«است» پیش از 1به 1 بدل شده است.
0 صورت ضعیف ريشهٌ 35200 است. ريشهٌ 5200*به معنی «لرزیدن» است. «آشفتن)
هم از ریشة 5200 آمده است > آشفتن.
10 ماده مضارع 02 است. به این قیاس ماده مضارع «کشفتن» باید به
صورت «کشوب» می‌آمد.
1 فارسی میانه در فارسی دری به «گٌ» بدل شده است. کشفتن باید باگاف می آمد.
اما با «ش» هم‌جنس شده و کاف به جای گاف آمده است.
کشیدن
کشید ج فارسی میانه 570ن۴. [ ۱ مادهماضی جعلی است. از مادهٌ مضارع ساخته شده
است.
کش < فارسی میانه #58 < ایرانی باستان ۷,5-۵*. برای 2 > آرای. ريشةٌ 88 که
صورت افزودهٌ آن 1815 است» «کشیدن» معنی می‌دهد.
ی
+کافتن
کندن
: َ * آراست. ريشةٌ 1۵
کند + فارسی میاته 1۵8۵4 < ایرانی باستان ۵0-۵ *.برای 18+ اراست. ريشه 180 به
معنی کندد است.
```


## [2026-09-06T22:22:50.644Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la MON_part*.txt && python3 - <<'EOF'\nfor f in ('MON_part1.txt','MON_part2.txt'):\n    d=open(f,encoding='utf-8',errors='replace').read()\n    print(f, 'len',len(d), 'ff',d.count('\\f'))\n    print(d[:400])\nEOF"
}
```


### [2026-09-06T22:22:52.660Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
MON_part1.txt len 2611770 ff 0
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
و ده ها وی مزا موی ماما میو و موه ومد
MON_part2.txt len 2568024 ff 0
معین» محمد» ۱۲۹۱ ۱۳۵۰. 


۰ 
۳ 


فرهنگ معین / محمد معین. -- تهران: آدنا: کتاب راه نو ۰۱۲۸۱ 


۲ج 
(دوره) :964-7252-51-2 :158 
(ج.۲) 964-7252-53-6 :158۷ (ج.۱) 964-7252-52-8 :5۳81] 
فهر ستنویسی بر اساس اطلاعات فیپا. 
۱. فارسی -- واژه‌نامه‌ها. الف. عنوان. 
۴۵ف ۲۹۵۴/۸۷ ۳112 ۳ فا ۴ 
۱۳۸۱ 
کتابخانه ملی ایران ۷۹۵ - ۸۱م 


انتشارات آدنا 
فر هنگ دوجلدی معین 
گردآورنده عزیزالته علیزاده 
نوبت چاپ سوم: ۸۳ 
ت
```


## [2026-09-06T22:23:01.791Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f in ('MON_part1.txt','MON_part2.txt'):\n    d=open(f,encoding='utf-8',errors='replace').read()\n    for w in ['شکار','گوارش','پیکار','پیکر']:\n        for m in re.finditer(w+r'\\b', d):\n            seg=d[m.start()-60:m.start()+260]\n            if 'پهلوی' in seg or 'اوستا' in seg or 'باستان' in seg:\n                print('##',f,w); print(seg.replace('\\n',' ')); print()\n                break\nEOF"
}
```


### [2026-09-06T22:23:03.682Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T22:23:10.543Z] TOOL CALL #76: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7er-",
 "prompt": "Give the reconstruction, meaning, Pokorny page, and the descendants (Proto-Indo-Iranian *kar-, Sanskrit karoti, Avestan, Old Persian) for PIE *kʷer-."
}
```


## [2026-09-06T22:23:13.537Z] TOOL CALL #77: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DB%8C%D8%B2%D8%AF%DA%AF%D8%B1%D8%AF",
 "prompt": "Give the etymology of the Persian name یزدگرد (Yazdegerd/Yazdgerd): Middle Persian form, the elements yazd \"god\" + kard/kirt \"made\", and the meaning (\"made by God\")."
}
```


### [2026-09-06T22:23:15.522Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T22:23:16.247Z] TOOL RESULT

```
# PIE *kʷer- Summary

**Reconstruction:** *kʷer- (perfective root)

**Meaning:** The original meaning is reconstructed as "to carve, to shape by cutting" based on Anatolian forms. The root also means "to do," "to make," "to build," and can denote "bowl" or "vessel."

**Descendants:**

- **Proto-Indo-Iranian:** *kar-
  - **Sanskrit:** karoti (does, makes)
  - **Avestan:** cāxrarə (3pl.perf., "has made")
  - **Old Persian:** caxriyā (3sg.perf.opt.)

The page does not provide a specific Pokorny page number in the visible content, though it references scholarly sources on Indo-European etymology and linguistics.
```


## [2026-09-06T22:23:19.740Z] TOOL CALL #78: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Yazdegerd",
 "prompt": "Give the etymology of Yazdegerd: Middle Persian Yazdegerd / Yazdkert, from Old Iranian *yazata-kṛta- \"made by God\" or \"created by God\". Quote the elements."
}
```


## [2026-09-06T22:23:21.846Z] TOOL CALL #79: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/-%DA%AF%D8%B1%D8%AF",
 "prompt": "Is there a Persian suffix -گرد (-gerd) meaning \"town, city\" in place names (Dastgerd, Borujerd)? Give its etymology (Middle Persian -kard/-kirt, Old Persian *kṛta- \"made\")."
}
```


### [2026-09-06T22:23:23.745Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T22:23:25.616Z] TOOL RESULT

```
# Etymology of Yazdegerd

Based on the Wiktionary content, Yazdegerd derives from Middle Persian sources with the following breakdown:

**Root composition:** The name combines two elements: "Yazd" + "-gird" (or "-kirt").

**Literal meaning:** According to the source, the name translates to **"made by God."**

**Original forms:** The entry indicates the Middle Persian forms as 𐭩𐭦𐭣𐭪𐭥𐭲𐭩 (Yazdegerd, Yazdgird), which the dictionary describes as coming from Old Iranian roots.

The document states the etymology as: *"From [Middle Persian] Yazdegerd, Yazdgird, literally 'made by God', from Yazd + -gird, -kirt."* This reflects a theophoric name structure common in Persian royal nomenclature, where divine creation or authorization is invoked through the naming convention.
```


## [2026-09-06T22:23:44.811Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"iškar\\|iskar\\|aiwiS\\|aiwiš\\|aiwi\\.s\" BRT.txt | head -20; echo \"=== KNT patikara/karta ===\"; grep -n \"patikara\\|kṛta\\|karta-\" KNT.txt | head -15"
}
```


### [2026-09-06T22:23:44.868Z] TOOL RESULT

```
2476:—  inVerbindung  mit  x^'aFpat^j'a-.  Aaxaji5 Im  einem  Satz,  der  einem  vorhergehenden ..  kudaena  naiuaUt  mPiö.ao]anhd  (sd.)  Relativsatz  inhaltlich  koordinirt  ist '*': /ru- aesqm  sfaSfaHya  hizvöXt.ig.^^.  2)  auf.  zaiiUlmca  .  .  ytri/id  pourBsca  b»r3jayan ein  Relativum  als  dessen  Korrelat;  a)  ad- 1  nagciica  aiAka  yasäiti  zyänsi  (sd)  Y.  65. jektivisch  (vgl  i  aa) ;  yi  ätnm  . .  ava.-  11;  —  dämSH  urvalsl  .  .  yahmi  sp>ntä baraiti  . .  cvat  ahmäi  natre  mTsd»m  anhat  ^wil  mainyS  urvaisi  jasö  (sd.)  mazdä V.cV.81.  a)  Das  adjekt  Pron.  vertritt  |  :e/flir,7  oAmJ  W:4ä  »H7«aw,4fl  "bei  welchem laL  eius,  eorum  (s.  i  a  a):  yö  mam  .  ,  Ende  du  mit  .  .,  o  M.,  mit  XL,  bei  dem zinät  nöil  ahmi  nmäne  *z3naile  a^rava..'  du  mit  VM.  kommen  wirst"  Y.  4J.6{.;  — aal  ahmi  nmäne  .  .  "wer  .  .,  in  dessen  s.  noch  ahmya  3.  3)  Das  Neutr.  oder Hause  .  .,  sondern  in  seinem  Haus  , ."  Fem.  Sing,  bezieht  sich  substantivisch  auf Y. //.5f.;  —  mit  Numeruswechsel  "> :  _>'ö..  den  Inhalt  eines  Satzes,  bes.  Vordersatzes haom»nvandaita..frä..abyötanubyökaom5  (s.  Z  4);  a)  GSn. 'dess'  sva.  'dafür':  yatba- visäite  (sd)  baliazäi  "quilibet . .  laudat, . .  ■  väni  aiwi.sasto  .  .  eis  atiihe  asti  baSsazö eorum  corporibus  . ."  Y.  jo.  8.  b)  sub-  (sd.)  Yt7.^34;  —  AS  mim  ava>a  vjrj- stantivisch:  yi  maibyä  yaol  ahmäi  asSlt\nüiti  ya^a  ..  Sl  ait?he  asti  uzvar?z)m (sd.)   vahista  .  .    cöiüm  Y.  46.18;  19;  — j  (sd)  V-iS-^^f.;  37,  57,  68';  —  d:7tü  hi
3892:•  j.  aiwi.sravana-  Adj.,  PPM.:  s.  srav-. KompE.
3920:•  j.  aiwi.saetan- :  'sJi^n-'^  m,  'Bewohner'; ti  . .  aibis  {sA.)  tal  vaakSus  *''hni  (LS.)'> V.J.  24.
3941:•  j.  aiwiS.huta-  Adj.,  PPfP. :  s.  'hav-.
3942:•  j.  aiwiS-hutayae-iTfl  Inf.  '(und)  um  aus- zukeltern, durch  Keltern  zuzubereiten': aiw°  . .  ysi  hmti  haotna  Vr.5,3.
4298:•  j.  an-aiwi.sravana-  Adj.  'der  nicht unterrichtetwirdin— '  {?iiiiV..):äat yat  a>ihat anästatS  vil  °nö  vä  dalnam  mäzdayasnim aääiii . .  "aber  wenn  er  sich  dem  masd. Glauben  nicht  angelobt  hat  und  nicht darin  unterrichtet  wird,  so  . ."  V.  5.40.
7036:aahat  ästais  . .  ä°  yezi  aahaj  anäsiütS  . . V.^.40;  5.28-35",  7.13,  IS,  75',  ■^'■37, 99,  106;  —  yeüca  hz  anya  aya  fyao%na fravarita  .  .  ä'  yezi  //  .  .  rigij  fravarila Y.3.21;  Vd.2  aSt  ß)  yezi  .  .  aiwi.- srunvaili  .  .  yezi  J-  nsit  aiwi.surunvaiH N.  26;  60,  _jtV,  3Q,  iV(V,  g6,  100,  101, 104, 105,  54*>,  26  aSt.*',  (J5'>,  97S>; — yu  nBit öim  .  .  vääm  *aiwy<Is  . .  yezi  S°  öyum.pe väcim  *aiwyas  anaiwisH  (sd.)  .  .  N.  74; IQ.  4)  zur  Anknüpfung  eines  begrün- denden oder  erläuternden  Satzes  'denn; nämlich';  minyö  yö  parö.dari  .  ,  ä°  hS msrrfS  väcim  baraiti  Y.iS.i^;  —  sasta he  .  .  /rasnsoay^n  ä°  yat  he  zasta  mit framata  äat  (s.  7)  ,.  V.  1^.40;  —  mä  äi barg  (sd.)  agvS  yat  irisUm  ä°  yezi  sS  barai aivö ..  V.5.14.  5)  in  Säuen,  die  eine Aufforderung  oder  Wülensäusserung  ent- halten, 'so  .  .  denn',  oder  unübersetzbar: a°  mS  ahe  .  .  paräca  vaepaya  Y.  /o.  12; ra,  Yt5,77;  —  ä°  tum  ,.  nava  rnaya ni^wjnsöis  Y.iO.iS;  22.2,  9;  —  3°  vS kascil  .  .  isalta  Yt/5.53;  —  ä°  tbaHä taurvayeni  Yt. /4-4;  —  a° .  .yasami  Yt^. '3o>  131;  —  ä°  dis  avaioayamahi  Y. 4.aff.,  24.Z,  5.  55-^^  Yt.ii.i6,  ai;  ^.5, 11.31.  a)  hinter  dem  ersten  Wort  des Satzes:  imqm  ä'  sqm  .  .  yazamaidiY.^H. 1 ;  gg.  1 ,  a ;  —  alahya  a°  sairl  .  .  ädä (sd.)  Y.  JJ.8;  —  aZsmanqmat  3°  .  .  /ra- näsayata  A.  j,  s^  b)  in  anderer  Stellung: paoirlm  upa  may>m  haktrit  äpö  ä° kvqm  tanüm  pairtyaozdai'^Tia  V.p.31; 31.  6)  hinter  dem  Pron.  interrog.  wie
7262:atihat  äsfütS  . .  ä°  yezt  atihat  anastals  . . V.J.40;  5.28-35",  7.13,  15,  75',  ,V.37, 99,  106;  — yeiica  ht  anya  aya  syao%iia fravarsta  .  .  ä°  yeii  sl  .  .  nsit  fravarSta V.J. 21;  Vd.2  2 St  ß)  yezi  .  .  aiwt.- srunvaiti  .  .  yezi  ä°  nOii  aiwi.surunvaiti N.  26;  60,  jiS',  3g,  (V^i  g6,  100,  loi,  104, 105,  g4*\  26  2Sti>,  55S',  57S>; — yS  nöil dim  .  .  väcim  ^aiwyss  .  .  yezi  a°  öyum.pe väcitn  *aiwyäs  anaiwisti  (sd.)  .  ,  N, /4; 4)  zur  Anknüpfung  eines  begrün- denden oder  erläuternden  Satzes  'denn ; nämlich':  m?r»yö  yU  pard.darl  ,  .  ä'  AS msri^B  väcim  baraiti  V. /<?.  15;  —  zasta Jrasnäiaypn  ä'  yat  hl  zasta  nStt frasnäla  äat  (s.  7)  . .  V.  8.  40;  —  mS  ä/ barö  (sd,)  ams  yal  irist^m  ä°  yezi  si  barät flft^J. ,  V.J.  14.  5)  in  Sätzen,  die  eine
8686:•  j.  u§-  n.  'Ohr'  uzw.  «^»rischer  Wesen'': k/(NS.)  F.9(?).  A)  sonst  nur  Du.;  a)  'die Ohren':  yezi  *kva£ibya  ''-sibya''^^  aiwi.- srunvaifi  . ,  yezi  äat  nöit  /ivagibya  "Hbya aiwi.surunvait(  N.  i'ö";  Uj;  —  *'sibya F.p'>*>;  —  drimts  .  .  asi  [-//Is)  karma gava  *dvari'^ra  zafan  Yt  jr.2;  —  pairi 'si  vSrayavw»m  kam  gava  nidanzaydmoMii Yt.  j.  27;  —  g?tirvaya  h?  päoave  züvar^ pairi  iS  'si  zvrpnäioi  sk)Hd?m  si  manS kirsnüioi  Y.9.28;  —  °//  ahuralu  mazda yazamaide  darp'^räi  (sd.)  maiirahe  .  . xratüm  .  .  mar>%räi  .  .  hisvqm  . .  fra^'äküi Yt. /.  28.  a)  von  Tieren;  °H  (näml. g>us)  pairi. dar ayänli  (sd.)  daSma  .  .  Vt. 14. 56.  b)  'Gehör*,  d.  i.  Fähigkeit  richtig zu  hören  und  zu  verstehen,  sva.  'Auf- fassungs-,  Verstandeskraft':  ava  pa'oS  ava zastS  ava  °/i  däraydiiwjm  .  .  däityanqm .  . syaoiinanqm  varpzäi  Vr.  75.  1;  —  d<lya ml . .  mastim  spilnö  xsviwrjm  (sd.)  hizi'qm uruiie  -si  xratBiH  .  .  Y.62.4.
10324:—  yj  °iä(f  asravayö  *qsta  (sd.)  va  ,  . N.  4i\  4^—45^'^\'^y^*  *alte  maiXyanqm (sd.)  pars  x''arftöil  *°IJaJ'  nöif  srävayeiti N.  25;  —  yS  .  .  *aimm  dahm>m  '%anqm *sraoi!rat  pairistayeiti  N.  44.  A)  für die  einzelnen  Tagesabschnitte  {asnya-)  war das  Beten  bestimmter  Grf^^stücke  vorge- schrieben: .(■aiOTJi'  kaca  ulaAinanqm  "^a- nqin . .  * Aavaiiinqm  °'ianqm  . .  *rapi^wina' nqm  ''ianqm  .  .  uzayairinqm  '"hanqm  . . aiwi.srO^rimanqm  'ianqm  ratu/rii  fra- jasaitil  N.46—S1.
12426:—  yesi  ai^Aai  ästuts  vH  aiwi.sravand  vä •nqm  Y.J.  40;  40',  P.  14;  —  njfii  kl  qpa.- staväne  (sd.)  ,  .    'nqm  V.i^.-j;  6,  NT^^;
18685:—  yo  naire  mmanh^nte  nSit  mms(sd.) paUi.baraiti  Y.4.1;  *¥.4c"^;  —  yat bavani  (Sp,  930  m.)  aiwi.sastS  *'pouru *narqm  {btsyantam  Yt  14.  34;  V.  4. 5 ;  — yars  nars  x'a.ao'^raAe(sd.)  iva/ff  V.  5. 46 PiiZ,;j.4i;  —  yeAya  iiiauHsd.)  nä spmld  Y.  48.  7;  5/.  ii;  —  spgntaRyaca ni>rJs{GS.)  ..yehyä  ..  Y.34.2; —  *vaäm
21238:'modalen  Formen:  yaT  adaif  (sd.)  asa *drujim  vSngAaitT  Ay  ('so  dass')  '^qsasuia (sd.)  ya  ..Y.4S.\;  —  ka%a  iBt  gavBi ratul  hy  ('auf  dass')  AJm  data  xsayatttS (sd.)  %waxsB  Y.  25.  2;  —  a  *m3yastra.- barattä  (Sp.  1190  u.)  ,  ,  Ay  ('auf  dass') ^<iärJ(sd.)  mana  bava/Y.30.^; 32.i6(f); —  vax^a  vS . ,  Ay  ('damit')  d/ih^ng  (sd.) vicayaha  ad^qs^ä  Y,  46.  15;  —  asaonl rafonS  RySm  .  .  Ay  ('auf  dass')  *a  *basils (sd.)  .  .  dya  Y.43.S;  —  tat  ai  vairi- maidl  .  .  Ay  ('damit")  r  mainimadila  .  . ^■35- 3-  b)  im  jAw.;  i)  mit  Ind.:  tä Ai  taurvayatam  tba^a  .  .  y  ('so  dass') ^it  apB  takäis  stayat  Yt  y .  7  8 ;  —  x^anns .  .  yat  uparaAacat  AaoiyanApm  .  .  y  x/a- yata  .  .  dasvanqm  ma^anqmca  ".  .  so dass  er  herrschte  über  .  ."  Yt  ig.  26; 28f.3,  13,  79,  84,  Y.().4;  —  saya  ava%a staxrB  y  ha  druxl  oHti  tnfnzvT  .  .  FrW. 8.  2  (?).  a)  die  Antwort  auf  eine  Frage mit  ^anl'  einleitend  (s.  2  a,  3):  ^Ivata  (sd.) na  *mtima  vaca  gdha  sravayS  ratu/riil y  Ai  nasdiSiB  daAmH  aiwi.srunvai/i  ", .  so, dass  ihn . .  verstehen  kann"  N.  27.  a)  mit Konj.  (oder  Inj,):  y  ('damit')  yavB  (sd.) pouruS  bavät  oBa  mq%r3m  *tat  mairyai V._j.  32f.;  —  :farm3..yai  upawAaiat sao^antqm  Vfr^rajaram  .  .  y  hrmavai frasim  aAüm  ,  .  ". .  auf  dass  er  die Menschheit  neu  gestalte"  Yt/9.88f.;  11, 8.  I,  V.  ig.  23;  —  neben  ya%a'.  Jrsit  mB tat  nqma  /ramrUiti  .  .  ya%a  (Sp.  1 246 u.)  azsm  taurvayetti  . .  y  ('auf  dass')  mqtn nasHS  taurvayät  Yt.  i.  6;  —  th  mazdi zbayal  avanAe  .  .  y  ('damit')  spmtB mainyul  vfharayat  asmatum  y  ap)m y*  .  .  YLy.28;  —  mä  buyama  sSihrB,- iricö  ,  .  m^a  (sd.)  y  ('damit')  nS  uyra.- bäzaus  nivanai  (sd.)  Ytjo.  75;  —  kana 'hwqm  yasna  yazäne  .. yasp*^  ('auf  dass') tava  mazdi  kinnaot  tacara  .  .  yasi^^ ('damit')  äwa  nöit  aiwi.druiante  .  .  Yt 5. 90.  a)  wie  I  a:  h/at  aiwyätsAayanttl yat  aliqm  *3r)dvaya  (sd.)  . .  *v3r»^antqm ndit  avanrasayai  (sd.)  N.  85.  3)  mit Opt.;  wie  I  a:  cvantö  ata  Am  alle  kata  ..l ■  .  y°  Al  nsit  >r)dv5.hr3han3m  (sd.)  vayta- n»m  upa.janyatY .^.\\.  4)  dasVerbum i^aA')  ist  weggelassen:  spanim  nida%?m y  dim  mazaos  (sd.)  ksArpB  tarahe  V.  13. 39.  V)    einen   Inhaltssatz    einleitend
24411:N.  77,  *20,  70 ;  —  'palibyS  sastlm  baraiti älari  Y.  02. 7 ;  —  'paitbyS  haca  *izyeiti hubirftxm  Y.  ffs.  7;  —  'paHbyasca  patri acisiaHbyö  V.  74. 17;  Y, 57.  la;  —  mat 'psbyS  aSaonibyS  fravasibyS  Y.  24.5,  23. a';  —  'paiiqm  (GPm.)  yazatanqm  Y.  23. 27;  7. 14,  Yt  77.  7;  —  yi  . .  paiH.baraiti aoät  anye  ,  .  v^rpzftiii  °paisqm(GPTt.)ca aiwi.srunvaiti  vTspe  ratufryB  ".  .  und (alle)  hören  alles,  so  sind  alle  r"  N.  60;
25049:altallqm  '/rtl  ratufritimi^A.)  *'k:W3r»saitl ^■53i  5^i  ~~  o^^s  '/ris  yS  Jayära  N.  f*?; *24'\  ''6o*>;  —  yS  gi^anqm  anuniaitl (sd,)  ..  *anu.mainyeU  ..  *°fris  N.  25^'; 8g;  —  y3  yasmm  *yai>nii  (statt  Du.)  .  . ,.va  *'/rya  (ND,)"'  N.  24;  — yi  ga'iä  .. *sr3vayate  N^'a  •/'"'J'' (statt  ND.)  N.  2_j;  — yB  *hi!.hasir^m  srävayäti  '/ryl  (statt  NS.) N-^J;  8y; — yj  vastra  vastnm  aiuyaftha- yänti  .  .  'fryö  N.<;_j;  ^  yiha  kaiah dahmB  staefa  yesnya  Äauna  daoäiti ..ai:a °/rii  N._j7;  —  surunaoiti  *£aota  upa.- sraolaranqm  nsit  upasraotird  zaolarS zaota  'fril  N.  2/;  2;;  —  dahmS  saota dahmU  upa.iraotJrO  vlspe  'fryB  tanuparihS ioola  .  .  visfe  arahtfryd  N..?(J;  60;  — (_>>«/)  äat  ndii  ap3is'(sd.)  aSala  *ma%mya *vaca  framarfmnS  'frii  N.  26;  — yü  uri'a- rqm  /rast>r?nte  .  .  vliarS  fraväxiö  "fris N.pS;  *g8*'>,  gg';  —  *ä'a/a  (Sp.  600  m.) na  nittma  vaia  ga><l  srävayj  'frÜ  N.  27; —  kva  llcii  (%p.  ^1  $  n.)  gSus  .  .  paiti.- barö  *'/ris'a.  1081^ ;  108;  —  {cvai)  *na *nihma  vasirahe  (Sp.  1385  m.)  aiwyäsiö 'fril  N.  86;  *8y  5>,  8y,  106;  —  *frasravay5 'fril  nSil  *asrävayö  N,  104;  lOj;  —  ye:i *Ävaa'iya  *uSihya  aiwi.srunvmti  °fris  N. 26;  —  yezi  sl  äätti  daoäili  *'frii  . .  yai aat  hl  n5it  däiti  datäiti  araiu/riiü.io^; *ioo"\  loi',  55;  — yai  %rii  *ha%rän^o yltayanle  (sd.)  'fryB  yezi  aal  (^ri/)  itsit *Aa'ijräneB  yätayarUi  aratufryj  N.  88;  gi, 9^1  95<  97'!  —  ^^  •  ■  ai'wyäfthay^nti  yai .  .  uva  >/tyB  (statt  Du.)  N.p4;  —  yaldit (sd.)  alteframannti..  'fryB  N.  j3.  a)  mit Angabe  dessen,  wodurch  oder  wofür  man r.  ist  oder  wird  durch  a)  Instr.;  *sraohra *na  goianam  '/rii'paiti.asti(%d.ya  yasnahe N.  22;  —  hia^hya  *nä  nit>ma?ibya  Aäva- nalibya  *'frii'i>  N.  108;  90;  —  *alvayacii .  .  *harismSMir?iti  '/r:/ U.  103;  —  V/S- ranaHbya    'Jri!  *aywhainalibya  ,  ,   «:/V
25866:mit  aiwi  'im  Gedächtnis  behalten,  denken an  — '  (Akk.)  -.yat . .  airyh  datähävS  tUtryeht .,  aiwi.sacyilr?s  i^OA..')  äilitlm  yasntm  .. "wenn  . .  die  d/ischen  Länder  an  des TiÜ'ryfl  gebührende  Anbetung. .dächten,.." Yt.Äs6.
26633:mit  ä  'sündigen,  sich  versündigen,  in den  Zustand  der  Sündigkeit  geraten;  sündig sein,  sich  im  Zustand  der  Süodigkeit  be- finden', Akt  und  Med.;  i)  absolut:  vlsatti (sd.)  ainyS  "usyS  null  ainyS  ^vlsimnö *äsiryäte  ava  ^vJsalte  (sd.)  *na^a.cil ästryeite  (in  pass.  Sinn  'non  pcccatur') P,57;  —  ya%a  .  .  äai^y^t  a^a  äsfryati "als  ob  er  ,  ,  so  versündigt  er  sich"  V. y.  zo;  —  aetavalla  aesasctt  *ästryäli^^ "und  in  solchem  Mass  macht  auch  er sich  sündig"  N. /2(?);  —  yalöil  (sd)  .  . asrävays  hyat  a^a  .  .  ästryaÜ  ",  .  bleibt er  im  Zustand  der  Sündigkeit"  N.  44',  — *ntsriti  (sd.)  aitahe  ästryeiti  mit  *'anisrili N.  II.  a)  Kaus.  'sündig  machen,  in den  Zustand  der  Sündigkeit  versetzen':; tiöit  asavarum  ainisHs  (sd.)  ästärayeiti\ P.12;  —  nsit  *asavan»m  *a/n)j?('/ (sd.)  1 ättäraiti  N,  log;  —  nStt  sp.bint5 ..  nasus nar?m  ndil  *äslärayaii  V.  5.  3 ;  "•'Nik.  2 ;  — AiaJ  aUai^qm  lyaoi^nanqm  (als  Subj.) astaraiti  "in  welchem  Mass  macht  solches Tun  sündig?"  V.  13.  20;  4.  5;  —  aha  tai "ä/rimnS  astärayäti  N.  12  (P);  —  mä äa/a  . .  *asläraila  Vyt_37(?).  2)  mit a)  Abi.  oder  Gen.  dessen,  an  dem,  b)  Instr, oder  Akk.  (des  Inhalts)  dessen,  womit man  sich  versündigt:  mit  ästryeiti  anyS^ ahmst  yS  kl  ''gaväsiryavans  N.  18;  —  nsil astqm  .  .  pairi.spaiti  (sd.)  apqm  ästrySnte V.  o,  2  9 ;  —  nasujpaSm  (sd.)  . .  astryante . . apasla  zimasca  urvarayasca  V.  6'.  3 ;  — fiBtl  gähanq/n  asruiti  ästryäti  N._50;  — yai  . .  anaiwiSfi  (sd.)  ästryäti  N.  i4\  ^4,
27283:•  j.  sraosä-varaz-  m.  Name  des  siebenten und  geringsten,  mit  der  Kirchenpolizei (s.  No.  2)  betrauten  Unterpriesters  (ratav-); auch  die  Kirchenzucht  liegt  ihm  ob:  *>d'> aiwySxiayai  "der  Sr.  soll  die  Aufsicht fuhren"  N.  Tj''*;  —  *anaiwi.?r?fvB^aiit (sd.)  aSa  abfrtta  *'ta  (ND,)^'  vlcarayattm N.  7p;  —  . .  paoiryS  . .  hävanatum  (sd) . . BstayHH  . .  hapla%3m  'um  N.  tfe;  —  'am Sstäya  Vr.^.i;  0.3.$;  —  rai^wiskare va  •«  vH  V.5.  57;  58;  —  a<):aB  ralui aoxtB  'zB^^  ä^qin  frä^wtrfsaiti  ". .  be- stimmt die  Strafe"  V.  7. 71*';  5.16;  —  'tahe Vyt  15.  a)  vom  Hahn,  der  als  'BUttel' des  Sraosa  gilt,  weil  er  die  Menschen aufweckt  und  so  zur  Erfüllung  ihrer  FSicht antreibt:  kB  asti  sraosahe  a^ehe  ..  '«J'V m?r>yB  yS  parö.dars  nqma  V.  7Ä  1 4  C
27349:mit  aiwi^"»^  i) 'hören,  verstehen';  a)  ohne Obj.:  yai  *kvaäbya  *usibya  aiwüsrun- vaiti"^ ,.  yai  Hat  nsij..aiwi.surunvaiti"'^ N.  26;  —  af/^  ratufril yü  nsit  aiwi*srun- vaiti'"^"^  a.24.  b)  mit  Gen.  obj.: yü  aivd . .  a^HJ  anye . .  vTspalsqmca  aiwi.- srunvaili  (statt  Plur.)  vXspe  ratu/ryS  yesi äat  nüit  aiwijrunvanti  alsS  ^ratufrii  yS .. "wenn  einer  . .  und  die  andern  . .  und (alle)  hören  alles  (von  einander),  so  sind alle  r.  Wenn  sie  aber  nicht  (alle  alles)  hören, ist  nur  der  r.,  welcher . ."  N.  60.  a)  'unter- richtet werden,  Unterricht  empfangen  in  — ' (Akk.):  yesi  anhat  ästütö  va  aiwi.sra- vanS  v3  dalnqm  mäzäayamJm  "sofern  er sich  der  masdayasn.  Religion  angelobt hat  oder  darin  Unterricht  empfängt"  V, 3-  40-
28178:—  anijai/i  zi..  ali'a  asff.itGiti/ . .  H.i.  5; V.5,42;  —  in  unrcgelmässiger  Stellung": ^wä paiti  zt  Aaxxnm  (sd.)  daiüe  vaAisttm Yt.  10.  80.  a)  im  Nachsatz:  yasca tili  tiiyas^a  sadirra  frabaral  dazat  si mqm  . .  P.  22;  —  yat  ^riilm  dali'ayasnd hnntat  ava  AB  miryjite  anamätö  sf  al^S ^■7-ZTy  39;  —  y^  anAat  ä'^rava  frä zl  dvqsaiti  .  ,  druxl  V.  5.  aS;  —  y&i  zl (s.  Anh.  2)  azim  nSil  daioyqm . .  tiärim . . AamaAe  zl  ml  iha  ayqn  .  .pairika  .  .parlit pairiirt>m(sd.)a»AvqmavaMsiiyst..ti/tryB zl  (zu  I ) . .  avqm  pairikqm  adanzayeiti  Yt ^■5*~SS-  S.  noch  Anhang.  Anhang. 3l  hinter  Konjunktionen;  nur  b)  im  jAw.; i)  yat  zi;  zu  i:  yai  zi . .  airyä  datrihävö tistryeAe . .  aiwi.sacyar)s  daitim  yasmmca . . mit  . .  Yt.  8.  56.  2)  y^i  zi,  yetU  zi (Sp.  i239f.);  zu  I):  azfm  datqm  ..  asS ramS.daitlm  (sd.) .  .yeuti  si, ,  nlit  daioyqm ..vispB  anhuS . .  airyamm  vaijS  fräsm-St V./.i;  Y.7/.is,Yt.Ä52,/j.i2;  — zu*)' yeßti  zi  mä  masyaka  .  .  yazayanta  .  .  ari mqm  az-i.baioryqm  dasanqm  aspanqm  aojs YiS.74;  II,  ff.*3,  /o.sS,'74-  gAw.  at zi  und  'yezl  sbcs.
=== KNT patikara/karta ===
1689:‚ү. Final m of the prior element was of course not written before an initial eonsonant of the second part: ha™-gmatd, ha"-karta-, ha"-dugà, but ham-aranam. ha™-taxSatavy, but ham-atax Sala.
1902:asa-bdra- ‘borne by horses’; uša-bart- ‘borne by camels’; [dasta]karta- ‘done by hand’.
2620:I. The participial suffix -lo- is accented, and the Ж verbal root is therefore regularly in the zero grade: $ thus para-ità, Skt. itd-, to ay- ‘go’; [phištā ni-pitta-, $ Skt. pistd-, to pai- ‘adorn’; sinuta- to zšnav-; a- $ тфай, Skt. kgala-, to zšan-; ava-jata, Skt. hatd-,to 4 jan-, karta-, Skt. kytd-, to kar-; u-barta- pard- 4 ратат, Skt. bhriá-, to bar-; maria-, Skt. mytd-, to Г | mar-; aría-, Skt. rtd-, to ar-; perhaps parta[m] to `
4917:! a- neg. prefix before consonants (867, 67.1, 0182.1; an- antevocalie, q.v.): Av. Skt. a-, Gk. a~, Lt. ?n-, Сте. un-, pIE *n-. See akarta-, ax áaina-, axsata-, Anümaka-, ayaumani-.
4940:akarta- adj. ‘not made, not built, unrepaired’; neg. a- + pte. of kar- ‘make’. {akarta] nsf. DSe 47 (conj. of Kent, JAOS 54.43).
5252:karonaoitt, Skt. kr-, pres. krndti karóti (809, $122, $132.2, 5182.3). See also akarta-, ucára-, kara-, dastakarta-, duskarta-, hakarta-.
5277:kara- sb. ‘doer, maker’, as 2d element of cpd.: deriv. of kar- ($82, §143.1); found in avükara-, ciyükara-, düraniyakara-, zürakara-,  hakara-, hamaranakara-, and with passive meaning, 'thing made’, in patikara- (cf. Bv. Gr. $289).
5537:dasta- sb. ‘hand’: Av. zasta-, N Pers. 0051, Skt. hdsta-, pIE *ghosto- (§88, $116, $145). See also dastakarta-. даѕіауа ism. DR 4.35. dastaibiya idm. (§189) DNb 41.
5538:dastakarta- adj. ‘handmade’: dasta- + pte. .
5539:karta- (5160.10), to kar- ‘make’. [dasta|kartam (restored after the Elam., Wb. ZDMG 91.85, Hz. Ap! 136-8) nsn. as sb. ‘handiwork’, DSe 42.
5572:duš- insep. prefix ʻi: Av. dui-, Skt. dus-, Gk. dve- ($76.Ш); in dušiyāra-, duskarta-.
5574:| du$karia- ad). ‘ill-done’, opposite of naiba- (Hz. ApI 1434): duš- + karta- ‘done, made’, past pte. pass. tokar-. duskartam nsn. DSe 31f; XPh 42. draug- vb., see duruj- and draujiya-.
5584:placing GAv. vahu- ‘good’, and opposite of duš- karta- (Hz. AMI 8.68, ApI 266-7): NPers. nē ‘brave, good’ ($11, §75.V, $148.11). пафа nsf. DPd 8. naibam nsn. XPa 13, 16; XPg 4; XV 20. naibam asn. DSe 32°; DSi 4^; DSp 2f°; XPh 43.
5632:patikara- sb. ‘picture, (sculptured) likeness’: .
5637:kar- ($143.V). patikaram asm. DSn 1°. palikara apm. DB 4.71, 78, 77; DNa 41.
```


## [2026-09-06T22:23:56.028Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nd=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nparts=re.split(r'\\[pdf page (\\d+)\\]', d)\npages={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)} if len(parts)>1 else None\nif pages is None:\n    pages={i:p for i,p in enumerate(d.split('\\f'))}\nprint(len(pages))\nfor p,t in pages.items():\n    if 'camati' in t or 'cämati' in t or 'schlürfen, schlucken' in t:\n        print('page',p); \n        i=max(t.find('camati'),t.find('cämati'))\n        print(t[max(0,i-800):i+600]); break\nEOF"
}
```


### [2026-09-06T22:23:57.667Z] TOOL RESULT

```
895
page 522
                          i                                                                              n



514                                                                  q“em — quel-

                                                        11
q'Aeni „schliirfen, schlucken                                .




        camati und camati „schliirft“, u-camati „schliirft (Wasser) ein, spiilt
      Ai.
sich den Mund aus“, ptc. dcanta-, camasd-h „Trinkschale, Becher“, cumu-h
„Schussel ‘; np. rant „das Essen 11 cnmtdan „trinken“, osset. cunnin „sch]iirfen“;
                                                                 ,
                              *
nisi, hvima (aus *hvnma, idg. q't.cmu = ai. camati) „verschlucken, verschlingen
                                                                                11
```


## [2026-09-06T22:24:03.821Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nd=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nparts=re.split(r'\\[pdf page (\\d+)\\]', d)\npages={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}\nfor p in (525,526):\n    t=pages[p]\n    print('== pdf',p); print(t[:2200])\nEOF"
}
```


### [2026-09-06T22:24:05.548Z] TOOL RESULT

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
KeyError: 525
```


## [2026-09-06T22:24:08.619Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nd=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npages={i:p for i,p in enumerate(d.split('\\f'))}\nfor p in (525,526):\n    t=pages[p]\n    print('== leaf',p); print(t[:2300])\nEOF"
}
```


### [2026-09-06T22:24:10.212Z] TOOL RESULT

```
== leaf 525
                  o   ;                          l




                                              q“el     q°er-                                                 517

                                                                                                    2
2.   qjel- „fern (ortlich und zeitlich)" in:
     Ai.   caramd- „der        letzte,     auberste", cirds „lang (zeitlich)", gr. r fjks, aol.
nfjkvi „fern, weit" (r rjXo-'&ev, -ih, -ae), nalai „langst“(
                                                             naXaiog „alt“, nalai-
               cymr. corn. bret. pel „fern“ (s. dazu Pedersen KG. I 128, 4S1,
r egos, -ratos),
Morris- Jones WelshGr. 127, 137, unter einer Gdf. q'iel-s-o-'t), cymr. pellaf „der
aufierste". Anreihung auch von lat. procitl (Lit. bei Yf. LEWb.          s. v.) be-

kampft Curtius 490 damit, dab an der Bed. von procul die Praep. den
Hauptanteil habe, doch ware Yerstarkung eines zu kurz gewordenen *quel,
*col (etwa aus *q'ide gr. rfjke) dureh Yortritt von pro nicbt undenkbar,
                                :




und ist die Deutung aus *proco-lo-s (Brugmann IP. 27, 248), Demin, eines
*proco-s „vorwarts gewendet" wenigstens nicbt ganz sicber (Hartmann
Gl. 4, 365).


3. q“el-    „Schwarm, Schar, Sippe“.
   Ai. kiila-m „Herde, Schwarm, Menge; Gescblecht, Familie"; -t(o)-Bildung
(vgl. lit. Jceltis) vielleicht in Jcutumba-m „Hausstand, Hauswesen, Gesinde,
Familie" (?; Petersson IF. 34, 226; nicbt iiberzeugend reibt derselbe Fran
filol. foreningen i Lund, Sprakl. uppsatser IV 1 20 f. auch     ai. kalatra-m

„Ehefrau“ an)
  Gr. re los n. „Schar“; aksl. celjadb „Gesinde“, Kollektiv zu dem in celo-
vekb „Mensch“ vorliegenden celo- (siehe Berneker 141, Brugmann Festgabe
f. Kaegi  33: iiber koleno „Stamm, Geschlecht = Knie, *Glied“ siehe Ber-
neker 545 f.).
   Vgl. Fick BB. 8, 331    16, 282, Bezz. BB. 16, 245, Fick Wb. I* 26, 286 f.
                                     ;


(mit fernzuhaltendem,               z.   B. dor. aneXXa).      Ob hierher ags. sceolu, as. scola
„Schar“ (Ehrismann PBrB. 20, 63) als s-Dublette?? Air. eland „Nach-
kommenschaft, Kinder, Familie, Clan“, cymr. plant „Kinder“ (Fick II 4 63 f.)
ist vielmehr          =
               air. eland „planta“, Lw. aus lat. planta (Thurneysen Hdb.

520, 522, Pedersen KG.
== leaf 526
                                                                                        ;                      ;




518                                              q“er-



Bed. zu vereinen; „aspeetus coeli“??), mir. creth „Diehtung“                           (q’irto-),     cymr.
pryda „dichten“, prydydd           ..Dichter".

  Lit. kuriii, kiirti „bauen“, apr. kara „erbaute“ ksl. knciji, gen. -ije „Scbmied“
                                                               ;



(wie ai. karmdra-li ), russ. korciji ds. (Abl. von *lwtcb, s. Berneker 671 ).
  Fick I 4 24, 384, Osthoff Par. I 1 ff. m. Lit., Yf. LEWb.
                                                                              2
                                                                                  u. corpus-,       ob hier-
her qrep- „Leib"??
  Hierber mit der Bed. „es jemandem antun, verhexen“, auch ai. hr tyd
(„Handlung, Tat“ und :) „Behexung, Zauber" u. dgl., lit. keriii, kereti „je-
manden durch bosen Blick oder durch Worte bezaubern, verrufen, in der
Gesundheit scliadigen", heras „Zauber“, slav. cam „Zauber“ in abg. caro-
dcjb „Zauberer“, cari f. pi. „Zauber, Reiz“ usw. (Osthoff BB. 24, 109 ff.,
Par. I 26, Berneker 136 mit Bed.-Parallelen, Trautmann Bsl. Wb. 127):
Osthoff, Arch. f. Rel.-Wiss. 8, 5 Iff. will auch gr. reoag ,,Wunderzeichen“,
TieXcoQ ,,ubernatiirlich groBes Ungetiim. Ungeheuer“, rei.mgiog yeyag, ne-
                                        :                                                   •



Icngiog Hes. anreihen, sowie mit anl. s- ivgl. ai. sr-slar-) ai. a-gcarya-h
,,seltsam, wunderbar", n. „seltsame Erscheinung, Wunder", aisl. skars n.
„ein  Ungeheuer; Riesin", sl.ersa f. „Riesenweib, Riesin“, sky rsc n. ,,'iibles)
Yorzeichen, Phantom", (welcbe die suffixale Schwundstufe des es-St. regag
enthielten)  (sk- statt skw- von skyrse aus verallgemeinert?)
                  ;




      fur   tf'gag    (das scbon Hirt       BB. 24, 255, 261, Abl. 77 mit lit. kereti unter
q«ere- verknupfte) sucbt Stokes KZ. 40, 250 anderweitigen AnschluB an mir.
tomthar n. pl. torathuir „monstrous births" i? /o-Praefix? und zu ro-ratha
             ,


„wurden gegeben", ro-lr „er gewahrte" usw., s. per- „verkaufen“ mit der
Bed. von per- „gebaren,"? als Gdf. *to-ro-tro-l).
   Wolil nicht h
```


## [2026-09-06T22:24:25.689Z] TOOL CALL #84: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/%D8%B4%DA%A9%D8%A7%D8%B1' \\\n 'https://en.wiktionary.org/wiki/%D9%82%D9%87%D8%B1%D9%85%D8%A7%D9%86' \\\n 'https://en.wiktionary.org/wiki/%D9%84%D8%A7%D8%AC%D9%88%D8%B1%D8%AF' \\\n 'https://en.wiktionary.org/wiki/%D9%BE%DB%8C%DA%A9%D8%B1' \\\n 'https://en.wiktionary.org/wiki/%D9%BE%DB%8C%DA%A9%D8%A7%D8%B1' \\\n 'https://en.wiktionary.org/wiki/%D8%B4%D8%A7%DA%AF%D8%B1%D8%AF' \\\n 'https://en.wiktionary.org/wiki/%DA%A9%D8%A7%D9%85' \\\n 'https://en.wiktionary.org/wiki/%DA%86%D9%85%DB%8C%D8%AF%D9%86' \\\n 'https://en.wiktionary.org/wiki/%D9%BE%D8%B1%DA%AF%D8%A7%D8%B1' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7er-' \\\n 'https://en.wiktionary.org/wiki/Yazdegerd' ; do\n python3 tools/fetch_source.py \"$u\" --note 'pdf page 292 (book 262), roots Kwen 2 / Kwer: verification of Persian and Iranian nodes' 2>&1 | tail -2\ndone"
}
```


### [2026-09-06T22:24:31.128Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/12208715571d13ee.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/140772a23fab87d4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/99fe23bd844c35b4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f5093977aaf0d949.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/46b4d3d00c0ad1c8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3ffce5baf57682b7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f6e00d566642fe24.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f8822b4cf0fd9706.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cd18e066f58697b8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/05ebe20cc6379e2e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8417aa345e189e6a.txt
```


## [2026-09-06T22:24:36.323Z] TOOL CALL #85: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg292.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/292.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -5"
}
```


### [2026-09-06T22:24:36.393Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  90918 Sep  5 10:16 92.png
-rw-rw-r--  1 sfmqrb sfmqrb  93420 Sep  5 10:18 94.png
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-06T22:25:11.506Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"sikar\\|sikär\\|Sikär\\|Jagd\" HRN.txt | head -10; echo \"=== BRT Jagd/hunt kar ===\"; grep -n \"aiwi\\.kar\\|aibi\\.kar\\|škara\\|skära\\|skar-\" BRT.txt | head -10; echo \"=== WLD Gaumen ===\"; python3 -c \"\nd=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npages=d.split(chr(12))\nt=pages[522]\ni=t.find('Gaumen'); print(t[max(0,i-700):i+500] if i>=0 else 'no Gaumen'); print('----'); print(t[:1500])\n\""
}
```


### [2026-09-06T22:25:13.218Z] TOOL RESULT

```
2325:224. biSgerd *Jagd' etc.
3769:Hund, Jagdhund'.
4916:Jagd' gehört nicht zu np. bese — es bliebe also nur
6462:742. sekär, sikar^ sukar 'Kohle'.
6854:786. sikär *Jagd', vergl. hisgerd (No. 224), sikerden, sekere,
6855:iskere 'Jagdhabicht'.
9743:- 1129. yöz *Jagdleopard' (Vis und Kamin, Seite 40 Vers 12'^).
9758:kurd. LW. yilz 'kleiner Jagdhund* (H.-Sch.); arm.
9760:Ursprünglich als Jagdtier *der Sucher (de Lagarde,
=== BRT Jagd/hunt kar ===
26468:Eig.  'gekrümmt,  gedreht',  ITfP.;  %.  skärayat.- ™3o-.  Vgl.  PDw.  ;iiw-r^ 'gekrümmt',  gr.  n^arysa; Bthl.  IF.  10.  199.  —  Pü.  i  girl.
=== WLD Gaumen ===
                                                 ,
                              *
nisi, hvima (aus *hvnma, idg. q't.cmu = ai. camati) „verschlucken, verschlingen
                                                                                11
                                                                                                                                              ,



hvOma f. „Speiserohre, Schlund“; arm. khim-lh pi. „faux, guttur                                                            11
                                                                                                                                              :




mit Ablautstufe <7, npers. i:am „Gaumen“, afgban. kumai ds. Liden Arm.
St. 19 f m. Lit.     Zweifelhaft ist gr. exejuev ij/zeXyev und it.uvovxu [wohl         ‘




xepovxa\' apeXyovxa Hes. iTick BB. '28, 108, wobei apeXyetv in der spatern
Bed. „fliissiges aussaugen, auspressen 11 zu fassen ware, Liden aaO.; liber
                              K
axjurjvog, y.oiuooa s. aber     kcmcL „Bissen“).   Fernzuhalten ist poln, skoma                                                               ,


odkomn ,,gro6er Appetit, groBe Begierde“
----
                          i                                                                              n



514                                                                  q“em — quel-

                                                        11
q'Aeni „schliirfen, schlucken                                .




        camati und camati „schliirft“, u-camati „schliirft (Wasser) ein, spiilt
      Ai.
sich den Mund aus“, ptc. dcanta-, camasd-h „Trinkschale, Becher“, cumu-h
„Schussel ‘; np. rant „das Essen 11 cnmtdan „trinken“, osset. cunnin „sch]iirfen“;
                                                                 ,
                              *
nisi, hvima (aus *hvnma, idg. q't.cmu = ai. camati) „verschlucken, verschlingen
                                                                                11
                                                                                                                                              ,



hvOma f. „Speiserohre, Schlund“; arm. khim-lh pi. „faux, guttur                                                            11
                                                                                                                                              :




mit Ablautstufe <7, npers. i:am „Gaumen“, afgban. kumai ds. Liden Arm.
St. 19 f m. Lit.     Zweifelhaft ist gr. exejuev ij/zeXyev und it.uvovxu [wohl         ‘




xepovxa\' apeXyovxa Hes. iTick BB. '28, 108, wobei apeXyetv in der spatern
Bed. „fliissi
```


## [2026-09-06T22:25:20.828Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6850,6870p' HRN.txt; echo \"=== 224 ===\"; sed -n '2320,2340p' HRN.txt; echo \"=== pages ===\"; python3 -c \"\nd=open('HRN.txt',encoding='utf-8',errors='replace').read()\npages=d.split(chr(12))\nfor i,p in enumerate(pages):\n    if '786.' in p and 'Jagd' in p: print('leaf',i,'printed',i-21)\n    if '224.' in p and 'bi' in p and 'Jagd' in p: print('224 leaf',i,'printed',i-21)\n\""
}
```


### [2026-09-06T22:25:22.622Z] TOOL RESULT

```
wie äs (No. 29) oder susten (No. 782) können zweifel-
haft sein, während die Zusammenstellung von np.
siften reiben, kratzen'^) mit aw. aiu)i]siföis, yt. 14, 35
(Geldner, 3 Yasht 77) geradezu falsch ist.
786. sikär *Jagd', vergl. hisgerd (No. 224), sikerden, sekere,
iskere 'Jagdhabicht'.
phlv. äkar Magd' (vd. 5 (134) Gl.), sakra Magdhabicht'
(Bund.).
oss. LW. sk'ärun 'treiben, jagen (v. Stackeiberg,
ZDMG. 43, 672)4).
aw. "^aiwis (doch vergl. No. 221) + [/^kar- (de
Lagarde, Beitr. z. altb. Lex. 42, Pers. Stud. 75);
aber dann gewiss nicht zu [/kar- 'tun, machen*, wie
de Lagarde will, sondern zu [/kar- in np. nigär^
niijerlden. Die ursprüngliche Bedeutung findet sich
^) Vergl. auch Miklosich, Denkschr. WAW. 34, 271; 37, 20.
^) Nach anderen wäre hebr. '^Ultfi? 'Fuchs', Schakal' damit identisch
(s. Rödiger-Öesenius, Wörterbuch, S. 1457).
') Die Grundbedeutung von np. sißen ist nicht klar. Mit AbuM
Ma*änl- Versen lässt sich nichts erweisen.
^) Schon Tomaschek, Centralasiat. Studien, II, 891 (wo auch
=== 224 ===
aw. aiwis (s. bes-, No. 221) + köfe; phlv. vsköfak
(Bund.); vergl. de Lagarde, Pers. Stud. 75. Nöldeke
(mündliche Mitteilung) möchte gr. aY.vq)og 'Becher ver-
gleichen, dessen v aber Schwierigkeiten macht (zu
OKvmpoQ siehe 6. Meyer, Griech. Gramm.- § 210).
224. biSgerd *Jagd' etc.
Vergl. sigerdm (No. 786) und bes- (No. 221),
de Lagarde, Pers. Stud. 75.
225. besäten (büsöden) 'Bösewicht'.
aw. pesötanU'.
Die Aussprache und Schreibung des immer als alter-
tümlich empfundenen Wortes ist nicht zweifelsfrei.
Zu beachten ist, dass der rituelle awestische t. t.
mit dem speciell awestischen s, wofür im Mittel-
persischen sonst hr eintritt, übernommen worden ist.
Das Wort soll dann auch *Aflfe' bedeuten.
226. bet *Ente ; xer]bet Idiot'.
arm. bad, bat *Ente'; alb. ^^a^« 'Gans' (G. Meyer,
Alban. Wörterbuch, 324, wo noch weitere Formen
gesammelt sind).
4*- 52 —
=== pages ===
224 leaf 72 printed 51
leaf 195 printed 174
```


## [2026-09-06T22:25:55.347Z] AGENT

Now I'll write the verification file.


## [2026-09-06T22:27:41.488Z] TOOL CALL #88: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk292.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\nPOKW = W + \"Reconstruction:Proto-Indo-European/k%CA%B7er-\"\n\ne0 = {\n \"entry\": 0,\n \"root\": \"Kwen 2\",\n \"verdict\": \"transcription_suspect\",\n \"modern_form\": \"PIE *kʷem- 'to sip, swallow' (Pokorny IEW 640 f. k̯em-; Walde-Pokorny I 514 qʷem-)\",\n \"error_in\": \"book\",\n \"book_prints\": \"Kwen 2\",\n \"correct_form\": \"Kwem 2 (PIE *kʷem-)\",\n \"note\": \"The gloss ('sip, swallow' = Pokorny's 'schlürfen, schlucken'), the language label 'Indo-European' and the reference POK:640 are all exactly right: Pokorny IEW pp.640-641 heads the entry 'k̯em- \\u201aschlürfen, schlucken\\u2018' and lists under it precisely the four items Nourai charts (Skt. camati/cāmati, NPers. čam / čamīδan, ablaut ō-grade NPers. kām 'Gaumen'). What is wrong is the LETTER of the root name: the root ends in -m, not -n. Nourai (or his typesetter) wrote 'Kwen 2' beside the genuine 'Kwen 1' (= PIE *kʷen- 'holy', POK 630, which he charts on page 291) and thereby created a phantom root. The printed page 262 of the book itself shows 'Kwen 2' in the root box and in the running head, so the extraction is faithful and the misprint is the author's. There is no PIE *kʷen- 'to sip' in Pokorny, Walde-Pokorny or Watkins/AHD; Watkins's only kʷen- is 'Holy' [Pok. kʷen- 630].\",\n \"note_fa\": \"ریشهٔ اصلی *kʷem- «آشامیدن، فروبردن» است؛ پوکورنی در ص ۶۴۰–۶۴۱ سرواژه را «k̯em- schlürfen, schlucken» آورده و والده–پوکورنی (جلد ۱ ص ۵۱۴) همان را qʷem- می‌نویسد. معنی، برچسب زبانی و ارجاع POK:640 که نورایی داده کاملاً درست است و هر چهار مدخل نمودار (سنسکریت camati، فارسی čam و čamīdan، و صورت کشیدهٔ ō در «کام») دقیقاً در همان صفحهٔ پوکورنی آمده‌اند؛ اما نام ریشه در کتاب «Kwen 2» چاپ شده که پایانهٔ آن باید «م» باشد نه «ن». این خطای چاپی خودِ کتاب است، نه خطای خوانش اسکن: در تصویر صفحهٔ ۲۶۲ چاپی نیز همین «Kwen 2» دیده می‌شود. در پوکورنی و واتکینز هیچ ریشهٔ *kʷen- به معنی «آشامیدن» وجود ندارد؛ تنها *kʷen- «مقدس» (پوکورنی ۶۳۰) هست که نورایی خودش آن را «Kwen 1» در صفحهٔ پیشین آورده است.\",\n \"sources\": [W + \"%DA%A9%D8%A7%D9%85\", W + \"%DA%86%D9%85%DB%8C%D8%AF%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"POK:640\", \"status\": \"supports\",\n    \"note\": \"Pokorny IEW, read in POK_02.txt (awk 'BEGIN{RS=\\\"\\\\f\\\"} NR==301'), between the printed page markers '640' and '641': 'k̯em- \\u201aschlürfen, schlucken\\u2018. Ai. cämati und camati \\u201aschlürft\\u2018, Partiz. ācānta-, camasá- m. \\u201aTrinkschale, Becher\\u2018, camū- \\u201aSchüssel\\u2018; npers. čam \\u201adas Essen\\u2018, čamīδan \\u201atrinken\\u2018, osset. cumun \\u201aschlürfen\\u2018; arm. kim-kʿ Pl. \\u201afaux, guttur\\u2018; mit Ablautstufe ō: npers. kām \\u201aGaumen\\u2018, afghan. kūmai ds.' The page number is right; only the root's final consonant differs from Nourai's headword.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I p.514 (WLD_Bd1_pages.txt, \\\\f-leaf 522, running head '514 qʷem — qʷel-')\", \"stance\": \"supports\",\n    \"note\": \"'qʷem \\u201aschlürfen, schlucken\\u2018. Ai. camati und cāmati \\u201aschlürft\\u2018 … np. čam \\u201adas Essen\\u2018, čamīdan \\u201atrinken\\u2018, osset. cumin \\u201aschlürfen\\u2018 … mit Ablautstufe ō, npers. kām \\u201aGaumen\\u2018, afghan. kūmai ds.' — the same four items, again under a root in -m.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 (AHD_watkins1985.txt), s.v. kʷen-\", \"stance\": \"contradicts\",\n    \"note\": \"Watkins's only kʷen- is 'kʷen-. Holy. … [Pok. kʷen- 630.]'; his make-root is 'kʷer-1. To make … [Pok. 1. kʷer- 641.]'. He has no root 'kʷen- to sip' at all, confirming that the form in the book is a misprint for kʷem-.\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"] = [\n {\"id\": 1, \"lang\": \"Old Iranian\", \"words\": \"čam\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Gershevitch reconstructs an Old Iranian verbal base *čam- 'to sip, drink' precisely as the chart has it, when explaining Av. čimaine (Yt 10.32): the Avestan stem čiman- is an -an- extension of that base. It is the regular Iranian continuation of PIE *kʷem-: PIE *kʷ- before a front vowel gives Indo-Iranian palatal *č- (satem palatalisation, as in *kʷe > Skt. ca, Av. ča), so *kʷem- > PII *čam- > Old Iranian *čam-, exactly matching Skt. camati. Ossetic cumun 'to sip' and Baluchi forms show the base outside Persian, so it is genuinely Old Iranian and not a Persian innovation.\",\n  \"derivation_fa\": \"ستاک ایرانی باستان *čam- «آشامیدن، نوشیدن» را گرشویچ در شرح واژهٔ اوستایی čimaine (یشت ۱۰ بند ۳۲) دقیقاً به همین صورت بازسازی کرده است. تحول آوایی روشن است: *kʷ هندواروپایی پیش از واکهٔ پیشین در هندوایرانی به č کامی بدل می‌شود (همان قانونی که *kʷe را به ca سنسکریت و ča اوستایی می‌رساند)، پس *kʷem- > *čam- ایرانی باستان، هم‌ریشه با camati سنسکریت. آسی cumun «هورت کشیدن» نشان می‌دهد که این ستاک تنها فارسی نیست بلکه ایرانی باستان است. ادعای نورایی درست است.\",\n  \"sources\": [],\n  \"ref_check\": [\n    {\"ref\": \"AHM:184\", \"status\": \"supports\",\n     \"note\": \"Gershevitch, The Avestan Hymn to Mithra, commentary note 32² (AHM.txt \\\\f-leaf 200; the page carries the running head '183 | 32.1-33.2] COMMENTARY', and the note runs on to the page headed '184 COMMENTARY §34.1-34.5', so Nourai's '184' lands on the same note): 'This stem I would analyse as an -an- extension … of the OIr. base *čam- \\u201ato sip, drink\\u2019, cf. Skt. camati, NPers. čam, čamīdan'. Word-for-word Nourai's node.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW p.640 (POK_02.txt leaf 301)\", \"stance\": \"supports\", \"note\": \"'npers. čam \\u201adas Essen\\u2018, čamīδan \\u201atrinken\\u2018, osset. cumun \\u201aschlürfen\\u2018' under k̯em-.\"},\n    {\"src\": \"HRN\", \"where\": \"no. 444, p.99 (HRN.txt leaf 120)\", \"stance\": \"supports\", \"note\": \"'444. (1)čam \\u201aEssen\\u2018, čamīden \\u201atrinken\\u2018. ai. √čam-, cāmati \\u201aschlürfen\\u2018, oss. cimin, baǰdimin \\u201aschlürfen\\u2018' — Horn keeps this čam strictly apart from the homonymous čam(īdan) 'to strut'.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. I p.514\", \"stance\": \"supports\", \"note\": \"Same Iranian set (np. čam, čamīdan, osset. cumin) listed under qʷem-.\"}\n  ]},\n\n {\"id\": 2, \"lang\": \"Persian\", \"words\": \"čamîdan 2\", \"verdict\": \"confirmed\",\n  \"derivation\": \"NP چمیدن čamīdan 'to sip, drink' is the ordinary New Persian denominative/derived infinitive built on the present stem čam- (< OIr. *čam-) with the productive infinitive suffix -īdan (MP -ītan), the same formation as ramīdan, xamīdan. Both Pokorny (npers. čamīδan 'trinken') and Horn (no. 444, 'čam \\u201aEssen\\u2018, čamīden \\u201atrinken\\u2018') record it, but only from the classical lexica — hence Nourai's correct label 'obsolete'. The homograph چمیدن that survives in living Persian ('to strut, walk gracefully'), which Wiktionary derives from a different Proto-Iranian *čam- 'to walk' (a blend of *čarH- and *gam-), is a separate word, and Nourai rightly numbers this one '2'.\",\n  \"derivation_fa\": \"«چَمیدن ۲» صورت مصدری فارسی نو است که از ستاک حال čam- (از *čam- ایرانی باستان) با پسوند مصدرساز پرکاربرد ‌ـیدن (میانهٔ ‑ītan) ساخته شده، درست مانند رمیدن و خمیدن. هم پوکورنی (npers. čamīδan «نوشیدن») و هم هرن (شمارهٔ ۴۴۴: «čam خوردن، čamīden نوشیدن») آن را ثبت کرده‌اند، اما تنها از فرهنگ‌های کهن؛ از این‌رو برچسب «متروک» که نورایی زده درست است. «چمیدن» زنده در فارسی امروز به معنی «خرامیدن» واژه‌ای دیگر است و از *čam- «رفتن» می‌آید؛ نورایی به‌درستی این یکی را با شمارهٔ ۲ جدا کرده است. ادعای نورایی درست است.\",\n  \"sources\": [W + \"%DA%86%D9%85%DB%8C%D8%AF%D9%86\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:640\", \"status\": \"supports\", \"note\": \"IEW p.640 s.v. k̯em-: 'npers. čam \\u201adas Essen\\u2018, čamīδan \\u201atrinken\\u2018' (POK_02.txt leaf 301).\"},\n    {\"ref\": \"AHM:184\", \"status\": \"supports\", \"note\": \"AHM commentary note 32² (leaf 200, printed p.183-184): '…the OIr. base *čam- \\u201ato sip, drink\\u2019, cf. Skt. camati, NPers. čam, čamīdan.'\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"HRN\", \"where\": \"no. 444, p.99\", \"stance\": \"supports\", \"note\": \"'(1)čam \\u201aEssen\\u2018, čamīden \\u201atrinken\\u2018' — Horn's numbering (1) again separates it from (2)čam 'Sinn' and from čam 'to strut'.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. I p.514\", \"stance\": \"supports\", \"note\": \"'np. čam \\u201adas Essen\\u2018, čamīdan \\u201atrinken\\u2018.'\"},\n    {\"src\": \"MON\", \"where\": \"en.wiktionary.org/wiki/چمیدن (archived)\", \"stance\": \"partial\", \"note\": \"Wiktionary lists only the living sense 'to strut, walk proudly' < PIr. *čam- 'to walk'; it does not know the 'drink' homonym, which survives only lexicographically — consistent with Nourai's '(obsolete)'.\"}\n  ]},\n\n {\"id\": 3, \"lang\": \"Persian\", \"words\": \"kâm 2\", \"verdict\": \"confirmed\",\n  \"derivation\": \"NP کام kām 'palate, roof of the mouth' continues the lengthened/ō-grade of the same root, PIE *kʷōm- > OIr. *kām- 'the swallowing part', i.e. the organ named from the act; Pokorny states this explicitly ('mit Ablautstufe ō: npers. kām \\u201aGaumen\\u2018, afghan. kūmai ds.'), and Pashto kūmai is the decisive Iranian witness that the ō-grade is old and not a Persian ad-hoc form. Note that the *kʷ- here does NOT palatalise, because in the ō/ā-grade it stands before a back vowel — which is exactly why the same root yields č- in čam but k- in kām. This kām is homonymous with, and etymologically unrelated to, kām 'desire' (< OP kāma-, PIE *keh₂-), which is why Nourai numbers it '2'.\",\n  \"derivation_fa\": \"«کام ۲» به معنی سقف دهان بازماندهٔ صورت کشیدهٔ همان ریشه است: *kʷōm- هندواروپایی > *kām- ایرانی باستان، یعنی اندام را از کارِ «فروبردن» نام‌گذاری کرده‌اند. پوکورنی صریحاً می‌نویسد: «با درجهٔ ō: npers. kām \\u201aGaumen\\u2018، افغانی kūmai». نکتهٔ آوایی مهم آن است که *kʷ در این درجه پیش از واکهٔ پسین قرار می‌گیرد و کامی نمی‌شود؛ از همین‌روست که یک ریشه در «چم» به č و در «کام» به k رسیده است. این «کام» با «کام» به معنی آرزو (از kāma- پارسی باستان، ریشهٔ *keh₂-) هم‌آواست ولی هم‌ریشه نیست، و شمارهٔ ۲ نورایی همین را نشان می‌دهد. ادعای نورایی درست است.\",\n  \"sources\": [W + \"%DA%A9%D8%A7%D9%85\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:640\", \"status\": \"supports\", \"note\": \"IEW p.640 f. s.v. k̯em-: 'mit Ablautstufe ō: npers. kām \\u201aGaumen\\u2018, afghan. kūmai ds.' (POK_02.txt leaf 301) — Nourai's node verbatim.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I p.514\", \"stance\": \"supports\", \"note\": \"'mit Ablautstufe ō, npers. kām \\u201aGaumen\\u2018, afghan. kūmai ds. Lidén Arm. St. 19 f.'\"},\n    {\"src\": \"MON\", \"where\": \"en.wiktionary.org/wiki/کام (archived)\", \"stance\": \"silent\", \"note\": \"Wiktionary's Persian entry marks the 'palate' sense '(This etymology is missing or incomplete)'; it gives a full chain only for کام 'desire' (< MP kʾm, OP kāma-, PIr *káHmah, PIE *kóh₂mos). No modern source contradicts Pokorny.\"}\n  ]},\n\n {\"id\": 4, \"lang\": \"Sanskrit\", \"words\": \"čamati, camati\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Skt. camati / cāmati 'sips, slurps' (RV+) is the Indic member of the equation and the form on which the whole root is built; the by-form with long ā is the Vedic/epic variant. From PIE *kʷem- with the regular Indo-Iranian palatalisation *kʷe- > ča-. The nominal derivatives quoted by Pokorny on the same page — camasá- 'drinking cup, goblet' and camū- 'bowl' — show that the root was firmly established in Old Indic. Nourai's double spelling 'čamati, camati' simply renders the two Sanskrit variants camati and cāmati (his 'č' = c [tʃ]).\",\n  \"derivation_fa\": \"camati / cāmati سنسکریت «هورت می‌کشد، می‌نوشد» (از ریگ‌ودا به بعد) عضو هندی این معادله است و ریشه بر پایهٔ همین صورت بازسازی شده. تحول آوایی همان قاعدهٔ هندوایرانی است: *kʷe- > ča-. مشتق‌های نامی که پوکورنی در همان صفحه می‌آورد — camasá- «جام» و camū- «کاسه» — نشان می‌دهند که ریشه در هندی باستان کاملاً جاافتاده بوده است. دو نویسهٔ «čamati, camati» در نمودار در واقع همان دو گونهٔ camati و cāmati است. ادعای نورایی درست است.\",\n  \"sources\": [],\n  \"ref_check\": [\n    {\"ref\": \"POK:640\", \"status\": \"supports\", \"note\": \"IEW p.640: 'Ai. cämati und camati \\u201aschlürft\\u2018. Partiz. ācānta-, camasá- m. \\u201aTrinkschale, Becher\\u2018, camū- m. \\u201aSchüssel\\u2018' (POK_02.txt leaf 301).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I p.514\", \"stance\": \"supports\", \"note\": \"'Ai. camati und cāmati \\u201aschlürft\\u2018, ā-camati \\u201aschlürft (Wasser) ein, spült sich den Mund aus\\u2018, ptc. ācānta-, camasá-ḥ \\u201aTrinkschale, Becher\\u2018, camū-ḥ \\u201aSchüssel\\u2018.'\"},\n    {\"src\": \"HRN\", \"where\": \"no. 444, p.99\", \"stance\": \"supports\", \"note\": \"'ai. √čam-, cāmati (skr. camayati) \\u201aschlürfen\\u2018' cited as the cognate of NP čam / čamīden.\"}\n  ]}\n]\n\njson.dump(e0, open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/e0.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)\nprint(\"ok e0\", len(e0[\"nodes\"]))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk292.py"
}
```


### [2026-09-06T22:27:43.675Z] TOOL RESULT

```
ok e0 4
```


## [2026-09-06T22:33:54.037Z] TOOL CALL #89: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk292b.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\nW = \"https://en.wiktionary.org/wiki/\"\nU_KWER = W + \"Reconstruction:Proto-Indo-European/k%CA%B7er-\"\nU_SEKAR = W + \"%D8%B4%DA%A9%D8%A7%D8%B1\"\nU_QAHR  = W + \"%D9%82%D9%87%D8%B1%D9%85%D8%A7%D9%86\"\nU_LAJ   = W + \"%D9%84%D8%A7%D8%AC%D9%88%D8%B1%D8%AF\"\nU_PEYKR = W + \"%D9%BE%DB%8C%DA%A9%D8%B1\"\nU_PEYKA = W + \"%D9%BE%DB%8C%DA%A9%D8%A7%D8%B1\"\nU_SHAG  = W + \"%D8%B4%D8%A7%DA%AF%D8%B1%D8%AF\"\nU_PARG  = W + \"%D9%BE%D8%B1%DA%AF%D8%A7%D8%B1\"\nU_YAZD  = W + \"Yazdegerd\"\n\ne2 = {\n \"entry\": 2,\n \"root\": \"Kwer, Qwer\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *kʷer- 'to do, make, construct' (Pokorny IEW 641 f. 1. k̯er-; Watkins/AHD kʷer-1; LIV 391)\",\n \"note\": \"Root name, language label, gloss and the page reference are all correct. Pokorny IEW p.641 heads '1. k̯er- ‚machen, gestalten‘' (i.e. 'to make, form' — Nourai's gloss is a literal translation) and opens the entry with Ai. karóti/kṛṇóti, Av. kərənaoiti, OP akunavam / karta-, exactly the Indo-Iranian branch this chart develops. Nourai's second headword 'Qwer' is only his alternative transcription of the labiovelar. Watkins (AHD) gives 'kʷer-1. To make … [Pok. 1. kʷer- 641.]' and Cheung 2007 s.v. *kar closes his entry with '*PIE *kʷer- ‚to do, make, construct’ = LIV: 391 | Pok.: 641' — Nourai's exact reference. Beyond the root the chart is uneven: the New Persian and Old Persian core (kardan, -gar, paykar, paykār, -gird, Yazdgerd, šāgird, angārdan) is solidly documented, but three items — aiwiš-kar/šekār, kahr-mān/qahramān and Lājvard — belong to other etymologies in modern scholarship, and Nourai's own authority Horn explicitly rejects two of them.\",\n \"note_fa\": \"نام ریشه، برچسب زبانی، معنی و شمارهٔ صفحه همه درست است. پوکورنی در ص ۶۴۱ سرواژه را «1. k̯er- machen, gestalten» آورده و بی‌درنگ karóti/kṛṇóti سنسکریت، kərənaoiti اوستایی و akunavam / karta- پارسی باستان را برمی‌شمارد؛ یعنی همان شاخهٔ هندوایرانی که این نمودار می‌گستراند. «Qwer» تنها گونهٔ دیگری از آوانگاری همان همخوان لبی‌کامی است. واتکینز (AHD) «kʷer-1 To make [Pok. 1. kʷer- 641]» دارد و چونگ (۲۰۰۷) ذیل *kar می‌نویسد: «PIE *kʷer- to do, make, construct؛ LIV 391، پوکورنی ۶۴۱» — دقیقاً همان ارجاع نورایی. اما بدنهٔ نمودار یکدست نیست: هستهٔ فارسی و پارسی باستان (کردن، ‑گر، پیکر، پیکار، ‑گرد، یزدگرد، شاگرد، انگاردن) با اسناد استوار تأیید می‌شود، ولی سه مورد — شکار، قهرمان و لاجورد — در پژوهش امروزی ریشه‌ای دیگر دارند و هرن، که خودِ نورایی به او ارجاع می‌دهد، دوتای آنها را صریحاً رد کرده است.\",\n \"sources\": [U_KWER],\n \"ref_check\": [\n   {\"ref\": \"POK:641\", \"status\": \"supports\",\n    \"note\": \"Pokorny IEW p.641 (POK_02.txt \\\\f-leaf 301, between the printed markers '641' and '642'): '1. k̯er- ‚machen, gestalten‘. Vielleicht ursprünglich von irgendeiner nicht mehr bestimmbaren Handwerkstätigkeit. Ai. karóti (Imper. kuru), kṛṇóti ‚macht, vollbringt‘, Partiz. kṛtá-; … av. kərənaoiti ‚macht, vollführt, tut‘, kərəitay- ‚Tat‘, Infin. kərətōe, apers. akunavam, karta-.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I pp.517-518 (WLD_Bd1_pages.txt leaves 525-526, running heads 'qʷel qʷer- 517' and '518 qʷer-')\", \"stance\": \"supports\",\n    \"note\": \"The same entry in its first edition, with the Indic, Iranian, Celtic (mir. creth, cymr. prydu) and Baltic (lit. kuriù, kùrti ‚bauen‘) material Pokorny later repeats.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. kʷer-1 (AHD_watkins1985.txt)\", \"stance\": \"supports\",\n    \"note\": \"'kʷer-1. To make. 1. Sanskrit karoti, he makes: SANSKRIT. … 4. Suffixed form *kʷer-mn̥ in Sanskrit karma, act, deed: KARMA. [Pok. 1. kʷer- 641.]'\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Etym. Dict. of the Iranian Verb, s.v. *kar 'to do, make', pp.236-238 (CHEUNG.txt ll.15768-15925)\", \"stance\": \"supports\",\n    \"note\": \"Closes with '*PIE *kʷer- ‚to do, make, construct’ = LIV: 391 | Pok.: 641' and lists Av. kar-, OP kar-, MP kun-/kird-, NP kardan with the very preverb-compounds this chart charts (*pati-, *ham-, *ni-, *ui-, *us-).\"},\n   {\"src\": \"SYN\", \"where\": \"Buck §9.11 DO, MAKE, p.537 (SYN.txt leaf 588)\", \"stance\": \"supports\",\n    \"note\": \"Buck's 'DO, MAKE' table gives 'Av. kar-, varəz-' and 'Skt. kar-' for this notion; §9.83 (p.628) then derives OPers. patikara- from 'pati- ‚over against‘ and kar- ‚make‘'.\"}\n ],\n \"nodes\": []\n}\n\ne2[\"nodes\"] = [\n {\"id\": 1, \"lang\": \"Avestan / Old Persian\",\n  \"words\": \"kar 1, kara 1; kara-manah; paiti-kâra; paiti-kara; aiwiš-kar; wi-kâr\",\n  \"verdict\": \"disputed\",\n  \"derivation\": \"Four of the six items are solid, two are not. (a) kar-/kara-: Av. kar- 'to do, make' (pres. kərənaoiti), OP kar- (akunavam, akutā, ptc. karta-), and the agent-noun kara- 'doer, maker' as second member of compounds (Kent, Old Persian, Lexicon s.v. kara-) — the direct Iranian reflex of *kʷer-. (b) paiti-kāra 'work against, fight': Horn no. 360 reconstructs 'aw. *paitikāra-' for NP peikār, comparing Av. paiti.kərənaot (Vd 2,6) and Phl. patkār 'Kampf', patkārītan; Nyberg's glossary p.157 has 'patkār, pitkār: quarrel, controversy, dispute … NP patkār'. (c) paiti-kara 'form against (like) something': OP patikara- 'picture, (sculptured) likeness' is directly attested (DB 4.71,77,78; DNa 41; DSn 1), and Kent analyses it as kara- 'with passive meaning, ‚thing made‘'; Buck p.628 spells it out: 'OPers. patikara- used of the figures sculptured in relief (NPers. paikar ‚face, form, portrait‘), cpd. of pati- ‚over against‘ and kar- ‚make‘, hence lit. ‚something made in likeness‘'. (d) wi-kār 'to digest': Abolqasemi FFD p.75 reconstructs Old Iranian *wi-kār-a- / *wi-kār-ta- for MP wigār- / NP gowār-, with wi- a verbal preverb and kār the lengthened grade of kar 'to do'. — DISPUTED: (e) 'aiwiš-kar' is not an attested Avestan compound; it is de Lagarde's conjecture, and Horn no. 786, who reports it, at once refuses Nourai's root: 'aw. *aiwiš + √kar- (de Lagarde) — aber dann gewiss NICHT zu √kar- ‚tun, machen‘, wie de Lagarde will, sondern zu √kar- in np. nigār, nigerīden'. Cheung 2007 removes it from *kar altogether, setting up a separate purely Iranian root *skar 'to pursue, drive, look for (the cattle)' (Parth. ʾškr- 'to hunt', BMP wiškar 'hunting-ground', škarag 'bird of prey') of which he says 'This root is exclusively Ir.; no reliable IE cognates can be cited.' (f) 'kara-manah' is likewise not attested in Avestan or Old Persian; it is Nourai's back-formation from qahramān, for which see node #2.\",\n  \"derivation_fa\": \"چهار واژه از شش واژهٔ این جعبه استوار است و دو تای دیگر نه. الف) kar-/kara-: اوستایی kar- «کردن» (حال kərənaoiti)، پارسی باستان kar- (akunavam، اسم مفعول karta-) و اسم فاعلِ kara- «کننده» در ترکیب‌ها (کنت، واژه‌نامهٔ پارسی باستان) — بازتاب مستقیم *kʷer-. ب) paiti-kāra: هرن (شمارهٔ ۳۶۰) برای «پیکار» صورت اوستایی *paitikāra- را بازسازی می‌کند و پهلوی patkār «کارزار» را گواه می‌گیرد؛ نیبرگ نیز در ص ۱۵۷ «patkār: نزاع، ستیز؛ فارسی نو patkār» دارد. ج) paiti-kara: patikara- پارسی باستان «تندیس، نگاره» در کتیبه‌ها (بیستون ۴٫۷۱ و ۷۷ و ۷۸؛ نقش رستم ۴۱) به‌روشنی گواهی شده و باک (ص ۶۲۸) آن را «ساختهٔ به‌مانندِ چیزی» از pati- + kar- می‌داند. د) wi-kār: ابوالقاسمی در «فعل‌های فارسی دری» ص ۷۵ برای «گواردن» صورت ایرانی باستان *wi-kār-a- را می‌آورد که wi پیشوند فعلی و kār صورت بالندهٔ ریشهٔ kar «کردن» است. — اما: هـ) «aiwiš-kar» ترکیبی اوستایی گواهی‌شده نیست؛ حدس دُلاگارد است و هرن (شمارهٔ ۷۸۶) که آن را نقل می‌کند بی‌درنگ ریشهٔ نورایی را رد می‌کند: «اوستایی *aiwiš + √kar- — اما در آن صورت قطعاً نه از √kar «کردن، ساختن» چنان‌که دُلاگارد می‌خواهد، بلکه از همان √kar که در نگار و نگریدن هست». چونگ (۲۰۰۷) آن را یکسره از *kar بیرون می‌برد و ریشهٔ جداگانه و صرفاً ایرانیِ *skar «راندن، پی‌جویی کردن» می‌گذارد و می‌نویسد «این ریشه منحصراً ایرانی است؛ هیچ هم‌ریشهٔ هندواروپایی معتبری برای آن نمی‌توان آورد». و) «kara-manah» نیز در اوستا و پارسی باستان گواهی ندارد و ساختِ قهقرایی نورایی از «قهرمان» است (بنگرید به گرهٔ ۲). پس حکم این گره: بخش اصلی درست، ولی دو واژه پژوهش امروزی را با خود ندارد.\",\n  \"sources\": [U_PEYKR, U_PEYKA, U_SEKAR],\n  \"ref_check\": [\n    {\"ref\": \"NYB:157\", \"status\": \"supports\",\n     \"note\": \"Nyberg, Manual of Pahlavi II, Glossary, printed p.157 (NYB_vol2_glossary.txt \\\\f-leaf 173, running head '157 patkarītan'): 'patkar [ptkly, Prth ptkr] image ŠPrs: 3. 14. Prth:4. — OP pati-kara-; MPrs phykr; Arm. lw. patker; Syr. Talm. lw. ptakrā ‚an idol‘ … NP paikar.' and 'patkār [ptkʾl], pitkār: quarrel, controversy, dispute … MPrs phykʾr; Paz. patkār; NP patkār.' Exactly Nourai's paiti-kara / paiti-kāra pair. (Caveat: Nyberg refers patkār and hangārtan to his ²kartan < Av. ²kar- ‚to recollect, mention‘, 'not from ¹kar- as Bthl. has it'.)\"},\n    {\"ref\": \"HRN:80\", \"status\": \"supports\",\n     \"note\": \"Horn, Grundriss p.80 (HRN.txt leaf 101): '360. peikār, peigār ‚Kampf‘. aw. *paitikāra-, vergl. paiti.kərənaot (vd. 2, 6); phlv. patkār ‚Kampf‘ …, patkārītan …, arm. LW. paykar ‚Kampf‘. 361. peiker ‚Bild‘. ap. patikara- ‚Bild‘; phlv. patkar (Bund.), arm. LW. patker.'\"},\n    {\"ref\": \"ZAW:38\", \"status\": \"supports\",\n     \"note\": \"Bartholomae, Zum altiranischen Wörterbuch p.38 (ZAW_pages.txt leaf 61), §16.2: 'kērd, qērd ‚gemacht‘ …, kērdan ‚machen‘ …, kērdag ‚Tat‘ …; man vergleiche zur Wurzelsilbe des bp. kartan, Paz. kardan, np. کردن kardan.'\"},\n    {\"ref\": \"SYN:628\", \"status\": \"supports\",\n     \"note\": \"Buck, Selected Synonyms p.628 = §9.83 STATUE (SYN.txt leaf 684): 'OPers. patikara- used of the figures sculptured in relief (NPers. paikar ‚face, form, portrait‘), cpd. of pati- ‚over against‘ and kar- ‚make‘, hence lit. ‚something made in likeness‘.'\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon s.vv. kar-, kara-, karta-, patikara- (KNT.txt ll.5252-5637)\", \"stance\": \"supports\",\n     \"note\": \"'kara- sb. ‚doer, maker‘, as 2d element of cpd.: deriv. of kar- … and with passive meaning, ‚thing made‘, in patikara-'; 'patikara- sb. ‚picture, (sculptured) likeness‘ … to kar-'; 'karta-, Skt. kṛtá-, to kar-'.\"},\n    {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW cols. 445-448 s.v. ¹kar- 'machen' (BRT.txt l.9139 ff.)\", \"stance\": \"partial\",\n     \"note\": \"'j., g., p. ¹kar- V. ‚machen‘. Praes. kar-, kərənu-…; PPfP. kərəta-, karta-; Inf. cartanaiy, kərətōe.' Bartholomae has ¹kar- 'machen' with kərəta-/karta-, but also a distinct ²kar- 'gedenken' and a ⁴kar- 'einfurchen'; he has NO entry aiwiš-kar / aiwi.škar-, so Nourai's fifth word is not in the Altiranisches Wörterbuch.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"s.v. *kar (Middle Persian and Parthian sections) and s.v. *skar p.345\", \"stance\": \"partial\",\n     \"note\": \"*kar covers '(+ *pati-) BMP ptkl /pahikar/ ‚picture, image‘, MMP phykʾr ‚battle, struggle‘' — i.e. Nourai's paiti-kara and paiti-kāra; but hunting is put under *skar, 'exclusively Ir.; no reliable IE cognates can be cited', which removes aiwiš-kar from this root.\"},\n    {\"src\": \"HRN\", \"where\": \"no. 786, p.174 (HRN.txt leaf 195)\", \"stance\": \"contradicts\",\n     \"note\": \"'786. šikār ‚Jagd‘ … phlv. škar ‚Jagd‘, šakra ‚Jagdhabicht‘ … aw. *aiwiš + √kar- (de Lagarde, Beitr. z. altb. Lex. 42, Pers. Stud. 75); aber dann gewiss nicht zu √kar- ‚tun, machen‘, wie de Lagarde will, sondern zu √kar- in np. nigār, nigerīden.' Horn — Nourai's own reference for this root elsewhere — denies precisely the arrow drawn here for aiwiš-kar.\"}\n  ]},\n\n {\"id\": 2, \"lang\": \"Persian\", \"words\": \"kârîdan 2; gar 2; kahr-mân\", \"verdict\": \"disputed\",\n  \"derivation\": \"kārīdan 2 / kardan / kār: the ordinary New Persian verb, MP kardan (pres. kun-, NW kar-) < OIr. *kṛta-/*karta- and *kṛ-nu-; Abolqasemi FFD p.68 spells it out — 'kard ← MP kird and kard ← Old Iranian *kṛ-ta- and *kar-ta-; kṛ is the weak grade of the root kar ‚to do‘; kun ← MP kun ← OP *kunu- ← OIr. *kṛ-nu-'; the variant kārīdan is the analogical -īdan infinitive built on the lengthened stem kār. gar 2, the agent suffix (āhan-gar 'smith', kuze-gar 'potter', zar-gar 'goldsmith' — the words in the chart's extra line): from OIr. *kara- 'doer' / *kṛta-, the same element Kent lists as the second member of avā-kara-, hamaranakara-; Mo'in's footnote in Borhan p.1779 gives 'Avestan kərəta- ‚made‘' for it. kahr-mān / qahramān is the problem: modern scholarship derives Arabic-Persian قهرمان 'steward, majordomo' (whence, in Persian, 'champion, hero') from Middle Persian kārframān 'manager, overseer' = kār 'work, affair' + framān 'command', borrowed into Arabic through Aramaic — which is why it begins with q- and has nothing to do with Arabic qahr 'force'. Nourai's kara-manah 'wise at work' is not the modern view; it does, however, faithfully reproduce his cited source, Mo'in's footnote in Borhan-e Qāṭeʿ p.1549 (after Dozy), which gives 'kahrumān … به معنی کاراندیش است از مصدر kar (= کردن) + مان (منش)'. So the node is a case of Nourai following an older Persian tradition against the current one.\",\n  \"derivation_fa\": \"«کاریدن ۲ / کردن / کار»: فعل معمول فارسی نو، از فارسی میانهٔ kardan (ستاک حال kun-، در شمال‌غربی kar-) از *kṛ-ta-/*kar-ta- و *kṛ-nu- ایرانی باستان؛ ابوالقاسمی در «فعل‌های فارسی دری» ص ۶۸ می‌نویسد: «کرد ← فارسی میانه kird و kard ← ایرانی باستان *kṛ-ta- و *kar-ta-؛ kṛ صورت ضعیف ریشهٔ kar به معنی کردن است؛ کن ← kun ← پارسی باستان *kunu- ← ایرانی باستان *kṛ-nu-». «‑گر» پسوند فاعلی (آهنگر، کوزه‌گر، زرگر) از *kara- «کننده» / kərəta- می‌آید و حاشیهٔ معین بر برهان ص ۱۷۷۹ همین را می‌آورد: «اوستا kərəta- (ساخته)». اما «کهرمان / قهرمان» جای بحث دارد: پژوهش امروزی آن را وام‌واژه‌ای از فارسی میانهٔ kārframān «کارگزار، سرکار» (kār + framān) می‌داند که از راه آرامی به عربی رفته و ازاین‌رو با قاف آغاز می‌شود و ربطی به «قهر» عربی ندارد؛ معنی «پهلوان» تحول معنایی درون‌فارسی است. بازسازی نورایی (*kara-manah «کاراندیش») دیدگاه امروزی نیست، ولی دقیقاً همان چیزی است که مرجع خودش، حاشیهٔ معین بر برهان ص ۱۵۴۹ به نقل از دُزی، می‌گوید. پس این گره نمونهٔ پیروی نورایی از سنت کهن‌تر فارسی در برابر دیدگاه نو است.\",\n  \"sources\": [U_QAHR],\n  \"ref_check\": [\n    {\"ref\": \"BQT:1549\", \"status\": \"supports\",\n     \"note\": \"Borhan-e Qāṭeʿ ed. Moʿin p.1549 (vol. 3, pdf p.342 of BQT_v3_picofile.pdf, via BQT_v3_pagemap.json): headword 'قهرمان … کارفرما را گویند', with Moʿin's footnote 5: '(ع) «قهرمان» جمع «قهارمة» … «کهرمان» kahrumān که بمعنی کاراندیش است از مصدر kar (= کردن) + مان (منش)'. This is verbatim Nourai's 'kahr-mân : wise at work'.\"},\n    {\"ref\": \"BQT:1779\", \"status\": \"supports\",\n     \"note\": \"Borhan p.1779 (vol. 3, pdf p.576): the entry «گر» — 'وبمعنی کننده و سازنده هم هست، همچو کوزه‌گر و کاسه‌گر … ومرادف کار باشد همچو آموزکار و آموزگر' — with Moʿin's footnote: 'اوستا kərəta- (ساخته)'. Supports 'gar 2: a suffix meaning worker'.\"},\n    {\"ref\": \"BQT:1617\", \"status\": \"not_found\",\n     \"note\": \"Borhan p.1617 (vol. 3, pdf p.410) carries the کر- entries (کردنگ، کرده‌کار، کردیدن، کرر، کردمان، کره), not کاریدن or کردن; the کاریدن/کردن headwords are not on that page in the Ibn Sina/Amir Kabir pagination. Either Nourai's number is a few pages off or he is citing the کردمان entry.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"FFD\", \"where\": \"Abolqasemi, Feʿl-hā-ye Fārsi-ye Dari, printed p.68 (FFD_pages.txt pdf page 73)\", \"stance\": \"supports\",\n     \"note\": \"'کردن: کرد ← فارسی میانه kird و kard ← ایرانی باستان *kṛ-ta- و *kar-ta- … kṛ صورت ضعیف ریشهٔ kar به معنی «کردن» است. کن ← فارسی میانه kun ← فارسی باستان *kunu- ← ایرانی باستان *kṛ-nu-.'\"},\n    {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary s.v. kardan and kirrōg (PHD_mackenzie.txt ll.3228, 3309)\", \"stance\": \"supports\",\n     \"note\": \"'kardan, kun-, (P kar-) [OBYDWN-tn’ …] to do, make'; 'kirrōg [k(y)lwk | M qrwg] artisan, craftsman; skilled' — the MP agent-noun type behind NP -gar.\"},\n    {\"src\": \"MON\", \"where\": \"en.wiktionary.org/wiki/قهرمان (archived)\", \"stance\": \"contradicts\",\n     \"note\": \"'from Middle Persian kārframān (also kʾlplmʾn in Book Pahlavi), ‚manager, overseer‘, from kār ‚work, affair‘ + framān ‚command, order‘ … Arabic قَهْرَمَان ‚superintendent, majordomo‘ was borrowed through Aramaic, explaining the initial q- rather than derivation from Arabic qahr.' Not kara-manah.\"}\n  ]},\n\n {\"id\": 3, \"lang\": \"Persian\", \"words\": \"paykâr; paykar; šekâr; govârdan\", \"verdict\": \"disputed\",\n  \"derivation\": \"Three of the four are confirmed, one is not. paykar پیکر 'body, figure, statue' < MP patkar/pahikar 'picture, image' [ptkl] < OP patikara- (attested DB 4.71,77,78; DNa 41) < PIr *pati-kára- 'thing made in likeness'; the Armenian loan patker guarantees the Middle Iranian form. paykār پیکار 'battle' < MP ptkʾl /pahikār/ 'struggle, battle, dispute' < *pati-kāra- with the causative-lengthened stem kār: 'acting against' → 'fighting'; Parthian pdkʾr- 'to contend' (Cheung) confirms it. govārdan گواردن 'to digest' < MP wigār- (past wigārd) < OIr *wi-kār-a- / *wi-kār-ta-, preverb wi- 'apart' + lengthened kār: 'to make apart, break down'; the -k- voices to -g- after the preverb and *wi- > gu-/go- (as in gozīdan < *wi-čaid-, gorīxtan < *wi-raik-); the nouns gowārā and gowāreš belong here too. šekār شکار 'hunt' is the odd one out: MP škār, Parthian ʾškr- 'to hunt, chase', MP wiškar 'hunting-ground', škarag 'bird of prey' point to a root *skar 'to pursue, drive, look for (the cattle)', which Cheung 2007 (p.345) declares 'exclusively Ir.; no reliable IE cognates can be cited', and Wiktionary follows him, adding that the Persian word may itself be a loan from Sogdian škʾr- 'to pursue, drive'. It therefore does not descend from *kʷer- at all, and even de Lagarde's *aiwiš-kar analysis was rejected by Horn (no. 786).\",\n  \"derivation_fa\": \"سه واژه از چهار واژه تأیید می‌شود و یکی نه. «پیکر» از فارسی میانهٔ patkar/pahikar «نگاره، تصویر» از patikara- پارسی باستان (گواهی‌شده در بیستون ۴٫۷۱ و ۷۷ و ۷۸ و نقش رستم ۴۱) از *pati-kára- ایرانی باستان «آنچه به‌مانند چیزی ساخته شده»؛ وام‌واژهٔ ارمنی patker صورت ایرانی میانه را تضمین می‌کند. «پیکار» از فارسی میانهٔ pahikār «ستیز، نبرد» از *pati-kāra- با ستاک بالندهٔ kār، یعنی «در برابر کسی عمل کردن» ← «جنگیدن»؛ پارتی pdkʾr- «ستیزیدن» (چونگ) گواه آن است. «گواردن» از فارسی میانهٔ wigār- (ماضی wigārd) از *wi-kār-a- ایرانی باستان: پیشوند wi- «جدا» + kār؛ ک پس از پیشوند به گ نرم شده و *wi- در فارسی نو به «گو/گُ» بدل گشته (چنان‌که در گزیدن < *wi-čaid- و گریختن < *wi-raik-)؛ «گوارا» و «گوارش» نیز از همین‌جایند. اما «شکار» جدا می‌افتد: فارسی میانه škār، پارتی ʾškr- «شکار کردن»، wiškar «شکارگاه» و škarag «مرغ شکاری» همه به ریشهٔ *skar «راندن، پی‌جویی کردن» می‌رسند که چونگ (ص ۳۴۵) آن را «منحصراً ایرانی، بدون هیچ هم‌ریشهٔ هندواروپایی معتبر» می‌داند و ویکی‌واژه نیز همان را می‌گوید و می‌افزاید که واژهٔ فارسی شاید وام از سغدی škʾr- باشد. پس «شکار» اصلاً از *kʷer- نیامده و پژوهش امروزی این پیکان را رد می‌کند.\",\n  \"sources\": [U_PEYKR, U_PEYKA, U_SEKAR],\n  \"ref_check\": [\n    {\"ref\": \"FFD:75\", \"status\": \"supports\",\n     \"note\": \"Abolqasemi, Feʿl-hā-ye Fārsi-ye Dari p.75 (FFD_pages.txt pdf page 80): 'گواردن — گوار ← فارسی میانه wigār- ← ایرانی باستان *wi-kār-a- … kār صورت بالندهٔ ریشهٔ kar به معنی «کردن» است. wi پیشوند فعلی است. مادهٔ ماضی در فارسی میانه wigārd بوده که جعلی است. «گوارد» فارسی دری بازماندهٔ *wi-kār-ta- ایرانی باستان است.' Exactly Nourai's wi-kâr → govârdan.\"},\n    {\"ref\": \"FFD:68\", \"status\": \"supports\",\n     \"note\": \"Same book p.68 (pdf 73), the کردن entry: 'کرد ← فارسی میانه kird و kard ← ایرانی باستان *kṛ-ta- و *kar-ta- … ریشهٔ kar به معنی کردن' — the base of the whole node.\"},\n    {\"ref\": \"MON:2057,3426\", \"status\": \"not_checked\",\n     \"note\": \"Nourai cites the 6-volume Amir Kabir Moʿin; the only local Moʿin text (MON_part1/2.txt) is the 2-volume Adena abridgement with different pagination and without the etymological brackets, and vajehyab was not consulted for these two pages, so his page references could not be verified.\"},\n    {\"ref\": \"DMO:115\", \"status\": \"not_checked\",\n     \"note\": \"Saʿid Nafisi, Dar Maktab-e Ostād — refs_online.json records no accessible copy ('PDF page exists; not fetched').\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"HRN\", \"where\": \"nos. 360-361, p.80; no. 786, p.174\", \"stance\": \"partial\",\n     \"note\": \"Supports peikār and peiker ('aw. *paitikāra-'; 'ap. patikara- ‚Bild‘'), but for šikār (no. 786) refuses the 'make' root: 'aber dann gewiss nicht zu √kar- ‚tun, machen‘ … sondern zu √kar- in np. nigār, nigerīden.'\"},\n    {\"src\": \"NYB\", \"where\": \"Glossary p.157 (leaf 173)\", \"stance\": \"supports\",\n     \"note\": \"'patkar … OP pati-kara- … NP paikar'; 'patkār, pitkār: quarrel, controversy, dispute … NP patkār.'\"},\n    {\"src\": \"CHEUNG\", \"where\": \"s.v. *kar (MP/Parth./NWIr. sections) and s.v. *skar p.345\", \"stance\": \"partial\",\n     \"note\": \"'(+ *pati-) BMP ptkl /pahikar/ ‚picture, image‘, MMP phykʾr ‚battle, struggle‘ … NP paykar ‚picture, statue‘' — but hunting is under *skar: 'BMP wskl /wiškar/ ‚hunting-ground, wilderness‘ … Parthian ʾškr- ‚to hunt, chase‘ … This root is exclusively Ir.'\"},\n    {\"src\": \"SYN\", \"where\": \"Buck §9.83 STATUE, p.628\", \"stance\": \"supports\",\n     \"note\": \"'OPers. patikara- … (NPers. paikar ‚face, form, portrait‘), cpd. of pati- ‚over against‘ and kar- ‚make‘.'\"}\n  ]},\n\n {\"id\": 4, \"lang\": \"Avestan / Old Persian\", \"words\": \"krta; yazato-karteta\", \"verdict\": \"plausible\",\n  \"derivation\": \"The arrow itself is beyond doubt: Av. kərəta- / OP karta- (= Skt. kṛtá-) is the perfect passive participle of kar- 'to make', with the accented *-tó- suffix regularly taking the zero grade of the root (Kent §160.10; cf. dasta-karta- 'handmade', duš-karta- 'ill-done', a-karta- 'not made'). The first half of Nourai's gloss, 'creation', is therefore right. Two reservations. (1) The sense 'city' is not Old Iranian: it is a secondary New Persian/Middle Persian development in the place-name suffix -gird/-kart ('the thing built' → 'the settlement'), and Bartholomae himself doubted even that, writing in AiW col. 448 n.22 that 'das np. -gird am Ende von Ortsnamen, mp. -kart, im arm. LW. -kert … bedeutet schwerlich ‚gemacht‘' and preferring a noun 'Aufenthalt, Heim'. Horn no. 900 takes the other side and derives -gird from 'ap. *kṛta-, phlv. -kart, vergl. Dārāhkart', which is the view Nourai follows and which is now standard. (2) 'yazato-karteta' is a garbled form: the compound behind Yazdgerd is *yazata-kṛta- / MP Yazdkart 'made by god', and no Iranian form *karteta exists; the printed page reads 'yazato-karteta', so the extraction is faithful and the oddity is the book's own loose transliteration.\",\n  \"derivation_fa\": \"خودِ پیکان تردیدناپذیر است: kərəta- اوستایی / karta- پارسی باستان (= kṛtá- سنسکریت) اسم مفعول ریشهٔ kar «کردن» است که با پسوند تکیه‌دار *-tó- ساخته می‌شود و ریشه در آن به درجهٔ صفر می‌رود (کنت §۱۶۰٫۱۰؛ قس dasta-karta- «دست‌ساخت»، duš-karta- «بدساخته»). پس بخش نخست معنی که نورایی داده («آفریده») درست است. دو نکته اما هست: نخست آنکه معنی «شهر» ایرانی باستان نیست، بلکه تحول معنایی ثانوی در پسوند جاینامی ‑گِرد / ‑kart فارسی میانه و نو است («ساخته» ← «آبادی»)؛ خودِ بارتولمه در حاشیهٔ ستون ۴۴۸ فرهنگ ایرانی باستان همین را هم رد می‌کند و می‌نویسد «‑گرد فارسی نو در پایان جاینام‌ها … به‌سختی می‌تواند ‚ساخته‘ معنی دهد» و آن را نامی به معنی «جایگاه، خانه» می‌داند؛ ولی هرن (شمارهٔ ۹۰۰) بر خلاف او آن را از «پارسی باستان *kṛta-، پهلوی ‑kart، قس داراب‌کرت» می‌گیرد و همین دیدگاه امروز پذیرفته است و نورایی از آن پیروی کرده. دوم آنکه صورت «yazato-karteta» آشفته است؛ ترکیب اصلی *yazata-kṛta- / Yazdkart فارسی میانه «ساختهٔ ایزد» است و صورتی به شکل *karteta در هیچ زبان ایرانی نیست. در تصویر صفحهٔ چاپی نیز همین «yazato-karteta» آمده، پس خطای خوانش اسکن نیست بلکه آوانگاری سست خودِ کتاب است.\",\n  \"sources\": [U_YAZD],\n  \"ref_check\": [\n    {\"ref\": \"HRN:201\", \"status\": \"supports\",\n     \"note\": \"Horn, Grundriss p.201 (HRN.txt leaf 222): '900. (1)gird (Endung von Ortsnamen). ap. *kṛta- (Hübschmann, KZ. 27, 112); phlv. -kart, vergl. Dārāhkart. Die Ableitung von ap. vardana- … ist unmöglich, da ap. rd im Np. zu l geworden sein müsste.'\"},\n    {\"ref\": \"ZAW:38\", \"status\": \"supports\",\n     \"note\": \"Bartholomae, ZAW p.38 (leaf 61), §16.2: 'yazdēgērd ‚Götterstadt‘ 75, SM.; vgl. dazu von Stackelberg …, Munkácsi …, Bartholomae AirWb. 448' — the name is put under the kar-/kart- material of AiW col. 448, though Bartholomae renders it 'god-city' rather than 'god-made'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon and §160.10 (KNT.txt ll.2620, 5537-5584)\", \"stance\": \"supports\",\n     \"note\": \"'karta-, Skt. kṛtá-, to kar-'; 'dastakarta- adj. ‚handmade‘: dasta- + ptc. karta- (§160.10), to kar- ‚make‘'; 'duškarta- adj. ‚ill-done‘ … past ptc. pass. to kar-'.\"},\n    {\"src\": \"BRT\", \"where\": \"AiW col. 448, footnote 22 (BRT.txt l.9139 ff.)\", \"stance\": \"contradicts\",\n     \"note\": \"'Das np. -gird am Ende von Ortsnamen, mp. -kart, im arm. LW. -kert (Hübschmann GIrPh. 1b.190) bedeutet schwerlich ‚gemacht‘. Ich sehe darin ein Nom. von der Bedeutung ‚Aufenthalt, Heim‘' — Bartholomae denies the 'city = made' equation Nourai's gloss assumes.\"},\n    {\"src\": \"MON\", \"where\": \"en.wiktionary.org/wiki/Yazdegerd (archived)\", \"stance\": \"supports\",\n     \"note\": \"'From Middle Persian Yazdegerd, Yazdgird, literally ‚made by God‘, from Yazd + -gird, -kirt' — Nourai's 'God's creation' is right, only his Avestan form is misspelt.\"}\n  ]},\n\n {\"id\": 5, \"lang\": \"Persian\", \"words\": \"-vard, -gard, -jerd; Yazdgerd; Lâjvard\", \"verdict\": \"disputed\",\n  \"derivation\": \"-gard/-gird and its Arabised doublet -jerd (Borūjerd, Susangerd, Dastgerd) are correctly derived: MP -kart/-gird < OP *kṛta- 'made, built', the participle of node #4, semantically 'the built (place)' → 'town, settlement'; Borhan-e Qāṭeʿ p.1787 s.v. گرد glosses it 'بمعنی شهر و مدینه هم هست، همچو داراب‌گرد و سیاوش‌گرد' with Moʿin's footnote 'پارسی باستان kṛta-، پهلوی kart-'. Yazdgerd is likewise correct: MP Yazdkart, Yazdgird, literally 'made by God' (yazd + -gird), and Borhan p.2432 s.v. یزدجرد notes 'معرب یزدکرت Yazdkart'. But two items fail. (1) -vard (Abīvard) is separated from -gird by Horn himself at exactly the page Nourai cites for node #4: 'Np. -verd dagegen in Abīverd u. a. m. kann nur auf ap. *varta- zurückgehen' — a different word, not *kṛta-. (2) Lājvard 'lapis lazuli, azure' is not '-vard' + a Turkish tribe name at all: the standard etymology takes it from the mining district Lāžvard in Badakhshan, and Bailey analyses the second element as PIr *varta- 'stone' (Wakhi wurt, Kurdish berd), i.e. once more *varta-, not *kṛta-; the whole word travelled on as Arabic lāzaward, Latin lazurium/azura, Old French azur, English azure. Nourai's 'home of the Turkish Lāj(in) tribe' is a folk etymology of the kind Borhan collects.\",\n  \"derivation_fa\": \"«‑گرد / ‑گِرد» و گونهٔ معرّب آن «‑جرد» (بروجرد، سوسنگرد، دستگرد) درست ریشه‌یابی شده است: فارسی میانهٔ ‑kart/‑gird از *kṛta- پارسی باستان «ساخته»، یعنی همان اسم مفعول گرهٔ ۴، با تحول معنایی «ساخته» ← «آبادی، شهر»؛ برهان قاطع ص ۱۷۸۷ ذیل «گرد» می‌آورد «بمعنی شهر و مدینه هم هست، همچو داراب‌گرد و سیاوش‌گرد» و حاشیهٔ معین «پارسی باستان kṛta-، پهلوی kart-» دارد. «یزدگرد» نیز درست است: فارسی میانه Yazdkart «ساختهٔ ایزد»، و برهان ص ۲۴۳۲ می‌نویسد «معرب یزدکرت». اما دو مورد نادرست است. نخست «‑ورد» (ابیورد) را خودِ هرن در همان صفحه‌ای که نورایی برای گرهٔ ۴ به آن ارجاع می‌دهد از «‑گرد» جدا می‌کند: «اما ‑verd فارسی نو در ابیورد و مانند آن تنها می‌تواند به *varta- پارسی باستان بازگردد» — واژه‌ای دیگر، نه *kṛta-. دوم «لاجورد» اصلاً «لاج + ورد» به معنی «خانهٔ قبیلهٔ ترکِ لاجین» نیست؛ ریشه‌شناسی پذیرفته آن را از نام کان لاژورد در بدخشان می‌داند و بیلی جزء دوم را *varta- ایرانی باستان «سنگ» (وخی wurt، کردی berd) می‌گیرد — باز هم *varta- و نه *kṛta-. همین واژه به عربی «لازورد»، لاتین lazurium/azura، فرانسهٔ کهن azur و انگلیسی azure رسیده است. توضیح نورایی ریشه‌شناسی عامیانه است.\",\n  \"sources\": [U_LAJ, U_YAZD],\n  \"ref_check\": [\n    {\"ref\": \"BQT:1787\", \"status\": \"supports\",\n     \"note\": \"Borhan-e Qāṭeʿ ed. Moʿin p.1787 (vol. 3, pdf p.584): s.v. «گرد» — '… ودور وحوالی واطراف را نیز گفته‌اند … وبمعنی شهر و مدینه هم هست، همچو داراب‌گرد و سیاوش‌گرد که مراد از آن شهر داراب و شهر سیاوش است', with Moʿin's footnote 3: 'پارسی باستان kṛta-، پهلوی kart-'.\"},\n    {\"ref\": \"BQT:2432\", \"status\": \"supports\",\n     \"note\": \"Borhan p.2432 (vol. 4, pdf p.515): 'یزدجرد - بکسر جیم، معرّب …', footnote 3: 'معرب یزدکرت Yazdkart'. Supports the Yazdgerd item; the page has no entry for Lājvard.\"},\n    {\"ref\": \"DMO:115\", \"status\": \"not_checked\", \"note\": \"Nafisi, Dar Maktab-e Ostād: no accessible copy per refs_online.json.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"HRN\", \"where\": \"no. 900, p.201 (HRN.txt leaf 222)\", \"stance\": \"partial\",\n     \"note\": \"Supports -gird ('ap. *kṛta-; phlv. -kart, vergl. Dārāhkart') but explicitly excludes -vard: 'Np. -verd dagegen in Abīverd u. a. m. kann nur auf ap. *varta- zurückgehen; vergl. -varta in indischen Städtenamen.'\"},\n    {\"src\": \"MON\", \"where\": \"en.wiktionary.org/wiki/لاجورد (archived)\", \"stance\": \"contradicts\",\n     \"note\": \"'From the place name Lāžvard in Badakhshan where the stone was mined … the second component, according to Bailey, from Proto-Iranian *varta- ‚stone‘ (Wakhi wurt, Northern Kurdish ber, Central Kurdish berd) … Descendants: Arabic لازورد, Latin lazulum/lazurium/azura, English azure.' No Turkish tribe, and no -kṛta-.\"},\n    {\"src\": \"BRT\", \"where\": \"AiW col. 448 n.22\", \"stance\": \"contradicts\",\n     \"note\": \"Bartholomae doubts that the -gird of place names means 'made' at all, taking it as a noun 'Aufenthalt, Heim' — a minority view today, but a caution against the chart's confident 'krta: creation, city'.\"}\n  ]},\n\n {\"id\": 6, \"lang\": \"Avestan\",\n  \"words\": \"han-kar; han-kareyemi, han-keretha; haša-kerta; pairi-kara\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"haša-kerta is the best-established item: Bartholomae (ZAW p.38) sets up Proto-Iranian *hašā-karta- for Manichaean MP hašāgērd 'discipulus', literally 'made a companion / attached to the service of a priestly colleague', from *haxay- 'friend, companion' (whence Nourai's cross-reference to Sekw = PIE *sekʷ- 'to follow') + karta- 'made'; at ZAW p.242 he adds the cross-reference to AiW col. 1744 s.v. haxay- and to OP haxāmaniš-. han-kar / hankārayemi / hankərəθa- are genuine Avestan (Y 1.1 ff., Vr 1.1 ff., F 34: 'nivaēδayemi hankārayemi'), and Bartholomae files them under ¹kar- 'machen' — 'mit ham ‚für Jemanden es (näml. den Yasna) vollziehen‘' — with the note 'Pü.: hangārtanem (vgl. np. angārdan)', which is exactly Nourai's arrow. But the attribution is contested: Nyberg (Glossary, s.v. ²kartan) reassigns hankārayemi to Av. ²kar- 'to recollect, mention, commend', saying explicitly 'not from ¹kar- as Bthl. has it', and Horn no. 123 hedges with 'ai. 2 √kar- ‚gedenken‘ (?)'. Cheung 2007 restores Bartholomae's view, putting MP hangār- 'to account, reckon' under *kar 'to do'. pairi-kara is the weakest: the Avestan form actually attested is pairi.kārayōiš (Vd 13,6) 'you shall draw a furrow all round', which Bartholomae assigns to his ⁴kar- 'einfurchen', not to ¹kar-; the semantics ('draw a circle around' → compass) fit Nourai's gloss well, but the root is a different one.\",\n  \"derivation_fa\": \"استوارترین جزء این گره «haša-kərəta» است: بارتولمه در «افزوده‌ها بر فرهنگ ایرانی باستان» ص ۳۸ برای hašāgērd فارسی میانهٔ مانوی «شاگرد» صورت ایرانی باستان *hašā-karta- را می‌گذارد، یعنی «آن‌که به خدمت و همراهی همکار روحانی گماشته شده»، از *haxay- «دوست، همراه» (که ارجاع نورایی به Sekw = *sekʷ- «پیروی کردن» به همان اشاره دارد) + karta- «ساخته»؛ و در ص ۲۴۲ همان کتاب آن را به ستون ۱۷۴۴ فرهنگ ایرانی باستان ذیل haxay- و به haxāmaniš- پارسی باستان پیوند می‌زند. «هنکار / hankārayemi / hankərəθa-» نیز اوستایی اصیل است (یسنه ۱٫۱ و ویسپرد ۱٫۱: nivaēδayemi hankārayemi) و بارتولمه آن را ذیل ¹kar- «کردن» می‌آورد با این یادداشت که «ترجمهٔ پهلوی: hangārtanem، قس فارسی نو انگاردن» — یعنی دقیقاً همان پیکان نورایی. اما این جای‌دهی محل اختلاف است: نیبرگ در واژه‌نامهٔ خود hankārayemi را به ²kar- «به یاد آوردن، یاد کردن» می‌برد و صریح می‌نویسد «نه از ¹kar- چنان‌که بارتولمه دارد»، و هرن (شمارهٔ ۱۲۳) با علامت پرسش می‌نویسد «سنسکریت ۲√kar «گدنکن» (؟)». چونگ (۲۰۰۷) دوباره به رأی بارتولمه بازمی‌گردد و hangār- فارسی میانه را ذیل *kar «کردن» می‌آورد. سست‌ترین جزء «pairi-kara» است: صورت گواهی‌شدهٔ اوستایی pairi.kārayōiš (وندیداد ۱۳٫۶) «گرداگرد شیار بکش» است که بارتولمه آن را به ⁴kar- «شیار کشیدن» می‌دهد نه به ¹kar-. معنا با «پرگار» جور است، ولی ریشه دیگری است.\",\n  \"sources\": [U_SHAG],\n  \"ref_check\": [\n    {\"ref\": \"ZAW:38\", \"status\": \"supports\",\n     \"note\": \"Bartholomae, ZAW p.38 (leaf 61): 'hašāgērd (Müller gīrd) ‚discipulus‘ 30, 32 … setze ich uriran. *hašākarta- an, d. i. eigentlich ‚der mit der Wartung, dem Dienst des Priesterkollegen oder Priesterkollegiums zu tun hat‘, eine Zusammensetzung aus *haxay- (jAw. …)'.\"},\n    {\"ref\": \"ZAW:242\", \"status\": \"supports\",\n     \"note\": \"Same book p.242 (leaf 265): 'Sp. 1744, Z. 33 und 43 ff. füge in den Noten zu jaw. haxay- ‚Freund‘ und zu ap. haxāmaniš- EN. hinzu: Vgl. mpT. hašāgērd, np. šāgird ‚Schüler‘. S. oben S. 38 f., 158 f. und 226.' — confirms Nourai's ☞Sekw cross-reference.\"},\n    {\"ref\": \"HRN:28\", \"status\": \"supports\",\n     \"note\": \"Horn no. 123, p.28 (HRN.txt leaf 49): 'engārden ‚glauben, wähnen‘, engāšten … aw. hankārayemi, hankərəθa-, hankərəti- ‚Zählung‘ (Geldner, KZ. 27, 239 Note 1); phlv. angārtan, angārttan ‚glauben, zählen‘' — Nourai's two Avestan forms verbatim, though Horn adds 'ai. 2 √kar- ‚gedenken‘ (?)'.\"},\n    {\"ref\": \"HRN:232\", \"status\": \"supports\",\n     \"note\": \"Horn no. 1036/1038, p.232 (leaf 253): 'nigāšten ‚malen‘ … Causativum zu nigerīden'; '1038. nigerīden ‚betrachten‘ … Wohl zu derselben Wurzel wie aw. hankārayēmi, siehe np. engārden (No. 123)' — covers the chart's extra words نگاریدن/نگاشتن/نگریستن.\"},\n    {\"ref\": \"HUB:39\", \"status\": \"supports\",\n     \"note\": \"Hübschmann, Persische Studien p.39 (HUB.txt leaf 49), note 301: 'Np. pargāl = pargār ‚Zirkel‘ (afgh. pargār ‚Zirkel‘) stellt de Lagarde (Btrg. zur bactr. Lexic. p. 54) nebst pargar ‚Halskette‘ zu zd. pairi-kara- vd. 17, 6 = ‚Furche‘ (phl. pērāmūn-kārišnīh) und vergleicht skr. parikara- ‚Gürtel‘. Unsicher.' Nourai's own NOTE on the chart reports this uncertainty correctly, and the two glosses 'compass, necklace' come straight from this passage.\"},\n    {\"ref\": \"BQT:173\", \"status\": \"supports\",\n     \"note\": \"Borhan-e Qāṭeʿ ed. Moʿin, vol. 1, printed p. c.171-173 (BQT_v1_pages.txt \\\\f-leaves 391-392, running head «انگارده»): the انگاردن / انگاره / انگاریدن / انگاشتن cluster, cross-referenced 'رك: انگاردن'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"AiW col. 448 (¹kar-, 'mit ham') and cols. 449-450 (²kar- 'gedenken', ⁴kar- 'einfurchen')\", \"stance\": \"partial\",\n     \"note\": \"Under ¹kar-: 'mit ham ‚für Jemanden (Dat., Gen.) es (näml. den Yasna) vollziehen‘: nivaēδayemi hankārayemi … ahurahe mazdā … Y.1.1 ff., Vr.1.1 ff., F.34', footnote 21 'Pü.: hangārtanem (vgl. np. angārdan)'. Under ⁴kar- 'einfurchen': 'mit pairi ‚ringsum einfurchen‘: xšaθrāi vairyā pairi.karəm pairi.kārayōiš … V.13.6' — so pairi-kar belongs to a different kar- in Bartholomae.\"},\n    {\"src\": \"NYB\", \"where\": \"Glossary s.v. ²kartan (NYB_vol2_glossary.txt l.2241)\", \"stance\": \"contradicts\",\n     \"note\": \"'Av. (448) ²kar- ‚to recollect, to mention, to commend‘ [from which in all probability ham + the caus. in the set phrase nivaēδayemi hankārayemi ‚I consecrate, I dedicate‘ (not from ¹kar- as Bthl. has it)] … V. ²kartak, kartāreh, hangartan, nikeriδ, nikeritan, patkārītan, uskartan.'\"},\n    {\"src\": \"CHEUNG\", \"where\": \"s.v. *kar, Middle Persian section\", \"stance\": \"supports\",\n     \"note\": \"'(+ *ham-) MMP hngʾr- (orig. caus.) ‚to (ac)count, reckon‘, BMP hngʾl- /hangār-/ ‚to perform, offer (thanks); calculate, determine; consider‘' — filed under *kar 'to do, make' < PIE *kʷer-, i.e. Bartholomae's and Nourai's placement.\"},\n    {\"src\": \"MON\", \"where\": \"en.wiktionary.org/wiki/شاگرد (archived)\", \"stance\": \"supports\",\n     \"note\": \"'From Middle Persian hšʾklt’ /hašāgird/ ‚disciple, pupil‘, from Proto-Iranian *hašā-kr̥táh-, first element *hu-šāk- … from PIE *sekʷ- ‚to follow‘, second element PII *kr̥tás ‚done, made‘' (citing Rastorgujeva–Edelʹman 2007).\"}\n  ]},\n\n {\"id\": 7, \"lang\": \"Persian\", \"words\": \"engârdan; šâgerd; pargâr\", \"verdict\": \"plausible\",\n  \"derivation\": \"šāgerd شاگرد is confirmed: NP šāgird < MP (Manichaean) hašāgērd, Book Pahlavi hšʾklt' 'disciple' < PIr *hašā-kṛta-; the initial ha- was lost in New Persian while Armenian kept it in the loan ašakert, and Bartholomae remarks that the Manichaean spelling shows the -š- is etymological. engārdan انگاردن (with engāštan, engār) is MP hangārdan/hangārtan 'to reckon, consider' < *ham-kāraya-, the causative of kar- with the preverb ham- 'together'; ham- > han- > an-/en- before the velar, and the Pahlavi translators use hangārtanem precisely to render Av. hankārayemi (AiW col. 448 n.21). The same stem gives the chart's extra words nigāštan/nigāridan/nigār (< *ni-kāraya- 'to draw, paint') and nigaristan/nigarīdan (< *ni-kar-), for which Moʿin's footnote in Borhan p.2164 refers explicitly to 'ریشهٔ این کلمه در اوستایی hankārayemi، فارسی نگاردن، دیده می‌شود … از kar، بارتولمه ۴۴۸'. pargār پرگار is the least secure: Wiktionary reconstructs PIr *pari- 'around' + *kar-, comparing Skt. prakāra- and Kurdish pergal, which supports Nourai; but the Avestan pairi.kārayōiš he leans on belongs to Bartholomae's ⁴kar- 'to furrow', and Hübschmann, whom Nourai's own NOTE cites, ends his discussion with a flat 'Unsicher'. The chart's third gloss for pargār, 'fortune', is not supported by any source consulted; 'necklace' comes from Hübschmann's pargar 'Halskette'.\",\n  \"derivation_fa\": \"«شاگرد» تأییدشده است: فارسی نو šāgird از فارسی میانهٔ مانوی hašāgērd و پهلوی کتابی hšʾklt' «شاگرد، پیرو» از *hašā-kṛta- ایرانی باستان؛ هجای آغازین ha- در فارسی نو افتاده ولی وام‌واژهٔ ارمنی ašakert آن را نگه داشته و بارتولمه یادآور می‌شود که املای مانوی نشان می‌دهد ش در آن ریشه‌ای است. «انگاردن» (با انگاشتن و انگار) از فارسی میانهٔ hangārtan «شمردن، پنداشتن» از *ham-kāraya-، صورت سببیِ ریشهٔ kar با پیشوند ham- «باهم»؛ ham- پیش از همخوان کامی به han- و سپس an-/en- بدل شده، و مترجمان پهلوی دقیقاً hangārtanem را در برابر hankārayemi اوستایی نهاده‌اند (فرهنگ ایرانی باستان، ستون ۴۴۸، حاشیهٔ ۲۱). از همین ستاک واژه‌های افزودهٔ نمودار نیز آمده‌اند: نگاشتن/نگاریدن/نگار از *ni-kāraya- «کشیدن، نگاشتن» و نگریستن/نگریدن از *ni-kar-؛ حاشیهٔ معین بر برهان ص ۲۱۶۴ صریح می‌گوید «ریشهٔ این کلمه در اوستایی hankārayemi، فارسی نگاردن، دیده می‌شود … از kar، بارتولمه ۴۴۸». «پرگار» کم‌استوارترین است: ویکی‌واژه *pari- «پیرامون» + *kar- بازسازی می‌کند و prakāra- سنسکریت و pergal کردی را هم‌ریشه می‌گیرد که مؤید نورایی است؛ اما صورت اوستایی pairi.kārayōiš که تکیه‌گاه اوست از ⁴kar- «شیار کشیدن» بارتولمه است، و هوبشمان — که خودِ یادداشت نمودار به او ارجاع می‌دهد — بحث را با «نامطمئن» به پایان می‌برد. معنی سومِ «بخت» برای پرگار در هیچ منبعی که دیدیم پشتیبانی ندارد؛ «گردن‌بند» از pargar «Halskette» هوبشمان آمده است.\",\n  \"sources\": [U_SHAG, U_PARG],\n  \"ref_check\": [\n    {\"ref\": \"BQT:173\", \"status\": \"supports\",\n     \"note\": \"Borhan-e Qāṭeʿ ed. Moʿin vol. 1, printed p. c.171-173 (BQT_v1_pages.txt leaves 391-392): the انگاردن cluster — 'انگاره … هر چیز که افسانه و سرگذشت باشد … انگاریدن، بمعنی تصور کردن و پنداشتن و گمان بودن باشد … انگاشتن، بمعنی تصور کردن و پنداشتن و گمان بردن باشد'.\"},\n    {\"ref\": \"BQT:2164\", \"status\": \"supports\",\n     \"note\": \"Borhan p.2164 (vol. 4, pdf p.247) s.v. نگریدن, Moʿin's footnote 1: 'از: نگر (ریشه) + یدن (پسوند مصدری)، انگرستن، نگریستن. پهلوی nikirīt … هوبشمان ۱۶۳۸. ریشهٔ این کلمه در اوستایی hankārayemi، فارسی نگاردن، دیده می‌شود … از kar (بخاطر آوردن، ذکر کردن) «بارتولمه ۴۴۸»' — exactly the link Nourai draws from han-kar to the نگار- family.\"},\n    {\"ref\": \"BQT:2157\", \"status\": \"not_found\",\n     \"note\": \"Borhan p.2157 (vol. 4, pdf p.240) is the نفیر / نقاب / نقد page; the نگار entry stands on p.2162 and نگاشتن on p.2163 in this printing, so Nourai's 2157 is about five pages short of the material he means (the نگار cluster).\"},\n    {\"ref\": \"ZAW:38\", \"status\": \"supports\",\n     \"note\": \"ZAW p.38: 'hašāgērd … ‚discipulus‘ … aber im Np. wird شاگرد šāgird gesprochen … setze ich uriran. *hašākarta- an'.\"},\n    {\"ref\": \"ZAW:242\", \"status\": \"supports\",\n     \"note\": \"ZAW p.242: 'Vgl. mpT. hašāgērd, np. šāgird ‚Schüler‘' added to the notes on jAw. haxay- 'Freund' and OP haxāmaniš-.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"HRN\", \"where\": \"no. 123, p.28; no. 900 footnote, p.201\", \"stance\": \"partial\",\n     \"note\": \"no. 123 supports engārden < aw. hankārayemi, phlv. angārtan (Ossetic anḳaryn, Armenian loan angarem); the footnote to no. 900 records that 'Hübschmann stellt a. a. O. auch zweifelnd np. šāgird ‚Schüler‘ (arm. LW. ašakert, phlv. ašōkart) hierher' — i.e. to the -gird/*kṛta- family, as Nourai does.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"s.v. *kar, NWIr. section\", \"stance\": \"supports\",\n     \"note\": \"'(+ *ham-) NP ingāštan/ingar- ‚to suppose; consider, believe‘, angārīdan/angār- ‚to think, imagine, estimate; to paint, figure‘ … NP angārah ‚revenue-book, cash-account‘; (+ *ni-) NP nigāštan/nigār- ‚to paint‘' — all under *kar < PIE *kʷer-.\"},\n    {\"src\": \"HUB\", \"where\": \"Persische Studien p.39, note 301\", \"stance\": \"partial\",\n     \"note\": \"de Lagarde's derivation of pargār from zd. pairi-kara- is reported and then judged 'Unsicher' — the very caveat printed in the chart's NOTE, which is therefore accurate.\"},\n    {\"src\": \"MON\", \"where\": \"en.wiktionary.org/wiki/پرگار (archived)\", \"stance\": \"supports\",\n     \"note\": \"'From Proto-Iranian, from Proto-Indo-Iranian. Cognate with Sogdian …, Northern Kurdish pergal, Sanskrit प्रकार (prakāra)': first element PIr *pari- 'around' < PIE *per-, second the root *kar-.\"}\n  ]}\n]\n\njson.dump(e2, open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/e2.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)\nprint(\"ok e2\", len(e2[\"nodes\"]))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk292b.py"
}
```


### [2026-09-06T22:33:57.020Z] TOOL RESULT

```
ok e2 7
```


## [2026-09-06T22:34:04.465Z] TOOL CALL #90: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json\nS='/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/'\ne0=json.load(open(S+'e0.json',encoding='utf-8'))\ne2=json.load(open(S+'e2.json',encoding='utf-8'))\nout={\"pdf_page\":292,\"book_page\":262,\"verified_by\":\"claude-opus-5\",\"verified_on\":\"2026-09-06\",\"entries\":[e0,e2]}\nwith open('data/verification/page-292.json','w',encoding='utf-8') as f:\n    json.dump(out,f,ensure_ascii=False,indent=1)\n    f.write('\\n')\nprint('written')\nEOF\npython3 -m json.tool data/verification/page-292.json > /dev/null && echo \"valid json\"\npython3 tools/verify_check.py 292"
}
```


### [2026-09-06T22:34:06.414Z] TOOL RESULT

```
written
valid json
nodes verified: 11/11
node verdicts: {'confirmed': 4, 'disputed': 4, 'plausible': 3}
root verdicts: {'transcription_suspect': 1, 'confirmed': 1}
ref checks: {'supports': 27, 'not_found': 2, 'not_checked': 3}
books consulted: {'supports': 19, 'partial': 9, 'silent': 1, 'contradicts': 6} | by book: {'HRN': 7, 'MON': 7, 'WLD': 4, 'BRT': 4, 'CHEUNG': 4, 'KNT': 2, 'NYB': 2, 'POK': 1, 'FFD': 1, 'PHD': 1, 'SYN': 1, 'HUB': 1}
```


## [2026-09-06T22:34:13.158Z] TOOL CALL #91: Bash

```json
{
 "command": "python3 -c \"\nimport json,glob,collections\nc=collections.Counter()\nfor f in glob.glob('data/verification/page-2[0-9][0-9].json'):\n    d=json.load(open(f))\n    for e in d['entries']:\n        for n in e.get('nodes',[]):\n            for x in n.get('consulted') or []: c[x.get('src')]+=1\nprint(c.most_common(30))\""
}
```


### [2026-09-06T22:34:14.863Z] TOOL RESULT

```
[('KLN', 557), ('PHD', 258), ('MON', 256), ('POK', 221), ('AHD', 205), ('BRT', 202), ('SKT', 200), ('HRN', 195), ('WLD', 195), ('BQT', 173), ('LKT', 161), ('CHEUNG', 158), ('NYB', 149), ('HUB', 145), ('ARY', 136), ('Wiktionary', 132), ('IEC', 117), ('SYN', 97), ('LAT', 91), ('WEB', 84), ('KNT', 75), ('FSD', 67), ('PLA', 60), ('Etymonline', 57), ('AFM', 49), ('SOD', 49), ('FVQ', 41), ('HJB', 40), ('DEV', 39), ('BOOK', 25)]
```


## [2026-09-06T22:34:21.908Z] TOOL CALL #92: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json\np='data/verification/page-292.json'\nd=json.load(open(p,encoding='utf-8'))\nn=0\nfor e in d['entries']:\n    for nd in e.get('nodes',[]):\n        for c in nd.get('consulted') or []:\n            if c.get('src')=='MON' and 'wiktionary' in (c.get('where') or ''):\n                c['src']='Wiktionary'; n+=1\njson.dump(d,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)\nopen(p,'a',encoding='utf-8').write('\\n')\nprint('renamed',n)\nEOF\npython3 tools/verify_check.py 292"
}
```


### [2026-09-06T22:34:24.177Z] TOOL RESULT

```
renamed 7
nodes verified: 11/11
node verdicts: {'confirmed': 4, 'disputed': 4, 'plausible': 3}
root verdicts: {'transcription_suspect': 1, 'confirmed': 1}
ref checks: {'supports': 27, 'not_found': 2, 'not_checked': 3}
books consulted: {'supports': 19, 'partial': 9, 'silent': 1, 'contradicts': 6} | by book: {'HRN': 7, 'Wiktionary': 7, 'WLD': 4, 'BRT': 4, 'CHEUNG': 4, 'KNT': 2, 'NYB': 2, 'POK': 1, 'FFD': 1, 'PHD': 1, 'SYN': 1, 'HUB': 1}
```


## [2026-09-06T22:34:27.969Z] TOOL CALL #93: Bash

```json
{
 "command": "ls -la data/verification/sources/refs/ocr/BOOK/292.png data/verification/page-292.json; git status --short | head -30"
}
```


### [2026-09-06T22:34:28.025Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb  67889 Sep  6 18:34 data/verification/page-292.json
-rw-rw-r-- 1 sfmqrb sfmqrb 103438 Sep  6 18:24 data/verification/sources/refs/ocr/BOOK/292.png
 M data/verification/page-292.json
```


## [2026-09-06T22:34:32.911Z] TOOL CALL #94: Bash

```json
{
 "command": "git log --oneline -5 && git diff --stat data/verification/page-292.json && git show HEAD --stat | head -20"
}
```


### [2026-09-06T22:34:33.018Z] TOOL RESULT

```
7bdd5bc Verify page 290 (Kwek/čašm, čašidan; Kwel part 1/čarx, bâzâr, čâlâk)
c41cf5c Verify page 291 (Kwel part 2/telesm, kâleskeh, cycle, wheel, colony; Kwen 1/esfand, gusfand)
e518449 Verify page 294 (Kwes/šoš, havâ, cyst, wheeze)
6eb2c4c Verify page 289 (Kwei 1/kin, punish; Kwei 2/čidan, gozidan, tuzidan, poem); fix Labibi quote
e74777e Verify page 287 (Kŭr/kur; Kurkanŭ/korkom, curcuma; Kurkizannu/kargadan); restore Kâl root line
 data/verification/page-292.json | 14 +++++++-------
 1 file changed, 7 insertions(+), 7 deletions(-)
commit 7bdd5bc17e9d706ca306a44dac94675fb32a0d65
Author: Sajad F. Maghrebi <sajad.faghfoor@gmail.com>
Date:   Sun Sep 6 18:34:12 2026 -0400

    Verify page 290 (Kwek/čašm, čašidan; Kwel part 1/čarx, bâzâr, čâlâk)
    
    Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>
    Claude-Session: https://claude.ai/code/session_016LcfU5CW3NBdZnsbF2dByz

 data/verification/page-290.json                 |  896 ++++
 data/verification/page-292.json                 |  629 +++
 data/verification/process/verify-page-290.jsonl |  388 ++
 data/verification/process/verify-page-290.md    | 5996 +++++++++++++++++++++++
 4 files changed, 7909 insertions(+)
```


## [2026-09-06T22:34:56.417Z] AGENT

Done. `verify_check.py 292` reports **0 PROBLEM lines** (11/11 nodes).

**Page 292 (book p. 262) — verdicts**
- Roots: 1 confirmed (Kwer), 1 transcription_suspect (Kwen 2)
- Nodes: 4 confirmed, 3 plausible, 4 disputed
- Ref checks: 27 supports, 2 not_found, 3 not_checked · 35 `consulted` entries across 12 books

**transcription_suspect**
- ROOT `Kwen 2` "sip, swallow" — the root is Pokorny's **k̯em-** (IEW 640 f.; Walde-Pokorny I 514 qʷem-), i.e. **Kwem**, not Kwen. Gloss, language and POK:640 are all correct; only the final letter is wrong. `error_in: book` — the printed page 262 itself shows "Kwen 2" (image saved to `data/verification/sources/refs/ocr/BOOK/292.png`), so the extraction is faithful. Watkins/AHD has no kʷen- 'sip', only kʷen- 'holy' (Pok. 630) = Nourai's own Kwen 1 on p. 291.

**disputed**
- Kwer #1 `aiwiš-kar` "hunt" (and #3 `šekâr`) — Cheung 2007 p.345 puts hunting under a separate, purely Iranian root *skar ("exclusively Ir.; no reliable IE cognates"), Wiktionary follows him (possible Sogdian loan); and Horn no. 786, Nourai's own authority, says the *aiwiš+kar analysis is "gewiss nicht zu √kar- 'tun, machen'".
- Kwer #2 `kahr-mân / qahramân` — modern view: MP **kārframān** "manager" (kār + framān) → Aramaic → Arabic qahramān. Nourai's *kara-manah "wise at work" faithfully reproduces his cited source (Moʿin's footnote in Borhan p.1549, after Dozy), but not current scholarship.
- Kwer #5 `-vard` and `Lâjvard` — Horn p.201 (the page Nourai cites) explicitly excludes -verd (Abīverd): "kann nur auf ap. *varta- zurückgehen", not *kṛta-; and لاجورد is the Badakhshan mine-name Lāžvard, second element PIr *varta- "stone" (Bailey), not "-vard = town" + a Turkish tribe. The -gard/-jerd and Yazdgerd items in the same node are confirmed (BQT 1787, 2432; Wiktionary "made by God").

**Nothing needs fixing in the extraction** — the JSON matches the printed page everywhere I checked, including the odd Avestan form `yazato-karteta` (book's own loose transliteration for *yazata-kṛta-) and the root name `Kwen 2`.

Ref-page notes for the owner: **BQT:2157** is the نفیر/نقاب page — the نگار cluster Nourai means stands at 2162–2164 in the Ibn Sina/Amir Kabir pagination; **BQT:1617** carries the کر- entries, not کاریدن/کردن. **AHM:184** is one page off (the *čam- passage is in note 32² on p. 183). MON:2057/3426 and DMO:115 were not checkable (no matching edition on disk).
