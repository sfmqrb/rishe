# Verification process log — verify-page-552


## [2026-10-17T00:00:15.661Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 552 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-552.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-552.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-552.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 552` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-17T00:00:15.735Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-17T00:00:18.375Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-17T00:00:18.473Z] TOOL RESULT

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


## [2026-10-17T00:00:18.876Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-552.txt"
}
```


### [2026-10-17T00:00:18.973Z] TOOL RESULT

```
1	=== PDF page 552 (book page 522) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Wes 5, Wes-no, Wesn, Veso, Věno, Vesno : Wes 5: to buy; Wes-no: buying price, value; Wesn: sell  (refs POK:1173; OEW:440; AEF:302)
4	#1 (parent #0) [Pahlavi] refs=AEF:302 | vah-âk : value
5	  #2 (parent #1) [Persian] refs=AEF:302; FSF:91 | bahâ «بها» : value ; bahâ-gîr «بهاگیر» : valuable
6	#3 (parent #0) [Latin] refs=AHD:1550; OEW:440 | věnum : sale ; ven-dere : to sell
7	  #4 (parent #3) [English] refs=OEW:440 | vend, vendor
8	--- entry 1 ---
9	ROOT Wesâ -> redirect to Wes 1
10	--- entry 2 ---
11	ROOT Wesn -> redirect to Wes 5
12	--- entry 3 ---
13	ROOT Wes-no -> redirect to Wes 5
14	--- entry 4 ---
15	ROOT We-spero -> redirect to Au 2
16	--- entry 5 ---
17	ROOT Wesr -> redirect to Aus 2
18	--- entry 6 ---
19	ROOT Wesu -> redirect to Su 1
20	--- entry 7 ---
21	ROOT [Indo-European] Wet : year, also referring to things with few years (young) or many years (old)  (refs POK:1175; OEW:441)
22	#1 (parent #0) [Iranian] refs=HRN:43 | vasa : one year old, young child
23	  #2 (parent #1) [Pahlavi] refs=HRN:43; HUB:26 | vhat-čak, cačak : one year old, child
24	    #3 (parent #2) [Persian] refs=BQT:237; HRN:26 | bačeh «بچّه» : child, baby
25	#4 (parent #0) [Sanskrit] refs=SKT:592 | vasta : young
26	#5 (parent #0) [Latin] refs=OEW:441; AHD | vitulus : having few years, young cow, calf ; vetus : having many years, old ; veterinus : old cattle
27	  #6 (parent #5) [English] refs=AHD | veal, veteran, veterinary
28	
```


## [2026-10-17T00:00:19.473Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-552.json"
}
```


### [2026-10-17T00:00:19.623Z] TOOL RESULT

```
1	{
2	  "pdf_page": 552,
3	  "book_page": 522,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Wes 5, Wes-no, Wesn, Veso, Věno, Vesno",
8	        "lang": "Indo-European",
9	        "refs": "POK:1173; OEW:440; AEF:302",
10	        "gloss": "Wes 5: to buy; Wes-no: buying price, value; Wesn: sell"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Pahlavi",
17	          "refs": "AEF:302",
18	          "words": [
19	            {"translit": "vah-âk", "gloss": "value", "script": null}
20	          ],
21	          "note": null,
22	          "quote": null
23	        },
24	        {
25	          "id": 2,
26	          "parent": 1,
27	          "lang": "Persian",
28	          "refs": "AEF:302; FSF:91",
29	          "words": [
30	            {"translit": "bahâ", "gloss": "value", "script": "بها"},
31	            {"translit": "bahâ-gîr", "gloss": "valuable", "script": "بهاگیر"}
32	          ],
33	          "note": null,
34	          "quote": {
35	            "text": "جهاندار بنشست بر تخت عاج - بیاویختند ان بهاگیر تاج",
36	            "poet": "Ferdowsî"
37	          }
38	        },
39	        {
40	          "id": 3,
41	          "parent": 0,
42	          "lang": "Latin",
43	          "refs": "AHD:1550; OEW:440",
44	          "words": [
45	            {"translit": "věnum", "gloss": "sale", "script": null},
46	            {"translit": "ven-dere", "gloss": "to sell", "script": null}
47	          ],
48	          "note": null,
49	          "quote": null
50	        },
51	        {
52	          "id": 4,
53	          "parent": 3,
54	          "lang": "English",
55	          "refs": "OEW:440",
56	          "words": [
57	            {"translit": "vend, vendor", "gloss": null, "script": null}
58	          ],
59	          "note": null,
60	          "quote": null
61	        }
62	      ]
63	    },
64	    {
65	      "root": {
66	        "name": "Wesâ",
67	        "redirect": "Wes 1"
68	      },
69	      "nodes": []
70	    },
71	    {
72	      "root": {
73	        "name": "Wesn",
74	        "redirect": "Wes 5"
75	      },
76	      "nodes": []
77	    },
78	    {
79	      "root": {
80	        "name": "Wes-no",
81	        "redirect": "Wes 5"
82	      },
83	      "nodes": []
84	    },
85	    {
86	      "root": {
87	        "name": "We-spero",
88	        "redirect": "Au 2"
89	      },
90	      "nodes": []
91	    },
92	    {
93	      "root": {
94	        "name": "Wesr",
95	        "redirect": "Aus 2"
96	      },
97	      "nodes": []
98	    },
99	    {
100	      "root": {
101	        "name": "Wesu",
102	        "redirect": "Su 1"
103	      },
104	      "nodes": []
105	    },
106	    {
107	      "root": {
108	        "name": "Wet",
109	        "lang": "Indo-European",
110	        "refs": "POK:1175; OEW:441",
111	        "gloss": "year, also referring to things with few years (young) or many years (old)"
112	      },
113	      "nodes": [
114	        {
115	          "id": 1,
116	          "parent": 0,
117	          "lang": "Iranian",
118	          "refs": "HRN:43",
119	          "words": [
120	            {"translit": "vasa", "gloss": "one year old, young child", "script": null}
121	          ],
122	          "note": null,
123	          "quote": null
124	        },
125	        {
126	          "id": 2,
127	          "parent": 1,
128	          "lang": "Pahlavi",
129	          "refs": "HRN:43; HUB:26",
130	          "words": [
131	            {"translit": "vhat-čak, cačak", "gloss": "one year old, child", "script": null}
132	          ],
133	          "note": null,
134	          "quote": null
135	        },
136	        {
137	          "id": 3,
138	          "parent": 2,
139	          "lang": "Persian",
140	          "refs": "BQT:237; HRN:26",
141	          "words": [
142	            {"translit": "bačeh", "gloss": "child, baby", "script": "بچّه"}
143	          ],
144	          "note": null,
145	          "quote": null
146	        },
147	        {
148	          "id": 4,
149	          "parent": 0,
150	          "lang": "Sanskrit",
151	          "refs": "SKT:592",
152	          "words": [
153	            {"translit": "vasta", "gloss": "young", "script": null}
154	          ],
155	          "note": null,
156	          "quote": null
157	        },
158	        {
159	          "id": 5,
160	          "parent": 0,
161	          "lang": "Latin",
162	          "refs": "OEW:441; AHD",
163	          "words": [
164	            {"translit": "vitulus", "gloss": "having few years, young cow, calf", "script": null},
165	            {"translit": "vetus", "gloss": "having many years, old", "script": null},
166	            {"translit": "veterinus", "gloss": "old cattle", "script": null}
167	          ],
168	          "note": null,
169	          "quote": null
170	        },
171	        {
172	          "id": 6,
173	          "parent": 5,
174	          "lang": "English",
175	          "refs": "AHD",
176	          "words": [
177	            {"translit": "veal, veteran, veterinary", "gloss": null, "script": null}
178	          ],
179	          "note": null,
180	          "quote": null
181	        }
182	      ]
183	    }
184	  ]
185	}
186	
```


## [2026-10-17T00:00:28.560Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; cat sources/SOURCE_MATRIX.md | head -80; python3 -c \"\nimport json;d=json.load(open('sources/refs_online.json'))\nfor k in ['POK','OEW','AEF','AHD','FSF','HRN','HUB','BQT','SKT','WLD','PHD','NYB','MON','ARY','CHEUNG','IEC','SYN','KLN','BRT']:\n  v=d.get(k);print(k, v and {x:v.get(x) for x in ['kind','local_file','page_offset','lookup_hint']})\n\"; command ls sources/refs | head -100"
}
```


### [2026-10-17T00:00:29.256Z] TOOL RESULT

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
POK {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt', 'page_offset': 'POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config"}
OEW {'kind': 'archive_restricted', 'local_file': None, 'page_offset': None, 'lookup_hint': "Borrow via IA lending (djvu.txt returns 401/403). Entries are IE roots in alphabetical order; use IA's in-book search: https://archive.org/details/originsofenglish00jose?q=<root>"}
AEF {'kind': 'catalog', 'local_file': None, 'page_offset': None, 'lookup_hint': "Not online (searched archive.org, ketabnak, noorlib, web; only bookshop listings). Because it is a translation of Horn/Hübschmann, verify AEF citations against HRN (archive.org, see Western agent's refs; local HRN.txt) and HUB (local HUB.txt): the entry order (آ–خ) follows Horn's numbering. The 2015 complete edition was retitled 'فرهنگ ریشه\u200cشناختی فارسی' (Mehrafarin), also not online."}
AHD {'kind': 'archive_djvu+website+archive_restricted', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt', 'page_offset': "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.", 'lookup_hint': "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.)."}
FSF {'kind': 'archive_djvu', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSF_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSF.txt'], 'page_offset': '484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking', 'lookup_hint': 'grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).'}
HRN {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt', 'page_offset': 'leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann."}
HUB {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt', 'page_offset': 'leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number."}
BQT {'kind': 'archive_djvu+local_scan_ocr', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'], 'page_offset': "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').", 'lookup_hint': "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)"}
SKT {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt', 'page_offset': 'leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags."}
WLD {'kind': 'archive_djvu', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'], 'page_offset': 'Band 3: leaf = printed + 6. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).', 'lookup_hint': "Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP."}
PHD {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD.txt', 'page_offset': 'leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB)."}
NYB {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol2_glossary.txt', 'page_offset': 'Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs."}
MON {'kind': 'website+archive_djvu', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'], 'page_offset': None, 'lookup_hint': "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks)."}
ARY {'kind': 'local_scan_ocr', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'], 'page_offset': 'printed page = pdf page + 1', 'lookup_hint': "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image"}
CHEUNG None
IEC {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt', 'page_offset': 'TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root."}
SYN {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt', 'page_offset': 'leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line."}
KLN {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt', 'page_offset': 'KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages."}
BRT {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BRT.txt', 'page_offset': 'Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops."}
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


## [2026-10-17T00:00:34.368Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,200p tools/verify_check.py | head -150; python3 -c \"\nimport json;d=json.load(open('data/verification/page-538.json'));print(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:5000])\""
}
```


### [2026-10-17T00:00:34.709Z] TOOL RESULT

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
{
 "entry": 0,
 "root": "Wekw, Weqw",
 "verdict": "confirmed",
 "modern_form": "PIE *wekʷ- 'to speak' (Pokorny 1135-1136 u̯ekᵘ-; LIV² 673f.; Watkins wekw-; o-grade root noun *wṓkʷs 'voice')",
 "note": "Root, label and gloss are correct: Pokorny 1135 u̯ekᵘ- 'sprechen' with Skt. vakti, vāc-, vacas-, Av. vac-, vacah-, vāxš, Gk. épos, ops, Lat. vōx, vocāre (WP I 245f.). Cheung 2007 (*u̯ač) and Wiktionary agree. The Latin/English branch and the Avestan vāč-/vacah-/uxδa- branches are textbook. The weaker parts of the chart are the Iranian compounds Nourai reconstructs or invents to reach particular New Persian words: 'paurvatâ-vac' (for pažvāk), 'hu-ni-vak' (for xonyā), Avestan 'vaxš-ô-bara' (only a reconstruction *vaxša-bara- behind MP waxšwar) and 'Old Persian wâk/wânk' (not attested). The derivation of xonyā (MP huniyāg) from *hu-ni-vāka- is opposed by the Middle Persian form, which has no -w- (see node 9). forūxtan 'sell' is linked to vac- by Justi/Horn/Mo'in, but Cheung puts it under *waxš- 'grow' (see node 4). The extraction matches the printed page (checked against site/pages/538.jpg).",
 "note_fa": "ریشهٔ هندواروپایی آغازین *wekʷ- «سخن گفتن» با بالاگونهٔ o در نام‌واژهٔ *wṓkʷs «آواز، صدا» در پوکورنی (ص ۱۱۳۵-۱۱۳۶)، والده-پوکورنی (ج ۱، ص ۲۴۵)، واتکینز و چونگ آمده است. بازمانده‌های آن سنسکریت vāc- و vacas-، اوستایی vāč- (حالت فاعلی vāxš) و vacah- «سخن»، یونانی épos و لاتینی vōx و vocāre است. ریشه و زبان و معنایی که نورایی داده درست است. ولی چند ترکیب ایرانی در این نمودار ساختهٔ خود اوست و در متن‌ها نیامده، مانند paurvatâ-vac و hu-ni-vak و vaxš-ô-bara. پیوند «خنیا» با این ریشه هم با پژوهش امروزی سازگار نیست.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wekʷ-"
 ],
 "ref_check": [
  {
   "ref": "POK:1135",
   "status": "supports",
   "note": "POK_full.txt l.90116ff. 'Root / lemma: ueḱ- (*hueḱᵘ-) / Meaning: to speak / Material: Old Indic vakti, vivakti says, talks, speaks ... Avestan vac- speak, uxta-. Old Indic vacas- = Avestan vacah (= gr. épos) discourse, word ... vāk = Avestan vāxš (= Latin vox) voice, discourse, word ... Latin vox, vocis voice, voco, -are call ... References: WP. I 245 f.' Page(s) 1135-1136."
  }
 ],
 "consulted": [
  {
   "src": "WLD",
   "where": "Bd. I 245-246 (WLD_Bd1_pages.txt l.22850ff., leaf 253)",
   "stance": "supports",
   "note": "'uekᵘ- „sprechen“. Ai. vákti, vivakti „sagt, redet, spricht“ ... av. vac- „sprechen“, uxta- ... ai. vacas- n. = av. vacah- (= gr. épos) „Rede, Wort“ ... ai. vāc-, n. sg. vāk = av. vāxš (= lat. vox) „Stimme, Rede, Wort“ ... lat. vox vocis „Stimme“, voco, -āre „rufen“'."
  },
  {
   "src": "AHD",
   "where": "Watkins 1985 s.v. wekw-",
   "stance": "supports",
   "note": "AHD_watkins1985.txt: 'wekw-. To speak. 1. O-grade form *wokw- in: a. Latin vox (stem voc-), voice: VOCAL, VOICE, VOWEL ... 2. Suffixed o-grade form *wokw-a- in Latin vocare, to call: VOCABLE, VOCATION ... 3. Suffixed form *wekw-es- in Greek epos, song, word: EPIC, EPOS. [Pok. uekw- 1135.]'"
  },
  {
   "src": "IEC",
   "where": "s.v. uequó",
   "stance": "partial",
   "note": "IEC.txt l.20012 'uequó (uequmi, uiuéqumi) call, say, speak ... WP I, 245 Skt. vakti ... Av. vač-, v. talk; Per. gūyam, inf: guftan, v. say' -- Mann has the root but wrongly files Persian guftan here (that verb is from *gaub-)."
  },
  {
   "src": "SYN",
   "where": "18.11 VOICE; 18.26 WORD",
   "stance": "supports",
   "note": "SYN.txt l.31455 '1. Derivs. of IE *wekʷ- speak, say (18.21). Walde-P. 1.245f. ... Grk. óps (poet.); Lat. vōx ...; Skt. vāc-, Av. vāč- (nom. sg. Skt. vāk, Av. vāxš); Toch. A wak, B wek'; l.31765 'Skt. vacas-, Av. vacah- ... Lat. vocabulum (more directly fr. vocāre call)'."
  },
  {
   "src": "CHEUNG",
   "where": "pp. 402-404 s.v. *u̯ač",
   "stance": "supports",
   "note": "CHEUNG.txt l.26156ff. '*uač to say, speak / AVESTAN: vaoc- (vāč-) to say || (+ *ā-) to say to || (+ *fra-) to proclaim ... PIE *uekʷ- to speak, to say > LIV: 673 f. | Pok.: 1135 ff.'"
  },
  {
   "src": "ARY",
   "where": "p. 513 (pdf 512) s.v. واژه، وات، واج",
   "stance": "supports",
   "note": "ARY_latin_index_pages.txt l.14955ff.: Avestan 'VAXSH, VAK, VACHAH', Pahlavi 'WAZ, VACHAK, WAZAG, VAJ', English VOICE, Latin VOX, VOCEM; references 'POKORNY 1135-1136'."
  }
 ],
 "nodes": [
  {
   "id": 1,
   "lang": "Avestan / Old Persian",
   "words": "vak, vačah, vaxš 1",
   "verdict": "confirmed",
   "derivation": "Avestan has the verb vac- / vaoc- 'to speak' (Indo-Iranian *wak-, *wač- < PIE *wekʷ-, with the labiovelar becoming k and then č before a front vowel), the neuter s-stem vacah- 'speech, word' (= Skt. vacas-, Gk. épos < *wekʷ-os) and the root noun vāč- 'voice, word', nominative vāxš (= Skt. vāk, Lat. vōx < *wōkʷs). Nourai's 'vak' is the root and 'vaxš' is that nominative (Bartholomae writes it vāxš with a long vowel). All three forms and the glosses are correct. The words are Avestan; Old Persian has no attested form of this root.",
   "derivation_fa": "در اوستایی فعل vac- / vaoc
```


## [2026-10-17T00:00:47.378Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; command ls site/pages/552.jpg; pdftoppm -f 552 -l 552 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg552 && echo ok"
}
```


### [2026-10-17T00:00:48.408Z] TOOL RESULT

```
site/pages/552.jpg
ok
```


## [2026-10-17T00:00:52.676Z] TOOL CALL #7: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg552.png"
}
```


### [2026-10-17T00:00:53.126Z] TOOL RESULT

```

```


## [2026-10-17T00:00:53.121Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-10-17T00:00:56.666Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'lemma: .*wes\\|lemma: u̯es\\|lemma: ues\\|lemma: .*wet\\|lemma: uet' POK_full.txt | head -30"
}
```


### [2026-10-17T00:00:57.088Z] TOOL RESULT

```
1541:lemma: ab-\ (water, river) : Root/ lemma: {en^^-2): ndd^-, errt'"-, /pb^-: (wet, damp; 
1561:lemma: {eneb'^-2): neb^-, errt^-, /pb^-: " wet, damp; water; clouds '. 
1587:(ro-): < with Aformant (n^^e/a): < Root/ lemma: {eneb'"-2): neb'"-, errt'"-, /pb^-: " wet, 
1743:Root/ lemma: au(e)-9, aued-, auer-\ "to flow, to wet; water, etc' 
3840:Root/ lemma: au(e)-9, aued-, auer-\ "to flow, to wet; water, etc' 
6032:/pbh-(A?-): < with /-formant {n^'^eli): < Root/ lemma: {en^^-2)\ /7ebh-, errio'^-, /pb^-: " wet, 
7244:Root/ lemma: uet-\ 'year' [prothetic i/- before bare initial vowels] derived from Root/ 
7699:lemma: au(e)-9, aued-, auer-\ "to flow, to wet; water, etc.'. 
9184:/■formant {neb^e/a)\ < Root/ lemma: {en^^-2): n^^-, errt^-, /pb^-: " wet, damp; water; 
9215:{ro-)\ < with Aformant {n^^el§)\ < Root/ lemma: {eneb'"-2)\ neb'"-, errt'"-, /pb^-: " wet, 
26887:Root/ lemma: uet-\ "year' [prothetic jt/- before bare initial vowels] derived from Root/ 
28560:Root /lemma: es-en-, os-en-, -er-\ harvest time, *autumn' : Root /lemma: ues-f. spring'. 
36220:Root/ lemma: uet-\ "year' [prothetic jt/- before bare initial vowels] derived from Root/ 
57042:Root/ lemma: mad-: wet; glossy, fat, well-fed, intoxicating : Root/ lemma: meA^w. honey, 
57861:Root/ lemma: rnahd-: wet; glossy, fat, well-fed, intoxicating : Root/ lemma: meM'^u: 
77670:Root / lemma: sRai-, sRai-. sRT-\ to glimmer (of wet things); shadow, derived from 
89129:Root/ lemma: ueti'^-, uii'^- 
92346:Root / lemma: ues-1 {* hauhes-f) 
92407:Root / lemma: ues-2 {* hauhes-2) 
92432:Root / lemma: ues-3 {* hyes-3) 
92461:Root / lemma: ues-4 {*hues-4) 
92484:Root / lemma: ues-5 {* haues-5) 
92523:Root / lemma: ues-no- {* haues-no-) 
92549:Root / lemma: ues-7 {* haues-7) 
92575:Root / lemma: ues-9 {* hayes-) 
92621:Root / lemma: ues-f{*h2auhies^ 
92627:Root/ lemma: ues-fi* h2auhies^\ spring, derived from Root/ lemma: aues-{* h2auhies^\ 
92688:Root / lemma: uet- {*huet-)
```


## [2026-10-17T00:00:58.614Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 92484,92548p POK_full.txt; echo =====; sed -n 92688,92760p POK_full.txt"
}
```


### [2026-10-17T00:00:58.933Z] TOOL RESULT

```
Exit code 1
Root / lemma: ues-5 {* haues-5) 

