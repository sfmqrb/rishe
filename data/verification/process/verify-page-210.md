# Verification process log — verify-page-210


## [2026-09-06T14:51:55.208Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 210 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-210.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-210.json. Write /home/sfmqrb/git/rishe/data/verification/page-210.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 210` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T14:51:56.391Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T14:51:57.269Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T14:51:57.284Z] TOOL RESULT

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


## [2026-09-06T14:51:57.819Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-210.txt"
}
```


### [2026-09-06T14:51:57.849Z] TOOL RESULT

```
1	=== PDF page 210 (book page 180) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Gwer 3, Gwere 2 : to swallow  (refs POK:474)
4	#1 (parent #0) [Avestan] refs=POK:474; KNT:199 | gar 3 : to swallow, devour ; jaraiti : swallows ; garah : throat
5	  #2 (parent #1) [Pahlavi] refs=HRN:207 | garŭk : throat
6	    #3 (parent #2) [Persian] refs=POK:474; BQT:1832; MON:3334 | galŭ «گلو» : throat ; gal «گل» : throat, neck, a narrow pass | extra: گلاویز | NOTE: Compare with "gal: mountain" from root "Gwer 4".
7	  #4 (parent #1) [Avestan] refs=KNT:199 | pati-gâra : a cup "for drinking" ☞Per 3
8	    #5 (parent #4) [Persian] refs=KNT:199 | pîyâleh «پیاله» : drinking cup or bowl | extra: پیغاله | NOTE: MON:862 lists "pîyâleh" as a cognate of Greek "piâle"
9	#6 (parent #0) [Old Persian] refs=KNT:199 | gar : to devour
10	  #7 (parent #6) [None] refs=None | 
11	#8 (parent #0) [Avestan] refs=POK:475; BQT:1807 | grîvâ : neck, also a hump ; grîvâ-pân : protector of neck, collar ☞Pa | NOTE: For sense development from "neck" to "hump" compare Indo-European roots "Men 3:to stand out" and "Mon:neck". Also compare with derivatives of root "Gwer 4".
12	  #9 (parent #8) [Persian] refs=SYN:233; BQT:1807 | garîveh «گریوه» : mountain, hilly land ; garîbân «گریبان» : collar
13	#10 (parent #0) [Greek] refs=AHD | bronxos : throat
14	  #11 (parent #10) [French] refs=None | 
15	    #12 (parent #11) [Persian] refs=MON:514 | bronšît «برونشیت»
16	  #13 (parent #10) [English] refs=None | bronchitis
17	#14 (parent #0) [Latin] refs=AHD | vorâre : to swallow
18	  #15 (parent #14) [English] refs=AHD | voracious, carnivorous
19	#16 (parent #0) [Indo-European] refs=IEC:265,305 | Gargelos, Gulgul : gargle
20	  #17 (parent #16) [Persian] refs=IEC:265,305; MON:1408 | ğerğereh «غرغره» : gargle ; xerxereh «خرخره» : throat ; ğolğol «غُلْغُل ، قُلْقُل» : boil, gargle
21	  #18 (parent #16) [Sanskrit] refs=IEC:265 | gargarah : gargle
22	  #19 (parent #16) [Latin] refs=AHD | gurges : throat ; gurguliô : windpipe
23	    #20 (parent #19) [English] refs=AHD | gargle
24	
```


## [2026-09-06T14:51:59.276Z] AGENT

I'll read the source JSON and reference infrastructure.


## [2026-09-06T14:52:00.631Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-210.json | head -200",
 "description": "Read source JSON for page 210"
}
```


## [2026-09-06T14:52:01.358Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T14:52:03.519Z] TOOL RESULT

```
{
    "pdf_page": 210,
    "book_page": 180,
    "entries": [
        {
            "root": {
                "name": "Gwer 3, Gwere 2",
                "lang": "Indo-European",
                "refs": "POK:474",
                "gloss": "to swallow"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Avestan",
                    "refs": "POK:474; KNT:199",
                    "words": [
                        {
                            "translit": "gar 3",
                            "gloss": "to swallow, devour",
                            "script": null
                        },
                        {
                            "translit": "jaraiti",
                            "gloss": "swallows",
                            "script": null
                        },
                        {
                            "translit": "garah",
                            "gloss": "throat",
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
                    "refs": "HRN:207",
                    "words": [
                        {
                            "translit": "gar\u016dk",
                            "gloss": "throat",
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
                    "refs": "POK:474; BQT:1832; MON:3334",
                    "words": [
                        {
                            "translit": "gal\u016d",
                            "gloss": "throat",
                            "script": "\u06af\u0644\u0648"
                        },
                        {
                            "translit": "gal",
                            "gloss": "throat, neck, a narrow pass",
                            "script": "\u06af\u0644"
                        }
                    ],
                    "script_extra": "\u06af\u0644\u0627\u0648\u06cc\u0632",
                    "note": "Compare with \"gal: mountain\" from root \"Gwer 4\".",
                    "quote": null
                },
                {
                    "id": 4,
                    "parent": 1,
                    "lang": "Avestan",
                    "refs": "KNT:199",
                    "words": [
                        {
                            "translit": "pati-g\u00e2ra",
                            "gloss": "a cup \"for drinking\"",
                            "script": null,
                            "see": [
                                "Per 3"
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
                    "refs": "KNT:199",
                    "words": [
                        {
                            "translit": "p\u00eey\u00e2leh",
                            "gloss": "drinking cup or bowl",
                            "script": "\u067e\u06cc\u0627\u0644\u0647"
                        }
                    ],
                    "script_extra": "\u067e\u06cc\u063a\u0627\u0644\u0647",
                    "note": "MON:862 lists \"p\u00eey\u00e2leh\" as a cognate of Greek \"pi\u00e2le\"",
                    "quote": null
                },
                {
                    "id": 6,
                    "parent": 0,
                    "lang": "Old Persian",
                    "refs": "KNT:199",
                    "words": [
                        {
                            "translit": "gar",
                            "gloss": "to devour",
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
                    "lang": null,
                    "refs": null,
                    "words": [],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 8,
                    "parent": 0,
                    "lang": "Avestan",
                    "refs": "POK:475; BQT:1807",
                    "words": [
                        {
                            "translit": "gr\u00eev\u00e2",
                            "gloss": "neck, also a hump",
                            "script": null
                        },
                        {
                            "translit": "gr\u00eev\u00e2-p\u00e2n",
                            "gloss": "protector of neck, collar",
                            "script": null,
                            "see": [
                                "Pa"
                            ]
                        }
                    ],
                    "script_extra": null,
                    "note": "For sense development from \"neck\" to \"hump\" compare Indo-European roots \"Men 3:to stand out\" and \"Mon:neck\". Also compare with derivatives of root \"Gwer 4\".",
                    "quote": null
                },
                {
                    "id": 9,
                    "parent": 8,
                    "lang": "Persian",
                    "refs": "SYN:233; BQT:1807",
                    "words": [
                        {
                            "translit": "gar\u00eeveh",
                            "gloss": "mountain, hilly land",
                            "script": "\u06af\u0631\u06cc\u0648\u0647"
                        },
                        {
                            "translit": "gar\u00eeb\u00e2n",
                            "gloss": "collar",
                            "script": "\u06af\u0631\u06cc\u0628\u0627\u0646"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": {
                        "text": "\u062f\u0631 \u0634\u0627\u0647\u0631\u0627\u0647 \u062c\u0627\u0647 \u0648 \u0628\u0632\u0631\u06af\u06cc \u062e\u0637\u0631 \u0628\u0633\u06cc \u0627\u0633\u062a - \u0622\u0646 \u0628\u0647 \u06a9\u0632\u06cc\u0646 \u06af\u0631\u06cc\u0648\u0647 \u0633\u0628\u06a9\u0633\u0627\u0631 \u0628\u06af\u0630\u0631\u06cc",
                        "poet": "H\u00e2fez"
                    }
                },
                {
                    "id": 10,
                    "parent": 0,
                    "lang": "Greek",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "bronxos",
                            "gloss": "throat",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
```


### [2026-09-06T14:52:03.553Z] TOOL RESULT

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


## [2026-09-06T14:52:07.257Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-210.json | sed -n '200,400p'",
 "description": "Rest of source JSON"
}
```


## [2026-09-06T14:52:08.322Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KNT','HRN','BQT','MON','SYN','IEC','AHD']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600]); print()\n\"",
 "description": "Check ref metadata"
}
```


### [2026-09-06T14:52:09.187Z] TOOL RESULT

```
                },
                {
                    "id": 11,
                    "parent": 10,
                    "lang": "French",
                    "refs": null,
                    "words": [],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 12,
                    "parent": 11,
                    "lang": "Persian",
                    "refs": "MON:514",
                    "words": [
                        {
                            "translit": "bron\u0161\u00eet",
                            "gloss": null,
                            "script": "\u0628\u0631\u0648\u0646\u0634\u06cc\u062a"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 13,
                    "parent": 10,
                    "lang": "English",
                    "refs": null,
                    "words": [
                        {
                            "translit": "bronchitis",
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
                    "lang": "Latin",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "vor\u00e2re",
                            "gloss": "to swallow",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 15,
                    "parent": 14,
                    "lang": "English",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "voracious, carnivorous",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 16,
                    "parent": 0,
                    "lang": "Indo-European",
                    "refs": "IEC:265,305",
                    "words": [
                        {
                            "translit": "Gargelos, Gulgul",
                            "gloss": "gargle",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 17,
                    "parent": 16,
                    "lang": "Persian",
                    "refs": "IEC:265,305; MON:1408",
                    "words": [
                        {
                            "translit": "\u011fer\u011fereh",
                            "gloss": "gargle",
                            "script": "\u063a\u0631\u063a\u0631\u0647"
                        },
                        {
                            "translit": "xerxereh",
                            "gloss": "throat",
                            "script": "\u062e\u0631\u062e\u0631\u0647"
                        },
                        {
                            "translit": "\u011fol\u011fol",
                            "gloss": "boil, gargle",
                            "script": "\u063a\u064f\u0644\u0652\u063a\u064f\u0644 \u060c \u0642\u064f\u0644\u0652\u0642\u064f\u0644"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 18,
                    "parent": 16,
                    "lang": "Sanskrit",
                    "refs": "IEC:265",
                    "words": [
                        {
                            "translit": "gargarah",
                            "gloss": "gargle",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 19,
                    "parent": 16,
                    "lang": "Latin",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "gurges",
                            "gloss": "throat",
                            "script": null
                        },
                        {
                            "translit": "gurguli\u00f4",
                            "gloss": "windpipe",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 20,
                    "parent": 19,
                    "lang": "English",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "gargle",
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


### [2026-09-06T14:52:11.060Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
```


## [2026-09-06T14:52:15.632Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport json\nd=json.load(open('../refs_online.json'))\nfor k in ['POK','KNT','HRN','IEC','SYN','BQT','MON']:\n    print('==',k); print(d[k].get('page_offset')); print('HINT:', d[k].get('lookup_hint'))\n\"",
 "description": "Page offsets"
}
```


### [2026-09-06T14:52:17.138Z] TOOL RESULT

```
== POK
POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
HINT: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
== KNT
leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
HINT: Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.
== HRN
leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
HINT: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
== IEC
TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
HINT: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
== SYN
leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
HINT: Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
== BQT
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
HINT: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
== MON
None
HINT: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).
```


## [2026-09-06T14:52:21.607Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: g\" POK_full.txt | grep -i \"er\" | head -40",
 "description": "Find Pokorny lemma"
}
```


### [2026-09-06T14:52:21.682Z] TOOL RESULT

```
3106:Root/ lemma: aiu-, aiu-\ "vital energy, vitality' derived from reduced Root/ lemma: g^ei-S 
5425:lemma: gen-1, gene-, gne- gnd-\ 'to bear (mother, father)' [origin of the old laryngeal g- > 
5928:From the reduced Root / lemma: ghsb"^-'. "to grab, take', derived Root/ lemma: aj/O-/ (exact 
7063:[see Root/ lemma: ghei-2. ghi-\ "winter; snow' 
7071:[common alb. gh- > d-] derived gr. x£Ai5u)v "swallow', therefore from Root/ lemma: ghel-: 
7161:lemma: arua {* herui): "intestines' derived from Root/ lemma: gher-5, ghor-na\ "bowels'. 
7245:lemma: ghei-2, ghi-, ghei-men-, *gheimn- : 'winter; snow'. 
7815:ek"- : water, river, derived from zero grade of Root / lemma: ghag^h- : young of an animal 
10307:Root/ lemma: b^a/6'^a: "beard' derived from the fussion of suffixed Root/ lemma: g^er-l, 
10319:fish' = Root / lemma: g^er-l, g^era- : " to devour; throat ' + zero grade of Root / lemma: 
10941:From Root / lemma: g^ady-: to sink, submerge, derived Root/ lemma: b'^au-l: b^J-: to hit. 
11316:From Root/ lemma: ghuoig"-: "to shine; star' derived Root/ lemma: b'^eig"-: "to shine' 
17987:Root / lemma: dem-, derna-: "to build; house' derived from Root/ lemma: ghei-2. ghi-: 
18005:Root/ lemma: denR-\ "to bite' derived from lllyrian derivative of Root/ lemma: gerrio'^-, 
18272:Root / lemma: deii(- : to look derived from Root / lemma: gher-3 und ghere-, ghre- : to 
23366:Two other roots, respectively Root/ lemma: ghesor-1, ghesr-: "hand' and Root/ lemma: 
23378:lemma: ghesto-2 {* gheus-): "hand, arm' are Baltic : Latvian pa-duse {zero grade) " armpit ' 
26888:lemma: ghei-2, ghi-, ghei-men-, *gheimn- : "winter; snow' 
29635:Root / lemma: gal-1\ "bald; naked' derived from Root/ lemma: koi-lo-\ "naked; miserable'. 
29822:Root/ lemma: gang-', "to mock' derived from the onomatopoeic duplication of Root/ 
31075:Root / lemma: gerdo^- 
31136:Root / lemma: ger-1, gere- 
31216:Root / lemma: ger-2 
31336:Root / lemma: ger-3 
31503:Root / lemma: ger-3\ "to turn, wind' : Root/ lemma: (s)ker-3\ "to turn, bend'. 
31670:Root / lemma: ger-4, grei- 
31704:Root / lemma: g(e)u-lo- : glowing coals derivded from Root / lemma: ker(9)-3\ to burn 
31759:Root/ lemma: geu- gsu- gu-\ to bend, curl; a kind of vessel probably derived from Root/ 
32159:Root/ lemma: ghsb"^-'. 'to grab, take' derived from the extended labials: gelet{h)-, glet{h)- 
32388:From Root / lemma: ghagha, gheghe, ghighi: "to cackle (of geese)' derived the new 
32698:Root/ lemma: gheigh-: "gland' derived from an extended Root/ lemma: gel-1\ "to curl; 
32806:the winter' [see Root/ lemma: ghei-2 . ghi-\ 'winter; snow' 
33008:Root / lemma: gher-1 
33052:Root / lemma: gher-2 
33078:Root / lemma: gher-3, ghre- : ghro- : ghra- 
33134:Root / lemma: ghers-1, ghres- 
33159:Root / lemma: ghers-2 
33175:Root / lemma: gherto- 
33412:Root/ lemma: ghoilo-s: foaming; turbulent; roaming, derived from Root/ lemma: g^el-l: 
33458:Root/ lemma: ghosti-s: stranger; guest, derived from Root/ lemma: ghds-\ to eat see
```


## [2026-09-06T14:52:22.731Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"474\\|475\" POK_full.txt | grep -i \"Page\" | head -20",
 "description": "Pokorny page 474/475"
}
```


### [2026-09-06T14:52:22.785Z] TOOL RESULT

```
39515:Page(s): 474-476 
39898:Page(s): 473-474
```


## [2026-09-06T14:52:25.682Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '39380,39530p' POK_full.txt",
 "description": "Pokorny 474-476 entry"
}
```


### [2026-09-06T14:52:25.738Z] TOOL RESULT

```
gr. popa f. ' food fed to livestock, dish, food' (= Latin *vora, whereof vorare), pop6(; (see 
above), pippcboKU) 'consume', hom. Opt. Perf. psppcbGoK;; ppcjopa, ppcbpn. Ppwcfk; 'dish, 
food', ppajTHp ' trencherman '; ppw- could have also originated from *gf- (Schwyzer Gr. 
Gr. I 361); Note: common lllyrian g"'- > b-. 

Maybe alb. bar' fodder, grass, food fed to livestock '. 

gr. papaGpov, hom. pEpsGpov, Arcadian ^spsGpov, SepsGpov 'gullet'; 



alb. zorre^ bowel ', PI. " intestines, entrails' ("*food fed to livestock, bowels ') from 
*g"erna, in addition zgurdhe {*dz-g'^orda) " intestines, entrails', anger(r), angurre{*a-n-g"or- 
na) ds., Jokl Mel. Pedersen 139 ff.; 

Note: 

Maybe alb. zo/r-e "bowel', PI. " intestines, entrails' didn't derive from Root/ lemma: g^er-l, 
g^era-: to devour; throat; but from Root/ lemma: gher-5, ghor-na\ bowels, [common alb. 
gh->z-\. 

Latin voro, -are {see above) " engorgement ', i/c»/'5^c» 'gullet', carni-vorus. 

Maybe alb. t/r/'hunger' a Latin loanword. 

Maybe alb. Geg {* g"'er- g"'ha) verza' (*throat), gill offish'. 

Old Irish tuarae^6\s\\, food' {*to-g"'r-liaR), mcymr. breuad^ dead worm ', breuan^ carrion 
crow ' (proto Celtic *bravato-, *bravana aiter Pick II'' 181; *bra= gr. ppoo-?); 

Old High German querdar^ sugarplum, bait' {*kver-t^ra-). Modern High German 'bait'; 
Old Icelandic krasi. ' tidbit ' ( *g'^re-so-)\ 

Balto Slavic *girdav\6 *gerd^ gobble' in: 

Lithuanian geriu, gerti, Latvian dzefu, o'ze?/ 'drink' (Baltic *^e/70 reshaped from Balto 
Slavic *gerd), ablaut. Lithuanian ger/sm. ' drinking, drink ' and g/rat " beverage, drink '; 
Kaus. Lithuanian girdyti, Latvian dzCrdtV water, soak '; 

Slavic *zbr-Q, zerti\v\ Old Church Slavic poz-tro, pozreti, sloven, pozrem, pozreti. Old 
Czech pozru pozfieti^ entwine; devour, swallow up, engulf, consume, gobble up ', besides 
Slavic *zerg, zbrat/"\n Czech zeru, zrati^ devour ', compare russ. pozratb ' eat up '; 

Balto Slavic participle Perf. Pass. *gTrta-\v\ Lithuanian girtas^ drunk, intoxicated ': Old 
Church Slavic pozrbtb ' devourer ' ( *gr-to-, compare Old Indie gJrna- ' devour'); 

Balto Slavic gurtia- n. "craw, throat' in: 

Old Prussian gurcle\. ' gullet ', Lithuanian gurklysm. 'craw, Adam's apple, projection of 
cartilage in the front of the throat '; 

Maybe alb. {*gurk-) ^/y/re "throat' a borrowing of Lithuanian gurklysxw. "craw, Adam's 
apple, projection of cartilage in the front of the throat '; 



Slavic *ghrdlo'c\. in russ.-Cliurcli Slavic ^ab/o 'tliroat', Serbo-Croatian grlo^ neck, gullet 
', poln. gardio^s., russ. gorio6s., besides Slavic *zbrdlo\v\ russ. -Church Slavic vozopi 
zerlom " crying voice ' and kir. zorlo " riverbed '; as well as Slavic *zerdlo in sloven, zrelo " 
jaw, gullet'; Old Russian zerelo^ embouchure, estuary '; 

Maybe alb. gre//e^deep place, abyss' a Slavic borrowing. 

Baltic -gara-' devouring ' in Lithuanian pra-garas^ abyss, hell', Latvian pragars^ 
wolverine ' (compare above Old Indie -gara-^ devouring ', gr. pop6(; ' voracious ', Latin 
carni-vorus' carnivorous '). 

2. With full or fractured reduplication: 

Old Indie ^a/ya/'a-/7 "gullet, whirlpool'; Intens. ni-galgalTti, ni-jalgulTti ^ 6eyours\ participle 
jargurana-, 

Latin gurgulid{-ur-as in Balto-Slavic) ' gullet, windpipe ', ^^/yes "(gullet =) whirlpool, 
whirl, deep pool ', gurgust/um {suffix after angustiae) " a small, mean dwelling, a hovel, hut 



Old High German quer(e)kela, querka' gullet ', Old Norse kverk {*g"'ergS) ^Gca\N, 
whereof Old Frisian querka. Old Norse kyrkia " strangulate '; 

Lithuanian gargaliuoju^ groan, gurgle '; after Specht KZ. 59, 110'' here Lithuanian 
gvrTgsti, gvarzdeti^ be hoarse ', Latvian gverg(z)det^ creak, babble, chatter '; s. above WH. 
1628; 

3. With formants -ua-: 

gr. Attic 5£pr|, Ionian 5£ipn, Lesbian Ssppcc, 5£pa, Doric 5npa " neck, nape ' ( *g'^er-ua); 

Note: [common lllyrian Albanian g- > o'-]. 

due to an h feminine *g"'(e)r7. *g''nua^ neck, throat area ' in: 

Old \v\6\c gnvat, Avestan grJva^ nape ', Latvian grJva^ embouchure, estuary; triangular 
land between rivers ', gnvis " tall grass'; 

Old Church Slavic gr/va ' mane' , gr/vbna 'coWar, neckband'. 

Maybe alb. krifa 'mane', grifshe' jay, shrew, lumberjack ' Slavic loanwords. 



4. As p'^extension presumably here *g'rogh-\ 

in gr. sppo^s, Aor. " devoured ', horn, ava-, Kara-ppo^Eis, ava-ppox£i<;, ppo^ai pocpnaai 
Hes., ppoxSoq m. 'gullet, throat'; Note: common lllyrian g"- > b-. 

Middle High German krage^ neck, throat, nape '; Modern High German Kragen ' collar ', 
Old Norse kragi^ neckwear, collar ', Middle English crawe, engl. craw^ bird or insect's 
crop; stomach ' (lengthened grade in addition Middle Low German kroch, kruch^ hostelry, 
inn ', Modern High German Krug\v\ the meaning ' inn '? meaning as in Latin gurgustium' a 
small, mean dwelling, a hovel, hut '); 

Old Irish bragae' neck, nape ' ( *gfg-nt-), acymr. abal-brouannou^ throat ' (actually ' 
Adam's apple'), mcymr. breuanV windpipe ' (proto Celtic *brag-)\ acorn. i6'/7a/7se'/7 "guttur', 
abret. Brehant-Dincat<^\. " gunu^receptaculi pugnae ', maybe from *brg-, Pedersen KG. 
100. Note: common lllyrian g""- > b-. 

With nasalization in addition perhaps gr. pp6yxo(; m., Ionian ppoyxir) " windpipe ', 
ppayxia, papayxia ' gill offish; trachea, windpipe ' seems in Vok. reshaped after ppayxaoj 
"be hoarse', ppaYXO(; " hoarseness ', that related to Old Irish brongide ^hoarse' (above 
103), but it must be separated from ppoyxot; to (: sppaxs " jangle, crack, shout ', Old Indie 
brmhatr barrire '? Johansson KZ. 36, 345). 

Note: 

Gr. ppayxia, papayxia ' gill offish' : alb. Geg {* g"er- g"ha) verza^ (*throat), gill offish' : 
Latvian barda^<^\\\ offish' : Latvian : M/'o'a "beard' [fa]; barzda {'6\a\.) "beard'. 
Root / lemma: g^er-l, g^ere-: " to devour; throat ' > Root/ lemma: b'^arH^a: " beard' 

5. With pure velar: gr. y£py£pO(; ppoyxoq Hes., yapyapscbv " uvula in mouth', yapyapi^w 
"gurgle' (: Armenian kerker/m 'become hoarse'?) perhaps through labialization after forms 
with yup- (yopyupn "subterraneous, underground jail, water pipe '), yet is previously ger- 
besides g"er- because of ge/- besides g^e/- is safe. 

References: WP. I 682 ff., WH. I 627 f., Trautmann 89 f., 98, Specht KZ. 59, 1 10, 1 . 
Page(s): 474-476 

Root / lemma: g''er-2, g^erQ-, g^erQu-, g^en- 

Meaning: heavy 

Material: Old Indie gurii-h' heavy, important, venerable ' (compounds ganyan. Sup. 

garistha-h), agru-' available, unoccupied; unmarried', gru-mustf-h' heavy handful ', 



garima^ heaviness' {*g"'er9-); Avestan gouru- (in compound) " lieavy '; npers. giran^ lieavy 
' {*grana-\ reshuffling after *frana-^i\}\\y, 

gr. papu(; " heavy ', papuvw "beschwere", papo^ n. " heaviness'; Note: common lllyrian
```


## [2026-09-06T14:52:31.685Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '39330,39385p' POK_full.txt",
 "description": "Start of POK gwer-1 entry"
}
```


### [2026-09-06T14:52:31.734Z] TOOL RESULT

```
through hybridization with onomatopoeic words with Germanic k- in aniaut. 

With d^^-extension perhaps here (see above gall, bardus) Armenian kardam " raise the 
voice ', Lithuanian gefdas^c\arc\or, message, official notice, communication transmitted 
through a messenger ', /s-g/rst/" accepted to hear ', g/rdet/^ hear', garsas " clangor ', Old 
Prussian gerdaut^ say', Latvian dzirdet^hear', MiJhlenbach-Endzelin I 552 with Lithuanian 

maybe alb. {* garsas) gerthas > theras "scream' : Lithuanian garsas " clangor '. 

