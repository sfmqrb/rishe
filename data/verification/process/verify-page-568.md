# Verification process log — verify-page-568


## [2026-10-17T00:30:14.443Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 568 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-568.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-568.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-568.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 568` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-17T00:30:14.517Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-17T00:30:17.530Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-17T00:30:17.552Z] TOOL RESULT

```
1	# Etymology verification task — instructions
2	
3	You are verifying the etymological derivations from Ali Nourai's *An Etymological
4	Dictionary of Persian, English and other Indo-European Languages* (1999), which this
5	repository (`/home/sfmqrb/git/rishe-private`) turned into JSON (`data/extracted/batch/page-<pdf>.json`).
6	Compact text renderings of the charts are in
7	`/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-<pdf>.txt`.
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
52	  offsets and lookup hints: `/home/sfmqrb/git/rishe-private/data/verification/sources/refs_online.json`
53	  (keys = abbreviations; `kind`, `url`, `lookup_hint`, `local_file`, `page_offset`, `scans`, `cites`).
54	- If `local_file` is set, the OCR text of that book is on disk under
55	  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/`: grep it for the headword (try
56	  several spellings — OCR of diacritics is noisy; e.g. `grep -n -i 'barak' …`) and, if a page
57	  offset is given, locate the cited page (pages are separated by form-feeds; `_pages.txt`
58	  files also carry `[pdf page N]` tags; use `awk 'BEGIN{RS="\f"} NR==<n>' file` to print one
59	  page). Read the entry and judge whether it actually says what Nourai's arrow says.
60	- **Scanned references without full OCR text** (Borhan-e Qate' vols 3–5 = BQT pages
61	  ~1208–2475, Farahvashi's Iranvij = IRN, Aryanpur = ARY, any entry with a `scans` list): do
62	  NOT OCR whole books. Fetch only the cited page:
63	  `python3 /home/sfmqrb/git/rishe-private/tools/ref_page.py BQT:918 --image`
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
103	`/home/sfmqrb/git/rishe-private/data/verification/sources/SOURCE_MATRIX.md`. Minimum per node:
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
140	with `pdftoppm -f <pdf page> -l <pdf page> -r 300 -png -singlefile /home/sfmqrb/git/rishe-private/EtymologicalDictionary-persian-english.pdf /tmp/pg<pdf page>`
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
187	  `python3 /home/sfmqrb/git/rishe-private/tools/fetch_source.py '<URL>' --note '<page N, root X, what you used it for>'`
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
224	Write `/home/sfmqrb/git/rishe-private/data/verification/page-<pdf>.json` (UTF-8, no BOM):
225	
226	Several agents run at the same time and share the scratchpad and `/tmp`, so every temporary
227	file you create must carry your page number in its name (e.g. `e0-363.json`, `pg363.png`,
228	`draft-363.json`), never a bare `e0.json` or `entry.json` — another agent will overwrite it.
229	
230	In the shell, `ls` is aliased to `eza`, which can hang without a terminal and leave your
231	command stuck. List files with `command ls` or `find` instead.
232	
233	```json
234	{
235	  "pdf_page": 126,
236	  "book_page": 96,
237	  "verified_by": "claude-opus-5",
238	  "verified_on": "2026-09-05",
239	  "entries": [
240	    {
241	      "entry": 0,
242	      "root": "Dheigh, Dhigha",
243	      "verdict": "confirmed",
244	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
245	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
246	      "note_fa": "ریشهٔ هندواروپایی آغازین *dʰeyǵʰ- «خمیر کردن، شکل دادن (گِل)» … ادعای نورایی درست است.",
247	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
248	      "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
249	      "consulted": [{"src": "WLD", "where": "Bd. I 833", "stance": "supports", "note": "…"}],
250	      "nodes": [
251	        {
252	          "id": 6,
253	          "lang": "Avestan",
254	          "words": "pairi-daeza",
255	          "verdict": "confirmed",
256	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' …",
257	          "derivation_fa": "«پردیس» … اوستایی pairi-daēza- «دیوارکشیده، باغِ محصور» از pairi «پیرامون» و daēza- «دیوار» …",
258	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza"],
259	          "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
260	          "consulted": [{"src": "BRT", "where": "col. 866", "stance": "supports", "note": "…"}]
261	        }
262	      ]
263	    }
264	  ]
265	}
266	```
267	
268	Rules:
269	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
270	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
271	- `words` = the transliterations of the node joined by "; " (copy from the chart).
272	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
273	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
274	- Keep `note` on the entry for root-level comments and for anything cross-cutting.
275	- If a node lists several words, cover each word; if they differ in verdict, use the worst
276	  verdict for the node and explain per word in `derivation`.
277	- Where the chart's own NOTE already records a dispute, evaluate it: say which side modern
278	  scholarship takes.
279	- Every node has `ref_check` (array, may contain a single `not_checked` item) AND `consulted`
280	  (array) AND `derivation_fa` (string); every entry has `note_fa`.
281	- Valid JSON only. Test it with `python3 -m json.tool` before finishing, then run
282	  `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
283	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
284	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
285	  any extraction errors (JSON differs from the printed page) the owner must fix.
286	  Do not paste the JSON back into your reply.
287	
```


## [2026-10-17T00:30:18.037Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-568.txt"
}
```


### [2026-10-17T00:30:18.066Z] TOOL RESULT

```
1	=== PDF page 568 (book page 538) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Yôs : to gird, belt  (refs POK:513)
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:513; KLN:1770; SYN:434 | yâh 4 : to put belt on ; yâhma : cover, clothes ; yâsta, yânhaeiti : belted
5	  #2 (parent #1) [Pahlavi] refs=HUB:49; HRN:93 | yâmak : clothes
6	    #3 (parent #2) [Persian] refs=BQT:556, 660 | jâmeh «جامه» : clothes ; pâ-jâmeh «پاجامه» : pants, pajamas ☞Ped ; jâmeh-dân «جامه دان» : suitcase ☞Dhě 2
7	      #4 (parent #3) [Hindustani] refs=HJB:748 | pâě-jâma
8	        #5 (parent #4) [English] refs=AHD; KLN | pajamas
9	          #6 (parent #5) [French] refs=ETM:63 | 
10	            #7 (parent #6) [Persian] refs=MON:868,902 | pîjâmeh «پی جامه» | extra: پیژاما
11	      #8 (parent #3) [Russian] refs=ETM:64 | čamadan : suitcase
12	        #9 (parent #8) [Persian] refs=ETM:64 | čamedân «چمدان» : suitcase
13	#10 (parent #0) [Greek] refs=AHD | zôně : girdle ; zonarion : a girdle worn by non-Moslems to be identified
14	  #11 (parent #10) [Persian] refs=BQT:1033; MON | zonnâr «زنّار» : belt worn by non-Moslems
15	  #12 (parent #10) [English] refs=None | zone
16	--- entry 1 ---
17	ROOT [Indo-European] Yu, Iu, Ues : you  (refs POK:513)
18	#1 (parent #0) [Avestan] refs=POK:513 | yŭš, yŭšmat : you
19	  #2 (parent #1) [Persian] refs=HRN:176; BQT:1291 | šomâ «شما» : you
20	#3 (parent #0) [Germanic] refs=AHD | jŭz : you
21	  #4 (parent #3) [English] refs=None | you, your
22	--- entry 2 ---
23	ROOT Yuwn -> redirect to Yeu 2
24	--- entry 3 ---
25	ROOT Yuwnkos -> redirect to Yeu 2
26	
```


## [2026-10-17T00:30:18.715Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-568.json"
}
```


### [2026-10-17T00:30:18.739Z] TOOL RESULT

```
1	{
2	  "pdf_page": 568,
3	  "book_page": 538,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Yôs",
8	        "lang": "Indo-European",
9	        "refs": "POK:513",
10	        "gloss": "to gird, belt"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Avestan / Old Persian",
17	          "refs": "POK:513; KLN:1770; SYN:434",
18	          "words": [
19	            {"translit": "yâh 4", "gloss": "to put belt on", "script": null},
20	            {"translit": "yâhma", "gloss": "cover, clothes", "script": null},
21	            {"translit": "yâsta, yânhaeiti", "gloss": "belted", "script": null}
22	          ],
23	          "script_extra": null,
24	          "note": null,
25	          "quote": null
26	        },
27	        {
28	          "id": 2,
29	          "parent": 1,
30	          "lang": "Pahlavi",
31	          "refs": "HUB:49; HRN:93",
32	          "words": [
33	            {"translit": "yâmak", "gloss": "clothes", "script": null}
34	          ],
35	          "script_extra": null,
36	          "note": null,
37	          "quote": null
38	        },
39	        {
40	          "id": 3,
41	          "parent": 2,
42	          "lang": "Persian",
43	          "refs": "BQT:556, 660",
44	          "words": [
45	            {"translit": "jâmeh", "gloss": "clothes", "script": "جامه"},
46	            {"translit": "pâ-jâmeh", "gloss": "pants, pajamas", "script": "پاجامه", "see": ["Ped"]},
47	            {"translit": "jâmeh-dân", "gloss": "suitcase", "script": "جامه دان", "see": ["Dhě 2"]}
48	          ],
49	          "script_extra": null,
50	          "note": null,
51	          "quote": null
52	        },
53	        {
54	          "id": 4,
55	          "parent": 3,
56	          "lang": "Hindustani",
57	          "refs": "HJB:748",
58	          "words": [
59	            {"translit": "pâě-jâma", "gloss": null, "script": null}
60	          ],
61	          "script_extra": null,
62	          "note": null,
63	          "quote": null
64	        },
65	        {
66	          "id": 5,
67	          "parent": 4,
68	          "lang": "English",
69	          "refs": "AHD; KLN",
70	          "words": [
71	            {"translit": "pajamas", "gloss": null, "script": null}
72	          ],
73	          "script_extra": null,
74	          "note": null,
75	          "quote": null
76	        },
77	        {
78	          "id": 6,
79	          "parent": 5,
80	          "lang": "French",
81	          "refs": "ETM:63",
82	          "words": [],
83	          "script_extra": null,
84	          "note": null,
85	          "quote": null
86	        },
87	        {
88	          "id": 7,
89	          "parent": 6,
90	          "lang": "Persian",
91	          "refs": "MON:868,902",
92	          "words": [
93	            {"translit": "pîjâmeh", "gloss": null, "script": "پی جامه"}
94	          ],
95	          "script_extra": "پیژاما",
96	          "note": null,
97	          "quote": null
98	        },
99	        {
100	          "id": 8,
101	          "parent": 3,
102	          "lang": "Russian",
103	          "refs": "ETM:64",
104	          "words": [
105	            {"translit": "čamadan", "gloss": "suitcase", "script": null}
106	          ],
107	          "script_extra": null,
108	          "note": null,
109	          "quote": null
110	        },
111	        {
112	          "id": 9,
113	          "parent": 8,
114	          "lang": "Persian",
115	          "refs": "ETM:64",
116	          "words": [
117	            {"translit": "čamedân", "gloss": "suitcase", "script": "چمدان"}
118	          ],
119	          "script_extra": null,
120	          "note": null,
121	          "quote": null
122	        },
123	        {
124	          "id": 10,
125	          "parent": 0,
126	          "lang": "Greek",
127	          "refs": "AHD",
128	          "words": [
129	            {"translit": "zôně", "gloss": "girdle", "script": null},
130	            {"translit": "zonarion", "gloss": "a girdle worn by non-Moslems to be identified", "script": null}
131	          ],
132	          "script_extra": null,
133	          "note": null,
134	          "quote": null
135	        },
136	        {
137	          "id": 11,
138	          "parent": 10,
139	          "lang": "Persian",
140	          "refs": "BQT:1033; MON",
141	          "words": [
142	            {"translit": "zonnâr", "gloss": "belt worn by non-Moslems", "script": "زنّار"}
143	          ],
144	          "script_extra": null,
145	          "note": null,
146	          "quote": {
147	            "text": "ای بر سر بازارت صد خرقه به زنّاری - وز روی تو در عالم هر روی به دیواری",
148	            "poet": "Molavî"
149	          }
150	        },
151	        {
152	          "id": 12,
153	          "parent": 10,
154	          "lang": "English",
155	          "refs": null,
156	          "words": [
157	            {"translit": "zone", "gloss": null, "script": null}
158	          ],
159	          "script_extra": null,
160	          "note": null,
161	          "quote": null
162	        }
163	      ]
164	    },
165	    {
166	      "root": {
167	        "name": "Yu, Iu, Ues",
168	        "lang": "Indo-European",
169	        "refs": "POK:513",
170	        "gloss": "you"
171	      },
172	      "nodes": [
173	        {
174	          "id": 1,
175	          "parent": 0,
176	          "lang": "Avestan",
177	          "refs": "POK:513",
178	          "words": [
179	            {"translit": "yŭš, yŭšmat", "gloss": "you", "script": null}
180	          ],
181	          "script_extra": null,
182	          "note": null,
183	          "quote": null
184	        },
185	        {
186	          "id": 2,
187	          "parent": 1,
188	          "lang": "Persian",
189	          "refs": "HRN:176; BQT:1291",
190	          "words": [
191	            {"translit": "šomâ", "gloss": "you", "script": "شما"}
192	          ],
193	          "script_extra": null,
194	          "note": null,
195	          "quote": null
196	        },
197	        {
198	          "id": 3,
199	          "parent": 0,
200	          "lang": "Germanic",
201	          "refs": "AHD",
202	          "words": [
203	            {"translit": "jŭz", "gloss": "you", "script": null}
204	          ],
205	          "script_extra": null,
206	          "note": null,
207	          "quote": null
208	        },
209	        {
210	          "id": 4,
211	          "parent": 3,
212	          "lang": "English",
213	          "refs": null,
214	          "words": [
215	            {"translit": "you, your", "gloss": null, "script": null}
216	          ],
217	          "script_extra": null,
218	          "note": null,
219	          "quote": null
220	        }
221	      ]
222	    },
223	    {
224	      "root": {"name": "Yuwn", "redirect": "Yeu 2"},
225	      "nodes": []
226	    },
227	    {
228	      "root": {"name": "Yuwnkos", "redirect": "Yeu 2"},
229	      "nodes": []
230	    }
231	  ]
232	}
233	
```


## [2026-10-17T00:30:22.944Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/verification/sources/SOURCE_MATRIX.md | head -80; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','SYN','HUB','HRN','BQT','HJB','AHD','ETM','MON','WLD','IEC','BRT','KNT','PHD','NYB','CHEUNG','ARY','SKT','FSD','WEB','AID','LKT','FVQ','AFM','PLA']:\n  v=d.get(k);print(k, v and {x:v.get(x) for x in ['local_file','page_offset','scans','kind','lookup_hint']})\n\"; command ls data/verification/sources/refs/ | head -100"
}
```


### [2026-10-17T00:30:23.543Z] TOOL RESULT

```
<persisted-output>
Output too large (29.8KB). Full output saved to: /home/sfmqrb/.claude-work/projects/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/tool-results/bflvn21wz.txt

Preview (first 2KB):
# Source matrix — which local books to grep for each kind of node

All files are OCR text; pages are separated by form-feeds (`\f`) and, in the `_pages.txt` files, tagged `[pdf page N]`. Print one page with `awk 'BEGIN{RS="\f"} NR==<n>' file`. Grep several spellings (OCR of diacritics is noisy; Persian OCR is rough — try short substrings). Full titles, page offsets and what a cited number means: data/verification/sources/refs_online.json.

ARY (Aryanpur) is alphabetical by Persian headword; grep the Persian word in ARY_pages.txt or the Latin-caps transliteration in ARY_latin_index_pages.txt, note the [pdf page N] tag, and quote from that page (printed page = pdf page + 1).


## Indo-European roots (any IE node, root boxes)

