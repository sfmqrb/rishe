# Verification process log — verify-page-514


## [2026-10-15T02:44:16.604Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 514 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-514.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-514.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-514.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 514` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-15T02:44:16.694Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-15T02:44:19.180Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-15T02:44:19.208Z] TOOL RESULT

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
279	  `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
280	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
281	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
282	  any extraction errors (JSON differs from the printed page) the owner must fix.
283	  Do not paste the JSON back into your reply.
284	
```


## [2026-10-15T02:44:19.684Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-514.txt"
}
```


### [2026-10-15T02:44:19.750Z] TOOL RESULT

```
1	=== PDF page 514 (book page 484) ===
2	--- entry 0 ---
3	ROOT Tŭ -> redirect to Tu
4	--- entry 1 ---
5	ROOT [Indo-European] Tuardo, Turd, Turt : Tuardo: quartz; Turd, Turt: hard, strong  (refs WLD1:747; IEC:1472)
6	#1 (parent #0) [Persian] refs=IEC:1472; MON:1066 | tord «تُرد» : brittle, stiff
7	#2 (parent #0) [Old Persian] refs=IEC:1472 | sparda, sfard : stiff, hard
8	#3 (parent #0) [Latin] refs=IEC:1472 | tardus : thick, sluggish
9	#4 (parent #0) [Greek] refs=IEC:1472 | sard : hard
10	--- entry 2 ---
11	ROOT [Chinese] Tu-kŭe : strong people  (refs PRT:743; SKT:578)
12	#1 (parent #0) [Persian] refs=BQT:487 | tork «تُرک» : a Turk, a beautiful woman | extra: ترکمن ، ترکیه ، ترکمنستان | NOTE: PHN:363 derives these from Arabic "T.r.k: to leave", as Turks were originally nomads
13	  #2 (parent #1) [Greek] refs=None | 
14	    #3 (parent #2) [Latin] refs=None | turcus
15	      #4 (parent #3) [French] refs=None | 
16	        #5 (parent #4) [English] refs=KLN:1665; AHD:1382 | Turk, Turkey, turkey, turquoise
17	--- entry 3 ---
18	ROOT [Indo-European] Tulupos : lump, ball, mass, crowd  (refs IEC:1455)
19	#1 (parent #0) [Persian] refs=IEC:1455 | torob, torb «تُرب» : radish
20	#2 (parent #0) [Greek] refs=IEC:1455 | tolupě : ball of thread
21	  #3 (parent #1) [Turkish] refs=IEC:1455 | turp : radish
22	--- entry 4 ---
23	ROOT Turd -> redirect to Tuardo
24	--- entry 5 ---
25	ROOT Turt -> redirect to Tuardo
26	
```


## [2026-10-15T02:44:20.449Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-514.json"
}
```


### [2026-10-15T02:44:20.531Z] TOOL RESULT

```
1	{
2	  "pdf_page": 514,
3	  "book_page": 484,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Tŭ",
8	        "redirect": "Tu"
9	      },
10	      "nodes": []
11	    },
12	    {
13	      "root": {
14	        "name": "Tuardo, Turd, Turt",
15	        "lang": "Indo-European",
16	        "refs": "WLD1:747; IEC:1472",
17	        "gloss": "Tuardo: quartz; Turd, Turt: hard, strong"
18	      },
19	      "nodes": [
20	        {
21	          "id": 1,
22	          "parent": 0,
23	          "lang": "Persian",
24	          "refs": "IEC:1472; MON:1066",
25	          "words": [
26	            {"translit": "tord", "gloss": "brittle, stiff", "script": "تُرد"}
27	          ],
28	          "note": null,
29	          "quote": null
30	        },
31	        {
32	          "id": 2,
33	          "parent": 0,
34	          "lang": "Old Persian",
35	          "refs": "IEC:1472",
36	          "words": [
37	            {"translit": "sparda, sfard", "gloss": "stiff, hard", "script": null}
38	          ],
39	          "note": null,
40	          "quote": null
41	        },
42	        {
43	          "id": 3,
44	          "parent": 0,
45	          "lang": "Latin",
46	          "refs": "IEC:1472",
47	          "words": [
48	            {"translit": "tardus", "gloss": "thick, sluggish", "script": null}
49	          ],
50	          "note": null,
51	          "quote": null
52	        },
53	        {
54	          "id": 4,
55	          "parent": 0,
56	          "lang": "Greek",
57	          "refs": "IEC:1472",
58	          "words": [
59	            {"translit": "sard", "gloss": "hard", "script": null}
60	          ],
61	          "note": null,
62	          "quote": null
63	        }
64	      ]
65	    },
66	    {
67	      "root": {
68	        "name": "Tu-kŭe",
69	        "lang": "Chinese",
70	        "refs": "PRT:743; SKT:578",
71	        "gloss": "strong people"
72	      },
73	      "nodes": [
74	        {
75	          "id": 1,
76	          "parent": 0,
77	          "lang": "Persian",
78	          "refs": "BQT:487",
79	          "words": [
80	            {"translit": "tork", "gloss": "a Turk, a beautiful woman", "script": "تُرک"}
81	          ],
82	          "script_extra": "ترکمن ، ترکیه ، ترکمنستان",
83	          "note": "PHN:363 derives these from Arabic \"T.r.k: to leave\", as Turks were originally nomads",
84	          "quote": {
85	            "text": "عرب دیده و تُرک و تاجیک و روم - زهر جنس در نفس پاکش علوم",
86	            "poet": "Sa`dî"
87	          }
88	        },
89	        {
90	          "id": 2,
91	          "parent": 1,
92	          "lang": "Greek",
93	          "refs": null,
94	          "words": [],
95	          "note": null,
96	          "quote": null
97	        },
98	        {
99	          "id": 3,
100	          "parent": 2,
101	          "lang": "Latin",
102	          "refs": null,
103	          "words": [
104	            {"translit": "turcus", "gloss": null, "script": null}
105	          ],
106	          "note": null,
107	          "quote": null
108	        },
109	        {
110	          "id": 4,
111	          "parent": 3,
112	          "lang": "French",
113	          "refs": null,
114	          "words": [],
115	          "note": null,
116	          "quote": null
117	        },
118	        {
119	          "id": 5,
120	          "parent": 4,
121	          "lang": "English",
122	          "refs": "KLN:1665; AHD:1382",
123	          "words": [
124	            {"translit": "Turk, Turkey, turkey, turquoise", "gloss": null, "script": null}
125	          ],
126	          "note": null,
127	          "quote": null
128	        }
129	      ]
130	    },
131	    {
132	      "root": {
133	        "name": "Tulupos",
134	        "lang": "Indo-European",
135	        "refs": "IEC:1455",
136	        "gloss": "lump, ball, mass, crowd"
137	      },
138	      "nodes": [
139	        {
140	          "id": 1,
141	          "parent": 0,
142	          "lang": "Persian",
143	          "refs": "IEC:1455",
144	          "words": [
145	            {"translit": "torob, torb", "gloss": "radish", "script": "تُرب"}
146	          ],
147	          "note": null,
148	          "quote": null
149	        },
150	        {
151	          "id": 2,
152	          "parent": 0,
153	          "lang": "Greek",
154	          "refs": "IEC:1455",
155	          "words": [
156	            {"translit": "tolupě", "gloss": "ball of thread", "script": null}
157	          ],
158	          "note": null,
159	          "quote": null
160	        },
161	        {
162	          "id": 3,
163	          "parent": 1,
164	          "lang": "Turkish",
165	          "refs": "IEC:1455",
166	          "words": [
167	            {"translit": "turp", "gloss": "radish", "script": null}
168	          ],
169	          "note": null,
170	          "quote": null
171	        }
172	      ]
173	    },
174	    {
175	      "root": {
176	        "name": "Turd",
177	        "redirect": "Tuardo"
178	      },
179	      "nodes": []
180	    },
181	    {
182	      "root": {
183	        "name": "Turt",
184	        "redirect": "Tuardo"
185	      },
186	      "nodes": []
187	    }
188	  ]
189	}
190	
```


## [2026-10-15T02:44:24.387Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; cat sources/SOURCE_MATRIX.md | head -80; ls sources/refs/ | head -100; python3 -c \"\nimport json;d=json.load(open('sources/refs_online.json'))\nfor k in ['IEC','WLD','WLD1','MON','BQT','PRT','SKT','KLN','AHD','PHN','POK','HRN','HUB','ARY','TTS','LKT','SYN','PHD','NYB','BRT','KNT','CHEUNG','FSD','WEB']:\n  print(k, json.dumps(d.get(k),ensure_ascii=False)[:400])\n\""
}
```


