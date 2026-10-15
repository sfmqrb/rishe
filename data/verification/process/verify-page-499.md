# Verification process log — verify-page-499


## [2026-10-15T02:25:52.463Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 499 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-499.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-499.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-499.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 499` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-15T02:25:52.492Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-15T02:25:53.976Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-15T02:25:54.004Z] TOOL RESULT

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


## [2026-10-15T02:25:54.477Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-499.txt"
}
```


### [2026-10-15T02:25:54.499Z] TOOL RESULT

```
1	=== PDF page 499 (book page 469) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Tel : to lift  (refs POK:1060; KLN:122)
4	#1 (parent #0) [Sanskrit] refs=POK:1060; AHD | tulâ, tulya : balance weight
5	  #2 (parent #1) [Avestan] refs=PLA:194 | tara-âz, tara-âzu : balance, scale ☞Ag
6	    #3 (parent #2) [Persian] refs=BQT:480 | tarâz «تراز ، طراز» : level, balanced, nice ; tarâzu «ترازو» : scale, balance
7	#4 (parent #0) [Greek] refs=AHD | a-tlâ : lift together ; Atlas : a titan holding the heavens
8	  #5 (parent #4) [Arabic] refs=None | 
9	    #6 (parent #5) [Persian] refs=BQT:143; MON5:5155 | atlas «اطلس ۱» : world ; atlas «اطلس ۲» : world map, map ; atlas «اطلس ۳» : Atlantic ocean
10	  #7 (parent #4) [French] refs=None | 
11	    #8 (parent #7) [Persian] refs=MON5:8 | Âtlântîk «آتلانتیک» : "(ocean) by the Atlas mountain"
12	  #9 (parent #4) [English] refs=AHD | atlas 1 : world, map ; Atlantic
13	#10 (parent #0) [Greek] refs=AHD | telos : charge, toll ; talanton : weight of gold
14	  #11 (parent #10) [English] refs=None | toll ; talent
15	#12 (parent #0) [Latin] refs=AHD | tolĕre : carry, bear ; lâtus : carried ; trans-latŭs : carried across, translated ☞Ter 1
16	  #13 (parent #12) [English] refs=None | tolerate ; relate ; translate
17	
```


## [2026-10-15T02:25:55.378Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-499.json"
}
```


### [2026-10-15T02:25:55.435Z] TOOL RESULT

```
1	{
2	  "pdf_page": 499,
3	  "book_page": 469,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Tel",
8	        "lang": "Indo-European",
9	        "refs": "POK:1060; KLN:122",
10	        "gloss": "to lift"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Sanskrit",
17	          "refs": "POK:1060; AHD",
18	          "words": [
19	            {"translit": "tulâ, tulya", "gloss": "balance weight", "script": null}
20	          ],
21	          "note": null,
22	          "quote": null
23	        },
24	        {
25	          "id": 2,
26	          "parent": 1,
27	          "lang": "Avestan",
28	          "refs": "PLA:194",
29	          "words": [
30	            {"translit": "tara-âz, tara-âzu", "gloss": "balance, scale", "script": null, "see": ["Ag"]}
31	          ],
32	          "note": null,
33	          "quote": null
34	        },
35	        {
36	          "id": 3,
37	          "parent": 2,
38	          "lang": "Persian",
39	          "refs": "BQT:480",
40	          "words": [
41	            {"translit": "tarâz", "gloss": "level, balanced, nice", "script": "تراز ، طراز"},
42	            {"translit": "tarâzu", "gloss": "scale, balance", "script": "ترازو"}
43	          ],
44	          "note": null,
45	          "quote": {
46	            "text": "یاد باد آن شب که آن شمسهٔ خوبان تراز - به طرب داشت مرا تا بگه بانگ نماز",
47	            "poet": "Farrokhî"
48	          }
49	        },
50	        {
51	          "id": 4,
52	          "parent": 0,
53	          "lang": "Greek",
54	          "refs": "AHD",
55	          "words": [
56	            {"translit": "a-tlâ", "gloss": "lift together", "script": null},
57	            {"translit": "Atlas", "gloss": "a titan holding the heavens", "script": null}
58	          ],
59	          "note": null,
60	          "quote": null
61	        },
62	        {
63	          "id": 5,
64	          "parent": 4,
65	          "lang": "Arabic",
66	          "refs": null,
67	          "words": [],
68	          "note": null,
69	          "quote": null
70	        },
71	        {
72	          "id": 6,
73	          "parent": 5,
74	          "lang": "Persian",
75	          "refs": "BQT:143; MON5:5155",
76	          "words": [
77	            {"translit": "atlas", "gloss": "world", "script": "اطلس ۱"},
78	            {"translit": "atlas", "gloss": "world map, map", "script": "اطلس ۲"},
79	            {"translit": "atlas", "gloss": "Atlantic ocean", "script": "اطلس ۳"}
80	          ],
81	          "note": null,
82	          "quote": null
83	        },
84	        {
85	          "id": 7,
86	          "parent": 4,
87	          "lang": "French",
88	          "refs": null,
89	          "words": [],
90	          "note": null,
91	          "quote": null
92	        },
93	        {
94	          "id": 8,
95	          "parent": 7,
96	          "lang": "Persian",
97	          "refs": "MON5:8",
98	          "words": [
99	            {"translit": "Âtlântîk", "gloss": "\"(ocean) by the Atlas mountain\"", "script": "آتلانتیک"}
100	          ],
101	          "note": null,
102	          "quote": null
103	        },
104	        {
105	          "id": 9,
106	          "parent": 4,
107	          "lang": "English",
108	          "refs": "AHD",
109	          "words": [
110	            {"translit": "atlas 1", "gloss": "world, map", "script": null},
111	            {"translit": "Atlantic", "gloss": null, "script": null}
112	          ],
113	          "note": null,
114	          "quote": null
115	        },
116	        {
117	          "id": 10,
118	          "parent": 0,
119	          "lang": "Greek",
120	          "refs": "AHD",
121	          "words": [
122	            {"translit": "telos", "gloss": "charge, toll", "script": null},
123	            {"translit": "talanton", "gloss": "weight of gold", "script": null}
124	          ],
125	          "note": null,
126	          "quote": null
127	        },
128	        {
129	          "id": 11,
130	          "parent": 10,
131	          "lang": "English",
132	          "refs": null,
133	          "words": [
134	            {"translit": "toll", "gloss": null, "script": null},
135	            {"translit": "talent", "gloss": null, "script": null}
136	          ],
137	          "note": null,
138	          "quote": null
139	        },
140	        {
141	          "id": 12,
142	          "parent": 0,
143	          "lang": "Latin",
144	          "refs": "AHD",
145	          "words": [
146	            {"translit": "tolĕre", "gloss": "carry, bear", "script": null},
147	            {"translit": "lâtus", "gloss": "carried", "script": null},
148	            {"translit": "trans-latŭs", "gloss": "carried across, translated", "script": null, "see": ["Ter 1"]}
149	          ],
150	          "note": null,
151	          "quote": null
152	        },
153	        {
154	          "id": 13,
155	          "parent": 12,
156	          "lang": "English",
157	          "refs": null,
158	          "words": [
159	            {"translit": "tolerate", "gloss": null, "script": null},
160	            {"translit": "relate", "gloss": null, "script": null},
161	            {"translit": "translate", "gloss": null, "script": null}
162	          ],
163	          "note": null,
164	          "quote": null
165	        }
166	      ]
167	    }
168	  ]
169	}
170	
```


## [2026-10-15T02:25:58.842Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; cat sources/SOURCE_MATRIX.md | head -120; ls sources/refs/ | head -100; python3 -c \"\nimport json;d=json.load(open('sources/refs_online.json'))\nfor k in ['POK','KLN','AHD','PLA','BQT','MON','WLD','IEC','SYN','HRN','HUB','ARY','SKT','FSD','WEB','BRT','CHEUNG','AFM','LKT','FVQ']:\n  print(k, json.dumps(d.get(k),ensure_ascii=False)[:400])\n\""
}
```


### [2026-10-15T02:25:59.446Z] TOOL RESULT

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
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt`
- **FRS** — Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FRS.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FRS_pages.txt`
- **FSF** — Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSF.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSF_pages.txt`
- **HENNING** — HENNING
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HENNING_selected_papers.txt`
- **EAV** — J. Duchesne-Guillemin, 'Etymologies avestiques', BSOAS 9.4 (1939) pp. 861-869
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/EAV_studies.txt`
- **ISS** — H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ISS_alt_DKS.txt`
- **AHM** — I. Gershevitch, The Avestan Hymn to Mithra, Cambridge 1959
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHM.txt`
- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt`
- **FFD** — Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD/FFD_pages.txt`
- **IRN** — Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/IRN/IRN_pages.txt`
- **AVG** — A. V. W. Jackson, An Avesta Grammar in Comparison with Sanskrit, Part I, Stuttgart 1892
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AVG.txt`
- **HID** — C. Bartholomae, Handbuch der altiranischen Dialekte, Leipzig 1883
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HID.txt`
- **ZAW** — C. Bartholomae, Zum altiranischen Wörterbuch: Nacharbeiten und Vorarbeiten (Beiheft zu IF XIX), Strassburg 190
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ZAW/ZAW_bartholomae_1906_gb_agDP0HdEssEC.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ZAW/ZAW_pages.txt`
- **TLM** — H. C. Tolman, Ancient Persian Lexicon and the Texts of the Achaemenidan Inscriptions, Vanderbilt Oriental Seri
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/TLM.txt`
- **UNV** — J. M. Unvala, King Husrav and his Boy: Pahlavi text and glossary, Paris (Geuthner) 1963 [orig. 'Der Pahlavi-Te
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/UNV.txt`
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
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf",
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/source
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verifica
CHEUNG null
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. l
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
```


## [2026-10-15T02:26:16.299Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; ls page-49*.json; python3 -c \"\nimport json;d=json.load(open('page-498.json'));e=d['entries'][0];print(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1)[:3000]);print(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:3000])\"; cat /home/sfmqrb/git/rishe-private/tools/verify_check.py | head -80"
}
```


### [2026-10-15T02:26:16.693Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   68k sfmqrb 14 Oct 22:14  page-49.json
.rw-r--r--   64k sfmqrb 14 Oct 22:14  page-490.json
.rw-r--r--   55k sfmqrb 14 Oct 22:14  page-491.json
.rw-r--r--   70k sfmqrb 14 Oct 22:14  page-492.json
.rw-r--r--   68k sfmqrb 14 Oct 22:14  page-493.json
.rw-r--r--   62k sfmqrb 14 Oct 22:14  page-494.json
.rw-r--r--   60k sfmqrb 14 Oct 22:14  page-495.json
.rw-r--r--   66k sfmqrb 14 Oct 22:14  page-496.json
.rw-r--r--   35k sfmqrb 14 Oct 22:14  page-497.json
.rw-r--r--   64k sfmqrb 14 Oct 22:14  page-498.json
{
 "entry": 0,
 "root": "Teku 1, Tekw",
 "verdict": "confirmed",
 "modern_form": "PIE *tekʷ- 'to run, to flow' (Pokorny 1059-1060; Watkins/AHD tekʷ- 'to run, flee')",
 "note": "Pokorny's IEW pp.1059-1060 heads the entry \"tekʷ-\" and glosses it 'to run; to flow' — Nourai's gloss word for word. His two headwords are one root: 'Tekw' is his transcription of *tekʷ-, and 'Teku 1' the same root written with -u for the labial glide (his own third entry on the page, 'Tekw', is a redirect to 'Teku 1'). The language label 'Indo-European' is right. One modern caveat: the root-final stop is contested — older handbooks (Pokorny, Watkins, Mann, LIV) write the labiovelar *kʷ on the strength of Hittite watkuzi, while Kroonen, Adams (Toch. B cake) and EIEC argue for plain *k, so Wiktionary lists *tek- as an alternative reconstruction. That does not affect any Iranian node on this page. The real problems on this chart are downstream: the melt-branch (#10, #11) belongs to a different root by current scholarship, and the 'throw/measure' branch (#5-#9) is assigned by Cheung to a homophonous *tač².",
 "note_fa": "پوکورنی در «فرهنگ ریشه‌شناختی هندواروپایی» صفحه‌های ۱۰۵۹–۱۰۶۰ سرواژهٔ *tekʷ- را با معنای «دویدن؛ روان شدن» می‌آورد — همان معنایی که نورایی داده است. دو سرواژهٔ نورایی («Teku 1» و «Tekw») در حقیقت یک ریشه‌اند و خودِ او در همین صفحه «Tekw» را به «Teku 1» ارجاع داده است؛ برچسب «هندواروپایی» نیز درست است. تنها نکتهٔ امروزی این است که همخوان پایانی ریشه مورد اختلاف است: فرهنگ‌های قدیمی‌تر (پوکورنی، واتکینز، مان، LIV) بر پایهٔ watkuzi هیتی *kʷ لبی‌کامی می‌نویسند، ولی کرونن و آدامز (با استناد به cake تخاری ب) و EIEC *k سادّه را ترجیح می‌دهند و ویکی‌واژه *tek- را به‌عنوان بازسازی جایگزین آورده است؛ این اختلاف بر هیچ‌یک از گره‌های ایرانی این صفحه اثر ندارد. اشکال‌های واقعی این نمودار در شاخه‌های پایین‌دست است: شاخهٔ «گداختن» (گره‌های ۱۰ و ۱۱) بنا بر پژوهش امروزی به ریشهٔ دیگری می‌رسد و شاخهٔ «انداختن/هندسه» (گره‌های ۵ تا ۹) را چونگ به ریشهٔ هم‌آوای *tač² می‌برد.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tek%CA%B7-",
  "https://www.etymonline.com/word/toxic"
 ],
 "ref_check": [
  {
   "ref": "POK:1059",
   "status": "supports",
   "note": "Pokorny IEW pp.1059-1060 s.v. tekʷ- 'to run; to flow' (local POK_full.txt, 'Root / lemma: tek\"-', Page(s): 1059-1060): \"Avestan tacaiti 'running, hurries; flows', participle -taxta-, np. taxtan 'run', hantacina-; Avestan vi-taxti- f. 'das Zerfließen, Schmelzen'; iran. (skyth.) *tahsa- (npers. taxs) 'arrow, bow', from which gr. toxon ds., Latin taxus 'yew'; Avestan taka- m., np. tak 'run, flow'; Avestan tacar- n. 'run, flow, pathway', tacan- 'hurrying', iran. *tahra- 'quick, fast'.\""
  }
 ],
 "consulted": [
  {
   "src": "POK",
   "where": "IEW pp.1059-1060, Root/lemma tekʷ-",
   "stance": "supports",
   "note": "Headword and gloss match Nourai exactly ('to run; to flow'); references at the end of the entry: \"WP. I 715 f., Trautmann 316 f., Vasmer 3, 89, 113 f., Mayrhofer 1, 466 f.\""
  
{
 "id": 1,
 "lang": "Avestan",
 "words": "tak, taka, tač; tačaiti",
 "verdict": "confirmed",
 "derivation": "Avestan has the primary verb tac- / tak- 'to run, to flow' (3sg. pres. tačaiti, Y 16.8 tačat, Yt 8.5 tačanti) and the noun taka- m. 'course, running, flow'; these continue Proto-Iranian *tač- < Proto-Indo-Iranian *tać- < PIE *tekʷ- exactly as drawn, the palatalisation of *kʷ before the thematic *-e- giving Av. -c- [č] while the zero/other grades keep k (taka-, -taxta-). Sanskrit tákti 'rushes', Lithuanian tekù 'I run, flow', OCS tekǫ are the direct cognates. Nourai's three citation forms tak / taka / tač are simply the root, the o-grade noun and the present stem; the gloss 'to run' is Pokorny's and Bartholomae's.",
 "derivation_fa": "در اوستایی فعل tac-/tak- «دویدن، روان شدن» با صیغهٔ سوم‌شخص tačaiti و اسم taka- «دو، جریان» به‌کار رفته است. این‌ها بازماندهٔ ایرانی باستان *tač- و در نهایت هندواروپایی آغازین *tekʷ- اند؛ *kʷ پیش از واکهٔ e به č (ج/چ اوستایی) بدل شده و در دیگر پایه‌ها به‌صورت k مانده است (taka-، -taxta-). هم‌ریشه‌های آن سنسکریت tákti و لیتوانیایی tekù است. ادعای نورایی در این گره کاملاً درست است (پوکورنی ۱۰۵۹، بارتولومه، چونگ).",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tek%CA%B7-",
  "https://en.wiktionary.org/wiki/%D8%AA%D8%A7%D8%AE%D8%AA%D9%86"
 ],
 "ref_check": [
  {
   "ref": "POK:1059",
   "status": "supports",
   "note": "Pokorny IEW pp.1059-1060 s.v. tekʷ- 'to run; to flow' (local POK_full.txt, 'Root / lemma: tek\"-', Page(s): 1059-1060): \"Avestan tacaiti 'running, hurries; flows', participle -taxta-, np. taxtan 'run', hantacina-; Avestan vi-taxti- f. 'das Zerfließen, Schmelzen'; iran. (skyth.) *tahsa- (npers. taxs) 'arrow, bow', from which gr. toxon ds., Latin taxus 'yew'; Avestan taka- m., np. tak 'run, flow'; Avestan tacar- n. 'run, flow, pathway', tacan- 'hurrying', iran. *tahra- 'quick, fast'.\""
  },
  {
   "ref": "BQT:503",
   "status": "partial",
   "note": "Borhan-e Qate' (BQT_v1_pages.txt, form-feed leaf 732 = printed p. ~503/504, running head تکابوی) carries the entries تکاپوی، تکاو، تکاور with Mo'in's footnote '۶ - از: تک + آور (آوردن)'. The page documents the Persian tak-family Nourai puts in the daughter box, but it gives no Avestan tak-/tač- form, so it supports the Persian side of the arrow only."
  }
 ],
 "consulted": [
  {
   "src": "BRT",
   "where": "AiW col. ~626 s.v. tac- ; col. 1869 s.v. tacan-",
   "stance": "supports",
   "note": "Bartholomae's Altiranisches Wörterbuch (local BRT.txt) lists Av. tac- with the senses 'laufen' and, 'insbesondere von Flüssigkeiten: fliessen, strömen' (e.g. 'kaθa xā .. apǎim tacinti nava', Yt 8.5), plus the Kaus. 'fliessen lassen' — exactly the root and glosses Nourai gives."
  },
  {
   "src": "CHEUNG",
   "where": "EDIV p. 373 s.v. *tač¹",
   "stance": "supports",
   "note": "Cheung 2007: \"*tač¹ 'to flow, run, walk' — AVESTAN: YAv. tac- 'to flow; walk'\", with the full paradigm (IND. 3sg. fratacaiti, INJ. 3sg. tacat, SU
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


## [2026-10-15T02:26:18.372Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; ls site/pages/499.jpg && python3 -c \"\nfrom PIL import Image; im=Image.open('site/pages/499.jpg'); print(im.size)\""
}
```


### [2026-10-15T02:26:18.803Z] TOOL RESULT

```
Exit code 1
Permissions Size User   Date Modified Name
.rw-r--r--   51k sfmqrb 14 Oct 22:15  site/pages/499.jpg
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    from PIL import Image; im=Image.open('site/pages/499.jpg'); print(im.size)
    ^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'PIL'
```


## [2026-10-15T02:26:21.402Z] TOOL CALL #7: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad && cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad && pdftoppm -f 499 -l 499 -r 200 -png -singlefile /home/sfmqrb/git/rishe-private/EtymologicalDictionary-persian-english.pdf pg499 && ls -la pg499.png"
}
```


### [2026-10-15T02:26:22.295Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   57k sfmqrb 14 Oct 22:26  pg499.png
```


## [2026-10-15T02:26:23.823Z] TOOL CALL #8: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg499.png"
}
```


### [2026-10-15T02:26:24.196Z] TOOL RESULT

```

```


## [2026-10-15T02:26:24.191Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-10-15T02:26:26.930Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'lemma: tel' POK_full.txt | head; grep -n -A12 'Root / lemma: tel-, tele' POK_full.txt | head -60"
}
```


### [2026-10-15T02:26:27.288Z] TOOL RESULT

```
85143:Root / lemma: telegh- 
85156:Root / lemma: telek- 
85184:Root /lemma: tel-1, tela-, tle(i)- tla- 
85249:Root / lemma: tel-2, tela-, telu- 
85292:Root / lemma: tel-3 
85311:Root / lemma: tel-4 
85317:Root / lemma: telp-
```


## [2026-10-15T02:26:28.662Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 85184,85250p POK_full.txt"
}
```


### [2026-10-15T02:26:29.012Z] TOOL RESULT

```
Root /lemma: tel-1, tela-, tle(i)- tla- 

Meaning: to transport, carry; to bear, suffer 

Material: Old Indie tulai. " scales, weight ', tulayati^hebi auf, wagt' (with Ablautneuerung in 

addition td/ayat/6s.), tu//ma- 'wagbar', tulya- "gleichartig, comparable '; Armenian t'oium^ 

allow, dulde, ertrage'; 

gr. TaAaaaai and TAf|vai (Doric etAqv), participle TAa(;, lAaaa, Fut. lAriaopiai, Doric 
TAaao|jai, Perf. tstAoijsv, tstAoGi, TSiAnuTa, T£TAr|6T0(; "bear, endure, brook ', participle 
TAr|T6(;, Doric tAc(t6(; "duldend, steadfast; ertraglich' (= Latin latus, cymr. tlawd^axxr\\ Indo 



Germanic *fl-tds), idKaq, -avToc; and (after |j£Ac((;) -avo(;, -aiva "ertragend, duldend, 
leidend', laAavTOv (originally to laAac;, n. laAav gehoriger PI. TaAavra (actually 'die beiden 
Waagschalen') ' scales; a certain weight ', araAavToc; 'from same weight, equivalent, alike 
', noAuiAac; 'wer viel ausgestanden has; very patiently'; PN "Aikaq, -avTOc;; tAhijcjov, Doric 
TAafJwv 'ertragend, duldend', laAaoc; ds., in compound laAa-; e.g. raAa-nsvGric; 'affliction 
ertragend', laAa-cppajv 'ausharrenden Sinnes, beharrlich', next to which TaAaai-cppwv and 
TaAai-nojpoc; '*Gefahren or Nachstellungen erduldend' i.e. ' afflicted, unlucky '; laAapoc; m. 
'(das, wherein man carries =) basket, pannier, Kasekorb etc.', *TaAaTr|c; '*wer mijhevolle 
Arbeit to ertragen has, specific from the spinnery as Arbeit the Frauen', whereof laAaaia 
epya, laAaaia 'Wollspinnerei'; 6-iKoq 'pain' (prefix 6-); redupl. PN TaviaKoq, TavraA-suu), - 
i^w, -6u) 'allow schweben, schwenke, swing, brandish'; gradation oin ToApri- ToApa 
'boldness, das cart ', ToApnsic; 'duldend, steadfast, bold', ToApau) 'ertrage, hold from, 
dulde; wage'; e^grade rsAaaaai ToA|jr|aai, lAnvai Hes., rsAaiJcbv ' bearer, sling, strap, etc.', 
further as 'aufheben = in die Hohe heave, life' ava-, s^ava-rsAAsiv 'sich erheben, 
aufgehen, from constellation ' (avaroAn 'Aufgang from constellation '), snirsAAsaGai, 
unspTsiAac; 6 nAioc;, trans, ('aufheben and jemandem aufladen, auferlegen')£VT£AA£iv, - 
eoGai 'auftragen, order', snirsAAsiv, -saGai ds., further: tsAoc; n. ' payment, tribute, tax, 
Ausgabe, Kosten', suTsAnc; ' cheap, little kostend', noAursAnc; 'viel Aufwand erfordernd, 
precious', arsAnc; 'frei from tributes and Leistungen, abgabenfrei', probably also (with 
formants as axGoc;, nAnGoc;, perhaps through mediation eines Verbums *t£A-Gu)) tsAGoc; n. 
'Entrichtung, sacrifice, oblation'; 

venet. to/ar3. Sg. Deponens 'bringt dar'; 

Latin to//d, -ere {sustulT, sublatum) 'empor, in die Hohe heave, life etc' {*tlnd, 
transfigured from *tl-na-mi), tolutim^\v\ Trabe' (actually 'die Fijfte hebend'), tolero, -are 
'(er)trage, unterhalte', tulf, old fetu/FPeil. to fero, Old Latin Konj. tu/am^bear, carry, bring', 
/5/^s'getragen' (= gr. tAqtoc;, cymr. tiawd); 

Middle Irish tlenaim^sieaX {*tlnami), cymr. tlawd^arm' ('*duldend'), Irish t/a/fh^weak, 
gentle' {*tla-ti-)\ Old Irish toli. 'volition' {*tola), whereof /c»//75//75/''welcher gefallt' ; at most 
Old Irish tailm. Gen. telma, bret. talm^ loop, noose, snare, Schleuder', cymr. /e//77'Dohne' 
(: TsAapcbv?); 

Gothic l=>ulan, -a/da'bear, endure, brook ', Old Icelandic Po/a, Old English dolian. Old 
High German do/ends., Old Icelandic Po/n. ' patience ', Old High German du/f, Old 
English get^yld. Modern High German Geduld, dulden^ brook'; 



Latvian /z-t/7t'bear, endure, endure', perhaps (compare Gothic barn'k\d, child', actually 
"as foetus getragen') Lithuanian te//as, Latvian te/'s, telens. Old Church Slavic telbCb, russ. 
telenok{P\. teljata) 'calf; different Buga Kalba ir s. 292 f. 

Tocharian A B tal- "heave, life, bear, carry', causative tiassi, preterit A cacal, B cala. 

References: WP. I 738 ff., WH. II 688 f., Trautmann 317, Vasmer3, 90, Mayrhofer 1, 516. 
Page(s): 1060-1061 

Root / lemma: tel-2, tela-, telu-
```


## [2026-10-15T02:26:31.591Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'tela-\\|telə\\|tel9' AHD_watkins1985.txt | head; "
}
```


### [2026-10-15T02:26:31.973Z] TOOL RESULT

```
1078:a. Latin téla, web, net, warp of a fabric, also weaver’s beam (to which the warp threads are tied): TILLER?, ToiL2; b. Latin subtilis, thin, fine, precise, subtle (< *sub-téla, “thread passing under the warp,” the finest thread; sub, under; see upo): SUBTLE. 3. Suffixed form *teks-On, weaver, maker of wattle for house walls, builder (possibly contaminated with *teks-tdr, builder), in Greek tekton, carpenter, builder: TECTONIC; ARCHITECT. 4. Suf- fixed form *teks-nd-, craft (of weaving or fabricating), in Greek tekhné, art, craft, skill: TECHNICAL, POLYTECHNIC, TECHNOLOGY. 5. Possibly Germanic *thahsu-, badger (“the animal that builds,” referring to its burrowing skill), in Old High German dahs (> German Dachs), badger but more likely borrowed from the same pre- Indo-European source as the Celtic totemic name Tazgo-, Gaelic Tadhg, “‘badger’”): DACHSHUND. [Pok. tekth- 1058.] tekv-. To run, flee. Suffixed o-grade form *tokv-so- in Iranian *taxsa-, bow, borrowed into Greek toxon, bow, also (in the plural) bow and arrow (< “that which flies’): Toxic. [Pok. tekz- 1059.] tel-. Ground, floor, board. 1. Germanic *thil-j6- in Middle Low German and Middle Dutch dele, plank: DEAL?. 2. Suffixed form *tel-n- in Latin telliis (stem telliir-), earth, the earth: (TELLURIAN), (TELLURIC), (TELLURION), (TELLURIUM), TELLURO-. 3. Possibly reduplicated form *ti-tel- in Latin titulus, placard, label, superscription, title: TITLE. [Pok. 2. tel- 1061.] tela-. To lift, support, weigh; with derivatives referring to measured weights and thence to money and payment. 1. Suffixed form *telo-mon- in Greek telamén, supporter, bearer: TELAMON. 2. Suffixed form *tel/a)-es- in: a. Greek telos, tax, charge: TOLL!; PHILATELY; b. Latin tolerdre, to bear, endure: TOLERATE. 3. Suffixed zero-grade form *th-i-, becoming *tali- (influenced by ¢dlis, such), in Latin ¢alid, reciprocal punishment in kind, “something paid out”: TALION; RETALIATE. 4. Suffixed variant zero-grade form *tala-nt- in Greek talanton, balance, weight, any of several specific weights of gold or silver, hence the sum of money represented by such a weight: TALENT. 5. Perhaps intensive reduplicated form *tantal- in Greek Tantalos, name of a legendary king, “the sufferer’: (TANTALIZE), TANTALUS. 6. Perhaps zero-grade form *tla- in Greek Atlas (stem Atlant-), name of the Titan supporting the world: ATLANTIC, ATLAS. 7. Suffixed zero-grade form *tl-é- in Germanic *thulén in Old English tholian, to suffer, endure: THOLE. 8. Suf- fixed zero-grade form *tl-to- in Latin ldtus, “carried, borne,” used as the suppletive past participle of ferre, to bear (see bher-'), with its compounds: ABLATION, COL- LATE, DILATORY, ELATE, ILLATION, LEGISLATOR, OB- LATE], PRELATE, PROLATE, RELATE, SUPERLATIVE, TRANSLATE. 9. Suffixed zero-grade form *tl-d- in San- skrit tuld, scales, balance, weight: TAEL, TOLA. 10. Nasal- ized zero-grade form *tl-n-a- in Latin tollere, to lift: EXTOL. [Pok. 1. éel- 1060.] tem-. Also teme-. To cut. I. Form *tema-. Nasalized form *t(e)m-n-a- in Greek temnein, to cut: TMESIS, TOME, -TOME, -TOMY; ANATOMY, ATOM, DIATOM, DICHOTOMY, ENTOMO-, EPITOME. II. Form *tem-. 1. Suffixed form *tem-lo- in Latin templum, temple, shrine, open place for observation (augury term < “place reserved or cut out”), small piece of timber: TEMPLE!, TEMPLE’; CONTEMPLATE. 2. Extended root *tem-d- becoming *tend- in o-grade suffixed (iterative) form *tond-eyo- in Latin tondére, to shear, shave: TONSURE. [Pok. 1. tem-, tend- 1062.] teme-. Dark. Suffixed form *tema-s-. 1. Latin temere, blindly, rashly: TEMERARIOUS, TEMERITY. 2. Suffixed form *temas-rd- in Latin tenebrae (plural), darkness: TENEBRAE, TENEBRIONID. [Pok. tem()- 1063.] temp-. To stretch. Extension of ten-. 1. Possibly Latin tempus, temple of the head (? where the skin is stretched from behind the eye to the ear): TEMPLE?. 2. Zero-grade form *tmp- perhaps in: a. Persian taftan, to weave (the
1426:DIET? deiw- DIFFER bher-! DIFFICULTY dhé-1 DIFFIDENT bheidh- DIFFRACTION bhreg- DIFFUSE gheu- DIG dhigw- DIGEST gerere DIGIT deik- DIGNIFY dek-1 DIGNITY dek-1 DIGRESS ghredh- DIKE dhig¥- DILATE stela- DILATORY tela- DILIGENT leg-1 DILUTE leu(@)- DIME dekm DIMENSION mé-2 DIMER (s)mer-2 DIMINISH mei-2 DIMITY mei-4
1488:EXTOL tela- EXTORT terkw- EXTRA- eghs
2084:-PHAGE bhag-1 -PHAGIA bhag-! PHAGO- bhag-1 -PHAGOUS  bhag-! PHALANGE bhelg- PHALANX bhelg- PHALAROPE bhel-1, ped-1 PHALLUS bhel-2 PHANEROGAM bha-! PHANTASM_ bha-! PHANTASMAGORIA bha-1 PHANTOM bha-1 PHARMACOPOEIA kWei-2 PHARYNX bher-2 PHASE bha-1 -PHASIA bha-2 PHELLEM bhel-2 PHELLODERM bhel-2 PHELLOGEN _bhel-2 PHENO- bha-1 PHENOMENON bha-1 PHEROMONE bher-1 PHILANDER ner-2 PHILANTHROPY ner-2 PHILATELY tela- -PHILE bhilo- -PHILIA bhilo- PHILLUMENIST leuk- PHILO- bhilo- PHILODENDRON deru -PHILOUS _bhilo- PHILTER bhilo- PHLEGETHON bhel-1 PHLEGM bhel-1 PHLEGMATIC bhel-1 PHLOEM bhlieu- PHLOGISTON bhel-1 PHLOGOPITE bhel-1, okw- PHLOX bhel-1 PHLYCTENA bhlieu- -PHOBE bheg¥- -PHOBIA bhegw- PHOEBE bheigw- PHOEBUS bheigw- PHONE! bha-2 -PHONE bha-2 PHONEME bha-2 PHONETIC bha-2 PHONO- bha-2 -PHONY bha-2 -PHORE bher-1 -PHORESIS bher-1 -PHOROUS bher-1 PHOS- bha-1 PHOSPHENE bha-1 PHOSPHORUS bha-1 PHOT bha-1
2336:TaaL del-2 TABES ta- TACET tak-1 TACHE dek-? TACHISM deik- TACHYLYTE leu-! TACHYPNEA pneu- TACIT tak-1 Tack! dek-2 TACT tag- TACTICS tag- TACTORECEPTOR tag- TAEL tele- TAENIA ten- TAFFETA temp- TAG! dek-2 TAHSILDAR dher-2 TAIL! dek-2 TAINT teng- Tad (s)teg- TAKE tak-2 TALE del-2 TALENT tela- TALES to- TALION tele- TALISMAN kWel-1 TALK del-2 TALLOW del-4 TAME deme-2 TAMPON tap- TANDEM to- TANG! denk- TANGENT tag- TANGIBLE tag- TANGLE? tenk-2 TANGORECEPTOR tag- TANSY dhwene- TANTALIZE tele- TANTALUS tele- TANTAMOUNT to- TANTRA ten- Tap! tap-
```


## [2026-10-15T02:26:35.249Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 -c \"\nimport json;d=json.load(open('../refs_online.json'))\nfor k in ['KLN','PLA','BQT','MON','WLD','IEC','HRN','HUB','ARY','PHD','NYB','SKT','LKT','AFM','CHEUNG']:\n  v=d.get(k) or {}; print(k, v.get('page_offset'), '|', str(v.get('lookup_hint'))[:500], '|', v.get('local_file'))\n\""
}
```


### [2026-10-15T02:26:35.742Z] TOOL RESULT

```
KLN KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages. | /home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt
PLA 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276). | HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor) | ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_pages.txt']
BQT vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf imag | ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt']
MON None | Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Aden | ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt']
WLD Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). | Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP. | ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt']
IEC TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root. | /home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt
HRN leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann. | /home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt
HUB leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number. | /home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt
ARY printed page = pdf page + 1 | Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image | ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt']
PHD leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB). | /home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD.txt
NYB Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs. | /home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol2_glossary.txt
SKT leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags. | /home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt
LKT leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number. | /home/sfmqrb/git/rishe-private/data/verification/sources/refs/LKT.txt
AFM 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image | Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير'). | ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM.txt']
CHEUNG None | None | None
```


## [2026-10-15T02:26:37.662Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i '^atlas\\|^Atlantic' KLN_1966.txt | head; awk 'BEGIN{RS=\"\\f\"} NR==74{print}' KLN_1966.txt | grep -n -i -A8 'atlas' | head -50"
}
```


### [2026-10-15T02:26:38.050Z] TOOL RESULT

```
3849:Atlantic,  adj.,  pertaining  to  the  Atlantic  Ocean or  to  Mount  Atlas.  —  L.  Atlanticus,  fr.  Gk. ’AxXavx<.xo<;,  fr.  "AxXap,  ‘the  Atlas  mountains’. See  Atlas  and  -ic.
3850:Atlas,  n.,  one  of  the  Titans,  son  of  lapetus  and Clymene,  supporting  the  heavens  on  his  shoul¬ ders;  later,  a  king  of  Mauretania,  changed  by Perseus  into  Mt.  Atlas  ( Greek  mythol.)  —  L. Atlas  (gen.  Atlantis),  fr.  Gk.  ’'AxXocp  (gen.  "Ax- Xavxop),  which  stands  for  ”A-xXa<;  and  lit.  means ‘the  Bearer  (scil.  of  Heaven)’,  fr.  copul.  pref.  4- and  the  stem  of  xXrjvoa,  ‘to  bear’  (cp.  jxoXu- xXa?,  ‘much-enduring’).  Copul.  pref.  4-  stands for  I.-E.  *sm-,  a  weak  gradational  form  of  I.-E. base  *sem-,  ‘one,  together’ ;  see  same.  Gk.  xXrjvai derives  fr.  *//-,  zero  degree  of  I.-E.  base  *tel-, *tal-,  *tol-,  ‘to  bear,  lift,  suffer’,  whence  xaXa 4, gen.  xaXcrvop  and  x4Xavxo9,  ‘bearing,  suffer¬ ing’,  TxXdooai  (aor.),  ‘to  bear,  suffer’,  L.  tol- lere,  ‘to  lift  up,  raise’,  tolerare,  ‘to  bear,  sup¬ port’.  See  tolerate  and  cp.  atlas,  name  of  the first  vertebra,  atlantes,  Atlantic,  Atalanta, talent.
3851:atlas,  n.,  a  collection  of  maps  bound  into  a  book. —  First  so  called  by  the  geographer  Mercator because  the  figure  of  Atlas  supporting  the  world was  frequently  put  on  the  front  page  of  such collections.  (The  first  part  of  Mercator’s  Atlas, sive  cosmographicae  meditaliones  defabrica  mun- di  appeared  in  1585.)  See  prec.  word, atlas,  n.,  name  of  the  first  vertebra  ( anal .)  — From  Atlas  (q.v.);  so  called  because  it  bears  the
```


## [2026-10-15T02:26:40.079Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; head -3850 KLN_1966.txt | tr -cd '\\f' | wc -c; grep -n -i '^toll,\\|^talent,\\|^tolerate,\\|^relate,\\|^translate,' KLN_1966.txt | head; "
}
```