gr. 5£ipic(v Aoi5op£Ta0ai. IKaKUivzc;, SsipsToi Aoi5opoi. oi auToi; Sspiai Aoi5opiai Hes. (i.e. 
probably 5r|p- from *g"er-s-); 

Old High German queran^siOih'. 



Compared with the similar onomatopoeic words ger-, gar- a sure separation is not 
everywhere possible; however, the concept of high utterance is unmistakeable here under 
^"'er- combined words, not surely to be attached therefore up to d^-extension. 

References: WP. I 686 f., WH. I 583, 619 f., Trautmann 88 f. 
Page(s): 478 

Root / lemma: g''er-1, g^era- 
Meaning: to devour; throat 

Material: 1 . Old Indie girati, gilati, grnat/' devours' (Fut. garisyati, participle gJrna-^ devour'; 
-^//-(in compounds) " devouring ', -gara-6s. {aja-gara-^ devouring nanny goats , boa ' :gr. 
5r|MO-p6po(;, Latin carni-vorus, gr. pop6(; " voracious ') Note: common lllyrian g"- > b-, 
gara-h^ drink, beverage, liquid which is swallowed to quench one's thirst, draught, potion', 
P'a/a-/7 'throat' (perhaps to parallel root *^(^";ie/- "intertwine, entwine; devour, swallow up, 
engulf, consume'), tuvi-gri-, -gra- " devouring a lot '; 

f\yes\.av\ Jaraiti^ gulp, sip, swallow, send down the throat', -gar(\n compounds) " 
devouring ' {aspd-gar-'\r\orse v.'), f. PI. 'throat, neck ', npers. gu/u^ throat', Avestan 
garaman- 'throat, neck '; 

Maybe Latin gula^ throat '. 

Armenian /re^'dish, food, food fed to livestock ', kur6s. {*g"'ur-), eker^ ate ', kokord 
'throat' (also krcum ' gnaw '?? Pedersen KZ. 39, 427); 

alb. ngrane^ eaten '; 

Note: 

alb. hangra'\ ate' : Armenian eker' ate ' (common Avestan Greek Armenian aorist prefix); 

From there alb. Geg. hanger' to eat ', ha' to eat '. 

gr. popa f. ' food fed to livestock, dish, food' (= Latin *vora, whereof vorare), pop6(; (see 
above), pippcboKU) 'consume', hom. Opt. Perf. psppcbGoK;; ppcjopa, ppcbpn. Ppwcfk; 'dish, 
food', ppajTHp ' trencherman '; ppw- could have also originated from *gf- (Schwyzer Gr. 
Gr. I 361); Note: common lllyrian g"'- > b-. 

Maybe alb. bar' fodder, grass, food fed to livestock '.
```


## [2026-09-06T14:52:41.750Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==215 || NR==214 || NR==216' KNT.txt | head -120",
 "description": "Kent p.199 area"
}
```


### [2026-09-06T14:52:43.516Z] TOOL RESULT

```
5-6).
Dérayava'u- sb. ‘Darius’ (I, son of Hystaspes, king 522-486 ».c.; IT, son of Artaxerxes I, king 426-04 в.с.): Elam da-ri-a-ma-u-ts, Akk. da-ri- ja-mus, Gk. Дарєюѕ (by haplology for *Aapetaios; Keiper, Acta Sem. Phil. Erlangen, 1.253). From pAr. *dháragat-, pic. to root in OP dar- (§162, §240), + pAr. *yasu asn. ‘the good’ (5158.1), see OP vau-: ‘He who holds firm the good’ (Hz. Arch. Hist. Iran 40, ApI 255, 267, takes as hypocoris- tie of *ddraya-vahu-manah- ‘Holder of Good Thought’; this is rejected by Nyberg, Rel. 361).
Dérayavaus nsm. (8118.IV, 5124.2) DB 1.1, 4, 6,9, 11, 13, 171, 201, 24, 27, 35, 44, 48, 61, 71, 73, 81, 83, 90; 2.1, 5, 8, 11, 13f, 18, 29, 37, 42f, 49, 57, 64, 70, 78, 91, 92; 3.1, 9, 10f, 19f, 21, 29, 40, 49, 53, 54, 64, 69, 75, 76, 83; 4.1, 2f, 31, 33, 36, 40, 43, 45, 50, 58, 57, 59, 611, 67, 69f, 72, 76; 80, 86, 88; 5.1, 14, 18, 20, 30, 34^; DBa 1, 41,9, 14; DPa 1;
190 OLD PERSIAN
DPb; DPd 4f, 5, 12; DPe 1, 5f, 19; DPh 1, 3f; DNa 8, 15, 30f, 40, 47t; DNb 5; DSa 1, 3; DSb 1f°; DSc; рва 1°, 3°; DSe 8, 14, 30f°, 41^, 49f; DSf 5f, 8, 55; DSg 1, 3; DSi 1, 3; DSj 1, 2, 5; DSk 1, 3f; DSI 1; DSm 1, 3°; DSn 1°; DSo 2f; D8q 2; DSt 7°, DSy 1; DZa; DZb 1; DZe 4, 7; DE 12; DH 1, 8; XPc 11; XPf 16f, 30, 38; XPg 6; XSa 2; XV 17; D*Sa 2; D'Sb 1°, 3°; Аа 3; Wa 21; Wb 1; We 2; Wd 2; SDa; SDb. Dérayavahaus as nsm. XPf 25 (851; Lg. 9.39).
Dérayavaum asm. DPd 2; DNa 5; ОХЬ 4; DSe 5^; DSf 3f; DSn 2; DSp 1f°; DSt 5°; DZe 3; DE 7; XPf 221; D'Sa 2f.
Dérayavahaus gsm. (8118.1V, 5124.2) DB 3.58f; DPe; DPd 10; DPi; DNe 1f; DNd 1; DZc 3; XPa 9f; XPb 19; XPe 8f, 14; XPd 13; XPe3; XPf 13f, 17; XPh 11; ХР}; XPk; X8e 2°; XE 19; XV Mf; A!Pa 16. Dérayavaus as gsm. XPf 28 (851; Lg. 9.39); (8313.11) A’Sb, A'Sd 2, A?Hb, A?Pa 13f, 14, 17, 18. Dérayavausahya gsm. (557) АЧ, A’Sa 1, 1f, 2f, 3; A?8c 0 bis; A?He 9f, 10 (as nom., 8813.1), 18, 14 (as nom.). Dàrayavasahyà gsm. (852.VI, $57) А?На 2, 2°, 4, 4°.
daru- sb. ‘wood’: Av. déuru-, Skt. dáru-, ef. Gk. доро ‘spear’. düruv (§181) nsn. DSf 41, in phrase asd атир ‘ebony’, lit. ‘stone wood’ (§308.- nl), so called because of its hardness; but also probably аз@ because of the assonance translated Akk. aban ‘stone’, ef. Hebr. eben ‘ebony’, Gk. Веро, from Egyptian hbnj ‘ebony’ (J. Duchesne- Guillemin, BSOS 10.925-7 [1942], noting that acc. to Hdt. 3.97 the Egyptians paid a tribute of ebony logs to the Persian King). Not to be normalized dārwa to root !dar- and the phrase taken as ‘copper’ (Scheil 21.30; Kent JAOS 51.208, 53.18- 9), or as ‘iron’ (Ву. BSLP 30.1.60; who also sug- gests that dáruva may be an adj. referring to some kind of tree); not asé + instr. déruv ‘window frames of wood’ (König, Burgbau 64-5); not asd süruva ‘lead’ (Hz. Ар] 299), to Av. srva- ‘lead’ (Bthl. AIW 1649), for the slight traces do not con- firm initial s". — [dár|uv asn. DSf 51 (so Hinz, Orientalia, soon to appear; not {23mal}uv, see Lex. S.V.).
darga- adj. ‘long’: GAv. daraga-, LAv. daroya-, NPers. dër, Skt. dirghd-, pIE *dlgho-, ef. Ck. dodexés, Lt. longus (881, $68, $101, $148.11, VI). dargam asn. as adv. ‘for a long time’ DB 4.56, 15.
dartana- (or perhaps zarlana-, with Med. 2) sb. ‘anger’: Av. zarafa- ‘enraged’, Skt. hrnité ‘ig angry’ (§34, §147.V, $238). [dalrtanaya lsn. DNb 13f (conj. of Kent, JNES 446-7; ef. §238.n1).
darš- vb. ‘dare’: GAv. dora&- ‘deed of vio- lence’, Skt. dhrs-noti ‘dares’, NEng. dare (570.11, $117). See also Dädarši-, darfam. adaršnauš imf. $80, §84, §210.1, $228.11) DB 1.53.
darsam adv. ‘mightily’: asn. to adj. darsa- ($143.1), to root dar§- (against this, Hz. Apī
135-6). DB 1.50 (MB Gr. $366; wrongly Kent, ·
JAOS 35.336-42); 4.37; DNb 14, 15, 50.
dasta- sb. ‘hand’: Av. zasta-, N Pers. 0051, Skt. hdsta-, pIE *ghosto- (§88, $116, $145). See also dastakarta-. даѕіауа ism. DR 4.35. dastaibiya idm. (§189) DNb 41.
dastakarta- adj. ‘handmade’: dasta- + pte. .
karta- (5160.10), to kar- ‘make’. [dasta|kartam (restored after the Elam., Wb. ZDMG 91.85, 
Hz. Ap! 136-8) nsn. as sb. ‘handiwork’, DSe 42.
Daha- adj. ‘Dahian’; pl., a province of the Persian Empire: АКК. da-a-an, Gk. Aaa (§76.V; Lg. 18.298; Hz. AMI 8.72). Dahà npm. XPh 26.
dahyu- sb. ‘land, province, district’: GAv. :
daltyu-, LAv. dahyu- daiphu-, NPers. dih ‘village’, Skt. ddsyu- ‘stranger, demon’ (5124.2, $153.IV, $166). Decl., 5183.1. See also visadahyu-.
dahyaus nsf. AmH 5, 8f (as Isf. §814b); DB 1.59; 2.28, 58, 59, 72; 3.9, 11, 20, 28, 66, 75, 79f; 5.4, 13f, 29f; DPd 6. dahydus-maty DB 4.39. dahyüum asf. (853, $72) AsH 8, 11, 13; DPd 15, 18; DNa 53. dahydvam (8124.VY) XPh 88, 58f. dahyaud (dahyuvd Wb.) isf. (M8, §124.2, 8137) DB 1.34.
dahyàva прі. ($124.7) DB 1.18, 17, 18, 28, 41; 2.6°; 4.33; DPe 7, 14; РМа 17, 39; DSe 15f, 32f; DSm 5°; XPh 15. dahyáva apf. DB 1.21, 47, 67; 4.92, XPh 31,35. dahyünüm gpf. DB 1.2; DBa 3; DPa 4; DPe 3; DNa 10; DSb 6f; DSe 9°; DZb 2{°, DZc 5; DE 15; XPa 7f; XPb 15; XPc 7; XPd 10f; XPf 10; XPh 8f; XSc 2°, ХЕ 15; XV 111; А:Ра 11f°; A’Sc 3f; Wb 5; We 6; Wd 6. dahyüv- näm (523.11) РР} 2; DH 1f. dahyusued lpf. DB 1.35.
DHum (842) asf. DSf 58; DSj 6°. DHyaum (553) А2Рә 26. -DHnám gpf. DSa 2; DSd 1; DSf 6; 056 1^; D8i 4°; DSk 2; РӘ 2°. DHyünam
LEXICON
DSy 2; ХР); АЧ; D'Sb 1; A’Sa 1; А84 1; А?На 1°; А?Не 8; A?Pa 11.
idi- vb. ‘see’: Av. *dá(y)- ‘see’ (Bthl. AW 124), NPers. diddn, Skt. dhi- ‘think’. didzy 2d sg. mv. (865, $129, 5209, $218.II, $237.1) DNa 41; DNb 57.
*di- vb. ‘take by force (a thing from a person, 2 acc.), deprive (a person of a thing, 2 acc.)’: Av. zinditi ‘harms’ (zyà-, Bthl. AYW 1700), Skt. jináti ‘oppresses’, jdyati ‘conquers’ ($88), ef. Gk. Bia ‘violence’. айтат Ist sg. imf. (5210.1, $226.II) DB 1.59. айта imf. (5210.1, $228.IT) DB 1.44f, 46, 66. ditam asm. past ріс. pass. (82421) DB 1.50. |
-di- enel. pron. ‘him, them’, usually with masc. antecedent: Av. di- (Bthl. AiW 684); start- ing by wrong division of pasdvad-im etc., where -im is acc. to *is, Lt. is, and extended (§195.II; Caland, KZ 42.173; Mt. MSLP 19.535, Gr. $166); on competition with pron. -%i-, see Bv. Gr. 645.
-dim asm. (5195.1) in pasdva-dim (with fem. an- tecedent) DNa 33; anu-dim DNb 16, 18; avabá- dim DNb 17; hau-dim ВЕ 32.
-diš apm. (8195.1) in tyà-di$ DB 1.65 (with collective sg. masc. antecedent); nazy-di& DB 4.78, 18; paribarüh?-di$ DB 4.74; vikanah*-dis DB 4.77; avafà-di$ DB 5.17, 33; ava-di$ DNa 21, DSe 20°, XPh 19; 00-015 DNb 46f (with nt. antecedent); hau-di$ DSs 6° (with antecedents of different genders). Written as separate word in drauga diš DB 4.34 (with fem. antecedents); pasdva diš DB 4.35; avaba diš DB 4.36.
daiy DB 5.11, as separate word, properly vi? with wrongly inserted divider following; read viy- ататда with Wb. ZfA 46.55, see under mard- (not apm. with Kent, JAOS 62.278; not gen.-dat. sg. with Wb. KIA 73n, Bv. Gr. $845, Gray AJP 53.69).
-diy emphatic encl. particle: Av. zi, Skt. hi, Gk. encl. -xı in vai-xı ‘yes indeed’, of-xé ‘not at all’, pIE *ghi ($88, 5191.1). ufraštā-diy DB 4.69 (JAOS 35.351-2; not pron. apm., with Bv. BSLP 31.2.63-4, Gr. $845); hardly vasnd-[dily XPg 7f (despite Lg. 9.320; see under apiy); 7‘va-diy A’Sd 3 (JAOS 51.229).
didà- sb. ‘wall, stronghold, fortress’: N Pers. diz, pIE *dhióhà-, cf. Skt. dehi- ‘wall’, Gk. réxos,
191
NEng. dike, ditch (676.011, 588, §148.IV, 5166). Cf. also paradayadàm. й nsf. DB 1.58; 2.39, 44; 3.61, 72; DSe 46; DSf 42. didäm asf. DB 2.78; DSe 48°; DSf 54.
dipi- sb. ‘inscription’: Elam. tup-pi, Akk. duppu (5152.1): borrowed from Sumerian dup- (Ву. Gr. §282; hardly contamination of Jran. *ripi- = Skt. lipi- ‘smearing, writing’, with Sum. dup-, as taken by Pisani, Riv. Stud. Or. 14.320, as Skt. lipi- ‘writing’ indicates writing with ink rather than engraving on stone) 4:4] nsf. DB 4.90, 91f. dzpim asf. DB 4.42, 48, 70, 73, 77, 89; XV 22, 24. dipiyd lsf. (§179.V) DB 447.
dug- vb., see hadugá-.
Dubála- sb. ‘Dubala’, a district in Baby- lonia: Elam. du-ib-ba--- ($6, $107). Dubala пет. DB 3.79.
dūra- adj. ‘far (in time or space)’: Av. düra-, . NPers. dür, Skt. dürd- (5148.1). See also dü
rada&a, duvaista-. dürau lsn. as adv. ‘afar, far away, far and wide’ (GAv. düiré, LAv. duire, Skt. d'ré; $65, 6191.111) DNa 44. duraty apiy DSe 11, DZe 6, DE 18, XPa 9, XPb 18, XPe 8, XPd 13, XPf 13, XPh 10, XE 18, XV 14, A'Pa 14f°, A’He 17. düraiapiyy DNa 12, dürayapiy DNa 46 ($18, $136).
duradasa adv. ‘from afar’, with preceding hacá: dūra- + adv. -dä asin отада + abl. -ša asin avada&a (§135, 5191.1; ЈАО 54.37).  DSf 23.
duruj- vb. ‘lie, deceive’: Av. druj- ‘le’ (draog-, Bthl. AYW 767), pres. druZasti, sb. druzé ‘principle of evil, devil’, Skt. drúhyatí ‘deceives’, Gm. trügen, pIE *dhrugh- (876.111). See alsodrauga-. adu- rujiya imf. (§101, $103.IV, $113, 5128, 4132.1, 2, 3, $214, 5228.11) DB 1.39, 78; 3.80; 4.8, 10f, 13, 16, 18, 21, 24, 261, 29; DBb 2; DBc 2; DBd 2; DBe 3f; DBf 1; DBg 2; DBh 2f; ОВ! 2f; DB} 2f. adurujiyasa" 3d pl. imf. ($214, §218.1, $232.III) DB 4.34f. duruxiam nsn. past pte. pass. ($103.IV, $122, $128, 8132.1, 3, $242.I) DNb 52, 5f; asn. DB 4.44f, 49f.
duruva- adj. ‘firm, secure’: Av. drva-, Skt. dhruvd-; deriv. to root in OP ‘dar- ($122, $128, $150). durwä nsf. DB 4.39.
duvatsta- adj. ‘very long, very far’: superl. to dūra- ($156.IIL, §190.11 $191.0; МВ Gr. $275), ef. Skt. davisthd- with slightly different formation.
192 OLD PERSIAN
duvais[ta]m asn. as adv. ‘for a long time’ DPe 23 (cf. remarks s.v. hyà).
duvara- sb. ‘door’: Av. dvar-, Skt. dhvar-, Gk. дора, Lt. forés, NEng. door, Lith. dvéras ‘court- yard’, pIE *dhuor- dhur- and its extended forms *dhyoro- etc.; see also duvarfi-. duvarayd-maiy lsn. ($186) DB 2.75; 89f.
duvari- sb. ‘portico, colonnade’: duvar- ‘door’ + varði- ‘cover, protection’, to root var- ‘cover’, with haplology ($34, $129, $152.IV, §160.Ia; ВЫ. AIW 766). duvarfim asm. XPa 12.
duvitdparanam adv. ‘one after the other, in succession’, a meaning agreeing with Elam. Samak- mar ‘ex ordine’: duvità ($191.11, $204.IT), MPers. dit ‘one or other of two’ (Bthl., quoted by Tm. Lex. 102), ef. OP duviliyam ‘a second time’, Skt. 0015 ‘twice’, Lt. bis, + paranam ‘before, previ- ously’ (Tm. 1.е., and Vdt. Stud. 1.8). This is better than Tm.’s "long aforetime', adv. duvità ong’, GAv. дайа, Skt. dvità (cf. OP duvaistam), + paranam (as above); also than KT's duvità- parnam ‘in two lines’, contaming the cognate of Skt. parnd- ‘wing’ (supported by Wb. ZDMG 61.724-5, KIA 10-1, and by Hz. AMI 1.112n). DB1.10; DBa 17.
duvitiya- adj. ‘second’: GAv. daibitya-, LAv. bitya-, Skt. dvitiya-, pLE *dyitiio- (676.11, 51441, 5204.1). See also duwilàáparanam. дилат, asn, as adv. ‘a second time’, DB 2.87f, 57, 3.77; as inner obj., ‘a second (uprising), DB 3.24 (not duvitiya-ma udapalalà ‘was second to rise up from me’, as Bthl. AiW 964 takes it, since udapatatà nowhere else takes an expression of the person against whom uprising is made).
duš- insep. prefix ʻi: Av. dui-, Skt. dus-, Gk. dve- ($76.Ш); in dušiyāra-, duskarta-.
dusiyara- sb. ‘evil year, bad harvest, famine’: duš- + yar- ‘year’ made thematic, Av. ydr-, Gk. ёра ‘season’, NGm. Jahr ($140.VIT, $143.IT). dušiyāram nsn. DPd 19. dudiyard absn. DPd 17.
| du$karia- ad). ‘ill-done’, opposite of naiba- (Hz. ApI 1434): duš- + karta- ‘done, made’, past pte. pass. tokar-. duskartam nsn. DSe 31f; XPh 42. draug- vb., see duruj- and draujiya-.
drauga- sb. *the Lie", the evil force opposed to Ahuramazda, Ávestan Druj: Av. draoga-, NPers.
dury, Skt. drógha- droha- ‘(malicious) injury’, pIE *dhrougho-, cf. NGm. Trug ‘deceit’, and OP duruj-, draujana-, draujiya- (870, 576.11, $101, $108.IV, $106, $122, $128, 5132.2, 3, $143.I, V). drauga nsm. DB 1.34, 434; DPd 20. draugà absm. DB 437; DPd 17f.
draujana- adj. ‘deceitful’, i.e. ‘adherent of the Lie’: deriv. of drauga- (§101, 5132.2, 5147.1), cf. GAv. drogvant- ‘adherent of the Dru? (Hz. Apl 140-1). draujana nsm. DB 4.38, 63, 68. drauja- nam asm. DNb 12.
draujiya- vb. ‘regard as a lie’, denom. to drauga- (S217). [Отау уау 2d sg. subj. (§222.11, §227.1) DB 4.43.
drayah- sb. ‘sea’: Av. zrayah-, NPers. dáryà, ·
Skt. jrdyas- ‘expanse’, pIE *órejos- (§88, $113, $128, $156.II). Decl, §185.1. See also para- draya. draya asn. DB 5.23; DP
```


## [2026-09-06T14:52:51.498Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"patigara\\|pati-gara\\|patigār\\|gāra\\|piyāla\\|piyala\" KNT.txt | head -20; echo ---; grep -n \"^gar-\\|gar- vb\\|‘swallow’\\|‘devour’\" KNT.txt | head -20",
 "description": "Kent gar/patigara"
}
```


### [2026-09-06T14:52:51.559Z] TOOL RESULT

```
---
5723:batugara- sb. ‘drinking cup, saucer’: if genu- ine ($55.11; JAOS 56.215; Schaeder, БРАМ 1935. 489-96), from batu- ‘wine’ ($153.1; etymology un- certain, but Hz. ApI 114 quotes Bariaxy from Athenaeus, bk. xi, page 784a, as the Persian word for ‘phiale, cup’) + -gara- (8143.1) ‘devouring, drinking’ ($160.Ia), cf. Av. aspé.gard ‘horse-de- vouring’, Skt. aja-gará- ‘goat-swallower, boa con- strictor’, Gk. dnuo-Bédpos ‘people-devouring’, Lt. carni-vorus ‘flesh-eating’, from root in Av. gar- ‘devour’, Skt. girdit, Lt. vorat, plE *g*er-. Bv. J As. 228.233-4 suggests, and На. AMI 8.9-17, Ap! 118—5, accepts cognation rather with Skt. galati ‘drips’, gdlayat ‘pours’, as ‘wine-pourer’, cf. Lt. рате ‘pour (as an offering to the gods)’, and NPers. piyàüla ‘drinking cup’, from *pati-gdra-. bülugara пет. ($56.V) АЧ.
```


## [2026-09-06T14:53:01.960Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\ni=t.find('batugara- sb.')\nprint('leaf0based',t[:i].count('\\f'))\n\"",
 "description": "Locate leaf of batugara"
}
```


## [2026-09-06T14:53:02.443Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"OLD PERSIAN$\" KNT.txt | sed -n '90,110p'",
 "description": "Page headers"
}
```


### [2026-09-06T14:53:03.684Z] TOOL RESULT

```
leaf0based 223
```


### [2026-09-06T14:53:06.322Z] TOOL RESULT

```
5438:OLD PERSIAN
5484:OLD PERSIAN
5526:190 OLD PERSIAN
5566:192 OLD PERSIAN
5610:194 OLD PERSIAN
5656:196 OLD PERSIAN
5704:OLD PERSIAN
5727:200 OLD PERSIAN
5762:202 OLD PERSIAN
5818:OLD PERSIAN
```


## [2026-09-06T14:53:17.244Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5704,5727p' KNT.txt | grep -n \"^g\\|gar\\|gaub\\|garma\" | head; echo \"=== g- entries in Kent lexicon:\"; awk 'NR>5400 && NR<5760' KNT.txt | grep -oE \"^[a-zA-Zāīūəšθčǰ*-]+- (sb|adj|vb|adv|pron)\\.\" | head -60",
 "description": "Kent g- lexicon entries"
}
```


### [2026-09-06T14:53:19.790Z] TOOL RESULT

```
20:batugara- sb. ‘drinking cup, saucer’: if genu- ine ($55.11; JAOS 56.215; Schaeder, БРАМ 1935. 489-96), from batu- ‘wine’ ($153.1; etymology un- certain, but Hz. ApI 114 quotes Bariaxy from Athenaeus, bk. xi, page 784a, as the Persian word for ‘phiale, cup’) + -gara- (8143.1) ‘devouring, drinking’ ($160.Ia), cf. Av. aspé.gard ‘horse-de- vouring’, Skt. aja-gará- ‘goat-swallower, boa con- strictor’, Gk. dnuo-Bédpos ‘people-devouring’, Lt. carni-vorus ‘flesh-eating’, from root in Av. gar- ‘devour’, Skt. girdit, Lt. vorat, plE *g*er-. Bv. J As. 228.233-4 suggests, and На. AMI 8.9-17, Ap! 118—5, accepts cognation rather with Skt. galati ‘drips’, gdlayat ‘pours’, as ‘wine-pourer’, cf. Lt. рате ‘pour (as an offering to the gods)’, and NPers. piyàüla ‘drinking cup’, from *pati-gdra-. bülugara пет. ($56.V) АЧ.
=== g- entries in Kent lexicon:
Jav- vb.
ji- vb.
tauman- sb.
lauviyah- adj.
takabara- adj.
taxma- adj.
tacara- sb.
tanii- sb.
tav- vb.
taš- vb.
Tigra- sb.
*hgra- adj.
Tigra- sb.
igrazauda- adj.
Odigarct- adj.
Oalagu- sb.
Gataguiya- adj.
Sanuvaniya- sb.
bard- sb.
barmi- sb.
citiya- adj.
dawa- sb.
daug- vb.
dauStar- sb.
idan- vb.
*dan- vb.
ldar- vb.
*dar- vb.
daraniya- sb.
daru- sb.
darga- adj.
darš- vb.
dasta- sb.
dastakarta- adj.
Daha- adj.
dahyu- sb.
idi- vb.
*di- vb.
dipi- sb.
dug- vb.
dūra- adj.
duruj- vb.
duruva- adj.
duvatsta- adj.
duvara- sb.
duvari- sb.
duvitiya- adj.
dusiyara- sb.
drauga- sb.
draujana- adj.
draujiya- vb.
drayah- sb.
naiba- adj.
naucaina- adj.
nab- vb.
Nabukudracara- sb.
Nabunaita- sb.
niman- sb.
nay- vb.
nar- sb.
```


## [2026-09-06T14:53:25.508Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -nE \"^(gar|gaub|garma|gaita|Gauma)\" KNT.txt | head -20; echo \"---BRT gairi/gar\"; grep -n \"garǝman\\|gar\\.man\\|garəman\" BRT.txt | head -10",
 "description": "Kent gar entries, BRT garəman"
}
```


### [2026-09-06T14:53:25.575Z] TOOL RESULT

```
4847:Gaumata started his rebellion in XII 14 of 523/2, and received the adherence of the Empire on IV 9 of 522/1. But Darius, a distant cousin of Cambyses, knowing that Gaumata was not the real Smerdis, with the aid of a few men fought with and slew Gaumata and his chief followers, on
5366:garta- sb., either ‘cave’ or ‘wagon’, see Asa- garla-.
---BRT gairi/gar
```


## [2026-09-06T14:53:32.973Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"grīvā\\|griva\\|grīva\\|gnva\" BRT.txt | head -20; echo \"=== jaraiti\"; grep -n \"jaraiti\\|jarati\\|gar- .*versch\\|verschlingen\" BRT.txt | head -20",
 "description": "Bartholomae grīvā, jaraiti"
}
```


### [2026-09-06T14:53:33.037Z] TOOL RESULT

```
6953:•  j.  ahmt,  ahmya  Adv.  'ibi';  I)  zurück- weisend; i)  zeitlich  'indem,  da':  'tnt  dim fraah>r3zal  (sd.)  "mi  liB  bavat  aosanhä (sd)  V.2.S  PüZ.  1)  räumlich,  in  Ver- bindung mit  vorhergehendem  a)  yat,  b) yaha,  c)  ye-A  an  Stelle  des  LS.  (m.  und  f.) des  Relativums  'ubi':  a)  aiAka  z»mö  .  . yat  'mi  spänasca  .  ,  para.iri^ttiti  V,  6.1; —  anzUrahe  grivaya  .  .  yat  'mya  daiva handvannti  V._j.7'*.  b)  vainlf  ahmi ninäne  sraosü  asntstTm  yaHa  'mya  am?ia sptnta  .  .  pailisqn  .  .  yasnqsca  .  .  Y.  6o. 5  t  c)  ^^  astsm  upanhanzaiti .  .yezt  'mya iri>yati  (sd.)  fii?m  ..  V.  ii'.io.  II)  vor- ausweisend,  auf  einen  Satz  TO.ityim  ('wenn') oder  yat,  zeiüich :  tasca  mg  nqma  ibayaisa 'mi..yim  sifsta  rfffiri^Ä/..  Yt. /5.50;  49, 50,  52  (wo  _>-<//).  3)  vorausgehendes yat  aufnehmend  (s.  'a-  II  Anh.  B),  zeitlich: yat  spSoa  kanjasante  .  .  vastAtihU  °mya nöit  vazyante  (sd.)  "wenn  . .,  wenn  .  ."  Yt.
21203:—  aitatahqm  urvaranqm  y  IUn.H^ranqm Y.  Ä  7  5 ;  —  aSaesqm  y  daxmanqm  V.  7. 51;  Yt_5.  9, 13; —  aäanhqm  y  myazda- nqm  N.  ^2.  Anhang.  Auftallig  ist  die Wortfolge  (zu  c):  daiiikanqmcli  aidyünam hyat  urunayazamaidfY.3g,3*'>.  2)oluie erkennbare  Bedeutung;  A)imgAw.;a)vor clt  in  ya-  hyalclt  'quicunque'  (Sp.  593  u., 1230  u.):  yä  mazdd^a  (sd.)  hyatüt}^  vt- du!iY.30.\.  b)  vor  cä:  däröi  ahvä astvatascä  hyaicä^l  mananhS  ayapta(sd.) "vitarum  et  (vitae)  corporeae  et  (vitae) animi  fclicitatcs"  Y.  2Ä3;  —  varp^aitl  .. ratui  syaoianS  razistä  (sd.)  drigvataüä hyaicä^'^  *asaom  yehyaca  hsm>myasaill (sd.)  . .  Y.33. 1.  c)  zur  Einleitung  einer Aufforderung:  hy^  höi  hudsmSm  (sd.)  dyäi vax)lrahya  Y.2g.B.  b)  im  jA^p.;  zur Einleitung  der  Antwort:  kva paoirJm  aiiihä zsniB  asailtimi  ..  y^  arpzürahe  grivaya V.J.  7;  —  zur  Einleitung  des  Refrains: paiti  /ahikayai . .  kthrpjm  näämnäi  asaone . .  vadar»  jatäi  y'^^  hl  k»hrppm  . .  vadar> jaiii  Y.5.  33;—  sonst:  bval  vispB  ankul astvä  *azar>s5 ..  daryypm  _y'"  yave  vispai F._3  h;  —  daiiihSul  dairihupaUlm  bisatyai vähm  .  .  anjB  y'i'>  paoirlm  nmana/ie nmänäpaitlm  näirikqm  bHasyät  ka'hioa daSnu  arsjB  V.  7.  41  f.;  —  vTtasti.dra/s y'fi huSkanqm  (sd.)  .  .  aiiihS  s»mB  mdat^yqn V.  7.  29;  29f.3,  33  f.*;  —  das?mB  y  ahmi spanB  alvandasö  spanaauha  .  ,  lutvadasa y    ahmi   data   visqstPmB   ahmi  y    ahmi
=== jaraiti
5878:•  j.  aspö.gar-  Adj.  'Rosse  verschlingend': azTm  . .  yim  °gar»n  mn^anm  \.q.\i.
10222:•  j.*gar-  i)  Adj. 'schluckend,  verschlingend' (nur  Komp.).  2)  f.,  Plur.  ■>  'Kehle,  Hals'  '> : aictl  ai3in  (näml. o^/)  tanUn  aguze  aiairi maisahe  -rö  Yt.  J7.  56.
19006:•  j.  nsra.gar-  Adj.  'männerverschlingend': ailm  .  .  yim   aspSganm  'garwt   Y.g.w.
```


## [2026-09-06T14:53:42.376Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gar-  Verb\\|gar-  V\\.\\|schlucken\\|Schlund\\|Kehle\" BRT.txt | head -20; echo \"=== garǝman\"; grep -n \"gar»man\\|garaman\\|gar\\*man\\|gr>man\" BRT.txt | head",
 "description": "BRT gar verb"
}
```


### [2026-09-06T14:53:42.447Z] TOOL RESULT

```
7856:•  j.  ^ah-  n.  i)  'Ein-,  ZusammenschnU- rung*  der  Kehle,  'Erdrosselung'  (nur Komp.).  3)  'Bedrängung,  Enge,  Not; Gefangenschaft':  mi^nm  .  .  yS  nargm  .  . ipa  'zatshat  .  .  fäyajanhat  baraiti  apa nö  haca  'zaahat  apa  haca  'satihibyö (DP.)'>  harSiS^l.  10,22V,— th  nS 'tahucit hals  %rayente  YL 13. 1 46 ;  Vy  t.  $0;  —  yd  AÜ
10203:•  j.  'gar-  V.  'preisen',  nur  mit  Praev. Praes.  11  g^nn-,  a6  gairya-  (Pass.)  — Int  °gairyä.
10209:•  j.  3gar-  V.  'schlucken'.  Praes.  ^jara-'^. *}arSil  *haom3m  .  .  bisanmta    *iristi-
10212:•  j.  ^gar-  V.,  nur  mit  «r  'niederschleu- dem'.     Praes.  zi  grä-.
10222:•  j.*gar-  i)  Adj. 'schluckend,  verschlingend' (nur  Komp.).  2)  f.,  Plur.  ■>  'Kehle,  Hals'  '> : aictl  ai3in  (näml. o^/)  tanUn  aguze  aiairi maisahe  -rö  Yt.  J7.  56.
10223:KompE.  —  Zum  V.  igar-.  —  ai.  'gir-  Adj. ;  vgl. ai.  gala-  m.,  np.  giilü  'Kehle'.  —  •)  Auch -ariman-  (sd.)  ist  Flur,  lant  —  =)  Gans  un- wahrscheinlich Gdn.  3Yt.   lao.
10276:•  j.  garaman-  m.,  Plur.  'Kehle,  Hals':  j  i'^'i  "ler  Klage  folgt  iti  dir.  Rede.  —  »  Mii y€zU'a  aZU  asti  düllhva  arante  'mS-\  '«'■rekter^Um^el^iune  i"s  jAw.;  s.  Btiil.  IF. kva   vToänie  "wenn   die    Knochen   (dem ,     ^'  '^  ^'  ""'•
14671:Ableit    —    Vgl.  aL  Irimidi-   f.,    np.  /JJ).    — Pü.;  30. —  ')  Statt  'lan/fm  (AS.),  in  Aniehnnng an   sal^m    'hundeit'.     Der   Akk.    dient   dann auch    als  Nom..  %3zj.2.   S.  noch   irisaf. — ')    ErstantM    Nora.,    vgl    Sray-    No.   5.    — i)  S  ^ro  udW. "  j,  *i^^i8a^9In'>  Adv.  'dreimal':    *jarSi/ "'Aaomtm  ..  buanmla  °r»m^a  ya^a  'nm nüfm)m    "du    sollst  H.    schlucken,  zwei- mal und  dreimal;  wenn  dreimal,  (jeweils) nur  ganz  wenig"  P.  20.
28368:•  j.  sam-  V.,  nur  mit  a  'einschlürfen, schlucken'.     Praes.  2  /ama-,
28371:ersten  falschen  Wort  soll  er  drei  Schluck Harn  schlucken  .  ,"  V.g.
28562:•  j.  zgar-  V.  'fliessen,  strömen'.  Praes.  2 igara-.
=== garǝman
10276:•  j.  garaman-  m.,  Plur.  'Kehle,  Hals':  j  i'^'i  "ler  Klage  folgt  iti  dir.  Rede.  —  »  Mii y€zU'a  aZU  asti  düllhva  arante  'mS-\  '«'■rekter^Um^el^iune  i"s  jAw.;  s.  Btiil.  IF. kva   vToänie  "wenn   die    Knochen   (dem ,     ^'  '^  ^'  ""'•
```


## [2026-09-06T14:53:54.605Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gnvä\\|griva\\|grivä\\|grlvä\\|gnva\\|Nacken\" BRT.txt | head -20",
 "description": "BRT grīvā entry"
}
```


### [2026-09-06T14:53:54.668Z] TOOL RESULT

```
5616:H1M.PSL  66.  —  Vgl.  farizah;  arizyä-.  —  Yü..:  grivä-  f.  'Nacken'  als  Name  eines  Bergs**':
5820:*)  Auch  blos  vllüiav-  genannt;  sd.  Er  wifft dem  Toten  eine  Schlinge  um  den  Nacken,  der nur  der  Geicchle  entrinnen  kann;  Dd.  2j.  3. Ebd.  j/.  II  heisst  er  „ihe  disintegiallon  of  matc- rial  beings"  und  gilt  nach  ^/.  81  als  Anführer der  mäztinischen  Daeva,  Sü.  hat  asii^^vahäda- yamafy  "der  A.  genannte  Todesgott".
6953:•  j.  ahmt,  ahmya  Adv.  'ibi';  I)  zurück- weisend; i)  zeitlich  'indem,  da':  'tnt  dim fraah>r3zal  (sd.)  "mi  liB  bavat  aosanhä (sd)  V.2.S  PüZ.  1)  räumlich,  in  Ver- bindung mit  vorhergehendem  a)  yat,  b) yaha,  c)  ye-A  an  Stelle  des  LS.  (m.  und  f.) des  Relativums  'ubi':  a)  aiAka  z»mö  .  . yat  'mi  spänasca  .  ,  para.iri^ttiti  V,  6.1; —  anzUrahe  grivaya  .  .  yat  'mya  daiva handvannti  V._j.7'*.  b)  vainlf  ahmi ninäne  sraosü  asntstTm  yaHa  'mya  am?ia sptnta  .  .  pailisqn  .  .  yasnqsca  .  .  Y.  6o. 5  t  c)  ^^  astsm  upanhanzaiti .  .yezt  'mya iri>yati  (sd.)  fii?m  ..  V.  ii'.io.  II)  vor- ausweisend,  auf  einen  Satz  TO.ityim  ('wenn') oder  yat,  zeiüich :  tasca  mg  nqma  ibayaisa 'mi..yim  sifsta  rfffiri^Ä/..  Yt. /5.50;  49, 50,  52  (wo  _>-<//).  3)  vorausgehendes yat  aufnehmend  (s.  'a-  II  Anh.  B),  zeitlich: yat  spSoa  kanjasante  .  .  vastAtihU  °mya nöit  vazyante  (sd.)  "wenn  . .,  wenn  .  ."  Yt.
10493:da»  Wort  fehlt  also;  aber  So.:  dli-gkam  .•  j.  grivä-  f.  'Nacken'  UZW.  (fofflTScher u/if/iapravraim  yävai  gfüio 'd mäniAravJttyä.  Wesen":  atfZBraAe [s,A.)  "i-aj-a  (LS.)  V.J.7. —  '>  S  ^^S.  37.  I      ii.gräia-i.;mp.l^ä.)grhai,Tt^.sar7va'iiä^t\',
15026:•  j.  paiti.varah-  n.  'Nacken' i'/u/A'/a  hl
19761:•  j.  'manaoSri-  £  'Hals,  Nacken',  uzw. a^anscher  Wesen'' :  "an"  F.  jg;  —  minum barat..ar3dvlsära..upa  tarn  srJrqm'^rim Yt5. 127;  —  ava  hl  (nämLjfi«J)  baraytn taihm  dauru  (sd.)  upa  tqm  «Srüw  V.7_j,30.
21203:—  aitatahqm  urvaranqm  y  IUn.H^ranqm Y.  Ä  7  5 ;  —  aSaesqm  y  daxmanqm  V.  7. 51;  Yt_5.  9, 13; —  aäanhqm  y  myazda- nqm  N.  ^2.  Anhang.  Auftallig  ist  die Wortfolge  (zu  c):  daiiikanqmcli  aidyünam hyat  urunayazamaidfY.3g,3*'>.  2)oluie erkennbare  Bedeutung;  A)imgAw.;a)vor clt  in  ya-  hyalclt  'quicunque'  (Sp.  593  u., 1230  u.):  yä  mazdd^a  (sd.)  hyatüt}^  vt- du!iY.30.\.  b)  vor  cä:  däröi  ahvä astvatascä  hyaicä^l  mananhS  ayapta(sd.) "vitarum  et  (vitae)  corporeae  et  (vitae) animi  fclicitatcs"  Y.  2Ä3;  —  varp^aitl  .. ratui  syaoianS  razistä  (sd.)  drigvataüä hyaicä^'^  *asaom  yehyaca  hsm>myasaill (sd.)  . .  Y.33. 1.  c)  zur  Einleitung  einer Aufforderung:  hy^  höi  hudsmSm  (sd.)  dyäi vax)lrahya  Y.2g.B.  b)  im  jA^p.;  zur Einleitung  der  Antwort:  kva paoirJm  aiiihä zsniB  asailtimi  ..  y^  arpzürahe  grivaya V.J.  7;  —  zur  Einleitung  des  Refrains: paiti  /ahikayai . .  kthrpjm  näämnäi  asaone . .  vadar»  jatäi  y'^^  hl  k»hrppm  . .  vadar> jaiii  Y.5.  33;—  sonst:  bval  vispB  ankul astvä  *azar>s5 ..  daryypm  _y'"  yave  vispai F._3  h;  —  daiiihSul  dairihupaUlm  bisatyai vähm  .  .  anjB  y'i'>  paoirlm  nmana/ie nmänäpaitlm  näirikqm  bHasyät  ka'hioa daSnu  arsjB  V.  7.  41  f.;  —  vTtasti.dra/s y'fi huSkanqm  (sd.)  .  .  aiiihS  s»mB  mdat^yqn V.  7.  29;  29f.3,  33  f.*;  —  das?mB  y  ahmi spanB  alvandasö  spanaauha  .  ,  lutvadasa y    ahmi   data   visqstPmB   ahmi  y    ahmi
26796:•  j.  stri-manaoÖTi-''  Adj.  (auch  mask.) 'mit  starkem,  derbem  Nacken':  pu^rö  ,  . =m(NSm.)  Yt.p.30.
```