### [2026-10-15T02:44:24.763Z] TOOL RESULT

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
Permissions Size User   Date Modified Name
drwxr-xr-x     - sfmqrb 14 Oct 22:19  incoming
drwxr-xr-x     - sfmqrb 14 Oct 22:19  ocr
drwxr-xr-x     - sfmqrb 14 Oct 22:19  pageimg
drwxr-xr-x     - sfmqrb 14 Oct 22:25  tessdata
.rw-r--r--  600k sfmqrb 14 Oct 22:19  AFA.txt
.rw-r--r--   15M sfmqrb 14 Oct 22:19  AFM.pdf
.rw-r--r--  355k sfmqrb 14 Oct 22:19  AFM.txt
.rw-r--r--  384k sfmqrb 14 Oct 22:19  AFM_alt.txt
.rw-r--r--  342k sfmqrb 14 Oct 22:19  AFM_pages.txt
.rw-r--r--  850k sfmqrb 14 Oct 22:19  AHD_watkins1985.txt
.rw-r--r--  825k sfmqrb 14 Oct 22:19  AHM.txt
.rw-r--r--  1.2M sfmqrb 14 Oct 22:19  AID.txt
.rw-r--r--  240k sfmqrb 14 Oct 22:19  AIN.txt
.rw-r--r--  256k sfmqrb 14 Oct 22:19  AKD.txt
.rw-r--r--  285k sfmqrb 14 Oct 22:19  ARB_abdulraheem.txt
.rw-r--r--  1.3M sfmqrb 14 Oct 22:19  ARB_mo3rb.txt
.rw-r--r--  744k sfmqrb 14 Oct 22:19  ARP.txt
.rw-r--r--  633k sfmqrb 14 Oct 22:19  AVG.txt
.rw-r--r--  2.6M sfmqrb 14 Oct 22:19  BQT_alt_v1.txt
.rw-r--r--   139 sfmqrb 14 Oct 22:19  BQT_dli_part1.txt
.rw-r--r--  2.6M sfmqrb 14 Oct 22:19  BQT_v1.txt
.rw-r--r--   26M sfmqrb 14 Oct 22:19  BQT_v1_djvu.xml
.rw-r--r--  2.2M sfmqrb 14 Oct 22:19  BQT_v1_pages.txt
.rw-r--r--  2.4M sfmqrb 14 Oct 22:19  BQT_v2.txt
.rw-r--r--  4.3M sfmqrb 14 Oct 22:19  BQT_v2_pages.txt
.rw-r--r--  4.8M sfmqrb 14 Oct 22:19  BRT.txt
.rw-r--r--  656k sfmqrb 14 Oct 22:19  BST.txt
.rw-r--r--  1.8M sfmqrb 14 Oct 22:19  CHEUNG.txt
.rw-r--r--  593k sfmqrb 14 Oct 22:19  DEV.txt
.rw-r--r--  144k sfmqrb 14 Oct 22:19  DOZ.txt
.rw-r--r--  1.5M sfmqrb 14 Oct 22:19  DRM.txt
.rw-r--r--  560k sfmqrb 14 Oct 22:19  EAV_studies.txt
.rw-r--r--  891k sfmqrb 14 Oct 22:19  FRS.txt
.rw-r--r--  1.6M sfmqrb 14 Oct 22:19  FRS_pages.txt
.rw-r--r--   16M sfmqrb 14 Oct 22:19  FSD_vol1.txt
.rw-r--r--   17M sfmqrb 14 Oct 22:19  FSD_vol2.txt
.rw-r--r--   13M sfmqrb 14 Oct 22:19  FSD_vol3.txt
.rw-r--r--   17M sfmqrb 14 Oct 22:19  FSD_vol4.txt
.rw-r--r--  1.2M sfmqrb 14 Oct 22:19  FSF.txt
.rw-r--r--  2.2M sfmqrb 14 Oct 22:19  FSF_pages.txt
.rw-r--r--  650k sfmqrb 14 Oct 22:19  FVQ.txt
.rw-r--r--  628k sfmqrb 14 Oct 22:19  FVQ_pages.txt
.rw-r--r--  573k sfmqrb 14 Oct 22:19  GPL.txt
.rw-r--r--  1.6M sfmqrb 14 Oct 22:19  HENNING_selected_papers.txt
.rw-r--r--  449k sfmqrb 14 Oct 22:19  HID.txt
.rw-r--r--  5.6M sfmqrb 14 Oct 22:19  HJB.txt
.rw-r--r--  688k sfmqrb 14 Oct 22:19  HRN.txt
.rw-r--r--  527k sfmqrb 14 Oct 22:19  HUB.txt
.rw-r--r--  3.3M sfmqrb 14 Oct 22:19  IEC.txt
.rw-r--r--  3.4M sfmqrb 14 Oct 22:19  ISS_alt_DKS.txt
.rw-r--r--  1.3M sfmqrb 14 Oct 22:19  KFL.txt
.rw-r--r--   11M sfmqrb 14 Oct 22:19  KLN_1966.txt
.rw-r--r--   10M sfmqrb 14 Oct 22:19  KLN_1971.txt
.rw-r--r--  874k sfmqrb 14 Oct 22:19  KNT.txt
.rw-r--r--  944k sfmqrb 14 Oct 22:19  KNT_full.txt
.rw-r--r--  488k sfmqrb 14 Oct 22:19  LAM.txt
.rw-r--r--  4.6M sfmqrb 14 Oct 22:19  LAT.txt
.rw-r--r--  627k sfmqrb 14 Oct 22:19  LEW_1910.txt
.rw-r--r--  1.1M sfmqrb 14 Oct 22:19  LKT.txt
.rw-r--r--   62k sfmqrb 14 Oct 22:19  LST.txt
.rw-r--r--  4.4M sfmqrb 14 Oct 22:19  MON_part1.txt
.rw-r--r--  4.3M sfmqrb 14 Oct 22:19  MON_part2.txt
.rw-r--r--  373k sfmqrb 14 Oct 22:19  MPP.txt
.rw-r--r--  470k sfmqrb 14 Oct 22:19  NAT_2005.txt
.rw-r--r--   139 sfmqrb 14 Oct 22:19  NYB.txt
.rw-r--r--  505k sfmqrb 14 Oct 22:19  NYB_vol1.txt
.rw-r--r--  920k sfmqrb 14 Oct 22:19  NYB_vol2_glossary.txt
.rw-r--r--  664k sfmqrb 14 Oct 22:19  PEI.txt
.rw-r--r--  8.4M sfmqrb 14 Oct 22:19  PHD.pdf
.rw-r--r--  341k sfmqrb 14 Oct 22:19  PHD.txt
.rw-r--r--  8.4M sfmqrb 14 Oct 22:19  PHD_mackenzie.pdf
.rw-r--r--  609k sfmqrb 14 Oct 22:19  PHD_mackenzie.txt
.rw-r--r--  609k sfmqrb 14 Oct 22:19  PHD_pages.txt
.rw-r--r--  604k sfmqrb 14 Oct 22:19  PHN.txt
.rw-r--r--  982k sfmqrb 14 Oct 22:19  POK_01.txt
.rw-r--r--  1.1M sfmqrb 14 Oct 22:19  POK_02.txt
.rw-r--r--  1.2M sfmqrb 14 Oct 22:19  POK_03.txt
.rw-r--r--  4.0M sfmqrb 14 Oct 22:19  POK_full.txt
.rw-r--r--  9.8M sfmqrb 14 Oct 22:19  RCH.txt
.rw-r--r--  1.3M sfmqrb 14 Oct 22:19  SBK.txt
.rw-r--r--  226k sfmqrb 14 Oct 22:19  SDQ.txt
.rw-r--r--  1.4M sfmqrb 14 Oct 22:19  SIN.txt
.rw-r--r--  2.7M sfmqrb 14 Oct 22:19  SKT.txt
.rw-r--r--  3.0M sfmqrb 14 Oct 22:19  SKT_dli_revised.txt
.rw-r--r--  326k sfmqrb 14 Oct 22:19  SNS.txt
.rw-r--r--  1.3M sfmqrb 14 Oct 22:19  SNS_pages.txt
.rw-r--r--  1.8M sfmqrb 14 Oct 22:19  SOD.txt
.rw-r--r--  3.7M sfmqrb 14 Oct 22:19  SOD_pages.txt
.rw-r--r--  466k sfmqrb 14 Oct 22:19  SPG_keilinschriften1881.txt
.rw-r--r--  4.5M sfmqrb 14 Oct 22:19  SYN.txt
.rw-r--r--  152k sfmqrb 14 Oct 22:19  TAD.txt
.rw-r--r--  243k sfmqrb 14 Oct 22:19  TAD_pages.txt
.rw-r--r--  313k sfmqrb 14 Oct 22:19  TLM.txt
.rw-r--r--   89k sfmqrb 14 Oct 22:19  UNV.txt
.rw-r--r--   12M sfmqrb 14 Oct 22:19  WEB_vol1.txt
.rw-r--r--  317k sfmqrb 14 Oct 22:19  WLD_band3.txt
.rw-r--r--  549k sfmqrb 14 Oct 22:19  ZAP.txt
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/source
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
WLD1 null
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
PRT {"title": "E. Partridge, Origins: A Short Etymological Dictionary of Modern English, New York 1958", "edition_found": "1958 (lending-only copies)", "kind": "archive_restricted", "url": "https://archive.org/details/originsshortetym00part (1958 1st ed.) ; originsetymologi0000part_j9t3 (4th ed. 1966) ; originsetymologi0000part (Routledge 2009) — all lending", "identifier": "originsshortetym00part (al
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe-private/data
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uof
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. l
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe-private/data
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verifica
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
CHEUNG null
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
```


## [2026-10-15T02:44:27.532Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; ls data/verification/page-5*.json | head; python3 -c \"\nimport json;d=json.load(open('data/verification/page-499.json'));e=d['entries'][0];print(json.dumps({k:v for k,v in d.items() if k!='entries'}));n=e['nodes'][0];print(json.dumps(n,ensure_ascii=False,indent=1)[:2500])\"; sed -n 1,200p tools/verify_check.py | grep -n -i 'problem' | head -40"
}
```


### [2026-10-15T02:44:28.289Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   69k sfmqrb 14 Oct 22:14  data/verification/page-50.json
.rw-r--r--   99k sfmqrb 14 Oct 22:14  data/verification/page-51.json
.rw-r--r--   50k sfmqrb 14 Oct 22:14  data/verification/page-52.json
.rw-r--r--   53k sfmqrb 14 Oct 22:14  data/verification/page-53.json
.rw-r--r--   84k sfmqrb 14 Oct 22:14  data/verification/page-54.json
.rw-r--r--   60k sfmqrb 14 Oct 22:14  data/verification/page-55.json
.rw-r--r--   84k sfmqrb 14 Oct 22:14  data/verification/page-56.json
.rw-r--r--   58k sfmqrb 14 Oct 22:14  data/verification/page-57.json
.rw-r--r--   79k sfmqrb 14 Oct 22:14  data/verification/page-58.json
{"pdf_page": 499, "book_page": 469, "verified_by": "claude-opus-5", "verified_on": "2026-10-14"}
{
 "id": 1,
 "lang": "Sanskrit",
 "words": "tulâ, tulya",
 "verdict": "confirmed",
 "derivation": "Sanskrit tulā́ f. 'balance, scales; weight' continues the zero grade *tl̥h₂-éh₂ of PIE *telh₂- 'to lift, weigh, bear': syllabic *l̥ before the laryngeal gives Indo-Aryan ul (the l is the dialectal Indo-Aryan reflex of *l, the u the coloured vowel of the syllabic liquid). tulya- 'equal in weight, comparable, equivalent' is the -ya- derivative of tulā (Wiktionary: from tulā + -ya), and the verb tulayati 'lifts, weighs' belongs here. Nourai's gloss 'balance weight' fits tulā exactly; for tulya the precise sense is 'of equal weight, comparable', a natural derivative.",
 "derivation_fa": "سنسکریت tulā «ترازو، کفهٔ ترازو، وزن» از پایهٔ ضعیف *tl̥h₂-éh₂ ریشهٔ هندواروپایی آغازین *telh₂- «برداشتن، وزن کردن، تحمل کردن» است؛ l هجایی پیش از همخوان حلقی در هندی باستان به ul بدل شده است. tulya «هم‌وزن، همسنگ، همانند» صفتی است که با پسوند -ya از همین tulā ساخته شده و فعل tulayati «برمی‌دارد، می‌سنجد» نیز از همین ریشه است. ادعای نورایی درست است (پوکورنی ۱۰۶۰، واتکینز، والده‌ـپوکورنی، کلاین، ویکی‌واژه).",
 "sources": [
  "https://en.wiktionary.org/wiki/तुला",
  "https://en.wiktionary.org/wiki/तुल्य",
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/telh₂-"
 ],
 "ref_check": [
  {
   "ref": "POK:1060",
   "status": "supports",
   "note": "Pokorny IEW pp.1060-1061 (local POK_full.txt line 85184, 'Root /lemma: tel-1, tela-, tle(i)- tla-', Page(s): 1060-1061): 'Meaning: to transport, carry; to bear, suffer'; 'Old Indie tula 'scales, weight', tulayati 'hebt auf, wägt' ... tulya- 'gleichartig, comparable''; Greek tlēnai, talanton ('die beiden Waagschalen'), PN Atlas, -antos, telos 'payment, tribute, tax'; 'Latin tollo, -ere ... tolero ... latus 'getragen''."
  },
  {
   "ref": "AHD",
   "status": "supports",
   "note": "Watkins AHD Roots s.v. telə- item 9: 'Suffixed zero-grade form *tl-ā- in Sanskrit tulā, scales, balance, weight: TAEL, TOLA.'"
  }
 ],
 "consulted": [
  {
   "src": "WLD",
   "where": "Bd. I p.738 s.v. 1. tel-",
   "stance": "supports",
   "note": "Walde-Pokorny Bd. I pp.738-740 (local WLD_Bd1_pages.txt leaves 747-749) '1. tel- „aufheben, z. T. wägend, z. T. sich aufladend; tragen; ertragen, dulden“: Ai. tulā „Waage, Waagbalken“, tulayati „hebt auf, wägt“' ... 'τάλαντον ... eig. „die beiden Waagschalen“', 'Ἄτλας, -αντος', 'lat. tollo ... tolero ... lātus'."
  },
  {
   "src": "KLN",
   "where": "1966 s.v. tolerate / talent",
   "stance": "supports
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


## [2026-10-15T02:44:33.525Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'tu̯ardo|tuardo|tu̯ard|t[uw]ard|turd|turt|tulup|tolup' IEC.txt | head -40"
}
```


### [2026-10-15T02:44:34.011Z] TOOL RESULT

```
121:STURTEVANT, E. H.: A Comparative Grammar of the Hittite Language, 2nd edn. Elliots Books, Northford 1951
122:STURTEVANT, E. H.: A Hittite Glossary, 2nd. edn. 1936, suppt. 1939, Kraus Reprint, Millwood
876:aue-ster- (auster-, uester-) “further down", See next Skt. cf. avás ‘down’; Lat. auster ‘south’; MHG wéster “western; westward? (and comm. Gmc.); ON vestr ‘west’; OCS ustrü 'summer-
2508:drütos (1) “wooden, of oak, of hardwood; solid, firm, strong’. WP I, 804 Per. durüd ‘timber, plank’; Arm. cf. artuc Cjuniper, fr. *drutio-); Gk. drútë ‘wooden bowl, wooden coffin’; Alb. i drutë ‘wooden’; Lat. cf. in-druticare Clusurate fr. Gaul.); Mir druit (€compression', but cf. drudh-); Gaul. drutos (sturdy, brisk’, substr. in Fr. dru); Li. drūtas “thick, solid, strong’. Cf. also dru- in Gk. dru-pepés ‘ripened on the tree’; drü-ppà ‘olive’. (The source of Gk. hi- drütós “set, established" is uncertain, perh. fr. *sed-, *síséd-)
2830:sole’, though equally to Lat. frētus. (For Lat. fortis, see turtos, is)
3196:dhrtos, is. “held; hold, holding; fast. Cf. dheró, dhermos, dhr-. I, 857 Skt. dhrt, adj.; dhrtib, £.; Av. doroto, adj. E s.; Per. (ambig.) dül ‘bucket’; (LW in Arm. dujl, id.); Arm. cf. han-dart (;calm': Skt. sám- dhrtah ‘held together"); W dryd, adj. ‘thrifty’; s. ‘thrift. (Lat. fortis ‘patient, constant, stout, strong' is ambig. cf. turtos)
3321:dhurdh- ‘shake, tremble’. See dhudhro- and durduro-, dhrdh- Arm. cf. (ambig.) drdvem; MHG turd *brome- grass; EMG (WG or Frankish) Dort, id.
4993:ghrudos (2) ‘broken, breakable, fragile; trun- cated’. Same as (1)? Mir grod ‘short’; Ir. grod ‘quick, prompt’; Lat. cf. rudis (in sense of ‘new, fresh’); OE cf. grot (2) “earth, soil beside grut, m. ‘rock; chasm’; Swiss Grotz ‘polled fir; Li. grudùs ‘fragile, sensitive’. Ir. groidhe, adj. ‘sturdy, spirited’ is semantically to ghrudos (1). Cf. E grotty “nas- ty’; G grotzig ‘dirty’
8389:kundos ‘stolid, stout, ponderous, stocky’ Arm. kunt & kund, gs knti & kndi, abl. -av “bald; squat, stocky’; Per. kund ‘blunt; stupid’; Hes. kundós ‘stolid, unwavering’; Fris. hont ‘stout fellow, sturdy fellow’. Cf. the variant Skt. kunthah (blunt, fr. a type *kundsios or sim.)
10224:-m, suffix of direction Skt. cf. kama-m "at will; Gk. dómo-n beside dómonde; Lat. domu-m; OHG inna-n *in- ward’; Sw. utan ‘from outside; without’; frá-n "away": EMLi. namó-n ‘homeward’; aikstë-n ‘outward’; akrüta-n ‘to the ship’. (For Sw. in- nan ‘before’ see enanti, and for -àm cf. proiam: Gk. & Latv.)
12037:-ois, theme of masc. pl. instrumental, used as an adverbial extn. Variant: -oisu. Skt. -ais; Av. as Gk. ois Lat. -is. Adv. usage in Li. nejuok-ais, “in earnest’; keturíesu, -iese ‘foursome’; Alb. katér-sh, id.; Latv. ce- turtais (sic) ‘fourth’.
12212:opákos ‘reversed, averted, everted, contrary, remote’. WP I, 122 Skt. ápākah “distant'; ápak ‘westward’; apäkä ‘distantly’; Arm. hak, cpds. haka- ‘contrary’; hakim, v. ‘lean’; Lat. opācus ‘shading, dense’; OBr. cf. acom, v. inf. ‘deny’; Ir. acc, aicc, s. ‘denial; OHG abah, aboh, abuh, adv. ‘turned back, reversed, perverse’; OS abuh, as OHG; ON ọfugr, adj. as OHG; Eng. cf. awk- in awk- ward; OCS opako, opaky, adv. ‘back, reversed’; Pol. opak, id.; Cz. opak, adv. “again, on the contrary’; Srb. opak, adj. ‘perverse, evil’; Slo- vene opak ‘inside-out beside pak, adv. ‘but, yet; Cz. pak ‘then’; cf. Slovene pačiti “de- stroy’; Cz. cf. páčit se ‘renege’
14021:queturtos ‘fourth’. Cf. quetuor- “above. WP I, 512 et seq. Skt. cf. Caturtháb, f: -thī, id.; Tokh. B starte, id.; Gk. tétartos, id.; Lat. cf. quartus, id.; Olr. cf. cetharde, n. ‘foursome’; OBr. petguaret, adj. ‘fourth’; Alb. i katërt, id.; OHG fiordo, OE feoweróa & feoróa, id.; OCS. (and com. Sl.) Cetvrütyj, id.; Li. ketvirftas, id.; Latv. cf. ceturtais, id.
14315:quséió (2) ‘tie, knot. (kséió?). (Phonol. ambig.). See Supt: Qu Hitt. sxiya(mi), sxai, v. ‘tie, bind, pledge’; OCS (and com. S1.) šija, f. ‘nape’; cf. (variant?) Skt. sisaye, m. (“be bound’. Here — Sturte- vant); cf. Slovene 3a-ka, f. handful
14649:rb- (?). Cf. ropos (roplos, us). See next. Lat. ambig. Preferably: *robh- OLat. robus, adj. ‘strong’; sn. ‘oak’; Lat. cf. rObur, gs: -oris, n. “oak; strength; courage; prison’; robustus, adj. ‘oaken; sturdy’; MHG ruofe, adj. ‘fragrant’; OE rop, adj. "liberal". (Semantics obscure)
15136:séior- Ir. siar ‘westward; back; late’; W hwyr, adj. “late, slow’; m. “evening, lateness’. Cf. sëiam- and sëros. See Supt: seiros
19017:troqueió (2) (?) trage, rampage’. (Gmc. pro- totype uncertain, see trauió and traio) OHG (ambig.) drauwen, threwen, drouwen, v. ‘threaten’; drowa, thrawa, f. ‘threat’; OE brëa- wian & préagan, v. ‘reprove, threaten, attack, afflic beside préa, s. *threat, abuse, attack"; Latv. strazds, m. id.; cf. the Lat. variant in turdus, a, mf. id.; Li. (ambig.) trankù, tràkti, v. ‘rampage’; traküs, adj. “wild, mad’; Latv. traks, adj. id.; tracis, s. "dun"
19076:trüg- (2) ‘coo, croon’; trugð(n) ‘crooner Gk. trüzo, v. id.; trügón, m. 'turtle-dove'"; Lat. cf. truo, gs: -Onis, m. ‘bittern’. For loss of *-g- cf. men, maius, maior)
19128:trut- (turt-) (1) ‘hump, pile; arse’. See turt- as separate entry Ir. (augmentative type) tortán, turtán, m. ‘hump, hillock’; Alb. truc, m. (mass, pile’, fr. *trutio-) beside (LLat. LW ?) torta, pl. “but- tocks', in view of Fr. tourte, f. ‘pie, batchloaf; fool’; OFr. torte, id.; Big. tráta, f. ‘buttocks, rump’ beside trátav, adj. ‘humped’; Lat. cf. also turtilla, mf. ‘coward’; Slovak cf. trtáč, m. ‘coccyx’
19202:trtor- ‘tremor, tremulous note’. Cf. tortor- and turtul- (turtur-). Onomat. W trydaru, inf. ‘chirp, twitter; Skt. cf. titti- rab, m. *francolin'; Li. cf. tirtulys, m. 'shak- ing, quivering’
19287:tulupos, å “lump, ball, mass, crowd’ Per. turb (‘radish’; LW in Tk. turp, id.); Gk. tolüpe, f. ‘ball of thread’; Alb. tulup, m. (‘col- lop of meat, spg. infl. by tul ‘lean meat, see tul- (4) beside tullupan, adj. ‘bald’); OCS tlüpa, R tolpà, Cz. tlupa “crowd, gang’; ambig. Ir. tola, gs. id., f. “mass, flood’
19306:tumtos, tumtlos *mass, lump' Gk. tüntlos, m. ‘clay, mud"; Li. turtas, tuñ- tas, m. “pack, gang?
19360:turs- (2) (tursis, os) ‘colossus, monster, pile, tower’. (Semantics of koros? queried *colos- sus, tower, giant'. WP I, 367, with ambigui- ties) Gk. türsis, f. ‘tower’; Alb. turrë, f. ‘pile’; Lat. turris, gs: -ium, f. as Gk., beside tursio, gs: -Onis, m. ‘dolphin’; Ob & Ir. torr, m. “pile, tor, load”; Ir. cf. also torrán, m. ‘heap’; tor- raim, v. “pile up’; OW twrr, W twr, pl. tyrau, m. (*pile'. OW also *crowd"); Devonian tor (in place-names); OHG duris (*thuris), m. ‘giant’; OE bere, id., ON purs, buss, id. (MHG turse and türse, wm. id. is held to be a Norse LW); LW in Finn. tursas ‘swollen, big’; s. ‘monster’; Li. (?) tufsis, gs: -io, m. *dwarf'(!), but tùrsa, mf. “person with large buttocks’ (?). Cf. turt- (trut-)
19363:turt- (trut-) ‘buttock’. Cf. tert- (trt-) Lat. *turta, id. (in turtilla, mf. "coward", and as a LW in Alb. torta, fpl. 'buttocks"); (un- certainly: OFr. & Fr. tourte, It. torta, Rum. turtá ‘tart’, but hardly fr. Lat. tortus, a on semantic grounds); Norman Fr. cf. tortiller du derrière, — des fesses ‘walk w. a sugges- tive gait’; Blg. tráta, f. ‘buttocks, rump’; Slovak cf. trtác, m. ‘coccyx’; trtkat', inf. ‘coire’; Blg.
19373:cf. trátnà, v. “take flight, turn tail". (ISophone: Ir. turt, m. *dwarf")
19374:turtul-, turtur- ^wood-pigeon'. Onomat. WP I, 718 Lat. turtur, gs: -is, m. id.; Ital. tórtola & tór- tora, f. id.; Alb. (LW?) türtull, m. id.; Li. tur- klys, m. id.
19376:turusdos, à (trusd-, tursd-) “a song-bird, thrush, blackbird' or sim. WP I, 762. Onomat. Cf. trosdos, us. Variant: trusk- (3). q. v. Arm. cf. tordik, dim. type (fthrush', variant: *tursdiko-); Gk. cf. torotix, interj. (of a bird- cry); Lat. turdus, a, mf. ‘thrush’; Mir truid, id.; Ir. cf. truisc, f. (/(moor-hen" beside liath- truisc, f. thrush’ fr. *truskis); Norw. trost, s. ‘thrush’: OE prostle, f. id. beside brysce (: Ir. truisc), id.; Ger. Drossel, f. id. beside MHG droschel, troschel & trostel, f. id. (NB. Sw. trast, pl. ar m. is fr. a type trosd-, q.v.)
19403:tuàr-, tuàrs- (tuor-) “hold, holding, contain- ment, container'. Cf. tuer- (2) & tuor-, tur- (tur-), turtos, is, tuerst- (tuorst-) Gk. cf. kü-ttaros, m. (lit. ‘hollow container, i.e. *bee-cell, acorn-cup; hold of ship"); Lat. fas, n. "licit act’; fastus, adj. "licit; ne-fas, n. “wrong, crime’; Li. tvorà, f. ‘fence’; Latv. tvàra, f. id.
19424:tuer- (2) ‘squeeze, press, grip, hold”. Cf. tur- (2), tuerst- (tuorst-) (2), tues- (2) and turtos, is. WP I, 749 Hitt. cf. türi(mi), turiya(mi), v. harness’. See tur- Ou: (ambig. in Lat. fer-rūmen, n. ‘sol- der, glue’; first part fr. Stuer or *dher-, cf. siüið for the second part); Gk. (?) seirà, f. ‘chain, cord, noose’; seirai, fpl. (clove of bulbs’, lit. ‘knot, tie'?); Norw. cf. (long-gde) tvaere ut, intr. “last, endure’; OCS cf. (o-gde) za-tvorjo, -tvoriti, v. 'shut'; Li. tveriù, tvérti, v. «tie; enclose; keep, hold, grasp’; Latv. tveru, tvert, v. tr. ‘seize’. (This radical is most diffi- cult to identify. Bossert cites a number of Cilician names of kings: Tberë-, Tbera-, cpds. -dberras. Lat. ob-, re-türare, v. "block invol- ves an alternative phonology. W fferu, inf. *congeal, harden, perish w. cold'; fferdd, adj. ‘solid, firm? involves a unique phonology, if related). Nominal types: Gk. seirós, m. (“cel- lar’, as Eng. «clamp'?); Li. tvērē, f. “iron band, thong’: Hes. será, f. ‘braid, binder’; Latv. tvere, f. ‘handmill’; tveres, fpl. ‘tongs’. See next
19483:tuorst- (tuort-) “fixed, firm'. Cf. tuer- (2) and tur- (2), tuor- (1) Av. Owarsta, pp. as adj. "limited, fixed; suit- able’; Li. tvarstas, m. ‘bandage’; tvartas, m. id. (and ‘stable, fold, pen"); Latv. tvarts, m. “shelter”. (For the initial cf. Go. ga-pwastjan, v. ‘secure, fix"). Cf. turtos, is
19485:tuor- — turtos
19496:turd- (variant of type turt- “hard, strong”, etc. cf. also tursKo-, tuer- (2) E tuorst-, tuor- (1). WP I, 747 Per. (ambig.) turd, adj. (stiff, coy’, fr. *turt- or *turd-); Lydian (Sardic) in OPer. sparda-, Sfard-, ‘stiff, hard, strong’; cf. also Sardeis (literally: ‘fortress’, the capital of Lydia); Oss. tüldz, Dig. toldzà Coak, fr. *turdio); Gk. cf. sardón, gs: -ónos, f. ‘snare’; sard-ónux, m. (*hard-nail' > 'sardonyx^); sárdion, n. *carne- lian’; Dacian cf. (Zeus) Zber-turdus, m. 'su- preme god’; Br. cf. troeZen, pl. -nnu & troeZu, f. ‘tree; OCS (and com. Sl.) tvrüdü, adj. “firm, hard, strong"; R cf. also tverdi, f. *firma- ment’; Cz. tvrz, f. ‘fortress’. (Variant in (?) Lat. tardus ‘thick, sluggish’, fr. *trd- or *trsd-?). NB. The root is *tur-, a form of zero- gde, see tur- (2) preserved in Gk. küt-taros *vault, hold', and Li. tvyru & tvirstu, inf: tvirti, v. “get strong'.See tuer- (2), tuor- (1)
19499:tursKó (turtsKo) ‘grow hard, become strong, get firm'. See next OLat. fortesco, ére, v. id.; Li. tvirstu, ti, v. id.
19500:turtos “firm, hard, strong'. (Lat. variant: turtis). Cf. tuer- (2), tuor- (1) and tur- (2); tuorst- and turd- Per. turd ‘stiff; Kurd. turt “hard, firm, brit- tle’; Lat. fortis, adj. ‘strong, firm’; LLat (also: “big, long’); Osc. cf. fortis, compar. ‘harder’; Li. tvirtas, adj. ‘strong’ beside turtas, m. ‘wealth’; Latv. tvirts, adj. “firm, strong’ beside turta, f. ‘wealth’ Note on IE *tu- and Lat. f-. The ambiguity
```


## [2026-10-15T02:44:41.194Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'quartz' IEC.txt | head; grep -n -i -E 'tvr[uüъ]d|tvrd|tverd' POK_full.txt | head; awk 'BEGIN{RS=\"\\f\"} NR==747' incoming/WLD/WLD_Bd1_pages.txt | head -5; grep -n '\\[pdf page 75[4-8]\\]' incoming/WLD/WLD_Bd1_pages.txt | head"
}
```


### [2026-10-15T02:44:41.624Z] TOOL RESULT

```
13954:quendh- (quenmn-, quens-) (1) “head, end, tip, point, headland'. Cf. WP I, 398 Oss. cánd, Dig. cándà “pile, mass, cairn’; Hes. cf. ténthinoi, mpl. ‘cobble stones, flat stones’ (phonol. ambig.); MIr. cend, cenn, Ir. ceann, m. pl: cinn & ceanna ‘head, end’; Gaul. pen- nos, m. ‘head’; Br. penn, pl. -u, m. ‘head, top’; cf. pens, f. (“arse”, fr. *quent-?); W pen, -nnau, m. “head, end’; Cor. pen, pl. pennow, m. ‘head, chief, chapter; E whin "hard rock, doleritic quartz-basalt; furze’; Li. cf. kensas, kesas, m. ‘hillock’; cf. (z-gde or r-gde) Cz. énét, čnít, inf. jut out?
21001:memorized prayers ' (compare Church Slavic tvrbditi^ moor ': russ. tverditb " learn by heart 
87908:"strong, tight, firm' {*tur-to-). Old Church Slavic tvrbd'b, russ. tverdyj ds. {*tur-, the variation 
138                                                                 tel-



Dorr- oder Trockenvorrichtung“                       „troekne (trans.) an der Luft“
```


## [2026-10-15T02:44:43.606Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 87880,87915p POK_full.txt; grep -n -E 'tvrъd|tvrdъ|tvirtas|tu̯er-' incoming/WLD/WLD_Bd1_pages.txt | head -20"
}
```


### [2026-10-15T02:44:44.011Z] TOOL RESULT

```
Swiss sturm^ dizzy ', sturmi^ dizziness, giddiness; swindle '. 

References: WP. I 749 f., WH. I 42, II 708 f., 718, 719, Mayrhofer 1, 514, 539, 569 f. 
Page(s): 1100-1101 

Root / lemma: tuer-2 : tur-, tuera- 
Meaning: to grab, to enclose 

Material: Gr. asipa:, ep. Ionian asipn f. "rope, cable, band, strap' {*tueria), napa-asipoq 
(TnTTOc;) "Handpferd', compare oz^xbzc, asipai and a£pi[q] ^ojarrip Hes.; with ogradation 
aop6(; f. "Urne' {*tuorc&); perhaps Isipnv, -\\voq, " siren (death goddess); eine wild 
Bienenart, ein small bird', whether originally "Umstrickerin', to asipa "rope, band'; aapyavr) 
f., -\c„ -i5o(;f. "basket, wickerwork ', compare Attic rapyavai nAoKoi, guvSegsk;, TT£5ai Hes.; 
perhaps extension *tuer-g-, compare *tuer-p-\v\ gr. rapnri f. "large basket', whether here 
*tu-p- to *t-p- dissimilated, thereafter also ropy- besides aapy-; 

after Loth RC 40, 475 f. here bret. /c»/77-ac»o'"Steilkuste', gall. /i//77c»- "height' in PN 
\N\eTurno-magus, Turnacum etc.; 

Lithuanian tverili, /i/e/t/" catch, to hem, gird, border, umhegen, form, mould', Latvian 
tveru, tverV grasp, catch, hold, stop', ablaut. Lithuanian turiCi, turet/"}r\o\d, stop, have', 
Latvian turu, turet ds.. Old Prussian tur/t^have, sollen'; Lithuanian ap-tvaras' paddock ', 
/i/5/:^55"Einzaunung', /i/5/'s/K//"mehrfach to hem, gird, border', Latvian tvarstFt' grasp, 
catch, capture '; Church Slavic tvorb "forma'. Old Church Slavic tvor/'t/" create, make'. Old 
Russian tvorh' appearance ', serb. fvorac' creator, god'; lengthened grade Lithuanian 
t\/ora, Latvian tvare ler\ce' , Old Church Slavic fvarb " creation, creature'; in addition russ. 
tvarogm. (from which Modern High German 'Quark = curd), compare zur formation 
Lat\r\ format/cum, French Yromage', originally participle: Lithuanian tvir-tas, Latvian tvirts 
"strong, tight, firm' {*tur-to-). Old Church Slavic tvrbd'b, russ. tverdyj ds. {*tur-, the variation 
/: d\rorr\ originally konson. Stammzu define); in addition still Old Russian tvhrdbi. " vault 
of the sky, firmament, heavens, skies, fortification '. 



References: WP. I 750 f., Trautmann 333 f., Vasmer 3, 85 ff., Hofmann Gr. etym. Wb. 305, 

48456:fiordi             lit. ketvirtas (lett. ceturfais wie ai. caturthd-h  aksl. ceimH.                                     ),
```


## [2026-10-15T02:44:46.504Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'tvirt|tvrd|tvr.d' incoming/WLD/WLD_Bd1_pages.txt | head; grep -n '\\[pdf page' incoming/WLD/WLD_Bd1_pages.txt | awk -F: '$1>0' | head -3"
}
```


### [2026-10-15T02:44:47.087Z] TOOL RESULT

```
48456:fiordi             lit. ketvirtas (lett. ceturfais wie ai. caturthd-h  aksl. ceimH.                                     ),
```


## [2026-10-15T02:44:49.094Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; head -c 600 incoming/WLD/WLD_Bd1_pages.txt; echo; awk 'BEGIN{RS=\"\\f\"} NR>=754 && NR<=760 {print \"=== \" NR; print substr($0,1,300)}' incoming/WLD/WLD_Bd1_pages.txt"
}
```


### [2026-10-15T02:44:49.609Z] TOOL RESULT

```
            GOVERNMENT OF INDIA
 ARCHEOLOGICAL SURVEY OF INDIA

               CENTRAL
            ARCHEOLOGICAL
                LIBRARY
ACCESSION NO. jj03?7
CALL No. gJ3 Wafjpok
                 f_
D.G.A. 79
                      ALOIS WALDE


VERGLEICHENDES WftRTERBDCH
                                DER


     INDOGERM ANISCHEN SPRACHEN

                HERAUSGEGEBEN UND BEARBEITET
                                VON

                     JULIUS POKORNY


                           I.   BAND


VM   /




                   BERLIN UND LEIPZIG 1930

              WALTER DE GRUYTER & CO.
  
=== 754
                                                                                                                                               ;




                                                          tu,   tutu   — tul(o)-                                                        745

lautlichun
=== 755
746                                                        tiegj-      — tuaq-, tuenq-
f.       Verwickeltes und Langwieriges", mala sik l paid „beim Sprechen
     „ etwas
stocken", nisi, paid-reict „anhaltender ermattender Ritt" u. dgl., pal-satmn

„cunctabundus“, (norw. tide „Sonderling, wunderlic
=== 756
                                               tuaq       — tuei-                   747

theban. ady.zdg „Arzt“ und das dem lat. sagana ,,Zauberin“ zugrunde-
liegende *oaydvy (s. Brugmann IF. 28, 286 a 2); oyxog, dor. oaxog (dessen
a den Yergleich mit abg. ost'kz ,.ovile“, s. z. B. Falk-Torp u. sven
=== 757
74S                                                             tuei-, tuei-s-            — tuengh-
tvpn-iju , -yti ..schlagen, staupen“ ist jedenfalls das aus nhd. gwicken stam-
mende poln. cwiczyc                              \ ,
                                                        lit.   tvysk
=== 758
                                                                              tuer-                                                                   749

   Mit dwingan verband man ahd. diilten „driicken, niederdriicken (nhd.
                                                                         
=== 759
750                                                                        tner-



Schar, Menge, Hacht, Herrlichkeit, Glanz, Majestat'*, prymma „Krieger“;
mkd. nhd. mdartl. drumeln „sich im Wirbel drehen, taumeln**, schweiz.
driimmel ..Schwindel'*, und mhd. *durm lurni ,, 'Wirbel, Taumel, Schwindel
=== 760
                                                      tuerk-         — tuibli-                                                              751


                                   Starke ', prudogr „kraftig“, ags. dryd , Kraft" (Brag-
                                              1
  [Aisl. prudr „
```


## [2026-10-15T02:44:51.347Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==756' incoming/WLD/WLD_Bd1_pages.txt | grep -v '^\\s*$' | head -80"
}
```


### [2026-10-15T02:44:51.718Z] TOOL RESULT

```
                                               tuaq       — tuei-                   747
theban. ady.zdg „Arzt“ und das dem lat. sagana ,,Zauberin“ zugrunde-
liegende *oaydvy (s. Brugmann IF. 28, 286 a 2); oyxog, dor. oaxog (dessen
a den Yergleich mit abg. ost'kz ,.ovile“, s. z. B. Falk-Torp u. svencl aus-     ,
schlieBt, selbst            vom Anlaut abgesehen) .,Hiirde, Stall; Umfriedigung eines
heiligen Ortes, dieser selbst", orjxd^co „pferehe ein, sperre ein", dor. oaxfrag
„in der Schaferei aufgezogenes                  Lamm'
                                               oyxig „Sklavin“; auch wohl oyxoco
                                                            -
                                                                ,
„Wiege", orjxwjua „Gewicht; Gegenwert, Belohnung" auf Grund einer
Bed. *„Waagscbale mit das Herunterfallen der Ware verhinderndem korb-
artigen Rande" von agxog; mit Abtonung o wohl horn, aioxog ,.kraftig,
stark" (wenn nicht etwa zu ten- „schwellen", s. d.: unrichtig G. Meyer
Alb. St. Ill 52, 72), acoy.eu) (Trag.) „bin stark, habe Kraft" (Vendryes Msl. 13,
62 ff aus dem Eigennamen Zcbxog, der allerdings Kurzform zu ^coxgargg
      ;
sein wird, folgt trotz Bechtel Lexil. 306 nicht derselbe Ursprung fur oorxog-,
zur Bed. vgl. lat. crassus slav. crbStvz , solidus, fest" ai. krtsnd- neben lat.
                                          ,
cratis    ;)
               Hurde" usw. qert- ..zusammendrehen") schwundstufig av/vog,
                                     u.
„gedrangt, zahlreich" (*t vx-avog, Lit. bei Boisacq s. v.).
  Verwandtschaft mit idg. tiiaqos ,.Haut‘ f„*die eng umschliefiende")? ist
ganz fragwiirdig; wie man zu teu- „schwellen" eine Bed.-Vermittlung
herstellen       soil,      ist   mir unerfindlich.
  Ygl. Bezz. BB. 12, 240, Fick I 4 63 f., 449, III 4 196, Zup. G. 141, Ven-
dryes Msl. 13, 62 ff., Prellwitz 2 406, Boisacq s. vv., Brugmann-Thumb
GrGr. 4 49, und das unter tuengh- Angefiihrte.
tuaq- „baden“.
  Apr. twaxtan „Badequast“;
                                                    -i
  got. pwahan, pwoh, aisl. pva, ae. pwiian „baden      ahd. clwahan, divog,
                                                                    ,
twuog .,waschen", aisl. pviittr (*pwahtu-) „das Waschen" usw. J. Schmidt
Jenaer Lit.-Z. 1874,508, Zup. G. 140, weitere Lit. bei Falk-Torp u. to
„waschen", der unberechtigt tuaq- ztjxo) = ags. pwcenan p&nun (s. viel-
                                                      :                     :
mehr u. ta- „schmelzen") setzt; die Gdbed. kann auch „mit dem Badequast
schlagen" gewesen sein, vgl. *per- „schlagen‘‘ und ..baden".
  Fick I 4 65 stellte pwahan zu ai. locate „traufelt, spendet(?)“.
tuaqos n. „Haut".
   Ai. tvacas- „Haut“ (in Zs. wie h irony a-tvacas- ..goldfellig" und in ivacasya-h
„in der Haut befindlich"), daneben tvac- f. ,.Haut, Fell; Schlauch; Rinde";
gr. oaxog „Schild" (aus Hiiuten, Leder), (ptQz-oodxyg „Schildtrager '.
  Kuhn KZ. 15, 399, Froehde KZ. 22, 263;         verkekrt iiber ody.og Ehrlich
Z. idg. Sprachg. 68 a (: ai. tvaksah n. „Kraft‘).
  Alte Beziehung zu tuaq- ,,fest umschlieBen" ist ganz fragwiirdig.
tuai’do-        (?   s.   u.)     Quarz".
  Gr. oaqdiov „eine haufige Quarzart (Sarder, Karneol)" mhd. nhd. Quarz :
                                                                                      ,
Sommer IF. 31, 373f. Wenn sein weiterer Vergl. mit aksl. tvmh ,,fest zutrifft,
ware oagd- als *turd- damit ablautgleich, dt. Quarz hingegen o-stuf. *tuorilos.
tnei- „scharf kauen, schlagen"??
  Ags. pwitan st. Y. „schneiden, schaben" (wiire d-Praes.; dazu) gepicit
„Span". aisl. pveitr ,.Querhieb, Einschnitt', Jwrita „hauen, stoBen"; [lit.
```


## [2026-10-15T02:44:56.819Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'quarz|sardion|σάρδιον' POK_full.txt | head; grep -n -i -E '^ *(quartz|sard|sardonyx|turk|turkey|turquoise|tardy)\\b' SKT.txt | head -20; grep -n -i -E '\\btolup|turb\\b|torob|turp\\b' SYN.txt HRN.txt HUB.txt LKT.txt TTS* incoming/TTS/* 2>/dev/null | head"
}
```


### [2026-10-15T02:44:57.212Z] TOOL RESULT

```
19177:TARDY
19188:Tardy.  (F.-L.)  F.  tardif  tardy.  (CC ItaL  tardivo,  tardy.)  From  L.  tardmTt slow ;  with  suffis  intts.  Allied  to  iererf, to  nib,  also  to  wa^te  time.     Sec  Trite,
20309:Turkey.  (K.  — Tatar.)  Called  a  Turkey cock,  or  a  cock  of  India,  from  the  notion tliat  it  came  from  Turkey  or  from  imiia  ; so  also  G.  Caitcutische  kahn,  a  turkey- cock,  is  lit  a  cock  of  Calicut.  (H  really caroe  from  the  New  World.)  From  K. Jurquitt  'I'orkcy.  — F.  7\(rc,  a  Turk. — Tatar  Turk,  a  Turk  ;  orij;.  an  adj.  meaning '  biave.*  %  The  usual  Turkish  word  lor 'Turk'i4'£?JM(i«//. turquoise,  turkle.  a  ^m.  (F.-ltal
20330:Turquoise ;  see  Turkey.
(eval):1: no matches found: TTS*
```


## [2026-10-15T02:45:08.086Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'tolyp|toliip|tolüp|τολύπ|tolup' POK_full.txt | head; grep -n -i -E 'turub|turb[^a-z]|turp[^a-z]|tvirt|turd[^a-z]|tard[^a-z]|t[uü]rk[^a-z]' HRN.txt HUB.txt | head -30"
}
```


## [2026-10-15T02:45:08.923Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; ls incoming/; ls incoming/TTS incoming/ARY 2>/dev/null; grep -n -i -E 'turp|türk|turk' LKT.txt | head -20"
}
```


### [2026-10-15T02:45:09.411Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
drwxr-xr-x     - sfmqrb 14 Oct 22:19  ARY
drwxr-xr-x     - sfmqrb 14 Oct 22:19  BLY
drwxr-xr-x     - sfmqrb 14 Oct 22:19  BQT
drwxr-xr-x     - sfmqrb 14 Oct 22:19  FFD
drwxr-xr-x     - sfmqrb 14 Oct 22:19  IRN
drwxr-xr-x     - sfmqrb 14 Oct 22:19  MFL
drwxr-xr-x     - sfmqrb 14 Oct 22:19  MON
drwxr-xr-x     - sfmqrb 14 Oct 22:19  PLA
drwxr-xr-x     - sfmqrb 14 Oct 22:19  TTS
drwxr-xr-x     - sfmqrb 14 Oct 22:19  TYL
drwxr-xr-x     - sfmqrb 14 Oct 22:19  VIE
drwxr-xr-x     - sfmqrb 14 Oct 22:19  WLD
drwxr-xr-x     - sfmqrb 14 Oct 22:19  ZAW
.rw-r--r--  8.1M sfmqrb 14 Oct 22:19  'فرهنگ ریشه های زبان فارسی (2).pdf'
incoming/TTS:
Permissions Size User   Date Modified Name
.rw-r--r--  646k sfmqrb 14 Oct 22:19  TTS_pages.txt
.rw-r--r--  9.8M sfmqrb 14 Oct 22:19  TTS_vambery1878_uoft.pdf
.rw-r--r--  497k sfmqrb 14 Oct 22:19  TTS_vambery1878_uoft_djvu.txt

incoming/ARY:
Permissions Size User   Date Modified Name
.rw-r--r--  8.1M sfmqrb 14 Oct 22:19  ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf
.rw-r--r--  586k sfmqrb 14 Oct 22:19  ARY_latin_index_pages.txt
.rw-r--r--  960k sfmqrb 14 Oct 22:19  ARY_pages.txt
30:Was  die  Ausgangssprachen  angeht,  so  kommen  in  erster  Linie  die Sprachen  des  islamischen  Kulturkreises  in  Betracht,  insbesondere  das Arabische,  Persische  und  Türkische;  daneben  lieferten  von  den  semitischen Sprachen  das  Hebräische  und  das  Aramäische,  ferner  das  Sanskrit  und seine  modernen  Entwicklungen  dem  Abendlande  manches  neue  Wort. Weniger  zahlreich  sind  die  Entlehnungen  aus  den  anderen  indischen  Sprachen [Drawidasprachen],  dem  Chinesischen  und  Japanischen  sowie  dem  Malay- ischen.  Gewöhnlich  wird  ein  orientalicher  Abkömmling  nicht  gleichzeitig in  alle  europäischen  Sprachen  aufgenommen,  vielmehr  von  einer  Einzelsprache ihrem  nationalen  Lautbestande  angeglichen  und  so  an  die  Nachbarsprachen weitergegeben.  Im  Altertum  sind  es  natürhch  vorwiegend  das  Griechische und  Lateinische,  die  diese  Durchgangsstation  bilden.  Ich  konnte  mir  nicht die  Aufgabe  stellen,  alle  griechisclien  und  lateinischen  Wörter,  die  seit  den
46:Mit  dem  epochalen  Ereignisse  des  Jahres  1453  beginnt  die  starke Wirkung  des  Türkischen  auf  die  Sprachen  der  Balkanhalbinsel,  die  nunmehr über  vier  Jahrhunderte  lang  unter  der  politischen  Herrscijaft  der  Osmanen stehen  sollte;  daher  stammt  die  starke  Vermischung  des  Rumänischen  und des  Bulgarischen  und  Serbischen,  sowie  in  weiterem  Umkreise  der  übrigen slavischeu  Sprachen  mit  türkischen  Lehn-  und  Fremdwörtern,  die  nur  noch selten  ihr  orientalisches  Gewand  abgelegt  und  eine  uationalslavische  Form angenommen  haben,  da  selbst  hier  in  den  Halbkulturländern  des  südöst- lichen Europas  die  Wirkung  der  Buchdruckerkunst  in  gleichem  Sinne  wie anderswo  zu  beobachten  ist.  Dazu  scheinen  überhaupt  die  Zeiten  der  ge- waltigen Lautänderungen,  wie  sie  sich  vom  8.  bis  L5.  Jahrhundert  in  ganz Europa  abspielten,  endgültig  vorbei  zu  sein,  jedenfalls  ein  weit  langsameres Ausmaß  der  Entwicklung  angenommen  zu  haben.  Eine  letzte  Wirkung der  orientalischen  Sprachen  auf  den  Wortschatz  des  Abendlandes  erzielen die  direkten  Beziehungen  kolonisatorischer  und  merkantiler  Tätigkeit,  welche die  Europäer  mit  den  Völkern  Süd-  und  Ostasiens  in  Berührung  bringt. Der  Zustrom  malayischer,  hindustanischer,  chinesischer  und  japanischer
51:Noch  einige  Bemerkungen  über  die  Wiedergabe  der  orientalischen und  europäischen  Wörter.  Die  Umsclirilt  der  orieri talischen  Formen  ist entsprechend  dem  Gebrauche  der  Semitisten  (Umschrift  der  DMG),  der Indologen  und  der  Sinologen  erfolgt;  es  schien  mir  dies  praktischer  zu  sein, als  eine  einheitliche  Umschrift  zu  wählen  und  durcli/.uführen,  wenn  auch derselbe  oder  ein  ähnlicher  Laut  auf  diese  Weise  verschiedene  Umschrift erfährt  (s,  s,  sh).  Bei  den  arabischen  und  persischen  Wörtern  ist  die klassische  Form,  also  mit  kurzem  oder  langem  a,  i,  u  angegeben,  und  nur, wo  es  nötig  schien,  die  vulgäre  Form  hinzugefügt.  Da  im  Türkischen  kein Unterschied  zwischen  langen  und  kurzen  Vokalen  vorhanden  ist,  wurde auch  bei  solchen  Wörtern,  die  dem  Türkischen  aus  dem  Arabischen  oder Persischen  zugekommen  sind,  von  einer  Angabe  der  Quantität  abgesehen. Dagegen  sind  durchweg  die  emphatischen  Konsonanten  auch  bei  rein  tür- kischen Wörtern  bezeichnet  worden,  wenn  sie  hier  auch  nur  geringfügige lautliche  Unterschiede  bedingen  (z.  B.  k  und  in  kel  und  kara).  Was  die Umschrift  der  Formen  aus  den  europäischen  Sprachen  anlangt,  so  ist  für das  Russische,  Bulgarische  und  Serbische  die  übliche  Umschrift  *  ohne  die bei  den  Slavisten  gebräuchlichen  Feinheiten  benutzt  worden;  im  übrigen ist  die  nationale  Orthographie  angewandt  worden,  die  nur  bei  älteren  Aus- drücken zu  Schwierigkeiten  führen  kann  (z.  B.  altspanisches  x).
53:'  Dabei  wurde  der  Einfachheit  halber  für  den  labialen  Reibelaul  wie  im Türkischen  auch  im  Slavischen  w  gesetzt;  wenn  auch  im  Arabischen  hiermit  der bilabiale  Laut  bezeichnet  wird,  so  scheinen  mir  phonetische  Fragen  hier  von  ge- ringerem Belange  zu  sein.  Ebenso  ist  in  den  slavischen  Wörtern  h  zur  Umschrei- bung von  X  gewählt  worden.
148:Vrtinbery  Frini  Kultur  —  Hermann  Vamliery,  Die  primitive  Cultur  des  Turko- Tatarisciien  Volkes  auf  Grund  sprachliclier  Fursc-hungen  erörtert.  Leipzig  1879.
149:Vambery  TktElWb  =  Hermann  Vambery,  Etymoloj^isches  Vi^örterhuch  der turkotatarischen  Sprachen.  Ein  Versuch  zur  Darstellung  des  Familienverhält- nisses des  turkütatarischen  Wortschatzes.    Leipzig  1878.
174:sum.  =  sumerisch  tk.  =  türkisch  (osmanisch)
280:lehrte vor  [Fleischer  in  ZDMG  XIX,  301]. Im  späteren  Osmanischen  heißt  aga 'der  ältere  Bruder',  Wiepasa  'der  jüngere Bruder'  ist.  Diese  Bedeutungen  hat das  heutige  Türkische  ganz  vergessen und  gebraucht  das  Wort  in  völlig  an- derem Sinne.  Aga  ist  jetzt  ein  häufig vorkommender  Titel,  besonders  bei niederen  militärischen  Chargen,  wird aber  nur  für  Analphabeten  benutzt, während  der  des  Schreibens  Kundige efendi  [s.  hier  Nr.  557]  genannt  wird. Als  Fremdwort  kommt  Aga  in  allen europäischen  Sprachen  vor,  oft  agha geschrieben.  Als  Lehnwort  hat  das  Rum. aga,  agha,  agia  'ehemaliger  Polizeiprä- fekt'.
413:mei.sl  von  Seide  und  im  Schnitte  unseren Schlafröcken  ähnlich,  doch  etwas  enger ist  [J.W.  Redhouse,  Turkish  Dictionary^. London  1880.  S.  1324;  tk.  entari  od. anteri  bei  A.  Hindoglu,  Dictionnairc Turc-Franqais.  Vienne  1838.  S.  71b]. Aus  dem  tk.  wurde  rum.  anteriü,  un- teren 'langes  Unterkleid  der  orientali- schen Priester,  Bauernrock';  bulg.  serb. anterija  'kurzes  Untergewand  mit  Är- meln'.   [Sain  46.    Bern  SlEtWb  28.
489:118.  Ar.  asTr : 'Kriegsgefangener',  ebenso  tk.  esir,  vul- gär jesir.  Hieraus  serb.  (dial.)  jesir 'Gefangener',  klruss.  jastjr  'dass.',  poln. ycfsfs)«/r 'Gefangenschaft  bei  den  Türken', russ.  (nur  alt  u.  dial.)  jasyr,  jesyr 'Sklave'.    [Bern  SlEtWb  449.
674:Aus  tk.  hal  'Honig'  und  bas  'Kopf, eigentlich  'Honigkopf',  hieraus  rum. balba^,  baba§  'Honigwasser'.  —  Aus  tk. balgy  'Honigverkäufer'  wird  rum.  balgiü 'dass.'.  —  Tk.  bal-jemez  'der  nicht  Honig ißt  oder  frißt'  ist  Bezeichnung  für  ein Geschütz  großen  Kalibers,  vgl.  v.  Moltke, Briefe  über  Zustände  und  Begebenheiten in  der  Türkei.^  1876.  S.  260  im  Briefe vom  12.  Mai  08.  Hieraus  rum.  balimez, baliemez  'großkalibriges  Geschütz'.  Hier- von kommt  sicherlich  auch  der  luia. Ausdruck  a  face  talme§  bahiief  'krumm und  lahm  schlagen'.
680:'2U3.  Ar.  Balkis: X.  pr.,  Name  der  sagenhaften  Königin von  Saba,  die  zur  Zeit  Salomos  lierrschte, vgl.  Koran  Sure  27,  wo  der  Name  aller- dings nicht  genannt  wird.  Nach  A.  Rösch, Die  Königin  von  Saba  als  Königin  Bil- qls.  Eine  Studie.  Leipzig  1890  ist  das ar.  Wort  vom  gr.  uaWaKiq  'Kebsweib' abzuleiten  [das  gr.  Wort  mufs  selbst  wie lat.  pallaca  vom  hebr.  oder  phöniz.  pi- leges  'Kebsweib,  Buhle'  kommen;  die Benennungen  unsittlicher  Personen  und Verhcältnisse  pflegen  von  dem  niedriger stehenden  Volk  aus  dem  Sprachschatz des  höher  gebildeten  übernommen  zu werden].  Nach  Löbel  EITAP  11  soll mit  Berufung  auf  Laurian  §i  Maxim, Glosariu  de  vorbe  sträine  In  limba  ro- mänä.  Bucure§ti  1876,  p.  50  das  Wort im  Türkischen  die  Bedeutung  'dick  und groß'  haben  [fehlt  aber  bei  Kelekian Kämüs].  Hieraus  rum.  balciz,  halcäz 'garstig,  plump,  stämmig'.  —  Die  von Löbel  a.  a.  0.  gegebene  Ableitung  vom gr.  TTaXaid  KüZiKoq  'Ruinen  von  Kyzikos am  Marmarameere'  ist,  weil  semantisch unzulässig,  abzulehnen.
828:Auch  bej  'Herr,  Baron'  [Stamm  baj  s. hier  Nr.  260],  eigentlich  Titel  des  mu- hammedanischen  Feudaladels  in  der Türkei,  früher  mit  manchen  eifersüchtig gewahrten  Vorrechten  verknüpft ;  heute oft  vom  Träger  des  Titels  sich  selbst verliehen  und  daher  in  der  Bewertung gesunken.  In  allen  europäischen  Spra- chen als  Fremdwort,  z.  B.  dtsch.  Bei/. Als  Lehnwort  rum.  öem;  betlic  'die Würde  eines  Begs' ;  beizadea  'Sohn  eines Begs'  [zu  zaäea  vgl.  hier  Nr.  69  b]. Bulg.  serb.  beg,  bej  'Fürst,  Herr'.  — Begier  beji  'Herr  der  Herren'  war  der Titel  der  Statthalter  großer  Provinzen; dtsch.  Beglerbeg,  Beilerbet.  —  Eine  be- sonders schmackhafte  Birne  erhielt  den Namen  beg  armudy  'Herrenbirne'  [wie ja  Zusätze  wie  königlich  u.  ähnl.  bei Naturgegenständen  ihren  Vorzug  an Pracht,  Wert  usw.  gegenüber  anderen andeuten  sollen,  vgl.  Basihcum  'Königs- kraut', Königskerze  (Verhascum),  Kpivov ßaaiXiKÖv  (Litium  candidum),  tk.  sultan böreji  (amaranthus)].  Hieraus  mit  fal- scher Bezugnahme  auf  die  Stadt  Ber- gamo it.  bergamotta,  trz.  bergamote.  sp. pg.  bergamota,  rum.  bergamot;  ndl.  engl. bergamot,  dtsch.  Bergamotte  [doch  Ber- gamottknöpfe mit  Volksetymologie  dial. aus  Perlmutterknöpfe  Andresen  D VE  41  ] ; russ.  bergamot.  [POTT  in  ZKM  VII, 107.  Kluge  47.  ZfromPh  XXXII,  41. XXXm,  62.    ML  1019.
952:N.  pr.,  Stadt  in  Russisch-Turkestan, daher  tk.  buliur  coha  'eine  Art  Wollen- zeug', hieraus  rum.  buhur  'Kaschmir'; ebenso  afrz.  bouqueraut,  frz.  bougran, sp.  bocarän,  it.  bucherame  'Steif  leinwand'. [ML  1366.    (Anders  ZfromPh  V,  556).
963:[Türk.  bük-.
968:[So  bei  A.  Hindoglu,  Diclionnaire  Turc- Franqais.  Vienne  1838.  S.  134  b;  aber bei  Kelekian  Kämüs  292  a:  bola,  altes Wort]  'Tante,  Frau  des  Oheims';  hieraus bulg.  bula  'Türkin'  und  mit  verschiedenen Übertragungen  'Mohn,  wilde  Schwalbe, Wiesel',  bulka  'Braut,  Schwiegertochter; Mohn',  serb.  hula  'Türkin',  bulka  'Feld- mohn'.   [Bern  SlEtWb  100.
1116:'Kneten  und  pressen  (nämlich  die  Mus- keln)'; der  Imperativ  chhämpö  ist  zu angloind.  Shampoo  verderbt.  Dieses Wort  bedeutet  ursprünglich  die  Behand- lung, wie  sie  bei  den  sogen,  türkischen Bädern  üblich  ist,  heutzutage  ist  es  so- viel wie  'Kopfwaschen';  ebenso  dtsch. schamponieren  'kopfwaschen',  neuer- dings volksetymologisch  umgestaltet  zu Schaumpun,  schaumpunieren.  [Hobson- Jobson  821.
1124:N.  pr.  [über  die  Etymologie  dieses  Wortes vgl.  Hobson-Jobson  196/197J.  In  der Bedeutung  'Porzellan'  wird  das  Wort in  vielen  asiatischen  Sprachen  und  im Englischen  benutzt:  engl,  china,  eigent- lich Abkürzung  für  china-dish  wie  turkey statt  turkey-carpet,  turquoise  statt  pne''>'e turquoise  [s.  hier  Nr.  2114].  [Hobson- Jobson  198/199.
1193:'Sperreisen  am  Tor,  Holzschloß'  [s.  Lane, Manners  and  customs  of  the  modern Egyptians  I,  25];  hieraus  mit  ar.  Art. sp.  aldaba,  pg.  aldrava  'Türklopfer, Türriegel' ;  augment.  sp.  aldabön  'großer Türklopfer',  demin.  aldabilla  'kleiner Türriegel'.  [DE  96.  Eguilaz  147.  ML 2455  a.
1290:[Aus  ar.  dar  'Haus',  sinä'a  'Betriebsam- keit, Handwerk,  Industrie']  'Fabrik',  be- sonders 'Waffenfabrik'  und  auch  schon ar.  'Schiffsbauhaus';  im  Türkischen  zu tershäne  korrumpiert,  als  wenn  es  von pers.  Jiänä  [s.  hier  Nr.  809]  käme.  Hier- aus it.  darsena,  siz.  tirzanä  'iniiei'es Hafenbecken',  arzanä,  arsenale,  terzana 'Zeughaus';  frz.  darse,  darsine  'kleiner Binnenhafen',  arsenal;  sp.  atarazana, atarazanal  'Schuppen',  arsenal;  pg. taracena,  tercena  'Schuppen',  arsenal; rum.  arsenal,  darsena.  Dtsch.  Arsenal, ndl.  arsenaal,  engl,  arsenal,  russ.  a?*- senal.  [Dozy  Oost  16/18.  DE  205/206. Eguilaz  304.  Gorjaiew  6.  Kluge  23. Devic  DEt  35/36.    ML  2474.
```


### [2026-10-15T02:45:09.604Z] TOOL RESULT

```
HRN.txt:688:Entlehnung aus osttürk. ast 'unter' an, ohne die Form
HRN.txt:1076:Vergl. türk. arys, oss. d. ItW.arcin (Hübschmann
HRN.txt:1190:phlv. astar; ai. agvatard- 'Maulesel'.
HRN.txt:1441:skr. antard' 'anderer, verschieden von'; osset. ändär
HRN.txt:2668:Enveri's (ed. Brockhaus, S. 56). Er erklärt das Wort durch türk.
HRN.txt:4277:itürk. /itnL'für. v.-ii:]. NOMtrkt: bei Uübschmann.
HRN.txt:4313:Weit gewandert, vergl. türk. qarpuz etc.
HRN.txt:6184:Dazu gehören auch die Lehnworte türk. ispenje
HRN.txt:6836:'Schakal'; plilv. sayäL LW. türk. caqal; ngr. rtjayuh;
HRN.txt:8157:semitisches Lehnwort. Beiläufig bemerkt, ist türk. LW.
HRN.txt:8452:973. murden sterben', Praes. mlr-em, nturdär 'Leichnam' ^),
HRN.txt:9716:Xünrä laute und yäse — türk. yaso^ yesäq sei (Vullers 1, yäsp).— 252 —
HRN.txt:10701:aw. katära- 'welcher von beiden'; ai. katard-.
```


## [2026-10-15T02:45:12.783Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^2114|turquoise|Türkis' LKT.txt | head -5; grep -n -i -E 'türk\\b|t[üu]rk ' incoming/TTS/TTS_vambery1878_uoft_djvu.txt | head -10; grep -n -i -E 'turp\\b|turub|rettig' incoming/TTS/TTS_vambery1878_uoft_djvu.txt | head"
}
```


### [2026-10-15T02:45:13.265Z] TOOL RESULT

```
30:Was  die  Ausgangssprachen  angeht,  so  kommen  in  erster  Linie  die Sprachen  des  islamischen  Kulturkreises  in  Betracht,  insbesondere  das Arabische,  Persische  und  Türkische;  daneben  lieferten  von  den  semitischen Sprachen  das  Hebräische  und  das  Aramäische,  ferner  das  Sanskrit  und seine  modernen  Entwicklungen  dem  Abendlande  manches  neue  Wort. Weniger  zahlreich  sind  die  Entlehnungen  aus  den  anderen  indischen  Sprachen [Drawidasprachen],  dem  Chinesischen  und  Japanischen  sowie  dem  Malay- ischen.  Gewöhnlich  wird  ein  orientalicher  Abkömmling  nicht  gleichzeitig in  alle  europäischen  Sprachen  aufgenommen,  vielmehr  von  einer  Einzelsprache ihrem  nationalen  Lautbestande  angeglichen  und  so  an  die  Nachbarsprachen weitergegeben.  Im  Altertum  sind  es  natürhch  vorwiegend  das  Griechische und  Lateinische,  die  diese  Durchgangsstation  bilden.  Ich  konnte  mir  nicht die  Aufgabe  stellen,  alle  griechisclien  und  lateinischen  Wörter,  die  seit  den
46:Mit  dem  epochalen  Ereignisse  des  Jahres  1453  beginnt  die  starke Wirkung  des  Türkischen  auf  die  Sprachen  der  Balkanhalbinsel,  die  nunmehr über  vier  Jahrhunderte  lang  unter  der  politischen  Herrscijaft  der  Osmanen stehen  sollte;  daher  stammt  die  starke  Vermischung  des  Rumänischen  und des  Bulgarischen  und  Serbischen,  sowie  in  weiterem  Umkreise  der  übrigen slavischeu  Sprachen  mit  türkischen  Lehn-  und  Fremdwörtern,  die  nur  noch selten  ihr  orientalisches  Gewand  abgelegt  und  eine  uationalslavische  Form angenommen  haben,  da  selbst  hier  in  den  Halbkulturländern  des  südöst- lichen Europas  die  Wirkung  der  Buchdruckerkunst  in  gleichem  Sinne  wie anderswo  zu  beobachten  ist.  Dazu  scheinen  überhaupt  die  Zeiten  der  ge- waltigen Lautänderungen,  wie  sie  sich  vom  8.  bis  L5.  Jahrhundert  in  ganz Europa  abspielten,  endgültig  vorbei  zu  sein,  jedenfalls  ein  weit  langsameres Ausmaß  der  Entwicklung  angenommen  zu  haben.  Eine  letzte  Wirkung der  orientalischen  Sprachen  auf  den  Wortschatz  des  Abendlandes  erzielen die  direkten  Beziehungen  kolonisatorischer  und  merkantiler  Tätigkeit,  welche die  Europäer  mit  den  Völkern  Süd-  und  Ostasiens  in  Berührung  bringt. Der  Zustrom  malayischer,  hindustanischer,  chinesischer  und  japanischer
51:Noch  einige  Bemerkungen  über  die  Wiedergabe  der  orientalischen und  europäischen  Wörter.  Die  Umsclirilt  der  orieri talischen  Formen  ist entsprechend  dem  Gebrauche  der  Semitisten  (Umschrift  der  DMG),  der Indologen  und  der  Sinologen  erfolgt;  es  schien  mir  dies  praktischer  zu  sein, als  eine  einheitliche  Umschrift  zu  wählen  und  durcli/.uführen,  wenn  auch derselbe  oder  ein  ähnlicher  Laut  auf  diese  Weise  verschiedene  Umschrift erfährt  (s,  s,  sh).  Bei  den  arabischen  und  persischen  Wörtern  ist  die klassische  Form,  also  mit  kurzem  oder  langem  a,  i,  u  angegeben,  und  nur, wo  es  nötig  schien,  die  vulgäre  Form  hinzugefügt.  Da  im  Türkischen  kein Unterschied  zwischen  langen  und  kurzen  Vokalen  vorhanden  ist,  wurde auch  bei  solchen  Wörtern,  die  dem  Türkischen  aus  dem  Arabischen  oder Persischen  zugekommen  sind,  von  einer  Angabe  der  Quantität  abgesehen. Dagegen  sind  durchweg  die  emphatischen  Konsonanten  auch  bei  rein  tür- kischen Wörtern  bezeichnet  worden,  wenn  sie  hier  auch  nur  geringfügige lautliche  Unterschiede  bedingen  (z.  B.  k  und  in  kel  und  kara).  Was  die Umschrift  der  Formen  aus  den  europäischen  Sprachen  anlangt,  so  ist  für das  Russische,  Bulgarische  und  Serbische  die  übliche  Umschrift  *  ohne  die bei  den  Slavisten  gebräuchlichen  Feinheiten  benutzt  worden;  im  übrigen ist  die  nationale  Orthographie  angewandt  worden,  die  nur  bei  älteren  Aus- drücken zu  Schwierigkeiten  führen  kann  (z.  B.  altspanisches  x).
53:'  Dabei  wurde  der  Einfachheit  halber  für  den  labialen  Reibelaul  wie  im Türkischen  auch  im  Slavischen  w  gesetzt;  wenn  auch  im  Arabischen  hiermit  der bilabiale  Laut  bezeichnet  wird,  so  scheinen  mir  phonetische  Fragen  hier  von  ge- ringerem Belange  zu  sein.  Ebenso  ist  in  den  slavischen  Wörtern  h  zur  Umschrei- bung von  X  gewählt  worden.
280:lehrte vor  [Fleischer  in  ZDMG  XIX,  301]. Im  späteren  Osmanischen  heißt  aga 'der  ältere  Bruder',  Wiepasa  'der  jüngere Bruder'  ist.  Diese  Bedeutungen  hat das  heutige  Türkische  ganz  vergessen und  gebraucht  das  Wort  in  völlig  an- derem Sinne.  Aga  ist  jetzt  ein  häufig vorkommender  Titel,  besonders  bei niederen  militärischen  Chargen,  wird aber  nur  für  Analphabeten  benutzt, während  der  des  Schreibens  Kundige efendi  [s.  hier  Nr.  557]  genannt  wird. Als  Fremdwort  kommt  Aga  in  allen europäischen  Sprachen  vor,  oft  agha geschrieben.  Als  Lehnwort  hat  das  Rum. aga,  agha,  agia  'ehemaliger  Polizeiprä- fekt'.
2274:türk.  olniaJc=:sem,  aufrecht  stehen. 
4408:lautes,  rcspectivc  Inlautes  das  mong.-türk.  Man  =  Fürst, 
7313:gende Tag,  von  der  Stammsilbe  sar,  türk.  jar  (scheinen, 
8071:Windspieler,  vom  türk.  jel  und  pers.  baze). 
10961:des  Nomen  proprium  Türk  =  Türke  zu  liegen,  der  Urbe- 
12513:Jaa  zum  osttürk.  niaj  steht,  wäre  in  Anbeti'acht  des  fast
```


## [2026-10-15T02:45:14.992Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 10950,10975p incoming/TTS/TTS_vambery1878_uoft_djvu.txt; grep -n -E '2114' LKT.txt | head -3"
}
```


### [2026-10-15T02:45:15.332Z] TOOL RESULT

```
197. 

Tuv,  tOT,  tÜT,  tör,  vorn,  ohen,  vorderer;  hervorhr'mgen, 
erschaffen,  aufstellen,  stellen,  stehen. 


uig.  ^ö>  =  obenan,  vor,  Ehrensitz  (das  Juxtaoppositum  dieses 
Wortes  ist  eden,  iden  =  der  unterste  Sitz  im  Zelte,  Ur- 
sprung?); «örtMHeÄ  =  aufkommen,  hervorkommen,  zur  Welt 
kommen ;  törülc,  türüJc  und  törüJcli  =  Geschöpf,  Wesen, 
Aufgekommener  (in  diesem  Worte  dünkt  mir  das  Etymon 
des  Nomen  proprium  Türk  =  Türke  zu  liegen,  der  Urbe- 
deutung nach  Geschöpf,  Wesen,  Mensch,  wie  wir  sol- 
ches auch  bei  andern  Sprachen  wahrnehmen);  <ö>'w=  Ge- 
setz, Sitte,  Mode  (eigentl.  das  Aufgekommene) ;  ;?ö>e  =  Prinz 
(Oberster),  Panzer  (oberes  Kleid);  törätmch,  töretmcl:  — 
hervorkommen  lassen,  erschaffen. 

cag.  tür,  tör  = -vorn,  Ehrensitz,  oberste  Fläche,  Aussehen,  Ge- 
stalt (bezüglich  der  Identität  von  oben  und  Aussehen  vgl. 
Jiiz— ohen,  Gestalt,  §  64);    tiirliJc  =  \on  Art,   Beschaffen- 


185 

lieit  oder  Gestillt  {ni  türlik^vfus  für  ein?);    töre,   tövet- 
1124:N.  pr.  [über  die  Etymologie  dieses  Wortes vgl.  Hobson-Jobson  196/197J.  In  der Bedeutung  'Porzellan'  wird  das  Wort in  vielen  asiatischen  Sprachen  und  im Englischen  benutzt:  engl,  china,  eigent- lich Abkürzung  für  china-dish  wie  turkey statt  turkey-carpet,  turquoise  statt  pne''>'e turquoise  [s.  hier  Nr.  2114].  [Hobson- Jobson  198/199.
4733:2114.  Tk.  türk:
5061:2114 Tseu-tung  2188 r^i/ra  2100 Tulpe  544
```


## [2026-10-15T02:45:17.304Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 4733,4736p LKT.txt | cut -c1-1500; grep -n -i -E 'turk|turc' PHN.txt | head -10"
}
```


### [2026-10-15T02:45:18.228Z] TOOL RESULT

```
2114.  Tk.  türk:
N.  pr.,  Name  eines  über  weite  Teile Asiens  und  Europas  verbreiteten  Volks- stammes. Er  geht  auf  den  Staunri  tür, tör  "^vorne,  oben  >  hervorbringen"  Väm- bery  TktEtWb  S.  184,  Nr.  197  1  zurück 'und  bedeutet  also  'Geschöpf,  Mensch', vgl.  SCHOTT  in  ZDMG  XXXIII,  538; 0.  Franke,  Beiträge  aus  chinesischen Quellen  zur  Kenntnis  der  Türkvölker und  Skythen  Zentralasiens.  Berlin  1904. S.  13;  Beruh. .Munkäcsi,  Die  Bedeutung des  Namens  der  Türken  in  Körösi Gsoma-Archivum  I,  59/63  und  H.  C.  v. d.  GABELENTZ  in  ZKM  II,  70/75. Dagegen  wird  das  Wort  wieder  von J.  J.  HESZ  im  Isl  IX,  99/100  als  'Eisen- hauben' oder  'Helme'  gedeutet.  Mit Recht  wird  die  letztere  Deutung  schon von  FRANKE  als  „bedenkhch"  und  die erstere  von  SCHOTT  als  „gut  begründet" bezeichnet.  Nach  den  Türken  oder  ihrem Lande  sind  insbesondere  bezeichnet: a)  Ein  Edelstein  it.  turchinn,  Adj.  tur- chino,  frz.  turquoise,  sp.  tiirquesa,  pg. turqtieza;  ndl.  turkoois,  dtsch.  Türkis, engl,  turquoise;  er  ist  so  benannt,  weil die  Europäer  ihn  zuerst  durch  die  Türken erhielten,  vgl.  J.  E.  Polak,  Der  orien- talische Türkis.  In  Österreichische  Mo- natsschrift für  den  Orient  1877,  S.  1 75/177.
b)  Der  Truthahn  heikit  engl,  turkey, turkey-powt  'Puter'  [bei  den  Türken  heißt er  übrigens  kaicuk  rnisri  od.  hindi  'ägyp- tische oder  mdische  Henne'].
c)  'Mais' :  frz.  bU  de  Turquie,  it.  gran turco,  dtsch.  türkischer  Weizen.
73:DE L'ARABE, DU PERSAN OU DU TURC.1
86:sans ET DES Turcs; in- 8*. — Paris, Imprimerie impériale, i856.
103:DE L'ARABE, DU PERSAN OU DU TURC,
121:avec leurs analogues arabes, pei*sans ou turcs, me fit
169:sidiairement au persan et au turc, une in^uence exa-
206:sance des caractères arabes, persans et turcs, j'ai placé
224:LES CARACTÈRES ARABES, PERSANS ET TURCS.
231:en usage chez les Persans et les Turcs. L'emploi des majuscules
321:w en arabe ; « et o en turc et en persan. —
333:turc.
```


## [2026-10-15T02:45:20.741Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^ *TURC|^TURC|abandonner|laisser' PHN.txt | head -10; grep -n -i -E '^ *(turk|turkey|turquoise|tardy|quartz|sard|sardine|sardonyx)\\b' KLN_1966.txt | head -20"
}
```


### [2026-10-15T02:45:21.257Z] TOOL RESULT

```
2517:à laisser échapper l'eau d'un réservoir, d'un étang, etc. —
3182:celui-ci veut bien lui abandonner. — En Turquie, qarah qoûlâq
5263:hémistiche soit renfoncé sous le premier, afin de laisser à dé-
7018:croisent par coquetterie sous le menton , de manière à ne laisser
9714:laisser tomber au pouvoir de l'ennemi. Quand les janissaires
9905:TURC, fém. TURQUE, subst. et adj. (a.)
9907:[tarak] quitter, abandonner, par exemple , le sol natal , les Turcs
1008:Turk.
31346:quartz,  n.,  a  crystalline  mineral,  SiO,.  —  G. Quarz,  fr.  kwardy,  a  Western  Slav,  dialectal equivalent  of  Pol.  twardy,  Czech  and  Slovak tvrdy,  ‘quartz’,  prop,  adjectives  meaning  ‘hard’, used  as  nouns,  and  rel.  to  OSlav.  tvrudu,  Lith. tvirtas,  ‘hard’,  Lith.  tveriu,  tverti,  ‘to  seize,  con¬ tain’,  and  prob.  cogn.  with  Gk.  crsipa,  ‘cord, rope,  string’.
33749:sardine,  n.,  a  small  fish.  —  F. ,  fr.  L.  sardina,  sarda , ‘pilchard’,  fr.  Gk.  act pSlvt]  (also  aapSivo?),  of s.m. ;  of  uncertain  origin.  The  usual  explanation of  Gk.  aapSlvr],  as  ‘the  fish  from  the  island  of ZapSci  (Sardinia)’  is  far  from  convincing,  it  is hardly  probable  that  the  Greeks  would  have  ob¬ tained  fish  from  so  far  as  Sardinia  at  a  time relatively  so  early  as  that  of  Aristotle,  from whom  Athenaios  quotes  a  passage  in  which  the fish  oapStvoi;  is  mentioned, sardine,  n.,  a  precious  stone.  —  Late  L.  lapis  sar- dinus,  fr.  Gk.  aapSTvop  Xiflos,  lit.  ‘Sardian stone’.  See  sard.
38207:tardy,  adj.,  late.  —  Fr.  earlier  tardif,  fr.  OF.  (  =  F.) tardif,  fr.  VL.  tardivus,  fr.  L.  tardus,  ‘slow’, which  is  of  uncertain  origin.  Cp.  tardo,  tarda¬ mente,  retard  and  the  second  element  in  bustard. Derivatives:  tardi-Iy,  adv.,  tardi-ness,  n.
40485:Turk,  n.  —  ME.,  fr.  MF.  (=  F.)  Turc,  fr.  ML. Tureus,  fr.  MGk.  ToCpxo?,  fr.  Turkish-Pers. Turk.  Cp.  turkey,  turquoise.
40487:Turkey,  n.  —  F.  Turquie,  fr.  ML.  Turchia,  fr.
```


## [2026-10-15T02:45:23.517Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 9905,9915p PHN.txt; sed -n 40485,40500p KLN_1966.txt | cut -c1-600; grep -n -E '^sard,' KLN_1966.txt; grep -n -E '^sard, ' KLN_1966.txt | head -2"
}
```


### [2026-10-15T02:45:23.959Z] TOOL RESULT

```
TURC, fém. TURQUE, subst. et adj. (a.)
^ji [tourk] , pluriel Jt^l [àtrâk] , dérivé du verbe arabe dij3
[tarak] quitter, abandonner, par exemple , le sol natal , les Turcs
étant considérés comme nomades. L'adjectif arabe se forme en
ajoutant un ^^ y au mot *àjJ [tourk] , et s*écrit ainsi : i^j^
[totirÂ:tyy] , féminin H^S^ \iJOur\wfyai[. — Les Turcs originaires
d'Asie s'appellent plus spécialement (^^^ [tor^mon] dont nous
avons fait Tubgomans ; et l'on entend par Turkbstan (u^^^'***^)
le pays situé à l'orient de la mer Caspienne, et habité par les364 TUT
Tatars Uzbeks, adonnés au voi et au brigandage. — Comme
le mot (fj^i— i [tourk ou turk] signifie aussi barbare, vagabond,
Turk,  n.  —  ME.,  fr.  MF.  (=  F.)  Turc,  fr.  ML. Tureus,  fr.  MGk.  ToCpxo?,  fr.  Turkish-Pers. Turk.  Cp.  turkey,  turquoise.
Derivatives:  Turki,  Turk-ic  (qq.v.),  Turk-ic-ize, tr.  v.,  Turki-fy,  tr.  v.,  Turk-ish,  adj.  and  n., Turk-ish-ly,  adv.,  Turk-ish-ness,  n.
Turkey,  n.  —  F.  Turquie,  fr.  ML.  Turchia,  fr.
Tureus,  ‘Turk’.  See  prec.  word, turkey,  n.  —  The  name  was  applied  orig.  to  the guinea  fowl,  imported  from  Africa  through  trad¬ ers  who  dealt  chiefly  with  the  Near  East  (and for  this  reason  were  called  ‘Turkey-merchants’) ; hence  the  birds  sold  by  these  merchants  came to  the  known  as  turkeys.  See  prec.  word.
Turki,  adj.,  pertaining  to  the  Southern  Turkic, including  Turkish.  —  Pers.  Turki,  fr.  Turk.  See Turk.
Derivative:  Turki,  n.,  the  Turki  languages. Turkic,  adj.,  designating,  or  pertaining  to,  a  sub¬ family  of  Altaic  languages  divided  into  South¬ ern  (=  Turki),  Eastern,  Central  and  Western branches.  —  Formed  fr.  Turk  with  suff.  -ic. Derivative:  Turkic,  n.,  the  Turkic  subfamily  of languages, turko-.  See  turco-.
Turkoman,  n.  —  ML.  Turcomannus,  fr.  Pers. Turkman,  lit.  Turklike’,  fr.  Turk,  ‘Turk’,  and -man,  ‘like".
turma,  n.,  troop,  squadron  of  horse  (Roman antiq.)  —  L.,  of  uncertain  origin.  It  is  possibly rel.  to  turba,  crowd’  (see  turbid), turmeric,  n.,  an  aromatic  plant  of  the  ginger  fam¬ ily  (Curcuma  longa).  —  Fr.  earlier  tormarilh,  tar- maret,  fr.  F.  terre  merite,  ‘saffron’,  fr.  ML.  terra merita  ( =  deserved  earth’),  a  folk-etymological corruption  of  Arab,  kurkum,  ‘curcuma’.  See Curcuma.
turmoil,  n.,  tumult.  —  Perh.  a  folk-etymological alteration  (after  E.  turn  and  moil)  of  OF.  tre- mouille,  tremuie  (whence  F.  trimie),  ‘mill  hop¬ per’,  fr.  L.  trimodia,  a  collateral  form  of  trimo- dium,  ‘a  vessel  containing  three  modii’,  fr.  tri-
turpitude
and  modius ,  name  of  a  measure,  which  is  rel.  to modus,  ‘measure’.  See  mode.  Cp.  It.  tramoggia, OProven?.  tremueia,  Catal.  tremuja,  Port,  tra- monha,  ‘mill  hopper’,  which  all  derive  fr.  L.  tri¬ modia.
Derivatives :  turmoil,  tr.  and  intr.  v. ,  turmoil-er,  n .
turn,  tr.  and  intr.  v.  —  ME.  turnen,  tournen,  part¬ ly  fr.  OE.  tyrnan,  turnian,  partly  fr.  OF.  torner, turner  (F.  tourner)  which  both  derive  fr.  L.  tor- nare,  ‘to  turn  in  a  lathe;  to  turn,  fashion’,  fr. tornus,  ‘lathe;  graver’s  tool’,  fr.  Gk.  x6pvo<;, ‘turner’s  wheel,  graver’s  tool,  a  tool  for  drawing a  circle’,  which  is  rel.  to  xopciis,  ‘graver’s  tool’, xopsuetv,  ‘to  bore  through;  to  work  in  relief’, fr.  I.-E.  base  *ter-,  ‘to  rub,  rub  by  turning,  turn, twist;  to  pierce’.  See  throw  and  cp.  toreutic.  Cp. also  attorn
turn,  n.  —  ME.,  fr.  OF.  torn,  later  tour  (F.  tour), back  formation  fr.  torner,  turner  (F.  tourner). See  turn,  v.
Turnicidae,  n.  pi.,  the  family  of  button  quails (ornithol.)  —  ModL.,  formed  fr.  Tumix  with suff.  -idae.
turnip,  n.  —  Prob.  a  contraction  of  turn-nip  and derived  fr.  ME.  turnen,  ‘to  turn’,  and  nepe, ‘turnip’  and  so  called  in  allusion  to  the  round shape  of  the  root.  See  turn,  v.,  and  navew. Derivatives:  turnip,  tr.  v.,  turnip-y,  adj.
```


## [2026-10-15T02:45:28.280Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^(turquoise|sard),' KLN_1966.txt | head; grep -n -E '^sard\\b' KLN_1966.txt|head -3; python3 -c \"\nimport json;d=json.load(open('../refs_online.json'));print(json.dumps(d['BQT'],ensure_ascii=False)[:1500]);print(json.dumps(d['MON'],ensure_ascii=False)[:1500])\""
}
```


### [2026-10-15T02:45:28.910Z] TOOL RESULT

```
{"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.", "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} 
{"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).", "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf", "/home/sfmq
```


## [2026-10-15T02:45:29.871Z] AGENT

Let me use the ref_page tool for BQT:487 and check MON locally.


## [2026-10-15T02:45:30.550Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; timeout 300 python3 tools/ref_page.py BQT:487 2>&1 | head -80"
}
```


### [2026-10-15T02:45:31.007Z] TOOL RESULT

```
no scan of BQT covers printed page 487 (see 'scans' in refs_online.json)
```


## [2026-10-15T02:45:32.393Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'ترک' BQT_v1_pages.txt | head -40"
}
```


### [2026-10-15T02:45:32.877Z] TOOL RESULT

```
3212:۷ ترکی ۲ -از زبان تر کی‌لفغات بسیاری- مستقلا ویا درذیل لغات
3571:و ترکی .که اصلا مستعمل نیست » وهمه موجب طول لاطایل ؛ و فرهنگ
6087:وترکانآختابهچی (۱) کونند .
6970:چه آذر بلفت ترکی بمعنی بلند است و بایسگان
7152:مقام دارد ؛ و معنی ترکیبی آن آتش جهنده
7217:کوش آذری‌تبریز» . - ترکان عثمانی و بتبم آنان خاورشناسان «آذری» را بلهجه کی معمول
7899:خوانند» ومعنی ترکیبی آن آسیا مانند است . : ِ
8200:بت زود - و ترکرده - و آمیخته باشد -
8234:ترکیبی آن آفت آب است - و جصب احطلاح
8273:است . ایکه در فرهنگها ممنی ترکیبی آبرا< آفت‌آب » نودته اند مبتنی برفقه اللغة عامیانه
8356:م آفریتگات ‏ رك : آفرنگان. ۵ آق ‏ در ترکی و مفولی بمعنی سقید
8591:۵ آلاچق - ترکی‌الاجو ختح همزه وضم جیم؛ بممنی سراپرده و سایبان دوستونیاست
8602:یادشاهان را گوبنده ویضی کویند اين, لفث ترکی .
8638:مرخبان . « کل گلاب ۲۲۳۷>. 4 آلتمغا - را: آل طمفا. » آلنوی - ترکی
9493:۵ اباقا - ترکی , اباغه . ابافا بمعنی برادر مهتر با کهتر پدر « جفتابی صا *.
9848:نقطه بالف کشیده , بلنت زند و پازید (۷) خالء | جوان را گوبند ۷ - و جماعتی از ترکان حم
9953:2۱۵068 انا 82 در ترکی بمعنی پدر است و د رکلمات م رکب ماند اتابکه‎ - ٩
9956:۵ 4 ترکی بسنی پدرء پبر» عنوانی است افتخاری. « جفتالی۳» .«سیخول» نیز کوبند . ۶
10081:اخترکاوبان
10400:بالش کنند و بترکی قو ۷ خواند - وک رکدن
10492:انوشیروان بنا کرده و از آن جهت فیردذ کرد | ومعنی ترکیبی آن شیر خشمنالك» چه ارد بمعنی
10644:ص۱۱۲ » - نام زبان مردم پا کستان که ممزوجی است از فارسی وخربی و هندی و ترکی . ره :
10872:قندهار هم هست؛ و معنی ترکیبی آن خشمگین
11708:ماوراء النپر که آنرا بترکی شبران بنر وزن
12927:بلفت بونانی؟ ترکیبی است کهآ نرا بغارسی پخته
13217:و از وه شمال شرقی با رشته ای باربك از پامیر بنام « واخان » و < سنکانك » ( ترکستان
13487:رشکوفه واستفراغ باشد وبترکی نانرا گویند .
13605:ارل و ثانی : لت ترکی بمعنی بز رکك باش که‌در
15521:سرحد شمالی از مغرب بمثرق بقفقازیه و دربای خزر و ترکتان روس , از مشرق باففانستان
15721:۷۲ در ترکی ابلك بفتح سوم»
15981:اجثاق _ ترکی, دومردراکه دو خواهررا درازدواج دارند نبت‌بهم باجناق گویند .
16540:از ترکان .
16660:از هم بکثایند و آنرا نیز بترکی قلاح خوانند
16689:دست چپ وقترکهرستهاراازهم بگشایند ۴ - وجمعنی
16742:از ترکان .
17689:بجر چگل - تامدرباچهایت‌درترکستان
19938:بخترک « بن اول بروزن عشتری,شخصی
21663:میوه ایست مفزدار که آنرا ون گویند و ترکان
22040:برخیاز شمرای ما آنرا بتخانه پنداشته وفرهنگها محل آنرا درترکستان بادر چن قراردادماند.
24458:کوهی با صحرایی و وحشی - و ترکان ی که باین جانور دسترس نداشتند نسوغ خود را از دم اسب
```


## [2026-10-15T02:45:35.925Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -c $'\\f' BQT_v1_pages.txt; grep -n 'pdf page' BQT_v1_pages.txt | head -3; grep -n -E '^\\s*(ترک|ترد|ترب)\\s' BQT_v1_pages.txt | head; grep -n -E 'ترب ' BQT_v1_pages.txt | head"
}
```


### [2026-10-15T02:45:36.361Z] TOOL RESULT

```
766
31679:ترد ابرایان ممالك »جاور جیحون است. در شاهنامه نوران مملکت ترکان و چبتیان است که
11803:کوره‌ای‌بمترب بغداد آمده (درهمةٌ این اسامی بکسر همزه). رک : ممجم البلدان؛ فرهنگستان»
29328:باشد.- و جشم اول و ثالت ترب را گونند و بعربی
29581:قی بونانی 1۳6۵ ,در فارسی: ترب (حبله ومکر) «استق۳۸۹*.
29757:لمدزین را کویند که تکلتو باشد - و ترب راهم
```


## [2026-10-15T02:45:38.485Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 520 525 530 535; do awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n{print \"=== leaf \" n; print substr($0,1,200)}' BQT_v1_pages.txt; done"
}
```


### [2026-10-15T02:45:39.068Z] TOOL RESULT

```
=== leaf 520
۳:9
بان خصوصاً .و آشیرا نیز که ازآن‌یز ند پلور
خوانشد .
بلقو ه - بروزن و «عنیکلگوده است؛
وآن غاژه‌ای باش که زنان‌بررومالنده وروبر! سرخ
گردانند .
بلفحت ه بفتح فا بروزن بدبشت.عاضی
بلخفتن ۱ ست که بمعنی ج
=== leaf 525
بنابه
و پابان و یخ درخت ٩‏ - و اتهای هر چیز
وچیزی نیز هست که آترا آبکامه گود, و آن
نان خورشی است معروف و مشهور در صفاهان
- وتنه درخت‌را لیز کنبهادب ۴ وخوشة خرمارا
هم میگوند .
بنابه - بنتع ول و بای ایب
=== leaf 530
بنگان - بکس اول وکاف فارسی بالف
کشید بروزن فنجان . طاسی باشد که دهقادان
بنآنرا سوزاخ کرده باشند وآترا درطفار پرآیی
گذار ند بمقدار زمانی که برشود؛ آب‌از رودخائه
با برغ باچشمه پزولمت: هرماك رود ربستی را
=== leaf 535
۱ 2۳9
شبیه‌به ثیهولیک نکوچکتر ازاوست" وا نرا بعربی
سلوی خوانند .
بو ر نم اول و انی مجهول ر رای
قرشت هردو ماکن» اسب سرخ ونك را گویند ۴
بودش
‌
بودص - بکر دال ابجد بروزن
سوزش » بیعتی هستی و بود باشد و بع
```


## [2026-10-15T02:45:44.124Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^ترک|ترک *[-ـ] *ب|ترد *[-ـ] *ب' BQT_v1_pages.txt | head -20; sed -n 29320,29335p BQT_v1_pages.txt"
}
```


### [2026-10-15T02:45:44.696Z] TOOL RESULT

```
8234:ترکیبی آن آفت آب است - و جصب احطلاح
29391:ترکان جفتابی ۴ .
31080:ترکان‌ننگی با ن‌منسوب بخوش‌صورتی‌مشهوراند9 -
«صحف : ترهث.
۹ «حور» صحیح است. رك.فاری.
۴ ۰
. «کل لاب 6۲6۱ «لك ]: ۰۳۰۹ .ر بره
قر بر ۵ - بر وزن غرغره » عام فوعی از
انگور است
قر بزه بنتح اول و ضم الث و سکون
ار و رگ
باشد.- و جشم اول و ثالت ترب را گونند و بعربی
قجل خوانند ۱ .
لر بزه ‏ بنتح اول و شم الث بر وزن
خربزه ۰ بمعنی نربز است که حتدوانه -
بادرنگه - و خيار باشد - و بضم اول نرب را
کونه ۲
قر له « بر وزن مدرسه, فوی قزح را
(۱) کوند .
```


## [2026-10-15T02:45:46.620Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 29270,29320p BQT_v1_pages.txt; echo ----; sed -n 31060,31110p BQT_v1_pages.txt"
}
```


### [2026-10-15T02:45:46.925Z] TOOL RESULT

```
و بسشی پدخوبی - و حبله وری هم‌آعده است
فرااو - بسکون واو ؛ بمعنی‌تراوش‌است
که از تراوبدن وترشح کردن باشد .
ثر او۵ ه با دال ابجد بزوزن عداوت »
مق از تراویدن وتراوی است » یمتی آب
وشراب وامثال آن تراوش «یکند .
تراول بکر واو بر وزن‌علاحل
بر کک گياهی است نا معلوم ۱
قر او دن « بروزن‌دواندن » چکیدن
و تراوش کردن آب و شراب وامثالآن باشد ۴.
ف رای ح بر وزن تباهی » میو؛ نوباوه
و نوزسده را گویند ة
تر )یمان بابای حطی(۱)آوهیم بروزن
فر ) بن» بابای‌حطی(۰)۱بروزن‌ومعنی
تراوبدن وتراوش کردن باشد؟ .
فرب » بفتح
مکر وحیله وزرق وتروبر ۴ - و کزاف و زبان
آوری باشد6 - و بضم اول عمروف است ۲ که
(۱) چك: با با .
۷ - ر9: وال ۲ -
کت وا ۶ کف (حاشه) .
اندر آهد مرد با زن چرب چرب ه
٩‏ - تربال
دایر پر کار باشد ودر میان شهر
یبد
عربان فجل خوانند ۷ .
رپ - با بای فلرسی بروزن چرب ۰
کشك‌سیاه را گویندوبتر کی فرافروت خوانند ۸.
قر بالمی * « بابایابجد بروزن‌چنگالی»
نام عمارنی است بپار عالی بنا کرد اردشیر
بلهك در شرفی شهر «کون» *۷. که از شهرهای
قاری است و« جون »۱۷ معرب آست . گوند
که برسر آن بنا آتتکده‌ای ساخته بودند ودر
برابر شهر کوهی است و از آن‌کوه آبی بان
آنشکده میآمده .
قر بامان با میم بر وزن متاقان .
بونانی نام کلی است لاجوردی و برگهای آن
دراز می‌باشد و و شاخ وبرکک آن همه نلغ
ب و آن را غافت بر وزن آفت نیز کویند »
وبجای بای ابجد بای حطی هم آهده است۱۴.
فرب بکر اول و الث و
ودال ابجد, نام ثهربست غیرمملوم۷۴- وبضم‌اول
و ثاكث دوایی است حمروف که اسهال آورد ۰۱۴
و بابمعنی بکسر اول و ثالث هم آهده است
وچوب وی میان خالی‌را نیز گوبند .
رود کی سمرقندی. «لفیت رس ۷۸ *.
۷ - نرب 13208105 ازتبر؛
۸ ۳ ۳
. «شکل‌آن عدورست چنانك
نامه س۱۳۷ وح۹و*۱همین صفجه.
«صحف : ترهث.
----
بروزن طبقیه ۰ باق عنکبوترا گوند .
تنستخج(4) بنم سین بر وزن عه رخ ۰
هرچیز برا کوبند که بسیار نادر و کمیاب وبی‌مثل
ومانند ودراهایت تفاست باشد ۰ و «هرب آن
سوق است ۰
(۳) چنی است‌درنسخ وظ: ثن‌زنده.
۴ .3 تشر , ؟ رك : تنزه.
ینبم میشود. «فاب اص۲۱۱ ج؛ .
۸ ‌ ركگ: مش
۷ ر: تن (نن زدن) .و کنابه . از دهان خویان هم هست - و بمعنی
فروبردن و نایدید کردن همآمده است - و هر
صضحه با نشته ای باشد که نفاشان ومسوران‌اظپار
صثمت خود ی آن‌کنند عموماً - و نگار ایا
مانیرا وین خصوصاً وباین ممنی با ثای مثأثه
هم آمده‌است؟ وتوار ی که برژین اسب مضوط
کننه - ودوالی که بدان‌بار بر پشت باربردار(۱)
محکم سازند - ودره اکویراهم گفته‌اند۴ - ونایاب
وعدیمالمشال را نیز کویند - و بمسنی‌ملول‌وستوه
وآزرده هم آمده است - و ام ولایتی اسث از
بدخشان - و تلم مقامی باشد از تر کستان که
ترکان‌ننگی با ن‌منسوب بخوش‌صورتی‌مشهوراند9 -
لی‌شوی » نم شین شقطه دار بروزن
بدخوی, حوض وجوي آب و چشمه و امتالآبرا
کونند عموماً - و تخته ای که میت را بر بالای
آن شود خصوصا .
تنقظاد -_بنم اول وفاف و طای‌حلی
بالف کشیده بر وزن پرخمار » پاسبان‌را گویند -
وشمم باريك بلئدی را نیز کفته‌اند که ازسرشب
تا صباح بسوزد , وبر وزن توالفقار و بردبار حم
گفتهاید .#9
قنگه س بفتح اوز وسکون ثانی وکاف
فارسی : ممروف است که هی فراخ باشدا -
وبك انگه بار و خروار شکر را یز کویند؟ -
۱ - اوستاه)نأکفی(20)8) (سفت عالی‌از 140۳08 بمعنی‌نمم وببر ومند)» پپلوی 808
(ضیق) , ارمنی 12017 ( سفت» ححکم ) , کردی 668 ,بلوچی ۱27 اففاني اقهتها .
وخی ۷28 .سریکلی 008) « اسشق ۳۹۸ * «صینا .4۲:۱4٩‏ بمنی آنرا ازرشة تنجیدن(«.م)ه
ازساس کرت 4206 و420 داسته‌اندرننگ بمعنی دوال زین مر کوب (در بلوچی 00۰808ه,
کردی 208 ,061208 (مبان کمربند وتنگ)؛ استی 8750088 (شک‌بند) .افنانی 18-۵08
( ننک زین ) و 1808 (ننکه زین) <هوبشمان ۳۹۸*.
۴ در این بلاد فزون دارد از هزار کلات بهريك ادر دبنار تنگها برتشگه .
فرخی سیستالی . *لغت‌فری ۶۲۷۹ .
۴ ر4: ارتنگه : ۱
۴ -دشت چوندیبای سوزن کرد وآحو جوق‌جوق استاده آمده بیرون صحراها زشکه .
منجيك ترمذی. هلت فرس ۲۷۹+
9 رکفث: تنگه ت رکان.
۵ قك -بشم اول ودوم» حندی باستانی ها , - هتلاحشا (نلزك , لطیف) « کردی
عطاهعا . استی اقا . بلوچی عطقعها , <هتقا . سربکلی لاله « اسشق ۳۹۷ > .
طبری ۹۵8 (روان. ضدغلیظ) «واژه‌نامه 6۷۳۳؛ بارىك» رقیق؛ نازك. لطیف. دان‌تنكث» درعرمی
رفاق. سلائق «السامی» «منتهی‌الارب» وان توع‌نانرا اکنون درایران «نان لواش» گویند ودر بهار
عجم «لواشی» و«لباش» (کلحة اخبر بنفل‌از جهادگیری) نیز نوشته (در:لواش):
تنكك دل چو باران بمنزل رسید نضبد که واماند کان از ند .
```


## [2026-10-15T02:45:49.997Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'ترك|ترد|ئرد' BQT_v1_pages.txt | sed -n 1,200p | awk -F: '$1>29000 && $1<29700' | head -30"
}
```


### [2026-10-15T02:45:50.420Z] TOOL RESULT

```
29164:۱ ۳ جانوریست سرخ رنگ ویردار که بشتردرحمامها
29266:+ کردی ۰۰۱۹۷ گیلکی 02-1۵250128 , طبری 8-25101۷28 « واژه نامه ۱۹۳ ؛ ستردن
29436:تردك۱۱- بروزن مردك ۰ کرم کندم
29456:بیعنی اول ترده ۱ ست که قبالة خانه وباغ باشد »
29606:۳ - ظاهراً اصل اترك است ولی دود مزبور در شمال خراسان جاری‌است. رأه:جفرافیای‌طبيمي.
29622:5 نود . ملله های ترك که در ابران دورة اسلامی سلطنت کردماند : غزنوبان ( ۳۵۱ -
29624:*_غلامان و کنیزان تر که نژاد زا بودند. بدین‌مناسبت تركیمعنی معشوق زباروی‌بکار رفته‌است.
29638:کوبته از جنی فرج یکه زدان ترك پوشند.
29662:. ترك جوشی کرده‌ام من نیم خام از حکیم غزنوی شنو تمام‎ - ٩
29676:وایشکه آن را از تر کیب فارسی «ترك مانند » گرفته‌اه ( محمود کاشفری آ]] . ۳۰۷) وجه
29689:ترك نیمرود » کنابه از آقتاب
```


## [2026-10-15T02:45:52.126Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 29420,29460p BQT_v1_pages.txt; echo -----; sed -n 29560,29690p BQT_v1_pages.txt"
}
```