### [2026-10-15T02:26:40.556Z] TOOL RESULT

```
75
32081:relate,  refer’,  fr.  re-  and  ferre,  ‘to  bear’.  See bear,  ‘to  carry’,  and  cp.  words  there  referred  to. Derivatives:  refer-able,  adj.,  referee  (q.v.), refer-ence,  n.  and  tr.  v.,  referendary  (q.v.),  re¬ ferendum  (q.v.),  referr-al,  n.,  referr-er,  n. referee,  n.  —  Formed  fr.  prec.  word  with  suff. -ee.  Cp.  referendum.
38043:talent,  n.  —  ME.,  ‘sum  of  money;  desire’,  fr.  L. talenta,  pi.  of  talentum,  fr.  Gk.  TccXavrov, ‘bal¬ ance’  (in  the  pi.,  ‘pair  of  scales’) ;  a  weight;  sum of  money  corresponding  to  a  talent  of  silver’,  fr. xdXaq,  gen.  TaXavTo?,  ‘bearing,  suffering,  en¬ during',  fr.  I.-E.  base  *tel,  *tal-,  *tol-,  ‘to  bear, carry,  support,  endure’,  whence  also  Gk.  raXda- axt  (aor.),  ‘to  bear,  suffer’,  OI.  tula,  ‘balance’, tulayati,  ‘lifts  up,  weighs’,  L.  tollere,  ‘to  lift  up, raise’,  tolerdre,  ‘to  bear,  support’.  See  tolerate and  cp.  Atalanta,  Atlas,  tael,  tantalus,  telamon. Cp.  also  thole,  ‘to  endure’.
39457:tolerate,  tr.  v.  —  L.  toleratus,  pp.  of  tolerdre,  ‘to bear,  support,  endure,  tolerate’,  from  the  stem of  tollere,  ‘to  lift  up,  raise’,  which  is  cogn.  with Gk.  xoXjroiv,  ‘to  carry,  bear’,  xcXapcov,  ‘a  broad strap  for  bearing  something’,  xaXdccrcrai  (aor.), ‘to  bear’,  xXr)jx<av,  ‘patient,  reckless,  miserable’, xXrjvat  (aor.),  ‘to  suffer,  endure’,  xaXocvxov, ‘balance  (in  the  pi.,  a  pair  of  scales);  a  weight’, xaXas,  gen.  xxXavo;,  and  xaXavxo;,  ‘bearing, suffering’,  ”A-xXa ;,  ‘the  Bearer  (scil.  of  Heav¬ en)’,  rroX'3-xXac  ‘much  enduring’,  L.  hit  us  (for *tlatos)  ‘borne’  (used  as  pp.  of  ferre,  ‘to  bear, carry’),  OI.  tula,  ‘balance’,  tulayati,  ‘lifts  up, weighs’,  Toch.  B  tal-,  A  tal-,  ‘to  lift’,  tldssi,  ‘to lift,  carry’,  cakal,  ‘he  lifted’.  Arm.  tolum,  ‘I allow,  suffer,  bear’,  Lith.  tiltas,  ‘bridge’,  Goth. pulan,  ON.  pola,  OE.  pollan,  ‘to  endure,  suffer’. All  these  words  derive  fr.  I.-E.  base  *tel-,  *tol-, *tal-,  *tl-,  ‘to  bear,  carry,  endure,  suffer’.  Cp. ablation,  ablative,  allative,  Atalanta,  atlantes, Atlantic,  Atlas,  collate,  collation,  delate,  dila¬ tory,  elate,  extol,  illation,  oblate,  prelate,  prolate, relate,  relation,  sublate,  sublation,  superlative, tael,  talent,  Tantalus,  telamon.  Telamon,  thole, ‘to  endure’,  tola,  toll,  ‘tax’,  toll,  ‘to  take  away’, tralatitious,  translate,  translation  and  the  second element  in  acceptilation,  fiddle,  legislate. Derivatives:  toleration  (q.v.),  tolerat-ive,  adj., tolerat-or,  n.
39461:toll,  n.,  tax.  —  ME.  tol,  fr.  OE.  toll,  rel.  to  OS. tolna,  ON.  tollr,  Dan.  told,  Swed.  lull,  OFris. tolen,  tolne,  OHG.,  MHG.  zol,  G.  Zoll\  borrow¬ ed  fr.  Late  L.  toloneum,  ‘custom  house’,  which was  formed  with  vowel  assimilation  fr.  earlier telonium,  teldneum,  fr.  Gk.  xsXtovetov,  ‘toll house’,  fr.  xeXcovy;?,  ‘tax  collector-,  fr.  xsXoi;, ‘tax’  (whence  also  efi-XEXfj;,  ‘easily  paid  for, cheap’,  rroXo-xeXf,;,  ‘very  expensive,  costly’, i-rzr.rfi,  ‘free  from  tax  or  tribute’),  which  is cogn.  with  xxXdoooa  (aor.),  ‘to  bear,  support’; see  tolerate.  For  sense  development  cp.  Gk. <popo<;,  'tax,  tribute',  which  is  rel.  to  ^speiv,  ’to bear,  carry’.  Cp.  the  first  element  in  tolbooth and  in  zollverein.
39463:toll,  tr.  v.,  to  attract,  allure.  —  ME.  toilen,  tullen, ‘to  draw,  pull,  attract’,  in  gradational  relation¬ ship  to  ME.  tillen,  tyllen,  ‘to  draw,  puli’.  See till,  ‘drawer’,  and  cp.  next  word.
39464:toll,  tr.  v.,  to  cause  to  sound;  intr.  v.,  to  sound. —  ME.  toilen,  tullen,  ‘to  draw,  pull’ ;  see  prec. word.  Toll  orig.  meant  ‘to  draw  a  bell  so  that it  sounds’.
39466:toll,  tr.  v.,  to  take  away.  —  ME.  toilen,  fr.  AF. toller,  fr.  L.  tollere,  ‘to  lift  up,  raise;  to  take away'.  See  tolerate, tollbooth,  n.  —  See  tolbooth. tolpatch,  n.,  a  foot  soldier.  —  G.  Tolpatsch,  fr. Hung,  talpas,  lit.  ‘having  big  feet’,  fr.  talp,  ‘sole of  the  foot,  foot’.
39861:translate,  tr.  v.,  —  L.  translatus,  ‘carried  over’ (used  as  pp.  of  transferre,  ‘to  carry  over’),  fr. trans-  and  latus,  ‘borne,  carried’  (used  as  pp.  of ferre,  ‘to  bear,  carry’),  which  stands  for  *tlatos, fr.  *//-,  zero  degree  of  I.-E.  base  *te!-,  *tol-,  ‘to bear,  carry’,  whence  L.  tollere,  ‘to  lift  up,  raise’, tolerare,  ‘to  bear,  support’.  See  tolerate  and  cp. tralatitious.
```


## [2026-10-15T02:26:43.359Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'tar[aā]z' HRN.txt HUB.txt PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt CHEUNG.txt BRT.txt | head -40"
}
```


### [2026-10-15T02:26:43.699Z] TOOL RESULT

```
PHD.txt:593:tan-bahr [żn'Þ’ hl] physique. tand [tnd | = P] faint, languishing. ~ih: faintness, langour. | tan-drust [tn'drw(y)st! | N ~] healthy, whole. ~ih: health. tang [ing | = M, N ~] narrow, tight. ~ih: narrowness; distress. tanig [tn'yk! | N tani] bodily, corporal. tanigard(ig) [tnykrt(yk)! | M inygyrd] corporeal. ` tanīhā [tn'y/? | M tnyP?, N tanha] alone. tanómand [tn wmnd | N ~] corporeal. “АҺ: corporeality. tan-tdhmag [tn'twhmk'] (sap) of plants. tanuk [tnwk! | N ~] thin, shallow, tanür [tnw] | M tnwr, N ~] oven. tar [LCDr! < A l-sd; tl | M tr] over, through, across. ~ kardan, ~ menidan: abuse, despise. -tar [-z# | (M -dr), N ~] suffix forming comparative adjectives. tar [2] | M гу] darkness. tarāzēnīdan, tarāzēn- [tcyn-ytn!] weigh. tarázüg [tPcwk! | (P tPzwg), N tarazü] balance, scales; astr. Libra. targ [tlg | N ~] helmet. tarģumān [tigm?n! | M trgwmn] interpreter. tarig/k [PIyk! | M гуур, N tárik!] dark. ~th: darkness. tarist [¢/st'] = tar. tar-mānīh [t/m’nyh] perversity. tar-menišn [tImynin! | N tarmanist] perverse; contemptuous. 7h : perversity; contempt. tarr [t/, LC Dr (in error, v. tar) | N —] moist, fresh. ~ag [tik! | N ~a] vegetable. tars [2/5 | M trs, N ~] fear, respect. tarság [ts k! | M trs’g, N tarsā] Christian. tarsāģāh [15(?)/?5] respectful, reverent. ~ih: respect, reverence. tarsidan, tars- [tls-ytn' | (M tyrs??dn), N ~] fear, be afraid. tarwénidan, tarwēn- [t/zvyn-ytn! | M trw-] overcome, conquer. tas [25 | N ~] die (for gaming). tasum [tswm | = M] fourth. tāšīdan, tāš- [O i-ytn!'] cut, cleave; create. taSkanag [tšknk!] under-shirt. tašt [tšt' | N ~] bowl. tāšt [021] *certainty. ~ig [-yk'] certain. tāwān [1?(d)w’n' | N ~] compensation, obligation. taxl [t?% | (M thr), P txl, N talx] bitter.
PHD.txt:919:balance tarāzūg.
PHD.txt:2614:Libra Tarazig.
PHD.txt:3525:scales tarāzūg.
PHD.txt:4297:weigh saxtan, tarazénidan. weight garanih.
PHD.txt:4471:tar, tarr tarazén- tarāzēnīdan tarāzūg piht
PHD_mackenzie.txt:4926:tarazenidan, tarazen- [tl)cyn-ytn l ] weigh.
PHD_mackenzie.txt:4927:taraziig [tPcwk I (P tl)zwg), N tarazu] balance, scales; astr. Libra.
PHD_mackenzie.txt:5995:astonishment skeftih, widimustih.        balance tarazUg.
PHD_mackenzie.txt:7493:rouse wigdidan, (gubras-).                 scales tarazug.
PHD_mackenzie.txt:7954: u'eigh saxtan, tarazenidan.            witch parig.
PHD_mackenzie.txt:8169:tom                            -6\0     tarazcnidan             "tf..'~~~
PHD_mackenzie.txt:8172:anoh   I                     ~    .     tarazug
NYB_vol2_glossary.txt:3727:191 tarāzūk
NYB_vol2_glossary.txt:3737:tarazčnitarčh [tl’eynyt’lyh] the act of weighing 72!5. — From taräzenitan ‘to weigh', den. of
NYB_vol2_glossary.txt:6954:$van-: !sak Sveta-: spét $vitra-: spihr tanu-: tanük tarna-ka-: tarr taruna-: tarr tavat: han-tài trpra-: sapük tulà: tarāzūk udara-: *ud(a)rài ud-vat-: yuvat upäka: tapak
```


## [2026-10-15T02:26:46.281Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 3720,3745p NYB_vol2_glossary.txt; sed -n 6945,6956p NYB_vol2_glossary.txt; grep -n 'tarāz\\|taraz\\|ترازو' HRN.txt HUB.txt CHEUNG.txt | head; grep -n 'ترازو' incoming/ARY/ARY_pages.txt | head; grep -n -i 'TARAZ' incoming/ARY/ARY_latin_index_pages.txt | head"
}
```


### [2026-10-15T02:26:46.830Z] TOOL RESULT

```
tangéh distress, straits 6615,
Tansar [tnsl] n. pr. the High Priest of Artaxsér 1092-3. 11118. — This is the traditional reading; but the transliter- ation twsr in Arabic letters is also found, and this reading seems to be confirmed
by the patron. twsrkn KZŠPrth 1. 24 =.
Prs twslk*n; the correct form would then be Tösar, v. Boyce, A.M., N.S. V, 1955, 50 n. 3.
tanomand [tn'"wmnd] provided with a body 10474; v. also pat-tanömand.
tanük [tnwk'] scarce, rare 971923, — NP tanuk ‘slender, thin’; Skr tanu-, Lat tenuts.
tapah [tp’h] spoiled, ruined; ~ kartan to kill, to destroy, to spoil 84%; ~ bütan
191 tarāzūk
to be spoiled 81**. — Paz. tawāh; NP tabāh.
tapāhēh annihilation 45». tapahenitan to destroy, to kill 5526,
tap [t’p'] fever 4323. — From tāftan (g.v.); ci MPrs tb ‘fever’ (S), NP tab; NP tab, tāv ‘heat, warmth, burning’. ‘Fever’ is
in Av. (632) tafnah-, tafnu-; NP taf ‘heat’. täpistän [t’pst’n'] summer 864, — Paz.
tāvastan; NP täbistän.
Mar [Prth LSD; Prs LSD-r; tl] 1. prep. beyond HajA:7 (LSD L- = tar 6). B: 7; through 1032; via, by way of 361°. 3813. 4115, — 2. adv. aside, secretly 421° [tl]. — V. also tarist, turist, hu-tarist. — Av. (641) tarč (‘secretly’ Vd. 15"); OP tara’; MPrs jr, try (S); Ps. LSD-r and tlyšy (cf ’esy = BP hactš).
?tar [tl] 1. subst. arrogance, contempt: ~ menitan to treat with arrogance, with contempt 3314. — 2. adj. contemptible: ~ kartan to make contemptible, to dis- honour 738; ~ u andzarmik kartan 758-4, Skr. v. hina; [Paz. Gar x“ār kard made contemptible and mean SGV XI, 56; hast i dar x"àr u anāžarm kard some of them were made contemptible, mean and dishonoured, ibd. XII, 40; Skr. v. also here hina]. — That ~ is used in BP as an independent noun, subst. or adj., is beyond doubt, but etymologically it is
identical with the prep. and prev. čar,
and secondarily abstracted from the Av. (1123 sq.) tard man- ‘to dishonour’ and (641) tard.mati- ‘obstinacy, recalcitrance’. V. also tar-menisneh.
tarazčnitarčh [tl’eynyt’lyh] the act of weighing 72!5. — From taräzenitan ‘to weigh', den. of
taräzük  [tl'ewk'] balance, scales for weighing 72%, — Olr *arä = Skr čula ‘balance, scale of a balance’ + Av. (223 sg.) az- ‘to convey, to conduct’
(Lat agere).
www.parsianjoman.org | col wok
tarik
192
Tatragat(i) vas
pumu ja Z RR ———————— sb SA ČR u
tārīk [t*lyk] dark 377°. 762. 859.1339, - M PrthPrs t’ryg, derived from Av. (650) iq0ra- ‘darkness’, MPrthPrs vr; NP tar ‘dark, obscure’; tārīk < *tqOriya-ka-, Av. taūrya- ‘dark’.
zadan: zatan zädan, zāēd: zätan zahisn: jayisn
Sanskrit
khan-: kandan krmi-: kirm ksira-: Sir ksipra-: "šif(a)rg ksubh-: višuftan lapati: rāpak-karēh lup-: *uzruftak maryá-: mérak matsya-: mahik modate: mustäpät, X6sr6i-mustapat muficáti: ämöxtan mus-: must namrá-: a-namr-tom nastikya, nàstika: anäst nikrti- (nikrta-): nikérai ni-vat-: yuvat padäti(ka)-: padätak pävaka-: päk pinasti: pist prarecana-: fréc prareka-: fréc pratyafic-: paitak pravät-, pravätä: yuvat rathyä: rahy rta-: Art-vahist
www.parsianjoman.org | olw
zama: zaman zani: zan z(a)reh: zréh Zargar: Zarér zari: zarik
zarin: zarrén zindaa: zivandak zindan: zčndan zišt: zčšt zivastan: zivistan zreh, zrih: zrah zufaé: zahyäi zufr: ~ Zuhūdaa - Zuhūda | : Yahüd
zurug: Zurvàn
sahasra-: hazar sama-bhàgin: ham-bài smar-: ó$murtan su-Sravas-: hu-srav šakta-: saxt
säs-: "a-sištak sri-: 2sih
$van-: !sak Sveta-: spét $vitra-: spihr tanu-: tanük tarna-ka-: tarr taruna-: tarr tavat: han-tài trpra-: sapük tulà: tarāzūk udara-: *ud(a)rài ud-vat-: yuvat upäka: tapak
va + -pi: aivap vara-: ham-var vatsa-: vaccak vāyu-: *vai
vic-: lvéxtan vicära, vicärayati: vicar vijate: ?vöxtan vrsan-: gusn
```