- **POK** — J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_02.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_03.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_full.txt`
- **WLD** — A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-3
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt`
...
</persisted-output>
```


## [2026-10-17T00:30:25.884Z] TOOL CALL #5: Bash

```json
{
 "command": "cat /home/sfmqrb/.claude-work/projects/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/tool-results/bflvn21wz.txt | sed -n 20,400p | cut -c1-300"
}
```


### [2026-10-17T00:30:26.440Z] TOOL RESULT

```
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt`
- **AHD** — W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appe
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt`
- **IEC** — S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt`
- **SYN** — C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt`
- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1971.txt`
- **SKT** — W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt`
- **LEW** — A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LEW_1910.txt`
- **LAT** — A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LAT.txt`
- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt`

## Iranian: Avestan / Old Persian / Pahlavi / Sogdian / Khotanese / New Persian

- **BRT** — C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BRT.txt`
- **KNT** — R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT.txt` (truncated before the lexicon's h–z section, ~p. 208 on)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT_full.txt` (complete archive.org djvu text — use this for lexicon pages 208–215: haumavarga-, siyamam, etc.)
- **PHD** — D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD_mackenzie.txt`
- **NYB** — H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol2_glossary.txt`
- **HRN** — P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt`
- **HUB** — H. Hübschmann, Persische Studien, Strassburg 1895
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt`
- **CHEUNG** — CHEUNG
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/CHEUNG.txt`
- **SOD** — Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD_pages.txt`
- **SNS** — Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS_pages.txt`
- **BQT** — Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/19
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_alt_v1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_dli_part1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf`
- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
POK {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt', 'page_offset': 'POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a lea
KLN {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt', 'page_offset': 'KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has
SYN {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt', 'page_offset': 'leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n
HUB {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt', 'page_offset': 'leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n
HRN {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt', 'page_offset': 'leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<id
BQT {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sf
HJB {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HJB.txt', 'page_offset': 'leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.490, leaf 905 = p.870). local file has \\f between leaves (0-based leaf index i == i-th form-feed 
AHD {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt', 'page_offset': "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the 
ETM {'local_file': None, 'page_offset': None, 'scans': None, 'kind': 'catalog', 'lookup_hint': 'Searched archive.org, ketabnak, noorlib, web: not found.'}
MON {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/
WLD {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.t
IEC {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt', 'page_offset': 'TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at 
BRT {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BRT.txt', 'page_offset': 'Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). G
KNT {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT.txt', 'page_offset': 'leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online
PHD {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD.txt', 'page_offset': 'leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n
NYB {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol2_glossary.txt', 'page_offset': 'Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/detail
CHEUNG None
ARY {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'], 'page_offset': 'printed page = pdf page + 1', 'scans': [{'file': '/home/sfmqrb/git/
SKT {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt', 'page_offset': 'leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n
FSD {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol1.txt', 'page_offset': 'vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset 
WEB {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WEB_vol1.txt', 'page_offset': 'not reliably detected (page_numbers.json sparse); grep headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org
AID {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AID.txt', 'page_offset': 'leaf = printed + 18 (e.g. leaf 20 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n
LKT {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LKT.txt', 'page_offset': 'leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n
FVQ {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ.txt'], 'page_offset': 'printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 335 leaves)', 'scans': None, 'kind': 'archive_dj
AFM {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM.txt'], 'page_offset': "198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image", 'sc
PLA {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming
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
KNT_full.txt
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
SKT_dli_revised.txt
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
```


## [2026-10-17T00:30:30.177Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; command ls data/verification/ | tail -5; python3 -c \"\nimport json;d=json.load(open('data/verification/page-558.json'));e=d['entries'][0];print(json.dumps({k:e[k] for k in e if k!='nodes'},ensure_ascii=False,indent=1)[:2500]);print(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:3000])\"; sed -n 1,200p tools/verify_check.py | grep -n -i 'problem' | head -40"
}
```


### [2026-10-17T00:30:30.659Z] TOOL RESULT

```
page-97.json
page-98.json
page-99.json
process
sources
{
 "entry": 0,
 "root": "Xac 1",
 "verdict": "plausible",
 "modern_form": "Skt. khac- 'shine through' (?) (Buck, after Uhlenbeck); modern view: Skt. kāca- probably a Nuristani loan, cognate with Skt. kāś- 'to shine'",
 "note": "The book files this chart under X because Nourai writes Skt. kh as X ('Xac' = Skt. khac-). The root and gloss come straight from Buck SYN 620, who gives it with a question mark: 'Skt. kāca- : khac- shine through (?). Uhlenbeck 51.' Wiktionary (after Mayrhofer) calls kāca- 'likely borrowed from a Nuristani language (*kāt's'a), cognate with Sanskrit kāś- to shine brightly'. Either way, a 'shining' root sits behind the glass word, so the chart is defensible, but the specific root khac- is uncertain. The extraction matches the printed page.",
 "note_fa": "نورایی ریشه را سنسکریت khac- «از درون درخشیدن» می‌گیرد (او kh سنسکریت را X می‌نویسد، از همین رو این مدخل زیر حرف X آمده). این ریشه را باک (SYN ص ۶۲۰) به پیروی از اولنبک، و خودش با علامت پرسش، آورده است. ویکی‌واژه به نقل از مایرهوفر سنسکریت kāca- «شیشه» را احتمالاً وام‌واژه‌ای از زبان‌های نورستانی (*kāt's'a) و هم‌ریشه با kāś- «درخشیدن» می‌داند. پس پیوند «شیشه» با ریشه‌ای به معنای درخشیدن پذیرفتنی است، اما خودِ ریشهٔ khac- قطعی نیست و ادعای نورایی را باید با احتیاط پذیرفت.",
 "sources": [
  "https://en.wiktionary.org/wiki/काच"
 ],
 "ref_check": [
  {
   "ref": "SYN:620",
   "status": "supports",
   "note": "SYN.txt (printed p. 620, section 9.74 GLASS), para 7: 'Skt. kāca- : khac- shine through (?). Uhlenbeck 51.' This is exactly Nourai's root and gloss, including Buck's hesitation."
  }
 ],
 "consulted": [
  {
   "src": "POK",
   "where": "POK_full.txt grep 'kāca|kāś-|kāçat'",
   "stance": "silent",
   "note": "no Pokorny entry for Skt. kāca- or kāś-."
  },
  {
   "src": "WLD",
   "where": "WLD_Bd1/Bd2_pages.txt, WLD_band3.txt grep 'kāca'",
   "stance": "silent",
   "note": "no hit."
  },
  {
   "src": "AHD",
   "where": "AHD_watkins1985.txt",
   "stance": "silent",
   "note": "no IE root for Skt. kāca- (an Indo-Aryan word with no European cognates)."
  }
 ]
}
{
 "id": 1,
 "lang": "Sanskrit",
 "words": "kâca",
 "verdict": "confirmed",
 "derivation": "Skt. kāca- m. 'glass, crystal, quartz' (classical, post-Vedic). Buck lists it as the Sanskrit word for GLASS and tentatively links it to khac- 'shine through'. Wiktionary instead suggests a Nuristani loan cognate with kāś- 'shine'. It continues in Pali kāca, Hindi kā̃c, Bengali kāc, Malay kaca. The gloss 'pearl' comes from Mo'in's BQT footnote, which cites Monier-Williams for 'شیشه، آبگینه، مروارید' (glass bead). The word and its sense 'glass' are secure.",
 "derivation_fa": "سنسکریت kāca- به معنای «شیشه، بلور، کوارتز» در سنسکریت کلاسیک به‌خوبی گواهی شده و در پالی kāca و هندی kā̃c (کانچ) و بنگالی kāc بازمانده است. باک آن را با تردید به ریشهٔ khac- «درخشیدن» می‌پیوندد و ویکی‌واژه آن را وامی از نورستانی می‌داند. معنای «مروارید» را معین در حاشیهٔ برهان قاطع به نقل از فرهنگ مونیر-ویلیامز آورده است (مهرهٔ شیشه‌ای). وجود واژه و معنای «شیشه» درست است.",
 "sources": [
  "https://en.wiktionary.org/wiki/काच"
 ],
 "ref_check": [
  {
   "ref": "SYN:620",
   "status": "supports",
   "note": "SYN p.620 GLASS table: 'Skt. kāca-'; para 7 'Skt. kāca- : khac- shine through (?)'."
  },
  {
   "ref": "BQT:1556",
   "status": "supports",
   "note": "BQT vol 3 p.1556 (pdf 349; vision file ocr/BQT/1556.vision.txt), footnote 9 to کاچ: 'قس: سانسکریت kâcá (شیشه، آبگینه، مروارید) «ویلیامز ۲:۲۶۸»'. Mo'in gives the Sanskrit word with these meanings."
  }
 ],
 "consulted": [
  {
   "src": "POK",
   "where": "POK_full.txt grep 'kāca'",
   "stance": "silent",
   "note": "not in Pokorny."
  },
  {
   "src": "WLD",
   "where": "WLD Bd1/Bd2 grep 'kāca'",
   "stance": "silent",
   "note": "not in Walde-Pokorny."
  },
  {
   "src": "SYN",
   "where": "p.620 §9.74",
   "stance": "supports",
   "note": "'Skt. kāca-' as the Sanskrit word for 'glass'."
  }
 ]
}
22:    missing_pages, problems = [], []
46:            problems.append(f"page {pg}: invalid JSON ({ex})")
52:                problems.append(f"page {pg}: entry {i} ({e['root']['name']}) missing")
56:                problems.append(f"page {pg}: entry {i} root verdict {rv!r} invalid")
65:                    problems.append(f"page {pg}: entry {i} ({e['root']['name']}) node #{n['id']} missing")
69:                    problems.append(f"page {pg}: entry {i} node #{n['id']} verdict {nv!r} invalid")
74:                    problems.append(f"page {pg}: entry {i} node #{n['id']} has no derivation")
89:    for p in problems:
90:        print("PROBLEM:", p)
94:    return 1 if problems else 0
```


## [2026-10-17T00:30:48.841Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'EOF'\nimport re\ndef leaf(f,n):\n    return open(f,errors='ignore').read().split('\\f')[n]\n# POK 513 -> leaf 521\nt=leaf('POK_01.txt',521)\nfor kw in ['ōs','gürt','ζών','ū','ihr','iū','yūš']:\n    pass\nprint(t[:6000])\nEOF"
}
```


### [2026-10-17T00:30:49.439Z] TOOL RESULT

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
  File "<stdin>", line 3, in leaf
IndexError: list index out of range
```


## [2026-10-17T00:30:52.744Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'EOF'\nfor f in ['POK_01.txt','POK_02.txt','POK_full.txt']:\n    t=open(f,errors='ignore').read().split('\\f'); print(f,len(t))\nt=open('POK_02.txt',errors='ignore').read().split('\\f')\nfor i in range(len(t)):\n    if 'gürten' in t[i] and ('ζών' in t[i] or 'zōn' in t[i] or 'yāh' in t[i] or 'ζω' in t[i]):\n        print('LEAF',i); print(t[i][:5000])\nEOF"
}
```


### [2026-10-17T00:30:53.200Z] TOOL RESULT

```
POK_01.txt 364
POK_02.txt 434
POK_full.txt 1
```


## [2026-10-17T00:30:55.569Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'gürten' POK_full.txt | head; grep -n 'yāh\\|jūs\\|yūš\\|iūs' POK_full.txt | head -20"
}
```


### [2026-10-17T00:30:55.875Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:30:58.471Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; wc -c POK_*.txt; grep -n -i 'gurten\\|gürt' POK_0*.txt | head; python3 -c \"\nt=open('POK_02.txt',errors='ignore').read().split('\\f');print(t[513-344][:300])\""
}
```


### [2026-10-17T00:30:58.809Z] TOOL RESULT

```
 981836 POK_01.txt
1137861 POK_02.txt
1170809 POK_03.txt
3971883 POK_full.txt
7262389 total
POK_03.txt:298:Ai.  vielleicht  palla-  m.  , Kornbehälter',  palll  .Getreidemaß'  (falls  -II-  aus -dl-)]  ahd.  fazzön,  mhd.  vazzen  ,in  ein  Gefäß  tun,  fassen,  rüsten,  sich bekleiden',  ahd.  fezzil,  mhd.  vezzel  ,Band,  Fessel',  ags.  fetel{s)  m.  , Gürtel', aisl.  fetill  m.  , Schulterband'  (germ.  *fatila-),  ahd.  vazz  , Behälter,  Kasten', as.  fat  n.  , Gefäß',  ags.  faet  n.  , Gefäß,  Faß',  aisl.  fat  n.  , Gefäß,  Kleid'; 3Lgs.  ßetels  ,Gefäß',  ahd.  givazzi  , Bagage',  mhd.  gevxzze,  nhd.  , Gefäß';  got. fetjan,  ags.  fäetan  , schmücken',  aisl.  fseta  ,es  mit  jemandem  zu  tun  haben (,schmücken'  aus  , schön  tun  mit?');  lit.  pMas  , Getreidegarbe',  lett.  peda ,Bund,  Armvoll',  ablaut.  lit.  püodas,  lett.  puods  m.  ,Topf'.
POK_03.txt:546:ai.  pari,  av.  pairi,  apers.  pariy,  gr.  tvsql,  tcbq,  alb.  per  (z.  T.  auch  = idg.  *pr6),  pej,  pe-,  daneben  per  {*periy  mit  wiederhergestelltem  r;  lat. per  (-^per  oder  *peri):  osk.-umbr.  per-  und  per t  {*per-ti)]  gall.  eri-,  air.  iV, er-  (analogisch  *ero-)]  cymr.  com.  bret.  er;  got.  fair-,  ags.  fyr-,  ahd. /r- ,ver-',  ahd.  as.  firi-  ds.;  apr.  per,  lit.  per,  per-]  slav.  per-  'm  aksl.  pr^- usw. ;  aus  ,vorwärts'  entwickelte  sich  schon  idg.  die  Bedeutung  ,sehr^  (ai. pari-pri-  ,sehr  lieb',  gr.  Ttsgi-y.allrjg  ,sehr  schon',  lat.  per-magnus  ,sehr groß';  lit.  per-didis  ,zu  groß',  aksl.  prä-hlag^  ,sehr  gut'),  dann  die  der Überlegenheit  {2i\.  pari — as-,pdri — bhü-  ,übertreffen',  gr.  negi-eZvai  ds.),  des Übermaßes  oder  hohen  Grades  (ai.  pdri-vid-,  gr.  Ttegl-oida,  lat.  per-videre ,genau  wissen');  besonders  ai.  und  gr.  ist  die  Bedeutung  ,ringsum,  um- herum'  (ai.  pari  i-  ,umhergehen',  gr.  negi-ievai]  gr.  TC£Qi-L,(bvvviii  =  lit. per-jousti  ,umgürten*) ;
POK_03.txt:1271:Ai.  rasanä  f.  ,Strick,  Riemen,  Gürtel',  rasmi-  m.  , Strang,  Riemen,  Zügel' ; aschwed.  hurraka  {hurd-)  ,Heck-Band',  aisl.  rakki  m.  ,Stropp   zum   Fest- halten der  Rahe',  ags.  racca  m.  ds.,  aisl.  rekendi  n.,  rekendr  f.  PL  ,Kette, Fessel';  ags.  racente,  racete  f.,  ahd.  rahhinza  f.  d. WP.  II  362.
POK_03.txt:1347:vermutlich  as.  ahd.  riomo  ,Riemen,  ledernes  Band,  Gürtel'  (*,abge- rissener  Hautstreifen'),  ags.  reoma,  reama  ds.,  auch  ,dünne  Haut'  (vgl. S.  873  *reugh-m(e)n-  ,Rahm');  mnd.  mndl.  rOw,  rüne,  schwäb.  raun  ,Wallach, Gaul',  wegen  ofries.  han-räne  , Hahnrei'  (eigentlich  »verschnittener  Hahn') ursprüngl.  ,equus  castratus',  mnl.  runen,  ruynen  'schneiden,  kastrieren*; (nhd.  runken);  entlehnt  lett.  rünlt  ,kastrieren',  ebenso  finn.  ruuna  , Wallach*, ruunata  , kastrieren*;
POK_03.txt:1839:lit.  sam-,  sq-  (z.  B.  sam-dyti  , dingen',  sdn-dora  , Eintracht',  sq-zine  , Ge- wissen, conscientia'),  apr.  san-,  sen-  (^san-insle  , Gürtel'),  sen  (*sem)  Präp. ,mit'  (idg.  *sem);  aksl.  so-  ,mit'  (sg-sMh  , Nachbar',  vgl.  ai.  sam-sdd-  »Ver- sammlung'), sq-log^  ,consors  tori',  vgl.  ä-Xoxog  usw. ;
POK_03.txt:2474:(über  nhd.  Schärpe,  hair.  schäyyfen  , Gürtel',  ndl.  sjerp,  engl,  scarf  ds.^ spätahd.  Scherbe  ,Tasche',  nd.  schrap  ,Tasche',  aisl.  skreppa,  , Rucksack' s.  Meyer-Lübken723,  Kluge-Goetzei^6ö3,  Holthausea  Awn.  Wb.  257: alles  aus  lat.  scirpea  ,Binsentasche') ;
POK_03.txt:5758:air.  ferenn  (*uereno-)  , Gürtel*,  fertae  (mir.  fert)  , Grabhügel*  (mit  Steinen verschlossen)  =  ags.  weoi-d  (s.  unten),  air.  feronn,  ferann  (*uerono-)  ,Land, Acker'  (wohl  ,*umhegt*);  mcymr.  gwerthyr  ,Festung'  (^üertro-]  vgl.  oben ai.  vartra-);  hierher  wohl  air.  J^riu,  Gen.  Erenrij  cymr.  Iwerddon  ,Irland' als  *epi-ueriö,  Gen.  -ionos  , Hügel,  Insel'  (vgl.  ahd.  icerid)  nach  Pokorny KZ.  47, "233,  ZcP.  15,  197 ff.;
POK_01.txt:760:gr.  ägaglayicü,  Perf.  llgäga  ;,füge  zusammen'^,  Ugiisvog  ^angefügt^  passend'^ 'oag  ^Gattin'   (wohl  nach  Brugmann  IF.  2'S,  293,    Schwyzer  Gr.  Gr.  I  434 hierher  mit  Präf.  *o-,  kaum  zur  Wz.  *ser-  oder  Wz.  *?^er-,  d-J^eigo))]   dazu öagl^ü)  ^liabe  vertrauten  Umgang'^;  auch  ^plaudere  vertraulich';  x^^'^^'^Q^^S ;,erzgefügt,   gepanzei't',   auch  xsQi-dgag   Ti%Vü)v   Pind.,   ^g-d-gov  , Glied,  Ge-  < lenk',  ägd-^ög  , Verbindung,  Freundschaft',  icgd-fiiog  ,vereint';  mit  ^-Suffixen  • homer.  dafi-or^-r- , Hausfrau'  (,die  des  Hauses  Waltende'),  äol.  doixogvLq  Hes. ;  ' Ttvlccgvrjg  , Hades  als  Verschließer  des  Unterweltstores'  (Schwyzer  Gr.  Gr. I  451,  5);    äge-   in  ägsaxco   ,gleiche   aus,    mache   gut,   befriedige',   dg€(Ty,EL IXOL  ,es  paßt,  gefällt  mir',  ägsaKsad-ccL,  dgsaaaa&ca  ,sich  verständigen,  einig werden  mit  jemandem;    sich  geneigt   machen,  versöhnen',   ägerrj  ,Tüchtig- keit',    dgsujüv  ,besser'  (in   Beziehung   steht  wohl  dgi-  ,sehr'  in   Kompositis, womit   Reuter  KZ.  31,  594  a  1  auch   ai.  ari-gürtd-,  -stutd-    als   ,eifrig  ge- priesen' vergleichen    möchte;    unsicher    wegen    gr.  igt-  ,sehr'   s.   Boisacq s.v.,  oben  S.  24  Anra.);  Icgiazog  ,besser,  best',  dgiGTsgög  ,links'.
POK_02.txt:1498:gherdh-  und  gherdh-  ,umfasseii,  umzäunen,  umgürten',  wegen  lat.  hortut^^ rs.  4.  qher-)  Erweiterung  von  4.  *gher-  ,fassen';  ghordho-s  ,Gehege<.-&
POK_02.txt:1504:got.  Ugairdan  ,umgürten',  aisl.  gyrda^  ags.  gyrdan,  afries.  gerda,  ahd. gurten  ds. ;  got.  gairda  L,  aisl.  gJQrd:  ,Gürtel',  ablaut.  aisl.  gyrdell,  ags. gyrdel,  afries.  gerdel,  ahd.  gurtil{a)  ds.  (mhd.  ^wr^  ist  nomen  postverbale) ; got.  gards*m.  ,Haus',  aisl.  gai^dr  m.  ,Zaun,  Gehege,  Hof,  Gehöft',  ags. geardy  as.  gard  , eingefriedetes  Grundstück',  Plur.  ,Wohnung',  ahd.  gart m.  ,Kreis'  in  mittügart  ,orbis',  heimgart  ,forum'  usw. ;  got.  garda  ,Hürde, Viehhof,  afries.  garda  , Garten',  as.  gardo,  ahd.  garto  ds.  (oder  aus  idg. *ghor-tö-]  vgl.  x<5^rog  unter  4.  gher-);
enn die  Göttin  eig.  ,die  jugendliche'  bedeutet,  ist  von  dem  in  jünix,  junior vorliegenden  St.  iün-  abgeleitet;  anders  Leumann-Stolz ^  239.
WP.  I  200  f.,  WH.  I  735  f.
^.  ieu-  ^trennen,  fernhalten',  s.  oben  S.  508 ;  nach  Renou  (mündl.)  ist  die ai.  Wz.  yu-  _,trenn
```


## [2026-10-17T00:31:02.812Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 -c \"\nt=open('POK_02.txt',errors='ignore').read().split('\\f')\nfor i in (169,170,171):print('=====LEAF',i);print(t[i][:6000])\""
}
```


### [2026-10-17T00:31:03.154Z] TOOL RESULT

```
=====LEAF 169
enn die  Göttin  eig.  ,die  jugendliche'  bedeutet,  ist  von  dem  in  jünix,  junior vorliegenden  St.  iün-  abgeleitet;  anders  Leumann-Stolz ^  239.
WP.  I  200  f.,  WH.  I  735  f.
^.  ieu-  ^trennen,  fernhalten',  s.  oben  S.  508 ;  nach  Renou  (mündl.)  ist  die ai.  Wz.  yu-  _,trennen'  mit  yu-  ^verbinden'  identisch  und  jene  Bedeutung aus  dem  Kompositis  mit  dpa-  und  vi-  übernommen.
ieu-dh-  ,m  heftiger  Bewegung  sein,  kämpfen';  ioudho-  , Erregung'.
Ai.  ud-yödhati  ,wallt  auf  (vom  Wasser) ;  fährt  zornig  auf,  Kaus.  yödhd- yati  , verwickelt  in  Kampf,  yndhyati,  yödhati  , kämpft',  yüdh-  m.  ,Kämpfer', f.  ,Kampf,  Schlacht',  yudhmd-h  ,kriegerisch',  m.  , Kämpfer',  yödhlyas-  ,streit- barer,  besser  kämpfend';  Päli  yuhati  ,kämpft';
av.  yüidyeinti  ,sie  kämpfen',  yüidiHa-  ,der  am  besten  kämpft';
gr.  hom.  va(uvL  Dat.,  vo^ivr]  , Treffen,  Schlacht,  Kampfgetümmel'  (*iudh-s- mln-,  Ableitung  von  einem  *iudh-s-m6-Sj  vgl.  ai.  yudhmd-h))
lat.  jubeö,  -ere  (=  lit.  judeti),  jussl  (alt  iousl),  jussum  eig.  ,*in  Bewegung setzen,  aufrütteln',  daher  ,jemanden  etwas  heißen,  befehlen';  juha  f. , Mähne' (,*die  sich  schüttelnde,  wallende') ;  (über  juhar,  -äris  ,Morgenstern,  strah- lendes Licht'  siehe  WH.  I  724) ;
acymr.  acorn.  abret.  Jud-  ,Kampf  (^ioudho-),  , Kämpfer'  (*ioudhios),  in MN  wie  acymr.  Jud-gual,  abret.  lud-uual  , Kampf-gewaltiger';  dieses  Jud- (=  iud-)  wird  später  im  Anlaut  mehrsilbiger  Namen  mcymr.  zu  Id-  (=  id-), in  allen  anderen  Stellungen  zu  ud  (=  üd),  so  acymr.  Mor-iud  , Meeres- kämpfer'  zu  mcymr.   Mor-ud,   selbständig   cymr.   udd  ,Herr'   (*ioudhios);
lit.  judilj  -Ui  ,sich  bebend,  zitternd  bewegen,  zanken',  jundü  jüsti  ,in zitternde  Bewegung,  in  Aufruhr  geraten',  alit.  judüs  ,zanksüchtig',  judra ^Wirbelwind' ;
ablautend  lit.  jaudä  f.  , Verlockung,  Verführung',  wovon  jdudinti  ,je- mands  Leidenschaft  erwecken,  jemanden  verführen',  refl.  ,aufgeregt  sein, sich  erregen',  lett.  jauda  , Vermögen,  Kraft',  jaudät  ,die  nötige  Kraft  haben' ;
poln.  judzic  ,zu  etwas  Bösem  bereden,  reizen,  aufwiegeln'  (:  ai.  yödhd- yati) ;  vielleicht  aksl.  ojhmim,  PI.  opmi  , Krieger'  (=  ai.  yudhmd-h  mit Präfix  0-) ;  auch  bulg.  juda  ,Nymphe' ;
512  •
toch.  A  yutk-  ^"besorgt  sein^
WP.  I  203  f.,  WH.  I  724  f.,  Trautmann  109.
ieug-  ^aufregen,  unruhig^
Av.  yaozaiti  ,regt  sich  auf  (vom  Wasser,  ,  von  unruhigen  Ländern)', yaöHi-  ,Rührigkeit,  Regsamkeit';
arm.  yuzem  ,rege  auf'  ist  iran.  Lw. ;
got.  ßuka  ,Zorn, 
=====LEAF 170
 Streit',  jiukan  ,kämpfen',  mhd.  jouchen,  jauchen  ^treiben, jagen'  und  ags.  geocor  ,full  of  hardship',  geocre  Adv.  ,streng';
toch.  A  yok-,  AB  yuk-  ,besiegen'.
WP.  I  203,  Feist  301  b.
ieu-ni-  oder  iou-ni-  etwa  ^angewiesene  Stätte,  richtiger  Weg'.
Ai.  yöni-  m.  ,Aufenthaltsort',  f.  ,Mutterleib',  av.  Akk.  Sg.  yaondm  »Weg*^ (wohl  aus  yaonim,  siehe  Wackernagel  KZ.  46,  266);  dazu  ai.  syond-  ,b( haglich'  aus  *su-yond-,  Wackernagel  KZ.  61,  203 f.;
air.  uain  f.  , Gelegenheit  (d.  i.  richtiger  Platz  =  richtige   Zeit),  Mußj Zeit'.
WP.  I  204;  wohl  zu  1.  ieu-  ,in  Bewegung  setzen'.
ieuo-  , Getreide',  vor  allem  , Gerste'.
Ai.  ydva-  m.  ,Getreide;  Gerste,  Hirse'  =  av.  yava-  m.  ,Getreide','^ npers.  jav  , Gerste'  (==  lii.javat)'^  ai.  yavya-  m.  ,Fruchtvorrat'  (:  lit.  ^a«;aj ,Scheune');  yavasd-  n.  ,Gras,  Futter',  av.  yavaidha-  n.  ,Weide';  av.  ydVlriA m.  , Getreidefeld' ;
hom.   att.  leial  f.  PL  , Spelt',   hom.    ^sldcuQog  ,Getreide   hervorbringend' (für   *^eJ^6Sü}Qog)^    q)vaL-^oog   (ala)   , Getreide   hervorbringend'   (:  ieuo-s s^-g)Q(i)v :  cpQifjv) ;
lit.  jävas  m.  , Getreideart',  java%  PL  , Getreide',  jduja  , Scheune'.
WP.  I  202  f.,  Trautmann  107.
ie^os-  etwa  ,Satzung,  Fug' ;  vielleicht  als  ,Verbindlichkeit'  zu  2.  *jet<-  ,ver- binden'.
Ai.  yöh  n.  ,Heil!'  (nur  in  Verbindung  mit  ^dm-^  zur  Form  s.  Bartholomae Airan.  Wb.  1234) ;  av.  yaoHa-däiti  ,macht  hell,  reinigt  rituell' ;
lat.  iüs  ,Satzung,  Verordnung,  Recht'  (alat.  ious  aus  *iouos,  vgl. :)  iüstm (alat.  iovestöd)  ,gerecht' ;  jürö,  -äre  ,schwören'  (alat.  wohl  in  iouesat  Duenos- Inschr.),  über  jürgö,  iniüria]  pe(r)ierarej  ejeräre^  deieräre  (tief stufiges iüsä-)  s.  WH.  I  732 ff.,  EM.2  506 ff.;  über  judex  ,Richter'  s.  oben  S.  188, WH.  1726;
air.  huisse  ,gerecht'  (*ius-t{o8).
WP.  I  203,  WH.  I  733  f.,  870.
513
io-  Relativstamm,  s.  oben  S.  283.
ioi-ni-  ,Binse^
Lat.  iuncus  ^Binse*^  (*ioini-ko-s)  gehört  zu  mir.  ain  ^Binse^  {*ioini-), Gen.  aine]  über  lat.  iüniperus  ^Wacholderstrauch'  s.  WH.  I  731,  870 und  Leumann  Gl.  27,  74;
aisl.  einiTj  schwed.  en  ,Wacholder^,  ndd.  en(e)ke  ds.  falls  aus  *jainia-, ■wodurch  der  Bedeutungs Wechsel  Binse :  Wacholder  (s.  oben)  als  alt  ge- sichert würde.  Doch  ist  dann  bei  mnd.  eynJiolz  und  nhd.  Einheerhaum (aus  aisl.  eini-ber  , Wacholderbeere')  Ei
=====LEAF 171
nfluß  von  ein  ,ein^  anzunehmen.
WP.  I  208  f.,    Kluge  11  126.
iofk-  _,Tier  aus  der  Gruppe  der  Rehe^
Gr.  ^OQ^j  ^OQy.ag,  mit  volksetym.  Anschluß  an  dsQxofxai  meist  ööq^,  öogy^ög-, dogycdg  f.,  dÖQy.og  m.  ,Reh,  Gazelle^;
gallo-rom.  *iorkos  ,Reh',  cjmr.  iwrch  ,caprea  mas',  corn.  yorch,  bret. iourc'h  ,Reh'  (vermutlich  aus  dem  Keltischen  stammen  die  späteren  ver- einzelten Formen  tb^xog,  io^xsg,  Yvoxeg  bei  Opp.  und  Hes.);  gall.  FN  Jurca.
WP.  I  209;  M.-L.  9678.
iou,  iu  .schon'^,  s.  oben  S.  285.
iö[u]s-  :  iüs-,  (vermutlich  zu  2.  ieu-)  , gürten^;  iös-to-s  ,gegürtet^,  iös-men- n.  ,Gurt'.
Av.  yäti^hayeiti  (meist  mit  aiwi-)  ,gürtet^,  Partiz.  yästa-  ,gegürtet^,  yäh n.  ;Gürtelschnur^;
gr.  tibwvixi  ,gürte',Xf^(TT6g  (=  av.  yästa-,  lit.  jüostas)  , gegürtet',  CcüOtt^q ,,GürteP,  ^ü)^a  ds.  (^toja-^a  vgl.  lit.  juosmud  ,Gurt'),  ^cowj  ds.  (%a)a-vä, vgl.  russ.-ksL poj asm  ds.);  ^ovad-o)'  Liawvad-u  Hes.  etwa  thessal.  =  ^cbaS-o)?
alb.  n-gjehs  ,ich  gürte';
lit.  jüosiu,  jüosti  .gürten',  jüostas  ,gegürtet',  jüosta  , Gürtel'  neben  pa- jüseti  ,gürten'  (Ablaut  öw.ü)]
a^Lsl.  pojaiQy  -jasati  ,gürten',  'pojasT>  , Gürtel'  (usw.,  siehe  Berneker  449).
WP.  I  209,  Schwyzer  Gr.  Gr.  I  330,  Trautmann  108  f.
I.  iu-   ,ihr'  ursprüngl.  nur  Nom. ;    Kasus   obliqui  vom  St.  "es-,    u6s-   (aus *iues.  *iuos?). 1.  Ai.  yuvdm  ,ihr'  Du.,  yüydm  PL,  av.  yv^rrij  gathav.  yüs\ arm.  nachwirkend  in  den  mit  je-  anlaut.  Kasus  z.  B.  Dat.  jez  (e  nach mez  ,nobis',  liez  ,tibi');
got.  jus  ,ihr'  PL,  sonst  nach  ,wir'  (s.  ue-)  umgebildet  aisl.  er,  ags.  gEj as.  g%j  ge,  ahd.  ir]  Du.  got.  *ju-t  (:  lit.  jii-du),  sonst  nach  ,wir'  umgebildet aisl.  itj  ags.  as.  git)
33
514  ,
litjüSj  lett.  jus,  pr.  ioüs,  iaüs  ,\hr'  PL,  \\t.  ju-du  ,ihr  beide';  apr.  iouson^ lit.  jiisij(>,  lett.  jusu  ,euer^ ues-,  u^S'i    ai.  vah,  av.  vä  enkl.  für  Akk.  Gen.   Dat.  PL,   Dual   ai.  väm- vom^Akk.   *us-sme  (=  lesb.  {/^u^tfi)   aus   mit   Übernalime    des   nominativi- sehen  i-  ai.  yusmän  Akk.  (usw.),  av.  Abi.  yü§mat-
gr.  lesb.  if^u/i«  (*ms-sw-),  dor.  ifis  Akk.,  daraus  nom.  lesb.  i'^^eg,  dor. ^^<fg,  sowie  att.  i^etg  usw.;
alb.  ^'w  ,ihr'  aus  *u  ==  ai.  vah  mit  hiatustilgendem  ^■- ;
lat.  vös  (=  av.  Akk.  PL  vä?),  pälign.  vus  ,vos'  und  ,vobis^,  la
```


## [2026-10-17T00:31:10.763Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'EOF'\nimport re\ndef pages(f): return open(f,errors='ignore').read().split('\\f')\nh=pages('HRN.txt'); \nfor i in (113,114,197,198):\n    t=h[i]\n    for m in re.finditer(r'(?i)ǰām|jäm|gäm|jam|yäh|yāh|sum|šum|xšm|isma',t):\n        print('HRN leaf',i,':',t[max(0,m.start()-300):m.start()+500].replace('\\n',' ')); print('--'); break\nu=pages('HUB.txt')\nfor i in (58,59,60):\n    t=u[i]\n    for m in re.finditer(r'(?i)jäma|jāma|ǰāma|yäh|yāh|gäma',t):\n        print('HUB leaf',i,':',t[max(0,m.start()-400):m.start()+700].replace('\\n',' '));print('--');break\nEOF"
}
```


### [2026-10-17T00:31:11.146Z] TOOL RESULT

```
HRN leaf 113 : soll vielleicht tey sein. Np. tey 'Berggipfel, Höhe', oss. fty, d. feyä 'Bergrücken (250) gehören ebenfalls hierher (spezialisirte Bedeutung: Spitze eines Berges). J. 410. JädU 'Zauberer, Jadül. aw. j/ätu- 'Zauberer'; i^hlw. jatuk, jatükih, arm. LW. jatuk; ai. yätü- 'Spuk, Hexerei; Spukdämon'. 411. Jäm 'Glas, Becher'. aw. yama- 'Glas' ; phlv. jatn bezw. yäm (auch für aw. gao.zasta-, vd. 3 (4)). Reimt auf /er« fSahn. I, 22 Vers 35), /ere^gr* (Sahn. I, 78 Vers 307). Mit aw. ^afra- (Justi; auch noch Geiger, ZDMG. 37, 130) hat np. tere nichts zu tun, vergl. Bartholomae, KZ. 29, 287. -) Das s statt z ist von np. tes (No. 387) bezogen. *) Bartholomae, Altiran. Verbum 105; zur Form vergl. Studien II, 107, 180.
--
HRN leaf 114 : — 93 — 412. jäme 'Kleid, Gewand'. ai. V^yam- mit chardis- etc. *ein Dach, einen Schirm, Schutz überhalten , lett. ju^m-f *dachdecken*, ksl. /)o- jata 'Dach' (Fick); phlv. jämak bezw. yamak (z. B. vd. 6 (71) Gl.)i). kurd. yüma 'grobes baumwollenes Zeug (H,-Sch.); LW. afy. jama, bei. jfämag (113). Hörn, KZ. 32, 583 No. 11. 413. Jan 'Leben, Seele', Janver. aw. daenä' 'Seele, zu [/'dliay-, dhyO- (oder nach Bartholomae, ZDM6. 43, 665 dhai-) „'sehen' im geistigen Sinn, subjektiv die Erkenntniss als psy- chischer 
--
HRN leaf 197 : — 176 — 790. suma 'ihr. aw. ynsmäka-, gä»*^. /smäka- euer; päz. suma; ai. yuämdka-; arm. yer 'euer (H. No. 176). oss. d. sinaxy t. suma/ ihr, euch' (225); bei. savä- "\\\v\ saraiy 'euer (365). 791. stifnar *Zahl, Anzahl', summden (mit her- erzählen*). g. simärtmün; Kä§. V. veresmörtdn , Q. öresmärdeff^ K. esmördemün, Z. veresmdrt^), aw. I/"r/?ar-, märay^iti 'bemerken, sieh merken* (y. 32, 6); phlv. sVmär (vd. 9 (132) Gl.), vergl. ösmartan^ ösmar (Bund.), anösmär 'ungezählt' (Men. 49, 22); ai. {^smar- gedenke
--
```


## [2026-10-17T00:31:15.605Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'EOF'\nimport re\ndef pages(f): return open(f,errors='ignore').read().split('\\f')\nu=pages('HUB.txt')\nfor i in range(55,63):\n    t=u[i]\n    for m in re.finditer(r'(?i)jäm|jām|ǰām|yäh|yāh|412',t):\n        print('HUB leaf',i,':',t[max(0,m.start()-300):m.start()+600].replace('\\n',' '));print('--')\nEOF"
}
```


### [2026-10-17T00:31:16.153Z] TOOL RESULT

```
HUB leaf 59 : lossen, dass das altpersische * Tlru des 5. Jhd. a. Chr. aus tistrya- entstanden ist. 408. Bal. te» ist LW. 409. Zu np. tey *Spitze, Schwert, Klinge, arm. LW. tSg 'Spitze der Lanze, Lanze', afgh. LW. tBy a sword' etc. gehSrt auch np. tSya 'lamina', modern t%yd * Klinge' (Rosen, Sprachfuhrer p. 55). 412. Fr. Mil Her vergleicht besser n^. Jama 'Kleid' aus phi. yamak = ap. ^yohma" mit gr. '(^vi^a, WZKM. 8, 93. 413. Zd. da^a- kann nicht gleichzeitig = np. jdn und = np. din (Nr. 597) sein. Ich setze Jdn *Seele' = skr. dhydna- *Nachsinnen. Justi und Fr. M tiller ver- kniipfen jdn mit zd. gay a- Xeben', was lautlich un- zulassig ist. Kurd, gdn bei Rhea und im Dialekt von Sivend (Journ. asiat. 1893, p. 248) ist schwerlich urspriinglich. 415. Bartholomae's Bemerkungen sind verfehlt. Np. Jdvldan *kauen etc. gehSrt zur idg. Wurzel giv, gyu^\ die in ksl. zHvati *kauen', deutsch kaum (vgl. K 1 u g e 
--
```


## [2026-10-17T00:31:23.188Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'jāmag\\|jamag\\|yʾmk\\|jāmak\\b' PHD.txt PHD_mackenzie.txt | head; grep -n -i 'jāmak\\|yāmak\\|jamak' NYB_vol2_glossary.txt | head; grep -n -i 'yāh-\\|yāh \\|yāsta\\|yåŋh\\|yāŋh' BRT.txt | head -20"
}
```


### [2026-10-17T00:31:23.608Z] TOOL RESULT

```
PHD.txt:252:bāmdād [6’md’t' | М bmd?d, N ~] dawn, morning. bāmīģ [P myk!] brilliant, glorious. -bān [-??s! | M Aa, N ~] suffix, -keeper, -guard. band [bnd | = Р, N ~] bond, link. band-, v. bastan. bandag [bndk! | P bndg, N ~a] servant. bang [bng | N ~] henbane. bānūg [Pnwk! | N Бапи) lady. bar [b] | N ~] fruit, produce, profit. bar-, —išn, v. burdan. ībār [Pl | N ~] time, occasion. *bār [P1 | N ~] bank, shore. заг [D] | M P?r, N ~] fruit. ‘bar [b] | M br, N ~] load, burden; duty. bāraģ [5/А! | N ~a] mount, horse. barbut [blbwt! | N ~] lyre. bārestān [b/st?n'] patient, resigned. ~ih: patience, resignation. barig/k [b’lyk' | N bārīk (cf. tārīg)) thin, fine, subtle. bar-jamag [bly mk! | N ~a] saddle-bag. barómand [b wmnd | N ~] fruitful, prolific. barsom [blswm | M brswm] the bunch of twigs used in the Yasna cere- mony. baršnūm [b/s2wm] the major purification ritual. bastan, band- [ASLWN-tn! < A Vier bstn', bnd- | M bstn, (bn-), P bnd-, N ~] tie, bind. bāstān [b’st?n' | M PysPn, N ~] always, often. bas [YHWWNS | M P, N ~] be! (imperative of büdan, q.v.) baSkué [bskwe] gryphon. bašn [bén' | = P] top, peak; stature; mane (v. buš). baw-, —i$n, v. büdan. baxš-, —išn, v. baxtan. baxt [b()At! | N ~] fortune, fate. baxtan, baxš- [HLKWN-tn! < А У hig; bC)htn', bhf- | M bxt, bx$-, N baxsidan] apportion, distribute. ~išn: bestowal, distribution. bay [ORHY A < A */h; bk', bg | M by] god, lord. im ~: his Majesty. бу ~: his late Majesty. bayaspān [by’sp’n'] messenger, envoy.
PHD.txt:1256:clothing jamag, paymog, wastar(ag).
PHD.txt:3496:saddle-bag barjamag.
PHD.txt:5552:daxmag, 1-2 jamag
PHD_mackenzie.txt:6207:clothing Jamag, paymog, wastar(ag).        (u)spurrig.
PHD_mackenzie.txt:11257:barJamag
1205:dast [YDH, Prth YD’; dst'], with the indef. art. dast-ē [YDH + 1] 1. hand HajA:11.14. B:12.16. 9% and passim; power 1924, 24%. 304; — ~~ apar nihātan to put one's hand to 6215; — ~ avis burtan to deal with a th. 8119-29; — frac ~ Sustan to wash one’s hands 443-9, with hac to dissociate oneself from, to break off all relations with 384; — a ~ 4... rasitan to come to close quarters with a p. 24?, — pat ~ daštan to have a hold on, to hold sway over 87%, — 2. ~ i yāmak a set of clothes 2; FrP 29. — 3. game: 3 ~ hae ... burt he won three games (of chess) against... 11915; ~ 4 vat vāzītan
```


## [2026-10-17T00:31:27.987Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'jāmag\\|Jāmag\\|jamag \\[' PHD.txt | head -5; grep -n -o '.\\{0,10\\}jāmag.\\{0,120\\}' PHD.txt | head -5; grep -n -o '.\\{0,5\\}yāmak.\\{0,200\\}' NYB_vol2_glossary.txt | head -5; grep -n -o '.\\{0,20\\}gürt.\\{0,200\\}' BRT.txt | head -10"
}
```


### [2026-10-17T00:31:30.590Z] TOOL RESULT

```
252:bāmdād [6’md’t' | М bmd?d, N ~] dawn, morning. bāmīģ [P myk!] brilliant, glorious. -bān [-??s! | M Aa, N ~] suffix, -keeper, -guard. band [bnd | = Р, N ~] bond, link. band-, v. bastan. bandag [bndk! | P bndg, N ~a] servant. bang [bng | N ~] henbane. bānūg [Pnwk! | N Бапи) lady. bar [b] | N ~] fruit, produce, profit. bar-, —išn, v. burdan. ībār [Pl | N ~] time, occasion. *bār [P1 | N ~] bank, shore. заг [D] | M P?r, N ~] fruit. ‘bar [b] | M br, N ~] load, burden; duty. bāraģ [5/А! | N ~a] mount, horse. barbut [blbwt! | N ~] lyre. bārestān [b/st?n'] patient, resigned. ~ih: patience, resignation. barig/k [b’lyk' | N bārīk (cf. tārīg)) thin, fine, subtle. bar-jamag [bly mk! | N ~a] saddle-bag. barómand [b wmnd | N ~] fruitful, prolific. barsom [blswm | M brswm] the bunch of twigs used in the Yasna cere- mony. baršnūm [b/s2wm] the major purification ritual. bastan, band- [ASLWN-tn! < A Vier bstn', bnd- | M bstn, (bn-), P bnd-, N ~] tie, bind. bāstān [b’st?n' | M PysPn, N ~] always, often. bas [YHWWNS | M P, N ~] be! (imperative of büdan, q.v.) baSkué [bskwe] gryphon. bašn [bén' | = P] top, peak; stature; mane (v. buš). baw-, —i$n, v. büdan. baxš-, —išn, v. baxtan. baxt [b()At! | N ~] fortune, fate. baxtan, baxš- [HLKWN-tn! < А У hig; bC)htn', bhf- | M bxt, bx$-, N baxsidan] apportion, distribute. ~išn: bestowal, distribution. bay [ORHY A < A */h; bk', bg | M by] god, lord. im ~: his Majesty. бу ~: his late Majesty. bayaspān [by’sp’n'] messenger, envoy.
1205: ~ i yāmak a set of clothes 2; FrP 29. — 3. game: 3 ~ hae ... burt he won three games (of chess) against... 11915; ~ 4 vat vāzītan
3814:  'gar:  —  ai.  aöMgürtay-  f.  —  Pü. : apar girisni&,(zu'Vi.):  apar  raäsniA'). —  ')  Statt IS.,  S  318.  4.  —  ')  Vgl,  zu  aibigat-,  aibijariiar. und  lu  jaritay-.
4310:t  der  Religion  umgürtet  zu sein"  V. /<V. r ".        [N.()6':  X\t%  anaiwyästi^
17211:{fem.  'ta-) 'hochgegürtet':  sraohm  .  .  yo  bsrizS  "tö Y.57. 30;  —  frava^ayS  .  .  yä  banzaitrl °ia  Yty.  39.
21691:m.  'ya-)  'mit umgegürtetem  Waffeneerät,  Gewaffen';  /ra- vaiayS  .  .  pouru.spS%ä  °yh  Yty,  37.
21697:•  j.  'yäh-  V.  'gürten'.  Praes.  24  ya»- Äaya-'\  —■  PPfP.  yosia-.
21698:'umgürten,  (sich)  den  Gürtel  umlegen': kainxns..  uskät  yastays  "eines  Mädchens ..  eines  hochgegUrteten"  Ytj,  64;  — vayus  aurvS  *usiat  *y3stll  YtJf.  54.
21704:\M.po-yaiaye&  'er  gürtet'!  liL/iuiu 'kli  gBrt< gr.  liiarn^,  - —  Pfi. :  aivjyähariUan  7),  anvyähan  7} dällatii  aänyäiin,  pa  ahvyäianismi?);  s.  nocli No.  4,  6.  —  >)  Vgl.  Bthl.  Stud.  2.  104,  loS, 110.
```


## [2026-10-17T00:31:36.224Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 21690,21720p BRT.txt; grep -n 'jāmag \\[' PHD.txt PHD_mackenzie.txt; grep -n -o 'jāmag[^.]\\{0,80\\}' PHD.txt PHD_mackenzie.txt|head; grep -n -o '.\\{0,30\\}šumā\\{0,1\\} \\[.\\{0,100\\}' PHD.txt | head -3; grep -n -o '.\\{0,10\\}šumā.\\{0,120\\}' NYB_vol2_glossary.txt | head -3"
}
```


### [2026-10-17T00:31:38.913Z] TOOL RESULT

```
0  So  Mf  3;  NA.  mit  F  I  yaslöMiätij  (was  ich nicht  Tcntehe ;  yasta-  könnte  nur  ai.  yatla- sein);  vgl.  V.  14.  9  tainäu!  mit  den  Var.  und *yäsßjaya:
•  j.  *y^*ö.zaya-"  Adj.  (fem.  'ya-)  'mit umgegürtetem  Waffeneerät,  Gewaffen';  /ra- vaiayS  .  .  pouru.spS%ä  °yh  Yty,  37.
■)  So  Jio,  vgl.  aach  Mf3.  NA.  mit  Fi yastä' ;  ».  das  Torherg.  Wort.
•  g.  yä.Syao*ana-  Adj.  'welche  Taten verrichtend,  wie  handelnd' :  ya%a  kvd  . . %w3vqs  (sd.)  , .  af?hat  -nasiä  Y.jj,  16.
Pü.:  pa  kunün.
•  \.  yä.äyao8«nä-  fem.  Adj.  'die  Worte ya  syao%ana  enthaltend,  damit  beginnend': 'na  Ääiti/{sd.y'>  Y.34  Überschr.;  —  •nqm haitim  yazamaide  Y.34. 16.
■)  D.  i.  Y,  34-
•  j.  'yäh-  V.  'gürten'.  Praes.  24  ya»- Äaya-'\  —■  PPfP.  yosia-.
'umgürten,  (sich)  den  Gürtel  umlegen': kainxns..  uskät  yastays  "eines  Mädchens ..  eines  hochgegUrteten"  Ytj,  64;  — vayus  aurvS  *usiat  *y3stll  YtJf.  54.
mit  aiwi  i)  'etwas  sich  umtun,  anlegen, anziehen'  (den  Gürtel,  Kleidungsstücke): aiwyäahantm  va  aiwyanhayamnS  aiw- yäffhamm  vS  ia/ayamnä (sd.)  Yt  i.  i  ?;  — ya  hama  *aiwyär9Aana  (sd.)  aiwyanha- .yänti  N.g4;  —  aat  aiähe  (näml.  aiwyata- hanahe)  ahi  aiwyUstS  *banlnuS  paiH  . . Y.  p.  26;  —  aiwi  vastra  yäwAayanuha "zieh  deine  Kleider  an"  V.iS.iq;  — ,  vastra  .  .  aiwyänhayaäa  V.p.  32;  —  yS vastra  vastrim  *aiwyarfhaya7iti^'>  N.55(?);
\aiwyast3m'^'^  dadarayS {sd.)  ^.g6;*g6^; —  i^at)  *na  *nii>ma  »urfraA« (sd.)  aiw- \yasts  ratufris  N.SS;  8-]*;  —  yS  aiwya- rakayaite  karatSsca  . .  pasca  ''aiwyästtm ]^mtao^ayäti  N.Ä^;  55.  a)  'die  Gürtel-
schnui  umbinden,  umlegen':  iva  i^ra aiwyitthayänte  atairi  iasatibya  cvat  am- xyhTskayinti  "wo  sollen  sie  hier  die  Gürtel I  schnür  anlegen?  Unterhalb  der  Achsel- höhlen. In  welcher  Grösse  sollen  sie  si- I  anlegen?"  N.iSj;  —  aiwyasta^^  maidas •^yasna  gli^ä  srävayaf  «Sil  anaiwyOsta  (sd.) 'N.(?5;  —  ya%a  ia%aca  dakmd  staota ,yesf>ya  haurva  dahäiti  .  .  barymns  v3 vaz?mnS  va  aiwyastS  a%a  raA(/"nT  "wie
dby  Google
immer  ein  D.  .  .  sei  es  reitend,  sei  es fahrend:  weon  er  nur  die  Gürtelschnur umhat,  BO  ist  er  r"  N.^7.  a)  von  der BUndduDg  der  SarTtManzweige:  iatvsma alaya  frastanttm  aiaya  aiwjäst>m  an- abäättm  (sd.)  "das  B.  . .  das  vorschrifts- massig  gebündelte"  Vytsj;  —  *%rig!i- mim  aiwyästat  kaca  *har?smm  parüiH
\M.po-yaiaye&  'er  gürtet'!  liL/iuiu 'kli  gBrt< gr.  liiarn^,  - —  Pfi. :  aivjyähariUan  7),  anvyähan  7} dällatii  aänyäiin,  pa  ahvyäianismi?);  s.  nocli No.  4,  6.  —  >)  Vgl.  Bthl.  Stud.  2.  104,  loS, 110. —  ')  Hdt.  arwyittti. —  3)  Hds.  cäieyiah- yinti.  —  4)  Statt  mwyästm  (s.  auch  No.  5) Teilangte  man  einen  Infinitiv;  s.  FQ.: /a  onf- yähanihük.  —  i)  Hds.  ahnyäsltim.  —  *)  Pü.  erl.  [ hl  tularak  u  tuitik  Idärind,  womit  mehr  gesagt wird,  als  der  Text  bietet.  —  7)  Ttansskr.: IF.  II.  1*5.
•  j.  'yäh-  n.  'Gürtel,  Gürtelschnur":  ta\a ayao/ {sd.)  ya'^a  (Sp.  1348  m.)  paoinm vJrym  avi  yä  (NS.)  bavaiti dem  Mann  zuerst  der  Gürtel  zu  teil wird"  Yt  Ä  14.
Zum  V.  yäh:  —  VgL  aiivyir»lit
*  j-t  K-  ^äh-   n.    'Krise,   Entscheidung, Wendepunkt' " :  ya'ha  Ais  . .  yazata .
durch  ein  Traumgesicht  als  Zwülingspaar
offenbarten,  . ."  V.jo.  3*'
■)   Sacblichei  iSt  (.  Dk.  g.  30.  4  und  n
Pü.:  iiän/ratum  an  i,
iuiän   vinät  u  iarpak
duu  Bthl.  1F.  12.  113.
umji
;  •  j,  y»vin-''  m,  'Getreidefeld':   oipmacä '  yivXne  (AP.)  yasamaide  Y.42.2;  —  ßäo- nlm    vq'^wqm  .  .  *aipanä?a  y/vlnS  yasa- \  maiäe  S.  2. 7.
Ableit  «US  yaua-,  vgl  iBUd.  Ben.  GrGr.) 188  d.  —  Vgl.  j-awn»-.  —  Fi.i  htrtöi,  Sa.: äAänyam. —  ')  Am  ix.*iiii/m-;  vgL  Mfilijt bei  Ben.  Grdr.>  r.  1091.*
[  •  j.  yeiti  indekl.  Pron.  rel.  'wie  viele',  nur '  1  der  Verbindung  yeiii  catila  'so  oft  als, ,  immer  wenn"',  im  Nachsatz  folgt  at^t'^-. y  c*  ..  dakmB  alava  'Aaurvi  ratW  (sd.) ,  äahai  aiHi**  . .  2.32.
al  yM  Pron.  rel.  —  Pü.:  o.  —  1)  S.  ka-'O.-i,
—  »)  Ist  Sp.  69  f.  vergcsien,  s.  Ktr.
[  •  j.  yeli,  yeiJi  Konjn.:  s.  unter  yadiy.
2847: šumurdan šumār.
3653:; Paz. NP šumā.
7458:šumurdan šumār-: ošmurtan
```


## [2026-10-17T00:31:46.053Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o '.\\{0,5\\}j[āa]mag \\[.\\{0,80\\}' PHD.txt PHD_mackenzie.txt | head; grep -n -o '.\\{0,5\\}šumā \\[.\\{0,100\\}' PHD.txt PHD_mackenzie.txt | head -3; sed -n 3650,3655p NYB_vol2_glossary.txt | cut -c1-400; grep -n -o '.\\{0,40\\}yāhm.\\{0,40\\}\\|.\\{0,40\\}yähm.\\{0,40\\}' BRT.txt | head"
}
```


### [2026-10-17T00:31:48.916Z] TOOL RESULT

```
PHD.txt:252: bar-jamag [bly mk! | N ~a] saddle-bag. barómand [b wmnd | N ~] fruitful, prolific. barsom [
škoh [škwh] majesty, magnificence 1614. — Paz. škēh, Skr. v. samüha (in pl.) SGV I, 39; J-Prs škwh ‘magnificence’ (e. g. Isa. 210.19), [To be distinguished from an- other Skoh, MPrs ‘skwhyh ‘poverty’ (A— H II), OP skau8;- ‘poor’].
škuft [Skwpt'] strange, surprising 724; stupefied 11%, - MPrth ‘sky/t ‘wonderful, amazing, immense(ly), very’; NP šikijt ‘anything wonderful’, šikuft ‘a prodigy, magnificence’, šigift, Sıguft ‘wonder, aston- ishment’. The etymological relation be- tween skapta- and *skupta-, *skipta- is not clear, but their meanings cross.
škuiteh embarrassment 665,
šmah [LKWM] pers. pron. 2nd p. pl., cas. rect. and obl., you; your: 2 bdrak $ ~ 62° sq.; dānākān 1 ~ 11814; Vazurg- mihr 4 ~ 11922, — Av. (1304) yūšmāka-, xšmāka-; šmāh < OP *xšmāzam with -xa- for -ka- as in a^müxam, v. amäh; MPrs 'šm'(h); MPrth ‘mwh; Paz. NP šumā.
šnas [Sn’s] pres. st. of šnāxtan, in com- pounds: spās-šnāsān (pl. cas. obl.) those understanding service = having service as their profession 71!, v. späs.
šnāsak knowing, learned 213. šnāsēh knowledge 7119.
ugrep: error: error at position 159
\x80-\xbf]*){0,40}yähm(?:[^\n\x80-\xbf][\x80-\xbf]*){0,40}
                             exceeds complexity limits___/
```


## [2026-10-17T00:31:52.784Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o '.\\{0,3\\}[jJ]āmag.\\{0,80\\}' PHD.txt PHD_mackenzie.txt PHD_pages.txt | head; grep -n -o '.\\{0,3\\}šumā.\\{0,80\\}' PHD.txt | head -3; grep -c '' NYB_vol2_glossary.txt; grep -n -o '.\\{0,3\\}yāmak.\\{0,150\\}' NYB_vol2_glossary.txt | head -4"
}
```


### [2026-10-17T00:31:53.156Z] TOOL RESULT

```
221: N šumā] you (?1.). āšnāg Pwk! | M ”šYg, N ama] known. āšnawāģ [?$nw?k! | M ?snz?g, N š
523: N šumāra] calculation, reckoning.
7515
1205: i yāmak a set of clothes 2; FrP 29. — 3. game: 3 ~ hae ... burt he won three games (of chess) against... 11915; ~ 4 vat vāzītan
```


## [2026-10-17T00:32:04.661Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o '.\\{0,120\\}N šumā\\].\\{0,10\\}' PHD.txt; grep -n -o '.\\{0,10\\}[jJy][āa]m[ao][gk] \\[.\\{0,80\\}' PHD.txt NYB_vol2_glossary.txt | head; grep -n -o '.\\{0,60\\}N jām.\\{0,40\\}' PHD.txt | head"
}
```


