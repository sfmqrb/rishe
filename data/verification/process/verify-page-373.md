# Verification process log — verify-page-373


## [2026-09-07T20:16:15.853Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 373 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-373.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-373.json. Write /home/sfmqrb/git/rishe/data/verification/page-373.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 373` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T20:16:17.638Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T20:16:18.211Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T20:16:18.223Z] TOOL RESULT

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


## [2026-09-07T20:16:19.161Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-373.txt"
}
```


### [2026-09-07T20:16:19.185Z] TOOL RESULT

```
1	=== PDF page 373 (book page 343) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ôku : swift  (refs POK:775)
4	#1 (parent #0) [Avestan] refs=POK:775 | âsu : swift ; âsya : faster ; âs-išto : fastest ☞Isto
5	  #2 (parent #1) [Pahlavi] refs=BQT:71; SOD:10 | âhŭk 1, âhŭg : a fast running animal, deer
6	    #3 (parent #2) [Persian] refs=MON:109 | âhŭ 1 «آهو ۱» : deer
7	  #4 (parent #1) [Sogdian] refs=SOD:10 | âs`wk` : deer, gazelle
8	#5 (parent #0) [Avestan / Old Persian] refs=BRT:458 | karši-ptan : swift flying ☞Pet 1 | NOTE: Compare with Latin "acu-pedius"
9	  #6 (parent #5) [Pahlavi] refs=HRN:191 | karšift : a fast bird
10	    #7 (parent #6) [Persian] refs=BQT:1652; MON:2988; HRN:191 | kašak «کَشَک» : a bird, magpie | extra: کَسَک ، کَشَکَک
11	#8 (parent #0) [Latin] refs=AHD; POK:775,826 | acu : swift ; acu-pedius, acci-piter : fast flying (bird), falcon ☞Pet 1
12	  #9 (parent #8) [English] refs=AHD:9 | accipiter : a hawk
13	#10 (parent #0) [Greek] refs=FSD:1707? | ôkys : swift
14	  #11 (parent #10) [Greek] refs=FSD:1707; TAD:5 | ôkeanos : swift, ocean | NOTE: KNT:164 derives this word from Greek "Keanos:lying, siting". See Root "Keanos".
15	    #12 (parent #11) [Arabic] refs=TAD:5 | oqyânŭs : ocean
16	      #13 (parent #12) [Persian] refs=MON:327 | oqyânŭs «اقیانوس» : ocean
17	    #14 (parent #11) [Latin] refs=AHD:909 | ôceanus : ocean
18	      #15 (parent #14) [English] refs=AHD | ocean
19	--- entry 1 ---
20	ROOT [Indo-European] Okw : eye, to see  (refs POK:775)
21	#1 (parent #0) [Avestan] refs=POK:775 | aši, axši : eyes ; aiwi-axši : to oversee ☞Ambhi
22	  #2 (parent #1) [Pahlavi] refs=None | ni-aš, niš : to watch
23	    #3 (parent #2) [Persian] refs=BQT:2143 | nešân «نشان» : a mark, sign, medallion
24	#4 (parent #0) [Germanic] refs=AHD:1467 | augôn : eye ; vind-auga : wind eye (opening) ☞Wě 1
25	  #5 (parent #4) [English] refs=None | eye ; window
26	#6 (parent #0) [Greek] refs=AHD | opsis : sight
27	  #7 (parent #6) [English] refs=AHD | optic, autopsy, synopsis
28	--- entry 2 ---
29	ROOT Ol 1 -> redirect to Al 1
30	--- entry 3 ---
31	ROOT Ol 2 -> redirect to Ul
32	--- entry 4 ---
33	ROOT Olěna -> redirect to El 3
34	
```


## [2026-09-07T20:16:23.506Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-373.json",
 "description": "Read source JSON page 373"
}
```


### [2026-09-07T20:16:23.542Z] TOOL RESULT

```
{
  "pdf_page": 373,
  "book_page": 343,
  "entries": [
    {
      "root": {
        "name": "Ôku",
        "lang": "Indo-European",
        "refs": "POK:775",
        "gloss": "swift"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:775",
          "words": [
            {"translit": "âsu", "gloss": "swift", "script": null},
            {"translit": "âsya", "gloss": "faster", "script": null},
            {"translit": "âs-išto", "gloss": "fastest", "script": null, "see": ["Isto"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:71; SOD:10",
          "words": [
            {"translit": "âhŭk 1, âhŭg", "gloss": "a fast running animal, deer", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:109",
          "words": [
            {"translit": "âhŭ 1", "gloss": "deer", "script": "آهو ۱"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "SOD:10",
          "words": [
            {"translit": "âs`wk`", "gloss": "deer, gazelle", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "BRT:458",
          "words": [
            {"translit": "karši-ptan", "gloss": "swift flying", "script": null, "see": ["Pet 1"]}
          ],
          "note": "Compare with Latin \"acu-pedius\"",
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Pahlavi",
          "refs": "HRN:191",
          "words": [
            {"translit": "karšift", "gloss": "a fast bird", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "BQT:1652; MON:2988; HRN:191",
          "words": [
            {"translit": "kašak", "gloss": "a bird, magpie", "script": "کَشَک"}
          ],
          "script_extra": "کَسَک ، کَشَکَک",
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD; POK:775,826",
          "words": [
            {"translit": "acu", "gloss": "swift", "script": null},
            {"translit": "acu-pedius, acci-piter", "gloss": "fast flying (bird), falcon", "script": null, "see": ["Pet 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": "AHD:9",
          "words": [
            {"translit": "accipiter", "gloss": "a hawk", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Greek",
          "refs": "FSD:1707?",
          "words": [
            {"translit": "ôkys", "gloss": "swift", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Greek",
          "refs": "FSD:1707; TAD:5",
          "words": [
            {"translit": "ôkeanos", "gloss": "swift, ocean", "script": null}
          ],
          "note": "KNT:164 derives this word from Greek \"Keanos:lying, siting\". See Root \"Keanos\".",
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "Arabic",
          "refs": "TAD:5",
          "words": [
            {"translit": "oqyânŭs", "gloss": "ocean", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "Persian",
          "refs": "MON:327",
          "words": [
            {"translit": "oqyânŭs", "gloss": "ocean", "script": "اقیانوس"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 11,
          "lang": "Latin",
          "refs": "AHD:909",
          "words": [
            {"translit": "ôceanus", "gloss": "ocean", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "ocean", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Okw",
        "lang": "Indo-European",
        "refs": "POK:775",
        "gloss": "eye, to see"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:775",
          "words": [
            {"translit": "aši, axši", "gloss": "eyes", "script": null},
            {"translit": "aiwi-axši", "gloss": "to oversee", "script": null, "see": ["Ambhi"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": null,
          "words": [
            {"translit": "ni-aš, niš", "gloss": "to watch", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:2143",
          "words": [
            {"translit": "nešân", "gloss": "a mark, sign, medallion", "script": "نشان"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD:1467",
          "words": [
            {"translit": "augôn", "gloss": "eye", "script": null},
            {"translit": "vind-auga", "gloss": "wind eye (opening)", "script": null, "see": ["Wě 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "eye", "gloss": null, "script": null},
            {"translit": "window", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "opsis", "gloss": "sight", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "optic, autopsy, synopsis", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Ol 1",
        "redirect": "Al 1"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Ol 2",
        "redirect": "Ul"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Olěna",
        "redirect": "El 3"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-07T20:16:23.907Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-07T20:16:23.943Z] TOOL RESULT

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


## [2026-09-07T20:16:30.131Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','BQT','SOD','MON','BRT','HRN','AHD','FSD','TAD','KNT','WLD','IEC','SYN','KLN','PHD','NYB','HUB','ARY','ISS','SKT','LKT','AFM','PLA','FVQ']:\n    v=d.get(k)\n    print('==',k, json.dumps(v,ensure_ascii=False)[:700])\n\""
}
```


## [2026-09-07T20:16:30.557Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && ls data/verification/page-37*.json 2>/dev/null"
}
```


### [2026-09-07T20:16:31.426Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
== SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get s
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
== FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt", "page_offset": "vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: le
== TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pag
== KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archiv
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' nu
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
== ISS {"title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967", "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute", "kind": "google_books_preview+archive_restricted", "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317936 (v.6, search-only) ; archive.org khotanesetexts0103bail (vols I-III only, lending)", "identifier": "dictionary-of-khotan-saka (substitute); khotanesetexts0103bail is vols I-III, lending-only", "local_file": null, "page_offset": "DKS: leaf = printed + 17..19 (e.g. leaf 158 = p.139). local file ha
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages.
== AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"], "page_offset": "19
== PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).", "loo
== FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"], "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt;
```


### [2026-09-07T20:16:31.467Z] TOOL RESULT

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
---
data/verification/page-37.json
```


## [2026-09-07T20:17:33.165Z] AGENT

Now let me start checking the local reference library. First Pokorny 775 for both roots.


## [2026-09-07T20:17:34.482Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 9 10 11 12 13 14; do echo \"=== POK_03 leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' POK_03.txt | head -60; done 2>/dev/null | head -200"
}
```


### [2026-09-07T20:17:35.730Z] TOOL RESULT

```
=== POK_03 leaf 9 ===
achten,  aisl. ätla  {*ahtilön)  ,meinen,  denken,  beabsichtigen'.
WP.  I  169;  nach  Specht  KZ  62,  211  zu  ok^-.
775
^^töiu)  ,acht^  ^
Ai.  astd^  astäu  (neben  aslti-  f.  , achtzig*),  av.  asta  zu  av.  asti-  , Breite von  vier  Fingern*  (zum  Sg.  *as^a-),  Henning  TrPhSoc.  1948,  69;  arm.  ut' /wahrscheinlich  aus  ^oftö  mit  von  der  Sieben  übernommenem  _p) ;  gr. d%r(ii ;  alb.  tete  (*oktö-t-) ;  vgl.  maked.  Otto-lohus  ,8  hüglig' ;  lat.  octö ;  air.  ocht 71- (Nasalwirkung  nach  secÄ^  n- und  nöi  n-);  cjmr.  icyth,  ncorn.  eathy  bret. eiz  (*ochtlj  älter  -ü  aus  -ö) ;  got.  ahtau^  aisl.  ätta^  ahd.  as.  alito,  ags.  eahta- lit.  astuo-ni]  aksl.  osmb  (nach  dem  Ordinale  osmi,  umgebildet);  toch.  B  okt, -V  okät.
Ordinale:  lat.  odävus  (vgl.  auch  osk.  Uhtavis  ,Oktavius*)  wohl  aus *oc^öM05;  aphryg.  OTvfoc  J^stsl  ,im  8.  Jahre*  (*oktöuoi  uetesi)\  gr.  ion.  att. l)ydo(f)og  {d  nach  eßdojxog),  verbaut  in  dyöoi]y,ovTa  (hom.  zu  dyddtxovxa umgebildet  nach  dxrw),  vgl.  lat.  octuägintä  ,80',  das  einstige  Vorbild von  septuäginta  und  in  sehr  später  Zeit  nach  letzterem  wieder  neu  auf- gekommen; nach  dem  Ordinale  zu  se^^^m  (und  dekm)  gerichtet  haben  sich ai.  astamd-^  av.  aHdma-^  gall.  oxtumetos,  air.  ochtmadj  cymr.  icythfed,  lit. äsmaSj  apr.  asman  (Akk.),  aksl.  osTm  (oktmo-)]  vgl.  toch.  A  oktänt,  B  ok- tante  ,der  achte'.
An  anderen  Übereinstimmungen  sind  zu  nennen  ved.  astäda^a-  18,  av. aHadase-  ,der  18.',  gr.  (3xt"w (xa/)  (5sxa,  lat.  octödecim,  ahd.  ahtozehan  18; gr.  (5xTax(5ö'tof,  lat.  octingenti  ^800^
WP.  I  172  f.,  WH.  II  199  f.,  Trautmann  15  f.
ökü-s  , schnell',  Kompar.  okiös,  Superl.  ökisto-.
Ai.  äsü-  ,schnell',  Kompar.  äälyän,  Superl.  äsistha-,  av.  äsu-  , schnell*, Kompar.  äsyä,  Superl.  äsistö-,  gr.  wxvg,  öjy.Latog,  poet.  wxvraTog,  lat.  öcio7' , schneller',  Superl.  öcissimus  (Positiv  fehlt),  acymr.  di-auc,  ncymr.  di-og^ corn.  di-oc^  bret.  di-ec  , träge',  eigentlich  ,unschnell';
vielleicht  im  Ablaut  zu  ak-y.ok-  , scharf  (oben  S.  18 f.);  dann  könnten lat.  acu-pedius  , schnellfüßig'  und  accipiter  , Habicht,  Falke*  (oben  S.  19) auch  hierher  gehören;
ein  verwandtes  *ök-ro-  (vgl.  zum  Formans  *ak-ro-  neben  *ak-u-)  ist vielleicht  die  Grundlage  von  ksl.  jastrehh  , Habicht*.
WP.  I  172,  WH.  II  198.
ok'i-    jsehen*;    ok^-,    ok\U-j    ok"(e)n-    (dieser    St.  in    den    Kasus    obliqui), oki^(e)s-,  ok^-p-  ,Auge*;  daneben  ok-y  s.  dort. Arisch   außerhalb   der  Komposita  nur  Formen  vom  St.  *ok}ip-  (worauf z.  T.  der  i-  und  n-St.  geschichtet  ist):
=== POK_03 leaf 10 ===

Ai.  dksi  n.  ,Auge*  (dieser  i-St.  ved.  nur  Nom.  Akk.  Sg.  und  in  Kom- positis,   ak§i-pdt   ,ein   wenig*,   nachved.    auch    in    den    ÖÄ-Kasus    und    im
Lok.  PL),  Gen.  Sg.  aks-n-dh  usw.,  Nom.  Du.  aksi  =  av.  ah  ,die  (beiden)  "^^ Augen'  (vgl.  *ofö-  ds.  in  lit.  aH,  abg.  o<fz  und  als  Grundlage  von  arm.  ac-i^  _ und  gi\  liaas),  Bildung  vom  kons.  St.  *aks-]  dieser  St.  ahs-  auch  in  ved.  an-"(ijb  r ,blind';   av.  rtsi   für  *axn  nach  wsi  ,Ohren',   vgl.  av.  aiwy-äxsayeinti  ,sie beaufsichtigen',  aiwyäxstar-  , Aufseher' ;  redupl.  ai.  iJcsate  ,sieht'  (idg.  *iiu, aus  *i-oÄ;^);  aksd-   m.  , Würfel',   d.  i.   ,mit  Augen  versehen';  ksana-  m.  n. , Augenblick'   (scheint  aus  einem   Lok.   *[a]ksdn  erwachsen);    nicht   über- gewuchert ist  der  /)-St.  in  die  verdunkelten  Komposita  ai.  prdtika-  ,zuge- wandt,   entgegengesetzt',  n.  , Antlitz'  (:  nQoa-tjnov),   dnlka-   n.  ,das  Zuge- kehrte, Vorderseite',  av.  ainlka-  m.  ,Antlitz'  (*proti,  '^eni  +  ^fc"- ;  vgl.  slav. nich  unter  *m-  ,nieder'),  ghrtäcl  f.  ,fettig  (aussehend) ;    Opferlöffel',  svitid f.  ,glänzend';
arm.  (mit  expressiver  Geminata)  akn,  Gen.  akan  ,Auge,  Öffnung,  Loch' (7i-St.),  Nom.  PL  ac-k  pluralisiert  aus  dem  Nom.  Du.  *oh^i;
gr.  öWfi  Nom.  Du.  , Augen'  (*ok^ie  für  *ote),  att.  *5V2r£,  wovon  TQLOTzig^ jHalsschmuck  mit  drei  gläsernen  Augen';  HoGoi-iaL  ,sehe  (geistig),  ahne', att.  ÖTTsvofiaL  ,ahne,  fürchte';  oipo(j,aL  ,ich  werde  sehen',  hjtwna  ,habe gesehen' ;  ÖTtiJtsvo)  ,gaffe  nach',  TtaQd^svoniTtrjg  ,Mädchengaffer'  mit  redupliz. Wurzel  Ö7t  (i-^07t>  Irt-) ;  h^iixa  ,Auge'  {*ä7t-(.in)j  dg)-d-al-(j,ög  , Auge'  (*ok^ph' mit  expressiver  Aspirata?);  ohne  Aspirata  böot.  oyiTaXXog]  mit  (nach ÖTtög  usw.)  analogischem  ft:  lak.  önTiXog,  epidaur.  dfTTiAAog;  ähnlich  ver- hält sich  5xxov  d(pd^alfj.6v  zu  lesb.  OTtTtccra  ^^^ixiiaxa''  (wohl  mit  expressiver Geminata);  dni]  , Lücke,  Öffnung'  (ivöftai  f.  PL  , Ohrringe'  u.  dgl.,  noXv- ü)7t6g  ,Netze  mit  vielen  Öffnungen  oder  Maschen');  dehnstufig  ^?//  , Gesicht'; TtQÖaajnov  ,  Antlitz',  ^irwrcov  , Stirn',  KvyX-o}1jj,  ßo-wrtLg  u.  dgl. ;  fiv-wrp  ,kurz- sichtig' ;  daneben  ald-oxp  u.  dgl.  mit  Kürze  (vergleichbar  lat.  atr-öx,  fer-öx) ; vielleicht  gr.  hnig  ,ehrfürchtige  Scheu;  Strafe,  Vergeltung',  eig.  ,animad- versio'?;  iipao  ,du  hast  zurechtgewiesen,  bestraft',  iv-LTtrj  ,tadelnde,  rügende Anrede',  ividacj  (geneuert  ivtTttto),  Aor.  ijvtTtanov  und  ivennov  ,tadeln, rügen,  ahnden,  tätlich  zurechtweisen'  (idg.  *lk'^-  aus  redupl.  *i-ok]^j  vgl.  ai. iksate) ;
alb.  Sil  ,Auge'  (:  lit.  akh)]
lat.  oculus  , Auge'  (ök^^elo-s) ;  atr-öx  ,gräßlich'  (zu  äter,  oben  S.  69),  fer-öx ,wild*  (zu  lat.  ferus,  oben  S.  493),  usw.  (:  gr.  (.iv-toip  ,kurzsichtig',  usw.);
air.  enech,  mcymr.  enep  ,Gesicht,  Antlitz',  mbret.  enep  ds.  und  Präp. »gegen',  und  cymr.  wyneb  ,Antlitz*,  acymr.  let-einepp  ,halbe  Seite'  sind unklar ;
im  Germ,  finden  wir  neben  dem  St.  *azw'  (*ök'A-,  ahd.  ac-siuni  f. ,species',  auc-siuno  ,ev
=== POK_03 leaf 11 ===
identer')  :  *awi.  {*ok^i-)  in  ahd.  atci-zoraht  ,augen- scheinlich',  ags.  eawis  {*eaw-wis)  ,offenbar',  eawan  ,zeigen,  offenbaren', afries.  aiüia,  auwia  ds.  (*awjan\  mhd.  z-ounen,  mndl.  t-önen  ,zeigen'   (mit
r
777
verkürztem  Präfix);  daneben  germ.  *awn- (*oÄ:"-en-);  durch  Ausgleich  und "Einfluß  von  *ausö  ,Ohr'  entstand  ein  St.  *au^an- :  krimgot.  PL  oeghene (gß  =  ö),  dann  got.  augöy  aisl.  auga^  ahd.  ouga,  ags.  eage  n.  ,Auge' ;  St. *auqj(^-  ir^  S^^'  and-augi  n.  , Antlitz*,  ags.  and-eages,  amd.  and-ouge  , ange- sichts', aisl.  -eygr,  ahd.  -ougi,  ags.  -eaged  ,-äugig* ;
lit.  akls  ,Auge*,  aki  (=  abg.  061)  ,die  beiden  Augen*,  lett.  acs  ,AugeS apr.  ackis  Nom.  PL  , Augen',  abg.  oko  (russ.  öko),  Gen.  o^ese,  Du.  oci* Auo-e';  lit.  akylas  ,auf merksam',  poln.  oJac^^/c  (dehnstufig)  ^sehen,  bemerken, erblicken',  woraus  durch  Suffixverkennung  {ol  :  0):  6 a c2?/c  , achtgeben,  auf- passen, wahrnehmen,  sehen*;  vom  n-St.  serb.-ksl.  okno  , Fenster';  vgl.  engl, (aisl.  Lw.)  wind-ow  ds.,  eig.  ,Windauge';
Zugehörigkeit  von  lit.  äkas  ,Wuhne,  Loch  im  Eise*,  lett.  aka  ,gegra- bener  Brunnen*,  russ.  Flußname  Oka  (anders  oben  S.  23),  lit.  eketl  (aketl, aJcyte)  ,in  das  Eis  gehauenes  Loch  zum  Wasserschöpfen,  Wuhne*,  lett.  akate mit  Wasser  gefüllte  Grube  im  Morast*  wahrscheinlich :  ,Wasserauge*,  vgl. , Meeraugen*  als  Bezeichnung  der  Tatraseen;
toch.  A  aÄ,  Du.  aääm,  B  ek,  Du.  esane  n.  ,Auge';  A  ak-mal  , Gesicht* (,Auge  +  Nase');  vgl.  W.  Schulze  KL  Sehr.  248.
WP.  I  169  ff.,  WH.  II  200 ff.,  Benveniste  Origines  1,  48,  Schwyzer  Gr. Gr.  1,  299,  Petersson  Heterokl.  121.
ol-{e)-  jVernichten*.
Gr.  ^Xlviii  {*dX-vv'-iii)^  Fut.  öleGu)  ,verderbe',  dleTrjq  ,Vernichter*,  öXi-/.(x) ^vernichte*,  öloög  {^dXofög)  »verhängnisvoll* ;
lat.  ab-oleö  , vernichte*;  vielleicht  mit  sek.  Ji-  umbr.  honduj  holtu  ,pros- ternito* ;
hitt.  hulläi-,  hulliya-  ,hekämpfen',  usw.
WH.  I  4  f.  (der  die  Zusammenstellung  bestreitet),  Couvreur  H  143.
0D2-,  reduktionsstufig  o^-  ,roh,  bitter*;  oin-ro-s,  ömo-s  ds. ;  o-ß^-ed-  ^rohes Fleisch  essend'.
Ai.  amld-,  amhld-  , sauer,  Sauerklee*  (=  maked.  aßgo-,  germ.  *ampra-)y dehnst,  amrd-  m.  ,Mangobaum*,  ämd-  ,roh,  unreif  (=  gr.  (b^ög),  ämäd- , rohes Fleisch  essend';  skjth.  VN  l^i.iddo'/.oi  aus  iran.  ^amäd-aka-  ,Rohfleischesser' ;
arm.  dehnst,  lium  ,roh,  grausam*;
maked.  dß^o-  , zusammenziehend*,  dßagv '  dqiyavov  Hes. ;
gr.  (h^og  ,roh,  grausam*,  (hfxrjaTTjg  , rohes  Fleisch  fressend*  usw.  (=  ai. ämäd-  mit  schon  idg.  Kont
=== POK_03 leaf 12 ===
raktion  von  ömo-  und  ed-  , essen');
alb.  tamle  ,(saure)  Milch',  amhele,  emble  ,süß',  tUmhl'e  , Galle'  (Artikel  ^);
lat.  amärus  ,bitter' ;  air.  om  ,roh',  cymr.  o/ds.,  dazu  air.  um{a)e  ,Kupfer, Erz'  =  cymr.  efydd  ,Kupfer,  Bronze'  (*omiio-) ;
778
germ.    *ampra-   (aus    *ambra  <  ''am-ro-)   in    ndl.    amper   ,scharf,    bitter, unreifS  aisl.  apr   (*ampraR)   ,scharf',    Subst.   ags.   ampre,    ahd.    ampfaro  t^l ,(Sauer)ampfer*;  unsicher  ags.  öm  m.  ,RostS  öme  f.  ,RotlaufS  aisl.  ama  f., öTnw-sö^i  f.  ,Rose'  (Krankheit),   ämr  ,rotbraunS  nhd.  Ahm,  Ohm  ,Rotlauf«j
lett.  amuols  ^Sauerklee'.
WP.  I  179,  WH.  I  35,  Frisk  Nominalbildung  14.
om{e)so-s  , Schulter'.
Ai.  ämsa-  m.  ,Schulter* ;  arm.  us,  Gen.  usoy  ds.;  dehnstuf.  gr.  cä^dg  ds. aus  *ömsos,  vgl.   äiv-oii^iddLog  bei   Theokr.:    lat.    umerus   aus  *omesos   ds.,    | umbr.  uze,  onse  ,in  umero*;    got.  ams  ds.  (germ.  *amsa-\   aisl.  ass  ,Berg- rücken*;   toch.  A  es  ,Schulter'  (*omso-),  B  äntse  (*omeso-).  "
WP.  I  178,  Pedersen  Toch.  2Ö0;  W.  Schulze  KZ.  63,  28,  WH.  II  815.     -
omo-  ,energisch  vorgehen*;  daraus  ,fest  worauf  bestehen,  festmachen  =  eidlich  3; bekräftigen'  und  ,zusetzen,  quälen,  schädigen';  o^iiiä  ,Kummer^  :?^
Ai.  dmlti  , bedrängt,  versichert  eindringlich,  schwört',  themat.  sam-amanU  ^ ,sie  geloben'  (:  avv-o^iöaai\  ahhy-amiti  ,plagt,  schädigt',  dmlvä  , Drangsal,  "*- Leiden,  Krankheit'  (:  gr.  Mr]),  mit  themat.  Gestaltung  der  2.  Silbe  dmaU  4 ,bedrängt',  dmatra-  ,fest',  dmavän-  ,ungestüm,  kräftig'  ==  av.  amavant-  -^ ,kräftig,  stark,  mächtig,  gewaltig',  ai.  dma-  m.  , Andrang,  Ungestüm'  = av.  ama-  ,Kraft,  männliche  Potenz,  Angriffskraft',  Adj.  ,stark',  ai.  ämdyati jSchädigt;  ist  schadhaft,  krank',  ämaya-  m.  ,Krankheit' ;  av.  amdyavä ,Leid,  Drangsal';
gr.Huvü^tj  df-ivvo)  , schwöre'  {di-idaai,  öfx(x)(.LO'A(x]  Fut.  dfÄSitca  Neubildung), avvo(.i6aac  (:  ai.  sam-amante),  hom.  d^oitog  ,plagend,  leidvoll'  (wohl  metr. Dehnung  von  o^ioJ^ioq,  zu  *(3uo-/e);  dvia,  ion.  Mtj  ,Kummer'  (dissimil. aus  *diiLUa,  Schwyzer   Gr.  Gv.  1,  259,  309) :
aisl.  ama  ,plagen,  belästigen',  amaslc  , Anstoß  nehmen,  Unwillen  fühlen, sich  womit  abplagen',  nisl.  ami  , Plage',  amstr  , rastlose  Arbeit,  Anstrengung', aml  n.  ,unaufhörliche,  bes.  erfolglose  Beschäftigung  mit  einer  Sache',  norw. amla  ,sich  abmühen,  arbeiten,  bes.  ohne  Erfolg',  aisl.  PN  Omlungr]  Amali der  Name  des  ostgotischen  Königshauses,  die  Ämalunge,  Amulinge  der deutschen  und  ags.  Heldensage,  ahd.  Amal-olf  u.  dgl. ;  ahd.  emiz  , beständig; fortwährend',  emizzig,  emazzig  ,bestän
=== POK_03 leaf 13 ===
dig,  beharrlich',  nhd.  emsig.
toch.  A  amühähne  , Unzufriedenheit',  B  omäskem  , schlecht'.
WP.  I  178  f.
ond-f  nd-  , Stein,  Fels'?
Ai.  ddri-  ,Stein,  bes.  zum  Somaschlagen  gebrauchter ;  Fels,  Berg',  apers. Ark-adris{7)  :  mir.  ond,  onn,  Gen.  tiinde  (St.  *ondes-)  n.  ,Stein,  Fels'. WP.  I  181.
779
r.
^     q'raum*;  alter  r/12-Stamm.
j^rm.  anurj  ,Trauin'  {^onör-io-,  vgl.  gr.  T;iy,i.ia)Q  :  Te^ixag  , Zeichen*) : Xvao  Nom.  Akk.  11.  ,Trauin*  und  Adv.  ,im  Traum';  hveiQog,  -oy,  äol.  ovoiQog, kret.  ävaiQog  (wohl  durch  Einfluß  der  Präpos.  dv-)  , Traum*,  Gen.  att.  ion. ^ygiparog  (ursprüngl.  *oVarog);  all),  gegh.  dderre^  tosk.  enderre  ,Traum' (onrio-)-
\AT.  I  180,  Meillet  Esquisse  de  l'Arm.^  150.
Oß^'  (besser  ang-)  , Kohle*;  angelo-  ds.
Ai.  diigära-  m.  , Kohle*,  npers.  angist  ds. ;  gael.  nir.  aingeal  ,Licht,  Feuer* ;
balt.-sl.  *a7i^^i- :  apr.  anglis,  lit.  anglls^  lett.  uogle  , Kohle*  (lett.  iio^Ze  ist 2^eubildung) :  aksl.  Qgh  m.  ds.,  aber  russ.  ugoh,  skr.  ugalj,  poln.  w^giel ds.  usw.  (to- Stämme).
WP.  I  181,  Macbain  Etym.  Gael.  Dict.  8 f.,  Trautmann  8,  H.Wagner, Lexis  3,  134.
iong"^'-  ,salben*;  ong^-en-,  ng^.-en-  ,Salbe*.
Ai.  aüj-,  andkti  (3.  PI.  aüjänti)  ^salbt,  bestreicht,  schmückt*,  Partiz. Perf.  aktd-,  Pass.  ajydte\  anjanam  ,das  Salben,  Salbe*,  dnjas-  n.  , Salbe*, aflji-  ,salbend;  m.  n.  , Salbe,  Schmuck',  äjyam  n.  ,Opferschmalz*  (ä+ajya- <*ng^o-);
arm.  aucanem  , salbe*  (vgl.  Meillet  Esquisse  de  l'Arm.^  37);
lat.   unguöy   unctus]   umbr.   nmtu   ,unguito*;  apr.    anctan,   ancte  ,Butter*.
ong^-en-  , Salbe,  Schmiere*. Lat.  nnguen,  unguen-tum  ,Fett,  Salbe*,  umbr.  umen  ds.,  ahd.  anclio^  anco m.,  mhd.  aiike  , Butter*,  alem.-südschwäb.  Anke  (m.,  selten  f.)  ,Butter*.
ng'^^-en-  :  ir.  imh  (Gen.  imbe),  Butter*,  acorn.  amen-en^  bret.  amann,  aman- enn,    cymr.   ymen-yn    (aus   umgelautetem  *emen-yn) ;    vgl.  oben  ai.  öjyam. WP.  I  181,  Kuiper  Nasalpräs.  122.
ono-  und  022s-,  auch  {6)no-d~  ,schmähen*.
Gr.  hvoiiai  , schelte,  tadle*,  dvozög  , getadelt,  tadelnswert*,  ovoTa^w  , schelte, tadle*;  mit  -9-  der  zweiten  Silbe  hom.  djvazo  und  ovaxai'  diTiiid^sTai. fj,£l.iq)S2a
=== POK_03 leaf 14 ===
i  Hes. ;  mir.  on  , Schande*;  vielleicht  mit  Red. -St.  auch  der  ersten Silbe  mir.  anim  (i-St.)  ,Makel,  Fehler*,  acjmr.  anamou  ,mendae*,  ncjmr. anaf,  mbret.  ana^ff-  , Makel,  Fehler*.
Erweiterung  {o)no-d-  in:  av.  nac^ö^iiö  , schmähende,  lästernde*,  gr.  övoa- aaad-ai  ,tadeln'  usw.,  dvooTog  , tadelnswert'.
WP.  I  180.
780  '
onogh-  {:ongh-,  nogh-;  kelt.  ngh-),  ongh-li-  ,Nagel  an  Fingern  und^ Zehen,  Kralle',  z.  T.  mit  Formans  -u-  (erweitert  -ut-)  und  -lo-.       '_
AI.  dnghri-  f.  ,Fuß*  (vermutlich  mit  r  aus  Z,  *0Tdgh-li-)',  mit  ar.  kh  ai. naÄÄa  m.,  n.,  naJchdra-  m.  n.,  ,Nagel,  Kralle',  np.  näxun  ds.  (ar.  kh-  eine Neuerung) ;  vielleicht  .arm.  eiungn  ds.  (*e-nungn) ;
gr.  5Vv?,  -vxog  »Nagel,  Kralle*  (aus  *dvxv-?)',
lat.  wn^M-w  ,der  Nagel  an  Fingern  und  Zehen*,  ungida  ,Klaue,  Huf*, später  auch  ,Nagel'  {*ongh-{e)la)s  air.  %en  f.  Dat.  PL  ingnih,  Nom.  PI. i?i^7iea,  acymr.  eguluy  ncymr.  eM?m  f.,  corn.  euuin,  bret.  zum  (m.  geworden) ,Nagel'  {*nghu'ma);  ahd.  wa^^aZ,  ags.  ncegel  ,NagelS  aisl.  nagl  ds.  (kons. St.  geworden,  PI.  negl) ;  negl  vielleicht  ursprüngl.  Sg.  i-St.,  vgl.  ai.  ängkri-^ und  zum  PI.  umgedeutet,  woran  sich  die  weitere  kons.  Dekl.  angliederte), got.  ga-nagljan  ,annageln';  lit.  nägas  m.  ,Nagel  an  Fingern  und  Zehen; Klaue  bei  Raubvögeln',  lett.  nags  ds.;  lit.  nagä  ,Huf',  apr.  nage  ,Fuß», abg.  noga,  russ.  nogd  ,Fuß'  (kollektive  ä-Bildung);  lit.  nagütls,  apr. nagutis  »Fingernagel',  abg.  nog^th,  russ.  nögoth  »Nagel,  Kralle';   '
nach  Specht  zu  gr.  ä/xog  (oben  S.  46),  also  Wurzel  on-.
WP.  I  180  f.,  Trautmann  192,  Specht  Idg.  Dekl.  253 1.
I.  op-  ,arbeiten,  zustande  bringen;  Ertrag  der  Arbeit,  Reichtum';  op-os- ;, Werk^
Ai.  d'pas-  n.  ,Werk'  (=  lat.  o'pus)^  '  av.  hv-apah-  ,gutes  Werk  (ver- richtend)' ;  dpas-  n.  , Werk,  religiöse  Handlung' ;  dpnas-  n.  jErtrag^  Habe, Besitz',  av.  afnah-vant-  , reich  an  Besitz' ;
gr.  Hf^rtvr]  f.  ^Nahrung,  Brotfrucht^,  bjj.TcvLog  ,nährend^;
lat.  opuSj  -eris  , Arbeit,  Beschäftigung,  Handlung,  Werk',  opus  est  ,es ist  nötig'  (,*ist  Mußarbeit'),  wovon  operö^  -art  , arbeiten',  osk.  üpsannam ,operandam',  upsatuh  sent  (,facti  sunt'),  Perf.  upsed  ,fecit',  uupsens  ,fecerunt', (dehnstufiges  Perf.  wie  in  lat.  öcZi),  umbr.  osatu  ,facitö',  pälign.  upsaseter jfieret';  lat.  ops,  opis  ,Vermögen,  Reichtum,  Macht ;  Hilfe,  Beistand',  bei Ennius  auch  , Bemühung,  Dienst',  officium  , Pflicht'  <  *opi-ßcium  , Arbeits- verrichtung', Ops  , Göttin  des  Erntesegens',  inops,  cöpia  (*co-opia)^  opu- lentus  , reich  an  Vermögen,  mächtig',  wohl  auch  optimus  ,der  Beste'  (eig. ,der  Wohlhabendste');  vielleicht  der  Name  der  Osct^  Opscl,  ""Otcl^oI  als ,die  Verehrer  der  Ops'  und  lat.  omnis  ,all,  ganz,  jeder'  (*op-n2-s);  viel- leicht air.  somme  ,reich',  domme  ,arm'  (sw-,  dus-op-smio-)  ]
ags.  efnan^  aisl.  efna  , wirken,  tun';  dehnstufig  ahd.  uoho  , Landbauer
```


## [2026-09-07T20:17:35.990Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"ōk̑ú\\|ok̑ú\\|ōku-s\\|ōk̑u\" POK_full.txt | head -20; echo \"--- okw eye\"; grep -n \"ok̑w\\|okʷ-\\|ok\\^w\" POK_full.txt | head -20"
}
```


### [2026-09-07T20:17:36.074Z] TOOL RESULT

```
--- okw eye
```


## [2026-09-07T20:18:01.285Z] AGENT

POK 775 confirms both roots directly. Now the Iranian nodes.


## [2026-09-07T20:18:03.749Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT karsipt ===\"; grep -n \"kar[sš]ipt\\|karšipt\\|kar\\^sipt\" BRT.txt | head -20; echo \"=== BRT leaf for col 458 ===\"; grep -n \"^ *458\\| 458 \" BRT.txt | head"
}
```


### [2026-09-07T20:18:03.822Z] TOOL RESULT

```
=== BRT karsipt ===
=== BRT leaf for col 458 ===
17664:*)  Als  Ralav  der  Vögel  {iiäyaHdakän,  mumän) wird  Bd.  34.  1 1  und  Vr.  /.  i  Pü.  der  Vogel KatUpt  (zn  Bd.  3^  11 :  karUpt  kc  larx  :fännid-, Sp.  458  m.),  aber  Bd.  34-  ag  der  Vogel  Camri! genannt;  s.  noch  Mx.  6z.  9  und  WCST  SBE. 24.   lOg.
```


## [2026-09-07T20:18:05.343Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HRN karsift/kasak ===\"; grep -n -i \"karšift\\|karsift\\|kašak\\|kasak\\|kāsak\" HRN.txt | head -20; echo \"=== HRN ahu ===\"; grep -n -i \"āhū\\|ahu \" HRN.txt | head -20"
}
```


### [2026-09-07T20:18:05.409Z] TOOL RESULT

```
=== HRN karsift/kasak ===
=== HRN ahu ===
```


## [2026-09-07T20:18:16.815Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor i,p in enumerate(t):\n    if '457' in p or '458' in p or '459' in p:\n        print('leaf',i, [l for l in p.split('\\n') if '457' in l or '458' in l or '459' in l][:4])\nEOF"
}
```


### [2026-09-07T20:18:18.232Z] TOOL RESULT

```
1041
leaf 90 ['heiligen  Texte)  nicht  obliegt,  (dass  er)  die G.  nicht  aufsagt"  V.iS.g\'K Aus  ar.  *ai*jäsä-  (oder  auch  \'asä-,   %  36S,  3, igS.\']\'}),  »om  V. \'a^-,  —  Pü.:  anvyähan  ahoyä- haninii;  s.  No,  2.  —  O  Vgl.  N.  II.  —  ")  Vgl. iSl  —   gegenüber  Pö.  und  Haug  SBayrAW. 1868.  2. 25,  DsT.  ZA.  2. 243 —Cld.  KZ.  jj.  459. j.  aiwyinli  N.  pj;  lies  amiySahayäiili. j.  aäoyslqm  N.  p5:  lies  aiuiyäsl°.']
leaf 171 ['Vgl.  asaväiah-,  —  PO, ;  ahrirv  zSyak  (weil  miui aiava-z5  teilte,  Hbm.  ZDMG.  26.  458>']
leaf 228 ['3iy.  h pa  var^iärTk  äyit . .,  (lu  Y.  5^] :  ,/»  mtto),  WO  Männer  kämpfen"  Yt.jj.27; rämiimk  5  ösän  vis  a/rbüm  ie..\').  — \')  Durch  \'  —  abdaca  (sd.)  "\'.a  sadayät  yat  mh..  V.  2. Aitrakiion;  s.  zu  anuxße.  —  »)  Also  Ä  wj«  1  24.  2)  \'ebenso,  gleicher  Weise\',  in lüTiuX    S.  SP.  Komm.  2.  459.  ^  elliptischen    Sätzen \'>;    nSit   zX  im    -Ji    s\'ä']
leaf 276 ['457']
leaf 277 ['459  karätayaeffl  —  kasyah-  460']
leaf 357 ["KompE.  —  Zur  ä-'Erweiterung'  des  V.  'gay-; ^E'-  et-  Wv  mit  Hbm.  AGr.  /.  459  0.  —  Vgl. Jyälav;  —  I)  Gmi  abweichend  Hibt  Ab- iaul  113."]
leaf 400 ["KompA-  ~  ai.  dSrgkä-  Adj. ;  mp.J),  ooss.  iiiiry ; np.  -vgl.  der<).  —  Vgl.  dräjäk:  —  Pü.:  dtr, (in  V.  63.  3):  dra$tg%\\  (lu  F.  I.  St.  imd  als Bciw.  von  u/H^anä-):  dai~j.  —  0  Vgl  DbB. VglS.  7.  459.  —  '>  Wo  'i>m  in  Erinnening an  Y.  9.  33   fOr   ein   andres  Wort  eingesetzt"]
leaf 441 ["—  '>  S  3:?  !■  —  3)  S  5i  IL  —  <)  In  Pü.  wird der  Aw.  Text  anders  zerlegt;  s.  die  Note der  NA.  und  SEE.  37.  457.  31.  —  S)  Falsch Sp.  301   m.,  wo  der  Absati  ß  zu  streichen."]
leaf 483 ['s.  dazu  Sf.  Komm.  /- 459-   Vgl.  noch  No.  i.']
leaf 552 ['*)  Als  Ralav  der  Vögel  {iiäyaHdakän,  mumän) wird  Bd.  34.  1 1  und  Vr.  /.  i  Pü.  der  Vogel KatUpt  (zn  Bd.  3^  11 :  karUpt  kc  larx  :fännid-, Sp.  458  m.),  aber  Bd.  34-  ag  der  Vogel  Camri! genannt;  s.  noch  Mx.  6z.  9  und  WCST  SBE. 24.   lOg.']
leaf 798 ['1457', "'   'v'Säi  ^     1458"]
leaf 799 ['1459']
leaf 825 ['dain  Sp.  Komm.  2. 17,  DsT.  2A.  /-457-']
leaf 943 ['Ableit.  aus  httoma-;  vgL  iBild.  >i.  ürnayäv-, bkmayäv-  usw.,  Wh.  Gr.»  S  it^Si.  —  Pü.: pa  hSm  u  giil  u  iarsm,  Npü. ;  ia  hüm  ujiväm H  barium.  —  OS.  zBed.  Cld,  KZ.  30.  459. 31.  273.  —  >)  Bthl.  IF.  10.  loa.']
leaf 982 ['•  g.  hSn-k«r»tay-,  j.  ban-k-  f:  s.  unter | aa^äm . .  V.Ä44;  458:  (oft);  ~  yasca  k- hanktntay.  _,  väHm  paiü  zamis  «wÄa/ (nämL  j/J)  nsit']
```


## [2026-09-07T20:18:22.725Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (276,277):\n    print('==== leaf',i)\n    print(t[i][:3500])\nEOF"
}
```


### [2026-09-07T20:18:24.112Z] TOOL RESULT

```
==== leaf 276
  awon^      des i  yazaläH  karr  u  kör,  woiu  die  np.  Erl. ;  kar  u   K.,  Sohns  des   Zb.  .  ."  Yt.  IJ.  1 06. kür  an  bUaitJ  ka  jimäit  i  hurmazd  didart  u  '      Abieil.   —   Et.?    Aus  ar.  ^karlsna-.     Vgl.  ai. suxun  hmidan  na  laväiiand'),    Sü.   (in  umge- 1      kftsnd-  Adj.  'ganz'?
Itehrter  Reihenfolge):  adari^ä  airotäraJca.^^  ,  ^^  karsnayana-  patr.   Adj.  'von  Karsna
')  S.  noch  BARTHfiLEMV  Gab.  57.  ■'  ,    <  .1     n  1      -  ,  ^    t
Stammend,  dessen  Nachkomme  :  vträspahe
•  g.  *karapo.tat-    f.    'die    Karapatt(sA.)-\  {^±)  '.„ahe  Yt. /^.  108;  loS'.
Schaft':  anäW  a  vlJDnäsä  ya  'ias^ä  (NS.)'*|      Ableit.  aus  karma-  EN.    Auffällige  Bildung.
kmtsscä     aväil    am  y}„g  ..    "deshalb  L    ■     «tarl-   V.  'trahere',   nur   mit  Praev.
ist  die  Karapan-  und  Ä^z-a^schaft   dem  p^^^s.  2  karAa-,  24  kar^aya-.
Untergang  verfallen   durch   die   (gerade),       ^^^    „^^    .(„,[(    si^h)    fortschleppen': D^  ^- 1       i'-^j'^'  ,.    r.       .  \dafva..vain3mnfm*apa.kttrsayml^ixA.y'^
jatms  haca  ma/yäkaiioyo     vor  aller  Augen
■e  karp  hrnd.  —   '>  iF.  s.  S  393-
•  j.  kahrpuna-  m.  Name  eines  a'aft'ischen  j  schleppten  sie  die  Weiber  den  Menschen Tiers'*:  baivan  alinam  spakanqm  •■nanqmX-^^^'  Yt. /g.  80".
ava.janyai  "zehntausend  Hundsschlangen,       ^jit   ava   '(mit  sich)   herabtühren,   an- (nämlich)  K. .  ."  V.14.  5.  schwemmen':  ana  tä  vaiötm  (sd.)  ayä  . .
Pü.:  transskt.  (karpun^) ^\t  der  Erl. :  «är  ,' I  ^^^-^  ^^.^^,^  „^^„,„  ava.kar»smü  späfum tanakll],    dazu  noch:    sakihii  t  tu  afiji:  o  kuti,'  „        ,  ,     -  ».   ,        j
nülnii  "handisch,  weil  er  sich  rückwärts  auf  ^'^  ■  ■  ■  •  d»™  l«im  Vierten  Mal  Schwem- den  Hintern  setzt",  —  »    DsT.s  Zusammen-'  men  sie  einen  Leichnam  an  ,  ."  V.5.  5.
Stellung  des  Worts  mit  np.£-«ria 'Katie' (ZA.  1  tti.  kdrsati,  np.  kasiJaii,  arm.  LW.  Haritl;  s. 3.  211)  ist  falsch;  das  wäre  Aw.  'gthrpa'  dam  Hbm.  KZ.  36.  166.  —  Pü. :  kaitlan.  — oder  *gir>pa'.  'I  Hds.  aparat';  »orher  gehl /ura,  mit  dem
.     „  ,_,    ,  ,      .     ,  die  Abschreiber   apa   lu   apata   ausgeglichen
•  j.    'karana-  m.    Ohr',   uzw.  rfnÄ^ischer       haben;  vgl.  Yt.  ,0.  125.-»)  Anders  freilich Wesen":    lai  drvalö   drvatyiisca    asi    usi ■     Dk.  /.  4.  44  (SBE.  47.  59). 'na{Kp.)gava*dvari>mzafar»..pairi.-\^    .     ^^^3-    V.    'ausschütten'.    Praes.    2 urvalit^m  (sd.)  Yt.//.2.  ,_(.^„^._  _  pp^p^  ^^„y^._
ai.  iarna-  m.    —    rii.:  undeutlich.    —     0  Im  ,     „™..     .        ,  1 -.„  ■
Cegensaii  zv  «i-;  sd.  mit  No.  5.  0    '(Flussiges)  ausschütten;    ausgiessen
.    „  ,,.,.,        .        .        ,    -  in  -'  (Akk.):    ya'äta  yat  htm    (näml.  zaü-
•  ].  »kanina;  Adj.  'taub  :  ndtl  avä  zaoirä  1  ;^^^^,  ^,^-.  _  _  ,,^^^^  _  _  ^^„^,v  "als  ob Paai.vise    yä      mävöya     frarmkarinb  .  .^^  ^j^  ^j^^^  Schlange  . .  in  den  Rachen  . .
'nasca  "i\5-^^-  ,  ^     .  .  ,  ,     „    .,  ; schUttete"N.4<?-       2)'(Samen)ausschütten,
si.  karna-    Ka\.    'stut lohne ,    np.  kor   'taub  ;  '  .  ,^  -  ■    ,     .        ,      .
s.  femer  KZ.  36.  15.  aussaen,  (Getreide)  durch  Aussaat  gewin-
...  ^     .  ,.     ,^    .     j    .     ,         nen':  aUavat  karitanam  {yavanam)  aHa-
.    ,.    
==== leaf 277
?).  |
*)  Die  mit  einem  spitzen  Metatlstück  ge- zogenen Furchitriche  tollen  dazu  dienen,  einen Unreineti  abzusondern  und  so  der  von  ihm drohenden  Ansteckungsgefahr  zn  begegnen.  Vgl,
KompA'.,  E.  —  Zum  V.  Üari.  —  Fü.;  (zu  1): *tri),  (zu  a):  küvar.  —  i>  Mit  ir.  ar  oder  /■, vorauf  mp.  iis  weist;  IF.  9.  j6i.  —  ')  Un- thero.  —  j)  Wo  kariavahl.  —  4)  zBed.  s.  kariü-.
•  p.  "fcaräa-"  m.  Name  einer  Gewichts- einheit**: 2  "sä  T>-ig.
'I  Deren  Gewicht  Grav  JAOS.  30.  55  zu bestimmen  versucht.  Danach  wäre  1  ^  i^  1 76.7JD4 Gramm.
Vgl.  ai.  iar/a-  m.  —  ■)  Zum  ar  s.  Foy  ZDMG.
S-t-  357-  :
•  j.  karäay-  £  i)  'Furche,  Furchstrich':' yai  .  .  'saim  (AS-)'*  kärayeiti  Yt. 4. 1 4.  2)  'Pflügen'  (nur  AbleiL)
AbleiL  —  Zum  V.  iiars-.  —  ai.  i^-fäj"  f. •Pflügen'.  —  ')  Ganz  unsicher.
).  iarlavani  F.  5:  lies  iariaifii;  s.  •iarsa:
•  j,  kariä-  f.  'abgefurchter,  durch  Furch- ' striche  abgegrenzter  Raum':  äa^  tum..' avaMstSis  ava  ttisiarfm  (sd.)  °sayä  V.^.12.
Zun  V.  ikars-.  —  zBed.  vgl.  'iarSa-  2  und larh;:  —  Pü.;  M.
j  •  j.  karäö.räzah-  Adj.  (auch  fem.)  'der !  dem  Gau  die  gesetzlichen  Bestimmungen
Igibt,  Gesetze  vorschreibt':  mi^tTm  .  . 'zavAsm  tylxamm  Yt.  /o.  6 1 ;  —  *frazain-' tlm  °sqm  (ASf.)"'  vyäxanam  Y.  ^s.s,  F.5,
I  Pü. ;  kisvar  vitäi ,  Npü. :  iibanda  iakr.  — '  '*  S  3^1-  ^  <^d  Ausgang  des  folgenden 1      Worts.
•  j.  karäiptar-  m.  Name  eines  Vogels, I 'accipiter'*' ■':   kö  avalia  dainqm  mSzda-
' yasnim  vT.barat  altaShxi  varpf^a  yd  yitnö I  ksrsnaoti  .  .  vti  'ta  "Wer  hat  dort  , ,  ver- breitet? ..  Der  Vogel  K."  V.2.  42.
*)  Er  gilt  Bd.  24.  11  und  Vr.  /.  1  Pü.  als I  Ralav  der  Vögel ;  s,  yiala  fraftirijäl-.  Vgl.  auch jBd.  /p.  6,  Zs.  23.  4.
;  Komp.:  Harii'  (nur  KompA.,  aus  "V"*.  IF- p.  a6l|,  zu  lat,  currö,  mhd.  hurrt»  (SOLMSEN Stud.30)-|-*/''"^(»iis  '^E'  Ve)"'""'  derKomp- form  des  Nom.  ag.  zum  V.pit-,  S  34%  JSchmidt Plur.  174);  also  eig.  'Schnellflieger',  vgL  gr. sfusTfjj«»,  (öuiiirtriK  'pi;!  (»  87)  und  lat  acd- piltt  bei  JSchmidt  aO.  —  >]  Diese  Bedeutung folgt  ans  Bd.  34.  11:  karUj'l  ki  farj  (i  r  k) i^äitftitl;  vgl.  np.  i-'ur/ (ZDMG.  ViJ.  493);  ander» Zs.  33.  4.  -r-  Pü. :  transskr.;  dazu  die  Erl.i (iuM'öi  (wozu  IFAnz.  Z2.  24).
•  j.  karäi'vant-  Adj.  'Pflüger,  Ackerer': Im  zS  ,  .  yä  Jarrfa  akarsta  saita  yä  karsya 'vata  "die  Erde  . .,  die  lang  ungepflügt liegt,  die  zu  pflügen  ist  vom  Pfliiger" V.J.  24.
ai.  vgl.  kfja-alä-  ra.  'Ackerbauer',  —  Fü. : kisiinSmand.
•  j.  karäij-  £  i)  '.\ckerland':  Z3mS *'suya'''  "des  Ackerlands  der  Erde"(?)  F. 5.  s)  'Flur,  Landgebiet,  -bezirk,  Gau': *pouru.niaili  hanjamaine  *pouru.nairyA 'suya  "in  der  zahlreich  besuchten  Festver- sammlung des  männerreichen  Gaus"  Y. //.  2.
Zum  V.  Mfl'/-.  —  ai.  katfu-  f.  'Furche'.  — Vgl.  'karia-,  iariä-,  karhiar-  und  -  auch  zFIejt.  — Bthl.  IF.  p.  276.—  Pü.  {zu  1);  *//  rar'),  (zu 2):  karlär,  Sü.:  krtaiilryrfu.  —  ■)  K  20  ;  M  6 hat  'h'ii,  —  ')  Vgl.  np.  kisl  lär.
•  j.  "karäta-  Adj,,  PPfP.:  s.  'kars-. KompE.  -  np.  t.Ua.
•  j.  'karsta-  Adj.  'gemacht,  bewirkt,  ver- anlasst'.
KompE.  ■ —  Vgl.  unter  "karsH,  "karilu,  wofür Pü.  karr  hat,  und  •frakarila-,  das  Pü.  mit  dem selben  Verbum  wie
```


## [2026-09-07T20:18:54.765Z] AGENT

Bartholomae's karšiptar- entry found. Now Horn, and the Pahlavi/Persian bird nodes.


## [2026-09-07T20:18:56.835Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HRN entry 191 (leaf=printed+21) ===\"; python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nprint(t[212][:2500])\nEOF"
}
```


### [2026-09-07T20:18:58.093Z] TOOL RESULT

```
=== HRN entry 191 (leaf=printed+21) ===
leaves 412
— 191 -
854. UuHt *Seite, Flanke', hu^Vl^ kustl 'Gürtel', vergl.
hergustvuan (No. 205) ; kusftgir 'Ringkämpfer (AM. 2()6
Zeile 8).
phlv. ktist^ kustak 'Seite*, kusttk^),
855. kuSten 'tödten', nt^^t^lD (Qiss. Dan.).
aw. l/ftaos-, kusaiti 'tödten'; phlv. kustan, vergl. asö]-
kvs (für aw. asavaynya-, vd. 5 (47)); skr. KÄö5-, kusnäti
'zerreissen' (?).
kurd. LW. (?) kustin 'tödton*; bei. L\V. (?) kuäag,
n. ßusay 'todten, scli lachten (207).
856. feesß/ ^Schildkröte ; Krebs (Zodiac, Sahn. I, 77 Vers
285)', keseto (dial.).
aw. kasyapu' 'Schildkröte' oder *Krebs' (Geldner,
KZ. 25, 503, 5()6j ; skr. (Brhm.) kagydpa- 'Schildkröte .
af/. kasy 'Schildkröte'; bei. käsib (190).
857. Ä-e«efc 'Elster .
Toniaschek, Painirdialokte S. 771, veigkM'cht aw.
karsiptan-^ phlv. kars{i)ft (L)eutun*i: nicht sicher), wa/.
karjöpc, sar. karjopc, si;'n. ksebc 'ElstiM-'.
858. kiSver^ kesver 'Ph-dteil'.
aw. karsvar- 'Weltteil'; phlv. kisvar^).
859. kesläen ziehen'.
aw. [/^km's-, karsayefi^); phlv. kasttan; ai. 1. [/^kars-,
• kdrsati, karmyati 'ziehen, schleppen'.
kurd. kisän ziehen'; af>'. k/dl; bei. kasay, n. /i'asay
'ziehen, abziehen, herausziehen' (19:^); arm. LW. (?)
Karsem 'ziehen*.
») Syr. LW. J^D^'ID, J^nDD, p^DDIp; ai'ab. LW. kustij (de
Lagarde, Ges. Abb. 59, 60); bei. LW. kustl (143). — Aber nicht gehört
dazu lat. c^ista *Rippe*, das Meringer, Sitzb. WAW. CXXV, *Beitr. z.
indg. Decl.*, 42, mir nicht einleuchtend, zu ai. dbthi- 'Knochen* stellt.
') Eine Volksetymologie in 'Selections of Zätsparnm* (West
P. T. I) 7, 9.
») Aw. [/has- will Hübschmann ZDMG. 44, 558 ausser Betracht
lassen.
```


## [2026-09-07T20:18:58.437Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HRN grep 191. ===\"; grep -n \"^ *191\\.\\| 191\\. \" HRN.txt | head; echo \"=== HRN carx/kaschak ===\"; grep -n -i \"karsipt\\|kar[sš]ipt\\|kaschak\\|kasak\\|Elster\" HRN.txt | head -20"
}
```


### [2026-09-07T20:18:58.504Z] TOOL RESULT

```
=== HRN grep 191. ===
2077:191. {2)ber, eber, auf, über, nahe bei' etc.; "ibN Is. 1, 1;
11051:191. Hiiflfßnltan zufriedenstellen', snäfjm(i)sn, snäyTnitärlli,
=== HRN carx/kaschak ===
7461:857. Ä-e«efc 'Elster .
7463:karsiptan-^ phlv. kars{i)ft (L)eutun*i: nicht sicher), wa/.
14562:! karSiptan- 857.
```


## [2026-09-07T20:19:19.131Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== PHD ahug ===\"; grep -n \"āhūg\\|ahug\\|ʾhwk\" PHD.txt PHD_mackenzie.txt | head -10; echo \"=== PHD karsipt ===\"; grep -n -i \"karšift\\|karšipt\\|karsift\" PHD.txt PHD_mackenzie.txt | head -10; echo \"=== PHD nisan ===\"; grep -n \"nišān\\|nisan\" PHD.txt PHD_mackenzie.txt | head -10; echo \"=== PHD nigah/nigerid ===\"; grep -n \"nigāh\\|nigerīdan\\|nigār\" PHD.txt | head -10"
}
```


### [2026-09-07T20:19:19.227Z] TOOL RESULT

```
=== PHD ahug ===
PHD.txt:993:bier gāhūg.
PHD_mackenzie.txt:2433:gahug [g)hwk ] bier.
PHD_mackenzie.txt:12386:ahog, ahug, xanag                 \ ~ t"O'    rrhid                          \~
=== PHD karsipt ===
=== PHD nisan ===
PHD.txt:128:delete mezidan ... suck. for ?mēzišn ... read ! meziin ... for mistan, *mēz- read... *mēz-.. mihoxt [mytwht' = Av. midaoxta-| falsehood. *mihr .. add ~ druxtan : break faith. add mizīdan, miz- [myc-ytn' | N mazidan] suck. for *moy-mard ... read mowmard ... mēy ... add M mwy. read nüxun [n^hwn' | P nxwn, N nàxun] (finger) nail. delete nāyīzag ... (read wezag). nek, ~th ... add benefit. nibastan ... delete SKBHWN-tn' < A Vškb; nibastan ... read M nb’st, P nb’y-. nibeg ... add M nbyg. nibištan ... |YKTYBWN-tn'... (not -stn'). nidan, nay- |DB(Y)LWN-tn' < A Ydbr |... nigün, ~sar |-s 1 | (P ngws’r)| downwards. add *nihēb |nyhyp | N ~] fear, terror. for nīšān read nišān...
PHD.txt:514:nihuftan, nihumb- [zhwptn', nhwmb- | = M, N <) cover, hide, conceal, clothe, nihumbidan [nhwmbytn'] = nihuftan. *nikóhidan, nikóh- [nkwh-ytn' | N ~] blame, execrate. ~išn: blame. ~išnīg : blameworthy, execrable. nil [nyl | N ~] indigo. nilópal [nylw(k)pl | N ~, nilēfar] lotus, water-lily. nimüdan, nimāy- [nmwtn', nmd- | M nmwdn, nm’y-, N ~] show, guide. nirfs- [nlps-] wane, decrease. ~išn: decrease, diminution. nirmad [nylmt'] profit, interest. ~ӧтапа [-’wmnd] profitable. P nisag [nys’k' | P nys’g] bright, splendid. niš- [nyi- | M nyyš-ydn, J ~] see, observe. nišān-, v. nišāstan. nīšān [ny$*x! | = M, N nisàn] sign, mark, banner. nišast [nsst! | N ~] association. nišastan, nišīn- [Y TY BWN-stn! < A V у; пт! | M nist, (nfyy-), N ~] sit. nišāstan, nišān- [Y TY BWN.stn!, 2n-; nP?stn!, nP?n- | M nf?st, (nP5y-), N ~] set, seat, plant, found. nišāyišn [n£ din! | M n$?y-, v. niSástan] foundation. nišēb [niyp | N ~] declivity; astr. dejection. ~ig [-yk'] declining. nišēm (nidm | M nšym, N ~an] seat, perch. ~ag [-k'] residence, abode. niSin-, v. niSastan. niwāģ [nw k! | M ng, N nawa] music, song, melody. *niwé [nwyk! | (N nuwéd)] good news. *niwéy-, -išn, v. niwistan, *niwéyénidan [nwykyn-ytn'] = niwistan. niwistan, *niwéy- [nwstn', nwyd- | nwyk-] announce, consecrate. —išn(ih): announcement. nixwār- [nswb’l- | M nyxw’r-] hasten. -išn: haste. niyübag [nyd’pk' | M ny’bg] becoming, fitting, suitable. ~th: suitability. niyāģ [nyd?k! | M nyg, N niya] grandfather, ancestor. niyāyišn [xyd?dšn! | N ~if] prayer, praise. niyāz [nyd?c | M ny’z, N ~] need, want, misery. —ómand [2wmnd | N ~mand] needy. ~6mandih: poverty. niyē(x)šidan, niyē(x)š- [n(y)duhš-ytn! | M nywi-, N niyófidan] hear. ~išn: hearing. І nizār [nz?l | (P nyz?*wr), N ~] weak, feeble.
PHD.txt:2732:mark daxšag, drēš(om), nišān.
PHD.txt:5296:nišān-!
PHD_mackenzie.txt:3786:nisan [nyen l I = M, N nUan] sign, mark, banner.
PHD_mackenzie.txt:3790:nisastan, nisan- [YTYBWN-stn', -)n-; ni)stn', n1)n-1 Mnf)st,(nf'y-),
PHD_mackenzie.txt:6001:at 0, pad.                               banner drafS, nisan.
PHD_mackenzie.txt:7049:mark daxsag, dros(om), nisan.              memorize warm kardan.
PHD_mackenzie.txt:7576:sign daxsag, nisan.                           sledgehammer potk.
PHD_mackenzie.txt:9909:nisan-, ,visan~                   - t""U\J\         wizihisnih                   AU t"U""U '\ \
=== PHD nigah/nigerid ===
512:nest [LOY T! < А P?yty | M nyst, N ~] is not. ~ih : non-existence. néw [TB < A tb; nyw' | = M, N —] good, brave. ~-ardaxSir [nyw lthsyl | N nard !] backgammon. nézag [nyck! | N néza] lance. nēzūmān, —16 [nycwmn', -yk! | M nyzwm!n] dextrous, skilful. -~th: skill, artistry. nibard [nplt' | N nabard] fight, struggle, battle. ~ag [-k! | N ~a] tried, experienced. nibardīdan, nibard- [npit-ytn! | P nbrd'd] fight, do battle. nibastan, nibay- [SK BHWN-tn! < A У hb; npstn', npd- | M nbst] lie down, sleep. nibāstan, *nibày- [np'stn! | M nb’st, nb y-] lay down. nibég [npyk! | N niwé] writing, scripture, book. nibém [npdm | (P nbdm-)] lying, prostrate. nibištan, nibés- [VK TY BWN-stn! < A yktbwn, У КЬ; npstn' | M nbyšt, nbys-, N —] write. nidan, nay- [YD(B)LWN-tn! < A ydbrwn, V dbr | M nyydn, ny-] lead. nidom [nytwm] least, smallest. nifridag [nplytk' | N nifrid] accursed. nifrin [nplyn' | N <] curse. nigah [nk’s | M пол, N ~] look, attention. ~ dāštan: watch, keep. — kardan: look. ~-darih, —-dári&nih [-d?/(sn)yh | N —dārī] keeping, care. nigān [nk’n' | P ng’n] buried. nigar- [nk’l- | M ng’r-, N ~] draw, design, paint. ~ag [-h! | (M agin, N nigār)] image, picture, diagram. nigástar [nk?s I] guard; protective. nigeridan, niger- [nkyl-ytn! | N nigaridan] look, observe. --išn: observation. ~iSnig : evident, manifest. nigéxtan, nigéz- [nkyhtn!, nkyc-] expound. ~i$n: exposition. nigéz [nkyc] exposition. nigün [nkwn! | N ~] inverted, upside down. ~th: depth, downward direction. ~sar [-s?l | М ngwns’r] downwards. nihadag [nyd’tk' | M ny? dg] foundation. nihādan, nih- [TNH TWN-tn! < А hnht, ~ nht | M пуа, nyh-, N ~] put, place, establish. nihal [nbl | N ~] sapling, self-planted tree. nihān [nyh’n' | N ~] concealment, secrecy. ~ig [-yk! | N ~7] secret. nihang [nsng] small, few.
1159:care (n.) nigāhdār(išn)ih, pahrēz; témár.
1351:consider abar nigerīdan, pad ēd dāštan, handēšīdan, hangārdan, ēšmurdan, uskārdan.
1598:diagram nigārag.
1692:draw (pull) kešīdan; (picture) nigār-; ~ out, ~ water āhixtan, hixtan.
2377:image nigārag, pahikar.
2517:keeping nigāhdār(išn)īh.
2661:look (v.) nigeridan, nigāh kardan.
3033:paint (picture) nigār-.
3121:picture pahikar, nigārag.
```


## [2026-09-07T20:19:20.156Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== NYB ahug ===\"; grep -n \"āhūg\\|āhūk\\|ʾhwk\" NYB_vol2_glossary.txt | head; echo \"=== NYB nisan ===\"; grep -n \"nišān\" NYB_vol2_glossary.txt | head; echo \"=== SOD gazelle/deer ===\"; grep -n -i \"gazelle\\|deer\" SOD.txt | head -20"
}
```


### [2026-09-07T20:19:20.232Z] TOOL RESULT

```
=== NYB ahug ===
=== NYB nisan ===
2764:nišāstan [nš'"stn'; YTYBWN - ’stn' 2127, YTYBWN-stn' 242-6] nišin- A. to place, to seat a p.; to encamp (an army): pres. 3d p. sg. nišānēt [nš'nyt' 7411], 3d p. pl. nišānēnd [YTYBWN-nynd 74]; pt. = pret. pass. 3d p. sg. nišāst [n3’st' 131; YTYBWN-st' 115257; YTYBWN-st' 012]; — B. to institute a Fire, to found a (special) Fire-temple 955-13-15 [YTYBWN-st']. 1139-10.21-22, 1164-8 [YTYBWN.st']: perhaps another vb., the ideogr. being the SW spelling of Prth YTYB- from Aram TAYYEB ‘to make ready, to prepare, to provide’, KZŠPrth l. 17: 'trw wrhrn YTYBW-t, Gr. v. tupeta Iovapadpav ispvoauev; of the Prs. rendering only YTYB ... is visible, but sufficient to show that the Prs. equivalent
=== SOD gazelle/deer ===
9197:gazelle 
34530:deer 
37557:deer 
88683:deer     4079,  4517 
89919:gazelle    258
```


## [2026-09-07T20:19:36.099Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SOD entry 258 ===\"; grep -n \"^ *258\\b\\|^258 \\| 258  \" SOD.txt | head; echo \"---\"; grep -n \"s'wk\\|sʾwk\\|'sʾwk\\|ʾsʾwk\" SOD.txt | head -20"
}
```


### [2026-09-07T20:19:36.188Z] TOOL RESULT

```
=== SOD entry 258 ===
7534:258. 
9195:258  "s'wk*  B  ^7 
22452:258,  10,  zyt>wk(Sji-) 
50984:258 
77370:258  "  so  white";  wtsVtt,  TSP  2.1020  "so  high" 
---
9195:258  "s'wk*  B  ^7 
69931:9179  s'wkwr'k   B  j/V^
```


## [2026-09-07T20:19:37.517Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== CHEUNG axs/nis ===\"; grep -n \"\\*axš\\|ni-xš\\|nixš\\|niš-\\|\\*xšay\" CHEUNG.txt | head -20; echo \"=== CHEUNG ahu ===\"; grep -n \"āhū\\|āsu-\" CHEUNG.txt | head -10"
}
```


### [2026-09-07T20:19:37.582Z] TOOL RESULT

```
=== CHEUNG axs/nis ===
10022:prxwy’. || (+ *fra-) Pres.: IND. 3pl. BSogd. Brxw’y’ntw || (+ *niš-) Pass.: pret. intr. IND. 35р. BSogd. 
19874:*KHOTANESE: LKh. pusta- (ppp.) ‘driven’ || (+ *niš-) naspusta- ‘driven, thrown out’ 
20049:cause’ || (+ *niš-) LKh. naspasd- ‘to remove’ = SGS: 41, 18, 51 
=== CHEUNG ahu ===
```


## [2026-09-07T20:19:47.271Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '9180,9215p' SOD.txt; echo \"=== pages file ===\"; python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if '\"s\\'wk' in p or \"s'wk\" in p and '258' in p:\n        print('leaf',i)\n        import re\n        for l in p.split('\\n'):\n            if '258' in l or \"s'wk\" in l: print('   ',l[:200])\n        break\nEOF"
}
```


### [2026-09-07T20:19:48.623Z] TOOL RESULT

```
asakc   ©<v^*sak-   =>*s>ytk 

suitable,  compatible 
TSPn  p2 16,  8.139,  140 

255  »s»nk  °±  *s»k 

256  Vt-   B  =»  »s- 

257  Vwys-   B  ojl^J*^l*  i^^ 
asuxs  (*swyt-) 

(to)bc  burned,  (to)bo  consumed 
TSP  2.530-,  BSTBL,  Vim.  117 

258  "s'wk*  B  ^7 
asuk   (sswk)  ©<*dsuka-,  Av.  asu\  Pahl.  ahug 
gazelle 

SCE  151,  354;GMS976n  978 

259  »s»wr   B  Vj^Oh^ 
asOr   (*swr)   ©<Skt,  asura   ©pi.  -t\  ob.  pi.  -/y, 

-}n   =^swr} 
Asura 
STii  8.6;  BSTBL,  Padm.  3;  TSP  22.19 

260  "s'ym'nSy   B  o>; 

asemande   =^ss- 
possession 
STii  8.2  p574 

261  »sp'nh  ?   S  ?  J>i&<JX 
aspon  ?   (Bsprnh)  ©Av.  aspdrdnah   ^'nspmh  ? 
=== pages file ===
leaf 75
              aruyd ©pt. st. =»»rwxs-                                         258 "s'wk* B                                           ^7
```


## [2026-09-07T20:19:58.169Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\np=t[75]\nm=re.findall(r'\\[pdf page \\d+\\]',p)\nprint(m)\nprint(p[:300])\nEOF\necho \"=== BQT v1 ahu ===\"; grep -n \"آهو\" BQT_v1_pages.txt | head -20"
}
```


### [2026-09-07T20:20:35.372Z] TOOL RESULT

```
[]
                                                                                                                                     10
      Vync

             Hen. BBB; Bcnv. TSP 2.774 n pl79                                                                             */,

      239 Vync       B, M
=== BQT v1 ahu ===
1224:نتوانستندی آهوختن... > ۱ تار یخ بخارا ایضاً س ۵۷.
3448:ز - شیرازی : آهودوستك (ذیل" بر گ‌کازرونی » حزا دینارویه»
6442:تلم رودخانه ایست که آنرا رودخانة آهو ٩‏ فیز
9277:آهنگری - شفل وعمل آهنگره رگآهو پای
9287:استماره چشم را نیز آهو مبگویند - و شاهد
9292:آهوردی با واو مجهول بی وزن
9300:آهوی لقن س بسن یآهوی‌خاورست
9302:" آهوی دی - کنابه از آفتاب
9307:آهوی شیر اقکن - چن-طلوب
9310:آهوی فاك. 0 از خورشید
9313:۱ آهو یی - بکسر بای اول و سکون
9317:2 ای‌مبا رکه منای آهویای
9324:که هشن آهون‌بران خا کت ۳ «لفت نامه».
9326:زیبری مفزت آهومند گشته است
9327:( برهان فاطع ۱۴)(۱) بىمنیآهو باش د که عربان«غزال» کوبند ۱ .
13674:است و آنرا سب ارتفاع ی که دارد اله آهوت
15378:اسلام : آهواز» [رك : خوزستان] اهواز کرسی خوزستان و راءآهن جنوب ازآن گذرد و بضرعشهر
15388:۱ - رد :آهون. ۲۷ - رك : آهون‌بر. ۸۸ رك : آعانه.
17551:٩‏ - بند پولاد بردهن‌بابد آهو ار برئسس نهد بتفوز. ازری‌هروی ؛ رك: پتفوز.
25686:جکر آهو و مغز بادام و امثال آن سازند که
```


## [2026-09-07T20:20:43.712Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nlines=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\n# find nearest [pdf page N] tag before line 9300\nfor i in range(9300,9200,-1):\n    m=re.search(r'\\[pdf page (\\d+)\\]',lines[i])\n    if m: print('tag before 9300:',m.group(0),'at line',i); break\nfor i in range(9300,9400):\n    m=re.search(r'\\[pdf page (\\d+)\\]',lines[i])\n    if m: print('tag after 9300:',m.group(0),'at line',i); break\nprint('\\n'.join(lines[9270:9335]))\nEOF"
}
```


### [2026-09-07T20:20:45.011Z] TOOL RESULT

```
]هو بر وزن کاهو . جالورست
۶ مناس ۵ ۰ بر : هنگه و آهنجیدن .
۴ ره : لمت‌نامه .
ی ۱۸۶ > .
« لفت‌یامه » :
خر ۰
آهنگری - شفل وعمل آهنگره رگآهو پای
عب را نیز گفته اند "۱ خواه با مردم باشد و
خواء با چیزهای دبگر-
و یمعتی رم باشد که از
رمیدن است چه آحوبی
رمیدگی را کوبند - و
بمعنی قرباد و آواز بلئد . . ۳
عم آمنه است - و تام
مرضی و عأی حم صست احو
که آیزا جربی ضیق‌النفی خوانند - و بطریق
استماره چشم را نیز آهو مبگویند - و شاهد
و ممثوق را عم کنته ان .
]هو بای » با بای‌فارسی بالف کشده
و خالةٌ شش پپلو را گویند -
19
آهوردی با واو مجهول بی وزن
لاهوری » یمعنی‌خردل باشد ؛ و آن داروبی است
یار تند و نیز ؟ . 8 ۱
] هون بر وزن قارون » رخنه و قب
را کونند ۴
سم
"هون پر « بفئح بای ایجد بر وزن "
عالمتاب است .
آهوی لقن س بسن یآهوی‌خاورست
که کنابه از خورشید جهان آرا باشد .
" آهوی دی - کنابه از آفتاب
است - و صراحی طلا را نیز گفته‌اند .
هوی‌سیهین « ساتی سفید پوست را
گویند و آن صاحب حنئی است که در عجلس
بمردم شراب میدحد .
آهوی شیر اقکن - چن-طلوب
و تیش و مت ی
صست .
آهوی فاك. 0 از خورشید
است
از با اصافی کردن باشد .
۱ آهو یی - بکسر بای اول و سکون
بای ثأنی » بمعنی رمید کی ۷ و عیب ناکی باشد.
ول وعیب باه اکن :
یتیآن جاور که ژاید مك
2 ای‌مبا رکه منای آهویای
< بشت۱ ص۱۱۵ ب*.
ابوالفرج ردلی ۶ لخت نامه ‌.
گاه بررفتن ی است نیز
م شهاب طلحه . رک : ات ناعه.
۵ - بدل درفکندی چنان چاکه را
۷ - رمندگی لت نامه» .
که هشن آهون‌بران خا کت ۳ «لفت نامه».
مخز آحومند » مختل » مخبط :
زیبری مفزت آهومند گشته است
( برهان فاطع ۱۴)(۱) بىمنیآهو باش د که عربان«غزال» کوبند ۱ .
]هیافه » بکر تالك مروزن نازبانه »
استضوان بای دماغ را کویند و آنرا بیبی
وس وس نب ی 9
باشد لیکن" آباک سار واه است وبیی
«حناك» عیگوف .
آهیخت ۴ ت بر وزن آوبثت ؛
نی يکنی و برآورد 2 پاشدبا
ری ده
```


## [2026-09-07T20:20:53.636Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -c $'\\f' BQT_v1_pages.txt; grep -n \"pdf page\" BQT_v1_pages.txt | head -5; python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\n# find leaf containing 'آهوی سیهین' region\nfor i,p in enumerate(t):\n    if 'آهومند' in p or 'آهویی' in p:\n        print('leaf',i); print(p[:200]); break\nEOF"
}
```


### [2026-09-07T20:20:54.990Z] TOOL RESULT

```
766
leaves 777
leaf 282
آهو پای
عب را نیز گفته اند "۱ خواه با مردم باشد و
خواء با چیزهای دبگر-
و یمعتی رم باشد که از
رمیدن است چه آحوبی
رمیدگی را کوبند - و
بمعنی قرباد و آواز بلئد . . ۳
عم آمنه است - و تام
مرضی و عأی حم صست
```


## [2026-09-07T20:21:23.525Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== AHD okus ===\"; grep -n -i \"ōku-\\|oku-\\|ocior\\|accipiter\" AHD_watkins1985.txt | head -10; echo \"=== AHD okw eye ===\"; grep -n -i \"okw-\\|ok\\*w\\|window\\|ophthalm\" AHD_watkins1985.txt | head -10"
}
```


### [2026-09-07T20:21:23.584Z] TOOL RESULT

```
=== AHD okus ===
661:ladh-. To be hidden. 1. Greek léthé, forgetfulness: LETH- ARGY, LETHE. 2. Zero-grade form *ladh- (< *bdh-), with nasalized form *landh-, in Greek lanthanein (aorist lathein), to escape the notice of, with middle anthanes- thai, to forget: LANTHANUM; ALASTOR. 3. Suffixed (sta- tive) variant form */at-é- in Latin latére, to lie hidden: LATENT. [In Pok. 2. /a- 651.] laiwo-. Left. Latin Jaevus, left: LEVO-; (LEVOROTATION), (LEVOROTATORY). [Pok. laiuo- 652.] laks-. Salmon. Suffixed form */aks-o- in Germanic */ahs- az in Old High German Jahs, salmon: Lox}. [Pok. lak- 653.] laku-. Body of water, lake, sea. 1. Latin /acus, lake, pond, basin: LAKE!. 2. Greek lakkos, cistern: LACCOLITH. 3. O-grade form *loku- in Old Irish and Scottish Gaelic loch, lake: LocH, LouGH. [Pok. laku- 653.] lap-. To light, burn. Nasalized shortened form */a-m-p- in Greek lampein, to shine: LAMP, LANTERN; ECLAMPSIA. [Pok. la(i)p- 652.] las-. To be eager, wanton, or unruly. 1. Suffixed Ger- manic zero-grade form *lustuz in: a. Old English Just, lust: Lust; b. Old High German Just (> German Lust), desire: WANDERLUST; Cc. Germanic denominative verb *lustjan in Old English lystan, to please, satisfy a desire: LisT’, 2. Suffixed form */as-ko- in Latin lJascivus, wan- ton, lustful: Lascivious. [Pok. las- 654.] lat-. Wet, moist. Latin latex, liquid: LaTEx. [Pok. Jat- 654.] lau-. Gain, profit. 1. Suffixed form */au-no- in Germanic *Jaunam in Old High German J6n, reward: GUERDON. 2. Suffixed zero-grade form */u-tlo- in Latin lucrum, gain, profit: LUCRATIVE, LUCRE. 3. Suffixed variant form *low-ero- in Irish Gaelic ledr, sufficiency, enough: GA- LORE. [Pok. ldu- 655.] lé-1. To get. Contracted from “lea-. Suffixed zero-grade form *b-tr- in: a. Greek Jatreia, service (for pay), duties, worship: -LATRY; b. Greek Jatron, pay, akin to the Greek source of Latin latré, robber: LARCENY; c. Greek -/latrés, worshiper: IDOLATER. [Pok. 2. /é(i)- 665.] lé-2, To let go, slacken. Contracted from *les-. 1. Ex- tended form */éd- in: a. Germanic */étan in Old English létan, to allow, leave undone: LET!; b. Germanic deriva- tive *léthigaz, freed, in Medieval Latin /étus, litus, serf (< “free man”): LIEGE. 2. Extended zero-grade form */d- in: a. Germanic */ataz in Old English Zt, late, with its comparative lztra, latter, and its superlative Jatost, last: LATE, LATTER, LAST!; b. Germanic */atjan in Old English lettan, to hinder, impede (< “to make late”): LET?; c. suffixed form */od-to- in Latin lassus, tired, weary: LASSITUDE; ALAS. 3. Suffixed reduced form */é-ni- in Latin lénis, soft, gentle: LENIENT, LENIS, LENITIVE, LENITY. [Pok. 3. lé(i)- 666.] leb-'. Base of loosely related derivatives meaning “hang- ing loosely.” I. Variant form *lep- in Germanic */ap- in Old English lzppa, lappa, flap of a garment: Lap’. II. Nasalized form *lemb(h)-, with variant form *slemb(h)-. 1. Germanic *lemp- probably in obsolete English limphalt, lame (halt, lame; see kel-'): LIMP. 2. Germanic */ump- in: a. Dutch lomp, rag, akin to the Low German source of Middle English Jump, lump: LUMP!; b. possibly obsolete English Jump, lumpfish: LUMPFISH; Cc. German Lumpen, rags: LUMPEN. 3. Ger- manic *slimp- in Middle Dutch slim(p), slanting, bad: SLIM. 4, Middle High German slam, mud: SLUMGULLION. 5. Old Norse slambra, to strike at, akin to the Scandina- vian source of SLAM!. 6. Norwegian slumpa, to slump, akin to the Scandinavian source of sLuMpP. III. Variant *(s)lab- in Germanic *s/ab-. 1. Danish slab, mud, akin to the Scandinavian source of SLAB2. 2. Swedish slabb, slime, mud, akin to the Scandinavian source of Irish slab, mud: sLos. IV. Variants *slap-, *slep-. Germanic *slap- in: a. Low German s/app, slap: SLAP; b. Old Norse slafra, to slaver: SLAVER}. V. Variant */ab-. 1. Germanic *lab- in Old French label, ribbon, strip: LABEL. 2. Latin
796:Oku-. Swift. Zero-grade form *aku- in compound *oku-petro-, “swift-flying,” in Latin accipiter, hawk (*pet-ro-, flying; see pet-): ACCIPITER. [Pok. 6ku-s 775.] okv-, To see. 1. Germanic *augén- (with taboo deforma- tion) in: a. Old English éage, eye: EYE; DAISY; b. Old Norse auge, eye: WALLEYED, WINDOW; Cc. Low German 00g, eye: OGLE. 2. Suffixed form *ok-olo- in: a. Latin oculus, eye: EYELET, OCELLUS, OCULAR, OCULIST, UL- LAGE; INOCULATE, MONOCLE, OCULOMETER, OCULOMO- TOR; b. Gallo-Latin compound *ab-oculus, blind, modeled on Gaulish ex-ops, blind, in French aveugle, blind: INVEIGLE. 3. Form *okv-s in Greek dps, eye (and stem *op-, to see): METOPIC, MYOPIA, NYCTALOPIA, PEL- OPS, PHLOGOPITE, PYROPE. 4. Suffixed form *ok-ti- in Greek opsis, sight, appearance: OPSIN, -OPSIS, -OPSY; AUTOPSY, (IODOPSIN), (RHODOPSIN), SYNOPSIS. 5. Suf-
1208:ABAFT apo- ABANDON bha-2 ABASE bassus ABASH bat- ABASIA gWa- ABATE battuere ABBREVIATE mregh-u- ABDICATE deik- ABDUCENS deuk- ABDUCT deuk- ABELE albho- ABERRATION ers-1 ABET bheid- ABEYANCE bat- ABHOR ghers- ABIDE bheidh- ABJECT yé- ABJURE yewes- ABLATION  tele- ABLAUT apo-, kleu-1 ABLE ghabh- ABLUTION leu(@)- ABNEGATE ne ABNORMAL gné- ABODE bheidh- ABOLISH al-3 ABORT er-! ABOUND wed-1 ABOUT ud- ABOVE upo ABRADE réd- ABRIDGE mregh-u- ABROGATE reg-1 ABROSIA gWere-4 ABRUPT reup- ABSCESS ked- ABSCISE kae-id- ABSCOND dhé-1 ABSENT eS- ABSOLUTE leu-1 ABSOLVE feu-1 ABSORB srebh- ABSTAIN ten- ABSTRACT tragh- ABSTRUSE treud- ABSURD swer-2 ABULIA gWele-1 ABUT bhau- ABYSS gWadh- ACANTHO- ak- ACANTHOPTERYGIAN pet- ACANTHUS ak- ACAPNIA kwép- ACCEDE ked- ACCELERATE kel-3 ACCENT kan- ACCEPT kap- ACCESS ked- ACCIDENT kad- ACCIPITER Oku- ACCLAIM kele-2 ACCLIVITY klel- ACCOLADE kwel-1 ACCOMMODATE med- ACCOMPLISH pele-1 ACCORD kerd-1 accosT kost- ACCOUNT peu- ACCRUE_ ker-3 ACCUMBENT keu-2 ACCUMULATE keue-2 ACCURATE cira ACERATE ak- ACERB ak- ACETABULUM ak- ACETIC ak- ACETUM = ak- ACHALASIA ghé-
=== AHD okw eye ===
284:tives: a. ekhinos, hedgehog (< “‘snake-eater”): ECHINO-, ECHINUS; b. ekhidna, snake, viper: ECHIDNA. [Pok. ang#(hji- 43.] ank-. Also ang-. To bend. I. Germanic *ank- in Old Norse *ankula and Middle English ancle, ankle: ANKLE. Il. Suffixed form *ank-ulo-. 1.Germanic *ang-ul- in: a. Old English angul, angel, fishhook: ANGLE!; b. prob- ably Latin Angli, the Angles: ANGLE. 2. Greek ankulos, crooked, bent: ANKYLOSIS; ANCYLOSTOMIASIS. ITI. Greek ankura, anchor: ANCHOR. IV. Greek ankdn, elbow: AN- CON. V. Sanskrit anka, hook, avicati, he bends: PALAN- QUIN. VI. Suffixed variant form *onk-o- in Latin uncus, hooked, bent: UNCINARIA, UNCINATE, UNCINUS, UNCUS; UNCIFORM. VII. Suffixed form *ang-olo- in Latin angu- lus, angle, corner: ANGLE*, [Pok. 2. ank-, ang- 45.] ano-. Ring. 1. Latin dnus, ring, anus: ANUS; ANILINGUS. 2. Latin diminutive annulus, ring, signet ring: ANNULAR, ANNULET, ANNULUS. [Pok. dno- 47.] ans-. Loop, handle. Latin dnsa, handle: ANSATE. [Pok. ansa 48.] ansu-. Spirit, demon. 1. Germanic *ansu- in Old Norse dss, god: AEsIR. 2. Suffixed reduced form *nsu-ro- in Avestan ahura, spirit: AHURA Mazpa, Ormazp. [Pok. ansu- 48.] ant-. Front, forehead. I. Inflected form (locative singular) *anti, “against,” with derivatives meaning in front of, before; also end. 1. Germanic *andi- in Old English and-, indicating opposition: UN-?; ALONG. 2. Germanic *andja- in Old English ende, end: END. 3. Latin ante, before, in front of, against: ANCIENT!, ANTE, ANTE-, ANTERIOR; ADVANCE. 4. Greek anti, against, in enantios, opposite: ANTI-; ENANTIOMER, ENANTIOMORPH. 5. Compound form *anti-oko-, “appearing before, having prior aspect” (*akw-, appearance; see okW-), in Latin antiquus, former, antique: ANTIC, ANTIQUE. 6. Reduced form *nti- in Ger- manic *und- in Old Norse und (> Middle English un-), until, unto: UNTIL. 7. Variant form “anto- in Sanskrit antah, end, in Vedantah, essence of the Veda: VEDANTA. II. Probable inflected form (locative plural) *antbhi, “on ter sides of,” whence *ambhi. See ambhi. [Pok. ant-s 48. ap-'. To take, reach. 1. Latin apere, to attach, join, tie to: APT, (APTITUDE), ATTITUDE; (INEPT). 2. Latin apisci, to attain: ADEPT. 3. Latin apex, top, summit (< “something reached”): APEX. 4, Prefixed form *co-ap- (co-, together; see kom) in Latin cdpula, bond, tie, link: copuLa, COPULATE, COUPLE. 5. Perhaps Latin ammentum, dmen- tum (< *ap-mentum, “something tied”), thong, strap: AMENT!, [Pok. 1. ap- 50.] ap-2, Water, river. Iranian ap- in Persian ab, water: JULEP. [Pok. 2. ap- 51.] apero-. Shore. Perhaps a derivative of ap-?. Suffixed form *dper-yo- in Greek épeiros, land, mainland, conti- nent: EPEIROGENY. [Pok. dpero- 53.] apo-. Also ap-. Off, away. 1. Germanic *af in: a. Old English of, zf (> Middle English of, of-), off: oF, OFF, OFFAL; b. Old English ebba, low tide: EBB; c. Old High German aba, off, away from: ABLAUT; d. Germanic *aftan- in Old English zftan, behind: ABAFT. 2. Latin ab, ab-, away from: AB-!. 3. Greek apo, away from, from: apo-. 4, Suffixed (comparative) form “*ap(o)-tero- in Germanic *aftar- in Old English zfter, after, behind: AFTER. 5. Suffixed form *ap-t-is- in Germanic *aftiz in Old English eft, again: EFTsoons. 6. Suffixed form *apu-ko- in Germanic afug- in Old Norse dfugr, turned backward: AWKWARD. 7. Possible root *po(s), on, in: a. Russian po, at, by, next to: PoGROM; b. Latin post, behind, back, afterward: POST-, POSTERIOR; POST- MORTEM, PREPOSTEROUS, PUISNE, (PUNY); C. Latin pd- nere, to put, place, from *po-sinere (sinere, to leave, let; of obscure origin): APPOSITE, (APPOSITION), COMPONENT, (COMPOSE), (COMPOSITE), (COMPOSITION), (COMPOUND), DEPONE, DEPOSIT, DISPOSE, EXPOUND, IMPONE, IMPOSE, INTERPOSE, OPPOSE, POSITION, POSITIVE, POST, POSTS,
528:in Greek khriein, to anoint: CHRISM, CHRIST, CHRISTEN, (CHRISTIAN); (CHRISTMAS). [Pok. ghréi- 457.] ghreib-. To grip. 1. Germanic *grip- in Old English gripe, grasp, and gripa, handful: crip!. 2. Germanic *gripan in: a. Old English gripan, to grasp: GRIPE; b. Old French gripper, to seize: GRIPPE. 3. Suffixed o-grade form *ghroib-eyo- in Germanic *graipjan in Old English grd- pian, to feel for, grope: GROPE. [Pok. ghreib- 457.] ghrem-. Angry. 1. Germanic *grimmaz in: a. Old English grim(m), fierce, severe: GRIM; b. Old French grimace, a grimace: GRIMACE. 2. Germanic *grum- in Middle Dutch grommen, to mutter angrily, probably akin to Middle English grummen, to grumble: GRUMBLE. 3. Suffixed o-grade form *ghrom-o- in Russian grom, thunder: Po- crom. [Pok. 2. ghrem- 458.] ghrendh-. To grind. 1. Germanic “grindan in Old Eng- lish grindan, to grind: GRIND. 2. Germanic *grinst-, a grinding, in Old English grist, the action of grinding: GRisT. 3. Latin frénum (< frendere, to grind), horse’s bit (on which its teeth grind), bridle: FRENULUM, FRENUM; REFRAIN). 4, Variant form *ghrend- is sometimes but improbably regarded as the root of Greek khondros, granule, groats, hence cartilage: CHONDRO-; HYPOCHON- DRIA, MITOCHONDRION. [Pok. ghren- 459.] ghréu-. To rub, grind. Extension of gher-4. 1. Germanic *greut- in Old English gréot, sand, gravel: GRIT. 2. Ger- manic *grut- in Old English grotan, pieces of hulled grain, groats: GROATS. 3. Germanic “grit- in: a. Old English griit, coarse meal: GRouT; b. Old French gruel, porridge: GRUEL. 4, Germanic *grautaz, coarse, thick (< “coarsely ground”), in: a. Old English gréat, coarse, thick, bulky, large: GREAT; b. Middle Dutch groot, thick: Groat. 5. Germanic *griiw-, to recoil from (< “to be offended, be grated on by”), in Middle Dutch griiwen, to abhor, akin to Middle English grue, horrible: GRUESOME. 6. Variant form *ghrow- in Greek khrés, skin (< “rough surface” ?), hence flesh, complexion, color: RHODOCHRO- SITE. 7. Suffixed variant form *ghré-mn in Greek khréma, skin, complexion, color (semantic development as in 6. above): CHROMA, CHROMATIC, CHROMATO-, CHROME, -CHROME, (CHROMIUM), CHROMO-; ACHRO- Matic. 8. Probably Celtic *graw- in Old French grave, greve, coarse sand, gravel: GRAVEL. 9. Probably Latin *grau-, to touch, graze, in con-gruere, to agree (com-, together; see kom): CONGRUENT. [Pok. 2. ghréu- 460.] ghwer-. Wild beast. 1. Suffixed form *ghwer-o- in Latin ferus, wild: FERAL, FIERCE. 2. Compound *ghwero-okv-, “of wild aspect” (*-ak-, “-looking”; see okw-), in Latin feréx (stem feréc-), fierce: FEROCIOUS. 3. Length- ened-grade form *ghwér- in Greek thér, wild beast: TREACLE; THEROPOD. [Pok. ghuér- 493.] gladh-. Smooth. Suffixed form “gladh-ro- in Latin gla- ber, smooth, bald: GABRO, (GLABELLA), GLABROUS. gleubh-. To cut, cleave. 1. Germanic *k/euban in Old English cléofan, to split, cleave: CLEAVE!. 2. Germanic *klub-, a splitting, in: a. Old English clufu, clove (of garlic): CLOVE*; b. Middle Dutch clove, a cleft: KLOOF. 3. Germanic *k/aubri- in: a. Old Norse kleyfr, easy to split, perhaps akin to Middle English cliver, “expert in seizing,” skillful: CLEVER; b. Old Norse lofi, a cleft, akin to English clevi, “cleft instrument,” clevis: CLEVIS. 4. Zero-grade form *glubh- in Greek gluphein, to carve: GLYPH, GLYPTIC; ANAGLYPH, HIEROGLYPHIC. 5. Suffixed zero-grade form *glubh-md- in Latin glima, husk of grain: GLUME. [Pok. gleubh- 401.] glégh-. Thorn, point. 1. Suffixed form *glégh-i- in Greek glokhis, barb of an arrow: GLOCHIDIUM. 2. Suffixed form *glégh-ya in Greek gléssa, glétta, tongue, hence also language: GLOSS2, (GLOSSARY), GLOTTIS; BUGLOSS, GLOS- SOLALIA, ISOGLOSS, POLYGLOT, PROGLOTTID. [Pok. glégh- 402.] gno-. To know. Contracted from *gnoo-. 1. Variant form *gné- in Germanic *kné(w)- in Old English cndwan, to know: KNOW. 2. Zero-grade form *gno- in: a. Germanic
796:Oku-. Swift. Zero-grade form *aku- in compound *oku-petro-, “swift-flying,” in Latin accipiter, hawk (*pet-ro-, flying; see pet-): ACCIPITER. [Pok. 6ku-s 775.] okv-, To see. 1. Germanic *augén- (with taboo deforma- tion) in: a. Old English éage, eye: EYE; DAISY; b. Old Norse auge, eye: WALLEYED, WINDOW; Cc. Low German 00g, eye: OGLE. 2. Suffixed form *ok-olo- in: a. Latin oculus, eye: EYELET, OCELLUS, OCULAR, OCULIST, UL- LAGE; INOCULATE, MONOCLE, OCULOMETER, OCULOMO- TOR; b. Gallo-Latin compound *ab-oculus, blind, modeled on Gaulish ex-ops, blind, in French aveugle, blind: INVEIGLE. 3. Form *okv-s in Greek dps, eye (and stem *op-, to see): METOPIC, MYOPIA, NYCTALOPIA, PEL- OPS, PHLOGOPITE, PYROPE. 4. Suffixed form *ok-ti- in Greek opsis, sight, appearance: OPSIN, -OPSIS, -OPSY; AUTOPSY, (IODOPSIN), (RHODOPSIN), SYNOPSIS. 5. Suf-
798:fixed form *ok-to- in Greek optos, seen, visible: OPTIC; CATOPTRIC, DIOPTER, OPTOMETRY, PANOPTIC. 6. Suffixed form *okv-d in Greek opé, opening: METOPE. 7. Suffixed form *okv-mn in Greek omma (< *opma), eye: OMMA- TIDIUM, OMMATOPHORE. 8. Greek ophthalmos, eye (with taboo deformation): OPHTHALMO-; EXOPHTHALMOS. 9. Zero-grade form *ok- (of oldest full-grade form *zok-) in: a. Latin antiquus, “appearing before, having prior aspect,” former (*anti-, before; see ant-); b. Latin atréx, “black-looking,” frightful (*atro- black; see ater-); c. Latin ferdx, “wild-looking,” fierce (*ghwero-, wild; see ghwer-). [Pok. ok+- 775.]
1020:ster-*, Star. 1. Suffixed form “ster-s- in Germanic “ster- rén- in Old English steorra, star: STAR. 2. Suffixed form *stér-ld- in Latin stélla, star: STELLAR, STELLATE; CON- STELLATION. 3. Oldest root form “aster- in Greek astér, star, with its derivative astron, star, and possible com- pound astrapé, asteropé, lightning, twinkling (< “looking like a star”; Ops, stem op-, eye, appearance; see okw-): ASTER, ASTERIATED, ASTERISK, ASTERISM, ASTRAEA, ASTRAL, ASTRO-; ASTEROID, ASTRAPHOBIA, DISASTER, Sterope. 4, Iranian stem *s¢dr- in Persian sitareh, star: ESTHER. [Pok. 2. ster- 1027.]
1271:AUTOPSY OkW- AUXESIS aug-! AUXILIARY aug-! AUXIN aug-! AVAIL wal- AVAST  kel-3, past- AVATAR auc’, tera-? AVENGE deik- AVENUE gWa- AVER wéro- AVERT wer-3 AVIAN awi- AVIARY awi- AVIATION awi- AVICULTURE awi- AVIFAUNA awi- AVOCATION wekW- AVOID eu-2 AVULSE wel-4 AVUNCULAR awo- AWARE wer-4 AWAY wegh- AWE agh-1 AWKWARD apo- AWN ak-
1336:CASE2 kap- CASHIER kes-2 CASTE kes-? CASTIGATE kes-2 CASTLE kes-2 CASTRATE kes-2 CATA- kat-1 CATABOLISM gWele-1 CATACHRESIS gher-5 CATACLYSM kleu-2 CATALECTIC slég- CATALEPSY (s)lag¥- CATALOGUE leg-1 CATALYSIS leu-1 CATAMENIA mé-2 CATAPLEXY plak-2 CATAPULT pél- CATARRH sreu- CATASTASIS sta- CATASTROPHE streb(h)- CATCH kap- CATCHPOLE pau- CATECHIZE (s)wagh- CATEGORY ger-1 CATER-CORNERED kWetwer- CATERPILLAR pilo- CATHEDRA sed-1 CATHEPSIN kat-1 CATHETER yé- CATHODE sed-2 CATHOLIC sol- CATION ei-1 CATOPTRIC okw- CATTLE kaput CAUDILLO kaput CAUDLE kele-1 CAULESCENT kaul- CAULICLE kaul- CAULIFLOWER _bhel-3, kaul- CAULINE kaul- CAUSTIC kéu- CAUTERY kéu- CAUTION keue-1 CAVE keue-2 CAVEAT keue-1 CAVERN keue-2 CAVETTO keue-2 CAVIL  kel-8
1409:Dart dhabh- DAINTY dek-1 DAIRY dheigh- DAISY agh-2, okw- DALE dhel- DALLES dhel- DAMAGE dap- DAME deme-! DAMN dap- DAMNIFY dap- Dan? deme-! DANDELION dent- DANE dan- DANEGELD gheldh- DANELAW dan-, legh- DANGER deme-1 DaNIsH dan- DAPPER dheb- DARE dhers- DARK dher-! DASTARD dhé-2 DASYURE dens-2 DATE do- DATIVE do- DATUM do- DAUB _albho- DAUGHTER dhugheter- DAUNT deme-2 DAWN agh-2
1429:DIN dhwen- DINGUS _{enk-1 DINOSAUR dwei- DINOTHERE dwei- DIOCESE weik-! DIOECIOUS weik-1 DIOICOUS_ weik-1 DIOPTER oOkW- Dioscuri_ deiw-, ker-3 pip dheub- DIPHTHERIA deph- DIPHYODONT bheue- DIPLO- dwo- DIPLOCARDIAC kerd-1 DIPLODOCUS dek-1 DIPLOE dwo- DIPLOID pel-3 DIPLOMA dwo- DIPNOAN pneu- DIRE dwei- DIRECT reg-! DIRNDL tek- DISARM ar- DISASTER ster-3 DISBURSE bursa DISCERN krei- DISCIPLE dek-! DISCIPLINE dek-? DISCOMFIT dhé-1 DISCORD kerd-1 DISCOURSE kers-2 DISCRIMINATE krel- DIscuss kwét- DISDAIN dek-1 DISEMBOGUE beu-! DISFIGURE dheigh- DISGUST geus- DISK deik- DISMAL deiw-, mel-5 DISMAY magh-! DISMISS (s)meit(9)- DISPARATE pere-1 DISPATCH ped-! DISPEL pel-6 DISPENSE (s)pen- DISPERSE (s)preg- DISPLAY plek- DISPOSE apo- DISPUTE peu- DISQUISITION quaerere DISRUPT reup- DISSECT sek- DISSEMINATE 6-1 DISSENT sent- DISSERTATE ser-3 DISSIDENT sed-1 DISSILIENT sel-4 DISSIPATE swep-2 DISSOCIATE sekw-1 DISSOLVE leu-! DISSONANT swen- DISSUADE swad- DISTANT sta- DISTEND ten- DISTICH steigh- DISTINGUISH _ steig- DISTORT terkw- DISTRACT tragh- DISTRAIN  streig- DISTURB twer-! DITCH dhigw- DITTO deik- DITTY deik- DIURETIC wers-2 DIURNAL deiw- DIVA deiw- DIVARICATE wa- DIVE dheub- DIVERGE wer-3 DIVERT wer-3 DIvEs_ deiw- DIVIDE weidh- DIVINE! deiw- DIVINE? deiw- DIVULSION wel-4 Dizzy dheu-!
1486:EXxO- eghs EXOCRINE krei- EXODUS sed-2 EXOERGIC werg- EXONERATE en-es- EXOPHTHALMOS okw- EXORDIUM ar- EXOSTOSIS ost- EXOTERIC eghs EXOTIC eghs EXPAND pete- EXPATRIATE peter- EXPECT spek- EXPECTORATE peg- EXPEDITE ped-! EXPEL pel-6 EXPEND (s)pen- EXPERIENCE per-4 EXPERIMENT per-4 EXPERT per-4 EXPIATE pius EXPIRE spirare EXPLAIN pele-2 EXPLETIVE pela-1 EXPLICATE plek- EXPORT per-2
```


## [2026-09-07T20:21:24.467Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KLN accipiter ===\"; grep -n -i \"accipiter\" KLN_1966.txt KLN_1971.txt | head -6; echo \"=== KLN ocean ===\"; grep -n -i \"^ocean\\|ocean, n\\|Okeanos\\|Ōkeanós\" KLN_1966.txt KLN_1971.txt | head -10"
}
```


### [2026-09-07T20:21:24.550Z] TOOL RESULT

```
=== KLN accipiter ===
KLN_1971.txt:5442:Accipiter, n., a genus of hawks and falcons (orni- 
KLN_1971.txt:5443:thol.) — L. accipiter fr. orig. *acu-peter, ‘swift- 
KLN_1971.txt:21725:ML.,fr. L. acceptor , secondary form of accipiter , 
KLN_1971.txt:21726:‘falcon’ (see accipiter), whence also OSp. aztor , 
KLN_1971.txt:110590:the second element in goshawk. L. accipiter , 
KLN_1971.txt:169868:alteration of L. accipiter, ‘hawk’. See Accipiter 
=== KLN ocean ===
KLN_1971.txt:104971:ocean. — VArab. ghrdb , fr. Arab, ghurdb , 
KLN_1971.txt:165257:ocean, n. — F. ocean , fr. L. oceanus, fr. Gk. coxe- 
KLN_1971.txt:165262:Oceania, n., collective name for the Central and 
KLN_1971.txt:165265:Oceanid, n., a daughter of Oceanus; an ocean 
KLN_1971.txt:165268:Oceanus. 
KLN_1971.txt:165270:oceanography, n., that branch of geography which 
KLN_1971.txt:165277:oceanograph-ic-al, adjs. 
KLN_1971.txt:165279:Oceanus, n., 1) son of Uranus and Gaia, god of 
KLN_1971.txt:235445:ocean. — Formed fr. sub- and oceanic. See 
KLN_1971.txt:235446:ocean and adj. suff. -ic.
```


## [2026-09-07T20:21:35.440Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KLN accipiter full ===\"; sed -n '5440,5460p' KLN_1971.txt; echo \"=== KLN ocean full ===\"; sed -n '165255,165290p' KLN_1971.txt"
}
```


### [2026-09-07T20:21:35.542Z] TOOL RESULT

```
=== KLN accipiter full ===
ial, adj. 

Accipiter, n., a genus of hawks and falcons (orni- 
thol.) — L. accipiter fr. orig. *acu-peter, ‘swift- 
ly-flying’, but influenced in form through a con- 
fusion with accipere, ‘to take, receive’. The first 
element lit. means ‘sharp’ (cp. acu-pedius, ‘swift- 
footed’, lit. ‘sharp-footed’, and acuere, ‘to 
sharpen’) ; see acute. The second element is cogn. 
with OI. pdtram, ‘wing, feather’, Gk. 7rxep6v, 
‘wing’, OE. feder, ‘feather’. See feather. Cp. 
Astur, ostreger. 

Derivatives: accipitr-al , adj., accipitr-ary , n. (fr. 
ML. accipitrdrius), accipitr-ine , adj. 
accismus, n., feigned refusal (rhet.) — ModL., 
fr. Gk. 4xxta{z6q, rel. to 4xxt£ea&ai, ’to 
affect indifference’, and to ’A xxw, nurse of De- 
meter, 4xxo>, ‘a vain woman’, and cogn. with 
OI. akkd, ‘mother’, L. Acca Ldrentia, name of 
the mother of the 12 Arval brothers. All these 
=== KLN ocean full ===


ocean, n. — F. ocean , fr. L. oceanus, fr. Gk. coxe- 
avo?, ‘the great river encompassing the whole 
earth’ ; hence ’the great Outward Sea’ (opposed 
to the Inward or Mediterranean), which is of 
uncertain etymology. Derivative : ocean-ic , adj. 
Oceania, n., collective name for the Central and 
Western Pacific and its islands. — See prec. 
word and 1st -ia. Derivative: Oceani-an, adj. 
Oceanid, n., a daughter of Oceanus; an ocean 
nymph ( Greek mythol.) — Gk. *Dxeom<;, gen. 
’DxsocvcSos, fr. ’Qxeav6<; ‘Oceanus’. See 
Oceanus. 

oceanography, n., that branch of geography which 
deals with the ocean. — Formed on analogy of 
geography fr. Gk. taxeavdi;, ‘ocean’, and -ypa- 
<pta, fr. ypafpeiv, ‘to write’. See ocean and 
-graphy. 

Derivatives: oceanograph-er, n., oceanograph-ic, 
oceanograph-ic-al, adjs. 

Oceanus, n., 1) son of Uranus and Gaia, god of 
the sea before Poseidon ; 2) the immense stream 
supposed to encompass the whole earth ( Greek 
mythol.) — L., fr. Gk. , Qxeav6?, personifica- 
tion of o>xeav6<;, ‘the great river encompassing 
the whole earth’. See ocean, 
ocellate, oceilated, adj., having ocelli (zool.) — L. 
ocellatus, ‘having little eyes’, fr. ocellus , ‘little 
eye’. See next word and adj. suff. -ate, resp. also 
1st -ed. 

ocellus, n., 1) a little eye; 2) the rudimentary eye
```


## [2026-09-07T20:21:55.741Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== FSD which vol has p1707 ===\"; for f in FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt; do echo \"-- $f\"; grep -o \"^ *17[0-9][0-9] *$\" $f | head -3; done; echo \"=== FSD ocean ===\"; grep -n \"Ocean, n\\|ocean, n\\|G. ōkeanos\\|okeanos\" FSD_vol3.txt | head -10"
}
```


## [2026-09-07T20:21:56.530Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KNT leaf 179 (p.164) ===\"; python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor i in (178,179,180):\n    print('== leaf',i); print(t[i][:1200])\nEOF"
}
```


### [2026-09-07T20:21:57.071Z] TOOL RESULT

```
=== FSD which vol has p1707 ===
-- FSD_vol1.txt
1726
1780
1779
-- FSD_vol2.txt
-- FSD_vol3.txt
1708
1714
1728
-- FSD_vol4.txt
1770
1739
1793     
=== FSD ocean ===
2098:Ing Madeira and four others, In the Atlantic ocean, near the
11755:Ma^rennes', 1 maVen , 2 mi rin , «• A town aud commune ocean, near the coast of California, length, JO rn
35995:ft. Gulf of, an inlet of the Atlantic ocean, nearly enrlosed
48523:to the Atlantle ocean, near Cape Mondego.
```


### [2026-09-07T20:21:58.474Z] TOOL RESULT

```
=== KNT leaf 179 (p.164) ===
232
== leaf 178
 : hya : Dārayavauš : XS : руё : Haxdmanigiya : Mitra : mam : paluv
Nore то АНЬ: Probably the demonstrative imam stood before apadānam at the beginning, and other
155
phrases of the protective prayer may have stood at the end.
TRANSLATION oF Á?Hb: This palace, of stone in its column(s), Artaxerxes the Great King built, the son of Darius the King, an Áchaemenian. May Mithras protect me ...
A'Hc = Artaxerxes II, HAMADAN C. 1 baga : vazraka : Auramazda :hya : тайа : 2 baganam : һуа :imàm : bümim : ada : 3 һуа : avam : asmánam : ada : hya : martiya 4 m : айа : һуа : &y&tim : ада : martiyahy 5 & : hya : Artaxšaçām : XSm : akunaug : ai 6 vam : parünàm : XSm : aivam : parünàm : 7 framataram : ðātiy : Artaxšaçā : XS : va 8 zraka : XŠ : XSyinim : X8 : DHyünám :XS 9 : ahydya : BUya : adam : Darayavausahy 10 à : XShyà : риса : DarayavauSahya : Artax И Sacahya : XShya : puça : ArtaxSacahy 12 & : XSayarSahy3 : XShya : риса : Хау 13 arsahya : Dàrayavausahyà : XShya : p 14 uça : Dārayavaušahyā : Vištāspahyā : nā 15 ma : puça : Haxämanišiya :ðātiy : Artaxša 16 (à : XS : vagna : Auramazdaha : adam : XS :8 17 hyaya : BUyà : vazrak&yà : düraiy :a 18 piy : amiy : Auramazda : xSagam : manā : frába 19 r
== leaf 179
8. This is the Arab. 19. This is the Egyptian. 20. This is the Armenian.
21. This is the Cappadocian. 22. This is the Sardian. 23. This is the Ionian. 24. This is the Scythian across the sea. 25. This is the Skudrian. 26. This is the Petasos-Wearing Ionian. 27. This is the Libyan. 28. This is the Ethiopian. 29. This is the man of Maka. 30. This is the Carian.
A’Pa = ARTAXERXES III, PERSEPOLIS А, B, C, D. 1 Бара : vazraka : Auramazda : hya :' 2 упал : bümàm :adà : һуа :a 8 vam : asmünàm : ada : һуа : marti 4 yam : adi : hya : &yatàm : adi : mart ` 5 ihyà : һуа : mim : Агіахёаса : х$ауз 6 буа, : akunaus : aivam : parüvnàm :
[4
Т xšāyaðiyam : aivam : parüvnüm. 8 : framatàram : Вапу : Artaxsagà : 9 xšāyaðiya : vazraka : xsayaftya 10 :xšāyaðiyanām : хёйуабуа : 11 DHyünàm : xSayafiya : ahyàyà : BUyā : ada 12 m : Ártax faga : хёйуа | 13 буа : puça : Artaxsacd : Darayavau 14 š :xšāyaðiya : puça : Darayavaus : A 15 rtaxéacà : xSaya@iya : puça : ArtaxSa 16 cà : XSayarsa : хїйуайуа : puça : X 17 šayāršā : Dárayavaus : xšāyað 18 iya : puça : Darayavaus : Vistaspa 19 hyà : пата : риса : Vistaspahya : 20 ÁrSàma : пата : puça : Haxàmanisi 21 ya :08tly : ArtaxSacd : xSiyafh 22 ya : imam : ustašanā
== leaf 180
d: LX (units) in weight.
‚.. (= Wb ЕЎ).-
157
INSCRIPTIONS ON SEALS SDa = Darius, SEAL A: adam : Darayavaus XS SDb = Darius, SEAL B: adam : Dàrayavaus
SXa = XERXES, SEAL A: 1 X Sayarsa 2: ХБ : vazraka SXb = XERXES, SEAL B: 1 adam : X Say
2 агба : XS SXc = Xerxes, Seat c: 1 adam : Xšayāršā : XS D mure Sa = SEAL A: 1 Arša 5 yüba 2 ka :n 6 ušna à ата: 7 hyä: ‚4 Adi 8 puça Sb = Sear B: 1 Hadaxaya PNE EE 9 Вадаба, : ...
Sc = SEAL c: Vasdasaka
Sd = белі р: Vahyavisdipaya
Se = SEAL E: 1 ma : Xa 2 га 3 dašyā
Sf = SEALF:lupà 2 Arta 3xSac 44am Notes: Se: For Justi’s reading Xifyáráü, see Lex.
s.v. Xaršadašyā. Sf: There is no word-divider after upd. TRANSLATION. OF THE SEALS:
SDa: I (am) Darius the King.
SDb: I (am) Darius. -
SXa: Xerxes the Great King.
SXb~c: I (am) Xerxes the King.
Sa: Arshaka by name, son of Athiyabaushna.
Sb-e: ???
Sf: Under Artaxerxes.
Vase INSCRIPTIONS.
XVs = XERXES, VASE: XSayar 84 : XS : vazraka AVsa = ARTAXERXES, VASE A:
: Ardaxeakea : XS : vazraka AVsb-d = ARTAXERXES, VASES B, C, D: ArtaxSaca : xSayabiya
TRANSLATION: XVs: Xerxes the Great King. AVsa: Artaxerxes the Great King. -
AVsb-d: Artaxerxes the King.
158
OLD PERSIAN
HISTORICAL APPENDIX |
I. THE ÅCHAEMENIAN DYN
```


## [2026-09-07T20:22:09.220Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'LEXICON' in p.upper()[:2000] and i>150:\n        print('leaf',i, p[:300].replace('\\n',' | ')); \nEOF\necho \"=== search 164 header ===\"; grep -n \"^164$\\|^ *164 *$\" KNT.txt | head"
}
```


### [2026-09-07T20:22:10.588Z] TOOL RESULT

```
leaf 185 ugh not mentioned in the Behistan inscription, must have followed in the same or the next year. | V. THE ACCESSION OF XERXES. | In XPf, Xerxes gives us an account of his sue- cession to the throne: Darius had a number of sons, but—-as was Ahuramazda’s desire—he made Xerxes (presumably not his eldest son
leaf 186 � asn. DPd 20; DNa 53; XPh 43, 59; XSc 4°. ata- таш DPd 22; DNa 54; XPh 60. aitä apf. XPh 30, 35. | Ainaira- sb. ‘Ainaira’, a Babylonian, father of Nidintu-Bel; Elam. ha-a-na-a-ra, АКК. a-ni-ri-’, Ainaliralhya gsm. DB 1.77f. | atva- adj. ‘one’ ($150; §204.1): Av. aéva- ‘one’, Gk. Hom. olos, Cypr. orros 
leaf 193 t’). | - | LEXICON | ч. | Атах$аса- sb. ‘Artaxerxes’ (Т, son of Xerxes; П, son of Darius II; III, son of Artaxerxes II): Elam. ir-tak-Sa-a8-Sa, Akk; ar-tak-Sat-su, Gk. ’Aprakeptns (§29.n2, 530). From arta- ‘justice’ + т$аса- ‘kingdom’, ‘Having a kingdom of justice’ (hardly, with Nyberg, Rel. 352, ‘whose zša
leaf 195 's avabäštā adj. apm. 'thus standing". | avadà (ie. avadá) adv. ‘there, then’: LAv. атаба; from 'ava- + suffix seen in OP «dà (319.1). Usually resumptive of an immediately preceding place-phrase, which is thus made locative (so al- ways in DB except 1.85, 88; 2.24; 3.74; 4.81; 5.24, 28). See also avad
leaf 197 �; 4.33; DPe 7; DNa 16; DSe 15; DSm 5°; XPh 14. ima apf. DB 1.21; D$g 3°. | ima nsn. DB 1.27, 72; 2.01; 3.10, 20, 58, 76; 4.1, 9, 40, 49, 59; 5.2; DPh 4; ОМ 32; DSf 22; DH 3. ima asn. DB 1.25 bis, 26, 68; 444; DNb If; DSf 10; DS} 2°, 5°; ХРе 10f; XPd 16; XSa 1; Х8е 3°; XV 20; А:Ра 19°; D'Sb3?, 4°. imá
leaf 199  by Hz, ApI 71-2). | ufraSa- ufrasta- adj. ‘well punished": u- ‘well’ + pte. fraSta- or frasta- (893) ‘questioned, investi- gated? to root fraó-: pIE *su-prekto- (§33, 75, $242.II. — ufrasiam asm. DB 1.22, 4.66f; ufra&lam DB 438. ufrasa-diy apm. DB 4.69 (JAOS 35.351-2, ef. Bv. Gr. $845; not loc. ufras
leaf 201 to the wall alongside it (König, - Burgbau 32n; Hz. AMI 3.54-5, Ар! 224). katam nsn. DSf 25. | Katpatuka- sb. ‘Cappadocia’, a province of the Persian Empire; also, as adj., ‘Cappadocian’: Elam. ga-at-ba-du-qa, Akk. ka-at-pa-tuk-ka, Gk. Каттодокіа. ($93.11). | (1) ‘Cappadocia’: Katpatuka nsm. РВ 1.15f; D
leaf 212 fnu, Lt. јеси ‘made’, NEng. do, deed, pIE *dhe-. See also wadd-, data-,ddna-. айайй imf. (§209, 5228.1) DPd 8; DNb 1, 2; DSe 2°, 3°, 3f, 4. ada aor. ($62, S76.TIT, $122, $218.II, $228.IT) DNa 2, 3 bis, 4; DSf 1f^, 2 bis, 3, 9; DSp 2°; DSt 2°, 3, 3f°, 4°; DZe 1, 2 ter; DE 3, 4, 5, 6; XPa 1f, 2, 3 bis
leaf 214 Hz. Ap! 136-8) nsn. as sb. ‘handiwork’, DSe 42. | Daha- adj. ‘Dahian’; pl., a province of the Persian Empire: АКК. da-a-an, Gk. Aaa (§76.V; Lg. 18.298; Hz. AMI 8.72). Dahà npm. XPh 26. | dahyu- sb. ‘land, province, district’: GAv. : | daltyu-, LAv. dahyu- daiphu-, NPers. dih ‘village’, Skt. ddsyu- ‘strang
leaf 216 e 15; DZe 10. drayahya lsn. ($136, §251A; wrongly taken as gen., Hz. АрІ 141-3) DB 1.15, DPe 14, DSe 28°; drayahiyà ($27) XPh 23. | naiy adv. ‘not’: Av. 207, РЫ. në, Skt. ned; : | from pIE *ne, Skt. na, Lt. ne-scio ‘I don't know’, -+ Эа, asn. of pron. i-, Lt. id, OP id-am, ete. (869, 884, $191.1, $291.1
leaf 218 with Justi, IFA 17.107, ‘Pasargadae’, from paisiyd- ‘writing’ + "wüdá- ‘abode’ (572, §89, §126, $127, $142, §166, 5160.1): ‘Home of the Archives and Sacred Writings’ (on Pasargadae, ef. also Kónig, RuID 66; but Hz. ApI 275-6, modifying his view ш AMI 1.86n, takes prior element to be pati-, pati- bec
leaf 227 ion), Lt. mort-uos (after vi-vos ‘liv- ing), pIE *mrios ($80, $109, $122, §242.1); see OP mar-, and cf. Hz. АрІ 249-51. тапа пзш. XPh 48, 55. marlahyá gsm. РВ 5.20, 36. | EU: ET TORR ON | | INS SEE cals la pen X AN, ae ete. ЫЗ, Ses f. Av m ee Sm SN Ie e mne - | LEXICON 203 | ‘martiya- adj. as sb. ‘man’: -iz
leaf 229 d sg. opt. mid. ($223.II, $284.1I) XPh 50. yadiyaiša” (8220, 5228.11, 4282.101; written 11924, $5.1; cf. Hz. AMI 8.67, ApI 357-8) 3d pl. opt. pass. (Ogden ap. JAOS 58.325; not yadiyatš 2d sg. opt. mid. with Wb. Symbolae Koschaker 196, nor fut. pass. with Hz. AMI 8.67, ApI 357-8) XPh 39. | lwadé- conj.
=== search 164 header ===
136:164
4907:164
```


## [2026-09-07T20:22:19.602Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"okeanos\\|ocean\\|keanos\" KNT.txt | head; echo \"=== leaf 193 ===\"; python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[193][:1500])\nEOF"
}
```


### [2026-09-07T20:22:20.935Z] TOOL RESULT

```
4912:а adv. as prefix and prep. ‘to’; Av. Skt. à, prep. with acc. and abl., ‘to, as far as’ (also with other uses and meanings); pIE *à if = Lt. à ‘from’ (Sturtevant, Lg. 15.145-54), or *0 if = Gk. ó- in ó-xeayós ‘(lying round about), ocean’.
=== leaf 193 ===
t’).
-
LEXICON
ч.
Атах$аса- sb. ‘Artaxerxes’ (Т, son of Xerxes; П, son of Darius II; III, son of Artaxerxes II): Elam. ir-tak-Sa-a8-Sa, Akk; ar-tak-Sat-su, Gk. ’Aprakeptns (§29.n2, 530). From arta- ‘justice’ + т$аса- ‘kingdom’, ‘Having a kingdom of justice’ (hardly, with Nyberg, Rel. 352, ‘whose zšaça- de- rives from aría-); imitation of Xšayāršā, acc. -üm, explains the long vowel of the ultima in the nom. and acc. ($78, §161.[b; decl, §172, $187). Artazšaçã nsm. А:Ра 9°, 17°; АЧ; D'Sb 3°; A’Sa 1; A’5b; A*8c 1°; А4 1, 2; А? На 1; A*Hb; Ае 7, 156; A*Pa 5 (as acc., 52476), 8, 12 (as gen., $313.IT), 13 (as gen.), 14f (as gen.), 15f (as gen.), 21, 231; AVsb-d. — Ardaxcasca ($49; or -Sda) AVsa. Arlax áagüm asm. АІРА 51°; А%8а 4; A?He 5; S£ 2-4. ArtaxSacahyé gsm. D'Sb 2°; Artaxíafrahyà (Tm. Lex. 54) A?Ha 2f, 3; Arlazíagühya ($53) A’Sa 2 bis; A?He 101, (аз nom., 5313.1) 11.
ariàvan- adj. ‘righteous, blessed’, denoting the blissful state of the true religionists after death: identical with Av. asavan- ‘characterized by Arta or Asha, righteous’, Skt. rldvan- ‘true to sacred Jaw’ (cf. Hz. Ар! 289-93); from *ria-, OP arta-, with lengthened final vowel, + ad]. suffix -van- ($30, $155.IV). атара nsm. (8124.5, $187) XPh 48, 55.
Artavardiya- sb. ‘Artavardiya’, one of Darius’s generals: Flam. ?r-du-mar-ti-ja, АКК. ar- ta-mar-2i-ja. From arta- + vard- ‘to work’ + adj. suffix ($80, §31, §144.1V, S160.Ia): ‘Doer of Jus- tice’ (not from vard- ‘to increase’, Skt. vardh-, be- cause of -z- in АКК.
```


## [2026-09-07T20:22:28.328Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\ntxt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\n# char offset of line 4912 (1-based)\noff=sum(len(l)+1 for l in lines[:4911])\nleaf=txt[:off].count('\\f')\nprint('line 4912 is in leaf',leaf)\nt=txt.split('\\f')\nprint(t[leaf][:600])\nEOF"
}
```


### [2026-09-07T20:22:29.659Z] TOOL RESULT

```
line 4912 is in leaf 185
ugh not mentioned in the Behistan inscription, must have followed in the same or the next year.
V. THE ACCESSION OF XERXES.
In XPf, Xerxes gives us an account of his sue- cession to the throne: Darius had a number of sons, but—-as was Ahuramazda’s desire—he made Xerxes (presumably not his eldest son, though this is not stated in the inscription) the ‘greatest after himself; and when Darius ‘went from the throne,’ Xerxes—as was Ahuramazda's desire—became king on the throne of his father.
The account given by Herodotus 7.1-4 agrees with this, but gives more details: After Darius re- ceived the n
```


## [2026-09-07T20:22:37.757Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '4895,4925p' KNT.txt | cat -n | head -40"
}
```


### [2026-09-07T20:22:37.801Z] TOOL RESULT

```
     1	TEXTS WITH NOTES AND TRANSLATION
     2	Uvadaicaya, and Darius executed them with tor- ture (§43). Darius was now back in Persia, which had been restored to his rule (§44), as well as the other rebellious territories except Egypt and Scythia. It was not quite nine months since he had slain the usurper Gaumata.
     3	But while Darius was putting down the rebel- lions in Media and in Persia, an Armenian named Arkha, claiming to be Nebuchadrezzar son of Nabonidus, had established himself as King in Babylon (§49). Against him Darius sent a Persian officer named Intaphernes with an army, and Intaphernes routed Arkha and his forces on VIII 22, capturing and executing at Babylon both Arkha and his chief officers (§50).
     4	This is the latest event related in the first three
     5	163
     6	columns of the Behistan inscription, 13 months and 12 days after the death of Gaumata; the time does not seriously exceed the one year which Darius boastfully mentions m Column IV.
     7	Column V gives an account of a third rebellion in Elam, under Atamaita; against him Gobryas was sent with an army by Darius, and he defeated and captured him, bringing him to Darius, who put him to death (§71). The date of this rebellion seems to be in the third year of Darius’ reign, 520/19,5 though the Behistan text is here badly mutilated. After this rebellion in Elam Darius went to Seythia and defeated and captured Skunkha (§74). The reconquest of Egypt, though not mentioned in the Behistan inscription, must have followed in the same or the next year.
     8	V. THE ACCESSION OF XERXES.
     9	In XPf, Xerxes gives us an account of his sue- cession to the throne: Darius had a number of sons, but—-as was Ahuramazda’s desire—he made Xerxes (presumably not his eldest son, though this is not stated in the inscription) the ‘greatest after himself; and when Darius ‘went from the throne,’ Xerxes—as was Ahuramazda's desire—became king on the throne of his father.
    10	The account given by Herodotus 7.1-4 agrees with this, but gives more details: After Darius re- ceived the news that his forces had been defeated at Marathon and somewhat later that Egypt had risen in rebellion, he started preparations for one campaign against the Athenians and another against the Egyptians. Àt this time there was a dispute between Artobazanes, eldest son of Darius by his first wife, a daughter of Gobryas, and Xerxes, eldest son of Darius by Atossa, daughter of Cyrus the Great, whom Darius had married
    11	after his accession to the throne, as to which should have the succession. On the advice of Damaratus, exiled king of Sparta, Xerxes went to his father and pressed his claim on the ground that he was the oldest son of Darius the King, while Artobazanes was only the oldest son of Darius the private individual. Darius approved the claim, though perhaps the argument was not really needed (Atossa as daughter of Cyrus must have had great influence with Darius, and Xerxes was probably the ablest of Darius's sons), and named Xerxes to succeed him. Before he had finished the preparations for the campaigns, Darius died; whereupon Xerxes ascended to his father's throne.
    12	5 Kent, JNES 2.109-10 ; cf. R. A. Parker, AJSLL 58.373-7. $ Parker, l.c.
    13	164
    14	PART III. LEXICON
    15	This Lexicon includes a concordance to the words in the inscriptions, as well as materials for etymological comparison.
    16	The alphabetic orderisáf dk zgejt6 edn pfo тутіоѕ §zh, while final y and v are disregarded (thus пату has the alphabetic place of nai, and pre- cedes naiba-). Raised letters inserted to show sounds omitted in the OP system of writing also have no effect on the alphabetic order.
    17	References to Part I (the Grammar) are marked by §; they include all mentions of the word or form which add to the information given in the Lexicon, but are not in all instances complete list- ings. The Chapter on Syntax is only sparingly re- ferred to in this Lexicon, since the citations in that Chapter are mostly for passages rather than for words; there is an Index of Passages at the end of the Chapter.
    18	а adv. as prefix and prep. ‘to’; Av. Skt. à, prep. with acc. and abl., ‘to, as far as’ (also with other uses and meanings); pIE *à if = Lt. à ‘from’ (Sturtevant, Lg. 15.145-54), or *0 if = Gk. ó- in ó-xeayós ‘(lying round about), ocean’.
    19	(1) Prefix with verbs ay-, zšnav-, gam-, grab-, jan-, bar-, mà-, yam-; in verbal nouns dyadana-, dvahana-, and in the second parts of compounds Adiyabaukna-, Ariyáramna-, Bagabigna-, also in Akaufaciya-.
    20	(2) Postposition attached to loc. sg. and pl. ($270.1V) and in conj. yada.
    21	(3) Prep. with abl.: yàtà à ‘as far as’, DPh 6, 7; DH 5, 6.
    22	(4) Prep. with adv.: DSe 48.
    23	! a- neg. prefix before consonants (867, 67.1, 0182.1; an- antevocalie, q.v.): Av. Skt. a-, Gk. a~, Lt. ?n-, Сте. un-, pIE *n-. See akarta-, ax áaina-, axsata-, Anümaka-, ayaumani-.
    24	* a- demonst. ‘this’: Av. a- as in GAv. gsm. ahé, Skt. a- as in gsm. asyd, Gk. lsn. є 40, Lt. nsn. tod in ecce ‘lo’; pIE *e-. See also aciy, ada-. Decl., $199.
    25	anã ism. DPe 8 (not to Av. Skt. ana-, cf. Mt. MSLP 19.49-52); XPa 14 (with Wb. KIA 109, Mt. Gr. $326; translated by АКК. a-ga-’, Elam. hi ‘this’, which refutes interpretation of Bv. Gr. $368,
    26	$388, as prep. w. inst. ‘throughout’, Av. ana with ace. ‘along, on’, Gk. дра 'along. ahyāyā lsf, DB 447; DNa 11; DSd 2°; DSe 10; DSf 7, 15; DSg lf; DSi lf, 4; DS} 1°; D8m 5°; D8s If, 3°; DSy 2; DZb 3; DZc 5f; DE 17; XPa 8f; XPc 7; ХВ 12, 24; XPh 9f; XPj; XV 13; A!Pa 13; РЬ if; Аа 1; Ае 4; A’Sdb 1 (ahyd de, $52.VI) ; A?Ha If; А°Не 9, 16f; А#Ра 11; Wb 6; We 7f; Wd 7. ahiydyd ($27) XPb 17; XPd 12; XPjv; XE 17.
    27	aita- demonst. ‘this’ ($260. IIT, $266): Av. адіа-, Skt. elá, PAr. *айа-. айа nsn. ($202) DB 1.44, 45; DNa 48. aita-maty DNb 31. ай�� asn. DPd 20; DNa 53; XPh 43, 59; XSc 4°. ata- таш DPd 22; DNa 54; XPh 60. aitä apf. XPh 30, 35.
    28	Ainaira- sb. ‘Ainaira’, a Babylonian, father of Nidintu-Bel; Elam. ha-a-na-a-ra, АКК. a-ni-ri-’, Ainaliralhya gsm. DB 1.77f.
    29	atva- adj. ‘one’ ($150; §204.1): Av. aéva- ‘one’, Gk. Hom. olos, Cypr. orros ‘alone’, pIE *ozyos. ашат, asm. DNa 6, 7; DSe 6°, 6f; DSf 4, 5; DE 8f, 10; XPa 4, 5; XPb 8f, 10; XPe 4, 5; XPd 6, 7; XPf 6, 7; XPh 5,6; XE 9, 10; XV 7, 8; A!Pa 6f°, 8°; A?He 5f, 6; А?Ра 6, 7.
    30	aiš- vb. ‘hasten’, caus. azSaya- ‘send’: Av. aes-, caus. aéaya-, Skt. 15-, caus. esayatz (§117).
    31	fra + aiš- caus. ‘send forth’: Av. fraei-, Skt. .
```


## [2026-09-07T20:22:50.482Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== TAD oqyanus ===\"; grep -n \"أوقيانوس\\|اوقيانوس\\|أقيانوس\\|اقيانوس\\|قيانوس\" TAD.txt TAD_pages.txt | head -10"
}
```


### [2026-09-07T20:22:50.553Z] TOOL RESULT

```
=== TAD oqyanus ===
```


## [2026-09-07T20:22:52.512Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== FSD3 ocean ===\"; grep -n -i \"ocean\\b\" FSD_vol3.txt | grep -i \"gr\\.\\|Gk\\.\\|swift\\|ōkeanos\\|okeanos\\|L. oceanus\" | head -10; echo \"=== FSD3 okys ===\"; grep -n \"okys\\|ōkys\\|ökys\\|wkus\" FSD_vol3.txt | head"
}
```


### [2026-09-07T20:22:52.604Z] TOOL RESULT

```
=== FSD3 ocean ===
=== FSD3 okys ===
```


## [2026-09-07T20:22:58.349Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(json.dumps(d['TAD'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['FSD'],ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-07T20:22:59.773Z] TOOL RESULT

```
{
 "title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640",
 "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt"
 ],
 "page_offset": "86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image",
 "covers_etymology": true,
 "notes": "Arabic OCR fair. Nourai's exact edition unknown; the Beirut reprint reproduces the 1932 pagination."
}
{
 "title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)",
 "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/in.ernet.dli.2015.147439",
 "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt",
 "page_offset": "vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.",
 "notes": "Nourai cites 1940; page numbers in the New Standard were stable 1913-1940s (single-volume pagination 1-2814 continues across the DLI volumes). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt, /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol2.txt, /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol3.txt, /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol4.txt",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol2.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol3.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol4.txt"
 ],
 "cites": "page number of Funk & Wagnalls New Standard Dictionary (1940)"
}
```


## [2026-09-07T20:23:04.967Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('FSD_vol3.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor i in (240,241,242):\n    p=t[i]\n    print('=== leaf',i,'first 200:',p[:200].replace('\\n',' | '))\n    import re\n    for l in p.split('\\n'):\n        if 'cean' in l or 'ocean' in l.lower():\n            print('   >',l[:300])\nEOF"
}
```


### [2026-09-07T20:23:06.464Z] TOOL RESULT

```
leaves 698
=== leaf 240 first 200: tm | OceftmlStn K*t l; arUitlc, art; tet, fire; fftut; get« priy; hit, police; ob^, fi; nat, ir; full, rOla; but, bOm; final; inhabit, rm&m | Ocliroma KET*;llrt, ipe, fit, fire, fiit, wb^^t, nil; mi, git,
=== leaf 241 first 200: 17t9 | Kit 1: «Me;«i « out; all; IQafaud; dhln; so; Jat; q aBBlnfr: lo; ihlp; Chin, ttila; asure; F. bo&,dllne; r ss loch, t, obtolete;t* variant. OCCUHtSIII | Kit 8: bdhk, bdht; t«ll, rule, cQre, bOt, bh
   > as, the ocean lane Hoe oceanimihaphy
   > a. greyhound, figuratively, a fast ocean-line steamship.—
   > or possessing an ocean or oceans o'rean-fnl, n An
   > amount equal to the supposed contents of an ocean-basin
   > o'reon- wards;.— o'cean-wlse, odr By the way of the
   > ocean o'rean-waynt. [seat, Toms River.
   > o'eean-ad, n. hot An ocean plant
   > inhabiting Oceania, or to their languages. 11- ri A
   > native of Oceania O^ce-mn'I-cunt-
   > |K*rtaining to tlio ocean or an ocean, as, an oceanic
   > an ocean in exioiit or immensitv. as, an utranic trade
   > as. an oceanic fish. 4. [O-] Ooeaman f < L. ormnus;
   > cipeclallv . the iHlaiuls of Oceania
   > (IK) I Or. 0\raniif'>. d ve'ur bv the ocean, < Okeonoi:
   > pare continental! rv [An ocean formation
   > o^cean-on'ra-plijr, 1 6*5hen-og'rt»-fi , 2 ft’shuu-fig'ra-fv ,
   > ocean. -f-aRAeiiY l—dynamleoeoanography, the bran ‘hof
   > oceanography that tn*aui of the motion of wuvisi, causes of
   > tides causes of ocean currents, forniuiluii of Isiaiids, etc
   > — static n.« the branch of oceanography that treats of
   > OCEAN>, 1
   > of oceanography o'^eean-o-grapli'l-cai;.— u'^roan-o-
   > 1. The scMTin* that treats of the ocean. 2. A trea-
   > tise on lh»' ocean oervN -P -loijy.)
   > ocean plant oei’uiiud ( < o( nan 4- phyian, plant 1
   > of the ocean (river oldest nf the Tlluris. liuslmiid of
   > lectively oompose the great ocean, oommunly enumer-
   > Quantity; aa, oosang uf air. tossed on an ocean of doubts
   > [OF , < L scsomM. < Gr Meeanos, ocean, perhaps < Meys,
   > of the gHByi HeUbaue. Uvlng on the suifaee of the ocean.—
=== leaf 242 first 200: ochronosus K*t l: ortlitlc, art; fat, fSre; fust; get, prSy; hit, police; obey, gO; not, Sr; fall, rOle; bat, bOm; okIIiioI; mbablt, ronoir; | Odadnss KsTSiart, Spe, fSt, fSre, fSst, what, all; m«, git,
   > Pamlico sound. North Carolina, to the Atlantic ocean, 26
```


## [2026-09-07T20:23:16.818Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('FSD_vol3.txt',encoding='utf-8',errors='replace').read().split('\\f')\np=t[241]\nls=p.split('\\n')\nfor i,l in enumerate(ls):\n    if 'scsomM' in l or 'Meeanos' in l or 'Meys' in l:\n        print('\\n'.join(ls[max(0,i-6):i+4]))\n        break\n# also head of leaf for page numbers\nprint('---- numeric lines:', [l.strip() for l in ls if l.strip().isdigit()][:10])\nEOF"
}
```


### [2026-09-07T20:23:18.141Z] TOOL RESULT

```
lectively oompose the great ocean, oommunly enumer-
ated as the Arctic, the Antarctic, the Atlantic, the Pa-
dfle, and the Indian t distinguished from a eea. For area,
etc . see these words
8, Fiijuratively, any unbounded expanse or indefinite
Quantity; aa, oosang uf air. tossed on an ocean of doubts
[OF , < L scsomM. < Gr Meeanos, ocean, perhaps < Meys,
cwift.1 — •'aenn«ba*sin, a A sunken part of the surface
of the earth eontalalng aa oeean. as. the oesaa-ftoMa of the
Atlantic.- o.>bnnltn, a A fish (Oymnoearda petaimtsi
---- numeric lines: ['7', '10', '55', '7', '100']
```


## [2026-09-07T20:23:23.230Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor i in range(6,14):\n    print('=== leaf',i)\n    print(t[i][:1200])\nEOF"
}
```


### [2026-09-07T20:23:24.483Z] TOOL RESULT

```
leaves 87
=== leaf 6
‫معاه أخبار تارمحية وقد استعمابا العرب ععى‬           ‫اساطير ‏ بوناني ‪8‬‬
                                                            ‫خرافات وحكابات‬
                                     ‫استبرق ‪ -‬فارسي معناه الديباج الغديظ‬
                                   ‫اسرب ‪ -‬فارسي «سيرب» معناه رصاص‬
        ‫إسطيل واصطيل ‪ -‬لاتيني ‪#‬دااناطهاة معناه مأوى الخيل والدواب‬
‫خا لان | رانم كن من ‪ 807653‬أى ك كب وهلاةطه‪:‬ذا أُخذ وكان‬
 ‫الفلكيون القدماء يعرفون حركة الكوكب مبذه الآلة ويعينورن موضعه‬
                                                             ‫ويعيسون ارتقاعه‬

                       ‫يونالي تاواع ‪ 1015‬معئاه عنصر وأعيل‬     ‫ب‬
                                                                      ‫د‪5‬ي‬
                                                                        ‫‪95‬‬

                    ‫معتأد عله حربية وطائفة سفن‬      ‫اسطول ‪ 8-3‬وناني ‪8‬‬


‫ملدابةمرادفهمودوقابمة‬
                    ‫اسطوانة ‪ 5-3‬فارسي ‪ 0‬أستون « هماه دعامة وقوات ا‬


                                                            ‫ايضا فيالطبيعيات‬
‫نحري جسمه متخلخل‬          ‫اون‬
                            ‫و وه‬
                               ‫ينعصر‬
                           
=== leaf 7
 ‫إرفج ‪ -‬تعريب علتهة؛ الجرماني الذيمعناهحر" وهوالسشمعب غرني‬
‫جرمانيا الذي دوخ غاليا سنة ‪ 584‬ومماها داعمه؛ ‪,‬ععده‪ :‬فدخل هذا الاسمإلى‬
                                               ‫بلادنا إبان الهروب الصليبية‬
 ‫معمخورائط ب يوئاني ‪ 52114‬وهو اسملجار حامل الكرة الارضية‬        ‫طلس‬
                      ‫فارسي < أفراز‪ 6‬معناهمرتفععربيهطنف‬         ‫ار‬

 ‫إفسنتين ‏ ووناني دا غمزومج معناه لاذع وهو ثبات ورقهكورق الصعتر‬

                                                                 ‫راطم‬
                                ‫افندي ‪ -‬نري ‪ 0‬اذنذئ م‪6‬عتأة السداك‬

  ‫يك ‪ -‬في اللائينية دامه وفي اليونانية وامه معناه مائعوهو عصارة‬
                                                                 ‫الخشخاش‬
                                ‫ل‬
                                ‫قو‬‫تزن‬
                                    ‫اقة في اليونانية معاعه معناه و‬

‫اكسيحين س يونا مرك من ولودة أي حائض ومن مفعفه» أي واد‬
  ‫استياك ‪ -‬ايطالي معتاهداه معناه ممطوط في الأصل البوناني ويراد به حذاء‬
                                                    ‫مخصوف بالمادة الممعلوطة‬

  ‫امام يوناني ‪520‬هلة معناه غير مروض مرادفه السامور وهو عند‬
  ‫الاقدمين حجركر أمافيزماننافا كتشف انهعنصر الفح املمتب
=== leaf 8
                             ‫|قنوم ارامية ‪ 9 72‬قَدُوما ‪ 4‬معناه الشخص‬
 ‫في الفارسية ل‪2‬نكر» وفىاليونانية اله عرببها المرساة والموجل‬           ‫اجر‬

 ‫جيل يوناني‪#‬وألعههدوع (إوتجيليون )معناه خير بشارة وبشرى فرح‬
‫(نكليس ) عريها الجرى‬
                   ‫نقليسوحتكلس ‪ -‬يوناني ‪59‬ا‪600‬ي» إ‬
                                                               ‫والثلقوالصباور‬
        ‫هنا أراعى « عرب » أايلغرب‬
                                ‫صلةلولك‬
                                      ‫أجتا‬
                                         ‫اوريا ‏ ايطالي ‪#‬مه‬
                                ‫اوضة ‪ -‬ري وله يشارف عدر‬
‫أوقة‪ 5‬في اللددينية ‪3‬ن وفي اليونانية ‪#‬أعاىتاه براد مهاجزاء من|ثنيعشر‬

              ‫معناه مربع وعربية اليحر البط‬      ‫داتع يوناني ‪56‬‬

‫اوكاريستيا واوخاريستيا يوناني ‪2‬ناوذوداءنظا معناه نعمة وشكر أحسن‬
                                                        ‫وبراد به القريان المقكدس‬
                     ‫‪,‬نصاغوجي ‪ -‬يوناني ‪ ©8808351‬معناه مدخل وتوطئة‬

 ‫ارشّونة وقونة ‪ -‬يوناني ‪ ©7001‬معناءصورة وشبه ومثال وكثال أما نصمة في‬


‫ايطالي قجلاعناا‪ 61‬معناه لغة نفوذ وفي الطب هوالبلنمالوبابي‬          ‫إيتفاونسا‬
                                      
=== leaf 9
                                    ‫‪5‬‬

                                 ‫درن »‪6‬‬

           ‫بايا في اللاتينية همهم وهو تضعيف أب مقلوبا أي بايا‬
‫(كوين‬
    ‫ل الارض ت‬   ‫كسا‬
                  ‫نلل‬‫بأبللى ‏ دعي اسمهابابللان الرب هناك بلب‬
                ‫« بابيلو » أيباالباله‬   ‫ووت‬
                                          ‫نيةحفب‬
                                               ‫مشور‬
                                                  ‫‏‪ 4:١‬أ)مافي الا‬
‫يابج ‏ فارسي « بابوش » معناه غطاء الرجل وهو داس يلبس في الرجل‬
                        ‫باور ‪. 7‬يطالي عنندمة؟ معناه مخار امدرفه بآخرة‬

‫بواتبم ‪ -‬فارسي « بابونه » وحهشيشة ذات زهر أصفر مكلل بأبيض‬
                                                              ‫يتداوى بها‬
‫بادزص جافاريق عركن من بادأي ضد وزهرأي سم وهو حجر نحمله‬
                                                                 ‫الدجالون‬
‫باديجان ‪ -‬في الفارسية « بادينجان »‪ 6‬نقل الى الاسبانية ‪2‬مئمعمه‪ 8‬ومنها‬
‫الى الافر نسية ‪#‬هنعروطناة ثاملى الايطالية ‪5‬ةنهده؛وم ويقال له في الايطالية‬
‫أيضا هسةتدداءه» و «داعنت في اليونانية معناه اسود فنظر بعضيم الى ظاهر لنظه‬
‫ففسره « بيض المان أو ابن الجنينة ‪ 4‬أما أصل هذا النبات فههنودي فيكون‬
            
=== leaf 10
                                 ‫م‬‫ميه‬
                                    ‫م ل‬




‫وممامدم أي قاس وهو‬
                 ‫مكب م‪6‬ن‪ 5008‬أي قل د‬
                                   ‫باروسيرت يوناني ر‬
                                           ‫تستعمل لنرقة قن الوا وطذعاه‬
‫بارون ‪ -‬ايطاني مهن أصله من لغة جرمانيا ااقديمة ةط ومعناه رجل‬
‫حر كان يتولى قدي أراضي الامراء اعا هو الآن لقب شرف دون الكونت‬
                                                       ‫وهوآخر الالقاب‬
           ‫باز وبازي ‪ -‬فارسي عر بيهالصقر والعقاب واللاعة والحياقية‬
                                                 ‫اسايق ب ينا‬
     ‫وني مه لتههطا معناهملكيوهو لقب لعرق في الذراع‬
  ‫جرل ومن شاه أي ماك وسلطان‬
                          ‫باشا‪ -‬فارسي مركب من باأي لدم و‬
  ‫| باشق ‏ فارسي « باشه » وهو طائر أصشر من العقاب مرادفه يؤيو وج‪1‬م‬
‫بال ايطالي دادم معناه رفش وعربيه قملب ‪:‬قلب به الارضللزراعةأما‬
                        ‫رويب ‪ 8:585‬الابطالي وهومجرفة منحلية '‬
                                                            ‫عفه‬
                                                              ‫تمر‬
                                                                ‫ال‬
‫بال وبالة ‏ لاتيني ‪806‬هلده مناه 
=== leaf 11
                                                              ‫عت ات‬


 ‫بأميا ‪ -‬نبات له قرون تطبخ أصله من أهريكا الحو ببة واسمه هناك هطتترمع‬
 ‫و ‪40362‬دمع وعرنوه ياميا لويتئوه ‪1‬اناء وأطل! أي غاذق إزجة وهو من قصيلة‬
                                                                                                                          ‫الخعامي‬

                                                        ‫‪-‬مي « بير ب»راد به هعنردي‬    ‫ار‬‫يفبر‬
                                                 ‫بيغاء ‏ أصل هذا الطائر من الهند واسمه هندي‬
                                 ‫موف المفسول‬
                                           ‫من‬‫لم‬
                                              ‫ايج‬
                                                ‫بت ‪ -‬فارسي ‪ 0‬بت © وهو نس‬
               ‫مول ‪ 0‬ايطالي وتامماءم معناه زيت الحجر والنفط يستخرج منه‬

                ‫وبراد بهترميل من حشسب‬                          ‫دن اليونانية نا‬                  ‫ايطالي ‪06‬‬             ‫بثية ب‬


                                                                   ‫نخت ‪ -‬فارسي « مخت ‪ 4‬معناه حظ‬
                                       ‫‪5‬‬           ‫‪5‬‬                              ‫‪5‬‬          
=== leaf 12
                                 ‫عت اب‬


                                ‫رجيس ‪ -‬اسمالسيار لمشئري بالفارسية‬
 ‫ايطالي ‪ 35618200‬معناه سثر الباب أصله فارسي « برده (أي ‪5‬‬       ‫رداه‬

                                                           ‫وسجف وغطاء‬
‫ريد ‪ -‬فارسي دن ردن أي دل وهومذكورفيسفراستيروكان مستعملا‬

 ‫قبل ‪5‬ال‪626‬؟ اللاتيني الذي أنشاهاو عوطس لنقل الرسائل وفى الايطالية ‪8150‬م‬
                                                        ‫وقد عرلوه بوسطة‬
                    ‫برد س حامية‪ --‬تركي « برداخ » أي صل وجلا‬
                                   ‫ردي ‪ -‬مصرية وهو نبات كالقصب‬
                    ‫معناه زائر كنانمي”‬       ‫ودبوط ‪ -‬يوناني ‪7‬‬
             ‫رذعة ‏ ارامية ‪ 9‬بروّعتا » أي حلسالدابةمرادفه وكاف‬
            ‫دون ‪ 53‬لانيني مه ‪,‬روك قاط أي كل ابوهحصان وآية ائان‬

            ‫“رشان ‪ -‬ارامية «فريستا» أي قرصة تصنم املندقيق الابيض‬
                 ‫برسام ‏ فارسى مركب من راي صدر وسام أي المهاب‬
                                                  ‫رشت ‪ -‬انظر برشت‬
‫رطاش ‪ -‬عامية مأخوذة من ‪ 82:61:00‬الايطالية ومعناها ستر البابوعر بها‬
                                                            ‫أسكدَّة الاب‬
                                 
=== leaf 13
                                        ‫ك‬
                                        ‫ح ‪:‬و‬
                                           ‫تبن‬


      ‫ركي‪ -‬عامية ‏ فارسي « بملكرىوبالكدهف»ها لويعحلثمل أن‬
                          ‫رميل ‪ -‬ايطالمي ‪ 11:35‬وهو وعاء مستدير من خشب‬


                   ‫َ‬

                ‫وهو التعة‬          ‫برنيطة ب ايطالى ممتااع معط اوم ‪0‬‬



‫معناه ورقة ملصقة بالسجل وبراد به‬        ‫لظ بير نعطي‪6100‬م‬               ‫بروتوقل‬


                                  ‫السجل الأول والمحضروبيان الجلسات السياسية‬
                         ‫ببزار ‪ 3301‬فارسي « بازدار » أي حامل البازي أ الباز‬

‫معناه الحاصل قدام‬         ‫ايطالي ‪2121502‬م من اليوناني ‪56‬‬              ‫بروسطاتة‬

                       ‫وعربيه خائقةالمثانوةهي غدة محيطبعنقامثانةكزيق القميص‬
                            ‫فارمي ‪ 0‬بازيار ‪ 0‬أي الأكار أوالفلاح‬         ‫سار س‬


                                              ‫ديا » أي الثدي‬            ‫‪0‬‬
         ‫معناه جواز المربى مرادفه جواز‬          ‫ايطالي وم‬                ‫‪00‬‬

                         ‫وببكفي وتحاب"‬
                                     ‫بن "‪1‬س لنظفازبيبرادفهكتىو‬



  ‫و"ر‬
    ‫ب مر‬
       ‫وناها‬
```


## [2026-09-07T20:23:42.426Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/ref_page.py --help 2>&1 | head -30"
}
```


### [2026-09-07T20:23:43.812Z] TOOL RESULT

```
Fetch ONE cited page of a scanned reference, on demand.

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
```


## [2026-09-07T20:23:52.661Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"المحيط\\|اليحر\\|قيانوس\\|وقيان\" TAD.txt TAD_pages.txt | head -10; echo \"=== raw leaf8 line ===\"; python3 - <<'EOF'\nt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor l in t[8].split('\\n'):\n    if 'يوناني' in l and ('عربي' in l or 'بحر' in l or 'يحر' in l): print(repr(l))\nEOF"
}
```


### [2026-09-07T20:23:54.095Z] TOOL RESULT

```
TAD.txt:257:داتع يوناني 65 معناه مربع وعربية اليحر البط 
TAD.txt:2512:فى اسيا الصغرى على ساحل اليحر الاسود وثقله الى رومية القائد أ كولو 
TAD.txt:3142:2 قاموس محيط المحيط تأليف الملم بطرس البستانى طبع يبروت 
TAD.txt:3144:1 قطر المحيط ل تأليف المع ارس البستاني جرّءان طبع ييروت 
TAD_pages.txt:272:              ‫معناه مربع وعربية اليحر البط‬      ‫داتع يوناني ‪56‬‬
TAD_pages.txt:2380:‫فاىسيا الصغرى على ساحل اليحر الاسود وثقله ارلوىمية القائدأ كولو‬
TAD_pages.txt:3010:               ‫قاموسمحيطالمحيطتأليفالملمبطرسالبستانىطبعيبروت‬                ‫‪2‬‬
=== raw leaf8 line ===
'              \u202bمعناه مربع وعربية اليحر البط\u202c      \u202bداتع يوناني \u202a56\u202c\u202c'
```


## [2026-09-07T20:24:13.126Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; for f in BQT_v3_pages.txt BQT_v4_pages.txt BQT_v5_pages.txt; do echo \"=== $f\"; grep -n \"کسک\\|کشکک\" $f | head -8; done"
}
```


### [2026-09-07T20:24:14.485Z] TOOL RESULT

```
=== BQT_v3_pages.txt
995:کسب علم وهتر کند » کسکه در مدرسه تحصیل داش کند » متملم ۰ ‎aul‏ - کسیکه در ‎ap‏
21998:۴ - عریی است « قوة کسکر » رونای .*
23318:‎erry‏ ۷ - قرقوب بالضم » شهری بود يين واسط وصره و اهواز , ازاعمال کسکر
24452:قمرون خوانند . « ابن‌الببطار : اریان *. ۴ - ‎(Ge)‏ > قمل بالفتح. سپش... قمل کسکر»
26674:کاکره - بکسکان‌رفتح رای بی‌قطه,
32040:‏۱ -«کسکه . غلیه بود ‎Gade gen‏ » محمودی گوید:
32529:‏8 = کشیخان . عر « کشخان کسکران (بفتخ) و یکسر 1 زن جلب و بی‌غیرت در حق
=== BQT_v4_pages.txt
3281:قرشت » بوزه را کوبند و آن چیزیت مت هز کت ۸ - بنتح اول وکسکاف فارسی
6289:‎٩‏ - درعربی * میدان کسکران » ویک » فهومقمال من‌الودن » صفحهٌ زمین بی‌عمارت-
12834:آدیاین گوبند وشهر آن اربل نام داشت ) » اشکن ( کسکر ). رك : فیسی . تاریخ نمدن ابران
22204:‎٩‏ (ص) «بقم کسکر, درخت جوزمائل» «منتهی‌الارب» «بقم جضم با ونشدید قاف و فتح
=== BQT_v5_pages.txt
```


## [2026-09-07T20:24:14.878Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== MON parts: ahu ===\"; grep -n \"آهو\" MON_part1.txt | head -5; echo \"=== MON oqyanus ===\"; grep -n \"اقیانوس\\|اقیانوس\" MON_part1.txt MON_part2.txt | head -5; echo \"=== MON kasak ===\"; grep -n \"کسک\" MON_part1.txt MON_part2.txt | head -5"
}
```


### [2026-09-07T20:24:14.997Z] TOOL RESULT

```
=== MON parts: ahu ===
5449:اهمند: 0صعص ماع [ آهومند] (ص‌مر.) 
5550:چشمان زا است؛ غرال» ظبی؛ ج. آهوان» 
5551:آهوها. 
5553:آهو: 1 (.) عیب» نقص. بسماری» مر ض. 
5557:آهوان»چون آهو. 
=== MON oqyanus ===
MON_part2.txt:8031:رفقره» به دو فتح بجز اقیانوس و معیار اللغه 
MON_part2.txt:27941:در سواحل دریاهای گرم (اقیانوس هند و : 
MON_part2.txt:38067:اقیانوس‌های بزرگک می‌زیند و تا ٩۰۰‏ يا 
MON_part2.txt:42025:و در نواحی گرم اقیانوس کبیر و اقیانوس 
MON_part2.txt:43609:می‌رسد و در سواحل اقیانوس اطلس فراوان 
=== MON kasak ===
MON_part1.txt:42904:تکذ: ۱۵۷8 [- تکس - تکسکل ‏ تکسیز - 
MON_part1.txt:78614:سکسک: 0۲۵0۶: (ا.) زمین ناهموار و 
MON_part1.txt:78635:سکسک: (۰)هامعاده [ع. سکسکَ] 
MON_part1.txt:78638:کتک ته: (م-) 12 ک(ع5 [ع. سکسک] 
MON_part1.txt:78642:سکسکی : ]-20:0 (.) زحمتی که انسان
```


## [2026-09-07T20:24:19.786Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '5540,5575p' MON_part1.txt"
}
```


### [2026-09-07T20:24:19.844Z] TOOL RESULT

```
اهنین پنجه: (م-)دلصوم-. (ص‌مر.) قوی 
پنچه پر زور» بر فوت. 

اهو: 25 (.) (جاند.) جانوری از خانوادة 
تهی‌شاخان» جزو راستة نشخوارکنندگان که 
اقسام مختلف دارد و توا دوتة سار 
سریع و چابک و دارای دست و پای بلند و 


چشمان زا است؛ غرال» ظبی؛ ج. آهوان» 
آهوها. 

آهو: 1 (.) عیب» نقص. بسماری» مر ض. 
(ص.) بد» ناسند. 

افته انسه: (0-)200۷-202 (ق.) مانند 
آهوان»چون آهو. 

اهوپای: .5 [- آهوپا] (ص‌مر.) (معم.) 
بنا با خانه آهو پای. خانه شش پهلوء خانه 
ضلمی. 

اهسوتک: 2.1 (ص‌مر.) مانند آهو در 
دوندن» آهو دو. 

آهوجه: .2 (ص مر .) آنکه جهشی چون 
آهو دارد» جهنده مانند آهو. 

آهودل: 5-44 (ص‌مر.) ترسنده: شتردل؛ 
گاو دل» بزدل. 

اهومند: 20 (ص‌مر.) مر بض» سمار» 
آهمند. معیوب» اقص» مختل» آهومند. 
آهون: 0 (.) رخنه و راه و مجرایی که 
زیر زمین حفر کنند» نقب» سمج) اهون.
```


## [2026-09-07T20:24:33.140Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HRN nisan ===\"; grep -n \"niSän\\|nišän\\|nisan\\|nišān\" HRN.txt | head -15; echo \"=== HUB nisan ===\"; grep -n \"nišän\\|nisan\\|niSan\" HUB.txt | head -10"
}
```


### [2026-09-07T20:24:33.207Z] TOOL RESULT

```
=== HRN nisan ===
=== HUB nisan ===
```


## [2026-09-07T20:24:34.133Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; grep -n \"آهو\" ARY_pages.txt | head -8; echo \"=== nishan ===\"; grep -n \"نشان\" ARY_pages.txt | head -8; echo \"=== latin index ===\"; grep -n -i \"AHU\\|NESHAN\\|NISHAN\" ARY_latin_index_pages.txt | head -8"
}
```


### [2026-09-07T20:24:34.227Z] TOOL RESULT

```
8747:۲- هلت دگرگرنی چم این واژه در زبان‌های ایرانی این است که پس از ظهور زرتشت و آئین او "آهورامزدا" مورد
13275:۲- در اوستایی "گوش" و آهوش " هم چم بوده‌اند.
15575:در پهلوی این واژه هم به چم "یاد" و "حافظه" و آهوش" بوده و هم به چم "نیرومند"» آقهرمان".
=== nishan ===
14:هدف این کتاب نشان دادن ریشه‌ی هند و اروپایی واژه‌های فارسی ناب است. این هدف موجب
27:۴- برای نشان دادن خویشی زبان‌های هند و اروپایی و ریشه گیری آنها از یک سرچشمه‌ی
118:هند و باختر اروپاگسترش داشته باشد. ۲- بررسی‌های اغیر نشان می‌دهد که زبان‌های هند و اروپایی
122:اروپانیان از حاشبه آاز شده باشد. ضمناً دیگر قرائن نشان می‌دهند که زبان‌های هند و اروپائی این
188:یک پژوهش اخیر (مجله‌ی 861221678 جلد ۳۰۰ صفحه‌ی ۵۹۹ ۲۵ آوریل ۲۰۰۲) نشان
200:گسترش سریح قبایل ترکك نشان می‌دهد که سرعت تهاجم و تصاحب می‌تواند :
257:گهواره به سوی خاور و فلات ایران و هند) مضاقاًنشان می‌دهند که مکان جغرافیابی این زبانها در دو
286:آن. بررسی واژگان هند و اروپایی و شواهد تاریخی و اسطوره‌ای و باستانشناسی نشان می‌دهد که ۱
=== latin index ===
2777:éss AHU-, AHURA, —(AVESTAN) gl)
2975:BOG (OLD ENGLISH) oy pnts! BAHUH, BAHUS
3134:BRUG (DUTCH) gala BRUR, BAHU — (SANSKRIT) ca Si
3910:VESELS LATVIAN) (35) 393 VAHU
7490:‘TRE :(OLD SCANDINAVIAN) oS Sahu!
8266:DEIDEMON, DEIMOS, DEILOS DUSHAHU <(OLD PERSIAN) inl .go\
9625:AMINDAROY: (POISON) 269 ‘ZHAHR, ZHAHUR (ARMENIAN) ¢s,!
10942:FOUNDEN :(OLD ENGHISH) oS lSsi JUHOTI, AHUTIS
```


## [2026-09-07T20:24:41.428Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HRN Gazelle ===\"; grep -n \"Gazelle\" HRN.txt | head; echo \"=== HRN Zeichen entries ===\"; grep -n \"'Zeichen\" HRN.txt | head -20"
}
```


### [2026-09-07T20:24:41.507Z] TOOL RESULT

```
=== HRN Gazelle ===
974:59. ähu 'Gazelle*.
975:phlv. ahük 'Gazelle'.
=== HRN Zeichen entries ===
```


## [2026-09-07T20:24:47.023Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '965,990p' HRN.txt; echo \"=== leaf/page ===\"; python3 - <<'EOF'\ntxt=open('HRN.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\noff=sum(len(l)+1 for l in lines[:973])\nleaf=txt[:off].count('\\f')\nprint('leaf',leaf,'-> printed page',leaf-21)\nEOF"
}
```


### [2026-09-07T20:24:48.355Z] TOOL RESULT

```
sie gefangen und ai. i^sanj- *hängen* passen nicht, doch
soll np. ahenjiden auch Verfen* bedeuten ^. Np. aheng
'Plan, Absicht* wird ebenfalls hierhergehören. Des-
gleichen np. ferhe/teiiy ferhi/ten^ ferdhi/Un (phlv. fra-
hä/Jan 'erziehen etc., frasäxtan, AV., sind nur fraJtä/tun
zu lesen), die ebenso wie berhe/ten^ berki/teu 'ziehen,
herausziehen* und 'erziehen bedeuten sollen; vergl.
ferheng, ferhenj 'Wissen etc.' (phlv. /raAaw^, Nöldeke,
Kärn. 38; arm. LW. hrahang), ferhenjukn 'erziehen.
59. ähu 'Gazelle*.
phlv. ahük 'Gazelle'.
kurd. ask; afy, ösai; bei. äak (19), LW. aü (15); ya/.
LW. ahü.
60. äyem 'ich komme*, äyende.
ap. *el + l^«y- ; päz. ü^d, aend {üyad, äyand),
kurd. e/w, ei, et etc. (Justi, Gramm. S. 235, Houtum-
Schindler, S. 103); bei. äyag^ n. ay (21); wa/. ni-ytt
(3 Sg.).
61. äytn 'Sitte, Schmuck*, äJTw-); aöme^ adme 'Freitag*.
phlv. ädlnak, ay\i\nak 'Sitte, Gewohnheit'.
Wohl zu ö + i^dai- (ai. {^dhai-) wie die folgende
Nummer (die aw. und die ai. Wurzel stimmen übrigens
in der Bedeutung nicht scharf zu einander). Eine äi-
Wurzel ist anzunehmen nach Bartholomae, ZDMG.
43, 665.
Fr. Müller's Erklärung in der WZKM. IV, 355
=== leaf/page ===
leaf 36 -> printed page 15
```


## [2026-09-07T20:25:09.384Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'].get('scans'),ensure_ascii=False,indent=1))\nprint(d['BQT'].get('page_offset'))\n\""
}
```


### [2026-09-07T20:25:10.823Z] TOOL RESULT

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
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
```


## [2026-09-07T20:25:17.099Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; python3 - <<'EOF'\nimport re\nfor f,target in (('BQT_v3_pages.txt',445),('BQT_v4_pages.txt',226)):\n    t=open(f,encoding='utf-8',errors='replace').read().split('\\f')\n    for p in t:\n        m=re.search(r'\\[pdf page (\\d+)\\]',p)\n        if m and abs(int(m.group(1))-target)<=1:\n            print('=====',f,m.group(0))\n            print(p[:1800])\nEOF"
}
```


### [2026-09-07T20:25:18.443Z] TOOL RESULT

```
===== BQT_v3_pages.txt [pdf page 444]
[pdf page 444]
-1۱1۵۱-

وجابه ‎Lub‏ و اشارت را نیز گفته‌اندا .
کشف = ‎ce‏ اول و ثالی وسکون فا »
‎SY‏ پشت ‎ob,‏ پشت را کویند؟ - وبرج‌سرطان
را نیز ‎oT, ala”‏ برج چهارم است از ‎he‏
‎oil‏ برج فلکی؟ - و کوزة سریهن دهان ‎CD‏
‏باشد ‎lade LT,‏ هم میگوبند - و نم کوهی
‎ath‏ و بعربی کوه را جبل گویند (۱) - و بضم
اول و سکون ثالی, بمعنی سیم و نقر# سوخته
وسواد زرکری؟ ‏ - وزفت بآشد که برسر کچلها
چبانند ۴ .
شفت * - بنتح اول و انی وسکون
الث وفوقانی » بمعنی برا کنده و پربشان باشد
و ماضی ‎GET‏ هم هست یعتی پراکنده کرد
‎olen,‏ ساخت و پژمرده گردالید ؛ و بضم ‎Jal‏
‎gl,‏ هم کفته‌الد - وم اول و کسرثالی؛ عبات
خانه و معبد بهودان را گوبند .
‎cae geht‏ اول والی بروزن‌شنفتنه

(۱) چش : - وبسبی ... گویند .

بمعنی کشردن ۱ - وشکافتن و پراکنده ویربتان
کردن ویژمرده شدن و معدوم گردبدن باشد ۷؛
و بفتح اول وثالی هم‌آمده است .

کشفته * ‎pee‏ اول ‎JE»‏ بر وزن
شنفته , بمعنی پرشان ویر کنده و پژمرده شده
وسوخته ومعدبوم گردیهه باشد ؛ ویفتح اول وثانی
هم‌آمده است .

کثف 8399 ‎b=‏ رای بی‌قطه‌بروزن
نمك‌سود » نام رودخانه‌است که ‎pple‏ لریمان در
حوالی ‎oT‏ اژدهاییرا کشت .

HSB agit ‏بنتح اول و سکون‎ - CEST
‏وبتر کی قروت‌خوانند؛‎ Vash ‏شده‎ cles ‏دوغ‎
‏ازماست‎ LST ‏ویسی کوبند نان خورشی است که‎
‏می‌پزند ؛ و بسنی گویند. طمامی باشد معرو ف که‎
‏ازآرد گندم وآرد جو و شی رگوسفنددرست‎ LST
‏ازآنرا گوشت و گندم لیزداخل‎ AG ‏میکنند و‎

میازند و مالند ‎doe‏ میخورند - و بفتح اول

۱ کش ( نم اول ) بممتی قتل و کشتار است : « سبب ترول اين ‎ay OT aT‏ که .
مصطفی ص کافرالرا شکسته بود و کشش وفارت کرده ...» ( مولوی بلخی رومی . فیه مافیسسحح
فروزانفر ص۲). .۰ ۴ - اوستا - 62838۳8 ( سنگه پشت ) با (خرچنگه ) ؛ ساسکربت
- 6861622 ( سنگگ پشت ) » بلوچی 68610 « استق ‎۸۵٩‏ ۰ , افنانی ‎kshap‏ > هوبشمان
‎CAV‏ 2

چون کثف اببوه غوغائی بدید بانگه وژخ مردمان » خشم آورید.
«درودکی سمرقندی. نفیسی. ج ۳ ص ۱۳۸۶ >
کثف دید طالم خداوند ماه .

فردوسی طوسی « رشیدی * .

‎Say ۴‏
===== BQT_v3_pages.txt [pdf page 445]
[pdf page 445]
وثالی پیمنی ‎Ke‏ باشد ‎OT, ٩‏ پرندهء‌است ‎ah‏
‏و سفید که عربان ‎Gale‏ خوانند - و بمعتی خط
هم‌آمده است خواه بردیوارکشند و خواء برروی
کاغذ ۳ - ‎ging‏ اول وسکون انی, مخفف کوتك
است که بالاخانه باشد ۴ .

کشکاب ۴ » بر وزن میتاب : آش‌جو
را گون دکه بجهت بیمار پز ند .

کشگاو * - بسکون ‎aly‏ بروزن‌ومعنی
کشکاب است که آش جو باشد .

کشکبا 1 ه بفتح اول و سکون ‎gt‏
‏و الت و بای ابجد بالف کذیده , آش حلیم را

کشکر لك ۷ - بارای قرشت ‎Os»‏
‏احمدك, پرنده ای
است سیاه و سفید
که ‎RA Lat‏
‎aS‏ و عربان
‎Gate‏ خوانند .

کشکشان.

بروزن حهوشان۸ ۰

۰ agli \ lad 0

Vere

مخقف کشان کشان است که کنابه ازآهسته و
بتألی‌براه رفتن ‎lps‏ بردن ‎th‏

کشکله م بر وزن مشفله ؛ نوعی از
‎ch‏ افزار باشد که شاطران و پیاده روان بر پای
کنند ‎٩‏ .

کشکنجیر ‎athe‏ اول ۱۴و ثالث
وسکون ثالی و نون و جیم بتحتال ی کشیده‌وبرای
قرشت زده » چیزی باش دکه بکشیدن ‎OT‏ ارمان
و آرزری کمان کشیدن حاسل شود و ‎OT‏ چنان
است که ستونی برزمین فروبرند و سرآنراشکافته
غلطکی برآن قرار دهند ورسمانی بربالایغلطك
اندازت و ازآن شکاف ‎asl aS‏ و از يك سر
‎clas vey‏ را پر از منک ‎Sy,‏ کرده
بیاویز ند و بر مان ‎OT‏ ستون قبضه مانندی‌صب
کنند ‎KS‏ خواهد مشق کمانداری کندبدست
چپ ‎OT‏ فبضه را بگیرد و بدست راست سر ‎OT‏
‏رسمان را ود ر کشا کش آورد(۱) وآنرا بثیرازی
منجل و پعربی مجیر و بهندی منجر گویشد -
یمعنی فلاخن هم آمد» است - وم ‎Sal‏ توپ
کلاترا میگویند که بدان دبوار قلمه را سوراخ
کنند و ‎ans,‏ و خراب سازند و بعضی کویند

۱ س«کس‌که» ‏ کشکرك (ه.م.), قس ‎-Karshiptan_ toy)‏ پهلوی ‎karsh(ift‏
‏(مفهوم ‎oF‏ واخح لیست) » وخی ‎karjbpe‏ « سریکلی ‎kshebe gas ۰ karjope‏ ( زافی ,
کلاغ زاغی ‎(JT) Elster=(‏ « استق۷ه ۰ عم )4( = ‎magpie‏ ( انگ ).

۴ ۳ کشه (ه.م.) و ‎nh‏ معنی در دساتیر هم‌آمده « فرهنگگ دساتیرص*۲۹*.

۴ رگ : کوشکه. معرب ‎OT‏ هم «کشك» ‎Sy‏ : اقرب الموارد . المنجد .

۴ - از :کشکه + آب ح کشکاو , خورشی که از کشکه وآب و روغن و مسالح‌دیگر

ea) ‏کتتاب‎ 2 ay

-
===== BQT_v3_pages.txt [pdf page 446]
[pdf page 446]
--1۵۳-

‎UIT‏ توپ است ؛ و ‎gene‏ دیگ رکویند سنگی
باشد که در منجنیقگذارند و پرحصار الدازند با
بر خصم ‎Vas‏ و وجه ‎has‏ آنکوشك‌سوراخ
کننده باشد چه کشك مخفف کوشكث است‌وانجیر
‎me‏ سوراخ هم‌آمده است ۲ .

‎GES = FO‏ نفد کشکینه
است که نان جو باشد ؛ و بعض ی کوبند ‎Babb‏
‏که ازآرد جو و آرد ‎WL‏ وآرد گندم وآردنشود
مجموعه را بپم آمیخته خمیر کنند و بپزند ؛
و بعضی دیگر گویند کندم بربان است که‌درظرفی
کنند و ماهیابه درآن ریزند و ییاز خام و ساق
چقندر و ‎phi‏ خرفه درآن داخل کنند ودرآ فتاب
گذارند تا ترش گردد .

‏کشکو ؟ - بر وزن بدرو ۵ ‎wie‏

‎OS‏ که آش جو باشد - ‎thy‏ مرغی هم

‏هت ‎Le‏ وسقید که ‎oT‏ را عکه خواند .

‏کشکول = بروزن مقبول » بسنی کدا
باشد یعنیشخصی که کدایی کند - وکاسة کشکول
کاسة کدا را گویند ۷ و ععنی ت رکیبیآ نکشیدن
بدوش است چه کش بممنی کشیدن و کول دوش
وکتف را کرد و با کداییکننده این معنی
هست - وکاسه‌ای را نیز گویند که کدامان دارند
- و آنچه مشهور است ظرفی باشد که ۳ براباندام
کشتی سازند .

‏کشکهای پر توه = بفتح اولوثانی»
بمعنی خطوط شماعی است چه کشك بمعنی خط
باشد و پرتو بمعنی شعاع .

‏کشکهی ‎٩‏ » بر وزن بروین » بمنی
اول ‎ET‏ است که نان جو باشد - و الیرا نیز
کویندکه ازآرد ‎WL‏ و نضود ‏ و کندم وجودرهم

‎: ‏که کشکنجیر غیر از منجنیق است‎ WL, ‏انوری‎ ce gil - ٩

‏نه منجئیق بسقفش وسد نه کشکنجیر

‏نه تیرچرخ ونه سامان برشدن بوهق.
* انوری چاپ لبریز ص ‎ANYE‏

‎: ‏کشکنجیر ثیر میانداختند‎ Slee ‏منوچهری‎ ce oul

‏داد جشن مه رکان امپهید عادل دهد

‏آن کجا تنها بکشکتجیربندازد زرنگ (خدنگه) .

‏? منوچهری ص4۸٩‏ .

‏و از ‎So bed‏ نیز همین ‎er‏ برمیآید. رلد: فرهنگه نظام ‎GUT.‏ مینوی نوشته‌اند: کشکنجیر
بعنی سوراخ ‎BET‏ کوشك . ‎OT)‏ نوعی ازآلات قلمه کشابی بوده است که بدان سنگپای کلان
با تبرهای بز که وستبر بدبوار قلعه با باروی شهر پرتاب ‎her Cae‏ واز ضربت آن‌دبوارسوراخ
و خراب میشده است ‎J).‏ : تعلیقات نوروزنامه ‎۱۲٩ oe‏ - ۱۳۰ .

‏۴ رك : الچیردن . ۴ - مخفف « کشکینه » (هم.) .

‎kashkaw -
===== BQT_v4_pages.txt [pdf page 225]
[pdf page 225]
یرم ۱1۳
نسیرم۱- بتح اول و رای قرشت فسیله ؟ - بتح اول بروزن‌وسیله, کله
وسکون میم » بمعنی‌سراست وآن جایی‌باشد که | ورمةٌ اسب و استر وخرباشد ؛ وجشم اول هم‌آمده
آفتاب برآن کمترتابد - و تابدان را هم کفته‌اند ۱ است -
وآن روزنه‌است ازخانه که يك جالبآ ترا پارچه من ۴ - بنتح میم بروزن رسیدن .
چبانند و نقاشی کنند ؛ و بسنی کوبند یرم ۱ بلفت زند و پازند (۱) عبادت او نماز کردن را
جایی است که پیوسته‌آفتاب برآن تابد» اّاعلم. | کویند .
بیان دواز دهم
در نون با شین نقطه‌دار مشتمل بر چهل ودو لغت و کنایت
فش ۴ - بختح اول وسکون ثالی»بممنی ههر شاپور چه ده بفرس قدیم شهر را کوبند -
سایه وسایه گاه باشد که جای‌سایه است؛ ویمعتی و نام شبیه‌ای هم‌هت از مقام نواکه به‌نیشاپورك
۰ 5 ۹ مشهور است.
سایةکلاء ‏ هم نش آمده است . تشاخت ‎٩‏ -بروزن عنام ,سد
نا بکر اول و.ثانی بالف کشیده . امه ی
: ما اشاختن باشد که پممنی نشاندن است یمتی شاند
لفط است که ارا ببریی شامل میگویند یکی و اشانید - و بمعنی تعیین (۳) هم آمده است
میم - وشاسته را هم‌کفته‌اند که از آن‌الوده | که خبر دادن وآشکارا ماختن وخاسکردانیدن
رل ۳ باشد .
نغاپور ۸ (۷) ۰« بکراولامشهرست نشاخَقن « بروزن ومعنی شاندن‌باشد*۱
مشهور در خراسان و اسل‌آن نه شاپوراست ,بمنی - و بمعی تعیین کردن هم آمده است ۰۱۱
() چك ژند وپاژند . [ خم۱: نشابور - (۳) چش : تعین .
- سروری بنفل از فرهنگه میرزا ابراهیم و مود الفضلاء بدین معنی آورده » قس :
سر دار ." ۴ - مصحف « قیله » (.م.) ورك : چغار مقاله طبع دوم نگارنده ص ۹4
ح (۰)۸ ۴ - هز . (22512)82 ۰ پهلوی 82۳020 ( نماز ) ۶« پونکرص ۷۹ *.
۴ -قی :ضا. -اظ . ممحف « سایه‌گاء >
۹« شا بکراول ترجمةٌ شامل ومحتوی > « برهان جامع >.
۷ - در عربی نشاسته راکوبند . ر4 : تفی . « نشاستج » عوالذی پسمیه‌الجمعورالنشا +
و باليوتانية آملون و آمتولون.» «عقار۲۹۱». كلم نشا نام عمومی و معمولی نشاسته درمصراست <
0 (فر ) : عقار ۲۹۱ ق؟ . ۸ -ر4 : یغابور .
‎٩‏ -رك : شاختن. ۴ ناستن (ه.م.) ۶ هوبشمان ۱۶۳۷ « اسشق ۰۱۶۳۳
قی : ساسن ؛ و رك : شاخیدن :
ز دوستی بدل و دی
===== BQT_v4_pages.txt [pdf page 226]
[pdf page 226]
۱8۳۳ عاسن
تغاخقمه ۱ - بر وزن شاسته , بیمتی |[ - وامر پتغاندن هم هت پعنی پنغان ۸ -
تشانیده - و تعیین کرده شده باشد ۴ . و نشانده را نیز کفه‌اند که فاعن٩‏ شاسن باشد؛
نغاخیدن ۴ < بروزن ومعنی شاسن و باین معنی بجز 0 ۱
وتعیی نکردن باشد . رک در خر ی ۹
نشاده - بکس اول بروزن آشاره,چوب ی کگ 0
پوسیده را گوبند که مانند آرد شده باشد . و َ ی
نشاستن ۳ < با سین بی‌قطه ‏ بروزن و سنکنجبین ۸/
صفرا اشان وشیرة 4۱۵۱
ست نید اد 9 سیش 0
تشاد « بفتح اول‌بروزن علاك, بل | - و بمعنی هدف ب‌
زند و پازند (۱) بمعنی شکر باشد که از آن‌حلوا ونشانةٌ تیر وتفشکه ان
وچیزهای دیگر پزند . هم‌آمده است .
نشغان ‎٩‏ « بکسر اول بر وزن نهان » نشغاندن *۱- معروف آمت۱۱- وومعنی
بممنی‌علامت باشد۷ - وحصه واسیب رالیز کوبند. | نهادن هم‌هنت ۱۴
(۱) چك : ژند و پاژند .
3 یی
۱- اسم مقعول از « نشاختن > (ه.م.) ۲ - بنمثی * نب کرده و نشالیده ومعین
و مقررگشته > در دساتی رآمده « فرهنگه دسانیر ص۲۹۹ 1 ۴ -عاختن (همم.)
۴ - ناختن (ه.م.) » قی : نشاندن ؛ و آن متمدی نشستن (۸م.) است » در پهلوی
02 اسشق ۱۶۳۲ . و ر4 : دارمتتر . تتبعات ج ۱ ص ۰۲*۷
۰ الل4ف9 هزواری برای 512687 ( شکن ) «یوتکرص ۲:۹۱
‎٩‏ - پهلوی 2150 «در کلمتّمر کب 8158 - 17327۷ (نگپبان مرغان) ».از-081[288
از-850 - 081 . دراوراق مانوی تورفان 8513180 ۳ 81250200 ( خواهند دید)یپودی-
فارسی 8958218 ۰ و درلهجد‌ها -81813 ( نگاه کردن ) ؛ ایرانی میانه 315128 » فارسی‌فشان»
ارمنی ع 8190 از 02180 و 85028 , از 818088 (علامت ۰ نعان) ‏ قس: اوستایی-۸87۳91
- 2۳58 - 218۷1 نظارت کردن « پارتولمه ۰۳۹۰ « نیب رک مس ۶۱۶۷ ۰ کردی 8181080 »
اقا (علامت . شانه ) « ژاباا ی ۶۲۰ > ۰ معرب ان « دزی ج؟ اس ۹۷۶ * و یشان «دزی
اضا »۶ تفی >. ۷ - ۵« (وزبر )گفت : ای پادشاء ؛ نشان خردمند کافی جزآن نیس ت که
بچنین کارها ( امثال وزارت ) تن در ندهد . > «گالتان صس ۳۳ -
۸ رد4 : شاندن . ‎٩‏ - اسم فاعل هرخم. ۴ از: ش اندن (پوند
مصدر متعدی) » متعدی لشتن (ه.م.) ؛کردی نژبنین 81201018 ( تیف کردن » دیوا رکنیدن)
« ابا س 4۱۹ *. ۱-کی
===== BQT_v4_pages.txt [pdf page 227]
[pdf page 227]
بفاستن -ع ۱2
نشالستن ۱ - با سین بی‌قطه, بروزن بمعنی خراب و ضایع و است و پژمرده و زبون
و ممنی شایدن باشد . باشد - ویک اول‌بمعتی‌خوش وليك 9 .
قشپل ؟ - بنتح اول وبای ابجد بروزن مر ۱ < بروزن مخت , مخقف لبشتر
مشمل , بمعنی دست پرچیزی زدن و درآوختن است که‌آلت فد کردن حجام باشد .
باشد - و بمعثی دو چیز را بر هم دوختن و بهم لُشْهَن ۴ « بروزن رشتن » مخفف‌نشستن
چبایدن عوهت . ح
فشپهل - بکس اول وسکون ثالی وبای تشن چون خالك ‎٩۸‏ - کدایه از
ابجد بتختانی کشیده و بلام زده , مطلق لاب نشتن با کمال حلم و آرام و همواری باشد -
را کوبند عموماً و قلاب واشست ماهی گیری را و کنایه از خوار و زار و سر افکنده نشستن «م
2 همست .
خصوصا - و بفتح اول هم باین بل . نشقق « بفتح اول بر وزن نکرو » دام
معتی وهمآ لتی‌باشد مانند قلاب هردی بوده است .
که باآن خرما از درخت فرود سیل نشتی ‎٩‏ - بکسر اول بر وزن زشتی .
میآورند ۴ . ۱ بممنی خوش ولیکی باشد چه نشت بمعنی خوش
نت ۴ < بفتح اول‌وسکون‌انی‌وفوقانی» | وليك است و خوشی و لیکی- بمعنیلچوی وچه
ی یبای ببس
۹ ۳ نساستن » (هم.) :
کنو ن که بداستم چندانکه تواستم مهر تو نشانتم . از مات سلامالط +
مولوی بلخی رومی « فرهنگه نظام ».

۲ -ظ . مصحف « تنعل > (ه.م.) ۴« تعییل . شت ماهی شد پعتی دام .

منجيك ( ترمذی ) گوید :
ای ماهی زرین و بمه بر زده شپیل دبرست بباغ آدر برزرین قندیل. >
لغت فری ص ۰.۳۱۵

۴ - درخراسان 32501 بممنی‌زرد است. گویند : « انگور قدری نشت شده » نیز پارچهٌ
نیم سوخته را که از نزديك کرفتن با آتش زرد شده « نشت »کوبند « فرهنکه نظام > » طبری
0 ( جل . کهنه و پوسیده ) «واژه‌نامه ۶۷۵۹ ؛ درگیلکی 325111 بمعنی چین‌دار و تاشده
( کاغذن , جامه وغیره ) است؛ دراراك ( سلطانآباد ) زمین نرم ( مانند زمین باغجِه که خوب بیل
زده و کلوخهای آن کوبیده شده باشد ) یا زمینی که براثر ذوب شدن بخ زمستا:ها خاك آن از هم
باز شده باشد ) « مکی تژاد » ؛ همچنین درکناباد «کنابادی > و قزوین « دییر سیاقی » وکیلان
01 بمعتی لفون آب در چیزی امت - فیس : «وشت» ۳ وش ؛ ورك : نشتی -

‎٩‏ < رت ,کردی ع 818
```


## [2026-09-07T20:26:00.142Z] AGENT

Two key BQT pages located. Let me render p.2143 to read Mo'in's footnote properly, and check Bartholomae.


## [2026-09-07T20:26:00.887Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 600 python3 tools/ref_page.py BQT:2143 --image 2>&1 | tail -40"
}
```


### [2026-09-07T20:26:02.184Z] TOOL RESULT

```
REF: BQT:2143  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 226  OCR-lang: fas

-۱۳- ۱ عادست
نغاخمه ۱ - بر وزن شاسته » بمعنی - وامر پتغایدن هم هت پعتی بنغان ۸ -
نشانیده - و لعیین کرده شده باشد ۴ . و نشانده را نیز گفته‌اند که فاعل۹ شادن باشد؛
نشاخیدن ۴ « بروزن ومعنی نشاسن و باین معنی بجز ان
- وتعیین کردن باشد . ترکیپ در آخر ٍ ۵ ۱
نشاده - بکسر اول بروزن آشاره,چوب کلمات متفر ککگ 2
پوسیده را گویند که مانند آرد شده باشد . ی ۱ و ی
نشاستن ؟ - با سین بی‌ضه , بروزن | ۳ ین ۸
صفرا نشان وشیرة ر 4
ومستی ادن باشد ۳۰ کاستی‌حرارت نشان ل
نشارد * بفتح اول‌بروزن علاك, بلفث | - و بممنی هدف بب.
زند و پازند (۱) بممنی شکر باشد که از آن‌حلوا [ ونشانهٌ تیر وتفنکه شان
وچیزهای دیگر پزند . هم‌آمده است .
نغان ‎٩‏ < بکسر اول بر وزن نهان » نشاندن معروف است۱۱- ویمعنی
بممنی‌علامت باشد۷ - وحصه وتصیب رالیز کویند. | نهادن همست ۱۴
(۱) چك : ژند و پاژند .
۱ - اسم مقعول از ۸« نعاختن » (ه.م.) ۴ - بمعنی ۸« سب کرده و نشائیده وممین
و مقر رگشته » در دساتیر آهده 2 فرهنگه دسانیر ص۲۹۹ ۰ ی شاختن («.م.)
۴ - شاختن (ه.م.) . قس : شاندن ؛ و آن متعدی نشستن (۸.م.) است » در پهلوی
[ ۱ اسشق ۰۱۶۳۲ . و ر4 : دارمتتر . تتیعات ج ۱ ص ۰۲۹۷
اقلثه92 هزواری برای 5021687 ( شکرن ) «,وتکرس۲:۹۱*.
‎٩‏ - پهلوی 81810 «در کلمدّمر کب 8190 - 1702۳۷ (نگهبان هرغان) ».از-081280
از-28[2 - 001 ۰ دراوراق مانوی تورفان ‎8٩137180‏ << 2171858280 ( خواهند دید).یپودی-
فارسی 350018 » و درلهجه‌ها -015[3 ( نگاه کردن ) ؛ ایراتی میانه 2151128 » فارسی‌شان»
ارمنی ع 8198 از 0819۳ و 85028 . از 81888 (علامت ۰ نعان) » قس: اوستایی-(۸8791
- ط258 - 2181 نظارت کردن « بارتولمه ۳۹۰ > « نیب رک صس ۱۶۷ ۶ ۰ کردی 8188080 ۰
0و2 (علات . شانه ) « ژابااص ۶۲۰ > ۰ معرب نشان ۸ دزی ج؟ اس ۹۷۶ > و لیشان "دزی
اضا >« تفی >. ۷ - ۶ (وزبر ) گفت : ای پادشاه ؛ نشان خردمند کافی جز آن نیس ت که
بجنین کارها ( امثال وزارت ) تن در دهد . > «گللتان ص ۳۳ .
۸ - رك : شاندن . ‎٩‏ - اسم فاعل مرخم. ۴ از: ش +اندن (پوند
مصدر متعدی) » هتعدی لشتن (ج.م.) کردی نژشن 3 ۱ تیغه کردن نا دیوا ر کمیدن)
« ژابا س ۶2۱۹ .۰ ۱-کی را بنشتن واداشتن » چیزی را در جاپی مستق رکردن.
۳- دفع کردن . خاموش کردن » آرام کردن ( درد » الم ) : ۸ و دردهای چشم و کوش
بنغاند ( لین * شیر ) > «کتاب الابنیه : لین >.
0 نشاسته - بکسر ( و نیز فتح ) اول » معرب آن « شاستج » و نا« تفی » (رك :
شا ) وانیز اشاسته « دزی ج ۲ اس ۹۹۹ :۲ > ؛ مغ زکندم ( با حبوب دیگر ) مضولکوفته ؛
مادای سهی د که از آرد برنج وکندم وامثال آن کیرند » وچینده است « تقس >.
```


## [2026-09-07T20:26:02.777Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT aiwyaxs ===\"; grep -n \"aiwyäx\\|aiwyax\\|aiwy.äx\\|äxs\" BRT.txt | head -15; echo \"=== BRT asu ===\"; grep -n \"äsu-\\|äsi[sš]t\\|äsyah\" BRT.txt | head -15"
}
```


### [2026-09-07T20:26:02.863Z] TOOL RESULT

```
=== BRT aiwyaxs ===
2780:mit  para  Kaus.  '(Wasser  od.  dgl.)  weg- ' yaia  °iS  amavü  %rqfiuö  fraxstüne  s^mil laufen  lassen,  verschütten';  vTspanqm  zt  paiti  Y.  ff. 20;  —  'silät  ^wa  imavantasiä *avajrasn-ntqmparaca  aisayamananam  ^(yarnJ  (sd.)  Y.4'-4;  —  hyatcä  tnöi  hy^i dasva  *raizaiie  (sd.)  N.  ÖÄ  \växs  'iö  "und  dass  meine  Rede  wirksam
2802:folgendem  Fall  brauchen  wir  den  unbe- stimmten Artikel  'ein':  yavat  °sa  carsitika *avi.mqm  har>k>  (sd.)  hancayät  V.5.60. Undeutlich:  °sS  gaeHanam  . .  rass?  (sd.) N.  2;  —  ainitis  -iÖ  *växs  P.  26.  Vgl.
3174:Zu  einer  w.  Basis  *t'äxs-  (mit  ö);  i  aas  > '}.  — VgL  mp.  (äil,  eäilai  'Mahl'  (N.  64),  np.  !ä!t, xna.  LW.  r'aL  —  fu.-./nt  i  fuxt  pa  kämak  x^a- rii>/^Vi\  pa  iirVi.  —  ')  Uhlenbeck's  Elyroo- logie  WAiSpr.  90  ist  falsch.
3964:aiwyaxätar-
3967:Fa.:  fehlt, j.  armySii  N.  14:  lies  'yäs,  s.  'a*-. j.  aiwyäxiay'  Vf.:  ».  unter  ö;ri-  und  joy-.
4416:•  j.  an-äxätay  f.  'Unfriede':  vainJi  ahmt nmane  .  .  äxstis  "Um  Y,  60,  5 ;  —  iOm axsisis  'tSisÜa  mi>ra  xsayehe  dahyunqm Yt.  10.2  g.
4932:'töis  pouruhäxstayanake  asaonsYt.13. 112. Eig.  'des  Knochen   von  Metall  (Eisen)  sind'.
5233:j.  a-vi.barant-  Adj.  'nicht  auscinander- tuend,    zerteilend':    vl.barS  fraväxsö  (sd.)
5722:•  j.  asabanä-  C  £N.  einer  gläubigen  Frau: -rtaya  nairyä  pouru'jäxstöis  asaenya  "der  ; A.,  Frau  des  /*.  . ."  Ytij.140.  1
6084:(als  Subj.)3>  ya  'sät  gSUs  taiä  (sd.)  mraet Y.4/i.g;'~  mq'ir^m  yim  haurvatatS  'iahyä amsntätaicä  (sd.)  Y.gi.d;  —  kä  "iswöi 'iä  (Vok.)  äka  (sd.)  arpdrfng  isyä  Y.48. 8;  —  daidl  'iä  (Volc)  tqm  ailm  vanhsui ayaptä  manaifhö  Y.  28. 7;  6;  —  yS  vi mazdii  ahurä  pairljasäi  .  .  maibyO  dävBi akvh..  Jj-iT/t/J  (sd.)  'iilihacaY.28.2;sj.i; —  yahä  'sät  hacä  gqm  vJäal  (sd.)  västryS Y.5:.5;  43.14;  —  a/M  ahmai  mazda  'iä a»haüT..  ys..  "und  dem  o  M.,  wird  es (das  Rind)  durch  A.  zu  teil  werden . ., der  .  ."  Y.50.  3;  —  yehya  mUi  'iät  haia vahistsm  . .  valdä  (sd.)  mazdä  Y.5J.  12; 27. 15;  —  yqm  da  . .  °säcä  cBü  raneibyä (sd.)  xinOiim  Y.^i.$;  —  yj  vlänaet  da- iipmcä  (sd.)  aäa'Samli  dangrä  mante  -ia (Instr.)  mazdä  ahurö  ".  .  durch  seinen kundigen  Berater  Aia,  er  MAh."  Y.  46. 17;  3^-  '3;  —  vahista  säsnanqm  (sd.) yqm  .  .  sästl  'sä  ahurJ  Y.  48.  3;  34.  12, 46.  2;  —  maxdä  *yä  da  'iä  vanhSui mayh  (sd.)  manauAs  Y.  4y.  a;  44- ij  — yezl  ahyä  °iä psi  mat  xiayehl  (sd.)  ..mazdä Y.44~  15;  —  at  ahyäi  'iä  mazdä  urvarS vaxiat{sA.)  Y.48. 6;  —  ätrJm  ..  aojSt»hvan- tsm  'iä  Y.34-4'i  —  ^^  adr'ärum  . .  dalnk saoiyantqm  yä  ^haJc?r?tll  'iäcTt  urväxsat (sd.)  y'34.\z;  —  ks  vä  'iä  äfraiiä  (sd.) Y.5/.  11;  44- S;  —  'sät  hacä..  vaidä (sd.)  yS  Im  dat  Y.  45.  4;  —  vidui  (sd.) 'iä  ySm  mazdqm  ahur?tn  Y.  4S-  8 ;  — va»kSui  'iä  Aaozq%7Väi  (sd.)  ä  mananhs Y.45.  9;  —  ärmatsii  kasilt  'sä  hutSntus (sd.)  Y.  49.  S;  —  tSm  vS  'sä  mShmaidt huiJiaxäim  (sd.)  Y.  46.  13;  —  mazdä ahurS  'iä  hui.haxä  ifmvatä  Y.  32.  2 ;  — mazdä  ..%wävqs..  at  ns  fryä  °iä  dazdyäi häkurmä  (sd.)  Y.  44.  i;  —  spmtaHyäiä tur?i.. yehya  urvä  'iä  haiaifl (sd.)  Y.34. 2 ;  44. 1  o,  46- 16;  —  neit  'iahyä  adlvyeintj (sd.)  *hacsna  Y.  44. 13;  —  'iä  vyqm  (sd.) yehyä  hihäui(sd.)  nä  spmtö  Y.4^.  7;  — ärmaitlm  ..hi%qm  (sd.)  'iahyä  Y. ^4- ro; 4ß.  16;  —  tqm  dainqm  .  .  yä  msi  gai'iih •iä  frädBit  haiSmnä\sA)  Y.  44. 10;  43. 6,  34.14,  44-to,  4o-i',  —  'iahyä..  sairJ (sd,)  'iahyä  Virszsm  Y.35.Z;  41.6;  — /praiaaiträi  urväzistqm  (sd.)  'iahyä  da. sarSm  Y.49-8;  5J.  3,  31. 2\;  —  'i^miä ^ fradat.gal%Jm  Y.  j;j.  1 1 ;  —  'ia  (Vok.) kal  %wä  dar}sänl  (sd.)  Y.2ÄS,  45.6,  ;^. 6;  —  humqsdrä  (sd.)  °ia  (Instr.)  yeiä  yä
6189:Gen.  subj.  und  obj.:  alsm  *d>nidyäi{iA.) .  .  rayS  'st/  ". .  jrXoiiTOU  fioi'pai"  Y.  4J.  i ; —  abifra  (sd.) . .  ya  vaahsus  'sis  mananha Y._3i5.i3;  —  aiahya  yasa  {%A:)  'slm  y am iiyam  Y.  54.1;  —  °M/a  ^ae^ananqm viäu/(sd.)  ahurakya  mazdS  ".  .  des  AhM. Belohnungen  fiir  die  Taten  . ."  Y.2<V,4; — ■  nöit  kl  "M  *^ao^nanqm  vimysit  N. 16  ij);  —  zard>!ustrahe  .  .  asatinS  'itmia fravaiimca  yazamatde  Vr.  16. 2 ;  2,  Yt  13. 95;  —  tti  ahmt  nmane  Jamyarps  yh  asao- nqm  xshätas/a  'sayasca  . .  paitisatitayasla Y.  60. 2.  a)  mit  vanAav-  Adj.  und  aka^ Adj.  näher  bestimmt:  vatfkttyascä  °Ssi/ .. yS  ns  ara^ä  (sd.)  irmavaia^a  asanhäxs ^■5^-3't  —  syao^ana  mizdavqn  (sd.)  .. akfm  akai  vamthlm  'stm  vanhaavi  Y. 43. 5 ;  —  tSm  vatmklm  yasä  (sd.)  °sim  Y. 5;. ai;  —  maifyn  siaya  ahm  vaaAuya 'st  gaui  (sd)  Y.5/.  10«;  —  xmBth  afn- n>ntu  ahmya  nmsne  vawtklm  °/lm  i^a- parqm  Yt.  /J. i  S 7 ;  —  vaauAlsca  aöa  vaau- klsca  'sayS  Y.53.3;  —  yhca  tsi  gmh *aiura.mazda  ..  iSä  . .  vanukim  iihl/  'lim . .  ihm  .  .  *panndlm  yazamaidi  Y.^S. if  b)  Du.  'die  beiden,  beiderlei  Lose', d.  i.  (das)  gute  und  (das)  böse:  tmnanha (sd.) y5  dä%alibyd  priLratüm  xsayqs  'äfä*"^ üista  ". .,  der  über  beiderlei  Lose  gebietend den  Klugen  den  wahren  Ratav  versprochen hat"  Y.57.5.  A)  als  Gottheit,  die  die Lose,  insbesondere  die  guten  verteilt,  im jAw.  als  Göttin  des  durch  Frömmigkeit  ver- dienten Wohlstands*';  I)  im  gAw,:  Siraosö 'sfi  mqza.raya  (sd.)  Aacimnif  ya  vT  altl *ran3ibya  savlfi(sd.)  vldayäi  \ .  4j.  1 2 ; -^ sraosS  .  .  yU  *'li^  haiaiti  *mqxaraya  V. 27.6,  Vr. /2.1;  —  ya  vldayaf  'sts' (HS.) räshqm  (sd.)  Y.j^.  la;  —  ys  fta  'sSis aojaifha  var>dayaita  yqm  ,  .  gai^qm  .  . Y.  so.  3.  a)  Du,  in  Verbindung  mit armaiay-  Du.  ^A.  und  Arm.':  yads  ahm zivlm  (sd.)  .  ,  mazdasca  .  .  'sicil  armaitl Y.31.^.  II)  im  jAw.:  yö  'lim  yazäite ..k5  mihnm  yazaiieY\..i-j.2;  —  -/j  (VS.) srlre  'si  banumaili  .  .  °li  dä'ire  vehäm i^arifiilYt.sy.^;  6of.*;  —  hm  hacSl  'Hl pourvsj^ä'iira'Yt  /j?.54;  — /rä  mqm  aiwt.- urvalsayatfuha  marsdik?m  'al  (als  VS.) hnzaiti  Yl  77. 1 5 ;  —  'lim  . .  darr/S.- variiman3m..bartntltn  vispä  baSlazsY.S'i. 2;  —  sraohmla  'lim  nairXmca  sauh>m IVyt.40;   —  fravalays   .  .    'Isil  balsaza
6313:•  j.  aSa'vazdah-  m.  £N.  zweier  Gläubiger: i)  t?tn  yazitita  'da  pü^rS  pourui>3xÜBis.. Yt5.72;  —  "danhS  pouruoäxstayana/te asaonö  Yt  y .  112.*'  2)  t^m  yazsnta  .. "dasca  (NS.)'>  %ritai^a  sayuMrSis  pu%ra Yt  5. 7  2 ;  —  'daahd  %ritake  *ssyu\dröU Yty.113.
6314:*)  A.,  Sohn  des  Pauruiäxslay-  gilt  Dk.  ji-  16, 17  als  einer  der  sieben  unsterblichen  Herrscher in  X^a>äta%a  und  Bd.  zp.  6  als  einer  der  Helfer des  SaosyanI  bei  der  Auferstehung.
6801:yät K.4.%;  ■''N.  (iS;  —  'nahe  vairyehe  asaya frasrütahe  Y.27.7,  Vr.72.2;  7,4,  2.6,  Y. 7p.  2 1 ;  —  'nahe  vairyehe  arsuxoahe  växs y.^.i;  Vr.  70.2;  —  'nanqm  vairyanqm N.  702;  —  'n^m  vairlm  yazamaide  Y.  13. 8;  7.26,  61,1,  Vr.74.3;  —  'nJ  vairyS vacqm  j'irUrajqst^mäYl.  il.y,  —  sraohm .  .  yeAlie  'ns  vairyg  snatiis  vuata  Y.  57. 22;  — jainti   mqm   'na    vairy.
6944:•  j.,  g.  ahmät  Adv.  I)  'inde';  i)  räumlich; nHt  käu  as  vaote  (sd.)  .  .  nBit  a'  vaiata ". ,  oon  inde  procedit"  P.  4^.  2)  zeit- lich, a)  'von  nun  an,  nunmehr':  ys . .  kayä (sd.)  a°  . .  7'ästryä  Y._jy.6;  — yä  a°  staota yasnya  irävayeni  "indem  ich  nunmehr  die StY.  aufsage"  Ny.4-S-  b)  mit  folgen-' dem  ya^a  und  fiiL  Konj.  'doncc,  bis  dass': aU'it  a'  yaha  ap?mgm  maniva  an  Aat mz'Ji/is  (sd.)  Y. 10.16.  U)  beim  Kompar., wörtL  'als  das',  was  i)  vorausgeht  oder 1)  folgt;  meist  unübersetzbar,  i)  zurück- weisend auf  zuvor  Genanntes  oder  Ge- sagtes: imaj  vS  jatöyemi  .  .  yalca  a°  asH miirya  ".  .  quodque  hoc  est  maius"  Y. 'jj.  14;  14'i  —  saisisca  .  .  oAqxitäiscä *ß-äyjblscal(sA.)ca  a-  Vr.  Ä  i.  a)  in Verbindung  mit  eil :  ayaaAaUtäis  kan- täis  paiti  azdibis  avaJitriäiyilt  {%^)  masyd vü  'mii-'i/V. 4. 50;  51,52.  2)  voraus- weisend auf  einen  Nebensatz  mit  &)yd:ia: yifnö  zqm  visävayat  afvit  irii'va  a'  mas- yefäm  ydia  fara  ahmai  Y.  2. 1 1 ;  —  nüit il  a-  *drajyS  *yätltn  framraemi  (sd.)  .  . äfrOIm  .  .  ya>a  .  .  V.33;  Yt.  I3. 64^;  — xraesyöJaraia  (sd.)  ri5  a'  ya>a  vikrkS raiÄfsd.)  Ißi/eV.  IJ.8;  —  näirivai/e.  .  «• pÖurum  '>  frantraomi  . .  ya%a  mayavö  (sd.) /ratäxsffit'V.4.^T,  47J.  h)  yäha  yat: itsit  vaakö  a'  fyao>amm  v»r^yeiti  ya'^a yai..karMt^.4S;^.iS.\o.  c)  yattsit: nSit  vanhs  a'  syao%tum   vtnsyeiti  yaüöil
=== BRT asu ===
7514:•  j.  äsyah-  Adj.  'der  raschere,  schnellere':
12413:•  j.  *daeum.gan-''  Adj.  'der  den  Dana erschlägt,  tötet':  ätnm  väsistim  ..  'janjm sp?njayrlm  (sd.)  V.  ig.  40.
13138:—  firaSaosträi  urväsistqm  (sd.)  asahyä da  sarSm  Y.  4p.  8;  —  spmiä  mainyü vahihäcä  manaähä  ..  kacä  asäi  (Sp.  231 m.)  .  .  ahmäi  dqn  (3PKA.)'>  haurvätä ammtätä  matdh  xiakrä  ärmaiti  ahurS ".  .  wird  uns  Wohlfahrt  und  Unsterblich- keit verleihen  MAh.  im  Verein  mit  Xs., mit  Arm."  Y.  47. 1 ;  5^.  1 ;  —  däidl  *a/<*  V.; (Sp.  7  40  u.)  dangayü . .  sara%ustrili  Y.  2S.  6 ;
19924:«L  minati  'er  mindert'  (usw.).  —  Pü. ;  vinäsisti 'Zerstörung';  vgl.  'vmilay-.  —  ')  Unsicher. j.  mayludivanam  N.  63 :   lies  myaxdoüanqm (soT).
```


## [2026-09-07T20:26:09.760Z] TOOL CALL #51: Bash

```json
{
 "command": "ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/ 2>/dev/null | tail -8"
}
```


### [2026-09-07T20:26:09.831Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb    1931 Sep  4 15:02 70.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1606 Sep  4 14:54 72.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  669351 Sep  5 01:38 733.png
-rw-rw-r--  1 sfmqrb sfmqrb    1152 Sep  5 01:39 733.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  726576 Sep  6 18:36 829.png
-rw-rw-r--  1 sfmqrb sfmqrb     981 Sep  6 18:36 829.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  624515 Sep  5 16:20 902.png
-rw-rw-r--  1 sfmqrb sfmqrb    1658 Sep  5 16:20 902.vision.txt
```


## [2026-09-07T20:26:14.037Z] TOOL CALL #52: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/ | sort -n | tr '\\n' ' '; echo; echo \"--- 70,72 vision:\"; cat /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/70.vision.txt; echo \"=== 72 ===\"; cat /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/72.vision.txt"
}
```


### [2026-09-07T20:26:14.103Z] TOOL RESULT

```
0001.png 0001.txt 31.vision.txt 0049.png 0049.txt 58.vision.txt 70.vision.txt 72.vision.txt 103.vision.txt 172.vision.txt 180.png 180.vision.txt 181.png 181.vision.txt 220.vision.txt 333.png 333.vision.txt 733.png 733.vision.txt 829.png 829.vision.txt 902.png 902.vision.txt 1092.jpg 1092.vision.txt 1187.png 1187.vision.txt 1219.png 1219.txt 1219.vision.txt 1223.png 1223.txt 1225.png 1225.txt 1225.vision.txt 1226.png 1226.txt 1237.png 1237.txt 1237.vision.txt 1261.png 1261.txt 1266.png 1266.txt 1266.vision.txt 1267.png 1267.txt 1267.vision.txt 1272.png 1272.txt 1275.png 1275.txt 1279.png 1279.txt 1280.png 1280.txt 1280.vision.txt 1294.png 1294.txt 1294.vision.txt 1296.png 1296.txt 1296.vision.txt 1297.png 1297.txt 1298.png 1298.txt 1299.png 1299.vision.txt 1300.png 1300.txt 1300.vision.txt 1302.png 1302.txt 1302.vision.txt 1318.png 1318.txt 1320.png 1320.txt 1320.vision.txt 1339.png 1339.txt 1357.png 1357.txt 1382.png 1382.txt 1385.png 1385.txt 1385.vision.txt 1439.png 1439.txt 1445.png 1445.txt 1445.vision.txt 1452.png 1452.txt 1453.png 1453.txt 1455.png 1455.txt 1462.png 1462.txt 1465.png 1465.txt 1471.png 1471.txt 1472.png 1472.txt 1488.png 1488.txt 1492.png 1492.txt 1544.png 1544.txt 1550.png 1550.txt 1563.png 1563.txt 1564.png 1564.txt 1564.vision.txt 1567.png 1567.txt 1571.png 1571.txt 1572.png 1572.txt 1572.vision.txt 1578.png 1578.txt 1578.vision.txt 1583.png 1583.txt 1583.vision.txt 1589.png 1589.txt 1594.png 1594.txt 1594.vision.txt 1604.png 1604.txt 1604.vision.txt 1619.png 1619.txt 1622.png 1622.txt 1624.png 1624.txt 1631.png 1631.txt 1637.png 1637.txt 1637.vision.txt 1648.png 1648.txt 1648.vision.txt 1671.png 1671.txt 1673.png 1673.txt 1688.png 1688.txt 1688.vision.txt 1689.png 1689.txt 1689.vision.txt 1694.png 1694.txt 1707.png 1707.txt 1709.png 1709.txt 1709.vision.txt 1721.png 1721.txt 1731.png 1731.txt 1738.png 1738.txt 1738.vision.txt 1749.png 1749.txt 1754.png 1754.txt 1759.png 1759.txt 1774.png 1774.txt 1774.vision.txt 1776.png 1776.txt 1778.png 1778.txt 1781.png 1781.txt 1783.png 1783.txt 1786.png 1786.txt 1786.vision.txt 1795.png 1795.txt 1800.png 1800.txt 1802.png 1802.txt 1803.png 1803.txt 1803.vision.txt 1806.png 1806.txt 1807.png 1807.txt 1809.png 1809.txt 1814.png 1814.txt 1816.png 1816.txt 1819.png 1819.txt 1832.png 1832.txt 1835.png 1835.txt 1836.png 1836.txt 1838.png 1838.txt 1841.png 1841.txt 1848.png 1848.txt 1849.png 1849.txt 1854.png 1854.txt 1854.vision.txt 1858.png 1858.txt 1861.png 1861.txt 1862.png 1862.txt 1864.png 1864.txt 1865.png 1865.txt 1870.png 1870.txt 1872.png 1872.txt 1874.png 1874.txt 1874.vision.txt 1876.png 1876.txt 1876.vision.txt 1878.png 1878.txt 1879.png 1879.txt 1880.png 1880.txt 1894.png 1894.txt 1900.png 1900.txt 1902.png 1902.txt 1904.png 1904.txt 1908.png 1908.txt 1922.png 1922.txt 1922.vision.txt 1931.png 1931.txt 1931.vision.txt 1934.png 1934.txt 1947.png 1947.txt 1948.png 1948.txt 1949.png 1949.txt 1949.vision.txt 1986.png 1986.txt 2001.png 2001.txt 2001.vision.txt 2002.png 2002.txt 2002.vision.txt 2006.png 2006.txt 2010.png 2010.txt 2014.png 2014.txt 2014.vision.txt 2015.png 2015.txt 2023.png 2023.txt 2023.vision.txt 2029.png 2029.txt 2035.png 2035.txt 2039.png 2039.txt 2049.png 2049.txt 2049.vision.txt 2051.png 2051.txt 2053.png 2053.txt 2054.png 2054.txt 2055.png 2055.txt 2058.png 2058.txt 2060.png 2060.txt 2060.vision.txt 2062.png 2062.txt 2068.png 2068.txt 2069.png 2069.txt 2071.png 2071.txt 2073.png 2073.txt 2076.png 2076.txt 2079.png 2079.txt 2080.png 2080.txt 2083.png 2083.txt 2083.vision.txt 2084.png 2084.txt 2086.png 2086.txt 2095.png 2095.txt 2095.vision.txt 2099.png 2099.txt 2107.png 2107.txt 2130.png 2130.txt 2133.png 2133.txt 2134.png 2134.txt 2136.png 2136.txt 2143.png 2143.txt 2147.png 2147.txt 2155.png 2155.txt 2157.png 2157.txt 2163.png 2163.txt 2165.png 2165.txt 2167.png 2167.txt 2170.png 2170.txt 2170.vision.txt 2173.png 2173.txt 2173.vision.txt 2195.png 2195.txt 2195.vision.txt 2210.png 2210.txt 2210.vision.txt 2222.png 2222.txt 2224.png 2224.txt 2226.png 2226.txt 2228.png 2228.txt 2233.png 2233.txt 2242.png 2242.txt 2242.vision.txt 2246.png 2246.txt 2246.vision.txt 2258.png 2258.txt 2279.png 2279.txt 2293.png 2293.txt 2316.png 2316.txt 2316.vision.txt 2331.png 2331.txt 2395.png 2395.txt 2396.png 2396.txt 2406.png 2406.txt 2407.png 2407.txt 2417.png 2417.txt 2417.vision.txt 2420.png 2420.txt 2420.vision.txt 2427.png 2427.txt 2427.vision.txt 
--- 70,72 vision:
[BQT vol. 1 (Borhan-e Qate', ed. Mo'in), printed page 70 = archive.org borhan-ghate-v1 leaf n280.
Read from the page image (https://archive.org/download/borhan-ghate-v1/page/n280_w1600.jpg); OCR of the
local BQT_v1_pages.txt leaf 280 was too poor. Page identified by the running notes
"بقیه از صفحهٔ ۶۹" at the foot of this page and "بقیه در صفحهٔ ۷۰" at the foot of the preceding leaf.]

Headword (col. 2, top of page):
آهن ـ بفتح الف و سکون نون، معروفست. ـ و شمشیر و تیغ را نیز آهن گویند.
("āhan — with fatḥa on the alif and sukūn on the nūn, [it is] well known [i.e. iron]. — Sword and
blade are also called āhan.")

Mo'in's etymological footnote no. 2 to آهن (bottom of page 70), verbatim:
۲ ـ اوستا ـ ayah ، در ترجمه و تفسیر پهلوی âsênên «بارتولمه ۱۵۶»، پهلوی ایضاً asîn «دهارله ۱۸۸»
و âhên «نیبرگ ۱۳۵ـ۶»، اورامانی âsaen «دك. اورامان ۱۲۰»، سمنانی âsun، سنگسری ahän، سرخهٔ âsân،
لاسگردی âsân، شهمیرزادی asän «ك. ۲.۱۸۱ـ»، گیلکی âhin، فریزندی و یرنی âhan، نطنزی âhon «دك. ۱. ص۲۸۵».

(= "Avesta ayah; in the Pahlavi translation and commentary āsēnēn [Bartholomae 156]; Pahlavi likewise
asīn [Dhalla 188] and āhēn [Nyberg 135-6]; Awromani āsaen; Semnani āsun, Sangesari ahän, Sorkhaʾi āsân,
Lasgerdi āsân, Shahmirzadi asän, Gilaki āhin, Farizandi and Yarani āhan, Natanzi āhon.")

Footnote 5 on the same page, to آهنجیدن (a different word, "to pull"):
۵ ـ پهلوی âhanzhitan «مناى ۲۶۵»، فارسی آهنگ، آهنگیدن، هنجیدن، آهیختن هم‌ریشه‌اند. از ریشهٔ اوستائی
thang بمعنی کشیدن «بارتولمه ۷۸۴»، «نیبرگ ۷۰ ذیل frahang».
=== 72 ===
# Borhan-e Qate', ed. Mo'in, printed page 72 (vol. 1)
# read by Claude from the archive.org leaf image
# https://iiif.archive.org/iiif/borhan-ghate-v1%24282/full/1200,/0/default.jpg
# (item borhan-ghate-v1, leaf n282; running head "-۷۲-" confirms printed p.72)
# read 2026-09-04 for data/verification/page-38.json (root "Ahu")

--- main column, entry آهو (continuation from p.71) ---
عیب را نیز گفته اند ۱ خواه با مردم باشد و خواه با چیزهای دیگر - و بمعنی رم باشد که از
رمیدن است چه آهوبی رمیدگی را گویند - و بمعنی فریاد و آواز بلند هم آمده است - و نام
مرضی و علتی هم هست که آنرا بعربی ضیق‌النفس خوانند - و بطریق استعاره چشم را نیز
آهو میگویند - و شاهد و معشوق را هم گفته اند .

--- footnote 1 (Mo'in's etymological note, foot of p.72) ---
۱ - مشتق از کلمهٔ اوستایی ahu بمعنی عیب و نقص و صفت اوستایی âhita یعنی چرکین،
پلید و ناپاک، پهلوی âhôk (عیب) «مناس ۲۶۵». خاقانی در بیت ذیل به هر دو معنی آهو که
غزال و عیب باشد اشاره کند:
یعنی آن جانور که زاید مشک        نامش آهو و او همه هنر است.  «یشت ۱ ص۱۶۵»

--- footnote 5 (same page) ---
۵ - آهومند - مرکب از: آهو بمعنی عیب + مند پسوند اتصاف؛ بمعنی مریض - معیوب -
مغزآهومند، مختل، مخبط
```


## [2026-09-07T20:26:23.482Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 - <<'EOF'\nimport json,glob\nfor f in ['data/verification/page-38.json']:\n    d=json.load(open(f))\n    for e in d['entries']:\n        print(f, e['entry'], e.get('root'), e.get('verdict'))\n        if 'hu' in str(e.get('root','')).lower():\n            print(json.dumps(e,ensure_ascii=False)[:3000])\nEOF"
}
```


### [2026-09-07T20:26:24.745Z] TOOL RESULT

```
data/verification/page-38.json 0 Ahu plausible
{"entry": 0, "root": "Ahu", "verdict": "plausible", "modern_form": "the Avestan family is āhita- 'defiled, soiled' / āhiti- f. 'defilement, blemish' (Bartholomae, AiW cols. 345-348); an independent Avestan noun *ahu- 'defect' is not attested", "note": "Everything on this chart except the root box itself checks out. The root box comes straight from Nourai's single reference: Mo'in's etymological footnote at Borhan-e Qate' p.72 says the word is 'مشتق از کلمهٔ اوستایی ahu بمعنی عیب و نقص و صفت اوستایی âhita یعنی چرکین، پلید و ناپاک، پهلوی âhôk (عیب)' — i.e. Mo'in himself posits an Avestan ahu 'defect, fault' beside the adjective āhita-. But no such headword exists in Bartholomae's Altiranisches Wörterbuch: AiW has ahu-/aŋhu- 'lord' and 'existence, life' (a completely different word, whence Ahura), and for the 'blemish' family only āhita- Adj. 'befleckt, verunreinigt' and āhiti- f. 'Befleckung, Verunreinigung, Makel'. Two further points about the root box: (a) the vowel is long — the whole family has ā- (āhita-, MP āhōg, NP āhū), so the printed 'Ahu' is at best a shortened citation form; (b) Bartholomae, at the very column Nourai cites for the Persian node, derives MP āhōk / NP āhū from āhita- directly, so the chart's two branches are one branch in the standard treatment. The Avestan words, the Pahlavi word, the Persian words and their glosses are all correct as printed, so the entry is sound in substance; only the reconstructed apex is unverifiable. Node #2's chart NOTE (FAF:38 deriving āhū from AV 'a-hu: not good') is rejected by every source consulted — see that node.", "note_fa": "جز خودِ جعبهٔ ریشه، همه‌چیز این نمودار درست از آب درمی‌آید. جعبهٔ ریشه یکسره از تنها مرجع نورایی گرفته شده است: پانوشت ریشه‌شناختی معین بر برهان قاطع (ص ۷۲) که می‌نویسد «مشتق از کلمهٔ اوستایی ahu بمعنی عیب و نقص و صفت اوستایی âhita یعنی چرکین، پلید و ناپاک، پهلوی âhôk (عیب)»، یعنی معین خود در کنار صفت āhita- اسمی اوستایی به شکل ahu «عیب» فرض کرده است. اما چنین سرواژه‌ای در فرهنگ ایرانی باستان بارتولومه نیست: بارتولومه ahu-/aŋhu- را به معنی «سرور» و «هستی» دارد (که واژه‌ای یکسره دیگر و ریشهٔ «اهوره» است) و برای این خانواده تنها āhita- «آلوده» و āhiti- «آلودگی، لکه» را می‌آورد. دو نکتهٔ دیگر: نخست آنکه واکه در سراسر این خانواده کشیده است (āhita-، āhōg، آهو)، پس «Ahu»ی چاپی در بهترین حالت صورت کوتاه‌شدهٔ استنادی است؛ دوم آنکه بارتولومه در همان ستونی که نورایی برای گرهٔ فارسی یاد کرده، āhōk فارسی میانه و «آهو»ی فارسی را یکراست از āhita- می‌گیرد، پس دو شاخهٔ نمودار در روایت معیار یک شاخه‌اند. واژه‌های اوستایی و پهلوی و فارسی و معناهایشان همه درست چاپ شده‌اند و مدخل در گوهر سالم است؛ تنها رأسِ بازسازی‌شدهٔ آن وارسی‌پذیر نیست.", "sources": ["https://en.wiktionary.org/wiki/%D8%A2%D9%87%D9%88"], "ref_check": [{"ref": "BQT:72", "status": "supports", "note": "Borhan-e Qate' ed. Mo'in, printed p.72 (archive.org borhan-ghate-v1 leaf n282, running head '-۷۲-'; read from the leaf image, saved to data/verification/sources/refs/ocr/BQT/72.vision.txt). Footnote 1 to the entry آهو: 'مشتق 
data/verification/page-38.json 1 Ai confirmed
```


## [2026-09-07T20:26:31.563Z] TOOL CALL #54: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-07T20:26:31.569Z] TOOL RESULT

```


```


## [2026-09-07T20:26:35.794Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D9%87%D9%88",
 "prompt": "Give the full Persian etymology section for آهو (āhu) 'deer, gazelle': the Middle Persian form, the Proto-Iranian reconstruction, Avestan cognate, and any cited sources (Hasandust, Cheung, MacKenzie). Also note any separate homonym آهو 'defect'."
}
```


## [2026-09-07T20:26:38.160Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D8%B4%D8%A7%D9%86",
 "prompt": "Give the full Persian etymology of نشان (nešān) 'sign, mark': Middle Persian form, any Proto-Iranian root, whether it is connected to a verb meaning 'to see/watch' (ni- + axš-), and cited sources. Also list Arabic/Armenian/Turkish borrowings mentioned."
}
```


### [2026-09-07T20:26:42.170Z] TOOL RESULT

```
# Persian Etymology for آهو (āhu)

## Primary Etymology (Deer/Gazelle)

**Middle Persian form:** āhūg

**Etymology pathway:** The word derives from Middle Persian āhūg, ultimately tracing back to Proto-Indo-European *h₂eḱus, meaning "sharp, swift."

**Cognates:** Northern Kurdish *ask* and Baluchi *ásk* share the same root.

**Etymology 2 (Homonym):** A separate, archaic sense exists meaning "defect, imperfection," documented in 10th-century texts like Ferdowsi's Shahnameh with the phrase "āhō girift" (have grown faulty).

## Source Documentation

The Wiktionary entry cites three major references:

1. **Steingass** (1892) - *A Comprehensive Persian–English dictionary*
2. **Dehkhoda** (1931–) - *Dehkhoda Dictionary*
3. **MacKenzie** (1971) - *A concise Pahlavi dictionary* (page 7)

The page also references Paul Horn (1893) on neupersian etymology. However, the specific Avestan cognate and Proto-Iranian reconstruction are not explicitly provided in this source document.
```


### [2026-09-07T20:26:44.956Z] TOOL RESULT

```
# Persian Etymology of نشان (nešān)

## Middle Persian Origin
The word derives from Middle Persian **nyšʾn'** (/nīšān/, "sign, mark, banner"), representing a continuation of an earlier root form.

## Root Analysis
The etymology traces to a proto-root **nyš** (/nīš-/), which appears across related languages. The documentation suggests a connection to perception vocabulary, as evidenced by cognates in Old Armenian **նիշ** (niš) and Old Georgian **ნიში** (niši), though the specific verbal connection to "see/watch" with a ni- prefix is not explicitly detailed in the provided source material.

## Related Language Evidence
The comparative forms show widespread distribution:
- Old Armenian նշան (nšan)
- Old Georgian ნიშანი (nišani)
- Classical Syriac ܢܝܫܐ (nīšāʾ)
- Hebrew נֵס (nēs)

These are noted as "loanwords from Iranian."

## Major Borrowings Documented
**Arabic**: نِيشَان (nīšān)
**Armenian**: նիշան (nišan)
**Turkish**: nişan (via Ottoman Turkish نشان)

The source references MacKenzie (1971) and Dehkhoda Dictionary as scholarly authorities on this etymology.
```


## [2026-09-07T20:27:00.111Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E1%BD%A8%CE%BA%CE%B5%CE%B1%CE%BD%CF%8C%CF%82",
 "prompt": "Give the full etymology section for Ancient Greek Ὠκεανός: all proposed origins (Beekes/Pre-Greek, connection with ὠκύς 'swift', Sanskrit ā-śáyāna- 'lying around', *ḱey- 'to lie'), and which is preferred by modern scholarship. Quote the wording."
}
```


## [2026-09-07T20:27:01.358Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/ocean",
 "prompt": "Give the full etymology of 'ocean' as printed, including the Greek Okeanos and any statement about its origin being unknown or connected to okys 'swift'."
}
```


### [2026-09-07T20:27:05.207Z] TOOL RESULT

```
# Etymology of Ocean

According to the Online Etymology Dictionary, the word "ocean" comes from Old French *occean*, which derives from Latin *oceanus*, ultimately tracing to Greek *ōkeanos*. 

The Greek term referred to "the great river or sea surrounding the disk of the Earth (as opposed to the Mediterranean)." However, the dictionary notes that this Greek word has "unknown origin" and suggests it may be Pre-Greek in nature.

The entry does not mention any connection to *okys* (meaning "swift") in its etymology. The source simply states the origin cannot be determined with certainty, describing it as a word "of unknown origin" with the possibility of Pre-Greek roots.
```


### [2026-09-07T20:27:06.442Z] TOOL RESULT

```
# Etymology of Ancient Greek Ὠκεανός

Based on the Wiktionary article, the etymology section presents multiple proposed origins:

## Proposed Origins

**1. Non-Indo-European Substrate Loan (Primary View)**
The article states the term is "generally acknowledged to be a non-Indo-European substrate loan," with Beekes suggesting a Pre-Greek form "*ūkʲān-".

**2. Semitic Connection**
A possible link to Semitic root "*ʕ-w-g" ("to be crooked, tortuous") has been discussed, though this remains speculative.

**3. Sumerian Derivation**
Another possibility involves "unattested Sumerian *A-ki-an(u)" (Water of the Land and Heaven).

**4. Proto-Indo-European Theory**
Michael Janda revived an earlier comparison with Vedic dragon Vṛtra's attribute "*āśáyāna-* 'lying on [the waters]'", proposing derivation from Proto-Indo-European "*ō-ḱey-m̥[h₁]no-* ('lying on')", related to Greek "κεῖμαι" (to lie).

## Preferred View

The article presents the substrate loan explanation as the dominant modern scholarly position, with Beekes's Pre-Greek reconstruction receiving prominence as the most accepted etymology.
```


## [2026-09-07T20:27:16.167Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/accipiter",
 "prompt": "Give the full Latin etymology of accipiter: the reconstruction (*ōku-petro- / *aku-petri-), whether it is from PIE *ōḱus 'swift' or *h₂eḱ- 'sharp', the influence of accipere, comparanda (Greek ōkypteros, Sanskrit āśupátvan-), and cited authorities (de Vaan, Pokorny). Also mention acupedius if present."
}
```


## [2026-09-07T20:27:18.727Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A3%D9%88%D9%82%D9%8A%D8%A7%D9%86%D9%88%D8%B3",
 "prompt": "Is there an Arabic entry for أوقيانوس / أوقيانوس (ocean)? Give its etymology (from Ancient Greek Ὠκεανός, via Syriac?), and the modern Arabic form used (أوقيانوس / محيط). If the page does not exist, say so."
}
```


### [2026-09-07T20:27:23.221Z] TOOL RESULT

```
# Arabic Entry for أوقيانوس

Yes, the entry exists on Wiktionary. Here's what the page contains:

**Etymology:** The word is "Borrowed from Ancient Greek _Ὠκεανός_ (Ōkeanós)." The page does not mention Syriac as an intermediary.

**Definition:** Listed as an archaic term meaning "ocean."

**Modern Usage:** The page provides the form "أُوقْيَانُوس" (ʔūqyānūs) with full declension tables showing nominative, accusative, and genitive cases.

**Note:** The entry indicates this is an archaic usage. While the page doesn't specify what modern Arabic speakers use instead (like محيط), it does show descendant forms in Persian, Urdu, and Turkish, demonstrating the word's historical linguistic spread.
```


### [2026-09-07T20:27:23.503Z] TOOL RESULT

```
# Latin Etymology of *accipiter*

## Reconstruction and Components

The word's origin is uncertain but shows parallels across Indo-European languages. Scholars propose the compound structure *ac-* + *-piter*:

**First component (*ac-):** De Vaan suggests derivation from PIE *HéHḱus* ("swift, quick"), while Claire Le Feuvre argues for PIE *h₂eḱ-* (also the source of *acus*).

**Second component (*-piter*):** Possibly from earlier *\*petro-* or *\*petri-*, potentially meaning "wing," connected to PIE *peth₂-* ("to spread out, fly").

De Vaan proposes the Proto-Italic pre-form *\*aku-petris* ("having swift/pointed wings").

## Comparanda

The term parallels formations in related languages:
- Ancient Greek *ōkúpteros* (ὠκύπτερος, "swift-winged")
- Sanskrit *āśupátvan*
- Proto-Slavic *\*àstrę̄bъ*

## Phonological Development

The geminate *-cc-* may derive from influence by *accipiō* ("take, seize"), or alternatively from earlier *\*āci-* via the littera-rule, though Nussbaum disputes this explanation.

## Cited Authorities

De Vaan and Beekes are primary modern sources; Nussbaum offers alternative reconstructions based on Hittite *pát-tar* and Plautine attestations. The work represents consensus from contemporary Indo-European etymological scholarship.
```


## [2026-09-07T20:27:35.435Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== PHD ahug p7 ===\"; python3 - <<'EOF'\nt=open('PHD.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[28][:1500])\nEOF"
}
```


### [2026-09-07T20:27:36.753Z] TOOL RESULT

```
=== PHD ahug p7 ===
ngible, impalpable.
a-ģumān ['ewrm?n!] without doubt, certain.
a-gumég Pgwmyk! | M ?gzumyg] unmixed, pure. ~ih: purity. 33? águstan Pkwstn! | M ”gwst] hang up, suspend. 8.45% X wc āhan pA(y)n! ,^s(y)n! | M ?hwn, N ~] iron. ~én ['synyrn!] iron, of iron. ~gar [-kl | N ~] blacksmith. ahang [hng] pull, draught. āhanjīdan [?hncytn!] = āhixtan. ahanüz Phnwe | M *hnwn-c, N haniiz] yet, still. āhen = āhan, q.v. аһа Phyt' | M QYAyd] stain, impurity; confused. ^Àh : pollution; confusion.
āhixtan, āhanj- [?AAtn!, ?hnc- | М ?hxtn, Chynz-), N āhīxtan, ~] draw
out, pull up, extract.
аһа PAPy | (M ~hr’y)] righteous (of Sros). ahlaw Phlwb! | M ?hlw] righteous.
~ih: righteousness. ahlaw-dād Phlwb d”t'] alms, charity. ahlayih [kl dyh] righteousness. AN 7 ШЕ, * Md ahlomby [hlmwk' | M ?hImug] heretic. 3
~ih: heresy. āhēg Phwk' | M >ле, N ahd] fault, blemish. ahógénidan, áhógén- ["nokyn-ytn!] defile. a-homānāģ [’hwm’r’k'] unlike. ahēš [nof] deathless, immortal.
ahēših 7 amāwand
~ih : immortality. ahr Phl] dread, fury. ahrüftan, ahram- P4Pftn', *hm- | M hr’ рїп, ? hr? m-] raise, lead up. Ahreman ['Al(y)mn! | М ?hrmyn, N ~] the Evil Spirit. >
áhüg [TYBA < A ру; ”hwk! | MQyhwg, N āhū] gazelle. ahunawar [hnw!] the holiest prayer, beginning Yadā ahū wairyē. a-hunsand [Phwnsnd] dissatisfied. ^h : dissatisfaction. ahy [KZ Y < А k-zy | М hy] soon(est), first. ajģahān [>20/?л! | М ieikin, N azgahan] lazy, indolent. “АҺ: laziness, indolence. ak P! | N dk] evil, harm. -ak LIN ~] diminutive suffix. a-kámagóm
```


## [2026-09-07T20:27:37.978Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== IEC okus ===\"; grep -n \"ōkus\\|okus\\|ōkú\\|ocior\" IEC.txt | head -8; echo \"=== IEC okwos eye ===\"; grep -n \"okʷos\\|okwos\\|okʷ\" IEC.txt | head -8; echo \"=== SYN swift ===\"; grep -n \"ōkús\\|ōkus\\|ocior\" SYN.txt | head -8; echo \"=== LEW accipiter ===\"; grep -n -i \"accipiter\\|acupedius\\|acu-pedius\" LEW_1910.txt LAT.txt | head -8"
}
```


### [2026-09-07T20:27:38.089Z] TOOL RESULT

```
=== IEC okus ===
8539:Kakio (Kakos, us) “jump; jumper; jumping, agile, springy’. Cf. WP I, 334 Oss. sag ‘stag’; Gk. kekío (Doric: -à-) jump’; Li. Sóku, ti and $okiü, -éti “jump, dance’; cf. Sokus ‘agile, springy’; šoktas 'jumping-bar'
11072:moks-, mokust- (?) “case, sheath, pod'. Cf. mokos (1) Skt. cf. makusthah, m. ‘kind of bean’ beside ma$ákah (“skin bottle. Phonology uncertain); (Ober, maska, Per. mask, id. said to be a Semi- tic LW); Romani, cf. moxton, m. (‘box. Etym. uncertain); Arm. cf. maxay, gs -i, ab. sg. -av (bag, wallet, pouch’, fr. *moksola. But Arm. mask, i, av 'skin' is a LW via Iranian); OCS mosina, R. Cz. mo3na (bag, purse’, fr. *mok- sina); Li. mak$nà, f. id. beside makštis, (ës, f. ‘case, seedpod, vagina’ and makštys, io, m. id.
11079:moks-, mokust- — molks- (molsk-, molks-)
12097:óKus, os “sharp, keen, swift. WP I, 172 Skt. a$üh ‘quick’; Av. asus, d Arm. cf. an- uj$, gs: -uši, ab. s. -ušav, adj. (sweet, i.e. ‘not sharp); Myc. oku- (in names); Gk. oküs ‘swift, sharp’ beside n-ókar (lethargy, w. neg. px); Alb. eh, m. ‘cutting-edge, blade’; Lat. cf. ocior, Ocius ‘quicker; more quickly’; Se- quanian ox(queried: ‘keen’ of weather); Gaul. ociomu ‘most keen’; W awg, m. ‘keenness, sharpness; OBr. di-auc (‘slow’, w. neg. px. *dé-); Br. di-ok, -oek, -ek “lazy, slow’; OCor. dioc, Cor. dyec, id.; W di-og, id.; (ambig. in Cz. jas, m. ‘jubilation’); Latv. cf. ostins *trig- ger, spike
=== IEC okwos eye ===
=== SYN swift ===
=== LEW accipiter ===
LAT.txt:1098:accipiter,-trls m.(f. dans Lcr.): oiseau de proie, epervier ou
LAT.txt:1103:55; e "t Caper, GLK VII 107,8, accipiter, non acceptor. Le nom rustique
LAT.txt:1111:Si l'on fait abstraction de 1 'influence de accipio, le mot accipiter
LAT.txt:1112:est parallfele A acupedius (v. ce mot). De meme que acu-pedius rappelle
LAT.txt:1113:gr. ojcu-to>u C, accipiter rappelle gr. dao-nxepoq, skr .d<pu-patvan- "qui vole
LAT.txt:1345:Adaptation de ofjimouc., comme celeripes de ajamouc. V. accipiter. Pour la
LAT.txt:5632:r 4 cente. V. accipiter.
LAT.txt:42951:coaposds dans lea aots archaxques: acupes, acupedius, accipiter (v.
```


## [2026-09-07T20:27:53.254Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SYN swift/eye ===\"; grep -n \"^4\\.21\\|4\\.21 EYE\\|EYE\" SYN.txt | head -5; grep -n \"QUICK, FAST\\|SWIFT\" SYN.txt | head -5"
}
```


### [2026-09-07T20:27:53.322Z] TOOL RESULT

```
=== SYN swift/eye ===
5714:4.206 EYEBROW
5875:parts OF 4.21 EYE 5 Goth. augo er akis gpaadues, HHO ON  auga ett. acs Grk. oe Dan. #e ChSl. oko NG ulus S 6ga SCr. oko t. oc . WwW. 4 Lav echo OE éage Boh. oko Tr oeil ME — eze (eghe, eye) Pol. oko S eafo NE eye Russ. glaz ih ochiu Du. 00g Skt.  akgi, cakgus-, locana-, ; suil, rose OHG ouga netra- Nir. sil F MHG ouge Ay.  éaSman-, déiéra-, aki Ilyga G eC He lagad il ie , ae ‘fost of the words for ‘eye’ belong to sol, etc. ‘sun’ (1.52). Walde-P. 2.446. a ited group. The others are from | Pedersen 1.62. Stokes 692. an inher! Ir. rosc, fr. *pro-sc-, deriv. of sech-
24641:14.21 SWIFT, FAST, QUICK
```


## [2026-09-07T20:27:55.079Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; ls; echo \"=== WP I 172 okus ===\"; grep -n \"ōk̑ú\\|ok̑ú-s\\|ōku-s\\|äsu-\\|ocior\" WLD_Bd1_pages.txt | head -10"
}
```


### [2026-09-07T20:27:55.128Z] TOOL RESULT

```
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
=== WP I 172 okus ===
```


## [2026-09-07T20:28:04.196Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '24641,24660p' SYN.txt"
}
```


### [2026-09-07T20:28:04.240Z] TOOL RESULT

```
14.21 SWIFT, FAST, QUICK
Grk.  raxbs, dxbs, Bobs, dtbs Goth. sprauté (adv.) Lith. greitas, skubus
NG "YPiyopos, -yAjyopos ON Sjotr, skjotr, hradr, Lett. dlrs, 2igls
Lat. _celer, véléx, citus, ra- snarr ChSl.  skorit; jedro, _brtzo pidus Dan. = rask, hurtig, snar (advs.)
It. rapido, presto, veloce Sw. snabb, snar, rask SCr. — brz, hitar
Fr. rapide, vite (adv.) OE hrad, swift, snel(l) Boh. = rychly
Sp. rapido, presto, veloz ME swift, rad, snel, spede Pol. predki, szybki
Rum.  repede, iute NE fast, swifl, quick, Russ. bystryj, skoryj, Sibkij
Ir. dian, liiath, crib specdy Skt.  dgu-, tvarita-, gighra-,
Nir. luath, tapaidh Du. vlug, snel, gauw, java(na)-
W. buan, cyflym, chwyrn, ras(ch), spoedig Av. dsu-, aurvant-, Owa- clau OHG  sniumi, (h)rad, snel, §a-, xSviwra-
Br. buan, herrus rasc
MHG nel, rasch, sliume, geswinde
NHG schnell,
rasch,
geschwind
There is a wealth of words denoting rapid motion (besides those listed, e.g. NE rapid, NHG schleunig) from which it is not always easy to select the most generic and usual and between which the choice is too idiomatic, according to the context, to permit any generaliza- tion. NE swift or the now more com- mon fast may apply to rapid motion of
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
any duration, while in quick (in accord- ance with its original sense of ‘live, live- ly’) there is a notion of ‘sudden’ or ‘soon over’. We speak of a fast horse or run- ner in a race, a quick starter but not 2 quick horse, A somewhat similar feeling may distinguish NHG schnell and rasch, or it may be more a matter of local preference (for which cf. Kretschme?,
385). And so in the other
```


## [2026-09-07T20:28:05.902Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; grep -n \"ocior\\|acupedius\\|accipiter\" WLD_Bd1_pages.txt | head -10; echo \"=== page markers ===\"; grep -c $'\\f' WLD_Bd1_pages.txt; grep -n \"^ *17[0-4] *$\" WLD_Bd1_pages.txt | head"
}
```


### [2026-09-07T20:28:08.324Z] TOOL RESULT

```
3224:farbig“ ware (in diesem Falle ware aquila als Kurzform eines mit accipiter
15782:fii6ig“ ist   auch als tfbersetzung von gr. divnovg verstandlich: lat. accipiter
15792: nantenseharfung unter EinfluS von accipere zu accipiter). Auch ob got.
=== page markers ===
887
```


## [2026-09-07T20:28:16.225Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; sed -n '15765,15800p' WLD_Bd1_pages.txt; echo \"=== nearest page tag ===\"; awk 'NR<=15800 && /^\\s*1[0-9][0-9]\\s*$/ {p=$0; n=NR} END{}' WLD_Bd1_pages.txt; python3 - <<'EOF'\nlines=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\nimport re\nfor i in range(15782,15600,-1):\n    if re.match(r'^\\s*\\d{2,4}\\s*$',lines[i]): print('marker',lines[i].strip(),'at',i); break\nEOF"
}
```


### [2026-09-07T20:28:17.577Z] TOOL RESULT

```
unter Annahme verschiedener Praeformanten vermitteln. Es ist ja gar
nicht ausgemaclit,                       daB die verbalen Anwendungen                                   in   unserer Sippe    das
altere seien.


oku-s         „schnell‘\
      Ai. (leu- ,,schnell“,                  Komp. (inyirn. Sup. unstha-, av. Cisu- „schnell“, Komp.
ttst/Ct,     Sup. asiZta-.               gr.       lat. d dor ,.schneller“, Sup.
                                               Jjttvs.         tbyJcov.            mxtaxos,
ocissimus (Positiv fehlt), acymr.          ncymr. diog, corn, dioc, bret. di-ec
                                                                         cli-ciuc ,

„trage“, eigentlich „unschnelb‘ (Curtius Gdz. 5 131, Osthoff IP. 6, 2f. m. Lit.).
    Eine Ablautform *aku „schnell“ steht nicht fest. Lat. acupedias „schnell-
fii6ig“ ist   auch als tfbersetzung von gr. divnovg verstandlich: lat. accipiter
 „Habicht, Falke” Ur jedenfalls durch volksetymologische Anlehnung an
 accipere) kann zwar den Begriff „schnellfliegend“ voraussetzen (vgl. drs.vg.
 (hy.vjuTt'jg, dry.vnxtoog, eXupQoxarog nET£i]vd>v als Beiworter des Habichts

 bei Homer; Solmsen Enters. 149), erweist aber auch dann nicht ein *ahi-
 pctrts als Gdf., da auch ein *ocu-petns fvgl. aufier tby.v-TreTijg, wxvjt xegog
 auch ai. Cigu-patvan- „schnellfliegend“) iiber „ociipeter nach accipere zu cu-
 cipitcr werden konnte (Thurneysen aaO. erwagt „spitzfluglig“ als Gdbed.
 dann aus *ilrri-petri-s durch Dissimilation zu *acipiter und durch Konso-
 nantenseharfung unter EinfluS von accipere zu accipiter). Auch ob got.
 ninths .,Taube“ (ahd. lheinfr. dk-falla „Taubenschlag“ [nach Feist Got. \Yb. 2
 442 zweifelhafte Glosse]) von einem solchen *aku- abgeleitet sei (Solmsen
 Unters. 149                A 1), ist hochst zweifelhaft (s. Feist Got. Wb. 2 12).
       Eine Ablautform                       *ckn-         mit           Praef. ga-         vermutet Erdmann (Zitat bei
 Noreen                 Ltl. 44)        in   ahd. gain                  „rasch,       hastig,   plotzlich“,    mhd. ijcehe, nhd.
 jdh         bair.             gehda „Ungestum“ ist recte gehdu „Sorge“
                          gdcli).       aber        ags.
 (Zweifel hinsichtlich der Bed. und Lautform des ags. Wortes bei Zupitza
=== nearest page tag ===
```


## [2026-09-07T20:28:29.876Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; grep -n \"aiwyäx\\|aiwy-äx\\|aiwyax\\|okno\\|wind-ow\\|Windauge\" WLD_Bd1_pages.txt | head -10"
}
```


### [2026-09-07T20:28:29.935Z] TOOL RESULT

```
15722:passen, wahrnehmen, sehen“; vom w-St. abg. okno „Fenster‘ (vgl. engl.                                                                              !
15727:wind-oiv                ds.,       eig. ,,Windauge“).
28259:                                         aksl. rlakno „Faser", russ. volokno
70185:russ. tolok „Stampfe, Handranmie“, tolokno, pi. tolohia „durch StoBen im
```


## [2026-09-07T20:28:31.052Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SKT ocean ===\"; grep -n \"^Ocean\\|Ocean\\.\" SKT.txt | head -5; echo \"=== SKT window ===\"; grep -n \"^Window\\|Window\\.\" SKT.txt | head -5; echo \"=== SKT eye ===\"; grep -n \"^Eye\\b\" SKT.txt | head -5"
}
```


### [2026-09-07T20:28:31.125Z] TOOL RESULT

```
=== SKT ocean ===
12603:Ocean.  (F.-L.*Gk.)  O.V.  cctan.^ L.  oeeanum,  ace.  oi  cceatms.^i^V.  umtav6i, the  great  stream  supposed  to  eucompass  the eanu.
=== SKT window ===
=== SKT eye ===
6174:Eye.  ^E.)  ME  eye,  eighei  nl.  eya^ tyen  (whence  eyne),  A.  S.  t^,  pi  eAgan. ■+■  Du.  cog,  Icel.  aii^,  Don.  pit,  Swtil. iiga,  Goth.  augo.  G.  augt,  Kas«.  oko,  L. ocuftu  (dimin.  of  a'mj*);  O.  Ok.  0x«or  ; Skt.  aksha,  {^  AK.)  Der.  dais-y,  q.  t.  ; U'iHi{-ow,  q.  v,
```


## [2026-09-07T20:28:47.556Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== MON kashak headword ===\"; grep -n \"^کشک\\|کشک:\" MON_part1.txt MON_part2.txt | head -10; echo \"=== MON oqyanus headword ===\"; grep -n \"^اقیانوس\\|اقیانوس:\" MON_part1.txt MON_part2.txt | head -10; echo \"=== MON ahu headword tags ===\"; grep -n \"آهو:\" MON_part1.txt | head"
}
```


### [2026-09-07T20:28:47.650Z] TOOL RESULT

```
=== MON kashak headword ===
MON_part2.txt:11544:کشکول, چوبین؛ ج. اقحاف قحوف. 
MON_part2.txt:12084:کشک دوغی می‌سازند و از چکیدة آن پس 
MON_part2.txt:19256:کشک به آب نرم کرده را با روغن و کمی 
MON_part2.txt:23551:انکار). یعنی کشک: یعنی هیچ و پوچ. 
MON_part2.txt:23552:کشکاب: ۷:3 (- کشک او - کشکو] 
MON_part2.txt:23557:کشکبا: ۲۵:7 (امر.) آش حلیم. 
MON_part2.txt:23558:کشکرک: مه (۱.) (جاد.) پرنده‌ای 
MON_part2.txt:23563:کشک رک دمی دراز دارد. رنگگ پرهایش 
MON_part2.txt:23569:کشک رکث بطور کلی پرنده‌ای است مضر 
MON_part2.txt:23586:کشکله: (فه)دامطکتا (.) نوعی از بای‌افزار 
=== MON oqyanus headword ===
MON_part2.txt:38067:اقیانوس‌های بزرگک می‌زیند و تا ٩۰۰‏ يا 
MON_part2.txt:93655:اقیانوس‌های منجمد را شکنند تا رفت و آمد 
MON_part1.txt:797:اقیانوس بی‌پایان. (تص.) هستی بی‌حد و 
MON_part1.txt:15624:اقیانوس: 2555« [- اوقبانوس» معر.] ((.) 
MON_part1.txt:15626:اقیانوس وجود دارد: اقیانوس کبیر. اقیانوس 
MON_part1.txt:15628:اقیانوس منجمد جنوبی. 
MON_part1.txt:59242:اقیانوس. دریا. 
=== MON ahu headword tags ===
5553:آهو: 1 (.) عیب» نقص. بسماری» مر ض. 
82683:آهو: سروی آهو (غزال). کمان تبراندازی. 
90796:ضوامن» ضمناء (غم.)» ضامنین. ضامن آهو:
```


## [2026-09-07T20:28:48.443Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"^Window\\|Wind-ow\\|Windo\" SKT.txt | head -5"
}
```


### [2026-09-07T20:28:48.497Z] TOOL RESULT

```
1165:fvith  a  window)  in  a
1244:brfon  ft  iiiot>-window  ;'  Cot.
2879:■aah  (1).  a  case  or  Irame  for  panes  of gla**.  (F.-L)  Coiniptionof  F.  Mojiw.  •» fmme  of  wood  for  a  window ; '  Cot.— O.  F. (htutt  (F.  cMdsse),  a  case,  shrine.  —  L. eapsa,  a  cue.  See  ohaaa  (3)  and  oaae  (3) above.
5783:to  slope  the  sides  of  a  window.  — O.F.  em-
12009:Mullet  (2),  a  fire-pointed  star ;  see Molar. Muilion.  an  upright  di\i!>ion  between lights  of  windows,  (F.  —  L.)  A  corruption of  munnion^  which  occurs  with  the  same sense.  The  lit  sense  is  'stump,*  because the  muUion  is,  properly,  the  stump  or lower  part  of  the  division  below  the  tracery. "F.  nt^ignoti,  a  slump.  (Cf.  E.  trunnion -F.  troigttOH^  dimin.  of  F.  tram  ^\x^. tromo).^0,V.  moing,  maimed;  tJie  equi- valent of  Ital.  moruo,  al^o  mame,  maimed. ^LmoncHJ.  maimed.  Cf.Bret.  WtfW4.  nWf, maimed,  also  occnrring  in  the  forms  tnaflk, moHk,  moils.  AUo  Spaa.  muHfffh  the stump  of  an  arm  or  leg ;  &c. Multan^ar,  &&  \  see  Multiiudo. Multitude.  (F.-L.)  F.  muUituJe.^h. muUituJirum,  ace.  of  multitudo,  a  multi* tude.  *  L.  multus,  many,  much.  Hence mnltHingular,  muItilaUraly  Slc
```


## [2026-09-07T20:28:57.698Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== MON aqyanus ===\"; sed -n '15620,15632p' MON_part1.txt; echo \"=== MON kashk region ===\"; sed -n '23540,23575p' MON_part2.txt"
}
```


### [2026-09-07T20:28:57.787Z] TOOL RESULT

```
=== MON aqyanus ===

افهر: ۵۲ [ع.] (ص‌تسفض..) یره تر» 
قاهر تر. 

اقیانوس: 2555« [- اوقبانوس» معر.] ((.) 
دریای بسیار بزرگ» در کرة زمین پنج 
اقیانوس وجود دارد: اقیانوس کبیر. اقیانوس 
اطلس. ایانوس هند. اقیانوس منجمد شمالی. 
اقیانوس منجمد جنوبی. 
اک‌ابر: 0( 1( ج. اک بر. 
بزرگتران؛ مهتران» بزرگان. 29 (فر ه.) 
بزرگسالان. شر فا. اکابر و اصاغر: مهتران و 
کهتران مهان و کهان» بزرگان و ۱ 
=== MON kashk region ===


کشفشن: 32-0 (مص‌م.) پرا کنده کر دن» 
پرشان ساختن. بژمرده کر دن. معدوم کردن. 
کشی: :12 (.) نوعی از للنیات که عبارت 
است از دردی ماست یا دوغ که پس از 
جوشاندن خشکك کنند؛ پینو؛ بین و کد؛ 
قر وت. . (مج.) هیچ» پوج؛ بیهوده. . شیح 
حسین کشکت را بساب: (مثل) به همان کار 
اصلیت مشغول باش. کشکك چی؛ پشم چی ! 
(عم.) چه موضوعی" چه اصلی! (در مقام 
انکار). یعنی کشک: یعنی هیچ و پوچ. 
کشکاب: ۷:3 (- کشک او - کشکو] 
ور کح آ ناه که ای رد 
ترید کنند و خورند. آش‌جو که بیماران را 
دهند. آب‌جو؛ ماءالشعیر. 

کشکبا: ۲۵:7 (امر.) آش حلیم. 
کشکرک: مه (۱.) (جاد.) پرنده‌ای 
است از راسته سبکبالان جزو دسته دندانی 
نوکان از تیرة کلاغ‌ها که در اکثر نقاط کرة 
زمین بافت می‌شود. این برنده دارای قدی 
متوسط است (تقریباً به اندازهٌ یک کبوتر). 
کشک رک دمی دراز دارد. رنگگ پرهایش 
سیاه و سفید است. پرهای سپاهش متمایل به 
بنفش و ارغوانی است و برنده‌ای چایک و 
مودی و مزور و خوراکش دانه و میوه و 
حشرات و گوشت و تخم مرغان دیگر 
است. زیر سینه ماده فنص تفیل نک انیت 
کشک رکث بطور کلی پرنده‌ای است مضر 
زیرا تخم پرندگان مفید دیگر را می‌خورد و 
نسل آنها را کم می‌کند. رل از ازدیاد 
نسل این پرنده باید جلوگیری کرد. ۰ بهترین 
ی با تفنگ يا مسموم کردن 
طعمه‌های گوشتی این جانور است. نوک 
۲ زا 9
```


## [2026-09-07T20:29:11.554Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad 2>/dev/null || mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad; cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad; curl -sL -o bqt71-373.jpg \"https://iiif.archive.org/iiif/borhan-ghate-v1%24281/full/1400,/0/default.jpg\" && ls -la bqt71-373.jpg && file bqt71-373.jpg"
}
```


### [2026-09-07T20:29:14.900Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 257093 Sep  7 16:29 bqt71-373.jpg
bqt71-373.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, progressive, precision 8, 1400x1981, components 3
```


## [2026-09-07T20:29:18.510Z] TOOL CALL #74: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt71-373.jpg"
}
```


### [2026-09-07T20:29:18.572Z] TOOL RESULT

```

```


## [2026-09-07T20:29:53.429Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT asu leaf ===\"; python3 - <<'EOF'\ntxt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nt=txt.split('\\f')\nfor i,p in enumerate(t):\n    if 'äsyah-' in p or 'äsu-' in p or 'äsi&t' in p or 'äsist' in p:\n        print('leaf',i)\n        for l in p.split('\\n'):\n            if 'äsu' in l or 'äsyah' in l or 'äsist' in l or 'äsiit' in l: print('  >',l[:250])\n        # header\n        print('  HEADER:',p.split('\\n')[0][:120])\nEOF"
}
```


### [2026-09-07T20:29:54.963Z] TOOL RESULT

```
=== BRT asu leaf ===
leaf 217
  > •  j.  äsyah-  Adj.  'der  raschere,  schnellere':
  HEADER: anter  'had-.
leaf 384
  > •  j.  *daeum.gan-''  Adj.  'der  den  Dana erschlägt,  tötet':  ätnm  väsistim  ..  'janjm sp?njayrlm  (sd.)  V.  ig.  40.
  HEADER:   /raourvaaayäiti     drujS    vais- mmda  "  aztmnqm  (sd.)  Yt  10.  86. Vgl.  gr.  *ij  iilKi^i),    ahd.   zuo.   — 
leaf 409
  > —  firaSaosträi  urväsistqm  (sd.)  asahyä da  sarSm  Y.  4p.  8;  —  spmiä  mainyü vahihäcä  manaähä  ..  kacä  asäi  (Sp.  231 m.)  .  .  ahmäi  dqn  (3PKA.)'>  haurvätä ammtätä  matdh  xiakrä  ärmaiti  ahurS ".  .  wird  uns  Wohlfahrt  und  Unste
  HEADER:  vlsyU  zantumS  'mB zardhuärö ptixlöY-ig-iB.  A)  m.Name der  Gottheit  der  Länder*':  "mtm/a  aia- vamm  asahe  ratam
leaf 634
  > «L  minati  'er  mindert'  (usw.).  —  Pü. ;  vinäsisti 'Zerstörung';  vgl.  'vmilay-.  —  ')  Unsicher. j.  mayludivanam  N.  63 :   lies  myaxdoüanqm (soT).
  HEADER: h?m  'tsm  Yt 10.  143;  —  aiwyäahanam  stthrpaisam^fm 'ttmY  .g.36;Yt.l3.i,Y±20; — hat>ma{sA.) . .  stikrpaEsanha  Ua
```


## [2026-09-07T20:29:55.570Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== NYB nis- ===\"; grep -n \"niš-\\|nyš\\b\\|nikāh\\|nigāh\" NYB_vol2_glossary.txt | head -10; echo \"=== BRT col 390 region ===\"; python3 - <<'EOF'\ntxt=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i,p in enumerate(txt):\n    if re.search(r'\\b389\\b|\\b390\\b|\\b391\\b',p) and i<400:\n        h=[l for l in p.split('\\n') if re.search(r'\\b(389|390|391)\\b',l)]\n        print('leaf',i,h[:2])\nEOF"
}
```


### [2026-09-07T20:29:57.042Z] TOOL RESULT

```
=== NYB nis- ===
2598:murv-niš [mwlwnyš] soothsayer fore- telling the future by the flight or other tokens of the birds, an augur, pl. cas. obl. ~-dn 535. — murv + niš, the pres. st. of MPrs nyyšydn, nyyš- ‘to see’ (A-H I, Verbum 168); cf nišan.
2719:nikah [nk’s] look, glance, observation; custody, care: ~ kartan to look on, to watch 152. 259.24, 2726. 2817; ~~ daštan to notice, to observe, to pay attention to 108%. 12114; apar ~ dāštan to keep in safe custody 4112. — MPrth ng’h ‘look, attention’, n. kyrdn ‘to notice’ (A-H ITT); Paz. nagäh, NP nigäh; < Olr "ni-kada- from kà-, v. ākāh. Another derivative was "niš-ka0a- > Milr *niškāh ‘contempt’, preserved in Arm nškah-em ‘to reject, to condemn’. Cf also Arm nkat linel or nkat-em ‘to see, to consider, to contem- plate’ from MIr *nikät < Olr *nikātā, nom. sg. of the nomen actoris *nikätar- ‘contemplator’. The pt. pass. *nekāta- is found in the name of the 15th nask (q. v.) of the Sas. Avesta: N?kütom [nyk”- twm] = Av. *nikätem ‘that which is observed (in medical matters)’.
2761:nīšān [nyš'n'] sign, omen, portent 487, gl. by daxšak + anak; pl. —-iha 11018. — MPrthPrs nys’n; NP nišan.
2780:nizburtéh [nzbwltyhy] humiliation 128°. — Cf Verbum 226; in my opinion niz- < niš- is the genuine SW form, cf özmütan.
6737:nagäh: nikāh
=== BRT col 390 region ===
leaf 104 ['KompE.  —  ai.  äHTia-  n.,  kuid.  atii,  np.  vgl. fS-äm.  —  lEt.  s.  JScHMtDT  Plur.  390.  —  Pü, : äaii  (so!  Päi.  A^,  für  an  dk  r«  änii).']
leaf 135 ["El?')  —  DsT.  ZA.  2.  389  'ladte';  Gdn.  KZ. ^5-  395  'Knicker'  (was  schlecht  passt),  — ')  Es könnte  HaptoL  vorKegen."]
leaf 163 ["Abgekürzt ')    lur    asaaxia    .  .    arhuiia ;    s.    la (vtmiyraAro:    —    D   Anders  Gdn.  KZ.  2g. 391,  DST.  ZA.  2.  385.    Aber  als  Adj,  kommt <iu<i-  sonst  nicht  vor. j.  aia^ta  FrW.  J.  2  :  lies  asaili;  s.  qi-,"]
leaf 190 ['391']
leaf 199 ["Komp.:  ä.^-*ila):.  —  Vgl.  ufiiitilal.  —  ai.  vgL. Aaf.  f.  'Ankunft',  —  Pü.:  äii-atisn,  (zu  V.  g. 32):  äyiin.  —  ')  An  das  Praeverb  äiei  (so Sp.  VglGr.  389, 4S3)  glaube  ich  nicht.  Beachte Pü.  von  aili.harqn  V.  J.  41 1  rir-pän  barciid, — '■)  So  J  10.     NA.  -li."]
leaf 219 ["i- iaslaii,  (lu  Y.  6S)\\  apar  an  i  amäk  yaxiSn iiiSliü,  erl.:  fföS  däi-e;  s.  noch  No.  8.  — »  S  '4^-  —  '>  Doch  s.  No.  3.  —  J)  NA.  'inli (aber  •fnti  tu  Vt.  //.  1 1).  —  «)  Theni.  —  5)  Vgl. Dbr.  AiS.  391  und  unter  'iad-  mit  tit,  itiaex ■fl*-  I  5,  —  6)  5  i2ii.  _  7)  Vgl.  noch  ifl*- No.  3.  —  8)  PQ. ;  ßa  draj  i  tbSr  Su  Shrmazd  . . äAii/  (in  Aw.-Buchst)  ifiiJ."]
leaf 241 ['390']
leaf 242 ['391']
leaf 243 ['—  upavazab-  391']
leaf 289 ['ai,  i;Slama-  m.  EN.  —  ar,  *gaulama;  Be<3.? Anscheinend  Superl.  —  \')  Vgl,  daiu  Yt.5.  8l. Dass  es  sich  dabei  um  die  Disputation  m"\' einem  BuddhiBlen  handle  (Haiig,  Dst.;  lulel: Dakab  JRAS.  iSgS.  391,  der  naidy  für  \' corroption  of  the  Vedic  name  of  the  son  r Golama,  viz.  Nodhä^  ansieht),  ht  tinerweislich ond  mir  unwahrscheinlich;  s.  noch  Jn.  Zor. 177  nnd  lu  li^ryavanl:']
leaf 305 ['Vgl\'  fti.  jäi^rli  "er  wachl\',  woss.  rfal-Sänun \'wecken\'.  S.  noch  Fü.  und  zajajiiiivaJi.  No.  3. —  Pu.  (luH.  /)!  /rä/  Z\'ijp-äyisHUi),  (lu  V.  jS): Jräi  dn  p  r  äj\'f/*)  -  in  der  np.  Paraphrase  bei Sp.  Komm.  I.  391:  bidär  gatdad -,  (w  N.)i anpr  ivilmh,  dnnpi  äj\'/i«**«.  — OS.iBild. S  142  mil  JSCHMIDT  KZ.  J7.  34,  Bgm.  GrGr.3']
leaf 339 ['•>  Pü.  bietet  nur  caxr  (in  Aw.-Buchsu)  ohne weitere  Erläuterung.  Die  heimischen  G^c^ra- phen  kennen  zwei  Landschaften  iarx,  eine  in Xorä4än  nnd  eine  bei  Plana,  VgL  Gcft.  OK. 137,  GIrPh.  3.  391.']
leaf 371 ["Ableil.  (s.  'liiya-).  —  lEt.  s.  */äyii.'a-.  —  taya- *diebisch;  Dieb' (mit  Schwaslufeji  'tJya-  'Dieb- stahl' =•  ai.  vf-dkä-  :  vardha-  (usw.,  B.  JScHUinT riur.  391).  —  Pü.  (zu  1):  tiihäaik,  (zu  3  a): duzd,  (lU  2  b)i  tir/l  »>,  erl  1  duäilAä  dr/l.  — ')  Lies  läyö  (lu  ^/äya-)}  S.  No.  Z.  —  »  D.  i. 'Diebstahl',    s.   die  vAbleit   tirßenllan   unter"]
leaf 385 ["nim  Vr.  7.  3 ;  Yt  2.  i  a,  Vyt  i4-  a)  äai^ nayä  (näml.  ayah)  heisst  der  24.  Monats- tag; °nayä  vavhuyJ  mazdayasnUi^S.i.n; vgL  2. 24,  Y.7(».6.  a)  GS.  mit  a^OTOna- m.  Name  cioer  Gottheit:  äat  hl  (näml. mi^raie)  Aävlfya  ar^e  vasatte  .  .  'nayä mäzdayamSiS  upamaram  (statt  NS.;  Sp. 391  u.)  Yt/0.  ia6."]
```


## [2026-09-07T20:30:18.454Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\ntxt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\nfor ln in (3964,3967):\n    off=sum(len(l)+1 for l in lines[:ln-1]); leaf=txt[:off].count('\\f')\n    print('line',ln,'leaf',leaf)\nt=txt.split('\\f')\nprint('=== leaf of aiwyaxatar ===')\ni=None\nfor k,p in enumerate(t):\n    if 'aiwyaxätar-' in p: i=k;break\nprint('leaf',i)\nprint(t[i][:1500])\nEOF"
}
```


### [2026-09-07T20:30:19.829Z] TOOL RESULT

```
line 3964 leaf 89
line 3967 leaf 89
=== leaf of aiwyaxatar ===
leaf 89
denfalls   Kn.  /,  24.     Sü.   bat   dafür I      mahän, gurutarah,  Mpii.i  niklar,  mihtar,  bihtar. I      S.  noch  SWienAW.  Ö7.  840.  1  f. ]  •  j.  'a-bda-  Adj.  (fem,  -da-)  'wo  man  nicht !  hintreten ,    nicht  festen  Fuss  fassen  kann' Isva,  'grundlos':  -a'affl  (NSf )  ioa .. sadayät yat  iaa  pasius  anumayehe  pmirn  valnäite i"'und  unbetretbar  wird  es  ca^mX.  daiiihus) I  erscheinen,  wo  jetzt  der  Tritt  der  Schafe Izu  sehen  ist"  V.^.24'>. ]      S.   unter  i/flSfl-.    —    ai.   vgl.   äpada-  Adj.  'no j      place   10  siep  upon'  (SEE.  42-  if>7)-   —   PÜ.: I      transskr.  =)  —   ')  Vgl.  iSt.  Hau.  KZ.  27.  94. '      Ggr.  OK.   139.    —    ')  Wobei    a  statt  dd  ge- schrieben isL   ÜST.E  a/diA-ia  'unc  merveille'  ist Korrektur,  i.  tllr.  2.  IIS  ^o.  4.
•  j.  abdö.t^ma-  Adj.  (fem.  'mä-)  'der ausgezeichnetste,  trefflichste':  galiiyäi  le ysi  'me  (NDf.)  "für  das  Hauswesen  die .trefflichsten"  YLj.34.
I  j.  aiwyaahim  N.  lO:  lies  a'i-j}ayaah>m.
•  g.  abyaatay- f.  'eifrige  Bemühung  um-',
mit  Akk. :  mSneä  I  mqzdazdüm  (sd.)  ''valdö.- düm  dalnabis  "tä  (li.)  aAüm  ys  vatfhSus mananks  ".  .  und  lernt  sie  im  Innern  be- I  greifen  in  eifriger  Bemühung  um  das  Lebea des  guten  Sinns" "'  Y.  jj.  j  ".
Komp.:  aibl-'^''yaslay-,  zum  \.ya(:  —  ai.  'yal-
I       lay-  I.  —  l'ü. ;    iiiäs  dahiiiiih  i  pa  den  pa  Mar
2  aj^'än  i pa  vahuman;  das  Wort  fehlt  also;
I
```


## [2026-09-07T20:30:30.711Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Aufseher\\|beaufsicht\\|Aufsicht\" BRT.txt | head -10; echo \"=== asi Auge ===\"; grep -n \"'Auge'\\|,Auge'\\|die  (beiden)  Augen\" BRT.txt | head -10"
}
```


### [2026-09-07T20:30:30.776Z] TOOL RESULT

```
3968:•  j.  ai^ry-äxStar-  m.  'der  die  Aufsicht hat,  (ührt  über-,  Eeaufsichtiger" :  har^ia 'taca  z'ispaya  .  .  gai^ayä  ¥.57.15;  V.  2. 4,  5;  —  hant3rfmca  'türimca  .  .  gafkayä \l.  10.  103; — yüi  hmii  äiihqm  damanqm ..  'iarasifa  (NP.)  nipätarasca  .  .  Ytig.18.
3970:•  j.  aiwry-äxäträi  Inf.  'die  Aufsicht  zu führen  über —,  zu  beaufsichtigen',  mitAkk.: gai'i'Sscil  tattvasca  harsiräicä  'räuä  Y, 5Ä2;  7/.11,  VL5.6.
7099:j  i)  'die  Aufsicht  fuhren',  ohne  Obj,: l^sraOMvarizff  (jid.)   aiwyffxiayit  N,  77;  —
14947:•  j.  paiti.daya-  m.  i)  'der  die  Aufsicht führt,  Beaufsichtiger':  tiltrJm  ..yim  ratäm 'daimca'^  vTspaesqm  stärqm  frada%al ahurO  mazda  ya%a  narqm  zardiuftnm Yt  S,  44.  3)  'Erkennungszeichen,  Merk- mal' (?,  nur  Komp.).
26730:*)  D.  i.  sva.  der  religiös  und  bürgerücli  mündig geworden  ist.  Nach  vollendetem  15.  Jihr  tritt an  die  Stelle  der  elterlichen  Aufsicht  die  Be- ratung durch  den  Kaimi;  s.  Sp.  1498  f.  Vgl. dazu  Gor.  OK.  239,  Jn.  JAOS.  13.  ccix,  Dst. ZA.  I.  124  No.
27283:•  j.  sraosä-varaz-  m.  Name  des  siebenten und  geringsten,  mit  der  Kirchenpolizei (s.  No.  2)  betrauten  Unterpriesters  (ratav-); auch  die  Kirchenzucht  liegt  ihm  ob:  *>d'> aiwySxiayai  "der  Sr.  soll  die  Aufsicht fuhren"  N.  Tj''*;  —  *anaiwi.?r?fvB^aiit (sd.)  aSa  abfrtta  *'ta  (ND,)^'  vlcarayattm N.  7p;  —  . .  paoiryS  . .  hävanatum  (sd) . . BstayHH  . .  hapla%3m  'um  N.  tfe;  —  'am Sstäya  Vr.^.i;  0.3.$;  —  rai^wiskare va  •«  vH  V.5.  57;  58;  —  a<):aB  ralui aoxtB  'zB^^  ä^qin  frä^wtrfsaiti  ". .  be- stimmt die  Strafe"  V.  7. 71*';  5.16;  —  'tahe Vyt  15.  a)  vom  Hahn,  der  als  'BUttel' des  Sraosa  gilt,  weil  er  die  Menschen aufweckt  und  so  zur  Erfüllung  ihrer  FSicht antreibt:  kB  asti  sraosahe  a^ehe  ..  '«J'V m?r>yB  yS  parö.dars  nqma  V.  7Ä  1 4  C
=== asi Auge ===
6059:•  j.)  g-  aS-  n.  'Auge',  uzw.  Ä/iischer  Wesen'' ; norDu.;  tat  drvats  drvatyasca  '/»(AD.).. iarma  *diari^ra  za/ari . .  paiti.urvaistftn (sd.)  YLji.2;  —  ma  zqm  vasiiSit  °iibya''> Y.p.29;  29,  Yt;/.5;  — yS  aiistp/n  *vai- naühi  (sd.)  aogpdä  gam  'siiyä''>  kvancä V.ilMo.  ■
7111:femer   lit.  akh  'Auge'  usw.    bei   Bgm.  Grdr.= ,  wo"  NA,  ü./a/ bietet     S.  ä  No.  i8.
11263:•  j.,  g.  caäman-  n.  'Auge':  °ntanh(<jV).) sühnt  Yt  10.  23,  P.  ^4;  —  sonst  Sing,  in kollektSinn:  'manat hata  "vondenAugen her"  V.  _j.  14;  —  spUi.dSihra{^A^  °manat kaca  niibannti  V.  7.  24;  —  ts  'mSng''> ^wisra  härS  aibJ  aiä  aibi.vamahl  vTspä "all  dessen  wirst  du  durch  Äsa  gewahr,  es mit  leuchtendem  Auge  beobachtend"  Y.  j/. 13;  —  hyat  äz£/ä  hsm  'maini'^  ASr^ab»n "als  ich  dich  mit  dem  Auge  erfasste"  Y. 31.  8;  —  nS  BTt  (Sp.  1 54  u.)  'maint'^  vyä- danstm  Y.  4:5. 8;  —  y3cä  voAa  'mqm'^ arp/ai  (sd.)  manavAn  Y.  50. 10.
13576:•  j.  döiSra-  n.  'Auge'  uzw,  o^rischer Wesen'*:  köyümea  'nm  Y.i;.4;  —  kvan^a xsa^ahe  .  .  'rahe  akuralu  Y.  7.  i  r ;  — Tumd  Sfyö"  TäbyB  ya  akurafu  Y.  ÖÄ  22; Yt.  10. 8a',  ig.  94;  —  ho  ..  aküm  . .  üayä :■</«<?/  °räbya  Yt.  79.94;  7,29,  to.  107;  — baiz-ar?  'ranqm  videi^re  (sä.)  Yt  10.82; —  'ra  F.jd.
24856:KompE.;  Ableit.  —  ai.  raiand-  Adj.  'leuch- tend', n.  'Licht',  Ic'cana-  n.  'Auge' 3);  np.  iö:aii 'Fenster'.  —  0  S  29*.  4- —  »  Die  herkömm- liche Cberseliung,  bei  DST.  ZA.  i.  j8:  "une porle  et  une  fenelre",  verlangte  'caaimfa; s.  PisCHEL  ZnMG.  jff.  139.  —  ö)  Das  Fenster ist  das  Auge  des  Haukes.
```


## [2026-09-07T20:30:47.937Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\ntxt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\nfor ln in (3968,6059,7099,7514):\n    off=sum(len(l)+1 for l in lines[:ln-1]); leaf=txt[:off].count('\\f')\n    print('line',ln,'-> leaf',leaf,'~col',2*(leaf-25))\nEOF\necho \"=== FSD accipiter ===\"; grep -n \"Accipiter\\|ac-cip'i-ter\" FSD_vol1.txt | head -5"
}
```


### [2026-09-07T20:30:49.247Z] TOOL RESULT

```
line 3968 -> leaf 89 ~col 128
line 6059 -> leaf 158 ~col 266
line 7099 -> leaf 200 ~col 350
line 7514 -> leaf 217 ~col 384
=== FSD accipiter ===
```


## [2026-09-07T20:30:55.383Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (89,158,200,217):\n    nums=[l.strip() for l in t[i].split('\\n') if re.fullmatch(r'\\s*\\d{2,4}\\s*',l)]\n    # also numbers at line starts\n    inline=re.findall(r'(?m)^\\s*(\\d{2,4})\\s+\\S',t[i])\n    print('leaf',i,'standalone:',nums[:6],'linestart:',inline[:6])\nEOF"
}
```


### [2026-09-07T20:30:56.677Z] TOOL RESULT

```
leaf 89 standalone: ['97'] linestart: ['97']
leaf 158 standalone: [] linestart: ['331']
leaf 200 standalone: [] linestart: []
leaf 217 standalone: ['344'] linestart: ['344']
```


## [2026-09-07T20:31:11.724Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"'schnell'\\|,schnell'\\|schnell\" BRT.txt | head -12; echo \"=== leaf 216/217 asu region ===\"; python3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i in (215,216,217):\n    p=t[i]\n    for l in p.split('\\n'):\n        if 'schnell' in l or 'äsu' in l or 'äsy' in l or 'äsi' in l: print(i,'>',l[:230])\nEOF"
}
```


### [2026-09-07T20:31:13.109Z] TOOL RESULT

```
5554:mnbyascä  näiribyasca  xara>ustrahe  za-  »j.  aurva- Adj, 'schnell;tapfer">:  ^«rffli^^iT tshsus  raßoräi  manaahS  "het  komme  Ae^  aiWü  'vS  \X.4.q;  —  Iqm  yazjitta  'va liebe  X  zur  Unterstützung  zu  den  Männern  hunavSvalsakaya\\..$.t,T,i^;—iS>:riv!Ht und  Frauen  des  Z,  zur  Unterstützung  des  "'^"p«  Yt/0.109;  14;  —  'itwam  yazfmU guten  Sinns"  V.54,1.  "i-ätihs  ahuränhs  VL5.85;  —  yat  bäun
5566:•  j.  'airyaman-  m.  Name  des  mit  J  (7/r- ,  •  j.  'aurvataspa-  Adj.  'der  schnelle ysmä  isys  beginnenden  Gebets  Y.54.1:  Rosse  hat';  a)  von  ^rar-imd  Äj'ari>.tiiji^u-: 'matiim  mq^ranqm  maBittm  Yt.j.5;  —  Är'ur?  "toffi  YL/0.90;  6.4;  —  'tun  bavähi T-3r/irayn3m. .  ya^asli  antan  ahuna(&A.)  yaia  kiari  Az.  6";  —  am.nakc  hü  yat 'manaiAD.)Vi.24.i;*li.ioj.  a)  sonst |  Vn^  YLJO.  13;  —  hiarsxsaS^m  'ptm mit  isya-.  'mamm  isim  .  .  ßäsB  mq^fvm  Yt  6. 1,6, 12.^4, 1^.81,  \.  16.4;  —  hvar>- ..  b»r?am  Aa',aoxt?m  Vr.2.10;  G,/.6,  S.j^/attJj  °päi  Y.ÜÄ22;  —  hrerixiaiiahe 2.3;  —  tfm..  vJspanqm  sravanhqm  ufard.-\ ..  -pake  Yt.  Ö.o,  Y, 22. 24;  /.  11;  —  Iwan- kainm  fradaiqm  yim  'mamm  tsim  FrW. '  xsaiia  'pa  (VS.)  V,  j/.  5,  b)  von  apqm 4-1',  1 ;  —  'taan^m  isim  . .  maiisüm  o/aAe  napät-.  apqm  napa  -ps  Yt  ig.  51';  — sra-.arahqm  Y.54.2;  Vr.  24,1;  —  °manS  aPqm  napättm  'ptm  Y.  2. 5;  —  apqtn isyehe  hafu{iitä..'manö  isyeke ,.  haililca  ..  nap5  °pa  Y.65.13.  'pä'a  VyLjJ, Vr.24.2;  /.8,  S.7.3.                                    4'>"(?).
5583:•  j.  airyö.sayana-  n. 'arischer  Wohnsitz,  .j^g. aurvant-, aourvant-" Adj. 'schnell; W.  der  Arier':  vJspjm  .  .  'fvm  Yt  10.  13.  tapfer,  Held':  '7-at"  F.  7;  —  /laomo  aeibis
5606:•  j.  aurvo.t«ma-  Adj.  'der  schnellste,!  KB.  z*  verweise  ich  auf  ^/.inmJHf.  Gam  un- tapfcrste',    von    Vayav:    vaim    aurvanam\     elaublich^Dsx.  2A.  a.  627.
7446:•  j.,  g.  asav-  Adj.  'schnell,  rasch':  yä (mi^rs)  'sutiqm  °sus  Yt  10.  65;  —  srao- f^m..laxmym  "jäot  Y.57.1 1;  —  aurvanfym ..yS  °sui  asti  uzgasts  Yt5.i3i;  —  Aqm.- varfittm  . .  yä  saot  *äsyayä  Vr.  7.  3 ;  — buyät  -suua  asps  dtnzrasca  *vais  Yt  13. 52;  —  aspatfks  . .  °savö  Ytij.  12;  — i!  väiäi  dvqnmaibyasca  (sd.)  yaog^t  'sa (ASn.)  sva. '  'die  Schnelligkeit'  Y.  44, 4,  a)  ASn.  'SU  als  Adv.  'cito':  dayä ml  .  .  -SU  Y./i2.4i;  F.  7.
7455:•  j.  äsiäta-  Adj.  'der  schnellste,  rascheste': (mürs)  yS  -ts  yazatanqm  Yl/o.  98;  Y. p.  15;  —  sraohm  .  .  yOnqm  -tsm  Y. 37. 13;  —  «ÖS/  alte  fratihaniayai  °te  (als AP.)''  iataras^t  YL  1^.46;  —  minyahe .  .  vän-^nahe  .  .  yd  vayqm  asti  'tS  Yt.  14. ig.  a)  ASn.  °t)tn  als  Adv.  'am  rasche- sten, aufs  schnellste';  aitim  . .  dämanqm 't>m  zaurväntm  (sd.)  upaitt  ..  V.  JJ.  28; —  ya':ia  't3m  fi-tniaysii  (sd.)  V.  1^.75.
7465:•  j.  Isu.aspa-  Adj.  'der  schnelle  Rosse hat':  laxtnim  staotänm  .  .  "pfm  Yt.  ij. 12;  —  yat  mqm  Iura  pazdayanta  °fia naotaraca'1  Yt.  77.55;  S^.
7467:•  j.  äsu.asp5.'t9ma-  Adj.  'der  die  schnell- sten Rosse  hat':  vTsläsp}  ankam  dahyunqm ••t3m3  *bvat  Yt,5.98.
7468:•  j.  äsu.aspt-  Adj.  'im  Besitz  schneller Stuten':  yatät  mqm  (näml.  aTliii)  tura pazdayanta  'paim  (ASf) ''  naotaraca  Yt. 77.56.
7470:•  j.  äsu.aspya-  n.  'Besitz  schneller  Rosse, Reichtum  an  schnellen  Rossen':  'pTm da'jiiiti  mi%rU  Ytjo.3; —  '^wqm  naracit yöi  taxma  Jat'iyhnte  -ptm  YL5.86;  98.
7474:•  j.  asuya  Adv.  'schnell,  rasch':  moätca 'yaca  Y-tT^u;  FrW.«V.i.
7514:•  j.  äsyah-  Adj.  'der  raschere,  schnellere':
=== leaf 216/217 asu region ===
215 > •  j.,  g.  asav-  Adj.  'schnell,  rasch':  yä (mi^rs)  'sutiqm  °sus  Yt  10.  65;  —  srao- f^m..laxmym  "jäot  Y.57.1 1;  —  aurvanfym ..yS  °sui  asti  uzgasts  Yt5.i3i;  —  Aqm.- varfittm  . .  yä  saot  *äsyayä  Vr.  7.  3 
215 > g.  äsindä  Y.  57.14:  liesäjjnrfä-;  s.  ^sand.
215 > •  j.  äsit-  Adj.  'geniessend';  mä  . .  HB (NP.)  ..  ^caire  (sd.)  Y.jo.14.
215 > •  j.  äsiäta-  Adj.  'der  schnellste,  rascheste': (mürs)  yS  -ts  yazatanqm  Yl/o.  98;  Y. p.  15;  —  sraohm  .  .  yOnqm  -tsm  Y. 37. 13;  —  «ÖS/  alte  fratihaniayai  °te  (als AP.)''  iataras^t  YL  1^.46;  —  minyahe .
215 > •  j.  äsiStsm  Adv.:  s.  asi^ta-.
215 > •  j.  äsu  Adv,:  s.  asav-.
215 > •  j.  Isu.aspa-  Adj.  'der  schnelle  Rosse hat':  laxtnim  staotänm  .  .  "pfm  Yt.  ij. 12;  —  yat  mqm  Iura  pazdayanta  °fia naotaraca'1  Yt.  77.55;  S^.
215 > •  j.  äsu.asp5.'t9ma-  Adj.  'der  die  schnell- sten Rosse  hat':  vTsläsp}  ankam  dahyunqm ••t3m3  *bvat  Yt,5.98.
215 > •  j.  äsu.aspt-  Adj.  'im  Besitz  schneller Stuten':  yatät  mqm  (näml.  aTliii)  tura pazdayanta  'paim  (ASf) ''  naotaraca  Yt. 77.56.
215 > •  j.  äsu.aspya-  n.  'Besitz  schneller  Rosse, Reichtum  an  schnellen  Rossen':  'pTm da'jiiiti  mi%rU  Ytjo.3; —  '^wqm  naracit yöi  taxma  Jat'iyhnte  -ptm  YL5.86;  98.
215 > Abicit.  aus  äsu.aspa-.  —  ai.  äh/ohya-  n.
215 > •  j.  äsu.xSvaewa-  Adj.  'sich  rasch  (da- hin)schwingend':  HÜnm  . .  °tti»rn  Yt.  (^.  37.
215 > •  j.  asuya  Adv.  'schnell,  rasch':  moätca 'yaca  Y-tT^u;  FrW.«V.i.
215 > •  j.  äsu.yasna-  Adj.  'der  den  Y.  rasch vollziehen  kann' :  haomS  .  .  ytm  zaotänm slayata  ahurB  mazdh  °n?m  bsrizi^ä^r^m; yazata  zaota  "rtö  Yt  lo.  89.
217 > •  j.  äsyah-  Adj.  'der  raschere,  schnellere':
```


## [2026-09-07T20:31:36.774Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; cat > /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/71.vision.txt <<'EOF'\n[BQT vol. 1 (Borhan-e Qate', ed. Mo'in), printed page 71 = archive.org borhan-ghate-v1 leaf n281.\nRead from the leaf image https://iiif.archive.org/iiif/borhan-ghate-v1%24281/full/1400,/0/default.jpg\n(running head \"-۷۱-\", side head \"آهو\"); the local BQT_v1_pages.txt OCR of this leaf was unusable.\nRead 2026-09-07 for data/verification/page-373.json (root \"Ôku\", node âhŭk/âhŭ).]\n\n--- main column (bottom of col. 1), headword آهو ---\nآهو ۴ ـ بر وزن کاهو، جانورست معروف ۴ که بتازی غزال خواندش ـ و مطلق ...\n(continues on p.72)\n\n--- Mo'in's etymological footnote no. 4, foot of p. 71, verbatim ---\n۴ ـ از صفت اوستایی âsu بمعنی تیزرو، سانسکریت âsáv «بارتولمه ۳۹،۳۳۸»، در\nپهلوی âhûk «داونوالا ۲۷۲»، سغدی âsuk «بنونیست ۲۱۲»، گیلکی âhî، برنی و نطنزی\nâhû «دك ۱. ص۲۸۷»، سمنانی ahu، سنگسری و سرخهٔ ولاسگردی و شهمیرزادی âhû «ك ۲.\nص ۱۸۴».\n\n(= \"From the Avestan adjective âsu meaning 'swift-going', Sanskrit âsáv [Bartholomae\n338, 39]; in Pahlavi âhûk [Dhabhar/Dawnwala 272]; Sogdian âsuk [Benveniste 212];\nGilaki âhî; Farizandi and Natanzi âhû; Semnani ahu; Sangesari, Sorkha'i-Lasgerdi and\nShahmirzadi âhû.\")\n\n[Other footnotes on the same page: no. 1 to آهنگ (Av. thang 'to pull', Pahl. âhang);\nno. 5 to آهنگر (Pahl. âsin-kar).]\nEOF\necho written; wc -l data/verification/sources/refs/ocr/BQT/71.vision.txt"
}
```


### [2026-09-07T20:31:36.835Z] TOOL RESULT

```
written
22 data/verification/sources/refs/ocr/BQT/71.vision.txt
```


## [2026-09-07T20:31:41.140Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \"https://en.wiktionary.org/wiki/%D8%A2%D9%87%D9%88\" \"https://en.wiktionary.org/wiki/%D9%86%D8%B4%D8%A7%D9%86\" \"https://en.wiktionary.org/wiki/%E1%BD%A8%CE%BA%CE%B5%CE%B1%CE%BD%CF%8C%CF%82\" \"https://www.etymonline.com/word/ocean\" \"https://en.wiktionary.org/wiki/accipiter\" \"https://en.wiktionary.org/wiki/%D8%A3%D9%88%D9%82%D9%8A%D8%A7%D9%86%D9%88%D8%B3\"; do python3 tools/fetch_source.py \"$u\" --note \"pdf page 373 (book 343), roots Ôku / Okw: âhû, nešân, Ōkeanos/ocean, accipiter, Arabic ūqyānūs\" 2>&1 | tail -2; done"
}
```


### [2026-09-07T20:31:44.178Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/844b9204c5629849.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ab4069debfcc7a0b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1eb5155215338938.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cf916d46b2330595.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2991da7a26dcb077.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ee65922e97dce33c.txt
```


## [2026-09-07T20:31:56.715Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt71-373.jpg ocr/BQT/71.png 2>/dev/null; ls -la ocr/BQT/71.*; echo \"=== KLN window ===\"; grep -n \"^window, n\\|window, n\\. —\" KLN_1971.txt | head -3; echo \"=== KLN eye ===\"; grep -n \"^eye, n\\. —\\|eye, n\\.\" KLN_1971.txt | head -3; echo \"=== KLN optic ===\"; grep -n \"^optic, adj\\|synopsis, n\\|autopsy, n\" KLN_1971.txt | head -5; echo \"=== WEB accipiter ===\"; grep -n -i \"accipiter\" WEB_vol1.txt | head -3"
}
```


### [2026-09-07T20:31:58.160Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 257093 Sep  7 16:31 ocr/BQT/71.png
-rw-rw-r-- 1 sfmqrb sfmqrb   1476 Sep  7 16:31 ocr/BQT/71.vision.txt
=== KLN window ===
267446:window, n. — ME. windoge, windowe , fr. ON. 
=== KLN eye ===
89410:eye, n. — ME. eige, eye , eie, fr. OE. eage, rel. to 
264657:walleye, n., eye with a whitish cornea. — Back 
=== KLN optic ===
23596:autopsy, n., post-mortem examination of a body. 
115799:optic, adj. 
167966:optic, adj., pertaining to the eye or sight. — MF. 
239548:synopsis, n., a general view, outline. — Late L., 
=== WEB accipiter ===
1631:[Obs. ac-cip/i-tér, z. {L., a bird of prey, from ac- cipere; ad, to, and capere, to or seize] 1. in ornithology, any of an order of birds of prey, the Raplores. 3 2. a bandage tor the nose: so called from its resembiance to a hawk’s claw. è ac-cip’i-tral, a. of or like an accipiter,
```


## [2026-09-07T20:32:05.165Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"--- window\"; sed -n '267446,267456p' KLN_1971.txt; echo \"--- eye\"; sed -n '89410,89418p' KLN_1971.txt; echo \"--- optic\"; sed -n '167966,167974p' KLN_1971.txt; echo \"--- synopsis\"; sed -n '239548,239554p' KLN_1971.txt"
}
```


### [2026-09-07T20:32:05.353Z] TOOL RESULT

```
--- window
window, n. — ME. windoge, windowe , fr. ON. 
vindauga , lit. ‘windeye’. See wind, ‘air in motion 7 , 
and eye. 

Derivatives: window , tr. v., windo w-ed, adj., 
window-less, adj. 

Windsor, n., 1) the Windsor bean; 2) a Windsor 
chair; 3) Windsor soap. — Named after Wind- 
sor, a town in Berkshire, England, 
wine, n. — ME. win , fr. OE. win , fr. L. vinvm , 
--- eye
eye, n. — ME. eige, eye , eie, fr. OE. eage, rel. to 
OS. dga, OFris. age , ON. auga , Swed. oga , Dan. 
eie , OFris. age, MDu. dghe , Du. oog, OHG. 
ouga, MHG. ouge, G. Auge, Goth, augo, ‘eye’, 
fr. I.-E. base *oq w -, ‘to see; eye’, whence also 
OI. dk$i, gen. akfndh, ‘eye’, ak$ah, ‘die’, tk$ate. 



--- optic
optic, adj., pertaining to the eye or sight. — MF. 
(= F.) optique, fr. ML. opticus , fr. Gk. otctixog, 
‘pertaining to the eyes or sight’, fr. 6ttt6<; 1 ‘seen; 
visible’, verbal adj. of 3<J>o{jlou, ‘I shall see’, fr. 
I.-E. base *oq w -, ‘eye; to see’, whence also 6^, 
gen. 6tc6s, ‘eye, face’, ‘sight’, onumot, ‘I 



--- synopsis
synopsis, n., a general view, outline. — Late L., 
fr. Gk. auvcnjxi;, ‘general view’, lit. ‘a seeing to- 
gether’, fr. crov (see syn-)" and ‘sight, view’. 

See -opsis. 

synoptic, adj., pertaining to a synopsis. — ModL.
```


## [2026-09-07T20:32:15.843Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"ers-  ,laufen\\|kers-\\|k̑ers-\" POK_full.txt | head -6; grep -n \"583\" POK_02.txt | head -3"
}
```


### [2026-09-07T20:32:15.934Z] TOOL RESULT

```
44868:Note: compare also ker-3ax\(i kers-1. 
46328:Note: often extended with -/and -u, s. the extensions kerb(h)-ax\6 kers- 
46432:Root / lemma: kers- 
50244:extension the color root /re/'- (see S. 583 kers-), MiJhlenbach-Endzelin II 383. 
50433:*kers- because of common Italic lllyrian rs- > rr-). 
50661:Kspvai, K£pva PI. 'transverse processes of the vertebrae' {*kern- or *kers-n); Kpayv^v 
66:Vgl.  die  ähnlichen  Schallwurzeln  *ger-  und  *guer-. WP.  I  537.  WH.  I  583.
575:Dazu    vielleicht    russ.    gröcliot   ,Lärm,   Krachen^   lautes  Lachen'  u.  dgl. a,ls  jüngere  Schallnachahmung. WP.  I  591  ff.,  WH.  I  583,  601  f.,  615,  624,  Specht  Dekl.  48,  Trautmann
1005:WP.  I  536,  WH.  I  52,  583,    Trautmann  365  f.,    Specht  Dekl.  47,  204.
```


## [2026-09-07T20:32:18.597Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '46432,46460p' POK_full.txt"
}
```


### [2026-09-07T20:32:18.659Z] TOOL RESULT

```
Root / lemma: kers- 

Meaning: a kind of colour (black) 

Note: and probably also bloftes ker-, compare also kel-4 and ker-6. 

Material: Old Indie krsna-^b\acV! = Old Prussian kirsnands., FIN Kirsnappe= Old 

Bulgarian crbPb, russ. cerenb, Serbo-Croatian crn etc. "black' {*cbrxnb, *cbrsnb)\ without - 

/7o-forms Lithuanian kersas^ mottled, speckled black and white, *tabby', kerse' dappled 

cow', /re/^/s "black dappled ox', kersulis^ Ringeltaube '; karsisi. "Brassen, lead (fish)', 

k/rs/ysm. "ash'; the intonation from kersasi\ts but not to Old Indie; 



Note: 

Old Church Slavic: crbnb'b\ack' : Lithuanian: k/rsnas'b\ack (of a horse)' : Old Prussian: 

kirsnan 'black' : Krishna " Vedic black god ' 

Swedish Norwegian harr^ ash ' {*harzu-)\ Old English heard-hara, heardra-m.. Modern 
High German holl. harder, herder^ sea-asW. 

References: WP. I 428 f., Trautmann 118, 134 f. 
Page(s): 583
```


## [2026-09-07T20:32:26.895Z] TOOL CALL #88: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"kers-2\\|kers-.\\. To run\\|To run\\.\" AHD_watkins1985.txt | head -5; grep -o \"kers-2\\?\\. *[A-Za-z ,.']\\{0,120\\}\" AHD_watkins1985.txt | head -5"
}
```


### [2026-09-07T20:32:28.338Z] TOOL RESULT

```
384:dhgvher-. To run. Perhaps Greek phtheir, louse: (ICH), PHTHIRIASIS. [Pok. g¥hdher- 487.]
388:dhregh-. To run. 1. Greek trekhein (< *threkhein), to run (> trokhos, wheel): TROCHAL, TROCHANTER, TROCHE, TROCHEE; TROCHOPHORE. 2. O-grade form *dhrogh- in Greek trokhileia, trokhilia, system of pulleys, roller of a windlass: TROCHLEA, TRUCK!, (TRUCKLE). [Pok. 1. dhregh- 273.]
623:(SCARCE). 3. Greek karpos, fruit: -cARP, CARPEL, CARPO-, -CARPOUS. [In Pok. 4. sker- 938.] kers-'. Dark, dirty. 1. Suffixed form *ker(s)-no- in Rus- sian chérnyi (feminine chérnaya), black: CHERNOZEM. 2. Suffixed zero-grade form *krs-no- in Sanskrit krsna-), black, dark: KrisHNa. [Pok. kers- 583.] kers-2. To run. Zero-grade form *krs-. 1. Latin currere (past participle cursus), to run: CORRIDOR, (CORSAIR), COURANTE, COURIER, COURSE, CURRENT, CURSIVE, CUR- SOR, CURULE; CONCOURSE, CONCUR, DECURRENT, DIS- COURSE, EXCURSION, HUSSAR, INCUR, INTERCOURSE, OCCUR, PERCURRENT, PRECURSOR, RECOURSE, RECUR, succor. 2. Suffixed form *krs-o- in Gaulish carros, a wagon, cart, in: a. Latin carrus, a two-wheeled wagon: CAR, CAREER, CARGO, CARICATURE, CARIOLE, CAROCHE, (CARRY), CHARGE, CHARIOT; b. Latin carpentum, a two- wheeled carriage: CARPENTER. [Pok. 2. fers- 583.] kert-. To turn, entwine. I. Zero-grade form *krt-. 1. Suf- fixed form *krt-i- in Germanic *hurdiz, wickerwork frame, hurdle, in: a. Old English hyrdel, hurdle, frame: HURDLE; b. Old French hourd, fence, hurdle, scaffold: HOARDING. 2. Suffixed form “*krt-sti- in Germanic *hur- sti- in Old High German hurst, thicket: Horst. II. Per- haps suffixed variant form *krot-i- in Latin crdatis, wickerwork hurdle: CRATE, GRATE?, (GRID), GRIDDLE; (GRIDIRON). [Pok. kert- 584.] kes-'. To scratch. 1. Germanic *hezd6 in Old English heordan, coarse parts of flax: HARDS. 2. Extended form *kseu- in Greek xuein, to scrape: XYSTER. 3. Nasalized form *ks-n-eu- in: a. Germanic *snaww- in Old Norse snéggr, “close-cropped,” perhaps akin to the source of snuG!: b. Latin novdcula, razor: NOVACULITE. [Pok. kes- 585.] kes-2. To cut. Variant kas-. 1. Suffixed form *kas-tro- in: a. Latin castrare, to castrate: CASTRATE; b. Latin cas- trum, fortified place, camp (perhaps “separated place”): CASTLE. 2. Suffixed form *kas-to- in Latin castus, chaste, pure (< “cut off from, free of, faults”): CASTE, CHASTE; CASTIGATE, INCEST. 3. Suffixed (stative) form *kas-é- in Latin carére, “to be cut off from,” lack: CARET. 4. Ex- tended geminated form *kasso- in Latin cassus, empty, void: (CASHIER), QUASH. [Pok. hes- 586.] kes-°. To order. Suffixed 0-grade form *kos-mo- in Greek kosmos, order: COSMOS; MACROCOSM, MICROCOSM. keu-' Also ekeu-. To perceive, see, hear. O-grade form *akou-. 1. Extended form *kous- in: a. Germanic *haus- Jan in (i) Old English hieran, to hear: HEAR (ii) Old English he(o)rcnian, to harken: HEARKEN; b. suffixed form *9-kous-yo- in Greek akouein, to hear: ACOUSTIC. 2. Variant *skou- in: a. Germanic *skauwon in (i) Old English scéawian, to look at: SHOW (ii) Flemish scauwen, to look at: SCAVENGER; b. Germanic *skaunjaz in Mid- dle Dutch schoon, beautiful, bright (< “conspicuous, attractive”): SCONE; Cc. Germanic *skauniz in Old Eng- lish sciene, bright, sheen: SHEEN. [Pok. 1. keu- 587.] keu-?. Base of various loosely related derivatives with assumed basic meaning “to bend,” whence “a round or hollow object.” I. Extended forms *keub-, *keup-. 1. Ger- manic *haup- in: a. Old English héap, heap: HEAP; b. Dutch hoop, heap, troop: FORLORN HOPE. 2. Germanic *hupp-, to leap (by first bending the legs), in Old English hoppian, to hop: HoP!. 3. Germanic *Aupiz in Old Eng- lish hype, hip: H1P!. 4. Zero-grade form *kup-, vessel, in: a. suffixed form *kup-s- in Greek kupselé, chest, hollow vessel: CYPSELA; b. long-vowel form *kip- in (i) Ger- manic *Aifi- in Old English hyf, hive: HIVE (ii) suffixed form *kip-a in Latin cupa, tub, vat: CUPOLA, CUPULE; c. expressive form *kupp- in Late Latin cuppa, drinking vessel: cup. 5. Zero-grade form *kub- in: a. Greek kubos, cube: CUBE; b. suffixed form *kub-@- in (i) Latin cubdre, to lie down on (< “to bend down, prostrate”): COUVADE, COVEY, CUBICLE; CONCUBINE, INCUBATE, SUCCUBUS (ii) Latin cubitum, elbow: CUBIT; Cc. nasalized form *ku-m-b- in (i) Latin -cumbere, to lie down, recline: ACCUMBENT,
1334:CANDENT kand- CANDID kand- CANDIDA kand- CANDIDATE kand- CANDLE kand- CANDOR kand- CANESCENT kas- CANICULA kwon- CANINE kwon- CANKER kar-1 CANNABIS kannabis CANOROUS_ kan- CANT? kan- CANTABILE kan- CANTEEN kanto- CANTICLE kan- CANTILLATE kan- CANTO kan- CANTON kanto- CANTOR kan- CANVAS kannabis CANZONE kan- CAPABLE kap- CAPACIOUS kap- CAPE2 kaput CAPELLA kapro- CAPIAS kap- CAPITAL! kaput CAPITAL? kaput CAPITATE kaput CAPITATION kaput CAPITELLUM kaput CAPITULATE kaput CAPITULUM kaput CAPO! kaput CAPON skep- CAPRIC ACID kapro- CAPRICE kaput CAPRICORN kapro-, ker-1 CAPRIFIG kapro- CAPRIOLE kapro- CAPROIC ACID kapro- CAPSICUM kap- CAPSID kap- CAPSTAN kap- CAPSULE kap- CAPTAIN kaput CAPTION kap- CAPTIOUS kap- CAPTIVATE kap- CAPTIVE kap- CAPTOR kap- CAPTURE kap- CAR kers-2 CARAMEL kolem- CARAT ker-1 CARAVANSARY tere-2 CARBON ker-4 CARBUNCLE ker-4 CARCINO-  kar-1 CARCINOGEN kar-1 CARCINOMA kar-1 CARD? kars- CARDIA kerd-1 CARDIAC kerd-1 CARDIO- kerd-1 CARDOON kars- CARE gar- CAREEN kar-1 CAREER kers-2 CARESS ka- CARET kes-2 CARGO kers-2 CARICATURE kers-2 CARIES ker-5 CARILLON kWetwer- CARINA kar-1 CARIOLE kers-2 CARL karlaz CARLING karlaz CARMINATIVE kars- CARNAGE sker-1 CARNAL sker-1 CARNASSIAL_ sker-1 CARNATION sker-1 CARNET kWetwer- CARNIVAL legh-, sker-1 CARNIVOROUS = sker-1 CAROCHE kers-2 CAROL aulo- CAROTID ker-1 CAROUSE ud- CARP! ger-2 “CARP kerp- CARPAL kwerp- CARPEL kerp- CARPENTER kers-2 CARPET kerp- CARPO- kerp-
1335:-CARPOUS kerp- CARPUS kwerp- CARRION sker-1 CARROT ker-1 CARRY kers-2 CART ger-2 CARUNCLE = sker-1 CARVACROL ak- CARVE gerbh- CASCADE kad- CASCARA kwét- CASE! kad-
kers-2. To run. Zer
```


## [2026-09-07T20:33:29.124Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,80p' tools/verify_check.py"
}
```


### [2026-09-07T20:33:29.163Z] TOOL RESULT

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


## [2026-09-07T20:33:32.053Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '80,140p' tools/verify_check.py"
}
```


### [2026-09-07T20:33:32.117Z] TOOL RESULT

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


## [2026-09-07T20:33:36.237Z] AGENT

Now I'll write the verification file.


## [2026-09-07T20:42:52.614Z] TOOL CALL #91: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-373.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_AHU   = \"https://en.wiktionary.org/wiki/%D8%A2%D9%87%D9%88\"\nW_NESAN = \"https://en.wiktionary.org/wiki/%D9%86%D8%B4%D8%A7%D9%86\"\nW_OKE   = \"https://en.wiktionary.org/wiki/%E1%BD%A8%CE%BA%CE%B5%CE%B1%CE%BD%CF%8C%CF%82\"\nE_OCEAN = \"https://www.etymonline.com/word/ocean\"\nW_ACC   = \"https://en.wiktionary.org/wiki/accipiter\"\nW_UQY   = \"https://en.wiktionary.org/wiki/%D8%A3%D9%88%D9%82%D9%8A%D8%A7%D9%86%D9%88%D8%B3\"\n\nPOK775_OKU = (\"Pokorny IEW p.775 (local POK_03.txt leaf 9, the leaf carrying the printed '775'): \"\n  \"\\\"ōkú-s ,schnell', Kompar. ōkiōs, Superl. ōkisto-. Ai. āśú- ,schnell', Kompar. āśíyān, Superl. \"\n  \"āśiṣṭha-, av. āsu- ,schnell', Kompar. āsyā, Superl. āsištō-, gr. ὠκύς, ὤκιστος, lat. ōcior \"\n  \",schneller', Superl. ōcissimus (Positiv fehlt) ... vielleicht im Ablaut zu ak-/ok- ,scharf'; dann \"\n  \"könnten lat. acu-pedius ,schnellfüßig' und accipiter ,Habicht, Falke' auch hierher gehören.\\\"\")\n\nPOK775_OKW = (\"Pokorny IEW pp.775-777 (local POK_03.txt leaves 9-11): \\\"ok̑ʷ- ,sehen'; ok̑ʷ-, ok̑ʷi-, \"\n  \"ok̑ʷ(e)n- (dieser St. in den Kasus obliqui), ok̑ʷ(e)s-, ok̑ʷ-p- ,Auge'\\\"; the entry lists \\\"av. aši \"\n  \"für *axšī nach uši ,Ohren', vgl. av. aiwy-āxšayeinti ,sie beaufsichtigen', aiwyāxštar- ,Aufseher'\\\", \"\n  \"\\\"got. augō, aisl. auga, ahd. ouga, ags. ēage n. ,Auge'\\\", \\\"vom n-St. serb.-ksl. okno ,Fenster'; vgl. \"\n  \"engl. (aisl. Lw.) wind-ow ds., eig. ,Windauge'\\\" and Gk. ὄψομαι/ὄψις.\")\n\ne0 = {\n \"entry\": 0,\n \"root\": \"Ôku\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *h₂ōḱus (older notation *ōḱú-s) 'swift, fast'\",\n \"note\": (\"Root box, language label, gloss and reference are all right: Pokorny 775 has exactly \"\n   \"ōkú-s 'schnell' with the Avestan comparative series Nourai reproduces. In current notation the root \"\n   \"is *h₂ōḱus, generally taken as a lengthened-grade u-stem beside *h₂eḱ- 'sharp' (Pokorny already: \"\n   \"\\\"vielleicht im Ablaut zu ak-/ok- 'scharf'\\\"), which is why some handbooks (Klein, Mann, Le Feuvre) \"\n   \"file accipiter under 'sharp' rather than 'swift'. Two of the four branches under the root are sound \"\n   \"(the Iranian āsu-/āhūg/āhū branch and the Latin accipiter branch); the Avestan karšiptar- branch \"\n   \"(#5-#7) belongs to a different root (*ḱers- 'to run', Pokorny 583), and the Ōkeanos branch (#11-#15) \"\n   \"rests on an ancient folk etymology that modern Greek scholarship rejects.\"),\n \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *h₂ōḱus (به نگارش کهن‌تر *ōḱú-s) «تیز، تندرو» است و همان است که \"\n   \"پوکورنی در ص ۷۷۵ آورده، با همان سه صورت اوستایی āsu / āsyā / āsištō که نورایی نقل کرده؛ پس جعبهٔ ریشه، \"\n   \"برچسب زبانی، معنا و ارجاع همه درست است. امروز این ریشه را ستاکِ u-دارِ کشیده‌واکه در کنار *h₂eḱ- «تیز» \"\n   \"می‌دانند و پوکورنی نیز خود احتمال «تناوب آوایی با ak-/ok- (تیز)» را داده است؛ از همین رو کلاین و مان \"\n   \"واژهٔ لاتینی accipiter را زیر «تیز» می‌آورند. از چهار شاخهٔ این نمودار، شاخهٔ ایرانی (āsu ← āhūg ← آهو) و \"\n   \"شاخهٔ لاتینی (accipiter) استوارند؛ اما شاخهٔ karšiptar- به ریشهٔ دیگری (*ḱers- «دویدن»، پوکورنی ۵۸۳) \"\n   \"می‌رسد و شاخهٔ Ōkeanos بر ریشه‌شناسی عامیانهٔ کهنی تکیه دارد که پژوهش امروزی آن را رد می‌کند.\"),\n \"sources\": [W_AHU, W_ACC, E_OCEAN],\n \"ref_check\": [\n   {\"ref\": \"POK:775\", \"status\": \"supports\", \"note\": POK775_OKU}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I p.172 s.v. ōku-s (incoming/WLD/WLD_Bd1_pages.txt around line 15770)\",\n    \"stance\": \"supports\",\n    \"note\": \"\\\"ōku-s ,schnell'. Ai. āśu- ,schnell' ... av. āsu- ,schnell', Komp. āsyā, Sup. āsišta-. gr. ὠκύς ... lat. ōcior ,schneller', Sup. ocissimus (Positiv fehlt)\\\" — the direct source of Pokorny 775; adds the caution \\\"Eine Ablautform *aku ,schnell' steht nicht fest.\\\"\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ōku- (AHD_watkins1985.txt leaf 796)\", \"stance\": \"supports\",\n    \"note\": \"\\\"ōku-. Swift. Zero-grade form *aku- in compound *oku-petro-, 'swift-flying,' in Latin accipiter, hawk (*pet-ro-, flying; see pet-): ACCIPITER. [Pok. ōku-s 775.]\\\"\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. ōkus (IEC.txt line 12097)\", \"stance\": \"partial\",\n    \"note\": \"\\\"ōkus, os 'sharp, keen, swift'. WP I, 172. Skt. āśúh 'quick'; Av. āsuš ... Gk. okús 'swift, sharp' ... Lat. cf. ocior, ocius\\\" — Mann keeps 'sharp' and 'swift' in one lemma, i.e. does not separate *h₂eḱ- from *h₂ōḱus.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 14.21 SWIFT, FAST, QUICK (SYN.txt line 24641)\", \"stance\": \"supports\",\n    \"note\": \"Buck's row for the concept 'swift' gives \\\"Grk. ταχύς, ὠκύς ... Skt. āśu- ... Av. āsu-, aurvant-\\\" — the Avestan/Greek words of nodes #1 and #10 are the standard words for 'swift'.\"}\n ],\n \"nodes\": []\n}\n\nn = e0[\"nodes\"].append\n\nn({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"âsu; âsya; âs-išto\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Av. āsu- (nom. sg. m. āsuš, adv. āsu) 'swift, quick' is the regular Iranian reflex of \"\n   \"*h₂ōḱus: PIE *ōḱ- > Indo-Iranian *āś- (satem palatalisation of *ḱ), whence Skt. āśú- and Av. āsu- \"\n   \"(Iranian *ś > s). The comparative āsyah- (nom. āsyō, Nourai's 'âsya') continues *-yes-/-yos- and the \"\n   \"superlative āsišta- continues *-isto- — exactly the *ōkiōs / *ōkisto- pair Pokorny reconstructs (cf. \"\n   \"Gk. ὠκίων/ὤκιστος). All three are attested in the Young Avesta: āsu- of Mithra's swiftness (Yt.10.65), \"\n   \"āsišta- 'swiftest of the yazatas' (Yt.10.98), āsyah- in Vr.7.3. The 'Isto' cross-reference is to \"\n   \"Nourai's separate entry for the superlative suffix.\"),\n \"derivation_fa\": (\"صفت اوستایی āsu- «تیز، تندرو» بازماندهٔ منظمِ *h₂ōḱus هندواروپایی است: *ḱ در شاخهٔ \"\n   \"هندوایرانی به ś و در ایرانی به s بدل شده، پس *ōḱu- > هندوایرانی *āśu- > اوستایی āsu- (سنسکریت āśú-). \"\n   \"صورت برترِ āsyah- (حالت فاعلی āsyō، همان «âsya»ی نورایی) از پسوند سنجشی *-yos- و صورت برترین āsišta- از \"\n   \"*-isto- ساخته شده‌اند، درست همان جفتی که پوکورنی بازسازی می‌کند (قس یونانی ὠκίων/ὤκιστος). هر سه صورت در \"\n   \"اوستای نو گواهی دارند (یشت ۱۰٫۶۵، ۱۰٫۹۸، ویسپرد ۷٫۳). ادعای نورایی درست است.\"),\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"POK:775\", \"status\": \"supports\", \"note\": POK775_OKU + \" Pokorny prints Nourai's three forms verbatim (āsu-, āsyā, āsištō-).\"}],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"AiW cols. ~338-344 (BRT.txt leaves 215-217)\", \"stance\": \"supports\",\n    \"note\": \"\\\"j., g. āsav- Adj. 'schnell, rasch'\\\" (with ASn. āsu as adverb 'cito'), \\\"j. āsišta- Adj. 'der schnellste, rascheste'\\\", \\\"j. āsyah- Adj. 'der raschere, schnellere'\\\" — the three grades as in the chart; Mo'in cites this very place as 'بارتولمه ۳۳۸، ۳۹'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ōku-\", \"stance\": \"silent\",\n    \"note\": \"The appendix cites only the Latin outcome under ōku-; the Avestan comparative series is not listed (Watkins never lists Iranian comparatives).\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 14.21\", \"stance\": \"supports\", \"note\": \"\\\"Av. āsu-, aurvant-, θwaša-, xšviwra-\\\" as the Avestan words for 'swift'.\"}\n ],\n \"derivation_note\": None\n})\n\nn({\n \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"âhŭk 1, âhŭg\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"MP āhūg (Book Pahlavi ʾhwk', Manichaean ʾyhwg) 'gazelle, deer' < Old Iranian *āsuka- \"\n   \"'the swift one', a -ka- derivative of *āsu- 'swift' used as an animal name. The phonetics are regular \"\n   \"for Persian: intervocalic Old Iranian *-s- became -h- in Middle Persian (the same change as *masya- > \"\n   \"MP māhīg > NP māhī 'fish'), and *-uka- > -ūg; the non-Persian Iranian languages keep the s, which is \"\n   \"why Kurdish āsk, Baluchi āsk, Pashto ōsai and Sogdian ʾsʾwk (#4) all show -s-. Nourai's two spellings \"\n   \"are simply the older (āhūk, Horn's transcription of ʾhwk') and the modern (āhūg) readings of the same \"\n   \"word; the '1' distinguishes it from the homonym āhōg 'fault, blemish' (< Av. āhita-), which is Nourai's \"\n   \"separate root 'Ahu' on pdf p.38.\"),\n \"derivation_fa\": (\"فارسی میانهٔ āhūg (به خط پهلوی ʾhwk'، در مانوی ʾyhwg) «غزال، آهو» از ایرانی باستان \"\n   \"*āsuka- است، یعنی صفت *āsu- «تیزرو» با پسوند -ka- که نام جانور شده است. دگرگونی آوایی قاعده‌مند است: \"\n   \"*s ایرانی باستان در میان دو واکه در فارسی میانه به h بدل می‌شود (همان تحولی که *masya- را به māhīg و \"\n   \"«ماهی» رساند) و *-uka- به -ūg. دیگر زبان‌های ایرانی s را نگه داشته‌اند: کردی āsk، بلوچی āsk، پشتو ōsai و \"\n   \"سغدی ʾsʾwk. دو صورتِ نورایی (āhūk و āhūg) تنها دو خوانشِ کهن و نوِ یک واژه‌اند، و شمارهٔ ۱ آن را از همنامش \"\n   \"āhōg «عیب» (از اوستایی āhita-) جدا می‌کند. ادعای نورایی درست است.\"),\n \"sources\": [W_AHU],\n \"ref_check\": [\n   {\"ref\": \"BQT:71\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qate' ed. Mo'in, printed p.71 (archive.org borhan-ghate-v1 leaf n281, running head '-۷۱-'; read from the leaf image, transcription saved to data/verification/sources/refs/ocr/BQT/71.vision.txt, image copied to .../ocr/BQT/71.png). Mo'in's footnote 4 to آهو: 'از صفت اوستایی âsu بمعنی تیزرو، سانسکریت âsáv «بارتولمه ۳۹،۳۳۸»، در پهلوی âhûk «داونوالا ۲۷۲»، سغدی âsuk «بنونیست ۲۱۲»...' — Nourai's arrows #1→#2 and #1→#4 are Mo'in's own words.\"},\n   {\"ref\": \"SOD:10\", \"status\": \"supports\",\n    \"note\": \"Gharib, Sogdian Dictionary entry 258 (printed p.10; SOD.txt line 9195, SOD_pages.txt leaf 75 whose page numeral is '10'): '258 ʾsʾwk B / asūk (ʾswk) < *āsuka-, Av. āsu-, Pahl. āhug / gazelle' — the etymology of the whole node chain in one line.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p.7 (PHD.txt leaf 28)\", \"stance\": \"supports\",\n    \"note\": \"\\\"āhūg [TYBA < A ...; ʾhwk' | M ʾyhwg, N āhū] gazelle\\\" — and, three lines earlier, the separate \\\"āhōg [ʾhwk' | M ʾhwg, N āhū] fault, blemish\\\", confirming that Nourai's numbering of two homonyms is right.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn no. 59, p.15 (HRN.txt line 974)\", \"stance\": \"supports\",\n    \"note\": \"\\\"59. āhū 'Gazelle'. phlv. āhūk 'Gazelle'. kurd. āsk; afγ. ōsai; bal. āsk, LW. āhū; yaγ. LW. āhū\\\" — Horn's Kurdish/Baluchi/Pashto forms with -s- are the evidence for *āsu-ka-.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II, Glossary\", \"stance\": \"silent\",\n    \"note\": \"grep 'āhūg', 'āhūk', 'ʾhwk' in NYB_vol2_glossary.txt returns nothing: the word does not occur in Nyberg's texts.\"}\n ]\n})\n\nn({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"âhŭ 1 «آهو ۱»\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"NP آهو āhū 'deer, gazelle' is MP āhūg with the regular loss of final -g after ū in New \"\n   \"Persian (MP āhūg > NP āhū exactly as MP bāg > NP bā, MP nāxūg-type finals); the word is old in New \"\n   \"Persian and standard in the Shahnameh. The Central-dialect forms Mo'in lists (Semnani ahu, Sangesari/\"\n   \"Sorkhaʾi/Lasgerdi/Shahmirzadi āhū, Gilaki āhī, Natanzi āhū) show the same Persian-type *s > h, while \"\n   \"Kurdish āsk keeps -sk-. Mo'in's Farhang gives the deer as آهو ۱ (جاندارشناسی: 'جانوری از خانوادهٔ \"\n   \"تهی‌شاخان ... غزال، ظبی') and the homonym 'defect' as آهو ۲, matching Nourai's '1'.\"),\n \"derivation_fa\": (\"«آهو» در فارسی نو دنبالهٔ āhūg فارسی میانه است؛ -g پایانی پس از ū در فارسی نو افتاده \"\n   \"است (āhūg > آهو). واژه از کهن‌ترین متون دری و شاهنامه گواهی دارد. گونه‌های گویشی که معین برمی‌شمارد \"\n   \"(سمنانی ahu، سنگسری و سرخه‌ای و لاسگردی و شهمیرزادی āhū، گیلکی āhī، نطنزی āhū) همه همان ابدال *s > h \"\n   \"فارسی‌گونه را نشان می‌دهند، در برابر کردی āsk که خوشهٔ -sk- را نگه داشته است. در فرهنگ معین نیز «آهو ۱» \"\n   \"همین جانور (غزال، ظبی) و «آهو ۲» همنامِ «عیب» است؛ پس شمارهٔ نورایی درست است.\"),\n \"sources\": [W_AHU],\n \"ref_check\": [\n   {\"ref\": \"MON:109\", \"status\": \"supports\",\n    \"note\": \"Mo'in, Farhang-e Farsi, s.v. آهو (MON_part1.txt lines 5543-5556): 'آهو: (اِ.) (جاند.) جانوری از خانوادهٔ تهی‌شاخان، جزو راستهٔ نشخوارکنندگان ... سریع و چابک ... غزال، ظبی؛ ج. آهوان، آهوها' followed by the second homonym 'آهو: (اِ.) عیب، نقص، بیماری، مرض'. The printed page number cannot be checked in this OCR (no page markers) and the print edition's Latin-script Pahlavi tag was lost in the OCR, but the entry, the gloss and the numbering are exactly as cited.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"Horn no. 59, p.15\", \"stance\": \"supports\", \"note\": \"\\\"59. āhū 'Gazelle'. phlv. āhūk 'Gazelle'\\\" — the New Persian headword itself.\"},\n   {\"src\": \"BQT\", \"where\": \"printed p.71-72 (ocr/BQT/71.vision.txt, 72.vision.txt)\", \"stance\": \"supports\",\n    \"note\": \"'آهو ـ بر وزن کاهو، جانورست معروف که بتازی غزال خواندش' with Mo'in's footnote 4 deriving it from Av. āsu- via Pahl. āhūk.\"},\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien\", \"stance\": \"silent\",\n    \"note\": \"grep 'āhū', 'Gazelle' in HUB.txt gives no entry: Hübschmann does not treat the word (his Part I only supplements selected Horn numbers).\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-ha\", \"stance\": \"silent\",\n    \"note\": \"grep 'آهو' in incoming/ARY/ARY_pages.txt returns only اهورامزدا and آهوش passages, no headword for آهو 'deer'.\"}\n ]\n})\n\nn({\n \"id\": 4, \"lang\": \"Sogdian\", \"words\": \"âs`wk`\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Buddhist Sogdian ʾsʾwk (read āsūk/asūk) 'gazelle' is the same *āsuka- as MP āhūg, but \"\n   \"with Sogdian keeping intervocalic -s- (Sogdian did not share the Persian *s > h) and writing the long \"\n   \"ū with the digraph -ʾw-. Gharib's entry states the etymology herself: '< *āsuka-, Av. āsu-, Pahl. \"\n   \"āhug'. Nourai's transliteration with backticks (âs`wk`) simply renders the aleph/ʾayn of the Sogdian \"\n   \"script. It attests the derivative *āsuka- outside Persian and so secures the arrow #1→#2/#4.\"),\n \"derivation_fa\": (\"سغدی بودایی ʾsʾwk (خوانش āsūk) «غزال» همان *āsuka- است، با این تفاوت که سغدی s میان \"\n   \"دو واکه را نگه داشته (ابدال s > h ویژهٔ فارسی است) و ū کشیده را با -ʾw- می‌نویسد. غریب خود در همان مدخل \"\n   \"ریشه را می‌آورد: «< *āsuka-، اوستایی āsu-، پهلوی āhug». آوانگاری نورایی با نشانهٔ ` تنها الف/عین خط سغدی \"\n   \"را نشان می‌دهد. این گواه سغدی نشان می‌دهد که ساختِ *āsuka- تنها ویژهٔ فارسی نبوده و پیکانِ نمودار درست است.\"),\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"SOD:10\", \"status\": \"supports\",\n    \"note\": \"Gharib, Sogdian-Persian-English Dictionary, entry 258 on printed p.10 (SOD.txt line 9195; SOD_pages.txt leaf 75 carries the numeral '10'): '258 ʾsʾwk* B ... asūk (ʾswk) ©<*āsuka-, Av. āsu, Pahl. āhug / gazelle / SCE 151, 354; GMS 976n, 978'. The English index of the same dictionary lists 'gazelle 258'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"printed p.71, Mo'in's footnote 4 (ocr/BQT/71.vision.txt)\", \"stance\": \"supports\",\n    \"note\": \"'... سغدی âsuk «بنونیست ۲۱۲»' — Mo'in gives the Sogdian form from Benveniste, next to Pahlavi âhûk.\"},\n   {\"src\": \"ISS\", \"where\": \"Bailey, Dictionary of Khotan Saka (ISS_alt_DKS.txt)\", \"stance\": \"silent\",\n    \"note\": \"no Khotanese cognate of *āsuka- found by grep ('āsu', 'aska'); Bailey is not relevant to a Sogdian node.\"}\n ]\n})\n\nn({\n \"id\": 5, \"lang\": \"Avestan / Old Persian\", \"words\": \"karši-ptan\",\n \"verdict\": \"disputed\",\n \"derivation\": (\"The word is real and its meaning is as drawn, but it hangs from the wrong root and \"\n   \"carries a wrong language label. (a) Form: the Avestan bird-name is karšiptar- (Vd. 2.42, of the bird \"\n   \"that carried the Mazdean religion into Yima's vara); 'karšiptan-' is Horn's (and after him Tomaschek's \"\n   \"and Mo'in's) older n-stem citation form, which is also what Nourai copied — not a misprint. (b) \"\n   \"Language: it is Young Avestan only; Kent's Old Persian lexicon has nothing of the kind, so '/ Old \"\n   \"Persian' is wrong. (c) Root: Bartholomae analyses the compound as karši- + *ptar-, agent noun of pat- \"\n   \"'to fly', and derives the first member 'aus *k̑ers-, zu lat. currō, mhd. hurren' — i.e. from PIE *ḱers- \"\n   \"'to run' (Pokorny 583, AHD kers-²), not from *h₂ōḱus. His gloss is precisely 'eig. Schnellflieger', and \"\n   \"he himself compares Gk. ὠκυπέτης / ὠκύπτερος and Lat. accipiter — which is where Nourai's 'swift \"\n   \"flying' and his NOTE 'compare with Latin acu-pedius' come from. So the parallel is Bartholomae's; the \"\n   \"descent from *ōḱu- is Nourai's own and is not accepted.\"),\n \"derivation_fa\": (\"واژه واقعی است و معنایش نیز همان است که در نمودار آمده، اما زیر ریشهٔ نادرست نشسته و \"\n   \"برچسب زبانی‌اش هم درست نیست. یک: صورت اوستایی این نام‌پرنده karšiptar- است (وندیداد ۲٫۴۲، نام مرغی که دین \"\n   \"مزدیسنا را به «ورِ» جمشید برد)؛ «karšiptan-» صورت استنادیِ کهن‌ترِ هرن (و از او توماشک و معین) است و \"\n   \"نورایی همان را نقل کرده، پس خطای چاپی نیست. دو: این واژه تنها اوستایی نو است و در واژه‌نامهٔ پارسی باستانِ \"\n   \"کنت نشانی از آن نیست، پس «پارسی باستان» نادرست است. سه: بارتولومه این ترکیب را karši- + *ptar- (اسم فاعل \"\n   \"از pat- «پریدن») می‌داند و جزء نخست را «از *ḱers-، هم‌ریشه با currō لاتینی و hurren آلمانی میانه» \"\n   \"می‌گیرد، یعنی از ریشهٔ «دویدن» (پوکورنی ۵۸۳) و نه از *h₂ōḱus. معنای او هم درست «تندپرواز» است و خودش \"\n   \"ὠκυπέτης یونانی و accipiter لاتینی را برای سنجش می‌آورد؛ همان جا که «swift flying» و یادداشت نورایی از \"\n   \"آن آمده است. پس سنجشِ ساختاری از بارتولومه است، اما پیوند با ریشهٔ Ôku از خود نورایی است و پذیرفته نیست.\"),\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"BRT:458\", \"status\": \"partial\",\n    \"note\": \"The entry stands one column later than cited: BRT.txt leaf 277 (running head '459 karətayaeča — kasyah- 460') has 'j. karšiptar- m. Name eines Vogels, \\\"accipiter\\\": ... Der Vogel K. V.2.42', with the note 'Komp.: karši- (nur KompA., aus *k̑ers-, IF. 9.261), zu lat. currō, mhd. hurren + *ptar- ... der Kompform des Nom. ag. zum V. pat-; also eig. \\\"Schnellflieger\\\", vgl. gr. ὠκυπέτης, ὠκύπτερος und lat. accipiter'. Column 458 is where Bartholomae's own cross-reference to the Bundahišn gloss points ('karšipt ke čarx xvānīhēt, Sp. 458 m.', BRT.txt leaf 552), so Nourai's page is a near miss, and the reference supports the gloss but explicitly contradicts the root affiliation.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW p.583 kers-² 'to run' (POK_full.txt line 46432 area) vs p.775 ōku-s\",\n    \"stance\": \"contradicts\",\n    \"note\": \"Pokorny keeps the two roots apart: kers- (p.583, whence Lat. currere) and ōku-s (p.775). His ōku-s entry mentions no Iranian compound at all; the Avestan bird is not listed under 775.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kers-²\", \"stance\": \"contradicts\",\n    \"note\": \"\\\"kers-². To run. Zero-grade form *krs-. 1. Latin currere ... [Pok. 2. kers- 583.]\\\" — the root of Bartholomae's karši-, distinct from ōku-.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn no. 857, p.191 (HRN.txt line 7461)\", \"stance\": \"partial\",\n    \"note\": \"\\\"857. kesek 'Elster'. Tomaschek, Pamirdialekte S.771, vergleicht aw. karšiptan-, phlv. karš(i)ft (Deutung nicht sicher)\\\" — this is where the form 'karšiptan-' comes from, and Horn flags the interpretation as uncertain.\"},\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon pp.164-215\", \"stance\": \"silent\",\n    \"note\": \"no karši-/karšipta- of any shape in Kent's Old Persian lexicon (grep 'kars', 'karsi'): the 'Old Persian' half of the language label has no basis.\"}\n ]\n})\n\nn({\n \"id\": 6, \"lang\": \"Pahlavi\", \"words\": \"karšift\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"Pahlavi karšipt / karšift is the Middle Persian continuation of Av. karšiptar-, with the \"\n   \"loss of the final syllable normal in Pahlavi transcriptions of Avestan names and -pt- kept as -ft-. In \"\n   \"the Bundahišn (24.11) it is the ratav (chief) of birds, and there the text glosses it 'karšipt ke čarx \"\n   \"xvānīhēt' — 'karšipt, which is called čarx' (NP čarx, a bird of prey), which is why Bartholomae reads \"\n   \"the name as 'swift-flier'. Nourai's gloss 'a fast bird' is therefore an inference from the Avestan \"\n   \"etymology, not a Pahlavi dictionary gloss: MacKenzie's Concise Pahlavi Dictionary does not carry the \"\n   \"word at all, and the identification of the bird is uncertain (magpie in Horn's chain, čarx in the \"\n   \"Bundahišn, elsewhere a mythical bird).\"),\n \"derivation_fa\": (\"پهلوی karšipt / karšift دنبالهٔ اوستایی karšiptar- است؛ هجای پایانی، چنان‌که در \"\n   \"نام‌های اوستایی در متون پهلوی معمول است، افتاده و خوشهٔ -pt- به -ft- بدل شده است. در بندهش (۲۴٫۱۱) این \"\n   \"مرغ «رَدِ مرغان» است و همان جا آمده «karšipt ke čarx xvānīhēt» یعنی «کرشیپت که چرخ خوانده می‌شود»؛ از \"\n   \"همین گلوسه است که بارتولومه معنی «تندپرواز» را بیرون می‌کشد. پس معنی «مرغی تیزپرواز» که نورایی آورده \"\n   \"استنباط از ریشه‌شناسی اوستایی است، نه معنی فرهنگ‌های پهلوی: در فرهنگ کوچک پهلویِ مکنزی این واژه هیچ \"\n   \"نیامده و هویت خودِ پرنده (زاغی؟ چرخ؟ مرغ اسطوره‌ای؟) روشن نیست. با احتیاط پذیرفتنی است.\"),\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"HRN:191\", \"status\": \"supports\",\n    \"note\": \"Horn, Grundriss p.191 no. 857 (HRN.txt lines 7461-7464, leaf 212 = printed 191): '... vergleicht aw. karšiptan-, phlv. karš(i)ft (Deutung nicht sicher)'. The Pahlavi form is exactly Nourai's, and the page is exactly the one cited.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971\", \"stance\": \"silent\",\n    \"note\": \"grep 'karšift', 'karšipt', 'karsift' in PHD.txt / PHD_mackenzie.txt: nothing. The word is not in MacKenzie's dictionary (it belongs to the Avesta-derived onomastic vocabulary of the Bundahišn).\"},\n   {\"src\": \"BRT\", \"where\": \"AiW footnote at leaf 552 (to yasna frašūmrūta-) and col. 459\", \"stance\": \"supports\",\n    \"note\": \"\\\"Als Ratav der Vögel (mrayō sādakān, murwān) wird Bd. 24.11 und Vr.1.1 Pü. der Vogel Karšipt genannt (zu Bd. 24.11: karšipt ke čarx xvānīhēt, Sp. 458 m.)\\\" — the Pahlavi form and its Bundahišn context.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II Glossary\", \"stance\": \"silent\",\n    \"note\": \"grep 'karšipt' in NYB_vol2_glossary.txt: no entry.\"},\n   {\"src\": \"BQT\", \"where\": \"printed p.1652, Mo'in's footnote 1 (incoming/BQT/BQT_v3_pages.txt, pdf page 445)\", \"stance\": \"supports\",\n    \"note\": \"'قس پهلوی karsh(ift)، اوستایی Karshiptan- (مفهوم آن واضح نیست)' — Mo'in repeats Horn's Pahlavi form and repeats that the sense is not clear.\"}\n ]\n})\n\nn({\n \"id\": 7, \"lang\": \"Persian\", \"words\": \"kašak «کَشَک»\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"Borhan-e Qate' p.1652 does give کشک as 'پرنده‌ای است سیاه و سفید که عربان عقعق خوانند' — \"\n   \"a black-and-white bird which the Arabs call ʿaqʿaq, i.e. the magpie — alongside کشکرک in the same sense, \"\n   \"so the word and the gloss are right (Horn's headword is vocalised kesek, hence Nourai's variants کسک / \"\n   \"کشکک). The descent from karšift is Tomaschek's conjecture of 1880, taken over by Horn (who adds \"\n   \"'Deutung nicht sicher') and from Horn by Mo'in and by Nourai. It is not phonetically regular: MP \"\n   \"karšift would give NP *karšift/*kašift, and the Pamir forms Tomaschek adduced (Wakhi karjope, Sarikoli \"\n   \"karjope, Shughni kšebc) are not derivable from the Persian form either. Modern treatments therefore \"\n   \"leave کسک/کشک as a bird name of unclear, probably imitative origin, and the parallel with the Pamir \"\n   \"words as a resemblance rather than a pedigree. Mo'in's own Farhang keeps the bird under کشکرک and does \"\n   \"not give the bird sense to کشک at all.\"),\n \"derivation_fa\": (\"برهان قاطع (ص ۱۶۵۲) «کشک» را «پرنده‌ای است سیاه و سفید که عربان عقعق خوانند» می‌آورد و \"\n   \"«کشکرک» را نیز به همین معنی؛ پس واژه و معنی درست‌اند (سرواژهٔ هرن با واک‌گذاری kesek است، از این‌رو \"\n   \"گونه‌های کسک و کشکک). اما اشتقاق آن از karšift پهلوی، حدس توماشک (۱۸۸۰) است که هرن آن را با قید «تفسیرش \"\n   \"قطعی نیست» نقل کرده و از هرن به حاشیهٔ معین و از آنجا به نورایی رسیده است. این اشتقاق آواشناسانه \"\n   \"قاعده‌مند نیست: karšift فارسی میانه در فارسی نو *کشیفت می‌داد، و صورت‌های پامیری (وخی karjope، سریکلی \"\n   \"karjope، شغنی kšebc) نیز از صورت فارسی برنمی‌آیند. پژوهش امروزی «کسک/کشک» را نام‌پرنده‌ای با خاستگاه \"\n   \"ناروشن و به احتمال آوابنیاد (نام‌آوا) می‌داند. خودِ فرهنگ معین این پرنده را زیر «کشکرک» آورده و به «کشک» \"\n   \"معنی پرنده نداده است. با احتیاط پذیرفتنی است.\"),\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"BQT:1652\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qate', printed p.1652 = vol.3 pdf page 445 (incoming/BQT/BQT_v3_pages.txt, '[pdf page 445]'; the neighbouring leaves carry the numerals ۱۶۵۱ and ۱۶۵۳). Text: 'کشک ... و آن پرنده‌ای است سیاه و سفید که عربان عقعق خوانند'; and Mo'in's footnote 1: '«کسک» کشکرک (ه.م.)، قس پهلوی karsh(ift)، اوستایی Karshiptan- (مفهوم آن واضح نیست)، وخی karjope، سریکلی karjope، شغنی kshebc (زاغی، کلاغ زاغی = Elster (آلمانی)، magpie (انگلیسی))'. Exactly Nourai's arrow, uncertainty included.\"},\n   {\"ref\": \"MON:2988\", \"status\": \"partial\",\n    \"note\": \"Mo'in, Farhang-e Farsi (MON_part2.txt lines 23545-23570): the headword کشک gives only 'دردی ماست یا دوغ که ... خشک کنند؛ قروت' and the figurative 'هیچ، پوچ'; the magpie is a separate headword کشکرک '(جاند.) پرنده‌ای ... از تیرهٔ کلاغ‌ها ... رنگ پرهایش سیاه و سفید است'. So Mo'in has the bird but not under Nourai's headword, and no etymology. Page 2988 cannot be verified in this OCR (no page markers).\"},\n   {\"ref\": \"HRN:191\", \"status\": \"supports\",\n    \"note\": \"Horn no. 857, p.191: 'kesek \\\"Elster\\\". Tomaschek, Pamirdialekte S.771, vergleicht aw. karšiptan-, phlv. karš(i)ft (Deutung nicht sicher), waz. karjöpc, sar. karjopc, šign. kšebc \\\"Elster\\\"'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"printed p.1652 (vol.3), Mo'in's footnote 1\", \"stance\": \"supports\",\n    \"note\": \"See ref_check: Mo'in gives the whole comparison and marks the sense of the Avestan word as unclear.\"},\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien\", \"stance\": \"silent\",\n    \"note\": \"grep 'kesek', 'Elster' in HUB.txt: no entry; Hübschmann does not comment on Horn no. 857.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-ha\", \"stance\": \"silent\",\n    \"note\": \"grep 'کسک'/'کشک' in incoming/ARY/ARY_pages.txt returns only unrelated strings (کسکر etc.); no IE pedigree offered for the bird name.\"}\n ]\n})\n\nn({\n \"id\": 8, \"lang\": \"Latin\", \"words\": \"acu; acu-pedius, acci-piter\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"The compounds are right, the free-standing 'acu' is not. Latin has no adjective acu \"\n   \"'swift': the family is represented only by the comparative ōcior / superlative ōcissimus (Pokorny: \"\n   \"'Positiv fehlt') and by the compound first member acu- in the archaic glossary word acupedius \"\n   \"'swift-footed' (Paulus-Festus) and in accipiter 'hawk, falcon'. For accipiter the majority view is \"\n   \"Nourai's: de Vaan reconstructs Proto-Italic *aku-petris 'having swift wings' from *h₂ōḱus + *peth₂- \"\n   \"'to fly' (whence the -piter), the geminate -cc- being due to contamination with accipere 'to take, \"\n   \"seize' — an ancient folk etymology that Webster still prints. Two caveats: Walde-Pokorny warns that \"\n   \"the ablaut grade *aku- 'swift' 'steht nicht fest' and that acupedius may be a calque on Gk. ὠκύπους; \"\n   \"and Klein and (recently) Le Feuvre take the first element from *h₂eḱ- 'sharp' (acuere, acus) instead, \"\n   \"which for Pokorny is the same root complex in another ablaut grade. Nourai's second reference, \"\n   \"POK:826, is Pokorny's pet- 'to fly' (pp.825-826), i.e. the -piter element, and is apt.\"),\n \"derivation_fa\": (\"ترکیب‌ها درست‌اند، اما «acu»ی تنها نادرست است. در لاتین صفتِ مستقل acu «تند» وجود ندارد؛ \"\n   \"این خانواده تنها با صفت برترِ ōcior و برترینِ ōcissimus نمایان می‌شود (پوکورنی: «صورت ساده نیست») و با \"\n   \"جزء نخستِ ترکیبی acu- در واژهٔ کهنِ acupedius «تیزپا» (پاولوس-فستوس) و در accipiter «باز، شاهین». برای \"\n   \"accipiter دیدگاه غالب همان است که نورایی آورده: دِ وان صورت ایتالیایی آغازین *aku-petris «دارای بالِ \"\n   \"تند» را از *h₂ōḱus + *peth₂- «پریدن» بازمی‌سازد و دوگانه‌شدن -cc- را نتیجهٔ آمیختگی با accipere «گرفتن» \"\n   \"می‌داند؛ همان ریشه‌شناسی عامیانهٔ کهنی که وبستر هنوز چاپ می‌کند. دو نکتهٔ احتیاط: والده-پوکورنی هشدار \"\n   \"می‌دهد که پایهٔ *aku- «تند» قطعی نیست و acupedius می‌تواند گرته‌برداری از ὠκύπους یونانی باشد؛ و کلاین \"\n   \"(و تازگی لو فُور) جزء نخست را از *h₂eḱ- «تیز» می‌گیرند که در نگاه پوکورنی همان مجموعهٔ ریشه در پایهٔ \"\n   \"آوایی دیگر است. ارجاع دوم نورایی (پوکورنی ۸۲۶) هم درست است: آن صفحه ریشهٔ pet- «پریدن» است.\"),\n \"sources\": [W_ACC],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. ōku- (AHD_watkins1985.txt leaf 796): \\\"ōku-. Swift. Zero-grade form *aku- in compound *oku-petro-, 'swift-flying,' in Latin accipiter, hawk\\\"; the appendix's English index (leaf 1208) lists 'ACCIPITER ōku-'.\"},\n   {\"ref\": \"POK:775,826\", \"status\": \"supports\",\n    \"note\": \"IEW p.775 (leaf 9): \\\"dann könnten lat. acu-pedius ,schnellfüßig' und accipiter ,Habicht, Falke' (oben S.19) auch hierher gehören\\\" — with 'vielleicht/könnten', and with the cross-reference to ak-/ok- 'sharp' (pp.18-19). p.826 is Pokorny's pet- 'fliegen', the source of -piter, as Nourai's '☞Pet 1' says.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I p.172 s.v. ōku-s\", \"stance\": \"partial\",\n    \"note\": \"\\\"Eine Ablautform *aku ,schnell' steht nicht fest. Lat. acupedius ,schnellfüßig' ist auch als Übersetzung von gr. ὠκύπους verständlich; lat. accipiter ... erweist aber auch dann nicht ein *aku-petris als Gdf., da auch ein *ōku-petris ... über *ōcipeter nach accipere zu accipiter werden konnte.\\\"\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. accipiter (LAT.txt lines 1098-1113)\", \"stance\": \"supports\",\n    \"note\": \"\\\"accipiter, -tris m.: oiseau de proie, épervier ... Si l'on fait abstraction de l'influence de accipio, le mot accipiter est parallèle à acupedius. De même que acu-pedius rappelle gr. ὠκύπους, accipiter rappelle gr. ὠκύπτερος, skr. āśu-patvan- 'qui vole (vite)'.\\\"\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. Accipiter (KLN_1971.txt line 5442)\", \"stance\": \"partial\",\n    \"note\": \"\\\"L. accipiter fr. orig. *acu-peter, 'swiftly-flying', but influenced in form through a confusion with accipere ... The first element lit. means 'sharp' (cp. acu-pedius, 'swift-footed', lit. 'sharp-footed', and acuere)\\\" — same compound, but referred to 'sharp' rather than 'swift'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. ōkus\", \"stance\": \"partial\",\n    \"note\": \"Mann lists 'Lat. cf. ocior, ocius' under ōkus 'sharp, keen, swift' but does not cite accipiter or acupedius there.\"}\n ]\n})\n\nn({\n \"id\": 9, \"lang\": \"English\", \"words\": \"accipiter\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"English accipiter is Latin accipiter taken over unchanged as a zoological term (and, \"\n   \"capitalised, as the Linnaean genus Accipiter of true hawks, 1760); in older medical English it also \"\n   \"meant a nose bandage 'so called from its resemblance to a hawk's claw'. The route is thus a learned \"\n   \"borrowing from written Latin, not a phonetic descent, which is exactly what the chart's #8→#9 arrow \"\n   \"means; the AHD lists ACCIPITER among the English derivatives of ōku-.\"),\n \"derivation_fa\": (\"«accipiter» در انگلیسی همان واژهٔ لاتینی است که بی‌تغییر به‌عنوان اصطلاح جانورشناسی \"\n   \"وام گرفته شده و با حرف بزرگ نام سردهٔ لینه‌ای بازها (Accipiter، ۱۷۶۰) است؛ در انگلیسیِ پزشکیِ کهن نیز \"\n   \"به نوعی بانداژ بینی می‌گفتند «از آن‌رو که به چنگال باز می‌ماند». پس این وام‌گیریِ کتابی از لاتین است، نه \"\n   \"تحول آوایی، و پیکان نمودار همین را می‌گوید. فرهنگ AHD نیز ACCIPITER را در شمار بازماندگان انگلیسیِ ریشهٔ \"\n   \"ōku- آورده است. ادعای نورایی درست است.\"),\n \"sources\": [W_ACC],\n \"ref_check\": [\n   {\"ref\": \"AHD:9\", \"status\": \"partial\",\n    \"note\": \"The page of the AHD New College Edition cannot be checked here (only the Watkins appendix is on disk), but the appendix's word index (AHD_watkins1985.txt leaf 1208) lists 'ACCIPITER ōku-' in exactly the alphabetical place (a-words) that p.9 of the dictionary would cover, so the citation is coherent.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. Accipiter (KLN_1971.txt line 5442)\", \"stance\": \"supports\",\n    \"note\": \"\\\"Accipiter, n., a genus of hawks and falcons (ornithol.) — L. accipiter fr. orig. *acu-peter, 'swiftly-flying'\\\", with derivatives accipitral, accipitrine.\"},\n   {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century s.v. accipiter (WEB_vol1.txt line 1631)\", \"stance\": \"partial\",\n    \"note\": \"\\\"ac-cip'i-ter, n. [L., a bird of prey, from accipere; ad, to, and capere, to seize] 1. in ornithology, any of an order of birds of prey, the Raptores. 2. a bandage for the nose...\\\" — the English word is there, but Webster keeps the old accipere etymology.\"},\n   {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls\", \"stance\": \"silent\",\n    \"note\": \"grep 'Accipiter' in FSD_vol1.txt found no hit (the OCR of the a-pages is poor).\"}\n ]\n})\n\nn({\n \"id\": 10, \"lang\": \"Greek\", \"words\": \"ôkys\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Gk. ὠκύς 'swift' is the direct Greek reflex of *h₂ōḱus: initial *h₂ō- gives Greek ὠ-, \"\n   \"*ḱ gives κ (Greek is a centum language, so no palatalisation), and the u-stem inflection is kept \"\n   \"(ὠκύς, ὠκεῖα, ὠκύ; superlative ὤκιστος = Av. āsišta-, Skt. āśiṣṭha-). It is Homeric and common in epic \"\n   \"compounds (ὠκύπους 'swift-footed', ὠκυπέτης / ὠκύπτερος 'swift-flying', of hawks). Nourai's reference \"\n   \"'FSD:1707?' with its own question mark is the Funk & Wagnalls page for 'ocean', not for ὠκύς itself.\"),\n \"derivation_fa\": (\"ὠκύς یونانی «تند» بازماندهٔ یکراستِ *h₂ōḱus است: *h₂ō- آغازین در یونانی ὠ- شده، *ḱ به \"\n   \"κ بدل شده (یونانی از زبان‌های centum است و همگونیِ کامی ندارد) و ستاک u-دار برجا مانده است (ὠκύς، برترین \"\n   \"ὤκιστος، همتای āsišta- اوستایی و āśiṣṭha- سنسکریت). این واژه هومری است و در ترکیب‌های حماسی بسیار \"\n   \"می‌آید: ὠκύπους «تیزپا»، ὠκυπέτης و ὠκύπτερος «تندپرواز» (صفت باز). ارجاع نورایی «FSD:1707؟» — که خودش \"\n   \"هم علامت پرسش گذاشته — در واقع صفحهٔ مدخل «ocean» است، نه مدخل ὠκύς. ادعای نورایی درست است.\"),\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"FSD:1707?\", \"status\": \"partial\",\n    \"note\": \"Funk & Wagnalls New Standard, p.1707 = FSD_vol3.txt leaf 241 (offset leaf = p − 1466): the page is the OCEAN page, whose etymology bracket reads '[OF., < L. oceanus, < Gr. ōkeanos, ocean, perhaps < ōkys, swift.]'. So the page does mention ōkys 'swift' — but inside the 'ocean' entry, and with 'perhaps'. Nourai's own '?' is well placed.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW p.775\", \"stance\": \"supports\", \"note\": \"\\\"gr. ὠκύς, ὤκιστος, poet. ὠκύτατος\\\" listed with Av. āsu- under ōkú-s.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. ōkus (IEC.txt line 12097)\", \"stance\": \"supports\",\n    \"note\": \"\\\"Myc. oku- (in names); Gk. okús 'swift, sharp' beside n-ōkar ('lethargy', w. neg. px)\\\" — with the Mycenaean evidence.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 14.21\", \"stance\": \"supports\", \"note\": \"'Grk. ταχύς, ὠκύς, θοός, αἰπύς' as the Greek words for 'swift'.\"}\n ]\n})\n\nn({\n \"id\": 11, \"lang\": \"Greek\", \"words\": \"ôkeanos\",\n \"verdict\": \"disputed\",\n \"derivation\": (\"Ὠκεανός, the world-encircling river of Homer, is not derivable from ὠκύς. The formation \"\n   \"would be unparalleled (no Greek noun in -εανός is built to a u-stem adjective), the sense 'swift' does \"\n   \"not fit the sluggish encircling stream, and every modern authority abandons the connection: Beekes \"\n   \"treats the word as a Pre-Greek substrate loan, reconstructing *ūkʲān-; Etymonline calls it 'of unknown \"\n   \"origin, perhaps Pre-Greek'; Klein, s.v. ocean, says the Greek word 'is of uncertain etymology'. Of the \"\n   \"Indo-European proposals the surviving one is not 'swift' but 'lying': Thieme's comparison with the \"\n   \"Vedic epithet of Vṛtra ā-śáyāna- 'lying on (the waters)', revived by Janda as *ō-ḱey-m̥no- to κεῖμαι \"\n   \"'lie' — which is precisely the analysis Nourai's NOTE attributes to Kent, and Kent p.164 really does \"\n   \"print it. So the chart's own NOTE is the better half of the entry, and the drawn arrow #10→#11 is the \"\n   \"part modern scholarship rejects. The double gloss 'swift, ocean' also conflates the adjective with the \"\n   \"proper name.\"),\n \"derivation_fa\": (\"Ὠκεανός، رودِ گرداگردِ جهان در هومر، از ὠκύς برنمی‌آید. چنین ساختی در یونانی همتا \"\n   \"ندارد (هیچ اسمی با پایانهٔ -εανός از صفتِ u-دار ساخته نمی‌شود)، معنی «تند» با آن جریانِ کندِ گردابنده \"\n   \"نمی‌خواند، و همهٔ مراجع امروزی این پیوند را رها کرده‌اند: بیکس واژه را وام‌واژه‌ای از زیرلایهٔ پیش‌یونانی \"\n   \"می‌داند و *ūkʲān- را بازمی‌سازد؛ اتیمانلاین آن را «با خاستگاه ناشناخته، شاید پیش‌یونانی» می‌خواند؛ و \"\n   \"کلاین زیر «ocean» می‌نویسد که واژهٔ یونانی «ریشه‌شناسی نامعلوم» دارد. از پیشنهادهای هندواروپایی، آنکه \"\n   \"زنده مانده «تند» نیست بلکه «خفته» است: سنجش تیمه با صفتِ وداییِ وریتره، ā-śáyāna- «خفته بر آب‌ها»، که \"\n   \"یاندا آن را به شکل *ō-ḱey-m̥no- (هم‌ریشه با κεῖμαι «دراز کشیدن») از نو زنده کرد — و این همان تحلیلی است \"\n   \"که یادداشتِ خودِ نورایی به کنت نسبت داده و در ص ۱۶۴ کنت به‌راستی چاپ شده است. پس یادداشتِ نمودار \"\n   \"درست‌تر از پیکانِ نمودار است و پژوهش امروزی پیکان #10→#11 را رد می‌کند.\"),\n \"sources\": [W_OKE, E_OCEAN],\n \"ref_check\": [\n   {\"ref\": \"FSD:1707\", \"status\": \"partial\",\n    \"note\": \"Funk & Wagnalls p.1707 (FSD_vol3.txt leaf 241) s.v. ocean: '[OF., < L. oceanus, < Gr. ōkeanos, ocean, perhaps < ōkys, swift.]' — the reference Nourai used does say it, but hedged with 'perhaps'; this 1913/1940 dictionary is the only source consulted that still offers the ōkys etymology.\"},\n   {\"ref\": \"TAD:5\", \"status\": \"partial\",\n    \"note\": \"Al-Unaysi, Tafsir al-alfaz al-dakhila: the أوقيانوس entry sits on the أو- page (TAD_pages.txt leaf 8, printed p.4-5), between أوقة and أوكاريستيا, and its line reads in the OCR 'داتع يوناني [Latin-script Greek word] معناه ... وعربيه اليحر [البحر] الم(ح)يط' — headword and Latin-script Greek lemma are mangled by the Arabic OCR, so the wording cannot be quoted verbatim; what is legible is that al-Unaysi labels it يوناني (Greek) and equates it with البحر المحيط. No page image of TAD is available locally (text-only reference).\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. ocean (KLN_1971.txt line 165257)\", \"stance\": \"contradicts\",\n    \"note\": \"\\\"ocean, n. — F. océan, fr. L. oceanus, fr. Gk. ὠκεανός, 'the great river encompassing the whole earth'; hence 'the great Outward Sea' ... which is of uncertain etymology.\\\"\"},\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon p.164 s.v. ā (KNT.txt line 4912; the leaf carries the printed '164' immediately before 'PART III. LEXICON')\", \"stance\": \"supports\",\n    \"note\": \"The chart NOTE checks out to the letter: \\\"ā adv. as prefix and prep. 'to' ... pIE *ā if = Lt. ā 'from' (Sturtevant), or *ō if = Gk. ō- in ō-keanós '(lying round about), ocean'.\\\" — i.e. Kent, on exactly p.164, analyses the word as ō- + a 'lying' element.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Ocean (SKT.txt line 12603)\", \"stance\": \"silent\",\n    \"note\": \"\\\"Ocean. (F.-L.-Gk.) O.F. ocean, L. oceanum, acc. of oceanus, Gk. ὠκεανός, the great stream supposed to encompass the earth\\\" — Skeat gives the chain but no origin for the Greek word.\"},\n   {\"src\": \"FSD\", \"where\": \"vol.3 p.1707\", \"stance\": \"partial\", \"note\": \"see ref_check: 'perhaps < ōkys, swift'.\"}\n ]\n})\n\nn({\n \"id\": 12, \"lang\": \"Arabic\", \"words\": \"oqyânŭs\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Arabic أُوقْيَانُوس ūqyānūs 'the encircling ocean' is a learned borrowing of Gk. Ὠκεανός, \"\n   \"taken over in the Graeco-Arabic translation movement (Ptolemy's and Aristotle's geography, 3rd c. AH) \"\n   \"together with the calque al-baḥr al-muḥīṭ 'the encompassing sea', which is what actually stayed in use; \"\n   \"Wiktionary marks the transcription as archaic. Greek ōkeanós is rendered with prosthetic ʾū- for the \"\n   \"initial long ō (Arabic has no ō), -qy- for -κε-, and the Greek -ος ending kept as -ūs, as in \"\n   \"أرسطوطاليس, قاموس (< κάμος?), أطلس. Nourai's 'oqyânŭs' spelling reflects the variant أقيانوس without \"\n   \"the prosthetic alif-wāw, which is the form that reached Persian.\"),\n \"derivation_fa\": (\"عربی «أوقْيانوس» وام‌واژهٔ کتابیِ Ὠκεανός یونانی است که در جنبش ترجمهٔ یونانی به عربی \"\n   \"(جغرافیای بطلمیوس و ارسطو، سدهٔ سوم هجری) به عربی راه یافت، همراه با گرته‌برداریِ «البحر المحیط» که \"\n   \"همان در کاربرد ماند؛ ویکی‌واژه صورتِ آوانگاشته را کهن‌گرا می‌شمارد. در وام‌گیری، ō کشیدهٔ آغازین با أو- \"\n   \"نمایانده شده (عربی واکهٔ ō ندارد)، -κε- به -قی- بدل شده و پایانهٔ یونانیِ -ος به -وس مانده است، همچون \"\n   \"أرسطوطالیس و أطلس. صورتِ «اقیانوس» که نورایی آورده همان گونهٔ بی‌الفِ آغازی است و همین گونه به فارسی \"\n   \"رسیده است. ادعای نورایی درست است.\"),\n \"sources\": [W_UQY],\n \"ref_check\": [\n   {\"ref\": \"TAD:5\", \"status\": \"partial\",\n    \"note\": \"See node #11: the entry is present in al-Unaysi on the أو- page (leaf 8 of TAD_pages.txt, printed p.4-5) in its alphabetical slot between أوقة and أوكاريستيا, marked يوناني and glossed with البحر المحيط, but the Arabic OCR of the headword and of the Latin-script Greek lemma is unusable for a verbatim quote.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. ocean / Oceanus\", \"stance\": \"silent\",\n    \"note\": \"Klein traces the European word only (F. > L. > Gk.); he does not mention the Arabic borrowing.\"},\n   {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur'an\", \"stance\": \"silent\",\n    \"note\": \"grep 'قيانوس'/'اوقيانوس' in FVQ_pages.txt: nothing — the word is not Qur'anic, as expected for a 3rd-c. AH translation loan.\"},\n   {\"src\": \"MON\", \"where\": \"Mo'in s.v. اقیانوس (MON_part1.txt line 15624)\", \"stance\": \"supports\",\n    \"note\": \"'اقیانوس: [- اوقیانوس، معر.] (اِ.) دریای بسیار بزرگ' — Mo'in marks the Persian word معرّب (Arabicised) and gives اوقیانوس as its base form, i.e. the Arabic stage of the chain.\"}\n ]\n})\n\nn({\n \"id\": 13, \"lang\": \"Persian\", \"words\": \"oqyânŭs «اقیانوس»\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"NP اقیانوس oqyānūs 'ocean' is the Arabic أوقيانوس re-borrowed into Persian — a Greek word \"\n   \"that reached Persian through Arabic geographical literature, not directly from Greek. Mo'in's Farhang \"\n   \"marks it exactly so: 'اقیانوس [- اوقیانوس، معر.]', i.e. an Arabicised form whose base is اوقیانوس. In \"\n   \"Persian the prosthetic أو- was simplified to ا- and the word became the ordinary modern term (اقیانوس \"\n   \"کبیر, اقیانوس اطلس, اقیانوس منجمد شمالی), displacing the older دریای محیط.\"),\n \"derivation_fa\": (\"«اقیانوس» فارسی همان «أوقيانوس» عربی است، یعنی واژه‌ای یونانی که از راه متون جغرافیایی \"\n   \"عربی به فارسی رسیده، نه یکراست از یونانی. فرهنگ معین همین را می‌گوید: «اقیانوس [- اوقیانوس، معر.]»، \"\n   \"یعنی معرّبی که صورت پایهٔ آن اوقیانوس است. در فارسی، أو- آغازین به ا- ساده شده و واژه اصطلاح رایج امروز \"\n   \"شده است (اقیانوس کبیر، اقیانوس اطلس، اقیانوس منجمد شمالی) و جای «دریای محیط» کهن را گرفته است. ادعای \"\n   \"نورایی درست است.\"),\n \"sources\": [W_UQY],\n \"ref_check\": [\n   {\"ref\": \"MON:327\", \"status\": \"supports\",\n    \"note\": \"Mo'in, Farhang-e Farsi s.v. اقیانوس (MON_part1.txt lines 15624-15628): 'اقیانوس: [- اوقیانوس، معر.] (اِ.) دریای بسیار بزرگ. در کرهٔ زمین پنج اقیانوس وجود دارد: اقیانوس کبیر، اقیانوس اطلس، اقیانوس هند، اقیانوس منجمد شمالی، اقیانوس منجمد جنوبی.' The 'معر.' tag is exactly Nourai's Arabic→Persian arrow. The printed page number is not verifiable in this OCR (no page markers).\"}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate'\", \"stance\": \"silent\",\n    \"note\": \"grep 'قیانوس' in BQT_v1/v2 and incoming/BQT v3-v5 pages files: no entry — a modern learned word absent from the 17th-c. dictionary.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-ha\", \"stance\": \"silent\",\n    \"note\": \"no headword اقیانوس in ARY_pages.txt (the book covers native Iranian vocabulary).\"}\n ]\n})\n\nn({\n \"id\": 14, \"lang\": \"Latin\", \"words\": \"ôceanus\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Latin ōceanus is the standard Latin transcription of Gk. Ὠκεανός, borrowed with the \"\n   \"Greek long ō (written O, scanned long) and the -us of the second declension for Greek -ος; it is \"\n   \"attested from Cicero and Caesar on, both as the proper name Ōceanus and as the common noun 'the \"\n   \"outer sea'. This is an unproblematic learned Latin Graecism and the sole route by which the word \"\n   \"entered the Romance and Germanic languages.\"),\n \"derivation_fa\": (\"ōceanus لاتینی آوانگاشتِ معیارِ Ὠκεανός یونانی است: ō کشیدهٔ یونانی نگه داشته شده و \"\n   \"پایانهٔ یونانیِ -ος به -us صرفِ دومِ لاتین بدل شده است. این واژه از سیسرو و سزار به بعد گواهی دارد، هم \"\n   \"به‌عنوان نام خاص Ōceanus و هم اسم عام «دریای بیرونی». وام‌گیری‌ای کتابی و بی‌مسئله است و همین راه، تنها \"\n   \"راهِ ورودِ واژه به زبان‌های رومی و ژرمنی بوده است. ادعای نورایی درست است.\"),\n \"sources\": [E_OCEAN],\n \"ref_check\": [\n   {\"ref\": \"AHD:909\", \"status\": \"not_checked\",\n    \"note\": \"Only the Watkins Indo-European appendix of the AHD is on disk, not the A-Z pages, so p.909 (which in the New College Edition falls in the o- range and would carry 'ocean') cannot be inspected. Note that the appendix does NOT list ocean/Oceanus under any root, consistent with the modern view that the Greek word is not Indo-European.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. ocean and Oceanus (KLN_1971.txt lines 165257, 165279)\", \"stance\": \"supports\",\n    \"note\": \"\\\"Oceanus, n. ... — L., fr. Gk. Ὠκεανός, personification of ὠκεανός, 'the great river encompassing the whole earth'.\\\"\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Ocean (SKT.txt line 12603)\", \"stance\": \"supports\",\n    \"note\": \"\\\"O.F. ocean, L. oceanum, acc. of oceanus, Gk. ὠκεανός.\\\"\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet\", \"stance\": \"silent\",\n    \"note\": \"grep 'oceanus' in LAT.txt gives no etymological entry: Ernout-Meillet do not treat transparent Greek borrowings.\"}\n ]\n})\n\nn({\n \"id\": 15, \"lang\": \"English\", \"words\": \"ocean\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"English ocean is Middle English occean, borrowed c. 1300 from Old French occean (Modern \"\n   \"French océan) < Latin oceanus < Gk. Ὠκεανός; the French stress pattern gave ME occean /oˈsɛːan/, later \"\n   \"reduced to /ˈoʊʃən/ with the regular assibilation of -ci- before a vowel. First applied to the outer \"\n   \"encircling sea, then from the 16th c. to the great divisions of the world's waters. The chain \"\n   \"Greek > Latin > Old French > English is uncontroversial.\"),\n \"derivation_fa\": (\"«ocean» انگلیسی از انگلیسی میانهٔ occean است که نزدیک ۱۳۰۰ م از فرانسهٔ کهن occean \"\n   \"(فرانسهٔ امروز océan) وام گرفته شده، و آن از oceanus لاتینی و آن از Ὠκεανός یونانی. تکیهٔ فرانسوی \"\n   \"occean انگلیسی میانه را ساخت و سپس -ci- پیش از واکه به /ʃ/ بدل شد و تلفظ امروزی /ˈoʊʃən/ پدید آمد. \"\n   \"نخست به دریای گرداگردِ جهان می‌گفتند و از سدهٔ شانزدهم به بخش‌های بزرگ آب‌های زمین. زنجیرهٔ یونانی > \"\n   \"لاتین > فرانسهٔ کهن > انگلیسی بی‌چون‌وچرا است.\"),\n \"sources\": [E_OCEAN],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"partial\",\n    \"note\": \"The Watkins appendix (the only AHD volume on disk) has no entry for OCEAN under any root, as expected for a word whose Greek source is not Indo-European; the A-Z pages are not available.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. ocean\", \"stance\": \"supports\", \"note\": \"\\\"ocean, n. — F. océan, fr. L. oceanus, fr. Gk. ὠκεανός.\\\"\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Ocean\", \"stance\": \"supports\", \"note\": \"\\\"Ocean. (F.-L.-Gk.) O.F. ocean, L. oceanum, acc. of oceanus, Gk. ὠκεανός, the great stream supposed to encompass the earth.\\\"\"},\n   {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls vol.3 p.1707\", \"stance\": \"supports\",\n    \"note\": \"\\\"[OF., < L. oceanus, < Gr. ōkeanos, ocean, perhaps < ōkys, swift.]\\\" — the OF > L > Gk chain for the English word.\"}\n ]\n})\n\nfor nd in e0[\"nodes\"]:\n    nd.pop(\"derivation_note\", None)\n\n# ---------------- entry 1 ----------------\ne1 = {\n \"entry\": 1,\n \"root\": \"Okw\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *h₃ekʷ- / *h₃okʷ- 'to see', with the noun *h₃ekʷ-/*h₃okʷ- 'eye' (Pokorny's ok̑ʷ-)\",\n \"note\": (\"Root, language label, gloss and reference are all correct. Pokorny pp.775-777 has ok̑ʷ- 'sehen' \"\n   \"with the stem set ok̑ʷ-, ok̑ʷi-, ok̑ʷ(e)n-, ok̑ʷ(e)s-, ok̑ʷ-p- 'Auge', and Watkins's appendix has okʷ- \"\n   \"'to see'; both are the immediate sources of Nourai's box. In post-laryngeal notation the root is \"\n   \"*h₃ekʷ-, the initial *h₃- being what colours the vowel to o (Gk. ὄσσε, Lat. oculus). Nourai's 'Okw' \"\n   \"sits on the same Pokorny page (775) as the previous entry's 'Ôku' — a coincidence of alphabetisation, \"\n   \"not a relationship: Pokorny explicitly cross-refers 'daneben ok-, s. dort'. All four branches of the \"\n   \"chart check out; the only soft spot is the Persian branch (#2-#3), where the connection of nišān to \"\n   \"the 'see' root is the received Iranist opinion (Nyberg, Mo'in) but is not underpinned by a laryngeal-\"\n   \"era reconstruction.\"),\n \"note_fa\": (\"جعبهٔ ریشه، برچسب زبانی، معنا و ارجاع همه درست است. پوکورنی در ص ۷۷۵-۷۷۷ ریشهٔ ok̑ʷ- «دیدن» \"\n   \"را با مجموعهٔ ستاک‌های ok̑ʷ-, ok̑ʷi-, ok̑ʷ(e)n-, ok̑ʷ(e)s-, ok̑ʷ-p- «چشم» آورده و واتکینز نیز در پیوستِ \"\n   \"AHD ریشهٔ okʷ- «دیدن» را دارد؛ هر دو سرچشمهٔ بی‌واسطهٔ جعبهٔ نورایی‌اند. در نگارش امروزی این ریشه \"\n   \"*h₃ekʷ- است و همان *h₃- آغازین است که واکه را o می‌کند (ὄσσε یونانی، oculus لاتینی). این «Okw» با \"\n   \"«Ôku»ی مدخل پیشین در یک صفحهٔ پوکورنی (۷۷۵) نشسته است، اما این تنها همسایگیِ الفبایی است نه خویشاوندی؛ \"\n   \"پوکورنی خود می‌نویسد «daneben ok-, s. dort». هر چهار شاخهٔ نمودار درست‌اند؛ تنها جای نرمِ کار شاخهٔ فارسی \"\n   \"(گره‌های ۲ و ۳) است، که پیوند «نشان» با ریشهٔ «دیدن» رأی پذیرفتهٔ ایران‌شناسان (نیبرگ، معین) است ولی \"\n   \"بازسازی حلقی‌شناسانهٔ روشنی پشتِ آن نیست.\"),\n \"sources\": [W_NESAN],\n \"ref_check\": [\n   {\"ref\": \"POK:775\", \"status\": \"supports\", \"note\": POK775_OKW}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I pp.169ff. s.v. ok̑ʷ- (incoming/WLD/WLD_Bd1_pages.txt lines 15722-15727)\", \"stance\": \"supports\",\n    \"note\": \"The Walde-Pokorny entry behind IEW 775: \\\"... poln. obaczyć 'sehen, bemerken' ... vom n-St. abg. okno 'Fenster' (vgl. engl. wind-ow ds., eig. 'Windauge')\\\".\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. okʷ- (AHD_watkins1985.txt leaves 796-798)\", \"stance\": \"supports\",\n    \"note\": \"\\\"okʷ-. To see. 1. Germanic *augōn- (with taboo deformation) in: a. Old English ēage, eye: EYE; DAISY; b. Old Norse auga, eye: WALLEYED, WINDOW ... 4. Suffixed form *okʷ-ti- in Greek opsis, sight, appearance: ... AUTOPSY, SYNOPSIS. 5. Suffixed form *ok-to- in Greek optos, seen, visible: OPTIC ... [Pok. okʷ- 775.]\\\"\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 4.21 EYE (SYN.txt line 5875)\", \"stance\": \"supports\",\n    \"note\": \"\\\"Goth. augo, ON auga, OE ēage, NE eye, ChSl. oko, Skt. akṣi, Av. aši ... Most of the words for 'eye' belong to an inherited group\\\" — Buck's inherited group is exactly this root.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann\", \"stance\": \"silent\",\n    \"note\": \"grep 'okʷ', 'okwos' in IEC.txt returns nothing usable (Mann's lemma for 'eye' is spelt with a digraph the OCR destroyed).\"}\n ],\n \"nodes\": []\n}\n\nm = e1[\"nodes\"].append\n\nm({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"aši, axši; aiwi-axši\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Avestan aši 'the two eyes' is the nominative-accusative dual of the consonant stem aš- \"\n   \"'eye' (< *h₃ekʷ-, Skt. dual akṣī); Pokorny explains the shape as analogical — 'av. aši für *axšī nach \"\n   \"uši (Ohren)', i.e. the expected *axšī (Nourai's second form) was remodelled on uši 'the two ears'. So \"\n   \"aši is attested and axši is the reconstructed pre-form, not a second attested word. aiwi-axš- 'to keep \"\n   \"watch over' is the same root with the preverb aiwi 'around, over' (Nourai's '☞Ambhi' = PIE *h₂mbhi): \"\n   \"attested as aiwyāxšayeinti 'they supervise', the infinitive aiwyāxštrāi 'to supervise' and the agent \"\n   \"noun aiwyāxštar- 'overseer'. The semantic step 'have one's eyes on' > 'supervise' is transparent and \"\n   \"the same as Lat. animadvertere or Gk. epi-skopein.\"),\n \"derivation_fa\": (\"aši اوستایی «دو چشم» صورت فاعلی-مفعولیِ دوگانِ ستاکِ همخوانیِ aš- «چشم» است (از \"\n   \"*h₃ekʷ-، همتای دوگانِ akṣī سنسکریت)؛ پوکورنی شکلِ آن را قیاسی می‌داند: «aši اوستایی به‌جای *axšī، به \"\n   \"قیاسِ uši (دو گوش)». یعنی aši گواهی‌شده است و axši (صورت دومِ نورایی) پیش‌صورتِ بازسازی‌شده است، نه \"\n   \"واژه‌ای جداگانه. aiwi-axš- «نظارت کردن» همان ریشه با پیشوندِ aiwi «پیرامون، بر» است (اشارهٔ نورایی به \"\n   \"«Ambhi» یعنی *h₂mbhi هندواروپایی) و در صورت‌های aiwyāxšayeinti «نظارت می‌کنند»، مصدرِ aiwyāxštrāi و \"\n   \"اسم فاعلِ aiwyāxštar- «سرپرست» گواهی دارد. تحول معنایی «چشم داشتن بر» به «نظارت کردن» شفاف است. ادعای \"\n   \"نورایی درست است.\"),\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"POK:775\", \"status\": \"supports\",\n    \"note\": \"IEW p.775 (POK_03.txt leaf 10): \\\"Nom. Du. akṣī = av. aši 'die (beiden) Augen' ... av. aši für *axšī nach uši 'Ohren', vgl. av. aiwy-āxšayeinti 'sie beaufsichtigen', aiwyāxštar- 'Aufseher'\\\" — all three of Nourai's forms, and the explanation of axši as the pre-form.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"AiW s.v. aš- (col. ~331, BRT.txt leaf 158) and aiwy-āxštar-/aiwyāxšaya- (cols. ~97-98, leaf 89)\", \"stance\": \"supports\",\n    \"note\": \"\\\"j.) g. aš- n. 'Auge' ... nur Du.\\\" with the dual aši; and \\\"j. aiwy-āxštar- m. 'der die Aufsicht hat, führt über—, Beaufsichtiger'\\\", \\\"j. aiwy-āxštrāi Inf. 'die Aufsicht zu führen über—, zu beaufsichtigen'\\\", plus 'aiwyāxšayāt' glossed \\\"'die Aufsicht führen'\\\" (leaf 200).\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. okʷ-\", \"stance\": \"partial\",\n    \"note\": \"The appendix gives the Greek, Latin, Germanic, Baltic and Sanskrit reflexes but no Avestan; it does not contradict the node, it simply omits Iranian.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 4.21\", \"stance\": \"supports\", \"note\": \"Buck's 'eye' row lists 'Av. čašman-, dōiθra-, aši' — aši among the Avestan words for eye.\"}\n ]\n})\n\nm({\n \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"ni-aš, niš\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"MP niš- 'to see, observe' (Book Pahlavi nyš-, Manichaean nyyš-ydn) is Old Iranian *ni- + \"\n   \"*axš- 'to look', i.e. the same preverb-plus-root compound as Av. aiwi-axš- but with ni- 'down, at' \"\n   \"instead of aiwi-; Nourai's two entries 'ni-aš' and 'niš' are the morphological analysis and the actual \"\n   \"Middle Persian shape (*ni-axš- > niš- by loss of the unstressed vowel and simplification of -xš- to \"\n   \"-š-). MacKenzie lists the present stem, Nyberg lists it with its etymological cross-reference to \"\n   \"nišān, and it survives in the compound murw-niš 'bird-watcher, augur' of the Pahlavi books.\"),\n \"derivation_fa\": (\"ستاکِ niš- «دیدن، نگریستن» در فارسی میانه (به خط پهلوی nyš-، در مانوی nyyš-ydn) از \"\n   \"ایرانی باستان *ni- + *axš- «نگریستن» است، یعنی همان ترکیبِ پیشوند و ریشه‌ای که در aiwi-axš- اوستایی \"\n   \"دیدیم، اما با پیشوندِ ni- «فرو، بر» به‌جای aiwi-. دو صورتی که نورایی آورده (ni-aš و niš) در واقع \"\n   \"تجزیهٔ ساختواژی و صورتِ واقعیِ فارسی میانه‌اند: *ni-axš- با افتادنِ واکهٔ بی‌تکیه و ساده‌شدنِ خوشهٔ -xš- \"\n   \"به -š- به niš- رسیده است. مکنزی این ستاک را ثبت کرده، نیبرگ آن را با ارجاعِ ریشه‌شناختی به «نشان» \"\n   \"آورده، و در ترکیبِ پهلویِ murw-niš «مرغ‌بین، فالگیرِ پرندگان» زنده است.\"),\n \"sources\": [W_NESAN],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"Nourai gives no reference for this node (refs=None in the source JSON), so there is nothing of his to check; verified against MacKenzie and Nyberg instead (see consulted).\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p.59 s.v. niš- (PHD.txt leaf 514 / PHD_mackenzie.txt)\", \"stance\": \"supports\",\n    \"note\": \"\\\"niš- [nyš- | M nyyš-ydn, J ~] see, observe.\\\" — the Middle Persian verb of the node, exactly as drawn.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, Glossary s.v. murw-niš (NYB_vol2_glossary.txt line 2598)\", \"stance\": \"supports\",\n    \"note\": \"\\\"murw-niš [mwlwnyš] soothsayer foretelling the future by the flight or other tokens of the birds, an augur ... — murw + niš, the pres. st. of MPrs nyyšydn, nyyš- 'to see' (A-H I, Verbum 168); cf nišān.\\\" — Nyberg himself makes the #2→#3 link.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung, Etymological Dictionary of the Iranian Verb\", \"stance\": \"silent\",\n    \"note\": \"grep '*axš', 'niš-' in CHEUNG.txt returns only unrelated *niš- 'to drive out' compounds; Cheung has no lemma for this verb.\"}\n ]\n})\n\nm({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"nešân «نشان»\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"NP نشان nešān 'mark, sign, target, decoration' is MP nišān (nyšʾn') taken over unchanged; \"\n   \"it is a nominal derivative of the verb niš- 'to see, observe' of node #2, so literally 'what is looked \"\n   \"at' > 'target, mark' > 'sign, token' > (19th c.) 'decoration, medal'. Mo'in's footnote in Borhan-e \"\n   \"Qate' p.2143 sets out exactly this: Pahlavi nišān (in the compound murw-nišān 'bird-watcher'), \"\n   \"Manichaean Turfan nyšʾn, Judaeo-Persian nyšʾn, dialectal nigāh kardan 'to look', Armenian nšan (a loan \"\n   \"from Iranian), and then 'قس: اوستایی aiwi-axš- نظارت کردن، بارتولمه ۳۹۰' — compare Avestan aiwi-axš- \"\n   \"'to supervise'. The word was re-exported from Persian to Arabic (نيشان), Armenian, Ottoman Turkish \"\n   \"(nişan), Syriac and the Caucasus. Note that Persian نشاندن/نشستن 'to set, sit' is a different word \"\n   \"(*ni-had-/*ni-šad-) with which نشان is often confused by folk etymology.\"),\n \"derivation_fa\": (\"«نشان» فارسی نو همان nišān فارسی میانه (nyšʾn') است که بی‌تغییر برجا مانده؛ اسمی است \"\n   \"برساخته از ستاکِ niš- «دیدن» (گرهٔ ۲)، پس تحت‌اللفظ «آنچه بدان می‌نگرند» > «هدف، علامت» > «نشانه» > \"\n   \"(از سدهٔ سیزدهم/نوزدهم) «مدال». حاشیهٔ معین بر برهان قاطع (ص ۲۱۴۳) همین را می‌آورد: پهلوی nišān (در \"\n   \"ترکیبِ murw-nišān «نگهبان مرغان»)، اوراقِ مانویِ تورفان nyšʾn، یهودی-فارسی nyšʾn، در گویش‌ها nigāh کردن، \"\n   \"ارمنی nšan (وام از ایرانی)، و آنگاه «قس: اوستایی aiwi-axš- نظارت کردن، بارتولمه ۳۹۰». این واژه از \"\n   \"فارسی به عربی (نيشان)، ارمنی، ترکی عثمانی (nişan)، سریانی و قفقاز صادر شده است. توجه شود که «نشاندن/\"\n   \"نشستن» واژهٔ دیگری است (*ni-šad-) و ریشه‌شناسی عامیانه گاه این دو را به هم می‌آمیزد. ادعای نورایی درست \"\n   \"است.\"),\n \"sources\": [W_NESAN],\n \"ref_check\": [\n   {\"ref\": \"BQT:2143\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qate', printed p.2143 = vol.4 pdf page 226 (fetched with tools/ref_page.py BQT:2143 --image; cached at data/verification/sources/refs/ocr/BQT/2143.png/.txt). The headword is 'نشان: بکسر اول بر وزن نهان، بمعنی علامت باشد - و حصه و نصیب را نیز گویند'; its footnote 6 reads (Latin-script forms mangled by the Persian OCR but the Persian legible): 'پهلوی nišān «در کلمهٔ مرکب nišān-murw (نگهبان مرغان)» ... در اوراق مانوی تورفان nyšʾn ... یهودی-فارسی nyšʾn، و در لهجه‌ها nigāh (نگاه کردن)؛ ایرانی میانه ...، فارسی نشان، ارمنی nšan ... (علامت، نشان). قس: اوستایی aiwi-axš- نظارت کردن «بارتولمه ۳۹۰»، «نیبرگ ص ۱۶۷»، کردی nīšān ... معرب آن «دزی ج۲ ص۹۷۶» و نیشان.' — Mo'in's 'قس اوستایی aiwi-axš-' is precisely Nourai's chain root→#1→#2→#3. (Mo'in's column number 390 does not match Bartholomae, whose aiwy-āxštar- stands at cols. 97-98 and aš- 'Auge' at col. ~331.)\"}\n ],\n \"consulted\": [\n   {\"src\": \"NYB\", \"where\": \"Nyberg II Glossary s.v. nīšān and murw-niš (NYB_vol2_glossary.txt lines 2761, 2598)\", \"stance\": \"supports\",\n    \"note\": \"\\\"nīšān [nyš'n'] sign, omen, portent 487, gl. by daxšak + anak ... — MPrthPrs nyšʾn; NP nišān\\\", and under murw-niš the explicit 'cf nišān' after identifying niš- as the present stem of 'to see'.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. nišān (PHD.txt leaf 514; errata p.128 'for nīšān read nišān')\", \"stance\": \"supports\",\n    \"note\": \"\\\"nišān [nyšʾn | = M, N nišān] sign, mark, banner\\\" — MP form and meanings identical with the Persian word; MacKenzie lists it immediately after niš- 'see, observe'.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss der neupersischen Etymologie\", \"stance\": \"silent\",\n    \"note\": \"grep 'nišān', 'nisan', \\\"'Zeichen\\\" in HRN.txt: no entry; Horn does not number this word.\"},\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien\", \"stance\": \"silent\",\n    \"note\": \"grep 'nišān'/'nisan' in HUB.txt: nothing.\"}\n ]\n})\n\nm({\n \"id\": 4, \"lang\": \"Germanic\", \"words\": \"augôn; vind-auga\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Proto-Germanic *augōn- 'eye' (Goth. augō, ON auga, OHG ouga, OE ēage) does come from \"\n   \"this root, but not by a straight sound law: *h₃ekʷ- should have given Gmc *ahw-/*auhw-, and the \"\n   \"attested *aug- is explained by Watkins and others as a 'taboo deformation', more concretely as \"\n   \"contamination with *ausan- 'ear' (Pokorny: 'durch Ausgleich und Einfluß von *ausō \\\"Ohr\\\" entstand ein \"\n   \"St. *auǥan-') — the same pairing of eye and ear that produced Av. aši for *axšī in node #1. ON \"\n   \"vindauga 'wind-eye' is a transparent compound of vindr 'wind' (Nourai's '☞Wě 1' = PIE *h₂weh₁-) and \"\n   \"auga 'eye', the Norse name for the smoke-hole/opening in a roof.\"),\n \"derivation_fa\": (\"ژرمنی آغازین *augōn- «چشم» (گوتی augō، نورس کهن auga، آلمانی علیای کهن ouga، انگلیسی \"\n   \"کهن ēage) به‌راستی از همین ریشه است، اما نه با قانون آوایی مستقیم: *h₃ekʷ- در ژرمنی می‌بایست *ahw-/\"\n   \"*auhw- می‌داد و صورتِ گواهی‌شدهٔ *aug- را واتکینز «دگرشکلیِ تابویی» و پوکورنی روشن‌تر آمیختگی با \"\n   \"*ausō «گوش» می‌داند («durch Ausgleich und Einfluß von *ausō \\\"Ohr\\\" entstand ein St. *auǥan-») — همان \"\n   \"جفت‌شدنِ چشم و گوش که در گرهٔ ۱ صورتِ aši را به‌جای *axšī ساخت. vindauga نورس کهن «چشمِ باد» ترکیبِ \"\n   \"شفافِ vindr «باد» (اشارهٔ نورایی به «Wě 1»، یعنی *h₂weh₁-) و auga «چشم» است و نامِ روزنِ دودِ سقف بوده \"\n   \"است. ادعای نورایی درست است.\"),\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD:1467\", \"status\": \"partial\",\n    \"note\": \"The AHD A-Z pages are not on disk (only the Watkins appendix), so p.1467 cannot be inspected; but the appendix entry okʷ- says exactly what the node claims: \\\"Germanic *augōn- (with taboo deformation) in: a. Old English ēage, eye: EYE ... b. Old Norse auga, eye: WALLEYED, WINDOW\\\" (AHD_watkins1985.txt leaf 796).\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW p.777 (POK_03.txt leaf 11)\", \"stance\": \"supports\",\n    \"note\": \"\\\"daneben germ. *awn- (*okʷ-en-); durch Ausgleich und Einfluß von *ausō 'Ohr' entstand ein St. *auǥan-: krimgot. Pl. oeghene, dann got. augō, aisl. auga, ahd. ouga, ags. ēage n. 'Auge'\\\" — the mechanism behind the irregular *aug-.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I s.v. ok̑ʷ- (WLD_Bd1_pages.txt line 15722-15727)\", \"stance\": \"supports\",\n    \"note\": \"\\\"vom n-St. abg. okno 'Fenster' (vgl. engl. wind-ow ds., eig. 'Windauge')\\\" — the 'wind-eye' semantics of the compound, with the Slavic parallel okno.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. eye and window (KLN_1971.txt lines 89410, 267446)\", \"stance\": \"supports\",\n    \"note\": \"\\\"eye ... OE ēage, rel. to OS āga, ON auga, ... Goth. augo, 'eye', fr. I.-E. base *oqʷ-, 'to see; eye'\\\"; \\\"window, n. — ME. windoge, windowe, fr. ON. vindauga, lit. 'windeye'.\\\"\"}\n ]\n})\n\nm({\n \"id\": 5, \"lang\": \"English\", \"words\": \"eye; window\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"OE ēage (< Gmc *augōn-) > ME eige/eye/eie > NE eye, with the regular Middle English loss \"\n   \"of the intervocalic velar fricative and monophthongisation. Window is not a native formation but an \"\n   \"Old Norse loan of the Danelaw period: ON vindauga was borrowed as ME windoge/windowe (13th c.), \"\n   \"replacing native OE ēagþyrel 'eye-hole' and ēagduru 'eye-door'; the second element is therefore the \"\n   \"same auga 'eye' as in node #4, so 'window' and 'eye' are ultimately the same word twice over. Both are \"\n   \"listed under okʷ- in the AHD appendix.\"),\n \"derivation_fa\": (\"انگلیسی کهن ēage (از ژرمنی *augōn-) در انگلیسی میانه eige/eye/eie و در انگلیسی نو \"\n   \"eye شده است، با افتادنِ سایشیِ نرم‌کامیِ میان‌واکه‌ای و یک‌واکه‌شدنِ قاعده‌مندِ انگلیسی میانه. اما «window» \"\n   \"ساختِ بومی نیست؛ وام‌واژه‌ای نورسی از دورهٔ دِین‌لا است: vindauga نورس کهن در سدهٔ سیزدهم به شکلِ \"\n   \"windoge/windowe وام گرفته شد و جایِ ēagþyrel «چشم‌روزن» و ēagduru «چشم‌درِ» بومی را گرفت؛ جزء دومش همان \"\n   \"auga «چشم» گرهٔ ۴ است، پس «window» و «eye» در نهایت دو بارِ یک واژه‌اند. پیوستِ AHD هر دو را زیر okʷ- \"\n   \"آورده است. ادعای نورایی درست است.\"),\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"Nourai gives no reference for this node (refs=None); checked against Klein, Skeat and the Watkins appendix instead.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. eye, window (KLN_1971.txt lines 89410, 267446)\", \"stance\": \"supports\",\n    \"note\": \"\\\"eye, n. — ME. eige, eye, eie, fr. OE. ēage ... fr. I.-E. base *oqʷ-, 'to see; eye'\\\"; \\\"window, n. — ME. windoge, windowe, fr. ON. vindauga, lit. 'windeye'. See wind, 'air in motion', and eye.\\\"\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Eye (SKT.txt line 6174)\", \"stance\": \"supports\",\n    \"note\": \"\\\"Eye. (E.) ME. eye, eighe, pl. eyen (whence eyne), A.S. ēage, pl. ēagan. + Du. oog, Icel. auga, Dan. øje, Swed. öga, Goth. augo, G. auge, Russ. oko, L. oculus (dimin. of *ocus); Gk. ὄσσε; Skt. aksha. Der. dais-y; wind-ow.\\\" — Skeat derives both words of the node together.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. okʷ-\", \"stance\": \"supports\",\n    \"note\": \"EYE and WINDOW are both listed as English outcomes of okʷ- (the latter through Old Norse auga).\"}\n ]\n})\n\nm({\n \"id\": 6, \"lang\": \"Greek\", \"words\": \"opsis\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Gk. ὄψις 'sight, appearance' is *okʷ-ti- : the root *h₃ekʷ- plus the abstract suffix \"\n   \"*-ti-, with the regular Greek treatment of *kʷ + t as πτ/ψ (*okʷ-ti- > ὄψις, cf. ὄψομαι 'I shall see', \"\n   \"ὄπωπα 'I have seen', ὄψ/ὄπός 'eye, face'). The word is classical (Herodotus, Plato) and is the base of \"\n   \"the productive suffix -οψις / -οψία of node #7.\"),\n \"derivation_fa\": (\"ὄψις یونانی «دید، دیدار، نمود» بازماندهٔ *okʷ-ti- است: ریشهٔ *h₃ekʷ- به‌همراه پسوندِ \"\n   \"اسم‌ساز *-ti-، با تحولِ قاعده‌مندِ یونانیِ *kʷ + t به πτ/ψ (پس *okʷ-ti- > ὄψις؛ قس ὄψομαι «خواهم دید»، \"\n   \"ὄπωπα «دیده‌ام»، ὄψ «چشم، چهره»). واژه کلاسیک است (هرودوت، افلاطون) و پایهٔ پسوندِ زایای -οψις/-οψία در \"\n   \"گرهٔ ۷ است. ادعای نورایی درست است.\"),\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. okʷ- §4 (AHD_watkins1985.txt leaf 796): \\\"Suffixed form *okʷ-ti- in Greek opsis, sight, appearance: OPSIN, -OPSIS, -OPSY; AUTOPSY, (IODOPSIN), (RHODOPSIN), SYNOPSIS.\\\"\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW p.776 (POK_03.txt leaf 10)\", \"stance\": \"supports\",\n    \"note\": \"The Greek section of ok̑ʷ- lists \\\"ὄψομαι 'ich werde sehen', ὄπωπα 'habe gesehen' ... ὄψ, gen. ὀπός 'Auge, Gesicht'\\\" — the paradigm ὄψις belongs to.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. optic (KLN_1971.txt line 167966)\", \"stance\": \"supports\",\n    \"note\": \"\\\"... fr. ὀπτός, 'seen; visible', verbal adj. of ὄψομαι, 'I shall see', fr. I.-E. base *oqʷ-, 'eye; to see', whence also ὄψ, gen. ὀπός, 'eye, face', 'sight'.\\\"\"}\n ]\n})\n\nm({\n \"id\": 7, \"lang\": \"English\", \"words\": \"optic, autopsy, synopsis\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"All three are learned Greek loans into English via Latin/French. Autopsy (1650s) < Gk. \"\n   \"αὐτοψία 'a seeing for oneself' (αὐτός + ὄψις) and synopsis (1610s) < Late Latin < Gk. σύνοψις 'a \"\n   \"seeing together, general view' are direct derivatives of ὄψις, so the arrow #6→#7 is exact for them. \"\n   \"Optic (15th c., MF optique < ML opticus < Gk. ὀπτικός) is a sibling rather than a child: ὀπτικός is \"\n   \"built on the verbal adjective ὀπτός 'seen' (*ok-to-), which Watkins lists as a separate suffixed form \"\n   \"of the same root, not as a derivative of ὄψις. That is a nuance of internal Greek morphology, not an \"\n   \"error about the root.\"),\n \"derivation_fa\": (\"هر سه واژه وام‌واژه‌های کتابیِ یونانی‌اند که از راه لاتین و فرانسه به انگلیسی رسیده‌اند. \"\n   \"autopsy (سدهٔ هفدهم) از αὐτοψία «خود-دیدن» (αὐτός + ὄψις) و synopsis (سدهٔ هفدهم) از σύνοψις «هم‌دیدن، \"\n   \"نگاه کلی» هر دو یکراست از ὄψις ساخته شده‌اند، پس پیکان #6→#7 برای آن‌ها دقیق است. اما optic (از \"\n   \"فرانسهٔ میانه optique و لاتین میانه opticus و یونانی ὀπτικός) فرزندِ ὄψις نیست بلکه خواهرِ آن است: \"\n   \"ὀπτικός بر صفت مفعولیِ ὀπτός «دیده‌شده» (از *ok-to-) ساخته شده که واتکینز آن را صورتِ پسوندیِ جداگانه‌ای \"\n   \"از همان ریشه می‌شمارد. این نکته‌ای در ساختواژهٔ درونیِ یونانی است، نه خطایی در ریشه.\"),\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. okʷ-: §4 gives \\\"-OPSIS, -OPSY; AUTOPSY ... SYNOPSIS\\\" under opsis, and §5 \\\"Suffixed form *ok-to- in Greek optos, seen, visible: OPTIC; CATOPTRIC, DIOPTER, OPTOMETRY, PANOPTIC\\\" — all three English words of the node are there, optic under the neighbouring formation.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. optic, synopsis, autopsy (KLN_1971.txt lines 167966, 239548, 23596)\", \"stance\": \"supports\",\n    \"note\": \"\\\"optic, adj. ... fr. Gk. ὀπτικός ... fr. ὀπτός, 'seen; visible', verbal adj. of ὄψομαι\\\"; \\\"synopsis, n., a general view, outline. — Late L., fr. Gk. σύνοψις, 'general view', lit. 'a seeing together', fr. σύν and ὄψις 'sight, view'\\\"; autopsy is entered as a post-mortem examination from Gk. αὐτοψία.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat\", \"stance\": \"supports\",\n    \"note\": \"Skeat enters Optic (F.-L.-Gk., from Gk. ὀπτικός, from ὄψομαι) and Synopsis (Gk. σύν + ὄψις) in the same terms; the OCR of the o- and s- pages is poor but both headwords are present.\"}\n ]\n})\n\nout = {\n \"pdf_page\": 373,\n \"book_page\": 343,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-07\",\n \"entries\": [e0, e1]\n}\n\nwith open(\"/home/sfmqrb/git/rishe/data/verification/page-373.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-373.py"
}
```


### [2026-09-07T20:42:55.315Z] TOOL RESULT

```
ok
```


## [2026-09-07T20:43:00.636Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -m json.tool data/verification/page-373.json > /dev/null && echo \"JSON OK\"; python3 tools/verify_check.py 373"
}
```


### [2026-09-07T20:43:02.126Z] TOOL RESULT

```
JSON OK
nodes verified: 22/22
node verdicts: {'confirmed': 17, 'disputed': 2, 'plausible': 3}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 15, 'partial': 9, 'not_checked': 3}
books consulted: {'supports': 38, 'silent': 20, 'contradicts': 3, 'partial': 7} | by book: {'KLN': 10, 'BQT': 5, 'SKT': 5, 'AHD': 4, 'PHD': 4, 'HRN': 4, 'NYB': 4, 'POK': 4, 'BRT': 3, 'SYN': 3, 'HUB': 3, 'ARY': 3, 'FSD': 3, 'KNT': 2, 'WLD': 2, 'LAT': 2, 'IEC': 2, 'ISS': 1, 'WEB': 1, 'FVQ': 1, 'MON': 1, 'CHEUNG': 1}
```


## [2026-09-07T20:43:08.191Z] TOOL CALL #93: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 - <<'EOF'\nimport json\nd=json.load(open('data/verification/page-373.json'))\nfor e in d['entries']:\n    assert e.get('note_fa') and e.get('ref_check') and e.get('consulted'), e['entry']\n    for n in e['nodes']:\n        for k in ('derivation','derivation_fa','ref_check','consulted','words','lang','verdict'):\n            assert n.get(k), (e['entry'],n['id'],k)\n        assert len(n['consulted'])>=2, (e['entry'],n['id'])\nprint(\"all nodes complete; entries:\",len(d['entries']),\"nodes:\",sum(len(e['nodes']) for e in d['entries']))\nEOF\ngit -C /home/sfmqrb/git/rishe status --short"
}
```


### [2026-09-07T20:43:09.483Z] TOOL RESULT

```
all nodes complete; entries: 2 nodes: 22
?? data/verification/page-373.json
```


## [2026-09-07T20:43:14.436Z] TOOL CALL #94: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; git check-ignore -v data/verification/sources/refs/ocr/BQT/71.png data/verification/sources/web/ 2>&1 | head"
}
```


### [2026-09-07T20:43:15.814Z] TOOL RESULT

```
.gitignore:9:data/verification/sources/refs/	data/verification/sources/refs/ocr/BQT/71.png
```


## [2026-09-07T20:43:20.215Z] TOOL CALL #95: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; git status --short data/verification/sources/web | head; git check-ignore -v data/verification/sources/web/844b9204c5629849.txt"
}
```


### [2026-09-07T20:43:21.608Z] TOOL RESULT

```
Exit code 1
```


## [2026-09-07T20:43:24.730Z] TOOL CALL #96: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,20p' .gitignore; echo ---; ls data/verification/sources/web | wc -l; git ls-files data/verification/sources | head -3"
}
```


### [2026-09-07T20:43:24.802Z] TOOL RESULT

```
# regenerable from the PDF via pdftoppm (see tools/)
data/pages/

# built site (regenerate with tools/build_site.py)
site/risheh.html
__pycache__/

# Verification: OCR texts of copyrighted reference works (local audit copies only)
data/verification/sources/refs/
---
4128
data/verification/sources/MISSING_REFERENCES.md
data/verification/sources/SOURCE_MATRIX.md
data/verification/sources/refs_online.json
```


## [2026-09-07T20:43:46.614Z] AGENT

Done. `verify_check.py 373` reports 22/22 nodes, 0 PROBLEM lines.

**Page 373 (book p. 343) — 2 entries verified, 3 redirects skipped (Ol 1, Ol 2, Olěna)**

Roots: 2 confirmed. Nodes: 17 confirmed, 3 plausible, 2 disputed. Ref checks: 15 supports / 9 partial / 3 not_checked.

Disputed:
- **Ôku #5 `karši-ptan` (Av./OP, "swift flying")** — Bartholomae (AiW col. **459**, not the cited 458) derives the first member `karši-` "aus *k̑ers-, zu lat. currō" i.e. PIE *ḱers- "to run" (Pok. 583), not *ōḱus; the compound really does mean "Schnellflieger" and Bartholomae himself compares Gk. ὠκυπέτης and Lat. accipiter, which is where Nourai's gloss and NOTE come from. Also Young Avestan only — "Old Persian" is wrong (nothing in Kent).
- **Ôku #11 `ôkeanos`** — Beekes: Pre-Greek substrate *ūkʲān-; Etymonline "unknown origin"; Klein "of uncertain etymology". Only Nourai's own source (Funk & Wagnalls p.1707) still says "perhaps < ōkys, swift". The chart's NOTE is the better half: Kent p.164 s.v. `ā` really does print "Gk. ō- in ō-keanós '(lying round about), ocean'" — the Thieme/Janda *ō-ḱey- proposal.

Plausible: #6 `karšift` and #7 `kašak` (Tomaschek's guess relayed by Horn p.191 with "Deutung nicht sicher"; BQT 1652 repeats it; not phonetically regular); #8 Latin `acu` (no free-standing Latin adjective *acu* — "Positiv fehlt"; only the compound member in acupedius/accipiter).

No transcription_suspect nodes and **no extraction errors** — the JSON matches the printed page; `karši-ptan` is Horn's own citation form, faithfully copied by Nourai.

Best finds: BQT p.71 (read from the archive.org leaf image, saved as `refs/ocr/BQT/71.vision.txt` + `71.png`) carries Mo'in's footnote deriving آهو from "صفت اوستایی âsu ... پهلوی âhûk ... سغدی âsuk" — Nourai's arrows #1→#2→#3 and #1→#4 verbatim; Gharib SOD entry 258 (p.10) gives "ʾsʾwk < *āsuka-, Av. āsu-, Pahl. āhug"; BQT p.2143 footnote and Nyberg (s.v. murw-niš) both link نشان to MP niš- "to see" ← Av. aiwi-axš-.