## [2026-10-15T02:26:56.379Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; for w in '%D8%AA%D8%B1%D8%A7%D8%B2%D9%88' '%D8%B7%D8%B1%D8%A7%D8%B2' '%D8%AA%D8%B1%D8%A7%D8%B2' '%D8%A7%D8%B7%D9%84%D8%B3' 'Reconstruction:Proto-Indo-European/tel%E1%B8%A5%E2%82%82-' '%E1%BC%8C%CF%84%CE%BB%CE%B1%CF%82' '%E0%A4%A4%E0%A5%81%E0%A4%B2%E0%A4%BE'; do echo \"=== $w\"; curl -s \"https://en.wiktionary.org/w/index.php?title=$w&action=raw\" | grep -v '^\\s*$' | head -60; done 2>&1 | head -300"
}
```


### [2026-10-15T02:26:57.881Z] TOOL RESULT

```
=== %D8%AA%D8%B1%D8%A7%D8%B2%D9%88
{{also|تزارو}}
==Ottoman Turkish==
[[Image:Balance à tabac 1850.JPG|thumb|{{lang|ota|ترازو}}]]
===Etymology===
{{ety|ota|:bor|fa:ترازو<t:balance, scales><tr:tarâzu>|text=+|tree=1}}
===Noun===
{{head|ota|noun|tr=tarazu|tr2=terazi}}
# [[balance]], pair of [[scales]], a [[device]] for measuring [[weight]]
#: {{syn|ota|میزان|tr=mizan}}
# {{lb|ota|by extension}} any [[weigh]]ing or [[measure|measuring]] [[apparatus]]
# {{lb|ota|astronomy}} [[Libra]], a [[constellation]] of the [[Zodiac]]
#: {{syn|ota|میزان|tr=mizan}}
# {{lb|ota|astrology}} [[Libra]], the [[zodiac sign]] for the [[scales]]
#: {{syn|ota|میزان|tr=mizan}}
# {{lb|ota|figuratively}} [[balance]], [[equality]], [[equilibrium]], [[stability]]
====Derived terms====
{{col3|ota
|ترازو شاهینی<t:tongue of a balance><tr:terazi şahini>
|ترازوسز<t:without balance, unequal><tr:terazisiz>
|ترازولو<t:well-balanced, equal><tr:terazili>
|صو ترازوسی<t:water-balance><tr:su terazisi>
|صیجاق ترازوسی<t:thermometer><tr:sıcak terazisi>
|هوا ترازوسی<t:barometer><tr:hava terazisi>
}}
====Descendants====
* {{desc|tr|terazi}}
* {{desc|hy|թերազի|թա̈րա̈զո̈ւ|bor=1}}
* {{desc|mk|терезија|bor=1}}
* {{desc|axm|թէրազու|bor=1}}
* {{desc|sh|terazije|bor=1}}
* {{desc|sq|terezi|bor=1}}
===Further reading===
* {{R:tr:OTK|terazi2|vol=1|page=4747}}
* {{R:ota:Kelekian|page=358}}
* {{R:ota:Meninski|C|column=947|Libra}}
* {{R:ota:Meninski|T|column=1136}}
* {{R:tr:Nishanyan|terazi}}
* {{R:ota:Redhouse|page=525}}
{{C|ota|Measuring instruments|Constellations in the zodiac}}
==Persian==
===Etymology===
{{ety|fa|:inh|pal:<tr:tlʾcwk'><ts:tarāzūg><ety:bor<ae:𐬙𐬀𐬭𐬀.𐬀𐬰𐬎<alt:𐬙𐬀𐬭𐬀.𐬀𐬰𐬎>>>|tree=1}}
From {{inh|fa|pal||tr=tlʾcwk'|ts=tarāzūg|t=balance, scales|sc=Phlv}} (compare {{cog|xpr|𐫤𐫓𐫀𐫉𐫇𐫃|tr=tlʾzwg|ts=talāzūg|sc=Mani}}), borrowed from {{der|fa|ae|𐬙𐬀𐬭𐬀.𐬀𐬰𐬎|𐬙𐬀𐬭𐬀.𐬀𐬰𐬎}}. Compare {{cog|sa|तुला}}. Akin to the Iranian borrowings: {{cog|xcl|տարազուկ}}, {{cog|udi|таьраьзуькӏ}}.
===Pronunciation===
{{fa-IPA|tarā`zū}}
===Noun===
{{fa-regional|ترازو|ترازو|тарозу}}
{{fa-noun|cls=تَرَازُو}}
# [[balance]], [[scales]]
#: {{syn|fa|میزان|tr1=mizân|q1=dated}}
#* {{quote-book|fa|year=c. 1260|chapter=4:634|title={{w|Masnavi|The ''Masnavi''}}|author=w:Rumi|text=اندر آن کفه‌ی ترازو ز اعتداد، او به جای سنگ آن گل را نهاد.|tr=andar ân kaffe-ye '''tarâzu''' z-e'tedâd, u be jâ-ye sang ân gel-râ nehâd.|t=He placed the clay, because of its being ready [to his hand], in one scale of the '''balance''' instead of the [proper] weight.|footer=(adapted from the {{w|Reynold A. Nicholson}} translation)}}
# {{lb|fa|figurative}} [[equilibrium]], [[balance]]
====Descendants====
{{top2}}
* {{desc|az|tərəzi|bor=on}}
* {{desc|chg|ترازو|tr=tarāzū|bor=1}}
** {{desc|ug|تارازا}}
** {{desc|uz|tarozi|tarozu}}
** {{desc|kk|таразы|bor=on}}
* {{desc|bn|তরাজূ|tr=tôrazū|bor=1}}
=== %D8%B7%D8%B1%D8%A7%D8%B2
==Arabic==
===Etymology 1===
See {{m|ar|طَرْز}}.
====Pronunciation====
{{ar-pr|طِرَاز}}
* {{rhymes|ar|aːz|s=2}}
====Noun====
{{ar-noun|طِرَاز|m|pl=طُرُز,أَطْرِزَة}}
# [[embroidery]], or a piece of [[embroidered]] [[textile]]
# [[fashion]], [[type]], [[form]], [[sort]], [[style]], [[model]] etc.
=====Declension=====
{{ar-decl-noun|طِرَاز|pl=طُرُز|pl2=أَطْرِزَة}}
===Etymology 2===
{{ar-occupational noun}} of {{m|ar|طَرْز}}.
====Pronunciation====
{{ar-pr|طَرَّاز}}
* {{rhymes|ar|aːz|s=2}}
====Noun====
{{ar-noun+|طَرَّاز|m}}
# [[embroiderer]]
#* {{q|feminine plural}} {{RQ:ar:Lévi-Provençal:1934|page=237 (٤٥) 14}}
=====Declension=====
{{ar-decl-gendered-noun|طَرَّاز|pl=smp}}
{{C|ar|Occupations}}
==Persian==
===Etymology 1===
Arabic respelling of a word which is originally a Persian loan into Arabic.
====Pronunciation====
{{fa-IPA|tiˈrāz}}
====Noun====
{{fa-noun|tr=terâz}}
# {{alternative spelling of|fa|تراز|tr=terâz|t=embroidery, embroidered ornament}}
===Etymology 2===
{{wp|fa:}}
====Pronunciation====
{{fa-IPA|taˈrāz}}
====Proper noun====
{{head|fa|proper noun|tr=tarâz}}
# {{place|fa|city|country/Kazakhstan|t1=Taraz|t2=Talas}}
=====Usage notes=====
* In classical Persian literature, Taraz/Talas is renowned for the beauty of its inhabitants and the quality of its [[musk]].
=== %D8%AA%D8%B1%D8%A7%D8%B2
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
<a href="https://www.wikimedia.org"><img id="logo" src="https://www.wikimedia.org/static/images/wmf-logo.png" srcset="https://www.wikimedia.org/static/images/wmf-logo-2x.png 2x" alt="Wikimedia" width="135" height="101">
</a>
<div class="content-text">
<h1>Error</h1>
<p>Not Found</p>
</div>
</div>
<div class="footer"><p>If you report this error to the Wikimedia System Administrators, please include the details below.</p><p class="text-muted"><code>Request served via cp1106 cp1106, Varnish XID 472318333<br>Upstream caches: cp1106 int<br>Error: 404, Not Found at Thu, 15 Oct 2026 02:26:57 GMT<br><details><summary>Sensitive client information</summary>IP address: 74.14.198.44</details></code></p>
</div>
</html>
=== %D8%A7%D8%B7%D9%84%D8%B3
{{also|أطلس}}
==Arabic==
===Etymology===
{{ety|ar|nl=1}}
===Verb===
{{ar-verb form|+طلس<I>}}
==Persian==
===Pronunciation===
{{fa-IPA|atˈlas}}
===Etymology 1===
{{bor+|fa|ar|أَطْلَس}}, from {{der|fa|grc|Ἄτλας}}.
====Proper noun====
{{head|fa|proper noun|tr=atlas}}
# {{lb|fa|Greek mythology}} [[Atlas]]
=====Derived terms=====
{{col|fa
|اقیانوس اطلس<tr:oqyânus-e atlas><t:Atlantic Ocean>
|کوه‌های اطلس<tr:kuh-hâ-ye atlas><t:Atlas Mountains>
}}
====Noun====
{{fa-noun|tr=atlas}}
# [[atlas]] (collection of maps)
===Etymology 2===
{{bor+|fa|ar|أَطْلَس}}.{{root|fa|ar|ط ل س}}
====Noun====
{{fa-noun|tr=atlas}}
# {{C|fa|Fabrics}} [[satin]]
==Urdu==
[[Image:Deep petrol blue evening gown by Sybil Connolly.jpg|250px|thumb|نیلا اطلس]]
===Etymology===
{{ety|ur|:bor|fa-cls:اطلس<tr:atlas><ety:uder<ar:أَطْلَس>>|text=2|tree=1}}
===Pronunciation===
* {{ur-IPA|atlas}}
===Noun===
{{ur-noun|m|hi=अतलस|tr=atlas}}
# [[satin]]
====Declension====
{{ur-noun-c-m|اطلس|atlas}}
{{c|ur|Fabrics}}
=== Reconstruction:Proto-Indo-European/tel%E1%B8%A5%E2%82%82-
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
<a href="https://www.wikimedia.org"><img id="logo" src="https://www.wikimedia.org/static/images/wmf-logo.png" srcset="https://www.wikimedia.org/static/images/wmf-logo-2x.png 2x" alt="Wikimedia" width="135" height="101">
</a>
<div class="content-text">
<h1>Error</h1>
<p>Not Found</p>
</div>
</div>
<div class="footer"><p>If you report this error to the Wikimedia System Administrators, please include the details below.</p><p class="text-muted"><code>Request served via cp1106 cp1106, Varnish XID 471565174<br>Upstream caches: cp1106 int<br>Error: 404, Not Found at Thu, 15 Oct 2026 02:26:57 GMT<br><details><summary>Sensitive client information</summary>IP address: 74.14.198.44</details></code></p>
</div>
</html>
=== %E1%BC%8C%CF%84%CE%BB%CE%B1%CF%82
{{also|άτλας|Άτλας}}
==Ancient Greek==
{{wp|Atlas<dab!>}}
===Etymology===
{{root|grc|ine-pro|*sem-|*telh₂-|id2=bear}}
Perhaps from {{m|grc|ἁ-|pos=copulative prefix}} + {{der|grc|ine-pro|*telh₂-}}, the root of {{m|grc|ἔτλην||to suffer, to endure}}. Beekes suggests it is a {{der|grc|qsb-grc|-}} word.
===Pronunciation===
{{grc-IPA|ά̆τλᾱς}}
===Proper noun===
{{grc-proper noun|Ἄτλαντος|m|third|head=Ἄτλᾱς}}
# {{lb|grc|Greek mythology}} [[Atlas]]
# [[Atlas Mountains]]
====Inflection====
{{grc-decl|Ᾰ̓́τλᾱς|Ᾰ̓́τλᾰντος}}
====Derived terms====
* {{l|grc|Ἀτλαντικός}}
* {{l|grc|Ἀτλαντίς}}
====Descendants====
* {{desc|el|Άτλας|Άτλαντας}}
* {{desc|ga|Atlás}}
* {{desc|la|Atlas|bor=1}} {{see desc}}
===References===
* {{R:grc:LSJ|*)/atlas}}<!-- template doesn't accept capitals -->
* {{R:grc:Middle Liddell}}
* {{R:grc:Autenrieth}}
* {{R:grc:DGE}}
* {{R:grc:Slater}}
* {{R:grc:Woodhouse|1003}}
* {{R:grc:Beekes|volume=I|page=163}}
{{c|grc|Mythological figures|Mountains}}
=== %E0%A4%A4%E0%A5%81%E0%A4%B2%E0%A4%BE
{{also|तूळ|तौल|तूलि|तिल|ताला|तल|ताली|तेल}}
==Hindi==
{{wp|hi:+ राशि}}
{{wp|hi:+ तारामंडल}}
[[File:LibraCC.jpg|thumb|'''तुला तारामंडल''']]
===Etymology===
{{bor+|hi|sa|तुला}}. {{doublet|hi|तुली}}.
===Pronunciation===
* {{hi-IPA}}
===Noun===
{{hi-noun|f|ur=تلا}}
# [[balance]], [[scales]]
#: {{syn|hi|मापन|तराज़ू}}
====Declension====
{{hi-ndecl|<F>}}
===Proper noun===
{{hi-proper noun|f|ur=تلا}} (symbol [[♎]]&#xFE0E;)
# {{lb|hi|astrology}} [[Libra]]
# {{lb|hi|astronomy}} [[Libra]] [[constellation]]
====Declension====
{{hi-ndecl|<F.sg>}}
===See also===
{{table:zodiac/hi}}
===References===
* {{R:hi:Dasa||2117}}
* {{R:hi:Chaturvedi||292}}
* {{R:hi:McGregor||458}}
==Marathi==
===Pronunciation===
* {{mr-IPA}}
===Etymology 1===
{{rfe|mr}}
====Pronoun====
{{mr-pron}}
# {{inflection of|mr|तू||acc}}
# {{inflection of|mr|तू||dat}}
===Etymology 2===
{{bor+|mr|sa|तुला}}.
====Noun====
{{mr-noun|g=f}}
# [[balance]], [[scales]]
#: {{syn|mr|तराजू|tr=tarāj̈ū}}
==Pali==
```


## [2026-10-15T02:27:03.908Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /tmp; for w in '%F0%90%AC%99%F0%90%AC%80%F0%90%AC%AD%F0%90%AC%80.%F0%90%AC%80%F0%90%AC%B0%F0%90%AC%8E' 'Reconstruction:Proto-Indo-European/telh%E2%82%82-' '%D8%B7%D8%B1%D8%B2' '%D8%A3%D8%B7%D9%84%D8%B3' 'Reconstruction:Proto-Iranian/tar%C4%81%CC%81%C4%87u%C5%A1' '%D8%A2%D8%AA%D9%84%D8%A7%D9%86%D8%AA%DB%8C%DA%A9' 'Atlantic' 'toll'; do echo \"=== $w\"; curl -s \"https://en.wiktionary.org/w/index.php?title=$w&action=raw\" | grep -v '^\\s*$' | head -45; done 2>&1 | grep -v 'Wikimedia\\|^<\\|{ \\|^\\.\\|^\\*\\|^ \\|^@\\|^}' | head -250"
}
```


### [2026-10-15T02:27:05.292Z] TOOL RESULT

```
=== %F0%90%AC%99%F0%90%AC%80%F0%90%AC%AD%F0%90%AC%80.%F0%90%AC%80%F0%90%AC%B0%F0%90%AC%8E
=== Reconstruction:Proto-Indo-European/telh%E2%82%82-
{{reconstructed}}
==Proto-Indo-European==
===Root===
{{etymon|ine-pro|id=bear|pos=root}}
{{ine-root|pf}}<ref>{{R:itc:EDL|page=621-622|head=tollō, -ere}}</ref><ref name="LIV">{{R:ine:LIV|page=622-623}}</ref>
# to [[bear]], to [[undergo]], to [[endure]]
====Derived terms====
{{rootsee|id=bear}}
=== %D8%B7%D8%B1%D8%B2
==Arabic==
===Etymology===
{{ety|ar|id=stitch}}
An older {{doublet|nocap=1|ar|دَرْز|t1=suture}}. Compare {{cog|fa|تراز|tr=tarâz|t=raw silk}}, {{m|fa|تراز|tr=terâz, torâz|t=beauty, adornment}}, {{m|fa|ترازیدن|tr=tarâzidan|t=to adorn, to embellish; to embroider}}, with the vocalism also passed as {{m+|ar|طِرَاز}}, and this spelling made the Persian spelling {{m|fa|طرازیدن|tr=tarâzidan}}. Note also {{cog|xcl|տարազ}}, a Middle Iranian borrowing.
===Pronunciation===
{{ar-pr|طَرَّزَ}}
===Noun===
{{ar-noun|طَرْز|m|pl=طُرُوز}}
# a [[stitch]], [[suture]]
# [[fashion]], [[type]], [[form]], [[sort]], [[style]], [[model]] etc.
====Declension====
{{ar-decl-noun|طَرْز|pl=طُرُوز}}
====Descendants====
===Verb===
{{ar-verb|I/i~a.nopass.vn:طَرَز.ap:+++}}
# to be or become [[goodly]] in [[shape]] or [[apparel]]
====Conjugation====
{{ar-conj|I/i~a.nopass.vn:طَرَز.ap:+++}}
===Verb===
{{ar-verb|II}}
# to [[embroider]]
====Conjugation====
{{ar-conj|II}}
===References===
==Persian==
===Etymology===
{{bor+|fa|ar|طَرْز}}, from {{der|fa|fa|درز|tr=darz}}, from {{der|fa|ira-pro||*darz-|t=to fasten, to sew}}.
===Pronunciation===
{{fa-IPA|tarz}}
===Noun===
=== %D8%A3%D8%B7%D9%84%D8%B3
{{also|اطلس}}
==Arabic==
===Etymology 1===
{{wp|ar:}}
Borrowed from {{bor|ar|grc|Ἄτλας}}.
====Pronunciation====
{{ar-pr|أَطْلَس}}
====Proper noun====
{{ar-proper noun|أَطْلَس|m}}
# {{lb|ar|Greek god}} [[Atlas]]
=====Declension=====
{{ar-decl-noun|أَطْلَسُ|state=ind-def}}
=====Related terms=====
===Etymology 2===
{{wp|ar:+ (خرائط)}}
Borrowed from {{bor|ar|en|atlas}}, named after the mythical Greek Titan {{m|grc|Ἄτλας}}.
====Pronunciation====
{{ar-pr|أَطْلَس}}
====Noun====
{{ar-noun|أَطْلَس|m|pl=أَطَالِس}}
# [[atlas]] {{gloss|collection of maps}}
=====Declension=====
{{ar-decl-noun|أَطْلَسُ|pl=أَطَالِسُ}}
===Etymology 3===
{{ety|ar|id=rag}}
{{ar-rootbox|ط ل س}}
====Pronunciation====
{{ar-pr|أَطْلَس}}
====Adjective====
{{ar-adj|أَطْلَس|f=طَلْسَاء|pl=طُلْس}}
# [[worn-out]], having the [[quality]] of a [[rag]]
# [[filthy]], having a [[dusty]] [[hue]]
# having a [[skin]] of [[dark]] [[pigmentation]].
=====Declension=====
{{ar-decl-adj|أَطْلَس:cd}}
{{wp|ar:نسيج +}}
====Noun====
{{ar-noun|أَطْلَس|m|pl=طُلْس}}
# [[satin]]
=====Declension=====
{{ar-decl-noun|أَطْلَسُ:di|pl=طُلْس}}
=====Descendants=====
=== Reconstruction:Proto-Iranian/tar%C4%81%CC%81%C4%87u%C5%A1
=== %D8%A2%D8%AA%D9%84%D8%A7%D9%86%D8%AA%DB%8C%DA%A9
=== Atlantic
==English==
{{wp}}
{{swp|+, Iowa}}
===Alternative forms===
===Etymology===
{{etymon|en|:inh|enm:Atlantyke|tree=+}}
{{root|en|ine-pro|*telh₂- (bear)}}
From {{inh|en|enm|Atlantyke}}, from {{der|en|la|ā̆tlanticus|Ā̆tlanticus}}, from {{der|en|grc|Ἀτλαντικός||[[Atlantean]], of Atlas}}, from {{der|en|grc|Ἄτλᾱς}}, either from {{m|grc|ἁ-|pos=copulative prefix}} + {{der|en|ine-pro|*telh₂-||bear, undergo, endure}} or of {{der|en|qsb-grc|-}} origin.
===Pronunciation===
===Proper noun===
{{en-proper noun|head=the Atlantic}}
# The [[Atlantic Ocean]].
#* {{quote-journal|1=en|date=3 September 2026|author=James Gregory|title=More than 80 migrants feared dead after boat rescued off Canary Islands|url=https://www.bbc.co.uk/news/articles/c33kzv7kly4o|journal={{w|BBC News}}|text=Fernando Clavijo, head of the Canary Islands government, posted on X: "It is intolerable that lives continue to be lost. The Canaries cannot get used to or accept as normal the fact that '''the Atlantic''' continues to be a death trap."|accessdate=3 September 2026|archiveurl=https://web.archive.org/web/20261002234449/https://www.bbc.co.uk/news/articles/c33kzv7kly4o|archivedate=2 October 2026}}
# A [[phase]] of the [[Holocene]] [[epoch]] in the {{w|Blytt–Sernander system}}, [[extend]]ing from [[approximately]] 8,000 to 5,000 [[year]]s before present.
===Proper noun===
{{en-proper noun}}
# A [[branch]] of the [[Niger-Congo]] [[language]]s [[speak|spoken]] along the Atlantic [[coast]] in [[West Africa]].
# {{place|en|city/county seat|co/Cass County|s/Iowa|c/USA}}.
====Derived terms====
{{col3|en|Atlantic Standard Time Zone
|amphiatlantic
|Atlantic City|Atlantic County|Atlantic croaker
|Atlantic Daylight Time
|Atlantic Flyway
|Atlantic ghost crab
|Atlantic Highlands|Atlantic hookear sculpin|Atlantic humpback dolphin
|Atlantic silverside|Atlantic sixgill shark|Atlantic sturgeon
|Atlantic tarpon|Atlantic Time|Atlantic trumpetfish
|Atlantic Wall
|circum-Atlantic
|East Atlantic peacock wrasse|Euro-Atlantic
|Graveyard of the Atlantic
|Mid-Atlantic
|North Atlantic Treaty Organisation,North Atlantic Treaty Organization
|Subatlantic
|trans-Atlantic,transatlantic
|West Atlantic trumpetfish
=== toll
{{also|Toll}}
==English==
{{wp}}
===Pronunciation===
===Etymology 1===
{{ety|en|:inh|enm:toll|id=fee}}
From {{inh|en|enm|toll|id=toll}}, {{m|enm|tol|id=toll}}, {{m|enm|tolle|id=toll}}, from {{inh|en|ang|toll|g=m|g2=n}} and {{m|ang|toln|g=f|t=toll, duty, custom}}, from {{inh|en|gmw-pro|*toll}}, {{m|gmw-pro|*tolnu}}, from {{inh|en|gem-pro|*tullaz}}, {{m|gem-pro|*tullō|t=that which is counted or told, reckoning}}, from {{der|en|ine-pro|*del-||calculation, fraud}}.<ref>Whitney, ''The Century dictionary and cyclopedia'', toll.</ref>
Cognate with {{cog|stq|Tol||toll}}, {{cog|nl|tol||toll}}, {{cog|de|Zoll||toll, duty, customs}}, {{cog|da|told||toll, duty, tariff}}, {{cog|sv|tull||toll, customs}}, {{cog|is|tollur||toll, customs}}. More at {{l|en|tell}}, {{l|en|tale}}.
Alternate etymology derives {{inh|en|ang|toll}} from {{der|en|la-med|tolōneum}}, {{m|la|tolōnium}}, alteration (due to the Germanic forms above) of {{der|en|la|telōneum}}, from {{der|en|grc|τελώνιον||toll-house}}, from {{m|grc|τέλος||tax}}.
====Noun====
{{en-noun}}
# A [[fee]] paid for some [[liberty]] or [[privilege]], particularly for the privilege of passing over a bridge or on a highway, or for that of vending goods in a fair, market, etc.
#* {{quote-journal|en|date=1957 October|author=M. D. Greville and G. O. Holt|title=Railway Development in Manchester—2|journal=Railway Magazine|page=726|text=Meanwhile, the '''tolls''' dispute had gone to the courts, and the E.L.R. was completely successful when, in 1856, the House of Lords awarded it the sum of £30,000 against the L.Y.R. for '''tolls''' overcharged.}}
# Loss or damage incurred through a disaster.
#: {{ux|en|The war has taken its '''toll''' on the people.}}
# A fee paid by the owner of materials or other goods for processing such goods, as under a [[tolling agreement]].
#: '''''toll''' ore refining''; '''''toll''' manufacturing''
# {{lb|en|business|by extension}} A fee for using any kind of material processing service.
#: {{ux|en|We can handle on a '''toll''' basis your needs for spray drying, repackaging, crushing and grinding, and dry blending.}}
# {{lb|en|US}} A [[tollbooth]].
#: {{ux|en|We will be replacing some manned '''tolls''' with high-speed device readers.}}
# {{lb|en|UK|legal|obsolete}} A [[liberty]] to buy and sell within the bounds of a [[manor]].
# {{lb|en|obsolete|regional|_|England}} A portion of [[grain]] taken by a [[miller]] as a compensation for grinding.
=====Derived terms=====
{{col|en|antitoll|toll-free|tollage|tolldish|tollgatherer|tollhouse|tollkeeper|tollman|tollmaster|tollperson|tolltaker|tollway|tollwoman
|Cameron Toll
|death toll|take a toll
|toll road
|toll bridge
|toll booth
|toller
|tollgate
|burn the coal, pay the toll|e-toll|take its toll|toll barrier|toll call|toll castle|toll line
```


## [2026-10-15T02:27:10.708Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'tarazu\\|taräzu\\|tara[.-]*\\(a\\|ā\\|ä\\)z' BRT.txt AHM.txt AVG.txt HID.txt ZAP.txt 2>/dev/null| head; grep -n -i 'tarāz\\|taraz\\|teräz\\|teraz' HRN.txt HUB.txt LKT.txt | head; grep -n -i 'tula\\b\\|tulä\\|tulā' IEC.txt | head"
}
```


### [2026-10-15T02:27:11.292Z] TOOL RESULT

```
LKT.txt:1290:[Aus  ar.  dar  'Haus',  sinä'a  'Betriebsam- keit, Handwerk,  Industrie']  'Fabrik',  be- sonders 'Waffenfabrik'  und  auch  schon ar.  'Schiffsbauhaus';  im  Türkischen  zu tershäne  korrumpiert,  als  wenn  es  von pers.  Jiänä  [s.  hier  Nr.  809]  käme.  Hier- aus it.  darsena,  siz.  tirzanä  'iniiei'es Hafenbecken',  arzanä,  arsenale,  terzana 'Zeughaus';  frz.  darse,  darsine  'kleiner Binnenhafen',  arsenal;  sp.  atarazana, atarazanal  'Schuppen',  arsenal;  pg. taracena,  tercena  'Schuppen',  arsenal; rum.  arsenal,  darsena.  Dtsch.  Arsenal, ndl.  arsenaal,  engl,  arsenal,  russ.  a?*- senal.  [Dozy  Oost  16/18.  DE  205/206. Eguilaz  304.  Gorjaiew  6.  Kluge  23. Devic  DEt  35/36.    ML  2474.
LKT.txt:4564:'Wage',  tk.  ebenso  terazi ;  hieraus  serb. teresije,  klruss.  terezy,  russ.  tereza ' Wase' ; rum.  tirizie,  terezie  'Wagscliale'.  [Löbel EITAP  94.    Mikl  SlEtWb  354  a.
LKT.txt:10019:atarazana  495
LKT.txt:10020:atarazanal  495
HUB.txt:1213:Zar. 66, Anm. 61 = arm. paterazm *Krieg, Kampf,
HUB.txt:4681:Zar. 66, Anm. 61 = arm. paterazm 'Krieg, Kampf, Schlacht'
HUB.txt:7977:und paterazni, phi. razm u patrazm Yatk. i. Zar. 66, zd.
HRN.txt:5468:aw. vergl. areza- 'Schlacht'; arm. LW. paterazm
349:akskis, os (?) “chip, splinter. Cf. ak-, aK-, skiio Lat. cf. assis, LLat. axis “board”, and popular Lat. asser beside ascla, astla, astula; W asg; Srb. (?) o$ce *window-pane' and o&cela, f. ‘chip’, but these may be cpds. with px. o-
763:astlā (?) ‘floorboard’. WP I, 84 Lat. astla, astula (LWs in W astell *board, shingle' (?); OE æstel-); Li. aslà “floor”
5938:&hastos, à, is, io “hand, arm, handle, grasp’. WP I, 541 Skt. hastab; Av. zasto; Ober, dasta-; Per. dast “hand”; daste, s. “handle, pestle’; Kurd. des, dez ‘hand’; Tokh. A kas "ams length, fath- om’; Lat. cf. praesto “by the hand" beside hasta ‘pike, pole’; It. asta “handle, shaft’; Ir. gas ‘stem, branch’; gasta invar. adj. “handy, skill- ed”; Li. Zástas ‘arm’; pa-Zaste “armpit'; prié- žastis, ies, f. ‘opportunity’. Extn. in LLat. has- tula ‘twig’
9323:Kuistlos, à ^whistle, whizz, whirr; shrill bird- cry, bird w. similar cry’. Cf. Kuisto, Kuistos, Kuisolis Gk. síillos, m. (*mockery'. Cf. sense of Fr. per- sifler: siffler) beside sile-pordein, inf. ‘mock’; Alb. cf. cyl&, f. (^whistle', fr. *Kuisulis); LLat. quistula ‘quail; OE hwistle, f. 'reed-pipe, whistle'; long-gde. in ON hvísl, n., hvísla, f. ‘whisper’; Sw. cf. hvissla, vissla, v. ‘whistle’ (Isophonic: Li. Svisteleti, Svysteleti “to flash”. The history of Lat. f in fibia & fistula is un- certain, but cf. Kuibh- (1))
9326:Cf. Kuistó and extns. Oss. áxsitt, s. ‘whistle’; ON hvísta, v. id.; be- side hvísl, hvísla, hvískr, s. *whisper'; E dial. whist ‘windpipe’; OCS svistü, R svist, m. ‘whistle, whizz’; LLat. cf. quistula ‘quail’. WP I, 469 & II, 518
10384:matolos, à (?) "not Per. matar ‘pot; Lat. matula *chamber-pot
10650:mentolos (mentul-, mentor-, mentur, men- thol-, etc.) ‘stir, stirrer, stick’. Cf. mento (men- tho) and mentos (mentho-) Lat. mentula (“ penis”, lit. stick"); Ir. meadar, pi. meadra, f. ‘churn’; Cz. matla, m. & f. *mess- maker” beside metel-ice ‘snowstorm’; R mja- teľ, f. ‘snowstorm’; Li. mefitalas 'beer-mash' beside mentüris, io, m. ‘beater, stirrer, stir- ring-stick' beside mentüre, mefite, f. id.
10689:mestos, à (variant of type madtós, mast-? Cf. mad- (1)) ‘food, fattening; fattened’. WP IT, 231 Gk. mestós ‘crammed’; MIr. mess ‘beech and oak mast’; Ir. meas, pl. -a m. ‘fruit, crop’; W mes, fpl. ‘acorns’; Br. méz, m. & coll. ‘acorn, acorns’; Cor. mes, f. as W; W cf. also mest, m. “portion of food’; Myc. cf. (queried) me(s)- tura(i) or me(s)tula(i) ‘farm-animals’. With variant vocalism MHG mast, usu. f. ‘fruit; rich soil; fodder, masť; masten, v. ‘grow
10703:metolos, à (metil-) ‘cast, throw, dash, throw- ing-instrument',. See next Lat. metula, metila & metella “basket of stones to throw down on attackers’; OCS metla ‘lash’; Slovak metla ‘lash; besom’ (and com. SI). (For Slovak metel ‘snowstorm? see ment(h)-)
11138:mont- (month-) “stir, disturbance, move, re- moval; movable(s)'. Cf. mentó, mentos, mnt- MHG cf. mende, sf. ‘joy’; ge-mende, adj. ‘gay’; menden, mennen ('rejoice' if for *monteijo); OS mendian, v. id.; OCS motü, m. 'distur- bance; filth’; Pol. met, m. ‘cloudy water’; Cz. cf. moutev, f. /(stirring-stick'; s-mutek, m. ‘mourning’; Li. mantà (property, movables’. Sense of Lat. mobiles res furniture); Latv. manta, f. id.; mante, f. *potter's spatula’
```


## [2026-10-15T02:27:16.353Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n '^tel\\|^tl' IEC.txt | head -30; grep -n -i 'Atlas\\|talanton\\|tula\\b' WLD_band3.txt | head; grep -n -i 'tel-\\|tela-' incoming/WLD/WLD_Bd1_pages.txt | head -5"
}
```


### [2026-10-15T02:27:16.702Z] TOOL RESULT

```
18298:tel- (1) (telo, ið) “stretch, extend, expand; expanse’. Cf. telm- (1), titos Per. (ambig.) tar, s. “thread”, but cf. ter- be- low); Arm. cf. toy, Let s. ‘thread, line; row, series'; W tel, pl. -au, m. 'straight line; stric- ture’; adj. ‘stretched, taut’; telu, inf. ‘stretch’; tellu, inf. (extend over’, fr. *telið); Cor. cf. an-tel, f. “inveiglement; v. (“stretch; set — trap; prepare to jump”, fr. *ono-?); Gk. cf. telamón, -6nos, s. “strap, band’ and W telm, pl. -au, f. (“snare, contraption’, fr. telmn-, q. v.); OE cf. belma, wm. ‘noose, snare’; ON bjálmi as OE; Oss. táülm, tälmä, s. “strip, stripe, line’
18299:tel- (2) ‘space, ground, place, base’. Cf. WP L 740 & II 611. Same as (1) (?) Gk. selís, gs: -ídos, f. ‘space, esp. between thwarts of boat'; sélma, n. “space; bench of oars; cockpit'; Lat. cf. (?) tel-lüs, gs: -lüris, f. (goddess of earth; earth’. A cpd., second element obscure, hardly to ieur-, q.v.); ON peli, m. ‘frozen ground"; OPr. talus, s. (floor, but see next); Ir. cf. talamh, gs: talhman & talamhna, pl. talaimh, mf. (^earth', fr. *telem-)
18300:tel- (3) ‘tree, timber, plank, board" Skt. taruh, m. ‘tree’; OHG dilo, wm., dilla, f. ‘board; deck’; MHG dil, dille, id.; OE pille, n. ‘floorboard’: EME thill, mod. ‘floor of mine’ beside bel, bell, n. ( board’, fr. *təli-?); cf. OE pilian, v. “lay — floor’; piling, s. floor- ing’: G Diele; ON pili, n. *wainscot, panelling’; pilja, f. ‘plank’ beside pelli, n. (pine, deal, fr. *toli-?); Li. cf. (z-gde) tile, f. (floorboard; bottom of boat, fr. *t]io); OPr. (ambig.) talus (*floor': Skt. taruh, m. if not to tel- (1), q.v.)
18302:tel- — telpó
18313:tel- (5) “art, music? (?). See next Skt. cf. talaváh, m. ‘musician’; W teli, m. "art: telor, s. ‘warbler’; tél, adj. ‘shapely, beautiful”; telyn, s. “harp
18314:tel- (tēlos, à, om, io) “shape, form, figure, body’. Cf. tel- (5) Hitt. cf. (?) -ciel (in taya-ciel “theft”); Gk. selía, telia, f. ‘tray; rim; table; trough; cover; bin’; Lat. cf. -tēla (in müs-tela *mouse-shape'; nī- tela *nest-building shape”, hence: ‘weasel’ and *dormouse); W til, pl. -ion, m. “particle, atom’; OCS tělo, gs: -ese, n. (and com. Sl.) “Image, idol, pillar, altar”; Cz. R. télo, n. “body”; Latv tēls, m. ‘statue, figure, skeleton’. (Iso- phones in Lat. pro-telum, “forward thrust, advantage’; pro-telo ‘readily’; pro-telare, inf. ‘defer; worry’)
18315:telgo, io ‘fling, dash, shatter’. Cf. tolĝ- and WP I, 741 Gk. cf. a-selgés, adj. ‘excessive’; Ir. teilgim, v. ‘fling; overthrow, destroy’; Li. télžiu, ti, v. ‘fling, beat, dash, teem’
18316:telk-, (variants: tolk-, tlk-, q. v.) (1) “flatten, compress, batten down’ Slovene tleči, inf. ‘flog’; Li. telkiù, ti, v. “mass, rally’; o-gde in Li. talkà, f. ‘rally’; Cz. tlak, m. ‘pressure’; (z-gde in) R tolkat, inf. ‘push, jolt
18317:telk- (2) (variant: tIk-) (2). Cf. (telquo); tol- quos, à. (Cons. uncertain) Skt. tarkayami, v. ‘suppose’; Latv. telka, f. ‘complexion’; (z-gde in) R tolk, m. ‘meaning’; tolkovàt, inf. ‘explain’
18318:telm- (1) (telmn-) ‘stretch’. Cf. tel- (1) Oss. tülm, tälmä, s. ‘strip, stripe, line’; Gk. cf. telamón, gs: -mónos, m. “strap, band'; (*telmn- in) W telm, pl. au f. ‘snare; gadget; OE pelma, ‘snare’; ON bjálmi, m. id.
18319:telm- (2) Arm. Dm, gs: tymo, o-st. ‘mud’; Gk. télma, n. ‘mud, swamp’; telmís, gs: -minos, f. ‘mud, filth’
18320:telpð (1) “move, stir Oss. tálfín, pp: tälft, v. ‘move about, fidget’;
18323:telpo (2) (tolp-, tlp-) “have room’. Cf. tolp-. WP I, 741. E-gde in Li. telpù, inf: tilpti, v. “find room’; Late telpa, f. ‘space, room’
18333:telpó — tempos, -es-
18623:tlātos (tltos, is) ‘suffered, borne; suffering”. WP I, 738. Celtic ambig. Gk. tlētós, (Doric: -à-), adj. ʻendurable, en- dured'; Lat. latus, adj. “borne, carried’; MIr. tláith, adj. ‘tender, feeble’; tláithe, f. “weak- ness, defect; W tlawd, adj. ‘poor’ (Celtic forms *tlàt- or *t[t-)
18624:tl- (1) (tlo, tolo, io) “lift, raise, bear, suffer”. WP I, 701 & 738-9. Cf. tul-, dng, tlt-, tlat- Oss. cf. tàlát, s. removal, confiscation’; Gin. s. layabout; Tokh. A GL. B tal-, v. “ift, carry’; Gk. tlémi, aor: etlén, v. “bear, support, suffer”; cf. ó-tlos, m. ‘care, toil; OLat. (ambig.) tulo, ére, v. (“ bear; carry’. See tul-); Lat. perf. (te)tuli I carried); MIr. cf. tlenim, v. (óremove', tr.); tallaim, v. “steal, bereave'; Go. bulan, wv. *bear, suffer, endure'; OE polian, id.; ON pola, MHG dolen, id.
18625:tl- (2) (tolo, ið) “make so, estimate”. Cf. tal- (1) Gk. cf. tálanton (a weight, but in sense of “scale, balance? cf. tl- (1)); OBr. tal-, v. “pay”; at-tal, -tail, v. ‘repay’; W talu, at-talu, v. as Br.; Cor. tylly, 3s: tal, v. ‘owe; pay; be worth’; Icel. cf. pel, n. (2) “nature, temper'; OCS cf. toli ‘so much"; toljo, toliti, v. ‘restrain, pacify’. (Gk. tólma "courage is o-gde, semantics of Srb. ják ‘strong’: Cz. jak “how?)
18626:tl- (3) (tlo, io; tolo, ið) ‘abate’ Olr. cf. tuilim, v. “sleep; OE pyllan, v. (calm, pacify’, fr. *tInjo) beside byld, f. ('patience": MHG ge-dolt, -dult, -dulde, f. id. In this sense indistinguishable from tl- (1)); OCS toljo, iti, v. ‘pacify’; R u-tolit, inf. ‘allay’; Li. tiliù, éti, v. “be silent; cf. tylüs, adj. ‘silent’; tylü, tilti, v. ‘be silent", fr. *tIno
18627:tl- (4) (2) OCS cf. tlëja, tlěti, v. ‘decay’; R tlét, inf.
18638:tlk- (1) “strike, force, crash’. Cf. tolk- (1) Gk. salásso, v. (cram, fr. *tIkjo); Ir. tulc, m. and tolc, m., tulca, pl. -anna, m. “blow, stab’; tolca also = ‘mass, surge); OCS tlükü, m. Cknock', and com. Sl.) beside (o-gde) tlaka, f, Cz. tlak, m. ‘pressure’; (u-basis in) Cz. tluk, m. ‘knock’; tluku, tlouci, v. “knock, beat’; OCS tlüko, tlěšti, v. “clash, crash’; Slovene tolči, inf. ‘beat; Ukr. s-touči, inf. ‘beat, pound’; s-toukty, inf. ‘shatter’
18641:tlo-, form of tel- (2), see Supt: tal- and tol-. Ambig. in Li. cf. tilis & WP I, 740
18642:tlp- ‘space’. Cf. telp-, tolp- Ir. toillim, v. “have space’; Li. tilpti, inf. id. beside (o-gde) talpà, f. ‘capacity’
18644:tltos, is, ios ‘extended, stretched; extent, tract, roadway, passage’. Cf. WP I, 738 and stltos. Skt. ambig. Skt. (ambig.) tirthám, n. (“passage, crossing”. Cf. tr-, tro, etc.); Gk. cf. talásios, adj. travelled out, unravelled'; Thrac, tíltia, f. ‘way, road’; EMAIDb. i glat&, mod. i gjatë, adj. ‘long’; Umb. cf. tlatie, gs. (name of a meadow > Latium) (but for Lat. latus, OLat. stlatos “broad” see stitos); Li. tiltas, m. ‘bridge’; Latv. tits, id. (For Olr. tláith ‘weak’; Br. troet, troed ‘lean’; W tlawd ‘poor’, see tlātos, but vocalism is ambig.)
2558:61. feleigare lit. (614° set, atlas ik. 048°. stelgit, ‘ately lit. 645%, (040%),
3484:pflfigen kann", vgl. o. lat. acnua, actus quadratics), arm. art „Acker‘‘ (Mittel-
8611:zu    eyeiv, eyeiv),   d-zXog   (s. tel-      „tragen“), o-tpeXog, o-ipov, o-flgiitog (s. u. g'Xer-
12100:  Idg. (f)ng%- vermutlich Ablaut von ^eneg'kh- (mit g i aus g"h bei unmittel-
27913:  Weitere Ankniipfung an itel- ,,wollen“ (Vaniiek 266 v. Grienberger,
28189:zu *itel- „drangen, pressen“ (so daB dies veliu = att. eTXXo> Persson zu *uel-                   >,
```


## [2026-10-15T02:27:18.994Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; awk 'BEGIN{RS=\"\\f\"} NR==747||NR==748{print \"----LEAF\",NR; print}' WLD_Bd1_pages.txt | head -80"
}
```


### [2026-10-15T02:27:19.367Z] TOOL RESULT

```
----LEAF 747
138                                                                 tel-



Dorr- oder Trockenvorrichtung“                       „troekne (trans.) an der Luft“
                                                            ;
                                                                alb. ter
(u. dgl.     ;
                     G. Meyer      BB. 8, 187,             Alb. Wb. 427);
                                                         lat. torreo   -ere, -ui, tostum                           ,



,. dorren,   braten, rosten, sengen“ ( tostus aus *torsitos        ai. tarsita-h   kaum                =                         ,

=   ai. trsta-h   Ciardi-Dupre BB. 26,204), forms alat. (s. o.), erweitert tor-
                        ;


ridas „ausgetrocknet, dfirr", torris ,, Brand, brennendes Scheit‘, torrens
„brennend, sengend, erbitzt; heftig, brausend, reiBend in der Stromung“,
Subst. „Wildbach“ (dies eig. ,.im Sommer austrocknend ‘? Persson Beitr.
730); air. tart „Durst“ (*trsto-t) ; got. gapalrsan st. Y. „verdorren“ (= gr.
Tf goo/uai)-, gapaiirsnan ds. = aisl. porna ds.; abd. dorren ds.; ahd. derren
„trocken machen, dorren            aisl. perra „trocknen“ (= ai. tarsayati lat. torreo );                                  ,


got. putirsjan  2  „dfirsten“, aisl. pyrstr (got. *paursips) „durstig“, wovon' got.
paurstei f., aisl. porsti m., a,gs.purst, ahd. durst „Durst“ got, paursus is statt z
                            =
                                                                                                       ;


 nacb pnirsan        ai. trsit-li), aisl .pair, ags pyrrc, ahd. durri ,,dfirr“; ahd.
                                                                             .



durra schwed. tarre „Gestell zum Trocknen, Darre '; wohl auch aisl. porskr,
        ,
                                                                                           1




 mnd. dorsch .,Dorsch“ („*der zu trocknende"; s. Uhlenbeck KZ. 40, 560
 m. Lit. russ. treskd ,,Stoekfisch“ ist ursprgl. ,, Stock, Stange ‘)-
             ;
                                                                                 Hierher
auch        lat.      terra     ,.Erde'"       (:   extorris        ,,verbannt“      = tellus                  :   medihdliiim),     osk.
teer\um\,            teriim „territorium“,                terns „terrae“ aus           ital.               *terso-,        *tcrsd (siehe
zum Lautl. bes. Buck Yok. 176, Gramm. 48 f., v. Planta I 486); air. tlr n.
es- St. (Thurneysen KZ. 28. 147, Stokes ibd. 292) „Gebiet“, corn. bret. acymr.
tlr    .,tellus“,           air. *tlr,    ttrim          ,.trocken“;       da kelt.        tlr-            nicht          nach Zimmer
KZ. 30,210 aus *ters(o-) herleitbar ist, erwog man als Gdf. *teros-, *teres-
und lieB (Vendryes Msl. 13, 385) auch lat. ferres-tris terrenns ein nach terra                 ,


umgebildetes Heres-tris -nos sein was zur wenig ansprechenden Folgerung
                                           ,
                                                                ;


zvvang, dab die „Wz.“ tors- aus dem c(s)- St. *fe> [e]s- entwickelt sei oder           -




gegenfiber             dem St. ter-es- eine bloB verbale -s-Erweiterung enthalte (siehe
Vf. LEWb. u. terra).      Es darf aber nicht (trotz Thurneysen Hdb. 37) ver-
mutet werden. daB das Adj. ir. tlrlim) aus *tcrsro- (iiber *tesro-) entstand (er-
gabe ir. *terr[) und daB der c-s-St. tlr „terra entweder erst im Kelt, vom       ‘




Adj. abgeleitet ist oder daB — falls der formale Yergleich mit lat. terresfris                                                           ,
```


## [2026-10-15T02:27:22.794Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; awk 'BEGIN{RS=\"\\f\"} NR>=747&&NR<=750{print \"----LEAF\",NR; print}' WLD_Bd1_pages.txt | grep -n -i 'tela\\|tula\\|tolero\\|ertragen\\|tAac\\|Atlas\\|tel-' | head -30"
}
```


### [2026-10-15T02:27:23.354Z] TOOL RESULT

```
2:138                                                                 tel-
97: 1. tel-   „aufheben,                z.   T. wiigend,               z.   T. sich aufladend;                            tragen;   ertragen,
99:      Ai. tut a ,,Waage, Waagbalken“, tulaynti ,,hebt auf, wagY (mit Ablaut-
108:                                                                                                       ertragen, dulden“. Ptc.
116:                                                                            tel-                                              739
118:-aiva     ,,ertragend, duldend, leidend“,                                        zdXavzov (ursprgl. zu zaXag,           n.   zalav
126:„ertragend, duldend", zaXaog ds., in Zs. zaXa--, z. B. zaXa-jiev&rjg „Leid er-
137:korb, Kasekorb usw.", *zaXdzyg „*wer miihevolle MuBarbeit zu ertragen
181:Trabe"         (eig.         „die FiiBe hebend"), tolero „trage, ertrage, unterhalte", full,
204:  Got. pulan, -aklu „ertragen, dulden", aisl. pola, ags. pollan ahd. dolen,                                    ,
211:740                                                              tel-
215:  Lett. iz-iilt ,,ertragen, ausdauern                 (Endzelin KZ. 42, 378, Miihlenbach-End-
227:2. tel-                flacher Boden, Brett"; verbales ,,flach ausbreiten" nur im
230:           Balt, und zweifelhaften Alters, we all alb auch die Auffassung von tel-
285:von *tel- und *stcl-), tiles .,Bodenbretter im Kahn" (Lw. aus nhd. Diclel ):
300:                                    (aber in Yerquickung mit tel- „tragen“),
304:telliis, Persson Beitr. 40, L9Sff. (Gleichsetzung mit stel- „ausbreiten“j, 310
314: 3. tel- „still seiir‘.
336:Die Gruppe ist vielleicht eine s-lose Yariante zu ahd. si ill i „still“, idg. stel-
339:354. 371 und aaO. an got pitlan, ahd. (lolcn „dulden“, T?Sjvai „ertragen
```


## [2026-10-15T02:27:26.587Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; awk 'BEGIN{RS=\"\\f\"} NR>=747&&NR<=749{print}' WLD_Bd1_pages.txt | sed -n 95,125p; awk 'BEGIN{RS=\"\\f\"} NR>=747&&NR<=749{print}' WLD_Bd1_pages.txt | grep -n -i 'av\\.\\|npers\\|iran\\|ap\\.' | head"
}
```


### [2026-10-15T02:27:26.980Z] TOOL RESULT

```
 1. tel-   „aufheben,                z.   T. wiigend,               z.   T. sich aufladend;                            tragen;   ertragen,
        dulden‘\
      Ai. tut a ,,Waage, Waagbalken“, tulaynti ,,hebt auf, wagY (mit Ablaut-
 neuerung                    ds.), tnlima-li „wagbar“ (fiber tuna-h .,Kocher“
                       dazu tolnyati
 s. u. tu& u)-   ,,R6hre‘); arm. tohim .,lasse, dulde, ertrage“ (s. Pedersen
 KZ. 39,354, Scheftelowitz BB. 29,22);
    gr. ra Idooai und xlrjvai (dor. exldv), Ptc. rlag, xlaaa Fut. xItfoo/uai, dor.                         ,


 t Idaoyai.            Pf. rh /.(lit tv, t It lath, xex lyvla, xexltjorog                          ,
                                                                                                       ertragen, dulden“. Ptc.
                                                               (= lat. lotus,
 xlyxog. dor. x lards „duldend, standhaft; erduldbar, ertriiglich“
 cymr. tlawd ,.arm“, idg.         Fick II 4 130, Ernault Rc. 27, 70 ff., Hirt
                                                *tj:>-tds
 IF. 21, 167), xalug, -avxog und (nach yelag, Solmsen IF. 31, 499f.) -avog,

                                                                            tel-                                              739

-aiva     ,,ertragend, duldend, leidend“,                                        zdXavzov (ursprgl. zu zaXag,           n.   zalav
gehoriger PI. zalavza                        eig. „die beiden Waagschalen",
                                                      Solmsen aaO. 497ff.,
Kretschmer Gl. 3, 266 ff.) „Waage; ein bestimmtes Gewicht", azaXavzog „von
gleichem Gewicht, gleiclrwertig, gleich", noXvzXag „wer viel ausgestanden
hat (Horn.); sehr geduldig (Soph.)“, ’AzXdg, - avzog zXryxcov, dor. zXa/xcov                      ,


„ertragend, duldend", zaXaog ds., in Zs. zaXa--, z. B. zaXa-jiev&rjg „Leid er-
tragend", zala-cpQwv „ausharrenden Sinnes, beharrlich", woneben zaXaai-
157:auferlegen"),                ivzeXXetv,         -eoftai             „auftragen,         heiBen,       befehlen",       imzeXXav.
```


## [2026-10-15T02:27:28.803Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/ref_page.py PLA:194 --image 2>&1 | head -80"
}
```


### [2026-10-15T02:27:29.366Z] TOOL RESULT

```
(no exact page map; using offset 0 -> pdf page 194; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/PLA/0194.png
REF: PLA:194  PDF: data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf page 194  OCR-lang: deu+ara

Saläfim                                                                                  179                                                         Sambar


Pe         - Saläfim:                       Pl.           Vgl Salßam                    q. v.

 rF-               Salägim:                 Pl.           v. pie Salem                  a.    v.


 =             $Salfam:                "Rübe"              pers.        1, mand. Salgam (p. pI4 ) ®,aram. »,bw°,                                       syr.
     j
           nt.              4



ge-            Salgam:                 "Rübe"              = Salfam            q.       v.         °.

so;
GC         RR           -       sumarazinag: .                   m "anoethum             foeniculum                  Ammi    majus "     6 .




el                 -    $amäfidin:                        Pl.    v.aeh              $am°dän               q.    v.
           u            w        -                                         “        v              -




ae         - Sumahtar:                          "unglücklich"                            pers.           za.             Süm-ahtar     ? m          Ies axtar
                                            8
          "Sternbild"                            .


usa - SimSäd:                              "Buchsbaum"                  — pers.,Li; Semsäd MP.)u Zim$är "box-
          tree"             9        syr.            un     10,


Ge       - Samus:                 "Elink"                       pers.               ©amü$               "launisch,          muckenhaft,          eigensinnig,
          ungestüm",                                                           ”


aan            -       Sam°dän:                 "Leuchter"               pers.           11             eigentlich          nur   eine     arabisch-
          persische                    Zusammensetzung.


„Lö - Sanär: "häßlich"— pers. (Addai Scher).

„u-            Sambar:                 "Reifen"                 ägypt., Ar. pers.                               „e&anbar             T         mp. Dep Sambar.



1.       wahrmund                s.        v.,        BQ.       s.   v.,   Addai              Scher            s.    v.
2.       Macuch             s.       v.
3.       Löw       s.       v.
4.       Brockelmann                       s.        v.
5.       Wahrmund                s.        v.
6.       Kamäl
            s. v.
7. Muhit                s.       v.
8.       Nyberg             Bd.        IIs.v.
9.       Mackenzie                   Ss.    Vv.
10.       Brockelmann                       s.        v.
11.       Dozy Bd.                   I S. 788.-                  BQ.     s. v.,              Muhit         s.       v.
```


## [2026-10-15T02:27:31.668Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/ref_page.py PLA:194 --pdf-page 209 --image 2>&1 | head -90"
}
```


### [2026-10-15T02:27:32.073Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/PLA/0194.png
REF: PLA:194  PDF: data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf page 194  OCR-lang: deu+ara

Saläfim                                                                                  179                                                         Sambar


Pe         - Saläfim:                       Pl.           Vgl Salßam                    q. v.

 rF-               Salägim:                 Pl.           v. pie Salem                  a.    v.


 =             $Salfam:                "Rübe"              pers.        1, mand. Salgam (p. pI4 ) ®,aram. »,bw°,                                       syr.
     j
           nt.              4



ge-            Salgam:                 "Rübe"              = Salfam            q.       v.         °.

so;
GC         RR           -       sumarazinag: .                   m "anoethum             foeniculum                  Ammi    majus "     6 .




el                 -    $amäfidin:                        Pl.    v.aeh              $am°dän               q.    v.
           u            w        -                                         “        v              -




ae         - Sumahtar:                          "unglücklich"                            pers.           za.             Süm-ahtar     ? m          Ies axtar
                                            8
          "Sternbild"                            .


usa - SimSäd:                              "Buchsbaum"                  — pers.,Li; Semsäd MP.)u Zim$är "box-
          tree"             9        syr.            un     10,


Ge       - Samus:                 "Elink"                       pers.               ©amü$               "launisch,          muckenhaft,          eigensinnig,
          ungestüm",                                                           ”


aan            -       Sam°dän:                 "Leuchter"               pers.           11             eigentlich          nur   eine     arabisch-
          persische                    Zusammensetzung.


„Lö - Sanär: "häßlich"— pers. (Addai Scher).

„u-            Sambar:                 "Reifen"                 ägypt., Ar. pers.                               „e&anbar             T         mp. Dep Sambar.



1.       wahrmund                s.        v.,        BQ.       s.   v.,   Addai              Scher            s.    v.
2.       Macuch             s.       v.
3.       Löw       s.       v.
4.       Brockelmann                       s.        v.
5.       Wahrmund                s.        v.
6.       Kamäl
            s. v.
7. Muhit                s.       v.
8.       Nyberg             Bd.        IIs.v.
9.       Mackenzie                   Ss.    Vv.
10.       Brockelmann                       s.        v.
11.       Dozy Bd.                   I S. 788.-                  BQ.     s. v.,              Muhit         s.       v.
```


## [2026-10-15T02:27:34.095Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA; awk 'BEGIN{RS=\"\\f\"} NR==209{print}' PLA_pages.txt | grep -v '^\\s*$' | head -70"
}
```


### [2026-10-15T02:27:34.412Z] TOOL RESULT

```
tabaristän                                                                     194                                                       tirazdärän
ol.              -       tabaristän? : Landschaft                             in    Nordpersien           ı    mand.           tabaristan         ®,
Sh-            tabari:               "aus     Tiberias             od.    Tabaristan"             °.,
on        -    tabas:            eine        Stadt       in    Khorasan -
Ol             - tabasän:                   Dual    v.     tabas,         zwei          Städte     in    Khorasan             4,
     a                     7.                                                                    Fo              r   5
a         - taba$i:                  "eine        Heilpflanze" <                    Pers. a             tabafi           ”.
o-         tabag:     "Holzplatte",                           nach       Dehhodä          eine     arabisierte                Form       v.   pers.2,0
              =.  6
          tabük     .
apmb- tabanga:                          "Pistole"             = tabänfa q. v.
ENG            aßgan:           "in der Pfanne                 braten"             s.    tägin 7,
(rel - oo
       taräbis:                             Pl.    v. or» 5 tarbüs                  q. v.
Gelb - taräbiS:                             Pl. v. ab tarbüf                       q. v.
Jelb - tar&bil:                             Pl.    v..Jı) garbäl                   q. v.
ab             - taräbina:                   Pl. v.ubb tarhän q. v. 8,
lb.            tiraz:            "Stickerei,               Rand,         Saum!             pers.        ;|x taräz             m.              Dr taraz.
               .t                    =                                                                                               “         2 ee.
Olls;Lb - tiräzdäran:                                 "Futteral               der Waage" pers.                       olbyals              tarazudäran
              mp.           gi        r tarazük            "Balance,               Gleichgewicht"                    air.          *taraä=      skr.
          tula           + aw.        az "zugeben"                 tk.             terazi,       serb.,       kl.        russ,       terezy.
1.       LD.        s.    v.
2.       Macuch           Ss.    v.
3.       Wahrmund               s.    v.,     LD.     S.      v.
4.       al-Mu°arrab                  Ss.    V.
5.       LD.        s.    v.
6.       ebda.
7. Wahrmund
      s. v., Muhit s. v.
8.       LD.        s.    v.
9.       Wahrmund               s.    v..     Addai        Scher         s.    v.
```


## [2026-10-15T02:27:39.479Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; ls data/verification/sources/refs/ocr/PLA/ | head -30; grep -n 'cache\\|vision\\|pdf-page\\|pdf_page' tools/ref_page.py | head -30"
}
```


### [2026-10-15T02:27:39.985Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--  346k sfmqrb 14 Oct 22:19  0018.png
.rw-r--r--  4.3k sfmqrb 14 Oct 22:19  0018.txt
.rw-r--r--  326k sfmqrb 14 Oct 22:19  0022.png
.rw-r--r--  3.8k sfmqrb 14 Oct 22:19  0022.txt
.rw-r--r--  361k sfmqrb 14 Oct 22:19  0027.png
.rw-r--r--  4.5k sfmqrb 14 Oct 22:19  0027.txt
.rw-r--r--  296k sfmqrb 14 Oct 22:19  0194.png
.rw-r--r--  2.9k sfmqrb 14 Oct 22:19  0194.txt
6:    python3 tools/ref_page.py BQT:918 --pdf-page 375   # override the offset mapping
10:matching PDF page to PNG (for reading with a vision model), OCRs it with tesseract in
11:the reference's language(s), caches both under
18:save that transcription as <printed page>.vision.txt next to the .txt; from then on this
50:    if "--pdf-page" in argv:
51:        pdf_page = int(argv[argv.index("--pdf-page") + 1])
54:        pdf_page = None
57:            pdf_page = json.load(open(pm)).get("map", {}).get(str(page))
58:        if pdf_page is None:
59:            pdf_page = page + int(scan.get("pdf_offset", 0))
60:            print(f"(no exact page map; using offset {scan.get('pdf_offset', 0)} -> pdf page {pdf_page}; check the printed number and re-run with --pdf-page if off)")
72:        subprocess.run(["pdftoppm", "-f", str(pdf_page), "-l", str(pdf_page), "-r", "300", "-png", "-singlefile", pdf, base], check=True)
75:        r = subprocess.run(["pdftotext", "-layout", "-f", str(pdf_page), "-l", str(pdf_page), pdf, "-"], capture_output=True, text=True)
81:        header = f"REF: {abbr}{vol}:{page}  PDF: {os.path.relpath(pdf, ROOT)} page {pdf_page}  OCR-lang: {lang}\n\n"
83:    vision = base + ".vision.txt"   # a transcription made by reading the PNG; preferred over OCR
86:    if os.path.exists(vision):
88:        print(open(vision, encoding="utf-8").read())
```


## [2026-10-15T02:27:43.121Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; git status --short data/verification/sources/refs/ocr/PLA/ ; git log --oneline -1 -- data/verification/sources/refs/ocr/PLA/0194.txt"
}
```


## [2026-10-15T02:27:43.627Z] TOOL CALL #29: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/tools/ref_page.py",
 "offset": 60,
 "limit": 30
}
```


### [2026-10-15T02:27:43.720Z] TOOL RESULT

```
(Bash completed with no output)
```


### [2026-10-15T02:27:43.755Z] TOOL RESULT

```
60	            print(f"(no exact page map; using offset {scan.get('pdf_offset', 0)} -> pdf page {pdf_page}; check the printed number and re-run with --pdf-page if off)")
61	    else:
62	        print(f"no scan of {abbr} covers printed page {page} (see 'scans' in refs_online.json)"); return 1
63	    pdf = scan["file"] if os.path.isabs(scan["file"]) else os.path.join(REFS, scan["file"])
64	    if not os.path.exists(pdf):
65	        print("PDF not found:", pdf); return 1
66	    lang = scan.get("lang", "fas")
67	    out_dir = os.path.join(OCR, abbr + vol)
68	    os.makedirs(out_dir, exist_ok=True)
69	    base = os.path.join(out_dir, f"{page:04d}")
70	    png, txt = base + ".png", base + ".txt"
71	    if not os.path.exists(png):
72	        subprocess.run(["pdftoppm", "-f", str(pdf_page), "-l", str(pdf_page), "-r", "300", "-png", "-singlefile", pdf, base], check=True)
73	    if not os.path.exists(txt):
74	        # try the PDF's own text layer first; fall back to tesseract
75	        r = subprocess.run(["pdftotext", "-layout", "-f", str(pdf_page), "-l", str(pdf_page), pdf, "-"], capture_output=True, text=True)
76	        text = r.stdout if len(r.stdout.strip()) > 80 else ""
77	        if not text:
78	            env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)
79	            r = subprocess.run(["tesseract", png, "-", "-l", lang, "--psm", "6"], capture_output=True, text=True, env=env)
80	            text = r.stdout
81	        header = f"REF: {abbr}{vol}:{page}  PDF: {os.path.relpath(pdf, ROOT)} page {pdf_page}  OCR-lang: {lang}\n\n"
82	        open(txt, "w", encoding="utf-8").write(header + text)
83	    vision = base + ".vision.txt"   # a transcription made by reading the PNG; preferred over OCR
84	    if "--image" in argv:
85	        print("IMAGE:", png)
86	    if os.path.exists(vision):
87	        print("[transcription from the page image; OCR text in", os.path.relpath(txt, ROOT) + "]")
88	        print(open(vision, encoding="utf-8").read())
89	    else:
```


## [2026-10-15T02:27:46.286Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; rm data/verification/sources/refs/ocr/PLA/0194.png data/verification/sources/refs/ocr/PLA/0194.txt; python3 tools/ref_page.py PLA:194 --pdf-page 209 --image 2>&1 | head -40"
}
```


### [2026-10-15T02:27:48.190Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/PLA/0194.png
REF: PLA:194  PDF: data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf page 209  OCR-lang: deu+ara

tabaristän                                                                     194                                                       tirazdärän


ol.              -       tabaristän? : Landschaft                             in    Nordpersien           ı    mand.           tabaristan         ®,


Sh-            tabari:               "aus     Tiberias             od.    Tabaristan"             °.,


on        -    tabas:            eine        Stadt       in    Khorasan -


Ol             - tabasän:                   Dual    v.     tabas,         zwei          Städte     in    Khorasan             4,

     a                     7.                                                                    Fo              r   5
a         - taba$i:                  "eine        Heilpflanze" <                    Pers. a             tabafi           ”.


o-         tabag:     "Holzplatte",                           nach       Dehhodä          eine     arabisierte                Form       v.   pers.2,0
              =.  6
          tabük     .


apmb- tabanga:                          "Pistole"             = tabänfa q. v.

ENG            aßgan:           "in der Pfanne                 braten"             s.    tägin 7,

(rel - oo
       taräbis:                             Pl.    v. or» 5 tarbüs                  q. v.

Gelb - taräbiS:                             Pl. v. ab tarbüf                       q. v.

Jelb - tar&bil:                             Pl.    v..Jı) garbäl                   q. v.

ab             - taräbina:                   Pl. v.ubb tarhän q. v. 8,

lb.            tiraz:            "Stickerei,               Rand,         Saum!             pers.        ;|x taräz             m.              Dr taraz.
```


## [2026-10-15T02:27:50.534Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /ترازو/{print \"LEAF\",NR-1}' BQT_v1_pages.txt | head; "
}
```


### [2026-10-15T02:27:50.937Z] TOOL RESULT

```
LEAF 342
LEAF 345
LEAF 359
LEAF 570
LEAF 581
LEAF 643
LEAF 661
LEAF 683
LEAF 706
LEAF 770
```


## [2026-10-15T02:27:52.956Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==707||NR==708{print \"=====LEAF\",NR-1; print}' BQT_v1_pages.txt | grep -v '^\\s*$' | head -150"
}
```


### [2026-10-15T02:27:53.495Z] TOOL RESULT

```
=====LEAF 706
ی
تر اژوی دد - کنابه از آقاب
تراش - بقتح اول بروزن نواش " طمع
و نوقع وتراشده شده را گویند؟ -
تر ارو!۱ ه معروف است ؛ ون آلتي
باشد که‌چیز هارا
ندان وزن
برج حیز آن‌هم گراشه" هت تج ایل ورابع : یمی
هت که از ترازو آخر تراش اس تکه تراشیده شده و[ نجه‌ازتراش
۱ جبلة دوازده برح | برآمده باشد. وهلال واری ازخریزه وهندوانعزا
. فلکی است۳ ویر | نیز کوشده *
و عدالت رانیز گویند قر ۷2 بفت‌اول‌بروزن هلاه بسنی
ساب و ی عراز ور | چا وشکاف باشد- وآوازیراگوبندکه ازشکتن
با شکافته شدن چیزی بگوش رسد - و صدای
رعد را نز گفته اند ؛ وطراق ععرب‌آنت ۰
۰ ۳۹ است ۰
۳ ترازو بانشانه نجوه‌ی
ترازو چشمه‌داشتن ۰ کنابه از
زبادتی وسنگینی بك یل نرازوست ازیلهُ دیگر.
تر ارزو شدن « کنابه از برابرشدن
دو عنیم باشد با هم درشجاعت وزور .
ترادوی پو لاد سنحان - کنبه
از نیزه وسنان مبارزان است .
تر ا نه۲ بر وزن بهانه . جوان‌خوش
صورت وشاهدنر ونازه وصاحب جمال را گویند-
و باسطلاح اهل نقمه صنیفی است که آن سد
کوشه داشته «اشد هر کدام سارزی : ۹ نی
ود: گری كٍِ_۳ ویکی دیگر تلا وتارلا - ودرلفت
نقش‌وصوت ودوییتی وسرود ونفمه‌را خوانند۵ -
۱ - پهلوی 12۳220 , ابرانی باستان 12۲2201 ۵ - 2270 - ۵۲2 ۰ : 2۳2) ۵
از سانسکریت 24آلا) , ۷۷2) و22 ۰ از۰22 سانسکریت: 4 (راهنمابی کردن » راندن» پیش-
بردن.) » «نببکک ۰۲۲۳ . رگ : مزنا . ۴ _- خوارژمی : ترلزك سح موی : حیزان .
برح‌هفتم از بروح دوازده گاند « گاه شماری ص ۰۷۰۳ . ۴ اوستا تافقنا * ( نراشدن
بربدن) «بارنولمه 486 . رك : نراشیدن . کب اوه رای :هن (قتتت):
سر گنلک 3-2 ۱ - اسم صوت است . اصدی‌آرد: ترااء, طراق
بود. خسروی گوید :
«لفت فرسی ۲۹۵ .
۷ - از رمثة اوستایی ۸۷۲1108] بمعنی خرد» نر و تازه (رك : تر» توره * توله) «فاب
۱ ص ۷ سسنا۱ صس ۱۷۱ ؟. ۸ دوهی (حوان خوشروی» دو ستی و صشف)؛
هر نسفته دری دری می‌سفت هرترانه ترانه‌ای میگفت فرخی سیستانی.
۵ تراشیدن - بفتح اول و ششم » ار : ترانی - بدن (مصدری ) . پهلوی 2511102)
«سشدهش ۱۷۳ ,(. بر گت ۶ , مفدی 251 ( بر ددن ( «گونیو ۳۵ ۰ ۰ گورانی 2-10(
+ کردی ۰۰۱۹۷ گیلکی 02-1۵250128 , طبری 8-25101۷28 « واژه نامه ۱۹۳ ؛ ستردن
۳ ۳
موی‌وجز آن- رنده کردن حك کردن - خراطی کردن .
( زر هان فاطع ۷۵)
=====LEAF 707
یس
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
۹ «حور» صحیح است. رك.فاری.
۴ ۰
. «کل لاب 6۲6۱ «لك ]: ۰۳۰۹ .
```


## [2026-10-15T02:27:57.415Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==706{print \"=====LEAF\",NR-1; print}' BQT_v1_pages.txt | grep -v '^\\s*$' | head -120"
}
```


### [2026-10-15T02:27:57.793Z] TOOL RESULT

```
=====LEAF 705
پاخته بائد پس کیرد - و کنابه از مردم ملوث
ومردار و فاسق حم هست۷ .
فا بفتح اول بر وزن سرا ؛ دبوار
ودیوارفلعه وکاروان سرا - وسدی و دیواربرا لیز
کفته‌اند که دریش جزی یکفند؟ و دیواری
که باکاهگل و کلابه استوار کرده باشند - وبنم
اول تو کیبی باشد از لفظ « تو» و « را > که در
معحاورات و کتابت واو را می اندازند - و بمعنی
خود را هم هت .
تراب بفتح اول بروزن شراب» ترشح
وراوبدن و کم کم چکیدن آب و شراب وروغن
وامثالآن باشد از کوزه و سبو و معك و مانئد
آن؟ - و بمحنی حیله و زبان آوری هم بنظر
آمده است.و بضم اول بزبان عربی‌خاكشرا گویند.
ترا یل بروزن و ممنی تراود است که
تراز
میکند ومی‌ترآوده چچه در فارسی‌با بواو وبرعکس
تبدیل مي‌بابند؟ .
تر الیدن « بر وزن و حعنی تراوبدن
وترشح کردن باشد مطلفا اعما زب وشراب‌ودوغن
وامثالآن از ظرونه .
اشتهار دارد. و ترندنکش نیز گوند , و بعربی
جرجیر خوانند .
قر اج - منم اول بر وزن وعمنی دراج
است» وآن پرنده‌ای باشد صحرایب یکهآنرا شکار
8[ وخورند؟ ۰
قراار ‏ بر وزن نماز » رشتة ریسمان
خام را کوبند - و نام درخت صنویر هم هست
و نام شهری است در تر کستان که منسوب است
۴ - صف دشمن ترا ناستد بیش
بخل همه چنان تراید ازآن روی
۹ رك : دراج .
حدودالمالم . فهرست؟.
بقبه از صفْحٌ 1۷۸
ور همه آهنین ترا باشد. شهید بلخی.
«لت فرس ۱4*.
۵ رك : ثراو ندن:
کآب‌چنان ازسفال نوبترابد(ثرابد. دهخدا).
خروانی. «لفت فری۲۲*.
پونانی 166۵0 .استی 48118 (یسر بجه) . فارسی : ثر ء تازه . پپلوی ۰12۲۲ *صسیشال ۱8:»»
ازهمین ربثه است ترانهةٌ فارسی ( جوان خوش روی و دویرتی و سرود ) و تولة نارسی (بمسك)
وتوره (شغال) دیتتا اص ۱۷۱ ب ٩۷۲‏ , گوراای ۲ ( خبی » 9 گورالی ۷۵ ۰ , فر یز ندی
وبرنی ونطنزری 4۲ « دك . ٩ص‏ ۳ ,: سمنانی و سنگری و لاسکردی و شهمیرزادی ۹:۹9
سرخة #۲) «ثك. ۲س ۰۱۹۳ دزفولی هم 8۲ (خیس ؛ مرطوب). ر که: ترانه. نوره , توله.
```


## [2026-10-15T02:28:01.296Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/ref_page.py BQT:480 --image 2>&1 | head -8; ls data/verification/sources/refs/ocr/BQT/ | grep 04[78] "
}
```


### [2026-10-15T02:28:01.857Z] TOOL RESULT

```
no scan of BQT covers printed page 480 (see 'scans' in refs_online.json)
(eval):1: no matches found: 04[78]
```


## [2026-10-15T02:28:05.976Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; mkdir -p dl499; curl -sL -o dl499/bqt480.jpg 'https://archive.org/download/borhan-ghate-v1/page/n706_w1200.jpg'; file dl499/bqt480.jpg; ls -la dl499"
}
```


### [2026-10-15T02:28:13.663Z] TOOL RESULT

```
dl499/bqt480.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 1240x1754, components 1
Permissions Size User   Date Modified Name
.rw-r--r--  205k sfmqrb 14 Oct 22:28  bqt480.jpg
```


## [2026-10-15T02:28:15.652Z] TOOL CALL #36: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/dl499/bqt480.jpg"
}
```


### [2026-10-15T02:28:15.683Z] TOOL RESULT

```

```


## [2026-10-15T02:28:24.558Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; curl -sL -o dl499/bqt479.jpg 'https://archive.org/download/borhan-ghate-v1/page/n705_w1200.jpg'; file dl499/bqt479.jpg"
}
```


### [2026-10-15T02:28:26.211Z] TOOL RESULT

```
dl499/bqt479.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 1240x1754, components 1
```


## [2026-10-15T02:28:28.361Z] TOOL CALL #38: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/dl499/bqt479.jpg"
}
```


### [2026-10-15T02:28:28.381Z] TOOL RESULT

```

```


## [2026-10-15T02:28:37.532Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /tmp; for w in toll atlas talent tolerate relate translate; do echo \"=== $w\"; curl -sL \"https://www.etymonline.com/word/$w\" | python3 -c \"\nimport sys,re,html;t=sys.stdin.read();m=re.findall(r'<section[^>]*>(.*?)</section>',t,re.S)\ns=' '.join(m) if m else t\ns=re.sub(r'<[^>]+>',' ',s);s=html.unescape(re.sub(r'\\s+',' ',s));i=s.find('(n.') if 'toll' in sys.argv else 0\nprint(s[:1200])\" ; done"
}
```


### [2026-10-15T02:28:38.327Z] TOOL RESULT

```
=== toll
 Just a moment... *{box-sizing:border-box;margin:0;padding:0}html{line-height:1.15;-webkit-text-size-adjust:100%;color:#313131;font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji"}body{display:flex;flex-direction:column;height:100vh;min-height:100vh}.main-content{margin:8rem auto;padding-left:1.5rem;max-width:60rem}@media (width Enable JavaScript and cookies to continue (function(){window._cf_chl_opt = {cFPWv: 'g',cH: '3sFwHepf4QNndqYu_0VOAFfVHxDrd68D5Wi51MLr8_Q-1792031318-1.2.1.1-t_2FbhShAPEGM3AZB6vkfEQ6fcmIhWvCOC.ejV5Bruk2nMVdL2vVeNov_BXm5dpR',cITimeS: '1792031318',cN: '74MLsfsP9ml3wx9YhU8gkv',cRay: 'a4ab6439cf2755b7',cTplC:0,cTplO:0,cTplV:5,cType: 'managed',cUPMDTk:"/word/toll?__cf_chl_tk=GE_kh62KhKqoTDNdYso6a4gcgnS0JQO8uRQlwe0PrsA-1792031318-1.0.1.1-adUW5twS25X7QGudwq5cfMOtEAHitlSRUBaig0N7SGs",cvId: '3',cZone: 'www.etymonline.com',fa:"/word/toll?__cf_chl_f_tk=GE_kh62KhKqoTDNdYso6a4gcgnS0JQO8uRQlwe0PrsA-1792031318-1.0.1.1-adUW5twS25X7QGudwq5cfMOtEAHitlSRUBaig0N7SGs",md: 'p4QoEUSzSBsB0FLvg9GnCgbP3aad0DFx8y_P2aWV7CA-1792031318-1.2.1.1-2Soepwov
=== atlas
 Just a moment... *{box-sizing:border-box;margin:0;padding:0}html{line-height:1.15;-webkit-text-size-adjust:100%;color:#313131;font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji"}body{display:flex;flex-direction:column;height:100vh;min-height:100vh}.main-content{margin:8rem auto;padding-left:1.5rem;max-width:60rem}@media (width Enable JavaScript and cookies to continue (function(){window._cf_chl_opt = {cFPWv: 'g',cH: 'uP7K0F2.KYUhtYxqyGh6ZWj6hnurNH1_RbyD5ilmwD8-1792031318-1.2.1.1-h4eyEmE6dg.zO9322kTviX9x0abTtTYKQ5M4gkIepRJHSjzh3VYMBNjYQfAIaNzL',cITimeS: '1792031318',cN: '21MGQlAxEXSBZFBFVuWxLG',cRay: 'a4ab643a19c9eff9',cTplC:0,cTplO:0,cTplV:5,cType: 'managed',cUPMDTk:"/word/atlas?__cf_chl_tk=UxlDTOvnZK47yk7ShLWvrX98rCePiZ2icYt0mbo0FxQ-1792031318-1.0.1.1-plAiNn..YD1tKLmdadOjbqRH5XwrJT_1l7yA85R85qk",cvId: '3',cZone: 'www.etymonline.com',fa:"/word/atlas?__cf_chl_f_tk=UxlDTOvnZK47yk7ShLWvrX98rCePiZ2icYt0mbo0FxQ-1792031318-1.0.1.1-plAiNn..YD1tKLmdadOjbqRH5XwrJT_1l7yA85R85qk",md: 'YkdhAGWjVCccWcfQukbcZ0XTYjjkS8qRn__1RVrvJpg-1792031318-1.2.1.1-9dUuve
=== talent
 Just a moment... *{box-sizing:border-box;margin:0;padding:0}html{line-height:1.15;-webkit-text-size-adjust:100%;color:#313131;font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji"}body{display:flex;flex-direction:column;height:100vh;min-height:100vh}.main-content{margin:8rem auto;padding-left:1.5rem;max-width:60rem}@media (width Enable JavaScript and cookies to continue (function(){window._cf_chl_opt = {cFPWv: 'g',cH: 'gl81OhmKd_59GoJd7lX5c4vhiecpvxukSfLP5mL.sIk-1792031318-1.2.1.1-CGUu70xcyTsIucZ_qqGj4WVqWyI61NZ4yj2qlI7HU52q0jjEcrJMAl3VNhA5TzdZ',cITimeS: '1792031318',cN: 'EBHjrjegr77e4kKqXz6aDV',cRay: 'a4ab643a6943080c',cTplC:0,cTplO:0,cTplV:5,cType: 'managed',cUPMDTk:"/word/talent?__cf_chl_tk=eAKVb5Usj4fF0r9BrXFry_QDQZJtz8hKt03W3K_2NME-1792031318-1.0.1.1-hp8bosMyycWTZxrkiyyfiYxpgDWkdTAU_tVBZccvuhg",cvId: '3',cZone: 'www.etymonline.com',fa:"/word/talent?__cf_chl_f_tk=eAKVb5Usj4fF0r9BrXFry_QDQZJtz8hKt03W3K_2NME-1792031318-1.0.1.1-hp8bosMyycWTZxrkiyyfiYxpgDWkdTAU_tVBZccvuhg",md: 'sSUHw35iaURxmO.1lXIoeNTJEvuCH2XyRNrSnBtZbzs-1792031318-1.2.1.1-9XD.
=== tolerate
 Just a moment... *{box-sizing:border-box;margin:0;padding:0}html{line-height:1.15;-webkit-text-size-adjust:100%;color:#313131;font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji"}body{display:flex;flex-direction:column;height:100vh;min-height:100vh}.main-content{margin:8rem auto;padding-left:1.5rem;max-width:60rem}@media (width Enable JavaScript and cookies to continue (function(){window._cf_chl_opt = {cFPWv: 'g',cH: 'XtqmkeyNHlGrkbiabj_LMMym3lfACieWaMlqPZ2lMHU-1792031318-1.2.1.1-FFSjwr6pPzapmJLfAQXm41s.dgCRzJAUSO5ulfUUugzzMbeZwufeNJUk2EDj6Y8i',cITimeS: '1792031318',cN: 'Eqlxi5y6ig8d87fugyM6Ri',cRay: 'a4ab643aba81ab5d',cTplC:0,cTplO:0,cTplV:5,cType: 'managed',cUPMDTk:"/word/tolerate?__cf_chl_tk=i.QKa1eewBGmq0TUrYwPywwPHo8B.YQYKcpxIZ9cPo4-1792031318-1.0.1.1-mc3Vt3aQtll5sSobMWDtjK_I.o4YNPCj8xoG1N4NzNs",cvId: '3',cZone: 'www.etymonline.com',fa:"/word/tolerate?__cf_chl_f_tk=i.QKa1eewBGmq0TUrYwPywwPHo8B.YQYKcpxIZ9cPo4-1792031318-1.0.1.1-mc3Vt3aQtll5sSobMWDtjK_I.o4YNPCj8xoG1N4NzNs",md: 'Q56WYMVE6sVstHQ0TwxPPltYeYJr39dimOOJ2OgeL0k-1792031318-1.2.1.1-
=== relate
 Just a moment... *{box-sizing:border-box;margin:0;padding:0}html{line-height:1.15;-webkit-text-size-adjust:100%;color:#313131;font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji"}body{display:flex;flex-direction:column;height:100vh;min-height:100vh}.main-content{margin:8rem auto;padding-left:1.5rem;max-width:60rem}@media (width Enable JavaScript and cookies to continue (function(){window._cf_chl_opt = {cFPWv: 'g',cH: 'cSn_PQPhK10gdqv3nLN.Po7MhfNQUqydZczmYuhYAA4-1792031318-1.2.1.1-VlZEA2n_8pDSWdRLMcAe6bGtC9IR3nGWqQqdKPmMnbl7MXlM3SmxxQ9Vdx6dPk8r',cITimeS: '1792031318',cN: 'SMar3jD0ylLVBnpsbocK2e',cRay: 'a4ab643b0fbb94e3',cTplC:0,cTplO:0,cTplV:5,cType: 'managed',cUPMDTk:"/word/relate?__cf_chl_tk=pPsnnSFomy.zFToejNJ0pbAaPmhQrMdsXLfL4cj8DYc-1792031318-1.0.1.1-0yschUAOoldzaWM_jHvwUWxkmyDBZJ81TQFDB_9JfNY",cvId: '3',cZone: 'www.etymonline.com',fa:"/word/relate?__cf_chl_f_tk=pPsnnSFomy.zFToejNJ0pbAaPmhQrMdsXLfL4cj8DYc-1792031318-1.0.1.1-0yschUAOoldzaWM_jHvwUWxkmyDBZJ81TQFDB_9JfNY",md: '8YXJetCcDgxK1McuZXnY.IAuccasUTapYu.vLRc5oP4-1792031318-1.2.1.1-_Owv
=== translate
 Just a moment... *{box-sizing:border-box;margin:0;padding:0}html{line-height:1.15;-webkit-text-size-adjust:100%;color:#313131;font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji"}body{display:flex;flex-direction:column;height:100vh;min-height:100vh}.main-content{margin:8rem auto;padding-left:1.5rem;max-width:60rem}@media (width Enable JavaScript and cookies to continue (function(){window._cf_chl_opt = {cFPWv: 'g',cH: 'DCPC9XKSiEYmYQOt5rQkYAlmht_RY213ZiejQcfdUE4-1792031318-1.2.1.1-vh1OkcQjCwtNLPeE25VYPBhMdrsdr9oX6zTRwFDwkfuHgysT6XyvxEo.k7cAAb6_',cITimeS: '1792031318',cN: 'pEZhIPYpDqsd7LL9jW5dOh',cRay: 'a4ab643b8f76ab60',cTplC:0,cTplO:0,cTplV:5,cType: 'managed',cUPMDTk:"/word/translate?__cf_chl_tk=awHHVb3o1_lFsCRri4pxR_8le9ckxAYWPHvsgMUSq1U-1792031318-1.0.1.1-idX.teCcRAc_cyL08gOAS9A2wb3bXAL72SD4966zvDE",cvId: '3',cZone: 'www.etymonline.com',fa:"/word/translate?__cf_chl_f_tk=awHHVb3o1_lFsCRri4pxR_8le9ckxAYWPHvsgMUSq1U-1792031318-1.0.1.1-idX.teCcRAc_cyL08gOAS9A2wb3bXAL72SD4966zvDE",md: 'fXbZrVwXYe0etYdX71FOZtImAoV0vvXURaN0ijaKq8c-1792031318-1.2.1.
```


## [2026-10-15T02:28:43.120Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /tmp; for w in tolerate relate translate talent atlas '%CF%84%CE%AD%CE%BB%CE%BF%CF%82' '%CF%84%CE%AC%CE%BB%CE%B1%CE%BD%CF%84%CE%BF%CE%BD' 'toll%C5%8D' 'l%C4%81tus' '%E0%A4%A4%E0%A5%81%E0%A4%B2%E0%A5%8D%E0%A4%AF'; do echo \"=== $w\"; curl -s \"https://en.wiktionary.org/w/index.php?title=$w&action=raw\" | grep -i -A3 '^===Etymology' | head -14; done 2>&1 | cut -c1-600"
}
```


### [2026-10-15T02:28:44.876Z] TOOL RESULT

```
=== tolerate
===Etymology===
{{root|en|ine-pro|*telh₂- (bear)}}
{{bor+|en|la|tolerātus}}, the {{glossary|perfect}} {{glossary|passive}} {{glossary|participle}} of {{m|la|tolerō||to endure}}, see {{af|en|-ate|id1=verb|pos1=verb-forming suffix}}. Cognate with {{cog|ang|þolian||to tolerate, suffer, bear}} and {{cog|fr|tolérer}}. More at [[thole#Etymology_1|thole]].

=== relate
===Etymology===
{{root|en|ine-pro|*telh₂- (bear)}}
From {{der|en|la|relātus}}, perfect passive participle of {{m|la|referō||carry back; report}}, see {{l|en|-ate|id=verb|pos=verb-forming suffix}}. {{doublet|en|refer}}. See also [[infer]], [[collate]] and [[confer]], [[delate]] and [[defer]], as well as [[prefer]] and [[prelate]] among others.

=== translate
===Etymology===
{{root|en|ine-pro|*telh₂- (bear)}}
From {{inh|en|enm|translaten|t=to transport, translate, transform}}, from {{der|en|xno|translater}}, from {{der|en|la|trānslātus}}, {{glossary|perfect}} {{glossary|passive}} {{glossary|participle}} of {{m|la|trānsferō|t=to transport, carry across, translate}}.<ref name="OED">{{R:OED Online|pos=v|id=204841|date=March 2019|nodot=yes}}; {{R:Lexico|pos=v}}</ref> See also {{af|en|-ate|id1=verb|pos1=verb-forming suffix}}. Distant {{dbt|en|transfer|nocap=1}}, see {{m|en|collate}} and {{m|en|confer}}, {{m|en|delate}} and {{m|en|defer}}, as well as {{m|en|prelate}} and {{m|en|prefer}} among others.

=== talent
===Etymology===
{{ety|en|:inh|enm:talent|tree=1}}

From {{inh|en|enm|talent}}, from {{inh|en|ang|talente}}, borrowed from the plural of {{der|en|la|talentum||a Grecian weight; a talent of money}}, from {{der|en|grc|τάλαντον||balance, a particular weight, especially of gold, sum of money, a talent}}. Compare {{cog|goh|talenta||talent}}. Later figurative senses are from {{der|en|fro|talent||talent, will, inclination, desire}}, derived from the biblical {{w|Parable of the Talents}}.
--
===Etymology===
{{bor+|ca|la|talentum}}, from {{der|ca|grc|τάλαντον}}.

===Pronunciation===
--
===Etymology===
{{ety|cs|:bor|la:talentum|text=+|tree=1}}

===Pronunciation===
=== atlas
===Etymology 1===
{{root|en|ine-pro|*telh₂- (bear)}}
Borrowed from {{bor|en|la|Atlas}}, from the name of the {{der|en|grc|-}} mythological figure {{m|grc|Ἄτλας||Bearer (of the Heavens)}}, from {{m|grc|τλῆναι||to suffer”, “to endure”, “to bear}}. The sense referring to books of maps comes from the Atlas of Mercator, which he named thus in honor of Atlas, who was supposed to be skillful in astronomy and the doctrine of the sphere. The sense referring to the vertebra reflects that the spine carries the globe of the cranium (the neck carries the head).

--
===Etymology 2===
{{etymid|en|satin}} {{root|en|ar|ط ل س}}
From {{bor|en|ar|أَطْلَس||satin|id=rag}}.

--
===Etymology 1===
From {{der|ceb|en|atlas}}, from the name of the {{der|ceb|grc|-}} mythological figure {{m|grc|Ἄτλας||Bearer (of the Heavens)}}, from {{m|grc|τλῆναι||to suffer”, “to endure”, “to bear}}.

====Noun====
=== %CF%84%CE%AD%CE%BB%CE%BF%CF%82
===Etymology===
{{etymon|grc|id=goal|:inh|grk-pro:*kʷélos<ety:inh<ine-pro:*kʷelh₁-<id:turn>>>}}
From {{inh|grc|grk-pro|*kʷélos}}, from {{inh|grc|ine-pro|*kʷel-|*kʷél-os ~ *kʷél-es-}}. See {{cog|la|colō}} for more. Also from {{inh|grc|grk-pro|*télos}}.

--
===Etymology===
Inherited from {{inh|el|grc|τέλος}}. Sense "tax, dues", learnedly from {{der|el|grc|τέλος}}.

===Pronunciation===
=== %CF%84%CE%AC%CE%BB%CE%B1%CE%BD%CF%84%CE%BF%CE%BD
===Etymology===
{{etymon|grc|:inh|grk-pro:*tálanton<ety:der<ine-pro:*telh₂-<id:bear>>>}}
From {{inh|grc|grk-pro|*tálanton}}, from {{der|grc|ine-pro|*tl̥h₂ent-}}, from {{m|ine-pro|*telh₂-|t=to bear, endure}},<ref>{{R:grc:EDG|page=1445|head=τάλαντα|passage=VAR > Secondary sing. τάλαντον}}</ref> whence also {{m|grc|ἔτλην|t=to carry, endure}}.

=== toll%C5%8D
=== l%C4%81tus
=== %E0%A4%A4%E0%A5%81%E0%A4%B2%E0%A5%8D%E0%A4%AF
===Etymology===
{{bor+|hi|sa|तुल्य|t=equivalent, comparable}}.

===Pronunciation===
--
===Etymology===
From {{af|sa|तु॒ला|-य|t1=balance, scales}}.

===Pronunciation===
```


## [2026-10-15T02:28:53.510Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n '^TOLL\\|^ATLAS\\|^TALENT\\|^TOLERATE\\|^TRANSLATE\\|^RELATE' SKT.txt | head; grep -n 'tollō\\|^tollo\\|tollo,' LAT.txt | head -5; grep -n 'آتلانتیک\\|آتلانتيك' MON_part1.txt MON_part2.txt incoming/MON/*.txt | head; grep -n 'اطلس' MON_part1.txt | head -5; grep -n 'اطلس' incoming/MON/MON_2vol_Adena_v1_djvu.txt | head -5"
}
```


### [2026-10-15T02:28:53.910Z] TOOL RESULT

```
19106:TALENT,
19805:TOLERATE-
19826:TOLL,
19500:vera le haut: effero (ec-), extollo, eueho. A cette id 4 e a'apparente
61543:suspicio, suscito; suspendo, sustollo, sustineo et sans doute devant
64694:et de supin a feri} en face de tollo, dont 1'aspect est "d 4 terain 4 ",
14117:اطلس: ۵ (زمعر.] پرنیان» دینا» بارچه 
14122:دارای نقشه‌های متعدد باشد: اطلس تشر یح. 
14124:اطلس. 
14126:اطلسی: :2018 [معر. ف.] (ص نس.) 
14129:منسوب به اطلس. (گیا.) گیاهی است زینتی 
14117:اطلس: ۵ (زمعر.] پرنیان» دینا» بارچه 
14122:دارای نقشه‌های متعدد باشد: اطلس تشر یح. 
14124:اطلس. 
14126:اطلسی: :2018 [معر. ف.] (ص نس.) 
14129:منسوب به اطلس. (گیا.) گیاهی است زینتی
```


## [2026-10-15T02:28:56.026Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 14112,14132p MON_part1.txt; sed -n 19106,19110p SKT.txt; sed -n 19805,19830p SKT.txt | head -30; grep -n 'Atlas' SKT.txt | head -3"
}
```


### [2026-10-15T02:28:56.405Z] TOOL RESULT

```
هو ارو شرس اتصسال 
کلمه‌ای در معنبی مخصوص. (امسص.) 
رهایی» آزادی» خلاص از بند و قید. () 
حقی که به نوسندة مفاصا حساب پرداخته 
می‌شد» حق الاطلاق) ج. اطلاقات. 
اطلس: ۵ (زمعر.] پرنیان» دینا» بارچه 
ابر شمی. ساده» بی‌برز. (جاذ.) فقر و اول از 
فقرات گردن که بلافاصله زیر استخوان 
قمحدوه قرار گرفته و بر آن سوار است. 
(جف.) کتاب مصور جغرافی» هر کتابی که 
دارای نقشه‌های متعدد باشد: اطلس تشر یح. 
(نج.) سطح مقعر فلکك نهم. (اخ.) اقیانوس 
اطلس. 

اطلسی: :2018 [معر. ف.] (ص نس.) 


منسوب به اطلس. (گیا.) گیاهی است زینتی 


۱۹ فرهنگ فارسی معیز اطما 
TALENT,
S.  laiu,  noinber,  narrative  (Above). tiiien,  Iccl.  telja,  Dan.  tfrlie,  Swed. G.  idhlen ;  all  Irom  the  sbs.  above. alent.  (F.-U-Gk.)  The  sense  of ibility*  U  firom  the  parable;  Malt.  xxt. '.  iaUmt^  'a  talent  in  mon;:  also  will, eairc;*  Cot.  — L.  takntum.'^Gk..  rdAu'- »r,  a  balancCf  weight,  sum  of  money. iXent.  Named  from  being  liJted  and peighed ;  cf.  Skt.  /«/,  L.  toiUre,  to  lift v.  T(iA-of,  fustaining.  (^TAL.)  Allied D  Tolerate.    D«r.  taUnt'td,  in  nse  before
D.  1700.
ValiBXD&n,  a  spell.  (Span.-Arkb.V'GlL) ipaA.  is/uman,  a  maigical  character.  •- Lrab-  tihamdm^  pi.  of  fi/sam,  tilism,  a tisman,  magical  image.  —  Late  Gk. WA«4r;ut,  mystery,  initiation:  Gk.  riXtaita, p«yrocQt ;  TtX«<r/iA,  ui  accomplishment. Glc  rtxifiv^  to  accomplish,  end.<-Gk. ifXor,  end;  also  initiation  into  a  mystery. H  Skt.  tri,  to  pass  over,  fulfil,  tara^  a BSBacc,  a  spell.  (VTAR.) ^^al^  (Scand.  — Lith.)  Connected  with b7  and  /j/r  in  popular  etymology;  bnl rrongty.  M.  E.  talken.  —  Sweu.  tolka, Itan.  ^Ikt,  Icel.  /i//ia,  to  interpret,  explain, lead.-Swed.  Dan.  totk,  Icel.  Hilkr,  an lerpreter,  speaker;  M.  H.  G.  talk,  the *  Lithuanian  tulkas.,  an  interpreter ; %iJk^,  to  interpret ;  /rr  tuikas  kalbfti,  to re»ch  by  means  of  on  interpreter.  Frob. Bied  to  Skt.  tark.  to  suppo^,  speak. '  The  only  Lithuanian  word  in  English ; to  some  intercourse  between  the dinavians  and  Lithnaniau  by  means Fan  intrrfnttr.
Fall,  hish  m  suture,  lofty.  (E.  »r  C.  7) .  E.  /aA  which  meant  seemly,  elegant; ■lao  means  obedient,  good,  obsemiioas, UiaJit,  bold,  great.  Allied  to  A.  h.  /*/, >pe«ring  in  l^-tal,  friendly,  mn-ta^  bad loftbamb.  Goapels,  Malt,  xxvii.  ^i). be  aenae  of  tsJ  seems  to  have  been  good excellent ;  allied  to  A.  S.  /As/0,  ttla, ^•w^  well,  excellently.  So  also  Goth, w/r,  indocile,  uninstracted,  from  which infer  iaU,  dodle,  allied  to  Goth,  gafih^ table.  A.  S.  til,  fit.  good,  excellent  (a word),  whence  K.  tiii.  verb.  See 111  (1).  pL  But  in  the  particular  sense  of iofty'  (almo&t  the  only  sense  left  in  the od.  E,  /a/O,  the  word  may  be  Celtics  cf, tai.  high.  Com.  tat,  high;  Com.  tal m,  the  high  rock.  It  is  rcmiirkable  that h  ta.ila  means  *mecc  fit.  proper,  jo&t' difKcoU  word.)
TOLERATE-
Tod,  a  bush,  a  measure  of  v^xr^^ ^Scand.)  Icel.  totidi,  a  lod  of  n^l piece  (the  fox  being  named  ttd  fro bushy  tail).<t-G.  c4*//«.  swir,  a  tuft  ol anything  sluiggy.
Todny ;  sec  To.
Toddle ;  sec  Tilt  (a^
Toddy,  (llimiustani.)  Hind.  M '  vulgarly  loddv,  juice  or  sap  of  tlie  pa tree,*^&c.;  H.  II.  \Vilson.-Hind. palm-tree,  palmyra  tree.  ^  The  r pectdiar  sound,  which  has  come  lo presented  by  dm  English
Toe.   (E.)     A.  S.   fd,  dL  /d»«.    J tracted    form,    standing    for  tdke*.- teen,  Icel.  td,  Dan.  taa.  Swed.  ftf.  0 O.  H.  G.  ijhd,  a  tr>e.  alio  a  fanger. to  Dl^t.
Toft;  see  Tuft  (j).
To^a :  see  Tegument.
Together ;  sec  Oalhsr
Toil  (1  J,  labour;  to  labour.  (F. M  £.  toti,  disturbance,  titmalt;  Ml pull  about  (the  sense  having  son altered). »0.  F.  (ouilier,  to  entangie, together,  mix  coafuserity,  tronbte.  Ai Cotgrave.  Frob.  from  a  ftequenticiv of  U.  H.  G.  nitcchen  (G.  tU£Xtn\  to  1 pull  quickly ;  cf.  O.  H.  G.  aoeciJa,  t tear,  snatch  away,  ifigSn,  to  Icat,  pi derivatives  from  O.  H.  G.  tihaet  (.G.J to  pull;  see  Tow  (i).  %  7W  k derived  from  O.  Da.  htyUn^  t» manuie  land,  but  it  is  impossible  10  4 it  from  this  source;  the  M.  E.  u completely  at  vaiiance  with  this  \-iri
Toil  (I),  a  snare;  see  Text,
Toilet,  Toilette ;  see  Toxt,
Tolse;  sec  Tend  ;i).
Tokay,  a  wine.  \  Hungary.)    From a  town  in  Hungary,  t  N.  E  from  P
Token.  (E.)  hi.  K.  token.  AS. tden.  -  A.  S.  tedA  (  -  tdh  •),  pt  L  <rf usually  ti^n,  to  point  out.  todjciie, to  accuse,  criminate.  4*  Do  tetkm, tdhn,  teikn,  Dan  tegm.  Swed.  McAl uichen,  Goth  taikm.  All  from 'XWX^^ViWi,  whence  U  in point  out.     Sec  Diotlon.
betoken     (E)       Fomied with  prefix  6e-»  X.  S.  6t-,  bi,
teach.  ^E.)  M.  E.  ftxheu  tZ to  shew  how  to  do.  shew,  pL  t  tsAt t'kht.  Forine<J  (with  usual  wcng<  Am di\  from  tde-^  base  of  Al^Mt  A appearing;  as  ttdk^  pt  t.  of  tUum
Tol  -        -
-d.    MdM
I
oleraM.  yjL^)    Ffom  ppu  of  J
TOLL,
ip  with;  ftlltcd  to  tolUrt^  to  lift, Be.-4>Skt.  /h/.  to  Ua,  Gl.  rX^»-ai, Bi  S.  )v}/id«,  to  eodure.  ( V^AR, ■  From  L.  tlatum,  supine  of  tai Onr  written  latum,  are  formed  im- lenvatives,  such  as  ah  ht-ivi,  <oiiat- (X//j  ^-/o/^  rb-laU,  Sec. ;  see  below. ive ;  see  Ablative. SiOB,  n  comparison ;  fomierly,  a ft  (F.-L.)  O.  F.  <oiiiUi0H,  a f  »L.  ace.  toHeUioHtm,  n  bringing a  conferring.  — L.r0i7a/u/n,  supine th  the  verb  tonferrtt  to  briny  in- mL  from  a  different  rootl.  —  L.  col' BfWM),  together;  latunt^  supine Hb  take,  \)w.  See  above. late,  to  relate  or  refer  mutually. Jancd  from  L.  cqt'  (scum),  to- ■d  relate  (below), ■b.  (F.-L)  O.  F.  d>/ai,  delay. K  ai  Ital.  dilata,  dday.)  -  L. em.  of  dilaiuf,  deferred,  put  off. ^dis'\  apart;  latuSt  borne,  car- WL^iirt  (above). ItF.-L.)  0.  F.  dUaier.  to  widen wHu,  spread  abroad ;  the  same  as Jdierrecf ;  see  delay  i^abovc). gifted  up,  proud.  (L.)  L.  etatus, KL.  ^,  out ;  lalM,  pp.  of  tollere,
BfL.)  L.  txtalUrtt  to  lift  or Bu  eXt  out,  up;  tolltn.  to  lift. iTwidaKd  at  the  sidca.  (L.)  L. Iptead  out  vat  the  sides).  — L.  oh, laim,  bone,  earned  out,  pp.  of I  bear.
E,  lui  olTering.  (F.  —  L.)  F. offer  ing  ;  Cot.  — L,  ace.  Ma- of  phlatie,  an  offering.  —  L. bed  as  pp.  of  cftrrt.  to  offer  (but Iffereiil  coot);  see  oblate  (above). ta,  a  church  dignitary.  (F.  — L.) r(!s/.—  L.  ^ntlaiw,  set  above ;  used ra/irrt.  to  prefer  (but  from  a >t).  —  L.  pra,  before :   laitu,
of  (ollfri,  to  lift.  bear. extended  in  the  direction  of U.  (L.)     \^.prtlatiu,  extended. >rwaid;  /«/ia,  carried,  pp.  of l>car. flcvribc,  tell  (F.-U)    Y.rt- ite;*  Cot— Low  L.  relatan^ rtlAtm,  u«d  ai  pp.  Q^rtjerre, (butfromadiffcrcnt  root).  — L.  nr-, Uui,  bcjnie.  pp.  of  tollere,  to  bear. Its.    (F.-L.)      ¥.  super .att/, 'Udi$iu4,  u  a   grammatical
1094:Atlas.  (Gk.)  Named  afler  Atlns,  the demi-god  who  was  said  to  bear  the  world on  his  shDulders ;  his  figure  used  often  lo appear  on  the  title-page  of  atlases.  — Gk. ■'AtAoj  Cficn.  'ArAo»'Tiit>,  prob.  "the  sus- tainer'  or  l»earer,  from  ^  TAL,  to  bear.
1095:&U.autic,  sn  ocean,  named  after  Ml. Atlas,  in  the  N.W.  of  Africa;  from  aude form  'ArAavn-,
```


## [2026-10-15T02:29:04.861Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /اطلس/{print \"LEAF\",NR-1}' BQT_v1_pages.txt | head"
}
```


### [2026-10-15T02:29:05.488Z] TOOL RESULT

```
LEAF 371
LEAF 473
LEAF 528
LEAF 751
```


## [2026-10-15T02:29:07.345Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==372{print}' BQT_v1_pages.txt | grep -n -B3 -A8 'اطلس' | head -40"
}
```


### [2026-10-15T02:29:07.767Z] TOOL RESULT

```
46-خیم آن ماد سمی کونی‌تین بافت شود « کل کارب 2۱۹۹ ۰
47-افیانوس - از بونانی 1662705() بمعنی‌سریم . این کلمه
48-درعربی نیزمستممل امت ودرجفرافیا بدرباهای بز رکه اطلاق‌شود «نفس».
49:پنج اقیالوس کرة ارش‌عبارتست از : اقیانوی کبیر»اقیانوی اطلس ۰ افیانوی
50-جند » أقیانوی منجمد شمالی و افیانوی منجمد جنوبی -
```


## [2026-10-15T02:29:11.595Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 350 351 352 353 354 355; do echo \"LEAF $n: $(awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1{print}' BQT_v1_pages.txt | head -c 300 | tr '\\n' ' ')\"; done; awk 'BEGIN{RS=\"\\f\"} NR>=350&&NR<=358{print NR-1\": \"$0}' BQT_v1_pages.txt | grep -n 'طلس\\|اطل' | head"
}
```


### [2026-10-15T02:29:12.245Z] TOOL RESULT

```
LEAF 350: اسکندروی و دختثر از دارا حامله بودوأنظهار نمیکردتابوی دهن‌اورا با اسکندروی که آنرا بفارسی سیر کوشد علاح کردند و مدازآن فرزند بوجود آعد او را لسکنتو منم نهلدند . و تل
LEAF 351: - و۱۳ اسمنك بفتح اول وثالث وسکون نانی اسمند‌ر » بنتح او » پمعشی سمئدر باشد و آن چانوریت که در آتش حتکون میشود ۷ . اسموسا ه بح اول و سکون ثانی ومیم بوأو رسیده وسین بی‌نق�
LEAF 352: باشد ٩‏ - و بلفت زند و پازند (۱) بمعنی مینه است که جربی صدر خوانند ۴ . اسیر لگ - بارای فرشت بروز نکنيزك . یار خریزه را کوش . اسیز ۵ ]یه بنتح اول ورابع وسکون عیم» داروی چندی ا
LEAF 353: وا اول هم آمده است ٩‏ . اشتاب ۴ - جن‌اول وسکون بایابید. بمعنی ثتاب و تعجیل باشد » و بکر اول حم آمده است » و بجای حرف آخر واو هم کفته‌اند که اشتاو باشد . اشتا ؟ - بفتح اول ب
LEAF 354: اشتر گیا - بکر کاف فارسی و تحتانی بالف کشیده , بممتی اشتر خار است که خار شتری باشد ۰ و بسضنی کوبند کیاهی است‌دوابی که آنرا سلخه خوانند . اش شتر هرع - پرنده است که بای او ش
LEAF 355: و سکن الی و دال ابجد , نام روزدوم است از خمسا مترفةٌ فدیم- وبودن آفتاب دربرجعفرب ودرین روز عفان بمنی آتش پرستان جش نکنند و بمعنی اول بجای فوفانی نون عم آمده است . اشتیم -
```


## [2026-10-15T02:29:16.171Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in $(seq 356 368); do echo \"LEAF $n: $(awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1{print}' BQT_v1_pages.txt | grep -o '^ *ا[^ ]\\{2,8\\}' | head -4 | tr '\\n' ' ')\"; done"
}
```


### [2026-10-15T02:29:17.150Z] TOOL RESULT

```
LEAF 356: اخك اشگر اشگر اشکش 
LEAF 357: اشکو اشکوخیه اشکو اشکوه 
LEAF 358: اشو اشتاف اشیهه اشو۱ 
LEAF 359: اصطر اصطر ارتفاع اطماط 
LEAF 360: اطموط اطمسا اغره اغریا 
LEAF 361: اغشته اغلیسون افربدون افتدستا 
LEAF 362: اتمون الثمرا اقچ4 است 
LEAF 363: افر افر ارف افر 
LEAF 364: افری افر اللام اقفر 
LEAF 365: اسر افسرسگزی افسر افستتین 
LEAF 366: اقشه افغات» افشین افی 
LEAF 367: افگنده(۱) افالا افندبدن افیلون 
LEAF 368: اقسوس اقشون افطن اقطی
```


## [2026-10-15T02:29:20.132Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; curl -sL -o dl499/bqt_n359.jpg 'https://archive.org/download/borhan-ghate-v1/page/n359_w1200.jpg'; file dl499/bqt_n359.jpg"
}
```


### [2026-10-15T02:29:21.849Z] TOOL RESULT

```
dl499/bqt_n359.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 1240x1754, components 1
```


## [2026-10-15T02:29:24.041Z] TOOL CALL #48: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/dl499/bqt_n359.jpg"
}
```


### [2026-10-15T02:29:24.064Z] TOOL RESULT

```

```


## [2026-10-15T02:29:33.916Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /tmp; for w in آتلانتیک اطلس تراز; do echo \"=== $w\"; curl -sL \"https://vajehyab.com/moein/$w\" | python3 -c \"\nimport sys,re,html;t=sys.stdin.read();s=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S);s=re.sub(r'<[^>]+>',' ',s);s=html.unescape(re.sub(r'\\s+',' ',s));i=s.find('معین');print(len(t), s[:100]); \nimport re as r\nfor m in r.finditer('$w',s):\n  pass\nj=s.find('(اِ')\nprint(s[max(0,j-300):j+900])\"; done"
}
```


### [2026-10-15T02:29:34.947Z] TOOL RESULT

```
=== آتلانتیک
5500  صفحه پیدا نشد | واژه یاب 26 فرهنگ 404 متأسفیم! صفحه‌ای پیدا نشد. خرید اشتراک افزودن واژه افزونه مرو
 صفحه پیدا نشد | واژه یاب 26 فرهنگ 404 متأسفیم! صفحه‌ای پیدا نشد. خرید اشتراک افزودن واژه افزونه مرورگر تماس درباره نسخه جدید 
=== اطلس
10394  معنی اطلس | فرهنگ انتشارات معین | واژه یاب 26 فرهنگ همه دیکشنری مترادف طیفی آزاد + همه دقیق مترادف 
 معنی اطلس | فرهنگ انتشارات معین | واژه یاب 26 فرهنگ همه دیکشنری مترادف طیفی آزاد + همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه اطلس فرهنگ انتشارات معین (اَ لَ) [ معر - یو. ] (اِ.) 1 - پارچة ابریشمی . 2 - نام یکی از رب النوع های یونان قدیم که زمین را بر دوش خود حمل می کند. 3 - اولین مهرة گردن . 4 - نقشه جغرافی . 5 - سطح مقعر فلک نهم . 6 - نام اقیانوسی که بین اروپا و امریکا قرار دارد. اطلس در فرهنگ‌های دیگر معنی اطلس در لغت‌نامه دهخدا معنی اطلس در فرهنگ فارسی عمید / قربان‌زاده معنی اطلس در دیکشنری عربی به فارسی معنی اطلس در دیکشنری فارسی به عربی معنی اطلس در دیکشنری فارسی به انگلیسی معنی اطلس در فرهنگ مترادف و متضاد معنی اطلس در فرهنگ نام‌ها واژه‌های مشابه اطلسی اطلاع اطلاعیه اطلاق اطلاقی اطلال خرید اشتراک افزودن واژه افزونه مرورگر تماس درباره نسخه جدید 
=== تراز
10861  معنی تراز | فرهنگ انتشارات معین | واژه یاب 26 فرهنگ همه دیکشنری مترادف طیفی آزاد + همه دقیق مترادف 
 معنی تراز | فرهنگ انتشارات معین | واژه یاب 26 فرهنگ همه دیکشنری مترادف طیفی آزاد + همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه تراز فرهنگ انتشارات معین (تَ) (اِ.) 1 - زینت . 2 - نقش و نگار پارچه . 3 - ابزاری در بنُایی که به وسیلة آن ناهمواری سطح چیزی را مشخص می کنند. 4 - مانده ، تتمه . 5 - تفاوت بین کل اقلام بستانکار و بدهکار در هر حساب (حسابداری ). تراز در فرهنگ‌های دیگر معنی تراز در لغت‌نامه دهخدا معنی تراز در فرهنگ فارسی عمید / قربان‌زاده معنی تراز در دیکشنری فارسی به عربی معنی تراز در دیکشنری فارسی به انگلیسی معنی تراز در فرهنگ مترادف و متضاد معنی تراز در واژه‌نامه آزاد معانی دیگر تراز تراز (2) واژه‌های مشابه تراز کردن ترازنامه ترازو چرب ترازو هم ترازو تاز تازان تازاندن تازنده تازانده خرید اشتراک افزودن واژه افزونه مرورگر تماس درباره نسخه جدید
```


## [2026-10-15T02:29:38.885Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; grep -n 'ترازو\\|تراز' ARY_pages.txt | head; grep -n -i 'TARAZ\\|TELƏ\\|TEL-\\|TELA' ARY_latin_index_pages.txt | head"
}
```


### [2026-10-15T02:29:39.213Z] TOOL RESULT

```
2400:Veav gt sebG iby STELA, (OLD ENGLISH) op 6!
```


## [2026-10-15T02:29:42.347Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'r[aā]z[uū]' HRN.txt HUB.txt | head; grep -n -i 'atlas\\|atlantic' HJB.txt LKT.txt | head -5; grep -n -i 'tulā\\|tulä' BRT.txt | head -3; grep -n -c 'telos' IEC.txt"
}
```


### [2026-10-15T02:29:42.709Z] TOOL RESULT

```
HRN.txt:5452:Geldner hatte KZ. 24, 387 Note 2 aw. razura-
LKT.txt:516:131.  Ar.  atlas:
LKT.txt:517:'Glatt,  fein'.  Von  einem  Manne,  der nicht  viel  taugte,  sagte  man,  er  sei atlas;  ebenso  von  Seide,  sie  sei  atlas, d.  h.  minderwertig;  schheßlich  blieb das  Adjektiv  allein  zur  Bezeichnung  des Stofifes  [wie  z.  B.  im  Romanischen,  wo aus  lat.  ieciir  firatum  frz.  foie  'Leber', aus  lat.  caseum  fonnaticum  frz.  froinaffe 'Käse'  wurde],  und  zwar  des  sog.  Seiden- satins  [s.  hier  Nr.  2188].  Rum.  atlas, atlaz;  russ.  atlas,  bulg.  atlaz,  serb.  cech. atlas,  poln.  atlas  'Satin'.  Dtsch.  Atlas, ndl.  atlas.  [Joseph  Karabacek,  Über einige  Benennungen  mittelalterlicher Gewebe.  Wien  188±  S.  llfT.  Gorjajew 7.  Hobson-Jobson  39/40.  Kluge  '25. Dozy  Oost  22.
LKT.txt:1689:Vulg.  gemesit  [aus  pers.  gärni  'Avarm' Horn  NpEt  S.  203,  Nr.  911,  und  süd 'Nutzen,  Vorteil'  ebenda  S.  166,  Nr.  751] 'eine  Art  Stoff' ;  hieraus  rum.  ghermesit 'Art  Atlas'.
LKT.txt:2910:'Kleiderstoff,  Zeug',  tk.  und  kas.-tat.  ku- mas;  hieraus  russ.  kumac  'bucharisctier roter  oder  blauer  Baumwollstoff,  bulg. kumaS  'Stoff',  serb.  kttmaS  'Seidenzeug, Atlas',  ßech.  kumaö  'Baum wollsl off'; rum.  comas,  cumas  'Seidenstoff'.  [Bern SlEtWb  643.
LKT.txt:4463:Auch  Tafilet,  N.  pr.,  zu  Marokko  ge- hörige Oase  südlich  des  Atlas,  in  der Lederindustrie  heimisch  ist;  hieraus  kat. pg.  tafilet,  sp.  tafilete  'feines  Leder, Saffian'.
7999:Zum  V.  *j..  —  ai.  vgl  Üvari.  Adj.  —  PQ. (lu  V.  47):  '■'äilär,  erl.!  patUläh.  (lu  Y.  43)- ifW).  ~  ')  Vgl.  iSt  Bthl.  IF.  s-  36'-  — ')  Als  halte  man  svä  gelesen.
2
```


## [2026-10-15T02:29:45.388Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 4560,4564p LKT.txt; sed -n 513,516p LKT.txt"
}
```


### [2026-10-15T02:29:45.711Z] TOOL RESULT

```
2027.  Kas.-tat.  tarakau: 'Schabe';   hieraus  russ.  tarukan,  cech. tarakan  'dass.',    vielleicht  auch  poln. karuczan.     [Gorjajew  360.     Mikl  SiEt Wl)  347  a.
2028.  Ar,  taran^nbin:
'Flüssige  pers.  Manna'  [aus  pers.  türiin- gubin:  tär  'feucht,  irisch'  Hoin  NpEt S.  85,  Nr.  382  und  änguhin  'Honig'  eben- da 8.29,  Nr.  124];  hieraus  sp.  terenia- bin,  frz.  tireniabin  \teremabin  in  Roma- nia  XXXV,  409;  s.  Behrens  Beilr  264] 'dass.',  fiz.  tringibin.  [DE  350.  Devic DEt  219/220.  Eguilaz  505.  Lammens Rem  239.
2029.  Pers.  täräzQ:
'Wage',  tk.  ebenso  terazi ;  hieraus  serb. teresije,  klruss.  terezy,  russ.  tereza ' Wase' ; rum.  tirizie,  terezie  'Wagscliale'.  [Löbel EITAP  94.    Mikl  SlEtWb  354  a.
'tölpelhaft,  uiigeschickl'.  |Sain  16.  Bern SlKt\VI):?3.  Gorjajew  13.  Karlowicz  4'i3.
li."J.  Ar.  'atai^a: 'Dürsten,  nach  elw.  gierige  sein'.  Hier- aus siz.  nttaciu  'riesiger  Appetit,  Gier, Brunsf;  attaciatii  'durstig,  ängstlich'. [GrSVociSic  ^J^!7.
13(».  Ar.  atflja: rir.  atäfl  'Dreifuß';  hieraus  mit  dem ar.  Ari.  sp.  annafe,  anafrc  'Kohlen- hecken, kleiner  tragharer  Ofen'.  In  der ar.  Aussprache  von  Granada,  wo  die Iniiila  fä  ^  ij  sehr  stark  war,  er- gab sich  atifl  und  hieraus  sp.  atifle 'irdener  Dreifuß'.    [DE  1S4  u.  ^215.
131.  Ar.  atlas:
```


## [2026-10-15T02:29:58.006Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,30p tools/fetch_source.py"
}
```


### [2026-10-15T02:29:58.328Z] TOOL RESULT

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
```


## [2026-10-15T02:30:03.954Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; W=https://en.wiktionary.org/wiki; f(){ python3 tools/fetch_source.py \"$1\" --note \"page 499, root Tel: $2\" 2>&1 | tail -1; }\nf \"$W/ترازو\" \"Persian tarazu < MP tarazug, Avestan source form\"\nf \"$W/طراز\" \"Arabic tiraz embroidery; Persian Taraz city famed for beauties\"\nf \"$W/طرز\" \"Arabic tarz / Persian taraz adornment, tarazidan\"\nf \"$W/اطلس\" \"Persian atlas: Greek Atlas vs Arabic satin\"\nf \"$W/أطلس\" \"Arabic atlas three etymologies\"\nf \"$W/Ἄτλας\" \"Greek Atlas < a- + *telh2-\"\nf \"$W/Reconstruction:Proto-Indo-European/telh₂-\" \"PIE root *telh2-\"\nf \"$W/τάλαντον\" \"Greek talanton < *telh2-\"\nf \"$W/τέλος\" \"Greek telos etymology\"\nf \"$W/toll\" \"English toll: native Germanic vs Lat teloneum\"\nf \"$W/atlas\" \"English atlas\"\nf \"$W/Atlantic\" \"English Atlantic\"\nf \"$W/talent\" \"English talent\"\nf \"$W/tolerate\" \"English tolerate\"\nf \"$W/relate\" \"English relate\"\nf \"$W/translate\" \"English translate\"\nf \"$W/तुला\" \"Sanskrit tula\"\nf \"$W/तुल्य\" \"Sanskrit tulya\"\nf \"https://vajehyab.com/moein/اطلس\" \"Mo'in atlas senses incl. ninth sphere\"\nf \"https://vajehyab.com/moein/تراز\" \"Mo'in taraz senses\"\n"
}
```


### [2026-10-15T02:30:25.026Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c3147513546e91f4.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/1e562e240ab10bca.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/fe449dee3f4d89af.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/0f9d65f63a3463e9.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3329c633bc58c88d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/dede77f710903899.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/5973a0175255db96.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/129821b48a3fd518.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8bf65fee12da4647.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c074970fbea98b34.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/770fd9bae8f1198b.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/7146bba51cfcf6ca.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/9590b6853fee0acc.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/6faece0aebab0e4d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2f4065d9ab84ade9.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/cbd4d048fb3c052f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/adc3d1a0419dafff.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a855290797bbb880.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8d1a26a04b66c09c.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/1c6343c3dab3ed07.txt
```


## [2026-10-15T02:30:26.841Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -n -i 'tax\\|telh\\|Beekes' 8bf65fee12da4647.txt | head -15"
}
```


### [2026-10-15T02:30:27.425Z] TOOL RESULT

```
202: Merger of two different roots: Proto-Indo-European *kʷel- ( “ to turn; to revolve around ” , yielding “turning point (of the field or race-course)” ) and *telh₂- ( “ to bear; to endure ” , yielding “levy (of a tax or army)” ) . [ 1 ] 
244: money paid to the government: tax , toll 
467: ^ Beekes, Robert S. P. ( 2010 ), “ τέλος ”, in Etymological Dictionary of Greek (Leiden Indo-European Etymological Dictionary Series; 10 ), with the assistance of Lucien van Beek, Leiden, Boston: Brill, →ISBN , pages 1463-4 
529: tax idem, page 857.
544: Inherited from Ancient Greek τέλος ( télos ) . Sense "tax, dues", learnedly from Ancient Greek τέλος ( télos ) .
562: tax , dues paid to the government for specific public service, or product
563: τέλος ακίνητης περιουσίας (ΤΑΠ) ― télos akínitis periousías (TAP) ― tax of real estate 
603: ατελής ( atelís , “ imperfect, tax-free ” , adjective )
```


## [2026-10-15T02:30:38.278Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr; mkdir -p BQT; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/dl499; ls BQT | grep -E '^0(143|479|480)' ; cp $S/bqt_n359.jpg BQT/0143.jpg; cp $S/bqt479.jpg BQT/0479.jpg; cp $S/bqt480.jpg BQT/0480.jpg\ncat > BQT/0143.vision.txt <<'EOF'\n[BQT vol.1 printed p.143 = archive.org borhan-ghate-v1 leaf n359; read from the page image]\nMo'in's added entry (marked ☼) in the footnote zone:\n☼ اطلس - از تازی، از یونانی Atlas (نام ربّ‌النوع حامل کرهٔ زمین) «نفس». کتاب شامل نقشه‌های جغرافی - جامهٔ ابریشمی پرز دار.\n(Column text above, for context: اصطرلاب - معروف است و آن آلتی باشد از برنج ... و این لغت یونانی است بمعنی ترازوی آفتاب چه اصطر ترازو ...)\nEOF\ncat > BQT/0479.vision.txt <<'EOF'\n[BQT vol.1 printed p.479 = archive.org borhan-ghate-v1 leaf n705; read from the page image]\nتراز - بر وزن نماز، رشتهٔ ریسمان خام را گویند - و نام درخت صنوبر هم هست - و نام شهری است در ترکستان که منسوب است بخوبان و معرب آن طراز باشد ۷.\nFootnote 7: ۷ - طراز (Talas, Ulugh Talas) «مینورسکی، حدودالعالم. فهرست».\nEOF\ncat > BQT/0480.vision.txt <<'EOF'\n[BQT vol.1 printed p.480 = archive.org borhan-ghate-v1 leaf n706; read from the page image]\nترازو ۱ - معروف است، و آن آلتی باشد که چیزها را بدان وزن کنند - و نام برج میزان هم هست که از جملهٔ دوازده برج فلکی است ۲ - و عدل و عدالت را نیز گویند و بمعنی ادراک و درک هم آمده است.\nFootnote 1: ۱ - پهلوی tarâzûk، ایرانی باستان ☼ tarâzu = ☼ tara - âzu : ☼ tara از سانسکریت tulati، tulya، âz، az از سانسکریت aj (راهنمایی کردن، راندن، پیش‌بردن)، «نیبرگ ۲۲۳». رک: مزنا.\nFootnote 2: ۲ - = خوارزمی: ترازك = عربی: میزان. برج هفتم از بروج دوازده‌گانه «گاه‌شماری ص ۲۰۳».\nEOF\nls BQT | grep -E '^0(143|479|480)'"
}
```


