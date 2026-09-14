# Verification process log — verify-page-460


## [2026-09-14T02:27:32.226Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 460 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-460.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-460.json. Write /home/sfmqrb/git/rishe/data/verification/page-460.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 460` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T02:27:33.367Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T02:27:34.276Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T02:27:34.296Z] TOOL RESULT

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


## [2026-09-14T02:27:34.775Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-460.txt"
}
```


### [2026-09-14T02:27:34.796Z] TOOL RESULT

```
1	=== PDF page 460 (book page 430) ===
2	--- entry 0 ---
3	ROOT [Semitic] S.m.`a : to hear, listen  (refs KLN:1434)
4	#1 (parent #0) [Arabic] refs=KLN:1434 | samî`a : he heard
5	  #2 (parent #1) [Persian] refs=MON; FVA:197 | sam`a «سَمع» : hearing | extra: سَماع، سَميع، اِستِماع، مُستَمِع، سامِع
6	#3 (parent #0) [Hebrew] refs=KLN:817,1434 | shâma` : he heard ; shema` : sound, a prayer ; Yishma`-ěl : God hears ☞Layh
7	  #4 (parent #3) [Arabic] refs=KLN:817 | Ismâ`îl : "God hears", name of son of Abraham
8	    #5 (parent #4) [Persian] refs=MON | Esmâ`îl «اسماعیل» : "God hears", a male name, son of Abraham
9	  #6 (parent #3) [Persian] refs=MON | Šam`ŭn «شمعون» : Shimeon, Simeon, a follower of Jesus
10	  #7 (parent #3) [English] refs=KLN | Shema ; Simon ; Simeon ; Shimeon ; Ishmael
11	--- entry 1 ---
12	ROOT [Indo-European] Smeit : to throw, send forward  (refs POK:968)
13	#1 (parent #0) [Avestan] refs=POK:968; KLN:988 | maěth : to send, throw ; hamista : thrown down, put down ; hamaěstar : one who throws down, enemy
14	  #2 (parent #1) [Pahlavi] refs=SNS:53 | haměstâr : enemy ; haměstagân : awkward situation
15	    #3 (parent #2) [Persian] refs=HRN:279; MON:5185 | hamîstar «همیستر» : enemy ; hamîstakân «همیستکان» : a place between hell and heaven | NOTE: Almost obsolete words.
16	#4 (parent #0) [Latin] refs=AHD | mithere : to send off
17	  #5 (parent #4) [French] refs=AHD | 
18	    #6 (parent #5) [Persian] refs=MON:3079 | komîsîyon «کمیسیون» : commission | extra: کمیته
19	    #7 (parent #5) [English] refs=AHD; KLN:988 | commit ; emit ; omit ; remit ; submit ; admit ; permit ; transmit ; mission ; commission ; committee ; missile ; promise
20	--- entry 2 ---
21	ROOT Smelo -> redirect to Mel 2
22	--- entry 3 ---
23	ROOT Smer -> redirect to Mer 1
24	
```


## [2026-09-14T02:27:37.687Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-460.json",
 "description": "Read source JSON for page 460"
}
```


### [2026-09-14T02:27:37.734Z] TOOL RESULT