Meaning: to dress, put on 

Material: Old Indie i/a5/e"kleidet sich, zieht an', Avestan vasteds. (compare the unthemat. 

gr. EGoai, -soTai), varjhaiti 6s.\ Old Indie vasana-, Avestan varjhana- n. " garment '; Old 

Indie vasman- n. "cover' (= z\\\a)\ vastra-, Avestan vastra- n. " clothing ' (: gr. FEGipa, 

Middle High German westeil); 

Armenian z-genum^'^uW myself an' {*ues-nu- = zvvv[}\), z-gest^ clothing ' (-/i/-stem); 



gr. Evvupi, Ionian sTvupi, Aor. zo{o)a\ " apparel ', Med. "sich kleiden', athemat. Perf. £l|jai 
(*F£a-[jai) 3. Sg. Eni-Earai (Herod.); zoBoq n. ' clothing ' (-dhes-stem), zaBr\q, -nroc; ds. 
(*F£a[TO-]TaT-c; with dem 9 from eoQoq); savoc; "weibliches garment ' (Old Indie vasana-m); 
Ionian Attic sipa, Doric Fripa, Lesbian Fsppa 'dress' (: Old Indie vas-man-); Hes. yHMCi 
ipaTiov, £u-, KQKO, 5ua-£ifju)v "good, schlecht gekleidet', with Vorstufe of Itazismuslpariov 
'dress, mantle'; Doric Fsarpa (ysaTpa aroAri Hes.), z(pzoip'\qi. "warmeres Wintergewand, 
Soldatenmantel'; 

alb. vesh'\ kleide an', i//s/7e/77"kleide myself an'; 

Latin vest/'s ' clothing ', vest/'o, -Tre " apparel ' (compare Yscrria svSugk; Hes.); 

Gothic wasjan. Old High German werian. Old Icelandic veria^ apparel ', Old English 
werian^6s., dress bear, carry'; Gothic wastii. 'dress'; Middle High German wester {see 
above) Taufkleid' (but Old High German early wastibarn, previously by Notker westerwat); 
Old Icelandic veslu. "dress' {*wesala-), ver^ coating, layer' {*waza-); 

Hittite uas-, ues-, Luvian uas(s)-^beV\e\6ev\, lure, tempt '; Tocharian B wastsi, wastsi 
"dress' (neologism); A wsal6s.\ 

References: WP. I 309, WH. II 775 f.. Frisk 521 f. 
Page(s): 1172-1173 

Root / lemma: ues-no- {* haues-no-) 

Meaning: price 

Material: By den einzelnen Sprachen sways e-and ovocalism: Old Indie vasna- m. " 

purchase price', n. "earnings', i/5S/7ay5//"feilscht'; Armenian gin^ purchase price'; gr. hom. 

(I)vo(; " purchase price', Lesbian ovva {*uosnS), Ionian Attic cJbvri " purchase', cbv£0|jai " buy 

', gort. u)vr|v " sell '; Latin venus{ov\\)j in Akk. venum, Dat. veno, later venui) "sale' {vendo, - 

dere' sell ' is *venom+ do, i/e/7eo "verkauft become' = *venom+ eo); marr. eituam 

vena//nam ^pecun\a{r\ venaliciam' (?) muft ein loanword from Latin sein, da s/7marr. not n 

ergeben wurde; Old Russian i/e/70 "dowry'; Hittite ussan/ya-' sell ' (compare above uas- 

"buy'). 

References: WP. I 31 1 f., WH. II 753 f., Vasmer 1, 182 f. 

See also: ues-8 

Page(s):1173 

(eval):1: ==== not found
```


## [2026-10-17T00:01:01.225Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 92688,92745p POK_full.txt"
}
```


### [2026-10-17T00:01:01.690Z] TOOL RESULT

```
Root / lemma: uet- {*huet-) 

Meaning: year 

Material: Old Indie vatsa, vatsara-m. "year', vatsa-rc\. " yearling, calf, rother, cattle', 

vatsaka-m. " little calf, sa-vatarauH. Du. f. " identical calf habend'; sogd. wtsnyy{\eQ. 

wat(u)sand) "old'; 

gr. F£TO(;, £to(; n. "year', SiEinq " biennial ', i-\x\Q\oc^ "annual, yearly', Attic z\c, vsojia, 
delph. £vv£U)Ta "for the nachste year' (haplology from *v£Fu)-F£Ta, s. also £nr|£Tav6(; Frisk 
534, oi£T£ac; J. B. Hofmann Gr. etym. WB. 227, ar|T£c; above S. 609); gr. etcAov, etqAov " 
yearling from Haustieren' (: Latin vitulus, see below); 

alb. vit, PI. U7e/"year', parvJet^yo'cz\Ne\ Jahren', vjetei. "calf, vitsh, v/g'caW (from 
*ueteso-, compare Latin veterTnus); Messapic atavetes= auT6£T£(; "of gleichen year'; 

Comment: 

Alb. {*v/et) vit, PI. vjet^yeax' : Hittite witt- "year'; alb. vJeter^o\6' : Latin vetus, -er/s'o\6'. 



Latin vetus, -er/s'o\6' (alike £to(;; tlie Genet, veter/s sch\'\eQ>\. close connection to Old 
Lithuanian vetusas irom), vetustus ^o\d' (probably from * uetosto-s ^ aged' , formation as 
onustus: onus), vetulus^a\\.\\ch\ Oscan Vezkef "*Vetusco', god's name; Latin vetennus 
"Zugvieh'; v/tu/us'caW = Umbrian i/z/Az/'vitulos' (Italian /instead of e presumably through 
borrowing from a nicht naherto bestimmenden Indo Germanic language Italiens); Oscan 
l//fe//^" Italia', from which through Low Italian-gr. mediation Latin /fa//a, actually 'das land 
the //a//" ("young steers ', after dem Stiergott Mars); 

Middle Irish fe/s, corn, gu/s, abret. gu/s^so\N' {*uet-si-)\ 

Gothic w/Prus^one year old lamb', Old Icelandic vedr, Old High German w/dar^anes, 
ram' (compare above Old Indie sa-vatarau); 

Old Church Slavic vetbchb 'o\d', Old Lithuanian vefusas'o\6, aged'; 

a Lok. or possibly Akk. Sg. of zero grade stem ut- lies vor in Old Indie par-uf^'\n 
vergangenen years', Armenian heru, gr. TTspuoi, Doric nspuri. Old Icelandic ^'ord, Middle 
High German vertds., Old Irish onn-urid^ab anno priore' (Vokalumstellung?); 

Hittite Witt- "year', Hieroglyphic-Hittite usa-, Luvian ussa ds. 

References: WP. I 251, WH. I 723, II 776 ff., 807, Trautmann 365, Vasmer 1, 194, O. 
Szemerenyi ZDMG. 101, 204 f.. Word 8, 50, Frisk 534, 579 f., 583 f., Kronasser compare 
sound- under Formenlehre 126 A. 20. 
Page(s):1175 

Root / lemma: ye-l {*hue-) 

Meaning: we 

Grammatical information: uei- {P\ura\) 

Material: Nom. 1. Dual Old Indie vam{= va-am, Indo Germanic *-om), Avestan va, Gothic
```


## [2026-10-17T00:01:04.188Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; grep -n -i 'uesno\\|u̯esno\\|ues-no\\|„Kaufpreis\\|Kaufpreis' WLD_Bd1_pages.txt | head; grep -n 'uet-\\|u̯et-\\|„Jahr' WLD_Bd1_pages.txt | head"
}
```


### [2026-10-17T00:01:04.753Z] TOOL RESULT

```
23898:      Dazu wohl das Wort                        fur    den Kaufpreis der Braut.
23924:     Ags. WL otwnawihima, wctmam. „Kaufpreis der Braut*', afries. wetmu , led-
29532:                                                                  uesperoi (ueqeros;              — uesno-                                                                  311
29654:„Kaufpreis“,                          n.        ,,Lohn --     ,
49551:Kaufpreis“                ;
49562:mir. tor] ra „Umwerben“ (, ,*Brautkauf“), t-ind-s-cra „Kaufpreis fur die
1644:angu „wachse“ ugys „Jahreswuchs“) russ. uslo „Gewebe“ {uzda „Zaum“?).
1940:Hum), dann „Jahr, Jahrtag“ (Brugmann IF. 15, 87ff. und 17,319, gegen
3862:   Ai. dtati „geht,       wandert“.           annus „Jahr aus *atnos oder
3872:           got. dat. pi. aptiam „Jahr“.    Vgl. Fick I 2 338, W. Meyer KZ.
3874:jvram „Jahr“ zu ic- ,,gehen“).
3875:  Osk.-umbr. entspricht alcno- „Jahr, Festzeit, Opferzeit'* unit -In- zu -lot-,
9400:                    anord. ar , ags. gear ahd. jitr n. „Jahr‘ (nicht nach Noreen
9410:   av. yard n. „ Jahr“   gr. toga „Jahreszeit, Tageszeit, Stunde, rechte Zeit“,
12230:      Lit. eras , lett. jers      „Lamm“ gehoren zu got. jer „Jahr“, usw.
12232: jarbCb „Bock“ u. dgl. als „Jahrling“ zu jam, Miklosich E\Y. 100, Leskien
```


## [2026-10-17T00:01:06.508Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; sed -n 29640,29675p WLD_Bd1_pages.txt; echo ====; grep -n 'vatsa\\|vitulus\\|ve-tus\\|vetus' WLD_Bd1_pages.txt | head"
}
```


### [2026-10-17T00:01:06.885Z] TOOL RESULT

```
Exit code 1


..Wasserstrudel Zur Bedeutung vgl. anord. njol ..Nacht ', aus ,,*Aebel -£ S. 131.
                                       1-
                                            .
                                                                                                                                  -

                                                                                                                                                               ,


  Die zahlreiehe Lit. ist verzeichnet bei Yf. LEWb. 2 827 f.

iiesno- ,.Kaufprcis “.
  Bei den einzelnen Sprachen schwankt c- und o -Yokalismus.                                                                                           Ai. vasnd-h
„Kaufpreis“,                          n.        ,,Lohn --     ,
                                                                  vasnayati                ..feilscht" ;             gr.        hom. o>roz            ..Ivaufpreis",
lesb.    awn, ion. att. vnn)                                      ..Kauf
                                                                                --
                                                                                     ,   djveouai ,.kaufe
                                                                                                                       --
                                                                                                                            .
                                                                                                                                 gort. wri/r ..verkaufen"
iSolmsen KZ. 32, 293). Die gr. Grundform ist nicht mehr als K tiusuu- oder
*no no- anzusetzen, da lesb. own doutlich auf *yoovu weist. vgl. Kretsch-
mer 'Wiener Eranos 1900, 123. Ebensowenig weist arm. gin ..Ankaufspreis*
('Hiibschmann Arm. St. I 24 f.. Arm. Gr. I 434) auf ein delinstufiges *rc no-
 Pedersen KZ. 39, 414.                                             —
                                Lat. venus nur ini akk. leniun, dat. vcuo,
spiiter       vaiui) ..Verkauf --                                 [rendu, -dere ..verkaufen
                                                                                                                            --
                                                                                                                                 ist        *rr)iom        do,           r?neo
..verkauft werden — *r?uom — cn); marr. eituam vcnaVnmm ..pecuniam
                                                 --



(eval):1: === not found
```


## [2026-10-17T00:01:09.246Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; grep -n 'uet-\\|vatsd\\|vitul' WLD_Bd1_pages.txt | head; cd ../..; grep -n -i '^wes-\\|^wet-' AHD_watkins1985.txt; grep -n -i 'u̯et\\|^uet\\|^ues-no\\|^uesno\\|wesn' IEC.txt | head"
}
```


### [2026-10-17T00:01:09.567Z] TOOL RESULT

```
6116:miner „Farse“, acvmr. aideric „vitulus“, bret. ounner „Farse“ wiirden. wenn
12247:Arm. St. 23      erinj, „ddyaXig\ vitula, juvenca; bos“ (Petersson KZ. 47, 257).
20405:der leichten Wzf. *mie- envachsenes *uet- vgl. uhgov ai. mil-tra vielleicht                            :
20996:daS *uet- (wie *ii-er- „drehen“, uebli- „weben“, w dh- „knupfen“, uey- „weben“j
22504:aber bedeutungsahnlicher Sippen vorliegt:                                     s.   u. suet-.
23402:uet- „Jahr“,            -uetes-        n.           ds.,   *iietos(o)-           „*jahrig,   alt“;        in     Ableitungen auch
23405:  Ai. rutsa-, vatsard- m. „Jahr“, vatsd- m. „Jahrling, Kalb, Kind“. rat-
23420:vitulus, s. u.   Meister IA. 1, 204; 4, 32); alb. vjti „Jahr“, panjet „vor zwei
23441:„*Yetusco“, Gottername; lat. vetermus „Zugvieh“; vitulus „Kalb“ = umb.
23442:vitluf „vitulos“ (umbr. v- schlieBt, da bei einem landwirtschaftlichen Worte
133:wes-pero-. The Indo-Europeans oriented themselves by facing east. Therefore the root deks-, “right,” could also denote “south.” “Right” was considered lucky; the terms for “left” vary from language to language (one Indo-European term is laiwo-) and were evi- dently subject to taboo.
1157:wes-!
1159:wes-1. To buy. 1. Suffixed form *wes-no- in Latin vénum, sale: VENAL, VEND. 2. Suffixed o-grade form *wos-nd- in Greek dneisthai, to buy: DUOPSONY. [Pok. 8. wes- 1173.]
1160:wes-?. Wet. Germanic *wdés- in Old English wés, juice: 00ZE}. [Pok. 3. wes- 1171.]
1161:wes-3. To stay, dwell, pass the night, with derivatives meaning “to be.” 1.O-grade form *wos- in Germanic *was- in Old English wes, was: was. 2. Length- ened-grade form *wés- in Germanic *wéz- in Old English wére (subjunctive), w#ron (plural), were: WERE. 3. Ger- manic *wesan in Old Norse vesa, vera, to be: WASSAIL. 4. Suffixed form *wes-td- perhaps in Latin Vesta, house- hold goddess: Vesta. 5. Suffixed variant form *was-tu- possibly in Greek astu, town (< “place where one dwells”), whence Latin astus, skill, craft (practiced in a town): ASTUTE. [Pok. 1. wes- 1170.]
1162:wes-‘. To clothe. Extension of eu-'. 1. Suffixed o-grade form *wos-eyo- in Germanic *wazjan in Old English werian, to wear, carry: WEAR}, 2. Suffixed form *wes-ti- in Latin vestis, garment: VEST; DEVEST, INVEST, REVEST, TRAVESTY. 3. Suffixed form *wes-nu- in Greek hennunai, to clothe: HIMATION. [Pok. 5. wes- 1172.]
1163:wes-pero-. Evening, night. I. Reduced form “wes-. 1. Suffixed form *wes-to- in Germanic *west- in: a. Old English west, west: WEST; b. Old English westerne, western: WESTERN; C. Old English westra, more west- erly: WESTERLY. 2. Possibly Germanic *wis- in Late Latin Visigothi, “West Goths” (Gothi, the Goths): Vist- GorTu. II. Basic form *wespero-. 1. Latin vesper, evening: VESPER, VESPERTILIONID. 2. Greek hesperos, evening: HESPERIAN. [Pok. wesperos 1173.]
1165:wet-'. To blow, inspire, spiritually arouse. Related to wé-. 1. Lengthened-grade form *w6t- in Germanic suffixed form *wéd-eno-, *wéd-ono-, “raging,” “mad,” “inspired,” hence “spirit,” name of the chief Teutonic god, in: a. Old English Woéden, Woden: WoDEn; b. Old English Wod- nesdxg, ““Woden’s day”: WEDNESDAY; Cc. Old Norse Odhinn, Odin: Opin; d. Old High German Wuotan (> German Wotan), Wotan: WoTAN. 2. Lengthened variant form *wdt- in Latin vdtés, prophet, poet: vaTic. 3. Suf- fixed variant form *wat-no- in Latin vannus, a winnow- ing fan: FAN!, vAN3. 4, Oldest basic form *awet- becoming *awet- in suffixed form *awet-mo- in Greek atmos (< *aetmos), breath, vapor: ATMOSPHERE. [Pok. udé- 1113.]
1166:wet-2, Year. 1. Suffixed form *wet-ru- in Germanic *weth- ruz, perhaps “yearling,” in Old English wether, wether: WETHER. 2. Suffixed form *wet-es- in: a. Latin vetus, old (< “having many years”): VETERAN; INVETERATE; b. Latin veterinus, of beasts of burden, of cattle (perhaps chiefly old cattle): VETERINARY; C. Greek efos, year: ETESIAN. 3. Suffixed form *wet-olo- in Latin vitulus, calf, yearling: VEAL, VITELLUS. [Pok. wet- 1175.]
20184:uesnom (uosnom) ‘price’. Cf. ues- (1). WP I, 311 Skt. vasnám, n. id.; Oss. cf. wäi, s. ‘sale’; Hitt. cf. wesiya(s), s. ‘cost, price’; Arm. gin, gs: gno, s. id.; Lat. venum in — dare ‘sell’; venus, gs: -üs, m. ‘sale’; Umb. cf. (?) uestisia *JJibation'; OCS venjo, -iti, v. (1) "sell
20205:uetesi, abl. & instr. form of uetos, -es-, q. v. Myc. cf. wetei wetei ‘annually’; Alb. vjetë- vjetë, id. beside vjet, adv. “last year”; vitvit, m. ‘year’; Hitt. cf. wetassi “annually”
20206:uetesios, uetsios (uetsos) *year-old, annual; yearling'. Cf. uetos. WP I, 251 Skt. vatsáh, m. ‘calf, young animal, child”; Hitt. cf. sa-wetesc, adj. “of the same year; Gk. éteios, adj. ‘year-old; yearling’; Alb. vig, m. ‘calf; OLat. veter, Lat. vetus, gs: eis, adj. Cold" LW in Alb. i vjetër, id.); Go. wiprus, m. ‘ram’; OE weber, m. id. (and *wether); ON veðr, gs: veórs, m. ‘wether’; Sw. vädur, m. ‘ram, wether’; Du. cf. ouder-wetsch, -wets,
20209:uetəlos, om ‘year-old; yearling’. Cf. uetos and extns. Aeol. étalon, n. ‘yearling’; Lat. vetulus, adj. *oldish'; m. Cold man" Vocalism of Lat. vitu- lus, 1, m. ‘cal? problematical)
20211:uetios, cf. uetesios & uetos Arm. (?) gocan, s. ‘pig’, fr. *uetion-?); Li. ve- čias "old
20212:uetos, -es- “year, age’. Cf. uetesios, uetesi. WP I, 251 Skt. cf. tri-vatsám, n. ‘year’; vatsáh ‘yearling calf; Hitt. cf. weti “in a year’; wetasas (que- ried: “annual festival); wetanc ‘year’; Oss. cf. wäs 'calf; Gk. étos, gs: -eos, n. ‘year’; Alb. vit, m., vjetë, f., pl. vjet ‘year’; Lat. cf. vetus, gs: -eris, adj. old: Ir. cf. féis, OBr. guis, MBr. gwés, Cor. gwis, f. “pig, sow’; OE weóer, ON veðr, m. ‘wether’; OCS cf. vetüxü, adj. ‘old’; Cz. vetes, f. Junk, old rubbish'; OLi. cf. vë- tušas, Li. vecias, adj. "old": Latv. cf. vecs, adj. *old'; vecis ‘age’
20213:uetós (1) ‘woven, enmeshed; weave, mesh. Cf. WP I, 17, 134 & 224 Hitt. cf. wehtari, 3s. mp. “is turned’; MHG wat, sf. 'garment'; Du. wade, s. ‘shroud’; OE wæd ‘robe’; ON váð, pl. -ar, f. ‘textile, fishing- net”; pl. -ir, s. ‘ciothes’; Sw. våd, m. ‘width of cloth’; G Wat, f. “cloth, garment; Wate, f. “trawling-net'; Finn. (LW) vaate, s. ‘cloth, gar- ment
20215:uetolos, om — uibr-àió, -010
```


## [2026-10-17T00:01:14.581Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 23402,23412p incoming/WLD/WLD_Bd1_pages.txt; awk 'BEGIN{RS=\"\\f\"} {if(index($0,\"uet- „Jahr\")) print NR-1}' incoming/WLD/WLD_Bd1_pages.txt; awk 'BEGIN{RS=\"\\f\"} {if(index($0,\"iiesno- ,.Kaufpr\")) print NR-1}' incoming/WLD/WLD_Bd1_pages.txt; echo; grep -n -i '^wahāg\\|^wahag\\|wahâg' PHD.txt NYB_vol2_glossary.txt | head; grep -n -i 'wacc\\|wačč\\|waččag\\|baččag' PHD.txt NYB_vol2_glossary.txt | head"
}
```