### [2026-10-15T02:45:52.748Z] TOOL RESULT

```
بررآید» ومعرب آن طرخون است۸ ۰ قوت بامرا
نقهان دارو 4 3
تر خینه بر وزن کشکینه, بمعنی
طرخانه (۱) است . و آن کندمی باشد بلفور
کرد که درآب جوثانند نا پقوام آید پس شیر
کوسفند با آب غوره در آن ریزند وگلولها
ماخته خشك کنند و بوقت حاجت مموشانند
و بخورند *۷.
فر۵آهی « با دال بالف کشیده و میم
مفتوح ونون ساکن . کتابه از فاسق و فاجر -
و بد گمان - وعاسی و مجرم و کناهغر و آلودة
معصیت اوملوث باشد .
قر دست ‏ بروزن سرعت . مردم جلد
وچست و چابك را گوند .
قر دسعی ه بر وزن سردستی ۰ .جلدی
وچابکی را کوشد .
تردك۱۱- بروزن مردك ۰ کرم کندم
خوار را گوبند . و باين ممي با زا فارسی حم
افثه اتف
آر ده بروزن پرده ۰ قبالهةٌ باغ و خانه
وامثاز آن را گوبند ۷۴۳ و اجرت آمیاکردن
۳ . ممرب آن طرخان. « نقس .٩‏
۴ - تام جد ابواسر
ج۲ ص ٩۱۳4‏ .
فجتتایی ۰۲۱۳ ۰ ۵ ره : قردمانا وقرطمانا .
نرخینه. ‏ ۸ 0۲361۳60605 ۸۳6۲۳1512 <« کل کلاب ۲۹۹.
۷۰ - رك: ترخوانه ۰
۷ مسحف: ترقنده(ه.م). ‏ ۷ وله :
4 راه: ثرخان؛
و "۳ را ترزدههعئی با زای نقطه دار نیز بنظرآهده ات
ترر بان » بروزن همزبان؛ بمه‌:ی زبان
آور وشخصی که کرم کفنکو شود و خن هی
ثر وتازه بگوید - و بمعنی ترجمان هم هست
یمنی شخصی که لفتی را اززبانی بزبان دیگر
قرب کند ۷ .
فر ۵۵ بسکون ثالی بر وزن سرزده »
بیعنی اول ترده ۱ ست که قبالة خانه وباغ باشد »
- وقنح انی بروزن تبرزه هم‌آهدء ۲ ست.
تر فان بروزن ومعتی ترجمان است
یمنی شخصی که لفتی راز زبانی بز بان دیگرسیان
کند ؟- وترزبان را نیز گوبند ۴ و آن شخصی
-----
قفر قذا ٩۵‏ «بروزن‌شرمنده: پمعنی‌ترفند
است که‌دروغ- وییهودس وت وبرومکروحیله باشده
+ باین هعنی‌بجای حرف الث قاف هم بنظر آمده
است - ویمعنی قرس ودیم هم‌هست.
تر فینه* اس ون کشکینه , آخررا
کونند که فاتق آنرا فرافروت 0 باشند .
تر قنفه ۷۱- با قاف پروزن شرعنده .
بمعنی هرزه ویبپوده - و دروغ و محال- ومکن
وحیله‌باشد ,۵
فرقیین « بروزن تقین, بلفت نبعی‌خعطی
است که محرران دربنی‌محل‌میان دوحرف‌بی‌مد
(۱) چك: ۷۹
9 9 کرمان ]21 :
بشمر توفند ار ترف بودم و رخبی پند و حکمت اکذون چو شکر وقندم .
سوزنی سمرفندی. «لغت نامه حرف‌پ ص2۲۵
۴ رك : لك ] : ۳۱۰ . ۴ - رك : ترزفان و توزبان . ۳ ۱
( ۳9 -- با (‌ .۴
۵ راهی کو راست است بگزین ای دوست دورشو از راه بیکرانه ونوفنج.
رود کی سمرقندی. «لغت فرس ۹5.
۱ - از اوستابی 1۳۵0 ت , 666/1۷24 ( دزدیدن » با نقلب سرقت کردن ) ؛ بهله
۳ (بحیله ربودن) "هندی باستان - ۰00۲28 ۳۵8816) (انتقال بافتن. تغییر دادن)
قی بونانی 1۳6۵ ,در فارسی: ترب (حبله ومکر) «استق۳۸۹*.
۲ - باهتر او همه هثرها بافه باسخن او همه مخنا ترفند .
فرخی میستانی «لفت فری۸۸*.
۸ - چون خود نکنی چنانکه گوبی پند نو بود دروغ وتسرفند .
«ناصر خسرو بلخی*۹*.
٩‏ -ركٌ : ترفند. - از: ثرف (ه .۸ ۲- یله (پسوند اسبت) -
ی : ترفنده .
» تر قه - بفتح اول ودوم وسوم مشدد ومخفف. از: ترق (اسم صوت ت رکیدن چیز) ,
(پسوند پدید آورنده آساز صوت)؛ باروت و مواد منفجره .وامالآنرا نی زکفته‌اند - و گذاشتن و گذشتن
ونرك دادن وخلاصی از تملفات‌جسمانی وخواهش
نضالی و گشتن ازماسوی‌افه بجذیات حفانی,ونراد
باینمعنی عربی هم هست6 - ونام قصبه ایست از
مضافات آذربایجان ‏ و بنم اول و سکون انی
ممروف‌است که‌نفیض نازمك باشدء ‏ و کویندترکان
از ارلاد بافث بن نوح‌اند و ولابت ثرکتان‌رانیز
بطریق مجاز تراد میگویشا - و کنابه‌ازمطلوب
ومعشوق وفلام باشد۷ .
ثر کان‌چر خج- کنابه از سبعاٌ ساره
است که زحل و مشثری و مریخ وآفتاب و زهره
لت ومای أت
تر کافی س بر وزن قریانی» بالایوشی‌را
٩‏ - ترقین؛ سیاه کردن موضعی را بفرد حساب بخط زائده تااکمان نشو دکه‌ابنجارا برای
نوششن سفید کذاشته‌ند «غیا» :
هسند نست بحق بارز مجموع وجود وآن د گرها همه ترفین عدم‌را تفصیل .
انوری آبیوردی بنقل *المعجم شمس فیس چاپ مدری۲ ۲۷
۳ - ظاهراً اصل اترك است ولی دود مزبور در شمال خراسان جاری‌است. رأه:جفرافیای‌طبيمي.
کیهان۲ 4۷ .رردیدیگربنام«بر ک» است. رکه:پ رکه ۴ از: تر 4 (پسوندیدید آورندشاسم
ازصفت) تر حلوابی‌در آ ذر بابجان «ارمغان‌سال۱۲ شمارث۷«کاف» بقلم 7-3 وی*ودر کیلان‌هممُمو لاست:
۴ اسم صوت از: تر کیدن . 8 از عربی وارد فارسی شده. بت 3
جنم‌اون درتر کی بممنی شجاع و دلیر وسخت «جفتابی ۲۱۳ ۴ ۰ درچینی 6لاع_لا1 » در ونانی
[101۲*0 ,نام ترلك بعنوان قومی بدوی نخستین بار درفرن ششم میلادی دیده میشود. در همان
فرن تر کان دولتی بدوی تاسیس کردند که از معولستان و سرحد شمالی چین نا بحر اسود امتداد
داشته است . موسس حکومت مزبو رکه چینان اورا ۲760 - 11[ نامند ( در کنیبه‌یای ثرکی
0 درسال ۵6۲ در گذشت وبرادرش 15181 (درطیری [ , ۸٩۵‏ و ۸: منجبوخاقان)
که در مقرب فتوحانی کرده . ظاهراً تاسال ۵۷٩‏ زیسته است . این دو برادر کویا ازآغاز منتفل
ازیکدیگر حکومت میکردند .
چینیان ازدولت مزبور بنام امپرانوری تی‌کان شمال وامپراتوری ترکان «شرق یاد کرده‌اند.
7 در سال ۵۸۱ تحت نفوز -لسلهٌ چینی أفاگ اين دو امپرانوری بطور فطع از بکدیگی جدا شدند
وبه‌دها هردونايم‌سلملةً چینی 208" (۱۱۸ -۹۹۷) گردیدند . درحدود سال ۱۸۲ .ترکان شمال
موفق شدند استقلال خودرا بدست آورند . دربار؛ روابط این ترکان قدیم و اخلاف آنان حث‌های
بیار شده است که درین مختصر جایآنها نیست. برای‌اطلاع بیخثررجوع بداثرة المعارف‌اسلامذٍیل
5 نود . ملله های ترك که در ابران دورة اسلامی سلطنت کردماند : غزنوبان ( ۳۵۱ -
0 +) ۰ سلجوفیان ( 4۲4 - اواخر قرن شم )» خوارزهشاهیان(* 6۷ .)٩۲۸-‏
*_غلامان و کنیزان تر که نژاد زا بودند. بدین‌مناسبت تركیمعنی معشوق زباروی‌بکار رفته‌است.
کشند و باطل کردن عبارنی باشداز دفتر وحساب
دیوانی ۱ .
قر لك عبنتح اول و انی و سکون کاف »
خندقی را گویند که بردور حصار و باغ و قلعه
و اعشال | هکشب و نام رودخانه ایست تزدمكث بدر ژد
غروان؟ - وحلواب ی که از قند و نشاسنه و نشم
ربحان پزند؟ - و دخثر بکر و دوشیزه دا نیز
گونند - وصدای رعد - وهرصداً و آواز ی که
از ذکستن و ت رکیدن چیزی آبد۴ - و بمنی
رخنه وترالك باشد؟ - وحصفر ترهم‌هست که‌نقیض
خشك است- وب‌کون نائی کلاه خود باشد بعنی
کلاء آهنی که درروزهای‌جنگه برسرنهندوبعربی
مغفر خوآنند - و بخشها وسوزهای کلاه و خیمهت رکتازی
کوبته از جنی فرج یکه زدان ترك پوشند.
تر کتادی با تای قرشت بر وذن
مرخ بازی » تلخت آوردن بشتاب و تعجبل و می
خبروتا گاه باشدبرسبیل تاراج وغارت نمودن‌سوبمعنی
حولان کردن عم گفته‌اند ۱
قر لگ چوش » با جیم بر وزن سرخ
پوشی ۰ کوشت تیم پخته را کوندا -
قر لك جبی ۰ بکر تاك ۰ کنامد از
آخاب عالمثاب است -
تر لگ حصاری بکس اك وحای
بی نقطه ۰ کنابه از ماه امست و آفتاب ۳ نر
< فپ گس
برادر پیاز است که بمربی وم وفوم‌خوانند
‌ کش « بفتح‌اول و کاف بروزن‌سرکش:
مخفف تب رکش است ؟ که تبردان باشد .
تر کش جوداه ستارهابیرا کون
در برح‌جوزا که صورت تر کش وافم شده ائذ -
و تارهای روی سازها را نیز گفنه‌اند ۰
تر لگ قلاك - کنایه از کوک مین
است - ز آفتاب راهم کفته اند .
ولقب طابفه‌ای هم‌هست از ترکان‌بی‌اعتدال. گویند
این‌طایقه از اولاد ات بن نوح فسستل ‏
کویند
قر لگ ووستایان » کنابه از سیر | که‌کنابه ازک وکب مرخ باشد .
. ترك جوشی کرده‌ام من نیم خام از حکیم غزنوی شنو تمام‎ - ٩
۴ رگ : یر کش. مثنوی مولوی بلخی.
۴ - تر کمان با تر کمن نامفومی ادست ترله‌درآسیای مر کزی. این‌نام ازفرن پنمم‌هجری
(بلزدهم میلادی) تخت بشکل جمم فارسی «تر کمانان توسط نویسنه کان ابرانی مانند گردیزی
وابوالفضل بیپقی استصمال شده‌بهمان معنی که‌اغز درنر کی وغزدر عربی وفارسی بکار رفته. «یدانیم
که غزان نضت‌در مفولستان سکونت داشتند ودر کتسه‌های ارخون ۵۳۱00 متعلق بقرن‌هشتم
بلادی ذ کرابشان در مفولتان رفته . اغزان مزبور را نرك محسوب داشته اند نه نر کسان *
وت کمانانر! فقط درجانب‌مفرب اد کرده‌اند. نخست باتلفظ ۵-11-0008 ] در دائرتالمعارف
چیتی قرن هشتم میلادی (۷:60 - 18[ ضل ۱۹۳). بنول نونگ نين , کلم تو کومنگه
تلم دیگرست که بکشور 121 - لا بعنی کثشور آلانان اطلاق شده وابنان در آغاز ناریخ
میلادی درمشرق تا هسیر سفلی سیردربا متفر بودند وآنجا درفرن چهارم ه .(دهم میلادی) مفر
اسلی اتزان‌بود. در کب جفرافیابی عرب, تر کمان (التر کمان بااثتر کمانیون) ففط توسط مقدسی
(بد 274 , ]]] , 90۸) درشرح چندشهر واقم درشمال وشمال غربی *اربیجاب» باه‌سیرام*
کسوقم آدیدوست هعدن لسست : ح/ در یاب اصل کلمة تر کمان در فرن پنجم‌اط لاعی فداشتند
وایشکه آن را از تر کیب فارسی «ترك مانند » گرفته‌اه ( محمود کاشفری آ]] . ۳۰۷) وجه
اشتقاقی عامیانه است. ( همین وجه استقاق درمتن نفل شده).
بملت مهاجرت‌های تر کمانان بسوی مفرب, زبان وقیافةٌ آنان تعدیل‌شده بقمی که بن
ایشان وه نو کمانان فقط شباعتی مختصی بافی‌ماند. امروزه تر کمانان درآسیای‌مر کزی وشمال
کر کان‌وخرامان سکوت‌دارند. راث:دائرةالمعارف اسلام: 1۱1۲۴۳6۳6۵6 بقلم 82۲10018 ۷۷؛
سللمهای ت رکمان که درابران دورث اسلامی حکومت کرده‌اند : فره‌فوینلو (۷۸۰ -- ۸۷5 ه) »
آق‌قوینلو (۷۸۰- ۹۰۸ه).قاجاربه (۱۳۱۲ فعری ۱۳۰۶ شمی) .
: (بر هان فاطع )٩۱‏
رت۵
۷
۷
4
تاش 9ودرو غ باشد؟ .
ترك نیمرود » کنابه از آقتاب
جهان | راست و
```