```
{
  "pdf_page": 460,
  "book_page": 430,
  "entries": [
    {
      "root": {
        "name": "S.m.`a",
        "lang": "Semitic",
        "refs": "KLN:1434",
        "gloss": "to hear, listen"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "KLN:1434",
          "words": [
            {"translit": "samî`a", "gloss": "he heard", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "MON; FVA:197",
          "words": [
            {"translit": "sam`a", "gloss": "hearing", "script": "سَمع"}
          ],
          "script_extra": "سَماع، سَميع، اِستِماع، مُستَمِع، سامِع",
          "note": null,
          "quote": {
            "text": "بشنو سماع آسمان ، خیزید ای دیوانگان - جانم فدای عاشقان امروز جان افشان کنیم",
            "poet": "Molavî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Hebrew",
          "refs": "KLN:817,1434",
          "words": [
            {"translit": "shâma`", "gloss": "he heard", "script": null},
            {"translit": "shema`", "gloss": "sound, a prayer", "script": null},
            {"translit": "Yishma`-ěl", "gloss": "God hears", "script": null, "see": ["Layh"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Arabic",
          "refs": "KLN:817",
          "words": [
            {"translit": "Ismâ`îl", "gloss": "\"God hears\", name of son of Abraham", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "Esmâ`îl", "gloss": "\"God hears\", a male name, son of Abraham", "script": "اسماعیل"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "حلق پیش آورد اسماعیل وار - کارد بر حلقش نیارد کرد کار",
            "poet": "Molavî"
          }
        },
        {
          "id": 6,
          "parent": 3,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "Šam`ŭn", "gloss": "Shimeon, Simeon, a follower of Jesus", "script": "شمعون"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "همان رازهایی که عیسای پاک - به شمعون بگفت از لب تابناک",
            "poet": "Sorŭsh"
          }
        },
        {
          "id": 7,
          "parent": 3,
          "lang": "English",
          "refs": "KLN",
          "words": [
            {"translit": "Shema", "gloss": null, "script": null},
            {"translit": "Simon", "gloss": null, "script": null},
            {"translit": "Simeon", "gloss": null, "script": null},
            {"translit": "Shimeon", "gloss": null, "script": null},
            {"translit": "Ishmael", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Smeit",
        "lang": "Indo-European",
        "refs": "POK:968",
        "gloss": "to throw, send forward"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:968; KLN:988",
          "words": [
            {"translit": "maěth", "gloss": "to send, throw", "script": null},
            {"translit": "hamista", "gloss": "thrown down, put down", "script": null},
            {"translit": "hamaěstar", "gloss": "one who throws down, enemy", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "SNS:53",
          "words": [
            {"translit": "haměstâr", "gloss": "enemy", "script": null},
            {"translit": "haměstagân", "gloss": "awkward situation", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "HRN:279; MON:5185",
          "words": [
            {"translit": "hamîstar", "gloss": "enemy", "script": "همیستر"},
            {"translit": "hamîstakân", "gloss": "a place between hell and heaven", "script": "همیستکان"}
          ],
          "script_extra": null,
          "note": "Almost obsolete words.",
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "mithere", "gloss": "to send off", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "French",
          "refs": "AHD",
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "MON:3079",
          "words": [
            {"translit": "komîsîyon", "gloss": "commission", "script": "کمیسیون"}
          ],
          "script_extra": "کمیته",
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 5,
          "lang": "English",
          "refs": "AHD; KLN:988",
          "words": [
            {"translit": "commit", "gloss": null, "script": null},
            {"translit": "emit", "gloss": null, "script": null},
            {"translit": "omit", "gloss": null, "script": null},
            {"translit": "remit", "gloss": null, "script": null},
            {"translit": "submit", "gloss": null, "script": null},
            {"translit": "admit", "gloss": null, "script": null},
            {"translit": "permit", "gloss": null, "script": null},
            {"translit": "transmit", "gloss": null, "script": null},
            {"translit": "mission", "gloss": null, "script": null},
            {"translit": "commission", "gloss": null, "script": null},
            {"translit": "committee", "gloss": null, "script": null},
            {"translit": "missile", "gloss": null, "script": null},
            {"translit": "promise", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Smelo", "redirect": "Mel 2"},
      "nodes": []
    },
    {
      "root": {"name": "Smer", "redirect": "Mer 1"},
      "nodes": []
    }
  ]
}
```


## [2026-09-14T02:27:39.818Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','MON','FVA','POK','SNS','HRN','AHD','WLD','BRT','PHD','NYB','IEC','SYN','SKT','FSD','WEB','FVQ','AFM','PLA','BQT','ARY','HUB','CHEUNG','KNT']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:400])\n\""
}
```


### [2026-09-14T02:27:40.952Z] TOOL RESULT

```
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 202
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
CHEUNG null
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
```


## [2026-09-14T02:27:57.948Z] TOOL CALL #5: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ | head -80; echo ---; sed -n '1,120p' /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-14T02:27:58.018Z] TOOL RESULT

```
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
---
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
```


## [2026-09-14T02:28:02.826Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['KLN','POK','AHD','SNS','HRN','MON','BRT','PHD','NYB','LEW','LAT','IEC','SYN','FVQ','AFM','PLA','KLN']:\n    v=d.get(k)\n    if not v: continue\n    print('===',k, v.get('local_file'), '| offset:', v.get('page_offset'), '| hint:', str(v.get('lookup_hint'))[:300])\n\""
}
```


### [2026-09-14T02:28:03.943Z] TOOL RESULT

```
=== KLN /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt | offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
=== POK /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt | offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' giv
=== AHD /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt | offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru
=== SNS ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt'] | offset: 242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image | hint: grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.
=== HRN /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt | offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
=== MON ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] | offset: None | hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe
=== BRT /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt | offset: Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
=== PHD /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt | offset: leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).
=== NYB /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt | offset: Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.
=== LEW /home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt | offset: 1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Latin headword in bold at line start. For 1938 pagination borrow lateinischesetym0000awal.
=== LAT /home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt | offset: leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Latin headword in bold at line start followed by gender/declension, e.g. grep -n '^pater,'.
=== IEC /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt | offset: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
=== SYN /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt | offset: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
=== FVQ ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt'] | offset: printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves) | hint: Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).
=== AFM ['/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt'] | offset: 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image | hint: Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').
=== PLA ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt'] | offset: 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276). | hint: HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
=== KLN /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt | offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
```


## [2026-09-14T02:28:09.942Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'shama\\|shema\\|sama\\`\\|Ishmael\\|Yishma' KLN_1966.txt | head -60"
}
```


## [2026-09-14T02:28:11.012Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n '^Simon\\|^Simeon\\|^Shema\\|^Ishmael\\|^Shibboleth\\|^shema' KLN_1966.txt | head -40"
}
```


### [2026-09-14T02:28:11.098Z] TOOL RESULT

```
2030:Ahabah  Rabbah,  the  second  of  two  benedictions preceding  the  Shema  in  the  morning  prayer (Jewish  liturgy).  —  Heb.  ahabhdh  rabbd h,  lit. with  great  love’  (so  called  from  the  two  first words  of  the  text  of  the  benediction).  Ahabhdh, l°ve’,  derives  fr.  ahabh,  ‘he  loved’,  which  is  rel. to  Aram,  ahabh,  ‘he  loved’,  and  possibly  also to  Arab,  habba,  ‘he  was  moved’.  Rabbdh  is  fem.
2032:^■hath  Olam,  the  second  of  the  two  benedic¬ tions  preceding  the  Shema  in  the  evening  prayer
12751:El,  n.,  Hebrew  name  for  God.  —  Heb.  El,  ‘God’, of  uncertain  etymology;  possibly  related  to  el, ‘strong’  (cp.  e.g.  Gen.  31: 29  yesh  ESI  yadt,  ‘it is  in  my  power’).  Cp.  Elohim.  Cp.  also  the  first element  in  the  PN.s  Eleazar,  Eliezer,  Elihu, Elijah,  Elishah,  Elizabeth,  and  the  second  ele¬ ment  in  Babel,  bethel  and  in  the  PN.s  Daniel, Emmanuel,  Ezekiel,  Gabriel,  Gamaliel,  Ishmael, Israel,  Joel,  Michael,  Nathaniel,  Raphael, Samuel.
16090:Geullah,  n.,  the  benediction  which  follows  the Shema  in  the  morning  and  evening  service ( Jewish  liturgy).  —  Heb.  g('ullih,  ‘redemption’, from  the  stem  of  gd'dl,  ‘he  has  redeemed’:  so called  because  it  ends  with  the  words  “who  has redeemed  Israel”.  Cp.  goel.
19959:Ishmael,  n.,  son  of  Abraham  and  Hagar  (Bible); used  in  a  figurative  sense  to  denote  an  outcast (see  Gen.  16:12)  —  Heb.  Yishmafl,  lit.  ‘God hears’.  Heb.  yishmd',  ‘he  will  hear’,  is  imperf. of  shdmd,  ‘he  heard’.  See  Sbema  and  cp.  Simeon, Simon.  For  the  second  element  in  the  name Ishmael  see  El  and  cp.  words  there  referred  to. Derivative:  Ishmael-ite,  n.
20555:Kedar,  n.,  a  tribe  of  northern  Arabia.  —  Heb. Qedhdr,  fr.  Qedhdr,  son  of  Ishmael  (see  Gen. 25:3,  IChr.  1:29),  rel.  to  qadhar,  ‘was  black, dark,  swarthy’,  whence  also  qadhruth,  ‘dark¬ ness,  gloom’,  qedhorannlth,  ‘gloomily,’  QidhrSn, name  of  a  wady  and  valley  east  of  Jerusalem, Mishnaic  Heb.  qldherdh,  ‘pot’,  qadddr,  ‘potter’, and  to  Aram,  qidhrd,  qedherd,  Syr.  qedhrd,  ‘pot’, Arab,  qddhura,  qadhira,  ‘was  dirty’.
22428:Maarib  Arabim,  the  first  of  the  two  benedictions preceding  the  Shema  in  the  evening  prayer  (Jew¬ ish  liturgy ).  — Heb.  ma‘drtbh  'arabhim,' bring¬ ing  evenings’.  See  prec.  word;  ‘ arabhlm ,  ‘eve¬ nings’,  is  the  plural  of  ‘erebh.  The  name  of  the benediction  was  taken  from  the  words  ma'artbh ‘ arabhtm  occurring  in  the  text.
23791:mezuzah,  mezuza,  n.,  a  small  roll  of  parchment containing  Deut.  6:4-9  (the  Shema),  and  Deut. 11:13-21,  affixed  to  the  doorpost  of  every  room, on  the  right  side  of  the  entrance  (Jewish  religion).
24893:Nabataean,  Nabatean,  n,,  1)  a  member  of  an  an¬ cient  people  of  Arabia;  2)  the  Aramaic  dialect spoken  by  this  people.  —  Formed  with  suff.  -an fr.  L.  Nabataeus,  fr.  Gk.  NaflaTcaog,  fr.  Arab. Nabatu,  which  is  usually  connected  with  Ne- baioth,  the  Arst-born  son  of  Ishmael  (see  Gen. 25  :  13).  See  Gesenius-Buhl,  HWAT.,  p.  480. Derivative:  Nabat(a)ean,  adj. nabk,  n.,  Christ’s-thorn.  —  Arab,  nabiqa1'. nabla,  n.,  an  ancient  musical  instrument.  —  Gk. vaj3Aa,  fr.  Aram,  nabhla,  fr.  Heb.  nebhel,  name of  a  stringed  instrument,  fr.  nebhel,  ‘a  large  jar’ ; so  called  after  its  original  shape, nabob,  n.,  1)  a  native  deputy  in  India;  2)  a  Euro¬ pean  who  has  come  home  from  India  with  a great  fortune;  3)  a  very  rich  man.  —  Hind. nawwab,  nabob,  fr.  Arab,  nuwwab,  pi.  of  na'ib, 'deputy,  proxy,  lieutenant  governor',  prop.  act. part,  of  naba  (fr.  base  n-w-b),  'he  took  a  person’s place’.  The  pi.  nuwwab  is  used  as  a  plural  of dignity  and  has,  accordingly,  singular  meaning. Cp.  nawab.
25622:‘left  hand’.  Cp.  Heb.  mot,  Arab,  shamal,  ‘left hand;  north’;  OIr.  riiath,  ‘left,  northern’,  tuaith, ‘in  the  north’,  tuathun,  ‘on  my  left  hand’ ;  fochla , ‘north,  left  hand  seat  in  the  war  chariot’.  For sense  development  cp.  south.
34736:Derivatives:  servile-ly,  adv.,  servile-ness,  n., servil-ism,  n.,  servil-ity,  n. servitor,  n.,  servant.  —  ME.  servitour,  fr.  OF. servitour  (F.  serviteur),  fr.  Late  L.  servitorem, acc.  of  servitor,  ‘servant’,  fr.  L.  servire,  ‘to serve’.  See  serve  and  agential  suff.  -or. Derivatives :  servitor-ial,  adj.,  servitor-ship,  n. servitude,  n.,  bondage.  —  ME.,  fr.  OF.  ( —  F.) servitude,  fr.  L.  servitudd,  ‘slavery’,  fr.  servus, ‘slave’.  See  serve  and  -tude. sesame,  n.,  1)  an  East  Indian  plant,  whose  seeds yield  an  oil  and  are  used  as  food;  2)  its  seeds.  — F.  sesame,  fr.  L.  sesamum,  fr.  Gk.  arjoapiov, ‘seed  or  fruit  of  the  sesame  plant’,  crqa dtjarj,  ‘ses¬ ame  plant’,  fr.  Dor.  ai.aczp.ov,  which  is  a  Semit¬ ic  loan  word.  Cp.  Aram.  shumshlma,  ‘sesame’, Arab,  simsim,  Akkad,  shamashshamu,  of  s.m. Through  the  medium  of  the  Phoenicians  this Semitic  word  was  borrowed  by  the  Greeks  very early.  It  is  found  in  15th  cent.  Mycenaean Greek.  See  Michael  Ventris  and  John  Chad¬ wick,  Documents  in  Mycenaean  Greek  (Cam¬ bridge  University  Press),  Index,  s.v.  Semitic Loanwords.  Cp.  the  words  chiton,  chrysalis, cumin.
34871:Derivatives:  sham,  intr.  v.  and  adj. shama,  n.,  an  Indian  song  bird.  —  Hind,  sdma, fr.  OI.  sydmah,  ‘black,  dark-colored', shaman,  n.,  priest  of  the  Ural-Altaic  peoples. Tungus  saman,  ‘priest,  medicine  man’. Derivatives;  shaman-ic,  adj.,  shaman-ism,  n., shaman-ist,  n.,  shaman-ist-ic,  adj.
34872:Shamash,  n.,  the  chief  sun  god  of  Assyria  and Babylon.  —  Akkad,  shamash,  shamshu,  ‘sun; the  god  of  the  sun’,  rel.  to  Heb.  shemesh,  ‘sun’, Aram.shimsha,  Syr.  shemshd,Vgar.  sh-p-sh,  Arab. shams  (dissimilated  fr.  *shamsh),  of  s.m.;  prob. from  the  Semitic  base  s-m-s-m,  ‘to  be  swift’  (said of  the  quivering  sunrays).  Aram,  shumshdna, Arab,  sumsum,  Aram.  shumsh6mdna  (whence through  syncope  shumshdna,  whence  through metathesis  shushmana),  ‘ant ,  are  of  the  same base.  See  Fleischer,  Beitrage  zu  Jacob  Levy’s Worterbuch  iiber  die  Targumim,  II,  pp.  577f. Cp.  Samson.
34953:Shema,  n.,  one  of  the  most  important  parts  of  the Jewish  daily  liturgy,  consisting  of  the  three  sec¬ tions:  Deut.  6  :  4-9,  11  :  3-21,  Num.  15  :  37-41. —  Heb.  shema',  lit.  ‘hear’, imper.  of  Heb. shama', ‘he  heard’,  whence  shema',  ‘sound’,  shema', ‘hearing’,  shlmua,  sh(mu'dh,  ‘report’;  rel.  to Aram. -Syr.  shema',  Ugar.  shm‘,  Arab,  sami'a, Ethiop.  sanf'a,  ‘he  heard’,  Akkad,  shemii,  ‘to hear’.  The  prayer  is  called  Shema  from  the  first word  of  Deut.  6  :  4,  the  verse  containing  Israel’s confession  of  faith.  Cp.  Ishmael,  Simeon, smouse,  Tashmitum.
34957:Derivative:  Shemit-ic,  adj.  (=  Semitic), shemittah,  n.,  the  sabbatical  year,  i.e.  every seventh  year,  in  which  fields  and  vineyards  must not  be  tilled  (Jewish  Religion).  —  Heb.  shimittah, ‘remission,  release’  (short  for  sh^nath  hash- sh6mittah,  ‘the  year  of  release’),  fr.  shamat,  ‘he let  loose,  let  drop,  let  fall;  he  let  (the  land)  rest’, which  is  rel.  to  Aram,  shamat,  ‘he  let  loose, loosened,  detached;  he  unsheathed,  drew  (said esp.  of  a  sword)’,  Syr.  shemat,  ‘he  drew  (a sword)’,  Arab,  samata,  ‘he  hung  up  (some¬ thing)’,  sammata,  ‘he  released  (a  debtor)’, Akkad,  shamdtu,  ‘to  declare  null  and  void’, shenanigan,  n.,  foolery.  —  Perh.  fr.  Ir.  sionnach, ‘fox’.
35244:Simeon,  masc.  PN.;  in  the  Bible,  the  second  son of  Jacob  and  Leah ;  a  tribe  of  Israel.  - —  Late  L., fr.  Gk.  Eupccov,  fr.  Heb.  Shim' on,  lit.  ‘hearing’, fr.  shdma',  ‘he  heard’.  See  Shema  and  cp.  Simon. Cp.  also  Ishmael.
35245:simhah,  also  spelled  simeha,  n.,  a  joyful  occasion, as  in  a  birth,  bar  mitzvah  or  wedding.  —  Heb. simhaH,  ‘joy,  gladness,  merriment,  mirth’,  fr. sarndh,  ‘he  was  glad,  rejoiced’,  which  is  possibly rel.  to  Arab,  shamaha,  ‘was  high,  was  proud’. For  sense  development  cp.  E.  elated,  which unites  the  following  meanings:  ‘in  high  spirits; proud ;  joyful’  (see  elated).
35687:smoulder,  n.  —  A  var.  of  smolder, smouse,  smouch,  n.,  a  Jew  (slang.)  —  Du.  smous, fr.  G.  Schmus,  ‘talk’,  fr.  G.  Slang  schmuofi,  fr. Yiddish  schmuofi,  fr.  Heb.  shemu‘Sth,  pi.  of shemu‘dh,  ‘report,  news’,  fr.  shama,  ‘he  heard’. See  Shema.
38267:Tashmitum,  n.,  a  Babylonian  goddess,  the  wife  of Nebo.  —  Akkad.  Tashmitum,  lit.  ‘proclaimer’, fr.  tashmitum,  ‘a  hearing’,  fr.  shemu,  ‘to  hear’, which  is  rel.  to  Heb.  shama\  ‘he  heard’.  See Shema.
```


### [2026-09-14T02:28:11.155Z] TOOL RESULT

```
19959:Ishmael,  n.,  son  of  Abraham  and  Hagar  (Bible); used  in  a  figurative  sense  to  denote  an  outcast (see  Gen.  16:12)  —  Heb.  Yishmafl,  lit.  ‘God hears’.  Heb.  yishmd',  ‘he  will  hear’,  is  imperf. of  shdmd,  ‘he  heard’.  See  Sbema  and  cp.  Simeon, Simon.  For  the  second  element  in  the  name Ishmael  see  El  and  cp.  words  there  referred  to. Derivative:  Ishmael-ite,  n.
34953:Shema,  n.,  one  of  the  most  important  parts  of  the Jewish  daily  liturgy,  consisting  of  the  three  sec¬ tions:  Deut.  6  :  4-9,  11  :  3-21,  Num.  15  :  37-41. —  Heb.  shema',  lit.  ‘hear’, imper.  of  Heb. shama', ‘he  heard’,  whence  shema',  ‘sound’,  shema', ‘hearing’,  shlmua,  sh(mu'dh,  ‘report’;  rel.  to Aram. -Syr.  shema',  Ugar.  shm‘,  Arab,  sami'a, Ethiop.  sanf'a,  ‘he  heard’,  Akkad,  shemii,  ‘to hear’.  The  prayer  is  called  Shema  from  the  first word  of  Deut.  6  :  4,  the  verse  containing  Israel’s confession  of  faith.  Cp.  Ishmael,  Simeon, smouse,  Tashmitum.
35244:Simeon,  masc.  PN.;  in  the  Bible,  the  second  son of  Jacob  and  Leah ;  a  tribe  of  Israel.  - —  Late  L., fr.  Gk.  Eupccov,  fr.  Heb.  Shim' on,  lit.  ‘hearing’, fr.  shdma',  ‘he  heard’.  See  Shema  and  cp.  Simon. Cp.  also  Ishmael.
35256:Simon,  masc.  PN.  —  L.,  fr.  Gk.  Etpxov,  fr.  Heb. Shim'dn,  but  influenced  in  form  by  the  Greek PN.  Sfuojv,  lit.  ‘snub-nosed’  (fr.  ai(j.o?,  of s.m.),  whence  the  Talmudic  name  Simdn.  See
35257:Simeon.
35258:Simon  Pure,  the  right,  genuine  person.  —  Name of  a  Quaker  in  Susanna  Centlivre’s  play  A  Bold Stroke  for  a  Wife  (1717).  In  part  of  the  play Simon  Pure  is  impersonated  by  another  char¬ acter  (Colonel  Feignwell)  and  the  real  Simon Pure  is  dealt  with  as  an  impostor  and  is  believed only  after  he  has  proved  his  identity, simoniac,  n.,  one  who  practises  simony;  adj.,  per¬ taining  to  simony.  —  ML.  simoniacus,  fr.  simo- nia.  See  simony.
35261:Simon.
```


## [2026-09-14T02:28:17.678Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport bisect\n# map line number -> leaf\nlines=t.split('\\n')\ndef leaf_of_line(n):\n    # count formfeeds in first n lines\n    return '\\n'.join(lines[:n]).count('\\f')\nfor n in [19959,34953,35244,35256,35687,34872,12751]:\n    print(n, 'leaf', leaf_of_line(n))\nEOF"
}
```


## [2026-09-14T02:28:18.887Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n '^mission,\\|^commit,\\|^missile,\\|^admit,\\|^promise,\\|^emit,\\|^omit,\\|^transmit,' KLN_1966.txt | head"
}
```


### [2026-09-14T02:28:19.230Z] TOOL RESULT

```
19959 leaf 442
34953 leaf 761
35244 leaf 767
35256 leaf 767
35687 leaf 776
34872 leaf 759
12751 leaf 275
```


### [2026-09-14T02:28:19.301Z] TOOL RESULT

```
8381:commit,  tr.  v.  —  L.  committere,  ‘to  join  or  put together,  to  unite,  connect,  commit’,  fr.  com-  and mittere  (pp.  missus),  ‘to  send’.  See  mission  and cp.  fideicommissum.
24047:mission,  n.  —  L.  missio,  gen.  -onis,  ‘a  sending mission’,  fr.  missus,  pp.  of  mitt 6,  mittere,  ‘to cause  to  go,  to  send,  throw,  hurl,  cast’,  which  is prob.  cogn.  with  Avestic  mae&,  ‘to  send’,  pos¬ sibly  also  with  Goth,  bi-smeitan,  ga-smeitan,' to spread,  smear’,  OHG.  smizan,  ‘to  rub.  strike’, etc.  (see  Walde-Hofmann.  LEW.,  II,  98).  See smite  and  -ion  and  cp.  admission,  admit,  com¬ missariat,  commission,  commit,  committee,  com¬ promise,  demise,  demit,  dismiss,  emission,  emit, immission,  immit,  intermission,  intermit,  intro¬ mission,  intromit,  manumission,  manumit.  Mass, mess,  message,  mise,  missal,  missile,  missive, mittimus,  omission,  omit,  permission,  permit.
30502:promise,  n.  —  ME.  promis,  partly  fr.  L.  promis- sum,  neut.  pp.  of  L.  promittere,  ‘to  send  forward, foretell,  promise’,  partly  fr.  F.  promesse,  ‘prom¬ ise’,  fr.  L.  promissa,  neut.  pi.  of  the  pp.  pro- missus,  taken  as  a  fern.  sing.  noun.  L.  promittere is  formed  fr.  1st  pro-  and  mittere,  ‘to  send’.  See mission.
39872:transmit,  tr.  and  intr.  v.,  1)  to  send  over;  2)  to cause  to  pass  through;  3)  to  communicate;  4) to  hand  down  to.  —  ME.  transmitten,  fr.  L. transmittere,  ‘to  send  across,  send  off’,  fr.  trans- and  mittere,  ‘to  send’.  See  mission  and  cp.  words there  referred  to.
```


## [2026-09-14T02:28:26.868Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ndef leaf_of_line(n):\n    return '\\n'.join(lines[:n]).count('\\f')\nprint('mission leaf', leaf_of_line(24047))\nprint('commit leaf', leaf_of_line(8381))\nleaves=t.split('\\f')\nfor L in [442,761,767,486]:\n    seg=leaves[L]\n    print('--- leaf',L,'first 300:',repr(seg[:300]))\nEOF"
}
```


### [2026-09-14T02:28:28.075Z] TOOL RESULT

```
mission leaf 530
commit leaf 179
--- leaf 442 first 300: 'ains  in the  hip’,  compounded  of  Gk.  EoxEov,  ‘hipjoint’, and  itXyo ?,  ‘pain’.  See  ischium  and  -algia. ischiatic,  adj.,  ischial.  —  ML.  ischiaticus,  altered fr.  L.  ischiadicus.  See  ischiadic, ischio-,  before  a  vowel  ischi-,  combining  form meaning  ‘pertaining  to  the  hip’'
--- leaf 761 first 300: 'cepter’,  and  to  Heb. shebhet,  Tod,  staff,  club,  scepter’,  Aram,  shibhtd. Tod,  staff’,  Ethiop.  zabata,  ‘he  beat’, shebeen,  n.,  an  unlicensed  store  where  liquor  is sold.  —  Ir.  sibin,  seibin,  ‘a  little  mug’. Derivatives:  shebeen,  intr.  v.,  shebeen-er,  n.\nshechita,  shec'
--- leaf 767 first 300: 'g  to,  or  con¬ taining,  silica.  —  See  silica  and  -ous. silicic,  adj.,  derived  from,  or  pertaining  to,  silica. —  See  silica  and  adj.  suff.  -ic. siliciferous,  adj.,  containing  silica.  —  See  silica and  -ferous.\nsilicify,  tr.  v.,  to  convert  into  silica;  intr.  v.,  to '
--- leaf 486 first 300: "e’,  which  prob.  stands  for  *grl- bhos  and  is  cogn.  witn  MHG.  krebe,  ‘basket’, ON.  kiarf,  kerfi,  ‘bundle’,  OI.  grapsah,  ‘bundle’, logomachy,  n.,  a  fight  in,  or  about,  words.  —  Gk. Xoyopaxi®.  ‘war  about  words’,  compounded  of Xoyop,  ‘word,  speech’,  and  pedex'') >  ‘b"
```


## [2026-09-14T02:28:36.142Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor L in [529,530,531,760,761,762,441,442,443,178,179]:\n    seg=leaves[L]\n    nums=re.findall(r'\\b(8\\d\\d|9\\d\\d|1[0-7]\\d\\d)\\b', seg[:200]+seg[-200:])\n    print(L, nums[:6], '|', repr(seg[:60]), '|', repr(seg[-60:]))\nEOF"
}
```


### [2026-09-14T02:28:37.177Z] TOOL RESULT

```
529 [] | '  and  cp.  the  first  element  in  muscovado.  _ minuscule' | "pity, deplore',  fr.  miser,  ‘wretched,  miserable,  piti¬ "
530 [] | 'able’,  which  is  of  uncertain  etymology.  Cp.  Mi¬ serer' | ' OIr.  moith,  Mir. moeth,  Ir.  maoth,  ‘soft’.  Cp.  also '
531 [] | '— with  -/-forma¬ tive  element — OSlav.  milu,  ‘charitable' | '  mobb-ish,  adj. mob,  n.,  a  woman’s  headdress.  —  Shor'
760 ['987'] | 'n.  F.  chantier,  ‘workshop’, fr.  F.  chantier,  ‘timberya' | 'ee  HEL.,  p.  987),  which is  rel.  to  shabbitu.  Tod,  s'
761 [] | 'cepter’,  and  to  Heb. shebhet,  Tod,  staff,  club,  scept' | 'the  land)  rest’, which  is  rel.  to  Aram,  shamat,  ‘he '
762 [] | ' let  loose, loosened,  detached;  he  unsheathed,  drew  (s' | 'r. Chin,  shin  tao,  ‘the  path  of  the  gods’. Derivative'
441 [] | 'timulate,  stir  up,  provoke’, prob.  freq.  of  *ir-ri-re,' | 'e  ischium, ischialgia,  n.,  sciatica.  —  ModL.,  lit.  ‘p'
442 [] | 'ains  in the  hip’,  compounded  of  Gk.  EoxEov,  ‘hipjoint' | ' origin,  as  in  comparison, orison,  venison.  This  suff.'
443 [] | '  represents  1)  OF. -aison  (fr.  L.  ationem,  fr.  -atus' | 'Ithyphallus,  n.,  a  genus  of  fungi  of  the  family  of '
178 [] | ' coeno-).  Cp.  1st  con-,  contra-, count,  ‘title  of  nob' | 'cc.  of  cdmitds,  ‘courtesy,  kindness,  affa¬ bility’,  fr'
179 [] | 'om  comis,  ‘courteous,  kind,  affable’, fr.  OL.  cosmis, ' | ' cor¬ responding  to  F.  commis,  fr.  F.  commettre,  ‘to '
```


## [2026-09-14T02:28:53.358Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint('nleaves',len(leaves))\n# find leaves whose content starts/ends with a bare number\nfound=[]\nfor i,seg in enumerate(leaves):\n    m=re.match(r'\\s*(\\d{2,4})\\b', seg)\n    if m: found.append((i,m.group(1)))\nprint(found[:40])\nprint(len(found))\nEOF"
}
```


### [2026-09-14T02:28:54.740Z] TOOL RESULT

```
nleaves 903
[(325, '49'), (496, '1215'), (628, '9607'), (742, '91')]
4
```


## [2026-09-14T02:29:11.169Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'smeit' POK_full.txt | head -20; echo '=== POK_03 leaf for p968: leaf = p-762..766'; python3 - <<'EOF'\nt=open('POK_03.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor L in range(200,210):\n    print('---leaf',L, repr(leaves[L][:200]))\nEOF"
}
```


### [2026-09-14T02:29:12.301Z] TOOL RESULT

```
78446:Root / lemma: smeit-, smit- 
78458:intensification from *smTtd{*smeitd), compare cosm/ttere Pau\. Fest. 
78737:smeitan 'smear, stroke'. Old High German smTzan 'stroke, smear, hit'. Modern High 
=== POK_03 leaf for p968: leaf = p-762..766
---leaf 200 "LOv  , Wamme'  (vgl. iöJca  , schlaff  herabhängen'),  nasaliert  vermutlich  hierher  Xayycc^co Xayychv  , Zaudern',  Xayysvai '  cpevyat  Hes.  (*,matt  sein,  schlaff  und ^  sein') ;   mit   der  "
---leaf 201 "s)leih-  , schlüpfrig,   gleiten'  s.  oben   S.   663;   dazu  vielleicht  (nach  Morris- Jones  WGr.  125)  cymr.  llithr  m.  ,das  Gleiten'  (*slib-tro-).\n(s)leidh-  ^schlüpfrig,   gleiten';   Erw"
---leaf 202 "  len- kernenn , Eingeweidewurm*  (*slinkurl-),  mbret.  lencr  ,schleichend' ;  ahd. slingan^  ags.  slingan  st.  V.  , schwingen,  winden,  flechten',  refl.  ,sich schlängeln,  kriechen*,  aisl.  "
---leaf 203 "lokeren  ,schlaff  sein,   schlottern*,   mit   kk:  slukkern  ds.   (nhd.   Schluckt^ slukk   ,traurig',   slokh  ,schlaff,   schwach',  norw.   slauk   ,schlaffer   Men8< slauka   ,sich   schleppen'"
---leaf 204 "Regen  und  Schnee  durcheinander',  aisl. ilota  ,herabhängen*,  schwed.  dial.  ,faul  sein',  mit  gedehnter  Tiefstufe  aisl. tlüta  ,herabhängen,  hangen,  lässig  sein*,  nhd.  dial.  schlössen "
---leaf 205 "ggeln',  Schweiz,  slüche  ,schleppend  gO^^V'^ii slüchi  »langsamer,  schleichender,  heimtückischer  Mensch';  mhd.  ''hmk  ^ ,Schlangenhaut,  Schlauch'  (eig.  , worein  geschlüpft  wird'),  nhd.  "
---leaf 206 "s.  släh  (engl,  sloe), nhd.  ßchlehe'',  schwed.  slä{n)  ds. ;  vgl.  Martinet  Word  12,  4.\nWP.  II  715 f.,  WH.  I  816,  Trautmann  269  f.,  Vasmer  2,  660.\nslougo-,  -ä-  f.  ,das  Helfen, "
---leaf 207 'o-)\',  got.  bi-smeitan  ,beschmieren|"; bestreichen\',  ga-smeitan  ,schmieren,  streichen\',  ahd.  smlzan  , streichen? schmieren,  schlagen,\'  nhd.  schmeißen,  ahd.  bismizan  ,beschmieren\',  sloC '
---leaf 208 "wa^wriaf , Leckerbissen',  sma^w?naw^z , naschen',  smagüris  , Zeigefinger' (eigentlich  ,Naschfinger,  Näscher');  vielleicht  ist  smeg(hy  als  s-Form  mit  lit. m^gti  , Wohlgefallen'  usw.  iden"
---leaf 209 " im  Sim- plex erfolgtem  Anlautswandel  von  sm-  zu  [ä]w-);  hamaestar-  ,wer  nieder» wirft,  unterdrückt' ;  maed-  , werfen',  mit  Ablat.  *emittere  ex^  =  ,berauben* (möid-at),  mit  ä-  ,(a"
```


## [2026-09-14T02:29:17.825Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('POK_03.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor L in [206,207,208,209]:\n    print('======= leaf',L)\n    print(leaves[L][:2500])\nEOF"
}
```


### [2026-09-14T02:29:18.885Z] TOOL RESULT

```
======= leaf 206
s.  släh  (engl,  sloe), nhd.  ßchlehe'',  schwed.  slä{n)  ds. ;  vgl.  Martinet  Word  12,  4.
WP.  II  715 f.,  WH.  I  816,  Trautmann  269  f.,  Vasmer  2,  660.
slougo-,  -ä-  f.  ,das  Helfen,  Dienen*;  nur  keltisch  und  balto-slavisch.
Air.  slög,  slüag  m.  ,Heer,  Schaar*,  teg-lach  (*tego-slougo-)  , Hausgenos- senschaft, Familie*,  cymr.  llu  ,Heer',  acymr.  telu^  mcymr.  ieüu,  jünger teulu  , Gefolge*,  ncymr.  ^Haushalt,  Familie*,  acorn.  luu^  mcorn.  lu  ,Menge, Schaar,  Heer*;  gall.  VN  Catu-slugi  (leg.  -slögi)  , Kampfesscharen' ;  lit. ^emait.  slaugau,  slaugyti  ,unterstützen,  helfen*,  slaugä  ,das  Dienen',  pä- slauga  , Hilfe,  Hilfeleistung*;  aksl.  sluga  m.  ,Diener';  dazu  aksl.  sluzg, sluziti  , dienen*,  usw.
WP.  II  716,  Trautmann  268  f.,  Vasmer  2,  664f.
{s)lrg-  und  sler-  Schallwurzel.
Gr.  Xdgvy^,  -vyyog  m.  , Schlund*  (vielleicht  nach  gxxQvy^  umgebildet);
lat.  lurco{r)j  -äre,  -ärl  ,schlemmen,  fressen*,  wenn  auf  *lurgicos  beruhend; lurcö,  -önis  m.  , Schlemmer*;
mhd.  slurc  ^Schlund',  slurken  , schlucken*,  norw.  schwed.  slurk  , Schluck, Mundvoll',  norw.  schwed.  slurka  ,in  großen  Zügen  schlürfen*;  nhd.  schlur- chen  ,nachlässig  gehen*;
eine  schallnachahmende  Wurzel  sler-  mit  verschiedenen  Erweiterungen in  lett.  slarjpata  , alter  Lappen',   slarpatdt  , lumpig   einhergehen' :   schwed.
966  •
slarfva  ,Fetzen,  Lappen' ;  lett.  slarkset  (neben  slavpUt)  , schleppend  ffeh nhd.  schlarken  ,schleifend  gehen'  (schlarfen  ds.).  ^^
WP.  II  716,  WH.  I  837.
sme,  smä  u.  dgl.,  etwa  ,wahrlich,  allerdings'.
Ai  smä  hervorhebende  Partikel,  gr.  ^d  in  Schwüren  BeteuerungspartiVfti thess.  ^d  ,aber,  Ö€' ;  *fi&  (=  ai.  smä)  erweitert  zu  {.idv,  ion.-att.  ^i^y  ^^^ dings,  doch*,  ion.  (infolge  Funktionsschwächung)  gekürzt  zu  ^ev,  herri^" hebende  Partikel;  lat^  «am  ,denn^,  ursprüngl.  Versicherungspartikel,  ^14? leicht  aus  *män  umgestaltet;  hitt.  -ma  ,aber',  s.  Schwyzer  Gr.  Gr.  2  5fto A.  Hahn  Lg.  29,  242  f.  '^
WP.  II  685,  Schwyzer  Gr.  Gr.  2,  569,  M.  Leumann  Mus.  Helv.  6,  8öt
sme-,  smei,  sra-ei-  , schmieren,  darüberwischen, -streichen;  dar  über  hinreibea* Gr.  Infin.  Gfifjv,  Aor.  afirjffai  , schmieren,  abwischen,  abreiben*,  3.  Sg.  Pa|> anfjrai,  a^arai',  afii^x^j  afxfj^ai  ds.,  afiwxsiv  ,zerreiben',  a(xrjfj,a  f.  ,Salb«» (Tl^üJÖL^y  -Lyyog  f.  ,blutunterlaufener  Streifen, 
======= leaf 207
o-)',  got.  bi-smeitan  ,beschmieren|"; bestreichen',  ga-smeitan  ,schmieren,  streichen',  ahd.  smlzan  , streichen? schmieren,  schlagen,'  nhd.  schmeißen,  ahd.  bismizan  ,beschmieren',  sloC besmltan  ds.;  norw.  dial.  smita,  abl.  smlta  ,dünn  aufschmieren';  ags.  stmI^ tian  ^beflecken,  anstecken',  mhd.  schmitzen  ,anstreichen,  geißeln,  schlagen*^ nhd.  verschmitzt]  ags.  smitte  f.  ,Fleck*,  mhd.  smitze  f.  , Fleck,  Schmutz*!;' aksl.  smidz  ,fuscus',  auch  in  russ.  FIN.,  vielleicht  als  ,*schmierig'  hier-' her  (,unsicher^,  Vasmer  2,  670  f.).
sme[i]k- :  smik-  , zerriebenes,  winziges  Krümchen':  7^
gr.  anixQÖg^  {a)fiLyiQÖg  ,klein,  kleinlich,  kurz',  dor.  ion.  ^/ixxdg  ,klein' (Kurzbildung  wie  lippus,  yvvvig)-,  lat.  mlca  ,ein  Krümchen,  bißchen',  mlci' dus  ,winzig' ;  ahd.  smähi  , klein,  gering,  niedrig',  aisl.  smär  (*smäha-)  ,klein', ags.  smealic  ,fein,  sorgfältig',  ahd.  smähen  ,klein  machen,  verringern',  nhd. schmähen,  Schmach,  ahd.  gismähteön  , schwinden',  nhd.  schmachten,  ver'/' schmachten]  afries.  forsmäia  ,verschmähen',  mnd.  smaginge  , Schmähung*. In  ähnlicher  Wendung  auf  ,das  Kleine,  Zierliche':
smelJ^g- :  srntig- :  poln.  smagiy  , schlank,  schmächtig';  smigiy  ds.,  smiga , dünne  Rute'  (an  Entlehnung  aus  dt.  schmiegen  ist  gewiß  nicht  zu  denken); lit.  smaXgas  , Stange' ;  lett.  smidzis  ,Milbe,  Wasserfloh^ ;
mit  g-,  lit.  susmizes  , klein,  verkrüppelt';  nisl.  smeikr  ,glatt,  schüchtern';
967
a-s.  stnicre  , schön,  zierlich*,  ahd.  smechar,  smehhar,  mhd.  smecker  , schlank, schmächtig',  norw.  smikr  n.  ,feines  Schnitzwerk'  (daneben  ohne  s-  und  mit anderer  Gutturalstufe  migr  n.  ,allzu  feine  Arbeit',  migren  .schmächtig') ;
eine  deutlichere  Bedeutung  , schmieren,  streichen'  in  norw.  smika  , strei- chen? glätten',  smeikja  , streicheln,  schmeicheln',  nhd.  schmeicheln,  ags.  smä- cian  ds.,  mhd.  smicke  ,der  vorderste  Teil  einer  Peitsche;  Schmiß,  Wunde*, mhd.  smicke^  sminhe  , Schminke'.
Eine    u-Variante    {s)nieu-  :  (s)zn9u-  :  (s)n2u-    scheint   vorzuliegen    in aisl.   inä    (*mawen)   , abnutzen,    abschaben',    norw.    mugg  m.   n.   (*muiüwa-) Sägemehl' ;  aisl.  möa-sk  (*möwön)  ,verdaut  werden' ;  nhd.  bair.  schmaudeln schmeicheln'. '   WP.  11  685  f.,  WH.  II  5  f.,  85.
stneg(h)-  , schmecken';  nur  germ.  und  halt.
Mhd.  smach  , Geschmack,  Geruch',  mnd.  s
======= leaf 208
wa^wriaf , Leckerbissen',  sma^w?naw^z , naschen',  smagüris  , Zeigefinger' (eigentlich  ,Naschfinger,  Näscher');  vielleicht  ist  smeg(hy  als  s-Form  mit  lit. m^gti  , Wohlgefallen'  usw.  identisch,  s.  megh-  ,wohlgesinnt'  oben  S.  707.
WP.  II  689.
/.  (s)mei-,  smeu-  ,lächeln,  erstaunen';  stnei-ro-  , erstaunlich'.
Ai.  smdyate,  -ati  ,lächelt',  Kaus.  smäpayati-  smita-  , lächelnd',  vi-smita- ,erstaunt',  smaya-  n.  , Staunen',  smera-  ,lächelnd'  (=  lat.  mtrus)]
gr.  (mit  (^-Erw.)  ^Tdog'  yeXojg  Hes.,  q)LXo{x^eLdrjQ  ,gern  lächelnd',  (asl- ötjCUj  (.iSLÖLdü)  , lachen';
lat.  mlrus  , wunderbar'  (Bildung  wie  clärus,  =  ai.  smera-)]  lat.  cömis, alt  cosmis  ,gefällig,  freundlich',  als  ,mit  Lächeln',  von  einem  Wurzelnomen
87712- ;
air.  mlad  n.  ,Ruhm,  Stolz',  ablaut.  möldid  , rühmt  sich';
alem.  iml9  ,erstaunen' ;  mengl.  smilin,  engl,  smile^  dän.  smile,  norw. smüa  ,lächeln' ;  ags.  gäl-smäre  ,zum  Lachen  geneigt' ;
lett.  smejuy  smiet  , verlachen',  smaXda  ,das  Lächeln'  (im  -d-  wohl  mit  dem Gr.  zu  vergleichen);  smaidit  ^lächeln^  schmeicheln,  spotten';
aksl.  smäjg  (^smei-iö),  smijati  s§  , lachen',  smäch^  ,das  Lachen';
toch.  A  smi-  ,lächeln'.
Daneben  smeu-  in:
968  ♦
mhd.  smieren,  smielen,  älter  ndl.  smuylen  , lächeln*,  wohl  auch  mhd.  sm^^ ,aus  Unwillen  schweigen,  schmollen]  lächeln';  russ.  uchmyV dthsd  ,lä<^) schmunzeln*,  dial.  chmylüh  ,lächeln',  wohl  auch  poln.  dial.  chmlid  sifj^ verfinstern,  ein  verdrießliches  Gesicht  machend  ^^
WP.  II  686  f.,  WH.  II  94 f.,  Trautmann  270 f.,  Pedersen  ZcP.  17   ».
2.  smei-  :  srnsi-  :  smi-  , schnitzen,  mit  einem  scharfen  Werkzeug  arbeiUn*
Gr.  üixtlrj  ^Schnitzmesser',  aixiv^T],  af.itvvg  »Ha-cke*;
got.  aiza-smipa  , Schmied',   aisl.   smidr  , Arbeiter  in   Holz  (dies  das  fw schichtlich  ältere)  und  Metall',  ags.  smid  , Schmied,  Radmacher*,  ahd.  d^ , Schmied*;   ahd.   smlda   ,Metall,   Metallschmuck*,   gismldi   ,MetallschmuA;'^ Geschmeide*,    aisl.    smld    f.    ,kunstfertige    Arbeit*;    ahd.   smeidar  ,MeuS»^ künstler*;  eine  s-lose  Wzf.  ist  wohl  mai-  {mdi-)  ,hauen,  abhauen*,  s.  dortt*
unsicher  lett.  smicens  , schwarze  Spitzmaus'  (,*Nager*??  oder  zu  tmü. zisj  oben  S.  966?),  lit.  smailüs  ,spitz,  naschhaft',  smilius  ,Näscher,  Zei«K finger'.
WP.  II  686.
3.  smei-,  smeid-,  smeig-,  smeik-,  s.  oben  S.  966  f.
smeit-,  sm
======= leaf 209
 im  Sim- plex erfolgtem  Anlautswandel  von  sm-  zu  [ä]w-);  hamaestar-  ,wer  nieder» wirft,  unterdrückt' ;  maed-  , werfen',  mit  Ablat.  *emittere  ex^  =  ,berauben* (möid-at),  mit  ä-  ,(an  sich)  kommen  lassen*  (ämid-näiti),  mit  jpaiti-  ,*zurück- schicken'  =  ,den  Laufpaß  geben,  absagen',  mit  ham-  , berauben'  (h9mi^äj[j\ mit  ham  -\-  aihl  ,zulassen,  den  Zutritt  gestatten' ;
lat.  mittö,  -ere,  mlsi,  missum  , gehen  lassen,  laufen  lassen;  schicken,  senden', mit  expressiver  Verschärfung  aus  *smitö  (^smeitö),  vgl.  cosmittere  Paul.  Fest
WP.  II  687  f.,  WH  II  97  ff.  ti
sznek-  ,Kinn,  Mundpartie,  Bart',  im  ai.  mit  Je,
Ai.  smdsru-  n.  ,Bart,  Schnurrbart*  (assim.  aus  *smasru-) ;  arm.  mauruJ^ mort^Ä  , Bart' ;  alb.  mjekre  ,Kinn,  Bart'  {*smekra)]  vielleicht  lat.  mala  , Kinn- backe, Kinnlade',  Demin.  maxilla  (*smek-slä,  dessen  Vokal  mit  dem  arm.  a vergleichbar  wäre);  ir.  smech  ,Kinn*  {*smeka)j  vermutlich  ags.  smaras  m, PL  ,Lippen'  (*smahria-),  dazu  als  , Lippenblütler'  nisl.  smära  f.,  smäri  m., norw.  dän.  smösre  m.,  schwed.  dial.  smäre  m.  ,Klee'^  nach  anderen  zu  smei- jlächeln*;  lit.  smäkras  m.,  smakrä  f.  ,Kinn',  lett.  smaJcrs  ,Kinn,  Gaumen'; hitt.  zama(n)kur  ,Bart'  (*smokur  oder  *smokru-).
WP.  II  689,  WH.  II  15,  Trautmann  270.
969
5X22^2-  jlangsam  und  rauchend  verbrennen,  schwelen'.
Mir.  smäl,  smöl,  smüal  f.  ,Feuer,  Glut,  Asche*;  mnl.  smölen,  ndl.  smeulen trlimmen,  schwelen^,  nd.  smelen,  smölen  ds.,  ö-stufig  fläm.  smoel  , schwül': jjjeagl-  smolder  ,Rauch',  nengl.  smoulder-^  auch  (vgl.  rauchen :  riechen)  mengl. ^elj  smul  [-11-)  , Geruch',  engl,  smell]
osorb.  smalic  ,sengen'_,  nsorb.  smalis  , sengen,  schwärzen',  klr.  jprysmaiyty ^anbrennen'.
Hit  ic-Erweiterung :  lit.  smilhstüj  smilkti  , einen  schwachen  Dunst  oder Rauch  von  sich  geben',   smilkyti  , räuchern',   smelkiil,  smelkti  ,ersticken' ;_
daneben  im  Germ,  mit  r-  ags.  smorian  ,ersticken  (tr.)',  mnd.  smoren dämpfen,  ersticken  (tr.  und  intr.)  ^schmoren',  fläm.  smoren  , rauchen,  neblig sein',   mnd.   smurten  , ersticken',   mengl.   smorther,   engl,   smother   ,Dampf'.
WF.  II  691  f. ;  Vasmer  3,  670,  675.
2.  smel-  jgrau,  staubfarben'?
Gr.   (xsllrj  , Esche;   Speer   aus   Eschenholz*  {evnnsllr^q  ,mit  einem  guten Eschenspeer    bewaffnet'),    ^liXivog,    fxsiXivog    ,eschen'    (
```


## [2026-09-14T02:29:22.967Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '78440,78480p' POK_full.txt"
}
```


### [2026-09-14T02:29:23.042Z] TOOL RESULT

```
uchmylatbsa ' smile, schmunzein', dial, chmylftb ' smile ', probably also poln. dial, chmlic 
s/i?'sich verfinstern, ein verdrieftliches face machen'. 

References: WP. II 686 f., WH. II 94 f., Trautrnann 270 f., Pedersen ZcP. 17, 31 . 
Page(s): 967-968 

Root / lemma: smeit-, smit- 
Meaning: to throw 



Material: Avestan /75/77/s/a-"niedergeworfen, oppressed' {* ham-[h]mista-, with in Simplex 
erfoigtem Aniautswandel from sm- to {h]m-)\ hamaestar- 'wer niederwirft, oppressed'; 
/775ez?- "throw', with Ablat., *emittere ex'= "mug, rob' {moi&at), with a- "(an sich) come 
lassen' {ami&naiti), with pait'h "*zuruckschicken' = "den Laufpaft give, absagen', with ham- 
"mug, rob' {hemi&yat); with ham+ aibf admit, allow, den Zutritt gestatten'; 

Latin mitto, -ere, mTsi, m/ssum 'go let, run let; send, senden', with expressive 
intensification from *smTtd{*smeitd), compare cosm/ttere Pau\. Fest. 

References: WP. II 687 f., WH II 97 ff. 
Page(s): 968 

Root / lemma: smek- 

Meaning: chin, beard 

Note: in Old Indie with R 

Material: Old Indie smasru-u. "beard, whisker, moustache' (assim. from *sma'sru-)\ 

(through metathesis) Armenian mauruk', moruk' 'beard'; 

alb. mjekre, mjekera, mjekra'dc\\v\, beard' {*smekra)\ 

Note: 

Common alb. shift sm > m, drop of initial s- in alb. 

perhaps Latin mala' mandible, maxilla ', Demin. maxilla {*smek-sla, dessen vowel with
```


## [2026-09-14T02:29:30.143Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'smeit' AHD_watkins1985.txt | head; echo '---WLD---'; grep -n -i 'smeit\\|hamaestar\\|hamista' incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -20; echo '---IEC---'; grep -n -i '^smeit\\|^smit-\\|smeitō' IEC.txt | head"
}
```


### [2026-09-14T02:29:30.225Z] TOOL RESULT

```
958:(s)meit(e)-. To throw. Possibly Latin mittere (first per- son plural present indicative mittimus), to let go, send off, throw: MASS, MESS, MESSAGE, MISSILE, MISSION, MISSIVE, MITTIMUS; ADMIT, COMMIT, (COMPROMISE), DEMIT, DISMISS, EMIT, INTERMIT, INTROMIT, OMIT, PER- MIT, PREMISE, PRETERMIT, PROMISE, REMIT, SUBMIT, SURMISE, TRANSMIT. [Pok. smeit- 968.]
---WLD---
14310:zu germ, snutan „schmeiBen“ (s. dariiber u. srn^i- „schmieren“ und smeitli- 
14338:Auch av. hamisfa- usw. ? s. u. smeith- „werfen‘\ Ganz fraglich alb. (Jokl 
44554:smeid-: got. hismeitan „beschmieren, bestreicben“, „8cbmieren, 
44558:und lat. mitto s. u. smeit- „werfen‘‘), iisml^an „bescbmieren“, ags. hesmltan 
44655:smeit(h)> 
44704:ZfdtWtf. 6, 354 f.) zwei in Betracht kommende Reihen: einerseits hamista- 
44706:Anlautswandel von sm- zu [h]m-), hamistayae{-ca) „niederzuwerfen, zu unter- 
44707:driicken"; hamaestar- „wer niederwirft. iinterdriickt" (vgl. zur Bed. dt. 
44713:fallige Bed.:) „berauben" {Jmni'&yat; vielleicht naher zu hamista-1): mit 
44739:253 mit mitto verglichene germ, Sippe got. hismeitan „bestreichen, be- 
44743:ganz sicher, da eine mit av. mi'&na- verwandte Praes.-Bildung "^smeit-no 
44750:Es diirfte also maed-^ hamista- (doch s. u.) unter idg. snieitQi)- zu 
44756:Y erbindung von hamista- mit aisl. meida „verletzen“ usw. (s. mai-^ matt- 
---IEC---
16422:smit- ‘fling, strike’ Lat. cf. (expressive?) mitto, ére, pf. misi, v. (send; throw; put; have a go' etc.); cf. per- mities, f. ‘destruction’; Ir. smiotaim, v. “chip, shatter; Go. cf. ga-smipon, v. 'fabricate, shape’; aiza-smipa, wm. *bronze-worker'; MHG smit, gs: smides, sm. ‘craftsman, smith’; OE smiþ; ON smiðr, pl. -ar and -ir, id.; Li. cf. smitrùs, adj. ‘crafty’
```


## [2026-09-14T02:29:31.597Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'hamaestar\\|hamaēstar\\|hama[eē]star' BRT.txt | head -20; echo '=== hamista'; grep -n -i 'hamista\\|hamiŝta' BRT.txt | head -20"
}
```


### [2026-09-14T02:29:31.675Z] TOOL RESULT

```
29405:•  j.,  g.  hamaestar-  m.,  j.  hainöistri-  £ 'der,  die  nieder-,  zu  Boden  wirft,  unter- drückt': löi  zl  data  'maEstärö  *a^3mahya "denn  die  sind  die  geschaffenen  Unter- drücker des  A."  Y.  4S.  12;  —  sraos>m  .. yim  dahat  ahurS  .  .  aismahe  'matstär^m Yt.  Jf .  1 5 ;  —  mihnm  . .  'malstänm  pairi- kanqm  Yt  /O,  a6;  —  xh)iha  äzüiti  . .  äsBü ..  -'mifislri  {ADf.y^  Y.16.S;  —  ime  aUe vaca  yH  hanti  avaiähä  drujB ..'ma^ärim (sUtt  NP.)  V,  /o.  1 7 ;  —  äxitlm  hqm.vaintlm .  .  *pfr»tasca  mrvayäsca  'maisiara  (statt ADf.)  Yt  II.  1 5.  a)  mit  Akk.  verbunden: airyamm  i^artra  ..äzlm  'maatanm  (.sXMt ASn.)  dusmainyum  'malstartm  YX.i8.\.
=== hamista
8859:gäiu*saste\t 5. 102.  a)  mit  Gen,  part: hamistayalca  .  ,  kahe  kahyäcU  drvatqm Y.  61. a,.  3)  mit  vorangehendem  Relativ und  folgendem  1)  clt  (hinter  ka-\  2)  ^a (hinter  i kay-)  'Jeder  der..,  quisquis,  qui- cunque',  nur  substantivisch;  1)  nur  gAw.: y3  dalnqm  vokB  *sänsttl  (sd.)  manatthä .  .  kas^l  Y.4p.  5;  —  «ÄJ  ahmäi  yahmai Ulla  (sd.)  iahmäicit  .  .  däyät  akurö  Y. 43- 1 ;  —  at  .  .  s?rao^  jantü  .  .  ahmäi yahmäi  vasi{%A^  Ikahmäi^i'^.  44.16;  — ^ao^anäi/.  .  pailyaogJt  {sA.)  tä  .  .  yä  Tm AuJyätSi/ (sd.)  payät  '.  käclt  (NPn.)  Y. 4tf.8.  2)  yS  lcisca'^>    ahmt   nmsne  .  .
13852:Schöpfung  Übel  ist':  hamistaya^a .  .*anrahe *mainyfu^  matMämanB  'mat0  pouru.mahr- kahe  \.6i.2.~
19691:•  j.  mat.ditnan-  Adj.  'sammt  seinen  Ge- schöpfen, seiner  Schöpfung':  hamistayatca . .  angrake  *mainySul  °manS  duidämanS Y.61.2.
20541:•  j.  miÖTÖ-drug-  Adj.  'den  Mf^ra  be- lügend, betrügend',  auch  sva.  'den  Vertrag brechend'"':  msrsncaiU  vTspqm  dai^kaom mairyS  'druxs  Yt/o.  a;  19;  —  VtspsAu paiti  barszähu  .  .  spass  änAaire  mikraAe ''  drujim  *AispS.S3mna  Yt.  10. 45;  — pdhS. . yim  wnii  'ärup (SP.)  Yt.  10.4$;  i8,  80;  — aspacilySi  *drujam  vazyqstra  (sd.)  bavaintt Yt.  JO.  20;  —  mihrS  .  .  tiaram  'drujqm apqlgavS  dar)zayeiH  Yt/0.48;  —  mi^rtm .  .yö  nöit  kaAmäi  'drujqm  maiyänqm  aojö da\siti  n5il  zävar»  Yt/O.öz;  62,  23,  26, 37%  38.  73,  133.  J-^- 63;  —  hamistayalca ..  mihrB.zyqmca  *'drujimca  Y.  ö';.  3;*Yt .10.82.
29459:•  j.  hamista-  Adj.,  PPfP.:  s.  niaid-. Komp.;  iam-{-mislii',  S  304  II.  40.
29460:•  j.  hamist^e,  hamistayae-i-ii  Inf.  '(und) nieder-,  zu  Boden  zu  werfen,  zu  unter- drücken': frada^äi  vJspaya  asaonö  stsis •tSe  vispayi  drvatö  stsü  Y.  52. 4;  —  °tSe niibirit^e  vJspaya  drvatö  stöiS  Y.  In.  5  '*;  — •tayazca  ntzbiritaya^a  *aurahe  *mainy}us '^.61.2;  2-4"''.
```


## [2026-09-14T02:29:37.925Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"maiÖ-\\|maid-\\|mai0-\\|mai&-\\|maiè-\" BRT.txt | head -20"
}
```


### [2026-09-14T02:29:37.984Z] TOOL RESULT

```
29406:Zum  V.  maid-  mit  ham,  %  JO4  II.  40.  —  mp. hamenär').  —  Pü.  (in  Yt.  7/  und  V.  7/): hamiilir'\  (zu  Y.  48):  hamFslärVi,  (zu  V.  16): hamrslärih  rai;  Sil,  (zu  Y.  4S):  pratipakfah, (lu  Y.  /5):  pratidvanihialAytti,  erl.:  firatighälä- yai;  Npü.:  Aatif.  —  ')  Sp.  62z  No.  5.  — »IDasSWiei^W.öj'.Ssi.  18  mit:  zad  u  hian kunanda  üh ersetzt  wird.
```


## [2026-09-14T02:29:46.356Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo '--- PHD ---'; grep -n -i 'hamest\\|hamēst\\|hamestag' PHD.txt PHD_mackenzie.txt | head -20; echo '--- NYB ---'; grep -n -i 'hamest\\|hamēst' NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-14T02:29:46.431Z] TOOL RESULT

```
--- PHD ---
PHD.txt:125:did ... add other. add dig |YTMAL < А *?{т?1 | N di] yesterday. delete *drém ... (read balgam) drubušt ... add protective. drust [drw(d)st' ... duš-čihr ... add ill-natured. duš-nām [-n^m | (M dwjn'm), N ~] add ill-famed. dušwār [dwáw?l | (M dwjw'r), ... ékanag ... for obedient read loyal, faithful. ~th : for obedience read loyalty, faithfulness. for Farrēbāg... read KFarrēbāy [pinb(^)g] ... frayad |pl(y)d^t' | N faryad] ... delete M pry'd. frazand |prz/znd | ... frusag ... add M prwšg. garódman ... read | P grdm'n. gazdum |gcd(w)m, gzd(w)m |... guftàr ..., ~th : add eloquence. hambar |hm-, hnb] |... add  hamest |hmyst'] whose good and bad deeds weigh equal. ~(ag)an |-(k)^n'] limbo, the neutral station between heaven and hell. delete hammist ..., ~(ag)an ... handarz ... add M °’ndrz. hammoxtan, hammoz-, ~i8n : add learning. hast |TWMNYA < A tmny ; ... add hūg [HZWLYA < A hzyr’; hwk' | M hwg, N xiig] pig. add hūkar(ag) |hwkl(k') | N xükara] porcupine. (not hedgehog) add *huzārag [hwc’lk | N хијага) little, small, few. !jadag ... add fortune. jüdan ... | M jwwdn, jwy- ... add karawuš [kl wš| N ^] wine-press. delete karbunag ... read karbūg |klpwk', klbwk'| lizard. kardagān ... add service (ofthe gods). delete karxēš vds
PHD.txt:392:hamēstār, —ih [hmyst!l, -yh] = hamēmāl, ~ih. hamésag [hmyfk! | M hmyšg, N —a] always. ^h : eternity. ~-86z [-swe] ever-burning. hamē-wahār [hmy whl | N haméfa-bahar] marigold. ham-éwénag [Am'dwynk!'] of the same kind, homogeneous. ham-góhr (hmgwhl! | M hmgwhr] of the same substance or nature, consubstantial. ham-ginag [hmgwnk! | M hmgwng] likewise, so. P hāmharz [A())mAlc | P I? mhyrz] adjutant, attendant. hāmīn [A*myn! |= M] summer. ~ig [-yk'] (of) summer. hāmist [KHDE, v. hammis ; )”mst!] all. ham-kār [hmk’l | N ~] collaborator. 7h : collaboration. hāmkišwar [mkyfwl | M. -wr] universe. hammis [KH DE < A k-hdh), ат... ~: together with. hammist [hmyst'] stagnant, peaceful. ~(ag)an [-(kYn'] limbo, the neutral station between heaven and : hell. vl hammóxtan, hammoz- [ALPWN-tn! < A У "Ip: hmwhtn', hmwc-, Ki hmsoz- | M hmwxtn, N āmēxtan, ámóz-] teach; learn. -išn: teaching. hammdxtar [Amwht?!] learner. ~th: learning. hammóz- , ~i8n, v. hammóxtan. —@йг [kmwcek?l | N āmēzgār] teacher. ham-nibardih [hmnpityh] (single) combat. hamēūģ [/tmwg] equal, like. hámón [k mwn' | N kāmūn] level, flat. hámoyén [/?mwdyn!] all. ham-pursag [hmpwrsk!] consulting, taking counsel. ^h : consultation. ham- |-ránih [Am nyh] battle, combat. ~-samiain [-s"m?n!] contiguous. ~-sardag [-sltk'] of the same kind, like. ~-sayag [-sdk! | N hamsáya) neighbour. ~-tag [-t*k! | N hamid] equal, peer. «tan [-tn'] of the same stature, build. ~=-tihmag [-twhmk'] relative, relation. hamwar [hmwl | N hamwār] level, abreast. hámwiür(ag) [%()mw?/, -k! | N hamwdara] always. ham-zamān [hm ODNA | N —] instantly, immediately. handām [And*m | = P, N andàm] member, limb. handarz [hndle | N andarz] advice, injunction, testament. handarzénidan, handarzén- [hndleyn-ytn!] advise.
PHD.txt:737:adversary hamba/edig, hamémal, hamēstār; ébgat, petyārag.
PHD.txt:2985:opponent hamba/edig, hambasān, hamémil, hamēstār.
PHD.txt:2988:opposition hamémalih, hamēstārīh, padiragih.
PHD_mackenzie.txt:5892:abreast hamwar.                              hamemal, hamestiir; (spiritual)
PHD_mackenzie.txt:7182:   hambun, tis-iz.                        harnemal, hamestar.
PHD_mackenzie.txt:7185:notorious casrnagah, dusraw.           opposition hamernaIih, hamestarih,
PHD_mackenzie.txt:11647:hanmibanlih      "'O~a>~               hamestiir                  ~~
--- NYB ---
1822:hamēstār [hmyst?l] adversary, foe 7214, — Av. (1774) hamaéstar-.
3013:pätan [NTLWN-tn'] päy- [NTLWN., p'dt' = päyet 2512] 1. to guard, to protect, to watch: tan + x“éS be pāyēt: menišn hac dušmat . . . guard yourselves: your think- ing from evil thought (etc.) 65°; vas hamestar činod pdt estend a great many adversaries "keep watch there 724: pat seems to be an abstr. subst. < Olr *pāt?- ‘watch, guard’, cf Arm. lw. pat ‘fence, enclosure’, pat arnul, gal, pat-em, -im ‘to surround, to be surrounded by? — 2. to make a halt, to stay, to remain (zivan- dak apäc pätan 251), to last: 6%. 729, 107°. 205, 2671. 714, — Two vbs. have coalesced here: 1. Av. OP (885 sq.) päy- ‘to protect, to watch’, 2. a den. of pada- ‘place’ (v. pādak): "padayati > SW pāyēt, which has borrowed its inf. from the homonym päyet ‘to watch’. MPrthPrs only have p’dn p’y- ‘to protect’; Paz. id.; NP päyidan in both senses.
```


## [2026-09-14T02:29:48.029Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo '--- HRN p279: leaf=300 ---'; python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(len(leaves))\nfor L in [299,300,301]:\n    print('=== leaf',L)\n    print(leaves[L][:1800])\nEOF"
}
```


### [2026-09-14T02:29:49.151Z] TOOL RESULT

```
--- HRN p279: leaf=300 ---
412
=== leaf 299
- 278 —
aw. gairi- *Berg'; ai. f]firi' 'Berg': ksl. gora,
kurd. gir ^Hügel', girk; wa/. yar, ya/n. gor^ rösn.
jir, siyn, zir, sar. zer.
Wohl in dem Namen ferjistan *Bergland'.
90. ffars 'Haar (vd. 18 (4) GL, 17 (4)), daneben vars
(vd. 6 (12) u. ö.); arm. LW. vars yd/ttf], &piij rpi/ama.
aw. varesa- *Haar .
Np. gurs ist unbelegt (vergl. oben No. 908).
91. gas *Lied\
aw. gä&ä' 'Hymne, Lied'; ai. gdthä-,
92. gat (d. i. gad) 'Keule' (Bund.), vergl. gat\var (aw.
gadavara-).
W. gada- 'Keule* ; skr. gada- *Keule'.
oss. d. yädä, t. qäd 'Baum, Balken, Holz, Wald' (?)
(86).
92***^ gav (geschr. gub) 'Hand' (y. 9 (90)), wohl nur um-
schreibend, vgl. dranggav.
aw. gava- 'Hand' (nur von 'Dämonen'), asengö,gäum ;
hyyvdio Verloben (einhändigen)' (Fick^, 407).
93. garzltan 'klagen, weinen; beichten^)', garz(i)sn,
garz{i)snik 'zu beichten, sühnbar'*).
aw. \/^garZ'^ gerezaiti 'er klagt'; ai. V'^garh-^
gdrhate 'klagen*.
oss. d. yärzun, t. qärzin 'stöhnen (89).
94. geräk 'Ort*.
Die Pazend-Lesung ist jlnäk. Dr. Andreas leitet
das Wort von einer Grundform "^garyaka-, [/gar- 'ver-
sammeln*, gr. dyei()io ab; vergl. ayogä Versammlung,
Markt' (ZDMG. 43, 35 Note 21).
95. gömez 'Kuhurin', arm. LW. gomez 'Seifenkraut,
Ochsenurin'.
aw. gaomaeza- 'Kuhurin*.
Np. kutmz, kimtz, gimiz^ kumiziden, gimlztden
existiren wohl nur in den Wörterbüchern.
96. f/östdän Tleischschale' (für aw. gaolöyor-).
*) Letzteres ritueUer t. t.
=== leaf 300
— 279 —
97. yrav (geschrieben yrüb), vd. 9 (41) (42); vielleicht
nur Transcription.
aw. grava- 'Rohr, Stab'. West, S. B. E., Vol. XVIII,
437 übersetzt strongly* und nimmt also phlv. grav
nicht als aw. grava- entsprechend.
98. gristak 'Loch, Höhle' (für aw. gereda-; Bund.).
99. ffuaftlh ^Gewinn, Erlangung (AV.), guaftak gain*
(West, Dät. din 8, 4).
ai. cyäpti' *das Erreichen, Erlangen*.
100. f/tii)astak Verflucht* (päz. gizasta, gajasfa etc.), Men.,
Guj. Abälis (ed. Barthelemy).
aw. ^eijasta-j vergl. HDüi: (oben No. 1081) und np.
xujeste {oben No. 470).
101. yunierftan 'sich vermischen*, Praes. gumejet (pAz.
gumßz"), gunidj(i)sn (Bund., Aw.-Komm. etc.).
Vergl. np. äme/tefi (oben No. 51); np. gumeze des
BQ ist nicht belegt.
102. yursltan 'hungern' (vd. 9 (182) Gl.).
Derartige Verba sind nicht wenige verloren ge-
gangen, die nicht besonders aufgeführt sind, wie
kam(i)8tan, man(i)stan 'bleiben* etc.
H.
103. häj vor dem Imperativ.
Vergl. Nöldeke, Tabarl-Übersetzung, 385 Note 2.
104. hax 'Fußsohle (vd. 8 (219) (221), 9 (107) GL).
aw. ha/a- 'Fußsohle*.
Da der Kommentator keine Glosse macht, so ist
phlv. ha/ vielleicht noch verstanden worden; doch
steht das Wort an der letzterwähnten Stelle in
Awestabuchstaben.
Dasselbe gilt für lia/t 'Schenkel' (vd. 8 (184), Zend-
buchstaben; 9 (82) ff.), aw. haxti-, ai. sdkthi-^ sakthdn
'Schenkel', oss. t. ayd 'Lende' (7).
105. hamestär Gegner, Widersacher, hamestärih (Men.,
Bund.).
=== leaf 301
- 280 -
ap. vergl. hamiiViya- aufrührerisch' ; aw. Jtamaesttir-
Teind\
106. heimln 'Sommer, hänümk 'sommerlich*, häufig.
aw. harn- ') Sommer, hqmln- 'sommerlich' ; ai. samö-
'Halbjahr, Jahreszeit, Wetter, Jahr; arm. am 'Jahr
(H. No. 10), amarw 'Sommer (H. No. 12); ahd. an. sumar
'Sommer .
kurd. havin (H.-Sch.); sar. menj 'Sommer (aus
^haminaka^?),
107. hamkÖH 'synonym* (wörtl. 'zusammenstossend'), vd. 1
(4) u. ö.
Die Erklärung stammt von Fr. Müller, WZKM.
III, 171.
Composita mit harn- könnten eine ganze Reihe als
verloren gegangenes Sprachgut hier aufgezählt werden.
108. hän 1) alt' (vd. 15 (42) mit Awesta-, sonst mit
PehlevTbuchstaben).
aw. hanä" 'alt*; ai. sdna-; arm. hin (H. No. 168).
2) 'anderer* (päz. han),
ap. aniya- 'anderer; aw. ant/a-; ai. anyd-,
oss. d. t. inne, innä anderer' (140).
109. harvisp, oft verschrieben in harvtst 'all, jeder, sehr
häufig, vergl. haroistm,
ap. haruva- + vtspa-; aw. haurva- + vlspa-; ai.
sdrva- -|- vhjva-.
110. häsr 'Wegmass' (Bund.).
aw. hCL^ra-,
111. häva/nd'^o\Q\\, ähnlich*, päz. havand (P.-Vend., Men.).
aw. cwant' 'solch*.
112. häv(i)8t 'Schüler* (aw. a^&rya- übersetzend u. ö.).
aw. hävista- (y. 68, 12; ZPGl.).
113. hejak 'Eimer* (Kärn. 65 Note 3), vergl. he/tan, ib.
np. he:^ wird als PehlevTwort bezeichnet 2).
^) Zu aw. hama vergl. J. Schmidt, Pluraibildungen 209 folg.;
Bartholomae, Arische Forsch. II, 111, 112. Indog. Forsch. 1, 189, 190.
2) Nichts Neues bei Fr. Müller, WZKM. 5, 257.
```


## [2026-09-14T02:30:13.824Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo '--- NYB hamestagan ---'; grep -n -i 'hamestag\\|hamēstag\\|hamestak' NYB_vol2_glossary.txt NYB_vol1.txt | head; echo '--- SNS ---'; grep -n -i 'hamest' SNS.txt SNS_pages.txt | head -20"
}
```


### [2026-09-14T02:30:13.904Z] TOOL RESULT

```
--- NYB hamestagan ---
--- SNS ---
SNS.txt:4559:^^ ' o*^ J ■ v^j :hamest3r: 
SNS.txt:32630:hamestarlh 53/16 
SNS_pages.txt:2913:                        ^^ o*^ J v^j :hamest3r:
SNS_pages.txt:16187:                      hamestarlh 53/16                      har 215/18              hilld 205/21
```


## [2026-09-14T02:30:15.771Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo '--- MON همیست ---'; grep -n 'همیستار\\|همیستر\\|همیستکان\\|همیستگان' MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -20; echo '--- ARY ---'; grep -n 'همیست' incoming/ARY/ARY_pages.txt | head"
}
```


### [2026-09-14T02:30:15.863Z] TOOL RESULT

```
--- MON همیست ---
--- ARY ---
```


## [2026-09-14T02:30:21.337Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2895,2935p' SNS_pages.txt; echo '=== leaf of that line ==='; python3 - <<'EOF'\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nprint('\\n'.join(lines[:2913]).count('\\f'))\nEOF"
}
```


### [2026-09-14T02:30:22.424Z] TOOL RESULT

```
         u-n/ivJ u-ir/w^ )«v^ Y J>>v; m at V                                          ,


                                                                                                     \:&i&»r't*.i«lS rs 4J so«
                                                                                                                            -f-»>>W amOz:^ III, 49)
        n-n/iv^ .o'jJUimadarSn, 3 My, tl 5 n: ^\.M                                                                              i
                                                                                                                                           i            ]     l
                                                                                                                                                            iS s<)

                                                                                                     [Dkabhar, Essays (On Iranian Subjects,
                                                                                                                                            pp. lOSHi
                                                                                                             JjmW ' *&*jt :abar SraozSd:                                        >«<»).£• j*£          112.
                                                                             A"W»M
                                                                                                         •




                        ^^ o*^ J v^j :hamest3r:
                              '
                                                                                                                                                                                                      •Y/T***        1A

.(*+**) hamastarlr^Wi^. 1774) hamaSstar-,                                                 *«
                                                                                                                         .^T iSinurz                :   jUr^ f-0 o^jl* 1 :amurzisn:                      ^oOt-S'
                                                                             M/Tl
                                                                                                        •o^/j*^ 'o J                /^
                                                                                                                      *o-i*-l'4 :marz / mar^z + a <^r**  £-
                                                                                                      |W£r. Wan. II, 46)      J
 -il>:l 'CJ> J 3 C4i^OwrJ u                                                                                                     mwrz : jilt {AiWb 1152.)
                        *CJ^'0 K^** :hara§staganMr«v-"'*
                                                                                                                                                                                                 .




 .(ij*.^)      hamastagan: L ^-»^l^ U»LT ^ v l^ *5 Li. U                             l
                                                                                                                                                   .f/M*5                n/W^ ./»>• A*; 3murz r4
                                                                              •V'
                                                                                                             r
                                                                                                                 1   —^jo^oUKj »>l                  J ,ur.UI tiw«A4 f b. ibj.1                  :amurdad:Yi»"r       Y»
     £Q                                    U_   __U 4.L    «;i                                                                                                             • l'