### [2026-10-17T00:01:15.130Z] TOOL RESULT

```
uet- „Jahr“,            -uetes-        n.           ds.,   *iietos(o)-           „*jahrig,   alt“;        in     Ableitungen auch
       fur jahrige, junge Tiere.

  Ai. rutsa-, vatsard- m. „Jahr“, vatsd- m. „Jahrling, Kalb, Kind“. rat-
sakd- m. „Kalbchen“, savatardu N. du. f. „dasselbe Kalb habend" (Wacker-
nagel Ai. Gr. II 101).
   Gr. fezog,           hog n. „Jahr“, Siezqg ,,zweijahrig“, izijotog ,.jahrlich“, att. tig
vicora ,    delph. ev vecoza „fiirs      naehste Jahr“ (von Buck Gl. 1, 12Sf. auf
h'tfo-fara mit a aus idg. a zuruckgefiihrt, wofiir aber lokr. v-dmazEg keine
Stiitze ist, s. Brugmann IP. 38, 1 37 f.   vielmehr Haplologie aus *vE$-o)-$-tza
                                                                         ;
259
319

PHD.txt:909:baby waččag, kédak, kawādag.
PHD.txt:1223:child aburnüy(ag), frazand, waččag, zadag, zahag.
PHD.txt:1456:cub waččag.
PHD.txt:5142:wizihisnih wizihiin wizin- wizēn. wizēngar wizīr wizir- wizīristan wizīrišnīg wazīdan, wizīdan wizoh/y- wizoh/yisn wuzurg wuzurgih wizurdih wizurd wizóstan waččag wuzurg wuzurgih wačast wizistan wazišnig wazišn.
```


## [2026-10-17T00:01:17.871Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'waččag\\|wacc ag\\|wahāg\\|wahag\\b' PHD_mackenzie.txt PHD_pages.txt | head -20; grep -n -i 'price\\b' PHD.txt | head"
}
```


### [2026-10-17T00:01:18.267Z] TOOL RESULT

```
PHD_mackenzie.txt:6509:estimate wahag burdan.                             experience karagahih.
PHD_mackenzie.txt:7822:trading wahag.                           truthful arda; v. righteous.
PHD_mackenzie.txt:7886:union ayozisn, hamih, hambawisn(ih).     value (v.) wahag burdan.
PHD_pages.txt:6509:estimate wahag burdan.                             experience karagahih.
PHD_pages.txt:7822:trading wahag.                           truthful arda; v. righteous.
PHD_pages.txt:7886:union ayozisn, hamih, hambawisn(ih).     value (v.) wahag burdan.
```


## [2026-10-17T00:01:20.412Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i '^wa[hc]\\|^wacc\\|^wah' PHD_mackenzie.txt | head -20; grep -n -i 'price\\|value' PHD_mackenzie.txt | sed -n 1,20p"
}
```


### [2026-10-17T00:01:20.906Z] TOOL RESULT

```
5111:wacast [west I = Av. walas-tafti-] strophe (of the Gathas).
5112:waccag [wek l , (bek ) I N balia] child, baby, cub.
5139:wahig [wh)k' I M wh'g, N bahii] trading; value.
5141:wahar [wh)l, (bh)l) I M wh'r, N bahiir] spring.
5143:wahig [ZZLA < A ·zmr) (?); whyk ' I M whyg, N ·bahi] kid; astr.
5145:wahiAt [whit' I M whylt, N bihilt] paradise.
5147:Wahman [whwmn ' I M whmn, N bahman] Good Mind, the first Amahra-
5149:wAhman [·w-n l = w'hm'n l I M )w'hm'n, J whm)n, N bahman] so-and-so.
5150:Wahram [wllll'n l , w'hl'm I M whr)m, N bahram] god of war, victory; astr.
9785:wahig    I
10077:Wahram                               nigcr-                 -~.5'
10260:wahistig               ,~~,                 wazaraganih
10263:wahist                    \tbUN\            wazaragan
10375:waharig                    \~\                     dastiinestan      \"..tUJt""~
10379:wahman                     \t-06V\                 yastan                        \\teXV
59:without a unified map, and secondly to urge the practical value of
145:to the multiple values of the letters listed, some of them may
149:tion of one letter by one roman symbol of no practical value, a
154:guishing between the original values ), ~, dy, etc., of .~, n, W, r
156:beyond this by attempting to give closer 'phonetic' values to the
239: criminately for both phonetic values, !z for both Iranian h and x,
254:Iranian value(s), thus c and C for Aramaic~, h and Ii for Aramaic
267:under- or over-lining the letter value intended. Thus:
273:first value of each letter.
1190:arz [KSP' < A ksp; 'Ic I N ~] worth, value.
1195: -igih: value, worth, worthiness.
1197: -isn: value, worth.
1203:  .....ih: value, worth.
5139:wahig [wh)k' I M wh'g, N bahii] trading; value.
5140: ...... burdan: value, estimate.
7884:uninformed adistag.                      value (n.) arz, arzanigih, arzisn,
7886:union ayozisn, hamih, hambawisn(ih).     value (v.) wahag burdan.
12356:value of each letter only (see Table II, p. xiii), thus:
```


## [2026-10-17T00:01:25.287Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /trading; value/ {print \"wahag leaf\",NR-1} /child, baby, cub/ {print \"wacc leaf\",NR-1}' PHD.txt; grep -n -i 'wahāk\\|wahak\\|vahāk\\|wačak\\|waččak\\|wacak\\|vaččak\\|vačak' NYB_vol2_glossary.txt | head"
}
```


## [2026-10-17T00:01:26.823Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'baha\\b\\|bahâ\\|bahā\\|bača\\|bačč\\|bacca\\|bacah' HRN.txt | head -20; grep -n -i 'bahā\\|bačča\\|bacca\\|bačah\\|vatsa' HUB.txt | head -20"
}
```


### [2026-10-17T00:01:27.335Z] TOOL RESULT

```
wacc leaf 111
wahag leaf 112
```


### [2026-10-17T00:01:27.421Z] TOOL RESULT

```
829:-~ skr. vatsd' *KaIb' (vgl. skr. vatsaka- 'Kalbchen')
```