## [2026-10-15T02:45:58.045Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} {n=split($0,a,\"\\n\"); for(i=1;i<=n;i++){ln++; if(ln==29600) print \"leaf(1-based) \" NR}; ln--}' BQT_v1_pages.txt; awk 'BEGIN{RS=\"\\f\"} NR==628 || NR==629 || NR==630 {print \"== \" NR; print substr($0,1,150)}' BQT_v1_pages.txt"
}
```


### [2026-10-15T02:45:58.607Z] TOOL RESULT

```
leaf(1-based) 714
== 628
لس ۱ « جنم اول و سکون ثالی مخفف
بسر است که درمقابل دختر باشد . #۶
فسا - بر وزن و معنی با باشد. و آن
شهریت درملك فاری وضا معرب آنست ۴ .
پساچین - با جیم
== 629
سا نیدن- بروزن «سانیدن, آب دادن
باغ وزراعت را کویند ۱ .
بی‌او کند . با واوه بروزن و همتی
ساو ند ۲ ‌ِ پروزن دما تد, قاف؛شمررا
گومند همحو دچار ونگار و ب
== 630
حمشوق است.
بی جانشین ۳ ۳
شخصی ات که چون صاحب دکان برخیزد او
یجای صاحب د کان بنشیند وکالا بقروشد
ی خم زدن - کنابه از کریختن
باشث .
ی دست گردن ۰ کنابه ا
```


## [2026-10-15T02:46:02.508Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 -c \"\nt=open('BQT_v1_pages.txt').read()\nimport re\nfor ln in (29300,29600,31679):\n  pos=sum(len(l)+1 for l in t.split('\\n')[:ln-1]); print(ln, t[:pos].count('\\f'))\n\"; awk 'BEGIN{RS=\"\\f\"} NR==707 {print substr($0,1,400)}' BQT_v1_pages.txt | head -5"
}
```