## [2026-09-06T14:54:08.600Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==229' HRN.txt | head -60",
 "description": "Horn p.207"
}
```


## [2026-09-06T14:54:09.903Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gluk\\|gulūg\\|gulug\\|grīwbān\\|griwban\\|grīw\\b\\|griw \" PHD.txt PHD_mackenzie.txt | head -20",
 "description": "MacKenzie gulūg, grīwbān"
}
```


### [2026-09-06T14:54:11.792Z] TOOL RESULT

```
ma
- 207 -
phlv. varta d. i. varda ^) (PPGL), g^d (Bund.), vard in
arm. arab. LW. vard, (sogar ar. muvarrad rosenfarbig',
AM. 168 Zeile (>), vergl. arm. Vardges, phlv. N.
pr. Vardakl (Gemme, Hörn, Mitteilungen, Heft IV,
34); gr. Qoäoy, lesb. /J^'Jor.
927»»*« gil 'Schmutz. Lehm'.
arm. kir Xehm' (Fr. Müller, WZKM. 5, 268)2).
928. guia, gelü (AM. 109 Zeile 1 v. u.) 'Kehle .
aw. garah' 'Kehle'; phlv. garük vd. 15 (11); skr.
gala-; lat. gula; arm. vergl. -kul '-verschlingend' (H.
No. 145), ker 'Nahrung, Frass' etc. (H. No. 143).
kurd. gerü 'Kehle'; af}'. yäre; oss. gm' (166; un-
sicher); sangl. yar,
929. ffuJüle 'Kugel', (/öle.
Käs. gtdi, gulla,
Vergl. ai. gldv- 'Ballen, kropfartiger Auswuchs';
ykovTog 'Ballen, Rundung (NB. so nur bei Fick, sonst
'Hinterbacke, Gesäss'); ags. cleoven, ahd. chlluwa
'KnäuV,
Am Genauesten entspricht nhd. Knaul (für Kläuel
wie ndd. Mid für klmi, vergl. engl, crewl, Fick"*, 412).
Ein Suffix 'le mit verkleinernder Bedeutung will
Darmesteter, Et. ir. I, 298, in np. merdle erkennen,
aber wo hat er diese neupersische Form her?^). Zum
*) Natürlich in dieser Form nur das zurückgenommene aramäiHche
Lehnwort.
^) Zu lat^ llmus und ksl. glina vergl. Johansson, Paul und
Branne's Beiträge 14, 819, 320 und Stolz, Latein. Gramm. ^ S. 3S4.
') Diese Frage muss man sich (ganz abgesehen von den sehr
häufigen, durchaus falschen Aussprachen) öfter in Darmesteter^s
Buche vorlegen, z. B. bei gume/ten^ mihän 'Wohnung' (wohl statt
mehen?% yästden^ yä//- *Gunst*, kunisn imSähnäme; vergl. auch Sale-
mann, M61. asiat. IX, 235. Bei den damaligen nicht eben bedeutenden
neupersischen Kenntnissen des Verfassers darf man in solchen Fällen
kaum etwas Belangreicheres als Verlesungen (oben etwa statt merdike?)
oder kritiklose Übernahmen von Päzendworten aus West's Glossaren
mutmassen *).
*) Ein np, Deminutivsuffix -le finde ich nachträglich sehr häufig
bei den Bergjuden im Kaukasus. Aus Mi Her 's Glossar habe ich mir
```


### [2026-09-06T14:54:11.836Z] TOOL RESULT

```
PHD.txt:382:*g5k4n [gwk’n'] details. Lc um ~ig [-yk'] detailed; precisely. (sassa tu) ģūmēz [gwmyc | N giméz] bull's urine (as ritual purifier). ģgūmēz- [gwmyc- | N giméz-] urinate. gön [gwa' | N gün] colour, complexion. ~ag [-k' | M geng, N güna] = gön ; sort, kind, form. gor [gwl | N ~] onager, wild ass. göspand [K YNA < А апу ? ; gwspnd | N ~] (small) cattle, sheep. ~-tihrag [-cyhlk'] holding the seed of cattle. ģūstān [gwst^n!] cattle-stall, cowshed. 1858 [gws | = M, N ~J ear. *GÓ68 [guš | N ~] cal. 14th day. tūšag [gwsk' | N ~a] corner. ģēošūsrūd [rwi^wslwt! = Av. gaošū.srūta-| acquired, learnt. 5051 [BSLYA < A bsr’; рой! | N ~] meat, flesh. ģūšwār [gwštw] | N ~] ear-ring. ģūw-, ~išn, v. ģuftan. gowag [swb k! | М gw'g, N goya] speaking, eloquent; speaker. *ģoūwizār [gwwc'[] explicit, in detail. göy [gwd | N ~] ball. göz [gwc | N ~] walnut. ~énag [gwzynk! | N gózina) a walnut sweetmeat. Gözihr [gwcyhl | Ar. jawzahr] astr. the Dragon. ~ dumb: the descending node of the moon. ~ sar: the ascending node of the moon. grab [22р | P grb] womb. grāmag [gľmk! | P gr’mg] possessions, wealth. grāmig [gľmyk! | M grmyg, N girāmī] treasured, dear. ~ih: affection, respect. 1$raw [giwb! | P grww] cane. *ģraw [glwb' | N giraw] pledge, security. ~ih, ~(a)g4n [glwk’n' | M grug*n, N giraugān] = *graw. grayidan, gray- [gl?d-yin' | P gry-, N gtráy-] lean, incline; intend, desire. ģriftan, gir- [OHDWN-tn' < A V?hd; glptn!, gyl- | M grypt, gyr-, N giriftan, ~] take, hold, restrain. «išnīģ : tangible. griftār [gipt?l | N gir~] held, taken; captive. ~Omand [-'wmnd) tangible. grih [glyh | N girth] knot. lgriw [CWLE < A swr-h; glyw'] neck, throat. ?0riw [CWLE, glyw' | M gryw] self, soul. sgriw [glyw! | P gryw, N girī(b)] a grain measure, modius, peck. griwag [glywk!' | N giriwa] hill, ridge. ģrīwbān [g/ywp?n! | N girībān] neck-guard, gorget. griyistan, griy- [BK YWN-stn'< A У bky; gld-stn! | M gryy-stn, N giristan, giry-] weep, cry.
PHD.txt:2131:gorget grīwbān.
PHD.txt:2838:modtus grīw.
PHD.txt:3571:self grīw, xwad, xwēštan.
PHD.txt:5376:garānīh darhandarzbed yarranidan garan yarranisn gramigih gramig grāmag drāyīdan, grāyīdan drāz, grāb draxt griy- grih dargūh garasman 1 3uriw griwag grīwbān driyos driyöšīh darigbed dilér drëm griyistan
PHD_mackenzie.txt:2582:agriw [glywl I P gryw, N giri(b)] a grain measure, modius, peck.
PHD_mackenzie.txt:6685:genesis bawisn.                               gorget griwban.
PHD_mackenzie.txt:7140:mottled pes.                                   neck~guard griwban.
PHD_mackenzie.txt:10549:driiz:1nih             "'0 \c; ~   griwban                 \~Q)~
```


## [2026-09-06T14:54:25.063Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"throat\" PHD.txt | head -10; echo \"=== NYB\"; grep -n \"gulūg\\|glwk\\|garūk\\|griwbān\\|grīwbān\\|grīw\" NYB_vol2_glossary.txt | head -15",
 "description": "PHD throat, Nyberg"
}
```


### [2026-09-06T14:54:25.139Z] TOOL RESULT

```
378:galēģ [glwk' | N guld] throat. бато [gm | = M, N ~j pace, step, stride; a yard (3 ft.). ~ í dó pay: a pace (s ft.). -рапаб [-k’nk' | M eng, N -gàna] suffix forming numerical adjectives, -fold. бапа [gnd | N ~] stench. gandag [gndk' | (M gng), N —a] foul, stinking. ~th: stench. ģandanāģ [gndn’k' | N gandanā] leek. gandum [Hš < A nth | (M gnwm), N ~] wheat. ganj [gnc | (M gnz), N e treasure, treasury. ~war [-wbl | M -wr, N ~] treasurer. ģan(n)āģ [gr &! | (P gnd?g)] foul, corrupt (v. gandag). ~ ménó$g the Evil Spirit. ~ih: corruption. gar [gl] mountain. -gar [-Al, -gl | M -gr, N ~] suffix forming actor nouns. -gar [-£1| M -g’r, N ~] suffix forming actor nouns. garan [gPn! | M г?л, N girán] heavy, serious, difficult. АҺ; heaviness, weight. garasman [glsm’n' | М ртт?п] = garddman. gard [g/t! | N ~] dust. gardan [gitn! | M grdn, N ~] neck. ģardānāģ [gl h] die (for gaming). gardanidan, gardan- [gl n-ytn! | M grd(y)nydn, N ~] turn (tr.). gardidan, gard- [git-yin' | M grd-, N ~] turn, revolve. ~išn: revolution, turning. garm [gim | M grm, N ~] warm, hot. «„«ih: warmth, heat. garm-ābag [gim'pk! | N ~a] bath-house. garmāģ [glm^ k! | М grmg, N garmá] warmth, heat. g£armóg [gimwk!] warm, ardent, fervent. garmówar(ih) [glmwk wl(yh)] heat ordeal. ģarmsēr [gimsyl | N ~] warm region, lowlands. garódman [glwtmn' = Av. garó dəmana- | M grdm?n] paradise. ~ig [-yk'] (worthy) of paradise. yarranag [g”7k! | M grn’g ?] thunder. yarranidan, yarran- [gl’n-ytn' | (N yurridan)] roar, thunder. ~i$n: roaring. garzag [gick! | N garza] snake, serpent. garzidan, garz- [glc-ytn'] complain; confess. ~i$n: complaint. ~iSnig : complaining. gaw [gw!'] hand (daevic). базу [ТИРА < А twr) | M gw, N ~] ox, bull, cow; astr. Taurus. gawars [PZ < A prg’; g”wls | N ~] sorghum, giant millet.
382:*g5k4n [gwk’n'] details. Lc um ~ig [-yk'] detailed; precisely. (sassa tu) ģūmēz [gwmyc | N giméz] bull's urine (as ritual purifier). ģgūmēz- [gwmyc- | N giméz-] urinate. gön [gwa' | N gün] colour, complexion. ~ag [-k' | M geng, N güna] = gön ; sort, kind, form. gor [gwl | N ~] onager, wild ass. göspand [K YNA < А апу ? ; gwspnd | N ~] (small) cattle, sheep. ~-tihrag [-cyhlk'] holding the seed of cattle. ģūstān [gwst^n!] cattle-stall, cowshed. 1858 [gws | = M, N ~J ear. *GÓ68 [guš | N ~] cal. 14th day. tūšag [gwsk' | N ~a] corner. ģēošūsrūd [rwi^wslwt! = Av. gaošū.srūta-| acquired, learnt. 5051 [BSLYA < A bsr’; рой! | N ~] meat, flesh. ģūšwār [gwštw] | N ~] ear-ring. ģūw-, ~išn, v. ģuftan. gowag [swb k! | М gw'g, N goya] speaking, eloquent; speaker. *ģoūwizār [gwwc'[] explicit, in detail. göy [gwd | N ~] ball. göz [gwc | N ~] walnut. ~énag [gwzynk! | N gózina) a walnut sweetmeat. Gözihr [gwcyhl | Ar. jawzahr] astr. the Dragon. ~ dumb: the descending node of the moon. ~ sar: the ascending node of the moon. grab [22р | P grb] womb. grāmag [gľmk! | P gr’mg] possessions, wealth. grāmig [gľmyk! | M grmyg, N girāmī] treasured, dear. ~ih: affection, respect. 1$raw [giwb! | P grww] cane. *ģraw [glwb' | N giraw] pledge, security. ~ih, ~(a)g4n [glwk’n' | M grug*n, N giraugān] = *graw. grayidan, gray- [gl?d-yin' | P gry-, N gtráy-] lean, incline; intend, desire. ģriftan, gir- [OHDWN-tn' < A V?hd; glptn!, gyl- | M grypt, gyr-, N giriftan, ~] take, hold, restrain. «išnīģ : tangible. griftār [gipt?l | N gir~] held, taken; captive. ~Omand [-'wmnd) tangible. grih [glyh | N girth] knot. lgriw [CWLE < A swr-h; glyw'] neck, throat. ?0riw [CWLE, glyw' | M gryw] self, soul. sgriw [glyw! | P gryw, N girī(b)] a grain measure, modius, peck. griwag [glywk!' | N giriwa] hill, ridge. ģrīwbān [g/ywp?n! | N girībān] neck-guard, gorget. griyistan, griy- [BK YWN-stn'< A У bky; gld-stn! | M gryy-stn, N giristan, giry-] weep, cry.
4001:throat galóg, griw.
=== NYB
1974:hayyaréh help, aid, assistance: pat yaz- dàn ~ 314-15, 1214; pat ~ i yazdàn 505; pat nerök u ~ i Haftoiring 8774; nérók u ~ + zrat rād 8871; pat ~ <i> [better <u> or asyndeton] zor u z"arrah i .., spēnāk menoi 10628-24; pat name u nerök u ~ 1 dätär Ohurmazà 113?; 01? v. s. v. jāytšn; oigan ... kē-$ ~ hend those who are his (assistance =) assistants 100!!; ~ dātan 0 512; ~ dahišneh 11211; 6 ~ rasitan 61; Octo 3811 ; erat ~ 112-16 Ps, hdyb?-lyhy. hazangró-zim [hznglwkzym, -zm] a pe- riod of one thousand years, a millenium 3820.25, 391, 96% — Borrowed from Av. (1798) hazayro.zyam-.
```


## [2026-09-06T14:54:26.780Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"grivä.pän\\|grivapän\\|grīvā.pāna\\|pän-\\|griva.p\" BRT.txt | head -10; echo \"=== HUB gulu\"; grep -n \"gulū\\|gulu\\|gelü\\|garük\" HUB.txt | head -15",
 "description": "BRT grīvā-pāna, HUB"
}
```


### [2026-09-06T14:54:26.851Z] TOOL RESULT

```
=== HUB gulu
956:Gelages', bazma 'angulus in loco compotationis'. Frag-
8810:gulu *Kehle', zd. garah-; gulula 'Kugel* H. 929; gand 'Ge-
9456:gulu *Kehle*, skr. gala-, lat. jrw/a, d. Kehle, aber zd. garah-,
9457:kurd. geru, afgh. ydra und yarai; gulula 'Kugel', kurd.
9461:listan *leeken', aludan *beschmutzen* , galu *Kehle\ gulula
```


## [2026-09-06T14:54:43.141Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC gargel/gulgul\"; grep -nE \"^(gargel|gulgul|gargal|garg)\" IEC.txt | head -20; echo \"=== SYN leaf for p.233\"; awk 'BEGIN{RS=\"\\f\"} NR==258' SYN.txt | head -50",
 "description": "IEC and SYN lookups"
}
```


### [2026-09-06T14:54:45.265Z] TOOL RESULT

```
=== IEC gargel/gulgul
3891:gargəló, ið (gərgəl-) ‘gargle, gurgle’. cf. ghargəl- (ghərghəl-). Onomat. Skt. gárgarah ‘whirlpool’; gargara ‘churn’: Gk. cf. gargareón 'gullet; LLat. gargala ‘wind- pipe’; Li. gargaliuoti ‘be hoarse’; It. gar- gagliare (‘babble, purl’, beside gorgogliare, id.). See next
3892:gargəlos, à ‘babbling, raucous; babble, bubbling, gurgle, croak’. Onomat. Cf. WP I, . 538 & 683 Skt. gárgarah, gargarā; Per. yaryara ‘gurgle’; Gk. gárgalos (2), id.; Alb. gárgull ‘starling’; LLat. gargala ‘windpipe’; Li. gargalas, m. ‘hoarse speaker’; cf. garge “a water-fow?
3893:gargoros, ios “mass, pile, heap'. Cf. WP I, 590 Arm. karkar, Let ‘heap, pile’; Gk. gárgara, n. pl. id. cf. Hes. gargarés ‘tumult’: Li. cf. gargolas “lump, knot
3894:gargið (gargo, gargskö) ‘burble, gurgle’. Cf. gor-, gr&-, ghargh- Arm. cf. karkacem ‘burble, gurgle, chatter’. For Arm. gargacem, see ghargh-); OE cear- cian ‘creak, grind’; EME to chark ‘crack, chafe, gall’; Li. gargiù, ^ti & gargu, eti ‘be hoarse, croak, gargle’; Latv. gárdzu, er ‘roar of the chest, be hoarse’; gārkstu, et ‘be hoarse, rattle in the throat’; gārgt, inf. id. (For Skt. garjāmi, Av. garəz, jaroz-, Pehl. garzītan and Arm. kocem, kocim, korcem, see gorĝ-)
3895:garghö (gorgh-?) ‘complain’. Cf. ghargh- Skt. (ambig.) garhåmi, garhe “complain; blame for; MHG kargen "be sad'; LW in It. gargo ‘malicious’; Icel. cf. kergja, f. ‘obstinacy’
3898:gargolo, ið (gorgol-) — gauros
4472:gulgul-, gulugul- ‘gurgle’. Cf. gul-, gulg-. WP I, 683 Per. yulyul ‘clamour’; Arm. klklunk, s. ‘gurgle’; Alb. gullgulloj, v. ‘purl, babble’; G cf. kluckern ‘bubble out of a bottle’; Blg. gălăgăl ‘bubble- bubble from a bottle’
4481:gulgul-, gulugul- — gungul-
=== SYN leaf for p.233
� to tha Bee ae m verbs for ‘chew’ Or wae he modern Polish) seems to have dasa slang term forthe: ‘chauter starte - Several are obscure in their d ection. i a ait words for ew, aHal ‘chin’. Orig. sense Jaw and ultimate connection with ae word for ‘knee’, 1B *genu- (neut.), Gri. yoru, Lat. geni, etc. (4.36), through some com- mon notion like ‘angle’, is probable. Walde-P. 1.587. Ernout-M. 414. -H, 1.589 f. on ‘jaw’ (so always in Hom.) and ‘cheek’, -yéverov ‘chin’ (and ‘beard’) ; Lat. gena ‘cheek’ (mostly in pl.; stem genu- in genutni dentés ‘back teeth’); W. gen ‘jaw, chin’ (Ir. gin, W. geneu, Br. genou ‘mouth’); Goth. kinnus, ON kinn, Dan., Sw. kind ‘cheek’, OE cin, OHG kinni, etc. (all WGmce. words) ‘chin’ (but in early period traces of use for ‘jaw’, as OHG chinne ‘jaws’ Notker, Ps. 31.9, OHG chinnibacho ‘jaw’, OE cinban ‘jaw- bone’); Skt. hanu- ‘jaw’ (h for 7 second- ary), Av. zanu- ‘jaw’ or ‘chin’ (in epd., Barth, 1689) , NPers. zanaz ‘chin’; Toch. Ber oa (dual, SSS, 3, ftn.). Gre ae ae extension *Gon(e)dh-, Ba ease pn ; zandas ‘jaw’, al Mihl.-Endz, 4.759) edi pail # Ok rn al yom vor) istot, =i + Boisacq 862. GROpeRT se ce nr HdBos,. vers NG Hacé\)\a, of frequency.
fr. It. mascella (below
a 2)
Pe (mostly in pl.) ae It. mascella jaw’, but
SP. mejilla « back tooth’), cheek’, Rum. mased
ve, 1) in this order
Velum-vecril] belonging together like Perh my ala-azilla, wi a fr. *makslg Seine with mala,
Ir. smech, Lith.
-0. In Public Domain. Guru
Digitized by Arya Samaj Foundation Chennai and eGangotri
NCTIONS AND CONDITIONS 221
smakras ‘chin’, Skt. gmacru- ‘beard’ Walde-P. 2.689. Ernout-M. 582. Walde-H. 2.15.
Fr. mdchoire, fr. mdcher ‘chew’.
For Fr. dial. words and their distribu- tion, cf. H. Kahane, Bezeichnungen der Kinnbacken im Galloromanischen, in Berl. Beitr. z. rom. Ph. 2.2.
Sp. quijada, deriv. of Lat. capsa and capsus ‘box’, as if ‘box for the teeth’. Cf. Prov. cais ‘jaw’ and ‘cheek’. Port. queixo, formerly ‘jaw’, now ‘chin’. REW 1659c. Zauner, Rom. Forsch. 14.400. Wartburg 2.316. Malkiel, Lan- guage 21.151 ff.
Rum. falcd, fr. *falea for Lat. falz, falcis ‘sickle’ (8.33), hence ‘jaw’ from the similar shape of the lower jaw in side view. REW 3175. Puscariu 575.
4. Ir. carpat, Nir. carbad ‘chariot, wagon’ (10.75) used also for the ‘upper jaw, palate’ (cf. NIr. fiacla carbaid ‘teeth of the upper jaw’), apparently from the resemblance in shape. Here also Br. karvan ‘beam of a loom’ and reg. word for ‘jaw’ (upper or lower), and W. car yr én ‘jawbone’. Pedersen 1.118, 494.
NIr. corran ‘sickle’ (8.33) is used for the lower ‘jaw’.
NIr. giall, prob., like Gael. ciobhal, fr. forms of OE ceafl, NE jowl (below, 5). Macbain 193.
W. gen, above, 1.
W. cern, also ‘ch
```


## [2026-09-06T14:54:52.291Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"4\\.28 NECK\\|NECK$\\|4\\.28\" SYN.txt | head -10",
 "description": "Buck NECK section"
}
```


### [2026-09-06T14:54:53.802Z] TOOL RESULT

```
6001:a 4.28 NECK NG ath? T#AxvAos, Bion Goth. als Lith. kaklas Lat. ob ON _hals, sviri Lett.  kakls ee colla Dan. _hals ChSl. vyja, Sia coy Sw. hals SCr. _ vrat (Sija) Sp. cuello OE heals, sweora Boh.  fkrk, sje om git Ms hals, swere, necke Pol. — szyja, kark I, = A D ve a faa ae Du. hals ar reel kantha-
6047:‘throat’ to ‘neck’ has been noted in 4.28.
6068:Rum. gitlej, deriv. of git ‘neck’, orig. ‘throat’ (4.28).
6069:4. Ir. brage ‘neck’ (4.28), sometimes ‘throat’.
6071:W. gwddf, Br. gouzouk ‘neck’ (4.28) also ‘throat’,
8055:Russ. ustavsi7, perf. act. pple. of ustavat’ ‘get tired’: Boh. ustati ‘get tired, cease’, Pol. ustaé ‘cease’ (also sometimes ‘get tired’), ChSl. ustati, ustaviti ‘cease’ (14.28). Briickner 596.
10549:1. Derivs. of Lat. collum ‘neck’ (4.28), either directly or fr. Lat. collare ‘band or chain for the neck’. REW 2042, 2053.
10559:Br. gouzougenn, dim. of gouzoug ‘neck? (4.28).
10560:4. ON kragi (late and only on armor), Dan. krave, Sw. krage, fr. MLG krage = MHG eae (also ‘neck, gullet’), NHG kragen, Du. kraag, all orig. ‘neck’ (4.28).
10563:5. Lith. apikaklé, Lett. apkakle, cpds. of api ‘around’ and Lith. kaklas, Lett. kakls ‘neck’ (4.28).
```


## [2026-09-06T14:54:56.117Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6001,6050p' SYN.txt",
 "description": "Buck 4.28 NECK"
}
```


### [2026-09-06T14:54:56.170Z] TOOL RESULT

```
a 4.28 NECK NG ath? T#AxvAos, Bion Goth. als Lith. kaklas Lat. ob ON _hals, sviri Lett.  kakls ee colla Dan. _hals ChSl. vyja, Sia coy Sw. hals SCr. _ vrat (Sija) Sp. cuello OE heals, sweora Boh.  fkrk, sje om git Ms hals, swere, necke Pol. — szyja, kark I, = A D ve a faa ae Du. hals ar reel kantha-
' gudd Z OHG hals if aoé. a Wwda- Br, ee ong NEG hals, krage a4 aaa
hals Some Ww ords for ‘ ) ei.
hoted only the ee ck’ originally de- Others, denoting from the outset the Se NE nech : NHG nape) of the neck’ | whole round neck, are connected with 2 the Notion o nacken), and rest | words for ‘circle’, ‘column’, or ‘turn,
‘proj ection, ridge’ a
wind’. Some were originally words for
CC-O. In Public Domain. Gurukul Kangri Collection, Haridwar
232
‘throat’, with extension from the in- ternal throat (cf. 4.29), the latter being the front of the neck, hence ‘neck’. In general, words for ‘throat’ are sometimes used for ‘neck’, as conversely (cf. NHG halsweh ‘sore throat’, etc.).
1. Grk. adxjv (Hom.-+, regular word in Aristot. and not at all restricted to ‘nape of the neck’), perh.: Arm. @wj- in awjt-k ‘collar’, N. Adontz, Mélanges Boisacq 1.10.
Grk. rpaxndos (Hdt.+, displacing abxyv in Hellenistic Grk., as always in NT), prob. : tpoxés ‘wheel’, rpéxw ‘run’, etc. Walde-P. 1.874 f. (with query, but favored by analogies).
Grk. 5épy (poet.), see below, 7.
Grk. Aaruds ‘throat’ (4.29) is in NG also the usual word for ‘neck’ (rp4xyXos lit.). Cf. also oBépxos (= Alb. zverk) and ovtxe ‘nape of the neck’, loanwords but ultimate source?
2. Lat. collum (> It. collo, Fr. cou, Sp. cuello; Fr. col ‘neck’ of bottles, dresses, etc.) : Goth. hals, OE heals, ete., general Gme. word for ‘neck’, all prob. fr. IH *Kel- ‘turn around’ in Skt. car-, Grk. mé\ouat, etc., also Lith. kaklas ‘neck’ (below, 5), rather than fr. *kel- ‘rise, project’ in celsus ‘high’, collis ‘hill’, etc., though either connection is possible phonetically, and semantically accord- ing as the words orig. denoted the (round) neck’ or the ‘nape of the neck’. Ernout-M. 204. Walde-H. 1.245 (vs. Walde-P. 1.434). Feist 242.
Rum. git, orig. ‘throat’ (hence gitle7 ‘throat’), loanword fr. Slavic, SCr. gut ‘throat’ (obs., but gutati ‘swallow’), Slov. golt ‘throat’, Bulg. giiltitk ‘a swal- low’, etc., these : Lat. gula ‘throat’, etc. (4.29). Tiktin 684. Berneker 309.
3. Ir. brage ‘neck’ and rarely (inner) ‘throat’ (cf. K. Meyer, Contrib. 8.V.), Nir. bragha mostly ‘throat’ : MHG krage (below, 4), Grk. Bpéx6os ‘throat’,
Digitized by Arya Samaj Foundation Chennai and eGangotri
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
SELECTED INDO-EUROPEAN SYNONYMS
Skt. gr- ‘swallow’, Lith. gerti ‘drink’, ete. Walde-P. 1.683. Pedersen 1.100, 183.
Ir. muin, muinél ‘nape of the neck’? NIr. muinéal ‘neck’, W. mwn (arch,), mwnwgl ‘neck’: ON men, OE mene ‘necklace’ (also OF manu ‘mane’, etc.), Lat. monile ‘necklace, collar’, Skt. manya- ‘nape of the neck’, Av. miny, ‘necklace’, manaobri- ‘neck’ (both words in Yt. 5.127, cf. Barth. 1126), all prob, fr. IE *men- ‘project’ in Lat. eminére, prominere ‘project’, mons ‘mountain’, etc. Walde-P. 2.305, 265. Pedersen 1.33.
W. gwddf, Br. gouzoug (both also ‘throat’), etym.? Pedersen 1.63. Henry 142. Morris Jones 145 (cf. Loth, RC 36.170).
4. Goth. hals, etc., above, 2.
ON sviri, OE swéora, swira (so, not heals, always in the Gospels), ME swere (cf. NED s.v. swire) : OE swer, sweor ‘column’, Skt. svaru- ‘post’, etc. Walde- P. 1.528.
ME necke, NE neck, fr. OF hnecca ‘nape of the neck’ : ON hnakki, OHG hnac, NHG nacken, etc. general Gime. for ‘nape of the neck’, prob. : Ir. cnoc ‘hill’, etc. Walde-P. 1.391. Falk-Torp 754,
MHG krage ‘neck, throat, collar’ (NHG kragen ‘collar’, rarely ‘neck’, Du. kraag ‘collar’; ME crawe, NE craw with only specialized meaning) : Ir. brage, etc. above, 3.
5. Lith. kaklas, Lett. kakls : Grk. xbxdos ‘circle’, Skt. cakra- ‘circle, wheel’, OE hweol ‘wheel’, etce., fr. IE *kel- ‘turn’, as prob. also Lat. collum, Goth. hals, etc. (above, 2). Walde-P. 1.515.
6. ChSl. vyja (so always in Gospels, Supr., etc., sija only in later texts), etym.? Lowenthal, Z. sl. Ph. 8.129, connects with Av. uyamna- ‘lacking; deficient’ (Walde-P. 1.108) as if orig. ‘neck-hole’ (in a garment).
of THE BO
Sia ‘neck’ of Sia (SCr. se ‘nec
is e, Pol. szyja, Russ. geese etc. ’, Wiedemann, BB sca iit, "4 Lat. sinus ‘fold’ fr. a i wa root meaning ‘bend’. eae don fjklosiob, Lex. 8.V-) : Skt. st-, rt : at siet ‘bind’, ChSI. sé% ‘cord’, oT siia joist’, ete. (Walde-P. 2.468 fi; Lith. zt %ja). Form (with § for s fr. a Lane form with 3j-) like Lith. sya, es development like that in Lat. §
late fess ons. ( Boh. Sj
ChSl. vrtitéti, vratiti, Lat. vertere ue etc. (10.12). Walde-P. 1.275. Cf, fr. the same root, NPers. gardan ‘neck’ (*vartana-). Horn 903.
Boh. krk, Pol. kark (latter esp. ‘nape of the neck’) : Skt. krkata- joint of the neck’, prob. fr. same root as ChSl. si- kritéiti ‘contract’, etc. Walde-P. 2.569. Berneker 667 f.
7. Skt. griva- (in Vedic only pl. ‘ver-
Digitized by Arya Samaj Foundation Chennai and eGangotri
DY; BODILY FUNCTIONS AND CONDITIONS 2383
tebrae of the neck’), Av. griva- (Vend. 3.7, of a mountain called here the ‘neck’; elsewhere also ‘head’ or ‘back’ of Arazu- ra, name of a fiend; NPers. gariva ‘hill’) : Grk. d€pn, dep7 ‘neck’ (poet.), Arc. dépfa ‘ridge’ (so depas ‘ridge’), ChSI. griva ‘mane’, all prob. as orig. ‘throat’ : Skt. gr- ‘swallow’, Lith. gertz ‘drink’, Grk. Bi8pmacxw ‘devour’, etc. Walde-P. 1.683.
Skt. kantha-, prob. a Middle Indic form of a *kartra- (> *katta, *kattha-, then kantha- with the secondary nasali- zation frequent in Middle Indic), fr. *kvol-tlo-, deriv. of the same IE *kvel- ‘turn’ as in Lith. kaklas, Lat. collum, Goth. hals, etc. (above, 2). Tedesco (to appear in JAOS).
Skt. girodhara-, lit. ‘head-supporter’, epd. of giras- ‘head’ and dhr- ‘hold’.
Av. manaoéri-: Ir. muin, etc., above, 3.
4.29 THROAT Grk. ards, chayy Goths. Lith. gerkleé NG aids ON  kverkr (pl.), strjapi Lett. _rikle it fancés, iugulum, gula Dan. _ strube ChSl. griilo x gola, strozza Sw. slrupe SCr.  grlo Sp, paras OE —_ceole, hrace protu Boh. hrdlo Rum fae a gola ME ethrote (rake) Pol. _ gardlo Ir ie eae NE throat Russ. gorlo Nit. scornach Du. keel, strot Skt.  gala- W. guddf OHG  kela, drozza Av. garaman- (in pl.), Br. gouzoug aS ile drozze garo (pl.) ehle Most of the ; both the ean ae are used for | true, as in Lat. cugulum and the group But the L and external throat. | including NE throat. Extension from
ae atin terms are differentiated, aie no single word with the Ope of NE throat. The common-
&St semanti ; Ntic source je ¢ . With some o °e 1s ‘swallow’, which
ie ts, as ‘gurgle’, ‘abyss’ fate �� ee ‘narrow opening’ indi. ie Ppkeation to the internal
&® lew cases the Opposite is
‘throat’ to ‘neck’ has been noted in 4.28.
1. Derivs. of vbs. for ‘swallow, de- vour’ either 1) IE *gel- in Ir. gelim, etc.; or 2) IE *g“er- in Skt. gr-, Grk. BrBpacxa, Lat. vorare, etc.
TE *gel-. Walde-P. 1.621. Ernout- M. 437. Walde-H. 1.625 f.
Lat. gula ‘throat (internal), gullet’
```


## [2026-09-06T14:55:17.861Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nfor s in ['gargəlo, ið','gargəlos, à','gulgul-, gulugul- ‘gurgle’']:\n    i=t.find(s)\n    print(repr(s[:12]), 'leaf0', t[:i].count('\\f'))\n\"; echo \"=== AHD gwer\"; grep -n \"g^wer\\|gwer\\|gʷerə\\|vorare\\|bronchos\\|gargle\" AHD_watkins1985.txt | head -20",
 "description": "IEC leaves and AHD"
}
```