## [2026-10-17T00:01:31.299Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 815,840p HRN.txt; awk 'BEGIN{RS=\"\\f\"} /vatsd. .KaIb/ {print \"leaf\",NR-1}' HRN.txt; grep -n -i 'baha \\|bahä\\|bahd\\|vasna' HRN.txt | head"
}
```


### [2026-10-17T00:01:31.686Z] TOOL RESULT

```
Strasse)*; air. löeg 'Kalb*, (bei Feist).
kurd. helezium 'ich tanze*, lizim 'ich spiele', Inf.
leiztin.
Die Etymologie stammt von Justi, Dict. kurde-
frangais.
45. ätnäj 'Pflugsterz'.
g. matk (Houtum-Schindler, ZDMG. 36, 70).
arm. mac (de Lagarde No. 1413, Htibschmann
No. 186).
Die Lautverhältnisse von äinaj und mätk passen
nicht zu einander (vgl. auch Bartholomae, Studien
II, 24).
46. ümäden 'zurecht machen, rüsten*, ämUden, Praes.
ämäy-em, ämüy-em,
ap. vergl. ämäta- erprobt*; aw. ämata-, ämayäont^^
sie sollen sich versuchen',
oss. t. amain 'erbauen' (176).
47. äniär 'Berechnung', ämäre,
aw. a + 2 l^mar- 'sich erinnern'; phlv. amär 1) 'Zahl'
2) 'zähle, rechne* (das Verbum ämartan ist nicht belegt) ;
skr. a + V^smaV" (nicht belegt).
48. ätneden 'kommen*, Praes. äy-em (s. No. 60).
ap. ä+ [/^gam-, äjannya 'er käme*; aw. ci+ [/'(/am-,
ägemat; phlv. nrntan, ämatan (PPGl.) ').
Mit Mahjalvokal (FJ.).
^) FR hat einen Beleg aus Siräj eddin:
```


## [2026-10-17T00:01:35.057Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 815,835p HUB.txt; awk 'BEGIN{RS=\"\\f\"} /vatsd. .KaIb/ {print \"HUB leaf\",NR-1}' HUB.txt; grep -n -i 'Kind\\b' HRN.txt | head -30"
}
```


### [2026-10-17T00:01:35.428Z] TOOL RESULT

```
*bawr 'Tiger nicht hinaus.
181. Dieses Wort ist auch arabisch: vaftr animal quadrupes
fele minus, pulveris colorem habens, cauda carens*.
Nach Noldeke ist vabr 'Klippdachs* „wohl echt
arabisch**.
*) Also falsoh ftir vavar, vgl. avar oben Nr. 53.- 26 -
182. Np. hut ^Gotzenbild, Idol' (afgh. LW. but) nach Fr.
Miiller = Buddha, nach H o r n ~ zd. buiti 'Name eines
Damons' (vd. 19, 1). Beides schon im grossen Bunde-
hesh, vgl. Darmesteter, le Zend-Avesta II, p. 259.
184. Np. haSa, haSSa Munges, Kind' = phi. vacak (aus
*vaccak = vaUcaK*^) ist zunachst zu trennen von osset;
vdss *Kalb', bal. gvask *Kalb, Kalbchen (Geiger, Lautl.
p. 26), wax. vusk, sar. vi^k *Kalb', die auf iran. "^vasa^
-~ skr. vatsd' *KaIb' (vgl. skr. vatsaka- 'Kalbchen')
zuriickgehen und einem np. *vah' entsprechen wurden
(vgl. maht Tisch' = zd. masya^, skr. matsya-).
187. In bal. gvadil *feige' (aus ^gvaddil = *gvat-dil) ist
dil sicher persisches LW., dagegen wird goat echt sein
= np. badf phi. vat (arm. LW. vat) =■ ap. ^vata-. Da
es aber nur in gvadil vorkommt, nahm ich an, dass
HUB leaf 36
2203:afy. wör 'klein , wörkai, wörukai 'Kind*; bei. LW.
5711:zOq ') junges Huhn', zeh * Junges, Kind', zehdan 'Uterus*,
7578:871. kiitäh, küteh 'klein, kurz'; ködek 'Kind, Kleines,
11313:bei. gis 'Hausstand, Weib und Kind, Hauswesen und
```


## [2026-10-17T00:01:40.823Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n '^ *18[3-6]\\. \\|vacak\\|vaccak' HRN.txt | head; awk 'BEGIN{RS=\"\\f\"} NR==65' HRN.txt | head -60"
}
```


### [2026-10-17T00:01:41.379Z] TOOL RESULT

```
2013:184. bebe, beööe *Junges (von Tier und Menschen)' 2).
2026:185. beyit 'Schicksal'.
2031:186. bey(STden 'schenken', Praes. be/s-em, beyßis.
9888:184. Kauk.-bergjüd. auch vece,
11027:184. srältan 'schützen', sräy(i)sn, nur im AW.-Komm.
11030:185. Hvav *Wort', nur im AW.-Komm.
11033:186. Star 'Stern', häufig (neben stürak).
— 4:^ --
heSaz(i)änTh, bSSuzlnUan, bSSazlnUär und auch b(i)jaskth,
vd. 7 (94) ') ; ai. bhiSdj- *Arzt', hh^aja- *Arzenei\
arrn. LW. b^sk, b£skutiun.
g. pedesk (Houtum-Schindler) kann kaum hierher-
gehören.
184. bebe, beööe *Junges (von Tier und Menschen)' 2).
g. vaöe; Käs. veöd, veöi etc.; mäz. vaöa.
phlv. vaöak (vd. 14 (53) GL), baöak (vd. 19 (99) GL;
vd. 6 (17) flf., 'Glied des Fingers)»).
kurd. vacdhä *Familie' (H.-Sch.); oss. d. mss 'Kalb'
(79); bei. gvask *Kalb' (142); wa/. vmk^ sar. visk *Kalb'.
In der Bedeutung *Knabe' entlehnt in oss. d. biÖeu,
bifbeu (Hübschmann, Seite 121), bei. baiak (17),
af/. baöai.
Da np. c nicht für skr. ts stehen kann, so ist die
Zusammenstellung mit ai. vatsd- 'Kalb, Jährling*, unzu-
lässig ; das letztere Wort entspricht vielmehr np. gösäle
(No. 941).
185. beyit 'Schicksal'.
aw. baxta- *Verhängniss'; phlv. baxt 'Schicksal';
ai. bhaktd- zugeteilt'.
arm., bei., s.{y, LW. ba^t, kurd. LW. be/t, bakt
(letztere Form echt?).
186. bey(STden 'schenken', Praes. be/s-em, beyßis.
aw. |^6a/s- 'schenken' ; phlv. vergl. das im Np. auf-
gegebene Verbum baytan 'schenken', päz. baxsfdan,
ba/Sisn.
kurd. ba/sin; af/. ba$al resp. ba/al; bei. baksag,
n. baSkay (24).
np. ba^sis ist weithin entlehnt, schon arm. bas/is.
186^** bey(8uden (*buxsüden) 'gnädig sein, verzeihen',
Praes. bexsay-em, bex§äyis\ TNi^OJ^ (Qiss. Dan. 400,
13, 18; 402, 4).
1) Ha. büjasklh, so auch PPGl.
^) Peje bei AM. 220 Zeile 11 ist natürlich nur Druckfehler.
*) Hss. haben versohiedentlich die Variante bücak; derselbe
Fehler wie in der vorvorhergehenden Note.
```


## [2026-10-17T00:01:48.065Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /tmp; for u in 'https://en.wiktionary.org/w/index.php?title=%D8%A8%DA%86%D9%87&action=raw' 'https://en.wiktionary.org/w/index.php?title=%D8%A8%D9%87%D8%A7&action=raw' 'https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/wet-&action=raw' 'https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/wes-&action=raw'; do echo \"#### $u\"; curl -sL \"$u\" | grep -v '^\\s*$' | grep -i -A12 'etymology\\|{{root' | head -60; done"
}
```


### [2026-10-17T00:01:48.902Z] TOOL RESULT

```
#### https://en.wiktionary.org/w/index.php?title=%D8%A8%DA%86%D9%87&action=raw
===Etymology===
{{ety|ota|:bor|fa:بچه<t:child, kid><tr:bače>|text=+|tree=1}}
===Noun===
{{head|ota|noun|tr=beçe, beççe}}
# [[child]], [[infant]]
# [[boy]], [[lad]], [[youth]]
# [[page]], [[apprentice]]
# [[young]] of any [[animal]]
#: {{syn|ota|یاورو|tr=yavru}}
# [[issue]] or [[product]] of any thing
====Derived terms====
{{col2|ota
|بچهدار<t:pregnant><tr:beçedar>
--
===Etymology===
{{etymon|fa|id=child|:inh|ira-pro:*wacáh}}
{{inh+|fa|pal|tr=wck'|ts=waččag|t=child, baby, cub}},<ref>{{R:pal:Mackenzie:1971}}</ref> from {{inh|fa|ira-pro|*wacáh|gloss=calf}}.
===Pronunciation===
{{fa-IPA|bača,bačča|haz=bāča,bača}}
* {{IPA|fa|/betʃe/|a=Khesht,Konartakhteh,Dashtestan}}
* {{IPA|fa|/betːʃe/|a=Mashhad}}
* {{audio|fa|LL-Q9168 (fas)-Darafsh-بچه.wav|a=Iran}}
===Noun===
{{fa-regional|بچه|بچه|бача|dari2=کودک}}
{{fa-regional|بچه|پسر|писар|tg2=пур}}
{{fa-noun|cls=بَچَّه|cls2=بَچَه|pl=بچگان|pl2=بچه‌ها|tg=бача}}
# [[child]], [[kid]]
#### https://en.wiktionary.org/w/index.php?title=%D8%A8%D9%87%D8%A7&action=raw
===Etymology===
{{bor+|trk-oat|fa-cls|بها|tr=bahâ}}. <ref>{{R:tr:Nişanyan|paha}}</ref>
===Noun===
{{head|trk-oat|noun|head=بَهَا|tr=bähā}}
# [[price]], [[value]], [[valor]], [[worth]]
#: {{syn|trk-oat|دَكَرْ|tr=dägär}}
====Descendants====
* {{desc|az|baha}}
* {{desc|gag|paa}}
* {{desc|ota|بها|tr=baha}}
** {{desc|tr|paha}}
===References===
{{reflist}}
--
===Etymology 1===
{{inh+|ota|trk-oat|بَهَا|tr=bahā}}, from {{der|ota|fa-cls|بها|tr=bahâ}}, from {{der|ota|pal|tr=whʾk|ts=wahāg}}.
====Noun====
{{ota-noun|tr=baha}}
# [[price]]
=====Descendants=====
* {{desc|tr|paha}}
===Etymology 2===
{{ety|ota|:bor|ar:بَهَاء|text=+|tree=1}}
====Alternative forms====
* {{alter|ota|بهاء|tr=bahâ'}}
====Noun====
{{ota-noun|tr=bahâ}}
# [[beauty]], [[comeliness]]
=====Related terms=====
{{col|ota
|بهاء الدین<tr:Bahâ'uddîn>
}}
===Etymology 3===
{{ety|ota|:bor|ar:بِهَا<tr:bi-hā>|text=+|tree=1}}
====Prepositional phrase====
{{head|ota|prepositional phrases|tr=bi-hâ}}
# by her
===Further reading===
* {{R:ota:Redhouse|page=414}}
==Persian==
===Etymology 1===
From {{inh|fa|pal|tr=whʾk|ts=wahāg}}; ultimately from {{der|fa|ine-pro|*wes-||to sell, trade}}. Akin to Armenian {{m|hy|գին||price}}.
====Pronunciation====
{{fa-IPA|baˈhā|haz=bā}}
====Noun====
{{fa-noun|cls=بَهَا}}
# [[price]], [[value]]
=====Descendants=====
* {{desc|ba|баһа|bor=1}}
* {{desc|chg|بها|tr=baha|bor=1}}
** {{desc|ug|باھا}}
** {{desc|uz|baho}}
* {{desc|trk-oat|بَهَا|tr=bahā|bor=1}}
--
===Etymology 2===
{{bor+|fa|ar|بِهَا|tr=bi-hā}}.
====Pronunciation====
{{fa-IPA|biˈhā}}
====Prepositional phrase====
{{head|fa|prepositional phrases|tr=be-hâ}}
#### https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/wet-&action=raw
{{rootsee}}
* {{l|ine-pro||*wét-s}}<ref name="Kloekhorst">{{R:ine:Kloekhorst2008|head=u̯itt-|pages=1014-1015}}</ref>
** {{desc|ine-ana-pro}}
*** {{desc|hit|𒈬𒍝|tr=MU-za|ts=witta|t=year}}
* {{l|ine-pro|*wétos}} {{see desc}}
* {{l|ine-pro||*ut-só-s}}<ref name="Kloekhorst"/>
** {{desc|ine-ana-pro}}
*** {{desc|xlu|-}}
***: {{desc|xlu|𒈬𒅖|tr=MU-iš|ts=uššiš|sclang=1}}
***: {{desc|xlu|𔑺𔓉𔐤|tr=u-si-na|ts=usin|pos=acc.sg.|sc=Hluw|sclang=1}}
** {{desc|xlc|tr=uhe/i-||t=year}}
* {{l|ine-pro||*wétrus}}
** {{desc|gem-pro|*weþruz}} {{see desc}}
#### https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/wes-&action=raw
===Etymology 1===
{{etymon|ine-pro|id=dress|pos=root}}
====Root====
{{ine-root|impf}}<ref>{{R:itc:EDL|head=vestis|pages=671-672}}</ref><ref>{{R:gem:EDPG}}</ref><ref>{{R:ine:IEW|pages=1172-1173|head=u̯es}}</ref><ref name="LIV">{{R:ine:LIV|pages=692-693|head=1. *u̯es-}}</ref><ref>{{R:grc:Beekes|head=ἕννυμι|volume=I|pages=428-429}}</ref><ref>{{R:grc:Beekes|head=ἑᾰνός 1|volume=I|page=366}}</ref>
# {{topics|ine-pro|Clothing}} to [[dress]], [[clothe]]
=====Derived terms=====
{{rootsee|id=dress}}
* {{?}}{{l|ine-pro||*us-yé-ti|pos=yé-present}}
** {{desc|ine-ana-pro}}
*** {{desc|hit|𒉿𒀸𒊺𒄑𒍣|tr=wa-aš-š-še-ez-zi|ts=waššezzi|t=to wear, clothe|unc=1}}
* {{l|ine-pro|[[*wesnéwti|*wes-néw-ti]] ~ *wes-n̥w-énti|pos=nu-present}}
* {{l|ine-pro|*wéstor|*wés-tor|t=to be wearing|pos=deponent athematic Narten root present}}<ref name="LIV"/>
* {{l|ine-pro|*woséyeti|*wos-éye-ti|t=to dress|pos=causative}}<ref name="LIV"/>
* {{?}}{{l|ine-pro||*wḗs-t ~ *wés-n̥t|pos=s-aorist}}<ref name="LIV"/>
** Armenian:
*** {{desc|xcl|զգեցաւ|pos=aorist of {{m|xcl|զգենում}}}}
** {{desc|grk-pro}}
*** {{desc|grc|ἕσσα|pos=aorist of {{m|grc|ἕννῡμῐ}}}}
** Tocharian:
--
===Etymology 2===
{{etymon|ine-pro|id=graze|pos=root}}
====Root====
{{ine-root|impf}}<ref>{{R:ine:LIV|pages=693-694|head=3. *u̯es-}}</ref><ref>{{R:itc:EDL|head=vēscor}}</ref><ref>{{R:ine:IEW|page=1171}}</ref>
# to [[graze]], [[consume]], [[eat]]
=====Derived terms=====
{{rootsee|id=graze}}
* {{l|ine-pro||*wḗs-ti ~ *wés-n̥ti|pos=Narten present}}
** {{desc|ine-ana-pro}}
*** {{desc|hit|𒌑𒂊𒅆𒅀𒀜𒋫𒊑|tr=ú-e-ši-ya-at-ta-ri|t=to pasture, graze|unc=1}}<ref>{{R:hit:EDHIL|pages=1007-1008|head=u̯eši- / u̯ešai-}}</ref>
** {{desc|gem-pro|*wesaną|unc=1|qq=or from a thematic root presnet|t=to consume, feast}} {{see desc}}
* {{l|ine-pro||*wes-teh₂-}}
** {{desc|cel-pro|*westā|t=food, feast|unc=1}} {{see desc}}
* {{l|ine-pro||*wes-ti-}}
** {{desc|gem-pro|*wistiz|t=provisions, food|id=food}} {{see desc}}
* {{l|ine-pro||*wes-ri-}}
** {{desc|xto|wäsri|t=pasture}}
* {{l|ine-pro||*wēs ~ *wes-os|t=pasture}}?
** {{desc|itc-pro|*wēskōr|der=1|qq=with a long vowel perhaps via the analogical influence of a root noun or Narten verb|t=to nourish oneself}} {{see desc}}
--
===Etymology 3===
{{etymon|ine-pro|id=sell|pos=root}}
====Root====
{{ine-root}}<ref name="LIV2">{{R:ine:LIV|pages=693|head=2.*u̯es-}}</ref><ref>{{cite-book|last=Weeks|first=David Michael|year=2006|title=Hittite Vocabulary: An Anatolian Appendix to Buck’s ''Dictionary of Selected Synonyms in the Principal Indo-European Languages''. A dissertation submitted in partial satisfaction of the requirements for the degree Doctor of Philosophy in Indo-European Studies|location=Los Angeles|page=78|url=http://www.sonic.net/~dweeks/work/samples/write/Hittite_Vocab.pdf}}</ref><ref>{{R:hit:Kloekhorst:2008|page=981}}</ref>
# to [[sell]]
=====Derived terms=====
{{rootsee|id=sell}}
* {{l|ine-pro||*wés-ti ~ *us-énti|pos=athematic root present}}
** {{desc|ine-ana-pro}}
*** {{desc|hit|ts=u̯a-a-ši}}
* {{l|ine-pro||*we-wós-e ~ *we-ws-ḗr|pos=perfect}}<ref name="LIV2"/>
** {{desc|hit|ts=wāsi}}
* {{l|ine-pro||*wes-li-|t=sellable}}
** {{desc|itc-pro|*weslis}}
*** {{desc|la|vīlis}} {{see desc}}
* {{l|ine-pro|*wósn̥|*wós-n̥ ~ *us-né-s|sale; price}} {{see desc}}
* {{l|ine-pro||*wes-ó-s|selling, trade}}
** {{desc|iir-pro|*wasás}}
*** {{desc|ira-pro|*waháh}}
```


## [2026-10-17T00:01:52.452Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /tmp; curl -sL 'https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Iranian/wac%C3%A1h&action=raw' | head -40; echo ----; curl -sL 'https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/wes-&action=raw' | grep -A15 'ira-pro|\\*wah'; echo ---; curl -sL 'https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Iranian/wah%C3%A1h&action=raw' | head -30"
}
```


### [2026-10-17T00:01:53.489Z] TOOL RESULT

```
{{reconstructed}}
==Proto-Iranian==

===Etymology===
{{etymon|ira-pro|id=calf|:inh|iir-pro:*watsás}}
From {{inh|ira-pro|iir-pro|*watsás}}.<ref>{{R:inc:IAIL|vatsá-}}</ref>

===Noun===
{{head|ira-pro|noun}}

# [[yearling]] [[calf]]

====Inflection====
{{ira-decl-noun-auto}}

====Reconstruction notes====
Many of the descendants are suffixed with {{m|ira-pro|*-akah}}.

====Descendants====
{{top3}}
* {{desc|ira-nei}}
** {{desc|xsc-pro|*wasi}}
*** {{desc|xsc-skw-pro|alt=*wasaki|der=1}}
**** {{desc|xsc-sak-pro|alt=*basaki}}
***** {{desc|kho|tr=basakä}}
**** {{desc|wbl|wəšk|wušk}}
*** {{desc|xsc-sar-pro|alt=*was}}
**** {{desc|xln|alt=*wæs}}
***** {{desc|os-dig|уӕс}} 
*** {{desc|mns-pro|*wē̮səɣ|bor=1}}<ref>Sampsa Holopainen. ''Notes on Alanic and other steppe Iranian loanwords in Hungarian, Ob-Ugric and Permic'' (2022). </ref>
**** {{desc|mns-nor|tr=wāsiɣ}}
* {{desc|ira-sei}}
** {{desc|oru|tr=ɣoskák}}
** {{desc|ira-sgi-pro}}
*** {{desc|isk|tr=wusuk}}
*** {{desc|sgy|tr=wasōk}}
** {{desc|ira-shy-pro}}
*** {{desc|srh|wišk}}
*** {{desc|yah|в̌ус}}
* {{desc|ira-nwi}}
----
** {{desc|ira-pro|*wah-}} {{see desc}}
* {{desc|ine-toc-pro|*wäs-}}
** {{desc|xto|wäs-}}
** {{desc|txb|wäs-}}

===Etymology 2===
{{etymon|ine-pro|id=graze|pos=root}}

====Root====
{{ine-root|impf}}<ref>{{R:ine:LIV|pages=693-694|head=3. *u̯es-}}</ref><ref>{{R:itc:EDL|head=vēscor}}</ref><ref>{{R:ine:IEW|page=1171}}</ref>

# to [[graze]], [[consume]], [[eat]]

=====Derived terms=====
{{rootsee|id=graze}}
* {{l|ine-pro||*wḗs-ti ~ *wés-n̥ti|pos=Narten present}}
--
*** {{desc|ira-pro|*waháh}}
**** {{desc|kho|𑀩𑀳𑁄𑀬𑁆𑀲𑀦}}
**** {{desc|pal|tr=[[whʾk]]|ts=wahāg|sc=Phlv}}
***** {{desc|fa|بها|tr=bahâ}}
**** {{desc|os|-|t=sale}}
****: {{desc|os-dig|уӕйӕ}}
****: {{desc|os-iro|уӕй}}
**** {{desc|sog|ts=xwʾqr|t=merchant}}
**** {{desc|ira-pro|*wahá-čāra-|der=1|t=market}} {{q|with {{m|ine-pro|*kʷel-||to walk}}}}
***** {{desc|glk|واجار|tr=vājār|t=open market, bazaar}}
***** Kurdish:
*****: {{desc|ckb|باژاڕ|باژێڕ}}
*****: {{desc|kmr|bajar}}
***** {{desc|mzn|واجار|tr=vājār}}
***** {{desc|smy|vāžā́r}}
***** {{desc|pal|tr=[[wʾčʾl]]|ts=wāzār|sc=Phlv}}
****** {{desc|fa|بازار|tr=bâzâr}} {{see desc}}
*** {{desc|fiu-pro|*wosa|bor=1}} {{see desc}}

===References===
{{reflist}}

{{catlangname|ine-pro|homonymic roots}}
---
<!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<title>Wikimedia Error</title>
<style>
* { margin: 0; padding: 0; }
body { background: #fff; font: 15px/1.6 sans-serif; color: #333; }
.content { margin: 7% auto 0; padding: 2em 1em 1em; max-width: 640px; display: flex; flex-direction: row; flex-wrap: wrap; }
.footer { clear: both; margin-top: 14%; border-top: 1px solid #e5e5e5; background: #f9f9f9; padding: 2em 0; font-size: 0.8em; text-align: center; }
img { margin: 0 2em 2em 0; }
a img { border: 0; }
h1 { margin-top: 1em; font-size: 1.2em; }
.content-text { flex: 1; }
p { margin: 0.7em 0 1em 0; }
a { color: #0645ad; text-decoration: none; }
a:hover { text-decoration: underline; }
code { font-family: sans-serif; }
summary { font-weight: bold; cursor: pointer; }
details[open] { background: #970302; color: #dfdedd; }
.text-muted { color: #777; }
@media (prefers-color-scheme: dark) {
  a { color: #9e9eff; }
  body { background: transparent; color: #ddd; }
  .footer { border-top: 1px solid #444; background: #060606; }
  #logo { filter: invert(1) hue-rotate(180deg); }
  .text-muted { color: #888; }
}
</style>
<meta name="color-scheme" content="light dark">
<div class="content" role="main">
```


## [2026-10-17T00:01:56.285Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /tmp; curl -sL 'https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Iranian/wac%C3%A1h&action=raw' | sed -n 40,80p"
}
```


### [2026-10-17T00:01:56.729Z] TOOL RESULT

```
* {{desc|ira-nwi}}
** {{desc|bal|گوسک|tr=gwask}}
** {{desc|ku}}
**: {{desc|kmr|gîsk}}
**: {{desc|ckb|گیسک}}, {{l|ckb|گێسک}}
**: {{desc|sdh|گیسک}}
** {{desc|hac|گێسک|tr=gēsk}}
* {{desc|ira-swi}}
** {{desc|lrl|گیسه|tr=gēsa}}
** {{desc|pal|-|ts=wahīg|t=Capricorn sign; kid; he-goat}}
**: {{desc|pal|𐫇𐫍𐫏𐫃|sc=Mani|sclang=1}}
**: {{desc|pal|tr=whyk'|sc=Phlv|sclang=1}}, {{l|pal|tr=ZZLA|sc=Phlv}}
*** {{desc|bqi|بیگ|tr=bīg}}
*** {{desc|fa-cls|بهی|tr=bahī|t=Capricorn sign}} {{q|only in Albiruni works}}
{{bottom}}

===References===
{{reflist}}
* Edward F. Bryant and Laurie L (2005). Patton, eds. ''The Indo-Aryan Controversy: Evidence and Inference in Indian History''. London and New York: Routledge, P 201
{{reflist}}

{{topics|ira-pro|Mammals}}
```


## [2026-10-17T00:02:12.595Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in vend vendor veal veteran veterinary venal; do grep -n -i \"^$w,\" KLN_1966.txt | head -2; grep -n \"^${w^^}\" SKT.txt | head -2; done"
}
```


### [2026-10-17T00:02:13.033Z] TOOL RESULT

```
(eval):1: bad substitution
41201:vendor,  n.  —  AF.  vendour,  vendor,  fr.  OF.  (=  F.) vendeur,  fr.  L.  venditdrem,  acc.  of  venditor, ‘seller’,  fr.  venditus,  pp.  of  vendere.  Cp.  the  noun vender  and  see  vend  and  agential  suff.  -or. veneer,  tr.  v.,  to  overlay  (wood)  with  a  thin  sheet of  fine  wood.  —  Fr.  earlier  fineer,  fr.  G.  fur- nieren,  fr.  F.  fournir,  ‘to  furnish’,  fr.  OHG. frumjan,  ‘to  provide’.  The  word  was  borrowed from  and  re-borrowed  by  one  and  the  same language  at  two  different  periods.  See  furnish. Derivatives:  veneer,  n.,  veneer-er,  n.,  veneer-ing, n.
(eval):1: bad substitution
41153:veal,  n.  —  ME.  vel,  veel,  fr.  MF.,  reel,  veau  (F. veau),  fr.  OF.,  fr.  L.  vitellus,  dimin.  of  vitulus, ‘calf’,  which  is  rel.  to  Umbr.  vitluf  (pi.  acc.), ‘calves’,  and  cogn.  with  OI.  vatsdh,  ‘calf’.  The orig.  meaning  of  these  words  was  ‘yearling’,  fr. I.-E.  base  *wet,  ‘year’,  whence  also  Gk.  £to c, (dial.  *FIto?),  ‘year’,  sxaXov,  Dor.  exsXov, ‘yearling’,  Goth,  wifrus,  OE.  weder,  ‘wether’, L.  vetus,  ‘old’.  See  wether  and  cp.  etesian,  Ital¬ ian,  vellum,  veteran,  veterinary,  vitellus,  vitular. vectis,  n.,  an  instrument  used  as  a  lever  to  facili¬ tate  delivery  (obstetrics).  —  L.  vectis  ‘pole,  bar, lever’,  from  the  stem  of  vehere  (pp.  rectus),  ‘to carry,  convey’.  See  next  word, vector,  n.,  a  quantity  having  magnitude  and  di¬ rection  (math.)  —  L.,  ‘carrier,  bearer,  conveyer’, fr.  vectus,  pp.  of  vehere,  ‘to  convey’.  See  weigh and  cp.  vehicle.  Cp.  also  the  first  element  in walleyed.
(eval):1: bad substitution
(eval):1: bad substitution
(eval):1: bad substitution
(eval):1: bad substitution
```


## [2026-10-17T00:02:15.391Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"^vend,\\|^veteran,\\|^veterinary,\" KLN_1966.txt | cut -c1-500; for w in VEND VEAL VETERAN VETERINARY; do grep -n \"^$w\\b\" SKT.txt | head -2 | cut -c1-400; done; awk 'BEGIN{RS=\"\\f\"} NR==613' SKT.txt | head -15"
}
```


### [2026-10-17T00:02:15.884Z] TOOL RESULT

```
 much,  many.
Bwtn-uncle.  (E.)     Annvt-^an n  tJbr  preSxed  m  U  doe  to  the
indef.  article.  Afy  ntmcle^mint  untfe, Urhere  the  n  is  due  to  the  po&ses-^ivr  pro- nonn.  \q  n-cnce,  the  prefixed  n  m,  due  to the  dat.  case  of  the  def.  article,  as  shewn.
Iff-  (j),  negative  prefix.  (E.  cr  L.)  In now,  the  prefixed  n  is  doe  to  A.  S,  ne, not-  In  n-uli,  it  is  due  to  the  cognate L,  nt,  not.     See  Ne-.
We-,  Neg  .  (L.)  L.  nt,  not :  nee  (whence neg-  in  neg-iigtre),  not,  short  for  ne-que, nor,  noL  In  ne-fanous,  negation,  neg- lect, n^'Otiate,  nc-uter.     See  N-  (a).
H'on-,  not.  (L.;  ffrF.  — I..)  \..  »ton,  ncA. \ short  for  m«  unum,  not  one  :  see  aI;K>ve. It  appears  as  urn-  in  umpire,  put  for num^rt.
O  ;  omit;  see  Ob-.
Ob-.  (L.;  Qr  F.-L.)     L.  0^.  near;  allied
to  Gk.  ivi.upon,  near;  Skt.  a/*/,  more- over, Lith.  a/f,  near.     See    Epi-.     The forc€  of  A^   is  very  variable  :    it   ap- pears as  ♦-,  0*-,  oc;  c/',  op;  also  as  ex- tended   to  OS   (for  06s?)   in  o-mit,  ob- long, oc-cur,  of-fer,  op-press,  os-teosible. Oo-;  oc-cur;  sec  Ob-. Of    u);   offal.    (E,)     A.S.   cA   of.    off. away.     This  word  is  invariably  written cjf  in  composition,  except  in  the  case  of effa/,  where  its  u^  would  have  brought three  y's  together. +  L.  o^,  Gk.  d»«i ;  sec Ab-    (1),   Apo-.     It    appears  ■■  ••  In aitff7P». Of-  (j):  offer;  see  Ob-. Off-;  see  or- (1).
On-,  on,  upon.  (E.)    A.  S.  w,  on.  +  Gk. dj>a.    From  a  pronominal  base    Sec  Ana-. It  often  appears  as  a-,  as  in  a-foot.  a- sleep,  dec. Op-;  op-press;  sec  Ob-. Or-  (i);    or-rleal,  or-ts.    (E.)     A.S.  cr- ; cognate  with  Da,  Mr,  O.  Sax.  and  G. ur^.  Goth,  uj,  away,  out  of. Or-  [t):   or-lop.    (Hu)      Short   for   Dn. iwer.  cognate  with  E.  ffver ;  sec  Over-. Os-  :  ostensible :  see  Ob-. Out-.  (E.)     A.S.  W/,  E-iwA  [>rep.+Goth, u/,   G.auj,  Skt.  uU,  out.     Shortened  to utt-  in  ult  er. Outr- ;  outr-3gc    vF  — L.)      F.  ««/nr=-L.
ulfra,  beyond  ;  see  Ultra-. Over-.  (E)     A.  S.  o/er,  E,  fivtr,  prep.+ Goth,  w/ar,   L.  s  u/er,   Gk.  Cmtp,   Skt. u^ri,  anove.    A  comparative  form  from Up,  q.v.   See  Hyper-,  8ao«r-,  Q«-  <>'^.
Pft- 1  yAsy ;  «ft  "Pm*-
I
Palin-,  Pallm-.  again.  (GkO  Gk.  wiktr, back,  again.    It  becomes /iz/i'M'  in  palim-
Fan-.  Panto-,  all.  <Gk.)  Gk.  war,  nrut. of  irdr,  all :  woi'ro-,  crude  form  of  the lame,  occurring  in  panto-minie.
```


## [2026-10-17T00:02:18.435Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"veal\\b\\|^vend\\|veteran\\|vatsa\" SKT.txt | head -10 | cut -c1-400; grep -n \"vend, \\|veteran, \\|veterinary, \" KLN_1966.txt | cut -c1-400 | head"
}
```


### [2026-10-17T00:02:18.864Z] TOOL RESULT

```
805:Apocalypse.  (L.-Gk.)  M.E.  nfiotm (Wyclif).  —  L,  apocatypiis.  —  Gk.dffMtoAM a  revelation.— Gk.  anoKaKvwrtiv,  to  uaco< reveal.  — Gk.  dv6,  off;  and  «aXv«r«ir, cover.     (^KAL).
9344:Inveterate ;  see  Veteran.
16020:Reveal :  see  Vehicle.
20631:Veal.  (F.  -  U)  O.  F.  vt^/, uitelium,  ace.  oiuitellus,  dimin a  calf.  <f  Gk.  l-mXCt^  a  calf;  Skjl calf,  properly  '  n  yearling/  fitim  \ Gk.  jTor,  a  year.  Allicil  to  Ve* vellum.  (F.-L.)  M.  E,  w/« velin  (F.  v^iim).  —  Low  L  uit pelHs  uitnlina.  vellum,  calf's uitulinus,  adj..  from  uitnluf,  a  q
20647:reveal.  (F.  -  L.)     F.  rrvder.  Mo  re-
20662:venesection,  blood-letting.    (L.)     L. ^.  of  a  vein.  gen.  of  utna  ;  and  ttdion. venous,     bclunying    to    a   vein.    (I^) ^«j,  adj.,  from  uerta^  a  vem. ,    lo  harass.  ^F.  — L.)     F.   vtxer.^ re,  to  vex ;  orig.  intensive  form  of A/«  (pj  t.  it€jc-i).     And  see  Viaduct. elL  Vein ;  tec  Vohomont. oUum :  icc  Veal. ;Veloeit7.  (F.  -  L.)    F.  w&
20805:Veteran.    (L.)      L.    ueteniHUs,    expe- rienced ;  as  sb.,  a  veteran. —  L.  utUr-,  item, of  uthu,  old,  lit.  '  advanced  in  years.' Gk.  irofi,  Skt.  ra/io,  a  year.
20915:Viol.  iK.  —  L.)  F.  vioU.vUtU^  *a  violin;* Cot  The  same  as  Ital.  Span,  cro/a,  Port. viula,  viola.  —  Low  L.  vidula,  vitula^  a viol  (Die/),  — L.  uttulari,  to  celebrate  a festival,  keep  holiday ;  prob.  orig.  lo  sacri- fice a  calf  —  L.  uitniuSf  a  calf;  see  Veal. And  fee  Piddle.
21343:Wether,  a  castrated  ram.  (E.)  K.  S. Bv5*r+0.Sax.  wtthfir,witkar,  Icel.  ivCr, Dan.  vadcr,  Swed.  vadur,  G,  widdtr,  Goth. wiMrm,  a  lamb.  LiL  '  a  yeaxUng  ;  *  allied to  Veal.
23362:vade — fade, valtt — varlet. vast — waste. veal — wether, veneer— furnish. venew.  veiiey — venue, verb — woid vertex— voncK.
13881:Evelyn,  masc.  PN.  —  Prob.  fr.  prec.  word, even,  n.,  evening  (poet.)  —  ME.  eve,  even,  fr.  OE. it  fen,  rel.  to  OS.  aVand,  ON.  aptann,  Dan.  of¬ ten,  OFris.  evend,  Du.  avond,  OHG.  aband, MHG.  abend,  G.  Abend,  and  cogn.  with  Gk. 6m-  in  6ra#s(v),  Ion.  and  Att.  om<j(ls(v), ‘after,  behind’,  6i|;s,  ‘late  in  the  day,  at  even’, hid,  ‘upon,  after’;  
41153:veal,  n.  —  ME.  vel,  veel,  fr.  MF.,  reel,  veau  (F. veau),  fr.  OF.,  fr.  L.  vitellus,  dimin.  of  vitulus, ‘calf’,  which  is  rel.  to  Umbr.  vitluf  (pi.  acc.), ‘calves’,  and  cogn.  with  OI.  vatsdh,  ‘calf’.  The orig.  meaning  of  these  words  was  ‘yearling’,  fr. I.-E.  base  *wet,  ‘year’,  whence  also  Gk.  £to c, (dial.  *FIto?),  ‘year’,  sxaXov,  Dor.  exsXov,
41187:with  OI.  vasndfi,  ‘purchase  money’,  vasndm, ‘reward’,  vasnayati,  ‘he  bargains,  haggles  ,  Arm. gin  (for  *wesnom),  ‘purchase  money’,  Gk.  uvr), &v op,  ‘price  paid  (for  a  thing),  purchase  ^Les¬ bian  8wa  (for  *wosna),  ‘purchase’,  Gk.  cbvEt- cr9-oa,  ‘to  buy’,  Hitt,  ushshaniya-,  ‘to  sell',  and —without  the  suff.  -no — wash-,  ‘to  buy’.  Cp. vend,  vendee,  v
41189:Derivative:  venation-al,  adj. vend,  tr.  v.  —  F.  vendre,  fr.  L.  vendere,  ‘to  sell’, shortened  fr.  venundare,  fr.  venum  dare,  lit.  to give  (i.e.  offer)  for  sale’,  fr.  venum  or  venus, ‘sale’,  and  dare,  ‘to  give’.  See  venal  and  date, ‘point  of  time’.
41190:Derivatives:  vend,  n.,  vendee  (q.v.),  vend-er,  n., vend-ing,  n.  and  adj.,  vendor  (q.v.) vendace,  n.,  a  whitefish  ( Coregonus  vandesius).  — ModL.  vandesius,  fr.  MF.  (=  F.)  vandoise, ‘dace’,  fr.  Gaulish  *vindesia,  ‘whitefish’,  fr.  Cel¬ tic  vindo-,  ‘white’ ;  see  winter  and  cp.  Wend.  For sense  development  cp.  F.  able,  ablette,  ‘the bleak’,  fr.  L.  alb
```


## [2026-10-17T00:02:22.493Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /Veal.  \\(F/ {print \"veal leaf\",NR-1} /Veteran.    \\(L/ {print \"vet leaf\",NR-1}' SKT.txt; awk 'BEGIN{RS=\"\\f\"} /^veal,  n/ || /\\nveal,  n/ {print \"kln veal leaf\",NR-1} /\\nvend,  tr/ {print \"kln vend leaf\",NR-1}' KLN_1966.txt; grep -n -i 'veterinary,\\|veteran,' KLN_1966.txt | cut -c1-300 | head -4"
}
```


### [2026-10-17T00:02:22.916Z] TOOL RESULT

```
veal leaf 566
vet leaf 571
kln veal leaf 898
41153:veal,  n.  —  ME.  vel,  veel,  fr.  MF.,  reel,  veau  (F. veau),  fr.  OF.,  fr.  L.  vitellus,  dimin.  of  vitulus, ‘calf’,  which  is  rel.  to  Umbr.  vitluf  (pi.  acc.), ‘calves’,  and  cogn.  with  OI.  vatsdh,  ‘calf’.  The orig.  meaning  of  these  words  was  ‘yearling’,  fr. I.-E
```


## [2026-10-17T00:02:27.373Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'بهاگیر\\|بها گیر' FSF_pages.txt BQT_v1_pages.txt MON_part1.txt | head; grep -n 'waččag\\|wačak\\|vačak\\|wacak\\|vaccak\\|vacak' BQT_v1_pages.txt | head"
}
```


### [2026-10-17T00:02:27.808Z] TOOL RESULT

```
BQT_v1_pages.txt:21858:بها گیر با کاف فارسی بر وزن
BQT_v1_pages.txt:21865:بمملی_بهاگیر است که چیزی بسیار قیمت
MON_part1.txt:26334:بها گیر: ءآو.." (اا.) هر چیزی که قیمت
```


## [2026-10-17T00:02:29.832Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 21835,21875p BQT_v1_pages.txt; awk 'BEGIN{RS=\"\\f\"} /بها گیر با کاف فارسی/ {print \"leaf\",NR-1}' BQT_v1_pages.txt; sed -n 26330,26338p MON_part1.txt"
}
```


### [2026-10-17T00:02:30.823Z] TOOL RESULT

```
۵ « تاوادبا ۰۱۵4 < اونوالا ۳۸4» رك : آمی و فرهنگه روستابی ۲۵۹ وگل کلاب ۷۲۷- نیز
» پپلوی )۳2, ابرانی باستان ۰۳241 اوسنابیُ]]۳8» بارسی‌باستان۳2)1
« بارتولمه ۳۲۲ 4 . بازند ۳2 . پهلوی تورفان 02010 « یبر گه ۱۷۸ ».
۴ هن فری ات تیاه یه فشده.. ها پیلور
و5 دلرسی باستان 2 -1۱:۲8 * اسفا ۱: ۲ ص۲۳* ( ثوره واهره ماه دوم‌هضامنشی .
رك : دوازده ماه هخاهنشی بقلم نگارنده .آموزش ویروری سال 46 شمار؛ ۱ ص ۸ ۰ )» کیلکی
۳ «: فرب زندی و برنی 26192۲ « 2 . ۱ ص ۲۸4 ۰ سمنانی 9812۲ ری
۲فت ۱ سرخه 24 294 . لاسگردی ۳ ., ی ۳ اد . ۲ ص ۱۷۹ »
ورك:بهامن_ نیز وزنه ابست هندی «دائرالمعارف اسللام*. - مانسکریت ۷111878 بمعنی
دمر(تخانه). رك: توبهار ومزدینا ۳۲۵. اما بهارچین بابهار خانة 9 نگارستان چی‌وبابهارستان
طاهیآهمان جهشت گنک اس تکه برخی از شعرای ماآن را بتخانه بنداشته‌اند. رك : بهشت کنك .
۴ - رگ : بهار وبپعت کنگه .قدید گویندش . #
لها - بکس اول و ثانی بالف کشیده
و بزای نقطه دار زده » اسب اصلی زا گویند که
در ایلقی بجهت شاج کرفتن سردهند ۷ .
به ) ات هم کنابه ازهبود باشده و بهبود
معنی خیرت.
4 آ فرین - نام خواهر اسقندیار بن
کشتاسب است که او را ارجاسب اسر کرده بود
ودر رویثه در مجبوس داشت. بمد ازان اسفندبار
با تجا رفت وارجاسب را کشت وبهآفرین را نجات
داد. واورا به آفرد ح مسگوین دکه بسای‌نون
دال باشد .
بها گیر با کاف فارسی بر وزن
تباشیر, هرچیزی را گویند که قیمت وبهای‌بسبار
داشته باشد ۳
بهامین 5 بای بروزن معاجین.ضصل
بهار را گوشد .
بممنی گربه کردن باشد . #
بهاور * - بنتح اود بروزن تتاکر ,
بمملی_بهاگیر است که چیزی بسیار قیمت
۱ 5 مد نوروزنامه ص۱۳ ۰۱
7 کرسنن « بونکر۱۰۲*.
ویریها باشد. ۱
لت م بختح اول وگ#نی وسکون فوقانی؛
نوعی ازطملم باشد» وبعضی کوبند شیربرنج است
وی گویند فرنی است که برادر مالوده باشد .
وبستی کویند حلوای برنج است ۰ و ععرب آن
بیط باشد باتشدید طای حطی .
بهقر لك ۱ - بانای قرشت بروزن‌اسیركه
نام سالی است سیزده ماهه که پارسیان بیش از
leaf 543
جهت نتاج گرفتن آن را در گلهٌ اسب رها 
کنتد 


بها گیر: ءآو.." (اا.) هر چیزی که قیمت 
بسیار داشته باشد؛ قیمتی» گرانبها. 

بهانه: (0۵822)6 عدذر نایجاء دست آوبز. 
باز خواست؛ ایراد. سبب؛ باعث.
```


## [2026-10-17T00:02:34.421Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR-1>=440 && NR-1<=470 && /بچه/ {print \"leaf\",NR-1}' BQT_v1_pages.txt; grep -n '^بچه\\|^ *بچه -\\|بچه - ب\\|بچه ۱' BQT_v1_pages.txt | head"
}
```


### [2026-10-17T00:02:34.894Z] TOOL RESULT

```
leaf 457
leaf 468
17662:بچه‌جود ۰ کنابه ازلمل و بافوت
17664:بچه حور شید - بممنی ,چخوراست
17674:بچه نو بفتح نون‌وسکون‌واو» حادله‌ای
19200:بچهُ کوسفندباشد وآترا بمربی حمل خرانند۴ -
22551:بچه درآن متکون شده باشد .
```


## [2026-10-17T00:02:36.957Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR-1==457' BQT_v1_pages.txt | grep -n 'بچه\\|vac\\|wac\\|bac\\|ba[čc]' | head -20"
}
```


### [2026-10-17T00:02:37.386Z] TOOL RESULT

```
13:بچه‌جود ۰ کنابه ازلمل و بافوت
15:بچه حور شید - بممنی ,چخوراست
25:بچه نو بفتح نون‌وسکون‌واو» حادله‌ای
```


## [2026-10-17T00:02:39.674Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR-1==456' BQT_v1_pages.txt | tail -40"
}
```


### [2026-10-17T00:02:40.213Z] TOOL RESULT

```
چ - بش او و سکون ثانی , ادرون
لنبوی دهن باشد ۷ - و موی پیش سر را تیز
کنتماند .
بچ‌بج « ینم دو بای ابجد وسکون دو
جیم فارسی؛ حرف‌زدنی باشد در نهایت آهستگی»
و سرکوشی را دز کویند ۸ - و لقظی اس تکه
شباهان بزرا بدان نوازش کنند وییش خودخوانند.
پچر اعد سیدن - کنابه از رسیدن
بدواشی باشد با رسیدن بشدمت دولتمندی .
‌
پچ رگ ه بکر اول بر وزن خشتك »
بمعئی سخره و فربب‌خورنده باشد » و باین معنی
بکسر اول وثانی پروزن سرشا‌هم آمدهاست؟ .
توت بر هو
تحو جیا ۴ »با جیم بر دزن قلونیا .
بلفت زند و پاژند (۱) ملد هر حی‌انی را گویند
ی ون
بح ضم 00( .استضوان
شتالنگه را کوند و بتازی کب خوانند 9۵ ..
بحه ك‌ نح اول و ثالی» تام جابی‌وعقامی
است مابین اسفهان وظری ۷
‌
بچشی « بفتح‌اول و الی بروزن حبش »
و دج و مشفت هم آمده است ۰
بچشاك س یکراول ونالی‌بروزن‌سرشاك,
حکیم و طبیب وکیاه‌فووش را کونند *۷.
بچشم | هلان - چد زخم راگویند,
یعنی آزاری بکسی رسیدن .٩٩‏
" بچشم کردن ۰« کنابه از اتخاب
دمودن - و نشان کردن - وتند وتیز نگریتلن-
و چشم زده کردن و چشم زخم رساندن باشد .
بچلث - تح اول و ثانی وکون کاف
نام اسلمه‌ای باشد غیر عملوم .٩۳‏
. چك : ژد وپاژند‎ )٩(
٩‏ یمعنی طبیب است
۴ مرك : مجول. ۴ - هز »
ه‌ رگ : مجل.
۷ رد : یج
ره :پزخك .
۹ سئظء مصخف چرباك (ه.م).
```


## [2026-10-17T00:02:42.248Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; timeout 300 python3 tools/ref_page.py BQT:237 --image 2>&1 | tail -30"
}
```


### [2026-10-17T00:02:42.758Z] TOOL RESULT

```
no scan of BQT covers printed page 237 (see 'scans' in refs_online.json)
```


## [2026-10-17T00:02:46.782Z] TOOL CALL #35: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt552; cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt552; curl -sL -o leaf457-552.jpg 'https://archive.org/download/borhan-ghate-v1/page/n457_w1200.jpg'; file leaf457-552.jpg; ls -la"
}
```


### [2026-10-17T00:02:49.731Z] TOOL RESULT

```
leaf457-552.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 1240x1754, components 1
```


## [2026-10-17T00:02:51.830Z] TOOL CALL #36: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt552/leaf457-552.jpg"
}
```


### [2026-10-17T00:02:51.864Z] TOOL RESULT

```

```


## [2026-10-17T00:03:01.930Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources; mkdir -p refs/ocr/BQT refs/ocr/BOOK; cp /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg552.png refs/ocr/BOOK/552.png; command ls refs/ocr/BQT | head -3; cat > refs/ocr/BQT/237.vision.txt <<'EOF'\n[BQT vol.1 printed p. 237 = archive.org borhan-ghate-v1 leaf n457; read from page image]\nHeadword column (right): بچکم ... بچل ... بچم ... بچهٔ خور ... بچهٔ خورشید - بمعنی بچهٔ خوراست\n(left): بچهٔ خونین - کنایه از اشک گلگون باشد. بچهٔ طاوس علوی ... بچهٔ کو (۴) ... بچهٔ نو ... بچیز ...\nFootnote 4: مرکب از: بچه + کو (= مخفف کوی) [رک: کوی].\nFootnote 5 (Mo'in on بچه): بچه - بفتح اول و دوم، پهلوی vacak «تاوادیا ۹۱۶۶»، بندهش ۱۱۲، طبری vaca «واژه‌نامه ۷۸۰»، سمنانی vacâ، vashkâ، سرخه‌ای vacáe، لاسگردی vacáe، vashkâ «رک. ۲ ص ۱۸۵»؛ کودک، فرزند.\nEOF\ngrep -n 'بهاگ\\|بها گ' refs/FSF_pages.txt refs/FSF.txt | head; awk 'BEGIN{RS=\"\\f\"} NR-1>=95 && NR-1<=110 {print NR-1\": \"substr($0,1,150)}' refs/FSF_pages.txt | head -40"
}
```


### [2026-10-17T00:03:02.480Z] TOOL RESULT

```
0001.png
0001.txt
0049.png
refs/FSF_pages.txt:4161:‫اشترهای دوکوهانه و بزرگ از حدود سند‬                      ‫بهاگفت [سیندخت]بگذار بر چشم من‬
refs/FSF_pages.txt:23027:‫(‪)۱-۴۷-۰۱۴‬‬                                       ‫اکوان دیورستم رابرسردست گرفتهبها گووید‪:‬‬
refs/FSF.txt:5515:بهاگفت [سیندخت]بگذار بر چشم من 
refs/FSF.txt:7737:بیاویختند آن بهاگیر تاج 
refs/FSF.txt:7740:ز سر بر گرفت آن بهاگیر تاج 
95:                                                                                       ‫بدگمان‬


        ‫به رستم چنین گفت کای پهلوان‬              ‫(
96: ‫برآمدن‬

            ‫شنیدم که دستان جادوپرست‬                                ‫‪-۴‬نزد؛ پیش‪ .‬هنگام‪:‬‬
‫بهنهگام یازد بهخورشید دست‬                 
97:                                                                                     ‫برآن بودن‬

        ‫به شبگیر هنگام بانگ خروس‬                   
98: ‫بترین نام‬

             ‫یکی انجمن کردم از بخردان‬                            ‫چه مايه بدو اندرون کشتزار‬
 ‫موبدان‬     ‫و هم‬      ‫ستاره‌شناسان‬  
99:                                                                                    ‫برع‬


      ‫‪ ...‬چو برزد سر از برج خرچنگ ماه‬             ‫بدان
100: ‫برز‬


                ‫ی‬‫کر‬
                  ‫ید ه‬
                     ‫خانهٌ خود باز رو‬                                    ‫برخ (به فع اول)‬

101:                                                                                        ‫برزدن‬


            ‫شما جنگ راکس متازید زود‬                
102: ‫برگی‬

                                    ‫برفزود‬   ‫از‬       ‫صهود‬
                                                         ‫قک‬‫منیم‬
         
103:                                                        ‫میان‪ .‬تباه‪ .‬خراب‬
                                                                      ‫ا
104:  ‫برنشست‬
```


## [2026-10-17T00:03:04.036Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 7725,7745p FSF.txt"
}
```


### [2026-10-17T00:03:04.577Z] TOOL RESULT

```
چو دختر بود روشن اشترش نیست 
)1۷-۸4-1( 


بها کیر 


پربهاء گرانبها: «هر چیزی را گویند که 


قیمت و بهای بسیار داشته باشد» (برهان): 
جهاندار بنشست بر تخت عاج 
بیاویختند آن بهاگیر تاج 
(۸هرمزد ۱۵۶) 
بگفت و فرود آمد از خنگ عاج 
ز سر بر گرفت آن بهاگیر تاج 


(FA (۹پرویز‎
```


## [2026-10-17T00:03:07.587Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'WAHAG\\|VAHAG\\|WACHCHAG\\|VACHAK\\|WACHAG\\|VATSA\\|WES-NO\\|WESNO' incoming/ARY/ARY_latin_index_pages.txt | head; grep -n '^بها:\\|^بها \\|^بچه:\\|^بچه ' MON_part1.txt | head"
}
```


### [2026-10-17T00:03:08.104Z] TOOL RESULT

```
3203:BICHUKTI VACHAK, WACHAG (PAHLAVI) 5 hy
14960:ERWAHNEN, GIWAHT WAZ, VACHAK, WAZAG, VAJ,
20489:بچه روم و زنگ: (کد.) 
21251:بچه: (-)(25)۵(.) کودکك» طفل. فرزند؛ 
26006:بچه خصوصا. 
26293:بها: ۰2۳2 [گران‌قیمت] (.) قیمت» ارزش» 
26334:بها گیر: ءآو.." (اا.) هر چیزی که قیمت 
35088:بها ستاند. 
46479:بچه یست: پارو در رفته» آن شی از میان 
72104:بچه دار نده ] (ص فا.) مردی که زن و اولاد 
91334:بها به مشتر 
97065:بچه گوزن و برههای سب بزرگه را به
```


## [2026-10-17T00:03:10.319Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 3190,3215p incoming/ARY/ARY_latin_index_pages.txt; grep -n 'pdf page' incoming/ARY/ARY_latin_index_pages.txt | awk -F: '$1<3203' | tail -1; sed -n 21251,21253p MON_part1.txt; sed -n 26293,26296p MON_part1.txt"
}
```