### [2026-10-15T02:30:38.675Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-15T02:30:40.078Z] TOOL CALL #57: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/ | grep -E '0(143|479|480)'"
}
```


### [2026-10-15T02:30:40.591Z] TOOL RESULT

```
.rw-r--r--  190k sfmqrb 14 Oct 22:30  0143.jpg
.rw-r--r--   576 sfmqrb 14 Oct 22:30  0143.vision.txt
.rw-r--r--  202k sfmqrb 14 Oct 22:30  0479.jpg
.rw-r--r--   444 sfmqrb 14 Oct 22:30  0479.vision.txt
.rw-r--r--  205k sfmqrb 14 Oct 22:30  0480.jpg
.rw-r--r--   849 sfmqrb 14 Oct 22:30  0480.vision.txt
```


## [2026-10-15T02:33:34.056Z] TOOL CALL #58: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/gen-499.py",
 "content": "import json\n\nW = \"https://en.wiktionary.org/wiki/\"\nPOK_Q = (\"Pokorny IEW pp.1060-1061 (local POK_full.txt line 85184, 'Root /lemma: tel-1, tela-, tle(i)- tla-', Page(s): 1060-1061): \"\n         \"'Meaning: to transport, carry; to bear, suffer'; 'Old Indie tula 'scales, weight', tulayati 'hebt auf, wägt' ... tulya- 'gleichartig, comparable''; \"\n         \"Greek tlēnai, talanton ('die beiden Waagschalen'), PN Atlas, -antos, telos 'payment, tribute, tax'; 'Latin tollo, -ere ... tolero ... latus 'getragen''.\")\nAHD_Q = (\"Watkins AHD Roots (local AHD_watkins1985.txt line 1078) s.v. telə-: 'To lift, support, weigh; with derivatives referring to measured weights and thence to money and payment' — \"\n         \"2a 'Greek telos, tax, charge: TOLL1'; 2b 'Latin tolerare ... TOLERATE'; 4 '*tala-nt- in Greek talanton, balance, weight ... TALENT'; 6 'Perhaps zero-grade form *tla- in Greek Atlas ... ATLANTIC, ATLAS'; \"\n         \"8 '*tl-to- in Latin lātus ... RELATE ... TRANSLATE'; 9 '*tl-ā- in Sanskrit tulā, scales, balance, weight'; 10 '*tl-n-a- in Latin tollere'. [Pok. 1. tel- 1060.]\")\nWLD_Q = (\"Walde-Pokorny Bd. I pp.738-740 (local WLD_Bd1_pages.txt leaves 747-749) '1. tel- „aufheben, z. T. wägend, z. T. sich aufladend; tragen; ertragen, dulden“: Ai. tulā „Waage, Waagbalken“, tulayati „hebt auf, wägt“' ... 'τάλαντον ... eig. „die beiden Waagschalen“', 'Ἄτλας, -αντος', 'lat. tollo ... tolero ... lātus'.\")\nKLN_TOL = (\"Klein 1966 s.v. tolerate (KLN_1966.txt line 39457): 'L. tolerare ... from the stem of tollere ... cogn. with ... ταλάντον 'balance', ''A-τλας 'the Bearer (scil. of Heaven)', L. lātus (for *tlatos) 'borne', OI. tulā 'balance', tulayati 'lifts up, weighs' ... All these words derive fr. I.-E. base *tel-, *tol-, *tal-, *tl- 'to bear, carry, endure, suffer'.'\")\nNYB_Q = (\"Nyberg, Manual of Pahlavi II p.191 (NYB_vol2_glossary.txt line 3737): 'tarāzūk [tlʾcwkʾ] balance, scales for weighing ... — OIr *tarā = Skr tulā 'balance, scale of a balance' + Av. (223 sq.) az- 'to convey, to conduct' (Lat agere)'; index p.? lists 'tulā: tarāzūk'.\")\nPHD_Q = (\"MacKenzie CPD (PHD_mackenzie.txt line 4927): 'tarāzūg [tlʾcwkʾ | (P tlʾzwg), N tarāzū] balance, scales; astr. Libra'; line 4926 'tarāzēnīdan, tarāzēn- weigh'. No Old Iranian etymology given.\")\nPLA_Q = (\"Asbaghi, Persische Lehnwörter im Arabischen p.194 (PLA_pages.txt leaf 209; ref_page.py PLA:194 --pdf-page 209): 'ṭirāz: „Stickerei, Rand, Saum“ pers. tarāz, mp. taraz' and 'ṭirāzdārān: „Futteral der Waage“ pers. tarāzūdārān, mp. tarāzūk „Balance, Gleichgewicht“ air. *tarā = skr. tulā + aw. az „zuführen“; tk. terazi, serb., kl.russ. terezy'. \"\n         \"The cited page is the source of Nourai's tara-āz analysis, but it labels the form Old Iranian (air.), not Avestan.\")\nBQT480_Q = (\"BQT vol.1 p.480 (archive.org borhan-ghate-v1 leaf n706, read from image; saved ocr/BQT/0480.vision.txt) s.v. ترازو, Mo'in's fn.1: 'پهلوی tarâzûk، ایرانی باستان ☼tarâzu = ☼tara-âzu : ☼tara از سانسکریت tulati، tulya، âz، az از سانسکریت aj (راهنمایی کردن، راندن، پیش‌بردن)، «نیبرگ ۲۲۳»'. \"\n            \"Asterisked = reconstructed Old Iranian, after Nyberg.\")\nBQT479_Q = (\"BQT vol.1 p.479 (leaf n705, image; ocr/BQT/0479.vision.txt) s.v. تراز: 'رشتهٔ ریسمان خام را گویند - و نام درخت صنوبر هم هست - و نام شهری است در ترکستان که منسوب است بخوبان و معرب آن طراز باشد' (fn.7: طراز = Talas). \"\n            \"No 'level/balance' sense and no link to ترازو.\")\nMON_TARAZ = (\"Mo'in, Farhang-e Farsi via vajehyab s.v. تراز: '(تَ) (اِ.) ۱- زینت. ۲- نقش و نگار پارچه. ۳- ابزاری در بنّایی که به وسیلهٔ آن ناهمواری سطح چیزی را مشخص می‌کنند. ۴- مانده، تتمه. ۵- تفاوت بین کل اقلام بستانکار و بدهکار' — \"\n             \"the 'level' and 'balance (accounting)' senses sit beside 'adornment, embroidery', which belong to a different word.\")\n\nnodes = []\n\nnodes.append(dict(\n id=1, lang=\"Sanskrit\", words=\"tulâ, tulya\", verdict=\"confirmed\",\n derivation=(\"Sanskrit tulā́ f. 'balance, scales; weight' continues the zero grade *tl̥h₂-éh₂ of PIE *telh₂- 'to lift, weigh, bear': syllabic *l̥ before the laryngeal gives Indo-Aryan ul (the l is the dialectal Indo-Aryan reflex of *l, the u the coloured vowel of the syllabic liquid). \"\n             \"tulya- 'equal in weight, comparable, equivalent' is the -ya- derivative of tulā (Wiktionary: from tulā + -ya), and the verb tulayati 'lifts, weighs' belongs here. \"\n             \"Nourai's gloss 'balance weight' fits tulā exactly; for tulya the precise sense is 'of equal weight, comparable', a natural derivative.\"),\n derivation_fa=(\"سنسکریت tulā «ترازو، کفهٔ ترازو، وزن» از پایهٔ ضعیف *tl̥h₂-éh₂ ریشهٔ هندواروپایی آغازین *telh₂- «برداشتن، وزن کردن، تحمل کردن» است؛ l هجایی پیش از همخوان حلقی در هندی باستان به ul بدل شده است. \"\n                \"tulya «هم‌وزن، همسنگ، همانند» صفتی است که با پسوند -ya از همین tulā ساخته شده و فعل tulayati «برمی‌دارد، می‌سنجد» نیز از همین ریشه است. \"\n                \"ادعای نورایی درست است (پوکورنی ۱۰۶۰، واتکینز، والده‌ـپوکورنی، کلاین، ویکی‌واژه).\"),\n sources=[W+\"तुला\", W+\"तुल्य\", W+\"Reconstruction:Proto-Indo-European/telh₂-\"],\n ref_check=[{\"ref\": \"POK:1060\", \"status\": \"supports\", \"note\": POK_Q},\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins AHD Roots s.v. telə- item 9: 'Suffixed zero-grade form *tl-ā- in Sanskrit tulā, scales, balance, weight: TAEL, TOLA.'\"}],\n consulted=[{\"src\": \"WLD\", \"where\": \"Bd. I p.738 s.v. 1. tel-\", \"stance\": \"supports\", \"note\": WLD_Q},\n            {\"src\": \"KLN\", \"where\": \"1966 s.v. tolerate / talent\", \"stance\": \"supports\", \"note\": KLN_TOL},\n            {\"src\": \"IEC\", \"where\": \"s.v. tl- (1) (IEC.txt line 18624)\", \"stance\": \"silent\", \"note\": \"Mann: 'tl- (1) ... lift, raise, bear, suffer'. WP I, 701 & 738-9' with Tocharian, Greek tlēmi, Latin tuli, Gothic þulan — Sanskrit tulā is not quoted under this head.\"}]\n))\n\nnodes.append(dict(\n id=2, lang=\"Avestan\", words=\"tara-âz, tara-âzu\", verdict=\"plausible\",\n derivation=(\"Nourai's 'tara-âz, tara-âzu' is the Old Iranian reconstruction proposed by Nyberg (Manual of Pahlavi II 191) and repeated by Mo'in (BQT p.480 fn.1) and Asbaghi (PLA 194): MP tarāzūg 'balance' < OIr *tarā-āzu-, from *tarā- 'scale, balance' (= Skt tulā, PIE *tl̥h₂-eh₂-, with the regular Iranian *ar from a syllabic liquid before a laryngeal) + *āz- 'to lead, drive' (Av. az-, Skt aj-, Lat agere), i.e. 'that which carries the scale-pans'. \"\n             \"The form is not attested in the Avestan corpus — Bartholomae's Altiranisches Wörterbuch has no tarāzu-/tara-āzu- — and Mo'in marks it with the asterisk-symbol as reconstructed 'Old Iranian' (ایرانی باستان), Asbaghi as 'air.'; so the box label 'Avestan' overstates the evidence (Wiktionary's Persian entry nonetheless writes an Avestan-script source form without an Avestan entry of its own). \"\n             \"The link to Sanskrit tulā/PIE *telh₂- is accepted; the second element *āz- is Nyberg's analysis and remains a hypothesis.\"),\n derivation_fa=(\"«tara-âz, tara-âzu» که نورایی آورده، صورت بازسازی‌شدهٔ ایرانی باستان است که نخست نیبرگ (راهنمای پهلوی، ج۲ ص۱۹۱) پیشنهاد کرده و معین در حاشیهٔ برهان قاطع (ص۴۸۰) و اسباغی (ص۱۹۴) تکرار کرده‌اند: پهلوی tarāzūg از ایرانی باستان *tarā-āzu-، مرکب از *tarā- «کفهٔ ترازو» (هم‌ریشه با سنسکریت tulā) و *āz- «راندن، بردن» (اوستایی az-، سنسکریت aj-، لاتین agere). \"\n                \"این صورت در متن‌های اوستایی گواهی نشده است و بارتولومه آن را ندارد؛ معین نیز آن را با نشانهٔ ستاره «ایرانی باستان» خوانده است، پس برچسب «اوستایی» در کتاب دقیق نیست. پیوند آن با ریشهٔ *telh₂- پذیرفته است، ولی جزء دوم (*āz-) فرضیهٔ نیبرگ است؛ ادعای نورایی با احتیاط پذیرفتنی است.\"),\n sources=[W+\"ترازو\"],\n ref_check=[{\"ref\": \"PLA:194\", \"status\": \"partial\", \"note\": PLA_Q}],\n consulted=[{\"src\": \"NYB\", \"where\": \"Part II p.191 s.v. tarāzūk\", \"stance\": \"supports\", \"note\": NYB_Q},\n            {\"src\": \"BRT\", \"where\": \"AiW, grep 'tara.?az', 'tarazu', 'taräzu' in BRT.txt\", \"stance\": \"silent\", \"note\": \"No Avestan tarā-, tarāzu- or tara-āzu- in Bartholomae (grep returned nothing) — the form is unattested in Avestan; Av. az- 'to drive' is itself well attested.\"},\n            {\"src\": \"BQT\", \"where\": \"vol.1 p.480 fn.1 s.v. ترازو\", \"stance\": \"partial\", \"note\": BQT480_Q + \" Same analysis, but labelled Old Iranian, not Avestan.\"}]\n))\n\nnodes.append(dict(\n id=3, lang=\"Persian\", words=\"tarâz; tarâzu\", verdict=\"disputed\",\n derivation=(\"tarāzū 'balance, scales' (ترازو) is secure: NP tarāzū < MP tarāzūg [tlʾcwk'] (Manichaean MP tlʾzwg) 'balance; Libra' (MacKenzie, Nyberg), < OIr *tarāzu- (see #2); Khwarezmian trʾzk; borrowed into Ottoman Turkish terazi and on into Balkan languages (Lokotsch no. 2029). Confirmed. \"\n             \"tarāz is a different matter. In the sense 'mason's level; balance (accounting)' (Mo'in senses 3, 5) it is plausibly a modern clipping/back-formation from the tarāzū family (cf. MP tarāzēnīdan 'to weigh'), though no historical source in our library documents it. \"\n             \"But the spelling طراز, the gloss 'nice' and Farrokhī's verse belong to other words: Persian tarāz/ṭirāz 'adornment, embroidered border' (Mo'in senses 1-2; Arabic ṭirāz is a loan from it, Asbaghi 194), which Wiktionary connects with tarāzīdan 'to adorn' and Arabic ṭarz < Persian darz 'seam', not with the balance; and in Farrokhī's line «شمسهٔ خوبان طراز» Ṭarāz is the Turkestan city (Talas), 'famed for its beauties' (BQT p.479 s.v. تراز: 'نام شهری است در ترکستان که منسوب است بخوبان'; Wiktionary: Taraz renowned in classical poetry for the beauty of its inhabitants). \"\n             \"So the arrow holds for tarāzū (and perhaps for tarāz 'level'), but the 'nice/طراز' sense and the illustrative quotation are unrelated to *telh₂-.\"),\n derivation_fa=(\"«ترازو» بی‌گمان از پهلوی tarāzūg (مانوی tlʾzwg) «ترازو؛ برج میزان» و آن از ایرانی باستان *tarāzu- است (مکنزی، نیبرگ، معین)؛ ترکی عثمانی terazi نیز از همین واژهٔ فارسی گرفته شده است. \"\n                \"اما «تراز/طراز» یک‌دست نیست: «تراز» به معنای ابزار بنّایی و ترازِ حساب احتمالاً برگرفته از خانوادهٔ «ترازو» است، ولی «طراز» به معنای زینت و نقش و نگار جامه واژهٔ دیگری است (عربی طِراز از همین فارسی وام گرفته شده) و ویکی‌واژه آن را با «ترازیدن/طرازیدن» و «درز» مربوط می‌داند. \"\n                \"در بیت فرخی «شمسهٔ خوبان طراز» هم طراز نام شهری در ترکستان (تلاس) است که به زیبارویان نامبردار بوده (برهان قاطع ص۴۷۹). پس پیوند «ترازو» با ریشهٔ *telh₂- درست است، اما معنای «زیبا/طراز» و شاهد شعری به این ریشه ربطی ندارند.\"),\n sources=[W+\"ترازو\", W+\"طراز\", W+\"طرز\", \"https://vajehyab.com/moein/تراز\"],\n ref_check=[{\"ref\": \"BQT:480\", \"status\": \"supports\", \"note\": BQT480_Q + \" Supports tarāzū; p.480 has no entry تراز. The adjoining p.479 (\" + BQT479_Q + \") gives تراز only as 'raw thread', 'pine' and the city Ṭarāz.\"}],\n consulted=[{\"src\": \"PHD\", \"where\": \"p.82 s.v. tarāzūg\", \"stance\": \"supports\", \"note\": PHD_Q},\n            {\"src\": \"NYB\", \"where\": \"Part II p.191 s.v. tarāzūk\", \"stance\": \"supports\", \"note\": NYB_Q},\n            {\"src\": \"BQT\", \"where\": \"vol.1 p.479 s.v. تراز\", \"stance\": \"contradicts\", \"note\": BQT479_Q + \" This contradicts reading Farrokhī's طراز as 'balanced, nice'.\"},\n            {\"src\": \"MON\", \"where\": \"vajehyab s.v. تراز\", \"stance\": \"partial\", \"note\": MON_TARAZ},\n            {\"src\": \"PLA\", \"where\": \"p.194 s.v. ṭirāz\", \"stance\": \"partial\", \"note\": \"Asbaghi separates ṭirāz 'Stickerei, Rand, Saum' < pers. tarāz, mp. taraz from ṭirāzdārān < pers. tarāzūdārān, mp. tarāzūk — two different Persian words.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 2029 (LKT.txt line 4563)\", \"stance\": \"supports\", \"note\": \"'2029. Pers. tärāzū: 'Wage', tk. ebenso terazi; hieraus serb. teresije, klruss. terezy, russ. tereza 'Wage'; rum. tirizie'.\"},\n            {\"src\": \"HRN\", \"where\": \"grep 'taraz', 'razu' in HRN.txt\", \"stance\": \"silent\", \"note\": \"Horn has no entry for tarāzū or tarāz.\"},\n            {\"src\": \"HUB\", \"where\": \"grep 'taraz', 'razu' in HUB.txt\", \"stance\": \"silent\", \"note\": \"Hübschmann has no entry for tarāzū or tarāz.\"},\n            {\"src\": \"ARY\", \"where\": \"grep ترازو / تراز in ARY_pages.txt and TARAZ in latin index\", \"stance\": \"silent\", \"note\": \"Aryanpur does not list ترازو under any root (no hit).\"}]\n))\n\nnodes.append(dict(\n id=4, lang=\"Greek\", words=\"a-tlâ; Atlas\", verdict=\"plausible\",\n derivation=(\"Greek Ἄτλας (gen. Ἄτλαντος), the Titan who holds up the sky (Hesiod, Theogony 517ff.), is traditionally analysed as copulative ἁ-/ἀ- (< PIE *sm̥- 'together, one') + the zero-grade stem τλα- of τλῆναι 'to bear, endure' (PIE *tl̥h₂-), with the -ant- suffix as in τάλας, -αντος — i.e. 'the Bearer (of heaven)'. This is Klein's, Pokorny's and Watkins' view ('perhaps zero-grade *tla- in Greek Atlas'). \"\n             \"'a-tlâ' is not an attested Greek word but Nourai's segmentation of the name; his gloss 'lift together' renders exactly this copulative-prefix analysis. \"\n             \"Modern caution: Beekes (EDG I 163) suggests the name may be Pre-Greek, and Wiktionary gives the IE derivation only as 'perhaps', so the derivation is widely repeated but not certain.\"),\n derivation_fa=(\"نام یونانی Ἄτλας (اطلس)، تیتانی که آسمان را بر دوش دارد، را معمولاً از پیشوند همراهی ἀ- (از *sm̥- «با هم، یک») و ستاک ضعیف τλα- از فعل τλῆναι «برداشتن، تاب آوردن» (از *tl̥h₂-) می‌دانند، یعنی «بَرنده (ی آسمان)». \"\n                \"«a-tlâ» واژه‌ای گواهی‌شده نیست، بلکه تجزیهٔ خودِ نورایی از این نام است و معنای «با هم برداشتن» همان تحلیل پیشوندی را بازمی‌گوید. \"\n                \"پوکورنی، واتکینز و کلاین این ریشه‌شناسی را می‌پذیرند، ولی بیکس احتمال می‌دهد نام از زبان پیشایونانی باشد؛ پس ادعای نورایی با احتیاط پذیرفتنی است.\"),\n sources=[W+\"Ἄτλας\", W+\"Reconstruction:Proto-Indo-European/telh₂-\"],\n ref_check=[{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins AHD Roots s.v. telə- item 6: 'Perhaps zero-grade form *tla- in Greek Atlas (stem Atlant-), name of the Titan supporting the world: ATLANTIC, ATLAS.' — note Watkins' own 'perhaps'.\"}],\n consulted=[{\"src\": \"KLN\", \"where\": \"1966 p.122 s.v. Atlas (KLN_1966.txt line 3850)\", \"stance\": \"supports\", \"note\": \"'Gk. Ἄτλας (gen. Ἄτλαντος), which stands for Ἀ-τλας and lit. means 'the Bearer (scil. of Heaven)', fr. copul. pref. ἀ- and the stem of τλῆναι, 'to bear' ... Copul. pref. ἀ- stands for I.-E. *sm-'.\"},\n            {\"src\": \"POK\", \"where\": \"IEW pp.1060-1061 s.v. tel-1\", \"stance\": \"supports\", \"note\": \"Pokorny lists the 'PN Ἄτλας, -αντος' among the Greek derivatives of tel-, tela- (POK_full.txt line ~85196).\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p.739 s.v. 1. tel-\", \"stance\": \"supports\", \"note\": \"'... πολύτλας „wer viel ausgestanden hat“, Ἄτλας, -αντος, τλήμων ...' under 1. tel- „aufheben ... tragen; ertragen“.\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. Atlas (SKT.txt line 1094)\", \"stance\": \"supports\", \"note\": \"'Gk. Ἄτλας (gen. Ἄτλαντος), prob. 'the sustainer' or bearer, from √TAL, to bear.'\"}]\n))\n\nnodes.append(dict(\n id=5, lang=\"Arabic\", words=\"\", verdict=\"plausible\",\n derivation=(\"Empty pass-through box: Arabic أطلس aṭlas as the intermediary between Greek Atlas and Persian اطلس. For the proper name Atlas, the Atlas mountains, 'atlas (map book)' and 'Atlantic' (al-muḥīṭ al-aṭlasī) this is right: Arabic aṭlas renders Greek Ἄτλας (Greek t > emphatic ṭ, as often in Greek loans), and the map-book sense is a modern borrowing from European atlas (Wiktionary, أطلس etym. 1-2). \"\n             \"But Arabic also has a native homonym aṭlas 'smooth, plain; worn, dark' from the root ṭ-l-s, which gives aṭlas 'satin' (Lokotsch no. 131: 'Ar. aṭlas: glatt, fein ... zur Bezeichnung des ... Seidensatins') and the astronomical al-falak al-aṭlas 'the plain (starless) ninth sphere'; those senses have nothing to do with the Greek Titan. The box is therefore correct for part of what passes through it.\"),\n derivation_fa=(\"این خانهٔ میانی عربی است: «أطلس» عربی به معنای نام اطلس، کوه‌های اطلس، کتاب نقشه و «المحیط الأطلسی» (اقیانوس اطلس) از یونانی Ἄτλας گرفته شده است (t یونانی در عربی به ط بدل شده) و معنای «کتاب نقشه» وام‌گیری تازه از زبان‌های اروپایی است. \"\n                \"اما در عربی واژهٔ هم‌آوای دیگری از ریشهٔ «ط ل س» به معنای «صاف، ساده، بی‌نقش» هست که «اطلس» به معنای پارچهٔ ابریشمی و «فلک اطلس» (فلک نهمِ بی‌ستاره) از آن آمده و به اطلس یونانی ربطی ندارد (لوکوچ ۱۳۱، ویکی‌واژه). پس این گذرگاه برای بخشی از معانی درست است.\"),\n sources=[W+\"أطلس\", W+\"اطلس\"],\n ref_check=[{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The Arabic box carries no reference of its own.\"}],\n consulted=[{\"src\": \"LKT\", \"where\": \"no. 131 (LKT.txt line 516)\", \"stance\": \"partial\", \"note\": \"'131. Ar. aṭlas: 'Glatt, fein' ... schließlich blieb das Adjektiv allein zur Bezeichnung des Stoffes ... des sog. Seidensatins' — native Arabic for the satin sense, not from Greek.\"},\n            {\"src\": \"KLN\", \"where\": \"1966 s.v. Atlantic (line 3849)\", \"stance\": \"silent\", \"note\": \"'L. Atlanticus, fr. Gk. Ἀτλαντικός, fr. Ἄτλας 'the Atlas mountains'' — no Arabic stage, which is expected for the English word.\"}]\n))\n\nnodes.append(dict(\n id=6, lang=\"Persian\", words=\"atlas; atlas; atlas\", verdict=\"disputed\",\n derivation=(\"Persian اطلس has several homonyms (Mo'in: '۱- پارچهٔ ابریشمی ۲- نام یکی از رب‌النوع‌های یونان ... ۳- اولین مهرهٔ گردن ۴- نقشهٔ جغرافی ۵- سطح مقعر فلک نهم ۶- نام اقیانوسی که بین اروپا و امریکا قرار دارد'). \"\n             \"atlas 2 'map book' (via Arabic or directly from European atlas, after Mercator's Atlas 1595) and atlas 3 'Atlantic ocean' (oqyānus-e atlas, Arabic al-muḥīṭ al-aṭlasī) do go back to Greek Ἄτλας — confirmed. \"\n             \"atlas 1 'world', however, can only reflect the astronomical sense falak-e atlas 'the ninth (starless, outermost) sphere', which is Arabic aṭlas 'plain, smooth, featureless' (root ṭ-l-s, the same word as aṭlas 'plain satin'), not the Greek Titan; Mo'in (BQT p.143) lumps all senses under 'از تازی، از یونانی Atlas', but Lokotsch and Wiktionary separate the native Arabic aṭlas. \"\n             \"The reference 'MON5:5155' printed in the book (and copied faithfully by the extraction) is evidently Nourai's slip for MON5:155 (vol. 5 = proper names; cf. MON5:8 for آتلانتیک).\"),\n derivation_fa=(\"«اطلس» در فارسی چند واژهٔ هم‌آواست (معین: پارچهٔ ابریشمی؛ نام ربّ‌النوع یونانی؛ نخستین مهرهٔ گردن؛ نقشهٔ جغرافی؛ سطح مقعر فلک نهم؛ اقیانوس میان اروپا و امریکا). \"\n                \"«اطلس» به معنای کتاب نقشه و «اقیانوس اطلس» به راستی از یونانی Ἄτلας (از راه عربی و زبان‌های اروپایی) آمده‌اند. ولی معنای «جهان» که نورایی برای «اطلس ۱» آورده جز «فلک اطلس» (فلک نهمِ بی‌ستاره) نیست و آن از صفت عربی «أطلس» به معنای «صاف و بی‌نقش» (ریشهٔ ط ل س، همان که پارچهٔ اطلس را نام داده) است، نه از نام تیتان یونانی. \"\n                \"معین در برهان همهٔ معانی را از یونانی دانسته، اما پژوهش امروزی (لوکوچ، ویکی‌واژه) این دو را جدا می‌کند. نشانی «MON5:5155» در کتاب هم ظاهراً خطای چاپی به جای ۱۵۵ است.\"),\n sources=[W+\"اطلس\", W+\"أطلس\", \"https://vajehyab.com/moein/اطلس\"],\n ref_check=[{\"ref\": \"BQT:143\", \"status\": \"partial\", \"note\": \"BQT vol.1 p.143 (archive.org borhan-ghate-v1 leaf n359, read from image; ocr/BQT/0143.vision.txt), Mo'in's added entry: '☼ اطلس - از تازی، از یونانی Atlas (نام ربّ‌النوع حامل کرهٔ زمین) «نفس». کتاب شامل نقشه‌های جغرافی - جامهٔ ابریشمی پرز دار.' Supports Greek > Arabic > Persian for the map sense; gives no 'world' sense and wrongly folds 'satin' into the Greek word.\"},\n            {\"ref\": \"MON5:5155\", \"status\": \"not_checked\", \"note\": \"Mo'in vol. 5 (a'lām) is not on disk or online with page numbers; '5155' is presumably a misprint for p.155. The lexicon entry (vajehyab) is quoted in consulted.\"}],\n consulted=[{\"src\": \"MON\", \"where\": \"vajehyab s.v. اطلس; MON_part1.txt line 14117\", \"stance\": \"partial\", \"note\": \"'اطلس: [معر.] پرنیان، دیبا، پارچهٔ ابریشمی ساده، بی‌پرز. (جان.) فقرهٔ اول از فقرات گردن ... (جغ.) کتاب مصور جغرافی ... (نج.) سطح مقعر فلک نهم. (اخ.) اقیانوس اطلس.' — the only 'world'-like sense is the ninth sphere.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 131\", \"stance\": \"contradicts\", \"note\": \"'Ar. aṭlas: 'Glatt, fein'' as the source of the satin word — a native Arabic adjective, the same that underlies falak-e aṭlas; contradicts a Greek origin for those senses.\"},\n            {\"src\": \"HRN\", \"where\": \"grep 'atlas' in HRN.txt\", \"stance\": \"silent\", \"note\": \"No entry (Horn excludes Arabic loans).\"},\n            {\"src\": \"ARY\", \"where\": \"grep اطلس in ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"No entry (Aryanpur covers inherited IE words only).\"}]\n))\n\nnodes.append(dict(\n id=7, lang=\"French\", words=\"\", verdict=\"confirmed\",\n derivation=(\"Empty pass-through box for French Atlantique (adj./noun, 'l'océan Atlantique'), from Latin Atlanticus < Greek Ἀτλαντικός 'of Atlas' (the sea beyond Mount Atlas, Herodotus 1.202 ἡ Ἀτλαντὶς θάλασσα). French was the main channel of European geographical vocabulary into Qajar/Pahlavi-era Persian, so the route is right.\"),\n derivation_fa=(\"خانهٔ میانی فرانسوی است: Atlantique فرانسوی از لاتین Atlanticus و آن از یونانی Ἀτλαντικός «منسوب به اطلس» (دریای آن سوی کوه اطلس) است. واژه‌های جغرافیایی اروپایی در دورهٔ قاجار و پهلوی بیشتر از راه فرانسه به فارسی رسیده‌اند؛ این گذرگاه درست است.\"),\n sources=[W+\"Atlantic\"],\n ref_check=[{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The French box carries no reference of its own.\"}],\n consulted=[{\"src\": \"KLN\", \"where\": \"1966 s.v. Atlantic (line 3849)\", \"stance\": \"supports\", \"note\": \"'Atlantic, adj., pertaining to the Atlantic Ocean or to Mount Atlas. — L. Atlanticus, fr. Gk. Ἀτλαντικός, fr. Ἄτλας, 'the Atlas mountains''.\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. Atlantic (line 1095)\", \"stance\": \"supports\", \"note\": \"'Atlantic, an ocean, named after Mt. Atlas, in the N.W. of Africa; from the form Ἀτλαντ-'.\"}]\n))\n\nnodes.append(dict(\n id=8, lang=\"Persian\", words=\"Âtlântîk\", verdict=\"confirmed\",\n derivation=(\"Persian آتلانتیک ātlāntīk is a modern borrowing of French atlantique (French -ique regularly rendered -īk in Persian, as in politik, klasik), used beside the older oqyānus-e atlas. Nourai's gloss '(ocean) by the Atlas mountain' is the etymological meaning of Greek Ἀτλαντικός, correct. \"\n             \"The cited MON5:8 (Mo'in's a'lām volume) is not available to check, but the borrowing route is uncontroversial.\"),\n derivation_fa=(\"«آتلانتیک» وام‌واژه‌ای نو از فرانسوی atlantique است (پایانهٔ -ique فرانسوی در فارسی به «-یک» بدل می‌شود، مانند پولیتیک و کلاسیک) و در کنار «اقیانوس اطلس» به کار می‌رود. معنای «(دریای) کنار کوه اطلس» همان معنای ریشه‌ای یونانی Ἀτλαντικός است. ادعای نورایی درست است.\"),\n sources=[W+\"Atlantic\", W+\"اطلس\"],\n ref_check=[{\"ref\": \"MON5:8\", \"status\": \"not_checked\", \"note\": \"Mo'in vol. 5 (proper names) not on disk; vajehyab has no entry آتلانتیک (404).\"}],\n consulted=[{\"src\": \"MON\", \"where\": \"MON_part1.txt line 14117 s.v. اطلس\", \"stance\": \"partial\", \"note\": \"'(اخ.) اقیانوس اطلس' — Mo'in's lexicon knows the ocean under atlas; no separate آتلانتیک in the lexicon volumes (grep آتلانتیک in MON files: no hit).\"},\n            {\"src\": \"KLN\", \"where\": \"1966 s.v. Atlantic\", \"stance\": \"supports\", \"note\": \"'L. Atlanticus, fr. Gk. Ἀτλαντικός, fr. Ἄτλας' — the European source form of the Persian loan.\"}]\n))\n\nnodes.append(dict(\n id=9, lang=\"English\", words=\"atlas 1; Atlantic\", verdict=\"confirmed\",\n derivation=(\"English atlas (1636 in the map-book sense) comes from Mercator's Atlas sive cosmographicae meditationes (1585/1595), named after the Titan Atlas (Latin Atlas < Greek Ἄτλας); the anatomical atlas (first vertebra) is a separate application. \"\n             \"Atlantic: Middle English Atlantyke < Latin Atlanticus < Greek Ἀτλαντικός 'of Atlas', first of the sea beyond the Atlas mountains. Both are correctly derived from #4. (English atlas 'satin', from Arabic aṭlas, is a different word, not in the chart.)\"),\n derivation_fa=(\"«atlas» انگلیسی به معنای کتاب نقشه از عنوان کتاب مرکاتور (۱۵۸۵/۱۵۹۵) آمده که به نام تیتان اطلس (لاتین Atlas از یونانی Ἄτλας) نامیده شده بود؛ «Atlantic» از انگلیسی میانه Atlantyke، از لاتین Atlanticus و یونانی Ἀτλαντικός «منسوب به اطلس» است. هر دو به‌درستی از گرهٔ یونانی گرفته شده‌اند. ادعای نورایی درست است.\"),\n sources=[W+\"atlas\", W+\"Atlantic\"],\n ref_check=[{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins AHD Roots s.v. telə- item 6: '... Greek Atlas (stem Atlant-), name of the Titan supporting the world: ATLANTIC, ATLAS.'\"}],\n consulted=[{\"src\": \"KLN\", \"where\": \"1966 s.v. atlas (line 3851)\", \"stance\": \"supports\", \"note\": \"'atlas, n., a collection of maps bound into a book. — First so called by the geographer Mercator because the figure of Atlas supporting the world was frequently put on the front page of such collections. (The first part of Mercator's Atlas ... appeared in 1585.)'\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. Atlas, Atlantic (lines 1094-1095)\", \"stance\": \"supports\", \"note\": \"'Atlas. (Gk.) Named after Atlas, the demi-god who was said to bear the world on his shoulders; his figure used often to appear on the title-page of atlases.'\"}]\n))\n\nnodes.append(dict(\n id=10, lang=\"Greek\", words=\"telos; talanton\", verdict=\"confirmed\",\n derivation=(\"τάλαντον 'pair of scales; a weight; a talent (sum of money)' < Proto-Greek *tálanton < PIE *tl̥h₂-ent- (zero grade of *telh₂-, the laryngeal colouring the vowel to a), originally neuter plural τάλαντα 'the two scale-pans' (Beekes EDG 1445, Pokorny, Watkins). \"\n             \"τέλος in the sense 'payment, tax, toll, charge' (cf. ἀτελής 'tax-free', τελώνης 'tax-collector') is the s-stem *télh₂-es- 'what is borne/paid' of the same root; Greek τέλος is a merger of this word with τέλος 'end, goal' from *kʷel- 'turn' (Beekes; Wiktionary), and only the 'tax' sense — the one Nourai glosses — belongs here.\"),\n derivation_fa=(\"یونانی τάλαντον «ترازو، وزنه، تالان (مقداری زر و سیم)» از *tl̥h₂-ent-، پایهٔ ضعیف ریشهٔ *telh₂- است و در اصل جمعِ τάλαντα یعنی «دو کفهٔ ترازو» بوده است. \"\n                \"τέλος به معنای «باج، مالیات، عوارض» از ستاک *télh₂-es- «آنچه پرداخته/حمل می‌شود» از همین ریشه است؛ τέλος به معنای «پایان، غایت» از ریشهٔ دیگری (*kʷel- «گشتن») است و در یونانی با آن یکی شده، ولی معنایی که نورایی آورده (باج) از همین ریشه است. ادعای نورایی درست است (پوکورنی، واتکینز، بیکس).\"),\n sources=[W+\"τάλαντον\", W+\"τέλος\", W+\"Reconstruction:Proto-Indo-European/telh₂-\"],\n ref_check=[{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins AHD Roots s.v. telə-: '2. Suffixed form *tel(ə)-es- in: a. Greek telos, tax, charge: TOLL1; PHILATELY' and '4. Suffixed variant zero-grade form *tala-nt- in Greek talanton, balance, weight, any of several specific weights of gold or silver ...: TALENT.'\"}],\n consulted=[{\"src\": \"POK\", \"where\": \"IEW pp.1060-1061\", \"stance\": \"supports\", \"note\": \"'τάλαντον (originally to τάλας, n. τάλαν gehöriger Pl. τάλαντα (actually 'die beiden Waagschalen') 'scales; a certain weight''; 'τέλος n. 'payment, tribute, tax, Ausgabe, Kosten', εὐτελής 'cheap', ἀτελής 'frei from tributes''.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p.739\", \"stance\": \"supports\", \"note\": \"'τάλαντον (ursprgl. zu τάλας ... Pl. τάλαντα eig. „die beiden Waagschalen“ ...) „Waage; ein bestimmtes Gewicht“'.\"},\n            {\"src\": \"IEC\", \"where\": \"s.v. tl- (2) (line 18625)\", \"stance\": \"partial\", \"note\": \"Mann puts 'Gk. cf. tálanton (a weight, but in sense of 'scale, balance'? cf. tl- (1))' under a separate tl- (2) 'make so, estimate', while allowing the link with tl- (1) 'lift, bear'.\"},\n            {\"src\": \"KLN\", \"where\": \"1966 s.v. talent / toll\", \"stance\": \"supports\", \"note\": \"talent: 'Gk. τάλαντον 'balance' (in the pl. 'pair of scales'); a weight ... fr. I.-E. base *tel-, *tal-, *tol- 'to bear, carry'' ; toll: 'Gk. τέλος 'tax' ... which is cogn. with ταλάσσαι (aor.) 'to bear, support''.\"}]\n))\n\nnodes.append(dict(\n id=11, lang=\"English\", words=\"toll; talent\", verdict=\"plausible\",\n derivation=(\"talent: Old English talente < Latin talenta, pl. of talentum < Greek τάλαντον (a weight/sum of money); the sense 'natural ability' comes via Old French talent from the Parable of the Talents (Matthew 25) — confirmed. \"\n             \"toll 'tax, charge': OE toll/toln, cognate with OHG zol, ON tollr. Klein (and Watkins) derive the whole West/North Germanic group from Late Latin toloneum, telōneum < Greek τελώνιον 'toll-house' < τελώνης < τέλος 'tax', i.e. from *telh₂-; but Wiktionary prefers a native Germanic *tullaz/*tullō 'that which is counted' from PIE *del- 'count' (cf. tell, tale), mentioning the Latin route only as an alternative. \"\n             \"So toll's descent from τέλος is a respected but contested view; the node is plausible.\"),\n derivation_fa=(\"«talent» انگلیسی از انگلیسی باستان talente، از لاتین talentum و یونانی τάλαντον است و معنای «استعداد» از تمثیل «قنطارها» در انجیل متی آمده است؛ این بخش درست است. \"\n                \"«toll» (عوارض، باج) را کلاین و واتکینز از لاتین متأخر toloneum/telōneum و یونانی τελώνιον «گمرک‌خانه» از τέλος «باج» می‌دانند، ولی ویکی‌واژه آن را واژه‌ای بومی ژرمنی (*tullaz «شمرده‌شده») از ریشهٔ *del- «شمردن» (هم‌ریشه با tell و tale) می‌شمارد. پس پیوند toll با τέλος پذیرفتنی ولی مورد اختلاف است.\"),\n sources=[W+\"toll\", W+\"talent\"],\n ref_check=[{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The English box carries no reference; the parent's AHD citation (telə- 2a 'TOLL1', 4 'TALENT') supports both words.\"}],\n consulted=[{\"src\": \"KLN\", \"where\": \"1966 s.v. toll (line 39461), talent (line 38043)\", \"stance\": \"supports\", \"note\": \"toll: 'ME. tol, fr. OE. toll, rel. to OS. tolna, ON. tollr ... OHG. zol ... borrowed fr. Late L. toloneum, 'custom house' ... fr. earlier telonium, fr. Gk. τελωνεῖον 'toll house', fr. τελώνης 'tax collector', fr. τέλος 'tax''.\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. Talent (line 19106), Toll\", \"stance\": \"supports\", \"note\": \"Talent: 'L. talentum — Gk. τάλαντον, a balance, weight, sum of money. Named from being lifted and weighed; cf. Skt. tul, L. tollere, to lift'.\"}]\n))\n\nnodes.append(dict(\n id=12, lang=\"Latin\", words=\"tolĕre; lâtus; trans-latŭs\", verdict=\"confirmed\",\n derivation=(\"Latin tollō, tollere 'to lift, raise; carry off' < *tl̥-n-h₂- (nasal present of *telh₂-, *tl̥nā- > *tolnō > tollō by assimilation); tolerāre 'to bear, endure' is from the same root. \"\n             \"lātus 'borne, carried' < Old Latin tlātus < *tl̥h₂-tó- (initial tl- simplified to l-), used as the suppletive perfect participle of ferre 'to carry' (perfect tulī, old tetulī, also from this root); trānslātus 'carried across' = trāns + lātus, participle of trānsferre, whence 'translated'. \"\n             \"Nourai's 'tolĕre' is his rendering of the infinitive tollere (with the short ĕ marked); the forms and glosses are right.\"),\n derivation_fa=(\"لاتین tollere «برداشتن، بالا بردن» از حال نازالیِ *tl̥-n-h₂- ریشهٔ *telh₂- است و tolerāre «تحمل کردن» هم از همین ریشه است. \"\n                \"lātus «بُرده‌شده» از لاتین کهن tlātus و آن از *tl̥h₂-tó- است (tl- آغازین به l- ساده شده) و به‌عنوان صفت مفعولی فعل ferre «بردن» به کار می‌رود؛ trānslātus «آن سو بُرده‌شده، ترجمه‌شده» از trāns + lātus است. «tolĕre» نورایی همان tollere است. ادعای نورایی درست است.\"),\n sources=[W+\"translate\", W+\"tolerate\", W+\"Reconstruction:Proto-Indo-European/telh₂-\"],\n ref_check=[{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins AHD Roots s.v. telə-: '8. Suffixed zero-grade form *tl-to- in Latin lātus, 'carried, borne,' used as the suppletive past participle of ferre ...: ... RELATE, ... TRANSLATE' and '10. Nasalized zero-grade form *tl-n-a- in Latin tollere, to lift: EXTOL.'\"}],\n consulted=[{\"src\": \"POK\", \"where\": \"IEW p.1061\", \"stance\": \"supports\", \"note\": \"'Latin tollo, -ere (sustulī, sublātum) 'empor, in die Höhe heben' (*tlnō, transfigured from *tl-na-mi) ... tolero, -are '(er)trage', tulī, old tetulī ... lātus 'getragen' (= gr. τλητός, cymr. tlawd)'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p.739\", \"stance\": \"supports\", \"note\": \"'tolero „trage, ertrage, unterhalte“, tulī ...' and lātus under 1. tel-.\"},\n            {\"src\": \"IEC\", \"where\": \"s.v. tlātos (line 18623)\", \"stance\": \"supports\", \"note\": \"'tlātos ... 'suffered, borne; suffering'. WP I, 738. ... Lat. lātus, adj. 'borne, carried''.\"},\n            {\"src\": \"KLN\", \"where\": \"1966 s.v. translate (line 39861)\", \"stance\": \"supports\", \"note\": \"'L. translatus 'carried over' (used as pp. of transferre) ... latus 'borne, carried' ... which stands for *tlatos, fr. *tl-, zero degree of I.-E. base *tel-, *tol- 'to bear, carry', whence L. tollere'.\"}]\n))\n\nnodes.append(dict(\n id=13, lang=\"English\", words=\"tolerate; relate; translate\", verdict=\"confirmed\",\n derivation=(\"tolerate (1530s) < Latin tolerātus, pp. of tolerāre 'to bear, endure'; relate (late 15th c.) < Latin relātus, pp. of referre 'to carry back, report' (re- + lātus); translate (c.1300, ME translaten) < Anglo-Norman translater < Latin trānslātus, pp. of trānsferre 'to carry across'. \"\n             \"All three continue the Latin forms in #12 and thus PIE *telh₂-, as Watkins, Klein and Wiktionary all state.\"),\n derivation_fa=(\"انگلیسی tolerate از لاتین tolerātus (صفت مفعولی tolerāre «تحمل کردن»)، relate از relātus (صفت مفعولی referre «بازبردن، گزارش کردن») و translate از انگلیسی میانه translaten، از آنگلونورمن translater و لاتین trānslātus «آن سو بُرده» است. هر سه از صورت‌های لاتین گرهٔ پیشین و در نهایت از ریشهٔ *telh₂- آمده‌اند. ادعای نورایی درست است.\"),\n sources=[W+\"tolerate\", W+\"relate\", W+\"translate\"],\n ref_check=[{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The English box carries no reference; the parent's AHD citation (telə- 2b TOLERATE, 8 RELATE, TRANSLATE) supports all three.\"}],\n consulted=[{\"src\": \"KLN\", \"where\": \"1966 s.v. tolerate (line 39457), translate (line 39861)\", \"stance\": \"supports\", \"note\": \"tolerate: 'L. toleratus, pp. of tolerare, 'to bear, support, endure, tolerate', from the stem of tollere' ... 'Cp. ... relate, relation, ... translate, translation'.\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. Tolerate (line 19805ff.)\", \"stance\": \"supports\", \"note\": \"Skeat groups under tolerate/√TAL the Latin latus derivatives: 'relate ... L. relatum, used as pp. of referre ... latus, borne, pp. of tollere, to bear' and translate.\"}]\n))\n\nentry = dict(\n entry=0, root=\"Tel\", verdict=\"confirmed\",\n modern_form=\"PIE *telh₂- 'to lift, bear, weigh; endure' (Pokorny 1. tel-, telə-, tlē-, tlā- 1060-1061; Watkins/AHD telə-; LIV² 622-623)\",\n note=(\"Pokorny IEW pp.1060-1061 heads the entry '1. tel-, telə-, tle(i)-, tlā-' 'to transport, carry; to bear, suffer', Watkins (AHD) 'telə- to lift, support, weigh', modern notation *telh₂-. Nourai's 'Tel : to lift', the label Indo-European and both his citations (POK:1060; KLN:122 = Klein s.v. Atlas, which spells out the base *tel-, *tal-, *tol- 'to bear, lift, suffer') are correct. \"\n       \"The Greek, Latin, Sanskrit and English branches are standard (Pokorny, Walde-Pokorny, Watkins, Klein all list them). Two Iranian/Persian problems: (1) the 'Avestan' tara-āz(u) is Nyberg's reconstructed Old Iranian *tarā-āzu-, not an attested Avestan word; (2) the Persian tarāz/طراز box mixes tarāzū 'balance' (correct) with ṭarāz/tarāz 'adornment' and the city Ṭarāz of Farrokhī's verse, and the Persian atlas 'world' (falak-e atlas) is native Arabic aṭlas 'plain, smooth', not Greek Atlas. Toll's Greek origin is contested (Wiktionary prefers a native Germanic word). \"\n       \"No extraction errors: the JSON matches the printed page, including the odd ref 'MON5:5155' (a misprint in the book, presumably for MON5:155).\"),\n note_fa=(\"ریشهٔ هندواروپایی آغازین *telh₂- «برداشتن، بردن، سنجیدن؛ تاب آوردن» است؛ پوکورنی (ص۱۰۶۰–۱۰۶۱) آن را «tel-، telə-، tlā-» با معنای «بردن، حمل کردن؛ تحمل کردن» و واتکینز «telə- برداشتن، نگه داشتن، وزن کردن» آورده‌اند. «Tel: برداشتن» نورایی، برچسب «هندواروپایی» و هر دو مأخذ او (پوکورنی ۱۰۶۰ و کلاین ۱۲۲ ذیل Atlas) درست است. \"\n          \"شاخه‌های یونانی، لاتین، سنسکریت و انگلیسی همه پذیرفته‌اند. اشکال‌ها در بخش ایرانی است: «tara-âz» اوستایی نیست بلکه بازسازی ایرانی باستانِ نیبرگ است؛ در خانهٔ فارسی «ترازو» درست است ولی «طراز» (زینت، و شهر طراز در بیت فرخی) واژهٔ دیگری است؛ و «اطلس» به معنای «فلک اطلس/جهان» از صفت عربی «أطلس» (صاف، بی‌نقش) است نه از تیتان یونانی. خطای استخراج دیده نشد.\"),\n sources=[W+\"Reconstruction:Proto-Indo-European/telh₂-\", W+\"Ἄτλας\", W+\"τάλαντον\"],\n ref_check=[{\"ref\": \"POK:1060\", \"status\": \"supports\", \"note\": POK_Q},\n            {\"ref\": \"KLN:122\", \"status\": \"supports\", \"note\": \"Klein 1966 (KLN_1966.txt leaf ~75, two pages per leaf ≈ pp.126-127 by the offset formula; the Atlas entry is the one Nourai means) s.v. Atlas: 'Gk. τλῆναι derives fr. *tl-, zero degree of I.-E. base *tel-, *tal-, *tol-, 'to bear, lift, suffer', whence τάλας ... τάλαντον, ... L. tollere 'to lift up, raise', tolerare 'to bear, support''.\"}],\n consulted=[{\"src\": \"WLD\", \"where\": \"Bd. I pp.738-740 s.v. 1. tel-\", \"stance\": \"supports\", \"note\": WLD_Q},\n            {\"src\": \"AHD\", \"where\": \"Watkins s.v. telə-\", \"stance\": \"supports\", \"note\": AHD_Q},\n            {\"src\": \"IEC\", \"where\": \"s.v. tl- (1) (line 18624)\", \"stance\": \"supports\", \"note\": \"'tl- (1) (tlō, tolō, iō) 'lift, raise, bear, suffer'. WP I, 701 & 738-9 ... Tokh. A B tal-, v. 'lift, carry'; Gk. tlēmi, aor. etlēn 'bear, support, suffer'; Lat. perf. (te)tulī; Go. þulan'.\"},\n            {\"src\": \"SYN\", \"where\": \"not searched in detail\", \"stance\": \"silent\", \"note\": \"Buck's synonym dictionary treats 'lift', 'bear', 'tax' sections; grep for tel-/tulā gave no direct root discussion beyond Pokorny's data.\"}],\n nodes=nodes,\n)\n\nout = dict(pdf_page=499, book_page=469, verified_by=\"claude-opus-5\", verified_on=\"2026-10-14\", entries=[entry])\njson.dump(out, open(\"/home/sfmqrb/git/rishe-private/data/verification/page-499.json\", \"w\", encoding=\"utf-8\"), ensure_ascii=False, indent=1)\nprint(\"ok\")\n"
}
```


