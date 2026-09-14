# Verification process log — verify-page-474


## [2026-09-14T02:28:09.895Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 474 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-474.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-474.json. Write /home/sfmqrb/git/rishe/data/verification/page-474.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 474` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T02:28:10.983Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T02:28:11.889Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T02:28:11.903Z] TOOL RESULT

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


## [2026-09-14T02:28:12.449Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-474.txt"
}
```


### [2026-09-14T02:28:12.472Z] TOOL RESULT

```
1	=== PDF page 474 (book page 444) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Stâ, Stha, Stâk : to stand  (refs POK:1008,1009)  PART 1
4	#1 (parent #0) [Avestan / Old Persian] refs=BQT:123; HRN:20; POK:1008 | sta 1 : to stand, to set ; stâ 1, stata, šta 1, šti
5	  #2 (parent #1) [Persian] refs=BQT:289,1097; HRN:20 | - stân «- ستان» : location of, center of ; bağstân «بغستان» : location (mountain) of god ☞Bhag ; setâk «سیتاک» : branch | extra: بیستون ؛ سیتاخ ، استاک ، إستاخ
6	#3 (parent #0) [Avestan / Old Persian] refs=BQT:123; HRN:20; POK:1008; KNT:210 | adi-sta : in standing ☞En ; tap-stana : place (time) of heat ☞Tep ; â-stana : entrance ; stuna, stůnâ : column, pillar
7	  #4 (parent #3) [Sogdian] refs=SOD:67 | `st`wn` : pillar
8	  #5 (parent #3) [Persian] refs=BQT; MON | îstâdan «ایستادن» ; tâbestân «تابستان» : "heat season" ; âstân «آستان» : entrance ; sotůn «ستون» : pillar | extra: استان ، ستاد ؛ آستانه ؛ اُستُن
9	#6 (parent #0) [Avestan] refs=KLN:1222; POK:1008; SYN:1376; SOD:439 | ava-stata, hvô-îstâ : standing in front (of students) ; fra-sta : "stand forward", send ☞Per 1 ; fra-aiš, fraěšta : "sent forward" ☞Per 1 ; par-šta : [stand around], worship ☞Per 1 ; par-šti : "stand up", back ☞Per 1 ; â-x-stâ, axštî : put in place, put in peace
10	  #7 (parent #6) [Persian] refs=BQT:1463; HRN:66,182 | ostâd «استاد» : teacher ; ferestâdan «فرستادن» : send ; parastîtan «پرستیدن» : worship" ; pošt «پشت» : back ; âštî «آشتی» : peace | extra: فرشته ؛ پرستار
11	#8 (parent #0) [Old Persian] refs=KNT:210 | ava-stâ : set down, restore ; ni-stâ, ništâ : command
12	#9 (parent #0) [Avestan] refs=POK:1009,1011; KLN:1508; HRN:205 | sta-xra : firm, hard ; sta-xma, sta-mba : hardship, cruelty ; vi-stâ-ka : harsh, rude ☞Wi ; stůra : thick, large, husky
13	  #10 (parent #9) [Persian] refs=HRN:158-9,205; BQT:1099,1816 | estaxr «استخر» : "firm" ; setam «ستم» : "hardship" ; gostâx «گستاخ» : "hard mannered" ; sotorg «سُترگ» : "large and strong" | extra: اُستاخ
14	#11 (parent #0) [Avestan] refs=POK:866; MON:191; AVG:237; LEW:904 | ratha-eštra : "standing on a chariot", warrior ☞Ret
15	  #12 (parent #11) [Persian] refs=BQT:97, 1895; ARB:203 | arteštâr «ارتشتار» : soldier ; laškar «لشکر» : army | extra: ارتش ؛ عسکر
16	
```


## [2026-09-14T02:28:15.518Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-474.json",
 "description": "Read source JSON for page 474"
}
```


### [2026-09-14T02:28:15.559Z] TOOL RESULT

```
{
  "pdf_page": 474,
  "book_page": 444,
  "entries": [
    {
      "root": {
        "name": "Stâ, Stha, Stâk",
        "lang": "Indo-European",
        "refs": "POK:1008,1009",
        "gloss": "to stand"
      },
      "part": 1,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "BQT:123; HRN:20; POK:1008",
          "words": [
            {
              "translit": "sta 1",
              "gloss": "to stand, to set",
              "script": null
            },
            {
              "translit": "stâ 1, stata, šta 1, šti",
              "gloss": null,
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
          "refs": "BQT:289,1097; HRN:20",
          "words": [
            {
              "translit": "- stân",
              "gloss": "location of, center of",
              "script": "- ستان"
            },
            {
              "translit": "bağstân",
              "gloss": "location (mountain) of god",
              "script": "بغستان",
              "see": [
                "Bhag"
              ]
            },
            {
              "translit": "setâk",
              "gloss": "branch",
              "script": "سیتاک"
            }
          ],
          "script_extra": "بیستون ؛ سیتاخ ، استاک ، إستاخ",
          "note": null,
          "quote": {
            "text": "سوسن لطیف و شیرین چون خوشه های سیمین - شاخ و ستاک نسرین چون برج ثور و جوزا",
            "poet": "Kasâî Marvzî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "BQT:123; HRN:20; POK:1008; KNT:210",
          "words": [
            {
              "translit": "adi-sta",
              "gloss": "in standing",
              "script": null,
              "see": [
                "En"
              ]
            },
            {
              "translit": "tap-stana",
              "gloss": "place (time) of heat",
              "script": null,
              "see": [
                "Tep"
              ]
            },
            {
              "translit": "â-stana",
              "gloss": "entrance",
              "script": null
            },
            {
              "translit": "stuna, stůnâ",
              "gloss": "column, pillar",
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
          "lang": "Sogdian",
          "refs": "SOD:67",
          "words": [
            {
              "translit": "`st`wn`",
              "gloss": "pillar",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 3,
          "lang": "Persian",
          "refs": "BQT; MON",
          "words": [
            {
              "translit": "îstâdan",
              "gloss": null,
              "script": "ایستادن"
            },
            {
              "translit": "tâbestân",
              "gloss": "\"heat season\"",
              "script": "تابستان"
            },
            {
              "translit": "âstân",
              "gloss": "entrance",
              "script": "آستان"
            },
            {
              "translit": "sotůn",
              "gloss": "pillar",
              "script": "ستون"
            }
          ],
          "script_extra": "استان ، ستاد ؛ آستانه ؛ اُستُن",
          "note": null,
          "quote": {
            "text": "کنون پندار مُردم ، آشتی کن - که در تسلیم ، ما چون مردگانیم",
            "poet": "Molavî"
          }
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Avestan",
          "refs": "KLN:1222; POK:1008; SYN:1376; SOD:439",
          "words": [
            {
              "translit": "ava-stata, hvô-îstâ",
              "gloss": "standing in front (of students)",
              "script": null
            },
            {
              "translit": "fra-sta",
              "gloss": "\"stand forward\", send",
              "script": null,
              "see": [
                "Per 1"
              ]
            },
            {
              "translit": "fra-aiš, fraěšta",
              "gloss": "\"sent forward\"",
              "script": null,
              "see": [
                "Per 1"
              ]
            },
            {
              "translit": "par-šta",
              "gloss": "[stand around], worship",
              "script": null,
              "see": [
                "Per 1"
              ]
            },
            {
              "translit": "par-šti",
              "gloss": "\"stand up\", back",
              "script": null,
              "see": [
                "Per 1"
              ]
            },
            {
              "translit": "â-x-stâ, axštî",
              "gloss": "put in place, put in peace",
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
          "refs": "BQT:1463; HRN:66,182",
          "words": [
            {
              "translit": "ostâd",
              "gloss": "teacher",
              "script": "استاد"
            },
            {
              "translit": "ferestâdan",
              "gloss": "send",
              "script": "فرستادن"
            },
            {
              "translit": "parastîtan",
              "gloss": "worship\"",
              "script": "پرستیدن"
            },
            {
              "translit": "pošt",
              "gloss": "back",
              "script": "پشت"
            },
            {
              "translit": "âštî",
              "gloss": "peace",
              "script": "آشتی"
            }
          ],
          "script_extra": "فرشته ؛ پرستار",
          "note": null,
          "quote": {
            "text": "کنون پندار مُردم ، آشتی کن - که در تسلیم ، ما چون مردگانیم",
            "poet": "Molavî"
          }
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "KNT:210",
          "words": [
            {
              "translit": "ava-stâ",
              "gloss": "set down, restore",
              "script": null
            },
            {
              "translit": "ni-stâ, ništâ",
              "gloss": "command",
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
          "lang": "Avestan",
          "refs": "POK:1009,1011; KLN:1508; HRN:205",
          "words": [
            {
              "translit": "sta-xra",
              "gloss": "firm, hard",
              "script": null
            },
            {
              "translit": "sta-xma, sta-mba",
              "gloss": "hardship, cruelty",
              "script": null
            },
            {
              "translit": "vi-stâ-ka",
              "gloss": "harsh, rude",
              "script": null,
              "see": [
                "Wi"
              ]
            },
            {
              "translit": "stůra",
              "gloss": "thick, large, husky",
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
          "lang": "Persian",
          "refs": "HRN:158-9,205; BQT:1099,1816",
          "words": [
            {
              "translit": "estaxr",
              "gloss": "\"firm\"",
              "script": "استخر"
            },
            {
              "translit": "setam",
              "gloss": "\"hardship\"",
              "script": "ستم"
            },
            {
              "translit": "gostâx",
              "gloss": "\"hard mannered\"",
              "script": "گستاخ"
            },
            {
              "translit": "sotorg",
              "gloss": "\"large and strong\"",
              "script": "سُترگ"
            }
          ],
          "script_extra": "اُستاخ",
          "note": null,
          "quote": {
            "text": "چو بشنید پیغام شاه بزرگ - زمین را ببوسید سام سترگ",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 11,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:866; MON:191; AVG:237; LEW:904",
          "words": [
            {
              "translit": "ratha-eštra",
              "gloss": "\"standing on a chariot\", warrior",
              "script": null,
              "see": [
                "Ret"
              ]
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
          "refs": "BQT:97, 1895; ARB:203",
          "words": [
            {
              "translit": "arteštâr",
              "gloss": "soldier",
              "script": "ارتشتار"
            },
            {
              "translit": "laškar",
              "gloss": "army",
              "script": "لشکر"
            }
          ],
          "script_extra": "ارتش ؛ عسکر",
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-14T02:28:16.571Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo ---- && cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "List verification dir and read source matrix"
}
```


### [2026-09-14T02:28:16.665Z] TOOL RESULT

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
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt` (truncated before the lexicon's h–z section, ~p. 208 on)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT_full.txt` (complete archive.org djvu text — use this for lexicon pages 208–215: haumavarga-, siyamam, etc.)
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


## [2026-09-14T02:28:23.055Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','HRN','KNT','BQT','SOD','KLN','SYN','MON','AVG','LEW','ARB','PHD','NYB','BRT','HUB','CHEUNG','WLD','AHD','IEC','ARY','SKT']:\n    v=d.get(k)\n    print('==',k, json.dumps(v,ensure_ascii=False)[:900])\n\"",
 "description": "Show ref metadata for relevant abbreviations"
}
```


## [2026-09-14T02:28:23.829Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n 1,60p data/verification/page-385.json",
 "description": "Look at a recent verification file for format"
}
```


### [2026-09-14T02:28:23.999Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.", "notes": "OCR of German Fraktur-free text is decent; Persian
== KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; sec
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c
== SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}", "loca
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based l
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept head
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati
== AVG {"title": "A. V. W. Jackson, An Avesta Grammar in Comparison with Sanskrit, Part I, Stuttgart 1892", "edition_found": "1892", "kind": "archive_djvu", "url": "https://archive.org/details/pt1avestagrammar00jackuoft", "identifier": "pt1avestagrammar00jackuoft (also an-avesta-grammar-in-comparison-with-sanskrit, in.ernet.dli.2015.47742)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AVG.txt", "page_offset": "leaf = printed + 54 (e.g. leaf 61 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Grammar by numbered §; grep the § number or Avestan word.", "notes": ""}
== LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Latin headword in bold at line start. For 1938 pagination borrow lateinischesetym0000awal.", "notes": ""}
== ARB {"title": "al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edition)", "kind": "archive_djvu", "url": "https://archive.org/details/mo3rb (probably the Shakir edition) ; https://archive.org/details/almo3rab_gwaliqy_f_abduraheem (F. 'Abd al-Rahim ed., Damascus 1990) ; also uc1.aa0003615705 / AAlexandrina-148752 (Sachau's Leipzig 1867 ed.) ; text on shamela.ws", "lookup_hint": "Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_mo3rb.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_abdulraheem.txt"], "page_offset": null, "covers_etymology": true, "notes": "Arabic OCR fair."}
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsian
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.", "notes": " local_files: /home/sfmqrb/
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's BRT numbers are Bartholomae's COLUMN number
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.", "notes": "Built from djvu.xml (no hocr); OCR quality moderate.", "cites": "page number of Hübschmann, Persische Studien (1895)"
== CHEUNG null
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015.106625 (Band 3 duplicate)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: lea
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.", "notes": "", "cites": "column/page number of Mann, An Indo-Europea
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt"], "page_offset": "printed page = pdf page + 1
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.", "notes": "Nourai says '1882-1967'; the
```


### [2026-09-14T02:28:24.040Z] TOOL RESULT

```
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
          "stance": "silent",
          "note": "grep of IEC.txt for 'peg-', 'pokso-', 'pektos' returns no headword for this root."
        }
      ],
      "nodes": [
        {
          "id": 1,
          "lang": "Sanskrit",
          "words": "pakša",
          "verdict": "plausible",
          "derivation": "Sanskrit पक्ष (pakṣá-) m. is real and old (RV), but its meanings are 'wing, feather; side, flank; half (of a month); party, faction' — not 'breast'. Monier-Williams and Wiktionary give no 'breast' sense; the chart's 'breast' is imported from Nourai's root gloss. Formally pakṣa- goes back to Proto-Indo-Iranian *pakšás 'side, flank' < PIE *peg-/*pok-s-, with the regular Indo-Aryan treatment of *-ks- > -kṣ-; the Iranian cognate is Ossetic fæxs 'side'. So the arrow root -> Sanskrit is sound; only the gloss 'breast' is wrong.",
          "derivation_fa": "واژهٔ سنسکریت pakṣá- «بال، پر؛ پهلو، سو؛ نیمه (ماه)؛ دسته» از ریگ‌ودا به‌بعد گواهی شده است، اما معنای «سینه» برای آن ثبت نشده و نورایی آن را از معنای ریشه به این گره تسری داده است. از دید آوایی pakṣá- بازماندهٔ هندوایرانی آغازین *pakšás «پهلو، سو» است (خوشهٔ *-ks- در هندوآریایی به -kṣ- بدل می‌شود) و هم‌ریشهٔ آن در ایرانی، fæxs آسی به معنی «پهلو» است. بنابراین پیکان «ریشه ← سنسکریت» درست است و تنها معنای «سینه» نادرست است.",
          "sources": [
            "https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%95%E0%A5%8D%E0%A4%B7"
          ],
          "ref_check": [
            {
              "ref": "AHD",
              "status": "partial",
              "note": "Watkins 1985 s.v. peg-: '2. Possibly suffixed variant form *pek-so- in Sanskrit paksah, wing: PUNKA.' Watkins glosses the Sanskrit word 'wing' only, and marks the connection 'possibly'."
```


## [2026-09-14T02:28:29.296Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 242 243 244 245 246 247; do echo \"=== POK_03 leaf $n ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$((n+1))\"' {print}' POK_03.txt | head -20; done",
 "description": "Print Pokorny leaves around p.1008"
}
```


### [2026-09-14T02:28:30.363Z] TOOL RESULT

```
=== POK_03 leaf 242 ===
da.
WP.  II  684.
(s)pleigh-  ,die  Beine  spreizen*.
Ai.  *pUhate  ,geht,  bewegt  sich* ;  gr.  ftXlaao[.iaL  ,schreite  aus*,  i^TiXiaoo^at jklaffe  auseinander  (von  Wunden)*,  nXixdg  f.  ,die  Spreize,  Stelle  zwischen den  Schenkeln*,  OTÖna  ÖLarteTtlixög  »offenstehender  Mund* ;  mit  anl.  s-  wohl air.  sliassait  f.  ,Schenkel'  (*spleigh-s-ontl) ;  über  air.  lingid  ,springt*,  Prät. leblang-  (*ple-plong-?)'s.  Thurneysen  Gr.  §687. WP.  II  684.,  Pisani  Mel.  Boisacq  II,  181  ff.
1001
,  ^^QimTio-,  -ä  , Schaum,  Gischt*.
i'  ^i.  phina-  m.  ,Schaum,  Feim*;  osset.  fink,  ßnM  ds. ;  lat.  spüma  L Cßliaum,  Gischt',  pümex  m.  ^Bimsstein*  (von  seiner  schaumartig  porösen Beschaffenheit) ;
abd.  feim,   ags.  fäm   ^Feim^   Schaum*;   lit.   spdine  ^Schaumstreifen   auf ke^vegter  See^,   apr.   spoayno   , Schaum^  (*spdinä)j  aksl.   p^na  (russ.  pena^ skr.  pfli^^)  ^Schaum^ WP.  II  681,  WH.  II  388  f.,  580,  Trautmann  227  f.,  Vasmer  2,  334.
"   ^fßi'f  Spreu-,  s.  oben  S.  994  f.
jrt(i2)reig'-  ,strotzen,  prall  gespannt  sein';  vgl.  {s)p(h)ereg-.
Gr.  ocpQiydb)  ,strotze,  schwelle,  bin  in  voller  Lebenskraft,  bin  begierig, lüstern'  j(Tq)Qlyog  n.  ^strotzende  Fülle';  norw.  sprikja  ,ausspannen,  spreizen', iatr.  ,entspaQnt  sein,  strotzen,  schwellen',  schwed.  dial.  sprika  ,ausspannen'. WP.  II  683  f.
$r&kn-tO',  -ti-  , scharfkantig,  scharfe  Kante,  Ecke,  Felszacke'?
Ai.   srakti-    f.   , Zacke,    Ecke^,   av.    sraxti-y    -d-raxti-    ,Ecke,    Seite';    gr. {axTOi*  qxxgayysg  Hes.  neben  sekundärem  QÖcTtzaL  ds. WP.  II  702,  Schwyzer  Gr.  Gr.  1,  299.
srcbb-,  s^bh-  und  serbh-  , schlürfend
Arm.  arhi  (^sj-bh-)  ,ich  trank',  arb  , Zechgelage';  gr.  qoq)iw  (ion.  qvcpib}) jSchlürfe^  (auch  ^öcpeiv  EM.),  qoniög  ^geschlürft',  qöcprjy,a  (ion.  Qvcpr^fxa)  n., ^öcpog  m.  ,Brühe,  dicker  Trank';  alb.  gjerp  (*serbhö)  ,ich  schlürfe',  gjerbe ,Tropfen';  lat.  sorbeö,  -ere  , schlürfen';  mir.  srub  , Schnauze'  (*srobu-)]  lit. $rebiü,  sribti  ,schlürfen'  (auch  sriobiü,  sriaubiü,  vielleicht  auf  Grund  eines ^srubiu),  ablaut.  surbiü,  surbti  ,saugen,  schlürfen^,  lett.  surbju^  surbt  ,schlür- fen'  (-wr-Reduktionsstufe  zu  srobh-  oder  sorbh-?;  vgl.  auch  poln.  sarbac), lett.  strebju,  strebt  ,schlürfen,  auslöffeln',  streba  , etwas  zu  Schlürfendes; ein  Betrunkener' ;  urslav.  *serbjg^  *shrbati  , schlürfen',  mit  verschiedenen Ausgleichungen  in  sloven.  sr^bati,  cech.  strebati  usw. ;  vielleicht  auch  mhd. türpfeln,  sürfeln  , schlürfen',  isl.  sarpr  ,Kropf  der  Vögel',  aisl.  als  Spitz- name (,*Schlund'),  mit  germ.  p  aus  gemin.  pp]  auch  ndl.  slorpen,  sluipen, nhd.  schlürfen  mit  Z  nach  schlucken.
WP.  II  704,  716,  WH.  II  561  f.,  Trautmann  294,  Vasmer  2,  612;  W. Schulze  setzte  *s(u)erbh-j  *srubh-  an.
[•r-ecf22-,  sr-et-  , strudeln,  wallen,  brausen,  rauschen';  Erweiterg.  von  1.  se7^'.
Gr.  QÖd'og  m.  ,das  Wogenrauschen';,  äli-ggod^og  ,meerumrauscht',  raxv-
^^o-^OL  XöyoL  »schnell  dahinrauschende  Worte', 
=== POK_03 leaf 243 ===
 iniQQO&og  (und  iniTdgQo&og)
1002  '
, herbeisausend;  auch  von   Göttern:  zur  Hilfe',  gö-d-iog  ,brausend' ' gad-ayog'  idgaxog  Hes.;  vielleicht  auch  späteres  qco^cjv,  meist  PI. ^Nasenlöcher,  Nase^  als  Trivialausdruck  ,*Schnarcher,  Rassler* ;  da^ PL  ^Nasenlöcher,  Nase^-  vgl.  qtg,  ^ivög  f.  ;Nase'   als   ,die  Fließenc Wurzelform  *s7^ei- :  srl- ;
acorn.  stret  gl.  ,latex^,  mcorn.  streyth  ,Fluß^;  mir.  srithit  f.  ,Strilil  ^^ Milch  oder  Blut'  (*srt-nti)]  ahd.  stredan,  strad,  mhd.  streden  ,brtJ!!f strudeln,  kochen',  stredunga,  stridunga  , Aufwallung*,  mhd.  s^radem  ,Str*j3^ spät  mhd.  und  nhd.  Strudel.  ♦
WP.  II  704;  Fraenkel  Gl.  32,  81  f.;  Leumann  Hom.  Wörter  220.
{s)reigh-  (auch  (s)reikb-?)  , klettern,  mühsam  kriechen'?  '^'
Ai.  rihgati  (Media  in  Zusammenhang  mit  der  Nasalierung)  und  rihkk
jbewegt  sich  mühsam,  kriecht'  (von  Kindern);
gr.  diva-QQi%dof.iaL,  dQQLX(xo[.iai  ,mühselig  mit  Händen  und  Füßen  eian,
klettern*.
WP.  II  702,  Frisk  Gr.  Wb.  103.
srenk-  ^schnarchen'.  ^
Gr.  Qsyyio},  Qsyx^  , schnarche;  schnaube';  Qsyiiog  n.,  ^ey^tg  f.  ,Schnarch<?5 QÖyycog,  ^oyf.iög  ds. ;  air.  srennim  , schnarche'  (*srenk-nä-mi)'j  mir.  srSimm ^Schnarchen'  (*srenk-smn),  auch  srHmm  durch  Einfluß  von  srennim'^
einer  ähnlichen  Schallnachahmung  entspringt  wohl  gr.  ^vyxog  , Schwein rüssel,  Schnauze,  Schnabel' ;  ob  arm.  *rungn,  PI.  rngun-k,  rdngun-li  ,N«j|t löcher,  Nase'  daraus  entlehnt  oder  unter  idg.  *srungh-  damit  urverwftr^ sei,  ist  fraglich. WP.  II  705.
sreno-,  -ä  Körperteilbenennung,  etwa  ,Oberschenkel,  Lenden'.
Av.  räna-  m.  ,der  äußere  Teil   des   Oberschenkels,   OberschenkelVp»] np.  rän  , Schenkel';  lit.  strHos  ,die  Lenden,  das  Kreuz'. WP.  n  70Ö.
sresk'  ,tropfen'V
Av.  srask-  (srasca-)  ,triefen,  abtriefen  von ;  triefregnen',  sraska-  m.  (i sirisk)    ,Träne,  Weinen',    mp.    srixt   ,dropped',    arm.    srskel   {^srSsh- srösk-)  , besprengen' ;  Entlehnung  des  arm.  Wortes  aus  dem  Arischen die  Vorbedingung    für    die   Verbindung    von   av.    srask-,    arm.   srskti *klkk-skö-    mit   lit.    släkas    ,Tropfen',    §laketi    ,tröpfeln',    §lUti  ,spriti6S*i (s.  oben  S.  607  hleu-  ,spülen').  *  ■-
WP.  II  602  f.,  705.  4.
1003
=== POK_03 leaf 244 ===
  Flüsse',  urvant-{sru-vant-)  ^fließend' ; von  einem  (^(Ä)-Präs.  aus  (:  gr.  Qvd-fiög?):  av.  raodaiti  ,fließt',  raodah-  n. ^FlußS  urüd  f.  .Flußlauf,  Bett'  (ai.  visrüh-  f.  .Strom'  oder  dgl.?);
arm.  aroganem,  ofoganem  .benetze'  {*srou-),  vgl.  alit.  srävinu  .mache bluten'),  wohl  auch  aru  , Kanal*  (*s7^utis  oder  *sru{os);
gr.  Q€ü)  jfließe'  (Fut.  qevaoiiai,  Aor.  Epidaur.  i^sQQvß^  Kalymna  i[yyQvä Konj.  aus  ^^sruuä-]  vgl.  lit.  pasriivo  .floß'  aus  -ät]  gewöhnlich  *sreue-  in  äQQvrjv, lit.  sraveti]  zu  einer  dieser  beiden  schweren  Basen  ai.  Inf.  srdvitave)] QÖog  (kypr-  QO-Fog),  att.  godg  m.  .Strömung.  Flut'.  Ttegl-ggoog  .rings  um- flossen^ (auch  hp6-QOog  für  überliefertes  HipOQQog),  gorj  (korkyr.  Dat.  PI. QliOrPaXaiv)  .das  Strömen.  Strom'  (=  lit.  srava)^  Qvrög  ,fließend.  strömend', fcegiQQVTog  .rings  umflossen'  (==  ai.  pari-sruta-),  qvaig  f.  .das  Strömen', qvdg,  -döog  .rinnend',  ^vdrjv^  hom.  qvööv  Adv.  .im  Überfluß';  Qsv(.ia  n. .Strömen.  Fluß;  Wallen';  dy,ala-QQSLTr]g  .sanft  fließend',  ßad^v-QQelxiqg  .tief fließend',  iv-QQelzrjg  .reichlich  fließend'.  (*-QQeJ^eT7jg,  vgl.  ai.  sravat-),  wie ion.  QSsd^QOVj  att.  QsZd-QOv  n.  , Flußlauf.  Flußbett'  von  themat.  ^sreue-  aus- gegangen; Qvd^^ög,  ion.  Qvaf.i6g  (,dem  Wellenschlag  des  Meeres  verglichene) regelmäßige  Bewegung.  Rhythmus';  thrak.  ^tgt^Kjov  Flußname,  ^tq^j^t] Stadtname;
air.  sruaimm  n.  ,Fluß^,  abret.  strum  ,copia  (lactis)'  (=  gr.  gsvi-ittf  wenn nicht  ablautgleich  mit  germ.  *strauma-) ;  aber  air.  sruth  .Fluß',  cymr.  ffrwd usw.,  aus  *spru-tu-',  vgl.  Pokorny  Celtica  3,  308 f.;
ahd.  strourrij  ags.  stream,  aisl.  straumr  , Strom'  (:  lett.  straume,  poln. strumien) ;
lit.  sraviüj  sraveti  (alt  sravü)  , gelinde  fließen,  sickern',  sraüjas  .rasch fließend',  sravä  ,das  Fließen.  Menstruieren',  srove^  lett.  sträve,  sträume , Strom',  s^raw ^6- .Regenbach,  Stromschnelle',  lit.  srutä  .Jauche';  aksl.  struja ,Strömung'.  ostrov^  .Insel'  (,das  Umflossene'),  poln.  strumien  ,Bach';
idg.  sreu-  ist  Erweiterung  von  ser-  , fließen'.
WP.  II  702 f..  Trautmann  279 f.;  Vasmer  2,  287;  3,  32.
1004
sreup-  jSchorfiger  Schmutz  am  Körpe^^  t»^«
Gr.  (ßVTtog  m.  ^Schmutz,  UnreinlichkeitS  Qvrröayj  Qv^raivo)  ,befl^y ^vnaQÖg  ^schmutzig',  Qvrtdcj  ,bin  schmutzig',  ^vn;og  n.  ,Molken»,  f^^ ,reinigeS  Med.  ^wasche  mich,  schneuze  mich*;  urslav.  ''strup^  {&\xB*srtup^ oder  *sroupos)  ,Wunde^  (aksl.;  eig.  ,*Schorf  auf  der  Wunde^,  ,Gift,  fi^^ (slov.),  ,SchorP  (nbulg.  russ.),  ^Ausschlag  bei  Kindern^  (skr.),  ,Q^^ Kruste'  (pohi.  dech.);  ablaut.  ksl.  str^'p^t^  ,Rauheit,  Härte'. WP.  II  703,  Vasmer  3,  32.
srig-,  srigos-  ,Kälte,  Frost*.
Gr.  Qlyog  n.  ,Frost',  Qiyia),  Perf.  m.  Präs. -Bedeutung  eggiya  ,frierett, schaudern,  erschauern';  Qlyü)w  ^friere';
lat.  frigus,  -oris  n.  (=  gr.  Qlyog)  ,Kälte,  Frost',  fr
=== POK_03 leaf 245 ===
tgeö,  -ere  ,kaltlieii^ frieren,  gefroren  sein',  frlgidus  ,kalt'.  f;^
WP.  II  705  f.;  nach  WH.  I  547,  II  434,  Tiefstufe  von  \s)reig.,  zu  lat^iTf^ »Starre',  rigor  , Erstarrung  (vor  Kälte)',  lit.  reiztis  ,sich  strecken'  (ander« oben  S.  855,  862.)  .  *4^^^
srl^mo-  ,lahm';  nur  altindisch  und  slavisch.  itt
Ai.  srämd-  ,lahm',  srdma-  m.  ,Lahmheit';  aksl.  (usw.)  chroim  ,lahm'. WP.  II  706;  Machek  Slavia  16,  191,  IF.  53,  94;  Vasmer  3,  272  f.
■y  ■ stä-:stQ-,  redupliziert  si-stä-,  erweitert  stäi-isti-,  stäu-:stu-  und  st^Otf« ,stehen,  stellen';  stä-dho-  ,Stand',  stä-lo-  ,Gestell',  stä-iiiefl- , Stand« ort,  Statur',  stä-no-  ds.,  stä-ro-  ,groß',  sto-ro-  ds.,  stä-ter-  ,Lenker*, stä-ti-,   stä-to-   stä-tu-   ,das    Stehen',   stQ-to-  ds.,  stQ-tio-,  stQ'tl» , stehend',  stä-tlo-,  sto-tlo-  ,Stand',  -sti-,  -sto-  ,stehend',  stäu-ro-j st9u-ro-:stu-ro-  ,fest,  stark,  feststehend,  Ständer',  st-eu-ro-  ,Stier*. stä-uo-  ,das  Stehen,  Stellung'. A.  Ai.  tisthati,  av.  MUaiti,  ap.  3.  Sg.  Impf.  a-iHata  ,stehn*  (:  lat.  sist^f -sissiur-j  athem.  noch  gr.  'laTrji^i,  während  spät  ahd.  sestön  ,disponere*.,J dem   roman.    ital.    assestäre   ,in    Ordnung   bringen'    entlehnt   ist),  Aor.^^ d-sthä-m  (==  gr.  IWi^y),  Perf.  tasthäu,  tasthimd,  tasthivas-]  gr.  'Lorrjiii  (( larä^i)  ,stelle',  Aor.  k'aTrjv,  Perf.  gWiyxa,  eaTa[,isVj  kcvachg  (irtl-aTa^t, stehe'  wohl  Neubildung  nach  Aor.  i7TL-GTaL(.irjv,  im-GTa^svog)',  \at6g  ,Mlä bäum,  der  senkrechte  Weberbaum,  Gewebe'; av.  ap.  stäya-  , stellen ;  Med.  sich  stellen';
lat.  sistö  ,stelle',  umbr.  sestu  ,sistö',  volsk.  sistiatiens  ,statuerunt;   '^ air.   tai7'-(^s)issiur  , stehe,  bleibe  stehen*,  ar-sissedar  ,insistitur,  innitit fo-sissedar  ,tritt  ein  für'  {sessam  ,das  Stehen',  sessed  ds.  usw.);
lat.  stö  (stäre,  steti)  =  umbr.  stahu  ,stehe',  *stä-{ö]  altlat.  wohl  ftt
1005
trans.  ,stellen' ;  osk.  stait  {*staieieü)  ,stat'  PI.  stakint,  eestint  (*estaieient) extant';  air.  ad-täu,  -tö  ,ich  befinde  mich,  bin'  {*stä-i5),  3.  Sg.  {adytä  = cymr.  taw  ,daß  es  ist'  aus  *stä-t,  unpersönl.  Passiv  täthar  ,man  ist (böse)' aus  *stä-to-ro(?),  mcymr.  Impersonale  ny-m-dawr  ,es  kümmert  mich nicht',  com.  ny-m-deur  (*tä-ro-)  ,ich  will  nicht';  air.  ness-  (*ni-stä-)  ,nieder- treteu'  in  com-ness-  ds.,  ^verurteilen',  di-ness  ^verachten*,  to-ness-  »betreten', ar-ossa  ,erwartet'  {^are-uhs-stä-)]  assae  gleicht  zu  tun'  aus  *ad-stä-io- ^adponendus' ;
as.  ahd.  stän,  sten  ,stehen' ;  Reim  Wortbildungen  zu  gen,  gän  ,gehen' (S.  419);  mit  ^Erweiterung:  Prät.  got.  stöp,  aisl.  stöd^  as.  stöd,  ahd.  stuot (meist  stuont  nach  dem  Präs.)  ,ich  stand',  wozu  mit  präsentischer  Nasalie- rung got.  as.  standan,  aisl.  standa,  ags.  stondan,  ahd.  stantan  , stehen';  dazu ahd.  stanta  , Kübel,  Kufe'  und  mit  neuem
=== POK_03 leaf 246 ===
  Ablaut  aisl.  stund  ,Zeit(punkt), Weile,  Stunde,  Länge',  ags.  stund  f.  , bestimmte  Zeit,  Stunde,  Mal',  as. stunda  ,Zeit(punkt)',  ahd.  stunta  ds.,  spätmhd.  auch  ,Stunde'j
lit.  stöju  (*siä{ö),  stöti  ,treten',  aksl.  *stajg,  statt  ,sich  stellen',  stojg stojati  {*stdieti)  ,stehen';  toch.  B  ste  ,ist',  3.  PI.  stare.
B.  idg.  n-Präs.  *st9-nä-  in  av.  fra-stanvanti  ,sie  kommen  voran',  arm. stanam  , erstehe,  erwerbe',  gr.  kret.  oxavvu)  , stelle'  (Neubildung  gr.  laravo)) ; lat.  prae-stinäre  ,den  Preis  vorher  feststellen,  kaufen',  destinäre  , fest- machen, festsetzen,  fest  beschließen'  {destina  , Stütze'),  obstinäre  ,auf  etwas bestehen';  alb.  shtonj  ,vermehre'  (,*stelle,  staple  auf);  aksl.  stang  (Inf. stati)  , werde  mich  stellen,  treten';  apr.  postänimai  ,wir  werden',  postät ,werden',  stänintei  ,stehend';  toch.  B  stäm-  , stehen';  vgl.  auch  die  Nomina mit  7i-Formantien.
C.  Wurzel-Nomina  als  2.  Kompositionsglieder:
ai.  ni-sthä-  ,hervorstehend,  -ragend',  pari-stJiä-  ,(*herumstehend  =)  hem- mend', f.  , Hindernis',  pfthivi-stha-  (und  -sthd-)  ,auf  dem  Boden  stehend, fest  auftretend*,  ratke-sthä-  ,auf  dem  Wagen  stehend,  kämpfend*  =  av. rad-ae-Stä-  , Krieger';  gr.  d-Sf^Lg,  -arog  , Recht,  Gesetz'  (ursprüngl.  Götter- name ,die  fest  und  unverbrüchlich  Stehende',  ^d-ef-d-atöt)^  gr.  (.Latavdatrjg ,wer  seinen  ursprünglichen  Wohnsitz  durch  Aufstehen,  Wegzug  verändert hat';  air.  hiress  , Glaube'  (Präf.  *[p]eri -f  s^ä).
B.  -st-o-:  ai.  z.B.  pra^i-6'^Äa-, feststehend'  {-sthä  f. , Stillestehen, Beharren*), duh-stha-  =  gr.  öua[a]rog  „dvarrjvog" ,  bala-stha-  ,in  voller  Kraft  stehend^ u.  dgl.  5  Subst.  pra-stha-  m.  ,Bergebene'  (,hervorstehend')  ==  air.  7'oss  ,Vor- gebirge,  Wald',  mbret.  ross  ,Hüger,  cymr.  rhos  ,Moor*,  aksl.  Adj.  ,ge- rade,  schlicht,  einfach';  a.].  pr-sthd-  n.  , Rücken'  usw.  (S.  813);  gr.  naatog , Bettvorhang'  (vgl.  mit  c^-Suffix  gr.  TtaQaaxäg,  Tcaox&g  usw.  ebenda);  ai. gösthd-  m.  n.  , Kuhstall*,  bhayd-stha-  m.  n.  ,ge fahrvolle  Lage',  ahd.   eioi-st
1006
m.  ,Schafstal],  Schafhürde',  aisl.  nau-st  ii.  ^Schuppen  für  Schiffe,  Schiff,, haus';  alb.  breshte,  bresht  f.  ^Tannenwald'  (:  hrS  ,TanneO  u.  dgl. ;  altiUy^^ Tergeste,  Aadeora,  -aiov  usw.;  ai.  tri-sthd-  ,auf  drei  Unterlagen  stehend»* osk.  trstits  ,testes'  {tristaamentud  ,testamento');  lat.  (zum.  i-St.  geworden) testis  (Hri-sto-)  ,wer  als  dritter,  als  Zeuge  hei  zwei  Streitenden  steht',  air^ tress-  ^dritter*;  lat.  caelestis  ,in  caelo  stationem  hahens'  (ursprüngL  o-S^ vgl.  &'7ra?  Xsy.  Veneria  caelestae),  agrestis  ^ländlich';  lit.  atstüs  ,fern'  (:  atsUiti ,sich  entfernen';  vom  Adverh  atstü  =  Instr.  auf  -6  ausgegangen),  lett.  nix^ Adv.  ,weg,  hinweg,  fort';  lat.  praestö  ,gegenwärtig,  da,  zur  Hand,  ^ Diensten';  praestöläri  ,bereitstehen'  wohl  aus  *praestödärl ]
als  idg
=== POK_03 leaf 247 ===
.  *sf[9]^i-s  mit  in  der  Komposition  geschwundenem  a  sind  hin* gegen  aufzufassen:
ai.  pr-?ti-  f.  ,Rücken'  usw.  (S.  813  Mitte)  und  prati-sthi-  »Widerstand'*  ;;"' gr.  l^aOTiq  ,aus  dem  Gewehe  vorstehender  Faden*  (*£?-ay-o"rtg),  xax  ^«  "• rriüXLv  , gegenüber'  (*avTr]v-ati-);  lit.  dim-stis  ,Hofraum,  Hof,  Gut'.
E.  Nomina  mit  Dental-Suffixen:
1.  lat.  super-stes,  anti-stes  {*std-t-)]
2.  Partiz.  ai.  sthitd-  , stehend'  (av.  stäti-  ,stehend'  mit  geneuerter  Hoch stufe),  gr.  a-cardg  ,gestellt,  stehend',  lat.  (osk.-volsk.)  Status  ,gestellt';  air; fossad  ,fest',  cymr.   gwastad  ,planus,   constans,  aequus'  (*upo-statos)'y  aialj stadr  ,zum  Stehen  geneigt,  stätig'  (bes.  von  Pferden)  Ableitung  mhd.  stet^ ds. ;  ahd.  stata  f.  ,bequemer  Ort  oder   Zeitpunkt,   Hilfe',  nhd.   zitstatteni ahd.  gistatön  ,gute  Gelegenheit  gehen,  gestatten',   aisl.   stedja  , stellen, stätigen,   gestatten',   mnd.   steden  ds.,   ags.  stceppan  ,zum  Stehen  hringen' lit.  stataüj  -yti  ,stellen* ;
3.  alh.  meshtet,  pshtet  , stütze,  lehne  an',  f stetem  ,bleibe'  (zum  Yerbaladj *st9-to-) ;
4.  ai.  stliiti-  f.   ,das   Stehen,   Stand,   Bestand',   av.    stäti-   , Stehen,  Aq^ Stellung';  gr.  aiäaig,  -eo)q  ,Stellung,  Stand;  Aufstand'  (crarixoc,  aTdai\iO^\
lat.  statim  , während  des  Stehens,  stehend';  klass.  ,auf  der  Stelle*,  itai^ =  osk.  statif  , Standort',  got.  sta^s  m.  (i-St.),  aisl.  stadr  m.,  ahd.  stat  L ,Ort,  Stelle,  Stätte,  Stadt',  ags.  stede^  styde  f.  ,das  Stehen,  Stehenbleiben,' Stätte'  (vgl.  auch  anord.  ew-St.  stedi  m..  Gen.  stedja  , Amboß'  aus  "^stapjan-^ eigentlich  , Ständer');  hochstufig  av.  s^äi^i- , Stehen,  Stand,  Aufstellung*,  aksL^; postath  ,Bestimmung',  Inf.  lit.  stöti^  lett.  stät,  apr.  stät,  aksl.  statt  ,sich stellen,  treten';
lat.  Status,  -üs  ,das  Stehen,  Stellung,  Stand',  statuö,  -ere  ,hin-,  aufstellend^ umbr.  statita  , statuta';  bret.   steut,   cymr.   ystawd  , Garben'  (*sta-ta)j  hre steudenn  , Zapfen,  Nagel'  {*sta-t-),  Loth  RC.  43,  1541.;  lit.  statüs  ,steheni steil',  got.  stapa  Dat.,  as.  stath  m.,  ahd.  stad,  stado  m.  , Landungsort,  Üferj
1007
(jestade^;  aisl.  stgd  f.  ^Landungsort,  Stellung',  stqdva  ,zum  Stehen  bringen* ;     /*stapwö(n),  vgl.  lat.  statu-s,  -ere);  stadi  , Heustapel  in  der  Scheune^  (=  mnd. Stade  ,Ort,  wo  die  Ernte  aufgehäuft  wird').
5.  mit  cfA-Suffix:  cymr.  an-sawdd  yAs^s  Festmachen^,  air.  sädud (*städh-i-tu-) jg.j  aisl.  stöd  n.  , S
```


## [2026-09-14T02:28:37.822Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 248 249 250 251; do echo \"=== POK_03 leaf $n ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$((n+1))\"' {print}' POK_03.txt; done",
 "description": "Print Pokorny leaves 248-251 (pp. 1008-1011)"
}
```


### [2026-09-14T02:28:38.912Z] TOOL RESULT

```
=== POK_03 leaf 248 ===
tandort,  Herde  von  Stuten  mit  einem  oder  mehreren ^engsten',  ags.  stöd  n.  ,Pferdeherde',  mnd.  stöt  (-d-)  f.  , Einzäunung  für Pferde,  Herde  von  Zuchtpferden',  ahd.  stuot  f.  , Herde  von  Zuchtpferden', auch  , Stute',  nhd.  Stute-,  aisl.  (z.  B.  hug-)  stMr  ,feststehend,  fest*  (eher idg.  i  wegen  got.  ungastopai  ,ohne  festen  Stand';  t  oder  dh  mit  analog, j^blaut  e:  ahd.  stäti  ,fest,  dauerhaft,  stet',  mnd.  stBde  ,fest,  beständig');  Kaus. (Tot.  ana-y  du-stödjan  ,anfangen',  aisl.  stßda  ,zum  Stehen  bringen' ;  mit  germ. *stöpici-  lautet  ab  lit.  stäcias  , stehend';  lit.  statine  , große  Holzwanne';
6.  ai.  sthätar-  , Lenker',  sthätr  n.  ,das  Stehende*,  lat.  stätor]  gr.  OTair^q, •^Qog  ,ein  Gewicht  und  eine  Münze';  *st[9'}-ter  mit  Schwund  des  9  im Kompositum,  vielleicht  in  ai.  savya{e)-sthar-  ,der  links  stehende  Wagen- kämpfer', av.  rad^ae-Har-  , Krieger,  Kriegsheld*  (wie  rad-ae-§tä-,  s.  oben; vielleicht  aber  Umbildung  von  -sthä  nach  den  Nomina  agentis   auf  -tar) ;
I  7.  lat.  ohstäculum  , Hindernis*  n.;  cymr.  cystadl  ,gleichwertig*,  distadl ,wertlos'  (*st9-tlo-) ;  aisl.  stqdull  m.  ,Melkplatz,  Senne'  =  ags.  stapol , Grund- lage,, Stellung,  Platz',  as.  stathal  ,Stellung*,  mnd.  stadel  , Scheune',  ahd. stadal  , Stand,  Kornscheuer',  nhd.  (süddt.)  Stadel,  älter  dän.  stedel  , Grund, Hofstätte';  lit.  stäkles  PI.  ,Webstuhl';  lit.  stähle  , Pfahl',  lett.  staklis  ,ds. Zacke,  Zinne,  Gabel*,  apr.  stakle  ,Stütze'  (mit  M  aus  tl).
8.  mit  Formans  -dblo-:  lat.  stahulum  ,Standort,  Aufenthalt;  Lager  wilder Tiere,  Stall'  (pröstihulum  ,Ding  zum  öffentlich  Ausstehen,  Dirne',  nausti- bulum  , Schiffstandort,  Gefäß  in  Schiffsform'),  stahilis  ,f eststehend,  stand- haft', umbr.  staßarem  ,stabulärem',  osk.  staflatas-set  ,statutae  sunt*,  pälign. pri-stafalacirix  ,*praestibulätrix,  antistita* ;
vereinzeltere  Dentalableitungen:  -dh-  in  gr.  ara-d-i^ög,  meist  PI.  arad-ixd
,Stand,  Standort,  Gewicht',   arad^sgög   , stehend,   unbeweglich,  fest';  -d-  in
azdÖLog  , stehend,  unbeweglich,  steif,  zugewogen',  arddrjv  , stehend',   äfvo-
OTadov  ,fern  abstehend*.
•  *
9.  mit  i-Formantien :
cymr.  cystal  , ebensogut'  {*kom-sta-lo-)-^  got.  stöls  ,Thron',  ahd.  stuoly ags.  stöl,  anord.  stöll  ,Stuhl*,  lit.  pastölai  , Gestell  für  Bienenkörbe',  tief- stufig aksl.  stoh  , Thron,  Sitz',  in  den  neuern  slav.  Spr.  ,Stuhl'  oder  ,Tisch'.
10.  mit  122-Formantien : ai.  sthäman-  n.  , Standort,  Kraft*;  gr.  ari^fiwv  m.,  aT
=== POK_03 leaf 249 ===
rjiLsvai  ,stehen',  lat.
stämen   n.    , Aufzug   am  aufrecht   stehenden  Webstuhl,  usw.*,  umbr.   Dat.
1008
stahmei,st8.t\öm'',  stahmito  ,statütum^ ;  air.  sessam  ,das  Stehen'  (*n-s<(i^||^4i| föessam  ,Schutz'  (^wpo-si-sta-mu-)  =  mcymr.  gwaessaw  »Garantie»;  :'g^j Stoma  ,i7t(^(TraaLgy  Grundlage,  Stoff';  lit.  stomuo,  -ens  ,Statur^;  russ.  tto^^^ ,  Stützbalken^;
gv.  atdfxvog  ,KrugS  ara^tv-eg  PI.  , Ständer,  Seitenbalken';  cymr.  cy^  ^ ,erster'  {*kentu-stamino-)',  mir.  samaigim  ,stelle',  cymr.  sefyll^  corn.  %t^ ^stehen',  bret.  sevell  (*stamilio-)  ,errichten,  bauen'  (daneben  mit  kelt.  |  f^ tamun  »Baumstamm*;  ahd.  stam,  Stammes  ,Stamm''  usw.  scheint  Verqn|^ kung  eines  verwandten  *stamna-  mit  einem  staina-,  s.  *steb-  ,Pfo8teii')j toch.  A  stäm,  B  stäm  ,Baum*;  aber  ahd.  ungistuomi  ,ungestüm'  zu  «i^^ , hemmen',  s.  dort.  ,^,^,
11.  mit  JQ-Formantien  (vgl.  die  Präsensbildungen  mit  n)\  ■:. ai.  sthdna-  n.,  av.  ap.  stäna-  n.  , Standort,  Ort,  Platz',  npers.  sitan^  »t^
Ma-[a]TTjvog,  dor.  dvatävog  ,(in  schlechtem  Zustande)  unglücklich',  ^axiit^ ds.,  lit.  stönas  ,Stand',  aksl.  stam  , Stand,  Lager',  alb.  shtuare  ,stehen4*       ^ shtoraze  , auf  recht'   {*stä-no-dio-j  vgl.   zum   (i-Suffix   gr.    dnooTadöv  usw.l shtäze,  shteze  ,Vieh'  {*stan-ze).
12.  mit  r-Formans:  ai.  sthird-  ,fest,  unbeweglich';  lit.  störas  ,dick,  umfanr« reich'  (eigentlich  , stämmig'),  aksl.  starb  ,alt'  (,*stämmig'  im  Gegensatz  Bur zarteren  Jugend),  anord.  störr  ,groß',  as.  störi  ,groß,  berühmt',  ags.  tUir ^gewaltig';  '^^H
13.  mit  dem  i  von   *stä-iö  weitergebildet:  ai.  jala-sthäya-  m.  »Wasser^^ behälter',  sthäyin-  , stille  stehend,  verweilend,  stetig'  u.   dgl.,  sthemdn-  m. ^Festigkeit,  Ruhe,  Dauer'  {*sthayiman-).
F.  st(h)  äu- :  st(b)  ü- :  lit.  stöviu,  -eti  ,stehen'  (Memel  stdunu),  stovä  ,Stelle*, stövis  , Zustand',  stoviis  , stehend  (vom  Wasser)',  lett.  stävu,  stävet  ,stehei^ Mävus  , stehend,  aufrecht' ;  stävs  , steil',  stävs  , Gestalt',  stävi,  stäve  ^Webstuhl*; aksl.  staviti  ^stellen',  stav^  ,Stand,  Gefüge';  ags.  stöw,  afries.  stö  f.  , Stelle', aisl.  eld'Stö  , Feuerstätte';  got.  stöjan  ,richten'  (vielleicht  *stöwjan:  aksl. ■staviti),  staua  f.  _,Gericht'  (*stöwö)j  staua  m.  ,Richter',  ags.  stöwian  ,zurück- halten',  engl,  stow  , stauen',  ahd.  mhd.  stouwen  (*stawjan)  ,(au) klagen; (scheltend)  gebieten;  Refl.  sich  stauen',  nhd.  stauen-  mit  ü:  ahd.  stiiata^ ,Gerichtstag',  stüan  ,anklagen,  schelten,  hemmen',  mnd.  stüioen  (=  stouwtn^ ■stowen)  , stauen',  usw.;
mit  Abtönung  stöu-\  gr.  %rw/-(5g  , Säule'  in  att.  oxotd,  arod  (*(TTft;/j(ö), äol.  OTiüta  , Säulenhalle',  gtuSiölov  Demin.,  OToüyLÖg  ,zur  Schule  der  StOÄ gehörig',  OTcb^i^'  SoKig  §vXlvr]  Hes.;
schwachstufig:  ai.  sthünä  , Säule'  (mind.  n  aus  n),  av.  stUna,  s^wnä , Säule'; gr.  GTiu)  ,steife,  richte  empor'.  
=== POK_03 leaf 250 ===
Med.  ,bin  steil  aufgerichtet',  atvi^a  n. ^erectio  penis',  orv^iog'  ariXsxog,  yicgfiög]  axvlog  m.  ,Säule,  Griffel',  atvqoi
1
1009
jjjs  untere  Ende  der  Lanze' ;  aisl.  stümi  ,ein  Riese' ;  mhd.  stünende  ^wider- ggtzlicli^  nhd.  staunen  als  ^starr  blicken';  keine  Belege  für  diese  Ablaut- stufe  sind  hingegen  die  w-St.  ai.  su-sthü  Adv.  ^gut,  schön',  anu-sthu,  anu- flhuyä  ^sogleich';
mit  ^-Formans  dazu :  aisl.  stod  (PL  stoä:ir,  stedr,  stedr)  f.  ,Stütze,  Pfosten, Unterstützung^,  ags.  studu,  studu  f.  ,Stütze;  Pfosten^,  mhd.  stud  f.  ds.^  aisl. fiu^ill  m.  ds.,  mhd.  studel  , Pfosten,  Türpfosten';
aisl.  stydja  ,stützen^,  ahd.  studen  , festmachen,  statuere*,  aisl.  stoda  ,unter- ' stützen,  helfen';  mit  intens.  Konsonantendehnung:  mnd.  stutten  , (unter-) stützen',  ahd.  (unter) stutzen^  nhd.  (unter) stützen;  auch  ahd.  stüda  ßtaude^ -^ lett.  Stute,  stuta  ,Reis,  Rute';
reduktionsstufig  stsu-:  gr.  OTavQoq  ,Pfahl'  =  aisl.  staurr  ,Pfahl' (ablaut.  uoTW.  dial.  styr,  styrja  ,lange  Stange,  steife  Person');  lat.  in:  ins- tauräre  , instand  setzen'  (ursprünglich  von  Stangen,  Ständern  beim  Bau), restauräre  ,wiederinstandsetzen'.
Gr.  st-eu-,  st-euQ-  , massiv,  fest,  dick,  breit'  (germ.  stiura  s.  u.)  als  , stand- sicher, feststehend'  in  ai.  sthävard-  ,dick,  feststehend,  beständig'  (letztere Bed.  und  die  Vokallänge  vielleicht  durch  Anlehnung  an  sthä-  , stehen'), sthdvira-  , breit,  dick,  derb,  dicht,  alt',  (oder  nach  dem  Komp.  Sup.  er- folgter Ersatz  für:)  ai.  sthürd-,  sthüld-  ,dick'  =  av.  stüi^a-  , umfangreich, stark,  derb'  (Kompositionsform  stüi-,  stvi-^  d.  i.  *stuvi-),  Kompar.  Superl. ai.  sthdvlyas-,  av.  staoyä  ,der  Umfangreichere,  Stärkere,  Größere*,  ai.  sthd- vistha-,  av.  stävista-  ,der  Stärkste,  Derbste,  Gröbste',  ai.  sthdviman-  n. jBreite',  av.  stavah-  n.  ,Dicke,  Stärke';  arm.  stvar  ,dick'  (^stwaai^-) ]
aschw.  stür  ,groß'  (neben  stör,  s.  oben),  styras  ,großtun',  mnd.  stür ,groß,  stark,  schwer;  störrisch,  grob,  unfreundlich'  (vgl.  ai.  ni-sthura- ,rauh,  hart,  grob',  ni-sthürin-  ,grob,  roh'),  aisl.  stüra  , Düsterheit',  Vb. jbetrübt  sein'  (nschw.  stüra  , starr  hinsehen'  in  der  Bed.  nach  der  Sippe von  nhd.  stieren  umgeändert),  hochstufig  ahd.  stiuri  , stark,  stattlich, stolz' ;
mit  anderer  Bedeutung:  ahd.  stiura,  mhd.  stiure  , Stütze,  Steuerruder, Unterstützung,  Steuer',  nhd.  Steuer  f.  und  (aus  dem  Nd.)  n.,  ags.  steor  f. (Steuerruder',  aisl.  styri  n.  , Steuerruder',  mnd.  stür(e)  n.  , Steuerruder',  f. n.  ,Regierung;  Hilfe,  Gegenwehr',  f.  ,Unterstützung',  got.  us-stiurei  ,Zü- gellosigkeit',  mnd.  unstüre  ds.,  got.  stiurjan  »feststellen,  behaupten',  nhd. iur  Steuer  der  Wahrheit,  aisl.  styra  ,ein  Schiff  steuern;  regieren',  ags. Hieran  ds,,  ahd.  stiurren  , s
=== POK_03 leaf 251 ===
tützen,  steuern,  lenken';  wohl  ursprüngl.  , Pfahl, Steuerruder  (sekundär:  damit  stützen,  lenken)',  mit  aisl.  staurr,  gr.  atav- P<^S  (s.  oben)  unter  *steu-ro-:*st9u-ro-  vereinbar,  das  von  *st(h)äu-  nicht ganz  getrennt  werden  könnte;
64
1010
zu  ai.  sthürd-  usw.  stellt  sich  wohl  idg.   steu-ro-   ,Stier  (und^ Großvieh/:
av.  staora-  _,Großvieh^  mpers.  stör  , Zugtier^  Roß^  got.  stiur  m^ kalb,  Stier'  (nach  W.  Schulze  Kl.  Sehr.  483  ==  ai.  sthdvira-)-^  ahc ags.  steor,  aisl.  stiörr  (neben  pjörr)  , Stiert
WP.  II  603  ff.,  WH.  I  343  f.,  705  f.,   Trautmann  280  ff.,  Yasmer
stag-  ^sickern,  tröpfeln,  leise  rinnen^
Gr.    ard^a),    öTa^w   arayrjvaL   ^träufeln,    einträufeln   tr.,   tröpfeln tröpfeln  intr.,  rinnen',  oraA-iog  , tröpfelnd,  tropfend',  GTayd)v,  -övog  tf^*^^ fen',  (Tzdysg  PL  ds.;  ^
lat.  stägnum  ,jedes  ausgetretene  Gewässer,  See,  Teich,  Tümpel  PimV oder  langsam  fließendes  Gewässer';  -^   ,   '
lat.  (kelt.  Lw.  ?)  stagnum  ,Zinn'  (,das  Getropfte,  leicht  Schmelil)tr#v air.  stän  ,Zinn';  cymr.  ystaen,  ncorn.  stean,  bret.  stean  (aus   dem  ^LiLll*
abret.  staer,  nbret.  ster  _,Fluß,  Bach'  (*stagra),  cymr.  taen  ,coii»p©fi4,, adspersio'  (^stagnä).
WP.  II  612,  WH.  II  585,  Flasdieck  Zinn  u.  Zink  14  ff.  .1,^
{s)tai-  , heimlich  um  etwas  bringen,  hehlen,  stehlen';  taiu-s-,  ^a-fi-s  ,DitV Ai.  stäydt  , heimlich,  verborgen',  stäyu-,  täyü-  ,Dieb'  (=  aksl.  taj  J^if ,geheim',  wenn  aus  *täiu]  gr.  Trjv-aiog)',  stiya-m  ,Diebstahl',  siend-   Dieb* SLV.  täyu'  ,Dieb',   täya-  , Diebstahl',   gr.  Trfvairi  böog  ,ein  Weg,  der,elB#ii um  die  Mühe  der  Absicht  betrügt'  (Hav-TLOg,  von  *Täiv-TCt)^  ttJti;  •  ärto^^ evösia,  axBQTiaig  Hes.,  Trjxdü}  , bringe  um  etwas,  beraube*,  Med.  ,darbe*:  ftjf täid  ,Dieb'  (=  abg.   tath,  das   -d   analogisch);   aksl.   taj  , heimlich',  iak^ tajiti  , verhehlen',  tath  ,Dieb';  hitt.  tajezzi^  tajazzi  , stiehlt'.  V^
WP.  II  610,  Trautmann  313,  Vasmer  3,  69.  ,1^
stäi-,  stt-,  sti-ä-  ;,verdichten,  zusammendrängen,  stopfen;   sich  verdichi«,
gerinnen,  stocken';  sÜ-iä  ,etwas  Dichtes',   sti-mo-,  sÜ-ro-  ,dichl^:
dazu  sitih{}i)-j  stti'p-  , Stange  usw.'.
Ai.  stydyate  ,gerinnt,   wird  hart',  Partiz.   styäna-]    (Gramm.)   prastlfM
»gedrängt,  gehäuft',  stlmd-  ,träge'  (eig.  ,gestockt'),  vistlmin-  Bez.  des  cunnö»,
stiya  f.  ,träges,  stehendes  Wasser',  stimita-  , schwerfällig,  träge,  unbew^
lieh,  naß';  av.  sta{yy  , Haufen,  Masse';
gr.  aziag,  azearog  ,stehend
```


## [2026-09-14T02:28:55.534Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== POK_03 leaf 252 (p1011) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==253' POK_03.txt | head -60; echo; echo \"=== grep stāk / stak- headwords ===\"; grep -n \"st.k-\" POK_03.txt | grep -iE \"stehen|stellen\" | head -20",
 "description": "Print Pokorny p.1011 and search for stāk-"
}
```


### [2026-09-14T02:28:56.613Z] TOOL RESULT

```
=== POK_03 leaf 252 (p1011) ===
es  Fett,  Talg'  (^stäif)]  hom.  dyxi-azlvog  DaJ># aneinandergedrängt'  (vgl.  ai.  styä-na-);  azia  f.,  azTov  n.  , Steinchen';  <rföf ,Tropfen'  (vgl.  lat.  stlria,  stilla);
lat.  stiria  ,gefrorener  Tropfen,  Eiszapfen',  Demin.  stilla  ,Tropfen*  (*!« r[e]lä)',
jjjsl.  stlrur  ^stiffness  in  the  eyes';  norw.  stwa,  aisl.  sttra,  dän.  schwed. ftirra  ;Starren,  stieren^,  ostfries.  stli^  ^steif,  starr^;  nhd.  stier,  stieren-,  lit. ^t/i'stü,  styrti  , erstarren^,  styrau,  -oti  ^»steif  und  lümmelhaft  dastehen';
aisl.  stim  n.  ^Unruhe,  Lärm^,  norw.  stlm  ,Fischschwarm',  mhd.  stlm,  steim bunte  Menge,  Getümmel';
p-ot.  stalns^  aisl.  steinn,  ags.  stan^  ahd.  stein  , Stein';
aksl.  stena  ,Wand,  Mauer^^  st^ntm  ,steinig^;
vielleicht  auch  aisl.  stl  n.  , Stall',  stla  ^einhegen';  ags.  stig,  stl  ^Schweine- stall;  Halle',  mnd.  stege  , Pferch',  ahd.  stiga,  mhd.  st'ige,  stlje  ^Stall  oder Latteüverschlag  für  Kleinvieh';
lit.  stmgti  ,gerinnen',  lett.  stingt  ^kompakt  werden',  stingrs  ^stramm,  starr, lusammenhaltend,  gespannt,  steif;
über  lat.  timeö  , fürchte  mich',  usw.  s.  WH.  II  682.
WP.  II  610 f.,  WH.  II  595;  s.  auch  steu9-  S.  1035.
f^-,  stek-  , stehen,  stellen ;  stehend,  Ständer  =  aufrecht  stehender  PfahF; Erweiterung  von  stä-  , stehen';  stok-lo-  ,fest^
Ai.  stdkati  , widersteht',  av.  staxta-  ,fest,  stark',  staxra-  ,stark,  fest;  hes. Tom  Winterfrost:  streng';  umbr.  stakaz  ,statatus';
ahd.  stahal  n.  m.  aisl.  ntäl  n.  (abgeleitet  ahd.  stehlij  ags.  stiele  n.)  ,Stahl' (aus  dem  Germ,  stammt  apr.  staclan  ,Stahl'),  germ.  *stahla-  wohl  =  av. ttaxra-y  idg.  *stöklo- ;  aisl.  stagl  n.  ,Rad,  das  zur  Hinrichtung  dient',  norw. itagle  ,Pfahl',  staga  ,steif  gehen',  aisl.  stag  n.,  ags.  stcBg  n.  ,Tau'  (,*das Steif  gespannte');
mit  anderer  Bedeutungswendung  (,stehenbleiben  =  stocken,  zu  kurz L  werden')  aisl.  stakka  f.  , Stummel',  stakkadr,  stqkuttr  ,kurz',  dän.  stak-aandet ,kurzatmig' ;  lit.  stohä  , Mangel',  stokstü,  stokti  ,zu  mangeln  beginnen'.
WP.  II  611,  WH.  II  585.
[I<eb(ii)-  und  steb{h)-:stabh-,  nasaliert  stemb(hy]  step-  (auch  step-?), nasaliert  stemp-]  nominal  stobho-s,  steznb{h)ro-Sf  stonib{h)o-s. Bedeutungsumfang:  , Pfosten,  Pfeiler,  Stamm,  Baumstumpf  (auch  , Busch, Büschel');  verbal:  , stützen,  versteifen,  feststellen,  anhalten,  (auch  ,hemmen'), (auf) stampfen,  treten  (Tritt,  Stufe,  Fußspur);  beschimpfen  (steif  und  heraus- fordernd dastehen;  prahlen),  staunen  (aus  erstarrt  dastehen)';  Beziehung lu  *s^ä-  , stehen'  ist  möglich.
Wurzelform  mit  -b:
ai.  stdhaka-  m.  n.  ,Büschel',  stambd-  m.  ,Busch,  Büsche

=== grep stāk / stak- headwords ===
3435:f^-,  stek-  , stehen,  stellen ;  stehend,  Ständer  =  aufrecht  stehender  PfahF; Erweiterung  von  stä-  , stehen';  stok-lo-  ,fest^
3438:mit  anderer  Bedeutungswendung  (,stehenbleiben  =  stocken,  zu  kurz L  werden')  aisl.  stakka  f.  , Stummel',  stakkadr,  stqkuttr  ,kurz',  dän.  stak-aandet ,kurzatmig' ;  lit.  stohä  , Mangel',  stokstü,  stokti  ,zu  mangeln  beginnen'.
```


## [2026-09-14T02:28:57.043Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 521 522 523; do echo \"=== POK_02 leaf $n ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$((n+1))\"' {print}' POK_02.txt | head -40; done",
 "description": "Print Pokorny leaves near p.866"
}
```


### [2026-09-14T02:28:57.934Z] TOOL RESULT

```
=== POK_02 leaf 521 ===
=== POK_02 leaf 522 ===
=== POK_02 leaf 523 ===
```


## [2026-09-14T02:29:03.417Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for f in POK_01.txt POK_02.txt POK_03.txt POK_full.txt; do echo \"$f: $(tr -cd '\\f' < $f | wc -c) pages, $(wc -c < $f) bytes\"; done",
 "description": "Count form-feeds in POK files"
}
```


### [2026-09-14T02:29:04.514Z] TOOL RESULT

```
POK_01.txt: 363 pages, 981836 bytes
POK_02.txt: 433 pages, 1137861 bytes
POK_03.txt: 429 pages, 1170809 bytes
POK_full.txt: 0 pages, 3971883 bytes
```


## [2026-09-14T02:29:10.025Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"rota\" POK_03.txt | head -20; echo ====; awk 'BEGIN{RS=\"\\f\"} /ret\\(h\\)-|reth-.*laufen|,laufen, rollen/ {print NR\": \"substr($0,1,300)}' POK_03.txt | head",
 "description": "Find Pokorny ret(h)- root"
}
```


### [2026-09-14T02:29:11.264Z] TOOL RESULT

```
Exit code 1
644:arm.  ^i<^^^  ^ich  schlugt  (Aor.  zum  Präs.  Jiarkanem,  s.  u.);  harac  ^vulnus^; ^rot  ;,Doiiner^,  orotam  , donnere';
998:Mir.  räthaigid  ,bemerkt';  got.  frapi  n.  Sinn,  Verstand',  frapjan,  fröp ,verstehen',  fröps  ,klug,  verständig',  aisl.  frödr,  as.  ags.  fröd,  ahd.  fruot ds.,  mhd.  vruotec,  vrüetec  , schnell  entschlossen,  munter,  tapfer',  nhd.  Schweiz. fruetig  ,froh,  frisch,  tapfer,  schnell',  auch  ahd.  frad  ,strenuus  efficax', fradah-lih  ,procax';  vielleicht  ahd.  antfrist  ,interpretatio'  {*pret-sti-)'^  lit. prantü,  prästi  , gewohnt  werden',  su-prästi  ,versteheQ',  protas  , Verstand', lett.  prüotu,  prast  ,verstehen,  begreifen,  merken',  präts  ,Verstand,  Sinn, Wille,  Meinung,  Gemüt',  apr.  prätin  Akk.  ,Rat',  iss-jprestun  ,verstehen', is-presnan  Akk.  ,Vernunft',  issprettingi  Adv.  ,nämlich';
1312:Ai.  rdtha-  m.  .Wagen',  ratU- , Wagenlenker',  rdthya-  .zum  Wagen  gehörig', rathar-ydti  .f<ährt  im  Wagen';  rathesthä-  .Krieger'  =  av.  radaeUä  ds.;  av.  ra-. ^a-  .Wagen',  raid^ya  .Fahrstraße';  lat.  rota  ,Rad',  birotus  ,zweirädrig'  (:iit,  ^^ dvirätis),  rotundus  ,scheibenrund';  ir.  roth  m.  ,Rad';  cymr.  rhod  f.  .Rad'j gall.  OIST  Roto-magus  (Rouen);  kelt.  *-reto-  .Lauf,  neutr.  Abstraktsuffix  in cymr.  brith-red  .Verwirrung'  =  mir.  brecht-rad  .Mannigfaltigkeit'.  Kollektiv-,.. Suffix  in  mir.  aig-red  ,Eis' ;  dehnstufig  *-röto-  in  mcymr.  rhawd  ,Lauf,  LauM.,.. bahn,  Schaar',  gaeaf-rawd  .Winterszeit'  =  mir.  gem-rad  ds.,  mcymr.  bed- rawd,  cymr.  bedd-rod,  bret.  bez-ret  , Gräber'  (cymr.  bedd  .Grab'),  dazu  miri rä(i)the  .Jahreszeit.  Vierteljahr'  {^rötio-)]
1393:aisl.  rjödr,  ags.  reod  ,rot',  aisl.  rjöda  ,blutig  machen',  ags.  reodan  ,r färben',  got.  (über  , schamhaft  erröten')  ga-riups  ,ehrbar',  ga-riudei  ,Schai haftigkeit';  ablaut.  rau'ps,  aisl.  rauär,  ags.  read,  ahd.  rot  ,rot',  aisl.  raudi ,rotes  Eisenerz',  rodra  f.  ,Blut',  rodi  m.  ,Röte',  ryd  n.  und  rydr  m.  ,Rost roda  ,rot  sein  oder  werden',  ahd.  roten  ,erröten',  mhd.  rot  ,rot',  ahd.  rotami rosamo  i^rudh-s-men-)  ,Röte'  (hierzu  aisl.  rosmu-fjgll  ,rötliche  Berge*), rudu  ,Röte',  rudig  ,rötlich';  ä-ryderian  ^erröten';  ags.  rüst,  ahd.  as.  f^ ,Rost'  {*'rMh-s-t6)\
3697:tta  »stolpernd  geben',  ags.  strütian  , steif  stehen',  nd.  strutt  ,steif',  nhd. ^  ds.;  mhd.  nhd.  strotzen,  mhd.  striuzen  ,sträuben,  spreizen',  strüz  ,Wider- .  ^'^  Streit^  nhd.  Strauß  ds.  =  mengl.  strüt  ,das  Schwellen,  Streit'; i  hd-  strn^ach  ^Gehüsch^,  gestriuze  , Buschwerk^,  nhd.  (Blumen-) Strauß ; .j^j.jier  auch  as.  strota  ,tuba,  guttur',  mnd.  strote^  strotte  f.,  mhd.  strozze reblö;  Luftröhre',  afries.  strot-bolla  ds.;  ohne  anl.  s- :  ags.  (?ro<w,  ^ro<6;, ^jrl.  throat,  throttle  ,Kehle,  Luftröhre^,  ags.  drot-hoUa  ^Luftröhre',  (engl. Ar^üple)^  ahd.  drozza  , Kehle,  Luftröhre',  nhd.  Drossel  mit  der  Ableitung drosseln,  mhd.  drüzzel  ,Kehle'  und  , Schnauze',  aisl.  prütr  , Schnauze'; aisl.  prütinn  ,geschwollen',  prütna  ,schwellen,  auch  vor  Hochmut',  proti Anschwellung^,  ags.  drütian  ,vor  Hochmut  oder  Zorn  schwellen^; dieselben  Bedeutungen  ^schwellen,  Streit^  auch  in  mir.  trot,  nir.  troid Jgtreit^  (*truzdä7),  cymr.  trythu  , schwellen^,  trythyll  ,wollüstig^;
4820:•eu-d-  , quetschen,  stoßen,  drücken*,  wohl  Erw.  zu  3.  ter-^  iereu-  , reiben'. Alb.  treth  ,verschneide'  (,*zerstoße,  zerquetsche  die  Hoden')  =  lat.  trüdöy •ere  ,stoßen,  fortstoßen,  drängen'  {trüdis  ,eisenbeschlagene  Stange  zum  Fort- Itoßen');  mcymr.  cythrud  , quälen^,  godrud  ,wild'  gorthrud  , Bedrückung' (*-treudo-) ;  mir.  trotaid  , streitet'  (*truzd-  aus  *trud-d-),  cymr.  trythillj  dry- ihill  ,wollüstig'  (daraus  mir.  treitell  , Liebling');  air.  tromm,  cymr.  trwm tSchwer'  (*trudsmo-  , drückend');  got.  usPriutan  ,beschwerlich  fallen',  aisl. kjöta  ,mangeln',  ags.  (ä-)dreotan  unpers.  , ermüden,  überdrüssig  werden', »hd.  (ar-j  hi-)  driozan  ,bedrängen,  belästigen',  nhd.  verdrießen-^  aisl.  Prjötr »widerspenstiger  Mensch',  ahd.  urdrioz  ,Verdruß';  aisl.  Praut  f.  , Kraft- Probe,  Bedrängnis',  ags.   dreat  m.   ,Gedränge,   Gewalttätigkeit,  Drohung',
5692:ven.  Göttin   Vrotah  , Wenderin,  Geburtsgöttin*  (Vetter  Gl.  20,  72);
5771:Gelübde',   und   aksl.   rota   ,Eid';    ablaut.    apr.   wertemmai  ,wir   schwören';
5788:A.  uerd-:  av.  varddva-  ,weich,  locker*,  aksl.  vr^d^,  russ.  vered  , Wunde'; ytred-'.  ai.  avradanta  ,sie  wurden  weich*,  vrandin-  ,mürbe  werdend^* ured-:  apr.  redo  , Ackerfurche',  älter  dän.  vraade,  vrode  , wühlen,  auf- bohren*; uröd-:  lat.  rödöj  -ere  ,nage,  verzehre',  röstrum  (*röd-trom)  n. ,Nage Werkzeug,  Schnauze,  Schnabel',  ags.  wrötan  , wühlen,  graben',  aisl. röta  ds.,  ahd.  ruozit  ,suscitat,  movet',  ags.  wrötj  mhd.  ruozel,  rüezel,  nhd. Rüssel  (*im^ötila-)]  dazu  die  Schwundstufe  in  schwed.  dial.  rota,  ruta , wühlen*;  nach  Frisk  (Etyma  Armen.  30)  dazu  noch  arm.  gercum  , rasieren' aus  *uerd-s-  (ursprüngl.  Aoristbildung).
(eval):1: === not found
```


## [2026-09-14T02:29:16.483Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /rathesthä-/ {print \"LEAF(1-based)=\"NR; print substr($0,1,2500)}' POK_03.txt",
 "description": "Print Pokorny leaf containing rathesthā-"
}
```


### [2026-09-14T02:29:17.389Z] TOOL RESULT

```
LEAF(1-based)=101
  hess.  runde  f.  , Wundschorf.
WF.  II  372,  374.
rent-  ,Sache'?
Unter  dieser  Wurzel  könnten  vereinigt  werden :
ai.  rdtnam  ,Habe,  Besitz,  Gut'  (*?:n<ttd-)  und  ir.  rit  ,Sache'  (*r7}tu-  oder *rentu-)]  auch  lett.  ruotigs  ,mit  allem  versehen'  (falls  aus  *ront-). WP.  II  374.
rep-  ,an  sich  reißen,  raffen'.
Ai.  vermutlich  rdpas-  n.  , Gebrechen,  körperlicher  Schaden,  Verletzung', raphitd-  , elend  (beschädigt)';  gr.  igsTiTO^ai,  , rupfe,  reiße  ab,  fresse',  äQTtvia (Asper  nach  dem  unverwandten  ligm],  ägridCa)^  worüber  s.  *ser-,  serp- , Sichel'),  dgsTtvia  ,Harpye',  hom.  ägrcvLai  dv-r^geipavzo  (Hs.  ävjjgsixpavTo) ', alb.  rjep  , ziehe  aus,  ab,  beraube';  lat.  rapiö,  -ere  ,raffen,  an  sich  reißen, hastig  ergreifen,  rauben'  (a  =  ^]  mir.  recht  ,Zorn,  Wut'  (*reptu-)j  s.  auch rabh-]  germ.  "^rafisjan  ursprüngl.  »körperlich '  strafen'  (Denominativ  eines -es-St.  wie  ai.  rdpas-)]  aisl.  refsa^  ahd.  refsen  ,züchtigen,  strafen',  as.  respian ds.,  ags.  refsanj  repsan,  respan  ,tadeln',  woneben  *rafjan  in  mhd.  reßen =  refsen,  vgl.  mit  Dehnstufe  ags.  gerö&f  n.  (?)  =  geresp  , Anklage,  Tadel';
aisl.  o^afr  ,Streifen  Heilbuttenfleisch',  rejill , Streifen,  Stück  eines  Gewebes' (,abgerissenes'),  ndl.  rafel  , Faser,  ausgezupfter  Faden',  rafelen  ,ausfasern';
lit.  ap-r^pti  , fassen,  ergreifen,  begreifen',  lit.  repUs  (apr.  raples)  f.  PL ,Zange'.
WP.  II  369  f.,  WH.  II  417,  Trautmann  244.
I.  rep-  (rep-?)  ,kriechen,  schleichen'.
Lat.  repö,  -ere  ,kriechen,  schleichen';  ahd.  rebo,  reba,  vepa,  mhd.  rebe ,Schlingschößling' ;  ablaut.  mnd.  wln-räve  ,Weinrebe' ;
lit.  repliöti  ,kriechen',  ablaut.  roplöti  ds.,  lett.  räpdt,  räpt  ds.,  apr.  rlpaiti ,folget';  kaum  dazu  wruss.  rapiixa^  poln.  ropuclia  , Kröte'.
WP.  II  370,  WH.  II  430,  Trautmann  246,  Kluge-Goetze^«  604.
55
866  t
2.  rep-,  rop-  ,Pfahl,  Balken^
Ahd.  rävo  .Sparren',  aisl.  räfr,  räfr  m.,  räf  n.  ,Sparrendach^;  aisl. raptr  m.  , Stock,  Sparren'  (vandal.  PN  Raptus),  ags.  r(ßfter  ds.,  mnd. ra/iier,  rachter  .kleiner  Balken,  Latte';  lit.  replinti  ySiuinchteii,  hinstellen'; aksl.  rSphjhj  repijb  ,Pfahl',  repye  ,TQißoXog^.
WP.  II  370.
res-,  ros-  .fließen'  s.  oben  S.  336  f.
•^^.:
ret(hy  .laufen,  rollen';  roto-  ,Rad'.
Ai.  rdtha-  m.  .Wagen',  ratU- , Wagenlenker',  rdthya-
```


## [2026-09-14T02:29:23.553Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"ni-štā\\|ništā\\|nistā\\|avastā\\|ava-stā\\|stā-.*stand\\|stāna\" KNT_full.txt | head -40",
 "description": "Grep Kent for OP stā- forms"
}
```


### [2026-09-14T02:29:23.623Z] TOOL RESULT

```
23889:ardastāna- sb. ‘window-frame, window cor- 
23892:stāna- ‘place’ (831, §160.Ib; Foy, KZ 35.48; hardly 
29222:ni- + sld-, generalized ništā- (8117, $140. VT),
```


## [2026-09-14T02:29:25.730Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '29180,29280p' KNT_full.txt",
 "description": "Read Kent lexicon around stā-"
}
```


### [2026-09-14T02:29:25.798Z] TOOL RESULT

```
Soh; cf. §6, §116, $152.I, $190.IV, JAOS 56.219- 
20, 58.324; Ву. JAs. 223.244-5; Hz. Арі 305-10. 
Initial s is clear in photographs of DNb. skawh8 
nsm. DNb 8f. skaufim asm. DSe 39f; miswritten 
fkaurim DB 4.65.  skaufai$ gsm. DNb 10. 


Sku^za- sb. ‘Skunkha’, a Scythian rebel: 
Elam. ?ikun-qa. (9100; 58111; $110). Skuza 
nsm. DB 5. 27; DBk 1f. 


Lr 


210 


Skudra- adj. 'Skudrian'; mase. as sb., 
‘Skudra’, a province of the Persian Empire, prob- 
ably Thrace and Macedonia (cf. JNES 2.305): 
Elam. 18-ku-ud-ra, Akk. ts-ku-du-ru ($116). 

(1) Skudrian': Skudra nsm. A?P 25. 

(2) ‘Skudra’: Skudra nsm. DNa 29; DSe 29°; 
Рб 10°; XPh 27 (written Skudrá; see $51, Lg. 
13.298). 


stä- vb. ‘set; (mid.) stand’: Av. síá-, Skt. 

sthd-, Gk. tarnm, Lit. 81810 810, pIE *st(h)à- (576.1, 
$116, $122, $132.2-3). See also upasta-, stdna-. 
a^iMalà imf. mid. (827, §64, §117, §122, 5209, 
§235.11) DB 1.85. 

ava- + std- ‘set down, place, restore’: avastayam 
Ist sg. imf. (§214) DB 1.63, 66, 69. 

ni- + sld-, generalized ništā- (8117, $140. VT), 
‘enjoin, command’ (ef. Altheim, ZII 3.37; Hz. 
ApI 315-8): niyasidyam 1st sg. imf. (5140.1, 
§214) DB 3.91; DZe 8, 11; XV 23f. niyaštāya 
imf. D8n 1; XPh 50; XV 21; nistàya (528.1, $140.- 
IIT) XPh 52. 


stana- sb. ‘place’: Ау. -siána- in сраз., NPers. 
-stán, Skt. sthana-; deriv. of root sta- ($116, $122, 
§132.2-3, §147.1). See also ardastana-. siünam 
asn. XV 20f. 


sta™b- vb. ‘revolt’: NPers. suámb- ‘revolt’, 
perhaps also Skt. sta(m)bh- ‘fasten, hold up, op- 
pose’ (Wb. AbkSGW 29.1.34; Mt. Аз. 1911.637; 
MB Gr. $202). stabava 2d sg. inj. (8216, §224, 
6227.1, $287) DNa 60. 


stiind- sb. ‘column’: Av. stna- masc., stünà- 
fem., NPers. sutūn, Skt. sthiind- (6147.1). stund 
npf. DSf 45 (wrongly nsf. collective, Hz. AMI 
3.68-9). [stünä}] apf. DSg 3°. stünaya uncertain 
form, perhaps 18. (for -àya, $52.IIT, $176, §255; 
hardly adj. asm., with Hinz, ZDMG 95.250; 
wrongly Kent, JAOS 51.227-8) D'Sa 1, A?Hb. 


späda- sb. ‘army’: GAv. spdda-, NPers. sipah, 
Anglo-Indian spahi; in Taxmaspada-, cf. spá- 
maida- (76.V, $83.IT, $116, 5143.11). Possibly 
from pIE *kyd- ‘swell, be great’ (Gray, Lg. 25. 
377-8; cf. §90). ‘ 


spü&maida- sb. ‘camp, war’, meaning shown 
by АКК. version: cf. späda- ‘army’ (883.II), Av. 
hamaspa&maédaya- name of a diety and of his 
festival (Hz. ApI 310-5). spa@maidaya loc. sg. 
DNb 30f. 


OLD PERSIAN 


Sparda- sb. ‘Sardis’, a province of the Persian 
Empire: Elam. iš-par-da, АКК. sa-par-du, Gk. 
Убрбеѕ ($31); with *Sy-, seen in Lydian Sfard- 
(MB Gr. $52; Hz. AMI 3.68-4). See also Spar- 
diya-. Sparda nsm. DB 1.15; DPe 12; DNa 28; 
DSe 27°; DSm 7°; XPh 22. Spardà absm. DPh 
7f; DSf 36; DH 6. 


Spardiya- adj. ‘Sardian’: deriv. (5144.11) to 
preceding; cf. JAOS 54.40, Hz. AMI 3.37. Spar- 
dilya] nsm. A?P 22. Spardiyd npm. DSf 49, 52.
```


## [2026-09-14T02:29:33.372Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for p in 20 66; do n=$((p+21+1)); echo \"=== HRN printed p.$p (1-based leaf $n) ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$n\"' {print}' HRN.txt; done",
 "description": "Print Horn pp. 20 and 66"
}
```


### [2026-09-14T02:29:34.669Z] TOOL RESULT

```
=== HRN printed p.20 (1-based leaf 42) ===
- 20 -
81. est ^Knochen, este 'Knochen, Kern' (vergl. künjeste,
AM. 80 Zeile 5, 163 Zeile 5 v. u., 170 Zeile 3, daneben
auch gün]estej AM. 126 Zeile 4 v. \x,), /estu,
g. äste,
aw. ast-^) *Knochen ; phlv. ast 'Knochen*, astak *Kern;
ai. asthdn-, dsthi-,
kurd. haste 'Knochen etc.; oss. stag, L stäg (228);
minj. asti, sangl. astak.
82. i8tä%, istaky sitak 'Zweig*.
de Lagard e vergleicht arm. cax, aber np. istäx könnte
im Armenischen nur als stax erscheinen. Die ältere
Form ist istak, sitäk, phlv. stak (Bund.). Zu l^sthä-.
83. iistäd, ustaö *Meister'.
aw. "^avastata- 'Vorsteher; phlv. östat, arm. LW. ostat,
LW. kurd. üstä; aiy. usfaä; bei. vastäd (286).
84. istäden stehen*, estäden, Praes. esf-em^)^ sitaden,
p^N^xriD^t* (Jer. 5, 26).
ap. V^stä' (ai. sthü-); päz. estädan.
Im Sähnäme reimt ist *stehe* auf nest, ist also est zu
sprechen {me est I, 136 Vers 125). Ich leite np. estaden,
später istäden, von ap. *adi + l^stä- ab, vergl. phlv.
evar (unter No. 16) und KZ. 32, 581 No. 7.
oss. t. sfln, d. isfün aufstehen* (144) ; sist 'stehe auf*
etc., mit Praefix s (ms).
phlv. ösfätan [ava + \/'stä-) ; bei. östag, vustag n. östay
(402) finden sich im Np. nur dialektisch in g. ustädmün,
vistädmün.
Das PehlevT besass auch die mittlere^) Wurzelform
stT' in stinik (vd. 5 (38), aw. ereöwa-) ^b^%stm 'aufrecht
stehend* (vd. 18 (98) GL), vergl. skr. sthTyat^ (Brähm.)*).
^) Bartholomae, Arische Forschungen II, 112.
*) Auch in Indien spricht man nur Waden,
') Zur mittleren Wurzelform aihä- vergl. Hübschmann, Das
indogermanische Vocalsystem 20, 63.
*J NatürUch könnte man die Pehleviforraen auch steulk, -sten
lesen und skr. sthimän- etc. vergleichen, dessen e (*ai) aus ai/i ent-
standen sein könnte (vergl. Bartholomae, zuletzt Indog. Forsch. I,
490). Die Lesung stenik, sten scheint Bartholomae nach brieflicher
Mitteilung vorzuziehen.
=== HRN printed p.66 (1-based leaf 88) ===
— m —
np. per7' soll auch *Blatt' bedeuten, wie ai. parnd- ;
vgl. ebenso g. par^ kurd. per, af;'. pur, bei. pan (442),
wa;^. paU^ sar. porÄ-, si/n. />arjr (aus "^parnaka-).
294. /mr Voll'.
aw. perena- Voll*; phlv. pur; ai. pmrid-,
LW. kurd. afy. bei. (210) pyr, wa/. sar. pur 'voir.
Ich sehe nicht ein , weshalb auch Geiger, Laut-
lehre des BalücT, np. piir 'v o 1 V statt von aw. perena-^
ai. pfirnd' VolF von ap. pan^-, aw. pouru-, ai. puni-
Viel' ableitet, deren Bedeutung nicht passt. Laut-
lich mussten ja allerdings beide Worte schon im
Pchlevr zusammenfallen , aber pur 'viel' ist hier
bereits aufgegeben. Wenn der Kommentar z. B. aw.
pouru.mahrku' mit pnrmarg wiedergiebt, so hat er
voll Tod\ nicht 'viele tödtend' gemeint ; denn anderen-
falls hätte er rasmarg übersetzen müssen.
295. perfuf enden zerstreuen; erschrecken, pergenden,
phlv. pargantan (Bund.).
ap. "^para -\~ y/kan- (?). Der Bedeutungswechsel ist
allerdings sehr auffällig. Vergl. efgenden (No. 103).
296. pertew 'Glanz*.
para j- ^fap-^ vergl. np. fäßen (No. 372).
297. perdayten 'ausführen, ausleeren; streben, sich be-
mühen* ; Praes. ,perdazem.
phlv. parda/tan (AV.).
aw. *para + l^tac-; Bedeutungswechsel wie bei
end (Ixten (No. 117). Die np. Bedeutung 'ausleeren'
lässt sich aus 'weglaufen lassen' erklären.
von Stackeiberg (briefl. Mitteilung) vergleicht
oss. t. fäldä/jn 'wenden' (ZDMG. 41, 574 Anm. 3),
dessen Bedeutung sich mit der von V^tac- {-\- pard)
unschwer vermitteln lässt.
298. perest 'Verehrer , verehrend*, perestTde7i , perestür^
perestis.
```


## [2026-09-14T02:29:46.110Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for p in 182 158 159 205; do n=$((p+21+1)); echo \"=== HRN printed p.$p ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$n\"' {print}' HRN.txt; done",
 "description": "Print Horn pp. 182, 158-159, 205"
}
```


### [2026-09-14T02:29:47.164Z] TOOL RESULT

```
=== HRN printed p.182 ===
- 182 -
817. fiv'i stallen 'schicken*.
ap. *fra + [^sta-, vergl. a.i. pra -\- l^stho- (Causat.)
'entsenden, entlassen'.
vergl. Sit'/, (ififcwul 'senden'; bei. sastay ^ n. sastay
(363).
818. ferseng 'Parasange', arab. LW. farsax»
ap. 7Taf)f((r(iyy7j; phl. frasang bezw. farsany (Men.,
Bund.).
819. firisfe 'Bote.
phlv. firisfak (Dat. d. 3, 15); chald. LVV. vXpnonp
(das de Lagarde fälschlich = np. pereste setzt) und
NOPIDI.?« (Ezra 4, 9), Hoffmann, Zeitschr. f. Assy-
riologie II, 55 (danach Ezra 5, 6 und 7, 6 zu emen-
diren).
Zu np. ßristäden (No. 817), vergl. skr. prasthita-
aufgebrochen, der sich aufgemacht hat'. Ein aw.
^frcfsfa- (aus ar. *prasth'td', vergl. KZ. 25, 56) ist
etwa als Grundform anzunehmen ^).
^[()bi. ffriste, firzste (AM., d. l ßreste) 'Bote; Engel*.
skr. presita- {pra + |/es-, Causat.) 'gesandt', vergl.
ap. fräisayam, fräisaya ; arm. LW. hresfak 'Engel'.
bei. LW. piristay (202).
Die Etymologie stammt von de Lagarde, zuletzt
Semitica I, 67.
820. fermän 'Befehl'.
ap. framana- 'Befehl'; phlv. farman bezw. framm,
arm. LW. hramcm (davon hramanem), talm. }0*)n.
Allgemein entlehnt.
821. f ermüden 'befehlen', Praes. fermäy-em^ fermayis,
fra -f [/^ma-y vergl. ap. framätar- 'Gebieter ; phlv.
farmütan bezw. framiitan^ framät, framäy(i)sn,
822. fernüs 'töricht, nachlässig, verschlafen; Thorheit'.
ai. pra -f [/^nag- 'verloren gehen, verschwinden'.
*) Justi (Glossay 8. v. asta-) hat die Etymologie fra -|- astO' auf-
gestellt, doch giebt es ein aw. asta- 'Gesandter' nicht, und l/^as- (ai.
ag-, agnöti) heisst nicht 'senden*.
=== HRN printed p.158 ===
— 158 —
kuid. istirk; af/. sförai, 8tar[ya fAuge'); oss. stali
(229) ; wa/. stär, si/n. starf^ stirj ^), sar. /turj^ minj.
asiäri, sangl. ustürak.
712. {2)sitäre Tliegennetz, Schirm' (Öähn. I, 102 Vers 746).
Zu [/^star- ausbreiten' (Rückert, ZDMG. 8, 314).
713. sitebr, setehr (AM. 112 Zeile 4), istebr *stark, gewaltig',
vergl. usttiwär^); arab. LW. istabraq'^^) grober Atlas-
stoff'.
aw. stawra- i^stahlira-, "^str^bhra-) *fest*; phlv. stapr
(vd. 18 (65) GL), d. i. stawr; ai. [^stabh- 'feststellen,
stützen etc., stambha- 'Pfosten, Säule (Hübsch-
niann, ZDMG. 39, 93 Note 1).
oss. vergl. sfawd stark*.
714. sifff/r, ista/r 'Wasserbassin* (eigentlich etwas 'fest
sc. Ummauertes*).
Kh«. esseil j ostor ^ üsor^ sa/r (vergl. isfel etc. bei
Vullers).
aw. sta/ra- 'stark, fest'; vergl. den Stadtnamen
Sfa/r^ Ista/r,
715. sntuvff, sittirg 'stark, gross*.
ai. sthürd- 'dick, breit\ sthülä- 'grob, dick, gross,
feist'; phlv. sturg (ZPGl.).
kurd. nstär; oss. d, sfiir^ t. sfir gross, stark' (232);
bei. istür (167); yidg. üstür.
716. setei*veH, suturven^ esterven 'unfruchtbar' (Schefer,
ehrest, persane II, 188 Zeile 2).
Gehört wohl zu ai. start- 'unfruchtbar ; arm. sferj
(II. No. 258); gr. otttga; lat. sterilis; got. sfairö
(Hörn, KZ. 32, 583 No. 12).
Die neuper?ische Volksetymologie 'Maulesel ähnlich*
ist unwahrscheinlich, zumal es ein Suffix -ve72 'ähnlich*
sonst gar nicht giebt. Oder ist jüd.-pers. H^mriDN
(Is. 54, I) die ursprüngliche Form?
'J Im Satzsandlii entstanden nach Bartholomae, Studien II, 42;
aber verf^l. nhd. stern,. sterben u. v. a. ni. (Hörn, KZ. 32, 588 No. 24).
-) Arm. LW. sioivar.
8J Syr. LAV. ^n^P.DX» <lc Lagnrdo, Oor. Abli. 13.
=== HRN printed p.159 ===
— 159 —
717. ffitem 'unrecht, Gewalt'.
phlv. stahmak^ sfahmaklh bezw. sta/mak^ Rtaxtnakih
gewaltthätig, Gewaltthat'.
Also aus aw. '*8ta/ma-^ vergl. staxlra- (zu dem
Suffixwechsel vergl. oben unter No. 479). Vergl.
N. pr. Gustehm aus '^Vista/^na-,
718. Htetnbe') 'gewaltthätig, streitsüchtig, kampflustig
(Vfs und Kämtn, Seite 7»^ Vers 9), istembe ').
ap. "^stambaka-y vergl. ai. stambha- 'Aufgeblasenheit,
anspruchsvolles Wesen'; arm. LVV. sfambak {nvavrjoo^).
719. ftitTiden, sutä(fe7i 'loben, preisen*, Praes. sitäy-ew,
sifäyis,
aw. i/^stav-y staomi preisen ; phlv. stätaUj stät/ttan,
stai/(i)sn ; ai. \/'stav-^ xtätiti,
oss. sfatm 'loben, rühmen', d. sfitd, t. sfjd 'Lob,
Ruhm' (230); af/. L\V. stayal; wa/. sto-amy siyn. sar.
stdu-am.
720. sutöVy ustör 'Ross' (Srihn. Calc. 1373 Vors 10; Vts
und Ramm, S. 52, V. 4 v. u.).
aw.staora- 'Zugtier; phlv. s^ör 'Zugtier, aber auch
lioss' (Nöldeke, Kärn. 40, Note 5, vergl. störpcVf^
störgäSj ebendas. S. 43 bezw. 41)-); skr. sthätirin^
'Lastpferd, Lastochs (spät); got. st'mr \Stier'.
oss. t. sturtä 'Vieh' (233); kurd. zaza L\V. estör,
dujik. ästori 'Pferd'; Titr. LW. istorr^ astor 'Pferd',
si;'n. stör, sar. stdur^ stdor 'Zugtier, ausgowachscMio.s
Rind', ya/n. «li^wr 'Schaf, Vieh überhaupt' (Tomaschok,
S. 764).
721. sutünf usiün 'Säule'.
ajv. stüna- 'Säule'; phlv. stün, syr. LW. pDCN; ai.
sthunä' 'Säule*.
1) Geschrieben -tenbe,
*) Np. sutör in der angemeinen Bedeutung *Tier* (d. i. Säugetier)
kann ich aus der schon melirfach citirten z/e^. A'^'ärczin. nachweisen,
wo es Fol. 655 r (Berliner Handschrift) heisst: Mor Oleander toiUot
Menschen und sutörän*; der arabische Text des Ihn Sinä, don dor
Perser übersetzt (WZKM. IV, 132), hat aä-ilarräh (I, S. 292; Cuiro
1204 A. IT.).
=== HRN printed p.205 ===
- 205 -
919. gu^lr 'Hilfsmitter, guz^rden (Sahn. I, 61 Vers 519),
ffuzer, guzerden; vergl. näguztr.
Etwa "^viöarija-, vergl. skr. vi -r- i^car- 'ausführen,
vollführen'.
Hat mit reztr (No. 1084) nichts zu tun.
920. gustäx *kühn, frech', busta/ (nicht belegt), vergl.
usta/ (ebenfalls unbelegt).
aw. *vistaka', vergl. stax^'a-, phlv. sta^mak (Darme-
steter. Et. ir. 62)0; P^lv. v{i)stax (Mgn.), arm. LW.
vstah unverzagt'.
921. gtisterden ausbreiten', guster, vergl. blster (No. 218).
ai. vi -f- [/'sfar- ausbreiten'; phlv. v{i)siarta)i aus-
breiten*.
922. guMMen 'zerbrechen, trennen', Praes. gmihem^ gml
kerden Verabschieden, entlassen' (Öähn. I, 74 Vers 236),
pin '^''Di: Verstössen (Jer. 3, 8), vergl. gusll (Vullers),
gtisilänlden (Öähn. I, 88 Vers 494).
phlv. v{i)sastan (Bund.), v{i)sastakih (PPGl.).
Darmesteter, Et. ir. I, 84 hat das Wort auf eine
\/^*Qard' zurückgeführt, die neben ai. gar^, gpidti *zer-
brechen' auf iranischem Boden existirt haben müsse.
Bartholomae (briefl. Mitteilung) denkt an eine Ver-
mischung der beiden synonymen Wurzeln sk^heid- (aw.
sa^d-, hisidyäf; ai. dhed-, chindtti; bei. sindag, n. sinday,
Hübschmann, ZDM6. 44, 559) und k\er- (ai. ^c/r-,
Cfnäti). Ifp. gusisten wäre ap. *visistanaig (aus *«^z-
sid'tanaiy), dagegen gtisilem ap. *visardann (aus sar-
mit dem d von sid-). Er verweist dazu auf die
Wochenschr. f. klass. Phil., 1892 Sp. 397.
Der Inf. guslxten ist ganz unklar.
923. gusäden offnen , sich öffnen ; Praes. gusay-em,
gusüden, gusäyis (Öähn. I, 169 Vers 734).
phlv. v{i)sätan oflfnen'.
Darmesteter, Et. ir. I, 59 Note 3 nimmt als
Grundbedeutung von np. gvsäden sich freuen , indem
') An *v%8taxf'(i' hatten schon Fr. Müller, Kuhn und Schleiclier's
Beiträge V, 139 und Spiegel, Kommentar T, 64 gedacht.
```


## [2026-09-14T02:30:38.536Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SOD entry 67 / pillar ===\"; grep -n \"st'wn\\|stwn\\|pillar\\|ستون\" SOD_pages.txt | head -20",
 "description": "Grep Sogdian dictionary for pillar"
}
```


### [2026-09-14T02:30:38.592Z] TOOL RESULT

```
=== SOD entry 67 / pillar ===
7669:     apstawan       Opst'wn) =>pst}wn                                       Schwartz. HMV        p391, *ptrwxs-
7676:1349 'pst'wn => 'psVw'nh
10713:2395 'stwn M
10870:2455 p>m >stwn       M         (^yU^tj^ ^J^oy^
12870:3200 ckstwny M                                                           n pl69; MDii 1.1, 20; MSP b88
37443:      zerte (zyrtyh, zyrtk2) ©Yaghn. zerta                        11594 zystwn-       B                o*J*<j J j± ^o>
37453:    11595 zystwny C
```


## [2026-09-14T02:30:40.786Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; n=$((1222/2+12)); echo \"leaf guess $n\"; for i in $((n-1)) $n $((n+1)); do echo \"=== KLN_1966 leaf $i ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$((i+1))\"' {print substr($0,1,600)}' KLN_1966.txt; done",
 "description": "Locate Klein p.1222"
}
```


### [2026-09-14T02:30:41.948Z] TOOL RESULT

```
leaf guess 623
=== KLN_1966 leaf 622 ===
 adj.  —  MF.  (=  F.)  persuasif  (fem. persuasive ),  fr.  ML.  persuasivus,  fr.  L.  persuasus, pp.  of  persuadere.  See  persuade  and  -ive.
Derivatives:  persuasive,  n.,  persuasive-ly,  adv., persuasive-ness,  n.
persulfate,  persulphate,  n.  ( chem .)  —  Formed  fr. per-  and  sulfate.
persulfide,  persulfid,  persulphide,  persulphid,  n.
(chem.)  —  Formed  fr.  per-  and  sulfid(e). persulfuric,  persulphuric,  adj.  —  Formed  fr.  per- and  sulfuric.  See  sulfur  and  adj.  suff.  -ic. pert,  adj.,  impudent.  —  ME.,  aphetic  for  OF. apert,  ‘open’,  fr.  L.
=== KLN_1966 leaf 623 ===
r.  v.,  pett-ed,  adj., pett-er,  n.,  pett-ing,  n.
pet,  n.,  peevishness.  —  Of  uncertain  origin;  per¬ haps  fr.  pet,  ‘fondled  animal’.
Derivatives:  pett-ed,  adj.,  pett-ed-ly,  adv.,  petl- ed-ness,  n.,  pett-ish,  adj.
petal,  n.,  one  of  the  leaves  of  the  corolla.  — ModL.  petalum,  fr.  Gk.  -etxaov,  ‘leaf’.  See  pe-
talon.
Derivatives:  petal(l)-ed,  adj.,  petal-ine,  adj.,  pe- talite  (q.v.),  petal-ism,  n.,  petal-oid ,  adj.
petalism,  n.,  a  synonym  of  ostracism.  —  Gk. jr£Tx>aa|i.6;,  method  of  temporary  banishment in  Syracuse;  so  c
=== KLN_1966 leaf 624 ===
oun  formed  fr.  puier,  ‘to  prop,  support’, fr.  VL.  *podiare,  fr.  L.  podium,  ‘an  elevated place,  parapet,  balcony’,  fr.  Gk.  noStov,  ‘base, pedestal,  balcony’,  dimin.  of  nouc,  gen.  :ro86<;, ‘foot’.  See  foot  and  cp.  -pod,  podium,  puy.  Cp. also  appui,  apoggiatura.
Derivatives:  pew,  tr.  v.,  pew-age,  n. pewee,  also  spelled  peewee,  n.,  1)  the  flycatcher; 2)  the  lapwing.  —  imitative  of  the  bird’s  cry. pewit,  peewit,  n.,  the  lapwing;  the  pewee.  —  Imi¬ tative.  See  prec.  word.
pewter,  n.,  any  of  various  alloys  h
```


## [2026-09-14T02:30:59.251Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for i in 764 765 766 767 768; do echo \"=== KLN_1966 leaf $i ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$((i+1))\"' {print substr($0,1,400)}' KLN_1966.txt; done",
 "description": "Locate Klein p.1508"
}
```


### [2026-09-14T02:31:00.627Z] TOOL RESULT

```
=== KLN_1966 leaf 764 ===
shout-er,  n.,  shout-ing,  n. shove,  tr.  and  intr.  v.  —  ME.  shouven,  shoven,  fr. OE.  sciifan,  sceofan,  rel.  to  ON.  skufa,  Dan., Norw.  skyve,  OFris.  skuva,  Du.  schuiven,  OHG. scioban,  MHG.,  G.  schieben,  ‘to  push,  thrust', Goth,  af-skiuban,  ‘to  put  away’,  fr.  I.-E.  base *sqeubh-,  'to  throw,  to  shove’,  whence  also Lith.  skiibti,  ‘to  make  haste
=== KLN_1966 leaf 765 ===
er,  tr.  v.,  shutt-er- less,  adj.,  shutt-ing,  n.
shuttle,  n.  —  ME.  sehytel,  fr.  OE.  scytel,  ‘missile, dart’,  a  gradational  variant  formed  from  the stem  of  sceotan,  ‘to  shoot’;  so  called  from  its being  ‘shot’  across  the  threads  in  weaving.  See shoot  and  dimin.  suff.  -le  and  cp.  prec.  word. Cp.  also  skittle,  which  is  a  doublet  of  shuttl
=== KLN_1966 leaf 766 ===
.  -crximov,  fr.  oxo7reiv,  ‘to  look  at,  ex¬ amine’.  See  -scope.
siderosis,  n.,  1)  deposit  of  iron  in  a  tissue  of  the body,  esp.  in  the  lungs;  2)  inhalation  of  iron
dust  (med.)  —  Medical  L.,  formed  fr.  Gk. <jl8r)po?,  ‘iron’.  See  1st  sidero-  and  -osis. sideward,  adj.  —  Compounded  of  side  and  adj. suff.  -ward.
sideward,  sidewards,  adv.  �
=== KLN_1966 leaf 767 ===
g  to,  or  con¬ taining,  silica.  —  See  silica  and  -ous. silicic,  adj.,  derived  from,  or  pertaining  to,  silica. —  See  silica  and  adj.  suff.  -ic. siliciferous,  adj.,  containing  silica.  —  See  silica and  -ferous.
silicify,  tr.  v.,  to  convert  into  silica;  intr.  v.,  to  be converted  into  silica.  —  See  silica  and  -fy. silico-,  before  a  vowel  silic-,
=== KLN_1966 leaf 768 ===
 Pure  is  dealt  with  as  an  impostor  and  is  believed only  after  he  has  proved  his  identity, simoniac,  n.,  one  who  practises  simony;  adj.,  per¬ taining  to  simony.  —  ML.  simoniacus,  fr.  simo- nia.  See  simony.
Derivatives:  simoniae-al,  adj.,  simoniac-al-ly, adv.
simony,  n.,  the  buying  or  selling  of  sacred  things. —  F.  simonie,  fr.  ML.  simonia,  fr.  S
```


## [2026-09-14T02:31:17.869Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR>=620 && NR<=630 {print \"LEAF1B=\"NR\" :: \"substr($0,1,120)}' KLN_1966.txt; echo \"=== search for page-number lines ===\"; grep -nE \"^[[:space:]]*1(2[0-9][0-9])[[:space:]]*$\" KLN_1966.txt | head",
 "description": "Check Klein leaf numbering"
}
```


### [2026-09-14T02:31:19.032Z] TOOL RESULT

```
LEAF1B=620 :: t  (see  peri-)  and  L.  lympha,  ‘pure  spring water'.  See  lymph.
perimeter,  n.,  outline,  circumference.  —  
LEAF1B=621 :: —  ME .  pinewinkle,  fr.  OE.  pinewincle,  in  which the  first  element  is  prob.  borrowed  fr.  L.  pina, ‘mus
LEAF1B=622 :: fr.  OF.  pere  (F.  poire), fr.  VL.  piratum,  ‘made  of  pears’,  fr.  L.  pirum, ‘pear’.  See  pear.
persalt
LEAF1B=623 ::  adj.  —  MF.  (=  F.)  persuasif  (fem. persuasive ),  fr.  ML.  persuasivus,  fr.  L.  persuasus, pp.  of  persuader
LEAF1B=624 :: r.  v.,  pett-ed,  adj., pett-er,  n.,  pett-ing,  n.
pet,  n.,  peevishness.  —  Of  uncertain  origin;  per¬ haps  
LEAF1B=625 :: oun  formed  fr.  puier,  ‘to  prop,  support’, fr.  VL.  *podiare,  fr.  L.  podium,  ‘an  elevated place,  parap
LEAF1B=626 :: ,  n.
Pharisaism,  n.  —  ModL.  Pharisaismus,  fr.  Gk.
Oapioato?,  ‘Pharisee’.  See  next  word  and  -ism. Phar
LEAF1B=627 :: r-er ,  n. philanthrope,  n.,  a  philanthropist.  —  F.,  fr.  Gk. 9iXdvflpu>Tt05,  ‘loving  mankind,  humane,  ben
LEAF1B=628 :: phlegma- ticus,  fr.  Gk.  9XEYy.xx1.x65,  ‘abounding  in phlegm’,  fr.  9X27^,  gen.  9X2yizxT05.  See phlegm  and 
LEAF1B=629 ::  9607; pi;,  ‘a  bearing, a  being  borne’.  See  prec.  word.
Phormium,  n.,  a  genus  of  liliaceous  plants  (bo
LEAF1B=630 :: he  brain,  delirium (med.)  —  Medical  L.,  formed  fr.  Gk.  9p7)v,  gen. 9psvo 9,  ‘diaphragm,  heart,  mind’ 
=== search for page-number lines ===
29145:1200
29146:1201
29245:1204
29246:1200
29301:1206
29378:1209
29406:1210
29442:1213
29513:1214
29514:1215
```


## [2026-09-14T02:31:23.083Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for p in 1222 1223 1508 1509; do echo \"=== page marker $p ===\"; grep -n \"^$p$\" KLN_1966.txt | head -3; done",
 "description": "Find Klein page markers 1222 and 1508"
}
```


### [2026-09-14T02:31:24.249Z] TOOL RESULT

```
=== page marker 1222 ===
=== page marker 1223 ===
29747:1223
=== page marker 1508 ===
=== page marker 1509 ===
```


## [2026-09-14T02:31:26.281Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '29700,29760p' KLN_1966.txt",
 "description": "Read Klein around page 1223"
}
```


### [2026-09-14T02:31:26.336Z] TOOL RESULT

```
portfire,  n.  —  Formed  fr.  F.  porte-feu,  through the  substitution  of  the  E.  word  fire  for  its  F. equivalent  feu.  Porte-feu  lit.  means  ‘fire-carrier’. See  port,  ‘to  carry’.  (F.  feu,  ‘fire’,  derives  fr.  L. focus.  See  focus.)
portfolio,  n.  —  Form  earlier  porto  folio,  fr.  It. portafoglio,  portafogli,  lit.  ‘carrier  of  leaves’,  fr. portare  (fr.  L.  portare),  ‘to  carry’  and  foglio  (fr. L.  folium),  pi.  fogli,  ‘leaf’.  See  port,  ‘to  carry’, and  folio.
Porthetria,  n.,  a  genus  of  moths,  the  tussock  moth (zool.)  —  ModL.,  fr.  Gk.  TtopD-ryccop,  ‘destroyer.
ravager’,  fr.  7ropff£tv,  ‘to  destroy,  ravage",  freq. of  TTEp&siv,  ‘to  destroy’,  which  is  of  uncertain origin.  For  the  ending  se  1st  suff.  -ia.
porthole,  n.  —  Compounded  of  port, ‘gate;  open¬ ing  in  the  side  of  a  ship’,  and  hole.
portico,  n.,  a  roof  supported  by  columns;  colon¬ nade.  —  It.,  fr.  L.  porticus,  ‘colonnade,  arcade, porch’,  a  derivative  of  portus,  ‘entrance,  harbor'. See  port,  ‘harbor’,  and  cp.  porch,  which  is  a doublet  of  portico.
portiere,  n.,  door  curtain.  —  F.,  ‘door,  gate’,  fr. VL.  *portdria,  fr.  (..porta,  ‘door’.  See  port,  ‘gate’.
portion,  n.  —  ME.  porcioun,  fr.  OF.  porcion,  por¬ tion  (F.  portion),  fr.  L.  portionem,  acc.  of  portio, ‘share,  portion’,  which  stands  for  *partio,  fr  .pars, gen.  partis,  ‘part’.  See  part  and-  ion.  According to  A.  Walde  (Indogermanische  Forschungen, vol.  XXXIX  p.  93)  L.  portio  arose  through  the assimilation  of  the  term  pro  *partione  to  pro  por- tione,  ‘for  (his)  part  or  share’  (see  proportion). Moreover,  the  change  of  *partio  to  portio might  have  also  been  furthered  by  the  endeavor to  avoid  a  confusion  with  partio,  ‘a  bearing, bringing  forth’  (fr.  parere).  Cp.  apportion.
portion,  tr.  v.  —  ME.  portionen,  fr.  OF.  porcion- ner,  portionner  (F.  portionner),  fr.  porcion,  por¬ tion.  See  portion,  n.
Derivatives:  portion-able,  adj.,  portion-al,  adj., portion-al-ly,  adv.,  portion-er,  n.,  portionist (q.v.),  portion-less,  adj.
portionist,  n.,  a  student  in  a  college  who  receives a  certain  allowance  of  food.  —  ML.  portionista, ‘a  scholar  receiving  a  certain  portion  of  food’, fr.  L.  portio,  gen.  -ionis,  ‘part,  portion’.  See portion,  n.,  and  -ist.
Portland  cement.  —  So  called  by  its  inventor,  the English  mason  Joseph  Aspdin,  from  the  re¬ semblance  of  its  color  to  Portland  stone,  i.e. stone  quarried  in  the  isle  of  Portland,  Dorset¬ shire.
portmanteau,  n.,  a  large  traveling  bag  consisting of  two  compartments.  —  F.  porte-manteau,  lit. ‘cloak  bearer’,  fr.  porter,  ‘to  bear,  carry’,  and manteau,  ‘cloak’.  See  port,  ‘to  carry’,  and
mantle.
portmanteau  word,  another  name  for  blend.  —  A term  coined  by  Lewis  Carroll  (pseudonym  for Charles  Lutwidge  Dodgson,  1832-98)  to  denote the  words  coined  by  him  through  the  combina¬ tion  of  two  words.
portolano,  n.,  a  mariner’s  book  containing  de¬ scriptions  of  harbors,  etc.  —  It.,  lit.  ‘pilot’,  fr. porto,  ‘harbor’;  see  port,  ‘harbor’.  For  the  It. suff.  -lano  cp.  ortolano,  ‘kitchen  gardener',  fr. orto,  ‘kitchen  garden’.
portrait,  n.  —  MF.  (=  F.),  prop.  pp.  of  portraire, pourtraire,  ‘to  draw,  design’.  See  portray. Derivatives:  portrait-ist,  n.,  portraiture  (q.v.)
portraiture,  n.,  the  art  of  portraiting;  a  portrait; a  collection  of  portraits.  —  ME.  purtreiture,  fr. M  F.  portraiture,  fr.  portrait.  See  prec.  word  and -ure.
portray,  tr.  v.  —  ME .  portraien,  fr.  MF  .portraire, ‘to  draw,  design’,  fr.  L.  protrahere,  ‘to  draw forth’,  fr.  pro,  ‘forward,  forth’,  and  trahere,  ‘to draw'.  See  1st  pro-,  and  tract  and  cp.  protract. Derivatives:  portray-al,  n.,  portray-er,  n.,  por- tray-ist,  n.
portreeve,  n.,  mayor,  bailiff.  —  ME.  portereve, portreve,  fr.  OE.  portgerefa,  ‘mayor  of  a  town’, fr.  OE.  port,  ‘gate,  harbor,  town’,  and  gerefa, ‘magistrate’.  See  port,  ‘harbor’,  and  reeve,  ‘bail¬ iff’.
portress,  also  porteress,  n.,  a  female  doorkeeper.
—  Formed  fr.  porter,  ‘doorkeeper’,  with  suff. -ess.
Portuguese  man-of-war,  any  hydrozoans  of  the genus  Pharsalia.  —  So  called  from  their  sail¬ like  crest  which  enables  them  to  float  on  the  sea. Portulaca,  n.,  a  genus  of  plants,  the  purslane (bot.)  —  L.  ModL.  Portulaca,  fr.  portulaca,  a derivative  of  portula,  ‘a  small  door’,  dimin.  of porta,  ‘gate,  door’.  See  port,  ‘gate’  and  cp. purslane.
Portulacaceae,  n.  pi.,  the  purslane  family  (bot.)
—  ModL.,  formed  fr.  prec.  word  with  suff. -aceae.
portulacaceous,  adj.  —  See  prec.  word  and  -ace- ous.
posada,  n.,  an  inn.  —  Sp.,  ‘home,  lodging’,  fr. posar,  ‘to  repose,  rest;  to  lodge',  fr.  L.  pausare. See  pose,  ‘to  place’.
posaune,  n.,  1)  a  trombone  (mus.);  2)  a  reed  stop on  an  organ.  —  G.  Posaune,  fr.  OF.  boisine, buisine,  fr.  L.  bucina,  for  *bou-cana,  ‘an  in¬ strument  made  from  the  horn  of  an  ox’,  com¬ pounded  of  bos,  gen.  bovis,  ‘ox’,  and  canere,  ‘to sing’.  See  buccinator.
pose,  tr.  and  intr.  v.,  to  place,  propose.  —  ME. posen,  fr.  OF.  ( =  F.)  poser,  ‘to  halt,  rest ;  to  put, place’,  fr.  VL.  pausare,  ‘to  halt,  pause’  (whence also  It.  posare,  ‘to  rest,  stand ;  to  put,  place’,  Sp. posar,  ‘to  repose,  rest;  to  lodge’,  fr.  pausa, ‘stop,  cessation’  (see  pause);  influenced  in  mean¬ ing  by  an  association  in  Late  L.  with  L.  pos-,  the stem  of  pos-ui  and  pos-itus,  perfect,  resp.  pp.,  of ponere,  ‘to  put,  place’  (s ee  position).  Cp.  appose, depose,  juxtapose,  repose.  Cp.  also  posada. Derivative:  pos-er,  n.
pose,  n.,  attitude.  —  F.,  fr.  poser,  ‘to  place'.  See pose,  ‘to  place’.
Derivative:  pose-y,  adj.
pose,  tr.  v.,  to  embarrass,  puzzle.  —  Shortened fr.  oppose.
Derivative:  pos-er,  n.,  a  puzzling  question. Poseideon,  n.,  name  of  the  6th  month  of  the  Attic Greek  calendar  (corresponding  to  December- January).  —  Gk.  LIocjeiSccov.  lit.  ‘month  dedi¬ cated  to  Poseidon’,  fr.  Iloac'.Scov.  See  next  word. Poseidon,  n.,  the  god  of  earthquakes  and  of  the sea  in  Greek  mythology.  —  L.  Poseidon,  fr.  Gk. IloaciScov  (Dor.  noTstSav),  which  is  of  uncer¬ tain  origin.  According  to  Wilamowitz  the  name ITooetSiov  is  compounded  of  Tronic,  ‘master’.
poseur
posticne
and  85,  a  secondary  form  of  yij,  ‘earth’  (see  po¬ tent  and  Demeter),  hence  lit.  means  'master  of the  earth’.
poseur,  n.,  one  who  poses.  —  F.,  fr.  poser ,  ‘to pose".  See  pose,  ‘to  place’, posit,  tr.  v.,  to  assert.  —  L.  posit  us,  pp.  of  pond, ponere,  ‘to  place’.  See  next  word, position,  n.  —  MF.  (=  F.),  fr.  L .  positidnem,  acc. of  positio,  ‘a  placing,  setting,  situation,  posi¬ tion’,  fr.  positus ,  pp.  of  pond,  ‘I  put,  place,  lay', which  is  a  contraction  of  *pozno,  from  *po- s(i)no,  lit.  ‘I  lay  aside’,  fr.  pref.  po-  and  sind,  ‘I set  down,  leave’.  See  site  and  cp.  component, compose,  composition,  compost,  compound,  con¬ traposition,  depone,  deposit,  dispose,  disposition, entrepot,  exposition,  expound,  imponent,  impose, imposition,  impost,  ‘task’,  impost,  ‘upper  part  of  a pillar’,  impostor,  interposition,  juxtaposition,  op¬ ponent,  oppose,  oviposit,  pone,  ‘an  obsolete  writ’, positive,  post  of  a  soldier,  post  for  conveying  let¬ ters,  posture,  praepostor,  prepositor,  priest,  pro¬ ponent,  propose,  proposition,  propound,  provost, purpose,  repository,  superpose,  suppose,  supposi¬ tion,  suppository,  transpose.  For  po-,  the  prefix of  *po-s(i)nd,  cp.  polish,  pome.
Derivatives:  position,  tr.  v.,  position-al,  adj. positive,  adj.  —  ME .positif  fr.  OF.  (=  F.)  positif (fem.  positive),  fr.  L.  positivus,  ‘settled  by  agree¬ ment’  (opposed  to  ndturdlis,  ‘natural’),  fr.  posi¬ tus,  pp.  of  ponere,  ‘to  place'.  See  position  and -ive  and  cp.  dispositive,  expositive.
Derivatives:  positive,  n.,  positive-ly,  adv.,  posi- tive-ness,  n.,  positivism  (q.v.),  positivist  (q.v.), positiv-ity,  n.
positivism,  n.,  the  philosophical  system  of  Augus¬ te  Comte.  —  F.  positivisme,  coined  by  Auguste Comte  (1798-1857)  fr.  positif,  fem.  positive.  See prec.  word  and  -ism.
positivist,  n.,  an  adherent  of  positivism.  —  See prec.  word  and  -ist.
Derivatives:  positivist-ic,  adj.,  positivist-ic-al-ly, adv.
positron,  n.,  a  positively  charged  electron  (phys. and  chem.)  —  Coined  from  the  abbreviation  of positive)  (eiec)fron.
posologist,  n.,  a  compounder  of  doses.  —  See next  word  and  -ist.
posology,  n.,  the  science  of  doses  (med.)  —  F. posologie,  compounded  of  Gk.  ~6aoc.  ‘how much',  and  -Xoyla,  fr.  -Xoyoq,  ‘one  who  speaks (in  a  certain  manner);  one  who  deals  (with  a certain  topic)'.  The  first  element  derives  fr.  I.-E. base  *q"o-,  whence  also  L.  qui,  quae,  quod, ‘which’,  quis  ?,  ‘who  ?’,  quid  ?,  ‘what  ?’,  OI.  kali, Hitt,  kuwatta,  L.  quot,  ‘how  many?’.  See  what, who  and  cp.  quod,  quid.  For  the  second  element see  -logy.
Derivatives:  posolog-ic-al,  adj.,  posolog-ist,  n. posse,  n.,  1)  possibility;  2)  short  for  posse  comita- tus.  —  ML.  posse,  ‘power’,  fr.  L.  posse,  ‘to  be able’,  infin.  of  possum,  ‘I  can,  am  able’.  See  pos¬ sible.
1222.
1223
posse  comitatus,  the  power  of  the  county  (Jaw).  — ML.  posse  comitatus,  fr.  posse,  ‘power’  (see  prec. word),  and  gen.  of  comitatus,  ‘county’,  fr.  L. comitatus,  ‘escort,  retinue’.  See  county, possess,  tr.  v.  —  ME .possessen,  fr.  OF .possessier, fr.  L.  possessus,  pp.  of  possidere,  ‘to  possess’, which  stands  for  *pots-sidere,  lit.  ‘to  sit  as  a master’.  The  first  element  is  a  contraction  of potis,  ‘able,  mighty,  powerful’,  whence  potens, gen.  potentis,  ‘able,  capable’,  possum  (for  potis sum),  ‘I  am  able’ ;  see  potent  and  cp.  words  there referred  to.  The  second  element  is  rel.  to  sedere, ‘to  sit’,  sidere,  ‘to  sit  down’.  See  sedentary. Derivatives:  possess-ed,  adj.,  possession  (q.v.), possessive  (q.v.),  possessor  (q.v.) possession,  n.  —  ME.  possessioun,  fr.  OF.  (=  F.) possession,  fr.  L.  possessionem,  acc.  of  possessio, ‘a  possessing,  possession’,  fr.  possessus,  pp.  of possidere.  See  prec.  word  and  -ion.
Derivatives:  possession,  intr.  v.,  possession-al, adj .,  possession-ary,  adj.,  possession-ed,  adj. possessive,  adj.  —  MF.  (=  F.)  possessij  (fem. possessive),  fr.  L.  possessivus,  ‘relating  to  pos¬ session,  possessive’,  fr.  possessus,  pp.  of  possi¬ dere;  see  possess  and  -ive.  L.  possessivus  was coined  by  the  Roman  rhetorician  Marcus  Fa- bius  Quintilianus  (cca  35-cca  95  C.E.)  to  trans¬ late  Gk.  JCTr,Tix6?,  ‘acquisitive;  possessive’  (fr. XT&affai,  ‘to  get  for  oneself,  acquire’). Derivatives:  possessive,  n.,  possessiv-al,  adj., possessive-ly,  adv.,  possessive-ness,  n. possessor,  n.  —  ME.  possessour,  fr.  MF.  (=  F.) possesseur,  fr.  L.  possessorem,  acc.  of  possessor, ‘possessor’,  fr.  possessus,  pp.  of  possidere.  See prec.  word  and  agential  suff.  -or. possessory,  adj.  —  Late  L.  possessorius,  ‘relating to  possession’,  fr.  L.  possessor.  See  prec.  word and  adj.  suff.  -ory.
Derivative:  possessori-ness,  n. posset,  n.,  a  drink  of  hot  milk  curdled  with  ale  or wine.  —  ME.  poshote,  of  uncertain  origin. Derivative:  posset,  tr.  and  intr.  v. possibilist,  n.,  an  adherent  of  a  political  party which  aims  only  at  the  realization  of  what  is immediately  possible.  —  F.  possibiliste,  tr.  Sp. posibilista,  fr.  posible,  ‘possible’,  fr.  L.  possibilis. See  possible  and  -ist.
possibility,  n.  —  ME.  possibilite,  fr.  OF.  possi- bilite  (F.  possibility,  fr.  L.  possibilitatem,  acc.  of possibilitas,  fr.  possibilis.  See  next  word  and -ity.
possible,  adj.  —  F.,  tr.  L.  possibilis,  ‘possible  ,  fr. possum,  ‘I  am  able’.  See  possess  and  -ible. Derivatives:  possible,  n.,  possible-ness,  n.,  pos- sibl-y,  adv.
’possum,  n.  —  Aphetic  for  opossum, post,  n.,  pillar.  —  ME.,  fr.  OF.,  fr.  L.  postis, ‘doorpost’,  for  *por-stis,  lit.  ‘standing  out’, which  is  cogn.  with  OI.  pp-ftham,  ‘back,  roof, peak',  Avestic  par-shti  (dual),  ‘back’,  Gk.  rca- <JTas,  gen.  mxoTtkSoq  (fr.  *7tap<i'raS- ) ,  a  col¬ lateral  form  of  me paava?,  gen.  rrocpaaTaSos,
!■
‘porch  in  front  of  the  house,  colonnade’,  MHG. virst,  ‘ridgepole’,  Lith.  pirstas,  OSlav.  pristu, prustH,  ‘finger’,  lit.  ‘something  standing  out’, OHG.  first,  MHG.  virst,  G.  First,  ‘ridgepole’, MDu.  verste,  vorst,  OS.  first,  OE.fierst,  first,  of s.m.  See  1st  pro-  and  state.
Derivative:  post,  tr.  v.
post,  n.,  the  place  where  a  soldier  is  stationed.  — MF.  (=  F.)  paste,  fr.  It.  posto,  fr.  VL.  postum, fr.  L.  positum,  neut.  pp.  of  ponere,  ‘to  put, place’.  See  position.
Derivative:  post,  tr.  v.
post,  n.,  office  for  conveying  letters.  —  MF. (=  F.)  paste,  fr.  It.  posta,  fr.  VL.  posta,  whose original  meaning  was  ‘a  place  where  men  are  sta¬ tioned  for  the  conveyance  of  messages  or  let¬ ters’,  fr.  L.  ( mansio )  posita,  ‘a  fixed  halting  place or  station’,  fem.  pp.  of  ponere,  ‘to  put,  place’. See  position  and  cp.  prec.  word.  Cp.  also  pos¬ tilion,  poste  restante.
Derivatives:  post,  intr.  and  tr.  v.,  post-age,  n., post-al,  adj., postal-ly,  adv. post,  adv.,  with  post  horses;  rapidly.  —  From  the phrase  to  ride  post,  abbreviation  of  to  ride  in post.  See  post,  ‘office  for  conveying  letters’, post-,  pref.  meaning  ‘behind,  after’.  —  L.,  fr.  post, ‘behind,  after’,  fr.  earlier  *pos-ti,  cogn.  with Toch.  B  postam,  ‘after’,  Arm.  est,  ‘after’,  Arca¬ dian  and  Cypriote  no;,  Dor.  ttoti,  ‘toward,  to, near,  close  by’,  OSlav.  po,  ‘behind,  after’,  poz- du,  ‘late’  (adj.),  poz-de,  ‘late’  (adv.),  Lith.  pas,  ‘at, by’;  fr.  I.-E.  *pos-,  enlargement  of  *po-,  whence Gk.  X7TO,  ’from’,  L.  ab,  ‘away  from’.  Cp.  OI. pas-ca,  Lith.  pasu-Zcid, pas-fan  (which  prob.  stand for  I.-E.  *pos-q™o),  ‘behind,  after’.  See  ab,  apo- and  cp.  posterior,  postilion.  Cp.  also  the  pref.  in polatouche  and  in  Pomerania,  Prussia, postdate,  tr.  v.,  to  assign  (to  a  document)  a  date later  than  the  real  date.  —  Compounded  of  post- and  date,  v.  See  date,  ‘point  of  time’, postdate,  n.,  a  date  assigned  (to  a  document)  later than  the  real  date.  —  Compounded  of  post-  and date,  ‘point  of  time’.
```


## [2026-09-14T02:31:36.124Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^15[01][0-9]$\" KLN_1966.txt | head -20",
 "description": "Find Klein page markers around 1508"
}
```


### [2026-09-14T02:31:37.195Z] TOOL RESULT

```
36514:1501
36536:1503
36576:1505
36623:1507
36745:1513
36787:1514
36788:1515
37642:1510
```


## [2026-09-14T02:31:39.770Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '36623,36680p' KLN_1966.txt",
 "description": "Read Klein pages 1507-1509"
}
```


### [2026-09-14T02:31:39.835Z] TOOL RESULT

```
1507
starvation,  n.  —  A  hybrid  coined  fr.  starve,  a word  of  Teut.  origin  and  -ation,  a  suff.  derived fr.  L.  -dtio,  gen.  -ationis.
starve,  intr.  v.,  to  die  from  hunger;  tr.  v.,  to  cause to  starve.  —  ME.  sterven,  ‘to  die’,  fr.  OE.  steor- fan,  rel.  to  OFris.  sterva,  Du.  sterven,  OS. ster'ban,  OHG.  sterban,  MHG.,  G.  sterben,  ‘to die’,  and  to  ON.  stjarfi ,  ‘tetanus’,  and  cogn.  with Gk.  OT^pcpvtoi;  (Hesychius),  ‘stiff,  rigid’,  axsp- 90?,  ‘hide,  skin’,  OSlav.  strublu,  ‘strong, hard’.  All  these  words  derive  fr.  I.-E.  *sterbh-, a  -Wi-cnlargement  of  base  *ster-,  ‘stiff,  rigid’. See  stare  and  cp.  torpedo,  torpid.
Derivatives:  starve-ling,  n.  and  adj.
stasis,  n.,  stoppage  of  the  circulation  of  a  fluid  in the  body.  —  Medical  L.,  fr.  Gk.  axdaic,  ‘a standing  still’,  which  is  rel.  to  axaxoc,  ‘placed’, verbal  adj.  of  I<JT7)|zi  (for  *m-aT7]ii'. ),  ‘I  cause to  stand’,  fr.  I.-E.  base  *sta-,  ‘to  stand’.  See state  and  cp.  the  second  element  in  apostasy, metastasis.
stassfurtite,  n.,  a  variety  of  boracite  (mineral.)  — Named  after  Stassfurt  in  Prussia.  For  the  end¬ ing  see  subst.  suff.  -ite.
state,  n.  —  ME.  stat,  fr.  OF.  estat  (F.  etat),  fr.  L. status,  ‘posture,  position,  condition,  state,  pub¬ lic  affairs,  constitution’,  fr.  pp.  stem  of  stare,  ‘to stand’,  which  is  rel.  to  sistere,  ‘to  place,  stand, stand  still’,  fr.  I.-E.  base  *st(h)a-,  ‘to  stand’, whence  also  OI.  tisfhati,  ‘stands’,  dstham,  ‘I stood’,  stitdh,  ‘standing’,  sthatar-,  ‘ruler,  guide’, sthatf,  ‘that  which  stands’,  OPers.  and  Avestic sta-,  ‘to  stand’,  Avestic  hishtaiti,  ‘stands’,  Toch. shtam,  ‘I  stand’,  Gk.  I'a-rqut  (for  ),  ‘I
cause  to  stand,  I  set,  place;  I  stand’,  laxrjxa,  ‘I stand’,  axdaip,  ‘a  standing’,  OSlav.  stanjq,  stati, ‘to  place  oneself’,  stojQ,  stojati,  ‘to  stand’,  Lith. stdju,  stdti,  ‘to  place  oneself’,  Goth.,  OE.  start- dan,  ‘to  stand’,  OIr.  tair-(s)issim,  ‘I  remain  stand¬ ing’,  sessam  and  sessed,  ‘the  act  of  standing’, and — with  -n-enlargement — Gk.  laxdvco  (a new  formation  for  ‘I  cause  to  stand,  I
set,  place’.  Arm.  stanam,  ‘I  buy  at  an  auction, acquire’,  L.  de-stindre,  ‘to  make  firm,  fasten ;  to intend,  devote,  destine’,  ob-stinare,  ‘to  set  one’s mind  firmly  on,  persist  in’,  praestinare,  ‘to  buy, purchase’,  Alb.  shton,  ‘I  increase,  augment’.  See stand  and  cp.  status,  estate,  etat,  which  are doublets  of  state.  Cp.  also  aerostat,  anastasis, Anastasius,  apostasy,  apostate,  aposteme,  ap- preteur,  armistice,  arrest,  assist,  astatic,  astatine, catastasis,  bezesteen,  bostangi,  circumstance, consist,  constant,  constitute,  contrast,  cost,  desist, destine,  destitute,  diastase,  distant,  ecstasy,  en- statite,  epistemology,  establish,  etage,  etagere, exist,  extant,  gyrostat,  heliostat,  hemostasis, Hindustani,  histo-,  hypostasis,  iconostasis,  im- postume,  insist,  instant,  institute,  interstice,  meta¬ stasis,  obstacle,  obstetric,  obstinate,  oust,  peri- stalith,  persist,  post,  ‘pillar’,  presto,  prostate, prostitute,  resist,  rest,  ‘to  remain’,  restitute,  res¬ tive,  rheostat,  stable,  n.  and  adj.,  staddle,  stad-
holder,  stadium,  stage,  staith,  stall  and  words there  referred  to,  stamen  and  words  there  re¬ ferred  to,  stamnos,  stance,  stanch,  stanchion, stanza,  stapes,  stasis,  stater,  static,  Statice,  sta¬ tion,  stationer,  statistics,  stato-,  stator,  stato- scope,  statue,  stature,  statute,  stay,  ‘to  prop,  sup¬ port’,  stay,  ‘to  stand  still’,  stead,  steed,  steel, sterling,  stet,  stool,  stound,  stow,  ‘to  pack’,  stud of  horses,  stud,  ‘peg,  nail’,  Stundist,  subsist,  sub¬ stance,  substantive,  substituent,  substitute,  super¬ stition,  system,  thana,  thermostat,  vestibule  and the  suff.  in  celestial.
Derivatives:  state,  adj.  and  tr.  v.,  stat-ed ,  adj., stat-ed-ly,  state-ly,  adj.,  state-li-ness,  n.,  state¬ ment,  n.
stater,  n.,  one  who  states.  —  Formed  fr.  state,  v.
(see  state),  with  agential  suff.  -er. stater,  n.,  standard  coin  (of  gold  or  of  silver).  — L.  stater,  fr.  Gk.  rjxaxTjp,  which  is  rel.  to (for  *ai-errt)[ti),  ‘I  cause  to  stand’, meaning  also  ‘I  weigh’,  fr.  I.-E.  base  *sta-,  ‘to stand’.  See  state,  n.,  and  words  there  referred  to and  cp.  esp.  sterling.
static,  adj.,  1)  acting  by  mere  weight;  2)  at  rest. —  ModL.  staticus,  fr.  Gk.  oxaxtxd?,  ‘causing to  stand,  skilled  in  weighing’,  fr.  axaxos, ‘placed;  standing’,  verbal  adj.  of  laxYjpu  (for  *cn- ox7)p.i ),  ‘I  cause  to  stand’,  fr.  I.-E.  base  *sta-,  ‘to stand’.  See  state  and  adj.  suff.  -ic  and  cp. aerostat  and  words  there  referred  to. Derivatives:  static,  n.,  static-al,  adj.,  static-al-ly, adv.,  statics  (q.v.)
Statice,  n.,  a  genus  of  plants  of  the  family  Plum- baginaceae  ( hot .)  —  L.,  fr.  Gk.  axaxixr;,  ‘an astringent  plant’,  prop.  fern,  of  the  adj.  axa- ■u.niq,  ‘causing  to  stand;  stanching  blood’,  used as  a  noun;  so  called  because  of  the  astringent properties  of  the  plant.  See  prec.  word, statics,  n.,  mechanics  dealing  with  the  equilib¬ rium  of  forces.  —  Fr.  Gk.  axaxixr;  (scil.  xf/_- vr;), ‘the  art  of  weighing’,  fr.  uxa xix4s,  ‘skilled in  weighing’.  See  static  and  -ics. station,  n.  —  ME.  stacioun,  fr.  MF.  (=  F.)  sta¬ tion,  fr.  L.  stationem,  acc.  of  statio,  .‘act  of  stand¬ ing,  place,  position,  office;  station’,  fr.  stat-(um), pp.  stem  of  stare,  ‘to  stand’.  See  state  and  -ion. Derivatives:  station,  tr.  v.,  stational  (q.v,), stationary  (q.v.),  stationer  (q.v.) stational,  adj.,  pertaining  to  a  station.  —  L.  sta- tiondlis,  fr.  statio,  gen.  -onis.  See  prec.  word  and adj.  suff.  -al.
stationary,  adj.,  not  moving;  at  rest.  —  ME. stacionarye,  fr.  MF.  ( —  F.)  stationnaire,  fr.  L. stationarius,  ‘pertaining  to  a  post  or  station’,  fr. statio,  gen.  -onis.  See  station  and  adj.  suff.  -ary. Derivative:  stationary,  n. stationer,  n.,  1)  formerly,  a  bookseller  or  pub¬ lisher;  2)  a  person  who  sells  paper,  pens,  pen¬ cils,  ink  and  other  writing  materials.  —  ME. stacyonere,  ‘bookseller’,  fr.  ML.  stationarius,  fr. L.  statio,  gen.  -onis,  ‘a  station’ ;  he  was  so  called because  he  usually  had  a  permanent  place  or
station  (in  contradistinction  to  an  itinerant  ven¬ dor).  See  station  and  agential  suff.  -er. Derivatives :  stationer-y,  adj.  and  n. statist,  n.,  statistician.  —  G.  Statist,  back  forma¬ tion  fr.  Statistik.  See  statistics, statistic,  adj.,  statistical.  —  See  statistical, statistic,  n.  —  The  same  as  statistics, statistical,  adj.  —  Formed  fr.  statistic,  n.,  with adj.  suff.  -al.
statistician,  n.  —  Formed  fr.  statistic,  n.,  with suff.  -ian.
statistics,  n.  —  Fr.  earlier  statistic,  fr.  Gl|.  Sta¬ tistik,  coined  by  the  German  statistician  Gott¬ fried  Achenwall  (1719-1772)  in  1748,  fr.  ModL.
( collegium )  statisticum,  ‘(a  college)  occupying  it¬ self  with  statistics’,  formed  fr.  L.  status,  ‘state, condition’,  and  suff.  -isticum.  See  state  and  the suffixes  -istic  and  -ics.
statistology,  n.,  the  study  of  statistics.  —  A  hy¬ brid  coined  fr.  statistics,  a  word  of  L.  origin,  and Gk.  -Xoyia,  fr.  -X6yoc,  ‘one  who  speaks  (in  a certain  manner) ;  one  who  deals  (with  a  certain topic)’.  See  -logy.
stato-,  combining  form  meaning  ‘standing,  fixed’.
—  Gk.  axaxo-,  fr.  axxxo?,  ‘standing’.  See static.
stato-,  combining  form  meaning  ‘state’.  —  See state.
statoblast,  n.,  a  winter  bud  (zool.)  —  Compound¬ ed  of  stato-  ‘fixed’,  and  Gk.  flXaaxd?,  ‘bud, sprout,  shoot’.  See  -blast, stator,  n.,  the  stationary  part  in  a  power  genera¬ tor.  —  ModL.,  formed  fr.  L.  stat-(um),  pp.  stem of  stare,  ‘to  stand’.  See  state  and  agential  suff. -or.
statoscope,  n.,  an  instrument  for  measuring  at¬ mospheric  pressure.  —  Formed  fr.  stato-,  ‘fixed’, and  Gk.  -oxomov,  fr.  axo tceiv,  ‘to  look  at, examine’.  See  -scope.
statuary,  adj.,  pertaining  to,  or  suitable  for,  stat¬ ues.  —  L.  statuarius,  ‘of  statues’,  fr.  statua.  See statue  and  adj.  suff.  -ary. statuary,  n.,  a  maker  of  statues.  —  L.  statuarius, ‘a  maker  of  statues',  prop,  an  adj.  used  as  a noun.  See  statuary,  adj.
statuary,  n.,  the  art  of  making  statues.  —  L.  sta- tuaria  (scil.  ars),  fern,  of  statuarius,  ‘of  statues’. See  statuary,  adj.
statue,  n.  —  ME.,  fr.  OF.  (=  F.)  statue,  fr.  L. statua,  ‘image,  statue’,  prop,  ‘that  which  is  set up’,  back  formation  fr.  statuere,  ‘to  set  up’,  from the  stem  of  stare,  ‘to  stand’.  See  state  and  cp. words  there  referred  to.
Derivatives:  statue,  tr.  v.,  statu-ed,  adj.,  statue¬ like,  adj.,  statuesque  (q.v.) statuesque,  adj.,  1)  of,  or  like,  a  statue;  2)  stately.
—  A  hybrid  coined  fr.  L.  statua  (see  prec.  word) and  -esque,  a  suff.  of  Italian,  ult.  Teut.,  origin. Derivatives :  statuesque-ly,  adv.,  statuesque-ness, n.
statuette,  n.,  a  small  statue.  —  F.,  dimin.  of statue.  See  statue  and  -ette.
stature,  n.  —  ME.,  fr.  OF.  (=  F.)  stature,  fr. earlier  estature,  fr.  L.  statura,  ‘height,  size, stature’,  lit.  ‘an  upright  posture’,  fr.  stat-(um), pp.  stem  of  stare,  ‘to  stand’.  See  state  and  -ure. Derivative:  statur-ed,  adj. status,  n.  —  L.,  ‘mode  of  standing,  position,  at¬ titude’,  fr.  stat-(um),  pp.  stem  of  stare,  ‘to  stand’. See  state.
status  in  quo,  status  quo,  unaltered  condition.  — L.,  lit.  ‘condition  in  which  (something  is)’.  See prec.  word.
statutable,  adj.,  statutory.  —  Formed  from  next word  with  suff.  -able.
Derivative:  statutabl-y,  adv. statute,  n.  —  ME.  statut,  fr.  OF.  (=  F.)  statut,  fr. earlier  estatut,  fr.  Late  L.  statiitum,  prop.  neut. pp.  of  statuere,  ‘to  set  up,  establish,  constitute’, lit.  ‘to  cause  to  stand’,  formed  fr.  stat-(um),  pp. of  stare,  ‘to  stand’.  See  state  and  cp.  constitute, destitute,  institute,  prostitute,  restitute,  substitute. Derivative:  statut-ory,  adj. staunch,  also  stanch,  adj.  —  ME.,  fr.  OF.  estanch, fern,  estanche  (F.  etanche),  ‘watertight;  reliable’, back  formation  fr.  OF.  estanchier,  ‘to  check  the flow’.  See  stanch,  v.
stauro-,  before  a  vowel  staur-,  combining  form meaning  ‘cross’.  —  Gk.  oxaupo-,  axaup-,  fr. axaupd?,  ‘stock,  pile,  cross’.  See  steer,  ‘to  direct’, and  cp.  words  there  referred  to. stauroiite,  n.  (mineral.)  —  Lit.  ‘cross-stone’,  fr. Gk.  oxaup6?,  ‘cross’,  and  Xtftoc.  ‘stone’.  See stauro-  and  -lite.
Derivative:  staurolit-ic. ,  adj. stauroscope,  n.,  an  instrument  for  determining the  position  of  the  planes  of  vibrations  in  crys¬ tals.  —  Compounded  of  stauro-  and  Gk.  -0x6- 7tiov,  fr.  GY.oneXv,  ‘to  look  at,  examine’.  See -scope.
Derivative:  stauroscop-ic,  adj. stave,  n.,  1)  one  of  the  pieces  of  a  barrel;  2)  staff ( mus .)  —  Back  formation  fr.  staves,  pi.  of  staff. Derivatives:  stave,  tr.  \.,stav(e)-able,  adj., stave- less,  adj.
stavesacre,  n.,  a  kind  of  larkspur.  —  ME.  staphi - sagrie,  staphisagre,  fr.  L.  staphisagria  (whence also  F.  staphisaigre ),  fr.  Gk.  azctyl'  dypia,  lit. ‘wild  raisin’.  Lxa9t?  also  aaxa?!;,  ‘raisin’,  is prob.  rel.  to  0x390X7;,  ‘bunch  of  grapes’,  oxeu- 91) Xa  (pi.),  ‘mass  of  pressed  grapes';  see  sta- phylo-.  ’  Aypia  is  fern,  of  civ  pi  op.  ‘wild’,  which derives  fr.  dyp6p,  ‘field’ ;  see  agrio-. stay,  n.,  a  large  rope  for  supporting  a  mast.  — - ME.  stey,  stay,  fr.  OE.  sucg,  rel.  to  ON.,  Du. stag,  MLG.  stack,  MDu.  staeye,  ‘rope  for  sup¬ porting  a  mast’,  lit.  ‘prop,  support’.  OF.  estaie, ‘prop,  support’,  is  a  Middle  Dutch  loan  word. See  stay,  ‘to  prop,  support’.
Derivative:  stay,  tr.  v.,  to  fasten  with  stays, stay,  tr.  v.,  to  prop,  support.  —  MF.  estaier  (F. itayer),  fr.  estaie  (F.  dtai ),  ‘prop,  support’,  fr. MDu.  staeye,  which  is  rel.  to  Du.  staan,  OHG. stan,  Goth.,  OE.  standan,  ‘to  stand’.  See  stand.
stay
steimerous
1508'
I3UV
stay,  n.,  support;  pi.,  a  corset.  —  MF.  estate.  See prec.  word.
stay,  intr.  v.,  to  stand  still,  rest,  remain;  intr.  v., to  check,  stop;  to  restrain.  —  ME.  steyen,  fr. OF.  ester,  ‘to  be’,  prop,  ‘to  stand’,  fr.  L.  stare. Cp.  It.  stare,  O Proven?,  and  Sp.  estar,  ‘to  stand; to  be’,  and  see  state.  (F.  etre,  ‘to  be’,  is  not  re¬ lated  to  ester,  but  derives  fr.  VL.  *essere,  fr.  L. esse,  ‘to  be’.
stead,  n.  —  ME.  stede,  fr.  OE.  stede,  ‘act  of  stand¬ ing;  place’,  rel.  to  OS.  stedi,  ON.  stadr,  Dan. sted,  Swed.  stad,  Du.  stede,  stee,  ‘place’,  stad, ‘town’,  OFIG.,  MHG.  stat,  G.  Stdtte,  ‘place’,  G. Stadt,  ‘town’,  Goth,  stops,  ‘place’;  fr.  I.-E.  base *sta-,  ‘to  stand’.  See  state  and  cp.  stand.  Cp.  also staddle,  stithy,  and  the  first  element  in  stad- holder.
Derivatives:  stead,  tr.  v.,  stead-y,  adj.,  tr.  and intr.  v.,  and  n.,  stead-i-ly,  adv.,  stead-i-ness,  n. steadfast,  adj.  — -  ME.  stedefast,  fr.  OE.  stedefaest. See  stead  and  fast,  adj.
Derivatives:  steadfast-ly,  adv.,  steadfast-ness,  n. steak,  n.  —  ME.  steyke,  steke,  fr.  ON.  steik; prop,  ‘something  stuck  (on  a  spit)’,  and  rel.  to ON.  steikja,  ‘to  roast  on  a  spit’,  and  to  OE. stician,  ‘to  stick’.  See  stick,  v. steal,  tr.  and  intr.  v.  —  ME.  stelen,  fr.  OE.  stelan, rel.  to  OS.  stelan,  ON.,  Norw.,  OFris.  stela, Dan.  stjeele,  Swed.  stjdla,  Du.  stelen,  OHG.  ste¬ lan,  MF1G.  stein,  G.  stehlen,  Goth,  stilan,  and prob.  cogn.  with  Gk.  axepeiv,  Att.  axepiaxEtv, ‘to  deprive  of’,  Mir.  serbh  (for  *ster-wa),  ‘theft’, fr.  I.-E.  base  *ster-,  ‘to  steal’.  The  change  of I.-E.  *ster-  to  *stel-  in  Tent,  is  prob.  due  to  the influence  of  OS.,  OE.,  OHG.  helan,  OFris.  hela, ‘to  hide,  conceal’  (see  hall),  with  which  the  verb steal  is  often  associated.  Cp.  stalk,  ’to  walk furtively’.
Derivatives:  steal-er,  n.,  steal-ing,  adj.,  steal- ing-ly,  adv.,  steal-th,  n.,  stealth-y,  adj.,  steal-th- i-ly,  adv.,  steal-th-i-ness,  n. steam,  n.  —  ME.  stem,  steme,  ‘steam,  flame’,  fr. OE.  steam,  ‘exhalation,  steam,  vapor’,  rel.  to Du.  stoom,  ‘steam’ ;  of  unknown  origin. Derivatives:  steam,  intr.  and  tr.  v.,  steam-er,  n., steam-y,  adj.,  steam-i-ness,  n. stean,  steen,  n.,  a  vessel  for  liquids  or  foods.  — • ME.  stene,  fr.  OE.  stSne,  rel.  to  OHG.  steinna, ‘stone  jug’,  and  to  OE.  stan,  ‘stone’.  See  stone. Derivative:  stean-ing,  steen-ing,  n. stearate,  n.,  a  salt  of  stearic  acid  ( chem .)  —  See stearin  and  chem.  suff.  -ate. stearic,  adj.,  of,  or  derived  from,  stearin.  —  See stearin  and  adj.  suff.  -ic. stearin,  n.,  a  white,  crystalline  compound  found in  animal  and  vegetable  fats  (chem.)  —  F.  stea- rine,  coined  by  the  French  chemist  Marie-Eugene Chevreul  (1786-1889)  fr.  Gk.  arsap,  ‘fat’.  See steato-  and  -in.
stearinery,  n.,  manufacture  of  stearin.  —  Formed from  prec.  word  with  suff.  -ery. steat-,  form  of  steato-  before  a  vowel.
steatite,  n.,  a  massive  variety  of  talc  (mineral.)  — L.  steams ,  steatites,  fr.  Gk.  *axeaxiTi<;  (or -Err]?)  Xi&o?,  fr.  atiap,  gen.  ax£axo?,  ‘fat, tallow’.  See  steato-  and  subst.  suff.  -ite. Derivative:  steatit-ic,  adj. steato-,  before  a  vowel  steat-,  combining  form meaning  ‘fat,  tallow’.  — Gk.  ctxeaxo-,  axsax-, fr.  ax£ap,  gen.  crxeaxo?,  ‘fat,  tallow’,  which  is rel.  to  cttIS,  ‘pebble’,  at  iky,  ‘drop’.  See  stone and  cp.  words  there  referred  to. steatopygia,  n.,  an  abnormal  accumulation  of  fat on  the  buttocks  of  certain  races.  —  ModL., compounded  of  steato-  and  Gk.  ns>yin  ‘but¬ tocks’.  See  pygal  and  1st  -ia.
Derivatives:  steatopyg-ic,  steatopyg-ous,  adjs. steatosis,  n.,  fatty  degeneration.  —  ModL.,  fr.  Gk.
oxeap,  gen.  miitoc,  ‘fat’.  See  steato-  and  -osis. steed,  n.,  a  horse,  esp.  a  riding  horse.  —  ME. stede,  fr.  OE.  steda,  ‘horse,  stallion",  rel.  to  ON. stod,  OE.  stod,  ‘stud’.  See  stud,  ‘collection  of horses’.
Derivatives:  steed-less,  adj.,  steed-like,  adj. steel,  n.  —  ME.  stel,  fr.  OE.  stele,  stel,  style,  rel. to  OS.  stehli,  ON.,  MLG.  stal,  Dan.  staal,  Swed. stal ,  MDu.  stael,  Du.  staal,  OHG.  stahal,  MHG. stahel,  stal,  G.  Stahl,  ‘steel’,  and  cogn.  with OPruss.  stakla,  ‘steel’.  These  words  prob.  meant orig.  ‘something  firm  or  hard’,  and  are  cogn. with  OI.  stakati,  ‘resists’,  Avestic  staxta-,  ‘firm, solid’,  staxra-,  ’severe’  (said  of  the  cold  in  win¬ ter).  All  these  words  are  prob.  traceable  ult.  to I.-E.  base  *sta-,  ‘to  stand’.  See  state. Derivatives:  steel,  adj.  and  tr.  v.,  steel-y,  adj., steel-i-ness,  n.
steelyard,  n.,  a  kind  of  balance.  —  From  the  Steel¬ yard,  factory  of  the  Hanse  towns  in  London,  er¬ roneous  translation  of  MLG.  stdlhof  ‘sample yeard’,  fr.  stal,  ‘sample’,  which  was  confused with  MLG.  stal,  ‘steel’  (see  steel).  For  the  sec¬ ond  element  see  yard, steen,  n.  —  A  var.  spelling  of  stean. steenbok,  n.,  a  small  African  antelope.  —  Du.,  fr. steen,  ‘stone’,  and  bok,  ‘buck’.  See  stone  and buck  and  cp.  steinbok.
steenkirk,  n.,  a  kind  of  lace  cravat.  —  Named from  the  battle  of  Steenkirk,  in  Belgium  (1692). steep,  adj.,  precipitous.  —  ME.  stepe,  ‘steep’,  fr. OE.  steap,  ‘lofty,  tali’;  in  gradational  relation¬ ship  to  stoop  and  stoup  (qq.v.)  Cp.  steep,  ‘to soak’,  steeple.
```


## [2026-09-14T02:31:51.940Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '10705,10720p' SOD_pages.txt; echo \"=== find pdf page tag near ===\"; awk 'NR<=10713 && /\\[pdf page/ {p=$0} END{}' SOD_pages.txt; grep -n \"\\[pdf page\" SOD_pages.txt | awk -F: '$1<10713' | tail -2",
 "description": "Inspect Sogdian entry 2395 'stwn"
}
```


### [2026-09-14T02:31:53.539Z] TOOL RESULT

```
     GMS 1272                                                             2409 (ys-   M -» »ys-
2393 'stptyyh M                                                           2410 {ys M -» >ys
     (a)stapde ©pp. =*}stf3tyy                                            2411 'yskty(h) M -* }yskth
     cruel
                                                                          2412 (ysw(() M =4 >ysw
       BBB; GMS 157
                                                                          2413 (yt- M                                             j*f
2394 (stryc M =» >stryc                                                        et ®pt. St.; perf. st. 'y/^V-   ^'yt-, *yt-, »s
2395 'stwn M
     stun                                                                      OcOtake
                                                                               GMS 129, 539; BBB; AVS 127
      column
      W-Lii
                                                                  OjZ**   2414 'ytS'r- '-» 'yd'r-
                                                                          2415 *yw M =» >yw, yw2
2396 <sxnd-     M                         >/•        j iO*J> «.
=== find pdf page tag near ===
```


## [2026-09-14T02:31:59.704Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"\\[pdf page\" SOD_pages.txt | head -3; echo ...; awk '/\\[pdf page/{tag=$0; line=NR} NR==10713{print \"entry2395 at line 10713; last tag: \"tag\" (line \"line\")\"}' SOD_pages.txt",
 "description": "Find pdf page tag for SOD entry 2395"
}
```


### [2026-09-14T02:32:00.837Z] TOOL RESULT

```
...
entry2395 at line 10713; last tag:  (line )
```


## [2026-09-14T02:32:04.280Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; head -5 SOD_pages.txt; echo \"---FF count:\"; tr -cd '\\f' < SOD_pages.txt | wc -c; echo \"--- leaf of entry 2395:\"; awk 'BEGIN{RS=\"\\f\"} /2395 .stwn/ {print \"leaf(1-based)=\"NR}' SOD_pages.txt",
 "description": "Determine SOD leaf for entry 2395"
}
```


### [2026-09-14T02:32:05.483Z] TOOL RESULT

```
 SOGDIAN
DICTIONARY
Sogdian - Persian - English


---FF count:
644
--- leaf of entry 2395:
leaf(1-based)=161
```


## [2026-09-14T02:32:13.023Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for L in 133 134 135; do echo \"=== leaf1b $L ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$L\"' {print substr($0,1,500)}' SOD_pages.txt; done",
 "description": "Inspect SOD leaves near printed p.67"
}
```


### [2026-09-14T02:32:14.077Z] TOOL RESULT

```
=== leaf1b 133 ===
 67
                                                                                                                                 'stryt
                                                                                GMS 781; Dhy. 209; TSP 7.9, 11; AVS 225
          132; C2, 77V 12
 1685 »stVk B, M                                   >>-                    1697 'starch B                                     ^«aU
      (o)stare (st'ryyt, »stry) ©<*staraka ©pi. jfV*/                          
=== leaf1b 134 ===
  »st\v
                                                                                                                                            68




                                                                                                                              ■)
 1710 >st\v S                                               ^J>^             1725 'sy-' B                                   u^«jju7jk*
      ast(u)?
                                                               
=== leaf1b 135 ===
                                                                                                                             'smVt-

 69

       world                                                              BSTBL, Dhy. 200
       TSP 8.189-, >sk}np\ TSP 2.1150; Wnpvv, VJ n p91,             1751 >skrwp B                   (J>jJlt.)j^\^iKjF^
                                                                             dry
         101 etc. >nkynpw, VJ 38b; GMS 366, *skamb-,
```


## [2026-09-14T02:32:19.408Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"st.wn\" SOD_pages.txt | head -20; echo \"=== full leaf 134 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==134 {print}' SOD_pages.txt",
 "description": "Search SOD for st'wn and print leaf 134"
}
```


### [2026-09-14T02:32:20.476Z] TOOL RESULT

```
7669:     apstawan       Opst'wn) =>pst}wn                                       Schwartz. HMV        p391, *ptrwxs-
7676:1349 'pst'wn => 'psVw'nh
8661:1689 >st*wn B                                                            1700 >stq)(n)
11903:2840 pstywnp- B                    jjulTc^^j UOjulT               GMS 178, 318; TSP 2.138; Frag. 2a.23; AVS 105
15086:          =*pstywnp-
21851:6309 nyst wn- =* nyst, wn-\ kwn-
=== full leaf 134 ===
  »st\v
                                                                                                                                            68




                                                                                                                              ■)
 1710 >st\v S                                               ^J>^             1725 'sy-' B                                   u^«jju7jk*
      ast(u)?
                                                                                   (o)say    ©intrans. v. =>z>ryy sy-, sy-1
           property ?
                                                                                   OcOseem
                                                                                   GMS 494, 550; VJ 368; BSTBL, Dhu. 183
           MD; Nov. 3V7

 1711 'stwp*        B =» ,st,wp>h                                            1726 *sy-: B                                     j.^ <i>b jU;
 1712 'stwr        S => >st>wrh                                                    (o)say ©trans, v. =*sy-j
 1713 'stwrpS^ B                        ^j^-^^o^                                   0<?)show
                                                                                   GMS 494, 550
      (o)storpaSe (,st,wrp5,y) -»stwrpSyy, WwrpS'k
      cattle                                                                 1727 >sy-3     B                          cpfjJ**y.j*->
           SCE; VJ; TSP; Gersh. Advice. 86n 27a
                                                                                   (to)lic down,
                                                                                   (o)say   (sy-2) (/^establish
 1714 'stwrsnyk          M                       -uij>-l(
      astrusnik                                                                  SCE 175, 3pl. pres. }sy*nt
           {related to)Ustrushna                                            1728 >sy>yn>k B                                        J*^^
                                                                                 showing
           MDii piOll 3, >strwsnk                                                (o)saycne =»zJry sy'n'k
 1715 'sty1                                                 c~Jio                 BSTBL, Padm. 13f
          ast(i) (sty1, »st\ 'ymn) ©3sg. prcs. of Sah-
                                                                            1729 'symy C            (<^1 : J^>)^\          ^ t^\ J± tJ J^
            =^}ys\ 'ym^ 'y1, x-\ »t, (ycy, ycy, xcy, 'stq'Cn),                   ascmc ©pi. -/ =»sym(h)
                                                                                 troubled, confused
          is 'st'ynt, »st'yt *ynt, >st)t
                                                                                  BSTii 850.2; C2, 12V2 n p56; pi. -r. C2, 31R17,
                                                                                    54R17
          GMS 760-86
                                                                            1730 >s *± »rt rwc
 1716 >sty2 B                                           iT-*">r.J
                                                                            1731 'sp'rmyk         B                                    .&
          aste ^'st2 being
          existence,                                                              osfarmik        (sP'rnVy)
          TSP 2.1016; >*/, TSP 7.120
                                                                                  TSP 7.167
                                                                                  pudenda
1717 *>styh -> *st3
1718 'styw =» }styyw                                                        1732 'sp'rs-     B                      vjJu^o cJb*s- i -j^i-b* ji
                                                                                  osfars ©pass. st. =»sfrs-
1719 >styy M =» >st2                                                              0<?)be ashamed
1720 >styyw B                                        1 <^>rj v <J^                TSP 2.654; GMS 441
     ostyu ? Ostyw) =*styw
                                                                            1733 'sbdy      C =» >sybty
     although, even if                                                                                                             jj' lirjJ ^
                                                                            1734 ScyWk        B
          BSTBL, Vim. 99; TSP 6.107; Hen. Texts. 722
                                                                                  asciyane
                                                                                  worthy          ©<*aJ;ian <*azjian <*arjyan <*rjyan;
1721 >swr C                                            JJjUj^Ip
     asur, ansur ©Av. asura                ©ob. pi. ~ty ^^^wr                       *sacydna(ka) -^'ysc'n'y
     tusk
          BSTii 849.4; C2, 12R4 n p55; Gersh. AHM            219                  VJ 1096; BSTBL, Dhy. 14; BBB p93, b42; GMS
                                                                                    155, 263 n 2; S W, Studia Orientalia.
1722 >swswyn't(t) S                                                                 (Helsinki) 1980,7
                                                       \ u£ j (j—j w* *-*
     (o)sosuyant ©pi.
     Soshiyan(j)                                                            1735 ^SPr     M =» sf'r
          Livsic\ AO Hung. 1972, 88, Bugut. Insc. B 1.4                     1736 »sf»rkrty => sp>rkrt>k
1723 ^xw'y- M                                                               1737 >sk>p> S                                          ^jjj\j^
                                               jjjjLj OJ^Jx*
     osxway ©<*us-xwdhaya-                  =*sxwst-, 'sywst-,                   oskafa ? ^sq'P-
       'syw'y-, sxw'y-                                                           gnashing
     GcOtake out                                                                 MHC      p26, 36.8 V5
     MSP el6
                                                                            1738 'sk'np B                                          JUijl^
1724 'sxw'y        S =» sxw>y-      •                                            askamb ^sk'np, mskmp
```


## [2026-09-14T02:32:25.055Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '8650,8680p' SOD_pages.txt",
 "description": "Print SOD entry 1689"
}
```


### [2026-09-14T02:32:25.270Z] TOOL RESULT

```
       SCE 245; Gersh. IF 1970, 305
1687 'st'ryt M                                                           1699 >stk- B, M, S                             ol>U
                                                         olfjU-               ostak ®<*astaka\ Khwar. >stk\ Yaghn. sitak\ MP
     ostaret (st'r'k, *stryt) ©ob. pi. >st*rytyy
     stars                                                                      astag ©ace. -w, abl. -Snon. gen. -y =»stq-,
     GMS 157, 937                                                                 st'yn'k
                                                                                bone
1688 >st)t                                                                      GMS 981, 1185; BBB 93 b37; VJ 806, TSP 2.117,
       astat ©ast+at ©3sg. subj. =»x}t, "t, 'sty1                                 361, 370, 3.273; SCE 83, 271; STSC; -Wi, VJ
       GMS 781, 856; AVS 225
                                                                                  781,779
1689 >st*wn B                                                            1700 >stq)(n)
     ostun ©<OP stand ©ob. -yh
     column, colonnade                                                         ast-kan    ©3sg. fut. ->>styl
     SCE 229                                               J_^-                GMS

1690 >st,wp,h    B
                                                         • iL <          1701 'stkpys'y B                  fUl <^l>^J y±* ^'y^1
                                           ^i^jl                              ostak-pise ?
       ostupa   CstwpO ©ace. -w; ob. -(>,y
       stupa                                                                   bony, limb
                                                                               Gersh. IF 1970, 303; BSTBL, Intox. 24; SCE 368
     TSP; BSTBL, Dhy. 68, >stwpw
1691 >st,wrh B, S                                                        1702 'stkyn'y B                                      J**^
                                                                              ostakene
     (o)stor Cstwr) ©ob. -y(hk pi. -t =»stwr
     cattle                                                                   (o/)bone, bony
      TSP 2.540 & etc.; TSP 3.251, 282, 291; VJ 87 &                          SCE 169; GMS 1053
        etc.-, MD                                                        1703 >stny B
                                                                  j>~-                                                  jt£>» ii\^XA fU-
1692 's^wrpa^y =» >stwrp6>y                                                    (o)stane ^'st'ny
```


## [2026-09-14T02:32:32.245Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for L in 504 505 506; do echo \"=== leaf1b $L ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$L\"' {print}' SOD_pages.txt | head -60; done",
 "description": "Print SOD leaves near printed p.439"
}
```


### [2026-09-14T02:32:33.357Z] TOOL RESULT

```
=== leaf1b 504 ===
                                                                                                                     436

     xwgptyk

           BSTii 891.62; STii 5.15; C2, 60V30 -y n pl32;        10734 xwn>k     S                                      jl
             GMS 1336 n 1; MSP bl41, 143
                                                                      xone ^Ywn*^1* xwny
                                                                      that
     10722 xwfiptyk    S =* xwdbtyq
                                                                      KG 591
     10723 xwdq*r     C =» xw5k>r
     10724 Xw8kV      M                                    [&   10735 xwnwx S -» xwnx
                                                                10736 xwnx M, C, S                                  y<jT
           xu5-kar, xwaSkar (xwdq>r, YwtS>r)
             ©<*xwata-kdra ^yw&Vi                                     xo-nax     ©demons, pron. nom. sg. m. =>Ywn>Y»
                                                                        hwnx
           alone
           GMS 269 n 1, 1108, 1124A 1336 n 1; STii 1.71;              that, that one, he
                                                                      GMS 1410; BBB f 50; Hen. Tales. 469.4; Lentz.
             STi 3722, 752ft Sund. AoFiii 1975, 18V6; C2
                                                                        STii 5.29 p584, xwnwx, MSP b58, 70, 190,
             gloss. p234; BSTii 839.3, 848.55
                                                                        Frag. Len. apud. SW, BSOAS 1981, 238
    10725 xwdw =* xwd*w
                                                                10737 xwny      M, C, S             {oy^^^ji)3\^
    10726 xwdy C                                       ^              xone (xwnyy) ©demons, adj. & pron. nom. sg.
          xu6e, xwaSe =»xwd, xwty
          self                                                          m.*, f. & ob. -A; pi. -t =*xwnx, xwn}k, Ywn'k1
                                                                      that, the, he
          STii 1.37; GMS 269
                                                                      GMS 1411-4; BBB e2, 9; STi 40.3, 42.1; STii
                                                                        p584; BSTi 118 etc.; BSTii: C2 gloss4 MSP
    10727 xwj- M                     CvJ'jjJ'^y*'
                                                                        b62
          xoz, xwaz ®*xwaz-aya- *»xwz-, ywz~»
                                                                10738 xwnyy M «* xwny
          (ro)ywi z-, 0<?)ask
               wysh                                             10739 xwp M, C                        4^«i
          GMS 232, 595, 914; BBB 737                                    n>xwp, Ywp
                                                                      xQp ©<Av. hvapak Skt. svapas «»mntxwpy,
    10728 xwj>mndty M                           tl^-^f^
          xozamande *=>xwz*mnty
                                                                      good, skilful
          wish, demand                                                GMS 223, 389; BBB a5
          GMS 1100                                              10740 xwptr C                                    >Vj
    10729 xwmY M, C                         jJLs ^jy*                 xuptar =»YwPtr
          xumar ©<Av. vohu-mqOra ^ywm'r                               better
          consolation, soothing                                       BSTii 854.1: C2, 7V24
          GMS 208, 346; C2, 31V2, 12: BSTii 893.12              10741 xwpy(y)    M, C
    10730 xwmV w'Py S, C      (IaJ5>;cf^w. jS)*xjuj£Lj                xup(e) ©in compd. =»xwp, mntxwpy
          xumar-wape ^xwm'r
          Consolei(Paraclete)
                                                                10742 xwr M, C, S *                              x^j^
          Sund. MHC     p25 n 26
                                                                      xur, xwar ©<huwar; xwar ©ob. -y
    10731 xwmny(h) rwc M        jjjj*Aj<jjjy4><*\*{j>jjj                  ood
                                                                        g=>xwrtxyz, xwrsn, yv/r, xwyr
          xumana ©<Av. vohu manah ^'ywm'n rwc                         sun
          second day of the month                                     GMS 223, 389; BSTii 827.48, 84322, 846.17,
          GMS 163, 208, 404; Hen. Fasts. 149.1                          875.3; C2 gloss. p234; KG 366, 560; xwry,
=== leaf1b 505 ===
 437                                                                                                        xwrsn qyrn


 10744 xwr'ty* ? M                           ^^0-,>             10756 xwrmzt py =» xwrmzt* pyy
       x/yuratya ^ywry'ty^h                                     10757 xwrmztyc M              >yj* (*• ^jf^)l^jM^
       pride, arrogance                                               xurmazdic (xrwmztO
       BBB p63, 521
                                                                      (related /o)Hormazd
 10745 xwr byw        C =» xwrPyyy                                    GMS 1278; Hen. Magi. 142.4
 10746 xwrpyyy        M                                         10758 xwrn- M, C                            oy>-
       xur-Payi ©ace. -w                                              xurn ©<Av. vohuni ©nom. ob. -y -»ywxn-,
       Sun-god
                                                                        yxwn-, ywrn-, yywn(w), wyrn-(h), yxwrn-
       BBB pl39, xwrbYw, ace. C2, 68V17, 69V13                        blood
10747 xwrc*q =* xwrcy*q                                               GMS 208, 492, 1168n 1; BBB 88.763; ace.
10748 xwrcy>q C                                  S\.                    xwrnw, GMS 350; STii 6.9; BSTi 318; Sund.
                                                                        AoFviii 1981, 23V10
      xurcyak ©f. n. ^ywrtcyk*
      food                                                     10759 xwrndy(y)     M                   6ju*L <^^„j i*jjjy~
       BSTii 836.3: C2, 108R3 n pl79.3                                xwarande, xurande     ~»ftr xwrndy(y)
                                                                      destructible
10749 xwrd'r-         C
                                                                      BBBbl5b95
      xur-5ar        ©trans, pret. =*xwr-
                                                      o>j^>-   10760 xwrnptxwrk       M                  ^To^-^liToy-
       0o)eat
       C2, 69R16; Sund. AoFviii 1981, 23V6                            xurn-patxure -»xwrn-
                                                                      blood-stained
10750 xwrjn(y)c M             (j^>- ^j^dS** f>> ^                    Sogdica. 21.19b, +6ndy, Gersh. Sogd. Cpds
      xur-zan(i)c =>ywryznych                                          143b, 148
       second month of the year
                                                               10761 xwrny psyncny C              j'y-u>- < jljoj*-
       Sogdica. 27.2a, xwrjncrrfx, Hen. Fasts. JRAS                  xurne-pasenc-nS ©voc. -n\ pres. part.
         1945, 149.3, 151.16; GMS 1275                                 «=»ywxn* }psyyk

10751 xwrm M, C                               js*j<«^V               bloodthirsty(M<?0jly/ierf doer)
      xurm ^xrwm, ywrm(h), ywrwm                                     STii 6.9; BSTi 318; GMS 893
       soil, earth
                                                               10762 xwrnyy ws- M                      (cr*j? uj*-)^b«*~
       GMS 415; BSTii 848.52: C2, 69V18                              xurn(e)-as
                                                                     bloodletting «»xwrn-
10752 xwrmny C                                        ^fiz-
                                                                     Sund. Man. Lett 305.21, 29
      xurm-ne ©adj. pi. -r
      earthy, (made of)dust                                    10763 xwr rwc      M         jjjOjj(^^)j^"^^A           jjj
       BSTii 884.16: C2, 48V19 n p95
                                                                     xwar- roc, xur-roc -»ywr rwc
10753 xwrmynqy' C                           ^TU-jf^U-                eleventh day of the month
      xurmenakya ©f. n.
                                                                     Hen. JRAS 1945; Fasts. 153.1 & etc. 153
      earthenGv/iar is of dust)
                                                               10764 xwrsn M, C               (o^J^)&^i^jy>-         ^j&>
       C2, 51V5
                                                                     xwar-san, xursan     ©ob. -y «»xwyrsny
10754 xwrmzt* Pyy M              jjLJtijU^y/                         sunrise, east
      xurmazda- payi (xwrmzt Py)
                                                                     W-Lii 546; BBB; GMS 1014; Gersh. Sogd. Cpds.
      (name of a)Manichean god, First Man                              143a, 146.6, STii 12; BSTii 895.55, 56, 896.58;
       W-Lii 500, 546, GMS 163, 284, 391, 499; BBB                     C2, 54V25, 26, 28; Sund. AI 28.186
         724; Hen. Fasts. 154.12; Sund. KG pl92
=== leaf1b 506 ===
                                                                                                                            438
     xwrt

             xursan-kiran                                           10778 xwsnd     M                                     ^>
             east                                                         xusand     (xwsnt, xws>nt) ©<OP uBadus-, MP
             STii 1.22; BBB pl39; Sund. AoFviii 1981, 28V
                                                                            hunsand ^yws'nt
               18-9, 21-2
                                                                          happy, joyful, content
     10767 xwrt M, C                             LU < jTl^                Hen. Tales. 469.31; BSOAS 11, 66.16; STii 5.25;
           xurt ©<Av. xvardti =»ywrt                                        BSTi 208; BSTii 893.13: C2, 31V13; KG 595;
           food                                                             MSP bl64
           GMS 947; BBB 591, 661; Hen. BSOAS 12,                   10779 xwsndy* M                            o?-^>
             307.53; BSTi 117, 123; KG 504; STi 24.6; C2,                xusandya (*xwsdy\ xwsnty*) ^yws^tyh,
             94V12; BSTii 827.42                                           ^ws'ndyy*

    10768 xwrt- M, C                                      &jj>-           joy, satisfaction
                                                                          BBB 523; GMS 425; STi 72.5, 73.9, 12, 18; Sund.
          xurt, xwart ©pt. st. =^xwr-, ywrt-
                                                                            AoFviii 1981, 219; C2, 12V30, 60V24, 40V11,
            (to)eat
            GMS 592, 832, 927; BBB pi 39; perf. xwrt&r-,                   22; Frag. Len. 77R3; BSTii 829.25, 890.56,
              BBB a7; GMS 897; xwrcPr, BSTi, 117; STi                      907.22,906.11
              34.4; C2, 69R16                                      10780 xwsnt     C =» xwsnd
    10769 xwrtkVy       M                              (J)^>       10781 xwsnty* C =» xwsndy>
          xurtkare      ©inf.                                      10782 xwst- M, C                                  j=-Xi^j
          eating
                                                                         xwast, xust ©pt. St.; pres. *xwyy-y trans, pret.
            GMS 934                                                        xwsd}r-        ^yw^-, x}w-
    10770 xwrtx*yzcyk S                            ^J-^J^                0o)beat
          xwartoxizclk ©pi. -t -^xwrtxyz                                 GMS 566, 573; xwsd'r-, STii 4.34
          western                                                  10783 xwsty     M            (<z^l<<z^/.^jls)c>j<<^&
                                                                         xwaste, xuste ©Pahljcwastan
            KG 348, 349, 325, 326 pl92
                                                                         broken, beaten
    10771 xwrtxyz       M, C              ^>ju> ijj^jy^ VJ/              BBB 505
            xwartoxiz ^xwrtx'yzcyk                                 10784 xws-      M, C
            sunset, west                                                                                ©inf. -y-, pt. St. xwPt
                                                                         xwas (xwsy) ©<*waxs-
            BBB; GMS 662, 1614; Gersh. Sogd. Cpds. 1945,
                                                                           ^yws'y-, xws'ty
              143a; W-Lii 546, 3; KG 387; ob. -y, BSTii                  (ro)increase, (?<?)grow up
              895.56: C2, 54V26                                          GMS 428, 910; C2 gloss.
    10772 xwrtxyz kyr'n =» xwrtxyz                                 10785 xws'mnty C                            j
                                                                                                                  <^>(
    10773 xwrynyy        M                cjjj^- <0->j>^- J^- >>         xwas-amande ©ace. -tw ^wxs'mnty
          xwarene
          ea ting       ^ywr'ynUc                                        growth, salvation
                                                                         C2, 31V23 n p77: BSTii 893.23, Benv. JA 1959,
            BBB f77; GMS 890                                               131
    10774 xws*nt     S =» xwsnd                                    10786 xwasate
                                                                         xws'ty C©pp.                           4^Lx^ji^jzS
    10775 xws'nty'kh     S                             c*^>
                                                                         spread, grown up, full grown
            xusandyak    ^yws'nty'kh
            joy                                                          BSTii 895.27: C2, 54R27, 87V 16
            KG 602                                                 10787 xwsd'nc C                      ? (>_.> i ^j^SihJ^
                                                                         xwasSanc
    10776 xwsd'r- C ^ xwst-                                              six sixths ?
    10777 xwsm C                                                         Weber. 1970, 196 apud. Yoshida. SI 1984 pl46
```


## [2026-09-14T02:32:40.780Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^ *439 \\| 439 [^0-9]\" SOD_pages.txt | head -5; echo \"===\"; awk 'BEGIN{RS=\"\\f\"} NR==507 {print substr($0,1,200)}' SOD_pages.txt",
 "description": "Check SOD entry 439 and leaf 507"
}
```


### [2026-09-14T02:32:42.499Z] TOOL RESULT

```
===
439                                                                                                                    xwsywnc

      BSTi A23
```


## [2026-09-14T02:32:50.891Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"prystk\\|pryst\\b\\|fresta\\|frest\" SOD_pages.txt | head -10; echo \"=== ostad/ ʾwstʾt ===\"; grep -n \"wst'8\\|wst't\\|ustad\\|ostad\" SOD_pages.txt | head -10",
 "description": "Search SOD for messenger/master words"
}
```


### [2026-09-14T02:32:50.965Z] TOOL RESULT

```
11547:2709 pr>wcy B                               j^y\j                 freste (frystk, P^ysty, Prysty/k)
11556:       Pruk (pr>wkh) ©Yaghn. viruk, Khot. brauka%                 frestar ©<Av. fraesta-tara
15001:       frest ©<fra-ista    ©pt. St. ^P^yst-, pryst-1,                  fri/ytat (fryt*t) ©ob. -y =»pryt}t(t)
15017:     freste ©pi. -r; ob. pi. -ty% ace. -tw; abl. -f>; f.               BSTBL, Dhy. 63; TSP n pl71
23777:                      ^pr^t-, pryz-, pryst-2                           TSP 7.139; Sr(ms ? Hen. Texts. 716; Swaig ?
23784:       frasay    ©<*fraisaya- «*pr*s-, pryst-1, pr*ys-lf              (ro)water, (fo)flow
23862:     parimand     (pr*ymnt) «>prym*nt                                      frest ©<*fraista ©pt. St.; perf. pr*yStwd*r
23863:     for this, for these, in this, in these, about this,                     =»pryst-\ fryst-, prys-, P^sCy)-
23869:     parime5/9 =»prymy8, pr'ym                                             frestak(u), freste
24429:                                                                       parast Cprst-) ©pt. st. -^prstk, pryz-, pryst-2
=== ostad/ ʾwstʾt ===
9419:                                                                  ost ©impf. w*st ^wst't-, 'wst'y-
9445:  'wst't
9481:1976 J\vstt(y)     B =» >wst>yt, 'wst't-                                      TSP 5.10, 98; GMS 56; BBB; MSP c4; TSP 25.1
14066: 3613 Srwst't   S                                  j~.jx; *^yu.
```


## [2026-09-14T02:33:26.033Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n 1,40p tools/fetch_source.py; echo \"=== verify_check ===\"; sed -n 1,50p tools/verify_check.py",
 "description": "Inspect fetch_source and verify_check tools"
}
```


### [2026-09-14T02:33:26.099Z] TOOL RESULT

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
=== verify_check ===
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
```


## [2026-09-14T02:33:33.452Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/steh%E2%82%82-\" \\\n\"https://en.wiktionary.org/wiki/%D8%B3%D8%AA%D9%88%D9%86\" \\\n\"https://en.wiktionary.org/wiki/%D8%A7%DB%8C%D8%B3%D8%AA%D8%A7%D8%AF%D9%86\" \\\n\"https://en.wiktionary.org/wiki/%D8%A2%D8%B4%D8%AA%DB%8C\" \\\n\"https://en.wiktionary.org/wiki/%D9%BE%D8%B4%D8%AA\" \\\n\"https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%B4%D8%AA%D9%87\" \\\n; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 474, root Stâ/Stha/Stâk, node verification\" 2>&1 | tail -2; done",
 "description": "Archive Wiktionary pages batch 1"
}
```


### [2026-09-14T02:33:43.711Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/steh%E2%82%82-
/home/sfmqrb/git/rishe/data/verification/sources/web/9dd2e100b6c8ace7.txt
### https://en.wiktionary.org/wiki/%D8%B3%D8%AA%D9%88%D9%86
/home/sfmqrb/git/rishe/data/verification/sources/web/b21d3dcfd35472dc.txt
### https://en.wiktionary.org/wiki/%D8%A7%DB%8C%D8%B3%D8%AA%D8%A7%D8%AF%D9%86
/home/sfmqrb/git/rishe/data/verification/sources/web/7f63e697c3c55410.txt
### https://en.wiktionary.org/wiki/%D8%A2%D8%B4%D8%AA%DB%8C
/home/sfmqrb/git/rishe/data/verification/sources/web/8ffa24f4b7aa7604.txt
### https://en.wiktionary.org/wiki/%D9%BE%D8%B4%D8%AA
/home/sfmqrb/git/rishe/data/verification/sources/web/d881b3b7e4d72c49.txt
### https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%B4%D8%AA%D9%87
/home/sfmqrb/git/rishe/data/verification/sources/web/216cb77378f93223.txt
```


## [2026-09-14T02:33:46.914Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in 9dd2e100b6c8ace7 b21d3dcfd35472dc 7f63e697c3c55410 8ffa24f4b7aa7604 d881b3b7e4d72c49 216cb77378f93223; do echo \"######## $f\"; grep -n -A14 -i \"Etymology\" $f.txt | head -60; done",
 "description": "Read etymology sections of fetched Wiktionary pages"
}
```


### [2026-09-14T02:33:47.983Z] TOOL RESULT

```
######## 9dd2e100b6c8ace7
######## b21d3dcfd35472dc
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Numeral 
69-
70- 1.3.1 
71- Declension 
72-
73- 1.3.2 
74- Derived terms 
75-
76- 1.3.3 
--
88: Etymology 
89-
90- 2.2 
91- Pronunciation 
92-
93- 2.3 
94- Noun 
95-
96- 2.3.1 
97- Derived terms 
98-
99- 2.3.2 
100- Descendants 
101-
102- 2.4 
--
114: Etymology 
115-
116- 3.3 
117- Pronunciation 
118-
119- 3.4 
120- Noun 
121-
122- 3.4.1 
123- Descendants 
124-
125- 3.5 
126- References 
127-
128- 4 
--
134: Etymology 
135-
136- 4.2 
137- Pronunciation 
138-
139- 4.3 
140- Noun 
141-
142- 4.4 
143- References 
144-
145- Toggle the table of contents 
######## 7f63e697c3c55410
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Verb 
72-
73- 1.4.1 
74- Usage notes 
75-
76- 1.4.2 
77- Conjugation 
78-
79- 1.5 
--
158: Etymology
159- [ edit ] 
160-
161- Inherited from Middle Persian [script needed] ( YKOYMWNtn' /⁠ē̆stādan⁠/ ) , [ 1 ] from Old Persian , from Proto-Iranian *staH- ( “ to place, stand ” ) , from Proto-Indo-Iranian *staH- , from Proto-Indo-European *steh₂- ( “ to stand ” ) . [ 2 ] 
162-
163- Pronunciation
164- [ edit ] 
165-
166- ( Classical Persian ) IPA ( key ) : /ʔeːs.taː.ˈdan/ , /ʔiːs.taː.ˈdan/ 
167-
168- ( Dari, formal ) IPA ( key ) : [ʔeːs.t̪ʰɑː.d̪án] , [ʔiːs.t̪ʰɑː.d̪än] 
169-
170- ( Dari, formal ) IPA ( key ) : [ʔeːs.t̪ʰɑː.d̪án] , [ʔiːs.t̪ʰɑː.d̪än] 
171- ( Kabuli ) IPA ( key ) : [ʔɪs.t̪ʰɑː.d̪án] 
172-
######## 8ffa24f4b7aa7604
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Derived terms 
72-
73- 1.4 
74- Further reading 
75-
76- Toggle the table of contents 
--
153: Etymology
154- [ edit ] 
155-
156- From Middle Persian [Book Pahlavi needed] ( ʾštyh /⁠āštīh⁠/ ) . Akin to Old Armenian հաշտ ( hašt ) , an Iranian borrowing. See them for more.
157-
158- Pronunciation
159- [ edit ] 
160-
161- ( Classical Persian ) IPA ( key ) : /ʔaːʃ.ˈtiː/ 
162-
163- ( Dari, formal ) IPA ( key ) : [ʔɑːʃ.t̪ʰíː] 
164-
165- ( Dari, formal ) IPA ( key ) : [ʔɑːʃ.t̪ʰíː] 
166- ( Kabuli ) IPA ( key ) : [ʔɑːʃ.t̪ʰíː] 
167-
######## d881b3b7e4d72c49
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 1.2.1 
68- Derived terms 
69-
70- 1.2.2 
71- Descendants 
72-
73- 1.3 
74- Further reading 
75-
76- 2 
--
85: Etymology 1 
86-
87- 2.2.1 
88- Pronunciation 
89-
90- 2.2.2 
91- Noun 
92-
93- 2.2.2.1 
94- Derived terms 
95-
96- 2.2.2.2 
97- Descendants 
98-
99- 2.2.3 
--
103: Etymology 2 
104-
105- 2.3.1 
106- Pronunciation 
107-
108- 2.3.2 
109- Interjection 
110-
111- 2.4 
112- References 
113-
114- 3 
115- Urdu 
116-
117- Toggle Urdu subsection 
--
120: Etymology 
121-
122- 3.2 
123- Pronunciation 
124-
125- 3.3 
126- Noun 
127-
128- 3.4 
129- Further reading 
130-
131- Toggle the table of contents 
######## 216cb77378f93223
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
72-
73- 1.4.1 
74- Derived terms 
75-
76- 1.4.2 
77- Descendants 
78-
79- 1.5 
--
176: Etymology
177- [ edit ] 
178-
179- From Middle Persian plystk' ( frēstag , “ apostle; angel ” ) [Inscriptional Pahlavi needed] ( plystky , “ messenger ” ) . Compare Manichaean Middle Persian frystg , prystg ( frēstag ) , hrystg ( hrēstag , “ apostle; angle ” ) , Manichaean Parthian fryštg ( frēštag , “ apostle; angel ” ) , Avestan 𐬟𐬭𐬀𐬉𐬱𐬙𐬀- ( fraēšta- , “ messenger ” ) , Sanskrit प्रेष्यता ( preṣyatā ) ; Middle Iranian borrowings Old Armenian հրեշտակ ( hreštak ) , Jewish Babylonian Aramaic פרסתקא ( prestəqāʾ , “ royal guard, messenger ” ) , and Classical Syriac ܦܪܣܬܩܐ ( prestəqāʾ , “ royal guard, messenger ” ) .
180-
181- Pronunciation
182- [ edit ] 
183-
184- ( Classical Persian ) IPA ( key ) : /fa.riʃ.ˈta/ , /fi.riʃ.ˈta/ 
185-
186- ( Dari, formal ) IPA ( key ) : [fä.ɾɪʃ.t̪ʰá] , [fɪ.ɾɪʃ.t̪ʰá] 
187-
188- ( Dari, formal ) IPA ( key ) : [fä.ɾɪʃ.t̪ʰá] , [fɪ.ɾɪʃ.t̪ʰá] 
189- ( Kabuli ) IPA ( key ) : [fä.ɾɪʃ.t̪ʰá] , [fɪ.ɾɪʃ.t̪ʰá] 
190-
```


## [2026-09-14T02:34:05.337Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for w in \"frēst\" \"frēstag\" \"ōstād\" \"ōstāy\" \"stūn\" \"āštīh\" \"pušt\" \"paristīdan\" \"staxr\" \"stahm\" \"ēstādan\" \"abestāg\" \"stabr\"; do echo \"### $w\"; grep -n \"^$w\\|^$w \" PHD.txt | head -5; done",
 "description": "Grep MacKenzie Pahlavi dictionary"
}
```


### [2026-09-14T02:34:06.548Z] TOOL RESULT

```
### frēst
### frēstag
### ōstād
### ōstāy
### stūn
### āštīh
### pušt
552:puštag 70 ranjfénidan
553:puštaģ [pwstk'] load (carried on the back). puštībān [pwštykp”n! | N ~] supporter, bodyguard. ~ЛЬ : support, protection.
### paristīdan
### staxr
### stahm
### ēstādan
### abestāg
### stabr
```


## [2026-09-14T02:34:10.318Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for w in frést frest \"ōstā\" \"óstá\" \"estád\" \"éstád\" \"stūn\" \"stun \" \"áštih\" \"ashtih\" \"paristi\" \"staxr\" \"stahm\" \"stambag\"; do echo \"### $w\"; grep -n -i \"$w\" PHD.txt | head -4; done",
 "description": "Loose grep of PHD for relevant Pahlavi words"
}
```


### [2026-09-14T02:34:11.517Z] TOOL RESULT

```
### frést
366:fréstádan / frestidan, frést- [SDRWN-(y)tn' < A w šdr; plyst2tn!, -ytn! | M pryst-d, N firistádan] send.
367:fréstag [plystk! | M prystg, (N firista)] apostle, angel.
789:angel fréstag; guardian ~ frawahr, fraward.
811:apostle fréstag, paygambar; v. pro- phet. .
### frest
366:fréstádan / frestidan, frést- [SDRWN-(y)tn' < A w šdr; plyst2tn!, -ytn! | M pryst-d, N firistádan] send.
4682:frasang parragig pargan- parwar pargandan pargüd frég, parig frest- fréstadan fréstidan pargast fréstag fréb
### ōstā
### óstá
559:rēšaģ [/yšk! | N rēša] root, fibre. rēšīdan, rēš- [lysyin' | N ~] wound, hurt. rëškën [/yškn'] hurtful, harmful. ~th: harmfulness. réxtan, réz- [lyhtn', lyc- | P ryxt, M ryz-, N ~] flow, pour. --išn: flow. ridan, riy- [/ytn', Id- | N ~] defecate, void. rist [lyst' | M ryst] dead. Iristag [lystk'] corpse. 'ristag [/ystk!] way, manner; sect. rist-āxēz [/yst?hyc | M ryst?hyz, N ~] resurrection of the dead, rištaģ [/(y)stk! | N ~a] rope, string, thread. riy-, v. ridan. riyahrih [/d?hlyh] scorn, mockery. rdb [/wp] robbery. rób- [/wp- | N ruftan, ~} rub, sweep. rūbāh [TALE < A tP; lwph | N ~] fox. Irēd [Iowt! | M rwd, N ~] river. *rdd [lwt' | N ~] stringed instrument. réd-bar [lwtb’] | N ~] river bank. rddig [/zvtyk! | (N róda)] intestine, gut; ~4n, (p/.) entrails, guts. тбүп [M(H)SY A < A ті; lwkn! | Р тшеп, (M rwyyn), N rauyan] oil, butter. ~-xwardig [-hwltyk'] sweetmeats. ron [lwn' | M rwn] direction. б... ~: towards. róspig [lwspyk! | N ~i] whore. ~th: whoredom. róstág [lw(t)st?k! | (P rwdyst?g), N rūstā] river-bed; district, province. rošn [lwfn! | M rwšn, N rūšan] light; bright, light. ~ih: light. röšnjag [lwsnk'] clear, obvious. ~gar [-Al | (P gr, M -ygr), N -gar] illuminator. irēy [ltd | M rwy, N ~] face. *rdy [lwd | M rwy, N ~] copper, brass. гбу-, -išn, v. rustan. гӧуап [/wdyn! | N ~] madder. róyen [/wdyn! | M r'wyn, N róyin] (made of) copper, brazen. roz [YWM < А ушт; Гос | M rwc[z, N ~) day. rózag [lwck! | M rweg, N roza] fast, fasting. rozāģ [wc k'] lightning. rózan [/wcn! | N ~] window. roz(b)ānaģ [lwe(p)’nk'] window. rózénidan, rózén- [Iwcyn-ytn! | M rweyn-] lighten, brighten. rozģār [/wck”l | N ~] daytime. r6zig [/wcyk! | N rózi] daily bread, sustenance.
### estád
### éstád
323:2ēraxtan, ёгапј- Pylhtn', *ylnc- | M ‘yrxt, ( yrnz-)] fight, dispute. éraxtür [y/At? 1] warrior. ēr-kaš ['dik£ | M *yrkš] (hands under the armpits in respectful) salutation, greeting. 1ërmán [?y/mx! | (MÉÁry! mwn), N ~] friend; а god. — ih: friendship. 23ër-man(ag) ['dim?n(k)'] humble. ēr-menišnīh [dimyninyh] humility. ér-tan ['ditn!'] humble. ~ih: humility. ērwār [D yleo?1] befitting a hero. ērwāraģ [*dlw?Ik! | J ?rw’rh] jaw, cheek. ésm ['ysm] = ézm. esp", v. sp”. éstádan, ést- [YKOYMWN-tn! < A ygym, У gum; ?sttn!, *zost- tn! | M ‘yst-’dn, N ~] stand; be, continue (as auxiliary of the perfect con- tinuous tense). ~išn: permanence, lasting, dwelling. ēš Pys | N xéf] plough. efm, v. $n. &(w) [z; HD < A hd | M ‘yw, N -ēļ a, one. éwan [*dwn') stalk, trunk. ēwān ['dw?n!] bridle. éwar ру! | J ?yf?r] certain(ly), assured(ly). éwarz [dwlc] movement. éwarzidan, éwarz- ['dwlc-ytn!] move, travel. éwarzig ['dwlcyk!] moving. 1&wáüz [?уш?с] word, utterance. tēwāz [?уш?с] sole, only. ~ig [-yk'] particular, individual. čw-bār Duech?) once. ē(w)-čand D у(то)спа] some, a few. éwén Pdwyn' | M *ywyn, (N àyin)] manner, custom, form, propriety. pad —: properly. léwénag ['dwynk! | M *ywyng] = ëwën ; v. ёё-. Ў *éwénag [?*dwynk! | (N āyīna)] mirror. Set (ъд) yn k éw-kard(ag) ['ywkrt(k)', -kltk'] united, joined. ē(w)-mēg D»(zo)mtok!] wearing (only) one shoe. éw-sün Pywsn' | (N yak-sān)] uniform, (a)like. ^ Ah : uniformity, likeness. éw-tüg Pywt?k' | М ‘yw 12, (N yaktà)] alone, single, individual. éz-, v. yaz-. —išn [уст] worship. ézm [CY BA < A syb | N hëzum] firewood, fuel. ged Zm4
366:fréstádan / frestidan, frést- [SDRWN-(y)tn' < A w šdr; plyst2tn!, -ytn! | M pryst-d, N firistádan] send.
691:abandon abāz éstádan az, hištan.
1573:desist from abaz éstádan az.
### stūn
4762:petig, sti stendag sidig, stéy sidigar stér stézag stowih stūwēn- stowēnīdan stē Sadwēs dīdan -istan stūn stūnag stor, stür sturg stūrīh stórgáh storban stard *stūš stūdan star
### stun 
### áštih
### ashtih
### paristi
542:~ AZ: free (oneself) from. pargandan, pargan- [plkn-, plgn-dn! | (P pr'gnd, N parāgandan)] scatter, distribute, disperse. pargast [plgst' | N ~] let it not happen! Heaven forbid! pargüd [plgwt' | P prgwdg], ~ az: free, exempt from. parig [plyk' | M pryg, N pari] witch. paristag [pistk! | N pirista] servant. ~th: service; worship. paristar [plsť] | N parastár] maidservant. paristidan, parist- [plst-ytn' | M pryst-, N parastidan] serve, worship. ~išn: service, worship. paristog/k [plstwk' | P prstwg, N piristū(k)] swallow. рагпабап [pinyE?n! | M prng?n, N parniyān] polychrome damask. parr [pl | M pr, N ~] feather, wing. parrag [plk', pig | P prg, N ~a] wing. ~ig [-vk'] winged. parréxtan, parréz- [plyhin', plyc-] remain over, be superfluous. parrón [plwn' | M prwn] hence, away. parrwar [plwl | M prwr] winged. parsig [p’lsyk' | N pārsī] Persian. pars [5/f] spotted, speckled. parwāl [plwl | (P prwrz)] refreshment, nourishment. parwal- [plw���l- | (P prwrz'dn)) foster, nourish, -išn: nourishment. parwanag [phonk! | M prw’ng, N ~a] guide, leader. ^h : guidance, leadership. parwand [plwnd | N —] enclosure, comprehension. parwand-, v. parwastan. P parwānģāh [*plw?ng’s] throne. parwār [plyw?l | N ~] citadel; circumvallation; suburb, surroundings. parwardan, parwar- [plwl-tn' | M prwrdn, N ~) foster, nourish, cherish, educate. ~išn: nourishment, fostering, education. parwast [plwst'] enclosure. parwastan, parwand- [plwstn', plwnd-] surround, enclose, contain, comprise. parwāz [plw’c | N ~] flight. parzin [picyn' | M prcyn, J przyn, (N parčīn)] fence, hedge. pas [AHL < A?hr; BATL < Ab2tr; ps| = M, N ~] then, afterwards, behind. ~ az: after. ~ih: rear. pas [p’s | = M, N ~] guard, watch. ~ dāštan: keep watch, guard. pāsbān [p’sp’n' | M p’sb’n, N ~] guardian, watcher. ~ih: defence, protection.
601:*urwüzistan, urwāz- [”wlw?*c- = Av. urwaza-] rejoice. ~i8n: rejoicing, happiness. uskārdan, uskār- [wsk?l-tn' | J ~, (N sigāl-)] think, consider, discuss. -išn(ih): consideration, reflection. uspurrig (^wspwlyk!] = spurrig. us(t)dfrit Pzs(t)wplyt! = Av. usafriti-] offering. ušahin Pwšhyn! = Av. ufahina-] the night gah. ušnūg Pušnwk!'] = šnūģ. uštán ['wit?n! = Av. uštāna-] soul, ghost. ~th : vitality. ~отапа [-'wmnd] living, animate. uštar [GMRA < А gmD ;^wstl | N uštur] camel. 7—-$üw-palang Puštlg”plng | № ~) giraffe. uzdehig [we-, ^wzdhyk! | M ?wzdh] exiled; foreign. ~ih: exile. uzdés ["wc-,?wzdys | М ’wadys] idol. ~-parist [-plst' | M -pryst] idolater. ~-paristignih : idolatry. ~zar [-c1 | M -c’r] idol-temple. uzénag ['wcynk! | N hazina] expense, cost; exit. uzérin ['wz())ylyn! = Av. uzayeirina-] the evening gah. uzidan [wcytn! | M ?wzyd, *zozyh-] go out. uzmüdan, uzmāy- ['sozmwtn! , ”wzm'd-) prove, test, try. ~išn: testing. uzumburd ['wzmbwit! | N zumurrud] emerald. w uzwün [SNA < A If? ;^wzwn! | M ‘zw’n, (N zabdn)] tongue, language Ba ch uzwürdan, uzwār- Pwzw’l-tn! | M *zw'rdn] know, understand. ~išn: understanding; ‘huzwarish’.
2356:idolatry déw-ésnih / -ézagih, uzdés- paristišnīh.
3593:service paristagīh, paristišn, spās,
### staxr
### stahm
570:Srēš [slw$ | M sros, N surūš] the god Obedience; cal. 17th day. ~ig [-yk'] obedient. srū [slwb' | N suri(n)] horn, nail, prong. srub [s/(w)p | N usrub] lead. ~ën [-yn'] leaden. srüdan, sray- [s/wtn', sPd- | M sry-, № sur~] sing, recite, play (an in- strument). ~i$n(ih): singing, recitation. srüwar [siwbw!] horned. srūwēn [slwbyn'] horny. stabr [stpl | M stbr, N sitabr] big, coarse, strong. 7-ih : coarseness; strength, force. stabrag [stpik! | Ar. istabrag] shot silk. stadan, stán- [YNSBWN-tn' < A ynsbwn, V nsb | M ‘std, *stn-, N sit~] take. staft [stpt! | M ‘stpt] hard, firm; harsh, tyrannous; very. stahm [sthm | N sitam] power, oppression. ~ag [-k'] strong, oppressive. ~(ag)ih: oppression. stambag [sthmbk! (-h- < stahm) | M ‘stmbg, N sitamba] oppressive; obstinate. “АҺ: oppression; obstinacy. stān-, v. stadan. star [sil] = stāraģ. stárag [st?/k! | M ‘st?rg, N sitara] star. stard [st!/t!] stunned, stupefied, confounded. ~ih: stupidity, stupefaction. : star-Ošmār, -6šmur [stProfm?l, 2wfmwl] astrologer. starwan [stlwn' | N sit~] barren, childless. stáyIdan (s? dytn! | M гуд, N sit~] = stüdan. Stéy [styk! | N. sitéy] erect. sténdag [styndk!] standing, erect. stér [styl | N sitēr] stater. Stézag [styck! | M ‘styz-, N sitéza] quarrel, strife. sti [sty(y) = Av. sti-] being, existence. Std [stwh! | (P *stwb, N sutdh)] distressed, defeated. ~wih : distress. stör [stwl | P ‘stwr, N sutór] horse, mount; large cattle. «bān [-p’n' | N -bàn] (head) groom. --ģāh [-g’s] stable. *stēš [stw$] the fourth morning after death. stówénidan, stówén- [stwhyn-yin'] defeat, overcome, Stówih, v. sto. stüdan, stāy- [stwtn', st?d- | M ‘stwd, ‘st?y-~~, N sit—] praise. ~išn: praise. ~išnīg : praiseworthy.
2991:oppression awištāb, handraxtagih, pazd, stahm, stahm(ag)ih, stam- bagih.
2992:oppressive stahmag, stambag.
3194:power abzār, amāwandīh, nērēg, 07, stahm, tuwān, zor.
### stambag
570:Srēš [slw$ | M sros, N surūš] the god Obedience; cal. 17th day. ~ig [-yk'] obedient. srū [slwb' | N suri(n)] horn, nail, prong. srub [s/(w)p | N usrub] lead. ~ën [-yn'] leaden. srüdan, sray- [s/wtn', sPd- | M sry-, № sur~] sing, recite, play (an in- strument). ~i$n(ih): singing, recitation. srüwar [siwbw!] horned. srūwēn [slwbyn'] horny. stabr [stpl | M stbr, N sitabr] big, coarse, strong. 7-ih : coarseness; strength, force. stabrag [stpik! | Ar. istabrag] shot silk. stadan, stán- [YNSBWN-tn' < A ynsbwn, V nsb | M ‘std, *stn-, N sit~] take. staft [stpt! | M ‘stpt] hard, firm; harsh, tyrannous; very. stahm [sthm | N sitam] power, oppression. ~ag [-k'] strong, oppressive. ~(ag)ih: oppression. stambag [sthmbk! (-h- < stahm) | M ‘stmbg, N sitamba] oppressive; obstinate. “АҺ: oppression; obstinacy. stān-, v. stadan. star [sil] = stāraģ. stárag [st?/k! | M ‘st?rg, N sitara] star. stard [st!/t!] stunned, stupefied, confounded. ~ih: stupidity, stupefaction. : star-Ošmār, -6šmur [stProfm?l, 2wfmwl] astrologer. starwan [stlwn' | N sit~] barren, childless. stáyIdan (s? dytn! | M гуд, N sit~] = stüdan. Stéy [styk! | N. sitéy] erect. sténdag [styndk!] standing, erect. stér [styl | N sitēr] stater. Stézag [styck! | M ‘styz-, N sitéza] quarrel, strife. sti [sty(y) = Av. sti-] being, existence. Std [stwh! | (P *stwb, N sutdh)] distressed, defeated. ~wih : distress. stör [stwl | P ‘stwr, N sutór] horse, mount; large cattle. «bān [-p’n' | N -bàn] (head) groom. --ģāh [-g’s] stable. *stēš [stw$] the fourth morning after death. stówénidan, stówén- [stwhyn-yin'] defeat, overcome, Stówih, v. sto. stüdan, stāy- [stwtn', st?d- | M ‘stwd, ‘st?y-~~, N sit—] praise. ~išn: praise. ~išnīg : praiseworthy.
2959:obstinacy stambagih, wastürih.
2960:obstinate stambag, wastār.
2992:oppressive stahmag, stambag.
```


## [2026-09-14T02:34:24.434Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"sturg\\|stün\\|stûn\\|stun\\[\\|N sutūn\\|sutün\" PHD.txt | head -5; echo \"=== ō-words ===\"; grep -n -i \"ōstāy\\|óstáy\\|ostáy\\|ōst\\|awestwār\\|ōstīgān\\|ōstwār\" PHD.txt | head -5; echo \"=== āštīh ===\"; grep -n -i \"áštih\\|āštīh\\|aštih\\|ashti\" PHD.txt | head -5",
 "description": "Grep PHD for sturg, stūn, ōstā-, āštīh"
}
```


### [2026-09-14T02:34:24.525Z] TOOL RESULT

```
75:(1) abstract nouns ending in -ih [-y%], which immediately follow the words from which they are derived, e.g. stūrīh after stir, before sturg;
571:stün(ag) 78 šah-
572:stün(ag) [stwn(k)!' | M 'stwn, N sutūn] column, pillar, mast. stir [sżwl] trustee, curator, guardian. ~ЛЬ : trusteeship. sturģ [stwlg | N suturg] fierce, contentious; gross, coarse. süd [swt! | M send, N ~] use, profit, advantage. sudab [st?*5 | N ~] rue. sūd-abģār [swt?fk'/] profitable. sūdaģ [swtk!] negligent, indolent. ~ih: negligence, indolence. sidan, sāy- [swtn', s'd- | N ~] rub. sūd(ö)mand [swt(?w)mnd | N sūdmand] useful. suft [swpt' | N ~] shoulder. suftan, sumb- [swptn!, swmb- | N ~] pierce, bore. sumb [swmb* | N ~] hoof. isūr [sw] | M swr, N ~] meal, feast, banquet. *sür [sel] strong. sūrāg [swl(?)k'] hole, burrow. ~ig [-yk'] burrowing (animal). ««Omand (-'wmnd] holed. sūrāx [swPh | N ~] hole. sust [swst! | = M, N —] slack, lazy. ~ih: slackness, laziness. Iguš [swš | (N šus)] lung. *suš [stw$] degree (of arc). suxr [swhl | N surx] red. suy [swd | M swy-] hunger. *swahistan, swah- [swh-stn' | P swh-] sigh. sya [syd? | (P syw, N styah)] black. ~hag [-hk' | N -a] pupil (of eye).
651:wénig [wynyk! | M wynyg, N bini] nose. wénO£ [wynwk' | N bunü] lentil. wēš [zoy£ | = M, N béf] more. wé&ag [wysR! | N beta] thicket, wood. --estün [-st?n'] woodland. ~ig [-yk'] silvan. wēwag [wdpk! | N béwa] widow. 1wéxtan, wez- [NSSHWN-tn! < А V nsh; wyhtn', wyc- | P wyxt-, N bextan, béz-] sift, select, choose, separate, cleanse, purify, winnow. ~išn: selection. *wēxtan, wēz- [wyhtn!, wyc-] swing, brandish, throw, pour out. Wīdadafš [wydtpš = Av. wīdašafšū-| the south-western continent of the earth. widang [wtng | P wdng] trouble, distress, constraint. widār [xt' | N gudár] passage, entrance. widarag [wtlg | M wdr, N guàar] path, passage. widardan, wider- [wtitn!, wt(y)l- | M wd(y)r-, N guóar-] pass (by, away), cross, die. : ~išn(īh): passage, crossing, death. ~i$nig : transient. widārdan, widār- [xwt?/-tn! | M wyd’r-, N guóárdan] let pass, transport; endure, suffer. widārīdan [w?lytn'] = widardan. widaštan [wtstn' | N gušaštan] = widardan. widāxtan, widāz- [wt’hin', wtc- | (P wd’c-), N gudaxtan, gudāz-| melt, dissolve. widāzīhistan, widazih- [wt’cyh-stn'] be melted, dissolved. wider- , -išn(-īģ, -ih), v. widardan. widerān [wt(y)?n! | N guóarán) transient, dying. widest [zot(y)st! | N bidast] (hand) span (9 in.). ~ig [-yk'] span-sized, midget. widimās [wtym’s | (M wyd’m’s)] wonder, miracle. ~ig [-уА!] wonderful. ~ih: miracle. widimušt [wtymust | M wd(y)mwšt] astonished. ~ih: astonishment. *widwar [wytwl] contented, resigned, consoled. ~ih: contentment, resignation, consolation. wiftag [wyptk'] passive sodomite. wigrad [zogPt! | N bīdār] awake, alert. wigradan, wigras- [zog tn, wgl’s- | M wygr'd, wygr’s-] awaken, rouse. ~i$n(ih): awakening. wih-, v. wistan. wihan(ag) [zh?n(k)', (b-) | M wl?ng, N bahāna] cause, reason. wihēz- [wyhyc- | M twhyz-] move, progress. wihéz(ag) [wyhyc(k')] movement, progression.
1261:coarse stabr, sturg.
=== ō-words ===
223:āwēnišnīg : blameworthy. a-wēnišnīģ Pzwynšnyk'] invisible. awérag [”wylk!] = awērān. awērān Pwyln', ?5yPn! | N wērān] desolate, ruined. awestad ['zos??t! | M *zxoyst?d, N ēstād] master (craftsman). awestām [*wst?m | M ?wyst?m] province, district. awestarag [”wstlk! | N ustura] razor. awestardan, awestar- [*xvst/-tn! | P °wystr-, N suturdan] wipe; shave. mišn : wiping. awestwār Pwstwb’l | M ?wystw?r, N ustuwār] firm, reliable. “Аһ: reliability, firmness. awēšān [OLE?n, у. бу | М юу п, N ēšān] they, those. a-wināh Pwrs] innocent. a-winast [”wnst'] unharmed, immaculate. awiš [wbš | M ?wys] to him, it; postposition (= ©) to. awištāb Puwst*5 | M ’wyst?b, N šitāb] oppression. P awištādan, awišt- ['zoft2tn! | P ?wyst!dn] stand. awištāftan, awištāb- ['wi?j-tm | M ?wyšt?b-, N sitāftan, šitāb-] oppress; hasten (tr.). tāwištan, tāwāš- [HTYMWN-tn! < A Мут, V htm; ?wbstn' | M *wyšt] seal. a-wiyabanig Pwyd?f?nyk! | N biyābānī] astr. fixed (star). a-wizirignig Pweylinyk'] unavoidable, inevitable. āwurdan, awar- [YHYTYWN-in' < A hyty, У № | M wrd, "wr-, N ~] bring. āxēzīdan [>лусуѓп!] = āxistan. āxistan, āxēz- Phstn', ?hyc- | М *xyst, ?xyz-] rise, stand up. Axrámidan, āxrām- >А?т-уѓп! | M ?xr’m-, N xiram-idan] stride, strut. axtar [Atl | M *xtr, N ~] star, constellation, sign of the zodiac. axtar(ā)mār [Phil(?)m’/] astrologer. ~th: astrology. laxw Dell being, existence, world. ?axw Phw! | M *xvx] mind, will; vital force. *axw Phu'] lord. a-xwamn [’hwmn'] sleepless. axwān Phw’n'] = захм. a-xwārīh ['Aw'iyh] unhappiness. āxwarr [hwi | N àxur] manger, stable. --Sālār [-srd?I] head groom. a-xwaš [D BS YM] unpleasant; unhappy. ~ih: unhappiness. a-xwēškār [kwyšk'I] undutiful. ay Dy | N —J that is to say. āy-, у. amadan. ayāb [уор | М ik, N уд] or. ayāb- v. ayāftan.
=== āštīh ===
122:/abāz dādan б: 1. attribute, ascribe to; 2. appoint to. br ... add M fr! va-čār add helpless. delete á-distag ... (read ayidtag) add ‚тах |°р1°с | N farāz] acclivity. Afson ... add M ?pswn. Vagar ..., add useless. vāgēš [kw | (M "^ wa, P ?gwc), N aqóš] embrace, armful. add vājištag | gyštk' | P * gyšt, N ayišta] mixed, defiled. add \Ahliswang |*hlygwng] = Ard. delete Khriswang ... for alum ... read „alum |? № | N <] millet. Vāsnūd(ag) ... delete noble. aswür [|PR/LSYA < A pršy';.. āšnāg ... add acquainted with. āštīh ... add concord. ayad ... read |" byd^t' |... for bahr... and bahrag ... read bahr(ag) |b hl(k') | M bhr, N ~(a)] part, portion, share, lot; reason. (az) an bahrag ray : on that account, therefore. for  bahrwar ... read bahr(ag)war [b'hl(k)wl | N bahrawar| partaking, parti- cipator, partner. ~th : participation, advantage. balay add M by. add balgam |[blgm | N balyam] phlegm. baxtan ... add divide. bayaspān [by?sp^n' | = M]... bélür ... for M read P bylwr.
196:~ih: disbelief. an-āštīh [?n’styh] discord, enmity; disquiet, unrest. ānay-, v. ānīdan. an-ayād [?7’byd’t'] forgotten. an-āzarm [cim] without respect, dishonoured.
221:aswār [252002/, ?shw'l | N suwār] horseman, rider. ~th: horsemanship, riding. āsyāb [?sy?5] (water-)mill. āsyāg [sy’k!' | N asya] mill(-stone). aš [P$] the evil eye. āšixtan, āšinj- Pšyhtn!, ”*šnc- | P ?fyxt] pour, flow, overflow. aškamb [KLSE < A krs’; ”$kmb! | M *fkmb, N šikam] belly, womb. ~ag [-k! | N šikamba] = aškamb. āškārāg (34 1Q)k! | M sq?rg, N āškārā] obvious, evident. ~ih: revelation, confession. aškaragënidan [$k*Pkyn-ytn!] reveal, confess. aškūb рор | N dškē(b)) roof, ceiling. aškom(b) [’skwm(b')] = a$kamb. ašmā [LKWM < А l-kwm | MO fm'(h), N šumā] you (?1.). āšnāg Pwk! | M ”šYg, N ama] known. āšnawāģ [?$nw?k! | M ?snz?g, N šunawā] hearing. —ih: (sense of) hearing. āšnūdan, āšnaw- [OSMEN-tn! < А « ўт; топі | M? fnwdn, ?fnw-, N funüdan, funaw-] hear, understand. ~išn: hearing. або [šwk! = Av. ašawa] righteous. āšūb [>р | P swb, N ~] disturbance, turmoil. Aštād [s?t! | Md, N ~] the goddess Rectitude; cal. 26th day. aštag [štk'] messenger. ~th: mission. aštar РД whip. āštīh Pštyh | M 7st, N āštī] peace. Ašwahišt Piwhst'] = Ardwahišt. āšyān(ag) ['syd?n(k) | (M ?hy*ng), N ašyana] nest, lair. ātaxš Pths = Av. ātarš | N ātaš] fire. āwādaģ Pwb'tk! | J ?zo?d] generation. āwahan [wb’hn'] fortified place, stronghold. амат ['wbm | M ?w^m] time, season. -āwand [ла | M 2w(y)nd] suffix forming adjectives of quality. awar [LPNME < A I-pn-h | M ?wr] hither! come! awar-, v. āwurdan. a-wardàg ['wit?k&!] undeviating. a-wardisnig [?wltsnyk'] immutable. Аһ: immutability. āwarišn [zoblfn! | M *wryšn) abode, home. a-warzid [Pwicyt'] untilled. *Aiwas-, v. tāwištan. ама [Pc | N ~] voice, sound. a-wazisnig ['wcfnyk!] immobile. āwēnīdan, āwēn- ['wyn-ytn! | (P ?bzoyn-)] admonish, blame. ~i$n: blame, reproach.
1633:discord anāštīh.
1773:enmity anāštīh, dušmenīh.
```


## [2026-09-14T02:34:41.062Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for w in \"staxra\" \"stūna\" \"stuna\" \"raθaē\" \"radae\" \"rad-ae\" \"āxšti\" \"axsti\" \"fraēšta\" \"fraesta\" \"pairišti\" \"parsti\" \"avastāta\"; do echo \"### $w\"; grep -n -i \"$w\" BRT.txt | head -4; done",
 "description": "Grep Bartholomae AiW for Avestan forms"
}
```


### [2026-09-14T02:34:42.303Z] TOOL RESULT

```
### staxra
26551:•  j,  staxra-  Adj.  'stark,  fest',  inbes.  vom Winterfrost  'streng':  TS  mrUrS  ty&  V, 2.  22;  F.  /2;  —  zaya  ava%a  °rS  yat  .  . "der  Winter  ist  darum  (so)  streng,  weil . ," FrW. 8.t;  —  'rahe  FrW.  8.  a.
### stūna
### stuna
8551:•  j.  ust»m«m  Adv.:  s.  ustuna-.
26778:•  j.  stuna-  m.,  stunä-  f.  'Säule':  münm .,„,    .   Äktoi  T^-r'-Zl/'i.     ■-"  •■^(AH)  ilii™>Ä  »"^ii-^
29744:•  j.  hazaorö.stuna-'^  Adj.  'von  tausend Säulen  getragen,  tausendsäulig':  nmän>m  . . °n3m  Y._57.  21,  YL5.  loi.
### raθaē
### radae
8843:S4-J3',  —  *a/  aitahe  paiti  .  .  axaBa  V. JÄ68; — /fl/(ASn.)*'  alsa  nätrika paoifim :^ar»%anam  c^aräl  "was  soll  die  Frau  als erste  Speise  gemessen?"  V.5.S0;  —  Ictm (ASn.)3>  haxa  ha^  "baraiti  (sd.)  Y.tfa.S; 20,4;  —  kJng  ä  vaiihSus  fimat  mananhd /isti/{sd.)  "wer  sind  sie,  bei  denen  . ,"  Y. 4^.11;  —  kahmäi  fradaesayS  damqm  V. 2,1',  i;  —  ^Mahmäi*^  tg  alvahmi  paiti vals  . .  H.  1. 1 ;  —  kaAmai  vlvtduyi  (sd.) vasT  Y.  4j.  9;  —  las  akJ  kahya  akJ (sd.)  Y.^5.7;  —  kaht  vaca  vanni  kahe vaca  .  .  i  ana  vaca  vanäni  V.  ig.  8  f. ;  — kahmilt  haca  usahinanqtn  gaisanqm  ratu- fril  frajasaiti  (sd.)  "von  welchem  (Zeit- punkt) an  .  ."  '^{.46;  4-j~^o^;  —  k}  .. kä  (ISm.)  sp3ntä  ärmaitis  isA.)  "wer  .  .?, mit  wem  ,  ,?"  Y.5/.  ri;  —  kaSibyS  a^äi (sd.)  vohs  jimat  manaaha  Y.  46. 3 ;  44. 6.  a)    'wer    (von    zweien)?':    ku^rü
### rad-ae
25082:•  j.  raö'ae-star-,  rad-ae-ätä-,  ra95i-ätä-'' m.  'Krieger,  Kriegsheld':  ya'ha  «j  taxmS °tä  (NS.)  Yt  13.  67;  —  taxmim  tusim  'ia- nm  Yt  5,  58;  Vyt  26;  —  mihnm  .  .  yim yaztnte  'tärS  Yt.  10.  \i;  j.  53  '> ;  —  mihrfm . .  laxiram  °tam  Yt  70.  140;  112,  25,  102; —  iraosahe  . .  taxmake  .  .  'ta  (GS.)  Y. 57-33;  —  ätari  spmta  'i3ra<yS.)^  Ny.j. 6;  Y.  ä^2.8Gl.  A)insbe3.alsBezeichnung für  den  zweiten,  den  Kriegerstand  (vgl.  unter 'piära-):  shrava  '/i  (NS.)  västryö /ü^qs Asitis'  Y.  ig.  ij;  11. 6,  Yt.i3.89,  V.5.  38, '^•45^i  —  ähravarum  ..'iär>nt  ..vasirJm fsuyantftn  Vr.^.  2;  Yt2, 12;  —  a%auru- naSca  °tüua  västrySica  fiitymte  Yt/p.  8; 7J.88,  V.5.  57,  58;  —  västry^Z  fsuyatas ..  'tä  (GS.)  ..  a'iiaurunS  Y.  13.21.;  — asti  iir  haim  (sd.)  ydha  'tärahe^l  Y.13. 44;  4Si  Vyt  J,  16,  Az.5;  —  vUpe  saya °%äis'ti  (LS.)  "alle  Ausrilstungsgegenstände für  einen  Krieger"  V.  74-9;  9;  —  '^^<»- urunqscä  -tascä  (AP.)  västryas^a  f/uyants Y.  7j.  3;  —  a^aurunqs^a  'tarSsla  (AP.)3) väitryqsca  fiuyants  Vr.^j,  5;  —  hast»ma alahe  ama  'ta  Y.13.2.
25086:rad-aestä-
### āxšti
### axsti
4115:FrW.  4.3;  —  'rahe  mainySus  dämanam ^'^  '5'  3i  —  y^t  titarat  °rS  matnyus dähim  alahe  .  .  antan  pairi.aväit^m  (sd.) fokuca  mattö  atarsca  /J  hg  taurvayatsm tba^ä  °rahe  mainySus  drvats  Yt  7_J,  7  7  f. ; 13;  — yint  nöit  tiurr/pttte  'rS  mainym nsit  yatavS  fairikssca  Vt  1^.44;  —  ailm dahakim..yqm..  drujim  fraca  k>rmlat  'rS mainyus  Y.(?.8;  —  aal  ahe  paityarim  frä- ijrMiat  'rö  mainyus . .V.l. 2;  'J0.3,Aog.2^; —  pairiAä  .  .  yä  uzdtihat  'rS  mainyuS  .  , paiHj>r)tSe  Yt,  A",  39;  —  taxm?m  urupi  .  . yat  barata  'tvm  mainyBm  framitim  (sd.) aspake  JaArpa  ^risatjm  aiwi.gämanam Vt./^.  29;  — paiti.psrme  'nm  mainyBm V, /o.  5;  —  fränämiliti  duhjarstavari'  °r3 mainyus  ax^amanS  Yt/p.  96;  3.^;  — naiHs  xsayät  °rö  mainyus  duzdalnS  FrW. 4.  a ;  —  xsnagiira  akurahe  mazdä  tarSidlti 'raAe  mainyius  Yt.  i.  o;  —  daxstanam  ydi Amli  'rahe  ntainySus  daxstim  V.  2.  29;  P, 2-2,  Y,  7i>,  11;  —  apayafUamah^a  'rahe mainyius  xrafstra  Yt.  21.1;  —  'rif  mainyus . .  dtävanam  daivS  V.  ig.\;  —  vJspB.mahr- käatca  pairi  drvatat  yat  -rst  mainyaot VL/_j.7i;  /0.118,  Y.2-j~-i,  V.'/o.ie;  — ai  duida  °ra  mainyS  V.ii).^;  g,  1,44,  lt. 10,  Yt//.  19; —  iaÖx  dusda  'ra  mainyö V.  i^,  1 2 ;  —  *'rahe ''  *mainy9us  duzdamanH Y.  Ö/.  2;  V. /p.6;  —  skutara  "ra  mainyö V.  79. 3;  —  "rS  mainyus  pouru.mahrkS (Stveri.)  Yt  10. 97 ;  usw.
12617:mainyJtd  'ttm  mafyäi^ia  faiti  nSüÜ^m  V. z.  39.  a)  von  sichtbaren  körperlichen Mängeln  und  Leiden:  anäisca  kannis^a ..ava  -/«(IS.)  daxstavatUa  yä  rßit  peuru.- jira  (sd.)  fradaxita  Yt  5.  93;  —  ma  a%ra fi-akavö  mä  apakavS  .  .  tnüta,iSm  anyqm •tanqm  (Gen,  part  als  Subj.)  yBt  hmti anrahe  mainySus  daxStim  (s.  o.)  V.  2.  29;
16376:•  j.  pid-ana-  Adj.  —  ?  — :  pouru.spaxsti dürat  'na  of^ravana  darrfS.hax?6rayana Ytg.i.     Wertlos.
17567:•  j.  fraxSti  Adv.:  s.  fraxS^tay-,
### fraēšta
### fraesta
17499:•  g.  'fraeSta-  m.  'Gesandter,  Bote':  yavsi vTspsi  'tänhs  hr^hämä  "fiir  alle  Zeit  wollen wir  (deine)  Gesandten  sein"  V-^j?.  8".
### pairišti
### parsti
10443:winnen,  (als  Ziel)  erreichen':  ^^f/nwriv.,! srirä  baninava  gsrnvnäiti  YtiO.  13;  — j gpr7wnap'>  F. 21.  6)  '("li'  den  Sinnen,] dem  Verstand)  auffassen,  wahrnehmen,! begreifen':  vätd ..yint yava  vJtitn  nSnhaya hubaoStitimim  jigaurva  (iS.)*'  H.2.8;  36; —  Aata.mq'^rfm  taini.parStim  *upairi.- gatubyS  (sd.)  girspDm  Extr.  2;  t—  ka<,a.- mq%räi  ('iraie,  '^ra)  ..g^Dptäi  {'tafie, 'ta)  Extr.  j  (,  y,  4);  —  s.  noch  Jnggnbus' PPtA.   (nur    Äbleit)  Unklar:     *ayi.-
17886:mit^an  i)  'Jemanden  zu  Rate  ziehen': S.  Absol.  hqm.parstim  und  Inf.  hSmfar- iidif.        2)  'sich  beraten  mit  — ,  beraten
21237:(sd.)  dngvanhm  avS  Y.32, 14;  —  täis  zl nä  /yao^anai/dyentf(sd.)..Ay  ('insofern') as  *aojS.  näidyankifn  (sd.)  Y.^J^.  8;  — vaidä  tal  ya  aAml . .  anaisö  tnä  kamna/svä hyatcä  (Sp.  574  o.)  kamnäna  aAmX  Y. 46.3;  —  parstim  zl  %wa  yohanä  tat )mavatqm{sA.)  Ay  {'■<Nt)[')%wä  x^ayqs{5i) alitm  dyat  imavantim  Y.43, 10.  b)  im jAw.:  atcit  bä  lumS  Aaomai  y'  ('weil') vupe  anye  tnatävAs  ailma  Aacinte  Yt  //.  5 ; Y,  /0. 1 3 ;  —  avat  vayul  ba  nqma  aAmi y  »va  dqma  vayemi  Yt  i^.  43;  43f-^;  — aojists . .  y  dim  upanAacat . .  Aqm.vanitts Yt/p.  38f.;  —  aom  ofarmB  AangSurva- yata  . .  ^raltaond .  .y  as . .  vftT^ravastTtnB Yt/5.36;  38;  —  bawraini  vasfrä  vajtAata ,,y  asti  bawris{sd.)  sraiita  Yt.5. 129;  — wn'^rayriB  ..  nBil ..  yanyB  (sd.)  vaAmyB .. y  nürjm  .  ,  dafvayäsS  voAunim  va  taca- yänti  . .  Yt  J^  54;  —  ^banhvB  va  patU vajaanaAe  .  .  y  alta%a  *Aanjastlnte  pouru gaonaAe  (sd.)  u%aheca  N.  65.  IV)  die Folge  oder  den  Zweck  angebend  'so  dass; auf  dass,  damit';  a)  im  gAw.;  1)  mit dem  Praeteritum;  Ayatis.!!!)  ji 3.dibaomä (sd.)  .  .  upa.jasat  Ay  ('so  dass')  vtrstmtä (sd.)    aciitim    manB   Y. 30.(1.  2)    mit
29131:haslAäHalayä  -,    harn  dm  n  n  1)  -   Sü. :    saia- väiiHah.    —    ')  Ad«  ar.  *]admai;    %  403.   — «)  Vgl,  iSt  Y.  30.  10,  53.  3.  -  3)  S.  nmäna- No.  7. •    j,    haäa.m^^ra-    i)    Adj.    'mit    dem Mq^ra  zusammenseiend,  mit  ihm  eins'": zara^ultrim  °nm  Vr.  13.  i.         2)  m.  '(Mit- mq'^ra''',    d.  i.)     Ergänzungs/naSra,    Er- gänzung, Nachtrag  zur  Glaubenslehre'*': 'rtm  zainiparlUm,  °räi  zairti.parstili,  'rahe <zaini.parsiahe,  'ra  (VS.)  saini.parsta  Extr. \i-4.
### avastāta
```


## [2026-09-14T02:34:53.551Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### Friede\"; grep -n \"'Friede\" BRT.txt | head -8; echo \"### stura\"; grep -n -i \"stura-\\|stüra-\" BRT.txt | head -5; echo \"### staxma/stamba\"; grep -n -i \"staxma\\|stamba\\|stambana\" BRT.txt | head -5; echo \"### ā-stāna\"; grep -n -i \"ästäna-\\|astana-\\|upa.stäta\\|upastäta\\|avastäta\\|ava.stäta\" BRT.txt | head -6",
 "description": "Grep Bartholomae for more Avestan forms"
}
```


### [2026-09-14T02:34:53.700Z] TOOL RESULT

```
### Friede
### stura
7772:•  j.  ^öijrnata'stura-''  m.  EN,  eines  Gläu- bigen: avaryg3us  irgzavats  °ralie  aiagnd Yt;j..2s.
16495:•  j.  baeSatastura-  patr.  Adj.  'von  BaSsata- stura'-'>  abstammend,  dessen  Nachkomme': fratura  asntta  'rä  (GS.)  asaomJYt.  13.12$.
26761:avatghtm  (sd.)  Y.jrf-4;  ^T.  vciwcndel    Ny.       „  ^  AKri-i;  vgl.  »neh  «e»..  mhd.  j^^  'steif. J.  10;  — _y5  ^ijH   ahmäi  västravaitim  stsi       itatüich';  Bthl,  IF.  ii.  ijS. »tTj-J/fSp.  i38so.)  Y.50.2;— ^^"/(f  WT'«Ä/  ,  j    stiptay-  £  Name  eines  Insekts,  das *ustä  *j/»"    "denen  wir  beide  wünschen,   auf    Hunden    sclimaroUt':     duye    navaüi dass    es    ihnen    nach    Wunsch    gehe"    ^.  galwqm  pairi.yaoidaihtta   -tibyasca    ans- 4ß-i6;    —    a/    "i-^J    »tStighi    *J>aourvm  iritib}asca    -.yamiraHbyasca    vUpaäbyasca mazää  *ya^m  (sd)  stSi  Y.31.8;  —  nSil  pairi  aHitaäbyS  ySi  gahwam  pairiiavaiti spmiqm    dSTist  (Sp.  690  a)    ahmäi    stü  "zweimal  neunzig  Hunde  soll  er  von  St. armaitlm   \.4g.2-,  —   Ayat  ..  Bist  (Sp.   reinigen   und  von  An.  und  Vy.   und  von 430  m.)  ..  ahmäi  slH  dqn  ^JA  K/<7yfii/7|  ^11  den  bösesten  (Insekten),  die  auf  Hunden \.4S.io;  —    data  xratius  hixi-3  rai^ltit   schmarotzen"  V. 74.17. (sd.)  stöi  mahyä  räifng  .  .  iähil  ¥.50.6;!      Eig.  Bed.   und   Et.?    —    Pa,:    ddrptkrak, —  tum  tiB  äiraom  *tafftasU'>  "du,  O  A>.,  I      halb  {jap)  twtsskr. sollst  unser  Z.   sein"   Vr.j.7.        a)  im  •  j.   stivant*  in.  EN.   eines  Gläubigen: jAw,    mit    der   Negation,    in    altnbuüveja  /r3dat.vawhfus  •talö  aiaotiS  Yt  IJ.  121. Gebrauch  'der  nicht  existireQ  kann,  den      Ablcit.  mos  'siay-i    Bed.7 es  nicht  geben  kann' ^:  nöil  ma^S  gal^yj   •    j.    siai',    sli'i',    nur   KompA.:    sva. Sil  agjä  (sd.)  sunaiaoiti  gaosaiwe  "es  gibt ;  "stüra-.
### staxma/stamba
29784:PiL:   staxmak,   (lu  V.  3?)  erl.;   kum  ofF  apä-    praes    %   Aava-''>-   —  Perf    I   /iwäv     —
### ā-stāna
```


## [2026-09-14T02:35:03.077Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '29780,29790p' BRT.txt; echo \"=== axsti ===\"; grep -n \"xsti-\\|xUi-\\|äxsti\" BRT.txt | head -10; echo \"=== Frieden ===\"; grep -n \"Frieden\\|Friedens\" BRT.txt | head -6",
 "description": "Check BRT staxmak context and āxšti"
}
```


### [2026-09-14T02:35:03.168Z] TOOL RESULT

```
daroä  . ,  alä  'zs  smavai  "schenk  . .  durch  ! As'a  starke  Gewalt"  Y.33. 1 3 ;  — gartma  (sd.) , ^rS  hyat  .,  vartAsui  'tS  jtmal  matiat»As\ ". .  die  Macht  des  guten  Sinns  '>  . ."  Y.  .  j.  hahya-  Adj.  'der  es  mit  dem  Getreide, 4-3- ^-  3)  'Gewalt,  Gewalttat':  5a/ /i   der  Getreideerate  zu  tun  hat,  fnimentaiius',
snaehntis  .  .  •*!!  nivansaym  (sd.)    daaiaU(,a*paiHsJiaAya-{sA.):*paitilAaAlm 'htm Yt  ig.  8o;  —  amä  a^mff  'zasca  . .  äAi/aya  I  Vr.2.  a ;  —  *paUis.AaAyeAe  'Ayehe  Vr.  /.  1. (Sp.  1800  U.)    Y.  3p.  I*\  3)    'gewalt-  ,      Ableit.  aiu  "kakya-  n.  (mit  Verschiebung  dei
same    Wegnahme,    Raub':    ut  gSui  siuyl<      Wortakients).  —  PiL:  transskr.,  dain  dieEiL: tayäatra  -taaAai^ä  Y.  12. 2;  —  -zS  F.  25b. !     ^^  ^"''"'^  ^'^  "^'^  '>''•
AbleiL  —  Zum  V.  Aa«..  —  u.  sähai-  n.  —  \»   j.,  g.  ha(y)-  V.   'binden,    schliessen'.
PiL:   staxmak,   (lu  V.  3?)  erl.;   kum  ofF  apä-    praes    %   Aava-''>-   —  Perf    I   /iwäv     —
-    .)  D.i.    die   Macht,    wie   sie    dem   Gut-   PPn"-  '"*"-•  I°f-   °'*^'>«.   *'^3^rat. gesinnten  versprochen  ist    Pü.:  ia  ö  man  än\       l)  binden,fesseln':j'^4l'ffi(nämL<l!aAaffi) i  fa  vahaman  ilaxmak  äyii,    erL :  iS^-äns.  —    stätam  hitam  Aaitim  utvaiat  Aala  AinBtayS «)  Nach  Pa.  i^elmehr  lu  3.-   «  Sol    s^  zu    (sd.)  Yt /J.  100;  —  Ä»»'.     '    a) 'verbinden, hazaiihan-  und  Su. :  yfl  ha!hal  harati.     Falsch  ,..'       .',  .         i-fj  ._i
äzärit  (nach  Npü,)  MiLu  G.  20.  -  4)  S.  lu : «"«    einander     in    Verbmdun^    setzen': haznahtn-.
I  °Aita-,        a)  von  den  beiden  Teilen  der
•  j.  hazah'van- Adj.:  s.  unter  Aa<«ff-ia«-.  I  ^ff^Presse:  ya%a  *va  (nämL  Aavuita,
j.  htttdyäl:  s.  'had: j.  Aala,  Aase:  1,  Aaxay-.
•  j.  haSi-  f.  Name  einer  Datvl:  naiBm
=== axsti ===
4416:•  j.  an-äxätay  f.  'Unfriede':  vainJi  ahmt nmane  .  .  äxstis  "Um  Y,  60,  5 ;  —  iOm axsisis  'tSisÜa  mi>ra  xsayehe  dahyunqm Yt.  10.2  g.
14186:htn  . .  yö  äxstisca  . .  'u/s  (sd.)  spasys  (sd.) sffniäaAeYtit.14.  e)  von  einerspeziellen Gegnerin  des  Sraola :  sraosrm  . .  yS  JarUa daiciaya  'ujS  as.aojar>hs  *aAü.ittirynce  Y. 57.  15;  —  sraosS  .  .  'upm  jaynisto  Yt II.  y,  —  sraosS  ..'ußm  apansat  apayüxtai paiti  vatrat  'uxs  (als  Vok.)  ai^ä^re  .  ..- tum  .  .  aiva  .  .  anaiwyostis  AunaAi?  dat .  .  paiti.davata  ya  dagvi  'uxf  .  .  V.  j8. 3of.*'.  0   sonst:    *«»/  *tai  paiti  -uxs
=== Frieden ===
5581:Frieden  schafft'  (mit  NP.  im  I.Glied),  durch       Pü.:   -i-fö/.    —    >)    Hds.  a.*-Td/-.   —    »>  Pü.:
7115:•  j.  äxätay-  f.  i)  'Fnede.  Friedensver-  —  »/«/-/(Gen.?)  ^«ö/of«  N./o^;  —  ya^a trag':  vaiiut  ahmi  nmäne  Uis  anäxsnm  Y.  -.fars  kulkim  agstn?m  aiJnJhrmiaiti  hrwa- fjo.y,  —  tarn  'tdis  a».7xsm's7a  mi^ra  yäü  (sd.)  daiaiii  Y.7J.8;  —  *:bripi>'Wö xsayehe  daüyunam  Yt.  70.29;  —  sraos?m  (sd.)  .  .  astt  'tari .  .  kama  bipOtwS  ahvi.- ,  .  yS  'tlsca  (AP.)  urvaiHsca  dmjo  spasx5  ^.tme  F.  25b;  —  '%re  aEsman  isaiü  (sd.) (sd.)  spJnihahe  YL  7/.  14;  —  *'ti  'P-Y. 5.2;  14.T,—  baR'an  va^aiiam  aisim- 26'\  a)  mit  hqm.vainli-  Adj.  'sieg- 1  w^«,  , .  .^^  . .  „isirlnuyat  Y.i4-i\  3;  — reicher  Fneden':  Ulm  hqm.vaintim  Yx.-j.\j,Jspaäl>yS  sastm  baraiü  Hari  .  .  yaHbyS 1,  \tn.15,  is.i'\  5.2.1;—  '/äis  Aqm.-^aem  "ham.paMti  *xsajnmca  *säirmca vaintyä  S./.2;—  auch  Flur.:  *'tibyaseai'>  ^(^^:^  ^_.;.jspanam  para.car>ntatn  UarS  zasta *kqm.vaitttibyS  Vr.7/.i6.  2)  •■XPottim- \  adioaya  (sd.)'.  .  äat  yni  sr  asm  baraiti Stimmung,  Einklang  mit  -'  (Inatr.):  Hag'M  '  aSsrntm  va  . .  ä  kl'pas^am  frinaiH  atari dalnaya  V.j.i.  [Ytj6.i9:  hes  äxlta;  {z\x  A)  .  .  imat  .ikrö  (zu  A)  Sfnvaimn s.  axita-^  i(sd.)  v^  ahmSi  aismim  baraiti  V,6"2.7  — 10;
9637:•  j.  *kudat-sätay-'>  Adj.  'woher  Freude bietend  ?',  mit  der  Neg.  tait  'nicht  irgend woher,  nicht  irgendwelche  Freude  bietend' : ydii  sT  aam  nStt  daioyqm  . .  ass  rämö.däi- ttm'^  nöit  'säiflm'^  visps  aahvS . .  airyaram vaijs  /rämvai  "denn  wenn  ich  nicht  bewirkt hätte,  dass  auch  ein  nicht  irgend  welche Freuden  bietender  Ort  Frieden  gewährt, würde  die  ganze  Menschheit  nach  AV. gekommen  sein"  V.  j.  i;  i.
11631:(unter  ihnen  anrichten) ''  und  (so)  Frieden vor  ihnen  schaffen  den  frohen  Völkern,  . ." Y.5J.8.
13050:•  j ,  g.  dazdyü  Int  i)  'zu  gebeo,  zu  ge- 1 irähien':  gavffi  .  .  rämäcä  vSttrsmeä  d'  1 ". .  dem  Vieh  Frieden  und  Futter  zu  ge- währen" Y.  35.  4 ;  —  at  nS  asä  fryä  d°  \ Aaiufv/ta  (s±)  Y.44-t.  2)  'Jemanden; zu  besteUm,  zu  machen  zu  — '  (Akk.): altat  äim  .  .  d'  ahütnca  ratümca  yim ahur)m  mndam  "darum  wollen '*  wir ihn  .  .,  den  AkM.,  bestellen  zum  (zu unseim)  .  ."  Y.  27.  i.
22550:—  a/rfttämi  vavanvä''^  ..  6uye  vlspfm'"dtn  siegreichen  Frieden"  Vr.  7.  i  usw.; aarsa^^m  A.i.  10;  —  nffit . .  vanlUs.  i  a.) ', —  äxäsU  'lya  S./.a;  —  *axitibyasca vantäi  upa.äay3t  anrB  maitr/us  sp3iitai\*'Hbyö  Vr.iJ.i6.
```


## [2026-09-14T02:35:22.791Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### CHEUNG staH\"; grep -n \"staH\\|\\*staH-\" CHEUNG.txt | head -10; echo \"### CHEUNG axsti\"; grep -n -i \"āxšti\\|axšti\\|āštīh\\|āšti\" CHEUNG.txt | head -10",
 "description": "Grep Cheung for staH and āxšti"
}
```


### [2026-09-14T02:35:22.867Z] TOOL RESULT

```
### CHEUNG staH
11017:sim., go back to *fra- + *staH. 
23400:358 *staH 
23411:*staH ‘to place, set; [intr.] stand’ 
23455:*staH 359 
23506:360 *staH 
23573:*staHn ? ‘to take’ 
23598:© This root is perhaps originally a pres. n-stem of *staH (?). 
23995:instance, *staH ‘to place, set, stand’ and *@ra(n)é ‘to (op)press'. 
55885:*parH?. (s.v.), *staHn (s.v.), 
57368:*daH’, *kan', *staH 
### CHEUNG axsti
```


## [2026-09-14T02:35:25.086Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '23400,23520p' CHEUNG.txt",
 "description": "Read Cheung's *staH entry"
}
```


### [2026-09-14T02:35:25.159Z] TOOL RESULT

```
358 *staH 


© Further Ir. correspondences are not found. The structure of this possibly Ur. root is 
atypical of IE: regional borrowing ? 


“PIE LIV: — | Pok.: 
*REFERENCES: EVP: 77; DKS: 408a; NEVP: 98 


*staH ‘to place, set; [intr.] stand’ 

*AVESTAN: stä- ‘to place, set; (intr.) stand’ || (+ *aua-) ‘to enter; to settle (дозуп) || 
(+ *4-) ‘to take place’ || (+ *upa-) ‘to tread on’ || (+ *us-) ‘to get up, rise’ || (+ *pati-) 
‘to stay put, remain’ || (+ *pari-) ‘to refrain from’ || (+ *fra-) ‘to procede, go before’ 
|| (+ *ni-) ‘to order’ || (+ *ham-) ‘to come into existence’ = Liste: 64 

Pres. them. red.: IND. med. Zeg YAv. histahe (V 3.29), 3sg. Y Av. histaiti (Yt 8.9, Yt 8.32), ҮАУ. раш 
histaiti (Yt 10.36), med. YAv. histaité (Y 42.4, etc.), YAv. fraxstaite (Yt 10.107, Yt 19.92, V 15.45), 3р1. 
YAv. histanti (Yt 6.1, Yt 7.3, V 5.19, etc.), YAv. ham.histonti (Yt 8.32), med. YAv. histante, INJ. 3sg. 
Y Av. upa.histat (Yt 17.21), ? OAv. "axstat (Y 51.4), med. 3sg. YAv. fraxstata (Yt 13.97), med. 3pl. YAv. 
histonta (Yt), SUBJ. 159. ҮАУ. xsta (Y 12.3), med. 1sg. YAv. fraxstane (Y 9.20), 3sg. ҮАУ. paiti.histaiti 
(N 22), YAv. histät (Yt 8.32), Y Av. auua.histät (V 4.33, V 8.33, V 16.5), YAv. xstat (F 304), med. 3sg. 
Y Av. fraxstaite (Yt 10.107, Yt 19.92, V 15.45), 3р1. YAv. usahistan (Yt 19.11), ОРТ. 25р. ҮАУ. 
auua.histois (V 9.12), IMPV. 25р. Y Av. auua.hista (Yt 17.57), Y Av. upa.hista (Yt 17.21), usohista (V 
18.19, V 18.21, V 18.26, V 21.4), 2pl. YAv. usohistata (V 18.16, V 18.24); Aor. s-: SUBJ. 3sg. YAv. 
stanhaiti (N 42), OAv. stanhat (Y 50.4); Perf.: IND. 1sg. YAv. auua.hista (V 8.97, V 8.100, V 8.103), 3р1. 
Y Av. visastaro (Yt 19.8); Partic.: pres. YAv. histant-, med. YAv. histemna- (Yt 15.52, Yt 17.61, N 37), 
Y Av. paiti histemna- (Yt 10.36), perf. pass. Y Av. stata-, Y Av. auuastata- (F 149); Caus.: pres. IND. 15р. 
Y Av. astáiia (Y 13.3), 3sg. Y Av. ä.staiieiti (N 82), med. 1р1. YAv. ästäiiamaide (Vr 3.5), INJ. Zeg. ҮАУ. 
staiiat (Yt 13.78), med. 35р. Y Av. staiiata (Yt 10.89), SUBJ. 15р. YAv. ästaiia (Vr 3.1 f£), 35р. YAv. 
staiiāt (N 63), OPT. med. 3р1. YAv. astaiianta (V 3.18, V 5.49), IMPV.2sg. Y Av. auuastaiia (V 2.26) 
*OLD PERSIAN: stä- ‘to set, [med.] to stand’ || (+ *aua-) ‘to set down, place, restore’ || 
(+ ni-) ‘to enjoin, command’ = Kent: 210a 

Pres. red.: impf. IND. med. 3sg. aistatä <a-i-8-t-t-a> (DB 1.85); Caus.: impf. IND. 1590. avastayam < 
a-v-a-s-t-a-y-m> (DB 1.63, DB 1.66, DB 1.69), niyastayam < [n]-[i]-[8]-t-a-y-m> (DB 3.91), 
«n-i-[y]-[3]-t-a-y-m» DZe 8), < n-i-y-S-t-a-y-m> (XV 23), frastayam ‘I send forth’ <f-[r]-a-s-t-a-y-m> 
(DB 4.92), 3sg. niyastaya <n-i-8-[t]-[a]-[y]> (DSn 1), <n-i-y-8-t-a-y> (XPh 50, XV 21), nistäya 
<n-i-S-t-a-y> (XPh 52) 

MIDDLE PERSIAN: (+ *abi-) MMP ‘yst-, ВМР yst-, ’(y)st- (YK‘YMWN-) /ést-/ ‘to 
stay, stand, be’ (also aux.), MMP ‘ystyn-, BMP ’styn- (YK‘YMWN-) /éstén-/ (sec. 
caus.) ‘to place, put, set’, MMP ‘ystyh- (caus. pass. ?) ‘to be placed’ || (+ *aua-) 
BMP ’wst’- /östä-/ ‘to set out’ || (+ *upa-) MMP "Ьуз! ‘place of refuge’, ВМР ’pst’n 
/abestan/, (?) BMP "Bet ml /abestam/ ‘reliance, refuge, support, trust’ || (+ *pari-) 
MMP pryst-, BMP plst- /parist-/ ‘to serve (through worship); to worship’ || (+ *fra-) 
MMP pryst-, fryst-, BMP plyst- (SDRWN-) ‘to send’ > DMMPP: 99b f., 17a, 
282b, 159b 

(+ *abi-) Widely attested: Pres.: IND. 3sg. MMP ‘ystyd, ‘styd, 1р1. MMP ‘yst’m, 2р1. MMP ‘ystyd, 3р1. 
MMP ‘ystynd, etc. || (+ *aua-) Pres.: IND. 1р1. BMP ’wstym /dstém/; Partic.: perf. pass. BMP "watt 


*staH 359 


/ostad/ || (+ *pari-) Pres.: IND. 3р1. MMP prystynd, SUBJ. 3р1. MMP pryst’nd || (+ *fra-) Pres.: IND. 25р. 
BMP plystyh /fréstéh/, 152. MMP pryst’n, 3sg. MMP pryst’d, 3р1. MMP pryst’nd, IMPV. 2sg. MMP 
*pryst; Partic.: perf. pass. MMP fryst’d, pryst'd, II prystyd, prystyhyst; Inf.: MMP pryst’dn 

*PARTHIAN: 'Sf-, ‘yst- ‘to stay, be situated’ || (+ *abi-)’wyst- ‘to be situated’, (caus. 
?) ’wyst- ‘to place, put’ = Ghilain: 78, 90 | DMMPP: 94, 76 

Pres.: IND. 1sg. “т, “уһ, 3sg. “уа, “ууа, 1р1. “т, 2р1. “уа, 3р1. * ‘упа, ‘yStyynd, SUBJ. 2sg., 
3sg. “РА, 35р. ‘yst’h, OPT. *‘Styndyh; Partic.: perf. pass. П “Ра, ‘yst’d || (+ *abi-) Pres.: IND. 35р. 
"wystyd, 3р1. ’wystynd, ’wystynd, SUBJ. 25р. ’wyst’h, ? *’wyst’; Partic.: perf. pass. "wyst'd, "wst'd; Inf.: 
‘wyst’dn; Caus. (?): pres. 15р. ’wyst’m, 3р1. 'wystynd, SUBJ. 15р. ’wyst’n, ’wst’n, 2sg. *’wyst’, IMPV. 
2sg. "wst, 2р1. ’wystyd 

*KHOTANESE: stä- (stä-) ‘to stand; be’, stas- (inch.) ‘to come to a standstill; to 
become weary’ || (+ *aua-) vast- (vist-) ‘to remain’, (perf.) also ‘to approach’, vistä- 
(visti-) ‘to place, establish’ || (+ *a-) ? est- (*a-hista- ?) ‘to endure, be firm’ || (+ 
*pati-) OKh. past- ‘to arise, set out’, OKh. pastafi- (caus.) ‘to satisfy; to promote’ 
c SGS: 128 f., 120 f., 20, 77 

*SOGDIAN: SSogd. ’sty- ‘to stay, wait for’ || (+ *apa-) BSogd. ’psty ‘to entrust’ (diff. 
prev. ?), BSogd. "pstnh ‘delay’, BSogd. pstnh, CSogd. pstn’ (Ё) ‘respite’ || (+ *abi-) 
? SSogd. "Dok ‘settled’ || (+ *aua-) BSogd. ’wst- ‘to stand, become’, BSogd. 
"wst-, CSogd. ’wst-, MSogd. ’wst- ‘to stand, fix, put, place, set, lay (up, down)’, 
BSogd. (caus.) ’wst’y ‘to put, fix’ || (+ *a-) BSogd. ’’stnyh ‘permanence’, SSogd. 
"'st'nyk, CSogd. st’nyq ‘messenger’ || (+ *upa-) SSogd. (’)psty- ‘to instruct’, BSogd. 
"p3ty- ‘to entrust’, CSogd. pšty- ‘to admonish, instruct (Sims-Williams 1985: 62), 
MSogd. ’psty- ‘to command, order’ || (+ *pati-) BSogd. ptsty- ‘to lean on, rest’ || (+ 
*pari-) BSogd. prst’y, CSogd. pst’y ‘to prepare, make ready’ || (+ *fra-) SSogd. 
prsty ‘to send’ || (+ *ni-) SSogd. nysty ‘to order’, BSogd. nysty ‘to establish, fix’, 
CSogd. пуу ‘to send word, announce’ || (+ *ham-) ? BSogd. ’nst’y-, CSogd. ’st’y- 
‘to show’. 9 For a survey of the (esp. Manichaean) Sogdian forms see GMS: 
§552-559. 

Pres.: SUBJ. 15р. SSogd. ’sty’n {hapax} || (+ *apa-) Pres.: IND. 1sg. dur. BSogd. ’psty’m ’skwn {hapax} 
|| (+ *aua-) Widely attested: Pres.: IND. 35р. BSogd. ’wst, MSogd. ’wstyyt, 3pl. BSogd. ’wst’nt, SUBJ. 
3sg. BSogd. ’wst’t, OPT. 35р. CSogd. "wsty". etc. || (+ *upa-) Pres.: IND. 1pl. dur. BSogd. ’pSty’m ’skwn, 
3р1. CSogd. pstynt, Impf.: IND. 1sg. dur. SSogd. ""psty^m ’skwn, 3sg. CSogd. p’Sty; Pret.: tr. IND. 1sg. 
SSogd. pst'tw ó'rm, SSogd. *’pst’tw 6’r’m, 35р. SSogd. *’pst’t ö’rt || (+ *pati-) Inf.: BSogd. ptsty’y || (+ 
*pari-) Impf.: IND. 35р. CSogd. pryst’y; Pret.: tr. IND. 35р. CSogd. pst'd'rt, 2р1. MSogd. prst'tó róó; 
Partic.: pres. MSogd. prst’ynyy, perf. pass. CSogd. pst'ty t (pl.) ‘prepared’; Inf: pret. BSogd. prst’ty, 
CSogd. pst’yt, Pass.: pret. IND. 3sg. MSogd. prst’ty ’ktyy ‘was prepared’, pperf. intr. IND. 3sg. MSogd. 
prst’tyh wm’t (Kaw.G: 68) || (+ *fra-) Pres.: IND. 1sg. SSogd. prsty’m, SUBJ. 3sg. SSogd. prsty’t, OPT. 
2sg. SSogd. prstyy, 3sg. SSogd. prstyy; Partic.: perf. pass. SSogd. prst’t || (+ *ni-) Well attested: Pres.: 
IND. Ipl. pres. MSogd. nystymskwn, IMPV. 25р. SSogd. nsty ‘announce’; Impf.: IND. 1sg. MSogd. 
mnst^yw, 3sg. SSogd. nysty, CSogd. nysty, 3р1. CSogd. nystynt, INJ. 1sg. SSogd. nSty’w; Pret.: tr. IND. 
lsg. SSogd. nst’tw ó rm, 35р. BSogd. nyst’t ô’rt, etc. || (+ *ham-) Widely attested: Pres.: IND. 15р. 


360 *staH 


BSogd. "nst'ym, 2sg. BSogd. ’nst’y’y, 3sg. BSogd. ’nst’yt, CSogd. *’styt, MSogd. "nst'yt, dur. CSogd. 
*Stytq, CSogd. "stytqn, etc. 

*CHORESMIAN: (+ *apa-) 'bst”- ‘to stand apart’ || (+ *aua-) ws(y)- ‘to put, place 
on(to)’ © Samadi: 26, 221 f. 

*BACTRIAN: (+ *ара-) oßıotavo ‘waste of time, inconvenience’ || (+ *abi-) ? 
aBtiptado ‘landlord, (estate) owner, siss’, aßıpraoavo ‘estate’ || (+ *aua-) wota- 
‘to place, put, impose’ || (+ *pari-) mapotptaoo ‘surrounding area’ || (+ *fra-) 
форти- ‘to send’ = S-W, Bact.: 175a, 175b, 234b, 217a, 230a 

*NWIR: Delij. esdan ‘to stand; to go’, Gz. iss-/issä, Siv. isak-, isék-, esak-/esakiä ‘to
```


## [2026-09-14T02:35:44.592Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### fraesta in CHEUNG\"; grep -n -i \"fraešta\\|fraesta\\|frēstag\\|frestag\" CHEUNG.txt | head -10; echo; echo \"### *HaišH root\"; grep -n \"^\\*Hai\\|\\*HaiH\\|\\*ais\\b\\|aēš-\" CHEUNG.txt | head -10",
 "description": "Grep Cheung for fraēšta and the aēš- root"
}
```


### [2026-09-14T02:35:44.667Z] TOOL RESULT

```
### fraesta in CHEUNG
35466:plystk /frestag/, 159 

### *HaišH root
7409:*Hai) || (+ *fra-) SSogd. Вт, CSogd. f$’m (caus.) ‘to send’ || (+ *ni-) CSogd. 
10739:*Hai ‘to go’ 
10773:*Hai 155 
10870:*Haid 157 
10898:*Haid ‘to burn, set fire’ 
10937:*Hais ‘to be able, rule’ 
10957:*Hais ‘to desire, look for’ 
10993:*Haiz 159 
10996:*HaisH ‘to set in motion’ 
11048:*Haiz ‘to long for, desire’
```


## [2026-09-14T02:35:47.050Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '10996,11050p' CHEUNG.txt",
 "description": "Read Cheung *HaišH entry"
}
```


### [2026-09-14T02:35:47.111Z] TOOL RESULT

```
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

*IE COGNATES: Gr. îváo ‘I empty’, Gr. otpa (n.) ‘stormy attack, instigation’, Lat. 
ira ‘anger, rage’, ON eisa ‘to rush in’ 

*REFERENCES: Werba 1997: 336 f.; Paul 1998: 311b; ESIJa I: 124 ff.; Shahbakhsh: s.v. gis- 


*Haiz ‘to long for, desire’ 

*AVESTAN: 1Z- ‘to long for, desire’ = Liste: 13
```


## [2026-09-14T02:36:18.080Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for w in \"āštīh\" \"aštih\" \"ʾštyh\" \"ostad\" \"'wst't\" \"stun\" \"stahm\" \"sturg\" \"frestak\" \"paristitan\"; do echo \"### $w\"; grep -n -i -- \"$w\" NYB_vol2_glossary.txt | head -3; done",
 "description": "Grep Nyberg glossary"
}
```


### [2026-09-14T02:36:19.052Z] TOOL RESULT

```
### āštīh
### aštih
### ʾštyh
### ostad
### 'wst't
### stun
1434:én [inser., Ps. ZNH, but already in the inser. the z is often stunted; BP ZNH] dem. pron. this here, always referring to the present situation, that of the speaker, or to what is to follow; no pl.: api-n pad pat én darrak% nihat api-n tigr tar han citak be apakand we set our foot on this rock here and shot the arrow beyond that cairn yonder HajB:6-8; én damik this earth, our earth; én dam, én dam u dahisn, en getäh this world; én apécak vēh-dēn íi mäzdesnän this pure good religion of the Mazdayasnians 84? eto.; always én dén this (our) religion, of the Mazdaism; pat én apēgumān būtan ku to entertain no doubt about the fact that 634 etc.; vicčirišn ... en kū the explan- ation is this that 121"; — én i forms an elliptic gen.: frdc én % man yaz perform what here is mine (my duty, the rite incumbent on me on this occasion) 535; én būt i 6 peš gobam this happened which I am now going to tell 54!?; — én and, v. and. — Skr ena-; not in Av. and OP; SW w.: MPrs. ‘yn (no pl, instead im&sän, imin are used); Paz. NP in. Tedesco, Dial. 216.
3208:Rag [l'k']the name of a district and a town: né ka étar har 2 6 ham rasénd ~ u Notar not (even) when the two, Rag and Notar, come together here (i.e., never) 4316-17, 5017; fratom hac ax" 4 astomand andar ~ u Notar as the first of terrestrial beings between R. and N. (— far and wide, throughout the world) 5317-18, — A proverbial saying using op- posites to symbolize either absurdity or comprehensiveness. The saying is mean- ingless unless it refers to actual and well known geographical facts. Notar, other- wise unknown as a place-name, can only refer to the country of King Vištaspa, who derived his origin from Naotara the son of Manušcihr, thus symbolizing Eastern Iran (the Notars founded Tis, 1147-8). Rag must then be the OP Raga mentioned in the Behistun inseription (270, 32) as a district in Media ('Pdyat, called xčpoc by Arrianos III, 20, 2), thus representing Western Iran. That this dis- - trict had, already in Achaemenian time, a capital of the same name can scarcely be doubted, and is not contradicted by Strabo’s notice (C 525) that Alexander’s general Nikanor founded, besides other
3552:stunā-; MPrth ‘stwn ‘mast’ (MHC); M-
### stahm
1459:šton [ytwn'; HKYN 467] thus, in this way, passim; such 6215; han ~ 345, e(t) ~ 6920-21 such as that, as this; hàn i ~ such things 5817; — before an adj.: so 1225, 3724 ete. before an adv. 5611-12, 1192; — governed by a vb. of saying, thinking, perceiving etc., it anticipates a clause with kū ‘that’ 11. 34 etc. passim; ~ kartan kū to manage things so that 6°. 205; — ~ kū, ~ ka, ~ + consecutive: so that: a) ~ kū 1119, 7726, 105%; such that 1419-1; ~ stahmaktar būt hät ku would have been too violert to permit «148
1781:11814-15; — unfulfilled condition: past pt. + hé, or hà(h), or hat, pl. hand (v. h-): ~ citak city (HWH =) he, adak ... but (HWH =) kē if a cairn (v. s. v. citäk) had been erected, it would have been . HajB:9-10; —-am...n&özathäh,as...be apasthénit hah if I had not killed him he would have destroyed 3121-321; 3221-22, 3322-24, mo Kai-Xösröi uzdēscār . ne kand hät . . . adak patiyärak čton stahmaktar but hat ku ... if K. had not destroyed the heathen temple . the evil powers would have been so much more violent that ... 7113-18; —-am ūtšān ne ozat (HWH-nd =) hand Ahriman bit hah if they had not been killed by me A. would have become 331-9, — 2. without apodosis, expressing & wish: if only . .! would that . . .! ~-am zinhär (g.v.) dahēt would that you give... .! 1522-23; — mā ~ = NP magar perhaps 6. 137. — 3. in a dependent deliberative question: ~ ... atvāp whether ... or 268-9, — < OP ha-karam ‘once’; MPrs ’gr; Paz. NP agar; not in Prth, v. ak.
3349:Rötastahm [lwtsthm] n. pr. 1162. — NP Rustam; Old Sogd rwstmy, Reichelt, Sogd. Handschr.- R. II, 63.
### sturg
### frestak
### paristitan
2961:paristätan [plst’tn'], paristitan [plstytn'] parist- to worship, to adore, to submit to, to embrace (a religion) 194. 7511, 82.12, — < pari + stā-, v. ēstātan and cf par- ēstātan; Prth *part-štā- in Arm. lw. am- barišt ‘impious’ < Arm neg. an- + *parištā-, pastaun < *parštaun < "pariš- tamna- (middle pt.) ‘cult, service, office’, past-em ‘to worship’; in SW with -st- > -st-: MPrs pres. pryst-, and the inf. assum- ing the SW ending -ītan (cf MPrth pwrs'dn: MPrs pwrsydn, etc.): Paz. pa- rastidan parast- = NP; Verbum 194 sq.
```


## [2026-09-14T02:36:24.281Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '3550,3556p' NYB_vol2_glossary.txt; echo \"=== ēstātan ===\"; grep -n \"ēstātan \\[\" NYB_vol2_glossary.txt | head -3",
 "description": "Read Nyberg stūn and ēstātan entries"
}
```


### [2026-09-14T02:36:24.369Z] TOOL RESULT

```
stör-gäh [~ g's] stable 4?5. stor-pain [—-p?n'] equerry 62%; equestrian, pl. cas. rect. ~ 201,
stünak [stwnk'] pillar 3919.29; trunk, of the human body 727. + Av. (1608) stūna-,
stunā-; MPrth ‘stwn ‘mast’ (MHC); M-
Prs ‘(y)stwn ‘pillar’; Paz. stün ‘column’, stunaa ‘trunk’ (SGV); NP sutün ‘column’, sutünah ‘pivot’.
stür [stwl] juridical term: tutor, curator,
‘a man who has taken upon himself the duty to administer some part of the property of a deceased man for the benefit of someone who shall propagate the name of the deceased: (a capital sin škenet who breaks his tutorial engagement (to administer the property for the fos- terling) 828, Paz. star, Skr. v. stara- (simply taken over from Paz.) -pravriti-käritäm bhanakti, with the explanation: kila: kašcit apatya-hinah svargi bhavati, tasya dravyena tan-näma-kirtanäya tad-vamša- vrddhaye-ca kam-api purusam pratisthiyate ‘that is: somebody having died without progeny, he [the other man] is charged to provide [pratisthīyate ?] for a human be- ing, whoever it may be, by means of the property of the deceased, in order to preserve the name of the latter and prop- agate his family’. The procedure does not in itself imply adoption, but the term seems to have been extended to this mean- ing too, ef BdA p. 236-3; occurs in a great variety of legal trans- actions, v. Bthl, ZsR I, III-V (v. Indices), Pagliaro, RSO XXIII, 1948, 62-65; etymology: ibd. 62 n. 2.
stūrēh tutorship, curatorship, v. above: ke ~ rāyēnēt he who administers a tutor-
=== ēstātan ===
2952:par-ēstātan [pl YK‘YMWN-tn'] to go and stand in front of (pēš) a p. in order to protect him: peš Zartuxšt par-ēstāt 4919-20, — pari + ēstātan, cf Av. (1603) pairi-stä ‘to check, to prevent, to with- hold’.
```


## [2026-09-14T02:36:30.628Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n 1,60p tools/ref_page.py",
 "description": "Inspect ref_page tool"
}
```


### [2026-09-14T02:36:30.677Z] TOOL RESULT

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


## [2026-09-14T02:36:42.321Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; head -3 BQT_v1_pages.txt; echo ---; grep -n \"\\[pdf page\" BQT_v1_pages.txt | head -5; echo \"--- total ff:\"; tr -cd '\\f' < BQT_v1_pages.txt | wc -c; echo \"--- v2:\"; grep -n \"\\[pdf page\" BQT_v2_pages.txt | head -3; tr -cd '\\f' < BQT_v2_pages.txt | wc -c",
 "description": "Inspect BQT page text files"
}
```


### [2026-09-14T02:36:43.623Z] TOOL RESULT

```
۱ ۵ ۱! ۱
7 موم ۳ لام
م ۱ 0 و طق صفرررنیاعدریرماروی
---
--- total ff:
776
--- v2:
683
```


## [2026-09-14T02:36:50.228Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for w in \"سیتاک\" \"ستاک\" \"بغستان\" \"آستان\" \"ارتشتار\" \"استاد\" \"آشتی\" \"استخر\"; do echo \"### $w\"; grep -c \"$w\" BQT_v1_pages.txt BQT_v2_pages.txt 2>/dev/null; done",
 "description": "Grep BQT text for Persian headwords"
}
```


### [2026-09-14T02:36:51.319Z] TOOL RESULT

```
### سیتاک
BQT_v1_pages.txt:0
BQT_v2_pages.txt:0
### ستاک
BQT_v1_pages.txt:0
BQT_v2_pages.txt:2
### بغستان
BQT_v1_pages.txt:0
BQT_v2_pages.txt:0
### آستان
BQT_v1_pages.txt:8
BQT_v2_pages.txt:7
### ارتشتار
BQT_v2_pages.txt:0
BQT_v1_pages.txt:0
### استاد
BQT_v1_pages.txt:78
BQT_v2_pages.txt:63
### آشتی
BQT_v1_pages.txt:5
BQT_v2_pages.txt:0
### استخر
BQT_v1_pages.txt:20
BQT_v2_pages.txt:9
```


## [2026-09-14T02:36:56.939Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(json.dumps(d['BQT'].get('scans'),ensure_ascii=False,indent=1)[:2000]); print('ARB:',json.dumps(d.get('ARB'),ensure_ascii=False)[:400]); print('AVG local ok')\n\"",
 "description": "Check BQT scans config"
}
```


### [2026-09-14T02:36:58.102Z] TOOL RESULT

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
ARB: {"title": "al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edition)", "kind": "archive_djvu", "url": "https://archive.org/details/mo3rb (probably the Shakir edition) ; https://archive.org/details/almo3rab_gwaliqy_f_abduraheem (F. 'Abd al-Rahim ed., Damascus 1990) ; also uc1.aa0003615705 / AAlexandrina-148752 (Sachau's Leipzig 1867 ed.) ; t
AVG local ok
```


## [2026-09-14T02:37:02.768Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/ref_page.py BQT:1463 2>&1 | head -60",
 "description": "Fetch BQT page 1463"
}
```


### [2026-09-14T02:37:12.129Z] TOOL RESULT

```
REF: BQT:1463  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 256  OCR-lang: fas

-حچ۱2- فرشك
کشیدن نباشد ‎٩‏ . بالف کشیدموبنون‌دیگرزده, کنایه‌ازروحایان باشد.
۰ ظ‌ ۰ ۰ ,
فرش باستان « بکس ین و بای فرشتةٌ سحاب - بنتح سین بی‌ضله :
امجد بالف کشیده,بمعنی فرش خاك است که کنابه | کنایه از میکائیل علیه‌اللام (۱) است. .
از زمین باشد و عربان ار شکوبند . فرش خالك - بکرتات. بممنی‌فرش
فرشتو 4 ؟ - بروزن و معنی پرستوه باستان است که کنایه از زمین باشد .
باشد که عربان خطاف کوبند ؛ و بحذف کاف‌هم فرش دورد نگ - کنایه از روزکار
آمده اس ت که فرشتو باشد . است باعتبارشب وروز- وکنایه از زمین‌هم هست.
فرشته ۴ - بکس اول وئانی و سکون فرش عاج * - کنایه از برف است
ثالث وفتح فوقانی؛ معروف‌است وجربی ملك‌خوانند. که روی زمین را سفید کرده باشد ۰
۹ +4 ۰5 ۵ ه
(۷) چك : عم
۱- (عر) « فرش بالفتح» باط افکنده - وکشت‌ب رکه کسترده - ودشت فراغ وجای
گاه - و شتران ربزه - وخرد و باريك از درخت وهیزم - و حال و اندوه سخت - وکاو و
کوسپند وستو رکشتنی وخوردنی-واندك کشا د کی رد ین ات اد
درپای شتر » و آن محمود است - و دروغ > ود تفر 2
« منتهی‌الارب». ۴ < فرستوك < پرستو ات مه مهن او ۳)
وا ی است له و اعد ان 9 کمک
< پرشتوه > فرستو ‏ فراستوه > فراشترو < ۹ ۱ 2
فراشتروك << فراشتك < فراشتوله ۳ پرستوك : 1 ردان
(جم.) ۰ ۴ فرشته ۰ مانکرت ۹ ۱ 1 ۳ پ ۸ 1
هط 0۳89(از: ۳0۲8 683) ( سفیر)ءایرانی ال 0 7 :6 4 5
باستان ۶۳215312 (از:۳8- 2191 ) ( مقس : : ۱ ,9 اه : 1
قاصد ) ۶« بارتولمه ۳۱ ۰ اوستا ۲۳2851118 ۵ 1 ۱
« بار تولمه ۹۷۵ ۰ ارمنی ع 13۳690081 از 1 0 ۱ 6
1۴ ؛ فارسی جدیدط 119018 (لپی 1 1 رو سرا .۱
۱ ی : ! مه یس 111
شمال غربی), ۲1719127 (لهجهٌ جنوب غربی ). ار !1 : 0 ا !
قس : فرستادنءاستادن « نیب رکه ۷۹ ۶ اسشق- 1 و بوسر ۱۱زا
خوبشان۸۱۹ 819 ۷ ۴ - (ص) اج( ۰ و ا!
استخوان بشت دایه دربایی ۲ عامه عاج را : اه ام ۳ ۸ ً
دندان فیل گوبند * منتهی الارب > ۰ ۱ : 4 ۷ هن ی ی
8 - در تکلم امروز خراسان ۲2۳69101 4 پر 4 کل بیجن
دانپای انگور ريخته از خوشه است که انگور وا وک
فروش بعد از بیرون آوردن خوعه‌ها از سبد
آنچه دان شده باشد بنام « فرشك > علیحده می فرشته (صویس خیالی)
فروشد « فرهنگه نظام > اموْلف فرهنگه اخیر کوید : دخهٌ السامی تزد من خطی و نوشتهٌ آخر
قرن هفتم‌«جری است‌والفاظ پاحرکات نوشته شده و فرشك با فتح اول وضم دوهوسکون سوم‌است .
```


## [2026-09-14T02:37:24.481Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/ref_page.py BQT:1816 2>&1 | head -45",
 "description": "Fetch BQT page 1816"
}
```


### [2026-09-14T02:37:25.822Z] TOOL RESULT

```
(no exact page map; using offset -1205 -> pdf page 611; check the printed number and re-run with --pdf-page if off)
REF: BQT:1816  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 612  OCR-lang: fas

بیان یازدهم
در کاف فارسی با زای فارسی مشتمل 32 چهار لغت
وا ۱ - بنم اول و نانی‌بالف کدیده | بمعتی فیرباشد وآن صمفی‌است سباه که بر درز-
و بزای فارسی زده » چینه دان مرغانرا کوبنن | های کشتی و جهاز مالند - و بمعنی سیم سوخته
وبعربی حوصله خواند .# وسواد زرگری هم آمده است .
ارچ هر
گزدهم بفتح اول و سکون ثانی گم - بنم اول و سکون ثالی و میم ء
وفتح دال ابجد وها وسکون میم » دام پهلوانی | درخت سده را کوبند که درخت پعه غال است
است ایرانی ۰ وبمربی شجرقةالیق خوانندگ - وبمعتی اندوه ودل
گوف ؟ < بفتح اول و سکون نانی وفاء تنگی هم بنظرآمده است 8 .
بیان دواز دهم
در کاف فارسی با سین بی نقطه مشتّمل بر بیست و بك لغت وکنایت
کار ۹ ۰ سم اول بروزن دچارء بمعنی باشد بچه و بمعئی خوردن هم هست‌لیکن‌خوردن
گذارباشد که از گذاشتن است۷ - وامربگذاشتن | شراب وغم خوردن ۱۴.
هم هست بعتی بگذار ۷ - وبمعتی خورندة غم گسارده ۱۴ بروزن و معنی کذاشته
و خورنده شراب لیز هت ۸ همچو مگ ار است .
و میگار ‎٩‏ . مت » بنتح اول‌بروزن دست » بمعنی
گساردن *۱- "پروزن ومعمنی گذاشتن۷ | زشت و قبیح و نازیبا باشد ۱۴. ۱
۱ ۹ - رد :کزار . در رشیدی «گزار بالسم, چینه‌دان مرغ » اما دردشهٌ سروری بکاف
تازی آمده ». ۲ - ۳ط87548 ( پهلوان ایرانی ) ۶ فپرست ولف ؟.
۴ -رك :کزف ,کشف . ورك :کرف . ۴ - رك : رشیدی .
8 - مسحف «کرم» ( بشم اول ) . ‎٩‏ - رك : کاردن .
۷ - تلفظی درگذاردن . ۸ - اسم فاعل مرخم .
‎٩‏ - اندهگار من شد واندء بمن گذاغت وامق چه کرد درقم مضرا, من‌آ نکنم.
* از :گار (ه.م.)+دن ( پوند مصدری ) . ۹۱ باین معنی شاهدی باد
تکرده‌اند رك : کار گارده ۰ ۴قی: باده گسار, غمگار ۰ ورد ح ۹۳
ارزگ ام مفعول ازه گاردن» (و.م.):
سافیا مر مرا ازآن می ده که غ من از و گارده شد. آپوشکور بلخی «رشدی»؛ ۰
۴ دلبرا دورخ تو بی خوبست « از چه با یار کارکست کنی ؟
عماره مروزی « لغت فرس ۳۷ .
۵ گزدم - رك :کردم .
```


## [2026-09-14T02:37:35.111Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; grep -n \"گستاخ\" BQT_v3_pages.txt | head -5; echo \"=== lashkar ===\"; grep -n \"لشکر\" BQT_v3_pages.txt | head -5; grep -n \"لشکر\" BQT_v4_pages.txt | head -5",
 "description": "Grep BQT vol3/4 OCR for gostāx and laškar"
}
```


### [2026-09-14T02:37:35.201Z] TOOL RESULT

```
45028:‏گستاخ دست «کنابه از چابدست
=== lashkar ===
2466:OW ‏لشکر سوار شده متوجه کوه دماوند گردید‎
2746:‏شبهر - ینتم ها بر وزن لشکر » منفار
5183:= وهزیمت لشکر را نیز گوبند.
5319:کریختن و هزیمت و شکت لشکر هم آمده
5486:- و رخته شدن - وث‌کستن لشکر آمده است +
1188:قرو ستبی دل دشمن بدا ن كلك شهابآبین بدرانی صف لشکر بدان تیغ فلك مانا -
1499:اونداشت فرمو دکهآنچه لشکر کوفه بود پدیتور ماهاما؟٩‏ - با ها و میم هر دو پالف
1622:بنوکران دهند - لشکر اسلا کربخت وبمرو رفت ماهوبه باخاقان
1640:نت و بیژن برای جنگه با او لشکر کشید و دربن جنگه ماهو ی کشته شد . رك : شاهنامة بخ
1757:ز قنوج و از دلیر و مرغ وهای برفتند چون باد لشکر زجای. »
```


## [2026-09-14T02:37:38.123Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; awk 'NR>=45010 && NR<=45060' BQT_v3_pages.txt; echo \"=== pdf tag ===\"; awk 'NR<=45028 && /\\[pdf page/{t=$0} END{print t}' BQT_v3_pages.txt",
 "description": "Read BQT vol3 gostāx entry"
}
```


### [2026-09-14T02:37:39.218Z] TOOL RESULT

```
‎. ‏رفیدی‎ : Af . ‏ورك :کرف‎ GF GS: AF
. ‏اول ) . ۰ رل : کساردن‎ en) ‏مسحف «کرم»‎ - 6
. ‏تلفظی د رگذاردن . ۸ - اسم فاعل مرخم‎ - ۷

‎٩‏ - اندهگار من شد وانده بمنگذاشت وامق چه کرد درم ‎pie‏ من‌آ نکنم.
خاقانی شروالی .
*۶- از :کسار (هم.)۲-دن ( پوند مصدری ) . ۱ باين معتی شاهدی ماد
‎ashes Cs‏ . رک ‎AG:‏ ,کشارده . ‎rb‏ باده ‎LS‏ غمگسار ‎awe cid.‏
رز" اس مقعول ازه کساردن» (هم):
سافیا مر مرا ازآن ‎gt‏ ده که غم من ازو کسارده شد. . ابوشکور بلخی هرشیدی» .
‎Ida -۴‏ دورخ نو بس خویست ۰ از چه با بار کارکست کنی ؟
ار مروزی « لفت فرس ۳۷ *.
۵ گزدم - رك :کم .
[pdf page 613]
‎Clea”‏ ۱ » بنم اول ؛ بروزن وممنی
بستاج است که ‎ge‏ ادب و دلی و تند باشد ۴ .

‏گستاخ دست «کنابه از چابدست
وجلد و تندکار کننده باشد ۴ .

‏گستر ۴ = ‎ee‏ اول‌بروزن دختی؛بمعنی
پهن‌کننده و افرازنده باشد ‎٩‏ - و امرباین‌معنی
هم‌هت عنی پهن کن و بیفراز و ‎Merged‏
‏میاه وخار سفید را نیز گوبند .

‎Vo pal?‏ © فتح دال و سکون‌تون,
بععني پهن ‎OS‏ و فرو چیدن و فراز کردن
باشد .

‏گسترش ۷ ۰ بنم ارل و سکون آخر

‏که شین نقطه‌دار باشد , هرچیز راکه توان فرو

‎NAN

‏چید ‎oS uy‏ از دام وباط و فرش ۸ وامثال
آن

‏کته ‎٩‏ » بفتح اول‌بروزن ‎austen‏
‏مر کین باشد که فلا اسب و استر و خر وکاو
است .

‎Cire ‏نم اول و قتج‌ها‎ 5 re
‏محترم ۰ نام پسس نوذرین منوچهر است - و دام‎
‏پ سگژدهم نیز هست و او یکی ازپهلوانان‌ایران‎
MY ‏بود‎

‏گحتی ۰۱۳ بنتح اول بر وزن پستی »
بمعتی درشتی وزبولی و ازیبابی باشد ۶.۱۳

=== pdf tag ===
[pdf page 613]
```


## [2026-09-14T02:37:55.430Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; awk 'BEGIN{RS=\"\\f\"} /\\[pdf page 613\\]/{print}' BQT_v3_pages.txt | tail -30",
 "description": "Read footnotes of BQT vol3 pdf page 613"
}
```


### [2026-09-14T02:37:56.474Z] TOOL RESULT

```
«ممزی ‎Sayles‏ ص 44۲ *.
8 - اسم فاعل مرخم :داد کستر»

‏باستان ‎Startvi‏ ( پهن کردن ) . پهلوی ‎Vilstartan‏ ( پپن کردن ) « اسعق ۰۹۲۱ .
۷ - از : کستر (ه.م.) بش ( پسوند اسم مصدر ) .

‏۸ - بار کاهی بدو نمود بلند

‏کسترشهای بارگاه پسند .
نظامی کنجوی ۶ سروری * .

‎٩‏ - از گت (هم.) ۰-۳( ود سبت ) منوب بچیزی زشت «رشیدی» « فرهنکه

‎© ells

‏. *- در پهلوی ‎Vistaxm‏ با ‎Vistahm‏ , این نام در اوستا بقول دارستتر
بصورت ۷15480۳0 آمده که یکی از ناموران ابراست ازخاندان نوذر ( بتد؟۱۰ فروردینبشت).

‏این کلمة اوستابی ‎gine Bd‏ کشوده و منتشر شده میباشد « پررداود . بستها ج ۱ س 15۵ ح ©
و کرستنسن ليز برین عقیده است * کیانیان س ۱۵ > بتابرین ‎sisting‏ اوستابی تبدیل صورت
‎al‏ وستهم = کستهم گردیده که جزو اخیرآن « تهم » یمعنی دلیر است «یشتها ج ۰۱۳۹
‎A,‏ : فهرست ولف . ۱ رك : فبرست ولف . ۴ از : کت (هم.)+دی
‎dele)‏ مسدر ؛ اسم معنی ) -
۴- ترا جائیست بس عالی و تورانی چو یرون رفتی از جای بدی نکتی:
‎nt?‏ خروبلخی ص ۸۷۳ *.
‎٩ ۱‏ گستی - ‎pe‏ اول ‎Lape) Ss‏ مر کزی) یاقتح دوم وفتح چپارم. از ‎Sey‏ اوستایی
‎chide _ Sui =sid‏ < پارسی باستان ۷15۳20 «هوبشمان۹۲۲». پپلوی ‎vG@)sastan‏
‏رک : استق۲۲٩‏ ؛ دارستتر . تیمات ‎AEN‏ قطع ‎WS‏ بربدن » جداکردن — منقطم کشتن ,
پارمشدن شکته شدن - رها شدن ‎By.‏ گلیدن .
```


## [2026-09-14T02:38:05.423Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; awk 'BEGIN{RS=\"\\f\"} /\\[pdf page 69[01]\\]/{print substr($0,1,3000)}' BQT_v3_pages.txt",
 "description": "Read BQT vol3 pdf pages 690-691"
}
```


### [2026-09-14T02:38:06.495Z] TOOL RESULT

```
[pdf page 690]
os -۱۸۳-

لخلخهای ‎GS pi‏ ۰ بمنی درم
لخلخه باشد که کوبی است از ‎pte‏ و مشك‌وغیره
ترتیب داده شده ۴ - و کنابه از ساعات شب هم

‎lod‏ ۱ = با خای نقطه‌دار بروزن
دغدفه » ترکیبی باشد کهآنرا بجهت تقویت‌دماغ
ترتیب دهند - و گوی عنبری باشد که از عود

‏قماری و لادن و ‎Clee‏ وکافور سازند. ‎oe‏ .3

‏بیان هشتم

‏درلام با رای قرشت مشتمل برسه لغت

‎che J‏ اولوسکون ‎At‏ بممنی‌جوی | و بچة گوسفند را نیز گویند ‎٩‏ - و نام شهری

‏باشد اعم از آنکه آنرا سیلاب کنده باشد بسا
آدمی؟ = و پسنی بل و بخ ‎“SET aie‏ گر ك « بفتح اول بروزن فرد » میدان!

‏وضعیف ولاغررانیز گویند؟ - ویضم اول,طایفه‌ای @ بفتح ‎Jal‏ بروزن فرد + میدان‌اسب

‏باشد از صحراتشینان ‎٩‏ و مردم قهستان -وبممنی | دواتیرا گوبند - ونام میدانی هم‌هست در هرموز

‏که بلرد ‎jal‏ اشتهار دارد ‎HR‏

‏هم هست کهآترا لور خوانند ۷ .

‏کام وتوان و مراد و مطلب هم‌آمده است - وبره

‏۱ -(عر) خلطی ‎col‏ مرکب از مشك و ‎pte‏ و کافور و نظایر ‎OT‏ « الجماهر بیرولی
ص ۲۳۵ > . رك : ح۲ .

‏۴ - غالیه‌سای آسمان سود برآتشین صدف از ‎ATS pag‏ لشلخه‌های عنبری.
خاقالی شروانی « لفت نامه >.
۴ - لری کندند ناهموار در پیش که باد ازوی ‎wT‏ در اتك خویش.

‏امیرخرو دهلوی « جهانگیری »

‏۴ - در اراك ( سلطان آباد ) 87| ( لاغر . مخصوصاً بگوسفندهای لاغر اطلاق شود )
مکی نژاد ۰ . © ‎osm‏ طابفه‌ای چادر نشین ازایلهای ابران که در کوهستانهای‌جنوب
غربی ابران سکونت دارند . مبنای عمده‌ای که موجب شده چهارشعبة مهم: مسنی , کوهگیلوبی»
بختیاری واران ( خاس ) را تحت نام «لر» جمع کنند » مبنای زبانشناسی است ( چنانکه در ‎Bal‏
‏کردان نیز همین عمل شدء ) . لهجةٌ لری از شمب مهم لهجه‌های ‎shal‏ است و دارای ادیباقی
‎cul‏ . رك : داثرقالمعارف اسلام. -رك : ‎te‏ ۷ مراد لرستان )4.2( است.
رك : معج‌البلدان ۲

‎۰ ‏پابان کتاب‎ Bae old : ‏رك‎  هوردل‎ Oo

‎pe - ole DO‏ اول وکسر دوم ( نیزیفتح دوم ) از : لر(ه.م.) ج-ستان (یسوسعان)؛
‎clot‏ از شمال
[pdf page 691]
۱۸۵4 wos
. ‏لرلر ۱ « پفتح دو لام و سکون دو را | یکی ازدامهای خدای تعالی است جل‌جلاله‎

بیان نهم
در لام با زای نقطه ‎hy‏ مشتمل پر دو ‎cal‏

. ‏اول بروزن هجوم » کباده بمعتی لازم شدن باشد‎ ene PIP
‏بر وزن وزیر » بمعنی هوشمتد‎ = Pp ‏راکوبند وآن‌کمان نرمی باشد که کمانداران‎
‏بدان مش قکمان کشیدن کنند ۴ - و در عربی | وعاقل ودانا و بزرکک وپرهیز کار باشد.‎

بیان دهم

در لام با زای فارسی مشتمل بر دو لفت

‎ce =o FOZ‏ اول و ثالی و سکون‌ميم» ‎ne FOB‏ وزن ومعنی لجن است که
کل و لای تیره و ‎le‏ را کویند که درته‌حوضها | کل سیاء ته حوضها و ‎GY‏ بن تالابها باشد #
و بن تلبهامیباشد وآنرا لجن هم میگوبند.

‎Nee )۱(‏ : با زای تازی .
۱ - این پیت عنصری بلخی را شاهدآ ورده‌اند :

‏بقرزانگی ساب اضرش همیخواست از حضرت لرلرش.
و ظاهراً این صورت مصحف «کر کر» است « لغت نامه > ‎Ay‏ :گ رگر .
۴ - ای ببازوی قوت تو شد» مر فلك را کمان کمان لزیم .

‏سوزنی سمرقندی « انتدراج > .
۴ سح لیم « لجن = ۴ ح لجن ‏ لجم « لژم .
* لرز - بفتح اول . در اوراق مانوی ( پهلوی ) ۲۳2 ( لرزیدن از تب) ‎(Henning,‏
‎A list of Middle Persian ..., 505 , IX, 1, p . 87)‏ -کردی ‎larz‏ (ب)
«ژابا ی ۳۷۸ » ؛ جنبش با حرکات کوچکه غیر منظم و ارتماش ‎ry‏ لرزیدن .
۰ 0 لریدی - بفتح اول و.پنجم » از : لرز (ه.م.)+-یدن ( پسوند مصدری ) ؛ جنبیدن
و مرتض شدن با حرکات کوچك ‎pb‏ متظم ؛ طییدن .
لست ‎oll Bam old Jd)‏ کتاب .
```


## [2026-09-14T02:38:11.869Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; awk 'BEGIN{RS=\"\\f\"} /\\[pdf page 692\\]/{print substr($0,1,3500)}' BQT_v3_pages.txt",
 "description": "Read BQT vol3 pdf page 692 (printed 1895)"
}
```


### [2026-09-14T02:38:12.936Z] TOOL RESULT

```
[pdf page 692]
بیان بازدهم

در لام با شین قرش مشتمل بر شش لغت
شش ۳۹ ‎pe‏ اول وسکون ثانی,مخقف لك ۴ & بفتح اول وسکون انی‌وکاف»
لوش است که لجن باشد و آن کل و لايه نيد" | پمعنی پاره باشد که لك ‎LS‏ بسنی پاره پاره -
و ماه است که در ته تالابها و بن حوضها بهم و بمعنی شبتم هم‌آمده است و ‎OT‏ رطوبتی باشد

‎aa‏ حواکه ی ز زه نشیند و مانند
‎S55 5 Prt}‏ . در برروی ژمین و سبزه نشیند و
ن = بفتح اول بروزن ‎ES‏ » بمعنی ف زمین را سفید کند ۵ ؛ و باين ‎gine‏ یک
تماشا وتفرج باش - ویک ‎san Syl‏ لیسیدن برف رمین را : و بای هی بر

‏بعنی زبان برچیزی مالیدن ۴ . او ‎Ht ele‏

‏۸ سح لوش : 1
صاف باشد زلال دولت تو تبره شد آب دشمتانت ز لش .
‎cle on‏ جامی > جهالگیری * .

‏۴ - لش بفتح اول لاش ۳ لاشه بمعنی جیفه » مردار ؛ جسد پیروح - کشته و پوست
‎WT‏ و کوسفند وامثالآن - سخت بکاره » تثبل - بیمار » بی‌فیرت « لفت نامه » .

‏۴ 27 لیشتن * لبیدن . از رس پارسی باستان ‎olishtanaiy « liz‏ = فارسی‌لشتن
زمان ‎laizdmiy Je‏ ۵ فارسی 162810 5 ( نظیر نوشتن : ‎(ays‏ 163810 پدید آمده
«هوبشمان ۹۵5 , پهلوی ‎lishtan‏ , 1)(5420 , ارمنی ‎lixam,;, . lizum , lizem‏
رك : اسشق ‎Sef‏ . در اراك ( سلطانآباد ) ‎leshtan‏ > مکی‌نژاد » :

‏لعتند آستانت بزرگان ومپتران چون بوز پیراشته ‎Ly‏ نیر .
سوزنی سمرفندی « جپانگیری >

‎ae ۴‏ (هم) 9 - ظ , مصحف > بشکه » (ه.م.) یشک .

‎sae‏ - بقتح اول وسوم , معرب‌آن عسکر « داثرةالمعارف امیلام *قلعه » از اينکه تشک
به + عسکر» تعریب شده بعضی حدس زده‌اند که « ش » اصلی نیست . عسکی عربی در حفبقت از
کلمه‌ای ‎olaskar ost‏ با ‎cashkar‏ ناشی شده. انجمن آرای ناصری لشکر را از « لشکه ©
( قطمه , باره ) تاثی میداند , ولی با این وجه موجب پیدایش حرف آخر نامسلوم است
‎Fremdworter , ۲۰ 70, note ۱‏ ,510101 ) فول هدایت براساسی مبتنی نست*لفت
نامه».آقای پورداود احتمال میدهند که اين کلمه از اوستابی ۲265/01۳2 ویهلوی27 2۳41511
(رزمی , سپاهی ) (رك : ص ‎٩۷‏ ح ه ) ناشی شده . بدین ‎amy‏ رشتر ‏ رشتر = اشتر . اما
تبدیل آشتر به لشکر بمید ‎alee‏ ؛ کردی ع 1651061۳ ( قشون ) « ژابا ص ‎٩۳۷۹‏ ؛ مجموعاً
سپاهیان . خیل , قشون :
‎dal le‏ و رای و دانش فزون به از لک ‎AF‏ بی رهنمون .
ایوشکور بلخی « لفت نامه * .
- در اصطلاح نظام کنونی يك لشکر مر کب ازچند ( معمولا چهار ) هنك ( فوج ) است -
```


## [2026-09-14T02:38:27.493Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"العسكر\\|عسكر\" ARB_mo3rb.txt | head -10; echo \"=== abdulraheem ===\"; grep -n \"عسكر\" ARB_abdulraheem.txt | head -10",
 "description": "Grep al-Jawaliqi for ʿaskar"
}
```


### [2026-09-14T02:38:27.564Z] TOOL RESULT

```
10309:وهو تابعى ثقسة ٠‏ قال أبو أحمد العسكرى : د كان صاحب راي على" يوم صفين » ثم ولاه اصطخر » 5 
17003:نت 7 عسكر مم 5 سم بأد معروتف ل قال الأزهرى 5 وكاله 
17013:(0) فى نا« وهى > ٠‏ وهو خطأ ٠‏ 09 عبارة المهرة ( ؟ 1مة) : ه والعسكر 
17015:لان در يد رأيان ٠‏ والظاهى أن الكلمة عرربية ٠‏ قال ابن الأعر الى : « العسكر : الكثير من كل شىء: 
17018:(0) هذاغير جيد . فكلية ”عسكر'' الراخ أنها عر بية» و ””مكرم'' بشم اليم وسكون الكاقف 
18244:سوه كر وعسكر ١‏ 3 ّّ - رار 
=== abdulraheem ===
```


## [2026-09-14T02:38:29.821Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '16995,17025p' ARB_mo3rb.txt",
 "description": "Read al-Jawaliqi ʿaskar entry"
}
```


### [2026-09-14T02:38:29.872Z] TOOL RESULT

```
١ ١ ع 9 - مت يع 7 2 5 كر اعرسم‎ 
قال أبن دريد و‎ ٠١ فارسى معرب‎ ٠ 8 قال اءن قنبية : 4 العسر‎ 
رو لك)‎ 
53 هو ليش » بالفارسية ه وهو مجتمع اميش‎ 
26) 


5 مه سار تم وس و 5 5 5 2 0 
نت 7 عسكر مم 5 سم بأد معروتف ل قال الأزهرى 5 وكاله 


صرب ٠:‏ 
)١( :‏ ف اللسان : «وعزير امم يتصرف فته و إن كان أعميا » مثل نوح ولوط » ٠‏ وقالالإهام 
أبو البقاء المكبرى المتوق سنة 1 فى كاب إعراب القسرآن ( ؟ ؛: 7 ) : < لا يتصرف للعجمة 
ا » وهذا ضعيف» لأن الأهم عر عند أ كثر الناس » ٠‏ وقرأ عاصم والكسانى و يعقوب 
ل بالتنوين فالآب ٠‏ ادن سو رة التوية على أن ا لأسم على 6 وقرأ أ باقى الأر بعة عشر يدون تنو ين > 
وأختلف فى توحبه يما إعلم من كتب القراءات والتفسير» (١‏ الواو لم تذكر قى بف : 

(0) فى نا« وهى > ٠‏ وهو خطأ ٠‏ 09 عبارة المهرة ( ؟ 1مة) : ه والعسكر 
قاربى معرب »> !ما هوش » وهو ]آتفاق فى اللقتين » ٠‏ ولعل صوابه «أو هو اتقاق» فيُكون 
لان در يد رأيان ٠‏ والظاهى أن الكلمة عرربية ٠‏ قال ابن الأعر الى : « العسكر : الكثير من كل شىء: 
يقال : عسك من رجال » وخيل » وكلاب » ٠‏ وانظر المادةٌ فى اللسان ٠‏ 

(0) هذاغير جيد . فكلية ”عسكر'' الراخ أنها عر بية» و ””مكرم'' بشم اليم وسكون الكاقف 
وفتح الراء س هوكم بن مءزاء » أحد بنى جعونة بن الحرث » صاحب اجاج بن يوسف » أزل هذا 
الموضع , يتواحى بو زستان »6 وكانت هناك قرءة قدعة »© فيناها » رم ب زل لي ينيك ؟ وي جملها مدينة » 


قمياها اسك م ل الاسم كله شي خالص 9
```


## [2026-09-14T02:38:40.333Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SYN p1376 (leaf1b 1401) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==1401 {print substr($0,1,1200)}' SYN.txt; echo; echo \"=== AVG p237 (leaf1b 292) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==292 {print substr($0,1,1200)}' AVG.txt",
 "description": "Print Buck p.1376 and Jackson p.237"
}
```


### [2026-09-14T02:38:41.374Z] TOOL RESULT

```
=== SYN p1376 (leaf1b 1401) ===
rtly Subordinate to city, the technical dis- tinction showing wide local variation (in US., especially New England, according to the form of local government). Cf.
NED s.vv. city and town. The nearest parallel is in Latin, where oppidum is occasionally applied, like urbs, to cities like Rome or Athens, but mostly to other towns.
In general, terms for ‘town’ as inter- mediate between ‘city’ and ‘village’ are not included in the list, e.g. Fr. bourg,
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
1308 SELECTED INDO-EUROPEAN SYNONYMS
NHG hkleinstadt, Grk. xapn, xwudmrors, etc. Here belongs NG pop. xw#pa (used for the chief town of a district or island; as ‘town’ in Const. Porph.) with peculiar development of x#pa ‘country, place’ or perhaps re-formed (or reinterpreted) as augmentative of xwplov, NG xwpro ‘vil- lage’ (Kretschmer, KZ 39.554 ff.).
Many of the words denoted first an “nclosed and fortified place’. Several are specializations of ‘place’ or ‘dwelling- place’, and one group is narrowed from ‘state’.
1. Grk. ré\ts (in early use partly = dxpérons ‘citadel’) : Skt

=== AVG p237 (leaf1b 292) ===
'ri)  =  Skt.  -van,  (f.  -vari\  Whitney,  §  1 234. §  855.     A  few  secondary  derivatives    are   made  with the  suffix  -van.    They  show  also  a  corresponding  feminine -valri.     Examples  are:
Av.  ajavan-  adj.  m.,  afava'ri-  (beside  afaont-)  adj.  f.  'righteous* =  Skt.  ftavan-  (f.  -vart);  Av.  apravan-  m.  'priest'  =  Skt.  dtharv an-; Av.  hapto.karjyan-  n.  'seven  karshvars",  Av.  haptd.karj>vairi-  'belong- ing to  the  seven  karshvars'.
29.  Av.  -vana  =  Skt.  -vana  (Whitney,  §   1245  1). §  856.     This   suffix   arises   apparently    by    transfer   of  the  preceding -van  to  the  a-inflection.    It  bears  also  a  relation  to  -var  §  337.    It  is  to be  recognized  in  a  couple  of  instances :    Av.  Sfrivana-  n.  'blessing' ;   Av. panvana-  m.  'bow' ;  Av.  hapravana-  adj.  'splendid'.
30.  Av.  -vant  =  Skt.  -vant  (Whitney,  §  1233). §  857.  The  suffix  -vatit  is  closely  akin  to  the  suffix -man.t,  and  like  the  latter  it  is  used  in  making  a  large number  of  possessive  adjectives  from  nouns.  The  suffix -vatit  is  used  with  a-,  i-  and  consonant  stems,  -maqt  being employ
```


## [2026-09-14T02:38:55.947Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"raoae\\|raöae\\|rad.ae\\|rathae\\|Krieger\\|warrior\" AVG.txt | head -15; echo \"=== SYN leaf 1469 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==1469 {print substr($0,1,800)}' SYN.txt",
 "description": "Search Jackson for raθaēštā and print Buck leaf 1469"
}
```


### [2026-09-14T02:38:57.021Z] TOOL RESULT

```
653:Av.  aetaf  'this'  =  Skt.  etdt;  GAv.  vaedd,  YAv. vaeda  'knows*  =  Skt.  v£da.  —  A.v.frae<jye*ti  'he  drives forth*  (fra  -f-  w-^  =  Skt.  presyati.  —  Av.  duraedars 'far-seeing'  (loc.  du*re)=Skt.  dure.dfs-;  Av.  rapaestd- rtm  'warrior  in  chariot*  =  Skt.  rathe$thdm  (loc.  rdthe}.
1526:§  249.  Declension  of  Av.  ra^agjftS-  m.  'warrior  standing  in  chariot' =  Skt.  rathgf(hd-  (part  of  its  forms,  however,  are  from  the  stem  rapai$tar-t cf.  Skt.  savylf(hdr-). — The  forms  from  radical  rafae-ft&-  are:  —  Singular. Nom.  rafagjft<B;  Ace.  rapagitqm;  Dat.  rapoiSte  (cf.  Skt.  dhiyq-dht,  and  on oi  cf.  §  56),  rapalilSi  (a-decl.,  cf.  Skt.  rathlfthdyd);  Gen.  rapae$t&. — Plural.  Ace.  rapalSt&s-cH.
2020:§  330.  (ii)  Declension  of  Av.  rapaestar-  'warrior  stand- ing in  charriot'.  —  This  word  shows  also  a  parallel  stem rapaestd  according  to  the  radical  «-decl.,  see  §  249.  The forms  from  stem  rapaestar-  are: —
4789:Av.  vispa'ti  (subst.  -f-  subst.)  m.  'lord  of  the  clan'  =  Skt.  vispdti-; Av.  dar'ja.l>azu-  (adj.  -j-  subst.)  adj.  'longimanus'  =  Skt.  dirgha- liahu-;  Av.  wspo.bamya-  (adj.  -\-  adj.)  adj.  'all-shining';  Av.  kvaspa- (indecl.  -J-  subst.)  adj.  'well-horsed'  =  Skt.  svahia-;  Av.  rafaelta-, rapaeitar-  (subst.  -j-  rad.)  m.  'warrior  standing  in  chariot'  =  Skt. ratheffhd- ;  Av.  nidasnaipiH-  (rad.  -f-  subst.)  adj.  'having  weapons laid  down';  Av.  star'to.bar'sman-  (ptcpl.  -j-  subst.)  adj.  'with  out- spread barsom'.  Likewise  some  other  combinations.
4833:a.  Accusative  (especially  before  radical  finals).  Av.  ahtim.- mfr'w-  'destroying  the  soul',  ahmaoja-  'confounding  righteousness' (ahm  maoja,  m  -J-  m  =  m,  §  1 86),  ahumbiS-  'healing  the  soul', daeum.jan-  'daeva-smiting'.  —  b.  Dative.  Av.  yavae-jt-  'living  for ever'.  —  c.  Genitive.  Av.  z'mascipra-  'having  the  seed  of  earth'. —  d.  Locative.  Av.  duraedars-  'seeing  at  a  distance',  rafiaeSta-, rapailtar-  'warrior  standing  in  a  chariot1  (rapt-),  ma'dyoi.pa'tiitSna- 'to  the  middle  of  the  breast'.
4857:1.  Noun  value  (Whitney,  §   1264):    Accusative  relation.    Av. mipro.druj-  m.  'one   that   breaks  his  pledge".  —  Gen.  relation.    Av. •vispani-  m.  'lord    of  the    clan'.  —  Loc.   relation.     Av.  rafiaiita-  m. 'warrior  standing  in  a  chariot'  (rape  =  actual  loc.,  cf.  §  877).
=== SYN leaf 1469 ===
put, Lat. putidus ‘stinking’) Gamillscheg 726, Bloch 2.195.
Fr. courtesane (> NE courtesan), orig. ‘woman of the court’, in present sense since 16th cent. Wartburg 2.851. NED 8.V. courtesan.
Sp. ramera, Port. ramiera, fem. to
ramero, ramiero ‘young bird of prey’, lit. ‘little branch’, fr. ramo ‘branch’ (fr. Lat. ramus id.). REW 7035.
Rum. curvd, fr. Slavic (below, 6).
3. Ir. merirech, NIr. méirdreach, fr. Lat. meretriz (above, 2). Vendryes, De hib. voc. 155.
Ir. stripach, NIr. striopach, fr. Lat. stuprum ‘dishonor, disgrace, debauchery’ (with metathesis, cf. NE strumpet, be- low). Vendryes, De. hib .voc. 180.
W. putain, prob. fr. ME putaine (rather than directly fr. Fr. putain). Parry-Williams 173.
Br. gast = W. gast ‘bitch’, etym.? Loth, RC 36.166 (vs. Morris
```


## [2026-09-14T02:39:14.919Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for L in 1467 1468 1469 1470; do echo \"=== leaf1b $L head ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$L\"' {print substr($0,1,200)}' SYN.txt; awk 'BEGIN{RS=\"\\f\"} NR=='\"$L\"' {print}' SYN.txt | grep -oE \"1[0-9]{3} [A-Z]{3,}|SELECTED INDO-EUROPEAN SYNONYMS\" | head -3; done",
 "description": "Find Buck printed page numbers near leaf 1469"
}
```


### [2026-09-14T02:39:16.039Z] TOOL RESULT

```
=== leaf1b 1467 head ===
rike’, teagmhaim ‘happen’, etc.
W. cyfarfod, cpd. of cyf- ‘together’, ar ‘on, upon’, and bod ‘be’.
Br. en em gavout, refl. of kavout ‘find’ (11.32).
4. Goth. gamétjan, ON meta, 
=== leaf1b 1468 head ===
x, scortum, Dan. hore, sk¢ge ChSl. ljubodéica, bladtnica lupa, prostitita Sw. hora, skéka SCr.  bludnica, kurva
It. pullana, meretrice, OE miltestre, hore Boh.  kurva, nevéstka prostituta ME hore,
1368 SELECTED
=== leaf1b 1469 head ===
put, Lat. putidus ‘stinking’) Gamillscheg 726, Bloch 2.195.
Fr. courtesane (> NE courtesan), orig. ‘woman of the court’, in present sense since 16th cent. Wartburg 2.851. NED 8.V. courtesan.
S
=== leaf1b 1470 head ===
phrase with ljuby ‘love’ and déjati ‘put, perform’. Berneker 756.
ChSl. bladinica (Supr. for zéprn), SCr. bludnica, Russ. bljudnica, deriv. of ChSl. blqdti ‘ropveta, fornication’, blqdit
```


## [2026-09-14T02:39:22.795Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"137[0-9] SELECTED\\|SYNONYMS 137[0-9]\" SYN.txt | head; echo \"=== awk leaf ===\"; awk 'BEGIN{RS=\"\\f\"} /137[5-7] SELECTED|SYNONYMS 137[5-7]/ {print \"leaf1b=\"NR\": \"substr($0,1,1500)}' SYN.txt | head -40",
 "description": "Locate Buck printed page 1376"
}
```


### [2026-09-14T02:39:23.934Z] TOOL RESULT

```
34366:1372 SELECTED INDO-EUROPEAN SYNONYMS
34421:1374 SELECTED INDO-EUROPEAN SYNONYMS 20.138 WAR
34457:1376 SELECTED INDO-EUROPEAN SYNONYMS
34492:1378 SELECTED INDO-EUROPEAN SYNONYMS
=== awk leaf ===
leaf1b=1476: 20.15).
6. Chl. brant (reg. for wédenos in Gospels) : brati ‘fight’ (20.11). Berne- ker 74,
‘battle’
Digitized by Arya Samaj Foundation Chennai and eGangotri
WARFARE
1375
ChSl. ratt (Supr. freq., sometimes ‘battle’ but mostly = wédeuos), SCr. rat (Russ. rat’ formerly used for ‘army’ and ‘war’) : ChSl. ett ‘strife, emulation’, retiti ‘contend’ : Skt. r- ‘rise, move’, Grk. prune ‘stir up, rouse’, etc. Cf. Skt. rana-, etc. battle’ (20.13), fr. the same root. Walde-P. 1.139.
SCr. Russ. vojna, Pol. wojna (Boh. vojna now mostly in phrases like ‘call to war’, ie. to military service), beside ChSI. vojint (pl. voji) ‘soldier, warrior : Lith. veju, vyfi ‘pursue, chase’, Skt. veti ‘pursues, strives after, drives, etc.’, Av. vayeiti ‘pursues’, etc. Walde-P. 1.230. Briickner 629.
Boh. vdlka (Pol. walka ‘fight, combat, struggle’, WhRuss. valka ‘battle, wood- cutting’) : Boh. vdleti ‘make war’, OPruss. alint ‘fight’, OE wel ‘battle- field, corpses of the slain’, ON valr ‘bodies of the slain’, OHG wuol ‘defeat, ruin, plague’, etc. Walde-P. 1.304f. Otherwise Briickner 599 (: ChSl. valztz, Lat. volvere ‘turn’, etc.).
7. Skt. vigraha- ‘strife’, sometimes ‘war’, fr. vi-grabh- ‘stretch apart, sepa- rate, divide’, and also ‘fight, wage war’.
But in general for Indo-Iran., see words listed under ‘battle’.
20.132. ‘Enemy’ in war. Asnotedin 19.52, most of the words for personal ‘enem
```


## [2026-09-14T02:39:29.152Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '34440,34500p' SYN.txt",
 "description": "Read Buck p.1375-1377"
}
```


### [2026-09-14T02:39:29.210Z] TOOL RESULT

```
OE orlege, OS orlag, orlogi, MLG or- loge, orloch, Du. oorlog, OAG urliugi, MHG urliuge, perh. as ‘situation lacking oaths’ (of peace) : Goth. liuga ‘mar- riage’, Ir. Luige, W. lu ‘oath’, but in part confused with the Gme. group for ‘fate’, OE orleg, OS orlag, OHG orlac, etc. (fr. *legh- ‘lie’). Walde-P. 2.415, 425. Franck-v. W. 477. Falk-Torp 801.
Late OE wyrre, werre, ME werre, NE war, fr. Northeastern OFr. werre = Central OFr., NFr. guerre (above, 2). NED s.v.
Du. krijg, NHG krieg, but MLG krich (> Dan., Sw. krig) mostly ‘strife’, MHG kriec mostly ‘exertion, opposition, en- mity’, etc., less often ‘war’, OHG krig ‘stubbornness, defiance’ (cf. vb. NHG kriegen ‘get’, orig. ‘strive’, 11.16), prob. : Ir. brig ‘strength, worth’, Grk. vfpis ‘violence’, Bprapés ‘firm, strong’. Walde- P. 1.686. Falk-Torp 579. Weigand-H. 1.1151. Franck-v. W. 349 f.
5. Lith. karas, karé, Lett. kar’ : Lith. karias, OPruss. kragis (= kargis) ‘army’, Goth. harjis ‘army’, etc. (20.15).
6. Chl. brant (reg. for wédenos in Gospels) : brati ‘fight’ (20.11). Berne- ker 74,
‘battle’
Digitized by Arya Samaj Foundation Chennai and eGangotri
WARFARE
1375
ChSl. ratt (Supr. freq., sometimes ‘battle’ but mostly = wédeuos), SCr. rat (Russ. rat’ formerly used for ‘army’ and ‘war’) : ChSl. ett ‘strife, emulation’, retiti ‘contend’ : Skt. r- ‘rise, move’, Grk. prune ‘stir up, rouse’, etc. Cf. Skt. rana-, etc. battle’ (20.13), fr. the same root. Walde-P. 1.139.
SCr. Russ. vojna, Pol. wojna (Boh. vojna now mostly in phrases like ‘call to war’, ie. to military service), beside ChSI. vojint (pl. voji) ‘soldier, warrior : Lith. veju, vyfi ‘pursue, chase’, Skt. veti ‘pursues, strives after, drives, etc.’, Av. vayeiti ‘pursues’, etc. Walde-P. 1.230. Briickner 629.
Boh. vdlka (Pol. walka ‘fight, combat, struggle’, WhRuss. valka ‘battle, wood- cutting’) : Boh. vdleti ‘make war’, OPruss. alint ‘fight’, OE wel ‘battle- field, corpses of the slain’, ON valr ‘bodies of the slain’, OHG wuol ‘defeat, ruin, plague’, etc. Walde-P. 1.304f. Otherwise Briickner 599 (: ChSl. valztz, Lat. volvere ‘turn’, etc.).
7. Skt. vigraha- ‘strife’, sometimes ‘war’, fr. vi-grabh- ‘stretch apart, sepa- rate, divide’, and also ‘fight, wage war’.
But in general for Indo-Iran., see words listed under ‘battle’.
20.132. ‘Enemy’ in war. Asnotedin 19.52, most of the words for personal ‘enemy’ (vs. friend’) cover the ‘enemy’ in war, but in some languages certain words are preferred in the latter sense. Thus Grk. wodéutoe vs. éxOpoi, Lat. hosts (orig. ‘stranger’, 19.55) vs. tnimicus, Russ. neprijatel’ vs. vrag.
CC-O. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
1376 SELECTED INDO-EUROPEAN SYNONYMS
20.14 PEACE
c Goth. gawairpi Lith. tatka a ae ON fridr Lett. miers Lat. pax Dan. fred ChSl. mirit It. pace Sw. fred ’ SCr. mir Fr paix OE sib(b), frip Boh. mir P Sp. paz ME pais, frith Pol. pokéj Rum. pace NE peace Russ. mir : Ir. std Du. vrede Skt. samdhi- NIr. _ stothchdin OHG  fridu, sibba Av. Gxsti- W. heddwch MHG vride Br. peoc’h NHG friede
Words for ‘peace’ are based on such notions as ‘stable condition, quiet’, ‘friendship’, ‘kinship’ and ‘agreement’. Brugmann, Ber. Sichs. Ges. 1916. no. 3.
1. Grk. elpnyn (dial. tpdva, etc.), etym.? Brugmann, op. cit. (fr. the root of dpapicxw ‘fit, join’). Kretschmer, Glotta 10.238. Debrunner, Gétt. Gel. Anz. 1916.741 (pre-Greek origin).
2. Lat. pax (> Romance words), fr. *pak- beside *pag- in pangere ‘fasten, fix, join together’, Grk. miyvixe ‘fix, drive in’, etc. Walde-P. 2.2. Ernout-M. 720.
3. Ir. sid, sith, NIr. stothchain (cpd. with cain ‘law, rule’), fr. *sédo-, beside W. hedd (poet.), deriv. heddwch, Corn. hedh, fr. *sedo-, both prob. as orig. ‘stable condition’ fr. *sed- ‘sit’. Stokes 297 f. Loth, RC 36.162. Otherwise Walde-P. 2.462 (with refs.).
W. (obs.) tanc, tangnef, tangnefedd (cf. Tancoriz, etc.), prob. : OE panc ‘satisfaction, pleasure’, etc. Loth, RC 41,225.
Br. peoc’h, fr. Lat. pax. Loth, Mots lat. 194.
4. Goth. gawairpi, cf. OHG grwurt ‘liking’, prob. fr. the root of Goth. wairpan ‘become’, with development through ‘coming together, agreement’. Brugmann, op. cit. 13. Feist 209. Otherwise (: wairh ‘value, worth’) Schrader, Reallex. 1.650 and others (refs. in Feist).
ON fridr, OE frib, OHG Sridu, etc., general Gme. (Goth. only in the name
Fripa-reiks) : Goth. frijin, OE Sréon ‘love’, Goth. frijonds, OE fréond ‘friend’, Skt. pri- ‘please’, priya- ‘dear’, etc. Walde-P. 2.87. Falk-Torp 271 f.
OE sib(b), OHG sibba (reg. for paz in Tat.), properly ‘kinship, kin’ (2.81, 19.23), whence ‘peace’ as the normal condition among kin.
5. Lith. taika (neolog. in place of pakajus, formerly the usual word, fr. Pol. pok6j) : tike ‘fit, suit, agree’, taikyti ‘mediate’, tatkus ‘suitable, peaceful’, pa- taika ‘idleness’ (Walde-P. 1.725, Leskien, Ablaut 287, etc.).
OLith. mieras, Lett. miers = ChSI. mirt (below, 6).
6. ChSl. mir (also secondarily ‘world’, 1.1), SCr., Russ. mir, Boh. mir (Pol. mir, mostly replaced by pokéy), r-formation fr. the same root as ChSl. mili ‘pitiful’, Russ. mil ‘dear’, Lith. mielas ‘dear’, myléti ‘love’, Lat. mitis ‘mild, gentle’, etc. Walde-P. 2.244 Berneker 2.60 f.
Pol. pokéj = Boh. pokoj ‘quiet, rest, room’, Russ. pokoj ‘rest’ : ChSl. pokojt ‘rest’, po-kojiti ‘calm, put at rest’, po-citi ‘rest’, etc. Berneker 538 f.
7. Skt. samdhi-, lit. ‘putting together, union, conjunction’, whence ‘accord compact, peace’ : sam-dhd- ‘put to- gether’.
Av. dzéti-, NPers. agti, prob. : a (x)Sta- in caus. ‘put in place, appoint’, epd. of sta- (xsta-) ‘stand’. Brugmann, op. cit. 11. Barth. 311, 1602.
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
WARFARE 1377 20.15 ARMY Grk. orparés, orparevpa Goth. harjis Lith. kariuomene (karias, NG otparés (Byz. ON herr armija) goooGrov) Dan. her, armé Lett. kar’§ (kar’a spéks) Lat.  exercitus Sw. har, armé ChSl.  vojt It. esercito, armata OE here, fierd SCr.  vojska, armija Tr. armée ME (h)oste, here, ferd Boh.  vojsko, armdda Sp. ejército NE army Pol. wojsko, armia Rum. armatd, ostire (oaste) Du. __ heer, leger Russ. armija (vojsko) Ir. sliag OHG heri Skt.  sena- Nir. arm, sluagh MHG her(e) y Av. haéna-, spada- W. byddin (lu) NHG heer, armee OPers. kdra-, haina-
Br. arme(ad)
Words for ‘army’ are based upon such notions as ‘armed’ (force), ‘train- ing’ (> ‘military training, trained force’), ‘enemy’ (‘hostile army’ > ‘army’), ‘expedition’ (> ‘military ex- pedition’ > ‘army’), ‘camp’ (through ‘military camp’), and ‘missile’ (?). Several of the words, including a con- siderable cognate group, are used also in part for ‘people, crowd’, which may well be secondary (as in NE host), but the development ‘people’ > ‘people in arms, army’ is also possible. The French armée has been extensively bor- rowed all over Europe.
1. IE *kor- in words for ‘war’, ‘army’, and ‘people, crowd’. Walde-P. 1.462 f. Feist 247.
Here as ‘army’ Goth. harjis, ON herr, etc., general Gme.; Lith. (karias, ka- rauna) kariuomené (now the preferred form; cf. NSB s.v. armija), Lett. kar’s (also ‘war’, hence for ‘army’ esp. kar’a spéks, with spéks ‘strength, might’ also sometimes alone ‘army’), OPruss. kragis (= kargis); OPers. kara- (also ‘people, nation’), NPers. kar-zar ‘battle-field’ (Barth. 465); cf. Ir. cure ‘crowd, band’, Grk. kolpavos (*képravos) ‘ruler, leader’.
2. Grk. orparés, in form = Skt. sirta- ‘spread out, extended’, vbl. adj. fr. the root *ster- ‘spread out’ in Grk. orépvupt, Skt. sir-, Lat. sternere, etc. Develop- ment through ‘crowd, people’ (attested in Pind., Aesch., etc., and cf. Cret. orap-
76s @ division of the people); or through ‘camp, encamped army’ (cf. orparézedov, Byz. ¢ooc&rov, Du. leger)? Hence also orparia ‘army’ and vb. ozparebw ‘serve as soldier, campaign’, orpa7evpa ‘army’, orpatirns ‘soldier’, orpardéredov ‘camp’, sometimes ‘army’. Walde-P. 2.638 f. Boisacq 918.
Byz. ¢oscarov ‘camp’ and pop. word for ‘army’, fr. late Lat. fossdtum ‘ditch’ (: fossdre, fodere ‘dig’). Hence also OSp. fousado, OPort. fossado, Prov. fosat ‘army’ (REW 3461). Develop- ment through ‘moat’ > ‘camp’ (pro- vided with a moat) > ‘army’.
3. Lat. exercitus (> It. esercito, Sp. ejército, both lit. words in orig.), orig. ‘training’, abstract of exercére ‘pursue, practice, exercise’ (cpd. of arcére ‘in- close, confine, hold off’), hence esp. ‘military training’ and in concrete sense ‘body of trained men, army’. Ernout- M. 67 f.
Lat. hostis ‘enemy’ (orig. ‘stranger’ 19.55) was used in MLat. for ‘military service, army’ (whence Rum. oaste, and the older Romance terms Olt. oste, OF r. ost, Sp. huesta, Port. hoste, all obs. ex- cept Rum. oaste, and for this now pop. ostire, prop. ‘campaign’, fr. the deriv. vb. ostt ‘go to war’, and in lit. armatd; cf. Tiktin 1068, 1098). Although the direct transition ‘hostile army’ to ‘army’ in general is, of course, possible, the more likely development was through use in
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
a ns - 2
d Digitized by Arya Samaj Foundation Chennai and eGangotri
‘ q
1378 SELECTED INDO-EUROPEAN SYNONYMS
such phrases as convenire in hostem, exire in hostem, etc., where in hostem meant orig. ‘against the enemy’ but was easily construed ‘into military service’ and consequently ‘into the army’. Buck, Cl. Ph. 14.12f. Diez 229. REW 4201.
MLat. armata ‘armed force’, either land force or more commonly naval force (cf. Du Cange), fr. fem. sg. of Lat. armaius (pple. of armdre ‘provide with arms’, fr. arma ‘arms, weapons’, 20.21), and prob. abstracted fr. armdata classis (cf. classis, 20.16). Hence It. armata used of either ‘army’ or ‘fleet’, Sp., Port. armada ‘fleet’, Fr. armée ‘army’ (> Dan., Sw. armé, NHG armee, SCr., Russ. armija, etc.; Russ. > Lith. ar- mija); Rum. armaidé (neolog.). Also OFr. > ME armie, NE army, but the early use was ‘armed expedition’ or ‘armed force’, either of sea or of land, sometimes ‘fleet’, and only later restricted to a land force (NED s.v. army).
4. Ir. sliiag ‘host, troop, army’, NIr. sluagh (now as ‘army’ mostly replaced by arm, fr. NE army), W. Ulu (mostly ‘host’), OCorn. luw : ChSl. sluga ‘ser- vant’ (orig. coll. ‘body of servants, house- hold’, as in Ir. teglach, W. teulu ‘family’, epds. with Ir. tech, W. ty ‘house’). Walde-P. 2.716. Pedersen 1.84.
W. byddin, in MW ‘troop’ : Ir. buden ‘troop, band, quantity’, etym. dub. Pedersen 1.363, 2.59. Thurneysen, Kel- torom. 91.
Br. arme, fr. Fr. armée (above, 3).
5. Goth. harjis, etc., above, 1.
Dan., Sw. armé, NE army, NHG armee, fr. Fr. armée (above, 3).
OE fierd (ferd, fyrd), ME ferd, orig ‘expedition’ : OHG fart, ON ferd ‘jour- ney’, etc., OE, OHG faran, ON fara ‘travel’, etc. NED s.v. ferd.
```


## [2026-09-14T02:39:49.304Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /rafaelta-, rapaeitar-|rafaelta-/ {print \"leaf1b=\"NR}' AVG.txt; awk 'BEGIN{RS=\"\\f\"} NR>=290 && NR<=294 {print \"leaf1b=\"NR\" :: \"substr($0,1,80)}' AVG.txt; echo \"=== which leaf has line 4789 ===\"; awk 'NR==4789{print}' AVG.txt | head -c 200; echo; awk 'BEGIN{RS=\"\\f\"} {n++; if (index($0,\"(subst.  -j-  rad.)\")) print \"leaf1b=\"n}' AVG.txt",
 "description": "Locate Jackson's compound section leaf"
}
```


### [2026-09-14T02:39:50.447Z] TOOL RESULT

```
leaf1b=293
leaf1b=290 ::  Adjective.  Av. aptma-  'last'  =  Skt.  apamd- ;  Av.  upama-  'highest'  =  S
leaf1b=291 :: v.  afyrya-  m.  'pupil' ;  Av.  n&vhaipya-  n.  nomen  propr. , cf.  Skt.  nasa
leaf1b=292 :: 'ri)  =  Skt.  -van,  (f.  -vari\  Whitney,  §  1 234. §  855.     A  few  sec
leaf1b=293 :: e  MSS.  and  each is  followed  by  a  point,  the  compounds  are  not  always
leaf1b=294 :: Ys.  53.3,  Afr.  1.8,  Vd.  22.13;  so  Av.  u^tyaojana-  beside  »»'// aojan
=== which leaf has line 4789 ===
Av.  vispa'ti  (subst.  -f-  subst.)  m.  'lord  of  the  clan'  =  Skt.  vispdti-; Av.  dar'ja.l>azu-  (adj.  -j-  subst.)  adj.  'longimanus'  =  Skt.  dirgha- liahu-;  Av.  wspo.bamya-  (adj.  -\- 
leaf1b=293
```


## [2026-09-14T02:39:57.500Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for L in 916 917 918; do echo \"=== LEW_1910 leaf1b $L ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$L\"' {print substr($0,1,350)}' LEW_1910.txt; done; echo \"=== rota in LEW ===\"; grep -n \"^rota\" LEW_1910.txt | head -3",
 "description": "Check Walde Latin p.904"
}
```


### [2026-09-14T02:39:58.576Z] TOOL RESULT

```
=== LEW_1910 leaf1b 916 ===
=== LEW_1910 leaf1b 917 ===
=== LEW_1910 leaf1b 918 ===
=== rota in LEW ===
8832:rota II 440
14059:rota II 224, 757
```


## [2026-09-14T02:40:02.511Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; tr -cd '\\f' < LEW_1910.txt | wc -c; wc -l LEW_1910.txt; sed -n '8828,8836p' LEW_1910.txt",
 "description": "Check LEW file size and rota context"
}
```


### [2026-09-14T02:40:03.581Z] TOOL RESULT

```
305
14865 LEW_1910.txt
romr II 421
ropa I 418
rostenn II 447
rot II 415
rota II 440
rogg II 453
rok II 440
roskr II 444
rost II 419
```


## [2026-09-14T02:40:11.919Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==1 {print substr($0,1,300)}' LEW_1910.txt; echo \"...\"; awk 'BEGIN{RS=\"\\f\"} NR==150 {print substr($0,1,300)}' LEW_1910.txt",
 "description": "Inspect LEW_1910 content"
}
```


### [2026-09-14T02:40:13.075Z] TOOL RESULT

```
...

ing I 47
tot (akymr.) I 734
tow (akymr.) I 728
wr, yr ,aer~ TT 207.
wr, orun, IT 397
ws (mkymr.) J 686, II 294
asel I 686
ahr (akymr.) I 708
wud- [725
Iudnerth (akymr.) 1725
~iwng 1728
wwreh I 650 lain I 757 lann I 755 laun (akymr.) I 322 lenn (akymr.) IT 239 Letewic (akymr.) I 815 liaus (akymr.) I
```


## [2026-09-14T02:40:18.541Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for f in MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt; do echo \"### $f\"; grep -c \"ارتشتار\" $f 2>/dev/null; grep -n \"ارتشتار\" $f 2>/dev/null | head -3; done",
 "description": "Grep Mo'in for arteštār"
}
```


### [2026-09-14T02:40:19.813Z] TOOL RESULT

```
### MON_part1.txt
1
9487:دار تشد ن:) بکار میرفت با ارتشتاران را 
### MON_part2.txt
1
6533:ارتشتاران فر مانده. امبرء بادشاه. 
### incoming/MON/MON_2vol_Adena_v1_djvu.txt
1
9487:دار تشد ن:) بکار میرفت با ارتشتاران را
```


## [2026-09-14T02:40:22.288Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '9480,9495p' MON_part1.txt; echo \"-----\"; sed -n '6525,6540p' MON_part2.txt",
 "description": "Read Mo'in arteštār contexts"
}
```


### [2026-09-14T02:40:22.374Z] TOOL RESULT

```
نظامی یکث کشور (فره.) ضح.- این کلمه 
بدین صورت اصالت ندارد و بصورت 
نادرستی از لغت بهلوی رار تیشتر و معنی آن 
لفظاً یه گر دونه استاده» و توسعاً جنگاوری 
که با گر دونه به کارزار می‌رود» می‌باشده 
استخراج شده است و درست آن بود که 
«ار تشتار» به معنی مفرد (و جمع آن 
دار تشد ن:) بکار میرفت با ارتشتاران را 
بصورت اسم جمع بکار مسی‌بردند. 
(هر مزدنامه ص ۵ ۲۷.) 

ارتشاء: ۰+۹3 [ع. ف. ارتشا] (مسص م.) 
رشوه ستدن؛ رشوت ستاندن» رشوه گرفتن» 
رشوه خوردن. 


-----


فرمانده: ۲-1 [- فرمان دهنده ]| ((ص‌فا.) 


آنکه فرمان دهدء کسی که حکم کند. (نظ.) 
صاحب‌منصی که به واحدی از سربازان 
ریاست کند. فرمانده کل قوی: بزرگ 
ارتشتاران فر مانده. امبرء بادشاه. 
فرماندهی: -1ع0-] (حامص.) عمل و 
شغل ف مانده» حکومت؛ امارت» امبری. 
رباست واحدی از سربازان. 

فرمان رسیدد: هل آد(۲:)۵-] (مص‌ل.) 
ابلاغ حکم از طرف بزرگی به کوچکتر. 
(مج.) رسیدن اجل مقدر.
```


## [2026-09-14T02:40:39.143Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n\"https://en.wiktionary.org/wiki/%D8%A7%D8%B3%D8%AA%D8%A7%D8%AF\" \\\n\"https://en.wiktionary.org/wiki/%D8%B3%D8%AA%D9%85\" \\\n\"https://en.wiktionary.org/wiki/%DA%AF%D8%B3%D8%AA%D8%A7%D8%AE\" \\\n\"https://en.wiktionary.org/wiki/%D9%84%D8%B4%DA%A9%D8%B1\" \\\n\"https://en.wiktionary.org/wiki/%D8%AA%D8%A7%D8%A8%D8%B3%D8%AA%D8%A7%D9%86\" \\\n\"https://en.wiktionary.org/wiki/-%D8%B3%D8%AA%D8%A7%D9%86\" \\\n\"https://en.wiktionary.org/wiki/%D9%BE%D8%B1%D8%B3%D8%AA%DB%8C%D8%AF%D9%86\" \\\n\"https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%B3%D8%AA%D8%A7%D8%AF%D9%86\" \\\n; do python3 tools/fetch_source.py \"$u\" --note \"page 474, root Stâ/Stha/Stâk, node verification\" 2>&1 | tail -1; done",
 "description": "Archive Wiktionary pages batch 2"
}
```


### [2026-09-14T02:40:48.174Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/f78c380685162cdb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/84852bdc866a16b4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b226b9b9c3100465.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cb5d281da757664f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cf34416257ab50ca.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b470cdbcbf21b179.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/28a491a0bc765fa7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/150c50cf9889428b.txt
```


## [2026-09-14T02:40:51.326Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in f78c380685162cdb 84852bdc866a16b4 b226b9b9c3100465 cb5d281da757664f cf34416257ab50ca b470cdbcbf21b179 28a491a0bc765fa7 150c50cf9889428b; do echo \"######## $f\"; awk '/^ Etymology$/{c++} c>=1' $f.txt | sed -n '1,12p'; done",
 "description": "Extract etymologies from batch 2"
}
```


### [2026-09-14T02:40:52.318Z] TOOL RESULT

```
######## f78c380685162cdb
 Etymology
 [ edit ] 

 From earlier Classical Persian اُوسْتَاد ( ūstād ) , from Middle Persian [Book Pahlavi needed] ( ʾwstʾt' ) , 𐫀𐫇𐫏𐫘𐫤𐫀𐫅 ( ʾwystʾd /⁠awestād⁠/ , “ master, craftsman ” ) , from Proto-Iranian *Hawastātas (compare Avestan 𐬀𐬎𐬎𐬀𐬯𐬙𐬁𐬙𐬀 ( auuastāta ) , Northern Kurdish hoste , oste , wista , wusta , وەستا ( westa ) , Mazanderani استات ( estât ) , استا ( estâ ) , اسا ( essâ ) ), verbal noun of Proto-Iranian *HawastaHyáti (compare Old Persian 𐎠𐎺𐎠𐎿𐎫𐎠𐎹𐎶 ( a-v-a-s-t-a-y-m /⁠avāstāyam⁠/ ) , Avestan 𐬀𐬎𐬎𐬀𐬯𐬙𐬀𐬌𐬌𐬀 ( auuastaiia ) ), from *Hawa- ( compare Avestan 𐬀𐬎𐬎𐬀 ( auua ) ) +‎ *staHyáti , from Proto-Indo-Iranian *Háwa + *staHyáti , the latter from Proto-Indo-European *stoh₂éyeti ( “ to cause to stand ” ) . [ 1 ] 

 Cognate with Sanskrit अवस्था ( avasthā ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ʔus.ˈtaːd/ 

######## 84852bdc866a16b4
 Etymology
 [ edit ] 

 Borrowed from Classical Persian ستم ( sitam , “ tyranny ” ) .

 Pronunciation
 [ edit ] 

 ( Standard Urdu ) IPA ( key ) : /sɪ.t̪əm/ 

 Noun
 [ edit ] 
######## b226b9b9c3100465
 Etymology
 [ edit ] 

 From Middle Persian wstʾhw' ( wistāx , “ confident, bold ” ) , from wistāxw , from Old Persian *vistāhuva- . Akin to Old Armenian վստահ ( vstah ) , an Iranian borrowing.

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ɡus.ˈtaːx/ 

 ( Dari, formal ) IPA ( key ) : [ɡʊs.t̪ʰɑ́ːx] 

######## cb5d281da757664f
 Etymology
 [ edit ] 

 Etymology tree

 Proto-Indo-European *h₂lek- 

 Proto-Indo-European *-seti 

 Proto-Indo-European *h₂lékseti 
 Proto-Indo-Iranian *Hrákšati 

######## cf34416257ab50ca
 Etymology
 [ edit ] 

 Inherited from Middle Persian 𐭲𐭠𐭯𐭮𐭲𐭠𐭭 ( tʾpstʾn /⁠tābestān⁠/ ) . By surface analysis , تاب ( tâb , “ heat ” ) +‎ ـستان ( estân ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /taː.bis.ˈtaːn/ 

 ( Dari, formal ) IPA ( key ) : [t̪ʰɑː.bɪs.t̪ʰɑ́ːn] 

######## b470cdbcbf21b179
######## 28a491a0bc765fa7
 Etymology
 [ edit ] 

 Inherited from Middle Persian plstytn' ( paristīdan , “ to serve; to worship; to minister in a ritual ” ) , from Proto-Iranian *pari- ( “ around, peri- ” ) + *staH- ( “ to place, set, stand ” ) . The former prefix is from Proto-Indo-Iranian *pári , from Proto-Indo-European *péri , and the latter is from Proto-Indo-Iranian *stáH- , from Proto-Indo-European *steh₂- ( “ to stand ” ) .

 Related to Old Armenian պաշտեմ ( paštem ) , an Iranian borrowing.

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /pa.ras.tiː.ˈdan/ 

######## 150c50cf9889428b
 Etymology
 [ edit ] 

 From Middle Persian [script needed] ( plyst-ʾtn' /⁠frēstādan⁠/ ) , which seems to be a compound. If so, the elements are most likely from " fra- " and " sta- ". For the first element see " for- ". For the second element see ایستادن .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /fi.ris.taː.ˈdan/ 

 ( Dari, formal ) IPA ( key ) : [fɪ.ɾɪs.t̪ʰɑː.d̪án]
```


## [2026-09-14T02:41:07.064Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo \"=== LASHKAR ===\"; grep -n -B2 -A25 \"Proto-Indo-Iranian \\*Hrákšati\" cb5d281da757664f.txt | head -60",
 "description": "Read Wiktionary laškar etymology"
}
```


### [2026-09-14T02:41:07.129Z] TOOL RESULT

```
=== LASHKAR ===
190-
191- Proto-Indo-European *h₂lékseti 
192: Proto-Indo-Iranian *Hrákšati 
193-
194- Proto-Iranian *karah 
195-
196- Middle Persian lškl 
197- Persian لشکر 
198-
199: Inherited from Middle Persian lškl , from Proto-Indo-Iranian *Hrákšati + Proto-Iranian *karah . Compare Sanskrit रक्षति ( rakṣati ) .
200-
201- Pronunciation
202- [ edit ] 
203-
204- ( Classical Persian ) IPA ( key ) : /laʃ.ˈkar/ 
205-
206- ( Dari, formal ) IPA ( key ) : [läʃ.kʰäɾ] 
207-
208- ( Dari, formal ) IPA ( key ) : [läʃ.kʰäɾ] 
209- ( Kabuli ) IPA ( key ) : [läʃ.kʰäɾ] 
210-
211- ( Hazaragi ) IPA ( key ) : [läʃ.kʰäɾ] 
212-
213- ( Iran, formal ) IPA ( key ) : [læʃ.kʰʲæɹ] 
214-
215- ( Tajik, formal ) IPA ( key ) : [läʃ.kʰäɾ] 
216-
217- Rhymes: -ar 
218-
219- Readings
220-
221- Classical reading ? 
222-
223- laškar
224-
--
392-
393- Proto-Indo-European *h₂lékseti 
394: Proto-Indo-Iranian *Hrákšati 
395-
396- Proto-Iranian *karah 
397-
398- Middle Persian lškl 
399- Classical Persian لَشْکَر ( laškar ) bor. 
400- Urdu لشکر 
401-
402- Borrowed from Classical Persian لَشْکَر ( laškar ) .
403-
404- Pronunciation
405- [ edit ] 
406-
407- ( Standard Urdu ) IPA ( key ) : /ləʃ.kəɾ/ 
408-
409- Noun
410- [ edit ] 
411-
412- لَشْکَر • ( laśkar )  m ( Hindi spelling लश्कर ) 
413-
414- army , armed force , military 
415- Synonyms: فوج ( foj ) , آرمی ( ārmī )
```


## [2026-09-14T02:41:16.742Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; grep -n -A6 \"Middle Persian\" 84852bdc866a16b4.txt | head -40; echo \"=== sotorg / setāk ===\"; cd /home/sfmqrb/git/rishe; for u in \"https://en.wiktionary.org/wiki/%D8%B3%D8%AA%D8%B1%DA%AF\" \"https://en.wiktionary.org/wiki/%D8%A2%D8%B3%D8%AA%D8%A7%D9%86\" \"https://en.wiktionary.org/wiki/Bisotun\" \"https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D8%AA%D8%B4\"; do python3 tools/fetch_source.py \"$u\" --note \"page 474, root Stâ, node verification\" 2>&1|tail -1; done",
 "description": "Check setam Persian and fetch more pages"
}
```


### [2026-09-14T02:41:20.499Z] TOOL RESULT

```
=== sotorg / setāk ===
/home/sfmqrb/git/rishe/data/verification/sources/web/fb5136c50e101304.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/59cd75b5aa8c0819.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9c39d6f1195b45c1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/92fc0f40a56a67cb.txt
```


## [2026-09-14T02:41:23.818Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in fb5136c50e101304 59cd75b5aa8c0819 9c39d6f1195b45c1 92fc0f40a56a67cb; do echo \"######## $f\"; awk '/^ Etymology$/{c++} c>=1' $f.txt | sed -n '1,10p'; done; echo \"=== setam persian ===\"; grep -n \"Persian\" 84852bdc866a16b4.txt | head -20",
 "description": "Read etymologies batch 3"
}
```


### [2026-09-14T02:41:24.998Z] TOOL RESULT

```
######## fb5136c50e101304
 Etymology
 [ edit ] 

 From Middle Persian [Book Pahlavi needed] ( stwlg /⁠sturg⁠/ ) , from Proto-Iranian *stūrakah . Cognate to Bactrian στοργο ( storgo , “ mighty, strong, great ” ) . Minus one stem extension from pairing with the equivalent of بزرگ ( bozorg ) (like Proto-Slavic *čeršьňa ( “ sweet cherry ” ) from alignment with *višьňa ( “ sour cherry ” ) ) cognate to Sanskrit स्थूर ( sthūra , “ bulky, massive ” ) . In equivalent meaning with different root extension also in Ossetian стыр ( styr , “ large, great ” ) , Pashto ستر ( stër ) , and Sanskrit स्थिर ( sthira , “ firm ” ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /su.ˈturɡ/ , /si.ˈturɡ/ , /sa.ˈturɡ/ 

######## 59cd75b5aa8c0819
######## 9c39d6f1195b45c1
 Etymology
 [ edit ] 

 From Persian بیستون ( bisotun ) .

 Proper noun
 [ edit ] 

 Bisotun 

######## 92fc0f40a56a67cb
 Etymology
 [ edit ] 

 Rebracketing of ارتیشدار ( “ soldier, horseman ” ) analyzed as having the component ـدار ( -dâr , “ haver ” ) , introduced during the Reza Shah regime's Persianization program.

 Displaced Persian قشون ( qošun ) and displaced Persian اردو ( ordu ) , Mongolic and Turkic borrowings.

 Pronunciation
 [ edit ] 

=== setam persian ===
57: Persian 
59: Toggle Persian subsection 
153: Persian
159: ( Classical Persian ) IPA ( key ) : /si.ˈtam/ 
217: Borrowed from Classical Persian ستم ( sitam , “ tyranny ” ) .
235: Categories : Persian terms with IPA pronunciation 
236: Rhymes:Persian/am 
237: Rhymes:Persian/am/2 syllables 
238: Persian lemmas 
239: Persian nouns 
240: Urdu terms borrowed from Classical Persian 
241: Urdu terms derived from Classical Persian
```


## [2026-09-14T02:41:36.722Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D8%B3%D8%AA%D9%88%D9%86\" --note \"page 474, node 2, Bagastana>Bisotun\" 2>&1|tail -1; cd data/verification/sources/refs/incoming/ARY; for w in \"ستون\" \"ایستادن\" \"استاد\" \"لشکر\" \"تابستان\" \"پشت\" \"آشتی\" \"سترگ\"; do echo \"### $w\"; grep -n \"$w\" ARY_pages.txt | head -2; done",
 "description": "Fetch Bisotun and grep Aryanpur"
}
```


### [2026-09-14T02:41:38.996Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/66cb409cd3b28795.txt
### ستون
2450:معنی این واژه در برخی زبان‌های هند و اروپایی امروزین: تبره ستون» دسته) ساقه شاخه.
4987:چم این واژه در اوستایی و سانسکریت: ستون» پایه» نگهدار,
### ایستادن
2476:۱-اين واژه یا واژه‌های "استاک" و "ایستادن" همریشه است. ار
2480:۴ ۳016013۷ برای واژه‌های این فهرست دو واجریشه را می‌دهد یکی 978* , ۱۰۱۹(978) به معنی "ایستادن"
### استاد
1192:استادان ایرانی نیز (به ویژه معین و خانلری و پورداود) با بهره گیری از پژوهشهای برونمرزیان امن ۱
### لشکر
### تابستان
4034:چم این واژه در زبان‌های لیترانی و لنرنی: تابستان, 6 ۴
5874:۲ اين واجريیشه در واژه‌های "تابستان" و *تابخانه" و اوه" و "تون تاب" (و غیره) هم دیده می‌شود.
### پشت
245:سارماتی * سغدی * خوازمی + فارسی > پشتو + زبانهای هندوستان شمالی. جهت این موج‌های
320:این ريشه در زبانهای مختلف دارای معنی « کوه» يا «تپه؛ و یا «پشته» و يا «انباشته) هستند.
### آشتی
### سترگ
10342:چم اين واژه در سانسکریت: قری و سترگك.
```


## [2026-09-14T02:41:42.605Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; sed -n '2440,2490p' ARY_pages.txt; echo \"=== pdf tag ===\"; awk 'NR<=2476 && /\\[pdf page/{t=$0;l=NR} END{print t\" at line \"l}' ARY_pages.txt",
 "description": "Read Aryanpur entry on istādan/estāk"
}
```


### [2026-09-14T02:41:43.740Z] TOOL RESULT

```
لانین (4770ا): 57001018 ,8ت 871013 آلبانی (۵2اامقلم: 5177517
ایسلند یکهن (4۸ 560/010۸۷ 0ت0):
بل872 ,۰871609 [ پسگلت‌ها 35
فریزی کهن (۷لفاول۲ ام 978 0 ات20
آلمانی کهن (/05801۸ 271014 صان): 7 (6ت57۸) ات اسان ات
87۸3 1 (857۸7) 010/5
آلمانی (0570/۸/۷): این 6 (ت57۸) :37
انگلیسی کهن (#لولا5۸0 صات): بشآ878 برهان قاطع + ۱.۹۷۴
تابل۸ 57
بادداشت:
معنی این واژه در برخی زبان‌های هند و اروپایی امروزین: تبره ستون» دسته) ساقه شاخه.
8 اوستايی (۷ل۸۷87۸): 7۸ پونانی (076210): 05
َ پارسی باستان ((287314 00): 57۸۸۸ لاتین (70م): ۲اتااناق57۸ ,8تا1.00
پهلری (۷1ا۸7): ۸0 ,)51۸ فرانسه (۳6/614): 81۸86
سانسکریت (7ل5۸۸/58)بدش 8771۸ ,8771۸ آسپانیایی (8۸/184): ریز اند
ال نان ایتالیایی (4ا14): ات57۸
ارمنی (/5781۸1:0480120114 ب[978 )57۸ رومانی (۸(/1(7لاتا): بآل57۸
[pdf page 86]
لگ یی
ا
استخر(نام شهری در استان فارسی به چم "مستحکم») / ۸۷ ۱
ْ
گرتبک (007[410): 3 ان لهستانی (ط5/-۳0): هتشاد
ایسلند یکهن (010/1۸۷/ی5 صان): روسی (8/5514(۷): زد ان
57۸ ساق57۸ چکد (250(4): 51۸7
آلمانی کهن (/027۵4۸ بزهابز صا0): صربی (۷ل5581۸4): 357۸۸
87۸3 برهمی (8048211۸01): ماد
آلمانی (058//۸00): 578780 مال87۸ لنونی (لنی) (771۸۸7)ما): ات87۸
انگلیسی کهن (لل5لاه8۸ ط0): «بلف578 برتونی (878670/۷): 87۸01
ال اند آلبانی (7لهالمقلم: 51۸
انگلیسی (لل5اا6۸0): 87۸
دانمارکی (0۸(7824): 0 ,57۸7.0 پسگشت‌ها 05
سوئدی (8218(0((): 575۸ نان رس ۱
نروژی (۸/0719509). 87۸ 10-151 ماه
هلدی (00703): 857۸ برهان قاطم + ۱۰۹۷-7۴
۱ بادداشت:
۱-اين واژه یا واژه‌های "استاک" و "ایستادن" همریشه است. ار
۲- معطی این واژه در برخی زبان‌های هند و اروپایی: اسطبل» محل نگهداری دام. :
۳- واژه‌ی فارسی "اسطبل" از واژه‌ی لاتین 57۸811181 آمده د این واژه‌ی لانین خود یا واژه‌های اوستایی
۸ (حل نگهدار ی اسب‌ها) و 06۸۷0-57۸۷۸ (محل نگهداری گاوها) از یک ريشه است.
۴ ۳016013۷ برای واژه‌های این فهرست دو واجریشه را می‌دهد یکی 978* , ۱۰۱۹(978) به معنی "ایستادن"
و فرار گرفتن" و دبگری 818۳ (۱۰۱۹) به معنی "ایستاندن" و ار دادن", 8
ه-واژه‌ی انگلیسی 0 عم از همین ریشه‌ی -871* یا 87۸۰* آمده است.
4+ چم انگلیسی سرواژه‌ی فارسی:,577۸08013010 ,(3۸5 18 ۲07۷ ۸ 08 01۸168) 357۸6118
2 9 دا
اوستایی (لل۸725374): 51۸38۸۰ ,87۸3۳1۸۰ آلمانی کهن (058/۸2 ۲/0 صا0):
سانسکریت (54۸/88/7): 57۸7 ,7 )57۸ تفتت۸ 57
ایسلندی‌کهن (7 هش صضا0). ۰ آلمانی (085/۸). 857۸7۲
572 انگلیسی کهن 20/05 00 بکل75د
ساکسونی کهن (/5420 صا0): 575813 8 ان
سس
=== pdf tag ===
[pdf page 86] at line 2457
```


## [2026-09-14T02:42:24.849Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; grep -n -i -A6 \"Persian\" 59cd75b5aa8c0819.txt | sed -n '1,60p' | head -50; echo \"=== bisotun ===\"; awk '/^ Etymology$/{c++} c>=1' 66cb409cd3b28795.txt | sed -n '1,10p'",
 "description": "Check āstān and Bisotun etymologies"
}
```


### [2026-09-14T02:42:25.945Z] TOOL RESULT

```
=== bisotun ===
 Etymology
 [ edit ] 

 Inherited from Old Persian *Bagastānah . Doublet of فغستان ( faġistān  / faġestân , “ temple ” ) .

 By folk etymology, بی ( bē  / bi , “ without, -less ” ) +‎ ستون ( sutūn  / sotun , “ pillar ” ) , referring to its ancient reliefs which are carved directly into the rock without pillars.

 Pronunciation
 [ edit ]
```


## [2026-09-14T02:42:30.414Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; grep -n \"Middle Persian\\|Etymology\" 59cd75b5aa8c0819.txt | head -10; sed -n '140,175p' 59cd75b5aa8c0819.txt",
 "description": "Inspect āstān page"
}
```


### [2026-09-14T02:42:30.478Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T02:42:32.678Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; wc -c 59cd75b5aa8c0819.txt; head -30 59cd75b5aa8c0819.txt",
 "description": "Inspect āstān fetch result"
}
```


### [2026-09-14T02:42:32.728Z] TOOL RESULT

```
156 59cd75b5aa8c0819.txt
URL: https://en.wiktionary.org/wiki/%D8%A2%D8%B3%D8%AA%D8%A7%D9%86
FETCHED: 2026-09-14T02:41:19Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-09-14T02:42:38.072Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -o \"āstān[a-zğīš()]*\\s*\\[[^]]*\\][^.]*\\.\" PHD.txt | head -5; echo \"---\"; grep -n \"threshold\" PHD.txt | head -5; echo \"=== NYB astan ===\"; grep -n \"āstān\\|astan \\[\" NYB_vol2_glossary.txt | head -5",
 "description": "Grep PHD/NYB for āstān threshold"
}
```


### [2026-09-14T02:42:38.187Z] TOOL RESULT

```
252:āstān [b’st?n' | M PysPn, N ~] always, often.
---
=== NYB astan ===
855:ayyastan ['dybstn'] to long for, to yearn for: i ka-t 6 včnišn 1 Ahriman . . . ayyast since thou hadst (such a) longing to see A. 76?, impers. constr., cf Lat. tibi lubuit; — [pres. ayyds- DkM 4837-8 Cod.
925:this passage is & hopeless mess (Bthl. regarded it to be the translation of Av. bàóa which has, however, another sense, v. 8. v. bāstān).
933:bastan [bstn', inser. bstny ; '"SLWN-tn'] band-, to bind (hand and foot) 32!?; to fetter 74??. 115! (be ~); to fasten 2026; asp apar rahy ~ to harness a horse to the car 5416; andar ~ (apar rahy) id. 5418-14 (gl); dar bé ~ to shut the door 7514; puhlv, vitiry ~ to construct a bridge F:1-3.6; menišn i...6...~ to fix a p.’s mind upon = to suggest to his mind to (do ...) 4021-22; ddisr i... pat ménisn be ~ to obstruct the spiritual eye (sight) of a p. 5226-27 (ef. bastišn) — Av. (926) band- = OP; MPrth bstn bnd-; MPrs bstn, subju. byn’d = bennād,
2095:*hu-vaxm [hww’hm] “of good swing", epithet of the varz ‘mace’ (v. vazr) carried by Keresāspa 100%. — Renders Av. (1832) hu-nwiata- "well swung’, epithet of the vazra- of Mithra (Yt. 65. 10132) and of the vazra- in general (Yt. 10%. 1372); < m + vaeg-, v.s. v. ?vextan. Reading hypothet- ical, no Paz. reading being known to me. I take it as *hu-vexm < "hu-vataman- from *véxtan < vaig- (q. v.), which has been largely confounded with !vextan < vaik-; *huvērm > hu-vaxm (or perhaps better *hu-vahm) cf s. v. mahmän. As to véxtan as a battle term cf 254. — As Bthl (Wb 1832) has given quite misleading information about the Phl. w. I put here the notice he quotes in its correct form. It is found in the Phl Xvaršēt ntyāyišn (= Yt 6) in Zand-i Khürtak Avistäk ed. by Dhabhar, p. 21 $ 15: ké yast Ohur- mazd % amarg api-š yast Mihr 4 fragoyot . . . (l. 14) api-§ yast vazr i *hu- vazm | pat kamär apar i dévan | i Mihr frägöyöt (e: *huvaxméh € ku bāstān eton dàret: mēnēyīhā be šavet, vināskārān pã- tifrās bē kunét, u menöyihä apäc 6 kantir äyet) ‘he who has worshipped Ohurmazd the Immortal... has (at the same time) worshipped Mihr (the god) of wide (l. 14) and he has wor- shipped: the mace of good swing on the skulls of the devs, owned by Mihr of wide pasturages (its being “‘of good swing" means that it constantly behaves in the following manner: spiritually it goes off and punishes the sinners, and spiritually it returns to the quiver [sheath?])? NP v. xub nihädah, Skr. v. su-niyukta (Dhalla, The Nyaishes, 1908, p. 50). l
2130:jastan [ystn'] jah- [yh-] to jump, to leap, 1. in the proper sense 321°: hàn i hac pad 4 man be jast that which jumped up from my foot, explained by the following har cē-š patköft all that was hit by it. — 2. fig. to arise, to happen 12. 6911, 1127. — Paz. NP jastan jah-.
```


## [2026-09-14T02:42:45.145Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"āstānag\\|?st?nk\\|astanag\" PHD.txt | head -3; grep -n \"āstānak\\|astänak\" NYB_vol2_glossary.txt | head -3; echo \"=== MON astan ===\"; grep -n \"آستانه\" MON_part1.txt | head -3",
 "description": "Look for MP āstānag"
}
```


### [2026-09-14T02:42:45.236Z] TOOL RESULT

```
=== MON astan ===
3133:استان: (- آستانه ] (۱.) قسمت پیشین 
3134:اطاق متصل به در درگاه؛ آستانه» جناب؛ 
12915:آستانه» آستان‌در.
```


## [2026-09-14T02:43:01.982Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== AHD ===\"; grep -n \"^stā-\" AHD_watkins1985.txt | head -3; grep -n -A6 \"^stā-\" AHD_watkins1985.txt | head -25; echo \"=== IEC ===\"; grep -n \"^stā-\\|^staio\\|^stāio\" IEC.txt | head -5",
 "description": "Grep Watkins and Mann for the root"
}
```


### [2026-09-14T02:43:02.074Z] TOOL RESULT

```
=== AHD ===
=== IEC ===
```


## [2026-09-14T02:43:05.723Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"stā-\\|sta-\\. To stand\\|To stand\" AHD_watkins1985.txt | head -10; echo \"=== IEC stan ===\"; grep -n \"stāno-\\|stāna\\|stūnā\\|stauro\" IEC.txt | head -8",
 "description": "Find the stand root in Watkins and Mann"
}
```


### [2026-09-14T02:43:05.804Z] TOOL RESULT

```
997:sta-. To stand; with derivatives meaning “place or thing that is standing.” Contracted from *stag-. I. Basic form *std-. 1. Extended form *stddh- in: a. Germanic *stéd- J6n- in Old English stéda, stallion, studhorse ( < “place for breeding horses”): STEED; b. Germanic *st6d6 in Old English stéd, establishment for breeding horses: sTuD2. 2. Suffixed form *std-lo- in Germanic *stdlaz in: a. Old English st6/, stool: sTooL; b. compound *faldistélaz (see pel-3). 3. Latin stdre (third person singular present subjunctive séet), to stand, with its past participle status (< “sta-to-) and derivatives statira, height, stature, and statuere, to set up, erect, cause to stand: STAGE, STANCE, STANCH, (STANCHION), (STANZA), STATOR, (STATUE), STATURE, STATUTE, STAY!, STET; ARREST, CIRCUM- STANCE, CONSTANT, CONSTITUTE, CONTRAST, (COST), DESTITUTE, DISTANT, ESTANCIA, EXTANT, INSTANT, IN- STITUTE, OBSTACLE, OBSTETRIC, (OUST), PROSTITUTE, REST?, RESTITUTE, RESTIVE, SUBSTANCE, SUBSTITUTE, SUPERSTITION. 4. Suffixed form *std-men- in Latin std- men, thread of the warp (a technical term): STAMEN, STAMMEL. 5. Suffixed form *std-mon- in Greek stémén, thread: PENSTEMON. 6. Suffixed form “s¢d-ro- in Russian staryi, old (“long-standing”): STARETS. II. Zero-grade form *st- (before consonants). 1. Nasalized extended form *sfa-n-t- in Germanic *standan in: a. Old English standan, to stand: STAND; b. Old English understandan, to know, stand under (under-, under; see ndher): UN- DERSTAND; Cc. Old French estandard, rallying place: STANDARD; d. secondary zero-grade form in Germanic *stund-6 in Old English stund, a fixed time, while: STOUND. 2. Suffixed form *sé-tyo- in Germanic *stath- Jon- in Old Norse stedhi, anvil: strTHY. 3. Suffixed form *sta-tlo- in Germanic *stathlaz in Old English stathol, foundation: STADDLE, STARLING?. 4, Suffixed form *sta-mno- in Germanic *stamniz in Old English stefn, stem, tree trunk: sTeM!. 5. Suffixed form *sta-ti- in: a. Germanic *stadiz in (i) Old English stede, place: STEAD (ii) Dutch stad, place: STADHOLDER (iii) Old High Ger- man stat, place: SHTETL; b. Latin stati6, a standing still: STATION; C. Latin -stitium, a stoppage (in solstitium, solstice; see sawel-): ARMISTICE; d. Greek stasis, a standing, a standstill: sTAsIs; HYPOSTASIS, ICONOSTASIS, IsOSTASY. 6. Suffixed form *sfo-to- in Greek statos, placed, standing: STATIC, STATICE, STATO-; ASTASIA, ASTATINE. 7. Suffixed form “sta-no- in: a. Latin désti-
1001:stak-. To stand, place. Zero-grade form *stak-; extension of sta-. 1. Suffixed form *stok-o- in Germanic *staga- in: a. Old English stzg, rope used to support a mast: sTAY3; b. Old French estaie, a support: STAY?. 2. Suffixed form *stak-lo- in Germanic *stahla- in Old English stéli, style, steel (< “that which stands firm”): STEEL. [Pok. stak- 1011.]
=== IEC stan ===
17526:sthàn- (stháno; sthànos) ‘stand, set, set up, fix; standing, station, place. Cf. WP II, 606 and sthā- with extns. Verbal types: Gk. cf. histáno, v. get beside mod. sténo, v. ‘set up”; cf. -staino in kru-staíno, v. ‘turn to ice’; Lat. cf. de-stino, are ‘fix’; ob-stino, are ‘persist’; prae-stino, are ‘buy up’ (but for festino, festinus see below tuerst-); Ir. stă- naim, stán-, v. ‘stare’; W sanu, inf. ‘gaze; amaze’; cf. san, adj. ‘wide-eyed; amazed’; OCS stanọ, inf; stati & stanọti, v. stand’ and com. S1.). Nominal types: Skt. sthānam, n. “stand, station’; Av. stānō, m. ‘place, stable’; OPer. stānam, n. id.; Per. -stān, cpds. id.; Gk. cf. dústēnos, Doric: -stānos, adj. “in a bad state’; Hes. cf. bou-stáne, f. ‘cowstalľ; Oss. äston, ston, s. ‘stall, cowshed’; Tokh. A cf. stank, B: stank, s. ‘palace’; Alb. shtonë, f. “water- hole, catchment’; Ir. stán, m. “vat, barrel’; Du. steun, m. (umlaut) ‘support’; OCS stanü, m. ‘stand, camp’; Ukr. ‘state, condition’; Li. stónas, m. ‘rank, status’; stóne, f. ‘stable, stall’
17563:sthăuros (sthour-), variant of types stheuros, Stheuoros & sthauoros, q.v. General sense of ‘stiff, hard, strong, firm; stiffness’, etc: ‘stif- fening, post, hardness', etc. WP II, 608 Av. cf. staoró, m. 'draught-animal beside stavro, adj. ‘strong’; Per. cf. sutür 'farm- animal beside sitabr “thick, coarse; OPer. Pahl. ustuvar, id.; (LWs in) Arm. stuvar “thick”; astevor “certain” and stor “bottom, base'; Gk. staurós, m. ‘stake’; LLat. stauro, äre, v. ‘establish’; Lat. cf. re-stauràáre ‘restore’; Alb. shtaré, adj. ((bitter; also various bitter plants); ON staurr, m. “post, stake'; Sw. stór, m. id.; Norw. dial. staur, id.; Li. (variant) stavarys, gs: -io, m. ‘knot in wood; pith’. See next
```


## [2026-09-14T02:43:16.502Z] TOOL CALL #88: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; grep -n \"sthūnā\\|stūna\\|Säule\" WLD_Bd2_pages.txt | head -8; echo \"=== staxra ===\"; grep -n \"staxra\\|staxta\" WLD_Bd2_pages.txt | head -5",
 "description": "Grep Walde-Pokorny Bd2 for stūna/staxra"
}
```


### [2026-09-14T02:43:16.586Z] TOOL RESULT

```
=== staxra ===
40595:staxta- „fest, stark“, staxra- „stark, fest; bes. vom Winterfrost                      :   streng'' (die
40599:*staMa- wohl = av, staxra-, idg. "^sloklo (iiber air. tal „Axt'*' s. aber u. tekp-
```


## [2026-09-14T02:43:19.571Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; sed -n '40585,40605p' WLD_Bd2_pages.txt; echo \"=== pdf tag ===\"; awk 'NR<=40595 && /\\[pdf page/{t=$0} END{print t}' WLD_Bd2_pages.txt",
 "description": "Read Walde-Pokorny stāk- entry"
}
```


### [2026-09-14T02:43:20.680Z] TOOL RESULT

```
                      ,5


hausen KZ. 47, 307; andere Yersuche bei Yf. LEWb.^ s. v.)
   abg. telo „K6rper“ („*gedrungen, kompakt“??), ai. tedani „geronnenes
Bint*',    arm.     fm „Traubenkern“ (Petersson KZ. 47, 281, LUA. 1915, 18).
stak- „stehn, stellen; stehend, Stander               —
                                        aufrecht stehender Pfahl’".                                 Er-
    weiterung von sta~ „stehn‘^ Daneben *stek- (s. u.).
   Ai. sidkati „pratighate“           (Dhatup.),   d.     i.   ^widersteht,    stemmt sich“,         av.
staxta- „fest, stark“, staxra- „stark, fest; bes. vom Winterfrost                      :   streng'' (die
ar. Worte scheinen idg. '^stek-,               enthalten zu miissen); ahd. stahal n. m.
anord. stdl n. (abgeleitet       as. steldi, ags. stiele n.)         „Stahh‘    (aus       dem Germ,
stainmt apr.                   „Feuerstahh‘, s, Trautmann Apr. 389 f. rti. Lit.), germ.
*staMa- wohl = av, staxra-, idg. "^sloklo (iiber air. tal „Axt'*' s. aber u. tekp-
„zimmem“) (da auch betontes 5 nicht zu ar. a entwickelt ist, nicht          *st^k-            =
lo-; diese Gruppe riickt also im Yokal, wie in der Bed. „fest, widerstands-
kraftig^' von den flgdn. Worten ab, die allerdings sicher einer Erweiterung
zu stCi- entstammen).
   Umbr. stakaz „statutus“: lit. stokas „Pfahl“ ist Lw. aus mnd. stake; anord.
stagln. „Rad, das zur Hinrichtung dient'*, eigentlich ,,derPfahl, der es tragt‘",
=== pdf tag ===
```


## [2026-09-14T02:43:28.273Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in 9dd2e100b6c8ace7 b21d3dcfd35472dc d881b3b7e4d72c49 84852bdc866a16b4; do echo \"### $f\"; head -5 $f.txt; done",
 "description": "Check fetch statuses"
}
```


### [2026-09-14T02:43:29.357Z] TOOL RESULT

```
### 9dd2e100b6c8ace7
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/steh%E2%82%82-
FETCHED: 2026-09-14T02:33:37Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/steh₂- - Wiktionary, the free dictionary

### b21d3dcfd35472dc
URL: https://en.wiktionary.org/wiki/%D8%B3%D8%AA%D9%88%D9%86
FETCHED: 2026-09-14T02:33:39Z
STATUS: 200
TITLE: ستون - Wiktionary, the free dictionary

### d881b3b7e4d72c49
URL: https://en.wiktionary.org/wiki/%D9%BE%D8%B4%D8%AA
FETCHED: 2026-09-14T00:56:01Z
STATUS: 200
TITLE: پشت - Wiktionary, the free dictionary

### 84852bdc866a16b4
URL: https://en.wiktionary.org/wiki/%D8%B3%D8%AA%D9%85
FETCHED: 2026-09-14T02:40:43Z
STATUS: 200
TITLE: ستم - Wiktionary, the free dictionary
```


## [2026-09-14T02:43:33.273Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo \"=== PIE steh2 ===\"; grep -n -i \"to stand\\|Root\\b\" 9dd2e100b6c8ace7.txt | head -8; echo; echo \"=== sotun persian ===\"; sed -n '150,200p' b21d3dcfd35472dc.txt; echo \"=== posht persian ===\"; sed -n '/Etymology 1/,+0p' d881b3b7e4d72c49.txt; grep -n -A5 \"Middle Persian\" d881b3b7e4d72c49.txt | head -20",
 "description": "Read PIE root, sotūn, pošt entries"
}
```


### [2026-09-14T02:43:34.401Z] TOOL RESULT

```
=== PIE steh2 ===
62: Root 
139: Root
144: to stand (up)
154: Terms derived from the Proto-Indo-European root *steh₂- (185 c, 0 e) 
156: *stéh₂-t ~ *sth₂-ént ( athematic root aorist ) 
295: Northern Kurdish: westîn ( “ to be tired ” ) (> rawestîn / hilwestîn ( “ to stand ” ) , vewestîn ( “ to stop ” ) )
297: Central Kurdish: وەستان ( westan , “ to stand, wait, stop ” ) 
333: Proto-Slavic: *stavati ( “ to stand up, to become ” ) ( see there for further descendants )

=== sotun persian ===

 বাংলা 
 فارسی 
 हिन्दी 
 Magyar 
 Bahasa Indonesia 
 한국어 
 کٲشُر 
 Kurdî 
 ລາວ 
 Lietuvių 
 Malagasy 
 Nederlands 
 Polski 
 پښتو 
 Русский 
 Svenska 
 Türkçe 
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
=== posht persian ===
 Etymology 1 
 Etymology 1
```


## [2026-09-14T02:43:38.929Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo \"=== sotun etym ===\"; awk '/Persian$/{p=NR} /^ Etymology$/{c++; print \"--- Etym block at \"NR} c>0 && NR<c+0' b21d3dcfd35472dc.txt >/dev/null; grep -n \"Middle Persian\\|Proto-Iranian\\|Old Persian\" b21d3dcfd35472dc.txt | head -10; echo; echo \"=== posht ===\"; grep -n \"Proto-Iranian\\|Proto-Indo-European\\|Middle Persian\" d881b3b7e4d72c49.txt | head -10",
 "description": "Find sotūn and pošt etymology lines"
}
```


### [2026-09-14T02:43:40.094Z] TOOL RESULT

```
=== sotun etym ===
414: From Middle Persian [Book Pahlavi needed] ( stwn' ) , 𐫙𐫘𐫤𐫇𐫗 ( ʿstwn /⁠stūn⁠/ , “ column, pillar ” ) , from Old Persian 𐎿𐎬𐎢𐎴𐎠 ( stūnā , “ column, pillar ” ) , from Proto-Iranian *stuHnáH ( “ column, pillar ” ) (compare Avestan 𐬯𐬙𐬏𐬥𐬀 ( stūna ) ), from Proto-Indo-Iranian *stʰuHnáH ( “ column, pillar ” ) (compare Sanskrit स्थूणा ( sthūṇā ) ). Doublet of استوانه ( ostovâne , “ cylinder ” ) .
539: Persian terms inherited from Middle Persian 
540: Persian terms derived from Middle Persian 
541: Persian terms inherited from Old Persian 
542: Persian terms derived from Old Persian 
543: Persian terms inherited from Proto-Iranian 
544: Persian terms derived from Proto-Iranian 
567: Requests for Book Pahlavi script for Middle Persian terms 
568: Middle Persian terms with redundant script codes 
569: Old Persian terms with non-redundant manual transliterations 

=== posht ===
270: Inherited from Proto-Iranian *pr̥štáh ( “ back ” ) . Cognate with Avestan 𐬞𐬀𐬭𐬱𐬙𐬀 ( paršta ) , Sanskrit पृष्ठ ( pṛṣṭha ) . [ 1 ] 
486: Persian terms derived from Proto-Indo-European 
487: Persian terms inherited from Proto-Indo-European 
488: Persian terms inherited from Proto-Iranian 
489: Persian terms derived from Proto-Iranian
```


## [2026-09-14T02:43:57.765Z] TOOL CALL #93: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; head -4 b470cdbcbf21b179.txt; grep -n \"Middle Persian\\|Old Persian\" b470cdbcbf21b179.txt | head -4",
 "description": "Check -stān page"
}
```


### [2026-09-14T02:43:57.830Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/-%D8%B3%D8%AA%D8%A7%D9%86
FETCHED: 2026-09-14T02:40:45Z
STATUS: -1
TITLE:
```


## [2026-09-14T02:44:03.734Z] TOOL CALL #94: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%D9%80%D8%B3%D8%AA%D8%A7%D9%86\" --note \"page 474 node 2, Persian suffix -estān\" 2>&1|tail -1; f=$(python3 -c \"import hashlib;print(hashlib.sha1('https://en.wiktionary.org/wiki/%D9%80%D8%B3%D8%AA%D8%A7%D9%86'.encode()).hexdigest()[:16])\"); head -4 data/verification/sources/web/$f.txt; grep -n \"Middle Persian\\|Old Persian\\|Proto-Iranian\" data/verification/sources/web/$f.txt | head -4",
 "description": "Fetch Persian suffix -estān"
}
```


### [2026-09-14T02:44:06.515Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/8fa856b81abd63c9.txt
URL: https://en.wiktionary.org/wiki/%D9%80%D8%B3%D8%AA%D8%A7%D9%86
FETCHED: 2026-09-14T02:44:06Z
STATUS: 200
TITLE: ـستان - Wiktionary, the free dictionary
236: Middle Persian -stʾn' 
309: Middle Persian -stʾn' 
312: From Middle Persian -stʾn' ( -estān ) , from Old Persian 𐎿𐎫𐎠𐎴 ( s-t-a-n /⁠stānaʰ⁠⁠⁠/ ) , from Proto-Iranian *stā́nam (compare Avestan 𐬯𐬙𐬁𐬥𐬀 ( stāna ) ), from Proto-Indo-Iranian *stáHnam , from Proto-Indo-European *steh₂- ( “ to stand ” ) . Cognate with Ossetian -ыстон ( -yston ) , Sanskrit स्थान ( sthāna ) .
593: Borrowed from Classical Persian ـِسْتَان ( -istān ) , from Middle Persian -stʾn' ( -estān ) , from Old Persian 𐎿𐎫𐎠𐎴 ( s-t-a-n /⁠stāna⁠/ ) , from Proto-Iranian *stā́nam , from Proto-Indo-Iranian *stʰáHnam , from Proto-Indo-European *steh₂- ( “ to stand ” ) .
```


## [2026-09-14T02:48:00.648Z] TOOL CALL #95: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; pdftoppm -f 474 -l 474 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg474 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg474.png",
 "description": "Render PDF page 474 to PNG"
}
```


### [2026-09-14T02:48:02.630Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 106745 Sep 13 22:48 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg474.png
```


## [2026-09-14T02:48:04.595Z] TOOL CALL #96: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg474.png"
}
```


### [2026-09-14T02:48:05.320Z] TOOL RESULT

```

```


## [2026-09-14T02:48:05.315Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T02:48:24.732Z] TOOL CALL #97: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg474.png')\nprint(im.size)\n# Sogdian box approx y 690-745 of 2000-display -> scale\nw,h=im.size\nbox=(int(0.27*w),int(0.335*h),int(0.47*w),int(0.375*h))\nim.crop(box).resize((int((box[2]-box[0])*4),int((box[3]-box[1])*4))).save('pg474-sogd.png')\n\" && ls -la pg474-sogd.png",
 "description": "Crop Sogdian box from page image"
}
```


### [2026-09-14T02:48:26.002Z] TOOL RESULT

```
(1700, 2200)
-rw-rw-r-- 1 sfmqrb sfmqrb 54581 Sep 13 22:48 pg474-sogd.png
```


## [2026-09-14T02:48:28.096Z] TOOL CALL #98: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg474-sogd.png"
}
```


### [2026-09-14T02:48:28.123Z] TOOL RESULT

```

```


## [2026-09-14T02:48:46.336Z] TOOL CALL #99: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg474.png data/verification/sources/refs/ocr/BOOK/474.png && ls -la data/verification/sources/refs/ocr/BOOK/474.png",
 "description": "Copy page image for audit"
}
```


### [2026-09-14T02:48:46.418Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 106745 Sep 13 22:48 data/verification/sources/refs/ocr/BOOK/474.png
```


## [2026-09-14T02:56:39.164Z] TOOL CALL #100: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-474.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, os\n\nW = \"https://en.wiktionary.org/wiki/\"\nS = {\n \"pie\": W+\"Reconstruction:Proto-Indo-European/steh%E2%82%82-\",\n \"sotun\": W+\"%D8%B3%D8%AA%D9%88%D9%86\",\n \"istadan\": W+\"%D8%A7%DB%8C%D8%B3%D8%AA%D8%A7%D8%AF%D9%86\",\n \"ashti\": W+\"%D8%A2%D8%B4%D8%AA%DB%8C\",\n \"posht\": W+\"%D9%BE%D8%B4%D8%AA\",\n \"fereshte\": W+\"%D9%81%D8%B1%D8%B4%D8%AA%D9%87\",\n \"ostad\": W+\"%D8%A7%D8%B3%D8%AA%D8%A7%D8%AF\",\n \"gostax\": W+\"%DA%AF%D8%B3%D8%AA%D8%A7%D8%AE\",\n \"lashkar\": W+\"%D9%84%D8%B4%DA%A9%D8%B1\",\n \"tabestan\": W+\"%D8%AA%D8%A7%D8%A8%D8%B3%D8%AA%D8%A7%D9%86\",\n \"parastidan\": W+\"%D9%BE%D8%B1%D8%B3%D8%AA%DB%8C%D8%AF%D9%86\",\n \"ferestadan\": W+\"%D9%81%D8%B1%D8%B3%D8%AA%D8%A7%D8%AF%D9%86\",\n \"soturg\": W+\"%D8%B3%D8%AA%D8%B1%DA%AF\",\n \"bisotun_en\": W+\"Bisotun\",\n \"bisotun_fa\": W+\"%D8%A8%DB%8C%D8%B3%D8%AA%D9%88%D9%86\",\n \"artesh\": W+\"%D8%A7%D8%B1%D8%AA%D8%B4\",\n \"estan\": W+\"%D9%80%D8%B3%D8%AA%D8%A7%D9%86\",\n}\n\nnodes = []\n\nnodes.append({\n \"id\": 1, \"lang\": \"Avestan / Old Persian\",\n \"words\": \"sta 1 : to stand, to set; stâ 1, stata, šta 1, šti\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Avestan and Old Persian stā- 'to set; (mid.) to stand' continue PIE *steh₂- with the regular Indo-Iranian merger of *e/*o/*a into a and loss of the laryngeal with compensatory lengthening (*steh₂- > *stā-). The chart's four shapes are the standard stem forms: (a) the bare root stā- (OP stāyam, Av. stā-); (b) the verbal adjective *sth₂-tó- > Av. stata- (YAv. auuastāta- 'set down', F 149), OP -stāta-; (c) 'šta' is the reduplicated present *sti-sth₂-eti > Skt. tíṣṭhati, Av. hištaiti, OP a-ištatā (impf. mid., DB 1.85) — the -št- of the chart is the Avestan/OP treatment of *-st- after i; (d) 'šti' is the ti-abstract *sth₂-ti- > Av. stāti- 'standing, position', and in compounds -šti- (āxšti- 'peace', pairišti-). Kent p.210 gives exactly this equation. One caveat: Avestan and Old Persian are two distinct languages that Nourai puts in one box; the forms listed happen to be common to both.\",\n \"derivation_fa\": \"ستاک stā- در اوستایی و پارسی باستان به معنی «ایستادن، نهادن» دنبالهٔ مستقیم ریشهٔ هندواروپایی آغازین *steh₂- است؛ در هندوایرانی واکه‌های *e/*o/*a به a بدل شده و حنجره‌ای (laryngeal) با کشیده‌شدن واکه افتاده است (*steh₂- > *stā-). چهار صورتی که نورایی آورده، همان ستاک‌های شناخته‌شده‌اند: خودِ ریشه stā-؛ صفت مفعولی *sth₂-tó- > stata- اوستایی (auuastāta- «فرونهاده»)؛ «šta» که بازماندهٔ حال دوتایی‌شدهٔ (reduplicated) *sti-sth₂-eti است (سنسکریت tíṣṭhati، اوستایی hištaiti، پارسی باستان aištatā)؛ و «šti» که نام‌ستاک -ti است (اوستایی stāti- «ایستادن، جایگاه»، و در ترکیب‌ها -šti- مانند āxšti- «آشتی»). کنت (ص ۲۱۰) و هرن (ص ۲۰) همین را می‌گویند. تنها نکتهٔ قابل ایراد آن است که نورایی اوستایی و پارسی باستان را در یک جعبه جمع کرده است. ادعای نورایی درست است.\",\n \"sources\": [S[\"pie\"]],\n \"ref_check\": [\n  {\"ref\": \"BQT:123\", \"status\": \"not_checked\", \"note\": \"Borhan-e Qate' vols 1-2 are on disk only as un-paginated OCR (BQT_v1_pages.txt has no printed-page markers), so printed p.123 could not be located; vols 3-5 (the scans reachable by tools/ref_page.py) start at p.1208.\"},\n  {\"ref\": \"HRN:20\", \"status\": \"supports\", \"note\": \"Horn, Grundriss p.20 no.84: 'istāden \\\"stehen\\\", estāden, Praes. est-em, sitāden ... ap. √stā- (ai. sthā-); pāz. estādan' — the Old Persian root is exactly the chart's 'sta 1'. (local HRN.txt, form-feed leaf 42 = printed p.20)\"},\n  {\"ref\": \"POK:1008\", \"status\": \"supports\", \"note\": \"Pokorny IEW p.1008 (POK_03.txt leaf 249) is inside the article 'stā-: stə- ... \\\"stehen, stellen\\\"' and there gives '11. mit n-Formantien: ai. sthā́na-, av. ap. stāna- n. \\\"Standort, Ort, Platz\\\", npers. sitān'.\"}\n ],\n \"consulted\": [\n  {\"src\": \"KNT\", \"where\": \"p.210 s.v. stā-\", \"stance\": \"supports\", \"note\": \"'stā- vb. \\\"set; (mid.) stand\\\": Av. stā-, Skt. sthā-, Gk. ἵστημι, Lit. stóju stóti, pIE *st(h)ā- ... a-i-š-t-t-a imf. mid. DB 1.85' (KNT_full.txt line 29222 ff.)\"},\n  {\"src\": \"CHEUNG\", \"where\": \"s.v. *staH, pp. 358-360\", \"stance\": \"supports\", \"note\": \"'*staH \\\"to place, set; [intr.] stand\\\" — AVESTAN stā- ... Pres. them. red.: YAv. hištaiti ... Partic. perf. pass. YAv. stata-, YAv. auuastata- (F 149) ... OLD PERSIAN stā- \\\"to set, [med.] to stand\\\" = Kent: 210a' (CHEUNG.txt lines 23411 ff.)\"},\n  {\"src\": \"BRT\", \"where\": \"AiW s.v. stā-, and col. 1608 stuna-/stunā-\", \"stance\": \"supports\", \"note\": \"Bartholomae's Altiranisches Wörterbuch has the root and its participles; the OCR of the st- columns is poor but 'j. stuna- m., stunā- f. \\\"Säule\\\"' is legible (BRT.txt line 26778) and Nyberg cites the column number as '(1608)'.\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. sta-\", \"stance\": \"supports\", \"note\": \"'sta-. To stand; with derivatives meaning \\\"place or thing that is standing.\\\" Contracted from *staə-.' (AHD_watkins1985.txt line 997)\"}\n ]\n})\n\nnodes.append({\n \"id\": 2, \"lang\": \"Persian\",\n \"words\": \"- stân «- ستان»; bağstân «بغستان»; setâk «سیتاک»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"(1) -stān: Old Persian stāna- n. 'place' (XV 20f., Kent p.210, who himself glosses it 'Av. -stāna- in cpds., NPers. -stān, Skt. sthāna-; deriv. of root stā-') is *steh₂- + the *-no- suffix; MP -stān, NP -ستان, productive for 'place full of X' (گلستان, کوهستان) and for country names. (2) bağstān: Old Persian *Bagastāna- 'place of the gods', the name of the crag on which Darius cut the Bīsotūn inscription, known to Greek geographers as Βαγίστανον ὄρος (Diodorus 2.13); Iranian *baga- 'god' (whence also the doublet فغستان faġestān 'temple' with the regular b- > f- of the Parthian/NW form) + -stāna-; the modern name بیستون is a folk-etymological reshaping as bī-sotūn 'without pillars'. (3) setāk 'branch': Horn no.82 'istāx, istak, sitak \\\"Zweig\\\". Die ältere Form ist istak, sitāk, phlv. stak (Bund.). Zu √sthā-' — a *stā-ka- 'that which stands up', with the usual NP prothetic vowel before st-, and the variant سیتاخ/إستاخ from the same MP stak with -k > -x.\",\n \"derivation_fa\": \"۱) پسوند «ـستان» از پارسی باستان stāna- «جای» (کنت ص ۲۱۰) است که خود از ریشهٔ stā- با پسوند -na- ساخته شده؛ فارسی میانه -stān و فارسی نو ـستان (گلستان، کوهستان، تاجیکستان). ۲) «بغستان» از پارسی باستان *Bagastāna- «جایگاه خدایان»، نام همان صخره‌ای که داریوش سنگ‌نبشتهٔ خود را بر آن کند؛ یونانیان آن را Βαγίστανον ὄρος نوشته‌اند (دیودوروس). صورت امروزی «بیستون» ریشه‌شناسی عامیانه (folk etymology) است: بی + ستون. دوگانهٔ آن «فغستان» (پرستشگاه) با ابدال b > f در گویش شمال غربی است. ۳) «سیتاک/ستاک» از *stā-ka- «آنچه می‌ایستد»؛ هرن (ص ۲۰، شمارهٔ ۸۲) می‌نویسد صورت کهن‌تر istak، sitāk و پهلوی stak است و آن را به ریشهٔ √sthā- می‌رساند. ادعای نورایی در هر سه مورد درست است.\",\n \"sources\": [S[\"estan\"], S[\"bisotun_en\"], S[\"bisotun_fa\"]],\n \"ref_check\": [\n  {\"ref\": \"BQT:289\", \"status\": \"not_checked\", \"note\": \"Borhan vol.1 (which would contain بغستان under ب) is on disk only as un-paginated OCR; printed p.289 cannot be located.\"},\n  {\"ref\": \"BQT:1097\", \"status\": \"partial\", \"note\": \"p.1097 falls in vol.2, the س+ت stretch; Aryanpur's entry «ستون» cites exactly 'برهان قاطع ۱۰۹۷' for that word (ARY_pages.txt, pdf p.85), which confirms the page really is the setūn/setāk region of Borhan, but the un-paginated vol.2 OCR does not let the entry itself be read.\"},\n  {\"ref\": \"HRN:20\", \"status\": \"supports\", \"note\": \"Horn p.20 no.82: 'istāx, istak, sitak \\\"Zweig\\\" ... Die ältere Form ist istak, sitāk, phlv. stak (Bund.). Zu √sthā-.' — the chart's setāk 'branch' verbatim.\"}\n ],\n \"consulted\": [\n  {\"src\": \"KNT\", \"where\": \"p.210 s.v. stāna-\", \"stance\": \"supports\", \"note\": \"'stāna- sb. \\\"place\\\": Av. -stāna- in cpds., NPers. -stān, Skt. sthāna-; deriv. of root stā-.'\"},\n  {\"src\": \"IEC\", \"where\": \"Mann s.v. sthān-\", \"stance\": \"supports\", \"note\": \"'sthān- ... Nominal types: Skt. sthānam n. \\\"stand, station\\\"; Av. stānō m. \\\"place, stable\\\"; OPer. stānam n. id.; Per. -stān, cpds. id.' (IEC.txt line 17526)\"},\n  {\"src\": \"ARY\", \"where\": \"Aryanpur, printed p.86 (pdf p.85)\", \"stance\": \"supports\", \"note\": \"The «ستون» entry lists 'اوستایی STŪNĀ / پارسی باستان STŪNĀ / پهلوی STŪN / سانسکریت STHŪNĀ' and refers to برهان قاطع ۱۰۹۷ — an independent modern Persian cross-check for the whole -stān/sotūn family.\"},\n  {\"src\": \"MON\", \"where\": \"Mo'in, Farhang, s.v. استان\", \"stance\": \"supports\", \"note\": \"'استان: [- آستانه] (اِ.) قسمت پیشین اطاق متصل به در، درگاه؛ آستانه، جناب' (MON_part1.txt line 3133) — Mo'in equates استان with آستانه, i.e. the same *(ā-)stāna-.\"}\n ]\n})\n\nnodes.append({\n \"id\": 3, \"lang\": \"Avestan / Old Persian\",\n \"words\": \"adi-sta; tap-stana; â-stana; stuna, stůnâ\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Two of the four items are solidly attested, two are reconstructions of a kind modern handbooks no longer make. stuna/stūnā is exact: OP stūnā 'column' (DSf 45, Kent p.210 'stūnā- sb. \\\"column\\\": Av. stūna- masc., stūnā- fem., NPers. sutūn, Skt. sthūṇā-'), Av. stūna- m./stūnā- f. 'Säule' (Bartholomae col. 1608), from *stuH-n-eh₂ (Pokorny p.1008-9, section F: 'schwachstufig: ai. sthūnā \\\"Säule\\\", av. stūna, stunā \\\"Säule\\\"'). ā-stāna- 'entrance, threshold' is the same *-na- noun with preverb ā-; the type is attested in OP ardastāna- 'window-frame' (Kent p.210), and MP āstānag > NP آستان/آستانه. 'adi-sta' is not an attested compound: it is Horn's (p.20 no.84) proposal 'Ich leite np. estāden, später istāden, von ap. *adi + √stā- ab', which today's handbooks do not follow — Cheung 2007 puts MP ēst- under *abi-staH, and Wiktionary derives ایستادن simply from Old Persian stā- (Proto-Iranian *staH-). 'tap-stana' is likewise unattested in Old Iranian: تابستان is a Middle Persian formation (BMP tʾpstʾn /tābestān/) = tāb 'heat' + -estān, so the node's language label is a few centuries too early for it.\",\n \"derivation_fa\": \"از چهار صورت این جعبه دو تا گواهی‌شده‌اند و دو تا بازسازی‌های قدیمی‌اند. stūnā دقیق است: پارسی باستان stūnā «ستون» (سنگ‌نبشتهٔ DSf)، اوستایی stūna-/stūnā-، سنسکریت sthūṇā، از *stuH-n-eh₂ (پوکورنی ص ۱۰۰۸-۱۰۰۹). ā-stāna- «درگاه» همان نام‌ستاک -na- با پیشوند ā- است (قس پارسی باستان ardastāna- «چارچوب پنجره») و در فارسی میانه āstānag و در فارسی نو «آستان/آستانه» شده است. اما «adi-sta» صورتی گواهی‌شده نیست؛ این پیشنهاد هرن (ص ۲۰) است که ایستادن را از *adi + √stā- می‌گیرد، حال آنکه چونگ (۲۰۰۷) فعل ēst- فارسی میانه را زیر *abi-staH می‌آورد و ویکی‌واژه تنها به «از پارسی باستان، از ایرانی آغازین *staH-» بسنده می‌کند. «tap-stana» هم در ایرانی باستان گواهی ندارد: «تابستان» ساختی فارسی‌میانه است (tʾpstʾn) از تاب + ـستان. پس ادعای نورایی با احتیاط پذیرفتنی است و برچسب «اوستایی/پارسی باستان» برای دو مورد زودهنگام است.\",\n \"sources\": [S[\"istadan\"], S[\"tabestan\"], S[\"sotun\"]],\n \"ref_check\": [\n  {\"ref\": \"KNT:210\", \"status\": \"supports\", \"note\": \"Kent p.210 has both relevant headwords: 'stāna- sb. \\\"place\\\" ... See also ardastāna-' and 'stūnā- sb. \\\"column\\\": Av. stūna- masc., stūnā- fem., NPers. sutūn, Skt. sthūṇā-. stūnā npf. DSf 45'.\"},\n  {\"ref\": \"POK:1008\", \"status\": \"supports\", \"note\": \"IEW p.1008/1009 section F: 'st(h)āu-: st(h)ū- ... schwachstufig: ai. sthūnā \\\"Säule\\\" (mind. n aus ṇ), av. stūna, stunā \\\"Säule\\\"' (POK_03.txt leaf 249-250).\"},\n  {\"ref\": \"HRN:20\", \"status\": \"partial\", \"note\": \"Horn p.20 no.84 supplies the chart's 'adi-sta' but only as his own conjecture ('Ich leite np. estāden ... von ap. *adi + √stā- ab'); he marks no such Avestan/OP compound as attested.\"},\n  {\"ref\": \"BQT:123\", \"status\": \"not_checked\", \"note\": \"vols 1-2 OCR has no page markers (see node 1).\"}\n ],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"AiW col. 1608\", \"stance\": \"supports\", \"note\": \"'j. stuna- m., stunā- f. \\\"Säule\\\"' (BRT.txt line 26778); the column number 1608 is the one Nyberg quotes for this word.\"},\n  {\"src\": \"CHEUNG\", \"where\": \"s.v. *staH, p.358\", \"stance\": \"contradicts\", \"note\": \"Cheung lists the Avestan preverb-compounds actually attested — '(+ *aua-) \\\"to enter; to settle (down)\\\" || (+ *ā-) \\\"to take place\\\" || (+ *upa-) \\\"to tread on\\\" || (+ *us-) ... || (+ *fra-) ... || (+ *ni-) \\\"to order\\\"' — but no *adi-, and he assigns MP ēst-/ēstādan to '(+ *abi-)', not *adi-.\"},\n  {\"src\": \"PHD\", \"where\": \"p.29 s.v. ēstādan, p.78 s.v. stūn(ag)\", \"stance\": \"supports\", \"note\": \"'ēstādan, ēst- [YKOYMWN-tn' ... | M ʾyst-ʾdn, N ~] stand' and 'stūn(ag) [stwn(k)ʾ | M ʾstwn, N sutūn] column, pillar, mast'.\"},\n  {\"src\": \"NYB\", \"where\": \"Glossary s.v. stūnak\", \"stance\": \"supports\", \"note\": \"'stūnak [stwnkʾ] pillar 39¹⁹·²⁹; trunk, of the human body 72⁷. + Av. (1608) stūna-, stunā-; MPrth ʾstwn \\\"mast\\\"; MPrs ʾ(y)stwn \\\"pillar\\\"; ... NP sutūn \\\"column\\\"'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 4, \"lang\": \"Sogdian\",\n \"words\": \"`st`wn`\",\n \"verdict\": \"transcription_suspect\",\n \"error_in\": \"extraction\",\n \"book_prints\": \"`st`wn\",\n \"correct_form\": \"`st`wn (Gharib no. 1689 ʾstʾwn)\",\n \"derivation\": \"The etymology itself is confirmed and is exactly what Nourai's own reference says: Gharib, Sogdian Dictionary no. 1689 (printed p.67) reads 'ʾstʾwn B — ostun ©<OP stūnā ©ob. -yh — column, colonnade (SCE 229)'. Buddhist Sogdian ʾstʾwn /əstūn/ shows the regular Sogdian prothetic ʾa- before an initial st- cluster (the same prothesis as in ʾstʾrʾk 'star', ʾstk 'bone') and the -ʾw- spelling of ū; the word continues Old Iranian *stuHnā, i.e. the same *-nā- derivative as OP stūnā and Av. stūna-/stūnā- in the parent node. The flag is purely graphic: the printed page (pdf p.474, image copied to data/verification/sources/refs/ocr/BOOK/474.png) shows `st`wn with two backticks, while the extracted JSON has a third, spurious backtick at the end (`st`wn`). Nothing else in the node is wrong.\",\n \"derivation_fa\": \"ریشه‌شناسی این گره درست است و دقیقاً همان چیزی است که مأخذ خودِ نورایی می‌گوید: غریب، فرهنگ سغدی، مدخل ۱۶۸۹ (ص ۶۷): «ʾstʾwn (سغدی بودایی) = ostun، از پارسی باستان stūnā، ستون». الفِ آغازین سغدی همان واکهٔ میانجی (prothetic) پیش از خوشهٔ st- است (مانند ʾstʾrʾk «ستاره»، ʾstk «استخوان») و ʾw نشانهٔ ū است. واژه دنبالهٔ ایرانی باستان *stuHnā است، یعنی همان ساخت -nā- که در stūnā پارسی باستان و stūna-/stūnā- اوستایی دیده می‌شود. نشانهٔ هشدار تنها املایی است: صفحهٔ چاپی کتاب `st`wn را با دو علامت واروگون (backtick) نشان می‌دهد، ولی در دادهٔ استخراج‌شده یک واروگون اضافی در پایان آمده است (`st`wn`). این خطای خوانش اسکن است، نه خطای کتاب.\",\n \"sources\": [S[\"sotun\"]],\n \"ref_check\": [\n  {\"ref\": \"SOD:67\", \"status\": \"supports\", \"note\": \"Gharib, Sogdian-Persian-English Dictionary, printed p.67 (SOD_pages.txt form-feed leaf 133), entry 1689: 'ʾstʾwn B — ostun ©<OP stūnā ©ob. -yh — column, colonnade — SCE 229'. The page number Nourai cites is exact.\"}\n ],\n \"consulted\": [\n  {\"src\": \"KNT\", \"where\": \"p.210 s.v. stūnā-\", \"stance\": \"supports\", \"note\": \"Gives the Old Persian source form stūnā 'column' that Gharib names.\"},\n  {\"src\": \"PHD\", \"where\": \"p.78 s.v. stūn(ag)\", \"stance\": \"supports\", \"note\": \"'stūn(ag) [stwn(k)ʾ | M ʾstwn, N sutūn]' — Manichaean Middle Persian also writes the prothetic ʾ-, exactly like the Sogdian form.\"},\n  {\"src\": \"CHEUNG\", \"where\": \"s.v. *staH (Sogdian section)\", \"stance\": \"partial\", \"note\": \"Cheung's Sogdian material for *staH is verbal ('ʾwst- \\\"to stand, fix, put\\\"' etc.); the noun ʾstʾwn is not in his verb dictionary, so he is silent on this particular word.\"}\n ]\n})\n\nnodes.append({\n \"id\": 5, \"lang\": \"Persian\",\n \"words\": \"îstâdan «ایستادن»; tâbestân «تابستان»; âstân «آستان»; sotůn «ستون»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All four are genuine New Persian continuations of the parent node. (1) ایستادن < MP ēstādan (BMP ʾ(y)sttn', logogram YKOYMWN-tn'; MacKenzie p.29) < Old Iranian *(a)i-štā-, the reduplicated/preverbed present of *staH; the NP ē- > ī- raising is regular (ēstādan > īstādan), and the offshoots استان 'province' and ستاد 'headquarters' are later nominalisations of the same stem. (2) تابستان < MP tābestān (BMP tʾpstʾn) = tāb 'heat' (< *tap-) + -estān 'place/season of', with the intervocalic *p > b lenition of Middle Persian. (3) آستان/آستانه 'threshold' < MP āstānag < *ā-stāna- 'place of standing (at the door)'. (4) ستون < MP stūn (M ʾstwn) < OP stūnā (Wiktionary: 'from Old Persian 𐎿𐎬𐎢𐎴𐎠 (stūnā), from Proto-Iranian *stuHnáH, compare Avestan stūna, from Proto-Indo-Iranian *stʰuHnáH, compare Sanskrit sthūṇā'); the NP prothetic vowel (su-tūn) is the normal treatment of MP initial st-. The dialect form اُستُن given in the chart's extra shows the other prothesis (u-stun), exactly as in Horn no.721 'sutūn, ustūn \\\"Säule\\\"'.\",\n \"derivation_fa\": \"هر چهار واژه دنبالهٔ راستین جعبهٔ بالا هستند. ۱) «ایستادن» از فارسی میانهٔ ēstādan (YKOYMWN-tn' در پهلوی کتابی) از ایرانی باستان، با همان ستاک دوتایی‌شدهٔ *(a)i-štā-؛ تبدیل ē > ī در فارسی نو قاعده‌مند است، و «استان» و «ستاد» گونه‌های نام‌ساختهٔ همین ستاک‌اند. ۲) «تابستان» از فارسی میانهٔ tābestān (tʾpstʾn) = تاب (از *tap- «گرما») + ـستان؛ نرم‌شدن p میان دو واکه به b در فارسی میانه قاعده است. ۳) «آستان/آستانه» از فارسی میانهٔ āstānag از *ā-stāna- «جای ایستادن (بر در)». ۴) «ستون» از فارسی میانهٔ stūn (مانوی ʾstwn) از پارسی باستان stūnā، ایرانی آغازین *stuHnáH، هم‌ریشه با sthūṇā سنسکریت؛ واکهٔ میانجی su- در فارسی نو پیش از خوشهٔ st- افزوده شده است و گونهٔ «اُستُن» که نورایی آورده همان است که هرن (ص ۱۵۹، شمارهٔ ۷۲۱) با صورت ustūn ثبت کرده. ادعای نورایی درست است.\",\n \"sources\": [S[\"istadan\"], S[\"tabestan\"], S[\"sotun\"]],\n \"ref_check\": [\n  {\"ref\": \"BQT\", \"status\": \"not_checked\", \"note\": \"Nourai gives no page; Borhan vols 1-2 (which contain ایستادن، آستان، تابستان) are on disk only as un-paginated OCR.\"},\n  {\"ref\": \"MON\", \"status\": \"supports\", \"note\": \"Mo'in, Farhang s.v. استان: 'استان: [- آستانه] (اِ.) قسمت پیشین اطاق متصل به در، درگاه؛ آستانه' (MON_part1.txt line 3133) — Mo'in derives استان from آستانه, i.e. from the same *(ā-)stāna-.\"}\n ],\n \"consulted\": [\n  {\"src\": \"PHD\", \"where\": \"p.29 s.v. ēstādan; p.78 s.v. stūn(ag)\", \"stance\": \"supports\", \"note\": \"'ēstādan, ēst- [YKOYMWN-tn' < A yqym ... | M ʾyst-ʾdn, N ~] stand'; 'stūn(ag) [stwn(k)ʾ | M ʾstwn, N sutūn] column, pillar, mast'.\"},\n  {\"src\": \"HRN\", \"where\": \"p.159 no.721; p.20 no.84\", \"stance\": \"supports\", \"note\": \"'sutūn, ustūn \\\"Säule\\\". aw. stūna- \\\"Säule\\\"; phlv. stūn, syr. LW. ʾstwnʾ; ai. sthūnā- \\\"Säule\\\"'; and no.84 for istāden.\"},\n  {\"src\": \"NYB\", \"where\": \"Glossary s.v. stūnak\", \"stance\": \"supports\", \"note\": \"'+ Av. (1608) stūna-, stunā-; ... NP sutūn \\\"column\\\", sutūnah \\\"pivot\\\"'.\"},\n  {\"src\": \"ARY\", \"where\": \"Aryanpur, printed p.86\", \"stance\": \"supports\", \"note\": \"Entry «ستون» with AVESTAN STŪNĀ / OLD PERSIAN STŪNĀ / PAHLAVI STŪN / SANSKRIT STHŪNĀ / GREEK STŪLOS, citing برهان قاطع ۱۰۹۷.\"}\n ]\n})\n\nnodes.append({\n \"id\": 6, \"lang\": \"Avestan\",\n \"words\": \"ava-stata, hvô-îstâ; fra-sta; fra-aiš, fraěšta; par-šta; par-šti; â-x-stâ, axštî\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Five of the six items belong to *steh₂-; one does not. (a) ava-stāta- is attested (YAv. perfect passive participle, Fragment 149; Cheung s.v. *staH), lit. 'set down, set over', and Proto-Iranian *Hawastātas is the source of NP استاد. 'hvô-îstâ' (presumably *hu-ištā- 'well standing') is not an attested Avestan word and does not appear in Bartholomae; Horn no.83 offers only aw. *avastāta- 'Vorsteher' for ostād. (b) fra-stā- is real: Av. fra-stā- '(to) proceed, go before' and OP frastayam 'I send forth' (DB 4.92; Cheung s.v. *staH), whence MP frēstādan 'to send'. (c) fra-aiš / fraēšta does NOT belong here. Av. fraēšta- m. 'Gesandter, Bote' (Bartholomae) and OP fraiš- 'to send forth' (Kent p.164b) belong to the root *HaišH 'to set in motion' (Av. aēš-, Skt. eṣ-/preṣya-, PIE *h₁eisH-), which Cheung treats as a separate lemma; Mo'in's own footnote in Borhan p.1463 — the page Nourai cites in the daughter node — derives فرشته from *fra-ista- 'from fra- + aiš-', Av. fraēšta-, Arm. hreštak. So this arrow is disputed. (d) par-šta / par-šti: Av. paršta- / paršti- 'back' = Skt. pṛṣṭhá-/pṛṣṭí-, a compound *pr̥-sth₂-ó- 'standing forth' (Pokorny p.1006-7 lists 'ai. pr̥ṣṭhá- n. \\\"Rücken\\\"' and 'ai. pr̥ṣṭí- f. \\\"Rücken\\\"' among the *-sth₂-o-/-sth₂-i- compounds); Klein p.1223 s.v. post: 'L. postis \\\"doorpost\\\", for *por-stis, lit. \\\"standing out\\\", cogn. with OI. pṛṣṭham, Avestic par-shti (dual) \\\"back\\\"'. Confirmed — but the gloss 'worship' that Nourai attaches to par-šta belongs to a different formation, *pari-stā- 'to stand around, attend' (MP paristīdan), not to *pr̥šta- 'back'. (e) ā-x-stā/āxšti-: Av. āxšti- f. 'Friede, Friedensvertrag' (Bartholomae; an-āxšti- 'Unfriede'); Buck, Dict. of Selected Synonyms 20.14 p.1376: 'Av. āxšti-, NPers. āštī, prob. : ā(x)šta- in caus. \\\"put in place, appoint\\\", cpd. of stā- (xštā-) \\\"stand\\\". Brugmann ... Barth. 311, 1602.' Confirmed — the -xšt- is the regular Avestan outcome of the s-mobile/reduplicated stem (cf. fraxštaite, xšta).\",\n \"derivation_fa\": \"پنج مورد از شش مورد این جعبه به ریشهٔ *steh₂- می‌رسند، اما یکی نه. الف) ava-stāta- گواهی‌شده است (صفت مفعولی کامل در اوستای متأخر، قطعهٔ ۱۴۹) و ایرانی آغازین *Hawastātas سرچشمهٔ «استاد» است؛ ولی hvô-îstâ در اوستا گواهی ندارد و در بارتولومه نیامده است. ب) fra-stā- درست است: پارسی باستان frastayam «فرستادم» (بیستون ۴٫۹۲) و اوستایی fra-stā-. ج) اما fra-aiš/fraēšta به این ریشه تعلق ندارد: fraēšta- اوستایی «فرستاده، پیک» و fraiš- پارسی باستان از ریشهٔ *HaišH «به جنبش درآوردن» (اوستایی aēš-، سنسکریت eṣ-/preṣya-) است که چونگ آن را مدخلی جداگانه آورده؛ خودِ حاشیهٔ معین در برهان قاطع ص ۱۴۶۳ نیز «فرشته» را از *fra-ista- (از fra- + aiš-) می‌گیرد. پس این پیکان را پژوهش امروزی رد می‌کند. د) paršta-/paršti- «پشت» ترکیب *pr̥-sth₂-ó- «پیش‌ایستاده» است (پوکورنی ص ۱۰۰۶-۱۰۰۷؛ کلاین ص ۱۲۲۳ ذیل post)، اما معنای «پرستیدن» که نورایی به par-šta بسته، به ساخت دیگری یعنی *pari-stā- «گرداگرد ایستادن، خدمت کردن» مربوط است. ه) āxšti- «آشتی» درست است: باک (ص ۱۳۷۶، بخش ۲۰٫۱۴) می‌نویسد «اوستایی āxšti-، فارسی نو āštī، احتمالاً از ā(x)šta- ... مرکب از stā- \\\"ایستادن\\\"». خوشهٔ -xšt- برآمد قاعده‌مند ستاک دوتایی‌شده در اوستاست (قس fraxštaite). حکم کلی: به سبب مورد fra-aiš، این گره «رد‌شده» است.\",\n \"sources\": [S[\"fereshte\"], S[\"ashti\"], S[\"posht\"], S[\"ferestadan\"]],\n \"ref_check\": [\n  {\"ref\": \"KLN:1222\", \"status\": \"supports\", \"note\": \"Klein 1966, the page marked 1222./1223 (KLN_1966.txt line 29747 ff.), s.v. 'post, n., pillar. — ME., fr. OF., fr. L. postis, \\\"doorpost\\\", for *por-stis, lit. \\\"standing out\\\", which is cogn. with OI. pṛṣṭham, \\\"back, roof, peak\\\", Avestic par-shti (dual), \\\"back\\\", Gk. παστάς ... See 1st pro- and state.' — this is exactly the chart's par-šti item.\"},\n  {\"ref\": \"POK:1008\", \"status\": \"partial\", \"note\": \"IEW p.1008 has the n-stem nouns but the compounds Nourai lists here are on pp.1006-1007 ('ai. pr̥ṣṭhá- n. \\\"Rücken\\\" usw. (S. 813)'; 'ai. pr̥ṣṭí- f. \\\"Rücken\\\" ... und prati-sthí- \\\"Widerstand\\\"'). Pokorny nowhere puts fraēšta- under stā-.\"},\n  {\"ref\": \"SYN:1376\", \"status\": \"supports\", \"note\": \"Buck, A Dictionary of Selected Synonyms, p.1376, §20.14 PEACE: 'Av. āxšti-, NPers. āštī, prob. : ā(x)šta- in caus. \\\"put in place, appoint\\\", cpd. of stā- (xštā-) \\\"stand\\\". Brugmann, op. cit. 11. Barth. 311, 1602.' (SYN.txt line 34457 ff.) — precisely Nourai's 'â-x-stâ, axštî : put in place, put in peace'.\"},\n  {\"ref\": \"SOD:439\", \"status\": \"not_found\", \"note\": \"Gharib's printed p.439 (SOD_pages.txt leaf 507, running head 'xwsywnc') is in the xw- section and has nothing to do with these compounds; entry no. 439 is likewise unrelated. The Sogdian forms that would be relevant (frēst 'sent' < *fra-ista-, prstʾy 'to prepare') are elsewhere in the book.\"}\n ],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"AiW s.v. fraēšta-, āxšti-\", \"stance\": \"partial\", \"note\": \"'j. ᵃfraēšta- m. \\\"Gesandter, Bote\\\": yavōi vīspāi °tāṇhō hyāmā' (BRT.txt line 17499) — Bartholomae lists fraēšta- as a separate lemma, not under stā-; and 'j. āxšti- f. 1) \\\"Friede, Friedensvertrag\\\"' (line 7115) with 'an-āxšti- f. \\\"Unfriede\\\"' (line 4416).\"},\n  {\"src\": \"CHEUNG\", \"where\": \"s.v. *staH pp.358-360 and s.v. *HaišH pp.158-9\", \"stance\": \"contradicts\", \"note\": \"Under *HaišH 'to set in motion': 'OLD PERSIAN (+ *fra-) fraiš- \\\"to send forth\\\" = Kent: 164b ... NWIR (+ *fra-) Zaz. ristiš/risen- \\\"to send\\\", (old caus. ppp.) NP firistah/firestah \\\"angel; messenger\\\"'. Av. fraēšta- therefore belongs to *HaišH, not *staH.\"},\n  {\"src\": \"KNT\", \"where\": \"p.164b s.v. fraiš-\", \"stance\": \"contradicts\", \"note\": \"Kent puts OP fraišayam 'I sent forth' under the root aiš-/iš-, separate from stā- on p.210.\"},\n  {\"src\": \"PHD\", \"where\": \"p.34 s.v. frēstādan/frēstag\", \"stance\": \"partial\", \"note\": \"'frēstādan / frēstīdan, frēst- [SDRWN-(y)tn' ... plystʾtn', -ytn' | M pryst-d, N firistādan] send' and 'frēstag [plystkʾ | M prystg, (N firišta)] apostle, angel' — MacKenzie records the forms without deciding the root.\"}\n ]\n})\n\nnodes.append({\n \"id\": 7, \"lang\": \"Persian\",\n \"words\": \"ostâd «استاد»; ferestâdan «فرستادن»; parastîtan «پرستیدن»; pošt «پشت»; âštî «آشتی»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All five words are genuine *steh₂- descendants. (1) استاد < Classical NP ūstād < MP ʾwstʾt' / Manichaean ʾwystʾd /awestād/ 'master, craftsman' < Proto-Iranian *Hawastātas, cf. Avestan auuastāta- (Wiktionary); Horn no.83 already had 'ustād, ustaδ \\\"Meister\\\". aw. *avastāta- \\\"Vorsteher\\\"; phlv. ōstāt, arm. LW. ostat'. (2) فرستادن < MP frēstādan/frēstīdan (BMP plystʾtn') < *fra-stā-ta-, the causative-type past stem of fra- + stā- 'to make stand forth' > 'to dispatch'; cf. OP frastayam 'I send forth' and Skt. pra-sthāpayati 'sends off'. (3) پرستیدن < MP paristīdan 'to serve, worship' < *pari-stā- 'to stand around, attend on'; Nyberg: 'paristātan, paristītan parist- to worship, to adore ... < pari + stā-, v. ēstātan'. The derivative پرستار 'servant, nurse' = MP paristār 'maidservant'. (4) پشت < MP pušt < Proto-Iranian *pr̥štáh 'back' (Wiktionary), cognate with Av. paršta- and Skt. pṛṣṭhá-, i.e. *pr̥-sth₂-ó- 'standing forth'. (5) آشتی < MP āštīh 'peace' (MacKenzie: 'āštīh [ʾštyh | M ʾšty, N āštī] peace'; an-āštīh 'discord') < Av. āxšti-, with the regular MP simplification -xšt- > -št-; Old Armenian hašt is an Iranian loan of the same word. The extra word فرشته listed in the chart's script column is the one exception: it is MP frēstag 'angel, messenger', which Mo'in (Borhan p.1463) and Cheung derive from *fra-aišta- (root aēš-), not from stā-.\",\n \"derivation_fa\": \"هر پنج واژه به‌راستی از ریشهٔ *steh₂- می‌آیند. ۱) «استاد» از فارسی نو کهن ūstād، از فارسی میانهٔ awestād «استادکار، سرکارگر»، از ایرانی آغازین *Hawastātas، قس اوستایی auuastāta-؛ هرن (ص ۲۰، شمارهٔ ۸۳) نیز همین را می‌گوید: «aw. *avastāta- \\\"پیشوا\\\"؛ پهلوی ōstāt؛ وام‌واژهٔ ارمنی ostat». ۲) «فرستادن» از فارسی میانهٔ frēstādan از *fra-stā-ta- «واداشتن به پیش‌ایستادن» ← «گسیل کردن»؛ قس frastayam پارسی باستان و pra-sthāpayati سنسکریت. ۳) «پرستیدن» از فارسی میانهٔ paristīdan «خدمت کردن، نیایش کردن» از *pari-stā- «گرداگرد کسی ایستادن»؛ نیبرگ صریحاً می‌نویسد «< pari + stā-». «پرستار» نیز همان paristār پهلوی است. ۴) «پشت» از فارسی میانهٔ pušt، از ایرانی آغازین *pr̥štáh، هم‌ریشه با paršta- اوستایی و pṛṣṭhá- سنسکریت، یعنی *pr̥-sth₂-ó- «پیش‌ایستاده». ۵) «آشتی» از فارسی میانهٔ āštīh (مکنزی: āštīh «صلح»؛ an-āštīh «ناآشتی») از āxšti- اوستایی، با ساده‌شدن قاعده‌مند xšt > št در فارسی میانه؛ hašt ارمنی کهن وام‌واژهٔ همین است. تنها استثنا واژهٔ «فرشته» است که در ستون افزودهٔ نمودار آمده و معین (برهان، ص ۱۴۶۳) و چونگ آن را از *fra-aišta- (ریشهٔ aēš-) می‌گیرند نه از stā-. ادعای نورایی در مورد این پنج واژه درست است.\",\n \"sources\": [S[\"ostad\"], S[\"ferestadan\"], S[\"parastidan\"], S[\"posht\"], S[\"ashti\"], S[\"fereshte\"]],\n \"ref_check\": [\n  {\"ref\": \"BQT:1463\", \"status\": \"partial\", \"note\": \"Borhan p.1463 (vol.3, pdf p.256 via tools/ref_page.py) is the فرشته page; Mo'in's footnote there reads '... (سفیر) ایرانی باستان *fra-ista- (از fra- + aiš-) ... اوستا fraēšta ... بارتولمه ... ارمنی hreštak ... قس: فرستادن، استادن، نیبرگ ۷۹'. It supports the word but derives it from aiš-, and only cross-refers to فرستادن/استادن.\"},\n  {\"ref\": \"HRN:66\", \"status\": \"supports\", \"note\": \"Horn p.66 ends with no.298 'perest \\\"Verehrer, verehrend\\\", perestīden, perestār, perestiš' — the entry for parastīdan/parastār that Nourai cites.\"},\n  {\"ref\": \"HRN:182\", \"status\": \"supports\", \"note\": \"Horn p.182 no.817: 'firistāden \\\"schicken\\\". ap. *fra + √stā-, vergl. ai. pra + √sthā- (Causat.) \\\"entsenden, entlassen\\\"'; and no.819 'firištak ... Zu np. firistāden (No. 817), vergl. skr. prasthita- \\\"aufgebrochen\\\"' with the alternative from pra + √iš-.\"}\n ],\n \"consulted\": [\n  {\"src\": \"PHD\", \"where\": \"pp.14, 29, 34, 70 s.vv. āštīh, awestād, frēstādan, paristīdan, puštībān\", \"stance\": \"supports\", \"note\": \"'āštīh [ʾštyh | M ʾšty, N āštī] peace'; 'awestād [ʾwstʾt' | M ʾwystʾd, N ustād] master (craftsman)'; 'frēstādan / frēstīdan, frēst- ... send'; 'paristīdan, parist- [plst-ytn' | M pryst-, N parastīdan] serve, worship'; 'paristār [plstʾl | N parastār] maidservant'.\"},\n  {\"src\": \"NYB\", \"where\": \"Glossary s.v. paristātan\", \"stance\": \"supports\", \"note\": \"'paristātan [plstʾtn'], paristītan [plstytn'] parist- to worship, to adore ... < pari + stā-, v. ēstātan and cf. par-ēstātan; ... Paz. parastīdan parast- = NP.'\"},\n  {\"src\": \"CHEUNG\", \"where\": \"s.v. *staH (Middle Persian section)\", \"stance\": \"supports\", \"note\": \"'(+ *pari-) MMP pryst-, BMP plst- /parist-/ \\\"to serve (through worship); to worship\\\" || (+ *fra-) MMP pryst-, fryst-, BMP plyst- (SDRWN-) \\\"to send\\\" ... (+ *aua-) BMP ʾwstʾ- /ōstā-/ \\\"to set out\\\" ... Partic. perf. pass. BMP ʾwstʾt /ōstād/'.\"},\n  {\"src\": \"SYN\", \"where\": \"Buck p.1376 §20.14\", \"stance\": \"supports\", \"note\": \"'Av. āxšti-, NPers. āštī, prob. : ā(x)šta- ... cpd. of stā- (xštā-) \\\"stand\\\".'\"},\n  {\"src\": \"KLN\", \"where\": \"p.1223 s.v. post 'pillar'\", \"stance\": \"supports\", \"note\": \"'L. postis ... for *por-stis, lit. \\\"standing out\\\", cogn. with OI. pṛṣṭham, Avestic par-shti (dual), \\\"back\\\" ... See 1st pro- and state.'\"}\n ]\n})\n\nnodes.append({\n \"id\": 8, \"lang\": \"Old Persian\",\n \"words\": \"ava-stâ : set down, restore; ni-stâ, ništâ : command\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Both compounds are attested in the Achaemenid inscriptions and Nourai's gloss is Kent's, word for word. ava- 'down, away' + stā- in the causative stem *stāya- gives avastāyam 'I set down, put in place, restored' (Bisotun I 63, 66, 69 — Darius restoring the sanctuaries and pastures that Gaumāta had taken away). ni- 'down' + stā- gives a stem generalised as ništā- 'to enjoin, command': niyaštāyam (DB 3.91; DZe 8, 11; XV 23f.), niyaštāya (DSn 1; XPh 50; XV 21), nistāya (XPh 52). The -št- of ništā- is the regular Old Persian development of *ni-stā- with the -š- generalised from the forms in which *s stood after *i (Kent §140.VI). Semantically 'put down (an order)' > 'command', the same image as Latin dē-stināre and English 'lay down'.\",\n \"derivation_fa\": \"هر دو ترکیب در سنگ‌نبشته‌های هخامنشی گواهی شده‌اند و معنایی که نورایی داده عیناً از کنت است. ava- «فرو، پایین» + stā- در ستاک سببی *stāya- صورت avastāyam «فرونهادم، بازگرداندم» را می‌دهد (بیستون ستون یکم، بندهای ۶۳، ۶۶، ۶۹؛ داریوش چراگاه‌ها و نیایشگاه‌هایی را که گئوماتا گرفته بود بازمی‌گرداند). ni- «فرو» + stā- ستاک تعمیم‌یافتهٔ ništā- «فرمان دادن» را می‌دهد: niyaštāyam (بیستون ۳٫۹۱)، niyaštāya (DSn 1؛ XPh 50)، nistāya (XPh 52). خوشهٔ -št- در ništā- برآمد قاعده‌مند پارسی باستان است (کنت، بند ۱۴۰). از نظر معنایی «فرونهادن (فرمان)» ← «فرمان دادن»، درست همان تصویری که در dē-stināre لاتین دیده می‌شود. ادعای نورایی درست است.\",\n \"sources\": [S[\"pie\"]],\n \"ref_check\": [\n  {\"ref\": \"KNT:210\", \"status\": \"supports\", \"note\": \"Kent, Old Persian, Lexicon p.210 s.v. stā-: 'ava- + stā- \\\"set down, place, restore\\\": avastayam 1st sg. imf. (§214) DB 1.63, 66, 69. ni- + stā-, generalized ništā- (§117, §140.VI), \\\"enjoin, command\\\" ... niyaštāyam ... nistāya (§28.I, §140.III) XPh 52.' (KNT_full.txt lines 29215-29230)\"}\n ],\n \"consulted\": [\n  {\"src\": \"CHEUNG\", \"where\": \"s.v. *staH, Old Persian section\", \"stance\": \"supports\", \"note\": \"'*OLD PERSIAN: stā- \\\"to set, [med.] to stand\\\" || (+ *aua-) \\\"to set down, place, restore\\\" || (+ ni-) \\\"to enjoin, command\\\" = Kent: 210a' — Cheung copies Kent's glosses, the same ones the chart uses.\"},\n  {\"src\": \"BRT\", \"where\": \"AiW s.v. ava-stā-, ni-štā-\", \"stance\": \"supports\", \"note\": \"Bartholomae records the Old Persian forms in the same entries as the Avestan preverb compounds of stā-.\"},\n  {\"src\": \"TLM\", \"where\": \"Tolman, Ancient Persian Lexicon\", \"stance\": \"silent\", \"note\": \"grep of TLM.txt for 'avasta', 'nistaya' returns nothing usable (the OCR of the lexicon's s-section is broken).\"}\n ]\n})\n\nnodes.append({\n \"id\": 9, \"lang\": \"Avestan\",\n \"words\": \"sta-xra; sta-xma, sta-mba; vi-stâ-ka; stůra\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Item by item: (1) staxra- 'stark, fest; bes. vom Winterfrost: streng' is attested (Bartholomae; V 2.22, FrW 8) and Pokorny puts it under 'stāk-, stek- \\\"stehen, stellen\\\" ... Erweiterung von stā-' (IEW p.1011), together with Av. staxta- and Skt. stakati 'resists' — so this is the very item that justifies the root-box's third headword Stāk. (2) staxma- is NOT attested in Avestan: it is a reconstruction from MP stahm 'power, oppression', made by Horn (p.159 no.717: 'Also aus aw. *staxma-, vergl. staxra-'). The chart prints it without the asterisk. (3) stamba- is a different root: Skt. stambha- 'post, pillar; arrogance', Av. stembay- 'to prop', go back to PIE *stebh-/*stembh- (Pokorny p.1011-13), of which Pokorny says only 'Beziehung zu *stā- \\\"stehen\\\" ist möglich'. MacKenzie notes that MP stambag 'oppressive, obstinate' got its -h- by contamination from stahm ('stambag [sthmbkʾ (-h- < stahm)]'), i.e. the two words converged in Middle Persian but are etymologically distinct. Lumping sta-xma and sta-mba in one slot therefore mixes two roots. (4) vi-stā-ka is again Horn's reconstruction (p.205 no.920 'aw. *vistaka-, vergl. staxra-, phlv. staxmak ... phlv. v(i)staxv \\\"unverzagt\\\"'); Wiktionary instead reconstructs Old Persian *vistāhuva- for MP wistāx. Either way the second element is stā-. (5) stūra- 'umfangreich, stark, derb' is attested and Pokorny p.1009 puts it under 'st-eu-, st-euə- \\\"massiv, fest, dick, breit\\\" ... als \\\"standsicher, feststehend\\\"', with Skt. sthūrá-/sthūlá- and Av. stūra-; the connection to stā- is accepted but is itself an extension, not the bare root.\",\n \"derivation_fa\": \"مورد به مورد: ۱) staxra- «سخت، استوار، و به‌ویژه دربارهٔ سرمای زمستان: سخت» گواهی‌شده است (بارتولومه) و پوکورنی آن را ذیل «stāk-, stek- \\\"ایستادن، نهادن\\\"، گسترش‌یافتهٔ stā-» در ص ۱۰۱۱ می‌آورد، در کنار staxta- اوستایی و stakati سنسکریت؛ همین مورد است که سرواژهٔ سوم جعبهٔ ریشه یعنی Stâk را توجیه می‌کند. ۲) staxma- در اوستا گواهی ندارد؛ بازسازی هرن (ص ۱۵۹، شمارهٔ ۷۱۷) بر پایهٔ stahm فارسی میانه است و نورایی ستارهٔ بازسازی را نینداخته است. ۳) stamba- به ریشهٔ دیگری تعلق دارد: stambha- سنسکریت «ستون؛ گردن‌کشی» از *stebh-/*stembh- هندواروپایی است (پوکورنی ص ۱۰۱۱ به بعد) که پوکورنی تنها می‌گوید «پیوند آن با *stā- ممکن است». مکنزی یادآور می‌شود که -h- در stambag پهلوی از stahm به آن راه یافته، یعنی این دو در فارسی میانه به هم نزدیک شده‌اند ولی ریشه‌شان یکی نیست. ۴) vi-stā-ka نیز بازسازی هرن (ص ۲۰۵، شمارهٔ ۹۲۰) است؛ ویکی‌واژه به‌جای آن *vistāhuva- پارسی باستان را می‌نهد، ولی جزء دوم در هر دو stā- است. ۵) stūra- «ستبر، بزرگ، درشت» گواهی‌شده است و پوکورنی (ص ۱۰۰۹) آن را ذیل «st-eu-, st-euə- \\\"توپر، سخت، ستبر\\\"» می‌آورد. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [S[\"soturg\"], S[\"gostax\"]],\n \"ref_check\": [\n  {\"ref\": \"POK:1009\", \"status\": \"supports\", \"note\": \"IEW p.1009 (POK_03.txt leaf 250): 'Gr. st-eu-, st-euə- \\\"massiv, fest, dick, breit\\\" ... als \\\"standsicher, feststehend\\\" in ai. sthāvará- ... ai. sthūrá-, sthūlá- \\\"dick\\\" = av. stūra- \\\"umfangreich, stark, derb\\\"'.\"},\n  {\"ref\": \"POK:1011\", \"status\": \"supports\", \"note\": \"IEW p.1011 (POK_03.txt leaf 252): 'stāk-, stek- \\\"stehen, stellen; stehend, Ständer = aufrecht stehender Pfahl\\\"; Erweiterung von stā- \\\"stehen\\\"; stok-lo- \\\"fest\\\". Ai. stákati \\\"widersteht\\\", av. staxta- \\\"fest, stark\\\", staxra- \\\"stark, fest; bes. vom Winterfrost: streng\\\"; umbr. stakaz \\\"statutus\\\"'.\"},\n  {\"ref\": \"KLN:1508\", \"status\": \"supports\", \"note\": \"Klein 1966 p.1508 s.v. steel: 'These words prob. meant orig. \\\"something firm or hard\\\", and are cogn. with OI. stakati, \\\"resists\\\", Avestic staxta-, \\\"firm, solid\\\", staxra-, \\\"severe\\\" (said of the cold in winter). All these words are prob. traceable ult. to I.-E. base *sta-, \\\"to stand\\\". See state.' (KLN_1966.txt, page marker 1508 at line 36745 region)\"},\n  {\"ref\": \"HRN:205\", \"status\": \"supports\", \"note\": \"Horn p.205 no.920: 'gustāx \\\"kühn, frech\\\", bustax ... vergl. ustax ... aw. *vistaka-, vergl. staxra-, phlv. staxmak (Darmesteter, Ét. ir. 62); phlv. v(i)stax (Mēn.), arm. LW. vstah \\\"unverzagt\\\"'.\"}\n ],\n \"consulted\": [\n  {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 603 f. s.v. stak-\", \"stance\": \"supports\", \"note\": \"'stak- \\\"stehn, stellen; stehend, Ständer = aufrecht stehender Pfahl\\\". Erweiterung von sta- \\\"stehn\\\". Daneben *stek-. Ai. stákati \\\"pratighāte\\\" (Dhātup.), d. i. \\\"widersteht, stemmt sich\\\", av. staxta- \\\"fest, stark\\\", staxra- \\\"stark, fest ...\\\"' (WLD_Bd2_pages.txt line 40591 ff.)\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. stak-\", \"stance\": \"supports\", \"note\": \"'stak-. To stand, place. Zero-grade form *stək-; extension of stā-. ... 2. Suffixed form *stak-lo- in Germanic *stahla- in Old English stēli, style, steel (< \\\"that which stands firm\\\"): STEEL. [Pok. stak- 1011.]'\"},\n  {\"src\": \"BRT\", \"where\": \"AiW s.v. staxra-\", \"stance\": \"supports\", \"note\": \"'j. staxra- Adj. \\\"stark, fest\\\", inbes. vom Winterfrost \\\"streng\\\": V 2.22; FrW 8.1-2' (BRT.txt line 26551).\"},\n  {\"src\": \"IEC\", \"where\": \"Mann s.v. sthăuros\", \"stance\": \"supports\", \"note\": \"'sthăuros (sthour-) ... General sense of \\\"stiff, hard, strong, firm\\\" ... Av. cf. staorō m. \\\"draught-animal\\\" beside stavrō adj. \\\"strong\\\"; Per. cf. sutūr ... beside sitabr \\\"thick, coarse\\\"' (IEC.txt line 17563).\"}\n ]\n})\n\nnodes.append({\n \"id\": 10, \"lang\": \"Persian\",\n \"words\": \"estaxr «استخر»; setam «ستم»; gostâx «گستاخ»; sotorg «سُترگ»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"(1) استخر: Horn no.714 'sitaxr, istaxr \\\"Wasserbassin\\\" (eigentlich etwas \\\"fest\\\" sc. Ummauertes) ... aw. staxra- \\\"stark, fest\\\"; vergl. den Stadtnamen Staxr, Istaxr' — the Sasanian city Staxr near Persepolis and the common noun 'reservoir' are the same word, an *staxra- 'firm (masonry)'; the initial i-/o- is the usual NP prothesis before st-. (2) ستم < MP stahm 'power, oppression' (MacKenzie p.76 'stahm [sthm | N sitam] power, oppression; ~ag strong, oppressive'), Horn no.717 tracing it to aw. *staxma- beside staxra-, with the -xm- > -hm- > -m- reduction of Middle/New Persian (cf. the proper name Gustahm < *Vistaxma-). (3) گستاخ < MP wistāx 'confident, bold' (Horn no.920 phlv. v(i)stax; Wiktionary MP wstʾhw'), with the regular NP w- > g- (as wistardan > gustardan, wišādan > gušādan); the variant اُستاخ in the chart's extra column is the same word without the preverb's w-. (4) سترگ < MP sturg 'fierce; gross, coarse' (MacKenzie p.78 'sturg [stwlg | N suturg]'), from Proto-Iranian *stūrakah, a -ka- derivative of *stūra- = Skt. sthūrá- 'bulky, massive'; Horn no.715 'suturg, siturg \\\"stark, gross\\\". ai. sthūrá- ... phlv. sturg'. All four therefore descend from the Avestan node above exactly as drawn.\",\n \"derivation_fa\": \"۱) «استخر»: هرن (ص ۱۵۸، شمارهٔ ۷۱۴) می‌نویسد «sitaxr، istaxr \\\"آبگیر\\\" (در اصل چیزی \\\"استوار\\\" یعنی دیوارکشیده) ... اوستایی staxra- \\\"سخت، استوار\\\"؛ قس نام شهر Staxr/Istaxr»؛ یعنی شهر ساسانی اصطخر و نام عام «استخر» یک واژه‌اند، از *staxra-. ۲) «ستم» از فارسی میانهٔ stahm «زور، ستم» (مکنزی) و بنا بر هرن (شمارهٔ ۷۱۷) از اوستایی *staxma- در کنار staxra-؛ خوشهٔ xm > hm > m ساده شده است (قس نام گُستَهم < *Vistaxma-). ۳) «گستاخ» از فارسی میانهٔ wistāx «دلیر، بی‌باک»؛ ابدال w > g در آغاز واژه در فارسی نو قاعده‌مند است (گستردن، گشادن) و گونهٔ «اُستاخ» همان واژه بدون آن است. ۴) «سترگ» از فارسی میانهٔ sturg «درشت، ستبر» از ایرانی آغازین *stūrakah، ساخت -ka- از *stūra- = sthūrá- سنسکریت. بنابراین هر چهار واژه دقیقاً همان‌گونه که نمودار کشیده از جعبهٔ اوستایی بالا می‌آیند و ادعای نورایی درست است.\",\n \"sources\": [S[\"soturg\"], S[\"gostax\"]],\n \"ref_check\": [\n  {\"ref\": \"HRN:158-9\", \"status\": \"supports\", \"note\": \"Horn p.158 no.714 (istaxr) and no.715 ('suturg, siturg \\\"stark, gross\\\". ai. sthūrá- \\\"dick, breit\\\", sthūlá- ...; phlv. sturg'), p.159 no.717 ('sitem \\\"unrecht, Gewalt\\\". phlv. stahmak ... Also aus aw. *staxma-, vergl. staxra-').\"},\n  {\"ref\": \"HRN:205\", \"status\": \"supports\", \"note\": \"Horn p.205 no.920 for gustāx (quoted at node 9).\"},\n  {\"ref\": \"BQT:1099\", \"status\": \"partial\", \"note\": \"p.1099 is in Borhan vol.2, the س+ت region (Aryanpur cites برهان قاطع ۱۰۹۷ for ستون and ۱۰۹۷-۴ for استخر, so the neighbouring pages are indeed this family); the un-paginated vol.2 OCR does not allow the entry itself to be read.\"},\n  {\"ref\": \"BQT:1816\", \"status\": \"supports\", \"note\": \"Borhan vol.3 (pdf p.613 via tools/ref_page.py, printed ≈1817-1818, i.e. within a page or two of the cited 1816) carries the headword: 'گستاخ ... بنم اول، بروزن و معنی بستاخ است که بی‌ادب و دلیر و تند باشد' with 'گستاخ‌دست: کنایه از چابک‌دست و جلد و تندکار'. The cited page is the right entry; Mo'in adds no etymological footnote to it.\"}\n ],\n \"consulted\": [\n  {\"src\": \"PHD\", \"where\": \"pp.76, 78 s.vv. stahm, stambag, sturg\", \"stance\": \"supports\", \"note\": \"'stahm [sthm | N sitam] power, oppression'; 'stambag [sthmbkʾ (-h- < stahm) | M ʾstmbg, N sitamba] oppressive; obstinate'; 'sturg [stwlg | N suturg] fierce, contentious; gross, coarse'.\"},\n  {\"src\": \"ARY\", \"where\": \"Aryanpur, printed p.87 (pdf p.86)\", \"stance\": \"supports\", \"note\": \"Headword «استخر (نام شهری در استان فارس به چم \\\"مستحکم\\\")» with the Avestan/Old-Persian column and a reference to برهان قاطع — an independent modern Persian source for Horn's 'firm, walled' explanation.\"},\n  {\"src\": \"HUB\", \"where\": \"Persische Studien\", \"stance\": \"silent\", \"note\": \"grep of HUB.txt for 'staxr', 'sitem', 'gustax', 'suturg' returns no usable hit; Hübschmann's Part I follows Horn's numbering and does not re-treat these words.\"},\n  {\"src\": \"MON\", \"where\": \"Mo'in, Farhang\", \"stance\": \"silent\", \"note\": \"The two-volume abridgement on disk gives the meanings of ستم/گستاخ/سترگ but omits Mo'in's bracketed origin tags for them.\"}\n ]\n})\n\nnodes.append({\n \"id\": 11, \"lang\": \"Avestan\",\n \"words\": \"ratha-eštra\",\n \"verdict\": \"transcription_suspect\",\n \"error_in\": \"book\",\n \"book_prints\": \"ratha-eštra\",\n \"correct_form\": \"raθaē-štā- / raθaē-štar- (Bartholomae)\",\n \"derivation\": \"The etymology is right but the form is not one the sources know. Bartholomae (AiW) prints 'j. raθ'aē-star-, raδ-aē-štā-, raθaē-štā- m. \\\"Krieger, Kriegsheld\\\"', and adds that it is 'insbes. als Bezeichnung für den zweiten, den Kriegerstand' — the warrior estate beside the āθrauuan- (priests) and vāstrya- fšuyaṇt- (herdsmen). It is a locative compound: raθa- 'chariot' (loc. raθē) + the root noun -stā- 'standing', i.e. 'standing on the chariot', exactly matching Skt. rathe-ṣṭhā́- (RV) and Pokorny's own entry p.866 s.v. ret(h)- 'laufen, rollen': 'rathe-sthā- \\\"Krieger\\\" = av. raδaē-štā ds.'. The agent-noun variant raθaēštar- is what New Persian ارتشتار continues. The printed page (pdf 474, image at data/verification/sources/refs/ocr/BOOK/474.png) really does show 'ratha-eštra', so the extraction is faithful; the -ra is Nourai's own slip for the agent suffix -tar (he writes arteštâr correctly in the Persian node). A form *raθaēštra- is not attested.\",\n \"derivation_fa\": \"ریشه‌شناسی این گره درست است، اما صورتی که کتاب چاپ کرده در منابع وجود ندارد. بارتولومه در فرهنگ ایرانی باستان می‌نویسد: «raθaē-star-، raδ-aē-štā-، raθaē-štā- (مذکر) \\\"جنگاور، دلاور\\\"» و می‌افزاید که این واژه به‌ویژه نام طبقهٔ دوم، یعنی طبقهٔ ارتشتاران است، در کنار āθrauuan- (موبدان) و vāstrya- fšuyaṇt- (برزگران). ساخت آن ترکیب حالت دری (locative) است: raθa- «گردونه» (در حالت دری raθē) + نام‌ستاک -stā- «ایستنده»، یعنی «ایستاده بر گردونه»، هم‌ارز دقیق rathe-ṣṭhā́- سنسکریت در ریگ‌ودا. پوکورنی نیز در ص ۸۶۶ ذیل ret(h)- «دویدن، غلتیدن» همین را می‌آورد. صورت کارگزار raθaēštar- همان است که «ارتشتار» فارسی دنبالهٔ آن است. تصویر صفحهٔ چاپی نشان می‌دهد که خودِ کتاب «ratha-eštra» نوشته است؛ پس خطا از کتاب است نه از خوانش اسکن، و -ra لغزش نورایی به‌جای پسوند -tar است.\",\n \"sources\": [S[\"artesh\"]],\n \"ref_check\": [\n  {\"ref\": \"POK:866\", \"status\": \"supports\", \"note\": \"IEW p.866 (POK_03.txt leaf 101), s.v. 'ret(h)- \\\"laufen, rollen\\\"; roto- \\\"Rad\\\"': 'Ai. rátha- m. \\\"Wagen\\\", rathī- \\\"Wagenlenker\\\" ... rathesthā́- \\\"Krieger\\\" = av. raδaēštā ds.' The page number is exact.\"},\n  {\"ref\": \"MON:191\", \"status\": \"supports\", \"note\": \"Mo'in, Farhang, s.v. ارتش (MON_part1.txt line 9480 ff.): 'این کلمه بدین صورت اصالت ندارد و به صورت نادرستی از لغت پهلوی ارتیشتر ... و معنی آن لفظاً \\\"به گردونه ایستاده\\\" و توسعاً جنگاوری که با گردونه به کارزار می‌رود، استخراج شده است و درست آن بود که \\\"ارتشتار\\\" ... به کار می‌رفت (هرمزدنامه ص ۲۷۵)'.\"},\n  {\"ref\": \"AVG:237\", \"status\": \"supports\", \"note\": \"Jackson, Avesta Grammar: the compound section beginning on that opening reads 'Av. raθaēšta-, raθaēštar- (subst. + rad.) m. \\\"warrior standing in chariot\\\" = Skt. rathe-ṣṭhā́-' (AVG.txt form-feed leaf 293; with the file's stated offset this is printed p.238, i.e. Nourai's 237 is off by at most one page). Cf. also §249 'Declension of Av. raθaēštā- m. \\\"warrior standing in chariot\\\"'.\"},\n  {\"ref\": \"LEW:904\", \"status\": \"not_checked\", \"note\": \"The file held locally as LEW_1910.txt is in fact only a word index (entries like 'rota II 440'), not Walde's Lateinisches etymologisches Wörterbuch itself, and the 3rd-edition pagination Nourai cites is not available.\"}\n ],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"AiW s.v. raθaē-star-\", \"stance\": \"supports\", \"note\": \"'j. raθ'aē-star-, raδ-aē-štā-, raθaē-štā- m. \\\"Krieger, Kriegsheld\\\" ... A) insbes. als Bezeichnung für den zweiten, den Kriegerstand: āθrava ... vāstryō fšuyąs' (BRT.txt line 25082).\"},\n  {\"src\": \"AVG\", \"where\": \"Jackson §§249, 330, and the compound list\", \"stance\": \"supports\", \"note\": \"'§249. Declension of Av. raθaēštā- m. \\\"warrior standing in chariot\\\" = Skt. rathe-ṣṭhā- (part of its forms, however, are from the stem raθaēštar-)'; '§330. (ii) Declension of Av. raθaēštar- \\\"warrior standing in chariot\\\"'.\"},\n  {\"src\": \"POK\", \"where\": \"IEW p.866 and p.1006\", \"stance\": \"supports\", \"note\": \"Pokorny lists the compound both under ret(h)- (p.866) and among the *-sth₂-o- compounds of stā- (p.1006: 'ratha-sthā- \\\"auf dem Wagen stehend, kämpfend\\\" = av. raθaē-štā- \\\"Krieger\\\"').\"},\n  {\"src\": \"SYN\", \"where\": \"Buck §20.15 ARMY, p.1377\", \"stance\": \"silent\", \"note\": \"Buck's 'army' list gives 'Av. haēna-, spāda-; OPers. kāra-, haina-' and does not mention raθaēštar- or laškar.\"}\n ]\n})\n\nnodes.append({\n \"id\": 12, \"lang\": \"Persian\",\n \"words\": \"arteštâr «ارتشتار»; laškar «لشکر»\",\n \"verdict\": \"disputed\",\n \"derivation\": \"arteštār is right; laškar is not. (1) ارتشتار continues Avestan raθaēštar- through Middle Persian artēštār 'warrior', the name of the second Sasanian estate (artēštārān sālār 'commander of the warriors'); Old Iranian *raθa- lost its initial r- by dissimilation/prothesis in Middle Persian (*raθaēštār > artēštār), and New Persian took the word back from the Pahlavi books. The modern coinage ارتش 'army' of the Reza Shah period is a back-formation from it, wrongly analysed as having the suffix -dār (Wiktionary; Mo'in s.v. ارتش says 'this word in this shape is not authentic and was extracted incorrectly from the Pahlavi word artēštār ... the correct form would have been arteštār'). (2) لشکر does not come from raθaēštar-. Mo'in's own footnote on the page Nourai cites, Borhan-e Qate' p.1895, reports precisely this proposal and rejects it: 'آقای پورداود احتمال می‌دهند که این کلمه از اوستایی raθaēštar و پهلوی artēštār (رزمی، سپاهی) ناشی شده ... اما تبدیل ارتشتار به لشکر بعید می‌نماید' ('Mr Purdavud suggests the word comes from Avestan raθaēštar and Pahlavi artēštār ... but the change of arteštār to laškar seems improbable'). Current etymology derives NP laškar from MP lškr /laškar/ < Old Iranian *rakša-kara- 'protection-making' (root *rakš-, Skt. rakṣati 'protects', PIE *h₂lek-). Arabic عسکر ʿaskar, which the chart lists as an extra, is the Arabicised form of Persian laškar, as al-Jawāliqī states.\",\n \"derivation_fa\": \"«ارتشتار» درست است، «لشکر» نه. ۱) «ارتشتار» دنبالهٔ raθaēštar- اوستایی از راه فارسی میانهٔ artēštār «جنگاور» است، نام طبقهٔ دوم ساسانی (ارتشتاران‌سالار)؛ r آغازین در فارسی میانه افتاده و واکهٔ میانجی a- افزوده شده است (*raθaēštār > artēštār) و فارسی نو آن را از متون پهلوی بازگرفته است. واژهٔ نوساختهٔ «ارتش» در دورهٔ رضاشاه، چنان‌که معین در فرهنگ خود می‌نویسد، «بدین صورت اصالت ندارد و به‌صورت نادرستی از لغت پهلوی ارتیشتر استخراج شده است». ۲) «لشکر» از raθaēštar- نمی‌آید. خودِ حاشیهٔ معین در برهان قاطع ص ۱۸۹۵ — همان صفحه‌ای که نورایی به آن ارجاع داده — همین پیشنهاد را از پورداود نقل و آن را رد می‌کند: «اما تبدیل ارتشتار به لشکر بعید می‌نماید». ریشه‌شناسی امروزی «لشکر» را از فارسی میانهٔ laškar از ایرانی باستان *rakša-kara- «نگهبانی‌کننده» (ریشهٔ *rakš-، سنسکریت rakṣati، هندواروپایی *h₂lek-) می‌گیرد. «عسکر» عربی هم — که نورایی در ستون افزوده آورده — معرّبِ «لشکر» فارسی است، چنان‌که جوالیقی می‌نویسد. پس پژوهش امروزی پیکان «ارتشتار ← لشکر» را رد می‌کند.\",\n \"sources\": [S[\"lashkar\"], S[\"artesh\"]],\n \"ref_check\": [\n  {\"ref\": \"BQT:1895\", \"status\": \"contradicts\", \"note\": \"Borhan-e Qate' vol.3, printed p.1895 (pdf p.692 via tools/ref_page.py), Mo'in's footnote s.v. لشکر: 'معرّب آن عسکر ... انجمن‌آرای ناصری لشکر را از «لشکه» (قطعه، پاره) ناشی می‌داند، ولی با این وجه موجب پیدایش حرف آخر نامعلوم است ... آقای پورداود احتمال می‌دهند که این کلمه از اوستایی raθaēštar و پهلوی artēštār (رزمی، سپاهی) ناشی شده. بدین ترتیب: ارتشتر > رشتر = اشتر. اما تبدیل ارتشتر به لشکر بعید می‌نماید؛ کردی leškir (قشون)'. The page Nourai cites explicitly rejects his derivation.\"},\n  {\"ref\": \"BQT:97\", \"status\": \"not_checked\", \"note\": \"p.97 is in Borhan vol.1 (the ارتشتار entry under ا), available only as un-paginated OCR.\"},\n  {\"ref\": \"ARB:203\", \"status\": \"partial\", \"note\": \"al-Jawāliqī, al-Muʿarrab, s.v. العسكر (ARB_mo3rb.txt line 16995 ff.): 'قال ابن قتيبة: العسكر فارسي معرب. قال ابن دريد: ... هو لشكر بالفارسية وهو مجتمع الجيش'. This supports the Persian origin of Arabic ʿaskar (the chart's extra word) but says nothing about arteštār; the local OCR carries no page breaks, so p.203 could not be confirmed. The modern editor's note there argues the Arabic word is native ('والظاهر أن الكلمة عربية').\"}\n ],\n \"consulted\": [\n  {\"src\": \"MON\", \"where\": \"Mo'in, Farhang, s.v. ارتش\", \"stance\": \"supports\", \"note\": \"'... به صورت نادرستی از لغت پهلوی ارتیشتر و معنی آن لفظاً \\\"به گردونه ایستاده\\\" و توسعاً جنگاوری که با گردونه به کارزار می‌رود، استخراج شده است و درست آن بود که \\\"ارتشتار\\\" به معنی مفرد (و جمع آن ارتشتاران) به کار می‌رفت (هرمزدنامه ص ۲۷۵)' — supports arteštār, and dates ارتش as a modern coinage.\"},\n  {\"src\": \"BRT\", \"where\": \"AiW s.v. raθaē-star-\", \"stance\": \"supports\", \"note\": \"Gives the Avestan source of arteštār and its use for the warrior estate.\"},\n  {\"src\": \"SYN\", \"where\": \"Buck §20.15 ARMY p.1377\", \"stance\": \"silent\", \"note\": \"Buck's 'army' entry lists no Persian laškar and knows no connection with the chariot-warrior word.\"},\n  {\"src\": \"LKT\", \"where\": \"Lokotsch, Etym. Wb. der europäischen Wörter orientalischen Ursprungs\", \"stance\": \"silent\", \"note\": \"grep of LKT.txt for 'laschkar', 'lashkar', 'askar' finds no entry connecting either word with raθaēštar-.\"}\n ]\n})\n\nentry = {\n \"entry\": 0,\n \"root\": \"Stâ, Stha, Stâk\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *steh₂- 'to stand (up)'; Pokorny's headword 'stā- : stə-' (IEW 1004-1010), with the extension 'stāk-, stek-' (IEW 1011)\",\n \"note\": \"Pokorny p.1004 heads the article 'stā- : stə-, redupliziert si-stā-, erweitert stāi- : stī-, stāu- : stu- und stəu- \\\"stehen, stellen\\\"', and the two pages Nourai cites carry exactly the material his chart draws on: p.1008 §11 'mit n-Formantien: ai. sthā́na-, av. ap. stāna- n. \\\"Standort, Ort, Platz\\\", npers. sitān'; p.1008/9 section F 'st(h)āu- : st(h)ū- ... schwachstufig: ai. sthūnā \\\"Säule\\\", av. stūna, stunā \\\"Säule\\\"'; p.1009 'st-eu-, st-euə- \\\"massiv, fest, dick, breit\\\" ... av. stūra-'. The third headword 'Stâk' is a real but separate Pokorny entry, on p.1011 ('stāk-, stek- \\\"stehen, stellen\\\" ... Erweiterung von stā-'), which Nourai does cite correctly in node 9 (POK:1009,1011) but not in the root box. 'Stha' is not a third PIE variant: it is the Indo-Iranian/Sanskrit reflex sthā- (Skt. tíṣṭhati, sthātar-), the aspirate coming from *t + h₂. Watkins/AHD prints the root as 'sta-. To stand ... Contracted from *staə-' plus a separate 'stak-'. Root, language label and gloss are all correct.\",\n \"note_fa\": \"پوکورنی در صفحهٔ ۱۰۰۴ فرهنگ ریشه‌شناسی هندواروپایی خود سرواژه را چنین می‌آورد: «stā- : stə-، با دوتایی‌شدن si-stā-، گسترش‌یافته stāi- : stī-، stāu- : stu- و stəu- \\\"ایستادن، نهادن\\\"». دو صفحه‌ای که نورایی یاد کرده دقیقاً همان مطالبی را دارند که نمودار او بر آن‌ها استوار است: ص ۱۰۰۸ بند ۱۱ «با پسوند n: سنسکریت sthā́na-، اوستایی و پارسی باستان stāna- \\\"جایگاه، جا\\\"، فارسی نو sitān»؛ ص ۱۰۰۸-۱۰۰۹ بخش F «st(h)āu- : st(h)ū- ... با درجهٔ کاهش: سنسکریت sthūnā \\\"ستون\\\"، اوستایی stūna، stunā \\\"ستون\\\"»؛ ص ۱۰۰۹ «st-eu-, st-euə- \\\"توپر، سخت، ستبر\\\" ... اوستایی stūra-». سرواژهٔ سوم یعنی Stâk هم واقعی است ولی مدخل جداگانه‌ای در ص ۱۰۱۱ دارد («stāk-, stek- \\\"ایستادن، نهادن\\\" ... گسترش‌یافتهٔ stā-»)، و نورایی آن را در گرهٔ ۹ درست ارجاع داده است. اما «Stha» گونهٔ سوم هندواروپایی نیست؛ همان بازتاب هندوایرانی/سنسکریت sthā- است که h آن از حنجره‌ای *h₂ برخاسته. واتکینز در پیوست AHD نیز «sta-. To stand» و جداگانه «stak-» را می‌آورد. بنابراین ریشه، برچسب زبانی و معنا هر سه درست است؛ ادعای نورایی درست است.\",\n \"sources\": [S[\"pie\"]],\n \"ref_check\": [\n  {\"ref\": \"POK:1008\", \"status\": \"supports\", \"note\": \"POK_03.txt form-feed leaf 249 (printed 1008) carries §§10-11 of the stā- article, including 'ai. sthā́na-, av. ap. stāna- n. \\\"Standort, Ort, Platz\\\", npers. sitān' and the start of section F 'st(h)āu- : st(h)ū-'.\"},\n  {\"ref\": \"POK:1009\", \"status\": \"supports\", \"note\": \"POK_03.txt leaf 250 (printed 1009): 'schwachstufig: ai. sthūnā \\\"Säule\\\", av. stūna, stūnā \\\"Säule\\\" ... reduktionsstufig stəu-: gr. σταυρός \\\"Pfahl\\\" ... Gr. st-eu-, st-euə- \\\"massiv, fest, dick, breit\\\" ... ai. sthūrá-, sthūlá- \\\"dick\\\" = av. stūra-'.\"}\n ],\n \"consulted\": [\n  {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 603 ff. (cited by Pokorny as 'WP. II 603 ff.'), and II 611 s.v. stak-\", \"stance\": \"supports\", \"note\": \"The stak- entry is legible in WLD_Bd2_pages.txt line 40591: 'stak- \\\"stehn, stellen; stehend, Ständer — aufrecht stehender Pfahl\\\". Erweiterung von sta- \\\"stehn\\\". Daneben *stek-.'\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.vv. sta-, stak-\", \"stance\": \"supports\", \"note\": \"'sta-. To stand; with derivatives meaning \\\"place or thing that is standing.\\\" Contracted from *staə-' (line 997) and 'stak-. To stand, place. Zero-grade form *stək-; extension of sta-. ... [Pok. stak- 1011.]' (line 1001).\"},\n  {\"src\": \"KLN\", \"where\": \"p.1507 s.v. state\", \"stance\": \"supports\", \"note\": \"'fr. I.-E. base *st(h)ā-, \\\"to stand\\\", whence also OI. tíṣṭhati, \\\"stands\\\" ... OPers. and Avestic stā-, \\\"to stand\\\", Avestic hishtaiti, \\\"stands\\\" ...' — the same root with the same language spread.\"},\n  {\"src\": \"IEC\", \"where\": \"Mann, s.v. sthān-, sthăuros\", \"stance\": \"supports\", \"note\": \"'sthān- (stháno; sthānos) \\\"stand, set, set up, fix; standing, station, place\\\". Cf. WP II, 606 and sthā- with extns.'\"},\n  {\"src\": \"SYN\", \"where\": \"Buck §20.14 p.1376\", \"stance\": \"supports\", \"note\": \"Buck uses the same root for Av. āxšti-/NPers. āštī ('cpd. of stā- (xštā-) \\\"stand\\\"').\"}\n ],\n \"nodes\": nodes\n}\n\nout = {\n \"pdf_page\": 474,\n \"book_page\": 444,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [entry]\n}\n\npath = \"/home/sfmqrb/git/rishe/data/verification/page-474.json\"\nwith open(path, \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"wrote\", path, os.path.getsize(path), \"bytes\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-474.py",
 "description": "Build the verification JSON for page 474"
}
```


### [2026-09-14T02:56:40.489Z] TOOL RESULT

```
wrote /home/sfmqrb/git/rishe/data/verification/page-474.json 75082 bytes
```


## [2026-09-14T02:56:43.098Z] TOOL CALL #101: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -m json.tool data/verification/page-474.json > /dev/null && echo \"JSON OK\"; python3 tools/verify_check.py 474",
 "description": "Validate JSON and run verify_check"
}
```


### [2026-09-14T02:56:44.265Z] TOOL RESULT

```
JSON OK
nodes verified: 12/12
node verdicts: {'confirmed': 6, 'plausible': 2, 'transcription_suspect': 2, 'disputed': 2}
root verdicts: {'confirmed': 1}
ref checks: {'not_checked': 6, 'supports': 22, 'partial': 6, 'not_found': 1, 'contradicts': 1}
books consulted: {'supports': 35, 'contradicts': 3, 'partial': 3, 'silent': 6} | by book: {'BRT': 7, 'CHEUNG': 6, 'PHD': 6, 'KNT': 4, 'ARY': 3, 'MON': 3, 'NYB': 3, 'SYN': 3, 'AHD': 2, 'IEC': 2, 'HRN': 1, 'KLN': 1, 'TLM': 1, 'WLD': 1, 'HUB': 1, 'AVG': 1, 'POK': 1, 'LKT': 1}
```


## [2026-09-14T02:57:03.982Z] AGENT

Done. `data/verification/page-474.json` written; `verify_check.py 474` reports **12/12 nodes, 0 PROBLEM lines**.

**Page 474 (book p. 444) — root "Stâ, Stha, Stâk" [IE] "to stand", 1 entry, 12 nodes**

Verdicts: root `confirmed`; nodes — confirmed 6, plausible 2, disputed 2, transcription_suspect 2.
Ref checks: supports 22, partial 6, not_checked 6, not_found 1, contradicts 1. 18 different books consulted.

Disputed:
- **#6 (Avestan, `fra-aiš, fraěšta`)** — Av. *fraēšta-* "messenger" belongs to the root *\*HaišH* "set in motion" (Bartholomae; Kent 164b; Cheung s.v. *\*HaišH*), not to *\*steh₂-*. Mo'in's own footnote on BQT:1463 (the page Nourai cites in the daughter node) derives فرشته from *\*fra-ista-* "from fra- + aiš-". The other five items of the node (ava-stāta-, fra-stā-, par-šta/par-šti, ā-xšti-) are sound.
- **#12 (Persian, `laškar` «لشکر»)** — BQT:1895, Nourai's own citation, reports Purdavud's *raθaēštar > laškar* proposal and **rejects** it ("اما تبدیل ارتشتار به لشکر بعید می‌نماید"); current etymology is MP *laškar* < \**rakša-kara-* (PIE \*h₂lek-, Skt. rakṣati). `arteštâr` in the same node is confirmed.

Transcription_suspect:
- **#11 `ratha-eštra`** — `error_in: book`. Sources have only raθaē-štā- / raθaē-štar- (Bartholomae; Jackson §249/§330; Pokorny 866); \*raθaēštra- is impossible. The printed page does show "ratha-eštra", so the extraction is faithful — Nourai's own slip for -tar.
- **#4 Sogdian `` `st`wn` ``** — `error_in: extraction`. **The owner must fix this in `data/extracted/batch/page-474.json`: the book prints `` `st`wn `` (two backticks); the JSON has a spurious third trailing backtick.** The etymology is confirmed (Gharib no. 1689, p. 67: "ʾstʾwn … < OP stūnā, column, colonnade").

Plausible: #3 (adi-sta and tap-stana are unattested — Cheung puts MP ēst- under \*abi-staH, and تابستان is a MP formation tāb+-estān) and #9 (sta-xma is Horn's unasterisked reconstruction; sta-mba belongs to PIE \*stebh-/\*stembh-, a separate Pokorny headword).

Page image copied to `data/verification/sources/refs/ocr/BOOK/474.png`; 18 web pages archived via `fetch_source.py`. Note also: the local `LEW_1910.txt` is only a word index, not Walde's Latin dictionary, so LEW:904 is unverifiable; and Borhan vols 1–2 remain un-paginated OCR, so BQT:123/289/97 could not be located.