### [2026-10-17T00:03:10.646Z] TOOL RESULT

```
POKORNY, ——SSsS*~S~«S BABY GERMAN) «galT
BARNHART (BABE, BABY) 70 BABY, BABE ENGLISH) gS&b
ONroNs: (BABY) 67 (OLD CHURCH SLAVIC) oS 531
SKEAT: (BABE, BABYE) 70 BABLU
Lisa dasens dala BABA, BOBOCEM — (SERBIAN) ig po

BOBA, LITHUANIAN) gi\ 3

,

REFERENCES eh BAD ~ (ARMENIAN) ga)
MALLORY & ADAMS: ———~—~=«PAD= PATO SPANISH) gli
iad seb ily PATKA SERBIAN) ype 4.95
BICHUKTI VACHAK, WACHAG (PAHLAVI) 5 hy
CHICHU, (SANSKRIT) ey Sile CHUCHIK, KURDISH) «52,5
— .
[pdf page 113]
BERNIAKAS BALI-
BERNS — (LATVIAN) (4\4) (3) BARN, BAGR (4Lt}(GOTHIC) S35
. _ (4lt}(OLD SCANDINAVIAN) -Si¢-4L41
[pemerces SG] tenn tae
POKORNY: * 131 BARN  (.\#)(OLD SAXON) oS i p-S
BARNHART _ GAIRN) 71 (4ul4}(OLD HIGH ENGLISH) 4S git
MACKENZIE: (CHILD) 106 BOR, BURIAN, BARN
BUCK: 87-93 BYRE,(4j1!}(OLD ENGLISH) oS Si
ONIONS: (BAIRN) 69 BARN, BEARN
3178:[pdf page 112]
بچه: (-)(25)۵(.) کودکك» طفل. فرزند؛ 
ج. بچگان. بچهٌ خور: (کد.) جواهر معدنی از 
لعل» باقوت» طلاه نقره و غیره. بچهٌ خونین: 
بها: ۰2۳2 [گران‌قیمت] (.) قیمت» ارزش» 
ارز» فرح. 

ب‌هاء: 8 (ع. ف. بها] (.) روشنی»
```


