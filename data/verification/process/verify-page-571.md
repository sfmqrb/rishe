# Verification process log — verify-page-571


## [2026-10-17T00:30:14.564Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 571 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-571.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-571.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-571.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 571` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-17T00:30:14.619Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-17T00:30:18.122Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-17T00:30:18.140Z] TOOL RESULT

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


## [2026-10-17T00:30:18.656Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-571.txt"
}
```


### [2026-10-17T00:30:18.680Z] TOOL RESULT

```
1	=== PDF page 571 (book page 541) ===
2	--- entry 0 ---
3	ROOT [Semitic] Z.k.r : to remember, mention  (refs KLN:1766)
4	#1 (parent #0) [Arabic] refs=KLN:1766 | z.k.r : to remember, mention
5	  #2 (parent #1) [Persian] refs=FVA:150 | zekr «ذکر» : mention, remembrance (of God) | extra: ذاکر ، تذکّر ، تذکار ، تذکره مذاکره ، متذکر ، مذکور ، اذکار
6	#3 (parent #0) [Hebrew] refs=KLN:1766 | zâkar : he remembered ; zekhar-yâh : God has (is) remembered
7	  #4 (parent #3) [Arabic] refs=VDQ:233 | Zakarîa | NOTE: It is not quite clear through what language this word has reached Arabic.
8	    #5 (parent #4) [Persian] refs=None | Zakarîya «زکریا» : "God is remembered"
9	  #6 (parent #3) [Greek] refs=KLN:1766 | zakaris
10	    #7 (parent #6) [Latin] refs=KLN | zacharias
11	      #8 (parent #7) [English] refs=AHD | Zachary, Zacharias, Zachariah
12	--- entry 1 ---
13	ROOT [Arabic] Z.n.y : he commits adultery  (refs FVA:180)
14	#1 (parent #0) [Arabic] refs=LKT:44 | zînâ : adultery ; abŭ-zînâ : father of whoredom (referring to gibbons) ☞Ab 2
15	  #2 (parent #1) [Persian] refs=MON:602; FVA:180 | zenâ «زنا» : adultery | extra: زناء
16	  #3 (parent #1) [Persian] refs=MON:602; FVA:180 | bŭzîneh «بوزینه» : gibbon | extra: بوزنه
17	    #4 (parent #3) [Hindustani] refs=PRT:253 | bojîna : gibbon
18	      #5 (parent #4) [French] refs=KLN:655 |  | NOTE: This monkey was brought to France from India in the early 18th century.
19	        #6 (parent #5) [English] refs=KLN:655 | gibbon
20	  #7 (parent #1) [Turkish] refs=SYN:188 | ebuzine : gibbon
21	
```


## [2026-10-17T00:30:19.391Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-571.json"
}
```


### [2026-10-17T00:30:19.408Z] TOOL RESULT

```
1	{
2	  "pdf_page": 571,
3	  "book_page": 541,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Z.k.r",
8	        "lang": "Semitic",
9	        "refs": "KLN:1766",
10	        "gloss": "to remember, mention"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Arabic",
17	          "refs": "KLN:1766",
18	          "words": [
19	            {"translit": "z.k.r", "gloss": "to remember, mention", "script": null}
20	          ],
21	          "script_extra": null,
22	          "note": null,
23	          "quote": null
24	        },
25	        {
26	          "id": 2,
27	          "parent": 1,
28	          "lang": "Persian",
29	          "refs": "FVA:150",
30	          "words": [
31	            {"translit": "zekr", "gloss": "mention, remembrance (of God)", "script": "ذکر"}
32	          ],
33	          "script_extra": "ذاکر ، تذکّر ، تذکار ، تذکره مذاکره ، متذکر ، مذکور ، اذکار",
34	          "note": null,
35	          "quote": {
36	            "text": "مردم دیدهٔ ما جز به رخت ناظر نیست - دل سرگشتهٔ ما غیر تو را ذاکر نیست",
37	            "poet": "Hâfez"
38	          }
39	        },
40	        {
41	          "id": 3,
42	          "parent": 0,
43	          "lang": "Hebrew",
44	          "refs": "KLN:1766",
45	          "words": [
46	            {"translit": "zâkar", "gloss": "he remembered", "script": null},
47	            {"translit": "zekhar-yâh", "gloss": "God has (is) remembered", "script": null}
48	          ],
49	          "script_extra": null,
50	          "note": null,
51	          "quote": null
52	        },
53	        {
54	          "id": 4,
55	          "parent": 3,
56	          "lang": "Arabic",
57	          "refs": "VDQ:233",
58	          "words": [
59	            {"translit": "Zakarîa", "gloss": null, "script": null}
60	          ],
61	          "script_extra": null,
62	          "note": "It is not quite clear through what language this word has reached Arabic.",
63	          "quote": null
64	        },
65	        {
66	          "id": 5,
67	          "parent": 4,
68	          "lang": "Persian",
69	          "refs": null,
70	          "words": [
71	            {"translit": "Zakarîya", "gloss": "\"God is remembered\"", "script": "زکریا"}
72	          ],
73	          "script_extra": null,
74	          "note": null,
75	          "quote": null
76	        },
77	        {
78	          "id": 6,
79	          "parent": 3,
80	          "lang": "Greek",
81	          "refs": "KLN:1766",
82	          "words": [
83	            {"translit": "zakaris", "gloss": null, "script": null}
84	          ],
85	          "script_extra": null,
86	          "note": null,
87	          "quote": null
88	        },
89	        {
90	          "id": 7,
91	          "parent": 6,
92	          "lang": "Latin",
93	          "refs": "KLN",
94	          "words": [
95	            {"translit": "zacharias", "gloss": null, "script": null}
96	          ],
97	          "script_extra": null,
98	          "note": null,
99	          "quote": null
100	        },
101	        {
102	          "id": 8,
103	          "parent": 7,
104	          "lang": "English",
105	          "refs": "AHD",
106	          "words": [
107	            {"translit": "Zachary, Zacharias, Zachariah", "gloss": null, "script": null}
108	          ],
109	          "script_extra": null,
110	          "note": null,
111	          "quote": null
112	        }
113	      ]
114	    },
115	    {
116	      "root": {
117	        "name": "Z.n.y",
118	        "lang": "Arabic",
119	        "refs": "FVA:180",
120	        "gloss": "he commits adultery"
121	      },
122	      "nodes": [
123	        {
124	          "id": 1,
125	          "parent": 0,
126	          "lang": "Arabic",
127	          "refs": "LKT:44",
128	          "words": [
129	            {"translit": "zînâ", "gloss": "adultery", "script": null},
130	            {"translit": "abŭ-zînâ", "gloss": "father of whoredom (referring to gibbons)", "script": null, "see": ["Ab 2"]}
131	          ],
132	          "script_extra": null,
133	          "note": null,
134	          "quote": null
135	        },
136	        {
137	          "id": 2,
138	          "parent": 1,
139	          "lang": "Persian",
140	          "refs": "MON:602; FVA:180",
141	          "words": [
142	            {"translit": "zenâ", "gloss": "adultery", "script": "زنا"}
143	          ],
144	          "script_extra": "زناء",
145	          "note": null,
146	          "quote": {
147	            "text": "او زنا کرد و جزا صد چوب بود - گوید او من کی زدم کس را به عود",
148	            "poet": "Molavî"
149	          }
150	        },
151	        {
152	          "id": 3,
153	          "parent": 1,
154	          "lang": "Persian",
155	          "refs": "MON:602; FVA:180",
156	          "words": [
157	            {"translit": "bŭzîneh", "gloss": "gibbon", "script": "بوزینه"}
158	          ],
159	          "script_extra": "بوزنه",
160	          "note": null,
161	          "quote": {
162	            "text": "چون دل بوزینه گردد آن دلش - از دل بوزینه شد خوار آن گلش",
163	            "poet": "Molavî"
164	          }
165	        },
166	        {
167	          "id": 4,
168	          "parent": 3,
169	          "lang": "Hindustani",
170	          "refs": "PRT:253",
171	          "words": [
172	            {"translit": "bojîna", "gloss": "gibbon", "script": null}
173	          ],
174	          "script_extra": null,
175	          "note": null,
176	          "quote": null
177	        },
178	        {
179	          "id": 5,
180	          "parent": 4,
181	          "lang": "French",
182	          "refs": "KLN:655",
183	          "words": [],
184	          "script_extra": null,
185	          "note": "This monkey was brought to France from India in the early 18th century.",
186	          "quote": null
187	        },
188	        {
189	          "id": 6,
190	          "parent": 5,
191	          "lang": "English",
192	          "refs": "KLN:655",
193	          "words": [
194	            {"translit": "gibbon", "gloss": null, "script": null}
195	          ],
196	          "script_extra": null,
197	          "note": null,
198	          "quote": null
199	        },
200	        {
201	          "id": 7,
202	          "parent": 1,
203	          "lang": "Turkish",
204	          "refs": "SYN:188",
205	          "words": [
206	            {"translit": "ebuzine", "gloss": "gibbon", "script": null}
207	          ],
208	          "script_extra": null,
209	          "note": null,
210	          "quote": null
211	        }
212	      ]
213	    }
214	  ]
215	}
216	
```