=== leaf of that line ===
42
```


## [2026-09-14T02:30:39.350Z] TOOL CALL #25: Bash

```json
{
 "command": "ls site/pages/460.jpg 2>/dev/null; pdftoppm -f 460 -l 460 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg460 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg460.png"
}
```


### [2026-09-14T02:30:40.955Z] TOOL RESULT

```
site/pages/460.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 80591 Sep 13 22:30 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg460.png
```


## [2026-09-14T02:30:40.958Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo '--- MON grep test ---'; grep -c 'کمیسیون' MON_part1.txt MON_part2.txt 2>/dev/null; echo '--- سمع'; grep -c 'سماع' MON_part1.txt MON_part2.txt 2>/dev/null; head -c 400 MON_part1.txt"
}
```


### [2026-09-14T02:30:41.064Z] TOOL RESULT

```
--- MON grep test ---
MON_part1.txt:1
MON_part2.txt:0
--- سمع
MON_part2.txt:24
MON_part1.txt:27
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


هم مشب جج جب بیج چم �
```


## [2026-09-14T02:30:44.268Z] TOOL CALL #27: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg460.png"
}
```


### [2026-09-14T02:30:44.801Z] TOOL RESULT

```

```


## [2026-09-14T02:30:44.798Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T02:30:56.571Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 460 -l 460 -r 300 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg460hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg460hi.png'); print(im.size)\nim.crop((820,940,1800,1120)).save('crop460-shamun.png')\nim.crop((480,1780,1650,1960)).save('crop460-latin.png')\n\""
}
```