## [2026-10-17T00:03:13.661Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 3178,3190p incoming/ARY/ARY_latin_index_pages.txt; grep -n 'pdf page 112\\]' -A30 incoming/ARY/ARY_pages.txt | head -30"
}
```


### [2026-10-17T00:03:14.133Z] TOOL RESULT

```
[pdf page 112]
i,
Wr Cs" See sta oe ae
BABINAT (LATVIAN) (3) gis) BABABA- (SANSKRIT) cy Soile
BEBINT — :(OLD PRUSSIAN) oS gos 9 BABAI (GREEK) 3h y
BABAN CELTIC) (1S) gle BABAE, PAPAE LATIN) 3
BABAN WELSH) 5) BEBE (FRENCH) W313
BABAN AGABLIC) SSE NENE, BEBE (SPANISH) gly
BEBE HALBANIAN) (JT BABBO ITALIAN) gists
(MIDDLE GERMAN) :sls lJ

REFERENCES enthag BOBE, BABE
POKORNY, ——SSsS*~S~«S BABY GERMAN) «galT
3253:[pdf page 112]
3254-0
3255-یه یه (به چم ابچه‌ی کوچک" "نینی") / ۱۱۳
3256-سانسکرپت (8۸80707): 8 لتونی (لتی) (۲۸71۵۸): ادا ادا
3257-بونانی (0760): 8۸3۸1 پروسی کهن ((۶-5514 ۵ا0): ۰ 88817۲7
3258-لانین (/712مل): 5 ,8۸3۸6 سلتی(کلنی) (۴81-716): ۹
3259-فرانسه ([۳8۵۸/6): لد دز ولزی (87 5 ): 1
3260-اسپانیایی (5۸//87): 6 ,۴۴۴ گالیک (0/.لظ0۸): 1۸۸7
3261-ایتالیایی (۷لل74/): 0( آلبائی (۸/4قله): ان زان ز ۱
3262-آلمانی میانه:((0874۸ ۵47005
3263-
3264-8 ,8085 پسگشت‌ها 5
3265-آلمانی (05704۸2): مدا 1 ۸008006
3266-انگلیسی (8(/0/57): 8 ,2۸3 0 (8۸81 ,8۸85) 7
3267-اسلاری کهن (110ها5 )تال ام): 7 (8۸3) :010/5
3268-[ار8۸81 0 (8۸815 ,8۸5) +357
3269-صربی: (5858314(4): ۰ 308021581 ,8۸8۸ لغت‌نامه دهخدا: ۳۳۴۹
3270-
3271-بنرانی (1۷/منال72/): ,808۸
3272-
3273-ا
3274-
3275-ارمنی (/۸48(/1۸): - و۱۱ پسگشت‌ها ار هبار ۲
3276-امپایایی (820ت۶۸(۷ق: ۳70 ۰ 2 :۸0۸/5 4 1۸41082
3277-7 صربی (لففاق38): ه۳۸7 برهان قاطع : ۳۳۳
3278-پهلری (انماتطا): ۲۷۸۲33۸۴ ,۷۸۲۲۲۸۴ یه زا ده ۱
3279-کردی (80/57): ,ت73 سانسکریت (54756777): 11
3280-۰ سس
3281-[pdf page 113]
3282-۴ بخت
```


## [2026-10-17T00:03:22.524Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for a in \"https://en.wiktionary.org/wiki/%D8%A8%DA%86%D9%87|page 552, root Wet: Persian bačče < MP waččag < PIr *wacáh\" \"https://en.wiktionary.org/wiki/%D8%A8%D9%87%D8%A7|page 552, root Wes 5: Persian bahā < MP wahāg < PIE *wes-\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wes-|page 552, root Wes 5: PIE *wes- 'sell', *wos-n̥ price, *wes-ó-s > PIr *waháh > MP wahāg\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wac%C3%A1h|page 552, root Wet: PIr *wacáh 'yearling calf' < PII *watsás, descendants\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wet-|page 552, root Wet: PIE *wet- year\" \"https://en.wiktionary.org/wiki/vatsa|page 552, root Wet: Sanskrit vatsá calf\" \"https://www.etymonline.com/word/vend|page 552, root Wes 5: English vend\" \"https://www.etymonline.com/word/veal|page 552, root Wet: English veal\"; do u=\"${a%%|*}\"; n=\"${a#*|}\"; python3 tools/fetch_source.py \"$u\" --note \"$n\" 2>&1 | tail -1; done"
}
```


### [2026-10-17T00:03:26.715Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/31ae8dd4fbd148c5.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/4d9de86f5f61f02f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/4c8f69f23d3ef8f2.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/10b76db825a91d5d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/9d74262b903ab59d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/5eede17339718955.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/60e1ba836b7cfc5d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c36f7620e59423e3.txt
```


## [2026-10-17T00:03:29.195Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -i -m3 'vatsa\\|calf' 5eede17339718955.txt | cut -c1-300; grep -i -m3 'vend' 60e1ba836b7cfc5d.txt | cut -c1-400; grep -i -m2 'vitellus' c36f7620e59423e3.txt | cut -c1-400; grep -c . 31ae8dd4fbd148c5.txt"
}
```


### [2026-10-17T00:03:29.550Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/vatsa
TITLE: vatsa - Wiktionary, the free dictionary
vatsa - Wiktionary, the free dictionary 
URL: https://www.etymonline.com/word/vend
408
```


## [2026-10-17T00:03:36.418Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"Preis\\|Wert'\" HRN.txt | head; grep -n \"Preis\" HUB.txt | head -5; grep -n -i \"vahāk\\|vahak\\|wahag\\|vahâk\" NYB_vol2_glossary.txt CHEUNG.txt | head"
}
```


### [2026-10-17T00:03:36.896Z] TOOL RESULT

```
432:Preisaufgabe für das Jahr 1892/93 (nach den Zeitungsmitteilungen) *eine
1040:67. erj.'Wert' (Sahn. I, 2 Vers 16), erjmend.
1041:aw. arejah- 'Preis, Wert'; phlv. arj^ arjniand;
1042:ai. vergl. arghd- 'Preis, Wert'.
1045:gybis ^^^ 'Wert', erzan^ erzänis, erzTden,
2476:242. behä 'Wert'.
2480:Wert', lat. venum 'Verkauf, arm. gin ^Kaufpreis' (H.
8507:978. muzd, muzd 'Lohn, Preis', muzde {mizde) 'frohe Bot-
8915:1027. nirx, nerx "Preis, Wert' (z. B. Schefer, Chresto-
2131:arm. LW. druat in druati-R 'Lob, Preis, Lobeserhebung ,
5985:'Lebewohr, arm.drwo^-iSXobjPreis', ap.*rfwrw-
7017:wicht*; muzd, muzd *Lohn, Preis' = zd. mlzda, ksl. mtzda,
8150:z oder z: muzd^ muzd Lohn, Preis*, muzda (mizda) frohe
9528:narx 'Preis', afgh. LW. nirx *Preis-
```


## [2026-10-17T00:03:38.943Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 2474,2490p HRN.txt; awk 'BEGIN{RS=\"\\f\"} /242. behä/ {print \"leaf\",NR-1}' HRN.txt; grep -n '^ *242\\.' HUB.txt | head -3"
}
```


### [2026-10-17T00:03:41.076Z] TOOL RESULT

```
pih ist in dem Verse aus den HQ. bei Vullers aller-
dings durch den Reim auf bih gesichert.
242. behä 'Wert'.
phlv. vahak (AV.).
Spiegel, Ar, Periode 93 vergleicht ai. vasnd-
'Kaufpreis, Wert*. Dazu gehören gr. wvog 'Kaufpreis,
Wert', lat. venum 'Verkauf, arm. gin ^Kaufpreis' (H.
No. 69), ksl. vöno 'Mitgift*.
Doch muss man zwei Grundformen annehmen,
indog. *vesO' und ^vesno- bezw. H'eno-, Auf ^veso-
{*vesäkO') geht np. behä zurück, während ksl. veno ein
"^vBno- (nicht ^vesno-, sn hätte im Ksl. erhalten bleiben
müssen) voraussetzt; für arm. gin gilt wohl dasselbe
wie für vSno {i = B). Gr. wvvg kann aus *(jjavog ent-
standen sein, braucht es aber nicht (vergl. Solmsen,
KZ. 29, 81 folg.). Diese sprachliche Bemerkung ist
*) Die Wörterbücher geben pe(hj sonst eine gerade entgegen-
leaf 76
1050:242. Die Suffixe np. a, a, t, U, o =■- phi. afe, Oi, Fi, uk, dk,
```


## [2026-10-17T00:03:44.068Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'behä\\|bahä\\|vahäk' HUB.txt | head"
}
```


### [2026-10-17T00:03:44.441Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:05:48.120Z] TOOL CALL #47: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-552.py <<'PYEOF'\nimport json\nW_BAHA=\"https://en.wiktionary.org/wiki/%D8%A8%D9%87%D8%A7\"\nW_BACE=\"https://en.wiktionary.org/wiki/%D8%A8%DA%86%D9%87\"\nW_WES=\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wes-\"\nW_WAC=\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wac%C3%A1h\"\nW_WET=\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wet-\"\n\nPOK1173={\"ref\":\"POK:1173\",\"status\":\"supports\",\"note\":\"POK_full.txt l.92523ff. 'Root / lemma: ues-no- (*h2ues-no-) / Meaning: price / Material: ... Old Indic vasna- m. purchase price ... Armenian gin ... gr. hom. ōnos purchase price ... Latin venus (only in Akk. venum, Dat. veno ...) sale (vendo, -dere sell is *venom + do ...) ... Hittite ussaniya- sell (compare above uas- buy) ... References: WP. I 311 f. ... Page(s): 1173'. Note: Pokorny's '5. ues-' (pp. 1172-1173) is 'to dress, put on'; the 'buy' root is cited there only as Hitt. uas-.\"}\nPOK1175={\"ref\":\"POK:1175\",\"status\":\"supports\",\"note\":\"POK_full.txt l.92688ff. 'Root / lemma: uet- (*h1uet-) / Meaning: year / Material: Old Indic vatsa-, vatsara- m. year, vatsa- m. yearling, calf ... Latin vetus, -eris old ... vetulus ... Latin veterinus Zugvieh; vitulus calf = Umbrian vitluf ... Page(s): 1175'. No Iranian/Persian form is listed.\"}\nOEW_NC=lambda r:{\"ref\":r,\"status\":\"not_checked\",\"note\":\"OEW (Shipley, The Origins of English Words) is lending-only on archive.org (djvu text 401); no local copy.\"}\nAEF_NC={\"ref\":\"AEF:302\",\"status\":\"not_checked\",\"note\":\"AEF (Persian translation of Horn/Hübschmann) is not online; checked the underlying Horn entry instead: HRN no. 242 p. 55 (see consulted).\"}\nWLD311={\"src\":\"WLD\",\"where\":\"Bd. I 311 (WLD_Bd1_pages.txt leaf 319, l.29652ff.)\",\"stance\":\"supports\",\"note\":\"'uesno- „Kaufpreis“. Bei den einzelnen Sprachen schwankt e- und o-Vokalismus. Ai. vasnáh „Kaufpreis“ ... vasnayati „feilscht“; gr. hom. ōnos „Kaufpreis“ ... Lat. venus nur im akk. venum, dat. veno ... „Verkauf“; vendo, -dere „verkaufen“ ist *venom do'.\"}\nAHDwes={\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. wes-1 (AHD_watkins1985.txt l.1159)\",\"stance\":\"supports\",\"note\":\"'wes-1. To buy. 1. Suffixed form *wes-no- in Latin vēnum, sale: VENAL, VEND. 2. Suffixed o-grade form *wos-nā- in Greek ōneisthai, to buy ... [Pok. 8. wes- 1173.]'\"}\nIECwes={\"src\":\"IEC\",\"where\":\"s.v. uesnom (IEC.txt l.20184)\",\"stance\":\"supports\",\"note\":\"'uesnom (uosnom) price. Cf. ues- (1). WP I, 311 Skt. vasnám ... Arm. gin ... Lat. venum in — dare sell; venus ... sale'.\"}\nWLD251={\"src\":\"WLD\",\"where\":\"Bd. I 251 (WLD_Bd1_pages.txt leaf 259, l.23402ff.)\",\"stance\":\"supports\",\"note\":\"'uet- „Jahr“, -uetes- n. ds., *uetos(o)- „jährig, alt“; in Ableitungen auch für jährige, junge Tiere. Ai. vatsá-, vatsará- m. „Jahr“, vatsá- m. „Jährling, Kalb, Kind“ ... lat. veterīnus „Zugvieh“; vitulus „Kalb“ = umbr. vitluf'.\"}\nAHDwet={\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. wet-2 (AHD_watkins1985.txt l.1166)\",\"stance\":\"supports\",\"note\":\"'wet-2. Year. ... 2. Suffixed form *wet-es- in: a. Latin vetus, old (< \\\"having many years\\\"): VETERAN ... b. Latin veterīnus, of beasts of burden, of cattle (perhaps chiefly old cattle): VETERINARY ... 3. Suffixed form *wet-olo- in Latin vitulus, calf, yearling: VEAL, VITELLUS. [Pok. wet- 1175.]'\"}\nIECwet={\"src\":\"IEC\",\"where\":\"s.vv. uetesios, uetos (IEC.txt l.20206, 20212)\",\"stance\":\"supports\",\"note\":\"'uetesios ... year-old, annual; yearling. WP I, 251 Skt. vatsáh, m. calf, young animal, child ... Lat. vetus'; 'uetos, -es- year, age ... Skt. vatsáh yearling calf ... Oss. cf. wäs calf'.\"}\nHRN184={\"src\":\"HRN\",\"where\":\"no. 184, p. 43 (HRN.txt leaf 64)\",\"stance\":\"contradicts\",\"note\":\"'184. bačče, baččе Junges (von Tier und Menschen) ... phlv. vačak, bačak ... oss. d. wæss Kalb; bal. gvask Kalb ... Da np. č nicht für skr. ts stehen kann, so ist die Zusammenstellung mit ai. vatsá- Kalb, Jährling unzulässig; das letztere Wort entspricht vielmehr np. gōsāle (No. 941).'\"}\nHUB184={\"src\":\"HUB\",\"where\":\"no. 184, p. 26 (HUB.txt leaf 36, l.824ff.)\",\"stance\":\"contradicts\",\"note\":\"'184. Np. bača, bačča Junges, Kind = phl. vačak (aus *vaččak ...) ist zunächst zu trennen von osset. wæss Kalb, bal. gvask Kalb ... wax. vušk, sar. višk Kalb, die auf iran. *vasa- ~ skr. vatsá- Kalb ... zurückgehen und einem np. *vah entsprechen würden'.\"}\nBQT237={\"src\":\"BQT\",\"where\":\"vol. 1 p. 237, footnote 5 (archive.org borhan-ghate-v1 leaf n457; read from image, saved to ocr/BQT/237.vision.txt)\",\"stance\":\"partial\",\"note\":\"Mo'in: 'بچه - بفتح اول و دوم، پهلوی vacak «تاوادیا ۹۱۶۶»، بندهش ۱۱۲، طبری vaca ... سمنانی vacâ، vashkâ، سرخه‌ای vacáe ...؛ کودک، فرزند.' Gives Pahlavi vačak and dialect forms; no derivation from *vatsa-.\"}\n\nentries=[]\ne0={\"entry\":0,\"root\":\"Wes 5, Wes-no, Wesn, Veso, Věno, Vesno\",\"verdict\":\"confirmed\",\n\"modern_form\":\"PIE *wes- 'to buy, sell' (LIV² 2.*u̯es-; Hitt. wāš-), with *wes-no- / *wos-n̥ 'price, sale' (Pokorny 1173 u̯esno-; AHD wes-1)\",\n\"note\":\"The root and its glosses are right: PIE *wes- 'buy/sell' is continued by Hittite wāš- 'buy' and ušnai- 'put up for sale', and *wes-no- / *wos-no- 'price' by Skt. vasná-, Arm. gin, Gk. ōnos, Lat. vēnum, OCS věno. 'Wes 5' is Nourai's own homonym number (Pokorny numbers 5. u̯es- as 'to dress'; AHD calls the buy-root wes-1). The label 'Wesn: sell' is loose: the n-stem means 'price/sale', and 'sell' is Latin vēnum dare > vendere. The forms 'Veso, Věno, Vesno' at the bottom of the box are Horn's (no. 242): *veso- (> MP wahāg) beside *vesno-/*věno-. Wiktionary agrees: PIE *wes-ó-s 'selling, trade' > PIr *waháh > MP wahāg > NP bahā. The extraction matches the printed page.\",\n\"note_fa\":\"ریشهٔ هندواروپایی آغازین *wes- «خریدن، فروختن» با ساخت *wes-no- / *wos-no- «بها، قیمت» در پوکورنی (ص ۱۱۷۳)، والده-پوکورنی (ج ۱، ص ۳۱۱) و واتکینز آمده است. بازمانده‌های آن سنسکریت vasná- «بهای خرید»، ارمنی gin، یونانی ōnos و لاتینی vēnum «فروش» است. «بها»ی فارسی از ستاک بی‌پسوند *wes-o- می‌آید و نه از ساخت n-دار، چنان‌که هرن هم گفته است. ریشه و معنایی که نورایی داده درست است. فقط «Wesn: فروختن» دقیق نیست، زیرا ساخت n-دار به معنی «بها، فروش» است.\",\n\"sources\":[W_WES,W_BAHA],\n\"ref_check\":[POK1173,OEW_NC(\"OEW:440\"),AEF_NC],\n\"consulted\":[WLD311,AHDwes,IECwes,\n {\"src\":\"KLN\",\"where\":\"s.v. venal (KLN_1966.txt l.41187)\",\"stance\":\"supports\",\"note\":\"'... cogn. with OI. vasnáḥ, purchase money, vasnám, reward, vasnayati, he bargains, haggles, Arm. gin (for *wesnom), purchase money, Gk. ōnē ... Hitt. ushshaniya-, to sell, and — without the suff. -no — wash-, to buy.'\"}],\n\"nodes\":[\n {\"id\":1,\"lang\":\"Pahlavi\",\"words\":\"vah-âk\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Middle Persian wahāg [whʾk'] 'trading; value' (MacKenzie), Manichaean wh'g, is the source of NP bahā. It goes back to Old Iranian *wahāka-, built with the suffix -āka- on *waha- < Indo-Iranian *wasa- < PIE *wes-o- 'selling, trade'; PIr intervocalic *s became h. Horn (no. 242) gives 'phlv. vahāk' and derives it from *vesāko- / *veso-, without the n-suffix of Skt. vasna-. Nourai's 'vah-âk' is a faithful older transliteration of wahāg.\",\n  \"derivation_fa\":\"واژهٔ پهلوی wahāg (در خط پهلوی whʾk) به معنی «داد و ستد، ارزش» در فرهنگ مکنزی آمده است. این واژه از ایرانی باستان *wahāka- است، که با پسوند -āka- از *waha- ساخته شده و *waha- از هندواروپایی *wes-o- «فروش» می‌آید. s ایرانی آغازین میان دو واکه به h بدل شده است. هرن هم صورت پهلوی vahāk را آورده است. ادعای نورایی درست است.\",\n  \"sources\":[W_BAHA,W_WES],\n  \"ref_check\":[AEF_NC],\n  \"consulted\":[\n   {\"src\":\"PHD\",\"where\":\"p. 91 (PHD.txt leaf 112; PHD_mackenzie.txt l.5139)\",\"stance\":\"supports\",\"note\":\"'wahāg [whʾk' | M wh'g, N bahā] trading; value. ~ burdan: value, estimate.'\"},\n   {\"src\":\"HRN\",\"where\":\"no. 242, p. 55 (HRN.txt leaf 76, l.2476ff.)\",\"stance\":\"supports\",\"note\":\"'242. behā Wert. phlv. vahāk (AV.) ... Auf *veso- (*vesāko-) geht np. behā zurück, während ksl. věno ein *věno- ... voraussetzt'.\"},\n   {\"src\":\"NYB\",\"where\":\"NYB_vol2_glossary.txt\",\"stance\":\"silent\",\"note\":\"grep 'wahāk|wahak|vahāk' found no entry in the OCR.\"}]},\n {\"id\":2,\"lang\":\"Persian\",\"words\":\"bahâ; bahâ-gîr\",\"verdict\":\"confirmed\",\n  \"derivation\":\"NP bahā 'price, value' is the regular continuation of MP wahāg. Initial w- became b- in early New Persian (cf. wahār > bahār), and the final -āg was dropped (as in wahār, dānāg > dānā). bahā-gīr 'valuable, precious' is a Persian compound of bahā + gīr, the present stem of giriftan 'to take, hold', so it means 'holding (much) value'. It occurs in the Shahnameh line quoted by Nourai ('biyāvīxtand ān bahā-gīr tāj', Hormozd 156; Noushin's Shahnameh glossary). Borhan glosses it 'anything that has great price and value'. The homonym bahā' 'splendour' is Arabic and unrelated.\",\n  \"derivation_fa\":\"«بها» به معنی «قیمت، ارزش» دنبالهٔ منظم پهلوی wahāg است. w آغازین در فارسی دری به b بدل شده است، مانند wahār که «بهار» شده. پایانهٔ -āg هم افتاده است. «بهاگیر» به معنی «گران‌بها» ترکیبی فارسی از «بها» و «گیر» است. «گیر» ستاک حال «گرفتن» است، پس «بهاگیر» یعنی «دارای بهای بسیار». این واژه در بیت شاهنامه (پادشاهی هرمزد) آمده است و برهان قاطع آن را «هرچیزی که قیمت و بهای بسیار داشته باشد» معنی کرده است. «بهاء» عربی به معنی «روشنی» ربطی به این واژه ندارد. ادعای نورایی درست است.\",\n  \"sources\":[W_BAHA],\n  \"ref_check\":[AEF_NC,\n   {\"ref\":\"FSF:91\",\"status\":\"supports\",\"note\":\"FSF.txt l.7729ff. (Noushin, Vāženāme-ye Šāhnāme) s.v. بهاگیر: 'پربها، گرانبها: «هر چیزی را گویند که قیمت و بهای بسیار داشته باشد» (برهان): جهاندار بنشست بر تخت عاج / بیاویختند آن بهاگیر تاج (۸ هرمزد ۱۵۶)'. Same verse Nourai quotes; page number not mapped in this scan.\"}],\n  \"consulted\":[\n   {\"src\":\"HRN\",\"where\":\"no. 242, p. 55\",\"stance\":\"supports\",\"note\":\"'242. behā Wert. phlv. vahāk ... Auf *veso- (*vesāko-) geht np. behā zurück'.\"},\n   {\"src\":\"BQT\",\"where\":\"vol. 1 ≈ p. 323 (BQT_v1_pages.txt leaf 543, l.21858)\",\"stance\":\"supports\",\"note\":\"'بها گیر با کاف فارسی بر وزن تباشیر، هرچیزی را گویند که قیمت و بهای بسیار داشته باشد'; also 'بهاور ... بمعنی بهاگیر است'.\"},\n   {\"src\":\"MON\",\"where\":\"MON_part1.txt l.26293, 26334 (2-vol. abridgement)\",\"stance\":\"supports\",\"note\":\"'بها ... (اِ.) قیمت، ارزش، ارز' (with a separate Arabic بهاء 'روشنی'); 'بها گیر ... هر چیزی که قیمت بسیار داشته باشد؛ قیمتی، گرانبها'.\"},\n   {\"src\":\"HUB\",\"where\":\"HUB.txt\",\"stance\":\"silent\",\"note\":\"grep 'behä|bahä|vahäk' found nothing.\"}]},\n {\"id\":3,\"lang\":\"Latin\",\"words\":\"věnum; ven-dere\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Latin vēnum (acc.; dat. vēnō, later vēnuī) 'sale' is from *wes-no- / *wos-no-: *-sn- was simplified to -n- with compensatory lengthening, so *wesnom > vēnum. vendere 'to sell' is a univerbation of vēnum dare 'to give for sale' (the older venumdare is attested). Its partner vēnīre 'to be sold' is vēnum īre. Nourai's breve in 'věnum' is a misprint for the macron (vēnum); this is a minor diacritic slip in the book.\",\n  \"derivation_fa\":\"لاتینی vēnum «فروش» از *wes-no- است. خوشهٔ -sn- ساده شده و واکهٔ پیش از آن کشیده شده است. فعل vendere «فروختن» از پیوستن vēnum dare «به فروش دادن» پدید آمده است. همسان آن vēnīre «فروخته شدن» هم از vēnum īre ساخته شده. نشانهٔ کوتاهیِ روی e در کتاب لغزشی چاپی است و صورت درست vēnum است. ادعای نورایی درست است.\",\n  \"sources\":[W_WES],\n  \"ref_check\":[{\"ref\":\"AHD:1550\",\"status\":\"supports\",\"note\":\"1976 page not online; the same root in Watkins 1985 (AHD_watkins1985.txt l.1159): 'wes-1. To buy. 1. Suffixed form *wes-no- in Latin vēnum, sale: VENAL, VEND.'\"},OEW_NC(\"OEW:440\")],\n  \"consulted\":[WLD311,\n   {\"src\":\"KLN\",\"where\":\"s.v. vend (KLN_1966.txt l.41189)\",\"stance\":\"supports\",\"note\":\"'vend ... F. vendre, fr. L. vendere, to sell, shortened fr. venundare, fr. venum dare, lit. to give (i.e. offer) for sale, fr. venum or venus, sale, and dare, to give.'\"},\n   {\"src\":\"POK\",\"where\":\"p. 1173 u̯esno-\",\"stance\":\"supports\",\"note\":\"'Latin venus (only in Akk. venum, Dat. veno, later venui) sale (vendo, -dere sell is *venom + do, veneo ... = *venom + eo)'.\"}]},\n {\"id\":4,\"lang\":\"English\",\"words\":\"vend, vendor\",\"verdict\":\"confirmed\",\n  \"derivation\":\"English vend (early 17th c.) comes from French vendre < Latin vendere. vendor comes from Anglo-French vendour (OF vendeur) < Latin venditōrem, the agent noun of venditus, past participle of vendere. Related learned borrowings are venal (< vēnālis) and vendible.\",\n  \"derivation_fa\":\"انگلیسی vend در آغاز سدهٔ هفدهم از فرانسوی vendre وام گرفته شد، که از لاتینی vendere است. vendor «فروشنده» از فرانسوی-انگلیسی vendour است، که از لاتینی venditor «فروشنده» می‌آید. ادعای نورایی درست است.\",\n  \"sources\":[],\n  \"ref_check\":[OEW_NC(\"OEW:440\")],\n  \"consulted\":[\n   {\"src\":\"KLN\",\"where\":\"s.vv. vend, vendor (KLN_1966.txt l.41189, 41201)\",\"stance\":\"supports\",\"note\":\"'vend ... F. vendre, fr. L. vendere'; 'vendor, n. — AF. vendour, vendor, fr. OF. (= F.) vendeur, fr. L. venditōrem, acc. of venditor, seller, fr. venditus, pp. of vendere.'\"},\n   {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. wes-1\",\"stance\":\"supports\",\"note\":\"'*wes-no- in Latin vēnum, sale: VENAL, VEND.'\"},\n   {\"src\":\"SKT\",\"where\":\"SKT.txt\",\"stance\":\"silent\",\"note\":\"grep '^Vend' found no headword in the noisy OCR of the concise Skeat.\"}]}\n]}\nentries.append(e0)\n\ne7={\"entry\":7,\"root\":\"Wet\",\"verdict\":\"confirmed\",\n\"modern_form\":\"PIE *wet- 'year' (Pokorny 1175 u̯et-; AHD wet-2; Hitt. witt-); derivatives *wet-es- 'year', *wet-so- 'yearling', *wet-olo- 'yearling'\",\n\"note\":\"Root and gloss are correct and textbook: Gk. (w)étos 'year', Hitt. witt-, Lat. vetus 'old' (originally 'of many years'), vitulus 'calf', veterīnus, Skt. vatsá- 'yearling, calf'. The Latin/English branch is right. The Iranian branch is the weak part. (1) 'Iranian vasa' is the PIr *wasa- / *wacá- 'calf' of Oss. wæss and Wakhi wušk, but it means 'calf', not 'young child'. (2) The Pahlavi box prints 'vhat-čak, cačak' for MP waččag / vačak (wck'). (3) Nourai's own cited Horn (no. 184) and Hübschmann (no. 184) both reject linking bačče with Skt. vatsá-, because NP č cannot continue ts. Wiktionary nevertheless derives بچه from MP waččag < PIr *wacáh 'calf'. (4) Sanskrit 'vasta' is a misprint for vatsá- (Skt. vasta- means 'he-goat'). The extraction matches the printed page (site/pages/552.jpg; copy at sources/refs/ocr/BOOK/552.png).\",\n\"note_fa\":\"ریشهٔ هندواروپایی آغازین *wet- «سال» در پوکورنی (ص ۱۱۷۵)، والده-پوکورنی (ج ۱، ص ۲۵۱) و واتکینز آمده است. بازمانده‌های آن یونانی étos «سال»، هیتی witt-، لاتینی vetus «کهن» و vitulus «گوساله» و سنسکریت vatsá- «یکساله، گوساله» است. ریشه و شاخهٔ لاتینی-انگلیسی درست است. ولی شاخهٔ ایرانی جای بحث دارد. هرن و هوبشمان، که خود نورایی به آن‌ها ارجاع داده، پیوند «بچه» با vatsá- سنسکریت را نمی‌پذیرند، زیرا چ فارسی نمی‌تواند دنبالهٔ ts باشد. ویکی‌واژه با این همه «بچه» را از پهلوی waččag و ایرانی آغازین *wacáh «گوساله» می‌داند. صورت‌های «vhat-čak، cačak» و «vasta» هم لغزش چاپی کتاب است.\",\n\"sources\":[W_WET,W_WAC,W_BACE],\n\"ref_check\":[POK1175,OEW_NC(\"OEW:441\")],\n\"consulted\":[WLD251,AHDwet,IECwet,\n {\"src\":\"KLN\",\"where\":\"s.v. veal (KLN_1966.txt l.41153, leaf 898)\",\"stance\":\"supports\",\"note\":\"'... L. vitellus, dimin. of vitulus, calf ... cogn. with OI. vatsáḥ, calf. The orig. meaning of these words was yearling, fr. I.-E. base *wet, year, whence also Gk. étos ... L. vetus, old.'\"}],\n\"nodes\":[\n {\"id\":1,\"lang\":\"Iranian\",\"words\":\"vasa\",\"verdict\":\"plausible\",\n  \"derivation\":\"Proto-Iranian *wacá- (*watsa-), later *wasa- 'calf, yearling' (< Indo-Iranian *watsás = Skt. vatsá-, from PIE *wet-so-), is well established. It survives in Ossetic wæss 'calf', Balochi gwask, Wakhi wušk, Sarikoli višk, Kurdish gîsk and Khotanese basaka-. Hübschmann reconstructs exactly 'iran. *vasa-'. Two problems remain. The gloss 'one year old, young child' is not supported: the Iranian word means 'calf/kid'. And Hübschmann himself says this *vasa- would give NP *vah, not bačče, so the arrow to the Pahlavi box is doubtful (see #2-3).\",\n  \"derivation_fa\":\"ایرانی آغازین *wacá- یا *wasa- به معنی «گوساله، یکساله» شناخته شده است. این واژه از هندوایرانی *watsás (همان سنسکریت vatsá-) و از هندواروپایی *wet-so- است. بازمانده‌های آن آسی wæss «گوساله»، بلوچی gwask، وخی wušk و کردی gîsk است. ولی معنی «کودک» برای آن گواه ندارد. هوبشمان می‌گوید این واژه در فارسی به *vah می‌رسید و نه به «بچه». پس واژه پذیرفتنی است، ولی پیکان آن به «بچه» محل تردید است.\",\n  \"sources\":[W_WAC],\n  \"ref_check\":[{\"ref\":\"HRN:43\",\"status\":\"contradicts\",\"note\":\"Horn p. 43 no. 184 lists oss. wæss Kalb, bal. gvask Kalb, wax. vušk beside bačče but concludes: 'Da np. č nicht für skr. ts stehen kann, so ist die Zusammenstellung mit ai. vatsá- Kalb, Jährling unzulässig; das letztere Wort entspricht vielmehr np. gōsāle (No. 941).'\"}],\n  \"consulted\":[HUB184,IECwet,\n   {\"src\":\"BRT\",\"where\":\"BRT.txt\",\"stance\":\"silent\",\"note\":\"no Avestan *vasa-/*vaca- 'calf' found (grep 'Kalb'); the form is only reconstructed from the modern languages.\"}]},\n {\"id\":2,\"lang\":\"Pahlavi\",\"words\":\"vhat-čak, cačak\",\"verdict\":\"transcription_suspect\",\n  \"error_in\":\"book\",\"book_prints\":\"vhat-čak, cačak\",\"correct_form\":\"waččag (vačak, wck')\",\n  \"derivation\":\"The Middle Persian word is waččag [wck', also bck'] 'child, baby, cub' (MacKenzie). Horn and Mo'in cite it as vačak, Horn also as bačak. It is the direct ancestor of NP bačče/bača. The book prints 'vhat-čak, cačak'. 'vhat-čak' is not an attested form: it appears to be Nourai's etymologizing respelling, inserting the -t- of Skt. vatsa. 'cačak' is a misprint for vačak. The extraction faithfully reproduces the page. The word itself is real and the edge to #3 is correct; the edge from Iranian *vasa- is the contested part (see #1 and #3).\",\n  \"derivation_fa\":\"واژهٔ پهلوی waččag (در خط پهلوی wck' و bck') به معنی «کودک، نوزاد، تولهٔ جانور» در فرهنگ مکنزی آمده است. هرن و معین آن را vačak خوانده‌اند. این واژه نیای مستقیم «بچه»ی فارسی است. ولی کتاب «vhat-čak، cačak» چاپ کرده است. vhat-čak در هیچ متنی نیامده و گویا خود نورایی آن را با افزودن t از vatsa ساخته است. cačak هم لغزش چاپی به جای vačak است. خطا در خود کتاب است و نه در خوانش اسکن.\",\n  \"sources\":[W_BACE],\n  \"ref_check\":[{\"ref\":\"HRN:43\",\"status\":\"partial\",\"note\":\"Horn p. 43 no. 184: 'phlv. vačak (vd. 14 (53) Gl.), bačak (vd. 19 (99) Gl.)' — confirms the Pahlavi word (not 'vhat-čak'/'cačak') but rejects the link with Skt. vatsá-.\"},\n   {\"ref\":\"HUB:26\",\"status\":\"partial\",\"note\":\"Hübschmann p. 26 no. 184: 'Np. bača, bačča Junges, Kind = phl. vačak (aus *vaččak ...)' — confirms Pahlavi vačak but says it 'ist zunächst zu trennen' from Oss. wæss, Bal. gvask < iran. *vasa- ~ skr. vatsá-.\"}],\n  \"consulted\":[\n   {\"src\":\"PHD\",\"where\":\"p. 90 (PHD.txt leaf 111; PHD_mackenzie.txt l.5112)\",\"stance\":\"supports\",\"note\":\"'waččag [wck', (bck') | N bačča] child, baby, cub.' — the attested form; no 'vhat-čak'.\"},\n   {\"src\":\"NYB\",\"where\":\"NYB_vol2_glossary.txt\",\"stance\":\"silent\",\"note\":\"grep 'wačak|waččak|vačak|wacak' found nothing in the OCR.\"},\n   BQT237]},\n {\"id\":3,\"lang\":\"Persian\",\"words\":\"bačeh\",\"verdict\":\"plausible\",\n  \"derivation\":\"NP bačče / bača 'child, young (of animals)' continues MP waččag (wck'), with early NP w- > b- and loss of final -g. Dialect forms are Tabari vača, Semnani vačā/vaškā and Gilaki vača (Mo'in in Borhan p. 237; Horn no. 184). The question is what lies behind waččag. Horn and Hübschmann (both cited by Nourai) reject a link with Skt. vatsá- / Iran. *vasa- 'calf', because Old Iranian *ts gives s/h in Persian, never č (cf. MP wahīg 'kid' from the same *wacá-). Wiktionary nevertheless gives MP waččag < PIr *wacáh 'calf', treating the geminate čč as expressive. So the chain MP → NP is certain, while the ultimate attachment to PIE *wet- is possible but phonologically irregular and not generally accepted.\",\n  \"derivation_fa\":\"«بچه» (بَچّه، بَچه) دنبالهٔ پهلوی waččag است. w آغازین در فارسی دری به b بدل شده و g پایانی افتاده است. گونه‌های گویشی تبری vača و سمنانی vačā و vaškā را معین در حاشیهٔ برهان قاطع (ص ۲۳۷) آورده است. پیوند پهلوی به فارسی قطعی است. ولی هرن و هوبشمان رسیدن این واژه به vatsá- سنسکریت و *wet- هندواروپایی را نمی‌پذیرند. دلیلشان این است که ts ایرانی باستان در فارسی به s یا h می‌رسد و نه به چ، چنان‌که در پهلوی wahīg «بزغاله» دیده می‌شود. ویکی‌واژه این پیوند را با فرض تشدید عاطفی می‌پذیرد. پس سخن نورایی با احتیاط پذیرفتنی است.\",\n  \"sources\":[W_BACE,W_WAC],\n  \"ref_check\":[{\"ref\":\"BQT:237\",\"status\":\"partial\",\"note\":\"Borhan vol. 1 p. 237, Mo'in's footnote 5 (read from image, archive.org borhan-ghate-v1 leaf n457; saved ocr/BQT/237.vision.txt): 'بچه - بفتح اول و دوم، پهلوی vacak ... طبری vaca ... سمنانی vacâ، vashkâ ...؛ کودک، فرزند' — supports MP→NP, says nothing of *wet-/vatsa.\"},\n   {\"ref\":\"HRN:26\",\"status\":\"not_found\",\"note\":\"Horn p. 26 (leaf 47) is in the ā- section; the bačče entry is no. 184 on p. 43, which contradicts the vatsa link (see node #1). HRN:26 looks like a confusion with HUB:26.\"}],\n  \"consulted\":[HRN184,HUB184,\n   {\"src\":\"MON\",\"where\":\"MON_part1.txt l.21251 (2-vol. abridgement)\",\"stance\":\"silent\",\"note\":\"'بچه ... کودک، طفل، فرزند؛ ج. بچگان' — no etymology in the abridgement.\"},\n   {\"src\":\"ARY\",\"where\":\"p. 113 (pdf 112; ARY_latin_index_pages.txt l.3203)\",\"stance\":\"contradicts\",\"note\":\"Aryanpur lists Pahlavi 'VACHAK, WACHAG' on the page of nursery words (BABA, BABY, BEBE ...; Sanskrit CHICHU, Kurdish CHUCHIK), i.e. not under *wet-; OCR is rough, the reading is approximate.\"}]},\n {\"id\":4,\"lang\":\"Sanskrit\",\"words\":\"vasta\",\"verdict\":\"transcription_suspect\",\n  \"error_in\":\"book\",\"book_prints\":\"vasta\",\"correct_form\":\"vatsá-\",\n  \"derivation\":\"The Sanskrit cognate is vatsá- 'calf, yearling; child' (also vatsará- 'year', vatsaka- 'little calf'). It comes from PIE *wet-so- 'yearling', with the -ts- cluster kept. The book prints 'vasta : young'. This is a metathesis/misprint for vatsa: Sanskrit vasta- (basta-) exists but means 'he-goat' and does not belong here. The gloss 'young' loosely renders 'yearling'. Skeat, Nourai's cited source, has 'Skt. vatsa, a calf, properly a yearling' under veal.\",\n  \"derivation_fa\":\"هم‌ریشهٔ سنسکریت این واژه vatsá- به معنی «گوساله، یکساله، کودک» است. vatsará- «سال» هم از همین ریشه است. هر دو از هندواروپایی *wet-so- «یکساله» می‌آیند. کتاب «vasta» چاپ کرده است. این لغزش چاپی (جابه‌جایی t و s) به جای vatsa است. vasta- در سنسکریت به معنی «بز نر» است و به این ریشه ربطی ندارد. خطا در خود کتاب است.\",\n  \"sources\":[W_WET],\n  \"ref_check\":[{\"ref\":\"SKT:592\",\"status\":\"supports\",\"note\":\"Local Skeat is the Concise ed.; s.v. Veal on p. 546 (SKT.txt leaf 566, l.20631): 'Veal ... L. uitellus, dimin. of uitulus, a calf. + Gk. italos, a calf; Skt. vatsa, a calf, properly a yearling, from Gk. etos, a year' (OCR noisy). Page 592 refers to another edition; the content supports vatsa, not 'vasta'.\"}],\n  \"consulted\":[WLD251,\n   {\"src\":\"POK\",\"where\":\"p. 1175 u̯et-\",\"stance\":\"supports\",\"note\":\"'Old Indic vatsa, vatsara- m. year, vatsa- m. yearling, calf, vatsaka- m. little calf'.\"},\n   {\"src\":\"KLN\",\"where\":\"s.v. veal\",\"stance\":\"supports\",\"note\":\"'cogn. with OI. vatsáḥ, calf'.\"}]},\n {\"id\":5,\"lang\":\"Latin\",\"words\":\"vitulus; vetus; veterinus\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Latin vetus, veteris 'old' is from the s-stem *wet-es- 'year' (= Gk. étos), originally 'having many years'. veterīnus 'of draught/burden animals' (from *wetes-īno-, perhaps 'old, i.e. full-grown cattle') is built on the same stem. vitulus 'calf' (Umbr. vitluf) is from *wet-olo- 'yearling' (cf. Gk. étalon 'yearling'). Its i for e is unexplained: Pokorny suggests a loan from another Italic dialect, and Mann calls it problematic. All three words and glosses are right.\",\n  \"derivation_fa\":\"لاتینی vetus «کهن» از ستاک *wet-es- «سال» است، همان یونانی étos، و در اصل یعنی «پرسال». veterīnus «چارپای باربر» هم از همین ستاک ساخته شده است. vitulus «گوساله» از *wet-olo- «یکساله» است. i به جای e در این واژه هنوز روشن نیست و پوکورنی آن را وام از گویشی دیگر می‌داند. ادعای نورایی درست است.\",\n  \"sources\":[W_WET],\n  \"ref_check\":[OEW_NC(\"OEW:441\"),{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 wet-2: '*wet-es- in Latin vetus, old (< having many years) ... Latin veterīnus, of beasts of burden, of cattle (perhaps chiefly old cattle) ... *wet-olo- in Latin vitulus, calf, yearling'.\"}],\n  \"consulted\":[WLD251,\n   {\"src\":\"POK\",\"where\":\"p. 1175\",\"stance\":\"supports\",\"note\":\"'Latin vetus, -eris old ... Latin veterinus Zugvieh; vitulus calf = Umbrian vitluf (Italian i instead of e presumably through borrowing ...)'.\"},\n   {\"src\":\"IEC\",\"where\":\"s.v. uetəlos (l.20209)\",\"stance\":\"supports\",\"note\":\"'Lat. vetulus oldish ... Vocalism of Lat. vitulus, m. calf problematical'.\"}]},\n {\"id\":6,\"lang\":\"English\",\"words\":\"veal, veteran, veterinary\",\"verdict\":\"confirmed\",\n  \"derivation\":\"veal: ME veel < Old French veel (F. veau) < Latin vitellus, diminutive of vitulus 'calf'; it entered English after 1066 as the Norman word for calf-meat. veteran (early 16th c.) is from Latin veterānus 'old, experienced (soldier)', from vetus. veterinary (17th c.) is from Latin veterīnārius 'of beasts of burden', from veterīnae (bestiae).\",\n  \"derivation_fa\":\"انگلیسی veal «گوشت گوساله» از انگلیسی میانه veel است. veel از فرانسوی کهن veel (امروز veau) و آن از لاتینی vitellus، مصغّر vitulus «گوساله»، آمده است. veteran از لاتینی veterānus «کارکشته» و آن از vetus «کهن» است. veterinary از لاتینی veterīnārius «مربوط به چارپایان باربر» است. ادعای نورایی درست است.\",\n  \"sources\":[],\n  \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 wet-2 lists VETERAN, INVETERATE, VETERINARY, VEAL, VITELLUS.\"}],\n  \"consulted\":[\n   {\"src\":\"KLN\",\"where\":\"s.v. veal (l.41153)\",\"stance\":\"supports\",\"note\":\"'veal ... ME. vel, veel, fr. MF. veel, veau ... fr. L. vitellus, dimin. of vitulus ... cp. ... veteran, veterinary'.\"},\n   {\"src\":\"SKT\",\"where\":\"pp. 546, 551 (SKT.txt leaves 566, 571)\",\"stance\":\"supports\",\"note\":\"'Veal. (F.-L.) O.F. veel ... L. uitellum, acc. of uitellus, dimin. of uitulus, a calf'; 'Veteran. (L.) L. ueteranus, experienced ... L. ueter-, stem of uetus, old, lit. advanced in years.'\"}]}\n]}\nentries.append(e7)\nout={\"pdf_page\":552,\"book_page\":522,\"verified_by\":\"claude-opus-5\",\"verified_on\":\"2026-10-16\",\"entries\":entries}\njson.dump(out,open(\"/home/sfmqrb/git/rishe-private/data/verification/page-552.json\",\"w\"),ensure_ascii=False,indent=1)\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-552.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-552.json >/dev/null && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 552"
}
```


### [2026-10-17T00:05:48.863Z] TOOL RESULT

```
nodes verified: 10/10
node verdicts: {'confirmed': 6, 'plausible': 2, 'transcription_suspect': 2}
root verdicts: {'confirmed': 2}
ref checks: {'not_checked': 5, 'supports': 5, 'contradicts': 1, 'partial': 3, 'not_found': 1}
books consulted: {'supports': 20, 'silent': 6, 'contradicts': 4, 'partial': 1} | by book: {'KLN': 4, 'HRN': 3, 'HUB': 3, 'WLD': 3, 'POK': 3, 'PHD': 2, 'NYB': 2, 'BQT': 2, 'MON': 2, 'SKT': 2, 'IEC': 2, 'AHD': 1, 'BRT': 1, 'ARY': 1}
```


## [2026-10-17T00:05:50.914Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==48' HRN.txt | grep -o '^ *[0-9]*\\. [^ ]*' | head; grep -c 'Kalb' BRT.txt"
}
```


### [2026-10-17T00:05:51.419Z] TOOL RESULT

```
109. iimed
110. enhäz^)
111. enhästen^)
112. enhoylden>^)
113. en^äm
114. erCßumen
1
```


## [2026-10-17T00:05:55.487Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; sed -i 's/Horn p. 26 (leaf 47) is in the ā- section;/Horn p. 26 (HRN.txt leaf 47) holds nos. 109-114 (ummed, anbāz, anbāštan ...), not bačče;/' /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-552.py && python3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-552.py && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 552 | grep -c PROBLEM; grep -c 'nos. 109-114' page-552.json"
}
```


### [2026-10-17T00:05:55.953Z] TOOL RESULT

```
0
1
```


## [2026-10-17T00:06:03.965Z] TOOL CALL #50: SubagentHandback

```json
{
 "message": "I verified page 552 (book page 522) and wrote /home/sfmqrb/git/rishe-private/data/verification/page-552.json. `verify_check.py 552` reports 0 PROBLEM lines, with all 10 nodes in 2 roots verified.\n\n- **Roots:** both confirmed (Wes 5: PIE *wes-, *wes-no- \"buy, price\"; Wet: PIE *wet- \"year\").\n- **Nodes:** 6 confirmed, 2 plausible, 2 transcription_suspect, 0 disputed.\n\nFlagged items:\n- **Wet #2, Pahlavi \"vhat-čak, cačak\"** (transcription_suspect, error in the book): MacKenzie's form is waččag (wck'), which Horn, Hübschmann and Mo'in write vačak. \"vhat-čak\" is not attested and looks like Nourai's own respelling with the -t- of Sanskrit vatsa. \"cačak\" is a misprint for vačak.\n- **Wet #4, Sanskrit \"vasta\"** (transcription_suspect, error in the book): the right form is vatsá- \"calf, yearling\". Sanskrit vasta- means \"he-goat\". Skeat, Pokorny, Walde-Pokorny and Klein all give vatsa.\n- **Wet #1 and #3, Iranian *vasa → bačče** (plausible, not disputed):\n  - Against: Nourai's own sources, Horn no. 184 (p. 43) and Hübschmann no. 184 (p. 26), reject linking bačče to vatsá-, because Persian č cannot continue ts.\n  - For: Wiktionary derives بچه from Middle Persian waččag < Proto-Iranian *wacáh \"calf\".\n  - Certain: the Middle Persian → New Persian step (Mo'in, Borhan p. 237, footnote 5).\n- Smaller points: Nourai's ref HRN:26 does not have the entry (bačče is on Horn p. 43). \"věnum\" is a diacritic slip for vēnum. \"Wes 5\" is Nourai's own numbering; Pokorny's 5. u̯es- means \"to dress\".\n\nThere are no extraction errors: the JSON matches the printed page. To support the checks I saved the page image to data/verification/sources/refs/ocr/BOOK/552.png. I also saved my reading of Borhan p. 237 to data/verification/sources/refs/ocr/BQT/237.vision.txt. Five Wiktionary pages are archived and cited."
}
```


### [2026-10-17T00:06:04.226Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