### [2026-10-15T02:46:03.052Z] TOOL RESULT

```
29300 707
29600 713
31679 759
ی
تر اژوی دد - کنابه از آقاب
تراش - بقتح اول بروزن نواش " طمع
و نوقع وتراشده شده را گویند؟ -
تر ارو!۱ ه معروف است ؛ ون آلتي
```


## [2026-10-15T02:46:06.792Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^ *(تُرد|ترد|تُرب|ترب|تُرک|ترک)\\b' MON_part1.txt | head; grep -n -E 'ترد ' MON_part1.txt | head -5"
}
```


### [2026-10-15T02:46:07.155Z] TOOL RESULT

```
833:ترکسی داشته باشند مولد اکسیژن. آب 
4836:ترکیبات ازت است که در هوای شهرها و 
4842:ترکسات آمونباک مسجموعه بنام 
7166:ترکیب در اصل «اثنان عشر» بوده» نون به 
7510:ترکیب عناصر اربعه و تأثیرات اجسام و 
7754:ترکث زندگی بدوی و بیابانی گفتن. از سفر 
8431:ترکیب کردن دو يا چند جسم با یکدیگر 
9628:تردید گردیدن کمان داد و 
10946:ترکیب اضافی به فک اضافه) وسیله‌ها و 
11318:ترکیه بدان سخن می‌گویند و با ترکی معمول 
74541:ترد هر دو فرقه غیر سالم. اسا «باع» نزه 
85224:نمک و فلفل ریزند تا ترد شود. سپس چهار
```


## [2026-10-15T02:46:09.809Z] TOOL CALL #32: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-10-15T02:46:09.822Z] TOOL RESULT

```


```


## [2026-10-15T02:46:11.791Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/ترب",
 "prompt": "Give the Persian etymology section(s) verbatim, including Middle Persian forms and cited sources, and any mention of Turkish turp."
}
```


## [2026-10-15T02:46:12.446Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/ترد",
 "prompt": "Give the Persian etymology section verbatim (meaning crisp/brittle, tord/turd), with cited sources."
}
```


## [2026-10-15T02:46:13.496Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/ترک",
 "prompt": "Give the Persian etymology for turk 'Turk' verbatim, including Middle Persian form and senses like 'beloved, beautiful'."
}
```


## [2026-10-15T02:46:14.630Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Türk",
 "prompt": "Give the etymology sections for Old Turkic / Turkish Türk verbatim, including Chinese Tujue and theories of origin (e.g. 'strength', 'helmet')."
}
```


## [2026-10-15T02:46:15.204Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/τολύπη",
 "prompt": "Give the Ancient Greek etymology verbatim (Beekes etc.)."
}
```


## [2026-10-15T02:46:15.757Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/tardus",
 "prompt": "Give the Latin etymology section verbatim (de Vaan)."
}
```


### [2026-10-15T02:46:19.388Z] TOOL RESULT

```
# Latin Etymology Section (de Vaan Reference)

The etymology section cites de Vaan as follows:

"De Vaan notes the etymology remains 'uncertain' due to the lack of direct cognates with the specific meaning of 'slow' in other branches."

This appears in a footnote referencing:

De Vaan, Michiel (2008), "tardus", in *Etymological Dictionary of Latin and the other Italic Languages*, Leiden, Boston: Brill, page 607.

The page does not provide the verbatim text from de Vaan's work itself—only this secondary reference to his observation about etymological uncertainty.
```


### [2026-10-15T02:46:20.800Z] TOOL RESULT

```
# Ancient Greek Etymology of τολύπη

According to the Wiktionary source, Beekes states: "the word must belong to the Pre-Greek substrate, which must have spoken in large parts of Anatolia as well."

The entry also notes several proposed etymological connections:

- **Maurice's theory**: Links it to τυλυφάντης (tuluphántēs, "cushion-cover weaver"), with possible influence from κορύνη or τορύνη to explain the vowel pattern.

- **Furnée's comparison**: Connects it to Luwian *taluppi* ("clump of dough").

- **Melchert's suggestion**: Proposes a relationship with Hittite *tarupp* ("to gather, collect") and its rare variant *talupp*.

The consensus view, per Beekes, is that this ancient Greek word derives from a Pre-Greek substrate language that was spoken across much of Anatolia.
```


### [2026-10-15T02:46:21.662Z] TOOL RESULT

```
# Etymology Information for Türk

Based on the Wiktionary page provided, here's what's available:

## Turkish Etymology Section

The page states that Turkish **Türk** is "Inherited from Ottoman Turkish ترك/تورك (Türk), ultimately from Proto-Turkic *tür(ü)k." It notes cognates with Old Turkic 𐱅𐰇𐰼𐰜 (t²ẅr²ẅk² /türük/) and Chuvash тӗрӗк (tĕrĕk), plus Hungarian török as "an ancient Turkic borrowing."

## What's Missing

The provided webpage does **not contain** etymological information about:
- Chinese "Tujue" references
- Theoretical origins such as meanings like "strength" or "helmet"
- Old Turkic-specific etymology beyond the cognate mention

The etymology section traces the word back to Proto-Turkic *tür(ü)k but doesn't explain the proto-form's meaning or any competing theories about its ultimate origin. To find discussions of those alternative theories, you would need to consult additional scholarly sources beyond this Wiktionary entry.
```


### [2026-10-15T02:46:23.450Z] TOOL RESULT

```
# Persian Etymology of ترک (turk)

**Etymology 2** traces this word to Middle Persian with the form listed as "twlk' /⁠Turk⁠/" (script not provided in the source).

The word inherited this term "from [Middle Persian](https://en.wikipedia.org/wiki/Middle_Persian "w:Middle Persian")" and it derives ultimately from Proto-Turkic origins through Old Turkic.

**Primary senses** include:
- A person of Turkic ethnicity or heritage
- In poetic usage, "the [beloved]," often depicted as a beautiful but cruel Turkish warrior who destroys the lover's heart

An archaic, figurative poetic sense also refers to Mars as a planet, called "**tork**\-e čarx" (literally, "the **Turk** of heaven").
```


### [2026-10-15T02:46:24.109Z] TOOL RESULT

```
# Persian Etymology Section

## Etymology

The entry states the word derives "From [Turkic](https://en.wikipedia.org/wiki/Turkic_languages "w:Turkic languages"), see [Ottoman Turkish](https://en.wikipedia.org/wiki/Ottoman_Turkish "w:Ottoman Turkish") _[تورپ](/wiki/%D8%B7%D9%88%D8%B1%D9%BE#Ottoman_Turkish "طورپ")_ (turp)."

The scholarly analysis notes: "Intuited shakily by Laufer by Doerfer and Clauson to be an [Iranian](https://en.wikipedia.org/wiki/Iranian_languages "w:Iranian languages") borrowing in Turkic, in view of internal etymological opacity of the term in Turkic and the Persian variant _turf_, which we reckon to be a secondary variant like _[شفدر](/w/index.php?title=%D8%B4%D9%81%D8%AF%D8%B1&action=edit&redlink=1 "شفدر (page does not exist)")_ (šafdar) for _[شبدر](/wiki/%D8%B4%D8%A8%D8%AF%D8%B1#Persian "شبدر")_ (šabdar)."

Related forms are listed in Kurdish, Zazaki, Talysh, and Armenian, suggesting broader regional linguistic connections.

**Note:** No Middle Persian forms appear in this entry; the documentation focuses on Turkic origins and cross-linguistic variants.
```


### [2026-10-15T02:46:29.847Z] TOOL RESULT

```
# Persian Etymology Section

Based on the Wiktionary entry, here is the Persian section verbatim:

**Word:** ترد (turd / tord)

**Part of Speech:** Adjective

**Definition:** "brittle, fragile, delicate"

**Pronunciation:** /ˈturd/ (Classical Persian); [t̪ʰoɹd̪̥] (Iranian formal)

**Derived terms include:**
- تردک (turdak / tordak) — "cracker"
- تردی (turdī / tordi) — "brittleness, fragility"
- نان ترد (nān-i turd / nân-e tord) — "crispbread"

**Cited Sources:**
1. Hayyim, Sulayman (1934), *New Persian–English dictionary* (Tehran: Librairie-imprimerie Béroukhim)
2. Steingass, Francis Joseph (1892), *A Comprehensive Persian–English dictionary* (London: Routledge & K. Paul)
```


## [2026-10-15T02:46:32.602Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/tardus",
 "prompt": "Quote the full Latin Etymology paragraph exactly, including any proposed PIE root."
}
```


## [2026-10-15T02:46:33.721Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Turk",
 "prompt": "Quote the etymology of Turk verbatim (Persian, Greek, Latin, French routes; Chinese Tu-kin etc.)."
}
```


## [2026-10-15T02:46:34.430Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/turkey",
 "prompt": "Quote the etymology of turkey (bird and country) verbatim."
}
```


## [2026-10-15T02:46:34.850Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/turquoise",
 "prompt": "Quote the etymology verbatim."
}
```


## [2026-10-15T02:46:35.563Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/sard",
 "prompt": "Quote the etymology of sard verbatim (Sardis, sardios, Persian?)."
}
```


## [2026-10-15T02:46:36.511Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Σάρδεις",
 "prompt": "Quote the etymology of Sardis verbatim, including Lydian Sfard, Old Persian Sparda and any proposed meaning."
}
```


### [2026-10-15T02:46:36.986Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-10-15T02:46:36.995Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-10-15T02:46:37.000Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-10-15T02:46:37.005Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-10-15T02:46:39.738Z] TOOL RESULT

```
# Latin Etymology of "tardus"

According to the Wiktionary entry, the etymology section states:

"From Proto-Italic *tardos, from Proto-Indo-European *tr̥h₂-d-o-s, from the root *terh₂- ("to cross over, pass through, overcome")."

The entry explains that the phonetic development follows standard Latin patterns where a syllabic liquid followed by a laryngeal (*r̥h₂) becomes -ar-. The semantic shift likely occurred from meanings like "drawn out" or "taking a long time to cross/endure" toward the modern sense of "slow" or "late."
```


### [2026-10-15T02:46:41.116Z] TOOL RESULT

```
# Etymology of Sardis

According to the Wiktionary entry, the etymology is as follows:

"From earlier *Σϝάρδ- (*Swárd-), ultimately from pre-Lydian *Swar-, parallel with Old Persian 𐎿𐎱𐎼𐎭 (s-p-r-d /⁠Spardaʰ⁠/), and whence Lydian 𐤮𐤱𐤠𐤭 (sfar, 'Sardis')."