### [2026-10-17T00:32:08.607Z] TOOL RESULT

```
221:reveal, confess. aškūb рор | N dškē(b)) roof, ceiling. aškom(b) [’skwm(b')] = a$kamb. ašmā [LKWM < А l-kwm | MO fm'(h), N šumā] you (?1.)
PHD.txt:252:btle. bar-jamag [bly mk! | N ~a] saddle-bag. barómand [b wmnd | N ~] fruitful, prolific. barsom [
ugrep: error: error at position 82
bf][\x80-\xbf]*){0,40}
                      \___exceeds complexity limits
```


## [2026-10-17T00:32:11.899Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o '.\\{0,40\\}\\[y.mk.\\{0,60\\}' PHD.txt | head; grep -n -o 'jām.\\{0,50\\}' PHD.txt | head; grep -n -o '.\\{0,200\\}a set of clothes' NYB_vol2_glossary.txt"
}
```


### [2026-10-17T00:32:16.195Z] TOOL RESULT

```
ugrep: error: error at position 111
[\x80-\xbf]*)mk(?:[^\n\x80-\xbf][\x80-\xbf]*){0,60}
                      exceeds complexity limits___/


351:jām)] end, conclusion.
394:jām- [hnc’tn', hnm- | P hnj ft, hnjm-, (M hnzpt, N an
394:jāmīdan)] finish, complete, carry out. hanjām [kne m 
412:jām [y m | N ~] glass. јат [M ANE < A mn-h; ут | M Pm
412:jām. атар [y mk! | М ртр, N fama] clothing, garment. 
422:jām [-hnc’m] gaining one’s end, successful. -~-hanjam
1308:jām.
1761:jām, karan, Sar; come to an — 6 ham madan; v. finish;
2116:jām(ag), paygal.
3010:jām.
1205:ac to dissociate oneself from, to break off all relations with 384; — a ~ 4... rasitan to come to close quarters with a p. 24?, — pat ~ daštan to have a hold on, to hold sway over 87%, — 2. ~ i yāmak a set of clothes
3703:129-19; the vb. in opt.: framüt ku ~ dast à yamak ... avis üvurt he [HWH-d] that a set of clothes
```


## [2026-10-17T00:32:22.462Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'EOF'\nimport re\ndef pages(f): return open(f,errors='ignore').read().split('\\f')\ns=pages('SYN.txt')\nfor i in (457,458,459):\n    t=s[i]\n    for m in re.finditer(r'(?i)yāh|jāma|ζώνη|zōnē|GIRDLE|BELT',t):\n        print('SYN leaf',i,':',t[max(0,m.start()-200):m.start()+700].replace('\\n',' '));print('--')\nEOF"
}
```


### [2026-10-17T00:32:23.008Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:32:25.568Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -o '.\\{0,200\\}GIRDLE.\\{0,300\\}' SYN.txt | head -5; grep -n -o '.\\{0,200\\}jāma.\\{0,200\\}' SYN.txt | head"
}
```


### [2026-10-17T00:32:31.447Z] TOOL RESULT

```
ugrep: error: error at position 85
\xbf][\x80-\xbf]*){0,300}
                         \___exceeds complexity limits


ugrep: error: error at position 83
bf][\x80-\xbf]*){0,200}
                       \___exceeds complexity limits
```


## [2026-10-17T00:32:38.128Z] TOOL CALL #23: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/s568.py <<'EOF'\nimport re,sys\nf=sys.argv[1]; pat=sys.argv[2]; w=int(sys.argv[3]) if len(sys.argv)>3 else 250; mx=int(sys.argv[4]) if len(sys.argv)>4 else 6\nt=open(f,errors='ignore').read()\nn=0\nfor m in re.finditer(pat,t):\n    leaf=t.count('\\f',0,m.start())\n    print(f'[{f.split(\"/\")[-1]} leaf {leaf}]',t[max(0,m.start()-w):m.end()+w].replace('\\n',' '));print('--')\n    n+=1\n    if n>=mx:break\nif n==0: print('NO HIT',f,pat)\nEOF\ncd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/s568.py\npython3 $S SYN.txt 'GIRDLE' 400 3; python3 $S SYN.txt 'jāma' 300 3"
}
```


### [2026-10-17T00:32:38.567Z] TOOL RESULT

```
[SYN.txt leaf 482] . ¢iras- ‘head’. Av. «xaoda- (OPers. xauda- in tigra- rauda- ‘with pointed cap’), perh. : Lat. cud6é ‘skin helmet’, IE *(s)keudh-, ex- tension of *skeu- ‘cover’. Walde-P. 2.550. Walde-H. 1.301. loanword, but -0. In Public Domain. Gurukul Kangri Collection, Haridwar Digitized by Arya Samaj Foundation Chennai and eGangotri SELECTED INDO-EUROPEAN SYNONYMS eo in “> SAL A ea eo fe. a ae 434 6.57 BELT, GIRDLE ‘ oth. gairda Lith. juosta ne ee fae ON ae 0, gyrdill, lindi, Lett. juosta Lat. cinclus, cingulum, beltz ChSl pojasit balteus Dan. balle SCr. pojas It. cinlura Sw. balle, gérdel Boh. pds Ir. ceinture OE gyrdel, belt Pol. pas Sp. cinturon ME belt, girdel Russ. pojas, kuSak Rum. cingdloare, curea, NE belt, girdle Skt. kafict-, mekh ala-, colan Du. — gordel racana- Ir. ferenn, criss OHG © gurlil, ba
--
NO HIT SYN.txt jāma
```


## [2026-10-17T00:32:41.479Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 -c \"\nt=open('SYN.txt',errors='ignore').read().split('\\f');x=t[482];i=x.find('6.57');print(x[i:i+3500])\""
}
```


### [2026-10-17T00:32:41.847Z] TOOL RESULT

```
6.57 BELT, GIRDLE
‘ oth. gairda Lith. juosta ne ee fae ON ae 0, gyrdill, lindi, Lett. juosta Lat. cinclus, cingulum, beltz ChSl pojasit balteus Dan. balle SCr. pojas It. cinlura Sw. balle, gérdel Boh. pds Ir. ceinture OE gyrdel, belt Pol. pas Sp. cinturon ME belt, girdel Russ. pojas, kuSak Rum. cingdloare, curea, NE belt, girdle Skt. kafict-, mekh ala-, colan Du. — gordel racana- Ir. ferenn, criss OHG © gurlil, balz Ay. yGh-, kamara- NIr. —crios MHG giirtel W. guwregys NHG _ giirtel Br. gourtz
1. Derivs. of *yés- ‘gird’ (perh. orig. *you-s-, extension of *yeu- ‘bind’) in Grk. tévyipt, twords, Lith. guostt, ChSl. po-jasatt, Av. yah-, pple. yasta-. Walde- P. 1.209.
Grk. tworqp, Sov; Lith., Lett. juosta; ChSI. pojasti, SCr., Russ. pojas, Boh. pds, Pol. pas; Av. yah-.
2. Derivs. of IE *kenk- in Lat. cin- gere ‘gird’, Skt. kavic- ‘bend’ (Dhatup.), ete. Walde-P. 1.400. Ernout-M. 187. Walde-H. 1.216 f.
Lat. cinctus, cingulum, late cinctiira (> It. cintura, Fr. ceinture, Sp. cintura, cinturon; Rum. cingdtoare new forma- tion); Skt. kavicz-.
3. Lat. balteus (esp. ‘sword-belt’), ac- cording to Varro an Etruscan word. Walde-H. 1.95. Ernout-M. 102. Hence ON belti, Dan. belie, Sw. balte, OF-NE belt, OHG balz, Falk-Torp 124.
Rum. curea (‘strap’ and the usual word for the common leather ‘belt?), fr. Lat. corrigia ‘strap’. REW 2253.
Rum. colan (esp. for women), fr. Turk. kolan ‘saddle-girth’. Lokotsch 1195.
4. Ir. ferenn : fern ‘shield’ (20.34), and so prob. at first ‘sword-belt’.
Ir. criss, NIr. crios = W. crys ‘shirt’ (6.44); epds. in W. gwregys (for *gwe-
CC-0. I
```


## [2026-10-17T00:32:50.250Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/s568.py\npython3 $S KLN_1966.txt '\\nzone' 600 3; python3 $S KLN_1966.txt '(?i)\\npajamas|\\npyjamas' 600 2; python3 $S AHD_watkins1985.txt '(?i)\\nyōs-|\\nyos-' 500 2; python3 $S AHD_watkins1985.txt '(?i)\\nyu-' 500 2"
}
```


### [2026-10-17T00:32:50.918Z] TOOL RESULT

```
NO HIT KLN_1966.txt \nzone
[KLN_1966.txt leaf 594]   (i.e.  to give,  resp.  take)  for  equal  value’.  Cp.  par.  Cp. also  appreciate,  compare,  depreciate,  disparage, disparity,  interpreter,  nonpareil,  Paris,  ‘a  genus of  plants’,  parisy liable,  parity,  parlay,  paroli, peer,  n.,  pornography,  praise,  precious,  price, prize,  pros-,  umpire,  herb  Paris.  Base  *per-,  ‘to sell’,  is  prob.  ult.  identical  with  base  *per-,  ‘to assign,  allot’,  whence  L.  pars,  gen.  partis,  ‘part’; see  part,  n.  Cp.  pare  and  words  there  referred  to. Derivatives:  pair,  tr.  and  intr.  v.,  pair-ed,  adj., pair-ed-ness,  n. pajamas,  pyjamas,  n.  pi.,  loose  trousers  or  draw¬ ers.  —  Hind,  pajama,  paijama,  lit.  ‘leg-garment’, fr.  Pers.  pa,  pat,  ‘foot,  leg’,  and  jama,  ‘clothing, garment’.  Pers.  pal,  ‘foot,  leg’,  is  rel.  to  Avestic pad-,  ‘foot’,  and  cogn.  with  Gk.  tcou;,  gen.  tto- 86q,  L.  pes,  gen.  pedis,  ‘foot’,  Goth,  fotus,  OE. fot,  ‘foot’.  See  foot  and  cp.  the  second  element in  charpoy,  teapoy,  seerpaw. pal,  n.,  an  intimate  friend.  —  English  Gypsy  pal, phal,  ‘brother’,  fr.  Gypsy  phral,  fr.  OI.  bhratar , ‘brother’.  See  brother. Derivatives:  pal,  intr
--
[AHD_watkins1985.txt leaf 27] ary full-grade form. A new full- grade form created by inserting the funda- mental vowel e in the zero-grade form of an extended root. sta-. V. Zero-grade extended root *sti- (< *stuo) . . . VI. Secondary full-grade form *“steua-... basic form. The unchanged root; so identi- fied for descriptive contrast. suffixed form. A form with one or more suffixes, written with an internal hyphen. mut-. Suffixed form *mut-il- ... Apero. Suffixed form *dper-yo- ... mel-4, 1. Suffixed (comparative) form *mel- yos-... prefixed form. A form with a prefix, written with an internal hyphen. op-'. 6. Prefixed form *co-op-... extended form. A form with an extension or enlargement, written solid. pel-*. IT. Extended form *peb-... nasalized form. A form with a nasal infix, written with internal hyphens. tag-. 1. Nasalized form *ta-n-g-... reduplicated form. A form prefixed by its own initial consonant followed by a vowel. segh-. 5. Reduplicated form “si-sgh-... expressive form. A form with “expressive gemination”
--
[AHD_watkins1985.txt leaf 111] vative jirare, “to pronounce a ritual formula,” swear: JURAL, JURIST, JURY}; ABJURE, ADJURE, CONJURE, INJURY, JURIDICAL, JURISCONSULT, JURISDICTION, JURISPRUDENCE, (NON- JUROR), OBJURGATE, PERJURE. 2. Compound form *yewes-dik-, “one who shows or pronounces the law” (see deik-), in Latin jidex, judge: JUDGE; ADJUDICATE, PREJUDICE. 3. Suffixed form *yewes-to- in Latin jistus, just: sust!. [Pok. ievos 512.] yewo-. Grain. Suffixed form *yew-ya in Greek zeia, one-seeded wheat: ZEIN. [Pok. iewo- 512.] yos-. To gird. 1. Suffixed form *yds-ter- in Greek zéstér, girdle: ZOSTER. 2. Suffixed form *yds-nd in Greek z6né, girdle: ZONE; EVZONE. [Pok. i6(u)s- 513.] yu-1. You. Second person (plural) pronoun. Germanic *jiiz (nominative) and *iwwiz (oblique) in Old English gé and éow, you: YE?, You. [Pok. 1. iu- 513.] yu-2, Outcry (of exultation). 1. Latin jibildre, to raise a shout of joy: JUBILATE. 2. Greek iuzein, to cry, call: JINX. [Pok. 2. iu- 514.] Index A Al oi-no- 4-1 ne AARDVARK  er-2, porko- AARDWO
--
[AHD_watkins1985.txt leaf 111]  yem-. To pair. Perhaps altered into Latin geminus, twin, paired: GEMINATE, GEMINI, GIMMAL; BIGEMINAL, TRI- GEMINUS. [Pok. iem- 505.] yér-. Year, season. 1. Suffixed basic form *yér-o- in Germanic *jéram in Old English géar, year: YEAR. 2. Suffixed o-grade form *ydr-d- in Greek hdrd, season: HOUR; HOROLOGE, HOROLOGY, HOROSCOPE. [In Pok. 1. ei- 293.] yes-. To boil, foam, bubble. 1. Germanic *jest- in Old English gist, yeast: YEAST. 2. Greek zeein, zein, to boil: ECZEMA, ZEOLITE. [Pok. jes- 506.] yu-? yeu-. Vital force, youthful vigor. Earliest form *ayeu-; variant of aiw-. Suffixed zero-grade form *yuwen- (< *yu-sen-), “possessing youthful vigor,” young. 1. Further suffixed form *yuwn-ti- in Germanic *jugunthi-, *jugun- tha- in Old English geoguth, youth: YOUTH. 2. Further suffixed form *yuwn-ko- in: a. Germanic *juwungaz becoming *jungaz in (i) Old English geong, young: YOUNG (ii) Old High German jung, young: JUNKER (iii) compound *jung-fréw6-, young lady (see per’); b. Old Irish 6ac, Iri
--
[AHD_watkins1985.txt leaf 111] DENCE, (NON- JUROR), OBJURGATE, PERJURE. 2. Compound form *yewes-dik-, “one who shows or pronounces the law” (see deik-), in Latin jidex, judge: JUDGE; ADJUDICATE, PREJUDICE. 3. Suffixed form *yewes-to- in Latin jistus, just: sust!. [Pok. ievos 512.] yewo-. Grain. Suffixed form *yew-ya in Greek zeia, one-seeded wheat: ZEIN. [Pok. iewo- 512.] yos-. To gird. 1. Suffixed form *yds-ter- in Greek zéstér, girdle: ZOSTER. 2. Suffixed form *yds-nd in Greek z6né, girdle: ZONE; EVZONE. [Pok. i6(u)s- 513.] yu-1. You. Second person (plural) pronoun. Germanic *jiiz (nominative) and *iwwiz (oblique) in Old English gé and éow, you: YE?, You. [Pok. 1. iu- 513.] yu-2, Outcry (of exultation). 1. Latin jibildre, to raise a shout of joy: JUBILATE. 2. Greek iuzein, to cry, call: JINX. [Pok. 2. iu- 514.] Index A Al oi-no- 4-1 ne AARDVARK  er-2, porko- AARDWOLF er-2, wikwo- AB-!  apo- ABAFT apo- ABANDON bha-2 ABASE bassus ABASH bat- ABASIA gWa- ABATE battuere ABBREVIATE mregh-u- ABDICATE deik- ABDUCENS deuk- ABD
--
```


## [2026-10-17T00:32:55.445Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/s568.py\npython3 $S KLN_1966.txt 'zone,  n\\.|zone, n\\.' 900 2; python3 $S KLN_1966.txt '(?i)zonar|zunnar' 300 3; python3 $S KLN_1966.txt '\\nyou,|  you,  pron' 500 2"
}
```


### [2026-10-17T00:32:56.421Z] TOOL RESULT

```
[KLN_1966.txt leaf 134]  canvas,  n.  —  OF.  (=  F.)  canevas,  prop,  a  blend of  Picard  canevach  and  OF.  chenevas,  lit.  ‘made of  hemp,  hempen’,  fr.  OF.  chaneve  (F.  chanvre ), ‘hemp’,  fr.  L.  cannabis,  ‘hemp’,  fr.  Gk.  xxvvx- fhc;.  Sec  hemp  and  cp.  canvass. Derivative:  canvas,  tr.  v. canvass,  tr.  v.,  to  discuss;  intr.  v.,  to  solicit  votes. —  Fr.  canvas.  To  canvass  orig.  meant  ‘to  sift through  canvas’.  Cp.  OF.  canabasser,  ‘to  exam¬ ine  carefully’,  lit.  ‘to  sift  through  canvas',  fr. OProven?.  canabas,  ‘canvas’,  which  is  rel.  to OF.  canevas. Derivative:  canvass-er,  n. canyon,  canon,  n.,  a  narrow  valley  between  cliffs. canzone capreoi 234 235 —  Sp.  cation,  ‘deep,  hollow  gorge’,  augment,  of carlo,  'tube',  fr.  L.  canna,  ‘reed,  cane,  tube'.  See cane  and  cp.  canal,  cannon. Derivative:  canyon,  cation,  tr.  and  intr.  v. canzone,  n.,  a  song.  —  It.,  fr.  L.  cantionem,  acc. of  cantid,  ‘song’,  fr.  cant-(um),  pp.  stem  of  ca- nere,  ‘to  sing’.  See  cant,  ‘slang  of  beggars’,  and cp.  next  word.  Cp.  also  chanson, canzonet,  n.,  a  short  song.  —  It.  canzonetta,  di- min.  of  canzone,  ‘song’.  See  prec.  word  and  -et. caoba,  n.,  mahogany.  —  Sp.,  fr.  a  Caribbean  na¬ tive  word. caoutchouc,  n.  —  F.,  a  Tupi  loan  word  (prob. through  the  medium  of  Sp.  caucho). cap,  n.,  a  covering  for  the  head.  —  ME.  cappe,  fr. OE.  cxppe,  ‘hood,  cap’,  fr.  Late  L.  cappa.  See cape,  ‘cloak’,  and  cp,  words  there  referred  to. Derivatives:  cap,  tr.  v.,  capp-ed,  adj.,  capp-er, n.,  capp-ing,  n.,  capp-y ,  adj. capable,  adj.  —  F.,  fr.  L.  capabilis,  ‘able  to  grasp or  hold,  capable’,  fr.  capere,  ‘to  catch,  seize, hold’.  See  captive  and  -able. Deriva
--
[KLN_1966.txt leaf 592]  fr.  AF.  oyes,  which  corresponds  to  OF. oiez,  oyez,  ‘hear  ye!’,  imper.  pi.  of  oir  (F.  ouir), ‘to  hear’,  fr.  L.  audiatis,  2nd  pers.  pi.  of  pres, subj.  fr.  audire,  ‘to  hear’.  See  audible  and  cp. oyer. oyster,  n.  —  ME.,  fr.  OF.  oistre,  uistre  (F.  huitre), fr.  L.  ostrea,  ostreum,  fr.  Gk.  ocrxpsov,  ‘oyster’, which  is  rel.  to  octxeov,  oaxouv,  ‘bone’;  so called  from  its  hard  shell.  See  osteo-  and  cp. ostracize. ozo-,  combining  form  meaning  ‘smell’  (generally used  in  a  bad  sense.  —  Gk.  o^o-,  fr.  o£siv,  ‘to smell’.  See  odor  and  cp.  ozone,  osmium. ozocerite,  n.,  a  waxlike  mineral.  —  G.  Ozokerit , coined  by  the  German  mineralogist  Ernst  Frie¬ drich  Glocker  (1793-1858)  in  1833  fr.  ozo-,  Gk. x^pog,  ‘wax’,  and  suff.  -it,  which  goes  back  to Gk.  -iTt]?.  See  cere  and  subst.  suff.  -ite. ozone,  n.,  an  allotropic  form  of  oxygen  with  a pungent  odor  ( chem .)  —  Coined  by  the  German chemist  Christian  Friedrich  Schonbein  (1799- 1868) in  1840  fr.  Gk.  o£eiv,  ‘to  smell’;  so  called by  him  because  of  its  strong  smell.  See  ozo-. Derivatives:  ozon-ed,  ozon-ic,  adjs.,  ozonize (q.v.),  ozon-ous,  adj. ozonize,  tr.  v.,  to  convert  into  ozone;  to  impreg¬ nate  with  ozone  (chem.)  —  Formed  from  prec. word  with  suff.  -ize. Derivatives:  ozoniz-ation,  n.,  ozoniz-er,  n. pa,  n.,  father  ( colloq .)  —  Abbreviation  of  papa. pabulum,  n.,  food,  nourishment.  —  L.  pabulum, ‘food,  fodder’,  for  *pa-dhlo-m,  formed  with  in¬ strumental  suff.  *-dhlo-m  fr.  I.-E.  base  *pd-,  ‘to tend,  keep,  pasture,  feed,  guard,  protect’, whence  also  L.  pa-nis,  ‘bread’,  pd-scere,  ‘to graze,  pasture,  feed’,  pa-stor,  ‘shepherd’,  lit. ‘fee
--
NO HIT KLN_1966.txt (?i)zonar|zunnar
NO HIT KLN_1966.txt \nyou,|  you,  pron
```


## [2026-10-17T00:33:00.507Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/s568.py\npython3 $S KLN_1971.txt 'zone,\\s+n\\.' 700 2; python3 $S KLN_1971.txt 'you,\\s+pron' 600 1; python3 $S KLN_1971.txt 'gird,\\s+tr' 400 1"
}
```


### [2026-10-17T00:33:01.109Z] TOOL RESULT

```
[KLN_1971.txt leaf 0] made  of hemp, hempen’, fr. OF. chaneve (F. chanvre),  ‘hemp’, fr. L. cannabis, ‘hemp’, fr. Gk. xawa-  Pi<;. See hemp and cp. canvass.   Derivative: canvas , tr. v.  canvass, tr. v., to discuss; intr. v., to solicit votes.   — Fr. canvas. To canvass orig. meant ‘to sift  through canvas ' , Cp. OF. canabasser , ‘to exam-  ine carefully’, lit. ‘to sift through canvas’, fr.  O Proven*;, canabas, ‘canvas’, which is rel. to  OF. canevas.   Derivative: canvass-er, n.  canyon, cafton, n., a narrow valley between cliffs.   — Sp. cahdn, ‘deep, hollow gorge’, augment, of  caho, ‘tube*, fr. L. canna, ‘reed, cane, tube’. See  cane and cp. canal, cannon.   Derivative: canyon, canon, tr. and intr. v.  canzone, n., a song. — It., fr. L. cantidnem, acc.  of cant id, ‘song’, fr. cant-(um), pp. stem of ca-  nere , ‘to sing’. See cant, ‘slang of beggars’, and  cp. next word. Cp. also chanson,  canzonet, n., a short song. — It. canzone tta, di-  min. of canzone, ‘song’. See prec. word and -et.  caoba, n., mahogany. — Sp., fr. a Caribbean na-  tive word.   caoutchouc, n. — F., a Tupi loan word (prob.   through the medium of Sp. caucho).  cap, n„ a covering for the head. — ME. cappe, fr.  OE. exppe, ‘hood, cap’, fr. Late L. cappa. See  cape, ‘cloak’, and cp, words there referred to.  Derivatives: cap , tr. v., capp-ed, adj., capp-er,  n., capp-ing, n., capp-y, adj.  capable, adj. — F., fr. L. capabilis, ‘ab
--
[KLN_1971.txt leaf 0]  hear’, fr. L. audidtis , 2nd pers. pi. of pres,  subj. fr. audire, ‘to hear’. See audible and cp.  oyer,   oyster, n. — ME., fr. OF. oistre, uistre (F. huitre),  fr. L. ostrea , ostreum , fr. Gk. Saxpeov, ‘oyster’,  which is rel. to oct£ov, octxouv, ‘bone’; so  called from its hard shell. See osteo- and cp.  ostracize.   ozo-, combining form meaning ‘smell’ (generally  used in a bad sense. — Gk. &£o-, fr. ‘to  smell’ . See odor and cp. ozone, osmium,  ozocerite, n., a waxlike mineral. — G. Ozokerit ,  coined by the German mineralogist Ernst Frie-  drich Glocker (1793-1858) in 1833 fr. ozo-, Gk.  x?)p6<;, ‘wax’, and suff. -it, which goes back to  Gk. -fxr^. See cere and subst. suff. -ite.  ozone, n., an allotropic form of oxygen with a  pungent odor (chem.) — Coined by the German  chemist Christian Friedrich SchOnbein (1799-  1868) in 1840 fr. Gk. 6Ceiv, ‘to smell’; so called  by him because of its strong smell. See ozo*.  Derivatives : ozon-ed, ozon-ic , adjs., ozonize  (q.v.), ozon-ous, adj.   ozonize, tr. v., to convert into ozone; to impreg-  nate with ozone (chem.) — Formed from prec.  word with suff. -ize.   Derivatives: ozoniz-ation, n., ozoniz-er , n.      p     pa, n., father ( colloq .) — Abbreviation of papa,  pabulum, n., food, nourishment. — L. pabulum ,  ‘food, fodder’, for *pa-dhlo-m , formed with in-  strumental suff. *-dhlo-m fr. I.-E. base *pd~, ‘to  tend, keep, pastu
--
[KLN_1971.txt leaf 0] , gonder, ginder, Du.  ginder, Goth, jaindre, ‘over there’, and see prec.  word.   Derivative: yonder, adj.   yore, adv., long ago. — ME. yore , fr. OE. geara ,  geara, ‘long ago, formerly’, lit. ‘of years’, gen.  pi. of gear , ‘year’. See year.   Derivative: yore, n,   york, tr. v., to bowl out (a batsman) with a  yorker. — Back formation from next word,  yorker, n., a bowled ball that pitches inside the  crease (cricket). — Prob. connected with the  place name York.   Yorkist, n., an adherent of the house of York  ( English hist.) — Formed from the English  place name York with suff. -ist.  you, pron. — ME. eow, eou , you , yow, fr. OE.  eow, used as dat. and acc. of ge, ‘ye’; rel. to ON.  ydr (used as dat. and acc. of er, ‘ye’), OS. iu  (used as dat. and acc. of gi, ge, ‘ye’), OFris.  iuwe, iwe (used as dat. and acc. of gi, ‘ye’), MDu.  u (used as dat. and acc. of gi, ge, ‘ye’), Du. u  (used as dat. and acc. of gij, ‘ye’), OHG., MHG.  iu (used as dat. of ir , ‘ye’), OHG. iuwih, MHG.  iuwich, iuch (used as acc. of ir, ‘ye’), G. euch  (used as dat. and acc. of ihr, ‘ye’), Goth, izwis  (used as dat. and acc. of jus, ‘ye’). See ye, pron.,  and cp. your.   young, adj. — ME. yung , yong, fr. O
--
[KLN_1971.txt leaf 0] -li-ness, n., beggar-y , n.  begin, tr. and intr. v. — ME. beginnen, fr. OE. be-  ginnan, rel. to OS., OHG. beginnan, MDu. be-  ghinnen , MLG., Du., MHG., G. beginnen, OFris.  bijenna, Goth, du-ginnan, ‘to begin’, fr. Teut.  *bi-ginnan, fr. bi- (see be) and *ginnan, which  is prob. cogn. with Alb. zl and zq, ‘to touch,  begin’. Cp. gin, ‘to begin’.   Derivatives: beginn-er , n., beginn-ing, n.  begird, tr. v. — ME. begyrden , fr. OE. begyrdan,  fr. be- and gyrdan, ‘to gird’. See gird, ‘to en-  circle’.   beglerbeg, n., formerly, governor of a province in  the Ottoman empire. — Turk., lit. ‘bey of beys’,  fr. begler, pi. of beg , ‘bey’, and beg , ‘bey’. See  bey and cp, beg, n,, begum,  begnaw, tr. v. — OE. begnagan , fr. be- and gna-  gan , ‘to gnaw’. See gnaw.   begone, intr. v. and interj. — Pro
--
```


## [2026-10-17T00:33:04.582Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/s568.py\npython3 $S KLN_1971.txt '  zone, ' 800 2; python3 $S KLN_1971.txt '  ye, pron' 600 1"
}
```


### [2026-10-17T00:33:05.171Z] TOOL RESULT

```
NO HIT KLN_1971.txt   zone, 
NO HIT KLN_1971.txt   ye, pron
```


## [2026-10-17T00:33:09.215Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/s568.py\npython3 $S KLN_1971.txt 'zone, n' 800 2; python3 $S KLN_1971.txt 'ye, pron' 500 1; python3 $S KLN_1971.txt 'zonnar|zunnar|zonar' 300 2"
}
```


### [2026-10-17T00:33:09.824Z] TOOL RESULT

```
[KLN_1971.txt leaf 0] nadian.  canvas, n. — OF, (= F.) canevas, prop, a blend  of Picard canevach and OF. chenevas, lit. ‘made  of hemp, hempen’, fr. OF. chaneve (F. chanvre),  ‘hemp’, fr. L. cannabis, ‘hemp’, fr. Gk. xawa-  Pi<;. See hemp and cp. canvass.   Derivative: canvas , tr. v.  canvass, tr. v., to discuss; intr. v., to solicit votes.   — Fr. canvas. To canvass orig. meant ‘to sift  through canvas ' , Cp. OF. canabasser , ‘to exam-  ine carefully’, lit. ‘to sift through canvas’, fr.  O Proven*;, canabas, ‘canvas’, which is rel. to  OF. canevas.   Derivative: canvass-er, n.  canyon, cafton, n., a narrow valley between cliffs.   — Sp. cahdn, ‘deep, hollow gorge’, augment, of  caho, ‘tube*, fr. L. canna, ‘reed, cane, tube’. See  cane and cp. canal, cannon.   Derivative: canyon, canon, tr. and intr. v.  canzone, n., a song. — It., fr. L. cantidnem, acc.  of cant id, ‘song’, fr. cant-(um), pp. stem of ca-  nere , ‘to sing’. See cant, ‘slang of beggars’, and  cp. next word. Cp. also chanson,  canzonet, n., a short song. — It. canzone tta, di-  min. of canzone, ‘song’. See prec. word and -et.  caoba, n., mahogany. — Sp., fr. a Caribbean na-  tive word.   caoutchouc, n. — F., a Tupi loan word (prob.   through the medium of Sp. caucho).  cap, n„ a covering for the head. — ME. cappe, fr.  OE. exppe, ‘hood, cap’, fr. Late L. cappa. See  cape, ‘cloak’, and cp, words there referred to.  Derivatives: cap , tr. v., capp-ed, adj., capp-er,  n., capp-ing, n., capp-y, adj.  capable, adj. — F., fr. L. capabilis, ‘able to grasp  or hold, capable’, fr. capere, ‘to catch, seize,  hold’. See captive and -able.   Deri
--
[KLN_1971.txt leaf 0] s, fr. AF. oyes, which corresponds to OF.  oiez, oyez, ‘hear ye!’, imper. pi. of oir (F. ouir),  ‘to hear’, fr. L. audidtis , 2nd pers. pi. of pres,  subj. fr. audire, ‘to hear’. See audible and cp.  oyer,   oyster, n. — ME., fr. OF. oistre, uistre (F. huitre),  fr. L. ostrea , ostreum , fr. Gk. Saxpeov, ‘oyster’,  which is rel. to oct£ov, octxouv, ‘bone’; so  called from its hard shell. See osteo- and cp.  ostracize.   ozo-, combining form meaning ‘smell’ (generally  used in a bad sense. — Gk. &£o-, fr. ‘to  smell’ . See odor and cp. ozone, osmium,  ozocerite, n., a waxlike mineral. — G. Ozokerit ,  coined by the German mineralogist Ernst Frie-  drich Glocker (1793-1858) in 1833 fr. ozo-, Gk.  x?)p6<;, ‘wax’, and suff. -it, which goes back to  Gk. -fxr^. See cere and subst. suff. -ite.  ozone, n., an allotropic form of oxygen with a  pungent odor (chem.) — Coined by the German  chemist Christian Friedrich SchOnbein (1799-  1868) in 1840 fr. Gk. 6Ceiv, ‘to smell’; so called  by him because of its strong smell. See ozo*.  Derivatives : ozon-ed, ozon-ic , adjs., ozonize  (q.v.), ozon-ous, adj.   ozonize, tr. v., to convert into ozone; to impreg-  nate with ozone (chem.) — Formed from prec.  word with suff. -ize.   Derivatives: ozoniz-ation, n., ozoniz-er , n.      p     pa, n., father ( colloq .) — Abbreviation of papa,  pabulum, n., food, nourishment. — L. pabulum ,  ‘food, fodder’, for *pa-dhlo-m , formed with in-  strumental suff. *-dhlo-m fr. I.-E. base *pd~, ‘to  tend, keep, pasture, feed, guard, protect’,  whence also L. pa-nis , ‘bread’, pa-scere , ‘to  graze, pasture, feed’,
--
[KLN_1971.txt leaf 0] o achene, Chama, chasm, Chauna, chela,  ‘claw’, chemosis. Cp. alsochori- and words there      837   referred to.   Derivatives: yawn , n., the act of yawning, yawn-  er , n., yawn-ing, adj., yawn-ing-ly, adv.  yawp, intr. v., to yelp; n., a yelp. — Of imitative  origin. Cp. yap, yelp.   yaws, ft., a skin disease (med.) — A Caribbean  word.   yclept, ycleped, adj., called, named (archaic). —  ME. iclepedy fr. OE. gecleopod, geclypod , pp. of  ( ge)clypian , ‘to call’. See y-, ‘with’, and clepe.  ye, pron. of the 2nd person (archaic and poet.) —  ME. ye t fr. OE. ge, ‘ye’, rel. to OS. gf, ge , ON.  er (prob. influenced in form by ON. ver),  Dan., Swed. /, ‘ye, you’, OFris. gi, MDu. gi ,  ge , Du. gij, OHG., MHG. ir [prob. influenced  in form by OHG., MHG. (= G.) wir, ‘we’], G.  ihr, Goth, jus, and cogn. with OPruss. ious,  Lith. jus,A\b.ju, OI. yuydm, Avestic yuz 6 m, Gk.  0 [xcT;, ‘ye, you’. Cp. you.  ye, def. art. — Archaic printed form of the ar-  ticle the (OE. pe ), due to a confusion of th
--
[KLN_1971.txt leaf 0] he  supernatural power by which, according to  voodoo belief, a dead body may be reanimated.   — Of African origin. Cp. Kongo zumbi , fetish’.  Derivative: zomb-ism, n.   zonal, adj., pertaining to a zone. — Late L. zona-  lis, ft. L. zona. See zone and adj. suff. -al.  Derivative: zonal-ly , adv.  zonar, h., a girdle. — ModGk. £o)vapi, ‘a girdle’,  fr. Gk. ^eovdtptov, dimin. of £covt). See zone,  zone, n., 1) a belt; 2) a region, area; 3) any of the  five great divisions of the earth’s surface. — E,,     fr. L. zona, fr. Gk. whence £ovvuvai, ‘to   gird’, Ctoaxoc, ‘girt’, fr. I. -E. base *yds-, ‘to
--
[KLN_1971.txt leaf 0]  of the  five great divisions of the earth’s surface. — E,,     fr. L. zona, fr. Gk. whence £ovvuvai, ‘to   gird’, Ctoaxoc, ‘girt’, fr. I. -E. base *yds-, ‘to  gird; girdle’, whence also Avestic yasta-; ‘girt’,  Lith. juosiu, juosti , ‘to gird’, OSlav. po-jasit,  ‘girdle’, Alb. n-geS, ‘I gird’. Cp. zonar, Zostera,  azonic.   Derivatives: zone , tr. v., zonal (q.v.), zon-ary,  zon-ate , adjs., zonule (q.v.)  zonule, n., small belt. — L. zonula , dimin. of zona ,  ‘belt, girdle’. See prec. word and -ule.  Derivative: zonul-ar , adj.   Zonuridae, n. pi., a family of lizards (zool.) —  ModL., formed wi
--
```