### [2026-09-06T14:55:20.403Z] TOOL RESULT

```
'gargəlo, ið' leaf0 857
'gargəlos, à' leaf0 158
'gulgul-, gul' leaf0 180
=== AHD gwer
1044:s(w)eks. Six. I. Form *seks. 1. Germanic *seks in Old English s(iJex, six, six: sIx. 2. Latin sex (> Italian sei), six: SENARY, SEX-; SEICENTO, SEMESTER. 3. Suffixed form *seks-to- in Latin sextus, sixth: SESTET, SESTINA, SEXT, SEXTAN, SEXTANT, SEXTILE; SEXTODECIMO. II. Form *sweks in Greek hex, six: HEXA-, HEXAD. [Pok. sueks 1044.] swel-', To eat, drink. 1. Perhaps Germanic *swil- in Old English swilian, to wash out, gargle: swILL, 2. Extended form *swelk- in Germanic *swelgan, *swelhan in Old English swelgan, to swallow: SWALLOW!; GROUNDSEL!. 3. Iranian *khvdra- (attested in Avestan), to eat, in the probable source of Greek mantikhdras, manticore (see mer-?). [Pok. 1. suel(k)- 1045.] swel-2, To shine, burn. 1. Extended form *sweld- in Germanic *swiltan in Old English sweltan, to die, perish (perhaps < “be overcome with heat”): (SULTRY), SWEL- TER. 2. O-grade form *swol- in Germanic *swal- in Old Norse svalr, cool (< “lukewarm” < “hot”), akin to the Scandinavian source of Middle English swale, shade, shady place: SWALE. [Pok. 2. swel- 1045.]
1309:BITE bheid- BITTER bheid- BITTERN! beu-2 BITUMEN gWet-1 BIVOUAC ambhi, weg-2 BLACK bhel-1 BLACKMAIL méd- BLADDER bhié-2 BLADE bhel-3 BLAIN bhlei- BLAME bha-2 BLANCH bhel-1 BLANCMANGE bhel-1 BLAND mel-1 BLANDISH mel-1 BLANK bhel-1 BLANKET bhel-1 BLARE bhié-1 BLASPHEME bha-2 BLASPHEMOUS bha-2 BLAST bhlé-2 -BLAST melst- BLASTEMA melst- BLASTO- melst- BLASTULA melst- BLATHER bhlé-2 BLAZE! bhel-1 BLEACH bhel-1 BLEAK! bhel-1 BLEAK? bhel-1 BLEAT bhlé-1 BLEMISH bhel-1 BLENCH! bhel-1 BLEND bhel-1 BLENDE bhel-1 BLENNY mel-1 BLESBOK bhel-1, bhugo- BLIND bhel-1 BLINDFOLD bhel-1 BLINI mele- BLINTZ mele- BLISTER bhlei- BLITE mele- BLITZKRIEG bhel-1, gwere-2 BLOAT bhieu- BLOND bhel-1 BLOOM! bhel-3 BLOOM? bhel-3 BLOSSOM bhel-3 BLOW! bhié-2 BLOW3 bhel-3 BLUE bhel-1 BLUNDERBUSS (s)tene- BLUSH bhel-1 BOARD bherdh- BOAST! beu-1 BOAT bheid- BOATSWAIN bheid- BOCACCIO beu-1 BODE! bheudh- BODEGA dhé-1 BODHISATTVA bheudh-, es- BoER bheue-
```


## [2026-09-06T14:55:28.843Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==159' IEC.txt | head -8; echo \".....\"; awk 'BEGIN{RS=\"\\f\"} NR==159' IEC.txt | tail -5; echo \"=== leaf 181\"; awk 'BEGIN{RS=\"\\f\"} NR==181' IEC.txt | head -5",
 "description": "IEC leaf 158/180 page numbers"
}
```


### [2026-09-06T14:55:31.056Z] TOOL RESULT

```
��, but poss. denom. of gallus, cf. gagol-); MHG kalzen, kelzen *bawl'; kelz “loud talk’; OFris. kaltia “talk”; Du. kouten chat": kout, s. id.; R. cf. galdét ('brawl', but the phonol. is irregular) galið *shout'. Cf. gald-, galu- Gk. cf. a-gállo ‘glorify’; MHG kallen ‘shout, chatter, sing, croak’; Du. G kallen ‘chatter’; LG kohlen, id.; Tirol. kallen ‘bellow, rut; OE ceallian: ON kalla (“calP', etc.). Cf. also Alb. galé ‘rook’; Br. gal-dü “black sea-bird"; OE -calla *-crier'. (Ambig. or variant in Skt. járe, Av. jar- ‘creak, rustle; call’, cf. &el-) galuó ‘call’. Cf. galið, gald-; galuos, s. Skt. cf. garvah ‘pride’; Br. galv ‘appeal’; W galw ‘call, vocation’; Ir. (?) gailbh ‘squall’;
10
20
25
30
35
40
45
.....
gareio, (ið, aio) ‘mourn’. Cf. garos, garā above Olr. gairim ‘cal’; OHG karōn, karen, OS
265
karon, MHG karn 'mourn'; G Kären, id.; OE carian ‘grieve, care’; Sw kära ‘complain, lay a charge’; ON cf. kor, gs karar ‘sickbed’; Icel. kárna ‘deteriorate’; OCS cf. gorije ‘woe’; Li. gariù, Eti ‘wane, waste away”
gargəló, ið (gərgəl-) ‘gargle, gurgle’. cf. ghargəl- (ghərghəl-). Onomat. Skt. gárgarah ‘whirlpool’; gargara ‘churn’: Gk. cf. gargareón 'gullet; LLat. gargala ‘wind- pipe’; Li. gargaliuoti ‘be hoarse’; It. gar- gagliare (‘babble, purl’, beside gorgogliare, id.). See next
gargəlos, à ‘babbling, raucous; babble, bubbling, gurgle, croak’. Onomat. Cf. WP I, . 538 & 683 Skt. gárgarah, gargarā; Per. yaryara ‘gurgle’; Gk. gárgalos (2), id.; Alb. gárgull ‘starling’; LLat. gargala ‘windpipe’; Li. gargalas, m. ‘hoarse spe
=== leaf 181
Küchlein; Du. kuiken, id.; Li. gužas 'stork'; Alb. guzé (“coot is ambig. perh. *gugio or *gudio)
gügh- ‘huddle, hide, squat, crouch together; hiding-place, hole’. Cf. WP I, 566-7 & 638 Skt. gühami “hide”; guh, guha *hiding-place';
güd- — gulg- (gulgu-)
20
25
```


## [2026-09-06T14:55:36.893Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==181' IEC.txt | grep -nE \"^[0-9]{3}$\" ; echo \"---context\"; awk 'BEGIN{RS=\"\\f\"} NR==181' IEC.txt | grep -n -A3 -B3 \"gulgul-, gulugul- ‘gurgle’\"",
 "description": "IEC page 305 check"
}
```


### [2026-09-06T14:55:38.788Z] TOOL RESULT

```
10:304
18:305
---context
17-gulg- (gulgu-) ‘gulp, gurgle; belch’. See gul-, gulgul- & glgos Per. (ambig.) gulū (2) ‘gurgle; Arm. cf. klklunk' (redup.), id.; Alb. gullgulloj ‘babble, purľ; Lat. cf. in-gluvies ‘craw’; Ir. glug ‘gurg- le’; MHG kolc, gs -kes ‘whirlpool’; G Kolk, id. cf. Kolk-rabe, wm. ‘caw-crow’; Du. kolk ‘whirl- pooP: OFris. kolk ‘ditch’; Du. cf. kolken, v. ‘ddy’; OE cylcan ‘belch’; Slovak (LW fr. Slovene) gl-gotat ‘gulp’; glg, m. id.; Pol.
18-305
19-(variant) gulgotać ‘gargle’; Blg. glág ‘heart- burn’; Latv. guldzu, it ‘gulp’; gulgāties, v. ‘belch’
20:gulgul-, gulugul- ‘gurgle’. Cf. gul-, gulg-. WP I, 683 Per. yulyul ‘clamour’; Arm. klklunk, s. ‘gurgle’; Alb. gullgulloj, v. ‘purl, babble’; G cf. kluckern ‘bubble out of a bottle’; Blg. gălăgăl ‘bubble- bubble from a bottle’
21-gulos, ios ‘ball’. See gūl- & cf. WP I, 556 Skt. gulah, id.; Oss. gurä ‘mass’; Gk. gullós *gaming-die'; Alb. gul (3) ‘blockhead’, fr. *eulis; Du. kul (‘phallus’, fr. *gulis)
22-gulquios, iə (?). See next, and cf. guluk- Alb. gulçë ‘asthma’; Big. gălč ‘din, bluster’
23-gult- (gult-?) ‘gulp’. Cf. glut- (1) Arm. cf. hec-kltam ‘sob’; Lat. cf. sin-gultio, id. (sin- unexplained); Blg. (ambig.) gáltam ‘swallow’; Cz. (ambig.) hitit, id.
```


## [2026-09-06T14:55:47.378Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gwera-1\\|gwers-\\|To swallow\" AHD_watkins1985.txt | head; echo \"===\"; grep -o \"gwera-1[^.]\\{0,80\\}\" AHD_watkins1985.txt | head -5",
 "description": "AHD gwerə-1"
}
```


### [2026-09-06T14:55:48.992Z] TOOL RESULT

```
540:(COVEN), (COVENANT), EVENT, INTERVENE, INVENT, MIS- ADVENTURE, PARVENU, PREVENIENT, PREVENT, PROV- ENANCE, (PROVENIENCE), REVENANT, REVENUE, SOUVENIR, SUBVENTION, SUPERVENE. 3. Suffixed zero-grade form *gvm-yo- in Greek bainein, to go, walk, step, with basis (< *gm-ti-), a stepping, tread, base, and -batés (< *gwa-to-, zero-grade of gd-, contraction of *gaa-), agential suffix, “one that goes or treads, one that is based”: BASE!, BASIS; ABASIA, ACROBAT, ADIABATIC, AMPHISBAENA, ANABAENA, DIABASE, DIABETES, STEREO- BATE, STYLOBATE. 4, Suffixed zero-grade form “g“(g)-u- in compound form “pres-gu-, “going before” (see per’). 5. Basic form *gvd- in Greek béma, step, seat, raised platform: BEMA. 6. Sanskrit jigdti, he goes: JUGGER- NAUT. [Pok. g¥d- 463.] gvadh-. To sink. Possible root. 1. Suffixed form *guadh-u- in Greek bathus, deep (> bathos, depth): BATHOS, BATHY-. 2. Greek benthos, depth, may be formed on bathus by analogy with penthos, grief, and pathos, passion, suffering (or it may be from an unrelated root *g¥(e)ndh-): BENTHOS. 3. Suffixed variant form *gudh-yo- in Greek bussos, bottom of the sea: ABYSS. [Pok. gddh- 465.] g’ébh-'. To dip, sink. Suffixed zero-grade form *gvabh-yo- in Greek baptein, to dip: (BAPTIST), BAPTIZE; ANABAPTIST. [Pok. g¥ébh- 465.] g”ébh-2. Hypothetical base of some Germanic words associated with the notion of sliminess. 1. Middle Dutch quac-, unguent, liquid, in obsolete Dutch quacksalver, quacksalver: QUACKSALVER. 2. Low German quabbeln, to shake like jelly, tremble, akin to Middle English quaven, to tremble: QUAVER. [Pok. 2. g¥ébh- 466.] grei-. Also gveia-. To live. I. Suffixed zero-grade form *gwi-wo-, *gi-wo- (< *gi9-wo-), living. 1. Germanic *kwi(k)waz in: a. Old English cwic, cwicu, living, alive: QUICK, QUICKSILVER; b. as a name for couch grass (from its rapid growth), in Old English cwice, couch grass: (COUCH GRASS), QUITCH GRASS. 2. a. Latin vivus, living, alive: VIVIFY, VIVIPAROUS; b. Latin denominative vivere, to live: VIAND, VICTUAL, VIVA, VIVACIOUS, VIVID; CON- VIVIAL, REVIVE, SURVIVE. 3. Further suffixed form *gvi- wo-td in Latin vita, life: VIABLE, VITAL; LIGNUM VITAE, VITAMIN. II. Suffixed zero-grade form *gia-o- in Greek bios, life (> bioté, way of life): BIO-, BIOTA, BIOTIC; AEROBE, AMPHIBIOUS, ANABIOSIS, CENOBITE, MICROBE, RHIZOBIUM, SAPROBE, SYMBIOSIS. III. Variant form *gwyd- (< *gvyoo-). 1. Greek z0é, life: AzO-, (DIAZO). 2. Suffixed form *gvy6-yo- in Greek zdon, zdion, living being, animal: (-Z0A), -ZOIC, ZOO-, ZOON, -ZOON. IV. Pre- fixed and suffixed form *su-g~ia-es- (*su-, well; see su-), “living in good condition,” in Greek hugiés, healthy: HYGEIA, HYGIENE. [Pok. 3. gei- 467.] g”eia-. To press down, conquer. Sanskrit jayati, he con- quers: JAIN. [Pok. gveio- 469.] gvel-'. To pierce. 1. Suffixed o-grade form “gvol-eyo- in Germanic *kwaljan in Old English cwellan, to kill, destroy: QUELL. 2. Suffixed zero-grade form *g“/-yo- in Germanic *ku/jan in Old English *cyllan, to kill, perhaps the source of Middle English killen, to kill: KILL}. 3. Full-grade form *gvel- in Greek beloné, needle: BEL- ONEPHOBIA. [Pok. 1. g¥el- 470.] gel-2. To fly; a wing. Possibly in Latin voldre, to fly: VOLANT, VOLATILE, VOLE2, VOLITANT, VOLLEY. gvel-3, To swallow. Dissimilated to *gel-. 1. Germanic *kel- in Old English ceolu, throat, dewlap, perhaps akin to Middle English cholle, throat: JowL?. 2. Germanic *keluz in Old Norse Aj6ir, keel: KEEL}. 3. Suffixed zero-grade form “gul-d in Latin gula, gullet, throat, palate: GOLIARD, GULAR, GULES, GULLET. 4, Extended (expressive) form *glutt- in: a. Latin gluttire, gliitire, to swallow: GLUT; DEGLUTITION; b. Latin glutté, a glutton: GLuTTon. [In Pok. 2. gel- 365.] gvelbh-. Womb. 1. Suffixed form *gvelbh-u- in Greek delphus, womb, whence delphis, dolphin (referring to its
542:shape): DELPHINIUM, DOLPHIN. 2. Prefixed and suffixed form *sm-gvelbh-o-, “born of one womb” (*sm-, one; see sem-'), in Greek adelphos, brother: -ADELPHOUS. [Pok. gtelbh- 473.] gvele-1. To throw, reach. Variant *g/é-, contracted from *guleg-, 1. Suffixed zero-grade form *g/-n-o- in: a. Greek ballein, to throw (with o-grade *bol- and variant *b/é-): BALLISTA; AMPHIBOLE, ASTROBLEME, CATABOLISM, DEVIL, (DIABOLIC), (EBLIS), ECBOLIC, EMBLEM, EPIBOLY, (HYPERBOLA), HYPERBOLE, METABOLISM, (PALAVER), PARABLE, (PARABOLA), (PARLEY), (PARLIAMENT), (PAR- LOR), (PAROL), (PAROLE), PROBLEM, SYMBOL; b. Greek ballizein, to dance: BALL?, (BALLAD), (BALLET), BAYA- DERE. 2. Suffixed o-grade form *gvols-d in Greek bolé, beam, ray: BOLOMETER. 3. Suffixed o-grade form *gwolo-sdé in Greek boulé, determination, will (< “throw- ing forward of the mind”), council: BOULE!; ABULIA. 4. Suffixed variant zero-grade form *gvele-mno- in Greek belemnos, dart, javelin: BELEMNITE. [Pok. 2. g¥el- 471.] gwela-2, An acorn. 1. Suffixed zero-grade form *g¥/o-nd- in Latin gldns (stem gland-), an acorn: GLAND, GLAN- DERS, (GLANDULAR), GLANS. 2. Suffixed zero-grade form *gulg-no- in Greek balanos, acorn, date: VALONIA; MYRO- BALAN. [Pok. 3. gvel- 472.] gven-. Woman. 1. Suffixed form *gven-d- in: a. Germanic *kwen6n- in Old English cwene, woman, prostitute, wife: QUEAN; b. Old Irish ben (> Irish Gaelic bean), woman: BANSHEE; C. Persian zan, woman: ZENANA. 2. Suffixed lengthened-grade form *gvén-i- in Germanic *kwéniz, woman, wife, queen, in Old English cwén, woman, wife, queen: QUEEN. 3. Suffixed zero-grade form *g“n-d- in Greek guné, woman: GYNO-, -GYNOUS, -GYNY; GYNAE- CEUM, GYNECOCRACY, (GYNECOLOGY), POLYGYNY. [Pok. gvend 473.) g”ere-'. Mountain. Possibly o-grade form *gvors- in: a. Greek boreios, “coming from the north” (? < “coming from the mountains of Thrace, north of Greece”), whence Boreas, the north wind: Boras; b. Greek Huperboreioi, Huperboreoi, name of a people living in the far north, variously explained as “they who live beyond the north wind” and “they who live beyond the mountains” (hu- per-, beyond; see uper): HYPERBOREAN. [Pok. 3. gver- 477.) gvere-2. Heavy. I. Zero-grade form *gra-. 1. Suffixed form “g“ra-u-i- in Latin gravis, heavy, weighty: GRAVE?, GRAVID, (GRIEF), GRIEVE; AGGRAVATE, AGGRIEVE. 2. Suffixed form “gro-u- in: a. Greek barus, heavy: BARITE, BARITONE, (BARIUM), BARYON, (BARYSPHERE), BARYTA; b. Sanskrit guru-, heavy, venerable: GURU. 3. Suffixed form *gro-es- in Greek baros, weight: BAR?, BARO-; CENTROBARIC, ISALLOBAR, ISOBAR. 4. Possibly *guri- in Greek bri- in compound *u(d)-bri- (see ud-). II. Suffixed extended form *g-rii-to- in Latin britus, heavy, unwieldy, dull, stupid, brutish: BRUT, BRUTE. III. Suffixed extended form *g»ri-g- in: a. Celtic *brig-o-, strength, in Italian brio, vigor: BRIO; b. Germanic *krig- in Old High German krég, chrég, stubbornness (> Ger- man Krieg, war): BLITZKRIEG, SITZKRIEG. IV. Suffixed full-grade form *gvero-nd-, millstone, in Old English cweorn, quern: QUERN. [Pok. 2. g¥er- 476.] gvere-*. To praise (aloud). 1. Suffixed zero-grade form *gvra-to- in Latin grdtus, pleasing, beloved, agreeable, favorable, thankful: GRACE, GRATEFUL, GRATIFY, GRATIS, GRATITUDE, GRATUITY; AGREE, CONGRATULATE, IN- GRATE, INGRATIATE. 2. Suffixed zero-grade form *gwro-do-, “he who praises,” in Celtic bardo-, bard, in Welsh bardd and Scottish and Irish Gaelic bard, bard: BARD}. [Pok. 4. gver(a)- 478.] gvere-4. To swallow. 1. Possibly suffixed extended form *gro-gh- in Germanic *krag-, throat, in: a. Old English *craga, throat, possible source of Middle English crawe, craw: CRAW; b. Middle Dutch craghe, throat: scrac. 2. Suffixed o-grade form *gvor-d- in Latin vordre, to swallow up: VORACIOUS, -VOROUS; DEVOUR. 3. Expres-
===
```


## [2026-09-06T14:55:56.484Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o \"gvere-4\\. To swallow\\..\\{0,1400\\}\" AHD_watkins1985.txt | head -1",
 "description": "Full AHD gwerə-4"
}
```


### [2026-09-06T14:55:58.564Z] TOOL RESULT

```
gvere-4. To swallow. 1. Possibly suffixed extended form *gro-gh- in Germanic *krag-, throat, in: a. Old English *craga, throat, possible source of Middle English crawe, craw: CRAW; b. Middle Dutch craghe, throat: scrac. 2. Suffixed o-grade form *gvor-d- in Latin vordre, to swallow up: VORACIOUS, -VOROUS; DEVOUR. 3. Expres-
```


## [2026-09-06T14:56:01.236Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('AHD_watkins1985.txt',encoding='utf-8',errors='replace').read()\ni=t.find('gvere-4. To swallow')\nprint(t[i:i+2200])\n\"",
 "description": "AHD gwerə-4 full text"
}
```


### [2026-09-06T14:56:02.934Z] TOOL RESULT

```
gvere-4. To swallow. 1. Possibly suffixed extended form *gro-gh- in Germanic *krag-, throat, in: a. Old English *craga, throat, possible source of Middle English crawe, craw: CRAW; b. Middle Dutch craghe, throat: scrac. 2. Suffixed o-grade form *gvor-d- in Latin vordre, to swallow up: VORACIOUS, -VOROUS; DEVOUR. 3. Expres-
25
g"hi-
sive reduplicated form *gr-g- in Latin gurges, throat, also gulf, whirlpool: GARGET, GORGE, GORGET, GURGITA- TION; INGURGITATE, REGURGITATE. 4. Extended form *gwr6- (< *geroa-) in Greek br6- in: a. suffixed redupli- cated form bi-bré-sko- in Greek bibréskein, to eat: HELLEBORE; b. nasalized variant form *bro-n-kh- in Greek bronkhos, windpipe, throat: BRONCHO-, BRON- CHUS; C. suffixed form *gvré-mn in Greek bréma, food: THEOBROMINE; d. suffixed form *gvr6-ti- in Greek bro- sis, eating: ABROSIA. [Pok. 1. gver- 474.] gwes-. To extinguish. Suffixed variant form *sgves-nu- in Greek sbennunai, to extinguish: ASBESTOS. [Pok. g¥es- 479.] g”et-'. Resin (?). Only in Germanic and Celtic. Suffixed form *gvet-u- in: a. Germanic *kwithu- in Old English cwudu, cwidu, cudu, resin, mastic gum, “that which is chewed,” cud: CUD, QUID!; b. Celtic *betu-, birch, birch resin, in Latin bitumen, resin (Gaulish loanword): BITU- MEN. [Pok. 1. g¥et- 480.] gwet-2. To say, speak. Germanic *kwithan in Old English cwethan, becwethan, to say, speak: BEQUEATH, BEQUEST, QUOTH. [Pok. 2. g¥et- 480.] gvet-3. Intestine. Suffixed o-grade form *gvot-olo- in Latin botulus, intestine, sausage: BOTULINUM, BOTULISM, BOWEL; (BOTULIN). [Pok. gvet- 481.] ghedh-. To ask, pray. 1. Germanic *bidjan, to entreat, in Old English biddan, to ask, pray: BID. 2. Germanic *bidam, entreaty in Old English gebed (ge-, intensive and collective prefix; see kom), prayer: BEAD. [Pok. gehedh- 488, 2. bhedh- 114.] gvhen-'. To strike, kill. 1. O-grade *gvhon- in Germanic suffixed form *ban-6n- in: a. Old English bana, slayer, cause of ruin or destruction: BANE; b. Middle High German ban, bane (> German Bahn), way, road (? < “path hewn through woods”): AUTOBAHN. 2. Suffixed zero-grade form *ghn-tyd- in Germanic *gundjé, war, battle, in: a. Old Norse gunnr, war: GUN; b. compound *gund-fanon-, “battle f
```


## [2026-09-06T14:56:15.374Z] TOOL CALL #34: Bash

```json
{
 "command": "ls data/verification/sources/refs/ocr/ 2>/dev/null | head; echo \"---\"; python3 tools/ref_page.py BQT:1807 2>&1 | head -40",
 "description": "Fetch BQT page 1807"
}
```


### [2026-09-06T14:56:24.489Z] TOOL RESULT

```
AFM
ARY
BOOK
BQT
HRN
IRN
PLA
SNS
SOD
---
(no exact page map; using offset -1205 -> pdf page 602; check the printed number and re-run with --pdf-page if off)
REF: BQT:1807  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 602  OCR-lang: fas

ولا گریبانی
آب میشود وبته‌آب می‌نشیند - واند کی‌ازساعت | وکری که پنگان (۱) است دراب دشیند چویی
شبالروزیرا لیز کری کوبند وآن بیست ودودقبقه | برآن تختهٌ هقت جوش‌زنندتاصدائی کند.مردمان
وسی‌ثانيةٌ ساعت باشد - وبمعنی گر بودن۷ بعنی | دانند که چه مقدار از روز با ازشب گذشته‌است,
علت جرب داشتن هم‌هت - وبکر اول وئانی | و این در هندوستان متعارف است .
بمعنی گربه است ۴ - و امن بگربه کردن باشد گریان - بکراول معروفت که گربه
بعنی گربه کن ۴ - و مخفف کیری هم‌هست. که کنان باشد۸ - وجم اول» بمعنیآتشدان کرمابه
ا زگرفتن باشد ۴ - و با تحتانی مجهول, بمعنی باشد وآ بر گلخن هم میگوبند - وبمعنی فداهم
گره باشد ‎٩‏ مطلقاً اعم زگره رسمان و چوب | هت یعنی بدلی که خود را پا دیگربرا بدان از
و امثال آن - وگردن را نیز گوبند که بعربی بلا نجات‌دهن ‎٩‏ .36
جید خوانند و ازین جهت است که بخيةٌ جامهرا گریبان دامن کردن - کنابه از
کریبان میگوبند ‎٩‏ بعتی نگه دارندةکردن‌چه مرافیه کردن وسربگرببان فروبردن باشدمردمان
بان بمعنی‌نگه دارنده است؛ ودردیگ بربان‌پلاو دروش و صاحب حال را .
نیزمحاذی گردن گوسفند بربان را کربگاه ید گریبا نی یس بکسر اول پیراهن‌و گرته
خوانند ,منی جای کردن . راگوبند و بعربی سربال خوانند *۱- وپوستیرا
گر بال ۷ - بر وزن ابدال , نخته ای یز گوبند که بر (۳) کریبان پوستین و کاتبی
باشدازهفت جوش که چون زمانی‌ازساعت بگذرد | دوزند .
(۱) چش : بنکان . (۷) چش : گربگاه ! (۳) چش : - بر .
۱ - از :کر دی (حاصل مصدر » اسم ممنی).
۴ - ریشهٌ قعل «کربستن » (۸م.) و«گربیدن» :
جز از اوکس ندیده از بشری در طلب گاه خنده کاهگری .
سنائی غزنوی «فرهنگه نظام» -
۴ -رك :گریتن . ۴ - رك : گرفتن . ۵ سکره .
‎٩‏ - اوستا 8۲1۷8 (گردنه [ کوه] ) » پهلوی 871۷81 ( کردنه [ کوه] ) . هندی
باستان 871۷8 ( پشت کردن ) « اسشق ۹۱۳ رك :کرببان . ۷ - از هندی «گهربال»
با های مختفی و رای هندی . تاکنون نیز در هندوستان رسم است که بر درگاه بزرگان تختهٌ
فلزی آویشته است و سرهرساعت قراول با چوب عدد ساعت شبانه روزی را برآن می‌نوازد وآن
را «گهربال > گوبند ۵ فرهنگه نظام » . ۸ - از :گری (کربتن) ان ( پسوند صفت
فاعلی وحال ) ۰ ‎٩‏ -ظ . مصحف«* گربان» ۳ قربان . رك : کیربان, کربان .
*- امروز همی بمطربان بخشی وب شطری و شمر کرکانی
وزدست چوسنگه تونمی‌باید موذن بمئل یکی کرببانی .۰
ناصرخرو بلخی . دبوان ص 4۱۵ *.
5 گریبای - بکر اول . پپلوی 8048 - 8171۷ « اسشق ۹۱۳ » جزو اول در اوستا
83 (کردن ) (ر4:ح٩)‏ وجزو دوم پوند اتساف وحفاظت است , جممعاً بسنی محافظ گردن ؛
بخشی از جامه که اطراف گردن قرارگیرد :
سکه و دربان چو یافتند غریب این کربباش کبرد » آن دامن .
« کلتان ص ۰4۳۹
```


## [2026-09-06T14:56:36.729Z] TOOL CALL #35: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1832 2>&1 | head -50",
 "description": "Fetch BQT page 1832"
}
```


### [2026-09-06T14:56:45.557Z] TOOL RESULT

```
REF: BQT:1832  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 629  OCR-lang: fas

کننکین -۱۸۳۲-
کگلنگبین ۱ - بنم. اول و فتح نالی تحفه و هدیه بجایی فرستند - و چیزی باشد که
و سکون ثالك » ترکیبی باشد مانند کل قند آبرا ماد گلوبند از جوز و انجین سازندویجایی
لیکن ناوت آست که کل قند را با کل و قند | فرستند خصوصاً وآبراکلونده نیز کوبند - و نام
سازد وکلنگیین را با گل و انگبین که مل | کوحی یز هست .
باشد . گلوه - بنم اول ر سکون نالی وفتح
لو ؟ - بنم اول و ثانی بواوکشید. , |[ ثالت » سوراخ تنور نان پزی راگویند .
معروف است که حلق و حلقوم باشد . لوی 1 سیا < سوراخ وسط آسیا را
لو 3 - بنم اول وفتح فوقانی وظهود | کوبند که دانه از آن راء ریز تا آ ی گردد .
ها »کلاهی باشد گوشه‌دار پرینب ه که بیشتر چجهت کلوی سرخ « سرخ روده رآ گویند
طلنلان دوزند و کوشهای آرا در زبرچانه ابعان و آن محل گذشتن آب ودانه است .
بندند و وجه تسمیه‌اث, خود ظاهر است. جنه « بفتح اول و ثالی مشدد وغیرمشدد
گلور « بفتح اول‌پروزن تموز ۰ بممنی هردوآمده است » بمعنی کله ورمةٌ کوسفند وشتر
فندق باشد ۴ ؛ و بسی کوبند چلغوزه(۱)است! وخر وکاو وآهو و امثال آن باشد - وبضم اول
و بسن بادام کوهپراکفته‌اند ااملم» ومعرب‌آن | و فتح نانی مشدد , آسمان گیری باشد و آن
جلوز باشد . پارچه‌ایست که برسقف خانها ماشسایبان بندند-
لو له ؟ - بروزن و معنی غلوله‌است و موی جمع شده را نی زکوبند ‎٩‏ - و جم اول
که کروههٌ رسمان وغیره باشد . وفتح‌انی‌غیرمشدد» زلف معشوقرا میگوبند ‎٩‏ -
"لو ند * » بنتح اول پروزن فرزند » | و بکسر اول وافتح انی مخفف . شکوه وشکایت
مرسله راگوبند عموماً پمتی هرچیز که بطریق | باشد ۷ - و دانهٌ انگور که از خوشه جدا افتاده
(۱) خم۱: جلغوزه .
۱- از :گل (ٍم اول) ۲-انگیین (ه.م.)
۲ - دراوستا -8878 (کلو) » پهلوی 8270۵1 » سانسکربت -8818 بلاتینی 8118
قی ارمنی ۴۷ - ( فروبرده » بلمیده ) .کردی 86۳۵ . افغانی 80272 و 81872 (کردن:
قصبةالربه). استی ۹0۳ ( غیر قطعی ) » سنگلیجی 81187 «اسشق - هوبشمان ۹۲۸ خواناری
ناج . دزفولی 8011 « سالنامه کلپابگان 4۷ > ۰ کیلکی 811 »کردی 81060۲۵ » 81060۲1
(کلو » معبر تنگه) , 880۲1 ۰ 86720 , 82۷71 «زابا س۹-۳۹۸. ۰ ۴ * جلوز(معرب) .
- 2۷611202 0۶5[ر0) ۰ ثابتی ۲۱۰ >. ۴ «غلوله . فقس : هندی‌باستان -814۷
(صل . لنگه) .کردی 81187 (کرد ) . 181اع (کلوله ) . رك : اسشق - هوبشمان ۹۲۹ ؛
اضا کردی 11۵1 ( لوله » غلطیدن » سقوط سخت ) « ژابا مس ۳۸۱ ؛ ابا کردی 801۵16
(کلوله ) « ژابا س ۳۹۵ . 8 - رك : رشیدی .
-کردی 881 ( زلف زنان » دسَهٌ موی ) . زازا 8[16 « ژابا س ۳۷۰ >قس: کلاله.
۷ - پپلوی 121ع ( شکایت ؛ . پازند 18ج » از 5817402۴ از ۲221نع ( شکل
جنوب غربی ) . از 68728-862 از ( اوستابی ) 88762 « بارتولمه ۵۱۹ > « نیب رک س۱ ۰*۸
هندی باستان - 88710 .۰ 88712818 ( شکارت کردن » عارض شدن ) ,کردی 1اع ( شکایت ) :
( دعوی ) : استی 882۲210 . 837210 ( ناله کردن ) « اسشق ۹۳۰ .
```