### [2026-09-14T02:30:59.027Z] TOOL RESULT

```
(2550, 3300)
```


## [2026-09-14T02:31:01.011Z] TOOL CALL #29: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/crop460-shamun.png"
}
```


### [2026-09-14T02:31:01.024Z] TOOL RESULT

```

```


## [2026-09-14T02:31:06.679Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg460hi.png')\nim.crop((930,1060,2000,1130)).resize((2140,140)).save('crop460-shamunhdr.png')\n\""
}
```


### [2026-09-14T02:31:08.182Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T02:31:10.239Z] TOOL CALL #31: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/crop460-shamunhdr.png"
}
```


### [2026-09-14T02:31:10.293Z] TOOL RESULT

```

```


## [2026-09-14T02:31:10.290Z] INPUT

[Image: original 2140x140, displayed at 2000x131. Multiply coordinates by 1.07 to map to original image.]


## [2026-09-14T02:31:13.635Z] TOOL CALL #32: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/crop460-latin.png"
}
```


### [2026-09-14T02:31:13.650Z] TOOL RESULT

```

```


## [2026-09-14T02:31:16.564Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg460hi.png')\nim.crop((590,2020,1000,2130)).resize((1230,330)).save('crop460-mithere.png')\n\""
}
```


### [2026-09-14T02:31:17.942Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T02:31:19.941Z] TOOL CALL #34: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/crop460-mithere.png"
}
```


### [2026-09-14T02:31:19.959Z] TOOL RESULT

```

```


## [2026-09-14T02:31:26.411Z] TOOL CALL #35: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg460hi.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/460.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -3"
}
```


### [2026-09-14T02:31:26.565Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-14T02:31:26.901Z] TOOL CALL #36: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-14T02:31:26.909Z] TOOL RESULT

```


```


## [2026-09-14T02:31:29.804Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/smeyt-",
 "prompt": "Does this reconstruction page exist? What is the root, meaning, and descendants (Latin mittere, Avestan)?"
}
```


## [2026-09-14T02:31:31.337Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/mitto",
 "prompt": "Give the full etymology section for Latin mittō: what origin does Wiktionary give (de Vaan, unknown etymology?), and does it mention PIE *smeit- or Avestan maēθ-?"
}
```


### [2026-09-14T02:31:34.714Z] TOOL RESULT

```
# Proto-Indo-European Root *smeyt-

Yes, this reconstruction page exists on Wiktionary.

**Root:** *smeyt-

**Meaning:** "to throw"

**Descendants include:**

- **Slavic languages:** Russian метать (metátʹ), Bulgarian мятам (mjatam), Polish miotać
- **Avestan (Iranian):** maēθ- ("throw") and hamista ("oppressed")
- **Latin:** possibly mittō, though the page notes this might alternatively derive from *meyth₂-

The page notes these terms are "not directly attested, but are hypothesized to have existed based on comparative evidence."
```


### [2026-09-14T02:31:37.793Z] TOOL RESULT

```
# Latin *mittō* Etymology

According to Wiktionary, the word likely derives from *mītō* via the "littera rule," tracing back through Proto-Italic *\*meitō* to Proto-Indo-European *\*meyth₂-* ("exchange, remove"), itself an extension of *\*mey-* ("change").

The source notes: "From the original meaning 'to exchange' a semantic shift occurred to 'to give, bestow' and then 'to let go, send'."

**PIE *smeit-**: The etymology mentions this only speculatively. Some scholars reconstruct an initial *s-* based on the hapax *cōsmittō*, which might connect to Proto-Germanic *\*smītaną*, but De Vaan considers this reconstruction unreliable.

**Avestan *maēθ-***: Not mentioned in this article.

The entry provides cognates including Sanskrit *méthati* and Gothic *inmaidjan*, but does not discuss Avestan forms.
```


## [2026-09-14T02:31:49.694Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'maiH\\|maiϑ\\|maiθ\\|hamaēstar\\|hamaestar\\|hamist' CHEUNG.txt | head -20"
}
```


### [2026-09-14T02:31:49.757Z] TOOL RESULT

```
17070:258 *maiH 
17093:*maiH ‘to harm, damage, fade, decrease (?)’ 
17259:OAv. həmióñiiat (Y 53.9); Partic.: perf. pass. YAv. hamista- (Y 8.6); Partic.: perf. pass. YAv. homista- (Y 
56278:*maiH, *maréc, *ras 
56290:*maiH, *narp 
56573:*maiH 
56784:*maiH, *ras, *xsan
```


## [2026-09-14T02:31:52.010Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '17230,17320p' CHEUNG.txt"
}
```


### [2026-09-14T02:31:52.067Z] TOOL RESULT

```
Täuschung’ = DMMPP: 343a 

*KHOTANESE: (+ *fra-) hamäh- (hämä-) ‘to change [intr.]’, (caus.) OKh. hamih- ‘to 
change [tr.] = SGS: 147 

*NEIR: (+ *à- or *ham-) Pash. amleyal ‘to conceal’ 

*SANSKRIT: meth ‘to be opposite’ (RV+), (adv.) mithäs ‘opposite, in opposition’ 
c» EWAia II: 375 

9 On the range of meanings see Insler, l.c. 

«PIE *meitH,- ‘to change position, deviate [esp. in negative sense]’. 0 To be 
separated from the similar (homonymous ?) root for *to throw', which 1s on the basis 
of the semantics certainly justified (contra LIV: Lei © LIV: 431 | Pok.: 715 

*IE COGNATES: Lat. müto ‘I exchange’, Goth. inmaidjan ‘to change, turn into’, OHG 
midan ‘to evade, hide’, OE midan ‘to conceal, avoid, evade’, (pref.) Engl. mis- (e.g. 


mis-use), etc. 
*REFERENCES: Morgenstierne 1942: 262; DKS: 460a f.; Werba 1997: 311; NEVP: 8 


*maidH’ ‘to throw, discard, mittere’ 

*AVESTAN: OAv. mið- (moi0-) ‘to rob, discard, (e)mittere ?’ || (+ *ham-abi-) ‘to con- 
nect, join, admit (entrance), admittere ?’ || (+ *ham-) ‘to throw down’ = Liste: 45 
Aor. athem.: INJ. 3sg. OAv. höm.aibi.möist (Y 46.12), SUBJ. 3sg. OAv. moi0at (Y 46.4), OPT. 35р. 
OAv. həmióñiiat (Y 53.9); Partic.: perf. pass. YAv. hamista- (Y 8.6); Partic.: perf. pass. YAv. homista- (Y 
8.6) 

*NWIR: ? NP mihan (mehan ?) ‘fresh butter; sheep’s milk’ 


*maiz2 ? 261 


*NEIR: ? Oss. I. misyn, D. mesin, Yghn. mesin ‘buttermilk’ (contam. with *maisa- 
‘sheep’) 

© Further (Dir. correspondences are unknown. See also *maiz!. 

«PIE *m(e)itH- ‘to throw, let go’. 0 See *maiß?. > LIV: 430 | Pok.: 968 


*IE COGNATES: Lat. mittere ‘to throw, release’, Toch. B mit- ‘to go; set out’ 
*REFERENCES: Adams 1999: 461 


* maiz! ‘to mix, mingle’ 

*MIDDLE PERSIAN: (+ *а-) MMP ’(’)myz-, BMP ’myc- /améz-/ ‘to mix’, MMP 
’C)myxs- (inch.) ‘to be mixed’ || (+ *ui-) BMP gwmyc- /guméz-/ ‘to mix, mingle’, 
MMP gwmyxs- (inch.) ‘to be mixed, mingled’ = DMMPP: 41b f. 

(+ *а-) Pres.: IND. 3sg. BMP ’mycyt /amézéd/, 3р1. MMP *’myzynd, IMPV. 250. MMP ’myc /amez/; 
Partic.: perf. pass. MMP ’myxtg, MMP ’(’)myxt, Inf: BMP "myhtn /amextan/; Inch./Pass.: pres. IND. 
3sg. MMP *’myxsyd, 3р1. MMP ’myxsynd, MMP ’’myxsynd || (+ *ui-) Pres.: IND. 3sg. BMP gwmycyt 
/gumézéd/, 3pl. BMP gwmycynd /gumözönd/; Partic.: perf. pass. MMP gwmyxtg, (pl) MMP 
gwmyxtg’’n, MMP “gwmyxtg’n; Inf: BMP gwmyhtn /guméxtan/; Inch.: pres. SUBJ. 3pl. MMP 
gwmyxs’nd 

*PARTHIAN: (+ *4-) ’myj- ‘to mix’, "myxs- (inch.) ‘to be mixed with’ || (+ *ш-) 
wmyxs- (inch.) ‘to be mixed’ = Ghilain: 81, 80 | DMMPP: 41b 

(+ *а-) Pres.: IND. 3sg. "myjyd; Partic.: perf. pass. "myxt, ’myxtg; Inch.: pres. IND. 3sg. ’myxsyd, 3pl. 
"myxsynd; Inf.: *’myxtn || (+ *ui-) Inch.: pres. IND. 35р. wmyxsyd; Partic.: perf. pass. wmyxt, wmyxtg 
*SOGDIAN: (+ *ш-) SSogd. wmxsk PN 

*NWIR: (+ *а-) NP amextan/amez- ‘to mix’, Kurd. (Sor.) am&Zän ‘addition; ligature’ 
*NEIR: (+ *uz-) ? Oss. I. yzmis, D. (@)zme(n)sz ‘sand’ (semantically difficult) 
*MISC: Most Iranian forms apparently derive from the (IE) root variant *meig-. NP 
mihan (mehan ?) ‘fresh butter; sheep's milk’, Oss. I. misyn, D. mesin, Yghn. mesin 
‘buttermilk’, which are assumed to contain this root, are probably unrelated. NP 
mihan might contain the root жтаіӨН? ‘to throw, discard’, to which, considering the 
very close meaning, we have to add the Ossetic and Yghn. forms. The latter form 
probably show contamination with the ‘sheep’ *maisa- formation(s), cf. Av. maesi- 
(f.) ‘ewe’, maesina- ‘sheep-, ovine’. 

*SANSKRIT: meks ‘to mix, to mingle’ (RV+) = EWAia II: 373 

«PIE *meik(-s)-, *meig(-s)- ‘to mix, to mingle’ = LIV: 429 | Pok.: 714 

*IE COGNATES: Gr. (e) yvop, nioyo, Lat. misceo, Olrish mescaim, Lith. miesiü 
(miésti) ‘I mix’, etc. 

*REFERENCES: Abaev, Slovar’ II: 123 Ё; Abaev, Slovar’ IV: 281 Ё; Werba 1997: 393; Cabolov 2001: 77 


*maiz” ? ‘to take care, foster ?’
```


## [2026-09-14T02:32:04.794Z] TOOL CALL #41: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py MON:5185 --image 2>&1 | head -40"
}
```


### [2026-09-14T02:32:05.870Z] TOOL RESULT

```
no scan of MON covers printed page 5185 (see 'scans' in refs_online.json)
```


## [2026-09-14T02:32:06.690Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/hamestagan",
 "prompt": "What is hamēstagān, and what etymology is given for the word (Avestan/Middle Persian origin, relation to hamēstār 'adversary' or to hamēst 'equal/mixed')?"
}
```


### [2026-09-14T02:32:07.970Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T02:32:11.227Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%87%D9%85%DB%8C%D8%B3%D8%AA%D8%A7%D8%B1",
 "prompt": "Is there a Persian entry for همیستار? Give etymology and meaning."
}
```


## [2026-09-14T02:32:12.174Z] TOOL CALL #44: WebSearch

```json
{
 "query": "hamēstagān etymology Middle Persian \"hamēstagān\" limbo hamēstag mixed Avestan"
}
```


### [2026-09-14T02:32:12.285Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-14T02:32:19.923Z] TOOL RESULT

```
Web search results for query: "hamēstagān etymology Middle Persian "hamēstagān" limbo hamēstag mixed Avestan"

Links: [{"title":"HAMĒSTAGĀN - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/hamestagan/"},{"title":"Hamistagan - Wikipedia","url":"https://en.wikipedia.org/wiki/Hamistagan"},{"title":"Category:Middle Persian terms derived from Avestan - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Category:Middle_Persian_terms_derived_from_Avestan"},{"title":"- 853 - Chapter 33 Avestan and Old Persian Morphology Prods Oktor Skjærvø","url":"https://allegatifac.unipv.it/caterinamauri/sitovecchio/1972634256_Avestan3a.pdf"},{"title":"HAMÊSTAGÂN - A Place Between Hell and Heaven | CAIS","url":"https://www.cais-soas.com/CAIS/Languages/pahlavi/hamestagan.htm"},{"title":"Hamistagan","url":"https://grokipedia.com/page/hamistagan"},{"title":"graphsearch.epfl.ch","url":"https://graphsearch.epfl.ch/en/concept/63118/concepts"},{"title":"graphsearch.epfl.ch","url":"https://graphsearch.epfl.ch/en/concept/103407/concepts?page=2"}]

Based on the search results, here's what I found about the etymology of hamēstagān:

Hamēstagān is a word of uncertain etymology, used in Pahlavi literature to designate the intermediate stage between paradise and hell. 

It is related to the Avestan hə̄miiasaite, attested in Yasna 33.1, which means "reckoned together," referring to someone "whose defects and virtues are counted together." However, scholars have proposed different interpretations: Gert Klingenschmitt translates the word as "raised together (to the same height)," while David N. MacKenzie interprets it as "the neutral station between the earth and the sky," which should not be compared to "the Limbos," nor the purgatory of Christianity.

In the 9th century Zoroastrian text Dadestan-i Denig ("Religious Decisions"), hamistagan or hamēstagān is a neutral place or state for the departed souls of those whose good deeds and bad deeds were equal in life.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T02:32:30.066Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Hamistagan",
 "prompt": "Give the etymology section verbatim: what is the origin of the word hamistagan / hamēstagān, which Avestan form, which scholars (Klingenschmitt, MacKenzie), and the meaning."
}
```


## [2026-09-14T02:32:32.179Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%87%D9%85%DB%8C%D8%B3%D8%AA%D8%A7%D8%B1/",
 "prompt": "What do Dehkhoda and Mo'in say about همیستار? Give the definitions and any etymological tag."
}
```


### [2026-09-14T02:32:34.005Z] TOOL RESULT

```
I cannot provide the etymology section verbatim as requested because **no etymology section exists in the Wikipedia article provided**. 

The article contains no information about:
- The origin of the word hamistagan/hamēstagān
- Which Avestan form it derives from
- Scholars such as Klingenschmitt or MacKenzie
- The linguistic etymology or meaning derivation

The article begins directly with the definition: "hamistagan or hamēstagān is a neutral place or state for the departed souls of those whose good deeds and bad deeds were equal in life."

To find etymological information, you would need to consult other sources, such as the Encyclopædia Iranica or specialized linguistic references on Zoroastrian texts.
```


### [2026-09-14T02:32:35.957Z] TOOL RESULT

```
I cannot find specific definitions or etymological information from Dehkhoda and Mo'in dictionaries in the provided content. 

The page mentions that the Abadis dictionary includes "لغتنامه دهخدا، فرهنگ معین" (Dehkhoda dictionary and Mo'in dictionary) among its resources, but it does not actually present their individual definitions of "همیستار."

The only definition provided is from "نایسکان" which lists "همیستار" as having meanings related to opposition and enmity, but this source attribution is not attributed to either Dehkhoda or Mo'in.
```


## [2026-09-14T02:32:43.449Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg460hi.png')\nim.crop((1750,1820,1960,1940)).resize((840,480)).save('crop460-fa.png')\n\""
}
```


### [2026-09-14T02:32:44.847Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T02:32:44.920Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://www.cais-soas.com/CAIS/Languages/pahlavi/hamestagan.htm",
 "prompt": "Give the etymology of hamēstagān as stated: which Avestan form, which scholars, and what it means. Quote the key sentences."
}
```


### [2026-09-14T02:32:50.685Z] TOOL RESULT

```
# Etymology of Hamēstagān

**Avestan Form:** The word relates to Avestan *həmiiasaite*, found in *Yasna* 33.1.

**Key Scholars and Interpretations:**

Helmut Humbach defined it as "reckoned together," applying to "the one whose defects and virtues are counted together." Gert Klingenschmitt proposed an alternative rendering: "raised together (to the same height)." David N. MacKenzie offered another perspective, interpreting it as "the neutral station between the earth and the sky."

**Primary Definition:**

The article states that scholars disagreed on exact meaning. The most established sense comes from Humbach's analysis: the concept involves "defects and virtues are counted together," reflecting the intermediate state assigned to souls whose moral accounts balance equally.
```


## [2026-09-14T02:32:52.674Z] TOOL CALL #49: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/crop460-fa.png"
}
```


### [2026-09-14T02:32:52.694Z] TOOL RESULT

```

```


## [2026-09-14T02:33:02.479Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo '=== FVQ Ismail ==='; grep -n -i \"ism[aā]'?[īi]l\" FVQ_pages.txt | head -10; echo '=== FVQ sami ==='; grep -n -i 'samiʿa\\|sami.a' FVQ_pages.txt | head -5"
}
```


### [2026-09-14T02:33:02.550Z] TOOL RESULT

```
=== FVQ Ismail ===
=== FVQ sami ===
```


## [2026-09-14T02:33:05.236Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A5%D8%B3%D9%85%D8%A7%D8%B9%D9%8A%D9%84",
 "prompt": "Arabic إسماعيل: give the etymology (Hebrew יִשְׁמָעֵאל Yishmaʿel, via Syriac?), meaning 'God hears/hears God', and the Persian descendant."
}
```


### [2026-09-14T02:33:10.712Z] TOOL RESULT

```
# Etymology and Descendants of إسماعيل

**Etymology:**
The Arabic name إسماعيل derives "From Hebrew _יִשְׁמָעֵאל_ (yishma'él), from _יִשְׁמַע אֵל_ (yishmá' 'él, 'God heard')." The name combines elements meaning "hears" and "God," conveying the sense that God has heard.

**Persian Descendant:**
The entry documents that this name passed into Classical Persian as اِسْمَاعِیل (ismā'īl), which subsequently influenced various South Asian languages including Tajik, Hindi, Urdu, and Punjabi adaptations.

The name appears prominently in Islamic tradition, referenced in the Qur'an as the son of Abraham who assisted in raising the foundations of the Ka'ba.
```