## [2026-10-17T00:33:17.124Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/s568.py\npython3 $S HJB.txt '(?i)PYJAMAS' 900 2; python3 $S SKT.txt '(?i)pyjamas' 400 1; python3 $S SKT.txt '(?i)\\nzone' 400 1; python3 $S LKT.txt '(?i)ǧāma|ğāma|jama-dan|čamadan|camadan|ǵāmä' 400 3; python3 $S LKT.txt '(?i)zunn' 400 2"
}
```


### [2026-10-17T00:33:17.945Z] TOOL RESULT

```
[HJB.txt leaf 66] .  .  .  "— Cocks*8  Diary,  i.  64. 1648.— See  Van  Twist  above,  under  AL- CATIF.   And  1673,  see  ^r3/«r  under  ATLAS. 1653.— "Alaims  (Alajas)estvn  mot  Indien, qui  signifie  des  toiles  de  cotton  et  de  soye : meslM  de  plusieurs  couleurs." — DelaBoui- laye-U'Oouz,  ed.  1657,  p.  532. [c.  1666.— "Alachas,  or  silk  stuffs  inter- woven  with  gold  and  silver."— Anticr  (ed. ConstdbU),  p.  120-21.] 1690.— "It  (Suratt)  is  renown'd  .... both  for  rich  Silks,  such  as  Atlasses,  Cut- taneee,  Sooseys,  Chilgars,  Allajars  ....'* —OvijigUm,  218. 1712.— "An  AlleJah  petticoat  striped with  green  and  gold  and  white."— Advert, in  Spectator,  cited  in  Malcolm,  Anecdotes, 429. 1726.— "Gold  and  sUver  Allegias."— Valeniifn  {Surat),  iv.  146. 1813.— "Allachaa  (pieces  to  the  ton) 1200."— Jfi»ttra,  ii.  221. 1885.— "The  cloth  from  which  these pyjamas  aro  made  (in  Swat)  is  known  as Alacha,  and  is  as  a  rule  manufactured  in their  own  houses,  from  2  to  20  threads  of silk  being  let  in  with  the  cotton  ;  the  silk  aH well  as  the  cotton  is  brousrht  from  Peshawur and  spun  at  home"— M'Nair's  Report  on Explorations,  p.  5. ALLIGATOB,  s.  This  is  the  usual Anglo-Indian  term  for  the  great  lacer- tine  amnhibia  of  the  rivers.  It  was apparently  in  origin  a  corruption,  im- ported from  S.  America,  of  the  Spanish el  or  al  lagarto  (from  Lat.  lacerta),  'a lizard.'  The  "  Summary  of  the  Western Indies"  by  Pietro  Martire  d'Angheria, as  given  m  Ramusio,  recounting  the last  voyage  of  Columbus,  says  that,  in  a certain  river,  "they  sometimes  en- countered those  crocodiles  which  they call  Lagaxti ;  these  make  away  when they  see  the  Christians,  and 
--
[HJB.txt leaf 568]  — Letter  from  Cmai  of  EJ,C.  to  Madras,  Nov. 9th.    In  Nolti  ondRxU.,  No.  i.  p.  2. [1682. — " ...  for  Long  cloth  brown EngUsh  72:  Coveds  long  &2j  broad  No.  I. .  .  r^Pringle,  Diary,  Ft,  St.  Ueo.  Ist  ser. 1727.— "  iStuferoM,   or  Saderau  Patam,   a small  Factory  belonging  to  the  Dutdu  to- buy  up  long  Oloth."— ^.  Hamiltcn,  i.  858  ; 1785.— "The  trade  of  Fort  St  David's- consists  in  long  olothe  of  different  colours.*' — Carraoeiolt't  Life  ofClive,  i.  5. 1865.—"  Long-doth,  as  it  is  termed,  is  th& material  principally  worn  in  the  Tropics." — Waring,  Tropical  Rendent,  p.  111. 188Q.— "  A  Chinaman  is  probably  the  last man  in  the  world  to  be  taken  in  twice  with a  fraudulent  piece  of  long-doth.  " —  PaJC Mall  Bridget,  Jan.  9,  p.  9. L0NG-DBAWEB8,  s.  This  is  axt old-fashioned  equivalent  for  pyjamas^ (a. v.).  Of  late  it  is  confined  to  the Madras  Presidency,  and  to  outfitters* lists.  [Mosquito  drawers  were  probably like  these.] [1628.— "They  wear  a  pair  of  loog^ Drawers  of  the  same  Cloth,  which  cover  not only  their  Thighs,  but  legs  also  to  the  Feet,"* —P.  ddla  Voile,  Hak.  Soc.  i.  48.] 1711.  —  "  The  better  sort  wear  long- Drawers,  and  a  piece  of  Silk,  or  wrought Callico,  thrown  loose  over  the  Shoulders.  — Loekyer,  57. 1774. — ".  .  .  gave  each  private  man  a- frock  and  long  dnwoTB  of  chmts."- Formu^ V.  to  N,  Guinea,  100. 1780. — "  Leroy,  one  of  the  French  hussars, who  had  saved  me  from  being  cut  down  by Hyder's  horse,  save  me  some  soup,  and  & shirt,  and  long-drawBTB,  which  I  had  great want  of."— JSTcm.  John  Lindsay  in  Livet  of the  Lindsays,  iv.  266. 1789.— "It  is  true  t
--
NO HIT SKT.txt (?i)pyjamas
NO HIT SKT.txt (?i)\nzone
NO HIT LKT.txt (?i)ǧāma|ğāma|jama-dan|čamadan|camadan|ǵāmä
NO HIT LKT.txt (?i)zunn
```


## [2026-10-17T00:33:23.243Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/s568.py\npython3 $S HJB.txt 'PYJAMAS, s|PYJAMAS,  s|PAIJAMAS|PYJAMMAS' 1200 2; python3 $S SKT.txt '(?i)pyjama|pajama' 300 2; python3 $S SKT.txt 'zone, ' 300 2; python3 $S LKT.txt '(?i)zunn|zonn|zinnar|zunär' 300 3; python3 $S LKT.txt '(?i)čemodan|çamadan|camadan|cemodan|ʒāma|ǯāma' 300 3"
}
```


### [2026-10-17T00:33:24.123Z] TOOL RESULT

```
[HJB.txt leaf 794] r  or orderly  attached  to  an  office,  and bearing  a  belt  and  brass  l)adge,  called in  Bengal  chuprassy  or  peon  (qq.v.), in  Madras  usually  by  the  latter  name. 1878. — "  Here  and  there  a  belted  Govern- ment servant,  called  a  PuttiwUft,  or  Patta- wUft,  because  distinguished  by  a  belt.  .  ."." — Monier  Williams,  Modem  Itidia,  34. PUTWA,  s.  Hind.  pattPd.  The Hibucns  mhdariffa,  L.,  from  the  suc- culent acid  flowers  of  which  very  fair jelly  is  made  in  Anglo-Indian  house- nolds.  [It  is  also  known  as  the Rozelle  or  Red  Sorrel  {Watt,  Econ. Di^^.  iv.  243).  Riddell  {Domest.  Econ. 337)  calls  it  "  Oseille  or  Boselle  jam and  jelly.*'] PYE,  s.  A  familiar  designation among  British  soldiers  and  young officei-s   for  a   Pariah-dog  (q.v.) ;   a PYJAMAfAS. 748 PYKE,  PAIK. contraction,  no  douLt,  of  the  former word. [1892.—'*  We  English  call  him  a  pariali, but  this  word,  belonging  to  a  low,  yet  by  no moans  degraded  class  of  people  in  Maaras, is  never  heard  on  native  lips  as  applied  to  a dog,  any  more  than  our  other  word  *pie.' " — Z,  Kipling,  Bead  and  Man,  266.] PYJAMMAS,  8.  Hind,  pdi-jdma (see  JAMMA),  lit.  'leg-clothing.'^  A pair  of  loose  drawers  or  trowsers,  tied round  the  waist.  Such  a  garment  is used  by  various  persons  in  India,  e.g. by  women  of  various  classes,  by  Sikh men,  and  by  most  Mahommedans  of both  sexas.  It  was  adopted  from  the Mahommedans  by  Europeans  as  an article  of  dishabille  and  of  night attire,  and  is  synonymous  with  Long Drawers,  Shulw^urs,  and  Mogul- breecliefl.  [For  some  distinctions between  these  various  articles  of  dress see  Forbes-Watson,  {Textile  Manu- factures, 57).]  It  is  probable  that  we English  took  the  habit  like  a  good many  others  from  the  Portuguese. Thus  Pyrard  (c.  1610)  says,  in  speak- ing of  Goa  Hospital:  "lis  ont  force calsons  sans  quoy  ne  couchent  iamais les  Portugais  des  Indes"  (ii.  p.  11; [Hak.  Soc.  ii.  9]).  The  word  is  now  used in  London  shops.  A  friend  furnishes the  following  reminiscence  :  "  The  late Mr.   B   ,   tailor  in  Jermyn  Street, some  40  years  ago,  in  reply  to  a question  why  pyjammas  had  feet sewn  on  to  them  (as  was  sometimes the  case  with  those  fur
--
NO HIT SKT.txt (?i)pyjama|pajama
[SKT.txt leaf 106] Claok. Client.  (F.-L.)     F.  c/im/.  a  suJtor., L.  c/Unfer»,ucc  of  cltrtu  =  dufHS.  orig. hearer,  one  who  listens  to  advice  ;  pses  {t of  (lu^re.  to  hear.   (V  KRU.) cuff;  see  Cleave  (a). CUmatc.  (F.-Gk.)  M.E.  fUw^.^ F.  climat.  —  Ck.  «Xi^t».  stem  of  xAl'^ a  slope,  zone,  region  of  the  earth*  cfr m^ite.  -  Gk.  mkivw,  to  lean,  «loj>c: Lean. climacter.  a  critical  time  of  life  (F.^ Gk.)      F.   (limactert.   adj.  ;    whence  /*« clima£t€rt.    'the    cIun.ilericaU    '^-i    »•' every  7th.  or  qlh,  or  the  63  ycart life,  all  very  dangerous, 
--
NO HIT LKT.txt (?i)zunn|zonn|zinnar|zunär
[LKT.txt leaf 78] rs.  g:aii>ä(iaii : 'Kleiderbeliälter,  Kotier'  [aus  pers.  (/tfwä 'Tuch,  Kleid'  Horn  NpEl  S.  93,  Nr.  412, und  Suffix  -dän  'Behälter'  ebenda S.  118,  Nr.  533],  ebenso  Ik.  gamedan, öamedan;  hieraus  runi.  ö'eawan^an  'Fell- eisen, Handkoffer',  bulg.  zemadan,  ce- madan,  russ.  cemodan  'dass.'.  [Gor- jajew  410. ö53.  Ar.  gaiual: 'Kamel'  [aus  der  Wurzel  (jamala  'sam- meln', also  'Haufen,  Höcker',  vielleicht urverwandt  mit  hammäl  'Lastträger',  s. hier  Nr.  806,  SCHOTT  in  ZDMG  XXXIH, 54:-!];  aus  dieser  oder  einer  anderen semitischen  Form  gr.  Ka|nriXo;,  
--
```


## [2026-10-17T00:33:32.308Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/s568.py\npython3 $S LKT.txt '(?i)z.nn.r' 400 3; python3 $S AFM_pages.txt 'زنار|زنّار' 500 2; python3 $S FVQ_pages.txt '(?i)z.nn.r|ζων' 300 2; python3 $S incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt '(?i)z.nn.r|zonn|zun' 300 3"
}
```


### [2026-10-17T00:33:32.866Z] TOOL RESULT

```
[LKT.txt leaf 109] t  die  Han- delskarawanen aus  Ost-  und  Westasien trafen  [QUATREMERE  im  Journal  des Savants  1846,  S.  751  ;  W.  v.  Heyd,  Ge- schichte des  Levantehandels  im  MA  I, 37] ;  hieraus  mal.  kelang  'Zinn',  pg.  calah7i 'sehr  feines  ind.  Zinn'  [Constancio  Dicc 205b;  DE  245].  Über  tk.  kalaj  [ngr. Ka\di]  wurde  serb.  kalaj  'Zinn',  bulg. ebenso;  ferner  rum.  calangiü  'Verzinner'. 1022.  Ar.  kalafa: 'Ein  Schiff  kalfatern  und  teeren'  [junges Wort,  wohl  aus  dem  mgr.  KaXaqpaxeiv 'dass.',  KoXacpdTriq  'Schiffsarbeiter,  der die  betr.  Arbeit  ausführt';  dieses  kommt sicherlich  aus  ar.  kafr  'Asphalt',  s.  hier Nr.  999;  Ersatz  von  r  durch  l  und  Me- tathesis  sind  häufig];  hieraus  it.  cala- fatare  'ein  leckes  Schiff  ausbessern',  prov. calefa
--
NO HIT AFM_pages.txt زنار|زنّار
[FVQ_pages.txt leaf 171] ability that these are all derived from the Skt. ^JIF a horn. Sec, however, Laufcr, ftino-Iranica, 54fi, 583. 5 This then beoame ytyyt'jStpis and through the Lat. gingibvr became the Middle English gingevir and our ginger. IVorn fyytj3c/M? came the Syr. ^2)Q.kj] and other forms (Low, Aramainche Pfanzcnnarnen, p. 138). ^ 6 Fracnkel, Vocab, 11 ; Pautz, Offenbarung, 213 ; Horovitz, 1'aradie*, 11; Addai Sher, 80. 7 See Geyer, Zwei Gedichte, i, 57 ; ii, 83 ; Jacob, Beduinenleben, 258.FOREIGN VOCABULARY OF THK QUR^AN 155 ** the Aram. The verbal forms ir j j, etc., with this meaning are clearly denominati
--
[PLA_asbaghi_1988_ia_djvu.txt leaf 0] e und photographi-  sche Wiedergabe nur mit ausdrücklicher Genehmigung des Verlages. Reproduktion, Druck und buchbin-  derische Verarbeitung: Hubert & Co., Göttingen. Printed in Germany.    Meinem Lehrer, Herrn Prof. Dr. Macuch zu seinem 65. Geburtstag.    Inhaltsverzeichnis    Verzeichnis der Abkürzungen    Vorwort    Einleitung    Wörterbuch    Literaturverzeichnis    IX    XIII    275    Verzeichnis der Abkürzungen    a) Philologische Abkürzungen    aaram.  Adj.  Adv.  afghan.  afrz.  ägypt.  ägypt.-ar.  ahd.  ähnl.  air.  aind.  ait.  akk.  act. Pt.  alban.  ap.   ar.  aram.  arm,  ass.  assy
--
[PLA_asbaghi_1988_ia_djvu.txt leaf 0] n-  derische Verarbeitung: Hubert & Co., Göttingen. Printed in Germany.    Meinem Lehrer, Herrn Prof. Dr. Macuch zu seinem 65. Geburtstag.    Inhaltsverzeichnis    Verzeichnis der Abkürzungen    Vorwort    Einleitung    Wörterbuch    Literaturverzeichnis    IX    XIII    275    Verzeichnis der Abkürzungen    a) Philologische Abkürzungen    aaram.  Adj.  Adv.  afghan.  afrz.  ägypt.  ägypt.-ar.  ahd.  ähnl.  air.  aind.  ait.  akk.  act. Pt.  alban.  ap.   ar.  aram.  arm,  ass.  assyr.  aw.   bab.   Bd.   Bed.  Bez.  bibl.-aram.  bot.  bulg.  byz.  cech,  chald.  ch.-pal,    comp.  d.    altaramä
--
[PLA_asbaghi_1988_ia_djvu.txt leaf 0] t & Co., Göttingen. Printed in Germany.    Meinem Lehrer, Herrn Prof. Dr. Macuch zu seinem 65. Geburtstag.    Inhaltsverzeichnis    Verzeichnis der Abkürzungen    Vorwort    Einleitung    Wörterbuch    Literaturverzeichnis    IX    XIII    275    Verzeichnis der Abkürzungen    a) Philologische Abkürzungen    aaram.  Adj.  Adv.  afghan.  afrz.  ägypt.  ägypt.-ar.  ahd.  ähnl.  air.  aind.  ait.  akk.  act. Pt.  alban.  ap.   ar.  aram.  arm,  ass.  assyr.  aw.   bab.   Bd.   Bed.  Bez.  bibl.-aram.  bot.  bulg.  byz.  cech,  chald.  ch.-pal,    comp.  d.    altaramäisch  Adjektiv   Adverb  afghani
--
```


## [2026-10-17T00:33:43.045Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/s568.py\npython3 $S AFA.txt '(?i)z.nn.r|zonar' 300 2; python3 $S AFM.txt 'زنار' 300 2; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe-private/data/verification/sources/refs_online.json'));print(json.dumps(d['BQT'],ensure_ascii=False)[:2500]);print(json.dumps(d['MON'],ensure_ascii=False)[:1500])\""
}
```


### [2026-10-17T00:33:43.486Z] TOOL RESULT

```
NO HIT AFA.txt (?i)z.nn.r|zonar
NO HIT AFM.txt زنار
{"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.", "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)", "/home/sfmqrb/
{"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).", "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf", "/home/sfmq
```


## [2026-10-17T00:33:45.199Z] AGENT

Let me fetch the BQT pages with the tool.


## [2026-10-17T00:33:46.383Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for p in 556 660 1033 1291; do echo \"=== BQT:$p\"; timeout 300 python3 tools/ref_page.py BQT:$p 2>&1 | head -80; done",
 "timeout": 600000
}
```


### [2026-10-17T00:33:53.678Z] TOOL RESULT

```
=== BQT:556
no scan of BQT covers printed page 556 (see 'scans' in refs_online.json)
=== BQT:660
no scan of BQT covers printed page 660 (see 'scans' in refs_online.json)
=== BQT:1033
no scan of BQT covers printed page 1033 (see 'scans' in refs_online.json)
=== BQT:1291
REF: BQT:1291  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 82  OCR-lang: fas

-و۱۷۹- شملیر
است که کنایه از زبان باشد و بءربی لدان | وبیم مدهوش و بیخبن شده باشد - و شخ ی که
خوانند. ۷ ازو بوی بد آید.
شمع‌زدین لگن «کنایه از خورشید شمکور - باکان بروزن رنجور #شپری
انور باشد - است نزديك بگنجه از ولابت اران ۴ .
است که‌صبح کاذب, باشد- و کنایه ازآقتاب‌ءالمتاب | پای افزار چرمین باشد - و پای افزاری را لیز
هم هست . کوبند که زیر آن ازچرم خام ورویش از ریسمان
شمع صباح » کنابه از خورشد باشد و آنرا چاروق کوبند بتر کی - و درعریی
عالم آراست ۰ بممای فرا کرفتن باشد - و بفتح اول و سکون
شمه صیح ‏ دم رین شیم مان | ثالیهم درعربی بمعنی‌کارهای‌پر! کنده و کارهای جمع
ح‌ اک ۳ | شدمویراکند؟ ت باشد,و ابر ازاشداداست
که کنایه از آفتاب‌باشد. «وپر! مد در وجممعیت باشد وین از اصداداست.
شمع عالمتات مه در ۰ شملخح ۴ « بفتح اوزولام بروزن‌برزخ»
۳ بمعمی شمع صبحجی فا ۵ ۱ ۰ ۱
است که خورشید باشد. بمعنی شلغم باشد؛ و بفتح اول وثالی وسکون‌لام
۹ ۹ و سکن ۹ هم کفته اند ۰
۰ 9 ۳۹ ثملغ ۴ » با غین نقطه‌دار» بروزن‌ومعنی
۴ نک دملخ است که شلغم باشد .
شم مزعفر -کنایه ازبیراعفام شمله - بنتم اول بر وزن (۳) حمله :
ب ۰
شمع بهودی وس کنایه از هم پیچند - وعلاقةٌ دستار را نیز کفته‌اند- ویشم
شراب املی انگوری باشد. اول بممنی تبرشهاپ است ۰ وآن روشناییی‌باشد
شمفند ‎٩‏ < با غین نقطه‌دار (۱) بروزن که شبها درهوا از جانبی بجالب دبگر رود.
فرزند » زلی راکوبند که بفایت بدبوی و کنده شملید ۱- بروزن نهمید . رستنیی‌باشد
ومتعفن باشد وبعرمی لخنا بروزن سرماخوانند. ‏ | کهآ؛را بعربی حلبه کویند بعم حای‌بی قطه(4)
شمفنده ؟ » باغین قطه‌دار(۲)روزن | -وگلی باشد زرد وخوشبوی ؛ وبجای حرف آخر
شرهنده, بعنی شماغنده است که چزهای بد بو نای قرشت ۰( ‌ِ آهده است .
(۱) چك: - قطه دار . (۲) چك ؛ -قطه دار . (۳) چك : بوزن .
زه.م.) ۰ ۴ - رالد: حدودااعالم ص ۰.۹۶ ات شملغ * شلغم («.م.) ۰
8 < سلغ #علفم (هم.) . ‎٩‏ * منبلد )ه.م.) * فتبلیله (وم.) .
۷-ظ: دماین ۳ شملرد («.م )
# همعدان - از : شمع (عر)ل دان ( پونده‌کان وظرف ) ؛ مدرب آن لیز شممدان
جمع شممدانات وشماعدین«دزی ج ۱ص ۹۷۸۸ «تفی»* آلنی که درآن شمم راجا دوند.9ندیل.
```


## [2026-10-17T00:33:57.514Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; find data/verification/sources/refs/ocr/BQT -name '1291*' -o -name '1290*' -o -name '1289*' | head; python3 data/verification/sources/refs/../../../../tools/ref_page.py --help 2>&1 | head -20"
}
```


### [2026-10-17T00:33:57.927Z] TOOL RESULT

```
data/verification/sources/refs/ocr/BQT/1291.png
data/verification/sources/refs/ocr/BQT/1291.txt
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


## [2026-10-17T00:33:59.784Z] TOOL CALL #36: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1291.png"
}
```


### [2026-10-17T00:34:00.294Z] TOOL RESULT

```

```


## [2026-10-17T00:34:00.290Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-10-17T00:34:07.598Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; timeout 300 python3 tools/ref_page.py BQT:1291 --pdf-page 78 --image 2>&1 | head -60",
 "timeout": 400000
}
```


### [2026-10-17T00:34:08.103Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1291.png
REF: BQT:1291  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 82  OCR-lang: fas

-و۱۷۹- شملیر
است که کنایه از زبان باشد و بءربی لدان | وبیم مدهوش و بیخبن شده باشد - و شخ ی که
خوانند. ۷ ازو بوی بد آید.
شمع‌زدین لگن «کنایه از خورشید شمکور - باکان بروزن رنجور #شپری
انور باشد - است نزديك بگنجه از ولابت اران ۴ .
است که‌صبح کاذب, باشد- و کنایه ازآقتاب‌ءالمتاب | پای افزار چرمین باشد - و پای افزاری را لیز
هم هست . کوبند که زیر آن ازچرم خام ورویش از ریسمان
شمع صباح » کنابه از خورشد باشد و آنرا چاروق کوبند بتر کی - و درعریی
عالم آراست ۰ بممای فرا کرفتن باشد - و بفتح اول و سکون
شمه صیح ‏ دم رین شیم مان | ثالیهم درعربی بمعنی‌کارهای‌پر! کنده و کارهای جمع
ح‌ اک ۳ | شدمویراکند؟ ت باشد,و ابر ازاشداداست
که کنایه از آفتاب‌باشد. «وپر! مد در وجممعیت باشد وین از اصداداست.
شمع عالمتات مه در ۰ شملخح ۴ « بفتح اوزولام بروزن‌برزخ»
۳ بمعمی شمع صبحجی فا ۵ ۱ ۰ ۱
است که خورشید باشد. بمعنی شلغم باشد؛ و بفتح اول وثالی وسکون‌لام
۹ ۹ و سکن ۹ هم کفته اند ۰
۰ 9 ۳۹ ثملغ ۴ » با غین نقطه‌دار» بروزن‌ومعنی
۴ نک دملخ است که شلغم باشد .
شم مزعفر -کنایه ازبیراعفام شمله - بنتم اول بر وزن (۳) حمله :
ب ۰
شمع بهودی وس کنایه از هم پیچند - وعلاقةٌ دستار را نیز کفته‌اند- ویشم
شراب املی انگوری باشد. اول بممنی تبرشهاپ است ۰ وآن روشناییی‌باشد
شمفند ‎٩‏ < با غین نقطه‌دار (۱) بروزن که شبها درهوا از جانبی بجالب دبگر رود.
فرزند » زلی راکوبند که بفایت بدبوی و کنده شملید ۱- بروزن نهمید . رستنیی‌باشد
ومتعفن باشد وبعرمی لخنا بروزن سرماخوانند. ‏ | کهآ؛را بعربی حلبه کویند بعم حای‌بی قطه(4)
شمفنده ؟ » باغین قطه‌دار(۲)روزن | -وگلی باشد زرد وخوشبوی ؛ وبجای حرف آخر
شرهنده, بعنی شماغنده است که چزهای بد بو نای قرشت ۰( ‌ِ آهده است .
(۱) چك: - قطه دار . (۲) چك ؛ -قطه دار . (۳) چك : بوزن .
زه.م.) ۰ ۴ - رالد: حدودااعالم ص ۰.۹۶ ات شملغ * شلغم («.م.) ۰
8 < سلغ #علفم (هم.) . ‎٩‏ * منبلد )ه.م.) * فتبلیله (وم.) .
۷-ظ: دماین ۳ شملرد («.م )
# همعدان - از : شمع (عر)ل دان ( پونده‌کان وظرف ) ؛ مدرب آن لیز شممدان
جمع شممدانات وشماعدین«دزی ج ۱ص ۹۷۸۸ «تفی»* آلنی که درآن شمم راجا دوند.9ندیل.
```


## [2026-10-17T00:34:13.108Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; SP=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; pdftoppm -f 78 -l 78 -r 110 -png -singlefile data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf $SP/bqt568-78; command ls $SP | grep 568"
}
```


### [2026-10-17T00:34:13.761Z] TOOL RESULT

```
bqt568-78.png
s568.py
```


## [2026-10-17T00:34:17.246Z] TOOL CALL #39: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt568-78.png"
}
```


### [2026-10-17T00:34:17.274Z] TOOL RESULT

```

```


## [2026-10-17T00:34:23.492Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; SP=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; for p in 80 81; do pdftoppm -f $p -l $p -r 150 -png -singlefile data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf $SP/bqt568-$p; done; tesseract $SP/bqt568-80.png - -l fas 2>/dev/null | head -3; tesseract $SP/bqt568-81.png - -l fas 2>/dev/null | head -3"
}
```


### [2026-10-17T00:34:24.963Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:34:30.556Z] TOOL CALL #41: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt568-80.png"
}
```


### [2026-10-17T00:34:30.583Z] TOOL RESULT

```

```


## [2026-10-17T00:34:36.529Z] TOOL CALL #42: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt568-81.png"
}
```


### [2026-10-17T00:34:36.544Z] TOOL RESULT

```

```


## [2026-10-17T00:34:42.608Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; SP=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; pdftoppm -f 82 -l 82 -r 150 -png -singlefile data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf $SP/bqt568-82"
}
```


### [2026-10-17T00:34:43.406Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:34:47.279Z] TOOL CALL #44: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt568-82.png"
}
```


### [2026-10-17T00:34:47.305Z] TOOL RESULT

```

```


## [2026-10-17T00:34:56.642Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/s568.py\npython3 - <<'EOF'\nimport re\nfor f in ['BQT_v1_pages.txt','BQT_v2_pages.txt']:\n    t=open(f,errors='ignore').read().split('\\f')\n    for i,x in enumerate(t):\n        m=re.search(r'\\[pdf page (\\d+)\\]',x)\n        nums=re.findall(r'[-—]\\s*([۰-۹]{3,4})\\s*[-—]',x[:300])\n        for kw in ['yâmak','yāmak','yamak','zônê','zone','zunn','پاجامه','جامه‌دان','جامه دان','زنار']:\n            if kw in x:\n                print(f,i,m and m.group(1),nums[:1],kw)\nEOF"
}
```


### [2026-10-17T00:34:57.113Z] TOOL RESULT

```
BQT_v1_pages.txt 489 None [] زنار
BQT_v2_pages.txt 15 None [] جامه دان
BQT_v2_pages.txt 73 None [] جامه دان
BQT_v2_pages.txt 115 None [] زنار
BQT_v2_pages.txt 118 None [] جامه دان
BQT_v2_pages.txt 147 None [] زنار
BQT_v2_pages.txt 248 None [] زنار
BQT_v2_pages.txt 495 None [] زنار
```


## [2026-10-17T00:35:01.530Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',errors='ignore').read().split('\\f')\nfor i in (15,16,17,18):\n    x=t[i]; print('=== leaf',i, x[:200].replace('\\n',' '))\n    for m in re.finditer('جامه',x):\n        print('  >>',x[max(0,m.start()-200):m.start()+300].replace('\\n',' '))\nEOF"
}
```


### [2026-10-17T00:35:01.928Z] TOOL RESULT

```
=== leaf 15  ‫مدهرلل زدن‬  ‫و ابر وآنچه روی آفاب را بیوشاند ‪ -‬وباسطلاح‬      ‫هت ‪-‬وجام وصراحیو کوزه وکدوی شراب‌را‬ ‫سالکان عبارت ار بدن‌آدمی باشد چه جم لبای‬                                          ‫دز کفته‌
  >>  کوزه وکدوی شراب‌را‬ ‫سالکان عبارت ار بدن‌آدمی باشد چه جم لبای‬                                          ‫دز کفته‌اند ‪۰ ۴‬‬ ‫جان است » و خورشید در عرف ایشان روج‬   ‫ومردمك دیده را همکقتهاید ‪¥.‬‬   ‫جامه دان » بروزن لامعان‪ .‬صندوق‬                                    ‫ت‬   ‫حیوالی‬                                                                                    ‫گریختن باد‪.‬‬ ‫و خانه‌ای که رخوت پوشیدلی وقیر پوشیدلی در‬        ‫رخوت پوشیدلی وغیر پوشیدلی ودوخته ولادوخته‬                       
  >>                                       ‫گریختن باد‪.‬‬ ‫و خانه‌ای که رخوت پوشیدلی وقیر پوشیدلی در‬        ‫رخوت پوشیدلی وغیر پوشیدلی ودوخته ولادوخته‬                                 ‫آن بگنار ند ‪.‬‬ ‫جامه دنریلزدت «کنایه ازمزت‬                      ‫جامه خورشید » کنابه از زمین‬                            ‫مواتم داشتن باشد ‪.‬‬   ‫امت ‪ -‬وب رکه درختاترا دز گوبند ‪ -‬وغبار‪-‬‬                  ‫‪ ۶‬ای‌مردان بکوشید تا جامة زدان نپوشد ‪« » .‬کلتان ‪. ۲ ۰۲‬‬               ‫‪۱‬‬      ‫«جامه" مانشد کو
  >> .‬‬ ‫و خانه‌ای که رخوت پوشیدلی وقیر پوشیدلی در‬        ‫رخوت پوشیدلی وغیر پوشیدلی ودوخته ولادوخته‬                                 ‫آن بگنار ند ‪.‬‬ ‫جامه دنریلزدت «کنایه ازمزت‬                      ‫جامه خورشید » کنابه از زمین‬                            ‫مواتم داشتن باشد ‪.‬‬   ‫امت ‪ -‬وب رکه درختاترا دز گوبند ‪ -‬وغبار‪-‬‬                  ‫‪ ۶‬ای‌مردان بکوشید تا جامة زدان نپوشد ‪« » .‬کلتان ‪. ۲ ۰۲‬‬               ‫‪۱‬‬      ‫«جامه" مانشد کوزه باشد که شراب در وی کنند ‪ .‬منجيك ( ترمذی )کوبت
  >>                     ‫مواتم داشتن باشد ‪.‬‬   ‫امت ‪ -‬وب رکه درختاترا دز گوبند ‪ -‬وغبار‪-‬‬                  ‫‪ ۶‬ای‌مردان بکوشید تا جامة زدان نپوشد ‪« » .‬کلتان ‪. ۲ ۰۲‬‬               ‫‪۱‬‬      ‫«جامه" مانشد کوزه باشد که شراب در وی کنند ‪ .‬منجيك ( ترمذی )کوبت ‪:‬‬               ‫‪۴‬‬       ‫بوهم روزه بدو بشکند دل ابدال ‪.‬‬              ‫که چون رجامه بجام اتدررن فرو ریزی‬       ‫>‪.‬‬    ‫د لفت فرس ‪۷۸‬‬   ‫‪۶ - ۴‬یس مأمون آن روز (عروسی) جامه خانه‌ها عرض کردن خواست و ازآن‌هزار‬ ‫قباءاطلیمعد
  >> » .‬کلتان ‪. ۲ ۰۲‬‬               ‫‪۱‬‬      ‫«جامه" مانشد کوزه باشد که شراب در وی کنند ‪ .‬منجيك ( ترمذی )کوبت ‪:‬‬               ‫‪۴‬‬       ‫بوهم روزه بدو بشکند دل ابدال ‪.‬‬              ‫که چون رجامه بجام اتدررن فرو ریزی‬       ‫>‪.‬‬    ‫د لفت فرس ‪۷۸‬‬   ‫‪۶ - ۴‬یس مأمون آن روز (عروسی) جامه خانه‌ها عرض کردن خواست و ازآن‌هزار‬ ‫قباءاطلیمعدئی و ملکی و طمیم و لیج و ممزج و مقراضی وا کون هیچ پندید ‪٩٥ .‬‏ چهار‬   ‫تگاهداری جلمه ‪۳‬‬    ‫»جامه‌دار ‪ -‬مامور‬                                     
  >> جيك ( ترمذی )کوبت ‪:‬‬               ‫‪۴‬‬       ‫بوهم روزه بدو بشکند دل ابدال ‪.‬‬              ‫که چون رجامه بجام اتدررن فرو ریزی‬       ‫>‪.‬‬    ‫د لفت فرس ‪۷۸‬‬   ‫‪۶ - ۴‬یس مأمون آن روز (عروسی) جامه خانه‌ها عرض کردن خواست و ازآن‌هزار‬ ‫قباءاطلیمعدئی و ملکی و طمیم و لیج و ممزج و مقراضی وا کون هیچ پندید ‪٩٥ .‬‏ چهار‬   ‫تگاهداری جلمه ‪۳‬‬    ‫»جامه‌دار ‪ -‬مامور‬                                             ‫مقاله »‪. > ۲‬‬                                                                      
  >> د لفت فرس ‪۷۸‬‬   ‫‪۶ - ۴‬یس مأمون آن روز (عروسی) جامه خانه‌ها عرض کردن خواست و ازآن‌هزار‬ ‫قباءاطلیمعدئی و ملکی و طمیم و لیج و ممزج و مقراضی وا کون هیچ پندید ‪٩٥ .‬‏ چهار‬   ‫تگاهداری جلمه ‪۳‬‬    ‫»جامه‌دار ‪ -‬مامور‬                                             ‫مقاله »‪. > ۲‬‬                                                                         ‫مش‬                   ‫معرب و‬   ‫فف آنه جمدار» « دزی‪»۱:۲۱۲‬؛ وآن بگروهی‌ازممالك محافظط سلطان(مسر) اطلاق‬  ‫« دائرة الممارف اعلام ‪:‬‬           