## [2026-09-06T14:57:02.271Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"برونشیت\" \"پیاله\" \"غرغره\" \"گلاویز\" \"گریوه\"; do echo \"=== $w\"; grep -oh \".\\{0,160\\}$w.\\{0,200\\}\" MON_part1.txt MON_part2.txt 2>/dev/null | head -3; done",
 "description": "Grep Mo'in for words"
}
```


### [2026-09-06T14:57:19.552Z] TOOL RESULT

```
=== برونشیت
=== پیاله
=== غرغره
=== گلاویز
=== گریوه
```


## [2026-09-06T14:57:22.082Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la MON_part1.txt MON_part2.txt && head -c 600 MON_part1.txt",
 "description": "Check MON files"
}
```


### [2026-09-06T14:57:22.160Z] TOOL RESULT

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
و ده ها وی مزا موی
```


## [2026-09-06T14:57:25.565Z] TOOL CALL #38: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T14:57:25.573Z] TOOL RESULT

```


```


## [2026-09-06T14:57:28.948Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/پیاله/",
 "prompt": "Quote the فرهنگ معین entry for پیاله verbatim, including any bracketed origin tag (e.g. [یو.], [پهـ.], [ع.]). Also quote the دهخدا entry's etymology if given."
}
```


## [2026-09-06T14:57:30.775Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/پیاله",
 "prompt": "Give the full etymology section for the Persian word پیاله (piyāla) — what origin does Wiktionary give (Greek phialē? Old Iranian *pati-gāra-?), and what does it say about Sanskrit/Arabic cognates."
}
```


### [2026-09-06T14:57:36.271Z] TOOL RESULT

```
# Quotations from the Dictionary Entries

**From فرهنگ معین:**
"(لِ ) (اِ. ) ۱ - ظرفی که با آن شراب یا هر نوشیدنی دیگری را می نوشند. ۲ - یکی از لوازم آتشگاه"

**From لغت نامه دهخدا (Etymology section):**
"گویا اصل کلمه یونانی است و عرب از آن فیالجه ساخته است یا اینکه کلمه را یونانیها از ایرانیان گرفته و بهمین معنی بکار برده اند"

The دهخدا entry presents two possible etymological origins: either the word is Greek in origin and Arabs derived "فیالجه" from it, or Greeks borrowed it from Iranians and used it with the same meaning.
```


### [2026-09-06T14:57:38.354Z] TOOL RESULT

```
# Etymology of Persian پیاله (piyāla)

According to Wiktionary, the Persian word is "Inherited from Middle Persian (pygʾl /*paygāl/, 'cup, goblet')."

The article presents **two competing theories** for ultimate origin:

**Theory 1 - Ancient Greek Connection:**
The text notes that "a borrowing relationship with Ancient Greek φιάλη (phiálē, 'cup, bowl') has been suggested," though it acknowledges uncertainty since Greek itself may be a loanword.

**Theory 2 - Old Iranian Origin:**
Alternatively, the word may derive from Avestan patigāra ("a cup for drinking"), composed of Proto-Iranian *pati- plus a reflex of Proto-Indo-European *gʷerh₃- meaning "to swallow, devour."

**Regarding Sanskrit/Arabic:**
The page contains **no discussion of Sanskrit or Arabic cognates** for this entry. The descendants section lists several Arabic dialects (Gulf, Hijazi, Iraqi) that borrowed the word, but these represent later borrowing from Persian/Ottoman Turkish, not cognate origins.
```


## [2026-09-06T14:57:51.601Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"paiti\\.gar\\|patigär\\|paiti.gara\\|paiti-gar\" BRT.txt | head -5; echo \"(none means unattested)\"",
 "description": "BRT patigāra check"
}
```


### [2026-09-06T14:57:51.651Z] TOOL RESULT

```
(none means unattested)
```


## [2026-09-06T14:57:53.326Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/w/index.php?title=%D9%BE%DB%8C%D8%A7%D9%84%D9%87&action=raw",
 "prompt": "Show the Persian etymology section wikitext verbatim, including all reference templates and cited authors."
}
```


### [2026-09-06T14:57:59.799Z] TOOL RESULT

```
# Persian Etymology Section

Here is the Persian etymology section wikitext verbatim:

```
===Etymology===
{{ety|fa|:inh|pal:<tr:pygʾl><ts:*paygāl>|tree=1}}
{{inh+|fa|pal|tr=pygʾl|ts=*paygāl|t=cup, goblet}};<ref>{{R:pal:Mackenzie|*paygāl|page=67}}</ref> compare {{cog|mzn|پیلکا|tr=pilëkā}}, {{cog|sog|tr=ptγ'δ|t=cup}}, {{cog|kho|tr=phalau|t=flat dish, bowl}}.<ref name=iranica>http://www.iranicaonline.org/articles/greece-xiii</ref> Further origin is {{unc|fa|disputed}}:
* A borrowing from or otherwise cognate form of {{der|fa|ae|𐬞𐬀𐬙𐬌𐬔𐬁𐬭𐬀|t=a cup for drinking}}, from {{cog|ira-pro|*pati-}} + a reflex of {{inh|fa|ine-pro|*gʷerh₃-|t=to swallow, devour}}.<ref>{{R:fa:Nourai|page=180|head=Gwer 3, Gwere 2: to swallow}}</ref>
* A borrowing relationship with {{der|fa|grc|φιάλη|t=cup, bowl}} has been suggested,<ref name=iranica/> though the {{cog|el|-}} is itself thought to be a loanword, making the ultimate direction unclear.
```
```


## [2026-09-06T14:58:06.257Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -on \"paygāl[^]]*\\]\\|paygal[^]]*\\]\\|pyg.l\" PHD.txt PHD_mackenzie.txt | head -10; echo \"=== SOD ptg'd\"; grep -n \"ptγ\\|ptg'δ\\|جام\" SOD.txt | head -10",
 "description": "MacKenzie paygāl, Sogdian"
}
```


### [2026-09-06T14:58:06.324Z] TOOL RESULT

```
PHD.txt:547:paygal [pyg'l | N payyāla, piyála]
PHD_mackenzie.txt:4143:paygal [pyg)ll N payyiila, piyiila]
=== SOD ptg'd
```


## [2026-09-06T14:58:09.204Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '547p' PHD.txt | grep -o \".\\{0,200\\}paygal.\\{0,200\\}\"",
 "description": "MacKenzie paygāl context"
}
```


### [2026-09-06T14:58:13.195Z] TOOL RESULT

```
Exit code 2
ugrep: error: error at position 84
xbf][\x80-\xbf]*){0,200}
                        \___exceeds complexity limits
```


## [2026-09-06T14:58:15.949Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport io\nl=open('PHD.txt',encoding='utf-8',errors='replace').readlines()[546]\ni=l.find('paygal')\nprint(l[max(0,i-200):i+200])\n\"",
 "description": "MacKenzie paygāl context"
}
```


### [2026-09-06T14:58:17.815Z] TOOL RESULT

```
ibility, appearance. paydagénidan, paydagén- [ ГОР hinin | M pyd'gynyd] reveal, explain. paydagihistan, paydagih- [py kyh-stn'] appear, be revealed, payg [pdh! | (P рар), N ~] foot-soldier, courier. *paygal [pyg'l | N payyāla, piyála] cup, goblet. -- gar [-A/] cup-maker. payģām [pgt”m! | M pyg’m, N pay(y)ām] message. ~bar LA | N -bar] messenger, apostle. paygos [p?tktvs | M p’ygws] district, provi
```


## [2026-09-06T14:58:28.099Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/gargle",
 "prompt": "Give the full etymology of \"gargle\", and also of \"gargoyle\" and \"gorge\" if shown; note the Latin gurgulio/gurges connection and whether it is called imitative."
}
```


## [2026-09-06T14:58:28.589Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/bronchitis",
 "prompt": "Give the full etymology of bronchitis and bronchus/bronchial: who coined it, when, and from what Greek word."
}
```


### [2026-09-06T14:58:34.794Z] TOOL RESULT

```
# Etymology of Bronchitis and Bronchial Terms

**Bronchitis:**
Coined in 1808 by Charles Bedham, the term combines Modern Latin *bronchia* (bronchial tubes) with the suffix *-itis* (inflammation). As the source states: "coined in Modern Latin 1808 by Charles Bedham, from *bronchia* 'the bronchial tubes'...+ *-itis* 'inflammation.'"

**Bronchial/Bronchus:**
The root term *bronchia* originates from a Latinized form of Greek *bronkhia*, the plural of *bronkhos*, meaning "windpipe, throat." The document notes this Greek root "is of unknown etymology." The word entered English in the 1670s.

**Summary:**
The medical term was deliberately constructed during the early 19th century by combining an anatomical reference (from Greek via Latin) with a standard medical suffix denoting inflammatory conditions. The original Greek component's ultimate origin remains undetermined.
```


### [2026-09-06T14:58:34.846Z] TOOL RESULT

```
# Etymology of Gargle, Gargoyle, and Gorge

## Gargle (verb, 1520s)
From French *gargouiller* "to gurgle, bubble," derived from Old French *gargole* "throat, waterspout." The source likely combines imitative *garg-* (throat sounds) with *goule* (dialect for "mouth"), from Latin *gula* "throat." An earlier native form was Middle English *gargarize* from Latin and Greek roots.

## Gargoyle (noun, late 13c.)
From Old French *gargole*/*gargoule* meaning "throat" and "carved downspout." The term describes a "grotesque carved waterspout" connected to building gutters. The etymology shares the same imitative root as *gargle*, with the architectural feature named after its throat-like appearance and function.

## Gorge
**Not included in the provided content.** The page does not contain etymology for "gorge."

## Latin Connection
The document mentions Medieval Latin *gargola* and *gargulio* in connection with gargoyle, confirming shared roots between gargle and gargoyle. Both terms are explicitly described as deriving from "imitative" elements (*garg-*) representing throat sounds, rather than from classical Latin *gurges* or *gurgulio*.
```


## [2026-09-06T14:58:46.924Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN gargle\"; grep -oh \"gargle[^.]\\{0,300\\}\" KLN_1966.txt KLN_1971.txt | head -4; echo \"=== KLN bronchus\"; grep -oh \"bronchus[^.]\\{0,300\\}\" KLN_1966.txt KLN_1971.txt | head -3; echo \"=== SKT gargle\"; grep -oh \"Gargle[^.]\\{0,300\\}\\|gargle[^.]\\{0,250\\}\" SKT.txt | head -4",
 "description": "Klein and Skeat gargle/bronchus"
}
```


### [2026-09-06T14:58:48.661Z] TOOL RESULT

```
=== KLN gargle
gargle, gargoyle (q
gargle, intr
gargle, n
gargle’, 
=== KLN bronchus
bronchus and suff
bronchus, 
bronchus and suff
=== SKT gargle
Gargle
gargle  I '    Cot
```


## [2026-09-06T14:58:51.953Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nfor f in ['KLN_1966.txt','KLN_1971.txt']:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    for k in ['gargle, intr','bronchus, ','gurgle,','voracious,']:\n        i=t.find(k)\n        if i>0: print('##',f,k); print(t[i:i+500].replace('\\n',' ')); print()\n\"",
 "description": "Klein entries"
}
```


### [2026-09-06T14:58:53.774Z] TOOL RESULT

```
## KLN_1966.txt bronchus, 
bronchus, bronchiole,  n.,  a  minute  bronchial  tube  (anat.)  — Medical  L.  bronchiola,  a  diminutive  coined  by E.  Schultz  fr.  L.  bronchia  (pi.),  ‘the  bronchial tubes’;  see  bronchia.  Cp.  Joseph  Hyrtl,  Ono- matologia  anatomica,  p.  557- Derivative:  bronchiol-ar,  adj. bronchiolitis,  n.,  inflammation  of  the  bronchioles (med.)  —  Medical  L.  formed  fr.  bronchiola  with suff.  -itis.  See  prec.  word, bronchitis,  n. ,  inflammation  of  the  bronchial  tubes (med.) 

## KLN_1966.txt gurgle,
gurgle, dabble,  paddle’,  fr.  gargouille,  ‘throat’,  from  the imitative  base  *garg-.  See  prec.  word  and  cp. next  word  and  gurgle.  Cp.  also  jargon,  ‘confused speech’. Derivative :  gargle,  n.,  a  liquid  used  for  gargling, gargoyle,  n.,  a  grotesque  waterspout  representing a  human  or  animal  figure.  —  OF.  gargouille, ‘throat,  waterspout,  gargoyle’,  compounded  of the  imitative  base  *garg-  (see  garget)  and  goule, Western  dial,  form  of  gueule,  ‘mouth’,

## KLN_1966.txt voracious,
voracious, herbivore,  n.,  a  herbivorous  animal.  —  See  prec. word. herbivorous,  adj.,  feeding  on  grass.  —  See  Herbi¬ vora  and  -ous. herborist,  n.,  1)  a  collector  of  plants;  2)  a  her¬ balist.  —  F.  herboriste,  fr.  earlier  herboliste,  fr. herboliser.  See  herborize  and  -ist. herborization,  n.  —  F.  herborisation,  fr.  herboriser. See  next  word  and  -ation. herborize,  intr.  v.,  to  botanize  (archaic).  —  F. herboriser,  fr.  earlier  herboliser,  a  hybr

## KLN_1971.txt gargle, intr
gargle, intr. and tr. v. — F. gargouiller , ‘to gurgle,  dabble, paddle’, fr. gargouille, ‘throat’, from the  imitative base *garg-. See prec. word and cp.  next word and gurgle. Cp. also jargon, ‘confused  speech’.   Derivative: gargle, n., a liquid used for gargling,  gargoyle, n., a grotesque waterspout representing  a human or animal figure. — OF.   ‘throat, waterspout, gargoyle’, compou,  the imitative base *garg- (see garget) and g.  Western dial, form of gueule , ‘mouth*, fr.  gula. See g

## KLN_1971.txt bronchus, 
bronchus,  bronchiole, n., a minute bronchial tube (anat.) —  Medical L. bronchiola , a diminutive coined by  E. Schultz fr. L. bronchia (pi.), ‘the bronchial  tubes’; see bronchia. Cp. Joseph Hyrtl, Ono-  matologia anatomica, p. 557.   Derivative: bronchiol-ar, adj.  bronchiolitis, n,, inflammation of the bronchioles  (med.) — Medical L. formed fr. bronchiola with  suff. -itis. See prec. word,  bronchitis, n., inflammation of the bronchial tubes  (med.) — Medical L., coined by Charles Bed-  ham

## KLN_1971.txt gurgle,
gurgle,  dabble, paddle’, fr. gargouille, ‘throat’, from the  imitative base *garg-. See prec. word and cp.  next word and gurgle. Cp. also jargon, ‘confused  speech’.   Derivative: gargle, n., a liquid used for gargling,  gargoyle, n., a grotesque waterspout representing  a human or animal figure. — OF.   ‘throat, waterspout, gargoyle’, compou,  the imitative base *garg- (see garget) and g.  Western dial, form of gueule , ‘mouth*, fr.  gula. See gullet.   garibaldi,, n., a kind of blouse worn b

## KLN_1971.txt voracious,
voracious,  herbivore, n., a herbivorous animal. — See prec.  word.   herbivorous, adj., feeding on grass. — See Herbi-  vora and -ous.   herborist, n., 1) a collector of plants; 2) a her-  balist. — F. herboriste, fr. earlier herboliste, fr.  herboliser. See herborize and -ist.     herborization, n. — F. herborisation, fr. herboriser.  See next word and -ation.   herborize, intr. v., to botanize (archaic). — F.  herboriser, fr. earlier herboliser, a hybrid coined  fr. L. herbula, ‘a little herb
```


## [2026-09-06T14:59:02.302Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%BA%D8%B1%D8%BA%D8%B1",
 "prompt": "What does Wiktionary say about Arabic غرغر (ġarġara) 'to gargle' and its noun غَرْغَرَة — is it described as onomatopoeic/imitative? Also any Persian entry for غرغره."
}
```


## [2026-09-06T14:59:04.764Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFM/TAD غرغر\"; grep -oh \".\\{0,80\\}غرغر.\\{0,120\\}\" AFM.txt TAD.txt ARB_mo3rb.txt 2>/dev/null | head -5; echo \"=== ARY گلو\"; grep -n \"گلو\" incoming/ARY/ARY_pages.txt | head -5",
 "description": "Arabic sources for غرغر; Aryanpur گلو"
}
```


### [2026-09-06T14:59:08.279Z] TOOL RESULT

```
# غرغر Etymology and Definitions

**Onomatopoeia Status:**
Yes, Wiktionary explicitly describes the Arabic verb as onomatopoeic. The etymology section states it comes from a "reduplicated onomatopoeic root" with the pattern غ ر غ ر (ḡ r ḡ r).

**Arabic Noun:**
The noun غِرْغِر (ḡirḡir) refers to "guinea-fowl" (Numididae family), with a verbal noun form غَرْغَرَة (ḡarḡara).

**Persian Entry:**
The Wiktionary page includes a Persian section for غرغر (ġorġor), defined as:
- "murmur, muttering"
- "complaint, fuss"

The Persian entry shows different pronunciations across dialects (Classical Persian, Dari, Iranian, and Tajik variants) but no separate entry for غرغره with the additional ه suffix is documented on this page.
```


### [2026-09-06T14:59:12.762Z] TOOL RESULT

```
=== AFM/TAD غرغر
=== ARY گلو
799:وجود آمد. اطلاق واژه‌ی "انگلوسا کسون" به مردمان انگلیسی زبان بهمین دلیل است. بعدها انگلیسی
1101:و ایرلند و انگلوساً کسون و ایران باستان) به مردانی برمی‌خوریم که نه تنهاگنجینه‌ی دانسته‌ها و تاریخ
13049:: ۰ | گلو ۱
13103:اس چم اين واژه در زبان‌های ژرمنی: گلوله اگوی نخ
```