## [2026-09-14T02:33:15.424Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo '=== FVQ Isma ==='; grep -n 'Isma' FVQ_pages.txt | head -10; echo '=== FVQ Shama/shama ==='; grep -n 'Sham.un\\|Simeon' FVQ_pages.txt | head -5"
}
```


### [2026-09-14T02:33:15.510Z] TOOL RESULT

```
=== FVQ Isma ===
2014:to the effect that it has been vocalized on the analogy of Isma'll
2618:(Ismail).
=== FVQ Shama/shama ===
1155:Simeon of Beth Arshani, 3 though the predominant party there was
1174:p. 140. Theso converts of Simeon are said to have been brought back to the orthodox
```


## [2026-09-14T02:33:17.251Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%D9%85%D8%B9%D9%88%D9%86",
 "prompt": "Arabic/Persian شمعون: etymology (Hebrew Shimʿon via Syriac Shemʿun / Greek Symeon?), meaning, and any Persian entry."
}
```


### [2026-09-14T02:33:21.924Z] TOOL RESULT

```
# شمعون (Shamʿūn)

Based on the Wiktionary entry, here's what the page documents:

**Etymology**: The word is "borrowed from Hebrew _שִׁמְעוֹן_ (šimʕōn, 'Simon'), originally a patronymic." It's also noted as a doublet of two other Arabic forms representing different borrowing periods.

**Pronunciation**: /ʃam.ʕuːn/

**Definition**: The entry identifies شمعون as "a surname from Hebrew, equivalent to English Simon" and notes it can function as masculine or feminine depending on context.

**Descendants**: The term evolved into French "Chamoun," which then entered English with the same spelling.

The page indicates this represents a Semitic name that traveled through multiple languages—from Hebrew origins through Arabic, into French, and subsequently into English—maintaining recognizable phonetic similarities across these linguistic borrowings.
```


## [2026-09-14T02:33:28.560Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2608,2625p' FVQ_pages.txt; echo '--- leaf of 2618 ---'; python3 -c \"\nt=open('FVQ_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nprint('\\n'.join(lines[:2618]).count('\\f'))\n\""
}
```


### [2026-09-14T02:33:29.700Z] TOOL RESULT

```
religious significance, 1 as e.g. fl^tt /2?> etc. The same sense is found
in the Kabbinic writings (Horovitz, KU, 55), but it is particularly
in Syriac that we find j^] used precisely as in the Qur'an, e.g.
" he devoted himself to God and His
Church ", or -ooim2U OlL^ oVnV^. 2 and one feels confident in
looking here for the origin of the Arabic word.
J
*, of course, is a formation from this, 3 and was in use in
pre-Islamic Arabia. *y<**\ however, would seem to have been
formed by Muhammad himself after he began to use the word.
(Ismail).
ii, 119-134 ; iii, 78 ; iv, 161 ; vi, 86 ; xiv, 41 ; xix, 55 ; xxi, 85 ;
xxxviii, 48.
Ishmael.
The Muslim philologers early recognized that it was non- Arabic,
as is clear from Zam. on xix, 55, and from its being treated as non-
Arabic by al-Jawaliqi, Mu'arrab, 9 ; al-KhafajT, 10; as-SuyutT, Muzhir,
1 Robertson Smith, Religion of the Semites, 79 ff.
--- leaf of 2618 ---
80
```


## [2026-09-14T02:33:30.502Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D9%85%DB%8C%D8%B3%DB%8C%D9%88%D9%86",
 "prompt": "Persian کمیسیون: etymology (borrowed from French commission?), meaning. Also any mention of کمیته from French comité."
}
```


### [2026-09-14T02:33:35.924Z] TOOL RESULT

```
# Persian Word: کمیسیون (Komisiyon)

## Etymology
The word is "Borrowed from French _[commission](/wiki/commission#French 'commission')_." It traces back through Latin _committō_ and ultimately to Proto-Indo-European roots.

## Meanings
The term has two primary definitions:

1. **Commission** - "fee charged by an agent or broker for carrying out a transaction," with the synonym حق‌العمل (haqq-ol'-amal)

2. **Committee/Commission** - A group or body, with related synonyms هیئت (hey'at) and کمیته (komite)

## Related Term
The page also references **کمیته** (komite), which appears to be another Persian term for committee, though the content doesn't explicitly confirm whether it's also borrowed from French *comité*.
```


## [2026-09-14T02:33:45.047Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2625,2650p' FVQ_pages.txt; echo '=== ARY ==='; grep -n -i 'SMEIT\\|MITTERE\\|کمیسیون' incoming/ARY/ARY_latin_index_pages.txt incoming/ARY/ARY_pages.txt 2>/dev/null | head"
}
```


### [2026-09-14T02:33:45.120Z] TOOL RESULT

```
1 Robertson Smith, Religion of the Semites, 79 ff.
2 The example given by Horovitz, viz. OO1
is curiously like <jrdUl L>
3 Sura, li, 36 ; xxii, 77 ; and note Bagh, vii, 192, and Ya'qubl, 7/tVrf, i, 259, and
its use in Safaito (RvckmaiiK, Nmns propres, i, 239).64 FOREIGN VOCABULARY OF THE QUR'AN
i, 138. Various forms of the name are given J^*^ I ; +*" \ ; A
and Ju^U^l, the ^ in this last form, quoted from Sibawaih in Muzhir,
i, 132, being significant.
A Christian origin for the word is evident from a comparison
of the Gk. 'I(j/ia^A ; Syr. Vu^iQ*] ; Kth. ftfr'VJt.A, with the Heb.
7X17Q2T. A form derived from Heb. occurs in the inscriptions of
both the S. and N. of the Peninsula. 1 In S. Arabia we* find in a
Himyaritic inscription 1h3 A? 2 - ^NJJQO'' (cf. Eth.
and in the Safaite inscriptions of N. Arabia we find a form
It is thus clear that the form with initial * was well enough known
in Arabia before Muhammad's day, but on the other hand, there seems
to be no evidence that the form used in the Qur'an was in use as a
personal name among the Arabs in pre-Islamic times. 4 The fact
that in the Qur'an we find cJu-j^for ^JOV and CJJ.AA> for DplT,but
J for ^infiP and J-uH for ^KSTKOf], just as in Syr. we find
and >OQ^, but JfiCU and '^j.LSQ*] makes it
reasonably certain that the Qur'anic form came from a Syr. source, 6
and the form ^ A S V)fln) in the Christian Palestinian dialect removes
any difficulty which might have been felt of ^ for
1 I). H. Miiller suggests that the name is an independent formation in S. Arabian
(WZKM, iii, 225, being followed in this by Horovitz, .IPS, 155, 15C), but this is a
=== ARY ===
```


## [2026-09-14T02:33:46.407Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/%D8%B3%D9%85%D8%B9",
 "prompt": "What does Mo'in's dictionary say for سمع — origin tag (Arabic?) and meaning?"
}
```


### [2026-09-14T02:33:49.830Z] TOOL RESULT

```
# Mo'in's Dictionary Entry for سمع

According to the content, Mo'in's dictionary provides the following information:

**Origin:** The entry is marked with "[ع.]" indicating an **Arabic origin**.

**Meanings:** The dictionary lists two definitions:
1. "گوش ، حس شنوایی" (ear; the sense of hearing)
2. "شنیدن" (to hear), marked as a verbal noun form

The entry notes this is from "فرهنگ انتشارات معین" (Mo'in Publishing Dictionary).
```


## [2026-09-14T02:34:03.802Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/mission",
 "prompt": "Give Etymonline's etymology of 'mission' and of Latin mittere — what PIE root or origin does it give?"
}
```


## [2026-09-14T02:34:05.804Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D7%A9%D7%9E%D7%A2",
 "prompt": "Hebrew שמע: give the root ש־מ־ע, meaning 'to hear', and any Semitic cognates listed (Arabic سمع, Aramaic, Akkadian, Ugaritic)."
}
```


### [2026-09-14T02:34:09.180Z] TOOL RESULT

```
# Etymology of "Mission" and Latin "Mittere"

**Mission's Etymology:**
The word "mission" comes from 1590s, originally referring to "a sending abroad" of Jesuits. It derives from Latin *missionem* (nominative *missio*), meaning "act of sending, a dispatching; a release, a setting at liberty."

**Latin Mittere's Origin:**
The Latin verb *mittere* means "to release, let go; send, throw." According to the source, it traces back to a Proto-Indo-European (PIE) root: **\*m(e)ith-**, which signifies "to exchange, remove."

**Supporting Evidence:**
The etymological entry notes that "from original 'exchange', the meaning developed to 'give, bestow' ... and 'let go, send.'" The same PIE root also produced related words in Sanskrit (*methete*, *mimetha* meaning "to become hostile, quarrel") and Gothic (*in-maidjan* meaning "to change"), demonstrating the root's widespread linguistic influence across Indo-European languages.
```


### [2026-09-14T02:34:10.217Z] TOOL RESULT

```
# Hebrew Root ש־מ־ע (sh-m-ʿ)

**Meaning:** "to hear"

**Semitic Cognates:**

The Wiktionary entry identifies the following cognate:

- **Arabic:** سَمِعَ (samiʿa, "to hear") - described as cognate with the Hebrew verb through their shared Proto-Semitic origin *šamiʕ-

The entry notes that both the Hebrew and Aramaic versions of this root are "inherited from Proto-Semitic *šamaʕ-," establishing their common linguistic ancestry. However, the document does not list Akkadian or Ugaritic cognates for this particular root entry.
```


## [2026-09-14T02:34:22.655Z] TOOL CALL #60: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/smeyt-\" \\\n \"https://en.wiktionary.org/wiki/mitto\" \\\n \"https://en.wikipedia.org/wiki/Hamistagan\" \\\n \"https://www.cais-soas.com/CAIS/Languages/pahlavi/hamestagan.htm\" \\\n \"https://en.wiktionary.org/wiki/%D8%A5%D8%B3%D9%85%D8%A7%D8%B9%D9%8A%D9%84\" \\\n \"https://en.wiktionary.org/wiki/%D8%B4%D9%85%D8%B9%D9%88%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%DA%A9%D9%85%DB%8C%D8%B3%DB%8C%D9%88%D9%86\" \\\n \"https://vajehyab.com/moein/%D8%B3%D9%85%D8%B9\" \\\n \"https://abadis.ir/fatofa/%D9%87%D9%85%DB%8C%D8%B3%D8%AA%D8%A7%D8%B1/\" \\\n \"https://www.etymonline.com/word/mission\" \\\n \"https://en.wiktionary.org/wiki/%D7%A9%D7%9E%D7%A2\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 460 (S.m.`a / Smeit) verification\" 2>&1 | tail -1\ndone"
}
```


### [2026-09-14T02:34:23.737Z] TOOL RESULT

```
Exit code 1
(eval):14: unmatched "
```


## [2026-09-14T02:34:30.190Z] TOOL CALL #61: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/smeyt-\" \\\n \"https://en.wiktionary.org/wiki/mitto\" \\\n \"https://en.wikipedia.org/wiki/Hamistagan\" \\\n \"https://www.cais-soas.com/CAIS/Languages/pahlavi/hamestagan.htm\" \\\n \"https://en.wiktionary.org/wiki/%D8%A5%D8%B3%D9%85%D8%A7%D8%B9%D9%8A%D9%84\" \\\n \"https://en.wiktionary.org/wiki/%D8%B4%D9%85%D8%B9%D9%88%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%DA%A9%D9%85%DB%8C%D8%B3%DB%8C%D9%88%D9%86\" \\\n \"https://vajehyab.com/moein/%D8%B3%D9%85%D8%B9\" \\\n \"https://abadis.ir/fatofa/%D9%87%D9%85%DB%8C%D8%B3%D8%AA%D8%A7%D8%B1/\" \\\n \"https://www.etymonline.com/word/mission\" \\\n \"https://en.wiktionary.org/wiki/%D7%A9%D7%9E%D7%A2\" ; do\n python3 tools/fetch_source.py \"$u\" --note 'page 460 Smeit and Semitic sh-m-a verification' 2>&1 | tail -1\ndone"
}
```


### [2026-09-14T02:34:36.499Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/13ee8bf0b79f1586.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/24eb5973b1b74dae.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0a411ea5b813ed0c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e396d33e2ee03576.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a16234e901e406e4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/75ba37ae0cd5ac7f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4e8423fe70bd93a4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8c010ec5930ceb38.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/df563455eaec869d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e3e27e8da00c4eb0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6dceed5f8f770c75.txt
```


## [2026-09-14T02:34:47.106Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo '=== SKT mission ==='; grep -n '^mission\\|^Mission\\|^commit' SKT.txt | head -5; echo '=== LAT mitto ==='; grep -n '^mitto' LAT.txt | head -3; echo '=== LEW mitto ==='; grep -n '^mitto\\|mitto,' LEW_1910.txt | head -5; echo '=== SYN send ==='; grep -n 'smeit\\|mitto' SYN.txt | head -5"
}
```


### [2026-09-14T02:34:47.210Z] TOOL RESULT

```
=== SKT mission ===
11705:mission.  (L.)  [The  O.  F.  mission merely  nneans  •capcnce;' Cot].  — L.  ace missionem,  ace  01  missio,  a  sending.  — L. missus,  pp.  of  mitUrt^  Xo  sex^
=== LAT mitto ===
38403:mitto, omitto, permitto "laisser passer a travers", praetermitto,
38458:mitto: laisser un intervalle entre, d'ou, interrompre, cesser; dmitto:
=== LEW mitto ===
=== SYN send ===
13991:ME, NE smite (now only rhet. or poet.), fr. OE smitan ‘smear’ : OHG (be) smizan, MHG smizen ‘stroke, smear’, MHG also ‘strike’, NHG schmeissen ‘throw, hurl’, dial. ‘strike’, Goth. bi- smeitan, ga-smeitan ‘annoint’, prob. fr. an extension of *smé(z)- in Grk, cpaw, ouhxw ‘wipe off, cleanse’, etc. Walde-P. 2.685f. Falk-Torp 1081. Feist 96. Semantic development in Gmc. compli- cated and difficult (for ‘throw’ in NHG schmeissen cf. Paul, Deutsches Wtb. s.v.), but ‘strike’ prob. fr. ‘smear through ‘stroke’. Cf. the following and also the current slang use of NE smear in U.S. sports reporting (= ‘knock out, put out of action’).
```


## [2026-09-14T02:34:49.641Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo '=== BQT v4/v5 همیست ==='; grep -n 'همیست' incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v5_pages.txt 2>/dev/null | head -5; echo '=== BQT سماع ==='; grep -c 'سماع' BQT_v2_pages.txt 2>/dev/null; echo '=== PLA ==='; grep -n -i 'hamest\\|سماع' incoming/PLA/PLA_pages.txt | head -5; echo '=== AFM ==='; grep -n 'سماع\\|شمعون' AFM_pages.txt | head -5"
}
```


### [2026-09-14T02:34:49.751Z] TOOL RESULT

```
=== BQT v4/v5 همیست ===
=== BQT سماع ===
4
=== PLA ===
=== AFM ===
409:(المبر) الأسد المندي 5 في شفاء 0 +ابر جسن :من السماع دخيل في
```


## [2026-09-14T02:34:55.827Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'mittō\\|mitto,\\|^mitto' LAT.txt | head; echo '---'; sed -n '38395,38420p' LAT.txt; echo '=== LEW search ==='; grep -n 'cosmittere\\|mitto' LEW_1910.txt | head"
}
```


### [2026-09-14T02:34:55.915Z] TOOL RESULT

```
17316:le pcp. eat perditus. Different de amitto, cf. Rhet. Heren. Decius amisit
22213:-commissarius, fide(i)promitto, -promissor, fidiiubeB et fidiiussor,
28621:hostimentum adiungito', Pl., As.377, quin promitto, inquam, hostire
38402:quartier", dans les composta admittd, amittd, demitto, emittS, inter¬
38403:mitto, omitto, permitto "laisser passer a travers", praetermitto,
38404:pronitts, remitto, submitto, transnittd (trd-), Cf. encore missus,-us
38458:mitto: laisser un intervalle entre, d'ou, interrompre, cesser; dmitto:
38460:mamilla)', sur omitto, v.Havet, Man. 0 aOs; permitto: envoyer a travers,
40664:1,45,199, quos ego ope mea | pro incertis certos... f dimitto, ut
42680:ostendS, obmoueo (arch .), ommento (ii.), omitto, oppilo, etc.;l*idee
---
laisser partir, lacher, lancer", et, avec un infinitif "omettre de,
cesser de"; au sens moral "omettre, passer sous silence"; par suite
"envoyer". Le sens premier est bien atteste, cf.Pl., Ru.1015, mitte
rudentem, sceleste, — mittam; omitte uidulum; Hor., A.P.476, mittere
cutem, et 1 es expressions missum facere aliquem, manu missio; Pl.
Au.651, iam scrutari mitto; Cic., Mur.15,33, mitto proelia, praetereo
oppugnationes. C'est ce sens qu’on trouve dans missio "renvoi, cong£,
quartier", dans les composta admittd, amittd, demitto, emittS, inter¬
mitto, omitto, permitto "laisser passer a travers", praetermitto,
pronitts, remitto, submitto, transnittd (trd-), Cf. encore missus,-us
m. "fait de laisser aller", d*ou "lancer (d'une floche, etc.)",et
"course de chevaux"; missum,-1 n. (et missdrium): prix, a©\ov (Gloss.);
missilis, et missibilis (tardif) "qu'on lance", et missile n. "arme
de jet", missilia n.pl. "cadeaux qu 1 a 1’occasion de certaines fetes
on r^pandait dans le publie", missicius (miles) "soldat libare".
De mittendus : mittendarius (Ruf., Cod.Theod.): fonctionnaire envoye
pour percevoir 1’impot.
Le sens de "envoyer" est derive, bien qu'attest<? depuis Ennius
(ap. Cic.Tu.3,13,88) et a du se developper dans des emplois comme mittere
equos, Varr., L.L.4,153, etc„; Plaute cree un fr^quentatif missiculo
(Ep.138), sans autre exemple, semble-t-il. A basse epoque mittere
apparait sp^cialis^ dans le sens de "envoyer a table, mettre a table",
d'ou missus,-us "service" Lampr. Hei.30, Capitol.Pertin.i8; missSrium
"piat" (glosant ferculum, lanx) et dans les 1. romanes missus "mets",
cfiM.L.5611,5618, mittere "mettre" 5616. Pour missa "messe", v.l'article
spe ci al.
=== LEW search ===
```


## [2026-09-14T02:34:58.400Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '38420,38460p' LAT.txt"
}
```


### [2026-09-14T02:34:58.465Z] TOOL RESULT

```
spe ci al.
Composes: amitto: laisser s^chapper ou s'^loigner. Quod nos dicimus
dimittere, antiqui etiam dicebant amittere, D0n.Haut.480 (cf.Pl.Mi.
1096); par suite "perdre" (different, tout au moins a 1'origine, de
perdere "envoyer a sa perte, d^truire, perdre irr<?m <5 di abi ement " ,
omittere "abandonner, omettre");
admittS: laisser 3'approcher (sens local dans la 1 . augurale, cf.
P1 .,As.859, quouis admittunt aues), admettre, M.L.178; d'ou "laisser
faire" (fieri pati dit Donat, Eun.761); de la admittere in se (culpam)
(diff 4 r 6 nt de committere, qui indique 1'acte criminel accompli ouver-
tement, punissable par la loi civile) "se rendre coupable (par fai-
blesse)"; dans la 1. augurale "permettre"; admissiuae aues; dans la
l.des ^leveurs, conduire le male a la femelle (oppose a submittere),
d* ou admissarius (armissarius), M.L. 177, cf. gall. amws (de equo)"; ad¬
missio, admissura;
circummitto: envoyer de tous cotes;
committo: -ere proprie est insimul mittere; nunc eo utimur et pro
facere, aut pro linquere, aut pro incipere, P.F.36,4; mettre ensemble
ou aux prises; d'ou "comparer" et aussi "confier, remettre a quelqu^n".7 as
modius
- De committere legiones (e.g. Hirt.B.G.8,26, neque infimas legiones
hostibus committere uellent) on a dit committere pugnam, et c'est
ainsi qu 1 a du se developper le sens de "commencer, entreprendre",
"risquer", qui s'est specialise dans un sens pejoratif (cf, commereri)
"commettre une faute", cf. Don.Ad.159, committet: perficiet, sed hoc
proprie de illicitis et puniendis facinoribus dicimus', Prisc. GLK
II 404,1, committo : pro credo et pecco. De la committere ut "commettre
la faute de, s'exposer a ce que"; commissum "faute, delit", M.L,aoOsa.
- Panroman, M.L.qo86. Au sens premier de committo se rattachent com-
missii : t. technique "c^lebration des j eux" (proprement "fait de confier
les jeux a quelqu'un "). Puis dans la 1 .eccl."engagement". Confondu
avec commissum et avec commissura: assemblage, jointure, raccordement;
et "fissure" (= rima), M.L.aoBsb;
demitti: laisser tomber, baisser, fermer (les paupibres); dimitto:
envoyer dans des sens opposes, renvoyer; emitto: laisser s'echapper,
emettre; Emissarius: 4 missaire, et aussi doublet tardif de admissarius,
sans doute dfaprbs emissio seminis ; SmissSrium: canal d'^coulement;
emissicius (Pl.)j inmitti: lacher sur ou dans, envoyer dans; inter¬
mitto: laisser un intervalle entre, d'ou, interrompre, cesser; dmitto:
laisser echapper, omettre (de *obnitto > *ommitto > initti, cf. mamma,
mamilla)', sur omitto, v.Havet, Man. 0 aOs; permitto: envoyer a travers,
```


## [2026-09-14T02:35:02.120Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '38460,38500p' LAT.txt"
}
```


### [2026-09-14T02:35:02.186Z] TOOL RESULT

```
mamilla)', sur omitto, v.Havet, Man. 0 aOs; permitto: envoyer a travers,
laisser aller, permettre; praetermitti: laisser passer (cf. praetereo);
promitti : mettre ou envoyer en avant. Dans la 1 . augurale, synonyme
de portendi "mettre devant les yeux" (cf. dans Pl. Poe.1205 et 3.309
1'emploi de portentumst et de promisit)', puis dans la 1. commune "pro-
mettre, s'engager" (syn. de pol liceor). Anci en, usuel. Conservi! sous
des formes savantes dans les 1 . romanes. M.L.6775. Le caractbre ori-
ginairement religieux de primitto est visible dans la phrase du SC.
Bacch.: neue post hac inter sed conioura\_se neu]e ccmuouise neue
conspondise neue conpromesise uelet neue quisquam fidem inter sed
dedise uelet. De la promissor (Hor.A.P.134 = eKa.yye\xr\i); compromitti
t. de droit "s'engager reciproquement a remettre la d^cision d'une
affaire a un arbitre; compromettre"; compromissum,-i n., et repri¬
mi 11 i .
remitto: renvoyer, relacher, faire remise de, M.L.7197.
submitti: mettre sous, envoyer sous (cf .admitto); soumettre, M.L.
8 38».
transmitti, tramitto: envoyer au dela; faire passer, transmettre;
et aussi, passer, traverser (cf. traduco, transeo), M.L.8849.
Le present mitti, k cote du perfectum misi, ne peut etre qu'une
forne expressive a consonne interi eure g<!min<!e. Pas d*etymologie
sure. Le groupe de got. b i-smei t an " E7u.)(pi, elv" est trop loin pour le
sens. On rapproche de maniere seduisante une racine iranienne qui
a un 9 repr^sentant th, consonne expressive comme le -tt- de mitto:
av. maeQ~ que Bartholomae traduit justement par mittere.
modius, -I m. (modium n.): mesure (de capacit^ pour corps secs),
boisseau; mesure de surface <?gale au 1/3 du iugerum (sens rare); dans
la 1 . nautique, trou ou 8'emboite le pied d'un mat. Ancien, technique.
M.L.5639, Germ.: v.h.a .mutti, etc.; celt. : iri .buide, muide.
Derivas: modiali S; modiatio (Cod. Theod.), M.L.5S36; modiolus: petite
mesure. Usite dans de nombreuses acceptions techniques: moyeu, ba-
rillet, trepan, etc., cf. Rich, s.u. M.L.5638 et 5637 *modiolum.
Composes: semodius (v.s&mi-)} M.L.9709-10, sesqui-, tri-, decem¬
modius .
Modius serable etre a modus comme du-pundius, -dium k pondus.modus
- 736 -
V. medeor.
modus, -I m. (contamination de deux noms differenta; l'un, de aena
abstrait et de genre anime, a vocalisme en o, modus ; 1 'autre, de sena
concret et de genre inanime, a vocalisme en -e-, medos, atteste
in directement par le derive modestus [cf.scelus, sce lestus ], et par
```


## [2026-09-14T02:35:50.673Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '44650,44715p' incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt"
}
```


### [2026-09-14T02:35:50.725Z] TOOL RESULT

```
\bX. mirus „wunderbaF' (Bildung wie darns ^ — sd. smB^a^ nicht nach 
Pedersen IF. 5, 41 = abg. smichz ; die Deutung von lat. cmiis^ Daenosinschr. 