=== leaf 16  ‫سین وس‬                                                                       ‫‪۳‬‬                                                  ‫حاهة سچر ‪ -‬کنابه ازآتابات‪- ۱‬‬                      ‫چاك کردن
  >> ‫سین وس‬                                                                       ‫‪۳‬‬                                                  ‫حاهة سچر ‪ -‬کنابه ازآتابات‪- ۱‬‬                      ‫چاك کردن جامه باشد ‪.‬‬                       ‫کونایه آزباد صبا هم هست ‪.‬‬ ‫جامه فطر ان = جامه‌سیاهی‌را گوشد‬                ‫جامة عبد ه کنابه اژجامه و قبای‬                ‫که در عاشورا وتعزتها پوشند ‪.‬‬     ‫بهار را نیز‬   ‫فهاهوای‬                                                                     ‫وکل
  >>            ‫‪۳‬‬                                                  ‫حاهة سچر ‪ -‬کنابه ازآتابات‪- ۱‬‬                      ‫چاك کردن جامه باشد ‪.‬‬                       ‫کونایه آزباد صبا هم هست ‪.‬‬ ‫جامه فطر ان = جامه‌سیاهی‌را گوشد‬                ‫جامة عبد ه کنابه اژجامه و قبای‬                ‫که در عاشورا وتعزتها پوشند ‪.‬‬     ‫بهار را نیز‬   ‫فهاهوای‬                                                                     ‫وکل‬                                                                   
  >> ‬‬                                                  ‫حاهة سچر ‪ -‬کنابه ازآتابات‪- ۱‬‬                      ‫چاك کردن جامه باشد ‪.‬‬                       ‫کونایه آزباد صبا هم هست ‪.‬‬ ‫جامه فطر ان = جامه‌سیاهی‌را گوشد‬                ‫جامة عبد ه کنابه اژجامه و قبای‬                ‫که در عاشورا وتعزتها پوشند ‪.‬‬     ‫بهار را نیز‬   ‫فهاهوای‬                                                                     ‫وکل‬                                                                       ‫ششدک‪-‬و‬
  >> هة سچر ‪ -‬کنابه ازآتابات‪- ۱‬‬                      ‫چاك کردن جامه باشد ‪.‬‬                       ‫کونایه آزباد صبا هم هست ‪.‬‬ ‫جامه فطر ان = جامه‌سیاهی‌را گوشد‬                ‫جامة عبد ه کنابه اژجامه و قبای‬                ‫که در عاشورا وتعزتها پوشند ‪.‬‬     ‫بهار را نیز‬   ‫فهاهوای‬                                                                     ‫وکل‬                                                                       ‫ششدک‪-‬و‬‫سرخ با‬ ‫جامه نخچوانی ‏ مقرلات ولندره‬                
  >>  ‪.‬‬     ‫بهار را نیز‬   ‫فهاهوای‬                                                                     ‫وکل‬                                                                       ‫ششدک‪-‬و‬‫سرخ با‬ ‫جامه نخچوانی ‏ مقرلات ولندره‬                                               ‫گونند؟ ‪.‬‬                           ‫ومانند! تراکونند‪#.‬‬     ‫جامةغوك ‪ -‬چیزی باد سبز شه‬ ‫»یر وزن نان » روح حیوالی‬        ‫جات‬             ‫بارش که درروی آب بهم میرسد ‪ -‬و جوی آب‬ ‫باشد ‪ - ۴‬وملاح جنگ را لىز کفته‌
=== leaf 17 ‫چاندار‬                                                                                            ‫هو‬  ‫جانا نه‪ » ۱‬بر وزن کاشانه‪ ,‬کتابه از | روح اعظم است ‪ -‬واشاره بحق تعالی هم هست‬ ‫ونابه از 
=== leaf 18   ‫"‪٩‬‏چحص‬   ‫سب ‪۵‬‬                                                                                                   ‫جاندارو‬                         ‫وآب حیات را هم میگویند ‪.‬‬           ‫همآم
```


## [2026-10-17T00:35:10.346Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',errors='ignore').read().split('\\f')\nfor i in (13,14,15,73,115,118,147):\n    x=t[i]\n    lat=re.findall(r'[A-Za-zâāêîûôšžčğ\\.\\-]{4,}',x)\n    print(i,lat[:60])\nEOF"
}
```


### [2026-10-17T00:35:10.881Z] TOOL RESULT

```
13 []
14 ['natinêl', 'natfug']
15 []
73 []
115 []
118 ['dnamuc', 'kîmêc']
147 []
```


## [2026-10-17T00:35:15.691Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(json.dumps(d['BQT'].get('scans'),ensure_ascii=False)); print(d['BQT'].get('page_offset'))\"; command ls data/verification/sources/refs/pageimg | head; command ls data/verification/sources/refs/ocr/BQT | grep -E '^(55|56|66|103)' "
}
```


### [2026-10-17T00:35:16.237Z] TOOL RESULT

```
[{"volume": "3", "file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf", "first_printed": 1208, "last_printed": 1925, "pdf_offset": -1205, "page_map": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json", "lang": "fas", "ocr_text": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt", "ocr_note": "689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py"}, {"volume": "4", "file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf", "first_printed": 1920, "last_printed": 2475, "pdf_offset": -1917, "lang": "fas", "offset_note": "printed = pdf+1917, checked at pdf 150 and 500", "ocr_text": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt"}, {"volume": "5", "file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf", "first_printed": 1, "last_printed": 290, "pdf_offset": 5, "lang": "fas", "note": "vol 5 = ta'liqat (addenda) with its own pagination 1-290; cite as BQT5:<page>. Plain BQT:<n> with n<1208 refers to vols 1-2 (OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt), not to this scan.", "ocr_text": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt", "requires_volume": true}]
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
bqt_v3_p150-150.png
bqt_v3_p600-600.png
bqt_v4_p150-150.png
bqt_v4_p500-500.png
bqt_v5_p150-150.png
bqt_v5_p250-250.png
bqt_v5_p30-030.png
bqt_v5_p8-008.png
irn_p100-100.png
irn_p101-101.png
103.vision.txt
```


## [2026-10-17T00:35:23.777Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',errors='ignore').read().split('\\f')\nfor i in (13,14,117,118):\n    x=t[i]\n    for m in re.finditer('جامه|چمدان|یامك|یامک',x):\n        print(i,'>>',x[max(0,m.start()-150):m.start()+250].replace('\\n',' ').replace('‫','').replace('‬',''))\n    print('======')\nEOF"
}
```


### [2026-10-17T00:35:24.154Z] TOOL RESULT

```
======
14 >> اکوبند » وآن خانه‌است راب و وظیفه آونچه بملازم ون وکر وغلام‌دهند                                 که در ودبوارآ ترا ششه بندی کرده باشنف ‪. بجپت جامه بها ‪ -وخوراك ‪ -و فتبلةً تفنگم                                 جام سچر هکتس‌ابه ازآفتابعالمتاب ودردی پیاله را یز کفته‌اند و»بسکون میم هم                                                                         لت ‪.                    
14 >>    لت ‪.                                                  آمده است ‪#.                                                                         جامه بتاسین ہی تقطه بروزن‌خالسه» جامگی خوار = مردم علوفه‌داررا                                           باقلای قبطی را کوبند » و آن در مصر بیار  شرابخوارهم هت         و کنانه از مردم             گونند        (‪)۱     میشود و در آبپای 
14 >>       یعنی بگوید ‪.                                                                            اد بر وزن نامه » بارچة بافتة                   جامه =                       جامقول‪ -باغینقطەدارېروزنزاغنول‪. نادوخته راکوبند" ‪ -وبمعنی‌قبای پوشیدنی هم                                                       حرامزاده را کوبند ‪۰                                                           
14 >> ‪.             ‪۰        خود   تات سرجای        ت                                                            ا ت    امک          صخرة جامه پروزنکاملة ‪.    ‪- ۱    ‪« - ۳پدر من ( معزی ) امیر                                 ‪ - ۲ا ‪:ز جلمه ( جاماك ) ‪ +ی (سبت ) ‪.   اجراء پدر بمن تحوبل                 یں جامگی و           »‪0     مراسلطان ملك‌شاه سیر     الشم
======
======
118 >> ج اص ‪ ۷۸۷ورك ‪ :چا                          ‪( ۰يسوند نست) » رك‪ :چشمه‪.         از چمش( = چشم) ‪+                                   ‪ #چمدان ‪ -بفتح ارول ودوم ‪ :دزی<دان‌ممرب را از                                                                        سم                                                                                                     ز‪٩ص‪۵ف‪۹ح‏هٌ       
118 >>                                                                                   ز‪٩ص‪۵ف‪۹ح‏هٌ                                  فلرسی جامدان ( جامه دان) ماوق میداند «دزی حاص ‪.» ۲۱۲                                  را از روسی عارت مىداند       کرستنمن کلم استی ‪02000۳6                                  ؛ صندوق چرمن که جامه و اثیاء دیگر در                   دك ‪ .است              
118 >>  ۲۱۲                                  را از روسی عارت مىداند       کرستنمن کلم استی ‪02000۳6                                  ؛ صندوق چرمن که جامه و اثیاء دیگر در                   دك ‪ .است                                                          آن هند ‪ .رکه‪ :چرمدان و خرمدان ‪. 
======
```


## [2026-10-17T00:35:31.509Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; for n in 14 15; do curl -sL -m 60 -o bqtv2-568-n$n.jpg \"https://archive.org/download/borhan-ghate-v2/page/n${n}_w900.jpg\"; file bqtv2-568-n$n.jpg; done"
}
```


### [2026-10-17T00:35:37.768Z] TOOL RESULT

```
bqtv2-568-n14.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 1285x1985, components 1
bqtv2-568-n15.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 1285x1985, components 1
```


## [2026-10-17T00:35:41.702Z] TOOL CALL #51: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqtv2-568-n15.jpg"
}
```


### [2026-10-17T00:35:41.726Z] TOOL RESULT

```

```


## [2026-10-17T00:35:45.326Z] AGENT

Leaf 15 = p.557, so p.556 = leaf 14.


## [2026-10-17T00:35:46.627Z] TOOL CALL #52: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqtv2-568-n14.jpg"
}
```


### [2026-10-17T00:35:46.645Z] TOOL RESULT

```

```


## [2026-10-17T00:35:55.537Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; for n in 117 490; do curl -sL -m 60 -o bqtv2-568-n$n.jpg \"https://archive.org/download/borhan-ghate-v2/page/n${n}_w900.jpg\"; done; python3 -c \"\nt=open('/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt',errors='ignore').read().split('\\f')\nimport re\nfor i in range(486,497):\n  if 'زنار' in t[i] or 'زنّار' in t[i]: print(i)\n\""
}
```


### [2026-10-17T00:35:59.419Z] TOOL RESULT

```
495
```


## [2026-10-17T00:36:04.768Z] TOOL CALL #54: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqtv2-568-n117.jpg"
}
```


### [2026-10-17T00:36:04.785Z] TOOL RESULT

```

```


## [2026-10-17T00:36:11.789Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; for n in 118 495; do curl -sL -m 60 -o bqtv2-568-n$n.jpg \"https://archive.org/download/borhan-ghate-v2/page/n${n}_w900.jpg\"; done; ls -la bqtv2-568-n118.jpg bqtv2-568-n495.jpg 2>/dev/null || command ls -la"
}
```


### [2026-10-17T00:36:15.051Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--  261k sfmqrb 16 Oct 20:36  bqtv2-568-n118.jpg
.rw-r--r--  257k sfmqrb 16 Oct 20:36  bqtv2-568-n495.jpg
```


## [2026-10-17T00:36:19.145Z] TOOL CALL #56: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqtv2-568-n118.jpg"
}
```


### [2026-10-17T00:36:19.161Z] TOOL RESULT

```

```


## [2026-10-17T00:36:25.611Z] TOOL CALL #57: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqtv2-568-n495.jpg"
}
```


### [2026-10-17T00:36:25.633Z] TOOL RESULT

```

```


## [2026-10-17T00:36:34.488Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,40p tools/fetch_source.py | head -50"
}
```


### [2026-10-17T00:36:34.812Z] TOOL RESULT

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
```


## [2026-10-17T00:36:42.069Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; F=tools/fetch_source.py\nfor u in \"https://en.wiktionary.org/wiki/جامه\" \"https://en.wiktionary.org/wiki/pajama\" \"https://en.wiktionary.org/wiki/чемодан\" \"https://en.wiktionary.org/wiki/چمدان\" \"https://en.wiktionary.org/wiki/زنار\" \"https://en.wiktionary.org/wiki/زنار\" \"https://en.wiktionary.org/wiki/ζώνη\" \"https://en.wiktionary.org/wiki/zone\" \"https://en.wiktionary.org/wiki/شما\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/jūz\" \"https://en.wiktionary.org/wiki/you\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yeh₃s-\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yū́\" \"https://www.etymonline.com/word/pajamas\" \"https://www.etymonline.com/word/you\" \"https://www.etymonline.com/word/zone\" \"https://en.wiktionary.org/wiki/پیژامه\" \"https://en.wiktionary.org/wiki/pyjama\" \"https://en.wiktionary.org/wiki/ζωνάριον\" \"https://en.wiktionary.org/wiki/پاجامه\"; do python3 $F \"$u\" --note \"page 568, roots Yôs / Yu: Wiktionary/Etymonline check\" 2>&1 | tail -1; done",
 "timeout": 400000
}
```


### [2026-10-17T00:36:52.889Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/af8af7526e6843a4.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/0f93fa9310ba1c07.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/023ad1fde20701b6.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/70e4aeaca7d94920.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/44d22a1627092c83.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/44d22a1627092c83.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/4867e50bbfb9ec32.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/88697d8941b45d67.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/97c31b225a1f8218.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/28695b63acddb057.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/69d1baa690767ac6.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f8581da3b479b234.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/11e08f1bf10d111e.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ba31b0c49580744c.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/bfc3b37ce450b95c.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ca25ca363ef6fb3f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2748a4fbd796d5c5.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/1c65af0c8088a0e3.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e0ddd3d5a8571f36.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/592136221dfef068.txt
```


## [2026-10-17T00:36:59.010Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in af8af7526e6843a4 0f93fa9310ba1c07 023ad1fde20701b6 70e4aeaca7d94920 44d22a1627092c83 97c31b225a1f8218 2748a4fbd796d5c5 592136221dfef068 e0ddd3d5a8571f36; do echo \"##### $f $(wc -c <$f.txt)\"; python3 - $f.txt <<'EOF'\nimport sys,re\nt=open(sys.argv[1]).read()\nfor m in re.finditer(r'Etymology',t):\n    print(t[m.start():m.start()+700].replace('\\n',' ')); print('..')\n    break\nEOF\ndone"
}
```


### [2026-10-17T00:36:59.745Z] TOOL RESULT

```
##### af8af7526e6843a4 6078
Etymology    1.2   Noun    1.2.1   Related terms    1.3   Further reading    2   Persian    Toggle Persian subsection    2.1   Etymology    2.2   Pronunciation    2.3   Noun    2.3.1   Derived terms    2.3.2   Descendants    2.4   References    Toggle the table of contents    جامه    10 languages    Azərbaycanca   فارسی   Français   Magyar   Kurdî   Malagasy   پښتو   Русский   Türkçe   中文    Entry    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions   Read    Edit    View history    General   What links here   Related changes   Upload file   Permanent link   Page information   Cite this page   Get shortened URL    Print/export   Creat
..
##### 0f93fa9310ba1c07 4688
Etymology    3.2   Noun    3.2.1   Derived terms    3.3   Verb    3.4   Further reading    4   Swahili    Toggle Swahili subsection    4.1   Etymology    4.2   Noun    Toggle the table of contents    pajama    8 languages    Français   日本語   한국어   Malagasy   Polski   Kiswahili   ไทย   中文    Entry    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions   Read    Edit    View history    General   What links here   Related changes   Upload file   Permanent link   Page information   Cite this page   Get shortened URL    Print/export   Create a book   Download as PDF   Printable version    In other projects   Appearance   move to sidebar   hi
..
##### 023ad1fde20701b6 10923
Etymology    1.2   Noun    2   Mongolian    Toggle Mongolian subsection    2.1   Etymology    2.2   Pronunciation    2.3   Noun    2.3.1   Declension    3   Russian    Toggle Russian subsection    3.1   Alternative forms    3.2   Etymology    3.3   Pronunciation    3.4   Noun    3.4.1   Declension    3.4.2   Derived terms    3.4.3   Related terms    3.4.4   Descendants    3.5   Further reading    4   Ukrainian    Toggle Ukrainian subsection    4.1   Etymology    4.2   Pronunciation    4.3   Noun    4.3.1   Declension    4.4   References    Toggle the table of contents    чемодан    21 languages    Čeština   Esperanto   Eesti   Suomi   Français   Magyar   Ido   Íslenska   日本語   한국어   Кыргызча
..
##### 70e4aeaca7d94920 3736
Etymology    1.3   Pronunciation    1.4   Noun    Toggle the table of contents    چمدان    8 languages    فارسی   Na Vosa Vakaviti   Français   Bahasa Indonesia   Kurdî   Malagasy   Nederlands   Русский    Entry    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions   Read    Edit    View history    General   What links here   Related changes   Upload file   Permanent link   Page information   Cite this page   Get shortened URL    Print/export   Create a book   Download as PDF   Printable version    In other projects   Appearance   move to sidebar   hide    From Wiktionary, the free dictionary   Persian  [ edit ]    Alternative forms  [
..
##### 44d22a1627092c83 9576
Etymology    1.3   Pronunciation    1.4   Noun    1.4.1   Usage notes    1.4.2   Declension    1.4.3   Derived terms    1.4.4   Descendants    1.5   References    2   Persian    Toggle Persian subsection    2.1   Etymology    2.2   Pronunciation    2.3   Noun    2.4   Further reading    Toggle the table of contents    زنار    7 languages    فارسی   Magyar   Malagasy   Polski   پښتو   Русский   سرائیکی    Entry    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions   Read    Edit    View history    General   What links here   Related changes   Upload file   Permanent link   Page information   Cite this page   Get shortened URL    Print/e
..
##### 97c31b225a1f8218 6983
Etymology 1    1.1.1   Verb    1.2   Etymology 2    1.2.1   Verb    2   Persian    Toggle Persian subsection    2.1   Etymology    2.2   Pronunciation    2.3   Pronoun    2.3.1   Descendants    2.4   See also    2.5   References    Toggle the table of contents    شما    10 languages    العربية   فارسی   Français   Magyar   한국어   Kurdî   Malagasy   Nederlands   Русский   中文    Entry    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions   Read    Edit    View history    General   What links here   Related changes   Upload file   Permanent link   Page information   Cite this page   Get shortened URL    Print/export   Create a book   Downl
..
##### 2748a4fbd796d5c5 3364
Etymology    1.3   Pronunciation    1.4   Noun    Toggle the table of contents    پیژامه    4 languages    فارسی   Kurdî   Malagasy   Русский    Entry    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions   Read    Edit    View history    General   What links here   Related changes   Upload file   Permanent link   Page information   Cite this page   Get shortened URL    Print/export   Create a book   Download as PDF   Printable version    In other projects   Appearance   move to sidebar   hide    From Wiktionary, the free dictionary   Persian  [ edit ]    Alternative forms  [ edit ]    پیژاما ( pižâmâ ) , پیجامه ( pijâme )    Etymology
..
##### 592136221dfef068 6630
Etymology    1.2   Noun    1.2.1   Descendants    1.3   Further reading    2   Persian    Toggle Persian subsection    2.1   Alternative forms    2.2   Etymology    2.3   Pronunciation    2.4   Noun    2.4.1   Related terms    2.4.2   Descendants    2.5   Further reading    Toggle the table of contents    پاجامه    3 languages    فارسی   Malagasy   Türkçe    Entry    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions   Read    Edit    View history    General   What links here   Related changes   Upload file   Permanent link   Page information   Cite this page   Get shortened URL    Print/export   Create a book   Download as PDF   Print
..
##### e0ddd3d5a8571f36 4611
Etymology    1.2   Pronunciation    1.3   Noun    1.3.1   Declension    1.3.2   Descendants    1.4   Further reading    Toggle the table of contents    ζωνάριον    Not in other languages    Entry    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions   Read    Edit    View history    General   What links here   Related changes   Upload file   Permanent link   Page information   Cite this page   Get shortened URL    Print/export   Create a book   Download as PDF   Printable version    In other projects   Appearance   move to sidebar   hide    From Wiktionary, the free dictionary   Ancient Greek  [ edit ]    Etymology  [ edit ]    From ζώ
..
```


## [2026-10-17T00:37:05.542Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in af8af7526e6843a4 0f93fa9310ba1c07 023ad1fde20701b6 70e4aeaca7d94920 44d22a1627092c83 97c31b225a1f8218 2748a4fbd796d5c5 592136221dfef068 e0ddd3d5a8571f36 4867e50bbfb9ec32 28695b63acddb057 f8581da3b479b234 11e08f1bf10d111e; do echo \"##### $f\"; python3 - $f.txt <<'EOF'\nimport sys,re\nt=open(sys.argv[1]).read()\ni=t.find('From Wiktionary, the free dictionary')\ns=t[i:] if i>=0 else t\nfor m in re.finditer(r'Etymology[^\\n]{0,20}\\[ edit \\]',s):\n    print(s[m.start():m.start()+650].replace('\\n',' ')); print('..')\nEOF\ndone 2>&1 | cut -c1-900"
}
```


### [2026-10-17T00:37:06.642Z] TOOL RESULT

```
##### af8af7526e6843a4
##### 0f93fa9310ba1c07
##### 023ad1fde20701b6
##### 70e4aeaca7d94920
##### 44d22a1627092c83
##### 97c31b225a1f8218
##### 2748a4fbd796d5c5
##### 592136221dfef068
##### e0ddd3d5a8571f36
##### 4867e50bbfb9ec32
##### 28695b63acddb057
##### f8581da3b479b234
##### 11e08f1bf10d111e
```


## [2026-10-17T00:37:13.036Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; python3 - <<'EOF'\nimport re\nfor f in 'af8af7526e6843a4 0f93fa9310ba1c07 023ad1fde20701b6 70e4aeaca7d94920 44d22a1627092c83 97c31b225a1f8218 2748a4fbd796d5c5 592136221dfef068 e0ddd3d5a8571f36 4867e50bbfb9ec32 28695b63acddb057 f8581da3b479b234 11e08f1bf10d111e'.split():\n    t=open(f+'.txt').read()\n    i=t.find('From Wiktionary, the free dictionary')\n    s=re.sub(r'\\s+',' ',t[i:])\n    print('#####',f)\n    for m in re.finditer(r'Etymology( \\d)? \\[ edit \\]',s):\n        print('  ',s[m.start():m.start()+600]); \nEOF"
}
```


### [2026-10-17T00:37:13.612Z] TOOL RESULT

```
##### af8af7526e6843a4
   Etymology [ edit ] Etymology tree Middle Persian yʾmk' Classical Persian جامه ( jâme ) bor. Ottoman Turkish جامه Borrowed from Classical Persian جامه ( jâme ) . Noun [ edit ] جامه • ( came ) a cloth, any woven material; a length of cloth a sheet a wrapper, or a wrap a garment, raiment a cup, bowl, goblet Related terms [ edit ] جامه‌شوی ( cameşuy , “ laundry; laundryman ” ) جماشیر ( çamaşır , “ underclothes; linen; laundry ” ) پاجامه ( pacame ) Further reading [ edit ] Redhouse, James W. ( 1890 ), “ جامه ”, in A Turkish and English Lexicon ‎ [1] , Constantinople: A. H. Boyajian, page 637 Persia
   Etymology [ edit ] Inherited from Middle Persian yʾmk' ( jāmag ) , from Proto-Iranian *yām- ( “ to hold ” ) , from Proto-Indo-Iranian *yámas , *yam- ( “ to hold ” ) , from Proto-Indo-European *yém-o-s , from *yem- ( “ to hold ” ) , Northern Luri جۆمںە ( cømə ) , see also Sanskrit यम् ( yam , “ to sustain ” ) . Compare Old Armenian վարշամակ ( varšamak ) . Pronunciation [ edit ] ( Classical Persian ) IPA ( key ) : /d͡ʒaː.ˈma/ ( Dari, formal ) IPA ( key ) : [d͡ʒɑː.má] ( Dari, formal ) IPA ( key ) : [d͡ʒɑː.má] ( Kabuli ) IPA ( key ) : [d͡ʒɑː.má] ( Hazaragi ) IPA ( key ) : [d͡ʒɔː.má] ( Iran, formal
##### 0f93fa9310ba1c07
   Etymology [ edit ] From pa- +‎ jama . Noun [ edit ] pajama ( Lontara spelling ᨄᨍᨆ or 𑻣𑻪𑻥 , definite pajamaya ) worker ; craftsman ; someone who works on something Derived terms [ edit ] compounds pajama ballaʼ pajama baraʼ pajama biseang pajama intang pajama jama Verb [ edit ] pajama ( Lontara spelling ᨄᨍᨆ or 𑻣𑻪𑻥 ) ( transitive , causative ) to make someone work ; to put to work; to employ Further reading [ edit ] Cense, A. A. ( 1979 ), Makassaars-Nederlands woordenboek [ Makasar-Dutch dictionary ], 's-Gravenhage: Martinus Nijhoff, →ISBN , page 171 Swahili [ edit ] Etymology [ edit ] (This ety
   Etymology [ edit ] (This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium . Particularly: “Hindi or English?”) Noun [ edit ] pajama class IX ( plural pajama class X ) pyjamas Retrieved from " https://en.wiktionary.org/w/index.php?title=pajama&oldid=91358238 " Categories : English 3-syllable words English terms with IPA pronunciation English lemmas English nouns American English English terms with usage examples English terms with rare senses English terms with quotations Japanese non-lemma forms Japanese romanizations Makasar terms prefixed with 
##### 023ad1fde20701b6
   Etymology [ edit ] From Russian чемода́н ( čemodán ) . Noun [ edit ] чемодан • ( cemodan ) ( Arabic spelling چەمودان ) suitcase Mongolian [ edit ] Mongolian Cyrillic ᠴᠧᠮᠣᠳᠠᠨ čēmodan чемодан čemodan Etymology [ edit ] Borrowed from Russian чемода́н m inan sg ( čemodán ) , from Classical Persian جامه‌دان sg ( jāma-dān ) . Pronunciation [ edit ] IPA ( key ) : [t͡ʃʰe̝m.täˑɴ̟] Hyphenation: че‧мо‧дан Noun [ edit ] чемодан • ( čemodan ) suitcase Synonym: авдар ( avdar ) Declension [ edit ] This noun needs an inflection-table template . Russian [ edit ] Russian Wikipedia has an article on: чемодан Wik
   Etymology [ edit ] Borrowed from Russian чемода́н m inan sg ( čemodán ) , from Classical Persian جامه‌دان sg ( jāma-dān ) . Pronunciation [ edit ] IPA ( key ) : [t͡ʃʰe̝m.täˑɴ̟] Hyphenation: че‧мо‧дан Noun [ edit ] чемодан • ( čemodan ) suitcase Synonym: авдар ( avdar ) Declension [ edit ] This noun needs an inflection-table template . Russian [ edit ] Russian Wikipedia has an article on: чемодан Wikipedia ru Alternative forms [ edit ] чемода́нъ ( čemodán ) — pre-1918 spelling чекмода́н ( čekmodán ) — colloquial or humorous Etymology [ edit ] Via a Turkic medium, from Persian جامه‌دان ( jâme-dâ
   Etymology [ edit ] Via a Turkic medium, from Persian جامه‌دان ( jâme-dân , “ suitcase ” ) , from Persian جامه (whence also English pajamas , Russian пижа́ма ( pižáma ) ). Note that this Russian term has later become the source of re-borrowing into modern Persian چمدان ( čamedân ) and many Turkic languages. Pronunciation [ edit ] IPA ( key ) : [t͡ɕɪmɐˈdan] Audio : ( file ) Noun [ edit ] чемода́н • ( čemodán ) m inan ( genitive чемода́на , nominative plural чемода́ны , genitive plural чемода́нов , relational adjective чемода́нный , diminutive чемода́нчик ) suitcase , trunk 1973 , Венедикт Ерофее
   Etymology [ edit ] Via a Turkic medium, from Persian جامه‌دان ( jâme-dân , “ suitcase ” ) . Pronunciation [ edit ] IPA ( key ) : [t͡ʃemɔˈdan] Audio : ( file ) Noun [ edit ] чемода́н • ( čemodán ) m inan ( genitive чемода́на , nominative plural чемода́ни , genitive plural чемода́нів , relational adjective чемода́нний or чемода́новий , diminutive чемода́нчик ) suitcase Synonym: валі́за ( valíza ) Declension [ edit ] Declension of чемода́н ( inan hard masc-form accent-a ) singular plural nominative чемода́н čemodán чемода́ни čemodány genitive чемода́на čemodána чемода́нів čemodániv dative чемода́
##### 70e4aeaca7d94920
   Etymology [ edit ] Borrowed from Russian чемода́н ( čemodán ) , from Persian جامه‌دان ( jâme-dân , “ suitcase ” ) . Pronunciation [ edit ] ( Classical Persian ) IPA ( key ) : /t͡ʃa.ma.ˈdaːn/ ( Dari, formal ) IPA ( key ) : [t͡ʃʰä.mä.d̪ɑːn] ( Dari, formal ) IPA ( key ) : [t͡ʃʰä.mä.d̪ɑːn] ( Kabuli ) IPA ( key ) : [t͡ʃʰä.mä.d̪ɑːn] ( Hazaragi ) IPA ( key ) : [t͡ʃʰä.mä.d̪ɔːn] ( Iran, formal ) IPA ( key ) : [t͡ʃʰæ.me.d̪ɒːn] ( Iran, formal ) IPA ( key ) : [t͡ʃʰæ.me.d̪ɒːn] ( Tehrani ) IPA ( key ) : [t͡ʃʰæ.me.d̪uːn] ( Tajik, formal ) IPA ( key ) : [t͡ʃʰä.mä.d̪ɔn] Rhymes: -aːn Readings Classical reading 
##### 44d22a1627092c83
   Etymology [ edit ] From Ancient Greek ζωνάριον ( zōnárion ) , likely via Aramaic זונרא / ܙܘܢܪܐ ( zūnārā ) . See the usage notes for distinctions between various types of belts. Pronunciation [ edit ] IPA ( key ) : /zun.naːr/ Noun [ edit ] زُنَّار • ( zunnār ) m ( plural زَنَانِير ( zanānīr ) ) belt , girdle ( al-Andalus ) a kind of coarse mantle Usage notes [ edit ] In the time of ʿUmar a زُنَّار ( zunnār ) would mean a belt worn by Christians , Jews , Sabians , Magians and other non-Muslims; for it had become fashionable in the Byzantine Empire under Diocletian and Constantine to wear a ζώνη 
   Etymology [ edit ] Borrowed from Arabic زُنَّار ( zunnār ) , from Ancient Greek ζωνάριον ( zōnárion ) . Pronunciation [ edit ] ( Classical Persian ) IPA ( key ) : /zun.ˈnaːr/ ( Dari, formal ) IPA ( key ) : [zʊn.nɑ́ːɾ] ( Dari, formal ) IPA ( key ) : [zʊn.nɑ́ːɾ] ( Kabuli ) IPA ( key ) : [zʊn.nɑ́ːɾ] ( Hazaragi ) IPA ( key ) : [zun.nɔ́ːɾ] ( Iran, formal ) IPA ( key ) : [zon.nɒ́ːɹ] ( Tajik, formal ) IPA ( key ) : [zun.nɔ́ɾ] Rhymes: -aːr Readings Classical reading ? zunnār Dari reading ? zunnār Iranian reading ? zonnâr Tajik reading ? zunnor Noun [ edit ] زنار • ( zonnâr ) ( historical ) belt or thr
##### 97c31b225a1f8218
   Etymology 1 [ edit ] See the etymology of the corresponding lemma form. Verb [ edit ] شما ( form I ) شَمَّا ( šammā ) /ʃam.maː/ : inflection of شَمَّ ( šamma ) : third-person masculine dual past active second-person dual imperative شُمَّا ( šummā ) /ʃum.maː/ : inflection of شَمَّ ( šamma ) : third-person masculine dual past passive second-person dual imperative Etymology 2 [ edit ] See the etymology of the corresponding lemma form. Verb [ edit ] شِمَا • ( šimā ) ( form I ) /ʃi.maː/ second-person dual imperative of وَشَمَ ( wašama ) Persian [ edit ] Etymology [ edit ] Etymology tree Proto-Indo-
   Etymology 2 [ edit ] See the etymology of the corresponding lemma form. Verb [ edit ] شِمَا • ( šimā ) ( form I ) /ʃi.maː/ second-person dual imperative of وَشَمَ ( wašama ) Persian [ edit ] Etymology [ edit ] Etymology tree Proto-Indo-European *yúHs Middle Persian [script needed] ( ašmā ) der. Persian شما From Middle Persian ʾšmʾ, ʿšmʾ ( ašmā, išmā , “ you ” ) , from Proto-Indo-European *yúHs ( “ you (plural) ” ) . Compare Southern Luri ایسا ( īsâ , “ you ” ) and Bakhtiari ایسا ( īsâ , “ you ” ) . Pronunciation [ edit ] ( Classical Persian ) IPA ( key ) : /ʃu.ˈmaː/ ( Dari, formal ) IPA ( key 
   Etymology [ edit ] Etymology tree Proto-Indo-European *yúHs Middle Persian [script needed] ( ašmā ) der. Persian شما From Middle Persian ʾšmʾ, ʿšmʾ ( ašmā, išmā , “ you ” ) , from Proto-Indo-European *yúHs ( “ you (plural) ” ) . Compare Southern Luri ایسا ( īsâ , “ you ” ) and Bakhtiari ایسا ( īsâ , “ you ” ) . Pronunciation [ edit ] ( Classical Persian ) IPA ( key ) : /ʃu.ˈmaː/ ( Dari, formal ) IPA ( key ) : [ʃʊ.mɑ́ː] ( Dari, formal ) IPA ( key ) : [ʃʊ.mɑ́ː] ( Kabuli ) IPA ( key ) : [ʃʊ.mɑ́ː] ( Hazaragi ) IPA ( key ) : [ʃu.mɔ́ː] ( Iran, formal ) IPA ( key ) : [ʃo.mɒ́ː] ( Tajik, formal ) IPA (
##### 2748a4fbd796d5c5
   Etymology [ edit ] Borrowed from British English pyjama , from Hindi पैजामा ( paijāmā ) / Urdu پائِجامَہ ( pāijāma ) , from Persian پایجامه ( pāyjāma ) , archaic form of پاجامه ( pājāma ) . Doublet of پاجامه . Pronunciation [ edit ] ( Classical Persian ) IPA ( key ) : /piː.ʒaː.ˈma/ ( Dari, formal ) IPA ( key ) : [pʰiː.ʒɑː.má] ( Dari, formal ) IPA ( key ) : [pʰiː.ʒɑː.má] ( Kabuli ) IPA ( key ) : [pʰiː.ʒɑː.má] ( Hazaragi ) IPA ( key ) : [pʰi.ʒɔː.má] ( Iran, formal ) IPA ( key ) : [pʰiː.ʒɒː.mé] ( Tajik, formal ) IPA ( key ) : [pʰi.ʒɔ.má] Rhymes: -a Readings Classical reading ? pīžāma Dari reading
##### 592136221dfef068
   Etymology [ edit ] Borrowed from Persian پاجامه ( pâjâme ) . By surface analysis , پا ( pa ) + جامه ( came ) . Noun [ edit ] پاجامه • ( pacame ) trousers Synonyms: طون ( don ) , شلوار ( şelvar ) Descendants [ edit ] Turkish: pacame Further reading [ edit ] Mehmed Salâhî ( 1897–1906 ), “ پاجامه ”, in Kâmûs-ı Osmânî , volume 2, page 272 Persian [ edit ] Alternative forms [ edit ] پایجامه ( pâyjâme ) ( archaic ) Etymology [ edit ] From پا ( pâ , “ leg ” ) +‎ جامه ( jâme , “ garment ” ) . Pronunciation [ edit ] ( Classical Persian ) IPA ( key ) : /paː.d͡ʒaː.ˈma/ ( Dari, formal ) IPA ( key ) : [pʰɑ
   Etymology [ edit ] From پا ( pâ , “ leg ” ) +‎ جامه ( jâme , “ garment ” ) . Pronunciation [ edit ] ( Classical Persian ) IPA ( key ) : /paː.d͡ʒaː.ˈma/ ( Dari, formal ) IPA ( key ) : [pʰɑː.d͡ʒɑː.má] ( Dari, formal ) IPA ( key ) : [pʰɑː.d͡ʒɑː.má] ( Kabuli ) IPA ( key ) : [pʰɑː.d͡ʒɑː.má] ( Hazaragi ) IPA ( key ) : [pʰäj.d͡ʒi.má] ( Iran, formal ) IPA ( key ) : [pʰɒː.d͡ʒɒː.mé] ( Tajik, formal ) IPA ( key ) : [pʰɔ.d͡ʒɔ.má] Rhymes: -a Readings Classical reading ? pājāma Dari reading ? pājāma Iranian reading ? pâjâme Tajik reading ? pojoma Noun [ edit ] Dari پاجامه Iranian Persian Tajik поҷома پاجامه
##### e0ddd3d5a8571f36
   Etymology [ edit ] From ζώνη ( zṓnē , “ belt ” ) +‎ -άριον ( -árion , diminutive ) . Pronunciation [ edit ] IPA ( key ) : /zdɔː.ná.ri.on/ → /zoˈna.ri.on/ → /zoˈna.ri.on/ ( 5 th BCE Attic ) IPA ( key ) : /zdɔː.ná.ri.on/ ( 1 st CE Egyptian ) IPA ( key ) : /zoˈna.ri.on/ ( 4 th CE Koine ) IPA ( key ) : /zoˈna.ri.on/ ( 10 th CE Medieval ) IPA ( key ) : /zoˈna.ri.on/ ( 15 th CE Constantinopolitan ) IPA ( key ) : /zoˈna.ri.on/ Noun [ edit ] ζωνάρῐον • ( zōnárĭon ) n ( genitive ζωνᾰρίου ) ; second declension diminutive of ζώνη ( zṓnē ) Declension [ edit ] Second declension of τὸ ζωνᾰ́ρῐον ; τοῦ ζωνᾰρῐ
##### 4867e50bbfb9ec32
   Etymology [ edit ] Related to ζώννῡμι ( zṓnnūmi , “ to gird ” ) ; ultimately from Proto-Indo-European *yoh₃snéh₂ , from the root *yeh₃s- ( “ gird ” ) . Compare Old Church Slavonic (по)ꙗсъ ( (po)jasŭ ) , Sanskrit रास्ना ( rā́snā ) (< *yā́snā ). [ 1 ] [ 2 ] Pronunciation [ edit ] IPA ( key ) : /zdɔ̌ː.nɛː/ → /ˈzo.ni/ → /ˈzo.ni/ ( 5 th BCE Attic ) IPA ( key ) : /zdɔ̌ː.nɛː/ ( 1 st CE Egyptian ) IPA ( key ) : /ˈzo.ne̝/ ( 4 th CE Koine ) IPA ( key ) : /ˈzo.ni/ ( 10 th CE Medieval ) IPA ( key ) : /ˈzo.ni/ ( 15 th CE Constantinopolitan ) IPA ( key ) : /ˈzo.ni/ Noun [ edit ] ζώνη • ( zṓnē ) f ( genitive
   Etymology [ edit ] From Ancient Greek ζώνη ( zṓnē , “ belt; loins, waist ” ) . Noun [ edit ] ζώνη • ( zóni ) f ( plural ζώνες ) belt , sash , seat belt Δέσε τη ζώνη σου, σε παρακαλώ ― Dése ti zóni sou, se parakaló ― Fasten your seat belt , please μαύρη ζώνη στο καράτε. ― mávri zóni sto karáte. ― black belt in karate. zone band ζώνη συχνοτήτων ― zóni sychnotíton ― frequency band Declension [ edit ] Declension of ζώνη singular plural nominative ζώνη ( zóni ) ζώνες ( zónes ) genitive ζώνης ( zónis ) ζωνών ( zonón ) accusative ζώνη ( zóni ) ζώνες ( zónes ) vocative ζώνη ( zóni ) ζώνες ( zónes ) Re
##### 28695b63acddb057
   Etymology [ edit ] From Proto-Indo-European *yúHs , plural of *túh₂ . [ 1 ] Pronunciation [ edit ] IPA ( key ) : /juːz/ Rhymes: -uːz Pronoun [ edit ] *jūz you (plural) Inflection [ edit ] Proto-Germanic personal pronouns nominative accusative dative / instr possessive singular first person *ek (unstressed *ik ) *mek (unstressed *mik ) *miz *mīnaz second person *þū *þek (unstressed *þik ) *þiz *þīnaz dual first person *wet (unstressed *wit ) *unk *unkiz *unkeraz second person *jut , *jit *inkw *inkwiz *inkweraz plural first person *wīz (unstressed *wiz ) *uns *unsiz *unseraz second person *jūz 
##### f8581da3b479b234
##### 11e08f1bf10d111e
```