The term traces back to a proto-form meaning the city itself across multiple ancient languages. No specific semantic meaning beyond the place name is provided in the source material.
```


## [2026-10-15T02:46:44.692Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /tmp; curl -s 'https://en.wiktionary.org/w/index.php?title=tardus&action=raw' | sed -n '/==Latin==/,/===Pron/p' | head -15; for w in Turk turkey turquoise sard quartz; do echo \"== $w\"; curl -s -A 'Mozilla/5.0' \"https://www.etymonline.com/word/$w\" | python3 -c \"import sys,re,html;t=sys.stdin.read();m=re.findall(r'<section[^>]*>(.*?)</section>',t,re.S);print(html.unescape(re.sub('<[^>]+>','',' '.join(m)))[:900])\"; done"
}
```


### [2026-10-15T02:46:45.459Z] TOOL RESULT

```
==Latin==

===Etymology===
{{ety|la|:inh|itc-pro:*tardos<ety:inh<ine-pro:<alt:*tr̥h₂dos><ety:from<*terh₂->>>>}}
From {{inh|la|itc-pro|*tardos}}, from {{der|la|ine-pro||*tr̥h₂-d-o-s}}, from the root {{m|ine-pro|*terh₂-||to cross over, pass through, overcome}}. 

The phonetic development follows the regular Latin outcome of a syllabic liquid followed by a laryngeal ({{m|ine-pro||*r̥h₂}} > {{m|la||-ar-}}). Semantically, the word likely shifted from {{mg|drawn out}} or {{mg|taking a long time to cross/endure}} to {{mg|slow}} or {{mg|late}}. Cognate with {{cog|sa|तरति|tr=tárati||crosses over, overcomes}} and {{cog|grc|τρανής||piercing, clear, distinct}}. 

While this is the standard Indo-European reconstruction, [[w:Michiel de Vaan|De Vaan]] notes the etymology remains "uncertain" due to the lack of direct cognates with the specific meaning of {{mg|slow}} in other branches, and an {{der|la|ett|-}} origin has occasionally been suggested.<ref>{{R:itc:EDL|page=607|head=tardus}}</ref>

===Pronunciation===
== Turk

== turkey

== turquoise

== sard

== quartz
```


## [2026-10-15T02:46:49.117Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /tmp; for p in Turk turkey turquoise quartz sard turp 'Reconstruction:Proto-Slavic/tvьrdъ' '突厥' 'σάρδιον' 'Reconstruction:Proto-Turkic/türk'; do echo \"=================== $p\"; curl -s \"https://en.wiktionary.org/w/index.php?title=$(python3 -c \"import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))\" \"$p\")&action=raw\" | grep -i -A4 -E '===Etymology' | head -40; done 2>&1 | cut -c1-700"
}
```


### [2026-10-15T02:46:51.581Z] TOOL RESULT

```
=================== Turk
===Etymology===
From {{inh|en|enm|Turke}}, {{m|enm|Turk}}, from {{der|en|fro|Turc}}, from {{der|en|la-med|Turcus}}, from {{der|en|gkm|Τοῦρκος}}, from {{der|en|fa-cls|تُرْک}}, from {{der|en|pal|tr=twlk'|ts=turk}}, from {{der|en|otk|𐱅𐰇𐰼𐰜}}. See {{m+|trk-pro|*tür(ü)k}} for more.

===Pronunciation===
* {{IPA|en|/tɝk/|a=GenAm}}
=================== turkey
===Etymology===
{{etymon|en|:from|Turkey}}
{{multiple images
|direction = vertical
|image1 = Gall-dindi.jpg
=================== turquoise
===Etymology===
[[Image:Turquoise_with_quartz.jpg|thumb|right|220px|Turquoise with [[quartz]] (1)]]
From {{bor|en|frm|turquoise}}, from {{der|en|fro||([[pierre]]) [[turquois]]e|Turkish (stone)}}, from {{suf|fro|turc|ois|nocat=1}}. The stone, mined near {{w|Nishapur}} in the [[Khorasan]] region of [[Persia]], was originally brought to Europe through [[Turkey]]. {{doublet|en|Turkish}}.

Compare typologically {{m|en|copper}} (<< {{m+|grc|Κύπρος||[[Cyprus]]}}).
--
===Etymology===
{{inh+|fr|fro|turquois}}, from {{af|fro|turc|-ois|nocat=1}}.

===Pronunciation===
* {{fr-IPA}}
--
===Etymology===
{{ubor|id|fr|turquoise}}, from {{der|id|fro|turquois}}, {{af|fro|turc|-ois|nocat=1}}.

===Noun===
{{head|id|noun}}
--
===Etymology===
From {{bor|lb|fr|turquoise}}.

===Pronunciation===
* {{IPA|lb|/ˈtyrˌkvaːs/|[ˈtyχˌkwaːs]}}
--
===Etymology===
Inherited from {{inh|frm|fro|turquois}}.

===Noun===
{{frm-noun|f}}
=================== quartz
===Etymology===
From {{bor|en|de|Quarz}}, from {{uder|en|gmh|-}} (Central East German) {{m|gmh|quarz}}, {{m|gmh|twarc}}, from a {{uder|en|zlw|-}} language [compare {{cog|pl|twardy||hard}}, {{cog|cs|tvrdý||hard}}], from {{der|en|sla-pro|*tvьrdъ}} ultimately from {{der|en|ine-pro|*twerH-|t=to enclose, grab}}.

===Pronunciation===
* {{IPA|en|/k(w)ɔːts/|a=RP}}
--
===Etymology===
{{bor+|fr|de|Quarz}}, from a {{der|fr|zlw|-}} language, from {{der|fr|sla-pro|*tvьrdъ|t=hard}}.

===Pronunciation===
* {{fr-IPA|qwartce}}
=================== sard
===Etymology 1===
From {{inh|en|enm|sarde}}, borrowed from {{der|en|fro|sarde}}, from {{der|en|la|sarda}}, {{m|la|sardius}}. {{doublet|en|sardius}}.

====Noun====
{{en-noun|~}}
--
===Etymology 2===
From {{inh|en|enm|serden}}, from {{inh|en|ang|seorþan|t=to violate, rape}}, from {{der|en|gem-pro|*serþaną}}, from {{der|en|ine-pro|*sert-|t=to hit}}.

====Verb====
{{en-verb}}
--
===Etymology 1===
{{ety|ca|:lbor|la:sardus}}
{{lbor|ca|la|sardus}}.

====Adjective====
--
===Etymology 2===
[[File:Diplodus sargus01.jpg|thumb]]
By confusion with {{m|ca||sard|Sardinian}}, from {{m|ca|sarg}}, from {{der|ca|la|sargus}}.

====Noun====
--
===Etymology===
Related to {{cog|fa|سرد|tr=sard}} from {{cog|pal|slt'}}.

===Adjective===
{{h|ckb|adj}}
--
===Etymology===
{{ety|ro|:bor|fr:Sarde|text=+|tree=1}}

===Adjective===
{{ro-adj}}
--
===Etymology===
{{bor+|sv|la|sardus}}. {{doublet|sv|sardin|sardell}}.

===Pronunciation===
=================== turp
===Etymology===
From {{der|sq|la|turpis}}.

===Noun===
{{sq-noun|m}}
--
===Etymology===
From {{inh|az|trk-pro|*turp}}.

===Pronunciation===
* {{audio|az|LL-Q9292 (aze)-Azerbaijani audiorecordings-turp.wav|a=Baku}}
--
===Etymology===
From {{suffix|lv|tur|p|gloss1=there}}.

===Pronunciation===
{{rfap|lv}}
--
===Etymology===
{{inh+|tr|ota|طورپ|tr=turp|t=radish}}, from {{inh|tr|trk-pro|*turp|t=radish}}. Analyzable as [[durmak]] + [[-ip]], a suffix present in select words (see [[alp]], [[çöp]].)

Cognate with {{cog|ky|турп||radish}}, {{cog|az|turp||radish}}, {{cog|tk|turp||radish}}, etc. Compare also {{cog|hu|torma|t=[[horseradish]]}}, {{cog|fa|ترب|t=radish|tr=torob}}, [https://starling.rinet.ru/cgi-bin/response.cgi?single=1&basename=%2fdata%2falt%2fturcet&text_number=401&root=config Turkic borrowings].

=================== Reconstruction:Proto-Slavic/tvьrdъ
===Etymology===
{{ety|sla-pro|:inh|ine-bsl-pro:*twirˀtás}}
From {{inh|sla-pro|ine-bsl-pro|*twirˀtás}}, from {{inh|sla-pro|ine-pro|*twerH-}}.

Baltic cognates include {{cog|lt|tvìrtas}}, {{cog|lv|tvir̂ts||strong, firm, solid}}.
=================== 突厥
===Etymology===
Ultimately from a form which also gave rise to the name ''[[Türk]]'' (cf. {{m|otk|𐱅𐰇𐰼𐰜|tr=Türük}}), but the phonetics are difficult to reconcile.

It has been suggested that this is a transcription of {{cog|mis-rou|*türküt}}, a plural of the Mongolic type, composed of  {{suf|xgn-pro|*türk|*-üt}} (cf. {{cog|mn-kha|-үүд}}) ({{zh-ref|Pelliot, 1915}}). {{zh-ref|Pulleyblank (1965)}} proposed that this is a direct transcription of ''Türk''.

=================== σάρδιον
===Etymology===
{{ety|grc|:af<unc>|Σᾰ́ρδεις|-ῐον<pos:diminutive suffix>}}
Probably from {{af|grc|Σᾰ́ρδεις<t:[[Sardis]]>|-ῐον<pos:diminutive suffix>}}, because it was its place of origin.

===Pronunciation===
=================== Reconstruction:Proto-Turkic/türk
```


## [2026-10-15T02:46:59.614Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming; grep -n -E 'ترب|ترد|ترک' ARY/ARY_pages.txt | head -20; grep -n -i -E '\\bTOROB|\\bTORD\\b|\\bTORK\\b' ARY/ARY_latin_index_pages.txt | head; grep -n -i -E '\\bturp\\b|turub' TTS/TTS_vambery1878_uoft_djvu.txt | head"
}
```


### [2026-10-15T02:47:00.238Z] TOOL RESULT

```
28:شترکك» واژه‌های همريشه در زبان‌های سانسکریت و ارمنی و یونانی ولاتین و آلمانی و انگلیسی و
52:تبایل ترکك زبان (از حدود سده‌ی پنج میلادی به بعد) موجب از میان رفتن آن زبانهای محلی گردیده
79:ترکیپب (هند و آریایی (13100-۸837۸3) بکار می‌رود.
116:نکات زیر درستی دیدمان فوق را مورد تردید قرار می‌دهد: ۱- کردستان وارمشتان و نواحی
146:آیا خاستگاه مردمان هند و اروپایی در سرزمین‌های‌گسترده‌ی شمال . .
172:زبان‌های گوناگون شد. (وجود واژه‌های مشترک میان هند و اروپایی و زبان سامی آغازین
177:فرهنگی و زبانشناسی آنها را روشن می‌کند. بررسی کوچگری مردمان ترکك زبان مثال بسیار مفیدی
178:اس است: درفرن, ششم پس از میلاد» مردم ترک زبان فقً در ناحيه‌ي نسبتاً کوچکی در شمال مغولستان و
182:شدند. مردمان این نواحی (مثلا ساکنان آذربایجان و ترکیه) همه به زبانهای هند و اروپایی تکلم
183:می‌کردند ولی سلطه‌ی ترکك زبانان موجب شدکه طی چند قرن زبان آنها ترکی بشود ولی زبان ترکی
186:این نواحی نیز متقابلاً تحت تأثیر زبانهای محلی قرا رگرفت وکم کم به چندگویش تبدیل شد (ترکی
187:اسلامبولی و ترکی ترکمنی و آذری و غیره).
189:می‌دهد که مردم ترکیه (و شاید مردم آذربایجان) از نظر زادشناختی (0138287109) فقط دارای سی.
190:درصد ژن ترکك (نژاد خاور دور پا زرد) و هفتاد درصد ژن هندو اروپایی وغیره هدن 2
200:گسترش سریح قبایل ترکك نشان می‌دهد که سرعت تهاجم و تصاحب می‌تواند :
215:تردید قرار می‌دهد این است: زبان هند و اروپایی تخاری (10077۸131۸31) که در ترکستان چین "
221:نبست. دلیل دیگر» واژه‌ی «ماره در اکثر زبانهای «ستتم» مشترکك است (لاتین: ۵1۸712 ایرلندی
235:... زبانی‌های واقع در خاور خود (یعنی بالتیک و اسلاوی) دارند. به عبارت دیگر تربیت جغرافیایی. :
258:هزارهی گذشته (به استتنای هجوم و ماندگری قبایل ترک و مجار و فنلاندی) تغییر زیادی نگرده است
293:است. واژه‌های همریشه‌ی دیگر نیز در شناخت ماهیت هند و اروپائیان سودمنداند: واژه‌های مشترک
```


## [2026-10-15T02:47:03.445Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming; grep -n -E '^\\s*(ترد|ترب|ترک|تُرد)' ARY/ARY_pages.txt | head; grep -n -i -E 'tord|torob|turd' ARY/ARY_latin_index_pages.txt | head -5; grep -n -E 'turt|tvirt' ../ARY* 2>/dev/null | head -2; grep -n -i -E 'radish' ../SYN.txt | head -5"
}
```


### [2026-10-15T02:47:04.000Z] TOOL RESULT

```
79:ترکیپب (هند و آریایی (13100-۸837۸3) بکار می‌رود.
215:تردید قرار می‌دهد این است: زبان هند و اروپایی تخاری (10077۸131۸31) که در ترکستان چین "
729:ترکی) ز همچنین بهواسطه‌ی تطور طبیعی زبان» زبان پهلوی تبدیل ه فارسی نوین شد. امروزه مد
8227:ترکی و از ترکی به این زبان‌های انطال یافته است. ۱
5788:TORDEN (SWEDISH) «538 y+ STENEIN, STENO = (GREEK) gli,
5789:TORDNE (NORWEGIAN) 5335 TONARE, TONO LATIN) oy
5808:TORDEN (DANISH) ails
10108:TURD ASTOR KURDISH) 53,6
(eval):1: no matches found: ../ARY*
5502:| radish’, as applied first to the similar
9440:Grk. pédavos (Att. for xpauBn), beside jadov's ‘radish’ : pdms, padus ‘a fing. of turnip’, Dor. saga ‘a kind of radish’, Lat. rgpum ‘rape, turnip’, OHG ruoba, NHG (weisse) ribe ‘turnip’, rote riibe ‘beet’, geloe riibe ‘carrot’. Walde-P. 2.341. Emout-M. 852.
```


## [2026-10-15T02:47:06.131Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming; sed -n 10100,10112p ARY/ARY_latin_index_pages.txt; grep -n -E '\\[pdf page' ARY/ARY_latin_index_pages.txt | awk -F: '$1<10108' | tail -1"
}
```


### [2026-10-15T02:47:06.473Z] TOOL RESULT

```
oie Sib
[pdf page 348]
4
\
YA | oe |
TJOR, TYR (NORWEGIAN) «5}4,: STAORA., STAWRA-:(AVESTAN) .gl-3!
STIE (DUTCH) sacha STOR PAHLAVI) <5 slgy
(OLD CHURCH SLAVIC) 5 53+ STURTA HOSSETIC) gm!
TURD ASTOR KURDISH) 53,6
TAURAS — (44U)(LITHUANIAN) gi SUTUR AFGHANI) (gu) lai!
(4LE}(OLD PRUSSIAN) AS gd. STHAVIRAS (SANSKRIT) cy Sits
TAURIS STHAURIN ARMENIAN) 5s)
TARB —(4L4}(OLD IRISH) oyS 5.) p\ TADROS (ayLEY(GREEK) gb y,
10101:[pdf page 348]
```


## [2026-10-15T02:47:08.783Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'Sparda' KNT_full.txt | head -5; grep -n -E 'Sparda' BRT.txt | head -3"
}
```


### [2026-10-15T02:47:09.155Z] TOOL RESULT

```
2886:Sparda, haumavargd: many of these confirmed 
7699:Skudra-, Sparda-, Zazüna-, Züzahya-, Zra*ka-, 
7811:to Maka-; Spard-iya- to Sparda-; Haxámanis- 
8630:Yauna ‘Ionia’ or Yaund ‘the Ionians'; Sparda 
8724:Sparda Spardtya
```


## [2026-10-15T02:47:10.969Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^Sparda|Sparda-' KNT_full.txt | head; grep -n -E 'Sardis' KNT_full.txt | head -5"
}
```


### [2026-10-15T02:47:11.295Z] TOOL RESULT

```
2886:Sparda, haumavargd: many of these confirmed 
7699:Skudra-, Sparda-, Zazüna-, Züzahya-, Zra*ka-, 
7811:to Maka-; Spard-iya- to Sparda-; Haxámanis- 
8724:Sparda Spardtya 
8909:Sparda, Mudráyà, Küsa, Yaun, Gadard, Kar- 
29269:Sparda- sb. ‘Sardis’, a province of the Persian 
8631:‘Sardis, Lydia’; Skudra ‘Thrace and Mace- 
12201:Sardis’; but cf. $270.П. 
16943:are beside the sea, Sardis, Ionia, Media, Armenia, 
19195:Armenia, Cappadocia, Sardis, Ionians who are 
19244:Sind, thence unto Sardis—which Ahuramazda the
```


## [2026-10-15T02:47:13.378Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 29269,29275p KNT_full.txt; grep -n -i -E 'Sparda' BRT.txt | head -3; grep -n -E 'Sardes|Sard' BRT.txt | head -5"
}
```


### [2026-10-15T02:47:13.795Z] TOOL RESULT

```
Sparda- sb. ‘Sardis’, a province of the Persian 
Empire: Elam. iš-par-da, АКК. sa-par-du, Gk. 
Убрбеѕ ($31); with *Sy-, seen in Lydian Sfard- 
(MB Gr. $52; Hz. AMI 3.68-4). See also Spar- 
diya-. Sparda nsm. DB 1.15; DPe 12; DNa 28; 
DSe 27°; DSm 7°; XPh 22. Spardà absm. DPh 
7f; DSf 36; DH 6. 
26852:•  p.  sparda-  m.  Name  eines  Lands*': imn  dahyäva^  iyä  adam  *adarsiy  .  . artninJ'  katpaluk^  'da"  yauna  D.  5.  2 ; 6.  3,  Bh.  /.  6.
```


## [2026-10-15T02:47:18.078Z] TOOL CALL #53: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe-private/site/pages/514.* 2>/dev/null; python3 -c \"\nfrom PIL import Image;im=Image.open('/home/sfmqrb/git/rishe-private/site/pages/514.jpg');print(im.size)\""
}
```


### [2026-10-15T02:47:18.707Z] TOOL RESULT

```
Exit code 1
Permissions Size User   Date Modified Name
.rw-r--r--   60k sfmqrb 14 Oct 22:15  /home/sfmqrb/git/rishe-private/site/pages/514.jpg
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    from PIL import Image;im=Image.open('/home/sfmqrb/git/rishe-private/site/pages/514.jpg');print(im.size)
    ^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'PIL'
```


## [2026-10-15T02:47:19.930Z] TOOL CALL #54: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/site/pages/514.jpg"
}
```


### [2026-10-15T02:47:19.960Z] TOOL RESULT

```

```


## [2026-10-15T02:47:25.439Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/ترد",
 "prompt": "Quote Mo'in's entry for تُرد (tord) verbatim, including any origin tag like [په.]."
}
```


## [2026-10-15T02:47:26.231Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/ترب",
 "prompt": "Quote Mo'in's entry for تُرب (torb/torob, radish) verbatim, including origin tag."
}
```


### [2026-10-15T02:47:28.642Z] TOOL RESULT

```
# Definition of ترد (Tord)

According to Mo'in's Dictionary, **ترد** (tord) is defined as:

"تر و تازه" (fresh and moist) and "هر چیزی که زود شکسته گردد" (anything that breaks easily).

The entry is marked with (تُ) indicating pronunciation and (ص.) (عا.) denoting it as a common/colloquial term.
```


### [2026-10-15T02:47:29.167Z] TOOL RESULT

```
# Mo'in Dictionary Entry for ترب (Torb)

According to the Mo'in Publishing Dictionary (Farhang-e Entesharat-e Mo'in), the entry reads:

"گیاهی است یک ساله با برگ های درشت و ریشة چغندر مانند به رنگ های سفید و سیاه که دارای طعم تند و تیزی می باشد"

This defines torb as an annual plant featuring large leaves and a beet-like root system, typically white or black in color, characterized by a sharp, pungent taste. The word refers to the radish plant in Persian.
```


## [2026-10-15T02:47:29.974Z] AGENT

Now archive the sources.


## [2026-10-15T02:47:38.357Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; F=tools/fetch_source.py; \npython3 $F 'https://en.wiktionary.org/wiki/ترد' --note 'page 514, root Tuardo: Persian tord brittle, no etymology given' ;\npython3 $F 'https://en.wiktionary.org/wiki/ترب' --note 'page 514, root Tulupos: Persian torob from Turkic turp (or reverse per Laufer/Doerfer/Clauson)';\npython3 $F 'https://en.wiktionary.org/wiki/ترک' --note 'page 514, root Tu-kue: Persian turk from MP twlk from Old Turkic; poetic beloved sense';\npython3 $F 'https://en.wiktionary.org/wiki/Türk' --note 'page 514, root Tu-kue: Proto-Turkic *tür(ü)k';\npython3 $F 'https://en.wiktionary.org/wiki/突厥' --note 'page 514, root Tu-kue: Chinese Tujue is a transcription of Turkic Türk(üt)';\npython3 $F 'https://en.wiktionary.org/wiki/Turk' --note 'page 514, root Tu-kue: English Turk chain via OFr Turc, ML Turcus, MGk Tourkos, Persian turk';\npython3 $F 'https://en.wiktionary.org/wiki/turkey' --note 'page 514, root Tu-kue: turkey bird from Turkey';\npython3 $F 'https://en.wiktionary.org/wiki/turquoise' --note 'page 514, root Tu-kue: turquoise from OFr turquoise Turkish stone';\npython3 $F 'https://en.wiktionary.org/wiki/τολύπη' --note 'page 514, root Tulupos: Beekes Pre-Greek';\npython3 $F 'https://en.wiktionary.org/wiki/turp' --note 'page 514, root Tulupos: Turkish turp from Proto-Turkic *turp';\npython3 $F 'https://en.wiktionary.org/wiki/tardus' --note 'page 514, root Tuardo: Latin tardus etymology uncertain (de Vaan)';\npython3 $F 'https://en.wiktionary.org/wiki/Σάρδεις' --note 'page 514, root Tuardo: Sardis, OP Sparda, Lydian Sfard place name';\npython3 $F 'https://en.wiktionary.org/wiki/σάρδιον' --note 'page 514, root Tuardo: sardion from Sardis';\npython3 $F 'https://en.wiktionary.org/wiki/quartz' --note 'page 514, root Tuardo: Quarz from West Slavic twardy, PSl *tvьrdъ';\npython3 $F 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Slavic/tvьrdъ' --note 'page 514, root Tuardo: PSl tvьrdъ from PIE *twerH-';\npython3 $F 'https://vajehyab.com/moein/ترد' --note 'page 514, root Tuardo: Mo in entry tord';\npython3 $F 'https://vajehyab.com/moein/ترب' --note 'page 514, root Tulupos: Mo in entry torb' 2>&1 | tail -3"
}
```


### [2026-10-15T02:47:53.853Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/302e19983ccf6e74.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3fb219d0d3664acf.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/5ea48c215adc2372.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/448c0321389cc220.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a9963311cbe400f9.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/fe8c76428041c208.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a72b548533de44b5.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a09990f1d171a331.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/17a9b071fc292210.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/9ecc744f17afee69.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2e7c9ea2a29819f1.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/1eee01a5a7823fa3.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/7769176748991b09.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/903e428076fd1021.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/5a6f81fce091e78a.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/25a392de80337947.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/500bbc3893c50ec9.txt
```


## [2026-10-15T02:47:58.726Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'tolyp|xoXu|τολυ|toAu' incoming/WLD/WLD_Bd1_pages.txt incoming/WLD/WLD_Bd2_pages.txt WLD_band3.txt POK_full.txt AHD_watkins1985.txt | head; grep -n -i -E 'twer|tuer' AHD_watkins1985.txt | head -5; grep -n -i -E 'sardi|Sardis' AHD_watkins1985.txt | head -3"
}
```


### [2026-10-15T02:47:59.235Z] TOOL RESULT