### [2026-10-15T02:33:34.091Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/gen-499.py (file state is current in your context — no need to Read it back)
```


## [2026-10-15T02:33:42.524Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; python3 - <<'EOF'\np='gen-499.py'; s=open(p).read()\ns=s.replace(\"Ἄτلας\",\"Ἄτλας\")\ns=s.replace(\"'; index p.? lists 'tulā: tarāzūk'.\\\")\",\"'; the Sanskrit index of the same volume lists 'tulā: tarāzūk'.\\\")\")\ns=s.replace('\"where\": \"p.82 s.v. tarāzūg\"','\"where\": \"s.v. tarāzūg (PHD_mackenzie.txt line 4927)\"')\ns=s.replace(\"leaf ~75, two pages per leaf ≈ pp.126-127 by the offset formula; the Atlas entry is the one Nourai means\",\"leaf 75 = c. pp.122-127 by the two-pages-per-leaf offset; the Atlas entry is the one Nourai means\")\ni=s.index('            {\"src\": \"SYN\"'); j=s.index('\\n', s.index('beyond Pokorny', i))\ns=s[:i].rstrip().rstrip(',')+s[j:]\nopen(p,'w').write(s)\nEOF\ngrep -c 'Ἄτلας' gen-499.py; python3 gen-499.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-499.json >/dev/null && echo valid; python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 499"
}
```