## [2026-10-17T00:30:27.409Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/verification/sources/SOURCE_MATRIX.md | head -80; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','FVA','VDQ','AHD','LKT','MON','PRT','SYN','FVQ','AFM','PLA','LKT','HJB','SKT','TTS','BQT','ARY','HRN','WEB','FSD']:\n  print(k, json.dumps(d.get(k),ensure_ascii=False)[:400])\n\"; command ls data/verification/sources/refs/ | head -100",
 "description": "Read source matrix and reference index"
}
```


### [2026-10-17T00:30:27.904Z] TOOL RESULT

```
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
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 202
VDQ {"title": "Fereydun Badreh'i (tr.), Vazheha-ye Dakhil dar Qor'an-e Majid (Persian translation of Jeffery FVQ with notes), Toos 1372/1993", "kind": "website", "url": "https://noorlib.ir/book/view/12868?pageNumber=<N>&viewType=pdf (page images; viewType=html also exists) ; info: https://noorlib.ir/book/info/12868 ; ketabnak.com/book/51136 (download blocked)", "lookup_hint": "noorlib viewer is JavaSc
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. l
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
PRT {"title": "E. Partridge, Origins: A Short Etymological Dictionary of Modern English, New York 1958", "edition_found": "1958 (lending-only copies)", "kind": "archive_restricted", "url": "https://archive.org/details/originsshortetym00part (1958 1st ed.) ; originsetymologi0000part_j9t3 (4th ed. 1966) ; originsetymologi0000part (Routledge 2009) — all lending", "identifier": "originsshortetym00part (al
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf",
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. l
HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uof
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
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


## [2026-10-17T00:30:36.526Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; command ls data/verification/ | tail -20; sed -n 1,200p tools/verify_check.py | grep -n -i -E \"PROBLEM|required|must|consult|lang\" | head -60; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','LKT','PRT','SYN','VDQ','FVA','MON']:\n  print(k, json.dumps(d.get(k),ensure_ascii=False)[:1500]);print()\n\"",
 "description": "Inspect checker and ref details"
}
```


### [2026-10-17T00:30:37.075Z] TOOL RESULT

```
page-82.json
page-83.json
page-84.json
page-85.json
page-86.json
page-87.json
page-88.json
page-89.json
page-90.json
page-91.json
page-92.json
page-93.json
page-94.json
page-95.json
page-96.json
page-97.json
page-98.json
page-99.json
process
sources
22:    missing_pages, problems = [], []
46:            problems.append(f"page {pg}: invalid JSON ({ex})")
52:                problems.append(f"page {pg}: entry {i} ({e['root']['name']}) missing")
56:                problems.append(f"page {pg}: entry {i} root verdict {rv!r} invalid")
65:                    problems.append(f"page {pg}: entry {i} ({e['root']['name']}) node #{n['id']} missing")
69:                    problems.append(f"page {pg}: entry {i} node #{n['id']} verdict {nv!r} invalid")
74:                    problems.append(f"page {pg}: entry {i} node #{n['id']} has no derivation")
79:                for c in vn.get("consulted") or []:
86:    print("books consulted:", dict(con_tally), "| by book:", dict(con_books.most_common(40)))
89:    for p in problems:
90:        print("PROBLEM:", p)
94:    return 1 if problems else 0
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.", "notes": "Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt (paginated by leaf); /home/sfmqrb/git/rishe-private/data/verification

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.", "notes": "", "cites": "entry number of Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs (1927)"}

PRT {"title": "E. Partridge, Origins: A Short Etymological Dictionary of Modern English, New York 1958", "edition_found": "1958 (lending-only copies)", "kind": "archive_restricted", "url": "https://archive.org/details/originsshortetym00part (1958 1st ed.) ; originsetymologi0000part_j9t3 (4th ed. 1966) ; originsetymologi0000part (Routledge 2009) — all lending", "identifier": "originsshortetym00part (also originsshortetym0000unse, bwb_P8-AVM-445, 1958)", "local_file": null, "page_offset": null, "lookup_hint": "Borrow via IA lending; in-book search https://archive.org/details/originsshortetym00part?q=<word>. Entries are alphabetical with numbered sub-senses.", "notes": "RE-SEARCH 2026-09: 8 lending copies on archive.org, none open; HathiTrust search-only; Google no view. Borrow the 1958 copy to match Nourai's pagination."}

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.", "notes": "Two other open copies: dictionaryofselectedsynonyms...buck_963_N, fock_a-dictionary-...; restricted: dictionaryofsele0000carl.", "cites": "page number of Buck, A Dictionary of Selected Synonyms (1949)"}

VDQ {"title": "Fereydun Badreh'i (tr.), Vazheha-ye Dakhil dar Qor'an-e Majid (Persian translation of Jeffery FVQ with notes), Toos 1372/1993", "kind": "website", "url": "https://noorlib.ir/book/view/12868?pageNumber=<N>&viewType=pdf (page images; viewType=html also exists) ; info: https://noorlib.ir/book/info/12868 ; ketabnak.com/book/51136 (download blocked)", "lookup_hint": "noorlib viewer is JavaScript-rendered (WebFetch/curl get only the site chrome); needs a browser. Since it is a translation of FVQ, verify the substance via FVQ (same entry order); page numbers differ.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "Not on archive.org. Also on ghaemiyeh (ghbook.ir) as an app/EPUB per news reports.", "cites": "page number of the Persian translation of Jeffery's Foreign Vocabulary of the Qurʾān"}

FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with Nourai's title when buying. Catalogue record only."}

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).", "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf", "/home/sfmq
```


## [2026-10-17T00:30:46.230Z] AGENT

Now grep the local books.


## [2026-10-17T00:30:48.229Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E '^(Zachar|Zachary|gibbon)' KLN_1966.txt | head; grep -n -i 'zakar\\|zachar' KLN_1966.txt | head -20; echo ---; grep -n -i 'gibbon' KLN_1966.txt SKT.txt HJB.txt LKT.txt SYN.txt FSD_vol2.txt WEB_vol1.txt 2>/dev/null| head -30",
 "description": "Grep Klein, Skeat etc. for headwords"
}
```


### [2026-10-17T00:30:48.698Z] TOOL RESULT

```
16112:gibbon,  n.,  a  small,  long-armed  ape.  —  F.,  a  name of  Indian  origin  brought  to  Europe  by  the Marquis  Joseph-Frangois  Dupleix  (1697-1763), governor-general  of  the  French  possessions  in India  (1742-54).
12834:Elijah,  1)  masc.  PN. ;  2)  in  the  Bible,  name  of  the great  prophet  also  known  as  the  Tishbite.  — Heb.  Eliyydh,  lit.  ‘The  Lord  is  God’.  For  the first  element  see  El  and  words  there  referred  to and  cp.  esp.  Joel.  For  the  second  element  in Elijah  cp.  the  second  element  in  hallelujah, Hezekiab,  Isaiah,  Jeremiah,  Matthew,  Matthias, Nehemiah,  Obadiah,  Zachariah,  Zephaniah.  Cp. also  Elias,  a  shortened  form  of  Elijah. eliminable,  adj.  —  See  eliminate  and  -able, eliminant,  adj.,  promoting  elimination  ( med .)  — L.  eliminans,  gen.  -antis,  pres.  part,  of  eliminare. See  next  word  and  -ant.
38814:tezkirah,  tezkere,  n.,  a  certificate.  —  Arab,  tadh- kirah,  prop,  verbal  noun  of  dhdkkara,  ‘he  re¬ called  something  to  someone’,  the  second  con¬ jugation  of  dhakara,  ‘he  remembered’,  which  is rel.  to  Heb.  zakhar,  ‘he  remembered’,  zekher, ‘remembrance,  memorial’,  zikkdron,  ‘memor¬ ial,  remembrance’,  Aram.  Syr.  dikhar,  Ethiop. zakara,  ‘he  remembered’,  Akkad,  zakaru,  ‘to name,  speak,  swear’,  zikru,  ‘name’.
---
HJB.txt:11275:HOOLnCK,s.  Benf.hulakl  The word  is  not  in  the  Diets.,  [hut  it  is possibly  connected  with  ulUk,  Skt. uLahiy  <  an  owl,'  both  bird  and  animal taking  their  name  from  their  wailiiig note].  The  black  gibbon  {Hylobatts hoolaokyJerd.;  [Blanford,  Mami)udia,5'\^ not  unfrequently  tamed  on  our  £. frontier,  and  from  its  gentle  engaging ways,  and  plaintive  cries,  often  becom> ing  a  great  pet.  In  the  forests  of  the Kasia  Hills,  when  there  was  neither sound  nor  simi  of  a  living  creature,  by calling  out  noo !  hoo !  one  sometimes could  wake  a  clamour  in  response  from the  hoolucksy  as  if  hunareds  had suddenly  started  to  life,  each  shouting hoo !  hoo !  hoo  !  at  the  top  of  his  voice.
HJB.txt:11281:1884.—"  He  then  .  .  .  describes  a  gibbon he  had  (not  an  historian  nor  a  book,  but  a specimen  of  Hylobates  hooluck)  who  must have  been  wholly  delightful.  T^s  engaging anthropoid  used  to  pnt  his  arm  through Mr.  Stemdale's,  was  extremely  dean  in  his habits  (*  which,'  says  Mr.  Stemdale  thought- fully and  truthfully,  *  cannot  be  said  of  all the  monkey  tribe  ),  and  would  not  go  to sleep  without  a  pillow.  Of  course  he  died of  consumption.  The  gibbon,  however,  as a  pet  has  one  weakness,  that  of  '  howling  in a  piercing  and  somewhat  hysterical  fashion for  some  minutes  till  exhausted.*" — Saiy. Rfview,  May  31,  on  SUmdaU't  NaJL  Hist,  qf Mammalia  of  India,  kc.
HJB.txt:13436:1884.— "Less  interesting  personally  than the  gibbon,  but  an  animal  of  very  developed social  instincts,  is  SemnopUhecus  eniettus, otherwise  the  Bengal  langur.  (He)  fights for  his  wives  according  to  a  custom  not unheard  of  in  other  cases;  but  what  is peculiar  to  him  is  that  the  vanquished  males <^receive  charge  of  all  the  young  ones  of their  own  sex,  with  whom  they  retire  to some  neighbouring  jungle.'  Schoolmasters and  private  tutors  will  read  this  with interest,  as  showing  the  origin  and  early disabilities  of  their  profession."- iSczftirciay Afv.,  Bfay  31,  on  StemdaU'a  Nat,  Hitt,  of Mammalia  qf  India,  &c.
HJB.txt:13918:which  some  apprehend  to  be  a  cor- ruption of  the  word  Mandarin^  a  title of  distinction  among  the  Chinese  "  (H. of  Sumatra,  2nd  el  285).  Ritter adopts  the  etymology  from  mandar, apparently  after  A.  W.  Schlegel  * llie  true  etymon  ifl  pointed  out  in Notes  and  Queries  in  China  and  Japan, iii.  12,  and  by  one  of  the  present writers  in  Ocean  Highways  for  Sept. 1872,  p,  186.  Several  of  the  quota- tions beloiJir  will  show  that  the  earlier applications  of  the  title  have  no reference  to  China  at  all,  but  to  oflScers of  state,  not  only  in  the  Malay countries,  but  in  Continental  India. We  may  add  that  mantri  (see  MUN- TEEE)  IS  stiU  much  in  vogue  among theHess  barbarous  Hill  Races  on  the Eastern  frontier  of  Bengal  (e.g.  among the  Kagias  (see  C08STA)  as  a  de- nomination for  their  petty  dignitaries under  the  chief.  Gibbon  was  perhaps aware  of  the  true  origin  of  mandarin; see  below.
KLN_1966.txt:16112:gibbon,  n.,  a  small,  long-armed  ape.  —  F.,  a  name of  Indian  origin  brought  to  Europe  by  the Marquis  Joseph-Frangois  Dupleix  (1697-1763), governor-general  of  the  French  possessions  in India  (1742-54).
KLN_1966.txt:18044:Derivative:  hooligan-ism,  n. hoolock,  n.,  the  black  gibbon  (Hylobates  hoo¬ lock).  —  Fr.  hulak,  hulluk,  native  name  in  NE.
KLN_1966.txt:18047:India,  rel.  to  OI.  u/iikah,  ‘owl’,  from  an  imitative base  meaning  ‘to  wail’.  Both  the  gibbon  and  the owl  have  the  common  feature  that  they  are ‘wailing  animals’.
KLN_1966.txt:18422:Hylobates,  n.,  the  genus  of  the  gibbons  (zool.)  — ModL.,  fr.  Gk.  &Xo(3denr)<;,  ‘wood  walker’,  which is  compounded  of  6X7),  ‘wood’  (see  hylo-),  and PdtxT]i ;,  ‘treading  on’,  from  the  stem  of  (Jatveiv, ‘to  go,  walk’.  See  -bates, hylophagous,  adj.,  eating  wood  (zool.)  —  Gk. 0Xo9ayoi;,  compounded  of  6Xr],  ‘wood’  (see
WEB_vol1.txt:8537:an’thrō-poid, a. [anthropo-, and Gr. eidos, resembling.] resembling a human being: ap- plied especially to the most highly developed apes, as the gorilla, orangutan, gibbon, and chimpanzee.
WEB_vol1.txt:11703:right ascension; in astronomy, the are of the equator intercepted between the first point of Aries and that point of the equator which comes to the meridian with the sun or star. relating to ascension; as- cending or rising up. 2 ascensional difference; in astronomy, the dif- ference between the right and oblique ascen- sion of the same point on the surface of the sphere. ae as:cen/sive, a. 1. rising. 2. causing to rise. i; $ 3. in grammar. intensive; increasing the force; augmentative. [Rare.] ascent’, n. [L. ascensus, from ascendere, to ascend. ] > ; 1. the act of rising; rise; a mounting up- ward; as, the ascent oi vapors from the earth, 2. a going up; climbing. ot enie hill, or high place. [Obs.] 4. the amount of upward slope or elevation; as, that road has an ascent of five degrees. 5. acelivity; the rise of a hill; as, a steep ascent. 3 6. an advancement, as in rank, popularity, etc. 7. a going back in time or genealogy. as-cér-tain’, v.t.; ascertained, ptl., pp.; ascer- taining, ppr. [OFr. acertainer; L. ad, to, and certus, xed.) 3 1. to make certain; to define by removing obscurity or ambiguity; to determine. The divine law ascertains the truth. —Hooker. 2. to make certain by trial, examination, or experiment, so as to know what was before unknown; as, to ascertain the purity of a metal. 3. to make certain in the mind. [Archaic.] 4. to fix; to establish with certainty; to ren- der invariable, and not subject to will. [Obs.] The mildness and precision of their laws as- cerlained the rule and measure of taxation. — Gibbon. Syn.—find out, discover, determine, detect, discern, learn. as-cér-tain/a-ble, a. capable of being ascer- tained. as-cér-tain’a-ble-ness, n. the quality or state of being ascertainable. as-cér-tain’a-bly, adv. manner or condition. as-cér-tain/’ér, n. one who ascertains, or makes certain. as-cér-tain’ment, z. an ascertaining or being ascertained, as-ces/sin:cy, n., same as acescency. as-ces/sant, a. same as acescent. as-cet’ic, a. (Gr. askélikos, exercised, from as- kein, to exercise.] of or characteristic of as- cetics or asceticism; rigid; severe; austere. as-cet/ic, n. 1. one who lives a life of con- templation and rigorous self-denial for reli- gious purposes. . anyone who lives with strict self-disci- pline and abstinence. as-cet’/i-cal-ly, adv. 1. in an ascetic manner. 2. by means of asceticism. as-cet/i-cism, 7. 1. the practices or way of life of an ascetic; systematic self-denial for some ideal, 2. the religious doctrine that one can reach a higher spiritual state by rigorous self-dis- cipline and self-denial. as’cham, n. [after Roger Ascham (1515~1568), Eng. writer.] a receptacle for archery imple- ments. as/cl, 2., pl. of ascus. as/ciAin (ash’yan), n. [L. ascius, shadowless; Gr. askios; a priv., and skia, a shadow.] a person who casts no shadow at noon: said of the inhabitants of the Torrid Zone where the sun is vertical at noon for a few days a year. As-cid’i-a, n.pl. (Gr. askidion, a little bottle, from askos, a leather bag, a bottle.| an order of Tunicata, or sea squirts; ascidians. They are found at low tide on beaches, and are dredged from deep water attached to stones, shells, and fixed objects. They are usually sac-shaped, with a sonen outer covering or tunic. A single mass of ganglion represenis the nervous system, this mass being placed between the two openings of the body. Male and female reproductive organs exist in cach specimen. They may be single or simple, social, or compound. In social ascidians, the peduncles of a number of individuals are united into a common tubular stem. with a partial, common circulation of blood. as-cid/i-a, n., pl, of ascidium, aa lala) ©, e in te Aside s^. of the Ascidia; a sea squirt.
WEB_vol1.txt:37676:combated only for the choice of masters. —Gibbon. com/bat (or cém-bat’), v.t. to fight against; to oppose by force; as, to combat an antagonist. com/bat, n. 1. a fight; a struggle to resist, overthrow, or conquer; a contest by force; an engagement; an armed battle; as, the combat of armies.
WEB_vol1.txt:91947:hoo’lock, n. [from native name.] a species of gibbon, Hylobates hoolock, found in Assam.
FSD_vol2.txt:5363:Education  (L.  educere,  to  lead  or  draw  out)  is  the  system- atic development  and  cultivation  of  the  mind  and  other natural  powers.  "Education  Is  the  harmonious  develop- ment of  all  our  faculties.  It  begins  In  the  nursery,  and  goes on  at  school,  but  does  not  end  there.  It  continues  through life,  whetherwe  will  or  not. . . .   ‘   Every  person,’  says  Gibbon, ‘has  two  cducatlom,  one  which  he  receives  from  others,  and one,  more  important,  which  he  gives  himself.”’  John  Lub- bock The  Use  of  Life  ch.  vli,  p.  111.  [Maom.  1S94.)  Instruc- tion, the  Impartatlon  of  knowledge  by  othei's  (L.  instruere,  tO' ■   build  In  or  Into) ,   la  but  a   part  of  education,  often  the  amiille.st part.  TcflcWreff  Is  the  more  familiar  and  less  formal  word for  inatruciion.  Training  refers  not  merely  to  the  imptir- tation  ol  hnowledge,  but  to  the  exercising  of  one  In  actions with  the  design  to  form  habits.  Discipline  is  systematic and  rigorous  training,  with  the  idea  of  subjection  to  author- ity, and  perhaps  of  punishment.  Tuition  Is  the  technical term  for  teaching  as  the  business  of  an  instructor  or  as  in  the routine  of  a   .school;  tuition  is  narrower  than  teaching,  not, like  the  latter  word,  Including  training.  Study  is  em- phatically what  one  docs  for  himself.  We  speak  of  the teaching,  training,  or  discipline,  but  not  of  the  education  or tuition,  of  a   dog  or  a   horse.  Breeding  and  nurture  Include teaching  and  training,  especially  as  directed  by  and  de- pendent upon  home  life  and  personal  as.soclatlon;  breeding
FSD_vol2.txt:8403:Gibbons  vs.  Oadenia  vol.  vi.  p.  J3.  [l.  b.  is  co.  1S58.1 Ilf.  t.  To  seize  or  acquire  wrongfully.  [<  OF.  e
FSD_vol2.txt:10098:UuMnonpT  Co«mn.  tr.  by  B.  G.  ottfi.  vcl.  ii,  p.  00.  [«.  iK.-io.]  (»p«'i-<.er"ii-to-hy 'hi,  1   ep''i-,ser’'i.-t(t~lini'el;  2   i<p''i-ef'r'’n- 2.  Such  as  ifi  descinbetl  111  emc  poetry,  grand;  mible;  to-hy'ul.  I.  a.  Kitiiii  ted  above  tho  eeratohyal.  H.  «. as.  Gibbon  m   his  history  had  an  eptcjheino.  _   [,<,b.  Aneinceratohyal  !i
FSD_vol2.txt:12422:I   admire  his  [Burke’s]  eloquence,  I   approve  hia  politics,  I   adore his  chivalry,  and  I   ean  almost  oxouae  hia  revoroneo  for  church establishments.  BROuanAM  Men  of  Letters,  Gibbon  in  second Borios,  p.  185.  fc.  A   IIT.  1846.1
FSD_vol2.txt:31759:gibbon  {ffylobateslar')  of  Ten-  White-handed  Gibbon.  .i  /u asaerlm,  the  dun-cotored  gibbon  (B.  entelloUes)  of  the Malay  archipelago,  and  the  slamang  are  examples.
FSD_vol2.txt:48090:long  terminally  clubbed  tentacles  armed  with  a   double  hooGock,  1   hS'lek;  0   hdo'Idk,  n.  A   black  gibbon  found  In  ®r  tuba;  a   cooper.
FSD_vol2.txt:51125:Hy-lob'a-tes,  Ihcii-Ieb'a-tlz;  2   by-Iob'a-tegi,  a.  Mam.  1. A   genus  typical  of  HylohaiinB.  2.  [h-]  An  ape  of  this genus;  a   gibbon.  See  illus.  under  gibbon.
FSD_vol2.txt:51126:The  hylobaies  or  gibbon  is  as  much  longer  in  tho  arms  than  tho gorilla  as  the  gorilla  is  than  the  man.
FSD_vol2.txt:51127:E.  B.  Tvlob  in  Bncyc.  Brit,  11th  ed.,  vol.  ii,  p.  110. [   <   Gr.  hyloiaiss,  one  who  walks  the  woods,  <   hyU,  wood,  -|- baino,  go.]  —   hy'lo-bate,  n.  A   hyiobatine  ape;  a   gibbon.
FSD_vol2.txt:51128:Hy-lob"a-tFn!e,  1   hal-lob''3-tai'nI:  2   hy-lob'a-ti'ne,  w.  pi. Mam.  An  Oriental  subfamily  of  simlold  apes;  gibbons  or long-armed  apes.—  by-lob'a-tlne,  a.  &   ti.
FSD_vol2.txt:67537:Gibbon  Rome  vol.  iii,  p.  11.  (p.  s.  *   co,  1852.1
FSD_vol2.txt:71960:3.  [1-]  The  white-handed  gibbon  (Jiylobales  lar).
FSD_vol2.txt:79229:If  Gibbon  escaped  tho  peril  of  beine  an  ignoranl.  and  frivoloua lounger,  tho  merit  was  his  own.  Mobison  Gibbon  p,  6.  Iti.]
```


## [2026-10-17T00:30:58.414Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'Zach|Zechar|Zakhar' KLN_1966.txt | head; echo ---FSD; sed -n 31750,31760p FSD_vol2.txt | cut -c1-800; echo ---SKT; grep -n -i -E '^ *gibbon|gibbon,' SKT.txt SKT_dli_revised.txt | head",
 "description": "Grep Klein for Zachary and FSD gibbon"
}
```


## [2026-10-17T00:31:01.074Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'buzin|bozin|bûzîn|bŭzîn|zinā|zina\\b|ebuzin|ebu ?zine' LKT.txt TTS.txt incoming/TTS/*.txt PLA*.txt incoming/PLA/*.txt AFM_pages.txt HJB.txt 2>/dev/null | head -20; echo ---FVQ; grep -n -i -E 'zakar|zakariy' FVQ_pages.txt FVQ.txt | head",
 "description": "Grep Lokotsch, Vambery, Jeffery"
}
```


### [2026-10-17T00:31:01.353Z] TOOL RESULT

```
(eval):1: no matches found: PLA*.txt
---FVQ
FVQ.txt:9595:iL.i j J (Zakariyyd 9 ). 
FVQ_pages.txt:5621:iL.i j J (Zakariyyd 9 ).
```


### [2026-10-17T00:31:01.397Z] TOOL RESULT

```
1097:Zechariah
12834:Elijah,  1)  masc.  PN. ;  2)  in  the  Bible,  name  of  the great  prophet  also  known  as  the  Tishbite.  — Heb.  Eliyydh,  lit.  ‘The  Lord  is  God’.  For  the first  element  see  El  and  words  there  referred  to and  cp.  esp.  Joel.  For  the  second  element  in Elijah  cp.  the  second  element  in  hallelujah, Hezekiab,  Isaiah,  Jeremiah,  Matthew,  Matthias, Nehemiah,  Obadiah,  Zachariah,  Zephaniah.  Cp. also  Elias,  a  shortened  form  of  Elijah. eliminable,  adj.  —  See  eliminate  and  -able, eliminant,  adj.,  promoting  elimination  ( med .)  — L.  eliminans,  gen.  -antis,  pres.  part,  of  eliminare. See  next  word  and  -ant.
35807:soft,  adj.  • —  ME.  so  fie,  adj.  and  adv.,  fr.  OE. softe,  orig.  an  adv.  standing  in  gradational  rela¬ tionship  to  the  adj.  sefte,  ‘easy,  mild,  comfort¬ able,  gentle’;  rel.  to  OS.  sdfti  (adj.),  safto  (adv.), OHG.  semfti  (adj.),  samfto  (adv.),  MHG. senfte  (adj.),  sanfte  (adv.),  G.  sanft  (adj.  and adv.),  MDu.  sachte,  Du.  zacht  (adj.  and  adv.), G.  sacht  (adj.  and  adv.)  and  prob.  also  to  Goth. samjan,  ‘to  please’,  ON.  semja,  ‘to  shape,  com¬ pose,  arrange;  to  settle,  make  peace’. Derivatives:  soft,  adv.,  n.  and  interj.,  soft-en,  tr. and  intr.  v.,  soft-en-er,  n,,  soft-en-ing ,  n.,  soft- ish,  adj.,  soft-ling,  n.  and  adj.,  soft-ly,  adv.,  soft¬ ness,  n.
38814:tezkirah,  tezkere,  n.,  a  certificate.  —  Arab,  tadh- kirah,  prop,  verbal  noun  of  dhdkkara,  ‘he  re¬ called  something  to  someone’,  the  second  con¬ jugation  of  dhakara,  ‘he  remembered’,  which  is rel.  to  Heb.  zakhar,  ‘he  remembered’,  zekher, ‘remembrance,  memorial’,  zikkdron,  ‘memor¬ ial,  remembrance’,  Aram.  Syr.  dikhar,  Ethiop. zakara,  ‘he  remembered’,  Akkad,  zakaru,  ‘to name,  speak,  swear’,  zikru,  ‘name’.
---FSD
,1, t-i,.,  I,.,..,.,       («  ^   collapsible  hat;  an  opera-hat.  [<  Gibus,  the  maker.]
gi'bua-hat"t.
Gich'tel,  1   glH'tel;  2   gln'tSI.  Johann  Georg  (VulfiSS-*/!! 1710).  A   German  mystic  and  theosophlst:  Practical  T/icox- ophp.— Gich-te'le-an,  n.  A   follower  of  Gichtel;  one  be- longing to  the  order  of  Angelic  Brethren, gid'.lgid;  2gId,M.  [LocaLEng.]  1.  The  jack-snipe.  3.  The common  pike  or  jack,  giddf  . gid-f,  n.  The  staggers:  a' disease  of  sheep.  [<  giddy — gld'=bIad"der-worm,  ».  A   larval  tapeworm  tcmmrm ftralfs),  causing  gid.
Gld-dal'ti,  1   gi-dal'tai;  2   gl-dai'tl,  n.  Bib.  1   Chron.  xxv,  4: Gid'del,  l,gld'el:8gld'61,  n.  Ai6.  Fsi-a.  Ii,  47.  V gld'dhom,  1   gid'tham;  8   gid'thom,  h.  [Ir.]  Resttesness;  a half-frantic  gallop,  as  seen  In  cows  tormented  by  flies. Gid'dings,  I   gld'ipz:  2   gld'lng.s,  ft.  1.  Franklin  Henry  CVa» 1865-  ),  an  American  so'eiologist:  university  professor
and  writer.  3,  JoshuaReed  (“'/al79S-V8rl864),  anAnier- icau  lawyer  and  abolitionist.  3.  A   town,  county-seat  of Lee  county,  Tex.
gid'dy,  1   gid'i;  2   gtfl'y,  n.  [gid'died;  GiD'DX-iNa.l  I-  L To  make  dizzy  or  unsteady.
:   .-'.My. head  •
\   ^   Swims  with  them'ddm’na  whirl  ;o|  Kfe;about  Di
soutliern  Asia  and  adjacent islands,  having  a   slender form,  very  long  arms  (w'hich may  touch  the  ground when  the  animal  walks erect),  and  Lschial  cal- losities. The  wliite-bandea  -tn.,*..:.,,..-,,-,,,,  i ,
gibbon  {ffylobateslar')  of  Ten-  White-handed  Gibbon.  .i  /u asaerlm,  the  dun-cotored  gibbon  (B.  entelloUes)  of  the Malay  archipelago,  and  the  slamang  are  examples.
LoNoynmow  Michael  Angelo  »t.  i,  div.  '
---SKT
SKT_dli_revised.txt:31682:Gibbon, a kmd of ape. (F.) F. gibbon, 
SKT_dli_revised.txt:94524:gibbon, giblets, gill (3), glean, gobelin, cinchona (chinchona') , cockroach, embargo,
```