## [2026-10-17T00:37:23.303Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; wc -c f8581da3b479b234.txt 11e08f1bf10d111e.txt 69d1baa690767ac6.txt ba31b0c49580744c.txt bfc3b37ce450b95c.txt ca25ca363ef6fb3f.txt 88697d8941b45d67.txt 1c65af0c8088a0e3.txt; head -c 300 f8581da3b479b234.txt; python3 - <<'EOF'\nimport re\nfor f,kw in [('69d1baa690767ac6','Etymology'),('ba31b0c49580744c','pajamas (n.)'),('bfc3b37ce450b95c','you (pron.)'),('ca25ca363ef6fb3f','zone (n.)'),('88697d8941b45d67','Etymology'),('1c65af0c8088a0e3','Etymology')]:\n    t=re.sub(r'\\s+',' ',open(f+'.txt').read())\n    i=t.find('From Wiktionary'); s=t[i:] if i>=0 else t\n    j=s.find(kw); print('####',f, s[j:j+900])\nEOF"
}
```


### [2026-10-17T00:37:23.810Z] TOOL RESULT

```
  169 f8581da3b479b234.txt
10106 11e08f1bf10d111e.txt
32943 69d1baa690767ac6.txt
  134 ba31b0c49580744c.txt
  130 bfc3b37ce450b95c.txt
  131 ca25ca363ef6fb3f.txt
33715 88697d8941b45d67.txt
11542 1c65af0c8088a0e3.txt
88870 total
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yeh₃s-
FETCHED: 2026-10-17T00:36:47Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found#### 69d1baa690767ac6 Etymology 1 [ edit ] From Middle English you , yow , ȝow ( object case of ye ) , from Old English ēow ( “ you ” , dative case of ġē ) , from Proto-West Germanic *iwwi ( “ you ” , dative case of *jiʀ ) , from Proto-Germanic *iwwiz ( “ you ” , dative case of *jīz ) , the Western form of Proto-Germanic *izwiz ( “ you ” , dative case of *jūz ) , from Proto-Indo-European *yúHs ( “ you ” , plural ) . Cognate with Scots you ( “ you ” ) , Saterland Frisian jou ( “ you ” ) , West Frisian jo ( “ you ” ) , Low German jo , joe and oe ( “ you ” ) , Dutch jou and u ( “ you ” ) , German euch ( “ you ” ) , Middle High German eu , iu ( “ you ” , object pronoun ) , Latin vōs ( “ you ” ) , Avestan 𐬬𐬋 ( vō , “ you ” ) , Ashkun yë̃ ( “ you ” ) , Kamkata-viri šo ( “ you ” ) , Sanskrit यूयम् ( yūyám , “ you ” ) . See usage notes. Ye , you and your are cognate with Dutch jij / je , jou , jouw ; Low German ji , 
#### ba31b0c49580744c n
#### bfc3b37ce450b95c n
#### ca25ca363ef6fb3f n
#### 88697d8941b45d67 Etymology [ edit ] Etymology tree Proto-Indo-European *yeh₃s- Proto-Indo-European *-néh₂ Proto-Indo-European *yoh₃snéh₂ der. Ancient Greek ζώνη ( zṓnē ) bor. Latin zōna der. English zone From Latin zōna , from Ancient Greek ζώνη ( zṓnē , “ girdle , belt ” ) . Doublet of zona . Pronunciation [ edit ] ( General American ) enPR : zōn , IPA ( key ) : /zoʊn/ ( Received Pronunciation ) IPA ( key ) : /zəʊn/ Audio ( US ) : ( file ) Rhymes: -əʊn Noun [ edit ] zone ( plural zones ) ( geography , now rare ) Each of the five regions of the earth's surface into which it was divided by climatic differences, namely the torrid zone (between the tropics), two temperate zones (between the tropics and the polar circles), and two frigid zones (within the polar circles). 1567 , Ovid, translated by Arthur Golding , Metamorphoses , section I: And as two Zones doe cut the Heaven upon the righter side, / And oth
#### 1c65af0c8088a0e3 Etymology [ edit ] Borrowed from English pyjamas , with spelling pronunciation , from pai jamahs (“loose trousers tied at the waist, worn by Muslims in India”), adopted by colonials, especially for nightwear, probably from Hindi पैजामा ( paijāmā , “ pajama ” ) , itself from Persian پایجامه . Pronunciation [ edit ] Audio : ( file ) IPA ( key ) : /piˈjaːmaː/ Hyphenation: py‧ja‧ma Noun [ edit ] pyjama m ( plural pyjama's , diminutive pyjamaatje n ) pyjamas , a matching set of light material trousers and vest for wearing to bed and sleeping in Derived terms [ edit ] pyjamabroek pyjamajas pyjamapak pyjamatrui pyjamavest Descendants [ edit ] → Indonesian: piyama See also [ edit ] nachtkledij nachtkleed slaapmuts Finnish [ edit ] Etymology [ edit ] From English pyjamas . Pronunciation [ edit ] IPA ( key ) : /ˈpyjɑmɑ/ , [ˈpyjɑ̝mɑ̝] Rhymes: -yjɑmɑ Syllabification ( key ) : py‧ja‧ma Hyphenation (
```


## [2026-10-17T00:37:33.841Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; F=tools/fetch_source.py; for u in \"https://en.wiktionary.org/wiki/pajamas\" \"https://en.wiktionary.org/wiki/pyjama#French\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yewH-\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yeHs-\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yúHs\" \"https://en.wiktionary.org/wiki/ye\"; do python3 $F \"$u\" --note \"page 568, roots Yôs / Yu\" 2>&1|tail -1; done; cd data/verification/sources/web; python3 - <<'EOF'\nimport re,glob,hashlib\nfor u in [\"https://en.wiktionary.org/wiki/pajamas\",\"https://en.wiktionary.org/wiki/pyjama#French\",\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yewH-\",\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yeHs-\",\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yúHs\",\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yū́\"]:\n    h=hashlib.sha1(u.encode()).hexdigest()[:16]\n    t=re.sub(r'\\s+',' ',open(h+'.txt').read())\n    i=t.find('From Wiktionary'); s=t[i:] if i>=0 else t[:300]\n    print('####',u,len(t)); \n    for m in list(re.finditer(r'Etymology( \\d)? \\[ edit \\]|Root \\[ edit \\]|Pronoun \\[ edit \\]',s))[:3]:\n        print('   ',s[m.start():m.start()+600])\nEOF"
}
```


