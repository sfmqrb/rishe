# Verification process log — verify-page-417


## [2026-09-14T01:11:28.434Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 417 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-417.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-417.json. Write /home/sfmqrb/git/rishe/data/verification/page-417.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 417` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:11:29.481Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:11:30.255Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:11:30.294Z] TOOL RESULT

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


## [2026-09-14T01:11:30.820Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-417.txt"
}
```


### [2026-09-14T01:11:30.847Z] TOOL RESULT

```
1	=== PDF page 417 (book page 387) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Reg 1, Rěkto : move straight, right  (refs POK:854; KNT:206)
4	#1 (parent #0) [Avestan] refs=POK:854 | râsta : right ; erezu : straight (line) ; razma : lined up (for a fight) ; aiwi-reg : to straighten up ☞Ambhi
5	  #2 (parent #1) [Persian] refs=BQT:134,944,946; HRN:136 | râst «راست» : right, straight ; raj «رج» : line, row ; radeh «رده (رژه)» : a row of soldiers ; razm «رزم» : battle (with rows of soldiers) ; afrâštan «افراشتن ، افراختن (فرازیدن)» : to elevate
6	#3 (parent #0) [Old Persian] refs=KNT:171,206 | aršta : rectitude ; ardu : upright ; râsta : right, true
7	#4 (parent #0) [Sanskrit] refs=AHD:785 | maha-râjâ : great ruler ☞Meg
8	  #5 (parent #4) [Persian] refs=None | Mâhârâjeh «مهاراجه»
9	#6 (parent #0) [Germanic] refs=AHD | rehtaz : right ; rakô : rake
10	  #7 (parent #6) [English] refs=None | right, rich, rake
11	#8 (parent #0) [Latin] refs=AHD | regere : to guide ; regula : straight bar ; surgere : to surge
12	  #9 (parent #8) [French] refs=None | 
13	    #10 (parent #9) [Persian] refs=MON | âdres «آدرس» : address ; režîm «رژیم» : government, diet | extra: اسکورت ، ریل ، رگل
14	    #11 (parent #9) [English] refs=AHD | escort, address, regime, regular, rail, rule
15	  #12 (parent #8) [English] refs=AHD | direct, dress, correct, source
16	#13 (parent #0) [Latin] refs=AHD | rex : ruler, king
17	  #14 (parent #13) [Spanish] refs=AHD | real : royal coin
18	    #15 (parent #14) [Persian] refs=BQT:985 | rîyâl «ریال» : unit of money | NOTE: Currency after the Spanish domination of the Persian Gulf.
19	  #16 (parent #13) [French] refs=AHD | 
20	    #17 (parent #16) [Persian] refs=VOP:193 | royâl «رویال» : royal
21	    #18 (parent #16) [English] refs=AHD | royal
22	  #19 (parent #13) [English] refs=AHD | Rex
23	
```


## [2026-09-14T01:11:34.025Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-417.json",
 "description": "Read source JSON for page 417"
}
```


### [2026-09-14T01:11:34.064Z] TOOL RESULT

```
{
  "pdf_page": 417,
  "book_page": 387,
  "entries": [
    {
      "root": {
        "name": "Reg 1, Rěkto",
        "lang": "Indo-European",
        "refs": "POK:854; KNT:206",
        "gloss": "move straight, right"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:854",
          "words": [
            {"translit": "râsta", "gloss": "right", "script": null},
            {"translit": "erezu", "gloss": "straight (line)", "script": null},
            {"translit": "razma", "gloss": "lined up (for a fight)", "script": null},
            {"translit": "aiwi-reg", "gloss": "to straighten up", "script": null, "see": ["Ambhi"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:134,944,946; HRN:136",
          "words": [
            {"translit": "râst", "gloss": "right, straight", "script": "راست"},
            {"translit": "raj", "gloss": "line, row", "script": "رج"},
            {"translit": "radeh", "gloss": "a row of soldiers", "script": "رده (رژه)"},
            {"translit": "razm", "gloss": "battle (with rows of soldiers)", "script": "رزم"},
            {"translit": "afrâštan", "gloss": "to elevate", "script": "افراشتن ، افراختن (فرازیدن)"}
          ],
          "note": null,
          "quote": {"text": "کمان را ز بالای سر بر فراشت - به انگشت چون چرخ گردان بکاشت", "poet": "Asadî"}
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "KNT:171,206",
          "words": [
            {"translit": "aršta", "gloss": "rectitude", "script": null},
            {"translit": "ardu", "gloss": "upright", "script": null},
            {"translit": "râsta", "gloss": "right, true", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "AHD:785",
          "words": [
            {"translit": "maha-râjâ", "gloss": "great ruler", "script": null, "see": ["Meg"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": null,
          "words": [
            {"translit": "Mâhârâjeh", "gloss": null, "script": "مهاراجه"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "rehtaz", "gloss": "right", "script": null},
            {"translit": "rakô", "gloss": "rake", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "right, rich, rake", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "regere", "gloss": "to guide", "script": null},
            {"translit": "regula", "gloss": "straight bar", "script": null},
            {"translit": "surgere", "gloss": "to surge", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "French",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "âdres", "gloss": "address", "script": "آدرس"},
            {"translit": "režîm", "gloss": "government, diet", "script": "رژیم"}
          ],
          "script_extra": "اسکورت ، ریل ، رگل",
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 9,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "escort, address, regime, regular, rail, rule", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 8,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "direct, dress, correct, source", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "rex", "gloss": "ruler, king", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "Spanish",
          "refs": "AHD",
          "words": [
            {"translit": "real", "gloss": "royal coin", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "Persian",
          "refs": "BQT:985",
          "words": [
            {"translit": "rîyâl", "gloss": "unit of money", "script": "ریال"}
          ],
          "note": "Currency after the Spanish domination of the Persian Gulf.",
          "quote": null
        },
        {
          "id": 16,
          "parent": 13,
          "lang": "French",
          "refs": "AHD",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 16,
          "lang": "Persian",
          "refs": "VOP:193",
          "words": [
            {"translit": "royâl", "gloss": "royal", "script": "رویال"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 16,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "royal", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 19,
          "parent": 13,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "Rex", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-14T01:11:34.799Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T01:11:34.851Z] TOOL RESULT

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


## [2026-09-14T01:11:38.543Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KNT','BQT','HRN','MON','VOP','AHD','ARY']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:700])\n    print()\n\"",
 "description": "Check refs_online for keys"
}
```


### [2026-09-14T01:11:39.671Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archiv

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 

VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook. Decoys: ketabnak 132354 (Zomorrodian), Google Books RwdkAAAAMAAJ (Nahid Shahidi 1997, no view). Purchase second-hand only."}

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
```


## [2026-09-14T01:11:40.075Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"reĝ-\\|reg-.*gerade\\|1. reĝ-\" POK_full.txt | head -40",
 "description": "Grep Pokorny for reg root"
}
```


### [2026-09-14T01:11:40.147Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:11:43.824Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la POK_*.txt && grep -n \"854\" POK_full.txt | head -20",
 "description": "Inspect POK files"
}
```


### [2026-09-14T01:11:43.895Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb  981836 Sep  4 14:06 POK_01.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1137861 Sep  4 14:06 POK_02.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1170809 Sep  4 14:06 POK_03.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 3971883 Sep  4 14:06 POK_full.txt
20489:References: WP. I 791 f., 854, Trautmann 44 f. 
20877:WP. I 854 ff. 
20898:References: WP. I 854 f., WH. I 538 f., Schwyzer Gr. Gr. I 715. 
69530:Page(s): 854 
69548:Page(s): 854 
69712:Page(s): 854-857 
70998:Page(s): 854
```


## [2026-09-14T01:11:44.889Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==510 || NR==511' POK_02.txt | head -80",
 "description": "Print Pokorny leaf 510-511"
}
```


### [2026-09-14T01:11:46.140Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:11:48.109Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '69690,69790p' POK_full.txt",
 "description": "Print Pokorny page 854-857 entry"
}
```


### [2026-09-14T01:11:48.179Z] TOOL RESULT

```
English reccan {ior *recan aiter reccan ^ ausstrecken'; but preterit roiite). Old Saxon rokian. 
Old High German geruohhen^ care bear, carry, RiJcksicht nehmen'. Old High German 
ruoh, mo^^a'Achthaben, endeavor, Sorgfalt', Middle Low German rokexn. ds.. Middle 
High German ruochios. Old English /lece/eas (Modern High German ruchios, engl. 
reckiess) 'unbekijmmert, unworried ', Old Icelandic /i^Ar'sorgsam', die with gr. apnyu) ' 
help, stand by ', apnycbv, -ovoc;, apwyoc; ' helper ', apwyri 'help' sich engstens combine, 
merge; 

nasalized (compare das Lithuanian, also Old \v\6\c rnjati): Old English /'a/7c 'straight, 
stout, proud, bold'. Middle Low German rank^ slim, thin, weak' (*gereckt). Old Icelandic 
rakkr^ slim, erect, bold'; Old Saxon Old English rinc. Old Icelandic rekkr^xwavi; 

Lithuanian nasalized zem. rgzious, /i^z//s'sich reckon', ablaut, r^zaus, r^zytis{\'6. Jh. 
ranszies), r^zai. 'Reckon', Latvian rudzities's\c\r\ reckon'; russ. su-razina ^ goo6 order'; 

Tocharian A rak-, rak- 'hinbreiten, cover', B rak-6s., A rkai'cover'. 

References: WP. II 362 ff., WH. II 426 f., 432 f., 434 f., Wissmann Nom. Postverb. 106, 
Trautmann 244. 



Page(s): 854-857 



Root / lemma: reg-2, reR- {rek-7) 

Meaning: damp; rain 

Material: 1. reg-\ Latin /'/g^/'e'bewassern' (with /from e), alb. rrjeth, Aor. rroc/hal\o\N, 

quelle, tropfe'; Norwegian dial, rakem. " dampness, damp ', Old Icelandic rak/ ds., nisi. 

/•aAr" humid, wet'; 

2. rek- {rek-7) in: Gothic rignn. 'rain' {*rek-nd-), Crimean Gothic reghen. Old Icelandic 
regnu.. Old Saxon regan, reginrw.. Old Frisian rein. Old English reg(e)n, renm., Old High 
German regan, regin, regen. Middle High German regenm.; Old Icelandic r/gna'ra\n', Old 
High German reganon ds. etc.; Lithuanian (with West Indo Germanic A?) rok/a, rokt/" fine 
rain', roke " dust rain '. 

References: WP. II 365 f., WH. II 435. 
Page(s): 857 

Root / lemma: rehg^'os- {* ohrehg''ohs-) 

Meaning: darkness 

Note 

Root/ lemma: rehg^os-i^ ohrehg^ohs^'. darkness derived from an extended Root/ lemma: 

mehr-2\ to shimmer, shine {*mehr-\c^a > *mehr-b^a) (common Aryan Greek m- > zero) 

Grammatical information: n. 

Material: Old Indie rajanf- 'n'\ghV; gr. £p£pO(; " darkness of the underworld ' (s-suggestion); 

Armenian erek and erekoy 'even\ng'; also Adverb erek' yesterday '; 

Maybe alb. erret' dark ', erresire^ darkness ', erresoj^ darken ' 

Gothic riqis, -izisu. " darkness', nisi. r0kkr, -rs^ darkness, dawn, twilight'; here perhaps gr. 

6pcpv6(; "dark' ( *org"'sno-) and Tocharian A orkam ( *org"mo-) " darkness '; different above 

S. 334. 

References: WP. II 367, Benveniste Hirt-Festschrift 2, 236, Burrow BSOAS 12, 645 f. 

Page(s): 857 

Root / lemma: reb"^- 

Meaning: expr. root 

Material: Old Indie rebhat/" creak, rustle, mumble, murmur; cry'; Latvian ribet{a\so ribet) 

"din, drone, rumble, bawl, blaster'. 

References: WP. II 349; 

See also: probably to rei-3. 



Page(s): 860 



Root / lemma: reid!^- 

Meaning: to ride, go 

Note: 

Root/ lemma: reki!^-: "to ride, go' derived from zero grade of an extended Root/ lemma: 

er-3: or-. r-\ "to move' in -e/d^-formant.
```


## [2026-09-14T01:11:51.668Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '69590,69700p' POK_full.txt",
 "description": "Print Pokorny reg-1 entry start"
}
```


### [2026-09-14T01:11:51.746Z] TOOL RESULT

```
Avestan raz- {razayeiti, participle rasta-, gr. opsKToq, Latin rectus, Gothic rafhts, Avestan 
rast9m"\n gerader direction') " direct, aim, point, gerade richten, sort, order, arrange', 
razan-'order, statute ', rasnu-' justified, legitimate ' (compare gr. 6p£Yvu-|ji), probably also 
razura-n., razurat 'wood, forest', razare, razan- " command, alignment '; rasman-m. n. 
"Schlachtreihe' (: gr. opsypa, Latin regimen); 

Old Indie raj- (Nom. Sg. rat) "king' (= Latin rex. Old Irish rf, s. also Gothic reiks), rajan- 
ds., rajnro^ueeu, FiJrstin', rasp, rajati"\s king, herrscht, glares, gleams' (denominative), 
rajya-^ royal ' (= Latin regius, compare also Old High German rJhhl), rajya-, rajya-v\. 
"power, rule' (= Middle Irish rTge, compare also Gothic reiki), /'5s//7'"Herrscherin', rastra-n. 
"power, rule, empire', Avestan rastar- 'Lenker, ladder'; 

Maybe alb. adj. ri' young man', re' young female', a//?/" youth'. 

Armenian arcvisee above; doubtful thrak. PN DPnao^; 

gr. opsyu) (opsyvuiJi only in hom. participle 6p£Yvu(;) " to reach, stretch, stretch out; to 
reach out, hold out, hand, give; to stretch oneself out, stretch forth one's hand; to reach at 
or to a thing, grasp at; metaph. to reach after, grasp at, yearn for a thing; to help oneself to 
' (6p£kt6(; = Avestan rasta- eic), opiyvaopai "strecke myself, long, reiche' (6- is prefix), 
opyuia or opyuia, Ionian ep. opyuin " fathom', opoyuia ds. (probably from *6p£Yuia ass.); in 
compound cbpuy-, e.g. 5£KU)puY0(;; 6p£Ypa (= Avestan rasman-) "das Reckon the hands, 
the Fijfte (footstep); Darreichen'; about apnyu) see below beim Germanic; about apY6(; 
see above; 

venet. /?e/]f/5"Geburtsgottin (compare gr. OpGia), die die Kinder in die right Lage bringt' 
or "goddess the Erektion?'; 

Latin rego, -ere, rexT, rectum {e secondary lengthening) "gerade richten, steer, rule, 
reign' (= optyio, 6p£kt6c;), e/'/gc»"richte auf (= Irish eirgim ' surge') etc.; aboui pergo, 
porrigo, surge. Adv. cargo, ergo, ergas. WH. s. vv.), Ae^/io "direction, line; line, region', 
/'e^i//5"Richtholz, line; Richtschnur, lath' etc., regiiius'\N\t\r\ senkrechten Kettenfaden 
gewebt'; Oscan Regaturei 'Rectdr\'7 (from a verb *regare); Latin rogo, -are'{d\e Hand 
ausstrecken =) ersuchen, bid, beg, ask, inquire '; rogus'pyre, stake' (gr. sizil. poyog 



'Getreidescheune' is Latin loanword) probably actually "aufgerichteter shove ' (= Germanic 
*raka^\ rex, /-eg/s'king' (= Old Indie raj- etc.), reg/ha ' queen' (marr. regenfa/J Dal), regius 
" royal ' (= Old Indie rajya-); 

Latin riged, -ere^ to be stiff, be numb, stiffen; to be stiff, be rigid, stand on end, bristle, 
stand erect; stand out, to stand stiff, stand upright, rise ', rigidus^ stiff, hard, inflexible, rigid 
', rigor^ stiffness, inflexibility, rigidity, numbness, hardness, firmness, rigor, esp. for 
coldness; the coldness' (this specific meaning perhaps preferred through frTgus); whether 
for *regere&^e'c erigerel; 

Old Irish reg-, A/g-'austrecken, e.g. die hand', Perf. reraig {*re-rog-e) "direxif; *eks-reg- 
(: Latin erigd) e.g. in aZ-zie/ig" uplifts sich', e//ige"surrectio'; ablaut. Old Irish rog(a)id 
"strecktaus', mcymr. /'^o'gift', rhorgWe'; mcymr. oy-re'steht auf, dy-re/n^s\c\r\ erheben', 
rhein^ stiff, gereckt' (: Middle Irish r/'g/n ds.), acymr. ar-c/b-renou ^ sepu\t\' , mcymr. ar-gyu- 
/'e'//7'Begraben' {*are-com-reg(i)-no) etc.; Middle Irish re/? 'span' {*reg-no); Old Irish recht 
(/i/-stem), cymr. rhaith^ law ', bret. /le/z'order, law, right'; 

Maybe alb. mbret{mbe-ret) 'king' 

gall. Rectu-genus, Old Irish rh. Gen. /7^'king' (= Old Indie raj-, Latin /^a), cymr. /■/?/ "prince, 
lord', gall. Catu-rTx, PI. -/v^es actually "people of C, R/go-magus actuaWy "Konigsfeld' 
(acorn, ruy Middle Breton roe, nbret. roue'k\ng' probably French), Old Irish r/iga/n^ queen' 
{*regenT=) cymr. rh/a/n'queen. Dame'; Middle Irish rJgen. "Konigreich' {*regiom); Old Irish 
rfchedn. "Konigreich' {* regi-sedom); 

Gothic rafhts. Old Icelandic rettr. Old English riht. Old Saxon Old High German reht 
"right, straight' (= Avestan rasta- etc.), Gothic ga-rafhtjan. Old High German rihteneic. " 
direct, aim, point '; Old Icelandic rettr. Gen. rettar^das right, law, court' (= Celtic * rektu-; 
wgrm. through das n. of participle Old High German etc. /■e/7/"right' replaced); Gothic 
/'a/7/d/7"darreichen'; Kaus. Gothic uf-rakjan^\n die Hohe reckon, ausstrecken'. Old High 
German /'ecc/?©/? "ausstrecken, raise, uplift, reichen, cause, say, define'. Modern High 
German recken. Old Saxon rekkian^ieW, define'. Old English reccan {reahte) "ausstrecken, 
lead, define, reckon'. Old Icelandic rekja ^s\xecken, outspread, define, announce, declare ' 
(partly iterative VaA/a/? under Verdrangung from *regd, partly denominative); Old Icelandic 
/'aA77s"ausgestreckt become, zur Besinnung come'; 

Old English racui. " riverbed, run, flow', engl. /a/re "pathway, way, Geleise', Old English 
racian "run, lead, steer'. Old Icelandic rekja spor'd'\e spoor pursue ', Middle Low German 
rekei. {*raki) "row, order', raken^xnee\., reach'; Old English racui. " narration, account'. Old 



Saxon raka, Old High German /'a/7/75"Rechenschaft, thing', Old Icelandic rgkHoxw. PI. " 
origin, source, beginning; an ancestor, Ursache, ground'; Old Icelandic rakr, Frisian Middle 
Low German Aa/r'straight, right' (= Latin rogus); e-grade: Middle High German gerech 
"wohlgeordnef. Old Saxon rekon^ direct, aim, point, sort, order, arrange'. Middle Low 
German /le/re/? 'right, unhindered, often'. Old High German rehhanon^ sort, order, arrange, 
reckon, Rechenschaft ablegen'. Old English ge-recen/an ^ 6ei\ne' , engl. reckon^ therefore 
halten'; Old English recen^qu\ck, fast, willing, ready'; Old Icelandic /and-rek/^ king', Old 
High German anet-rehho " drake, male duck '; whether with the outlook the zum 
Zusammenscharren ausgereckten Hand die family of Gothic /7/ra/7 'anhaufen'. Middle High 
German /lec/?©/? 'zusammenscharren, anhaufen, gather, collect'. Old Icelandic raka. Middle 
Low German raken {*raken) '(together)scratch'. Old Icelandic reka. Old High German 
rehho^ rake, rake ', Old Saxon rekai. ' rake ', Old Saxon raka. Old English racu, Swedish 
rakai. ds., ©-grade: Norwegian dial, raaki. 'spoor, track, Streif, furrow, row', isl. raki. 
'Streif (compare Old Indie raji-, rajfsin^e, row') here belongs, is dubious; through 
borrowing from dem Celtic vor the Mediaverschiebung: Gothic Aez/rs 'ruler, vornehm, 
mighty' (Celtic rfg-s). Old Icelandic /'/^/''mighty'; Old High German rfhhi. Old Saxon rfki. Old 
English /Tce (Celtic *rTgio-) 'mighty, vornehm, rich'. Modern High German reich; Gothic 
reiki. Old High German z???/?/ "empire' (Celtic *rTgion); 

d-grade, with from 'uplift, set up, help' entwickelter meaning: Old Icelandic r0kja. Old 
English reccan {ior *recan aiter reccan ^ ausstrecken'; but preterit roiite). Old Saxon rokian. 
Old High German geruohhen^ care bear, carry, RiJcksicht nehmen'. Old High German 
ruoh, mo^^a'Achthaben, endeavor, Sorgfalt', Middle Low German rokexn. ds.. Middle 
High German ruochios. Old English /lece/eas (Modern High German ruchios, engl. 
reckiess) 'unbekijmmert, unworried ', Old Icelandic /i^Ar'sorgsam', die with gr. apnyu) ' 
help, stand by ', apnycbv, -ovoc;, apwyoc; ' helper ', apwyri 'help' sich engstens combine, 
merge; 

nasalized (compare das Lithuanian, also Old \v\6\c rnjati): Old English /'a/7c 'straight, 
stout, proud, bold'. Middle Low German rank^ slim, thin, weak' (*gereckt). Old Icelandic 
rakkr^ slim, erect, bold'; Old Saxon Old English rinc. Old Icelandic rekkr^xwavi;
```


## [2026-09-14T01:11:56.039Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '69560,69592p' POK_full.txt",
 "description": "Print Pokorny reg-1 header"
}
```


### [2026-09-14T01:11:56.098Z] TOOL RESULT

```
Alb. shq/pe ' eag\e' seems related to Old \n6\c rj7-pya ' darting along ' epithet of the bird 
syena- ("eagle, falcon'), [Rumanian soim "falcon'], Avestan arazi-fya- (cf. gr. ap^icpo(; asTOi; 
irapa FlEpaaK; H., aivinoijj), Armenian arcui{< *arci-wl) "eagle' which is evidently a form of 
the same word; that it is Macedonian confirms its reality. 

Alb., gr., Avestan, and Old Indie prove that from Root/ lemma: er-1, or- : "eagle' derived 
extended Root/ lemma: ar(e)-g-{arg-?), fgi-\ "glittering, white, fast' and its subsequent 
zero grade Root/ lemma: reg-1 \ "right, just, to make right; king'. 

Material: Old Indie „^ya//; nasalized //t/s//" stretches itself, it hurries (from horses)'; probably 
also irajyati {W\Vc\ unclear /■) " arranges, orders, enacts, decrees '; rjLi-, Avestan srezu-^ 
just, right ' (in addition arszus^ finger'. Gen. srezvo), Kompar. Superl. Old Indie rajlyas-, 
rjTyas- " straight ', rajistha-, Avestan razista- " the justest, justest '; 

Old Indie ^/yra- from horses = rju-gamin, rjrasva-, Avestan arazraspa- EN actually " 
whose steeds haste straight on; with fast horses ', next to which compound form *rji- in rji- 
pya-{2. part unclear) " soaring straight ahead ' (epithet of syena- " eagle, falcon '), Avestan 
arazi-fya- m. " eagle, name of a mountain or mountains ', by Hes. ap^icpoc; (i.e. ap^icpo(;) 
a£T6(;napa FIspaaK;, Armenian arciv{*arcivi) " eagle ' (beside it *rju-pya-, ap. *ardufya-\x\ 
npers. aluh "eagle', compare gr. aiYuni6(;, if transfigured by folk etymology after ai^ from 
*apYuni6(;); rji-svan- EN actually " with fast dogs ', compare in gr. dp^oq, (from *apY-pO(; 
diss.) " fast, quick ', above S. 64; 



Maybe zero grade in alb. (*p^i(po(;), ^icpo-, shqiponje^ea<^\e', alb. Geg Shqipni, alb. Tosc 
Shq/per/land of the eagles'. 

Old Indie raj/-'s\ch aufrichtend, straight', rajf- RV perhaps "line, row' (= Middle Low 
German reke under S. 856); rajas- (Avestan razah-) n. 'Raum'; 

Avestan raz- {razayeiti, participle rasta-, gr. opsKToq, Latin rectus, Gothic rafhts, Avestan 
rast9m"\n gerader direction') " direct, aim, point, gerade richten, sort, order, arrange',
```


## [2026-09-14T01:12:04.069Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"aršta\\|arsta\\|ardu\\|rāsta\\|rasta\" KNT.txt | head -40",
 "description": "Grep Kent for Old Persian forms"
}
```


### [2026-09-14T01:12:04.131Z] TOOL RESULT

```
335:III. Among the less known Old Iranian lan- guages the most important was Median, known only from glosses, place and personal names, and its developments m Middle Persian, apart from borrowings in OP, which are of considerable im- portance for the understanding of OP itself. Others were the language of the Carduchi, pre- sumably the linguistic ancestor of modern Kurd- ish; Parthian, the language of a great empire which contended against Rome in the time just before and after the beginning of the Christian era; Sogdian in the northeast, the ancestor of the medieval Sogdian; Scythian, the language or languages of the various tribes known in OP аз Saká, located to the east of the Caspian and north of Parthia and Sogdiana, but also to the west of the Caspian on the steppes north of the Euxine Sea.
351:VI. The Kurdish dialects, apparently derived from the ancient Carduchian; now spoken by various tribes in western Persia and in the neighboring parts of the Turkish Republic.
559:arstam = Mam by etymology, see Lex. s.v.
584:By the Elam. writings: Атта (or Araza), Arbairé-, Armina, Asagaria, Paréava, Fravartis (also РЫ. fravartikdn), Margu&, Marduniya, -vard- in Ar- tavardiya, Vidafarna (also Av. хатто), Vidarna, Sparda, haumavargd: many of these confirmed also by Greek forms, ete.
595:frastam in u-frasiam u-frastam, pte. to root seen in Lt. precor, keeping strong-grade vowel.
921:*su- ‘good, well’, OP u-frastam, Skt. su-, Gk. b-yens ‘healthy’.
1207:ійѕра-, see Lex. s.v. pIE *prek-to-, OP *u-frasta- ‘well punished’; for
1211:' u-frasta-, varying with "u-frasta-, see above.
1212:pIE *réj-to- ОР rasta- ‘straight, mght’, Av. rasta- ‘directed’, Lt. réctus ‘directed, ruled, straight’.
1335:šc; so also OP avasciy from earlier *avad-cid, OP aniyasciy from earlier *angad-cid. $106. PIE у remained unchanged in most IE languages, down into the recorded forms of the languages; exceptional combinations in which it suffered change in OP, are mentioned below. pIE *réto- ‘directed’, OP rästa- ‘straight’, Av. rasta- ‘upright’, Lt. тёсіо-. pIE *pro, ОР fra- (in cpds.), Av. fra, Skt. pra, Gk. тро. |
1534:*prek- in ufrastam ‘well punished’, *prk- in aparsam ‘I punished’.
1636:(3) plr. change of p tk to f 0 x before con- sonants ($74.D): рага but fra-, aparsam but -frastam, tuvam but ace. ийт, akariya but cazriyü, drauga adurujiya but duructam.
1793:IV. Other formations, ineluding some personal names: agr-iya- to agra- (5148.1), батшап-їуа-, daran-ija-, brazman-iya-, mart-iya- to marta-, haš- iya- to hat- (8240), ha-mic-iya- to mitra-; Artavard- iya-, Ka"büj-iya-, Bard-iya-, M ardun-tya-.
1811:П. Secondary -па-, forming adjectives: para- na-, perhaps here kam-na; as mase. sb., drauja- па-, as nt. abstract pariy-ana-; forming hypo- coristic personal name, Aci-na-; perhaps Mardu- na- in Mardun-tya-; forming place names, with lengthening of preceding vowel, Varkàna- to varka-, Ha"-gmalàna- to ha?-gmala-; with -na- of uncertain origin, h*zdna- (see Lex. s.v.).
1838:I. Stems in -й-: adj. par-u-, ard-u- in personal name Ardu-mants-, va-u- in personal names Déraya-vau- Vau-misa- Vahau-ka-; substantives baru- in Gau-barw-a-, maršiy-u- ‘death’ in adj. uvd-marSiyu-, mard-u- in Marduniya-, Mag-u-, Hitd-u-, Marg-u-, Kür-u-, uncertain bat-u- in bátu- gara-; loanwords pir-u-, Ufrat-u-; restored loan- word agur-u-; uncertain as to stem, Qatag-u-, sikabr-u-.
1941:b. Names of other Persians: Artavardiya-, Ardumants-, Aspacanah- (M), Ulana-, Өилта-, Dàtwahya-, Dédar&i-, Bagübigna-, BagaburSa-, Marduniya-, Vaumisa- (with -s- which is not Per- sian nor Median), Vayaspara-, Vahauka-, Vahyaz- dáta-, Vidafarnah- (M), Vidarna-, Vivina-, Hazà- manis-.
1956:IV. Still other names are appellatives indicat- ing the qualities of the persons, like the redupli- cated Dé-dar- ‘Bold’. Possibly *U-vazstra-, Vi- darna-, Vi-vàna- (given under П) also belong here. Or names may denote occupations, as per- haps in the adjectival derivative, possibly pa- tronymie, Mardun-iya- ‘Vintner’s son’.
2075:айа DB 1.28, XPh 49, 52, when used with pari-ay- ‘respect’, is probably inst. rather than abl., because of the lack of prep. Ласа; note that the text of DSe 37-9, as now restored, gives no support for the abl. in the other passages, despite my remarks JAOS 54.46, Lg. 13.308, JAOS 58.117. On inst. sg. karšā, loc. sg. karšayā, nt. асе. casam, acc. pl. ufrasta-diy, see Lex. s.vv.
2634:but OP u-frašta- u-frasta- ‘well punished’ (where
2639:pIE *reg- ‘direct’: *ré§-to- with lengthening of the vowel (593.02), Latin réctus, Av. rasta-, OP rastam ‘straight, right’.
3479:22 bartam : abaram : hya : апка : аһа : avam : ufrastam : aparsam : vašnā : Auramazda 23 ha : ima : dahyáva : tyanà : manā : dita : apariyàya : yaðāšām : hacima : абаһ
3832:38 patipayauvi : martàya : hya : draujana : ahatiy : avam : ufrastam : pars : ya
3857:63 yàha : bagitha : tyaiy : hatiy : yaf : палу : апка : Sham : пау : draujana : арат : na 04 iy : zürakara : &ham : поту : adam : поталу : tauma : upariy pev omis ~ 65 yam : naiy : škaurim : naiy : tunuvatam : züra : akunavam : martiya : һуа : hamata 66 xšatā : manā : vityà : avam : ubartam : abaram : hya : viyanüfaya : avam : ufrasta 67 т: aparsam | : фу : Юйгауауац$ : xSayafiya : tuvam : К : xšāyaðiya :
3876:83 à : Vidafarnà : пато : V&yaspárahy& : puça : Parsa : Utàna : пата : Guxrahyá 84 : риса : Parsa : Gaubaruva : паша : Marduniyahyá : puça : Parsa : Vidarna : nama : Ва 85 gabignahya : puça : Parsa : Bagabux’a : пата : Dütuvahyahyà : риса : Pársa :
3889:Маг ат Foy KZ 35.45 (conj.), Jn., KT, for КІ в in- correct, abiStam. 9*5 Definitive жи е by Cameron, upariy | dlyalm [:] пабу : Sakaurim : naty : t[u]nuvatam, confirming uparty[üyam] of WB, HK, Wb. KIA; Sakaurim WB, Jn., fakauri[m] KT, Tm., Wb. KIA (read rather Skaurim, see Lex. s.v. skaudi-); [nay] Spiegel; ... uvata Rl., ]nuvatam Jn., t{ulnuvatam KT. ® zuku RL, züra Ri. later.  hya WB (from Rl.'s squeezes), Jn.; omitted by KT. #06... ВІ; 2076 WB, Jn; 090 KT. 6 piyaná[sa]ya WB, KT, HK, Tm., Wb. KIA; correctly viyana\balya Foy KZ 35.46. “avam : ufrasta- WB; wrongly ava : ufrasta- KT. ® [zu]rakara : ++ : KT, with possibly traces of two characters in the gap; but, Cameron finds [zuü]rakara : ahat- with only а gap for опе
3891:character, perhaps miswritten and erased, after the divider. * daustà WB, KT. 9 ...à KT; biylà WBn, НК, Tm. © atifraštādiy RL; aifrastádiy WB, Jn.; ufrastadvy KT.
4316:Notes то D§j: * [paruv}iyaba naiy ‘nicht in einem einzigen Anhieb�� Brd.; [пратш)|туаба naty ‘wie nie zuvor’ Hz. Api 103; [+++-+]:yaa@ тату ‘nicht planlos’ Hinz, ZDMG 95.240-1. € frasam ðadayāļtaiy}) Hz., аз in Da 5, q.v.; frasta Gadaya{maiy} Scheil, supported by Hinz, ZDMG 95.224.
4859:Gaubaruva son of Mardunitya ^ Gobryas Vidarna son of Bagübigna Hydarnes Bagabuxsa son of Détuvahya ^ Megabyzus Ardumamé son of Vahauka Aspathines
5072:against Gaumata: АКК. a-ar-di-ma-ni-i$. From ardu- ‘upright’, GAv. arazu-, Skt. rjú- + manis-, see manah- ‘mind’ (§34, $68.11, §124.4, §156.IV, $61.IIa, 8185.11): ‘Upright-minded’ (hardly Ardimanis- ‘dessen manah- glühend ist’, as taken by Nyberg, Rel. 352).  Ar[duma]|n[is] nsm. DB 4.86.
5082:arstà- sb. ‘rectitude’ ($80; $93): haplologie for *aršta-tā- (8129), abstract to arSta- ‘upright’ (8145), pIE *rĝ-ta-, with zero-grade to root *rej- (8122; Mt. Gr. $123, $125), cf. Av. arštāt- ‘goddess of rectitude’, OP ardu- in Ardumani&-, rüsta-; or merely fem. *rĝ-iã- as abstract (Bv. Gr. $123, $125). атат asf. DB (4.64.
5158:^u- insep. prefix ‘good, well’ (uv- before vow- els): Av. hu-, Skt. su-, Gk. 0-уиѕ ‘having good life, healthy’, pIE *su- (§140.IV): in uxSnav-, ukàra-, ucüra-, Utüna-, ulava-, ubanwaniya-, ufrasta- ufrasta-, ubarta-, umartiya-, иғада-, uradana-, Uvaxstra-, &Uvürazmi-, warstika-, uvdsabdra-, waspa-, dinara-, uwkhamaranakara-.
5189:ufraSa- ufrasta- adj. ‘well punished": u- ‘well’ + pte. fraSta- or frasta- (893) ‘questioned, investi- gated? to root fraó-: pIE *su-prekto- (§33, 75, $242.II. — ufrasiam asm. DB 1.22, 4.66f; ufra&lam DB 438. ufrasa-diy apm. DB 4.69 (JAOS 35.351-2, ef. Bv. Gr. $845; not loc. ufrastë + prep. айту, as taken by ВШ. IF 12.110, A1W 60-1, Mt. Gr. $818).
5699:fral- vb. ‘ask, examine, investigate, punish’: Av. fras-, Skt. pra-, Lt. precor, pIE *prek-, with inchoative present, *prk-ske-, OP parsa-, Av. poro- saiti, NPers. pursdd, Skt. precháti, Lt. poscit. Cf. also ufrasta- ufrasta-. parsdémiy 1st sg. (830, $97, $130, $212, 5226.1) ОМ 19. aparsam Ist sg. imf. ($122, 5182.3, $212. $226.П) DB 1.22; 4.67, parsü 2d sg. imv. (8212, 5237.1) DB 4.38, 69. . frabiyaiš opt. pass. ($220, $228.П, $228.11) DNb 21 (not desid. fut. pass., as taken by Hz. Арі 167). pati- + parsa- ‘examine, read’ (on meaning, Bv. DSLP 31.2.71-2): patiparsühy 2d sg. subj. (§222.- II, $227.I) DB 442.  patiparsátiy subj. ($222.11) DB 4.48.
5709:fraša- adj. ‘excellent’ (‘tauglich’, König Burg- bau 48, Brd. АКМ 39.87): Av. frasa- ‘directed toward, useful’, formed on adv. fraša to frünk-, Skt. adv. praca to ртайс-, from pra- + añe- (Bthl. AiW 1006-7); the irregular -3- for -s- of Sy- may be a contamination of *frasa- and *frasya- (otherwise ВБ. IF 2,266-7; borrowed from Aves- tan aec. to Hz. ApI 162). Hz. ApI 156-65 (recant- ing derivation from fra- + záy- ‘shine’, ‘brilliant’, AMI 3.1-11) takes as deriv. of pra-, through an idiom of racing or fighting, as 'extra (certamen), hors (concours)’, and therefore "incomparable, su- preme’. Cf. also Hz. RHRel. 113.26; Bailey, BSOS 6.595-7; Kent, Lg. 15.169. — frasam nsn. DSa 5, DS] 6 (see frasta-, for reading). frasam asn. DNb 2; DSf 56, 56f; DSo 4^; DSs 1°.
5789:mard- vb. ‘crush’: Av. marad- ‘destroy’, Skt. mrd- ‘rub, crush’, Lt. mordet ‘bites’, pIE *merd- (Foy, KZ 35.48). See also Marduniya-.
5791:Marduniya- sb. 'Mardonius, father of Gobryas: Elam. mar-du-nu-ia, Gk. Марббио; per- haps deriv. to *marduna- ‘vintner’ (§144.IV, 8147. П, $153.1, $164.1V), ef. NPers mul ‘wine’, Skt. mydvikd- ‘grapevine’ (Bthl. AW 1151; otherwise Justi, INB 195), which possibly contains root mard- ‘crush (the grapes in the wine-making)’. Marduniyahya gsm. DB 4.84.
```


## [2026-09-14T01:12:14.935Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# map line number -> leaf\nleaf=0\nfor i,l in enumerate(lines,1):\n    if i in (5072,5082,5158,1212,2639,1838):\n        print(i, 'leaf', leaf)\n    leaf += l.count('\\f')\nEOF",
 "description": "Map Kent line numbers to leaves"
}
```


### [2026-09-14T01:12:16.115Z] TOOL RESULT

```
1212 leaf 48
1838 leaf 67
2639 leaf 95
5072 leaf 193
5082 leaf 194
5158 leaf 197
```


## [2026-09-14T01:12:16.465Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"rāsta-\\|rasta- adj\\|rāsta- adj\\|razm\\|rāst\" KNT.txt | sed -n '1,30p'",
 "description": "Grep Kent rasta lexicon entry"
}
```


### [2026-09-14T01:12:16.521Z] TOOL RESULT

```
596:brazmaniya, Elam. pir-ra-1s-man-ni-ta.
1040:brazmantya-; see Lex. s.vv.
1494:pIE gh: brazmaniya-, Uvárazmi-, игта-, züra-, zü- rakara-.
1498:It is to be noted that OP 2 remained unchanged before m, as in brazman-, though it became voice- less (and was further changed) before m, as in baránà. But the zm which was retained in GAv. became sm in ТАУ.
1792:Ш. Forming ethnics: Akaufac-iya- to * Akau- faka-; Aéur-iya- to Aéurd-; Armin-iya- to Ar- mina-; Asagart-iya- to Asagarta-; U(v)j-iya- to 0(0)ја-; Uvürazmiya-; Küfiya- to Küša-; Ga"dara-ya- (possibly error for -riya-) to Ga"dara-; Gatagu-iya- (error for -uviya- or -udaya- or -udiya- ?) to 8alagu-; Pulü-ya-; Bäbiruv-tya-; Mac-iya- to Maka-; Spard-iya- to Sparda-; Haxámanis- iya-; Harawati-ya-; Hi"du-ya (error for Hi"duv- iya- ?).
1793:IV. Other formations, ineluding some personal names: agr-iya- to agra- (5148.1), батшап-їуа-, daran-ija-, brazman-iya-, mart-iya- to marta-, haš- iya- to hat- (8240), ha-mic-iya- to mitra-; Artavard- iya-, Ka"büj-iya-, Bard-iya-, M ardun-tya-.
1834:II. Stems in -1-‚ some of which may have been transferred to -2- stem declension (5179.1): áp-i- (see Lex. з.у.); dual u&4-; fem. adj}. to stems in -vant-, as place names, Sikaya! -uval-i-, Hara*-uvat- i-; fem. pte. yau{de"tzm], to masc. -ani-; to stem in -lar-, Bax-ir-i-; *Uvärazm-ī-; adj., a0a7gain-i- in npf. -1ya, to masc. aa"gatna-.
1854:III. Stems in -man-: as-man-, lau-man-, nā- 4 man-, braz-man- in adj. brazman-tya-, yau-man- in. 4
1889:Place names: Uvddatcaya-, Uvürazmi-, Paifi- yauvada-. |
1981:Akaufaciya ‘Men of Akaufaka’; Unarazmiy and -miš ‘Chorasmia’; Gadára ‘Gandaritis’; 8ata- gu’ Sattagydia’; Рала ‘the Daae’; Maka or ethnic Maciya; Saka or fem. бака Scythia’ or Хака ‘the Scythians’; Sug(u)da ‘Sogdiana’; Haraiva ‘Aria’; Hidus Sind’.
2003:Province Ethnic Province Ethnic as Province Province Aturà Aturiya Arabiya x* Armina Arminiya Arminiya Asagarta Asagartiya 0 (v)ja X Ü (v)jiya Uvárazm-iy -iš Uvürazm'ya* Katpatuka x*
2132:Nom. Sg.: Uvárazmiy Uvārazmiš, Baztriš; Harau- valiá (Skt. sárasvati), Sikalyaluvatis; apis (in айт = dpif-&m), BU ‘earth’ (ideogram only).
2134:АЫ. Sg.: Harawatiyà, Baxtriya, Uvdrazmiyd.
2143:I. The -- stems and the -i- stems fell together in OP into one declensional paradigm, having nom. sg. -1&, acc. -tm, gen. -ais, abl. -cya* (= Skt. -уӣз), loc. -îy (= Skt. -yà-m), nom. pl. -iya*. The only survival of separate declensional forms is nom. Uvarazmiy, with original -7, replaced in later inscriptions by Uvdrazmis. There is the possibil- ity that when nom. -i of -i- stems took the ending -8, the length of the vowel remained to distin- guish the -i- stems from the -i- stems; and simi- larly the long vowel in асе. -im may have re- mained. The OP system of writing leaves this am- biguous. But 1 is more likely that the new ending -i§ and the old ending -im became 2 and -їт in imitation of the corresponding forms of -{- stems.
2238:1! Nom. hamiciya DB 2.93 is predicate to two singular masculine nouns, but is more probably plural than dual; ef. $259. ? The form karšā does not belong here, nor probably artá-cà brazmanty (if во normalized) nor tau- mani-Saty; on these words see the Lexicon s.vv. * On these forms, cf. Kent. Lg. 19.225;
3474:15 Qura : Arabaya : Mudraya : tyaiy : drayahya : Sparda : Yauna : Mada : Armina : Kat 16 patuka : Parfava : Zraka : Haraiva : Uvárazmiy : Bāxtriš : Suguda : Gadara : Sa
4075:17 àrazmiy : Gataguá : Harauvatis : Н
4103:Tux Inscriptions or NaAQS-1-RugTAM. DNa = Darius, Nags-1-RustaMm A. 1 baga : vazraka : Auramazda : һуа : im 2 ām :bümtm :adà : hya : avam : asm 9 апат :adà : һуа : martiyam :adà : h 4 ya : Siyatim :adā : martiyahyà 5 :hya : D&rayavaum :xšāyaðiyam : ak 6 unau$ : aivam : parüvnàm : xSdyaé 7 iyam :aivam : parüvnàm : framátà 8 ram : adam : DarayavauS : xsayatiya : va 9 zraka : xSàyafiya : xSdyafiyanim 10 : xSdyaiya : dahyünàm : vispazaná 11 nam : х$йуайуа :abyáyà : шт ` 12 уа :уалаКауй : diiraiapiyf: Vistas 13 pahyà : puça : Haximanisiya : Parsa : P 14 àrsahyà : риса : Ariya : Ariya : ei 15 с̧а :0atiy : Darayavaus : xsaya 16 fiya : vašnā : Auramazdaha : ima : 17 dahyáva : {уй : adam : agarbáyam : 18 apataram : haeà : Ратѕа : adamsàm : 19 patiyaxSayaiy : manā : bàjim : abara 20 ha : tyasàm : hacdma :afahya :ava : a 21 kunava : dàtam : tya : mani : avadis : 22 adaraiya : Mada : Uvja : Parfava : Harai 23 va : Bàxtri$ : Suguda : Üvürazm 24 i$ : Zraka : Harauvatis : Gatagus : Ga 25 dara : Hidug : Saki : haumavargà : Sa 26 kā : tigraxaudà : Bābiruš : A 27 Gura : Arabàya : Mudràya : Armina
4214:DSe = Darius, Susa Е. 1 baga : vazraka : Auramazdà : hya : ima 2 т: bimim : adadé ; һуа : avam : as 3 татат : adadà : hya : martiyam : ad 4 ada : hya : &iyàülim : adad& : mart 5 iyahyü : hya : Darayavaum : XŠm : ak 6 unauš : айбат : parūvnām : XSm : a 7 шат : parüvnüm : framálàram : a 8 dam : Darayavaus : XS : vazraka : XS : XSy 9 anim : XS : dahyünám : vispazanü 10 nam : XS : ahyaya : bümiyà : vaz 11 rakàyà : düraiy : apiy : Vistas 12 pahyà : puça : HazamaniSya : Рат 13 sa : Pārsahyā : рисо : Ariya : Ari 14 ya : ciga : 08tiy : Dàrayavaus : XS : 15 уа&па : Auramazdaha : imá : dahy 16 āva : {уй : adam : agarbayam : apaia 17 ram : hacd : Parsa : adamsdm : pat 18 iyaxíayaty : manā : bajim : abara : 19 tyasam : hacéma : afahya : ava : aku 20 nava : datam : tya : mand : avadis : a 21 dáraya : Майа: Uja : Parðava : Haraiva : 22 Baatris : Suguda : Uvarazmis 23 : Zrdka : Наташайх : Bataguš : Maci 24 уй : Gadàra : Hidus : Зака : haumava 25 rgà : Saká : tigrazaudà : Babir 26 u$ : Авита : Arabéya : Мийгаа : 27 Armina : Katpatuka : Sparda : Yaun 28 à : аву : drayahya : ula : уа 29 y : paradraya : Skudra : Putayà : 30 Kuxiyd : Karka ; 6àtiy : Рата 31 yavau& : XS : vasiy : tya : duskarta 32 m : Gha : ava : naibam : akunavam : da 33 hyáva : ayauda : aniya : aniyam : 34 aja : ava : adam : akunavam : vašnā 39 : Auramazdaha : уаба : aniya : a 36 шуат : пау : jatiy : cind : gà 37 fava : kaSciy : astiy : дат : 38 tya : maná : haeá : avana : tarsat 39 y : улда : hya : tauviyd : tyam :s 40 kauéim : naiy : jatiy : naiy : vi 41 mardatiy : байу : Dérayavaus :
4330:7 Üja : BabiruS : Авита : Arabya : Mudrüya : Sparda : 8 Yauna : Майа: Armina : Katpatuka : Parbava : Zraka : 9 Haraiva : Uvürazmi$ : Báxtri& : Suguda : Gadára : 10 8atagut : Harawvati$ : Hidus : Skudra : Yound : taka
4576:21 : Haraiva : Baxtn$ : Sugda : Uvarazmi
4596:41 iy : агійса : brazmaniya : uta : aniyas
4601:51 rtácá : brazmaniya : martiya : һуа : avan
4604:54 rtaca : brazmaniya : hauv : uta : iva :
4610:59 yàvam : aita : adam : Auramazdam : jadiy 60 àmiy : aitamaiy : Auramazda : dadàtuv Notes To XPh: " The h* of abaraha has become л by failure to engrave the prior angle. ? tye for уу = tyaty. ? The p? of upariy lacks the two small verticals in copy a. * The daivaddna- of copy a is daivadáva- in copy b; the engraver was misled by the v* ending the previous line (Hz. AMI 8.62). ® ydeiysis for yid'iysife = yadiyaiša. 4 For the normalization brazmaniya here and in 51 and 54, see Lex. s.v, 4° antya$c for «cnp = -ciy. 5 The me of -maiy lacks the small middle vertical in copy b. 6 The a of kā, in both copies, has the horizontal over а single vertical only. “ арага is perhaps an error for aparam, which elsewhere stands in this idiom. " Copy b ends midway in this line, with the left-hand part lacking; the engraver was accustomed to Aramaic writ- ing, which went from right to left, Hz. AMI 8.62. 50 pariyail = -iye = -tiy. % In the prior uid the space for the first character is left blank; probably the char- acter in the model copy was illegible to the engraver.
4719:8 iyam : Uvarazmiya 9 iyam : така
5060:arta- sb. ‘Law, Justice’, an archangel attend- ing Ahuramazda: pte. to ar- as sb., Av. aša- and arata-, Skt. rid- ‘cosmic order’, Lt. ortus -‘risen, originated’, pIE *rto- ($30, $66, 5242.1). See also Artaxsaca-, arlavan-, Artavardiya-. ^ arid-cà isn. (8252.1, Lg. 21.223-9) XPh 41, 50f, 531 (not with Hartmann, OLZ 40.145-60; nor with Nyberg, Rel. 367, 478; Bailey ap. Nyberg, Rel. 478; Henning, TPS 1944.108; hardly, with Sen 155, artäcã braz- maniy apn. ‘and the divine fulfillments’; nor with Pisani, Riv. Stud. Or. 19.85-8, as elliptic dual ‘Arta and Brazman’, the -cé connecting with the preceding Auramazdém, and Brazman being the OP for the Av. vohü man ‘Good Thought’).
5158:^u- insep. prefix ‘good, well’ (uv- before vow- els): Av. hu-, Skt. su-, Gk. 0-уиѕ ‘having good life, healthy’, pIE *su- (§140.IV): in uxSnav-, ukàra-, ucüra-, Utüna-, ulava-, ubanwaniya-, ufrasta- ufrasta-, ubarta-, umartiya-, иғада-, uradana-, Uvaxstra-, &Uvürazmi-, warstika-, uvdsabdra-, waspa-, dinara-, uwkhamaranakara-.
5189:ufraSa- ufrasta- adj. ‘well punished": u- ‘well’ + pte. fraSta- or frasta- (893) ‘questioned, investi- gated? to root fraó-: pIE *su-prekto- (§33, 75, $242.II. — ufrasiam asm. DB 1.22, 4.66f; ufra&lam DB 438. ufrasa-diy apm. DB 4.69 (JAOS 35.351-2, ef. Bv. Gr. $845; not loc. ufrastë + prep. айту, as taken by ВШ. IF 12.110, A1W 60-1, Mt. Gr. $818).
5212:Uvárazmi- sb. ‘Chorasmia’, a province of the Persian Empire: Elam. ma-ra-18-mi-18, Akk. þu- ma-ri-iz-ma-’, Gk. Xwpaspin, Av. asf. z'airizom. From u- ‘good’ + vāra- ‘0° (8126, 5148.111), + ami- (§95, $120, 5152.) to zam- ‘land’. See also Uvürazmiya-. Uvirazmiy nsf. (SI79.1; Lg. 19.223) DB 1.16, DPe 16f; Uvārazmiš DNa 231, DSe 22°, DSm 9°, XPh 21f. Uvārazmiyā арзї. DSf 39f.
```


## [2026-09-14T01:12:23.819Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==195' KNT.txt | head -5 && echo \"=====186===\" && awk 'BEGIN{RS=\"\\f\"} NR==187' KNT.txt | head -8",
 "description": "Check Kent leaf page headers"
}
```


### [2026-09-14T01:12:24.821Z] TOOL RESULT

```
пат. AsH 1, 5; DB 1.4f; DBa 6; DSf 13; XPf 19, 20; A’Pa 20 (as gen.; §313.1[). Aršämahyā gsm. DB 1.3, 5; DBa 4, 6.
arstà- sb. ‘rectitude’ ($80; $93): haplologie for *aršta-tā- (8129), abstract to arSta- ‘upright’ (8145), pIE *rĝ-ta-, with zero-grade to root *rej- (8122; Mt. Gr. $123, $125), cf. Av. arštāt- ‘goddess of rectitude’, OP ardu- in Ardumani&-, rüsta-; or merely fem. *rĝ-iã- as abstract (Bv. Gr. $123, $125). атат asf. DB (4.64.
172
аг$Е- sb. ‘spear’ (830): Av. arsti-, Skt. rstt-, pIE *rs-ti- ($152.IIT, $179.IIT), to root in Skt. drsatt rşáli ‘rush, push’. See also ár&tika-, arsti- bara-. ат] nsf. DNa 44.
Grshka- sb. 'spearman': from ar&- ‘spear’ with vriddhi (as in wárttika-, $126), + suffix -ka- ($146.10). ага пет. DNb 44.
=====186===
� asn. DPd 20; DNa 53; XPh 43, 59; XSc 4°. ata- таш DPd 22; DNa 54; XPh 60. aitä apf. XPh 30, 35.
Ainaira- sb. ‘Ainaira’, a Babylonian, father of Nidintu-Bel; Elam. ha-a-na-a-ra, АКК. a-ni-ri-’, Ainaliralhya gsm. DB 1.77f.
atva- adj. ‘one’ ($150; §204.1): Av. aéva- ‘one’, Gk. Hom. olos, Cypr. orros ‘alone’, pIE *ozyos. ашат, asm. DNa 6, 7; DSe 6°, 6f; DSf 4, 5; DE 8f, 10; XPa 4, 5; XPb 8f, 10; XPe 4, 5; XPd 6, 7; XPf 6, 7; XPh 5,6; XE 9, 10; XV 7, 8; A!Pa 6f°, 8°; A?He 5f, 6; А?Ра 6, 7.
aiš- vb. ‘hasten’, caus. azSaya- ‘send’: Av. aes-, caus. aéaya-, Skt. 15-, caus. esayatz (§117).
fra + aiš- caus. ‘send forth’: Av. fraei-, Skt. .
preg-. frdiSayam ist sg. imf. (§24, §72, 6181, §215) DB 1.82; 2.19, 30, 50, 72f, 82; 3.2, 18, 30, 84; 5.7. frütsaya imf. DB 3.55, 60, 71.
Auliyüra- sb. ‘Autiyara’, a district in Ar- menia: Elam. ha-u-ti-ja-ru-i§, АКК. ú-ti-ņa-a-ri. Auliyàra nsm. DB 2.58f.
Aura- (Le. A*ura-) sb. ‘Lord, God’: Av. ahura-, Skt. dsura- ‘demon’, pIE *esuro- (6148.1). Aurahya Mazdaha gsm. ({36.ГУЬ, $44) XPe 10. Аита ism. DPe 24 (otherwise Bv. BSLP 30.1.70-3, Gr. §179, 8889; ‘downward’, isn. of aura-, zero- grade of avara-, comparative of *ava-, cf. Ау. aora ‘down’). Elsewhere always in cpd. Auramazdah-.
```


## [2026-09-14T01:12:33.071Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 220 221 222; do echo \"=== leaf $n ===\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' KNT.txt | head -30; done",
 "description": "Print Kent leaves 220-222"
}
```


### [2026-09-14T01:12:34.256Z] TOOL RESULT

```
=== leaf 220 ===
‘I pierce (as with a spit)’, Gt. faran ‘to travel’. рамо[т- іаїу| nsn. past pte. pass. ($242.1) DNb 54 (dubious con]. of Kent, Lg. 15.167, 178-4).
ipara- adj. ‘later’, possibly in hyáparam (q.v.) : Av. para- ‘farther’, Skt. pára- ‘distant’, Gk. qépav ‘beyond’.
nara prep. with acc. ‘beyond’ (§32, $63.1): Av. pard ‘before’, Skt. purds ‘before’, Gk. таро ‘before’; DPe 15; DPh 5; DH 4, See also para- dayadàm, paradraya.
parü postpos. with acc. ‘along’, and verbal prefix ‘forth’ ($132.3): Av. ?pará ‘before’, Skt. purá ‘before, formerly’, Gk. rapá ‘alongside’: in avapard and with ay-, ar-, gam-, bar-.
parauvaty lsn. as sb. ‘in the east’: руи] "Ре 15, a misreading for pr? : d*r^ ye (uninseribed space between r* and y*) = para : dra ya; seeunder paradraya.
paradayadám sb. asf., perhaps ‘pleasant re- treat’ ($55.II, §148.1V): Аа 3. Possibly mis- written руат“ for p'rud*iljme = paridai- dam, Av. patridaéza- ‘Umwallung, Ummauerung' (Bthl. AiW 865), borrowed in Gk. тарабено ‘park’, cf. JAOS 51.229; or for p'r*d'id^am* = paradidam, from ?para ‘beyond’ + didá- ‘wall’ (q.v.), as ‘that which is beyond or behind the wall’ (ef. Scheil 21.93; Bv. BSLP 30.1.67 j'vadiy paradayadám ‘paradis de vie’).
paradraya phrasal adv. ‘across the sea’ ($44, $191.[V): рата ‘beyond’ + acc. draya ‘sea’. DNa 28f; DSe 29°; XPh 24. paradraiya (848) A?P 24 (Hz. ApI 142). As two words, para draya DPe 15 (Cameron, JNES 2.307-8).
parana- adj. ‘former’: deriv. ($147.11) of stem in OP ?para, para (cf. ВЕШ. AiW 854), Av. рагі, рагб, Skt. рига ‘formerly’ (hardly to be normal- ized parna-, with MB Gr. $267, to Gt. faírneis ‘old’). See also dumlaparanam. — paranam asn. as adv. ‘formerly’ DB 1.51, D'Sb 3.
pariy prep. and prefix ‘around, about’: Av. pairi, Skt. pári, Gk. тері, Lt. per ‘through’, pIE *peri ($64, §75.1, $113, §140.1). Prep. with aec. ‘about’ DB 1.54. Prefix-with ay-, bar-; ef. also pariyana-.
196 OLD PERSIAN
pariyana- sb. ‘superiority’: deriv. ($147.IT) of pariy, in meaning seen in Ау. pairi ‘vorne, über ... hin’, Skt. pári as prefix ‘much, excessively’, cf. Gk. meptoads ‘excessive’ (otherwise Hz. ApI 273, Sen 250). pariyanam nsn. DNb 52.
paru- adj. ‘much, many’: Av. pouru-, Skt. purú-, Gk. modts, Gt. filu, pIE *palu- (§63.1, $107). See also paruzana-. рати) nsm. ($114, $127, $140.I) DB 449; DSf 56 bis. pariindm gpm. DSi 4, 5; DE 9, 10; XPa 5 bis; XPb 9, 10; XPc 4f, 5; XPd 6f, 7f; XPf 6, 7; XPh 5, 6; XE 9f, 11; XV 7,8; А:Ра 7°, 8°; А°Нс 6 bis. parünàm gpf. DPe 4. parüenüm ($28.П) gpm. DNa 6, 7; DSe 6, 7; Азра 6, 7.
paruva- adj. ‘being before in time or place’ (§35.1[): Av. paurva-, Skt. pürva-, pIE *pruos (868, $150), ef. Gk. Ion. трохоѕ ‘early’. See also paruviyata, paruviyaüd. parwā npm. ‘former’ DB 4.51. parwam asn. as adv. ‘formerly’ DB 1.9; DBa 15f; DSe 43°, 47; XPh 36, 39; paruvam- ciy DB 1.63, 67, 69.
parwnyata, adv. with preceding hacd, ‘from long ago’: *paruviya- (ie. *parvya-, deriv. of paruva-), Av. paouruya-, Skt. pürvyd-, + adv. suffix -la^, Av. -£ó, Skt. -tas, Gk. -ros, Lt. -tus asin funditus, pIE *-los ($191.11). C£. also paruviyatà. DB 1.7, 8, 45; DBa 11, 12.
[paruv|iyafà adv. ‘at first attempt’: *paruviya- (see paruviyala) + adv. suffix -0à, Av. -fa, Skt. -ihà ($191.ID). DSj 3 (conj. of Brandenstein, WZKM 39.49-51; ef. note ad loc.).
paruzana- adj. ‘having many men, or many kinds of men’ (‘having men of all tongues’, Wb. ZfA 44.165, after the Akk.): paru- ‘many’ + zana- ‘man’ ($9.11, $88, $120, $161.ППа). paru- zanānām (5140.1) gpf. DE 15f; XE 15f; А!Ра 12°. poruvzandndm (523.1) XPb 15f; XPd 11. раги zandnam ($23.11, $44) XPa 8; XPe 7; XPf 11; XPh 9; XV 12.
Parga- sb. ‘Parga’, a mountain in Persia: Elam. par-rak-qa, NPers. Purg ($30). Parga лет. DB 3.44. |
partara- sb. ‘battle’ (as in Elam. and АКК. versions): extension of -r/n- s
=== leaf 221 ===
tem (530, $148.I, 6154.1), ef. Av. posana- ‘battle’, Skt. pfiana- ‘battle, army’, to root in Av. poral-onie ‘they fight’? (Bv. TPS 1945.69-4; not agency noun
‘fighter, foe’ as taken by Wb. KIA 90-1, Bv. Gr. $277; not paratara- ‘foe’, with Wackernagel, KZ 59.29-30, as compar. to [Skt.] pára- ‘distant’ = RV ‘enemy’). partaram asn. DNa 47.
Ратдата- (§29.n2, $31) adj. ‘Parthian’, also тазе, as sb. ‘Parthia’, a province of the Persian Empire: Elam. par-tu-ma, АКК. pa-ar-tu-á, Gk. IIapóià. Extension ($150) of stem seen with vriddhi in Pársa-, but with dialectal difference in the 0/s ($9. VT, 887).
(1) ‘Parthian’: Paréava nsm. DN iv; A?P 4. Par&avaibi$ ipm. DB 2.96. (2) ‘Parthia’: Paréava nsm. DB 1.16; 2.7, 92;
DPe 15; DNa 22; DSe 21°; DSm 8°; XPh 20.
Par8avai ism. DB 2.94° 96°; 3.5, 10. parna-, see duildparanam, parana-. ‘parsa- vb., see fraó-.
?parsa- sb. ‘court’, only in Hz. ApI 278; for his pa[r|saiy lsm. DNb 22, see under patiy.
Pársa- adj. ‘Persian’; also masc. as sb. ‘Persia’, a province of the Persian Empire: Elam. par-sin, АКК. pa-ar-su, Gk. Перо, Пероќа (§9. VI, $87, §126, 5143.11). See also Paréava-. `
(1) ‘Persian’: Pársa nsm. DB 1.49; 2.18, 19, 49; 3.18, 26, 31, 32, 56, 84; 4.16, 26, 83, 84 bis, 85 bis, 86; 5.8°; DPe 22; DNa 18, 46; DN i; DSe 12; DZe 7; XPh 12; A?P 1. Pérsam asm. DB 2.81; 8.2, 29f; DPe 21. Pàrsahyà gsm. DNa 13f, 43; DSe 13; XPh 12. Pérsé ism. DPe 8.
(2) ‘Persia’: Pársa пзш. AsH 3 (for loc., §52.1);
DB 1.14, 41; 2.7; DPd 6f; DSm 6°. Pársam asm. AsH 8f; DB 1.46; 3.33, 34; 49, 28; DZe 12. Pérsam-cé DB 1.66. Pürsá ism. XPa 14 (here ‘Persepolis’, acc. to Cameron, by letter; $166, 6166.1). Pürsà absm. РМа 18, 46f; DSe 17°; Юле 7f, 10; XPh 16. Parsa for lsm. AmH 2 (856.V, §314b; wrongly Hz. AMI 4.132-4, 8.17- 9, as instr. of extent); for пзш. AmH 5 ($53; not nsf. adj., as taken by Hz. AMI 820-1, 34). Pärsaiy lsm. DB 1.2, 34; 2.9; 3.23, 24, 28, 34, 52, 58, 71; DBa 2.
pasü prep. ‘after’, temporal with асе. and local with gen. (Bv. BSLP 33.2.153): Av. paséa, NPers. pds, Skt. paácá, isn. to stem in Lith. (dat.) adv. and prep. різки ‘behind, later, after’ (Foy, KZ 35.26); pIE *po as in Lt. po-lið, positus, Gk. &-vó, + *sg*é, inst. to root noun from *seq*- ‘fol- low’, Av... hacatte, Skt) Gdeate, Gk. trerai, Lt.
See nada lai baa a D Lo AMA tae io at OT IPE Ауаз a зз
~
LEXICON
sequitur (§105; Uhlenbeck, Etym. Wtb. d. altind. Spr., s.v. paced). The s in pasá is OP for Med. $c, Av. sé, from pAr. $c (Ву. Gr. §114; otherwise Mt. Gr. §114). Less probably pAr. *pas (Lith. pds ‘at, to’) from the same *po + adv. -s as in OP patiš, + -cà isn. of stems in -айс-, for -acã (from *-ncà) by influence of contracted forms like Skt. praca (*pra-acd) to ртайс- (*pra-atic-) ‘forward’, cf. similar analogical form in Skt. adv. nica ‘downward’ (for *ni-acd) to пуайс-. Hardly from *pas (as above) + -à after its opposite para ‘before’ (Bthl. AiW 879). Direct cognation with Lith. páskw: is eliminated by the second and third etymologies; with Av. pasta, Skt. paícá, by the third. pasã with gen. DB 3.32; with асе. XPf 31 and in pasdva (q.v.).
pasáva phrasal adv. (§191.IV) ‘after that, afterwards’: pasé + asn. ava (8181). DB 1.27, 30, 32, 33, 34°, 35f, 40, 43, 46, 54, 72, 731, 75, 79, 82, 83, 86, 91, 94; 2.1, 3, 4, 12, 16, 19, 21, 27, 31, 32, 47, 49°, 51, 52, 62, 64, 67, 71, 72, 81, 84f, 94; 3.1,4, 9, 12f, 15, 20, 25, 29, 33, 36f, 41, 50, 59, 70, 73,75, 81, 84, 86, 90f°; 4.5, 35, 91; 5.3, 6, 9, 10f, 13, 21°, 28, 25°, 29; DSe 48; DSf 25; DZe 10; XPh 36; XSe 3; XV 23; А:Ра 21°; Рр 4°. pasãva-šim DB 2.76, 90. pasdva-Saiy DB 2.88.  pasáva-dim DNa 33. pasdva-mary XPh 32.
pasti- sb. ‘foot-soldier’: Skt. pailt-, from pIE *ped- ‘foot’ (OP pad-) + suffix -t&- ($85, 5152.11; Wb. Grab 40, Hz. ApI 94-8). — pasti$ nsm. DNb 48, 45.
pilar- sb. ‘father’: Av. pilar-, NPers. pióür, Skt. pitd
=== leaf 222 ===
r-, Gk. rarnp, Lt. pater, Gt. fadar, pIE *poler- (863.11, 875.1, 576.1, $154.II); see also hamapilar-. pita пет. ($86.П, $124.5, $186.1T) DB 1.4 bis, 5 bis, 6; 2.93; DBa 5, 6, 6f, 7, 8; DSf 12, 58; XPa 15; ХРе 12; XPf 16, 17, 19, 23, 31, 33, 42; XPg 7; X8a 2; XV 18; А!Ра 20f; D?Sb 4°. pica gsm. ($78, $124.5, $186.If) XPa 20; ХРе 14; XPf 35, 38, 47.
Pirdva- sb. ‘Nile’ (§75.V, $124.II, §166.V]): Pirdva пзш. DZc 9, in naming phrase, anacolu- thic for abl. after Ласа; either ‘Ivory River’, as deriv. adj. to piru- ‘ivory’, or possibly plural ‘The Tusks’ (JAOS 51.209).
miru- sb. ‘ivory’ (§75.V, 5153.1): Elam. pi- ru-§, Akk. pilu-, with cognates (or borrowings) in Eastern Asiatic languages (Przyluski, BSLP
197
27.3.220-2; Scheil, Rev. d’Assyr. 24.120; Bv. BSLP 30.1.62; König, Burgbau 66; Hz. AMI 3.67-8).  piruf пет. DSf 48.
pi-, vb., see paid-.
pisa- sb. ‘raft’: perhaps originally ‘cut mate- rial’, from root pazd- (8143.1II). різ ism. or isn., with collective meaning (§255), DB 5.24.
pisa- or paisa-, vb. stem, see paið-.
Putéya- adj. ‘man of Put, Libyan’ (§75.V, $/6.V, §144.HI); pl., ‘Libya’, a province of the Persian Empire (Cameron, JN ES 2.308-9) : Elam. pu-á-ti-ja-ap, Akk. pu-u-ta (Lg. 18.299, 15.165). Pulüya пет. A?P 27. Putāyā npm. DNa 29f; DSe 29°; XPh 28,
puça- sb. ‘son’: Av. puéra-, Ars. РЬ. рим, N Pers. pus, Skt. pulrá-, Ose. puclo-, рї *putlo- ($64, §75.1,§78,§148.1II). pucansm. AmH 3; AsH 4; CMb 2°; DB 1.8, 28, 39, 53, 74, 78, 79; 2.9; 3.25, 79, 81; 4.9, 14, 28, 30, 83, 84° bis, 85 bis, 86; DBa 3; DBb 6; DBd 6; DBh 7; DBi 8f; DPa 5; DPb; DPe 5; DPh 2; DNa 18, 14; DSa 2; DSb 10; DSe; DSd 2; DSe 12, 13; DSf 7; DSg 2°; DSi 2°; DS} 2°; DSk 3; DSm 2°; DSy 3; DZb 5f; DZec 6; DE 20; DH 2; XPa 10; XPb 20; XPe 9; XPd 14; XPe 4; XPf 14; XPh 11, 12; XPj; XPk; Х5е 2; XE 20; XV 15; A!Pa 15f; АЧ bis; D'Sb 2°; Аба 1, 2 bis, 3 bis; Ab; A?Sc 0° bis; А4 2; A?Ha 2°, 8, 3°, 4, 4°; А?Не 10, 11, 12, 13f, 15; A3Pa 18, 14, 15, 16, 18, 19, 20; Wa 7; Wb 8; We 9; Wd 9; Sa 8°, pucä npm. XPf 28; as nsm. А?НЬ (853; with -a after парӣ, acc. to Brd. WZKM 39.92).
farnah- sb., see Vidafarnah-.
fra- prefix ‘before, forth’ (as prep., not found in OP): Av. fra, Skt. pra, Gk. тро, Lt. prü-fessus, Gt. fra-, pIE *pro ($33, $01, $75.II, $106, $132.3). Found with verbs а1$-, jan-, nay-, var-, má-, sá-, haj-; in nouns framdtar-, framānä-, Fravarti-; in phrasal adv. fraharavam; with suffixes and exten- sions, in fratama-, fratara-, fratara-, fravata, fraxa-.
fratama- adj. ‘foremost’: fra- + superl. suf- fix -lama-, Av. fratama-, Skt. -tama- (4190.11). fratama npm. DB 1.57; 2.77; 3.48f, 51, 74, 90°, 91.
fratara- ad). ‘prior, further’: fra- + comp. suf- fix -tara-, Av. fratara-, Skt. adv. pratardm, Gk. mpotepos (§106, 5190.11). " fratara ism. DNb 38 (Sen 249 needlessly takes as error» for frataram).
198
frataram asn. XPg 11; adv. ‘previously’ DB 3.26, A!Pa 21.
fratarta DB 3.26, incorrect reading for fra- taram (Cameron).
fral- vb. ‘ask, examine, investigate, punish’: Av. fras-, Skt. pra-, Lt. precor, pIE *prek-, with inchoative present, *prk-ske-, OP parsa-, Av. poro- saiti, NPers. pursdd, Skt. precháti, Lt. poscit. Cf. also ufrasta- ufrasta-. parsdémiy 1st sg. (830, $97, $130, $212, 5226.1) ОМ 19. aparsam Ist sg. imf. ($122, 5182.3, $212. $226.П) DB 1.22; 4.67, parsü 2d sg. imv. (8212, 5237.1) DB 4.38, 69. . frabiyaiš opt. pass. ($220, $228.П, $228.11) DNb 21 (not desid. fut. pass., as taken by Hz. Арі 167). pati- + parsa- ‘examine, read’ (on meaning, Bv. DSLP 31.2.71-2): patiparsühy 2d sg. subj. (§222.- II, $227.I) DB 442.  patiparsátiy subj. ($222.11) DB 4.48.
frafara- adj. ‘superior’: fra- + variant com- par. suffix -thara- seen in Av. fraéara- ($1491, 6190.11; Wb. ЖА 41.319; Bv. 33.2.150-1, 34.1.33-4, Hz. AMI 4.126-7, 8.3940, ApI 166-7), cf. superl. -thama- in Skt. prathamd- ‘first’. Cf. also uradara
```


## [2026-09-14T01:12:40.523Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=229 && NR<=233 {print \"=== leaf \" NR \" ===\"; print}' KNT.txt | grep -n \"rāsta\\|rasta\\|205\\|206\\|207\\|=== leaf\" | head -40",
 "description": "Locate rasta in Kent lexicon"
}
```


### [2026-09-14T01:12:41.693Z] TOOL RESULT

```
1:=== leaf 229 ===
32:=== leaf 230 ===
37:LEXICON | 205
56:=== leaf 231 ===
63:206
71:=== leaf 232 ===
```


## [2026-09-14T01:12:44.697Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==231' KNT.txt | sed -n '1,30p'",
 "description": "Print Kent leaf 231 (p.205-206)"
}
```


### [2026-09-14T01:12:46.196Z] TOOL RESULT

```
am. rak-qa-an, АКК. ra-ga-’, Gk. ‘Payys, now Rai near Teheran. kagä nsf. DB 2.71f. Ваду absf. DB 8.2.
гада- sb. ‘wagon’ (570.11, $148.11), see urata-.
Irad- vb. ‘leave’: Skt. rah-, pres. rahati 'sep- arates, leaves’, to pIE *regh-, Av. razah- 5isola- tion’, or to pIE *redh-, NPers. (through Ars. РЫ.) rähäð ‘he gets free from’; Fr. Müller, WZKM 11.208-4; Foy, KZ 37.564-5; Bthl. AiW 1505; MB Gr. $192.
ava- + rad- ‘leave, abandon’: avarada 2d sg. inj. (5213, $224, $227.11, $237) РМа 60.
?rad- vb. ‘direct’ Ау. raz-, Skt. rdj- ‘reign’, Lt. rego ‘I direct, rule’, pIE *reg-; in uradana-, тазіа-.
rādiy postpos. ($133) ‘on account of’, with gen.: NPers. тё, enel. postpos. as in &-rà ‘why’, also particle of various uses, often affixed to direct object for elarity; also OCS radi, postpos. with gen., “оп account of’; 10е, sgoof räd- (5188111), io root in Ski. radh- ‘effect; complete! (not to
206
"rad-, pIE *rej-, with Hz. ApI 280). DB 4.54; DNb 9, 10f; also in avahyarádiy, q.v.
ram- vb. ‘be at peace’, with prefix d, in Arüjyüramna-, q.v.
rasa- present stem of vb., see ar-.
rüsla- adj. ‘straight, right, true’, with nt. as Sb.; ріс. of ?^rad-: Av. réSta-, Turfan РЫ. тай ‘true’, Lt. réctus ‘straight’, pIE *rékto- (593, §93.- n1-2, $106, $122, 5126, $24211). Cf. arštā-. таӣз- iam asf. DNa 59. rdstam usn. DNb 11; asn. DNb 7.
‚ .. rlaryary, see vart-.
Labandna- (or Labnàna-) sb. ‘Lebanon’ (§6, §107), 2 mountain in Syria famous for its cedars. Labanéna nsm. DSf 31.
-vä encl. conj. ‘or’ (8133, $291.1
```


## [2026-09-14T01:12:57.528Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"rasman\\|rāšta\\|aiwi.raz\\|aiwi-raz\\|ǝrǝzu\\|ərəzu\\|erezu\" BRT.txt | head -40",
 "description": "Grep Bartholomae"
}
```


### [2026-09-14T01:12:57.590Z] TOOL RESULT

```
4923:unsTcs  schwachbetonten  'er'*':  fravasayB ..  yä  ahurahe  xiayatö  daiinam  ufayüÜt- ynnii  yai  aim  bavaiti  *alavaxmul  yai fi  bavainti  anäzaritä  Yt.  /J.63;  —  ä  dim paskät  anumar»zatim  aHila  . .  färfndtl'a  . . visp>m  ä  akmät  yat  aim  paiti.apayat.,'H\.. iV.38;  —  vispaeibyS  sastim  baraiti  älarS. . yaübyS  alm'''*  *ham.paeaili  ..  \.62.T,  — iim  Aaxa  Aase  baraiti  . .  ?  äat  yai  s!  a^m  " baraiti  .  .  Y.  62.  8f.;  —  yim?m  .  .  yerihe xsä^rä',a  ndit  aotim  inha  . .  para  akmät yat  hlm  a!m  *draogpm  välim  .  .  patti.- barata  Yt.  ig.  33 ;  —  tvai  na  *ai^rapaitim updisai  .  .  iim  *aSm  at^^  aS^rapaitim upayat  (sd.)  N.  Jlt;  —  mürtm  .  .  yd .  . frä  rasmanö  scandayeiti  .  .  ari  dlsalm.  . Ji^iM  *baraiti  Vtio-^Gt;  loi,  71  (yavata aim),  .5', 43  {yezi  alm),  47  (ya^a  am); —  aom  asmatum  ,  ,  mariay^n  ahe  yäiia vis  aim  .  .  Yt.  ij,2.  2)  auf  ein  Nomen vorausweisend:  äa^  mg  alm'°^  pait- yaoxta  AaomU..Y.ff.i;  V.2.3.  III)  ver- doppelt, substantivisch  sva,  'irgend  ein  be- liebiger': _)(7/  hl  nazdiUö  dahmö :'dü'/(sd.)  yavat  vä  aSm  aim^^^ uübya  N.2;.
9136:•  j.  kava'rasman-  m.  F.N.  eines  Cliiubigen : -«Hj''  «.tiiö«,- Vt.  ij.103.
9251:srayä  voumkaiaya  Y,  65. 4;  —  ys  haaiay-j  S/-'^v^'^'jU^'ond''zD"'"w',/irLter ...va  uruassayat  '«o»  Yt,5.  131;  —  ^-i  HriÄ^-^  No^T).  -  mp,  fl'ü.  Tu  V.'s  49" rasmanS  hqm.ststse  (sd.)  ^5  ^'na  ">  J'  karkäi,  vgl.  np.  (Npa,)  kargas. iHndayänti  Yt,  jj.  39;  —  yaoz)nH  »aA'«j.*kahrkäs5.parana-"  Adj. 'mit  Federn •«ff  (NP.)'>  rasmans  Ytio.36.  2)  zeitlich  ^  des  (Vogels)  Kakrklsa  versehen':  isunqm (nur  Komp.).  ^-paranum'^  Yt/o.isg.
9273:mit  avi  'entzweischneiden'  (?):  yS  ras- mattS  k»r3ntaydti  .  .  avi  rasmanS  k9r>n- tayeiti  ,  .  v»ri^rafnS  Yt/^.öz,
12780:—  Aurqyai(sii.)ai  . .  aHavatS  daidyat  ä *it  Jrankärayat  A.J.  4;  —  aitat  3?ar»nö frapinvata . .  ä  'im  (als  ASn.) . .  hangiurva- yat  apqm  rtaph  Yt.  /(/.  5 1 ;  —  yaosfnti  vupe karanS  .  .  avi  'if  (APm.)  «»«  .  .  äihim  1 *baraiii  Yt  10.  36 f.;  —  ll  rasmanö  *raica- ,
14493:•  j.  ^Oraxta-')  Adj.  'zusammengedrängt, eng  aufgeschlossen':  'ianam  rasmanqm "phalangum  stipatarura"  Yt.  14-  63-
16982:barasman-  Noten
16984:•  j.  barasman-  n^  meist  kollekt  Sing., Bezeichnung  eines  beim  Gottesdienst  ge- brauchten ZweigbUndeIs*':*Äa/a  nä  *mbma 'tnana   ratufrisi  %rilurvara  (sd.)  N.fjo;
18592:harShre  pasvqmla  . .  "Arm.,  geh  vorwärts und  tu  dich  auseinander,  um  tragen  zu können  .  ."  V.  2. 10.  a)  Kaus.  'aus- einander treiben,  sprengen':  fravasayS  .  . yi  rasmanS  .  .  vf  ma&iyqmtn   namayeinti
19642:_fr(rydit . .  a  *yqnasat  (AblS.)  •>  a  mnhrt- sascit  V.  6. 2  7 ;  —  ava  hl  yarum  bSjyamanS Vd.20.  ß)  bei  Tieren,  sva.  'Rumpf: ^faräim  .  .  vT  'yqram  fiänaydnti  (sd.) handäma  . .  Yti4.  $6.  b)  des  Heers, 'Zentrum' :  visfie  karanS  rasmanS. .  yqrum . . sfi^ahe  Yt  lo.  36;  13. 39.
20954:paiti-ayatahs {^^  Yt  /j.  7;  —  *'iraxtanqm (sd.)  rasmanqm  yüxtanqm  ssi%ranqm ".  .  der  verbündeten  Länder"  Yt.  i4- 63.  b)  mit  Angabe  des  womit?  durch b)  Instr.:  kyat  daina  . .  yüpn  (sd.,  bei4) , . tt^ä  yuxiä  y.4<).  9.  ß)  Dat:  kS  vätai
20988:34.  146,  Hauc  Essayi'  3«).  j'aPKw/i  vtipe  karand  rasmanS  anzojruiafu
20990:',^'  ^^fT";"-  ^^^'^^f'-P"^-      y"''^   bringen':  i-^/^ir^*^ .  .^J  rasmanö  yacza-
20994:•  p.  yauna-'»  Adj.,  bezeidmet  ein  Volk  bringen'(?):  v^-kra^mm  .  .  y5  rasmans •jonisch;  Jonier':  ■«.!  iyaiy  uikahyä  lää  yaosaye-ti  (vgl  SimpL  a  a)  .  .  avi  rasmanS tyaiy  ^drayahyä  "die/,  des  Festlands  und  yaozayeiti  \t14.6a.
25216:»  ].  rasman-  m.,  n.  'Schlachtreihe ,  Pha- lanx': spala  . .  raihm  (sd.)  rasma  (NSn.) katarasHt  Yt  /4. 43 ;  —  ys  'manS  (APm.) sandaydti  Yti^öa;  61',  10.36,  41;  — antan  rSlta  'mana  (ADm.)  Yt74.47;  —
25224:i)  'richten,  gerade  richten,  ordnen':  yat \sp3ta  han/asänte  .  .  ra/t^m  rasma  kata- rasHt  "wenn  die  beiden  Heere  zusammen !  treffen  .  .,  ein  jedes  eine  (in  Reihen)  ge- richtete Phalanx"  Yt  i4-  43;  —  antan \  rästa(ADm.)rasmanaYti4.4T, — yahmya !  sästärU . .  paoiril  Irs  (sd.)  rätayente  Yt.  10. 14.  a)raii';'walsAdv.  sbes.  a)'recken (gewaltsam),  verrenken':  vT  maityqmm fiänayeinti  {s^)  vTspa  handäma  räzayänti Yt  14-  56.
25415:.  .  yB  vXräsaiti  anian  rSsta  rasmana  ä!a
26444:'zerbrechen,  zerstören,  zu  nichte  machen' : yS  rasmanö  iHndayäti  Yt  14.  62;  — Jra- vasayS  .  .  yä  .  .  aurva%anqm  ,  .  iSsBs scandayeinti  YtJj.  31;  —  ime  nS  *^uyra *bäzava  kanta  .  .  sHndayeinti  "die  da machen  unsere  starken  Arme  . .  mit  dem Messer  zu  nicht"  Yt.  /o.  42;—  tum  aisqm.. Ibaisi  scindayehi  Yt. 70.76;  —  alsqm  ihai^S scindaydmtmYt.i.tT,  —  sSndaya  {i%lh..) asavajanS  Yt.  iO.  76;  —  scindayat  F.  12,
26445:mit  ai>i  'entzweibrcchen'(?):  yS ratmanS sHndayäti  . .  avi  rasmans  *sc?ndayeiti'^ Yt  14.  62.
26447:I  mit_^a 'zerbrechen,  zerstören,  zunichte I  machen':  fra  rasmanS  scandayäti  Yt  70.
```


## [2026-09-14T01:13:11.048Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==158' HRN.txt | head -60",
 "description": "Print Horn p.136"
}
```


### [2026-09-14T01:13:12.016Z] TOOL RESULT

```
— 136 -
609. reje^ reze *Reihe\
aw. razista- ^geradester ; ai. räjistha- (Nöldeke,
mündliche Mitteilung). Jüd.-pers. T]T\ dagegen dürfte
zu aw. rasman- 'Schlachtreihe', ai. ragmän-^ racmi'^
ragi- gehören.
Geldner hatte KZ. 24, 387 Note 2 aw. razura-
'Geleis' (yt. 5, 50) vergleichen wollen.
np. rede 'Richtung, Linie, Reihe' (Öähn. I, 367
Vers 823) scheint dagegen zu aw. ereta-, areta-y ai.
ftd' 'richtig, vollkommen' zu gehören (ursprünglich
'etwas Rechtes, Gerades).'
610. ru%8 {rexs) 'Glanz, Licht', ru/^Tden [rexsiden).
aw. vergl. rao/snc^ 'glänzend, leuchtend, strahlend' ;
ai. ruksd' 'glänzend'.
oss. d. ro/s^ t. rü/s 'Licht, leuchtend', rü/say (214);
ya;'n. ru/sinie.
Gehört np. ru/ 'Wange' auch zu derselben Wurzel?
611. red 'weise, tapfer' (z. B. Sahn. I, 149 Vers 365; Vis
und Rämin S. 13, V. 5 v. u.).
aw. ratU' 'Herr'; phlv. rat, -rat^),
612. rezm 'Schlacht, Kampf.
aw. vergl. areza- 'Schlacht'; arm. LW. paterazm
'Kampf, auch razm.
An Ableitung von aw. rasman- 'Schlachtreihe' zu
denken {s könnte statt z vor m stehen), verbietet die
Bedeutungsverschiedenheit (s. No. 609).
613. rest]äy(^e^ 'Auferstehung der Todten'^).
aw. irista- 'todt'; phlv. rist^ ristä/ez (paz. ristaxez),
614. rasten 'wachsen, Praes. röy-em, röylden, röyäniden,
rösta (arab. syr. LW. rustOq), pNDDn, Is. 42, 11.
aw. |/>c/orf-, raoöahe 'wachsen'; phlv. rustan (bezw.
rödastan , aber nicht wahrscheinlich), röyend bezw.
rödent (3. Plur.), rostäk [rödastak, Salemann, Eine
*) Vergl. Nöldeke, Tabarl-Obersetzung, 447.
*) Kaum gehört hierher röz-l *ir,9 'Todestag' (Pertsch, Die
persischen Handschriften der herzogl. Bibl. zu Gotha, S. 115, 116),
vergl- de t^agarde, Ges. Abb» 3?,
```


## [2026-09-14T01:13:12.470Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"rāst\\|razm\\|afrāxtan\\|afrāštan\\|frāzīdan\" HRN.txt | head -30",
 "description": "Grep Horn for rast/razm"
}
```


### [2026-09-14T01:13:12.525Z] TOOL RESULT

```
5468:aw. vergl. areza- 'Schlacht'; arm. LW. paterazm
5469:'Kampf, auch razm.
```


## [2026-09-14T01:13:29.352Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"afrāxtan\\|afrāštan\\|frāz\\|\\*raz\\b\\|raz-\" CHEUNG.txt | head -40",
 "description": "Grep Cheung for raz"
}
```


### [2026-09-14T01:13:29.412Z] TOOL RESULT

```
2046:*AVESTAN: YAv. baraz- ‘to enlarge’, (Gpl.) barazimanam ‘heights’, YAv. barazant- 
2606:*AVESTAN: YAv. braz- ‘to shine’ — Liste: 40 
2638:*NWIR: NP barazidan/baraz- ‘to shine, beam’ 
5108:*AVESTAN: daraz- ‘to attach’ || (+ *ni-) ‘to fasten’ || (+ *ham-) ‘to bind together’. > 
9405:*AVESTAN: YAv. haraz- ‘to release (esp. water, liquid)’ || (+ *aua-) ‘to decline, 
12367:*AVESTAN: maraz- ‘to wipe, rub’ || (+ *anu-) ‘to sweep’ || (+ *a-) ‘to sweep to’ || (+ 
13357:*AVESTAN: Y Av. raz- ‘to draw a line; to direct, richten’ || (+ *ham-) ‘[med.] to rise, 
13441:‘to adorn, decorate, ornament’ || (+ *abi-) NP afraxtan, afrastan/afraz- ‘to raise’ (LW 
13444:(Kand.) -uraz-, (impv.) viraz- ‘to sew, attach’ 
20624:*NEIR: Rosh. réz-, Yzgh. raz- ‘to colour the eyes’, Ishk. reZ-/rüyd ‘to colour 
20909:*NEIR: Bart. ruj-/ruxt, Orosh. ruj-/ruxt ‘to dig’, Wa. riz-, raz-/razd- ‘to tear apart, rip 
21153:*raz ‘to leave, escape (one's notice)’ 
21183:*NEIR: ? Sh. (Baj.) raz-/rixt ‘to fall (leaves, fruit); to crumble, scatter’, Ishk. roZ- ‘to 
21197:9 Henning, l.c. derived SSogd. ’pr’st and Yghn. piráyZ- from *apa-raz-, to which he 
23097:*AVESTAN: OAv. ("ä)sparaz- ‘to aspire to, strive’? = Liste: 65 
25749:traz-/trayd- ‘to tie’, Wa. tranj-/tranjd, tranZ-/tranZd-, trayd-, trayn- ‘to press, 
27619:ayäuuaraz- ‘who does evil’, gauuästriiäuuarez- ‘who does pastoral work’, 
27620:hai@1iauuaraz- ‘making real’, etc. and vauuoroz- (De Vaan 2003: 81 fn. 45, 170 £). 
33318:braz-, 21 
33463:haraz-, 132 
33869:varaz-, 422 
40690:afraxtan, afrastan/afraz-, 
40804:barazidan/baraz-, 22 
42194:baristin/biraz-, 
43020:wirastay/wiraz-, 198 
43114:-uraz-, viraz-, 198 
48282:raz-/rixt, 322 
49701:riz-, raz-/razd-, 318 
55097:*mard, *raic, *raz (S.V.), 
56484:*(h)rah, *raz 
57053:*(h)rah, *raic, *raz, *zaH
```


## [2026-09-14T01:13:32.706Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '13340,13460p' CHEUNG.txt",
 "description": "Print Cheung *raz entry"
}
```


### [2026-09-14T01:13:32.762Z] TOOL RESULT

```
*NEIR: (+ *4-) Oss. І. areexsyn/araxst, D. arzexsun/araxst ‘to fit, match; to deal, cope 
with; to be able’ 

*MISC: Arm. (LW) erasxi-k‘ ‘warrant, security’ (Benveniste 1945: 71) 

*SANSKRIT: raks” ‘to protect, guard’ (RV+) > EWAia II: 422 

9 This root goes back to an apparently old ingress. stem, which has a cognate in Gr. 
*PIE ingress. *Holek-s^/;- ‘to defend, protect” = LIV: 278 | Pok.: 32 


*IE COGNATES: Gr. &A€Ew ‘I ward off, defend’ 
*REFERENCES: Abaev, Slovar’ I: 59; DKS: 233b f.; Werba 1997: 468 


*Hraz ‘to draw a line; to direct, richten’ 
*AVESTAN: Y Av. raz- ‘to draw a line; to direct, richten’ || (+ *ham-) ‘[med.] to rise, 


become erect; to comb’ = Liste: 56f. 

Caus.: pres. IND. 3sg. Y Av. "razaiieiti (Yt 4.9), med. 3sg. YAv. ham.räzaiiete (V 17.2), 3р1. ҮАУ. 
razaileinti (Yt 14.56), med. 3pl. YAv. razaiiente (Yt 10.14), INJ. med. 2sg. YAv. ham.razatianha (V 
17.4), med. 3sg. YAv. ham.razatiata (Yt 19.47); Partic.: pres. caus. razaiiant- (V 8.100 ff.) 


*OLD PERSIAN: rasta- < r-a-s-t-°> (ppp.) ‘right, straight, true’ = Kent: 206a 

*MIDDLE PERSIAN: MMP r’yn-, BMP I’dyn- /rayén-/ ‘to arrange’, MMP r’yyhy- 
(pass.) ‘to be prepared’ || (+ *api- ?) MMP *pyr’st- (pret. stem), BMP pyl’d-, pdl’d- 
/péray-/ ‘to adorn’ || (+ *abi-) MMP ’br’st- (pret. stem) ‘to raise up, exalt’ || (+ *a-) 
ВМР ’I’d- /aray-/ ‘to prepare, arrange, adorn’ || (+ *pati-) MMP pdr’y- ‘to prepare; 
to rise’ || (+ *fra-) MMP pr’r’z- ‘to stretch out’ (LW) || (+ *ui-) 2. MMP wnyr-, BMP 
wynl- /win(n)ir-/ ‘to be arranged, put in order, be prepared’, MMP wyn’r-, BMP 
wyn'l- /winär-/ (sec. caus.) ‘to put in order, arrange’, MMP wyr’y-, BMP wyl’d- 
/wiray-/ ‘to arrange, adorn, prepare’, BMP wl’c- /wiraZ-/ (caus.) ‘to arrange, 


*Hraz 197 


prepare’ (LW), ВМР wyl'dyh- /wirayih-/ (pass.) ‘to be arranged, etc.’ || (+ *ham-) 
MMP hr’s- (pret. stem) ‘to arrange, prepare’. 0 MMP hr’s- with *-mr- > MMP -rr- 
<-r->, also in MMP hrwb- ‘to collect, gather; receive’ (< *ham-raup). Incorrect 
Henning 1933: 187: < *uhrastan < *uzrästanai. || Klingenschmitt (Congress Graz 
2002) compares the WIr. forms wnyr-, etc. to Lat. norma ‘ruler’. It is more 
preferable though to look for a provenance within (Dlr. rather than to rely on an 
obscure and isolated form that is Lat. norma (e.g. no Italic cognates). Perhaps, 
wnyr-, etc. derive from a nasal pres. stem *ui-Hrnza- (cf. Skt. RV rñjá-) > OP 
*vi-Hrnda-, which subsequently shows metathesis and simplification/assimilation of 
the apparently awkward consonant cluster: > win(n)ir- ? > DMMPP: 294a, 290a, 
270b, 277b, 344a, 354b f. 356 

Partic.: pres. caus. MMP r’yn’g ‘leader, guide’, perf. pass., MMP r’st ‘correct, true’, caus. BMP I’dynyt 
/rayénid/; Caus.: pres. IND. 3sg. BMP I’dynyt /rayénéd/, ВМР I’dynnd /rayénénd/, IMPV. 258. MMP 
r’yn-; Inf.: caus. BMP I’dynytn /rayénidan/; Pass.: pres. IND. 3pl. MMP r’yyhynd || (+ *api- ?) Partic.: 
perf. pass. BMP pdl’stk /payrastag/, MMP “pyr’st; Inf.: caus. ВМР pyl’dynytn /payrayenidan/ || (+ *abi-) 
Partic.: perf. pass. MMP *’br’st || (+ *a-) Pres.: IND. 3р1. BMP ’r’dynd /arayénd/; Partic.: perf. pass. BMP 
Pst /arast/, BMP "l'stk /arastag/; Inf.: BMP "Tom /arastan/ || (+ *pati-) Pres.: IND. 1р1. MMP pdr’ywm; 
Partic.: perf. pass. MMP pdr’st || (+ *fra-) Pres.: IND. 1р1. MMP fr’r’zwm, SUBJ. 1р1. MMP pr’r’z’m; 
Partic.: perf. pass. MMP pr’r’st || (+ *ui-) Pres.: IND. 3sg. MMP wnyryd, SUBJ. 1sg. MMP wnyr’n, 35р. 
MMP wnyr’d, etc. Caus.: pres. IND. 1sg. BMP wyl’dym /wirayém/, 3sg. MMP wyr’yd, BMP wyl’dyt 
/wirayéd/, 3pl. BMP wyl’dynd /wirayénd/, etc. || (+ *ham-) Inf.: MMP hr’stn 

*PARTHIAN: r’st ‘true’ || (+ *pati-) pdrz- ‘to rise up’, (caus.) pdr’z- ‘to raise up’, ? 
pdr’y- ‘to prepare, make ready; to achieve’ (< MP ?) || (+ *ui-) wyr’z- ‘to complete, 
arrange’, wyn’r- ‘to put in order, arrange, array’, wyn’r’g ‘arranger’ (< MP) 
= Ghilain: 69 f., 52, 70, 75 | DMMPP: 293a, 270b, 356b, 344a, 354b f. 

(+ *pati-) Pres.: IND. 3sg. pdrzyd, 3pl. pdrzynd; Partic.: perf. pass. pdr’st, caus. H pdr’z’d; Caus.: pres. 
IND. 3sg. pdr’zyd, 3pl. pdr’zynd, SUBJ. 2sg. pdr’z’h || (MP LW ?) Pres.: IND. 3pl. pdr’ynd; Partic.: perf. 
pass. pdr’st, П pdr’y’d || (+ *ui-) Pres.: IND. 35р. “wyr’zyd, 3р1. *wyr’zynd, SUBJ. *wyr’z’, IMPV. 2pl. 
wyr’zyd; Partic.: pres. wyr’z’n, perf. pass. wyr'st; Inf.: *wyr'stn || Pres.: IND. 3pl. wyn’rynd, SUBJ. 2sg. 
wyn’r’h, 3р1. wnyr'nd; Partic.: perf. pass. "wyn’r’d 

*KHOTANESE: Khot. rras- (denomin. ?) ‘to rule’ || (+ *aua-) varas- (varas-) ‘to 
experience’ || (+ *fra-) harays-, (caus.) һагаѕ- ‘to extend’ || (+ *ш-) birays- (biras-) 
‘to extend, spread’ = SGS: 115, 119 f., 149 f., 98 

*SOGDIAN: BSogd. rsth, CSogd. rst’ (f.) ‘truth’ || (+ *uz-) CSogd. zrys(-) ‘raise, lift 
up’ || (+ *pati-) BSogd. ptryz- ‘to rise’, CSogd. ptrz- ‘to become exalted, be proud’, 
(caus.) BSogd. ptr’yz- ‘to raise, erect’ || (+ *fra-) SSogd. Br’s- ‘to conclude a treaty 
(?)’, BSogd. fr’yz-, CSogd. fryZ- ‘to straighten, make straight’ 

(+ *uz-) ’z-Impf.: IND. 35р. CSogd. zrys’z || (+ *pati-) Pres.: SUBJ. 35р. BSogd. ptryz’t, OPT. 35р. 
CSogd. ptrzy; Fut.: IND. 35р. CSogd. ptrztyq’; Caus.: pres. IND. 35р. BSogd. ptr’yzt, POT. 3sg. BSogd. 
ptr’yztwnty || (+ *fra-) Pres.: SUBJ. 35р. BSogd. fr'yz't; Pret.: tr. IND. 35р. SSogd. Br’stw Ai ‘he 
concluded a treaty (?)’; Partic.: perf. pass. CSogd. frst- ‘straight, upright’ 


198 *(H)spar(H)j 


*CHORESMIAN: "rz- (TZ-) ‘to be straight, just, in order; ‘to be extended’, (caus.) r’zy- 
‘to make straight; to demand (justice from)’; to arrange’ || (+ *abi-) m/’brzy- ‘to feel, 
sense, observe’ || (+ *fra-) hr’zy- ‘to grab, stretch out to’, hr’zyk ‘extended (string)’ 
(74.1) || (+ *ui- ог? *aua-) wr’ry- ‘to sweep’ (diff. MacKenzie I: 546) = Samadi: 
177, 2, 168, 91, 216 

*NWIR: Awrom. (awa-)faznay/(war-)fazn- ‘to adorn’ || (+ *api- ?) NP pérastan/péray- 
‘to adorn, decorate, ornament’ || (+ *abi-) NP afraxtan, afrastan/afraz- ‘to raise’ (LW 
?), NP afraz ‘exalted’ (LW ?) || (+ *а-) NP arastan/aray- ‘to adorn’ || (+ *ui-) Zaz. 
virastis/virazen- ‘to prepare, restore, build’, Awrom. wırästay/wıräz- ‘to sew’, Gur. 
(Kand.) -uraz-, (impv.) viraz- ‘to sew, attach’ 

*NEIR: (+ *aua- or *ui-) ? Yi. uriz-/urizd ‘to spread manure’ (Morgenstierne, IFL 
Ile Rather *Hraiz ?) || (+ *а-) Oss. І. arzzyn/araezt, D. ar&zumarzzt ‘to be 
arranged, done’, I. arazyn/areezt, D. arazun/arzzt (caus./tr.) ‘to direct to; to 
construct, build, make; to adorn’, ? Pash. ar(a)t ‘wide, expanded’ || (+ *uz-) Sh. Xáz-/ 
xäzd ‘to darn, mend (shoes, etc.)’, Wa. Saz-/Sazd- ‘to darn’ || (+ *pati-) Sariq. 
padráz-/padrázd, Wa. рыігы2-/роігоға- ‘to lean on, against, support on’ || (+ *ui-) 
Oss. I. ræzyn/ræzt, D. irezun/irezt ‘to grow, gain in length; to be arranged’, Rosh. 
wiréz-/wiroxt, Bart. wiroz-/wiróXt ‘to make, build’ 

*MISC: Par. réz-/rast ‘to make, build, prepare’ || (+ *pati-) Arm. (LW) patrast ‘ready’, 
Arab. (LW) fihrist ‘index, table of contents, catalogue’ (Bailey 1935: 762 f.) || (+ 
*fra-) Par. rhiz- ‘to lie down’ || (+ *ui-) Arm. (LW) varsa-viray ‘hair-dresser’ 
*SANSKRIT: raj ‘to stretch, direct’ (RV) = EWAia II: 425 

«PIE *H3reg- ‘to stretch, direct’ = LIV: 304 f. | Pok.: 854 f.
```


## [2026-09-14T01:13:44.114Z] TOOL CALL #24: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py",
 "description": "Inspect ref_page tool"
}
```


### [2026-09-14T01:13:44.169Z] TOOL RESULT

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


## [2026-09-14T01:13:45.411Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -c 1500 BQT_v1_pages.txt; echo; echo ====; grep -c \"pdf page\" BQT_v1_pages.txt BQT_v2_pages.txt",
 "description": "Check BQT page files format"
}
```


### [2026-09-14T01:13:45.465Z] TOOL RESULT

```
۱ ۵ ۱! ۱
7 موم ۳ لام
م ۱ 0 و طق صفرررنیاعدریرماروی
۰ ۱ "۳
۳
م و اس مر هر وه او
7 رین خلت ریز یتایب بره ات
لف‌بال ۶۲ .یرک
ا اند کل داي رشب , رمع
فان تا تا
رن 9 3
کرحم تن
اد شش مرا
مو رم | مر
وک رهب اه نات مج
لش
وان روکد ور
۱ و
طراول ؛ | ع اس
چاپ دوم فروردین ۱۳۴۳
با تجدید نظر کامل
بسرمایه کنابفروشی ابن سینا - تپر اناداره کل دک زون.
شماره ۷9 9 ۳
بر
5
‌ ۰ م۸
و «ارس‌شبات
4
د انشمند محتر م آقای‌د کترمحمد معین‌استاد دانشگاه تهران
فوپانت تاموی ۲۰/۹/۳ ها رتیفارد *
کلیه حقوق‌تجد ید طبم کتاب برهان قاطع با تمحیحات وحواشی و
تملیقا ت وتصا ویرواقتباس‌وتلخیص وترجمه آن بنام‌جنابمالی
محفوظ ومخصوص خوا هد بودضمنا وزا رنفرهنگ فرصت رامفتنم شمرد ه
بد ینوسیله اززحمات شماد رانجام این‌خد مت مهم فرهنگی قد رد انی
میکند وموفقیت آن) ستا د محتر مراد را ینکونه خد مات خواستاراست»
هنگ
رن
یی سینشیر زوا عرسا رده ارسال ۱۳۱۷ ۰۳۳1« 9 لو امد ۰
/ ی و ۷ مر
دسج ناویح ( منیا مینست
با ل 
(eval):1: === not found
```


## [2026-09-14T01:13:49.786Z] TOOL CALL #26: Bash

```json
{
 "command": "grep -o \"\\[pdf page [0-9]*\\]\" data/verification/sources/refs/BQT_v1_pages.txt | head -3; echo \"---v2---\"; grep -o \"\\[pdf page [0-9]*\\]\" data/verification/sources/refs/BQT_v2_pages.txt | head -3; echo \"--- try tool ---\"; timeout 600 python3 tools/ref_page.py BQT:134 2>&1 | head -60",
 "description": "Try ref_page for BQT:134"
}
```


### [2026-09-14T01:13:50.995Z] TOOL RESULT

```
---v2---
--- try tool ---
no scan of BQT covers printed page 134 (see 'scans' in refs_online.json)
```


## [2026-09-14T01:13:55.371Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nprint('formfeeds', t.count(chr(12)))\nt2=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nprint('v2 formfeeds', t2.count(chr(12)))\nimport re\nprint(re.findall(r'\\[[^\\]]{0,30}\\]', t)[:10])\n\"",
 "description": "Count BQT page separators"
}
```


### [2026-09-14T01:13:56.544Z] TOOL RESULT

```
formfeeds 776
v2 formfeeds 683
['[شکار\x0cیازده زبانبای\u200cایرانی\nشدن ]', '[ نجمله ابوریحان بیرونی\nدر ]', '[\n۲ م, 6۵۷6۱۱5/6 . ظ و ]', '[در: افتالیدن (شکافتن)]', '[است]', '[ به ]', '[رك:ص\u200cهشتادوپنج ]', '[ وجه.]', '[بن]', '[ بن ]']
```


## [2026-09-14T01:14:00.813Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f in ['BQT_v1_pages.txt']:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    pages=t.split('\\f')\n    for i,p in enumerate(pages):\n        if 'افراشتن' in p or 'افراختن' in p:\n            print(f, 'leaf',i, repr(p[:80]))\nEOF",
 "description": "Find afrashtan in BQT v1"
}
```


### [2026-09-14T01:14:01.974Z] TOOL RESULT

```
BQT_v1_pages.txt leaf 183 'وت دستور زبای پارسی\n۴ آشفتن » و« رفتن » خوانندمگر جابی که وزن شعر اقتضا کند اشوف'
BQT_v1_pages.txt leaf 256 'آشناو ۳ ف_\nرای فرشت ۰ بمعنی شناور باش که شناکننده | شور و فتده و غوغا - و بمعتی '
BQT_v1_pages.txt leaf 362 'اتمون\nحمف خدایتمالی هم هست! -\n/ لتیهاون » بعتح\u200cاول. دوابی\u200cاست\u200cممروف\nوآن شَكوفةٌ '
BQT_v1_pages.txt leaf 400 'واجب و بفستا وا گیبتد و جر هی اهنت »\nو آن\u200cقدارست ازسرانگشت ,کوچك ۷ مرانگشت\nبزر ک'
```


## [2026-09-14T01:14:10.413Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (361,362,363):\n    print('==== leaf',i)\n    print(pages[i][:2500])\nEOF",
 "description": "Print BQT v1 leaf 361-363"
}
```


### [2026-09-14T01:14:11.634Z] TOOL RESULT

```
==== leaf 361
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
افتاد جنم اول بروزن استاد ۰ بعنی از
بای درآمد - و کنابه از دور شد هم هست که
ماضی دورشدن است .
افتاث گان » کاب از مظلومان
ویر بشان شدکان‌باشد .3۶
افتاده ممعثی عاجز و سقط وخراب
که و ژبرن گردننه باخد..
اقتال ‏ یک راون بروزن اقبال . به‌عنی
برا گنده وباشیده - وشکاقه ودریده باشد .
افتا ليفن « بکراول مصدر افتالاست
که بمعنی پراکندن و یائیدن و افشاندن -
وشکافتن ودربدن باشد .
افتان و خیز ان - کنابه از آحته
ودیر براه رفن باشد .
افقد - بنتم اود و کسر الث مر وژن
محجد ؛ و بمعنی ستاننده و متایش. کنده. باق ت
وبععنی شگفت وعجب ونعجب هم‌هسته .
افتدستا - کلمه ابیت مرکب از افتد
ستایش‌عجب وئیکوترین ستاش‌وبند گی- ویمعنی
2 ۱ متفه
۴ - بوتانیلا ان «اشتینگای».
==== leaf 362
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
افر احته بر وزن برداخته ». نی
برداشته وبلند گردانیده .
/ فر ازه بر وزن برواز, بمعنی‌بلندی
وبلند باشد - وامربدین معنی هم‌هست بعنی‌بردار
وبلند ساز - واسم فاعل هم آمده ات که بلنف
کننده باشد - و عنبر خطیبان را هم گویند -
ویمعنی جمم‌باشد که در مفابل فرد است - ویسته
و کشاده وبین شده را نیز گومند - ویمعنی‌قریب
وترديك وپیش باشد - وغشیب را هم کنته‌اند که
درمقابل فراز است - وبمعنی آزین باز و بعد از
این هم هست - و سر کش و سر کشیده را نیز
«ک تفت وا بینی آت تتال هم آمده است .
افر از بدن بمعئی ‏ بلند ساختن
و افراختن باشد - وبمعنی آراستن و زب دادن
وخوش کردن هم مده است .
افر اس س پروزن کربای . خیمه‌وفناث
را گویند ۰
بمعنی سواران آپ است که حباب باشد .
اقر اسیاب۱ - نم پادشاه تر کتان
است - و کناده ازهموار براه رونده هم‌هست جه
آب پمعنی راء رو هموار است .
افراشت بروزن برداشت , بعنی بلند
ساخت وبالا برد .
جز ازایز و تواع خداو ندی
==== leaf 363
افر اشتن بروزن ومعنی‌برداشتن: بلند
ساختن باشد .
افر اشته بروزث ومعنی برداشته‌و بطند
ماخته و بالارده )۱( باشد ۰
۱ فر دون - بفتح اول رانی‌وسکون‌نالث
و کربای ابجد وبای حطی بواو رسیده و بنون
زده , دوایی اس تکه آنرا قرفیون کوبند . ا کر
کزند کی جانوران را نانع است .
که آنرا بشیرازی بالنگوی خوورو (۲گوبند .
ء اس را نافع است ۳
نام شهرست که نوشیروان آ ادکرده بود در کتار
دربای مصی » و مادر عثرا از آن شهر است ۱ -
وم ولایتی‌است از زنگبا - وم زمینی ه‌هست
در بلاد غرب ۰
ارف » بروزن فرزند ۰ فر و نیکوبی
وزیبایی وحشمت باشد؟ .
افر ندیدن مصدر افرید است بعنی
زب دادن وزشت کردن وآراستن .
افر نگ . بروژن و معنی اورنگت لست
تخت پادشاهان باشد - وبمعثی فر وفکوبی
کون که بمربی صاری‌خوانند؟ .
49 چث : (- شده .
۱ -ظ , معرب افرنگه.
۲ ۱۳
افر و خشن؟ « بروزن اندوختن بسعنی
روئن کردن آتش رچراغ باشد .
افر ود بر وزن سردوز . بممنی
روشن و روشن کردن باشد - و روشن کننده را
نز گویند - وامر بدین‌معنی م‌عست بمنی‌روشن
کن ویفروز . *
افر وسا لین باین بالف کشیدم و کس
لام وبای‌حطی بتحتانی رسیده وبنون زده ؛ بلخت
بونانی6 سنکی است که آنرا حربی حجر القمر
خوانند ؛ وآن سفید وشفاف میباشد ودر شبهای
افرونی ماه می‌بابند , اگر بر گردن‌مصروعبندند
شفا باید .
افر و شه۱ ۳ بفتح اول وشن شطمرار .
نام حلوابی است. وآن چنان باش دکه‌آرد وروغن
را باهم بيامیز ند وبدست بعالند تلدانه داله گُردده
آنگاه در بائیلی کنند وصل‌درآن ریزندوبربالای
آش هند نا يك بیزد و سخت شود - و بحنی
گوند نان‌خورشی‌است د رکیلان. و آن‌چنانباشد
که زرد؛ تخم مرغ را در شیی خم ریزند و يك
برهم زند ویربالای آاش نهند ۴ شیرمانند دلمه
بىته شود بعد از آن شیرینی داخل آن سازند
ونان را درآن تربت کنند با خشکه پلاو در آن
ریزید و با قاشق خورند - وحلوای کندم دلیده
شده - ولوژیشه را فیزافروشه گوبند .
افروغ « بنتح‌اول. بسنی‌فروخ‌ودوشنی
وفابش وپرنو باشد اعم‌از دوشنی‌وپرنو فتاب وعاء
و آش و امثال آن :
۱ فر هنج ه بغع‌اول واكوها وسکون
(۲) چك : خرد .
۵ افروزیدن - رکه : افروختن .
۱ رک : آفروشه .
```


## [2026-09-14T01:14:24.174Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('n',len(pages))\nfor i,p in enumerate(pages):\n    for w in ['رزم','ریال','رده','راست','رج']:\n        pass\n    if 'رزم' in p[:400] or 'ریال' in p[:400]:\n        print(i, repr(p[:100]))\nEOF",
 "description": "Scan BQT v2 leaves"
}
```


### [2026-09-14T01:14:25.672Z] TOOL RESULT

```
n 684
125 '                                        \u202bيان بیستم\u202c\n             \u202bونات\u202c\n                \u202bدر جیم فارس'
142 '      \u202bا\u202a4\u202cس\u202c\n        \u202bسه\u202c\n\n\n\u202bکوبند؟ \u202a -\u202cواز\u202c                                               \u202bحر با _'
201 '  \u202bخرش\u202c                                                                                             '
629 ' \u202bمگ\u202c                                                                                       \u202bاس\u202c    '
678 ' \u202b\u202a۷۲۸\u202c\u202c                                                                                            '
```


## [2026-09-14T01:14:31.807Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    n=p.count('رزم')+p.count('رژه')\n    if n>2:\n        print(i,n, repr(p[:60]))\nEOF",
 "description": "Find razm-heavy leaves in BQT v2"
}
```


### [2026-09-14T01:14:33.044Z] TOOL RESULT

```
405 3 '  \u202bرزه\u202c                                                     '
598 3 '    \u202b\u202a-۱ ۱۳۹\u202c\u202c\n\u202bهآممده است \u202a ۵\u202cو\u202a-\u202cنام ولابتی وجایی\u200cبیز هت\u202c '
```


## [2026-09-14T01:14:35.715Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (404,405,406):\n    print('==== leaf',i)\n    print(pages[i][:2000])\nEOF",
 "description": "Print BQT v2 leaves 404-406"
}
```


### [2026-09-14T01:14:36.800Z] TOOL RESULT

```
==== leaf 404
   ‫‪—ttA‬‏‬                                                                            ‫رد کا‬
 ‫رده ‪ - ۴‬تح اول وثالی » صف ورستة‬                ‫ردک ‪١‬ہ‏ بفتح اول وسکون ثالی وکاف‬
 ‫آدمی وحیوانات دیگر‪ -‬وهرچیز که وربكراسته‬       ‫بالف کشیده » بلغت زند و پازند ( ‪ ) ۱‬بمعنی‬
 ‫باشد حمچو دندان و دکان و خاله و برح وامثال‬    ‫راست و درست باشد که درمقابل کج و درد غ‬
 ‫آن‪ ۴‬وچوبیرا یز گوبند که درزبرآن غلطکها‬                                              ‫است ‪.‬‬
‫راست کنند وبر گردن گاوبندند وبربالای غلهکه‬      ‫رد نحو ؟ ‏ باجیم بروزن سمن بو ‪۰‬‬
             ‫ازکاه جدا شده باشد بگردانشد ‪.‬‬
                                                ‫ام کرمیست که پشمینه راخراب میکند وبعربی‬
                                                ‫واين ممنی بجای حرف ثالی‬
                                                                      ‫ارضه گوبند ؛ ب‬
   ‫است که یکی از دوازده برج قلکی است ‪.٩‬‏‬                                   ‫واو هم آمده است‬



                                       ‫بیان هشتم‬
             ‫‪۱‬هر سنرده لغت‬        ‫‪۳‬‬     ‫در رای بی‌نقطه بازای نقطه دار‬


‫وحرباغ را گونند‬   ‫وبمعنی انگورهمآمده است ‪-‬‬      ‫مفتح اول و سکون تالی » درخت‬     ‫=‬   ‫رز‬

  ‫انکور باشد ® و بمرپی‌کرم خوانند یفتح‌کاف ‪ | -‬عموماً ‪٦‬‏ ‪ -‬و باانعکور را خصوصاً و‪-‬مطلق‬

                                                          ‫‪ :‬رتد ویاژند ‪.‬‬   ‫)‪ (۱‬چك‬


      ‫‪ ۱‬هز ‪ , 2120۵۲‬پهلوی ‪ ۰ 452۲‬راست «یونکر ‪ ۵۰۱‬بی‌اصل « رادکا » امت‬
    ‫‪ ۴‬ظ » ازیهلوی ‪ « # 61202۲‬حوشمان‬           ‫‪ - ۴‬مصحف « روئجو » (ھ‪.‬م‪. ).‬‬
           ‫‪ 6‬ورکه ‪ :‬استق ‪ » ۹۰‬در اوراق مالوی (پهلوی) ‪( 80۲‬سطر » صف ؛ ردیف)‪:‬‬              ‫‪۹‬‬
           ‫‪(Henning,‬‬      ‫‪A list of Middle‬‬         ‫‏)‪Persian..., BSOS ,lX,1,p.87.‬‬
  ‫ودو جزو مکی برین کنار‬      ‫‪۰:‬‬       ‫را‬               ‫کے کو‬
   ‫* گیلکی ‪ 22۳‬ازتبره رزها است ودر‬              ‫نپی ویکی بنرکآناراهی ‪« »...‬داشنامه ‪.*۷۷‬‬
                                  ‫تمام لقاط ‪ 8‬سطح زمی‌کاشته میشود ‪.‬گلهای آن د
==== leaf 405
  ‫رزه‬                                                                                               ‫‪‎-‬ی ) ‪“A‬‬


 ‫مکان‌جنکه‬      ‫زرمگاه‪ -‬بروزن گا‬                         ‫رنگضرا کننزته‌اند ‪-‬و‪٩‬ی‏معنی رنگ کننده ‪- ۴‬‬
                                                         ‫وامر برنگ کردن هم هت ‪٩‬‏ ‪ -‬و زهر هلاهل‬
                                                          ‫را کیویزند ‪ -‬ویکس اول مخقف ریز باه‬
                       ‫گاه باشد ‪۲‬‬   ‫کردن وجنگ‬

   ‫مت‬      ‫که‬         ‫ون‬     ‫ررمگه ‪-‬‬
             ‫رزمگاه است که جنک گاه باشد ‪۹‬‬                ‫ازریختن مشتق است ‪ -۴‬ودرعربی شالی راگوبند‬
 ‫بروزن گرم سیر ‪ ,‬لامروز‬
                                                         ‫کبهرنج پوست دباارشد ‪ ۴‬چرهزاز براج کوب‬
                        ‫مگیر =‬            ‫رد‬
                   ‫بازدهم باشد از ماهپای ملکی ‪۱‬‬
                                                                                      ‫رکاویند ‪.‬‬
 ‫ررمه = بفتح‌اول والك وسکون ثالی»‬                       ‫ربران * د بباای ابجدبالف کشیده‬
  ‫ایند*‪ -۱‬وبك لنگه بار واسباب‬
                            ‫رو‬‫بوفچرخت ک‬                                  ‫بروزن بزدان ‪ .‬باغبانرا گویند ‪.‬‬
 ‫وقماش را نکیفزته‌اند » و بکضویبند ابن لفت‬               ‫ررد ‏‪ = ٩‬بقتح اول وسکون نالی ودال‬
                    ‫غرمی است‪ »:‬وبکسی اول ات‬                     ‫ابجد (‪ » )۱‬پرخور وشکم خوار کروایند ‪.‬‬

 ‫دزم یوز بوامبیامی حطی (»)‬                               ‫ررده ‪ = ۷‬بقتح اول بر وزن زرده »‬
                                                              ‫بمعنی «انده وکوفته شده وآزرد‪ :‬راه باشد ‪.‬‬
‫جوز بمعنی تفحص و تجسی و جستجو کردن حم‬                    ‫درم = بفتح اول وسکون الی و میم »‬
                                    ‫‪٣‬‏‬    ‫آ مده ات‬       ‫بمعتی جنک و جدال باشد ‪ - ۸‬و هیمه وهیزم‬

    ‫زره د بنتح اول وتخفیف ثالی » ن‬                       ‫وی »‬
                                                            ‫طعام پختن را نیزگوند ‪ -‬و بفتحاتولال‬
‫‪۱‬ت‪ .۴‬وآن ناي
==== leaf 406
      ‫‪- 6‬‬                                                                               ‫رژیدن‬

‫رر بدن "ت بورژن رسیدن » بمعنی‬                      ‫اندازند وبعربی شربط کوبند وبزبان دیگر سازو‬
                      ‫رنگه کردن باشد ‪.‬‬             ‫خوانند ‪ -‬وسکه انگور را کیفزته‌اند که بتازی‬
‫ددلن » بر وزن امین ‪ ۰‬بمعنی محکم‬                    ‫عنب‌الملب کوبند = و باتشدید ثالی در عربی‬
                                                  ‫حلقه‌ای که برآستان درس کنند ‪ ۱‬و‪-‬ققل را‬
‫واستوار ومضبوط باشد؟ ‪ -‬ودرعربی‌به‌عتی آرمیده‬
‫و آرامکرفته و کرامایه وچیزبکه بوزن کران‬             ‫لیز کوبند‪ .‬وبمعنی زدن‌هم‌هست که بعربی ضرب‬
                                ‫وسنکن باشد ‪۴‬‬                                            ‫خوانند ‪.‬‬



                                         ‫بیان نهم‬
                  ‫غوت‬
                    ‫لد‬‫ررای بنیقطه با زای فارسی مشتمل بر‬
                                                      ‫د‬

‫ررد (‪ »)۱‬بفتح اول وسکون انی بر | براستی‌آن دبوار سازد وآنرا رزه‌بهنایز کوبند‪-‬‬
‫ورسمالی که هر دو سر آ را برجایی نشدلد ویر‬          ‫درهمه چیز را‬   ‫‪ ,‬سيار خوار وحر‪.‬ص‬     ‫وزن وجد‬

‫ومثال آن اندازند و آنرا‬
                      ‫آن رخوت پوشیدلی ا‬                                              ‫کوبند ‪: ۷‬‬




                                                                    ‫(‪ )۱‬چك‪ :‬رزد ()‬
  ‫از ‪ :‬رز (ه‪.‬م‪٣ ) .‬‏ يدن‬    ‫‪-‬‬    ‫‪۳‬‬             ‫امروز « چفته ورزه » مستعمل است ‪.‬‬   ‫‪- ۱‬‬

                    ‫‪ ۴‬ماخون از (عی) «ناطمالاطبا» رك‪ :‬حاشية ‪: 4‬‬               ‫(پونه مصدری) ‪.‬‬
         ‫چون عهد ٽو ليکو وچوحلم "و رزین‌است‪.‬‬            ‫چون قدر تو عالی وچو روی توکشاده‬
  ‫د منوچهری دامفانی ‪.* ۶۷۱‬‬
      ‫(عر) ‏ رزن ازباب کرم بعنی آهسته و بآرام شد ووصف آن د«ررمزکیرن»‪...‬‬             ‫‪۴‬‬
  ‫® _ رك ‪:‬‬              ‫و «درزین » چیزکرانمابه و تقیل و باسنگه است‪ « » .‬شرح قاہوی *‪.‬‬
                                                                                   ‫رزد » ری ‪.‬‬
           ‫ز
```


## [2026-09-14T01:14:56.130Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[405][1500:4000])\nEOF",
 "description": "Print rest of BQT v2 leaf 405"
}
```


### [2026-09-14T01:14:57.709Z] TOOL RESULT

```
رده »‬
                                                              ‫بمعنی «انده وکوفته شده وآزرد‪ :‬راه باشد ‪.‬‬
‫جوز بمعنی تفحص و تجسی و جستجو کردن حم‬                    ‫درم = بفتح اول وسکون الی و میم »‬
                                    ‫‪٣‬‏‬    ‫آ مده ات‬       ‫بمعتی جنک و جدال باشد ‪ - ۸‬و هیمه وهیزم‬

    ‫زره د بنتح اول وتخفیف ثالی » ن‬                       ‫وی »‬
                                                            ‫طعام پختن را نیزگوند ‪ -‬و بفتحاتولال‬
‫‪۱‬ت‪ .۴‬وآن ناي ا هردوسوآیرا‬                 ‫‪E‬‬             ‫رنگه هم‌آمده‬     ‫بعنیر نگه میکنم‪٩‬‏ چه ربزمعتی‬




                                         ‫(‪ )۲‬چك ‪ :‬بامیم ویا‪.‬‬               ‫امد‬       ‫‪:‬‏‬   ‫(‪ )۱‬چك‬


   ‫رکه ‪:‬‬     ‫‪۴‬‬           ‫‪ ۴‬در ‪ :‬رنگرز ( رنگگ رزنده ) ‪.‬‬                  ‫‪ :‬رزیدن ‪.‬‬         ‫رکه‬
                                                                                            ‫‏‪٩‬‬
   ‫*‏ از ‪ :‬رز‬            ‫وید دوم) برنج ( منتهی الارب ) ‪۰‬‬
                                                       ‫اتولشد‬               ‫م‬
                                                                            ‫(ضرز‬
                                                                               ‫‪۴‬‬                     ‫ربخن ‪.‬‬
                                                   ‫(باغ وباغ انگور) (ه‪.‬م‪ ).‬بت بان (یسوند حفاظت ) ‪:‬‬
         ‫مادر ایز‪ ,‬بچگکایرا ندهد شیر همی ‪...‬‬                  ‫رزبان گفت چه رابت وچه ندییرهمی‬
    ‫«منوچهری دامخانی ‪ ۸۲۱‬ورك ‪ :‬رز‬
             ‫‪ ۷‬ظ ؛ مصحثف « زردهم» مخذف ‪ 5‬آزرده * ‪.‬‬                       ‫ری ‪.‬‬   ‫»‬   ‫رژد‬   ‫رك‪:‬‬   ‫‪۹‬‬


    ‫(ده وصف جنك) از ‪= 74۲‬‬   ‫‪ - ۸‬از پارسی باستان ‪٥ 200123۲‬‏ = اومتا ‪ 30152۲‬ر‬
   ‫[رك‪ :‬رده ] رك‪ :‬هو شمان‬     ‫هندوزرمالی (هند و ارویادی) ‪EET‬‏ قس‪ :‬خاشکریت ‪ijar‬‏ (رده سف)‬

                                ‫ارمنی ع ‪( 0۳22۲6۱۵۳‬جنکه) و ‪« 0122۲‬اسشق ‪۲۱۱٩‬‏ ‪.‬‬                             ‫‪۲‬‬
   ‫است‬   ‫سته‌شده‬   ‫آجیزیتکه‬     ‫بکراول»‬        ‫) عر ( «رزمه‬    ‫‪۹‬‬          ‫‪‎‬ندیزر > ‪.‬‬
                                                                                 ‫‪ _ ٩‬زا «‬
   ‫دربك جامه و آنرا بفارسی پشت وارء میگویند و آن قدری از جام بکجا بسته است که‌بریشت‬
                                                                        ‫توان برداشت ‪« ».‬شرح قاموس »‬
   ‫انون مخرمن؛عودسوز اکنون‌بتنگه‪.‬‬
                                ‫مثك ریز ک‬                     ‫خزبده اکنون برزهه» می‌بده اکنون برطل
```


## [2026-09-14T01:15:17.078Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\ndef norm(s):\n    return s.translate(str.maketrans('۰۱۲۳۴۵۶۷۸۹','0123456789'))\nfor i in range(395,415):\n    head=norm(pages[i][:200])\n    nums=re.findall(r'\\b\\d{3,4}\\b',head)\n    print(i,nums, repr(pages[i][:70]))\nEOF",
 "description": "Extract page numbers from BQT v2 leaf headers"
}
```


### [2026-09-14T01:15:18.320Z] TOOL RESULT

```
395 [] '  \u202bراهوی\u202c                                                             '
396 [] '\u202bومطلوب را گویند و مردم ماز ندران ربکا\u202c         \u202bمصوب\u202c        \u202bراهی = '
397 [] '                                                 \u202bبیان دوم\u202c\n\n         '
398 [] '  \u202b—\u202a—Ara\u202c\u202c                                                           '
399 [] '                                                                      '
400 [] '    \u202bسس\u202c                                                              '
401 [] ' \u202bرخش\u202c                                                                '
402 [] '  \u202b\u202a4 ) ۰۷\u202c\u202c                                                          '
403 [] ' \u202bردای لیل\u202c                                                           '
404 [] '   \u202b\u202a—ttA\u202c\u200f\u202c                                                          '
405 [] '  \u202bرزه\u202c                                                               '
406 [] '      \u202b\u202a- 6\u202c\u202c                                                         '
407 [] '                                                    \u202bبیان دهم\u202c\n       '
408 [] ' \u202b—\u202aAtA-\u202c\u202c                                                            '
409 [] '  \u202bبا\u202c                                                                '
410 [] '   \u202bها\u202c    \u202bوی\u202c   \u202b\u202a-\u202c\u202c\n                                              '
411 [] ' \u202bرشتاك\u202c                                                              '
412 [] '    \u202b\u202a“Ao\u202c\u202c\n                                      \u202b\u202ae\u202c\u202c\n\u202bرشته نگنده \u202a '
413 [] ' \u202bرسد گه ځا کی\u202c                                                       '
414 [] '                                         \u202bيبان سیز دهم\u202c\n              '
```


## [2026-09-14T01:15:24.880Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (399,400,401):\n    print('==== leaf',i)\n    print(pages[i][:2600])\nEOF",
 "description": "Print BQT v2 leaves 399-401"
}
```


### [2026-09-14T01:15:26.497Z] TOOL RESULT

```
==== leaf 399
                                                                                                     ‫‪ 4۳‬هت‬
                                                  ‫که کیاهی باشد که چرنده را خوردن آن مت کند ‪.‬‬




                                                ‫بیان جهارم‬

                 ‫مشتمل برچهار لغت‬                   ‫فرشت‬
                                                       ‫یه‌با‬
                                                           ‫اقط‬
                                                             ‫دررای بتی ن‬
 ‫رنگه‌میباشد ونرآادرآب کنند ودست‌برآن زد‬                      ‫»رهنه و عریاترا‬
                                                                            ‫ه بفتح اول ‪ ۱‬ب‬                ‫رت‬
 ‫چون‌صابون کف بآروردجامه بدان شویندخصوصاً‬                     ‫گوبند ‪ -‬وم اول تهی دست وبینوا ‪ -‬وبرهنه‬
                                                             ‫وخالی گروابند ‪ -‬و بمعنی‌کاغذ هم بنظر آمده‬
‫جامة ابرشمی‪ .‬وچون باسرکه برختازیر طلا‬
‫کنند تحلیل دهد » و اکر بماآربزنگوش در‬                        ‫است ‪ - ۴‬و همه را نیزگوبند و بعربی کل‬
                                                                                                          ‫خوانند ‪.‬‬
 ‫فندق‬      ‫بوی‬
             ‫رد »‬
                ‫صپبر‬
                   ‫کبوری را‬
                          ‫چشم کشند ش‬
                                 ‫خوانند ‪. ۴‬‬     ‫هندی‬
                                                              ‫رتك ب=ضم اول وفتح‌ثالی وسکون‌کاف»‬
                                                               ‫ورد‬
                                                                 ‫پودنةٌ بری باشد که ا کر کوسفند امزخآن‬
‫یریانج ‪ -‬بکر اول و ثائی بتحتانی‬
‫رسیده وبای ابجد بالف کشیده ولون‌مفتوح بجیم‬                    ‫ومشکطرامشیز نیز گوبند و بعربی بقلة‌الفزال‬
  ‫ضی‬
   ‫حو‬‫زده » نوعی از سرطان بحری باشد ‪ ۴‬؛‬                                                                    ‫خوانند ‪.‬‬
 ‫کویند سنگی است مانند سرطان و دارروهای‬                       ‫ر ‪ » 4‬باول وثانیمفتوح » باردرختی‬
                                   ‫چشم بکار برند ‪.‬‬            ‫کوچکت از آن‌وساه‬     ‫است درهتد شببه‌بفندق اما‬



                                                 ‫ان پنحم‬


                            ‫ج‬
‫راك ‪ » ۱‬بروزن کجك‪ .‬بمعنی رجنك‬                                 ‫راق ‪ -‬بفتع‌اول بروزن طواف ‪.‬آواز‬
                                                                                            ‫ج‬
‫است که آروغ باشد » وبضم جیم فلرسی هم باین‬                                        ‫وصدبای کوس و لقاره را گوند ‪۰‬‬

              
==== leaf 400
    ‫سس‬                                                                                                      ‫رجوعام‬
 ‫ا او ماندند»‬   ‫تف و دوسہط‬    ‫سر دسل‬   ‫از مطاوعش‬        ‫رونك‬   ‫حمام‬   ‫ددوارهای‬     ‫و‬    ‫زم اه‬   ‫زعمن‬   ‫در‬   ‫که‬   ‫است‬


 ‫وسبط بکسر اول در عربی گروه وقبیله و فرزند‬              ‫صر دهد »‬          ‫أحنلای‬       ‫و شر‬      ‫مخورند‬          ‫وا‬

‫زاده گروابند؛ ورجوعا بحذف میم هم‌بنظر ا مده‬                                            ‫وبعربی خرفه رگاویند ‪.‬‬
                                                        ‫جروعام" ‪ -‬بفتح‌اول وثانی‌بواورسیده‬
                                           ‫‪.‬‬   ‫است‬

 ‫رجه ‪ - ۴‬بفتح اول وانی ‪ ۰‬طنابی‌باشد‬                    ‫می‌نقطه ( ‪ )۱‬بالف کشیده ویمیم زده » بلفت‬                  ‫رعن‬

‫کجهامه و لنکی و چیزهای دیگر بربالای آن‬                  ‫سربانی نام پسر سلیمان علیه‌اللام است » چون‬
                                       ‫انداز ید ‪.‬٭‬      ‫ولیمهد پدر شدیسیب هوا و وی بسیار ده سبط‬


                                               ‫سان ششم‬     ‫ص‬




     ‫ووو لغت و کنات‬              ‫در رای بی نقطه باخای نقطه دار مشتمل بر ست‬

 ‫ديهم هم هت که تاج بادشاهان باشد ‪ -‬وسوی‬
                                                        ‫رخ = بفتح ارل وسکون انی » بمعنی‬
 ‫وطرف وجاب رایز گفته‌الس وکنایماهی است ‪۷‬‬                 ‫شکاف‌ررخنه وچاك ‪ -۴‬وغ‌ونصه واندوه‌باشد؟ ‪-‬‬
                                                         ‫ول‪ ,‬رخاره و روی رگاونند ویعربی خد‬
                                                                                         ‫و باضم‬
                             ‫وخربزه بدان آویزند ‪.‬‬      ‫خوانند ‪ - 6‬ولام جانوریت که اولیز مانند عنقا‬
 ‫رخام = س اول بورزن غلام » نوعی‬                         ‫در خارح وجود ندارد و آنچه کویند که فيل‬
 ‫از منک است‪ ۰ ۸‬وآن زردوسفید وسرخ میباشد‬                  ‫وکر کدن رطاعمهٌ بجهای خود میکند غلط‬
 ‫و بپترین آن سفید است » و گوبند بفایت صلب‬                ‫ودروغ است‪ - ۱‬و بك مپره از مهرهای شطرلج‬
 ‫‏‪57 ۷ i‬‬                                               ‫بنام اوموسوم است » و بسضی گویندباین معنی‬
                                                         ‫عربی است ‪ -‬وعنان اسب رالیز گویند ‪ -‬ویمعنی‬
                      ‫میشود گووبند عربی است ‪.‬‬
                                                                          ‫‪.‬‬   ‫‪ - :‬بی‌شطه‬        ‫(‪ )۱‬چك‬



         ‫شو‬
        ‫ین‬     ‫» عبری ( کیکه قوم را وسمت مردهد ) ‪.‬‬
             ‫جوی‬
           ‫اپر‬                                                                           ‫‪ ۱‬ر‬
                                              
==== leaf 401
 ‫رخش‬                                                                                             ‫~‪t‬‬


                             ‫مرده را نز گفته‌اند‬         ‫رخبین ‪ » ۷‬اول وبای‌ابجد بتحتالی‬
‫کنابه ازمقیم‌شدن‬        ‫رحت افکندن‬                       ‫رسیده بروزن خرجین » دوغ ترش سخت نشدمرا‬
                           ‫_ وعاجز آمدن باشد ‪.‬‬            ‫گوبند» وبعضی کوبند چیزست کهآ ترا اکزشك‬
                                                         ‫آوردوشیرسازند وترش مزه باشد مانند قراقروت‬
‫رحت بلرست ک=نابه ازسفر کردن‪.‬‬
                                                         ‫ترش سخت شده همچو‬           ‫غ‬
                                                                                    ‫‪-‬و‬‫ددو‬
                                                                                        ‫سياه رنگه بو‬
                                    ‫ومردن باشث ‪.۰‬‬
                                                         ‫پنیر را گنفزته‌اند ؛ وبکراود هم‌آمده است»‬
‫شی!دن ه کنابه از‬
               ‫کحر‬
                 ‫خت بص‬
                     ‫ر‬                                   ‫وبعضی گوبند هرچیز که آنرا ازدوغ ترش سازند‬
                ‫مردن باشد که سفر آخرت است ‪.‬‬                                      ‫رخبین ورخبینه خوالند ‪.‬‬

‫خت لستی» کنابهاز سفر کردن دیا‬
                            ‫ر‬                            ‫رخیینه ‪ = ۴‬بنماول‪,‬بمعنیآخررخیین‬
                                                         ‫است وآن هرچیز باشد که از دوغ ترش سازند‪-‬‬
                                    ‫وخرت است ‪۰‬‬
                                             ‫آ‬
                                                                        ‫و مخ صنویر را نز گفته‌اند ‪۱‬‬
‫رحج ‪ = ۱‬بضم‌اول وسکون ثالی وجیم‪.‬‬
                                                         ‫ر خت ‪ -‬بنتح اول بروزن سخت‪ .‬بمعنی‬
                   ‫تام ناحبه‌است ازنواحی بست ‪.‬‬           ‫راست ودرست باشد‪ -‬ویمعتی اسب همآمده است‬
‫ر حش ‪٣‬‏ بفتحاول وسکون‌ئالی وشین‬                          ‫که بعربی فرس خوالند ‪ - ۴‬وپوشیدلی واسباب‬
‫نقطه دار )‪ ۱‬رىگ سرج و سقمد درهم آمیشته‬                   ‫خانه ‪ ۴‬وبار وبنه وسامان‌رانیز گوبند وبمعنی‬
‫باشد» وبعضی گوبند رنگی‌است میان سیاه وبور‪-‬‬               ‫غم وغصه واندوه هم هت ‪ -‬وطعام وخورش‌بك‬

                                                                     ‫دار ‪۰‬‬    ‫قطه‬   ‫‪+‬‬   ‫جك‬   ‫)‪۱‬‬




 ‫ج‬     ‫‪ ۱۷‬نآ‌برمم نسخر نفخرو « یزد‬              ‫ص‪۲‬‬   ‫‪) petit‬رف( كل«‬      ‫—=‪lait acide‬‬         ‫‏‪۱‬‬

   ‫و‪٩۹۱۵‬‏ ‪ :‬رخبین؛کبح «السامی»؛ ترف سرخ م هذن الماء؟» قره فروت «مسر الحواهر»‬
```


## [2026-09-14T01:15:42.063Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\ntr=str.maketrans('۰۱۲۳۴۵۶۷۸۹','0123456789')\nhits=[]\nfor i,p in enumerate(pages):\n    s=p.translate(tr)\n    head=s[:120]; tail=s[-120:]\n    for m in re.findall(r'\\b(\\d{3})\\b', head+' '+tail):\n        n=int(m)\n        if 500<=n<=1300:\n            hits.append((i,n,n-i))\nfor h in hits[:80]:\n    print(h)\nEOF",
 "description": "Fit BQT v2 leaf-to-page offset"
}
```


### [2026-09-14T01:15:43.759Z] TOOL RESULT

```
(14, 705, 691)
(16, 900, 884)
(17, 531, 514)
(20, 792, 772)
(27, 649, 622)
(32, 692, 660)
(32, 575, 543)
(36, 870, 834)
(37, 981, 944)
(44, 891, 847)
(57, 644, 587)
(76, 919, 843)
(84, 991, 907)
(84, 729, 645)
(91, 639, 548)
(106, 949, 843)
(119, 771, 652)
(121, 882, 761)
(126, 911, 785)
(133, 591, 458)
(133, 979, 846)
(147, 912, 765)
(158, 722, 564)
(162, 705, 543)
(170, 971, 801)
(174, 719, 545)
(177, 801, 624)
(183, 927, 744)
(186, 927, 741)
(189, 731, 542)
(194, 739, 545)
(195, 703, 508)
(196, 925, 729)
(197, 763, 566)
(208, 780, 572)
(208, 884, 676)
(212, 557, 345)
(214, 980, 766)
(215, 701, 486)
(217, 930, 713)
(230, 959, 729)
(234, 777, 543)
(243, 987, 744)
(244, 728, 484)
(252, 661, 409)
(253, 793, 540)
(254, 597, 343)
(257, 897, 640)
(258, 712, 454)
(258, 501, 243)
(259, 711, 452)
(267, 916, 649)
(274, 701, 427)
(276, 521, 245)
(277, 930, 653)
(280, 982, 702)
(281, 891, 610)
(282, 590, 308)
(282, 801, 519)
(290, 501, 211)
(296, 953, 657)
(298, 938, 640)
(302, 881, 579)
(303, 701, 398)
(303, 868, 565)
(307, 930, 623)
(308, 759, 451)
(308, 988, 680)
(314, 558, 244)
(324, 618, 294)
(325, 731, 406)
(340, 733, 393)
(354, 711, 357)
(355, 998, 643)
(357, 898, 541)
(362, 671, 309)
(362, 985, 623)
(362, 811, 449)
(364, 509, 145)
(365, 531, 166)
```


## [2026-09-14T01:15:55.820Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'ریال' in p:\n        print('leaf',i, [l for l in p.split('\\n') if 'ریال' in l][:4])\nprint('---rast---')\nfor i,p in enumerate(pages[380:400],380):\n    if 'راست' in p[:600]:\n        print('leaf',i, repr(p[:80]))\nEOF",
 "description": "Find riyal and rast in BQT v2"
}
```


### [2026-09-14T01:15:57.010Z] TOOL RESULT

```
leaf 142 ['\u202bسموم\u200cقتاله است\u202a.\u202c\u202c                                             \u202bای بالف کده » بلغت سریالی\u200cلوعی ازسوسمار\u202c']
leaf 164 ['                                                                                          \u202bآرا بریالی حربا\u202c']
leaf 245 [' \u202bبافت سریالی نام دبوی است از جملة شیاطین \u202a-\u202c\u202c               \u202bبرناد که از بندی که در یشاب\u202c     \u202bومی\u202c']
leaf 324 ['      \u202bسامیهس \u202a:»۷۲۲\u202c\u202c                  \u202bباشد«معمجمیات عرسه\u202c            \u202bواردعر می وسریالی\u202a :\u202cله\u202c       \u202bفارسی «رسکره \u202a 6\u202cحاخود و ازاا\u202c']
leaf 371 ['   \u202b\u202a = ۴\u202cدور » طبری \u202a( ۲114\u202cدور) «ساب\u202c                          \u202b\u202a( - ۱\u202cعی) ازسریالی «دائرةالمعارف اسلام» \u202a.\u202c\u202c']
leaf 447 ['   \u202b* ریال \u202a -\u202cبکسر اول \u202a .\u202cاصلا اسپانیابی \u202a 148\u202cبه\u200cمنی لغوی شاهی (فراسوی [\u202a,)20۲\u202c\u202c']
leaf 597 [' \u202b\u202a #\u202cسریالی \u202a -\u202cبضم اول » منوب بسورستان ( عراق وبلاد شام ) « ممجم البلدان » \u202a .\u202cنام\u202a\u200e\u202c\u202c', ' \u202b\u202aN5115\u202c\u202c   \u202bبپتر و روشنتر شد \u202a .\u202cدیگر از مراکز مهم سریالی\u202a ,\u202cشهر روحانی عیسوبان شرقی\u202a .\u202cصبین\u202a\u200e\u202c\u202c']
---rast---
leaf 384 '    \u202b\u202a۷\u202c\u202c                                                                       '
leaf 387 '   \u202bراست\u202c                                                                       '
leaf 388 ' \u202b”\u202a~A\u202c\u202c                                                                        '
leaf 389 '                                                                                '
```


## [2026-09-14T01:16:07.372Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\np=pages[447]\nimport re\nidx=p.find('ریال')\nprint(p[max(0,idx-1200):idx+1500])\nEOF",
 "description": "Print BQT riyal entry context"
}
```


### [2026-09-14T01:16:08.573Z] TOOL RESULT

```
هوشمان ‪.۷۳۱‬‬          ‫‪۴‬‬        ‫‪ - ۱‬از ‪ :‬ره (راء) ‪ +‬ی (نبت)‪.‬‬
   ‫‪.‬وبنده با نویسنده دقردیم‬
                          ‫طرلاح امروز گ‬
                                      ‫صد‬‫‪ - ۴‬مراد ( اینجاب ) و (بنده) ااست‬
                                                        ‫از خود بلفظ (رهی) تعبیر میکردند ‪:‬‬
           ‫بپرهیزی از درد سر وزگرالی»‬                  ‫اگرچهرهی را ت کومتر لوازی‬
          ‫خودیربرالی ‪.‬‬     ‫دزست‬
                              ‫اگرچند ا‬                 ‫منبدون‌چوبازم کهزیتوشتابم‬
  ‫«منوچپری دامغاتی ‪٩٩‬‏ »‪.‬‬
                ‫از ‪ :‬ره (یدن یوند مصدری) = رستن (بفتح اول) (ه م‪) .‬‬               ‫‪۴‬‬
  ‫‪ - 6‬بارسی باستان ‪ 882 -‬اوستا ‪ 80188‬بونانی ‪ 81883۰‬سریانی» ارمنی‬
   ‫‪۵‬‏ “‪ « Rai 821.12۳ 12۳ ,ql‬اسفا ‪۲ :۱‬ص‪ .*۸۳‬دراوستالا‪)il 27[َ6‬‏ ‪)۹۱۰۸۱‬‬
  ‫با جزء آخربمعنی درجاب ری‌آمده ومحتملا بخطه وناحيةٌ مزبور اطلاق میشده " در پارسی ماله‬
  ‫‪htiB‬‬    ‫‏‪ RAj - Îk‬ا‪,‬رمنی ‪kihzaR‬‏ ‪67801221 .ıl xêzaR. énêkazaR. ,yy .‬‬
   ‫(ابالت)؛پارسی جدید «رازی»‪ .‬رك‪ :‬مار کوارت‪ .‬ابرانشهرص‪۲۲۱‬؛مار کوارت‪ .‬شهرستانهایابراشهر‪.‬‬
                                      ‫‪ ۱‬لاننتی ‪ 6561‬فرانه‪( 10۳‬یادشاه)‪.‬‬         ‫ص‪.۱ ۲۱‬‬

   ‫* ریال ‪ -‬بکسر اول ‪ .‬اصلا اسپانیابی ‪ 148‬به‌منی لغوی شاهی (فراسوی [‪,)20۲‬‬
  ‫وآن بمکوکات لقره اطلاق همشد معر ب آن‌هم رمال ‪٩‬‏ نفس؟‪ .‬این‌کلمه از زمان تلط اسیالیاییان‬

  ‫‪ | .‬کنون واحد دول فقرة‬    ‫و يرتقالان در خلیج فلری ومر اودةٌ اشان ا ابرایان وارد فارسی شده‬

                                 ‫اران معادل صدوینار ‏ يكقران ت عثر بلك تومان است ‪.‬‬
```


## [2026-09-14T01:16:24.232Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"reg-1\\|reg-\\. To move in a straight line\\|rex, king\\|maharaja\" AHD_watkins1985.txt | head -20",
 "description": "Grep Watkins AHD for reg-"
}
```


### [2026-09-14T01:16:24.294Z] TOOL RESULT

```
1208:ABAFT apo- ABANDON bha-2 ABASE bassus ABASH bat- ABASIA gWa- ABATE battuere ABBREVIATE mregh-u- ABDICATE deik- ABDUCENS deuk- ABDUCT deuk- ABELE albho- ABERRATION ers-1 ABET bheid- ABEYANCE bat- ABHOR ghers- ABIDE bheidh- ABJECT yé- ABJURE yewes- ABLATION  tele- ABLAUT apo-, kleu-1 ABLE ghabh- ABLUTION leu(@)- ABNEGATE ne ABNORMAL gné- ABODE bheidh- ABOLISH al-3 ABORT er-! ABOUND wed-1 ABOUT ud- ABOVE upo ABRADE réd- ABRIDGE mregh-u- ABROGATE reg-1 ABROSIA gWere-4 ABRUPT reup- ABSCESS ked- ABSCISE kae-id- ABSCOND dhé-1 ABSENT eS- ABSOLUTE leu-1 ABSOLVE feu-1 ABSORB srebh- ABSTAIN ten- ABSTRACT tragh- ABSTRUSE treud- ABSURD swer-2 ABULIA gWele-1 ABUT bhau- ABYSS gWadh- ACANTHO- ak- ACANTHOPTERYGIAN pet- ACANTHUS ak- ACAPNIA kwép- ACCEDE ked- ACCELERATE kel-3 ACCENT kan- ACCEPT kap- ACCESS ked- ACCIDENT kad- ACCIPITER Oku- ACCLAIM kele-2 ACCLIVITY klel- ACCOLADE kwel-1 ACCOMMODATE med- ACCOMPLISH pele-1 ACCORD kerd-1 accosT kost- ACCOUNT peu- ACCRUE_ ker-3 ACCUMBENT keu-2 ACCUMULATE keue-2 ACCURATE cira ACERATE ak- ACERB ak- ACETABULUM ak- ACETIC ak- ACETUM = ak- ACHALASIA ghé-
1246:ANILE an-! ANILINGUS 4no-, leigh- ANIMA ane ANIMADVERT ane- ANIMAL ane- ANIMATE ane ANIMATO ane- ANIMISM ane- ANIMOSITY ane- ANIMUS ane- ANION ei-1 ANISEIKONIA weik-3 ANKLE ank- ANKYLOSIS ank- ANLAGE an}, legh- ANNALS at- ANNEAL aidh- ANNEX ned- ANNIHILATE ne ANNIVERSARY at-, wer-3 ANNOTATE gno- ANNOUNCE neu-! ANNOY od-2 ANNUAL at ANNUITY at- ANNUL ne ANNULAR 4no- ANNULET 4no- ANNULUS 4no- ANODE sed-2 ANODYNE ed- ANOINT ong¥- ANOMALOUS sem-! ANOMIE nem- ANON ol-no- ANONYMOUS né-men- ANOPHELES obhel- ANORECTIC reg-1 ANOREXIA reg-1 ANORTHITE wrddh- ANOSMIA od-! ANSATE ans- ANSERINE ghans- ANSWER swer-1 ANT mai-1
1260:ARMADILLO = ar- ARMATURE ar- ARMIGER gerere ARMILLARY SPHERE al- ARMISTICE sta- ARMOIRE ar- ARMY ar- ARPENT pert ARRAIGN  ar- ARRANGE sker-3 ARRAY reidh- ARREARS re- ARREST sta- ARRIERE-BAN koro- ARRIVE rei-1 ARROGATE reg-1 ARROW arku- ARSENIC ghel-2 ARSIS wer-2 ARSON as-
1473:ERGO reg-1 ERGOGRAPH werg- ERNE or-
1682:INTER en, ters- INTERCALATE kela-2 INTERCEDE ked- INTERCEPT kap- INTERCOSTAL kost- INTERCOURSE kers-2 INTERDICT deik- INTEREST es- INTERIM en INTERIOR en INTERJECT yé- INTERLOCUTION  tolkw- INTERLOPE klou- INTERLUDE leid- INTERMEDIATE medhyo- INTERMIT (S)meit(a)- INTERNAL en INTERNECINE nek-1 INTERPELLATE pel-6 INTERPOSE apo- INTERPRET per-68 INTERREX reg-1 INTERROGATE reg-1 INTERRUPT reup- INTERSECT sek- INTERSPERSE (s)preg- INTERSTICE sta- INTERVAL walso- INTERVENE gWa- INTERVIEW weid- INTESTINE en INTIMA en INTIMATE? en INTINCTION  teng- INTINE en
2129:PRECINCT kenk-! PRECIOUS per-6 PRECIPITATE kaput PRECISE kae-id- PRECLUDE kleu-3 PRECOCIOUS pekw- PRECURSOR kers-2 PREDATORY ghend- PREDECESSOR ked- PREDICATE delk- pRepicT deik- PREDOMINATE deme-1 PREEMPTION em- PREFACE bha-2 PREFECT dhé-1 PREFER bher-1 PREFIGURE dheigh- PREFIX dhig¥- PREGNABLE ghend- PREGNANT! gene- PREGNANT? per-5 PREHENSILE ghend- PREHENSION ghend- PREJUDICE deik-, yewes- PRELAPSARIAN leb-1 PRELATE telo- PRELECT leg-1 PRELIBATION [éi- PRELUDE leld- PREMATURE ma-1 PREMIER per! PREMISE (s)meit(@)- PREMIUM em- PREMONITION men-1 PREMORSE mer-2 PREMUNITION mel-3 PREPARE pere-! PREPENSE (s)pen- PREPONDERATE (S)pen- PREPOSITION apo- PREPOSTEROUS apo- PREPOTENT _poti- PREPUCE pu-! PREROGATIVE reg-1 PRESAGE sag- PRESBYOPIA per! PRESBYTER pert PRESCIENT skel- PRESCIND  skel- PRESCRIBE skribh- PRESENT! es- PRESENT? es- PRESENTIMENT sent- PRESERVE ser-! PRESIDE sed-! PRESS! per-5 PRESSURE per-5 PRESTIGE streig- PRESUME em- PRETEND ten- PRETERIT el-1!, per? PRETERMIT (s)melt(@)- PRETEXT teks- PRETZEL mregh-u- PREVAIL wal- PREVENIENT gWa- PREVENT gWa- PREVIOUS wegh- PREVISE weld- PREY ghend- PRICE per-6
2136:PRO-2 per? PROBABLE per! PROBE pert PROBITY per! PROBLEM gWele-1 PROBOSCIS g¥6- PROCEED ked- PROCLAIM kele-2 PROcLITIC § klei- PROCLIVITY klei- PROCREATE ker-3 PROCTITIS prdkto- PROCTOLOGY prdkto- PROCTOR cura PROCTOSCOPE prdkto- PROCUMBENT keu-2 PROCURATOR cura PROCURE cura PROCYON kwon- PRODIGAL ag- PRODIGY ég- PRODROME der-1 PRODUCE deuk- PROFANE dhés- PROFESS bha-2 PROFESSOR reg-! PROFFER bher-1 PROFICIENT dhé-1 PROFILE gWhi- PROFIT dhé-1 PROFLIGATE bhiig- PROFOUND bhudh- PROFUSE gheu- PROGENITOR gene- PROGENY gene- PROGLOTTID glégh- PROGNOSIS gnd- PROGRAM gerbh- PROGRESS ghredh- PROHIBIT ghabh- PROJECT yée- PROLAN al-3 PROLAPSE leb-1 PROLATE tele- PROLEGOMENON leg-! PROLEPSIS (s)lag¥- PROLETARIAN al-3 PROLIFEROUS _al-3 PROLIFIC al-3 PROLIX wleik- PROLOCUTOR tolkw- PROLOGUE leg-1 PROLONG del-1 PROLUSION leid- PROMENADE men-2 PROMINENT men-2 PROMISCUOUS meik- PROMISE (s)meit(e)- PROMOTE meue- PROMPT em- PRONE per! PRONEPHROS _ negwh-ro- PRONOUN no-men- PRONOUNCE neu-! PROOF per! PROPAGATE pag- PROPEL pel-6 PROPEND (8)pen- PROPER pert PROPERTY per? PROPHET bha-2 PROPHYLACTIC phulax PROPINQUITY per? PROPIONIC ACID peie- PROPITIOUS pet- PROPOLIS pele-3 PROPORTION pere-2 PROPOSE apo- PROPRIOCEPTION per! PROPRIOCEPTOR per? PROPTOSIS pet- PROPYLAEUM pulé PROPYLON pulé PROROGUE reg-1 PROS- pert PROSCRIBE skribh- PROSE wer-3 PROSECUTE sekw-1 PROSELYTE leudh-1 PROSOMA teue- PROSOPOPEIA kWwel-2, per! PROSPECT spek- PROSPER spé-1 PROSTATE sta- PROSTHESIS dhé-1 PROSTITUTE sta- PROSTOMIUM ste-men-
2160:RABBET battuere RABBLE? reu-2 RABID rebh-1 RABIES rebh-1 RACE? ers-1 RACES wrad- RACHIS wragh- RACK! reg-1 RACK3 wreg- RACLETTE réd- RADDLE! reidh- RADICAL wrad- RADICLE wrad- RADIOSONDE swem- RADISH wrad- RADIX wrad- RADULA réd- RAFT! rép-2 RAFTER rép-2 RAG! reu-2 RAGA reg-3 RAGE rebh-1 RAGOUT geus- RAID reidh- RAIL! reg-1 RAIN reg-2 RAINBOW reg-2 RAISE risan RAJ reg-1 RAJAH_ reg-! RAKE! reg-1 RALLENTANDO lento- RALLY leig-1 RAMBUNCTIOUS reudh-1 RAMEKIN reugh-men- RAMIFY wrad- RAMOSE wrad- RAMP2  skerbh- RAMPART pere-1 RAMPION rap- RAMSON krem- RAMUS wrad- RANCH sker-3 RANGE sker-3 RANI reg-1 RANK!  sker-3 RANK? reg-1 RANKLE derk- RANSACK sag- RANSOM em- RAPACIOUS rep- RAPE! rep- RAPE? rap- RAPHE wer-3 RAPHIDE wer-3 RAPID rep- RAPPORT per-2 RAPPROCHEMENT per! RAPT rep- RARE! era-2
2169:REAL? reg-1
2174:REBUT bhau- RECALESCENCE kele-! RECANT kan- RECAPITULATE kaput RECEDE ked- RECEIVE kap- RECENSION kens- RECENT ken-3 RECIDIVISM kad- RECIPROCAL pert RECISION kae-id- RECK reg-1 RECKLESS reg-! RECKON reg-1 RECLAIM kele-2 RECLINE klei- RECLUSE kleu-3 RECOGNIZE gnd- RECOIL (s)keu- RECOMMEND man-2 RECONDITE dhé-1 RECORD kerd-1 RECOURSE kers-2 RECOVER kap- RECREANT kerd-1 RECREMENT krei- RECRIMINATE  krei- RECRUDESCE kreud-! RECRUIT ker-3 RECTANGLE reg-1 RECTIFY dhé-1, reg-1 RECTILINEAR reg-1 RECTITUDE reg-!
2175:RECTUM reg-1 RECUMBENT keu-2 RECUPERATE kap- RECUR kers-2 RED reudh-1 REDE ar- REDEEM em- REDEMPTION em- REDOLENT od-1 REDOUBT deuk- REDOUBTABLE dwo- REDOUND wed-! REDSTART ster-1 REDUCE deuk- REDUNDANT wed-1 REDUVIID eu-! REED kreut- REEF! = rebh-2 REEF? rebh-2 REEK reug- REEL! krek-1 REFECT dhé-1 REFECTORY dhé-1 REFER bher-! REFLUX bhieu- REFRACT bhreg- REFRAIN! ghrendh-
2177:REFRAIN? bhreg- REFRIGERATE Srig- REFRINGENT bhreg- REFUGE bheug-! REFULGENT bhel-1 REFUND! gheu- REFUSE! gheu- REFUSE? gheu- REFUTE bhau- REGAL reg-! REGENT reg-1 REGICIDE reg-1 REGIME reg-? REGIMENT reg-1 REGION reg-! REGISTER gerere REGIUS reg-! REGLET reg-1 REGOLITH reg-3 REGRATE grat- REGRESS ghredh- REGULAR reg-! REGULATE reg-1 REGULUS reg-! REGURGITATE gWere-4 REIFY ré-
2184:RICH reg-1 RICOTTA pekw-
2190:RIG reig-1 RIGATONI rei-1 RIGHT reg-! RIGID reig-2 RIGOR reig-2 Ric-VEDA erkw-, weid- RIKsMaL_ méd-, reg-1 RILL  rei-3 RIMOSE rei-1 RIMPLE skerbh- RIND rendh- RINDERPEST ker-1 RING!  sker-3 RING2 ker-2 RINGHALS kWel-1, sker-3 RINK sker-3
2192:RIP! reup- RIPARIAN rei-1 RIPE rej-1 RIPPLE? rei-1 RISE isan RISORGIMENTO reg-1 RISSOLE reudh-1 RITE ar-
2198:ROE! krek-2 ROE? rei-2 ROGATION reg-1 ROGATORY reg-1 ROLL ret- ROLLMOPS mul- ROOD rét-
2205:RYE! wrughyo- RYE? reg-1
2323:sTuD2 sta- STUDENT (s)teu- sTUDY (s)teu- STULTIFY _ stel- sTUM stam- STUMBLE stam- STUMP stebh- STUN (s)tena- STUPA steu(@)- STUPE steu(9)- STUPEFY (s)teu- STUPENDOUS (s)teu- STUPID (s)teu- STURDY trozdo- STUTTER (s)teu- stTy2  steigh- STYLITE sta- STYLOBATE gWa-, sta- STYPTIC steu(@)- Styx (s)teu- SUASION swad- SUAVE swad- SUB- upo SUBALTERN al-1 SUBAUDITION au-5 SUBDUCTION deuk- SUBDUE deuk- SUBITO ei-! SUBJACENT yé- SUBJECT yé- SUBJOIN yeug- SUBJUGATE yeug- SUBLUNARY leuk- SUBMERGE mezg-! SUBMIT (s)meit(9)- SUBORDINATE ar- SUBORN ar- SUBPOENA kwei-1 SUBREPTION rép-1 SUBROGATE reg-1 SUBSCRIBE skribh- SUBSEQUENT sekw-1 SUBSIDE sed-1 SUBSIDY sed-1 sUBSIST sta- SUBSTANCE sta- SUBSTITUTE sta- SUBSTRATUM ster-2 SUBSTRUCTION | ster-2 SUBSUME em- SUBTEND ten- SUBTERFUGE bheug-', upo SUBTERRANEAN ters- SUBTLE teks- SUBTRACT tragh- SUBULATE syU- SUBVENTION gWa- SUBVERT wer-3 SUCCEED ked- succincT kenk-1 succor kers-2 succuBUS keu-2 SUCCULENT seud-2 SUCCUMB keu-2 SUCCUSSION kwét- SUCH swo-
```


## [2026-09-14T01:16:30.944Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^reg-1\\|reg-1\\. To move in\\|reg-!\\. To move\" AHD_watkins1985.txt | head; grep -n \"rectus\\|regere\\|maharajah\\|Sanskrit raj-\" AHD_watkins1985.txt | head -20",
 "description": "Find Watkins reg-1 entry"
}
```


### [2026-09-14T01:16:31.019Z] TOOL RESULT

```
893:culdre, to rake, in Provengal rasclar (> French racler), to rake, scrape: RACLETTE. [Pok. 2. réd- 854.] reg-'. To move in a straight line, with derivatives mean- ing “to direct in a straight line, lead, rule.” I. Basic form *reg-. 1. Suffixed form *reg-to- in Germanic *rehtaz in Old English riht, right, just, correct, straight: RIGHT. 2. Latin regere, to lead straight, guide, rule (past partici- ple réctus, hence adjective réctus, right, straight): REALM, RECTITUDE, RECTO, RECTOR, RECTUM, REGENT, REGIME, REGIMENT, REGION; CORRECT, DIRECT, ERECT, RECTANGLE, RECTIFY, RECTILINEAR, RISORGIMENTO, SURGE. 3. Greek oregein (with prothetic vowel from oldest root form *sreg-), to stretch out, reach out for: ANORECTIC, ANOREXIA. II. Lengthened-grade form *rég-, Indo-European word for a tribal king. 1. Celtic suffixed form *rig-yo- in Germanic *rikja- in: a. Old English rice, realm: BISHOPRIC; b. Old Norse riki (> Norwegian rik), realm: RIKSMAL; c. Old English rice, strong, powerful: RICH. 2. Latin réx, king (royal and priestly title): REAL, REGAL, REGULUS, REIGN, ROYAL; INTERREX, REGICIDE, REGIUS PROFESSOR, VICEREINE, VICEROY. 3. Suffixed form *rég-en- in Sanskrit raja, rdjan-, king, rajah (femi- nine rdjni, queen, rani), and rdjati, he rules: RAJ, RAJAH, (RANI), (RYE2); MAHARAJAH, MAHARANTI. III. Suffixed lengthened-grade form *rég-old in Latin régula, straight piece of wood, rod: RAIL!, REGLET, REGULAR, REGULATE, RULE, IV. O-grade form *rog-. 1. Germanic *rak6 in Old English raca, racu, rake (implement with straight pieces of wood): RAKE!, 2,Germanic *rak- in Middle Dutch rakke, framework: RACK}, 3. Possibly Germanic *rankaz (with nasal infix) in Old English ranc, straight, strong, hence haughty, overbearing: RANK?. 4, Germanic *rak- inaz, ready, straightforward, in Old English gerecenian, to arrange in order, recount (ge-, collective prefix; see kom): RECKON. 5. Suffixed form *rog-d- in Latin rogdare, to ask (< “stretch out the hand”): ROGATION, ROGATORY; ABROGATE, ARROGATE, CORVEE, DEROGATE, INTERRO- GATE, PREROGATIVE, PROROGUE, SUBROGATE, SUPERER- ocaTE. 6. Suffixed form *rog-o- in a possible Latin noun *rogus, “extension, direction,” perhaps in a Latin phrase *é rogd, “from the direction of” (€ < ex, out of; see eghs), contracted into ergd, therefore, in consequence of: ARGAL, ERGO. V. Lengthened o-grade form *rég-. 1. Ger- manic *rdkjan in Old English rec(c)an, to pay attention to, take care (formally influenced by Old English reccan, to extend, stretch out, from Germanic *rakjan): RECK. 2. Germanic *rdékja- in Old English receléas, careless (-léas, lacking; see leu-1):; RECKLESS. [Pok. 1. reg- 854.] reg-2. Moist. 1. Suffixed variant form *rek-no- in Ger- manic *regnaz, rain, in Old English reg(e)n, rén, rain: RAIN; RAINBOW. 2. Possibly Latin rigdre, to wet, water: IRRIGATE. [Pok. 2. reg- 857.] reg-3. To dye. Lengthened-grade form *rég-. 1. Suffixed form *rég-és- in Greek rhégos, blanket, rug: REGOLITH. 2. Sanskrit rdgah, color, red: RAGA. 3. Perhaps Sanskrit raékshd, earlier form of lékshd, red dye: Lac}. [Pok. 1. reg- 854.] regv-es-. Darkness. Oldest root form *areg’-es-. Greek Erebos (with prothetic vowel), Erebus, a place of dark- ness under the earth: EREBUS. [Pok. regt-os- 857.] rei-1, To scratch, tear, cut. I. Extended form ‘reik-. 1. Germanic *rigon- in Italian riga, line (< “something cut out’’): RIGATONI. 2. Suffixed form *rei-md or *reig-sma in Latin rima, crack, cleft, fissure: RIMOSE. 3. Suffixed o-grade form *roik-wo- in Germanic *rai(h)-wa- in Old English raw, réw, a line, row: ROW!. II. Possible extended form *reipp-. Germanic *raipaz, rope, in: a. Old English rap, rope: ROPE; b. compound *stig-raipaz, “‘mount-rope,” in Old English stigrap, stirrup (see steigh-). III. Extended form *reip-. 1. Ger- manic *rifan, in Old Norse rifa, to tear: RIVE. 2. Zero-grade form *rip- in: a. Germanic *77fti- in Danish rift, breach, akin to the Scandinavian source of Middle English rift, rift: R1FT!; b. Germanic *rif- in Old English
```


## [2026-09-14T01:16:43.016Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o \"DRESS [a-z0-9ë*-]*\\|ADDRESS [a-z0-9ë*-]*\\|ESCORT [a-z0-9ë*-]*\\|SOURCE [a-z0-9ë*-]*\\|SURGE [a-z0-9ë*-]*\\|MAHARAJAH [a-z0-9ë*-]*\" AHD_watkins1985.txt | sort -u | head -20",
 "description": "Check Watkins index for dress/address/escort/source"
}
```


### [2026-09-14T01:16:43.079Z] TOOL RESULT

```
MAHARAJAH meg-
SURGE reg-
```


## [2026-09-14T01:16:46.183Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -on \"DRESS[^ ]* [a-zA-Z0-9ë*()-]*\\|ADDRESS [a-zA-Z0-9ë*()-]*\\|ESCORT [a-zA-Z0-9ë*()-]*\\|SOURCE [a-zA-Z0-9ë*()-]*\" AHD_watkins1985.txt | head -20",
 "description": "Grep Watkins index entries again"
}
```


### [2026-09-14T01:16:46.249Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:16:48.772Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"DRESS\\|ESCORT\\|SOURCE\" AHD_watkins1985.txt | cut -c1-300 | head -10",
 "description": "Locate DRESS/ESCORT/SOURCE in Watkins"
}
```


### [2026-09-14T01:16:48.829Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:16:54.118Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"escort,\" \"address,\" \"dress,\" \"source,\" \"regime,\" \"real,\" \"royal,\"; do echo \"### $w\"; grep -n -m2 -i \"^$w\\| $w n\\.\\|^ *$w\" KLN_1966.txt | cut -c1-600; done",
 "description": "Grep Klein for Romance words"
}
```


### [2026-09-14T01:16:55.312Z] TOOL RESULT

```
### escort,
### address,
### dress,
12258:dress,  tr.  and  intr.  v.  —  ME.  dressen,  ‘to  direct, prepare;  to  dress’,  fr.  OF.  (=  F.)  dresser,  fr. VL.  *directiare,  fr.  L.  directus,  pp.  of  dirigere, ‘to  put  into  a  straight  line;  to  direct,  guide’.  See direct,  v.,  and  cp.  words  there  referred  to. Derivatives:  dress,  n.,  dresser  (q.v.),  dress-ing, n.,  dress-y,  adj.,  dress-i-ly,  adv.,  dress-i-ness,  n. dresser,  n.,  one  who  dresses.  —  Formed  fr.  dress, v.,  with  agential  suff.  -er. dresser,  n.,  cupboard.  —  F.  dressoir,  fr.  dresser. See  dress,  v.
### source,
23143:source,  origin’,  formed  fr.  mater,  gen.  mdtris, ‘mother',  on  analogy  of  nutrix,  ‘wet-nurse, nurse'.  See  mother.  For  the  sense  development of  L.  matrix  (fr.  mater,  ‘mother’)  cp.  Gk.  p.r)tpa, ‘uterus,  womb’,  which  derives  fr.  moth-
36020:source,  n.  —  ME.  sours,  fr.  OF.  sorse,  surse, sorce  (later  source),  fern,  of  sors,  pp.  of  sordre, ‘to  rise',  used  as  a  noun,  fr.  L.  surgere,  ‘to  rise’. See  surge  and  cp  3rd  souse,  resource, sourdine,  n.  —  F.  See  sordine, souse,  n.,  salt  pickle.  —  ME.  souse,  fr.  OF.  souz, souce,  which — together  with  OProveng.  solz. It.  soldo,  of  s.m.— is  of  Teut.  origin.  Cp.  OHG. sulza  (for  *sult-ja),  ‘brine’  and  see  salt.  Cp.  also silt.
### regime,
32151:regime,  regime,  n.,  system  of  government.  —  F. regime,  fr.  OF.  regimen,  fr.  L.  regimen.  See  next word.
### real,
31813:real,  n.,  an  old  Spanish  silver  coin.  —  Sp.,  prop, an  adjective  meaning  ‘royal’,  fr.  L.  regalis (whence  also  F.  royal).  See  regal,  adj.,  and  cp. royal.  Cp.  also  reis.
### royal,
```


## [2026-09-14T01:17:01.915Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in escort address royal rail rule rex surge; do echo \"### $w\"; grep -n -m3 \"  $w,  n\\.\\|  $w,  tr\\.\\|^$w,  \" KLN_1966.txt KLN_1971.txt | cut -c1-700; done",
 "description": "Grep Klein for escort/address/royal/rail"
}
```


### [2026-09-14T01:17:03.180Z] TOOL RESULT

```
### escort
KLN_1966.txt:13625:Derivative :  escort,  tr.  v.
### address
KLN_1966.txt:1597:Derivatives:  address,  n. (q.v.), address-ee, n., ad- dr  ess-er,  n.,  address-ful,  adj.,  address-or,  n. address,  n.  —  A  blend  of  address,  v.,  and  F. adresse ,  ‘address’.
### royal
KLN_1966.txt:33240:Derivatives:  royal,  n.,  royal-ism,  n.,  royal-ist,  n., royal-ist-ic,  adj.,  royal-ize,  intr.  and  tr.  v.,  royal- iz-ation,  n.,  royal-ly,  adv.,  royalty  (q.v.) royalty,  n.  —  ME.  roialte,  fr.  MF.  roialte  (F.
### rail
KLN_1966.txt:31573:rail,  n.,  bar  (whence  railroad,  railway).  —  ME. raile,  fr.  MF.  reille ,  ‘bar,  rail’,  fr.  OF.  reille,  fr. L.  regula,  ‘a  straight  piece  of  wood,  ruler;  rule’, fr.  regere,  ‘to  keep  straight,  lead  straight,  rule’. See  regent  and  cp.  rule.  Cp.  also  derail,  mo¬ norail.
KLN_1966.txt:31574:rail,  intr.  v.,  to  furnish  with  rails.  —  ME.  railen, fr.  raile.  See  prec.  word.
KLN_1966.txt:31575:rail,  intr.  v.,  to  speak  reproachfully,  scold.  — ME.  railen,  fr.  MF.  (=  F.)  railler,  ‘to  jeer  at’,  fr. OProvene.  ralhar,  ‘to  joke,  jest’,  fr.  VL.  *ragu- lare,  ‘to  bray’  (whence  It.  ragghiare,  ‘to  bray’), fr.  Late  L.  ragere,  ‘to  neigh’,  which  is  prob.  of imitative  origin.  Originally  OProvenp.  ralhar  de¬ noted  different  kinds  of  cries,  and  only  gradually developed  the  meanings  ‘to  babble,  prattle;  to joke,  jest’.  Cp.  rally,  ‘to  banter’,  which  is  a doublet  of  rail.  Cp.  also  raillery.
### rule
KLN_1966.txt:32175:Derivatives :  regrettable-ness,n.,regrettabl-y,a<iv. regula,  n.,  a  band  or  filled  in  a  Doric  architrave (arch.)  —  L.  regula,  ‘ruler ;  rule’.  See  rule,  n.,  and cp.  regular.
KLN_1966.txt:33322:Derivatives:  rule-dom,  n.,  rule-less,  adj. rule,  tr.  and  intr.  v.  —  ME.  reulen,  rulen,  fr.  OF. reuler,  riuler,  fr.  L.  regulare,  ‘to  direct,  regulate’, fr.  regula.  See  rule,  n.,  and  cp.  regulate. Derivatives:  rul-er,  n.,  rul-er-ship,  n.,  rul-ing, adj.  and  n.,  rul-ing-Iy,  adv. nun,  n.,  spirit,  alcoholic  liquor.  —  Shortened  fr. rumbullion.
KLN_1966.txt:40824:Derivatives:  unmeet-ly,  adv.,  unmeet-ness,  n. unruly,  adj.,  hard  to  restrain,  disorderly.  —  ME. unreuly,  fr.  priv.  pref.  un-  and  reuiy,  ruly,  ‘amen¬ able  to  rule’,  fr.  reule,  ‘rule’.  See  rule,  n.,  and adj.  suff.  -y.
### rex
KLN_1966.txt:32739:rex,  n.,  king.  —  L.  rex,  gen.  regis,  ‘ruler,  king’, rel.  to  regere,  ‘to  keep  straight,  guide,  lead,  rule’, regina,  ‘queen’,  and  cogn.  with  Oi.  raj,-  rdjan-, ‘king’,  OIr.  ri,  gen.  rig,  ‘king’,  fr.  I.-E.  base *reg-,  ‘to  stretch,  straighten;  straight,  right;  to lead,  direct,  rule,  reign’.  See  regent,  adj.,  and  cp. raj,  rajah,  ranee,  regal,  regulus,  royal,  and  the second  element  in  viceroy.
### surge
KLN_1966.txt:37579:Derivatives:  surfeit-er,  n. surge,  intr.  v.,  to  rise.  —  MF.  sourgir,  fr.  Catal. sorgir  or  Sp.  surgir,  ‘to  cast  anchor’,  lit.  ‘to  rise (at  sea)’,  fr.  L.  surgere,  ‘to  raise,  erect ;  to  rise', contraction  of  *subs-regere,  fr.  sub-  and  regere, ‘to  direct’;  see  regent,  adj.  Cp.  OF.  sordre (whence  F.  sourdre),  ‘to  rise,  spring,  gush  forth ; to  result’,  which  derives  directly  fr.  L.  surgere. F.  sourdre  is  now  used  only  in  the  inf.  and  only in  an  elevated  style.  It  has  been  replaced  by  sur¬ gir,  ‘to  rise,  surge’,  as  a  loan  word  fr.  Sp.  surgir (see  above).  Cp.  surge,  n.
KLN_1966.txt:37580:surge,  n.,  a  large  mass  of  moving  water;  wave.  — Fr.  MF.  sourge-,  altered  (owing  to  the  influence of  L.  surgere)  fr.  sourje-,  stem  of  sourdre,  ‘to  rise’. Cp.  F.  surgeon,  ‘sucker,  offshoot’,  altered  fr.  OF. sourjon  through  the  influence  of  surgere.  See surge,  v.
```


## [2026-09-14T01:17:09.115Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '13620,13628p;1590,1600p;33235,33242p' KLN_1966.txt | cut -c1-800",
 "description": "Print Klein escort/address/royal entries"
}
```


### [2026-09-14T01:17:09.284Z] TOOL RESULT

```
Derivatives:  addict,  n.,  addict -ed,  adj.,  addict- ed-ness,  n.
addiction,  n.  —  L.  addictio,  gen.  -onis,  ‘an  award¬ ing,  devoting’,  fr.  addictus,  pp.  of  addicere.  See
addict  and  -ion.
Addison’s  disease.  —  So  called  by  its  discoverer Thomas  Addison  of  Guy’s  Hospital  in  1855. additament,  n.,  addition.  —  L.  additdmentum, ‘addition,  increase’,  fr.  *additare,  freq.  of  ad¬ dere  (pp.  additus),  ‘to  add’.  See  add  and  -ment. Derivative:  additament-ary,  adj. addition,  n.  —  OF  (=  F.),  fr.  L.  additionem,  acc. of  additio ,  ‘an  adding  to,  addition’,  fr.  additus, pp.  of  addere.  See  add  and  -ion.
Derivatives:  addition,  tr.  v.,  addition-al,  adj., addition-al-ly,  adv.,  addition-ary,  adj. additicious,  adj.,  increasing.  —  L.  additicius, ‘added,  additional’,  fr.  additus,  pp.  of  addere.  See add.  For  E.  -ous,  as  equivalent  to  L.  -us,  see  -ous. additive,  adj.  —  L.  additivus,  ‘added,  anexed', fr.  additus,  pp.  of  addere.  See  add  and  -ive. Derivatives:  additive-ly,  adv.,  additiv-ity,  n. addle,  n.,  urine,  filth.  —  OE.  adela,  rel.  to  OSwed. adel,  ‘urine’,  MLG.  adel,  Du.  aal,  ‘puddle’.  Cp. addle,  adj.
addle,  adj.,  putrid  (said  of  an  egg);  confused, muddled.  —  From  addle,  n.,  ‘urine,  filth’, whence  addle  egg,  used  in  the  sense  of  ‘an  egg that  does  not  hatch,  rotten  egg’,  but  lit.  meaning ‘urine  egg’ ;  a  term  due  to  the  literal  rendering of  L.  ovum  urinum,  ‘urine  egg’,  which  arose  from the  erroneous  translation  of  Gk.  oupiov  4»ov, ‘putrid  egg’,  prop,  ‘wind  egg’,  fr.  oupiog,  ‘of the  wind’  (fr.  oJSpog,  ‘wind’),  confused  with oiipiog,  ‘of  urine’,  fr.  oupov,  ‘urine’, address,  tr.  v.  —  ME.  adressen,  ‘to  raise,  adorn’,
F.  adresser,  fr.  OF.  adrecier,  fr.  a.  ‘to’  (see  hi), and  drecier  (F.  dresser),  ‘to  direct’.  See  ad- and  dress  and  cp.  direct
Derivatives:  address,  n. (q.v.), address-ee, n., ad- dr  ess-er,  n.,  address-ful,  adj.,  address-or,  n. address,  n.  —  A  blend  of  address,  v.,  and  F. adresse ,  ‘address’.
adduce,  tr.  v.,  to  bring  forward;  to  cite.  —  L .ad- ducere,  ‘to  lead  to’,  fr.  ad-  and  ducere  (pp. ductus),  ‘to  lead’.  See  duke.
23
Derivatives:  adduc-er,  n.,  adduc-ible,  adj. adducent,  adj.,  drawing  together  (said  of  mus¬ cles)  ;  the  opposite  of  abducent  ( anat .)  —  L.  ad- ditcens,  gen.  -ends,  pres.  part,  of  adducere.  See prec.  word  and  -ent.
esclave,  ‘slave’.  See  slave  and  -age. escoba,  n.,  tropical  American  mallow.  —  Sp., ‘broom,’  fr.  L.  scopa,  ‘twig,  shoot;  broom, besom,’  which  is  rel.  to  scapus,  ‘shaft,  beam’, fr.  I.-E.  base  *skap-,  *skop-,  ‘shaft,  thin  branch’, whence  also  shaft,  ‘stem,  stock’,  and  scepter (qq.v.)  Cp.  also  scopa.
esconson,  n.  (archit.)  —  OF.  escoinson  (F.  ecoin- f on,  ecoinson),  ‘jamb  of  doors  or  windows’.  See scuncheon,  which  is  a  doublet  of  esconson. Escorial,  n.,  a  palace  built  in  the  16th  century by  Philip  II  of  Spain,  NW.  of  Madrid.  —  Sp., prop,  ‘a  place  where  a  mine  has  been  exhausted’, fr.  escoria,  ‘dross,  scoria’,  fr.  L.  scoria,  of  s.m. See  scoria  and  adj.  suff.  -al. escort,  n.,  a  person  or  persons  accompanying  an¬ other  or  others  for  protection,  courtesy,  etc.  —
escritoire
estamisn
F.  escorte,  fr.  It.  scoria ,  fr.  scorgere,  ‘to  show, to  guide’,  fr.  VL.  *ex corrigere,  fr,  1st  ex-  and L.  corrigere,  ‘to  make  straight,  set  right’.  See correct,  adj.
Derivative :  escort,  tr.  v.
escritoire,  n.,  a  writing  desk.  —  OF.  (F.  ecritoire), fr.  Late  L.  scriptorium ,  ‘place  for  writing’,  prop, neut.  of  the  Latin  adjective  scriptorius,  ‘per¬ taining  to  writing’,  fr.  scriptus,  pp.  of  scribere, ‘to  write’.  See  scribe  and  cp.  scriptorium,  which is  a  doublet  of  escritoire. escrow,  n.,  a  written  engagement  (law).  —  OF. escroe ,  escroue,  ‘roll  of  papers’.  See  scroll, escudo,  n.,  i)  name  of  various  Spanish  and  Portu¬ guese  gold  and  silver  coins :  2)  the  gold  mone¬ tary  unit  of  Portugal,  —  Sp.  and  Port,  escudo, fr.  L.  scutum,  ‘shield’.  See  scutum  and  cp. escutcheon.
esculent,  adj.,  eatable;  edible.  - —  L.  esculentus, ‘good  to  eat,  eatable’,  fr.  esca,  ‘food’,  fr.  *eds- qd  (cp.  Lith.  eska,  ‘appetite’),  fr.  I.-E.  base  *ed-, ‘to  eat’.  See  eat.
escutcheon,  n.,  a  shield  on  which  a  coat  of  arms is  depicted  (her.)  —  ONF.  escuchon,  corres¬ ponding  to  OF.  escuson,  F.  ecusson,  fr.  VL. *scutidnem,  acc.  of  *sei<tio,  fr.  L.  scutum,  ‘shield’. See  scutum  and  cp.  scutcheon,  escudo.  For  the collateral  forms  escutcheon  and  scutcheon  cp. espy,  spy;  esquire,  squire;  estate,  state.
rowan,  n.,  1)  the  mountain-ash;  2)  the  berries  of the  mountain-ash.  —  Of  Scand.  origin.  Cp.  ON. reynir,  ron,  Swed.  ronn,  ‘the  rowan’, rowdy,  n.,  a  rough,  quarrelsome  person.  —  Prob. a  derivative  of  row,  ‘noise,  uproar’.
Derivatives:  rowdy,  adj.,  rowdi-Iy,  adv.,  rowdi¬ ness,  n.,  rowdy-ish,  adj.,  rowdy-ism,  n. rowel,  n.,  pointed  wheel  in  a  spur.  —  ME.  rowelle, ruel,  fr.  OF.  roele,  rouele  (F.  rouelle),  ‘a  small wheel',  dimin.  of  roue,  ‘wheel’,  fr.  L.  rota.  See rota  and  -el,  and  cp.  rouelle,  roulette. Derivative:  rowel,  tr.  v.
rowlandite,  n.,  an  yttrium  silicate  (mineral.)  — Named  after  the  American  physicist  Henry Augustus  Rowland  (1848-1901).  For  the  ending see  subst.  suff.  -ite.
rowlock,  n.,  an  oarlock.  —  An  alteration  of  oar¬ lock,  through  the  substitution  of  the  verb  row, ‘to  propel  with  oars’,  for  the  noun  oar.
Roxana,  n,,  fem.  PN.  —  L.  Roxane,  fr.  Gk. ’  Pcocxvq,  which  is  of  Persian  origin.  Cp.  Avestic raoxshna-,  ‘shining,  brilliant’, royal,  adj.  —  ME.  roial,  fr.  MF.  roial  (F.  royal), fr.  L.  regalis,  'pertaining  to  a  king,  royal',  fr. rex,  gen.  regis,  ‘king’.  See  rex  and  cp.  regal  and real,  ‘a  coin',  which  are  doublets  of  royal.  Cp. also  viceroy,  corduroy.
Derivatives:  royal,  n.,  royal-ism,  n.,  royal-ist,  n., royal-ist-ic,  adj.,  royal-ize,  intr.  and  tr.  v.,  royal- iz-ation,  n.,  royal-ly,  adv.,  royalty  (q.v.) royalty,  n.  —  ME.  roialte,  fr.  MF.  roialte  (F.
royaute),  fr.  VL.  *regdlitatem,  acc.  of  *regdlitas, fr.  L.  regalis.  See  royal  and  -ty  and  cp.  regality, realty,  which  are  doublets  of  royalty.
-rrhagia,  combining  form  used  to  denote  ‘a  burst¬ ing  forth,  excessive  flow’,  as  in  menorrhagia ( med .)  —  Medical  L.,  fr.  Gk.  -ppoqxa,  ‘a  burst¬ ing  forth’,  from  the  stem  of  prjYvuvai.,  ‘to  break forth,  burst  forth’.  See  regma.
```


## [2026-09-14T01:17:17.348Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"آدرس\" \"رژیم\" \"اسکورت\" \"رگل\" \"رویال\"; do echo \"### $w\"; grep -h -m3 -n \"$w\" MON_part1.txt MON_part2.txt 2>/dev/null | cut -c1-400; done",
 "description": "Grep Moin for French loans"
}
```


### [2026-09-14T01:17:18.493Z] TOOL RESULT

```
### آدرس
98863:آدرس؛ ج. عناوین» عنوانات. 
### رژیم
16910:مسحاک مه گردند. صح.- مش رژیم 
16926:آشکارا از رژیم کاپیتولاسیون استفاده 
67907:خوشه‌ای را بوجود می آورند که رژیم نامیده 
7782:زیان آور» رژیم. 
67222:مسمکلت: رژیم دموکراسی رژیم 
### اسکورت
12942:اسکورت: 07 (.) دسته‌ای از سربازان 
### رگل
1177:پیشانی» زبرگلو) که بریدن و برآوردن آن 
1207:سرگلو و حلقوم از سوی دهان. جان به غرغر 
1330:آواز انفجا رگلو له. 
7537:وقت. مرگك» هنگام مرگله نهایت زمان 
29839:درخت و گل» پرگل. (بنا.) تيغة روی قالب 
47554:شود. جرس د رگلو بستن: (کد.) دعا کردن به 
### رویال
```


## [2026-09-14T01:17:22.375Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -m2 -B2 -A2 \"اسکورت\" MON_part1.txt | cut -c1-300; echo \"-----\"; grep -rn \"آدرس\" MON_part1.txt | head -5 | cut -c1-300",
 "description": "Context for eskort and adres in Moin"
}
```


### [2026-09-14T01:17:22.470Z] TOOL RESULT

```
12940-شکافی. 
12941-
12942:اسکورت: 07 (.) دسته‌ای از سربازان 
12943-مسلح که در التزام رکاب شاه» رئیس جمهور 
12944-و غیر ه باشد. 
-----
MON_part1.txt:98863:آدرس؛ ج. عناوین» عنوانات.
```


## [2026-09-14T01:17:30.984Z] TOOL CALL #49: Bash

```json
{
 "command": "ls site/pages/417.jpg 2>/dev/null; pdftoppm -f 417 -l 417 -r 150 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg417 && echo OK",
 "description": "Render PDF page 417"
}
```


### [2026-09-14T01:17:32.474Z] TOOL RESULT

```
site/pages/417.jpg
OK
```


## [2026-09-14T01:17:34.623Z] TOOL CALL #50: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg417.png"
}
```


### [2026-09-14T01:17:34.661Z] TOOL RESULT

```

```


## [2026-09-14T01:17:52.033Z] TOOL CALL #51: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-14T01:17:52.042Z] TOOL RESULT

```


```


## [2026-09-14T01:17:55.360Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83re%C7%B5-",
 "prompt": "Give the reconstructed root, its meaning, and the list of derived terms/descendants (Indo-Iranian, Latin, Germanic, Greek). Quote the gloss exactly."
}
```


## [2026-09-14T01:17:56.957Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D8%B2%D9%85",
 "prompt": "Persian entry رزم: give the full etymology (Middle Persian, Proto-Iranian, Avestan cognates) and the meaning. Quote exactly."
}
```


### [2026-09-14T01:18:00.482Z] TOOL RESULT

```
# Proto-Indo-European Root: h₃reǵ-

**Reconstructed Root:** *h₃reǵ-

**Meanings:** The root carries two related senses: "to straighten" and "to righten."

**Key Derived Terms and Descendants:**

*Indo-Iranian:*
- Sanskrit: राज् (rāj, "to rule, govern"), ऋज् (ṛj, "to direct, stretch")
- Sanskrit: राष्टि (rā́ṣṭi), राजति (rā́jati)

*Latin:*
- rēxī (aorist form from the s-aorist stem)

*Greek:*
- ὤρεξα (ṓrexa, "aorist of ὀρέγω" (orégō))

*Celtic:*
- Old Irish: atrecht (from s-aorist stem)

The root fundamentally relates to concepts of straightening, directing, and ruling—meanings that evolved across Indo-European daughter languages into terms for sovereignty and authority.
```


### [2026-09-14T01:18:01.035Z] TOOL RESULT

```
# Persian Entry: رزم (razm)

**Etymology:**
According to the Wiktionary entry, the word comes "From Middle Persian _lcm_ (razm). Akin to Old Armenian _ռազմ_ (ṙazm), an Iranian borrowing."

The entry does not provide Proto-Iranian or Avestan cognates—only the Middle Persian source and an Armenian cognate.

**Meaning:**
The noun رزم (razm) means "war, battle, combat." Related synonyms include نبرد (nabard), پیکار (peykâr), آورد (âvard), کارزار (kârzâr), and جنگ (jang).
```


## [2026-09-14T01:18:05.037Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D8%A7%D8%B3%D8%AA",
 "prompt": "Persian entry راست (râst): give the etymology in full (Middle Persian, Old Persian, Proto-Iranian, Avestan, PIE) and the meanings. Quote exactly."
}
```


## [2026-09-14T01:18:06.761Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B1%D8%A7%D8%B4%D8%AA%D9%86",
 "prompt": "Persian entry افراشتن: give the etymology (Middle Persian, prefix, root) and meaning. Quote exactly. Also mention افراختن if present."
}
```


### [2026-09-14T01:18:10.463Z] TOOL RESULT

```
# افراشتن (afrâštan)

## Etymology
The word derives from Middle Persian *abrāštan* meaning "to lift, raise." It is a compound verb composed of:
- Prefix *af-* from Proto-Iranian *Hápa* ("off, away, from")
- Root *rāš-* from Proto-Indo-Iranian *Hraštás* ("straightened, right")

## Meaning
The verb means "to raise, to elevate, to lift, to exalt, to erect."

## Alternative Form
**افراختن** (afrâxtan) is listed as an alternative form.
```


### [2026-09-14T01:18:10.611Z] TOOL RESULT

```
# Persian Entry: راست (râst)

## Etymology

The word traces back through several language stages:

**Middle Persian:** "rāst"

**Old Persian:** "𐎼𐎠𐎿𐎫" (rāsta, meaning "right")

**Proto-Iranian:** "*Hraštáh"

**Proto-Indo-European:** "*h₃reǵtós" — described as ""having moved in a straight line"", deriving from "*h₃reǵ-" meaning ""to straighten, direct""

The entry notes it is cognate with English "right."

## Meanings

As an adjective, راست carries five primary senses:

1. Straight (opposite of curved or bent)
2. Direct; proceeding without deviation
3. Right (the dexter side, opposite of left)
4. True; correct (opposite of false)
5. Erect in posture

As a noun, it means:

1. Truth (the opposite of falsehood)
2. In music, a Persian modal system called "rast"
```


## [2026-09-14T01:18:14.514Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D8%AC%23Persian",
 "prompt": "Persian entry رج (raj): etymology and meaning. Quote exactly."
}
```


## [2026-09-14T01:18:15.460Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D8%AF%D9%87",
 "prompt": "Persian entry رده (rade): etymology and meaning. Quote exactly. Also any Middle Persian form."
}
```


### [2026-09-14T01:18:19.120Z] TOOL RESULT

```
# Persian Entry for رج (raj)

Based on the Wiktionary page provided, there is **no Persian entry** for رج (raj) included in this document. 

The page contains entries only for:
1. **Arabic** - where رج (rajja) is a verb meaning "to shake, to agitate, to convulse"
2. **Talysh** - where رج (raj) means "order" or "line"

The page header indicates "6 languages" are covered, and mentions a link to "فارسی" (Persian) Wiktionary, but the actual Persian definition and etymology are not presented in this particular page content.
```


### [2026-09-14T01:18:19.672Z] TOOL RESULT

```
# Persian Entry: رده (rade)

## Etymology
The word is "Inherited from Middle Persian _ltg'_ (/⁠radag⁠/, 'line, rank, row')" and traces back to Proto-Indo-European *h₂rey- meaning "to arrange, count."

**Middle Persian form:** ltg' (radag)

## Meanings
The Persian noun رده has three primary definitions:
1. Row
2. Category
3. Class (in biology contexts)
```


## [2026-09-14T01:18:33.250Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"razm\\|radag\\|rāst\\b\\|rāst \\|rāstīh\" PHD_mackenzie.txt PHD.txt 2>/dev/null | head -20; echo \"=== NYB ===\"; grep -n \"razm\\|radak\\|rāst\" NYB_vol2_glossary.txt | head -20",
 "description": "Grep MacKenzie and Nyberg"
}
```


### [2026-09-14T01:18:33.334Z] TOOL RESULT

```
PHD.txt:158:(p. 143) (vii) read 1 frārāst, ārešn ....
PHD.txt:214:a-pus [' BRE] without a son, childless. ár-, v. árdan. 5 āranj "Inc | N ~] elbow.. 9-43. "Ant *a-rāst Prst'] untruth. ārāstan, ārāy- [Pstn!,^Pd- | N ~] prepare, arrange, adorn. ~ién: arrangement, adornment. a-rawüg [”/wbk!] immobile. Ard р | M?yrd, N ~] a goddess; cal. 25th day. ard [KHM A < А gm; п | N ~] flour. агаа [py | (M rd?w)] righteous, truthful. ardan, ār- [THNN-tn' < А V thn; ?l-tn'] grind, mill. ardāyīh ['i?dyh | M?rd?yyh] righteousness, rectitude. ardig [/tyk! | M ?rdyg] battle. ardikkar рук], -kl | M?rdyqr] warlike, warrior. ~ith: doing battle. arduš [”ldwš = Av. aroduš-] a degree of sin. Ardwahišt Prtwhst' | M ?rdywhyst, (N urdībihist)] Right, the second Amahraspand, guardian of fire; cal. 2nd month; 3rd day. arešk [lysk' | M ()rysk, N rašk] envy, jealousy. ~én [-yn'] envious, jealous. ārešn Pim! | M ”7ysn-, N (a)rif] cubit. aryand [?/епа | N ~] horrible. arģawān [*/gwk'*n! | N aryawān] purple. armēšt ["/myst'] inactive, infirm. ~ih: infirmity. armēšt-ģāh [-g’s] secluded place for the infirm. агбуї&п [/wdšn'] growth. ~ig [-y&!] growing, vegetable. ars Dis | M?rs, N ~] tear (drop). artēštār УЯ? | N artēšdār!] warrior. „īh: warriorhood. arus [2/00] white. arwand [wnd] swift, valiant; river Orontes. ~ih: swiftness, valour. arwés [lwys | M ?rwys, N ~] rope. arz [KSP! < А Ар; с | N ~] worth, value. Arzah [Iz h == Av. arazahi-] the eastern continent of the earth. arzan [PE < А prg’; len! | N <) millet. arzàn Plen | M *rz'n, N ~] valuable, worthy. ~ig [-yk'] worthy. ~igih: value, worth, worthiness. arzidan, arz- [?/с-уїп! | N ~] be worth. ~išn: value, worth. arziz (сус | M ?rzyz, N ~] tin, lead. —ën [-yn'] tin, leaden. ārzōg Picwk! | M'wrzwg, N àrzó] desire, lust,
PHD.txt:538:pādīrān [p'igP n!] restrained, held back. pādīrān(ēn)īdan, pādirān(ēn)- [þptgľn(yn)-ytn'] restrain, impede. padīriftan, padir- [MK BLWN-tn!Ü < A mqbl, V qbl; ptgl-ptn! | M pdyr-yptn, N paóiruftan] receive, accept. ~išn: reception, acceptance. īpadisār [ptys' | N padīsār ?] beginning, basis. tpadisār [ptys’/] bridle, halter. padisāy [pts’d | M рдуу] on account of, for the sake of. padist [ptst! | P pdyst] promise, vow. & (abar) burdan: promise. padistadan, padist- [ptyst-”tn! | (P pdystwd)] promise, vow. padistā(£) [ptyst*k! | (M pdystw)] = padist. padiš (pts | M pdys] to him, it; postposition (= pad) to, etc. padištān [pryst?n' | P pdyst??n] leg. padišxwar [ptshwl] dish, bowl. pādixšā(y) [SL Y TA < A йур; p’ths?(d) | M раху] ruler; powerful, authoritative, authorized. ~ЛЬ : sovereignty, authority. pādixšīr [p’thsyl] agreement, treaty. pad-néróg [PW Nnylwk!] strong. pad-niģerišn [PWNnkylin'] cared for, guarded. pādofrāh [p’twpl’s) = pādifrāh. pad-panag [PWNpnk!] guarded, protected. Р pádrazm [p’tlcm] battle. pàd-rózag [p’tlwck' | M p'drweg] fasting. pād-uzwān [p’??wzw’n'] reticent. ~ih: reticence. pad-wizén [PW Nwcyn!] choice, select. pādyāb [pty | N ~] ritually clean; ceremonial ablution. ~ih : ceremonial ablution. pādyāwand [p?tyd’wnd | J p'dywnd] strong, powerful. cAh : strength, superiority. pádzahr [p’tzhl | N pa(d)zahr] bezoar, antidote. pad-zyān [PWNzyd"?n'] harmful. pafšār- [pps?/-] shame. pafšīr- [ppsyl-] be ashamed. ~i8n(ih): shame. pah [p’h] sheep. ~ast [-st'] sheep-fold, -pen. pahikaftan, pahikaf- [ptkp-tn! | M phykf-] fall on, touch, hit, attack. ~išn: attack, fight. pahikāftan, pahikāf- [ptk’p-in'] throw on, make fight. pahikar [ptk] | M phykr, N paykar] picture, image. pahikār [ptk?! | M phyk”r, N paykār] struggle, battle, dispute. īpahikār- [ptk?/-] fight, contend with, defeat. pahikardan, *pahikār- [ptk’/-tn'] request, claim, consult.
PHD.txt:555:rabih [/pyh | M rbyh] noon, midday (heat). rad [/t! | N —] (spiritual) chief, master. АҺ: office of rad. rad [Pu | P rd, N ~] generous, liberal. ~ih: generosity, liberality. radag [itk! | M rdg, N rada] line, rank, row. radómand [/t?^wmnd] having a rad. rad-passag [/tps’k'] ceremonies of the gáhanbar festivals. radunay [/twny = Av. ratunaya-] one under the guidance of a rad. raftan, raw- [SGY TWN-tn! < А V sg’; lwb- | M rptn, rw-, N ~] go, move, proceed. ~išn, v. rawišn. raftār [/pt?] | N ~] goer. rag А! | M rg, N ~] vein. «ЛЬ: disposition, character. ray [/gy | P rg] quick, swift. ray [Pg | N —] meadow, plain. rah [/s, lh, [hy | M rh(y)] chariot, wagon. rah-, у. rastan. rah [Ps | M rh, N ~] road, way. rahag [/hk! | P rhg] = rag. rāh-dār [lsd] | N ~] brigand, highway robber. ~ih: brigandage. rahig [/syk!, Ikyk' | M rhyg, N rahi] child, page. ~ih: childhood. rāh-nimāy [Psnm?d | (M r’-hnmwd’r), № ~numa] guide. ram [Pm | М әт, N ~] peace; cal. 21st day. ram(ag) [/m(k') | P rm, N ram(a)] herd, flock. ráménidan, rāmēn- [Pmyn-ytn! | M ?myn-] give peace, pleasure. rāmišn [P min! | M rmyfn, N rāmi$] peace, ease, pleasure. ~ig [-vk! | N —z#] peaceful, at ease. ran [Рп! | N ~] thigh. P rān- [/^n-] fight. randidan, rand- [/nd-ytn! | N —] scratch, grate, abrade. rang [/ng | M rng, N —] colour, dye. ranj [Inc | P rnj, (M rnz), N ~] toil, trouble. ~ag [-k' | N —a] troubled. ranjénidan, ranjén- [/ncyn-ytn'] trouble.
PHD.txt:557:ranjwar [Incwl | (M rnzwr), N ranjūr] troubled, distressed. rapihwin [/pys-, Ipyt-pyn!, -wyn' = Av. rapiüfina-] the afternoon gah; south. ~tar [-tl] southern. rasan [/sn' | N ~] rope. rasénidan, rasén- [/syn-yin'] bring. rasidan, ras- [YHMTWN-tn' < А yhmtwn, V mt^; ls-ytn! | M rs-ydn, N ~] arrive, mature. raspig [Pspyk!] second officiating priest. rast [Pst! | M rst, N ~] true, straight, direct. ~ih: truth, rastaģ [lstk! | N rasta] series, row, progression; element, газап, rah- [Istn', Ї(?)А- | N ~] escape. rastarih [/st?/y%] escape. rasüg [/swk! | (N rāsū)] weasel. Rašn [/@! | M ri, N ~] god of Justice; cal. 18th day. ra&tan, *raz- [/ftn'] colour, dye. raw-, v. raftan. rawag [/wP^k! | N rawá] current. ~ih: currency. rawügenidan, rawagén- [/zob)hyn-ytn!] set in motion, propagate. rawénidan, rawén- [SGYTWNyn-ytn', v. raftan] cause to go, extend. rawišn [lwbin', SGYTWNsn', v. raftan | N rawif] going, motion. ^h : behaviour; as a suffix, forms abstract nouns. ray [Pd | M ry, N ra] postposition, for, for the sake of. rāyēnāģ [Pdym bi | M r’yn’g] arranger. rayénidan, rāyēn- [Pdyn-ytn! | M r'yn-ydn] lead, direct, arrange, organize. ~išn: action, function; arrangement. rāyēnīdārīh [/”*dynyt?lyh | M r!ynyd?ryh] direction, organization, rāyišn [”dsn'] order, arrangement. rāyomand [Pd^wmnd] rich, majestic. raz [/c, lz | N ~] vine; vineyard. raz [Pc | M Pz, N ~] secret, mystery. ~ig [-yk'] secret. rāz-kirrēģ [Pc kylwk' | M г qrwg] architect, builder. razm [/cm | M rzm, N —] battle. —--$àh [-g's | P -g’h, (M rzm?h), N ~] battlefield. razor [lcw] | M rzwr] forest. rédak [lytk' | N ~] lad, page. тёр [/yā! | N ~] sand. rëm [lym | M rym, N —] dirt, filth, purulence. réman [lymn' | M rymn, N ~] dirty, filthy, purulent. ^b : filth. 1r€§ []yf | N ~] wound, sore. *rēš [/yf | N —] beard.
PHD.txt:939:battle ardīg, hamrānīh, jang, nibard, pahikār, razm, P pādrazm; do ~ nibardidan; v. fight; doing ~ ardikkarih.
PHD.txt:940:battlefield kārezār, razmgāh.
PHD.txt:1457:cubit ārešn, frārāst.
PHD.txt:2639:line kiš, radag.
PHD.txt:3324:rank radag; without ~ agāh,
PHD.txt:3482:row radag, rastag.
PHD.txt:4429:1 frārāst (24 a.) = 1 ft. ëm. ‘cubit’
PHD.txt:4688:frahixtan frahixtag frayádisnig fravādišn frāy frādahišnīh frahist farroxīh farrox lxwah-I xwastant frārāst frārūnīh frārēn frāmēš frūmēš- frāmuštan frahist parrag frch pardāxtan frehbūdīh frehbūd pardāz-
PHD.txt:4743:padrazm sò rey о) pādifrāh © teras arzan!, gāwars! 5o)
PHD.txt:4891:jām mānsīr māns*rbar mānsšrspand māraspand mānbān mānbed mānišn māzanīg māzandar māzdēsnīh māzdēsn fradagt mar
PHD.txt:4905:tat! , (tarr) lajan razür razm razmgah tar!
PHD.txt:4907:rad radunay radag саас
PHD.txt:4960:е rahag ult ulih! € эў ulimadant AA rim ey nānī _ rāmēn- А“ riménidan OV r��mišnīg _ ~ rámián A» rāspīg we rāstīh 14 nu» rast
PHD_mackenzie.txt:3949:P padrazm [p)tlcm] battle.
PHD_mackenzie.txt:4302:radag [ltk' I M rdg, N rada] line, rank, row.
=== NYB ===
621:ürüstan [’P’stn'] ārāy-, to equip (an army) 712, 9617, 9815 etc.; to prepare 105; 6 ham ~ id. 3927. 408 19; — to organize 1315, to arrange 11213. — < à + Av. (1520 sa.) rüd-, cf (335) ārādah-; Paz. ārāstan ārāēd, NP ärästan ārāy-. V. pairästak and virästan, and cf s. v. nisästan.
848:Pywe't'] cikāmcihē Pourusäsp ku yazišn kunät whenever P. intends to perform a sacrifice 5313-14, — Av. (1231) yaoz- ‘to be agitated’; MPrth rzmy(y)wz ‘eager for battle’ (A-H III); Arm. lw. yoiz 'commo- tion, trouble’, but also ‘research, investi- gation’ (den. vb. yuz-em ‘to agitate; to scrutinize’); — ä-yaoz- ‘to agitate, to MPrth ”ywštn, ?ywz- (’y-) (A-H III), ”*ywštg ‘tossing’ (sea), ’ywz ‘violent; disturbance’ (MHC). Borrowed in MPrs in the same sense (Verbum 183) and also in BP: razmik adydzisn ["ywešn'] ‘the act of fighting in battle-array', NSt § 3; äyöz renders Av. yaozante Y. 654. In SW, where Z changed to z, āyēz- coincided with āyēž- and adopted its inf. āyuxtan, ef DkM 695 pres. äyöz-, but 6815 äyux- tārēh in the sense ‘strive for’. The genuine SW form of yaoz-: OP yaud-, v. yöd-; possibly represented by *āhēyēnītan (q.
884:āžarmīkēh an honoured position (in this life) 724. — Paz. substitutes dzarmi. Azi-dahäk [?cydh’k'], Aždahik [’cdh’k'] the name of a dragon; ~ razm ''a Dragon battle", a battle as furious as if the dragon A. were the enemy 21°. 309. — Borrowed from Av. (266, 704) AZi-daha- ka-; MPrs 'zdh'g (S, A-H I), ’wzdh’g (A-H I, a popular etymology); MPrth ’zdh’g, jd ?g, Sogd. 21sg.; Paz. Aži-dahāk; NP aždaha. — V. also Dahäk.
1019:brahmak [blhmk'] (splendid) garment, of the princely footwear 295. — MPrthPrs brhm ‘garment, elegant form, grace’ eto., v. Henning, TPhS 1944, 108-118 (I cannot accept his combining this w. with OP brazman.) Paz. brahm, Skr. v. vesa, šriigara (SGV).
1436:. ~ šutan nē šāyet except on a mission ‘of the gods it is not possible to pass 7810-11; ba 801% is not taken up by ~ until 1. 24; bē ka rāst göbeh ēnyā, ham- dātistān ne bavém except if thou tellest the truth we shall not come to terms 1521-22; 6520 v. pditiašdi; hakar ... vicà- ret — ... if he explains ... [it is just right], otherwise ... 1181-15, as in Arab in halla wa'illa; hac Armail ~ except (by) Armail 1151-11, — Av. (138) anyādā, Gath. for anyd@G, Skr anydtha; Paikuli, Prs ’yny’ (Herzfeld p. 132); FrP
1451:age DkM 6989; tat pat dātistān(ūman>- deh či veh tuvän zatan u éraxtan cigón ka-š pat davreh u drusteh apäk gēbāh through righteousness thou art better able to defeat him and make him lose the case than if thou speakest to him coarsely and roughly (cf s. v. davr) PR 573; — pres. pass. 3d p. sg. éraxtét he is pronounc- ed guilty, opp. buxtet he is acquitted, v. Bthl, ZsR IV, 8; Paz. buxted ... érexted SGV III, 26; kē rāstēh rad pat xudstak eraxtet, ah veh cigon kē družeh rād pat ruvān éraxtét he who suffers loss of prop- erty because of his righteousness is better than the one who suffers the loss of his soul (forfeits his soul) because of his falsity PR 26$-9.] — Two vbs. seem to have coalesced here: 1) črtatan ērēc-, cf Paz. érexted and the caus. érezinidan ‘to condemn’ SGV XI, 257, most probably < abi- + Av. (1479 sq.) raék- ‘to leave in the lurch, to abandon to destruction’ (Bthl IF XII, 112sqq.); 2. éraxtan érang-, most probably a denom. of érang, črangčh 'trouble, delusion' (Paz. ŠGV X, 58 ete.) < *abi-ranga-, cf. an-črang, ranj, ranjak; MPrs ‘yrat, “yrnz- ‘to combat’, Verbum 199. (Bthl, l.c. adopted the reading érazt).
1477:ēvarz ['dwlc'] review, muster, as a mili- tary term: ~ kartan to review, to muster (an. army) 2014; — [hence ēvarzīk kas probably *a man called up for military service, DkM 750!?]. — Originally ‘com- putation, calculation, account’, ef the following examples: ~ 4 x“atdydn 6 osti- kan the rulers’ calling of their trustees to account DkM 40416; étar *zarvan i (K drang) àivan (< K) andak, ~ züt; änöd dātavār (!) rāst here (in this world) the term of the court is short, and the account swift; there (in heaven) is & righteous *judgment DkM 5481-11; apar hān 4 andar nihvārēh ~ about the items (necessary) in combat FrP 14, heading. In all probability to be connected with NP dvàr(ah) ‘calculation, reckoning; an account-book’ (of which dvārjah, dvarcah ‘a cash-book, a book of receipts and dis- boursments, a diary, or register’ is the diminutive) < *abi-varda- SW form of *abi-varza-; dvdr : ēvarz, cf ēvāc, Evar, évar. (Wrong interpretation by Nyberg, TMK 69 sq., Pagliaro, Iscr. Dura-Europo 592. 595). — From varz-, v. varz, varzitan.
2212:Karazm [klem] n. pr. son or relative of Vištāsp 114%, — NP Gurazm (Sn), late form of Av. (443) Kavdrasman-; Cat. 50.
2902:pairästak [pdl'stk'] ready-made 6°. — Arm lw. patrast; NP vb. patrāstan patrāy-; < pati + Av. (1520) räd- ‘to get ready’ (Skr rddh-). The prev. pat-, generally preserved in the archaistic BP orthogra- phy, is here written phonetically in the genuine SW form pai-. Through mutual exchange MPrth. and MPrs have got one common vb. pdr’stn pdr’y-: Verbum 187, Ghilain 60. There has been some con- fusion between old räd- and old räz-, SW rüd-, but there is no necessity for deriv- ing pairästan from räz- as does Hen- ning. V. the following ws. and cf ärästan, virastan.
2905:pairāyišnīk possessing embellishment, embellished, sup. —-tar 178. — Adj. of pairäyisn, v. 8. v. pavrāstak.
2906:pairök [pylwk'] efflux of light, effulgence 1124. — < *pati-rauka-, cf röc, rošn; as to pai- v.S.v. patrāstak. Ps. ptlwk ‘splendour’.
3022:pat-fracéh [PWN pPcyh] appearance 40% (read: api-sän ētēn-aš ~ 6 ham ārāst *,.. his appearance’). 4019, cf 39??, — pat fraceh 52? are two distinct ws., v. frācēk.
3080:pätrazm [p’tlem] counterattack 2719, v. razm. — Arm. lw. paterazm ‘war, battle’.
3220:celestial body 877-15; — in a metaphorical sense, of religion and its doctrines 62°. 6325-27; — in a psychological sense 659-19; — pat ~ i by means of 6216. 6712-18; pat ~ + rāstēh in the way of righteousness 7019; ~ u bahän means and motives 8313. — MPrthPrs rh; Paz. NP rah; OIr "rada- derived from Av. (1506) rada- ‘car, chariot’; ef rahy.
3272:āfrīn (q. v.) ~ i rāstē u ~ i ahläyeh the
3298:riyénitan to arrange, to manage, to organize, to further: 137-17, 8818. 9119; to dispose of = to make away with 501°; to distribute 892°; — as a juridical term: to carry on a lawsuit, of every legal procedure in its entirety (Bthl, SRb 22), hence patvand i geteh ~ to settle for- mally (by juridically valid contract) one’s family-ties in this world 6316; to contract a marriage 104%; stüreh ~ 84%, v. stureh. — Paz. räinidan; as to the etymo- logy ef s. v. patrāstak.
3302:razm [lem] battle, 21-30 passim; pl. cas. obl. —-an 2611, 291; ~~ u pätrazm (g. v.) 2719; pēš-~ soldier of the first line 11913, — Av. (1513 sq.) rasman- ‘battle-array, phalanx’; MPrthPrs rzm; Paz. NP razm.
3320:2ristak [lystk', Istk'] 1. custom, rule, law: v. yuvat-ristak. — 2. adj. firm, reliable, truthful 1101’; sup. ~-tom 59", cf ristake- nitan. — From Av. rād-, v. s. v. patrāstak and ef rdyénitan; MPrth pt. ryst ‘exact, correct’, Ghilain 60; Paz. subst. (SGV) rastaa ‘law, element’ (= Gr ototxetov, thus de Menasce); NP rast ‘firm, steady’, rastah ‘rule, institute, market’; Talm lw. rystq? ‘market-place’, Telegdi 255.
3690:täftan [t’ptn'] tāp-, opt. 2nd p. sg. tapes, l. trans. razm ~ to stir up, to excite a battle 2219.13.16; nat ātaxš ~ to roast, to grill 445. — 2. intrans. to shine 1%, 372, — Av. (631sg.) tap-, pres. tāpa-, caus. täpaya-; MPrth t’b’dn tb- ‘to burn, to shine’, Ghilain 72; NP taftan tàb- ‘to set on fire, to shine’; v. also tap.
4397:yabb(u) [ybb] a Turkish royal title 113%. 11524. — F. W. K. Miller, Mahrnamag 1, l. 93 yaßyü,l. 77 Zaßyü; Ibn Xordadbeh, BGA VI, 163.401: jabyüyah; al-Xuarizmi, Mafatih al-"ulum 120: jabbüyah ; Ērānšahr, v. Index; Bailey, BSOS VI, 1930, 63—64; Unvala, The translation of an extract from Mafdtih al-ulūm of al-Khwärazmi (The K. R. Cama Oriental Institute, s.a.) 20, n. 50.
```


## [2026-09-14T01:18:48.719Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/maharaja",
 "prompt": "Give the etymology of maharaja: Sanskrit components, PIE roots of each, and meaning. Quote exactly."
}
```


## [2026-09-14T01:18:50.711Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%DB%8C%D8%A7%D9%84",
 "prompt": "Persian entry ریال: etymology (Spanish real? Arabic?) and meaning. Quote exactly. Also any Arabic ريال entry etymology."
}
```


### [2026-09-14T01:18:53.226Z] TOOL RESULT

```
# Etymology of Maharaja

## Sanskrit Components

According to the Wiktionary entry, maharaja derives from Sanskrit **महाराज** (mahārāja), which breaks down as:

- **mahā** = "great"
- **rāja** = "king/ruler"

## Exact Quote

The entry states: "Borrowed from Hindi महाराजा (mahārājā). First attested in 1698."

For the Sanskrit connection, the Malay section notes: "Borrowed from Sanskrit महाराज (mahārāja). By surface analysis, maha + raja."

## PIE Roots

The document does not provide Proto-Indo-European (PIE) root etymologies for the Sanskrit components. It only identifies the Sanskrit word and its compound structure (great + king), without tracing the roots further back to PIE origins.
```


### [2026-09-14T01:18:55.674Z] TOOL RESULT

```
# ریال (Rial) - Etymology Summary

## Persian Entry Etymology

The Persian ریال entry states: "Compare [Arabic](https://en.wikipedia.org/wiki/Arabic "w:Arabic") _[رِيَال](/wiki/%D8%B1%D9%8A%D8%A7%D9%84#Arabic "ريال")_ (riyāl) and [Ottoman Turkish](https://en.wikipedia.org/wiki/Ottoman_Turkish "w:Ottoman Turkish") _[ریال](#Ottoman_Turkish)_, both from [Spanish](https://en.wikipedia.org/wiki/Spanish_language "w:Spanish language") _[real](/wiki/real#Spanish "real")_."

This indicates the Persian word traces back to Spanish *real*, with the Arabic term sharing the same ultimate origin.

## Persian Noun Definition

The word means "rial (the official currency of Iran)."

## Note on Arabic Entry

The page mentions an Arabic entry ريال exists but does not provide its etymology details in the content shown. The etymology section only notes that both the Arabic and Ottoman Turkish forms derive from Spanish *real*.
```


## [2026-09-14T01:18:59.873Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A2%D8%AF%D8%B1%D8%B3/",
 "prompt": "Show the فرهنگ معین entry for آدرس, including any origin tag like [فر.] or [فرانسه]. Quote exactly."
}
```


## [2026-09-14T01:19:01.230Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B1%DA%98%DB%8C%D9%85/",
 "prompt": "Show the فرهنگ معین entry for رژیم, including any origin tag like [فر.]. Quote exactly."
}
```


### [2026-09-14T01:19:03.442Z] TOOL RESULT

```
The server returned HTTP 400 Bad Request.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-14T01:19:05.945Z] TOOL RESULT

```
# فرهنگ معین Entry for رژیم

According to the فرهنگ معین section provided, the entry reads:

"(رِ ) [ فر. ] (اِ. ) ۱ - حکومت ، نوع حکومت . ۲ - دستورالعمل برای غذا خوردن . ۳ - طریقه ، روش ، قاعده ."

The origin tag [فر.] indicates the word derives from French (فرانسوی), and the entry presents three primary definitions: governance/type of government, dietary guidelines, and method/rule/procedure.
```


## [2026-09-14T01:19:09.512Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/%D8%A2%D8%AF%D8%B1%D8%B3",
 "prompt": "Show the فرهنگ معین entry for آدرس with its origin tag. Quote exactly."
}
```


### [2026-09-14T01:19:13.158Z] TOOL RESULT

```
# Farhang-e Moein Entry for آدرس

According to the Farhang-e Moein dictionary shown above, the entry for آدرس includes this origin tag and definition:

**(رِ) [ فر. ]** — indicating Persian origin

The definition states: **"1 - نشانی خانه ، اداره و مانند آن ، نشانی (فره ). 2 - عنوان و نام کس یا جایی بر پشت پاکت و مانند آن"**

This translates to the word meaning an address or location identifier for a home, office, or similar place, as well as a title or name written on envelopes and similar items.
```


## [2026-09-14T01:19:23.726Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd2 reĝ ===\"; grep -n \"reĝ-\\|re:ĝ-\\|reg-.*gerade richten\\|gerade richten\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -10",
 "description": "Grep Walde-Pokorny Bd2 for reg"
}
```


### [2026-09-14T01:19:23.791Z] TOOL RESULT

```
=== WLD Bd2 reĝ ===
40873:,, gerade richten“ eingemischt sei, z. B. Falk-Torp u. stroekke ist eine iiber-
```


## [2026-09-14T01:19:25.621Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB ===\"; grep -n \"razm\\|rāst\\|rast \" HUB.txt | head -15; echo \"=== LAT rex ===\"; grep -n \"^rex\\|rego,\\|rex,\" LAT.txt | head -10",
 "description": "Grep Hubschmann and Ernout-Meillet"
}
```


### [2026-09-14T01:19:25.698Z] TOOL RESULT

```
=== HUB ===
1212:paz. padafrah, phi. patafrds; phi. patrazm Yatk. i.
1213:Zar. 66, Anm. 61 = arm. paterazm *Krieg, Kampf,
1214:Schlacht' (vgl. np. razm *Kampf ') , entsprechend im
2110:standig Min. Gl. 66 (LW. bal. drust^ afgh. drast ganz,
2321:612. Np. razm 'Schlacht' ist = ap. "^razma = zd. rasma
2327:regelrecht zd. sm = ap. zm, Zu arm. razm und pate'
2328:razm vgl. phi. razm u patrazm Yatk. i. Zar. p. 66.
3788:arm. yoiz-k 'Suchen* etc. (vgl, np. razmyoz Kampf-
4457:XoHQOTjg = pers. Xusrav ; XfO()aaiLua = ap. {h)uvarazmis, np.
4458:x^'arazm; ^AguyMaia = ap. hara(h)uvatis etc.
4680:Strafe', paz. padafrah, phi. patafrds; phi. patrazm Yatk. i.
4681:Zar. 66, Anm. 61 = arm. paterazm 'Krieg, Kampf, Schlacht'
4682:(vgl. np. razm ^Kampf).
5334:zd. myazda^; niyCt *Grossvater' = ap. zd. nyaka-; razm-yOz
5383:suche' (5. Jhd.), np. razmyOz *kampfbegierig*, vgl. arm. Raz~
=== LAT rex ===
156:1'autre, ainsi credd ou rex, lex, dans deux des langues qui
3266:Rappelle imbrex, imbrices dont il pourrait etre, comme le suggbre
5104:sedisant grex, et Colum.3,14,4 diff 4 rencie armenta de iumenta comme
5386:Arx serait un mot racine comme lux,uox, prex, etc. Mais il n'y a peut-
7678:rex potando lassatur, calore torretur, bractatur nero. De la bracta-
25376:Dirivis: gallo "( 3 bj 3 a^u)" ( 61 .); gallina : poule. Cf. rex, rSgina. Sans
26942:grex, gregis m.(f£n. dans Lucii, et Lucr.): d^signe une r^union
26950:"r 4 unir en troupeau" (lat. inp 4 r., M.l.3858) d^prfes congrego, M.L.
29462:Derives et compos^s: imbrex,-icis f. et m. : tuile faitibre (snr la
31275:pontificum euulgauit. - Atteste de tout temps; non roman (cf. rego,
```


## [2026-09-14T01:19:34.268Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2315,2335p' HUB.txt",
 "description": "Print Hubschmann 612"
}
```


### [2026-09-14T01:19:34.316Z] TOOL RESULT

```
610. Np.rwa? Wange gehSrt nicht hierher.
611. Np. rod weise, tapfer' stimmt in der Bedeutung nicht
zu zd. ratU' 'geistliches Oberhaupt, Herr' = paz. ra3
'master' Shk. 264 = np. rad (rad) 'Oberhaupt eines
Kreises' (Tab. 447). Nach NSldeke ist aber rad bei
F i r d u s i = 'Herr oder 'Held'. Vgl. z. B. Fi r d. 1, 130, 28.
612. Np. razm 'Schlacht' ist = ap. "^razma = zd. rasma
'Schlachtreihe (von Wzl. raz = idg. reg^, vgl. skr.
raju *Reihe'). Der Ubergang von 'Schlachtreihe' zu
'Schlacht' ist, meine ich, begreiflich und iiberdies be-
legbar, vgl. z. B. arm. iakat *Stim, Front, Heerresfront,- 67 -
Schlachtreibe, Schlacht'. Fiir idg. g^m, g^hm erscheint
regelrecht zd. sm = ap. zm, Zu arm. razm und pate'
razm vgl. phi. razm u patrazm Yatk. i. Zar. p. 66.
616. Np. rasad = ap. rasatiy zu skr. rdchdti. Uber die
Bildung vgl. Bartholomae, Idg. Forsch. II, 264.
Die Etymologie gait schon lange vor WZKM. 6, 187,
vgl. z. B. Bartholomae, Handbuch p. 120.
617. Osset. alwtstn^ dltolstn spinnen* findet sich bei Sjogren
p. 351 und Bischof Joseph p. 441 (s. v. prjasfi). Es
stimmt zu bal. brBsag. Aus dem Afgh. geh5rt hierher
```


## [2026-09-14T01:19:46.460Z] TOOL CALL #67: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83re%C7%B5-\" \\\n \"https://en.wiktionary.org/wiki/%D8%B1%D8%B2%D9%85\" \\\n \"https://en.wiktionary.org/wiki/%D8%B1%D8%A7%D8%B3%D8%AA\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B1%D8%A7%D8%B4%D8%AA%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%B1%D8%AF%D9%87\" \\\n \"https://en.wiktionary.org/wiki/maharaja\" \\\n \"https://en.wiktionary.org/wiki/%D8%B1%DB%8C%D8%A7%D9%84\" \\\n \"https://vajehyab.com/moein/%D8%A2%D8%AF%D8%B1%D8%B3\" \\\n \"https://abadis.ir/fatofa/%D8%B1%DA%98%DB%8C%D9%85/\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"pdf page 417, root Reg 1 / *h3reg-, verification of Persian rast/raj/rade/razm/afraštan, maharaja, riyal, adres/režim\" 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-14T01:19:52.086Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/b0f1264324ea4839.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/72ca9f4c36216d04.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3ff0003ebf2f5e8f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b5f815bd0c1c7d9e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5fe8767639ad0120.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/390c52e77db82991.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4ca4c56ebdf15023.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/09089d0dfecedc95.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8c1e2abd59f920d7.txt
```


## [2026-09-14T01:19:56.826Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT right/rake/royal/rail ===\"; grep -n -m1 \"^Right, adj\\|^Right,\" SKT.txt | cut -c1-500; grep -n -m1 \"^Rake (1)\\|^Rake,\" SKT.txt | cut -c1-400; grep -n -m1 \"^Royal,\" SKT.txt | cut -c1-400; echo \"=== LKT real/rial ===\"; grep -n -i \"real\\b.*span\\|rial\" LKT.txt | head -8 | cut -c1-300; echo \"=== HJB maharaja ===\"; grep -n -i \"maharaja\" HJB.txt | head -5 | cut -c1-300",
 "description": "Grep Skeat, Lokotsch, Hobson-Jobson"
}
```


### [2026-09-14T01:19:56.951Z] TOOL RESULT

```
=== SKT right/rake/royal/rail ===
=== LKT real/rial ===
29:Das  etymologische  Wörterbuch  der  europäischen  Wörter  urieulaHschen Ursprungs  verdankt  seine  erste  Anregung  dem  häufig  ausgesprochenen Wunsche  meiner  Hörer  an  der  Kölner  Handelshochschule  und  Universität, die  Hinweise  auf  das  Weiterleben  orientalischer  Grundwörte
2472:'Hohe  Mütze'  aus  verschiedenem  Ma- terial (Ziegen-  oder  Lammfell,  Leinen); hieraus  bulg.  serb.  kalpak  'Pelzmütze', poln.  kofpak  'hohe  Pelzmütze,  Husaren- mütze', russ.  kolpak  'Schlafmütze',  klruss. koupak  'Barett' ;  rum.  calpac  'Pelzmütze', frz.  kaipack,  calpan;  d
2518:'Hoher  Berg',  N.  pr.,  ein  Berg,  der  we- nige Meilen  nordwestlich  von  der  Stadt King-te-chen  (290  gg'  n.  Br.,  1"  10'  ö.  L. von  Peking)  liegt.  Hier  wurden  große Mengen  einer  besonderen  Art  Feldspats als  Rohmaterial  für  die  Porzellanher- stellung gewonnen.  Eine
2817:'Kohle,  Holzkohle'  [Stamm  k'dj  'brennen, glühen,  Glut,  Brand',  also  *küjmiir 'Brennmaterial',  Vämbery  TktEtWb S.  105,  Nr.  116];  hieraus  bulg.  k'iimur., k'imur  'Kohle',  kiimurica  'Kohlenmeiler', serb.  cumur  'Kohle'.  [Bern  SiEtWb  681.
3619:'Adler  Aquila  imperialis'  [vom  Vb.  ka- sara  'die  Flüg'el  einziehen,  um  sich  zu senken']  beeinflußt  sein?  [Devic  DEt  28 und  226.  Lammens  Rem  249/250.
3693:'Reif,  gekocht',  dann  auch  'beständig, fest';  hieraus  angloind.  pucka  zur  Be- zeichnung eines  aus  Ziegeln  und  Mörtel gebauten  Hauses  im  Gegensalz  zu  solchen aus  geringerem  Material  [s.  hier  Nr.  983]. [Hobson-Jobson  734.
3914:1716.  Ar.  ri'äs: 'Schwertknauf,  -griff'  [vgl.  ra's,  s.  hier Nr.  1701];  hieraus  mit  ar.  Art.  s^t.arriaz, arrial  'Slichblatt  des  Degens',  pg.aniaz 'Metallstück  am  Pferdeharnisch'  [Con- stancio  Dicc  117  a].  [DE  202.  Eguilaz 288.    ML  7295.
=== HJB maharaja ===
4406:[1875.— "  Bandflqis,  or  orderlies  of  the Maharaja,  carrying  long  guns  in  a  loose  red cloth  cover." — Drew,  Jummoo  and  Kashmir, 74.]
7891:c.  943.— '*  The  territories  of  this  Prince Qhe  Maharaja  of  the  Isles)  produce  all  sorts of  spices  and  aromatics.  .  .  .  The  exports are  camphor,  lign-aloee,  clove,  sandal-wood, betel-nut,  nutmeg,  caraamom,  onbeb  (al- koMbah).  .  .  ."—Ma^adt,  i.  841  teq.
8367:1888.— "The  Maharajah  sent  us  in  the evening  a  new  set  of  dandng  giris,  as  they were  called,  though  they  turned  out  to  he twelve  of  the  ugliest  old  women  I  ever  saw." — Otbome,  Court  and  Camp  of  Runjeel  Singh, 164.
8792:1808. — "A  remarkable  circumstance  took place  yesterday.  Some  Sirdars  put  the Maharaja  (Sindia)  in  dhuma.  He  was angry,  and  threatened  to  put  them  to  death. Bhugwunt  Ras  Byse,  their  head,  said,  'Sit still;  put  us  to  death.'  Sindia  was  enraged, and  ordered  hi
10865:of  several  ancient  Hindu  dynasties, and  from  the  time  of  the  early Mahommedan  sovereLps  of  Delhi down  to  the  reign  of  Aurangzib  it was  used  as  a  state-prison.  Early  in the  18th  century  it  fell  into  the  posses- sion of  the  Manratta  family  of  Smdhia, whose  r
```


## [2026-09-14T01:20:02.173Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i -m3 \"RIGHT, adj\\|RAKE (1)\\|ROYAL\\.\" SKT.txt | cut -c1-600; echo \"====\"; grep -n -i -m2 \"REGENT\\|RECTITUDE\" SKT.txt | cut -c1-600",
 "description": "Explore Skeat format"
}
```


### [2026-09-14T01:20:02.248Z] TOOL RESULT

```
1485:n  -  .l,.,f  .V  _T  _<;l  'i  Short  for ;*  Cot.— ,    royal.—
15841:royal.   (F.-L.)     M.  K.   rtai,  r^ial  ^
23240:regal— royal.
====
5116:L.)    I.,   dirw,    featful.    -^    Gk. idfol ;  allied  to  Ai'or,  fear. see  Regent. CC.)     Irish   duirt,    a
15682:Reach  (i),  to  attain.  (£.) pt.  t-  rai^hte,  raujf^fe,  pp    n.- TiXi  att,  rAcean,    pt.  t.  rikft.  -^  ' '   rn rika,    G.   rtithen.      The   A  S.   r-fv  aiv raikian)  seems  to  mean  'to  !■■•'  '"f-  '•■ power,*  and  is  allied  to  the  >  i answering  to  Goth,  reiki,  |(ri» Still  more  cloMrly  allied  to  tbe occasion,  due  time;   Ihls  wonU orig.  sense  '  lo  seize  an  opport comes  to  much  the  same  thing.     Thcl base  is  RAK  «  Aryan  lO\G.  to  rule; Regent.   Der.  reaek,  sb.,  which  also  nU '  a  stretch  in  a  river."
```


## [2026-09-14T01:20:03.657Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i -m4 \"RAJA\\b\\|RAJAH\" HJB.txt | cut -c1-600; echo \"=== AID ===\"; grep -n -i -m4 \"maharaja\\|Raja,\" AID.txt | cut -c1-400",
 "description": "Hobson-Jobson raja entry"
}
```


### [2026-09-14T01:20:03.731Z] TOOL RESULT

```
178:Other  terms  again  are  corruptions,  more  or  less  violent,  of  Oriental  words and  phrases  which  have  put  on  an  English  mask.  Such  are  maund,  fooVs rack,  bearer,  cot,  boy,  belly-band,  Penang-lavjyer,  buckshaw,  goddess  (in  the Malay  r^on,  representing  Malay  gddts,  *a  maiden'),  compound,  college* pheasant,  chopper,  summer-head,*  eagle-wood,  Jocfco^^-copal,  bobbery.  Upper  Roger (used  in  a  correspondence  given  by  Dalrj'mple,  for  Yuva  Raja,  the  '  Young King,'  or  Caesar,  of  Indo-Chinese  monarchies),  Isle-o^-Bats  (for  Allahabad  or Il
1651:Dekho  Raja  teri  Marwar.
1655:Sack  is  thy  kingdom,  Raja  of  Marwar  !)
1852:1798.— "The  Rajah's  Sotoarree  was  very grand  and  superb.  He  had  twenty  ele- phants, with  richly  embroidered  ambazrehs, the  whole  of  them  mounted  by  his  sirdars, — ^he  himself  ridmg  upon  the  largest,  put  in the  centre." — Skinner,  Mem.  i.  157.
=== AID ===
```


## [2026-09-14T01:20:09.224Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Skt.  rdjd\\|Skt.  raja\\|rdjan\\|maha-raja\\|mahd-raja\\|mahdraja\" HJB.txt | head -10 | cut -c1-400",
 "description": "HJB raja etymology"
}
```


### [2026-09-14T01:20:09.297Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:20:12.615Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"RAJA\" HJB.txt | head -10 | cut -c1-400; echo \"=== SYN king ===\"; grep -n \"rex, regis\\|Skt. rajan\\|OIr. ri, rig\" SYN.txt | head -6 | cut -c1-400",
 "description": "HJB RAJA headword and Buck king"
}
```


### [2026-09-14T01:20:12.723Z] TOOL RESULT

```
18502:RAJA,  RAJAH.
18520:RAJAMUNDBY,  n.p.  A  town, formerly  head-place  of  a  district,  on the  lower  Godavery  R  The  name  is in  Telegii  Rdjamahendravaramu, '  King- chief('s>-Town,'  [and  takes  its  name from  Mahendradeva  of  the  Oriasa dynasty ;  see  Morrisy  Godavery  Mnn^ 23].
18834:BOY,  s.  A  common  mode  of  writ- ing the  title  rdt  (see  RAJA) ;  which sometimes  occurs  also  as  a  family name,  as  in  that  of  the  famous  Hindu Theist  Rammohun  Boy.
=== SYN king ===
33218:were often used where we should render ‘prince’ (so Grk. Baotdebs, Lat. réx with dim. régulus, Skt. rajan-, etc.), or words for ‘ruler, leader’ (so Grk. a&pxwy in the Bible commonly rendered ‘prince’), or words for ‘a noble’ (as ON gdlingr, OK epeling, etc.).
```


## [2026-09-14T01:20:15.980Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '18502,18520p' HJB.txt | cut -c1-1200; echo \"=== SYN 'king' section ===\"; grep -n \"19.31 KING\\|KING$\" SYN.txt | head; grep -n \"Skt. rajan-, orig\" SYN.txt | head",
 "description": "Print HJB RAJA entry"
}
```


### [2026-09-14T01:20:17.155Z] TOOL RESULT

```
RAJA,  RAJAH.
754
RAJPOOT.
India  it   generally  means  'a    native gentleman  of  respectable  position.'
1610.—*' .  .  .  Beyses  of  all  our  Nauyes." —Birdtpood,  Firtt  Letter  Book,  435.
1785. — *'.  .  .  their  chief  (more  worthless in  truth  than  a  honekeepeor)."  In  note — "  In  the  original  the  word  flnrBO  is  introduced for  the  sake  of  a  jingle  with  the  word  Bysa (a  chief  or  leader)." — Tippoo't  Lettert,  18.
1870.—" Baees."    See  under  EYOT.
1900. — "The  petition  was  signed  by  re- presentative landlords,  Taises.  *  —  Ptower Mail,  April  13.]
BAJA,  BAJAH,  s.  Skt.  raid, *  king.'  The  word  is  still  used  in  this sense,  but  titles  have  a  tendency  to degenerate,  and  this  one  is  applied  to many  humbler  dignitaries,  petty  chiefs, or  large  Zemindars.  It  is  also  now  a title  of  nobility  conferred  by  the British  Government,  as  it  was  by  their Mahommedan  predecessors,  on  Hindus, as  Nawab  is  upon  Moslem.  Rdl,  RdOy Rdnd,  Rd^valy  Rdya  (in  S.  India),  are other  forms  which  the  word  has  taken in  vernacular  dialects  or  particular applications.  The  word  spread  with Hindu  civilisation  to  the  eastward, and  survives  in  the  titles  of  Indo- Chinese  sovereigns,  and  in  those  of Malay  and  Javanese  chiefs  and  princes.
It  18  curious  that  the  term  Rdjd  can- not be  traced,  so  far  as  we  know,  in any  of  the  Greek  or  Latin  references to  India,  unless  the  very  questionable instance  of  Pliny's  Rachias  be  an exception.  In  early  Mahommedan writers  the  now  less  usual,  but  stiU Indian,  forms  Rdo  and  Rd%  are  those which  we  find.  (Ibn  Batuta,  it  will be  seen,  regards  the  words  for  king  in India  and  in  Spain  as  identical,  in which  he  is  fundamentally  right.) Among  the  English  vulgarisms  of  the 18th  century  again  we  sometimes  find the  word  barbarised  into  Roger.
c.  1838.—".  .  .  Bahfi-uddin  fled  to  one of  the  heathen  Kings  called  the  R&1  Kan- bUah.  The  word  Bfti  among  those  people, just  as  among  the  people  of  Rum,  signifies *King."'— /6»  Batuta,  iii.  318.  The  tra- Teller  here  refers,  as  appears  by  another passage,  to  the  Spanish  it^/.
[1609.— "Ealaw."    See  under  OOONT.]
1612.—"  In  all  this  part  of  the  East  there are  4  castes.  .  .  .  The  first  caste  is  that  of the  Bayas,  and  this  is  a  most  noble  race from  which  spring  all  the  Kings  of  Canara. .  .  ."—Couto,  V.  vi.  4.
[1615.— "According  to  your  direction  I have  sent  per   Orincay   (see   OBANKAY)
Beege    Roger's    junk    six    peoculles    (se^ PECUL)  of  loBid."— Foster,  LdtUrt,  iv.  107.
[1628. —  "A  Ba«ia,  that  u  an  Indian Pnnoe."— P.  dellaValle,  Hak.  Soc.  i.  84.]
1688.—"  I  went  a  hunting  with  ye  Sa^TB^ who  was  attended  with  2  or  800  men,  armed with  bows  and  arrows,  swords  and  tazvets.**' —Hedges,  Diary,  March  1 ;  [Hak,  Soc.  i.  6«].
1786.  —  Tippoo  with  gross  impropriety addresses  Louis  XVI.  as  "the  Bajah  of  the French."— &^  Letters,  369.
RAJAMUNDBY,  n.p.  A  town, formerly  head-place  of  a  district,  on the  lower  Godavery  R  The  name  is in  Telegii  Rdjamahendravaramu, '  King- chief('s>-Town,'  [and  takes  its  name from  Mahendradeva  of  the  Oriasa dynasty ;  see  Morrisy  Godavery  Mnn^ 23].
=== SYN 'king' section ===
26058:15.26 BAD SMELLING, STINKING
33141:19.32 KING
```


## [2026-09-14T01:20:21.888Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '33141,33175p' SYN.txt | cut -c1-1500",
 "description": "Print Buck 19.32 KING"
}
```


### [2026-09-14T01:20:21.948Z] TOOL RESULT

```
19.32 KING
Grk.  Bacvdebs (vat poet.), Goth. piudans Lith. karalius
Byz. pnt ON konungr, bjddann Lett. karalis, k'énin’’ NG  Baotdebs, pop. Dan.  konge ChSl.  césar’t, kral’t
Baotdtas Sw. konung SCr. kralj Lat. rex OE cyning, péoden Boh. krdl It. re ME kyng Pol. krél Fr. Tot NE king Russ. korol’ Sp. rey Du. koning Skt. rdjan-, raj- Rum. rege OHG  kuni(n)g Av. xsaya-, OPers. Tr. rt MHG kunec xsayabiya- NIr. 7% NHG kénig W. brenin, teyrn Br. roue
The title of ‘king’ has been, in the course of history, applied not only to the rulers of independent states, even great empires (before the rise of a superior title ‘emperor’, 19.34), but also to the petty chiefs of tribes or clans. Cf. NED s.v. king.
1. IE *rég-, fr. the root *reg- in Lat. regere ‘direct, guide, rule’, etc. (19.31) Walde-P. 2.362 ff. Ernout-M. 864.
Lat. réx, gen. régis (> the Romance words; but Rum. rege modern; older cratu, fr. Slavic kral’t); Gall. -rix in Dumno-riz, etc., Ir. ri, gen. rig (W. rhi arch. ‘lord, nobleman’), OCorn. ruy, Br. roue, MBr. roe (Pedersen 1.51; or Br. forms fr. Fr. roi ?); Skt. (Vedic) raj-, but commonly n-stem rajan-; cf. Goth. reiks ‘ruler’, loanword fr, Celtic.
2, Grk. Baothebs, NG pop. Baodrds, without etym. (connection with ads people’ impossible) and prob. of pre- Greek origin. Boisacq 115f. Wacker- nagel, Sprachl. Untersuch. zu Homer 212, Kretschmer, Glotta 10.222. Wie- ewiez, Hos 31.526 ff.
Grk. ayat, dial. favat, poet. word often applied to kings but also to gods and heroes, ‘lord, master’ (for Hom. use
of avat vs. Baoidebs, cf. Wackernagel, op. cit. 209 ff.), possibly : Skt. van- ‘win, gain’, etc. (Schwyzer, Glotta 6.86), but more prob. of pre-Greek origin. Cuny, Rev. ét. anc. 16.297. Debrunner in Ebert, Reallex. 4.2.527. Smieszek, Eos 31.547 ff.
In Byzantine times Bactdebs was ‘em- peror’, the regular title of the Roman emperor and the Persian ‘king of kings’ (19.34). For ‘king’ Lat. réx was adopted, e.g. pnt TorOwv, pre dpayxwv, etc. Theo- phanes (1.472f. DeBoor) notes the crowning of Charlemagne, s7£ trav dpay- Kwy, &S Bactdeds ‘Pwyaiwy. But generally the German emperors were not accord- ing the emperor title by the Byzantine court. NG pias ‘king’ in cards.
3. W. brenin : W. bry ‘high’, Ir. bri, W. bre ‘hill’, Skt. brhant- ‘great, high’ (cf. fem. brhatt-, Ir. Brigit ‘the exalted one’), Av. barazant- ‘high’, ete. Walde-P. 2.173. Pedersen 1.100.
W. teyrn ‘ruler, king. : Ir. tigerne ‘master, lord’ (19.41). Here also W. mechdeyrn, OBr. machtiern (‘tributary prince’), OCorn. mychtern (reg. word for ‘king’, Williams Lex. 260), epd. with word seen in Ir. mac, W. mach ‘bond
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
?
1322
surety’. Loth, L’&migration bretonne en Armorique 218 ff., Voc. vieux-bret. 182. Thurneysen Z. celt Ph. 19.130. Otherwise (but to be rejected) Pedersen 1.137 and Ifor Williams, BBCS 10.39 ff.
4, Goth. piudans, ON pjddann, OF péoden, derivs. of Goth. biuda, ON )jo0, OE féod ‘people, nation’ (19.22).
ON konungr, OF cyning, etc. (with short forms OF cyng, etc.), general Gmc. except Goth. : Goth. kunz, OE cyn, etc. ‘family, race’ (NE kin), but prob. more directly as patronymic of ON konr ‘man of noble birth’, OF cyne-, OHG kuni- in epds., hence orig. ‘descendant of one of noble birth’. Falk-Torp 563. Weigand- H. 1.1108. NED s.v. king.
5. Lith. karalius (> Lett. karalis), fr. the Slavic (below, 6). Brickner, SI. Fremdwéorter 90. Miihl.-Endz. 2.160.
Lett. (pop.) k’énin’§, fr. MLG konink
Digitized by Arya Samaj Foundation Chennai and eGangotri
SELECTED INDO-EUROPEAN SYNONYMS
(Du. koning, etc., above). Miihl.-Endz. 2.374. :
6. ChSl. césar’t (reg. for Bacrdeds, whether ‘king’ as in the Gospels or the Roman ‘emperor’), see under ‘emperor’ (19.34).
Late ChSl. kral’t, etc., general mod- ern Slavic, fr. OHG Karl, the name of Charlemagne, who came into conflict with various Slavic peoples and was known to them all as the great ‘king’ of the time. An adverse, but improbable, view is that the source is not the personal name but the antecedent appellative seen in OHG karl ‘man, freeman’. Berneker 572 f. (with lit., to which add, for the adverse view, Stender-Petersen 206 ff.)
7. Skt. raj-, rdjan-, above, 1.
Av. xSaya-, OPers. xsdayadiya- : Av. xsi- ‘have power, rule’, Skt. ksi- ‘possess, rule’ (19.31).
19.33 QUEEN Grk. actdea, Bact\roca Goth. Lith. karaliené NG ss Bactd\rcoa ON drotining Lett. karaliene, k'eniniene Lat.  régina Dan. dronning ChSl.  césarica It. regina Sw. drotining SCr. _ kraljica Fr. reine OE cwén Boh. kralovna Sp. reina ME quene Pol. krélowa Rum. regina NE queen Russ. koroleva ; Ir. rigan Du. koningin Skt. rajiir- Nir. —_bainrioghan OHG kunninginna, kun- W. brenhines ningin Br. rouanez MHG kininginne, kiinigin NHG kénigin
Nearly all the words for ‘queen’ are obvious fem. derivs. of those for ‘king’ (NIr. bainrioghan, with common prefix ban-, bain- : bean ‘woman’). Exceptions are the following:
( OE cwén, ME quene, NE queen : | Goth. géns ‘wife’, gind ‘woman’, Grk.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
yuri ‘woman, wife’, etc. (2.22, 2.32). In OE sometimes simply ‘wife’, but mostly specialized to ‘king’s wife’. NED s.v. queen.
ON drotining, Dan. dronning, Sw. drottning, in ON also ‘mistress’, fem. of ON dréttinn ‘master’ (19.41).
SOCIAL RELATIONS
```


## [2026-09-14T01:20:31.313Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW rego ===\"; grep -n \"rego, -ere\\|rego,-ere\\|^rego\" LEW_1910.txt | head -5 | cut -c1-500; echo \"=== IEC reg ===\"; grep -n \"reĝō\\|regō \\|reg- 'straighten\\|rēg-\" IEC.txt | head -8 | cut -c1-300; echo \"=== ARY latin index rast ===\"; grep -n -i \"rast\\|RAZM\" incoming/ARY/ARY_latin_index_pages.txt | head -10 | cut -c1-200",
 "description": "Grep Walde-LEW, Mann, Aryanpur"
}
```


### [2026-09-14T01:20:31.423Z] TOOL RESULT

```
=== LEW rego ===
=== IEC reg ===
=== ARY latin index rast ===
1398:RATEN H(GERMAN) aT ARASTAN (PAHLAVI) 5 shy
8597:RIHT HOLD ENGLISH) gS gad! RASTA- (OLD PERSIAN) glob go
8598:RIGHT ENGLISH) gudSst RAST PAHLAVI) 6 3h
8600:RAT (SWEDISH) (543 yo RAST KURDISH) 3,5
8601:REIT NORWEGIAN) $395 RAST ABALUCHD) go sh
8602:RECHT (DUTCH) gale RAST 4AFGHANI) (24), jail
8688:REIKS, REIKI GOTHIC) 3, RASTAR 4AVESTAN) glues)
8783:PATERAZM, RAZM (ARMENIAN) «| RASMA
8784:OREGMA (GREEK) gly RAZMA (OLD PERSIAN) ijtaly +
8785:REGIMEN, REGERE — (LATIN) 33 RAZM s(PAHLAVI) 5 3h )
```


## [2026-09-14T01:20:36.538Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('incoming/ARY/ARY_latin_index_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ncur=None\nfor i,l in enumerate(lines,1):\n    m=re.search(r'\\[pdf page (\\d+)\\]',l)\n    if m: cur=m.group(1)\n    if i in (8597,8598,8688,8783,8784,8785,1398):\n        print(i,'pdfpage',cur,l[:160])\nEOF",
 "description": "Map ARY index lines to pdf pages"
}
```


### [2026-09-14T01:20:38.155Z] TOOL RESULT

```
1398 pdfpage 51 RATEN H(GERMAN) aT ARASTAN (PAHLAVI) 5 shy
8597 pdfpage 297 RIHT HOLD ENGLISH) gS gad! RASTA- (OLD PERSIAN) glob go
8598 pdfpage 297 RIGHT ENGLISH) gudSst RAST PAHLAVI) 6 3h
8688 pdfpage 300 REIKS, REIKI GOTHIC) 3, RASTAR 4AVESTAN) glues)
8783 pdfpage 303 PATERAZM, RAZM (ARMENIAN) «| RASMA
8784 pdfpage 303 OREGMA (GREEK) gly RAZMA (OLD PERSIAN) ijtaly +
8785 pdfpage 303 REGIMEN, REGERE — (LATIN) 33 RAZM s(PAHLAVI) 5 3h )
```


## [2026-09-14T01:20:44.364Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ncur=None\nfor i,l in enumerate(lines,1):\n    m=re.search(r'\\[pdf page (\\d+)\\]',l)\n    if m: cur=m.group(1)\n    if ('رزم' in l and 'RASMA' in l.upper()) or ('راست' in l and 'RAST' in l.upper()):\n        print(i,cur,l[:250])\nEOF\ngrep -n \"RASMA\\|RAZMA\" incoming/ARY/ARY_pages.txt | head -10 | cut -c1-250",
 "description": "Find ARY main entries"
}
```


### [2026-09-14T01:20:45.556Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:20:48.268Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"رزم\" incoming/ARY/ARY_pages.txt | head -10 | cut -c1-300; echo \"---\"; grep -n \"راست\" incoming/ARY/ARY_pages.txt | head -6 | cut -c1-300",
 "description": "Grep ARY pages for razm/rast"
}
```


### [2026-09-14T01:20:48.348Z] TOOL RESULT

```
87:معتقد بودند که گهواره‌ی آریایی‌های ابرنژاد شمال باختری اروپا بوده و از آنجا به سرزمین‌های دیگر
90:نژادهای «پست‌تر» بیشتر شد. بهمین دلیل در سرزمین‌های دور از آلمان درصد مردم چشم آبی و
108:سرزمین آغازین هند و اروپائیان
111:کردستان و سرزمین‌های اطراف آن است چون در اين نواحی بود که در حدود ده هزار سال پیش
114:سرزمین کم‌کم از یک سو به فلات ایران و شمال هندوستان و از سوی دیگر به آسیای صغیر و از آنجا
121:حاشیه‌ی سرزمین‌های هند و اروپایی را محقق می‌کند و پعید است که جنبش کوچگری هند و
123:نواحی زبان‌های اولیه این سّرزمین‌ها نبوده‌اند و توسط کوچگران به آنجا برده شده‌اند. ۳-بسیاری از
146:آیا خاستگاه مردمان هند و اروپایی در سرزمین‌های‌گسترده‌ی شمال . .
164:شامل سرزمین‌های شمال دریای سیاه و دریای خزر می‌شد. همین خوی کوچگری و تحرکك (به
165:علاوه‌ی مجهز بودن به اسب و ارابه و سلاح‌ها و ترفندهای رزمی پیشرفته و دارا بودن خصلت
---
85:باور می‌کردند که آریایی‌های راستین مردمی بلند قامت با چشمان آبی ر موی طلایی بودند که از نظر
710:۹ جنوب را مختمل تر می‌نماید. مضاقاً به اینکه قبل از آنان؛ نیا کان هندیان نیز در همین راستاکوج کرده
1193:پژوهش‌ها را ادامه داده و برای فارسی‌ز؛ بانان و به زبان فارسی ارائه داده‌اند. ویراست فرهنگ پرها **
1923:۱ این واژه با واژه‌ی "راست" همریشه است.
4836:۱- معنی اين واژه در هتبت: حفظ و حراست کردن.
6589:: چم اين واژه در زبان آلمانی: حفظ و حراست کردن.
```


## [2026-09-14T01:21:04.284Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"rëx\\|rex, regis\\|regö\\|rego \" LEW_1910.txt | head -8 | cut -c1-400; echo \"=== LAT rego ===\"; grep -n \"rego,\\|regere,\" LAT.txt | head -6 | cut -c1-500",
 "description": "Grep Latin etymological dictionaries"
}
```


### [2026-09-14T01:21:04.351Z] TOOL RESULT

```
=== LAT rego ===
26950:"r 4 unir en troupeau" (lat. inp 4 r., M.l.3858) d^prfes congrego, M.L.
31275:pontificum euulgauit. - Atteste de tout temps; non roman (cf. rego,
53131:regere, ou du prdfixe re-.
53490:- Il est naturel de penser que rex appartient au groupe de rego,
53766:rogo, -as, -aul, -atum, -are: s'apparente sans doute a rego, le
```


## [2026-09-14T01:21:06.572Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '53470,53510p' LAT.txt | cut -c1-1000",
 "description": "Print Ernout-Meillet rex"
}
```


### [2026-09-14T01:21:06.628Z] TOOL RESULT

```
regnum, -t n.: rogne, royaume; d'ou regnS,-as , M.L.7173,7176 (formes
savantes); interregnum: interrbgne; sur lequel a ete refait interrex.
- regifugium: sacrum dicebant quo die rex Tarquinius fugerit e Roma.
P.F.363,3.
Le nom *reg- du "roi" eat de ces mots de 1 a langue politique et
religieuse qui se trouvent en i talo-celtique et en indo-iranien;
cf. lex. Sous forme verbale, la racine n'apparait que dans 1 'Inde:
ved .rasti et, sous forme thematique, plus frequente mais sans doute
secondaire, rajati "il rogne". Sous forme nominale, avec valeur de
nom d'agent, *reg- n'est attendu qu'au second terme de composes,
et en effet, raj- n'est courant en sanskrit qu 1 en cette position,
ainsi sam-raj- "roi suprSme"; au simple, la forme usuelle est rajan-
( nom. raja, a.cc. r 3 j anam, gen. rajflah , etc.) avec le feminin rajrli
"reine"; le gaulois a de meme beaucoup de noms propres du type corapose
de Dumno-rix. Toutefois le v^dique n'ignore pas tout a fait le nom.sg.
rat "roi" qui a pour correspondant lat .rex, irl.rt; la flexion du
type gen.lat. regis, irl.rtg n'apas de correspondant exact en sanskrit
au simple. Le feminin iri. rigain semble repondre a skr. rajrtt; lat.
regina (qu'on retrouve dans les dialectes italiques, marr. regen[ai]
dat."reginae") est nouveau, du type de gallina k c$t^ de gallus.
- Il est naturel de penser que rex appartient au groupe de rego,
comme dux au groupe de duco. L'emploi de ces themes racines pour
designer des agents est chose exceptionnelle; ce doit etre l'un des
archaismes des langues peripheriques du domaine indo-europ^en.
* t *
rhetor, -8rls m. : orateur, rheteur. Emprunt savant au gr. pr^xcop
(deja dans Cic.; rhetorici est dans Novius, rhetorisso dans Pomponius);
rhetorica conserve dans quelques parlers romans, M.L.73O7; et en
iri. retairic, rithoirg.
r(h)eubarbarum, -In.: rhubarbe. Mot tardif (isid. 17,9 qui cite un
un mot rheu "racine"?). M.L.7373.
r(h)ombus, -I m.: designe comme le gr. pop.| 3 oe (pup.( 3 oc) dont il
provient, tout obj et de forme circulaire ou losang^e: toupie, rouet,
losange; rhombe ou turbot. Emprunt d'abord savant, puis passe dans
la langue parlee, M.L.7393.; britt. *rwmp "tariere".
r(h) onchus: -y.roncus.rhythmus
- 10 13
rhythmus, -I m.: rythme, cadence. Emprunt siyant atteste de-
puia Varr. au gr. pi> 0 p, 6 s; rhythmicus (Cic.), passe par l'ecole en fr.
rime, M.L.7394b, et en iri. rithim.
rica, -ae f.: piece de drap, carree et bordee d'une frange, que
```


## [2026-09-14T01:21:10.918Z] TOOL CALL #81: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py",
 "description": "Inspect verify_check requirements"
}
```


### [2026-09-14T01:21:10.973Z] TOOL RESULT

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


## [2026-09-14T01:21:21.322Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"aiwi\\.raz\\|aiβi\\.raz\\|aibi.raz\\|ai&i.raz\\|aiwi-\\|raz-\" BRT.txt | grep -i \"raz\" | head -20 | cut -c1-250",
 "description": "Grep Bartholomae for aiwi-raz"
}
```


### [2026-09-14T01:21:21.390Z] TOOL RESULT

```
5636:loMi  . .  mnayml  iiimsni  •latra  (NP.)      ^,1  ^^^  3  y,  j^  (.umpflu.iiE'),  Dit.  ZA.  ,. V. /Ä  31;   — ^d^a   anyasSt   'iuris  aii      56S  {'qui  rend  viril'). xSudri  aa^riha  trm_mr,navainti  y-lS._,  .    ,      ,   „5.^
7758:•  j.  araz-UxÄa-  Adj.:  s.  unter  arhxua-. Ableit
7976:*)  Vgl.  Bd.  32.  y.  ha/i-äsir  äsraz-än  ml  mav patan  mavpat  iül,  IQO  säl  fas  (Aar)  den  lilarl. Eig.  'nach  Weiden  verlangend'.    —    ')  Hds. $al.v';  vgl.  Bd.  ja   10.
9895:•  j.  gaoSö.baraz-  f.  'Höhe  des  Ohrs': ä^ritlM  xsa'hrS.k^ntake  (sd.)  'zS  us.iäva- yuit{%±)  "^.46.
10179:•  j.*gavä8trya-varaz-"  Adj.  'der  landwirt- schaftliche Arbeit  verrichtet':  'isit  ilstryeiti anyö  ahmät  yS  hl  'varjs  daidU  aitahmäi "man  begehl  keine  Sunde  ausser  an  dem, der  einem  landwirtschaftliche  Arbeit  tut; dem
10265:•  j.,   g.   garaz-  V.   'klagen',     Praes. ,gii-}Z;  S  Jlg»r3z-  [,  25  g»r?zanä\.
12610:—  yqm  xsnütpm  räniiiyä  (sd.)  da  ..  aiAf aAvsAB  't»m  davBi{%A.)'^.$i.');  —  narym . .  aiavamm  *jas»nitm  aAmya  nmäne  mat avabyS    -inbyö'-'^  ydka    äiraz-a   V.  ij.  22;
13546:•  g.  (,  j.)  daraz-  f.  'Bande,  Fessel':  irata a"  dva��s  (sd.)  hvs  'za  (IS.)  *ituni^yaei maziits  Y,5J.8.
13871:hörig  dargebrachte  Verehning':  kö  huyesti  'J;  duiSvaräta-varaz- Adj.  'able  Werke, (sd.)  ks  y^sti  mam  zl  mainydt  yatat^m  \  U^'es  wirkend  t  frai;asayö  .  .  fravaz^U Vt/o  108  '  avaiiAe  narqm  asaoiiqm  qzartke 'varnqm
17179:•  j.  b^raz-  f.:  s.  unter  'banz-.
19008:•  j.  n^ra.baraz-  f.  'Mannshöhe,   -tiefe':
20077:•  j.  maraz-  V.  'streifend  berühren'.  Praes. 2  marsza-,  3  mfrpza-,  8  m^qz-''>.  —  Int m^rqidyäi.  [S,  noch  zu  mfr>^yumna-^
20833:—  AblSm.,!!,:  vazrpm..yaAmat  /laca/ra- tpnsaili  ar»rS  mainyul  Yt  10.  97;  97J,  7  y. 87,  Aog.  5<¥;  —  hukairjm  bar>zB  yahmat ml  hala  frazgahaife  ar)dvj  Ytf,  96;  — tistrlm  .  .  *yahmat  haca  b}r»zat  haosra- var?h
23003:•  j.,  g.  'varaz-  V.  'wirken'.  Praes.  1 vatvz- :  v»r>z-,  1 6  (Des.)  vJvarfsa-,  1 7  (Fut.)
23006:■varaz-
23597:•  j.  västryä-varaz-  Adj.  'Feldarbeit  ver- richtend,  in  der  Landwirtschaft  tätig': narqmca  näirinamca  apfrynäyäkanqmcit kainikanqmca  'zanqmca ''  ".  .  und  den Männern  und  Frauen  und  den  Knaben und  Mädchen  und  (Ü
23889:'  •  j.  vohvaraz-  Adj,  (fem,  'zt-)  'Gutes I  wirkend':  'tarn  asaonam  ..  'sinam  aiao- \tdnqm  Vr. //.  14.
25223:•  j.  raz-  V.  'richten'.  Fiaes.  30  (Iter.) rosaya-,  —  PPfP.  raSia-,  rasla-'\
27283:•  j.  sraosä-varaz-  m.  Name  des  siebenten und  geringsten,  mit  der  Kirchenpolizei (s.  No.  2)  betrauten  Unterpriesters  (ratav-); auch  die  Kirchenzucht  liegt  ihm  ob:  *>d'> aiwySxiayai  "der  Sr.  soll  die  Aufsicht fuhren" 
28320:•  j.  'zraz-dä-  kompV.  'vertrauen,  glauben'. Praes.  i  zrazda-.  —  Inf.  *sraiäatai-ia.
```


## [2026-09-14T01:21:59.742Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== TLM ===\"; grep -n \"aršta\\|arsta\\|ardu-\\|rāsta\\|rasta\" TLM.txt | head -8 | cut -c1-300; echo \"=== MON maharaja ===\"; grep -n \"مهاراجه\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -5 | cut -c1-300; echo \"=== MON riyal ===\"; grep -n \"ریال\" MON_part1.txt MON_part2.txt 2>/dev/null | head -4 | cut -c1-200",
 "description": "Grep Tolman and Moin"
}
```


### [2026-09-14T01:21:59.931Z] TOOL RESULT

```
=== TLM ===
138:67.  0atiy  darayavaus  xsaya0iya  tuvarn  [ka]  xsaya0iya  68.  h}ra aparam  ahy  martiya  [kya]  draujana  ahatiy  hyava  [zujrakara  +   + ahat-69.  iy  avaiy  rua  dausta  +   +   +   a   ufrastadiy  parsa
192:8.  0atiy  [Dara]yava-21)us  xsayatfiya  a"tar  ima  dahyava  martiya hya  agar[ta]2 3  aha  avam  u-22)bartam  abaram  hva  araika  aha avain  ufrastam  aparsam  vasn[a]  Auramazda-23)ha  ima  dahyava tyanaa  mana  data8  apariyaya"4 5  yaflasam  hacama  a&th-24)ya [ajvaftl  akunavaya”ta®
447:5.  0iltiy  Darayavaus  xsilya0i-37)ya  tuvam  ka  x[saya0iya  htya aparam3  aky4  haca  drauga  darsam  38)patipayauva  mart[iya  hya drau]jana  ahatiy  avam  ufrastam5  parsa  ya-39)diy  ava0a  man[iyil- hav']6  dahyausmaiy  duruva  ahati-40)y
452:5   ufrastam,  KT.  See  voc.
497:[naiy  a]da[m  na]  imaiy  tauraa  upariy  arstam1  upariy-65)[axsa- yai}r]2  naiy  sakauri[m3  naiy]  +   +   tunnuvatamai  zura  akunavam martiya  kya  hamata-66)xsata  mana  v^ifya  a]vam  ubartam a[ba]ram  hya  viyana[sa]ya5  avam  ufrasta-67)m  aparsam
498:14.  0atiy  Darayavaus  xsayafliya  tuvam  [ka]  xsayafliya  68)hya aparam6  ahy  martiya  [bya]  draujana  ahatiy  hyava  [zu]rakara++T ahat-69)iy  avaiy  ma  dausta  [bly]a8  ufrastadiy  parsa
503:1   arstam,  Foy,  Jn.,  KT.  See  voc.
830:6.  56)martiya  hya  Auramazdak-57)a  framana  hauvtaiy  gas- 58)ta  ma  0adaya  pa0im  59)tyam  rastam  ma  60)avarada  ma star ava1 5
=== MON maharaja ===
=== MON riyal ===
MON_part2.txt:29:قیمت دوره دوه جلدی: ۱۳۰/۰۰۰ ریال 
MON_part2.txt:12109:نخود معادل یک ریال کنونی. 
MON_part2.txt:41683:ماتریالیست: 15۱ (ص. .) ببر و 
MON_part2.txt:52158:۰ ریال در مدت یک سال. در مسایل
```


## [2026-09-14T01:22:06.046Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"rectitude\\|arstä\\|Ardumanis\\|ardumanis\" TLM.txt | head -8 | cut -c1-400",
 "description": "Grep Tolman lexicon"
}
```


### [2026-09-14T01:22:06.121Z] TOOL RESULT

```
489:13.  Says  Darius  the  king:  For  this  reason  Ahura  Mazda  bore me  aid  and  the  other  gods  which  are,  because  I   was  not  an enemy,  I   was  not  a   deceiver,  I   was  not  a   wrong-doer,  neither  I nor  my  family;  according  to  rectitude  [I  ruled]  nor  against  the slave(?)  nor  the  lowly(?)  did  I   exercise  oppression;3  the  man  who helped  my  house,  him  w
524:18.  Says  Darius  the  king:  These  (are)  the  men  who  were there  then  when  I   slew  Gaumata  the  Magian,  who  called  himself Bardiya;  then  these  men  cooperated  as  my  allies;  Intaphernes by  name,  the  son  of  Vayaspara,  a   Persian;  Otanes  byname,  the son  of  Thukhra,  a   Persian;  Gobryas  by  name,  the  son  of  Mar- donius,  a   Persian ;   Hydarnes  by  name, 
1156:ardumanis  (Elam,  [artumannis] ;   Bab.  a-ar-di-ma-ni-is),  m.  name  of one  of  the  allies  of  Darius  against  Gaumata.  Nom.  sg.  ar(duma]- n[is].  'fardu,  right ,   GAv.arazu,  Skt.  rju  -(-  "'manis,  mind ,   Av.  manah, Skt.  manas.  ^
1165:arsta  (for  arstata;  “the  sign  is  quite  clearly  r   and  not  b   on  the rock ”   KT),  f.  Rectitude.  Acc.  sg.  arstam,  Bh.  4.  13.  upariy  ars- tam upariy  +   +   +   +   ;   Elam,  sutur  ukku  bupa  git,  1   ruted  in  accordance with  the  ordinance ;   Bab.  ina  di-na-a-tu  a-si-ig-gu,  in  accordance  with the  laws  I   governed.  The  old  reading  of  Rawlinson  
1340:a   bold  supplement  which  I   suggested  (Vdt.  Stud.  1,  33)  in  Bh. 4.  1.  65,  upariy  arstam  upariy  [axsayaiy]  naiy,  with  rectitude  \   h ruled\ , as  corresponding  to  Elam,  sutur  ukku  hupa  git,  I   ruled  in  accord- ance with  the  ordinances;  Bab.  ina  di-na-a-tu  a-si-ig-gu,  in  accordance with  the  laws  I   governed.  Does  the  supplement  answer  in  any way
1766:vahauka  (Elam,  maukka),  m.  name  of  the  father  of  Ardumanish. Gen.  sg.  vahau[kahya],  Bh.  4.  18.
```


## [2026-09-14T01:30:13.739Z] TOOL CALL #85: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-417.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndata = {\n  \"pdf_page\": 417,\n  \"book_page\": 387,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Reg 1, Rěkto\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *h₃reǵ- 'to straighten, direct, make right' (Pokorny 1. reĝ- 854-857; Watkins reg-1); the to-participle *h₃reǵ-tó- / lengthened *rēǵ-to- 'directed, straight' = Nourai's 'Rěkto'\",\n      \"note\": \"Root, language label and gloss are all correct. Pokorny I 854-857 has 'reĝ-1: gerade richten, lenken, recken (strecken), aufrichten; recht, gerade'; Watkins/AHD reg-1 'to move in a straight line, with derivatives meaning to direct in a straight line, lead, rule' [Pok. 1. reg- 854]; Cheung 2007 s.v. *Hraz cites 'PIE *H3reg- to stretch, direct = LIV: 304 f. | Pok.: 854 f.'. Nourai's second headword 'Rěkto' is the verbal adjective seen in Lat. rēctus, Av. rāšta-, OP rāsta-, Gmc *rehtaz — Kent §93 states 'pIE *rēĝ-to- with lengthening of the vowel, Latin rēctus, Av. rāsta-, OP rāstam straight, right'. Two observations on the extraction/printing of this page: (a) the book prints the Old Persian word with a circumflex, 'arštâ : rectitude', while the JSON has 'aršta' (a lost diacritic — trivial, but the owner may want to normalise it); (b) between the Old Persian box and the right-hand column the printed page carries an EMPTY rectangle with no language label and no words, which the extraction (rightly) did not turn into a node — it is blank in the book itself, not lost text.\",\n      \"note_fa\": \"ریشهٔ «Reg 1, Rěkto» همان ریشهٔ هندواروپایی آغازین *h₃reǵ- «راست کردن، سو دادن، فرمان راندن» است که پوکورنی آن را در صفحهٔ ۸۵۴ تا ۸۵۷ زیر مدخل reĝ-1 آورده و واتکینز (پیوست ریشه‌های هندواروپایی فرهنگ American Heritage) نیز همان را با ارجاع به همان صفحه ثبت کرده است. صورت دوم یعنی Rěkto صفت مفعولی همین ریشه است (*rēǵ-to-) که در لاتین rēctus، در اوستایی rāšta-، در پارسی باستان rāsta- و در ژرمنی *rehtaz دیده می‌شود؛ کنت در بند ۹۳ دستور پارسی باستان دقیقاً همین برابری را می‌آورد. بنابراین نام ریشه، برچسب زبانی و معنای آن هر سه درست است و ادعای نورایی در این بخش پذیرفتنی است. تنها دو نکتهٔ فنی: در متن چاپی «arštâ» با کلاه آمده که در استخراج به «aršta» بدل شده، و در کنار جعبهٔ پارسی باستان یک مستطیل خالی چاپ شده که در خود کتاب هم تهی است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₃reǵ-\",\n        \"https://en.wiktionary.org/wiki/راست\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:854\", \"status\": \"supports\", \"note\": \"Pokorny IEW 'Root/lemma: reg-1' printed pages 854-857 (POK_full.txt lines 69560-69712, ending 'Page(s): 854-857'): material includes 'Avestan raz- (razayeiti, participle rāsta-, gr. ορεκτος, Latin rectus, Gothic raihts …) direct, aim, point, gerade richten, sort, order, arrange', 'rasman- m. n. Schlachtreihe (: gr. ὄρεγμα, Latin regimen)', 'Old Indic rāj- (Nom. Sg. rāt) king (= Latin rex, Old Irish rí)', 'Latin rego, -ere … rēx, regis king', 'Gothic raihts, Old English riht', 'Old English racu … Old High German rehho rake'. Exactly the spread of the chart.\"},\n        {\"ref\": \"KNT:206\", \"status\": \"supports\", \"note\": \"Kent, Old Persian, Lexicon printed p. 206 (KNT.txt form-feed leaf 231): '?rad- vb. \\\\'direct\\\\' Av. raz-, Skt. rāj- \\\\'reign\\\\', Lt. rego \\\\'I direct, rule\\\\', pIE *reg-; in uradana-, rāsta-.' and 'rāsta- adj. \\\\'straight, right, true\\\\' … pIE *rēkto-. Cf. arštā-.'\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"IEW I 854-857, reg-1\", \"stance\": \"supports\", \"note\": \"'reg-1 … gerade richten, lenken, recken, aufrichten; recht, gerade'; the Avestan, Old Indic, Latin, Celtic and Germanic material of the chart is all gathered there.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. reg-1\", \"stance\": \"supports\", \"note\": \"'reg-1. To move in a straight line, with derivatives meaning \\\"to direct in a straight line, lead, rule.\\\" … [Pok. 1. reg- 854.]' — with sections for *reg-to- (RIGHT), Latin regere (CORRECT, DIRECT, RECTUM, REGENT, REGIME, REGIMENT, REGION, SURGE), *rēǵ- (REX: REAL, REGAL, ROYAL; Sanskrit rāja: RAJ, RAJAH, MAHARAJAH), *rēǵ-olā (RAIL1, REGULAR, REGULATE, RULE) and *rog- (RAKE1, RECKON).\"},\n        {\"src\": \"CHEUNG\", \"where\": \"Etym. Dict. of the Iranian Verb, s.v. *Hraz (p. 196-198)\", \"stance\": \"supports\", \"note\": \"'*Hraz \\\\'to draw a line; to direct, richten\\\\' … «PIE *H3reg- \\\\'to stretch, direct\\\\' = LIV: 304 f. | Pok.: 854 f.'\"},\n        {\"src\": \"SYN\", \"where\": \"Buck 19.32 KING\", \"stance\": \"supports\", \"note\": \"'1. IE *rēǵ-, fr. the root *reg- in Lat. regere \\\\'direct, guide, rule\\\\' … Lat. rēx, gen. rēgis (> the Romance words) … Skt. (Vedic) rāj-, but commonly n-stem rājan-.'\"},\n        {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 362 ff. (cited by Pokorny and by Buck 19.32)\", \"stance\": \"supports\", \"note\": \"Pokorny closes reg-1 with 'References: WP. II 362 ff., WH. II 426 f., 432 f., 434 f.'; Buck 19.32 likewise cites 'Walde-P. 2.362 ff.' for IE *rēǵ- 'king'. The Bd. II OCR on disk is too damaged to quote the column verbatim (grep for 'gerade richten' returns only one stray line, 40873).\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"râsta; erezu; razma; aiwi-reg\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Avestan has the verb raz- 'to direct, make straight, arrange' (Bartholomae, AiW col. 1512: 'j. raz- V. \\\\'richten\\\\'. Praes. rāzaya-. — PPfP. rāšta-, rasta-'), so Nourai's 'râsta' is the participle rāšta-/rasta- 'directed, straight' — the exact cognate of Lat. rēctus and OP rāsta-. 'erezu' is Av. ərəzu- 'straight, upright' (Pokorny s.v. reg-1: 'rj̥ú-, Avestan ərəzu- \\\\'just, right\\\\' (in addition ərəzuš \\\\'finger\\\\')'), the same stem that Kent invokes for OP ardu-. 'razma' is the weak point: the attested Avestan noun is rasman- (nom. sg. rasma) 'Schlachtreihe, phalanx' (Bartholomae col. 1513, 'rasman- m., n. \\\\'Schlachtreihe, Phalanx\\\\''), with -sm-; the form razma with -zm- is the Old Persian shape reconstructed by Hübschmann, Persische Studien §612: 'Np. razm \\\\'Schlacht\\\\' ist = ap. *razma = zd. rasma \\\\'Schlachtreihe\\\\' (von Wzl. raz = idg. reǵ)', because IE *ǵm gives Av. sm but OP zm. So Nourai has printed the Old Persian reconstruction under the Avestan label. 'aiwi-reg' is likewise a normalisation rather than an attested Avestan lemma: Bartholomae records only ham-rāzaiia- (V 17.2) as a preverb compound of raz-, and Cheung's *Hraz lists the Iranian compounds as *ā-, *pati-, *fra-, *ui-, *ham- and *abi-Hraz (the last giving NP afrāxtan). An aiwi-/aibi- compound is a legitimate reconstruction of the preform of afrāxtan but is not itself quotable from the Avesta.\",\n          \"derivation_fa\": \"ستاک اوستایی raz- «راست کردن، سو دادن، سامان دادن» است و بارتولومه در ستون ۱۵۱۲ فرهنگ ایرانی باستان صفت مفعولی آن را rāšta-/rasta- آورده؛ پس «râsta»ی نورایی درست است و همان است که در لاتین rēctus و در پارسی باستان rāsta- دیده می‌شود. «erezu» همان ərəzu- «راست، مستقیم» است که پوکورنی زیر ریشهٔ reg-1 ثبت کرده و کنت نیز آن را همریشهٔ ardu- پارسی باستان می‌داند. اما «razma» با احتیاط پذیرفتنی است: صورت اوستایی rasman- (حالت فاعلی rasma) «صفِ رزم» با sm است و صورت razma با zm بازسازیِ پارسیِ باستان است که هوبشمان در بند ۶۱۲ «مطالعات ایرانی» پیشنهاد کرده، زیرا *ǵm هندواروپایی در اوستایی sm و در پارسی باستان zm می‌شود؛ یعنی نورایی صورت پارسی باستان را زیر برچسب اوستایی چاپ کرده است. «aiwi-reg» نیز مدخلی اوستایی نیست بلکه بازسازی پیشوند *abi-/aiwi- + raz- است که چونگ آن را برای «افراختن/افراشتن» فارسی می‌آورد؛ در اوستا تنها ham-rāzaiia- گواهی شده است. خلاصه: هستهٔ ادعا درست، ولی دو صورت آن بازسازی‌شده و برچسب زبانیِ razma نادقیق است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₃reǵ-\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:854\", \"status\": \"supports\", \"note\": \"Pokorny p. 854 (POK_full.txt line 69590 ff.) gives, under reg-1, both 'Avestan raz- (razayeiti, participle rāsta- …) direct, aim, point, gerade richten' and 'rasman- m. n. \\\\'Schlachtreihe\\\\' (: gr. ὄρεγμα, Latin regimen)' plus 'rj̥ú-, Avestan ərəzu- \\\\'just, right\\\\''. It does NOT print a form 'razma' and has no aiwi- compound.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"AiW col. ~1512-1513 (BRT.txt lines 25223-25224, 25216)\", \"stance\": \"partial\", \"note\": \"'j. raz- V. \\\\'richten\\\\'. Praes. 30 (Iter.) rāzaya-. — PPfP. rāšta-, rasta-' and 'j. rasman- m., n. \\\\'Schlachtreihe, Phalanx\\\\': spāδa … rāštəm rasma katarascit Yt 14.43'. Supports rāsta and the rasman- family; the -zm- form razma is not Avestan.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien §612, pp. 66-67\", \"stance\": \"supports\", \"note\": \"'Np. razm \\\\'Schlacht\\\\' ist = ap. *razma = zd. rasma \\\\'Schlachtreihe\\\\' (von Wzl. raz = idg. reǵ, vgl. skr. rāji \\\\'Reihe\\\\'). … Für idg. ǵm, ǵhm erscheint regelrecht zd. sm = ap. zm.' — i.e. Nourai's razma is Hübschmann's Old Persian reconstruction.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"s.v. *Hraz, p. 196-198\", \"stance\": \"partial\", \"note\": \"'*AVESTAN: YAv. raz- \\\\'to draw a line; to direct, richten\\\\' || (+ *ham-) …' — lists only a ham- compound for Avestan; the abi- compound appears first in New Persian afrāxtan/afrāstan.\"},\n            {\"src\": \"KNT\", \"where\": \"Kent p. 206\", \"stance\": \"supports\", \"note\": \"'rāsta- adj. \\\\'straight, right, true\\\\' … : Av. rāšta-, Turfan Phl. rāst \\\\'true\\\\', Lt. rēctus \\\\'straight\\\\', pIE *rēkto-.' — the Avestan participle is spelled rāšta-.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"râst «راست»; raj «رج»; radeh «رده (رژه)»; razm «رزم»; afrâštan «افراشتن ، افراختن (فرازیدن)»\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Four of the five words are sound, one is not. (a) râst «راست» 'right, straight, true' descends regularly Av. rāšta- / OP rāsta- > MP rāst (MacKenzie, CPD: 'rast [lst\\\\' | M rst, N ~] true, straight, direct') > NP rāst; Wiktionary reconstructs Proto-Iranian *Hraštáh < PIE *h₃reǵtós. Confirmed. (b) raj «رج» 'line, row' is what Horn no. 609 treats as 'reje, reze \\\\'Reihe\\\\'', comparing 'aw. razišta- \\\\'geradester\\\\'; ai. rājiṣṭha-' — i.e. the superlative of the same root, matching Skt. rājí- 'line, row' which Hübschmann also cites. Confirmed/plausible. (c) razm «رزم» 'battle': MP razm (MacKenzie 'razm [lcm | M rzm, N ~] battle'), Nyberg, Manual II 170 s.v. razm: 'battle … — Av. (1513 sq.) rasman- \\\\'battle-array, phalanx\\\\'; MPrthPrs rzm; Paz. NP razm', and Mo'in's footnote 8 in Borhan-e Qāṭeʿ on رزم derives it from Old Persian *razma = Avestan rasman-, comparing Skt. rāji 'row' and citing Hübschmann for Arm. razm/paterazm. Nourai's gloss 'battle (with rows of soldiers)' is exactly Hübschmann's semantic argument ('Schlachtreihe' > 'Schlacht'). Horn no. 612 dissents ('An Ableitung von aw. rasman- … zu denken … verbietet die Bedeutungsverschiedenheit', preferring Av. arəza- 'Schlacht'), but Hübschmann, Nyberg, Moʿin and the current Wiktionary/Proto-Iranian *Hrazman- line all take Nourai's side. Confirmed. (d) afrâštan / afrâxtan «افراشتن، افراختن» 'to raise, elevate' = *abi- + raz-: Cheung s.v. *Hraz, '(+ *abi-) NP afrāxtan, afrāstan/afrāz- \\\\'to raise\\\\'', MMP ʾbrʾst- 'to raise up, exalt'; Wiktionary: 'from Middle Persian abrāštan \\\\'to lift, raise\\\\''. Confirmed. (e) radeh «رده» 'a row of soldiers' is the DISPUTED item: it goes back to MP radag (MacKenzie: 'radag [ltk\\\\' | M rdg, N rada] line, rank, row'; Moʿin's footnote quotes Henning, BSOS IX.1 p. 87 for Pahlavi rdk 'سطر، صف، ردیف'), and Horn no. 609 expressly separates it from the reg- group — 'np. rede \\\\'Richtung, Linie, Reihe\\\\' scheint dagegen zu aw. ərəta-, arəta-, ai. r̥tá- \\\\'richtig, vollkommen\\\\' zu gehören' — while Wiktionary derives رده from PIE *h₂rey- 'to arrange, count'. A form from *reǵ- would have given *raz-/rāz-, not rad-. So رده (and the parade-word رژه built on it) belongs to *h₂er-/*h₂rey-, not to Reg 1. Because one word of the node is rejected by modern scholarship, the node takes the worst verdict.\",\n          \"derivation_fa\": \"از پنج واژهٔ این جعبه چهارتا درست است و یکی نادرست. «راست» از فارسی میانهٔ rāst (مکنزی: rast «راست، درست»)، از پارسی باستان rāsta- و اوستایی rāšta-، و در نهایت از *h₃reǵtós هندواروپایی؛ کاملاً پذیرفتنی است. «رج» را هرن در بند ۶۰۹ با اوستایی razišta- «راست‌ترین» و سنسکریت rājiṣṭha- می‌سنجد، پس همان ریشه است. «رزم» از فارسی میانهٔ razm است و نیبرگ در واژه‌نامهٔ «راهنمای پهلوی» (ج۲، ذیل razm) آن را از اوستایی rasman- «صف رزم» می‌گیرد؛ حاشیهٔ ۸ معین بر «رزم» در برهان قاطع نیز آن را «از پارسی باستان *razma = اوستا rasman-» می‌داند و به هوبشمان و ارمنی paterazm ارجاع می‌دهد. هرن (بند ۶۱۲) به دلیل اختلاف معنایی این اشتقاق را رد کرده و رزم را با اوستایی arəza- «نبرد» سنجیده، ولی رأی امروزی با هوبشمان و نیبرگ است. «افراشتن/افراختن» از *abi- + raz- است؛ چونگ زیر *Hraz صراحتاً «(+ *abi-) NP afrāxtan, afrāstan/afrāz-» را می‌آورد. اما «رده» را پژوهش امروزی رد می‌کند: این واژه از rdk/radag پهلوی است و هرن در همان بند ۶۰۹ آن را جدا کرده و به اوستایی ərəta-/arəta- و سنسکریت r̥tá- «راست، درست» (ریشهٔ *h₂er-) بازبسته است؛ اگر از ریشهٔ *reǵ- بود باید *راز/رز می‌شد نه رد. پس در این جعبه «رده» (و «رژه» ساختهٔ آن) نادرست جای گرفته است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/راست\",\n            \"https://en.wiktionary.org/wiki/رزم\",\n            \"https://en.wiktionary.org/wiki/افراشتن\",\n            \"https://en.wiktionary.org/wiki/رده\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:134\", \"status\": \"partial\", \"note\": \"Borhan-e Qāṭeʿ, the افراختن/افراشتن spread (BQT_v1_pages.txt form-feed leaves 362-363, ≈ printed p. 133-134): 'افراختن - بر وزن پرداختن، بمعنی برداشتن و بلند ساختن باشد'، 'افراشتن بروزن و معنی برداشتن، بلند ساختن باشد'، 'افرازیدن بمعنی بلند ساختن و افراختن باشد'. The page attests the word and Nourai's gloss 'to elevate' but carries no etymological footnote.\"},\n            {\"ref\": \"BQT:944\", \"status\": \"supports\", \"note\": \"Borhan-e Qāṭeʿ, the رده spread (BQT_v2_pages.txt leaf 404, ≈ printed p. 942-944): 'رده - بفتح اول و ثانی، صف و رستهٔ آدمی و حیوانات دیگر …' with Moʿin's footnote 6: 'در اوراق مانوی (پهلوی) rdk (سطر، صف، ردیف): Henning, A list of Middle Persian…, BSOS IX,1,p.87.' — supports the WORD and gloss 'row, rank', but Moʿin gives only the Pahlavi form, no link to raz-/*reǵ-.\"},\n            {\"ref\": \"BQT:946\", \"status\": \"supports\", \"note\": \"Borhan-e Qāṭeʿ, the رزم spread (BQT_v2_pages.txt leaf 405, ≈ printed p. 943-946): 'رزم = بفتح اول و سکون ثانی و میم، بمعنی جنگ و جدال باشد ۸' with Moʿin's footnote 8: 'از پارسی باستان *razma = اوستا rasman- … هندواروپایی …؛ قس: سانسکریت rāji (رده، صف) [رک: رده]؛ رک: هوبشمان؛ ارمنی paterazm (جنگ) و razm.' — precisely Nourai's arrow, glosses included.\"},\n            {\"ref\": \"HRN:136\", \"status\": \"partial\", \"note\": \"Horn, Grundriss p. 136 (HRN.txt leaf 158) is indeed the page with 'rej/reze' and 'rezm'. It SUPPORTS raj: '609. reje, reze \\\\'Reihe\\\\'. aw. razišta- \\\\'geradester\\\\'; ai. rājiṣṭha-'. It CONTRADICTS Nourai on razm: '612. rezm \\\\'Schlacht, Kampf\\\\'. aw. vergl. arəza- \\\\'Schlacht\\\\' … An Ableitung von aw. rasman- \\\\'Schlachtreihe\\\\' zu denken (s könnte statt z vor m stehen), verbietet die Bedeutungsverschiedenheit (s. No. 609).' And it contradicts him on رده: 'np. rede \\\\'Richtung, Linie, Reihe\\\\' scheint dagegen zu aw. ərəta-, arəta-, ai. r̥tá- \\\\'richtig, vollkommen\\\\' zu gehören.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD pp. 70, 71 (PHD.txt line 555, 557)\", \"stance\": \"supports\", \"note\": \"'radag [ltk\\\\' | M rdg, N rada] line, rank, row'; 'rast [lst\\\\' | M rst, N ~] true, straight, direct. ~ih: truth'; 'razm [lcm | M rzm, N ~] battle. ~-gāh battlefield'. All three Middle Persian links of the chart are attested; MacKenzie offers no PIE etymology.\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary s.v. razm (and pātrazm)\", \"stance\": \"supports\", \"note\": \"'razm [lcm] battle … — Av. (1513 sq.) rasman- \\\\'battle-array, phalanx\\\\'; MPrthPrs rzm; Paz. NP razm.' and 'pātrazm [p\\\\'tlcm] counterattack … — Arm. lw. paterazm \\\\'war, battle\\\\'.' Directly backs Nourai's razm ← Avestan 'lined up for a fight'.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien §612 (pp. 66-67)\", \"stance\": \"supports\", \"note\": \"'Np. razm \\\\'Schlacht\\\\' ist = ap. *razma = zd. rasma \\\\'Schlachtreihe\\\\' (von Wzl. raz = idg. reǵ, vgl. skr. rāji \\\\'Reihe\\\\'). Der Übergang von \\\\'Schlachtreihe\\\\' zu \\\\'Schlacht\\\\' ist, meine ich, begreiflich.'\"},\n            {\"src\": \"CHEUNG\", \"where\": \"s.v. *Hraz, pp. 196-198\", \"stance\": \"supports\", \"note\": \"'*NWIR: … (+ *abi-) NP afrāxtan, afrāstan/afrāz- \\\\'to raise\\\\' (LW ?), NP afrāz \\\\'exalted\\\\''; MMP ʾbrʾst- 'to raise up, exalt'; MP 'rʾst \\\\'correct, true\\\\''. Confirms afrāštan and rāst; no mention of رده under this root.\"},\n            {\"src\": \"HRN\", \"where\": \"nos. 609 and 612, p. 136\", \"stance\": \"contradicts\", \"note\": \"Horn separates رده from the root ('zu aw. ərəta-, arəta-, ai. r̥tá-') and rejects razm ← rasman- on semantic grounds; he supports only rej/reze.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Latin index, pdf pages 297, 300, 303\", \"stance\": \"supports\", \"note\": \"The index groups 'RIGHT (ENGLISH) / RIHT (OLD ENGLISH) / RASTA- (OLD PERSIAN) / RAST (PAHLAVI) / RASTAR (AVESTAN)' under راست, and 'RASMA (AVESTAN) / RAZMA (OLD PERSIAN) / RAZM (PAHLAVI) / PATERAZM, RAZM (ARMENIAN) / OREGMA (GREEK) / REGIMEN, REGERE (LATIN)' under رزم — the same cognate set Nourai draws, and the same Avestan rasma ~ OP razma distinction.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Old Persian\",\n          \"words\": \"aršta; ardu; râsta\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three are genuine Old Persian and all three are referred by Kent to the root *reǵ-. arštā- (the book prints 'arštâ') is the abstract 'rectitude' of DB 4.64 upariy arštām 'I ruled with rectitude': Kent p. 171 'arštā- sb. \\\\'rectitude\\\\': haplology for *aršta-tā-, abstract to aršta- \\\\'upright\\\\', pIE *r̥ǵ-ta-, with zero-grade to root *reǵ-, cf. Av. arštāt- \\\\'goddess of rectitude\\\\', OP ardu- in Ardumaniš-, rāsta-'. ardu- 'upright' is known only from the name Ardumaniš- 'Upright-minded': Kent p. 170-171 'From ardu- \\\\'upright\\\\', GAv. ərəzu-, Skt. r̥jú- + maniš-'; Tolman's lexicon has the same, '*ardu, \\\\'right\\\\', GAv. ərəzu, Skt. r̥jú + *maniš, \\\\'mind\\\\''. rāsta- is the ppp. 'straight, right, true' of DNa 59 / DNb 7, 11 (pathim tyam rāstam 'the straight path'), Kent p. 206 'rāsta- adj. \\\\'straight, right, true\\\\' … ptc. of ?rad-: Av. rāšta-, Turfan Phl. rāst \\\\'true\\\\', Lt. rēctus \\\\'straight\\\\', pIE *rēkto-'. The zero-grade *r̥ǵ-ta- > OP aršta- with anaptyctic a- and the regular Iranian *ǵt > št is exactly the phonology Kent states.\",\n          \"derivation_fa\": \"هر سه واژه پارسی باستانِ اصیل‌اند و کنت هر سه را به ریشهٔ *reǵ- بازمی‌گرداند. arštā- «راستی، درستکاری» در کتیبهٔ بیستون (بند ۴ سطر ۶۴) به کار رفته و کنت در صفحهٔ ۱۷۱ آن را کوتاه‌شدهٔ *aršta-tā-، مشتق از aršta- «راست‌ایستاده»، از *r̥ǵ-ta- هندواروپایی می‌داند و اوستایی aršta̅t- (ایزدبانوی راستی) را همریشهٔ آن می‌شمارد. ardu- «راست» تنها در نام Ardumaniš- «راست‌اندیش» دیده می‌شود و کنت (ص ۱۷۰-۱۷۱) و تولمن هر دو آن را با ərəzu- گاهانی و r̥jú- سنسکریت برابر می‌نهند. rāsta- صفت مفعولی «راست، درست» است (pathim tyam rāstam «راه راست» در نقش رستم) و کنت در صفحهٔ ۲۰۶ آن را از *rēkto- می‌گیرد و با rāšta- اوستایی، rāst پهلوی ترفانی و rēctus لاتین برابر می‌کند. تبدیل *ǵt ایرانی به št و افزودن a- آغازین به خوشهٔ آغازین دقیقاً همان است که کنت توصیف کرده. ادعای نورایی در این جعبه درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/راست\"],\n          \"ref_check\": [\n            {\"ref\": \"KNT:171\", \"status\": \"supports\", \"note\": \"Kent, Lexicon printed p. 171 (KNT.txt leaf 195, the page break '172' follows immediately): 'arštā- sb. \\\\'rectitude\\\\' (§80; §93): haplology for *aršta-tā- (§129), abstract to aršta- \\\\'upright\\\\' (§145), pIE *r̥ǵ-ta-, with zero-grade to root *reǵ- … cf. Av. arštāt- \\\\'goddess of rectitude\\\\', OP ardu- in Ardumaniš-, rāsta-.' The same spread (leaf 193) has 'Ardumaniš- … From ardu- \\\\'upright\\\\', GAv. ərəzu-, Skt. r̥jú- + maniš-'.\"},\n            {\"ref\": \"KNT:206\", \"status\": \"supports\", \"note\": \"Kent p. 206 (KNT.txt leaf 231): '?rad- vb. \\\\'direct\\\\': Av. raz-, Skt. rāj- \\\\'reign\\\\', Lt. rego \\\\'I direct, rule\\\\', pIE *reǵ-; in uradana-, rāsta-.' and 'rāsta- adj. \\\\'straight, right, true\\\\' … pIE *rēkto- … Cf. arštā-.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KNT\", \"where\": \"pp. 170-171, 206 and §93 (KNT.txt line 2639)\", \"stance\": \"supports\", \"note\": \"§93: 'pIE *reǵ- \\\\'direct\\\\': *rēǵ-to- with lengthening of the vowel, Latin rēctus, Av. rāsta-, OP rāstam \\\\'straight, right\\\\'.'\"},\n            {\"src\": \"TLM\", \"where\": \"Tolman, Ancient Persian Lexicon, s.vv. ardumaniš, aršta (TLM.txt lines 1156, 1165) and text DNa (line 830)\", \"stance\": \"supports\", \"note\": \"'ardumaniš … *ardu, \\\\'right\\\\', GAv. ərəzu, Skt. r̥jú + *maniš, \\\\'mind\\\\''; 'aršta (for arštāta) … f. Rectitude. Acc. sg. arštām, Bh. 4.13'; and the DNa passage 'paθim tyam rāstam' for rāsta-.\"},\n            {\"src\": \"BRT\", \"where\": \"AiW col. 1512 s.v. raz- and col. 202 arštāt-\", \"stance\": \"supports\", \"note\": \"'raz- V. \\\\'richten\\\\' … PPfP. rāšta-, rasta-' is the Avestan counterpart of OP rāsta-; Bartholomae's arštāt- is the goddess Kent compares for arštā-.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"maha-râjâ\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sanskrit mahā-rāja- 'great king' is a bahuvrīhi/tatpuruṣa of mahā- 'great' (PIE *meǵh₂-, hence Nourai's cross-reference ☞Meg) and rājan-/rāj- 'king'. The second member is the direct descendant of the lengthened grade *h₃rēǵ-s that also gives Lat. rēx and OIr. rí: Pokorny s.v. reg-1 'Old Indic rāj- (Nom. Sg. rāṭ) \\\\'king\\\\' (= Latin rex, Old Irish rí …), rājan- ds., rājñī \\\\'Königin, Fürstin\\\\', rājati \\\\'is king, herrscht\\\\''; Buck 19.32 'IE *rēǵ- … Skt. (Vedic) rāj-, but commonly n-stem rājan-'; Watkins reg-1 II.3 'Suffixed form *rēǵ-en- in Sanskrit rāja, rājan-, king, rajah … MAHARAJAH, MAHARANI'. Placing the compound on the reg- chart (with the meg- cross-reference for the first element) is exactly right.\",\n          \"derivation_fa\": \"«مهاراجه» در سنسکریت mahā-rāja- «شاه بزرگ» است: mahā- «بزرگ» از *meǵh₂- هندواروپایی (از همین رو نورایی به ریشهٔ Meg ارجاع داده) و rāja-/rājan- «شاه» که بازماندهٔ صورت کشیدهٔ *h₃rēǵ-s است، همان که در لاتین rēx و در ایرلندی کهن rí دیده می‌شود. پوکورنی زیر reg-1 می‌نویسد: «هندی باستان rāj- (حالت فاعلی rāṭ) \\\\'شاه\\\\' = لاتین rex، ایرلندی کهن rí» و باک در بند ۱۹٫۳۲ همین را تکرار می‌کند. واتکینز نیز در بخش دوم مدخل reg-1 صریحاً MAHARAJAH را ذیل rāja سنسکریت می‌آورد. پس جای دادن این ترکیب در این نمودار با ارجاع بخش نخست آن به ریشهٔ Meg درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/maharaja\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:785\", \"status\": \"partial\", \"note\": \"Nourai's page number points to the 1975 New College main dictionary (s.v. maharajah), which is not on disk; but the Watkins appendix that the reference ultimately rests on does say it: 'reg-1 … II.3. Suffixed form *rēǵ-en- in Sanskrit rāja, rājan-, king, rajah (feminine rājñī, queen, rani), and rājati, he rules: RAJ, RAJAH, (RANI), (RYE2); MAHARAJAH, MAHARANI.' The index also lists 'MAHARAJAH meg-' for the first element — which is Nourai's own ☞Meg cross-reference.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW I 855 (reg-1)\", \"stance\": \"supports\", \"note\": \"'Old Indic rāj- (Nom. Sg. rāṭ) \\\\'king\\\\' (= Latin rex, Old Irish rí, s. also Gothic reiks), rājan- ds., rājñī \\\\'Königin\\\\' … rājya- \\\\'royal\\\\' (= Latin regius).'\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 19.32 KING\", \"stance\": \"supports\", \"note\": \"'1. IE *rēǵ- … Skt. (Vedic) rāj-, but commonly n-stem rājan-; cf. Goth. reiks \\\\'ruler\\\\', loanword fr. Celtic.'\"},\n            {\"src\": \"HJB\", \"where\": \"Hobson-Jobson p. 754, s.v. RAJA, RAJAH\", \"stance\": \"supports\", \"note\": \"'RAJA, RAJAH, s. Skt. rājā, \\\\'king\\\\'. … (Ibn Batuta, it will be seen, regards the words for king in India and in Spain as identical, in which he is fundamentally right.)' — Yule's aside is precisely the rājā ~ Sp. rey (< rēx) cognation this chart draws.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"Mâhârâjeh «مهاراجه»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian «مهاراجه» is a modern culture-word, not an inherited form: it is the Indian title mahārāja(ḥ), taken into Persian in its Indo-Persian shape (Hindi/Urdu महाराजा mahārājā), the final -eh «ـه» being the ordinary Persian rendering of the Indic final -ā. Persian had used it since Mughal times for Hindu princes and, in the 19th-20th c., it was reinforced by European usage (English maharaja, first attested 1698 per Wiktionary). The route therefore is Sanskrit mahā-rāja- > Middle Indic/Hindi mahārājā > Persian māhārāje; it is a borrowing, not a descent, and the chart's arrow from the Sanskrit box is correct in substance. Nourai gives no reference and no gloss for this box.\",\n          \"derivation_fa\": \"«مهاراجه» در فارسی وام‌واژه‌ای نوست، نه صورتی موروثی: عنوان هندی mahārāja(ḥ) است که از راه هندی/اردو (महाराजा mahārājā) به فارسی رسیده و «ـه» پایانی برگردان معمول ـā هندی است. از روزگار گورکانیان در فارسی برای شاهزادگان هندو به کار می‌رفته و در سده‌های نوزدهم و بیستم با کاربرد اروپایی (انگلیسی maharaja، نخستین گواهی ۱۶۹۸ به گفتهٔ ویکی‌واژه) دوباره رواج یافته است. پس مسیر چنین است: سنسکریت mahā-rāja- ← هندی mahārājā ← فارسی مهاراجه؛ وام‌گیری است نه تحول آوایی درون‌زبانی، و پیکان نمودار از نظر محتوا درست است. نورایی برای این جعبه نه مأخذی آورده و نه معنایی.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/maharaja\"],\n          \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai cites no reference for this box.\"}],\n          \"consulted\": [\n            {\"src\": \"HJB\", \"where\": \"Hobson-Jobson p. 754 s.v. RAJA, RAJAH\", \"stance\": \"supports\", \"note\": \"'The word spread with Hindu civilisation to the eastward, and survives in the titles of Indo-Chinese sovereigns, and in those of Malay and Javanese chiefs and princes' — the same kind of title-borrowing that carried مهاراجه into Persian.\"},\n            {\"src\": \"MON\", \"where\": \"MON_part1/part2 (grep 'مهاراجه')\", \"stance\": \"silent\", \"note\": \"The OCR of Moʿin's lexicon volumes on disk returns no hit for مهاراجه; the word belongs to the aʿlām volumes (5-6), which are not in the local text.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 index\", \"stance\": \"supports\", \"note\": \"'MAHARAJAH meg-' and, under reg-1 II.3, 'MAHARAJAH, MAHARANI' among the descendants of Sanskrit rāja — i.e. the compound is exactly meg- + reg-.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Germanic\",\n          \"words\": \"rehtaz; rakô\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *rehtaz 'right, straight' is the regular outcome of PIE *h₃reǵ-tó- (Grimm's law: *ǵ > Gmc *k, and the cluster *kt > ht), whence Goth. raihts, OE riht, OHG reht; Pokorny lists it with Av. rāsta- and Lat. rēctus. *rakō 'rake' is the o-grade *rog-eh₂ 'an implement with straight teeth', OE raca/racu, OHG rehho, ON reka. Watkins states both explicitly: 'Suffixed form *reg-to- in Germanic *rehtaz in Old English riht, right, just, correct, straight: RIGHT' and 'O-grade form *rog-. 1. Germanic *rakō in Old English raca, racu, rake (implement with straight pieces of wood): RAKE1'. Nourai's forms and glosses match Watkins letter for letter.\",\n          \"derivation_fa\": \"*rehtaz ژرمنی آغازین «راست، درست» بازتاب منظم *h₃reǵ-tó- هندواروپایی است: بر پایهٔ قانون گریم، *ǵ هندواروپایی در ژرمنی به k بدل می‌شود و خوشهٔ *kt به ht؛ از همین رو گوتی raihts، انگلیسی کهن riht و آلمانی علیای کهن reht. *rakō نیز صورت درجهٔ o یعنی *rog-eh₂ است به معنی «ابزارِ دندانه‌راست» که انگلیسی کهن raca/racu و آلمانی علیای کهن rehho «شن‌کش» از آن است. واتکینز هر دو را عیناً ثبت کرده و صورت‌ها و معناهای نورایی واژه‌به‌واژه با او می‌خواند. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₃reǵ-\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. reg-1: 'I. Basic form *reg-. 1. Suffixed form *reg-to- in Germanic *rehtaz in Old English riht, right, just, correct, straight: RIGHT.' and 'IV. O-grade form *rog-. 1. Germanic *rakō in Old English raca, racu, rake (implement with straight pieces of wood): RAKE1.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW I 856\", \"stance\": \"supports\", \"note\": \"'Gothic raihts, Old Icelandic rettr, Old English riht, Old Saxon Old High German reht \\\\'right, straight\\\\' (= Avestan rāsta- etc.)'; 'Old Icelandic reka, Old High German rehho \\\\'rake\\\\', Old Saxon reka f. \\\\'rake\\\\', Old English racu, Swedish raka.'\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. rex (and right, rake)\", \"stance\": \"supports\", \"note\": \"s.v. rex: 'rel. to regere … cogn. with OI. rāj-, rājan- \\\\'king\\\\', OIr. rí … fr. I.-E. base *reg-, \\\\'to stretch, straighten; straight, right; to lead, direct, rule, reign\\\\'.'\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"right, rich, rake\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"right < OE riht < Gmc *rehtaz < *h₃reǵ-tó- (Watkins reg-1 I.1) — confirmed. rake < OE raca/racu < Gmc *rakō < o-grade *rog- (Watkins reg-1 IV.1) — confirmed. rich is the one word that does not sit under the plain Germanic node as drawn: Watkins puts it under the LENGTHENED grade *rēǵ- and, more importantly, treats the Germanic word as a Celtic loan — 'II. Lengthened-grade form *rēǵ-, Indo-European word for a tribal king. 1. Celtic suffixed form *rīg-yo- in Germanic *rīkja- in … c. Old English rīce, strong, powerful: RICH'; Pokorny says the same ('through borrowing from dem Celtic vor the Mediaverschiebung: Gothic reiks … Old High German rīhhi, Old English rīce \\\\'mighty, vornehm, rich\\\\''), and Buck 19.32 adds 'cf. Goth. reiks \\\\'ruler\\\\', loanword fr. Celtic'. Modern English rich was further re-shaped by Old French riche (itself Germanic). So the root is right but the intermediate history is Celtic → Germanic → (with French reinforcement) English, not the simple Gmc *rehtaz/*rakō box the arrow comes out of.\",\n          \"derivation_fa\": \"«right» از انگلیسی کهن riht، از ژرمنی *rehtaz، از *h₃reǵ-tó- می‌آید و «rake» از انگلیسی کهن raca/racu، از ژرمنی *rakō با درجهٔ آوایی o یعنی *rog-؛ هر دو بی‌چون‌وچرا درست‌اند. اما «rich» با احتیاط پذیرفتنی است: واتکینز آن را زیر صورت کشیدهٔ *rēǵ- می‌آورد و ژرمنی *rīkja- را وام‌واژه‌ای از سلتی *rīg-yo- می‌داند؛ پوکورنی نیز می‌نویسد که این خانواده «پیش از جابه‌جایی صامت‌ها از سلتی وام گرفته شده» و باک هم گوتی reiks را وام سلتی می‌شمارد. افزون بر این، صورت امروزی انگلیسی زیر تأثیر riche فرانسهٔ کهن بازساخته شده است. پس ریشه همان است ولی راه آن سلتی ← ژرمنی ← انگلیسی (با تقویت فرانسوی) است، نه شاخهٔ سادهٔ *rehtaz/*rakō که پیکان از آن بیرون آمده.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₃reǵ-\"],\n          \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai cites no reference for this box; the parent Germanic box carries 'AHD'.\"}],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. reg-1, sections I.1, II.1c, IV.1\", \"stance\": \"partial\", \"note\": \"RIGHT and RAKE1 are under the basic and o-grade forms of reg-1; RICH is under the lengthened grade via 'Celtic suffixed form *rīg-yo- in Germanic *rīkja-'. Index lines confirm 'RIGHT reg-1', 'RAKE1 reg-1', 'RICH reg-1'.\"},\n            {\"src\": \"POK\", \"where\": \"IEW I 856\", \"stance\": \"partial\", \"note\": \"'through borrowing from dem Celtic vor the Mediaverschiebung: Gothic reiks \\\\'ruler, vornehm, mighty\\\\' (Celtic rīg-s) … Old High German rīhhi, Old Saxon rīki, Old English rīce (Celtic *rīgio-) \\\\'mighty, vornehm, rich\\\\', Modern High German reich.'\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 19.32\", \"stance\": \"partial\", \"note\": \"'cf. Goth. reiks \\\\'ruler\\\\', loanword fr. Celtic.'\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Latin\",\n          \"words\": \"regere; regula; surgere\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin regō, regere 'to keep straight, guide, rule' is the thematic present of *h₃reǵ- (ppp. rēctus < *rēǵ-to-); rēgula 'straight piece of wood, ruler, rule' is the instrument noun *rēǵ-olā from the same stem; surgere 'to rise' is a contraction of *subs-regere (sub + regere) 'to direct/raise from below'. Watkins: 'Latin regere, to lead straight, guide, rule (past participle rēctus) : … SURGE' and 'III. Suffixed lengthened-grade form *rēǵ-olā in Latin regula, straight piece of wood, rod: RAIL1, REGLET, REGULAR, REGULATE, RULE'. Klein s.v. surge: 'fr. L. surgere, \\\\'to raise, erect; to rise\\\\', contraction of *subs-regere, fr. sub- and regere'. Nourai's three Latin headwords and glosses are accurate; 'straight bar' for regula and 'to surge' for surgere are both fair renderings.\",\n          \"derivation_fa\": \"فعل لاتینی regō/regere «راست نگه داشتن، راهبری کردن، فرمان راندن» صورت مضارعِ درون‌مایه‌دارِ همان ریشهٔ *h₃reǵ- است و صفت مفعولی آن rēctus از *rēǵ-to- می‌آید. rēgula «چوب راست، خط‌کش، قاعده» اسم ابزار از همین ستاک است (*rēǵ-olā) و surgere «برخاستن» کوتاه‌شدهٔ *subs-regere (sub «زیر» + regere) به معنی «از پایین راست کردن/برخیزاندن» است؛ کلاین در مدخل surge همین را می‌گوید. واتکینز نیز هر سه را زیر reg-1 می‌آورد. پس صورت‌ها و معناهای نورایی در این جعبه درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₃reǵ-\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. reg-1: '2. Latin regere, to lead straight, guide, rule (past participle rēctus, hence adjective rēctus, right, straight): REALM, RECTITUDE, RECTO, RECTOR, RECTUM, REGENT, REGIME, REGIMENT, REGION; CORRECT, DIRECT, ERECT, RECTANGLE, RECTIFY, RECTILINEAR, RISORGIMENTO, SURGE.' and 'III. Suffixed lengthened-grade form *rēǵ-olā in Latin regula, straight piece of wood, rod: RAIL1, REGLET, REGULAR, REGULATE, RULE.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. rex / rego\", \"stance\": \"supports\", \"note\": \"'Il est naturel de penser que rex appartient au groupe de rego, comme dux au groupe de duco' — the same root-family for regere, rēx and their derivatives.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.vv. surge, rail, rule, regime\", \"stance\": \"supports\", \"note\": \"'surge … fr. L. surgere, \\\\'to raise, erect; to rise\\\\', contraction of *subs-regere, fr. sub- and regere'; 'rail, n., bar … fr. L. regula, \\\\'a straight piece of wood, ruler; rule\\\\', fr. regere'; 'rule, v. … fr. L. regulare, \\\\'to direct, regulate\\\\', fr. regula'.\"},\n            {\"src\": \"POK\", \"where\": \"IEW I 855-856\", \"stance\": \"supports\", \"note\": \"'Latin rego, -ere, rēxī, rectum … \\\\'gerade richten, steer, rule, reign\\\\' … regula \\\\'Richtholz, line; Richtschnur, lath\\\\' … about pergo, porrigo, surgo.'\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"A pass-through box with no words printed: it stands for the Old/Modern French continuations of Latin regere and rēgula that feed both the Persian and the English boxes below — OF drecier / F. dresser and adrecier / adresser (< VL *dīrēctiāre, *ad-dīrēctiāre, to L. dīrēctus, ppp. of dīrigere < regere), F. régime (< L. regimen), F. escorte (< It. scorta < scorgere < VL *excorrigere < corrigere < regere), OF/MF reille, F. rail 'bar' and F. règle (< L. rēgula), and OF reuler > F. régler / régule. All of these are the immediate donors of the Persian and English words in the two daughter boxes, so the empty French box is factually justified even though the author printed nothing in it.\",\n          \"derivation_fa\": \"این جعبه تهی است و در کتاب واژه‌ای در آن چاپ نشده؛ کار آن تنها واسطه‌گری است: بازماندگان فرانسویِ regere و rēgula لاتین را نشان می‌دهد که هم به جعبهٔ فارسی و هم به جعبهٔ انگلیسیِ زیرین خوراک می‌دهند — یعنی dresser و adresser فرانسوی (از *dīrēctiāre و *ad-dīrēctiāre لاتین عامیانه، از dīrēctus، صفت مفعولی dīrigere)، régime (از regimen)، escorte (از scorta ایتالیایی، از scorgere، از *excorrigere)، reille/rail «میله» و règle (هر دو از rēgula). چون همین صورت‌ها وام‌دهندهٔ مستقیم واژه‌های فارسی و انگلیسیِ دو جعبهٔ پایین‌اند، خالی بودن جعبه اشکال محتوایی ایجاد نمی‌کند.\",\n          \"sources\": [],\n          \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai cites no reference for this pass-through box.\"}],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.vv. dress, address, regime, escort, rail, rule\", \"stance\": \"supports\", \"note\": \"'dress … fr. OF. (= F.) dresser, fr. VL. *directiare, fr. L. directus, pp. of dirigere'; 'address … F. adresser, fr. OF. adrecier, fr. a- \\\\'to\\\\' and drecier (F. dresser), \\\\'to direct\\\\''; 'regime … F. régime, fr. OF. regimen, fr. L. regimen'; 'escort … F. escorte, fr. It. scorta, fr. scorgere … fr. VL. *excorrigere'; 'rail, n., bar … fr. MF. reille … fr. L. regula'.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. reg-1, sections 2 and III\", \"stance\": \"supports\", \"note\": \"The French-mediated English words REGIME, REGIMENT, REGION, RAIL1, REGULAR, REGULATE, RULE are all listed there.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"Persian\",\n          \"words\": \"âdres «آدرس»; režîm «رژیم»; (extra: اسکورت ، ریل ، رگل)\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All five are 19th-20th century European loans taken into Persian through French, which is why Moʿin tags them [فر.]. آدرس ādres < F. adresse (< adresser < OF adrecier < VL *ad-dīrēctiāre < L. dīrēctus < dīrigere < regere); Moʿin: 'آدرس (رِ) [ فر. ] ۱ - نشانی خانه، اداره و مانند آن، نشانی؛ ۲ - عنوان و نام کس یا جایی بر پشت پاکت'. رژیم režim < F. régime (< L. regimen 'direction, government', from regere); Moʿin: 'رژیم (رِ) [ فر. ] (اِ.) ۱ - حکومت، نوع حکومت. ۲ - دستورالعمل برای غذا خوردن. ۳ - طریقه، روش، قاعده' — exactly Nourai's double gloss 'government, diet'. اسکورت eskort < F. escorte (< It. scorta < VL *excorrigere); Moʿin has the headword 'اسکورت: دسته‌ای از سربازان مسلح که در التزام رکاب شاه، رئیس‌جمهور و غیره باشد'. ریل reyl 'rail' < F. rail, which French itself re-borrowed from English rail (< MF reille < L. rēgula) — a round trip Latin > Old French > English > French > Persian. رگل regl 'menstruation' < F. règle (< L. rēgula), the French medical euphemism 'les règles'. Every step is loan-transmission, not inheritance, and the chart draws it that way.\",\n          \"derivation_fa\": \"هر پنج واژه وام‌واژه‌های اروپایی سدهٔ سیزدهم و چهاردهم خورشیدی‌اند که از راه فرانسه به فارسی آمده‌اند و معین در فرهنگ فارسی همه را با نشان [فر.] می‌آورد. «آدرس» از adresse فرانسوی (از adresser، از *ad-dīrēctiāre لاتین عامیانه، از dīrēctus، از dīrigere، از regere)؛ معین: «آدرس (رِ) [فر.] ۱ـ نشانی خانه، اداره و مانند آن». «رژیم» از régime فرانسوی (از regimen لاتین، از regere)؛ معین: «[فر.] (اِ.) ۱ـ حکومت، نوع حکومت. ۲ـ دستورالعمل برای غذا خوردن» که دقیقاً همان دو معنای نورایی است. «اسکورت» از escorte فرانسوی (از scorta ایتالیایی، از *excorrigere). «ریل» از rail فرانسوی که خودِ فرانسه آن را از انگلیسی بازستانده و انگلیسی از reille فرانسهٔ میانه و آن از rēgula لاتین گرفته است — یک رفت‌وبرگشت کامل. «رگل» از règle فرانسوی (از rēgula) در معنای پزشکی «قاعدگی». همهٔ این‌ها وام‌گیری است نه تحول درون‌زبانی، و نمودار هم همین را نشان می‌دهد؛ ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://vajehyab.com/moein/آدرس\",\n            \"https://abadis.ir/fatofa/رژیم/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON\", \"status\": \"supports\", \"note\": \"Moʿin, Farhang-e Fārsi, read through vajehyab/abadis: آدرس '(رِ) [ فر. ] ۱ - نشانی خانه، اداره و مانند آن، نشانی (فره). ۲ - عنوان و نام کس یا جایی بر پشت پاکت و مانند آن'; رژیم '(رِ) [ فر. ] (اِ.) ۱ - حکومت، نوع حکومت. ۲ - دستورالعمل برای غذا خوردن. ۳ - طریقه، روش، قاعده'. The tag [فر.] = French is exactly Nourai's arrow.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt line 12942 (اسکورت) and the online Moʿin entries for آدرس / رژیم\", \"stance\": \"supports\", \"note\": \"'اسکورت: … دسته‌ای از سربازان مسلح که در التزام رکاب شاه، رئیس جمهور و غیره باشد' — the printed lexicon carries the French loan as a headword (the local OCR loses the bracketed [فر.] tags, which the online text preserves).\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.vv. address, regime, escort, rail\", \"stance\": \"supports\", \"note\": \"Gives the French etyma that Persian borrowed: 'address … F. adresser, fr. OF. adrecier'; 'regime … F. régime, fr. OF. regimen, fr. L. regimen'; 'escort, n. … F. escorte, fr. It. scorta, fr. scorgere, \\\\'to show, to guide\\\\', fr. VL. *excorrigere'; 'rail, n., bar … fr. MF. reille, \\\\'bar, rail\\\\', fr. OF. reille, fr. L. regula'.\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"English\",\n          \"words\": \"escort, address, regime, regular, rail, rule\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All six reached English through French from Latin regere / rēgula. escort < F. escorte < It. scorta, from scorgere < VL *excorrigere (ex- + corrigere 'to make straight') — Klein s.v. escort. address < ME adressen < F. adresser < OF adrecier = a- + drecier < VL *ad-dīrēctiāre, to L. dīrēctus < dīrigere < regere — Klein s.v. address. regime < F. régime < OF regimen < L. regimen 'direction, rule' — Klein s.v. regime. regular < L. rēgulāris < rēgula; rail (the bar) < ME raile < MF reille < L. rēgula 'straight piece of wood'; rule < ME reulen < OF reuler < L. rēgulāre < rēgula — Klein s.vv. rail, rule. Watkins lists RAIL1, REGLET, REGULAR, REGULATE, RULE under *rēǵ-olā and REGIME under Latin regere; ESCORT and ADDRESS are simply absent from the 1985 index, which is why the AHD citation is only partial.\",\n          \"derivation_fa\": \"هر شش واژه از راه فرانسه و از لاتین regere/rēgula به انگلیسی رسیده‌اند. escort از escorte فرانسوی، از scorta ایتالیایی، از scorgere و آن از *excorrigere لاتین عامیانه (ex + corrigere «راست کردن»). address از adresser فرانسوی، از adrecier فرانسهٔ کهن، یعنی a- + drecier، از *ad-dīrēctiāre، از dīrēctus. regime از régime فرانسوی، از regimen لاتین «راهبری، فرمانروایی». regular از rēgulāris، rail از reille فرانسهٔ میانه و rule از reuler فرانسهٔ کهن، هر سه بازگشته به rēgula «چوب راست، خط‌کش». کلاین همهٔ این زنجیره‌ها را واژه‌به‌واژه می‌آورد و واتکینز نیز RAIL، REGULAR، REGULATE، RULE و REGIME را ذیل reg-1 ثبت کرده است؛ تنها ESCORT و ADDRESS در فهرست چاپ ۱۹۸۵ نیامده‌اند. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins 1985 index has 'RAIL1 reg-1', 'REGULAR reg-1', 'REGULATE reg-1', 'RULE' under the *rēǵ-olā section of reg-1, and 'REGIME' among the Latin regere derivatives. ESCORT and ADDRESS do not appear in the 1985 index at all (grep returns nothing), so for those two the reference cannot be said to support the arrow.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.vv. escort, address, regime, rail, rule\", \"stance\": \"supports\", \"note\": \"'escort, n. … F. escorte, fr. It. scorta, fr. scorgere, \\\\'to show, to guide\\\\', fr. VL. *excorrigere, fr. 1st ex- and L. corrigere, \\\\'to make straight, set right\\\\''; 'address, tr. v. — ME. adressen, \\\\'to raise, adorn\\\\', F. adresser, fr. OF. adrecier, fr. a-, \\\\'to\\\\', and drecier (F. dresser), \\\\'to direct\\\\''; 'rule, tr. and intr. v. — ME. reulen, rulen, fr. OF. reuler, riuler, fr. L. regulare, \\\\'to direct, regulate\\\\', fr. regula'.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. reg-1, section III\", \"stance\": \"supports\", \"note\": \"'III. Suffixed lengthened-grade form *rēǵ-olā in Latin regula, straight piece of wood, rod: RAIL1, REGLET, REGULAR, REGULATE, RULE.'\"}\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"English\",\n          \"words\": \"direct, dress, correct, source\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"direct < L. dīrēctus, ppp. of dīrigere (dis- + regere) 'to set straight' — Watkins lists DIRECT under Latin regere. correct < L. correctus, ppp. of corrigere (com- + regere) 'to make straight' — Watkins lists CORRECT there too. dress < ME dressen < OF/F dresser < VL *dīrēctiāre, a verb built on dīrēctus, Klein: 'dress, tr. and intr. v. — ME. dressen, \\\\'to direct, prepare; to dress\\\\', fr. OF. (= F.) dresser, fr. VL. *directiare, fr. L. directus, pp. of dirigere'. source < ME sours < OF sorse/surse, the feminine past participle of sordre 'to rise' used as a noun, from L. surgere (< *subs-regere), Klein: 'source, n. — ME. sours, fr. OF. sorse, surse, sorce (later source), fem. of sors, pp. of sordre, \\\\'to rise\\\\', used as a noun, fr. L. surgere, \\\\'to rise\\\\'.' The semantic step 'rising (of a stream)' > 'spring, origin' is the ordinary one. Note that the parent box for this node is the Latin box (regere, regula, surgere) directly, without the French box — which is right for direct and correct but slightly loose for dress and source, which did pass through French.\",\n          \"derivation_fa\": \"«direct» از dīrēctus لاتین، صفت مفعولی dīrigere (dis- + regere) «راست کردن»؛ «correct» از correctus، صفت مفعولی corrigere (com- + regere)؛ واتکینز هر دو را ذیل regere آورده است. «dress» از dressen انگلیسی میانه، از dresser فرانسوی، از *dīrēctiāre لاتین عامیانه که بر پایهٔ dīrēctus ساخته شده (کلاین). «source» از sours انگلیسی میانه، از sorse فرانسهٔ کهن که صفت مفعولی مؤنث فعل sordre «برخاستن» است و آن از surgere لاتین (= *subs-regere)؛ تحول معنایی «برخاستن آب» به «سرچشمه، خاستگاه» تحولی متعارف است. تنها نکته آن است که پیکان این جعبه یکراست از جعبهٔ لاتین آمده و نه از راه فرانسه، حال آنکه dress و source از فرانسه گذشته‌اند. ادعای نورایی در اصل درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins 1985 s.v. reg-1 lists 'CORRECT, DIRECT … SURGE' among the Latin regere derivatives, and the index has 'SURGE reg-'. DRESS and SOURCE are not in the 1985 index (grep returns nothing), so for those two the reference does not itself carry the arrow.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.vv. dress, source\", \"stance\": \"supports\", \"note\": \"'dress … fr. OF. (= F.) dresser, fr. VL. *directiare, fr. L. directus, pp. of dirigere, \\\\'to put into a straight line; to direct, guide\\\\''; 'source, n. — ME. sours, fr. OF. sorse, surse, sorce … fem. of sors, pp. of sordre, \\\\'to rise\\\\', used as a noun, fr. L. surgere, \\\\'to rise\\\\'. See surge.'\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. reg-1, section 2\", \"stance\": \"supports\", \"note\": \"'… : REALM, RECTITUDE, RECTO, RECTOR, RECTUM, REGENT, REGIME, REGIMENT, REGION; CORRECT, DIRECT, ERECT, RECTANGLE, RECTIFY, RECTILINEAR, RISORGIMENTO, SURGE.'\"}\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"Latin\",\n          \"words\": \"rex\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin rēx, gen. rēgis 'king' continues the IE root-noun *h₃rēǵ-s 'director, ruler', the lengthened grade of *h₃reǵ-, and is the exact cognate of Sanskrit rā́j-/rā́jan-, Old Irish rí (gen. ríg) and Gaulish -rīx in Dumnorīx. Watkins: 'II. Lengthened-grade form *rēǵ-, Indo-European word for a tribal king … 2. Latin rēx, king (royal and priestly title): REAL, REGAL, REGULUS, REIGN, ROYAL; INTERREX, REGICIDE, REGIUS PROFESSOR, VICEREINE, VICEROY'. Ernout-Meillet: 'Le nom *rēg- du \\\\'roi\\\\' est de ces mots de la langue politique et religieuse qui se trouvent en italo-celtique et en indo-iranien … Il est naturel de penser que rex appartient au groupe de rego, comme dux au groupe de duco.' Nourai's gloss 'ruler, king' and the placement under Reg 1 are both correct.\",\n          \"derivation_fa\": \"rēx لاتین (مضاف‌الیه rēgis) «شاه» بازماندهٔ اسمِ ریشه‌ایِ هندواروپایی *h₃rēǵ-s «راه‌نماینده، فرمانروا»، یعنی صورت کشیدهٔ همان ریشهٔ *h₃reǵ-، است و دقیقاً همریشهٔ rā́j-/rā́jan- سنسکریت، rí ایرلندی کهن و -rīx گالی (در Dumnorīx) است. واتکینز آن را زیر بخش دوم مدخل reg-1 می‌آورد و ارنو-مه‌یه می‌نویسد که نام *rēg- «از واژه‌های زبان سیاسی و دینی است که هم در ایتالیک-سلتی و هم در هندوایرانی دیده می‌شود» و افزون می‌کند که «طبیعی است rex را از خانوادهٔ rego بدانیم، چنان‌که dux از خانوادهٔ duco است». معنای «فرمانروا، شاه» و جای گرفتن آن ذیل این ریشه هر دو درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₃reǵ-\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. reg-1: 'II. Lengthened-grade form *rēǵ-, Indo-European word for a tribal king. … 2. Latin rēx, king (royal and priestly title): REAL, REGAL, REGULUS, REIGN, ROYAL; INTERREX, REGICIDE, REGIUS PROFESSOR, VICEREINE, VICEROY.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, DELL s.v. rex\", \"stance\": \"supports\", \"note\": \"'Le nom *rēg- du \\\\'roi\\\\' est de ces mots de la langue politique et religieuse qui se trouvent en italo-celtique et en indo-iranien … Il est naturel de penser que rex appartient au groupe de rego, comme dux au groupe de duco.'\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 19.32 KING\", \"stance\": \"supports\", \"note\": \"'Lat. rēx, gen. rēgis (> the Romance words) … Skt. (Vedic) rāj-, but commonly n-stem rājan-.' Buck's table gives Sp. rey, Fr. roi, It. re as its Romance continuations.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. rex\", \"stance\": \"supports\", \"note\": \"'rex, n., king. — L. rex, gen. regis, \\\\'ruler, king\\\\', rel. to regere … cogn. with OI. rāj-, rājan-, \\\\'king\\\\', OIr. rí, gen. ríg … fr. I.-E. base *reg-.'\"}\n          ]\n        },\n        {\n          \"id\": 14,\n          \"lang\": \"Spanish\",\n          \"words\": \"real\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Spanish real 'royal' < Latin rēgālis 'kingly' (rēx + -ālis), the same adjective that gave French royal and English regal; used as a noun it is the name of the silver coin struck in Castile from Pedro I (mid-14th c.) and in vast quantities in the Spanish Americas, the real de a ocho / 'piece of eight'. Klein states it exactly: 'real, n., an old Spanish silver coin. — Sp., prop. an adjective meaning \\\\'royal\\\\', fr. L. regalis (whence also F. royal). See regal, adj., and cp. royal. Cp. also reis.' Watkins lists 'REAL2' under reg-1 II.2 (Latin rēx). The semantic step 'royal (coin)' > 'a coin' is the ordinary metonymy of coin-names (cf. sovereign, ducat, crown).\",\n          \"derivation_fa\": \"real اسپانیایی «شاهانه» از rēgālis لاتین (rēx + -ālis) می‌آید، همان صفتی که royal فرانسوی و regal انگلیسی نیز از آن‌اند. این صفت در کاربرد اسمی نام سکهٔ نقره‌ای شد که از روزگار پدرو یکم (میانهٔ سدهٔ چهاردهم میلادی) در کاستیل و سپس به فراوانی در مستعمرات اسپانیا در امریکا ضرب می‌شد (real de a ocho، همان «هشت‌ریالی»). کلاین صریح می‌گوید: «real، سکهٔ نقرهٔ کهن اسپانیایی — اسپانیایی، در اصل صفتی به معنی \\\\'شاهانه\\\\'، از rēgālis لاتین (که royal فرانسوی نیز از آن است)». تحول معنایی «شاهانه» به «سکه» همان مجازِ آشنای نام‌های پول است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/ریال\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 index: 'REAL2 reg-1', and the reg-1 entry lists REAL among the descendants of 'Latin rēx, king (royal and priestly title)'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. real (the coin)\", \"stance\": \"supports\", \"note\": \"'real, n., an old Spanish silver coin. — Sp., prop. an adjective meaning \\\\'royal\\\\', fr. L. regalis (whence also F. royal). See regal, adj., and cp. royal. Cp. also reis.'\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 19.32 KING, table\", \"stance\": \"supports\", \"note\": \"Buck's table gives 'Sp. rey' as the Spanish continuation of Lat. rēx, the base of the adjective rēgālis > real.\"}\n          ]\n        },\n        {\n          \"id\": 15,\n          \"lang\": \"Persian\",\n          \"words\": \"rîyâl «ریال»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian «ریال» riyāl is a loan of Spanish real, and Nourai's note ('Currency after the Spanish domination of the Persian Gulf') is verbatim what Moʿin says in his own added entry to Borhan-e Qāṭeʿ: '* ریال - بکسر اول. اصلاً اسپانیایی real به‌معنی لغوی شاهی (فرانسوی royal)، و آن به مسکوکات نقره اطلاق می‌شد، معرّب آن هم ریال … این کلمه از زمان تسلط اسپانیاییان و پرتقالیان در خلیج فارس و مراودهٔ ایشان با ایرانیان وارد فارسی شده … اکنون واحد پول ایران، معادل صد دینار', with the footnote 'لاتینی regalis، فرانسه roi (پادشاه)'. The Spanish real de a ocho circulated throughout the Indian Ocean and the Gulf from the 16th century (Portuguese Hormuz 1515-1622); the name was Arabised as ريال and re-entered Persian, and in 1932 it replaced the qerān as the official Iranian unit. Wiktionary agrees: Persian ریال, 'Compare Arabic رِيَال (riyāl) and Ottoman Turkish ریال, both from Spanish real'. Confirmed, including the historical note.\",\n          \"derivation_fa\": \"«ریال» فارسی وام‌واژهٔ real اسپانیایی است و یادداشت نورایی («پول رایج پس از چیرگی اسپانیایی‌ها بر خلیج فارس») عیناً همان است که معین در مدخل افزودهٔ خود بر برهان قاطع نوشته: «* ریال ـ بکسر اول. اصلاً اسپانیایی real به معنی لغوی شاهی (فرانسوی royal)، و آن به مسکوکات نقره اطلاق می‌شد، معرّب آن هم ریال … این کلمه از زمان تسلط اسپانیاییان و پرتقالیان در خلیج فارس و مراودهٔ ایشان با ایرانیان وارد فارسی شده … اکنون واحد پول ایران، معادل صد دینار»، با حاشیهٔ «لاتینی regalis، فرانسه roi (پادشاه)». سکهٔ اسپانیاییِ real de a ocho از سدهٔ شانزدهم میلادی در اقیانوس هند و خلیج فارس رواج داشت (هرمزِ پرتغالی ۱۵۱۵ـ۱۶۲۲)، نام آن در عربی به «ریال» معرّب شد و از همان راه در فارسی جا افتاد و در ۱۳۱۱ خورشیدی جای «قران» را به عنوان واحد رسمی پول ایران گرفت. ویکی‌واژه نیز همین را می‌گوید. ادعای نورایی، از جمله یادداشت تاریخی‌اش، درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/ریال\"],\n          \"ref_check\": [\n            {\"ref\": \"BQT:985\", \"status\": \"supports\", \"note\": \"Borhan-e Qāṭeʿ with Moʿin's additions, BQT_v2_pages.txt form-feed leaf 447 (≈ printed p. 985): '* ریال - بکسر اول. اصلاً اسپانیایی real به‌معنی لغوی شاهی (فرانسوی royal)، و آن به مسکوکات نقره اطلاق می‌شد، معرّب آن هم ریال … این کلمه از زمان تسلط اسپانیاییان و پرتقالیان در خلیج فارس و مراودهٔ ایشان با ایرانیان وارد فارسی شده … اکنون واحد پول ایران معادل صد دینار'; footnote 1: 'لاتینی regalis، فرانسه roi (پادشاه)'. This is the source of Nourai's box AND of his NOTE.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BQT\", \"where\": \"Moʿin's added entry * ریال (BQT_v2 leaf 447)\", \"stance\": \"supports\", \"note\": \"See the quotation above; Moʿin explicitly names Spanish real, French royal and Latin regalis, and dates the borrowing to the Spanish/Portuguese presence in the Gulf.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. real (the coin)\", \"stance\": \"supports\", \"note\": \"'Sp., prop. an adjective meaning \\\\'royal\\\\', fr. L. regalis' — the donor form.\"},\n            {\"src\": \"MON\", \"where\": \"MON_part2.txt (grep ریال)\", \"stance\": \"silent\", \"note\": \"The local OCR of Moʿin's lexicon shows ریال only in running text (prices, 'نخود معادل یک ریال کنونی'), not as an etymologised headword.\"}\n          ]\n        },\n        {\n          \"id\": 16,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"A second empty pass-through box, standing for French roi 'king' (< L. rēx, rēgem) and above all for the adjective royal (OF roial, MF roial < L. rēgālis), which is the immediate donor of both the English word in node 18 and the Persian رویال in node 17. Klein s.v. royal: 'ME. roial, fr. MF. roial (F. royal), fr. L. regalis, \\\\'pertaining to a king, royal\\\\', fr. rex, gen. regis, \\\\'king\\\\''; Watkins lists ROYAL among the descendants of Latin rēx. The box is factually justified even though nothing is printed in it.\",\n          \"derivation_fa\": \"دومین جعبهٔ تهیِ واسطه است و نمایندهٔ roi فرانسوی «شاه» (از rēx/rēgem لاتین) و به‌ویژه صفت royal (فرانسهٔ کهن roial، از rēgālis لاتین) است؛ همین صفت وام‌دهندهٔ مستقیم واژهٔ انگلیسیِ گرهٔ ۱۸ و «رویالِ» فارسیِ گرهٔ ۱۷ است. کلاین در مدخل royal می‌نویسد: «انگلیسی میانه roial، از roial فرانسهٔ میانه، از rēgālis لاتین \\\\'وابسته به شاه\\\\'، از rex» و واتکینز نیز ROYAL را در شمار بازماندگان rēx می‌آورد. پس با آنکه در کتاب چیزی در این جعبه چاپ نشده، محتوای آن درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. reg-1 II.2: 'Latin rēx, king … : REAL, REGAL, REGULUS, REIGN, ROYAL' — ROYAL being the French-mediated member of the list.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. royal\", \"stance\": \"supports\", \"note\": \"'royal, adj. — ME. roial, fr. MF. roial (F. royal), fr. L. regalis, \\\\'pertaining to a king, royal\\\\', fr. rex, gen. regis, \\\\'king\\\\'. See rex and cp. regal and real, \\\\'a coin\\\\', which are doublets of royal.'\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. rex\", \"stance\": \"supports\", \"note\": \"rēx and its adjective rēgālis are the base of the Romance forms (Fr. roi, Sp. rey) listed there and in Buck 19.32.\"}\n          ]\n        },\n        {\n          \"id\": 17,\n          \"lang\": \"Persian\",\n          \"words\": \"royâl «رویال»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Persian «رویال» royāl is a 20th-century European loan used in trade names and in the sense 'royal, de luxe' (royal jelly ژل رویال, paper sizes, hotel and product names). The form with -oy- and final -āl matches French royal [ʁwajal] rather than English royal [ˈrɔɪəl], so Nourai's French parent is the likelier donor, though English mediation cannot be excluded for the technical uses. The chain itself is beyond doubt: L. rēgālis > OF roial > F. royal > Pers. رویال (Klein s.v. royal). The verdict is only 'plausible' because the single reference Nourai gives, VOP:193 (Mahshid Moshiri, Farhang-e Vāžehā-ye Orupāyi dar Fārsi), has no copy anywhere — refs_online.json records 'Searched archive.org, ketabnak, noorlib, web: not found' — and neither Moʿin nor Borhan has the headword, so the specific French-vs-English attribution is untested.\",\n          \"derivation_fa\": \"«رویال» وام‌واژه‌ای اروپایی از سدهٔ بیستم است که در فارسی بیشتر در نام‌های بازرگانی و به معنی «شاهانه، درجه‌یک» به کار می‌رود (ژل رویال، قطع رویال کاغذ، نام هتل‌ها و کالاها). شکل آوایی آن با -وی- و پایانهٔ -ال به royal فرانسوی [ʁwajal] می‌خورد نه به royal انگلیسی [ˈrɔɪəl]؛ پس وام‌دهی از فرانسه که نورایی گفته محتمل‌تر است، هرچند در کاربردهای فنی میانجی‌گری انگلیسی را نمی‌توان کنار گذاشت. خودِ زنجیره تردیدی ندارد: rēgālis لاتین ← roial فرانسهٔ کهن ← royal فرانسوی ← رویالِ فارسی. داوری «با احتیاط پذیرفتنی» تنها از آن روست که یگانه مأخذ نورایی، یعنی VOP:193 (فرهنگ واژه‌های اروپایی در فارسی، مهشید مشیری)، هیچ نسخهٔ در دسترسی ندارد و معین و برهان قاطع نیز این سرواژه را نیاورده‌اند.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"VOP:193\", \"status\": \"not_checked\", \"note\": \"Moshiri, Farhang-e Vāžehā-ye Orupāyi dar Fārsi (Alborz 1371/1992) has no online or local copy; refs_online.json s.v. VOP: 'kind: none … Searched archive.org, ketabnak, noorlib, web: not found … Purchase second-hand only.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. royal\", \"stance\": \"supports\", \"note\": \"'royal, adj. — ME. roial, fr. MF. roial (F. royal), fr. L. regalis … fr. rex' — establishes the Latin > French link that Persian borrowed.\"},\n            {\"src\": \"MON\", \"where\": \"MON_part1/part2 (grep رویال)\", \"stance\": \"silent\", \"note\": \"No hit for رویال in the local OCR of Moʿin's lexicon volumes.\"},\n            {\"src\": \"BQT\", \"where\": \"BQT_v2_pages.txt, the ر+ی spread (leaf 447, where * ریال stands)\", \"stance\": \"silent\", \"note\": \"Moʿin added * ریال there but no entry رویال; the word is too recent for Borhan and its supplements.\"}\n          ]\n        },\n        {\n          \"id\": 18,\n          \"lang\": \"English\",\n          \"words\": \"royal\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English royal < Middle English roial (13th c.) < Old/Middle French roial (Modern French royal) < Latin rēgālis 'of a king' < rēx. Klein: 'royal, adj. — ME. roial, fr. MF. roial (F. royal), fr. L. regalis, \\\\'pertaining to a king, royal\\\\', fr. rex, gen. regis, \\\\'king\\\\'. See rex and cp. regal and real, \\\\'a coin\\\\', which are doublets of royal.' The three-way doublet regal (learned, straight from Latin) / royal (through French) / real (through Spanish) is exactly the pattern the chart draws across nodes 14, 18 and 19.\",\n          \"derivation_fa\": \"«royal» انگلیسی از roial انگلیسی میانه (سدهٔ سیزدهم میلادی)، از roial فرانسهٔ کهن و میانه (royal امروزی)، از rēgālis لاتین «شاهانه»، از rēx می‌آید. کلاین می‌نویسد که regal (وام مستقیم و کتابی از لاتین)، royal (از راه فرانسه) و real (از راه اسپانیایی) سه «دوگانه»ی یک واژه‌اند — و همین الگو دقیقاً همان است که نمودار در گره‌های ۱۴، ۱۸ و ۱۹ رسم کرده است. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. reg-1 II.2 lists ROYAL among the English descendants of 'Latin rēx, king'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. royal, royalty\", \"stance\": \"supports\", \"note\": \"'royal, adj. — ME. roial, fr. MF. roial (F. royal), fr. L. regalis … cp. regal and real, \\\\'a coin\\\\', which are doublets of royal.'\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 19.32\", \"stance\": \"supports\", \"note\": \"'Fr. roi' from Lat. rēx heads the French column; royal is its adjective via rēgālis.\"}\n          ]\n        },\n        {\n          \"id\": 19,\n          \"lang\": \"English\",\n          \"words\": \"Rex\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English Rex is Latin rēx taken over unchanged as a learned word: in British legal and numismatic usage 'Rex' follows the sovereign's name (Georgius VI Rex; R. v. Smith = 'the Crown against Smith'), and it is also a common dog's name. Klein's entry is simply 'rex, n., king. — L. rex, gen. regis, \\\\'ruler, king\\\\', rel. to regere … fr. I.-E. base *reg-'. Because it is a direct Latin borrowing there is no sound change to describe; the only shift is one of register, from the ordinary Latin word for 'king' to a titular formula.\",\n          \"derivation_fa\": \"«Rex» در انگلیسی همان rēx لاتین است که بی‌هیچ دگرگونی آوایی و به صورت وام‌واژه‌ای کتابی گرفته شده: در کاربرد حقوقی و سکه‌شناسی بریتانیا پس از نام پادشاه می‌آید (Georgius VI Rex) و در دعاوی کیفری به جای «دادستان/تاج» به کار می‌رود (R. v. Smith). کلاین در مدخل خود تنها می‌نویسد: «rex، شاه — لاتین rex، مضاف‌الیه regis \\\\'فرمانروا، شاه\\\\'، وابسته به regere … از ریشهٔ هندواروپایی *reg-». چون وام‌گیری مستقیم است، دگرگونی آوایی‌ای در کار نیست و تنها تحول، تحول کاربردی است: از واژهٔ عادی لاتین برای «شاه» به یک فرمول لقبی. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. reg-1 II.2: 'Latin rēx, king (royal and priestly title)' with the English descendants listed; the index likewise has 'REGIUS PROFESSOR' and 'INTERREX reg-1' as direct Latin borrowings of the same word.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. rex\", \"stance\": \"supports\", \"note\": \"'rex, n., king. — L. rex, gen. regis, \\\\'ruler, king\\\\', rel. to regere, \\\\'to keep straight, guide, lead, rule\\\\', regina, \\\\'queen\\\\', and cogn. with OI. rāj-, rājan-, \\\\'king\\\\', OIr. rí, gen. ríg, \\\\'king\\\\', fr. I.-E. base *reg-.'\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. rex\", \"stance\": \"supports\", \"note\": \"'rex … Il est naturel de penser que rex appartient au groupe de rego' — the Latin word taken over by English unchanged.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-417.json\",\"w\",encoding=\"utf-8\") as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-417.py",
 "description": "Build page-417.json"
}
```


### [2026-09-14T01:30:15.031Z] TOOL RESULT

```
written
```


## [2026-09-14T01:30:19.314Z] TOOL CALL #86: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-417.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 417",
 "description": "Validate and run verify_check"
}
```


### [2026-09-14T01:30:22.278Z] TOOL RESULT

```
JSON OK
nodes verified: 19/19
node verdicts: {'plausible': 3, 'disputed': 1, 'confirmed': 15}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 14, 'partial': 5, 'not_checked': 4}
books consulted: {'partial': 5, 'supports': 42, 'contradicts': 1, 'silent': 4} | by book: {'KLN': 13, 'SYN': 5, 'AHD': 5, 'POK': 4, 'MON': 4, 'LAT': 4, 'BRT': 2, 'HUB': 2, 'CHEUNG': 2, 'KNT': 2, 'HJB': 2, 'BQT': 2, 'PHD': 1, 'NYB': 1, 'HRN': 1, 'ARY': 1, 'TLM': 1}
```


## [2026-09-14T01:30:27.449Z] TOOL CALL #87: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg417.png data/verification/sources/refs/ocr/BOOK/417.png && ls -la data/verification/sources/refs/ocr/BOOK/417.png",
 "description": "Archive page image"
}
```


### [2026-09-14T01:30:27.569Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 55756 Sep 13 21:30 data/verification/sources/refs/ocr/BOOK/417.png
```


## [2026-09-14T01:30:45.755Z] AGENT

Page 417 (book p. 387), one entry, root **Reg 1, Rěkto** — verification written to `/home/sfmqrb/git/rishe/data/verification/page-417.json`; `verify_check.py 417` reports 19/19 nodes, **0 PROBLEM lines**.

Verdicts: root confirmed; nodes — 15 confirmed, 3 plausible, 1 disputed. Ref checks: 14 supports, 5 partial, 4 not_checked. 17 different books consulted.

- **disputed — #2 Persian, رده / رژه "a row of soldiers"**: رده goes back to MP *radag* (MacKenzie; Moʿin's BQT footnote quotes Henning for Phl. *rdk*), and Horn §609 expressly separates it ("np. *rede* … scheint zu aw. *ərəta-*, ai. *r̥tá-* zu gehören"); Wiktionary derives it from PIE *\*h₂rey-*. A *\*reǵ-* form would give *rāz-*, not *rad-*. The node's other four words (râst, raj, razm, afrâštan) are all sound, so the node takes the worst verdict.
- **plausible — #1 Avestan "razma"**: the attested Avestan noun is *rasman-* (nom. *rasma*); *razma* with -zm- is Hübschmann's reconstructed **Old Persian** form (Pers. Studien §612), so Nourai printed an OP form under an Avestan label. "aiwi-reg" is likewise a reconstruction, not an Avestan lemma (Bartholomae has only *ham-rāzaiia-*).
- **plausible — #7 English "rich"**: under the lengthened grade and a Celtic→Germanic loan (Watkins, Pokorny, Buck), not a descendant of the *\*rehtaz/\*rakō* box the arrow leaves.
- **plausible — #17 رویال**: chain itself certain, but the sole reference VOP:193 (Moshiri) exists in no accessible copy, and neither Moʿin nor Borhan has the headword.

Notable confirmations: Horn 136 turned out to *contradict* Nourai on رزم, but Hübschmann §612, Nyberg II s.v. *razm*, Moʿin's own BQT footnote 8 and Wiktionary all back Nourai — so razm stands. BQT:985 is Moʿin's added entry "* ریال … اصلاً اسپانیایی real … از زمان تسلط اسپانیاییان و پرتقالیان در خلیج فارس", i.e. it supports the node *and* Nourai's printed NOTE verbatim. Kent 171/206 supports all three Old Persian words exactly.

Extraction issues for the owner (minor, both checked against the rendered page, image saved to `data/verification/sources/refs/ocr/BOOK/417.png`):
- The book prints **`arštâ`** (node #3); the JSON has `aršta` — a lost circumflex.
- The printed page carries a blank, unlabelled rectangle to the right of the Old Persian box; it is empty in the book itself, so the extraction is correct to omit it — noting it only so it isn't later mistaken for lost text.