### [2026-10-15T02:33:43.042Z] TOOL RESULT

```
0
  File "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/gen-499.py", line 223
    )
    ^
SyntaxError: closing parenthesis ')' does not match opening parenthesis '[' on line 219
nodes verified: 0/13
node verdicts: {}
root verdicts: {}
ref checks: {}
books consulted: {} | by book: {}
pages without verification (1): 499
```


## [2026-10-15T02:33:45.490Z] TOOL CALL #60: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/gen-499.py",
 "offset": 214,
 "limit": 12
}
```


### [2026-10-15T02:33:45.508Z] TOOL RESULT

```
214	 note_fa=("ریشهٔ هندواروپایی آغازین *telh₂- «برداشتن، بردن، سنجیدن؛ تاب آوردن» است؛ پوکورنی (ص۱۰۶۰–۱۰۶۱) آن را «tel-، telə-، tlā-» با معنای «بردن، حمل کردن؛ تحمل کردن» و واتکینز «telə- برداشتن، نگه داشتن، وزن کردن» آورده‌اند. «Tel: برداشتن» نورایی، برچسب «هندواروپایی» و هر دو مأخذ او (پوکورنی ۱۰۶۰ و کلاین ۱۲۲ ذیل Atlas) درست است. "
215	          "شاخه‌های یونانی، لاتین، سنسکریت و انگلیسی همه پذیرفته‌اند. اشکال‌ها در بخش ایرانی است: «tara-âz» اوستایی نیست بلکه بازسازی ایرانی باستانِ نیبرگ است؛ در خانهٔ فارسی «ترازو» درست است ولی «طراز» (زینت، و شهر طراز در بیت فرخی) واژهٔ دیگری است؛ و «اطلس» به معنای «فلک اطلس/جهان» از صفت عربی «أطلس» (صاف، بی‌نقش) است نه از تیتان یونانی. خطای استخراج دیده نشد."),
216	 sources=[W+"Reconstruction:Proto-Indo-European/telh₂-", W+"Ἄτλας", W+"τάλαντον"],
217	 ref_check=[{"ref": "POK:1060", "status": "supports", "note": POK_Q},
218	            {"ref": "KLN:122", "status": "supports", "note": "Klein 1966 (KLN_1966.txt leaf 75 = c. pp.122-127 by the two-pages-per-leaf offset; the Atlas entry is the one Nourai means) s.v. Atlas: 'Gk. τλῆναι derives fr. *tl-, zero degree of I.-E. base *tel-, *tal-, *tol-, 'to bear, lift, suffer', whence τάλας ... τάλαντον, ... L. tollere 'to lift up, raise', tolerare 'to bear, support''."}],
219	 consulted=[{"src": "WLD", "where": "Bd. I pp.738-740 s.v. 1. tel-", "stance": "supports", "note": WLD_Q},
220	            {"src": "AHD", "where": "Watkins s.v. telə-", "stance": "supports", "note": AHD_Q},
221	            {"src": "IEC", "where": "s.v. tl- (1) (line 18624)", "stance": "supports", "note": "'tl- (1) (tlō, tolō, iō) 'lift, raise, bear, suffer'. WP I, 701 & 738-9 ... Tokh. A B tal-, v. 'lift, carry'; Gk. tlēmi, aor. etlēn 'bear, support, suffer'; Lat. perf. (te)tulī; Go. þulan'."}
222	 nodes=nodes,
223	)
224	
225	out = dict(pdf_page=499, book_page=469, verified_by="claude-opus-5", verified_on="2026-10-14", entries=[entry])
```


## [2026-10-15T02:33:48.582Z] TOOL CALL #61: Edit

```json
{
 "replace_all": false,
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/gen-499.py",
 "old_string": "Go. þulan'.\"}\n nodes=nodes,",
 "new_string": "Go. þulan'.\"}],\n nodes=nodes,"
}
```


### [2026-10-15T02:33:48.614Z] TOOL RESULT

```
The file /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/gen-499.py has been updated successfully.
```


## [2026-10-15T02:33:49.970Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; python3 gen-499.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-499.json >/dev/null && echo valid; python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 499"
}
```