### [2026-10-17T00:37:37.500Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/961b8447cdb32270.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/49691bd77d69eb84.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/fcb188fac26dc863.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/1cfa1b5b5515156b.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/4d486fd0a1107b98.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e8a026fb18980362.txt
#### https://en.wiktionary.org/wiki/pajamas 11575
    Etymology [ edit ] Borrowed from Hindustani ( Hindi पाजामा ( pājāmā ) / Urdu پاجامہ ( pājāma ) ), from Classical Persian پَاجَامَه ( pājāma , “ trousers, drawers ” ) , from پَا ( pā , “ leg ” ) + جَامَه ( jāma , “ garment ” ) . Pronunciation [ edit ] ( Mid-Atlantic , New England , Southern US ) IPA ( key ) : /pəˈd͡ʒɑ.məz/ [ 1 ] IPA ( key ) : ( Canada , Midland US , Northern US , Western US ) /pəˈd͡ʒæ.məz/ [ 1 ] ( Ireland ) IPA ( key ) : /pəˈd͡ʒaː.məs/ , /pəˈd͡ʒæː.məs/ ( South Asia ) IPA ( key ) : /pə(j).dʒɑ.mɑs/ , /pɑː(j)-/ , /pɛː-/ ( Philippines ) IPA ( key ) : /pɐˈd͡ʒaː.mɐs/ Audio ( US ) : (
    Etymology [ edit ] Borrowed from English pyjamas . Pronunciation [ edit ] ( North Wales ) IPA ( key ) : /paˈd͡ʒamas/ ( South Wales ) IPA ( key ) : /paˈd͡ʒamaz/ Noun [ edit ] pajamas pl ( no singulative , plural only ) alternative form of pyjamas Mutation [ edit ] Mutated forms of pajamas radical soft nasal aspirate pajamas bajamas mhajamas phajamas Note: Certain mutated forms of some words can never occur in standard Welsh. All possible mutated forms are displayed for convenience. Retrieved from " https://en.wiktionary.org/w/index.php?title=pajamas&oldid=93459503 " Categories : English terms b
#### https://en.wiktionary.org/wiki/pyjama#French 9707
    Etymology [ edit ] Borrowed from English pyjamas , with spelling pronunciation , from pai jamahs (“loose trousers tied at the waist, worn by Muslims in India”), adopted by colonials, especially for nightwear, probably from Hindi पैजामा ( paijāmā , “ pajama ” ) , itself from Persian پایجامه . Pronunciation [ edit ] Audio : ( file ) IPA ( key ) : /piˈjaːmaː/ Hyphenation: py‧ja‧ma Noun [ edit ] pyjama m ( plural pyjama's , diminutive pyjamaatje n ) pyjamas , a matching set of light material trousers and vest for wearing to bed and sleeping in Derived terms [ edit ] pyjamabroek pyjamajas pyjamapak
    Etymology [ edit ] From English pyjamas . Pronunciation [ edit ] IPA ( key ) : /ˈpyjɑmɑ/ , [ˈpyjɑ̝mɑ̝] Rhymes: -yjɑmɑ Syllabification ( key ) : py‧ja‧ma Hyphenation ( key ) : py‧ja‧ma Noun [ edit ] pyjama pajamas , pyjamas Declension [ edit ] Inflection of pyjama ( Kotus type 10/ koira , no gradation) nominative pyjama pyjamat genitive pyjaman pyjamien partitive pyjamaa pyjamia illative pyjamaan pyjamiin singular plural nominative pyjama pyjamat accusative nom. pyjama pyjamat gen. pyjaman genitive pyjaman pyjamien pyjamain rare partitive pyjamaa pyjamia inessive pyjamassa pyjamissa elative pyj
    Etymology [ edit ] English pyjama , from Urdu پایجامه ( pāyjāma ) / Hindi पैजामा ( paijāmā ) , from Persian پایجامه ( pâyjâma ) / پاجامه ( pâjâma , “ leg garment ” ) . Pronunciation [ edit ] IPA ( key ) : /pi.ʒa.ma/ Audio : ( file ) Audio ( Canada ( Shawinigan ) ) : ( file ) Audio ( Switzerland ( Valais ) ) : ( file ) Audio ( France ( Vosges ) ) : ( file ) Noun [ edit ] pyjama m ( plural pyjamas ) pyjamas Derived terms [ edit ] soirée pyjama Descendants [ edit ] → Romanian: pijama → Turkish: pijama Further reading [ edit ] “ pyjama ”, in Trésor de la langue française informatisé [ Digitized Tr
#### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yewH- 164
#### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yeHs- 164
#### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yúHs 8928
    Pronoun [ edit ] *yúHs [ 1 ] [ 2 ] [ 3 ] you (plural) Declension [ edit ] A user suggests that this Proto-Indo-European reconstruction entry be cleaned up, giving the reason: “manual table should be moved to a template” . Please see the discussion on Requests for cleanup ( + ) or the talk page for more information and remove this template after the problem has been dealt with. Andrew Sihler 's reconstruction [ 4 ] dual plural nominative *yū́h₁ ( ? *yūh₁) *yū́s ( ? *yúHs) accusative *uh₁-wé ~ *wō̆h₁ *usmé ~ *wō̆s genitive ? *usóm ~ *wō̆s ablative ? *usm-ét dative ? *usm-éy ~ *wō̆s Donald Ringe 
#### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yū́ 8985
    Pronoun [ edit ] *yúHs [ 1 ] [ 2 ] [ 3 ] you (plural) Declension [ edit ] A user suggests that this Proto-Indo-European reconstruction entry be cleaned up, giving the reason: “manual table should be moved to a template” . Please see the discussion on Requests for cleanup ( + ) or the talk page for more information and remove this template after the problem has been dealt with. Andrew Sihler 's reconstruction [ 4 ] dual plural nominative *yū́h₁ ( ? *yūh₁) *yū́s ( ? *yúHs) accusative *uh₁-wé ~ *wō̆h₁ *usmé ~ *wō̆s genitive ? *usóm ~ *wō̆s ablative ? *usm-ét dative ? *usm-éy ~ *wō̆s Donald Ringe
```


## [2026-10-17T00:37:45.200Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/s568.py\npython3 $S incoming/WLD/WLD_Bd1_pages.txt '(?i)gürten' 300 6 | head -40"
}
```


### [2026-10-17T00:37:45.639Z] TOOL RESULT

```
NO HIT incoming/WLD/WLD_Bd1_pages.txt (?i)gürten
```


## [2026-10-17T00:37:51.188Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/s568.py\npython3 $S incoming/WLD/WLD_Bd1_pages.txt '(?i)g.rten|jüosti|juosti|ζών' 300 4; python3 $S incoming/WLD/WLD_Bd1_pages.txt '(?i)yūšmat|yüsmat|jus .ihr|got\\. jus' 300 3"
}
```


### [2026-10-17T00:37:51.990Z] TOOL RESULT

```
[WLD_Bd1_pages.txt leaf 217] s. (*gajo-;ia vgl. lit. juosmub „Gurt“), ijdzvy ds.            vgl. russ. -ksl. pojasnb ds.); jovodo)        jmvvvo&o) Hes. otwa      •    thessal.        = *'C<boi}m ? (zum gr. £- s. Sommer Gr. Ltst. 145. 147); alb. (G. Meyer Alb. Wb. 308) n-qes „ich giirte";                      lit. jiiosiu,     juosti   ,                                                                                       giirtenX juostas ,,gegiir- tet", ji'wsta „Giirtel“:           aksl. pojasa, -jasati ,.giirten‘‘ pojasz, „Giirtel“                                      usw., siehe Berneker 449).   I.   iu-       ,,ihr“ ursprgl
--
[WLD_Bd1_pages.txt leaf 280] w. zu werten.             —                        Kein ureg- folgt aus gr. gfjyog, s. u. reg- „farben".   ner-gh- .,drehen, zusammenwinden, wiirgen, pressen'       Gr. egyaxog   '       <fgay/.i6g   lies.,     egyaxaco „hege         ein,   sperre             ein",    ogyaxog  „Gehege fur Pflanzen, Garten", dgydvg, ogyag, -ado; „Zaun“ (ursprgl. ,,ge-  flochtener Zaun'"', kaum „umwindend“, s. zur Sache Meringer IF. 17, 1 3 9 ff                                         .      vgl. unten slov. vrzii „Zaun, Heeke“; Brugmann IF. 15, S4f.), wozu auch  der Stadtname Ogyojuevo alter Egyouevog (Prellwitz. J. 
--
[WLD_Bd1_pages.txt leaf 290] weord . word n. m. ..Gehege. am Haus, Ilofplatz, Stralle" (*iwr-io-, *nr-to-), as.  wurth f., ,.Boden. gestampfter oder gepflasterter Platz" (= ai. ertt-'j, mnd. wnrt, wort, wurde , worde f. ..erhohter oder eingeziiunter Platz,                                               r Ilofstiitte, Hausplatz; Garten, Feldstiick, AA aldniark", anord. urd i. ..Haufe oder Reihe von hinabgestiirzten Felsbliicken am FuB eines Berges' (vgl. zu den germ. AA'orten bes. Fick III 4 395, Falk-Torp u. urd, renje, vent.               v               ,                                                                        
--
[WLD_Bd1_pages.txt leaf 291] t, veer,             vert\f      \ ,                                           i   'mail [doch s. dazu*i'C>- ..Sclmur-);                               am niiehsten stehn alb. vcide ,,Gehege,                     Hof urn das Haus, Hiirde, Schafstall” is. o.; * uor-tii ), toehar. B. iciir/o, icarto ,, Garten, Hain"? (Liden aaO.                                             '.       ir.fcrt ..Grabhiigel”                               ;       in   der Bed. auch aksl. v ora ,,saepiinentum”.       Zu scheiden von tier- ..gewaliren, sorgend worauf sehn” gegen Fick 1 4 130, 54Sf.); auch einzelne Beruhrungen mi
--
[WLD_Bd1_pages.txt leaf 217]                      usw., siehe Berneker 449).   I.   iu-       ,,ihr“ ursprgl. nur Rom.; Ivasus obliqui vom St. lies-, iio(sj-.      1.       Ai.   yurdm „ihr“ Du., yuydni PL. av. yuzom, gathav. f/uv; arm. nach- wirkend in den mit je- anl. Kasus z. B. dat. jrz (c nacli mez „nobis“, T:ez „tibi“);  got. jus ,,ihr“ PL, sonst nacb „wir“ (s. ue~) umgebildet aisl.       r,                                             <                                                                                                                                   7    ags. ye, as. yf, ye, ahd. ir: Du. got. *ju-t (: lit. ju
--
```


## [2026-10-17T00:37:58.114Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/s568.py\npython3 $S IEC.txt '(?i)gird' 250 6 | head -30; python3 $S CHEUNG.txt '(?i)jāma|jâma|yām-|\\*yam' 250 4; python3 $S BRT.txt 'yüs |yūš |yüi |yuš ' 200 3"
}
```


### [2026-10-17T00:37:58.693Z] TOOL RESULT

```
[IEC.txt leaf 30] hold’ antro- “interior; hollow'. Cf. entero- Gk. antron (‘cave’. LW in Lat. antrum, id.); OCS cf. otrí “inside”, otro-ba ‘intestines’, and com. Sl. ants- (?) “forepiece, crosspiece'. Cf. anti and derivatives Go. ans ‘beam’; ON áss; MHG cf. ans-boum ‘girder’ anu (ənu), cf. ana (ənə) Skt. ánu “after, behind; later’; anu-, px.; anuh 'non-Aryan'; Av. anu; OPer. anuv; Gk. cf. anuo, ánūmi ‘complete’ anus, see anos (2) ānus, os ‘ring, circle Arm. aniw, cpds. anu- ‘wheel’; cf. mad-ani ‘finger-ring’; Lat. an
--
[IEC.txt leaf 72] atv. braucu, braukt ‘travel bhrouK- *edge, side; side-piece' . „ Ir. bruach “edge, side’; Cz. Pol. brus, R (dim.) brusók ‘whetstone’ beside Cz. brusle ‘skate’; bhronghos, à — bhrughno- 10 15 20 25 30 35 40 45 106 Srb. brüs ‘whetstone’; R brus ‘beam, girder bhroulios, iə ‘seething, brew, surge’ Br. brülľ’, pl. brüP u ‘wave, billow; brew, soup’; brül'a v. ‘vomit’; OCS brulja ‘fountain’. (For a possible verbal prototype, cf. OCS brujọ, ati ‘roar’; Li. bráujuos, bráutis “rush?). A zero-gde occurs in Srb
--
[IEC.txt leaf 75] cover’ and Oss. åm-bårzin, id.; Tokh. A pär- kàw-, B páürko- ‘gain’; Gk. phrásso beside phárkhma &  phrágma; MHG borgen ‘watch, care for; ON byrgja ‘enclose’. An extended form appears to be OLat. fraxare ‘patrol’ (*r) w. sim. long-zero in Alb. brez *girdle; wall-brace'; Dac. substr. briu, id. in Rumanian. Noun-forms include Go. baürgs *walled city, tower' and com. Gmc.; E borough and burrow; OCz. brh ‘lair, den, camp’; mod. Cz. *hencoop, fowling-net’. (The question of an Anatolian equivalent of typ
--
[IEC.txt leaf 202] Sl. ‘pole’) ghrdhos, om, iom, iə ‘enclosure, stronghold’. (Variant: ghrgh-?) Skt. grháh, Am “house” beside o-gde gráhah, id. Ambig. in view of Ir. gráig, f. “village”, fr. *ghrgh-?); Tokh. kerciye ‘palace’; Hitt. gurtas ‘fortress’; MHG (prob.) gurt ‘girdle’ beside OHG gurtila, etc. ghrguhos, is (?) ‘dry branch, stick’. Cf. gro8-. (Evidence ambig.) Tokh. A karke, B karak ‘branch’; Gk. kárphos, -6 ‘twig; chaff; Ir. gráig *gnurled branch? be- side grágán, id. (and ‘shock of hair’) ghrið ‘shout’. (Most 
--
[IEC.txt leaf 212] lm- Oss. qurmä ‘anxious; anxiety’; Alb. gulm (1) ‘sorrow’. O-gde in MHG qualm ‘anxiety qualm’; OE cwealm; EME qualm (also ‘nau- sea’). A zero-gde alleged G dial. Quulm is hy- pothetical gulnos, iom, 'gulnd- (gulnd-), gul- ‘acorn’. WP I, 692 Per. (?) girdü ‘nut’; Arm. kayni, -vo, -eav (“oak. But for kayin, gs kayno ‘hazel’, see koslo-, ko- solo-); Gk. bálanos, balánion; Aeol. (alleged) galanos; Lat. glans, gs glandis; Alb. l&nd, léndé (facorn" may be a LW fr. Lat.); OCS zelodi, Let m. (and com. SL Po
--
[IEC.txt leaf 217] d’; Lusat. hordy, id.; Pol. cf. also wz- garda ‘contempt’ beside gardzić ‘despise’; Li. gurdùs ‘sluggish, ailing, weak’; Latv. gurds ‘tired, faint’ gurdh- (1). Cf. gur- (3). Cf. WP I, 686 Av. goroóo, adj. ‘howling’; Arm. kardam “call; read out’; Li. girdžiù, girdéti ‘hear’; girdà f. ‘hearing’; Latv. dzirdu, et ‘hear’ O-gde in Skt. garha “abuse” gurdh- (2) 'stir, rouse'. Cf. gurgotio Gk. brásso, aor. ébrasa; Alb. cf. ngrydh (stir up, foment': Gk. embrásso ‘cast up’ ofthe sea) gurdhlom, gurdhrom, à, 
--
[CHEUNG.txt leaf 0] L37.5)   *CHORESMIAN: (+ *ui-) ? m/wy’s- ‘to yawn’ = Samadi: 224   *NWIR: (+ *ui-) Bal. g(iy)asit/g(iy)as-, gihasit/gihas- (etc.) ‘to yawn’, ? Kurd.  (Kurm.) bäwisk, bahusk (f.), (Sor.) bawésk ‘yawn(ing)’. © The Kurd. forms are  hardly from the root *yamH ‘to vomit’, as stated by Cabolov, l.c.   *NEIR: (+ *ni-) Yi. niáské, M. niezye ‘yawn’   © A reconstruction *kas-ja- (*xà- ‘to open’) is cautiously cited for the Khot. forms  by Emmerick (SGS: 97). The comparison with Sogd. wy’s and Chor. m/wy’s- ra
--
[CHEUNG.txt leaf 0]  Pres. ja-: IND. 15р. OAv. ufiia^ (Y 43.8), YAv. ufiiemi (Yt 13.21, Y 17.18, Y 26.1, etc.), SUBJ. 15р.  OAv. ufiiani (Y 28.3), Ү Ау. 35р. ufiiat (Yt 13.50)    *PARTHIAN: ? wf- ‘to spit’. Ò Differently Ghilain (l.c.), who connects the Pth. form  with *yamH ‘to vomit’. An analogical developent m > f is quoted from  Bartholomae, ZAIW: 218. = Ghilain: 56 | DMMPP: 340b   Pres.: IND. 3pl. *wfynd {hapax}   *SOGDIAN: SSogd. w’B, BSogd. w’B, CSogd. w’b, MSogd. w’B “о say, speak’  (supplet. BSogd. wyt- < part
--
[CHEUNG.txt leaf 0] rabH (s.v.), *Huar' (s.v.),  *man (s.v.), *ram (S.V.),  *srau (S.V.)   *iauz   *sarH?   *Hand   *Caud, *Hranj   *&iaH? (s.v.), *Hmaiz  *skamb   *staub/f, *uab/f , *zag   *iaz, *uah’, *ui(H)z  *xSuaip/b   *daj (s.v.), *skap/f (s.v.),  *sna9H (s.v.)   *yamH    to wade   to wail   to wake up,  be awake    to walk   walnut   to wander   to wane   to want   to want to leave  to ward off   to wash    to watch   to wave   to wear clothes,  be dressed   to wear (off)   to weave   to weep    to welcome  to w
--
[BRT.txt leaf 48] aut';  '',a  ..*kay:i apat Aaca ni:iiiraj-fnV.6.$if?); — asH.masÖ  fi^nti  masyat»hd  'r,a  *ydi  *aparaya  paiti xraoidi'aAe  bis  'rate  lar^AaAe  "..h\s^3iXtto  *)tiastrfynaya..*kaya  kasya/i/t^  *yüi  *paou- mollisligni"  V.  jj.  30;  —  'val  apayaiia  H.  ruya  paiti  *mastrr/nya  "Kopfhaut.  — iog(X).  a)  mit  dem  Korrelat  _v(K'a«/- :  Welcher TeilderKopfhautistdergrössere? ^t/ (sd.)  °vat 
--
[BRT.txt leaf 62] ß;  —  at  tJ  mainya , .  manahicä  vacahicä  Syaoianöi  hl  vahyö akimcii  "und  die  beiden  Geister  . .  sind das  Bessere  und  das  Schlechte  in  Ge- danken, Wort  und  Tal"  Y.^0.3;  ■ —  at yüs  daevti  vtspatshö  'käi  manatikB  sta •■  yasSj    .  .  drüjascH  pairi.malsisca Böses  schaffe-    —    mp-  (P"-)  akalai (Transskr.);    vgL  daiu  SBE.  5.  109,  3^.  181, •  j.  akana-  n.  '
--
[BRT.txt leaf 89]  ai^ry-äxStar-  m.  'der  die  Aufsicht hat,  (ührt  über-,  Eeaufsichtiger" :  har^ia 'taca  z'ispaya  .  .  gai^ayä  ¥.57.15;  V.  2. 4,  5;  —  hant3rfmca  'türimca  .  .  gafkayä \l.  10.  103; — yüi  hmii  äiihqm  damanqm ..  'iarasifa  (NP.)  nipätarasca  .  .  Ytig.18. Zam  V.  5.11-  (sd.  mit  No.  1).  —  Pü.:  a/ar fiiiäs  däslär. •  j.  aiwry-äxäträi  Inf.  'die  Aufsicht  zu führen  über 
--
```


## [2026-10-17T00:38:06.896Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/s568.py\npython3 $S IEC.txt '(?i)zō[sn]|zṓ|juosti|jüosti|juõsti' 250 3; python3 $S IEC.txt '(?i)\\nyūs|\\nyus|jūs|jus ' 250 3; python3 $S incoming/ARY/ARY_pages.txt 'جامه' 300 3; python3 $S incoming/ARY/ARY_pages.txt '\\nشما|شما ' 250 3"
}
```


### [2026-10-17T00:38:07.914Z] TOOL RESULT

```
[IEC.txt leaf 260] Cf. quos-is) iosio (iosmi, iosnu-) “gird, gird on; gird one- sell”. WP I, 209. Cf. iosmn-, ióst- Av. yàh- (. . . aiwi ‘gird on"); yasta, pp. ‘girt’; Gk. cf. zónnüo, zónnumi, fut. zóso; Alb. cf. ngjesh, id. (fr. *en-10si0); OLi. juosmi, Li. jüo- siu, jüosti; OCS po-jasü ‘belt’. (Variants in Skt. ya$u, n. 'embrace', and in Latv. joZu, jozt (1) ‘gird on") iosmn- (iosmà, iosmo-) ‘girth; belt. WP I, 209. Cf. iðsið Gk. zóma, zósma; Alb. cf. i ngjeshém 'com- pact’; Cz. cf. p-ásmo; Li. juosmuo, -eñs ‘girth, w
--
[IEC.txt leaf 128] mio “skin, flay’; Slovak drmat' *téar, tug’; Big. cf. drim “dust. (Isophonic is Latv. drūms ‘gloomy, dingy’) dhrumbó, ið lumber along’. (variant with *-b-. Cf. dhrombh-, dhrmbh-) MHG trumpfen, id.; Li. drumbiü, éti, id. dhrun- ‘rumble, roar’ Go. drunjus ‘din’: Icel. drunur, f. pl. id.; drynja, v. ‘rumble’; Cz. drním, čti, id.; Big. drán! ‘zoom! twang!; Li. druniù, éti ‘snooze’ dhrugh- — dhruuos, à 10 15 20 25 30 35 40 45 210 (Extended forms in) Big. dránkam ‘jangle’; Slovene drndati, id. dhrunuk-, s
--
[IEC.txt leaf 166] ios “sticky; stickiness, glue, paste, clay, loam’. WP I, 619 Oss. (?) årgå “clay, mud’; Gk. gloios, gloía ‘glue’; gloiós ‘slimy; sluggish’; MIr. glaedh, glaoidh ‘glue’; OS klei; LG, Du. klei, OFris. klai; OE clæg ‘clay, loam’; Pol. glej, id.; Li. glájus ‘cake-filling, paste’; cf. glieju, glieti, v. ‘smear’. See next gloim- ‘daub, smear; mud, mucus, slime’. WP I, 619. Cf. gloiió, etc. OHG kleimen ‘mould from clay’; G kleimen and (fr LG) klehmen, LG kleemen “stick, lime, glue, daub’; Kiem ‘daub, mud’
--
[IEC.txt leaf 171]  527, 677 Skt. gayah “house, family; OE cég, cége ‘key’; OFris. ka kei, id., beside keia, v. *pro- tect’; OCS goj ‘peace’ beside (*-0-) gaj ‘grove, copse’, Pol. gaj, Cz. háj, cf. Cz. hájit “protect and OR iz-gój (fey, outlawed’ or sim.); LW in Li. gojus ‘grove’. (Du. kooj ‘cage’ is a LW fr. Lat. cavea) golətis (golt-) “chill, cold, frost’. cf. gel-, geldios, golos MHG kelte, id.; OCS goloti “ice” (golg-, see gelg-. O-gde in OCS *glazü “eye” in glaz-atü ‘eyed’; R glaz, pl. glazà, id. The sense of Cyp
--
[ARY_pages.txt leaf 60] : ۱۳۴-۳۵ ه۷۸ برهان قاطع : ۴۱ نورس کهن (۸0782 010): ۷۹7 فرهنگ معین : ۳ یادداشت. ۱- رابطه‌ی واژه‌ی "آستر"(پهلوی )) با دیگر واژه‌های این فهرست در هیچ کدام از پسگشت‌ها(مراجع) من داده شده است و لذا در جلو واجریشه‌ی هند و اروپایی(شاید) آورده‌ام. ۲ جّم همه‌ی واژه‌های این فهرست (به جز واژه‌ی پهلوی 887۸14): جامه» پوشا که» پوشیدن. ٍ [pdf page 62] یج ی کش ۲ آسمان / ۶۳ ی ای اوستایی (4۳237۸0۷): هام هلندی (لع017): اد ۱۱ نا پارسی باستان ((۶8781۸ 070): اسلاوی کهن (ع1اما5 7ل8نات) ا0): ۸۸8۵۸ ات پهلو ی (۵7آل(۸ط). ۸۹۸۵۲ لهستانی (۳۵/3[4). ۱:۱ کردی (154ص(): ند روسی (5931۸2(): رد۱۹۹۱ افغانی (پشتو) (/۸۳۵7۸2): ۳۹ چکه (0ل
--
[ARY_pages.txt leaf 270] 307517): 22 آلبانی (1427لمقلم): 2037 تخاری ۸ (۸ ((703۸73): هتیت (7177175): 7۸3۸77۲ ۰ ,16 ,71282 [pdf page 271] اّ پسگشت‌ها دب ند 1 (88۸71) :۱۷۸0052/2 8 00200 برهان قاطع رن ۸۳۵ پا شور 9 یادداشت: و چم این واژه در اوستایی و سانسکریت: محکم کردن چم اين واژه در ارمنی: خیاط ربسمان ۰ چم این واژه در اوستی: جامه چم اين واژه در زبانهای تخاری: اجازه دادن» رخصت دادن. چم این واژه در کردی: ریسمان ۲- در زبان پهلوی واژه‌ی 2۸16210 به چم «خیاط» بکار می‌رفته است. اوستایی (۸۲87/27): ید ۱۱ هلندی (7ع017): رید ای بان نی پارسی باستان (۸(۷ای۳87 صا0): لیتوانی (۸2]897لا73ر): نارای ۱۱ ۷-1 با1 1011-08517 پروسی کهن (40۷ا۳#055 
--
[ARY_pages.txt leaf 15] ی قرن‌ها مورد قبول بود و موجب رکود پیشرفت شاخه‌ی عمده‌ای از زبانشناسی شد. ضمناً چون این دیدمان به مذهب وکتاب مقدس متکی برد کسی آنرا مورد تردید و بررسی علمی قرار نمی‌داد. [ در سده‌های شانزدهم و هفدهم میلادی که طی آن آموزش زبانهای خارجی رونق گرفته بود» شماری از دانشمندان اروپایی متوجه شباهت‌هایی میان برخی از زبان‌ها شدند. آنچه که ک‌کم واضح شد این پودکه در اروپا چند خانواده‌ی زبان وجود دارد (ژرمنی و لاتین و اسلاوی وغیره) وهر یک از این خانواده‌ها شامل چند زبان‌اند. مثلاً خانواده‌ی لاتین شامل ایتالیایی و
--
[ARY_pages.txt leaf 24]  تا دهم به زبان آنها نگاشته شده است و اعقاب آنها امروژه در پامیر ۱ زندگی می‌کنند. : گسترش اقوام ترک زبان (سده‌های ششم تا سیزدهم میلادی) موجب آمپزش آنها با ایرانیان و جایگزینی زبان ترکی شدء بطوری که امروزه زبانهای ایرانی در سرزمین‌های خاور دریای خزر و شمال دریای سیاه برافتاده‌اند. نقط در شمال کوه‌های قفقاز اوست‌ها (0888788) که اعقاب الان‌ها . , هستند و جمعیت آنها بالغ بر حدود ۸۰۰ هزار است» به صورت جمهوری خود مختار (جزو روسیه) ‏ وجود دارند. زیان آنها (زبان ارستی) که برخی از ویژگی‌های ایرانی کهن را حفظ
--
[ARY_pages.txt leaf 30] . ۲- زبانهای اسلاوی باختری (لهستانی؛ چکه» اسلوا کی). ۳-زبان‌های اسلاوی جنوبی (بلغاری» اسلوینی» صربی» کرواتی» مقدونی). جمع سخنگویان به این زبان‌ها حدود ۴۵۰ میلیون نفر است. از خاستگاه نخستین اسلاوها اطلاع قطعی در دست نیست. حدس این است که آنها در شمال و شمال خاوری دربای سیاه در اثر آمیزش اقوام ایرانی (مکاها) و مردمان ناشناخته دیگر به وجود آمدند. ولی رشد آنها آنقدر سریع بود که از قرن چهارم تا قرن نهم میلادی از خاور تاکوه‌های اورال و از باختر تا مرز باختری لهستان و از جنوب تا بلفارستان و مقدونیه را تصرف 
--
```


## [2026-10-17T00:38:14.693Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/s568.py\npython3 $S incoming/ARY/ARY_latin_index_pages.txt '(?i)JAME|JAMEH|SHOMA|ŠOMA|ZONNAR|ZUNNAR' 100 6; python3 $S incoming/ARY/ARY_pages.txt 'yos|y[oō]s-|iōs|yeu-' 200 3"
}
```


### [2026-10-17T00:38:15.183Z] TOOL RESULT

```
[ARY_latin_index_pages.txt leaf 16] Slorl ols ppoy SoS oly! ron 2a4 Seat als oll a ohsst sles Semloals (3 SoS ody . 2% ahd OLS 32 41.04 JAMES PARSONS) (51S 3 yesh jar abo 1 SLi sho SLY, LS oy ute sé (THE REMAINS OF JAPHET.., 1767) Se ola Bl
--
NO HIT incoming/ARY/ARY_pages.txt yos|y[oō]s-|iōs|yeu-
```


## [2026-10-17T00:38:20.584Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; F=tools/fetch_source.py; for w in جامه شما زنار پیژامه چمدان پیجامه; do p=$(python3 $F \"https://vajehyab.com/moein/$w\" --note \"page 568, Mo'in (MON) entry for $w\" 2>&1|tail -1); echo \"== $w $p\"; python3 -c \"\nimport re,sys;t=re.sub(r'\\s+',' ',open('$p').read());i=t.find('معین');print(t[:120]);\nfor m in list(re.finditer('$w',t))[2:5]: print('  >',t[m.start():m.start()+300])\n\"; done",
 "timeout": 300000
}
```


### [2026-10-17T00:38:23.820Z] TOOL RESULT

```
== جامه /home/sfmqrb/git/rishe-private/data/verification/sources/web/bd76d1e20f7002a1.txt
URL: https://vajehyab.com/moein/جامه FETCHED: 2026-10-17T00:38:21Z STATUS: 200 TITLE: معنی جامه | فرهنگ انتشارات معین | 
  > جامه | فرهنگ انتشارات معین | واژه یاب 26 فرهنگ همه دیکشنری مترادف طیفی آزاد + همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه جامه فرهنگ انتشارات معین (مِ) [ په . ] (اِ.) 1 - لباس ، تن پوش . 2 - جام ، صراحی . 3 - پارچه ، پارچة نادوخته . ؛~ عباسیان کنایه از: لباس سیاه . ؛~ فرو نیل کردن کنایه از: سیاه 
  > جامه فرهنگ انتشارات معین (مِ) [ په . ] (اِ.) 1 - لباس ، تن پوش . 2 - جام ، صراحی . 3 - پارچه ، پارچة نادوخته . ؛~ عباسیان کنایه از: لباس سیاه . ؛~ فرو نیل کردن کنایه از: سیاه کردن لباس به نشانة عزادار شدن . ؛~ قبا کردن کنایه از: پیراهن دریدن از شدت شور و وجد یا اندوه . جامه در فرهنگ‌های دیگر معنی جا
  > جامه در فرهنگ‌های دیگر معنی جامه در لغت‌نامه دهخدا معنی جامه در فرهنگ فارسی عمید / قربان‌زاده معنی جامه در دیکشنری فارسی به عربی معنی جامه در دیکشنری فارسی به انگلیسی معنی جامه در دیکشنری فارسی به ترکی معنی جامه در گویش مازنی معنی جامه در فرهنگ مترادف و متضاد واژه‌های مشابه جامة نادوخته جامه دریدن ج
== شما /home/sfmqrb/git/rishe-private/data/verification/sources/web/ed11f5d3b4c038b0.txt
URL: https://vajehyab.com/moein/شما FETCHED: 2026-10-17T00:38:21Z STATUS: 200 TITLE: معنی شما | فرهنگ انتشارات معین | وا
  > شما | فرهنگ انتشارات معین | واژه یاب 26 فرهنگ همه دیکشنری مترادف طیفی آزاد + همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه شما فرهنگ انتشارات معین (ش ) [ فر . ] (اِ.) تصویری کلی از چیزی بدون جزییات آن . شما در فرهنگ‌های دیگر معنی شما در لغت‌نامه دهخدا معنی شما در فرهنگ فارسی عمید / قربان‌زاده معنی 
  > شما فرهنگ انتشارات معین (ش ) [ فر . ] (اِ.) تصویری کلی از چیزی بدون جزییات آن . شما در فرهنگ‌های دیگر معنی شما در لغت‌نامه دهخدا معنی شما در فرهنگ فارسی عمید / قربان‌زاده معنی شما در دیکشنری فارسی به عربی معنی شما در دیکشنری فارسی به انگلیسی معنی شما در دیکشنری فارسی به ترکی معنی شما در گویش اصفهانی
  > شما در فرهنگ‌های دیگر معنی شما در لغت‌نامه دهخدا معنی شما در فرهنگ فارسی عمید / قربان‌زاده معنی شما در دیکشنری فارسی به عربی معنی شما در دیکشنری فارسی به انگلیسی معنی شما در دیکشنری فارسی به ترکی معنی شما در گویش اصفهانی معنی شما در گویش کرمانشاه معنی شما در گویش خلخال معنی شما در گویش مازنی واژه‌ها
== زنار /home/sfmqrb/git/rishe-private/data/verification/sources/web/1ce0170a2dec08f6.txt
URL: https://vajehyab.com/moein/زنار FETCHED: 2026-10-17T00:38:22Z STATUS: 200 TITLE: معنی زنار | فرهنگ انتشارات معین | 
  > زنار | فرهنگ انتشارات معین | واژه یاب 26 فرهنگ همه دیکشنری مترادف طیفی آزاد + همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه زنار فرهنگ انتشارات معین (زُ نّ) [ یو. ] (اِ.) 1 - رشته ای که مسیحیان به وسیلة آن صلیب را به گردن آویزند. 2 - کُستی ؛ شالی که زردشتیان به کمر بندند. زنار در فرهنگ‌های دیگر معن
  > زنار فرهنگ انتشارات معین (زُ نّ) [ یو. ] (اِ.) 1 - رشته ای که مسیحیان به وسیلة آن صلیب را به گردن آویزند. 2 - کُستی ؛ شالی که زردشتیان به کمر بندند. زنار در فرهنگ‌های دیگر معنی زنار در لغت‌نامه دهخدا معنی زنار در فرهنگ فارسی عمید / قربان‌زاده معنی زنار در دیکشنری عربی به فارسی معنی زنار در واژه‌نامه
  > زنار در فرهنگ‌های دیگر معنی زنار در لغت‌نامه دهخدا معنی زنار در فرهنگ فارسی عمید / قربان‌زاده معنی زنار در دیکشنری عربی به فارسی معنی زنار در واژه‌نامه آزاد واژه‌های مشابه زنار بستن زار زار زار زار و نزار زاراغنگ زارج گندم زار چمن زار سبزه زار شن زار خرید اشتراک افزودن واژه افزونه مرورگر تماس درباره
== پیژامه /home/sfmqrb/git/rishe-private/data/verification/sources/web/b501a71b342f33c8.txt
URL: https://vajehyab.com/moein/پیژامه FETCHED: 2026-10-17T00:38:22Z STATUS: -1 TITLE: FETCH FAILED: HTTP Error 404: Not
== چمدان /home/sfmqrb/git/rishe-private/data/verification/sources/web/bce44efaa4130141.txt
URL: https://vajehyab.com/moein/چمدان FETCHED: 2026-10-17T00:38:23Z STATUS: 200 TITLE: معنی چمدان | فرهنگ انتشارات معین 
  > چمدان | فرهنگ انتشارات معین | واژه یاب 26 فرهنگ همه دیکشنری مترادف طیفی آزاد + همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه چمدان فرهنگ انتشارات معین (چَ مِ) [ روس . ] (اِمر.) کیف بزرگ چرمی یا برزنتی یا غیره که هنگام سفر لباس ها یا لوازم دیگر را در آن نهند. چمدان در فرهنگ‌های دیگر معنی چمدان در لغ
  > چمدان فرهنگ انتشارات معین (چَ مِ) [ روس . ] (اِمر.) کیف بزرگ چرمی یا برزنتی یا غیره که هنگام سفر لباس ها یا لوازم دیگر را در آن نهند. چمدان در فرهنگ‌های دیگر معنی چمدان در لغت‌نامه دهخدا معنی چمدان در فرهنگ فارسی عمید / قربان‌زاده معنی چمدان در دیکشنری فارسی به عربی معنی چمدان در دیکشنری فارسی به ان
  > چمدان در فرهنگ‌های دیگر معنی چمدان در لغت‌نامه دهخدا معنی چمدان در فرهنگ فارسی عمید / قربان‌زاده معنی چمدان در دیکشنری فارسی به عربی معنی چمدان در دیکشنری فارسی به انگلیسی معنی چمدان در دیکشنری فارسی به ترکی معنی چمدان در گویش اصفهانی معنی چمدان در گویش کرمانشاه معنی چمدان در گویش خلخال معنی چمدان د
== پیجامه /home/sfmqrb/git/rishe-private/data/verification/sources/web/20aa4e4a746bfba8.txt
URL: https://vajehyab.com/moein/پیجامه FETCHED: 2026-10-17T00:38:23Z STATUS: -1 TITLE: FETCH FAILED: HTTP Error 404: Not
```


## [2026-10-17T00:38:29.652Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; F=tools/fetch_source.py; for w in پیژاما; do p=$(python3 $F \"https://vajehyab.com/moein/$w\" --note \"page 568, Mo'in (MON) entry for $w\" 2>&1|tail -1); python3 -c \"\nimport re;t=re.sub(r'\\s+',' ',open('$p').read());print(t[:150]);i=t.find('فرهنگ انتشارات معین (');print(t[i:i+300])\"; done"
}
```


### [2026-10-17T00:38:30.534Z] TOOL RESULT

```
URL: https://vajehyab.com/moein/پیژاما FETCHED: 2026-10-17T00:38:30Z STATUS: 200 TITLE: معنی پیژاما | فرهنگ انتشارات معین | واژه یاب معنی پیژاما | فره
```


## [2026-10-17T00:38:34.579Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; python3 -c \"\nimport re,hashlib;u='https://vajehyab.com/moein/پیژاما';h=hashlib.sha1(u.encode()).hexdigest()[:16];t=re.sub(r'\\s+',' ',open(h+'.txt').read());i=t.find('قافیه');print(t[i:i+400])\""
}
```


### [2026-10-17T00:38:34.936Z] TOOL RESULT

```
قافیه پیژاما فرهنگ انتشارات معین [ انگ . ] (اِ.) نک پی جامه . پیژاما در فرهنگ‌های دیگر معنی پیژاما در لغت‌نامه دهخدا معنی پیژاما در فرهنگ فارسی عمید / قربان‌زاده معنی پیژاما در فرهنگ مترادف و متضاد خرید اشتراک افزودن واژه افزونه مرورگر تماس درباره نسخه جدید
```


## [2026-10-17T00:38:41.420Z] TOOL CALL #73: Bash

```json
{
 "command": "SP=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; pdftoppm -f 568 -l 568 -r 130 -png -singlefile /home/sfmqrb/git/rishe-private/EtymologicalDictionary-persian-english.pdf $SP/pg568"
}
```


### [2026-10-17T00:38:42.140Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:38:45.972Z] TOOL CALL #74: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg568.png"
}
```


### [2026-10-17T00:38:45.995Z] TOOL RESULT

```

```


## [2026-10-17T00:39:08.717Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; curl -sL -m 60 -o bqtv2-568-n496.jpg \"https://archive.org/download/borhan-ghate-v2/page/n496_w900.jpg\"; python3 -c \"\nfrom PIL import Image; im=Image.open('bqtv2-568-n496.jpg'); w,h=im.size; im.crop((0,0,w,int(h*0.15))).save('bqtv2-568-n496top.png')\""
}
```


### [2026-10-17T00:39:11.182Z] TOOL RESULT

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    from PIL import Image; im=Image.open('bqtv2-568-n496.jpg'); w,h=im.size; im.crop((0,0,w,int(h*0.15))).save('bqtv2-568-n496top.png')
    ^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'PIL'
```


## [2026-10-17T00:39:16.383Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; magick bqtv2-568-n496.jpg -crop 100%x12%+0+0 bqtv2-568-n496top.png 2>&1 || convert bqtv2-568-n496.jpg -crop 100%x12%+0+0 bqtv2-568-n496top.png"
}
```


### [2026-10-17T00:39:16.980Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:39:21.283Z] TOOL CALL #77: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqtv2-568-n496top.png"
}
```


### [2026-10-17T00:39:21.319Z] TOOL RESULT

```

```


## [2026-10-17T00:39:36.748Z] TOOL CALL #78: Bash

```json
{
 "command": "D=/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT; command ls $D | grep -E '^(556|660|1033|1291)\\.' ; \ncat > $D/556.vision.txt <<'EOF'\n[BQT vol 2, printed p. 556 = archive.org borhan-ghate-v2 leaf n14; transcribed by eye, page 568 verification]\nجامه - بر وزن نامه، پارچهٔ بافتهٔ نادوخته را گویند(۶) - و بمعنی قبای پوشیدنی هم ...\nحاشیهٔ ۶ (معین): هندی باستان yam با chardish وغیره (بلم، حمایت)، پهلوی jâmak و yâmak «اسنق ۴۱۲». مولر بهتر توضیح داده و «جامه» را از کلمهٔ پهلوی yâmak = پارسی باستان yâhma، و یونانی Zôma دانسته «هوبشمان ۴۱۲» و رك: نیبرگ ۲۴۸. استی jauma «ک. ا ص ۱۲۲» طبری jema (پیراهن) «نصاب طبری ۱۰۳».\n(also on this page: جامگی، footnote ۲ «از: جامه (جامك) + ی (نسبت)».)\nEOF\ncat > $D/660.vision.txt <<'EOF'\n[BQT vol 2, printed p. 660 = archive.org borhan-ghate-v2 leaf n118; transcribed by eye, page 568 verification]\n* چمدان - بفتح اول و دوم: دزی چمدان معرب را از فارسی جامدان (جامه دان) مأخوذ میداند «دزی ج۱ ص۲۱۲». کریستنسن کلمهٔ استی cemodan را از روسی عاریت میداند «ک. است ۱۱۶»؛ صندوق چرمین که جامه و اشیاء دیگر در آن نهند. رک: چرمدان و خرمدان. [with a picture captioned چمدان]\nEOF\ncat > $D/1033.vision.txt <<'EOF'\n[BQT vol 2, printed p. 1033 (no running head; chapter opening «بیان پانزدهم در زای نقطه دار با نون»; next leaf n496 = p.1034) = archive.org borhan-ghate-v2 leaf n495; transcribed by eye, page 568 verification]\nزنار(۳) - بضم اول و ثانی مشدد بر وزن کفار، هر رشته را گویند عموماً و رشته‌ای که بت پرستان و آتش پرستان با خود دارند خصوصاً.\nحاشیهٔ ۳ (معین): از یونانی جدید Zônári، از یونانی قدیم Zônárion مصغر Zônê بمعنی کمربند و منطقه «فرهنگ یونانی - انگلیسی لیدل واسکات» «نفس». زنار کمربندی بوده که ذمیان نصرانی در مشرق زمین بامر مسلمانان مجبور بوده‌اند داشته باشند تا بدینوسیله از مسلمانان ممتاز گردند، چنانکه یهودیان مجبور بوده‌اند علی (وصله‌ای علی رنگ) بر روی لباس خود بدوزند، در کتاب‌های فارسی گاه زنار بکستی (= کشتی) (ه.م.) زرتشتیان اطلاق شده است. رك: نو روزنامه. تعلیقات ص ۱۲۳.\nEOF\ncat > $D/1291.vision.txt <<'EOF'\n[BQT:1291 — NOT IN THE SCAN. Checked during page 568 verification: BQT_v3_picofile.pdf pdf page 80 = printed 1289, pdf 81 = 1290, pdf 82 = 1295 (شمع ... شملیز). Printed pages 1291-1294 (which should contain شما) are missing from this scan. The cached 1291.png/1291.txt actually show printed p. 1295.]\nEOF\necho ok"
}
```


### [2026-10-17T00:39:37.061Z] TOOL RESULT

```
1291.png
1291.txt
ok
```


## [2026-10-17T00:42:05.445Z] TOOL CALL #79: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build568.py <<'PYEOF'\nimport json\nW=\"https://en.wiktionary.org/wiki/\"\nV=\"https://vajehyab.com/moein/\"\nPOK_yos={\"src\":\"POK\",\"where\":\"POK_02.txt leaf 171 (p.513)\",\"stance\":\"supports\",\"note\":\"'iō[u]s- : iūs- ... gürten; iōs-to-s gegürtet, iōs-men- n. Gurt. Av. yåŋhayeiti (meist mit aiwi-) gürtet, Partiz. yāsta- gegürtet, yāh n. Gürtelschnur; gr. ζώννυμι, ζωστός, ζωστήρ, ζῶμα, ζώνη ...; lit. júosti; aksl. pojasъ'.\"}\nWLD_yos={\"src\":\"WLD\",\"where\":\"WLD_Bd1_pages.txt leaf 217 (Bd. I 209)\",\"stance\":\"supports\",\"note\":\"same article as Pokorny: 'lit. jüosiu, juosti gürten, juostas gegürtet, júosta Gürtel; aksl. pojasъ, -jasati gürten' with Greek ζώνη, ζῶμα.\"}\nAHD_yos={\"src\":\"AHD\",\"where\":\"AHD_watkins1985.txt leaf 111, s.v. yōs-\",\"stance\":\"supports\",\"note\":\"'yōs-. To gird. 1. Suffixed form *yōs-ter- in Greek zōstēr, girdle: ZOSTER. 2. Suffixed form *yōs-nā in Greek zōnē, girdle: ZONE; EVZONE. [Pok. iō(u)s- 513.]'\"}\nIEC_yos={\"src\":\"IEC\",\"where\":\"IEC.txt leaf 260, s.v. iosio / iosmn-\",\"stance\":\"supports\",\"note\":\"'iosio ... gird, gird on. WP I, 209. Av. yāh- (aiwi 'gird on'); yāsta, pp. girt; Gk. zṓnnumi ...; Li. júosti; OCS po-jasŭ belt'; 'iosmn- girth, belt: Gk. zōma, zōsma; Li. juosmuo'.\"}\nSYN_yos={\"src\":\"SYN\",\"where\":\"SYN.txt leaf 482, p.434 §6.57 BELT, GIRDLE\",\"stance\":\"supports\",\"note\":\"'1. Derivs. of *yōs- gird (perh. orig. *you-s-, extension of *yeu- bind) in Grk. ζώννυμι, ζώνη, Lith. juosti, ChSl. po-jasati, Av. yāh-, pple. yāsta-. Walde-P. 1.209.'\"}\nPOK_yu={\"src\":\"POK\",\"where\":\"POK_02.txt leaf 171-172 (pp.513-514)\",\"stance\":\"supports\",\"note\":\"'1. iu- ihr, ursprüngl. nur Nom.; Kasus obliqui vom St. ues-, uos- ... ai. yūyám, av. yūžəm, gathav. yūš; got. jus ... ; ues-, us-: ai. vaḥ, av. vō enkl.; Akk. *us-sme ... ai. yuṣmān Akk., av. Abl. yūšmat'.\"}\nWLD_yu={\"src\":\"WLD\",\"where\":\"WLD_Bd1_pages.txt leaf 217 (Bd. I 209-210)\",\"stance\":\"supports\",\"note\":\"'1. iu- ihr, ursprgl. nur Nom.; Kasus obliqui vom St. ues-, uo(s)-. Ai. yuvám Du., yūyám Pl., av. yūžəm, gathav. yūš; ... got. jus ihr'.\"}\nAHD_yu={\"src\":\"AHD\",\"where\":\"AHD_watkins1985.txt leaf 111, s.v. yu-1\",\"stance\":\"supports\",\"note\":\"'yu-1. You. Second person (plural) pronoun. Germanic *jūz (nominative) and *iwwiz (oblique) in Old English gē and ēow, you: YE, YOU. [Pok. 1. iu- 513.]'\"}\n\nnodes0=[\n dict(id=1,lang=\"Avestan / Old Persian\",words=\"yâh 4; yâhma; yâsta, yânhaeiti\",verdict=\"plausible\",\n  derivation=\"Avestan yāh- 'to gird' (pres. yåŋhaya-, 3sg. yåŋhayeiti, mostly with aiwi- 'put on [belt, clothes]'), past participle yāsta- 'girded', and the noun yāh- n. 'girdle, belt-cord' are all attested (Bartholomae) and continue PIE *yōs-/*yeh3s- exactly as in Greek ζωστός and Lithuanian juostas. The form 'yâhma' 'cover, clothes' is NOT attested in Avestan or Old Persian: it is the Old Persian *yāhma- reconstructed by Fr. Müller and Hübschmann (= Greek ζῶμα, Lith. juosmuo) to explain Pahlavi yāmak; Nourai prints it as if it were a real word. Attested items are confirmed; yâhma should carry an asterisk.\",\n  derivation_fa=\"اوستایی yāh- «کمر بستن» (ستاک حال yåŋhaya-، سوم شخص yåŋhayeiti، بیشتر با پیشوند aiwi- به معنای «پوشیدن، کمربند بستن»)، صفت مفعولی yāsta- «کمربسته» و اسم yāh- «کمربند، بند کمر» همه در اوستا گواهی شده‌اند و از ریشهٔ هندواروپایی *yōs- آمده‌اند (بارتولومه، پوکورنی). اما «yâhma» واژه‌ای گواهی‌شده نیست؛ صورتی بازسازی‌شدهٔ پارسی باستان (*yāhma-) است که مولر و هوبشمان برای توضیح پهلوی yāmak پیشنهاد کرده‌اند. پس بخش گواهی‌شده درست است و yâhma را باید با ستاره و با احتیاط پذیرفت.\",\n  sources=[W+\"ζώνη\"],\n  ref_check=[{\"ref\":\"POK:513\",\"status\":\"supports\",\"note\":\"POK_02.txt leaf 171: 'Av. yåŋhayeiti (meist mit aiwi-) gürtet, Partiz. yāsta- gegürtet, yāh n. Gürtelschnur' under iō[u]s- 'gürten'. No *yāhma.\"},\n   {\"ref\":\"KLN:1770\",\"status\":\"supports\",\"note\":\"KLN_1971.txt s.v. zone: 'fr. I.-E. base *yōs-, to gird; girdle, whence also Avestic yāsta-, girt, Lith. juosiu, juosti, to gird, OSlav. po-jasŭ girdle, Alb. n-gesh I gird'.\"},\n   {\"ref\":\"SYN:434\",\"status\":\"supports\",\"note\":\"SYN p.434 §6.57: 'Av. yāh-, pple. yāsta-' listed under derivs. of *yōs- 'gird'; table gives Av. yāh- for BELT.\"}],\n  consulted=[{\"src\":\"BRT\",\"where\":\"BRT.txt lines ~21697-21720 (col. 1284-1286)\",\"stance\":\"supports\",\"note\":\"'yāh- V. gürten. Praes. 24 yåŋhaya-. PPfP. yāsta-' ... 'mit aiwi etwas sich umtun, anlegen, anziehen (den Gürtel, Kleidungsstücke)' ... 'yāh- n. Gürtel, Gürtelschnur'. No yāhma- entry.\"},\n   POK_yos,WLD_yos,{\"src\":\"HUB\",\"where\":\"HUB.txt leaf 59 (p.49, no. 412)\",\"stance\":\"partial\",\"note\":\"'np. jāma Kleid aus phl. yāmak = ap. *yāhma' — the OP form is starred (reconstructed), not attested.\"}]),\n dict(id=2,lang=\"Pahlavi\",words=\"yâmak\",verdict=\"plausible\",\n  derivation=\"Pahlavi jāmag (book script yʾmk', also read yāmak; MacKenzie 'clothing, garment', NP jāma) is secure. Its origin is debated: Fr. Müller and Hübschmann (Persische Studien no. 412) derive it from OP *yāhma- = Greek ζῶμα 'girdle', i.e. from PIE *yōs- 'gird' (Nourai's arrow, also given by Mo'in in Borhan); Horn (no. 412) and Wiktionary instead connect it with Old Indic yam- 'to hold out (a shelter, chardis-)', PIE *yem- 'hold', via *yāma-ka-. Intervocalic/OIr. -hm- > MP -m- is regular (cf. OP taumā > MP tōhm), so Müller's derivation is phonetically sound but not proven.\",\n  derivation_fa=\"پهلوی jāmag / yāmak (به خط پهلوی yʾmk) به معنای «جامه، تن‌پوش» به‌خوبی گواهی شده است (مکنزی، نیبرگ). دربارهٔ ریشهٔ آن دو نظر هست: مولر و هوبشمان آن را از پارسی باستان بازسازی‌شدهٔ *yāhma- هم‌ریشه با یونانی ζῶμα «کمربند» و از ریشهٔ *yōs- «کمر بستن» می‌دانند (همان که نورایی آورده و معین هم در حاشیهٔ برهان پذیرفته)، اما هرن و ویکی‌واژه آن را به ریشهٔ yam- «نگه داشتن، پناه دادن» (سنسکریت yam- با chardis-) می‌پیوندند. ادعای نورایی پذیرفتنی است ولی قطعی نیست.\",\n  sources=[W+\"جامه\"],\n  ref_check=[{\"ref\":\"HUB:49\",\"status\":\"supports\",\"note\":\"HUB.txt leaf 59 (p.49), no. 412: 'Fr. Müller vergleicht besser np. jāma Kleid aus phl. yāmak = ap. *yāhma mit gr. ζῶμα, WZKM. 8, 93.'\"},\n   {\"ref\":\"HRN:93\",\"status\":\"contradicts\",\"note\":\"HRN.txt leaf 114 (p.93), no. 412: 'jāme Kleid, Gewand. ai. √yam- mit chardis- etc. ein Dach, einen Schirm, Schutz überhalten, lett. jumt dachdecken ... phlv. jāmak bezw. yāmak' — Horn has the Pahlavi word but derives it from yam-, not yāh-.\"}],\n  consulted=[{\"src\":\"PHD\",\"where\":\"PHD.txt line 412\",\"stance\":\"supports\",\"note\":\"'jāmag [yʾmk' | M jʾm(g), N jāma] clothing, garment' (OCR garbled) — word and sense confirmed, no etymology.\"},\n   {\"src\":\"NYB\",\"where\":\"NYB_vol2_glossary.txt line 1205, s.v. dast\",\"stance\":\"supports\",\"note\":\"'2. ~ i yāmak a set of clothes' — confirms Pahlavi yāmak 'clothes'.\"},\n   {\"src\":\"BQT\",\"where\":\"vol 2 p.556 footnote 6 (ocr/BQT/556.vision.txt)\",\"stance\":\"partial\",\"note\":\"Mo'in gives both views: 'هندی باستان yam با chardish ... پهلوی jâmak و yâmak «اسنق ۴۱۲». مولر بهتر توضیح داده و «جامه» را از کلمهٔ پهلوی yâmak = پارسی باستان yâhma و یونانی Zôma دانسته «هوبشمان ۴۱۲»'.\"}]),\n dict(id=3,lang=\"Persian\",words=\"jâmeh; pâ-jâmeh; jâmeh-dân\",verdict=\"plausible\",\n  derivation=\"NP jāma 'garment, clothes' < MP jāmag (loss of final -ag > -a, regular). pā-jāma (older pāy-jāma) 'trousers' = pā(y) 'leg, foot' + jāma; jāma-dān 'clothes-chest, portmanteau' = jāma + suffix -dān 'container'. The compounds are transparent and confirmed; the ultimate link to PIE *yōs- inherits the uncertainty of node 2 (Horn and Wiktionary prefer *yem- 'hold').\",\n  derivation_fa=\"«جامه» از فارسی میانهٔ jāmag است (افتادن -ag پایانی در فارسی نو، قاعده‌مند). «پاجامه» (کهن‌تر: پای‌جامه) از «پا(ی)» + «جامه» به معنای «تن‌پوش پا، شلوار» است و «جامه‌دان» از «جامه» + پسوند «-دان» (ظرف) به معنای «صندوق رخت». این ترکیب‌ها روشن و درست‌اند؛ تنها پیوند نهایی «جامه» با ریشهٔ *yōs- همان تردید گره پیشین را دارد (هرن و ویکی‌واژه ریشهٔ yam- را ترجیح می‌دهند).\",\n  sources=[W+\"جامه\",W+\"پاجامه\",V+\"جامه\"],\n  ref_check=[{\"ref\":\"BQT:556\",\"status\":\"supports\",\"note\":\"BQT vol 2 p.556 (archive.org borhan-ghate-v2 leaf n14; ocr/BQT/556.vision.txt): headword جامه 'پارچهٔ بافتهٔ نادوخته ... قبای پوشیدنی'; footnote 6: 'جامه را از کلمهٔ پهلوی yâmak = پارسی باستان yâhma و یونانی Zôma دانسته «هوبشمان ۴۱۲»'. This is clearly Nourai's source for yâhma.\"},\n   {\"ref\":\"BQT:660\",\"status\":\"supports\",\"note\":\"BQT vol 2 p.660 (leaf n118; ocr/BQT/660.vision.txt), s.v. چمدان: 'دزی چمدان معرب را از فارسی جامدان (جامه دان) مأخوذ میداند' — supports jāma-dān.\"}],\n  consulted=[{\"src\":\"HRN\",\"where\":\"HRN.txt leaf 114 (p.93) no. 412\",\"stance\":\"contradicts\",\"note\":\"jāme from √yam- (Skt. yam- with chardis-), not from yāh-.\"},\n   {\"src\":\"HUB\",\"where\":\"HUB.txt leaf 59 (p.49) no. 412\",\"stance\":\"supports\",\"note\":\"'np. jāma Kleid aus phl. yāmak = ap. *yāhma mit gr. ζῶμα'.\"},\n   {\"src\":\"MON\",\"where\":\"vajehyab.com/moein/جامه\",\"stance\":\"supports\",\"note\":\"'جامه (مِ) [په.] (اِ.) ۱- لباس، تن پوش. ۲- جام، صراحی. ۳- پارچه' — Pahlavi origin.\"},\n   {\"src\":\"LKT\",\"where\":\"LKT.txt leaf 78 (no. 552)\",\"stance\":\"supports\",\"note\":\"'pers. jāmadān Kleiderbehälter, Koffer [aus pers. jāma Tuch, Kleid Horn NpEt S.93 Nr.412, und Suffix -dān Behälter]'.\"},\n   {\"src\":\"CHEUNG\",\"where\":\"CHEUNG.txt grep 'jāma|yām-'\",\"stance\":\"silent\",\"note\":\"no entry for jāma (noun, not a verb).\"},\n   {\"src\":\"ARY\",\"where\":\"ARY_pages.txt / latin index grep 'جامه', 'JAME'\",\"stance\":\"silent\",\"note\":\"جامه appears only as a gloss in other entries; no etymology.\"}]),\n dict(id=4,lang=\"Hindustani\",words=\"pâě-jâma\",verdict=\"confirmed\",\n  derivation=\"Hindi paijāmā / pājāmā, Urdu pā'ejāma 'loose drawers tied at the waist' is a loan of Persian pāy-jāma / pā-jāma 'leg-garment', brought to India with Persian as the Mughal court language; the -ai-/-ā'e- reflects Persian pāy 'foot'. Hobson-Jobson and Klein agree.\",\n  derivation_fa=\"هندی paijāmā / اردو پائجامه به معنای «شلوار گشادی که با بند به کمر بسته می‌شود» وام‌واژه از فارسی «پای‌جامه / پاجامه» است که با رواج فارسی در دربار گورکانیان هند به آن‌جا رفت. هابسن-جابسن و کلاین همین را می‌گویند؛ ادعای نورایی درست است.\",\n  sources=[W+\"pajamas\"],\n  ref_check=[{\"ref\":\"HJB:748\",\"status\":\"supports\",\"note\":\"HJB.txt leaf 794 (p.748): 'PYJAMMAS, s. Hind. pāi-jāma (see JAMMA), lit. leg-clothing. A pair of loose drawers or trowsers, tied round the waist ... adopted from the Mahommedans by Europeans as an article of dishabille and of night attire'.\"}],\n  consulted=[{\"src\":\"KLN\",\"where\":\"KLN_1966.txt leaf 594 s.v. pajamas\",\"stance\":\"supports\",\"note\":\"'Hind. pajama, paijama, lit. leg-garment, fr. Pers. pā, pāi, foot, leg, and jāma, clothing, garment'.\"},\n   {\"src\":\"AID\",\"where\":\"AID.txt grep 'pyjama|paijama'\",\"stance\":\"silent\",\"note\":\"no hit found in Whitworth's OCR.\"}]),\n dict(id=5,lang=\"English\",words=\"pajamas\",verdict=\"confirmed\",\n  derivation=\"English pyjamas / pajamas (first recorded c. 1800) was taken by British colonials in India from Hindustani pā(i)jāma; originally loose trousers, it came to mean night attire in the later 19th century. Wiktionary, Klein and Hobson-Jobson agree.\",\n  derivation_fa=\"انگلیسی pyjamas / pajamas (از حدود ۱۸۰۰ م.) را انگلیسی‌های مقیم هند از هندوستانی pā(i)jāma گرفتند؛ نخست به معنای شلوار گشاد بود و در سدهٔ نوزدهم به «لباس خواب» تحول معنایی یافت. ادعای نورایی درست است.\",\n  sources=[W+\"pajamas\"],\n  ref_check=[{\"ref\":\"KLN\",\"status\":\"supports\",\"note\":\"KLN_1966.txt leaf 594: 'pajamas, pyjamas, n. pl., loose trousers or drawers. — Hind. pajama, paijama, lit. leg-garment, fr. Pers. pā, pāi ... and jāma'.\"},\n   {\"ref\":\"AHD\",\"status\":\"not_checked\",\"note\":\"1976 AHD main-dictionary entry not online; the Watkins appendix has no entry for a non-IE-root loan.\"}],\n  consulted=[{\"src\":\"HJB\",\"where\":\"p.748\",\"stance\":\"supports\",\"note\":\"'the word is now used in London shops'; English took it from Hind. pāi-jāma.\"},\n   {\"src\":\"SKT\",\"where\":\"SKT.txt grep 'pyjama|pajama'\",\"stance\":\"silent\",\"note\":\"not in Skeat's Concise dictionary.\"}]),\n dict(id=6,lang=\"French\",words=\"\",verdict=\"confirmed\",\n  derivation=\"Pass-through node for French pyjama (attested from 1837), borrowed from English pyjamas and pronounced /piʒama/ with French j = [ʒ]; Wiktionary (French section) and TLFi give English (< Urdu/Hindi < Persian) as the source.\",\n  derivation_fa=\"این گره برای فرانسوی pyjama است (از ۱۸۳۷ م.) که از انگلیسی pyjamas وام گرفته شده و حرف j در آن به آوای «ژ» خوانده می‌شود. ویکی‌واژه همین را تأیید می‌کند؛ ادعای نورایی درست است.\",\n  sources=[W+\"pyjama#French\"],\n  ref_check=[{\"ref\":\"ETM:63\",\"status\":\"not_checked\",\"note\":\"ETM not accessible (refs_online.json: 'not found').\"}],\n  consulted=[{\"src\":\"KLN\",\"where\":\"KLN_1966.txt s.v. pajamas\",\"stance\":\"silent\",\"note\":\"Klein does not mention French pyjama.\"},\n   {\"src\":\"FSD\",\"where\":\"FSD vols grep 'pyjama'\",\"stance\":\"silent\",\"note\":\"no French form discussed.\"}]),\n dict(id=7,lang=\"Persian\",words=\"pîjâmeh\",verdict=\"plausible\",\n  derivation=\"Modern Persian pižāma / pižāme (also written pi-jāme) 'pyjamas' is a re-borrowing of the European word that ultimately came from Persian pāy-jāma: a round trip Persian > Hindustani > English > (French) > Persian. The ž [ʒ] points to French pyjama (or Russian пижама) as the immediate donor, which matches Nourai's French arrow; Mo'in tags پیژاما as [انگ.] (English) and Wiktionary also says British English. The round trip is confirmed; the exact last donor (French vs English/Russian) is uncertain.\",\n  derivation_fa=\"«پیژاما / پیژامه» (و «پی‌جامه») در فارسی امروز وام‌واژه‌ای بازگشتی است: فارسی «پای‌جامه» ← هندوستانی ← انگلیسی ← (فرانسوی) ← دوباره فارسی. آوای «ژ» نشان می‌دهد که واسطهٔ آخر به احتمال زیاد فرانسوی pyjama (یا روسی پیژاما) بوده است، چنان‌که نورایی آورده؛ اما معین آن را [انگ.] می‌داند و ویکی‌واژه هم انگلیسی بریتانیایی را منبع می‌شمارد. بازگشت واژه قطعی است و زبان واسطهٔ آخر محل تردید.\",\n  sources=[W+\"پیژامه\",V+\"پیژاما\"],\n  ref_check=[{\"ref\":\"MON:868,902\",\"status\":\"partial\",\"note\":\"Mo'in online (vajehyab.com/moein/پیژاما): 'پیژاما [انگ.] (اِ.) نک پی جامه' — Mo'in has the word but tags it English, not French. Page numbers cannot be mapped online.\"}],\n  consulted=[{\"src\":\"BQT\",\"where\":\"vol 2 grep 'پیژاما|پیجامه'\",\"stance\":\"silent\",\"note\":\"modern loan, not in Borhan.\"},\n   {\"src\":\"ARY\",\"where\":\"ARY_pages.txt grep\",\"stance\":\"silent\",\"note\":\"not listed.\"}]),\n dict(id=8,lang=\"Russian\",words=\"čamadan\",verdict=\"confirmed\",\n  derivation=\"Russian чемодан čemodán 'suitcase' (pronounced [tɕɪmɐˈdan], so Nourai's čamadan is a phonetic spelling, not a misreading) came via a Turkic intermediary (Tatar/Turkish čamadan, çamadan) from Persian jāma-dān 'clothes-chest'. Lokotsch and Wiktionary both give this route: Persian j- > Turkic č-, -a- > Russian -e- in the unstressed syllable.\",\n  derivation_fa=\"روسی чемодан (چِمادان، به تلفظ [tɕɪmɐˈdan]) به معنای «چمدان» از راه زبان‌های ترکی (تاتاری/ترکی çamadan) از فارسی «جامه‌دان» گرفته شده است؛ «ج» فارسی در ترکی «چ» شده است. نگارش čamadan در کتاب ضبط آوایی است نه خطا. لوکوچ و ویکی‌واژه همین مسیر را تأیید می‌کنند.\",\n  sources=[W+\"чемодан\"],\n  ref_check=[{\"ref\":\"ETM:64\",\"status\":\"not_checked\",\"note\":\"ETM not accessible.\"}],\n  consulted=[{\"src\":\"LKT\",\"where\":\"LKT.txt leaf 78 (no. 552)\",\"stance\":\"supports\",\"note\":\"'pers. jāmadān Kleiderbehälter, Koffer ... ebenso tk. jamedān, čamedān; hieraus rum. geamantan Felleisen, Handkoffer, bulg. žemadan, čemadan, russ. čemodan dass. [Gorjajew 410]'.\"},\n   {\"src\":\"BQT\",\"where\":\"vol 2 p.660 (ocr/BQT/660.vision.txt)\",\"stance\":\"supports\",\"note\":\"'کریستنسن کلمهٔ استی cemodan را از روسی عاریت میداند'.\"}]),\n dict(id=9,lang=\"Persian\",words=\"čamedân\",verdict=\"confirmed\",\n  derivation=\"Persian čamedān 'suitcase' is the Russian čemodan re-borrowed (19th c., via trade and travel with Russia), so it is a doublet of native jāma-dān: Persian > Turkic > Russian > Persian. Mo'in tags it [روس.] (Russian); Wiktionary agrees. Dozy's older view that Arabic/Persian čamadān came straight from jāmadān is superseded by the Russian round-trip.\",\n  derivation_fa=\"«چمدان» وام‌واژه‌ای بازگشتی از روسی чемодан است که خود از راه ترکی از فارسی «جامه‌دان» رفته بود؛ پس «چمدان» و «جامه‌دان» دوگانه (doublet) هستند. معین آن را [روس.] می‌داند و ویکی‌واژه هم همین را می‌گوید. ادعای نورایی درست است.\",\n  sources=[W+\"چمدان\",W+\"чемодан\",V+\"چمدان\"],\n  ref_check=[{\"ref\":\"ETM:64\",\"status\":\"not_checked\",\"note\":\"ETM not accessible.\"}],\n  consulted=[{\"src\":\"MON\",\"where\":\"vajehyab.com/moein/چمدان\",\"stance\":\"supports\",\"note\":\"'چمدان (چَ مِ) [روس.] (اِمر.) کیف بزرگ چرمی ... که هنگام سفر لباس‌ها ... را در آن نهند'.\"},\n   {\"src\":\"BQT\",\"where\":\"vol 2 p.660 (ocr/BQT/660.vision.txt)\",\"stance\":\"supports\",\"note\":\"Mo'in: Dozy derives it from جامدان (جامه دان); Christensen calls the Ossetic cemodan a Russian loan.\"},\n   {\"src\":\"LKT\",\"where\":\"no. 552\",\"stance\":\"supports\",\"note\":\"Turkic čamedān and Russian čemodan from Pers. jāmadān.\"}]),\n dict(id=10,lang=\"Greek\",words=\"zôně; zonarion\",verdict=\"confirmed\",\n  derivation=\"Ancient Greek ζώνη zṓnē 'girdle, belt' < PIE *yōs-neh2 (*yoh3s-néh2), beside ζώννυμι 'gird', ζωστήρ; *y- > Greek ζ- (zd-) regularly. ζωνάριον zōnárion is its diminutive (-άριον), Modern Greek ζωνάρι 'sash'. Nourai's gloss 'a girdle worn by non-Moslems' belongs to the later Arabic/Persian zunnār, not to the Greek word, which simply meant 'small belt'.\",\n  derivation_fa=\"یونانی باستان ζώνη (zṓnē) «کمربند» از هندواروپایی *yōs-neh2 است و با ζώννυμι «کمر بستن» هم‌ریشه است؛ y آغازین هندواروپایی در یونانی به ζ بدل می‌شود. ζωνάριον (zōnárion) مصغّر آن است (یونانی نو ζωνάρι). معنای «کمربند ویژهٔ نامسلمانان» که نورایی آورده از آنِ «زنّار» عربی و فارسی است، نه واژهٔ یونانی. ریشه‌شناسی درست است.\",\n  sources=[W+\"ζώνη\",W+\"ζωνάριον\"],\n  ref_check=[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"AHD_watkins1985.txt leaf 111: 'Suffixed form *yōs-nā in Greek zōnē, girdle: ZONE'.\"}],\n  consulted=[POK_yos,WLD_yos,IEC_yos,{\"src\":\"KLN\",\"where\":\"KLN_1971.txt s.v. zonar\",\"stance\":\"supports\",\"note\":\"'zonar, n., a girdle. — ModGk. ζωνάρι, a girdle, fr. Gk. ζωνάριον, dimin. of ζώνη'.\"}]),\n dict(id=11,lang=\"Persian\",words=\"zonnâr\",verdict=\"plausible\",\n  derivation=\"Persian zonnār (Classical zunnār) 'belt worn by dhimmī Christians/Jews; Zoroastrian kustī' is borrowed from Arabic زُنّار zunnār (pl. zanānīr), which comes from Greek ζωνάριον, most likely through Aramaic/Syriac zūnārā. The Greek origin is certain; the chart's direct Greek > Persian arrow skips the Arabic (and Syriac) stages, which is why Persian has the Arabic gemination -nn-. Mo'in in Borhan also gives Greek directly.\",\n  derivation_fa=\"«زُنّار» در فارسی از عربی زُنّار (جمع: زَنانیر) وام گرفته شده و عربی آن را از یونانی ζωνάριον، به احتمال زیاد از راه سریانی zūnārā، گرفته است. ریشهٔ یونانی قطعی است، اما نمودار نورایی مرحلهٔ عربی (و سریانی) را انداخته و یونانی را مستقیم به فارسی پیوسته است؛ تشدید «نّ» نشان واسطهٔ عربی است. معین در حاشیهٔ برهان نیز یونانی را بی‌واسطه ذکر کرده است. ادعا در اصل درست ولی مسیر ناقص است.\",\n  sources=[W+\"زنار\",V+\"زنار\"],\n  ref_check=[{\"ref\":\"BQT:1033\",\"status\":\"supports\",\"note\":\"BQT vol 2 p.1033 (archive.org leaf n495; ocr/BQT/1033.vision.txt), footnote 3 to زنار: 'از یونانی جدید Zônári، از یونانی قدیم Zônárion مصغر Zônê بمعنی کمربند و منطقه ... زنار کمربندی بوده که ذمیان نصرانی در مشرق زمین بامر مسلمانان مجبور بوده‌اند داشته باشند'.\"},\n   {\"ref\":\"MON\",\"status\":\"supports\",\"note\":\"vajehyab.com/moein/زنار: 'زنار (زُ نّ) [یو.] (اِ.) ۱- رشته‌ای که مسیحیان به وسیلهٔ آن صلیب را به گردن آویزند. ۲- کُستی' — tagged Greek.\"}],\n  consulted=[{\"src\":\"KLN\",\"where\":\"KLN_1971.txt s.v. zonar\",\"stance\":\"partial\",\"note\":\"has Gk. ζωνάριον dimin. of ζώνη, but no Arabic/Persian zunnār.\"},\n   {\"src\":\"FVQ\",\"where\":\"FVQ_pages.txt grep 'zunn'\",\"stance\":\"silent\",\"note\":\"not a Qur'anic word.\"},\n   {\"src\":\"LKT\",\"where\":\"LKT.txt grep 'z.nn.r'\",\"stance\":\"silent\",\"note\":\"no hit.\"},\n   {\"src\":\"AFM\",\"where\":\"AFM.txt / AFM_pages.txt grep 'زنار'\",\"stance\":\"silent\",\"note\":\"no hit (OCR).\"},\n   {\"src\":\"AFA\",\"where\":\"AFA.txt grep 'z.nn.r'\",\"stance\":\"silent\",\"note\":\"no hit.\"}]),\n dict(id=12,lang=\"English\",words=\"zone\",verdict=\"confirmed\",\n  derivation=\"English zone (late 14th c., 'each of the five climatic belts of the earth') < Latin zōna 'belt, girdle; zone of the earth' < Greek ζώνη. The chart's arrow goes straight from Greek; the Latin intermediary is omitted but uncontroversial.\",\n  derivation_fa=\"انگلیسی zone (سدهٔ چهاردهم، نخست به معنای هر یک از پنج کمربند اقلیمی زمین) از لاتین zōna «کمربند؛ منطقهٔ زمین» و آن از یونانی ζώνη است. نمودار مرحلهٔ لاتین را نیاورده، ولی مسیر قطعی است.\",\n  sources=[W+\"zone\"],\n  ref_check=[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"no reference given by Nourai for this node.\"}],\n  consulted=[{\"src\":\"KLN\",\"where\":\"KLN_1971.txt s.v. zone\",\"stance\":\"supports\",\"note\":\"'zone, n., 1) a belt; 2) a region ... — F., fr. L. zona, fr. Gk. ζώνη, whence ζωννύναι to gird ... fr. I.-E. base *yōs-'.\"},AHD_yos,\n   {\"src\":\"SKT\",\"where\":\"SKT.txt grep 'zone'\",\"stance\":\"silent\",\"note\":\"zone entry not found in this OCR (only in the gloss of climate).\"}]),\n]\nnodes1=[\n dict(id=1,lang=\"Avestan\",words=\"yŭš, yŭšmat\",verdict=\"confirmed\",\n  derivation=\"Gathic Avestan yūš (YAv. yūžəm) 'you (pl.), nom.' < PIIr. *yūš < PIE *yūs (*yúHs); ablative yūšmat, gen. yūšmākəm show the oblique stem *yušma- < PIE *usme- with the y- of the nominative carried over (Pokorny: 'mit Übernahme des nominativischen i-'), exactly as Skt. yūyám / yuṣmān.\",\n  derivation_fa=\"اوستایی گاهانی yūš (اوستای نو yūžəm) «شما، حالت فاعلی» از هندوایرانی *yūš و هندواروپایی *yūs است؛ حالت ازی yūšmat و حالت اضافی yūšmākəm ستاک غیرفاعلی *yušma- را نشان می‌دهند که از *usme- هندواروپایی با گرفتن y از حالت فاعلی ساخته شده است (پوکورنی)، همانند سنسکریت yūyám و yuṣmān. ادعای نورایی درست است.\",\n  sources=[W+\"Reconstruction:Proto-Indo-European/yúHs\"],\n  ref_check=[{\"ref\":\"POK:513\",\"status\":\"supports\",\"note\":\"POK_02.txt leaf 171-172: 'av. yūžəm, gathav. yūš' and 'Akk. *us-sme ... mit Übernahme des nominativischen i- ai. yuṣmān Akk. (usw.), av. Abl. yūšmat'.\"}],\n  consulted=[{\"src\":\"BRT\",\"where\":\"BRT.txt leaf 62 (col. ~70)\",\"stance\":\"supports\",\"note\":\"Gathic citation 'at yūš daēvā vīspåŋhō ... sta' (Y.32.3) shows nom. yūš; NYB cites 'Av. (1304) yūšmāka-, xšmāka-' i.e. BRT col. 1304.\"},\n   POK_yu,WLD_yu]),\n dict(id=2,lang=\"Persian\",words=\"šomâ\",verdict=\"plausible\",\n  derivation=\"NP šumā < MP ašmā / šmāh (Pahlavi ideogram LKWM; Manichaean ʾšmʾh) < OP *xšmāxam (gen. pl.), cf. Gathic xšmākəm 'of you', xšmā- 'you' (obl.). The Persian form thus continues the Gathic variant stem xšm- (with initial x-, of debated origin, beside yušm-), not yūš or yūšmat directly. Both belong to the same PIE 2pl paradigm (*yūs / *usme-), so the root assignment is right but the immediate ancestor should be Av. xšmā-, xšmākəm.\",\n  derivation_fa=\"«شما» از فارسی میانهٔ ašmā / šmāh (هزوارش LKWM) و آن از پارسی باستان بازسازی‌شدهٔ *xšmāxam (حالت اضافی جمع) است؛ هم‌سنج با اوستای گاهانی xšmākəm «از شما» و ستاک xšmā-. پس «شما» از ستاک گاهانی xšm- (با x آغازینِ مورد بحث) آمده، نه مستقیم از yūš یا yūšmat. هر دو ستاک به یک صرف ضمیر دوم شخص جمع هندواروپایی (*yūs / *usme-) تعلق دارند؛ بنابراین ریشه درست است اما نیای بی‌واسطه باید xšmā- اوستایی باشد.\",\n  sources=[W+\"شما\"],\n  ref_check=[{\"ref\":\"HRN:176\",\"status\":\"partial\",\"note\":\"HRN.txt leaf 197 (p.176), no. 790: 'šumā ihr. aw. yušmāka-, gāth. xšmāka- euer; päz. šumā; ai. yuṣmāka-' — Horn gives both stems, with the Gathic xšm- form.\"},\n   {\"ref\":\"BQT:1291\",\"status\":\"not_found\",\"note\":\"Pages 1291-1294 are missing from the BQT vol 3 scan (pdf 81 = p.1290, pdf 82 = p.1295); recorded in ocr/BQT/1291.vision.txt. The cached 1291.png actually shows p.1295.\"}],\n  consulted=[{\"src\":\"NYB\",\"where\":\"NYB_vol2_glossary.txt line 3653, s.v. šmāh\",\"stance\":\"partial\",\"note\":\"'šmāh [LKWM] pers. pron. 2nd p. pl. ... — Av. (1304) yūšmāka-, xšmāka-; šmāh < OP *xšmāxam ... MPrs ʾšmʾ(h); Paz. NP šumā'.\"},\n   {\"src\":\"PHD\",\"where\":\"PHD.txt line 221\",\"stance\":\"supports\",\"note\":\"'ašmā [LKWM | M ʾšmʾ(h), N šumā] you (pl.)'.\"},\n   {\"src\":\"HRN\",\"where\":\"p.176 no. 790\",\"stance\":\"partial\",\"note\":\"yušmāka- / gāth. xšmāka-.\"},\n   {\"src\":\"MON\",\"where\":\"vajehyab.com/moein/شما\",\"stance\":\"silent\",\"note\":\"online page shows only the homograph شما [فر.] 'schéma'; pronoun entry not shown.\"},\n   {\"src\":\"ARY\",\"where\":\"ARY grep 'شما', 'SHOMA'\",\"stance\":\"silent\",\"note\":\"no entry found.\"}]),\n dict(id=3,lang=\"Germanic\",words=\"jŭz\",verdict=\"confirmed\",\n  derivation=\"Proto-Germanic *jūz 'you (pl.), nom.' < PIE *yūs (*yúHs) with Verner/final *-s > *-z; continued in Gothic jus, OE gē (> ye), OS gī, OHG ir (reshaped after wir). Its oblique stem is *izwiz / *iwwiz.\",\n  derivation_fa=\"ژرمنی آغازین *jūz «شما، حالت فاعلی» از هندواروپایی *yūs است (s پایانی در ژرمنی به z بدل شده) و در گوتی jus، انگلیسی کهن gē (← ye) و آلمانی کهن ir بازمانده است. ادعای نورایی درست است.\",\n  sources=[W+\"Reconstruction:Proto-Germanic/jūz\"],\n  ref_check=[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"AHD_watkins1985.txt leaf 111: 'yu-1. You ... Germanic *jūz (nominative) and *iwwiz (oblique) in Old English gē and ēow'.\"}],\n  consulted=[POK_yu,WLD_yu,{\"src\":\"KLN\",\"where\":\"KLN_1971.txt s.v. ye\",\"stance\":\"supports\",\"note\":\"'ye ... OE ge ... Goth. jus, and cogn. with OPruss. ious, Lith. jus, ... OI. yuyam, Avestic yuzəm'.\"}]),\n dict(id=4,lang=\"English\",words=\"you, your\",verdict=\"plausible\",\n  derivation=\"English you < ME you/yow < OE ēow, the dative/accusative of gē 'ye', < PGmc *iwwiz (West Gmc form of *izwiz), the oblique stem; your < OE ēower (gen.) < *izwaraz. Only ye continues the nominative *jūz directly; you and your come from the oblique stem of the same paradigm (AHD, Klein, Wiktionary). The root is right; the immediate parent is *iwwiz/*izwiz rather than *jūz.\",\n  derivation_fa=\"انگلیسی you از انگلیسی میانه you/yow و انگلیسی کهن ēow (حالت مفعولی و برای gē «ye») و آن از ژرمنی *iwwiz (ستاک غیرفاعلی) است؛ your از ēower (حالت اضافی) آمده. تنها ye مستقیم از حالت فاعلی *jūz است و you و your از ستاک غیرفاعلی همان صرف‌اند. پس ریشه درست است، ولی نیای بی‌واسطه *iwwiz است نه *jūz.\",\n  sources=[W+\"you\"],\n  ref_check=[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"no reference given by Nourai for this node.\"}],\n  consulted=[{\"src\":\"KLN\",\"where\":\"KLN_1971.txt s.v. you\",\"stance\":\"partial\",\"note\":\"'you, pron. — ME. eow, eou, you, yow, fr. OE. eow, used as dat. and acc. of ge, ye; ... Goth. izwis (used as dat. and acc. of jus, ye). See ye, pron., and cp. your'.\"},AHD_yu,\n   {\"src\":\"SKT\",\"where\":\"SKT.txt grep\",\"stance\":\"silent\",\"note\":\"entry not located in OCR.\"}]),\n]\nout={\"pdf_page\":568,\"book_page\":538,\"verified_by\":\"claude-opus-5.5\",\"verified_on\":\"2026-10-16\",\"entries\":[\n {\"entry\":0,\"root\":\"Yôs\",\"verdict\":\"confirmed\",\"modern_form\":\"PIE *yōs- / *yeh3s- 'to gird' (Pokorny 513 iō[u]s-; AHD yōs-)\",\n  \"note\":\"Root, language and gloss confirmed by Pokorny 513, Walde-Pokorny I 209, AHD, Mann and Buck. Branches: (a) Greek ζώνη > zone, ζωνάριον > (Syriac/Arabic) zunnār > Persian zonnār: certain, though the Arabic stage is omitted; (b) Avestan yāh-, yāsta-: certain; (c) Pahlavi jāmag / NP jāma: Müller-Hübschmann's link to *yōs- via OP *yāhma- (= Gk ζῶμα) is followed by Mo'in and Nourai, but Horn and Wiktionary derive jāma from *yem- 'hold', so the whole jāma sub-tree (pājāma > pajamas > pyjama > pižāma; jāmadān > Russian čemodan > čamedān) is plausible rather than proven at its root, while the loan chains themselves are confirmed. 'yâhma' is a reconstruction printed without an asterisk. The extraction matches the printed page (čamadan is printed as such; it is a phonetic spelling of чемодан).\",\n  \"note_fa\":\"ریشهٔ هندواروپایی *yōs- «کمر بستن» را پوکورنی (ص ۵۱۳)، والده-پوکورنی، فرهنگ امریکن هریتیج، مان و باک تأیید می‌کنند. شاخهٔ یونانی (ζώνη ← zone و ζωνάριον ← زنّار از راه سریانی و عربی) و شاخهٔ اوستایی (yāh-، yāsta-) قطعی است. اما پیوند «جامه» (پهلوی jāmag) با این ریشه از راه پارسی باستان بازسازی‌شدهٔ *yāhma- نظر مولر و هوبشمان است که معین و نورایی پذیرفته‌اند، در حالی که هرن و ویکی‌واژه آن را از ریشهٔ *yem- «نگه داشتن» می‌دانند؛ پس زنجیره‌های وام‌گیری (پاجامه ← pajamas ← پیژاما؛ جامه‌دان ← چمدان روسی ← چمدان) درست‌اند ولی ریشهٔ نخستین «جامه» با احتیاط پذیرفتنی است.\",\n  \"sources\":[W+\"ζώνη\",W+\"zone\",W+\"جامه\"],\n  \"ref_check\":[{\"ref\":\"POK:513\",\"status\":\"supports\",\"note\":\"POK_02.txt leaf 171 (p.513): 'iō[u]s- : iūs-, (vermutlich zu 2. ieu-) gürten; iōs-to-s gegürtet, iōs-men- n. Gurt'.\"}],\n  \"consulted\":[WLD_yos,AHD_yos,IEC_yos,SYN_yos],\n  \"nodes\":nodes0},\n {\"entry\":1,\"root\":\"Yu, Iu, Ues\",\"verdict\":\"confirmed\",\"modern_form\":\"PIE *yūs (*yúHs) 'you (pl.), nom.'; oblique *us-me-, *wos (Pokorny 513 1. iu-; AHD yu-1)\",\n  \"note\":\"Pokorny 513 lists exactly this: nom. iū- 'ihr', oblique cases from ues-/uos- (us-me). The Avestan and Germanic nominatives (yūš, *jūz) are direct reflexes. Persian šomā continues the Gathic oblique variant xšmā- (OP *xšmāxam), and English you/your continue the Germanic oblique *iwwiz/*izwiz, so these two arrows are right at the root level but name the wrong immediate parent (nominative instead of oblique stem).\",\n  \"note_fa\":\"پوکورنی (ص ۵۱۳) همین ریشه را می‌آورد: حالت فاعلی *yūs «شما» و حالت‌های دیگر از ستاک ues-/us-me-. اوستایی yūš و ژرمنی *jūz بازماندهٔ مستقیم حالت فاعلی‌اند. «شما»ی فارسی از ستاک گاهانی xšmā- (پارسی باستان *xšmāxam) و انگلیسی you / your از ستاک غیرفاعلی ژرمنی *iwwiz آمده‌اند؛ پس ریشه درست است ولی نیای بی‌واسطه در این دو مورد دقیق نیست.\",\n  \"sources\":[W+\"Reconstruction:Proto-Indo-European/yúHs\",W+\"Reconstruction:Proto-Indo-European/yū́\"],\n  \"ref_check\":[{\"ref\":\"POK:513\",\"status\":\"supports\",\"note\":\"POK_02.txt leaf 171: '1. iu- ihr, ursprüngl. nur Nom.; Kasus obliqui vom St. ues-, uos- (aus *iues, *iuos?)'.\"}],\n  \"consulted\":[WLD_yu,AHD_yu,{\"src\":\"IEC\",\"where\":\"IEC.txt grep 'jūs|yūs'\",\"stance\":\"silent\",\"note\":\"entry not located in OCR.\"}],\n  \"nodes\":nodes1}\n]}\njson.dump(out,open('/home/sfmqrb/git/rishe-private/data/verification/page-568.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build568.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-568.json >/dev/null && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 568"
}
```


### [2026-10-17T00:42:06.068Z] TOOL RESULT

```
nodes verified: 16/16
node verdicts: {'plausible': 7, 'confirmed': 9}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 13, 'contradicts': 1, 'not_checked': 6, 'partial': 2, 'not_found': 1}
books consulted: {'supports': 29, 'partial': 6, 'contradicts': 1, 'silent': 16} | by book: {'KLN': 7, 'POK': 4, 'WLD': 4, 'BQT': 4, 'LKT': 4, 'MON': 3, 'ARY': 3, 'SKT': 3, 'BRT': 2, 'HUB': 2, 'PHD': 2, 'NYB': 2, 'HRN': 2, 'AHD': 2, 'CHEUNG': 1, 'AID': 1, 'HJB': 1, 'FSD': 1, 'IEC': 1, 'FVQ': 1, 'AFM': 1, 'AFA': 1}
```


## [2026-10-17T00:42:12.288Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/s568.py; python3 $S AID.txt '(?i)pyjama|paijama|pajama' 150 2; for f in FSD_vol*.txt; do python3 $S $f '(?i)pyjama' 200 1; done; python3 $S SKT.txt '(?i)\\bzone\\b' 100 3 | head -5"
}
```


### [2026-10-17T00:42:13.921Z] TOOL RESULT

```
[AID.txt leaf 252] stA. PAhn.  A   village  priest  among  the Kols ;   he  is  remunerated  by  service land. PAi.  More  commonly  Pie.  Also another  form  of  PAhi. PAijAmA.  [Persian.]  Drawers,  trou- sers, such  as  are  worn  by  MusalmAn men  and  women.  Among  Euro- peans, sleeping-drawers. FAlk.  [Hindi,  from  p
--
NO HIT FSD_vol1.txt (?i)pyjama
NO HIT FSD_vol2.txt (?i)pyjama
NO HIT FSD_vol3.txt (?i)pyjama
NO HIT FSD_vol4.txt (?i)pyjama
[SKT.txt leaf 106] eave  (a). CUmatc.  (F.-Gk.)  M.E.  fUw^.^ F.  climat.  —  Ck.  «Xi^t».  stem  of  xAl'^ a  slope,  zone,  region  of  the  earth*  cfr m^ite.  -  Gk.  mkivw,  to  lean,  «loj>c: Lean. climacter.  a  crit
--
```


## [2026-10-17T00:42:17.079Z] AGENT

Correct the AID entry to reflect the real hit.


## [2026-10-17T00:42:19.818Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 - <<'EOF'\nimport json\np='data/verification/page-568.json'\nd=json.load(open(p))\nfor n in d['entries'][0]['nodes']:\n    for c in n['consulted']:\n        if c['src']=='AID':\n            c.update(where=\"AID.txt leaf 252 s.v. Pāijāmā\",stance=\"supports\",note=\"'PĀIJĀMĀ. [Persian.] Drawers, trousers, such as are worn by Musalmān men and women. Among Europeans, sleeping-drawers.'\")\n        if c['src']=='FSD':\n            c.update(where=\"FSD_vol1-4.txt grep 'pyjama'\",note=\"no hit in the OCR of any volume.\")\njson.dump(d,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)\nEOF\npython3 -m json.tool data/verification/page-568.json >/dev/null && python3 tools/verify_check.py 568 | grep -c PROBLEM"
}
```


### [2026-10-17T00:42:20.366Z] TOOL RESULT

```
0
```


## [2026-10-17T00:42:31.328Z] TOOL CALL #82: SubagentHandback

```json
{
 "message": "I wrote the page 568 verification to /home/sfmqrb/git/rishe-private/data/verification/page-568.json. verify_check.py 568 reports 0 PROBLEM lines.\n\n**Verdicts:** 16 of 16 nodes covered.\n- Roots: 2 confirmed (Yôs \"to gird\", Pokorny 513; Yu/Iu/Ues \"you\", Pokorny 513).\n- Nodes: 9 confirmed, 7 plausible, 0 disputed, 0 transcription_suspect.\n\n**Plausible items worth noting:**\n- **Yôs, yâhma:** this form is not attested in Avestan. It is the Old Persian *yāhma- that Müller and Hübschmann reconstructed. Nourai took it from Mo'in's footnote in Borhan p.556 and printed it without an asterisk.\n- **Yôs, Pahlavi yâmak → jâmeh (and the subtree under it):** Hübschmann p.49 and Borhan p.556 support the link to *yōs-. Horn p.93 and Wiktionary contradict it and derive jāma from yam-/*yem- \"hold\". The borrowing chains under it are confirmed: pājāma → pajamas → pyjama → pižāma, and jāmadān → Russian чемодан → čamedān.\n- **Yôs, pîjâmeh:** Nourai routes it through French. The ž sound fits French, but Mo'in tags it [انگ.] (English) and Wiktionary also says English.\n- **Yôs, zonnâr:** the Greek origin is certain, but the chart skips the Arabic zunnār and probable Syriac zūnārā stages.\n- **Yu, šomâ:** it comes from the Gathic stem xšmā- (Old Persian *xšmāxam, per Nyberg and Horn), not directly from yūš/yūšmat.\n- **Yu, English you/your:** these come from the Germanic oblique stem *iwwiz/*izwiz, not from *jūz.\n\n**Extraction errors:** none. The JSON matches the printed page. \"čamadan\" is printed that way in the book; it is a phonetic spelling of чемодан, not a misreading.\n\n**Source notes:**\n- BQT:1291 (šomâ) cannot be checked. Printed pages 1291–1294 are missing from the vol 3 scan: pdf page 81 is p.1290 and pdf page 82 is p.1295. The cached 1291.png actually shows p.1295. I recorded this in data/verification/sources/refs/ocr/BQT/1291.vision.txt.\n- I read Borhan pp. 556, 660 and 1033 from archive.org page images and saved transcriptions as 556/660/1033.vision.txt in the same folder.\n- ETM (ETM:63, ETM:64) is not accessible anywhere, so those checks are not_checked.\n- Etymonline pages failed to fetch and are not cited."
}
```


### [2026-10-17T00:42:31.706Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