## [2026-09-06T14:59:15.652Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '13040,13075p' incoming/ARY/ARY_pages.txt; echo \"=== pdf page tag\"; awk 'NR<13060 && /\\[pdf page/' incoming/ARY/ARY_pages.txt | tail -2",
 "description": "Aryanpur گلو entry"
}
```


### [2026-09-06T14:59:17.406Z] TOOL RESULT

```
هار ا
پارسی باستان (4(۷اق8۴ظ 6۸08-۰۰:00 برنانی 078810): 10
پهلری (۲1اللم): انا لاه زان گرنبک (077//0): 0۸71 ,01178۸0
کردی (8015[7): 7 61710 ایسلندی کهن (۸2 57070۸ ضاه): ۱
سندی (/(ا600/2): 22۷۵1 بال2[۸ 3 ,ف۷821
سانسکریت (54/۶587): ۰ 6۸0 ,6۸0۸7 ساکسونی کهن ((843:0 0]0): :
آرمنی (47042/14): 101 17 ,015773۸
[pdf page 439]
۹ 95
: ۰ | گلو ۱
فریزی کهن (/(۲۸354 ام 01878۸ پسگشت‌ها خرس
آلماتی کهن ((08704۸ ۶0 صا): 0 ۶00120
۸1 ,010875۳3۸۵ 8 (000711) :۵ ی من
: انگلیسی کهن (54ا20/0 صا0): 9و ههام ی اما
7 بافشتا 0۴1 1 (8۸) :5 ۲02/2 ۳۰۱*۱۲۸
دانمارکی (0۸۸/574): امه 1257 اه
۱ سرئدی (5050157): 0۸ 4 (01071) ۰" 005
: نروژی (08014(7/): ۸08 4 (07ن0) 57
: 39 :7
, برهان قاطع + ۸۳۱
یادداشت,
۱ رابطه‌ی این واژه‌های ایرانی با دیگر واژه‌های این فهرست احتمالی است و پهمین غلت جلر واجریشه‌ی هند و
۱ اروپایی» (شاید) آمده است.
۱ اوستایی (۸3:87۸4۷): آلمانی کهن (0272/400 17/07 01.2): 51۸
۷ ,اتش6۸ بالذج. آلمانی (۸(7ل057): لداه|:د ۱۹
: پهلوی (1ماتله): 6۸06 بکانآه۸ج انگلیسی کهن (877ل20/01 00: ,۲8۵۲
کردی ((7015). هلندی (00767). 8 ار ننک
۱ 1 ,01۲818 ,هقی لهستانی (بللاه۳): ماهقی»
: افغانی (پشتو) (۸۳027): روسی ((175514): متام
6۸۸ بتفغالفتاه اسلواکی 51.0140): ۱۰۱۹۱۱۵
سانسکریت (54(/8877): آلشت۸ج بش۸5 لیتوانی (77711۸(۷۷ل): اد 1 نی
ارمنی (/4ل(۵/2:. باناگ ,000073
۱ لاتین (700مل): هلاه پسگشت‌ها 3/5
: فراته (0ل۳8(/0): هاتااناه 4 ۶0020
اسپانیایی (8۸۸154): ها00 و99 شا هد
ایتالیایی (/(0744): ها00 6 (31380۸5) :23/لعل مهر
=== pdf page tag
[pdf page 438]
[pdf page 439]
```


## [2026-09-06T14:59:26.135Z] TOOL CALL #53: Bash

```json
{
 "command": "ls site/pages/210.jpg 2>/dev/null || pdftoppm -f 210 -l 210 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg210 && echo done",
 "description": "Render page 210"
}
```


### [2026-09-06T14:59:27.626Z] TOOL RESULT

```
site/pages/210.jpg
done
```


## [2026-09-06T14:59:30.102Z] TOOL CALL #54: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/210.jpg"
}
```


### [2026-09-06T14:59:30.134Z] TOOL RESULT

```

```


## [2026-09-06T14:59:55.066Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('CHEUNG.txt',encoding='utf-8',errors='replace').read()\nimport re\nfor k in ['*gar','GAR','gar-']:\n    pass\ni=0\nfor m in re.finditer(r'\\*gar', t):\n    print(t[m.start()-200:m.start()+700].replace('\\n',' '))\n    print('---')\n    i+=1\n    if i>3: break\n\"",
 "description": "Cheung *gar"
}
```


### [2026-09-06T14:59:57.247Z] TOOL RESULT

```
nd E.M. Pescereva.   5 Not included are the most recent, mainly New Persian, borrowings in languages such as Turkish, Uzbek,  Urdu-Hindi, Indonesian, etc.   ° Т only recently discovered that the root *gar” ‘to be/make warm’ has been preserved as verb in Oss.  (engaryn) and several modern dialects spoken in Iran. Also the informal form NP sas ‘pee’ has a more  ancient pedigree than previously thought, once the connection with Av. Sa- ‘to defecate’ is recognised.    xli INTRODUCTION    It is for this reason that I have reconstructed Iranian roots that are sometimes based  on little data, as it cannot be excluded that in the future one would find more,  perhaps even more convincing, cognate forms.    1.3. Methodology   The roots have been reconstructed according to the principles of comparative  (Indo-)Iranian and Indo-European philology. It is inevitable that, as with many other  works, th
---
ash. caredol ‘to graze’. Ф These verbal  forms are unrelated to Oss. I. angaryn/enzerst, D. enzarun/enzarst (caus.) ‘to  kindle, light a fire’, cited by Abaev, Le: 158 f. They rather contain the root *gar’ ‘to  heat’.   *SANSKRIT: car ‘to move, walk, go, wander, travel’ (RV+), > Also in Wai. caräy ‘to  pasture’ = EWAia I: 534 f.   PIE *K"elH;- ‘to move, turn, wander; to pasture; to settle and cultivate’ 0 This verb  seems to describe several stages of the Indo-European way of living, viz. nomadism,  followed by pastoralism and (semi-)sedentary agriculturalism. = LIV: 386 ff. |  Pok.: 639    *Cas2 35    *IE COGNATES: Gr. méA0p01 ‘I move [intr.]’, Zero (aor.) ‘was, were, happened’,    Lat. colo (caus.) ‘I till, cultivate, inhabit’, Olrish bua-chail (m) ‘cowherd, bouvier  *REFERENCES: Horn 1893: 204; EVP: 17; Abrahamian 1936: 111; Abaev, Slovar’ I: 303, 291, 158 f.;  Werba 1997: 286 f.; Pau
---
l’, (Siwer.)  gn-/gun- ‘to fall, strike, draw to’, (Kor.) gin- ‘to strike, hit (the target)’, (pass.)  gin-/ginän- ‘to be struck’, Abyan. gennoyan ‘to become, arrive’ (from older *geln®,  *gern‘, see *gart), Khuns. gen-/gena, Semn. -gänä-, Sang. -goeneé ‘to become’, Mah.  gin-, Siv. gen-, gin-/genä, gina, gyänä, gyenä ‘to become, occur’, Qohr. gina/gin-,  Soi gin-ü ‘to become (into something)’, Delij. geni/gena ‘to become; to shake’,  (denomin.) ? Sorkh. gänd- *‘befalling, striking to ?’ (e.g. in gänd&j Боёо ‘one must  go’, gänn-, gänd- ‘to want’), Lasg. gände (in gändoe beso ‘one must go’, gänd- ‘to  want’)   *NEIR: Oss. I. qan, D. gana ‘wound, fracture; shortcoming; [also D.] guilt,  transgression’   *SANSKRIT: ghanä- (m.) ‘slaying’ (RV 6.26.8), han ‘to kill, slay? = EWAia II: 800   9 In several modern languages and dialects, a stem gen-, gin-, etc. is found. This  verbal stem has hith
---
 CSogd. ynt ‘stench’, SSogd. ynt'kw, BSogd. ynt’’k, ynt'k, CSogd. ynt'q  “bad, evil’ || (+ *a-) BSogd. ’’y’ynt- (caus.) ‘to defile’   (+ *à-) Pres.: IND. 3sg. ’’y’ynt (Dhu. 127(N), SCE 180(N))    104 *garl    *NWIR: Kurd. ganin/gan- ‘to rot’, NP gand ‘stench’, NP gandah ‘fetid, stinking,  rotten; filthy, dirty’, Bal. gandag ‘bad’, Kurd. gani ‘rotting; stinking’, (orig. ppp.)  Siv. gäs(s) ‘bad’   *NEIR: Pash. yandol ‘to dislike’ (+ *pari-) Oss. D. feelgandun/faelgzst ‘to smear;  paint’ (+ *ui-) Oss. D. igaendun/igest ‘to smell; defile, desacrate’, Oss. I. gast, D.  iğæstæ ‘desacration by something contagious or poisonous; desacrated’   *MISC: ? Par. ges ‘bad, sinful’, Orm. yanj ‘bad’ (< Pash. or other Ir. language ?)  *SANSKRIT: gandh ‘to smell’ (RV+) = EWAia I: 461   © The Ir. root *gant- (and Skt. gandh-) can hardly be of IE origin. The IE  correspondences, notably Gr. ö£vvog (m.) ‘blam
---
```


## [2026-09-06T15:00:01.346Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('CHEUNG.txt',encoding='utf-8',errors='replace').read()\nimport re\nfor m in re.finditer(r'to swallow', t):\n    s=t[m.start()-400:m.start()+400].replace('\\n',' ')\n    if 'gar' in s or 'Jar' in s or 'jar' in s:\n        print(s); print('===')\n\" | head -40",
 "description": "Cheung 'to swallow' root"
}
```


### [2026-09-06T15:00:03.109Z] TOOL RESULT

```
to the presence of a laryngeal, on which see Lühr 1976: 92. = LIV: 207 | Pok.: 471f.  *IE COGNATES: Hitt. /ku(ua)liya-/ ‘to flow; to run smoothly, be calmed’, OHG  quellan, Engl. to well    *REFERENCES: EVP: 51; IIFL II: 533a; Morgenstierne 1942: 266; Abaev, Slovar’ II: 268 f.; Abaev,  Slovar’ III: 205 f.; EVS: 17b, 52a; Werba 1997: 282; Puhvel IV: 303 ff.; Steblin-Kamenskij 1999: 251    * garH* *to swallow"   *AVESTAN: YAv. garð (f. pl.) ‘throats’ (Yt 17.56), YAv. aspo.garom noro.garom  ‘who swallows horses (and) who swallows men’ (Y 9.11).. 6 YAv. "jar- ‘to swallow’  (Y Av. "jarois P22), as cited by Bartholomae, AIW: 512, does not exist, on which see  Jamaspa — Humbach 1971: 45, fn. a.   *NWIR: Gz. Zara/Zar-, Tr. Zarta/Zar- ‘to chew’, NP Zard ‘gluttony’ (LW) || (+ *aua-) ?  Bal. ugarit/u
===
 quellan, Engl. to well    *REFERENCES: EVP: 51; IIFL II: 533a; Morgenstierne 1942: 266; Abaev, Slovar’ II: 268 f.; Abaev,  Slovar’ III: 205 f.; EVS: 17b, 52a; Werba 1997: 282; Puhvel IV: 303 ff.; Steblin-Kamenskij 1999: 251    * garH* *to swallow"   *AVESTAN: YAv. garð (f. pl.) ‘throats’ (Yt 17.56), YAv. aspo.garom noro.garom  ‘who swallows horses (and) who swallows men’ (Y 9.11).. 6 YAv. "jar- ‘to swallow’  (Y Av. "jarois P22), as cited by Bartholomae, AIW: 512, does not exist, on which see  Jamaspa — Humbach 1971: 45, fn. a.   *NWIR: Gz. Zara/Zar-, Tr. Zarta/Zar- ‘to chew’, NP Zard ‘gluttony’ (LW) || (+ *aua-) ?  Bal. ugarit/ugar- ‘to chew the cud, swallow, devour, devastate, misspend’. © The  etymology of Bal. ugarit/ugar- is unclear: Sims-Williams apud Shahbakhsh suggests  a connectio
===
. ugaranu ‘to chew the cud’ seems quite likely, as observed by Shah-  bakhsh. The older Bal. form might have been *ögär- ?   *NEIR: Pash. yaráy ‘greedy, gluttonous’, ? Pash. yur (m.) ‘goitre’ || (+ *a-) Pash. ayér  (m.) ‘indigestion’ || (+ *uz-) M. zoyóriy ‘thirsty’ || (+ *ni-) Pash. nyar(d)-/nyar- ‘to  swallow’ (with sec. -r-) || (+ *niZ-) Oss. I. nyqq.yryn/nyqqoyrd, D. niq(q)warun  /niq(q)ward ‘to swallow’ (contaminated with q.yr/qur throat), Wa. noZ(y)or-/  noZ(y)ord-, noZ(y)or-/noZ(y)ord ‘to swallow’   *SANSKRIT: gar’ ‘to devour, swallow’ (RV+)  EWAia I: 469   «PIE *g”erH;- ‘to devour, consume (wholly)? = LIV: 211 f. | Pok.: 474 ff.   *IE COGNATES: Gr. В.Вроско “I eat, digest’, Lat. voräre ‘to devour, to eat greedily’,  OCS po-Zréti ‘to eat (of animals), to devour’, Lith. gérti ‘to dri
===
might have been *ögär- ?   *NEIR: Pash. yaráy ‘greedy, gluttonous’, ? Pash. yur (m.) ‘goitre’ || (+ *a-) Pash. ayér  (m.) ‘indigestion’ || (+ *uz-) M. zoyóriy ‘thirsty’ || (+ *ni-) Pash. nyar(d)-/nyar- ‘to  swallow’ (with sec. -r-) || (+ *niZ-) Oss. I. nyqq.yryn/nyqqoyrd, D. niq(q)warun  /niq(q)ward ‘to swallow’ (contaminated with q.yr/qur throat), Wa. noZ(y)or-/  noZ(y)ord-, noZ(y)or-/noZ(y)ord ‘to swallow’   *SANSKRIT: gar’ ‘to devour, swallow’ (RV+)  EWAia I: 469   «PIE *g”erH;- ‘to devour, consume (wholly)? = LIV: 211 f. | Pok.: 474 ff.   *IE COGNATES: Gr. В.Вроско “I eat, digest’, Lat. voräre ‘to devour, to eat greedily’,  OCS po-Zréti ‘to eat (of animals), to devour’, Lith. gérti ‘to drink’, etc.   *REFERENCES: EVP: 26, 51; IIFL II: 533a, 275a; Morgenstierne 1942: 266; Abaev, Slovar’
===
   *hau'   *staij   *ua(n)c   *huar   *pad, *staH, *uindar  *gaHz   *maus(H), *tarp   *garH?   *Cap, *kard   *gar’, *starH’, *stamb(H),  *stranj   *gaz   *gant, *pauH   *eaiz, *man3H, *sar?   *taH   *har^, *iam, *tan    *pars, *Oras    to stride  to strike    to strike down  to strive  to struggle    to stumble  to submerge  to succeed  to suck   to suckle   to suffer    to supervise  to support  to swallow  to swear   to sweat   to sweep   to swell   to swim   to swing   to take    to take away   to take care   to take pleasure in  to take position   to take refuge    to take wing  to talk, chat  to tame  to teach    to tear    to tear out    to tend  to think    599    *xramH   *čak/g, *Cap, *daH’, *damb,  *daub, *gan, *huah, *jan,  *karc, *namH, *sna9H, *xad  *kap/f!   *Hiaud, *sparz   
===
```


## [2026-09-06T15:00:16.586Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/گلاویز/",
 "prompt": "Quote the فرهنگ معین and دهخدا entries for گلاویز verbatim, including any etymological analysis (is it گلو + آویز?)."
}
```


## [2026-09-06T15:00:17.904Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/گریوه/",
 "prompt": "Quote the فرهنگ معین and دهخدا entries for گریوه verbatim, including any bracketed origin tag (e.g. [پهـ.]) and meanings (mountain/hill/pass)."
}
```


### [2026-09-06T15:00:23.106Z] TOOL RESULT

```
# گلاویز - Dictionary Entries

**فرهنگ معین:**
"(گَ ) (ص فا. ) دست به گریبان ، دست به یقه ."

**لغت نامه دهخدا:**
"گل آویز. \[ گ َ \] ( نف مرکب ) دست به گریبان. دست به یقه. مرکب است از گلو و آویز. آویختن."

The Dehkhoda entry explicitly identifies the etymological composition as **گلو (throat) + آویز (hanging/suspended)**, literally meaning "throat-hanging" or "grappling by the collar." This compound structure reflects the word's primary sense of seizing someone by the neck during a fight or struggle.
```


### [2026-09-06T15:00:25.642Z] TOOL RESULT

```
# گریوه - Dictionary Entries

## Dehkhoda Dictionary (لغت نامه دهخدا)
"گریوه. [ گ َ/ گ ِ ری وَ / وِ ] ( اِ ) پهلوی ، گریو [ گردن ، پشت گردن ] اوستا، گریوا" - describing it as a small mountain, elevated ridge, or eroded highland terrain.

## Moein Dictionary (فرهنگ معین)
"(گَ وِ ) [ په . ] (اِ. ) ۱ - گردن ، پشت گردن . ۲ - کوه پست ، پشته ، تپه"

This entry identifies the word as coming from Pahlavi origins, with two primary definitions: the neck or back of the neck, and a low mountain or elevated ridge formation.

Both entries trace the term's ancestry to older Persian linguistic layers, with connections to expressions meaning "neck" or "nape," which metaphorically extend to geographical features resembling such topography.
```


## [2026-09-06T15:00:32.417Z] TOOL CALL #59: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-06T15:00:32.456Z] TOOL RESULT

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


## [2026-09-06T15:00:40.126Z] TOOL CALL #60: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/%D9%BE%DB%8C%D8%A7%D9%84%D9%87\" \"https://www.etymonline.com/word/gargle\" \"https://www.etymonline.com/word/bronchitis\" \"https://abadis.ir/fatofa/%DA%AF%D8%B1%DB%8C%D9%88%D9%87/\" \"https://abadis.ir/fatofa/%DA%AF%D9%84%D8%A7%D9%88%DB%8C%D8%B2/\" \"https://abadis.ir/fatofa/%D9%BE%DB%8C%D8%A7%D9%84%D9%87/\" \"https://en.wiktionary.org/wiki/%D8%BA%D8%B1%D8%BA%D8%B1\"; do python3 tools/fetch_source.py \"$u\" --note \"page 210, root Gwer 3 (to swallow): piyala/gargle/bronchitis/gariveh/gelaviz/gargara verification\" 2>&1 | tail -2; done",
 "description": "Archive web sources"
}
```


### [2026-09-06T15:00:48.062Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/396d9fd7f944b221.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6ea1490170dadbe6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3c56cb0db90d096d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d939665e373438f4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9c48c8f44f280c18.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ea20420770077800.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0346b620f2af5073.txt
```


## [2026-09-06T15:00:52.940Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/gʷerh₃-",
 "prompt": "Give the reconstruction, gloss, and the list of descendants (Indo-Iranian, Greek, Latin, Balto-Slavic) for PIE *gʷerh₃-."
}
```


## [2026-09-06T15:00:54.165Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%AF%D9%84%D9%88",
 "prompt": "Give the Persian etymology for گلو (gulū) 'throat' — Middle Persian form, Proto-Iranian, PIE root, and any cited sources (Hasandust, MacKenzie)."
}
```


### [2026-09-06T15:00:59.000Z] TOOL RESULT

```
# PIE *gʷerh₃-

**Reconstruction:** *gʷerh₃- (perfective)

**Gloss:** "to swallow, devour, eat"

**Descendants by language family:**

- **Indo-Iranian:** Sanskrit gṝ; various formations including jagā́ra (reduplicated stative) and gīrṇá (swallowed, devoured)

- **Greek:** Ancient Greek forms including borá (fodder), bibrṓskō (to eat, digest), and brōtós

- **Latin:** vorō "to swallow, devour"

- **Balto-Slavic:** Lithuanian girtas (drunk, intoxicated); Proto-Balto-Slavic descendants meaning "throat" (*gerˀtlán, *gúrˀtlan)

Additional descendants appear in Armenian (ker), Albanian (ngrënë, hangër), and Avestan (garō, aspōgarəm).
```


### [2026-09-06T15:01:00.379Z] TOOL RESULT

```
# Persian Etymology of گلو (gulū) 'throat'

Based on the Wiktionary entry provided:

**Middle Persian form:** [Book Pahlavi needed] (glwk' /⁠galōg⁠/)

**Proto-Indo-European root:** *gʷel- ("throat")

**Etymology chain:** The word is "inherited from Middle Persian," which derives from Proto-Indo-European, with cognates appearing in Latin *gula* ("throat") and Sanskrit *गल* (gala, "throat, neck").

**Note on sources:** The entry does not cite Hasandust or MacKenzie. The sole reference listed is Hayyim, Sulayman (1934), from the *New Persian–English dictionary*. The entry indicates a need for Book Pahlavi script documentation for the Middle Persian term, suggesting this etymological connection remains partially incomplete in the source material.
```


## [2026-09-06T15:02:05.087Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN piyala\"; grep -n \"pijäle\\|pijale\\|piyäla\\|piäle\\|pyäle\" HRN.txt | head -5; echo \"== HUB piyala\"; grep -n \"pijäle\\|pijale\\|piäle\" HUB.txt | head -5; echo \"== LEW voro\"; grep -n \"^voro\\|voro,\\|vorare\" LEW_1910.txt | head -5; echo \"== NYB galog\"; grep -n \"galōk\\|galok\\|glwk\" NYB_vol2_glossary.txt | head -5; echo \"== AFM/PLA piyala\"; grep -oh \".\\{0,60\\}پیاله.\\{0,100\\}\" AFM.txt TAD.txt 2>/dev/null | head -3",
 "description": "Extra consultations"
}
```


### [2026-09-06T15:02:09.023Z] TOOL RESULT

```
== HRN piyala
== HUB piyala
== LEW voro
== NYB galog
1974:hayyaréh help, aid, assistance: pat yaz- dàn ~ 314-15, 1214; pat ~ i yazdàn 505; pat nerök u ~ i Haftoiring 8774; nérók u ~ + zrat rād 8871; pat ~ <i> [better <u> or asyndeton] zor u z"arrah i .., spēnāk menoi 10628-24; pat name u nerök u ~ 1 dätär Ohurmazà 113?; 01? v. s. v. jāytšn; oigan ... kē-$ ~ hend those who are his (assistance =) assistants 100!!; ~ dātan 0 512; ~ dahišneh 11211; 6 ~ rasitan 61; Octo 3811 ; erat ~ 112-16 Ps, hdyb?-lyhy. hazangró-zim [hznglwkzym, -zm] a pe- riod of one thousand years, a millenium 3820.25, 391, 96% — Borrowed from Av. (1798) hazayro.zyam-.
== AFM/PLA piyala
```


## [2026-09-06T15:02:13.571Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN piyale variants\"; grep -niE \"piäla|piala|pijala|payäla|payyala|piyala\" HRN.txt HUB.txt | head -8; echo \"== LEW voro\"; grep -niE \"voro|vorāre|vorax\" LEW_1910.txt | head -5; echo \"== LAT voro\"; grep -niE \"^uoro|uorare|voro \" LAT.txt | head -5",
 "description": "Horn piyala, Latin voro"
}
```


### [2026-09-06T15:02:13.646Z] TOOL RESULT

```
== HRN piyale variants
HUB.txt:9474:piyala *Becher = gr. (pidXri; kiltd *Schlusser = gr. xXsTda
== LEW voro
10785:havoro I 134
== LAT voro
26508:cf., d'une nanifere generale, uorare.
26700:sur laquelle v. uorare.
70258:uoro, -as, -aul, -atum, -are: avaler, engloutir; cf.Cic.N.D.
70279:thematiques: skr.girami, v. sl.itrp. Le latin a le deriv 4 uorare.
```


## [2026-09-06T15:02:19.678Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '70255,70282p' LAT.txt; echo \"== HUB context\"; sed -n '9470,9478p' HUB.txt",
 "description": "Ernout-Meillet voro, Hübschmann piyala"
}
```


### [2026-09-06T15:02:19.744Z] TOOL RESULT

```
c f. HLin.7,49: uopiscos appellabant a geminis qui retenti utero nasce¬
rentur, altero interempto abortu. Conserve seulement comme cognomen.
L't est attestf? par des apex.
uoro, -as, -aul, -atum, -are: avaler, engloutir; cf.Cic.N.D.
8,47,122: animalium alia uorant, alia mandunt. Sens propre et figure.
Ancien (Pl.), classi que, usuel. Mais tend a etre remplac 4 par le
compos^ d 1 aspect d<£ termini deuoTO • Non roman* _ __
D 4 riv 4 s et compos 4 s: uordx (class. ), M.L.9454a, uoraciter, uoracitas
( 4poq. imp4r.) ; uorago : gouffre, abime (sens physique et moral,
e.g. Cic. Sest.53, m, gurges et uorago patrinonii\ M.L.9457, d' ou
uoraginosus-, uordtor, uordtus, -us m., uoratnna f.: "taverne, cabaret",
et "gouffre" (ces trois derniers tardifs); carni-uorus, Pline,
d'apros CTapxoqayos) ; omniuorus (id.) compos 4 s savants imites du
grecj cf. le type 8 T}|i,oj 3 opoS. Une forme simple de uorus avec geminee
expressive se trouve dans la glose uorri: edaces. ~ t
deuoro (class. et usuel), M.L.aOifij d 4 riv 4 s tardifs deuorator, ~trix,_
-fdrius; deuordtift-, deuorab ilis •, transuord (tardif), transuordtio
(Cael. Aur. ).
La racine dissyllabique *g w er 9 ~, *g*>re/o- "avaler" fournissait
un aoriste radical qu'a conserve gr. e( 3 pwv dans de rares formes de
la langue 4pique, et un parfait dont fSeppuKa, t 3eppwp.ai, sont les
repr4sentants; l'arm 4 nien a un aoriste keray "j'ai mange" en face
de uten "je mange». Pour le pr 4 sent, il a 4 t 4 recouru a des derivds
comme gr. | 3 1,; 3 pamw ou lit. geriii (inf .gerti) "j 'avale", ou a des formes
thematiques: skr.girami, v. sl.itrp. Le latin a le deriv 4 uorare.
Par suite de son sens, la racine admettait en indo-europeen beaucoup
de formes intensives et expressives entrainant des dissimilations
de r ou l; d'autre part, les formes a vocalisme zero admettaient
== HUB context
'Becken, Leuchter = gr. kt^dvrj; kalam = karanb, arm. kalamh
*Kohr = gr. x()diu(it] ; kdlbad, kalbud *Modeir, phi. kolput =
gr. aaXonddiov; ddl *Einier , nach Noldeke aus dem Semi-
tischen, syr, daula u. s. w. ; pilpil 'Pfeffer = skr. pippall;
piyala *Becher = gr. (pidXri; kiltd *Schlusser = gr. xXsTda
(ace.) u. s. w. (NSldeke, Pers. Stud. II, p. 38 fig.).
Kapitel 31: Konsonantenvorschlag.
Einigen vokalisch anlautenden WSrtern wird h oder
cr vorgeschlagen.
```


## [2026-09-06T15:02:38.350Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"\\[pdf page\" WLD_Bd1_pages.txt | sed -n '690,700p'; echo \"---search\"; grep -n \"gulü\\|gulu 'Kehle'\\|garəman\\|gar\\.man\\|npers. gulu\" WLD_Bd1_1930_dli_70244_djvu.txt | head -5",
 "description": "Walde-Pokorny Bd1 682"
}
```


### [2026-09-06T15:02:38.438Z] TOOL RESULT

```
---search
```


## [2026-09-06T15:02:41.491Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && ls -la; grep -c \"\" WLD_Bd1_1930_dli_70244_djvu.txt 2>/dev/null; grep -niE \"gulu|Kehle\" WLD_Bd1_1930_dli_70244_djvu.txt | head -5",
 "description": "Check WLD files"
}
```


### [2026-09-06T15:02:41.572Z] TOOL RESULT

```
total 146216
drwxrwxr-x  2 sfmqrb sfmqrb     4096 Sep  4 14:06 .
drwxrwxr-x 23 sfmqrb sfmqrb     4096 Sep  4 14:06 ..
-rw-rw-r--  1 sfmqrb sfmqrb  2993454 Sep  4 14:06 WLD_Bd1_1930_dli_70244_djvu.txt
-rw-rw-r--  1 sfmqrb sfmqrb 42256714 Sep  4 14:06 WLD_Bd1_1930_dli_70244_text.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  4327601 Sep  4 14:06 WLD_Bd1_pages.txt
-rw-rw-r--  1 sfmqrb sfmqrb  2417287 Sep  4 14:06 WLD_Bd2_1927_dli_106624_djvu.txt
-rw-rw-r--  1 sfmqrb sfmqrb 94865800 Sep  4 14:06 WLD_Bd2_1927_dli_106624_text.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  2833963 Sep  4 14:06 WLD_Bd2_pages.txt
55520
1790:avyjjv „Genick. Kehle“ zusammen. In itsuiha liegt das Deminutivsuffix 
2605:ang- (lat. angulus) bezogen werden, wie notwendig das von Schrader KZ. 
2664:agra- als *ngro- mit arm. ankiun, slav. qgh, lat. angulus „Winkel, Ecke“ 
4090:(oyxlvog = unclnus „Haken, Widerhaken“; ungulus ,,Fingerring“ Pacuvius, 
4146:Nicht recht Mar ist das g von lat. ungulus , ungustus s. o.).
```


## [2026-09-06T15:02:46.326Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -niE \"verschlingen\" WLD_Bd1_pages.txt | head -8; echo \"===\"; grep -niE \"^\\s*g\\^?uer|guer-|g\\\"er\" WLD_Bd1_pages.txt | head -5",
 "description": "WLD verschlingen"
}
```


### [2026-09-06T15:02:46.398Z] TOOL RESULT

```
28826:unter *uel- „drangen‘"), Haare verwirren, verschlingen“, raids „Garn, Fischer-
32438:auf p oder bh oder V) nhd. (eigentlich nd.) happen, liapstn „verschlingen'‘,
48568:nisi, hvima (aus *hvnma, idg. q't.cmu = ai. camati) „verschlucken, verschlingen
53788: nehmen, verschlingen" (verschieden ags. gUap .,krumm“,zu gheub[h}- „biegen“;
54502:einem Haufen, Wirrwarr“, gomotdti se „sich zu einem Kniiuel verschlingen“,
59082:2. gel-     und gUel- „verschlingen“; die Form mit   vermutlicb nach Osthoff
59599:ags. glindrian, fc/rglendrian „verschlingen“ von Falk-Torp bei Fick aaO.
59972:als       „Nagerin.     gefraBiges                  Tier",    Wz. *gel-         „verschlingen“,         ist       denkbar.
===
53458:aaO. zw., Uhlenbeck EWb. 104) mit ai. jvalati (s. unter guer-) und aksl.
60934:                                            guer,- guere                    ghuel-                                         643
60948:guer- und guere- „leuchten und heiG sein“. (Ygl. auch gher-).
64617:2.    g"er- ,,veischlingen, Schlund“.
64659:                                                     guer-                                                                        683
```


## [2026-09-06T15:02:48.901Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '64617,64700p' WLD_Bd1_pages.txt",
 "description": "WLD gʷer- verschlingen"
}
```


### [2026-09-06T15:02:48.951Z] TOOL RESULT

```
2.    g"er- ,,veischlingen, Schlund“.
     Ai. girdti ,
              gildti grnCiti ,,verschlingt“ (fut. gariiijati, ptc. gtrna- „ver-
                                             ,


schlungen“, gurtu- „gefressen"), intens. ni-gahiohli ni-jalgulUi ptc. jdrgu-                                ,                   ,


rdna-; - glr (in Zs.   „verschlingend‘, -yam- ds. (aja-gam- , Ziegen ver-
schlingend,                 Boa" = gr. dy/uo-flogog, lat. eami-corus gr. /logos ,,gefra6ig“,                    ,


tjard-h             ,,   Trank" (nicht wahrscheinlicher nach Johansson IF. 8, 176 zu *g\iel
                                                                            u
.Jierabtriiufeln"),                         gnla-Jt    ,,Kehle                    (vielleicht         zur   Parallelwz.         *gdi)el-     „ver-
schlingen"'),                 tuvi-jri-,            -yrn-           „viel verschlingend";                       av. Jaraiti          ..schluckt"',
-gar        :   in Zs.l          „verschlingend“                            (aspo-yar-             ..Pferd v.“),    f.   pi.   (Keltic, Hals"',
                                            av. yardman- „Ivehle, Hals“;
                                    -
np. gitlu ,,Kehle‘                      .



  arm. her ,,Speise, FraS“, kur ds. (*</“„»•-, oder nach Bartholomae IF. 2,
268 g       keri „ich a6", kokord ,,Kehle“ (Hiibschmann Arm. Gr. I, 459;
auch kreum „nage“?? Pedersen KZ. 39, 427); alb. nqrane ..gegessen'                                                                                  -




(G. Meyer Alb. Wb. 306);
     gr. flood              „Fra6,               Speise-‘       !=              lat.    *vorcb,      wo von cordre ),          [logos      (s.   o.J,

fjtf)Q(boy.(o              „verzehre“,                hom.          opt.          pf.    jleflotb/lois,      fSgo'jiia,    jlgtojug,     flgatoig
„Speise‘'. flganyg „Esser";
     gr. fldga&gov,                     hom. /jegt&gov, ark. £ege&gov, dege&gov „Schlund“;
     lat.        (s. o.) ,,verschlingen“, vordgo „Schlund“, carni- corns; air.
                vo ro,       -die
tuarae „Speise“ (*lo-(f,ir-iia‘! Pokorny KZ. 45, 76; anders K. Meyer Sitz.-
Ber. Akad. Berlin 1918, S. 628), acymr. breuad „Totenwurm", breuan ,, Aas-
krahe“ (urkelt. *bravato-, *bruvand nach Fick II 4 181; *brd = gr. (Igco-l s. u.);
                                                     guer-                                                                        683

   ahd. (jiterdctr „Lockspeise, Koder", nhd. Koder" (s. auch Falk-Torp 565.
                                                                        .,


1500 unter kore);
   lit. gent), gerti „trinken", gird ,, Trank", lett. dzeris „betrunken“, dzeri
,,trinken", aksl. Iwq, zreti ,,verschlingen" ; serb. grbtlo (*g1r3ibldinl) Schlund":                         ,,


mit gib - als voreinzelsprachlicber Entwicklung aus               (*g e rj) aksl. ynlo.            l‘




                                   „Kehle“ (ursl. *girdlo), lit. gurklf/s, ace.
russ. gorlo , serb. grlo, poln. gardto
gurkl[        „Kropf    £
                                    apr. garde „Gurgel“ ( *gur-tl{i)o -), vgl.
                            (hochstufig gerkle),
aksl. gntanb, russ. yortchib (usw., s. Berneker 372) ,,Luftrohre, Rachen".
Ygl. Trautmann Bsl. Wb. 89 f., Miihlenbach-Endzelin I 546 f., 643.
   Mit voller oder gebrocbener Reduplikation:
    ai   .
             gargara-h      ..Schlund,      Strudel";         lit .   gargaliuojit     „rochle,         glucke            -

                                                                                                                              ;
                                                                                                                                  lat.

gurgulio {-ur- wie im             „Gurgel, Luftrohre", yuryes ..(Schlund =)
                                       Balt. -SI.)
Strudel, Wirbel, tiefes Gewasser", guryustium (Suffix nach unyustiac )
„armliches Loch als Hiitte oder Kneipe"; ahd. queried; da, querka ..Gurgel".
anord. letter  „Kropf", wovon afries. querka, anord. kyrkia ..erwtirgen"
(Noreen Ltl. 226; alb. (d)zverk „Hals“ bleibt fern, s. Pedersen KZ. 36, 325                                                             .




   Sehr unsicher ist die Auffassung von eflov^e (efigvie'!) ..schlang hinunter‘
als *g^r u -g{ u )- (Schrader KZ. 30, 470; Prellwitz 2 86 denkt alternativ an
```


## [2026-09-06T15:02:55.258Z] AGENT

Now I have everything I need. Writing the verification file.


## [2026-09-06T15:11:10.234Z] TOOL CALL #70: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /home/sfmqrb/git/rishe/data/verification/page-210.json << 'JSONEOF'\n{\n  \"pdf_page\": 210,\n  \"book_page\": 180,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Gwer 3, Gwere 2\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *gʷerh₃- (older notation *gʷer-1, *gʷerə-) 'to devour, swallow', with derivatives meaning 'throat, gullet'\",\n      \"note\": \"Pokorny I 474-476 heads the entry 'Root/lemma: gʷer-1, gʷerə-. Meaning: to devour; throat', which is exactly Nourai's root box (his numbering 'Gwer 3 / Gwere 2' is his own serial numbering of homophonous roots, not Pokorny's). Walde-Pokorny I 682-683 = '2. gʷer- „verschlingen, Schlund“'; Watkins/AHD 'gʷerə-4. To swallow. [Pok. 1. gʷer- 474]'; LIV 211f. and Cheung 2007: 104 reconstruct *gʷerH₃-/Iranian *garH³ 'to swallow'. Language label (Indo-European) and gloss ('to swallow') are both correct. One cross-cutting caveat governs several nodes below: beside *gʷer- there is a parallel root *gʷel-/gel- 'swallow' (Lat. gula, Skt. gala-, Pok. 365), and Walde-Pokorny itself notes of Skt. gala-ḥ 'Kehle' that it belongs 'vielleicht zur Parallelwz. *gʷel- „verschlingen“'. Ernout-Meillet s.v. uoro explain why the two are hard to separate: 'Par suite de son sens, la racine admettait en indo-européen beaucoup de formes intensives et expressives entraînant des dissimilations de r ou l.' Persian galū/gulū (node 3) sits precisely on that fault line. A second caveat: the 'Gargelos/Gulgul' sub-root (node 16) is expressly onomatopoeic in Mann and in Pokorny's §5, and only loosely attached to *gʷer-.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *gʷerh₃- «بلعیدن، فروبردن؛ گلو» است. پوکورنی (ص ۴۷۴–۴۷۶) همین ریشه را با معنای «to devour; throat» آورده و والده-پوکورنی (ج ۱، ص ۶۸۲–۶۸۳) آن را «gʷer- verschlingen, Schlund» نامیده است؛ واتکینز در پیوست AHD نیز gʷerə-4 «to swallow» را با ارجاع به پوکورنی ۴۷۴ ثبت کرده و چونگ (۲۰۰۷، ص ۱۰۴) ریشهٔ ایرانی *garH³ «بلعیدن» را از همین ریشه می‌گیرد. پس نام ریشه، برچسب زبانی و معنای آن در نمودار نورایی درست است (شمارهٔ «۳» از آنِ خودِ نورایی است، نه پوکورنی). دو نکتهٔ کلی: نخست آنکه در کنار این ریشه، ریشهٔ همسانِ *gʷel-/gel- «بلعیدن» (لاتینی gula، سنسکریت gala-) نیز هست و والده-پوکورنی خود می‌گوید gala- «شاید» به آن ریشهٔ موازی تعلق دارد؛ سرنوشت «گلو» در همین‌جا تعیین می‌شود. دوم آنکه شاخهٔ «Gargelos/Gulgul» در فرهنگ مان صریحاً «Onomat.» (آواواژه) خوانده شده و پیوندش با ریشهٔ اصلی سست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/gʷerh₃-\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:474\", \"status\": \"supports\", \"note\": \"POK_full.txt block ending 'Page(s): 474-476': 'Root / lemma: gʷer-1, gʷerə- / Meaning: to devour; throat'. Nourai's root box reproduces the gloss word for word.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"IEW I 474-476, s.v. gʷer-1, gʷerə-\", \"stance\": \"supports\", \"note\": \"'Meaning: to devour; throat … References: WP. I 682 ff., WH. I 627 f., Trautmann 89 f.' (grep -n 'Page(s): 474-476' POK_full.txt)\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. I 682-683, '2. gʷer- „verschlingen, Schlund“'\", \"stance\": \"supports\", \"note\": \"WLD_Bd1_pages.txt line 64617: '2. gʷer- „verschlingen, Schlund“ … av. jaraiti „schluckt“, -gar- in Zs. „verschlingend“ … np. gulū „Kehle“'; note also the caveat 'gala-ḥ „Kehle“ (vielleicht zur Parallelwz. *gʷel- „verschlingen“)'\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. gʷerə-4\", \"stance\": \"supports\", \"note\": \"'gʷerə-4. To swallow. … 2. Suffixed o-grade form *gʷor-ə- in Latin vorāre … [Pok. 1. gʷer- 474.]'\"},\n        {\"src\": \"CHEUNG\", \"where\": \"EDIV p. 104, s.v. *garH³\", \"stance\": \"supports\", \"note\": \"'*garH³ „to swallow“ … PIE *gʷerH₃- „to devour, consume (wholly)“ = LIV: 211 f. | Pok.: 474 ff.'\"},\n        {\"src\": \"SYN\", \"where\": \"Buck 4.29 THROAT, p. 233\", \"stance\": \"supports\", \"note\": \"'1. Derivs. of vbs. for „swallow, devour“ either 1) IE *gel- in Ir. gelim, etc.; or 2) IE *gʷer- in Skt. gṛ-, Grk. βιβρώσκω, Lat. vorare, etc.' — Buck keeps the two roots side by side, as here.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"gar 3; jaraiti; garah\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Nourai's 'gar 3' is Bartholomae's numbering: AiW s.v. '³gar- V. „schlucken“. Praes. jara-' — so the label 'gar 3 : to swallow, devour' is copied correctly from the standard Avestan dictionary, and Bartholomae's ⁴gar- '1) Adj. „schluckend, verschlingend“ (nur Komp.). 2) f., Plur. „Kehle, Hals“' gives the noun. 'garah' is not Bartholomae's citation form but Horn's: Grundriss no. 928 (p. 207) writes 'aw. garah- „Kehle“', and Buck 4.29 likewise tabulates 'Av. garəman- (in pl.), garō (pl.)'; the attested Young Avestan form is the f. pl. garō (Yt 17.56), beside the stem garəman- 'throat, neck'. The weak point is 'jaraiti'. Bartholomae AiW 512 posited YAv. jaraiti 'swallows' in Pursišnīhā 22, and Pokorny and Walde-Pokorny copied it ('av. jaraiti „schluckt“'); Cheung, EDIV 104, s.v. *garH³, states flatly: 'YAv. *jar- „to swallow“ (YAv. *jarōiš P22), as cited by Bartholomae, AIW: 512, does not exist, on which see Jamaspa — Humbach 1971: 45, fn. a.' So jaraiti is a ghost form corrected out of the text in 1971; Nourai (following Pokorny) still prints it. The zero-grade adjectival -gar- is genuinely attested in compounds: aspō.gar- 'horse-devouring', nərə.gar- 'man-devouring' (Y 9.11).\",\n          \"derivation_fa\": \"«gar 3» همان شمارهٔ بارتولمه است: در فرهنگ ایرانی باستان ذیل «³gar-» آمده «V. schlucken، ستاک حال jara-»، و «⁴gar-» هم صفت «بلعنده» (تنها در ترکیب) و هم اسم مؤنث جمع «گلو، گردن» است؛ پس برچسب نورایی از منبع معتبر گرفته شده. صورت «garah» از بارتولمه نیست بلکه از هرن است: هرن در بند ۹۲۸ (ص ۲۰۷) می‌نویسد «اوستایی garah- گلو»، و باک نیز در جدول ۴٫۲۹ صورت‌های garəman- و garō (جمع) را می‌آورد. اما «jaraiti» جای چون‌وچرا دارد: بارتولمه (ستون ۵۱۲) آن را از متن پرسشنیها برساخته بود و پوکورنی از او گرفت، ولی چونگ در فرهنگ ریشه‌شناختی فعل ایرانی (ص ۱۰۴) صریحاً می‌گوید این فعل «وجود ندارد» و خوانش درست متن را جاماسپ‌آسا و هومباخ (۱۹۷۱) نشان داده‌اند. بنابراین ادعای نورایی دربارهٔ خودِ ریشه و «گلو» درست است، ولی صورت jaraiti واژه‌ای موهوم است که از پوکورنی به کتاب راه یافته.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/gʷerh₃-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:474\", \"status\": \"supports\", \"note\": \"POK p.474: 'Avestan jaraiti „gulp, sip, swallow, send down the throat“, -gar- (in compounds) „devouring“ (aspō-gar- „horse v.“), f. Pl. „throat, neck“, npers. gulu „throat“, Avestan garəman- „throat, neck“.' Every word of Nourai's node is on that page — including the now-rejected jaraiti.\"},\n            {\"ref\": \"KNT:199\", \"status\": \"partial\", \"note\": \"Kent p.199 (KNT.txt line 5723, between the running heads for pp.198 and 200) s.v. batugara- refers to 'root in Av. gar- „devour“, Skt. girati, Lt. vorat, pIE *gʷer-' — it corroborates the Avestan verb gar-, but Kent gives no form garah and no jaraiti.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"AiW, s.v. ³gar-, ⁴gar-, garəman- (cols. ~512, 514)\", \"stance\": \"supports\", \"note\": \"BRT.txt line 10209 '• j. ³gar- V. „schlucken“. Praes. jara-'; line 10222 '• j. ⁴gar- 1) Adj. „schluckend, verschlingend“ (nur Komp.). 2) f., Plur. „Kehle, Hals“ … Yt. 17.56'; line 10223 'Zum V. ³gar-. — ai. ¹gir- Adj.; vgl. ai. gala- m., np. gulū „Kehle“'; line 10276 '• j. garəman- m., Plur. „Kehle, Hals“'; line 5878 'aspō.gar- Adj. „Rosse verschlingend“'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"EDIV p. 104, s.v. *garH³ 'to swallow'\", \"stance\": \"partial\", \"note\": \"'*AVESTAN: YAv. garō (f. pl.) „throats“ (Yt 17.56), YAv. aspō.garəm nərō.garəm … ◊ YAv. *jar- „to swallow“ (YAv. *jarōiš P22), as cited by Bartholomae, AIW: 512, does not exist, on which see Jamaspa — Humbach 1971: 45, fn. a.' — supports gar-/garō, deletes jaraiti.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 683\", \"stance\": \"supports\", \"note\": \"'av. jaraiti „schluckt“, -gar- in Zs. „verschlingend“ (aspō-gar- „Pferd v.“), f. pl. „Kehle, Hals“, av. garəman- „Kehle, Hals“; np. gulū „Kehle“' — the pre-1971 consensus Nourai reproduces.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 4.29 THROAT, table on p. 233\", \"stance\": \"supports\", \"note\": \"the Avestan row of the THROAT table reads 'Av. garəman- (in pl.), garō (pl.)'.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"garŭk\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The Book Pahlavi spelling is ⟨glwk'⟩, a -k/-g diminutive-ish noun suffix on the 'throat' stem. Horn, Grundriss no. 928, p. 207 — the very page Nourai cites — reads it 'phlv. garūk Vd. 15 (11)', i.e. from the Pahlavi Vidēvdād gloss on Vd. 15.11, and that 1893 reading is what Nourai copies letter for letter. MacKenzie's Concise Pahlavi Dictionary now reads the same ⟨glwk'⟩ as galōg (some read gulōg): 'galōg [glwk' | N gulū] throat'. Since Book Pahlavi ⟨l⟩ and ⟨r⟩ are the same letter and ⟨w⟩ can be read u/ō, garūk and galōg are two readings of one written word — Nourai is faithful to Horn but a century behind MacKenzie. The step Avestan gar-/garō → MP ⟨glwk'⟩ is the traditional derivation (Horn, Hübschmann, Pokorny), but see node 3 for the l/r problem it raises.\",\n          \"derivation_fa\": \"املای پهلوی این واژه ⟨glwk'⟩ است و در ترجمهٔ پهلوی وندیداد (۱۵٫۱۱) به کار رفته. هرن در بند ۹۲۸ (ص ۲۰۷) — همان صفحه‌ای که نورایی ارجاع داده — آن را «garūk» خوانده است و نورایی همان خوانش ۱۸۹۳ را نقل کرده. مکنزی در فرهنگ کوتاه پهلوی همین ⟨glwk'⟩ را «galōg» می‌خواند: «galōg [glwk' | فارسی نو gulū] گلو». چون در خط پهلوی «ل» و «ر» یک حرف‌اند و ⟨w⟩ را هم می‌توان u یا ō خواند، garūk و galōg دو خوانش از یک نوشتهٔ واحدند؛ پس خطای کتاب نیست، بلکه پیروی از خوانش کهنهٔ هرن است. گذر از اوستایی gar-/garō به این صورتِ پهلوی همان راهی است که هرن و هوبشمان و پوکورنی می‌پیمایند (برای اشکال «ل/ر» نک. گرهٔ بعد).\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"HRN:207\", \"status\": \"supports\", \"note\": \"Horn, Grundriss der neupersischen Etymologie, no. 928, p. 207 (leaf 228 of HRN.txt): 'gulū, gelū (AM. 109 Zeile 1 v. u.) „Kehle“. aw. garah- „Kehle“; phlv. garūk Vd. 15 (11); skr. gala-; lat. gula …'. Nourai's Pahlavi form and its parent are Horn's, verbatim.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie 1971, p. 35 s.v. galōg\", \"stance\": \"partial\", \"note\": \"PHD.txt line 378: 'galōg [glwk' | N gulū] throat' — same written word, modern reading galōg rather than Horn's garūk; PHD.txt line 4001 'throat galōg, grīw'.\"},\n            {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II (Glossary)\", \"stance\": \"silent\", \"note\": \"grep -n 'galōk|galok|glwk' NYB_vol2_glossary.txt returns no entry for the word; Nyberg's glossary is limited to the texts he edits.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien (HUB.txt line 8810, 9456)\", \"stance\": \"supports\", \"note\": \"'gulū „Kehle“, zd. garah-'; and 'gulū „Kehle“, skr. gala-, lat. gula, d. Kehle, aber zd. garah-, kurd. gerū, afgh. γāra' — Hübschmann accepts Horn's chain (note his 'aber' before zd. garah-, flagging the l/r mismatch).\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"galŭ «گلو»; gal «گل»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"NP گلو galū/gulū 'throat' continues MP ⟨glwk'⟩ (galōg/garūk) with the regular loss of final -g/-k after ō in New Persian (MP galōg > NP gulū, exactly as MP gōnag > NP gūna). Pokorny p. 474 lists 'npers. gulu „throat“' directly under gʷer-1, Horn no. 928 and Hübschmann make it the reflex of Av. garah-, and Mo'in's footnote to Borhān-e Qāṭeʿ p. 1832 gives the same family: 'در اوستا GARA- (گلو)، پهلوی GALUK، سانسکریت GALA-، لاتینی GULA … کردی GERU … گیلکی GALI، کردی GELUGA/GELUGI (گلو، معبر تنگه)'. The reservation is the lateral: an Old Iranian *gar- should give NP *gar-, and both the MP ⟨l⟩ and the Skt./Lat. cognates gala-/gula point rather to the parallel root *gʷel-/gel- 'swallow' (Pok. 365; AHD gʷel-3 'To swallow. Dissimilated to *gel-. … Latin gula, gullet, throat'), which is where English Wiktionary now files گلو. Walde-Pokorny I 683 hedges the same way about Skt. gala-ḥ, and Ernout-Meillet explain the whole r/l muddle as expressive dissimilation inside one root. So Nourai's arrow is the traditional Horn/Pokorny one and defensible, but not the only modern option. The second word, gal «گل» 'throat, neck, a narrow pass', is the same stem without the -ū; the 'narrow pass' sense is confirmed for the cognate Kurdish gelūga/gelūgi 'گلو، معبر تنگه' in Mo'in's note, and the chart's extra گلاویز galāvīz is transparently گلو + آویز, as Dehkhoda states ('مرکب است از گلو و آویز').\",\n          \"derivation_fa\": \"«گلو» در فارسی نو دنبالهٔ ⟨glwk'⟩ فارسی میانه (galōg / خوانش هرن: garūk) است؛ افتادن ‑گ پایانی پس از ō در گذر از فارسی میانه به فارسی نو قاعده‌مند است (مانند gōnag > گونه). پوکورنی (ص ۴۷۴) خودِ «npers. gulu» را زیر همین ریشه آورده، هرن (بند ۹۲۸) و هوبشمان آن را بازماندهٔ اوستایی garah- می‌دانند، و حاشیهٔ معین بر برهان قاطع (ص ۱۸۳۲) همین خانواده را می‌شمارد: «در اوستا GARA (گلو)، پهلوی GALUK، سانسکریت GALA، لاتینی GULA، کردی GERU … کردی GELUGA (گلو، معبر تنگه)». اشکال کار «ل» است: ایرانی باستان *gar- در فارسی باید *gar بدهد، و «ل»ِ فارسی میانه و نیز gala- سنسکریت و gula لاتینی بیشتر به ریشهٔ موازی *gʷel- «بلعیدن» می‌خورند (پوکورنی ۳۶۵؛ واتکینز gʷel-3). ویکی‌واژه امروز «گلو» را زیر همان ریشهٔ موازی می‌گذارد. پس ادعای نورایی همان دیدگاه سنّتی هرن و پوکورنی است و با احتیاط پذیرفتنی است، نه قطعی. «گل» صورت کوتاه همان ستاک است و «گلاویز» چنان‌که دهخدا می‌گوید «مرکب است از گلو و آویز».\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/گلو\",\n            \"https://abadis.ir/fatofa/گلاویز/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:474\", \"status\": \"supports\", \"note\": \"POK p.474, within the Avestan paragraph: '… f. Pl. „throat, neck“, npers. gulu „throat“, Avestan garəman- „throat, neck“.'\"},\n            {\"ref\": \"BQT:1832\", \"status\": \"supports\", \"note\": \"Borhān-e Qāṭeʿ ed. Moʿin p. 1832 (BQT_v3_picofile.pdf pdf-page 629; headword «گلو - بضم اول و ثانی بواو کشیده، معروف است که حلق و حلقوم باشد»), footnote 3: 'در اوستا GARA- (گلو)، پهلوی GALUK، سانسکریت GALA-، لاتینی GULA … اشتقاق - هوبشمان ۹۲۸ … کردی GELUGA، GELUGI (گلو، معبر تنگه)'.\"},\n            {\"ref\": \"MON:3334\", \"status\": \"not_checked\", \"note\": \"Moʿin's 6-vol Farhang-e Fārsi is not page-mapped online (vajehyab/abadis give entry text without pagination) and the archive.org copy is a differently paginated 2-vol abridgement whose OCR (MON_part1/2.txt) is unusable. p. 3334 is consistent with the گ range of the continuous lexicon pagination (cf. MON:514 for ب, 862 for پ, 1408 for خ elsewhere on this page).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"no. 928, p. 207\", \"stance\": \"supports\", \"note\": \"'gulū, gelū „Kehle“. aw. garah- „Kehle“; phlv. garūk … skr. gala-; lat. gula … kurd. gerū „Kehle“'.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien, HUB.txt line 9456\", \"stance\": \"partial\", \"note\": \"'gulū „Kehle“, skr. gala-, lat. gula, d. Kehle, aber zd. garah-, kurd. gerū, afgh. γāra und γarai' — Hübschmann's 'aber' marks the very r/l discrepancy discussed above.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, ARY_pages.txt [pdf page 439] = printed p. 440, headword گلو\", \"stance\": \"supports\", \"note\": \"the entry lists Avestan, پهلوی GALŪK, سانسکریت GALA, لاتینی GULA, کردی, ایسلندی کهن etc. and cites «برهان قاطع» as its source — the same family tree as Nourai's.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. gʷel-3\", \"stance\": \"contradicts\", \"note\": \"'gʷel-3. To swallow. Dissimilated to *gel-. … 3. Suffixed zero-grade form *gul-ā in Latin gula, gullet, throat, palate … [In Pok. 2. gel- 365.]' — Watkins puts gula (and by implication gala-/galōg) under the parallel root, not under gʷerə-4.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 683\", \"stance\": \"partial\", \"note\": \"'gala-ḥ „Kehle“ (vielleicht zur Parallelwz. *gʷel- „verschlingen“)' — Walde-Pokorny lists np. gulū here but explicitly flags the alternative.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Avestan\",\n          \"words\": \"pati-gâra\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"No such Avestan word is attested: Bartholomae's AiW has no paiti.gāra- (grep of BRT.txt for paiti.gar-/paiti-gāra- returns nothing), and Kent, the reference Nourai cites, writes the form with an asterisk, '*pati-gāra-', i.e. as a reconstructed Old Iranian compound, not an Avestan citation. Morphologically it is impeccable — *pati- 'at, to' (Av. paiti, OP patiy) + a -gāra- action/agent noun, exactly parallel to attested *pati-gāma- 'message' > MP paygām — and Kent explicitly attaches an element -gara- 'devouring, drinking' to 'root in Av. gar- „devour“' when he analyses batugara- 'drinking cup' on that very page. But Kent then reports that Benveniste (J.As. 228.233-4) and Herzfeld (AMI 8.9-17) prefer to link this second element 'rather with Skt. galati „drips“, gālayati „pours“, as „wine-pourer“, cf. Lt. libare' — i.e. to the *gel-/*gal- 'pour' family, not to 'swallow'. Since it is precisely from that alternative sense that Kent then derives piyāla (node 5), Nourai's placing of *pati-gāra- under the 'swallow' root reproduces only one half of his own source. Verdict: a real reconstruction, wrongly labelled 'Avestan' and hung on the arguably wrong root.\",\n          \"derivation_fa\": \"چنین واژه‌ای در اوستا گواهی نشده است: در فرهنگ بارتولمه صورت paiti.gāra- نیامده، و کنت — همان مرجعی که نورایی به آن ارجاع می‌دهد — این صورت را با ستاره یعنی «*pati-gāra-» می‌نویسد، پس بازسازی است نه واژهٔ اوستایی. ساخت واژه بی‌ایراد است: پیشوند *pati- (اوستایی paiti، پارسی باستان patiy) به‌علاوهٔ اسمِ ‑gāra-، درست مانند *pati-gāma- > پهلوی paygām «پیغام». کنت نیز هنگام تحلیل batugara- «جام شراب» جزء ‑gara- را «بلعنده، نوشنده» و از «ریشهٔ اوستایی gar- devour» می‌گیرد. اما بلافاصله می‌افزاید که بنونیست و هرتسفلد این جزء را به جای آن با galati سنسکریت «چکیدن» و gālayati «ریختن» می‌سنجند، یعنی «شراب‌ریز»، و پیاله را از همان می‌گیرند. بنابراین برچسب «اوستایی» نادرست است و انتساب به ریشهٔ «بلعیدن» تنها یکی از دو رأیِ منبعِ خودِ نورایی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/پیاله\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KNT:199\", \"status\": \"partial\", \"note\": \"Kent, Old Persian, p. 199 s.v. batugara-: '… + -gara- (§143.I) „devouring, drinking“ (§160.Ia), cf. Av. aspō.garō „horse-devouring“ … from root in Av. gar- „devour“ … pIE *gʷer-. Bv. J As. 228.233-4 suggests, and Hz. AMI 8.9-17, ApI 113-5, accepts cognation rather with Skt. galati „drips“, gālayati „pours“, as „wine-pourer“ … and NPers. piyāla „drinking cup“, from *pati-gāra-.' The form is there but starred and Old Iranian, not Avestan, and Kent's preferred root for it is not 'swallow'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"AiW, paiti- compounds\", \"stance\": \"silent\", \"note\": \"grep -n 'paiti.gar|paiti-gar|patigār' BRT.txt returns nothing: no Avestan paiti.gāra- exists in Bartholomae's dictionary.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie 1971, p. 67 s.v. *paygāl\", \"stance\": \"partial\", \"note\": \"'*paygāl [pyg'l | N payyāla, piyāla] cup, goblet. ~gar [-kl] cup-maker' — MacKenzie records the Middle Persian etymon but offers no Old Iranian derivation; the MP -l is the obstacle for *pati-gāra-.\"},\n            {\"src\": \"KNT\", \"where\": \"p. 199\", \"stance\": \"partial\", \"note\": \"see ref_check; Kent's own preference on that page is Benveniste/Herzfeld's 'wine-pourer' etymology.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"pîyâleh «پیاله»\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"NP پیاله piyāla 'drinking cup' certainly continues MP ⟨pyg'l⟩ *paygāl 'cup, goblet' (MacKenzie 1971: 67; the chart's variant spelling پیغاله preserves the older -γ-). Beyond that the field splits. (a) Kent p. 199 — the page Nourai cites — reports Herzfeld's derivation 'NPers. piyāla „drinking cup“, from *pati-gāra-', which is Nourai's arrow. (b) Against it, Hübschmann's Persische Studien lists 'piyāla „Becher“ = gr. φιάλη' in his chapter of Greek loanwords in Persian, i.e. a borrowing of Gk. phiálē 'shallow bowl' (whence also Arabic فيالجة, as Dehkhoda notes: 'گویا اصل کلمه یونانی است و عرب از آن فیالجه ساخته است، یا اینکه کلمه را یونانی‌ها از ایرانیان گرفته'). Encyclopaedia Iranica (Greece xiii) is cited on Wiktionary for the same Greek connection, alongside Sogdian ptγ'δ 'cup' and Khotanese phalau 'flat dish' — forms which fit an Iranian *pati-gā-δa- better than *pati-gāra-. The phonology is the crux: Old Iranian -r- does not normally yield MP -l, so *pati-gāra- should give *paygār, not paygāl; Kent's own source (Benveniste/Herzfeld) therefore attached -gāl to Skt. galati 'pours', not to gar- 'swallow'. Caution on Wiktionary here: its 'Avestan patigāra' bullet cites Nourai, p. 180 — this very chart — so it is not independent evidence.\",\n          \"derivation_fa\": \"«پیاله» بی‌گمان از فارسی میانهٔ ⟨pyg'l⟩ *paygāl «جام، ساغر» می‌آید (مکنزی، ص ۶۷)؛ صورت کهنه‌تر «پیغاله» که در نمودار هم آمده، غین میانی را نگاه داشته است. اما دربارهٔ خاستگاه کهن‌تر اختلاف هست. کنت (ص ۱۹۹) رأی هرتسفلد را نقل می‌کند که «پیاله از *pati-gāra-» است — همان چیزی که نورایی نمودار کرده. در برابر، هوبشمان در «پژوهش‌های فارسی» آن را در فصل وام‌واژه‌های یونانی می‌آورد: «piyāla جام = یونانی φιάλη»، و دهخدا نیز می‌نویسد «گویا اصل کلمه یونانی است و عرب از آن فیالجه ساخته است، یا اینکه کلمه را یونانی‌ها از ایرانیان گرفته». دانشنامهٔ ایرانیکا هم همین پیوند یونانی را می‌آورد و در کنارش سغدی ptγ'δ «جام» و ختنی phalau «کاسه» را که با *pati-gā-δa- سازگارترند. مشکل آوایی روشن است: «ر»ِ ایرانی باستان در فارسی میانه به «ل» بدل نمی‌شود، پس *pati-gāra- باید *paygār بدهد نه paygāl. هشدار: بند «اوستایی patigāra» در ویکی‌واژه خودِ نورایی (همین صفحهٔ ۱۸۰) را مأخذ گرفته و شاهد مستقل نیست. حکم: پژوهش امروزی این اشتقاق را قطعی نمی‌داند و بیشتر به وام‌گیری از یونانی یا به ریشهٔ «ریختن» گرایش دارد.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/پیاله\",\n            \"https://abadis.ir/fatofa/پیاله/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KNT:199\", \"status\": \"supports\", \"note\": \"Kent p. 199 s.v. batugara-: '… and NPers. piyāla „drinking cup“, from *pati-gāra-.' The wording is exactly Nourai's arrow — but Kent attributes it to Herzfeld and pairs it with the Skt. galati 'pours' etymology, not with gar- 'devour'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie 1971, p. 67\", \"stance\": \"supports\", \"note\": \"'*paygāl [pyg'l | N payyāla, piyāla] cup, goblet' — establishes the Middle Persian link in the chain.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien, HUB.txt line 9474 (chapter on Greek loanwords)\", \"stance\": \"contradicts\", \"note\": \"'piyāla „Becher“ = gr. φιάλη' — listed beside kalbad = καλόπόδιον and pilpil = Skt. pippalī, i.e. as a foreign loan, not an inherited *pati-gāra-.\"},\n            {\"src\": \"MON\", \"where\": \"Farhang-e Moʿin s.v. پیاله (via abadis.ir)\", \"stance\": \"silent\", \"note\": \"'(لِ) (اِ.) ۱- ظرفی که با آن شراب یا هر نوشیدنی دیگری را می‌نوشند. ۲- یکی از لوازم آتشگاه' — Moʿin gives no origin tag at all here, so the chart's own note 'MON:862 lists pîyâleh as a cognate of Greek piâle' reflects the printed edition's etymological bracket, which the online text drops; the Greek comparison is in any case Hübschmann's.\"},\n            {\"src\": \"BQT\", \"where\": \"Dehkhoda quoting the tradition (abadis.ir)\", \"stance\": \"partial\", \"note\": \"'گویا اصل کلمه یونانی است و عرب از آن فیالجه ساخته است یا اینکه کلمه را یونانیها از ایرانیان گرفته و بهمین معنی بکار برده اند' — the direction of borrowing was already undecided in the Persian lexicographical tradition.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Old Persian\",\n          \"words\": \"gar\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The root is right but the language label is not quite. Kent's Old Persian lexicon has no verb gar- 'devour': the only place the element appears in the Achaemenid corpus is the compound noun batugara- 'drinking cup, saucer' (attested once, A³Pa, and even there Kent hedges 'if genuine'), analysed as batu- 'wine' + -gara- 'devouring, drinking'; and when Kent names the verbal root he calls it Avestan — 'from root in Av. gar- „devour“, Skt. girati, Lt. vorat, pIE *gʷer-'. So an Old Persian *gar- 'to devour' is a legitimate inference from batugara- (Old Persian would regularly show *gar- for PIE *gʷer-, the labiovelar losing its labial element before a non-front vowel as in OP gaub- etc.), but it is a reconstruction, not an attested Old Persian lemma, and the chart prints it without an asterisk.\",\n          \"derivation_fa\": \"ریشه درست است ولی برچسب زبانی دقیق نیست. در واژه‌نامهٔ پارسی باستانِ کنت هیچ فعل gar- «بلعیدن» نیامده است؛ تنها جایی که این جزء در سنگ‌نبشته‌های هخامنشی دیده می‌شود ترکیب batugara- «جام شراب» است (یک بار، در A³Pa، و کنت خود می‌افزاید «اگر اصیل باشد») که آن را batu- «شراب» + ‑gara- «بلعنده، نوشنده» می‌گیرد؛ و آنجا که کنت نام ریشه را می‌برد آن را اوستایی می‌خواند: «from root in Av. gar- devour». پس *gar- پارسی باستان استنتاجی پذیرفتنی است (لبی‌کامی *gʷ در پارسی باستان پیش از واکهٔ پسین به g بدل می‌شود)، اما صورتی بازسازی‌شده است نه گواهی‌شده، و نمودار آن را بدون ستاره چاپ کرده است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"KNT:199\", \"status\": \"partial\", \"note\": \"Kent p. 199 has only 'batugara- sb. „drinking cup, saucer“: if genuine … from batu- „wine“ … + -gara- „devouring, drinking“ … from root in Av. gar- „devour“ … pIE *gʷer-.' There is no headword gar- in Kent's Old Persian lexicon (grep -nE '^(gar|gaub|garma)' KNT.txt finds only garta- 'cave/wagon').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KNT\", \"where\": \"Lexicon pp. 164-215; entry batugara-, p. 199\", \"stance\": \"partial\", \"note\": \"the compound is the sole Old Persian witness; Kent labels the verb Avestan.\"},\n            {\"src\": \"BRT\", \"where\": \"AiW s.v. ³gar-\", \"stance\": \"supports\", \"note\": \"'³gar- V. „schlucken“' — the verb is securely Avestan, so the Old Iranian root behind the OP compound is not in doubt.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"EDIV p. 104, s.v. *garH³\", \"stance\": \"supports\", \"note\": \"Cheung's Iranian root *garH³ 'to swallow' covers Old Persian by implication, but he cites no Old Persian finite form either.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": null,\n          \"words\": \"\",\n          \"verdict\": \"unverified\",\n          \"derivation\": \"An empty box. On the printed page (p. 180) the box to the right of 'Old Persian | gar: to devour' carries no language label, no word and no reference — it is a blank continuation cell of the chart's grid, presumably a slot the author left unfilled (the obvious candidate would have been a Persian reflex of OP *gar-, but nothing is printed). The extraction is faithful to the page; there is nothing to verify.\",\n          \"derivation_fa\": \"خانهٔ خالی. در صفحهٔ چاپی (ص ۱۸۰) کادر سمت راستِ «پارسی باستان | gar: بلعیدن» هیچ نام زبان، هیچ واژه و هیچ ارجاعی ندارد؛ خانه‌ای است که نویسنده پر نکرده است (به گمان، جای یک بازماندهٔ فارسی از *gar- پارسی باستان بوده). داده‌های استخراج‌شده با صفحهٔ چاپی مطابق است و چیزی برای راستی‌آزمایی وجود ندارد.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"none\", \"status\": \"not_checked\", \"note\": \"the node carries no reference in the book (refs=None).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BOOK\", \"where\": \"printed p. 180 (site/pages/210.jpg)\", \"stance\": \"silent\", \"note\": \"the box is printed empty; JSON (lang null, words []) matches the page exactly — no extraction error.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Avestan\",\n          \"words\": \"grîvâ; grîvâ-pân\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Av. grīvā- f. 'nape, neck' is a genuine Avestan word, formed with the feminine *-uā suffix on the zero grade of the root: Pokorny p. 475, §3 'With formants -uā-: … due to an ā feminine *gʷ(e)rī-uā „neck, throat area“: Old Indic grīvā, Avestan grīvā „nape“, ChSl. griva „mane“'. Bartholomae AiW s.v. grīvā- f. 'Nacken' notes it is attested only in Vd. 3.7 arəzūrahe grīvā, 'the Neck of Arəzūra', where it is already the name of a mountain ridge — so the 'neck → ridge/hump' semantics Nourai's NOTE calls for is present in the earliest attestation itself, and the comparison with *men- 'stand out' (Lat. mons, Skt. manyā- 'nape') that the NOTE invites is exactly the parallel Buck draws at 4.28. The second word is the weak point: grīvā-pāna- is not attested in Avestan (no such entry in Bartholomae); the attested form is Middle Persian grīwbān 'neck-guard, gorget' (MacKenzie p. 37), and Moʿin's footnote to Borhān p. 1807 says just that — 'پهلوی GRIVBAN … جزو اول در اوستا GRIVA (گردن) و جزو دوم پسوند اتصاف و حفاظت است، جمعاً یعنی محافظ گردن'. So the compound belongs one storey lower, in Pahlavi. The 'also a hump' gloss is Nourai's extension, not Bartholomae's.\",\n          \"derivation_fa\": \"grīvā- اوستایی، مؤنث، «پشت گردن، گردن»، واژه‌ای اصیل است: پوکورنی (ص ۴۷۵، بند ۳) آن را از صورت مؤنثِ *gʷ(e)rī-uā می‌گیرد و با grīvā سنسکریت و griva اسلاوی کهن «یال» می‌سنجد. بارتولمه یادآور می‌شود که این واژه تنها در وندیداد ۳٫۷ در ترکیب arəzūrahe grīvā «گردنِ ارزور» آمده و همان‌جا نامِ گردنهٔ کوه است؛ پس تحول معناییِ «گردن ← گردنه/برآمدگی» که نورایی در یادداشتش خواستارِ آن است، در کهن‌ترین گواه هم دیده می‌شود، و مقایسه‌اش با ریشهٔ *men- «برآمدن» (لاتینی mons، سنسکریت manyā- «پشت گردن») همان است که باک در بند ۴٫۲۸ می‌آورد. اما جزء دوم لغزش دارد: grīvā-pāna- در اوستا گواهی نشده؛ صورت گواهی‌شده پهلویِ grīwbān «گردن‌بند زره، یخهٔ محافظ» است (مکنزی ص ۳۷)، و حاشیهٔ معین بر برهان (ص ۱۸۰۷) هم دقیقاً همین را می‌گوید: «پهلوی GRIVBAN … جزو اول در اوستا GRIVA (گردن) و جزو دوم پسوند اتصاف و حفاظت است، جمعاً یعنی محافظ گردن». معنای «برآمدگی/کوهان» هم افزودهٔ نورایی است نه بارتولمه.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"POK:475\", \"status\": \"supports\", \"note\": \"POK, within the gʷer-1 article: '3. With formants -uā-: … Old Indic grīvā, Avestan grīvā „nape“, Latvian grīva „embouchure, estuary“ … Old Church Slavic griva „mane“, grivьna „collar, neckband“.' Page 475 is the middle of the 474-476 article, which is where §3 falls.\"},\n            {\"ref\": \"BQT:1807\", \"status\": \"supports\", \"note\": \"Borhān-e Qāṭeʿ ed. Moʿin p. 1807 (BQT_v3_picofile.pdf pdf-page 602), footnote 6: 'اوستا GRIVA (گردنه [کوه])، پهلوی GRIVAK (گردنه [کوه])، هندی باستان GRIVA (پشت گردن)، اشتقاق ۹۱۳؛ رک: گریبان'; footnote 5 (s.v. گریبان): 'پهلوی GRIVBAN … جزو اول در اوستا GRIVA (گردن) و جزو دوم پسوند اتصاف و حفاظت است، جمعاً یعنی محافظ گردن'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"AiW s.v. grīvā- (BRT.txt line 10493), and line 5616\", \"stance\": \"partial\", \"note\": \"'j. grīvā- f. „Nacken“ … arəzūrahe grīvā (LS.) V.3.7'; and at line 5616 'grīvā- f. „Nacken“ als Name eines Bergs' — supports grīvā-, but there is no grīvā-pāna- in Bartholomae (grep for paiti/pāna compounds finds none).\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 4.28 NECK, p. 233\", \"stance\": \"supports\", \"note\": \"'Skt. grīvā- (in Vedic only pl. „vertebrae of the neck“), Av. grīvā- (Vend. 3.7, of a mountain called here the „neck“; elsewhere also „head“ or „back“ of Arəzura, name of a fiend; NPers. gariva „hill“) : Grk. δέρη „neck“ … all prob. as orig. „throat“ : Skt. gṛ- „swallow“ … Walde-P. 1.683.'\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie 1971, p. 37\", \"stance\": \"partial\", \"note\": \"'grīwbān [glywp'n' | N girībān] neck-guard, gorget' — the compound is Middle Persian, not Avestan.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Persian\",\n          \"words\": \"garîveh «گریوه»; garîbân «گریبان»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both words descend from the grīv- stem through Middle Persian. (i) گریوه garīva 'hill, low mountain, ridge, mountain pass' < MP grīwag 'hill, ridge' (MacKenzie p. 37: 'grīwag [glywk'] | N girīwa] hill, ridge'), itself the -ag derivative of grīw 'neck, throat'; the semantic route 'neck > ridge' is already Avestan (Vd. 3.7 'the Neck of Arəzūra' is a mountain), and Buck states it as fact: 'NPers. gariva „hill“'. Moʿin's dictionary keeps both senses side by side — 'گریوه (گَ وِ) [په.] (اِ.) ۱- گردن، پشت گردن. ۲- کوه پست، پشته، تپه' — and Dehkhoda gives the chain 'پهلوی گریو [گردن، پشت گردن]، اوستا گریوا'. Hāfez's line quoted in the chart ('آن به کزین گریوه سبکسار بگذری') uses the topographic sense. (ii) گریبان garībān 'collar' < MP grīwbān 'neck-guard, gorget' = grīw 'neck' + -bān, the agent/protector suffix (as in باغبان، دربان); MP -w- was vocalised and the word entered New Persian with the regular b of the suffix. Nothing here is controversial.\",\n          \"derivation_fa\": \"هر دو واژه از ستاک grīv- و از راه فارسی میانه آمده‌اند. ۱) «گریوه» از پهلوی grīwag «تپه، پشته» (مکنزی ص ۳۷)، خود مشتقِ ‑ag از grīw «گردن»؛ تحول معناییِ «گردن ← گردنه، پشته» از اوستا آغاز شده است (وندیداد ۳٫۷ «گردنِ ارزور» نام کوه است) و باک آن را چنین ثبت می‌کند: «NPers. gariva „hill“». معین هر دو معنی را کنار هم نگه داشته: «گریوه (گَ وِ) [په.] (اِ.) ۱- گردن، پشت گردن. ۲- کوه پست، پشته، تپه»، و دهخدا زنجیره را می‌آورد: «پهلوی گریو [گردن، پشت گردن]، اوستا گریوا». بیت حافظ که در نمودار نقل شده («آن به کزین گریوه سبک‌سار بگذری») به همین معنای جغرافیایی است. ۲) «گریبان» از پهلوی grīwbān «محافظ گردن» است: grīw «گردن» + پسوند ‑بان (مانند باغبان و دربان). ادعای نورایی در این گره کاملاً درست است.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/گریوه/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"SYN:233\", \"status\": \"supports\", \"note\": \"Buck, Selected Synonyms, §4.28 NECK, p. 233: 'Skt. grīvā-, Av. grīvā- (Vend. 3.7, of a mountain called here the „neck“ … NPers. gariva „hill“) : Grk. δέρη „neck“ … all prob. as orig. „throat“ : Skt. gṛ- „swallow“ … Walde-P. 1.683.' — the whole of Nourai's arrow, root included, in one sentence.\"},\n            {\"ref\": \"BQT:1807\", \"status\": \"supports\", \"note\": \"Borhān-e Qāṭeʿ ed. Moʿin p. 1807 (pdf-page 602 of BQT_v3_picofile.pdf) is the گریبان page; Moʿin's footnote 5 reads 'گریبان - بکسر اول. پهلوی GRIVBAN «اشتقاق ۹۱۳». جزو اول در اوستا GRIVA (گردن) و جزو دوم پسوند اتصاف و حفاظت است، جمعاً یعنی محافظ گردن؛ بخشی از جامه که اطراف گردن قرار گیرد', and footnote 6 'اوستا GRIVA (گردنه [کوه])، پهلوی GRIVAK (گردنه [کوه])'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie 1971, p. 37\", \"stance\": \"supports\", \"note\": \"'grīwag [glywk'] | N girīwa] hill, ridge'; 'grīwbān [glywp'n' | N girībān] neck-guard, gorget'; '1grīw [CWLE] neck, throat'. Both New Persian outcomes are given by MacKenzie himself.\"},\n            {\"src\": \"MON\", \"where\": \"Farhang-e Moʿin s.v. گریوه (via abadis.ir)\", \"stance\": \"supports\", \"note\": \"'(گَ وِ) [ په . ] (اِ. ) ۱ - گردن ، پشت گردن . ۲ - کوه پست ، پشته ، تپه' — the [په.] tag makes it a Pahlavi inheritance, and both senses are kept.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 4.28, p. 233\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n            {\"src\": \"BQT\", \"where\": \"Dehkhoda s.v. گریوه (via abadis.ir)\", \"stance\": \"supports\", \"note\": \"'گریوه. [ گ َ/ گ ِ ری وَ / وِ ] ( اِ ) پهلوی، گریو [گردن، پشت گردن] اوستا، گریوا' — glossed as a small mountain / ridge.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"Greek\",\n          \"words\": \"bronxos\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Gk. βρόγχος brónkhos 'windpipe, throat' (with βρόγχια, the plural used for the bronchial tubes) is assigned to this root by Nourai's cited authority: Watkins/AHD s.v. gʷerə-4 §4 'Extended form *gʷrō- (< *gʷerō-) in Greek brō- in: … b. nasalized variant form *bhro-n-kh- in Greek bronkhos, windpipe, throat: BRONCHO-, BRONCHUS'. Pokorny gives the same analysis with more hesitation: at the end of §4 (p. 475-476) 'With nasalization in addition perhaps gr. βρόγχος m., Ionian βρογχίη „windpipe“, βράγχια „gill of fish; trachea“ seems in Vok. reshaped after βραγχάω „be hoarse“ … but it must be separated from βρόγχος'. Greek βρ- from *gʷr- is regular (cf. βορά, βιβρώσκω on the same page). Against this, Etymonline reports that brónkhos 'is of unknown etymology', which reflects Beekes's view that it is a Pre-Greek word. So the attachment is the standard American-Heritage one but not secure.\",\n          \"derivation_fa\": \"واژهٔ یونانی βρόγχος «نای، گلو» (جمعِ βρόγχια برای نایژه‌ها) در همان مرجعی که نورایی به آن ارجاع می‌دهد به این ریشه بسته شده است: واتکینز ذیل gʷerə-4 می‌نویسد «صورتِ خیشومی‌شدهٔ *bhro-n-kh- در یونانی bronkhos „نای، گلو“». پوکورنی هم همین را می‌آورد ولی با تردید: «با خیشومی‌شدن، شاید یونانی βρόγχος … که در واکه‌اش زیر تأثیر βραγχάω „گرفته‌صدا شدن“ بازساخته شده». تبدیل *gʷr- به βρ- در یونانی قاعده‌مند است (سنجید با βορά و βιβρώσκω در همان صفحه). در برابر، اتیمونلاین (و به پیروی از بیکس) می‌گوید ریشهٔ این واژه «ناشناخته» و احتمالاً پیشایونانی است. پس ادعای نورایی همان دیدگاه AHD است، اما قطعی نیست.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/bronchitis\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. gʷerə-4 §4b: 'nasalized variant form *bhro-n-kh- in Greek bronkhos, windpipe, throat: BRONCHO-, BRONCHUS. [Pok. 1. gʷer- 474.]'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW I 475-476, §4 of gʷer-1\", \"stance\": \"partial\", \"note\": \"'With nasalization in addition perhaps gr. βρόγχος m., Ionian βρογχίη „windpipe“ … seems in Vok. reshaped after βραγχάω „be hoarse“ … it must be separated from βρόγχος' — Pokorny includes it but with 'perhaps'.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. bronchia / bronchus\", \"stance\": \"partial\", \"note\": \"KLN_1966: 'bronchiole … fr. L. bronchia (pl.), „the bronchial tubes“' — Klein derives the Latin from Gk. βρόγχια but offers no PIE root.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 683-684\", \"stance\": \"partial\", \"note\": \"Walde-Pokorny treat the βρ- forms under gʷer- with the same hesitations as Pokorny 1959.\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"An unlabelled pass-through box: the French relay between Greek and Persian. French bronche (pl. bronches) 'bronchial tubes' comes from Late Latin bronchia < Gk. βρόγχια, and the disease name bronchite was formed in French in the first half of the 19th century on the model of the Modern Latin bronchitis coined in 1808. It is French bronchite — not English bronchitis — that Persian borrowed (see node 12), so the box is correctly placed even though the book prints no word in it.\",\n          \"derivation_fa\": \"این کادر بی‌واژه، حلقهٔ واسطِ فرانسه میان یونانی و فارسی است. فرانسویِ bronche «نایژه» از لاتینی متأخر bronchia و آن از یونانی βρόγχια است، و نام بیماری bronchite در نیمهٔ نخست سدهٔ نوزدهم در فرانسه بر الگوی bronchitis لاتینِ نو (ساختهٔ ۱۸۰۸) پدید آمد. فارسی «برونشیت» را از همین صورت فرانسوی گرفته است نه از انگلیسی؛ پس جای این کادر در نمودار درست است، هرچند کتاب واژه‌ای در آن چاپ نکرده.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/bronchitis\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"none\", \"status\": \"not_checked\", \"note\": \"the box carries no reference in the book (refs=None).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. bronchitis\", \"stance\": \"supports\", \"note\": \"KLN_1971: 'bronchitis, n., inflammation of the bronchial tubes (med.) — Medical L., coined by Charles Bedham …' — the Modern Latin form on which French bronchite was built.\"},\n            {\"src\": \"BOOK\", \"where\": \"printed p. 180 (site/pages/210.jpg)\", \"stance\": \"silent\", \"note\": \"the box is printed with the label 'French' and no word; the extraction (lang 'French', words []) matches the page.\"}\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"Persian\",\n          \"words\": \"bronšît «برونشیت»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian برونشیت boronšit 'bronchitis' is a 20th-century medical loan from French bronchite, as the pronunciation shows: the -sh- of برونشیت renders French /ʃ/ in bronchite (English or Latin bronchitis would have given *بronkitis with k). This is the standard route for Persian medical vocabulary of the Qajar/Pahlavi period, which came through French via the Dār al-Fonūn. The final -t reflects French -te; Persian has no separate feminine ending. Moʿin's dictionary marks such words [فر.] (French).\",\n          \"derivation_fa\": \"«برونشیت» وام‌واژه‌ای پزشکی از سدهٔ بیستم و از فرانسویِ bronchite است؛ گواهش خودِ تلفظ است: «ش» در برونشیت برابرِ /ʃ/ فرانسوی است، حال آنکه اگر از انگلیسی یا لاتین گرفته شده بود «ک» می‌داشتیم (*برونکیتیس). این همان مسیر همیشگیِ واژگان پزشکی فارسی در دورهٔ قاجار و پهلوی است که از راه دارالفنون و زبان فرانسه وارد شد. «ت» پایانی بازتاب ‑te فرانسوی است. معین چنین واژه‌هایی را با نشانهٔ [فر.] مشخص می‌کند. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"MON:514\", \"status\": \"not_checked\", \"note\": \"Moʿin's 6-vol Farhang-e Fārsi is not page-mapped online and its archive.org OCR is unusable; p. 514 is consistent with the ب range of the continuous lexicon pagination (cf. MON:862 for پ and MON:1408 for خ cited elsewhere on this chart). The Persian word and its French source are not in doubt.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. bronchitis\", \"stance\": \"supports\", \"note\": \"'Medical L., coined by Charles Bedham' — establishes the modern coinage that French bronchite and Persian برونشیت both continue.\"},\n            {\"src\": \"BOOK\", \"where\": \"printed p. 180 (site/pages/210.jpg)\", \"stance\": \"supports\", \"note\": \"the page prints 'bronšît' with the script برونشیت and the reference MON:514; the JSON matches.\"}\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"English\",\n          \"words\": \"bronchitis\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English bronchitis was coined in Modern Latin in 1808 by the physician Charles Badham (Klein prints 'Bedham'), from bronchia 'the bronchial tubes' (Latinised Gk. βρόγχια, pl. of βρόγχος) + the medical suffix -itis 'inflammation'; bronchial had entered English in the 1670s and bronchus is the singular in anatomical use. So the arrow Greek → English is right in substance, with Modern Latin as the actual workshop in which the word was made — a routine step for -itis coinages of the period.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی bronchitis در سال ۱۸۰۸ به دست پزشکی به نام چارلز بدهام در لاتینِ نو ساخته شد: bronchia «نایژه‌ها» (صورت لاتینی‌شدهٔ βρόγχια، جمعِ βρόγχος یونانی) به‌علاوهٔ پسوند پزشکیِ ‑itis «التهاب». صفت bronchial از دههٔ ۱۶۷۰ در انگلیسی بوده و bronchus صورت مفردِ کالبدشناختی است. پس پیکانِ «یونانی ← انگلیسی» در اصل درست است، با این توضیح که کارگاهِ ساختِ واژه لاتینِ نو بوده است، چنان‌که در همهٔ واژه‌های ‑itis آن دوره.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/bronchitis\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"none\", \"status\": \"not_checked\", \"note\": \"the node carries no reference in the book (refs=None); the parent Greek node cites AHD, which does list BRONCHO-, BRONCHUS under gʷerə-4.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein, A Comprehensive Etymological Dictionary, s.v. bronchitis\", \"stance\": \"supports\", \"note\": \"'bronchitis, n., inflammation of the bronchial tubes (med.) — Medical L., coined by Charles Bedham …'; and s.v. bronchiole 'fr. L. bronchia (pl.), „the bronchial tubes“'.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gʷerə-4 §4b\", \"stance\": \"supports\", \"note\": \"'Greek bronkhos, windpipe, throat: BRONCHO-, BRONCHUS' — the English derivatives are listed at the root.\"}\n          ]\n        },\n        {\n          \"id\": 14,\n          \"lang\": \"Latin\",\n          \"words\": \"vorâre\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin vorāre 'to swallow, devour' is the textbook o-grade derivative of this root: AHD gʷerə-4 §2 'Suffixed o-grade form *gʷor-ə- in Latin vorāre, to swallow up'. Pokorny p. 474 sets it beside Gk. βορά 'food' — 'gr. βορά f. „food fed to livestock, dish, food“ (= Latin *vora, whereof vorare)' — and lists vorāgō 'gullet, chasm' and carni-vorus in the same paragraph. PIE *gʷ- gives Latin v- before o (as in vīvus < *gʷih₃-wo-), which is exactly what *gʷor-ā- requires. Ernout-Meillet s.v. uoro confirm the root shape: 'La racine dissyllabique *gʷerə-, *gʷre/o- „avaler“ … Le latin a le dérivé uorare.'\",\n          \"derivation_fa\": \"لاتینیِ vorāre «بلعیدن، فروبردن» نمونهٔ کتابیِ صورتِ o-درجهٔ این ریشه است: واتکینز ذیل gʷerə-4 می‌نویسد «*gʷor-ə- در لاتینی vorāre». پوکورنی (ص ۴۷۴) آن را کنار βορά یونانی «خوراک» می‌گذارد و در همان بند vorāgō «مغاک» و carni-vorus را می‌آورد. تبدیل *gʷ هندواروپایی به v لاتینی پیش از o قاعده‌مند است (چنان‌که vīvus از *gʷih₃-wo-). ارنو و مه‌یه هم می‌نویسند: «ریشهٔ دوهجاییِ *gʷerə-, *gʷre/o- „فروبردن“ … لاتین مشتقِ uorare را دارد». ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. gʷerə-4 §2: 'Suffixed o-grade form *gʷor-ə- in Latin vorāre, to swallow up: VORACIOUS, -VOROUS; DEVOUR.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW I 474\", \"stance\": \"supports\", \"note\": \"'gr. βορά f. „food fed to livestock, dish, food“ (= Latin *vora, whereof vorare) … Latin voro, -are „engorgement“, vorago „gullet“, carni-vorus.'\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. uoro (LAT.txt line 70258 ff.)\", \"stance\": \"supports\", \"note\": \"'uoro, -as, -aui, -atum, -are: avaler, engloutir … Dérivés et composés: uorāx, uorācitās, uorāgō: gouffre, abîme … carni-uorus, Pline … La racine dissyllabique *gʷerə-, *gʷre/o- „avaler“ … Le latin a le dérivé uorare.'\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 683\", \"stance\": \"supports\", \"note\": \"'lat. voro, -āre „verschlingen“, vorāgō „Schlund“, carni-vorus.'\"}\n          ]\n        },\n        {\n          \"id\": 15,\n          \"lang\": \"English\",\n          \"words\": \"voracious, carnivorous\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both are learned Latinisms of the 17th century. voracious < Latin vorāx (stem vorāc-) 'greedy, devouring', an adjective in -āx from vorāre, with the English adjectival suffix -ious substituted for -āx; carnivorous < Latin carnivorus 'flesh-eating' = carō, carn- 'flesh' (PIE *(s)ker- 'cut') + -vorus, the compound-final of vorāre. Both English words are listed at the root by Watkins ('VORACIOUS, -VOROUS; DEVOUR'), and Ernout-Meillet note that carni-uorus is first in Pliny and is itself a calque of Gk. σαρκοφάγος.\",\n          \"derivation_fa\": \"هر دو واژه وام‌های عالمانهٔ سدهٔ هفدهم از لاتین‌اند. voracious از لاتینیِ vorāx (ستاک vorāc-) «پرخور، بلعنده»، صفتی با پسوند ‑āx از vorāre، که در انگلیسی پسوند ‑ious جای ‑āx را گرفته است؛ carnivorous از لاتینیِ carnivorus «گوشت‌خوار»، مرکب از carō/carn- «گوشت» و ‑vorus، جزء پایانیِ ترکیبیِ vorāre. واتکینز هر دو را در همان مدخل ریشه فهرست کرده («VORACIOUS, -VOROUS; DEVOUR»)، و ارنو و مه‌یه یادآور می‌شوند که carni-uorus نخست‌بار در پلینیوس و گرته‌برداری از σαρκοφάγος یونانی است. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. gʷerə-4 §2 lists exactly 'VORACIOUS, -VOROUS; DEVOUR' as the English outcomes of Latin vorāre.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. uoro\", \"stance\": \"supports\", \"note\": \"'Dérivés et composés: uorāx (class.) … carni-uorus, Pline, d'après σαρκοφάγος; omniuorus (id.) composés savants imités du grec.'\"},\n            {\"src\": \"POK\", \"where\": \"IEW I 474\", \"stance\": \"supports\", \"note\": \"'Latin carni-vorus „carnivorous“' cited beside Skt. aja-gara- and Gk. δημο-βόρος.\"}\n          ]\n        },\n        {\n          \"id\": 16,\n          \"lang\": \"Indo-European\",\n          \"words\": \"Gargelos, Gulgul\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Both 'roots' are Mann's lemmas, quoted accurately: IEC p. 265 'gargəlos, ā „babbling, raucous; babble, bubbling, gurgle, croak“. Onomat.' and IEC p. 305 'gulgul-, gulugul- „gurgle“'. But Mann labels both Onomat., i.e. independent sound-imitation rather than inherited PIE lexemes, and he cross-refers them to WP I 538 and 683 — two different articles. Pokorny is equally guarded: he puts the γαργ-/gurg- material in §5 of gʷer-1 'With pure velar: gr. γέργερος … γαργαρεών „uvula in mouth“, γαργαρίζω „gurgle“ … perhaps through labialization after forms with γυρ- … yet is previously ger- besides gʷer- because of gel- besides gʷel- is safe' — i.e. the reduplicated 'gargle' family may belong to a plain-velar ger-, distinct from labiovelar gʷer-. So the sub-root box is legitimately drawn from Mann, but its attachment to Gwer 3 is loose: these are expressive reduplications that any language can and did make afresh.\",\n          \"derivation_fa\": \"هر دو «ریشه» سرواژه‌های فرهنگ مان‌اند و نورایی آنها را درست نقل کرده است: در ص ۲۶۵ «gargəlos، ā „پرگو، خشن؛ غرغره، قلقل“. Onomat.» و در ص ۳۰۵ «gulgul-، gulugul- „غرغره کردن“». اما مان هر دو را «آواواژه» (Onomat.) می‌خواند، یعنی ساختِ تقلید صوتی و نه واژهٔ به‌ارث‌رسیدهٔ هندواروپایی، و آنها را به دو مقالهٔ جداگانهٔ والده-پوکورنی ارجاع می‌دهد. پوکورنی هم محتاط است: این خانواده را در بند ۵ ذیل gʷer-1 و «با کامیِ ساده» می‌آورد و می‌گوید در کنارِ gʷer- ریشهٔ ger- نیز به‌یقین هست، همان‌گونه که در کنار gʷel- ریشهٔ gel- هست. پس این کادر از مان گرفته شده و درست است، ولی پیوندش با ریشهٔ اصلی سست است: این‌گونه صورت‌های مکرّر آواگون را هر زبانی می‌تواند از نو بسازد.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"IEC:265,305\", \"status\": \"supports\", \"note\": \"IEC.txt leaf carrying the printed number 265: 'gargəlos, ā „babbling, raucous; babble, bubbling, gurgle, croak“. Onomat. Cf. WP I, 538 & 683 Skt. gárgaraḥ, gargarā; Per. γarγara „gurgle“ …'; the leaf carrying 305: 'gulgul-, gulugul- „gurgle“. Cf. gul-, gulg-. WP I, 683 Per. γulγul „clamour“ …'. Both page numbers are exact.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"IEC\", \"where\": \"Mann pp. 265 and 305\", \"stance\": \"partial\", \"note\": \"the lemmas exist verbatim, but Mann's own label is 'Onomat.', which is not a genealogical derivation from *gʷer-.\"},\n            {\"src\": \"POK\", \"where\": \"IEW I 476, §5 of gʷer-1\", \"stance\": \"partial\", \"note\": \"'5. With pure velar: gr. γέργερος βρόγχος Hes., γαργαρεών „uvula in mouth“, γαργαρίζω „gurgle“ … perhaps through labialization after forms with γυρ- …, yet is previously ger- besides gʷer- because of gel- besides gʷel- is safe.'\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 683, 'Mit voller oder gebrochener Reduplikation'\", \"stance\": \"partial\", \"note\": \"'ai. gargara-ḥ „Schlund, Strudel“; lit. gargaliuoju „röchle, glucke“; lat. gurgulio … „Gurgel, Luftröhre“' — Walde-Pokorny do treat the reduplicated set under gʷer-, as a reduplication of it rather than a separate root.\"}\n          ]\n        },\n        {\n          \"id\": 17,\n          \"lang\": \"Persian\",\n          \"words\": \"ğerğereh «غرغره»; xerxereh «خرخره»; ğolğol «غُلْغُل ، قُلْقُل»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"All three are living Persian words, and two of them are cited by Nourai's own source: Mann gives 'Per. γarγara „gurgle“' at IEC 265 and 'Per. γulγul „clamour“' at IEC 305. But their history is not inheritance from PIE. غرغره ġarġara 'gargling' is the Arabic verbal noun of the reduplicated quadriliteral غرغر ġarġara, which Arabic lexicography and Wiktionary both treat as onomatopoeic (a 'reduplicated onomatopoeic root' غ‑ر‑غ‑ر); it entered Persian as an Arabic-form loan, as did غلغل/قلقل ġulġul/qulqul 'bubbling, gurgling' (the doublet with غ and ق is itself a mark of imitative, non-etymological spelling). خرخره xerxere 'rattling in the throat, windpipe' is a native Persian reduplication of the same imitative type, formed on the خر of خرناس/خروپف. So the words are real and the sound-symbolism is the same the world over; what they are not is descendants of *gʷer- by regular sound change. Nourai's arrow is best read as 'same imitative pattern', which is how Mann intends it.\",\n          \"derivation_fa\": \"هر سه واژه در فارسی زنده‌اند و دوتای آنها را خودِ منبعِ نورایی آورده است: مان در ص ۲۶۵ «Per. γarγara» و در ص ۳۰۵ «Per. γulγul» را ثبت کرده. اما تاریخ این واژه‌ها تاریخِ وراثت از هندواروپایی نیست. «غرغره» مصدرِ عربیِ فعل رباعیِ مکررِ «غَرْغَرَ» است که فرهنگ‌های عربی و ویکی‌واژه هر دو آن را ریشهٔ مکررِ آواگون (غ‑ر‑غ‑ر) می‌دانند؛ این واژه با ساخت عربی وارد فارسی شده، و همچنین است «غلغل/قلقل» که دوگانگی املای آن با «غ» و «ق» خود نشانهٔ آواواژه بودن است. «خرخره» ساختِ مکررِ بومیِ فارسی از همان گونه است و بر پایهٔ «خر»ِ خرناس و خروپف ساخته شده. پس واژه‌ها اصیل‌اند و تقلید صوتی در همهٔ زبان‌ها یکسان عمل می‌کند، اما این‌ها بازماندهٔ قاعده‌مندِ ریشهٔ *gʷer- نیستند. پیکان نورایی را باید «هم‌الگو بودن آواواژه‌ها» خواند، نه اشتقاق؛ و مان هم همین را در نظر داشته است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/غرغر\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IEC:265,305\", \"status\": \"supports\", \"note\": \"p. 265: 'Onomat. … Skt. gárgaraḥ, gargarā; Per. γarγara „gurgle“; Gk. gárgalos'; p. 305: 'gulgul-, gulugul- „gurgle“ … WP I, 683 Per. γulγul „clamour“; Arm. klklunkʿ „gurgle“'. Both Persian words are literally in Mann, under the 'Onomat.' heading.\"},\n            {\"ref\": \"MON:1408\", \"status\": \"not_checked\", \"note\": \"Moʿin cannot be checked by page (no page-mapped copy); p. 1408 falls in the خ range of the continuous lexicon pagination, so it most likely covers خرخره rather than the two غ words, which would sit some 900 pages later.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. gargle/gargoyle\", \"stance\": \"partial\", \"note\": \"'from the imitative base *garg-' — Klein treats the whole γαργ-/garg- family as imitative, which is the right frame for the Persian words too.\"},\n            {\"src\": \"AFM\", \"where\": \"Addi Shir, Kitāb al-alfāẓ al-fārisiyya al-muʿarraba\", \"stance\": \"silent\", \"note\": \"grep for غرغر / غلغل in AFM.txt and TAD.txt returns nothing — neither Addi Shir nor al-Unaysi claims these are Persian words arabicised, consistent with their being Arabic onomatopoeic formations.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann pp. 265, 305\", \"stance\": \"partial\", \"note\": \"supports the forms, labels them onomatopoeic rather than inherited.\"}\n          ]\n        },\n        {\n          \"id\": 18,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"gargarah\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Skt. gargara- is genuinely attested and genuinely belongs here, but not with the gloss the chart gives. Pokorny p. 475, in the reduplication paragraph, has 'Old Indic gargara-ḥ „gullet, whirlpool“'; Walde-Pokorny I 683 'ai. gargara-ḥ „Schlund, Strudel“'; Mann at IEC 265, the very page Nourai cites, glosses it 'Skt. gárgaraḥ „whirlpool“; gargarā „churn“'. The Vedic word denotes a whirlpool or a churning-vessel (RV gargara- is also a musical instrument), i.e. a thing that makes a gurgling noise — not the act of gargling. So the derivation from a reduplicated *gʷer-/ger- base is confirmed; the English gloss 'gargle' in the chart is Nourai's simplification of his source.\",\n          \"derivation_fa\": \"واژهٔ سنسکریتِ gargara- گواهی‌شده است و به‌راستی به همین خانواده تعلق دارد، اما معنایش آن نیست که نمودار می‌گوید. پوکورنی (ص ۴۷۵) در بندِ مضاعف‌سازی می‌آورد «هندی باستان gargara-ḥ „گلو، گرداب“»، والده-پوکورنی (ج ۱، ص ۶۸۳) «Schlund, Strudel»، و مان در همان ص ۲۶۵ که نورایی ارجاع داده آن را «gárgaraḥ „گرداب“؛ gargarā „مشک/خیک دوغ‌زنی“» معنی می‌کند. واژهٔ ودایی نامِ گرداب یا ظرفِ دوغ‌زنی است، یعنی چیزی که صدای قلقل می‌دهد، نه خودِ عملِ غرغره. پس اشتقاق آن از ستاکِ مضاعفِ *ger-/gʷer- درست است و تنها معنایی که در نمودار آمده ساده‌سازیِ نورایی از منبع خودش است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"IEC:265\", \"status\": \"partial\", \"note\": \"IEC p. 265 s.v. gargəlos: 'Skt. gárgaraḥ, gargarā' glossed at the head of the neighbouring lemma gargəló as 'Skt. gárgaraḥ „whirlpool“; gargara „churn“' — the word is there, the meaning is 'whirlpool/churn', not 'gargle'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW I 475, §2 'With full or fractured reduplication'\", \"stance\": \"partial\", \"note\": \"'Old Indic gargara-ḥ „gullet, whirlpool“; Intens. ni-galgalīti, ni-jalgulīti „devours“' — supports the derivation, differs on the gloss.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 683\", \"stance\": \"partial\", \"note\": \"'ai. gargara-ḥ „Schlund, Strudel“' — same.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann p. 265\", \"stance\": \"partial\", \"note\": \"see ref_check.\"}\n          ]\n        },\n        {\n          \"id\": 19,\n          \"lang\": \"Latin\",\n          \"words\": \"gurges; gurguliô\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin gurges 'whirlpool, gulf, (poetically) gullet' and gurguliō 'windpipe, gullet' are the Latin members of the reduplicated set: Pokorny p. 475 '2. With full or fractured reduplication: … Latin gurgulio (-ur- as in Balto-Slavic) „gullet, windpipe“, gurges „(gullet =) whirlpool, whirl, deep pool“, gurgustium … „a small, mean dwelling“'; Watkins puts the same forms at the root, '3. Expressive reduplicated form *gʷr̥-g- in Latin gurges, throat, also gulf, whirlpool: GARGET, GORGE, GORGET, GURGITATION; INGURGITATE, REGURGITATE'. The -ur- vocalism (from syllabic *r̥ before a labiovelar) is exactly what a reduplicated *gʷr̥-gʷ- would give. Note that Nourai's gloss for gurges, 'throat', is the secondary/poetic sense; the ordinary sense is 'whirlpool, flood'.\",\n          \"derivation_fa\": \"لاتینیِ gurges «گرداب، مغاک، (در شعر) گلو» و gurguliō «نای، حلقوم» اعضای لاتینیِ همین مجموعهٔ مضاعف‌اند: پوکورنی (ص ۴۷۵، بند ۲ «با مضاعف‌سازی کامل یا شکسته») می‌آورد «لاتینی gurgulio „حلقوم، نای“، gurges „(حلقوم =) گرداب، چرخاب، آبِ ژرف“»، و واتکینز همان صورت‌ها را ذیل ریشه می‌گذارد: «صورتِ مضاعفِ بیانگرِ *gʷr̥-g- در لاتینی gurges». واکهٔ ‑ur‑ (از *r̥ هجایی پیش از لبی‌کامی) دقیقاً همان چیزی است که از *gʷr̥-gʷ- انتظار می‌رود. تنها نکته آنکه معنای «گلو» برای gurges معنای ثانوی و شاعرانه است؛ معنای رایج آن «گرداب» است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. gʷerə-4 §3: 'Expressive reduplicated form *gʷr̥-g- in Latin gurges, throat, also gulf, whirlpool: GARGET, GORGE, GORGET, GURGITATION; INGURGITATE, REGURGITATE.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW I 475, §2\", \"stance\": \"supports\", \"note\": \"'Latin gurgulio (-ur- as in Balto-Slavic) „gullet, windpipe“, gurges „(gullet =) whirlpool, whirl, deep pool“.'\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 683\", \"stance\": \"supports\", \"note\": \"'lat. gurgulio (-ur- wie im Balt.-Sl.) „Gurgel, Luftröhre“, gurges „(Schlund =) Strudel, Wirbel, tiefes Gewässer“.'\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. uoro (cross-reference)\", \"stance\": \"partial\", \"note\": \"under uorāgō Ernout-Meillet quote Cic. Sest. 53 'gurges et uorago patrimonii', pairing gurges with uorago in the same semantic field.\"}\n          ]\n        },\n        {\n          \"id\": 20,\n          \"lang\": \"English\",\n          \"words\": \"gargle\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"English gargle does not come from Latin gurges/gurguliō as drawn. Klein: 'gargle, intr. and tr. v. — F. gargouiller, „to gurgle, dabble, paddle“, fr. gargouille, „throat“, from the imitative base *garg-'; Etymonline agrees (first attested 1520s; from French gargouiller, from Old French gargole 'throat, waterspout', imitative garg- + goule 'mouth' < Latin gula), and adds that the older English learned form was gargarize, borrowed from Latin gargarizāre < Gk. γαργαρίζειν. Watkins, the reference cited here, lists GARGET, GORGE, GORGET, GURGITATION, INGURGITATE, REGURGITATE under gurges — gargle is not among them. The connection is not wholly severed: the imitative *garg- of gargouille is precisely Mann's gargəlos (node 16) and Pokorny's plain-velar γαργαρίζω, so gargle belongs in this chart, but under the 'Gargelos' box and via French, not as a descendant of Latin gurges.\",\n          \"derivation_fa\": \"واژهٔ انگلیسیِ gargle چنان‌که در نمودار کشیده شده از لاتینیِ gurges/gurguliō نیامده است. کلاین می‌نویسد: «gargle از فرانسویِ gargouiller „غرغره کردن“، از gargouille „گلو“، از پایهٔ آواگونِ *garg-». اتیمونلاین نیز همین را می‌گوید (نخستین گواه در دههٔ ۱۵۲۰؛ از فرانسویِ gargouiller، از فرانسویِ کهن gargole «گلو، ناودان»، از garg- آواگون + goule «دهان» از gula لاتینی) و می‌افزاید که صورتِ عالمانهٔ کهن‌ترِ انگلیسی gargarize بوده که از لاتینیِ gargarizāre و آن از γαργαρίζειν یونانی گرفته شده. واتکینز — همان مرجعی که در این گره ذکر شده — ذیل gurges واژه‌های GARGET، GORGE، GORGET، GURGITATION، INGURGITATE و REGURGITATE را می‌آورد و gargle در میان آنها نیست. البته پیوند به‌کلی گسسته نیست: پایهٔ آواگونِ *garg- در gargouille همان gargəlos مانِ (گرهٔ ۱۶) و γαργαρίζω پوکورنی است؛ پس جای gargle در این نمودار هست، ولی زیر کادر «Gargelos» و از راه فرانسه، نه به‌عنوان بازماندهٔ gurges لاتینی. حکم: پژوهش امروزی این پیکان را رد می‌کند.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/gargle\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"not_found\", \"note\": \"Watkins 1985 s.v. gʷerə-4 §3 lists 'GARGET, GORGE, GORGET, GURGITATION; INGURGITATE, REGURGITATE' as the English words from Latin gurges. GARGLE is absent from the whole gʷerə-4 article (grep of AHD_watkins1985.txt confirms).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. gargle (KLN_1971)\", \"stance\": \"contradicts\", \"note\": \"'gargle, intr. and tr. v. — F. gargouiller, „to gurgle, dabble, paddle“, fr. gargouille, „throat“, from the imitative base *garg-. See prec. word and cp. next word and gurgle.'\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary, s.v. Gargle\", \"stance\": \"contradicts\", \"note\": \"SKT.txt has the headword 'Gargle' with the reference 'Cot(grave)', i.e. Skeat too derives it from the French verb recorded in Cotgrave's 1611 French-English dictionary, not from Latin gurges.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann p. 265, s.v. gargəló/gargəlos\", \"stance\": \"partial\", \"note\": \"'It. gargagliare („babble, purl“, beside gorgogliare)' and 'LLat. gargala „windpipe“' — the Romance forms behind French gargouiller belong to the imitative garg- set, i.e. to node 16, not to gurges.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-210.json > /dev/null && echo \"JSON OK\"",
 "description": "Write verification file for page 210"
}
```


### [2026-09-06T15:11:14.082Z] TOOL RESULT

```
JSON OK
```


## [2026-09-06T15:11:17.834Z] TOOL CALL #71: Bash

```json
{
 "command": "python3 tools/verify_check.py 210",
 "description": "Run verify_check for page 210"
}
```


### [2026-09-06T15:11:20.822Z] TOOL RESULT

```
nodes verified: 20/20
node verdicts: {'plausible': 10, 'disputed': 2, 'unverified': 1, 'confirmed': 7}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 15, 'partial': 4, 'not_checked': 6, 'not_found': 1}
books consulted: {'supports': 26, 'partial': 23, 'silent': 6, 'contradicts': 4} | by book: {'WLD': 7, 'POK': 6, 'KLN': 6, 'PHD': 5, 'BRT': 4, 'IEC': 4, 'SYN': 3, 'HUB': 3, 'BOOK': 3, 'LAT': 3, 'CHEUNG': 2, 'AHD': 2, 'KNT': 2, 'MON': 2, 'BQT': 2, 'NYB': 1, 'HRN': 1, 'ARY': 1, 'AFM': 1, 'SKT': 1}
```


## [2026-09-06T15:11:24.856Z] TOOL CALL #72: Bash

```json
{
 "command": "ls -la data/verification/sources/refs/ocr/BQT/ | tail -6; git -C /home/sfmqrb/git/rishe status --short | head -20",
 "description": "Check cached OCR and git status"
}
```


### [2026-09-06T15:11:26.929Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb   1931 Sep  4 15:02 70.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb   1606 Sep  4 14:54 72.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb 669351 Sep  5 01:38 733.png
-rw-rw-r--  1 sfmqrb sfmqrb   1152 Sep  5 01:39 733.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb 624515 Sep  5 16:20 902.png
-rw-rw-r--  1 sfmqrb sfmqrb   1658 Sep  5 16:20 902.vision.txt
```


## [2026-09-06T15:11:29.572Z] TOOL CALL #73: Bash

```json
{
 "command": "ls data/verification/sources/refs/ocr/BQT/ | grep -E \"^(1807|1832)\" ; git status --short | head",
 "description": "Check BQT cache for 1807/1832"
}
```


### [2026-09-06T15:11:29.647Z] TOOL RESULT

```
1807.png
1807.txt
1832.png
1832.txt
```


## [2026-09-06T15:11:49.263Z] AGENT

Verification of PDF page 210 (book p. 180) complete. `verify_check.py 210` reports 20/20 nodes, **0 PROBLEM lines**.

**File:** `/home/sfmqrb/git/rishe/data/verification/page-210.json`

**Counts** — root: 1 confirmed. Nodes: 7 confirmed, 10 plausible, 2 disputed, 1 unverified (the empty box). Ref checks: 15 supports, 4 partial, 1 not_found, 6 not_checked (all MON — no page-mapped copy). 20 books consulted across nodes.

**Disputed:**
- `#5 پیاله piyāleh` — Kent p.199 does carry "NPers. piyāla … from *pati-gāra-", but that is Herzfeld's, and Kent pairs it with Skt. *galati* 'pours', not with *gar-* 'swallow'. Hübschmann lists piyāla among Greek loans ("= gr. φιάλη"); MP is *paygāl*, and OIr. *-r-* would not give MP *-l*. Note: Wiktionary's "Avestan patigāra" bullet **cites Nourai p.180 itself** — circular, not independent support.
- `#20 English gargle` — Klein, Skeat and Etymonline all derive it from French *gargouiller* < imitative *garg-*, not from Latin *gurges/gurguliō*; AHD lists GARGET/GORGE/GORGET/GURGITATION under *gurges*, and gargle is absent from the whole gʷerə-4 article.

**Other findings worth flagging (marked plausible, not disputed):**
- `#1 jaraiti` — Cheung, EDIV p.104: "YAv. *jar- 'to swallow' … as cited by Bartholomae, AIW: 512, **does not exist**" (Jamaspa–Humbach 1971). Nourai inherits the ghost form from Pokorny/Walde-Pokorny.
- `#3 گلو` — Horn 928 / Pokorny 474 / BQT:1832 all support Nourai's chain, but the *l* points to the parallel root *gʷel-* (Lat. *gula*, Skt. *gala-*); AHD files *gula* under gʷel-3, and WLD itself hedges.
- `#4 pati-gâra` labelled "Avestan" — unattested in Bartholomae; Kent writes it starred (*Old Iranian*). `#6 gar` labelled "Old Persian" — no such lemma in Kent; only *batugara-*, and Kent calls the verb Avestan. `#8 grîvâ-pân` labelled Avestan — attested only as MP *grīwbān* (MacKenzie p.37; Moʿin's own BQT:1807 footnote says so).

**Strong confirmations:** HRN:207 (`garūk`/`gulū`), SYN:233 (Buck: "NPers. *gariva* 'hill'" from Av. *grīvā-*), BQT:1807 and BQT:1832 (Moʿin's footnotes, fetched as pdf pp. 602 and 629 of BQT vol. 3), IEC:265 and IEC:305 (both page numbers exact).

**Extraction errors:** none. Read `site/pages/210.jpg`; the JSON matches the printed page in every cell, including the genuinely blank box (#7) under Old Persian *gar*. Seven web pages archived via `fetch_source.py`.