### [2026-10-15T02:33:50.622Z] TOOL RESULT

```
ok
valid
nodes verified: 13/13
node verdicts: {'confirmed': 7, 'plausible': 4, 'disputed': 2}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 7, 'partial': 2, 'not_checked': 6}
books consulted: {'supports': 26, 'silent': 8, 'partial': 7, 'contradicts': 2} | by book: {'KLN': 10, 'SKT': 5, 'WLD': 4, 'IEC': 3, 'MON': 3, 'LKT': 3, 'POK': 3, 'NYB': 2, 'BQT': 2, 'HRN': 2, 'ARY': 2, 'BRT': 1, 'PHD': 1, 'PLA': 1, 'HUB': 1}
```


## [2026-10-15T02:34:01.365Z] TOOL CALL #63: SubagentHandback

```json
{
 "message": "Page 499 (book p. 469) is verified: one entry, root \"Tel\", 13 nodes. `verify_check.py 499` shows no PROBLEM lines and the JSON is valid.\n\n**Verdicts:**\n- **Root:** confirmed. Nourai's \"Tel : to lift\" is PIE *telh₂- \"lift, bear, weigh\". This matches Pokorny 1060–61 and Watkins (AHD telə-). His Klein citation, KLN:122, is Klein's Atlas entry.\n- **Nodes:** 7 confirmed, 4 plausible, 2 disputed, 0 transcription_suspect.\n\n**Disputed:**\n- **#3 Persian tarâz / tarâzu (تراز، طراز / ترازو):**\n  - tarāzū is fine: it comes from Middle Persian tarāzūg.\n  - The طراز spelling and the gloss \"nice\" belong to a different word, tarāz/ṭirāz \"adornment, embroidery\".\n  - In Farrokhī's quoted verse, «شمسهٔ خوبان طراز» names Ṭarāz, the Turkestan city (Talas) famous for its beauties. Borhan-e Qate' p. 479 says this, and so does Wiktionary.\n- **#6 Persian atlas «اطلس ۱» \"world\":**\n  - The only sense close to \"world\" is falak-e atlas, the starless ninth sphere.\n  - That sense comes from the native Arabic adjective aṭlas \"plain, smooth\" (root ṭ-l-s), which also gives \"satin\". It does not come from the Greek Titan Atlas (Lokotsch no. 131, Wiktionary).\n  - The \"map\" and \"Atlantic\" senses do come from Greek Atlas and are fine.\n\n**Other notes:**\n- **#2 \"Avestan\" tara-âz, tara-âzu (plausible):** this is Nyberg's reconstructed Old Iranian *tarā-āzu-, not an attested Avestan word. Bartholomae does not have it. Mo'in (Borhan p. 480 footnote) and Asbaghi (PLA 194) both label it Old Iranian.\n- **#11 English toll (plausible):** Klein and Watkins derive it from Greek telos via Late Latin teloneum. Wiktionary prefers a native Germanic *tullō.\n- The book's reference \"MON5:5155\" in node #6 looks like Nourai's misprint for MON5:155.\n\n**Extraction errors:** none. The JSON matches the printed page, including that odd reference.\n\n**Housekeeping:**\n- The cached `ocr/PLA/0194.*` held the wrong scan page: the PDF has a 15-page offset, so printed p. 194 is PDF page 209. I deleted it and regenerated it with `--pdf-page 209`.\n- I saved images and transcriptions for Borhan pages 143, 479 and 480 under `data/verification/sources/refs/ocr/BQT/` (`0143`, `0479`, `0480` .jpg and .vision.txt).\n- I archived 20 web pages (Wiktionary and vajehyab) with `fetch_source.py`. Etymonline was blocked by Cloudflare, so it is not cited.\n\nOutput: `/home/sfmqrb/git/rishe-private/data/verification/page-499.json`"
}
```


### [2026-10-15T02:34:01.852Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