smeit(h)> 


687 


cosmis als „niit Lacheln'^, von einem Wznomen smi-^ Vf. LEWb.^ s, v., ist 
bestritten; Fay IP. 26, 40 mit A. 1 setzt es = gr. x6o/j,ig; Ehrlich z. idg. 
Sprg. 75, BPhW. 1911, 1574. Solmsen Jagic-Festschr, 580 verbinden es 
mit ai. mayd- „Kunst, Wunderkraft“, das aber mit maya „Yerwandlung, 
Tauschung usw.'^ und andern imter ma- „winken“ erwahnten Worten zu- 
sammengehort, also aus dem BegrifF des gauklerischen, triigerischen Kunst- 
stiickes geflossen ist, vrelche Bed.-Farbung in minis kaum zugrunde liegt); 

mengl. srmlin^ engl. smile^ dan. norw. smile „lacheln'‘; ahd. fe 2 >//i 6 r.„Spott“, 
tismeron „ver8potten“; sehr fraglich (nach Uhlenbeck PBrB. 26, 570 f.) ags. 
mticere „Lippe“ i^smairia^, Eher nach Zup. KZ. 37, 401, Pedersen KG. I 
86 als "^smdhria- zu lit. smakrd „Kinn‘‘ usw.), galsni^re „zam Lachen ge- 
neigt'‘, womit auch dan. norw. smcere „Klee‘^ identisch ist (s. Falk-Torp s. v. 
gegen andere Deutungen); 

lett. smeju^ smiet ,,verlachen‘', smaldi „das Lacheln“ (im -d- wohl mit 
dem Gr. zu vergleichen) ; 

abg. smejq^ smijati sq „lachen“, smech^ „das Lachen''. 

Khd. schmeicheln^ mhd. smeiclieln ds., aber zu norw. mdartl. smika „streichen, 
glatten", aisl. smeikr ,,glatt, schuchtern", s. Wood Men. 22, 236. 

Curtins 328, Pick I ^ 151, 575, 111^ 529 usw. 

Daneben smeu- in: 

mhd. smieren^ smielen^ alter ndl. smitylen „lacheln“, wohl auch mhd. smollen 
„aus Unwillen schweigen. schmollen; lacheln" [von Sutterlin IP. 29, 126 nicht 
uberzeugend als ^smeush, smnzh mit gr. avco C^uvaco^.) „schlie6e mich“ 
(vom Munde) verbunden] ; russ. u-chmyVdhsa „lacheln, schmuiizeln", mund- 
artlich chmylith „lacheln“, wohl auch poln. mdartl. climidic sic „sich ver- 
finstern, ein verdriefilichesGesichtmachen, traurig werden". IJhlenbeckPBrB, 
22, 199; 26, 308, Berneker 391, Pick III^ 531, s. auch Falk-Torp u. smile. 

Gleichsetzung unserer Wzln. mit smi-, smu- ,,reiben" (Falk-Torp aaO. 
und unter smorblid nach Wood [AlPh. 20, 260 f.]) wird durch die Bed. 
nicht empfohlen; Yerwandtschaft mit der Lautgebarde mu- (s. o. zu yvoS) 
ist auch fur smeii- mindestens gaiiz nebeihaft. 

sineit(h)- „werfen“. 

Das Avest. bietet (s. Bartholomae Airan. ^Yb. 1 105 f., IF. 19 Beitr. 202fF., 
ZfdtWtf. 6, 354 f.) zwei in Betracht kommende Reihen: einerseits hamista- 
„niedergeworfen, unterdriickt" (;^ham-[h]mista-. mit im Simplex erfolgtem 
Anlautswandel von sm- zu [h]m-), hamistayae{-ca) „niederzuwerfen, zu unter- 
driicken"; hamaestar- „wer niederwirft. iinterdriickt" (vgl. zur Bed. dt. 
„zusammenschmei6en“) ; andererseits (mit vielleicht ebenfalls aus sni- ent- 
wickeltem Anlaut m-) maed- Gdbed. etwa „werfen", mit Abl. ^'^emitfere ex'' 
= „berauben“ mit a- ,,(an sich) kommen lassen“ ayni'&naiti), mit 

paiii- „*zuruckschicken" = ,,den LaufpaS geben, absagen", mit ham- (auf- 
fallige Bed.:) „berauben" {Jmni'&yat; vielleicht naher zu hamista-1): mit 
Jiam-\-aibi „zulassen, den Zutritt gestatten". Ob die erste Reihe Wzlausl. 
d oder t(h) hat, ist nicht zu entscheiden, Gleichsetzung beider Reihen wird
```


## [2026-09-14T02:35:52.946Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo '=== AFA ==='; grep -n -i 'sami.a\\|شمعون\\|اسماعيل' AFA.txt | head -5; echo '=== LKT ==='; grep -n -i 'komission\\|commission\\|komite' LKT.txt | head -5; echo '=== PLA hamest/samaa ==='; grep -n -i 'samā\\|samaa' incoming/PLA/PLA_pages.txt | head -3"
}
```


### [2026-09-14T02:35:53.029Z] TOOL RESULT

```
=== AFA ===
=== LKT ===
1898:Armenier  oder  Griechen  aus,  ist  meist allein  und  greift  zur  SchußwatTe  nur, wenn  man  sie  gegen  ihn  erhebt.  Der Hyrsyz  entspricht  dem  gewöhnlichen Briganlen,  wie  er  auch  in  anderen Ländern  der  Halbkultur  vorkommt.  Der Haiduk  ist  der  Bandit  mit  nationaler Färbung,  eine  Spezialität  des  Balkans, heutzutage  häufig  Komitadschi  [<tk. komita  ==  comite  und  Suffix  -gi  zur  An- gabe des  Berufes,  also  ,dem  Komite Angehöriger",  d.h.  dem  Komite  zur  Be- freiung Mazedoniens  von  jeglicher  nicht- mazedonischer oder  -bulgarischer  Herr- schaft] genannt:  frz.  comitadji.
=== PLA hamest/samaa ===
```


## [2026-09-14T02:35:57.536Z] TOOL CALL #69: Bash

```json
{
 "command": "timeout 300 python3 tools/ref_page.py SNS:53 --image 2>&1 | head -20"
}
```


### [2026-09-14T02:35:58.657Z] TOOL RESULT

```
no scan of SNS covers printed page 53 (see 'scans' in refs_online.json)
```