## [2026-10-17T00:31:06.522Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 5615,5660p FVQ_pages.txt | cut -c1-600; echo ---SKT; sed -n 31680,31686p SKT_dli_revised.txt; echo ---LKT; command ls incoming/ ; grep -n -i -E 'zin[aā]|maimun|bûzine|bozine|ebu' LKT.txt | head -20",
 "description": "Read Jeffery Zakariyya entry, Skeat, LKT"
}
```


### [2026-10-17T00:31:06.869Z] TOOL RESULT

```
148). 2 The most likely origin, however, is that suggested by Noldeke,
Nenc Beilmye, 53, that it is from the Eth. HCfl*'!* carpet. Noldeke
admits the possibility that the borrowing may have been the other
way, 3 and one is inclined to derive both the Ar. and Kth. words from
an Iranian source, but at present there is not sufficient evidence to
decide what this source is.
iL.i j J (Zakariyyd 9 ).
x"
iii, 32, 33 ; vi, 85 ; xix, 1,7; xxi, 89.
Zachariah.
Always as the father of John the Baptist, 4 though in iii, 32, he is
the elder who reared Mary from childhood, an idea dependent of
course on Protevanyelion, viii, 4. ^ ^ ^
There are variant spellings of the word, . u j j ; u j j and ( j j
(Tab. on iii, 32), and the early authorities recognized the name as
foreign, al-Jawallqi, Mu'arrab, 77. 5 The probabilities seem to be that
it came into Ar. from Syr. Vp1. 6 We find fcOISKT in Mandaean, 7
but there seems reason to believe that this form, like Yahya for
Yohanna, has been influenced by Arabic (Brandt, JiRM, viii, 380).
The name apparently does not occur in the early literature, 8 though
it must have been well known to Arabian Christians in pre-Islamic
times.
1 Vullers, Lex, li, 168, 169.
2 Addai Slier, 77, also argues for a Persian origin, but he wants to derive it from
->ljJ meaning yellow water.
3 80 Kraenkrf, op. eit.
4 It is remotely possible that in the list of Prophets in vi, 85, it refers to someone
else, but its elose connection there with the name Yahya would seem to indicate that
the same Zachariah is meant as is mentioned in the other passages.
8 So al-KhafajT, 99.
Rhodokanakis, WZKM, xvii, 285; Horovitz, KU, 113; Mingatm, Kyriac,
Influence, 82.
7 As in the Liber Adami (ed. Norbcrg), and Qinzn (tr. Lidzbarski), 51, 213, 219.
8 Horovitz rightly rejects the examples collected by Cheikho, 232.152 FOREIGN VOCABULARY OF THE QUR^AN
; (Zakd).
Of frequent occurrence in many forms.
To be pure.
The three forms which particularly concern us are ^-J j (cf. xxiv,
>" <^
21), ^S j (ii, 146 ; iv, 52 ; xci, 9), and ^5 J>" (xx, 78 ; IxxxviL 14).
The primitive meaning of the Arabic D j is to grow, to flourish,
thrive, as is recognized by the Lexicons (cf. LA, xix, 77 ; and Raghib,
Mufradat, 212). 1 This is the meaning we find in the earliest texts,
e.g. Hawdsa, 722, 11 ; Labld (ed. Chalidi), etc., and with this we must
connect the ^ jl of ii, 232 ; xviii, 18, etc., as Noldeke notes. 2 In this
sense it is cognate with Akk. zalcu, to be free, immune 3 ; Aram. fcOT
---SKT
from M. Du. tvippCy ‘ a gibbet,’ in Hexham ^ 

Gibbon, a kmd of ape. (F.) F. gibbon, 
in Buffon ; of unknown origin. 

Gibbous, humped, swelling. (L.) 
From L. gibbosus, humped (whence also 
---LKT
ARY
BLY
BQT
FFD
IRN
MFL
MON
PLA
TTS
TYL
VIE
WLD
ZAW
فرهنگ ریشه های زبان فارسی (2).pdf
35:Neben  der  Änderung  der  Form  geht  in  vielen  Fällen  eine  Verschiebung der  Wortbedeutung  vor  sich,  zumal  wenn  es  sich  nicht  um  Gegenstände
374:sp.  pg.  mit  Verkennung  des  ar.  Stammes am  ...  als  ar.  Artikel]  almiraglio,  sp. pg.  almirante  [mit  volksetymologischer Umbildung  gemäß  dem  lat.  partic.  praes.], afrz.  aumirant,  prov.  amiran,  it.  almi- rante.  Die  Bedeutung  ist  überall  'Ober- befehlshaber der  Flotte'.  Ebenso  mhd. admirät  [als  Titel  des  Kalifen],  dtsch. Admiral,  ndl.  admiraal,  engl,  admiral. —  Daß  die  Worte  aus  amlr-al-bahr 'Befehlshaber  der  See,  des  Meeres'  ent- standen sein  sollen,  scheint  wenig  wahr- scheinlich, wenn  auch  ein  solcher  Weg- fall des  arab.  Wortes  hahr  an  und  für sich  möglich  ist,  vgl.  z.  B.  Denebola  [s. hier  Nr.  482],  Abdul  [wurde  bei  einem tk.  Schüler,  der  'Abd-ul-hädl  hieß,  stets als  Name  gebucht].  Dem  Wunsche  von ML  423  nach  einer  Geschichte  der  Form u.  Bedeutung  dieses  Wortes  muß  zuge- stimmt werden.  Nur  zum  Teil  ist  dieser Wunsch  durch  Christoph  Gebhardt,  Das arabische  Etymon  einiger  romanischer Wörter.  Programm  des  Slädt.  Gymna- siums mit  Realschule  zu  Greiz.  1912. S.  6 — 19  erfüllt  worden.  Der  Verfasser stellt  als  neues  Etymon  für  die  verschie- denen Formen  der  Gruppe  Admiral  ar. amir  awival  'erster  Emir,  Oberemir' auf,  leider  ohne  diese  Zusammenstellung in  arabischen  Schriftstellern  belegen  zu können.  Den  Formen  prov.  amiran, amirant,  sp.  pg.  it.  almirante  wird  [a. a.  0.  S.  15]  der  Ausdruck  anUr-amlrän 'Emir  der  Emire'  zugrunde  gelegt,  doch scheint  die  pers.-ar.  hybride  Form  in dieser  Gestalt  nicht  bestanden  zu  haben, auch  scheint  die  notwendige  Abkürzung zu  amiran  zu  merkwürdig  zu  sein  [na- türlich nach  pers.  u.  arab.  Sprachge- brauche ist  nur  die  Verkürzung  mir- mlrän].  Orientalische  Entlehnungen lassen  sich  nicht  ohne  weiteres  nur  mit Beachtung  der  romanischen  Lautgesetze verfolgen,  wie  im  Vorwort  allgemein bemerkt  wurde.  [Devic  DEt  31/32. Lammens  Rem  23/24.  DE  165.  Dozy Oost  5/6.  Kluge  7.  Rom  Forsch  IV, 368.
548:c)  Mit  cfßitß  'Fliegen'  ergab  sich Ba'^al-ze^ü^  'Herr  der  Fliegen',  ähnlich wie  Zeüi;  öttöiliuio?,  der  'Fliegenbewah- rer',  Name  einer  philistäischen  Gottheit [übrigens  gr.  wohl  absichtlich  zu  BeeX- SeßouX  'Herr  des  Mistes'  verstümmelt]. Hieraus  dtsch.  Beelzebub,  frz.  belzibuth,
549:it.  belzebu,  wie  schon  im  NT  Bezeich- nung des  'Fürsten  der  Hölle'.
697:'Finger',  Einheisnomen  banäna;  wahr- scheinlich Grundwort  zu  der  Bezeich- nung Banane  für  die  Frucht  der  Musa paradisiaca  L.  oder  Musa  sapientum  L. [Musa  übrigens  aus  ar.  mauz,  müz  'Baum, und  Frucht  der  Musa'],  doch  wurde  der Name  zuerst  im  Kongogebiete  gehört [obwohl  der  Bantu-Name  dafür  bi-tebbe oder  ähnhch  lautet]  und  um  die  Mitte des  16.  Jahrhunderts  nach  Europa  ge- bracht; sp.  pg.  banana,  it.  banano,  rum. bananä,  frz.  banane  'Pisangfrucht',  ba- nanier  'Pisangbaum',  ndl.  banaan,  engl. banana,  dtsch.  Banane,  russ.  banan.  — Nach  einem  Vorschlage  von  HÜMMEL, soll  Banane  von  babyl.  banu  'süß  schmek- ken,  gut  sein'  [wohl  banu  II,  1)  bei  Del HWB  180  a]  kommen,  wovon  auch  über *bana  das  ar.  bala  'Dattel'  abgeleitet wird.  [Kluge  35.  Hobson-Jobson  56. E.  Werth,  Zur  Natur-  u.  Kulturgeschichte der  Bananen.  In  Festschrift  zu  Eduard Hahns  60.  Geburtstage.  Stuttgart  1917.. S.  22—58.   MWiD  130.
912:'Kanal'  [Stamm  bag,  heg,  bog  'Band, gebunden,  binden'  Vämbery  TktEtWb S.  192,  Nr.  204  I];  hieraus  rum.  bogaz, hoaz  'Meerenge,  Kanal'.
1413:5.56.  Tk.  ebnzine: Auch  buzine  'Affe'  [aus  ar.  abü  zina" 'Vater   der   Unzucht'];    hieraus  russ. obez'jana,  klruss.  obezjana  'Affe'  [vgl. lit.  bezdona].
1960:Auel)  hänä  'Haus'  [Horn  NpEt  S.  103, Nr.  4fi6  und  ANDKEAS  in  Festgabe  für Tlieodor  Nöldeke  zum  80.  Geburtstage. Göttingen  1916.  S.  4/6];  hieraus  tk.  han 'Herberge,  Wirtshaus',  rum.  han  'Gast- haus'.
2057:'Bezirk,  Umgebung';  hieraus  mit  ar. Art.  sp.  pg.  alfoz  'Landschaft,  Feldflur', im  MA  der  Bezirk,  der  seine  eigene Jurisdiktion  hatte  und  nach  einem  be- sonderen fuero  regiert  wurde,  meistens nur  eine  Pfarrei  oder  ein  Schloßgebiet umfassend.    [DE  116/117.
2093:zination (puXaKTTipiov'  MSOS  XII,  192 Anm.  1).  Vgl.  auch  ZOTENBERG  in Revue  Critique  ("10.  4.  1867),  der  beide Ansichten  zu  vereinen  sucht,  und  Fausto LASINIO  in  GSAJ  III  (1889),  142.
2203:Eigentlich  Infin.  des  Vbs.  salama  IV 'sich  unterwerfen',  nämlich  dem  Willen Gottes,  also  'Ergebung  in  Allahs  Willen'. Es  ist  der  Name  für  die  Religion  Mu- hammads geworden:  dtsch.  Islam,  engl. islam,  islamism  ;  frz.  islain,  islamisme,  it. islaniismo;  russ.  islam  [s.  hier  Nr.  1516  a].
2398:'Wein'  [doch  stammt  das  Wort  sicher- lich wie  die  Sache  selbst  aus  der  Um- gebung Abessiniens:  die  Landschaft Kaffa  ist  die  Heimat  des  Kaffeebaumes, der  von  Saih  aS-SÄDILI  nach  Süd- arabien eingeführt  wurde,  wo  der  Haupt- ausfuhrhafen Moha  war;  hieraus  dtsch. Mokka],  tk.  kahtve;  hieraus  um  die Wende  des  16.  und  17.  Jahrhunderts  in Europa  eingeführt  als  it.  cahue  [Pietro della  Valle,  Viaggi  (ediz.  di  Roma)  I, 110],  caffh,  frz.  sp.  pg.  cafS,  rum.  cafe, cafea;  engl,  coffee,  ndl.  hoffie,  dtsch. Kaffee  [1582  als  chaube,  1663  cahwe belegt] ;  russ.  kofe,  kofej,  klruss.  kofij, kava,  Cech.  käva,  poln.  kaiva,  bulg. kahwe,  serb.  kahwa,  kafa  [vgl.  poln.  ka- pinaz,  kafenauz  <^  dtsch.  Kaffeehaus].
2522:'Falle;  große  Warenmenge'  [zwei  ver- schiedene klanglich  zusammengefallene Wörter;  ersteres  vom  Stamme  kap  'er- greifen, erfassen,  bes.  gewaltsam  er- greifen' Vämbery  TktEtWb  S.  75,  Nr.  80; letzteres  vom  Stamme  kap  'zudecken, verhüllen,  umbinden',  s.  hier  Nr.  1061, vgl.  ujgurisch  kamnmk  'gebunden  = alle',  kamukiuk  'Menge'];  iiieraus  rum. capangä,  capcanä  [schon  tk.  kapkan ältere  und  östhche  Form:  'Falle']  'Falle, Hinterhalt';  ca/;«w 'Vorraisraum',  capan- liu  'Proviantmeister';  bulg. Ä-«2^an 'Falle'
3150:1355  Ar.  lualijas: 'Prahlerei'  [modern  und  sehr  selten, vgl.  Dozy  Suppl  II,  62^];  hieraus  viel- leicht siz.  Diafia.  Adj.  mafiusu,  von  einem Manne,  der  sofort  bereit  ist,  zu  den Waffen  zu  greifen,  um  irgendeine  Be- leidigung zu  rächen,  und  dabei  Blut zu  vergießen.  Im  Anfange  des  XIX. Jahrhunderts  in  Faieniio  und  Umgebung entstanden,  ging  das  Wort  bald  ins  lt. über:  maffia,  maffioso,  bes.  zur  Bezeich- nung einer  verbrecheri.schen  Geheim- geseilscliaft  [entsprechend  der  napole- tanischen  Camorra].  Die  Etymologie kann  nicht  als  sicher  gelten.  [GrSVoci Sic  24U.
3251:'Gebunden'  [pari.  pass.  von  rahata 'binden,  fromm  sein'];  hieraus  frz. marabout  'Einsiedler',  ein  heiligmäßiger Mann,  der  nach  seinem  Tode  in  einer Kapelle  begraben  wird  und  dort  Ver- ehrung findet;  das  Wort  wird  auch fälschlich  auf  diese  Grabkapelle  selbst bezogen ;  sp.  morabito,  pg.  marabuto, rum.  marabut  'Einsiedler',  siz.  mura- bitu  'Abstinenzler';  engl,  maraboot; ferner  wegen  des  ernsthatten  Aussehens des  Vogels  sp.  marabA  'Riesenstorch vom  Senes^al  oder  aus  Indien,  Lepto- ptilus  argaia  Gray.',  dtsch.  Marabu,  engl. marabou.  —  Dagegen  muß  sp.  morabito 'Seemann'  auf  ar.  muräkibi  'dass.'  zu- rückgehen. [Devic  DEt  157.  Eguilaz  443. GrSVociSic  242.
3376:1461a.  Ar.  mimbar: Aussprache  für  ursprüngliches  minbar [von  ar.  nabara  'erheben';  minbar  aXso ursprünglich  die  Erhebung,  auf  die  man sieh  setzt  oder  stellt,  Untergestell,  s. BECKER  in  Orient.  Studien  (Festschrift für  Nöldeke)  I,  S.  338;  letzten  Endes aus  dem  Äthiop.,  s.  Nöldeke,  Neue  Bei- träge, S.  49]  'Kanzel',  und  zwar  im Gegensatz  zur  Predigtkanzel  kurst  die- jenige Kanzel  in  der  Moschee,  auf  der an  jedem  Freitag  die  Jiutba,  d.  h.  das Gebet  für  den  obersten  Herrscher  der Gläubigen,  gehalten  wird.  Hieraus  jüd.- dtsch.  Almemor,  die  inmitten  der  Syna- goge betindliche,  zum  Verlesen  der Tliora  bestimmte  Erhöhung  [die  in  jüd. Schriften  als  bema  oder  mifdal  bezeich- net wird],  vgl.  z.  B.  in  Heinrich  Heines , Prinzessin  Sabbath":  'Stolz  aufflackern auch  die  Kerzen  /  Auf  der  Brüstung des  Almemors'.
3966:Der  Ruhetag  nach  den  sechs  Wochen- tagen; hieraus  gr.  ödßßaxov,  lat.  sab- batum  und  it.  sabbato,  prov.  sabda,  sp. pg.  sdbado,  [mit  Einschiebung  eines  m angeblich  unter  Einfluß  von  lat.  septi- mus]  frz.  samedi,  rum.  sämhätä;  ähnlich in  den  slav.  Sprachen:  VMSs.subota,  serb, subota,  öech.  poln.  sobota,  und  in  den germ.  Sprachen:  dtsch.  Samstag [<^  Sampztag  <^  Sambtac  <^  Sambez- <^  ahd.  Sambaztac],  mhd.  sameztag.  — Die  neuhebr.  Aussprache  sabbes  ergab jüd.-dtsch.  Schabbes  und  russ.  sabas 'Feierabend'  >  'gut,  fertig,  genug!'. Engl,  sabbdth  wird  in  England  und
4613:'Wilder  Ölbaum,  Rhamnus  lycioides'; hieraus  zunächst  ar.  zanhüg,  ferner  sp. acebuche,  pg.  azambtijo,  zambujo  'dass.'. [DE  32.  Eguilaz  1.5/17  (der  lat.  acerbus als  Gdwt.  vorschlägt;  lautlich  viel  zu schwierig).
4866:Vulg.  'Unterjacke.  Korsett',  ebenso  tk. zebun  'Jäckchen,  Mieder' ;  hieraus  rum. zäbun  'wattierter  Bauernkittel';  bulg.  za- bunce,  serb.  zubuii,  klruss.  zobuncac, russ.  zipun  'Jacke'  [vielleicht  geht  das ar.  Grundwort  selbst  zuletzt  auf  ^r.gubba, s.  hier  Nr.  737,  zurück].  [Löbel  EITAP 99.    Mikl  SlEtWb  404a.
4868:'Schwach',  ebenso  tk.  zebun  'dass., energielos';  hieraus  serb.  zabun  'ver- blüfft', Vb.  zabuniti.  [Mikl  SlEtWb  399a.
```


## [2026-10-17T00:31:24.639Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; mkdir -p $S; pdftoppm -f 571 -l 571 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf $S/pg571; echo done; awk 'BEGIN{RS=\"\\f\"} NR>=69 && NR<=72' data/verification/sources/refs/LKT.txt | grep -n -E '^[0-9]+ *$|556|ebuzine' | head; sed -n 1405,1416p data/verification/sources/refs/LKT.txt",
 "description": "Render page image and check Lokotsch"
}
```


### [2026-10-17T00:31:25.719Z] TOOL RESULT

```
done
26:42
50:43
85:44
105:45
550.  Mal.  düri:
'Stachel,  Dorn'  [Pijn  112];  hieraus  dü- rlan  'ein  Baum  Ostindiens,  Durio  zibe- thinus  L.',  der  veegen  seiner  melonen- artigen Früchte,  die  eine  mit  Stacheln versehene  Schale  haben,  so  genannt  wird. Hieraus  ndl.  doerian,  engl,  durian,  frz. dourion,  durion,  it.  duriano.  [Devic  DEt 107.  MMM17.  JAOSXYH,  137/139.
.551.  Ar.  durra: 'Moorhirse,  Sorghum  vulgare';  hieraus it.  sorgo,  frz.  sorgo,  sorgho;  dtsch.  Sorg- iveizen  [mit  volksetymologischer  An- lehnung an  'Sorge'].  —  [Nach  SPITZER in  WuS  IV,  140ff.  allerdings  eher  aus lat.  *syricum,  m.  E.  jedoch  fraglich.]
552.  Ar.  durr  uinfassal: 'Gesonderte  Perlen'  [aus  durr  'Perlen, Musiknoten' und  »««(/"assa?  Kunstausdruck für  die  regelmäßige  Ünterbrechung  je zweier  Perlen  der  Perlenschnur],  viel- leicht mit  pers.  sog.  Izäfät:  dtirr-i- nmfassal;  aus  diesem  Grundwort  sind die  Tonbezeichnungen  der  sog.  Solmi- sation  do  re  mi  fa  so  Z«  entstanden,  die man  gewöhnlich  als  von  GUIDO  VON AREZZO  [995—1050]  erfunden  erklärt; offenbar  hat  er  sie  aber  einem  orienta- talischen  Notensystem  entnommen.  Der angeblich  von  PAUL  DIAKONUS  stam- mende bekannte  Hymnus  Ut  queant laxis  Resonare  fibris  Mira  gestorum Famuli  tuorum  Solve  polluti  Labii
reatuni  Sancte  Johannes  ist  natürlich erst  später  entstanden ;  daher  der  übliche [außer  bei  den  Italienern]  Anfang  ut  usw. Der  Laut  so  statt  sa  entsteht  im  Ara- bischen auch  sonst  infolge  der  Emphasis des  vorhergehenden  Konsonanten ;  mi aus  mü  ist  tk.  Aussprache  des  ar.  mu.
553.  Pers.  diirük-kär: 'Zimmermann'  [aus  durük  'dünnes  Holz' Horn  NpEt  S.  116,  Nr.  522  und  kär 'Täter'  ebenda  S.  185,  Nr.  832],  hieraus zunächst  mit  Dissimilation  von  r  zu  l tk.  dillger  'dass.'  und  dann  rum.  dulgher 'Zimmermaim',  dulgherie  'dessen  Hand- werk', bulg.  dulger,  dulgerin,  serb.  dun- der,  dunderin  'Zimmermann'.  [Bern SlEtWb  259.
.554.  Pers.  dnsmäu: 'Feind'  [aus  dui,  dus  'übel,  böse'  Horn NpEt  S.  126,  Nr.  565  und  män(is)  ebenda S.  222,  Nr.  992],  ebenso  tk.  dähnen; hieraus  rum.  du§man  'dass.',  Ableitung du^mancä,  du^mänie,  du^manesc;  bulg. dusman,  dusmanin,  serb.  dusman,  dus- manin  'Feind',  klruss.  dusman  'Wüiger, Tyrann'.    [Bern  SlElWb  239.
555.  Tk.  düweiek: 'Kleine,  noch  grüne  Melone  oder  andere Frucht'  [Kelekian  Kämüs  591  b];  hieraus rum.  dovleac  'Kürbis',  doviecel  'VValzen- kürbis'.
5.56.  Tk.  ebnzine: Auch  buzine  'Affe'  [aus  ar.  abü  zina" 'Vater   der   Unzucht'];    hieraus  russ. obez'jana,  klruss.  obezjana  'Affe'  [vgl. lit.  bezdona].
557.  Tk.  efendi:
[Aus  gl-,  aiiöevxrii;  'Herr',  s.  Glotta  III, 289 ff.,  moderne  Aussprache  aftendis, und  zwar  Vokativ  auö^vxri  afMdi  MSOS I,  44,  Anm.  2];  früher  Ehrentitel  [s.  hier Nr.  28],  jetzt  entsprechend  unserer  höf- lichen Anrede  „mein  Herr,  monsieur". Frz.  efendi,  effendi,  dtsch.  Effendi  usw. [MWilJ  107.
558.  Mal.  egung :
```


## [2026-10-17T00:31:32.152Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; head -n 1413 LKT.txt | tr -cd '\\f' | wc -c; awk 'BEGIN{RS=\"\\f\"} NR==71' LKT.txt | grep -n -E '^ *[0-9]{2} *$' ; grep -n -E '^(4\\.?36|4\\.36|MONKEY|APE)' SYN.txt | head; awk 'BEGIN{RS=\"\\f\"} NR==213' SYN.txt | head -60",
 "description": "Locate LKT page and Buck p.188"
}
```


### [2026-10-17T00:31:32.464Z] TOOL RESULT

```
71
22:44
ti ‘sing’. Briickner 404.
ChSl. piitentct ‘young bird’, dim. of pita ‘bird’ (8.64), also ‘chicken’ like vooolov which it renders (Mt. 23.37).
Boh. slepice ‘hen’ (similar forms in Polabian), deriv. of slepy ‘blind’ (4.97), based on the hen’s blinking eyes? Miklosich 307.
SCr., Bulg. pile ‘chicken’ : Upper
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
ts
Digitized by Arya Samaj Foundation Chennai and eGangotri
ANIMALS 177
ble Sorb. pile 4, ‘duckling Lower » : Sorb. ea pile ‘duck’, Lith. pyptt, igosling ae ‘peep’, ete., all of Lees Y, Lf, re
ae er inakii, KZ 43.178. Walde
hs ss. cyplenok ‘chicken’, of imitative uss.
: kukkuta- ‘cock’, kukkutt- ‘hen’,
rig.
ct. A tre orig., like MLat. coccus, 0
pove, 2). | ae hrka-vaku- ‘eock’ (second part : tyoice’); Av. kahrkatas ‘cock’ (vul-
oe NPers. kark ‘fowl’, belonging
to the same imitative group as Ir. cerc ‘hen’, etc. (above, 3). Barth. 452.
Av. parodar§ ‘cock’ (ceremonial term), epd. of paré ‘in front, before’ and daras- ‘see’, hence lit. ‘seeing ahead’, that is, announcing the day. Barth. 859. On the pair parddar§ and kahrkatds, cf. Benveniste, Studia Indo-Iranica, Ehren- gabe fiir W. Geiger, 219 ff.
Av. karatodqsug ‘cock’, cpd. of karata- ‘knife’ and adj. *dqsu-: Skt. darig- ‘bite’, hence lit. ‘biting with knives’ with reference to the spurs. Barth. 454.
gar term), 3.56 GOOSE p Goth Lith.  Zqsis
Ge oe ON gas Lett. zass NG xiv Lat.  dnser Dan. gaas a *gast, gust
i Sw. gas SCr.  guska tf oca ie oie ON gos Boh. husa Sp. gausa, oca ME goos Pol. ges Rum. giscd NE goose Russ. gus’ Ir. ged, giugrann Du. gans Skt.  hansa- NIr. gé OHG gazs Ay. z W. guwydd MHG gans Br. gwaz NHG gans
1, If *§hans-, prob. fr. the root seen in Grk. xéoxw, éxavov ‘yawn, gape’, with reference to the goose’s characteristic Squawk with wide open bill. Walde-P. 1.536. Ernout-M. 56. Walde-H. 1.52. Berneker 342,
. Grk. xiv, Dor. xév; Lat. anser (for hanser) ; (Ir. géis ‘swan’) ; ON gas, OF ie OHG gans, etc., general Gmc. ; Lith. ass, ChSl. *gqsi, (gust), ete., general
Palto-Slavie (Slavic g fr. Gme.?); Skt Lansa- (also ‘swan’, etc.). :
Fr. ove, fr. late Lat. Bee on tion fr. avicula, aucu- as “bird’, with Specializa-
tion to ‘goose’, p
```


## [2026-10-17T00:31:41.303Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'MONKEY|APE\\b' SYN.txt | head; grep -n -i -E 'bozina|buzina|maymun|meymun|majmun|obez' SYN.txt | head",
 "description": "Grep Buck for monkey section"
}
```


### [2026-10-17T00:31:41.645Z] TOOL RESULT

```
855:1. Grk. és (also xov-oprés ‘dust stirred up’, but simply ‘dust’ in NT), NG pop. oxévy (o fr. forms of the article, ris, etc.; cf. Hatzidakis, Mec. 2.412) : Lat. cinis ‘ashes’, perh. fr. the root seen in Grk. xvaw ‘scrape’. Walde-P. 1.392. Boisacq 490.
968:Grk. Addos ‘nape of the neck, crest’ and ‘ridge, hill’, etym.? Walde-P. 1.93. Boisacq 588f. For ‘hill’ from ‘neck, crest’, cf. also Sp. cerro, Ir. cnoc, below.
980:Tr. cnoc ‘hill’, Br. krec’h, OBr. knoch (W. cnwceh ‘boss, knuckle’) : ON hnakki ‘nape of the neck’, NE neck, etc. Walde-P. 1.390 ff. Pedersen 1.160.
1082:W. cwm (Br. komb, komm in place names) : Ir, cum ‘vessel’, Grk. xipBy ‘drinking vessel, boat’, Skt. kumbha- ‘pot’, NE hump, etc., all with notion of curved shape. Walde-P. 1.376.
1181:precipitous bank or coast. yOS Past prégit, below, 6. The meaning ‘moun tain, hill’ appears in Rum. and ape place names. Densusianu Hats 349 f.
1308:‘curved shape’. Others are ‘harbor’, ‘branch’, ‘inlet’, or Gnflow’ (of the sea).
1392:Lat. amnis ‘river’ (poet.); Ir. ab (aba, oub, etc.), NIr. abha ‘river’, W. afon ‘river’, afonig ‘brook’, Br. aven ‘river’ (mostly obs.), Lith. upé, Lett. upe, OPruss. ape ‘river’, Lith. upelis, Lett. upele ‘brook’ (but Lett. upe also ‘brook’).
1592:1. Grk. AlGos ‘stone’, NG (Aidos lit.) pop. AJape ‘9 (large) stone’, etym.? Walde-P. 2.379. Boisacq 581.
1622:etc., fr. IE *gel- in words denoting spherical shape, whence ‘protuberance’, then ‘cliff’, ‘tock’. Walde-P. 1.614. Miihl.-Endz. 2.229.
4467:ME pigge (prob. OE *picga, like doc. ga, frocga), NE pig, MLG bigge, Dy. big, prob. : Dan. pig, Sw. pigg ‘spike’, etc. beside OE pic ‘pick, pike’, ete. (cf. Falk-Torp. 823), and orig. an epithet referring to the shape. Bjorkman, IF 30.266f. NED s.v. pig. Franck-y. w. 64.
5009:Grk. —_xl8nxos Goth. Lith. bezdzioné NG E itie patpod ON apt Lett. pertik'is Lat.  simia Dan. abe ChSl. (pitikit) It. scimmia Sw. ape SCr. majmun, opica Fy. singe OE apa Boh. opice
5010:Sp. mono ME ape Pol.  matpa Rum. maimu(d NE monkey (ape) Russ. obez’jana Ir. es atte Du. aap Skt. kapi- NIr. apa OHG affo Av. was
5027:Russ. obez’jana (> Lith. bezdZioné), fr. Turk. ebuzine. Lokotsch 556.
5029:SCr. majmun fr. Turk., Arab. mat- mun.
9486:OE ofet, OHG obaz, MHG obez, NHG obst, whence (Briickner 388) ChS]. ovosti, SCr. voée, Boh. ovoce, Pol. owoc, (Russ. ovosé ‘vegetables’), orig. ‘fruit’ in wider sense, as esp. OF ofet, etym. dub. Prell- witz, BB 25.158. G. S. Lane, JEGPh. 32.486 f.
32919:NG obvopov, dptov ON landam@ri Lett. ruobeZa
```


## [2026-10-17T00:31:44.066Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 5005,5032p SYN.txt; head -n 5009 SYN.txt | tr -cd '\\f' | wc -c",
 "description": "Read Buck MONKEY section"
}
```


### [2026-10-17T00:31:44.450Z] TOOL RESULT

```
C-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
188 SELECTED INDO-EUROPEAN SYNONYMS
3.76 MONKEY
Grk. —_xl8nxos Goth. Lith. bezdzioné NG E itie patpod ON apt Lett. pertik'is Lat.  simia Dan. abe ChSl. (pitikit) It. scimmia Sw. ape SCr. majmun, opica Fy. singe OE apa Boh. opice
Sp. mono ME ape Pol.  matpa Rum. maimu(d NE monkey (ape) Russ. obez’jana Ir. es atte Du. aap Skt. kapi- NIr. apa OHG affo Av. was
W. epa MHG aff
Br. marmouz NHG affe
Here is understood the generic name for the simians, NE: monkey in current popular usage, but formerly and still sometimes ape, though the latter now generally denotes the tailless species. Cf. NED s.v. ape.
1. Grk. wi@nxos, etym.? Walde-P. 2.186. This is the generic term, while kiros, xjBos (cf. below, 6) is specific. Cf. Aristot. HA 502° 6 pev xijBos ai@nxos éxwv obpav.
Byz. pipe : wipéopar ‘mimic’.
NG paupod, fr. Turk., Arab. maimin. Lokotsch 1365.
2. Lat. stmia (>It. scimmia, Fr. singe), deriv. of stmus, loanword fr. Grk. otés ‘snub-nosed’. First used as a nickname and prob. based on the name ZYuyuslas, Simia. Kretschmer, KZ 33, 563.
Olt., OFr. maimon, Rum. maimuté, also OIt. monna, Sp. mono, -a, fr. Arab. maimin. Lokotsch 1865. REW 5242.
3. NIr. apa, W. ab (arch.), fr. ME ape, OF apa (below, 4), W. epa late loan- word fr. NE ape.
Br. marmouz, fr. OF r. marmot or mar- mouset, both used for ‘monkey’ (also
‘small child’, etc.), history dub. Henry 196. REW 5587. Gamillscheg 593.
4. ON api, OF apa, OHG affo, etc., the general Gme. word, orig. unknown, perh. Celtic. Walde-P. 1.51 ff.
From Gme. come the Slavic forms, Boh. op, opice, SCr., ORuss. opica, etc. Stender-Petersen 361.
NE monkey, prob. fr. a MLG moneke (Moneke as name attested), dim. of the word that appears as Sp. mono, etc. (above, 2). NED s.v.
5. ChSl. (late) pitikd fr. Grk. riOnxos.
Boh. opice, etc. from Gme. (above, 4).
Russ. obez’jana (> Lith. bezdZioné), fr. Turk. ebuzine. Lokotsch 556.
Lett. pertik’is, fr. Esth. pertik (or con- versely?). Miithl.-Endz. 3.210.
SCr. majmun fr. Turk., Arab. mat- mun.
Pol. matpa fr. NHG maul-affe. Briickner 320.
6. Skt. kapi- : kapila- ‘brownish, red- dish’, fr. ‘smoke-colored, Grk. xamvés, etc.? Walde-P. 1.379. Prob. source of Egypt. gephi, Grk. xios, xfBos, etc. Schrader, Reallex. 1.16.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
223
```


## [2026-10-17T00:31:47.179Z] TOOL CALL #14: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg571.png"
}
```


### [2026-10-17T00:31:47.631Z] TOOL RESULT

```

```


## [2026-10-17T00:31:47.627Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-10-17T00:31:59.531Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; mkdir -p ocr/BOOK; cp $S/pg571.png ocr/BOOK/571.png; sed -n 1090,1100p KLN_1966.txt | cut -c1-200; grep -n -E '^(Zebedee|zealot|Zebulun|zebra|Zion|Zeus|zany|Zechariah|Zacharias)' KLN_1966.txt KLN_1971.txt | head; grep -c . KLN_1966.txt; tail -c 3000 KLN_1966.txt | head -40",
 "description": "Copy page image, search Klein end pages"
}
```


### [2026-10-17T00:31:59.956Z] TOOL RESULT

```
W.African
West  African
WSem.
West  Semitic
WTeut.
West  Teutonic
Zech.
Zechariah
Zeph.
Zephaniah
zool.
KLN_1971.txt:3854:Zechariah 
KLN_1971.txt:71803:Zeus’, fr. Aio?, gen. of Zeu?, ‘Zeus’, and ptTjSo?, 
KLN_1971.txt:71823:Zeus and cp. prec. word and the first element in 
KLN_1971.txt:141775:Zeus a dish of human flesh, in order to test his 
KLN_1971.txt:142573:Zeus at Athens, lit. ‘stormy, boisterous, impetu- 
KLN_1971.txt:197582:zebra. — A Hottentot name of imitative origin, 
KLN_1971.txt:270291:zany, n., a buffoon. — F. zani, borrowed fr. 
KLN_1971.txt:270340:zealot, n. — Late L. zeldtes , fr. Gk. 
KLN_1971.txt:270352:zebra, n. — Port., fr. Amharic zebra. 
KLN_1971.txt:270355:zebra-, combining form denoting stripiness. — 
41263
��  Lit.  ‘neigh¬ borhood’,  fr.  ML.  vicinetum,  fr.  L.  vicinus, ‘neighboring,  near’,  fr.  views,  ‘district’;  see vicinage.  Venue  in  this  sense  was  influenced  in form  by  venue,  ‘arrival’.
venule,  n.,  a  small  vein.  —  L.  venttla,  formed  fr.
vena  with  dimin.  suff.  -i da.  See  vein  and  -ule. Venus,  n.  —  L.  Venus,  gen.  Veneris,  ‘the  goddess of  love’.,  fr.  venus,  ‘love,  sexual  desire,  loveliness, attractiveness,  beauty,  charm’,  whence  venerari, ‘to  reverence,  worship,  venerate’.  See  venerate, vera,  n.,  name  of  a  tree,  Bu/nesia  arborea.  —  Am. Sp.,  fr.  Sp.  vera,  ‘border’,  which  derives  fr.  L. ora,  ‘border’  (through  the  intermediate  form *uera\  cp.  Sp.  hueso,  ‘bone’  (fr.  L.  ossum).  L. ora  (for  *osa)  is  a  collective  noun  formed  fr.  os, gen.  -oris,  ‘mouth,  opening,  entrance’.  See  oral, veracious,  adj.,  truthful,  true.  —  Formed  with suff.  -ous  fr.  L.  verax,  gen.  veracis,  ‘truthful, speaking  truly",  fr.  verus.  See  very.
Derivatives:  veracious-ly,  adj.,  veracious-ness,  n. veracity,  n.,  truthfulness,  truth.  —  F.  veracite,  fr. ML.  veracitdtem,  acc.  of  veracitas,  ‘truthfulness’, fr.  L.  verax,  gen.  -acis.  See  prec.  word  and  -ity. veranda,  verandah,  n.  —  Port,  varanda,  ‘balcony’, introduced  into  English  from  India.  Port,  ra- randa  itself  is  of  uncertain  origin.  F.  veranda was  borrowed  from  English.
Derivative:  veranda(h)-ed,  adj. verano,  n.,  the  dry  season  in  tropical  America.  — Sp.,  fr.  L.  ver,  ‘spring’.  See  vernal.
Verbesina
verascope,  n.,  a  small  stereoscopic  camera.  —  A hybrid  coined  fr.  L.  verus,  ���true’,  and  Gk. ruov,  fr.  mtoraiv,  ‘to  look  at,  examine’.  See very  and  -scope.  The  correct  form  would  be alethoscope  (fr.  Gk.  dcXvjffrji;,  ‘true’  and  -rsy.6- mov ) .
veratral,  n.,  the  radical  C9H10O4  (chem.)  —  Form¬ ed  with  adj.  suff.  -al  fr.  L.  verdtrum,  'hellebore’. See  veratrine.
veratric,  adj.,  pertaining  to  a  white  crystalline acid. —  Formed  with  adj.  suff.  -ic  fr.  L.  verdtrum, ‘hellebore’  (see  veratrine) ;  so  called  because  it  is easily  obtained  by  the  decomposition  of  vera¬ trine.  \
veratridine,  also  veratridin,  n.,  an  amorphous  al¬ kaloid  obtained  from  sabadilla  seeds, C36H61OnN  (chem.)  —  Coined  fr.  L.  verdtrum, ‘hellebore’  (see  next  word),  and  the  chem. suffixes  -ide  and  -ine  (resp.  -in), veratrine,  n.,  also  veratrin,  veratrina,  veratria,  a poisonous  mixture  of  alkaloids  obtained  from sabadilla  seeds,  used  in  medicine  in  the  treat¬ ment  of  rheumatism,  neuralgia,  etc.  —  F.  vera¬ trine,  fr.  ModL.  veratrina,  fr.  L.  verdtrum,  ‘helle¬ bore’,  fr.  verare ,  ‘to  tell  the  truth’,  fr.  verus, ‘true’;  so  called  because
```


## [2026-10-17T00:32:05.535Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E '^Zach|^Zechar|^Zacchae' KLN_1971.txt | head; n=$(grep -n -i -m1 -E '^Zachar' KLN_1971.txt | cut -d: -f1); [ -n \"$n\" ] && sed -n \"${n},$((n+14))p\" KLN_1971.txt; grep -n -i -E '^gibbon' KLN_1971.txt; m=$(grep -n -i -m1 -E '^gibbon' KLN_1971.txt|cut -d: -f1); sed -n \"${m},$((m+5))p\" KLN_1971.txt",
 "description": "Grep Klein 1971 for Zachariah and gibbon"
}
```


### [2026-10-17T00:32:05.936Z] TOOL RESULT

```
3854:Zechariah 
270220:Zachariah, Zacharias, Zachary, masc. PN. {Bi- 
270234:Zacchaeus, Zaccheus, masc. PN. — Late L. Zac- 
270375:Zechariah, n., in the Bible, 1) the eleventh in the 
270377:Zechariah (Bible). — Heb. See Zachariah. 
Zachariah, Zacharias, Zachary, masc. PN. {Bi- 
ble). — Late L. Zacharias , fr. Gk. 
fr. Heb. Zakhar ydhu, Z*kharyah , lit. ‘the Lord 
has remembered’. The first element of this com- 
pound name derives fr. Heb. zdkhar , ‘he re- 
membered’, whence also zekher , zikkdron, ‘re- 
membrance, memorial’, azkara h , 'memorial 
offering; name’. Cp. Aram.-Syr. d e khar, Arab. 
dhakara , Ethiop. zakhdra , ‘he remembered’, 
Akkad, sakaru , zakdru , ‘to say, name, swear’, 
zikru , ‘name’. For the second element see Elijah 
and cp. words there referred to. Cp. Zecha- 
riah. 

Zacchaeus, Zaccheus, masc. PN. — Late L. Zac- 
102420:gibbon, n., a small, long-armed ape. — F., a name 
gibbon, n., a small, long-armed ape. — F., a name 
of Indian origin brought to Europe by the 
Marquis Joseph-Fran<;ois Dupleix (1697-1763), 
governor-general of the French possessions in 
India (1742-54).
```


## [2026-10-17T00:32:12.748Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for f in BQT_v1_pages.txt MON_part1.txt MON_part2.txt; do echo \"== $f\"; grep -n -E 'بوزینه|بوزنه' $f | head -5 | cut -c1-400; done; echo == HRN; grep -n -i -E 'bûzin|buzin|bôzin|būzīn|būzna|bûzna' HRN.txt HUB.txt | head; echo == TTS; command ls incoming/TTS; grep -n -i -E 'buzin|ebuzin|ebu ?zin' incoming/TTS/*.txt | head",
 "description": "Grep Persian and Turkic sources for bozine"
}
```


### [2026-10-17T00:32:13.207Z] TOOL RESULT

```
Exit code 1
== BQT_v1_pages.txt
22116:میمون است که بوزینه بائد - و بکسر او بر
30734:س رکرمی و مشفولی: هو بفرمود تاهمةٌ مطربان و مسض رکان و هزالان و سگان شکاری و بوزنه
== MON_part1.txt
26095:بورینه: (6-)۱1212 [- بوزینا - بوزنه - 
26100:بوزنه: (م-)هم002 (۱.) شکو فه و هار درخت 
82874:میمون» بوزینه. 
== MON_part2.txt
12191:فرد: 2۵«(ع.] (4.) بوزینه» میمون نر) ج. 
12195:فردبوزینه؛ ج. قرد. 
29953:ک 0۲ [- کپی - کبی] (.) بوزینه؛ 
70813:هندوستان می‌زید؛ بوزینه‌هاء بوزنه‌ها. 
72114:نازین (قس. بوزینه) | (ص‌نسه.) دارنده نازء 
(eval):1: = not found
```


## [2026-10-17T00:32:17.929Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 26093,26100p MON_part1.txt; echo ==BQT; grep -n -E '^بوزینه|بوزینه[ :]|بوزنه' BQT_v1_pages.txt | head; grep -n 'بوزینه' BQT_v1.txt BQT_alt_v1.txt | head -5 | cut -c1-300; echo; grep -n -i 'buzin\\|bûzin\\|bozin\\|buzna' HRN.txt HUB.txt BQT_v1_pages.txt | head",
 "description": "Read Moin bozine entry, Borhan"
}
```


### [2026-10-17T00:32:18.226Z] TOOL RESULT

```
Exit code 1
ارزن و جو سازند. 

بورینه: (6-)۱1212 [- بوزینا - بوزنه - 
بوزنینه ] (.) (جاذ.) میمون. 

بوژ: (02۳2)00۷ (.) گرداب. 

بوزنه: (م-)هم002 (۱.) شکو فه و هار درخت 
(eval):1: =BQT not found
```


## [2026-10-17T00:32:22.311Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'بوزین|بوزنه|بوزنا' BQT_v1_pages.txt | head -20 | cut -c1-300; grep -n -E 'بوزین|بوزنه' BQT_v1.txt | head | cut -c1-300",
 "description": "Grep Borhan vol1 for bozine variants"
}
```


### [2026-10-17T00:32:22.729Z] TOOL RESULT

```
22116:میمون است که بوزینه بائد - و بکسر او بر
30734:س رکرمی و مشفولی: هو بفرمود تاهمةٌ مطربان و مسض رکان و هزالان و سگان شکاری و بوزنه
44099:میمون است که بوزینه بائد - و بکسر او بر 
63065:س رکرمی و مشفولی: هو بفرمود تاهمةٌ مطربان و مسض رکان و هزالان و سگان شکاری و بوزنه
```


## [2026-10-17T00:32:27.578Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^ *بوز' BQT_v1_pages.txt | head -30 | cut -c1-200; grep -n -E 'abu zin|abū zin|ابوزنه|ابو زنه|أبو زنة|ابوزنة' BQT_v1_pages.txt MON_part*.txt AFM_pages.txt | head",
 "description": "Look for Borhan headwords starting with buz"
}
```


### [2026-10-17T00:32:27.936Z] TOOL RESULT

```
12842:بوزد و جریی میم سائله گوبند و بسل لبن
```


## [2026-10-17T00:32:32.033Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,40p tools/fetch_source.py | head -50",
 "description": "Check fetch_source tool usage"
}
```


### [2026-10-17T00:32:32.462Z] TOOL RESULT

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


## [2026-10-17T00:32:38.228Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in 'https://en.wiktionary.org/wiki/Zachariah' 'https://en.wiktionary.org/wiki/gibbon' 'https://www.etymonline.com/word/gibbon' 'https://www.etymonline.com/word/Zachariah' 'https://en.wiktionary.org/wiki/بوزینه' 'https://en.wiktionary.org/wiki/زنا' 'https://en.wiktionary.org/wiki/ذکر' 'https://en.wiktionary.org/wiki/زکریا' 'https://en.wiktionary.org/wiki/Ζαχαρίας' 'https://en.wiktionary.org/wiki/обезьяна' 'https://en.wiktionary.org/wiki/زكريا' 'https://vajehyab.com/dehkhoda/بوزینه' 'https://en.wiktionary.org/wiki/ز_ن_ي' 'https://en.wiktionary.org/wiki/ذ_ك_ر'; do python3 tools/fetch_source.py \"$u\" --note \"page 571, Z.k.r / Z.n.y verification\" 2>&1 | tail -1; done",
 "description": "Archive Wiktionary/Etymonline pages",
 "timeout": 300000
}
```


### [2026-10-17T00:32:46.994Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/fe71dcdf01d7e80b.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/5b69fb503d4db1b7.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/5480297bf52b0bbb.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f7a7d0c69c6fa85b.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/eebb9864227854c6.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d1829cb433110112.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e13107ffd46e76a8.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/7e6388242044da6b.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b166c71cbf80b05a.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/de71bb615c38ad6d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/68cf1fe4a953259c.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a52404454a520ad1.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a62a290063d1f925.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/017b565495e0c797.txt
```


## [2026-10-17T00:32:51.123Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; tail -14 index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n  d=json.loads(l);print(d['url'],d.get('status'),d.get('bytes'))\"; for f in fe71dcdf01d7e80b 5b69fb503d4db1b7 5480297bf52b0bbb f7a7d0c69c6fa85b eebb9864227854c6 7e6388242044da6b de71bb615c38ad6d; do echo \"#### $f\"; grep -n -i -A6 'Etymology' $f.txt | head -24 | cut -c1-500; done",
 "description": "Read etymology sections of fetched pages"
}
```


### [2026-10-17T00:32:51.569Z] TOOL RESULT

```
https://www.etymonline.com/word/gibbon -1 39
https://www.etymonline.com/word/Zachariah -1 39
https://abadis.ir/fatofa/زبد/ 200 4860
https://en.wiktionary.org/wiki/بوزینه 200 3623
https://en.wiktionary.org/wiki/زنا 200 11957
https://abadis.ir/fatofa/مضحک/ 200 4463
https://en.wiktionary.org/wiki/ذکر 200 6736
https://en.wiktionary.org/wiki/زکریا 200 6727
https://en.wiktionary.org/wiki/Ζαχαρίας 200 4703
https://en.wiktionary.org/wiki/обезьяна 200 6367
https://en.wiktionary.org/wiki/زكريا 200 4983
https://vajehyab.com/dehkhoda/بوزینه 200 1245
https://en.wiktionary.org/wiki/ز_ن_ي -1 39
https://en.wiktionary.org/wiki/ذ_ك_ر -1 39
#### fe71dcdf01d7e80b
65: Etymology 
66-
67- 1.3 
68- Proper noun 
69-
70- Toggle the table of contents 
71-
--
151: Etymology
152- [ edit ] 
153-
154- From Hebrew זְכַרְיָה ( Zəḵaryā , “ Yahweh has remembered ” ) under influence from Latin Zacharias and Koine Greek Ζαχαρίας ( Zakharías ) . Doublet of Zach , Zachary , Zacharias , Zechariah , Zakariya , and Jakariya .
155-
156- Proper noun
157- [ edit ] 
#### 5b69fb503d4db1b7
62: Etymology 1 
63-
64- 1.1.1 
65- Alternative forms 
66-
67- 1.1.2 
68- Pronunciation 
--
86: Etymology 2 
87-
88- 1.2.1 
89- Noun 
90-
91- 1.3 
92- Anagrams 
--
100: Etymology 
101-
102- 2.2 
103- Pronunciation 
104-
105- 2.3 
106- Noun 
--
#### 5480297bf52b0bbb
#### f7a7d0c69c6fa85b
#### eebb9864227854c6
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
--
145: Etymology
146- [ edit ] 
147-
148- Inherited from Proto-Iranian [Term?] ; compare Pashto بيزو ( bízo , “ monkey ” ) . Anciently borrowed into Old East Slavic обезьꙗ́на ( obezĭjána ) whence Russian обезья́на ( obezʹjána , “ monkey, ape ” ) , and likely into Old Turkic 𐰋𐰃𐰲𐰃𐰤 ( béčin , “ monkey ” ) .
149-
150- Pronunciation
151- [ edit ] 
#### 7e6388242044da6b
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Proper noun 
--
79: Etymology 
80-
81- 2.2 
82- Pronunciation 
83-
84- 2.3 
85- Proper noun 
--
163: Etymology
164- [ edit ] 
165-
166: Etymology tree
167-
168- Biblical Hebrew זכר ( zakhár ) 
169-
170- Biblical Hebrew יהוה ( YHWH ) 
#### de71bb615c38ad6d
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
--
79: Etymology 
80-
81- 2.2 
82- Pronunciation 
83-
84- 2.3 
85- Noun 
--
196: Etymology
197- [ edit ] 
198-
199- Borrowed from Russian обезья́на ( obezʹjána ) .
200-
201- Pronunciation
202- [ edit ] 
--
```


## [2026-10-17T00:32:56.863Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; sed -n 108,125p 5b69fb503d4db1b7.txt; sed -n 140,160p eebb9864227854c6.txt; echo '#### zakariya'; sed -n 160,200p 7e6388242044da6b.txt | grep -v '^\\s*$' | head -30; echo '#### greek'; grep -n -A4 -i 'Etymology' b166c71cbf80b05a.txt | tail -8",
 "description": "Read gibbon, bozine, Zakariya, Greek entries"
}
```


### [2026-10-17T00:32:57.263Z] TOOL RESULT

```
 3 
 French 

 Toggle French subsection 

 3.1 
 Etymology 

 3.2 
 Pronunciation 

 3.3 
 Noun 

 3.4 
 References 

 3.5 
 From Wiktionary, the free dictionary

 Persian
 [ edit ] 

 Etymology
 [ edit ] 

 Inherited from Proto-Iranian [Term?] ; compare Pashto بيزو ( bízo , “ monkey ” ) . Anciently borrowed into Old East Slavic обезьꙗ́на ( obezĭjána ) whence Russian обезья́на ( obezʹjána , “ monkey, ape ” ) , and likely into Old Turkic 𐰋𐰃𐰲𐰃𐰤 ( béčin , “ monkey ” ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /buː.ziː.ˈna/ 

 ( Dari, formal ) IPA ( key ) : [buː.ziː.ná] 

 ( Dari, formal ) IPA ( key ) : [buː.ziː.ná] 
 ( Kabuli ) IPA ( key ) : [buː.ziː.ná] 

 ( Hazaragi ) IPA ( key ) : [bu.zi.ná] 
#### zakariya
 Wikipedia fa 
 Etymology
 [ edit ] 
 Etymology tree
 Biblical Hebrew זכר ( zakhár ) 
 Biblical Hebrew יהוה ( YHWH ) 
 Biblical Hebrew יָהּ ( Yah ) 
 Biblical Hebrew ־יה ( -yá ) 
 Biblical Hebrew זְכַרְיָה ( zəḵaryā ) bor. 
 Classical Syriac ܙܟ݂ܼܿܪܝܵܐ ( z'ḵaryāʾ ) bor. 
 Arabic زَكَرِيَّا ( zakariyyā ) bor. 
 Persian زکریا 
 Borrowed from Arabic زَكَرِيَّا ( zakariyyā ) .
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /za.ka.rij.ˈjaː/ 
 ( Dari, formal ) IPA ( key ) : [zä.kʰä.ɾi.jɑː] 
 ( Dari, formal ) IPA ( key ) : [zä.kʰä.ɾi.jɑː] 
 ( Kabuli ) IPA ( key ) : [zä.kʰä.ɾi.jɑː] 
 ( Hazaragi ) IPA ( key ) : [zä.kʰä.ɾi.jɔː] 
 ( Iran, formal ) IPA ( key ) : [zæ.kʰʲæ.ɹi.jɒː] 
 ( Tajik, formal ) IPA ( key ) : [zä.kʰä.ɾi.jɔ] 
 Rhymes: -aː 
 Readings
#### greek
65- Pronunciation 
66-
--
159: Etymology
160- [ edit ] 
161-
162- From Hebrew זְכַרְיָה ( zəḵaryā ) .
163-
```


## [2026-10-17T00:33:02.892Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -n -B2 -A8 'Etymology' 5b69fb503d4db1b7.txt | sed -n '/\\[ edit \\]/,+8p' | grep -v '^\\S*-\\s*$' | head -40; echo '#### russ'; grep -n -A4 'Etymology' de71bb615c38ad6d.txt | grep -i -E 'Turk|Persian|Arab|обез' | head; echo '#### zina'; grep -n -A3 'Etymology' d1829cb433110112.txt | grep -v '^\\S*-\\s*$'| head -20; echo '#### dhikr'; grep -n -A3 'Etymology' e13107ffd46e76a8.txt | grep -v '^\\S*-\\s*$' | head -20; echo '#### dehkhoda'; cat a52404454a520ad1.txt | head -40; echo '#### ar zakariya'; grep -n -A3 'Etymology' 68cf1fe4a953259c.txt | head",
 "description": "Read remaining etymology sections"
}
```


### [2026-10-17T00:33:03.274Z] TOOL RESULT

```
223- [ edit ] 
225- Reborrowing from French gibbon , folk etymology (compare English Gibbon ) [ 1 ] ultimately from a Northern Aslian language (compare Batek kəboɲ ). [ 2 ] 
227- Alternative forms
228- [ edit ] 
230- guibon ( obsolete ) 
375- [ edit ] 
377- Noun
378- [ edit ] 
380- gibbon ( plural gibbons ) 
382- Alternative form of jibbon ( “ spring onion ” ) .
397- [ edit ] 
399- Borrowed from French gibbon .
401- Pronunciation
402- [ edit ] 
404- IPA ( key ) : /ˈɣɪ.bɔn/ 
418- [ edit ] 
420: Etymology
421- [ edit ] 
423- Brought to Europe from French India by Joseph François Dupleix , probably from an English folk etymology (compare English Gibbon ) [ 1 ] with an Aslian root. [ 2 ] 
425- Pronunciation
426- [ edit ] 
445- [ edit ] 
447: Douglas Harper ( 2001–2026 ), “ gibbon ”, in Online Etymology Dictionary . 
449- “ gibbon ”, in Trésor de la langue française informatisé [ Digitized Treasury of the French Language ], 2012 
451- Retrieved from " https://en.wiktionary.org/w/index.php?title=gibbon&oldid=93364675 "
453- Categories : English terms borrowed from French 
#### russ
199- Borrowed from Russian обезья́на ( obezʹjána ) .
229- Inherited from Old East Slavic обезьꙗ́на ( obezĭjána ) , обозьꙗ́на ( obozĭjána ) , further borrowed from Persian ابوزینه ( abuzina ) , بوزینه ( buzina , “ simian ” ) . Cognates include Old Ruthenian обезъꙗ́на ( obezʺjána ) .
#### zina
62: Etymology 1 
64- 1.1.1 
65- Noun 
71: Etymology 2 
73- 1.2.1 
74- Verb 
77: Etymology 3 
79- 1.3.1 
80- Verb 
91: Etymology 
93- 2.3 
94- Noun 
117: Etymology 
119- 3.3 
120- Pronunciation 
140: Etymology 
142- 4.2 
143- Noun 
219: Etymology 1
220- [ edit ] 
#### dhikr
70: Etymology 
72- 2.2 
73- Pronunciation 
90: Etymology 1 
92- 3.1.1 
93- Pronunciation 
99: Etymology 2 
101- 3.2.1 
102- Pronunciation 
116: Etymology 1 
118- 4.1.1 
119- Pronunciation 
125: Etymology 2 
127- 4.2.1 
128- Pronunciation 
228: Etymology
229- [ edit ] 
231- Borrowed from Arabic ذِكْر ( ḏikr ) . 
282: Etymology 1
283- [ edit ] 
#### dehkhoda
URL: https://vajehyab.com/dehkhoda/بوزینه
FETCHED: 2026-10-17T00:32:45Z
STATUS: 200
TITLE: معنی بوزینه | لغت‌نامه دهخدا | واژه یاب

معنی بوزینه | لغت‌نامه دهخدا | واژه یاب 

 26 فرهنگ 

 همه دیکشنری مترادف طیفی آزاد + 

 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 

 بوزینه

 لغت‌نامه دهخدا
 بوزینه . [ ن َ / ن ِ ] (اِ) میمون را گویند. (برهان ). کنیت میمون که آنرا بفارسی کپی خوانند. بوزینه مخفف ابوزینه . (از غیاث ) (آنندراج ). پهنانه . (فرهنگ اسدی ). ابوخالد.ابوحبیب . ابوخلف . ابوزنه . ابوقشه . ابوقیس . (المرصع). کپی . قرد. حمدونه . شادی . بوزنه . (یادداشت بخط مؤلف ) : هرکه بتکلیف کاری کند که سزای آن نباشد بدو آن رسد که بدان بوزینه رسید. (کلیله و دمنه ). بوزینه بر چوب نشست و بریدن گرفت . (کلیله و دمنه ).
کافران اندر مری بوزینه طبع
آفتی آمد درون سینه طبع.
 مولوی .

پس خدا آن قوم رابوزینه کرد
چون که عهد خود شکستند از نبرد.
 مولوی .

- امثال :
 بوزینه را با درودگری چه کار .
رجوع به بوزنه و بوزنینه وامثال و حکم دهخدا شود.

 بوزینه در فرهنگ‌های دیگر
 معنی بوزینه در فرهنگ انتشارات معین 
 معنی بوزینه در فرهنگ فارسی عمید / قربان‌زاده 
 معنی بوزینه در دیکشنری فارسی به عربی 
 معنی بوزینه در دیکشنری فارسی به انگلیسی 
 معنی بوزینه در دیکشنری فارسی به ترکی 
 معنی بوزینه در فرهنگ مترادف و متضاد 
 واژه‌های مشابه
 بودینه 
 بوزانة 
 بوزنه 
#### ar zakariya
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
--
145: Etymology
146- [ edit ] 
147-
148: Etymology tree
149-
```


## [2026-10-17T00:33:21.771Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^ذکر[: ]|^زنا[: ]|^زکریا|^ذاکر' MON_part1.txt MON_part2.txt | head; grep -n -i -E 'b[uūû]z[iīî]n|b[uūû]zn' HRN.txt HUB.txt PHD.txt NYB_vol2_glossary.txt | head; grep -n -E 'زكريا|زکریا' AFM_pages.txt FVQ_pages.txt | head -3; grep -n -E 'بوزينة|بوزنة|ابوزنة|أبو زنة' AFM_pages.txt incoming/PLA/*.txt 2>/dev/null | head; grep -n -E 'بوزینه|بوزنه' incoming/ARY/ARY_pages.txt | head -3",
 "description": "Grep Moin, Horn, AFM, PLA, ARY"
}
```


### [2026-10-17T00:33:22.282Z] TOOL RESULT

```
MON_part2.txt:4041:زنا کار+ ج. فاجر ین فحار . قحر ۵. 
MON_part2.txt:4086:زنا کار؛ روسپی» جنده؛ ج. فواحش. (.) هر 
MON_part2.txt:7395:زنا کاری. (ا.) کار بد» گناه. زنا. فسق و فجور: 
MON_part2.txt:11488:زنا کاری» روسپی‌گری. 
MON_part2.txt:57199:ذکر شی به لفظی غیر از لفظ مقرر برای 11 
MON_part2.txt:89582:ذکر شده است که اين هم نمی تواند تابع 
MON_part1.txt:11442:ذکر ادواتی مانند: مگ سوای» الا» نجز 
MON_part1.txt:21659:زنا کار لواط کننده. 
MON_part1.txt:32610:زنا کار» زانی. 
MON_part1.txt:65002:ذاکر. (فل. روان.) قوه‌ای در انسان که حوادث 
HUB.txt:3066:dafur buztna, buzina etc. gebraucht.
HUB.txt:9718:p. 87, Nr. 842 — 845. Np. buzina (im pi. huzinagan) schon
```


## [2026-10-17T00:33:25.968Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 3058,3068p HUB.txt; echo ----; sed -n 9712,9722p HUB.txt; head -n 3066 HUB.txt | tr -cd '\\f' | wc -c; grep -n -E '^زنا|^ذکر|^زکریا|^بوزینه' MON_part1.txt MON_part2.txt | head",
 "description": "Read Hubschmann buzina passages"
}
```


### [2026-10-17T00:33:26.346Z] TOOL RESULT

```
*) Besser: hari = idg. kor9 zweisilbig.— 87 —
skr. ^JfOsa^ zuriickgeht. Den Lauten nach kann das
Wort sowohl Lehnwort wie Originalwort sein.
842. Vgl. modern asp i kdtbud *Grausehimmer, Kosen,
Np. Sprachftihrer p. 38.
Hier fehlt np. kaM 'Affe JRAS. 1894, p. 480 = phi.
hapik, arm. LW. kapik, skr. Icapi-. Das Wort ist
in alter Zeit aus dem Indischen entlehnt. Jetzt wird
dafur buztna, buzina etc. gebraucht.
845. Lies afgh. kon (fem. kana *taub'). Vgl. Idg. Forsch.
Ill, 169, Anm.
----
11 n. 8. w.
p. 79, Nr. 782. Vgl. WZKM. 8, 276.
p. 82, Nr. 800. Np. mdrisBba belegt v. Stackelberg, ZDMG.
48, 494.
p. 83, Nr. 808. Vgl. syr. HIID (in Ardasir-xurrah) ZDMG.
43, 397, Z. 1 (vor 544 p. Chr.).
p. 87, Nr. 842 — 845. Np. buzina (im pi. huzinagan) schon
im alten Korancommentar, JRAS. 1894, 449.
p. 87, Nr. 861. Np. kal (wo vorkommend?) = ka6al *calvus*
= zd. kaurva-, lat. calvus, Geiger, Idg. F.
IV, Anz. 23. Lat. calvus (aus *calovos) zu
97
MON_part2.txt:1637:زنان» عشقبازی کردن. حکایت کردن از 
MON_part2.txt:1658:زنان در آن رشته را به وقت دوختن 
MON_part2.txt:4041:زنا کار+ ج. فاجر ین فحار . قحر ۵. 
MON_part2.txt:4086:زنا کار؛ روسپی» جنده؛ ج. فواحش. (.) هر 
MON_part2.txt:7395:زنا کاری. (ا.) کار بد» گناه. زنا. فسق و فجور: 
MON_part2.txt:7492:زنان بر آن نشینند؛ ج. فشول. 
MON_part2.txt:10489:زنانه, طمث» خونر بزی ماهانه» بی‌نمازی؛ 
MON_part2.txt:10493:زنان به علت شروع دوره بائسی با به علت 
MON_part2.txt:11488:زنا کاری» روسپی‌گری. 
MON_part2.txt:19333:زنان پنبةٌ رشتنی و ریسمان رشته شده را در
```


## [2026-10-17T00:33:31.104Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for w in بوزینه زنا ذکر زکریا; do f=$(python3 tools/fetch_source.py \"https://vajehyab.com/moein/$w\" --note \"page 571, Mo'in entry for $w\" 2>&1|tail -1); echo \"### $w\"; grep -v '^\\s*$' $f | sed -n 8,16p | cut -c1-400; done",
 "description": "Fetch Moin entries from vajehyab",
 "timeout": 200000
}
```


### [2026-10-17T00:33:33.290Z] TOOL RESULT

```
### بوزینه
 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 
 بوزینه
 فرهنگ انتشارات معین
 (نِ) ( اِ.) میمون .
 بوزینه در فرهنگ‌های دیگر
 معنی بوزینه در لغت‌نامه دهخدا 
 معنی بوزینه در فرهنگ فارسی عمید / قربان‌زاده 
 معنی بوزینه در دیکشنری فارسی به عربی 
 معنی بوزینه در دیکشنری فارسی به انگلیسی 
### زنا
### ذکر
 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 
 ذکر
 فرهنگ انتشارات معین
 (ذَ کَ) [ ع . ] (اِ.) 1 - نر، نرینه . ج . ذکور. 2 - آلت تناسلی مرد.
 ذکر در فرهنگ‌های دیگر
 معنی ذکر در لغت‌نامه دهخدا 
 معنی ذکر در فرهنگ فارسی عمید / قربان‌زاده 
 معنی ذکر در دیکشنری عربی به فارسی 
 معنی ذکر در دیکشنری فارسی به عربی 
### زکریا
```


## [2026-10-17T00:33:40.672Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/page-558.json'));print(d['verified_by'],d['verified_on'])\"; grep -c . data/verification/sources/web/index.jsonl; grep -o '\"url\": \"[^\"]*\"' data/verification/sources/web/index.jsonl | tail -20",
 "description": "Check prior metadata and archived URLs"
}
```


### [2026-10-17T00:33:41.024Z] TOOL RESULT

```
claude-opus-5.5 2026-10-16
6825
"url": "https://en.wiktionary.org/wiki/eczema"
"url": "https://en.wiktionary.org/wiki/zeolite"
"url": "https://en.wiktionary.org/wiki/𐭩𐭥𐭰"
"url": "https://en.wiktionary.org/wiki/yeast"
"url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yewH-_(mix)"
"url": "https://en.wiktionary.org/wiki/Gemini"
"url": "https://en.wiktionary.org/wiki/zeolit"
"url": "https://en.wiktionary.org/wiki/ζέω"
"url": "https://en.wiktionary.org/wiki/𐬫𐬌𐬨𐬀"
"url": "https://en.wiktionary.org/wiki/خدنگ"
"url": "https://en.wiktionary.org/wiki/شیون"
"url": "https://en.wiktionary.org/wiki/بخشودن"
"url": "https://en.wiktionary.org/wiki/بخشیدن"
"url": "https://en.wiktionary.org/wiki/افشردن"
"url": "https://en.wiktionary.org/wiki/فشار"
"url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Turkic/kadïŋ"
"url": "https://vajehyab.com/moein/بوزینه"
"url": "https://vajehyab.com/moein/زنا"
"url": "https://vajehyab.com/moein/ذکر"
"url": "https://vajehyab.com/moein/زکریا"
```


## [2026-10-17T00:33:45.771Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; sed -n 219,226p d1829cb433110112.txt; grep -n -i 'zinā\\|زِنًا\\|زِنَى\\|Persian' d1829cb433110112.txt | head -8",
 "description": "Read Wiktionary zina etymology"
}
```


### [2026-10-17T00:33:46.102Z] TOOL RESULT

```
 Etymology 1
 [ edit ] 

 Noun
 [ edit ] 

 زِنًا • ( zinan )  m ( construct state زِنَا ( zinā ) ) 

109: Persian 
111: Toggle Persian subsection 
225: زِنًا • ( zinan )  m ( construct state زِنَا ( zinā ) ) 
227: alternative form of زِنَاء ( zināʔ ) 
234: Declension of noun زِنًا ( zinan )
249: zinā 
252: az-zinā 
255: zinā
```


## [2026-10-17T00:33:48.228Z] AGENT

Now writing the JSON.


## [2026-10-17T00:35:55.613Z] TOOL CALL #31: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-571.py <<'EOF'\nimport json\nW={\n'zach':\"https://en.wiktionary.org/wiki/Zachariah\",\n'gib':\"https://en.wiktionary.org/wiki/gibbon\",\n'buz':\"https://en.wiktionary.org/wiki/بوزینه\",\n'zina':\"https://en.wiktionary.org/wiki/زنا\",\n'zekr':\"https://en.wiktionary.org/wiki/ذکر\",\n'zakfa':\"https://en.wiktionary.org/wiki/زکریا\",\n'zakar':\"https://en.wiktionary.org/wiki/زكريا\",\n'gr':\"https://en.wiktionary.org/wiki/Ζαχαρίας\",\n'ru':\"https://en.wiktionary.org/wiki/обезьяна\",\n'dkh':\"https://vajehyab.com/dehkhoda/بوزینه\",\n'mbuz':\"https://vajehyab.com/moein/بوزینه\",\n'mzekr':\"https://vajehyab.com/moein/ذکر\",\n}\nKLN71_Z=\"KLN_1971.txt l.270220 s.v. Zachariah: 'Late L. Zacharias, fr. Gk. [Zacharias], fr. Heb. Zakhar yahu, Zekharyah, lit. the Lord has remembered ... fr. Heb. zakhar, he remembered ... Cp. Aram.-Syr. dekhar, Arab. dhakara, Ethiop. zakhara, he remembered, Akkad. sakaru, zakaru, to say, name, swear'\"\nKLN66_T=\"KLN_1966.txt l.38814 s.v. tezkirah: 'Arab. tadhkirah, verbal noun of dhakkara ... second conjugation of dhakara, he remembered, which is rel. to Heb. zakhar, he remembered, zekher, remembrance'\"\nFVQ_Z=\"FVQ_pages.txt l.5621ff. (Jeffery p.151) s.v. Zakariyya: 'the early authorities recognized the name as foreign, al-Jawaliqi, Mu'arrab, 77. The probabilities seem to be that it came into Ar. from Syr. ... found in Mandaean ... influenced by Arabic'\"\nLKT_556=\"LKT.txt leaf 71 = printed p.44, no. 556: 'Tk. ebuzine: Auch buzine Affe [aus ar. abu zina Vater der Unzucht]; hieraus russ. obez'jana, klruss. obezjana Affe [vgl. lit. bezdona]'\"\nSYN_188=\"SYN.txt p.188, 3.76 MONKEY (grep 'obez'): 'Russ. obez'jana (> Lith. bezdzione), fr. Turk. ebuzine. Lokotsch 556.' — no word on the Arabic/Persian etymon\"\nKLN_GIB=\"KLN_1966.txt l.16112 s.v. gibbon: 'F., a name of Indian origin brought to Europe by the Marquis Joseph-Francois Dupleix (1697-1763), governor-general of the French possessions in India (1742-54)' — no Persian/Hindustani etymon named\"\nHUB_87=\"HUB.txt p.87 (nos. 842-845) and Nachtraege p.97 (grep 'buzina'): 'np. kabi Affe ... aus dem Indischen entlehnt. Jetzt wird dafur buzina, buzina etc. gebraucht'; 'Np. buzina (im pl. buzinagan) schon im alten Korancommentar, JRAS 1894, 449' — treated as a Persian word, no Arabic origin suggested\"\nMON_BUZ=\"vajehyab Mo'in s.v. بوزینه: '(نِ) (اِ.) میمون.' — no [ع.] Arabic tag; MON_part1.txt l.26095 'بوزینه ... [= بوزینا = بوزنه = بوزنینه] (اِ.) (جانو.) میمون' likewise untagged\"\nDKH_BUZ=\"vajehyab Dehkhoda s.v. بوزینه: 'کنیت میمون ... بوزینه مخفف ابوزینه (از غیاث) (آنندراج) ... ابوزنه ... (المرصع)' — the traditional Persian lexicographers' derivation from an Arabic kunya\"\nWK_BUZ=\"Wiktionary بوزینه: 'Inherited from Proto-Iranian; compare Pashto بيزو (bízo, monkey). Anciently borrowed into Old East Slavic обезьꙗна whence Russian обезьяна'\"\nWK_GIB=\"Wiktionary gibbon (French/English): 'Brought to Europe from French India by Joseph François Dupleix, probably from an English folk etymology (compare English Gibbon) with an Aslian root'; 'ultimately from a Northern Aslian language (compare Batek kəboɲ)'\"\n\ndef n(id,lang,words,verdict,der,derfa,src,rc,con,**kw):\n    d=dict(id=id,lang=lang,words=words,verdict=verdict,derivation=der,derivation_fa=derfa,sources=[W[s] for s in src],ref_check=rc,consulted=con); d.update(kw); return d\nNC=lambda r,why=\"no digital copy accessible\": {\"ref\":r,\"status\":\"not_checked\",\"note\":why}\n\ne0_nodes=[\nn(1,\"Arabic\",\"z.k.r\",\"confirmed\",\n \"Arabic ذَكَرَ ḏakara 'to remember, mention', root ḏ-k-r, the regular reflex of Proto-Semitic *ḏ-k-r (Hebrew and Akkadian merge *ḏ with z, Aramaic/Syriac shift it to d: dəḵar, Arabic keeps ḏ). Nourai writes the root 'z.k.r' in Persian pronunciation (Persian reads ذ as z); strictly the Arabic root is ḏ.k.r, but the identification is correct.\",\n \"ریشهٔ عربی ذ-ک-ر (ذَکَرَ ḏakara «یاد کردن، بر زبان آوردن») همان ریشهٔ سامی آغازین *ḏ-k-r است؛ در عبری و اکدی ذ به ز و در آرامی/سریانی به د بدل شده و عربی ذ را نگه داشته است. نورایی ریشه را به تلفظ فارسی «z.k.r» نوشته (فارسی‌زبانان ذ را ز می‌خوانند)؛ دقیق‌تر آن ḏ.k.r است، ولی ادعای او درست است (کلاین).\",\n ['zekr'],\n [{\"ref\":\"KLN:1766\",\"status\":\"supports\",\"note\":KLN71_Z+\" (the 1966 vol. II p.1766 is not in the truncated local KLN_1966 OCR; same entry read in the 1971 one-volume edition)\"}],\n [{\"src\":\"KLN\",\"where\":\"1966 s.v. tezkirah\",\"stance\":\"supports\",\"note\":KLN66_T},\n  {\"src\":\"FVQ\",\"where\":\"p.151 s.v. Zakariyya\",\"stance\":\"silent\",\"note\":\"Jeffery treats only the proper name, not the native verb ḏakara; grep 'dhakara' in FVQ_pages.txt gives no etymological discussion\"}]),\nn(2,\"Persian\",\"zekr\",\"confirmed\",\n \"Persian ذکر zekr 'mention; remembrance, esp. litany of God (Sufi dhikr)' is a learned loan of Arabic ذِكْر ḏikr, verbal noun of ḏakara; Persian pronounces ḏ as z and inserts no vowel in the cluster. The listed derivatives (ذاکر ḏākir, تذکّر taḏakkur, تذکار taḏkār, تذکره taḏkira, مذاکره muḏākara, متذکّر, مذکور, اذکار) are all regular Arabic patterns of the same root borrowed into Persian.\",\n \"«ذکر» (zekr) وام‌واژه‌ای از عربی ذِکْر ḏikr، مصدرِ ذَکَرَ «یاد کرد» است و در فارسی به معنای «یاد، بر زبان آوردن، و به‌ویژه ذکرِ خدا در تصوف» به کار می‌رود؛ فارسی‌زبانان ذ عربی را ز تلفظ می‌کنند. ذاکر، تذکّر، تذکار، تذکره، مذاکره، متذکّر، مذکور و اذکار همه ساخت‌های قیاسی عربی از همین ریشه‌اند که به فارسی راه یافته‌اند. ادعای نورایی درست است (ویکی‌واژه، کلاین).\",\n ['zekr','mzekr'],\n [NC(\"FVA:150\",\"Nahvi, Farhang-e vazheha-ye Arabi: no digital copy (refs_online.json)\")],\n [{\"src\":\"WIKT\",\"where\":\"ذکر (Persian)\",\"stance\":\"supports\",\"note\":\"'Borrowed from Arabic ذِكْر (ḏikr)'\"},\n  {\"src\":\"MON\",\"where\":\"vajehyab moein/ذکر\",\"stance\":\"partial\",\"note\":\"the page returned is the homograph ذَکَر 'male, penis' tagged '[ ع . ]' — confirms Arabic origin of the spelling, not the zekr sense; MON_part1.txt l.65002 has 'ذاکر ... قوه‌ای در انسان که حوادث ...' (Arabic derivative in use)\"},\n  {\"src\":\"KLN\",\"where\":\"1966 s.v. tezkirah\",\"stance\":\"supports\",\"note\":KLN66_T+\" — the same Arabic root behind Persian tazkere/tazkira\"}]),\nn(3,\"Hebrew\",\"zâkar; zekhar-yâh\",\"confirmed\",\n \"Biblical Hebrew זָכַר zāḵar 'he remembered' (root z-k-r < Proto-Semitic *ḏ-k-r), and the theophoric name זְכַרְיָה Zəḵaryāh / זְכַרְיָהוּ Zəḵaryāhû 'YHWH has remembered' = zāḵar + -yāh (short form of the divine name). Nourai's gloss 'God has (is) remembered' is loose: the name means 'Yah has remembered', with God as subject.\",\n \"عبری کتاب مقدس זָכַר zāḵar «به یاد آورد» از ریشهٔ z-k-r (سامی آغازین *ḏ-k-r) است، و نام זְכַרְיָה Zəḵaryāh از zāḵar و -yāh (کوتاه‌شدهٔ نام خدا، یهوه) ساخته شده و معنایش «یهوه به یاد آورده است» است. ترجمهٔ نورایی «خدا به یاد آورده شده» دقیق نیست (خدا فاعل است نه مفعول)، ولی ریشه‌شناسی درست است (کلاین، ویکی‌واژه).\",\n ['zach','zakar'],\n [{\"ref\":\"KLN:1766\",\"status\":\"supports\",\"note\":KLN71_Z}],\n [{\"src\":\"KLN\",\"where\":\"1966 s.v. tezkirah\",\"stance\":\"supports\",\"note\":\"'Heb. zakhar, he remembered, zekher, remembrance, memorial, zikkaron'\"},\n  {\"src\":\"FVQ\",\"where\":\"p.151\",\"stance\":\"supports\",\"note\":\"Jeffery glosses Zakariyya as 'Zachariah' and derives it from the Biblical name via Syriac\"}]),\nn(4,\"Arabic\",\"Zakarîa\",\"confirmed\",\n \"Qur'anic Arabic زَكَرِيَّا Zakariyyāʾ (variants زكريّاء, زكرى), the father of John the Baptist (Q 3:37-38, 19:2-7). Jeffery (FVQ 151, after Rhodokanakis, Horovitz, Mingana) holds that it most probably came into Arabic from Syriac ܙܟܪܝܐ Zḵaryā (itself from Hebrew Zəḵaryāh), the -iyyā ending matching the Syriac; the early Arab philologists (al-Jawālīqī) already marked it as foreign. Nourai's NOTE ('not quite clear through what language') reflects Jeffery's hedging; modern opinion (Wiktionary's tree Hebrew → Classical Syriac → Arabic) favours Syriac transmission.\",\n \"«زکریّا» در عربی قرآنی (زَکَرِیّا، با گونه‌های زکریّاء و زکری) نام پدر یحیی است. جفری (واژه‌های دخیل قرآن، ص ۱۵۱) آن را به احتمال زیاد وام‌گرفته از سریانی Zḵaryā می‌داند که خود از عبری Zəḵaryāh است؛ لغویان کهن عرب (جوالیقی، المعرّب) نیز آن را بیگانه شمرده‌اند. یادداشت نورایی که «روشن نیست از چه زبانی به عربی رسیده» تردید جفری را بازمی‌تاباند؛ پژوهش امروزی (ویکی‌واژه) راه عبری ← سریانی ← عربی را ترجیح می‌دهد. ادعای اصلی نورایی (عبری ← عربی) درست است.\",\n ['zakar','zakfa'],\n [{\"ref\":\"VDQ:233\",\"status\":\"not_checked\",\"note\":\"noorlib viewer is JavaScript-only; VDQ is Badreh'i's Persian translation of FVQ, so the substance was checked in FVQ instead\"}],\n [{\"src\":\"FVQ\",\"where\":\"p.151 s.v. Zakariyya\",\"stance\":\"supports\",\"note\":FVQ_Z},\n  {\"src\":\"KLN\",\"where\":\"1971 s.v. Zachariah\",\"stance\":\"silent\",\"note\":\"Klein lists Arab. dhakara as cognate of the verb but does not treat the Arabic name\"},\n  {\"src\":\"AFM\",\"where\":\"grep 'زكريا' AFM_pages.txt\",\"stance\":\"silent\",\"note\":\"no entry (Addi Shir lists Persian loans, not Hebrew/Syriac names)\"}]),\nn(5,\"Persian\",\"Zakarîya\",\"confirmed\",\n \"Persian زکریا Zakariyyā (colloquially Zakariyā) is taken over from Arabic Zakariyyāʾ with Islam, as the Qur'anic name of the prophet; the Arabic final hamza is dropped as usual in Persian. Gloss 'God is remembered' see node 3 (properly 'Yah has remembered').\",\n \"«زکریّا» در فارسی از عربی زکریّاء (نام پیامبر در قرآن) همراه با اسلام وام گرفته شده و همزهٔ پایانی عربی، چنان‌که معمول است، در فارسی افتاده است. ادعای نورایی درست است؛ تنها معنای «خدا به یاد آورده شده» را باید «یهوه به یاد آورده است» خواند (ویکی‌واژه).\",\n ['zakfa'],\n [NC(\"(none)\",\"node carries no reference\")],\n [{\"src\":\"WIKT\",\"where\":\"زکریا (Persian)\",\"stance\":\"supports\",\"note\":\"etymology tree 'Biblical Hebrew זְכַרְיָה → Classical Syriac ܙܟ݂ܪܝܐ (bor.) → Arabic زَكَرِيَّا (bor.) → Persian زکریا'; 'Borrowed from Arabic زَكَرِيَّا (zakariyyā)'\"},\n  {\"src\":\"MON\",\"where\":\"vajehyab moein/زکریا\",\"stance\":\"silent\",\"note\":\"page returned no Mo'in lexicon entry (proper names are in the a'lam volumes, not online)\"},\n  {\"src\":\"FVQ\",\"where\":\"p.151\",\"stance\":\"supports\",\"note\":\"the Arabic name Persian took over: 'Zakariyya ... Zachariah'\"}]),\nn(6,\"Greek\",\"zakaris\",\"transcription_suspect\",\n \"The Septuagint/New Testament Greek form is Ζαχαρίας Zakharías (Luke 1:5), transcribing Hebrew Zəḵaryāh with χ for the spirant ḵ and the Greek masculine -ías ending. The book prints 'zakaris' (checked on the page image): this is Nourai's misprint for Zakharias; the extraction is faithful. The derivation Hebrew → Greek itself is correct.\",\n \"صورت یونانی این نام در ترجمهٔ هفتادی و انجیل لوقا Ζαχαρίας (Zakharías) است که عبری Zəḵaryāh را با χ (برای خ نرم عبری) و پسوند مذکر -ías برگردانده است. کتاب «zakaris» چاپ کرده (در تصویر صفحه دیده شد)؛ این خطای چاپی کتاب است و درست آن Zakharias است؛ استخراج داده درست است. خود راه عبری ← یونانی درست است (کلاین، ویکی‌واژه).\",\n ['gr','zach'],\n [{\"ref\":\"KLN:1766\",\"status\":\"supports\",\"note\":\"Klein 1971 s.v. Zachariah: 'Late L. Zacharias, fr. Gk. [Zacharias], fr. Heb. Zekharyah' — the Greek form is Zacharias, not 'zakaris'\"}],\n [{\"src\":\"WIKT\",\"where\":\"Ζαχαρίας\",\"stance\":\"supports\",\"note\":\"'From Hebrew זְכַרְיָה (zəḵaryā)'\"},\n  {\"src\":\"SKT\",\"where\":\"grep 'Zachar' SKT.txt / SKT_dli_revised.txt\",\"stance\":\"silent\",\"note\":\"no entry\"}],\n error_in=\"book\",book_prints=\"zakaris\",correct_form=\"Zakharías (Ζαχαρίας)\"),\nn(7,\"Latin\",\"zacharias\",\"confirmed\",\n \"Late (Church) Latin Zacharias, the Vulgate rendering of Greek Zakharías, with ch for Greek χ; second-declension/first-declension masculine -ās as in other Greek names (Matthias, Elias).\",\n \"لاتینی متأخر (کلیسایی) Zacharias، برگردان ولگاتا از یونانی Zakharías است که χ یونانی را با ch نوشته است. ادعای نورایی درست است (کلاین).\",\n ['zach'],\n [{\"ref\":\"KLN\",\"status\":\"supports\",\"note\":\"Klein 1971 s.v. Zachariah: 'Late L. Zacharias, fr. Gk.'\"}],\n [{\"src\":\"WIKT\",\"where\":\"Zachariah\",\"stance\":\"supports\",\"note\":\"'under influence from Latin Zacharias and Koine Greek Ζαχαρίας'\"},\n  {\"src\":\"SKT\",\"where\":\"grep 'Zachar'\",\"stance\":\"silent\",\"note\":\"no entry in Skeat\"}]),\nn(8,\"English\",\"Zachary, Zacharias, Zachariah\",\"confirmed\",\n \"English Zacharias is the Latin form (Wyclif/Douay usage); Zachariah follows the Hebrew-based spelling of the Authorized Version (-iah for -yāh, cf. Jeremiah); Zachary is the vernacular form through Old French Zacharie / Middle English Zacharie with loss of the Latin ending. All three are doublets of the same Hebrew name.\",\n \"در انگلیسی Zacharias صورت لاتینی است، Zachariah از املای نزدیک به عبری در ترجمهٔ رسمی کتاب مقدس (مانند Jeremiah) می‌آید، و Zachary صورت عامیانه از راه فرانسوی کهن و انگلیسی میانه Zacharie است. هر سه دوگانه‌های یک نام عبری‌اند؛ ادعای نورایی درست است (کلاین، ویکی‌واژه).\",\n ['zach'],\n [{\"ref\":\"AHD\",\"status\":\"not_found\",\"note\":\"AHD_watkins1985.txt is the IE-roots appendix; grep 'Zachar' finds nothing (Semitic names are not covered there)\"},\n  {\"ref\":\"KLN:1766\",\"status\":\"supports\",\"note\":\"Klein 1971 l.270220: 'Zachariah, Zacharias, Zachary, masc. PN. (Bible). — Late L. Zacharias, fr. Gk., fr. Heb.'\"}],\n [{\"src\":\"KLN\",\"where\":\"1971 s.v. Zachariah\",\"stance\":\"supports\",\"note\":KLN71_Z},\n  {\"src\":\"WIKT\",\"where\":\"Zachariah\",\"stance\":\"supports\",\"note\":\"'From Hebrew זְכַרְיָה (Zəḵaryā, Yahweh has remembered) under influence from Latin Zacharias and Koine Greek Ζαχαρίας. Doublet of Zach, Zachary, Zacharias, Zechariah'\"},\n  {\"src\":\"SKT\",\"where\":\"grep 'Zachar' SKT*.txt\",\"stance\":\"silent\",\"note\":\"no entry\"}]),\n]\n\ne1_nodes=[\nn(1,\"Arabic\",\"zînâ; abŭ-zînâ\",\"plausible\",\n \"zinā: Arabic زِنًا / زِناء zinan, zināʾ 'fornication, adultery', verbal noun of zanā (root z-n-y) — confirmed. abū zinā: Lokotsch (556) explains Turkish ebuzine/buzine 'monkey' from Arabic abū zinā 'father of fornication'; Arabic and Persian lexicography does record monkey kunyas such as أبو زنة abū zina (Dehkhoda citing al-Muraṣṣaʿ: ابوزنه, ابوقشه, ابوقیس...), but with zina, not zinā, and that kunya is best seen as an Arabic reshaping of the Persian word būzīna (see node 3). The gloss 'referring to gibbons' is too narrow: the word means 'monkey' in general.\",\n \"«زنا» در عربی (زِنًا / زِناء) مصدرِ زَنی «زنا کرد» از ریشهٔ ز-ن-ی است و درست است. اما «ابوزنا» («پدر زنا») را لوکوچ برای توضیح ترکی ebuzine «میمون» آورده است؛ در فرهنگ‌های عربی و فارسی کنیه‌هایی چون «ابوزنه» برای میمون آمده (دهخدا به نقل از المرصّع)، ولی با zina نه zinā، و به احتمال زیاد این کنیه خود عربی‌شدهٔ واژهٔ فارسی «بوزینه» است (ریشه‌شناسی عامیانه). معنای «گیبون» هم تنگ است؛ واژه یعنی «میمون» به‌طور کلی. پس بخش نخست درست و بخش دوم تنها با احتیاط پذیرفتنی است.\",\n ['zina','dkh','buz'],\n [{\"ref\":\"LKT:44\",\"status\":\"supports\",\"note\":LKT_556}],\n [{\"src\":\"SYN\",\"where\":\"p.188, 3.76 MONKEY\",\"stance\":\"partial\",\"note\":SYN_188},\n  {\"src\":\"DKH\",\"where\":\"vajehyab dehkhoda/بوزینه\",\"stance\":\"partial\",\"note\":DKH_BUZ},\n  {\"src\":\"AFM\",\"where\":\"grep 'بوزنة|ابوزنة' AFM_pages.txt\",\"stance\":\"silent\",\"note\":\"no entry for the monkey kunya\"},\n  {\"src\":\"FVQ\",\"where\":\"grep 'zina' FVQ_pages.txt\",\"stance\":\"silent\",\"note\":\"zanā is native Arabic, not treated by Jeffery\"}]),\nn(2,\"Persian\",\"zenâ\",\"confirmed\",\n \"Persian زنا zenā (also زناء) 'adultery, fornication' is a loan of Arabic zinan / zināʾ, used since Classical Persian (Rumi's Masnavi verse quoted in the chart); Persian drops the final hamza/tanwin and has short e for Arabic i. Derivatives zenākār, zenākāri are Persian compounds with -kār.\",\n \"«زنا» (zenâ، نیز زناء) در فارسی وام‌واژه از عربی زِنًا / زِناء است و از دورهٔ فارسی کلاسیک (چنان‌که در بیت مثنوی آمده) به کار رفته؛ همزهٔ پایانی و تنوین عربی در فارسی افتاده است. «زناکار» و «زناکاری» ترکیب‌های فارسی با پسوند -کار هستند. ادعای نورایی درست است (معین، ویکی‌واژه).\",\n ['zina'],\n [NC(\"MON:602\",\"6-vol. Mo'in page cannot be mapped online; the vajehyab moein/زنا page returned no lexicon text\"),NC(\"FVA:180\",\"Nahvi: no digital copy\")],\n [{\"src\":\"MON\",\"where\":\"MON_part2.txt l.7395, l.4041\",\"stance\":\"supports\",\"note\":\"'... زناکاری. (اِ.) کار بد، گناه. زنا. فسق و فجور'; 'زناکار ج. فاجرین ...' — zenā used in Mo'in definitions of Arabic words\"},\n  {\"src\":\"WIKT\",\"where\":\"زنا (Arabic)\",\"stance\":\"supports\",\"note\":\"'زِنًا (zinan) m (construct state زِنَا zinā) ... alternative form of زِنَاء (zināʔ)'\"}]),\nn(3,\"Persian\",\"bŭzîneh\",\"disputed\",\n \"Persian بوزینه būzīna (also بوزنه būzna, بوزنینه) 'monkey', attested early (old Qur'an commentary, Kalila-va-Dimna, Rumi). Nourai follows the traditional lexicographers (Ghiyāth, Ānandrāj: 'بوزینه مخفف ابوزینه') and Lokotsch in taking it from Arabic abū zinā 'father of fornication'. Modern scholarship treats it as a native Iranian word: Wiktionary (Persian) 'inherited from Proto-Iranian; compare Pashto bízo monkey', with Mo'in giving no Arabic tag; the Arabic kunya abū zina is then a folk-etymological Arabization of the Persian word, not its source. Gloss 'gibbon' is also too narrow ('monkey').\",\n \"«بوزینه» (بوزنه، بوزنینه) به معنای «میمون» از کهن‌ترین متن‌های فارسی (تفسیرهای کهن قرآن، کلیله و دمنه، مثنوی) آمده است. نورایی به پیروی از فرهنگ‌نویسان قدیم (غیاث و آنندراج: «بوزینه مخفف ابوزینه») و لوکوچ آن را از عربی «ابوزنا» («پدر زنا») می‌داند. پژوهش امروزی آن را واژه‌ای ایرانی می‌شمارد (ویکی‌واژه: بازمانده از ایرانی آغازین، هم‌ریشه با پشتو bízo «میمون»)، و معین نیز نشانهٔ عربی [ع.] به آن نداده است؛ بنابراین کنیهٔ عربی «ابوزنه» ریشه‌شناسی عامیانه و عربی‌شدهٔ همین واژهٔ فارسی است، نه سرچشمهٔ آن. ادعای نورایی را پژوهش امروزی رد می‌کند.\",\n ['buz','dkh','mbuz','ru'],\n [{\"ref\":\"MON:602\",\"status\":\"partial\",\"note\":MON_BUZ+\" — Mo'in has the word but does not mark it Arabic\"},NC(\"FVA:180\",\"Nahvi: no digital copy\")],\n [{\"src\":\"HUB\",\"where\":\"p.87 and p.97\",\"stance\":\"partial\",\"note\":HUB_87},\n  {\"src\":\"MON\",\"where\":\"vajehyab moein/بوزینه; MON_part1.txt l.26095\",\"stance\":\"contradicts\",\"note\":MON_BUZ},\n  {\"src\":\"DKH\",\"where\":\"vajehyab dehkhoda/بوزینه\",\"stance\":\"supports\",\"note\":DKH_BUZ},\n  {\"src\":\"HRN\",\"where\":\"grep 'buzin|būzīn|buzna' HRN.txt\",\"stance\":\"silent\",\"note\":\"no entry in Horn\"},\n  {\"src\":\"BQT\",\"where\":\"grep 'بوزینه' BQT_v1_pages.txt\",\"stance\":\"silent\",\"note\":\"OCR has the word only in running text ('میمون است که بوزینه باشد', l.22116); headword/footnote not legible in OCR, page not identified\"},\n  {\"src\":\"ARY\",\"where\":\"grep 'بوزینه' ARY_pages.txt\",\"stance\":\"silent\",\"note\":\"no entry\"},\n  {\"src\":\"LKT\",\"where\":\"p.44 no.556\",\"stance\":\"supports\",\"note\":LKT_556}]),\nn(4,\"Hindustani\",\"bojîna\",\"plausible\",\n \"Hindustani (Urdu/Hindi) has بوزنہ būzna / būzīna 'monkey' borrowed from Persian būzīna in the Mughal period, with Persian z kept (z → j is the usual nativized Hindi treatment of Perso-Arabic z, which makes a 'bojīna' variant possible). I could not find 'bojîna' itself in an accessible source; Nourai cites Partridge (PRT:253), which is lending-only. The existence of the Persian loan in Hindustani is unproblematic; its being the source of 'gibbon' is not (nodes 5-6).\",\n \"در هندوستانی (اردو/هندی) واژهٔ بوزنه (būzna/būzīna) «میمون» از فارسی «بوزینه» در دورهٔ گورکانیان وام گرفته شده است؛ تبدیل ز به ج در هندی عامیانه رایج است و صورت «بوجینا» را ممکن می‌کند، ولی من این صورت را در منبعی دسترس‌پذیر نیافتم (پارتریج، مرجع نورایی، در دسترس نیست). وجود این وام‌واژه پذیرفتنی است، اما اینکه سرچشمهٔ «gibbon» باشد پذیرفته نیست (گره‌های ۵ و ۶).\",\n ['buz'],\n [NC(\"PRT:253\",\"Partridge, Origins: archive.org lending-only (refs_online.json)\")],\n [{\"src\":\"HJB\",\"where\":\"grep 'gibbon|buzna|bozina' HJB.txt\",\"stance\":\"silent\",\"note\":\"Hobson-Jobson mentions gibbons only s.v. HOOLOCK ('The black gibbon (Hylobates hoolock)'), no buzna/bojina and no entry gibbon\"},\n  {\"src\":\"KLN\",\"where\":\"1966 s.v. gibbon\",\"stance\":\"partial\",\"note\":KLN_GIB},\n  {\"src\":\"AID\",\"where\":\"grep 'gibbon|bozin|buzin' AID.txt\",\"stance\":\"silent\",\"note\":\"no entry\"}]),\nn(5,\"French\",\"\",\"disputed\",\n \"French gibbon was introduced by Buffon (Histoire naturelle, 1766) for an ape brought from French India, reportedly by Dupleix (governor 1742-54) — so Nourai's NOTE ('brought to France from India in the early 18th century') is roughly right about the route but early by a few decades. The source word is unknown: Klein only says 'a name of Indian origin', Skeat 'of unknown origin', and Wiktionary now suggests a Northern Aslian (Malay-peninsula) word, cf. Batek kəboɲ. No source derives it from Hindustani būzna/Persian būzīna, and phonetically b-z-n → g-b-n is not a regular correspondence.\",\n \"واژهٔ فرانسوی gibbon را بوفون (تاریخ طبیعی، ۱۷۶۶) برای میمونی که از هند فرانسه (به روایتی به دست دوپلکس، فرماندار ۱۷۴۲–۱۷۵۴) آورده شده بود به کار برد؛ پس یادداشت نورایی دربارهٔ راه انتقال کمابیش درست است ولی تاریخ «اوایل سدهٔ ۱۸» چند دهه زود است. اصل واژه ناشناخته است: کلاین فقط «نامی هندی»، اسکیت «اصل ناشناخته» و ویکی‌واژه واژه‌ای از زبان‌های اَسلیایی شبه‌جزیرهٔ مالایا (مانند Batek kəboɲ) را پیشنهاد می‌کند. هیچ منبعی آن را از «بوزینه» نمی‌داند و تبدیل b-z-n به g-b-n قاعده‌مند نیست؛ پژوهش امروزی ادعای نورایی را نمی‌پذیرد.\",\n ['gib'],\n [{\"ref\":\"KLN:655\",\"status\":\"partial\",\"note\":KLN_GIB}],\n [{\"src\":\"SKT\",\"where\":\"SKT_dli_revised.txt l.31682\",\"stance\":\"contradicts\",\"note\":\"'Gibbon, a kind of ape. (F.) F. gibbon, in Buffon; of unknown origin.'\"},\n  {\"src\":\"FSD\",\"where\":\"vol.2 l.31759 s.v. gibbon\",\"stance\":\"silent\",\"note\":\"describes 'white-handed gibbon (Hylobates lar)'; etymology not legible in OCR\"},\n  {\"src\":\"WIKT\",\"where\":\"gibbon (French)\",\"stance\":\"contradicts\",\"note\":WK_GIB}]),\nn(6,\"English\",\"gibbon\",\"disputed\",\n \"English gibbon (first recorded 1770, in translations of Buffon) is from French gibbon; that last link is secure. The deeper derivation from Hindustani/Persian būzīna and Arabic abū zinā drawn by Nourai is not supported by any source consulted (origin unknown, possibly Aslian; see node 5).\",\n \"انگلیسی gibbon (نخستین کاربرد حدود ۱۷۷۰ در ترجمه‌های بوفون) از فرانسوی gibbon است و این حلقه استوار است؛ اما پیوند آن با «بوزینه» و «ابوزنا» که نورایی کشیده در هیچ‌یک از منابع دیده نمی‌شود (اصل واژه ناشناخته، شاید اسلیایی). پژوهش امروزی این ادعا را رد می‌کند.\",\n ['gib'],\n [{\"ref\":\"KLN:655\",\"status\":\"partial\",\"note\":KLN_GIB+\" — supports French → English, not the Persian source\"}],\n [{\"src\":\"SKT\",\"where\":\"SKT_dli_revised.txt l.31682\",\"stance\":\"contradicts\",\"note\":\"'F. gibbon, in Buffon; of unknown origin'\"},\n  {\"src\":\"WEB\",\"where\":\"WEB_vol1.txt\",\"stance\":\"silent\",\"note\":\"vol. 1 only covers A–?; 'gibbon' appears only in other definitions (anthropoid, hoolock)\"},\n  {\"src\":\"WIKT\",\"where\":\"gibbon (English)\",\"stance\":\"contradicts\",\"note\":WK_GIB}]),\nn(7,\"Turkish\",\"ebuzine\",\"plausible\",\n \"Ottoman Turkish ebuzine (ابوزینه), also buzine, 'monkey' (not specifically 'gibbon'), the source of Old Russian obezĭjana > Russian obez'jana (Lokotsch 556; Buck 3.76). The Turkish form with ebu- shows the word was reinterpreted as an Arabic kunya abū-...; Lokotsch derives it from Arabic abū zinā, whereas modern opinion (Wiktionary s.v. обезьяна: 'borrowed from Persian ابوزینه (abuzina), بوزینه (buzina)') makes Persian the immediate (and ultimate) source. So the edge exists, but the parent is better Persian (a)būzīna than Arabic.\",\n \"ترکی عثمانی ebuzine (ابوزینه، نیز buzine) به معنای «میمون» (نه فقط گیبون) سرچشمهٔ روسی کهن obezĭjana و روسی امروزی obez'jana است (لوکوچ ۵۵۶؛ باک ۳٫۷۶). پیشوند ebu- نشان می‌دهد که ترکان واژه را کنیه‌ای عربی (ابو...) پنداشته‌اند. لوکوچ آن را از عربی «ابوزنا» می‌داند، ولی پژوهش امروزی (ویکی‌واژه زیر обезьяна) آن را از فارسی «ابوزینه / بوزینه» می‌گیرد؛ پس پیوند ترکی درست است ولی مادرِ آن بهتر است فارسی دانسته شود. با احتیاط پذیرفتنی است.\",\n ['ru','buz'],\n [{\"ref\":\"SYN:188\",\"status\":\"supports\",\"note\":SYN_188}],\n [{\"src\":\"LKT\",\"where\":\"p.44 no.556\",\"stance\":\"supports\",\"note\":LKT_556},\n  {\"src\":\"TTS\",\"where\":\"grep 'buzin|ebuzin' incoming/TTS/*.txt\",\"stance\":\"silent\",\"note\":\"no match in Vámbéry's (Turkic roots) dictionary\"},\n  {\"src\":\"WIKT\",\"where\":\"обезьяна (Russian)\",\"stance\":\"partial\",\"note\":\"'Inherited from Old East Slavic обезьꙗна, обозьꙗна, further borrowed from Persian ابوزینه (abuzina), بوزینه (buzina, simian)'\"}]),\n]\n\nout={\"pdf_page\":571,\"book_page\":541,\"verified_by\":\"claude-opus-5.5\",\"verified_on\":\"2026-10-16\",\"entries\":[\n {\"entry\":0,\"root\":\"Z.k.r\",\"verdict\":\"confirmed\",\"modern_form\":\"Proto-Semitic *ḏ-k-r 'to remember, mention' (Heb. z-k-r, Ar. ḏ-k-r, Aram. d-k-r, Akk. zakāru)\",\n  \"note\":\"Root, label and gloss correct. Strictly the Proto-Semitic root has *ḏ (Arabic ذ), which Hebrew/Akkadian render z and Aramaic d; Nourai's 'Z.k.r' follows Hebrew and the Persian reading of ذ. Greek node 'zakaris' is a misprint in the book for Zakharias.\",\n  \"note_fa\":\"ریشهٔ سامی آغازین *ḏ-k-r «یاد کردن، بر زبان آوردن» است که در عبری و اکدی با ز (zāḵar، zakāru)، در آرامی با د (dəḵar) و در عربی با ذ (ذَکَرَ) آمده است. نورایی ریشه را «Z.k.r» نوشته که با صورت عبری و تلفظ فارسیِ ذ سازگار است؛ ادعای او درست است (کلاین). صورت یونانی «zakaris» در کتاب خطای چاپی برای Zakharias است.\",\n  \"sources\":[W['zach'],W['zekr']],\n  \"ref_check\":[{\"ref\":\"KLN:1766\",\"status\":\"supports\",\"note\":KLN71_Z}],\n  \"consulted\":[{\"src\":\"KLN\",\"where\":\"1966 s.v. tezkirah\",\"stance\":\"supports\",\"note\":KLN66_T},\n               {\"src\":\"FVQ\",\"where\":\"p.151\",\"stance\":\"partial\",\"note\":\"Jeffery treats the name Zakariyya only\"}],\n  \"nodes\":e0_nodes},\n {\"entry\":1,\"root\":\"Z.n.y\",\"verdict\":\"confirmed\",\"modern_form\":\"Arabic ز-ن-ي zanā (yaznī) 'to commit adultery/fornication', verbal noun zinan / zināʾ\",\n  \"note\":\"Root and gloss correct. The second branch (bozine → Hindustani → French/English gibbon) is the weak part: Persian būzīna is today regarded as a native Iranian word (cf. Pashto bízo), the Arabic kunya 'abū zina' being folk etymology, and 'gibbon' is of unknown (perhaps Aslian) origin. The gloss 'gibbon' for bozine/ebuzine should be 'monkey'.\",\n  \"note_fa\":\"ریشهٔ عربی ز-ن-ی (زَنی یَزنی «زنا کرد»، مصدر زِنًا / زِناء) و معنای آن درست است. اما شاخهٔ دوم نمودار سست است: «بوزینه» را پژوهش امروزی واژه‌ای ایرانی (هم‌ریشه با پشتو bízo) می‌داند و کنیهٔ «ابوزنه» ریشه‌شناسی عامیانه است؛ انگلیسی/فرانسوی gibbon نیز اصلی ناشناخته (شاید اسلیایی) دارد. معنای «گیبون» برای بوزینه و ebuzine هم باید «میمون» باشد.\",\n  \"sources\":[W['zina'],W['buz']],\n  \"ref_check\":[NC(\"FVA:180\",\"Nahvi: no digital copy\")],\n  \"consulted\":[{\"src\":\"MON\",\"where\":\"MON_part2.txt l.7395\",\"stance\":\"supports\",\"note\":\"'زناکاری ... زنا. فسق و فجور' — Arabic zinā in Persian use\"},\n               {\"src\":\"WIKT\",\"where\":\"زنا (Arabic)\",\"stance\":\"supports\",\"note\":\"'زِنًا (zinan) ... alternative form of زِنَاء (zināʔ)'\"}],\n  \"nodes\":e1_nodes}]}\njson.dump(out,open('/home/sfmqrb/git/rishe-private/data/verification/page-571.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)\nEOF\ncd /home/sfmqrb/git/rishe-private && python3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-571.py && python3 -m json.tool data/verification/page-571.json >/dev/null && python3 tools/verify_check.py 571",
 "description": "Build page-571 JSON and run checker"
}
```


### [2026-10-17T00:35:56.568Z] TOOL RESULT

```
nodes verified: 15/15
node verdicts: {'confirmed': 8, 'transcription_suspect': 1, 'plausible': 3, 'disputed': 3}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 7, 'not_checked': 7, 'not_found': 1, 'partial': 3}
books consulted: {'supports': 17, 'silent': 17, 'partial': 6, 'contradicts': 5} | by book: {'WIKT': 9, 'KLN': 6, 'FVQ': 5, 'SKT': 5, 'MON': 4, 'AFM': 2, 'DKH': 2, 'LKT': 2, 'SYN': 1, 'HUB': 1, 'HRN': 1, 'BQT': 1, 'ARY': 1, 'HJB': 1, 'AID': 1, 'FSD': 1, 'WEB': 1, 'TTS': 1}
```


## [2026-10-17T00:36:05.989Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; command ls incoming/TTS; grep -i -c -E 'buzin|ebuzin|bozin' incoming/TTS/* AID.txt 2>&1; grep -c -E 'بوزینه|بوزنه' incoming/ARY/ARY_pages.txt; grep -c -E 'زكريا|زکریا|بوزنة|ابوزنة' AFM_pages.txt; grep -c -i 'Zachar' SKT.txt SKT_dli_revised.txt",
 "description": "Confirm silent greps"
}
```


### [2026-10-17T00:36:06.542Z] TOOL RESULT

```
TTS_pages.txt
TTS_vambery1878_uoft_djvu.txt
TTS_vambery1878_uoft.pdf
incoming/TTS/TTS_pages.txt:0
incoming/TTS/TTS_vambery1878_uoft_djvu.txt:0
AID.txt:0
0
0
SKT.txt:0
SKT_dli_revised.txt:0
```


## [2026-10-17T00:36:18.039Z] TOOL CALL #33: SubagentHandback

```json
{
 "message": "Page 571 (book page 541) is verified. I wrote `/home/sfmqrb/git/rishe-private/data/verification/page-571.json`, and `verify_check.py 571` reports 0 PROBLEM lines.\n\n**Counts:** 2 roots, both confirmed (Z.k.r and Z.n.y). 15 nodes: 8 confirmed, 3 plausible, 3 disputed, 1 transcription_suspect.\n\n**Disputed:**\n- Z.n.y #3, Persian bozine «بوزینه»: Nourai takes it from Arabic abū zinā \"father of fornication\", as do Lokotsch and the old Persian dictionaries Ghiyath and Anandraj. Wiktionary instead treats it as an inherited Iranian word (cf. Pashto bízo \"monkey\"), and Mo'in gives it no Arabic tag. On that view the Arabic monkey nickname «ابوزنه» is a folk-etymology reshaping of the Persian word, not its source.\n- Z.n.y #5, French gibbon: Skeat says \"of unknown origin\", Klein only \"a name of Indian origin\", and Wiktionary suggests an Aslian word (Batek kəboɲ). No source derives it from Hindustani or Persian būzīna.\n- Z.n.y #6, English gibbon: the French → English step is sound, but the deeper Persian/Arabic origin Nourai draws has no support.\n\n**Transcription suspect:**\n- Z.k.r #6, Greek \"zakaris\": the printed page really shows \"zakaris\", so this is the author's misprint for Zakharías (Ζαχαρίας), not an extraction error. I copied the page image to `data/verification/sources/refs/ocr/BOOK/571.png`.\n\n**Plausible (with caveats):**\n- Z.n.y #1: zinā is fine, but abū-zinā as the source of the monkey word is shaky.\n- Z.n.y #4: the form \"bojîna\" is unattested in any source I could reach.\n- Z.n.y #7: Turkish ebuzine is better derived from Persian (a)būzīna than from Arabic.\n- The gloss \"gibbon\" should be \"monkey\" throughout the Z.n.y chart.\n\n**Smaller notes:**\n- The chart writes the Arabic root as z.k.r; strictly it is ḏ.k.r (ذ), which Persian pronounces as z.\n- Nourai's gloss for the Hebrew name, \"God is remembered\", should be \"Yah has remembered\", with God as the subject.\n\n**Extraction errors:** none; the JSON matches the printed page.\n\n**References I could not check:** FVA (no digital copy), PRT (lending-only), VDQ (its online viewer needs a browser; checked through Jeffery's FVQ p.151 instead) and MON:602 (6-volume page numbers can't be mapped online). The Klein entries were read in the local 1971 edition, because the local OCR of the 1966 edition stops partway through V."
}
```


### [2026-10-17T00:36:18.352Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