```
POK_full.txt:6932:following kin in: 6p5£U) " put on a fabric ', opSiKOv tov xitcjovIgkov. Dapioi, 6p5r||JC( n ToAunr) 
POK_full.txt:78863:'rinnend, flowing ', vaETwp pscov, TToAuppoo(; Hes., Attic Vok. varop m. "stream', vapa 
127:complete agreement on the numerals from two to ten: dwo- (*duw6), trei- (*treyes), kvetwer- (*k”etwores), penk”e, s(w)eks, septm, oktd(u), newn, dekm. For the nu- meral “one” the dialects vary. We have a root sem-' in some derivatives, while the western Indo-European languages Germanic, Celtic, and Latin share the form oi-no-. The word for “hundred,” formed from dekm, “ten,” was *(d)kmtom. No common form for “thousand” or any other higher number can be reconstructed for the protolanguage.
320:battuere
321:yawn, gape: BAY2, BEVEL; ABASH, ABEYANCE. 2. Possibly Vulgar Latin *abbaidre (> Old French (a)baiier), to bay: BAY‘*.] [battuere. To beat. Latin verb of unknown origin. (BATE?), BATTER!, (BATTER’), (BATTERY), BATTLE; ABATE, COMBAT, DEBATE, (RABBET), (REBATE?), (RE- BATO).] bel-. Strong. 1. Suffixed o-grade form *bol-iyo- in Russian bol’shoi, large: BOLSHEVIK. 2. Prefixed form *dé-bel-i- (dé-, privative prefix; see de-), “without strength,” in Latin débilis, weak: DEBILITATE, DEBILITY. [Pok. 2. bel- 96.] bend-. Protruding point. 1. Germanic *pannja-, “struc- ture of stakes,” in Old English penn, pen for cattle: PEN2. 2. Germanic *pund- possibly in Old English pund- (> Middle English pound), pundfald, enclosure for stray animals: POND, POUND3; IMPOUND, PINFOLD. 3. Germanic *pin- in Old English pintel, penis: PINTLE. [Pok. bend- 96.) beu-'. Also bheu-. Appears in words loosely associated with the notion “to swell.” I. Root form *beu-. 1. Ger- manic *puk- in: a. Old English pocc, pustule: POCK; b. Old French po(u)che and Old North French poke, bag: POACH!, POCKET, POKE3, POUCH, (PUCKER). 2. Old Eng- lish pyffan, to blow out: puFF. 3. Old English -piite, “fish with large head” (in aele-piite, eelpout): pouT?. II. Root form *bheu- with various Germanic derivatives. 1. Old English bdsm, bosom: Bosom. 2. Old English biic, belly, pitcher: BUCKBOARD. 3. Frankish *biak (> Old French buc), trunk of the body: TREBUCHET. 4. Old English bye), pustule: BorL?. 5. German dialectal baustern, to swell, akin to the source of Middle English bost, a bragging: BoasT!. III. Root form *beu-. 1. Latin bulla, bubble, round object, amulet (> Old French boule and Spanish bola, ball): BILL!, BILLET!, BOLA, BOULE?, BOWL’, (BULL?2), BULLA, BULLATE, BULLET, (BULLETIN); BOULE- VERSEMENT. 2. Latin bullire (> French bouiller), to bubble, boil: BOIL!, BOUILLON, BUDGE!, (BULLION), BULLY?; BOUILLABAISSE, EBULLIENCE, GARBOIL, PAR- BOIL. 3. Possibly Latin bucca (> Old French boucle, buckle, curl, and Spanish boca, mouth), (inflated) cheek: BOCACCIO, BOUCLE, BUCCAL, BUCKLE!, BUCKLE?; DE- BOUCH, DISEMBOGUE, EMBOUCHURE. 4. Greek boubén, groin, swollen gland: BUBO. [Pok. 2. beu- 98.] beu-2. Root imitative of muffled sounds. 1. Latin bitié (perhaps > Old French butor), bittern: BITTERN!. 2. Latin bited, a kind of hawk: BUZZARD. [Pok. 1. b(e)u- 97.] bha-'. To shine. Contracted from *bhas-. 1. Germanic *baukna-, beacon, signal, in: a. Old English béac(e)n, beacon: BEACON; b. Old English denominative bécnan, biecnan, to make a sign, beckon: BECKON. 2. Perhaps Germanic *bazja-, berry (< “bright-colored fruit”), in Old English berie, berige, berry: BERRY. 3. Germanic *bandwa-, “identifying sign,” banner, standard, sash, also “company united under a (particular) banner,” in: a. Spanish banda, sash: BANDOLEER; b. Late Latin ban- dum, banner, standard: BANNER, (BANNERET). 4. Suf- fixed form *bhaw-es- in Greek phds (stem phét-), light: PHOS-, PHOT, PHOTO-; PHOSPHORUS. 5. Extended and suffixed form *bhan-yo- in Greek phainein, “to bring to light,” cause to appear, show, and phainesthai (passive), “to be brought to light,” appear: FANTASY, (PANT), PHANTASM, (PHANTOM), PHASE, PHENO-, PHENOMENON; DIAPHANOUS, EMPHASIS, EPIPHANY, HIEROPHANT, PHAN- EROGAM, (PHANTASMAGORIA), PHOSPHENE, SYCOPHANT, THEOPHANY, (TIFFANY). [Pok. 1 bha@- 104.] bha-2. To speak. Contracted from *bhaa-. 1. Latin fari, to speak: FATE; AFFABLE, (FANTOCCINI), INEFFABLE, IN- FANT, (INFANTRY), PREFACE. 2. Greek phanai, to speak: -PHASIA; PROPHET. 3. Suffixed form in Germanic *ban- wan, *bannan, to speak publicly (used of particular kinds of proclamation in feudal or prefeudal custom; “to proclaim under penalty, summon to the levy, declare
652:kwelek-. Bundle. Proposed by some as the root of Latin culcita, mattress, sack, which is more likely of unknown origin: QUILT. [Pok. kuelak- 630.] kwelp-. To arch. 1. Germanic *hwalbjan in Old English *hwelfan, hwylfan, with parallel form *hwelman (> Middle English whelman), to turn over: WHELM. 2. Suf- fixed o-grade form *kwolp-o- in Greek kolpos, bosom, womb, vagina: GULF; COLPITIS, COLPOSCOPE, COLPOS- copy. [Pok. 2. kuelp- 630.] kwen-. Holy. Suffixed zero-grade form *kwn-s-lo- in Germanic *hunslam in Old English hisl, hiisel, Eucha- rist: HOUSEL. [Pok. kuen- 630.] kwent(h)-. To suffer. 1. Suffixed form *kventh-es- in Greek penthos, grief: NEPENTHE. 2. Zero-grade form *kenth- in: a. Greek pathos, suffering, passion, emotion, feelings: PATHETIC, PATHO-, PATHOS, -PATHY; PATHOGNO- MONIC, SYMPATHY; b. suffixed form *k“nth-sko- in Greek paskhein, to feel, suffer: PROTOPATHIC. [Pok. kventh- 641.] kwép-. To smoke, cook, move violently, be agitated emotionally. Hypothetical base of possibly related words. 1. Suffixed variant form *kup-yo- in Latin cupere, to desire: COVET, CUPID, CUPIDITY; CONCUPISCENCE. 2. Zero-grade form *kwap-, becoming *kwap- possibly in: a. Latin vapor, steam, vapor: VAPOR; EVAPORATE; b. Latin vapidus, that has emitted steam or lost its vapor, flat, poor: VAPID; c. Greek kapnos, smoke: ACAP- niA. [Pok. kuép- 596.] kver-1, To make. 1. Sanskrit karoti, he makes: SANSKRIT. 2. Suffixed form *kver-6r with dissimilated form *kel-6r in Greek pelér, monster (perhaps “that which does harm”): PELORIA. 3. Suffixed form *ker-as- in Greek teras, monster: TERATOCARCINOMA, TERATOGEN, TERA- TOID, TERATOMA. 4, Suffixed form *ker-mn in Sanskrit karma, act, deed: KARMA. [Pok. 1. kver- 641.] kwer-2. Something shaped like a dish or shell. Suffixed variant form *k”ar-yo- in Scottish Gaelic coire, cauldron, hollow, whirlpool: corrt&. [Pok. 2. kver- 642.] kwerp-. To turn oneself. 1. Germanic *hwarb- in Old English hwearf, wharf (< “place where people move about”): WHARF. 2. Germanic *hwerban in: a. Old Norse hverfa, to turn: VARVE; b. Old Norse *hvirfa, to whirl, perhaps assimilated to Danish hvirre, to whir, akin to the Scandinavian source of Middle English whirren, to whir: WHIR; C. Old Norse hAvirfla, to whirl: WHIRL; d. Old North French werble, a warbling: WARBLE!. 3. Possibly suffixed zero-grade form *kwrp-o- in Greek karpos, wrist: CARPAL, CARPUS. [Pok. kuerp- 631.] kwes-. To pant, wheeze. 1. Germanic *hwésjan in Old Norse huzsa, to hiss: WHEEZE. 2. Latin queri, to com- plain: QUARREL!, QUERULOUS. 3. Suffixed zero-grade form *kus-ti- in Greek kustis, bladder, bag (< “bellows”): cyst, cysTo-. [Pok. kues- 631.] kwé6t-. To shake. Zero-grade form *kwet-, becoming *kwat- in Latin quatere (past participle quassus, in composition -cussus), to shake, strike: CASCARA, KVETCH, SCUTCH, SQUASH?; CONCUSS, DISCUSS, PERCUSS, RESCUE, succussIoNn. [Pok. kuét- 632.] kvetwer-. Four. I. O-grade form *ketwor-. 1. Probably Germanic *fe(d)wor- in: a. Old English féower, four: Four; b. Old English féowertig, forty: FORTY; c. Old English féowerténe, fourteen: FOURTEEN. 2. Latin quat- tuor (> Italian quattro), four: CAHIER, CARNET, QUATRAIN; CATER-CORNERED, QUATTROCENTO. IT. Mul- tiplicatives *kveturs, kvetrus, and combining forms *kvetur-, *kvetru-. 1. Latin quater, four times: (CARIL- LON), QUATERNARY, QUATERNION, QUIRE’. 2. Latin gua- drus, four-sided thing, square: CADRE, QUADRATE, QUARREL?, QUARRY?; SQUAD, SQUARE, TROCAR. 3. Latin quadri-, four: QUADRI-. 4. Latin quadra, square: QUA- DRILLE!. 5, Latin quadrdns, a fourth part: QUADRANT. 6. Latin quadrdagintd, forty (-gintd, ten times; see dekm): QUARANTINE. 7. Variant form *ket(w)r- in: a. Greek tetra-, four: TETRA-; b. Greek tessares, tettares,
654:four (genitive tessardn): TESSERA; DIATESSARON. c. Greek tetras, group of four: TETRAD; d. zero-grade form *k¥t(w)r- in Greek tra-, four: TRAPEZIUM. III. Ordi- nal adjective *ketur-to-. 1. Germanic *fe(d)worthén- in: a. Old English féortha, féowertha, fourth: FOURTH; b. Middle Dutch veerdel, one-fourth: FIRKIN; c. Old English féorthing, féorthung, fourth part of a penny: FARTHING. 2. Latin qudrtus, fourth, quarter: QUA- DRILLE?, QUADROON, QUART, QUARTAN, QUARTER, quarto. [Pok. kvetuer- 642.]
1083:thresh, tread, wear out: TRITE, TRITURATE; ATTRITION, CONTRITE, DETRIMENT; b. Greek teréddn, a kind of biting worm: TEREDO. 2. Suffixed form *ter-et- in Latin teres (stem feret-), rounded, smooth: TERETE. 3. Suffixed form *ter-sko- in Germanic *therskan, *threskan, to thresh, tread, in: a. Old English therscan, to thresh: (THRASH), THRESH; b. Old English therscold, threscold, sill of a door (over which one treads; second element obscure): THRESHOLD. II. O-grade form *tor(a)-. 1. Greek toreus, a boring tool: TOREUTICS. 2. Suffixed form *tor(e)-mo-, hole, in Germanic *tharma in Old High German darm, gut: DERMA2. 3. Suffixed form *tor(g)-no- in Greek tornos, tool for drawing a circle, circle, lathe (> Latin tornus, lathe): TURN; (ATTORN), CONTOUR, (DE- TOUR), (RETURN). III. Zero-grade form *tr- in Germanic *thr- in Dutch drillen, to drill: DRILL’. IV. Variant form *tré-. 1.Germanic *thréw- in Old English thrdwan, to turn, twist: THROW. 2. Greek tréma, perforation: MONO- TREME, TREMATODE. 3. Suffixed form *tré-tu- in Ger- manic *thrédu-, twisted yarn, in Old English thréd, thread: THREAD. V. Extended form tri- (< “trig-). 1. Suf- fixed form *tri-dn-, probably in Latin tid, plow ox: SEPTENTRION. 2. Suffixed form *tri-dhlo- in Latin tribu- lum, a threshing sledge: TRIBULATION. VI. Various ex- tended forms. 1. Forms *tré-, *trau- in Greek trauma, hurt, wound: TRAUMA. 2. Form *tru- in Greek truma, trumé, hole: TRYMA. 3. Form *érib- in Greek tribein, to rub, thresh, pound, wear out (> ¢ripsis, a rubbing): DIATRIBE, TRIBOELECTRICITY, TRIBOLOGY, TRYPSIN. 4. Form *trdg- in Greek trégein, to gnaw: TROGON. 5. Form *¢rup- in Greek trupé, hole (> trupanon, auger): TREPAN!; TRYPANOSOME. 6. Form *trig- possibly in Old French truant, beggar: TRUANT. [Pok. 3. ter- 1071.] tera-2. To cross over, pass through, overcome. Variant *trd-, contracted from “traa-. I. Zero-grade form “*tr()-. 1. Germanic suffixed form *thur-ila- in Old English thyr(e)l, thyrel, a hole (< “a boring through”): THRILL; NOSTRIL. 2. Suffixed form *tra-kve in Germanic *thurh in Old English thurh, thuruh, through: THOROUGH, THROUGH. 3. Greek nek-tar, overcoming death ‘(see nek-'). 4, Zero-grade form *tre- and full-grade form *ter(a)- in Sanskrit tirati, tarati, he crosses over: AVATAR. Il. Variant form ‘*trd-. 1. Latin trans, across, over, be- yond, through (perhaps originally the present participle of a verb *trdre, to cross over): TRANS-, TRANSIENT, (TRANSOM). 2. Suffixed form *trd-yo- in Iranian thrdaya-, to protect, in Middle Persian srdyidhan, to protect, in Persian sardi, inn: CARAVANSARY. III. Extended form *tru-. 1. Suffixed form *tru-k- in Latin trux (stem truc-), savage, fierce, grim (< “overcoming,” “powerful,” “pene- trating”): TRUCULENT. 2. Suffixed nasalized form *tru-n-k-o- in Latin truncus, deprived of branches or limbs, mutilated, hence trunk (? < “overcome, maimed”): TRENCH, TRUNCATE, TRUNK. [Pok. 5. ter- 1075.] terkw-. To twist. Extension of tera-'. 1. Possible variant form *twjerk- in Germanic *thwerh-, twisted, oblique, in Old Norse thverr, transverse: THWART. 2. Suffixed (caus- ative) o-grade form *tork’-eyo- in Latin torquére, to twist: TORCH, TORMENT, TORQUE}, TORQUE?, TORSADE, TORT, TORTUOUS; CONTORT, DISTORT, EXTORT, NASTUR- TIUM, RETORT!, TORTICOLLIS. [Pok. terk- 1077.] terp-. To satisfy oneself. Greek terpein, to delight, cheer: TERPSICHORE. [Pok. terp- 1077.] ters-. To dry. 1. Suffixed zero-grade form *trs-t- in Germanic *thurs- in: a. suffixed form *thurs-tu- in Old English thurst, dryness, thirst: THIRST; b. Old Norse thorskr, cod (< “dried fish”), whence Norwegian torsk, tosk, cod, with dialectal variant tusk, cod, stockfish: cusk. 2. Suffixed form *ters-d- in Latin terra, “dry land,” earth (> French and Old French terre, earth, ground): TERRACE, (TERRAIN), TERRAN, TERRENE, TER- RESTRIAL, TERRIER, TERRITORY, TUREEN; FUMITORY, INTER, MEDITERRANEAN, PARTERRE, SUBTERRANEAN, TERRAQUEOUS, TERREPLEIN, TERRE-VERTE, TERRICO-
```