## [2026-09-14T02:42:34.888Z] TOOL CALL #70: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build460.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_SMEYT=\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/smeyt-\"\nW_MITTO=\"https://en.wiktionary.org/wiki/mitto\"\nWIKI_HAM=\"https://en.wikipedia.org/wiki/Hamistagan\"\nCAIS=\"https://www.cais-soas.com/CAIS/Languages/pahlavi/hamestagan.htm\"\nW_ISM=\"https://en.wiktionary.org/wiki/%D8%A5%D8%B3%D9%85%D8%A7%D8%B9%D9%8A%D9%84\"\nW_SHAM=\"https://en.wiktionary.org/wiki/%D8%B4%D9%85%D8%B9%D9%88%D9%86\"\nW_KOM=\"https://en.wiktionary.org/wiki/%DA%A9%D9%85%DB%8C%D8%B3%DB%8C%D9%88%D9%86\"\nVAJ_SAM=\"https://vajehyab.com/moein/%D8%B3%D9%85%D8%B9\"\nABADIS_HAM=\"https://abadis.ir/fatofa/%D9%87%D9%85%DB%8C%D8%B3%D8%AA%D8%A7%D8%B1/\"\nETY_MISSION=\"https://www.etymonline.com/word/mission\"\nW_SHEMA=\"https://en.wiktionary.org/wiki/%D7%A9%D7%9E%D7%A2\"\n\nKLN_SHEMA = (\"KLN_1966.txt line 34953 (leaf 761 = printed p. 1434; the leaf-to-page fit through \"\n             \"'Ishmael' leaf 442 = p.817 and 'mission' leaf 530 = p.988 is exact) s.v. Shema: \"\n             \"\\\"Heb. shema', lit. 'hear', imper. of Heb. shama', 'he heard' ... rel. to Aram.-Syr. shema', \"\n             \"Ugar. shm', Arab. sami'a, Ethiop. sam'a, 'he heard', Akkad. shemu, 'to hear'.\\\"\")\n\ndata = {\n \"pdf_page\": 460,\n \"book_page\": 430,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"S.m.`a\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"Proto-Semitic *šamaʿ- 'to hear' (root š-m-ʿ; Arabic s-m-ʿ سمع, Hebrew ש־מ־ע)\",\n   \"note\": (\"The root is real and the gloss is right. The only correction is the shape of the \"\n            \"reconstruction: Proto-Semitic had *š, so the etymon is *šamaʿ- (Hebrew/Ugaritic/Aramaic š-, \"\n            \"Akkadian šemû); Arabic s- in سمع is the regular Arabic reflex of Proto-Semitic *š. Nourai's \"\n            \"'S.m.`a' simply cites the root in its Arabic shape, as he does throughout the book. Klein's \"\n            \"entry s.v. Shema (his p. 1434) gives exactly the cognate set Nourai charts. Nourai's label \"\n            \"'Semitic' is acceptable for a book that does not distinguish Proto-Semitic from Common Semitic.\"),\n   \"note_fa\": (\"ریشهٔ سامی *šamaʿ- «شنیدن» ریشه‌ای واقعی و کاملاً شناخته است: عبری شָמַע (šāmaʿ)، اوگاریتی šmʿ، \"\n               \"آرامی/سریانی šmaʿ، اکدی šemû و عربی سَمِعَ همگی از آن‌اند. تنها نکته آن است که در سامی آغازین \"\n               \"آوای نخست *š بوده و «س» عربی دگرگونیِ قاعده‌مند همان *š است؛ نورایی ریشه را به شکل عربی‌اش \"\n               \"«S.m.`a» آورده که در سراسر کتاب او رسم است. کلاین (ص ۱۴۳۴، ذیل Shema) همین خویشاوندی‌ها را \"\n               \"می‌آورد. پس ادعای نورایی دربارهٔ ریشه درست است.\"),\n   \"sources\": [W_SHEMA],\n   \"ref_check\": [\n     {\"ref\": \"KLN:1434\", \"status\": \"supports\", \"note\": KLN_SHEMA}\n   ],\n   \"consulted\": [\n     {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 34953, leaf 761 (p. 1434) s.v. Shema\", \"stance\": \"supports\",\n      \"note\": \"Lists Heb. shama', Aram.-Syr. shema', Ugar. shm', Arab. sami'a, Ethiop. sam'a, Akkad. shemu — the common Semitic root Nourai posits.\"},\n     {\"src\": \"Wiktionary\", \"where\": \"he/Aramaic root ש־מ־ע entry\", \"stance\": \"supports\",\n      \"note\": \"'inherited from Proto-Semitic *šamaʕ-', cognate with Arabic سَمِعَ (samiʿa) 'to hear' — same root, with *š- as the Proto-Semitic onset.\"},\n     {\"src\": \"FVQ\", \"where\": \"FVQ_pages.txt leaf 80 (printed p. 63-64), s.v. Ismāʿīl\", \"stance\": \"partial\",\n      \"note\": \"Jeffery does not treat سمع itself (it is native Arabic, not a Qur'anic foreign word) but his Ismāʿīl entry works with the same Hebrew/Syriac root forms.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Arabic\", \"words\": \"samî`a\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"Arabic سَمِعَ samiʿa 'he heard' is the form-I perfect (fiʿila type, with the stative \"\n                    \"vowel -i-) of the inherited triliteral root s-m-ʿ < Proto-Semitic *šamaʿ-; the \"\n                    \"Proto-Semitic sibilant *š regularly gives Arabic s (cf. Heb. šālōm : Arab. salām). \"\n                    \"Klein p. 1434 s.v. Shema lists 'Arab. sami'a' among the direct cognates of Heb. shāmaʿ, \"\n                    \"so the arrow root→Arabic is a straightforward inheritance, not a borrowing.\"),\n     \"derivation_fa\": (\"عربی سَمِعَ (باب فَعِلَ، با واکهٔ حالتیِ ـِ) از ریشهٔ سه‌حرفیِ موروثی س‌م‌ع است که خود \"\n                       \"دنبالهٔ سامی آغازین *šamaʿ- می‌باشد؛ *š سامی آغازین در عربی به‌قاعده به «س» بدل شده \"\n                       \"است (مانند شالوم عبری در برابر سلامِ عربی). کلاین (ص ۱۴۳۴) سَمِعَ را در کنار šāmaʿ عبری \"\n                       \"می‌نشاند. پس این پیوند وام‌گیری نیست بلکه وراثت است و ادعای نورایی درست است.\"),\n     \"sources\": [W_SHEMA],\n     \"ref_check\": [{\"ref\": \"KLN:1434\", \"status\": \"supports\", \"note\": KLN_SHEMA}],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 34953 (leaf 761, p. 1434) s.v. Shema\", \"stance\": \"supports\",\n        \"note\": \"'rel. to Aram.-Syr. shema', Ugar. shm', Arab. sami'a ... Akkad. shemu, to hear'.\"},\n       {\"src\": \"AFM\", \"where\": \"grep 'سماع' / 'سمع' in AFM_pages.txt\", \"stance\": \"silent\",\n        \"note\": \"Addi Shir lists only Persian loanwords in Arabic; سمع is native Arabic and is (correctly) absent. Sole hit at line 409 is an unrelated OCR fragment.\"},\n       {\"src\": \"PLA\", \"where\": \"grep 'sam' in incoming/PLA/PLA_pages.txt\", \"stance\": \"silent\",\n        \"note\": \"Asbaghi, Persische Lehnwörter im Arabischen, has no entry — confirming سمع is not an Iranian loan.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\", \"words\": \"sam`a «سَمع»\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"Persian سَمع samʿ 'hearing, the sense of hearing' is a straight Arabic loan (the maṣdar \"\n                    \"of samiʿa), taken into New Persian with the whole Arabic lexical layer of the 9th-11th \"\n                    \"centuries; Moʿin tags it [ع.] i.e. Arabic. The box's further forms are all regular \"\n                    \"derivatives of the same Arabic stem borrowed with it: سَماع samāʿ (maṣdar 'listening', \"\n                    \"in Sufi usage the audition/musical séance, as in the Rumi couplet Nourai quotes), \"\n                    \"سَميع samīʿ (faʿīl adjective 'all-hearing', a divine name), اِستِماع istimāʿ (form-X \"\n                    \"maṣdar 'listening attentively'), مُستَمِع mustamiʿ (form-X active participle 'listener'), \"\n                    \"سامِع sāmiʿ (form-I active participle 'hearer'). None of them is a Persian formation; \"\n                    \"Persian only received them. The transliteration 'sam`a' in the chart renders the \"\n                    \"Arabic-style pausal/with-fatḥa citation سَمْع; the normal Persian pronunciation is samʿ.\"),\n     \"derivation_fa\": (\"«سَمع» وام‌واژه‌ای عربی است (مصدر سَمِعَ) که همراه لایهٔ بزرگ واژگان عربی در سده‌های \"\n                       \"سوم تا پنجم هجری وارد فارسی دری شد؛ معین نیز آن را با نشانِ [ع.] «گوش، حس شنوایی» \"\n                       \"آورده است. دیگر صورت‌های همین خانه نیز همگی مشتق‌های عربیِ همان ستاک‌اند که یکجا به \"\n                       \"فارسی آمده‌اند: سَماع (مصدر، و در اصطلاح صوفیان مجلس آواز و رقص، چنان‌که در بیت مولوی)، \"\n                       \"سَمیع (صفت بر وزن فَعیل، از نام‌های خداوند)، اِستِماع (مصدر باب افتعال)، مُستَمِع (اسم \"\n                       \"فاعل باب افتعال) و سامِع (اسم فاعل باب اول). هیچ‌یک ساختهٔ فارسی‌زبانان نیست. ادعای \"\n                       \"نورایی درست است.\"),\n     \"sources\": [VAJ_SAM],\n     \"ref_check\": [\n       {\"ref\": \"MON\", \"status\": \"supports\",\n        \"note\": \"Moʿin via vajehyab.com/moein/سمع: entry tagged '[ع.]' (Arabic) with the senses 'گوش، حس شنوایی' and 'شنیدن'. Nourai gives no page for MON here, so only the entry itself could be checked.\"},\n       {\"ref\": \"FVA:197\", \"status\": \"not_checked\",\n        \"note\": \"Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi — refs_online.json records no digital copy anywhere (archive.org, noorlib, ketabnak all searched by the project); page 197 could not be seen.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"MON\", \"where\": \"vajehyab.com/moein/سمع\", \"stance\": \"supports\",\n        \"note\": \"'[ع.] ۱- گوش، حس شنوایی ۲- شنیدن' — Arabic-origin tag, matching the chart's Arabic→Persian arrow.\"},\n       {\"src\": \"BQT\", \"where\": \"grep 'سماع' in BQT_v2_pages.txt (4 hits, all in definitions, no headword)\", \"stance\": \"silent\",\n        \"note\": \"Borhān-e Qāṭeʿ is a dictionary of Persian (largely non-Arabic) words; سمع/سماع have no etymological footnote by Moʿin there.\"},\n       {\"src\": \"ARY\", \"where\": \"grep in incoming/ARY/ARY_pages.txt\", \"stance\": \"silent\",\n        \"note\": \"Aryanpur covers only Indo-European roots of Persian words, so an Arabic loan is absent — negative confirmation that سمع is not Iranian.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Hebrew\", \"words\": \"shâma`; shema`; Yishma`-ěl\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"Hebrew שָׁמַע šāmaʿ 'he heard' is the qal perfect 3ms of the root ש־מ־ע < Proto-Semitic \"\n                    \"*šamaʿ-. שְׁמַע šemaʿ is both the imperative 'hear!' and a noun 'sound, report'; because \"\n                    \"Deut. 6:4 opens with that imperative, the confession of faith itself came to be called \"\n                    \"the Shemaʿ — which is exactly the 'a prayer' sense in the chart. יִשְׁמָעֵאל Yišmāʿēl is a \"\n                    \"sentence-name, yišmaʿ 'he (God) will hear' (qal imperfect 3ms of the same root) + ʾēl \"\n                    \"'God', hence 'God hears/God will hear' (Gen. 16:11 explains it so). The ☞Layh cross-\"\n                    \"reference sends the reader to Nourai's root for ʾēl/Allāh, which is the correct second \"\n                    \"element. All three items therefore belong to this root exactly as drawn.\"),\n     \"derivation_fa\": (\"عبری שָׁמַע (šāmaʿ) «شنید» صیغهٔ ماضی سوم‌شخص مفرد باب قَل از ریشهٔ ש־מ־ע است که به سامی \"\n                       \"آغازین *šamaʿ- می‌رسد. שְׁמַע (šemaʿ) هم امر «بشنو!» است و هم اسم به معنی «صدا، خبر»؛ و \"\n                       \"چون آیهٔ ۴ باب ششم سفر تثنیه با همین امر آغاز می‌شود، خودِ آن اقرارِ ایمان «شِمَع» نامیده \"\n                       \"شد — همان معنای «دعا» در نمودار. یִשְׁמָעֵאל (Yišmāʿēl) نامی جمله‌ای است: yišmaʿ «(خدا) \"\n                       \"خواهد شنید» + ʾēl «خدا»، یعنی «خدا می‌شنود» (سفر پیدایش ۱۶:۱۱ خود همین توضیح را می‌دهد). \"\n                       \"ارجاع ☞Layh نیز به ریشهٔ «ایل/الله» نزد نورایی است و درست است. ادعای نورایی درست است.\"),\n     \"sources\": [W_SHEMA],\n     \"ref_check\": [\n       {\"ref\": \"KLN:817\", \"status\": \"supports\",\n        \"note\": \"KLN_1966.txt line 19959 (leaf 442 = printed p. 817) s.v. Ishmael: \\\"Heb. Yishma'el, lit. 'God hears'. Heb. yishma', 'he will hear', is imperf. of shama', 'he heard'. See Shema and cp. Simeon, Simon. For the second element in the name Ishmael see El.\\\"\"},\n       {\"ref\": \"KLN:1434\", \"status\": \"supports\", \"note\": KLN_SHEMA}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"KLN_1966.txt lines 19959 and 34953 (leaves 442, 761 = pp. 817, 1434)\", \"stance\": \"supports\",\n        \"note\": \"Both of Nourai's cited pages carry exactly the forms he charts, including 'shema', sound' and 'shema', hearing'.\"},\n       {\"src\": \"Wiktionary\", \"where\": \"root ש־מ־ע\", \"stance\": \"supports\",\n        \"note\": \"'inherited from Proto-Semitic *šamaʕ-' for both the Hebrew and the Aramaic verb.\"},\n       {\"src\": \"FVQ\", \"where\": \"FVQ_pages.txt leaf 80 (pp. 63-64) s.v. Ismāʿīl\", \"stance\": \"supports\",\n        \"note\": \"Jeffery prints the Hebrew יִשְׁמָעֵאל beside Gk. Ἰσμαήλ, Syr. ʾIšmāʿīl and Eth. as the ancestors of the Arabic name.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Arabic\", \"words\": \"Ismâ`îl\", \"verdict\": \"plausible\",\n     \"derivation\": (\"Arabic إسماعيل Ismāʿīl is indeed the Hebrew name Yišmāʿēl, but not taken straight from \"\n                    \"Hebrew: Jeffery (FVQ pp. 63-64) shows that the Qurʾānic spelling is Syriac-mediated. His \"\n                    \"argument is formal — the Qurʾān writes إسحاق for יִצְחָק and يعقوب for יַעֲקֹב but إسماعيل \"\n                    \"for יִשְׁמָעֵאל and إسرائيل for יִשְׂרָאֵל, exactly the split found in Syriac (ʾIsḥāq, Yaʿqōb \"\n                    \"vs. ʾĪšmāʿīl, ʾĪsrāʾēl) — so 'it is reasonably certain that the Qurʾānic form came from a \"\n                    \"Syriac source', the Christian Palestinian Aramaic form removing the last difficulty. The \"\n                    \"Arabic ʾi- prosthesis and the -īl for Hebrew -ēl are the marks of that Aramaic route; \"\n                    \"cognate names with the initial sibilant were already known in Ṣafaitic and Ḥimyaritic \"\n                    \"inscriptions, but the Qurʾānic form itself is the borrowed one. So Nourai's arrow \"\n                    \"Hebrew→Arabic is right in substance and only omits the Syriac/Christian relay.\"),\n     \"derivation_fa\": (\"«إسماعيل» عربی همان نامِ عبری یִשְׁמָעֵאל است، اما نه مستقیم از عبری: جفری در «واژگان \"\n                       \"بیگانهٔ قرآن» (ص ۶۳–۶۴) نشان می‌دهد که املای قرآنی از راه سریانی آمده است. دلیل او صوری \"\n                       \"است: قرآن برای יִצְחָק «إسحاق» و برای יַעֲקֹב «يعقوب» می‌نویسد، اما برای יִשְׁמָעֵאל «إسماعيل» و \"\n                       \"برای יִשְׂרָאֵל «إسرائيل» — همان تقسیمی که در سریانی دیده می‌شود. همزهٔ آغازین و «ـيل» به \"\n                       \"جای ـēl عبری نشانهٔ همین مسیر آرامی‌اند. پس پیکان «عبری ← عربی» نورایی در اصل درست است و \"\n                       \"تنها واسطهٔ سریانی را نیاورده؛ با احتیاط پذیرفتنی است.\"),\n     \"sources\": [W_ISM],\n     \"ref_check\": [\n       {\"ref\": \"KLN:817\", \"status\": \"supports\",\n        \"note\": \"KLN_1966.txt line 19959 (leaf 442 = p. 817) s.v. Ishmael: 'Heb. Yishma'el, lit. God hears' — Klein derives the name from Hebrew, as Nourai's arrow does, but says nothing about the Arabic form or the Syriac relay.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"FVQ\", \"where\": \"FVQ_pages.txt leaf 80 (printed pp. 63-64), s.v. إسماعيل\", \"stance\": \"partial\",\n        \"note\": \"\\\"A Christian origin for the word is evident from a comparison of the Gk. Ἰσμαήλ; Syr. ʾIšmāʿīl; Eth. ... with the Heb. ישמעאל ... makes it reasonably certain that the Qur'anic form came from a Syr. source\\\" — same ultimate Hebrew origin, but via Syriac.\"},\n       {\"src\": \"KLN\", \"where\": \"leaf 442 (p. 817) s.v. Ishmael\", \"stance\": \"supports\",\n        \"note\": \"Hebrew Yishma'el 'God hears', imperf. of shama' + El.\"},\n       {\"src\": \"Wiktionary\", \"where\": \"ar/إسماعيل\", \"stance\": \"supports\",\n        \"note\": \"'From Hebrew יִשְׁמָעֵאל (yishmaʿel), from יִשְׁמַע אֵל (yishmaʿ ʾel, God heard)'; descendants include Classical Persian اِسْمَاعِیل.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Persian\", \"words\": \"Esmâ`îl «اسماعیل»\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"Persian اسماعیل Esmāʿīl is the Qurʾānic Arabic إسماعيل taken over unchanged in spelling \"\n                    \"with Islam; the only adaptation is phonetic — the Arabic hamzat al-waṣl with kasra is \"\n                    \"read as Persian e-, and the ʿayn is not pronounced as a pharyngeal in Persian, giving \"\n                    \"Esmāʾil/Esmāil. Wiktionary records the Classical Persian اِسْمَاعِیل as a direct descendant of \"\n                    \"the Arabic, from which Tajik, Urdu, Hindi and Punjabi forms in turn descend. The name's \"\n                    \"currency in Persian literature is exactly what Nourai's Rumi couplet (حلق پیش آورد \"\n                    \"اسماعیل‌وار) illustrates: the Qurʾānic Ismāʿīl, not the biblical Ishmael, is the son \"\n                    \"offered for sacrifice in Islamic tradition, which is why the Persian gloss keeps 'son of \"\n                    \"Abraham'.\"),\n     \"derivation_fa\": (\"«اسماعیل» فارسی همان «إسماعيل» عربیِ قرآنی است که با اسلام و بی‌تغییرِ املا به فارسی آمد؛ \"\n                       \"تنها سازگاری آوایی است: همزهٔ وصل مکسور در فارسی «اِ» خوانده می‌شود و «ع» در فارسی حلقی \"\n                       \"تلفظ نمی‌شود. ویکی‌واژه نیز فارسی کلاسیک «اِسْمَاعِیل» را دنبالهٔ مستقیم عربی می‌داند که \"\n                       \"صورت‌های تاجیکی، اردو، هندی و پنجابی از آن گرفته شده‌اند. بیت مولوی («حلق پیش آورد \"\n                       \"اسماعیل‌وار») به روایت اسلامیِ ذبحِ اسماعیل اشاره دارد، نه به روایت تورات. ادعای نورایی \"\n                       \"درست است.\"),\n     \"sources\": [W_ISM],\n     \"ref_check\": [\n       {\"ref\": \"MON\", \"status\": \"partial\",\n        \"note\": \"Nourai cites Moʿin without a page; اسماعیل is a proper name and belongs to Moʿin's aʿlām volumes (5-6), which are not among the scans in refs_online.json, so the printed entry could not be opened. The Persian currency of the name is confirmed independently (Wiktionary, Classical Persian اِسْمَاعِیل).\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"Wiktionary\", \"where\": \"ar/إسماعيل, Descendants\", \"stance\": \"supports\",\n        \"note\": \"Lists Classical Persian اِسْمَاعِیل (ismāʿīl) as a direct descendant of the Arabic name.\"},\n       {\"src\": \"FVQ\", \"where\": \"FVQ_pages.txt leaf 80 (pp. 63-64)\", \"stance\": \"supports\",\n        \"note\": \"Establishes the Arabic form that Persian took over; Jeffery notes the Muslim philologers themselves 'early recognized that it was non-Arabic' (al-Jawālīqī, Muʿarrab 9; al-Khafājī 10).\"},\n       {\"src\": \"MON\", \"where\": \"grep of MON_part1/2.txt (OCR of the Persian scan is unusable)\", \"stance\": \"silent\",\n        \"note\": \"The local Moʿin OCR is garbage for Persian script; no usable hit.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"Persian\", \"words\": \"Šam`ŭn «شمعون»\", \"verdict\": \"plausible\",\n     \"derivation\": (\"Persian شمعون Šamʿun is ultimately Hebrew שִׁמְעוֹן Šimʿōn 'hearing', a -ōn formation on \"\n                    \"šāmaʿ 'he heard' (Gen. 29:33 explains the name of Leah's second son by 'the LORD has \"\n                    \"heard'). But Persian did not take it from Hebrew: the Persian form with a- in the first \"\n                    \"syllable and -ūn in the second is the Aramaic/Syriac ܫܡܥܘܢ Šemʿōn as it came through \"\n                    \"Arabic شمعون Šamʿūn, which Wiktionary derives explicitly from the Hebrew name and which \"\n                    \"is the form used in Arabic and Persian Christian and historical writing for Simon Peter \"\n                    \"(the 'follower of Jesus' of the chart, as in the Sorush couplet quoted). Nourai's direct \"\n                    \"Hebrew→Persian arrow is therefore right about the origin but silently skips the \"\n                    \"Syriac/Arabic relay; the Greek Συμεών/Σίμων route gave Persian nothing here.\"),\n     \"derivation_fa\": (\"«شمعون» در نهایت همان שִׁמְעוֹן (Šimʿōn) عبری است، ساختی با پسوند ـōn بر پایهٔ šāmaʿ \"\n                       \"«شنید» (سفر پیدایش ۲۹:۳۳ خود نام را به «خداوند شنید» بازمی‌بندد). اما فارسی آن را از \"\n                       \"عبری نگرفته است: صورت فارسی با «ـَـ» در هجای نخست و «ـون» در هجای دوم بازتاب ܫܡܥܘܢ \"\n                       \"سریانی است که از راه «شمعون» عربی به فارسی رسیده؛ ویکی‌واژه نیز شمعونِ عربی را \"\n                       \"وام‌گرفته از عبری می‌داند. بنابراین پیکانِ مستقیمِ «عبری ← فارسی» نورایی دربارهٔ خاستگاه \"\n                       \"درست است ولی واسطهٔ سریانی–عربی را نادیده گرفته: با احتیاط پذیرفتنی است.\"),\n     \"sources\": [W_SHAM],\n     \"ref_check\": [\n       {\"ref\": \"MON\", \"status\": \"not_checked\",\n        \"note\": \"IMPORTANT: the printed page (pdf p. 460, rendered at 300 dpi, saved as data/verification/sources/refs/ocr/BOOK/460.png) shows this Persian box with NO reference at all — the header reads just 'Persian'. The refs value 'MON' in data/extracted/batch/page-460.json is not on the page; it is an extraction artefact. Nothing to check.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"Wiktionary\", \"where\": \"ar/شمعون\", \"stance\": \"supports\",\n        \"note\": \"'Borrowed from Hebrew שִׁמְעוֹן (šimʕōn, Simon), originally a patronymic' — and a doublet of two other Arabic forms representing different borrowing periods.\"},\n       {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 35244 (leaf 767) s.v. Simeon\", \"stance\": \"partial\",\n        \"note\": \"'Late L., fr. Gk. Συμεών, fr. Heb. Shim'on, lit. hearing, fr. shama', he heard' — same Hebrew source, but Klein traces only the European route.\"},\n       {\"src\": \"AFM\", \"where\": \"grep 'شمعون' in AFM_pages.txt\", \"stance\": \"silent\",\n        \"note\": \"Addi Shir has no entry (he treats only Persian words arabised, not Semitic names).\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"English\", \"words\": \"Shema; Simon; Simeon; Shimeon; Ishmael\", \"verdict\": \"plausible\",\n     \"derivation\": (\"All five are Hebrew in origin, as Nourai draws, but three of them reached English through \"\n                    \"Greek and Latin rather than from Hebrew directly, so the single arrow is a shortcut. \"\n                    \"Shema is a modern learned borrowing straight from Heb. šemaʿ, the opening imperative of \"\n                    \"Deut. 6:4 (Klein p. 1434). Ishmael is the Septuagint/Vulgate form of Yišmāʿēl, current in \"\n                    \"English since the Wycliffite Bible and figurative ('outcast') since the 19th century after \"\n                    \"Gen. 16:12 and Melville (Klein p. 817). Simeon is, in Klein's words, 'Late L., fr. Gk. \"\n                    \"Συμεών, fr. Heb. Shimʿōn'. Simon is 'L., fr. Gk. Σίμων, fr. Heb. Shimʿōn, but influenced \"\n                    \"in form by the Greek PN Σίμων, lit. snub-nosed (fr. σιμός)' — an assimilation of the \"\n                    \"Semitic name to an existing Greek one, which is why Simon and Simeon are doublets. \"\n                    \"'Shimeon' is not an English word but the scholarly transliteration of the Hebrew, listed \"\n                    \"here as a variant.\"),\n     \"derivation_fa\": (\"هر پنج صورت در نهایت عبری‌اند — چنان‌که نورایی کشیده — اما سه تای آن‌ها از راه یونانی و \"\n                       \"لاتینی به انگلیسی رسیده‌اند و پیکانِ یکسرهٔ «عبری ← انگلیسی» کوتاه‌سازی است. Shema \"\n                       \"وام‌واژه‌ای عالمانه و مستقیم از שְׁמַע عبری است. Ishmael صورت سبعینیه/ولگات یִשְׁמָעֵאל است. \"\n                       \"Simeon به گفتهٔ کلاین «از لاتینی متأخر، از یونانی Συμεών، از عبری Šimʿōn» است، و Simon \"\n                       \"همان نام است که در یونانی به نام یونانیِ Σίμων «پخ‌بینی» (از σιμός) همگون شده — پس \"\n                       \"Simon و Simeon دوگانه‌اند. «Shimeon» واژهٔ انگلیسی نیست، آوانگاریِ عالمانهٔ عبری است. \"\n                       \"ادعای نورایی با احتیاط پذیرفتنی است.\"),\n     \"sources\": [W_SHEMA],\n     \"ref_check\": [\n       {\"ref\": \"KLN\", \"status\": \"supports\",\n        \"note\": \"Nourai gives KLN without a page; all five items are in Klein: Shema (line 34953, leaf 761 = p. 1434), Ishmael (line 19959, leaf 442 = p. 817), Simeon (line 35244, leaf 767), Simon (line 35256, leaf 767), and Klein's Shema entry closes 'Cp. Ishmael, Simeon, smouse, Tashmitum'.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"KLN_1966.txt lines 19959, 34953, 35244, 35256\", \"stance\": \"supports\",\n        \"note\": \"s.v. Simon: 'L., fr. Gk. Σίμων, fr. Heb. Shim'on, but influenced in form by the Greek PN Σίμων, lit. snub-nosed (fr. σιμός)'.\"},\n       {\"src\": \"SKT\", \"where\": \"grep '^Simon' / '^Shema' in SKT.txt\", \"stance\": \"silent\",\n        \"note\": \"Skeat's concise dictionary omits proper names, so no entry — not evidence against.\"},\n       {\"src\": \"FSD\", \"where\": \"grep in FSD_vol1..4\", \"stance\": \"silent\",\n        \"note\": \"Funk & Wagnalls indexes these as biblical names without etymological discussion beyond 'Heb.'\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"Smeit\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *smeyt- / *smeit-, *smit- 'to throw' (Pokorny 968; Walde-Pokorny II 687f.)\",\n   \"note\": (\"Pokorny's IEW p. 968 has exactly 'smeit-, smit- \\\"to throw\\\"' (German 'werfen'), and Walde-\"\n            \"Pokorny II 687 has the same lemma 'smeit(h)- werfen'. Wiktionary reconstructs it as *smeyt- \"\n            \"'to throw' with Slavic (Russian метать) and Avestan (maēθ-, hamista-) descendants. Nourai's \"\n            \"language label 'Indo-European' and gloss 'to throw, send forward' are therefore right; \"\n            \"'send forward' is his addition from the Latin branch and is not part of the reconstructed \"\n            \"meaning. Note that the root is confined to Iranian, Slavic and (doubtfully) Latin: Pokorny \"\n            \"himself keeps the Germanic 'smite' group under the separate root smei-/smeid- 'to smear', \"\n            \"and Buck (SYN) agrees.\"),\n   \"note_fa\": (\"ریشهٔ هندواروپاییِ *smeyt- / *smeit- «پرتاب کردن، افکندن» ریشه‌ای شناخته‌شده است: پوکورنی در \"\n               \"«فرهنگ ریشه‌شناختی هندواروپایی» ص ۹۶۸ آن را با همین صورت و همین معنا (werfen) آورده و \"\n               \"والده–پوکورنی (جلد دوم، ص ۶۸۷) نیز مدخل smeit(h)- «werfen» دارد. ویکی‌واژه دنباله‌های آن را \"\n               \"در اسلاوی (روسی метать) و ایرانی (اوستایی maēθ-، hamista-) می‌شمارد. برچسب زبانی و معنای \"\n               \"نورایی درست است؛ تنها «send forward» افزودهٔ خود اوست که از شاخهٔ لاتینی گرفته شده و جزو \"\n               \"معنای بازسازی‌شده نیست. ادعای نورایی دربارهٔ ریشه درست است.\"),\n   \"sources\": [W_SMEYT],\n   \"ref_check\": [\n     {\"ref\": \"POK:968\", \"status\": \"supports\",\n      \"note\": \"POK_03.txt leaf 208-209 (printed p. 968, the number '968' is printed in the OCR of leaf 208) and POK_full.txt line 78446: 'Root / lemma: smeit-, smit- / Meaning: to throw ... Page(s): 968'. The material listed is Avestan hamista-, hamaēstar-, maēθ- and Latin mittō < *smītō (*smeitō).\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"POK\", \"where\": \"POK_03.txt leaves 208-209 = IEW p. 968; POK_full.txt line 78446\", \"stance\": \"supports\",\n      \"note\": \"'smeit-, smit- ... Meaning: to throw'; refs given as 'WP. II 687 f., WH II 97 ff.'\"},\n     {\"src\": \"WLD\", \"where\": \"incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt line 44655, printed p. 687\", \"stance\": \"supports\",\n      \"note\": \"Lemma 'smeit(h)- \\\"werfen\\\"' with the two Avestan series hamista-/hamaēstar- and maēθ-, and the note that in the simplex sm- became [h]m-.\"},\n     {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt line 958\", \"stance\": \"partial\",\n      \"note\": \"Watkins: '(s)meit(e)-. To throw. Possibly Latin mittere ... [Pok. smeit- 968.]' — the root is accepted, the Latin attachment is only 'possibly'.\"},\n     {\"src\": \"IEC\", \"where\": \"IEC.txt line 16422\", \"stance\": \"partial\",\n      \"note\": \"Mann lists 'smit- \\\"fling, strike\\\"' but puts Latin mittō under 'cf. (expressive?)' and attaches the Germanic smith-words, i.e. a looser grouping than Pokorny's.\"},\n     {\"src\": \"SYN\", \"where\": \"SYN.txt line 13991 s.v. smite\", \"stance\": \"partial\",\n      \"note\": \"Buck puts English smite / Goth. bi-smeitan under *smē(i)- 'smear' (Walde-P. 2.685f.), not under the 'throw' root — i.e. the Germanic words are NOT part of this root.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"maěth; hamista; hamaěstar\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"The three forms are Bartholomae's and Pokorny's. Av. maēθ-/mōiθ- (Nourai's 'maěth') is \"\n                    \"the verbal root 'to throw, let go, mittere', attested in Old Avestan with preverbs: \"\n                    \"mōiθat̰ (Y 46.4) 'may he rob' = *emittere ex, ā-miθnāiti 'lets come to himself', paiti- \"\n                    \"'send back, dismiss', ham-aibi-mōist (Y 46.12) 'admit, grant entrance'. hamista- (Y 8.6) \"\n                    \"is its past passive participle with the preverb ham-, 'thrown down, oppressed'; Pokorny \"\n                    \"and Walde-Pokorny explain the initial as *ham-[h]mista- with the Iranian change of \"\n                    \"word-initial sm- to (h)m- in the simplex, which is precisely why the root's *s- is \"\n                    \"invisible in Avestan. hamaēstar- is the agent noun in -tar- to the same compound, \"\n                    \"Bartholomae 'der, die nieder-, zu Boden wirft, unterdrückt' (AiW col. 1774), used of \"\n                    \"Zarathustra as smiter of the daēvas (Yt. 10.26, Y 48.12) and glossed by the Pahlavi \"\n                    \"translators with Sanskrit pratipakṣaḥ 'adversary' — hence Nourai's 'enemy'.\"),\n     \"derivation_fa\": (\"هر سه صورت از بارتولومه و پوکورنی گرفته شده‌اند. maēθ-/mōiθ- اوستایی ستاکِ فعلیِ «افکندن، \"\n                       \"رها کردن» است که در اوستای گاهانی با پیشوند به کار رفته: mōiθat̰ (یسنه ۴۶٫۴)، \"\n                       \"ā-miθnāiti، و həm-aibi-mōist (یسنه ۴۶٫۱۲) «راه دادن». hamista- (یسنه ۸٫۶) صفت مفعولیِ \"\n                       \"همان ستاک با پیشوند ham- است، «فروافکنده، سرکوب‌شده»؛ پوکورنی و والده–پوکورنی آن را \"\n                       \"*ham-[h]mista- می‌دانند، یعنی sm- آغازینِ هندواروپایی در ایرانی به (h)m- بدل شده و \"\n                       \"به همین سبب «س» ریشه در اوستایی دیده نمی‌شود. hamaēstar- اسم فاعل با پسوند ـtar- از \"\n                       \"همان ترکیب است؛ بارتولومه (ستون ۱۷۷۴) آن را «آن‌که فرومی‌افکند و سرکوب می‌کند» معنی \"\n                       \"می‌کند و مترجمان پهلوی آن را به سنسکریت pratipakṣaḥ «دشمن» برگردانده‌اند. ادعای \"\n                       \"نورایی درست است.\"),\n     \"sources\": [W_SMEYT],\n     \"ref_check\": [\n       {\"ref\": \"POK:968\", \"status\": \"supports\",\n        \"note\": \"POK_full.txt line ~78453: 'Avestan hamista- \\\"niedergeworfen, oppressed\\\" (*ham-[h]mista-, with in Simplex erfolgtem Anlautswandel from sm- to [h]m-); hamaēstar- \\\"wer niederwirft\\\"; maēθ- \\\"throw\\\"' — all three of Nourai's words, on the cited page.\"},\n       {\"ref\": \"KLN:988\", \"status\": \"supports\",\n        \"note\": \"KLN_1966.txt line 24047 (leaf 530 = printed p. 988) s.v. mission: Latin mittere 'is prob. cogn. with Avestic maēθ-, to send' — Klein's page 988 does carry the Avestan form Nourai cites.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"BRT\", \"where\": \"BRT.txt line 29405, AiW col. 1774 s.v. hamaēstar-\", \"stance\": \"supports\",\n        \"note\": \"'hamaēstar- m. der, die nieder-, zu Boden wirft, unterdrückt' with Y. 48.12, Yt. 14.15, Yt. 10.26; line 29459 'hamista- Adj., PPfP.: s. maiθ-'; line 29406 'Zum V. maiθ- mit ham' and the Sanskrit gloss pratipakṣaḥ.\"},\n       {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt line ~17259, root *maidH2 'to throw, discard, mittere'\", \"stance\": \"supports\",\n        \"note\": \"'OAv. miθ- (mōiθ-) to rob, discard, (e)mittere || (+ *ham-) to throw down ... Partic. perf. pass. YAv. hamista- (Y 8.6)'; PIE '*m(e)itH- to throw, let go ... LIV 430 | Pok. 968'. Cheung also warns that this root must be kept apart from the homonymous *maiH 'to change'.\"},\n       {\"src\": \"WLD\", \"where\": \"WLD Bd. II p. 687\", \"stance\": \"supports\",\n        \"note\": \"Same two Avestan series, with Bartholomae IF 19 Beitr. 202ff. cited.\"},\n       {\"src\": \"AVG\", \"where\": \"grep in AVG.txt\", \"stance\": \"silent\",\n        \"note\": \"Jackson's Avesta Grammar has no entry for these lexemes.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"haměstâr; haměstagân\", \"verdict\": \"disputed\",\n     \"derivation\": (\"The two words must be separated. (a) MP hamēstār [hmyst'l] 'adversary, opponent' is the \"\n                    \"regular continuation of Av. hamaēstar-: Avestan -ae- > MP -ē-, the -tar- agent suffix \"\n                    \"survives as -tār, and the abstract hamēstārīh 'opposition' is built on it. Nyberg's \"\n                    \"glossary states this outright ('hamēstār [hmyst'l] adversary, foe 7214, — Av. (1774) \"\n                    \"hamaēstar-'), and Horn's Pahlavi list no. 105 does the same. This half of the node is \"\n                    \"confirmed. (b) hamēstagān 'the neutral station between heaven and hell, the place of \"\n                    \"souls whose good and bad deeds balance' does NOT belong here on the current view. \"\n                    \"MacKenzie's own addenda list it under a separate headword hamēst 'whose good and bad \"\n                    \"deeds weigh equal', and Humbach connects the word with Old Avestan hə̄miiasaite (Y 33.1) \"\n                    \"'reckoned together', Klingenschmitt with 'raised together (to the same height)' — i.e. \"\n                    \"with ham- + a root yah/yas, not with ham- + maēθ- 'throw down'. The etymology is \"\n                    \"explicitly called uncertain. Nourai's gloss 'awkward situation' is also wrong for the \"\n                    \"Pahlavi word, which is a technical eschatological term (his own Persian box glosses it \"\n                    \"correctly).\"),\n     \"derivation_fa\": (\"این دو واژه را باید از هم جدا کرد. (الف) هَمیستار (hamēstār) فارسی میانه «دشمن، \"\n                       \"حریف» دنبالهٔ قاعده‌مند hamaēstar- اوستایی است: ـaē اوستایی در فارسی میانه ـē شده و \"\n                       \"پسوند فاعلیِ ـtar- به ـtār بدل گشته؛ نیبرگ در واژه‌نامهٔ خود صریحاً می‌نویسد \"\n                       \"«hamēstār … ــ اوستایی (۱۷۷۴) hamaēstar-» و هرن نیز (شمارهٔ ۱۰۵) همین را می‌گوید. این \"\n                       \"نیمه از ادعای نورایی درست است. (ب) اما هَمیستَگان (hamēstagān)، یعنی جایگاه میانهٔ \"\n                       \"بهشت و دوزخ برای روانی که کرفه و گناهش برابر است، در دیدگاه امروزی به این ریشه \"\n                       \"بازنمی‌گردد: مکنزی خود در «افزوده‌ها» آن را زیر سرواژهٔ جداگانهٔ hamēst «آن‌که نیک و \"\n                       \"بدش برابر است» می‌آورد، و هومباخ آن را با həmiiasaite اوستایی (یسنه ۳۳٫۱) «با هم \"\n                       \"شمرده‌شده» و کلینگن‌اشمیت با «هم‌اندازه برافراشته» می‌سنجد — یعنی ham- + ریشهٔ yah/yas، \"\n                       \"نه ham- + maēθ-. ریشه‌شناسی این واژه را صریحاً نامسلم خوانده‌اند. افزون بر این، معنیِ \"\n                       \"«وضعیت ناخوشایند» که نورایی برای صورت پهلوی می‌آورد نادرست است. پس پژوهش امروزی این \"\n                       \"نیمه از ادعا را رد می‌کند.\"),\n     \"sources\": [WIKI_HAM, CAIS],\n     \"ref_check\": [\n       {\"ref\": \"SNS:53\", \"status\": \"partial\",\n        \"note\": \"Tavoosi's Shāyast nē-Shāyast glossary, SNS_pages.txt leaf 42, carries both entries: ':hamēstār:' with the note 'hamaēstar-, (AiW) 1774' and ':hamēstagān:' with a Persian gloss 'جایی که ...'; the word-index (SNS_pages.txt line 16187) records 'hamestarih 53/16'. The printed page number of the glossary leaf could not be confirmed — refs_online.json says SNS's page offset is undetermined and tools/ref_page.py has no scan for SNS:53 — so 'partial': the words and the Avestan source are there, but the glossary does not derive hamēstagān from hamaēstar-.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt line 1822\", \"stance\": \"supports\",\n        \"note\": \"\\\"hamēstār [hmyst'l] adversary, foe 7214, — Av. (1774) hamaēstar-\\\" — Nyberg derives the Pahlavi word from exactly the Avestan form Nourai charts. He has no entry for hamēstagān.\"},\n       {\"src\": \"PHD\", \"where\": \"PHD.txt line 392 (main glossary) and line 125 (addenda)\", \"stance\": \"contradicts\",\n        \"note\": \"Main text: \\\"hamēstār, ~īh [hmyst'l, -yh] = hamēmāl, ~īh\\\" (adversary) but separately \\\"hammist [hmyst'] stagnant, peaceful. ~(ag)an limbo, the neutral station between heaven and hell\\\"; the addenda replace that with \\\"add hamēst [hmyst'] whose good and bad deeds weigh equal. ~(ag)an limbo\\\". MacKenzie thus keeps hamēstagān apart from hamēstār.\"},\n       {\"src\": \"HRN\", \"where\": \"HRN.txt leaf 300-301 = printed pp. 279-280, no. 105\", \"stance\": \"supports\",\n        \"note\": \"\\\"105. hamestār 'Gegner, Widersacher', hamestārīh (Mēn., Bund.). — ap. vergl. hamiçiya- 'aufrührerisch'; aw. hamaēstar- 'Feind'.\\\" Horn lists it among Pahlavi words and gives the Avestan etymon.\"},\n       {\"src\": \"Encyclopaedia Iranica / CAIS\", \"where\": \"cais-soas.com article HAMĒSTAGĀN\", \"stance\": \"contradicts\",\n        \"note\": \"'The word relates to Avestan həmiiasaite, found in Yasna 33.1'; Humbach 'reckoned together', Klingenschmitt 'raised together (to the same height)', MacKenzie 'the neutral station between the earth and the sky' — etymology uncertain, and in no case from ham- + maēθ-.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"hamîstar «همیستر»; hamîstakân «همیستکان»\", \"verdict\": \"disputed\",\n     \"derivation\": (\"Nourai's own NOTE ('almost obsolete words') is fair: neither is current Persian. (a) \"\n                    \"همیستار hamīstār 'adversary, opponent' is the MP hamēstār carried into New Persian in \"\n                    \"Zoroastrian and archaising usage; MP -ē- in an open syllable is written and read -ī- in \"\n                    \"New Persian (cf. MP dēn > NP دین), which is exactly the chart's hamīstar. Abadis (from \"\n                    \"Dehkhoda/Naisakān) still lists همیستار with the senses of opposition and enmity. This \"\n                    \"half is confirmed and its Avestan ancestry (hamaēstar-) is agreed by Horn and Nyberg. \"\n                    \"(b) همیستکان hamīstakān, the intermediate place of souls, is the Middle Persian \"\n                    \"eschatological term hamēstagān taken over unchanged by Persian Zoroastrian writing \"\n                    \"(Dādestān ī dēnīg etc.); its etymology is disputed and modern scholarship (Humbach, \"\n                    \"Klingenschmitt, MacKenzie) does not connect it with the 'throw' root at all, but with \"\n                    \"Av. hə̄miiasaite 'reckoned together'. Because the two words of the node have different \"\n                    \"verdicts the node takes the worse one. The printed Persian script («همیستَر»، «همیستکان») \"\n                    \"matches the JSON; note only that the standard Persian lemma is همیستار with alef.\"),\n     \"derivation_fa\": (\"یادداشت خود نورایی («واژه‌هایی تقریباً منسوخ») درست است. (الف) «همیستار» به معنی «دشمن، \"\n                       \"حریف» همان hamēstār فارسی میانه است که در نوشتار زردشتی و کهن‌گرای فارسی نو مانده؛ \"\n                       \"ē فارسی میانه در فارسی نو «ی» نوشته و خوانده می‌شود (مانند dēn ← دین)، و همین صورتِ \"\n                       \"hamīstar نمودار است. آبادیس (به نقل از دهخدا) نیز «همیستار» را با معنای ضدیت و دشمنی \"\n                       \"می‌آورد؛ تبار اوستاییِ آن (hamaēstar-) مورد پذیرش هرن و نیبرگ است. (ب) اما «همیستکان» \"\n                       \"اصطلاحی فرجام‌شناختی است که یکراست از فارسی میانه (دادستان دینیگ و مانند آن) به \"\n                       \"فارسی رسیده و ریشه‌شناسی آن مورد اختلاف است؛ پژوهش امروزی آن را نه به ریشهٔ «افکندن» \"\n                       \"بلکه به həmiiasaite اوستایی «با هم شمرده‌شده» می‌بندد. چون دو واژهٔ این خانه داوری \"\n                       \"یکسان ندارند، داوریِ سخت‌گیرانه‌تر برگزیده شد. املای فارسی چاپ‌شده با داده‌ها می‌خواند؛ \"\n                       \"تنها سرواژهٔ معیار «همیستار» (با الف) است.\"),\n     \"sources\": [ABADIS_HAM, WIKI_HAM, CAIS],\n     \"ref_check\": [\n       {\"ref\": \"HRN:279\", \"status\": \"supports\",\n        \"note\": \"HRN.txt leaf 300 = printed p. 279, entry no. 105: 'hamestār Gegner, Widersacher, hamestārīh (Mēn., Bund.)' with 'aw. hamaēstar- Feind' on p. 280. Horn's cited page is exactly right, though he treats the word as Pahlavi, not New Persian, and says nothing about hamēstagān.\"},\n       {\"ref\": \"MON:5185\", \"status\": \"not_checked\",\n        \"note\": \"tools/ref_page.py MON:5185 answers 'no scan of MON covers printed page 5185'; the local MON OCR (MON_part1/2.txt) is unusable for Persian script (garbage characters), and vajehyab/abadis do not expose page numbers. Moʿin's entry could not be seen.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"HRN\", \"where\": \"HRN.txt leaves 300-301 (pp. 279-280), no. 105\", \"stance\": \"supports\",\n        \"note\": \"Gives hamestār with Av. hamaēstar- and cf. OP hamiçiya- 'rebellious'.\"},\n       {\"src\": \"MON\", \"where\": \"abadis.ir/fatofa/همیستار (Dehkhoda + Moʿin aggregator)\", \"stance\": \"supports\",\n        \"note\": \"The page lists همیستار with meanings 'related to opposition and enmity' — the word is attested in the Persian lexicographical tradition, as Nourai says.\"},\n       {\"src\": \"PHD\", \"where\": \"PHD.txt lines 125, 392\", \"stance\": \"contradicts\",\n        \"note\": \"MacKenzie's separate headwords hamēstār 'adversary' vs hamēst/hamēst(ag)ān 'limbo' undercut the chart's single Pahlavi box feeding a single Persian box.\"},\n       {\"src\": \"ARY\", \"where\": \"grep 'همیست' in incoming/ARY/ARY_pages.txt\", \"stance\": \"silent\",\n        \"note\": \"Aryanpur's dictionary of Indo-European roots of Persian has no entry for either word (they are obsolete).\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Latin\", \"words\": \"mithere\", \"verdict\": \"transcription_suspect\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"mithere\",\n     \"correct_form\": \"mittere\",\n     \"derivation\": (\"The Latin verb is mittō, mittere, mīsī, missum 'to let go, send, throw'. There is no \"\n                    \"Latin *mithere: the printed page (pdf p. 460, box 'Latin | AHD') really does read \"\n                    \"'mithere', so this is Nourai's own misprint and the JSON extraction is faithful — the \"\n                    \"300-dpi render is filed as data/verification/sources/refs/ocr/BOOK/460.png. Probably he \"\n                    \"wrote -th- to show the -θ- of the Avestan comparandum. On the etymology itself the \"\n                    \"arrow is defensible but not certain: Pokorny 968 derives mittō from *smītō < *smeitō \"\n                    \"with 'expressive' gemination, citing the archaic compound cosmittere (Paulus Festus) \"\n                    \"for the lost s-; Walde-Hofmann II 97ff., Watkins ('possibly Latin mittere'), Cheung \"\n                    \"(IE cognates of *maidH2: 'Lat. mittere') and above all Ernout-Meillet ('on rapproche de \"\n                    \"manière séduisante une racine iranienne ... av. maēθ- que Bartholomae traduit justement \"\n                    \"par mittere') all go that way. Against it, de Vaan and Etymonline derive mittō from \"\n                    \"PIE *meyth2- 'to exchange, remove' (Skt. méthati, Goth. in-maidjan), and de Vaan calls \"\n                    \"the s-mobile reconstruction based on cōsmittō unreliable. So: form wrong, derivation \"\n                    \"plausible-but-contested.\"),\n     \"derivation_fa\": (\"فعل لاتینی mittō / mittere «رها کردن، فرستادن، افکندن» است و *mithere در لاتینی وجود \"\n                       \"ندارد. تصویر ۳۰۰ نقطه‌ایِ صفحهٔ چاپی (pdf ۴۶۰) نشان می‌دهد که خودِ کتاب «mithere» چاپ \"\n                       \"کرده است؛ پس این خطای چاپیِ نورایی است و خوانشِ داده‌ها درست بوده — احتمالاً او ـth- را \"\n                       \"برای نمایاندن ـθ- اوستایی نوشته است. اما دربارهٔ خودِ اشتقاق: پوکورنی (ص ۹۶۸) mittō را \"\n                       \"از *smītō < *smeitō می‌گیرد و برای اثبات «س» ازدست‌رفته به ترکیب کهنِ cosmittere \"\n                       \"استناد می‌کند؛ والده–هوفمان، واتکینز («شاید»)، چونگ و به‌ویژه ارنو–مِیه («به‌گونه‌ای \"\n                       \"فریبنده آن را با ریشه‌ای ایرانی، اوستایی maēθ-، می‌سنجند که بارتولومه درست به mittere \"\n                       \"برگردانده») همین راه را می‌روند. در برابر، دخوان (de Vaan) و اتیمآنلاین mittō را از \"\n                       \"*meyth₂- «مبادله کردن» می‌دانند. پس: خطای چاپی کتاب در صورت واژه، و اشتقاق با احتیاط \"\n                       \"پذیرفتنی.\"),\n     \"sources\": [W_MITTO, ETY_MISSION, W_SMEYT],\n     \"ref_check\": [\n       {\"ref\": \"AHD\", \"status\": \"partial\",\n        \"note\": \"AHD_watkins1985.txt line 958: '(s)meit(e)-. To throw. Possibly Latin mittere (first person plural present indicative mittimus), to let go, send off, throw: MASS, MESS, MESSAGE, MISSILE, MISSION ... [Pok. smeit- 968.]' — Watkins spells the Latin mittere (not 'mithere') and hedges with 'Possibly'.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"POK\", \"where\": \"POK_03.txt leaf 209 = IEW p. 968\", \"stance\": \"supports\",\n        \"note\": \"'lat. mittō, -ere, mīsī, missum \\\"gehen lassen, laufen lassen; schicken, senden\\\", mit expressiver Verschärfung aus *smītō (*smeitō), vgl. cosmittere Paul. Fest.'\"},\n       {\"src\": \"LAT\", \"where\": \"LAT.txt lines 38480-38485 (Ernout-Meillet s.v. mittō, p. ~735)\", \"stance\": \"partial\",\n        \"note\": \"'Le présent mittō, à côté du perfectum mīsī, ne peut être qu'une forme expressive à consonne intérieure géminée. Pas d'étymologie sûre. ... On rapproche de manière séduisante une racine iranienne ... av. maēθ- que Bartholomae traduit justement par mittere.' Supports the Iranian comparison but calls the etymology unsure; also note it spells the verb mittō/mittere throughout.\"},\n       {\"src\": \"Etymonline / de Vaan\", \"where\": \"etymonline.com/word/mission; Wiktionary s.v. mitto\", \"stance\": \"contradicts\",\n        \"note\": \"'Latin mittere \\\"to release, let go; send, throw\\\", from PIE root *m(e)ith- \\\"to exchange, remove\\\"'; Wiktionary/de Vaan: from Proto-Italic *meitō < PIE *meyth2-, and the *s- reconstruction from the hapax cōsmittō is 'unreliable'.\"},\n       {\"src\": \"IEC\", \"where\": \"IEC.txt line 16422\", \"stance\": \"partial\",\n        \"note\": \"Mann puts Latin mittō under 'cf. (expressive?)' at smit- — accepting the comparison only with reservation.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"French\", \"words\": \"\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"An empty pass-through box: it stands for the French continuations of Latin mittere and \"\n                    \"its compounds — commettre, mission, commission, comité, commis — which are the immediate \"\n                    \"sources of the Persian and English boxes below it. Most of these are learned \"\n                    \"re-borrowings from Latin in Middle French rather than inherited forms (inherited \"\n                    \"mittere survives as mettre 'to put'), which is why they keep the Latin -miss-/-mit- \"\n                    \"shape intact.\"),\n     \"derivation_fa\": (\"این خانه تهی و گذرگاهی است و نمایندهٔ دنباله‌های فرانسویِ mittere لاتینی و ترکیب‌های \"\n                       \"آن است: commettre، mission، commission، comité، commis — که سرچشمهٔ بی‌واسطهٔ خانه‌های \"\n                       \"فارسی و انگلیسیِ زیرین‌اند. بیشتر این واژه‌ها در فرانسهٔ میانه از لاتینی وام‌گیریِ \"\n                       \"عالمانه شده‌اند، نه میراثِ آوایی (صورت موروثیِ mittere همان mettre «نهادن» است) و \"\n                       \"به همین سبب ریختِ لاتینیِ ـmiss-/-mit- را دست‌نخورده نگاه داشته‌اند. ادعای نورایی درست است.\"),\n     \"sources\": [ETY_MISSION],\n     \"ref_check\": [\n       {\"ref\": \"AHD\", \"status\": \"partial\",\n        \"note\": \"AHD_watkins1985.txt line 958 lists the English outcomes of this root but, as an IE-root appendix, names no French intermediate; the French stage is standard and uncontroversial (Etymonline s.v. mission: 'from Latin missionem').\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/mission\", \"stance\": \"supports\",\n        \"note\": \"'mission ... from Latin missionem (nom. missio) act of sending, a dispatching; a release, a setting at liberty' — the French forms are the learned continuations of these.\"},\n       {\"src\": \"SKT\", \"where\": \"SKT.txt line 11705 s.v. mission\", \"stance\": \"supports\",\n        \"note\": \"'mission. (L.) [The O.F. mission merely means capacity; Cot.] — L. acc. missionem ... — L. missus, pp. of mittere, to send.' Skeat confirms the French link exists but notes the English word came from Latin directly.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"Persian\", \"words\": \"komîsîyon «کمیسیون»\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"Persian کمیسیون komisiyon 'commission, committee, broker's fee' is a French loan of the \"\n                    \"constitutional/Qajar-modernisation period, borrowed from French commission (itself Latin \"\n                    \"commissiōnem, to committere = com- + mittere). The French nasal -on is rendered by \"\n                    \"Persian ـون -on and the French -ssi- by ـسی-, the usual adaptation of French -tion/-sion \"\n                    \"words in Persian (cf. پانسیون, کمیسیون, ایستگاه-era borrowings). Wiktionary states \"\n                    \"plainly 'Borrowed from French commission'. The parenthesised کمیته komite on the page is \"\n                    \"the parallel loan from French comité (itself borrowed from English committee, which is \"\n                    \"again mittere), and travelled through the same channel; Lokotsch (LKT) records the same \"\n                    \"word reaching Turkish as komita in komitadschi.\"),\n     \"derivation_fa\": (\"«کمیسیون» وام‌واژه‌ای فرانسوی از دورهٔ نوسازی قاجاری و مشروطه است، از commission فرانسوی \"\n                       \"که خود از commissiōnem لاتینی و از committere (com- + mittere) می‌آید. «ـon» خیشومیِ \"\n                       \"فرانسوی در فارسی «ـون» و «ـssi» آن «ـسی» شده است، درست مانند دیگر وام‌واژه‌های \"\n                       \"ـtion/-sion دار. ویکی‌واژه نیز می‌نویسد «وام‌گرفته از فرانسویِ commission». «کمیته» که \"\n                       \"در پرانتز آمده وام‌واژهٔ هم‌خانوادهٔ دیگری است از comité فرانسوی (که خود از committee \"\n                       \"انگلیسی گرفته شده و باز به mittere می‌رسد). لوکوچ نیز همین واژه را در ترکی به صورت \"\n                       \"komita (در komitadschi) ثبت کرده است. ادعای نورایی درست است.\"),\n     \"sources\": [W_KOM],\n     \"ref_check\": [\n       {\"ref\": \"MON:3079\", \"status\": \"not_checked\",\n        \"note\": \"tools/ref_page.py has no scan of Moʿin covering printed page 3079 ('no scan of MON covers printed page ...' for the neighbouring 5185 as well), and MON_part1/2.txt OCR of Persian script is unusable. Moʿin does mark French loans with [فر.] in the online text, and vajehyab/abadis carry کمیسیون, but the printed page could not be opened.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"Wiktionary\", \"where\": \"fa/کمیسیون\", \"stance\": \"supports\",\n        \"note\": \"'Borrowed from French commission'; senses 'fee charged by an agent or broker' and 'committee', synonym کمیته.\"},\n       {\"src\": \"LKT\", \"where\": \"LKT.txt line 1898\", \"stance\": \"partial\",\n        \"note\": \"Lokotsch s.v. Komitadschi: 'tk. komita == comité und Suffix -gi' — documents the same French comité entering the Islamic East, the sister-loan of the کمیته in the chart's parenthesis.\"},\n       {\"src\": \"ARY\", \"where\": \"grep 'کمیسیون' in incoming/ARY/ARY_pages.txt\", \"stance\": \"silent\",\n        \"note\": \"No entry — Aryanpur covers inherited Indo-European vocabulary, not modern European loans.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"English\",\n     \"words\": \"commit; emit; omit; remit; submit; admit; permit; transmit; mission; commission; committee; missile; promise\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"All thirteen are the Latin mittere family, reaching English partly through Old/Middle \"\n                    \"French and partly as direct learned Latin borrowings, and Klein's entry s.v. mission \"\n                    \"(p. 988) lists almost exactly this set as the words 'there referred to'. The -mit verbs \"\n                    \"come from the Latin present stem (committere 'to join, entrust' > commit; ēmittere > \"\n                    \"emit; omittere < *ob-mittere > omit; remittere > remit; submittere > submit; admittere > \"\n                    \"admit; permittere > permit; transmittere > transmit), the -mission nouns from the \"\n                    \"supine stem miss- (missiō, commissiō), and missile from missilis 'that may be thrown'. \"\n                    \"committee is an English formation in -ee on commit (17th c., one 'to whom something is \"\n                    \"committed'), and promise is Latin prōmissum / French promesse, from prōmittere 'to send \"\n                    \"forward' — the one word in the box that literally carries Nourai's gloss 'send \"\n                    \"forward'. The only caveat is inherited from node 4: whether this whole family goes back \"\n                    \"to *smeit- or to *meyth2- is disputed.\"),\n     \"derivation_fa\": (\"هر سیزده واژه از خانوادهٔ mittere لاتینی‌اند و بخشی از راه فرانسویِ کهن و میانه و بخشی \"\n                       \"همچون وام‌واژه‌های عالمانهٔ لاتینی به انگلیسی رسیده‌اند؛ کلاین در مدخل mission (ص ۹۸۸) \"\n                       \"تقریباً همین فهرست را می‌آورد. فعل‌های ـmit از ستاک مضارع لاتینی‌اند (committere، \"\n                       \"ēmittere، omittere، remittere، submittere، admittere، permittere، transmittere)، \"\n                       \"نام‌های ـmission از ستاک مفعولیِ miss-، و missile از missilis «افکندنی». committee \"\n                       \"ساختی انگلیسی با پسوند ـee بر پایهٔ commit است (سدهٔ هفدهم) و promise از prōmissum \"\n                       \"لاتینی/promesse فرانسوی، از prōmittere «پیش‌فرستادن» — تنها واژه‌ای که معنیِ «send \"\n                       \"forward» نورایی را عیناً در خود دارد. تنها احتیاط همان است که در خانهٔ لاتینی گفته شد: \"\n                       \"بازگشت این خانواده به *smeit- یا به *meyth₂- مورد اختلاف است. ادعای نورایی درست است.\"),\n     \"sources\": [ETY_MISSION, W_MITTO],\n     \"ref_check\": [\n       {\"ref\": \"AHD\", \"status\": \"supports\",\n        \"note\": \"AHD_watkins1985.txt line 958 under (s)meit(e)-: 'MASS, MESS, MESSAGE, MISSILE, MISSION, MISSIVE, MITTIMUS; ADMIT, COMMIT, (COMPROMISE), DEMIT, DISMISS, EMIT, INTERMIT, INTROMIT, OMIT, PERMIT, PREMISE, PRETERMIT, PROMISE, REMIT, SUBMIT, SURMISE, TRANSMIT' — Nourai's list is a subset.\"},\n       {\"ref\": \"KLN:988\", \"status\": \"supports\",\n        \"note\": \"KLN_1966.txt line 24047 (leaf 530 = printed p. 988) s.v. mission: 'L. missio ... fr. missus, pp. of mittō, mittere ... cp. admission, admit, commissariat, commission, commit, committee, compromise, ... emission, emit, ... omission, omit, permission, permit' — the cited page carries the whole family.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"KLN_1966.txt lines 8381 (commit), 24047 (mission), 30502 (promise), 39872 (transmit)\", \"stance\": \"supports\",\n        \"note\": \"s.v. promise: 'ME. promis, partly fr. L. promissum ... L. promittere is formed fr. pro- and mittere, to send' — exactly the 'send forward' sense.\"},\n       {\"src\": \"SKT\", \"where\": \"SKT.txt line 11705\", \"stance\": \"supports\",\n        \"note\": \"s.v. mission: 'L. acc. missionem ... L. missus, pp. of mittere, to send'.\"},\n       {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/mission\", \"stance\": \"partial\",\n        \"note\": \"Same word-family, but roots it in PIE *m(e)ith- 'to exchange, remove', not in *smeit-.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nout=\"/home/sfmqrb/git/rishe/data/verification/page-460.json\"\nwith io.open(out,\"w\",encoding=\"utf-8\") as f:\n    json.dump(data,f,ensure_ascii=False,indent=2)\n    f.write(\"\\n\")\nprint(\"written\",out)\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build460.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-460.json > /dev/null && echo JSON_OK"
}
```


### [2026-09-14T02:42:36.270Z] TOOL RESULT

```
written /home/sfmqrb/git/rishe/data/verification/page-460.json
JSON_OK
```


## [2026-09-14T02:42:39.212Z] TOOL CALL #71: Bash

```json
{
 "command": "python3 tools/verify_check.py 460"
}
```


### [2026-09-14T02:42:40.219Z] TOOL RESULT

```
nodes verified: 14/14
node verdicts: {'confirmed': 8, 'plausible': 3, 'disputed': 2, 'transcription_suspect': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 11, 'not_checked': 4, 'partial': 4}
books consulted: {'supports': 24, 'silent': 11, 'partial': 6, 'contradicts': 4} | by book: {'KLN': 6, 'Wiktionary': 5, 'MON': 3, 'ARY': 3, 'FVQ': 3, 'SKT': 3, 'AFM': 2, 'PHD': 2, 'HRN': 2, 'Etymonline': 2, 'PLA': 1, 'BQT': 1, 'FSD': 1, 'BRT': 1, 'CHEUNG': 1, 'WLD': 1, 'AVG': 1, 'NYB': 1, 'Encyclopaedia Iranica / CAIS': 1, 'POK': 1, 'LAT': 1, 'Etymonline / de Vaan': 1, 'IEC': 1, 'LKT': 1}
```


## [2026-09-14T02:42:56.653Z] AGENT

Page 460 (book p. 430) verified — `/home/sfmqrb/git/rishe/data/verification/page-460.json`, `verify_check.py 460` reports 0 PROBLEM lines.

**Counts** — roots: 2 confirmed. Nodes 14/14: 8 confirmed, 3 plausible, 2 disputed, 1 transcription_suspect. Ref checks: 11 supports, 4 partial, 4 not_checked. Books consulted: 24 supports, 6 partial, 4 contradicts, 11 silent.

**disputed**
- *Smeit* → Pahlavi `hamēstagān` (and its Persian reflex `hamīstakân`): MacKenzie's own addenda put "limbo" under a separate headword `hamēst` "whose good and bad deeds weigh equal", and Humbach/Klingenschmitt tie it to Av. `hə̄miiasaite` (Y 33.1) "reckoned together", not to ham- + maēθ- "throw down". The other word in each box (`hamēstār`/`hamīstar` "adversary" ← Av. `hamaēstar-`) is solidly confirmed by Nyberg, Horn 279 and Bartholomae col. 1774, so the node takes the worse verdict.

**transcription_suspect**
- *Smeit* → Latin "mithere": the printed page really reads `mithere` (300-dpi render filed at `data/verification/sources/refs/ocr/BOOK/460.png`), so this is Nourai's misprint for `mittere`; the extraction is faithful. `error_in: "book"`. Separately, the derivation of Latin mittō from *smeit- is only plausible: Pokorny 968, Watkins ("possibly"), Cheung and Ernout–Meillet back it; de Vaan/Etymonline prefer *meyth₂-.

**Extraction errors for the owner to fix**
- Entry 0, node 6 (Persian `Šam`ŭn` شمعون): `data/extracted/batch/page-460.json` gives `refs: "MON"`, but the printed box header is bare "Persian" with no reference icon. The ref should be `null`.

Other notes carried in the file: Nourai's Pahlavi gloss "awkward situation" for `hamēstagān` is wrong (it is the eschatological intermediate place — his own Persian box glosses it correctly); Ismāʿīl and Šamʿūn reached Arabic/Persian via Syriac, not straight from Hebrew (Jeffery FVQ pp. 63-64); the Semitic root is properly *šamaʿ- with *š, Nourai citing it in its Arabic shape. `FVA:197`, `MON:5185` and `MON:3079` could not be checked (no digital copy / no scan covering those pages / unusable Persian OCR).