## [2026-10-15T02:48:02.167Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -o -i -E '.{200}QUARTZ.{60}' AHD_watkins1985.txt | head -3; grep -o -E '.{100}TARD(Y|ILY).{50}' AHD_watkins1985.txt | head"
}
```


### [2026-10-15T02:48:02.622Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-15T02:50:38.104Z] TOOL CALL #60: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-514.py <<'EOF'\nimport json\nW=\"https://en.wiktionary.org/wiki/\"\nIEC1472=\"Mann IEC.txt line 19496 s.v. 'turd- (variant of type turt- \\\"hard, strong\\\")', WP I, 747: 'Per. (ambig.) turd, adj. (stiff, coy', fr. *turt- or *turd-); Lydian (Sardic) in OPer. sparda-, Sfard-, \\\"stiff, hard, strong\\\"; cf. also Sardeis (literally: \\\"fortress\\\") ... Gk. cf. sardón ... sárdion, n. \\\"carnelian\\\" ... OCS tvrüdü \\\"firm, hard, strong\\\" ... (Variant in (?) Lat. tardus \\\"thick, sluggish\\\", fr. *trd- or *trsd-?)'; line 19500 turtos 'firm, hard, strong': 'Per. turd \\\"stiff\\\"; Kurd. turt \\\"hard, firm, brittle\\\"; Lat. fortis'.\"\nWLD747=\"Walde-Pokorny Bd. I p.747 (WLD_Bd1_pages.txt leaf 756): 'tu̯ardo- (? s. u.) \\\"Quarz\\\". Gr. σάρδιον \\\"eine häufige Quarzart (Sarder, Karneol)\\\", mhd. nhd. Quarz: Sommer IF. 31, 373f. Wenn sein weiterer Vergl. mit aksl. tvrьdъ \\\"fest\\\" zutrifft, wäre σαρδ- als *tu̯r̥d- damit ablautgleich' — explicitly queried by WP itself.\"\nPOK1100=\"Pokorny IEW 1100-1101 (POK_full.txt line ~87884) 'tu̯er-2 : tur-, tu̯erə- to grab, to enclose': 'Lithuanian tvir-tas, Latvian tvirts \\\"strong, tight, firm\\\" (*tur-to-). Old Church Slavic tvrьdъ, russ. tverdyj'; no separate root tu̯ardo-, no Persian, Old Persian, Latin tardus or Greek σάρδιον.\"\nentries=[]\n# ---------- entry 1\ne1=dict(entry=1,root=\"Tuardo, Turd, Turt\",verdict=\"disputed\",\nmodern_form=\"PIE *tu̯er(H)- 'to grasp, enclose' (Pokorny 1100) → Balto-Slavic *twirˀtás 'firm, hard' (Lith. tvirtas, OCS tvrьdъ); no PIE *tu̯ardo- 'quartz'\",\nnote=\"Nourai copies Mann's turd-/turt- 'hard, strong' entry (IEC 1472, citing WP I 747) and Walde-Pokorny's queried tu̯ardo- 'Quarz'. The kernel is real: Pokorny's tu̯er-2 'grab, enclose' has a zero-grade adjective *tu̯r̥-to-/*tu̯r̥-dʰo- giving Lith. tvirtas, OCS tvrьdъ 'firm, hard'. But tu̯ardo- 'quartz' rests on two items now explained otherwise: German Quarz is a medieval loan from West Slavic twardy 'hard' (so it is a Slavic, not an IE-level, form), and Greek σάρδιον 'carnelian' is named after Sardis. None of the four daughters drawn (Persian tord, OP Sparda, Lat. tardus, Gk. sard-) is accepted as a reflex of this root by modern sources.\",\nnote_fa=\"نورایی این ریشه را از مان (۱۴۷۲) و والده‌ـپوکورنی (۱: ۷۴۷) برگرفته است. هستهٔ آن درست است: پوکورنی ریشهٔ هندواروپایی آغازین *tu̯er- «گرفتن، در بر گرفتن» را آورده که صفت بالتی‌ـاسلاوی *twirtas «سفت، محکم» (لیتوانیایی tvirtas، اسلاوی کلیسایی tvrьdъ) از آن است. اما *tu̯ardo- «کوارتز» را خود والده‌ـپوکورنی با علامت پرسش آورده‌اند و امروز رد شده است: Quarz آلمانی وام‌واژه‌ای از اسلاوی غربی twardy «سخت» است و σάρδιον یونانی به نام شهر سارد نامیده شده. هیچ‌یک از چهار واژهٔ این نمودار در پژوهش امروزی بازماندهٔ این ریشه شمرده نمی‌شود.\",\nsources=[W+\"quartz\",W+\"Reconstruction:Proto-Slavic/tvьrdъ\",W+\"σάρδιον\"],\nref_check=[{\"ref\":\"WLD1:747\",\"status\":\"supports\",\"note\":WLD747+\" So the reference has the root as Nourai draws it, but only as a tentative equation (Quarz + σάρδιον).\"},\n {\"ref\":\"IEC:1472\",\"status\":\"supports\",\"note\":IEC1472}],\nconsulted=[{\"src\":\"POK\",\"where\":\"pp.1100-1101 tu̯er-2\",\"stance\":\"partial\",\"note\":POK1100},\n {\"src\":\"AHD\",\"where\":\"Watkins 1985\",\"stance\":\"silent\",\"note\":\"grep 'QUARTZ', 'TARDY', 'twer' in AHD_watkins1985.txt: no root tu̯ardo-/turd-; tardus not listed under terə-2.\"},\n {\"src\":\"KLN\",\"where\":\"1966 s.v. quartz\",\"stance\":\"contradicts\",\"note\":\"KLN_1966 line 31346: 'quartz ... G. Quarz, fr. kwardy, a Western Slav. dialectal equivalent of Pol. twardy, Czech and Slovak tvrdy, \\\"quartz\\\", prop. adjectives meaning \\\"hard\\\" ... rel. to OSlav. tvrudu, Lith. tvirtas' — i.e. Quarz is a Slavic loan, not an IE *tu̯ardo-.\"},\n {\"src\":\"IEC\",\"where\":\"p.1472 turd-, turtos\",\"stance\":\"supports\",\"note\":IEC1472}],\nnodes=[\ndict(id=1,lang=\"Persian\",words=\"tord\",verdict=\"unverified\",\nderivation=\"NP tord/turd ترد 'crisp, brittle, fragile' (Steingass, Hayyim; Mo'in: 'تر و تازه؛ هر چیزی که زود شکسته گردد') is real, but no Middle Persian or Old Iranian antecedent is recorded and none of the Iranian handbooks (Horn, Hübschmann, MacKenzie, Aryanpur) or Wiktionary gives an etymology. Mann alone sets it under turd-/turt- and himself labels it '(ambig.)'. Phonetically a PIE *tu̯r̥-to- would give Iranian *θwr̥ta- > MP *turd (cf. *θwam > tō 'you', -rt- > -rd- as in murd), so the equation is not impossible, but it is an unsupported guess; note also the semantic clash 'brittle' vs. Balto-Slavic 'firm, hard'.\",\nderivation_fa=\"«تُرد» در فارسی به معنی «شکننده، زودشکن، تازه» واژه‌ای واقعی است (معین، استاینگاس)، ولی صورت فارسی میانه یا ایرانی باستانِ آن در هیچ منبعی ثبت نشده و هرن، هوبشمان، مکنزی، آریان‌پور و ویکی‌واژه برایش ریشه‌ای نمی‌دهند. تنها مان آن را با تردید (ambig.) به *turt- «سفت» پیوند داده است. از نظر آوایی *tu̯r̥-to- می‌توانست به ایرانی *θwr̥ta- و فارسی میانهٔ *turd برسد، اما این فرضی بی‌پشتوانه است و معنای «شکننده» با «سفت و محکم» ناسازگار است. ادعای نورایی نه تأیید می‌شود و نه رد.\",\nsources=[W+\"ترد\",\"https://vajehyab.com/moein/ترد\"],\nref_check=[{\"ref\":\"IEC:1472\",\"status\":\"supports\",\"note\":IEC1472+\" — but Mann marks the Persian '(ambig.)'.\"},\n {\"ref\":\"MON:1066\",\"status\":\"partial\",\"note\":\"Mo'in via vajehyab.com/moein/ترد: '(تُ) (ص.) (عا.) تر و تازه؛ هر چیزی که زود شکسته گردد' — confirms word and sense, gives no etymology (marked colloquial).\"}],\nconsulted=[{\"src\":\"HRN\",\"where\":\"grep turd/turt\",\"stance\":\"silent\",\"note\":\"grep -E 'turd|turt' HRN.txt: no entry for turd 'brittle'.\"},\n {\"src\":\"HUB\",\"where\":\"grep turd\",\"stance\":\"silent\",\"note\":\"no entry in HUB.txt.\"},\n {\"src\":\"ARY\",\"where\":\"ARY_pages.txt / latin index\",\"stance\":\"silent\",\"note\":\"grep '^ترد' and 'TORD' — no headword; only 'TURD (KURDISH)' at [pdf page 348] under the unrelated ستور entry.\"},\n {\"src\":\"BQT\",\"where\":\"BQT_v1_pages.txt line 29436\",\"stance\":\"silent\",\"note\":\"Borhan has تردك 'wheat-weevil' and ترده 'deed of house', no tord 'brittle' with etymology.\"}]),\ndict(id=2,lang=\"Old Persian\",words=\"sparda, sfard\",verdict=\"disputed\",\nderivation=\"Old Persian Sparda- is a place-name: 'Sardis', the Lydian capital and the Achaemenid satrapy of Lydia (DB 1.15, DPe 12, etc.); Elamite iš-par-da, Akkadian sa-par-du, Lydian sfard-/sfar-, Greek Σάρδεις from *Swárd-. No source gives it a lexical meaning 'stiff, hard'; Mann's '\\\"stiff, hard, strong\\\"' and 'Sardeis (literally \\\"fortress\\\")' are his own speculation. The name is Lydian (Anatolian), not Iranian, and cannot descend from an IE *tu̯r̥d- by any known sound law (Lydian/Greek s- from *tw- is unparalleled).\",\nderivation_fa=\"Sparda- در پارسی باستان نام جای است: «سارد»، پایتخت لیدیه و ساتراپی هخامنشی آن (کتیبهٔ بیستون ۱. ۱۵ و جز آن)؛ ایلامی iš-par-da، اکدی sa-par-du، لیدیایی sfard، یونانی Sardeis. هیچ منبعی برای آن معنای «سفت و سخت» نمی‌آورد؛ این برداشت و نیز «دژ» معنی کردنِ سارد ساختهٔ مان است. نام لیدیایی (آناتولیایی) است نه ایرانی و با هیچ قاعدهٔ آوایی از *tu̯r̥d- برنمی‌آید. پژوهش امروزی ادعای نورایی را رد می‌کند.\",\nsources=[W+\"Σάρδεις\"],\nref_check=[{\"ref\":\"IEC:1472\",\"status\":\"supports\",\"note\":\"Mann IEC line 19496: 'Lydian (Sardic) in OPer. sparda-, Sfard-, \\\"stiff, hard, strong\\\"; cf. also Sardeis (literally: \\\"fortress\\\")' — Nourai copies exactly this.\"}],\nconsulted=[{\"src\":\"KNT\",\"where\":\"lexicon s.v. Sparda- (KNT_full.txt line 29269)\",\"stance\":\"contradicts\",\"note\":\"'Sparda- sb. \\\"Sardis\\\", a province of the Persian Empire: Elam. iš-par-da, Akk. sa-par-du, Gk. Σάρδεις; with *Sv-, seen in Lydian Sfard-' — only a toponym, no sense 'hard'.\"},\n {\"src\":\"BRT\",\"where\":\"col. ~1617 (BRT.txt line 26852)\",\"stance\":\"contradicts\",\"note\":\"'p. sparda- m. Name eines Lands' — a country name, no appellative meaning.\"}]),\ndict(id=3,lang=\"Latin\",words=\"tardus\",verdict=\"disputed\",\nderivation=\"Latin tardus 'slow, sluggish, late' (> tardy, retard) is real, but its etymology is uncertain: de Vaan (EDL 607) finds no secure cognate; Wiktionary tentatively reconstructs *tr̥h₂-d-o- from *terh₂- 'cross over', and an Etruscan source has also been suggested. Mann himself only offers it as a queried variant ('(?) Lat. tardus ... fr. *trd- or *trsd-?'). A derivation from *tu̯r̥d- is phonetically impossible for Latin (initial *tw- gives Latin t- only sporadically, while *-r̥- gives -or-, not -ar-), and the sense 'slow' does not match 'hard'.\",\nderivation_fa=\"tardus لاتینی «کند، دیر» (سرچشمهٔ tardy و retard) واژه‌ای واقعی است، ولی ریشه‌اش روشن نیست: دو وان (۶۰۷) هم‌ریشهٔ استواری برایش نمی‌یابد، ویکی‌واژه با احتیاط آن را از *terh₂- «گذشتن» می‌داند و برخی اصل اتروسکی پیشنهاد کرده‌اند. خود مان آن را با علامت پرسش آورده است. r هجایی در لاتین به -or- می‌رسد نه -ar-، و معنای «کند» با «سخت» نمی‌خواند. پیوند آن با این ریشه را پژوهش امروزی نمی‌پذیرد.\",\nsources=[W+\"tardus\"],\nref_check=[{\"ref\":\"IEC:1472\",\"status\":\"partial\",\"note\":\"Mann IEC line 19496: '(Variant in (?) Lat. tardus \\\"thick, sluggish\\\", fr. *trd- or *trsd-?)' — Mann himself queries it; Nourai drops the question mark.\"}],\nconsulted=[{\"src\":\"KLN\",\"where\":\"1966 s.v. tardy (line 38207)\",\"stance\":\"contradicts\",\"note\":\"'L. tardus, \\\"slow\\\", which is of uncertain origin.'\"},\n {\"src\":\"SKT\",\"where\":\"s.v. Tardy (SKT.txt line 19188)\",\"stance\":\"partial\",\"note\":\"'From L. tardus, slow ... Allied to tererf, to rub' (Skeat's old guess, *ter- 'rub'), not *tu̯ar-.\"},\n {\"src\":\"POK\",\"where\":\"pp.1100-1101\",\"stance\":\"silent\",\"note\":\"tardus not listed under tu̯er-2.\"}]),\ndict(id=4,lang=\"Greek\",words=\"sard\",verdict=\"disputed\",\nderivation=\"The Greek word is σάρδιον (λίθος) / σάρδιος 'carnelian, sard' (the book prints the English-style 'sard'); it is the diminutive/adjective of Σάρδεις 'Sardis', the stone being named after its place of trade (Wiktionary; Klein 'sardine... Gk. σάρδινος λίθος, lit. \\\"Sardian stone\\\"'). Latin sarda, sardius > OFr. sarde > English sard. Walde-Pokorny's comparison with Quarz and OCS tvrьdъ was explicitly hedged ('wenn ... zutrifft') and is abandoned now that Quarz is known to be a Slavic loan; Mann's gloss 'hard' is not the Greek meaning.\",\nderivation_fa=\"واژهٔ یونانی σάρδιον / sardios «عقیق سرخ، سارد» است (کتاب صورت انگلیسیِ sard را نوشته) و به نام شهر سارد (Sardeis) نامیده شده، چون این سنگ از آنجا می‌آمد؛ لاتین sarda / sardius، فرانسوی کهن sarde و انگلیسی sard از آن است. پیوند آن با Quarz و اسلاوی tvrьdъ را خود والده‌ـپوکورنی با شرط آورده بودند و امروز کنار گذاشته شده؛ معنای «سخت» هم معنای یونانیِ واژه نیست. ادعای نورایی رد می‌شود.\",\nsources=[W+\"σάρδιον\",W+\"Σάρδεις\"],\nref_check=[{\"ref\":\"IEC:1472\",\"status\":\"supports\",\"note\":\"Mann IEC line 19496: 'Gk. cf. sardón ... \\\"snare\\\"; sard-ónux, m. (\\\"hard-nail\\\" > \\\"sardonyx\\\"); sárdion, n. \\\"carnelian\\\"' — Nourai follows Mann.\"}],\nconsulted=[{\"src\":\"WLD\",\"where\":\"Bd. I p.747\",\"stance\":\"partial\",\"note\":WLD747},\n {\"src\":\"KLN\",\"where\":\"1966 s.v. sardine (line 33749)\",\"stance\":\"contradicts\",\"note\":\"'sardine, n., a precious stone. — Late L. lapis sardinus, fr. Gk. σάρδινος λίθος, lit. \\\"Sardian stone\\\". See sard.'\"},\n {\"src\":\"POK\",\"where\":\"grep σάρδ/sardi\",\"stance\":\"silent\",\"note\":\"Pokorny does not list σάρδιον under tu̯er-2 or elsewhere.\"}])\n])\nentries.append(e1)\n# ---------- entry 2\nSKT=\"Skeat SKT.txt line 20309 s.v. Turkey: 'From F. Turquie Turkey. — F. Turc, a Turk. — Tatar Turk, a Turk; orig. an adj. meaning \\\"brave\\\"'; turquoise: see Turkey.\"\nBQT=\"Borhan-e Qate' ed. Mo'in, BQT_v1_pages.txt lines ~29595-29624 (leaf 713 of vol. 1), s.v. ترک: text '... و بضم اول معروف است که نقیض تاجیک باشد ... و کنایه از مطلوب و معشوق و غلام باشد'; Mo'in's footnote: 'در ترکی بمعنی شجاع و دلیر و سخت (جغتایی ۲۱۳)؛ در چینی T'u-küe؛ در یونانی Tourkoi؛ نام ترک بعنوان قومی بدوی نخستین بار در قرن ششم میلادی دیده میشود ... غلامان و کنیزان ترک‌نژاد زیبا بودند. بدین مناسبت ترک بمعنی معشوق زیباروی بکار رفته است'.\"\nLKT=\"Lokotsch LKT.txt line 4733, no. 2114 'Tk. türk: N. pr. ... geht auf den Stamm tür, tör \\\"vorne, oben > hervorbringen\\\" Vámbéry ... bedeutet also \\\"Geschöpf, Mensch\\\" ... a) Ein Edelstein ... frz. turquoise ... engl. turquoise; er ist so benannt, weil die Europäer ihn zuerst durch die Türken erhielten. b) Der Truthahn heißt engl. turkey'.\"\nKLNT=\"Klein 1966 (KLN_1966.txt line 40485), s.v. Turk: 'ME., fr. MF. (= F.) Turc, fr. ML. Turcus, fr. MGk. Τοῦρκος, fr. Turkish-Pers. Turk. Cp. turkey, turquoise.' turkey: 'The name was applied orig. to the guinea fowl, imported from Africa through traders who dealt chiefly with the Near East (\\\"Turkey-merchants\\\")'.\"\ne2=dict(entry=2,root=\"Tu-kŭe\",verdict=\"disputed\",\nmodern_form=\"Old Turkic Türk / Türük (𐱅𐰇𐰼𐰜), Proto-Turkic *tür(ü)k; Chinese 突厥 Tūjué (MC *dʰuət-kʉɐt) is a transcription of it\",\nnote=\"The name of the Turks is Turkic: Orkhon inscriptions (8th c.) Türk/Türük. Chinese 突厥 (Wade-Giles T'u-chüeh, older T'u-küe) is a transcription of that name (Pelliot: of a Mongolic-type plural *Türküt; Pulleyblank: of Türk directly), not its source. The sense 'strong' is one of several old proposals (Mo'in after Chagatai: 'brave, strong'; Skeat: 'brave'; Vámbéry/Lokotsch: 'creature, man' from tür-/tör-); none is established. Nourai took the Chinese form from Mo'in's footnote and Partridge, but inverted its role.\",\nnote_fa=\"نام «ترک» خود ترکی است: در کتیبه‌های اورخون (سدهٔ هشتم میلادی) Türk / Türük و در ترکی آغازین *tür(ü)k. صورت چینی 突厥 (تو-کیوئه) آوانویسیِ همین نام ترکی است (به نظر پلیو از جمع *Türküt) و سرچشمهٔ آن نیست. معنای «نیرومند» تنها یکی از پیشنهادهای قدیم است (معین به نقل از فرهنگ جغتایی: «شجاع و دلیر و سخت»؛ وامبری: «آفریده، انسان») و هیچ‌یک قطعی نیست. نورایی صورت چینی را از حاشیهٔ معین گرفته اما آن را به‌اشتباه ریشه شمرده است؛ پس ادعای او پذیرفته نیست.\",\nsources=[W+\"突厥\",W+\"Türk\",W+\"Turk\"],\nref_check=[{\"ref\":\"PRT:743\",\"status\":\"not_checked\",\"note\":\"Partridge, Origins (1958) is lending-only on archive.org; no local text.\"},\n {\"ref\":\"SKT:578\",\"status\":\"partial\",\"note\":SKT+\" — Skeat has the Turkic origin and the 'brave' gloss but no Chinese form.\"}],\nconsulted=[{\"src\":\"LKT\",\"where\":\"no. 2114 türk\",\"stance\":\"contradicts\",\"note\":LKT+\" — Turkic origin, no Chinese source.\"},\n {\"src\":\"TTS\",\"where\":\"p.184 no. 197 tür, tör (TTS_vambery1878_uoft_djvu.txt line 10961)\",\"stance\":\"contradicts\",\"note\":\"Vámbéry: 'törük, türük ... = Geschöpf, Wesen, Aufgekommener (in diesem Worte dünkt mir das Etymon des Nomen proprium Türk = Türke zu liegen)' — a Turkic etymology.\"},\n {\"src\":\"BQT\",\"where\":\"vol.1 s.v. ترک (Mo'in footnote)\",\"stance\":\"partial\",\"note\":BQT}],\nnodes=[\ndict(id=1,lang=\"Persian\",words=\"tork\",verdict=\"disputed\",\nderivation=\"NP tork/turk ترک 'a Turk' is inherited from Middle Persian turk (Pahlavi twlk'), which was taken in the 6th century from the Turkic ethnonym Türk when the Göktürk khaganate bordered Sasanian Iran — not from Chinese. The poetic sense 'beloved, beautiful (cruel) youth' arose because Turkish slave-boys and girls were prized for their beauty (Mo'in; Wiktionary 'the beloved'); Sa'di's line quoted on the page illustrates the ethnic sense. Derivatives Torkman ترکمن (Turkic Türkmen; Kashgari's folk etymology 'Turk-like' is rejected by Mo'in), Torkiye ترکیه, Torkamanestân are later formations. Pihan's derivation from Arabic taraka 'to leave' (PHN 363, quoted in the chart's note) is a folk etymology with no support: the word is attested in Middle Persian and Old Turkic before Arabic contact.\",\nderivation_fa=\"«تُرک» در فارسی از فارسی میانهٔ turk (پهلوی twlk') است که در سدهٔ ششم میلادی، هنگام همسایگی خاقانات ترکان با ساسانیان، از نام قومی ترکی Türk گرفته شده است، نه از چینی. معنای شاعرانهٔ «معشوق زیباروی» از آنجاست که غلامان و کنیزان ترک‌نژاد به زیبایی شهره بودند (معین در حاشیهٔ برهان). «ترکمن» از ترکی Türkmen است و پیوندش با «ترک‌مانند» ریشه‌شناسی عامیانه است. نظر پیهان که ترک را از ریشهٔ عربی «ترک» (رها کردن) می‌داند نیز ریشه‌شناسی عامیانه و مردود است. واژه و معانی درست است، ولی سرچشمه‌اش ترکی است نه چینی.\",\nsources=[W+\"ترک\",W+\"Türk\"],\nref_check=[{\"ref\":\"BQT:487\",\"status\":\"partial\",\"note\":BQT+\" — supports the word, the sense 'beloved', and lists Chinese T'u-küe, but as a parallel rendering beside the Turkic meaning 'brave', not as the source.\"}],\nconsulted=[{\"src\":\"PHN\",\"where\":\"p.363 s.v. TURC (PHN.txt line 9905)\",\"stance\":\"contradicts\",\"note\":\"'TURC ... [tourk], pluriel [atrâk], dérivé du verbe arabe [tarak] quitter, abandonner, par exemple, le sol natal, les Turcs étant considérés comme nomades' — the folk etymology recorded in the chart's NOTE; rejected by all modern sources.\"},\n {\"src\":\"LKT\",\"where\":\"no. 2114\",\"stance\":\"contradicts\",\"note\":LKT},\n {\"src\":\"HRN\",\"where\":\"grep türk\",\"stance\":\"silent\",\"note\":\"Horn has no headword turk (only 'türk.' as language label).\"},\n {\"src\":\"MON\",\"where\":\"MON_part1.txt\",\"stance\":\"silent\",\"note\":\"local 2-vol abridgement OCR has only ترکیب/ترکیه lines; Mo'in's view is taken from his BQT footnote above.\"}]),\ndict(id=2,lang=\"Greek\",words=\"\",verdict=\"confirmed\",\nderivation=\"Pass-through node: Byzantine Greek Τοῦρκοι / Τοῦρκος, first in 6th-century historians (Menander Protector on the embassies of 568 to the Turkic khagan), from the Turkic (or Persian-mediated) name Türk/turk; Klein: 'MGk. Τοῦρκος, fr. Turkish-Pers. Turk'.\",\nderivation_fa=\"گرهٔ میانی: یونانی بیزانسی Tourkos / Tourkoi که نخستین بار در تاریخ‌نویسان سدهٔ ششم (مناندر، دربارهٔ سفارت‌های سال ۵۶۸ به دربار خاقان ترک) آمده و از نام ترکی Türk یا صورت فارسی آن گرفته شده است. درست است.\",\nsources=[W+\"Turk\"],\nref_check=[{\"ref\":\"none\",\"status\":\"not_checked\",\"note\":\"node carries no reference in the book.\"}],\nconsulted=[{\"src\":\"KLN\",\"where\":\"1966 s.v. Turk\",\"stance\":\"supports\",\"note\":KLNT},\n {\"src\":\"BQT\",\"where\":\"Mo'in footnote s.v. ترک\",\"stance\":\"supports\",\"note\":\"'در یونانی Tourkoi' listed among the forms.\"}]),\ndict(id=3,lang=\"Latin\",words=\"turcus\",verdict=\"confirmed\",\nderivation=\"Medieval Latin Turcus (pl. Turci), from Byzantine Greek Τοῦρκος; in common use from the Crusades (11th–12th c.) for the Seljuks; Turchia 'Turkey' is formed from it.\",\nderivation_fa=\"لاتین سده‌های میانه Turcus از یونانی بیزانسی Tourkos است و از روزگار جنگ‌های صلیبی برای سلجوقیان به کار رفت؛ Turchia «سرزمین ترکان» از آن ساخته شده. درست است.\",\nsources=[W+\"Turk\"],\nref_check=[{\"ref\":\"none\",\"status\":\"not_checked\",\"note\":\"node carries no reference in the book.\"}],\nconsulted=[{\"src\":\"KLN\",\"where\":\"1966 s.v. Turk, Turkey\",\"stance\":\"supports\",\"note\":\"'fr. ML. Turcus, fr. MGk. Τοῦρκος'; 'Turkey ... F. Turquie, fr. ML. Turchia, fr. Turcus'.\"},\n {\"src\":\"SKT\",\"where\":\"s.v. Turkey\",\"stance\":\"supports\",\"note\":SKT}]),\ndict(id=4,lang=\"French\",words=\"\",verdict=\"confirmed\",\nderivation=\"Pass-through node: Old/Middle French Turc 'Turk', Turquie 'Turkey' and turqueise (pierre turqueise) 'Turkish stone', adjective in -ois/-eise from Turc.\",\nderivation_fa=\"گرهٔ میانی: فرانسوی کهن و میانه Turc «ترک»، Turquie «ترکیه» و turquoise «سنگ ترکی» (با پسوند -ois از Turc). درست است.\",\nsources=[W+\"turquoise\",W+\"Turk\"],\nref_check=[{\"ref\":\"none\",\"status\":\"not_checked\",\"note\":\"node carries no reference in the book.\"}],\nconsulted=[{\"src\":\"KLN\",\"where\":\"1966 s.v. Turk\",\"stance\":\"supports\",\"note\":\"'ME., fr. MF. (= F.) Turc'.\"},\n {\"src\":\"LKT\",\"where\":\"no. 2114\",\"stance\":\"supports\",\"note\":\"'frz. turquoise ... er ist so benannt, weil die Europäer ihn zuerst durch die Türken erhielten'.\"}]),\ndict(id=5,lang=\"English\",words=\"Turk, Turkey, turkey, turquoise\",verdict=\"confirmed\",\nderivation=\"Turk: ME Turke < (M)F Turc < ML Turcus. Turkey (country): F Turquie < ML Turchia. turkey (bird, 16th c.): first the guinea fowl, brought to Europe by 'Turkey merchants' via the Ottoman Levant, then transferred to the American Meleagris. turquoise (14th c. turkeis, later re-borrowed): MF turquoise < OF pierre turqueise 'Turkish stone', because the Nishapur (Khorasan) stone reached Europe through Turkish lands. All four are confirmed; note the chain runs Turkic → Greek → Latin → French, not from Chinese.\",\nderivation_fa=\"Turk انگلیسی از فرانسوی Turc و لاتین Turcus است؛ Turkey (کشور) از Turquie فرانسوی؛ turkey (بوقلمون) نخست نام مرغ شاخدار (مرغ گینه) بود که بازرگانانِ «ترکیه» از راه قلمرو عثمانی به اروپا می‌آوردند و سپس به پرندهٔ آمریکایی داده شد؛ turquoise (فیروزه) از فرانسوی pierre turqueise «سنگ ترکی» است، چون فیروزهٔ نیشابور از راه سرزمین ترکان به اروپا می‌رسید. هر چهار درست است.\",\nsources=[W+\"Turk\",W+\"turkey\",W+\"turquoise\"],\nref_check=[{\"ref\":\"KLN:1665\",\"status\":\"supports\",\"note\":KLNT},\n {\"ref\":\"AHD:1382\",\"status\":\"not_checked\",\"note\":\"AHD 1975 dictionary body (not the IE-roots appendix); not available on disk or online.\"}],\nconsulted=[{\"src\":\"SKT\",\"where\":\"s.v. Turkey, Turquoise\",\"stance\":\"supports\",\"note\":SKT+\" 'Called a Turkey cock ... from the notion that it came from Turkey or from India'.\"},\n {\"src\":\"LKT\",\"where\":\"no. 2114\",\"stance\":\"supports\",\"note\":LKT}])\n])\nentries.append(e2)\n# ---------- entry 3\nIEC1455=\"Mann IEC.txt line 19287 (p.1455): 'tulupos, ā \\\"lump, ball, mass, crowd\\\" Per. turb (\\\"radish\\\"; LW in Tk. turp, id.); Gk. tolüpē, f. \\\"ball of thread\\\"; Alb. tulup ...; OCS tlüpa, R tolpà, Cz. tlupa \\\"crowd, gang\\\"' — exactly Nourai's chart.\"\ne3=dict(entry=3,root=\"Tulupos\",verdict=\"disputed\",\nmodern_form=\"no such PIE root in Pokorny, Walde-Pokorny or Watkins; Gk. τολύπη is Pre-Greek (Beekes); Slavic *tьlpa 'crowd' has a separate (possibly Germanic) origin\",\nnote=\"Tulupos is Mann's private reconstruction (IEC 1455) joining Greek τολύπη, Slavic tolpa 'crowd' and Persian torb 'radish'. It is absent from Pokorny, Walde-Pokorny and Watkins (grep). Beekes assigns τολύπη to the Pre-Greek (Anatolian) substrate, comparing Luwian taluppi 'clump of dough'. The Persian–Turkish radish word (torob/turp) has its own, disputed history (see nodes) and nothing ties it to a PIE 'lump' word.\",\nnote_fa=\"«تولوپوس» بازسازیِ ویژهٔ مان است (۱۴۵۵) که یونانی tolypē «گلولهٔ نخ»، اسلاوی tolpa «انبوه» و فارسی «ترب» را به هم پیوند می‌دهد. پوکورنی، والده‌ـپوکورنی و واتکینز چنین ریشه‌ای ندارند. بیکس واژهٔ یونانی را از زبان زیرین پیشایونانی (آناتولیایی) می‌داند و با لووی taluppi «چانهٔ خمیر» می‌سنجد. واژهٔ «ترب/turp» هم تاریخ جداگانه و بحث‌برانگیز خود را دارد. پس پژوهش امروزی این ریشه را نمی‌پذیرد.\",\nsources=[W+\"τολύπη\",W+\"ترب\",W+\"turp\"],\nref_check=[{\"ref\":\"IEC:1455\",\"status\":\"supports\",\"note\":IEC1455}],\nconsulted=[{\"src\":\"POK\",\"where\":\"grep tolyp/τολύπ/tolu\",\"stance\":\"silent\",\"note\":\"no lemma tulupos/tolupā in POK_full.txt; τολύπη not cited.\"},\n {\"src\":\"WLD\",\"where\":\"Bd. I–III grep\",\"stance\":\"silent\",\"note\":\"no hit for τολύπ/tolyp in WLD_Bd1/Bd2/band3 text.\"},\n {\"src\":\"AHD\",\"where\":\"Watkins 1985\",\"stance\":\"silent\",\"note\":\"no root of this shape.\"}],\nnodes=[\ndict(id=1,lang=\"Persian\",words=\"torob, torb\",verdict=\"disputed\",\nderivation=\"NP torob/torb ترب 'radish' (Raphanus sativus; Mo'in: 'annual plant with beet-like root, white or black, sharp taste'; Borhan: 'بضم اول معروف است ... عربان فجل خوانند') is real, with a variant torf. No Middle Persian form is attested and no Iranian etymology exists. Wiktionary derives it from Turkic (Ottoman طورپ turp, Proto-Turkic *turp), noting that Laufer, Doerfer and Clauson inversely suspected an Iranian loan into Turkic because the word is opaque within Turkic. Either way it is a regional Turkic–Persian word, and Mann's link to a PIE *tulupos 'lump' (with the impossible *-l- > -r- and loss of the second syllable) has no support.\",\nderivation_fa=\"«تُرُب/تُرب» در فارسی گیاهی است با ریشهٔ تند (معین؛ برهان: «بضم اول معروف است ... عربان فجل خوانند») و گونهٔ «ترف» هم دارد. صورت فارسی میانهٔ آن دیده نشده و ریشهٔ ایرانی ندارد. ویکی‌واژه آن را وام از ترکی (turp، ترکی آغازین *turp) می‌داند، هرچند لاوفر، دورفر و کلاوسن برعکس احتمال داده‌اند که ترکی آن را از ایرانی گرفته باشد. در هر حال پیوند آن با ریشهٔ هندواروپایی *tulupos «گلوله» (که خود ساختهٔ مان است) هیچ پشتوانه‌ای ندارد و رد می‌شود.\",\nsources=[W+\"ترب\",\"https://vajehyab.com/moein/ترب\"],\nref_check=[{\"ref\":\"IEC:1455\",\"status\":\"supports\",\"note\":IEC1455}],\nconsulted=[{\"src\":\"BQT\",\"where\":\"vol.1 s.v. ترب (BQT_v1_pages.txt lines ~29285-29300)\",\"stance\":\"partial\",\"note\":\"'ترب ... بفتح [اول] مکر و حیله ... و بضم اول معروف است ... عربان فجل خوانند' — word and sense, no IE etymology.\"},\n {\"src\":\"HRN\",\"where\":\"grep turb/turub\",\"stance\":\"silent\",\"note\":\"no entry in HRN.txt.\"},\n {\"src\":\"HUB\",\"where\":\"grep turb\",\"stance\":\"silent\",\"note\":\"no entry in HUB.txt.\"},\n {\"src\":\"ARY\",\"where\":\"ARY_pages.txt\",\"stance\":\"silent\",\"note\":\"no headword ترب in Aryanpur's IE-roots dictionary.\"}]),\ndict(id=2,lang=\"Greek\",words=\"tolupě\",verdict=\"disputed\",\nderivation=\"Greek τολύπη (tolúpē; the book prints 'tolupě', a diacritic slip for -ē) 'ball of wool/thread, clew' (Homer τολυπεύω 'wind off, accomplish') is real. Beekes (EDG) holds it is a Pre-Greek substrate word, comparing Luwian taluppi 'lump of dough' (Furnée) or Hittite tarupp- 'gather' (Melchert); no IE reconstruction is accepted, and Pokorny/Walde-Pokorny do not list it. So the word is right, but its descent from a PIE *tulupos is disputed.\",\nderivation_fa=\"یونانی tolypē «گلولهٔ پشم یا نخ» (کتاب tolupě چاپ کرده که لغزشی جزئی در نشانهٔ واکه است) واژه‌ای واقعی است. بیکس آن را از زبان زیرین پیشایونانی می‌داند و با لووی taluppi «چانهٔ خمیر» و هیتی tarupp- «گرد آوردن» می‌سنجد؛ پوکورنی ریشهٔ هندواروپایی برای آن نمی‌آورد. واژه درست است ولی وابستگی‌اش به *tulupos پذیرفته نیست.\",\nsources=[W+\"τολύπη\"],\nref_check=[{\"ref\":\"IEC:1455\",\"status\":\"supports\",\"note\":IEC1455}],\nconsulted=[{\"src\":\"POK\",\"where\":\"grep τολύπ\",\"stance\":\"silent\",\"note\":\"not in POK_full.txt (only an unrelated OCR hit at line 6932).\"},\n {\"src\":\"WLD\",\"where\":\"grep\",\"stance\":\"silent\",\"note\":\"no hit in Walde-Pokorny volumes.\"}]),\ndict(id=3,lang=\"Turkish\",words=\"turp\",verdict=\"disputed\",\nderivation=\"Turkish turp 'radish' (Ottoman طورپ) is real and pan-Turkic (Azerbaijani, Turkmen, Kyrgyz turp; cf. Hungarian torma 'horseradish', an old Turkic loan). Mann and Nourai make it a loan from Persian; Wiktionary and Starling treat it as inherited Proto-Turkic *turp, with Persian torob borrowed from Turkic, while Laufer/Doerfer/Clauson suspected the opposite. The direction is thus contested and the PIE link is unsupported.\",\nderivation_fa=\"«turp» ترکی (عثمانی طورپ) به معنی ترب در همهٔ زبان‌های ترکی هست (آذری، ترکمنی، قرقیزی) و مجاری torma «ترب کوهی» وام کهنی از آن است. مان و نورایی آن را وام از فارسی می‌دانند، اما ویکی‌واژه آن را از ترکی آغازین *turp و فارسی را وام از ترکی می‌شمارد؛ لاوفر و دورفر برعکس می‌اندیشیدند. پس جهت وام‌گیری مورد بحث است و پیوند با ریشهٔ هندواروپایی بی‌پایه است.\",\nsources=[W+\"turp\",W+\"ترب\"],\nref_check=[{\"ref\":\"IEC:1455\",\"status\":\"supports\",\"note\":\"Mann IEC line 19287: 'Per. turb (\\\"radish\\\"; LW in Tk. turp, id.)'.\"}],\nconsulted=[{\"src\":\"TTS\",\"where\":\"grep turp\",\"stance\":\"silent\",\"note\":\"no entry turp in Vámbéry (TTS_vambery1878_uoft_djvu.txt).\"},\n {\"src\":\"LKT\",\"where\":\"grep turp\",\"stance\":\"silent\",\"note\":\"no entry turp in Lokotsch.\"}])\n])\nentries.append(e3)\nout=dict(pdf_page=514,book_page=484,verified_by=\"claude-opus-5\",verified_on=\"2026-10-14\",entries=entries)\njson.dump(out,open('/home/sfmqrb/git/rishe-private/data/verification/page-514.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)\nEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-514.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-514.json >/dev/null && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 514"
}
```


### [2026-10-15T02:50:38.690Z] TOOL RESULT

```
nodes verified: 12/12
node verdicts: {'unverified': 1, 'disputed': 7, 'confirmed': 4}
root verdicts: {'disputed': 3}
ref checks: {'supports': 7, 'partial': 3, 'not_checked': 4}
books consulted: {'silent': 15, 'contradicts': 6, 'partial': 3, 'supports': 8} | by book: {'KLN': 5, 'LKT': 4, 'HRN': 3, 'BQT': 3, 'SKT': 3, 'POK': 3, 'HUB': 2, 'ARY': 2, 'WLD': 2, 'KNT': 1, 'BRT': 1, 'PHN': 1, 'MON': 1, 'TTS': 1}
```


## [2026-10-15T02:50:50.028Z] TOOL CALL #61: SubagentHandback

```json
{
 "message": "Page 514 (book page 484) is verified. I wrote /home/sfmqrb/git/rishe-private/data/verification/page-514.json, and `verify_check.py 514` reports 0 PROBLEM lines and 12/12 nodes verified.\n\n**Verdicts:** 3 roots, all disputed. Of the 12 nodes, 4 are confirmed, 7 disputed and 1 unverified.\n- The unverified node is Persian tord ترد \"brittle\". No Iranian source gives it an etymology, and Mann himself marks it \"(ambig.)\".\n- The 4 confirmed nodes are the Turk chain: Greek Τοῦρκος → Latin Turcus → French → English Turk, Turkey, turkey, turquoise.\n\n**Disputed:**\n- **Tuardo/Turd/Turt** (root): Walde-Pokorny I 747 already gives tu̯ardo- \"quartz\" with a question mark. German Quarz is a loan from West Slavic twardy \"hard\", and only Balto-Slavic *twirtas from PIE *tu̯er- holds up.\n- **Old Persian sparda, sfard**: this is just the place name Sardis (Kent, Bartholomae). The meaning \"hard\" comes from Mann alone.\n- **Latin tardus**: its origin is uncertain (de Vaan; Klein), and Mann himself queries it.\n- **Greek \"sard\"**: the Greek word is σάρδιον, named after Sardis.\n- **Chinese Tu-kŭe** (root): Chinese 突厥 transcribes the Turkic name Türk, so it is not the source. Nourai took the Chinese form from Mo'in's footnote in BQT.\n- **Persian tork**: it comes from Middle Persian turk, taken from Old Turkic, not from Chinese. Pihan's derivation from Arabic t-r-k \"to leave\" (the chart's NOTE) is a folk etymology.\n- **Tulupos** (root): this is Mann's own reconstruction and is not in Pokorny, Walde-Pokorny or Watkins.\n- **Persian torob/torb**: no IE etymology exists. Wiktionary derives it from Turkic *turp; Laufer, Doerfer and Clauson suggested the reverse direction.\n- **Greek τολύπη**: Beekes treats it as a Pre-Greek substrate word.\n- **Turkish turp**: the direction of borrowing is disputed. Mann's reading (from Persian) is opposed by Proto-Turkic *turp.\n\n**Transcription:** no nodes are flagged and there are no extraction errors; the JSON matches the printed page. The book itself has two small slips. It prints \"tolupě\" for tolúpē and gives the English form \"sard\" as the Greek word; both are noted in the derivations.\n\n**References I could not check:** PRT:743 (Partridge is lending-only) and AHD:1382 (a page in the main dictionary, not the roots appendix).\n\nEtymonline returned 403, so I relied on Klein, Skeat and Lokotsch on disk and on Wiktionary. All 17 web sources I used are archived with fetch_source.py."
}
```


### [2026-10-15T02:50:50.333Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
